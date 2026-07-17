# -*- coding: utf-8 -*-
"""mali_tablolar_analizi / karsilastirmali_analiz — yüzde değişim alıştırmaları.

SORUN: 14 soru aynı iskeleti kullanıyor ("Bir kalem önceki dönemde X ₺, cari
dönemde Y ₺'dir. Yüzde değişim kaçtır?") ama yalnız 6 farklı cevap veriyordu
(%25 dört kez, %20 üç kez…) → 8 KLON.

ÇÖZÜM: 14'üne ayrı yüzde değişim. Hem artış hem azalış korunur (dosyada
“−%20” biçiminde azalış cevapları vardı; U+2212 eksi işareti aynen kullanılır).

⚠ Çeldiriciler burada da tek formülden gelmiyordu; gerçek hata türlerinden
yeniden türetiliyor. Bkz. build_mta_trend_drill.py — orada varsayımı 28 soruda
sınayıp yalnız 5'inde tuttuğunu görmüştüm.
"""
import json
import re

P = ("/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"
     "mali_tablolar_analizi/karsilastirmali_analiz.json")
KOK = re.compile(r"^Bir kalem önceki dönemde ([\d.]+) ₺, cari dönemde ([\d.]+) ₺'dir\. "
                 r"Yüzde değişim kaçtır\?$")
EKSI = "−"   # dosyadaki azalış işareti: −%20 (tire değil, matematiksel eksi)


def tr(n):
    return f"{int(n):,}".replace(",", ".")


def yuzde(v):
    """30 → '%30' · -20 → '−%20'"""
    v = round(v, 1)
    govde = f"{int(abs(v))}" if abs(v) == int(abs(v)) else f"{abs(v)}".replace(".", ",")
    return f"{EKSI}%{govde}" if v < 0 else f"%{govde}"


def celdiriciler(onceki, cari, r):
    """Adayın yapabileceği gerçek hatalar; ilk 4 geçerli alınır."""
    degisim = cari - onceki
    adaylar = [
        degisim / cari * 100,        # bölen olarak CARİ dönemi almak
        cari / onceki * 100,         # yüzde değişim yerine TREND yüzdesi vermek
        -r,                          # değişimi ters yöne okumak
        r / 10,                       # ondalık kaydırmak
        abs(degisim) / 1000,          # tutarı doğrudan yüzde sanmak
        r * 2,                        # iki katına çıkarmak
    ]
    secilen, gorulen = [], {yuzde(r)}
    for deger in adaylar:
        if not (0.5 <= abs(deger) <= 600):
            continue
        m = yuzde(deger)
        if m in gorulen:
            continue
        gorulen.add(m)
        secilen.append(m)
        if len(secilen) == 4:
            break
    assert len(secilen) == 4, f"({onceki}, {cari}) için 4 çeldirici yok: {secilen}"
    return secilen


# 14 alıştırma × ayrı yüzde değişim; artış ve azalış birlikte.
# cari = onceki × (100+r)/100 daima tam sayı olacak biçimde seçildi.
PLAN = [
    (200_000, 5), (400_000, 10), (300_000, 15), (500_000, 20), (600_000, 25),
    (200_000, 30), (250_000, 40), (400_000, 50), (800_000, 60), (500_000, 75),
    (400_000, -10), (600_000, -15), (500_000, -25), (800_000, -40),
]
assert len({r for _, r in PLAN}) == len(PLAN), "yüzde değişimler benzersiz olmalı"

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    hedef = [q for q in qs if KOK.match(q["stem"])]
    assert len(hedef) == len(PLAN), f"{len(hedef)} alıştırma var, planda {len(PLAN)}"

    for q, (onceki, r) in zip(hedef, PLAN):
        cari = onceki * (100 + r) // 100
        assert cari * 100 == onceki * (100 + r), f"küsuratlı cari: {onceki} × {r}"
        degisim = cari - onceki
        harf = q["answer"]                       # harf KORUNUR → dağılım bozulmaz
        opts = {harf: yuzde(r)}
        for k, c in zip([k for k in "ABCDE" if k != harf], celdiriciler(onceki, cari, r)):
            opts[k] = c
        assert len(set(opts.values())) == 5, f"{q['id']}: şık çakışması {opts}"
        yon = "artış" if r > 0 else "azalış"
        q["stem"] = (f"Bir kalem önceki dönemde {tr(onceki)} ₺, cari dönemde "
                     f"{tr(cari)} ₺'dir. Yüzde değişim kaçtır?")
        q["options"] = opts
        q["solution"] = (f"Değişim = {tr(abs(degisim))} ₺. Yüzde Değişim = "
                         f"({tr(abs(degisim))} ÷ {tr(onceki)}) × 100 = "
                         f"**{yuzde(r)} {yon}**. Bölen daima ÖNCEKİ dönemdir.")

    gorulen = {}
    for q in qs:
        anahtar = (re.sub(r"[\d.,]+", "#", q["stem"]), q["options"][q["answer"]])
        assert anahtar not in gorulen, f"HÂLÂ KLON: {q['id']} ↔ {gorulen[anahtar]}"
        gorulen[anahtar] = q["id"]

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yeniden üretilen: {len(hedef)} | değişimler: "
          f"{', '.join(yuzde(r) for _, r in PLAN)}")
