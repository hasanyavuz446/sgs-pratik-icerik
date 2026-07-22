#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS içerik yapısı ve mekanik kalite denetimi.

Bu araç yalnız SGS `{ders, konu, stem, options, answer, solution}` şemasını ve
manifestte `programIds=["sgs"]` olarak kayıtlı paketleri kabul eder. SMMM'ye özgü
soru tipi kotalarını uygulamaz.
"""
from __future__ import annotations

import collections
import difflib
import json
import os
import re
import sys


LETTERS = set("ABCDE")
DEMO = re.compile(r"demo\s+(?:soru|açıklama)", re.IGNORECASE)
# "Doğru cevap B." — büyük harf + sınır ara. `re.I` ile aramak "Doğru seçenek bu…"
# içindeki b'yi cevap harfi sanar.
SOLUTION_LETTER = re.compile(r"Doğru\s+(?:cevap|seçenek)\s+([A-E])\b")
# Uygulamada geçmişte seçeneklerin başında ham "```text" görünmüştü. Kod çiti
# içerik şemasının değil render katmanının işaretidir ve kullanıcıya taşınamaz.
DISPLAY_CODE_FENCE = re.compile(r"```(?:\s*(?:text|plain|plaintext))?", re.IGNORECASE)
CURRENT_SGS_YEAR = 2026
SHORT_STEM_EXEMPT_LESSONS = {"matematik", "yabanci_dil"}
NUMERIC_LEGISLATION_LESSONS = {
    "vergi_hukuku",
    "meslek_hukuku",
    "is_ve_sosyal_guvenlik_hukuku",
    "ticaret_hukuku",
    "borclar_hukuku",
    "maliye",
    "muhasebe_standartlari",
    "denetim",
}

# Çeldiricileri şişirmek için kullanılan dolgu kalıpları. Yalnız çeldiricilerde
# görünürlerse kalıbın kendisi güvenilir bir "yanlış" işaretine dönüşür.
DOLGU = re.compile(r"(zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır)", re.I)
# Öncüllü (I/II/III "hangileri") sorularda şık boyu doğal olarak eşit → boy ölçümü dışı.
ONCUL = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")


def kor_ogrenci(questions: list[dict]) -> tuple[int, str]:
    """Soruyu HİÇ OKUMADAN alınabilen EN İYİ puan (%) ve onu veren strateji.

    ⚠ Ölçüt İKİ YÖNLÜ olmalı. İlk sürümü yalnız "en kısayı seç" deniyordu ve
    "doğru hep en UZUN" yazılmış dersleri temiz gösteriyordu; oysa öğrencinin
    öğreneceği kural hangi yönde olursa olsun aynı derecede zararlıdır.

    ⚠⚠ TABAN %20 DEĞİL, ~%23. Dört stratejinin EN İYİSİ alındığı için şans
    kayırılır. 60 soruluk tamamen rastgele paketlerle ölçüldü (400 deneme):
    ortalama %23, %5–%95 aralığı %16–%30, en yüksek %38. Bu yüzden:
      · %35 FATAL  → rastgele paketlerin yalnız %1'i aşar; kalibre.
      · %31 UYARI  → 95. yüzdelik. (Önce %28 demiştim; rastgelenin %14'ü
                     aşıyordu, yani her yedi temiz dosyadan biri boşuna
                     uyarı alacaktı — gürültü, uyarıyı önemsizleştirir.)
    Hedef "~%20" yazmak da yanlıştı: ulaşılamaz. Gerçekçi hedef ≤%30.
    """
    if not questions:
        return 0, "-"

    def uzun(o):
        return {max(o, key=lambda k: (len(o[k]), k))}

    def kisa(o):
        return {min(o, key=lambda k: (len(o[k]), k))}

    def dolgusuz(o):
        return {k: v for k, v in o.items() if not DOLGU.search(v)} or o

    def ortadakiler(o):
        enb, enk = max(len(v) for v in o.values()), min(len(v) for v in o.values())
        return {k for k in o if enk < len(o[k]) < enb} or set(o)

    # Her strateji bir ADAY KÜMESİ döndürür; puan = küme doğruyu içeriyorsa 1/|küme|.
    # ⚠ Çerçeve önce tek şık seçiyordu ve "daraltma" stratejilerini modelleyemiyordu:
    # aday iki ucu eleyip 3 şıkta kalırsa %33 eder (taban %20), ama tek-şık çerçevesi
    # bunu göremez. emlak_vergisi'nde boy dengelerken doğru şıkkı sistematik olarak
    # ortaya itmiştim (%0 en uzun / %0 en kısa) — yani bir ipucunu düzeltirken daha
    # küçük bir yenisini üretmiştim ve ölçüt kördü.
    stratejiler = {
        "en kısayı seç": kisa,
        "en uzunu seç": uzun,
        "dolguluyu ele, en kısayı seç": lambda o: kisa(dolgusuz(o)),
        "dolguluyu ele, en uzunu seç": lambda o: uzun(dolgusuz(o)),
        "iki ucu ele, ortadan tahmin et": ortadakiler,
    }
    en_iyi = (0, "-")
    for ad, sec in stratejiler.items():
        beklenen = 0.0
        for question in questions:
            aday = sec(question["options"])
            if question["answer"] in aday:
                beklenen += 1 / len(aday)
        puan = int(beklenen * 100 / len(questions))
        if puan > en_iyi[0]:
            en_iyi = (puan, ad)
    return en_iyi


def metin(value: str, *, sablon: bool = False) -> str:
    """Ölçüm için düz metin. `sablon=True` ise sayıları `#` ile maskeler."""
    value = re.sub(r"[`*_]", "", str(value or "")).strip().casefold()
    if sablon:
        value = re.sub(r"\b\d[\d.,]*\b", " # ", value)
    return " ".join(re.findall(r"[\wçğıöşü#]+", value, flags=re.UNICODE))


def cevap_metni(value: str) -> str:
    """Cevap karşılaştırması için normalleştirme — İŞARETLERİ KORUR.

    ⚠ Burada `metin()` KULLANILAMAZ: o, sözcük olmayan her karakteri atar ve
    “−%10” ile “%10” ikisini birden “10” yapar — biri azalış, öteki artış olduğu
    hâlde. Bu, karsilastirmali_analiz'de 4 sahte klon üretmişti.
    """
    return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", str(value or ""))).strip().casefold()


def soru_sablonu(question: dict) -> tuple:
    """Kök + şık kümesinin sayıları maskelenmiş iskeleti."""
    return (metin(question["stem"], sablon=True),
            tuple(sorted(metin(v, sablon=True) for v in question["options"].values())))


def jaccard(a: str, b: str) -> float:
    left, right = set(a.split()), set(b.split())
    return len(left & right) / len(left | right) if left and right else 0.0


def oncul_dagilimi(questions: list[dict]) -> list[tuple[str, str]]:
    """Öncüllü (I/II/III "hangileri") sorularda doğru cevap hangi bileşimde?

    ⚠⚠ BU KONTROL, DEDEKTÖRE YAZILMAYAN DÜZELTMENİN GERİ GELDİĞİNİ GÖSTERDİĞİ
    İÇİN VAR. Daha önce "hepsi" (I, II ve III) cevabı %75'e çıkmıştı; 266 soruyu
    elle düzeltip %18'e indirdim ama kuralı yalnız kafamda tuttum, araca
    yazmadım. Sonra üretilen muhasebe_standartlari'nda kusur AYNEN geri geldi,
    yalnız kılık değiştirdi: 155 öncüllü sorunun %65'inde cevap «I ve II».
    "Hepsi"den kaçarken yerine yeni bir sabit koymuşum. Öğrenci açısından fark
    yok — okumadan «I ve II» işaretleyen %65 alır.

    Bu yüzden ölçüt TEK BİR BİLEŞİME değil, DAĞILIMA bakar: beş seçenekli bir
    öncül sorusunda düzgün dağılım her bileşim için ~%20'dir; herhangi biri
    baskınsa hangisi olduğunun önemi yoktur.

    ⚠ EŞİK ULAŞILABİLİR OLANA GÖRE. Önce %35 demiştim; ölçünce gördüm ki bu,
    mevcut soru TASARIMINDA ulaşılamaz bir hedef: bütün öncüllü sorularda üç
    öncülün tam ikisi doğru yazılmış, yani cevap ancak 4 bileşimden biri olabilir.
    8 soruyu üç iki'li bileşime dağıtınca en iyi ihtimal 3/3/2 = %37 — yani
    kusursuz dengelenmiş bir dosya bile %35 eşiğinde uyarı alıyordu. Ulaşılamaz
    hedefe göre uyarı vermek, uyarıyı değersizleştirir. Eşik: ≥%50 FATAL,
    ≥%40 UYARI.

    ⚠ ASIL KUSUR DAĞILIMDA DEĞİL, TASARIMDA — bu yüzden ayrıca ölçülür: 51
    dosyanın 50'sinde "Yalnız X" şıkkı HİÇ doğru cevap değil (416 soru). Öğrenci
    "Yalnız" ile başlayan iki şıkkı okumadan eler; taban %20 değil %33 olur.
    Çaresi permütasyon değil İÇERİK: tek öncülü doğru soru yazmak.
    """
    oncullu = [q for q in questions if len(ONCUL.findall(q["stem"])) >= 2]
    if len(oncullu) < 6:
        return []
    issues: list[tuple[str, str]] = []
    tekli = re.compile(r"^\s*yalnız\s+(i{1,3}|iv|v)\s*$", re.I)
    varsa = any(tekli.match(re.sub(r"\s*\([^)]*\)", "", v)) for q in oncullu
                for v in q["options"].values())
    dogruysa = any(tekli.match(re.sub(r"\s*\([^)]*\)", "", q["options"][q["answer"]]))
                   for q in oncullu)
    if varsa and not dogruysa:
        issues.append(("UYARI", f"“Yalnız X” şıkkı {len(oncullu)} öncüllü sorunun hiçbirinde "
                                "doğru değil — öğrenci iki şıkkı okumadan eler (taban %20 → %33); "
                                "tek öncülü doğru soru yazılmalı"))

    # ⚠ ÖLÇÜT YÜZDE DEĞİL, GERÇEK İSTİSMAR (fazladan bedava soru sayısı).
    # Salt yüzde küçük örnekte yanıltıyor: tfrs_9'da yalnız 8 öncüllü soru var ve
    # şablon "tam 2 öncül doğru + {Yalnız I, Yalnız III, I ve II, II ve III,
    # hepsi}" olduğundan ulaşılabilir 2'li bileşim sadece ikidir — permütasyon en
    # iyi %50 verir, yani kusursuz dengelenmiş bir dosya bile "%50 → FATAL"
    # alıyordu. Ama 4/60 soru, öğrencinin bütün testte kazandığı ~2 fazladan puan
    # demek; dosyanın kör-öğrenci skoru (%23) bundan etkilenmiyor.
    #
    # Doğru ölçü: fazla = baskın bileşimin adedi − rastgele beklenti (öncül/5).
    # Bu, "okumadan işaretleyen kaç FAZLADAN soru kazanır"ı verir; dosya boyutuna
    # ve öncül sayısına göre kendiliğinden ölçeklenir. Genel bias hâlâ yakalanır
    # (30 öncüllü soruda 20 baskınsa fazla=14 → FATAL), küçük örnek bloke olmaz.
    dagilim = collections.Counter(
        re.sub(r"\s+", " ", q["options"][q["answer"]]).strip().casefold() for q in oncullu
    )
    metin, adet = dagilim.most_common(1)[0]
    fazla = adet - len(oncullu) / 5  # rastgele beklentinin üstündeki fazlalık
    if fazla >= 3:
        oran = adet * 100 // len(oncullu)
        kalanlar = ", ".join(f"“{t}” %{n * 100 // len(oncullu)}"
                             for t, n in dagilim.most_common()[1:3])
        issues.append(("FATAL" if fazla >= 5 else "UYARI",
                       f"öncüllü soruların %{oran}'inde cevap “{metin}” "
                       f"({adet}/{len(oncullu)}, ~{fazla:.0f} fazladan) — okumadan işaretlenir"
                       f"{'; sonraki: ' + kalanlar if kalanlar else ''}"))
    return issues


def tekrar_sorunlari(questions: list[dict]) -> list[tuple[str, str]]:
    """Şablon klonu, çözüm tekrarı ve yakın-tekrar.

    ⚠ Alıştırma ↔ klon ayrımı. SMMM'nin denetimi "aynı şablon = FATAL" der; SGS'de
    bu kural olduğu gibi uygulanamaz, çünkü matematik alıştırmasında kök zaten
    şablondur ("#x + # = # denkleminin çözümü kaçtır?") ve 52 meşru soruyu birden
    yakar. Ayrımı HAM cevap kuruyor:
      · aynı şablon + FARKLI cevap → alıştırma; mekanik beceride istenen şeydir.
      · aynı şablon + AYNI cevap   → kopya; aynı işlemi aynı sonuçla iki kez sorar
        (trend_analizi'nde 600.000/500.000 ve 960.000/800.000 → ikisi de %120).
    """
    issues: list[tuple[str, str]] = []
    # şablon → {cevap: ilk soran id}. ⚠ Şablon başına yalnız İLK soruyu tutmak
    # yetmez: iskelet aynı, ilk soru %20, sonraki ikisi %10 ise o ikisi hiç
    # karşılaştırılmaz ve klon kaçar. İlk sürümüm böyleydi; 20 klon raporladı,
    # cevap bazında tutunca gerçek sayı çıktı.
    sablonlar: dict[tuple, dict[str, str]] = {}
    cozumler: dict[str, str] = {}
    coz_sablon: dict[str, str] = {}

    for question in questions:
        qid = str(question.get("id") or "<idsiz>")
        cevap = cevap_metni(question["options"][question["answer"]])

        anahtar = soru_sablonu(question)
        gorulen = sablonlar.setdefault(anahtar, {})
        if cevap in gorulen:
            issues.append(("FATAL", f"{qid}: {gorulen[cevap]} ile aynı şablon VE aynı cevap "
                                    "— sayı değişmiş ama sorulan işlem ve sonuç aynı"))
        else:
            gorulen[cevap] = qid

        cozum = metin(re.sub(r"\s*Doğru cevap [A-E]\.\s*$", "", question["solution"]))
        if len(cozum) >= 45:
            if cozum in cozumler:
                issues.append(("FATAL", f"{qid}: çözüm {cozumler[cozum]} ile birebir aynı"))
            else:
                cozumler[cozum] = qid
        cs = metin(re.sub(r"\s*Doğru cevap [A-E]\.\s*$", "", question["solution"]), sablon=True)
        if len(cs) >= 60:
            if cs in coz_sablon and cozum not in cozumler:
                issues.append(("UYARI", f"{qid}: çözüm yalnız sayı değişimiyle "
                                        f"{coz_sablon[cs]} ile aynı şablona düşüyor"))
            coz_sablon.setdefault(cs, qid)

    # Yakın-tekrar pahalıdır; ucuz jaccard ön-elemesinden geçenlere difflib uygulanır.
    birlesik = [(q, " | ".join((soru_sablonu(q)[0], *soru_sablonu(q)[1]))) for q in questions]
    for i, (sol, sol_metin) in enumerate(birlesik):
        if len(sol_metin) < 100:
            continue
        for sag, sag_metin in birlesik[i + 1:]:
            if len(sag_metin) < 100 or soru_sablonu(sol) == soru_sablonu(sag):
                continue  # şablon eşitliği zaten yukarıda değerlendirildi
            j = jaccard(sol_metin, sag_metin)
            if j < 0.80:
                continue
            r = difflib.SequenceMatcher(None, sol_metin, sag_metin, autojunk=False).ratio()
            if r >= 0.97 and j >= 0.90:
                issues.append(("UYARI", f"{sag['id']}: {sol['id']} ile çok yüksek benzerlik "
                                        f"(dizi %{r*100:.0f}, sözcük %{j*100:.0f}) — elle karşılaştır"))
    return issues


def guncellik_sorunlari(questions: list[dict]) -> list[tuple[str, str]]:
    """Sayısal mevzuat bilgisinin yıl ve kaynak çıpası.

    Gerçek SGS; süre, ceza, artırım oranı ve parasal sınırı doğrudan sorabilir.
    Denetimin görevi bunu yasaklamak değil, bayatlayabilecek sayıyı yıl ve birincil
    kaynak olmadan yayıma sokmamaktır.

    ⚠ İnce ayrım:
      · Oranın soru KÖKÜNDE verilmesi GÜVENLİDİR — "5.000 ₺ + %20 KDV" kayıt
        becerisini ölçer; oran değişse de soru kendi içinde tutarlı kalır.
      · Cevabın oran olması tek başına ihlal değildir: türetilmiş oran, TDHP'nin
        yapısal sınırı ve "cari oran" adlı finansal rasyo ayrı değerlendirilir.

    Regex yalnız bariz sayısal mevzuat sorularını yakalar; semantik doğruluk insan
    incelemesindedir.
    """
    issues: list[tuple[str, str]] = []
    oran = re.compile(r"%\s?\d+(?:[,.]\d+)?|\d+(?:[,.]\d+)?\s?%")
    ciplak_oran = re.compile(r"^\s*%\s?\d+(?:[,.]\d+)?\s*$")
    ciplak_sayisal = re.compile(
        r"^\s*(?:%\s*)?\d+(?:[.,]\d+)?(?:\s*(?:%|gün|ay|yıl|kat|₺|tl))?\s*$",
        re.I,
    )
    mevzuat_orani = re.compile(
        r"\b(kdv|katma değer|özel tüketim|ötv|gelir vergisi|kurumlar vergisi|stopaj|"
        r"tevkifat|damga vergisi|gecikme zammı|gecikme faizi|yeniden değerleme|"
        r"asgari ücret|harç)\b", re.I)
    sayisal_mevzuat = re.compile(
        r"\b(süre|ceza|artırım|zam|oran|had|sınır|sermaye|ibraz|başvuru|bildirim|"
        r"beyan|ödeme|zamanaşımı|hapis|para cezası|gecikme|vergi|harç)\b",
        re.I,
    )
    # ⚠ "cari" BİLEREK dışarıda: Türkçe muhasebede "cari oran" = current ratio
    # (Dönen Varlıklar ÷ KVYK), bir rasyonun adıdır — "hâlihazırda geçerli oran"
    # değil. Kalıba dâhil edince Mali Tablolar Analizi'nin en temel terimi 10 kez
    # mevzuat ihlali sanıldı. "Cari dönem" de aynı biçimde masumdur.
    ortuk = re.compile(r"(yürürlükteki|güncel)\s+"
                       r"(oran|had|tutar|tarife|orandan|oranda)", re.I)
    yil = re.compile(r"\b20\d{2}\b")
    for question in questions:
        qid = str(question.get("id") or "<idsiz>")
        kok = question["stem"]
        cevap = question["options"][question["answer"]]
        ders = str(question.get("ders") or "")
        try:
            valid_year = int(question.get("validYear"))
        except (TypeError, ValueError):
            valid_year = None
        source = question.get("source") if isinstance(question.get("source"), dict) else {}
        ref = str(source.get("legislationRef") or "").strip()

        direct_rate = (ciplak_oran.match(cevap) and mevzuat_orani.search(kok)
                       and not oran.search(kok))
        direct_numeric = (ciplak_sayisal.match(cevap) and sayisal_mevzuat.search(kok)
                          and (ders in NUMERIC_LEGISLATION_LESSONS
                               or mevzuat_orani.search(kok)))
        if direct_rate or direct_numeric:
            if valid_year is None:
                issues.append(("UYARI", f"{qid}: doğrudan sayısal mevzuat cevabı "
                                        f"(“{cevap.strip()}”) `validYear` olmadan yayımlanamaz"))
            elif valid_year < CURRENT_SGS_YEAR:
                issues.append(("UYARI", f"{qid}: sayısal mevzuat cevabının `validYear` "
                                        f"değeri {valid_year}; {CURRENT_SGS_YEAR} için yeniden doğrula"))
            if not ref:
                issues.append(("UYARI", f"{qid}: sayısal mevzuat cevabının madde/fıkra "
                                        "düzeyinde dayanağı yok"))

        if (ortuk.search(kok) and not (oran.search(kok) or yil.search(kok))
                and valid_year is None):
            issues.append(("UYARI", f"{qid}: kök dönem/oran vermeden "
                                    f"“{ortuk.search(kok).group(0)}” diyor ve `validYear` yok"))
    return issues


def kok_profili(questions: list[dict]) -> tuple[int, int]:
    """(çıplak kök %, medyan kök uzunluğu) — paket genelinde tanım sorusu yığılması."""
    uzunluklar = sorted(len(metin(q["stem"])) for q in questions)
    if not uzunluklar:
        return 0, 0
    ciplak = sum(1 for u in uzunluklar if u < 60)
    return ciplak * 100 // len(uzunluklar), uzunluklar[len(uzunluklar) // 2]


def boy_egilimi(questions: list[dict]) -> tuple[int, int, int]:
    """(en-uzun%, en-kısa%, ölçülen) — doğru şıkkın boy sıralamasındaki yeri.

    İkisi de ~%20 olmalı. Biri baskınsa boy ipucu vardır; YÖNÜ ÖNEMSİZ —
    "doğru hep en uzun" kadar "doğru hep en kısa" da okumadan çözdürür.
    """
    olcum = [q for q in questions if len(ONCUL.findall(q["stem"])) < 2]
    if not olcum:
        return 0, 0, 0
    uzun = kisa = 0
    for question in olcum:
        lengths = [len(v) for v in question["options"].values()]
        answer_length = len(question["options"][question["answer"]])
        # Eşit uzunluktaki şıklar bir tahmin kuralı vermez. Beş sayısal
        # seçeneğin de iki basamaklı olduğu bir soruda doğru seçenek teknik
        # olarak hem en uzun hem en kısadır; ancak öğrenci uzunluğa bakarak onu
        # diğerlerinden ayıramaz. Yalnızca TEK BAŞINA uçta olan doğru şık sayılır.
        uzun += answer_length == max(lengths) and lengths.count(max(lengths)) == 1
        kisa += answer_length == min(lengths) and lengths.count(min(lengths)) == 1
    return uzun * 100 // len(olcum), kisa * 100 // len(olcum), len(olcum)


def load(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    return data if isinstance(data, list) else data.get("questions", [])


def letter_pattern(sequence: str) -> bool:
    if len(sequence) < 10:
        return False
    for period in range(1, min(11, len(sequence))):
        compared = len(sequence) - period
        matches = sum(sequence[i] == sequence[i + period] for i in range(compared))
        if compared and matches / compared >= 0.9:
            return True
    return False


def audit(path: str) -> tuple[int, list[tuple[str, str]]]:
    questions = load(path)
    issues: list[tuple[str, str]] = []
    ids: set[str] = set()
    stems: set[str] = set()
    answers = []

    for index, question in enumerate(questions, 1):
        qid = str(question.get("id") or f"#{index}")
        if qid in ids:
            issues.append(("FATAL", f"yinelenen id: {qid}"))
        ids.add(qid)

        required = ("ders", "konu", "stem", "options", "answer", "solution")
        missing = [field for field in required if not question.get(field)]
        if missing:
            issues.append(("FATAL", f"{qid}: eksik alan: {', '.join(missing)}"))
            continue

        stem = re.sub(r"\s+", " ", question["stem"]).strip().casefold()

        options = question["options"]
        if not isinstance(options, dict) or set(options) != LETTERS:
            issues.append(("FATAL", f"{qid}: seçenekler tam A–E değil"))
            continue
        if any(not isinstance(value, str) or not value.strip() for value in options.values()):
            issues.append(("FATAL", f"{qid}: boş seçenek var"))
        normalized = {re.sub(r"\s+", " ", value).strip().casefold() for value in options.values()}
        if len(normalized) != 5:
            issues.append(("FATAL", f"{qid}: yinelenen seçenek var"))

        # Kopya ölçütü kök DEĞİL, kök + şık kümesidir. Genel kökler ("Aşağıdakilerden
        # hangisi ... değildir?") farklı şıklarla meşru olarak tekrar eder; yalnız köke
        # bakmak 16 pakette 43 sahte FATAL üretiyordu. Şıklar küme olarak alındığından
        # harf permütasyonuyla çoğaltılmış gerçek kopya da yakalanır.
        signature = (stem, frozenset(normalized))
        if signature in stems:
            issues.append(("FATAL", f"yinelenen soru (kök ve şıklar aynı): {qid}"))
        stems.add(signature)

        answer = question["answer"]
        if answer not in options:
            issues.append(("FATAL", f"{qid}: cevap seçeneklerde değil"))
        else:
            answers.append(answer)

        visible = " ".join((question["stem"], *options.values(), question["solution"]))
        if DEMO.search(visible):
            issues.append(("FATAL", f"{qid}: kullanıcıya görünen demo ifadesi"))
        if DISPLAY_CODE_FENCE.search(visible):
            issues.append(("FATAL", f"{qid}: kullanıcıya görünecek ham kod çiti/format etiketi"))

        # Çözümdeki harf atfı, şık harfleriyle kırılgan biçimde eşleşir: harf ataması
        # sonradan değişince çözüm sessizce yanlış kalır (bir konuda 46 soru böyle
        # bozulmuştu). Hedef harf ATIFSIZ çözüm; atıf varsa hiç değilse tutarlı olmalı.
        harf = SOLUTION_LETTER.search(question["solution"])
        if harf and harf.group(1) != answer:
            issues.append(("FATAL", f"{qid}: çözüm “{harf.group(1)}” diyor, cevap “{answer}”"))

        source = question.get("source")
        if not isinstance(source, dict) or not str(source.get("legislationRef", "")).strip():
            issues.append(("UYARI", f"{qid}: kaynak/dayanak eksik"))

    sequence = "".join(answers)
    if letter_pattern(sequence):
        issues.append(("FATAL", "cevap harflerinde kısa periyot/örüntü var"))
    if len(sequence) >= 20:
        counts = collections.Counter(sequence)
        expected = len(sequence) / 5
        # Beklenen değer bir kota değildir. 60 soruda 13/13/12/11/11 gibi doğal
        # sapmalar kabul edilir; yalnız adayın fark edebileceği belirgin yığılma
        # uyarılır. Kısa periyot ve rotasyon yukarıda ayrı olarak FATAL'dir.
        if any(abs(counts[letter] - expected) > max(2, expected * 0.35) for letter in "ABCDE"):
            issues.append(("UYARI", f"cevap harfi dağılımı dengesiz: {dict(counts)}"))

    # Şıklardan sızan örüntü. Harf dizisi kusursuz olsa bile şıkların KENDİSİ
    # cevabı ele verebilir; eski dedektör yalnız "doğru şık en uzun mu" bakıp
    # bunu kaçırıyordu (Muhasebe Standartları'nda kör öğrenci %54 alıyordu).
    saglam = [q for q in questions
              if isinstance(q.get("options"), dict) and set(q.get("options", {})) == LETTERS
              and q.get("answer") in q.get("options", {})]
    # Kopya ve güncellik soru/çift düzeyinde ölçülür → örneklem eşiği YOK.
    # (Bu kontroller önce "≥20 soru" kapısının içindeydi; gerçek paketler 60 soruluk
    # olduğu için üretimde fark etmiyordu ama küçük dosyada sessizce atlanıyordu.)
    issues.extend(tekrar_sorunlari(saglam))
    issues.extend(oncul_dagilimi(saglam))
    issues.extend(guncellik_sorunlari(saglam))

    # Aşağıdakiler İSTATİSTİKSEL; küçük örneklemde gürültü olur.
    if len(saglam) >= 20:
        ciplak, medyan = kok_profili(saglam)
        dersler = {str(q.get("ders") or "") for q in saglam}
        # Matematikte kısa formül kökü, yabancı dilde kısa cümle/kelime kökü gerçek
        # sınavın doğal biçimidir. Karakter sayısı bu iki derste bilişsel yük ölçmez.
        if ciplak >= 60 and not dersler.intersection(SHORT_STEM_EXEMPT_LESSONS):
            issues.append(("UYARI", f"kök profili: soruların %{ciplak}'i çıplak/kısa tanım "
                                    f"(medyan {medyan} karakter); SGS uygulama ve yorum ölçer"))

        kor, strateji = kor_ogrenci(saglam)
        if kor >= 35:
            issues.append(("FATAL", f"kör öğrenci soruyu okumadan %{kor} alıyor "
                                    f"(rastgele taban ~%23) — strateji: “{strateji}”"))
        elif kor >= 31:
            issues.append(("UYARI", f"kör öğrenci %{kor} alıyor (rastgele taban ~%23) "
                                    f"— “{strateji}”"))

        uzun, kisa, olcum = boy_egilimi(saglam)
        if olcum >= 20 and max(uzun, kisa) >= 45:
            yon = "en UZUN" if uzun >= kisa else "en KISA"
            issues.append(("UYARI", f"boy ipucu: doğru şık %{max(uzun, kisa)} oranında {yon} "
                                    f"({olcum} öncüllü-olmayan soruda; hedef ~%20)"))

        # Aynı çeldiricinin dosya boyunca tekrarı ("bu husus standartta düzenlenmemiştir"
        # gibi atma-şıkları): her seferinde yanlış olduğu için tek başına öğrenilir.
        # Öncül seçicileri ("Yalnız I", "II ve III") meşru olarak tekrar eder — sayma.
        #
        # ⚠ UZUNLUK EŞİĞİ ŞART. Eşiksiz ilk sürüm matematik'te “12”yi atma-şıkkı
        # sandı: sayısal şıklar (“12”, “400.000 TL”) doğal olarak tekrar eder ve
        # hiçbir şey ele vermez — ipucu ancak metin bir İDDİA taşıyorsa doğar.
        #
        # ⚠ “hep yanlış” İDDİASI ÖLÇÜLMELİ, varsayılmamalı: metin bir soruda doğru
        # bir başkasında çeldiriciyse öğrenilebilir kural YOKTUR. İlk sürüm yalnız
        # çeldirici geçişlerini sayıyor, doğru geçişlerine hiç bakmıyordu.
        #
        # ⚠ most_common(3) YETMEZ: tms_40'ta bu ailenin 45 üyesi var, ilk üçü
        # göstermek kusurun boyunu gizliyordu. Aile üye üye değil, TOPLAM raporlanır.
        # ⚠ PARANTEZİ KIRP, sonra ölç. Atma-şıkkı bir CÜMLE iddiasıdır ("…standartta
        # düzenlenmemiştir") ve parantezsiz de uzundur. Buna karşılık öncül seçicileri
        # ve kategori cevapları çoğu kez açıklayıcı bir parantez taşır:
        #   "Yalnız I (yalnızca birinci ifade doğrudur)"  → öncül seçicisi
        #   "devletçilik (ekonomide devlete öncü rol veren ilke)" → kategori cevabı
        # Parantez, hem >40 uzunluk eşiğini hem secici eşleşmesini atlatıp bunları
        # sahte-FATAL yapıyordu (maliye, iş hukuku, atatürk, vergi…). Çekirdeği
        # (parantezsiz) ölçünce ikisi de elenir: kısa kalır ya da secici'ye uyar.
        secici = re.compile(r"^(yalnız\s+)?(i{1,3}|iv|v)(\s*(,|ve)\s*(i{1,3}|iv|v))*$", re.I)
        nerede: dict[str, list[bool]] = {}
        for q in saglam:
            for k, v in q["options"].items():
                cekirdek = re.sub(r"\s*\([^)]*\)", "", re.sub(r"\s+", " ", v)).strip()
                if len(cekirdek) <= 40 or secici.match(cekirdek):
                    continue
                nerede.setdefault(re.sub(r"\s+", " ", v).strip().casefold(),
                                  []).append(k == q["answer"])
        for metin, gecisler in sorted(nerede.items(), key=lambda t: -len(t[1]))[:5]:
            adet = len(gecisler)
            if any(gecisler) or adet < max(5, len(saglam) * 0.08):
                continue
            duzey = "FATAL" if adet >= max(8, len(saglam) * 0.15) else "UYARI"
            issues.append((duzey, f"atma-şıkkı {adet} kez tekrarlanmış (hepsinde yanlış) "
                                  f"— standardı bilmeden elenir: “{metin[:56]}…”"))

    return len(questions), issues


def manifest_paths(path: str) -> list[str]:
    manifest = json.load(open(path, encoding="utf-8"))
    base = os.path.dirname(path)
    result = []
    for pack in manifest.get("packs", []):
        if "sgs" not in pack.get("programIds", []):
            continue
        candidates = (
            os.path.join(base, pack["file"]),
            os.path.join(os.path.dirname(base), pack["file"]),
        )
        existing = next((candidate for candidate in candidates if os.path.exists(candidate)), None)
        if existing:
            result.append(existing)
    return result


def main() -> int:
    args = sys.argv[1:]
    paths = [arg for arg in args if not arg.startswith("--")]
    if "--manifest" in args:
        if not paths:
            print("--manifest için manifest yolu gerekli.")
            return 2
        paths = manifest_paths(paths[0])
    if not paths:
        print(__doc__)
        return 2

    repo = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    content = os.path.join(repo, "content")
    forbidden = os.path.join(content, "yeterlilik")
    totals = collections.Counter()
    for path in paths:
        resolved = os.path.realpath(path)
        if os.path.commonpath((content, resolved)) != content or os.path.commonpath((forbidden, resolved)) == forbidden:
            print(f"SGS kapsamı dışında dosya reddedildi: {path}")
            return 2
        count, issues = audit(path)
        severity = collections.Counter(level for level, _ in issues)
        totals.update(severity)
        flag = "❌" if severity["FATAL"] else ("⚠️" if severity["UYARI"] else "✅")
        print(f"{flag} {os.path.basename(path):48} {count:4} soru | FATAL {severity['FATAL']:3} UYARI {severity['UYARI']:3}")
        for level, message in issues[:20]:
            print(f"    [{level}] {message}")
    print(f"TOPLAM: FATAL {totals['FATAL']} | UYARI {totals['UYARI']}")
    return 1 if totals["FATAL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
