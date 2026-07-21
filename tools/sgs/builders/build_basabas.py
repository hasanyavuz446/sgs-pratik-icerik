# -*- coding: utf-8 -*-
"""SGS — Maliyet Muhasebesi / Başabaş Noktası (Maliyet-Hacim-Kâr) — 60 soru.

Baba isteği (2026-07-18): "Maliyet muhasebesi: Başabaş noktası".
Kaynak: maliyet muhasebesi MHK analizi (katkı payı, başabaş, güvenlik payı,
faaliyet kaldıracı). ÖZGÜN. Hesaplar Python ile üretilir → aritmetik GARANTİ doğru.

★ Şık örüntüsü temiz: hesap sorularında şıklar sayısal → boy ipucu düşük;
kavram sorularında çeldiriciler doğruyla aynı boyda. Dolgu YOK. Harf gen_letters.
__main__ kör-öğrenciyi ölçer (≤%30 hedef; gerekiyorsa fix_basabas_boy.py).

⚠ Senaryo sayıları VARSAYIMSAL (gerçek/yıla-bağlı fiyat değil) — başabaş saf
matematiktir, güncellikten etkilenmez. ₺ kullanılır.
"""
import json
import random

DERS, KONU = "maliyet_muhasebesi", "basabas_noktasi"
PREFIX, SEED = "basabas-gen", 20260720
OUT_APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/maliyet_muhasebesi/basabas_noktasi.json"
OUT_CONTENT = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/maliyet_muhasebesi/basabas_noktasi.json"


def fmt(x):
    """Sayıyı TR biçiminde: 5000 → '5.000', 12.5 → '12,5'."""
    if isinstance(x, float) and not x.is_integer():
        s = f"{x:,.2f}".rstrip("0").rstrip(".")
        # 12,345.67 → 12.345,67
        s = s.replace(",", "␟").replace(".", ",").replace("␟", ".")
        return s
    return f"{int(x):,}".replace(",", ".")


Q = []
def cq(stem, correct, distractors, unit, why, ref):
    """Hesap sorusu: sayısal doğru + 3 çeldirici, birimle biçimlenir."""
    assert len(distractors) == 3, stem[:40]
    vals = [correct] + distractors
    assert len(set(vals)) == 4, "sayı tekrarı: " + stem[:40]
    def lab(v):
        return f"{fmt(v)} {unit}".strip()
    Q.append(dict(stem=stem, correct=lab(correct),
                  distractors=[lab(v) for v in distractors], why=why, ref=ref, calc=True))

def kq(stem, correct, distractors, why, ref):
    """Kavram sorusu: metin şıklar."""
    assert len(distractors) == 3, stem[:40]
    assert correct not in distractors, "doğru çeldiricide: " + stem[:40]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref, calc=False))


# Not: SGS 5 şıklı; hesap sorularında 1 doğru + 3 sayısal çeldirici + 1 "hiçbiri/
# diğer" yerine 4. sayısal çeldirici gen aşamasında eklenir. Basitlik için burada
# 4 şık verip 5.'yi montajda türetiyoruz → aşağıda cq 3 çeldirici alır, montaj +1.
# (5 şık zorunlu olduğundan cq'ya 4. çeldirici ekliyoruz.)

# ── A. Temel kavramlar (8, kavram) ───────────────────────────────────────────
kq("Katkı payı (katkı marjı) bakımından aşağıdakilerden hangisi doğrudur?",
   "Birim satış fiyatından birim değişken maliyetin çıkarılmasıyla bulunan tutardır",
   ["Birim satış fiyatından birim sabit maliyetin çıkarılmasıyla bulunan tutardır",
    "Toplam satış tutarından toplam sabit maliyetin çıkarılmasıyla bulunan tutardır",
    "Birim satış fiyatına birim değişken maliyetin eklenmesiyle bulunan tutardır"],
   "Katkı payı = birim satış fiyatı − birim değişken maliyet; önce sabit maliyetleri karşılar, kalanı kâra geçer.",
   "MHK - katkı payı"),

kq("Başabaş noktası bakımından aşağıdakilerden hangisi doğrudur?",
   "Toplam gelirin toplam maliyete eşit olduğu, kâr ve zararın sıfırlandığı satış düzeyidir",
   ["Toplam gelirin toplam değişken maliyete eşit olduğu ve kârın en yüksek olduğu düzeydir",
    "Toplam sabit maliyetin toplam değişken maliyete eşit olduğu üretim düzeyidir",
    "İşletmenin en yüksek kârı elde ettiği ve kapasitenin tümünü kullandığı düzeydir"],
   "Başabaş noktasında toplam gelir = toplam maliyet olduğundan kâr da zarar da sıfırdır.",
   "MHK - başabaş noktası"),

kq("Sabit maliyet bakımından aşağıdakilerden hangisi doğrudur?",
   "Üretim ve satış hacmi değişse de toplamı belirli bir aralıkta değişmeyen maliyettir",
   ["Üretim hacmi arttıkça toplamı da aynı oranda artan ve hacme bağlı olan maliyettir",
    "Her üretim düzeyinde birim başına tutarı sabit kalan ve toplamı değişen maliyettir",
    "Yalnızca üretim durduğunda ortaya çıkan ve üretim sürerken sıfırlanan maliyettir"],
   "Sabit maliyet (kira, amortisman gibi) toplamda hacimden bağımsızdır; birim sabit maliyet ise hacim arttıkça azalır.",
   "MHK - sabit maliyet"),

kq("Değişken maliyet bakımından aşağıdakilerden hangisi doğrudur?",
   "Üretim hacmiyle doğru orantılı olarak toplamı artıp azalan maliyettir",
   ["Üretim hacmi değişse de toplamı hiç değişmeyen ve sabit kalan maliyettir",
    "Birim başına tutarı hacme göre sürekli değişen, toplamı sabit olan maliyettir",
    "Yalnızca kapasite aşıldığında ortaya çıkan sıçramalı nitelikte bir maliyettir"],
   "Değişken maliyet (hammadde, direkt işçilik gibi) toplamda hacimle orantılıdır; birim değişken maliyet ise sabittir.",
   "MHK - değişken maliyet"),

kq("Katkı oranı (katkı payı oranı) bakımından aşağıdakilerden hangisi doğrudur?",
   "Birim katkı payının birim satış fiyatına bölünmesiyle bulunan orandır",
   ["Birim katkı payının birim değişken maliyete bölünmesiyle bulunan orandır",
    "Birim sabit maliyetin birim satış fiyatına bölünmesiyle bulunan orandır",
    "Toplam sabit maliyetin toplam satış tutarına bölünmesiyle bulunan orandır"],
   "Katkı oranı = katkı payı ÷ satış fiyatı; başabaş tutarı bu oranla hesaplanır.",
   "MHK - katkı oranı"),

kq("Güvenlik payı (emniyet marjı) bakımından aşağıdakilerden hangisi doğrudur?",
   "Fiili satışların başabaş satışlarını aştığı, zarara düşmeden önceki tampon tutarıdır",
   ["Başabaş satışlarının fiili satışları aştığı ve zararı gösteren tutardır",
    "Toplam sabit maliyet ile toplam değişken maliyet arasındaki farktır",
    "İşletmenin ulaşabileceği en yüksek kapasite ile fiili üretim arasındaki farktır"],
   "Güvenlik payı = fiili satış − başabaş satış; satışların başabaşın ne kadar üstünde olduğunu, dolayısıyla zarara ne kadar dayanıklı olunduğunu gösterir.",
   "MHK - güvenlik payı"),

kq("Maliyet-hacim-kâr analizinin varsayımları bakımından aşağıdakilerden hangisi doğrudur?",
   "Birim satış fiyatı ve birim değişken maliyet ilgili aralıkta sabit kabul edilir",
   ["Birim satış fiyatı hacim arttıkça sürekli düşen bir değer olarak kabul edilir",
    "Toplam sabit maliyet, üretim hacmiyle doğru orantılı artan bir tutar sayılır",
    "Birim değişken maliyet üretim arttıkça sürekli yükselen bir değer kabul edilir"],
   "MHK analizi; fiyatın, birim değişken maliyetin ve toplam sabit maliyetin ilgili faaliyet aralığında sabit olduğunu varsayar.",
   "MHK - varsayımlar"),

kq("Faaliyet kaldıracı bakımından aşağıdakilerden hangisi doğrudur?",
   "Satışlardaki yüzde değişimin faaliyet kârında yarattığı yüzde değişimi ölçen katsayıdır",
   ["Satışlardaki değişimin işletmenin borç faizinde yarattığı değişimi ölçen katsayıdır",
    "Toplam sabit maliyetin toplam değişken maliyete oranını gösteren bir katsayıdır",
    "İşletmenin öz kaynak ile yabancı kaynak arasındaki dengesini ölçen katsayıdır"],
   "Faaliyet kaldıracı = toplam katkı payı ÷ faaliyet kârı; sabit maliyeti yüksek işletmelerde satış değişimi kârı daha çok oynatır.",
   "MHK - faaliyet kaldıracı"),

# ── B. BEP miktar hesabı (10, hesap) ─────────────────────────────────────────
# BEP(adet) = Sabit / (SF − DM)
cq("Birim satış fiyatı 50 ₺, birim değişken maliyet 30 ₺ ve toplam sabit maliyet 100.000 ₺ olan işletmenin başabaş noktası kaç adettir?",
   5000, [2000, 1250, 3333], "adet",
   "Katkı payı = 50 − 30 = 20 ₺. Başabaş (adet) = 100.000 ÷ 20 = 5.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 80 ₺, birim değişken maliyet 50 ₺ ve toplam sabit maliyet 240.000 ₺ olan işletmenin başabaş üretim miktarı kaç adettir?",
   8000, [3000, 4800, 6000], "adet",
   "Katkı payı = 80 − 50 = 30 ₺. Başabaş = 240.000 ÷ 30 = 8.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 40 ₺, birim değişken maliyet 24 ₺ ve toplam sabit maliyet 320.000 ₺ olan işletmenin başabaş noktası kaç adettir?",
   20000, [8000, 13333, 12500], "adet",
   "Katkı payı = 40 − 24 = 16 ₺. Başabaş = 320.000 ÷ 16 = 20.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 120 ₺, birim değişken maliyet 70 ₺ ve toplam sabit maliyet 500.000 ₺ olan işletmenin başabaş miktarı kaç adettir?",
   10000, [4167, 7143, 5000], "adet",
   "Katkı payı = 120 − 70 = 50 ₺. Başabaş = 500.000 ÷ 50 = 10.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 25 ₺, birim değişken maliyet 15 ₺ ve toplam sabit maliyet 90.000 ₺ olan işletmenin başabaş noktası kaç adettir?",
   9000, [3600, 6000, 4500], "adet",
   "Katkı payı = 25 − 15 = 10 ₺. Başabaş = 90.000 ÷ 10 = 9.000 adet.",
   "MHK - başabaş adet"),

cq("Birim katkı payı 25 ₺ ve toplam sabit maliyet 375.000 ₺ olan işletmenin başabaş satış miktarı kaç adettir?",
   15000, [7500, 12500, 18750], "adet",
   "Başabaş (adet) = sabit maliyet ÷ birim katkı payı = 375.000 ÷ 25 = 15.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 60 ₺, birim değişken maliyet 45 ₺ ve toplam sabit maliyet 180.000 ₺ olan işletmenin başabaş miktarı kaç adettir?",
   12000, [3000, 4000, 15000], "adet",
   "Katkı payı = 60 − 45 = 15 ₺. Başabaş = 180.000 ÷ 15 = 12.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 200 ₺, birim değişken maliyet 120 ₺ ve toplam sabit maliyet 320.000 ₺ olan işletmenin başabaş noktası kaç adettir?",
   4000, [1600, 2667, 2000], "adet",
   "Katkı payı = 200 − 120 = 80 ₺. Başabaş = 320.000 ÷ 80 = 4.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 15 ₺, birim değişken maliyet 9 ₺ ve toplam sabit maliyet 36.000 ₺ olan işletmenin başabaş miktarı kaç adettir?",
   6000, [2400, 4000, 3000], "adet",
   "Katkı payı = 15 − 9 = 6 ₺. Başabaş = 36.000 ÷ 6 = 6.000 adet.",
   "MHK - başabaş adet"),

cq("Birim satış fiyatı 90 ₺, birim değişken maliyet 60 ₺ ve toplam sabit maliyet 210.000 ₺ olan işletmenin başabaş noktası kaç adettir?",
   7000, [2333, 3500, 3000], "adet",
   "Katkı payı = 90 − 60 = 30 ₺. Başabaş = 210.000 ÷ 30 = 7.000 adet.",
   "MHK - başabaş adet"),

# ── C. BEP tutar (TL) hesabı (8, hesap) ──────────────────────────────────────
# BEP(TL) = Sabit / katkı oranı
cq("Katkı oranı %40 ve toplam sabit maliyet 200.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   500000, [80000, 300000, 800000], "₺",
   "Başabaş (₺) = sabit maliyet ÷ katkı oranı = 200.000 ÷ 0,40 = 500.000 ₺.",
   "MHK - başabaş tutar"),

cq("Birim satış fiyatı 50 ₺, birim değişken maliyet 30 ₺ ve toplam sabit maliyet 100.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   250000, [200000, 166667, 500000], "₺",
   "Katkı oranı = (50−30)/50 = %40. Başabaş (₺) = 100.000 ÷ 0,40 = 250.000 ₺ (5.000 adet × 50 ₺).",
   "MHK - başabaş tutar"),

cq("Katkı oranı %25 ve toplam sabit maliyet 150.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   600000, [37500, 375000, 200000], "₺",
   "Başabaş (₺) = 150.000 ÷ 0,25 = 600.000 ₺.",
   "MHK - başabaş tutar"),

cq("Katkı oranı %50 ve toplam sabit maliyet 320.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   640000, [160000, 480000, 800000], "₺",
   "Başabaş (₺) = 320.000 ÷ 0,50 = 640.000 ₺.",
   "MHK - başabaş tutar"),

cq("Birim satış fiyatı 80 ₺, birim değişken maliyet 48 ₺ ve toplam sabit maliyet 180.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   450000, [270000, 225000, 360000], "₺",
   "Katkı oranı = (80−48)/80 = %40. Başabaş (₺) = 180.000 ÷ 0,40 = 450.000 ₺.",
   "MHK - başabaş tutar"),

cq("Katkı oranı %30 ve toplam sabit maliyet 90.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   300000, [27000, 270000, 450000], "₺",
   "Başabaş (₺) = 90.000 ÷ 0,30 = 300.000 ₺.",
   "MHK - başabaş tutar"),

cq("Toplam satışları 800.000 ₺, toplam değişken maliyeti 480.000 ₺ ve sabit maliyeti 160.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   400000, [266667, 320000, 640000], "₺",
   "Katkı oranı = (800.000−480.000)/800.000 = %40. Başabaş (₺) = 160.000 ÷ 0,40 = 400.000 ₺.",
   "MHK - başabaş tutar"),

cq("Katkı oranı %20 ve toplam sabit maliyet 150.000 ₺ olan işletmenin başabaş satış tutarı kaç ₺'dir?",
   750000, [30000, 300000, 600000], "₺",
   "Başabaş (₺) = 150.000 ÷ 0,20 = 750.000 ₺.",
   "MHK - başabaş tutar"),

# ── D. Hedef kâr için satış (8, hesap) ───────────────────────────────────────
# Miktar = (Sabit + Hedef kâr) / katkı payı
cq("Birim katkı payı 20 ₺, toplam sabit maliyet 100.000 ₺ olan işletmenin 40.000 ₺ kâr için satması gereken miktar kaç adettir?",
   7000, [5000, 2000, 8000], "adet",
   "Miktar = (sabit + hedef kâr) ÷ katkı payı = (100.000 + 40.000) ÷ 20 = 7.000 adet.",
   "MHK - hedef kâr"),

cq("Birim satış fiyatı 60 ₺, birim değişken maliyet 40 ₺, sabit maliyet 200.000 ₺ olan işletmenin 100.000 ₺ kâr için satması gereken miktar kaç adettir?",
   15000, [10000, 5000, 12000], "adet",
   "Katkı payı = 60 − 40 = 20 ₺. Miktar = (200.000 + 100.000) ÷ 20 = 15.000 adet.",
   "MHK - hedef kâr"),

cq("Birim katkı payı 25 ₺, sabit maliyet 150.000 ₺ olan işletmenin 150.000 ₺ kâr hedefi için satması gereken miktar kaç adettir?",
   12000, [6000, 9000, 15000], "adet",
   "Miktar = (150.000 + 150.000) ÷ 25 = 12.000 adet.",
   "MHK - hedef kâr"),

cq("Birim satış fiyatı 100 ₺, birim değişken maliyet 60 ₺, sabit maliyet 320.000 ₺ olan işletmenin 80.000 ₺ kâr için satması gereken miktar kaç adettir?",
   10000, [8000, 5000, 6000], "adet",
   "Katkı payı = 100 − 60 = 40 ₺. Miktar = (320.000 + 80.000) ÷ 40 = 10.000 adet.",
   "MHK - hedef kâr"),

cq("Katkı oranı %40, sabit maliyet 200.000 ₺ olan işletmenin 120.000 ₺ kâr için ulaşması gereken satış tutarı kaç ₺'dir?",
   800000, [500000, 300000, 640000], "₺",
   "Tutar = (sabit + hedef kâr) ÷ katkı oranı = (200.000 + 120.000) ÷ 0,40 = 800.000 ₺.",
   "MHK - hedef kâr tutar"),

cq("Katkı oranı %25, sabit maliyet 150.000 ₺ olan işletmenin 100.000 ₺ kâr için ulaşması gereken satış tutarı kaç ₺'dir?",
   1000000, [600000, 400000, 625000], "₺",
   "Tutar = (150.000 + 100.000) ÷ 0,25 = 1.000.000 ₺.",
   "MHK - hedef kâr tutar"),

cq("Birim katkı payı 30 ₺, sabit maliyet 90.000 ₺ olan işletmenin 60.000 ₺ kâr için satması gereken miktar kaç adettir?",
   5000, [3000, 2000, 4500], "adet",
   "Miktar = (90.000 + 60.000) ÷ 30 = 5.000 adet.",
   "MHK - hedef kâr"),

cq("Birim satış fiyatı 45 ₺, birim değişken maliyet 30 ₺, sabit maliyet 90.000 ₺ olan işletmenin 30.000 ₺ kâr için satması gereken miktar kaç adettir?",
   8000, [6000, 4000, 10000], "adet",
   "Katkı payı = 45 − 30 = 15 ₺. Miktar = (90.000 + 30.000) ÷ 15 = 8.000 adet.",
   "MHK - hedef kâr"),

# ── E. Güvenlik payı (6, hesap + kavram) ─────────────────────────────────────
cq("Fiili satışları 800.000 ₺ ve başabaş satışları 500.000 ₺ olan işletmenin güvenlik payı tutarı kaç ₺'dir?",
   300000, [500000, 1300000, 200000], "₺",
   "Güvenlik payı = fiili satış − başabaş satış = 800.000 − 500.000 = 300.000 ₺.",
   "MHK - güvenlik payı"),

cq("Fiili satışları 1.000.000 ₺ ve başabaş satışları 600.000 ₺ olan işletmenin güvenlik payı oranı yüzde kaçtır?",
   40, [60, 66.67, 20], "%",
   "Güvenlik payı oranı = (fiili − başabaş) ÷ fiili = (1.000.000 − 600.000) ÷ 1.000.000 = %40.",
   "MHK - güvenlik payı oranı"),

cq("Fiili satışları 500.000 ₺ ve başabaş satışları 400.000 ₺ olan işletmenin güvenlik payı oranı yüzde kaçtır?",
   20, [80, 25, 100], "%",
   "Güvenlik payı oranı = (500.000 − 400.000) ÷ 500.000 = %20.",
   "MHK - güvenlik payı oranı"),

cq("Başabaş satışları 300.000 ₺ ve güvenlik payı 150.000 ₺ olan işletmenin fiili satış tutarı kaç ₺'dir?",
   450000, [150000, 300000, 200000], "₺",
   "Fiili satış = başabaş + güvenlik payı = 300.000 + 150.000 = 450.000 ₺.",
   "MHK - güvenlik payı"),

kq("Güvenlik payı oranının yüksek olması bakımından aşağıdakilerden hangisi doğrudur?",
   "Satışların başabaş noktasının belirgin biçimde üstünde olduğunu ve zarara karşı direncin yüksekliğini gösterir",
   ["Satışların başabaş noktasının hemen altında olduğunu ve zarar riskinin yüksekliğini gösterir",
    "İşletmenin sabit maliyetlerinin değişken maliyetlerini fazlasıyla aştığını gösterir",
    "İşletmenin kapasitesinin tamamına yakınını kullandığını ve büyüyemeyeceğini gösterir"],
   "Yüksek güvenlik payı oranı, satışlar başabaşın çok üstünde olduğundan satışlar düşse bile zarara geçmenin zor olduğunu gösterir.",
   "MHK - güvenlik payı yorumu"),

cq("Fiili satışları 600.000 ₺ ve başabaş satışları 450.000 ₺ olan işletmenin güvenlik payı oranı yüzde kaçtır?",
   25, [75, 33.33, 15], "%",
   "Güvenlik payı oranı = (600.000 − 450.000) ÷ 600.000 = %25.",
   "MHK - güvenlik payı oranı"),

# ── F. Değişkenlerin BEP'e etkisi (8, kavram + hesap) ────────────────────────
kq("Birim satış fiyatının artması hâlinde başabaş noktası (adet) bakımından aşağıdakilerden hangisi doğrudur?",
   "Katkı payı büyüyeceğinden başabaş noktası daha az adette gerçekleşir",
   ["Katkı payı küçüleceğinden başabaş noktası daha çok adette gerçekleşir",
    "Katkı payı değişmeyeceğinden başabaş noktası hiçbir biçimde etkilenmez",
    "Sabit maliyet artacağından başabaş noktası daha yüksek bir adede çıkar"],
   "Fiyat artınca katkı payı (SF−DM) büyür; sabit maliyet aynı katkıya daha az adette ulaşılır, başabaş düşer.",
   "MHK - fiyatın etkisi"),

kq("Birim değişken maliyetin artması hâlinde başabaş noktası bakımından aşağıdakilerden hangisi doğrudur?",
   "Katkı payı azalacağından başabaş noktası daha yüksek bir satış düzeyine çıkar",
   ["Katkı payı artacağından başabaş noktası daha düşük bir satış düzeyine iner",
    "Sabit maliyet azalacağından başabaş noktası daha düşük düzeyde gerçekleşir",
    "Katkı oranı yükseleceğinden başabaş noktası hiç değişmeden aynı kalır"],
   "Değişken maliyet artınca katkı payı (SF−DM) küçülür; sabit maliyeti karşılamak için daha çok satış gerekir, başabaş yükselir.",
   "MHK - değişken maliyetin etkisi"),

kq("Toplam sabit maliyetin artması hâlinde başabaş noktası bakımından aşağıdakilerden hangisi doğrudur?",
   "Karşılanacak sabit yük büyüyeceğinden başabaş noktası daha yüksek bir düzeye çıkar",
   ["Karşılanacak sabit yük büyüse de başabaş noktası daha düşük düzeye iner",
    "Katkı payı artacağından başabaş noktası daha az satışla gerçekleşir",
    "Değişken maliyet düşeceğinden başabaş noktası değişmeden aynı kalır"],
   "Sabit maliyet artınca aynı katkı payıyla karşılanacak tutar büyür; başabaş noktası yükselir.",
   "MHK - sabit maliyetin etkisi"),

cq("Başabaş noktası 5.000 adet iken birim katkı payı 20 ₺'den 25 ₺'ye çıkarsa (sabit maliyet 100.000 ₺) yeni başabaş kaç adettir?",
   4000, [5000, 6250, 5500], "adet",
   "Yeni başabaş = 100.000 ÷ 25 = 4.000 adet; katkı payı arttığından başabaş düşer.",
   "MHK - katkı değişimi"),

cq("Sabit maliyeti 100.000 ₺ ve birim katkı payı 20 ₺ olan işletmenin sabit maliyeti 120.000 ₺'ye çıkarsa başabaş noktası kaç adet olur?",
   6000, [5000, 4000, 5833], "adet",
   "Yeni başabaş = 120.000 ÷ 20 = 6.000 adet; sabit maliyet arttığından başabaş yükselir.",
   "MHK - sabit maliyet değişimi"),

kq("Katkı payı sıfır (birim satış fiyatı = birim değişken maliyet) olduğunda başabaş bakımından aşağıdakilerden hangisi doğrudur?",
   "Her satış yalnızca kendi değişken maliyetini karşılar; sabit maliyet hiç karşılanamaz ve başabaşa ulaşılamaz",
   ["Her satış hem değişken hem sabit maliyeti karşılar; başabaşa ilk satışta ulaşılır",
    "Sabit maliyet kendiliğinden sıfırlanır ve işletme her düzeyde kâr elde eder",
    "Başabaş noktası negatif bir değere düşerek üretim öncesinde gerçekleşmiş olur"],
   "Katkı payı sıfırsa hiçbir satış sabit maliyete katkı sağlamaz; sabit maliyet karşılanamayacağı için başabaş noktası oluşmaz.",
   "MHK - katkı payı sıfır"),

cq("Birim satış fiyatı 50 ₺, birim değişken maliyet 30 ₺, sabit maliyet 100.000 ₺ olan işletme fiyatı 60 ₺'ye çıkarırsa başabaş noktası kaç adet olur?",
   100000 // 30, [5000, 2000, 4000], "adet",
   "Yeni katkı payı = 60 − 30 = 30 ₺. Başabaş = 100.000 ÷ 30 ≈ 3.333 adet; fiyat artınca başabaş düşer.",
   "MHK - fiyat değişimi hesap"),

cq("Birim satış fiyatı 40 ₺, birim değişken maliyet 20 ₺, sabit maliyet 160.000 ₺ olan işletmede değişken maliyet 24 ₺'ye çıkarsa başabaş noktası kaç adet olur?",
   10000, [8000, 6667, 9000], "adet",
   "Yeni katkı payı = 40 − 24 = 16 ₺. Başabaş = 160.000 ÷ 16 = 10.000 adet; değişken maliyet artınca başabaş yükselir.",
   "MHK - değişken maliyet hesap"),

# ── G. Katkı oranı / faaliyet kaldıracı / kâr (6, hesap) ─────────────────────
cq("Birim satış fiyatı 80 ₺ ve birim değişken maliyet 60 ₺ olan ürünün katkı oranı yüzde kaçtır?",
   25, [75, 33.33, 20], "%",
   "Katkı payı = 80 − 60 = 20 ₺. Katkı oranı = 20 ÷ 80 = %25.",
   "MHK - katkı oranı hesap"),

cq("Toplam katkı payı 300.000 ₺ ve faaliyet kârı 100.000 ₺ olan işletmenin faaliyet kaldıracı derecesi kaçtır?",
   3, [0.33, 4, 2], "",
   "Faaliyet kaldıracı = toplam katkı payı ÷ faaliyet kârı = 300.000 ÷ 100.000 = 3.",
   "MHK - faaliyet kaldıracı hesap"),

cq("Faaliyet kaldıracı 4 olan işletmenin satışları %10 artarsa faaliyet kârı yüzde kaç artar?",
   40, [10, 4, 14], "%",
   "Kâr değişimi = faaliyet kaldıracı × satış değişimi = 4 × %10 = %40.",
   "MHK - kaldıraç etkisi"),

cq("Satışları 10.000 adet, birim katkı payı 20 ₺ ve sabit maliyeti 100.000 ₺ olan işletmenin faaliyet kârı kaç ₺'dir?",
   100000, [200000, 300000, 120000], "₺",
   "Toplam katkı = 10.000 × 20 = 200.000 ₺. Faaliyet kârı = 200.000 − 100.000 = 100.000 ₺.",
   "MHK - kâr hesabı"),

cq("Satışları 8.000 adet, birim satış fiyatı 50 ₺, birim değişken maliyet 30 ₺ ve sabit maliyeti 100.000 ₺ olan işletmenin faaliyet kârı kaç ₺'dir?",
   60000, [160000, 300000, 40000], "₺",
   "Katkı payı = 50 − 30 = 20 ₺. Toplam katkı = 8.000 × 20 = 160.000 ₺. Kâr = 160.000 − 100.000 = 60.000 ₺.",
   "MHK - kâr hesabı"),

cq("Toplam satışları 600.000 ₺, değişken maliyeti 360.000 ₺ ve sabit maliyeti 150.000 ₺ olan işletmenin faaliyet kârı kaç ₺'dir?",
   90000, [240000, 240000 - 60000 + 1, 60000], "₺",
   "Toplam katkı = 600.000 − 360.000 = 240.000 ₺. Faaliyet kârı = 240.000 − 150.000 = 90.000 ₺.",
   "MHK - kâr hesabı"),

# ── H. Çok ürün / karışım + genel (6, kavram) ────────────────────────────────
kq("Birden fazla ürün üreten işletmede başabaş analizi bakımından aşağıdakilerden hangisi doğrudur?",
   "Başabaş, ürünlerin belirli bir satış karışımı varsayımı altında ağırlıklı katkı payıyla hesaplanır",
   ["Başabaş, her ürün için ayrı ayrı bulunup toplanır; satış karışımının hiçbir etkisi olmaz",
    "Başabaş yalnızca en çok satan tek ürün dikkate alınarak tek katkı payıyla bulunur",
    "Çok ürünlü işletmelerde başabaş noktası hesaplanamaz; yalnızca tek ürün için mümkündür"],
   "Çok ürünlü işletmede başabaş, sabit satış karışımı varsayımıyla ağırlıklı ortalama katkı payı üzerinden hesaplanır; karışım değişirse başabaş da değişir.",
   "MHK - çok ürünlü başabaş"),

kq("Satış karışımının değişmesi hâlinde başabaş noktası bakımından aşağıdakilerden hangisi doğrudur?",
   "Ağırlıklı ortalama katkı payı değişeceğinden başabaş noktası da değişir",
   ["Ağırlıklı ortalama katkı payı değişse de başabaş noktası her hâlde sabit kalır",
    "Satış karışımı yalnızca toplam sabit maliyeti değiştirir, başabaşı etkilemez",
    "Satış karışımı yalnızca değişken maliyeti sıfırlayarak kârı garantiye alır"],
   "Karışımdaki yüksek katkılı ürün payı artarsa ağırlıklı katkı yükselir, başabaş düşer; tersi durumda başabaş yükselir.",
   "MHK - satış karışımı"),

kq("Başabaş noktasında faaliyet kârı bakımından aşağıdakilerden hangisi doğrudur?",
   "Toplam katkı payı toplam sabit maliyete tam eşit olduğundan faaliyet kârı sıfırdır",
   ["Toplam katkı payı toplam sabit maliyeti aştığından faaliyet kârı en yüksektir",
    "Toplam katkı payı sıfır olduğundan işletme en yüksek zararı bu noktada yazar",
    "Toplam değişken maliyet sıfırlandığından faaliyet kârı sabit maliyete eşittir"],
   "Başabaşta toplam katkı payı = toplam sabit maliyet olduğundan, katkıdan sabit düşülünce faaliyet kârı tam sıfır çıkar.",
   "MHK - başabaşta kâr"),

kq("Katkı payı yaklaşımında faaliyet kârı bakımından aşağıdakilerden hangisi doğrudur?",
   "Toplam katkı payından toplam sabit maliyet düşülerek faaliyet kârına ulaşılır",
   ["Toplam satış tutarından yalnızca sabit maliyet düşülerek faaliyet kârına ulaşılır",
    "Toplam katkı payına toplam sabit maliyet eklenerek faaliyet kârına ulaşılır",
    "Toplam değişken maliyetten toplam sabit maliyet düşülerek faaliyet kârına ulaşılır"],
   "Katkı payı yaklaşımında: satış − değişken maliyet = katkı payı; katkı payı − sabit maliyet = faaliyet kârı.",
   "MHK - katkı payı yaklaşımı"),

kq("Başabaş noktasının üstündeki her ek satış bakımından aşağıdakilerden hangisi doğrudur?",
   "Sabit maliyet zaten karşılandığından her ek satışın katkı payı doğrudan kâra eklenir",
   ["Sabit maliyet henüz karşılanmadığından her ek satış önce zararı büyütür",
    "Her ek satış hem değişken hem sabit maliyeti yeniden doğurduğundan kâr değişmez",
    "Başabaşın üstündeki satışlar katkı payını sıfırladığından kâra hiç katkı vermez"],
   "Başabaşta sabit maliyet tümüyle karşılanmıştır; bu noktadan sonra her ek birimin katkı payı doğrudan faaliyet kârına eklenir.",
   "MHK - başabaş üstü satış"),

kq("Nakit başabaş noktası bakımından aşağıdakilerden hangisi doğrudur?",
   "Sabit maliyetlerden nakit çıkışı gerektirmeyen amortisman düşülerek hesaplanan başabaş düzeyidir",
   ["Tüm sabit maliyetlere amortisman iki kez eklenerek bulunan başabaş düzeyidir",
    "Yalnızca değişken maliyetler dikkate alınarak sabit maliyetin sıfır sayıldığı düzeydir",
    "İşletmenin bankadaki nakit mevcuduna eşit satış yaptığı özel üretim düzeyidir"],
   "Nakit başabaşta, sabit maliyetlerden nakit çıkışı doğurmayan amortisman gibi kalemler çıkarılır; bu yüzden nakit başabaş, normal başabaştan daha düşük satışta gerçekleşir.",
   "MHK - nakit başabaş"),


# Kavram sorularının 5. şıkkı (4. çeldirici) — SORUYA ÖZGÜ yanlış ifade (tekrarlı
# atma-şıkkı YASAK). stem başı ile eşleştirilir.
FOURTH = {
 "Katkı payı (katkı marjı)": "Birim değişken maliyetten birim sabit maliyetin çıkarılmasıyla bulunan tutardır",
 "Başabaş noktası bakımından": "Toplam değişken maliyetin toplam sabit maliyeti tam karşıladığı üretim düzeyidir",
 "Sabit maliyet bakımından": "Üretim hiç yapılmadığında en yüksek olan, üretim arttıkça toplamı azalan maliyettir",
 "Değişken maliyet bakımından": "Üretim hacmi arttıkça birim başına tutarı artan, toplamı sabit kalan maliyettir",
 "Katkı oranı (katkı payı oranı)": "Toplam değişken maliyetin toplam satış tutarına bölünmesiyle bulunan orandır",
 "Güvenlik payı (emniyet marjı)": "Başabaş satışları ile işletmenin toplam sabit maliyeti arasındaki olumlu farkı gösteren bir güvenlik tutarıdır",
 "Maliyet-hacim-kâr analizinin varsayımları": "Üretilen tüm birimlerin stokta bekletildiği ve dönemde hiç satılmadığı varsayılır",
 "Faaliyet kaldıracı bakımından": "Faaliyet kârının toplam katkı payına bölünmesiyle bulunan, daima birden küçük bir orandır",
 "Güvenlik payı oranının yüksek olması": "İşletmenin değişken maliyetlerinin tamamını sabit maliyete dönüştürerek toplam riskini azalttığını ve kârını güvenceye aldığını gösterir",
 "Birim satış fiyatının artması": "Sabit maliyet de aynı oranda artacağından başabaş noktası hiç değişmeden kalır",
 "Birim değişken maliyetin artması": "Birim satış fiyatı da kendiliğinden artacağından başabaş noktası düşer",
 "Toplam sabit maliyetin artması": "Birim katkı payı da kendiliğinden artacağından başabaş noktası tam tersine daha düşük bir satış düzeyine iner",
 "Katkı payı sıfır": "Katkı payı sıfır olsa bile her satış sabit maliyeti de karşıladığından başabaş noktasına daha ilk satışta ulaşılmış olur",
 "Birden fazla ürün üreten işletmede": "Başabaş, ürünlerin toplam satış adedinin tek bir ortalama katkı payına bölünmesiyle ve satış karışımı göz ardı edilerek bulunur",
 "Satış karışımının değişmesi": "Satış karışımı yalnızca birim satış fiyatını değiştirir, katkı payını etkilemez",
 "Başabaş noktasında faaliyet kârı": "Toplam satış tutarı sıfıra indiğinden faaliyet kârı da sıfıra eşit olur",
 "Katkı payı yaklaşımında faaliyet kârı": "Toplam satış tutarına toplam değişken maliyet eklenerek faaliyet kârına ulaşılır",
 "Başabaş noktasının üstündeki her ek satış": "Başabaşın üstünde birim değişken maliyet sıfırlandığından satış tümüyle kâra geçer",
 "Nakit başabaş noktası": "Nakit satışların kredili satışlara tam olarak eşitlendiği ve işletmenin dönem içinde hiç borçlanmadığı özel bir başabaş düzeyidir",
}


def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i - 1] == base[i - 2]) for i in range(2, len(base))):
            return base


def five_options(it, ans, rng):
    """4 şıklı içeriği 5 şıklığa tamamla: hesapta 4. sayısal çeldirici, kavramda
    4. metin çeldirici zaten var mı? cq 3 çeldirici verir → 4 şık; +1 gerek.
    kq 3 çeldirici verir → 4 şık; +1 gerek. Beşinciyi türet."""
    opts = {ans: it["correct"]}
    dist = list(it["distractors"])
    return opts, dist


if __name__ == "__main__":
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    # Her soru 1 doğru + 3 çeldirici = 4 şık. SGS 5 şıklı → 4. çeldiriciyi türet.
    rng = random.Random(SEED)
    for it in Q:
        if it["calc"]:
            # sayısal 4. çeldirici: mevcut sayısal şıklardan türet (birimi koru)
            import re
            def num(s):
                m = re.findall(r"[\d\.]+", s.replace(".", ""))
                return int(m[0]) if m else 0
            unit = it["correct"].split(" ", 1)[1] if " " in it["correct"] else ""
            base_vals = {num(it["correct"])} | {num(d) for d in it["distractors"]}
            cand = None
            cbase = num(it["correct"])
            for mult in (2, 3, 1.5, 0.5, 0.75, 4):
                v = int(cbase * mult)
                if v not in base_vals and v > 0:
                    cand = v
                    break
            lab = f"{fmt(cand)} {unit}".strip()
            if lab not in [it["correct"]] + it["distractors"]:
                it["distractors"].append(lab)
        else:
            # kavramsal 4. çeldirici: soruya ÖZGÜ (FOURTH); tekrarlı atma-şıkkı yok
            key = next((k for k in FOURTH if it["stem"].startswith(k)), None)
            assert key, "FOURTH eksik: " + it["stem"][:50]
            dd = FOURTH[key]
            assert dd not in [it["correct"]] + it["distractors"], "4. çeldirici tekrar: " + key
            it["distractors"].append(dd)
        assert len(it["distractors"]) == 4, "4 çeldirici olmalı: " + it["stem"][:40]

    letters = gen_letters(len(Q), SEED)
    out = []
    for i, it in enumerate(Q):
        ans = letters[i]
        opts = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            opts[k] = d
        assert len(set(opts.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı ({it['stem'][:30]})"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "ders": DERS, "konu": KONU,
            "stem": it["stem"], "options": opts, "answer": ans,
            "solution": it["why"] + f" Doğru cevap {ans}.",
            "source": {"kind": "generated",
                       "styleRef": "SGS Maliyet Muhasebesi / Başabaş (MHK; sınav stiline kalibre)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })

    import sys, os
    sys.path.insert(0, "tools/sgs")
    from audit import kor_ogrenci
    from collections import Counter
    puan, strateji = kor_ogrenci(out)
    rank = Counter()
    for q0 in out:
        lens = sorted((len(v), k) for k, v in q0["options"].items())
        rank[[k for _, k in lens].index(q0["answer"]) + 1] += 1
    print(f"kör: {puan}% ← {strateji} | boy-sırası {dict((r, rank[r]) for r in range(1,6))}")
    if puan > 30:
        print(f"  ⚠ %{puan} — kavram şıklarını dengele (fix_basabas_boy.py)")

    for path in (OUT_APP, OUT_CONTENT):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yazıldı {len(out)} soru → iki repo | harf {''.join(x['answer'] for x in out)}")
