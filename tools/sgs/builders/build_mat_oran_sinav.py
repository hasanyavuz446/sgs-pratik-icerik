#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS Matematik — Oran-Orantı, Yüzde ve Problemler (gerçek sınav derinliğinde).

Kalibrasyon (2021-2026, 16 kitapçık): problem soruları her sınavda 1-2 adet ve
çok adımlıdır (iki kişinin parası arasında yüzde ilişkisi, orantılı paylaştırma,
günlere bölünmüş okuma planı, ardışık indirim). Eski paketteki tek işlemli
sorular ('200'ün %15'i') baştan değiştirildi; soru kimlikleri korundu.
Sayılar ve kurgu özgündür; çıkmış sorulardan alınmamıştır.

Her sonuç builder'dan bağımsız olarak sympy/kesirli aritmetikle doğrulanır.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mat_common import main, make_q

Q: list[dict] = []
q = make_q(Q)
R = sp.Rational
x = sp.symbols("x")
def coz(denklem):
    s = sp.solve(denklem, x)
    assert len(s) == 1, s
    return s[0]

# ══ Oran-orantı ve paylaştırma (8) ══════════════════════════════════════════
q("Bir miras, üç kardeş arasında yaşlarıyla doğru orantılı olarak paylaştırılacaktır. Kardeşlerin yaşları 12, 15 ve 18'dir. En büyük kardeş 2.700 ₺ aldığına göre mirasın tamamı kaç ₺'dir?",
  "6.750", ["7.500", "7.200", "4.500", "8.100"],
  "Paylar 12k, 15k, 18k'dir. 18k = 2.700 → k = 150. Toplam 45k = 6.750 ₺.",
  verify=(45 * R(2700, 18), 6750))
q("Bir ödül, üç yarışmacı arasında bitirme süreleri olan 2, 3 ve 6 saatle ters orantılı olarak paylaştırılacaktır. Ödül 42.000 ₺ olduğuna göre en hızlı yarışmacı kaç ₺ alır?",
  "21.000", ["14.000", "7.000", "12.000", "18.000"],
  "Ters orantıda paylar 1/2, 1/3, 1/6 ile orantılıdır; paydalar eşitlenince 3 : 2 : 1 olur. En hızlı (2 saat) olanın payı 42.000 · 3/6 = 21.000 ₺.",
  verify=(42000 * R(1, 2) / (R(1, 2) + R(1, 3) + R(1, 6)), 21000))
q("a/3 = b/4 = c/5 ve a + b + c = 48 olduğuna göre b kaçtır?",
  "16", ["12", "20", "24", "17"],
  "Ortak oran k olsun: a = 3k, b = 4k, c = 5k. 12k = 48 → k = 4. b = 16.",
  verify=(4 * R(48, 12), 16))
q("a/b = 2/3, b/c = 4/5 ve c − a = 14 olduğuna göre b kaçtır?",
  "24", ["16", "30", "12", "20"],
  "b'nin ortak katı 12 alınır: a : b = 8 : 12 ve b : c = 12 : 15. c − a = 7k = 14 → k = 2. b = 12 · 2 = 24.",
  verify=(12 * R(14, 15 - 8), 24))
q("x ile y ters orantılıdır. x = 6 iken y = 10 olduğuna göre x = 15 iken y kaçtır?",
  "4", ["25", "6", "9", "5"],
  "Ters orantıda çarpım sabittir: x·y = 60. x = 15 için y = 60/15 = 4.",
  verify=(R(6 * 10, 15), 4))
q("Bir işletme kârını, ortakların sermayeleri ve çalıştıkları ay sayısıyla doğru orantılı paylaştırmaktadır. A ortağı 40.000 ₺ ile 6 ay, B ortağı 30.000 ₺ ile 12 ay çalışmıştır. Toplam kâr 75.000 ₺ olduğuna göre B'nin payı kaç ₺'dir?",
  "45.000", ["30.000", "37.500", "40.000", "50.000"],
  "Paylar sermaye × süre ile orantılıdır: A 240.000, B 360.000 → 2 : 3. B'nin payı 75.000 · 3/5 = 45.000 ₺.",
  verify=(75000 * R(30000 * 12, 40000 * 6 + 30000 * 12), 45000))
q("1 : 250.000 ölçekli bir haritada iki kent arasındaki uzaklık 6 cm'dir. Bu iki kent arasındaki gerçek uzaklık kaç km'dir?",
  "15", ["150", "1,5", "25", "60"],
  "Gerçek uzaklık 6 · 250.000 = 1.500.000 cm'dir. 1 km = 100.000 cm olduğundan 15 km.",
  verify=(R(6 * 250000, 100000), 15))
q("Bir sınıfta kız öğrenci sayısının erkek öğrenci sayısına oranı 3/5'tir. Sınıfa 4 kız öğrenci katıldığında kızların sayısı erkeklerin sayısına eşit oluyor. Başlangıçta sınıfta kaç öğrenci vardı?",
  "16", ["20", "24", "28", "8"],
  "Kızlar 3k, erkekler 5k. 3k + 4 = 5k → k = 2. Başlangıçta 6 + 10 = 16 öğrenci vardı.",
  verify=(8 * coz(3*x + 4 - 5*x), 16))

# ══ Yüzde ilişkileri (8) ════════════════════════════════════════════════════
q("Ayşe'nin parasının %25 eksiği, Can'ın parasının %50 fazlasına eşittir. İkisinin toplam parası 900 ₺ olduğuna göre Ayşe'nin parası kaç ₺'dir?",
  "600", ["300", "450", "500", "675"],
  "0,75A = 1,5C → A = 2C. A + C = 3C = 900 → C = 300, A = 600 ₺.",
  verify=(2 * R(900, 3), 600))
q("Bir mağaza tanesi 400 ₺'ye aldığı 50 gömleği %50 kârla etiketleyip 30'unu etiket fiyatından satmıştır. Kalan gömleklerin yarısını etiket fiyatı üzerinden %20 indirimle, geri kalanını ise bu indirimli fiyat üzerinden ayrıca %25 indirimle satmıştır. Buna göre mağazanın bu gömleklerden elde ettiği toplam kâr kaç ₺'dir?",
  "6.400", ["7.600", "10.000", "6.100", "26.400"],
  "Etiket fiyatı 400 · 1,5 = 600 ₺. Gelir: 30 · 600 = 18.000; 10 · 480 = 4.800; 10 · 360 = 3.600 → 26.400 ₺. Maliyet 50 · 400 = 20.000 ₺; kâr 6.400 ₺. İkinci indirim etiket fiyatına değil indirimli fiyata uygulanır.",
  verify=(30 * 600 + 10 * 600 * R(4, 5) + 10 * 600 * R(4, 5) * R(3, 4) - 50 * 400, 6400))
q("Bir ürünün fiyatı önce %20 artırılmış, ardından yeni fiyat üzerinden %20 indirim yapılmıştır. Ürünün son fiyatı ilk fiyatına göre nasıl değişmiştir?",
  "%4 azalmıştır", ["Değişmemiştir", "%4 artmıştır", "%2 azalmıştır", "%40 azalmıştır"],
  "İlk fiyat 100 alınırsa 120'ye çıkar, sonra %20 indirimle 96 olur. Son fiyat ilk fiyattan %4 azdır.",
  verify=(100 * R(12, 10) * R(8, 10), 96))
q("Bir okulda öğrencilerin %40'ı kızdır. Kızların %25'i, erkeklerin %10'u gözlük kullanmaktadır. Okuldaki öğrencilerin yüzde kaçı gözlük kullanmaktadır?",
  "16", ["35", "17,5", "14", "20"],
  "100 öğrencide 40 kızın 10'u, 60 erkeğin 6'sı gözlüklüdür. Toplam 16 kişi, yani %16.",
  verify=(40 * R(25, 100) + 60 * R(10, 100), 16))
q("a sayısı b sayısından %25 fazladır. Buna göre b sayısı a sayısından yüzde kaç azdır?",
  "20", ["25", "75", "80", "15"],
  "a = 1,25b → b = a/1,25 = 0,8a. b, a'dan %20 azdır.",
  verify=(100 - 100 / R(125, 100), 20))
q("Bir kentin nüfusu iki yıl üst üste %10 artarak 72.600 olmuştur. Kentin iki yıl önceki nüfusu kaçtır?",
  "60.000", ["58.080", "60.500", "66.000", "60.600"],
  "İki yıllık çarpan 1,1 · 1,1 = 1,21'dir. 72.600 / 1,21 = 60.000.",
  verify=(R(72600) / R(121, 100), 60000))
q("Bir üniversitede bir dersin başarı notu, iki ara sınavın aritmetik ortalamasının %60'ı ile dönem projesi notunun %40'ı toplanarak hesaplanmaktadır. Başarı notu 76 ve üzeri olan öğrenciler bir üst seviyedeki derse doğrudan kayıt yaptırabilmektedir. Ara sınavlardan 64 ve 80 alan bir öğrencinin bu hakkı kazanabilmesi için projeden en az kaç alması gerekir?",
  "82", ["76", "79", "88", "85"],
  "Ara sınav ortalaması (64 + 80) / 2 = 72; katkısı 72 · 0,60 = 43,2. Kalan 76 − 43,2 = 32,8 puan projeden gelmeli: proje · 0,40 ≥ 32,8 → proje ≥ 82.",
  verify=((76 - R(64 + 80, 2) * R(3, 5)) / R(2, 5), 82))
q("Boş bırakılan sorunun olmadığı 60 soruluk bir sınavda bir öğrencinin doğru sayısı, yanlış sayısının %150'si kadardır. Öğrencinin doğru sayısı kaçtır?",
  "36", ["48", "40", "42", "45"],
  "D = 1,5Y ve D + Y = 60 → 2,5Y = 60 → Y = 24, D = 36.",
  verify=(R(3, 2) * coz(R(5, 2) * x - 60), 36))

# ══ Kâr-zarar ve indirim (10) ═══════════════════════════════════════════════
q("Maliyeti 800 ₺ olan bir ürünün etiket fiyatı %25 kârla belirlenmiş, ardından etiket fiyatı üzerinden %20 indirim yapılarak satılmıştır. Bu satışın sonucu aşağıdakilerden hangisidir?",
  "Ne kâr ne zarar edilmiştir", ["40 ₺ kâr edilmiştir", "40 ₺ zarar edilmiştir", "200 ₺ kâr edilmiştir", "160 ₺ zarar edilmiştir"],
  "Etiket fiyatı 800 · 1,25 = 1.000 ₺. %20 indirimle satış fiyatı 800 ₺ olur; bu maliyete eşittir.",
  verify=(800 * R(125, 100) * R(8, 10) - 800, 0))
q("Bir elektronik mağazası, KDV hariç maliyeti 2.000 ₺ olan bir ürünün KDV hariç satış fiyatını %40 kârla belirlemekte ve bu fiyata %20 KDV eklemektedir. Kampanya döneminde ürün, KDV dâhil fiyat üzerinden %25 indirimle satılmıştır. Buna göre indirimli satışta mağazanın KDV hariç kâr oranı yüzde kaçtır?",
  "5", ["15", "26", "20", "10"],
  "KDV hariç fiyat 2.800 ₺, KDV dâhil 3.360 ₺. İndirimli KDV dâhil fiyat 3.360 · 0,75 = 2.520 ₺; KDV hariç 2.520 / 1,2 = 2.100 ₺. Kâr 100 ₺ → 100 / 2.000 = %5. KDV dâhil tutarla hesaplamak %26 verir.",
  verify=((2000 * R(7, 5) * R(6, 5) * R(3, 4) / R(6, 5) - 2000) * 100 / 2000, 5))
q("Bir mağaza etiket fiyatı üzerinden önce %20, ardından kalan fiyat üzerinden %10 indirim yapmaktadır. Toplam indirim oranı yüzde kaçtır?",
  "28", ["26", "25", "24", "18"],
  "100 ₺'lik ürün önce 80 ₺'ye, sonra 72 ₺'ye iner. Toplam indirim 28 ₺, yani %28.",
  verify=(100 - 100 * R(8, 10) * R(9, 10), 28))
q("%40 kârla 1.400 ₺'ye satılan bir ürünün maliyeti %10 artmıştır. Aynı kâr oranıyla satılabilmesi için yeni satış fiyatı kaç ₺ olmalıdır?",
  "1.540", ["1.440", "1.500", "1.554", "1.400"],
  "Maliyet 1.400 / 1,4 = 1.000 ₺. Yeni maliyet 1.100 ₺; %40 kârla satış 1.100 · 1,4 = 1.540 ₺.",
  verify=(R(1400) / R(14, 10) * R(11, 10) * R(14, 10), 1540))
q("Bir tüccar tanesi 12 ₺'den aldığı 300 kalemin 200'ünü tanesi 15 ₺'den satmıştır. Toplamda %20 kâr edebilmesi için kalan kalemlerin tanesini kaç ₺'den satması gerekir?",
  "13,20", ["14,40", "15,40", "15,00", "13,40"],
  "Toplam maliyet 3.600 ₺, hedef gelir 4.320 ₺. 200 kalemden 3.000 ₺ elde edildi; kalan 100 kalemden 1.320 ₺ gerekir: tanesi 13,20 ₺.",
  verify=(R(3600 * R(12, 10) - 200 * 15, 100), R(1320, 100)))
q("Bir ürünün fiyatına %25 zam yapılmıştır. Fiyatın eski düzeyine inmesi için yeni fiyat üzerinden yüzde kaç indirim yapılmalıdır?",
  "20", ["25", "26", "30", "22"],
  "100 ₺ zamla 125 ₺ olur. 125 ₺'den 25 ₺ indirim gerekir: 25/125 = %20.",
  verify=(R(25, 125) * 100, 20))
q("Bir satıcı elindeki malların 1/3'ünü %30 kârla, kalanını %12 zararla satmıştır. Satıcının bu satışlardan toplam kâr ya da zarar oranı aşağıdakilerden hangisidir?",
  "%2 kâr", ["%18 kâr", "%2 zarar", "%9 kâr", "%6 kâr"],
  "Toplam maliyet 300 alınırsa 100'lük kısım 130'a, 200'lük kısım 176'ya satılır. Gelir 306; kâr 6/300 = %2.",
  verify=(100 * R(13, 10) + 200 * R(88, 100) - 300, 6))
q("Üç arkadaş bir iş kurmak için sırasıyla 120.000 ₺, 180.000 ₺ ve 200.000 ₺ sermaye koymuştur. Yıl sonunda elde edilen kârın %20'si işletmede yedek olarak bırakılmış, kalan kısım sermayelerle doğru orantılı olarak paylaştırılmıştır. En fazla sermaye koyan arkadaşın payına 96.000 ₺ düştüğüne göre işletmenin yıl sonu kârı kaç ₺'dir?",
  "300.000", ["240.000", "288.000", "250.000", "360.000"],
  "Sermayeler 6 : 9 : 10 oranındadır. 10 pay = 96.000 → 1 pay = 9.600 ₺; dağıtılan kâr 25 · 9.600 = 240.000 ₺. Bu tutar kârın %80'idir: kâr = 240.000 / 0,8 = 300.000 ₺.",
  verify=(96000 * R(25, 10) / R(4, 5), 300000))
q("Bir kütüphanedeki kitapların %60'ı roman, kalanı bilim kitabıdır. Kütüphaneye 120 yeni kitap eklenmiş ve bunların 1/3'ü roman olmuştur. Son durumda romanların tüm kitaplar içindeki oranı %55'e düştüğüne göre kütüphanede başlangıçta kaç kitap vardı?",
  "520", ["640", "480", "600", "400"],
  "Başlangıç N olsun: 0,6N + 40 = 0,55(N + 120) → 0,05N = 26 → N = 520. Son durumdaki toplam (640) sorulmamaktadır.",
  verify=(coz(R(3, 5) * x + 40 - R(11, 20) * (x + 120)), 520))
q("Bir satıcı etiket fiyatını maliyetin %50 fazlası olarak belirlemekte ve etiket fiyatı üzerinden %20 indirim yapmaktadır. Satıcının kâr oranı yüzde kaçtır?",
  "20", ["30", "25", "10", "70"],
  "Maliyet 100 ise etiket 150, indirimli satış 120 olur. Kâr 20, oranı %20.",
  verify=(100 * R(15, 10) * R(8, 10) - 100, 20))

# ══ Karışım (6) ═════════════════════════════════════════════════════════════
q("Bir gıda fabrikasında turşu suyu hazırlamak için tuz oranı %20 olan 60 kg tuzlu su kaynatılarak 20 kg'ı buharlaştırılıyor. Soğuyan karışıma, tuz oranı %5 olan 40 kg hafif tuzlu su ekleniyor. Buna göre son karışımın tuz oranı yüzde kaçtır?",
  "17,5", ["14", "30", "12,5", "22,5"],
  "Tuz miktarı 60 · 0,20 = 12 kg; buharlaşmada tuz kaybolmaz, karışım 40 kg olur. Eklenen suda 40 · 0,05 = 2 kg tuz vardır. Son karışım 80 kg, tuz 14 kg → 14 / 80 = %17,5.",
  verify=(R(60 * 20, 100) + R(40 * 5, 100), R(175, 1000) * 80))
q("Şeker oranı %30 olan 60 litre şerbetten kaç litre su buharlaştırılırsa şeker oranı %45 olur?",
  "20", ["35", "30", "25", "40"],
  "Şeker 18 litredir. 18/(60 − x) = 0,45 → 60 − x = 40 → x = 20.",
  verify=(coz(18 - R(45, 100) * (60 - x)), 20))
q("Alkol oranı %40 olan 30 litre karışım ile alkol oranı %10 olan kaç litre karışım birleştirilirse yeni karışımın alkol oranı %25 olur?",
  "30", ["40", "45", "50", "60"],
  "12 + 0,1x = 0,25(30 + x) → 12 + 0,1x = 7,5 + 0,25x → 0,15x = 4,5 → x = 30.",
  verify=(coz(12 + R(1, 10) * x - R(1, 4) * (30 + x)), 30))
q("Kilogramı 80 ₺ olan çaydan 30 kg ile kilogramı 120 ₺ olan çaydan 20 kg karıştırılıyor. Karışımın kilogramı kaç ₺'dir?",
  "96", ["100", "102", "104", "112"],
  "Toplam tutar 2.400 + 2.400 = 4.800 ₺, toplam 50 kg. Kilogram fiyatı 4.800 / 50 = 96 ₺.",
  verify=(R(30 * 80 + 20 * 120, 50), 96))
q("Boş bir havuzu A musluğu 10 saatte, B musluğu 15 saatte doldurmaktadır. İki musluk birlikte 4 saat açık kaldıktan sonra A musluğu arızalanıp kapanmış ve aynı anda dolu havuzu 30 saatte boşaltan C vanası açılmıştır. Havuzun tamamen dolması için B ve C birlikte kaç saat daha açık kalmalıdır?",
  "10", ["5", "8", "12", "15"],
  "A ve B birlikte saatte 1/10 + 1/15 = 1/6 doldurur; 4 saatte havuzun 2/3'ü dolar. Kalan 1/3 için B ve C'nin net hızı 1/15 − 1/30 = 1/30'dur: (1/3) / (1/30) = 10 saat.",
  verify=((1 - 4 * (R(1, 10) + R(1, 15))) / (R(1, 15) - R(1, 30)), 10))
q("Süt ve sudan oluşan 50 litrelik bir karışımda süt miktarının su miktarına oranı 3/2'dir. Karışıma kaç litre su eklenirse süt ile su miktarı eşit olur?",
  "10", ["5", "15", "20", "30"],
  "Süt 30, su 20 litredir. Su 30 litreye çıkmalıdır: 10 litre eklenir.",
  verify=(50 * R(3, 5) - 50 * R(2, 5), 10))

# ══ İşçi-havuz (6) ══════════════════════════════════════════════════════════
q("A bir işi 12 günde, B aynı işi 18 günde bitirmektedir. İkisi birlikte 4 gün çalıştıktan sonra A işten ayrılıyor. Kalan işi B kaç günde bitirir?",
  "8", ["6", "10", "4", "12"],
  "Birlikte günlük iş 1/12 + 1/18 = 5/36. 4 günde 20/36 = 5/9 biter, 4/9 kalır. B bunu (4/9) · 18 = 8 günde bitirir.",
  verify=((1 - 4 * (R(1, 12) + R(1, 18))) * 18, 8))
q("Bir havuzu A musluğu 6 saatte, B musluğu 9 saatte doldurmaktadır. C musluğu ise dolu havuzu 18 saatte boşaltmaktadır. Üç musluk birlikte açılırsa boş havuz kaç saatte dolar?",
  "4,5", ["3,6", "5", "6", "4"],
  "Saatlik dolum 1/6 + 1/9 − 1/18 = 4/18 = 2/9. Havuz 9/2 = 4,5 saatte dolar.",
  verify=(1 / (R(1, 6) + R(1, 9) - R(1, 18)), R(9, 2)))
q("4 işçi günde 6 saat çalışarak bir işi 15 günde bitirmektedir. 5 işçi günde 8 saat çalışarak aynı işi kaç günde bitirir?",
  "9", ["10", "12", "8", "7,5"],
  "İş miktarı 4 · 6 · 15 = 360 işçi-saattir. 5 · 8 = 40 işçi-saat/gün ile 360/40 = 9 gün.",
  verify=(R(4 * 6 * 15, 5 * 8), 9))
q("Bir işi Ali tek başına 10 günde, Ali ile Can birlikte 6 günde bitirmektedir. Can bu işi tek başına kaç günde bitirir?",
  "15", ["4", "16", "8", "12"],
  "Can'ın günlük işi 1/6 − 1/10 = 1/15'tir; işi 15 günde bitirir.",
  verify=(1 / (R(1, 6) - R(1, 10)), 15))
q("Bir boyacı bir evi tek başına 8 günde boyamaktadır. İşe başladıktan 2 gün sonra yanına aynı hızda çalışan ikinci bir boyacı katılıyor. Ev toplam kaç günde boyanır?",
  "5", ["2", "4", "3", "1"],
  "2 günde işin 1/4'ü biter, 3/4 kalır. İki boyacı günde 2/8 = 1/4 iş yapar; kalan 3 günde biter. Toplam 5 gün.",
  verify=(2 + (1 - R(2, 8)) / R(2, 8), 5))
q("Bir fabrikada 6 makine 10 saatte 1.200 parça üretmektedir. Aynı tür 8 makine 2.000 parçayı kaç saatte üretir?",
  "12,5", ["9", "10", "12", "11,5"],
  "Bir makine saatte 1.200 / 60 = 20 parça üretir. 8 makine saatte 160 parça; 2.000 / 160 = 12,5 saat.",
  verify=(R(2000, 8 * R(1200, 60)), R(25, 2)))

# ══ Hız (6) ═════════════════════════════════════════════════════════════════
q("Aralarında 360 km bulunan iki kentten iki araç aynı anda birbirine doğru hareket ediyor. Araçların saatlik hızları 70 km ve 50 km olduğuna göre kaç saat sonra karşılaşırlar?",
  "3", ["6", "2", "4", "5"],
  "Yaklaşma hızı 70 + 50 = 120 km/sa. 360 / 120 = 3 saat.",
  verify=(R(360, 120), 3))
q("Bir araç A kentinden B kentine saatte 80 km hızla 3 saatte gidiyor ve saatte 60 km hızla geri dönüyor. Gidiş-dönüşteki ortalama hızı saatte kaç km'dir?",
  "480/7", ["70", "68", "72", "65"],
  "Tek yön 240 km. Dönüş 240/60 = 4 saat sürer. Toplam yol 480 km, toplam süre 7 saat; ortalama hız 480/7 km/sa.",
  verify=(R(480, 3 + R(240, 60)), R(480, 7)))
q("Bir koşucu bir parkuru saatte 12 km hızla 25 dakikada koşmaktadır. Aynı parkuru 20 dakikada koşabilmesi için saatteki hızı kaç km olmalıdır?",
  "15", ["17", "16", "18", "19"],
  "Parkur 12 · 25/60 = 5 km'dir. 20 dakikada (1/3 saat) koşmak için hız 5 / (1/3) = 15 km/sa olmalıdır.",
  verify=(R(12 * 25, 60) / R(20, 60), 15))
q("Saatteki hızı 72 km olan bir tren, 600 m uzunluğundaki bir tüneli 40 saniyede tamamen geçmektedir. Trenin uzunluğu kaç metredir?",
  "200", ["800", "400", "240", "300"],
  "72 km/sa = 20 m/sn. 40 saniyede 800 m yol alınır; bu, tünel ile trenin uzunlukları toplamıdır. Tren 800 − 600 = 200 m.",
  verify=(R(72000, 3600) * 40 - 600, 200))
q("Akıntı hızının saatte 3 km olduğu bir nehirde bir kayık, akıntı yönünde 45 km'yi 3 saatte almaktadır. Kayık aynı yolu akıntıya karşı kaç saatte alır?",
  "5", ["4", "2", "3", "2,5"],
  "Akıntı yönündeki hız 15 km/sa → kayığın durgun sudaki hızı 12 km/sa. Akıntıya karşı hız 9 km/sa; 45/9 = 5 saat.",
  verify=(R(45, (R(45, 3) - 3) - 3), 5))
q("Aralarında 510 km bulunan A ve B kentlerinden, saat 08.00'de A'dan saatte 60 km hızla bir otobüs, saat 09.00'da B'den saatte 90 km hızla bir otomobil birbirine doğru yola çıkıyor. Otomobil karşılaşmadan önce yolda 30 dakika mola veriyor. Otobüs hiç durmadığına göre iki araç saat kaçta karşılaşır?",
  "12.18", ["12.00", "11.24", "12.30", "12.48"],
  "Saat 09.00'a kadar otobüs 60 km yol alır, aradaki uzaklık 450 km kalır. Otomobil t saatin yarım saatinde durur: 60t + 90(t − 0,5) = 450 → 150t = 495 → t = 3,3 saat = 3 saat 18 dakika. Karşılaşma 09.00 + 3.18 = 12.18'dedir.",
  verify=(coz(60 * x + 90 * (x - R(1, 2)) - 450) * 60, 198))

# ══ Yaş (4) ═════════════════════════════════════════════════════════════════
q("Bir annenin yaşı kızının yaşının 4 katıdır. 6 yıl sonra annenin yaşı kızının yaşının 2,5 katı olacaktır. Annenin bugünkü yaşı kaçtır?",
  "24", ["30", "36", "28", "32"],
  "Kız k, anne 4k yaşında. 4k + 6 = 2,5(k + 6) → 1,5k = 9 → k = 6. Anne 24 yaşındadır.",
  verify=(4 * coz(4*x + 6 - R(5, 2) * (x + 6)), 24))
q("İki kardeşin bugünkü yaşları toplamı 31'dir. 5 yıl önce büyük kardeşin yaşı küçük kardeşin yaşının 2 katıydı. Büyük kardeş bugün kaç yaşındadır?",
  "19", ["12", "16", "17", "15"],
  "Küçük K, büyük 31 − K. 26 − K = 2(K − 5) → 3K = 36 → K = 12. Büyük kardeş 19 yaşındadır.",
  verify=(31 - coz(31 - x - 5 - 2 * (x - 5)), 19))
q("Bir babanın yaşı iki çocuğunun yaşları toplamının 2 katıdır. 10 yıl sonra babanın yaşı, çocuklarının yaşları toplamından 6 fazla olacaktır. Babanın bugünkü yaşı kaçtır?",
  "32", ["28", "26", "24", "30"],
  "Çocukların yaş toplamı S, baba 2S. 10 yıl sonra baba 2S + 10, çocukların toplamı S + 20 olur. 2S + 10 = S + 26 → S = 16, baba 32 yaşındadır.",
  verify=(2 * coz(2*x + 10 - (x + 20 + 6)), 32))
q("Ali'nin bugünkü yaşı, Veli'nin 3 yıl önceki yaşına eşittir. İkisinin yaşları toplamı 47 olduğuna göre Veli kaç yaşındadır?",
  "25", ["29", "27", "26", "28"],
  "A = V − 3 ve A + V = 47 → 2V − 3 = 47 → V = 25.",
  verify=(coz(2*x - 3 - 47), 25))

# ══ Faiz ve ortalama (6) ════════════════════════════════════════════════════
q("Bir kişi birikiminin 2/5'ini yıllık %30 basit faizle bir bankaya, kalanını yıllık %20 basit faizle başka bir bankaya yatırmıştır. 9 ayın sonunda iki hesaptan toplam 12.600 ₺ faiz aldığına göre kişinin toplam birikimi kaç ₺'dir?",
  "70.000", ["52.500", "63.000", "84.000", "56.000"],
  "Yıllık ağırlıklı faiz 0,4 · 0,30 + 0,6 · 0,20 = 0,24; 9 ayda 0,24 · 9/12 = 0,18. Birikim 12.600 / 0,18 = 70.000 ₺. Süreyi bir yıl almak 52.500 ₺ verir.",
  verify=(coz(x * (R(2, 5) * R(3, 10) + R(3, 5) * R(1, 5)) * R(9, 12) - 12600), 70000))
q("Yıllık %30 basit faiz uygulanan bir hesaba yatırılan para 2 yılda 9.000 ₺ faiz getirmiştir. Yatırılan para kaç ₺'dir?",
  "15.000", ["13.500", "18.000", "30.000", "12.000"],
  "Faiz = A · 0,30 · 2 = 0,6A = 9.000 → A = 15.000 ₺.",
  verify=(coz(R(6, 10) * x - 9000), 15000))
q("Bir sınıftaki 18 öğrencinin not ortalaması 62'dir. Sınıfa notları 82 ve 92 olan iki öğrenci katılırsa sınıfın not ortalaması kaç olur?",
  "64,5", ["65", "63", "66", "64"],
  "Toplam not 18 · 62 = 1.116; yeni toplam 1.116 + 174 = 1.290. 20 öğrenciyle ortalama 64,5.",
  verify=(R(18 * 62 + 82 + 92, 20), R(129, 2)))
q("Beş sayının aritmetik ortalaması 24'tür. Bu sayılardan biri çıkarıldığında kalan dört sayının ortalaması 22 oluyor. Çıkarılan sayı kaçtır?",
  "32", ["24", "2", "26", "30"],
  "Beş sayının toplamı 120, kalan dördün toplamı 88'dir. Çıkarılan sayı 120 − 88 = 32.",
  verify=(5 * 24 - 4 * 22, 32))
q("Bir çalışan yılın ilk 3 ayında aylık 24.000 ₺, kalan 9 ayında aylık 28.000 ₺ ücret almıştır. Çalışanın bu yıldaki aylık ortalama ücreti kaç ₺'dir?",
  "27.000", ["26.000", "25.000", "27.500", "28.000"],
  "Yıllık toplam 3 · 24.000 + 9 · 28.000 = 324.000 ₺. 12 aya bölününce 27.000 ₺. Basit ortalama (26.000) ayların sayısını dikkate almaz.",
  verify=(R(3 * 24000 + 9 * 28000, 12), 27000))
q("Bir şirketteki 12 çalışanın yaş ortalaması 34'tür. Yaş ortalaması 50 olan 2 çalışan emekli olmuş, yerlerine 3 yeni çalışan alınmıştır. Son durumda şirketteki çalışanların yaş ortalaması 29 olduğuna göre yeni alınan çalışanların yaş ortalaması kaçtır?",
  "23", ["29", "25", "21", "27"],
  "Başlangıç yaş toplamı 12 · 34 = 408; emekli olanlar 100 → 308 (10 kişi). Son durumda 13 · 29 = 377. Yeni gelenlerin yaş toplamı 377 − 308 = 69 → ortalama 23.",
  verify=(R(13 * 29 - (12 * 34 - 2 * 50), 3), 23))

# ══ Kesir problemleri (6) ═══════════════════════════════════════════════════
q("Bir öğrenci 240 sayfalık bir kitabın ilk gün 1/4'ünü, ikinci gün kalanın 1/3'ünü okumuştur. Kitabın okunmayan kısmı kaç sayfadır?",
  "120", ["100", "140", "160", "80"],
  "İlk gün 60 sayfa okunur, 180 kalır. İkinci gün 180'in 1/3'ü olan 60 sayfa okunur; 120 sayfa kalır.",
  verify=(240 * R(3, 4) * R(2, 3), 120))
q("Bir kişi aylık gelirinin 2/5'ini kiraya, kalanın 1/3'ünü mutfak giderlerine ayırıyor. Geriye 12.000 ₺ kaldığına göre aylık geliri kaç ₺'dir?",
  "30.000", ["20.000", "36.000", "24.000", "40.000"],
  "Kiradan sonra gelirin 3/5'i kalır; bunun 2/3'ü geriye kalır: 3/5 · 2/3 = 2/5. Gelirin 2/5'i 12.000 ₺ → gelir 30.000 ₺.",
  verify=(R(12000) / (R(3, 5) * R(2, 3)), 30000))
q("Bir öğrenci harçlığının 1/4'ünü kitaba, kalanın 2/5'ini yemeğe harcamıştır. Ertesi gün annesinden 300 ₺ daha harçlık almış ve elindeki paranın yarısını ulaşım kartına yüklemiştir. Son durumda öğrencinin 690 ₺'si kaldığına göre başlangıçtaki harçlığı kaç ₺'dir?",
  "2.400", ["2.000", "2.760", "3.200", "1.840"],
  "Harcamalardan sonra harçlığın 3/4 · 3/5 = 9/20'si kalır. 300 ₺ eklenip yarısı harcanınca 690 ₺ kaldığına göre öncesinde 1.380 ₺ vardı: (9/20)H + 300 = 1.380 → H = 2.400 ₺.",
  verify=(coz((R(9, 20) * x + 300) / 2 - 690), 2400))
q("Bir sınıftaki öğrencilerin 3/7'si kızdır. Erkek öğrencilerin sayısı kızlarınkinden 6 fazla olduğuna göre sınıfın mevcudu kaçtır?",
  "42", ["36", "48", "35", "28"],
  "Erkekler 4/7, kızlar 3/7'dir; fark mevcudun 1/7'si kadardır. Mevcut 6 · 7 = 42.",
  verify=(coz(R(4, 7) * x - R(3, 7) * x - 6), 42))
q("Bir bidondaki zeytinyağının 1/3'ü satıldıktan sonra kalanın yarısı da satılıyor. Bidonda 20 litre zeytinyağı kaldığına göre başlangıçta kaç litre vardı?",
  "60", ["40", "80", "30", "120"],
  "Satışlardan sonra başlangıcın 2/3 · 1/2 = 1/3'ü kalır. 1/3 = 20 litre → başlangıç 60 litre.",
  verify=(R(20) / (R(2, 3) * R(1, 2)), 60))
q("Bir kırtasiye, defterlerin satış fiyatına %25 zam yaptığında günlük satış adedi %20 azalmıştır. Bir hafta sonra zamlı fiyat üzerinden %10 indirim yapılınca günlük satış adedi zamdan önceki düzeyin %90'ına çıkmıştır. Buna göre son durumda günlük satış geliri, zamdan önceki gelire göre nasıl değişmiştir?",
  "%1,25 artmıştır", ["%12,5 artmıştır", "%1,25 azalmıştır", "Değişmemiştir", "%10 artmıştır"],
  "Son fiyat ilk fiyatın 1,25 · 0,90 = 1,125 katı, satış adedi 0,90 katıdır. Gelir 1,125 · 0,90 = 1,0125 katına çıkar: %1,25 artış.",
  verify=(R(5, 4) * R(9, 10) * R(9, 10), R(10125, 10000)))

assert len(Q) == 60, len(Q)

if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix="mat-oran-gen", ders="matematik", konu="oran_oranti_yuzde_problemler",
        style="SGS Matematik (gerçek sınav 8-15 derinliği)", seed=20261005,
        relative_path="content/matematik/oran_oranti_yuzde_problemler.json", label="Oran-Orantı, Yüzde ve Problemler",
    ))
