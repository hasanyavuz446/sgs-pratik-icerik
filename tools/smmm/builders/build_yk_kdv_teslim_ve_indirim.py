# -*- coding: utf-8 -*-
"""Vergi · KDV · Teslim, Hizmet, Vergiyi Doğuran Olay ve İstisnalar — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında bu konu; KDV'nin konusuna giren/girmeyen işlemler, istisna listeleri, ihraç kaydıyla
teslimde tecil-terkin şartları ve tecil edilebilir/tecil edilecek KDV hesabı üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 3065 sayılı KDVK md. 1-6, 8, 10-14, 17, 27, 32
(7577 sayılı Kanunla eklenen md. 17/4-ğ dahil). Oranlar kökte verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_kdv_teslim_ve_indirim_2026.json", lesson="katma_deger_vergisi", topic="kdv_teslim_ve_indirim",
          konu_adi="KDV Teslim ve İstisnalar", seed=2026092906,
          surum="3065 sayılı KDVK güncel metni (7577 dahil); oranlar kökte; 29.09.2026 kontrolü")

K = "3065 sayılı Katma Değer Vergisi Kanunu’na göre"
K26 = "3065 sayılı Katma Değer Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
ORAN = "(KDV oranı %20 olarak alınacaktır.)"

tc1 = min(5_000_000 * 0.20, (2_000_000 + 5_000_000) * 0.20 - 900_000)
P.sayisal("KDVK md. 11/1-c",
    "İmalatçı (ABC) A.Ş. 2026/Mart döneminde yurt içinde 2.000.000 ₺ tutarında normal teslim, ihracatçı bir firmaya da ihraç "
    "kaydıyla 5.000.000 ₺ tutarında teslim yapmıştır. Şirketin bu döneme ait toplam indirilecek KDV’si 900.000 ₺’dir. "
    f"{ORAN}\n\n{K}, (ABC) A.Ş.’nin 2026/Mart dönemi beyannamesinde tecil edilecek KDV tutarı kaç ₺’dir?",
    tl(tc1), secenekler(tc1, 1_000_000, 1_400_000 - 900_000 + 400_000, 400_000, 1_400_000),
    "Tecil edilebilir KDV, ihraç kaydıyla teslim bedeline isabet eden vergidir (1.000.000 ₺). Tecil edilecek KDV, tecil "
    "edilebilir KDV ile ödenmesi gereken KDV'den küçük olanıdır: hesaplanan (2.000.000 + 5.000.000) × %20 = 1.400.000; "
    "1.400.000 − 900.000 = 500.000 ₺; küçük olan 500.000 ₺ tecil edilir.", zorluk="hard")

P.q("KDVK md. 1, 6",
    "Türkiye’de faaliyet gösteren (GHI) Danışmanlık A.Ş.’nin 2026 yılında yaptığı işlemlerin KDV karşısındaki durumu "
    f"incelenmektedir.\n\n{K}, aşağıdakilerden hangisi KDV’nin konusuna girer?",
    "Yurt dışındaki firmaların ürünlerinin Türkiye’de satışı için bu firmalara verilen aracılık hizmeti",
    ["Yurt dışındaki bir firmanın mallarını yurt dışında başka firmaya pazarlamak için yurt dışında verilen hizmet",
     "Yurt dışında yapılan inşaat ve montaj işleri",
     "Yurt dışında düzenlenen fuarda yurt dışında verilen stant kurulum hizmeti",
     "Yurt dışındaki bir otelde Türk turistlere yurt dışında verilen rehberlik hizmeti"],
    "Md. 1 ve 6/b'ye göre KDV'nin konusu Türkiye'de yapılan işlemlerdir; hizmetin Türkiye'de yapılması veya hizmetten "
    "Türkiye'de faydalanılması gerekir. Yurt dışında yapılıp yurt dışında faydalanılan hizmetler konu dışıdır. Türkiye'deki "
    "satışlar için verilen aracılık hizmetinden Türkiye'de faydalanılır.", zorluk="hard")

P.q("KDVK md. 1/3",
    f"{K}, aşağıdakilerden hangisi “diğer faaliyetlerden doğan teslim ve hizmetler” kapsamında KDV’ye tabi değildir?",
    "Ticari faaliyeti olmayan bir kişinin kendi otomobilini bir defaya mahsus satması",
    ["Her türlü şans ve talih oyunlarının tertiplenmesi",
     "Profesyonel sporcuların katıldığı maçların tertiplenmesi",
     "Müzayede mahallerinde yapılan satışlar",
     "GVK md. 70’te belirtilen mal ve hakların kiralanması"],
    "Md. 1/3'e göre şans oyunları, profesyonel sanatçı ve sporcuların katıldığı gösteri ve maçlar, müzayede mahallerindeki "
    "satışlar ve GVK md. 70'teki mal ve hakların kiralanması ticari faaliyet aranmaksızın KDV'ye tabidir. Ticari faaliyeti "
    "olmayan kişinin özel otomobilini arızi satması konu dışıdır.", zorluk="hard")

tc2 = (3_000_000 + 4_000_000) * 0.20 - 700_000 - min(3_000_000 * 0.20, (7_000_000) * 0.20 - 700_000)
P.sayisal("KDVK md. 11/1-c",
    "İmalatçı (DEF) Ltd. Şti. 2026/Nisan döneminde yurt içinde 4.000.000 ₺ normal teslim, ihracatçıya ihraç kaydıyla "
    "3.000.000 ₺ teslim yapmıştır. Dönemin indirilecek KDV’si 700.000 ₺’dir; devreden KDV yoktur. "
    f"{ORAN}\n\n{K}, (DEF) Ltd. Şti.’nin 2026/Nisan döneminde fiilen ödeyeceği KDV tutarı kaç ₺’dir?",
    tl(tc2), secenekler(tc2, 700_000, 600_000, 800_000, 0),
    "Hesaplanan KDV (4.000.000 + 3.000.000) × %20 = 1.400.000; ödenmesi gereken 1.400.000 − 700.000 = 700.000 ₺. Tecil "
    "edilebilir KDV 600.000 ₺'dir ve 700.000 ₺'den küçük olduğundan tamamı tecil edilir. Fiilen ödenecek KDV 700.000 − "
    "600.000 = 100.000 ₺.", zorluk="hard")

P.q("KDVK md. 2",
    f"{K}, teslime ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zincirleme akitlerde mal doğrudan son alıcıya devredilirse aradaki safhalar teslim sayılmaz.",
    ["Teslim, mal üzerindeki tasarruf hakkının alıcıya devredilmesidir.",
     "Malın alıcının gösterdiği yere veya kişilere tevdii teslim hükmündedir.",
     "Su, elektrik, gaz, ısıtma ve soğutma dağıtımları mal teslimidir.",
     "Trampa iki ayrı teslim hükmündedir."],
    "Md. 2/2'ye göre tasarruf hakkının zincirleme akitlerle malın el değiştirmeden doğrudan sonuncu kişiye devredilmesi "
    "hâlinde aradaki safhaların her biri ayrı bir teslimdir.")

P.q("KDVK md. 2/5",
    "Arsa sahibi Bay (L) ile müteahhit (JKL) İnşaat A.Ş. arasında, arsa karşılığında konut yapılmasına ilişkin sözleşme "
    f"imzalanmıştır.\n\n{K}, bu işlemin KDV karşısındaki durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Arsa sahibinin arsa payı teslimi ile müteahhidin konut teslimi ayrı teslimler olarak kabul edilir.",
    ["Arsa karşılığı inşaat tek bir hizmet işlemidir.",
     "Sadece müteahhidin üçüncü kişilere yaptığı satışlar teslim sayılır.",
     "Arsa karşılığı inşaat işleri KDV’nin konusu dışındadır.",
     "Sadece arsa sahibinin arsa payı teslimi vergiye tabidir."],
    "Md. 2/5'e göre arsa karşılığı inşaat işlerinde arsa sahibi tarafından müteahhide arsa payı teslimi, müteahhit tarafından "
    "arsa sahibine konut veya işyeri teslimi yapılmış sayılır; arsa sahibinin teslimi, ticari faaliyet kapsamında değilse "
    "vergiye tabi olmayabilir.", zorluk="hard")

ia = 800_000 - 1_000_000 * 0.20
P.sayisal("KDVK md. 11/1-a, 32",
    "(GHI) A.Ş. 2026/Mayıs döneminde 10.000.000 ₺ tutarında mal ihraç etmiş, yurt içinde 1.000.000 ₺ (KDV hariç) teslim "
    "yapmıştır. Dönemde yüklendiği ve tamamı indirilebilir nitelikteki KDV 800.000 ₺’dir; devreden KDV yoktur. İade "
    f"tutarı ihracat bedeline göre hesaplanan sınırı aşmamaktadır. {ORAN}\n\n{K}, (GHI) A.Ş.’nin bu dönem için iade talep "
    "edebileceği KDV tutarı kaç ₺’dir?",
    tl(ia), secenekler(ia, 800_000, 2_000_000, 200_000, 2_000_000 - 800_000),
    "Md. 11/1-a'ya göre ihracat teslimleri istisnadır; md. 32'ye göre istisnalı işlemlere ait yüklenilen KDV hesaplanan "
    "vergiden indirilir, indirilemeyen kısım iade edilir: 800.000 − 200.000 = 600.000 ₺.", zorluk="hard")

P.q("KDVK md. 3",
    f"{K}, aşağıdakilerden hangisi teslim sayılan hâllerden biri değildir?",
    "Malın alıcıya fatura düzenlenmeden önce sipariş alınması",
    ["Vergiye tabi malların işletmeden vergiye tabi işlemler dışındaki amaçlarla çekilmesi",
     "Vergiye tabi malların personele ikramiye olarak verilmesi",
     "Vergiye tabi malların istisna edilmiş malların üretiminde kullanılması",
     "Mülkiyeti muhafaza kaydıyla yapılan satışlarda zilyetliğin devri"],
    "Md. 3'e göre işletmeden çekme, personele ücret, prim, ikramiye ve hediye olarak verme, istisna edilmiş malların "
    "üretiminde kullanma ve mülkiyeti muhafaza kaydıyla satışta zilyetliğin devri teslim sayılır. Sipariş alınması bir "
    "teslim değildir.", zorluk="easy")

P.q("KDVK md. 4",
    "(MNO) A.Ş., bir müşterisine verdiği bakım-onarım hizmetinin bedelini nakit yerine müşterinin ürettiği bir jeneratörü "
    f"alarak tahsil etmiştir.\n\n{K}, bu işlemin vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hizmet ve jeneratör teslimi ayrı ayrı vergilendirilir.",
    ["İşlem tek bir trampa sayılır ve sadece jeneratör teslimi vergilendirilir.",
     "Bedel para olmadığından işlem KDV’nin konusuna girmez.",
     "Sadece bakım-onarım hizmeti vergilendirilir.",
     "İşlem hizmet ithalatı sayılır."],
    "Md. 4/2'ye göre bir hizmetin karşılığının bir mal teslimi veya diğer bir hizmet olması hâlinde bunların her biri ayrı "
    "işlem olup hizmet veya teslim hükümlerine göre ayrı ayrı vergilendirilir; matrah md. 27 gereği emsal bedeldir.")

ia2 = 500_000 - 1_500_000 * 0.20
P.sayisal("KDVK md. 32",
    "(JKL) A.Ş.’nin 2026/Haziran döneminde yurt içi teslimleri 1.500.000 ₺ (KDV hariç) olup bunun yanında ihracat da "
    "yapmıştır. Dönemde yüklenilen KDV toplamı 500.000 ₺ olup bunun 250.000 ₺’si ihracata konu mallara aittir. Devreden "
    f"KDV yoktur. {ORAN}\n\n{K}, (JKL) A.Ş.’nin bu dönemde ihracat nedeniyle iade talep edebileceği KDV kaç ₺’dir?",
    tl(ia2), secenekler(ia2, 250_000, 500_000, 300_000, 50_000),
    "Md. 32'ye göre istisnalı işlemlere ait KDV önce hesaplanan vergiden indirilir; indirim yoluyla giderilemeyen kısım iade "
    "edilir. Hesaplanan 300.000 ₺, toplam indirim 500.000 ₺; giderilemeyen 200.000 ₺, ihracata ait 250.000 ₺'den küçük "
    "olduğundan iade edilebilecek tutar 200.000 ₺'dir.", zorluk="hard")

P.q("KDVK md. 4",
    f"{K}, hizmete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bir şeyi yapmamayı taahhüt etmek hizmet sayılmaz.",
    ["Hizmet, teslim ve teslim sayılan hâller ile mal ithalatı dışında kalan işlemlerdir.",
     "Bir şeyi imal etmek, onarmak veya temizlemek hizmet şeklinde gerçekleşebilir.",
     "Kiralama işlemi hizmettir.",
     "Hizmetin karşılığı mal teslimi olursa her biri ayrı işlem olarak vergilendirilir."],
    "Md. 4/1'e göre hizmet; bir şeyi yapmak, işlemek, meydana getirmek, imal etmek, onarmak, temizlemek, muhafaza etmek, "
    "kiralamak ve bir şeyi yapmamayı taahhüt etmek gibi şekillerde gerçekleşebilir.")

P.q("KDVK md. 8/2",
    "KDV mükellefi olmayan emekli Bay (M), bir şirkete sattığı eski ofis mobilyası için düzenlediği belgede KDV göstermiş ve "
    f"bu tutarı tahsil etmiştir.\n\n{K}, Bay (M)’nin durumu hakkında aşağıdakilerden hangisi doğrudur?",
    "Belgede gösterdiği KDV’yi ödemekle mükelleftir.",
    ["Mükellef olmadığından tahsil ettiği KDV’yi ödemez.",
     "Tahsil ettiği KDV’yi alıcıya iade etmekle yükümlüdür, vergi dairesine ödemez.",
     "Tahsil edilen KDV, alıcı tarafından sorumlu sıfatıyla ödenir.",
     "Belgede KDV göstermek sadece usulsüzlük cezası gerektirir."],
    "Md. 8/2'ye göre vergiye tabi işlem söz konusu olmadığı veya KDV'yi belgede göstermeye hakkı bulunmadığı hâlde düzenlediği "
    "belgelerde KDV gösterenler bu vergiyi ödemekle mükelleftir.")

P.sayisal("KDVK md. 32",
    "(MNO) A.Ş., 2024/Kasım döneminde gerçekleştirdiği ihracat işlemine ait yüklenilen ve indirim yoluyla giderilemeyen KDV’nin "
    f"iadesini henüz talep etmemiştir.\n\n{K}, (MNO) A.Ş. bu iadeyi en geç hangi yılın sonuna kadar talep etmelidir?",
    "2026", ["2025", "2027", "2028", "2029"],
    "Md. 32'ye göre indirilemeyen KDV, işlemin gerçekleştiği dönemi izleyen ikinci takvim yılının sonuna kadar talep "
    "edilmesi şartıyla iade olunur: 2024 işlemi için 2026 yılı sonu.", zorluk="hard")

P.q("KDVK md. 8/1",
    f"{K}, aşağıdakilerden hangisi KDV mükellefi değildir?",
    "Mevduat faizi elde eden emekli kişi",
    ["Mal teslimi ve hizmet ifası hâllerinde bu işleri yapanlar",
     "Mal ve hizmet ithal edenler",
     "Müzayede mahallerinde yapılan satışlarda bu satışları yapanlar",
     "GVK md. 70’teki mal ve hakları kiraya verenler"],
    "Md. 8/1'e göre teslim ve hizmet yapanlar, ithalatçılar, müzayede mahallerinde satış yapanlar, şans oyunlarını tertip "
    "edenler ve GVK md. 70'teki mal ve hakları kiraya verenler KDV mükellefidir. Mevduat faizi elde etmek KDV'ye tabi bir "
    "işlem değildir.", zorluk="easy")

P.q("KDVK md. 10",
    f"{K}, vergiyi doğuran olaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Elektrik dağıtımında vergiyi doğuran olay bedelin tahsil edilmesiyle meydana gelir.",
    ["Mal teslimi ve hizmet ifasında vergiyi doğuran olay malın teslimi veya hizmetin yapılmasıdır.",
     "Malın alıcıya gönderilmesi hâlinde nakliyeye başlanması vergiyi doğuran olaydır.",
     "Komisyoncu vasıtasıyla satışlarda vergiyi doğuran olay malın alıcıya teslimidir.",
     "Gümrük vergisine tabi olmayan ithalatta vergiyi doğuran olay gümrük beyannamesinin tescilidir."],
    "Md. 10/g'ye göre su, elektrik, gaz, ısıtma ve soğutma gibi enerji dağıtımlarında vergiyi doğuran olay bunların "
    "bedellerinin tahakkuk ettirilmesidir, tahsil değildir.")

P.sayisal("KDVK md. 11/1-c",
    "İmalatçı (PRS) A.Ş., 12 Şubat 2026’da ihracatçı (TUV) Ltd. Şti.’ye ihraç kaydıyla mal teslim etmiştir. İhracat için "
    f"mücbir sebep veya ek süre söz konusu değildir.\n\n{K}, tecil edilen verginin terkin edilebilmesi için malın, teslim "
    "tarihini takip eden ay başından itibaren en geç kaç ay içinde ihraç edilmesi gerekir?",
    "3", ["1", "2", "6", "12"],
    "Md. 11/1-c'ye göre mallar ihracatçıya teslim tarihini takip eden ay başından itibaren üç ay içinde ihraç edilirse tecil "
    "edilen vergi terkin olunur; Şubat teslimi için süre Mart başında başlar ve 31 Mayıs 2026'da dolar.", zorluk="hard")

P.q("KDVK md. 10/ı",
    "(PRS) A.Ş., gümrük vergisine tabi bir makineyi ithal etmektedir. Gümrük beyannamesi 3 Mart’ta tescil edilmiş, gümrük "
    f"vergisi ödeme mükellefiyeti de aynı gün başlamış, mal 10 Mart’ta işletmeye getirilmiştir.\n\n{K}, bu ithalatta KDV "
    "açısından vergiyi doğuran olay ne zaman meydana gelir?",
    "Gümrük vergisi ödeme mükellefiyetinin başladığı 3 Mart’ta",
    ["Malın işletmeye getirildiği 10 Mart’ta",
     "Mal bedelinin yabancı satıcıya ödendiği tarihte",
     "İthalat faturasının kanuni defterlere kaydedildiği tarihte",
     "Malın yurt dışında gemiye yüklendiği tarihte"],
    "Md. 10/ı'ya göre ithalatta vergiyi doğuran olay Gümrük Kanununa göre gümrük vergisi ödeme mükellefiyetinin başlaması, "
    "gümrük vergisine tabi olmayan işlemlerde ise gümrük beyannamesinin tescilidir.")

P.q("KDVK md. 17",
    "Bir mali müşavir, müşterilerinin 2026 yılındaki işlemlerinden hangilerinin KDV’den istisna olduğunu "
    f"değerlendirmektedir.\n\n{K}, aşağıdakilerden hangisi KDV’den istisna değildir?",
    "Gerçek usul tüccarın mağazasındaki giyim satışı",
    ["Banka ve sigorta muameleleri vergisi kapsamına giren işlemler",
     "Kazançları basit usulde tespit edilen mükelleflerin teslim ve hizmetleri",
     "Külçe altın ve külçe gümüş teslimleri",
     "İktisadi işletmelere dahil olmayan gayrimenkullerin kiralanması"],
    "Md. 17/4'e göre BSMV kapsamındaki işlemler (e), basit usul mükelleflerinin teslim ve hizmetleri (a), külçe altın ve gümüş "
    "teslimleri (g) ve iktisadi işletmelere dahil olmayan gayrimenkullerin kiralanması (d) istisnadır. Gerçek usul tüccarın "
    "olağan satışı vergilidir.", zorluk="easy")

P.sayisal("KDVK md. 11/1-c",
    "İhracatçı (VYZ) A.Ş., ihraç kaydıyla satın aldığı malları mücbir sebep nedeniyle üç aylık süre içinde ihraç "
    f"edememiştir.\n\n{K}, ihracatçının ek süre alabilmesi için üç aylık sürenin dolduğu tarihten itibaren en geç kaç gün "
    "içinde başvurması gerekir?",
    "15", ["7", "10", "30", "60"],
    "Md. 11/1-c'ye göre ihracatın mücbir sebepler veya beklenmedik durumlar nedeniyle üç ay içinde gerçekleştirilememesi "
    "hâlinde, en geç üç aylık sürenin dolduğu tarihten itibaren on beş gün içinde başvuran ihracatçılara üç aya kadar ek "
    "süre verilebilir.")

P.q("KDVK md. 17/4-ğ",
    "Bir belediye, 2026 yılında kent meydanı projesi için (STU) A.Ş.’nin aktifinde kayıtlı bir taşınmazı 2942 sayılı "
    f"Kamulaştırma Kanunu kapsamında kamulaştırmıştır.\n\n{K26}, bu taşınmazın belediyeye devrinin KDV karşısındaki "
    "durumu hakkında aşağıdakilerden hangisi doğrudur?",
    "Kamulaştırma kapsamındaki devir KDV’den istisnadır.",
    ["Devir, ticari işletmeye dahil taşınmaz olduğu için genel oranda KDV’ye tabidir.",
     "Devir, taşınmaz iki tam yıl aktifte kalmışsa istisnadır.",
     "Devir KDV’nin konusuna girmez, ancak belediye sorumlu sıfatıyla KDV öder.",
     "Devir, kamulaştırma bedeli üzerinden indirimli oranda vergilendirilir."],
    "7577 sayılı Kanunla 2026'da eklenen md. 17/4-ğ'ye göre 2942 sayılı Kamulaştırma Kanunu kapsamında taşınmazların "
    "kamulaştırmayı yapan Devlet ve kamu tüzel kişilerine devri KDV'den istisnadır.", zorluk="hard")

P.q("KDVK md. 17/4-r",
    f"{K26}, kurumların iştirak hissesi satışlarına ilişkin KDV istisnası hakkında aşağıdakilerden hangisi doğrudur?",
    "Aktifte en az iki tam yıl bulunan iştirak hisselerinin satışı istisnadır; bu kıymetlerin ticaretini yapanlar hariçtir.",
    ["Tüm hisse satışları elde tutma süresine bakılmaksızın vergilidir.",
     "Sadece halka açık şirket hisselerinin satışı istisnadır.",
     "İştirak hisseleri ile birlikte tüm taşınmazların satışı da süre şartı olmaksızın istisnadır.",
     "İstisna sadece gerçek kişilerin hisse satışlarına uygulanır."],
    "Md. 17/4-r'ye göre kurumların aktifinde en az iki tam yıl süreyle bulunan iştirak hisselerinin satışı istisnadır; bu "
    "kıymetlerin ticaretini yapan kurumların bu amaçla elde tuttukları hisseler kapsam dışıdır. Taşınmazlara ilişkin genel "
    "istisna 2023'te bentten çıkarılmıştır.", zorluk="hard")

P.sayisal("KDVK md. 17/4-r",
    "(ZAB) A.Ş., aktifinde bulunan ve iştirak hissesi ticareti yapmadığı bir şirketin hisselerini satmayı planlamaktadır."
    f"\n\n{K}, bu satışın KDV’den istisna olabilmesi için hisselerin kurumun aktifinde en az kaç tam yıl süreyle bulunması "
    "gerekir?",
    "2", ["1", "3", "4", "5"],
    "Md. 17/4-r'ye göre kurumların aktifinde en az iki tam yıl süreyle bulunan iştirak hisselerinin satışı suretiyle "
    "gerçekleşen devir ve teslimler istisnadır; bu kıymetlerin ticaretini yapanların bu amaçla elde tuttukları hisseler "
    "istisna dışıdır.", zorluk="easy")

P.q("KDVK md. 17/4-c",
    "(VYZ) Ltd. Şti., Kurumlar Vergisi Kanunu’na uygun olarak (ZAB) A.Ş.’ye devrolmuş ve infisah etmiştir. Devir sırasında "
    f"(VYZ) Ltd. Şti.’nin yüklenip indiremediği KDV bulunmaktadır.\n\n{K}, bu devir işlemine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Devir istisnadır; indirilemeyen KDV devralan kurumca indirilebilir.",
    ["Devir genel oranda KDV’ye tabidir.",
     "Devir istisnadır ve infisah eden kurumun indirilemeyen KDV’si gider yazılır.",
     "Devir istisnadır; ancak indirilemeyen KDV devralana geçmez.",
     "Devir sadece devralan kurum için vergiye tabidir."],
    "Md. 17/4-c'ye göre KVK'ya göre yapılan devir ve bölünme işlemleri istisnadır; infisah eden mükellefçe yüklenilen ve "
    "indirilemeyen vergiler, devralan tarafından mükerrer indirime yol açmayacak şekilde, vergi incelemesi sonucuna göre "
    "indirim konusu yapılır.", zorluk="hard")

P.q("KDVK md. 11/1-b",
    "Türkiye’de ikamet etmeyen yabancı turist Bayan (N), İstanbul’da bir mağazadan halı satın almış ve halıyı yurt dışına "
    f"götürmüştür.\n\n{K}, bu satışta KDV uygulamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "KDV tahsil edilir, çıkışta belge ibrazıyla iade olunur.",
    ["Satış anında KDV hesaplanmaz, fatura KDV’siz düzenlenir.",
     "KDV tahsil edilir ve iade edilmez.",
     "KDV sadece halının bedeli belirli bir tutarı aşarsa tahsil edilir.",
     "KDV turistin kendi ülkesinde ödenir."],
    "Md. 11/1-b'ye göre Türkiye'de ikamet etmeyen yolcuların satın alarak Türkiye dışına götürdükleri malların teslimi "
    "anında KDV tahsil edilir; gümrükten çıkış anında fatura veya belgenin ibrazında tahsil edilen KDV iade olunur.")

hd = 60_000 * 0.20
P.sayisal("KDVK md. 3/a, 27",
    "Beyaz eşya satan (CDE) A.Ş., 2026/Nisan döneminde stoklarındaki buzdolaplarından maliyeti 50.000 ₺, emsal bedeli "
    "60.000 ₺ olan kısmını çalışanlarına bayram hediyesi olarak vermiştir; çalışanlardan herhangi bir bedel alınmamıştır. "
    f"{ORAN}\n\n{K}, bu işlem nedeniyle hesaplanacak KDV kaç ₺’dir?",
    tl(hd), secenekler(hd, 50_000 * 0.20, 0, 60_000 * 0.18, 10_000 * 0.20),
    "Md. 3/a'ya göre vergiye tabi malların işletme personeline hediye olarak verilmesi teslim sayılır; bedeli bulunmadığından "
    "md. 27'ye göre matrah emsal bedelidir: 60.000 × %20 = 12.000 ₺.")

P.q("KDVK md. 12",
    f"{K}, ihracat teslimi sayılmanın şartlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Malın ihraçtan önce alıcı adına yurt içinde işlenmesi ihracat teslimi niteliğini ortadan kaldırır.",
    ["Teslim yurt dışındaki bir müşteriye veya serbest bölgedeki alıcıya yapılmalıdır.",
     "Mal Türkiye gümrük bölgesinden çıkarak bir dış ülkeye veya serbest bölgeye varmalıdır.",
     "Gümrüksüz satış mağazalarına yapılan teslimler de şartlarla ihracat sayılır.",
     "Yurt içindeki firmanın yurt dışında müstakil faaliyet gösteren şubesi yurt dışındaki müşteri sayılır."],
    "Md. 12/1-b'ye göre teslim konusu malın ihraç edilmeden önce yurt dışındaki alıcı adına hareket eden yurt içindeki "
    "firmalar veya bizzat alıcı tarafından işlenmesi veya değerlendirilmesi durumu değiştirmez.", zorluk="hard")

P.q("KDVK md. 11/1-c",
    f"{K}, ihraç kaydıyla teslimlerde tecil-terkin uygulamasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tecil edilen vergi, malların teslimi izleyen ay başından itibaren altı ay içinde ihracı hâlinde terkin edilir.",
    ["İhraç kaydıyla teslim edilen mallara ait KDV ihracatçılar tarafından ödenmez.",
     "Beyan edilen KDV vergi dairesince tarh ve tahakkuk ettirilerek tecil olunur.",
     "İhracat şartlara uygun gerçekleşmezse tecil edilen vergi, tahakkuk tarihinden itibaren gecikme zammıyla birlikte tahsil edilir.",
     "Mücbir sebeple ihraç edilemezse vergi tecil faiziyle birlikte tahsil edilir."],
    "Md. 11/1-c'ye göre tecil edilen vergi, malların ihracatçıya teslim tarihini takip eden ay başından itibaren üç ay içinde "
    "ihraç edilmesi hâlinde terkin olunur; mücbir sebep ve beklenmedik durumlarda başvuru üzerine üç aya kadar ek süre "
    "verilebilir.", zorluk="hard")

cek = 30_000 * 0.20
P.sayisal("KDVK md. 3/a, 27",
    "Mobilya mağazası sahibi Bay (K), 2026/Mayıs döneminde işletmesinin stokundaki emsal bedeli 30.000 ₺ olan bir koltuk "
    "takımını evinde kullanmak üzere işletmeden çekmiş ve işletmeye bedel ödememiştir. "
    f"{ORAN}\n\n{K}, bu işlem nedeniyle hesaplanacak KDV kaç ₺’dir?",
    tl(cek), secenekler(cek, 0, 30_000 * 0.10, 30_000 * 0.18, 30_000),
    "Md. 3/a'ya göre vergiye tabi malların vergiye tabi işlemler dışındaki amaçlarla işletmeden çekilmesi teslim sayılır; "
    "matrah emsal bedelidir: 30.000 × %20 = 6.000 ₺.", zorluk="easy")

P.q("KDVK md. 13/b",
    f"{K26}, deniz ve hava taşıma araçları için liman ve hava meydanlarında yapılan hizmetlere ilişkin istisna "
    "hakkında aşağıdakilerden hangisi doğrudur?",
    "Özel tekne ve yatlar deniz taşıma aracı sayılmaz.",
    ["Özel yatlara limanlarda verilen hizmetler de istisna kapsamındadır.",
     "İstisna sadece yabancı bayraklı gemilere verilen hizmetleri kapsar.",
     "İstisna sadece hava taşıma araçlarına verilen hizmetleri kapsar.",
     "Liman hizmetleri istisnası 2024 yılında tamamen kaldırılmıştır."],
    "Md. 13/b'ye göre deniz ve hava taşıma araçları için liman ve hava meydanlarında yapılan hizmetler istisnadır; 7524 "
    "sayılı Kanunla eklenen parantez hükmüne göre gezi, eğlence, spor ve amatör balıkçılık gibi faaliyetlerde kullanılan "
    "araçlar, özel tekne ve yatlar deniz taşıma aracı kabul edilmez.", zorluk="hard")

P.q("KDVK md. 13/d",
    "Yatırım teşvik belgesi sahibi (CDE) A.Ş., belge kapsamındaki makineleri KDV ödemeden satın almış; ancak yatırım "
    f"belgede öngörüldüğü şekilde gerçekleşmemiştir.\n\n{K}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Vergi alıcıdan ceza ve gecikme faiziyle tahsil edilir.",
    ["Zamanında alınmayan vergi makineyi satan firmadan tahsil edilir.",
     "Yatırım gerçekleşmese de istisna korunur.",
     "Vergi sadece gecikme faizi ile tahsil edilir, ceza kesilmez.",
     "Vergi, belgeyi veren idareden tahsil edilir."],
    "Md. 13/d'ye göre yatırım teşvik belgesi sahiplerine belge kapsamındaki makine ve teçhizat teslimleri istisnadır; yatırım "
    "belgede öngörüldüğü şekilde gerçekleşmezse zamanında alınmayan vergi alıcıdan vergi ziyaı cezası uygulanarak gecikme "
    "faizi ile birlikte tahsil edilir.", zorluk="hard")

vd = (500_000 + 200_000) * 0.20
P.sayisal("KDVK md. 10/a-b",
    "(FGH) A.Ş. 2026/Mart döneminde 500.000 ₺ (KDV hariç) mal teslim etmiştir. Ayrıca Nisan ayında teslim edilecek 200.000 ₺ "
    "(KDV hariç) tutarındaki mal için müşterisinin talebiyle Mart ayında fatura düzenlemiştir. "
    f"{ORAN}\n\n{K}, (FGH) A.Ş.’nin 2026/Mart dönemi hesaplanan KDV tutarı kaç ₺’dir?",
    tl(vd), secenekler(vd, 500_000 * 0.20, 200_000 * 0.20, 700_000 * 0.18, 300_000 * 0.20),
    "Md. 10/b'ye göre malın tesliminden önce fatura düzenlenmesi hâlinde, faturada gösterilen miktarla sınırlı olmak üzere "
    "vergiyi doğuran olay fatura düzenlenmesiyle meydana gelir: (500.000 + 200.000) × %20 = 140.000 ₺.")

P.q("KDVK md. 32",
    f"{K}, istisnalı işlemlere ait yüklenilen KDV’nin iadesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İade talebi için süre, işlemin gerçekleştiği yılın sonuna kadardır.",
    ["İhracat istisnasına ait yüklenilen KDV önce hesaplanan vergiden indirilir.",
     "İndirim yoluyla giderilemeyen KDV iade olunur.",
     "İade, mükellefin vergi ve SGK prim borçlarına mahsup suretiyle sınırlandırılabilir.",
     "Vergiye tabi işlemi olmayan ihracatçı da yüklendiği KDV’yi iade alabilir."],
    "Md. 32'ye göre indirilemeyen KDV, işlemin gerçekleştiği dönemi izleyen ikinci takvim yılının sonuna kadar talep edilmesi "
    "şartıyla iade olunur. Bakanlık iadeyi borçlara mahsup suretiyle sınırlamaya yetkilidir.")

P.q("KDVK md. 17/2",
    "Bir kamu yararına çalışan derneğin işlettiği huzurevi yaşlılara bakım hizmeti vermekte, ayrıca derneğe ait bir kafe halka "
    f"açık olarak işletilmektedir.\n\n{K}, bu faaliyetlerin KDV karşısındaki durumuna ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Huzurevi hizmeti istisna, kafe hizmeti vergilidir.",
    ["Derneğin bütün faaliyetleri istisnadır.",
     "Derneğin bütün faaliyetleri vergiye tabidir.",
     "Kafe istisna, huzurevi hizmetleri vergilidir.",
     "Sadece yaşlılardan bedel alınmayan hizmetler vergilidir."],
    "Md. 17/2-a'ya göre md. 17/1'de sayılan kurum ve kuruluşların huzurevi, yurt ve benzeri kuruluşları işletmek suretiyle "
    "ifa ettikleri kuruluş amaçlarına uygun teslim ve hizmetleri istisnadır; halka açık ticari kafe işletmesi bu kapsamda "
    "değildir.")

ks = 250_000 * 0.20
P.sayisal("KDVK md. 10/d",
    "(IJK) A.Ş., 2026/Mart ayında satılmak üzere komisyoncuya toplam 400.000 ₺ bedelli mal göndermiştir. Komisyoncu bu "
    f"malların 250.000 ₺’lik kısmını Mart, kalanını Nisan ayında alıcılara teslim etmiştir. {ORAN}\n\n{K}, (IJK) A.Ş. "
    "açısından bu işlemlerle ilgili 2026/Mart döneminde hesaplanacak KDV kaç ₺’dir?",
    tl(ks), secenekler(ks, 400_000 * 0.20, 150_000 * 0.20, 0, 250_000 * 0.18),
    "Md. 10/d'ye göre komisyoncular vasıtasıyla veya konsinyasyon suretiyle yapılan satışlarda vergiyi doğuran olay malların "
    "alıcıya teslimidir; komisyoncuya gönderim değildir: 250.000 × %20 = 50.000 ₺.")

P.q("KDVK md. 14",
    f"{K}, uluslararası taşımacılık istisnasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Cumhurbaşkanınca belirlenen uluslararası taşıma işleri istisnadır.",
    ["Tüm yurt içi taşımacılık işleri istisnadır.",
     "İstisna, yerleşik mükelleflere karşılıklılık şartı aranmaksızın tanınır.",
     "Yurt dışına çıkacak kamyonlara yapılan her türlü akaryakıt teslimi sınırsız olarak istisnadır.",
     "Uluslararası taşımacılık KDV’nin konusu dışındadır."],
    "Md. 14/1'e göre transit ve Türkiye ile yabancı ülkeler arasındaki taşımacılık işlerinde Cumhurbaşkanınca belirlenecek "
    "taşıma işleri istisnadır; yerleşik olmayanlara karşılıklılık şartıyla tanınır. Motorin istisnası standart depo miktarı ve "
    "belirlenen sınır kapılarıyla sınırlıdır.")

P.oncul("KDVK md. 17/4",
    f"{K} aşağıdaki işlemler değerlendirilmektedir:",
    ["Döviz ve hisse senedi teslimi",
     "Gerçek usulde vergilendirilen tüccarın dükkân kiralaması",
     "Metal ve plastik hurda teslimi",
     "İktisadi işletmeye dahil bir binanın kiralanması"],
    "Yukarıdakilerden hangileri KDV’den istisnadır?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 17/4-g'ye göre döviz, para, hisse senedi (I) ile metal, plastik ve benzeri hurda ve atık teslimleri (III) istisnadır. "
    "Md. 17/4-d'deki kiralama istisnası iktisadi işletmelere dahil olmayan gayrimenkullere ilişkindir; ticari işletmeye dahil "
    "gayrimenkullerin kiralanması (II ve IV) vergilidir.", zorluk="hard")

kk = 300_000 * 0.20
P.sayisal("KDVK md. 10/c",
    "Yazılım şirketi (LMN) A.Ş., müşterisiyle toplam 900.000 ₺ bedelli projenin üç eşit aşamada teslim edileceğini ve her "
    "aşama için ayrı fatura düzenleneceğini kararlaştırmıştır. 2026/Mart ayında sadece birinci aşama tamamlanıp teslim "
    f"edilmiştir. {ORAN}\n\n{K}, (LMN) A.Ş.’nin bu proje için 2026/Mart döneminde hesaplayacağı KDV kaç ₺’dir?",
    tl(kk), secenekler(kk, 900_000 * 0.20, 0, 600_000 * 0.20, 450_000 * 0.20),
    "Md. 10/c'ye göre kısım kısım hizmet yapılmasında mutabık kalınan hâllerde vergiyi doğuran olay her bir kısmın "
    "yapılmasıyla meydana gelir: 300.000 × %20 = 60.000 ₺.")

P.q("KDVK md. 1",
    f"{K}, aşağıdakilerden hangisi KDV’nin konusuna girmez?",
    "Bir işçinin işverenine bağımlı olarak verdiği hizmet",
    ["Her türlü mal ve hizmet ithalatı",
     "Belediyeye ait işletmenin ticari nitelikteki teslimleri",
     "Profesyonel sanatçıların yer aldığı konserlerin tertiplenmesi",
     "Posta ve telekomünikasyon hizmetleri"],
    "Md. 1'e göre ticari, sınai, zirai ve mesleki faaliyet çerçevesindeki teslim ve hizmetler, ithalat ve md. 1/3'te sayılan "
    "diğer faaliyetler KDV'nin konusudur. Hizmet akdine dayalı bağımlı çalışma bir ücret ilişkisidir ve konu dışıdır.",
    zorluk="easy")

P.q("KDVK md. 6/a",
    "(ZAB) A.Ş., Hollanda’daki deposunda bulunan malları, Türkiye’ye getirmeden Almanya’daki bir müşteriye satmış ve "
    f"mallar doğrudan Hollanda’dan Almanya’ya gönderilmiştir.\n\n{K}, bu satışın KDV karşısındaki durumuna ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Mal teslim anında Türkiye’de olmadığından konu dışıdır.",
    ["Satıcı Türkiye’de yerleşik olduğundan işlem KDV’ye tabidir.",
     "İşlem ihracat istisnası kapsamındadır.",
     "İşlem ihraç kaydıyla teslim sayılır ve vergi tecil edilir.",
     "Alıcı KDV’yi sorumlu sıfatıyla öder."],
    "Md. 6/a'ya göre mal teslimlerinde işlemin Türkiye'de yapılması, malların teslim anında Türkiye'de bulunmasını ifade "
    "eder; teslim anında yurt dışında bulunan malların satışı KDV'nin konusuna girmez. İhracat istisnası malın Türkiye gümrük "
    "bölgesinden çıkmasını gerektirir.", zorluk="hard")

yd = 400_000 * 0.20
P.sayisal("KDVK md. 6/b, 11/1-a, 12/2",
    "Türkiye’deki (OPR) Danışmanlık A.Ş. 2026/Nisan döneminde iki hizmet vermiştir: Almanya’daki bir şirkete Almanya’daki "
    "fabrikasında uygulanacak 600.000 ₺ tutarında mühendislik danışmanlığı; Fransa’daki bir şirkete, bu şirketin Türkiye’deki "
    f"şubesinde kullanılacak 400.000 ₺ tutarında yazılım danışmanlığı. {ORAN}\n\n{K}, (OPR) A.Ş.’nin bu hizmetler için "
    "hesaplayacağı KDV kaç ₺’dir?",
    tl(yd), secenekler(yd, 1_000_000 * 0.20, 600_000 * 0.20, 0, 200_000 * 0.20),
    "Md. 12/2'ye göre hizmet ihracatı istisnası için hizmetin yurt dışındaki müşteri için yapılması ve hizmetten yurt dışında "
    "faydalanılması gerekir. Almanya'daki hizmet istisnadır; Türkiye'deki şubede faydalanılan hizmet md. 6/b gereği "
    "Türkiye'de yapılmış sayılır ve vergilidir: 400.000 × %20 = 80.000 ₺.", zorluk="hard")

P.q("KDVK md. 2/1, 10/e",
    "(CDE) A.Ş., İzmir’deki bir müşterisine sattığı malları 28 Mart 2026’da nakliye firmasına teslim etmiş; mallar 2 Nisan "
    f"2026’da müşteriye ulaşmıştır.\n\n{K}, bu teslimde vergiyi doğuran olay ne zaman meydana gelmiştir?",
    "Nakliyeciye tevdi edildiği 28 Mart 2026’da",
    ["Malların müşteriye ulaştığı 2 Nisan 2026’da",
     "Satış bedelinin tahsil edildiği tarihte",
     "Faturanın müşteriye ulaştığı tarihte",
     "Nisan dönemi beyannamesinin verildiği tarihte"],
    "Md. 2/1 ve 10/e'ye göre malın alıcıya gönderilmesi hâlinde malın nakliyesine başlanması veya nakliyeci ya da sürücüye "
    "tevdii teslimdir ve vergiyi doğuran olay bu anda meydana gelir.")

sr = 500_000 * 0.20
P.sayisal("KDVK md. 6/b, 9",
    "(STU) A.Ş., Türkiye’de işyeri ve daimi temsilcisi bulunmayan İngiliz bir firmadan 2026/Mayıs döneminde 500.000 ₺ "
    "karşılığında pazar araştırması hizmeti satın almıştır. Hizmet İngiltere’de hazırlanmış, sonuçlarından Türkiye’deki "
    f"satış faaliyetlerinde faydalanılmıştır. {ORAN}\n\n{K}, (STU) A.Ş.’nin sorumlu sıfatıyla beyan edeceği KDV kaç ₺’dir?",
    tl(sr), secenekler(sr, 0, 500_000 * 0.18, 500_000 * 0.10, 500_000 * 0.20 * 1.2),
    "Md. 6/b'ye göre hizmetten Türkiye'de faydalanılması işlemin Türkiye'de yapılması sayılır. Hizmeti veren Türkiye'de "
    "mükellefiyeti olmayan yabancı firma olduğundan md. 9 uyarınca alıcı KDV'yi sorumlu sıfatıyla beyan eder: 500.000 × "
    "%20 = 100.000 ₺.")

P.q("KDVK md. 12/2",
    f"{K}, hizmet ihracatı istisnasında “yurt dışındaki müşteri” kavramına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yurt içindeki bir firmanın yurt dışında kendi adına müstakilen faaliyet gösteren şubesi de yurt dışındaki müşteri sayılır.",
    ["Yurt dışındaki müşteri sadece yabancı uyruklu gerçek kişileri ifade eder.",
     "Türkiye’de iş merkezi bulunan yabancı şirketler yurt dışındaki müşteri sayılır.",
     "Bedeli döviz olarak ödeyen her alıcı yurt dışındaki müşteri sayılır.",
     "Yurt dışındaki müşteriye yapılan hizmetten Türkiye’de faydalanılsa da istisna uygulanır."],
    "Md. 12/2'ye göre yurt dışındaki müşteri; ikametgâhı, işyeri, kanuni ve iş merkezi yurt dışında olan alıcılar ile yurt "
    "içindeki firmanın yurt dışında kendi adına müstakilen faaliyet gösteren şubeleridir. Ayrıca hizmetten yurt dışında "
    "faydalanılması şarttır.", zorluk="hard")

amb = (100_000 - 10_000) * 0.20
P.sayisal("KDVK md. 2/4",
    "Maden suyu üreticisi (VYZ) A.Ş., 2026/Haziran döneminde bir markete 100.000 ₺ bedelle maden suyu teslim etmiştir. "
    "Bedelin 10.000 ₺’si, geri verilmesi mutat olan ve iade edilecek depozitolu cam şişelere aittir. "
    f"{ORAN}\n\n{K}, bu teslim için hesaplanacak KDV kaç ₺’dir?",
    tl(amb), secenekler(amb, 100_000 * 0.20, 10_000 * 0.20, 110_000 * 0.20, 100_000 * 0.10),
    "Md. 2/4'e göre kap ve ambalajların geri verilmesinin mutat olduğu hâllerde teslim bunlar dışında kalan maddeler "
    "itibarıyla yapılmış sayılır: (100.000 − 10.000) × %20 = 18.000 ₺.", zorluk="hard")

P.q("KDVK md. 11/1-a, 12/3",
    "(FGH) Tekstil A.Ş., serbest bölgede faaliyet gösteren bir firmaya ait kumaşları Türkiye’deki tesisinde dikip serbest "
    f"bölgeye geri göndermektedir; firma ürünlerden serbest bölgede faydalanmaktadır.\n\n{K}, bu fason hizmetin KDV "
    "karşısındaki durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Serbest bölgede faydalanılan fason hizmet istisnadır.",
    ["Hizmet Türkiye’de yapıldığından genel oranda vergilidir.",
     "Fason hizmetler sadece ihracat kaydıyla istisnadan yararlanamaz.",
     "Hizmet istisnadır ancak yüklenilen KDV indirilemez.",
     "Hizmet, bedel döviz olarak tahsil edilirse istisnadır."],
    "Md. 11/1-a'ya göre serbest bölgelerdeki müşteriler için yapılan fason hizmetler istisnadır; md. 12/3'e göre fason "
    "hizmetin serbest bölgedeki müşteri için yapılması ve hizmetten serbest bölgede faydalanılması gerekir.")

tr = 150_000 * 0.20
P.sayisal("KDVK md. 2/5, 27",
    "Kereste ticareti yapan (ZAB) Ltd. Şti., emsal bedeli 150.000 ₺ olan keresteyi, emsal bedeli 150.000 ₺ olan bir forklift "
    "karşılığında (CDE) A.Ş.’ye vermiştir; taraflar arasında ayrıca para ödenmemiştir. İki şirket de KDV mükellefidir. "
    f"{ORAN}\n\n{K}, (ZAB) Ltd. Şti.’nin bu işlem için hesaplayacağı KDV kaç ₺’dir?",
    tl(tr), secenekler(tr, 0, 300_000 * 0.20, 75_000 * 0.20, 150_000 * 0.18),
    "Md. 2/5'e göre trampa iki ayrı teslim hükmündedir; bedel paradan başka bir değer olduğundan md. 27 gereği matrah emsal "
    "bedelidir: 150.000 × %20 = 30.000 ₺. (CDE) A.Ş. de forklift teslimi için ayrıca KDV hesaplar.")

P.q("KDVK md. 17/1",
    "Bir belediye; şehir tiyatrosu, halk kütüphanesi ve spor tesisi işletmekte, ayrıca halka açık bir düğün salonunu "
    f"ticari olarak kiraya vermektedir.\n\n{K}, bu faaliyetlerden hangisi kültür ve eğitim amaçlı istisna kapsamında "
    "değildir?",
    "Düğün salonu kiralaması",
    ["Şehir tiyatrosu işletilmesi",
     "Halk kütüphanesi işletilmesi",
     "Spor tesisi işletilmesi",
     "Konferans salonu işletilmesi"],
    "Md. 17/1-b'ye göre belediyelerin tiyatro, konser salonu, kütüphane, sergi, okuma ve konferans salonları ile spor tesisleri "
    "işletmek suretiyle ifa ettikleri kültür ve eğitim faaliyetleri istisnadır; ticari nitelikteki düğün salonu kiralaması bu "
    "kapsamda değildir.")

kb = 20_000 * 0.20
P.sayisal("KDVK md. 5, 27",
    "Araç kiralama şirketi (DEF) A.Ş., emsal kira bedeli 20.000 ₺ olan bir aracını 2026/Temmuz ayında şirket müdürünün "
    "tatilinde kullanmasına karşılıksız olarak bırakmıştır. "
    f"{ORAN}\n\n{K}, bu işlem için hesaplanacak KDV kaç ₺’dir?",
    tl(kb), secenekler(kb, 0, 20_000 * 0.10, 20_000 * 0.18, 20_000),
    "Md. 5'e göre vergiye tabi bir hizmetten işletme personelinin karşılıksız yararlandırılması hizmet sayılır; matrah md. 27 "
    "gereği emsal ücretidir: 20.000 × %20 = 4.000 ₺.")

P.q("KDVK md. 17/4-a",
    f"{K}, esnaf ve basit usul mükelleflerine ilişkin istisna hakkında aşağıdaki ifadelerden hangisi yanlıştır?",
    "Basit usul mükelleflerinin teslimleri genel oranda vergilendirilir.",
    ["GVK’ya göre vergiden muaf esnafın teslim ve hizmetleri istisnadır.",
     "Kazançları basit usulde tespit edilenlerin teslim ve hizmetleri istisnadır.",
     "Gerçek usulde vergiye tabi olmayan çiftçilerin teslimleri istisnadır.",
     "GVK md. 66’ya göre vergiden muaf serbest meslek erbabının hizmetleri istisnadır."],
    "Md. 17/4-a ve b'ye göre GVK'ya göre muaf esnaf, basit usul mükellefleri, gerçek usulde vergiye tabi olmayan çiftçiler ve "
    "md. 66'ya göre muaf serbest meslek erbabının teslim ve hizmetleri istisnadır.", zorluk="easy")

tc3 = min(2_000_000 * 0.20, 3_000_000 * 0.20 - 350_000 - 150_000)
P.sayisal("KDVK md. 11/1-c",
    "İmalatçı (FGH) A.Ş. 2026/Temmuz döneminde yurt içinde 1.000.000 ₺ normal teslim, ihracatçıya ihraç kaydıyla "
    "2.000.000 ₺ teslim yapmıştır. Dönemin indirilecek KDV’si 350.000 ₺, önceki dönemden devreden KDV 150.000 ₺’dir. "
    f"{ORAN}\n\n{K}, (FGH) A.Ş.’nin 2026/Temmuz döneminde tecil edilecek KDV tutarı kaç ₺’dir?",
    tl(tc3), secenekler(tc3, 400_000, 250_000, 200_000, 600_000),
    "Tecil edilebilir KDV 2.000.000 × %20 = 400.000 ₺. Ödenmesi gereken KDV: (1.000.000 + 2.000.000) × %20 = 600.000 − "
    "350.000 − 150.000 = 100.000 ₺. Tecil edilecek KDV ikisinden küçük olan 100.000 ₺'dir.", zorluk="hard")

P.q("KDVK md. 17/4-e",
    "Bir sigorta acentesi, sigorta şirketleri adına poliçe düzenleyip komisyon almaktadır; ayrıca aynı acente bir müşterisine "
    f"ücret karşılığında muhasebe danışmanlığı vermiştir.\n\n{K}, bu işlemlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sigorta aracılığı istisna, danışmanlık vergilidir.",
    ["Her iki işlem de BSMV kapsamında olduğundan KDV’den istisnadır.",
     "Her iki işlem de genel oranda KDV’ye tabidir.",
     "Sigorta aracılığı vergili, muhasebe danışmanlığı istisnadır.",
     "Acente mükellef olmadığından iki işlem de KDV dışındadır."],
    "Md. 17/4-e'ye göre BSMV kapsamındaki işlemler ile sigorta aracılarının sigorta şirketlerine yaptığı sigorta muamelelerine "
    "ilişkin işlemler istisnadır; bunun dışındaki danışmanlık hizmetleri genel hükümlere göre vergilidir.")

hr = 700_000 * 0.20
P.sayisal("KDVK md. 17/4-g",
    "Geri dönüşüm firması (IJK) Ltd. Şti. 2026/Mart döneminde 300.000 ₺ tutarında metal hurda ile 700.000 ₺ tutarında "
    "hurdadan ürettiği işlenmiş alüminyum profil teslim etmiştir. (Vergiye tabi teslimlerde KDV oranı %20 olarak "
    f"alınacaktır.)\n\n{K}, (IJK) Ltd. Şti.’nin 2026/Mart dönemi hesaplanan KDV tutarı kaç ₺’dir?",
    tl(hr), secenekler(hr, 1_000_000 * 0.20, 300_000 * 0.20, 0, 700_000 * 0.10),
    "Md. 17/4-g'ye göre metal, plastik, lastik, kauçuk, kâğıt ve cam hurda ve atıklarının teslimi istisnadır; hurdadan "
    "üretilen mamul ürünün teslimi vergilidir: 700.000 × %20 = 140.000 ₺.")

P.q("KDVK md. 13/a",
    f"{K}, deniz taşıma araçlarının tesliminde KDV istisnasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İstisna, faaliyeti bu araçların kiralanması veya işletilmesi olan mükelleflere bu amaçla yapılan teslimleri kapsar.",
    ["Deniz taşıma aracı kimin tarafından satın alınırsa alınsın teslimi istisnadır.",
     "Sadece yabancı ülkelere ihraç edilen gemilerin teslimi istisnadır.",
     "Gemilerin onarım ve bakım hizmetleri istisna kapsamı dışındadır.",
     "İstisna sadece hava taşıma araçları için geçerlidir."],
    "Md. 13/a'ya göre faaliyetleri kısmen veya tamamen deniz, hava ve demiryolu taşıma araçlarının kiralanması veya "
    "işletilmesi olan mükelleflere bu amaçla yapılan teslimler ile bu araçların imal, inşa, tadil, onarım ve bakımına ilişkin "
    "teslim ve hizmetler istisnadır.")

ar = 10_000 * 0.20
P.sayisal("KDVK md. 1/3-f, 17/4-d",
    "Ticari faaliyeti bulunmayan emekli Bay (P), 2026/Mart ayında sahibi olduğu bir daireyi aylık 20.000 ₺’ye konut olarak, "
    "özel otomobilini ise aylık 10.000 ₺’ye bir şirkete kiraya vermiştir. Bu malvarlıkları bir işletmeye dahil değildir. "
    f"{ORAN}\n\n{K}, Bay (P)’nin 2026/Mart ayı kira gelirleri için hesaplanacak KDV kaç ₺’dir?",
    tl(ar), secenekler(ar, 30_000 * 0.20, 20_000 * 0.20, 0, 30_000 * 0.10),
    "Md. 1/3-f'ye göre GVK md. 70'teki mal ve hakların kiralanması KDV'ye tabidir; md. 17/4-d'deki istisna yalnız iktisadi "
    "işletmelere dahil olmayan gayrimenkullerin kiralanmasına ilişkindir. Otomobil kirası vergilidir: 10.000 × %20 = "
    "2.000 ₺.", zorluk="hard")

P.q("KDVK md. 11/1-a",
    f"{K}, aşağıdakilerden hangisi ihracat istisnası kapsamında değildir?",
    "Türkiye’deki bir firmaya verilen ve Türkiye’de faydalanılan reklam hizmeti",
    ["İhracat teslimleri ve bu teslimlere ilişkin hizmetler",
     "Yurt dışındaki müşteriler için yapılan hizmetler",
     "Serbest bölgelerdeki müşteriler için yapılan fason hizmetler",
     "Karşılıklılık şartıyla yurt dışındaki müşterilere Türkiye’de verilen roaming hizmetleri"],
    "Md. 11/1-a'ya göre ihracat teslimleri ve bunlara ilişkin hizmetler, yurt dışındaki müşteriler için yapılan hizmetler, "
    "serbest bölgelerdeki müşteriler için fason hizmetler ve karşılıklı roaming hizmetleri istisnadır. Yurt içi müşteriye "
    "verilen ve Türkiye'de faydalanılan hizmet vergilidir.", zorluk="easy")

zn = 1_200_000 * 0.20
P.sayisal("KDVK md. 2/2",
    "(LMN) A.Ş., (OPR) Ltd. Şti.’den 1.000.000 ₺’ye satın aldığı makineleri, kendi deposuna getirmeden, (PRS) A.Ş.’ye "
    "1.200.000 ₺’ye satmıştır. Makineler doğrudan (OPR) Ltd. Şti.’nin deposundan (PRS) A.Ş.’ye gönderilmiştir. "
    f"{ORAN}\n\n{K}, (LMN) A.Ş.’nin (PRS) A.Ş.’ye yaptığı teslim için hesaplayacağı KDV kaç ₺’dir?",
    tl(zn), secenekler(zn, 0, 200_000 * 0.20, 1_000_000 * 0.20, 2_200_000 * 0.20),
    "Md. 2/2'ye göre tasarruf hakkının zincirleme akitlerle, mal el değiştirmeden doğrudan sonuncu kişiye devredilmesi "
    "hâlinde aradaki safhaların her biri ayrı bir teslimdir: 1.200.000 × %20 = 240.000 ₺.")

P.q("KDVK md. 8/2",
    "(GHI) A.Ş., istisna kapsamındaki bir teslim için düzenlediği faturada yanlışlıkla KDV hesaplamış, alıcıdan tahsil "
    f"etmiş ve beyan ederek ödemiştir.\n\n{K}, bu yersiz hesaplanan verginin iadesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Beyanlar düzeltilmeli ve vergi alıcıya geri verilmelidir.",
    ["Yersiz ödenen vergi kural gereği iade edilmez.",
     "Vergi, alıcıya doğrudan vergi dairesince iade edilir.",
     "Vergi, satıcıya herhangi bir şart aranmaksızın iade edilir.",
     "Yersiz ödenen vergi satıcının gelecek yıl kurumlar vergisinden mahsup edilir."],
    "Md. 8/2'ye göre fazla veya yersiz hesaplanan ve Hazineye ödenen vergi, Bakanlığın belirleyeceği usullere göre işlemi "
    "yapan mükellefe iade edilir; iade için beyanların düzeltilmesi ve verginin satıcı tarafından alıcıya geri verilmesi "
    "şarttır.", zorluk="hard")

ist = 80_000 * 0.20
P.sayisal("KDVK md. 3/b, 27",
    "(STU) A.Ş., KDV’den istisna olan engellilere özel araç-gereç üretiminde, kendi ürettiği ve normalde vergiye tabi olarak "
    "sattığı emsal bedeli 80.000 ₺ olan elektronik parçaları kullanmıştır. "
    f"{ORAN}\n\n{K}, bu parçaların kullanımı nedeniyle hesaplanacak KDV kaç ₺’dir?",
    tl(ist), secenekler(ist, 0, 80_000 * 0.10, 80_000 * 0.18, 80_000),
    "Md. 3/b'ye göre vergiye tabi malların, üretilip teslimi vergiden istisna edilmiş olan mallar için kullanılması teslim "
    "sayılır; matrah emsal bedelidir: 80.000 × %20 = 16.000 ₺.", zorluk="hard")

P.q("KDVK md. 17/4-c",
    f"{K}, aşağıdaki işlemlerden hangisi KDV’den istisna değildir?",
    "Ferdi işletmedeki tek bir makinenin satışı",
    ["Ferdi işletmenin bütün hâlinde sermaye şirketine devri",
     "Şartları sağlayan adi ortaklığın sermaye şirketine dönüşmesi",
     "KVK’ya göre yapılan devir işlemi",
     "KVK’ya göre yapılan bölünme işlemi"],
    "Md. 17/4-c'ye göre GVK md. 81'deki işlemler (ferdi işletmenin bütün hâlinde sermaye şirketine devri gibi), şartlı adi "
    "ortaklık dönüşümleri ve KVK'ya göre yapılan devir ve bölünme işlemleri istisnadır. Tek bir makinenin satışı olağan "
    "vergili bir teslimdir.")

mm = 600_000 * 0.20
P.sayisal("KDVK md. 3/c",
    "(VYZ) A.Ş., 2026/Mart ayında bir müşterisine 600.000 ₺ bedelle iş makinesi satmış; bedel 12 eşit aylık taksitle "
    "ödenecek, mülkiyet son taksit ödenene kadar satıcıda kalacaktır. Makine Mart ayında alıcıya teslim edilmiş ve "
    f"alıcı makineyi kullanmaya başlamıştır. {ORAN}\n\n{K}, (VYZ) A.Ş.’nin bu satış için 2026/Mart döneminde hesaplayacağı "
    "KDV kaç ₺’dir?",
    tl(mm), secenekler(mm, 50_000 * 0.20, 0, 600_000 * 0.10, 600_000 * 0.18),
    "Md. 3/c'ye göre mülkiyeti muhafaza kaydıyla yapılan satışlarda zilyetliğin devri teslim sayılır; vergiyi doğuran olay "
    "Mart ayında meydana gelir: 600.000 × %20 = 120.000 ₺.")

if __name__ == "__main__":
    sys.exit(P.yaz())
