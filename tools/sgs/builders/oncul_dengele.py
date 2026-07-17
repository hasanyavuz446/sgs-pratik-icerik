#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Öncüllü sorularda doğru cevap dağılımını dengeler — İÇERİĞE DOKUNMADAN.

SORUN
─────
Havuzdaki 541 öncüllü ("I/II/III … hangileri doğrudur?") sorunun %47'sinde cevap
«I ve II». 541 sorunun yalnız 2'sinde cevap "Yalnız X". Yani ilk iki öncül
neredeyse hep doğru, üçüncü neredeyse hep yanlış yazılmış. Öğrenci soruyu hiç
okumadan «I ve II» işaretleyerek %47 alır.

Bu, daha önce "hepsi" cevabının %75 olması kusurunu düzeltirken ÜRETTİĞİM bir
kusur: "hepsi"yi %18'e indirdim ama yerine yeni bir sabit koydum. Kuralı
dedektöre yazmadığım için de yeni üretilen derslerde (muhasebe_standartlari
%65) aynen tekrarlandı. Kontrol artık audit.py'de: `oncul_dagilimi`.

ÇÖZÜM: PERMÜTASYON
──────────────────
Öncüllerin SIRASINI değiştirmek yeter. İçerik, doğruluk, çözüm metni ve öğretilen
şey birebir aynı kalır; yalnız yanlış öncülün NUMARASI değişir, dolayısıyla doğru
şık başka bir bileşime kayar:

    I. doğru   II. doğru   III. yanlış   → cevap «I ve II»
    (III'ü başa al)
    I. yanlış  II. doğru   III. doğru    → cevap «II ve III»

Bu yüzden burada soru YENİDEN YAZILMIYOR — yalnız sıra değişiyor. Üç şey
birlikte güncellenir, yoksa soru bozulur:
  1. kökteki öncül sırası
  2. cevap harfi (yeni doğru bileşimi taşıyan şık)
  3. çözümdeki romen rakamları + "Doğru cevap X" harfi

SINIR
─────
Permütasyon iki-doğrulu soruları üç bileşim arasında dağıtabilir; üç öncülü de
doğru olan soru ("hepsi") permütasyonla değişmez. Ulaşılabilir en iyi dağılım
bu yüzden ~%25, ~%20 değil. "Yalnız X" cevabı da üretilemez — onun için tek
öncülü doğru soru YAZMAK gerekir (ayrı iş).
"""
from __future__ import annotations

import collections
import itertools
import json
import re
import sys

ROMEN = ["I", "II", "III", "IV", "V"]
# Kökteki öncül satırı: "I. metin" / "II) metin"
ONCUL_SATIR = re.compile(r"(?m)^\s*(I{1,3}|IV|V)[\.\)]\s*(.+?)\s*$")


def bilesim(metin: str) -> frozenset | None:
    """Şık metnini öncül numaraları kümesine çevir.

    "I ve II" → {1,2} · "Yalnız III" → {3} · "I, II ve III (her üç ifade de
    doğrudur)" → {1,2,3}
    ⚠ Parantezli son ek atılmalı: eski dosyalarda şıklar "(her üç ifade de
    doğrudur)" gibi açıklama taşıyor ve tam-eşleme onları kaçırıyor.
    """
    t = re.sub(r"\s*\([^)]*\)", "", metin).strip()
    if not re.fullmatch(r"(Yalnız\s+)?(I{1,3}|IV|V)(\s*(,|ve)\s*(I{1,3}|IV|V))*", t, re.I):
        return None
    return frozenset(ROMEN.index(r.upper()) + 1 for r in re.findall(r"\b(I{1,3}|IV|V)\b", t))


def ayristir(question: dict):
    """(önek, [öncül metinleri], {bileşim: harf}, doğru bileşim) — olmazsa None."""
    satirlar = ONCUL_SATIR.findall(question["stem"])
    if len(satirlar) < 3:
        return None
    if [r for r, _ in satirlar] != ROMEN[:len(satirlar)]:
        return None  # sıra bozuksa dokunma
    secenekler = {}
    for harf, metin in question["options"].items():
        b = bilesim(metin)
        if b is None:
            return None  # şıklar bileşim değil → bu soru öncüllü değil
        secenekler[b] = harf
    dogru = next(b for b, h in secenekler.items() if h == question["answer"])
    ilk = question["stem"].index(satirlar[0][0] + ".")
    return question["stem"][:ilk], [m for _, m in satirlar], secenekler, dogru


def cozum_haritala(cozum: str, harita: dict, yeni_harf: str) -> str:
    """Çözümdeki romen rakamlarını yeni numaralara çevir + cevap harfini güncelle.

    ⚠ TEK GEÇİŞTE yapılmalı. Sırayla (I→II, sonra II→III) değiştirirsen ilk
    adımın ürettiği II'yi ikinci adım tekrar çevirir ve numaralar birbirine
    karışır. Bu yüzden tüm eşleşmeler tek `re.sub` içinde, yer tutucusuz.
    """
    def degis(m):
        return ROMEN[harita[ROMEN.index(m.group(1)) + 1] - 1]

    cozum = re.sub(r"(?<![\wçğıöşü])(I{1,3}|IV|V)(?![\wçğıöşü])", degis, cozum)
    return re.sub(r"Doğru\s+(cevap|seçenek)\s+[A-E]", rf"Doğru \1 {yeni_harf}", cozum)


def dengele(path: str, sayac: collections.Counter, yaz: bool = True) -> dict:
    """⚠ DENGE DOSYA BAZINDA KURULMALI, havuz geneline göre değil.

    İlk sürüm yalnız küresel sayacı kullanıyordu: havuz geneli mükemmel çıkıyordu
    (%47 → %26) ama 34 dosya tek tek FATAL kalıyordu, çünkü açgözlü atama bir
    dosyadaki 8 sorunun 4'ünü aynı bileşime yığabiliyor. Öğrenci havuzu değil
    KONUYU çözüyor — 20 soruluk bir testte dosya içi yığılma birebir ipucu.
    Bu yüzden birincil ölçüt dosya sayacı, küresel sayaç yalnız eşitlik bozucu.
    """
    qs = json.load(open(path, encoding="utf-8"))
    # ⚠ content/ altında SGS soru dosyası olmayan JSON'lar da var (manifest,
    # farklı şema). Şema kontrolü olmadan araç onlarda patlıyor ve dosyaların
    # bir kısmını yazdıktan sonra duruyor — yarım uygulanmış dağılım en kötüsü.
    if not isinstance(qs, list) or not qs or not isinstance(qs[0], dict) or "stem" not in qs[0]:
        return {"degisen": 0, "atlanan": 0, "qs": []}
    yerel: collections.Counter = collections.Counter()
    degisen = atlanan = 0
    for q in qs:
        parca = ayristir(q)
        if parca is None:
            continue
        onek, oncul, secenekler, dogru = parca
        n = len(oncul)
        if len(dogru) == n:
            sayac[frozenset(dogru)] += 1     # "hepsi" — permütasyon değiştirmez
            yerel[frozenset(dogru)] += 1
            continue

        # Her permütasyon için: yeni doğru bileşim → o şık var mı? → en az
        # kullanılmış bileşimi seç (küresel dengeyi açgözlü kurar).
        adaylar = []
        for p in itertools.permutations(range(1, n + 1)):
            harita = {eski: yeni for yeni, eski in enumerate(p, 1)}
            yeni_dogru = frozenset(harita[i] for i in dogru)
            if yeni_dogru in secenekler:
                adaylar.append(((yerel[yeni_dogru], sayac[yeni_dogru]), p, harita, yeni_dogru))
        if not adaylar:
            atlanan += 1
            continue
        _, p, harita, yeni_dogru = min(adaylar, key=lambda t: t[0])
        sayac[yeni_dogru] += 1
        yerel[yeni_dogru] += 1
        if yeni_dogru == dogru:
            continue

        yeni_harf = secenekler[yeni_dogru]
        q["stem"] = onek + "\n\n".join(f"{ROMEN[i]}. {oncul[p[i] - 1]}" for i in range(n))
        q["solution"] = cozum_haritala(q["solution"], harita, yeni_harf)
        q["answer"] = yeni_harf
        degisen += 1

    if yaz:
        json.dump(qs, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return {"degisen": degisen, "atlanan": atlanan, "qs": qs}


if __name__ == "__main__":
    sayac: collections.Counter = collections.Counter()
    toplam = collections.Counter()
    for path in sorted(sys.argv[1:]):
        s = dengele(path, sayac, yaz="--rapor" not in sys.argv)
        if s["degisen"] or s["atlanan"]:
            print(f"{path.split('/')[-1][:-5]:34} değişen {s['degisen']:3} · atlanan {s['atlanan']}")
    T = sum(sayac.values())
    print(f"\n══ sonuç dağılımı ({T} öncüllü soru) ══")
    for b, n in sayac.most_common():
        etiket = " ve ".join(ROMEN[i - 1] for i in sorted(b))
        print(f"  {n:3} (%{n * 100 // T:2})  {etiket}")
