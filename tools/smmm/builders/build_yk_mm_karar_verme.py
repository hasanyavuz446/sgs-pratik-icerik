# -*- coding: utf-8 -*-
"""Yönetim Muhasebesi · Karar Verme — 60 soru, 2026 test biçimi.

İlgili maliyet (batık, fırsat, kaçınılabilir, artan maliyet); özel sipariş (atıl ve tam kapasite); üretme veya
satın alma; bölüm/ürün hattı kapatma; ortak ürünlerde ayrılma noktasında satma veya ileri işleme; ekipman
yenileme; kısıtlı kaynak altında ürün karması; beklenen değer ve fiyatlandırma kararları gerçek kitapçıklardaki
gibi tutar veren olaylarla sorulur.

Dayanak: ilgili maliyet ve artan (diferansiyel) analiz yaklaşımının genel kabul görmüş esasları; paranın zaman
değeri yalnız kökte ihmal edildiği belirtilen kısa dönemli karşılaştırmalarda dışarıda bırakılır. Tutarlar
builder içinde hesaplanır; her seçenek karşılaştırması ayrı toplamlarla denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_karar_verme_2026.json", lesson="yonetim_muhasebesi", topic="karar_verme",
          konu_adi="Karar Verme", seed=2026093088,
          surum="İlgili maliyet ve artan analiz esasları; 30.09.2026 kontrolü")

IM = "İlgili maliyet kavramları"
OS = "Özel sipariş kararları"
US = "Üretme veya satın alma kararları"
BK = "Bölüm ve ürün hattı kararları"
II = "Satma veya ileri işleme kararları"
KK = "Kısıtlı kaynak ve ürün karması"
BD = "Belirsizlik ve fiyatlandırma kararları"


def birim(x):
    return f"{tl(x)} birim"


# ------------------------------------------------------------------ ilgili maliyet
P.q(IM,
    "Bir işletmenin yönetim kurulu, iki üretim yöntemi arasında seçim yaparken hangi maliyet kalemlerinin analize "
    "alınacağını tartışmaktadır. Listede geçen yıl ödenmiş danışmanlık bedeli, her iki yöntemde aynı olacak fabrika "
    "kirası ve yöntemlere göre farklılaşacak enerji gideri yer almaktadır.\n\nBir maliyet kaleminin bu karar için "
    "ilgili sayılabilmesi hangi iki niteliği birlikte taşımasına bağlıdır?",
    "Gelecekte doğması ve seçenekler arasında farklılık göstermesi",
    ["Geçmişte ödenmiş olması ve muhasebe kayıtlarında yer alması",
     "Sabit nitelikte olması ve tüm seçeneklerde aynı kalması",
     "Nakit çıkışı gerektirmesi ve vergi matrahından indirilmesi",
     "Doğrudan üretimle ilgili olması ve mamul maliyetine girmesi"],
    "Bir maliyet, ancak gelecekte doğacaksa ve seçeneklere göre farklılaşıyorsa karar için ilgilidir. Geçmişte "
    "ödenmiş danışmanlık bedeli batık maliyet, her iki yöntemde aynı olan kira ise farklılaşmayan maliyettir.",
    zorluk="easy")

P.q(IM,
    "Bir matbaa beş yıl önce 900.000 ₺’ye aldığı baskı makinesini yenilemeyi düşünmektedir. Makinenin kayıtlı "
    "defter değeri 360.000 ₺, bugünkü satış değeri ise 110.000 ₺’dir. Muhasebe müdürü, defter değerinin yenileme "
    "kararında zarar olarak dikkate alınması gerektiğini ileri sürmektedir.\n\nMakinenin defter değeri yenileme "
    "kararında nasıl ele alınır?",
    "Batık maliyettir; karar analizine alınmaz.",
    ["Yeni makinenin maliyetine eklenerek karşılaştırılır.",
     "Fırsat maliyetidir; eski makineyi tutma seçeneğine eklenir.",
     "Kaçınılabilir maliyettir; yenilemede tasarruf sayılır.",
     "Satış değeriyle arasındaki fark yeni makineye yüklenir."],
    "Defter değeri geçmişte yapılmış harcamanın henüz amortismana ayrılmamış kısmıdır; hangi seçenek seçilirse "
    "seçilsin değişmez ve batık maliyettir. Bugünkü satış değeri (110.000 ₺) ise yenileme seçeneğinde ilgili nakit "
    "girişidir.")

P.q(IM,
    "Bir işletme kendi deposunu yeni bir ürünün stoklanması için kullanmayı planlamaktadır. Depo boş durmakta olup "
    "bir lojistik firması depoyu aylık 45.000 ₺ bedelle kiralamayı teklif etmiştir. Deponun aylık amortismanı 12.000 "
    "₺’dir.\n\nYeni ürün kararında depo kullanımı için dikkate alınması gereken maliyet aşağıdakilerden hangisidir?",
    "Aylık 45.000 ₺ fırsat maliyeti",
    ["Aylık 12.000 ₺ amortisman gideri", "Aylık 57.000 ₺ toplam depo maliyeti", "Aylık 33.000 ₺ net kira farkı",
     "Depo işletmenin olduğundan maliyet yoktur"],
    "Depo yeni ürün için kullanılırsa vazgeçilecek kira geliri (45.000 ₺) fırsat maliyetidir ve karara girer. "
    "Amortisman her iki durumda da oluşacağından ilgisizdir.")

P.q(IM,
    "Bir yönetim muhasebesi eğitiminde katılımcılara ilgili maliyet kavramlarıyla ilgili ifadeler dağıtılmış, "
    "hatalı olanı bulmaları istenmiştir.\n\nİlgili maliyet analiziyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Batık maliyetler seçenekler arasında dağıtılarak karara dâhil edilir.",
    ["Fırsat maliyeti muhasebe kayıtlarında yer almasa da karara girer.",
     "Tüm seçeneklerde aynı olan gelecek maliyetler karşılaştırmayı etkilemez.",
     "Kaçınılabilir sabit maliyetler ilgili maliyet olabilir.",
     "Nitel faktörler sayısal sonucun yanında değerlendirilmelidir."],
    "Batık maliyetler geçmişte katlanılmış ve değiştirilemez maliyetlerdir; hiçbir seçeneği etkilemediklerinden "
    "karara dâhil edilmezler. Diğer ifadeler ilgili maliyet yaklaşımına uygundur.")

P.q(IM,
    "Bir işletme bir ürün hattının kapatılmasını değerlendirirken maliyetleri sınıflandırmaktadır. Hattın ustabaşı "
    "maaşı hat kapatılınca ortadan kalkacak, fabrika müdürünün maaşı ise değişmeyecektir.\n\nUstabaşı maaşı bu "
    "karar bakımından nasıl sınıflandırılır?",
    "Kaçınılabilir maliyet",
    ["Kaçınılamaz sabit maliyet", "Batık maliyet", "Değişken maliyet", "Ortak maliyet"],
    "Belirli bir seçenek uygulandığında ortadan kalkan maliyetler kaçınılabilir maliyettir; ustabaşı maaşı sabit "
    "nitelikte olsa da hat kapatılınca kalktığı için ilgilidir. Fabrika müdürünün maaşı kaçınılamaz maliyettir.",
    zorluk="easy")

P.sayisal(IM,
    "Bir işletmenin aylık toplam üretim maliyeti 10.000 birimlik üretimde 820.000 ₺, 12.000 birimlik üretimde "
    "950.000 ₺’dir. Yönetim üretimi 12.000 birime çıkarmanın ek maliyetini, gelecek ay beklenen ek satış geliriyle "
    "karşılaştıracaktır.\n\nÜretim artışının artan (diferansiyel) maliyeti kaç ₺’dir?",
    tl(130_000), secenekler(130_000, 950_000, 164_000, 65_000, 1_770_000),
    "Artan maliyet iki seçenek arasındaki toplam maliyet farkıdır: 950.000 − 820.000 = 130.000 ₺ (ek birim başına "
    "65 ₺). Ortalama birim maliyetle (82 ₺ × 2.000 = 164.000 ₺) hesaplamak sabit maliyetleri de artıyor sayar.",
    zorluk="easy")

P.sayisal(IM,
    "Bir işletmenin stokunda geçmiş maliyeti 70.000 ₺ olan bir malzeme bulunmaktadır. Malzeme bugün olduğu gibi "
    "52.000 ₺ net bedelle satılabilir. Yönetim bu malzemeyi, aksi hâlde başka bir amaçla kullanmayacağı yeni bir "
    "müşteri siparişinde kullanmayı düşünmektedir.\n\nSipariş kararında malzemenin ilgili maliyeti kaç ₺’dir?",
    tl(52_000), secenekler(52_000, 70_000, 18_000, 122_000, 35_000),
    "Malzeme siparişte kullanılırsa vazgeçilecek net satış değeri (52.000 ₺) fırsat maliyetidir ve ilgili maliyettir. "
    "Geçmiş maliyet 70.000 ₺ batık olduğundan karara girmez.")

hesap = 28_000 + 36_000 + 9_000
etki = 151_200 - hesap
P.sayisal(IM,
    "Bir işletme tek seferlik bir sözleşmeden 151.200 ₺ gelir elde edebilecektir. Sözleşme için; stokta bulunan ve "
    "defter değeri 40.000 ₺, bugünkü satış değeri 28.000 ₺ olan malzeme, ayrıca 36.000 ₺’lik yeni malzeme, atıl "
    "durumdaki kadrolu işçilerin 22.000 ₺’lik ücreti, 9.000 ₺ fazla mesai ve 18.000 ₺ dağıtılmış genel gider "
    "kullanılacaktır.\n\nSözleşmenin işletme kârına etkisi kaç ₺’dir?",
    tl(etki), secenekler(etki, 151_200 - 40_000 - 36_000 - 9_000, 151_200 - hesap - 22_000,
                         151_200 - 28_000 - 36_000 - 22_000 - 9_000 - 18_000, 151_200 - 36_000),
    "İlgili maliyetler: stok malzemenin satış değeri 28.000 ₺ (fırsat maliyeti), yeni malzeme 36.000 ₺ ve fazla mesai "
    "9.000 ₺; toplam 73.000 ₺. Kadrolu işçi ücreti her durumda ödenecek, dağıtılmış genel gider değişmeyecektir. Kâr "
    "etkisi = 151.200 − 73.000 = 78.200 ₺ artış.", zorluk="hard")

# ------------------------------------------------------------------ özel sipariş
etki = 2_000 * (58 - 42 - 2) - 8_000
P.sayisal(OS,
    "Atıl kapasitesi bulunan bir işletmeye 2.000 birim için birim fiyatı 58 ₺ olan tek seferlik bir sipariş "
    "gelmiştir. Birim maliyetler: DİMM 24 ₺, DİŞ 12 ₺, değişken GÜG 6 ₺ ve sabit GÜG payı 10 ₺ (tam maliyet 52 ₺). "
    "Sipariş için birim başına 2 ₺ özel ambalaj ve toplam 8.000 ₺ kalıp hazırlık gideri doğacaktır; normal satışlar "
    "etkilenmeyecektir.\n\nSiparişin kabulü işletme kârını kaç ₺ artırır?",
    tl(etki), secenekler(etki, 28_000, 32_000, 4_000, 12_000),
    "Atıl kapasitede sabit GÜG değişmez ve ilgisizdir. Birim ilgili maliyet = 24 + 12 + 6 + 2 = 44 ₺; katkı = 2.000 × "
    "(58 − 44) = 28.000 ₺; kalıp gideri düşülünce kâr 20.000 ₺ artar.")

sip = 800 * (90 - 55)
kayip = 800 * (110 - 55)
assert sip - kayip == -16_000
P.q(OS,
    "Tam kapasiteyle çalışan bir işletmeye 800 birimlik, birim fiyatı 90 ₺ olan bir özel sipariş teklif edilmiştir. "
    "Ürünün normal satış fiyatı 110 ₺, birim değişken maliyeti 55 ₺’dir. Sipariş kabul edilirse aynı miktarda normal "
    "satıştan vazgeçilecektir; sabit maliyetler değişmeyecektir.\n\nSiparişin kabulü ile ilgili aşağıdakilerden "
    "hangisi doğrudur?",
    "Kâr 16.000 ₺ azalır; sipariş reddedilmelidir.",
    ["Kâr 28.000 ₺ artar; sipariş kabul edilmelidir.",
     "Kâr 44.000 ₺ azalır; sipariş reddedilmelidir.",
     "Kâr 16.000 ₺ artar; sipariş kabul edilmelidir.",
     "Kâr değişmez; sipariş nitel faktörlere göre değerlendirilir."],
    "Siparişin katkısı 800 × (90 − 55) = 28.000 ₺; vazgeçilen normal satışların katkısı 800 × (110 − 55) = 44.000 ₺. "
    "Net etki 16.000 ₺ azalıştır. Tam kapasitede kaybedilen katkı siparişin fırsat maliyetidir.")

en_dusuk = 34 + 4 + 12_000 / 1_500
P.sayisal(OS,
    "Atıl kapasitesi bulunan bir işletme 1.500 birimlik tek seferlik bir ihracat siparişi için fiyat teklifi "
    "hazırlamaktadır. Birim değişken üretim maliyeti 34 ₺, birim başına ek taşıma gideri 4 ₺’dir. Sipariş için "
    "toplam 12.000 ₺ özel belgelendirme gideri doğacak, sabit üretim giderleri değişmeyecektir.\n\nSiparişin kârı "
    "azaltmaması için teklif edilebilecek en düşük birim fiyat kaç ₺’dir?",
    tl(en_dusuk), secenekler(en_dusuk, 38, 34, 42, 54),
    "En düşük fiyat siparişe özgü tüm ilgili maliyetleri karşılamalıdır: 34 + 4 + 12.000 ÷ 1.500 = 34 + 4 + 8 = 46 "
    "₺. Değişmeyen sabit üretim giderleri ilgisizdir.")

P.sayisal(OS,
    "Tam kapasiteyle çalışan bir işletme, bir özel siparişi karşılamak için her birimde normal satışlardan "
    "vazgeçecektir. Normal satışların birim katkı payı 19 ₺’dir. Siparişin birim değişken üretim maliyeti 48 ₺ olup "
    "siparişe özgü başka maliyet yoktur.\n\nSiparişin kârı azaltmaması için gereken en düşük birim fiyat kaç "
    "₺’dir?",
    tl(48 + 19), secenekler(67, 48, 19, 86, 58),
    "Tam kapasitede en düşük fiyat = birim değişken maliyet + vazgeçilen birim katkı (fırsat maliyeti) = 48 + 19 = "
    "67 ₺.", zorluk="easy")

kat = 500 * (66 - 46)
kayip = (500 - 300) * (80 - 46)
assert kat - kayip == 3_200
P.sayisal(OS,
    "Bir işletmenin 300 birimlik atıl kapasitesi vardır. Bir müşteri 500 birimlik ve birim fiyatı 66 ₺ olan tek "
    "seferlik bir sipariş vermek istemektedir; sipariş bölünemez. Ürünün normal satış fiyatı 80 ₺, birim değişken "
    "maliyeti 46 ₺’dir. Atıl kapasiteyi aşan miktar için normal satışlardan vazgeçilecektir.\n\nSiparişin kabulü "
    "işletme kârını kaç ₺ artırır?",
    tl(kat - kayip), secenekler(kat - kayip, 10_000, 6_800, 4_000, 16_800),
    "Siparişin katkısı = 500 × (66 − 46) = 10.000 ₺. Atıl kapasiteyi aşan 200 birim için vazgeçilen katkı = 200 × "
    "(80 − 46) = 6.800 ₺. Net etki = 10.000 − 6.800 = 3.200 ₺ artış.", zorluk="hard")

P.q(OS,
    "Bir işletmenin satış müdürü, atıl kapasitenin bulunduğu bir dönemde gelen özel siparişi değerlendirirken "
    "kullanılacak ilkeleri bir not hâlinde hazırlamıştır. Notta bir hatalı ilke bulunmaktadır.\n\nÖzel sipariş "
    "kararlarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Atıl kapasitede siparişin sabit GÜG payı ilgili maliyet olarak fiyattan düşülür.",
    ["Atıl kapasitede siparişin değişken maliyetleri ilgili maliyettir.",
     "Tam kapasitede vazgeçilen satışların katkı payı fırsat maliyetidir.",
     "Siparişe özgü ek sabit giderler karara dâhil edilir.",
     "Düşük fiyatın mevcut müşterilere etkisi ayrıca değerlendirilir."],
    "Atıl kapasitede sabit GÜG sipariş kabul edilse de edilmese de değişmez; birime dağıtılmış sabit GÜG payı "
    "ilgisizdir. Diğer ifadeler özel sipariş analizinin doğru ilkeleridir.")

fiyat = (31 * 2_000 + 14_000 + 10_000) / 2_000
P.sayisal(OS,
    "Atıl kapasitesi bulunan bir işletme 2.000 birimlik tek seferlik bir sözleşme için teklif hazırlamaktadır. Birim "
    "değişken maliyet 31 ₺’dir. Sözleşme için 14.000 ₺ özel kalıp yaptırılacak ve kalıp başka işte "
    "kullanılamayacaktır. Yönetim bu sözleşmeden 10.000 ₺ ek kâr elde etmek istemektedir.\n\nTeklif edilmesi gereken "
    "birim fiyat kaç ₺’dir?",
    tl(fiyat), secenekler(fiyat, 38, 36, 31, 48),
    "Gerekli toplam gelir = 31 × 2.000 + 14.000 + 10.000 = 86.000 ₺; birim fiyat = 86.000 ÷ 2.000 = 43 ₺.")

saat = 900 * 0.40
kayip = (saat - 250) * 45
etki = 900 * (76 - 50) - kayip
assert etki == 18_450
P.sayisal(OS,
    "Bir işletmenin darboğaz makinesinde bu ay 250 saat atıl kapasite vardır. 900 birimlik bir özel siparişin birim "
    "fiyatı 76 ₺, birim değişken maliyeti 50 ₺’dir ve her birim 0,40 makine saati gerektirmektedir. Atıl kapasiteyi "
    "aşan saatler normal üretimden alınacak; normal ürünler makine saati başına 45 ₺ katkı sağlamaktadır.\n\n"
    "Siparişin kabulü işletme kârını kaç ₺ artırır?",
    tl(etki), secenekler(etki, 23_400, 4_950, 11_250, 12_150),
    "Siparişin katkısı = 900 × 26 = 23.400 ₺. Gerekli saat = 900 × 0,40 = 360; atıl 250 saati aşan 110 saat normal "
    "üretimden alınır ve 110 × 45 = 4.950 ₺ katkı kaybedilir. Net etki = 23.400 − 4.950 = 18.450 ₺.", zorluk="hard")

etki = 3_200 * 14 - 4 * 6_500
P.sayisal(OS,
    "Bir işletme atıl kapasitede karşılayabileceği 3.200 birimlik bir özel sipariş almıştır. Sipariş, hazırlık "
    "giderleri dışında birim başına 14 ₺ katkı payı sağlayacaktır. Müşteri teslimatı dört ayrı parti hâlinde "
    "istemekte ve her parti için makinelerin yeniden ayarlanması 6.500 ₺ hazırlık gideri doğurmaktadır.\n\n"
    "Siparişin kabulü işletme kârını kaç ₺ artırır?",
    tl(etki), secenekler(etki, 44_800, 38_300, 26_000, 12_300),
    "Katkı payı = 3.200 × 14 = 44.800 ₺. Parti sayısına bağlı hazırlık gideri = 4 × 6.500 = 26.000 ₺. Net etki = "
    "44.800 − 26.000 = 18.800 ₺ artış.")

P.q(OS,
    "Atıl kapasitesi bulunan bir mobilya üreticisine, normal fiyatının %30 altında ancak birim değişken maliyetin "
    "üzerinde fiyat öneren toplu bir sipariş gelmiştir. Sayısal analiz siparişin kârı artıracağını göstermektedir. "
    "Sipariş veren firma, işletmenin düzenli müşterileriyle aynı bölgede faaliyet göstermektedir.\n\nSiparişin "
    "reddedilmesini haklı kılabilecek durum aşağıdakilerden hangisidir?",
    "Düşük fiyatın düzenli müşterilerin fiyat beklentisini bozması",
    ["Siparişe dağıtılan sabit GÜG payının fiyattan yüksek olması",
     "Siparişin toplam katkısının sıfırdan büyük çıkması",
     "Siparişin atıl kapasiteyle karşılanabilecek olması",
     "Makinelerin geçmiş yıllarda yüksek bedelle alınmış olması"],
    "Özel sipariş kararında nitel faktörler de önemlidir; düşük fiyatın duyulması düzenli müşterilerin indirim "
    "talep etmesine ve uzun dönemde kârın azalmasına yol açabilir. Dağıtılmış sabit GÜG ve geçmiş maliyetler "
    "ilgisizdir.")

# ------------------------------------------------------------------ üretme veya satın alma
uret = 6_000 * 26 + 48_000
al = 6_000 * 36
assert al - uret == 12_000
P.q(US,
    "Bir işletme yıllık 6.000 adet kullandığı bir parçayı kendisi üretmektedir. Parçanın birim değişken maliyeti "
    "26 ₺’dir; üretim bırakılırsa 48.000 ₺ sabit giderden kaçınılacak, 30.000 ₺ fabrika amortismanı ise sürecektir. "
    "Bir tedarikçi parçayı adet başına 36 ₺’den sağlamayı teklif etmiştir; serbest kalacak kapasitenin başka "
    "kullanımı yoktur.\n\nBu karar için aşağıdakilerden hangisi doğrudur?",
    "Üretmek 12.000 ₺ avantajlıdır.",
    ["Satın almak 18.000 ₺ avantajlıdır.",
     "Satın almak 12.000 ₺ avantajlıdır.",
     "Üretmek 60.000 ₺ avantajlıdır.",
     "İki seçeneğin maliyeti eşittir."],
    "Üretmenin ilgili maliyeti = 6.000 × 26 + 48.000 = 204.000 ₺; satın alma = 6.000 × 36 = 216.000 ₺. Üretmek "
    "12.000 ₺ avantajlıdır. Sürecek amortisman (30.000 ₺) iki seçenekte de oluştuğundan ilgisizdir; eklenirse "
    "satın alma yanlışlıkla 18.000 ₺ avantajlı görünür.")

en_yuksek = (6_000 * 26 + 48_000 + 30_000) / 6_000
P.sayisal(US,
    "Bir işletme yıllık 6.000 adet ürettiği bir parçanın birim değişken maliyetini 26 ₺, üretim bırakılırsa "
    "kaçınılacak sabit giderleri 48.000 ₺ olarak hesaplamıştır. Parça satın alınırsa serbest kalan alan bir başka "
    "firmaya yıllık 30.000 ₺’ye kiralanabilecektir.\n\nİşletmenin parçayı satın almayı kabul edebileceği en yüksek "
    "birim fiyat kaç ₺’dir?",
    tl(en_yuksek), secenekler(en_yuksek, 36, 34, 26, 44),
    "Üretmenin ilgili maliyeti 6.000 × 26 + 48.000 = 204.000 ₺’dir; üretime devam edilirse 30.000 ₺ kira gelirinden "
    "vazgeçilir. Toplam 234.000 ₺ ÷ 6.000 = 39 ₺’nin altındaki her dış fiyat satın almayı avantajlı kılar.",
    zorluk="hard")

P.q(US,
    "Bir işletme bir parçayı dışarıdan satın alma teklifini değerlendirmektedir. Maliyet raporunda parçaya ilişkin "
    "kalemler; direkt malzeme, direkt işçilik, değişken GÜG, parça hattının ustabaşı maaşı ve fabrika binasından "
    "dağıtılan amortisman payı olarak sıralanmıştır. Bina başka bir amaçla kullanılamayacaktır.\n\nÜretme veya satın "
    "alma kararında aşağıdakilerden hangisi ilgili maliyet değildir?",
    "Fabrika binasından dağıtılan amortisman payı",
    ["Parça için kullanılan direkt malzeme", "Parça üretiminin direkt işçilik gideri",
     "Parça üretimindeki değişken GÜG", "Hat kapanınca ortadan kalkacak ustabaşı maaşı"],
    "Bina amortismanı parça satın alınsa da aynen sürecektir; seçenekler arasında farklılaşmadığından ilgisizdir. "
    "Değişken maliyetler ve üretim bırakılınca kalkacak ustabaşı maaşı kaçınılabilir ve ilgilidir.")

P.q(US,
    "Bir işletmenin yaptığı analiz, kritik bir parçanın dışarıdan satın alınmasının yıllık 25.000 ₺ daha ucuz "
    "olduğunu göstermektedir. Ancak tek tedarikçi bulunmakta, sektörde teslimat gecikmeleri sık yaşanmakta ve parça "
    "üretim hattının durmasına yol açabilmektedir.\n\nBu durumda iç üretimin sürdürülmesini destekleyen gerekçe "
    "aşağıdakilerden hangisidir?",
    "Tedarik sürekliliği ve kalite kontrolünün kaybedilme riski",
    ["Parçanın geçmişte yüksek maliyetle üretilmiş olması",
     "İç üretime dağıtılan sabit genel giderlerin tutarının yüksek olması",
     "Satın alma fiyatının değişken maliyetten yüksek olması",
     "Parça üretim makinesinin defter değerinin yüksek olması"],
    "Üretme veya satın alma kararında sayısal sonucun yanında tedarikçinin güvenilirliği, kalite ve teslim "
    "sürekliliği gibi nitel faktörler de değerlendirilir. Geçmiş maliyetler, dağıtılmış sabit giderler ve defter "
    "değeri ilgisizdir.")

al_birim = 25 + 2 + 0.10 * 15
P.sayisal(US,
    "Bir tedarikçi, işletmenin kendisi ürettiği bir parçayı adet başına 25 ₺’den sağlamayı teklif etmiştir. Satın "
    "alınan her parça için 2 ₺ giriş kontrol gideri doğacak ve geçmiş verilere göre parçaların %10’u adet başına 15 "
    "₺ gideri olan yeniden işleme gerektirecektir. İç üretimin birim ilgili maliyeti 27 ₺’dir.\n\nSatın alma "
    "seçeneğinin birim ilgili maliyeti kaç ₺’dir?",
    tl(al_birim), secenekler(al_birim, 27, 25, 42, 30),
    "Satın alma maliyeti = 25 + 2 + 0,10 × 15 = 28,50 ₺. İç üretim (27 ₺) adet başına 1,50 ₺ daha ekonomiktir; "
    "yeniden işlemenin tüm parçalara uygulanması (42 ₺) olasılığı göz ardı eder.")

P.sayisal(US,
    "Bir işletme bir parçayı birim değişken maliyeti 18 ₺ ile üretmekte; üretim bırakılırsa birim başına 4 ₺ "
    "kaçınılabilir sabit giderden kurtulacaktır. Parça satın alınırsa serbest kalan kapasite başka bir ürüne "
    "ayrılacak ve parça başına 3 ₺ ek katkı sağlanacaktır.\n\nİşletmenin parçayı satın almayı kabul edebileceği en "
    "yüksek birim fiyat kaç ₺’dir?",
    tl(18 + 4 + 3), secenekler(25, 22, 18, 21, 29),
    "Üretime devam etmenin birim maliyeti = 18 + 4 = 22 ₺ ve buna vazgeçilen 3 ₺ ek katkı (fırsat maliyeti) eklenir: "
    "22 + 3 = 25 ₺. Bu fiyatın altındaki her teklif satın almayı avantajlı kılar.")

ic = 4_000 * 30 + 20_000
dis = 4_000 * 33
P.sayisal(US,
    "Bir işletme yıllık 4.000 adet bileşeni birim değişken maliyeti 30 ₺ ile üretmekte ve bu üretim için ayrıca "
    "20.000 ₺ kaçınılabilir sabit gidere katlanmaktadır. Maliyet raporunda bileşene birim başına 8 ₺ fabrika genel "
    "gideri de dağıtılmaktadır. Bir tedarikçi bileşeni adet başına 33 ₺’den sağlamayı teklif etmiştir.\n\nTeklif "
    "kabul edilirse işletmenin yıllık kârı kaç ₺ artar?",
    tl(ic - dis), secenekler(ic - dis, 12_000, 20_000, 40_000, 28_000),
    "İç üretimin ilgili maliyeti = 4.000 × 30 + 20.000 = 140.000 ₺; satın alma = 4.000 × 33 = 132.000 ₺. Kâr 8.000 ₺ "
    "artar. Dağıtılan 8 ₺’lik fabrika genel gideri üretim bırakılsa da süreceğinden ilgisizdir; dâhil edilirse "
    "avantaj 40.000 ₺ gibi görünür.")

P.oncul(US,
    "Üretme veya satın alma kararına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Üretim bırakılınca ortadan kalkacak sabit giderler ilgili maliyettir.",
     "Serbest kalan kapasitenin alternatif kullanımından doğan gelir fırsat maliyeti olarak dikkate alınır.",
     "Parçaya dağıtılan ve üretim bırakılsa da sürecek genel giderler ilgili maliyettir.",
     "Tedarikçinin kalite ve teslimat güvenilirliği nitel faktör olarak değerlendirilir."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve II", "I ve III", "II, III ve IV", "I, II ve IV", "I, III ve IV"],
    "I, II ve IV doğrudur. III yanlıştır: üretim bırakılsa da sürecek dağıtılmış genel giderler seçenekler arasında "
    "farklılaşmadığından ilgisizdir.")

P.q(US,
    "Bir hastane, yıllık ilgili iç maliyeti 240.000 ₺ olan temizlik hizmetini dışarıdan almayı düşünmektedir. "
    "Temizlik firmasının yıllık teklifi 220.000 ₺’dir; ancak dış kaynak seçilirse hizmet kalitesini izlemek için "
    "yıllık 30.000 ₺ denetim gideri doğacaktır. Mevcut temizlik personeli başka birimlere kaydırılamayacaktır ve "
    "ücretleri iç maliyete dâhil edilmiştir.\n\nBu karar için aşağıdakilerden hangisi doğrudur?",
    "İç hizmet 10.000 ₺ avantajlıdır.",
    ["Dış kaynak 20.000 ₺ avantajlıdır.",
     "Dış kaynak 10.000 ₺ avantajlıdır.",
     "İç hizmet 30.000 ₺ avantajlıdır.",
     "İki seçeneğin maliyeti eşittir."],
    "Dış kaynağın toplam ilgili maliyeti = 220.000 + 30.000 = 250.000 ₺; iç hizmet 240.000 ₺. İç hizmet 10.000 ₺ "
    "avantajlıdır. Denetim gideri göz ardı edilirse dış kaynak yanlışlıkla 20.000 ₺ avantajlı görünür.")

# ------------------------------------------------------------------ bölüm kararları
P.q(BK,
    "Bir işletmenin C ürün hattı yıllık 150.000 ₺ katkı payı sağlamaktadır. Hat kapatılırsa 110.000 ₺ hatta özgü "
    "sabit giderden kaçınılacaktır. Hatta ayrıca genel merkezden 45.000 ₺ ortak gider dağıtılmakta olup bu gider hat "
    "kapatılsa da diğer hatlara dağıtılacaktır. Raporda hat 5.000 ₺ zararlı görünmektedir.\n\nHattın kapatılmasıyla "
    "ilgili aşağıdakilerden hangisi doğrudur?",
    "İşletme kârı 40.000 ₺ azalır; hat sürdürülmelidir.",
    ["İşletme kârı 5.000 ₺ artar; hat kapatılmalıdır.",
     "İşletme kârı 45.000 ₺ artar; hat kapatılmalıdır.",
     "İşletme kârı 150.000 ₺ azalır; hat sürdürülmelidir.",
     "İşletme kârı değişmez; karar nitel faktörlere bırakılır."],
    "Kapatmada kaybedilecek katkı 150.000 ₺, kaçınılacak sabit gider 110.000 ₺’dir; net etki 40.000 ₺ azalıştır. "
    "Dağıtılmış 45.000 ₺ ortak gider kapatmayla ortadan kalkmadığından ilgisizdir.")

etki = -120_000 + 70_000 + 30_000
assert etki == -20_000
P.q(BK,
    "Bir perakende zincirinin ev tekstili bölümü yıllık 120.000 ₺ katkı payı sağlamaktadır. Bölüm kapatılırsa "
    "70.000 ₺ bölüme özgü sabit giderden kaçınılacak ve boşalan alan bir kafeye yıllık 30.000 ₺’ye kiralanabilecektir. "
    "Diğer bölümlerin satışları etkilenmeyecektir.\n\nBölümün kapatılmasının işletme kârına etkisi aşağıdakilerden "
    "hangisidir?",
    "Kâr 20.000 ₺ azalır.",
    ["Kâr 20.000 ₺ artar.", "Kâr 50.000 ₺ azalır.", "Kâr 80.000 ₺ azalır.", "Kâr 100.000 ₺ artar."],
    "Kapatmanın etkisi = −120.000 (kaybedilen katkı) + 70.000 (kaçınılan sabit gider) + 30.000 (kira geliri) = "
    "−20.000 ₺. Kira geliri dikkate alınmazsa kâr 50.000 ₺ azalıyor görünür.")

P.q(BK,
    "Bir işletmenin yönetim kurulu, zarar ettiği görülen bir bölümün kapatılmasını tartışırken dikkate alınacak "
    "ilkeleri belirlemektedir. Önerilen ilkelerden biri hatalıdır.\n\nBölüm kapatma kararıyla ilgili "
    "aşağıdakilerden hangisi yanlıştır?",
    "Bölüme dağıtılan genel merkez giderleri kapatmada tasarruf sayılır.",
    ["Kapatmayla kaybedilecek katkı payı karşılaştırmaya alınır.",
     "Bölüme özgü kaçınılabilir sabit giderler tasarruf olarak dikkate alınır.",
     "Diğer bölümlerin satışlarına etkisi analize dâhil edilir.",
     "Boşalan kaynakların alternatif kullanımı fırsat olarak değerlendirilir."],
    "Bölüm kapatılsa da genel merkez giderleri çoğunlukla aynı tutarda sürer ve diğer bölümlere dağıtılır; bu "
    "nedenle tasarruf sayılmaz. Diğer ifadeler bölüm kapatma analizinin doğru ilkeleridir.")

P.sayisal(BK,
    "Bir lojistik işletmesi kurumsal müşteri gruplarının kârlılığını incelemektedir. Bir müşteri grubundan yıllık "
    "240.000 ₺ gelir elde edilmekte, bu gruba 155.000 ₺ değişken hizmet maliyeti ve gruba özgü 50.000 ₺ kaçınılabilir "
    "sabit gider (hesap yöneticisi maaşı) katlanılmaktadır. Gruba ayrıca 60.000 ₺ ortak gider dağıtılmaktadır.\n\n"
    "Müşteri grubunun işletme kârına katkısı (segment marjı) kaç ₺’dir?",
    tl(240_000 - 155_000 - 50_000), secenekler(35_000, 85_000, 25_000, 190_000, 95_000),
    "Segment marjı = gelir − değişken maliyet − kaçınılabilir sabit gider = 240.000 − 155.000 − 50.000 = 35.000 ₺. "
    "Ortak gider düşülünce grup 25.000 ₺ zararlı görünür; ancak grup bırakılırsa kâr 35.000 ₺ azalır.")

P.sayisal(BK,
    "Bir işletme yeni bir ürün hattı açmayı değerlendirmektedir. Yeni hat yıllık 180.000 ₺ katkı payı sağlayacak ve "
    "hatta özgü 70.000 ₺ sabit gider doğuracaktır. Pazarlama birimi yeni ürünün mevcut bir ürünün satışlarını bir "
    "miktar azaltacağını ve bu ürünün katkısının yıllık 45.000 ₺ düşeceğini öngörmektedir.\n\nYeni hattın işletme "
    "kârına net etkisi kaç ₺’dir?",
    tl(180_000 - 70_000 - 45_000), secenekler(65_000, 110_000, 180_000, 135_000, 25_000),
    "Net etki = 180.000 − 70.000 − 45.000 = 65.000 ₺ artış. Mevcut ürünün kaybedilen katkısı (yamyamlık etkisi) yeni "
    "hattın ilgili maliyetidir.")

etki = -210_000 + 260_000 - 35_000
assert etki == 15_000
P.q(BK,
    "Talebin geçici olarak düştüğü bir dönemde bir tesis üç ay kapatılabilir. Kapatma süresince 210.000 ₺ katkı "
    "payı kaybedilecek, 260.000 ₺ sabit giderden kaçınılacak ve tesisin yeniden açılması için 35.000 ₺ gider "
    "doğacaktır. Müşteri kaybı beklenmemektedir.\n\nGeçici kapatma kararıyla ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "Kapatma kârı 15.000 ₺ artırır.",
    ["Kapatma kârı 50.000 ₺ artırır.", "Kapatma kârı 15.000 ₺ azaltır.", "Kapatma kârı 35.000 ₺ azaltır.",
     "Kapatma kârı 210.000 ₺ azaltır."],
    "Net etki = −210.000 + 260.000 − 35.000 = 15.000 ₺ artış. Yeniden açılış gideri göz ardı edilirse kazanç 50.000 ₺ "
    "gibi görünür.")

tablo = ("| Ürün hattı | Satış (₺) | Değişken maliyet (₺) | Hatta özgü sabit gider (₺) |\n|---|---|---|---|\n"
         "| A | 500.000 | 300.000 | 80.000 |\n| B | 400.000 | 220.000 | 60.000 |\n| C | 200.000 | 140.000 | 50.000 |")
mevcut = (200_000 - 80_000) + (180_000 - 60_000) + (60_000 - 50_000) - 150_000
yeni = (200_000 - 80_000) + (180_000 - 60_000) - 150_000
assert (mevcut, yeni) == (100_000, 90_000)
P.sayisal(BK,
    "Bir işletmenin üç ürün hattına ait yıllık veriler aşağıdadır; hatlara özgü sabit giderler hat kapatılırsa "
    "ortadan kalkmaktadır:\n\n" + tablo + "\n\nİşletmenin ayrıca 150.000 ₺ ortak sabit gideri vardır ve bu gider "
    "satış hasılatı oranında dağıtıldığında C hattı zararlı görünmektedir.\n\nC hattı kapatılırsa işletmenin "
    "toplam faaliyet kârı kaç ₺ olur?",
    tl(yeni), secenekler(yeni, mevcut, 117_273, 60_000, 240_000),
    "Mevcut kâr = 120.000 + 120.000 + 10.000 − 150.000 = 100.000 ₺. C kapatılırsa 10.000 ₺ segment marjı kaybedilir, "
    "ortak gider aynen kalır: kâr 90.000 ₺ olur. C’ye dağıtılan ortak gider (27.273 ₺) kapatmayla kalkmaz.",
    zorluk="hard")

# ------------------------------------------------------------------ satma veya ileri işleme
fark = (104_000 - 75_000) - 21_000
assert fark == 8_000
P.q(II,
    "Bir kimya işletmesinde ortak üretim sürecinden elde edilen bir ürün, ayrılma noktasında 75.000 ₺ net bedelle "
    "satılabilmektedir. Ürün 21.000 ₺ ek işlem maliyetiyle arıtılırsa 104.000 ₺’ye satılabilecektir. Ayrılma "
    "noktasına kadar bu ürüne dağıtılan ortak maliyet 60.000 ₺’dir.\n\nBu ürünle ilgili karar aşağıdakilerden "
    "hangisidir?",
    "İleri işlenmelidir; kâr 8.000 ₺ artar.",
    ["Ayrılma noktasında satılmalıdır; kâr 8.000 ₺ artar.",
     "İleri işlenmelidir; kâr 29.000 ₺ artar.",
     "Ayrılma noktasında satılmalıdır; ileri işlem 52.000 ₺ zarar doğurur.",
     "İleri işlenmelidir; kâr 23.000 ₺ artar."],
    "İleri işlemenin artan geliri = 104.000 − 75.000 = 29.000 ₺; artan maliyeti 21.000 ₺. Net 8.000 ₺ artış "
    "sağladığından ileri işlenmelidir. Ortak maliyet (60.000 ₺) her iki seçenekte de katlanılmış olduğundan "
    "ilgisizdir.")

P.q(II,
    "Bir süt işletmesinde çiğ sütün işlenmesiyle krema ve yağsız süt ortak ürün olarak elde edilmektedir. Yönetim, "
    "kremayı ayrılma noktasında satmak ya da tereyağına dönüştürmek arasında seçim yaparken ortak işleme maliyetinin "
    "kremaya düşen payını da hesaba katmak istemektedir.\n\nOrtak maliyetin bu kararda ilgisiz olmasının nedeni "
    "aşağıdakilerden hangisidir?",
    "Ortak maliyet her iki seçenekte de aynı tutarda katlanılmıştır.",
    ["Ortak maliyet yağsız süte yüklendiğinden kremanın kararını etkilemez.",
     "Ortak maliyet dönem gideri olduğundan mamul maliyetine girmez.",
     "Ortak maliyet ileri işlem maliyetine eklenerek karşılaştırılır.",
     "Ortak maliyet değişken olduğundan üretim miktarıyla değişir."],
    "Ayrılma noktasına kadarki ortak maliyet, ürün ister o noktada satılsın ister ileri işlensin aynı kalır; "
    "seçenekler arasında farklılaşmadığından karar için ilgisizdir. Kararı yalnız artan gelir ve artan maliyet "
    "belirler.")

P.sayisal(II,
    "Bir işletmenin ortak üretimden elde ettiği A ürününün ileri işlenmesi 64.000 ₺ artan gelir ve 49.000 ₺ artan "
    "maliyet doğurmaktadır. B ürününün ileri işlenmesi ise 45.000 ₺ artan gelir ve 52.000 ₺ artan maliyet "
    "doğurmaktadır. Ortak maliyetler 120.000 ₺’dir ve ürünler birbirinden bağımsız olarak işlenebilir.\n\nEn uygun "
    "kararlar uygulandığında ileri işleme işletme kârını kaç ₺ artırır?",
    tl(15_000), secenekler(15_000, 8_000, 7_000, 64_000, 22_000),
    "A için artan kâr 64.000 − 49.000 = 15.000 ₺ olduğundan ileri işlenir; B için 45.000 − 52.000 = −7.000 ₺ "
    "olduğundan ayrılma noktasında satılır. Kâr artışı 15.000 ₺’dir; ikisi birlikte işlenirse artış 8.000 ₺’ye "
    "düşer.")

P.q(II,
    "Bir işletme ortak üretimden çıkan bir ürünü ayrılma noktasında satmak ya da ek işlemle daha değerli bir ürüne "
    "dönüştürmek arasında seçim yapmaktadır. Maliyet raporunda ürüne ilişkin çeşitli kalemler yer almaktadır.\n\n"
    "Satma veya ileri işleme kararında aşağıdakilerden hangisi dikkate alınmaz?",
    "Ayrılma noktasına kadar oluşan ortak maliyetler",
    ["İleri işlem için katlanılacak ek malzeme ve işçilik",
     "Ayrılma noktasındaki net satış değeri",
     "İleri işlenmiş ürünün satış değeri",
     "İleri işlem için kiralanacak ek ekipman bedeli"],
    "Karar artan analizle verilir: ileri işlenmiş ürünün satış değeri ile ayrılma noktasındaki satış değeri arasındaki "
    "fark, ek işlem maliyetleriyle karşılaştırılır. Ortak maliyetler her iki seçenekte aynı olduğundan dikkate "
    "alınmaz.", zorluk="easy")

P.sayisal(II,
    "Bir işletmede ortak üretimden elde edilen bir ürün ayrılma noktasında kilogram başına 18 ₺’den "
    "satılabilmektedir. Ürün kilogram başına 7 ₺ ek işlem maliyetiyle rafine edilebilir; rafine ürünün satış fiyatı "
    "henüz pazarlık aşamasındadır. Ortak maliyetin kilogram başına payı 11 ₺’dir.\n\nİleri işlemenin kârı "
    "azaltmaması için rafine ürünün kilogram satış fiyatı en az kaç ₺ olmalıdır?",
    tl(18 + 7), secenekler(25, 18, 36, 29, 11),
    "Rafine ürünün fiyatı, vazgeçilen ayrılma noktası satış değerini (18 ₺) ve ek işlem maliyetini (7 ₺) "
    "karşılamalıdır: 18 + 7 = 25 ₺. Ortak maliyet payı (11 ₺) ilgisizdir.")

# ------------------------------------------------------------------ ekipman yenileme ve stok
eski = 4 * 75_000
yeni = 260_000 - 40_000 + 4 * 15_000
assert eski - yeni == 20_000
P.q(IM,
    "Bir işletmenin eski makinesi 4 yıl daha kullanılabilir ve yıllık 75.000 ₺ işletme gideri doğurmaktadır; "
    "defter değeri 120.000 ₺, bugünkü satış değeri 40.000 ₺’dir. Yeni makine 260.000 ₺’ye alınabilir, 4 yıllık "
    "ömrü boyunca yıllık 15.000 ₺ işletme gideri doğurur ve ömür sonunda hurda değeri yoktur. Paranın zaman değeri "
    "ihmal edilmektedir.\n\nBu karar için aşağıdakilerden hangisi doğrudur?",
    "Yeni makine 20.000 ₺ avantajlıdır.",
    ["Eski makine 100.000 ₺ avantajlıdır.",
     "Eski makine 20.000 ₺ avantajlıdır.",
     "Yeni makine 240.000 ₺ avantajlıdır.",
     "Yeni makine 60.000 ₺ avantajlıdır."],
    "Eski makine: 4 × 75.000 = 300.000 ₺. Yeni makine: 260.000 − 40.000 (eski makinenin satış bedeli) + 4 × 15.000 = "
    "280.000 ₺. Yeni makine 20.000 ₺ avantajlıdır. Defter değeri (120.000 ₺) batıktır; karşılaştırmaya eklenirse "
    "eski makine yanlışlıkla 100.000 ₺ avantajlı görünür.", zorluk="hard")

fark = 5_000 * ((34 - 12) - 18)
P.sayisal(IM,
    "Bir işletmenin stokunda birim maliyeti 60 ₺ olan 5.000 adet eski model ürün bulunmaktadır. Ürünler olduğu gibi "
    "adet başına 18 ₺’den bir ikinci el satıcısına satılabilir ya da adet başına 12 ₺ yenileme gideriyle "
    "güncellenerek 34 ₺’den satılabilir.\n\nYenileme seçeneği, olduğu gibi satmaya göre işletme kârını kaç ₺ "
    "artırır?",
    tl(fark), secenekler(fark, 80_000, 90_000, 110_000, 60_000),
    "Olduğu gibi satış 5.000 × 18 = 90.000 ₺; yenileme sonrası net 5.000 × (34 − 12) = 110.000 ₺. Fark 20.000 ₺’dir. "
    "Birim maliyet 60 ₺ batık olduğundan iki seçenekte de dikkate alınmaz.", zorluk="easy")

P.q(IM,
    "Bir işletme iki tedarikçi arasında seçim yapmaktadır. Her iki tedarikçiden alınan malzeme aynı ürüne "
    "dönüşecek, ürün her iki durumda aynı fiyattan satılacak ve fabrika giderleri değişmeyecektir; tedarikçilerin "
    "yalnızca birim fiyatları ve teslim giderleri farklıdır.\n\nİki seçenekte de aynı olan satış geliri ve fabrika "
    "giderleri kararda nasıl ele alınır?",
    "Seçenekleri farklılaştırmadıklarından analiz dışında bırakılabilir.",
    ["Seçeneklere eşit dağıtılarak her iki toplama eklenmelidir.",
     "Satış geliri eklenmeli, fabrika giderleri çıkarılmalıdır.",
     "Batık maliyet sayıldığından fırsat maliyetine dönüştürülür.",
     "Fabrika giderleri eklenmeli, satış geliri çıkarılmalıdır."],
    "Artan analizde yalnız seçenekler arasında farklılaşan gelir ve maliyetler karşılaştırılır. Her iki seçenekte "
    "aynı olan kalemler sonucu değiştirmediğinden dışarıda bırakılabilir; eklenseler de fark değişmez.")

P.q(IM,
    "Bir işletme kendi deposunu stoklarında kullanmaktadır. Bir firma depoyu yıllık 180.000 ₺’ye kiralamak "
    "istemektedir. Depo kiraya verilirse işletme stokları için yıllık 150.000 ₺’ye dış depo kiralayacaktır; "
    "deponun amortismanı ve sigortası her iki durumda da işletmeye aittir.\n\nBu karar için aşağıdakilerden "
    "hangisi doğrudur?",
    "Depoyu kiraya vermek 30.000 ₺ avantajlıdır.",
    ["Kendi deposunu kullanmak 30.000 ₺ avantajlıdır.",
     "Depoyu kiraya vermek 180.000 ₺ avantajlıdır.",
     "Kendi deposunu kullanmak 150.000 ₺ avantajlıdır.",
     "İki seçenek arasında kâr farkı oluşmaz."],
    "Depo kiraya verilirse 180.000 ₺ kira geliri elde edilir, 150.000 ₺ dış depo gideri doğar; net 30.000 ₺ "
    "avantaj oluşur. Kendi deposunu kullanmanın fırsat maliyeti vazgeçilen 180.000 ₺ kira geliridir; amortisman ve "
    "sigorta ilgisizdir.")

# ------------------------------------------------------------------ kısıtlı kaynak
P.q(KK,
    "Bir işletme A ve B ürünlerini aynı darboğaz makinesinde üretmektedir. A ürünü birim başına 4 makine saati "
    "kullanıp 56 ₺, B ürünü 3 makine saati kullanıp 48 ₺ katkı sağlamaktadır. Her iki ürünün talebi makine "
    "kapasitesinin çok üzerindedir.\n\nKâr en çoklanmak isteniyorsa üretimde hangi ürüne öncelik verilmelidir?",
    "B’ye; makine saati başına 16 ₺ katkı sağlar.",
    ["A’ya; birim katkı payı daha yüksektir.",
     "A’ya; makine saati başına 14 ₺ katkı sağlar.",
     "B’ye; birim katkı payı daha düşüktür.",
     "Kapasite iki ürüne eşit bölünmelidir."],
    "Kısıtlı kaynak altında ürünler kısıtlı kaynağın birimi başına katkıya göre sıralanır: A için 56 ÷ 4 = 14 ₺, B "
    "için 48 ÷ 3 = 16 ₺. Birim katkısı düşük olsa da B önceliklidir.")

kalan = 1_800 - 300 * 3
katki = 300 * 48 + kalan / 4 * 56
assert katki == 27_000
P.sayisal(KK,
    "Bir işletmenin darboğaz makinesinde ay içinde 1.800 saat kapasite vardır. A ürünü birim başına 4 saat kullanıp "
    "56 ₺, B ürünü 3 saat kullanıp 48 ₺ katkı sağlamaktadır. B ürününün aylık talebi en çok 300 birimdir; A "
    "ürününün talebi sınırsızdır.\n\nEn uygun ürün karmasında elde edilecek toplam katkı payı kaç ₺’dir?",
    tl(katki), secenekler(katki, 25_200, 28_800, 14_400, 26_400),
    "Saat başına katkı B’de 16 ₺, A’da 14 ₺ olduğundan önce B talebi karşılanır: 300 × 3 = 900 saat, katkı 14.400 ₺. "
    "Kalan 900 saatle 225 birim A üretilir: 12.600 ₺. Toplam 27.000 ₺.", zorluk="hard")

P.q(KK,
    "Bir işletmede ithal hammadde kısıtlıdır ve ay içinde ek alım yapılamamaktadır. C ürünü birim başına 3 kg "
    "hammadde kullanıp 36 ₺, D ürünü 2 kg hammadde kullanıp 28 ₺ katkı payı sağlamaktadır. Diğer kaynaklarda kısıt "
    "yoktur ve iki ürünün talebi de yüksektir.\n\nHammadde kısıtı altında hangi ürüne öncelik verilmelidir?",
    "D’ye; kilogram başına 14 ₺ katkı sağlar.",
    ["C’ye; birim katkı payı daha yüksektir.",
     "C’ye; kilogram başına 12 ₺ katkı sağlar.",
     "D’ye; birim başına daha az hammadde kullanır.",
     "Hammadde iki ürüne eşit dağıtılmalıdır."],
    "Kısıtlı kaynağın birimi başına katkı: C için 36 ÷ 3 = 12 ₺, D için 28 ÷ 2 = 14 ₺. Öncelik kilogram başına daha "
    "fazla katkı sağlayan D’ye verilir; az hammadde kullanması tek başına ölçüt değildir.")

kalan = 2_400 - 800 * 2
katki = 800 * 22 + kalan / 5 * 30
assert katki == 22_400
P.sayisal(KK,
    "Bir işletmenin ay içinde kullanabileceği hammadde 2.400 kg ile sınırlıdır. E ürünü birim başına 5 kg hammadde "
    "kullanıp 30 ₺, F ürünü 2 kg hammadde kullanıp 22 ₺ katkı sağlamaktadır. F ürününün talebi en çok 800 birim, E "
    "ürününün talebi sınırsızdır.\n\nEn uygun ürün karmasında elde edilecek toplam katkı payı kaç ₺’dir?",
    tl(katki), secenekler(katki, 26_400, 14_400, 17_600, 20_000),
    "Kilogram başına katkı F’de 11 ₺, E’de 6 ₺’dir. Önce F talebi karşılanır: 800 × 2 = 1.600 kg, katkı 17.600 ₺. "
    "Kalan 800 kg ile 160 birim E üretilir: 4.800 ₺. Toplam 22.400 ₺.")

P.sayisal(KK,
    "Bir işletmede darboğaz makinesinde P ve R ürünleri üretilmektedir. P ürünü birim başına 6 saat kullanıp 90 ₺, R "
    "ürünü 4 saat kullanıp 72 ₺ katkı sağlamaktadır. R ürününün talebinin tamamı karşılanmış, kalan kapasite P "
    "ürününe ayrılmıştır; P’nin talebi karşılanamamaktadır.\n\nDarboğaz makinesine eklenecek bir saatlik kapasite "
    "işletmeye en fazla kaç ₺ ek katkı sağlar?",
    tl(90 / 6), secenekler(15, 18, 90, 72, 16.5),
    "R’nin talebi zaten karşılandığından ek saat P üretimine gider ve P’nin saat başına katkısını (90 ÷ 6 = 15 ₺) "
    "sağlar. Bu tutar ek kapasite için ödenebilecek saat başı bedelin üst sınırıdır.", zorluk="hard")

P.sayisal(KK,
    "Bir işletmenin darboğaz makinesinde bir saat, karşılanmamış talebi bulunan üründe 16 ₺ katkı payı "
    "yaratmaktadır. Bir taşeron, 400 makine saatlik ek kapasiteyi toplam 4.800 ₺ bedelle sağlamayı teklif etmiştir; "
    "başka bir maliyet doğmayacaktır.\n\nTeklifin kabulü işletme kârını kaç ₺ artırır?",
    tl(400 * 16 - 4_800), secenekler(1_600, 6_400, 4_800, 11_200, 1_200),
    "Ek kapasitenin katkısı = 400 × 16 = 6.400 ₺. Bedel 4.800 ₺ olduğundan kâr 1.600 ₺ artar; saat başı bedel (12 ₺) "
    "saat başı katkının (16 ₺) altındadır.")

P.q(KK,
    "Bir üretim müdürü, kısıtlı kaynak altında ürün karması kararına ilişkin ilkeleri ekibine anlatmaktadır. "
    "Anlatılan ilkelerden biri hatalıdır.\n\nKısıtlı kaynak altında ürün karmasıyla ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Ürünler birim katkı payı en yüksekten başlanarak sıralanır.",
    ["Tek bir kısıt varsa ürünler kısıt birimi başına katkıya göre sıralanır.",
     "Talep sınırı olan ürünün talebi karşılandıktan sonra kalan kapasite sıradakine ayrılır.",
     "Darboğaz dışındaki kaynaklardaki verim artışı toplam çıktıyı artırmayabilir.",
     "Ek kapasitenin değeri, sıradaki ürünün kısıt birimi başına katkısıyla ölçülür."],
    "Kısıtlı kaynak varken ölçüt birim katkı payı değil, kısıtlı kaynağın birimi (saat, kg) başına katkıdır. Birim "
    "katkısı yüksek ürün kısıtlı kaynağı çok kullanıyorsa daha az kârlı olabilir.")

P.q(KK,
    "Bir işletmede üretim beş istasyondan geçmekte ve boyama istasyonu darboğaz oluşturmaktadır. Yönetim, "
    "darboğaz olmayan kesim istasyonunda verimliliği %20 artıran yeni bir yöntem uygulamıştır. Talep, mevcut "
    "çıktının üzerindedir.\n\nBu uygulamanın toplam çıktıya etkisi aşağıdakilerden hangisidir?",
    "Darboğaz değişmediği için toplam çıktı artmaz.",
    ["Toplam çıktı %20 oranında artar.",
     "Boyama istasyonunun kapasitesi %20 artar.",
     "Kesim istasyonu darboğaz hâline gelir.",
     "Toplam çıktı kesim ve boyama ortalamasıyla artar."],
    "Toplam çıktıyı darboğaz istasyon belirler. Darboğaz olmayan istasyondaki verim artışı ara stok birikmesine yol "
    "açar, ancak boyama kapasitesi değişmediğinden toplam çıktı artmaz; iyileştirme darboğaza yöneltilmelidir.")

# ------------------------------------------------------------------ belirsizlik ve fiyatlandırma
bd = 0.60 * 150_000 + 0.40 * (-30_000)
P.sayisal(BD,
    "Bir işletme yeni bir projeyi değerlendirmektedir. Talebin yüksek olması hâlinde (%60 olasılık) proje 150.000 ₺ "
    "kâr, düşük olması hâlinde (%40 olasılık) 30.000 ₺ zarar sağlayacaktır. Yönetim riske karşı nötr kabul "
    "edilmektedir.\n\nProjenin beklenen kârı kaç ₺’dir?",
    tl(bd), secenekler(bd, 90_000, 60_000, 102_000, 120_000),
    "Beklenen değer = 0,60 × 150.000 + 0,40 × (−30.000) = 90.000 − 12.000 = 78.000 ₺. Zararın ağırlıklandırılmaması "
    "90.000 ₺, işaretinin yanlış alınması 102.000 ₺ sonucunu verir.", zorluk="easy")

x = 0.40 * 180_000 + 0.60 * 20_000
y = 0.40 * 110_000 + 0.60 * 70_000
assert (x, y) == (84_000, 86_000)
P.q(BD,
    "Bir işletme iki yatırım seçeneği arasında seçim yapacaktır. Talebin yüksek olma olasılığı %40, düşük olma "
    "olasılığı %60’tır. X seçeneği yüksek talepte 180.000 ₺, düşük talepte 20.000 ₺; Y seçeneği yüksek talepte "
    "110.000 ₺, düşük talepte 70.000 ₺ kâr sağlayacaktır.\n\nBeklenen değer ölçütüne göre hangi seçenek seçilmelidir?",
    "Y; beklenen kârı 86.000 ₺’dir.",
    ["X; beklenen kârı 84.000 ₺’dir.",
     "X; beklenen kârı 100.000 ₺’dir.",
     "Y; beklenen kârı 90.000 ₺’dir.",
     "X; en yüksek kârı 180.000 ₺’dir."],
    "X: 0,40 × 180.000 + 0,60 × 20.000 = 84.000 ₺. Y: 0,40 × 110.000 + 0,60 × 70.000 = 86.000 ₺. Y seçilir. Basit "
    "ortalama X için 100.000 ₺, Y için 90.000 ₺ verir; olasılıkları dikkate almaz.")

bd = 0.30 * 200_000 + 0.50 * 90_000 + 0.20 * (-60_000)
P.sayisal(BD,
    "Bir işletme yeni bir mağaza açmayı değerlendirmektedir. Uzmanlara göre ilk yıl kârı iyimser senaryoda (%30 "
    "olasılık) 200.000 ₺, beklenen senaryoda (%50 olasılık) 90.000 ₺ olacak; kötümser senaryoda (%20 olasılık) ise "
    "mağaza 60.000 ₺ zarar edecektir.\n\nMağazanın ilk yıl beklenen kârı kaç ₺’dir?",
    tl(bd), secenekler(bd, 105_000, 76_667, 117_000, 230_000),
    "Beklenen kâr = 0,30 × 200.000 + 0,50 × 90.000 + 0,20 × (−60.000) = 60.000 + 45.000 − 12.000 = 93.000 ₺.")

P.q(BD,
    "Bir işletmenin risk komitesi, yatırım seçeneklerini beklenen değer yöntemiyle karşılaştıran raporu "
    "incelemektedir. Komite üyelerinden biri yöntemin sınırlılıklarını sıralamıştır.\n\nBeklenen değer yaklaşımıyla "
    "ilgili aşağıdakilerden hangisi yanlıştır?",
    "Sonuçların dağılımını ve seçeneklerin risk düzeyini de gösterir.",
    ["Olasılıkların tahmin edilmesini gerektirir.",
     "Her sonucu gerçekleşme olasılığıyla ağırlıklandırır.",
     "Karar vericinin riske karşı tutumunu yansıtmaz.",
     "Tekrarlanan kararlarda ortalama sonuca yaklaşır."],
    "Beklenen değer tek bir ağırlıklı ortalama verir; aynı beklenen değere sahip seçeneklerin sonuçlarının ne kadar "
    "dağıldığını (riskini) göstermez. Bu nedenle standart sapma veya senaryo analiziyle desteklenir.")

P.q(BD,
    "Bir işletme, yeni ürünün kârlılığını satış fiyatı, satış miktarı, hammadde fiyatı ve kur varsayımlarına göre "
    "hesaplamıştır. Yönetim, her varsayımın ne ölçüde değişmesi hâlinde projenin zarara geçeceğini bilmek "
    "istemektedir.\n\nBu amaçla kullanılan analizin karar sürecine temel katkısı aşağıdakilerden hangisidir?",
    "Sonucu en çok etkileyen kritik varsayımları belirlemek",
    ["Belirsizliği ortadan kaldırarak kesin kâr tahmini üretmek",
     "Olasılıkları hesaplayarak beklenen değeri bulmak",
     "Geçmiş dönem sapmalarını sorumlu birimlere dağıtmak",
     "Batık maliyetleri karar modelinden ayıklamak"],
    "Duyarlılık analizi, varsayımlardan biri değiştiğinde sonucun nasıl etkilendiğini gösterir ve yönetimin dikkatini "
    "kritik değişkenlere yöneltir; belirsizliği ortadan kaldırmaz.")

P.sayisal(BD,
    "Bir işletme maliyet artı fiyatlandırma yöntemini uygulamaktadır. Bir ürünün birim tam maliyeti; DİMM 48 ₺, DİŞ "
    "30 ₺, değişken GÜG 12 ₺ ve sabit GÜG ile pazarlama-yönetim giderlerinden düşen pay 30 ₺ olmak üzere 120 "
    "₺’dir. İşletme tam maliyet üzerine %25 kâr eklemektedir.\n\nÜrünün satış fiyatı kaç ₺’dir?",
    tl(120 * 1.25), secenekler(150, 112.5, 160, 145, 125),
    "Maliyet artı fiyat = tam maliyet × (1 + kâr oranı) = 120 × 1,25 = 150 ₺. Kâr oranının yalnız değişken maliyete "
    "(90 ₺) uygulanması 112,50 ₺ verir.", zorluk="easy")

P.sayisal(BD,
    "Bir işletme yeni bir ürün için pazar araştırması yapmış ve rakip ürünlerin 400 ₺’den satıldığını, bu fiyatın "
    "üzerinde satış yapılamayacağını belirlemiştir. İşletme satış fiyatı üzerinden %20 kâr marjı elde etmek "
    "istemektedir. Mühendislik ekibi ürünü bu hedefe göre tasarlayacaktır.\n\nÜrünün hedef maliyeti kaç ₺’dir?",
    tl(400 * 0.80), secenekler(320, 333.33, 480, 80, 380),
    "Hedef maliyet = hedef fiyat − hedef kâr = 400 − 400 × %20 = 320 ₺. Kâr marjı maliyete uygulanırsa (400 ÷ 1,20 = "
    "333,33 ₺) satış üzerinden %20 hedefi tutmaz.")

P.q(BD,
    "Bir elektronik üreticisi yeni ürünlerinde önce pazarın kabul edeceği fiyatı ve istenen kâr marjını "
    "belirlemekte, ardından tasarım ve tedarik ekiplerinden ürünü bu maliyetin altında üretecek çözümler "
    "istemektedir.\n\nBu yaklaşım aşağıdakilerden hangisidir?",
    "Hedef maliyetleme",
    ["Maliyet artı fiyatlandırma", "Standart maliyetleme", "Değişken maliyetleme", "Kaymak (üst) fiyatlama"],
    "Hedef maliyetlemede fiyat pazardan alınır; hedef kâr düşülerek izin verilen maliyet bulunur ve ürün bu maliyete "
    "göre tasarlanır. Maliyet artı yöntemde ise fiyat maliyetten türetilir.", zorluk="easy")

P.q(BD,
    "Bir işletme atıl kapasitenin bulunduğu kısa bir dönemde tek seferlik siparişlere düşük fiyat vermekte, ancak "
    "yıllık fiyat listesini tam maliyet ve hedef kâr üzerinden belirlemektedir. Yönetim bu iki uygulamanın "
    "tutarlılığını sorgulamaktadır.\n\nBu uygulamayla ilgili aşağıdakilerden hangisi doğrudur?",
    "Kısa dönemde değişken maliyet, uzun dönemde tam maliyet fiyatın alt sınırıdır.",
    ["Kısa ve uzun dönemde fiyatın alt sınırı değişken maliyettir.",
     "Kısa dönemde tam maliyet, uzun dönemde değişken maliyet alt sınırdır.",
     "Uzun dönemde sabit maliyetler batık olduğundan fiyata yansıtılmaz.",
     "Tek seferlik siparişlerde fiyat tam maliyetin altına inemez."],
    "Kısa dönemde sabit maliyetler zaten katlanıldığından atıl kapasitede değişken maliyeti aşan her fiyat kârı "
    "artırır. Uzun dönemde ise işletmenin sürekliliği için fiyatların tüm maliyetleri ve makul kârı karşılaması "
    "gerekir.")

P.serpistir()

if __name__ == "__main__":
    sys.exit(P.yaz())
