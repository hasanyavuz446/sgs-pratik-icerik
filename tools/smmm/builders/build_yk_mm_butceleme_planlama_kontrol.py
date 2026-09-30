# -*- coding: utf-8 -*-
"""Yönetim Muhasebesi · Bütçeleme, Planlama ve Kontrol — 60 soru, 2026 test biçimi.

Ana bütçe ve hazırlanma sırası; satış, üretim, DİMM, DİŞ, GÜG ve satılan mamul maliyeti bütçeleri; nakit
bütçesi (tahsilat, ödeme, finansman ihtiyacı); esnek bütçe ve performans raporu; satış fiyat/hacim sapmaları;
sorumluluk merkezleri, yatırım getirisi, artık gelir ve transfer fiyatı; bütçe türleri ve davranışsal konular
gerçek kitapçıklardaki gibi tutar veren olaylarla sorulur.

Dayanak: bütçeleme ve sorumluluk muhasebesinin genel kabul görmüş esasları. Vergi ve asgari getiri oranları
yıla bağlı olmasın diye kökte verilir. Tutarlar builder içinde hesaplanır; stok ve nakit denklikleri denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_butceleme_planlama_kontrol_2026.json", lesson="yonetim_muhasebesi",
          topic="butceleme_planlama_kontrol", konu_adi="Bütçeleme, Planlama ve Kontrol", seed=2026093089,
          surum="Bütçeleme ve sorumluluk muhasebesi esasları; 30.09.2026 kontrolü")

FB = "Faaliyet bütçeleri"
NB = "Nakit bütçesi"
EB = "Esnek bütçe ve sapmalar"
SM = "Sorumluluk muhasebesi ve performans ölçümü"
BT = "Bütçe türleri ve bütçe süreci"


def birim(x, b="birim"):
    return f"{tl(x)} {b}"


# ------------------------------------------------------------------ faaliyet bütçeleri
sb = 1_200 * 250 + 800 * 400
P.sayisal(FB,
    "Bir işletme gelecek çeyrekte A ürününden 1.200 birimi 250 ₺’den, B ürününden 800 birimi 400 ₺’den satmayı "
    "öngörmektedir. Satışların %30’unun vadeli yapılacağı ve A ürününün dönem başında 150 birim stokunun "
    "bulunduğu bilinmektedir.\n\nİşletmenin çeyreklik satış bütçesi kaç ₺’dir?",
    tl(sb), secenekler(sb, 300_000, 434_000, 1_300_000, 582_500),
    "Satış bütçesi = bütçelenen miktar × bütçelenen fiyat: 1.200 × 250 + 800 × 400 = 300.000 + 320.000 = 620.000 ₺. "
    "Vade yapısı nakit bütçesini, stok durumu üretim bütçesini etkiler; satış bütçesini değiştirmez.", zorluk="easy")

sb = 2_000 * 150 + 2_400 * 150 * 1.10
P.sayisal(FB,
    "Bir işletme ilk çeyrekte 2.000 birim ürünü birim 150 ₺’den satmayı planlamaktadır. İkinci çeyrekte satış "
    "fiyatının %10 artırılması ve satış miktarının 2.400 birime çıkması beklenmektedir.\n\nİlk iki çeyreğin toplam "
    "satış bütçesi kaç ₺’dir?",
    tl(sb), secenekler(sb, 660_000, 726_000, 360_000, 690_000),
    "Birinci çeyrek: 2.000 × 150 = 300.000 ₺. İkinci çeyrek: 2.400 × 165 = 396.000 ₺. Toplam 696.000 ₺. Fiyat "
    "artışı yok sayılırsa 660.000 ₺ bulunur.")

ub = 10_000 + 1_800 - 1_200
P.sayisal(FB,
    "Bir işletmenin gelecek yıl satış bütçesi 10.000 birimdir. Dönem başında 1.200 birim mamul stoku bulunmakta, "
    "yönetim dönem sonunda 1.800 birim mamul stoku bulundurmak istemektedir. Yarı mamul stoku yoktur.\n\nÜretim "
    "bütçesi kaç birimdir?",
    birim(ub), [birim(x) for x in (9_400, 13_000, 11_800, 10_000)],
    "Üretim = satış + hedef dönem sonu stok − dönem başı stok = 10.000 + 1.800 − 1.200 = 10.600 birim.",
    zorluk="easy")

son = 0.20 * 9_000
ub = 8_000 + son - 1_500
P.sayisal(FB,
    "Bir işletme her ay sonunda, izleyen ayın satışlarının %20’si kadar mamul stoku bulundurmaktadır. Ocak satışları "
    "8.000 birim, şubat satışları 9.000 birim olarak bütçelenmiş; ocak başında 1.500 birim mamul stoku "
    "bulunmaktadır.\n\nOcak ayı üretim bütçesi kaç birimdir?",
    birim(ub), [birim(x) for x in (8_100, 9_500, 6_500, 8_000)],
    "Ocak sonu hedef stok = 9.000 × %20 = 1.800 birim. Üretim = 8.000 + 1.800 − 1.500 = 8.300 birim. Hedef stokun "
    "ocak satışına göre hesaplanması (1.600) 8.100 birim sonucunu verir.")

kg = 5_000 * 3 + 2_000 - 1_500
tut = kg * 40
P.sayisal(FB,
    "Bir işletmenin bütçelenen üretimi 5.000 birimdir ve her birim için 3 kg hammadde kullanılmaktadır. Dönem başında "
    "1.500 kg hammadde stoku vardır; dönem sonunda 2.000 kg stok bulundurulması istenmektedir. Hammaddenin "
    "bütçelenen alış fiyatı kilogram başına 40 ₺’dir.\n\nHammadde satın alma bütçesi kaç ₺’dir?",
    tl(tut), secenekler(tut, 600_000, 580_000, 680_000, 540_000),
    "Kullanım = 5.000 × 3 = 15.000 kg. Satın alma = 15.000 + 2.000 − 1.500 = 15.500 kg; tutar = 15.500 × 40 = "
    "620.000 ₺.")

dis = 6_000 * 0.4 * 180
P.sayisal(FB,
    "Bir işletme gelecek çeyrekte 6.000 birim üretim planlamaktadır. Her birim için standart olarak 0,4 direkt "
    "işçilik saati gerekmekte ve saat ücreti 180 ₺ olarak bütçelenmektedir. Satış bütçesi 5.600 birimdir.\n\n"
    "Direkt işçilik bütçesi kaç ₺’dir?",
    tl(dis), secenekler(dis, 403_200, 1_080_000, 450_000, 2_400),
    "Direkt işçilik bütçesi üretim bütçesine dayanır: 6.000 × 0,4 = 2.400 saat × 180 = 432.000 ₺. Satış miktarıyla "
    "hesaplamak (5.600 birim) 403.200 ₺ verir.", zorluk="easy")

gug = 12 * 2_400 + 180_000
nakit = gug - 40_000
P.sayisal(FB,
    "Bir işletmenin GÜG bütçesinde değişken GÜG oranı direkt işçilik saati başına 12 ₺, dönemlik sabit GÜG ise "
    "180.000 ₺’dir. Sabit GÜG’ün 40.000 ₺’si makine amortismanıdır. Dönemde 2.400 direkt işçilik saati "
    "bütçelenmiştir.\n\nGÜG bütçesinin nakit ödeme gerektiren kısmı kaç ₺’dir?",
    tl(nakit), secenekler(nakit, gug, 140_000, 28_800, 248_800),
    "Toplam GÜG bütçesi = 12 × 2.400 + 180.000 = 208.800 ₺. Amortisman nakit çıkışı gerektirmediğinden nakit "
    "bütçesine aktarılacak tutar 208.800 − 40.000 = 168.800 ₺’dir.")

smm = 120_000 + 1_450_000 - 170_000
P.sayisal(FB,
    "Bir işletmenin bütçe verileri şöyledir: dönem başı mamul stoku 120.000 ₺, bütçelenen üretim maliyeti "
    "1.450.000 ₺ ve hedef dönem sonu mamul stoku 170.000 ₺. Dönem başı ve sonu yarı mamul stoku yoktur; bütçelenen "
    "satışlar 2.100.000 ₺’dir.\n\nSatılan mamul maliyeti bütçesi kaç ₺’dir?",
    tl(smm), secenekler(smm, 1_450_000, 1_500_000, 1_740_000, 700_000),
    "SMM = dönem başı mamul + üretim maliyeti − dönem sonu mamul = 120.000 + 1.450.000 − 170.000 = 1.400.000 ₺. "
    "Bütçelenen brüt kâr 2.100.000 − 1.400.000 = 700.000 ₺’dir.")

P.sayisal(FB,
    "Bir satış bütçesinde bir ürün için 480.000 ₺ satış hasılatı ve 1.600 birim satış miktarı öngörülmüştür. "
    "Pazarlama müdürü, bütçe hazırlanırken kullanılan birim fiyatı fiyat listesinde kontrol etmek istemektedir.\n\n"
    "Bütçelenen birim satış fiyatı kaç ₺’dir?",
    tl(480_000 / 1_600), secenekler(300, 320, 250, 360, 280),
    "Birim fiyat = satış bütçesi ÷ satış miktarı = 480.000 ÷ 1.600 = 300 ₺.", zorluk="easy")

son = 12_400 + 900 - 12_000
P.sayisal(FB,
    "Bir işletmenin üretim bütçesi 12.400 birim, satış bütçesi 12.000 birimdir. Dönem başında 900 birim mamul "
    "stoku bulunmaktadır. Yönetim, bütçede öngörülen dönem sonu stokunun depo kapasitesini aşıp aşmadığını kontrol "
    "etmektedir.\n\nBütçelenen dönem sonu mamul stoku kaç birimdir?",
    birim(son), [birim(x) for x in (500, 400, 900, 2_100)],
    "Dönem sonu stok = dönem başı stok + üretim − satış = 900 + 12.400 − 12.000 = 1.300 birim.")

kull = 18_200 + 1_000 - 2_200
uretim = kull / 2
P.sayisal(FB,
    "Bir işletme dönem için 18.200 kg hammadde satın almayı bütçelemiştir. Dönem başı hammadde stoku 1.000 kg, "
    "hedef dönem sonu stoku 2.200 kg’dır. Her birim mamul için 2 kg hammadde kullanılmaktadır.\n\nBütçelenen "
    "üretim miktarı kaç birimdir?",
    birim(uretim), [birim(x) for x in (9_100, 9_700, 8_000, 17_000)],
    "Kullanılacak hammadde = 18.200 + 1.000 − 2.200 = 17.000 kg. Üretim = 17.000 ÷ 2 = 8.500 birim.",
    zorluk="hard")

P.sayisal(FB,
    "Bir işletmenin 4.000 birimlik üretim için hazırladığı direkt işçilik bütçesi 504.000 ₺’dir. Bütçelenen saat "
    "ücreti 210 ₺’dir. Üretim planlama birimi, bütçede kullanılan birim başına işçilik süresini doğrulamak "
    "istemektedir.\n\nBirim başına bütçelenen direkt işçilik süresi kaç saattir?",
    "0,6", ["0,5", "1,2", "0,8", "2,4"],
    "Toplam saat = 504.000 ÷ 210 = 2.400 saat; birim başına süre = 2.400 ÷ 4.000 = 0,6 saat.")

kg = 6_000 + 0.25 * 7_000 - 1_500
P.sayisal(FB,
    "Bir işletme her ay sonunda, izleyen ayın hammadde ihtiyacının %25’i kadar stok bulundurmaktadır. Nisan ayı "
    "üretimi için 6.000 kg, mayıs ayı üretimi için 7.000 kg hammadde gerekmektedir. Nisan başında 1.500 kg "
    "hammadde stoku vardır.\n\nNisan ayında satın alınması gereken hammadde kaç kg’dır?",
    birim(kg, "kg"), [birim(x, "kg") for x in (6_000, 5_750, 7_750, 4_500)],
    "Nisan sonu hedef stok = 7.000 × %25 = 1.750 kg. Satın alma = 6.000 + 1.750 − 1.500 = 6.250 kg.")

dimm = 7_500 * 2.4 * 15
P.sayisal(FB,
    "Bir işletmenin üretim bütçesi 7.500 birimdir. Her birim için 2,4 kg hammadde kullanılmakta ve hammaddenin "
    "bütçelenen fiyatı kilogram başına 15 ₺’dir. Dönem başı hammadde stoku 1.200 kg, hedef dönem sonu stoku 1.800 "
    "kg’dır.\n\nDirekt ilk madde ve malzeme kullanım bütçesi kaç ₺’dir?",
    tl(dimm), secenekler(dimm, 279_000, 261_000, 112_500, 36_000),
    "Kullanım bütçesi üretimde tüketilecek miktara dayanır: 7.500 × 2,4 = 18.000 kg × 15 = 270.000 ₺. Stok "
    "değişimi satın alma bütçesini etkiler: satın alma 18.600 kg × 15 = 279.000 ₺ olur.")

# ------------------------------------------------------------------ nakit bütçesi
th = 0.40 * 500_000 + 0.50 * 400_000 + 0.10 * 300_000
P.sayisal(NB,
    "Bir işletmenin satışlarının %40’ı peşin tahsil edilmekte, %50’si izleyen ay, %10’u ise iki ay sonra tahsil "
    "edilmektedir; tahsil edilemeyen alacak beklenmemektedir. Ocak satışları 300.000 ₺, şubat 400.000 ₺ ve mart "
    "500.000 ₺ olarak bütçelenmiştir.\n\nMart ayında bütçelenen nakit tahsilatı kaç ₺’dir?",
    tl(th), secenekler(th, 500_000, 400_000, 460_000, 380_000),
    "Mart tahsilatı = mart satışlarının %40’ı (200.000) + şubatın %50’si (200.000) + ocağın %10’u (30.000) = "
    "430.000 ₺.")

od = 0.70 * 400_000 + 0.30 * 350_000
P.sayisal(NB,
    "Bir işletme hammadde alımlarının %70’ini alım ayında, %30’unu izleyen ayda ödemektedir. Şubat alımları 350.000 "
    "₺, mart alımları 400.000 ₺ olarak bütçelenmiştir. Mart ayında ayrıca 60.000 ₺ amortisman gideri "
    "bulunmaktadır.\n\nMart ayında hammadde alımları için bütçelenen nakit ödeme kaç ₺’dir?",
    tl(od), secenekler(od, 400_000, 445_000, 365_000, 280_000),
    "Mart ödemesi = mart alımlarının %70’i (280.000) + şubat alımlarının %30’u (105.000) = 385.000 ₺. Amortisman "
    "nakit çıkışı olmadığından ödemeye eklenmez.")

acik = 100_000 + 500_000 - 650_000
fin = 80_000 - acik
P.sayisal(NB,
    "Bir işletmenin nakit bütçesinde ay başı nakit 100.000 ₺, bütçelenen nakit girişleri 500.000 ₺ ve nakit "
    "çıkışları 650.000 ₺’dir. İşletme politikası gereği ay sonunda en az 80.000 ₺ nakit bulundurulmalıdır; açık "
    "banka kredisiyle kapatılacaktır.\n\nAy içinde sağlanması gereken finansman kaç ₺’dir?",
    tl(fin), secenekler(fin, 50_000, 80_000, 30_000, 150_000),
    "Finansman öncesi nakit = 100.000 + 500.000 − 650.000 = −50.000 ₺. Asgari 80.000 ₺’ye ulaşmak için 50.000 + "
    "80.000 = 130.000 ₺ finansman gerekir.")

P.q(NB,
    "Bir işletmenin mali işler müdürü aylık nakit bütçesini hazırlarken gelir tablosu bütçesindeki kalemleri tek tek "
    "incelemektedir. Bazı kalemler nakit hareketi doğurmakta, bazıları doğurmamaktadır.\n\nAşağıdakilerden hangisi "
    "nakit bütçesinde yer almaz?",
    "Makinelerin dönem amortismanı",
    ["Peşin satışlardan tahsilat", "Satıcılara yapılan borç ödemesi", "Banka kredisinin anapara geri ödemesi",
     "Peşin ödenen yıllık kira"],
    "Nakit bütçesi yalnız nakit giriş ve çıkışlarını içerir. Amortisman gider olmakla birlikte nakit çıkışı "
    "doğurmadığından nakit bütçesinde yer almaz; kredi anapara ödemesi ise gider olmasa da nakit çıkışıdır.",
    zorluk="easy")

onceki = (410_000 - 0.60 * 600_000) / 0.25
P.sayisal(NB,
    "Bir işletmede bu ayın satışlarının %60’ı ay içinde, önceki ay sonundaki alacakların ise %25’i bu ay tahsil "
    "edilmiştir. Bu ayın satışları 600.000 ₺ ve toplam tahsilat 410.000 ₺’dir.\n\nÖnceki ay sonundaki alacak "
    "tutarı kaç ₺’dir?",
    tl(onceki), secenekler(onceki, 50_000, 240_000, 125_000, 164_000),
    "Bu ayın satışlarından tahsilat = 600.000 × %60 = 360.000 ₺. Önceki alacaktan tahsilat = 410.000 − 360.000 = "
    "50.000 ₺; bu tutar önceki alacağın %25’i olduğundan alacak 50.000 ÷ 0,25 = 200.000 ₺’dir.", zorluk="hard")

cikis = 120_000 + 560_000 + 90_000 - 100_000
P.sayisal(NB,
    "Bir işletmenin nakit bütçesinde dönem başı nakit 120.000 ₺, nakit girişleri 560.000 ₺ ve sağlanan banka "
    "kredisi 90.000 ₺’dir. Dönem sonunda 100.000 ₺ nakit kalması öngörülmektedir.\n\nBütçelenen dönem içi nakit "
    "çıkışları kaç ₺’dir?",
    tl(cikis), secenekler(cikis, 580_000, 780_000, 760_000, 490_000),
    "Dönem sonu nakit = başı + girişler + finansman − çıkışlar: 100.000 = 120.000 + 560.000 + 90.000 − X; X = "
    "670.000 ₺.")

th = 0.50 * 300_000 + 0.48 * 250_000
P.sayisal(NB,
    "Bir işletmenin satışlarının %50’si peşin tahsil edilmekte, %48’i izleyen ay tahsil edilmekte ve %2’si "
    "tahsil edilemeyen alacak olarak kalmaktadır. Mart satışları 250.000 ₺, nisan satışları 300.000 ₺ olarak "
    "bütçelenmiştir.\n\nNisan ayında bütçelenen nakit tahsilatı kaç ₺’dir?",
    tl(th), secenekler(th, 275_000, 300_000, 294_000, 150_000),
    "Nisan tahsilatı = nisan satışlarının %50’si (150.000) + mart satışlarının %48’i (120.000) = 270.000 ₺. Tahsil "
    "edilemeyen %2 nakit girişi yaratmaz.")

net = (2_000_000 - 1_200_000 - 450_000 - 50_000) * 0.75
P.sayisal(NB,
    "Bir işletmenin bütçelenmiş gelir tablosu verileri şöyledir: net satışlar 2.000.000 ₺, satılan mamul maliyeti "
    "1.200.000 ₺, faaliyet giderleri 450.000 ₺ ve finansman gideri 50.000 ₺. Kurumlar vergisi oranının %25 olduğu "
    "varsayılmaktadır.\n\nBütçelenen dönem net kârı kaç ₺’dir?",
    tl(net), secenekler(net, 300_000, 262_500, 350_000, 600_000),
    "Vergi öncesi kâr = 2.000.000 − 1.200.000 − 450.000 − 50.000 = 300.000 ₺. Net kâr = 300.000 × (1 − 0,25) = "
    "225.000 ₺.", zorluk="easy")

# ------------------------------------------------------------------ esnek bütçe ve sapmalar
esnek = 150_000 + 35 * 8_000
P.sayisal(EB,
    "Bir işletme GÜG bütçesini 10.000 birim üretime göre 500.000 ₺ olarak hazırlamıştır; değişken GÜG birim başına "
    "35 ₺, sabit GÜG 150.000 ₺’dir. Ay içinde fiilen 8.000 birim üretilmiştir.\n\nFiili üretim düzeyine göre esnek "
    "bütçe tutarı kaç ₺’dir?",
    tl(esnek), secenekler(esnek, 500_000, 400_000, 280_000, 150_000 + 35 * 10_000 * 0.8 + 30_000),
    "Esnek bütçe = sabit GÜG + birim değişken GÜG × fiili hacim = 150.000 + 35 × 8.000 = 430.000 ₺. Toplam bütçenin "
    "hacimle orantılı küçültülmesi (400.000 ₺) sabit giderleri de değişken sayar.", zorluk="easy")

statik = 200_000 + 30 * 10_000
esnek = 200_000 + 30 * 9_000
fiili = 482_000
assert (fiili - esnek, statik - fiili) == (12_000, 18_000)
P.q(EB,
    "Bir işletme üretim giderlerini 10.000 birimlik üretime göre 500.000 ₺ olarak bütçelemiştir (sabit 200.000 ₺, "
    "birim değişken 30 ₺). Ay içinde 9.000 birim üretilmiş ve 482.000 ₺ gider gerçekleşmiştir.\n\nEsnek bütçeye "
    "göre harcama sapması ve yorumu aşağıdakilerden hangisidir?",
    "12.000 ₺ olumsuz; giderler üretim düzeyine göre fazladır.",
    ["18.000 ₺ olumlu; giderler bütçenin altında kalmıştır.",
     "12.000 ₺ olumlu; giderler üretim düzeyine göre azdır.",
     "18.000 ₺ olumsuz; giderler statik bütçeyi aşmıştır.",
     "30.000 ₺ olumsuz; üretim hacmi bütçenin altındadır."],
    "Fiili hacme göre esnek bütçe = 200.000 + 30 × 9.000 = 470.000 ₺; harcama sapması = 482.000 − 470.000 = 12.000 ₺ "
    "olumsuz. Statik bütçeyle karşılaştırma (18.000 ₺ olumlu) hacim düşüşünü tasarruf gibi gösterir ve yanıltıcıdır.",
    zorluk="hard")

P.sayisal(EB,
    "Bir işletme ürününün birim satış fiyatını 50 ₺ olarak bütçelemiş, 10.000 birim satış öngörmüştür. Ay içinde "
    "rekabet nedeniyle birim fiyat 48 ₺’ye düşmüş ve 11.000 birim satılmıştır.\n\nSatış fiyat sapması kaç ₺’dir?",
    tl(2 * 11_000), secenekler(22_000, 20_000, 50_000, 28_000, 2_000),
    "Satış fiyat sapması = (fiili fiyat − bütçe fiyatı) × fiili miktar = (48 − 50) × 11.000 = 22.000 ₺ olumsuz. "
    "Bütçelenen miktarla hesaplamak (20.000 ₺) hacim etkisini karıştırır.")

P.sayisal(EB,
    "Bir işletme 10.000 birim satış bütçelemiş; bütçelenen birim fiyat 50 ₺, bütçelenen birim değişken maliyet 30 "
    "₺’dir. Ay içinde 11.000 birim satılmıştır. İşletme sapmaları katkı payı esasına göre analiz etmektedir.\n\n"
    "Satış hacmi sapması kaç ₺’dir?",
    tl(1_000 * 20), secenekler(20_000, 50_000, 30_000, 220_000, 2_000),
    "Katkı esaslı satış hacmi sapması = (fiili miktar − bütçe miktarı) × bütçelenen birim katkı = 1.000 × (50 − 30) = "
    "20.000 ₺ olumlu. Gelir esasında 1.000 × 50 = 50.000 ₺ olurdu.")

P.sayisal(EB,
    "Bir işletmenin ay içindeki fiili gideri 525.000 ₺ olup performans raporunda harcama sapması 25.000 ₺ olumsuz "
    "olarak gösterilmiştir. Sapma fiili faaliyet düzeyine göre hazırlanan esnek bütçeyle hesaplanmıştır.\n\nFiili "
    "faaliyet düzeyine göre esnek bütçe tutarı kaç ₺’dir?",
    tl(500_000), secenekler(500_000, 550_000, 525_000, 475_000, 25_000),
    "Olumsuz sapma fiili giderin bütçeyi aştığını gösterir: esnek bütçe = 525.000 − 25.000 = 500.000 ₺.",
    zorluk="easy")

P.sayisal(EB,
    "Bir işletme hammaddeyi fiilen kilogram başına 33 ₺’den 6.000 kg olarak satın almıştır. Performans raporunda "
    "satın alma fiyat sapması 18.000 ₺ olumsuz olarak raporlanmıştır.\n\nBütçelenen kilogram fiyatı kaç ₺’dir?",
    tl(33 - 18_000 / 6_000), secenekler(30, 36, 33, 27, 31),
    "Fiyat sapması = (fiili fiyat − bütçe fiyatı) × fiili miktar; olumsuz sapma fiili fiyatın yüksek olduğunu "
    "gösterir: 18.000 ÷ 6.000 = 3 ₺. Bütçe fiyatı = 33 − 3 = 30 ₺.")

P.sayisal(EB,
    "Bir işletmede ay içinde 14.400 birim satılmıştır. Bütçelenen birim satış fiyatı 70 ₺’dir ve gelir esasına "
    "göre satış hacmi sapması 84.000 ₺ olumlu olarak raporlanmıştır.\n\nBütçelenen satış miktarı kaç birimdir?",
    birim(14_400 - 84_000 / 70), [birim(x) for x in (15_600, 14_400, 12_000, 1_200)],
    "Hacim sapması = (fiili miktar − bütçe miktarı) × bütçe fiyatı; 84.000 ÷ 70 = 1.200 birim fazla satılmıştır. "
    "Bütçe miktarı = 14.400 − 1.200 = 13.200 birim.")

P.sayisal(EB,
    "Bir işletmenin 10.000 birimlik fiili faaliyet için hazırlanan esnek bütçe toplamı 470.000 ₺’dir. Birim "
    "değişken gider 32 ₺ olup geçerli aralıkta değişmemektedir.\n\nGeçerli aralıktaki toplam sabit gider kaç "
    "₺’dir?",
    tl(470_000 - 320_000), secenekler(150_000, 320_000, 470_000, 138_000, 47_000),
    "Sabit gider = esnek bütçe − değişken gider = 470.000 − 32 × 10.000 = 150.000 ₺.", zorluk="easy")

P.sayisal(EB,
    "Bir işletmenin 12.000 birim fiili faaliyet düzeyi için hazırlanan esnek bütçe gideri 516.000 ₺’dir. Toplam "
    "sabit gider 180.000 ₺’dir ve geçerli aralıkta değişmemektedir.\n\nBirim başına bütçelenen değişken gider kaç "
    "₺’dir?",
    tl((516_000 - 180_000) / 12_000), secenekler(28, 43, 15, 58, 30),
    "Değişken gider toplamı = 516.000 − 180.000 = 336.000 ₺; birim değişken gider = 336.000 ÷ 12.000 = 28 ₺.")

P.q(EB,
    "Bir fabrikada ay içinde fiili üretim bütçelenenden %15 yüksek gerçekleşmiş, üretim giderleri de statik bütçeyi "
    "aşmıştır. Üst yönetim fabrika müdürünü giderleri kontrol edememekle eleştirmektedir.\n\nFabrika müdürünün "
    "harcama performansı nasıl değerlendirilmelidir?",
    "Fiili gider, fiili üretime göre esnek bütçeyle karşılaştırılmalıdır.",
    ["Fiili gider, dönem başındaki statik bütçeyle karşılaştırılmalıdır.",
     "Fiili gider, geçen yılın aynı ayıyla karşılaştırılmalıdır.",
     "Sapmanın tamamı üretim fazlalığından doğduğu için dikkate alınmaz.",
     "Sabit giderler de üretimle orantılı artırılarak karşılaştırılmalıdır."],
    "Üretim hacmi değiştiğinde değişken giderlerin de değişmesi doğaldır. Harcama performansı, fiili hacme uyarlanmış "
    "esnek bütçeyle ölçülür; statik bütçeyle karşılaştırma hacim etkisini verimsizlik gibi gösterir.")

P.q(EB,
    "Bir işletmenin maliyet muhasebecisi esnek bütçe hazırlama yöntemini yeni çalışanlara anlatmaktadır. Anlatımdaki "
    "ifadelerden biri hatalıdır.\n\nEsnek bütçeyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Sabit giderler faaliyet hacmine göre orantılı değiştirilir.",
    ["Değişken giderler fiili faaliyet düzeyine uyarlanır.",
     "Birden fazla faaliyet düzeyi için hazırlanabilir.",
     "Harcama sapmasını hacim etkisinden ayırmayı sağlar.",
     "Maliyetlerin sabit ve değişken olarak ayrılmasını gerektirir."],
    "Esnek bütçede değişken giderler fiili hacme göre ayarlanır, sabit giderler ise geçerli aralıkta aynı tutarda "
    "bırakılır. Sabit giderlerin orantılı değiştirilmesi esnek bütçenin mantığıyla çelişir.")

P.oncul(EB,
    "Esnek bütçe ve performans raporlarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Esnek bütçe fiili faaliyet düzeyine göre hazırlanır.",
     "Statik bütçe sapması satış hacmindeki değişimin etkisini de içerir.",
     "Esnek bütçede sabit giderler fiili hacimle orantılı olarak artırılır.",
     "Harcama sapması, fiili gider ile esnek bütçe arasındaki farktır."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve IV", "II ve III", "I, II ve III", "I, II ve IV", "II, III ve IV"],
    "I, II ve IV doğrudur. III yanlıştır: sabit giderler geçerli aralıkta hacimden bağımsızdır ve esnek bütçede aynı "
    "tutarda kalır.")

# ------------------------------------------------------------------ sorumluluk muhasebesi
P.q(SM,
    "Bir işletmenin montaj bölümü yöneticisi yalnızca bölümdeki malzeme kullanımı, işçilik ve bakım giderleri "
    "üzerinde yetki sahibidir. Bölüm dış müşterilere satış yapmamakta, yatırım kararları genel merkezde "
    "alınmaktadır.\n\nSorumluluk muhasebesi açısından montaj bölümü nasıl sınıflandırılır?",
    "Maliyet merkezi",
    ["Kâr merkezi", "Yatırım merkezi", "Gelir merkezi", "Hizmet satış merkezi"],
    "Yöneticinin yalnız maliyetler üzerinde yetkili olduğu ve gelir yaratmayan birimler maliyet merkezidir; "
    "performansı bütçelenen maliyetlerle karşılaştırılarak ölçülür.", zorluk="easy")

P.q(SM,
    "Bir perakende zincirinin bölge müdürü; bölgedeki mağazaların satış fiyatlarını, kampanyalarını ve işletme "
    "giderlerini belirleyebilmektedir. Mağaza açma ve kapatma gibi yatırım kararları ise genel merkez tarafından "
    "alınmaktadır.\n\nSorumluluk muhasebesi açısından bu bölge nasıl sınıflandırılır?",
    "Kâr merkezi",
    ["Maliyet merkezi", "Yatırım merkezi", "Gelir merkezi", "Harcama merkezi"],
    "Yöneticinin hem gelirler hem maliyetler üzerinde yetkili olduğu, ancak yatırım tabanını belirleyemediği birim kâr "
    "merkezidir; performansı bölüm kârıyla ölçülür.")

P.q(SM,
    "Bir holdingin bir iştiraki; ürün fiyatlarını, giderlerini ve yeni makine, depo gibi yatırımlarını kendisi "
    "belirlemektedir. Holding, iştirakin performansını kullandığı varlıklarla ilişkilendirerek ölçmek "
    "istemektedir.\n\nBu birim nasıl sınıflandırılır ve performansı hangi ölçütle değerlendirilir?",
    "Yatırım merkezi; yatırım getirisi ve artık gelir",
    ["Kâr merkezi; brüt satış kârı",
     "Maliyet merkezi; bütçe-fiili gider farkı",
     "Gelir merkezi; satış hacmi sapması",
     "Kâr merkezi; birim başına katkı payı"],
    "Gelir, maliyet ve yatırım tabanı üzerinde yetkili yönetici yatırım merkezini yönetir. Performans, kârın "
    "kullanılan varlıklarla ilişkisini gösteren yatırım getirisi (ROI) ve artık gelir ile ölçülür.")

roi = 360_000 / 2_400_000
P.sayisal(SM,
    "Bir yatırım merkezinin dönem verileri şöyledir: satış hasılatı 3.000.000 ₺, faaliyet kârı 360.000 ₺ ve "
    "ortalama yatırım tabanı 2.400.000 ₺. Genel merkez bölümleri yatırım getirisiyle "
    "değerlendirmektedir.\n\nBölümün yatırım getirisi (ROI) yüzde kaçtır?",
    "%15", ["%12", "%80", "%125", "%18"],
    "ROI = faaliyet kârı ÷ yatırım tabanı = 360.000 ÷ 2.400.000 = %15. Bu oran kâr marjı (%12) ile yatırım devir "
    "hızının (1,25) çarpımına eşittir.", zorluk="easy")

ag = 360_000 - 0.12 * 2_400_000
P.sayisal(SM,
    "Bir yatırım merkezi 360.000 ₺ faaliyet kârı ve 2.400.000 ₺ yatırım tabanı raporlamıştır. Genel merkezin "
    "bölümlerden beklediği asgari getiri oranı %12’dir.\n\nBölümün artık geliri kaç ₺’dir?",
    tl(ag), secenekler(ag, 288_000, 360_000, 43_200, 432_000),
    "Artık gelir = faaliyet kârı − yatırım tabanı × asgari getiri = 360.000 − 2.400.000 × %12 = 360.000 − 288.000 = "
    "72.000 ₺.")

P.sayisal(SM,
    "Bir yatırım merkezinin faaliyet kârı 390.000 ₺, yatırım tabanı 2.500.000 ₺ ve artık geliri 90.000 ₺ olarak "
    "raporlanmıştır. Denetim ekibi hesaplamada kullanılan asgari getiri oranını doğrulamak istemektedir.\n\n"
    "Kullanılan asgari getiri oranı yüzde kaçtır?",
    "%12", ["%15,6", "%3,6", "%18", "%10"],
    "Asgari getiri tutarı = 390.000 − 90.000 = 300.000 ₺; oran = 300.000 ÷ 2.500.000 = %12. Bölümün ROI’si ise "
    "%15,6’dır.")

P.sayisal(SM,
    "Bir yatırım merkezinin ortalama yatırım tabanı 3.000.000 ₺ ve yatırım getirisi %18’dir. Bölümün satış "
    "hasılatı 4.500.000 ₺’dir.\n\nBölümün faaliyet kârı kaç ₺’dir?",
    tl(540_000), secenekler(540_000, 810_000, 360_000, 166_667, 450_000),
    "Faaliyet kârı = yatırım tabanı × ROI = 3.000.000 × %18 = 540.000 ₺. Kâr marjı %12, yatırım devir hızı 1,5’tir.")

P.q(SM,
    "Bir bölümün mevcut yatırım getirisi %18’dir. Bölüm yöneticisine, getirisi %14 olan yeni bir proje "
    "önerilmiştir; işletmenin sermaye maliyeti %12’dir. Yönetici primini bölümün ROI’sine göre almaktadır ve "
    "projeyi reddetmeyi düşünmektedir.\n\nBu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Proje işletme için kabul edilmeli; artık gelir ölçütü bu uyumu sağlar.",
    ["Proje ROI’yi düşürdüğü için işletme açısından da reddedilmelidir.",
     "Proje getirisi sermaye maliyetinin altında olduğu için reddedilmelidir.",
     "ROI ve artık gelir bu projede aynı kararı verdiğinden fark yoktur.",
     "Proje ancak getirisi %18’in üzerine çıkarsa artık geliri artırır."],
    "Projenin getirisi (%14) sermaye maliyetinin (%12) üzerinde olduğundan artık geliri artırır ve işletme için "
    "yararlıdır. ROI’ye göre ödüllendirilen yönetici bölüm oranını düşüreceği için reddetmek ister; artık gelir bu "
    "amaç uyumsuzluğunu giderir.", zorluk="hard")

P.sayisal(SM,
    "Bir işletmenin satıcı bölümü ürettiği bir parçayı dış pazarda 60 ₺’den satmakta ve dış satışlarda birim başına "
    "3 ₺ satış gideri katlanmaktadır; iç satışlarda bu gider doğmamaktadır. Parçanın birim değişken maliyeti 42 "
    "₺’dir ve bölüm tam kapasiteyle çalışmaktadır.\n\nSatıcı bölüm için asgari transfer fiyatı kaç ₺’dir?",
    tl(42 + (60 - 42 - 3)), secenekler(57, 60, 42, 63, 45),
    "Asgari transfer fiyatı = birim değişken maliyet + vazgeçilen dış satış katkısı = 42 + (60 − 42 − 3) = 57 ₺. "
    "İç satışta 3 ₺ satış gideri doğmadığından piyasa fiyatının tamamı (60 ₺) gerekmez.", zorluk="hard")

P.q(SM,
    "Bir bölüm müdürünün performans raporunda ay içinde önemli bir olumsuz sapma görülmüştür. İnceleme, sapmanın "
    "tamamının genel merkezin bölüme dağıttığı bilgi işlem giderindeki artıştan ve müdürün etkileyemediği bir yasal "
    "düzenlemeden kaynaklandığını göstermiştir.\n\nBu durumda uygulanması gereken sorumluluk muhasebesi ilkesi "
    "aşağıdakilerden hangisidir?",
    "Kontrol edilebilirlik ilkesi",
    ["İstisnalara göre yönetim ilkesi", "Tutarlılık ilkesi", "İhtiyatlılık ilkesi", "Dönemsellik ilkesi"],
    "Kontrol edilebilirlik ilkesine göre yöneticiler yalnızca etkileyebildikleri gelir ve maliyetlerden sorumlu "
    "tutulur; kontrol dışı kalemler raporda ayrı gösterilir ve performans değerlendirmesinde dışarıda bırakılır.")

P.q(SM,
    "Bir işletmenin sorumluluk muhasebesi sistemi yeniden düzenlenmektedir. Proje ekibinin hazırladığı ilkeler "
    "listesinde bir hatalı madde bulunmaktadır.\n\nSorumluluk muhasebesiyle ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Maliyet merkezi yöneticisi dağıtılan genel merkez giderlerinden sorumlu tutulur.",
    ["Raporlar örgüt yapısındaki yetki ve sorumluluk düzeylerine göre hazırlanır.",
     "Kâr merkezi yöneticisi gelir ve giderlerden birlikte sorumludur.",
     "Yatırım merkezinin performansı kullanılan varlıklarla ilişkilendirilir.",
     "Kontrol edilemeyen kalemler raporda ayrı gösterilebilir."],
    "Dağıtılan genel merkez giderleri maliyet merkezi yöneticisinin kontrolü dışındadır; performans değerlendirmesinde "
    "bu giderlerden sorumlu tutulmamalıdır. Diğer ifadeler sorumluluk muhasebesinin temel ilkeleridir.")

# ------------------------------------------------------------------ bütçe türleri ve süreç
P.q(BT,
    "Bir işletmenin bütçe komitesi ana bütçe takvimini hazırlamaktadır. Üretim, satın alma, işçilik ve nakit "
    "bütçelerinin hangi sırayla hazırlanacağı tartışılmakta; talebin kapasiteden düşük olduğu öngörülmektedir.\n\n"
    "Ana bütçe sürecinde satış bütçesinin diğer faaliyet bütçelerinden önce hazırlanmasının nedeni "
    "aşağıdakilerden hangisidir?",
    "Üretim ve gider bütçeleri satış miktarına dayandığı için",
    ["Nakit bütçesinin satış bütçesine veri sağlaması gerektiği için",
     "Satış bütçesinin vergi beyannamesi için zorunlu olduğu için",
     "Bütçelenmiş bilançonun satış bütçesinden önce hazırlandığı için",
     "Sabit giderlerin satış miktarına göre orantılı belirlendiği için"],
    "Talep kısıtlayıcı faktör olduğunda üretim, hammadde, işçilik, GÜG ve pazarlama bütçeleri satış tahminine "
    "dayanır; bu nedenle ana bütçe satış bütçesiyle başlar. Nakit bütçesi ve bütçelenmiş tablolar en son hazırlanır.",
    zorluk="easy")

P.q(BT,
    "Bir işletmede talep yıllık 20.000 birim olmasına karşın darboğaz makinesi en çok 16.000 birim üretime izin "
    "vermektedir. Ek kapasite gelecek yıl içinde sağlanamayacaktır.\n\nAna bütçe hazırlanırken hangi yaklaşım "
    "izlenmelidir?",
    "Bütçe, sınırlayıcı faktör olan üretim kapasitesine göre kurulmalıdır.",
    ["Satış bütçesi talep tahmini olan 20.000 birime göre hazırlanmalıdır.",
     "Üretim bütçesi talep ile kapasitenin ortalamasına göre kurulmalıdır.",
     "Kapasite açığı nakit bütçesinde finansman ihtiyacı olarak gösterilmelidir.",
     "Darboğaz dikkate alınmadan bütçe dönem içinde revize edilmelidir."],
    "Ana bütçe, işletmenin faaliyetini sınırlayan temel faktörden (bütçe kısıtı) başlatılır. Burada kısıt talep değil "
    "üretim kapasitesidir; satış ve diğer bütçeler 16.000 birime göre uyumlu hâle getirilmelidir.")

P.q(BT,
    "Bir işletmenin yönetim kurulu ana bütçe hazırlama sürecini gözden geçirmektedir. Bütçe uzmanının hazırladığı "
    "süreç notunda bir hatalı ifade yer almaktadır.\n\nAna bütçe süreciyle ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Nakit bütçesi, satış bütçesinden önce hazırlanır.",
    ["Üretim bütçesi, satış bütçesi ve stok politikasına dayanır.",
     "Hammadde satın alma bütçesi üretim bütçesinden türetilir.",
     "Bütçelenmiş gelir tablosu faaliyet bütçelerinden sonra hazırlanır.",
     "Bütçelenmiş bilanço nakit bütçesinden veri alır."],
    "Nakit bütçesi tahsilat ve ödemeleri gösterdiğinden satış, satın alma ve gider bütçelerinden sonra hazırlanan "
    "finansal bütçelerdendir. Satış bütçesinden önce hazırlanamaz.", zorluk="easy")

P.q(BT,
    "Bir belediye şirketi, her yıl bütçeyi bir önceki yılın tutarlarını enflasyon oranında artırarak "
    "hazırlamaktan vazgeçmiştir. Yeni sistemde her birim, bütçe talebindeki her kalemi yeni dönem için baştan "
    "gerekçelendirmek ve faaliyetlerin gerekliliğini kanıtlamak zorundadır.\n\nBu bütçeleme yaklaşımı "
    "aşağıdakilerden hangisidir?",
    "Sıfır tabanlı bütçeleme",
    ["Artırımlı (geleneksel) bütçeleme", "Kayan (sürekli) bütçeleme", "Faaliyet tabanlı bütçeleme",
     "Esnek bütçeleme"],
    "Her bütçe kaleminin geçmiş tutarlardan bağımsız olarak sıfırdan gerekçelendirildiği yaklaşım sıfır tabanlı "
    "bütçelemedir. Önceki yıl tutarlarının artırılması ise artırımlı bütçelemedir.", zorluk="easy")

P.q(BT,
    "Bir işletme on iki aylık bütçesini her ay güncellemektedir: biten ay bütçeden çıkarılmakta ve bütçenin sonuna "
    "yeni bir ay eklenmektedir. Böylece bütçe her zaman önümüzdeki on iki ayı kapsamaktadır.\n\nBu bütçeleme "
    "yöntemi aşağıdakilerden hangisidir?",
    "Kayan (sürekli) bütçeleme",
    ["Sıfır tabanlı bütçeleme", "Statik bütçeleme", "Program bütçeleme", "Faaliyet tabanlı bütçeleme"],
    "Bütçe ufkunun her dönem yeni bir ay veya çeyrek eklenerek sabit uzunlukta tutulduğu yöntem kayan (sürekli) "
    "bütçelemedir; planların güncel kalmasını sağlar.")

P.q(BT,
    "Bir işletme gider bütçesini, sipariş işleme, makine ayarı ve kalite kontrol gibi faaliyetlerin öngörülen "
    "işlem sayılarından hareketle hazırlamaktadır. Bir süreç iyileştirmesi sonucunda gelecek yıl makine ayarı "
    "sayısının %30 azalması beklenmektedir.\n\nBu bütçeleme yaklaşımında iyileştirmenin bütçeye ilk yansıması "
    "aşağıdakilerden hangisidir?",
    "Ayar faaliyetinin kaynak ihtiyacı ve bütçesi azalır.",
    ["Tüm GÜG’ler üretim hacmine göre %30 azaltılır.",
     "Satış bütçesi ayar sayısındaki azalış oranında düşer.",
     "Ayar gideri sabit sayıldığından bütçe değişmez.",
     "Yalın süreç nedeniyle nakit bütçesi hazırlanmaz."],
    "Faaliyet tabanlı bütçelemede kaynak ihtiyacı faaliyet sürücülerinin öngörülen miktarından türetilir; ayar sayısı "
    "azalınca ayar faaliyetine ayrılan kaynaklar ve bütçesi azalır.")

P.q(BT,
    "Bir işletmede bölüm müdürleri kendi sorumluluk alanlarının bütçe hedeflerinin belirlenmesine aktif olarak "
    "katılmaktadır. Genel müdür, bu yöntemin güçlü ve zayıf yönlerini değerlendirmektedir.\n\nAşağıdakilerden "
    "hangisi katılımcı bütçelemenin yararlarından biri değildir?",
    "Bütçe boşluğu yaratma riskini ortadan kaldırması",
    ["Hedeflerin yöneticiler tarafından benimsenmesini artırması",
     "Alt kademenin sahadaki bilgisinden yararlanılması",
     "Yöneticilerin motivasyonunu ve bağlılığını güçlendirmesi",
     "Kademeler arası iletişimi ve koordinasyonu artırması"],
    "Katılımcı bütçeleme benimsemeyi, motivasyonu ve bilgi akışını artırır; ancak yöneticilerin hedefleri kolay "
    "ulaşılabilir kılmak için giderleri yüksek, gelirleri düşük göstermesi (bütçe boşluğu) riskini doğurur.")

P.q(BT,
    "Bir satış müdürü, performans primine kolay hak kazanmak için güvenilir piyasa tahmini 12.000 birim iken satış "
    "bütçesini 10.500 birim olarak önermiştir. Üretim müdürü de gider bütçesini gerçekçi tahminin üzerinde "
    "sunmuştur.\n\nBu davranış aşağıdakilerden hangisiyle açıklanır?",
    "Bütçe boşluğu (bütçe gevşekliği)",
    ["Kontrol edilebilirlik ilkesi", "İstisnalara göre yönetim", "Amaç uyumu", "Esnek bütçeleme"],
    "Yöneticilerin hedeflere kolay ulaşmak için gelirleri düşük, giderleri yüksek tahmin etmesi bütçe boşluğudur "
    "(bütçe gevşekliği). Özellikle katılımcı bütçelemede ve prim sistemleri bütçeye bağlı olduğunda görülür.")

P.q(BT,
    "Bir işletmenin bütçe raporlarında sıfır tabanlı, kayan ve faaliyet tabanlı bütçeleme yöntemleri "
    "karşılaştırılmaktadır. Karşılaştırma tablosundaki bir ifade hatalıdır.\n\nBütçe türleriyle ilgili "
    "aşağıdakilerden hangisi yanlıştır?",
    "Sıfır tabanlı bütçede geçmiş yıl tutarları başlangıç noktası alınır.",
    ["Kayan bütçede bütçe ufku her dönem yeni bir dönem eklenerek korunur.",
     "Faaliyet tabanlı bütçede kaynak ihtiyacı faaliyet sürücülerinden türetilir.",
     "Sıfır tabanlı bütçeleme yönetsel iş yükünü artırabilir.",
     "Esnek bütçe birden fazla faaliyet düzeyi için hazırlanabilir."],
    "Sıfır tabanlı bütçede her kalem sıfırdan gerekçelendirilir; geçmiş yıl tutarlarını başlangıç alan yöntem "
    "artırımlı bütçelemedir. Diğer ifadeler doğrudur.")

P.q(BT,
    "Bir işletmede satış bölümü yüksek stok bulundurulmasını isterken üretim bölümü kapasite kısıtını, finans bölümü "
    "ise nakit sıkıntısını gerekçe göstermektedir. Bütçe komitesi bölümlerin planlarını ortak bir hedefte "
    "birleştirmek için ana bütçeyi kullanmaktadır.\n\nBütçenin burada öne çıkan işlevi aşağıdakilerden hangisidir?",
    "Koordinasyon",
    ["Performans ölçümü", "Motivasyon", "Kontrol", "Yetkilendirme"],
    "Bütçe, farklı bölümlerin plan ve hedeflerini birbiriyle uyumlu hâle getirerek koordinasyon sağlar; satış, "
    "üretim ve finans planları tek bir ana bütçede tutarlı kılınır.")

P.q(BT,
    "Bir işletme, hammadde fiyatlarının üç ay sonra %25 artacağına ilişkin sektör tahminini dikkate alarak artış "
    "gerçekleşmeden alternatif tedarikçilerle anlaşmış ve bütçesini buna göre revize etmiştir.\n\nBu uygulama "
    "aşağıdaki kontrol türlerinden hangisine örnektir?",
    "İleriye dönük (önleyici) kontrol",
    ["Geriye dönük (sonuç) kontrolü", "Eş zamanlı kontrol", "Dış denetim", "Sapma analizi"],
    "Sapma ortaya çıkmadan önce gelecekteki gelişmeleri öngörüp önlem alan kontrol ileriye dönük (önleyici) "
    "kontroldür. Geriye dönük kontrol ise gerçekleşen sonuçları bütçeyle karşılaştırır.")

P.q(BT,
    "Bir işletme ana bütçenin son aşamasında bütçelenmiş gelir tablosunda dönem kârını, nakit bütçesinde ise dönem "
    "sonu nakdini hesaplamıştır. Bütçe uzmanı, bu verilerin bütçelenmiş bilançoya nasıl aktarılacağını "
    "açıklamaktadır.\n\nİki tablo arasındaki bağlantıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Dönem kârı özkaynaklara, dönem sonu nakdi hazır değerlere aktarılır.",
    ["Dönem kârı hazır değerlere, dönem sonu nakdi özkaynaklara aktarılır.",
     "Dönem kârı ve nakit birbirine eşit olduğundan tek kalemde gösterilir.",
     "Dönem kârı yabancı kaynaklara, nakit dönen varlıklara aktarılır.",
     "Bütçelenmiş bilanço gelir tablosundan bağımsız olarak hazırlanır."],
    "Bütçelenmiş gelir tablosundaki dönem kârı bilançonun özkaynaklar bölümüne, nakit bütçesinden gelen dönem sonu "
    "nakdi ise dönen varlıklardaki hazır değerlere aktarılır; kâr ile nakit tahakkuk esası nedeniyle farklıdır.")

P.q(FB,
    "Bir işletme yeni yıl satış tahminini 2.000 birim azaltmıştır. Hedef dönem sonu mamul stoku ve dönem başı mamul "
    "stoku değiştirilmemiş, birim başına hammadde kullanımı da aynı kalmıştır.\n\nBu değişikliğin bütçelere etkisi "
    "aşağıdakilerden hangisidir?",
    "Üretim bütçesi 2.000 birim azalır, hammadde bütçesi de buna bağlı düşer.",
    ["Üretim bütçesi değişmez, satış bütçesi 2.000 birim azalır.",
     "Üretim bütçesi 2.000 birim artar, dönem sonu stok artışı telafi edilir.",
     "Hammadde bütçesi değişmez, işçilik bütçesi azalır.",
     "Satış bütçesi azalırken dönem sonu mamul stoku 2.000 birim artar."],
    "Üretim = satış + hedef son stok − başlangıç stok. Stoklar değişmediğinden satıştaki 2.000 birimlik azalış "
    "üretimi de aynı miktarda azaltır; üretime bağlı hammadde, işçilik ve değişken GÜG bütçeleri de düşer.")

odeme = min(260_000 - 100_000, 200_000)
P.sayisal(NB,
    "Bir işletmenin nakit bütçesinde ay sonu finansman öncesi nakit mevcudu 260.000 ₺ olarak hesaplanmıştır. "
    "İşletme politikası gereği ay sonunda en az 100.000 ₺ nakit bulundurulmakta, fazla nakitle bankaya olan "
    "200.000 ₺’lik kısa vadeli kredinin anaparası mümkün olduğu kadar geri ödenmektedir.\n\nAy sonunda "
    "geri ödenecek kredi anaparası kaç ₺’dir?",
    tl(odeme), secenekler(odeme, 200_000, 100_000, 60_000, 260_000),
    "Kullanılabilir nakit fazlası = 260.000 − 100.000 = 160.000 ₺. Kredi bakiyesi (200.000 ₺) bu tutardan büyük "
    "olduğundan 160.000 ₺ anapara geri ödenir; kalan kredi 40.000 ₺ olur.")

P.q(SM,
    "Bir işletmenin bölge satış ofisinin yöneticisi, satış fiyatları ve ürün maliyetleri genel merkezde "
    "belirlendiği için yalnızca bölgedeki satış hasılatını artırmaktan sorumlu tutulmaktadır. Ofisin küçük işletme "
    "giderleri ayrı bir bütçede izlenmektedir.\n\nSorumluluk muhasebesi açısından bu ofis nasıl sınıflandırılır?",
    "Gelir merkezi",
    ["Kâr merkezi", "Yatırım merkezi", "Maliyet merkezi", "Üretim merkezi"],
    "Yöneticinin performansının esas olarak elde edilen gelirle ölçüldüğü, fiyat ve ürün maliyetleri üzerinde yetkisi "
    "olmayan birimler gelir merkezidir. Performansı satış bütçesiyle karşılaştırılarak değerlendirilir.",
    zorluk="easy")

P.serpistir()

if __name__ == "__main__":
    sys.exit(P.yaz())
