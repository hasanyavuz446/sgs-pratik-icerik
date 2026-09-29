# -*- coding: utf-8 -*-
"""Vergi · KDV · KDV Mekanizması (matrah, oran, indirim, düzeltme, beyan) — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında KDV mekanizması; ödenecek KDV'nin çok kalemli bir dönem tablosundan hesaplanması
(vade farkı, zayi mal düzeltmesi, sorumlu sıfatıyla ödenen KDV, değerleme kur farkı, devreden KDV) biçiminde sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 3065 sayılı KDVK md. 9, 20-30, 33-36, 39-40, 46, 48.
Cumhurbaşkanı kararıyla belirlenen oranlar kökte verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_kdv_mekanizmasi_2026.json", lesson="katma_deger_vergisi", topic="kdv_mekanizmasi",
          konu_adi="KDV Mekanizması", seed=2026092905,
          surum="3065 sayılı KDVK güncel metni; oranlar kökte; 29.09.2026 kontrolü")

K = "3065 sayılı Katma Değer Vergisi Kanunu’na göre"
K26 = "3065 sayılı Katma Değer Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
ORAN = "(KDV oranı %20 olarak alınacaktır.)"

o1 = 1_500_000 * 0.20 + 30_000 * 0.20 - 150_000 - 40_000
P.sayisal("KDVK md. 24, 29",
    "(ABC) A.Ş.’nin 2026/Mart dönemine ait işlemleri şöyledir: yurt içi mal teslimleri 1.500.000 ₺ (KDV hariç); daha önce "
    "vadeli satılan malın bedelinin geç ödenmesi nedeniyle müşteriden 30.000 ₺ (KDV hariç) vade farkı alınmış ve faturası "
    "düzenlenmiştir; kanuni defterlere kaydedilen alış faturalarında gösterilen KDV 150.000 ₺; önceki dönemden devreden "
    f"KDV 40.000 ₺. {ORAN}\n\n{K}, (ABC) A.Ş.’nin 2026/Mart dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(o1), secenekler(o1, 300_000 - 150_000 - 40_000, 306_000 - 150_000, 306_000 - 40_000, 300_000 - 150_000),
    "Md. 24/c'ye göre vade farkı matraha dahildir: hesaplanan KDV (1.500.000 + 30.000) × %20 = 306.000 ₺. İndirilecek KDV "
    "150.000 + devreden 40.000 = 190.000 ₺. Ödenecek KDV 306.000 − 190.000 = 116.000 ₺.")

P.q("KDVK md. 20",
    "(FGH) A.Ş., sattığı malın bedelinin bir kısmını nakit, bir kısmını alıcının vereceği danışmanlık hizmeti karşılığında "
    f"almayı kararlaştırmıştır.\n\n{K}, teslim ve hizmet işlemlerinde “bedel” kavramına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Alıcıdan alınan veya borçlanılan para, mal ve para ile temsil edilebilen menfaat ve hizmetlerin toplamıdır.",
    ["Sadece nakden veya banka yoluyla tahsil edilen tutardır; mal veya hizmet şeklindeki ayni ödemeler bedele dahil edilmez.",
     "Sadece faturada gösterilen tutardır; faturaya yansımayan menfaatler dikkate alınmaz.",
     "Satıcının malın maliyetine eklediği kâr payından ibarettir.",
     "Alıcının ödemeyi tamamladığı tarihte tahsil edilen tutardır."],
    "Md. 20/2'ye göre bedel; malı teslim alan veya kendisine hizmet yapılanlardan bu işlemler karşılığında her ne suretle "
    "olursa olsun alınan veya borçlanılan para, mal ve diğer suretlerde sağlanan ve para ile temsil edilebilen menfaat, hizmet "
    "ve değerler toplamıdır; md. 27'ye göre paradan başka değerlerde emsal bedel esas alınır.")

P.q("KDVK md. 24",
    "(IJK) A.Ş., müşterilerine düzenlediği faturalarda satış bedelinin yanında çeşitli ek tutarlar da göstermektedir."
    f"\n\n{K}, aşağıdakilerden hangisi KDV matrahına dahil değildir?",
    "Faturada gösterilen ticari teamüle uygun iskonto",
    ["Teslim alanın gösterdiği yere kadar satıcının yaptığı taşıma gideri",
     "Satış bedeline eklenen ambalaj ve sigorta giderleri",
     "Vadeli satışta alıcıdan alınan vade farkı",
     "Bedele eklenen servis ücreti adı altında sağlanan menfaat"],
    "Md. 24'e göre taşıma, yükleme ve boşaltma giderleri, ambalaj ve sigorta giderleri, vade farkı, fiyat farkı, kur farkı "
    "ile servis adı altında sağlanan menfaatler matraha dahildir; md. 25'e göre faturada gösterilen ticari teamüle uygun "
    "iskontolar ve hesaplanan KDV matraha dahil değildir.", zorluk="easy")

o2 = 1_000_000 * 0.20 - 120_000 + 8_000
P.sayisal("KDVK md. 30/c",
    "(DEF) Ltd. Şti.’nin 2026/Nisan dönemi işlemleri: yurt içi teslimler 1.000.000 ₺ (KDV hariç); indirilecek KDV 120.000 ₺. "
    "Aynı dönemde depodan çalınan ve geçmiş dönemde alış KDV’si indirilmiş olan malların alış bedeli 40.000 ₺, bunlara ait "
    f"KDV 8.000 ₺’dir. Hırsızlık deprem, sel veya yangın kaynaklı değildir. {ORAN}\n\n{K}, (DEF) Ltd. Şti.’nin 2026/Nisan "
    "dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(o2), secenekler(o2, 200_000 - 120_000, 200_000 - 128_000, 200_000 - 120_000 + 40_000, 200_000 - 112_000 + 8_000 * 2),
    "Md. 30/c'ye göre deprem, sel ve ilan edilmiş yangın dışındaki sebeplerle zayi olan mallara ait KDV indirilemez; daha önce "
    "indirilmiş olan 8.000 ₺ düzeltilerek eklenir: 200.000 − 120.000 + 8.000 = 88.000 ₺.", zorluk="hard")

P.q("KDVK md. 25-26",
    f"{K}, KDV matrahına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hesaplanan KDV, bedelin bir unsuru olduğundan matraha dahil edilir.",
    ["Döviz ile hesaplanan bedel vergiyi doğuran olayın meydana geldiği andaki cari kurla Türk parasına çevrilir.",
     "Faturada gösterilen ticari teamüle uygun iskontolar matraha dahil değildir.",
     "Vade farkı, fiyat farkı ve kur farkı matraha dahildir.",
     "Bedeli bulunmayan işlemlerde matrah emsal bedeli veya emsal ücretidir."],
    "Md. 25/b'ye göre hesaplanan KDV matraha dahil değildir. Md. 26 döviz, md. 25/a iskonto, md. 24/c vade ve kur farkı ile "
    "md. 27 emsal bedeli hükümlerini düzenler.", zorluk="easy")

P.q("KDVK md. 27",
    f"{K}, emsal bedeli ve emsal ücretine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Emsal bedelin tayininde genel giderlerden mamule düşen payın bedele katılması isteğe bağlıdır.",
    ["Bedelin mal veya hizmet gibi paradan başka değerler olması hâlinde matrah emsal bedeli veya emsal ücretidir.",
     "Emsal bedeli ve emsal ücreti Vergi Usul Kanunu hükümlerine göre tespit olunur.",
     "Serbest meslek faaliyetlerinde meslek teşekkülünce tespit edilen tarife varsa bedel bu tarifedeki ücretten düşük olamaz.",
     "Bedelin emsale göre açıkça düşük olduğu ve haklı sebeple açıklanamadığı hâllerde emsal bedeli esas alınır."],
    "Md. 27/4'e göre KDV uygulamasında emsal bedelin tayininde genel idare giderleri ve genel giderlerden mamule düşen hissenin "
    "bedele katılması mecburidir.", zorluk="hard")

o3 = 800_000 * 0.20 - 90_000
P.sayisal("KDVK md. 30/c",
    "(GHI) A.Ş.’nin deprem bölgesindeki deposunda bulunan ve alış KDV’si önceki dönemde indirilmiş olan 50.000 ₺ bedelli "
    "(KDV’si 10.000 ₺) emtia 2026/Şubat ayında meydana gelen depremde zayi olmuştur. Aynı dönemde yurt içi teslimler "
    f"800.000 ₺ (KDV hariç), indirilecek KDV 90.000 ₺’dir. {ORAN}\n\n{K}, (GHI) A.Ş.’nin 2026/Şubat dönemi ödenecek KDV "
    "tutarı kaç ₺’dir?",
    tl(o3), secenekler(o3, 160_000 - 90_000 + 10_000, 160_000 - 100_000, 160_000 - 90_000 + 50_000, 160_000),
    "Md. 30/c'ye göre deprem sonucu zayi olan mallara ait KDV indirim yasağı dışındadır; düzeltme gerekmez: 160.000 − "
    "90.000 = 70.000 ₺.")

P.q("KDVK md. 23",
    f"{K}, aşağıdakilerden hangisi Kanunda sayılan özel matrah şekillerinden biri değildir?",
    "Kiralanan iş makinesinin aylık kira bedeli",
    ["Milli Piyango dahil her türlü piyangoda piyangoya katılma bedeli",
     "Profesyonel sanatçıların yer aldığı konserlere giriş karşılığında alınan bedel",
     "Müzayede mahallerinde yapılan satışlarda kesin satış bedeli",
     "Ziynet eşyası tesliminde külçe altın bedeli düşüldükten sonra kalan miktar"],
    "Md. 23'e göre piyangoya ve bahislere katılma bedeli, profesyonel gösteri ve konserlere giriş bedeli, gümrük depoları ve "
    "müzayede mahallerindeki kesin satış bedeli, ziynet eşyasında külçe altın bedeli düşülmüş tutar ve ikinci el taşıt ve "
    "taşınmazlarda alış bedeli düşülmüş tutar özel matrahtır. İş makinesi kirası genel hükümlere tabidir.")

P.q("KDVK md. 23/f",
    "İkinci el taşınmaz ticareti yapan (LMN) Emlak A.Ş., KDV mükellefi olmayan bir kişiden satın aldığı daireyi kapsamlı "
    f"tadilatla vasfını esaslı olarak değiştirdikten sonra satmıştır.\n\n{K}, bu teslimin matrahına ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Vasfında esaslı değişiklik yapıldığından özel matrah uygulanmaz; matrah satış bedelidir.",
    ["Alış bedeli düşüldükten sonra kalan tutar matrahtır.",
     "Hem tadilat giderleri hem de alış bedeli satış bedelinden düşüldükten sonra kalan tutar matrahtır.",
     "Satış bedelinin yarısı matrahtır.",
     "İkinci el taşınmaz teslimleri KDV’nin konusuna girmez."],
    "Md. 23/f'deki özel matrah, KDV mükellefi olmayanlardan alınan ikinci el taşıt veya taşınmazların vasfında esaslı "
    "değişiklik yapılmaksızın satılması şartına bağlıdır. Vasfı esaslı değiştirildiğinden genel hüküm (md. 20) uygulanır.",
    zorluk="hard")

o4 = 1_250_000 * 0.20 - 100_000
P.sayisal("KDVK md. 30/b",
    "Tekstil ticareti yapan (JKL) A.Ş., 2026/Mayıs döneminde işinde kullanmak üzere 1.500.000 ₺ + 300.000 ₺ KDV bedelle "
    "binek otomobil satın almıştır. Aynı dönemde yurt içi teslimleri 1.250.000 ₺ (KDV hariç), binek otomobil dışındaki "
    f"alışlarına ait KDV 100.000 ₺’dir. {ORAN}\n\n{K}, (JKL) A.Ş.’nin 2026/Mayıs dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(o4), secenekler(o4, 250_000 - 100_000 - 300_000 * 0.30, 250_000, 250_000 - 300_000 * 0.30, 100_000),
    "Md. 30/b'ye göre faaliyeti binek otomobil kiralama veya işletme olmayanların binek otomobillerine ait alış KDV'si "
    "indirilemez: 250.000 − 100.000 = 150.000 ₺. Binek otomobile ait KDV maliyete eklenir.")

P.q("KDVK md. 21",
    f"{K}, aşağıdakilerden hangisi ithalatta KDV matrahına dahil edilmez?",
    "Tescilden sonra yurt içinde yapılan ve ayrıca vergilendirilen taşıma gideri",
    ["Gümrük vergisi tarhına esas olan kıymet",
     "İthalat sırasında ödenen gümrük vergisi",
     "Tescil tarihine kadar yapılan ve vergilendirilmeyen giderler",
     "Tescil tarihine kadar mal bedeli üzerinden hesaplanan fiyat farkı ve kur farkı ödemeleri"],
    "Md. 21'e göre ithalatta matrah gümrük vergisine esas kıymet, ithalatta ödenen vergi, resim, harç ve paylar ile tescil "
    "tarihine kadar yapılan ve vergilendirilmeyen giderler ve mal bedeli üzerinden hesaplanan fiyat ve kur farklarının "
    "toplamıdır. Tescilden sonra yurt içinde yapılan ve ayrıca vergilendirilen giderler dahil değildir.")

P.q("KDVK md. 28",
    f"{K26}, KDV oranına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kanundaki genel oran %10 olup Cumhurbaşkanı bunu dört katına kadar artırabilir.",
    ["Genel oran Kanunda %20 olarak belirlenmiş olup Cumhurbaşkanının oranı değiştirme yetkisi yoktur.",
     "Cumhurbaşkanı oranı %1’e kadar indirebilir ancak artıramaz.",
     "Konut teslimleri için farklı oran belirlenemez.",
     "Oranlar sadece Maliye Bakanlığınca belirlenir."],
    "Md. 28'e göre KDV oranı vergiye tabi her bir işlem için %10'dur; Cumhurbaşkanı bu oranı dört katına kadar artırmaya, "
    "%1'e kadar indirmeye ve konut teslimleri gibi işlemler için farklı oranlar belirlemeye yetkilidir. Uygulanan %20 "
    "genel oran bu yetkiyle belirlenmiştir.", zorluk="hard")

dev5 = (80_000 + 50_000 + 150_000) - 250_000 * 0.20
P.sayisal("KDVK md. 29/2, 30/b",
    "Faaliyeti binek otomobil kiralama olan (MNO) A.Ş., 2026/Haziran döneminde kiralamada kullanmak üzere 400.000 ₺ + "
    "80.000 ₺ KDV bedelle binek otomobil almıştır. Dönemde kiralama hasılatı 250.000 ₺ (KDV hariç), diğer alışlara ait "
    f"KDV 50.000 ₺, önceki dönemden devreden KDV 150.000 ₺’dir. {ORAN}\n\n{K}, (MNO) A.Ş.’nin 2026/Temmuz dönemine "
    "devredecek KDV tutarı kaç ₺’dir?",
    tl(dev5), secenekler(dev5, 150_000, 280_000, 200_000, 280_000 - 50_000 - 80_000 * 0.30),
    "Md. 30/b'ye göre faaliyeti binek otomobil kiralama olanların bu amaçla kullandıkları araçların KDV'si indirilebilir. "
    "İndirilecek toplam 80.000 + 50.000 + 150.000 = 280.000 ₺; hesaplanan 50.000 ₺. Md. 29/2'ye göre fark 230.000 ₺ "
    "sonraki döneme devreder, iade edilmez.", zorluk="hard")

P.q("KDVK md. 29/3, 34",
    "(OPR) A.Ş.’ye Kasım 2025’te düzenlenen ve KDV’si ayrıca gösterilen bir alış faturası, muhasebe hatası nedeniyle kanuni "
    f"defterlere ancak Ekim 2026’da kaydedilmiştir.\n\n{K}, bu faturadaki KDV’nin indirimine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Fatura 2026 yılı aşılmadan deftere kaydedildiğinden KDV Ekim 2026 döneminde indirilebilir.",
    ["İndirim hakkı vergiyi doğuran olayın olduğu 2025 yılı sonunda sona erdiğinden KDV indirilemez.",
     "KDV sadece Kasım 2025 dönemine ait düzeltme beyannamesiyle indirilebilir.",
     "KDV indirilemez, ancak gider olarak dikkate alınabilir.",
     "KDV’nin indirimi için vergi dairesinden izin alınması gerekir."],
    "Md. 29/3'e göre indirim hakkı, vergiyi doğuran olayın vuku bulduğu takvim yılını takip eden takvim yılı aşılmamak "
    "şartıyla, vesikaların kanuni defterlere kaydedildiği dönemde kullanılabilir; md. 34'e göre KDV'nin faturada ayrıca "
    "gösterilmesi ve belgenin kanuni defterlere kaydı şarttır.", zorluk="hard")

P.q("KDVK md. 34",
    f"{K}, KDV indiriminin belgelendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "KDV alış belgesinde ayrıca gösterilmeli ve belge kanuni defterlere kaydedilmelidir.",
    ["KDV’nin belgede ayrıca gösterilmesi gerekmez; toplam tutar yeterlidir.",
     "Belgenin kanuni defterlere kaydı indirim için şart değildir.",
     "İthalatta ödenen KDV gümrük makbuzu olmaksızın da indirilebilir.",
     "İndirim hakkı sadece e-fatura ile belgelenen alışlarda kullanılabilir."],
    "Md. 34/1'e göre yurt içinden sağlanan veya ithal olunan mal ve hizmetlere ait KDV, alış faturası veya benzeri vesikalar "
    "ve gümrük makbuzu üzerinde ayrıca gösterilmek ve bu vesikalar kanuni defterlere kaydedilmek şartıyla indirilebilir.",
    zorluk="easy")

o6 = 60_000 * 0.70
P.sayisal("KDVK md. 33",
    "(PRS) A.Ş., 2026/Mart döneminde hem vergiye tabi hem de indirim hakkı tanınmayan istisna kapsamında işlemler yapmıştır. "
    "Dönem hasılatının %70’i vergiye tabi, %30’u indirim hakkı tanınmayan istisnalı işlemlerden oluşmaktadır. Her iki "
    "faaliyette ortak kullanılan genel giderlere ait faturalarda 60.000 ₺ KDV gösterilmiştir; ortak giderler hasılat "
    f"oranında dağıtılacaktır.\n\n{K}, bu ortak giderlere ait KDV’nin indirilebilecek kısmı kaç ₺’dir?",
    tl(o6), secenekler(o6, 60_000, 60_000 * 0.30, 0, 60_000 * 0.50),
    "Md. 33'e göre indirim hakkı tanınan ve tanınmayan işlemlerin birlikte yapılması hâlinde, faturalarda gösterilen KDV'nin "
    "ancak indirim hakkı tanınan işlemlere isabet eden kısmı indirilebilir: 60.000 × %70 = 42.000 ₺.")

P.q("KDVK md. 30",
    "(STU) A.Ş.’nin muhasebe müdürü, 2026/Mart dönemi beyannamesi için alış belgelerindeki KDV’leri incelemektedir."
    f"\n\n{K}, aşağıdaki KDV’lerden hangisi indirim konusu yapılabilir?",
    "Üretimde kullanılan hammadde alışına ait KDV",
    ["Faaliyeti kiralama olmayan işletmenin binek otomobil alışına ait KDV",
     "Hırsızlık sonucu zayi olan emtiaya ait KDV",
     "Kanunen kabul edilmeyen gidere ait KDV",
     "İndirim hakkı tanınmayan istisnalı teslimlere ait alışların KDV’si"],
    "Md. 30'a göre binek otomobil alış KDV'si (kiralama faaliyeti hariç), deprem, sel ve ilan edilmiş yangın dışında zayi olan "
    "mallara ait KDV, KKEG'e ait KDV ve vergiye tabi olmayan veya istisna edilmiş işlemlere ait KDV indirilemez. Hammadde "
    "alışına ait KDV md. 29'a göre indirilir.", zorluk="easy")

P.q("KDVK md. 30/c",
    f"{K26}, amortismana tabi iktisadi kıymetlerin zayi olmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Faydalı ömrünü tamamlamadan zayi olan kıymetin yüklenilen KDV’sinin kullanılan süreye isabet eden kısmı indirilebilir.",
    ["Faydalı ömrünü tamamlayan kıymetin zayi olması hâlinde KDV’nin tamamı düzeltilerek ilgili dönemin beyannamesinde beyan edilir.",
     "Amortismana tabi kıymetlerin zayi olması hâlinde KDV indirilemez.",
     "Zayi olan kıymetin KDV’si ancak sigorta tazminatı alınmışsa indirilebilir.",
     "Faydalı ömür dikkate alınmaksızın KDV’nin %50’si indirilebilir."],
    "Md. 30/c'ye 7104 sayılı Kanunla eklenen hükme göre faydalı ömrünü tamamladıktan sonra zayi olan amortismana tabi "
    "kıymetlerin yüklenilen KDV'si ile faydalı ömrünü tamamlamadan zayi olanların KDV'sinin kullanılan süreye isabet eden "
    "kısmı indirilebilir.", zorluk="hard")

m1 = (100_000 - 10_000 + 5_000 + 2_000) * 0.20
P.sayisal("KDVK md. 24-25",
    "(STU) A.Ş., müşterisine 100.000 ₺ liste fiyatlı mal satmış; faturada ticari teamüle uygun 10.000 ₺ iskonto göstermiştir. "
    "Malın müşterinin gösterdiği depoya kadar taşınması için satıcı 5.000 ₺ nakliye bedeli ve 2.000 ₺ ambalaj bedelini "
    f"faturaya eklemiştir. {ORAN}\n\n{K}, bu teslim için hesaplanacak KDV kaç ₺’dir?",
    tl(m1), secenekler(m1, 100_000 * 0.20, 107_000 * 0.20, 90_000 * 0.20, 95_000 * 0.20),
    "Md. 24'e göre teslim alanın gösterdiği yere kadar yapılan taşıma giderleri ve ambalaj giderleri matraha dahildir; md. "
    "25'e göre faturada gösterilen ticari teamüle uygun iskontolar matraha dahil değildir: (100.000 − 10.000 + 5.000 + "
    "2.000) × %20 = 19.400 ₺.")

P.q("KDVK md. 29/2",
    f"{K}, indirilecek KDV’nin hesaplanan KDV’den fazla olmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aradaki fark kural olarak sonraki dönemlere devrolunur ve iade edilmez.",
    ["Aradaki fark talep hâlinde nakden iade edilir.",
     "Aradaki fark mükellefin gelir vergisi borcuna mahsup edilir.",
     "Aradaki fark yıl sonunda gider yazılarak kapatılır.",
     "Aradaki fark takip eden yılın sonunda silinir."],
    "Md. 29/2'ye göre indirilecek KDV hesaplanandan fazla olursa fark sonraki dönemlere devrolunur ve iade edilmez. İndirimli "
    "orana tabi işlemlerde Cumhurbaşkanınca belirlenen sınırı aşan tutarın iadesi gibi Kanunda sayılan istisnalar saklıdır.",
    zorluk="easy")

P.q("KDVK md. 29/2",
    "(VYZ) A.Ş. sadece indirimli KDV oranına tabi ekmeklik un teslim etmektedir. Şirketin alışlarındaki KDV oranı yüksek "
    f"olduğundan her yıl önemli tutarda KDV yüklenmektedir.\n\n{K}, bu mükellefin yüklendiği KDV’ye ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Cumhurbaşkanınca belirlenen sınırı aşan indirilemeyen vergi iade edilebilir.",
    ["İndirilemeyen vergi iade edilemez, sadece devreder.",
     "İndirilemeyen vergi her ay sonunda gider yazılır.",
     "İndirimli oranlı teslimlerde, yüklenilen vergi maliyete eklendiğinden indirim hakkı bulunmamaktadır.",
     "İndirilemeyen vergi ancak ihracat yapılırsa iade edilir."],
    "Md. 29/2'ye göre Cumhurbaşkanınca vergi nispeti indirilen teslim ve hizmetlerle ilgili olup indirilemeyen ve belirlenen "
    "sınırı aşan vergi, mükellefin vergi ve SGK prim borçlarına mahsuben iade edilir; belirlenen sektörlerde yılı içinde, "
    "diğerlerinde izleyen yıl içinde talep şartıyla nakden iade edilebilir.", zorluk="hard")

m2 = (1_000_000 + 100_000 + 20_000) * 0.20
P.sayisal("KDVK md. 21",
    "(VYZ) A.Ş., 2026 yılında gümrük vergisi tarhına esas kıymeti (CIF) 1.000.000 ₺ olan bir makine ithal etmiştir. İthalat "
    "sırasında 100.000 ₺ gümrük vergisi ödenmiş, gümrük beyannamesinin tescil tarihine kadar vergilendirilmemiş 20.000 ₺ "
    f"ardiye ve liman gideri yapılmıştır. {ORAN}\n\n{K}, bu ithalat nedeniyle ödenecek KDV kaç ₺’dir?",
    tl(m2), secenekler(m2, 1_000_000 * 0.20, 1_100_000 * 0.20, 1_020_000 * 0.20, 1_120_000 * 0.18),
    "Md. 21'e göre ithalatta matrah; gümrük vergisine esas kıymet, ithalat sırasında ödenen vergi, resim ve harçlar ile tescil "
    "tarihine kadar yapılan ve vergilendirilmeyen giderlerin toplamıdır: 1.120.000 × %20 = 224.000 ₺.")

P.q("KDVK md. 35",
    f"{K}, matrah ve indirim miktarlarının değişmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Düzeltme, değişikliğin meydana geldiği dönemde değil, ilk işlemin yapıldığı dönemin beyannamesinde yapılır.",
    ["Mal iadesi hâlinde satıcı borçlandığı vergiyi düzeltir.",
     "Mal iadesi hâlinde alıcı indirdiği vergiyi düzeltir.",
     "İade olunan malların fiilen işletmeye girmesi ve bu girişin defter kayıtları ile beyannamede gösterilmesi şarttır.",
     "İşlemden vazgeçilmesi de matrahta değişiklik sebebidir."],
    "Md. 35'e göre malların iadesi, işlemin gerçekleşmemesi, işlemden vazgeçilmesi gibi sebeplerle matrahta değişiklik olursa "
    "satıcı borçlandığı vergiyi, alıcı indirdiği vergiyi değişikliğin vukubulduğu dönem içinde düzeltir.")

P.q("KDVK md. 36",
    f"{K}, Cumhurbaşkanının KDV indirim hakkına ilişkin yetkileri arasında aşağıdakilerden hangisi yer almaz?",
    "Hesaplanan KDV’yi matrahın bir unsuru hâline getirmek",
    ["İndirim hakkını kısmen veya tamamen kaldırmak veya yeniden koymak",
     "İndirim hakkı kısıtlanan mal ve hizmetleri belirlemek",
     "İadesi talep edilmeyen devreden KDV’nin gider yazılmasına imkân vermek",
     "İade talep edilebilecek asgari tutarı belirlemek"],
    "Md. 36'ya göre Cumhurbaşkanı indirim hakkını kısmen veya tamamen kaldırmaya ya da yeniden koymaya, kısıtlanan mal ve "
    "hizmetleri belirlemeye, devreden KDV'nin gider yazılmasına imkân vermeye ve iade talep edilebilecek asgari tutarı "
    "belirlemeye yetkilidir. Hesaplanan KDV md. 25 gereği matraha dahil değildir.")

m3 = (1_000_000 - 800_000) * 0.20
P.sayisal("KDVK md. 23/f",
    "İkinci el motorlu kara taşıtı ticaretiyle uğraşan (ZAB) Otomotiv Ltd. Şti., KDV mükellefi olmayan Bay (K)’dan 800.000 "
    "₺’ye satın aldığı otomobili vasfında esaslı değişiklik yapmaksızın 2026 yılında 1.000.000 ₺’ye satmıştır. (Bu "
    f"teslimde uygulanacak KDV oranı %20 olarak alınacaktır.)\n\n{K}, bu teslim için hesaplanacak KDV kaç ₺’dir?",
    tl(m3), secenekler(m3, 1_000_000 * 0.20, 800_000 * 0.20, 200_000 * 0.01, 1_000_000 * 0.01),
    "Md. 23/f'ye göre ikinci el motorlu kara taşıtı ticaretiyle uğraşanlarca KDV mükellefi olmayanlardan alınıp vasfında "
    "esaslı değişiklik yapılmadan satılan taşıtların tesliminde matrah, alış bedeli düşüldükten sonra kalan tutardır: "
    "(1.000.000 − 800.000) × %20 = 40.000 ₺.", zorluk="hard")

P.q("KDVK md. 9/1",
    "Türkiye’de ikametgâhı, işyeri, kanuni merkezi ve iş merkezi bulunmayan (WXY) Inc., Türkiye’deki KDV mükellefi olmayan "
    f"gerçek kişilere çevrim içi müzik aboneliği satmaktadır.\n\n{K}, bu hizmete ait KDV’nin beyanına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "KDV, hizmeti sunan (WXY) Inc. tarafından beyan edilip ödenir.",
    ["KDV, hizmeti satın alan gerçek kişiler tarafından sorumlu sıfatıyla ödenir.",
     "Hizmet yurt dışından sunulduğu için KDV’nin konusuna girmez.",
     "KDV, ödemeye aracılık eden banka tarafından tevkif edilir.",
     "Gerçek kişiler mükellef olmadığından bu hizmet KDV’den istisnadır."],
    "Md. 9/1'e göre Türkiye'de ikametgâhı, işyeri, kanuni ve iş merkezi bulunmayanlarca KDV mükellefi olmayan gerçek kişilere "
    "elektronik ortamda sunulan hizmetlere ilişkin KDV, bu hizmeti sunanlar tarafından beyan edilip ödenir.", zorluk="hard")

P.q("KDVK md. 9/2",
    "Vergi incelemesinde (ZAB) Ltd. Şti.’nin deposunda alış belgesi bulunmayan mallar tespit edilmiştir."
    f"\n\n{K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mükellefe belgelerin ibrazı için tespit tarihinden itibaren 10 gün süre verilir.",
    ["Belgesiz mallara ait KDV sadece satıcıdan aranır.",
     "Mükellefe belge ibrazı için 30 gün süre verilir.",
     "Belgeler ibraz edilemezse vergi, malların alış bedeli üzerinden hesaplanır ve ceza kesilmez.",
     "Belgesiz mal bulundurulması sadece usulsüzlük cezası gerektirir."],
    "Md. 9/2'ye göre belgesiz mal bulunduran mükellefe alış belgelerinin ibrazı için tespit tarihinden itibaren 10 günlük süre "
    "verilir; ibraz edilemezse tespit tarihindeki emsal bedel üzerinden hesaplanan KDV resen tarh edilir ve vergi ziyaı cezası "
    "uygulanır.", zorluk="hard")

m4 = (500_000 - 420_000) * 0.20
P.sayisal("KDVK md. 23/e",
    "Kuyumcu Bay (L), 2026 yılında 500.000 ₺ bedelle altın bilezik satmıştır. Bileziğin içerdiği külçe altının bedeli "
    f"420.000 ₺’dir. {ORAN}\n\n{K}, bu teslim için hesaplanacak KDV kaç ₺’dir?",
    tl(m4), secenekler(m4, 500_000 * 0.20, 420_000 * 0.20, 80_000 * 0.01, 500_000 * 0.01),
    "Md. 23/e'ye göre altından mamul veya altın ihtiva eden ziynet eşyalarının tesliminde matrah, külçe altın bedeli "
    "düşüldükten sonra kalan tutardır: (500.000 − 420.000) × %20 = 16.000 ₺.")

P.q("KDVK md. 39",
    f"{K}, KDV’de vergilendirme dönemine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Vergi kesintisi yapmakla sorumlu tutulanlar için vergilendirme dönemi üç aydır.",
    ["Kanundaki genel kural, faaliyet gösterilen takvim yılının üçer aylık dönemleridir.",
     "Maliye Bakanlığı hasılata göre birer aylık vergilendirme dönemi belirleyebilir.",
     "Götürü usulde vergilendirilenler için vergilendirme dönemi bir takvim yılıdır.",
     "İthalatta vergilendirme dönemi gümrük bölgesine girildiği andır."],
    "Md. 39/2-b'ye göre vergi kesintisi yapmakla sorumlu tutulanlar için vergilendirme dönemi bir aydır. Kanunda genel kural "
    "üçer aylık dönem olup Bakanlık aylık dönem belirleyebilir; götürü usulde takvim yılı, ithalatta gümrük bölgesine giriş "
    "anı vergilendirme dönemidir.")

P.q("KDVK md. 40",
    "(CDE) A.Ş., 2026/Ağustos döneminde tadilat nedeniyle hiç satış yapmamış, sadece alış yapmıştır."
    f"\n\n{K}, (CDE) A.Ş.’nin bu döneme ilişkin beyan yükümlülüğü hakkında aşağıdakilerden hangisi doğrudur?",
    "Vergiye tabi işlemi bulunmasa da KDV beyannamesi vermek mecburiyetindedir.",
    ["Vergiye tabi işlemi olmadığından beyanname vermez.",
     "Sadece alışlarına ait KDV’yi iade almak için beyanname verebilir.",
     "Beyanname yerine vergi dairesine yazılı bildirimde bulunur.",
     "Bir sonraki dönemde iki dönemi birlikte beyan eder."],
    "Md. 40/3'e göre herhangi bir vergilendirme döneminde vergiye tabi işlemleri bulunmayan mükellefler de beyanname vermek "
    "mecburiyetindedir.", zorluk="easy")

m5 = 1_000 * 240 * 20 / 120
P.sayisal("KDVK md. 20/4",
    "Belediye sınırları içinde yolcu taşımacılığı yapan (CDE) A.Ş., fiyatı tarifeyle belirlenen ve KDV dahil 240 ₺ olan "
    f"biletlerden 2026/Mart döneminde 1.000 adet satmıştır. {ORAN}\n\n{K}, bu satışlar nedeniyle hesaplanacak KDV kaç "
    "₺’dir?",
    tl(m5), secenekler(m5, 240_000 * 0.20, 240_000 * 0.18, 200_000 * 0.18, 240_000 * 0.10),
    "Md. 20/4'e göre belli bir tarifeye göre fiyatı tespit edilen işlerde ve bedelin biletle tahsil edildiği hâllerde bilet "
    "bedeli KDV dahil olarak tespit edilir: 240.000 × 20/120 = 40.000 ₺.", zorluk="hard")

P.q("KDVK md. 40, 46",
    f"{K}, ithalatta KDV’nin beyanı ve ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İthalde KDV gümrük giriş beyannamesiyle tarh edilir, gümrük vergisiyle birlikte ödenir.",
    ["İthalde alınan KDV ithalatçının aylık KDV beyannamesiyle beyan edilip izleyen ay ödenir.",
     "İthalde KDV ödenmez, ithalatçı mükellef sorumlu sıfatıyla beyan eder.",
     "İthalatta KDV yıllık beyannameyle beyan edilir.",
     "İthalde alınan KDV gümrük vergisinden sonra, üç ay içinde ödenir."],
    "Md. 40/4'e göre ithalatta KDV gümrük giriş beyannamesindeki beyan üzerine tarh olunur; md. 46/2'ye göre ithalde alınan "
    "KDV gümrük vergisi ile birlikte ve aynı zamanda ödenir.")

P.q("KDVK md. 48",
    "(FGH) A.Ş., ithalat sırasında eksik ödenen KDV’yi sonraki dönemde verdiği KDV beyannamesinde hesaplayıp ödemiştir. "
    f"Daha sonra gümrük idaresi eksik ödenen KDV’yi tahsil etmek istemektedir.\n\n{K}, bu durumda aşağıdakilerden hangisi "
    "doğrudur?",
    "Beyannameyle ödenen KDV, gümrükte tahsili gereken KDV’den düşülür.",
    ["Beyannameyle ödenen KDV dikkate alınmaz, eksik KDV gümrükte ayrıca tahsil edilir.",
     "Eksik ödenen KDV sadece vergi dairesince, ceza ile birlikte tahsil edilir.",
     "Eksik ödenen KDV terkin edilir, tahsil edilmez.",
     "Sorumlu sıfatıyla ödenen KDV de gümrükte tahsili gereken KDV’den düşülür."],
    "Md. 48'e göre indirim hakkı tanınan işlemlere konu eşyanın serbest dolaşıma girdiği tarihin içinde bulunduğu veya sonraki "
    "dönemlere ait beyannamelerle ödenen KDV (sorumlu sıfatıyla ödenenler hariç), ithalde hiç ödenmemesi veya eksik "
    "ödenmesi nedeniyle tahsili gereken KDV'den düşülür.", zorluk="hard")

m6 = 500_000 * 0.20
P.sayisal("KDVK md. 27",
    "(FGH) A.Ş., emsal bedeli 500.000 ₺ olan bir malı ortağının akrabası olan bir kişiye 300.000 ₺’ye satmıştır. Şirket bu "
    f"düşüklüğü haklı bir sebeple açıklayamamaktadır. {ORAN}\n\n{K}, bu teslim için hesaplanacak KDV kaç ₺’dir?",
    tl(m6), secenekler(m6, 300_000 * 0.20, 200_000 * 0.20, 400_000 * 0.20, 800_000 * 0.20),
    "Md. 27/2'ye göre bedelin emsal bedeline göre açıkça düşük olduğu ve bu düşüklüğün haklı bir sebeple açıklanamadığı "
    "hâllerde matrah emsal bedelidir: 500.000 × %20 = 100.000 ₺.")

P.oncul("KDVK md. 24-25",
    f"{K} aşağıdaki unsurlar değerlendirilmektedir:",
    ["Vadeli satışta alınan vade farkı",
     "Faturada gösterilen ticari teamüle uygun iskonto",
     "Satıcının teslim alanın gösterdiği yere kadar yaptığı taşıma gideri",
     "Hesaplanan katma değer vergisi"],
    "Yukarıdakilerden hangileri KDV matrahına dahildir?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 24'e göre vade farkı (I) ve teslim alanın gösterdiği yere kadar yapılan taşıma giderleri (III) matraha dahildir; md. "
    "25'e göre faturada gösterilen iskontolar (II) ve hesaplanan KDV (IV) matraha dahil değildir.")

m7 = 50_000 * 0.20
P.sayisal("KDVK md. 24/c",
    "(IJK) A.Ş., Ocak 2026’da ihraç kaydı olmaksızın yurt içindeki bir müşterisine döviz bazında vadeli mal satmıştır. "
    "Şubat 2026’da tahsilat sırasında şirket lehine 50.000 ₺ kur farkı oluşmuş ve fatura düzenlenmiştir. Aynı ay dönem "
    f"sonunda kasadaki dövizlerin değerlemesinden 30.000 ₺ kur farkı geliri doğmuştur. {ORAN}\n\n{K}, Şubat 2026 döneminde "
    "bu kur farkları nedeniyle hesaplanacak KDV kaç ₺’dir?",
    tl(m7), secenekler(m7, 80_000 * 0.20, 30_000 * 0.20, 0, 80_000 * 0.18),
    "Md. 24/c'ye göre teslimle ilgili kur farkı matraha dahildir (50.000 × %20 = 10.000 ₺). Kasadaki dövizlerin "
    "değerlemesinden doğan kur farkı bir teslim veya hizmet karşılığı olmadığından KDV'nin konusuna girmez.", zorluk="hard")

P.q("KDVK md. 26",
    "(IJK) A.Ş., 5 Mart 2026’da yurt içindeki bir müşterisine 10.000 ABD doları bedelli mal teslim etmiş, bedeli 5 Nisan "
    f"2026’da tahsil etmiştir.\n\n{K}, bu teslimde KDV matrahının Türk parasına çevrilmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Döviz, vergiyi doğuran olayın meydana geldiği 5 Mart 2026’daki cari kurla çevrilir.",
    ["Döviz, bedelin tahsil edildiği 5 Nisan 2026’daki kurla çevrilir.",
     "Döviz, faturanın düzenlendiği ayın son günündeki kurla çevrilir.",
     "Döviz, Merkez Bankasının yıllık ortalama kuruyla çevrilir.",
     "Mükellef istediği kuru seçebilir."],
    "Md. 26'ya göre bedelin döviz ile hesaplanması hâlinde döviz, vergiyi doğuran olayın meydana geldiği andaki cari kur "
    "üzerinden Türk parasına çevrilir; tahsilat sırasında oluşan kur farkı md. 24/c'ye göre ayrıca matraha dahil edilir.")

m8 = 120_000 * 20 / 120
P.sayisal("KDVK md. 29/4",
    "(LMN) A.Ş.’nin 2024 yılında yaptığı ve KDV’sini beyan edip ödediği bir satıştan doğan KDV dahil 120.000 ₺ tutarındaki "
    "alacağı, VUK md. 322 uyarınca 2026/Mayıs döneminde değersiz hâle gelmiş ve zarar yazılmıştır. Alacak için daha önce "
    f"karşılık ayrılmamıştır. {ORAN}\n\n{K}, (LMN) A.Ş.’nin 2026/Mayıs döneminde bu alacak nedeniyle indirim konusu "
    "yapabileceği KDV kaç ₺’dir?",
    tl(m8), secenekler(m8, 120_000 * 0.20, 0, 120_000 * 0.18, 100_000 * 0.18),
    "Md. 29/4'e göre VUK md. 322'ye göre değersiz hâle gelen alacaklara ilişkin hesaplanan ve beyan edilen KDV, alacağın "
    "zarar yazıldığı dönemde indirilebilir; KDV dahil 120.000 ₺ içindeki vergi 120.000 × 20/120 = 20.000 ₺'dir.")

P.q("KDVK md. 27/5",
    "Avukat Bay (N), müvekkiline verdiği danışmanlık hizmeti için baro tarafından belirlenen asgari ücret tarifesindeki "
    f"tutarın altında bir ücret belirlemiştir.\n\n{K}, bu hizmetin KDV matrahına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hizmetin bedeli meslek teşekkülünce belirlenen tarifedeki ücretten düşük olamaz.",
    ["Tarafların anlaştığı bedel matrah olarak esas alınır.",
     "Matrah, avukatın aynı yıl içinde aldığı en yüksek ücrettir.",
     "Tarifenin altında kalan ücretlerde KDV hesaplanmaz.",
     "Matrah, tarifedeki ücretin yarısıdır."],
    "Md. 27/5'e göre serbest meslek faaliyetleri için ilgili meslek teşekküllerince tespit edilmiş bir tarife varsa, hizmetin "
    "bedeli bu tarifede gösterilen ücretten düşük olamaz.", zorluk="easy")

m9 = (200_000 - 50_000) * 0.20 - 25_000
P.sayisal("KDVK md. 35",
    "(OPR) A.Ş. 2026/Nisan döneminde 200.000 ₺ (KDV hariç) mal satmış; aynı dönem içinde müşteri 50.000 ₺’lik kısmını iade "
    "etmiş ve iade edilen mallar fiilen işletmeye girerek kayıtlara alınmıştır. Dönemin indirilecek KDV’si 25.000 ₺’dir. "
    f"{ORAN}\n\n{K}, (OPR) A.Ş.’nin 2026/Nisan dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(m9), secenekler(m9, 40_000 - 25_000, 40_000, 30_000, 10_000),
    "Md. 35'e göre malların iadesi hâlinde satıcı borçlandığı vergiyi değişikliğin olduğu dönemde düzeltir; iade edilen "
    "malların fiilen işletmeye girmesi şarttır: (200.000 − 50.000) × %20 = 30.000 ₺; 30.000 − 25.000 = 5.000 ₺.")

P.q("KDVK md. 20/4",
    f"{K}, fiyatı tarifeyle belirlenen veya bedeli biletle tahsil edilen işlemlere ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Tarife ve bilet bedeli KDV dahil tespit edilir ve vergi müşteriye ayrıca yansıtılmaz.",
    ["Bilet bedeline KDV ayrıca eklenerek müşteriden tahsil edilir.",
     "Biletle tahsil edilen bedeller KDV’den istisnadır.",
     "Bilet bedelinin yarısı KDV matrahı olarak kabul edilir.",
     "Tarifeli işlerde KDV, tarifeyi belirleyen kamu kurumunca ödenir."],
    "Md. 20/4'e göre belli bir tarifeye göre fiyatı tespit edilen işler ile bedelin biletle tahsil edildiği hâllerde tarife ve "
    "bilet bedeli KDV dahil edilerek tespit olunur ve vergi müşteriye ayrıca intikal ettirilmez.")

m10 = 2_000_000 * 0.20 - 250_000 - 90_000 - 30_000
P.sayisal("KDVK md. 29/1-ç",
    "(STU) A.Ş.’nin 2026/Ocak dönemi işlemleri: yurt içi teslimler 2.000.000 ₺ (KDV hariç); alış faturalarında gösterilen KDV "
    "250.000 ₺; Aralık 2025 döneminde aldığı yapım işi için sorumlu sıfatıyla 2 No.lu beyannameyle beyan edip Ocak 2026’da "
    "ödediği KDV 90.000 ₺; dönem sonu yabancı para değerlemesinden doğan kur farkı geliri 400.000 ₺; önceki dönemden devreden "
    f"KDV 30.000 ₺. {ORAN}\n\n{K}, (STU) A.Ş.’nin 2026/Ocak dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(m10), secenekler(m10, 400_000 - 250_000 - 30_000, m10 + 80_000, 400_000 - 250_000 - 90_000, m10 + 80_000 + 90_000),
    "Hesaplanan KDV 2.000.000 × %20 = 400.000 ₺; değerleme kur farkı bir teslim karşılığı olmadığından matraha girmez. Md. "
    "29/1-ç'ye göre sorumlu sıfatıyla beyan edilerek ödenen KDV indirilebilir: 400.000 − 250.000 − 90.000 − 30.000 = "
    "30.000 ₺.", zorluk="hard")

P.q("KDVK md. 30/a",
    f"{K}, vergiye tabi olmayan veya istisna edilmiş işlemlerle ilgili alış KDV’sine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Kural olarak indirilemez; Kanunda sayılan bazı istisnalar bu yasağın dışındadır.",
    ["Tüm istisnalı işlemlere ait alış KDV’si indirilebilir.",
     "Bu KDV talep edilince doğrudan iade edilir.",
     "Bu KDV sadece yıl sonunda toplu olarak indirilebilir.",
     "Bu KDV ithalatta gümrük idaresine ödenmişse indirilebilir, yurt içi alışlarda ise indirilemez."],
    "Md. 30/a'ya göre vergiye tabi olmayan veya istisna edilmiş işlemlerle ilgili alış KDV'si indirilemez; ancak md. 17/2-b, "
    "c, d ile 17/4-ı ve ö bentleri uyarınca istisna edilen işlemler bu yasağın dışında tutulmuştur.", zorluk="hard")

m11 = 30_000
P.sayisal("KDVK md. 29/1-c",
    "Basit usulde vergilendirilen Bay (M), 1 Ocak 2026’dan itibaren gerçek usulde vergilendirmeye geçmiştir. Çıkardığı "
    "envantere göre hesap dönemi başındaki mallarına ait faturalarda gösterilen KDV toplamı 30.000 ₺’dir. Ocak 2026 "
    f"döneminde teslimleri 500.000 ₺ (KDV hariç), diğer alışlarına ait KDV 40.000 ₺’dir. {ORAN}\n\n{K}, Bay (M)’nin Ocak "
    "2026 dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(100_000 - 40_000 - 30_000), secenekler(100_000 - 40_000 - 30_000, 100_000 - 40_000, 100_000, 100_000 - 30_000, 100_000 - 70_000 + 30_000 * 2),
    "Md. 29/1-c'ye göre götürü veya telafi edici usulden gerçek usule geçenler, envantere göre dönem başındaki mallara ait "
    "faturalarda gösterilen KDV'yi indirebilir: 500.000 × %20 = 100.000; 100.000 − 40.000 − 30.000 = 30.000 ₺.")

P.q("KDVK md. 29/1",
    "Gerçek usulde KDV mükellefi olan (LMN) Ltd. Şti. 2026/Mart döneminde çeşitli alışlar yapmıştır."
    f"\n\n{K}, aşağıdakilerden hangisi Kanunda sayılan indirilebilecek vergilerden biri değildir?",
    "KDV mükellefi olmayan bir kişiden alınan ve KDV gösterilmeyen gider pusulasındaki tutar",
    ["Kendisine yapılan teslim ve hizmetler dolayısıyla faturada gösterilen KDV",
     "İthal olunan mal ve hizmetler dolayısıyla ödenen KDV",
     "Sorumlu sıfatıyla beyan edilerek ödenen KDV",
     "Götürü usulden gerçek usule geçişte envanterdeki mallara ait faturalarda gösterilen KDV"],
    "Md. 29/1'e göre faturada gösterilen KDV, ithalatta ödenen KDV, götürü usulden gerçek usule geçişte envanterdeki mallara "
    "ait KDV ve sorumlu sıfatıyla beyan edilerek ödenen KDV indirilebilir. KDV hesaplanmayan belgedeki tutar indirim konusu "
    "olamaz.")

P.sayisal("KDVK md. 30/d",
    "(VYZ) A.Ş., ortağının ailesiyle yaptığı ve işletmeyle ilgisi bulunmayan tatil harcamasını şirket adına faturalandırarak "
    "gider yazmıştır; faturadaki KDV 12.000 ₺’dir. Aynı dönemde işletmeyle ilgili alışlara ait KDV 70.000 ₺, yurt içi "
    f"teslimler 600.000 ₺’dir (KDV hariç). {ORAN}\n\n{K}, (VYZ) A.Ş.’nin bu dönem ödenecek KDV tutarı kaç ₺’dir?",
    tl(120_000 - 70_000), secenekler(120_000 - 70_000, 120_000 - 82_000, 120_000, 120_000 - 70_000 + 12_000, 70_000),
    "Md. 30/d'ye göre gelir ve kurumlar vergisi kanunlarına göre indirimi kabul edilmeyen giderler dolayısıyla ödenen KDV "
    "indirilemez: 600.000 × %20 = 120.000; 120.000 − 70.000 = 50.000 ₺.")

P.q("KDVK md. 39/3",
    f"{K}, vergilendirme dönemlerine ilişkin Maliye Bakanlığının yetkileri hakkında aşağıdakilerden hangisi doğrudur?",
    "Mükellefleri gruplayıp gruplar için dönemlerin başlangıç aylarını belirleyebilir.",
    ["Vergilendirme dönemini bir yıldan uzun belirleyebilir.",
     "Sorumluların vergilendirme dönemini üç aylık olarak belirlemekle yükümlüdür.",
     "İthalat için yıllık vergilendirme dönemi belirleyebilir.",
     "Götürü usulde vergilendirilen mükellefler için takvim yılı yerine aylık vergilendirme dönemi belirleyebilir."],
    "Md. 39/3'e göre Maliye Bakanlığı mükellefleri gruplar içinde toplamaya ve gruplar için vergilendirme dönemlerinin "
    "başlangıç aylarını tespit etmeye yetkilidir; bu takdirde üçer aylık dönemlerin aynı takvim yılı içinde olması şartı "
    "aranmaz.", zorluk="hard")

m13 = 400_000 * 0.20 * 0.9
P.sayisal("KDVK md. 9",
    "(ZAB) A.Ş., KDV mükellefi olan bir temizlik firmasından 2026/Mart döneminde 400.000 ₺ (KDV hariç) temizlik hizmeti "
    "almıştır. Bu hizmet Maliye Bakanlığınca belirlenen kısmi tevkifat kapsamındadır. (Hizmet için KDV oranı %20, tevkifat "
    f"oranı 9/10 olarak alınacaktır.)\n\n{K}, (ZAB) A.Ş.’nin sorumlu sıfatıyla beyan edip ödeyeceği KDV kaç ₺’dir?",
    tl(m13), secenekler(m13, 80_000, 400_000 * 0.20 * 0.7, 400_000 * 0.20 * 0.5, 400_000 * 0.20 * 0.2),
    "Md. 9'a göre Maliye Bakanlığı vergi alacağının emniyeti için işlemlere taraf olanları verginin ödenmesinden sorumlu "
    "tutabilir. Hesaplanan KDV 80.000 ₺'nin 9/10'u (72.000 ₺) alıcı tarafından sorumlu sıfatıyla beyan edilip ödenir; "
    "kalan 8.000 ₺'yi satıcı beyan eder.")

P.q("KDVK md. 23/c",
    "Bir organizasyon şirketi, profesyonel sanatçıların yer aldığı bir konser düzenlemiş; giriş biletleri satmış ve konser "
    f"alanında yiyecek-içecek satışı yapmıştır.\n\n{K}, bu organizasyonda KDV matrahına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Giriş bedeli ile konser mahallinde yapılan teslim ve hizmetlerin bedeli özel matraha dahildir.",
    ["Sadece giriş bileti bedeli matraha dahildir, yiyecek-içecek satışları KDV dışıdır.",
     "Profesyonel sanatçı konserleri KDV’den istisnadır.",
     "Matrah, sanatçıya ödenen ücret düşüldükten sonra kalan tutardır.",
     "Konser alanındaki yiyecek-içecek satışları özel matraha dahil olup giriş bileti bedeli bu matraha dahil değildir."],
    "Md. 23/c'ye göre profesyonel sanatçıların yer aldığı gösteri ve konserlerde, icra edildikleri mahallere giriş karşılığında "
    "alınan bedel ile bu mahallerde yapılan teslim ve hizmetlerin bedeli özel matrahtır.")

m14 = 250_000 * 0.20 - (60_000 + 35_000)
P.sayisal("KDVK md. 29/2",
    "(CDE) A.Ş.’nin 2026/Haziran döneminde yurt içi teslimleri 250.000 ₺ (KDV hariç), alış faturalarındaki KDV 60.000 ₺, "
    f"önceki dönemden devreden KDV 35.000 ₺’dir. Dönemde iade hakkı doğuran işlem yoktur. {ORAN}\n\n{K}, (CDE) A.Ş.’nin "
    "2026/Temmuz dönemine devredecek KDV tutarı kaç ₺’dir?",
    tl(-m14), secenekler(-m14, 60_000 + 35_000, 60_000, 35_000, 0),
    "Hesaplanan KDV 250.000 × %20 = 50.000 ₺; indirilecek KDV 60.000 + 35.000 = 95.000 ₺. Md. 29/2'ye göre indirilecek KDV "
    "hesaplanandan fazla olursa fark sonraki döneme devrolunur ve iade edilmez: 95.000 − 50.000 = 45.000 ₺.", zorluk="easy")

P.q("KDVK md. 9",
    f"{K}, KDV’de vergi sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sorumlu sıfatıyla beyan edilip ödenen KDV, sorumlu tarafından indirim konusu yapılamaz.",
    ["Maliye Bakanlığı vergi alacağının emniyeti için işlemlere taraf olanları sorumlu tutabilir.",
     "Mükellefin Türkiye’de işyeri ve merkezinin bulunmaması sorumluluk uygulanabilecek hâllerdendir.",
     "Sorumluluk hâllerinde beyan vergi kesintisi yapmakla sorumlu tutulanlarca yapılır.",
     "Sorumlular için vergilendirme dönemi bir aydır."],
    "Md. 29/1-ç'ye göre vergi kesintisi yapmakla sorumlu tutulanlarca sorumlu sıfatıyla beyan edilerek ödenen KDV indirim "
    "konusu yapılabilir. Md. 9, 40/2 ve 39/2-b diğer ifadeleri doğrular.", zorluk="hard")

st = 400_000 * 0.20 * 0.1 - 5_000
P.sayisal("KDVK md. 9",
    "Temizlik hizmeti veren (OPR) Ltd. Şti., 2026/Nisan döneminde tek müşterisi olan bir anonim şirkete 400.000 ₺ (KDV hariç) "
    "hizmet vermiştir. Hizmet Maliye Bakanlığınca belirlenen kısmi tevkifat kapsamındadır. Şirketin dönem içi alışlarına ait "
    "KDV 5.000 ₺’dir, devreden KDV yoktur. (KDV oranı %20, tevkifat oranı 9/10 olarak alınacaktır.)"
    f"\n\n{K}, (OPR) Ltd. Şti.’nin 2026/Nisan dönemi 1 No.lu beyannamesinde ödenecek KDV kaç ₺’dir?",
    tl(st), secenekler(st, 80_000 - 5_000, 8_000, 72_000 - 5_000, 40_000 - 5_000),
    "Hesaplanan KDV 80.000 ₺'nin 9/10'u (72.000 ₺) alıcı tarafından sorumlu sıfatıyla ödenir. Satıcı tevkif edilmeyen "
    "8.000 ₺'yi beyan eder ve indirilecek KDV'yi düşer: 8.000 − 5.000 = 3.000 ₺.", zorluk="hard")

P.q("KDVK md. 29/3",
    f"{K}, indirim hakkının kullanılma zamanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İndirim hakkı sadece vergiyi doğuran olayın meydana geldiği ayın beyannamesinde kullanılabilir.",
    ["İndirim, belgelerin kanuni defterlere kaydedildiği dönemde kullanılabilir.",
     "Vergiyi doğuran olayın olduğu yılı izleyen takvim yılı aşılmamalıdır.",
     "Boru hattı ile sürekli akışlı mal ithalinde süresinde ödenen KDV ithalat döneminde indirilebilir.",
     "Belgede KDV’nin ayrıca gösterilmesi gerekir."],
    "Md. 29/3'e göre indirim hakkı, vergiyi doğuran olayın vuku bulduğu takvim yılını takip eden takvim yılı aşılmamak şartıyla "
    "belgelerin kanuni defterlere kaydedildiği dönemde kullanılabilir; boru hattıyla ithal edilen mallar için özel hüküm "
    "vardır.", zorluk="hard")

kd = 550_000 * 10 / 110
P.sayisal("KDVK md. 20, 25/b",
    "(STU) A.Ş., indirimli orana tabi bir teslimi için müşterisinden KDV dahil toplam 550.000 ₺ tahsil etmiştir; faturada "
    "KDV ayrıca gösterilmiştir. (Bu teslimde uygulanacak KDV oranı %10 olarak alınacaktır.)"
    f"\n\n{K}, bu teslim nedeniyle hesaplanan KDV kaç ₺’dir?",
    tl(kd), secenekler(kd, 55_000, 550_000 * 0.20 / 1.2, 49_500, 60_500),
    "Md. 25/b'ye göre hesaplanan KDV matraha dahil değildir; KDV dahil tutardan matrah 550.000 / 1,10 = 500.000 ₺, "
    "KDV 500.000 × %10 = 50.000 ₺'dir.", zorluk="easy")

P.q("KDVK md. 30",
    f"{K}, aşağıdakilerden hangisine ait KDV indirim konusu yapılabilir?",
    "Selde zayi olan emtia",
    ["Hırsızlık sonucu kaybolan emtia",
     "Kiralama işi yapmayan işletmenin binek otomobili",
     "Kanunen kabul edilmeyen gider sayılan harcama",
     "İndirim hakkı tanınmayan istisnalı işlem için alınan mal"],
    "Md. 30/c'ye göre deprem, sel ve Bakanlığın mücbir sebep ilan ettiği yerlerdeki yangın sonucu zayi olan mallar indirim "
    "yasağının dışındadır; hırsızlık zayii, binek otomobil (kiralama hariç), KKEG ve istisnalı işlemlere ait KDV "
    "indirilemez.")

al = 450_000 * 0.20 - (300_000 * 0.20 - 10_000)
P.sayisal("KDVK md. 35",
    "(VYZ) A.Ş. 2026/Mayıs döneminde 450.000 ₺ (KDV hariç) mal satmıştır. Aynı dönemde yaptığı 300.000 ₺ (KDV hariç) "
    "alışın KDV’sini indirim konusu yapacaktır; ancak bu alışlarının 50.000 ₺’lik kısmını kusurlu olduğu için aynı dönemde "
    f"satıcıya iade etmiş ve iade faturası düzenlemiştir. {ORAN}\n\n{K}, (VYZ) A.Ş.’nin 2026/Mayıs dönemi ödenecek KDV kaç "
    "₺’dir?",
    tl(al), secenekler(al, 90_000 - 60_000, 50_000, 90_000 - 60_000 - 10_000, 90_000),
    "Md. 35'e göre mal iadesinde alıcı indirdiği vergiyi değişikliğin olduğu dönemde düzeltir: indirilebilecek KDV (300.000 − "
    "50.000) × %20 = 50.000 ₺. Ödenecek KDV 90.000 − 50.000 = 40.000 ₺.")

P.q("KDVK md. 21",
    f"{K}, ithalatta KDV matrahına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gümrük vergisi matraha dahil edilmez, sadece malın CIF değeri esas alınır.",
    ["Gümrük vergisine esas kıymet matrahın unsurudur.",
     "Gümrük vergisinden muaf mallarda sigorta ve navlun dahil (CIF) değer esas alınır.",
     "Tescil tarihine kadar yapılan ve vergilendirilmeyen giderler matraha dahildir.",
     "Mal bedeli üzerinden hesaplanan kur farkı matraha dahildir."],
    "Md. 21/b'ye göre ithalat sırasında ödenen her türlü vergi, resim, harç ve paylar (gümrük vergisi dahil) ithalatta KDV "
    "matrahına dahildir.", zorluk="easy")

it = 2_500_000 * 0.20 - 200_000 - 150_000
P.sayisal("KDVK md. 29, 30/b",
    "(ZAB) A.Ş.’nin 2026/Haziran dönemi işlemleri: yurt içi teslimler 2.500.000 ₺ (KDV hariç); yurt içi alışlara ait KDV "
    "200.000 ₺; ithal edilen hammadde için gümrükte ödenen KDV 150.000 ₺; faaliyeti kiralama olmayan şirketin satın aldığı "
    f"binek otomobile ait KDV 60.000 ₺. {ORAN}\n\n{K}, (ZAB) A.Ş.’nin 2026/Haziran dönemi ödenecek KDV kaç ₺’dir?",
    tl(it), secenekler(it, 500_000 - 200_000, 500_000 - 410_000, 500_000 - 260_000, 500_000 - 150_000),
    "Md. 29/1'e göre faturada gösterilen ve ithalatta ödenen KDV indirilebilir; md. 30/b'ye göre kiralama faaliyeti "
    "olmayanların binek otomobil alış KDV'si indirilemez: 500.000 − 200.000 − 150.000 = 150.000 ₺.")

P.q("KDVK md. 23",
    f"{K}, özel matrah şekillerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müzayede mahallerinde yapılan satışlarda matrah, açılış fiyatıdır.",
    ["At yarışlarında matraha yarışa katılma bedeli ile giriş bedeli dahildir.",
     "Sikke altın tesliminde matrah, külçe altın bedeli düşüldükten sonra kalan miktardır.",
     "Maliye Bakanlığı işin mahiyetini göz önünde tutarak özel matrah şekilleri belirleyebilir.",
     "Gümrük depolarında yapılan satışlarda matrah kesin satış bedelidir."],
    "Md. 23/d'ye göre gümrük depolarında ve müzayede mahallerinde yapılan satışlarda matrah kesin satış bedelidir; açılış "
    "fiyatı esas alınmaz.")

vf = 36_000 * 20 / 120 + 600_000 * 0.20
P.sayisal("KDVK md. 24/c",
    "(CDE) Ltd. Şti. 2026/Temmuz döneminde 600.000 ₺ (KDV hariç) mal teslim etmiştir. Ayrıca geçmiş dönemde vadeli sattığı "
    "mal için müşterisinden KDV dahil 36.000 ₺ vade farkı tahsil etmiş ve fatura düzenlemiştir. "
    f"{ORAN}\n\n{K}, (CDE) Ltd. Şti.’nin 2026/Temmuz dönemi hesaplanan KDV toplamı kaç ₺’dir?",
    tl(vf), secenekler(vf, 120_000, 120_000 + 36_000 * 0.20, 120_000 + 36_000, 120_000 + 36_000 * 0.18),
    "Md. 24/c'ye göre vade farkı matraha dahildir; KDV dahil 36.000 ₺ içindeki vergi 36.000 × 20/120 = 6.000 ₺'dir. "
    "Toplam: 120.000 + 6.000 = 126.000 ₺.")

if __name__ == "__main__":
    sys.exit(P.yaz())
