# -*- coding: utf-8 -*-
"""Yönetim Muhasebesi · Maliyet-Hacim-Kâr Analizi — 60 soru, 2026 test biçimi.

Maliyet davranışı ve yüksek-düşük noktalar yöntemi; katkı payı, başabaş, hedef kâr (vergi öncesi/sonrası),
nakit başabaş; güvenlik payı ve faaliyet kaldıracı; çok ürünlü analiz ve satış karması; duyarlılık ve maliyet
yapısı seçimi; değişken ve tam maliyetleme farkı gerçek kitapçıklardaki gibi tutar veren olaylarla sorulur.

Dayanak: doğrusal MHK modelinin genel kabul görmüş varsayımları; TMS 2 md. 12-13 (sabit GÜG'ün normal
kapasiteye göre dağıtılması). Vergi oranları yıla bağlı olmasın diye kökte verilir. Tutarlar builder içinde
hesaplanır; her hesap bağımsız bir denklemle denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_maliyet_hacim_kar_2026.json", lesson="yonetim_muhasebesi", topic="maliyet_hacim_kar",
          konu_adi="Maliyet-Hacim-Kâr Analizi", seed=2026093087,
          surum="Doğrusal MHK modeli; TMS 2 md. 12-13; 30.09.2026 kontrolü")

MD = "Maliyet davranışı"
BA = "Başabaş ve hedef kâr analizi"
GK = "Güvenlik payı ve faaliyet kaldıracı"
CU = "Çok ürünlü MHK analizi"
DU = "MHK duyarlılık analizi"
DM = "Değişken ve tam maliyetleme"


def birim(x):
    return f"{tl(x)} birim"


# ------------------------------------------------------------------ maliyet davranışı
tablo1 = ("| Ay | Makine saati | Bakım gideri (₺) |\n|---|---|---|\n| Ocak | 6.200 | 318.000 |\n"
          "| Şubat | 7.800 | 366.000 |\n| Mart | 5.000 | 282.000 |\n| Nisan | 9.000 | 402.000 |\n"
          "| Mayıs | 8.100 | 381.000 |")
dg = (402_000 - 282_000) / (9_000 - 5_000)
assert dg == 30
P.sayisal(MD,
    "Bir tekstil işletmesinin son beş aylık makine saatleri ve bakım giderleri aşağıdaki tabloda verilmiştir:\n\n"
    + tablo1 + "\n\nYüksek-düşük noktalar yöntemine göre makine saati başına değişken bakım gideri kaç ₺’dir?",
    tl(dg), secenekler(dg, 44.67, 56.4, 33, 24),
    "En yüksek (Nisan: 9.000 saat, 402.000 ₺) ve en düşük (Mart: 5.000 saat, 282.000 ₺) faaliyet düzeyleri "
    "alınır: (402.000 − 282.000) ÷ (9.000 − 5.000) = 30 ₺. Ara aylar yöntemde kullanılmaz.", zorluk="easy")

tablo2 = ("| Dönem | Üretim (birim) | Enerji gideri (₺) |\n|---|---|---|\n| 1 | 12.000 | 195.000 |\n"
          "| 2 | 22.000 | 290.000 |\n| 3 | 16.000 | 232.000 |\n| 4 | 8.000 | 150.000 |\n| 5 | 20.000 | 268.000 |")
dg = (290_000 - 150_000) / (22_000 - 8_000)
sb = 150_000 - dg * 8_000
assert (dg, sb) == (10, 70_000) and 290_000 - dg * 22_000 == sb
P.sayisal(MD,
    "Bir plastik enjeksiyon işletmesinin son beş dönemdeki üretim miktarları ve enerji giderleri aşağıdadır:\n\n"
    + tablo2 + "\n\nYüksek-düşük noktalar yöntemine göre dönemlik sabit enerji gideri kaç ₺’dir?",
    tl(sb), secenekler(sb, 80_000, 150_000, 68_000, 90_000),
    "Değişken oran = (290.000 − 150.000) ÷ (22.000 − 8.000) = 10 ₺/birim. Sabit gider = 150.000 − 10 × 8.000 = "
    "70.000 ₺ (sağlama: 290.000 − 10 × 22.000 = 70.000 ₺).")

tah = 84_000 + 12.5 * 14_400
P.sayisal(MD,
    "Bir işletmenin maliyet uzmanı geçmiş verilerden bakım giderini Y = 84.000 + 12,5X (X: makine saati) denklemiyle "
    "tahmin etmiştir. Denklem 8.000-16.000 makine saati aralığındaki verilerden türetilmiştir. Gelecek ay 14.400 "
    "makine saati çalışılması planlanmaktadır.\n\nGelecek ayın tahmini bakım gideri kaç ₺’dir?",
    tl(tah), secenekler(tah, 180_000, 276_000, 254_400, 198_000),
    "Planlanan hacim geçerli aralıkta olduğundan denklem kullanılabilir: 84.000 + 12,5 × 14.400 = 84.000 + 180.000 = "
    "264.000 ₺.", zorluk="easy")

P.q(MD,
    "Bir çağrı merkezinin telefon gideri; hat sayısına bağlı olarak her ay ödenen 18.000 ₺ sabit abonelik ücreti ile "
    "konuşma süresine göre dakika başına 0,40 ₺ tutarındaki kullanım ücretinden oluşmaktadır. Konuşma süresi aydan "
    "aya önemli ölçüde değişmektedir.\n\nBu gider maliyet davranışı bakımından nasıl sınıflandırılır?",
    "Yarı değişken (karma) gider",
    ["Basamaklı sabit maliyet", "Tam değişken maliyet", "Batık maliyet", "Kaçınılamaz sabit maliyet"],
    "Bir kısmı faaliyet hacminden bağımsız (18.000 ₺ abonelik), bir kısmı hacimle orantılı (dakika ücreti) olan "
    "giderler karma (yarı değişken) maliyettir; MHK analizinde sabit ve değişken kısımlarına ayrılır.", zorluk="easy")

P.q(MD,
    "Bir gıda işletmesinde her 2.000 birimlik aylık üretim için bir kalite kontrol uzmanı gerekmektedir. Uzmanlar aylık "
    "sabit maaşla çalışmakta; üretim 2.000 birimi her aştığında yeni bir uzman işe alınmaktadır. Üretim 1.500 "
    "birimden 1.900 birime çıktığında kalite kontrol gideri değişmemiştir.\n\nKalite kontrol uzmanlarının maaşları "
    "maliyet davranışı bakımından nasıl sınıflandırılır?",
    "Basamaklı sabit maliyet",
    ["Karma (yarı değişken) maliyet", "Tam değişken maliyet", "Doğrusal sabit maliyet", "Fırsat maliyeti"],
    "Belirli bir hacim aralığında sabit kalan, aralık aşılınca bir basamak yükselen maliyetler basamaklı sabit "
    "maliyettir. Basamak geniş olduğundan MHK analizinde her aralıkta sabit maliyet gibi ele alınır.")

P.q(MD,
    "Bir işletmenin mevcut tesisinde tek vardiyayla aylık 6.000-12.000 birim arasında üretim yapılabilmektedir. "
    "Yönetim, gelecek yıl talebin 15.000 birime çıkacağını ve bunun için ikinci vardiya ile ek makine kiralanacağını "
    "öngörmektedir. MHK hesapları mevcut aralıktaki verilerle yapılmıştır.\n\nBu durumda MHK analizinin sonuçlarıyla "
    "ilgili aşağıdakilerden hangisi doğrudur?",
    "Mevcut hesaplar 12.000 birimi aşan hacimde güvenilir olmaz.",
    ["Sabit maliyetler 15.000 birimde de mevcut tutarında kalır.",
     "Birim değişken maliyet hacim arttıkça aynı oranda yükselir.",
     "Geçerli aralık dışındaki tahminler daha doğru sonuç verir.",
     "Ek vardiya maliyetleri değil birim satış fiyatını etkiler."],
    "MHK ilişkileri geçerli faaliyet aralığında doğrusal kabul edilir. İkinci vardiya ve ek makine sabit maliyetleri "
    "(ve belki birim değişken maliyeti) değiştireceğinden 12.000 birimi aşan hacim için analiz yeniden yapılmalıdır.")

# ------------------------------------------------------------------ başabaş ve hedef kâr
be = 540_000 / (250 - 160)
P.sayisal(BA,
    "Bir bisiklet üreticisi tek model üretmektedir. Bisikletin satış fiyatı 250 ₺, birim değişken maliyeti (malzeme, "
    "işçilik, değişken GÜG ve satış komisyonu dâhil) 160 ₺’dir. Aylık toplam sabit maliyet 540.000 ₺ olup bunun "
    "360.000 ₺’si üretim, 180.000 ₺’si yönetim giderlerine aittir.\n\nBaşabaş satış miktarı kaç birimdir?",
    birim(be), [birim(x) for x in (2_160, 3_375, 4_000, 6_750)],
    "Birim katkı payı = 250 − 160 = 90 ₺. Başabaş miktarı = toplam sabit maliyet ÷ birim katkı payı = 540.000 ÷ 90 = "
    "6.000 birim. Sabit maliyetin üretim ya da yönetim gideri olması sonucu değiştirmez.", zorluk="easy")

bh = 450_000 / (1 - 0.64)
P.sayisal(BA,
    "Bir perakende işletmesinde değişken maliyetler net satış hasılatının %64’ünü oluşturmaktadır. Yıllık toplam sabit "
    "maliyet 450.000 ₺’dir; işletme birçok ürün sattığı ve satış karmasının dönem içinde değişmediği varsayılmaktadır."
    "\n\nBaşabaş net satış hasılatı kaç ₺’dir?",
    tl(bh), secenekler(bh, 703_125, 1_125_000, 1_500_000, 900_000),
    "Katkı payı oranı = 1 − 0,64 = %36. Başabaş satış hasılatı = 450.000 ÷ 0,36 = 1.250.000 ₺. Değişken maliyet "
    "oranına bölmek (703.125 ₺) katkı payı yerine maliyet oranını kullanmak olur.")

satis, dur, dpaz, sur, syon = 2_400_000, 1_080_000, 240_000, 420_000, 300_000
kp = satis - dur - dpaz
assert kp - sur - syon == 360_000
P.sayisal(BA,
    "Bir işletmenin dönem verileri şöyledir: net satışlar 2.400.000 ₺, değişken üretim maliyeti 1.080.000 ₺, "
    "değişken pazarlama gideri 240.000 ₺, sabit genel üretim gideri 420.000 ₺ ve sabit yönetim gideri 300.000 ₺. "
    "İşletme iç raporlamada katkı payı esaslı gelir tablosu düzenlemektedir.\n\nBu tabloda toplam katkı payı kaç ₺ "
    "olarak gösterilir?",
    tl(kp), secenekler(kp, satis - dur, satis - dur - sur, kp - sur - syon, satis - dur - dpaz - sur),
    "Katkı payı = net satışlar − tüm değişken maliyetler = 2.400.000 − 1.080.000 − 240.000 = 1.080.000 ₺. Sabit "
    "üretim ve yönetim giderleri (720.000 ₺) katkı payından sonra düşülür; faaliyet kârı 360.000 ₺’dir.")

P.q(BA,
    "Bir işletme iç raporlamada katkı payı esaslı gelir tablosu, dış raporlamada ise fonksiyon esaslı (tam maliyet) "
    "gelir tablosu kullanmaktadır. Fabrika binasının aylık 80.000 ₺ kira gideri üretim hacminden bağımsızdır.\n\nBu "
    "kira gideri katkı payı esaslı gelir tablosunda nerede gösterilir?",
    "Katkı payından sonra dönem sabit giderleri arasında",
    ["Satılan malın maliyeti içinde mamul maliyetine katılarak",
     "Değişken üretim maliyetleri arasında satışlardan önce",
     "Satış hasılatından indirim olarak brüt satışların altında",
     "Stok maliyetine eklenip satıldıkça gidere dönüşerek"],
    "Katkı payı esaslı tabloda satışlardan önce tüm değişken maliyetler düşülerek katkı payı bulunur; üretime ilişkin "
    "olanlar dâhil sabit maliyetler katkı payından sonra dönem gideri olarak toplu gösterilir.")

P.q(BA,
    "Bir işletmenin ay sonu raporunda satış hasılatı ile toplam maliyetlerin birbirine eşit olduğu, dolayısıyla "
    "faaliyet kârının sıfır çıktığı görülmüştür. İşletmenin birim satış fiyatı ve birim değişken maliyeti ay içinde "
    "değişmemiştir.\n\nBu satış düzeyi için aşağıdakilerden hangisi doğrudur?",
    "Toplam katkı payı toplam sabit maliyete eşittir.",
    ["Toplam katkı payı sıfırdır.",
     "Toplam satış toplam değişken maliyete eşittir.",
     "Güvenlik payı oranı %100’dür.",
     "Faaliyet kaldıracı derecesi 1’e eşittir."],
    "Başabaş noktasında kâr sıfırdır; bu da katkı payının sabit maliyetleri tam olarak karşıladığı anlamına gelir. "
    "Güvenlik payı sıfır olup faaliyet kaldıracı derecesi tanımsız (sonsuz) hâle gelir.")

hk = (504_000 + 216_000) / (180 - 108)
P.sayisal(BA,
    "Bir ev aletleri üreticisinin tek ürününün satış fiyatı 180 ₺, birim değişken maliyeti 108 ₺’dir. Yıllık sabit "
    "maliyetler 504.000 ₺’dir. Yönetim gelecek yıl için vergi öncesi 216.000 ₺ faaliyet kârı hedeflemektedir.\n\n"
    "Hedef kâra ulaşmak için satılması gereken miktar kaç birimdir?",
    birim(hk), [birim(x) for x in (7_000, 3_000, 12_000, 4_000)],
    "Birim katkı payı = 180 − 108 = 72 ₺. Hedef miktar = (sabit maliyet + hedef kâr) ÷ birim katkı = (504.000 + "
    "216.000) ÷ 72 = 10.000 birim. Başabaş miktarı 7.000 birimdir.")

vo = 240_000 / (1 - 0.20)
hh = (600_000 + vo) / 0.40
P.sayisal(BA,
    "Bir işletmenin katkı payı oranı %40, yıllık sabit maliyeti 600.000 ₺’dir. Kurumlar vergisi oranının %20 olduğu "
    "varsayılmaktadır. Yönetim, vergi sonrası 240.000 ₺ net kâr elde etmeyi hedeflemektedir.\n\nBu hedef için "
    "gerekli satış hasılatı kaç ₺’dir?",
    tl(hh), secenekler(hh, (600_000 + 240_000) / 0.40, 600_000 / 0.40, 2_400_000, 2_700_000),
    "Vergi öncesi kâr = 240.000 ÷ (1 − 0,20) = 300.000 ₺. Gerekli hasılat = (600.000 + 300.000) ÷ 0,40 = 2.250.000 ₺. "
    "Vergi etkisi dikkate alınmazsa 2.100.000 ₺ bulunur.", zorluk="hard")

hm = 360_000 / (200 - 130 - 0.10 * 200)
P.sayisal(BA,
    "Bir işletmenin ürününün satış fiyatı 200 ₺, birim değişken maliyeti 130 ₺ ve yıllık sabit maliyeti 360.000 "
    "₺’dir. Yönetim, satış hasılatının %10’u kadar faaliyet kârı elde edilecek satış düzeyini belirlemek "
    "istemektedir.\n\nBu hedef için satılması gereken miktar kaç birimdir?",
    birim(hm), [birim(x) for x in (5_143, 6_000, 9_000, 4_800)],
    "Her birimden kâr olarak ayrılacak tutar 200 × %10 = 20 ₺’dir; bu tutar katkı payından düşülür: 70 − 20 = 50 ₺. "
    "Gerekli miktar = 360.000 ÷ 50 = 7.200 birim (hasılat 1.440.000 ₺, kâr 144.000 ₺).", zorluk="hard")

nb = (720_000 - 180_000) / (90 - 54)
P.sayisal(BA,
    "Bir işletmenin yıllık sabit maliyetleri 720.000 ₺ olup bunun 180.000 ₺’si makine ve bina amortismanıdır. Ürünün "
    "satış fiyatı 90 ₺, birim değişken maliyeti 54 ₺’dir ve tüm değişken maliyetler peşin ödenmektedir.\n\nNakit "
    "başabaş satış miktarı kaç birimdir?",
    birim(nb), [birim(x) for x in (20_000, 5_000, 10_000, 8_000)],
    "Nakit başabaş hesabında nakit çıkışı gerektirmeyen amortisman sabit maliyetten düşülür: (720.000 − 180.000) ÷ "
    "(90 − 54) = 540.000 ÷ 36 = 15.000 birim. Muhasebe başabaş noktası 20.000 birimdir.")

kb = 385_000 / (150 - 80 - 0.10 * 150)
P.sayisal(BA,
    "Bir işletmenin ürünü 150 ₺’ye satılmakta; birim değişken üretim maliyeti 80 ₺’dir. Ayrıca bayilere satış "
    "fiyatının %10’u oranında komisyon ödenmektedir. Yıllık sabit maliyetler 385.000 ₺’dir.\n\nBaşabaş satış "
    "miktarı kaç birimdir?",
    birim(kb), [birim(x) for x in (5_500, 7_700, 11_000, 6_000)],
    "Satış komisyonu fiyatla orantılı değişken maliyettir: 150 × %10 = 15 ₺. Birim katkı = 150 − 80 − 15 = 55 ₺. "
    "Başabaş = 385.000 ÷ 55 = 7.000 birim.")

r1 = (350_000 + 100_000) / 50
r2 = (470_000 + 100_000) / 50
assert r1 > 8_000 and r2 > 8_000
P.sayisal(BA,
    "Bir işletmenin birim katkı payı 50 ₺’dir. Yıllık sabit maliyetler 8.000 birimlik üretime kadar 350.000 ₺ "
    "olup bu düzey aşıldığında ek tesis kiralanacağından 470.000 ₺’ye yükselmektedir. Yönetim 100.000 ₺ faaliyet "
    "kârı hedeflemektedir.\n\nHedef kâr için satılması gereken miktar kaç birimdir?",
    birim(r2), [birim(x) for x in (9_000, 7_000, 9_400, 13_000)],
    "Birinci aralıkta gerekli miktar (350.000 + 100.000) ÷ 50 = 9.000 birimdir; bu 8.000 birimlik sınırı aştığı "
    "için geçersizdir. İkinci aralıkta (470.000 + 100.000) ÷ 50 = 11.400 birim bulunur ve aralık içindedir.",
    zorluk="hard")

kp = 120 - 75
mevcut = 7_500 * kp - 405_000
ek = (405_000 + 45_000) / kp - 7_500
assert mevcut == -67_500
P.sayisal(BA,
    "Bir işletme ürününü 120 ₺’den satmakta, birim değişken maliyeti 75 ₺ ve yıllık sabit maliyeti 405.000 ₺’dir. "
    "İşletme bu yıl 7.500 birim satmış ve zarar etmiştir. Yönetim gelecek yıl fiyat ve maliyetler değişmeden 45.000 ₺ "
    "faaliyet kârı elde etmek istemektedir.\n\nBu yılki satışlara ek olarak kaç birim daha satılmalıdır?",
    birim(ek), [birim(x) for x in (1_500, 1_000, 10_000, 3_500)],
    "Bu yılki zarar = 7.500 × 45 − 405.000 = 67.500 ₺. Hedef miktar = (405.000 + 45.000) ÷ 45 = 10.000 birim; ek "
    "satış = 10.000 − 7.500 = 2.500 birim (1.500 birim zararı kapatır, 1.000 birim kârı sağlar).")

# ------------------------------------------------------------------ güvenlik payı ve kaldıraç
bh = 441_000 / 0.35
gp = 1_800_000 - bh
assert gp == 540_000
P.sayisal(GK,
    "Bir işletmenin bütçelenen yıllık satış hasılatı 1.800.000 ₺, katkı payı oranı %35 ve yıllık sabit maliyeti "
    "441.000 ₺’dir. Yönetim, satışların olası bir daralmada zarara geçmeden ne kadar azalabileceğini bilmek "
    "istemektedir.\n\nİşletmenin güvenlik payı tutarı kaç ₺’dir?",
    tl(gp), secenekler(gp, bh, 630_000, 189_000, 1_359_000),
    "Başabaş hasılatı = 441.000 ÷ 0,35 = 1.260.000 ₺. Güvenlik payı = bütçelenen satış − başabaş satış = 1.800.000 − "
    "1.260.000 = 540.000 ₺ (oran %30).")

P.sayisal(GK,
    "Bir işletmenin ürününün satış fiyatı 80 ₺, birim değişken maliyeti 50 ₺ ve yıllık sabit maliyeti 270.000 "
    "₺’dir. İşletme bu yıl 12.000 birim satış yapmıştır.\n\nİşletmenin güvenlik payı oranı yüzde kaçtır?",
    "%25", ["%75", "%33,3", "%20", "%12,5"],
    "Başabaş = 270.000 ÷ 30 = 9.000 birim. Güvenlik payı = 12.000 − 9.000 = 3.000 birim; oranı = 3.000 ÷ 12.000 = "
    "%25. Güvenlik payını başabaş miktarına bölmek (%33,3) yanlış tabanı kullanmaktır.")

P.sayisal(GK,
    "Bir işletmenin katkı payı esaslı gelir tablosunda toplam katkı payı 630.000 ₺, sabit maliyetler 450.000 ₺ ve "
    "faaliyet kârı 180.000 ₺ olarak raporlanmıştır. Yönetim satış değişikliklerinin kâra etkisini ölçmek "
    "istemektedir.\n\nİşletmenin faaliyet kaldıracı derecesi kaçtır?",
    "3,5", ["0,29", "2,5", "4,5", "1,4"],
    "Faaliyet kaldıracı derecesi = toplam katkı payı ÷ faaliyet kârı = 630.000 ÷ 180.000 = 3,5. Satışlardaki %1’lik "
    "değişim kârı %3,5 değiştirir.", zorluk="easy")

yeni = 250_000 * (1 + 4 * 0.06)
P.sayisal(GK,
    "Bir işletmenin mevcut satış düzeyinde faaliyet kaldıracı derecesi 4 ve faaliyet kârı 250.000 ₺’dir. Gelecek "
    "yıl satış miktarının, fiyat ve maliyet yapısı değişmeden %6 artacağı tahmin edilmektedir.\n\nFaaliyet "
    "kaldıracı yaklaşımına göre gelecek yılın faaliyet kârı kaç ₺’dir?",
    tl(yeni), secenekler(yeni, 265_000, 325_000, 290_000, 274_000),
    "Kârdaki değişim = faaliyet kaldıracı derecesi × satıştaki değişim = 4 × %6 = %24. Yeni kâr = 250.000 × 1,24 = "
    "310.000 ₺.")

P.sayisal(GK,
    "Tek ürünlü ve doğrusal maliyet yapısına sahip bir işletmenin güvenlik payı oranı %20’dir. Yönetim, satışlardaki "
    "dalgalanmaların faaliyet kârını ne ölçüde etkileyeceğini değerlendirmek istemektedir; fiyat ve maliyetlerin "
    "değişmeyeceği varsayılmaktadır.\n\nİşletmenin faaliyet kaldıracı derecesi kaçtır?",
    "5", ["4", "0,2", "1,25", "20"],
    "Doğrusal modelde faaliyet kaldıracı derecesi güvenlik payı oranının tersidir: 1 ÷ 0,20 = 5. Satışlar %20 "
    "düşerse kâr %100 azalır ve işletme başabaş noktasına iner.", zorluk="hard")

P.q(GK,
    "Aynı sektörde faaliyet gösteren A ve B işletmelerinin satış hasılatı ve faaliyet kârı bu yıl eşittir. A "
    "işletmesinde maliyetlerin büyük kısmı değişken (parça başı ücret, fason üretim), B işletmesinde ise sabittir "
    "(otomasyon, kendi tesisleri).\n\nİki işletmenin satışları aynı oranda değiştiğinde aşağıdakilerden hangisi "
    "beklenir?",
    "B’nin kârı satış artışında daha hızlı artar, düşüşte daha hızlı azalır.",
    ["A’nın kârı satış artışında daha hızlı artar, düşüşte daha yavaş azalır.",
     "İki işletmenin kârı her satış değişiminde aynı oranda değişir.",
     "B’nin başabaş noktası A’nınkinden daha düşük olduğu için risk azdır.",
     "A’nın faaliyet kaldıracı derecesi B’ninkinden daha yüksektir."],
    "Sabit maliyet ağırlığı yüksek olan B’nin katkı payı ve dolayısıyla faaliyet kaldıracı derecesi daha yüksektir; "
    "kârı satış değişimlerine daha duyarlıdır. Bu, satış artışında avantaj, düşüşte risk demektir.")

P.q(GK,
    "Bir işletmenin finans müdürü, yönetim kuruluna sunacağı risk raporunda güvenlik payı ve faaliyet kaldıracı "
    "kavramlarını açıklamaktadır.\n\nGüvenlik payı ve faaliyet kaldıracıyla ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Sabit maliyet payı arttıkça faaliyet kaldıracı derecesi düşer.",
    ["Başabaş noktasına yaklaştıkça faaliyet kaldıracı derecesi yükselir.",
     "Güvenlik payı oranı, faaliyet kaldıracı derecesinin tersine eşittir.",
     "Güvenlik payı, satışların zarara geçmeden düşebileceği tutarı gösterir.",
     "Faaliyet kaldıracı derecesi toplam katkı payının faaliyet kârına bölümüdür."],
    "Sabit maliyet payı arttıkça aynı kâr için daha yüksek katkı payı gerekir; bu da faaliyet kaldıracı derecesini "
    "yükseltir. Diğer ifadeler doğrudur.")

ky = (204_000 - 120_000) / (22 - 15)
P.sayisal(GK,
    "Bir işletme ürün dağıtımı için iki seçeneği değerlendirmektedir. A seçeneğinde (kendi araç filosu dışında "
    "kiralık araç) yıllık sabit gider 120.000 ₺ ve birim başına 22 ₺, B seçeneğinde (kendi filosu) yıllık sabit gider "
    "204.000 ₺ ve birim başına 15 ₺ gider oluşmaktadır.\n\nİki seçeneğin toplam giderinin eşit olduğu dağıtım "
    "miktarı kaç birimdir?",
    birim(ky), [birim(x) for x in (10_000, 14_000, 16_000, 8_400)],
    "Kayıtsızlık noktasında 120.000 + 22X = 204.000 + 15X olur; 7X = 84.000 ve X = 12.000 birim. Bu miktarın "
    "üstünde birim gideri düşük olan B, altında sabit gideri düşük olan A daha ekonomiktir.")

# ------------------------------------------------------------------ çok ürünlü analiz
ort = 0.40 * 50 + 0.60 * 20
P.sayisal(CU,
    "Bir işletme A ve B olmak üzere iki ürün satmaktadır. Toplam satış miktarının %40’ı birim katkı payı 50 ₺ olan "
    "A’dan, kalanı birim katkı payı 20 ₺ olan B’den oluşmaktadır. Satış karmasının değişmeyeceği varsayılmaktadır.\n\n"
    "Ağırlıklı ortalama birim katkı payı kaç ₺’dir?",
    tl(ort), secenekler(ort, 35, 38, 30, 26),
    "Ağırlıklı ortalama birim katkı = 0,40 × 50 + 0,60 × 20 = 20 + 12 = 32 ₺. Basit ortalama (35 ₺) satış "
    "karmasını dikkate almaz.", zorluk="easy")

paket = 3 * 40 + 2 * 25
paket_be = 850_000 / paket
assert paket_be == 5_000
P.q(CU,
    "Bir işletme her 3 adet A ürününe karşılık 2 adet B ürünü satmaktadır. A’nın birim katkı payı 40 ₺, B’nin 25 "
    "₺’dir. Ortak sabit maliyetler yıllık 850.000 ₺ olup ürünlere dağıtılmamaktadır. Satış karmasının "
    "korunacağı varsayılmaktadır.\n\nBaşabaş noktasında A ve B satış miktarları sırasıyla kaçtır?",
    "15.000 A; 10.000 B",
    ["10.000 A; 15.000 B", "12.500 A; 12.500 B", "5.000 A; 5.000 B", "9.000 A; 6.000 B"],
    "Bir paket (3A + 2B) katkı payı = 3 × 40 + 2 × 25 = 170 ₺. Başabaş paket = 850.000 ÷ 170 = 5.000; A = 5.000 × 3 = "
    "15.000, B = 5.000 × 2 = 10.000 birim.")

P.sayisal(CU,
    "Bir işletmenin satış hasılatının %60’ı katkı payı oranı %50 olan A ürününden, kalanı katkı payı oranı %25 olan "
    "B ürününden gelmektedir. Ortak sabit maliyetler yıllık 480.000 ₺’dir ve hasılat karmasının korunacağı "
    "varsayılmaktadır.\n\nİşletmenin ağırlıklı ortalama katkı payı oranı yüzde kaçtır?",
    "%40", ["%37,5", "%35", "%45", "%30"],
    "Ağırlıklı katkı payı oranı = 0,60 × %50 + 0,40 × %25 = %30 + %10 = %40. Basit ortalama %37,5, ağırlıkların ters "
    "kullanılması ise %35 sonucunu verir.")

bh = 600_000 / 0.40
a_be = bh * 0.60
P.sayisal(CU,
    "Bir işletmenin ağırlıklı ortalama katkı payı oranı %40, ortak sabit maliyetleri yıllık 600.000 ₺’dir. Satış "
    "hasılatının %60’ı A ürününden, %40’ı B ürününden elde edilmekte ve karmanın korunacağı varsayılmaktadır.\n\n"
    "Başabaş noktasında A ürününden elde edilecek satış hasılatı kaç ₺’dir?",
    tl(a_be), secenekler(a_be, bh, 600_000, 1_200_000, 750_000),
    "Toplam başabaş hasılatı = 600.000 ÷ 0,40 = 1.500.000 ₺. A’nın payı = 1.500.000 × %60 = 900.000 ₺; B’ye 600.000 ₺ "
    "düşer.")

P.q(CU,
    "Bir işletme katkı payı oranı %45 olan X ve %20 olan Y ürünlerini satmaktadır. Yeni bir pazarlama kampanyası "
    "sonucunda toplam satış hasılatı değişmemiş, ancak satışların daha büyük kısmı X ürününe kaymıştır. Fiyatlar, "
    "birim değişken maliyetler ve sabit maliyetler değişmemiştir.\n\nBu durumun etkisi aşağıdakilerden hangisidir?",
    "Ağırlıklı katkı oranı yükselir, başabaş hasılatı düşer.",
    ["Ağırlıklı katkı oranı düşer, başabaş hasılatı yükselir.",
     "Toplam hasılat değişmediğinden kâr ve başabaş aynı kalır.",
     "Başabaş hasılatı değişmez, güvenlik payı azalır.",
     "Ağırlıklı katkı oranı yükselir, faaliyet kârı azalır."],
    "Karma katkı oranı yüksek X’e kaydığında ağırlıklı katkı payı oranı yükselir; aynı sabit maliyet daha düşük "
    "hasılatla karşılanır. Hasılat değişmediğinden toplam katkı ve kâr artar, güvenlik payı genişler.")

paket = 1 * 60 + 3 * 20
y = (480_000 + 120_000) / paket * 3
assert y == 15_000
P.sayisal(CU,
    "Bir işletme her 1 adet X ürününe karşılık 3 adet Y ürünü satmaktadır. X’in birim katkı payı 60 ₺, Y’nin 20 "
    "₺’dir. Ortak sabit maliyetler 480.000 ₺ olup yönetim 120.000 ₺ faaliyet kârı hedeflemektedir.\n\nHedef kâr "
    "için kaç adet Y ürünü satılmalıdır?",
    birim(y), [birim(x) for x in (5_000, 12_000, 20_000, 4_000)],
    "Bir paket (1X + 3Y) katkı payı = 60 + 3 × 20 = 120 ₺. Gerekli paket = (480.000 + 120.000) ÷ 120 = 5.000; Y "
    "satışı = 5.000 × 3 = 15.000 adet.")

eski = 360_000 / (45 + 15) * 2
yeni_be = 360_000 / (45 + 3 * 15) * 4
assert (eski, yeni_be) == (12_000, 16_000)
P.sayisal(CU,
    "Bir işletme A ve B ürünlerini satmaktadır; birim katkı payları sırasıyla 45 ₺ ve 15 ₺, ortak sabit maliyetler "
    "360.000 ₺’dir. Satış karması bu yıl 1 A : 1 B iken rakip baskısı nedeniyle gelecek yıl 1 A : 3 B olacaktır.\n\n"
    "Yeni satış karmasında toplam başabaş satış miktarı (A + B) kaç birimdir?",
    birim(yeni_be), [birim(x) for x in (12_000, 4_000, 8_000, 24_000)],
    "Yeni paket (1A + 3B) katkısı = 45 + 45 = 90 ₺; başabaş paket = 360.000 ÷ 90 = 4.000; toplam birim = 4.000 × 4 = "
    "16.000. Eski karmada 12.000 birim yetiyordu; düşük katkılı ürüne kayış başabaş miktarını artırır.",
    zorluk="hard")

P.q(CU,
    "Birden fazla ürün satan bir işletmenin yönetim muhasebecisi, bütçe toplantısında çok ürünlü başabaş analizinin "
    "varsayımlarını ve sonuçlarını açıklamaktadır.\n\nÇok ürünlü başabaş analiziyle ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Satış karması değişse de başabaş satış hasılatı aynı kalır.",
    ["Analiz satış karmasının sabit kaldığını varsayar.",
     "Ortak sabit maliyetler ürünlere dağıtılmadan toplam olarak ele alınır.",
     "Ağırlıklı ortalama katkı payı oranı karmaya göre hesaplanır.",
     "Katkı oranı yüksek ürünün payı artarsa başabaş hasılatı düşer."],
    "Ağırlıklı katkı payı oranı satış karmasına bağlı olduğundan karma değiştiğinde başabaş hasılatı da değişir. "
    "Diğer ifadeler çok ürünlü analizin temel özellikleridir.")

kar = 1_200_000 * 0.35 + 800_000 * 0.25 - 480_000
P.sayisal(CU,
    "Bir işletmenin A ürününden satış hasılatı 1.200.000 ₺ ve katkı payı oranı %35; B ürününden satış hasılatı "
    "800.000 ₺ ve katkı payı oranı %25’tir. İşletmenin ortak sabit maliyetleri 480.000 ₺ olup ürünlere "
    "dağıtılmamaktadır.\n\nİşletmenin toplam faaliyet kârı kaç ₺’dir?",
    tl(kar), secenekler(kar, 620_000, 120_000, 100_000, 160_000),
    "Toplam katkı payı = 1.200.000 × 0,35 + 800.000 × 0,25 = 420.000 + 200.000 = 620.000 ₺. Faaliyet kârı = 620.000 − "
    "480.000 = 140.000 ₺.")

oran = 0.70 * 0.45 + 0.30 * 0.30
vo = 243_000 / 0.75
hh = (486_000 + vo) / oran
assert round(hh) == 2_000_000
P.sayisal(CU,
    "Bir işletmenin hasılat karması %70 X ve %30 Y ürünüdür; katkı payı oranları sırasıyla %45 ve %30’dur. Ortak "
    "sabit maliyetler 486.000 ₺’dir. Kurumlar vergisi oranının %25 olduğu varsayılmakta ve yönetim vergi sonrası "
    "243.000 ₺ net kâr hedeflemektedir.\n\nHedef için gerekli toplam satış hasılatı kaç ₺’dir?",
    tl(round(hh)), secenekler(round(hh), 1_800_000, 1_200_000, 2_200_000, 2_160_000),
    "Ağırlıklı katkı oranı = 0,70 × %45 + 0,30 × %30 = %40,5. Vergi öncesi kâr = 243.000 ÷ 0,75 = 324.000 ₺. "
    "Gerekli hasılat = (486.000 + 324.000) ÷ 0,405 = 2.000.000 ₺.", zorluk="hard")

# ------------------------------------------------------------------ duyarlılık
mevcut_kp = 8_800 * (120 - 70)
yeni_m = mevcut_kp / (110 - 70)
assert yeni_m == 11_000
P.sayisal(DU,
    "Bir işletme ürününü 120 ₺’den satmakta ve ayda 8.800 birim satış yapmaktadır; birim değişken maliyet 70 "
    "₺’dir. Rakip baskısı nedeniyle fiyatın 110 ₺’ye indirilmesi düşünülmektedir. Sabit maliyetler değişmeyecektir."
    "\n\nMevcut faaliyet kârını korumak için indirimli fiyatla kaç birim satılmalıdır?",
    birim(yeni_m), [birim(x) for x in (8_800, 9_600, 2_200, 10_000)],
    "Mevcut katkı payı = 8.800 × 50 = 440.000 ₺. Yeni birim katkı = 110 − 70 = 40 ₺. Aynı katkıyı sağlamak için "
    "440.000 ÷ 40 = 11.000 birim satılmalıdır; satışlar %25 artmalıdır.")

P.sayisal(DU,
    "Bir işletmenin ürününün satış fiyatı 200 ₺, birim değişken maliyeti 125 ₺ ve yıllık sabit maliyeti 600.000 "
    "₺’dir. Tedarikçiyle yapılan yeni anlaşma sonucunda birim değişken maliyet 120 ₺’ye düşecektir.\n\nYeni "
    "maliyet yapısında başabaş satış miktarı kaç birimdir?",
    birim(600_000 / 80), [birim(x) for x in (8_000, 500, 5_000, 3_000)],
    "Yeni birim katkı = 200 − 120 = 80 ₺. Başabaş = 600.000 ÷ 80 = 7.500 birim; eski yapıda 600.000 ÷ 75 = 8.000 "
    "birimdi.", zorluk="easy")

ek_kp = (11_500 - 10_000) * (180 - 110)
fark = ek_kp - 120_000
assert fark == -15_000
P.q(DU,
    "Bir işletme ürününü 180 ₺’den satmakta, birim değişken maliyeti 110 ₺’dir ve yıllık 10.000 birim satış "
    "yapmaktadır. Pazarlama birimi 120.000 ₺’lik bir reklam kampanyasıyla satışların 11.500 birime çıkacağını "
    "öngörmektedir.\n\nKampanyanın faaliyet kârına etkisi ve karar aşağıdakilerden hangisidir?",
    "Kâr 15.000 ₺ azalır; kampanya uygulanmamalıdır.",
    ["Kâr 105.000 ₺ artar; kampanya uygulanmalıdır.",
     "Kâr 150.000 ₺ artar; kampanya uygulanmalıdır.",
     "Kâr 15.000 ₺ artar; kampanya uygulanmalıdır.",
     "Kâr 120.000 ₺ azalır; kampanya uygulanmamalıdır."],
    "Ek katkı payı = 1.500 × (180 − 110) = 105.000 ₺. Kampanya maliyeti 120.000 ₺ olduğundan kâr 15.000 ₺ azalır. "
    "Ek hasılatın (270.000 ₺) reklam gideriyle karşılaştırılması değişken maliyetleri göz ardı eder.")

eski = 12_000 * (75 - 50)
yeni = 10_800 * (80 - 50)
P.sayisal(DU,
    "Bir işletme ürününü 75 ₺’den satmakta ve yılda 12.000 birim satış yapmaktadır; birim değişken maliyet 50 "
    "₺’dir. Fiyatın 80 ₺’ye çıkarılması hâlinde satışların 10.800 birime düşeceği tahmin edilmektedir. Sabit "
    "maliyetler değişmeyecektir.\n\nFiyat artışı faaliyet kârını kaç ₺ artırır?",
    tl(yeni - eski), secenekler(yeni - eski, 54_000, 60_000, 30_000, 36_000),
    "Mevcut katkı = 12.000 × 25 = 300.000 ₺; yeni katkı = 10.800 × 30 = 324.000 ₺. Sabit maliyetler değişmediğinden "
    "kâr 24.000 ₺ artar.")

bh_yeni = 510_000 / 0.30
gp = 2_000_000 - bh_yeni
P.sayisal(DU,
    "Bir işletmenin yıllık satış hasılatı 2.000.000 ₺, katkı payı oranı %30 ve sabit maliyetleri 450.000 ₺’dir. "
    "Yeni bir depo kiralanması nedeniyle sabit maliyetler 510.000 ₺’ye çıkacak, satışlar ve katkı oranı "
    "değişmeyecektir.\n\nYeni durumda işletmenin güvenlik payı tutarı kaç ₺’dir?",
    tl(gp), secenekler(gp, 500_000, 200_000, 60_000, bh_yeni),
    "Yeni başabaş hasılatı = 510.000 ÷ 0,30 = 1.700.000 ₺. Güvenlik payı = 2.000.000 − 1.700.000 = 300.000 ₺. "
    "Eski yapıda güvenlik payı 2.000.000 − 1.500.000 = 500.000 ₺ idi.")

dm = 165 - (540_000 + 300_000) / 12_000
P.sayisal(DU,
    "Bir işletme ürününü 165 ₺’den satmakta ve gelecek yıl 12.000 birim satış beklemektedir. Yıllık sabit maliyetler "
    "540.000 ₺’dir. Yönetim 300.000 ₺ faaliyet kârı hedeflemekte ve tedarikçilerle yapılacak pazarlıkta kabul "
    "edilebilecek en yüksek birim değişken maliyeti belirlemek istemektedir.\n\nBirim değişken maliyet en fazla kaç "
    "₺ olabilir?",
    tl(dm), secenekler(dm, 70, 120, 100, 110),
    "Gerekli birim katkı = (540.000 + 300.000) ÷ 12.000 = 70 ₺. En yüksek birim değişken maliyet = 165 − 70 = 95 ₺.")

fiyat = 70 + 300_000 / 6_000
P.sayisal(DU,
    "Yeni bir ürün için birim değişken maliyet 70 ₺, yıllık sabit maliyet 300.000 ₺ olarak tahmin edilmektedir. "
    "Pazar araştırması ilk yıl en az 6.000 birim satılabileceğini göstermektedir. Yönetim, bu miktarda zarar "
    "etmeyecek en düşük fiyatı belirlemek istemektedir.\n\nBu koşulu sağlayan en düşük birim satış fiyatı kaç "
    "₺’dir?",
    tl(fiyat), secenekler(fiyat, 50, 100, 170, 125),
    "Başabaşta birim katkı = 300.000 ÷ 6.000 = 50 ₺ olmalıdır. En düşük fiyat = 70 + 50 = 120 ₺.")

P.q(DU,
    "Bir mobilya üreticisinde ana hammaddenin fiyatı %20 artmış, rekabet nedeniyle satış fiyatları ise "
    "değiştirilememiştir. Sabit maliyetler ve satış miktarı da aynı kalmıştır.\n\nBu gelişmenin MHK göstergelerine "
    "etkisi aşağıdakilerden hangisidir?",
    "Katkı payı oranı düşer, başabaş satış hasılatı yükselir.",
    ["Katkı payı oranı yükselir, başabaş satış hasılatı düşer.",
     "Katkı payı oranı değişmez, sabit maliyet oranı artar.",
     "Başabaş satış hasılatı düşer, güvenlik payı genişler.",
     "Birim katkı payı artar, faaliyet kaldıracı derecesi azalır."],
    "Değişken maliyet artıp fiyat sabit kalınca birim katkı ve katkı oranı düşer. Aynı sabit maliyeti karşılamak "
    "için daha yüksek hasılat gerekir; güvenlik payı daralır.")

P.q(DU,
    "Bir işletmenin planlama birimi, bütçelenen kârın satış fiyatı, satış miktarı, birim değişken maliyet ve sabit "
    "maliyetlerdeki %5’lik değişimlere nasıl tepki verdiğini tek tek hesaplamakta ve kârı en çok etkileyen "
    "değişkeni belirlemektedir.\n\nBu çalışma aşağıdakilerden hangisidir?",
    "Duyarlılık (ne olur-eğer) analizi",
    ["Faaliyet tabanlı maliyet analizi", "Yüksek-düşük noktalar analizi", "Standart maliyet fark analizi",
     "Dikey yüzdeler analizi"],
    "Model değişkenlerinden biri değiştirildiğinde sonucun nasıl etkilendiğini inceleyen yöntem duyarlılık analizidir; "
    "MHK modelinde belirsizliği yönetmek ve kritik değişkeni belirlemek için kullanılır.", zorluk="easy")

hedef = 1_200_000 * 0.15
m = (270_000 + hedef) / 45
P.sayisal(DU,
    "Bir işletme yeni üretim hattına 1.200.000 ₺ yatırım yapmıştır ve bu yatırım üzerinden yıllık %15 faaliyet "
    "kârı elde etmeyi hedeflemektedir. Hattın yıllık sabit maliyetleri 270.000 ₺, ürünün birim katkı payı 45 "
    "₺’dir.\n\nHedef getiri için yıllık kaç birim satılmalıdır?",
    birim(m), [birim(x) for x in (6_000, 4_000, 14_000, 8_000)],
    "Hedef kâr = 1.200.000 × %15 = 180.000 ₺. Gerekli miktar = (270.000 + 180.000) ÷ 45 = 10.000 birim.")

P.sayisal(DU,
    "Bir işletme gelecek yıl için 3.000.000 ₺ satış hasılatı bütçelemiştir. Yıllık sabit maliyetler 840.000 ₺’dir ve "
    "yönetim 360.000 ₺ faaliyet kârı hedeflemektedir. Satın alma birimi, maliyet sözleşmelerinde uyulacak üst "
    "sınırı bilmek istemektedir.\n\nDeğişken maliyetlerin satış hasılatına oranı en fazla yüzde kaç olabilir?",
    "%60", ["%40", "%72", "%28", "%52"],
    "Gerekli katkı = 840.000 + 360.000 = 1.200.000 ₺; katkı oranı = 1.200.000 ÷ 3.000.000 = %40. Değişken maliyet "
    "oranı en fazla 1 − %40 = %60 olabilir.")

yeni = 400_000 * (1 - 3 * 0.10)
P.sayisal(GK,
    "Bir işletmenin mevcut faaliyet kârı 400.000 ₺ ve faaliyet kaldıracı derecesi 3’tür. Ekonomik daralma "
    "nedeniyle gelecek yıl satış miktarının %10 azalacağı, fiyat ve maliyet yapısının ise değişmeyeceği tahmin "
    "edilmektedir.\n\nGelecek yılın tahmini faaliyet kârı kaç ₺’dir?",
    tl(yeni), secenekler(yeni, 360_000, 120_000, 520_000, 300_000),
    "Kârdaki değişim = 3 × (−%10) = −%30. Yeni kâr = 400.000 × 0,70 = 280.000 ₺. Satışlardaki düşüş kâra kaldıraç "
    "derecesi kadar büyüyerek yansır.")

# ------------------------------------------------------------------ varsayımlar ve maliyetleme
P.q(BA,
    "Bir işletmenin yönetim muhasebecisi MHK analizine başlamadan önce modelin dayandığı varsayımları "
    "listelemektedir. Liste, yeni bir çalışan tarafından hazırlanmış ve bir hatalı madde içermektedir.\n\n"
    "Aşağıdakilerden hangisi doğrusal MHK analizinin varsayımlarından biri değildir?",
    "Birim satış fiyatı satış miktarı arttıkça düşer.",
    ["Maliyetler sabit ve değişken olarak ayrılabilir.",
     "Geçerli aralıkta birim değişken maliyet sabittir.",
     "Çok ürünlü işletmede satış karması sabittir.",
     "Üretilen miktar ile satılan miktar eşittir."],
    "Doğrusal modelde birim satış fiyatı geçerli aralıkta sabittir; hasılat doğrusu bu nedenle düz bir çizgidir. "
    "Miktar arttıkça fiyatın düşmesi (hacim indirimi) doğrusal olmayan bir hasılat eğrisi doğurur.")

P.oncul(MD,
    "Geçerli faaliyet aralığında maliyet davranışına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Toplam sabit maliyet üretim hacmi değişse de aynı kalır.",
     "Birim sabit maliyet üretim hacmi arttıkça azalır.",
     "Birim değişken maliyet üretim hacmi arttıkça azalır.",
     "Toplam değişken maliyet üretim hacmiyle doğru orantılı değişir."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "I, II ve IV doğrudur. III yanlıştır: geçerli aralıkta birim değişken maliyet sabittir; toplam değişken maliyet "
    "hacimle orantılı değişir. Birim sabit maliyet ise sabit tutarın daha çok birime yayılmasıyla azalır.")

bsg = 360_000 / 10_000
fark = (10_000 - 8_500) * bsg
assert fark == 54_000
P.q(DM,
    "Bir işletme dönem içinde 10.000 birim üretmiş ve 8.500 birim satmıştır; dönem başı stok yoktur. Normal "
    "kapasite 10.000 birim olup sabit genel üretim giderleri 360.000 ₺’dir. Diğer tüm maliyetler değişkendir ve "
    "birim maliyetler dönem içinde değişmemiştir.\n\nTam maliyetleme ile değişken maliyetleme yöntemlerine göre "
    "hesaplanan faaliyet kârları arasındaki ilişki aşağıdakilerden hangisidir?",
    "Tam maliyetleme kârı 54.000 ₺ fazladır.",
    ["Değişken maliyetleme kârı 54.000 ₺ fazladır.",
     "Tam maliyetleme kârı 306.000 ₺ fazladır.",
     "İki yöntemde faaliyet kârı eşittir.",
     "Tam maliyetleme kârı 45.900 ₺ fazladır."],
    "Birim sabit GÜG = 360.000 ÷ 10.000 = 36 ₺. Stok 1.500 birim arttığından tam maliyetlemede 1.500 × 36 = 54.000 ₺ "
    "sabit GÜG stokta kalır; bu yöntemde kâr 54.000 ₺ fazladır.", zorluk="hard")

P.q(DM,
    "Bir işletme iç raporlamada değişken maliyetleme yöntemini kullanmakta ve yıl sonunda finansal tablolarını "
    "hazırlamaktadır. Bağımsız denetçi, stokların TMS 2 Stoklar Standardı’na göre ölçülüp ölçülmediğini "
    "incelemektedir.\n\nTMS 2 ile değişken maliyetleme ilişkisi hakkında aşağıdakilerden hangisi yanlıştır?",
    "Değişken maliyetle ölçülen stoklar finansal tablolarda doğrudan kullanılabilir.",
    ["Sabit genel üretim giderleri normal kapasiteye göre dönüşüm maliyetlerine dağıtılır.",
     "Atıl kapasiteye düşen sabit genel üretim gideri oluştuğu dönemde gider yazılır.",
     "Değişken maliyetleme iç raporlamada karar desteği amacıyla kullanılabilir.",
     "Değişken genel üretim giderleri fiili kullanım düzeyine göre dağıtılır."],
    "TMS 2 md. 12-13’e göre sabit GÜG normal kapasite esas alınarak stok maliyetine dahil edilir; değişken "
    "maliyetleme sabit GÜG’ü stoka almadığından finansal raporlamada doğrudan kullanılamaz. İç raporlamada ise "
    "karar desteği için uygundur.", zorluk="hard")

P.q(BA,
    "Bir işletmenin yönetim muhasebesi eğitiminde katılımcılardan katkı payı kavramıyla ilgili ifadeleri "
    "değerlendirmeleri istenmiştir. İfadelerden biri kavramı brüt satış kârıyla karıştırmaktadır.\n\nKatkı payıyla "
    "ilgili aşağıdakilerden hangisi yanlıştır?",
    "Satışlardan satılan malın tam maliyeti düşülerek bulunur.",
    ["Birim katkı payı fiyattan birim değişken maliyet düşülerek bulunur.",
     "Toplam katkı payı önce sabit maliyetleri karşılar, kalanı kârı oluşturur.",
     "Katkı payı oranı ile değişken maliyet oranının toplamı %100’dür.",
     "Başabaş noktasının üstünde her birim, katkı payı kadar kâr sağlar."],
    "Katkı payı satışlardan tüm değişken maliyetlerin (üretim ve üretim dışı) düşülmesiyle bulunur. Satılan malın "
    "tam maliyeti sabit GÜG’ü de içerdiğinden bu işlem brüt satış kârını verir.")

P.q(BA,
    "Bir toptancı, belirli miktarın üzerinde alım yapan müşterilerine kademeli iskonto uygulamaktadır; sipariş "
    "büyüdükçe birim satış fiyatı düşmektedir. Yönetim buna rağmen başabaş hesabını tek bir fiyatla doğrusal MHK "
    "modeline göre yapmıştır.\n\nBu uygulama doğrusal MHK modelinin hangi varsayımını ihlal eder?",
    "Birim satış fiyatının sabit olduğu varsayımını",
    ["Satış karmasının sabit olduğu varsayımını",
     "Maliyetlerin sabit ve değişken ayrılabildiği varsayımını",
     "Üretim ve satış miktarının eşit olduğu varsayımını",
     "Birim değişken maliyetin sabit olduğu varsayımını"],
    "Doğrusal modelde birim satış fiyatı geçerli aralıkta sabittir. Hacim arttıkça iskonto nedeniyle fiyatın düşmesi "
    "hasılat doğrusunu eğriye dönüştürür ve doğrusal başabaş hesabını yanıltır.")

P.q(BA,
    "Bir işletmenin yönetimi, gelecek yıl başabaş satış miktarını düşürmek için alınabilecek önlemleri "
    "tartışmaktadır. Her önlem tek başına ve diğer koşullar sabitken değerlendirilecektir.\n\nAşağıdakilerden "
    "hangisi başabaş satış miktarını düşürmez?",
    "Fabrika kira sözleşmesinin daha yüksek bedelle yenilenmesi",
    ["Satış fiyatının rakiplerle uyumlu biçimde artırılması",
     "Hammadde tedarikçisinden daha düşük fiyat alınması",
     "Sabit yönetim giderlerinde tasarrufa gidilmesi",
     "Bayilere ödenen satış komisyonu oranının düşürülmesi"],
    "Başabaş miktarı = sabit maliyet ÷ birim katkı. Kira artışı sabit maliyeti yükselttiği için başabaşı artırır. Fiyat "
    "artışı, değişken maliyet ve komisyon indirimi birim katkıyı yükseltir; sabit gider tasarrufu payı küçültür.")

P.sayisal(DM,
    "Bir işletmenin bir birim mamul için maliyetleri şöyledir: direkt ilk madde ve malzeme 40 ₺, direkt işçilik 25 ₺, "
    "değişken GÜG 15 ₺, normal kapasiteye göre sabit GÜG 20 ₺ ve değişken pazarlama gideri 10 ₺.\n\nDeğişken "
    "maliyetleme yöntemine göre bir birim mamul stokunun maliyeti kaç ₺’dir?",
    tl(40 + 25 + 15), secenekler(80, 100, 90, 110, 65),
    "Değişken maliyetlemede stok maliyeti değişken üretim maliyetlerinden oluşur: 40 + 25 + 15 = 80 ₺. Sabit GÜG "
    "dönem gideri yazılır; değişken pazarlama gideri üretim maliyeti olmadığından stoka girmez.", zorluk="easy")

kar = 8_000 * (150 - 80 - 10) - 240_000 - 160_000
P.sayisal(DM,
    "Bir işletme dönem içinde ürettiği 8.000 birimin tamamını birim 150 ₺’den satmıştır. Birim değişken üretim "
    "maliyeti 80 ₺, birim değişken satış gideri 10 ₺’dir. Sabit genel üretim giderleri 240.000 ₺, sabit yönetim "
    "giderleri 160.000 ₺’dir.\n\nDeğişken maliyetleme yöntemine göre faaliyet kârı kaç ₺’dir?",
    tl(kar), secenekler(kar, 480_000, 240_000, 160_000, 320_000),
    "Katkı payı = 8.000 × (150 − 80 − 10) = 480.000 ₺. Faaliyet kârı = 480.000 − 240.000 − 160.000 = 80.000 ₺. "
    "Üretim ve satış eşit olduğundan tam maliyetleme de aynı kârı verir.")

P.q(GK,
    "Bir işletme gelecek yılın planında satışların başabaş noktasının çok az üzerinde gerçekleşeceğini "
    "öngörmektedir. Finans müdürü, bu durumda satışlardaki küçük bir değişimin kârı nasıl etkileyeceğini "
    "açıklamaktadır.\n\nSatışların başabaş noktasına yakın olmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Faaliyet kaldıracı derecesi yüksektir; küçük satış değişimi kârı büyük oranda değiştirir.",
    ["Faaliyet kaldıracı derecesi düşüktür; satış değişimleri kârı az etkiler.",
     "Güvenlik payı oranı yüksektir; zarar riski azdır.",
     "Katkı payı sıfıra yaklaştığından kâr satıştan bağımsız hâle gelir.",
     "Faaliyet kaldıracı derecesi 1’e yaklaşır; kâr satışla aynı oranda değişir."],
    "Başabaş noktasına yakın satışta kâr küçük, katkı payı ise büyüktür; bu nedenle faaliyet kaldıracı derecesi "
    "(katkı ÷ kâr) yüksek olur ve güvenlik payı dardır. Satışlardaki küçük değişimler kârı büyük oranda etkiler.")

kar = 13_500 * (95 - 57) - 418_000
P.sayisal(BA,
    "Bir işletmenin ürününün satış fiyatı 95 ₺, birim değişken maliyeti 57 ₺ ve yıllık sabit maliyeti 418.000 "
    "₺’dir. Satış birimi gelecek yıl 13.500 birim satış yapılacağını öngörmekte; fiyat ve maliyetlerin geçerli "
    "aralıkta değişmeyeceği varsayılmaktadır.\n\nBu satış düzeyinde beklenen faaliyet kârı kaç ₺’dir?",
    tl(kar), secenekler(kar, 513_000, 418_000, 76_000, 133_000),
    "Toplam katkı payı = 13.500 × (95 − 57) = 513.000 ₺. Faaliyet kârı = 513.000 − 418.000 = 95.000 ₺. Başabaş "
    "miktarı 11.000 birim olduğundan başabaşı aşan 2.500 birimin katkısı kârı oluşturur.", zorluk="easy")

P.q(CU,
    "Bir işletme A ve B ürünlerini satmaktadır. Ortak sabit maliyetler satış hasılatı oranında dağıtıldığında B "
    "ürünü 40.000 ₺ zararlı görünmektedir; oysa B’nin toplam katkı payı 110.000 ₺’dir. Ortak sabit maliyetler B "
    "üretimi durdurulsa da aynı kalacaktır.\n\nB ürününün üretiminin durdurulmasıyla ilgili aşağıdakilerden "
    "hangisi doğrudur?",
    "İşletmenin toplam kârı 110.000 ₺ azalır.",
    ["İşletmenin toplam kârı 40.000 ₺ artar.",
     "İşletmenin toplam kârı 70.000 ₺ artar.",
     "İşletmenin toplam kârı 150.000 ₺ azalır.",
     "Ortak sabit maliyetler ortadan kalktığından kâr değişmez."],
    "Ortak sabit maliyetler kaçınılamaz olduğundan B durdurulunca yalnızca katkı payı kaybedilir; toplam kâr 110.000 "
    "₺ azalır. Dağıtılmış sabit maliyetlerle hesaplanan ürün zararı karar için yanıltıcıdır.", zorluk="hard")

P.serpistir()

if __name__ == "__main__":
    sys.exit(P.yaz())
