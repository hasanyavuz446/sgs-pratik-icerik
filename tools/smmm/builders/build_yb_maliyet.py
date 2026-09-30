# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarındaki Maliyet Muhasebesi ağırlığını izler: maliyet kavramları ve 7/A
hesapları ~5, maliyet unsurları ~4, maliyet sistemleri (safha, sipariş, ortak ve yan ürün) ~5, gider dağıtımı
~2, standart maliyet ~3, üretim kayıpları ~1 ve yönetim muhasebesi ~1; soruların yarısından fazlası tutar veya
tablo taşır. Konu havuzundaki olaylar tekrar edilmez; aynı kural farklı bir olayla ölçülür. Dayanaklar konu
builder'larıyla aynıdır (build_yk_mm_*.py); 30.09.2026 kontrolü.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K

SURUM = "MSUGT Tekdüzen Hesap Planı 7/A-7/B; TMS 2; maliyet ve yönetim muhasebesi esasları; 30.09.2026 kontrolü"
MT, MU, GD, MS, UK, SM = ("maliyet_temelleri", "maliyet_unsurlari", "gider_dagitimlari", "maliyet_sistemleri",
                          "uretim_kayiplari", "standart_maliyet")
YM = "yonetim_muhasebesi"
R = "Maliyet muhasebesi esasları"


def paket(dosya, seed):
    return Paket(dosya, lesson="maliyet_muhasebesi", topic=MT, konu_adi="Maliyet Muhasebesi", seed=seed,
                 surum=SURUM, havuz="bolum")


T1 = paket("questions_maliyet_muhasebesi_2026.json", 2026093091)
T2 = paket("questions_maliyet_muhasebesi_test2_2026.json", 2026093092)
T3 = paket("questions_maliyet_muhasebesi_test3_2026.json", 2026093093)

# =============================================================================================== TEST 1
T1.q(R,
    "Bir çelik kapı üreticisinde mart ayında direkt ilk madde ve malzeme giderleri 184.500 ₺, direkt işçilik "
    "giderleri 62.000 ₺ ve genel üretim giderleri 91.500 ₺ olarak gerçekleşmiştir. Aynı ay pazarlama giderleri "
    "28.000 ₺, genel yönetim giderleri 35.000 ₺’dir.\n\nİlk (asal) maliyet ve dönüştürme (şekillendirme) maliyeti "
    "sırasıyla kaç ₺’dir?",
    "246.500; 153.500",
    ["184.500; 153.500", "246.500; 338.000", "153.500; 246.500", "338.000; 153.500"],
    "İlk (asal) maliyet = DİMM + DİŞ = 184.500 + 62.000 = 246.500 ₺. Dönüştürme maliyeti = DİŞ + GÜG = 62.000 + "
    "91.500 = 153.500 ₺. Pazarlama ve yönetim giderleri dönem gideridir, üretim maliyetine girmez.",
    topic=MT, zorluk="easy")

tablo = ("| Kalem | Tutar (₺) |\n|---|---|\n| Direkt ilk madde ve malzeme | 300.000 |\n| Direkt işçilik | 150.000 |\n"
         "| Genel üretim giderleri | 210.000 |\n| Dönem başı yarı mamul | 40.000 |\n| Dönem sonu yarı mamul | 55.000 |\n"
         "| Dönem başı mamul | 80.000 |\n| Dönem sonu mamul | 70.000 |")
umm = 300_000 + 150_000 + 210_000 + 40_000 - 55_000
smm = umm + 80_000 - 70_000
assert (umm, smm) == (645_000, 655_000)
T1.sayisal(R,
    "Bir endüstri işletmesinin nisan ayına ait maliyet verileri aşağıdaki tabloda verilmiştir:\n\n" + tablo +
    "\n\nBu verilere göre satılan mamuller maliyeti kaç ₺’dir?",
    tl(smm), secenekler(smm, umm, 660_000, 670_000, 635_000),
    "Dönem üretim maliyeti = 300.000 + 150.000 + 210.000 = 660.000 ₺. Üretilen mamul maliyeti = 660.000 + 40.000 − "
    "55.000 = 645.000 ₺. SMM = 645.000 + 80.000 − 70.000 = 655.000 ₺.", topic=MT)

T1.q(R,
    "Bir işletmenin muhasebe müdürü, maliyet muhasebesi ile finansal muhasebenin rollerini yeni çalışanlara "
    "anlatmaktadır. Hazırlanan sunumdaki ifadelerden biri hatalıdır.\n\nMaliyet muhasebesi ile finansal muhasebe "
    "arasındaki ilişkiyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Maliyet muhasebesi raporları dış kullanıcılar için yasal biçimde hazırlanır.",
    ["Maliyet muhasebesi mamul ve gider yeri düzeyinde ayrıntılı bilgi üretir.",
     "Maliyet muhasebesi verileri stok değerlemesi yoluyla finansal tablolara girer.",
     "Maliyet muhasebesi yönetimin kararları için dönem içi raporlar sunar.",
     "Finansal muhasebe işletmenin bütününe ilişkin sonuçları raporlar."],
    "Maliyet muhasebesi raporları esas olarak işletme içi kullanıcılara yöneliktir ve biçimi yönetimin ihtiyacına göre "
    "belirlenir. Dış kullanıcılara yönelik ve yasal biçim kurallarına bağlı raporlama finansal muhasebenin konusudur.",
    topic=MT)

T1.q("MSUGT 7/A: 720, 721",
    "Tekdüzen Muhasebe Sistemi Uygulama Genel Tebliği’nin 7/A seçeneğini uygulayan bir işletmede ay içinde direkt "
    "işçilik giderleri 720 hesabına fiili tutarla kaydedilmiş, üretime yüklenen tutarlar ise 721 hesabının alacağına "
    "yazılmıştır. Ay sonunda iki hesap arasında fark kalmamıştır.\n\nDönem sonunda 720 Direkt İşçilik Giderleri "
    "hesabı nasıl kapatılır?",
    "721 hesabı borçlandırılıp 720 hesabı alacaklandırılarak kapatılır.",
    ["720 hesabının kalanı doğrudan 620 hesabının borcuna aktarılır.",
     "720 hesabının kalanı 152 Mamuller hesabının alacağına aktarılır.",
     "720 hesabı kapatılmaz, bilançoda gider tahakkuku olarak kalır.",
     "720 hesabının kalanı 770 Genel Yönetim Giderleri hesabına devredilir."],
    "7/A seçeneğinde gider hesapları dönem sonunda karşılık gelen yansıtma hesaplarıyla kapatılır: 721 Direkt İşçilik "
    "Giderleri Yansıtma hesabı borçlandırılır, 720 hesabı alacaklandırılır. Böylece iki hesap da sıfırlanır.",
    topic=MT)

T1.sayisal(R,
    "Hareketli (sürekli) ağırlıklı ortalama yöntemini kullanan bir işletmenin mart ayı hammadde hareketleri "
    "şöyledir: 1 Mart stok 1.000 kg × 20 ₺; 5 Mart alış 3.000 kg × 24 ₺; 10 Mart üretime çıkış 2.500 kg; 20 Mart "
    "alış 1.500 kg × 27 ₺; 25 Mart üretime çıkış 2.000 kg.\n\nMart ayında üretime verilen hammaddenin maliyeti kaç "
    "₺’dir?",
    tl(2_500 * 23 + 2_000 * 25), secenekler(107_500, 105_500, 112_500, 102_000, 110_250),
    "5 Mart sonrası ortalama = (20.000 + 72.000) ÷ 4.000 = 23 ₺; 10 Mart çıkışı 2.500 × 23 = 57.500 ₺, kalan 1.500 "
    "kg × 23 = 34.500 ₺. 20 Mart sonrası ortalama = (34.500 + 40.500) ÷ 3.000 = 25 ₺; 25 Mart çıkışı 2.000 × 25 = "
    "50.000 ₺. Toplam 107.500 ₺.", topic=MU, zorluk="hard")

T1.q(R,
    "Bir mobilya fabrikasında ay içinde kereste kesen marangozların, döşeme işçilerinin, ürünlere cila uygulayan "
    "işçilerin ve montaj hattındaki işçilerin ücretleri ödenmiştir. Ayrıca fabrika binasını koruyan bekçinin ücreti "
    "de aynı bordroda yer almaktadır.\n\nBu ücretlerden hangisi genel üretim gideri olarak izlenir?",
    "Fabrika bekçisinin ücreti",
    ["Kereste kesen marangozların ücreti", "Döşeme işçilerinin ücreti", "Cila işçilerinin ücreti",
     "Montaj hattı işçilerinin ücreti"],
    "Mamul üzerinde doğrudan çalışan ve mamulle ilişkisi kolayca izlenebilen işçilerin ücretleri direkt işçiliktir. "
    "Bekçi üretime dolaylı hizmet verir; ücreti endirekt işçilik olarak genel üretim giderleri içinde izlenir.",
    topic=MU, zorluk="easy")

dis = 440 * 150 * 1.225
T1.sayisal(R,
    "Bir işletmede üretim işçileri ay içinde siparişlerden bağımsız olarak 400 saat normal ve 40 saat fazla mesai "
    "yapmıştır. Normal saat ücreti 150 ₺, fazla mesai zammı %50’dir; zam belirli bir siparişten "
    "kaynaklanmadığından genel üretim giderine yüklenmektedir. İşveren sigorta primi payının brüt ücretin %22,5’i "
    "olduğu varsayılmaktadır.\n\nDirekt işçilik gideri olarak kaydedilecek tutar kaç ₺’dir?",
    tl(dis), secenekler(dis, 84_525, 66_000, 69_000, 73_500),
    "Fazla mesai saatleri normal ücretle direkt işçiliğe girer: 440 × 150 = 66.000 ₺; işveren payıyla 66.000 × 1,225 = "
    "80.850 ₺. Zam kısmı (40 × 75 = 3.000 ₺ ve payı) siparişe özgü olmadığından GÜG’e yüklenir.",
    topic=MU, zorluk="hard")

tablo = ("| Gider yeri | Birincil giderler (₺) | Alan (m²) | Yardımcı hizmet saati |\n|---|---|---|---|\n"
         "| A esas üretim | 180.000 | 400 | 400 |\n| B esas üretim | 250.000 | 600 | 700 |\n"
         "| Y yardımcı üretim | 70.000 | 200 | – |")
kira = 240_000
b = 250_000 + kira * 600 / 1_200 + (70_000 + kira * 200 / 1_200) * 700 / 1_100
assert b == 440_000
T1.sayisal(R,
    "Bir işletmenin gider yerlerine ait veriler aşağıdadır:\n\n" + tablo + "\n\nAyrıca 240.000 ₺ fabrika kirası "
    "alan esasına göre gider yerlerine dağıtılacak, ardından Y yardımcı gider yerinin toplamı esas üretim gider "
    "yerlerine hizmet saati esasına göre aktarılacaktır.\n\nİkinci dağıtım sonunda B gider yerinin toplam gideri kaç "
    "₺’dir?",
    tl(b), secenekler(b, 370_000, 425_000, 410_000, 480_000),
    "Kira payları: A 80.000, B 120.000, Y 40.000 ₺. Y toplamı 70.000 + 40.000 = 110.000 ₺; B’nin payı 110.000 × 700 ÷ "
    "1.100 = 70.000 ₺. B toplamı = 250.000 + 120.000 + 70.000 = 440.000 ₺.", topic=GD, zorluk="hard")

T1.sayisal(R,
    "Faaliyet tabanlı maliyetleme uygulayan bir işletmede makine ayar faaliyetinin yıllık gideri 360.000 ₺, "
    "bütçelenen ayar sayısı 120’dir. Kalite kontrol faaliyetinin gideri 240.000 ₺, bütçelenen kontrol sayısı "
    "400’dür. X ürünü dönem içinde 18 makine ayarı ve 50 kalite kontrol gerektirmiştir.\n\nX ürününe bu iki "
    "faaliyetten yüklenecek toplam gider kaç ₺’dir?",
    tl(18 * 3_000 + 50 * 600), secenekler(84_000, 54_000, 30_000, 90_000, 78_000),
    "Faaliyet oranları: ayar 360.000 ÷ 120 = 3.000 ₺/ayar; kalite kontrol 240.000 ÷ 400 = 600 ₺/kontrol. X’e "
    "yüklenen = 18 × 3.000 + 50 × 600 = 54.000 + 30.000 = 84.000 ₺.", topic=GD)

T1.sayisal(R,
    "Ağırlıklı ortalama yöntemini uygulayan bir safha işletmesinde dönem başında 2.000 birim yarı mamul (dönüşüm "
    "%40) vardır; dönemde 18.000 birim üretime başlanmış, 17.000 birim tamamlanmıştır. Dönem sonunda 3.000 birim "
    "yarı mamul dönüşüm bakımından %60 tamamlanmıştır. Hammaddenin tamamı sürecin başında verilmektedir.\n\n"
    "Dönüşüm maliyetleri için eşdeğer birim sayısı kaçtır?",
    f"{tl(17_000 + 1_800)} birim", [f"{tl(x)} birim" for x in (18_000, 20_000, 17_000, 19_200)],
    "Ağırlıklı ortalamada eşdeğer birim = tamamlanan + dönem sonu yarı mamulün eşdeğeri = 17.000 + 3.000 × %60 = "
    "18.800 birim. Dönem başı stokun tamamlanma derecesi bu yöntemde düşülmez (FIFO’da 18.000 olurdu).",
    topic=MS)

sip = 42_000 + 600 * 150 + 600 * 80
T1.sayisal(R,
    "Sipariş maliyet yöntemini uygulayan bir işletmede 400 birimlik S-12 siparişi için 42.000 ₺ direkt ilk madde "
    "ve malzeme kullanılmış, 600 direkt işçilik saati çalışılmıştır. Saat ücreti 150 ₺’dir; genel üretim giderleri "
    "önceden belirlenmiş oranla direkt işçilik saati başına 80 ₺ olarak yüklenmektedir. Sipariş ay içinde "
    "tamamlanmıştır.\n\nS-12 siparişinin birim maliyeti kaç ₺’dir?",
    tl(sip / 400), secenekler(sip / 400, 330, 225, 105, 570),
    "Sipariş maliyeti = 42.000 + 600 × 150 + 600 × 80 = 42.000 + 90.000 + 48.000 = 180.000 ₺. Birim maliyet = "
    "180.000 ÷ 400 = 450 ₺.", topic=MS, zorluk="easy")

r = 240_000 * 120_000 / 300_000
T1.sayisal(R,
    "Bir işletmede ortak üretim sürecinden ayrılma noktasında P ve R ürünleri elde edilmektedir. Ortak maliyet "
    "240.000 ₺’dir. Ayrılma noktasında P’den 4.000 kg (satış fiyatı 45 ₺/kg), R’den 6.000 kg (satış fiyatı 20 ₺/kg) "
    "elde edilmiştir. İşletme ortak maliyeti ayrılma noktasındaki satış değerleri oranında dağıtmaktadır.\n\nR "
    "ürününe dağıtılacak ortak maliyet kaç ₺’dir?",
    tl(r), secenekler(r, 144_000, 120_000, 80_000, 160_000),
    "Satış değerleri: P 4.000 × 45 = 180.000 ₺, R 6.000 × 20 = 120.000 ₺; toplam 300.000 ₺. R’nin payı = 240.000 × "
    "120.000 ÷ 300.000 = 96.000 ₺. Fiziksel miktar esası (144.000 ₺) farklı sonuç verir.", topic=MS)

yan = 40_000 - 6_000 - 4_000 - 0.10 * 40_000
T1.sayisal(R,
    "Bir işletmede ortak üretim maliyeti 500.000 ₺’dir. Ana ürünün yanında elde edilen yan ürünün satış değeri "
    "40.000 ₺’dir; yan ürün için ayrılma noktasından sonra 6.000 ₺ işlem ve 4.000 ₺ satış gideri katlanılacak, "
    "satışlar üzerinden %10 normal kâr beklenmektedir. Yan ürün maliyeti satış fiyatından geriye doğru hesaplama "
    "yöntemiyle bulunmaktadır.\n\nAna ürüne kalan ortak maliyet kaç ₺’dir?",
    tl(500_000 - yan), secenekler(500_000 - yan, 460_000, 470_000, 500_000, 480_000),
    "Yan ürünün ayrılma noktasındaki maliyeti = 40.000 − 6.000 − 4.000 − 4.000 (normal kâr) = 26.000 ₺. Ana ürün "
    "maliyeti = 500.000 − 26.000 = 474.000 ₺.", topic=MS, zorluk="hard")

T1.q(R,
    "Bir çimento fabrikası kesintisiz ve tek tip üretim yapmakta; ürün kırma, öğütme ve paketleme bölümlerinden "
    "sırayla geçmektedir. Muhasebe birimi maliyet yöntemini açıklayan bir not hazırlamıştır.\n\nBu işletmenin "
    "uygulayacağı safha maliyet yöntemiyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Maliyetler siparişler itibarıyla sipariş maliyet kartlarında izlenir.",
    ["Maliyetler üretim bölümleri (safhalar) itibarıyla toplanır.",
     "Dönem sonu yarı mamuller için eşdeğer birim hesaplanır.",
     "Bir safhada tamamlanan ürünün maliyeti sonraki safhaya aktarılır.",
     "Birim maliyet, safha maliyetinin eşdeğer birime bölünmesiyle bulunur."],
    "Safha maliyet yönteminde maliyetler bölümler itibarıyla toplanır ve eşdeğer birimlere bölünür. Maliyetlerin "
    "sipariş maliyet kartlarında izlenmesi sipariş maliyet yönteminin özelliğidir.", topic=MS)

T1.q(R,
    "Sipariş maliyet yöntemini uygulayan bir matbaada K-8 siparişinde, müşterinin baskı sırasında renk tonunu "
    "değiştirmesi nedeniyle 300 adet katalog kullanılamaz hâle gelmiştir. Bozulan kataloglar hurda olarak "
    "satılamamaktadır ve müşteri değişikliğin maliyetini üstlenmeyi kabul etmiştir.\n\nBozulan katalogların "
    "maliyeti nasıl işlem görür?",
    "K-8 siparişinin maliyetinde bırakılır.",
    ["Genel üretim giderlerine eklenerek tüm siparişlere dağıtılır.",
     "Olağan dışı gider ve zarar olarak dönem gideri yazılır.",
     "Satılan mamuller maliyetine doğrudan aktarılır.",
     "Diğer siparişlerin maliyetlerine eşit olarak bölüştürülür."],
    "Bozulma belirli bir siparişe özgü nedenden (müşteri isteği) doğduğunda maliyeti o siparişte bırakılır ve "
    "müşteriye yansıtılır. Tüm üretimde olağan olan bozulmalar ise GÜG yoluyla dağıtılır.", topic=UK)

T1.q(R,
    "Bir işletmede bir birim mamul için standart olarak 2 kg hammadde öngörülmüş, standart fiyat 18 ₺/kg’dır. Ay "
    "içinde 4.500 birim üretilmiş; 9.300 kg hammadde kilogramı 17,50 ₺’den kullanılmıştır.\n\nDirekt ilk madde ve "
    "malzeme fiyat ve miktar farkları sırasıyla aşağıdakilerden hangisidir?",
    "4.650 ₺ olumlu; 5.400 ₺ olumsuz",
    ["4.650 ₺ olumsuz; 5.400 ₺ olumlu", "4.500 ₺ olumlu; 5.250 ₺ olumsuz", "4.650 ₺ olumlu; 5.250 ₺ olumsuz",
     "750 ₺ olumsuz; 5.400 ₺ olumsuz"],
    "Standart miktar = 4.500 × 2 = 9.000 kg. Fiyat farkı = (17,50 − 18) × 9.300 = 4.650 ₺ olumlu; miktar farkı = "
    "(9.300 − 9.000) × 18 = 5.400 ₺ olumsuz. Toplam fark 750 ₺ olumsuzdur.", topic=SM)

T1.q("MSUGT 7/A: 722",
    "Tekdüzen Muhasebe Sistemi Uygulama Genel Tebliği’nin 7/A seçeneğini ve standart maliyet sistemini uygulayan bir "
    "işletmede ay içinde hem standarttan yüksek hem de standarttan düşük ücretle çalışılan dönemler olmuştur.\n\n"
    "722 Direkt İşçilik Ücret Farkları hesabıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Olumsuz farklar borca, olumlu farklar alacağa yazılır; dönem sonunda stok ve satış maliyetine aktarılır.",
    ["Olumlu ve olumsuz farklar alacağına yazılır; dönem sonunda 720 hesabına aktarılarak kapatılır.",
     "Olumsuz farklar alacağına, olumlu farklar borcuna yazılır; dönem sonunda 649 hesabına aktarılır.",
     "Ücret ve süre farkları aynı hesapta izlenir; dönem sonunda kapatılmayıp bilançoda gider tahakkuku olarak kalır.",
     "Olumsuz farklar borcuna yazılır; olumlu farklar 722 yerine 723 hesabının alacağında izlenir."],
    "722 hesabı direkt işçilik ücret farklarını izler; olumsuz farklar borca, olumlu farklar alacağa kaydedilir. "
    "Süre farkları ayrıca 723 hesabında izlenir; fark hesapları dönem sonunda ilgili stok ve satış maliyeti "
    "hesaplarına aktarılarak kapatılır.", topic=SM)

degisken = 245_000 - 251_300
sabit = 367_000 - 347_100
assert (degisken, sabit, degisken + sabit) == (-6_300, 19_900, 13_600)
T1.q(R,
    "Bir işletmede ay içinde mamullere yüklenen (standart) ve gerçekleşen genel üretim giderleri şöyledir: değişken "
    "GÜG yüklenen 245.000 ₺, gerçekleşen 251.300 ₺; sabit GÜG yüklenen 367.000 ₺, gerçekleşen 347.100 ₺.\n\nToplam "
    "GÜG’de ortaya çıkan fark ve niteliği aşağıdakilerden hangisidir?",
    "13.600 ₺ fazla yükleme",
    ["13.600 ₺ eksik yükleme", "26.200 ₺ fazla yükleme", "19.900 ₺ fazla yükleme", "6.300 ₺ eksik yükleme"],
    "Değişken GÜG’de 251.300 − 245.000 = 6.300 ₺ eksik, sabit GÜG’de 367.000 − 347.100 = 19.900 ₺ fazla yükleme "
    "vardır. Toplamda yüklenen 612.000 ₺, gerçekleşen 598.400 ₺ olduğundan 13.600 ₺ fazla yükleme oluşur.",
    topic=SM)

T1.sayisal(R,
    "Bir işletmenin tek ürününün satış fiyatı 400 ₺, birim değişken maliyeti 260 ₺’dir. Yıllık sabit maliyetler "
    "1.120.000 ₺ olup bunun 320.000 ₺’si amortismandır. Yönetim gelecek yıl zarar etmemek için ulaşılması gereken "
    "satış hasılatını bilmek istemektedir.\n\nBaşabaş satış hasılatı kaç ₺’dir?",
    tl(1_120_000 / 0.35), secenekler(3_200_000, 1_723_077, 2_285_714, 2_800_000, 3_600_000),
    "Katkı payı oranı = (400 − 260) ÷ 400 = %35. Başabaş satış hasılatı = 1.120.000 ÷ 0,35 = 3.200.000 ₺. "
    "Amortisman yalnız nakit başabaş hesabında düşülür.", lesson=YM, topic="maliyet_hacim_kar")

T1.oncul(R,
    "Maliyet kavramlarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Dönem maliyetleri stoklarda aktifleştirilir ve mamul satılınca gidere dönüşür.",
     "Mamul maliyetleri mamul satıldığında satılan mamuller maliyeti olarak gider yazılır.",
     "Genel yönetim giderleri oluştukları dönemin gideridir.",
     "Fabrika binasının amortismanı mamul maliyetine girer."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "II, III ve IV", ["I ve II", "II ve III", "I, II ve IV", "II, III ve IV", "I, III ve IV"],
    "II, III ve IV doğrudur. I yanlıştır: stoklarda aktifleştirilip satışla gidere dönüşen maliyetler mamul "
    "maliyetleridir; dönem maliyetleri oluştukları dönemde doğrudan gider yazılır.", topic=MT)

# =============================================================================================== TEST 2
umm = 64_000 + 210_000 + 95_000 + 133_000 - 72_000
T2.sayisal(R,
    "Bir endüstri işletmesinin 151 Yarı Mamuller – Üretim hesabına ilişkin mayıs ayı verileri şöyledir: dönem başı "
    "yarı mamul 64.000 ₺, dönemde yüklenen direkt ilk madde ve malzeme 210.000 ₺, direkt işçilik 95.000 ₺ ve genel "
    "üretim giderleri 133.000 ₺. Ay sonunda 72.000 ₺ tutarında yarı mamul kalmıştır.\n\nAy içinde 152 Mamuller "
    "hesabına aktarılacak tamamlanan mamul maliyeti kaç ₺’dir?",
    tl(umm), secenekler(umm, 438_000, 502_000, 366_000, 494_000),
    "Tamamlanan mamul maliyeti = dönem başı yarı mamul + dönem üretim maliyeti − dönem sonu yarı mamul = 64.000 + "
    "438.000 − 72.000 = 430.000 ₺.", topic=MT, zorluk="easy")

T2.q(R,
    "Bir işletmede ay içinde şu olaylar yaşanmıştır: üretimde 120.000 ₺ hammadde kullanılmış, reklam ajansına "
    "45.000 ₺ ödenmiş, yeni bir makine 300.000 ₺’ye satın alınmıştır. Ayrıca sel baskını nedeniyle depodaki 80.000 "
    "₺’lik hammadde kullanılamaz hâle gelmiş ve sigorta tazminatı alınamamıştır.\n\nDepodaki hammaddenin sel "
    "nedeniyle kullanılamaz hâle gelmesi hangi kavramla açıklanır?",
    "Zarar",
    ["Maliyet", "Gider", "Yatırım harcaması", "Dönem maliyeti"],
    "Karşılığında gelir elde edilmeyen, olağan dışı nedenle ortaya çıkan değer kaybı zarardır. Hammaddenin üretimde "
    "kullanılması maliyet, reklam ödemesi gider, makine alımı ise yatırım harcamasıdır.", topic=MT, zorluk="easy")

T2.q(R,
    "Bir işletmenin maliyet muhasebecisi gider kalemlerini fonksiyonlarına göre sınıflandıran bir tablo "
    "hazırlamıştır. Denetim sırasında tablodaki eşleştirmelerden birinin hatalı olduğu görülmüştür.\n\nAşağıdaki "
    "eşleştirmelerden hangisi yanlıştır?",
    "Fabrika müdürünün maaşı – direkt işçilik",
    ["Mobilya üretiminde kullanılan kereste – direkt ilk madde",
     "Fabrika binasının sigorta primi – genel üretim gideri",
     "Satış temsilcisinin primi – pazarlama gideri",
     "Muhasebe servisinin kırtasiye gideri – genel yönetim gideri"],
    "Fabrika müdürü mamul üzerinde doğrudan çalışmaz; maaşı endirekt işçilik olarak genel üretim giderleri içinde "
    "izlenir. Diğer eşleştirmeler doğrudur.", topic=MU, zorluk="easy")

T2.q("MSUGT 7/B: 790-798",
    "Tekdüzen Muhasebe Sistemi Uygulama Genel Tebliği’ne göre giderlerini 7/B seçeneğine göre izlemeyi seçen bir "
    "işletmenin muhasebe müdürü, hesap planını yeniden düzenlemektedir.\n\n7/B seçeneğinde giderler hangi hesap "
    "grubunda ve hangi esasa göre izlenir?",
    "79 Gider Çeşitleri grubunda, çeşit esasına göre",
    ["71-77 hesap gruplarında, fonksiyon esasına göre",
     "62 Satışların Maliyeti grubunda, satış esasına göre",
     "15 Stoklar grubunda, mamul esasına göre",
     "69 Dönem Net Kârı grubunda, sonuç esasına göre"],
    "7/B seçeneğinde giderler çeşit esasına göre 790-797 hesaplarında (ilk madde ve malzeme, işçi ücretleri, "
    "amortisman vb.) izlenir ve 798 Gider Çeşitleri Yansıtma hesabıyla aktarılır. Fonksiyon esasına göre izleme 7/A "
    "seçeneğidir.", topic=MT)

T2.sayisal(R,
    "İlk giren ilk çıkar (FIFO) yöntemini uygulayan bir işletmenin dönem başında 500 kg × 40 ₺ hammadde stoku "
    "vardır. Dönem içinde önce 1.500 kg × 44 ₺, sonra 1.000 kg × 46 ₺ alış yapılmış ve tüm alışlardan sonra toplam "
    "2.200 kg hammadde üretime verilmiştir.\n\nÜretime verilen hammaddenin maliyeti kaç ₺’dir?",
    tl(500 * 40 + 1_500 * 44 + 200 * 46), secenekler(95_200, 96_800, 98_800, 88_000, 101_200),
    "FIFO’da önce eldeki en eski partiler kullanılır: 500 × 40 + 1.500 × 44 + 200 × 46 = 20.000 + 66.000 + 9.200 = "
    "95.200 ₺. Dönemsel ağırlıklı ortalama 96.800 ₺, son giren ilk çıkar 98.800 ₺ verir.", topic=MU)

T2.q("TMS 2 md. 10-11, 18",
    "Bir işletme ithal ettiği hammaddenin maliyetini belirlemektedir. Faturada mal bedelinin yanında navlun, taşıma "
    "sigortası, gümrük vergisi ve boşaltma giderleri yer almakta; ayrıca bedelin altı ay vadeli ödenmesi karşılığında "
    "tedarikçiye vade farkı ödenmektedir.\n\nTMS 2 Stoklar Standardı’na göre aşağıdakilerden hangisi hammaddenin "
    "maliyetine eklenmez?",
    "Vadeli alım nedeniyle ödenen vade farkı",
    ["Alış nakliyesi (navlun)", "Taşıma sigortası", "İthalatta ödenen gümrük vergisi",
     "Boşaltma ve yükleme giderleri"],
    "TMS 2’ye göre satın alma maliyeti alış fiyatı, ithalat vergileri, nakliye ve elleçleme gibi doğrudan giderleri "
    "içerir. Normal kredi koşullarının ötesindeki vadeden doğan fark finansman niteliğinde olduğundan faiz gideri "
    "olarak dönem boyunca muhasebeleştirilir.", topic=MU)

dis = 120_000 * 1.205
T2.sayisal(R,
    "Bir işletmenin ay sonu ücret bordrosunda brüt ücretler toplamı 180.000 ₺’dir; bunun 120.000 ₺’si üretim "
    "işçilerine, 25.000 ₺’si ustabaşılarına, 35.000 ₺’si satış personeline aittir. İşveren sigorta primi payının "
    "brüt ücretin %20,5’i olduğu varsayılmaktadır.\n\nDirekt işçilik gideri olarak kaydedilecek tutar kaç ₺’dir?",
    tl(dis), secenekler(dis, 120_000, 174_725, 216_900, 145_000),
    "Direkt işçilik yalnız üretim işçilerinin ücretini ve bu ücret üzerindeki işveren payını kapsar: 120.000 × 1,205 = "
    "144.600 ₺. Ustabaşı ücreti GÜG’e, satış personelinin ücreti pazarlama giderine girer.", topic=MU)

a = 300_000 + 60_000 * 0.60 + 90_000 / 3
T2.sayisal(R,
    "Bir işletmede yardımcı gider yerlerinin giderleri doğrudan dağıtım yöntemiyle esas üretim gider yerlerine "
    "aktarılmaktadır. Y1 yardımcı gider yerinin 60.000 ₺’lik gideri A ve B’ye %60 ve %40, Y2’nin 90.000 ₺’lik "
    "gideri A ve B’ye 1/3 ve 2/3 oranında dağıtılacaktır. A gider yerinin birincil giderleri 300.000 ₺’dir.\n\n"
    "Dağıtım sonunda A gider yerinin toplam gideri kaç ₺’dir?",
    tl(a), secenekler(a, 336_000, 330_000, 384_000, 450_000),
    "A’nın payları: Y1’den 60.000 × %60 = 36.000 ₺, Y2’den 90.000 × 1/3 = 30.000 ₺. A toplamı = 300.000 + 36.000 + "
    "30.000 = 366.000 ₺. Doğrudan dağıtımda yardımcı gider yerleri birbirine pay vermez.", topic=GD)

T2.q(R,
    "Bir işletmede kalıp döküm bölümünde üretimin büyük kısmı otomatik makinelerle yapılmakta, işçiler yalnızca "
    "makinelerin gözetimini üstlenmektedir. Bölümün genel üretim giderlerinin çoğu amortisman, enerji ve bakım "
    "giderlerinden oluşmaktadır.\n\nBu bölüm için en uygun GÜG yükleme esası aşağıdakilerden hangisidir?",
    "Makine saati",
    ["Direkt işçilik saati", "Direkt işçilik tutarı", "Direkt ilk madde tutarı", "Üretilen birim sayısı"],
    "Yükleme esası, GÜG’ün oluşmasına en çok neden olan faktörle ilişkili olmalıdır. Makine yoğun bir bölümde "
    "amortisman, enerji ve bakım giderleri makine çalışma süresiyle değiştiğinden makine saati en uygun esastır.",
    topic=GD, zorluk="easy")

dimm_es = 8_500 - 1_000 + 1_500
don_es = 8_500 - 300 + 600
assert (180_000 / dimm_es, 220_000 / don_es) == (20, 25)
T2.sayisal(R,
    "FIFO yöntemini uygulayan bir safha işletmesinde dönem başında 1.000 birim yarı mamul (hammadde %100, dönüşüm %30 "
    "tamamlanmış) bulunmaktadır. Dönemde 9.000 birime başlanmış, 8.500 birim tamamlanmış; dönem sonunda 1.500 birim "
    "yarı mamul dönüşüm bakımından %40 tamamlanmıştır. Dönemde 180.000 ₺ hammadde ve 220.000 ₺ dönüşüm maliyeti "
    "katlanılmıştır.\n\nDönem dönüşüm maliyetinin eşdeğer birim maliyeti kaç ₺’dir?",
    tl(25), secenekler(25, 22, 20, 27.5, 26),
    "FIFO’da yalnız dönemde yapılan iş hesaba katılır: dönüşüm eşdeğeri = 8.500 − 1.000 × %30 + 1.500 × %40 = 8.500 − "
    "300 + 600 = 8.800 birim. Birim dönüşüm maliyeti = 220.000 ÷ 8.800 = 25 ₺.", topic=MS, zorluk="hard")

T2.q(R,
    "Bir işletme GÜG’ü dönem başında belirlediği makine saati başına 60 ₺ oranla siparişlere yüklemektedir. Ay "
    "içinde siparişlerde 5.200 makine saati çalışılmış ve 325.000 ₺ fiili genel üretim gideri "
    "gerçekleşmiştir.\n\nAy sonunda GÜG yüklemesinde ortaya çıkan fark ve niteliği aşağıdakilerden hangisidir?",
    "13.000 ₺ eksik yükleme",
    ["13.000 ₺ fazla yükleme", "312.000 ₺ eksik yükleme", "25.000 ₺ eksik yükleme", "7.000 ₺ fazla yükleme"],
    "Yüklenen GÜG = 5.200 × 60 = 312.000 ₺; fiili GÜG 325.000 ₺. Fiili gider yüklenenden fazla olduğundan 13.000 ₺ "
    "eksik yükleme vardır; fark dönem sonunda stok ve satış maliyetine ya da doğrudan SMM’ye aktarılır.",
    topic=MS)

ngd = {"X": 5_000 * 40 - 50_000, "Y": 3_000 * 50 - 30_000, "Z": 2_000 * 30}
y = 165_000 * ngd["Y"] / sum(ngd.values())
assert y == 60_000
T2.sayisal(R,
    "Bir işletmede 165.000 ₺ ortak maliyetle X, Y ve Z ürünleri elde edilmektedir. X (5.000 birim) 50.000 ₺ ek "
    "işlemden sonra birim 40 ₺’ye, Y (3.000 birim) 30.000 ₺ ek işlemden sonra birim 50 ₺’ye satılmakta; Z (2.000 "
    "birim) ek işlem görmeden birim 30 ₺’ye satılmaktadır. Ortak maliyet net gerçekleşebilir değer yöntemiyle "
    "dağıtılmaktadır.\n\nY ürününe dağıtılacak ortak maliyet kaç ₺’dir?",
    tl(y), secenekler(y, 55_000, 49_500, 75_000, 72_000),
    "Net gerçekleşebilir değerler: X 200.000 − 50.000 = 150.000 ₺; Y 150.000 − 30.000 = 120.000 ₺; Z 60.000 ₺; toplam "
    "330.000 ₺. Y’nin payı = 165.000 × 120.000 ÷ 330.000 = 60.000 ₺.", topic=MS, zorluk="hard")

T2.q(R,
    "Bir rafineride ham petrolün işlenmesiyle aynı süreçten benzin, motorin ve az miktarda asfalt elde edilmektedir. "
    "Benzin ve motorinin satış değerleri toplam gelirin %96’sını, asfaltın ise %4’ünü oluşturmaktadır.\n\nBu "
    "ürünlerin maliyet muhasebesi açısından sınıflandırılması aşağıdakilerden hangisinde doğru verilmiştir?",
    "Benzin ve motorin ortak mamul, asfalt yan üründür.",
    ["Üç ürün de yan üründür; ortak maliyet dağıtılmaz.",
     "Benzin ana ürün, motorin ve asfalt artıktır.",
     "Asfalt ortak mamul, benzin ve motorin yan üründür.",
     "Üç ürün de ortak mamuldür; satış payı önem taşımaz."],
    "Aynı süreçten birlikte elde edilen ve satış değerleri önemli olan ürünler ortak mamuldür. Satış değeri ana "
    "ürünlere göre önemsiz kalan asfalt yan üründür; maliyeti genellikle ortak maliyetten düşülerek belirlenir.",
    topic=MS, zorluk="easy")

anormal = (650 - 10_000 * 0.04) * 30
T2.sayisal(R,
    "Bir safha işletmesinde dönemde 10.000 birime başlanmıştır. Başlanan birimlerin %4’üne kadar kayıp normal kabul "
    "edilmektedir; dönemde 650 birim kayıp olmuştur. Kayıp sürecin sonundaki kontrol noktasında ortaya çıkmakta ve "
    "kontrol noktasına ulaşan bir birimin maliyeti 30 ₺’dir.\n\nDönem gideri olarak yazılacak anormal kayıp "
    "maliyeti kaç ₺’dir?",
    tl(anormal), secenekler(anormal, 19_500, 12_000, 7_800, 4_500),
    "Normal kayıp = 10.000 × %4 = 400 birim; anormal kayıp = 650 − 400 = 250 birim. Anormal kayıp maliyeti = 250 × 30 = "
    "7.500 ₺ olup dönem gideri yazılır; normal kaybın maliyeti sağlam ürünlere yüklenir.", topic=UK)

u, z = (210 - 200) * 3_400, (3_400 - 3_200) * 200
assert (u, z) == (34_000, 40_000)
T2.q(R,
    "Bir işletmede ay içinde fiilen 3.400 direkt işçilik saati çalışılmış ve saat başına 210 ₺ ücret ödenmiştir. "
    "Ayın fiili üretimi 1.600 birimdir; birim başına standart süre 2 saat, standart saat ücreti 200 ₺’dir.\n\nDirekt "
    "işçilik ücret ve zaman farkları sırasıyla aşağıdakilerden hangisidir?",
    "34.000 ₺ olumsuz; 40.000 ₺ olumsuz",
    ["34.000 ₺ olumlu; 40.000 ₺ olumsuz", "32.000 ₺ olumsuz; 42.000 ₺ olumsuz", "34.000 ₺ olumsuz; 42.000 ₺ olumsuz",
     "40.000 ₺ olumsuz; 34.000 ₺ olumsuz"],
    "Standart saat = 1.600 × 2 = 3.200. Ücret farkı = (210 − 200) × 3.400 = 34.000 ₺ olumsuz; zaman farkı = (3.400 − "
    "3.200) × 200 = 40.000 ₺ olumsuz.", topic=SM)

T2.q(R,
    "Bir işletmenin maliyet kontrol birimi, standart maliyet farklarını sorumluluk birimleriyle eşleştiren bir rapor "
    "hazırlamıştır. Raporun değerlendirilmesi sırasında bir eşleştirmenin hatalı olduğu görülmüştür.\n\nStandart "
    "maliyet farklarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "DİMM fiyat farkının sorumlusu genellikle üretim bölümü yöneticisidir.",
    ["DİMM miktar farkı genellikle üretim bölümünün kontrolündedir.",
     "Direkt işçilik zaman farkı işçilerin verimliliğiyle ilgilidir.",
     "Kapasite farkı çoğunlukla satış hacmi ve üst yönetim kararlarından doğar.",
     "GÜG bütçe farkı gider kalemlerindeki fazla harcamayı gösterir."],
    "DİMM fiyat farkı alış fiyatının standarttan sapmasıdır ve alım kararını veren satın alma biriminin "
    "sorumluluğundadır. Üretim bölümü ise kullanılan miktardan, dolayısıyla miktar farkından sorumludur.",
    topic=SM)

butce = 164_000 - (120_000 + 10 * 3_800)
T2.sayisal(R,
    "Bir işletmede normal kapasite 4.000 DİS, sabit GÜG bütçesi 120.000 ₺ ve değişken GÜG oranı DİS başına 10 ₺’dir. "
    "Ay içinde fiilen 3.800 DİS çalışılmış, fiili üretim için standart süre 3.700 DİS olmuş ve 164.000 ₺ GÜG "
    "gerçekleşmiştir.\n\nÜçlü analize göre GÜG bütçe farkı kaç ₺’dir?",
    tl(butce), secenekler(butce, 7_000, 12_000, 16_000, 4_000),
    "Fiili saate göre esnek bütçe = 120.000 + 10 × 3.800 = 158.000 ₺. Bütçe farkı = 164.000 − 158.000 = 6.000 ₺ "
    "olumsuz. Standart saate göre bütçe (157.000 ₺) kullanılırsa 7.000 ₺ bulunur.", topic=SM, zorluk="hard")

kar = 9_000 * (220 - 150) - 480_000
T2.sayisal(R,
    "Bir işletme dönem içinde ürettiği 9.000 birimin tamamını birim 220 ₺’den satmıştır. Birim değişken maliyet "
    "(üretim ve satış) 150 ₺’dir. Sabit genel üretim giderleri 300.000 ₺, sabit yönetim giderleri 180.000 ₺’dir. "
    "İşletme iç raporlamada katkı payı esaslı gelir tablosu kullanmaktadır.\n\nBu tabloda raporlanacak faaliyet kârı "
    "kaç ₺’dir?",
    tl(kar), secenekler(kar, 630_000, 330_000, 450_000, 1_980_000),
    "Toplam katkı payı = 9.000 × (220 − 150) = 630.000 ₺. Faaliyet kârı = 630.000 − 300.000 − 180.000 = 150.000 ₺.",
    lesson=YM, topic="maliyet_hacim_kar", zorluk="easy")

T2.q("MSUGT 7/A: 730, 731",
    "7/A seçeneğini uygulayan bir işletmede ay içinde genel üretim giderleri 730 hesabında 420.000 ₺ olarak "
    "toplanmış ve aynı tutar önceden belirlenmiş oranlarla yarı mamullere yüklenerek 731 hesabına alacak "
    "kaydedilmiştir.\n\nAy sonunda 730 hesabının kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(731, 420_000)], [(730, 420_000)]),
    [K([(730, 420_000)], [(731, 420_000)]),
     K([(151, 420_000)], [(730, 420_000)]),
     K([(152, 420_000)], [(731, 420_000)]),
     K([(620, 420_000)], [(730, 420_000)])],
    "7/A’da gider hesapları yansıtma hesaplarıyla kapatılır: 731 GÜG Yansıtma hesabı borçlandırılır, 730 GÜG "
    "hesabı alacaklandırılır. Yarı mamullere yükleme (151 borç / 731 alacak) ay içinde yapılmıştır.", topic=MT)

T2.q(R,
    "Faaliyet tabanlı maliyetleme sistemi kuran bir işletme, satın alma faaliyetinin giderlerini ürünlere yüklemek "
    "için bir maliyet sürücüsü seçecektir. Satın alma giderleri, verilen sipariş sayısına göre değişmekte; sipariş "
    "tutarı ve miktarı giderleri etkilememektedir.\n\nBu faaliyet için en uygun maliyet sürücüsü aşağıdakilerden "
    "hangisidir?",
    "Satın alma sipariş sayısı",
    ["Satın alınan malzeme tutarı", "Direkt işçilik saati", "Üretilen birim sayısı", "Makine çalışma saati"],
    "Maliyet sürücüsü, faaliyet giderinin oluşmasına neden olan etkendir. Satın alma giderleri sipariş sayısıyla "
    "değiştiğinden sipariş sayısı seçilmelidir; hacme dayalı esaslar karmaşık ürünlere eksik pay yükler.",
    topic=GD)

# =============================================================================================== TEST 3
uretim = 150_000 + 90_000 + 120_000
gelir_tablosu = uretim * 0.80 + 60_000 + 80_000 + 20_000
T3.sayisal(R,
    "Yeni kurulan bir işletmenin ilk dönem giderleri şöyledir: DİMM 150.000 ₺, DİŞ 90.000 ₺, GÜG 120.000 ₺, "
    "pazarlama 60.000 ₺, genel yönetim 80.000 ₺ ve finansman 20.000 ₺. Dönemde başlanan ürünlerin tamamı "
    "bitirilmiş ve üretilen mamullerin %80’i satılmıştır.\n\nBu dönemin gelir tablosunda gider olarak yer alacak "
    "toplam tutar kaç ₺’dir?",
    tl(gelir_tablosu), secenekler(gelir_tablosu, 520_000, 360_000, 288_000, 432_000),
    "Üretim maliyeti 360.000 ₺’nin %80’i (288.000 ₺) satılan mamuller maliyeti olarak gider yazılır, kalan 72.000 ₺ "
    "stokta kalır. Dönem giderleri (60.000 + 80.000 + 20.000 = 160.000 ₺) doğrudan gider yazılır. Toplam 448.000 ₺.",
    topic=MT)

T3.q(R,
    "Bir işletmede fabrika binası kirası üretim miktarından bağımsız olarak her ay 50.000 ₺ ödenmektedir. Üretim "
    "4.000 birimden 5.000 birime çıktığında kira tutarı değişmemiştir.\n\nÜretim artışının fabrika kirasına etkisi "
    "aşağıdakilerden hangisidir?",
    "Toplam kira aynı kalır, birim kira azalır.",
    ["Toplam kira ve birim başına kira artar.",
     "Toplam kira artar, birim başına kira değişmez.",
     "Toplam kira ve birim başına kira değişmez.",
     "Toplam kira azalır, birim başına kira artar."],
    "Sabit maliyetin toplamı geçerli aralıkta değişmez; birim başına payı ise üretim arttıkça azalır: 50.000 ÷ 4.000 = "
    "12,50 ₺’den 50.000 ÷ 5.000 = 10 ₺’ye düşer.", topic=MT, zorluk="easy")

T3.q("MSUGT 7/A: 740-780",
    "Tekdüzen Muhasebe Sistemi Uygulama Genel Tebliği’nin 7/A seçeneğini uygulayan bir işletmenin yeni muhasebe "
    "personeli, fonksiyon esasına göre gider hesaplarının işlevlerini bir tabloda özetlemiştir. Tablodaki bir "
    "eşleştirme hatalıdır.\n\nAşağıdaki eşleştirmelerden hangisi yanlıştır?",
    "760 hesabı üretim bölümlerinin giderlerini izler.",
    ["740 hesabı hizmet üretim maliyetlerini izler.",
     "750 hesabı araştırma ve geliştirme giderlerini izler.",
     "770 hesabı genel yönetim giderlerini izler.",
     "780 hesabı finansman giderlerini izler."],
    "760 Pazarlama, Satış ve Dağıtım Giderleri hesabı satış fonksiyonuna ait giderleri izler. Üretim bölümlerinin "
    "genel giderleri 730 Genel Üretim Giderleri hesabında izlenir.", topic=MT)

dimm = 45_000 + 310_000 - 52_000 - 18_000
T3.sayisal(R,
    "Bir işletmenin ay başında 45.000 ₺ hammadde ve malzeme stoku vardır; ay içinde 310.000 ₺ alım yapılmış ve ay "
    "sonunda 52.000 ₺ stok kalmıştır. Ay içinde üretime verilen malzemenin 18.000 ₺’si makine yağı ve temizlik "
    "malzemesi gibi mamulle doğrudan ilişkilendirilemeyen yardımcı malzemedir.\n\nAyın direkt ilk madde ve malzeme "
    "gideri kaç ₺’dir?",
    tl(dimm), secenekler(dimm, 303_000, 321_000, 292_000, 355_000),
    "Kullanılan toplam malzeme = 45.000 + 310.000 − 52.000 = 303.000 ₺. Bunun 18.000 ₺’si endirekt malzeme olarak "
    "GÜG’e girer; DİMM = 303.000 − 18.000 = 285.000 ₺.", topic=MU)

T3.q(R,
    "Bir işletmede ay içinde makine arızası nedeniyle üretim işçileri toplam 120 saat çalışamamış, bu sürede de "
    "ücretleri ödenmiştir. Arızalar olağan işletme koşullarında zaman zaman görülmekte ve belirli bir siparişle "
    "ilişkilendirilememektedir.\n\nBu 120 saatlik boş geçen zamana ait ücret nasıl sınıflandırılır?",
    "Genel üretim gideri",
    ["Direkt işçilik gideri", "Olağan dışı gider ve zarar", "Genel yönetim gideri", "Pazarlama gideri"],
    "Olağan işletme koşullarında oluşan ve belirli bir mamulle ilişkilendirilemeyen boş geçen zaman ücretleri "
    "endirekt işçilik olarak genel üretim giderlerine yüklenir ve tüm üretime dağıtılır.", topic=MU)

y1, y2_kendi = 80_000, 40_000
y2 = y2_kendi + y1 * 0.25
a = 200_000 + y1 * 0.45 + y2 * 0.50
assert a == 266_000
T3.sayisal(R,
    "Basamaklı dağıtım yöntemini uygulayan bir işletmede önce Y1, sonra Y2 yardımcı gider yeri dağıtılmaktadır. Y1’in "
    "80.000 ₺’lik gideri Y2’ye %25, A’ya %45, B’ye %30; Y2’nin kendi gideri 40.000 ₺ olup Y1’den aldığı payla "
    "birlikte A ve B’ye eşit olarak dağıtılacaktır. A esas üretim gider yerinin birincil giderleri 200.000 ₺’dir."
    "\n\nDağıtım sonunda A gider yerinin toplam gideri kaç ₺’dir?",
    tl(a), secenekler(a, 256_000, 236_000, 276_000, 296_000),
    "Y1’den A’ya 80.000 × %45 = 36.000 ₺, Y2’ye 20.000 ₺. Y2 toplamı 40.000 + 20.000 = 60.000 ₺; A’nın payı 30.000 "
    "₺. A toplamı = 200.000 + 36.000 + 30.000 = 266.000 ₺.", topic=GD, zorluk="hard")

T3.q(R,
    "Bir işletmenin maliyet muhasebecisi gider dağıtım yöntemlerini karşılaştıran bir not hazırlamıştır. Notun "
    "gözden geçirilmesinde ifadelerden birinin hatalı olduğu anlaşılmıştır.\n\nGider dağıtımıyla ilgili "
    "aşağıdakilerden hangisi yanlıştır?",
    "Doğrudan dağıtımda yardımcı gider yerleri birbirine hizmet payı dağıtır.",
    ["Birinci dağıtımda ortak giderler tüm gider yerlerine paylaştırılır.",
     "Basamaklı dağıtımda dağıtılan gider yerine geri pay verilmez.",
     "Karşılıklı dağıtım yardımcı yerlerin birbirine hizmetlerini dikkate alır.",
     "Dağıtım anahtarı giderin oluşumuyla ilişkili seçilmelidir."],
    "Doğrudan dağıtım yönteminde yardımcı gider yerlerinin birbirine verdiği hizmetler dikkate alınmaz; giderleri "
    "doğrudan esas üretim gider yerlerine aktarılır. Karşılıklı hizmetleri dikkate alan yöntemler basamaklı ve "
    "karşılıklı dağıtımdır.", topic=GD)

dimm_b = (30_000 + 270_000) / 20_000
don_b = (12_000 + 368_000) / (18_000 + 1_000)
tam = 18_000 * (dimm_b + don_b)
assert (dimm_b, don_b, tam) == (15, 20, 630_000)
T3.sayisal(R,
    "Ağırlıklı ortalama yöntemini uygulayan bir safha işletmesinde dönem başında 2.000 birim yarı mamul vardır "
    "(hammadde 30.000 ₺, dönüşüm 12.000 ₺). Dönemde 270.000 ₺ hammadde ve 368.000 ₺ dönüşüm maliyeti katlanılmış, "
    "18.000 birim tamamlanmıştır. Dönem sonunda 2.000 birim yarı mamul hammadde bakımından %100, dönüşüm bakımından "
    "%50 tamamlanmıştır.\n\nTamamlanan ürünlerin maliyeti kaç ₺’dir?",
    tl(tam), secenekler(tam, 612_000, 680_000, 594_000, 648_000),
    "Eşdeğer birimler: hammadde 18.000 + 2.000 = 20.000; dönüşüm 18.000 + 1.000 = 19.000. Birim maliyetler: hammadde "
    "300.000 ÷ 20.000 = 15 ₺, dönüşüm 380.000 ÷ 19.000 = 20 ₺. Tamamlanan = 18.000 × 35 = 630.000 ₺; dönem sonu "
    "yarı mamul 50.000 ₺.", topic=MS, zorluk="hard")

T3.q(R,
    "Sipariş maliyet yöntemini uygulayan bir makine imalatçısında M-5 siparişi ay içinde tamamlanıp depoya "
    "alınmış, henüz müşteriye teslim edilmemiştir. Siparişin maliyet kartında toplanan tutar 385.000 ₺’dir.\n\nM-5 "
    "siparişinin tamamlanmasına ilişkin kayıt için aşağıdakilerden hangisi doğrudur?",
    "152 Mamuller borç, 151 Yarı Mamuller – Üretim alacak",
    ["620 Satılan Mamuller Maliyeti borç, 152 Mamuller alacak",
     "151 Yarı Mamuller – Üretim borç, 152 Mamuller alacak",
     "152 Mamuller borç, 731 GÜG Yansıtma alacak",
     "153 Ticari Mallar borç, 151 Yarı Mamuller – Üretim alacak"],
    "Tamamlanan siparişin maliyeti yarı mamulden mamul hesabına aktarılır: 152 borç, 151 alacak 385.000 ₺. Satış ve "
    "teslim gerçekleştiğinde 620 borç, 152 alacak kaydı yapılır.", topic=MS, zorluk="easy")

k = 420_000 * 300_000 / 420_000
T3.sayisal(R,
    "Bir işletmede 420.000 ₺ ortak maliyetle K ve L ürünleri elde edilmektedir. Ayrılma noktasında K’dan 6.000 kg "
    "(satış fiyatı 50 ₺/kg), L’den 4.000 kg (satış fiyatı 30 ₺/kg) üretilmiştir. Ortak maliyet ayrılma noktasındaki "
    "satış değerleri oranında dağıtılmaktadır.\n\nK ürününe dağıtılacak ortak maliyet kaç ₺’dir?",
    tl(k), secenekler(k, 252_000, 210_000, 120_000, 168_000),
    "Satış değerleri: K 6.000 × 50 = 300.000 ₺, L 4.000 × 30 = 120.000 ₺; toplam 420.000 ₺. K’nın payı = 420.000 × "
    "300.000 ÷ 420.000 = 300.000 ₺. Fiziksel miktar esasıyla K’ya 252.000 ₺ düşerdi.", topic=MS)

T3.q(R,
    "Bir işletmenin maliyet uzmanı, ortak mamul maliyetlemesine ilişkin bir eğitim notu hazırlamıştır. Nottaki "
    "ifadelerden biri hatalıdır.\n\nOrtak mamul maliyetlemesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Ayrılma sonrası ek işlem giderleri ortak maliyete katılıp dağıtılır.",
    ["Ortak maliyet ayrılma noktasına kadar katlanılan maliyettir.",
     "Ortak maliyet fiziksel miktar veya satış değeri esasına göre dağıtılabilir.",
     "Net gerçekleşebilir değer yönteminde ek işlem giderleri satış değerinden düşülür.",
     "Yan ürün maliyeti ortak maliyetten indirilerek ana ürün maliyeti bulunabilir."],
    "Ayrılma noktasından sonraki ek işlem giderleri yalnız ilgili mamule aittir ve doğrudan o mamulün maliyetine "
    "eklenir; ortak maliyete katılıp dağıtılmaz.", topic=MS)

T3.sayisal(R,
    "Bir safha işletmesinde dönemde 5.000 birime başlanmış ve tamamı işlem görmüştür. Sürecin sonundaki kontrolde "
    "250 birimin normal kayıp olduğu belirlenmiş, 4.750 birim sağlam ürün tamamlanmıştır. Dönemin toplam üretim "
    "maliyeti 285.000 ₺’dir ve dönem başı ile sonu yarı mamul stoku yoktur.\n\nSağlam ürünlerin birim maliyeti kaç "
    "₺’dir?",
    tl(285_000 / 4_750), secenekler(60, 57, 63, 54, 66),
    "Normal kayıp maliyeti sağlam ürünlere yüklenir; kayıp birimler eşdeğer birime katılmaz: 285.000 ÷ 4.750 = 60 ₺. "
    "Başlanan birime bölmek (57 ₺) normal kaybı maliyetten çıkarmak olur.", topic=UK, zorluk="easy")

T3.sayisal(R,
    "Bir işletmenin bir birim mamul için hazırladığı standart maliyet kartında şu bilgiler yer almaktadır: DİMM 1,5 kg, "
    "kilogramı 40 ₺; DİŞ 0,75 saat, saati 160 ₺; GÜG direkt işçilik saatine göre saat başına 56 ₺ (değişken ve sabit "
    "toplamı).\n\nBir birim mamulün standart maliyeti kaç ₺’dir?",
    tl(1.5 * 40 + 0.75 * 160 + 0.75 * 56), secenekler(222, 236, 180, 256, 276),
    "DİMM = 1,5 × 40 = 60 ₺; DİŞ = 0,75 × 160 = 120 ₺; GÜG = 0,75 × 56 = 42 ₺. Standart maliyet = 60 + 120 + 42 = 222 "
    "₺.", topic=SM, zorluk="easy")

T3.q(R,
    "Bir işletme DİMM fiyat farkını, malzemenin üretimde kullanıldığı anda değil satın alındığı anda ayırmaya karar "
    "vermiştir. Böylece hammadde stokları standart fiyatla izlenecektir. Satın alma müdürü bu değişikliğin "
    "gerekçesini sormaktadır.\n\nFiyat farkının satın alma anında ayrılmasının temel yararı aşağıdakilerden "
    "hangisidir?",
    "Fiyat sapması erken belirlenip sorumlusuna raporlanır.",
    ["Miktar farkı ortadan kalkar ve üretim kontrolü kolaylaşır.",
     "Stoklar fiili maliyetle değerlendiği için TMS 2 uygulanmaz.",
     "Fiyat farkı dönem sonuna kadar hesaplanmadan bekletilir.",
     "Satın alınan malzeme miktarı standart miktara eşitlenir."],
    "Fiyat farkı satın alma anında ayrılırsa sapma kullanım beklenmeden ortaya çıkar ve satın alma birimine hemen "
    "raporlanır; stoklar da standart fiyatla izlendiğinden kayıtlar kolaylaşır. Miktar farkı ayrıca hesaplanır.",
    topic=SM)

k, v = 30 * (10_000 - 9_700), (9_700 - 9_400) * 50
assert (k, v) == (9_000, 15_000)
T3.q(R,
    "Bir işletmede normal kapasite 10.000 makine saati, sabit GÜG bütçesi 300.000 ₺ ve değişken GÜG oranı makine saati "
    "başına 20 ₺’dir. Ay içinde fiili üretim için standart süre 9.400 saat olmuş, fiilen 9.700 saat çalışılmıştır."
    "\n\nÜçlü analize göre GÜG verimlilik ve kapasite farkları sırasıyla aşağıdakilerden hangisidir?",
    "15.000 ₺ olumsuz; 9.000 ₺ olumsuz",
    ["9.000 ₺ olumsuz; 15.000 ₺ olumsuz", "6.000 ₺ olumsuz; 9.000 ₺ olumsuz", "15.000 ₺ olumsuz; 18.000 ₺ olumsuz",
     "15.000 ₺ olumlu; 9.000 ₺ olumlu"],
    "Standart oran = 300.000 ÷ 10.000 + 20 = 50 ₺. Verimlilik farkı = (9.700 − 9.400) × 50 = 15.000 ₺ olumsuz; "
    "kapasite farkı = 30 × (10.000 − 9.700) = 9.000 ₺ olumsuz.", topic=SM, zorluk="hard")

etki = 1_000 * (85 - 62) - 5_000
T3.sayisal(R,
    "Atıl kapasitesi bulunan bir işletmeye 1.000 birimlik tek seferlik bir sipariş gelmiştir. Siparişin birim fiyatı "
    "85 ₺’dir; ürünün birim değişken maliyeti 62 ₺, birim tam maliyeti 80 ₺’dir. Sipariş için 5.000 ₺ özel kalıp "
    "gideri doğacak, normal satışlar etkilenmeyecektir.\n\nSiparişin kabulü işletme kârını kaç ₺ artırır?",
    tl(etki), secenekler(etki, 23_000, 5_000, 28_000, 13_000),
    "Atıl kapasitede sabit maliyetler değişmez. Siparişin katkısı = 1.000 × (85 − 62) = 23.000 ₺; kalıp gideri "
    "düşülünce kâr 18.000 ₺ artar. Tam maliyetle hesaplamak (1.000 × 5 − 5.000 = 0) yanlış karar verdirir.",
    lesson=YM, topic="karar_verme")

esnek = 210_000 + 24 * 7_500
T3.sayisal(R,
    "Bir işletme GÜG bütçesini 8.000 birim üretime göre hazırlamıştır; değişken GÜG birim başına 24 ₺, sabit GÜG "
    "210.000 ₺’dir. Ay içinde fiilen 7.500 birim üretilmiş ve 398.000 ₺ GÜG gerçekleşmiştir.\n\nFiili üretim "
    "düzeyine göre esnek bütçe tutarı kaç ₺’dir?",
    tl(esnek), secenekler(esnek, 402_000, 376_875, 180_000, 398_000),
    "Esnek bütçe = 210.000 + 24 × 7.500 = 390.000 ₺. Harcama sapması 398.000 − 390.000 = 8.000 ₺ olumsuzdur. Statik "
    "bütçenin (402.000 ₺) hacimle orantılı küçültülmesi 376.875 ₺ verir ve sabit gideri değişken sayar.",
    lesson=YM, topic="butceleme_planlama_kontrol")

T3.q("MSUGT 7/A: yansıtma hesapları",
    "Tekdüzen Muhasebe Sistemi Uygulama Genel Tebliği’nin 7/A seçeneğinde her fonksiyonel gider hesabının karşısında "
    "bir yansıtma hesabı bulunmaktadır (711, 721, 731, 761, 771 gibi). Yeni bir muhasebe elemanı bu hesapların neden "
    "kullanıldığını sormaktadır.\n\nYansıtma hesaplarının işlevi aşağıdakilerden hangisidir?",
    "Giderlerin maliyet ya da sonuç hesaplarına aktarımını göstermek",
    ["Giderlerin çeşit esasına göre izlenmesini sağlamak",
     "Dönem sonu gider tahakkuklarını bilançoda göstermek",
     "Gider hesaplarındaki hataları düzeltmek için ters kayıt yapmak",
     "Giderlerin vergi matrahından indirilemeyen kısmını ayırmak"],
    "Yansıtma hesapları, fonksiyon hesaplarında toplanan giderlerin maliyet (151) veya dönem sonucu (63) hesaplarına "
    "aktarıldığını gösterir (satış ve yönetim giderleri 63, finansman giderleri 66 grubuna); gider hesaplarının tutarı değişmeden bakiyeleri dönem sonunda karşılıklı kapatılır.",
    topic=MT)

gug = 1_440_000 / 48_000 * 320
T3.sayisal(R,
    "Sipariş maliyet yöntemini uygulayan bir işletme yıl başında genel üretim giderlerini 1.440.000 ₺, direkt işçilik "
    "saatini 48.000 saat olarak tahmin etmiş ve GÜG’ü bu tahminlerle belirlenen oranla yüklemektedir. Ay içinde "
    "tamamlanan S-21 siparişinde 320 direkt işçilik saati çalışılmış, siparişin fiili GÜG payı ise 10.400 ₺ olarak "
    "hesaplanmıştır.\n\nS-21 siparişine yüklenecek GÜG kaç ₺’dir?",
    tl(gug), secenekler(gug, 10_400, 800, 14_400, 30),
    "Önceden belirlenmiş oran = 1.440.000 ÷ 48.000 = 30 ₺/saat. Siparişe yüklenen GÜG = 320 × 30 = 9.600 ₺. Fiili "
    "pay ile yüklenen arasındaki fark dönem sonunda eksik/fazla yükleme olarak ele alınır.", topic=MU)

T3.q(R,
    "Bir işletmede tornalama, montaj ve boyama bölümlerinde doğrudan mamul üretimi yapılmakta; bakım-onarım ve "
    "enerji bölümleri ise bu bölümlere hizmet vermektedir. İşletme genel müdürlüğü ve satış ofisi ayrı binalarda "
    "bulunmaktadır.\n\nTornalama bölümü gider yeri olarak nasıl sınıflandırılır?",
    "Esas üretim gider yeri",
    ["Yardımcı üretim gider yeri", "Yardımcı hizmet gider yeri", "Genel yönetim gider yeri",
     "Pazarlama gider yeri"],
    "Mamulün doğrudan üretildiği bölümler esas üretim gider yeridir. Bakım-onarım ve enerji yardımcı üretim gider "
    "yerleri, genel müdürlük ve satış ofisi ise üretim dışı (yönetim ve pazarlama) gider yerleridir.",
    topic=GD, zorluk="easy")

for p_ in (T1, T2, T3):
    p_.serpistir()

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
