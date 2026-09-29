# -*- coding: utf-8 -*-
"""Vergi · Vergi Hukuku · Vergi Uyuşmazlıkları (düzeltme, uzlaşma, vergi yargısı) — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında uyuşmazlık konusu; başvuru ve dava süreleri ile idari çözüm yolları (düzeltme,
uzlaşma, izaha davet) üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 213 sayılı VUK md. 116-126, 376, Ek md. 1, 6-9, 11
(7524 sayılı Kanunla uzlaşmanın cezalarla sınırlandırılması dahil); 2577 sayılı İYUK md. 3, 7, 10, 11, 16, 27, 37, 45,
46. Yeniden değerlenen parasal sınırlar sorulmaz veya kökte verilir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_vergi_uyusmazliklari_2026.json", lesson="vergi_hukuku", topic="vergi_uyusmazliklari",
          konu_adi="Vergi Uyuşmazlıkları", seed=2026092910,
          surum="213 sayılı VUK (7524 dahil) ve 2577 sayılı İYUK (7589 dahil) güncel metni; 29.09.2026 kontrolü")

V = "213 sayılı Vergi Usul Kanunu’na göre"
V26 = "213 sayılı Vergi Usul Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
I = "2577 sayılı İdari Yargılama Usulü Kanunu’na göre"
I26 = "2577 sayılı İdari Yargılama Usulü Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İYUK md. 7",
    "(ABC) A.Ş.’ye vergi incelemesi sonucunda düzenlenen vergi ve ceza ihbarnamesi tebliğ edilmiştir. Şirket uzlaşma "
    f"talebinde bulunmadan dava açmak istemektedir.\n\n{I}, vergi mahkemesinde dava açma süresi kaç gündür?",
    "30", ["15", "45", "60", "90"],
    "İYUK md. 7/1'e göre dava açma süresi, özel kanunlarında ayrı süre gösterilmeyen hâllerde Danıştay ve idare "
    "mahkemelerinde altmış, vergi mahkemelerinde otuz gündür.", zorluk="easy")

P.q("VUK md. 117",
    "Bir mükellefin gelir vergisi beyannamesinde indirilecek tutar yanlış toplandığı için matrah fazla hesaplanmış ve buna "
    f"bağlı olarak fazla vergi tahakkuk etmiştir.\n\n{V}, bu hata hangi türdedir?",
    "Matrah hatası",
    ["Mükellefin şahsında hata", "Mükellefiyette hata", "Mevzuda hata", "Vergilendirme döneminde hata"],
    "Md. 117/1'e göre vergilendirme ile ilgili belgelerde matraha ait rakamların veya indirimlerin eksik veya fazla gösterilmiş "
    "ya da hesaplanmış olması matrah hatasıdır ve hesap hataları arasındadır.", zorluk="easy")

P.q("VUK md. 118",
    "Vergi dairesi, bir borcun asıl borçlusu olan Bay (P) yerine aynı soyadı taşıyan kardeşi Bay (R)’den vergi istemiştir."
    f"\n\n{V}, bu hata hangi türdedir?",
    "Mükellefin şahsında hata",
    ["Mükellefiyette hata", "Mevzuda hata", "Vergi miktarında hata", "Verginin mükerrer olması"],
    "Md. 118/1'e göre bir verginin asıl borçlusu yerine başka bir kişiden istenmesi veya alınması mükellefin şahsında hatadır; "
    "vergilendirme hataları arasındadır.")

P.sayisal("İYUK md. 7",
    "Bir belediye meclisinin düzenleyici nitelik taşımayan bir idari işlemi, işlemin muhatabına yazılı olarak bildirilmiştir. "
    f"Muhatap işleme karşı idare mahkemesinde iptal davası açacaktır.\n\n{I}, bu dava için dava açma süresi kaç gündür?",
    "60", ["15", "30", "45", "90"],
    "İYUK md. 7/1'e göre dava açma süresi Danıştay ve idare mahkemelerinde altmış, vergi mahkemelerinde otuz gündür; süre "
    "yazılı bildirimin yapıldığı tarihi izleyen günden başlar.")

P.q("VUK md. 117-118",
    f"Bir vergi dairesi müdürü, düzeltme taleplerini hata türlerine göre sınıflandırarak hesap hataları ile vergilendirme hatalarını ayırmaktadır.\n\n{V}, aşağıdakilerden hangisi hesap hataları arasında yer almaz?",
    "Mükellefiyette hata",
    ["Matrah hataları", "Vergi miktarında hatalar", "Verginin mükerrer olması", "Nispetin yanlış uygulanması"],
    "Md. 117'ye göre hesap hataları matrah hataları, vergi miktarında hatalar (nispetin yanlış uygulanması dahil) ve verginin "
    "mükerrer olmasıdır. Mükellefiyette hata md. 118'e göre vergilendirme hatasıdır.")

P.q("VUK md. 118",
    "Vergiden muaf bir kuruluştan, muaf olduğu açıkça anlaşıldığı hâlde vergi istenmiştir."
    f"\n\n{V}, bu hata hangi türdedir?",
    "Mükellefiyette hata",
    ["Mevzuda hata", "Matrah hatası", "Verginin mükerrer olması", "Mükellefin şahsında hata"],
    "Md. 118/2'ye göre açık olarak vergiye tabi olmayan veya vergiden muaf bulunan kimselerden vergi istenmesi veya "
    "alınması mükellefiyette hatadır.")

P.sayisal("İYUK md. 45",
    "Vergi mahkemesi, (DEF) Ltd. Şti.’nin açtığı davayı reddetmiş ve karar şirkete tebliğ edilmiştir. Uyuşmazlık tutarı "
    f"istinaf sınırının üzerindedir.\n\n{I26}, şirket kararın tebliğinden itibaren kaç gün içinde istinaf yoluna "
    "başvurabilir?",
    "30", ["7", "15", "45", "60"],
    "İYUK md. 45/1'e göre idare ve vergi mahkemelerinin kararlarına karşı kararın tebliğinden itibaren otuz gün içinde "
    "bölge idare mahkemesine istinaf yoluna başvurulabilir; Kanundaki tutarı geçmeyen davalardaki kararlar kesindir.")

P.q("VUK md. 118",
    f"Vergi dairesi, açıkça vergiden istisna olan bir işlem nedeniyle bir mükelleften vergi istemiş; mükellef bu durumun hangi tür hata olduğunu sormaktadır.\n\n{V}, mevzuda hataya ilişkin aşağıdakilerden hangisi doğrudur?",
    "İstisna veya konu dışı işlemden vergi alınmasıdır.",
    ["Verginin asıl borçlusu yerine başkasından alınmasıdır.",
     "Aynı matrah üzerinden birden fazla vergi alınmasıdır.",
     "Vergi nispetinin yanlış uygulanmasıdır.",
     "Vergilendirme döneminin yanlış gösterilmesidir."],
    "Md. 118/3'e göre açık olarak vergi mevzuuna girmeyen veya vergiden müstesna bulunan gelir, servet, madde, kıymet, evrak "
    "ve işlemler üzerinden vergi istenmesi veya alınması mevzuda hatadır.")

P.q("VUK md. 119",
    f"Bir teftiş raporunda, vergi dairesindeki bazı hatalı tahakkukların farklı yollarla tespit edildiği belirtilmiştir.\n\n{V}, aşağıdakilerden hangisi vergi hatalarının meydana çıkarılma yollarından biri değildir?",
    "Mükellefin sosyal medya paylaşımı",
    ["İlgili memurun hatayı bulması", "Üst memurların incelemesi", "Teftiş sırasında hatanın bulunması",
     "Mükellefin başvurusu"],
    "Md. 119'a göre vergi hataları ilgili memurun bulması, üst memurların incelemesi, teftiş, vergi incelemesi ve mükellefin "
    "başvurusu yollarıyla meydana çıkarılabilir.", zorluk="easy")

P.sayisal("İYUK md. 10",
    "Bay (K), vergi dairesine bir işlem yapılması için başvurmuş; idare 30 gün içinde kesin olmayan bir cevap vermiştir. "
    f"Bay (K) kesin cevabı beklemeyi tercih etmiştir.\n\n{I}, bu bekleme süresi başvuru tarihinden itibaren en fazla kaç ay "
    "olabilir?",
    "4", ["1", "2", "6", "12"],
    "İYUK md. 10/2'ye göre otuz gün içinde verilen cevap kesin değilse ilgili kesin cevabı bekleyebilir; bu takdirde dava "
    "açma süresi işlemez, ancak bekleme süresi başvuru tarihinden itibaren dört ayı geçemez.", zorluk="hard")

P.q("VUK md. 120-121",
    f"Bir vergi dairesinde tespit edilen hatalı tarhiyatların nasıl ve kim tarafından düzeltileceği değerlendirilmektedir.\n\n{V}, vergi hatalarının düzeltilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Düzeltmeye vergi mahkemesi karar verir.",
    ["Düzeltmeye ilgili vergi dairesi müdürü karar verir.",
     "Hatalar düzeltme fişine dayanılarak düzeltilir.",
     "Açık ve mutlak vergi hataları resen düzeltilir.",
     "Aleyhine düzeltme yapılanların dava açma hakkı saklıdır."],
    "Md. 120'ye göre vergi hatalarının düzeltilmesine ilgili vergi dairesi müdürü karar verir; md. 121'e göre idarece "
    "tereddüt edilmeyen açık ve mutlak hatalar resen düzeltilir, aleyhine düzeltme yapılanların dava hakkı saklıdır.")

P.q("VUK md. 122-124",
    "Bay (S), vergi dairesine yaptığı düzeltme talebinin reddedilmesinden sonra dava açma süresini de kaçırmıştır. Bay (S), "
    f"hatanın açık olduğunu düşünmektedir.\n\n{V}, Bay (S)’nin başvurabileceği yol aşağıdakilerden hangisidir?",
    "Şikâyet yoluyla Maliye Bakanlığına başvurmak",
    ["Uzlaşma komisyonuna başvurmak",
     "Doğrudan Danıştaya temyiz başvurusunda bulunmak",
     "Vergi dairesine yeniden düzeltme talebinde bulunmak",
     "Anayasa Mahkemesine bireysel başvuru yapmak"],
    "Md. 124'e göre dava açma süresi geçtikten sonra yaptıkları düzeltme talepleri reddolunanlar şikâyet yoluyla Maliye "
    "Bakanlığına başvurabilir; belediye vergilerinde belediye başkanlığına başvurulur.", zorluk="hard")

P.sayisal("İYUK md. 11",
    "Bay (L)’ye vergi ihbarnamesi 1 Mart 2026’da tebliğ edilmiştir. Bay (L), 10 Mart 2026’da işlemin geri alınması için "
    "vergi dairesine başvurmuş; başvurusu reddedilmiş ve ret 20 Mart 2026’da tebliğ edilmiştir. Vergi mahkemesinde dava "
    f"açma süresi 30 gündür.\n\n{I}, ret kararının tebliğinden sonra Bay (L)’nin dava açmak için kalan süresi kaç gündür?",
    "21", ["9", "15", "30", "60"],
    "İYUK md. 11'e göre üst makama başvuru işlemeye başlamış dava açma süresini durdurur; ret hâlinde süre yeniden işler ve "
    "başvuru tarihine kadar geçen süre hesaba katılır. 2-10 Mart arasında 9 gün geçmiştir; kalan süre 30 − 9 = 21 gündür.",
    zorluk="hard")

P.q("VUK md. 122",
    f"Fazla vergi ödediğini düşünen bir mükellef, hatanın düzeltilmesi için vergi dairesine nasıl başvuracağını araştırmaktadır.\n\n{V}, düzeltme talebine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hataların düzeltilmesi yazıyla istenebilir.",
    ["Düzeltme talebi sadece sözlü olarak yapılabilir.",
     "Düzeltme talebi sadece vergi mahkemesine yapılır.",
     "Düzeltme talebi posta ile gönderilemez.",
     "Düzeltme talebi için avukat şarttır."],
    "Md. 122'ye göre mükellefler vergi muamelelerindeki hataların düzeltilmesini vergi dairesinden yazıyla isteyebilir; bu "
    "taleplerin posta ile taahhütlü gönderilmesi caizdir.", zorluk="easy")

P.q("VUK md. 126",
    f"Bir mükellef, yıllar önce yapılmış bir vergi hatasının düzeltilmesini isteyip isteyemeyeceğini değerlendirmektedir.\n\n{V}, düzeltme zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zamanaşımından sonra bulunan hatalar düzeltilemez.",
    ["Vergi hataları süre sınırı olmaksızın düzeltilebilir.",
     "Düzeltme zamanaşımı on yıldır.",
     "Düzeltme zamanaşımı mükellefin başvurusuyla başlar.",
     "İlan yoluyla tebliğ edilen vergilerde düzeltme yapılamaz."],
    "Md. 126'ya göre md. 114'teki zamanaşımı süresi dolduktan sonra meydana çıkarılan vergi hataları düzeltilemez; bazı "
    "hâllerde düzeltme zamanaşımı belirli tarihten itibaren bir yıldan aşağı olamaz.")

P.sayisal("VUK Ek md. 1",
    "(GHI) A.Ş. adına kesilen vergi ziyaı cezasına ilişkin ihbarname 2 Mart 2026’da tebliğ edilmiştir. Şirket tarhiyat "
    f"sonrası uzlaşma talep etmek istemektedir.\n\n{V26}, uzlaşma talebi ihbarnamenin tebliğ tarihinden itibaren kaç gün "
    "içinde yapılmalıdır?",
    "30", ["7", "15", "45", "60"],
    "Ek md. 1'e göre uzlaşma talebi vergi ihbarnamesinin tebliğ tarihinden itibaren otuz gün içinde yapılır.", zorluk="easy")

P.q("VUK Ek md. 1",
    "(CDE) A.Ş. adına vergi incelemesi sonucunda ikmalen vergi tarh edilmiş ve vergi ziyaı cezası kesilmiştir. Şirket "
    f"uzlaşma talep etmeyi düşünmektedir.\n\n{V26}, tarhiyat sonrası uzlaşmanın konusuna ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Sadece vergi ziyaı cezası uzlaşmaya konu edilebilir.",
    ["Vergi aslı ve ceza birlikte uzlaşmaya konu edilir.",
     "Sadece vergi aslı uzlaşmaya konu edilir.",
     "İkmalen tarhiyatlarda uzlaşma yapılamaz.",
     "Uzlaşma sadece usulsüzlük cezaları için yapılır."],
    "Ek md. 1'in 7524 sayılı Kanunla değişik hâline göre uzlaşma ikmalen, resen veya idarece tarh edilen vergilere ilişkin "
    "vergi ziyaı cezaları ile Kanundaki tutarı aşan usulsüzlük ve özel usulsüzlük cezalarının miktarı konusunda yapılır; "
    "vergi aslı uzlaşmaya konu edilmez.", zorluk="hard")

P.q("VUK Ek md. 1",
    f"Bir uzlaşma komisyonu, önüne gelen başvurulardan hangilerinin uzlaşmaya konu edilebileceğini incelemektedir.\n\n{V26}, aşağıdaki cezalardan hangisi uzlaşmaya konu edilemez?",
    "Sahte belgeyle ziyada kesilen üç kat ceza",
    ["İkmalen tarh edilen vergiye ilişkin bir kat vergi ziyaı cezası",
     "Resen tarh edilen vergiye ilişkin vergi ziyaı cezası",
     "Kanundaki tutarı aşan özel usulsüzlük cezası",
     "Kanundaki tutarı aşan usulsüzlük cezası"],
    "Ek md. 1'e göre md. 359'daki fiillerle vergi ziyaına sebebiyet verilmesi hâlinde kesilen ceza, bu fiillere iştirak "
    "edenlere kesilen ceza ve md. 370/b kapsamındaki cezalar uzlaşma kapsamı dışındadır.")

P.sayisal("VUK Ek md. 7",
    "(JKL) Ltd. Şti.’nin uzlaşma talebi sonucunda uzlaşma vaki olmamıştır. Tutanak tebliğ edildiğinde dava açma süresinin "
    f"bitmesine 8 gün kalmıştır.\n\n{V}, şirketin dava açma süresi tutanağın tebliğinden itibaren kaç gün olur?",
    "15", ["8", "10", "30", "60"],
    "Ek md. 7'ye göre uzlaşmanın vaki olmaması hâlinde dava açma süresi bitmiş veya 15 günden az kalmışsa bu süre tutanağın "
    "tebliği tarihinden itibaren 15 gün olarak uzar.", zorluk="hard")

P.q("VUK Ek md. 1",
    f"{V}, aşağıdakilerden hangisi uzlaşma talebinde ileri sürülebilecek sebeplerden biri değildir?",
    "Mükellefin ödeme gücünün bulunmaması",
    ["Kanun hükümlerine yeterince nüfuz edememe",
     "Md. 369’daki yanılma",
     "Vergi hatası veya maddi hata bulunması",
     "Yargı kararları ile idarenin görüş farklılığı"],
    "Ek md. 1'e göre vergi ziyaının kanun hükümlerine yeterince nüfuz edememekten, md. 369'daki yanılmadan, vergi veya maddi "
    "hatalardan ya da yargı kararlarıyla idare arasındaki görüş farklılığından kaynaklandığının ileri sürülmesi hâlinde "
    "uzlaşılabilir. Ödeme gücü uzlaşma sebebi değildir.", zorluk="hard")

P.q("VUK Ek md. 1",
    f"Tarhiyat sonrası uzlaşma talebinde bulunan bir şirket, uzlaşma sürecinin nasıl işleyeceğini ve sonuçlarını araştırmaktadır.\n\n{V}, uzlaşma usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Uzlaşma vaki olmazsa mükellef aynı ceza için yeniden uzlaşma talep edebilir.",
    ["Uzlaşma talebi ihbarnamenin tebliğinden itibaren otuz gün içinde yapılır.",
     "Uzlaşmanın vaki olmadığına dair tutanağa idarenin nihai teklifi yazılır.",
     "Mükellef nihai teklifi dava açma süresi içinde yazıyla kabul ederse uzlaşma sağlanmış sayılır.",
     "Mükellef uzlaşma görüşmelerinde bir meslek mensubu bulundurabilir."],
    "Ek md. 1'e göre uzlaşmanın vaki olmaması veya temin edilememesi hâlinde yeniden uzlaşma talebinde bulunulamaz.")

P.sayisal("VUK Ek md. 8",
    "(MNO) A.Ş. ile vergi idaresi arasında uzlaşma sağlanmış; uzlaşma tutanağı, cezanın ödeme zamanı geçtikten sonra şirkete "
    f"tebliğ edilmiştir.\n\n{V}, uzlaşılan ceza tutanağın tebliğinden itibaren en geç kaç ay içinde ödenmelidir?",
    "1", ["2", "3", "6", "12"],
    "Ek md. 8'e göre uzlaşma vaki olduğunda tutanak ödeme zamanlarından sonra tebliğ edilmişse, ödeme süreleri geçmiş olanlar "
    "uzlaşma tutanağının tebliğinden itibaren bir ay içinde ödenir.")

P.q("VUK Ek md. 6",
    "(FGH) A.Ş. ile idare arasında uzlaşma sağlanmış ve tutanak imzalanmıştır. Şirket daha sonra uzlaşılan cezanın yüksek "
    f"olduğunu düşünmüştür.\n\n{V}, şirketin durumu hakkında aşağıdakilerden hangisi doğrudur?",
    "Uzlaşılan hususlar hakkında dava açamaz ve şikâyette bulunamaz.",
    ["Tutanağın tebliğinden itibaren 30 gün içinde dava açabilir.",
     "Uzlaşma tutanağına itiraz ederek yeniden uzlaşma talep edebilir.",
     "Tutanak vergi dairesi onaylamadıkça kesinleşmez.",
     "Maliye Bakanlığına şikâyet yoluyla başvurabilir."],
    "Ek md. 6'ya göre uzlaşma tutanakları kesindir ve vergi dairelerince derhal yerine getirilir; üzerinde uzlaşılan ve "
    "tutanakla tespit olunan hususlar hakkında dava açılamaz ve herhangi bir mercie şikâyette bulunulamaz.")

P.q("VUK Ek md. 7",
    "(IJK) A.Ş., uzlaşma talebinden önce aynı ceza için vergi mahkemesinde dava açmıştır."
    f"\n\n{V}, bu davanın durumu hakkında aşağıdakilerden hangisi doğrudur?",
    "Dava uzlaşma sonuçlanmadan incelenmez.",
    ["Dava açıldığından uzlaşma talebi reddedilir.",
     "Dava ve uzlaşma birlikte yürütülür, önce biten geçerli olur.",
     "Dava açılması uzlaşma hakkını ortadan kaldırmaz ve dava normal şekilde görülür.",
     "Uzlaşma talebi davadan feragat sayılır."],
    "Ek md. 7'ye göre mükellef aynı ceza için uzlaşma talebinden önce dava açmışsa dava, uzlaşma işlemi sonuçlanmadan "
    "incelenmez; herhangi bir sebeple incelenip karara bağlanırsa karar hükümsüz sayılır.", zorluk="hard")

P.sayisal("VUK md. 120",
    "Vergi dairesi müdürü, Bayan (M)’den fazla alınan bir vergiyi düzeltme fişiyle terkin etmiş ve reddedilecek tutarı "
    f"bildiren fişi Bayan (M)’ye tebliğ etmiştir.\n\n{V}, Bayan (M) parasını geri almak için tebliğden itibaren en geç kaç yıl "
    "içinde başvurmalıdır?",
    "1", ["2", "3", "5", "10"],
    "Md. 120'ye göre düzeltme fişinin bir nüshası mükellefe tebliğ edilir; mükellef tebliğden başlayarak bir yıl içinde "
    "parasını geri almak üzere başvurmazsa hakkı düşer.")

P.q("VUK Ek md. 9",
    "(LMN) Ltd. Şti. adına kesilen cezaya ilişkin 376. madde uyarınca indirim talebinde bulunulmuştur. Şirket daha sonra "
    f"aynı ceza için uzlaşma talep etmek istemektedir.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "376. madde uygulanan cezalar için uzlaşma hükümleri uygulanmaz.",
    ["Şirket hem indirim hem uzlaşmadan birlikte yararlanır.",
     "Uzlaşma talebi indirim talebini resen iptal eder.",
     "Uzlaşılan cezaya ayrıca 376. madde indirimi uygulanır.",
     "Uzlaşma ancak indirimden vazgeçilirse bir yıl sonra yapılabilir."],
    "Ek md. 9'a göre hakkında md. 376/1-1 hükümleri uygulanan cezalar için uzlaşma hükümleri uygulanmaz; uzlaşılan cezalara "
    "başkaca indirim uygulanmaz. Mükellef tutanağı imzalayıncaya kadar uzlaşmadan vazgeçerek md. 376'dan yararlanmayı "
    "isteyebilir.", zorluk="hard")

P.q("VUK Ek md. 11",
    f"{V26}, tarhiyat öncesi uzlaşmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Anlaşma olmazsa sonradan uzlaşma istenebilir.",
    ["Vergi incelemesine dayanılarak kesilecek cezalar için yapılabilir.",
     "Kaçakçılık fiilleriyle ziyada kesilecek ceza kapsam dışıdır.",
     "Uzlaşmaya varılırsa tutanaktaki hususlar hakkında dava açılamaz.",
     "Usulsüzlük cezalarında fiil bazında toplam ceza tutarı dikkate alınır."],
    "Ek md. 11'e göre tarhiyat öncesi uzlaşmanın temin edilememesi veya uzlaşmaya varılamaması hâlinde mükellefler, cezanın "
    "kesilmesinden sonra uzlaşma talep edemez.", zorluk="hard")

u1 = 30_000 * 0.25
P.sayisal("VUK Ek md. 1, 376",
    "(PRS) Ltd. Şti. adına vergi aslına bağlı olmaksızın, tek fiil nedeniyle toplam 30.000 ₺ usulsüzlük cezası kesilmiştir. "
    "Şirket cezayı indirimli ödemek istemektedir. (Uzlaşma için Kanunda belirtilen usulsüzlük cezası tutarı 40.000 ₺ olarak "
    f"alınacaktır.)\n\n{V26}, şirket 376. madde şartlarını yerine getirirse ödeyeceği ceza kaç ₺’dir?",
    tl(u1), secenekler(u1, 15_000, 30_000, 10_000, 20_000),
    "Ek md. 1'e göre Kanundaki tutarı aşmayan usulsüzlük cezaları uzlaşmaya konu edilemez; bunlar için md. 376'daki indirim "
    "oranı %50 artırımlı (%75) uygulanır: 30.000 × %25 = 7.500 ₺.", zorluk="hard")

P.q("VUK Ek md. 11",
    "(OPR) A.Ş. hakkında vergi incelemesi devam etmektedir. İnceleme elemanı cezayı gerektiren bir tespit yapmış, ancak "
    f"henüz tarhiyat yapılmamıştır.\n\n{V}, şirketin başvurabileceği idari çözüm yolu aşağıdakilerden hangisidir?",
    "Tarhiyat öncesi uzlaşma",
    ["Tarhiyat sonrası uzlaşma", "Vergi mahkemesinde iptal davası", "Düzeltme şikâyeti", "İstinaf başvurusu"],
    "Ek md. 11'e göre Maliye Bakanlığı vergi incelemesine dayanılarak tarh edilecek vergilere ilişkin kesilecek cezalarda "
    "tarhiyat öncesi uzlaşma yapılmasına izin verebilir. Henüz tarhiyat olmadığından dava ve tarhiyat sonrası uzlaşma "
    "mümkün değildir.")

P.q("VUK Ek md. 1",
    f"{V26}, usulsüzlük cezalarının uzlaşmaya konu edilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Fiil bazında toplam ceza tutarı dikkate alınır.",
    ["Tutarına bakılmaksızın tüm usulsüzlük cezaları uzlaşmaya konu edilir.",
     "Usulsüzlük cezaları tutarına bakılmaksızın uzlaşmaya konu edilmez.",
     "Her bir ceza ayrı ayrı değerlendirilir, toplam dikkate alınmaz.",
     "Sadece özel usulsüzlük cezaları uzlaşmaya konu edilir."],
    "Ek md. 1'e göre uzlaşmaya konu edilebilecek usulsüzlük ve özel usulsüzlük cezalarının tespitinde cezayı gerektiren fiil "
    "bazında kesilecek toplam ceza tutarı dikkate alınır; Kanundaki tutarı aşmayanlarda md. 376 indirimi %50 artırımlı "
    "uygulanır.", zorluk="hard")

uz = 100_000 + 40_000
P.sayisal("VUK Ek md. 1",
    "İnceleme sonucunda (TUV) A.Ş. adına 100.000 ₺ ikmalen vergi tarh edilmiş ve 100.000 ₺ vergi ziyaı cezası kesilmiştir. "
    "Kaçakçılık fiili yoktur. Tarhiyat sonrası uzlaşmada ceza 40.000 ₺ olarak uzlaşılmıştır."
    f"\n\n{V26}, şirketin ödeyeceği vergi ve ceza toplamı kaç ₺’dir?",
    tl(uz), secenekler(uz, 80_000, 200_000, 100_000, 50_000 + 40_000),
    "7524 sayılı Kanunla yapılan değişiklikten sonra uzlaşma sadece cezalara ilişkindir; vergi aslı uzlaşmaya konu olmaz. "
    "Vergi 100.000 ₺ olarak ödenir, ceza uzlaşılan tutar olan 40.000 ₺'dir: toplam 140.000 ₺.", zorluk="hard")

P.q("İYUK md. 7",
    f"{I}, vergi uyuşmazlıklarında dava açma süresinin başlangıcına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tevkifatta süre muhtasar beyan tarihinde başlar.",
    ["Tahakkuku tahsile bağlı vergilerde süre tahsilatın yapıldığı tarihi izleyen gün başlar.",
     "Tebliğ yapılan hâllerde süre tebliği izleyen gün başlar.",
     "Tescile bağlı vergilerde süre tescili izleyen gün başlar.",
     "İdarenin dava açması gereken konularda komisyon kararının idareye geldiği tarihi izleyen gün başlar."],
    "İYUK md. 7/2-b'ye göre tevkif yoluyla alınan vergilerde süre, istihkak sahiplerine ödemenin yapıldığı tarihi izleyen "
    "günden başlar.", zorluk="hard")

P.q("İYUK md. 27",
    f"Tarhiyata karşı dava açmayı düşünen bir mükellef, dava süresince vergi dairesinin tahsil işlemlerine devam edip edemeyeceğini sormaktadır.\n\n{I}, vergi davalarının tahsil işlemlerine etkisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İhtirazi kayıtlı beyana dair davalar da tahsili durdurur.",
    ["Vergi davasının açılması dava konusu bölümün tahsil işlemlerini durdurur.",
     "İşlemden kaldırılan dosyalarda tahsil işlemine devam edilir.",
     "Tahsilat işlemlerine karşı açılan davalar tahsili durdurmaz.",
     "Tahsili durdurmayan davalarda yürütmenin durdurulması istenebilir."],
    "İYUK md. 27/4'e göre vergi davasının açılması dava konusu bölümün tahsilini durdurur; ancak ihtirazi kayıtla verilen "
    "beyannameler üzerine yapılan işlemler ve tahsilat işlemleri nedeniyle açılan davalar tahsil işlemini durdurmaz, bunlar "
    "için yürütmenin durdurulması istenebilir.", zorluk="hard")

td = 500_000 - 300_000
P.sayisal("İYUK md. 27",
    "(VYZ) A.Ş. adına 500.000 ₺ vergi tarh edilmiştir. Şirket bu tarhiyatın sadece 300.000 ₺’lik kısmına karşı vergi "
    f"mahkemesinde dava açmıştır.\n\n{I}, dava süresince tahsil işlemlerine devam edilebilecek tutar kaç ₺’dir?",
    tl(td), secenekler(td, 0, 300_000, 500_000, 250_000),
    "İYUK md. 27/4'e göre vergi davasının açılması, tarh edilen vergi ve cezaların dava konusu edilen bölümünün tahsil "
    "işlemlerini durdurur; dava konusu edilmeyen 200.000 ₺ için tahsil işlemleri devam eder.")

P.q("İYUK md. 27",
    f"Bir mükellef, dava konusu ettiği bir idari işlemin uygulanmasının kendisine telafisi güç zarar vereceğini ileri sürmektedir.\n\n{I}, yürütmenin durdurulmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Telafisi güç zarar ve açık hukuka aykırılık birlikte aranır.",
    ["Dava açılması her idari işlemin yürütülmesini doğrudan durdurur.",
     "Yürütmenin durdurulması için bu iki şarttan birinin varlığı yeterlidir.",
     "Yürütmenin durdurulması kararında gerekçe gösterilmez.",
     "Yürütmenin durdurulması sadece Danıştay tarafından verilebilir."],
    "İYUK md. 27/2'ye göre idari işlemin uygulanması hâlinde telafisi güç veya imkânsız zararların doğması ve işlemin açıkça "
    "hukuka aykırı olması şartlarının birlikte gerçekleşmesi durumunda gerekçeli olarak yürütmenin durdurulmasına karar "
    "verilebilir; kural olarak dava açılması yürütmeyi durdurmaz.")

P.q("İYUK md. 37",
    "Ankara’daki bir vergi dairesi, merkezi İzmir’de olan bir şirketin Ankara şubesiyle ilgili vergi tarh etmiş ve ceza "
    f"kesmiştir.\n\n{I}, bu tarhiyata karşı açılacak davada yetkili mahkeme aşağıdakilerden hangisidir?",
    "Tarh eden dairenin yerindeki vergi mahkemesi",
    ["Şirket merkezinin bulunduğu İzmir vergi mahkemesi",
     "Mükellefin seçeceği herhangi bir vergi mahkemesi",
     "Danıştay vergi dava dairesi",
     "Ankara bölge idare mahkemesi"],
    "İYUK md. 37/a'ya göre vergi uyuşmazlıklarında yetkili mahkeme, uyuşmazlık konusu vergiyi tarh ve tahakkuk ettiren, zam "
    "ve cezaları kesen dairenin bulunduğu yerdeki vergi mahkemesidir.")

P.sayisal("İYUK md. 16",
    f"Vergi mahkemesinde görülen bir davada davalı vergi dairesinin savunması davacıya tebliğ edilmiştir.\n\n{I}, davacı "
    "tebliğ tarihinden itibaren kaç gün içinde cevap verebilir?",
    "30", ["7", "15", "45", "60"],
    "İYUK md. 16/3'e göre taraflar yapılacak tebliğlere karşı tebliğ tarihinden itibaren otuz gün içinde cevap verebilir; "
    "haklı sebeplerle bu süre bir defaya mahsus uzatılabilir.")

P.q("İYUK md. 37",
    f"Kendisine ödeme emri tebliğ edilen bir borçlu, ödeme emrine karşı hangi yer mahkemesinde dava açacağını araştırmaktadır.\n\n{I}, 6183 sayılı Kanunun uygulanmasından doğan davalarda yetkili vergi mahkemesi hangisidir?",
    "Ödeme emrini düzenleyen dairenin bulunduğu yerdeki mahkeme",
    ["Borçlunun ikametgâhının bulunduğu yerdeki mahkeme",
     "Haczedilen malın bulunduğu yerdeki mahkeme",
     "Vergi Denetim Kurulunun bulunduğu yerdeki mahkeme",
     "Borçlunun seçeceği yerdeki mahkeme"],
    "İYUK md. 37/c'ye göre Amme Alacaklarının Tahsil Usulü Kanunu'nun uygulanmasında yetkili mahkeme, ödeme emrini düzenleyen "
    "dairenin bulunduğu yerdeki vergi mahkemesidir.")

P.q("İYUK md. 3",
    f"{I}, vergi davalarında dava dilekçesinde gösterilmesi gereken bilgiler arasında aşağıdakilerden hangisi yer almaz?",
    "Davacının son beş yıla ait yıllık gelir vergisi beyan tutarları",
    ["Tarafların ve varsa vekillerinin adları ve adresleri",
     "Davanın konu ve sebepleri ile dayandığı deliller",
     "Vergi davalarında uyuşmazlık konusu miktar",
     "Verginin veya cezanın nevi ve yılı ile ihbarnamenin tarih ve numarası"],
    "İYUK md. 3/2'ye göre dilekçede tarafların kimlik ve adresleri, davanın konu ve sebepleri ile deliller, işlemin bildirim "
    "tarihi, uyuşmazlık konusu miktar ve vergi davalarında verginin veya cezanın nevi, yılı, ihbarname tarihi ve numarası "
    "gösterilir.", zorluk="easy")

P.sayisal("İYUK md. 7",
    "Adresi bilinmeyen Bay (N)’ye vergi ihbarnamesi özel kanuna göre ilan yoluyla bildirilmiştir; Vergi Usul Kanunu’nda ilan "
    f"yoluyla tebliğe ilişkin ayrıca bir süre dikkate alınmayacaktır.\n\n{I}, dava açma süresi son ilan tarihini izleyen "
    "günden itibaren kaç gün sonra işlemeye başlar?",
    "15", ["7", "10", "30", "60"],
    "İYUK md. 7/3'e göre adresleri belli olmayanlara özel kanunlarına göre ilan yoluyla bildirim yapılan hâllerde, özel "
    "kanunda aksine hüküm yoksa süre son ilan tarihini izleyen günden itibaren on beş gün sonra işlemeye başlar.",
    zorluk="hard")

P.q("İYUK md. 10",
    "Bay (T), bir vergi iadesinin yapılması için vergi dairesine başvurmuş; idare 30 gün içinde hiç cevap vermemiştir."
    f"\n\n{I}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "İstek zımnen reddedilmiş sayılır.",
    ["İstek kabul edilmiş sayılır.",
     "İdare cevap verinceye kadar dava açılamaz.",
     "Bay (T) başvurusunu yenilemekle yükümlüdür.",
     "Dava açma süresi bir yıl olarak uygulanır."],
    "İYUK md. 10/2'ye göre otuz gün içinde cevap verilmezse istek reddedilmiş sayılır; ilgililer bu sürenin bittiği tarihten "
    "itibaren dava açma süresi içinde dava açabilir.")

P.q("İYUK md. 11",
    f"Bir mükellef, dava açmadan önce işlemin geri alınması için üst makama başvurmayı düşünmektedir.\n\n{I}, üst makamlara başvurmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Geçmiş süre hesaba katılmaz, süre yeniden başlar.",
    ["Başvuru idari dava açma süresi içinde yapılmalıdır.",
     "Başvuru işlemeye başlamış olan dava açma süresini durdurur.",
     "Otuz gün içinde cevap verilmezse istek reddedilmiş sayılır.",
     "Üst makam yoksa işlemi yapan makama başvurulur."],
    "İYUK md. 11'e göre isteğin reddedilmesi veya reddedilmiş sayılması hâlinde dava açma süresi yeniden işlemeye başlar ve "
    "başvuru tarihine kadar geçmiş süre de hesaba katılır.")

P.sayisal("VUK md. 126",
    "Tarh zamanaşımı süresinin son yılı olan 2026 yılının Aralık ayında (ZAB) Ltd. Şti. adına bir vergi tarh ve tebliğ "
    f"edilmiştir. Tarhiyatta bir hesap hatası yapılmıştır.\n\n{V}, bu hatanın düzeltilebilmesi için düzeltme zamanaşımı "
    "süresi hatanın yapıldığı tarihten itibaren en az kaç yıldır?",
    "1", ["2", "3", "5", "10"],
    "Md. 126'ya göre zamanaşımı dolduktan sonra ortaya çıkan hatalar düzeltilemez; ancak zamanaşımının son yılı içinde tarh ve "
    "tebliğ edilen vergilerde düzeltme zamanaşımı hatanın yapıldığı tarihten başlayarak bir yıldan aşağı olamaz.",
    zorluk="hard")

P.q("İYUK md. 45",
    f"Vergi mahkemesinin aleyhine verdiği kararı üst yargı merciine taşımak isteyen bir mükellef, izleyeceği yolu araştırmaktadır.\n\n{I26}, istinaf yoluna ilişkin aşağıdakilerden hangisi doğrudur?",
    "İstinaf başvurusu bölge idare mahkemesine yapılır.",
    ["İstinaf başvurusu doğrudan Danıştaya yapılır.",
     "Tüm vergi davalarında tutara bakılmaksızın istinaf yolu açıktır.",
     "İstinaf süresi kararın tebliğinden itibaren yedi gündür.",
     "İstinaf başvurusu kararın icrasını doğrudan durdurur."],
    "İYUK md. 45'e göre idare ve vergi mahkemelerinin kararlarına karşı mahkemenin yargı çevresindeki bölge idare mahkemesine "
    "tebliğden itibaren otuz gün içinde istinaf başvurusu yapılabilir; Kanundaki tutarı geçmeyen davalarda kararlar kesindir.")

P.q("İYUK md. 46",
    f"Bölge idare mahkemesinin kararından memnun olmayan bir mükellef, kararı Danıştaya taşıyıp taşıyamayacağını değerlendirmektedir.\n\n{I26}, temyize ilişkin aşağıdakilerden hangisi doğrudur?",
    "Belirli kararlar otuz gün içinde Danıştayda temyiz edilir.",
    ["Tüm bölge idare mahkemesi kararları tutara bakılmaksızın temyiz edilebilir.",
     "Temyiz başvurusu bölge idare mahkemesine yapılır ve orada karara bağlanır.",
     "Temyiz süresi kararın tebliğinden itibaren altmış gündür.",
     "Vergi mahkemesi kararları doğrudan Danıştayda temyiz edilir."],
    "İYUK md. 46'ya göre Danıştay dava dairelerinin nihai kararları ile bölge idare mahkemelerinin Kanunda sayılan davalardaki "
    "(Kanundaki tutarı aşan vergi davaları dahil) kararları tebliğden itibaren otuz gün içinde Danıştayda temyiz edilebilir.",
    zorluk="hard")

u2 = 60_000 / 2
P.sayisal("VUK md. 376, Ek md. 1",
    "(ABC) Ltd. Şti. adına vergi aslına bağlı olmaksızın tek fiil nedeniyle 60.000 ₺ özel usulsüzlük cezası kesilmiştir. "
    "Şirket uzlaşma talep etmemiş, 376. madde şartlarını yerine getirmiştir. (Uzlaşma için Kanunda belirtilen tutar 40.000 ₺ "
    f"olarak alınacaktır.)\n\n{V26}, şirketin ödeyeceği ceza kaç ₺’dir?",
    tl(u2), secenekler(u2, 15_000, 60_000, 20_000, 45_000),
    "Ceza Kanundaki tutarı aştığından uzlaşmaya konu edilebilir ve %50 artırımlı indirim uygulanmaz; md. 376'ya göre cezanın "
    "yarısı indirilir: 60.000 / 2 = 30.000 ₺.", zorluk="hard")

P.q("İYUK md. 17",
    f"Vergi mahkemesinde görülen bir davada taraflar, dosyanın duruşmalı görülmesini isteyip isteyemeyeceklerini değerlendirmektedir.\n\n{I}, idari yargıda duruşmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mahkeme istem olmasa da resen duruşma kararı verebilir.",
    ["Vergi davalarında duruşma yapılması şarttır.",
     "Duruşma talebi sadece karar aşamasında yapılabilir.",
     "Temyizde duruşma talebi kural gereği kabul edilmez.",
     "Duruşma davetiyesi duruşmadan bir gün önce gönderilir."],
    "İYUK md. 17'ye göre Kanundaki tutarları aşan davalarda taraflardan birinin isteği üzerine duruşma yapılır; bu kayıtlara "
    "bağlı olmaksızın Danıştay, mahkeme ve hâkim duruşma yapılmasına resen karar verebilir; davetiyeler en az otuz gün önce "
    "gönderilir.")

P.oncul("VUK Ek md. 1, 11",
    f"{V26} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Tarhiyat sonrası uzlaşma vergi ziyaı cezalarını kapsar.",
     "Vergi aslı tarhiyat sonrası uzlaşmaya konu edilebilir.",
     "Uzlaşma talebi ihbarnamenin tebliğinden itibaren otuz gün içinde yapılır.",
     "Tarhiyat öncesi uzlaşmada anlaşılamazsa ceza kesildikten sonra yeniden uzlaşma istenebilir."],
    "Yukarıdakilerden hangileri doğrudur?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Ek md. 1'e göre uzlaşma vergi ziyaı cezalarını kapsar (I) ve talep otuz gün içinde yapılır (III); 7524 sayılı Kanunla "
    "vergi aslı uzlaşma dışına çıkarılmıştır (II yanlış). Ek md. 11'e göre tarhiyat öncesi uzlaşma sağlanamazsa sonradan "
    "uzlaşma talep edilemez (IV yanlış).", zorluk="hard")

P.sayisal("İYUK md. 7-8",
    "(DEF) A.Ş.’ye vergi ve ceza ihbarnamesi 5 Mayıs 2026’da tebliğ edilmiştir. Şirket uzlaşma talep etmeyecektir; sürenin "
    f"son günü resmî tatile rastlamamaktadır.\n\n{I}, şirket en geç Haziran 2026’nın kaçıncı günü vergi mahkemesinde dava "
    "açmalıdır?",
    "4", ["3", "5", "6", "15"],
    "İYUK md. 7'ye göre vergi mahkemesinde dava açma süresi otuz gündür ve tebliği izleyen günden başlar: 6 Mayıs'tan itibaren "
    "otuzuncu gün 4 Haziran'dır.", zorluk="hard")

P.q("VUK md. 121",
    "Vergi dairesi, mükellef (VYZ) A.Ş.’nin beyannamesinde vergi nispetinin açıkça yanlış uygulandığını fark etmiş ve "
    f"şirket aleyhine düzeltme yapmıştır.\n\n{V}, şirketin bu düzeltmeye karşı hakkı nedir?",
    "Düzeltmeye karşı vergi mahkemesinde dava açabilir.",
    ["Düzeltmeye karşı herhangi bir yola başvuramaz.",
     "Sadece uzlaşma yoluna başvurabilir.",
     "Sadece Cumhurbaşkanlığına şikâyette bulunabilir.",
     "Düzeltme, şirket kabul etmedikçe uygulanmaz."],
    "Md. 121'e göre idarece tereddüt edilmeyen açık ve mutlak vergi hataları resen düzeltilir; kendi aleyhlerine düzeltme "
    "yapılanların düzeltmeye karşı vergi mahkemesinde dava açma hakları saklıdır.")

P.q("VUK md. 117",
    f"Bir mükellef, aynı döneme ait gelir vergisinin aynı matrah üzerinden iki kez tahakkuk ettirildiğini fark etmiştir.\n\n{V}, verginin mükerrer olması aşağıdakilerden hangisini ifade eder?",
    "Aynı matrahtan birden fazla vergi alınması",
    ["Verginin yanlış kişiden alınması",
     "Vergi nispetinin yanlış uygulanması",
     "Vergilendirme döneminin yanlış gösterilmesi",
     "Muaf kişiden vergi istenmesi"],
    "Md. 117/3'e göre verginin mükerrer olması, aynı vergi kanununun uygulanmasında belli bir vergilendirme dönemi için aynı "
    "matrah üzerinden bir defadan fazla vergi istenmesi veya alınmasıdır.")

P.sayisal("İYUK md. 10",
    "Bay (K), 2 Mart 2026’da vergi dairesine bir iade talebiyle başvurmuş, idare hiç cevap vermemiştir."
    f"\n\n{I}, Bay (K)’nın isteği Nisan 2026’nın kaçıncı günü reddedilmiş sayılır?",
    "1", ["2", "3", "15", "30"],
    "İYUK md. 10/2'ye göre otuz gün içinde cevap verilmezse istek reddedilmiş sayılır: 2 Mart'tan itibaren otuzuncu gün 1 "
    "Nisan'dır.", zorluk="hard")

P.q("VUK Ek md. 1",
    "(JKL) A.Ş. uzlaşma görüşmesine katılacaktır. Şirket yetkilileri görüşmede kendilerine kimlerin eşlik edebileceğini "
    f"sormaktadır.\n\n{V}, uzlaşma görüşmelerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mükellef bir meslek mensubu bulundurabilir.",
    ["Görüşmelere sadece şirket ortakları katılabilir.",
     "Görüşmelerde avukat bulundurulması zorunludur.".replace(" zorunludur", " şarttır"),
     "Görüşmelere vergi mahkemesi hâkimi katılır.",
     "Görüşmeler sadece yazılı olarak yürütülür."],
    "Ek md. 1'e göre mükellef uzlaşma görüşmelerinde bağlı olduğu meslek odasından bir temsilci ve 3568 sayılı Kanuna göre "
    "kurulan meslek odasından bir meslek mensubu bulundurabilir.")

P.q("İYUK md. 7",
    "Bir bakanlık, vergi uygulamasına ilişkin düzenleyici bir işlemi Resmî Gazete’de ilan etmiştir. Bir mükellef bu "
    f"düzenlemeye karşı dava açmak istemektedir.\n\n{I}, dava açma süresi ne zaman başlar?",
    "İlan tarihini izleyen günden",
    ["Mükellefe yazılı bildirim yapıldığı günden",
     "Düzenlemenin mükellefe uygulandığı günden",
     "Düzenlemenin yürürlüğe girdiği yılın sonundan",
     "Mükellefin durumu öğrendiği günden"],
    "İYUK md. 7/4'e göre ilanı gereken düzenleyici işlemlerde dava süresi ilan tarihini izleyen günden başlar; ilgililer "
    "düzenleyici işlemin uygulanması üzerine düzenleyici işlem veya uygulama işlemi ya da her ikisine birden dava açabilir.")

ik = 300_000
P.sayisal("İYUK md. 27",
    "(GHI) A.Ş., bir işleme ilişkin tereddüdü nedeniyle KDV beyannamesini ihtirazi kayıtla vermiş; beyan edilen 300.000 ₺ "
    f"vergi tahakkuk etmiştir. Şirket bu tahakkuka karşı dava açmıştır.\n\n{I}, dava süresince tahsil işlemlerine devam "
    "edilebilecek tutar kaç ₺’dir?",
    tl(ik), secenekler(ik, 0, 150_000, 100_000, 30_000),
    "İYUK md. 27/4'e göre ihtirazi kayıtla verilen beyannameler üzerine yapılan işlemlerden dolayı açılan davalar tahsil "
    "işlemini durdurmaz; tutarın tamamı tahsil edilebilir, ancak yürütmenin durdurulması istenebilir.", zorluk="hard")

P.q("İYUK md. 11",
    f"Kendisine tebliğ edilen işleme karşı dava açmadan önce üst makama başvuran bir mükellef, bu başvurunun sürelere etkisini sormaktadır.\n\n{I}, dava açılmadan önce üst makama başvurmanın dava açma süresine etkisi nedir?",
    "İşlemeye başlamış süreyi durdurur.",
    ["Süreyi kesmez, süre işlemeye devam eder.",
     "Süreyi baştan ve yeniden başlatır.",
     "Süreyi iki katına çıkarır.",
     "Dava açma hakkını ortadan kaldırır."],
    "İYUK md. 11/1'e göre idari dava açılmadan önce üst makama başvuru, işlemeye başlamış olan idari dava açma süresini "
    "durdurur; ret hâlinde süre kaldığı yerden işler.")

P.q("VUK md. 118",
    "Vergi dairesi, Bay (M)’nin 2025 yılına ait vergisini ihbarnamede yanlışlıkla 2024 yılına aitmiş gibi göstermiştir."
    f"\n\n{V}, bu hata hangi türdedir?",
    "Vergilendirme döneminde hata",
    ["Mevzuda hata", "Mükellefiyette hata", "Matrah hatası", "Mükellefin şahsında hata"],
    "Md. 118/4'e göre aranan verginin ilgili bulunduğu vergilendirme döneminin yanlış gösterilmesi veya süre itibarıyla eksik "
    "ya da fazla hesaplanması vergilendirme veya muafiyet döneminde hatadır.")

P.sayisal("İYUK md. 45",
    "Bölge idare mahkemesi, 48. maddenin yedinci fıkrası uyarınca bir karar vermiş ve karar 3 Haziran 2026’da taraflara "
    f"tebliğ edilmiştir.\n\n{I26}, bu karara karşı temyiz yoluna tebliğ tarihini izleyen günden itibaren kaç gün içinde "
    "başvurulabilir?",
    "7", ["10", "15", "30", "60"],
    "İYUK md. 45/2'ye 7524 sayılı Kanunla eklenen cümleye göre bölge idare mahkemesinin md. 48/7 uyarınca verdiği kararlara "
    "karşı tebliğ tarihini izleyen günden itibaren yedi gün içinde temyiz yoluna başvurulabilir.", zorluk="hard")

P.q("İYUK md. 27",
    f"Bir mükellef, hakkındaki bir idari işleme karşı dava açarsa işlemin uygulanmasının duracağını düşünmektedir.\n\n{I}, idari işlemlere karşı dava açılmasının işlemin yürütülmesine etkisi kural olarak nedir?",
    "İşlemin yürütülmesini durdurmaz.",
    ["İşlemin yürütülmesini her durumda durdurur.".replace("her durumda ", "doğrudan "),
     "İşlemi geçersiz kılar.",
     "İşlemin yürütülmesini altı ay süreyle durdurur.",
     "İşlemi idarenin onayına bağlar."],
    "İYUK md. 27/1'e göre Danıştay veya idari mahkemelerde dava açılması dava edilen idari işlemin yürütülmesini durdurmaz; "
    "vergi davalarında ise md. 27/4 gereği dava konusu kısmın tahsili durur.")

P.sayisal("İYUK md. 10",
    "Bayan (L)’nin başvurusuna idare 30 gün içinde cevap vermemiş, Bayan (L) de dava açmamıştır. İdare daha sonra ret "
    f"cevabı vermiş ve bu cevap Bayan (L)’ye tebliğ edilmiştir.\n\n{I}, Bayan (L) cevabın tebliğinden itibaren kaç gün "
    "içinde dava açabilir?",
    "60", ["15", "30", "45", "90"],
    "İYUK md. 10/2'ye göre dava açılmaması hâllerinde otuz günlük sürenin bitmesinden sonra yetkili idari makamlarca cevap "
    "verilirse, cevabın tebliğinden itibaren altmış gün içinde dava açılabilir.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
