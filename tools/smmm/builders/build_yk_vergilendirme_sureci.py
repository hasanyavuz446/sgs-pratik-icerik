# -*- coding: utf-8 -*-
"""Vergi · VUK · Vergilendirme Süreci (tarh, tebliğ, tahakkuk, tahsil, süreler, zamanaşımı; 6183) — 60 soru.

Gerçek 2026/1-2026/2 kitapçıklarında bu konu; ihtiyati haciz hâlleri ve süreleri, ödeme emrine karşı başvuru süresi,
tahsil zamanaşımını kesen hâller ve tarh zamanaşımı üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 213 sayılı VUK md. 13-24, 29-30, 93-107/A, 113-114;
6183 sayılı AATUHK md. 9-17, 35, 37, 48, 51, 54-61, 71, 102-106. Başvuru merciine ilişkin güncel metin ile 2026/1
kitapçığı arasındaki fark nedeniyle yalnız süre sorulur, merci sorulmaz.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_vergilendirme_sureci_2026.json", lesson="vergi_usul_kanunu", topic="vergilendirme_sureci",
          konu_adi="Vergilendirme Süreci", seed=2026092907,
          surum="213 sayılı VUK (7587 dahil) ve 6183 sayılı Kanun güncel metni; 29.09.2026 kontrolü")

V = "213 sayılı Vergi Usul Kanunu’na göre"
V26 = "213 sayılı Vergi Usul Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
A = "6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun’a göre"
A26 = "6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun’un 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("VUK md. 114",
    "Bay (K)’nın 2021 takvim yılına ait gelir vergisi alacağı, vergiyi doğuran olayın 2021 yılında gerçekleşmesiyle doğmuştur. "
    "Bay (K) beyanname vermemiş, vergi dairesi de takdir komisyonuna başvurmamıştır."
    f"\n\n{V}, bu vergi en geç hangi yılın sonuna kadar tarh edilip tebliğ edilmezse zamanaşımına uğrar?",
    "2026", ["2025", "2027", "2028", "2031"],
    "Md. 114'e göre vergi alacağının doğduğu takvim yılını takip eden yılın başından başlayarak beş yıl içinde tarh ve "
    "tebliğ edilmeyen vergiler zamanaşımına uğrar: 1 Ocak 2022'den itibaren beş yıl, 31 Aralık 2026'da dolar.")

P.q("VUK md. 19-23",
    "Bir vergi dairesi müdürü, yeni başlayan memurlara vergilendirme sürecinin aşamalarını anlatmaktadır."
    f"\n\n{V}, aşağıdaki tanımlardan hangisi yanlıştır?",
    "Tahakkuk, verginin kanuna uygun şekilde ödenmesidir.",
    ["Tarh, vergi alacağının matrah ve nispetler üzerinden hesaplanarak miktar olarak tespit edildiği idari işlemdir.",
     "Tebliğ, hüküm ifade eden hususların yetkili makamlarca mükellefe yazıyla bildirilmesidir.",
     "Vergi alacağı, vergiyi bağladıkları olayın vukuu veya hukuki durumun tekemmülü ile doğar.",
     "Tahakkuku tahsile bağlı vergilerde tahsil tahakkuku da içine alır."],
    "Md. 22'ye göre tahakkuk, tarh ve tebliğ edilen bir verginin ödenmesi gereken bir safhaya gelmesidir; verginin kanuna "
    "uygun şekilde ödenmesi md. 23'e göre tahsildir. Diğer tanımlar md. 19, 20, 21 ve 24'e uygundur.", zorluk="easy")

P.q("VUK md. 29-30",
    "Vergi incelemesi sonucunda, daha önce beyana dayalı olarak vergilendirilmiş bir mükellefin kayıtlarından tespit edilen "
    f"ve belgelere dayanan bir matrah farkı ortaya çıkmıştır.\n\n{V}, bu matrah farkı üzerinden yapılacak tarhiyat hangi "
    "türdedir?",
    "İkmalen vergi tarhı",
    ["Resen vergi tarhı", "İdarece vergi tarhı", "Beyana dayanan tarh", "Götürü tarh"],
    "Md. 29'a göre ikmalen tarh, bir vergi tarh edildikten sonra bu vergiye ilişkin ortaya çıkan ve defter, kayıt ve "
    "belgelere veya kanuni ölçülere dayanılarak miktarı tespit olunan matrah farkı üzerinden verginin tarh edilmesidir. "
    "Resen tarh ise matrahın bunlara dayanılarak tespit edilemediği hâllerdir.")

P.sayisal("VUK md. 114",
    "Vergi dairesi, bir mükellefin matrahının takdiri için takdir komisyonuna başvurmuş; komisyon kararını geç vermiştir."
    f"\n\n{V}, takdir komisyonuna başvuru nedeniyle işlemeyen tarh zamanaşımı süresi her hâlde en fazla kaç yıl olabilir?",
    "1", ["2", "3", "5", "6"],
    "Md. 114'e göre vergi dairesince takdir komisyonuna başvurulması zamanaşımını durdurur; duran zamanaşımı komisyon "
    "kararının vergi dairesine tevdiini takip eden günden itibaren işlemeye devam eder; ancak işlemeyen süre her hâl ve "
    "takdirde bir yıldan fazla olamaz.")

P.q("VUK md. 30",
    f"Vergi dairesi, bazı mükelleflerin matrahlarının defter ve belgelere dayanılarak tespit edilip edilemeyeceğini ve takdire sevk gerekip gerekmediğini değerlendirmektedir.\n\n{V}, aşağıdakilerden hangisi resen vergi tarhını gerektiren hâllerden biri değildir?",
    "Beyannamenin kanuni süresinde verilmiş olması",
    ["Beyannamenin kanuni süresi geçtiği hâlde verilmemesi",
     "Tutulması mecburi defterlerin tutulmaması veya tasdik ettirilmemesi",
     "Defterlerin inceleme yetkililerine herhangi bir sebeple ibraz edilmemesi",
     "Beyannamede matraha ilişkin bilgilerin gösterilmemesi"],
    "Md. 30'a göre beyannamenin süresinde verilmemesi, beyannamede matrah bilgilerinin gösterilmemesi, defterlerin "
    "tutulmaması, tasdik ettirilmemesi veya ibraz edilmemesi gibi hâllerde matrahın defter ve belgelere dayanılarak "
    "tespitinin mümkün olmadığı kabul edilir ve resen tarh yapılır.", zorluk="easy")

P.q("VUK md. 30",
    f"Defterlerini inceleme elemanına ibraz etmeyen bir mükellefin matrahının hangi yöntemle ve kimler tarafından belirleneceği tartışılmaktadır.\n\n{V}, resen vergi tarhına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Resen takdir sadece takdir komisyonlarınca yapılabilir.",
    ["Matrahın defter ve belgelere dayanılarak tespit edilemediği hâllerde yapılır.",
     "Vergi inceleme raporunda belirtilen matrah üzerinden de yapılabilir.",
     "İnceleme raporunda bu maddeye göre belirlenen matrah resen takdir olunmuş sayılır.",
     "Beyannamenin süresinde verilmemesi resen tarh sebebidir."],
    "Md. 30'a göre resen tarh, takdir komisyonlarınca takdir edilen veya vergi incelemesi yapmaya yetkili olanlarca "
    "düzenlenmiş inceleme raporlarında belirtilen matrah üzerinden yapılır; inceleme raporundaki matrah da resen takdir "
    "olunmuş sayılır.")

P.sayisal("6183 md. 102",
    "Bir mükellefin kesinleşmiş vergi borcunun vadesi 30 Nisan 2025’tir. Borç için hiçbir takip işlemi yapılmamış, borçlu "
    f"ödeme de yapmamıştır.\n\n{A}, bu amme alacağı en geç hangi yılın sonunda zamanaşımına uğrar?",
    "2030", ["2028", "2029", "2031", "2035"],
    "Md. 102'ye göre amme alacağı, vadesinin rastladığı takvim yılını takip eden takvim yılı başından itibaren beş yıl içinde "
    "tahsil edilmezse zamanaşımına uğrar: 1 Ocak 2026'dan itibaren beş yıl, 31 Aralık 2030.")

P.q("VUK md. 13, 15",
    f"Beyannamelerini süresinde veremeyen bazı mükellefler, gecikmenin sebebini vergi dairesine açıklayarak mücbir sebep hâlinden yararlanmak istemektedir.\n\n{V}, aşağıdakilerden hangisi Kanunda sayılan mücbir sebeplerden biri değildir?",
    "Mükellefin yoğun iş temposu",
    ["Ödevlerin yerine getirilmesine engel olacak ağır hastalık",
     "Ödevlerin yerine getirilmesine engel olacak yangın ve su basması",
     "Kişinin iradesi dışındaki mecburi gaybubet",
     "Defter ve belgelerin sahibinin iradesi dışında elinden çıkması"],
    "Md. 13'e göre ağır kaza, ağır hastalık ve tutukluluk; yangın, yer sarsıntısı ve su basması gibi afetler; iradesi "
    "dışındaki mecburi gaybubetler ve defter ve belgelerin iradesi dışında elden çıkması mücbir sebeptir.", zorluk="easy")

P.q("VUK md. 15",
    "Mükellef Bay (S), beyanname verme süresi devam ederken ağır bir trafik kazası geçirmiş ve iki ay hastanede kalmıştır."
    f"\n\n{V}, bu durumun sonuçlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mücbir sebep ortadan kalkıncaya kadar süreler işlemez.",
    ["Süreler işlemeye devam eder, sadece ceza indirimli uygulanır.",
     "Mücbir sebep hâlinde tarh zamanaşımı kısalır.",
     "Mücbir sebebin ispatı gerekmez, beyan yeterlidir.",
     "Süreler işler, ancak Bakanlık resen mühlet verir."],
    "Md. 15'e göre md. 13'teki mücbir sebeplerden birinin bulunması hâlinde bu sebep ortadan kalkıncaya kadar süreler "
    "işlemez ve tarh zamanaşımı işlemeyen süre kadar uzar; mücbir sebebin malum olması veya ispat edilmesi gerekir.")

P.sayisal("6183 md. 102-103",
    "Vadesi 2022 yılında olan bir amme alacağı için borçluya 2024 yılı Mart ayında haciz tatbik edilmiştir; başka bir "
    f"kesme sebebi yoktur.\n\n{A}, bu alacak en geç hangi yılın sonunda zamanaşımına uğrar?",
    "2029", ["2027", "2028", "2030", "2032"],
    "Md. 103'e göre haciz tatbiki zamanaşımını keser; kesilmenin rastladığı takvim yılını takip eden takvim yılı başından "
    "itibaren zamanaşımı yeniden işler: 1 Ocak 2025'ten itibaren beş yıl, 31 Aralık 2029.", zorluk="hard")

P.q("VUK md. 17",
    f"{V}, zor durum nedeniyle mühlet verilmesinin şartları arasında aşağıdakilerden hangisi yer almaz?",
    "Mükellefin mühlet için teminat göstermesi",
    ["Mühletin sürenin bitmesinden önce yazıyla istenmesi",
     "Gösterilen mazeretin mühlet verecek makamca kabule layık görülmesi",
     "Mühlet verilmesi hâlinde verginin alınmasının tehlikeye girmemesi",
     "Mühletin kanuni sürenin bir katını aşmaması"],
    "Md. 17'ye göre mühlet için sürenin bitmesinden önce yazılı istem, mazeretin kabule layık görülmesi ve verginin "
    "alınmasının tehlikeye girmemesi gerekir; mühlet kanuni sürenin bir katını geçemez. Teminat şartı öngörülmemiştir.",
    zorluk="hard")

P.q("VUK md. 18",
    f"Bir mükellef, kendisine tebliğ edilen ihbarnameye karşı başvuru süresinin hangi gün dolacağını ve tatil günlerinin etkisini hesaplamaktadır.\n\n{V}, sürelerin hesaplanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Resmî tatil günleri süreye dahil edilmez.",
    ["Gün olarak belirlenen sürede başladığı gün hesaba katılmaz.",
     "Ay olarak belirlenen süre, son ayda başladığı güne karşılık gelen günün tatil saatinde biter.",
     "Sonu belli bir gün ile belirlenen süre o günün tatil saatinde biter.",
     "Sürenin son günü resmî tatile rastlarsa süre izleyen ilk iş gününün tatil saatinde biter."],
    "Md. 18/4'e göre resmî tatil günleri süreye dahildir; ancak sürenin son günü resmî tatile rastlarsa süre tatili takip "
    "eden ilk iş gününün tatil saatinde biter.")

gz = 100_000 * 0.037 * 3
P.sayisal("6183 md. 51",
    "Bay (L)’nin vadesi 31 Mart 2026 olan 100.000 ₺ gelir vergisi borcu, 30 Haziran 2026’da ödenmiştir. (Aylık gecikme "
    f"zammı oranı %3,7 olarak alınacak ve ay kesri bulunmamaktadır.)\n\n{A26}, Bay (L)’nin ödeyeceği gecikme zammı kaç ₺’dir?",
    tl(gz), secenekler(gz, 3_700, 100_000 * 0.037 * 4, 100_000 * 0.04 * 3, 100_000 * 0.037 * 12),
    "Md. 51'e göre ödeme süresi içinde ödenmeyen amme alacağına vadenin bitiminden itibaren her ay için gecikme zammı "
    "uygulanır: Nisan, Mayıs, Haziran için 100.000 × %3,7 × 3 = 11.100 ₺.")

P.q("VUK md. 93-94",
    "Vergi dairesi, (GHI) A.Ş. adına düzenlenen ihbarnameyi şirketin işyeri adresine tebliğe çıkarmıştır. Şirket yetkilisi "
    f"adreste bulunamamış, ihbarname işyerinde çalışan 17 yaşında bir stajyere verilmiştir.\n\n{V}, bu tebliğe ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Muhatap yerine tebliğ yapılan kişi 18 yaşından küçük olduğundan tebliğ usulsüzdür.",
    ["İşyerinde bulunan herkes tebliğ alabileceğinden tebliğ geçerlidir.",
     "Tüzel kişilere tebliğ sadece ilan yoluyla yapılabilir.",
     "Tebliğ sadece şirketin ortaklarına yapılabilir.",
     "Tebliğ geçerlidir; yaş şartı sadece gerçek kişilere tebliğde aranır."],
    "Md. 94'e göre tüzel kişilere tebliğ başkan, müdür veya kanuni temsilcilerine yapılır; bunlar bulunmazsa işyerindeki "
    "memur veya müstahdemlerden birine yapılabilir. Ancak bu kişinin görünüşüne göre 18 yaşından aşağı olmaması ve bariz "
    "ehliyetsiz bulunmaması gerekir.", zorluk="hard")

P.q("VUK md. 93",
    f"Bir vergi dairesi, düzenlediği ihbarname ve kararların mükelleflere hangi yollarla ulaştırılacağını belirlemek üzere tebliğ usullerini gözden geçirmektedir.\n\n{V}, tebliğ usullerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Adresi bilinmeyenlere tebliğ ilan yoluyla yapılır.",
    ["Adresi bilinenlere tebliğ sadece ilan yoluyla yapılır.",
     "Tebliğ sadece memur vasıtasıyla yapılabilir.",
     "Tebliğin daire veya komisyonda yapılması kanunen mümkün değildir.",
     "Tahakkuk fişleri de posta yoluyla tebliğ edilir."],
    "Md. 93'e göre tahakkuk fişinden gayri hüküm ifade eden vesikalar adresi bilinenlere posta vasıtasıyla ilmühaberli "
    "taahhütlü olarak, adresi bilinmeyenlere ilan yoluyla tebliğ edilir; ilgilinin kabulü şartıyla tebliğ daire veya "
    "komisyonda da yapılabilir.", zorluk="easy")

gz2 = 40_000 * 0.037 * 2
P.sayisal("6183 md. 51",
    "Bir mükellefe kesilen ve vadesi 31 Mart 2026 olan 40.000 ₺ vergi ziyaı cezası ile 10.000 ₺ özel usulsüzlük cezası 31 "
    "Mayıs 2026’da ödenmiştir. (Aylık gecikme zammı oranı %3,7 olarak alınacak ve ay kesri bulunmamaktadır.)"
    f"\n\n{A26}, bu cezalar için ödenecek gecikme zammı toplamı kaç ₺’dir?",
    tl(gz2), secenekler(gz2, 50_000 * 0.037 * 2, 0, 40_000 * 0.037 * 2 / 2, 10_000 * 0.037 * 2),
    "Md. 51'e göre gecikme zammı VUK'a göre uygulanan vergi ziyaı cezalarında aynı oranda uygulanır; bunların dışındaki "
    "ceza mahiyetindeki amme alacaklarına (mahkeme cezaları hariç) gecikme zammı tatbik edilmez: 40.000 × %3,7 × 2 = "
    "2.960 ₺.", zorluk="hard")

P.q("VUK md. 102",
    "Posta memuru, bir mükellefin ikametgâhına götürdüğü vergi ihbarnamesini mükellef imzalamaktan kaçındığı için teslim "
    f"edememiş; tebliğ evrakının vergi dairesinden alınabileceğine ilişkin pusulayı kapıya yapıştırmıştır.\n\n{V}, tebliğ "
    "hangi tarihte yapılmış sayılır?",
    "Pusulanın kapıya yapıştırıldığı tarihte",
    ["Mükellefin vergi dairesine gelip evrakı aldığı tarihte",
     "Pusulanın yapıştırılmasından bir ay sonra",
     "Evrakın vergi dairesine iade edildiği tarihte",
     "İlan yoluyla yapılacak tebliğin tamamlandığı tarihte"],
    "Md. 102'ye göre muhatap tebellüğden imtina ederse tebliğ evrakının idareden alınabileceği şerhini içeren pusula kapıya "
    "yapıştırılır ve tebliğ pusulanın kapıya yapıştırıldığı tarihte yapılmış sayılır.")

P.q("VUK md. 101",
    f"Vergi dairesi, bir mükellefe gönderilecek ihbarnamenin hangi adrese tebliğ edileceğini ve hangi adreslerin bilinen adres sayılacağını belirlemektedir.\n\n{V}, tebliğ bakımından “bilinen adresler” arasında aşağıdakilerden hangisi yer almaz?",
    "Mükellefin sosyal medya profilinde yer alan adres",
    ["İşe başlamada veya adres değişikliğinde bildirilen işyeri adresi",
     "Yoklama fişinde veya ilgilinin imzalı tutanağında tespit edilen işyeri adresi",
     "Adres kayıt sistemindeki yerleşim yeri adresi",
     "Adres değişikliğinde vergi dairesine bildirilen yeni işyeri adresi"],
    "Md. 101'e göre bilinen adresler; işe başlamada veya adres değişikliğinde bildirilen işyeri adresleri, yoklama fişinde "
    "veya imzalı tutanakla tespit edilen işyeri adresleri ve adres kayıt sistemindeki yerleşim yeri adresidir.")

tm = (1_600_000 - 1_000_000) / 2
P.sayisal("6183 md. 48",
    "Bir şirket, tahsil dairesindeki toplam 1.600.000 ₺ vergi borcunun tecilini talep etmiştir. (Kanundaki teminat "
    f"tutarlarının Cumhurbaşkanınca değiştirilmediği kabul edilecektir.)\n\n{A}, tecil için gösterilmesi zorunlu teminat "
    "tutarı kaç ₺’dir?",
    tl(tm), secenekler(tm, 1_600_000, 600_000, 800_000, 0),
    "Md. 48'e göre tecil edilen borçların toplamı bir milyon Türk lirasını aşmıyorsa teminat aranmaz; bu tutarın üzerindeki "
    "alacaklarda gösterilmesi zorunlu teminat, bir milyon Türk lirasını aşan kısmın yarısıdır: (1.600.000 − 1.000.000) / 2 "
    "= 300.000 ₺.", zorluk="hard")

P.q("VUK md. 107/A",
    f"{V26}, elektronik tebligata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurumlar vergisi mükellefleri için sistem isteğe bağlıdır.",
    ["Gerçek usulde vergilendirilen ticari kazanç mükellefleri sistemi kullanmakla yükümlüdür.",
     "Kollektif ve adi komandit şirketler sistemi kullanmakla yükümlüdür.",
     "Zorunlu olmayanlar talep ederlerse sisteme dahil olabilir.",
     "65 yaşını doldurmuş kişiler talep ederlerse sistemden çıkarılır."],
    "Md. 107/A'nın 7587 sayılı Kanunla değişik hâline göre kurumlar vergisi mükellefleri, gerçek usulde vergilendirilen "
    "ticari, zirai ve mesleki kazanç mükellefleri ve kollektif ile adi komandit şirketler elektronik tebligat sistemini "
    "kullanmak zorundadır; 65 yaşını dolduranlar talep ederse sistemden çıkarılır.", zorluk="hard")

P.q("VUK md. 104",
    f"Vergi dairesi, bilinen son adresinde bulunamayan ve yeni adresi tespit edilemeyen bir mükellefe ihbarnameyi ilan yoluyla tebliğ etmeye karar vermiştir.\n\n{V}, ilanen tebliğe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bir sureti son adresin bağlı olduğu muhtarlığa gönderilir.",
    ["İlan sadece Türkiye genelinde yayımlanan gazetelerde yapılır.",
     "İlan yazısı vergi dairesinde asılmaz, sadece internette yayımlanır.",
     "Tutarı ne olursa olsun tüm ilanlar gazetede yayımlanır.",
     "İlanen tebliğ sadece tüzel kişilere uygulanır."],
    "Md. 104'e göre ilan yazısı vergi dairesinin ilan mahalline asılır, bir sureti mükellefin bilinen son adresinin bağlı "
    "olduğu muhtarlığa gönderilir; gazetede ve internette ilan yapılıp yapılmayacağı ve yayın yeri vergi veya ceza tutarına "
    "göre belirlenir.")

P.sayisal("6183 md. 48",
    f"Ödeme güçlüğü içindeki bir mükellef, vergi borcunun tecilini istemektedir.\n\n{A}, amme alacağı borçlunun yazılı talebi "
    "ve teminat şartıyla en fazla kaç ay süreyle tecil edilebilir?",
    "72", ["12", "36", "48", "60"],
    "Md. 48'e göre amme alacağı, borçlunun yazılı talebi ve teminat gösterilmesi şartıyla 72 ayı geçmemek üzere ve faiz "
    "alınarak tecil olunabilir.")

P.q("VUK md. 113-114",
    f"Bir vergi müfettişi, incelediği mükellefin geçmiş yıllara ait vergilerinin hâlâ tarh edilip edilemeyeceğini ve sürenin nasıl işlediğini değerlendirmektedir.\n\n{V}, tarh zamanaşımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zamanaşımı ancak mükellefin başvurusu üzerine hüküm ifade eder.",
    ["Zamanaşımı, süre geçmesi suretiyle vergi alacağının kalkmasıdır.",
     "Süre vergi alacağının doğduğu yılı takip eden yıl başından başlar.",
     "Takdir komisyonuna başvuru zamanaşımını durdurur.",
     "Şarta bağlı istisnalarda süre, şartların ihlal edildiği tarihi takip eden yıl başından başlar."],
    "Md. 113'e göre zamanaşımı, mükellefin bu hususta bir müracaatı olup olmadığına bakılmaksızın hüküm ifade eder.")

P.q("VUK md. 114",
    "(JKL) A.Ş., 2019 yılında şarta bağlı bir KDV istisnasından yararlanmış, ancak istisnanın şartlarını 2024 yılında ihlal "
    f"etmiştir.\n\n{V}, bu nedenle alınmayan verginin tarh zamanaşımı ne zaman başlar?",
    "2025 yılı başından itibaren",
    ["2019 yılı başından itibaren", "2020 yılı başından itibaren", "2024 yılı başından itibaren",
     "Şartın ihlal edildiği günden itibaren"],
    "Md. 114/3'e göre şarta bağlı istisna veya muafiyet uygulamaları sonucu alınmayan vergilere ilişkin zamanaşımı süresi, "
    "şartların ihlal edildiği tarihi takip eden takvim yılı başından itibaren başlar: 1 Ocak 2025.", zorluk="hard")

hc = 60_000 / 4
P.sayisal("6183 md. 71",
    "Amme borçlusu Bay (M)’nin aylık net ücreti 60.000 ₺ olup bu tutar asgari ücretin üzerindedir. Tahsil dairesi ücrete "
    f"haciz koyacaktır.\n\n{A26}, Bay (M)’nin ücretinden aylık olarak haczedilebilecek en az tutar kaç ₺’dir?",
    tl(hc), secenekler(hc, 60_000 / 3, 6_000, 30_000, 60_000),
    "Md. 71'e göre aylık ve ücretler kısmen haczolunabilir; haczolunacak miktar bunların üçte birinden çok, dörtte birinden "
    "az olamaz: en az 60.000 / 4 = 15.000 ₺, en fazla 20.000 ₺.", zorluk="hard")

P.q("6183 md. 103-104",
    f"{A}, aşağıdakilerden hangisi tahsil zamanaşımını kesen hâllerden biri değildir?",
    "Borçlunun hileli iflas etmesi",
    ["Ödeme emri tebliği", "Haciz tatbiki", "Amme alacağının teminata bağlanması",
     "Amme alacağının özel kanunlara göre ödeme planına bağlanması"],
    "Md. 103'e göre ödeme, haciz, cebren tahsilat, ödeme emri tebliği, mal bildirimi, teminata bağlama ve ödeme planına "
    "bağlama zamanaşımını keser. Md. 104'e göre borçlunun yabancı memlekette bulunması, hileli iflası veya terekenin "
    "tasfiyesi zamanaşımını keser değil, durdurur.", zorluk="hard")

P.q("6183 md. 102",
    f"{A}, tahsil zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zamanaşımından sonra mükellefin rızaen yaptığı ödemeler kabul olunur.",
    ["Zamanaşımına uğrayan borç için yapılan ödemeler iade edilir.",
     "Tahsil zamanaşımı süresi on yıldır.",
     "Süre vadenin rastladığı günden başlar.",
     "Para cezalarında özel kanunlardaki zamanaşımı hükümleri uygulanmaz."],
    "Md. 102'ye göre amme alacağı vadenin rastladığı yılı takip eden yıl başından itibaren beş yılda zamanaşımına uğrar; "
    "para cezalarına ait özel hükümler saklıdır ve zamanaşımından sonra rızaen yapılan ödemeler kabul olunur.")

lo = 400_000 * 0.30
P.sayisal("6183 md. 35",
    "(ABC) Ltd. Şti.’nden tahsil edilemeyen 400.000 ₺ amme alacağı bulunmaktadır. Şirket ortağı Bay (N)’nin sermaye "
    f"payı %30’dur ve payını devretmemiştir.\n\n{A}, Bay (N)’nin bu alacaktan sorumlu olduğu tutar kaç ₺’dir?",
    tl(lo), secenekler(lo, 400_000, 200_000, 0, 400_000 * 0.70),
    "Md. 35'e göre limited şirket ortakları, şirketten tahsil edilemeyen amme alacağından sermaye hisseleri oranında "
    "doğrudan sorumludur: 400.000 × %30 = 120.000 ₺.")

P.q("6183 md. 13",
    f"{A}, aşağıdakilerden hangisi ihtiyati haciz uygulanmasını gerektiren hâllerden biri değildir?",
    "Borçlunun vergi borcunu taksitle ödemesi",
    ["Borçlunun belli ikametgâhının olmaması",
     "Borçlunun mallarını kaçırması ihtimalinin bulunması",
     "Teminat istendiği hâlde belli sürede teminat gösterilmemesi",
     "Mal bildirimine çağrılan borçlunun eksik bildirimde bulunması"],
    "Md. 13'e göre teminat istenmesini gerektiren hâller, belli ikametgâhın olmaması, kaçma veya mal kaçırma ihtimali, "
    "istenen teminatın gösterilmemesi, mal bildiriminde bulunmama veya eksik bildirim, para cezasını gerektiren fiil nedeniyle "
    "kamu davası açılması ve iptal davası konusu mallar ihtiyati haciz sebebidir.", zorluk="easy")

P.q("6183 md. 13",
    "Vergi incelemesi sırasında, (MNO) A.Ş.’nin ortaklarının şirkete ait gayrimenkulleri hızla elden çıkardığı ve kaçma "
    f"hazırlığı içinde oldukları tespit edilmiştir.\n\n{A}, bu durumda ihtiyati haciz hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Mahalli en büyük memurun kararıyla derhal uygulanır.",
    ["Ancak amme alacağı kesinleştikten sonra uygulanabilir.",
     "Vergi mahkemesi kararı olmadan uygulanamaz.",
     "Borçluya önce 30 gün süre verilmesi gerekir.",
     "Sadece taşınmazlar üzerinde uygulanabilir."],
    "Md. 13'e göre ihtiyati haciz, sayılan hâllerden birinin varlığında hiçbir süreyle bağlı olmaksızın alacaklı amme "
    "idaresinin mahalli en büyük memurunun kararıyla, haczin nasıl yapılacağına dair hükümlere göre derhal uygulanır.",
    zorluk="hard")

P.sayisal("6183 md. 55",
    f"Vadesinde ödenmeyen bir vergi borcu için borçluya ödeme emri tebliğ edilmiştir.\n\n{A}, ödeme emrinde borçluya "
    "borcunu ödemesi veya mal bildiriminde bulunması için kaç günlük süre verilir?",
    "15", ["7", "10", "30", "60"],
    "Md. 55'e göre amme alacağını vadesinde ödemeyenlere, 15 gün içinde borçlarını ödemeleri veya mal bildiriminde "
    "bulunmaları lüzumu bir ödeme emri ile tebliğ olunur.", zorluk="easy")

P.q("6183 md. 9",
    f"Vergi incelemesi devam eden ve hakkında vergi ziyaı cezası kesilmesi muhtemel bir mükellefin borcunun güvence altına alınması düşünülmektedir.\n\n{A}, teminat istenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi ziyaı gerektiren hâllerde ilk hesaplara göre istenir.",
    ["Teminat sadece vergi kesinleştikten sonra istenebilir.",
     "Türkiye’de ikametgâhı bulunmayan borçludan teminat istenemez.",
     "Teminat miktarı borçlunun beyanına göre belirlenir.",
     "Teminat istenmesi mahkeme kararına bağlıdır."],
    "Md. 9'a göre VUK md. 344'e göre vergi ziyaı cezası kesilmesini gerektiren hâller ile md. 359'daki hâllere temas eden "
    "bir amme alacağı için muamelelere başlanmışsa inceleme yetkililerinin ilk hesaplarına göre teminat istenir; tahsili "
    "tehlikede olan ve Türkiye'de ikametgâhı bulunmayan borçludan da teminat istenebilir.")

P.q("6183 md. 10",
    f"Kendisinden teminat istenen bir borçlu, tahsil dairesine teminat olarak kabul edilmesi için çeşitli değerler sunmaktadır.\n\n{A}, aşağıdakilerden hangisi teminat olarak kabul edilmez?",
    "Borçlunun kendi düzenlediği bono",
    ["Para",
     "Bankaların verdiği süresiz ve şartsız teminat mektubu",
     "Hazine tarafından ihraç edilen Devlet iç borçlanma senetleri",
     "İlgililerce gösterilen ve haczedilen menkul ve gayrimenkul mallar"],
    "Md. 10'a göre para, bankaların süresiz ve şartsız teminat mektupları ile sigorta şirketlerinin kefalet senetleri, Devlet "
    "iç borçlanma senetleri, Hükümetçe belli edilecek esham ve tahvilat ile haczedilen menkul ve gayrimenkul mallar teminat "
    "olarak kabul edilir.")

P.sayisal("6183 md. 61",
    "Mal bildiriminde malı olmadığını bildiren amme borçlusu Bay (P), daha sonra miras yoluyla bir daire edinmiştir."
    f"\n\n{A}, Bay (P) bu edinimi edinme tarihinden itibaren en geç kaç gün içinde tahsil dairesine bildirmelidir?",
    "15", ["7", "10", "30", "90"],
    "Md. 61'e göre malı olmadığını veya borca yetecek kadar mal göstermediğini bildiren borçlu, sonradan edindiği malları ve "
    "gelirindeki artmaları edinme ve artma tarihinden başlayarak 15 gün içinde tahsil dairesine bildirmeye mecburdur.")

P.q("6183 md. 17",
    f"{A}, ihtiyati tahakkuka ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tahakkuk etmemiş vergiyi derhal tahakkuk ettirir.",
    ["Tahakkuk etmiş vergilerin ödeme süresini uzatır.",
     "Sadece gümrük vergilerine uygulanır.",
     "Vergi mahkemesi kararıyla uygulanır.",
     "Ödeme emri tebliğ edildikten sonra uygulanabilir."],
    "Md. 17'ye göre ihtiyati haciz sebeplerinden bazılarının varlığında veya takibat hâlinde, vergi dairesinin talebiyle "
    "defterdar veya vergi dairesi başkanı, mükellefin henüz tahakkuk etmemiş vergi ve resimlerinin derhal tahakkuk "
    "ettirilmesi için yazılı emir verebilir.")

P.q("6183 md. 37",
    "Hususi kanununda ödeme zamanı belirlenmemiş bir amme alacağı borçluya tebliğ edilmiştir."
    f"\n\n{A}, bu amme alacağının ödeme süresi hakkında aşağıdakilerden hangisi doğrudur?",
    "Tebliğden itibaren bir ay içinde ödenir.",
    ["Tebliğden itibaren 15 gün içinde ödenir.",
     "Tebliğden itibaren üç ay içinde ödenir.",
     "Takvim yılı sonuna kadar ödenir.",
     "Borçlunun belirleyeceği tarihte ödenir."],
    "Md. 37'ye göre hususi kanunlarında ödeme zamanı belirlenmemiş amme alacakları, tebliğden itibaren bir ay içinde ödenir; "
    "bu sürenin son günü vade günüdür. Borçlu isterse borcunu önceden ödeyebilir.")

P.sayisal("6183 md. 60",
    "Ödeme emri tebliğ edilen borçlu, 15 günlük süre içinde ne borcunu ödemiş ne de mal bildiriminde bulunmuştur."
    f"\n\n{A}, bu borçlu hakkında uygulanabilecek hapisle tazyik en fazla kaç ay olabilir?",
    "3", ["1", "2", "6", "12"],
    "Md. 60'a göre borcunu ödemeyen ve mal bildiriminde de bulunmayan borçlu, mal bildiriminde bulununcaya kadar bir defaya "
    "mahsus olmak ve üç ayı geçmemek üzere hapisle tazyik olunur; karar icra hâkimince verilir.")

P.q("6183 md. 48",
    f"{A}, amme alacaklarının tecil edilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tecil hâlinde faiz alınmaz.",
    ["Vadesinde ödeme borçluyu çok zor duruma düşürecekse tecil yapılabilir.",
     "Tecil borçlunun yazılı talebine bağlıdır.",
     "Tecil süresi 72 ayı geçemez.",
     "Tecil talebi reddedilenlere ödeme için 30 güne kadar süre verilebilir."],
    "Md. 48'e göre amme alacağı 72 ayı geçmemek üzere ve faiz alınarak tecil olunabilir; talebi reddedilenlere 30 güne kadar "
    "ödeme süresi verilebilir.")

P.q("6183 md. 51",
    f"{A}, gecikme zammına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gecikme zammı mahkemelerce verilen cezalara da tam oranda uygulanır.",
    ["Vadenin bitiminden itibaren her ay için ayrı ayrı uygulanır.",
     "Ay kesirlerine isabet eden gecikme zammı günlük olarak hesaplanır.",
     "VUK’a göre uygulanan vergi ziyaı cezalarına aynı oranda uygulanır.",
     "Cumhurbaşkanı gecikme zammı oranını belirli sınırlar içinde değiştirebilir."],
    "Md. 51'e göre gecikme zammı mahkemelerce verilen ve ceza mahiyetinde olan amme alacaklarında belirlenen oranın yarısı "
    "ölçüsünde uygulanır; vergi ziyaı cezalarında tam oranda uygulanır, diğer ceza mahiyetindeki alacaklara uygulanmaz.",
    zorluk="hard")

P.sayisal("6183 md. 105",
    "Çiftçi Bay (R)’nin ürünlerinin yarısı dolu afeti sonucu zarar görmüştür. Bay (R), bu gelir kaynağıyla ilgili amme "
    f"alacaklarının terkinini istemektedir.\n\n{A}, Bay (R) afetin vukuu tarihinden itibaren en geç kaç ay içinde ilgili "
    "idareye yazıyla başvurmalıdır?",
    "6", ["1", "3", "12", "24"],
    "Md. 105'e göre afetler yüzünden varlıklarının ve mahsullerinin en az üçte birini kaybedenler adına tahakkuk ettirilmiş "
    "ilgili amme alacakları Cumhurbaşkanı kararıyla terkin olunabilir; bunun için afetin vukuu tarihinden itibaren 6 ay "
    "içinde yazıyla başvurulması şarttır.")

P.q("6183 md. 54",
    f"{A}, aşağıdakilerden hangisi cebren tahsil yollarından biri değildir?",
    "Borçlunun borcunun Hazine tarafından üstlenilmesi",
    ["Teminatın paraya çevrilmesi",
     "Kefilin takibi",
     "Borçlunun mallarının haczedilerek paraya çevrilmesi",
     "Şartları varsa borçlunun iflasının istenmesi"],
    "Md. 54'e göre cebren tahsil; teminatın paraya çevrilmesi veya kefilin takibi, borçlunun mallarının haczedilerek paraya "
    "çevrilmesi ve şartları varsa iflasın istenmesi yollarıyla yapılır.", zorluk="easy")

P.q("6183 md. 58",
    f"{A}, ödeme emrine karşı başvuruda ileri sürülebilecek sebepler arasında aşağıdakilerden hangisi yer almaz?",
    "Borcun miktarının borçlunun ödeme gücünü aştığı",
    ["Böyle bir borcun olmadığı",
     "Borcun kısmen ödendiği",
     "Borcun zamanaşımına uğradığı",
     "Borcun tamamen ödendiği"],
    "Md. 58'e göre ödeme emri tebliğ olunan kişi böyle bir borcu olmadığı, kısmen ödediği veya borcun zamanaşımına uğradığı "
    "iddiasıyla 15 gün içinde başvurabilir; ödeme gücünün yetersizliği ödeme emrine karşı başvuru sebebi değildir.",
    zorluk="hard")

P.sayisal("6183 md. 15",
    "Borçlu (DEF) A.Ş.’ye kendi huzurunda ihtiyati haciz uygulanmıştır. Şirket, ihtiyati haczin sebebinin yerinde "
    f"olmadığını düşünmektedir.\n\n{A}, şirket ihtiyati haciz sebebine karşı haczin tatbiki tarihinden itibaren en geç kaç "
    "gün içinde başvurabilir?",
    "15", ["7", "10", "30", "60"],
    "Md. 15'e göre haklarında ihtiyati haciz uygulananlar, haczin tatbiki, gıyapta yapılan hacizlerde haczin tebliği "
    "tarihinden itibaren 15 gün içinde ihtiyati haciz sebebine karşı başvurabilir (süre 7061 sayılı Kanunla 7 günden 15 "
    "güne çıkarılmıştır).")

P.q("6183 md. 58",
    "Kendisine ödeme emri tebliğ edilen Bay (T), borcun sadece bir kısmına itiraz etmek istemektedir."
    f"\n\n{A}, bu kısmi başvuruya ilişkin aşağıdakilerden hangisi doğrudur?",
    "İtiraz edilen kısmın cihet ve miktarı açıkça gösterilmelidir.",
    ["Kısmi itirazda miktar belirtmek gerekmez.",
     "Kısmi itiraz mal bildirimi süresini uzatır.",
     "Borcun bir kısmına itiraz edilemez.",
     "Kısmi itiraz borcun tamamının takibini durdurur."],
    "Md. 58'e göre borcun bir kısmına itiraz eden borçlu o kısmın cihet ve miktarını açıkça göstermelidir; aksi hâlde "
    "itiraz edilmemiş sayılır. Borcun bir kısmına karşı yapılan başvuru mal bildirimi süresini uzatmaz.")

P.q("6183 md. 71",
    f"{A26}, kısmen haczedilebilen gelirlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Asgari ücreti aşmayan aylık gelirlerin yarısı haczolunabilir.",
    ["Aylık ve ücretler kısmen haczolunabilir.",
     "Haczolunacak miktar üçte birden çok olamaz.",
     "Haczolunacak miktar dörtte birden az olamaz.",
     "Emeklilik aylıkları kısmen haczolunabilecek gelirlerdendir."],
    "Md. 71'e göre aylık, ücret ve emeklilik aylıkları kısmen haczolunabilir; miktar üçte birden çok, dörtte birden az "
    "olamaz. Asgari ücreti aşmayan aylık gelirlerin onda birinden fazlası haczolunamaz.")

P.sayisal("VUK md. 18",
    "Bir vergi ceza ihbarnamesi mükellefe 10 Mart 2026 Salı günü tebliğ edilmiştir. Mükellefin başvuru süresi tebliğden "
    f"itibaren 15 gündür ve bu süre içinde resmî tatil yoktur.\n\n{V}, süre Mart 2026’nın kaçıncı günü tatil saatinde "
    "sona erer?",
    "25", ["24", "26", "27", "31"],
    "Md. 18'e göre süre gün olarak belli edilmişse başladığı gün hesaba katılmaz ve son günün tatil saatinde biter: 11 "
    "Mart'tan itibaren 15. gün 25 Mart'tır.")

P.q("6183 md. 35",
    "(PRS) Ltd. Şti.’nin ortağı Bay (U), 2024 yılında şirketteki payını Bay (Y)’ye devretmiştir. Şirketin 2023 yılına ait "
    f"vergi borcu şirketten tahsil edilememiştir.\n\n{A}, bu borçtan sorumluluk hakkında aşağıdakilerden hangisi doğrudur?",
    "Payı devreden ve devralan, pay oranında müteselsilen sorumludur.",
    ["Sadece payı devralan Bay (Y) sorumludur.",
     "Sadece payı devreden Bay (U) sorumludur.",
     "Pay devredildiğinden ortakların sorumluluğu sona ermiştir.",
     "Ortaklar borcun tamamından sınırsız sorumludur."],
    "Md. 35'e göre limited şirket ortakları tahsil edilemeyen amme alacağından sermaye hisseleri oranında sorumludur; payın "
    "devri hâlinde devreden ve devralan, devir öncesine ait amme alacaklarından müteselsilen sorumlu tutulur.", zorluk="hard")

P.q("6183 md. 106",
    f"{A}, tahsil imkânsızlığı nedeniyle terkine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kanuni tutara kadar alacaklar beklemeden terkin edilebilir.",
    ["Tahsili imkânsız her alacak tutara bakılmaksızın terkin edilir.",
     "Terkin için zamanaşımının dolması şarttır.",
     "Terkin yetkisi sadece Cumhurbaşkanına aittir.",
     "Terkin sadece gümrük vergileri için uygulanır."],
    "Md. 106'ya göre takip sonunda tahsili imkânsız veya giderleri alacaktan fazla olan ve Kanunda belirtilen tutara kadar "
    "olan amme alacakları, terkin yetkisini haiz olanlarca zamanaşımı süresi beklenmeksizin terkin olunabilir; Cumhurbaşkanı "
    "bu tutarları on katına kadar artırabilir.")

P.sayisal("VUK md. 17",
    "Bir mükellef, 15 günlük kanuni süresi olan bir vergi ödevini ağır bir aile sorunu nedeniyle süresinde yerine "
    f"getiremeyeceğini süre bitmeden yazıyla bildirerek mühlet istemiştir.\n\n{V}, Maliye Bakanlığınca verilebilecek "
    "mühlet en fazla kaç gün olabilir? (Bir ay 30 gün kabul edilecektir.)",
    "30", ["15", "45", "60", "90"],
    "Md. 17'ye göre zor durumdakilere kanuni sürenin bir katını, kanuni süre bir aydan az ise bir ayı geçmemek üzere mühlet "
    "verilebilir. 15 günlük süre bir aydan az olduğundan mühlet en fazla bir ay (30 gün) olabilir.", zorluk="hard")

P.q("6183 md. 22",
    "(VYZ) A.Ş., çalışanlarına ödediği ücretlerden kestiği gelir vergisini süresinde vergi dairesine yatırmamıştır."
    f"\n\n{A}, bu vergi kimden tahsil edilir?",
    "Vergiyi kesmekle yükümlü olan (VYZ) A.Ş.’den",
    ["Ücret alan çalışanlardan",
     "Şirketin bağlı olduğu vergi dairesi müdüründen",
     "Şirketin muhasebe servisinde çalışan personelden",
     "Çalışanlardan ve şirketten eşit olarak"],
    "Md. 22'ye göre amme alacağını borçlusundan kesip tahsil dairesine ödemek mecburiyetinde olanlar bu görevlerini süresinde "
    "yerine getirmezse, ödenmeyen alacak bu kişilerden tahsil olunur.", zorluk="easy")

P.q("6183 md. 60",
    f"Ödeme emri tebliğ edilmesine rağmen ne borcunu ödeyen ne de mal bildiriminde bulunan bir borçlu hakkında tahsil dairesi hapisle tazyik yoluna gitmek istemektedir.\n\n{A}, hapisle tazyike ilişkin aşağıdakilerden hangisi doğrudur?",
    "Karar tahsil dairesinin talebi üzerine icra hâkimince verilir.",
    ["Karar vergi dairesi müdürünce verilir.",
     "Hapisle tazyik aynı borç için birden fazla uygulanabilir.",
     "Hapisle tazyik süresi en az altı aydır.",
     "Borçlu mal bildiriminde bulunsa da hapis devam eder."],
    "Md. 60'a göre borçlu mal bildiriminde bulununcaya kadar bir defaya mahsus ve üç ayı geçmemek üzere hapisle tazyik "
    "olunur; karar tahsil dairesinin yazılı talebi üzerine icra hâkimi tarafından verilir ve Cumhuriyet savcılığınca infaz "
    "edilir.")

P.sayisal("VUK md. 104",
    "Adresi bilinmeyen bir mükellefe 20.000 ₺ tutarında vergi cezasına ilişkin ihbarname ilan yoluyla tebliğ edilecektir; "
    f"ilan yazısı 2 Nisan 2026’da vergi dairesinin ilan mahalline asılmıştır.\n\n{V}, ilan tarihi olarak kabul edilecek gün "
    "askıya çıkarılma tarihini izleyen kaçıncı gündür?",
    "15", ["7", "10", "30", "60"],
    "Md. 104/1'e göre tebliğin konusu, her biri için ayrı ayrı 30.000 TL'den az vergi veya cezaya ilişkin olduğunda gazetede "
    "ayrıca ilan yapılmaz ve ilan yazısının askıya çıkarıldığı tarihi izleyen on beşinci gün ilan tarihi kabul edilir.",
    zorluk="hard")

P.oncul("6183 md. 103",
    f"{A} aşağıdaki işlemler değerlendirilmektedir:",
    ["Mal bildirimi", "Borçlunun yabancı memlekette bulunması", "Amme alacağının teminata bağlanması",
     "Borçlunun terekesinin tasfiyesi"],
    "Yukarıdakilerden hangileri tahsil zamanaşımını keser?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 103'e göre mal bildirimi (I) ve amme alacağının teminata bağlanması (III) zamanaşımını keser. Md. 104'e göre "
    "borçlunun yabancı memlekette bulunması (II) ve terekenin tasfiyesi (IV) zamanaşımını durdurur.", zorluk="hard")

P.sayisal("VUK md. 106",
    "İlan yoluyla tebliğ edilen bir vergi ihbarnamesine ilişkin ilan tarihi 1 Mart 2026’dır. Mükellef ne vergi dairesine "
    f"başvurmuş ne de adresini bildirmiştir.\n\n{V}, tebliğ ilan tarihinden itibaren kaç ay sonunda yapılmış sayılır?",
    "1", ["2", "3", "6", "12"],
    "Md. 106'ya göre ilan tarihinden başlayarak bir ay içinde ne vergi dairesine başvurmuş ne de adresini bildirmiş olanlara "
    "bir ayın sonunda tebliğ yapılmış sayılır.")

P.q("VUK md. 24",
    f"Bir işyeri kira sözleşmesinin damga vergisi, sözleşme düzenlenirken üzerine pul yapıştırılarak ödenmiş; ayrıca tarh ve tebliğ işlemi yapılmamıştır.\n\n{V}, tahakkuku tahsile bağlı vergilere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu vergilerde tahsil tahakkuku da içine alır.",
    ["Bu vergilerde tahakkuk tahsilden sonra ayrıca yapılır.",
     "Bu vergiler sadece beyanname ile tahsil edilir.",
     "Bu vergilerde tebliğ şarttır.",
     "Bu vergiler zamanaşımına uğramaz."],
    "Md. 24'e göre mahiyetleri itibarıyla tahakkuku tahsile bağlı vergilerde verginin tahsili tahakkuku da içine alır; "
    "örneğin damga vergisinin pul yapıştırılarak ödenmesinde olduğu gibi.")

P.sayisal("VUK md. 107/A",
    "(ABC) A.Ş.’ye ait vergi ihbarnamesi, elektronik tebligat sistemi ile 3 Nisan 2026 tarihinde şirketin elektronik "
    f"adresine iletilmiştir.\n\n{V26}, tebliğ Nisan 2026’nın kaçıncı günü sonunda yapılmış sayılır?",
    "8", ["3", "4", "10", "18"],
    "Md. 107/A'ya göre elektronik ortamda tebligat, tebliğin sistem ile muhatabına iletildiği tarihi izleyen beşinci günün "
    "sonunda yapılmış sayılır: 3 Nisan'ı izleyen beşinci gün 8 Nisan'dır.", zorluk="hard")

P.q("6183 md. 105",
    f"{A}, tabii afetler nedeniyle terkine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Terkin için varlıkların en az yarısının kaybedilmesi gerekir.",
    ["Terkin Cumhurbaşkanı kararıyla kısmen veya tamamen yapılabilir.",
     "Afetin vukuu tarihinden itibaren altı ay içinde yazıyla başvurulmalıdır.",
     "Zararın mevcut olup olmadığı il veya ilçe idare kurullarınca tespit edilir.",
     "Terkin, afetin zarar verdiği gelir kaynaklarıyla ilgili alacakları kapsar."],
    "Md. 105'e göre afetler yüzünden varlıklarının ve mahsullerinin en az üçte birini kaybedenler adına tahakkuk ettirilmiş "
    "ve afetin zarar verdiği gelir kaynaklarıyla ilgili amme alacakları Cumhurbaşkanı kararıyla terkin edilebilir.")

tv = 200_000 * 0.85
P.sayisal("6183 md. 10",
    "Amme borçlusu (DEF) A.Ş., tahsil dairesine teminat olarak Hükümetçe belirlenmiş tahvilat göstermiştir. Tahvilatın "
    f"teminatın kabulüne en yakın borsa cetvelindeki değeri 200.000 ₺’dir.\n\n{A}, bu tahvilatın teminat değeri kaç ₺’dir?",
    tl(tv), secenekler(tv, 200_000, 200_000 * 0.75, 200_000 * 0.90, 200_000 * 0.50),
    "Md. 10/4'e göre Hükümetçe belli edilecek esham ve tahvilat, teminatın kabul edilmesine en yakın borsa cetvelleri "
    "üzerinden %15 noksanıyla değerlendirilir: 200.000 × 0,85 = 170.000 ₺.")

P.q("6183 md. 55",
    f"{A}, ödeme emrinde yer alan hususlar arasında aşağıdakilerden hangisi bulunmaz?",
    "Borçlunun banka hesap hareketlerinin dökümü",
    ["Borcun asıl ve ferilerinin mahiyet ve miktarları",
     "Borcun nereye ödeneceği",
     "Süresinde ödenmezse borcun cebren tahsil edileceği",
     "Gerçeğe aykırı mal bildiriminde hapis cezası uygulanacağı"],
    "Md. 55'e göre ödeme emrinde borcun asıl ve ferilerinin mahiyet ve miktarları, nereye ödeneceği, süresinde ödenmez veya "
    "mal bildiriminde bulunulmazsa cebren tahsil ve hapisle tazyik uygulanacağı ile gerçeğe aykırı bildirimin cezası yer "
    "alır.")

P.sayisal("6183 md. 48",
    "Bay (K)’nın vergi borcunun tecili talebi uygun görülmeyerek reddedilmiş ve ret kararı kendisine tebliğ edilmiştir."
    f"\n\n{A}, idarece Bay (K)’ya borcunu faiziyle ödemesi için ret kararının tebliğinden itibaren en fazla kaç günlük "
    "süre verilebilir?",
    "30", ["7", "15", "60", "90"],
    "Md. 48'e göre tecil talebi reddedilen borçlular, borçlarını reddin tebliği tarihinden itibaren idarece 30 güne kadar "
    "verilebilecek süre içinde öderlerse amme alacağı ödendiği tarihe kadar faiz alınarak tahsil edilir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
