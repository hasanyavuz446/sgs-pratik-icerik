# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Oran Analizi — 60 soru, 2026 test biçimi.

Gerçek kitapçıklardaki gibi soruların çoğu ortak bir bilanço + gelir tablosuna bağlıdır: likidite (cari,
asit-test, nakit oranı, net işletme sermayesi), faaliyet (stok, alacak, borç ve aktif devir hızı/süresi),
kârlılık ve mali yapı oranları. Bir üretim işletmesinin maliyet tablosundan stok türlerine göre devir
süreleri, hedef değerden geriye hesap (tahsil/ödeme süresi, likidite hedefi) ve işlem etkisi yorumları
da sorulur. Devir hızı ve sürelerinde ortalama değer ve 360 gün kullanılır; bu kural ortak tablonun
açıklamasında ve bağımsız sorularda kökte belirtilir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl
from fta_ortak import Sirket, Fta, Hesap, bicimle

P = Paket("questions_topic_oran_analizi_2026.json", lesson="mali_tablolar_analizi", topic="oran_analizi",
          konu_adi="Oran Analizi", seed=2026093101,
          surum="Finansal tablolar analizi genel kabul görmüş oran tanımları; 30.09.2026 kontrolü")
F = Fta(P, "yet-fta-oran-")
R = "Finansal oran analizi"
Y = ("2023", "2024", "2025")

klm = Sirket("KLM A.Ş.", Y,
             hd=[40_000, 55_000, 30_000], ta=[260_000, 300_000, 340_000], stok=[300_000, 360_000, 420_000],
             mdv=[900_000, 950_000, 1_020_000], modv=[60_000, 55_000, 50_000], tb=[180_000, 220_000, 260_000],
             uvmb=[400_000, 380_000, 340_000], sermaye=[500_000] * 3, gyk=[40_000, 70_000, 110_000],
             brut=[2_450_000, 2_900_000, 3_300_000], ind=[50_000, 60_000, 100_000],
             smm=[1_800_000, 2_100_000, 2_380_000], fg=[380_000, 470_000, 540_000], fin=[90_000, 110_000, 120_000])
nop = Sirket("NOP A.Ş.", Y,
             hd=[80_000, 60_000, 45_000], mk=[20_000, 30_000, 25_000], ta=[420_000, 480_000, 560_000],
             da=[30_000, 40_000, 35_000], stok=[350_000, 520_000, 610_000], mdv=[1_200_000, 1_260_000, 1_300_000],
             modv=[100_000, 120_000, 110_000], tb=[300_000, 420_000, 500_000], db=[40_000, 50_000, 60_000],
             uvmb=[500_000, 450_000, 520_000], sermaye=[800_000] * 3, gyk=[60_000, 90_000, 120_000],
             brut=[3_050_000, 3_600_000, 4_080_000], ind=[50_000, 100_000, 80_000],
             smm=[2_250_000, 2_700_000, 3_100_000], fg=[450_000, 520_000, 560_000], fin=[140_000, 160_000, 180_000])
rst = Sirket("RST A.Ş.", Y,
             hd=[25_000, 15_000, 20_000], ta=[150_000, 170_000, 190_000], stok=[90_000, 110_000, 140_000],
             mdv=[700_000, 760_000, 800_000], modv=[30_000, 40_000, 45_000], tb=[120_000, 180_000, 210_000],
             uvmb=[200_000, 160_000, 120_000], sermaye=[400_000] * 3, gyk=[20_000, 35_000, 60_000],
             brut=[1_220_000, 1_410_000, 1_640_000], ind=[20_000, 10_000, 40_000],
             smm=[840_000, 980_000, 1_150_000], fg=[210_000, 240_000, 260_000], fin=[50_000, 60_000, 70_000])
assert rst.x("dv", "2025") < rst.x("kvyk", "2025")  # negatif net işletme sermayesi sorusu için

S_KLM = F.uyaran(klm.uyaran("yet-fta-oran-klm"))
S_NOP = F.uyaran(nop.uyaran("yet-fta-oran-nop"))
S_RST = F.uyaran(rst.uyaran("yet-fta-oran-rst"))

for m, y in [("cari", 2025), ("likidite", 2024), ("nis", 2024), ("stok_sure", 2025), ("alacak_sure", 2024),
             ("borc_sure", 2025), ("aktif_hiz", 2024), ("brut_marj", 2023), ("faal_marj", 2025),
             ("varlik_karl", 2024), ("ozk_karl", 2025), ("kaldirac", 2023), ("ds_oran", 2025), ("borc_ozk", 2024)]:
    F.olcu(klm, S_KLM, m, y, 0, R)
for m, y in [("cari", 2024), ("likidite", 2025), ("nakit_orani", 2023), ("nis", 2025), ("stok_hiz", 2024),
             ("alacak_sure", 2025), ("borc_sure", 2024), ("dv_hiz", 2025), ("brut_marj", 2025), ("net_marj", 2024),
             ("varlik_karl", 2023), ("ozk_karl", 2024), ("kaldirac", 2025), ("ozk_oran", 2024)]:
    F.olcu(nop, S_NOP, m, y, 1, R)
for m, y in [("cari", 2023), ("likidite", 2023), ("nis", 2025), ("stok_sure", 2024), ("alacak_hiz", 2025),
             ("borc_sure", 2025), ("aktif_hiz", 2025), ("faal_marj", 2024), ("net_marj", 2025),
             ("varlik_karl", 2025), ("ds_oran", 2023), ("borc_ozk", 2025)]:
    F.olcu(rst, S_RST, m, y, 3, R)

# ------------------------------------------------------------------ üretim işletmesinde stok türleri
tuv = ("| Kalem | 2024 | 2025 |\n|---|---|---|\n"
       "| Dönem sonu DİMM stoku | 60.000 | 40.000 |\n| DİMM giderleri | 560.000 | 600.000 |\n"
       "| Direkt işçilik giderleri | 470.000 | 500.000 |\n| Genel üretim giderleri | 700.000 | 740.000 |\n"
       "| Üretim giderleri toplamı | 1.730.000 | 1.840.000 |\n| Dönem başı yarı mamul | 80.000 | 90.000 |\n"
       "| Dönem sonu yarı mamul | 90.000 | 110.000 |\n| Dönemin üretim maliyeti | 1.720.000 | 1.820.000 |\n"
       "| Dönem başı mamul | 120.000 | 140.000 |\n| Dönem sonu mamul | 140.000 | 160.000 |\n"
       "| Satılan mamul maliyeti | 1.700.000 | 1.800.000 |\n| Dönem başı ticari mal | 40.000 | 50.000 |\n"
       "| Dönem sonu ticari mal | 50.000 | 70.000 |\n| Satılan ticari mal maliyeti | 1.300.000 | 1.440.000 |")
assert 1_840_000 + 90_000 - 110_000 == 1_820_000 and 1_820_000 + 140_000 - 160_000 == 1_800_000
S_TUV = F.uyaran({"id": "yet-fta-oran-tuv", "title": "TUV Üretim A.Ş. — Maliyet Verileri", "kind": "table",
                  "bodyMarkdown": tuv,
                  "caption": "TUV Üretim A.Ş.’ye ait soruları bu tabloya göre cevaplayınız. Devir hızı ve sürelerinde "
                             "ortalama stok tutarlarını kullanınız ve bir yılı 360 gün kabul ediniz."})
R2 = "Stok türlerine göre devir hızı"
F.hesap(R2, "TUV Üretim A.Ş.’nin maliyet verilerine göre 2025 yılı ortalama DİMM stok devir süresi kaç gündür?",
        Hesap(360 / (600_000 / 50_000), "gun", [360 * 40_000 / 600_000, 365 / 12, 360 * 50_000 / 1_820_000,
                                                360 * 60_000 / 600_000],
              "TUV Üretim A.Ş. DİMM devir hızı = DİMM giderleri ÷ ortalama DİMM stoku = 600.000 ÷ [(60.000 + 40.000) ÷ 2] "
              "= 12; süre = 360 ÷ 12 = 30,00 gün."), stimulus_id=S_TUV)
F.hesap(R2, "TUV Üretim A.Ş.’nin 2025 yılı yarı mamul stoklarının ortalama devir süresi kaç gün olarak hesaplanır?",
        Hesap(360 * 100_000 / 1_820_000, "gun", [360 * 110_000 / 1_820_000, 360 * 100_000 / 1_800_000,
                                                 360 * 100_000 / 1_840_000, 365 * 100_000 / 1_820_000],
              "TUV Üretim A.Ş. yarı mamul devir hızı = dönemin üretim maliyeti ÷ ortalama yarı mamul = 1.820.000 ÷ "
              "[(90.000 + 110.000) ÷ 2] = 18,20; süre = 360 ÷ 18,20 = 19,78 gün."), stimulus_id=S_TUV)
F.hesap(R2, "Verilen maliyet tablosuna göre TUV Üretim A.Ş.’nin 2025 yılı mamul stok devir hızı kaçtır?",
        Hesap(1_800_000 / 150_000, "kat", [1_800_000 / 160_000, 1_820_000 / 150_000, 1_800_000 / 140_000,
                                           1_440_000 / 150_000],
              "TUV Üretim A.Ş. mamul stok devir hızı = satılan mamul maliyeti ÷ ortalama mamul stoku = 1.800.000 ÷ "
              "[(140.000 + 160.000) ÷ 2] = 12,00."), stimulus_id=S_TUV)
F.hesap(R2, "TUV Üretim A.Ş.’nin 2025 yılında ticari mal stoklarının ortalama devir süresi kaç gün olur?",
        Hesap(360 * 60_000 / 1_440_000, "gun", [360 * 70_000 / 1_440_000, 365 * 60_000 / 1_440_000,
                                                360 * 50_000 / 1_440_000, 1_440_000 / 60_000],
              "TUV Üretim A.Ş. ticari mal devir hızı = satılan ticari mal maliyeti ÷ ortalama ticari mal = 1.440.000 ÷ "
              "[(50.000 + 70.000) ÷ 2] = 24; süre = 360 ÷ 24 = 15,00 gün."), stimulus_id=S_TUV)

# ------------------------------------------------------------------ hedef değerden geriye hesap
KURAL = "(Devir hızlarında ortalama değeri kullanınız ve bir yılı 360 gün kabul ediniz.)"
ort = 720_000 * 60 / 360
F.hesap(R,
    "Bir firmanın 2025 yılı sonunda ticari alacakları 100.000 ₺’dir. 2026 yılında net satışların 720.000 ₺ olacağı "
    "öngörülmekte ve ortalama tahsil süresinin 60 gün olması hedeflenmektedir.\n\nBu hedefe ulaşmak için 2026 yılı "
    f"sonunda ticari alacak tutarı kaç ₺ olmalıdır?\n{KURAL}",
    Hesap(2 * ort - 100_000, "tutar", [ort, 2 * ort, 100_000, ort - 100_000 + 60_000, 2 * 720_000 * 60 / 365 - 100_000],
          f"Ortalama alacak = 720.000 × 60 ÷ 360 = {tl(ort)} ₺. Ortalama = (100.000 + X) ÷ 2 olduğundan X = 2 × "
          f"{tl(ort)} − 100.000 = {tl(2 * ort - 100_000)} ₺."), zorluk="hard")

F.hesap(R,
    "Bir firmanın izleyen dönem sonunda dönen varlıklarının 240.000 ₺, kısa vadeli yabancı kaynaklarının 160.000 ₺ "
    "olması ve likidite (asit-test) oranının 0,9 olması hedeflenmektedir.\n\nLikidite oranı hedefine ulaşmak için "
    "dönem sonu stok tutarı kaç ₺ olmalıdır?",
    Hesap(240_000 - 0.9 * 160_000, "tutar", [0.9 * 160_000, 160_000, 240_000 - 0.9 * 240_000, 240_000 / 1.5],
          "Likidite oranı = (dönen varlıklar − stoklar) ÷ KVYK; 0,9 = (240.000 − S) ÷ 160.000 olduğundan 240.000 − S = "
          "144.000 ve S = 96.000 ₺."))

F.hesap(R,
    "Bir işletmenin mali analizinde pasif toplamına göre hesaplanan devamlı sermaye oranı %70, uzun vadeli yabancı "
    "kaynak oranı %25 olarak bulunmuştur. Kaldıraç oranı toplam yabancı kaynakların pasif toplamına bölünmesiyle "
    "hesaplanmaktadır.\n\nBu verilere göre işletmenin kaldıraç oranı yüzde (%) kaçtır?",
    Hesap(100 - (70 - 25), "yuzde", [30, 45, 95, 75],
          "Devamlı sermaye = UVYK + öz kaynaklar = %70; öz kaynaklar = %70 − %25 = %45. Kaldıraç = 1 − öz kaynak oranı = "
          "%100 − %45 = %55 (KVYK %30 + UVYK %25)."), zorluk="hard")

ort_tb = 1_080_000 * 45 / 360
F.hesap(R,
    "Bir ticari firmanın 2025 yılı sonunda ticari borçları 150.000 ₺’dir. 2026 yılında satışların maliyetinin "
    "1.080.000 ₺ olacağı tahmin edilmekte ve ortalama ticari borç ödeme süresinin 45 gün olması istenmektedir.\n\n"
    f"Bu hedef için 2026 yılı sonunda ticari borç tutarı kaç ₺ olmalıdır?\n{KURAL}",
    Hesap(2 * ort_tb - 150_000, "tutar", [ort_tb, 2 * ort_tb, 150_000, ort_tb - 30_000 + 150_000 - 135_000],
          f"Ortalama ticari borç = 1.080.000 × 45 ÷ 360 = {tl(ort_tb)} ₺. (150.000 + X) ÷ 2 = {tl(ort_tb)} olduğundan "
          f"X = {tl(2 * ort_tb - 150_000)} ₺."))

ort_st = 1_440_000 * 40 / 360
F.hesap(R,
    "Bir firmanın dönem başı stoku 200.000 ₺’dir. Dönem içinde satışların maliyetinin 1.440.000 ₺ olacağı "
    "öngörülmekte ve ortalama stok devir süresinin 40 güne indirilmesi hedeflenmektedir.\n\nBu hedefe ulaşmak için "
    f"dönem sonu stok tutarı kaç ₺ olmalıdır?\n{KURAL}",
    Hesap(2 * ort_st - 200_000, "tutar", [ort_st, 200_000, 2 * ort_st, 1_440_000 * 40 / 365],
          f"Ortalama stok = 1.440.000 × 40 ÷ 360 = {tl(ort_st)} ₺. (200.000 + X) ÷ 2 = {tl(ort_st)} olduğundan X = "
          f"{tl(2 * ort_st - 200_000)} ₺."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin net kâr marjı %8, aktif devir hızı 1,5 ve aktif toplamının öz kaynaklara oranı (öz kaynak "
    "çarpanı) 2’dir. Oranlar dönem sonu değerlerle hesaplanmıştır.\n\nDu Pont yaklaşımına göre işletmenin öz kaynak "
    "kârlılığı yüzde (%) kaçtır?",
    Hesap(8 * 1.5 * 2, "yuzde", [8 * 1.5, 8 * 2, 8 + 1.5 + 2, 8 / 1.5 * 2],
          "Varlık kârlılığı = net kâr marjı × aktif devir hızı = %8 × 1,5 = %12. Öz kaynak kârlılığı = varlık kârlılığı × "
          "öz kaynak çarpanı = %12 × 2 = %24."))

F.hesap(R,
    "Bir firmanın dönem sonu dönen varlıklarının 450.000 ₺ olması beklenmektedir. Kredi sözleşmesi gereği cari "
    "oranın 1,8’in altına düşmemesi gerekmektedir.\n\nFirmanın dönem sonunda taşıyabileceği en yüksek kısa vadeli "
    "yabancı kaynak tutarı kaç ₺’dir?",
    Hesap(450_000 / 1.8, "tutar", [450_000 * 1.8, 450_000 - 250_000, 450_000 / 1.5, 450_000 * 0.8],
          "Cari oran = dönen varlıklar ÷ KVYK ≥ 1,8 olmalıdır; KVYK ≤ 450.000 ÷ 1,8 = 250.000 ₺."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin ortalama stok devir süresi 45 gün, ortalama ticari alacak tahsil süresi 60 gün ve ortalama ticari "
    "borç ödeme süresi 40 gündür. Hesaplamalarda 360 günlük yıl ve ortalama değerler kullanılmıştır.\n\n"
    "İşletmenin nakit dönüşüm süresi kaç gündür?",
    Hesap(45 + 60 - 40, "gun", [45 + 60, 45 + 60 + 40, 60 - 40 + 5 - 20, 60 + 40 - 45 + 30],
          "Faaliyet döngüsü = stok süresi + tahsil süresi = 45 + 60 = 105 gün. Nakit dönüşüm süresi = faaliyet döngüsü − "
          "borç ödeme süresi = 105 − 40 = 65 gün."))

F.hesap(R,
    "Bir işletmenin yabancı kaynaklarının öz kaynaklarına oranı 1,5’tir. Bilançoda başka kaynak kalemi yoktur ve "
    "oranlar dönem sonu değerlerle hesaplanmıştır.\n\nİşletmenin öz kaynaklarının aktif toplamına oranı yüzde "
    "kaçtır?",
    Hesap(100 / 2.5, "yuzde", [60, 100 / 1.5, 150, 25],
          "Yabancı kaynak = 1,5 × öz kaynak olduğundan pasif = 2,5 × öz kaynak. Öz kaynak oranı = 1 ÷ 2,5 = %40; "
          "kaldıraç oranı %60’tır."))

F.hesap(R,
    "Bir firmanın 2025 yılında net satışları 900.000 ₺, satışların maliyeti 630.000 ₺ olmuştur. Dönem başı ticari "
    "alacaklar 120.000 ₺, dönem sonu ticari alacaklar 180.000 ₺’dir.\n\nFirmanın 2025 yılı ortalama ticari alacak "
    f"tahsil süresi kaç gündür?\n{KURAL}",
    Hesap(360 * 150_000 / 900_000, "gun", [360 * 180_000 / 900_000, 360 * 150_000 / 630_000, 365 * 150_000 / 900_000,
                                            360 * 120_000 / 900_000],
          "Ortalama alacak = (120.000 + 180.000) ÷ 2 = 150.000 ₺; devir hızı = 900.000 ÷ 150.000 = 6; tahsil süresi = "
          "360 ÷ 6 = 60,00 gün. Satışların maliyeti alacak devrinde kullanılmaz."), zorluk="easy")

# ------------------------------------------------------------------ yorum ve işlem etkisi
F.q(R,
    "Cari oranı 1,6 olan bir işletme, kısa vadeli banka kredisinin 50.000 ₺’lik kısmını kasasındaki nakitle "
    "ödemiştir. İşlemden önce net işletme sermayesi pozitiftir.\n\nBu işlemin cari oran ve net işletme sermayesine "
    "etkisi aşağıdakilerden hangisidir?",
    "Cari oran artar, net işletme sermayesi değişmez.",
    ["Cari oran azalır, net işletme sermayesi değişmez.",
     "Cari oran ve net işletme sermayesi birlikte artar.",
     "Cari oran değişmez, net işletme sermayesi azalır.",
     "Cari oran artar, net işletme sermayesi azalır."],
    "Dönen varlıklar ve KVYK aynı tutarda azalır; fark (net işletme sermayesi) değişmez. Oran 1’den büyükken pay ve "
    "paydanın eşit azalması oranı yükseltir: örneğin 160/100 = 1,6 iken 110/50 = 2,2 olur.", zorluk="hard")

F.q(R,
    "Bir işletme 80.000 ₺ tutarındaki ticari malı peşin olarak satın almış ve ödemeyi banka hesabından yapmıştır. "
    "İşlemden önce cari oran 1,4, likidite oranı 0,9’dur.\n\nBu işlemin cari oran ve likidite oranına etkisi "
    "aşağıdakilerden hangisidir?",
    "Cari oran değişmez, likidite oranı azalır.",
    ["Cari oran artar, likidite oranı değişmez.",
     "Cari oran ve likidite oranı birlikte azalır.",
     "Cari oran azalır, likidite oranı artar.",
     "Cari oran ve likidite oranı değişmez."],
    "Hazır değerler azalıp stoklar aynı tutarda arttığından dönen varlık toplamı ve cari oran değişmez. Likidite "
    "oranı stokları dışarıda bıraktığından pay azalır ve oran düşer.")

F.q(R,
    "Bir toptancının ortalama ticari alacak tahsil süresi 75 gün, ortalama ticari borç ödeme süresi 30 gündür. Stok "
    "devir süresi ise 40 gün olarak hesaplanmıştır.\n\nBu verilere ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Satıcılara ödeme müşteri tahsilatından önce yapıldığından işletme sermayesi finansmanı gerekir.",
    ["Müşterilerden tahsilat satıcılara ödemeden önce yapıldığından nakit fazlası oluşur.",
     "Tahsil süresi borç süresinden uzun olduğundan faaliyet döngüsü kısalır.",
     "Stok devir süresi tahsil süresinden kısa olduğundan likidite sorunu doğmaz.",
     "Nakit dönüşüm süresi sıfırın altında olduğundan kısa vadeli borçlanma gerekmez."],
    "Faaliyet döngüsü 40 + 75 = 115 gün, nakit dönüşüm süresi 115 − 30 = 85 gündür. İşletme satıcıya 30. günde öder "
    "ama müşteriden ortalama 75 günde tahsil eder; aradaki süre için işletme sermayesi finansmanı gerekir.")

F.q(R,
    "Bir işletmenin ortalama stok devir süresi üç yıl içinde 36 günden 58 güne çıkmıştır. Aynı dönemde satışların "
    "maliyeti yaklaşık aynı kalmıştır.\n\nBu gelişmeye ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Stoklar yavaş eritilmekte, stoklara bağlanan fon artmaktadır.",
    ["Stoklar daha hızlı satılmakta, stok maliyeti azalmaktadır.",
     "Stok devir hızı artmakta, likidite güçlenmektedir.",
     "Satışların maliyeti arttığı için süre uzamış, stok düzeyi aynı kalmıştır.",
     "Stok süresi uzadıkça nakit dönüşüm süresi kısalmaktadır."],
    "Satışların maliyeti değişmezken devir süresinin uzaması ortalama stokun büyüdüğünü, yani stokların daha yavaş "
    "eritildiğini gösterir. Stoklara bağlanan fon artar, nakit dönüşüm süresi uzar.")

F.q(R,
    "Bir finansal analiz eğitiminde katılımcılara likidite oranlarıyla ilgili ifadeler dağıtılmış, hatalı olanı "
    "bulmaları istenmiştir.\n\nLikidite oranlarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Asit-test oranı, stoklar dâhil tüm dönen varlıkların KVYK’ye bölünmesiyle bulunur.",
    ["Cari oran, dönen varlıkların KVYK’ye bölünmesiyle bulunur.",
     "Nakit oranı, hazır değerler ve menkul kıymetlerin KVYK’ye oranıdır.",
     "Net işletme sermayesi, dönen varlıklardan KVYK’nin düşülmesiyle bulunur.",
     "Stoklar paraya çevrilmesi en uzun süren dönen varlık kalemidir."],
    "Asit-test (likidite) oranında paraya çevrilmesi en uzun süren stoklar dönen varlıklardan çıkarılır. Stoklar "
    "dâhil hesaplanan oran cari orandır.")

F.q(R,
    "Bir işletmenin kaldıraç oranı %82, öz kaynakların aktif toplamına oranı %18’dir. Sektör ortalaması kaldıraç "
    "oranında %55 düzeyindedir.\n\nBu verilere ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Varlıkların büyük kısmı yabancı kaynakla finanse edildiğinden finansal risk yüksektir.",
    ["Varlıkların büyük kısmı öz kaynakla finanse edildiğinden finansal risk düşüktür.",
     "Kaldıraç oranı yüksek olduğundan işletme borçlarını ödeme gücü güçlüdür.",
     "Öz kaynak oranı sektörün üzerinde olduğundan yeni borçlanma kolaydır.",
     "Kaldıraç oranının yüksekliği likiditeyi etkiler, finansal riski etkilemez."],
    "Kaldıraç oranı toplam yabancı kaynakların pasife oranıdır; %82 düzeyi sektörün (%55) çok üzerindedir. "
    "Varlıkların büyük kısmı borçla finanse edildiğinden faiz yükü ve finansal risk yüksektir.")

if __name__ == "__main__":
    sys.exit(F.yaz())
