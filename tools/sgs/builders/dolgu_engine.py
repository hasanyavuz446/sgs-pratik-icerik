# -*- coding: utf-8 -*-
"""Dolgu kuyruğu temizleyicisi — muhasebe_standartlari ailesi için ortak motor.

NEDEN MOTOR, NEDEN TABLO DEĞİL
──────────────────────────────
tms_10'u dosyaya özel 50 satırlık bir KIRP tablosuyla düzelttim. Sonra ölçtüm:
aynı dolgu kalıbı 9 dosyada birden var (çeldiricilerin %18-61'i), çünkü dokuzunu
da aynı geri alınmış kuralla ("doğruyu kısa, çeldiriciyi uzun yaz") ürettim.
Dosya başına tablo yazmak 9 × 50 satır elle iş demekti ve her tablo bir sonraki
dosyanın kuyruğunu kaçırırdı.

Kuyruklar aslında tek bir Türkçe biçimbirim: EDİLGEN GENİŞ ZAMANIN dolguya
açılmış hâli.

    açıklanmak zorunda kalınır              → açıklanır
    muhasebeleştirilmek zorunda tutulmaktadır → muhasebeleştirilir
    ölçülmek zorunda tutulmaktadır          → ölçülür
    yapılmamak durumundadır                 → yapılmaz

Yani "<gövde>mAk zorunda/durumunda <herhangi bir yardımcı>" → <gövde>'nin geniş
zamanı. Kural tablo değil, morfoloji: ünlü uyumuna göre -ır/-ir/-ur/-ür.
Bu 9 dosyayı da tek geçişte, gelecekteki dosyaları da bedava kapsar.

⚠ Bu motor SADECE ÇELDİRİCİYE dokunur. Doğru şık, kök ve çözüm sabittir
(her dosyada 0/0/0/0 doğrulanır).

⚠ Motor tek başına YETMEZ — tms_10'da öğrenildi. Kırpma dolguyu atar ama
çeldirici yine de doğrudan uzun kalır (bir yanılgıyı adıyla söylemek yer ister),
"en kısayı seç" hâlâ ~%40 tutar. Bu yüzden motor iş bitince RAPOR verir:
hangi soruda doğru en kısa/en uzun kaldı, hedef uzunluk kaç. Kalan iki iş
(atma-şıkkı yerine gerçek yanılgı · doğrunun altına yazılmış çeldirici) içeriktir,
dosyaya özel yazılır.
"""
from __future__ import annotations

import json
import re

# ── Türkçe geniş zaman ────────────────────────────────────────────────────────
UNLU = "aeıioöuü"
# 4 yönlü ünlü uyumu: son ünlü → geniş zaman ünlüsü
UYUM = {"a": "ı", "ı": "ı", "e": "i", "i": "i", "o": "u", "u": "u", "ö": "ü", "ü": "ü"}
# tek heceli düzensizler (et → eder, git → gider); gövde sonuna göre bakılır
DUZENSIZ = {"et": "eder", "git": "gider", "tat": "tadar"}


def _son_unlu(govde: str) -> str:
    for ch in reversed(govde.lower()):
        if ch in UNLU:
            return ch
    return "a"


def genis_zaman(govde: str, olumsuz: bool = False) -> str:
    """<govde> fiilinin geniş zaman 3. tekil hâli.

    açıklan → açıklanır · ölçül → ölçülür · karşıla → karşılar · et → eder
    olumsuz: yapıl → yapılmaz
    """
    g = govde.strip()
    if olumsuz:
        return g + ("maz" if _son_unlu(g) in "aıou" else "mez")
    son = g.rsplit(" ", 1)[-1].lower()
    if son in DUZENSIZ:
        return g[: len(g) - len(son)] + DUZENSIZ[son]
    if g[-1].lower() in UNLU:          # ünlüyle biten gövde: karşıla → karşılar
        return g + "r"
    return g + UYUM[_son_unlu(g)] + "r"


# "<gövde>mAk zorunda/durumunda <yardımcı>"
#
# ⚠⚠ YARDIMCI ZORUNLU VE SAYILI — kural FAIL-CLOSED olmalı.
# İlk sürümde yardımcı isteğe bağlıydı ("(...)?"). Sonuç: eşleşmeyen biçimlerde
# regex yine de "-mAk zorunda"yı yiyor, arkasındaki yardımcıyı bırakıyordu →
# "indirilmek zorunda kalmaktadır" → "indirilir kalmaktadır". Veride ~280 böyle
# eşleşme vardı. Daha kötüsü OLUMSUZLAR: "indirilmek zorunda KALMAZ" → "indirilir
# kalmaz" olur, yani şıkkın anlamı TERSİNE döner ve yanlış bir çeldirici doğru
# hâle gelirdi. 17 dosyada 1078 kuyruk için sessizce yayılacaktı.
#
# Bu yüzden yardımcı biçimler tek tek sayıldı (verideki 178 kuyruk ölçülerek).
# Listede olmayan biçim KIRPILMAZ, raporlanır. Olumsuzlar (kalmaz · değildir ·
# bulunmamaktadır) listede KASTEN yok.
YARDIMCI = (r"(?P<dir>dır|dir|dur|dür)"
            r"|\s+(?P<aux>tutulmaktadır|tutulmuştur|tutulmakta|tutulur"
            r"|bulunmaktadır|bulunur|kalınmaktadır|kalınmakta|kalınır"
            r"|kalmaktadır|kalır|olunmaktadır)"
            r"|\s+(?P<olup>olup)\s+")

DOLGU_KUYRUK = re.compile(
    r"(?P<govde>[\wçğıöşüÇĞİÖŞÜ]+?)(?P<olumsuz>ma|me)?(?:mak|mek)\s+"
    r"(?:zorunda|durumunda)(?:" + YARDIMCI + r")",
    re.IGNORECASE,
)


def _kuyruk_kirp(m: re.Match) -> str:
    fiil = genis_zaman(m.group("govde"), olumsuz=bool(m.group("olumsuz")))
    # "X-mak zorunda olup Y" → "X-ır; Y" (ikinci cümlecik olumsuz olabilir,
    # aynen korunur — anlamı taşıyan yer orası).
    return fiil + "; " if m.group("olup") else fiil


# ── Dolgu regex'ine takılmayan, aynı işi gören adlaştırmalar ──────────────────
# "zorunda" içermez ama şişkinliği aynıdır; tms_10'da bunlar kalınca "en kısayı
# seç" %40'ta takılmıştı.
# ⚠ SIRA ÖNEMLİ: ÖZELDEN GENELE. İlk sürümde genel "…bir husus niteliğinde"
# kuralı listede öncelikliydi ve "düzenlenmemiş bir husus niteliğindedir" →
# "düzenlenmemiştir" özel kuralına sıra hiç gelmiyordu.
#
# ⚠ BURAYA "olan bir X ifade eder" → "olur" KURALI EKLEME. Denedim: bağlamda
# öncesinde "-mAk zorunda" duruyor, sonuç "aktifleştirilmek zorunda olur" oluyor
# — hem bozuk Türkçe hem dolgu duruyor. O aile (≈100 şık) kasten kırpılmadan
# bırakıldı; onlar boy dengelemesiyle (KISALT) çözülür.
ADLASTIRMA = [
    # özel
    (r"tanımlanmamış bir husus niteliğinde(?: bulunur| bulunmaktadır|dir)", "tanımlanmamıştır"),
    (r"düzenlenmemiş bir husus niteliğinde(?: bulunur| bulunmaktadır|dir)", "düzenlenmemiştir"),
    (r"kapsayan (?:bir düzenleme niteliğindedir|dar kapsamlı bir düzenlemedir)", "kapsar"),
    (r"([\wçğıöşü]+) bir husus niteliğinde(?: bulunur| bulunmaktadır|dir)", r"\1 bir husustur"),
    (r"\s*hususu belirleyici (?:sayılır|olur|sayılmaktadır)", " belirleyicidir"),
    # şimdiki zamanın geniş zamana indirgenmesi (anlam aynı, kuyruk kısa)
    (r"kapsamaktadır", "kapsar"),
    (r"ifade etmektedir", "ifade eder"),
    (r"karşılamaktadır", "karşılar"),
    (r"göstermektedir", "gösterir"),
    (r"gerektirmektedir", "gerektirir"),
    (r"sayılmaktadır", "sayılır"),
    (r"edilmektedir", "edilir"),
    (r"olmaktadır", "olur"),
    (r"bulunmaktadır", "bulunur"),
    # genel kuyruklar
    (r"\s*niteliğinde bulunan", ""),
    (r"\s*niteliğinde (?:bulunur|olmaktadır)", ""),
    (r"\s*niteliğindedir", ""),
    (r"\s*durumunu ifade eder", ""),
]

# ── Atma-şıkkı ailesi ────────────────────────────────────────────────────────
# "Bu husus standartta düzenlenmemiştir / serbest takdire bırakılmıştır" — 17
# dosyada 474 üye, dosya başına ~28. Her göründüğünde YANLIŞ, dolayısıyla
# standardı hiç bilmeyen öğrenci tek oturumda "böyle diyen şık yanlıştır"
# kuralını öğrenir ve soruların yarısında bedava eleme yapar.
#
# ⚠ İlk regex yalnız "Bu husus … düzenlenmemiş olup … serbest takdirine
# bırakılmıştır" tam kalıbını arıyordu ve ailenin ~%40'ını kaçırıyordu:
# "…tanımlanmamış olup uygulamada kullanılmamaktadır", "…düzenlenmemiş bir
# husustur", "…belirsiz bırakılmıştır" hepsi aynı işi görüyor. Ortak çekirdek
# standardın adı + olumsuz fiil; kalıbın kuyruğu değişken.
ATMA = re.compile(
    r"(?:TMS|TFRS|Kavramsal Çerçeve|bu standartta|standartta)[^.]{0,48}?"
    r"(?:düzenlenmemiş|tanımlanmamış|belirlenmemiş|hüküm bulunmamakta|"
    r"serbest takdirine bırakıl|serbest bırakılmış)",
    re.IGNORECASE,
)
DOLGU_TEST = re.compile(r"(zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır)", re.I)
ONCUL = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")


def _atma_sec(kurallar, question: dict, sira: int, ozel=None) -> str:
    """Atma-şıkkının yerine geçecek yanılgıyı seç — KÖKE GÖRE, sırayla değil.

    ⚠ Sırayla döndürmek yetmiyor. tms_10'da konu dardı ve kurtardı; tms_12'de
    41 sorunun her biri ayrı bir alt konu ("muhasebe kârı" · "iskonto" ·
    "netleştirme"). Netleştirme yanılgısını "muhasebe kârı nedir" sorusunun
    altına koyarsan şık KONU DIŞI kalır — öğrenci standardı bilmeden yine eler,
    yani atma-şıkkını yeni bir atma-şıkkıyla değiştirmiş olursun.

    kurallar: [(kök_regex, metin), …] — ilk eşleşen kazanır (ÖZELDEN GENELE
    sırala). Hiçbiri eşleşmezse SON eleman genel yedektir.
    Düz liste verilirse eski sırayla-dağıtma davranışı korunur (tms_10).
    """
    if ozel and question["id"] in ozel:
        return ozel[question["id"]]
    if kurallar and isinstance(kurallar[0], str):
        return kurallar[sira % len(kurallar)]
    # ⚠ Çakışma gerçek çıktı. tms_12/0016'da "YÜKSEK olması" yanılgım o sorunun
    # A şıkkıyla birebir aynıydı — çünkü A KIRPILDIKTAN SONRA benim cümleme
    # indi. Çakışmayı kırpma öncesi şıklarla ölçmek yetmiyor; SONRAKİ hâle bak.
    mevcut = {v.casefold() for v in question["options"].values()}
    for kalip, metin in kurallar[:-1]:
        if re.search(kalip, question["stem"], re.IGNORECASE) and metin.casefold() not in mevcut:
            return metin
    if kurallar[-1][1].casefold() not in mevcut:
        return kurallar[-1][1]
    raise SystemExit(
        f"\n{question['id']}: eşleşen her yanılgı zaten şıklarda var — bu soruya ÖZEL yazılmalı.\n"
        f"  kök   : {question['stem']}\n"
        + "".join(f"  {h}{'◀doğru' if h == question['answer'] else '     '}: {v}\n"
                  for h, v in sorted(question['options'].items()))
        + f"  → KONFIG'e ekle:  \"atma_ozel\": {{\"{question['id']}\": \"<yeni yanılgı>\"}}\n")


def temizle(path: str, atma_yerine=None, atma_ozel=None, uzat=None,
            kisalt: "dict[str, dict[str, str]] | None" = None,
            yaz: bool = True) -> dict:
    """Bir dosyayı temizle; ne yapıldığını ve NE KALDIĞINI döndür."""
    qs = json.load(open(path, encoding="utf-8"))
    onceki = {q["id"]: dict(q["options"]) for q in qs}
    idx = {q["id"]: q for q in qs}
    kirpilan = atma_sayi = 0
    sira = 0

    for q in qs:
        for harf, v in list(q["options"].items()):
            if harf == q["answer"]:
                continue
            if atma_yerine and ATMA.search(v):
                q["options"][harf] = _atma_sec(atma_yerine, q, sira, atma_ozel)
                sira += 1
                atma_sayi += 1
                continue
            yeni = DOLGU_KUYRUK.sub(_kuyruk_kirp, v)
            for bul, koy in ADLASTIRMA:
                yeni = re.sub(bul, koy, yeni)
            yeni = re.sub(r"\s+", " ", yeni).strip().rstrip(";").strip()
            if yeni != v:
                q["options"][harf] = yeni
                kirpilan += 1

    # doğrunun altına/üstüne yazılan çeldiriciler (içerik işi, dosyaya özel)
    for qid, degisim in (kisalt or {}).items():
        q = idx[qid]
        d = len(q["options"][q["answer"]])
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            assert len(yeni) < d, f"{qid}/{harf}: {len(yeni)} ≥ doğru {d} — kısalmamış"
            q["options"][harf] = yeni

    # ⚠ Uzatma doğrunun EN AZ 15 KARAKTER üstüne yazılmalı. Kıl payı uzatmak
    # (122 ↔ 123) göz kararıyla fark edilmiyor ve dosyayı sessizce FATAL
    # bırakıyor; vergi/borçlar dosyalarında bu bana toplam 6 tur yaktırdı.
    # Bu yüzden kural assert — yazarken hedefi dökümden al, tahmin etme.
    for qid, degisim in (uzat or {}).items():
        q = idx[qid]
        d = len(q["options"][q["answer"]])
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            assert len(yeni) >= d + 15, \
                f"{qid}/{harf}: {len(yeni)} < doğru {d} + 15 — {d + 15 - len(yeni)} karakter daha gerek"
            q["options"][harf] = yeni

    for q in qs:
        assert len(set(q["options"].values())) == 5, f"{q['id']}: şık çakışması"
        assert q["options"][q["answer"]] == onceki[q["id"]][q["answer"]], \
            f"{q['id']}: DOĞRU ŞIK DEĞİŞTİ"

    if yaz:
        json.dump(qs, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    return {"qs": qs, "kirpilan": kirpilan, "atma": atma_sayi,
            "kalan_dolgu": sum(1 for q in qs for h, v in q["options"].items()
                               if h != q["answer"] and DOLGU_TEST.search(v)),
            "kalan_atma": sum(1 for q in qs for h, v in q["options"].items()
                              if h != q["answer"] and ATMA.search(v))}


def rapor(qs: list[dict]) -> str:
    """Kırpma sonrası boy dağılımı — kalan içerik işini bu belirler."""
    u = k = n = 0
    ds, cs = [], []
    for q in qs:
        if len(ONCUL.findall(q["stem"])) >= 2:
            continue
        n += 1
        o = q["options"]
        d = len(o[q["answer"]])
        L = [len(v) for v in o.values()]
        ds.append(d)
        cs += [len(v) for h, v in o.items() if h != q["answer"]]
        u += d == max(L)
        k += d == min(L)
    return (f"doğru en uzun {u * 100 // n}% / en kısa {k * 100 // n}% / "
            f"ortada {(n - u - k) * 100 // n}%  | doğru ort {sum(ds) // len(ds)} · "
            f"çeldirici ort {sum(cs) // len(cs)}  (n={n})")
