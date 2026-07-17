# -*- coding: utf-8 -*-
"""denetim / denetim_riski — tespit riski alıştırmaları.

SORUN: 9 soru aynı iskeleti kullanıyor ("Yapısal risk %A, kontrol riski %B,
hedeflenen denetim riski %C olan bir denetimde kabul edilebilir tespit riski
yüzde kaçtır?") ama yalnız İKİ farklı cevap veriyordu — %20 beş kez, %10 dört
kez → 7 KLON. Aday birini çözünce diğer sekizini okumadan işaretliyordu.

ÇÖZÜM: 9'una ayrı tespit riski. TR = DR ÷ (YR × KR).

⚠ Çeldiriciler gerçek hata türlerinden türetilir. Denetim riski modelinde en
öğretici yanılgı, tespit riski yerine ÖYR'yi (yapısal × kontrol) vermektir;
o yüzden çeldirici bankasında önceliklidir.
"""
import json
import re

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/denetim/denetim_riski.json"
KOK = re.compile(r"^Yapısal risk %[\d,]+, kontrol riski %[\d,]+, hedeflenen denetim riski "
                 r"%[\d,]+ olan bir denetimde kabul edilebilir tespit riski yüzde kaçtır\?$")


def yuzde(x):
    """0,15 → '%15' · 0,075 → '%7,5'"""
    v = round(x * 100, 2)
    govde = f"{v:.2f}".rstrip("0").rstrip(".").replace(".", ",")
    return f"%{govde}"


def celdiriciler(yr, kr, dr, tr):
    oyr = yr * kr
    adaylar = [
        oyr,          # tespit riski yerine ÖYR'yi vermek — en sık yanılgı
        dr / yr,      # kontrol riskini hesaba katmamak
        dr / kr,      # yapısal riski hesaba katmamak
        dr * oyr,     # bölmek yerine çarpmak
        tr / 2,       # ondalık/yarı hatası
        tr * 2,
        1 - tr,       # tümleyenini almak
    ]
    secilen, gorulen = [], {yuzde(tr)}
    for deger in adaylar:
        if not (0.005 <= deger <= 0.95):
            continue
        m = yuzde(deger)
        if m in gorulen:
            continue
        gorulen.add(m)
        secilen.append(m)
        if len(secilen) == 4:
            break
    assert len(secilen) == 4, f"({yr}, {kr}, {dr}) için 4 çeldirici yok: {secilen}"
    return secilen


# 9 alıştırma × ayrı tespit riski. TR = DR ÷ (YR × KR); hepsi tam bölünür.
PLAN = [
    (0.60, 0.50, 0.06),   # → %20
    (0.50, 0.40, 0.03),   # → %15
    (0.40, 0.50, 0.06),   # → %30
    (0.50, 0.60, 0.03),   # → %10
    (0.80, 0.25, 0.05),   # → %25
    (0.50, 0.50, 0.02),   # → %8
    (0.60, 0.50, 0.12),   # → %40
    (0.40, 0.25, 0.05),   # → %50
    (0.80, 0.50, 0.02),   # → %5
]

if __name__ == "__main__":
    beklenen = [round(dr / (yr * kr), 4) for yr, kr, dr in PLAN]
    assert len(set(beklenen)) == len(PLAN), f"tespit riskleri benzersiz olmalı: {beklenen}"

    qs = json.load(open(P, encoding="utf-8"))
    hedef = [q for q in qs if KOK.match(q["stem"])]
    assert len(hedef) == len(PLAN), f"{len(hedef)} alıştırma var, planda {len(PLAN)}"

    for q, (yr, kr, dr) in zip(hedef, PLAN):
        oyr, tr = yr * kr, dr / (yr * kr)
        harf = q["answer"]                       # harf KORUNUR → dağılım bozulmaz
        opts = {harf: yuzde(tr)}
        for k, c in zip([k for k in "ABCDE" if k != harf], celdiriciler(yr, kr, dr, tr)):
            opts[k] = c
        assert len(set(opts.values())) == 5, f"{q['id']}: şık çakışması {opts}"
        q["stem"] = (f"Yapısal risk {yuzde(yr)}, kontrol riski {yuzde(kr)}, hedeflenen "
                     f"denetim riski {yuzde(dr)} olan bir denetimde kabul edilebilir "
                     f"tespit riski yüzde kaçtır?")
        q["options"] = opts
        q["solution"] = (f"DR = YR × KR × TR olduğundan TR = DR ÷ (YR × KR) = "
                         f"{dr:.4g} ÷ ({yr:.4g} × {kr:.4g}) = {dr:.4g} ÷ {oyr:.4g} = "
                         f"**{yuzde(tr)}**. Önemli yanlışlık riski ({yuzde(oyr)}) "
                         f"tespit riskinin kendisi değil, paydasıdır.")

    gorulen = {}
    for q in qs:
        anahtar = (re.sub(r"[\d.,]+", "#", q["stem"]), q["options"][q["answer"]])
        assert anahtar not in gorulen, f"HÂLÂ KLON: {q['id']} ↔ {gorulen[anahtar]}"
        gorulen[anahtar] = q["id"]

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yeniden üretilen: {len(hedef)} | tespit riskleri: "
          f"{', '.join(yuzde(dr / (yr * kr)) for yr, kr, dr in PLAN)}")
