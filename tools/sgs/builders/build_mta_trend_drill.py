# -*- coding: utf-8 -*-
"""mali_tablolar_analizi / trend_analizi — hesap alıştırmalarını yeniden üretir.

SORUN: Dosyadaki 60 sorunun 27'si aynı iskeleti kullanıyor ("Baz yılda X ₺ olan
bir kalem, izleyen bir yılda Y ₺ olmuştur. Trend yüzdesi kaçtır?") ama yalnız 9
farklı cevap veriyordu → 18 KLON. Aday 260.000/200.000'i çözünce 1.300.000/
1.000.000 ve 780.000/600.000'i (üçü de %130) okumadan işaretliyordu.

ÇÖZÜM: 27 alıştırmanın her birine FARKLI bir trend yüzdesi. Böylece klon meşru
alıştırmaya döner: aynı şablon + farklı cevap = mekanik beceride istenen şey.

⚠ Bu dosyanın builder'ı yoktu (builder disiplininden önceki içerik) ve
çeldiricileri tek bir formülden GELMİYORDU — varsayımımı 28 soruda sınadım,
yalnız 5'inde tuttu. İkisi formülden (artış%, ters oran), ikisi elle seçilmişti.
Bu yüzden çeldiriciler burada gerçek hata türlerinden yeniden türetiliyor;
her biri adayın yapabileceği belirli bir yanılgıyı temsil eder.

Yalnız bu 27 alıştırma değişir; dosyadaki 33 kavram/yorum sorusuna dokunulmaz.
"""
import json
import re

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/mali_tablolar_analizi/trend_analizi.json"

# İleri yönlü trend alıştırması: baz ve cari verilip yüzde isteniyor. ÜÇ ifade
# çeşidi var ("bir kalem" 28 · "net satışlar" 2 · "…'ye çıkmıştır" 1) ve bu
# çeşitlilik KORUNUR — iskeleti farklılaştırdığı için işimize yarar. Bu yüzden
# kök yeniden yazılmaz; yalnız içindeki iki ₺ tutarı değiştirilir.
ILERI = re.compile(r"^Baz yılda [\d.]+ ₺ olan .+?(?:izleyen|ilerleyen) bir yılda [\d.]+ ₺"
                   r".*?trend yüzdesi kaçtır\?$", re.I)
TUTAR = re.compile(r"([\d.]+) ₺")
# Ters yönlü aile (trend verilip cari isteniyor) AYRI bir sorudur; dokunulmaz.
TERS = re.compile(r"trend yüzdesi %[\d.,]+")


def tr(n):
    return f"{int(n):,}".replace(",", ".")


def yuzde(v):
    v = round(v, 1)
    return f"%{int(v)}" if v == int(v) else f"%{v}".replace(".", ",")


def celdiriciler(r):
    """Adayın yapabileceği gerçek hatalar — sırayla denenir, ilk 4 geçerli alınır."""
    adaylar = [
        (r - 100 if r > 100 else 100 - r, "trend yerine yüzde DEĞİŞİMİ hesaplamak"),
        (10000 / r,                       "oranı ters kurmak (baz ÷ cari)"),
        (200 - r,                         "değişimi yanlış yöne uygulamak"),
        (r / 10,                          "ondalık kaydırmak"),
        (100 - 10000 / r,                 "değişimi cari yıla bölmek"),
        (r * 2,                           "iki katına çıkarmak"),
    ]
    secilen, gorulen = [], {yuzde(r)}
    for deger, _ in adaylar:
        if not (1 <= deger <= 600):
            continue
        m = yuzde(deger)
        if m in gorulen:
            continue
        gorulen.add(m)
        secilen.append(m)
        if len(secilen) == 4:
            break
    assert len(secilen) == 4, f"r={r} için 4 çeldirici üretilemedi: {secilen}"
    return secilen


# 27 alıştırma × ayrı trend yüzdesi. Baz yıl da çeşitlendirildi — hepsi aynı baz
# olsaydı o da kendi başına bir örüntü olurdu. cari = baz × r/100 daima tam sayı
# (baz 100.000'in katı, r tam sayı).
PLAN = [
    (400_000, 40), (500_000, 50), (600_000, 60), (400_000, 65), (800_000, 70),
    (1_200_000, 75), (500_000, 80), (600_000, 85), (200_000, 90), (400_000, 95),
    (2_000_000, 105), (300_000, 110), (600_000, 115), (500_000, 120), (800_000, 125),
    (1_000_000, 130), (400_000, 135), (200_000, 140), (600_000, 145), (300_000, 150),
    (500_000, 155), (400_000, 160), (800_000, 165), (1_500_000, 180), (250_000, 200),
    (400_000, 225), (200_000, 250), (600_000, 35), (500_000, 45), (400_000, 55),
    (800_000, 175),
]
assert len({r for _, r in PLAN}) == len(PLAN), "trend yüzdeleri benzersiz olmalı"

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    hedef = [q for q in qs if ILERI.match(q["stem"]) and not TERS.search(q["stem"])]
    assert len(hedef) == len(PLAN), f"{len(hedef)} alıştırma var, planda {len(PLAN)}"

    for q, (baz, r) in zip(hedef, PLAN):
        cari = baz * r // 100
        assert cari * 100 == baz * r, f"küsuratlı cari: {baz} × {r}"
        harf = q["answer"]                       # harf KORUNUR → dağılım bozulmaz
        opts = {harf: yuzde(r)}
        for k, c in zip([k for k in "ABCDE" if k != harf], celdiriciler(r)):
            opts[k] = c
        assert len(set(opts.values())) == 5, f"{q['id']}: şık çakışması {opts}"

        # Kök YENİDEN YAZILMAZ: ifade çeşidi korunsun diye yalnız iki tutar değişir.
        tutarlar = TUTAR.findall(q["stem"])
        assert len(tutarlar) == 2, f"{q['id']}: 2 tutar bekleniyordu, {tutarlar}"
        yeni_kok, sira = q["stem"], iter([tr(baz), tr(cari)])
        yeni_kok = TUTAR.sub(lambda m: f"{next(sira)} ₺", yeni_kok)
        q["stem"] = yeni_kok
        q["options"] = opts
        q["solution"] = (f"Trend Yüzdesi = (Cari Yıl ÷ Baz Yıl) × 100 = "
                         f"({tr(cari)} ÷ {tr(baz)}) × 100 = **{yuzde(r)}**.")

    # Dosyanın TAMAMINDA hiçbir iki soru aynı (iskelet, cevap) çiftine düşmemeli.
    gorulen = {}
    for q in qs:
        anahtar = (re.sub(r"[\d.,]+", "#", q["stem"]), q["options"][q["answer"]])
        assert anahtar not in gorulen, f"HÂLÂ KLON: {q['id']} ↔ {gorulen[anahtar]}"
        gorulen[anahtar] = q["id"]

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yeniden üretilen alıştırma: {len(hedef)} | "
          f"trend yüzdeleri: {', '.join(yuzde(r) for _, r in PLAN[:6])}…")
