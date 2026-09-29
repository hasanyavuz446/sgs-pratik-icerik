# -*- coding: utf-8 -*-
"""Vergi dersi builder'larının ortak hesap yardımcıları.

Gerçek 2026/1-2026/2 kitapçıkları gibi, yıla bağlı tutarlar (tarife, istisna ve beyan sınırları) soru kökünde verilir;
doğru cevaplar burada hesaplanır ki aritmetik hatası kalmasın.
"""
from decimal import Decimal, ROUND_HALF_UP

# 2025 takvim yılı tarifesi (2026/1 kitapçığındaki tabloyla aynı)
DILIM_2025 = [(158_000, 0.15), (330_000, 0.20), (800_000, 0.27), (4_300_000, 0.35), (None, 0.40)]
DILIM_2025_UCRET = [(158_000, 0.15), (330_000, 0.20), (1_200_000, 0.27), (4_300_000, 0.35), (None, 0.40)]

TARIFE_2025 = ("2025 yılı gelir vergisi tarifesi: 158.000 ₺’ye kadar %15; 330.000 ₺’nin 158.000 ₺’si için 23.700 ₺, "
               "fazlası %20; 800.000 ₺’nin (ücret gelirlerinde 1.200.000 ₺’nin) 330.000 ₺’si için 58.100 ₺, fazlası %27; "
               "4.300.000 ₺’nin 800.000 ₺’si için 185.000 ₺ (ücret gelirlerinde 1.200.000 ₺’si için 293.000 ₺), fazlası %35; "
               "4.300.000 ₺’den fazlasının 4.300.000 ₺’si için 1.410.000 ₺ (ücret gelirlerinde 1.378.000 ₺), fazlası %40.")


def gv2025(matrah, ucret=False):
    """2025 tarifesine göre gelir vergisi (tam sayı ₺ sonuç beklenir)."""
    dilimler = DILIM_2025_UCRET if ucret else DILIM_2025
    vergi, alt = Decimal(0), 0
    for ust, oran in dilimler:
        if ust is None or matrah <= ust:
            vergi += (Decimal(matrah) - alt) * Decimal(str(oran))
            break
        vergi += (Decimal(ust) - alt) * Decimal(str(oran))
        alt = ust
    return vergi


def tl(x):
    """Türkçe tutar biçimi: 1710000 -> '1.710.000'; 12345.5 -> '12.345,50'."""
    d = Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    tam, kesir = divmod(abs(d), 1)
    s = f"{int(tam):,}".replace(",", ".")
    if kesir:
        s += "," + f"{kesir:.2f}"[2:]
    return ("-" if d < 0 else "") + s


def secenekler(dogru, *adaylar, adet=4):
    """Doğru sayısal cevaptan farklı, tekrarsız çeldirici listesi (ilk 4 geçerli aday)."""
    out, gor = [], {Decimal(str(dogru)).quantize(Decimal("0.01"))}
    for a in adaylar:
        k = Decimal(str(a)).quantize(Decimal("0.01"))
        if a is None or k in gor or k < 0:
            continue
        gor.add(k)
        out.append(tl(a))
        if len(out) == adet:
            return out
    raise AssertionError(f"yeterli çeldirici yok: {dogru} {adaylar}")
