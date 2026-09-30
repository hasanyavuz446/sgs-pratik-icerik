# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Dikey (Yüzde) Analiz — 60 soru, 2026 test biçimi.

Bilanço kalemleri aktif (pasif) toplamının, gelir tablosu kalemleri net satışların yüzdesi olarak ortak
tablolara bağlı sorulur (brüt satışlar %100'ü aşar). Dikey yüzdelerden geriye tutar hesabı, yüzdeler
arası ilişki (brüt kâr − faaliyet giderleri) ve ortak ölçekli tablo yorumları da yer alır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from fta_ortak import Sirket, Fta, Hesap, AD

P = Paket("questions_topic_dikey_analiz_2026.json", lesson="mali_tablolar_analizi", topic="dikey_analiz",
          konu_adi="Dikey Analiz", seed=2026093102,
          surum="Finansal tablolar analizi: dikey (yüzde) analiz yöntemi; 30.09.2026 kontrolü")
F = Fta(P, "yet-fta-dikey-")
R = "Dikey (yüzde) analiz"
Y = ("2023", "2024", "2025")

d_def = Sirket("DEF A.Ş.", Y,
               hd=[50_000, 40_000, 60_000], ta=[300_000, 360_000, 390_000], stok=[250_000, 300_000, 350_000],
               mdv=[800_000, 850_000, 900_000], modv=[100_000, 90_000, 100_000], tb=[200_000, 260_000, 300_000],
               uvmb=[350_000, 300_000, 320_000], sermaye=[600_000] * 3, gyk=[50_000, 80_000, 110_000],
               brut=[2_040_000, 2_450_000, 2_900_000], ind=[40_000, 50_000, 100_000],
               smm=[1_500_000, 1_800_000, 2_100_000], fg=[300_000, 380_000, 450_000], fin=[60_000, 70_000, 90_000])
d_hjk = Sirket("HJK A.Ş.", Y,
               hd=[30_000, 45_000, 25_000], mk=[10_000, 15_000, 20_000], ta=[180_000, 220_000, 260_000],
               stok=[160_000, 210_000, 280_000], ddv=[20_000, 30_000, 25_000], mdv=[600_000, 640_000, 700_000],
               modv=[40_000, 40_000, 50_000], tb=[150_000, 190_000, 240_000], db=[20_000, 25_000, 30_000],
               uvmb=[250_000, 280_000, 260_000], sermaye=[400_000] * 3, gyk=[30_000, 50_000, 70_000],
               brut=[1_530_000, 1_840_000, 2_150_000], ind=[30_000, 40_000, 50_000],
               smm=[1_080_000, 1_310_000, 1_560_000], fg=[240_000, 290_000, 330_000], fin=[50_000, 60_000, 80_000])
d_mnp = Sirket("MNP A.Ş.", Y,
               hd=[60_000, 35_000, 40_000], ta=[400_000, 460_000, 500_000], da=[20_000, 25_000, 30_000],
               stok=[320_000, 380_000, 430_000], mdv=[1_100_000, 1_150_000, 1_250_000],
               modv=[80_000, 100_000, 120_000], tb=[280_000, 330_000, 380_000], uvmb=[450_000, 500_000, 480_000],
               sermaye=[900_000] * 3, gyk=[40_000, 60_000, 90_000], brut=[3_060_000, 3_570_000, 4_100_000],
               ind=[60_000, 70_000, 100_000], smm=[2_250_000, 2_660_000, 3_040_000],
               fg=[480_000, 520_000, 600_000], fin=[110_000, 130_000, 150_000])

ORTAK = {}
for s, sid, v, secim in [
    (d_def, "yet-fta-dikey-def", 0, [("brut", 2024), ("smm", 2025), ("bk", 2023), ("fk", 2024), ("nk", 2025),
                                     ("ind", 2025), ("fin", 2023), ("hd", 2023), ("ta", 2025), ("stok", 2024),
                                     ("dv", 2025), ("kvmb", 2024), ("ok", 2023), ("uvyk", 2025)]),
    (d_hjk, "yet-fta-dikey-hjk", 1, [("brut", 2023), ("ind", 2024), ("smm", 2024), ("fg", 2025), ("dk", 2025),
                                     ("nk", 2023), ("bk", 2025), ("stok", 2025), ("mdv", 2024), ("kvyk", 2023),
                                     ("tb", 2025), ("fk", 2023), ("ok", 2025), ("mk", 2024)]),
    (d_mnp, "yet-fta-dikey-mnp", 3, [("brut", 2025), ("smm", 2023), ("fk", 2025), ("fin", 2024), ("fg", 2023),
                                     ("nk", 2024), ("ta", 2024), ("hd", 2025), ("da", 2023), ("dv", 2023),
                                     ("kvmb", 2025), ("tb", 2024), ("uvyk", 2023), ("ok", 2024)]),
]:
    ORTAK[sid] = F.uyaran(s.uyaran(sid))
    for a, y in secim:
        F.ifade(s, sid, s.dikey(a, str(y)), [f"{y} yılı dikey yüzde analizinde {AD[a]} kaleminin payı",
                                             f"{y} yılı ortak ölçekli tablosunda {AD[a]} kalemine düşen oran",
                                             f"{y} yılı dikey analizinde {AD[a]} kaleminin taban içindeki payı"], v, R)

# ------------------------------------------------------------------ dikey yüzdeden tutara
F.hesap(R,
    "Bir firmada gelir tablosunun dikey yüzde analizine göre faaliyet kârı %15, brüt satışlar %102 olarak "
    "hesaplanmıştır. Firmanın brüt satışları 612.000 ₺’dir.\n\nFirmanın faaliyet kârı kaç ₺’dir?",
    Hesap(612_000 / 1.02 * 0.15, "tutar", [612_000 * 0.15, 612_000 * 0.15 / 1.02 * 0.98, 612_000 * 0.17, 612_000 * 0.13],
          "Gelir tablosunda baz net satışlardır: net satışlar = 612.000 ÷ 1,02 = 600.000 ₺. Faaliyet kârı = 600.000 × "
          "%15 = 90.000 ₺. Oranın brüt satışlara uygulanması 91.800 ₺ verir."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin gelir tablosu dikey analizinde satış indirimleri %2,5 olarak hesaplanmıştır. Aynı dönemde satış "
    "indirimlerinin tutarı 30.000 ₺’dir.\n\nİşletmenin brüt satışları kaç ₺’dir?",
    Hesap(30_000 / 0.025 + 30_000, "tutar", [30_000 / 0.025, 30_000 / 0.025 - 30_000, 30_000 * 40, 30_000 / 0.0275],
          "Dikey yüzdeler net satışlara göre hesaplanır: net satışlar = 30.000 ÷ 0,025 = 1.200.000 ₺. Brüt satışlar = "
          "net satışlar + satış indirimleri = 1.230.000 ₺ (dikey yüzdesi %102,5)."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin bilançosunun dikey analizinde stoklar aktif toplamının %20’si olarak hesaplanmıştır. Dönem sonu "
    "stok tutarı 180.000 ₺, dönen varlıklar ise 405.000 ₺’dir.\n\nİşletmenin aktif toplamı kaç ₺’dir?",
    Hesap(180_000 / 0.20, "tutar", [180_000 * 5 - 405_000, 405_000 / 0.20, 180_000 / 0.45, 180_000 * 1.2],
          "Aktif toplamı = stoklar ÷ stokların dikey yüzdesi = 180.000 ÷ 0,20 = 900.000 ₺. Dönen varlıkların payı "
          "405.000 ÷ 900.000 = %45’tir."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin pasif toplamı 2.000.000 ₺’dir. Bilançonun dikey analizinde kısa vadeli yabancı kaynakların payı "
    "%35, uzun vadeli yabancı kaynakların payı %25 olarak bulunmuştur.\n\nİşletmenin öz kaynak tutarı kaç ₺’dir?",
    Hesap(2_000_000 * 0.40, "tutar", [2_000_000 * 0.60, 2_000_000 * 0.65, 2_000_000 * 0.75, 2_000_000 * 0.35],
          "Öz kaynakların payı = %100 − %35 − %25 = %40; tutarı = 2.000.000 × %40 = 800.000 ₺."), zorluk="easy")

F.hesap(R,
    "Satış indirimi bulunmayan bir işletmenin gelir tablosu dikey analizinde satışların maliyetinin payı bir yıl "
    "içinde %72’den %76’ya yükselmiştir. Faaliyet giderlerinin payı her iki yılda da %14’tür.\n\nİkinci yılda "
    "faaliyet kârının dikey yüzdesi kaçtır?",
    Hesap(100 - 76 - 14, "yuzde", [100 - 72 - 14, 100 - 76, 76 - 72 + 14 - 4, 100 - 76 + 14],
          "Brüt satış kârının payı = %100 − %76 = %24; faaliyet kârı payı = %24 − %14 = %10. Bir önceki yıl bu pay %14 "
          "idi; maliyet payındaki 4 puanlık artış kârlılığı aynı ölçüde düşürmüştür."))

F.hesap(R,
    "Bir işletmenin gelir tablosu dikey analizinde brüt satış kârı %30, faaliyet kârı %12 olarak hesaplanmıştır. "
    "Gelir tablosunda brüt kâr ile faaliyet kârı arasında yalnız faaliyet giderleri bulunmaktadır.\n\nFaaliyet "
    "giderlerinin dikey yüzdesi kaçtır?",
    Hesap(30 - 12, "yuzde", [30 + 12, 12, 30, 70 - 12],
          "Faaliyet kârı = brüt satış kârı − faaliyet giderleri olduğundan faaliyet giderlerinin payı = %30 − %12 = "
          "%18’dir."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin bilançosunda duran varlıkların aktif toplamındaki payı %64 olup aktif toplamı 3.500.000 "
    "₺’dir. Dönen varlıklar içinde hazır değerler 140.000 ₺’dir.\n\nHazır değerlerin dönen varlıklar içindeki payı "
    "yüzde (%) kaçtır?",
    Hesap(140_000 / (3_500_000 * 0.36) * 100, "yuzde", [140_000 / 3_500_000 * 100, 140_000 / (3_500_000 * 0.64) * 100,
                                                         36, 140_000 / 3_500_000 * 100 * 0.64],
          "Dönen varlıklar = 3.500.000 × (1 − 0,64) = 1.260.000 ₺. Hazır değerlerin grup içi payı = 140.000 ÷ "
          "1.260.000 = %11,11; aktif toplamı içindeki payı ise %4’tür."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin net satışları 2.500.000 ₺’dir. Gelir tablosunun dikey analizinde dönem net kârı %6, finansman "
    "giderleri %3 olarak hesaplanmıştır.\n\nİşletmenin dönem net kârı kaç ₺’dir?",
    Hesap(2_500_000 * 0.06, "tutar", [2_500_000 * 0.09, 2_500_000 * 0.03, 2_500_000 * 0.06 * 0.75, 2_500_000 * 0.94],
          "Dikey yüzde net satışlara göre hesaplandığından dönem net kârı = 2.500.000 × %6 = 150.000 ₺."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin bilançosunun dikey analizinde kısa vadeli yabancı kaynakların toplam payı %40’tır. Bu grup içinde "
    "ticari borçların payı %22, diğer borçların payı %3 olup geri kalanı kısa vadeli mali borçlardır.\n\nKısa vadeli "
    "mali borçların pasif toplamındaki payı yüzde (%) kaçtır?",
    Hesap(40 - 22 - 3, "yuzde", [40 - 22, 22 + 3, 40 + 22 + 3, 60 - 22 - 3],
          "Kısa vadeli mali borçlar = KVYK payı − ticari borçlar − diğer borçlar = %40 − %22 − %3 = %15."))

F.hesap(R,
    "Bir işletmenin gelir tablosu dikey analizinde brüt satışlar %104, satışların maliyeti %68 olarak "
    "hesaplanmıştır. Satış indirimleri dışında brüt satışlardan indirim yoktur.\n\nBrüt satış kârının brüt satışlara "
    "oranı yüzde (%) kaçtır?",
    Hesap(32 / 104 * 100, "yuzde", [32, 36, 104 - 68, 32 / 100 * 104],
          "Brüt satış kârının dikey yüzdesi = %100 − %68 = %32 (net satışlara göre). Brüt satışlara oranı = 32 ÷ 104 = "
          "%30,77’dir; iki taban karıştırılmamalıdır."), zorluk="hard")

# ------------------------------------------------------------------ kavram ve yorum
F.q(R,
    "Bir analist, iki işletmenin gelir tablolarını ortak ölçekli (common-size) biçimde hazırlamak için her kalemi "
    "aynı tabana bölmektedir. İşletmelerden birinin satış indirimleri yüksektir.\n\nGelir tablosunun dikey "
    "analizinde taban (%100) olarak alınan kalem aşağıdakilerden hangisidir?",
    "Net satışlar",
    ["Brüt satışlar", "Satışların maliyeti", "Brüt satış kârı", "Faaliyet kârı"],
    "Gelir tablosunun dikey analizinde net satışlar %100 kabul edilir; bu nedenle satış indirimleri olan işletmelerde "
    "brüt satışların dikey yüzdesi %100’ün üzerinde çıkar.", zorluk="easy")

F.q(R,
    "Bir işletmenin bilançosunun dikey analizinde hazır değerlerin payı üç yılda %8’den %2’ye düşerken stokların "
    "payı %15’ten %27’ye çıkmıştır. Kısa vadeli yabancı kaynakların payı değişmemiştir.\n\nBu gelişmeye ilişkin "
    "aşağıdaki yorumlardan hangisi doğrudur?",
    "Varlık yapısı paraya çevrilmesi güç kalemlere kaymış, likidite zayıflamıştır.",
    ["Varlık yapısı hazır değerlere kaymış, likidite güçlenmiştir.",
     "Stok payı arttığı için asit-test oranı yükselmiştir.",
     "KVYK payı değişmediğinden likidite üzerinde etki oluşmamıştır.",
     "Hazır değerlerin payı düştüğünden cari oran da aynı ölçüde azalmıştır."],
    "En likit kalemin payı azalırken paraya çevrilmesi en uzun süren stokların payı artmıştır. KVYK payı aynı "
    "kaldığından asit-test oranı düşer; dönen varlıkların yapısı likidite aleyhine değişmiştir.")

F.q(R,
    "Bir işletmenin gelir tablosu dikey analizinde satışların maliyetinin payı %70’ten %77’ye yükselmiş, faaliyet "
    "giderlerinin payı %15 düzeyinde sabit kalmıştır.\n\nBu değişimin sonucu aşağıdakilerden hangisidir?",
    "Brüt kâr ve faaliyet kârı payları 7 puan azalmıştır.",
    ["Brüt kâr payı 7 puan artmış, faaliyet kârı payı değişmemiştir.",
     "Faaliyet kârı payı 7 puan artmış, brüt kâr payı azalmıştır.",
     "Satış hacmi arttığı için kârlılık payları değişmemiştir.",
     "Faaliyet giderleri sabit kaldığından faaliyet kârı payı artmıştır."],
    "Brüt kâr payı %30’dan %23’e, faaliyet kârı payı (%30 − %15) %15’ten (%23 − %15) %8’e düşer; her iki pay 7 puan "
    "azalmıştır.")

F.q(R,
    "Bir finansal analiz eğitiminde katılımcılara dikey analiz yöntemiyle ilgili ifadeler dağıtılmış ve hatalı olanı "
    "bulmaları istenmiştir.\n\nDikey analizle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Kalemlerin yıllar içindeki değişim hızını bir baz yıla göre gösterir.",
    ["Farklı büyüklükteki işletmelerin karşılaştırılmasını kolaylaştırır.",
     "Bilançoda her kalem aktif (pasif) toplamının yüzdesi olarak yazılır.",
     "Gelir tablosunda her kalem net satışların yüzdesi olarak yazılır.",
     "Tek bir dönemin finansal yapısını oransal olarak gösterir."],
    "Kalemlerin bir baz yıla göre gelişimini gösteren yöntem trend (eğilim yüzdeleri) analizidir. Dikey analiz her "
    "dönemin kalemlerini aynı dönemin toplamına göre yüzdelendirir.")

F.q(R,
    "Bir işletmenin brüt satışlarının dikey yüzdesi %103, net satışlarınınki %100 olarak hesaplanmıştır. İşletme "
    "yöneticisi brüt satışların %100’ü aşmasını hata sanmaktadır.\n\nBu durumun nedeni aşağıdakilerden hangisidir?",
    "Brüt satışlardan satış indirimlerinin düşülmesi",
    ["Satışların maliyetinin net satışlardan büyük olması",
     "Faaliyet giderlerinin brüt satışlara eklenmesi",
     "Diğer faaliyet gelirlerinin satışlara katılması",
     "Stokların dönem içinde artmış olması"],
    "Dikey analizde taban net satışlardır. Net satışlar = brüt satışlar − satış indirimleri olduğundan indirim varsa "
    "brüt satışlar net satışlardan büyük olur ve dikey yüzdesi %100’ü aşar; bu örnekte indirimler %3’tür.")

F.q(R,
    "Aynı sektörde faaliyet gösteren A işletmesinin aktif toplamı 50 milyon ₺, B işletmesininki 4 milyon ₺’dir. "
    "Analist, iki işletmenin varlık ve kaynak yapısını karşılaştırmak istemektedir.\n\nBu karşılaştırma için en "
    "uygun analiz aşağıdakilerden hangisidir?",
    "Dikey analiz",
    ["Trend analizi", "Karşılaştırmalı tablolar analizi", "Nakit akış analizi", "Başabaş analizi"],
    "Dikey analiz tutarları toplamın yüzdesine çevirdiğinden büyüklük farkını ortadan kaldırır ve farklı ölçekteki "
    "işletmelerin yapısal karşılaştırmasını sağlar.", zorluk="easy")

F.q(R,
    "Bir işletmenin gelir tablosu dikey analizinde finansman giderlerinin payı iki yılda %2’den %6’ya yükselmiş, "
    "faaliyet kârı payı %10’da kalmıştır.\n\nBu gelişmeye ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Faaliyet kârının daha büyük kısmı faize gitmekte, borçlanma yükü artmaktadır.",
    ["Faaliyet kârı değişmediğinden net kârlılık da değişmemiştir.",
     "Finansman giderleri arttığı için brüt kâr payı düşmüştür.",
     "İşletmenin borçlanması azalmış, finansal risk düşmüştür.",
     "Finansman giderleri faaliyet giderleri içinde yer aldığından sonuç değişmez."],
    "Faaliyet kârı payı sabitken finansman giderlerinin payı üç katına çıkmıştır; dönem kârı payı %8’den %4’e iner. "
    "Bu, borçlanma yükünün arttığını ve finansal riskin yükseldiğini gösterir.")

F.q(R,
    "Bir işletmenin bilançosunun dikey analizinde öz kaynakların payı %45’ten %30’a düşmüş, uzun vadeli yabancı "
    "kaynakların payı değişmemiştir.\n\nBu değişime ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Kısa vadeli yabancı kaynakların payı 15 puan artmıştır.",
    ["Uzun vadeli yabancı kaynakların payı 15 puan artmıştır.",
     "Kaldıraç oranı 15 puan azalmıştır.",
     "Öz kaynak tutarı 15 puan oranında azalmıştır.",
     "Duran varlıkların payı 15 puan azalmıştır."],
    "Pasif toplamı %100 olduğundan öz kaynak payındaki 15 puanlık düşüş, UVYK payı değişmediği için KVYK payının 15 "
    "puan artmasıyla karşılanır. Tutarların değil payların değiştiği unutulmamalıdır.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(F.yaz())
