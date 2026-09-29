# -*- coding: utf-8 -*-
"""Vergi · Gelir Vergisi · Gelir Unsurları — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında gelir unsurları; hangi kazancın hangi unsura girdiği, istisnalar (telif, ticari
plaka, kâr payı), değer artışı ve arızi kazanç, binek otomobil gider kısıtlaması üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 193 sayılı GVK md. 1-9, 18, 23, 37-42, 52, 61, 65-68,
70-76, mük. 80, 81, mük. 81, 82. Yıla bağlı tutarlar soru kökünde verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_gelir_unsurlari_2026.json", lesson="gelir_vergisi", topic="gelir_unsurlari",
          konu_adi="Gelir Unsurları", seed=2026092902,
          surum="193 sayılı GVK güncel metni; 2025 tutarları kökte; 29.09.2026 kontrolü")

K = "193 sayılı Gelir Vergisi Kanunu’na göre"
K26 = "193 sayılı Gelir Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

# ================================================================ gelir kavramı ve mükellefiyet
P.q("GVK md. 2",
    f"{K}, aşağıdakilerden hangisi gelire giren kazanç ve iratlardan biri değildir?",
    "Miras yoluyla intikal eden bir dairenin değeri",
    ["Zirai faaliyetten elde edilen kazançlar", "Serbest meslek faaliyetinden doğan kazançlar", "Nakdi sermayeden elde edilen menkul sermaye iratları", "Diğer kazanç ve iratlar"],
    "Md. 2'ye göre gelire giren kazanç ve iratlar ticari, zirai ve serbest meslek kazançları, ücretler, gayrimenkul ve menkul "
    "sermaye iratları ile diğer kazanç ve iratlardır. Miras yoluyla intikaller 7338 sayılı Veraset ve İntikal Vergisinin "
    "konusudur.", zorluk="easy")

P.q("GVK md. 4-5",
    "İngiliz vatandaşı Bay (A), 2025 yılında bir üniversitede bir dönemlik araştırma projesi için belli ve geçici görevle "
    f"Türkiye'ye gelmiş ve Türkiye'de 8 ay kalmıştır.\n\n{K}, Bay (A)’nın vergilendirilmesine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Belli ve geçici görevle geldiğinden altı aydan fazla kalsa da Türkiye’de yerleşmiş sayılmaz.",
    ["Altı aydan fazla kaldığı için tam mükellef olur ve dünya genelindeki geliri vergilendirilir.",
     "Sadece yabancı uyruklu olduğu için dar mükellef sayılır.",
     "Türkiye’de altı aydan fazla kalan her yabancı Türkiye’de yerleşmiş sayılır.",
     "Türkiye’de elde ettiği gelir dahil gelirlerinin tamamı vergi dışı kalır."],
    "Md. 4'e göre bir takvim yılında altı aydan fazla oturanlar Türkiye'de yerleşmiş sayılır; ancak md. 5'e göre belli ve "
    "geçici görev veya iş için gelen ilim ve fen adamları, uzmanlar ile tahsil, tedavi veya seyahat amacıyla gelenler altı "
    "aydan fazla kalsalar da yerleşmiş sayılmaz. Bu kişi dar mükellef olarak Türkiye'de elde ettiği gelir üzerinden "
    "vergilendirilir (md. 6).", zorluk="hard")

P.q("GVK md. 3",
    f"{K}, aşağıdakilerden hangisi tam mükellef olarak Türkiye içinde ve dışında elde ettikleri kazanç ve iratların "
    "tamamı üzerinden vergilendirilenler arasında yer almaz?",
    "Türkiye’de altı aydan fazla tedavi amacıyla kalan yabancı uyruklu kişi",
    ["İkametgâhı Türkiye’de bulunan Türk vatandaşı",
     "Bir takvim yılı içinde Türkiye’de devamlı olarak altı aydan fazla oturan yabancı iş insanı",
     "Resmi daire adına yabancı ülkede oturan ve orada gelir vergisine tabi tutulmayan Türk vatandaşı",
     "Türkiye’de yerleşik olup yurt dışına geçici olarak ayrılan kişi"],
    "Md. 3'e göre Türkiye'de yerleşmiş olanlar ile resmi daire ve müesseseler adına yabancı memleketlerde oturan ve orada "
    "vergilendirilmeyen Türk vatandaşları tam mükelleftir; md. 4'e göre geçici ayrılmalar oturma süresini kesmez. Md. 5'e "
    "göre tedavi amacıyla gelen yabancılar altı aydan fazla kalsalar da yerleşmiş sayılmaz.")

P.q("GVK md. 7",
    "Almanya'da yerleşik dar mükellef Bayan (B), Türkiye'deki bir anonim şirketin yönetim kurulu üyesi olarak 2025 yılında "
    f"huzur hakkı almıştır; toplantılara çevrim içi olarak Almanya'dan katılmıştır.\n\n{K}, bu ücretin Türkiye'de elde "
    "edilip edilmediğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Türkiye’de kâin müesseselerin idare meclisi üyelerine ait huzur hakları Türkiye’de elde edilmiş sayılır.",
    ["Hizmet Türkiye’de fiilen ifa edilmediğinden huzur hakkı Türkiye’de elde edilmiş sayılmaz.",
     "Huzur hakkı ücret değil serbest meslek kazancı olduğundan Türkiye’de vergilendirilmez.",
     "Dar mükelleflerin huzur hakları sadece ödeme Türkiye’de yapılırsa vergilendirilir.",
     "Huzur hakkı ancak Almanya ile çifte vergilendirmeyi önleme anlaşması yoksa Türkiye’de vergilendirilebilir."],
    "Md. 7/3-b'ye göre dar mükellefler bakımından Türkiye'de kâin müesseselerin idare meclisi başkan ve üyelerine, "
    "denetçilere ve tasfiye memurlarına ait huzur hakkı ve benzeri ödemeler Türkiye'de elde edilmiş sayılır; hizmetin ifa "
    "yeri ayrıca aranmaz.", zorluk="hard")

P.q("GVK md. 9",
    f"{K}, esnaf muaflığından yararlanabilecekler arasında aşağıdakilerden hangisi yer almaz?",
    "Kamyonetle köy köy dolaşarak giyim eşyası satan kişi",
    ["Bir iş yeri açmaksızın gezici olarak ve doğrudan tüketiciye iş yapan ayakkabı tamircisi",
     "Evinde dışarıdan işçi almadan ürettiği el örgüsü ürünleri kanundaki sınırla internetten satan kişi",
     "Bir adet hayvan arabasıyla nakliyecilik yapan kişi",
     "Denizde toplamı 50 rüsum tonilatoyu aşmayan motorsuz nakil vasıtası işleten kişi"],
    "Md. 9'a göre motorlu nakil vasıtası kullanmamak şartıyla gezici perakende ticaret yapanlar muaftır; ancak giyim eşyası "
    "satanlar bu kapsamdan hariçtir ve motorlu araç kullanımı muafiyeti engeller. Gezici küçük sanat erbabı, evde üretilen "
    "ürünleri sınır içinde internetten satanlar ve hayvan arabasıyla nakliyecilik yapanlar muaftır.")

# ================================================================ ticari kazanç
tk = 3_000_000 + 400_000 - 300_000 - 2_000_000 - 500_000
P.sayisal("GVK md. 39",
    "İşletme hesabı esasına göre defter tutan tüccar Bay (C)’nin 2025 yılı verileri şöyledir: satış hasılatı 3.000.000 ₺, "
    "mal alışları 2.000.000 ₺, diğer giderler 500.000 ₺, dönem başı emtia mevcudu 300.000 ₺, dönem sonu emtia mevcudu "
    f"400.000 ₺.\n\n{K}, Bay (C)’nin 2025 yılı ticari kazancı kaç ₺’dir?",
    tl(tk), secenekler(tk, 500_000, 700_000, 400_000, 1_000_000, 300_000),
    "Md. 39'a göre işletme hesabında kazanç, hasılat ile giderler arasındaki müspet farktır; dönem sonu emtia mevcudu "
    "hasılata, dönem başı mevcudu giderlere eklenir: (3.000.000 + 400.000) − (2.000.000 + 500.000 + 300.000) = 600.000 ₺.")

isl = (2_400_000 + 250_000) - (1_500_000 + 200_000 + 320_000 + 80_000)
P.sayisal("GVK md. 39",
    "İşletme hesabına göre defter tutan Bayan (R)’nin 2025 yılı verileri: satışlar 2.400.000 ₺, mal alışları 1.500.000 ₺, "
    "dönem başı emtia 200.000 ₺, dönem sonu emtia 250.000 ₺, işyeri kirası ve diğer giderler 320.000 ₺, VUK’a göre ayrılan "
    f"amortisman 80.000 ₺.\n\n{K}, Bayan (R)’nin 2025 yılı ticari kazancı kaç ₺’dir?",
    tl(isl), secenekler(isl, isl + 80_000, isl - 50_000, isl + 50_000, isl + 500_000),
    "Md. 39'a göre işletme hesabında kazanç hasılat ile giderler arasındaki farktır; dönem sonu emtia hasılata, dönem başı "
    "emtia giderlere eklenir ve amortismanlar da indirilir: (2.400.000 + 250.000) − (1.500.000 + 200.000 + 320.000 + "
    "80.000) = 550.000 ₺.")

gider = 300_000 + 60_000 + 40_000
kkeg = gider * 0.30 + 15_000
P.sayisal("GVK md. 40/5, 41",
    "Tüccar Bayan (D) 2025 yılında işletmesine kayıtlı ve işte kullandığı binek otomobili için 300.000 ₺ akaryakıt, 60.000 ₺ "
    "bakım-onarım ve 40.000 ₺ kasko sigortası gideri ile 15.000 ₺ motorlu taşıtlar vergisi ödemiş ve tamamını gider yazmıştır. "
    f"Faaliyeti binek otomobil kiralama değildir.\n\n{K26}, bu harcamalardan kanunen kabul edilmeyen gider olarak dikkate "
    "alınacak tutar kaç ₺’dir?",
    tl(kkeg), secenekler(kkeg, gider * 0.30, (gider + 15_000) * 0.30, 15_000, gider * 0.70, (gider + 15_000) * 0.70),
    "Md. 40/5'e göre binek otomobillerine ilişkin giderlerin en fazla %70'i indirilebilir; akaryakıt, bakım ve sigorta "
    "toplamı 400.000 ₺'nin %30'u (120.000 ₺) gider yazılamaz. Binek otomobiller için ödenen motorlu taşıtlar vergisi md. 41 "
    "gereği tamamen indirilemeyen giderdir: 120.000 + 15.000 = 135.000 ₺.", zorluk="hard")

P.q("GVK md. 40",
    f"{K}, ticari kazancın tespitinde indirilecek giderler arasında aşağıdakilerden hangisi yer almaz?",
    "İşletme sahibinin kendisine ödediği aylık ücret",
    ["Ticari kazancın elde edilmesi ve idame ettirilmesi için yapılan genel giderler",
     "İşle ilgili olmak şartıyla ödenen zarar, ziyan ve tazminatlar",
     "İşletme ile ilgili bina, gider ve damga vergileri gibi ayni vergi, resim ve harçlar",
     "Vergi Usul Kanunu hükümlerine göre ayrılan amortismanlar"],
    "Md. 40 genel giderleri, işle ilgili tazminatları, ayni vergi, resim ve harçları ve amortismanları indirilecek giderler "
    "arasında sayar. Md. 41'e göre teşebbüs sahibinin kendisine, eşine ve küçük çocuklarına işletmeden ödenen aylıklar, "
    "ücretler ve kâr payları gider yazılamaz.", zorluk="easy")

P.q("GVK md. 41",
    f"{K}, aşağıdakilerden hangisi ticari kazancın tespitinde gider olarak indirilemeyecek unsurlardan biri değildir?",
    "İşletmede çalışan işçilere ödenen ücretler",
    ["Teşebbüs sahibinin işletmeye koyduğu sermaye için yürütülen faiz",
     "Teşebbüs sahibinin eşine işletmeden ödenen ücretler",
     "Her türlü para cezaları ve vergi cezaları",
     "Teşebbüs sahibinin küçük çocuklarına ödenen kâr payları"],
    "Md. 41'e göre teşebbüs sahibinin işletmeye koyduğu sermaye için faiz, kendisine, eşine ve küçük çocuklarına ödenen "
    "aylık, ücret, prim, ikramiye ve kâr payları ile para ve vergi cezaları gider yazılamaz. İşçilere ödenen ücretler "
    "md. 40/1 kapsamında gider yazılabilir.", zorluk="easy")

P.q("GVK md. 42",
    "Müteahhit Bay (E) Ağustos 2024'te bir alışveriş merkezi inşaatına başlamış, inşaat Mart 2026'da bitmiş ve geçici kabul "
    f"yapılmıştır.\n\n{K}, bu yıllara yaygın inşaat işinden doğan kazancın vergilendirilmesine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Kazanç işin bittiği 2026 yılında tespit edilir ve o yılın beyannamesiyle beyan edilir.",
    ["Kazanç her yıl yapılan iş oranında ayrı ayrı tespit edilip beyan edilir.",
     "Kazanç işe başlanılan 2024 yılında tahmini olarak beyan edilir, fark işin bittiği yıl düzeltilir.",
     "Kazanç geçici vergi dönemleri itibarıyla kümülatif olarak vergilendirilir.",
     "İnşaat birden fazla yıla yaydığı için arızi kazanç olarak vergilendirilir."],
    "Md. 42'ye göre birden fazla takvim yılına yaygın inşaat ve onarma işlerinde kazanç, işin bittiği yılda kesin olarak "
    "tespit edilir ve o yılın geliri olarak beyan edilir; mük. 120'ye göre bu kazançlar geçici vergi matrahına dahil "
    "edilmez.")

P.q("GVK md. 37",
    "Bir vergi dairesi, 2025 yılı yıllık beyannamelerini incelerken mükelleflerin bildirdiği gelirlerin doğru gelir "
    "unsuruna yazılıp yazılmadığını kontrol etmekte; özellikle gayrimenkul, maden ve işletme satışlarından doğan "
    f"kazançları ayrıca değerlendirmektedir.\n\n{K}, aşağıdakilerden hangisi ticari kazanç sayılmaz?",
    "Emekli bir öğretmenin konut olarak kiraya verdiği dairesinden aldığı kira",
    ["Satın alınan gayrimenkullerin alım satımıyla devamlı uğraşan kişinin kazancı",
     "Maden, taş ve kum ocakları işletilmesinden elde edilen kazanç",
     "Gayrimenkulleri kiraya verme işiyle devamlı uğraşanların kazancı",
     "Faaliyetine devam eden bir işletmenin satılmasından doğan kazanç"],
    "Md. 37'ye göre her türlü ticari ve sınai faaliyetten doğan kazançlar ile gayrimenkul alım satımı ve kiralama işleriyle "
    "devamlı uğraşanların kazançları, maden ve taş ocakları işletme kazançları ticari kazançtır; mük. 80'e göre faaliyetine "
    "devam eden işletmenin satışından doğan kazanç da ticari kazanç sayılır. Tek konutun kiralanması gayrimenkul sermaye "
    "iradıdır.")

# ================================================================ zirai kazanç, ücret
P.q("GVK md. 61",
    "Bir mali müşavir, müşterisi olan bir anonim şirketin 2025 yılında yaptığı ödemeleri gelir unsurlarına göre "
    "sınıflandırmaktadır. Ödemeler arasında çalışanlara, yönetim kurulu üyelerine, emeklilere ve şirkete dışarıdan "
    f"bağımsız hizmet veren kişilere yapılan ödemeler bulunmaktadır.\n\n{K}, aşağıdakilerden hangisi ücret sayılmaz?",
    "Bir avukatın müvekkilinden aldığı vekâlet ücreti",
    ["İşverene tabi ve belirli bir iş yerine bağlı çalışan kişiye hizmet karşılığı ödenen para",
     "Hizmet erbabına verilen ayni menfaatler",
     "Anonim şirket yönetim kurulu üyelerine ödenen huzur hakları",
     "Emekli, dul ve yetimlere bağlanan aylıklar"],
    "Md. 61'e göre ücret, işverene tabi ve belirli bir işyerine bağlı olarak çalışanlara hizmet karşılığı verilen para ve "
    "ayınlarla sağlanan menfaatlerdir; huzur hakları ile emekli, dul ve yetim aylıkları ücret sayılan ödemeler arasındadır "
    "(emekli aylıkları ayrıca md. 23 ile istisnadır). Avukatın vekâlet ücreti serbest meslek kazancıdır.")

P.q("GVK md. 23",
    f"{K26}, aşağıdakilerden hangisi gelir vergisinden istisna edilen ücretler arasında yer almaz?",
    "Anonim şirket yönetim kurulu üyelerine ödenen huzur hakları",
    ["Emekli, malullük, dul ve yetim aylıkları",
     "Hizmet erbabının asgari ücrete isabet eden kısım için kanunda düzenlenen istisna tutarı",
     "Kanunda belirtilen şartlarla işverence hizmet erbabına iş yerinde verilen yemek",
     "Köy muhtarlarına ödenen ücretler"],
    "Md. 23'e göre emekli, dul ve yetim aylıkları, asgari ücrete isabet eden kısım, belirli şartlarla verilen yemek ve köy "
    "muhtarlarına ödenen ücretler istisnadır. Huzur hakları ücret sayılır ve istisna değildir (2026/2 kitapçığındaki "
    "örnekte olduğu gibi).")

ym = (380 - 300) * 22
P.sayisal("GVK md. 23/8",
    "Bir anonim şirkette çalışan Bayan (P)’ye, işyerinde yemek verilmediği için 2026 Mart ayında çalıştığı 22 gün için "
    "günlük 380 ₺ tutarında yemek bedeli ödenmiştir. (2026 yılı için günlük yemek bedeli istisna tutarı 300 ₺’dir.)"
    f"\n\n{K26}, bu ödemenin ücret olarak vergilendirilecek kısmı kaç ₺’dir?",
    tl(ym), secenekler(ym, 380 * 22, 300 * 22, 80, 380 * 22 - 300),
    "Md. 23/8'e göre işyerinde yemek verilmeyen durumlarda çalışılan günlere ait günlük yemek bedelinin kanundaki tutarı "
    "aşmayan kısmı istisnadır; aşan kısım ücrettir: (380 − 300) × 22 = 1.760 ₺.")

P.q("GVK md. 64",
    "Bay (F), 2025 yılında tek bir anonim şirketten yönetim kurulu üyeliği huzur hakkı almıştır. Ödemeler üzerinden "
    f"tevkifat yapılmıştır.\n\n{K}, bu gelirin niteliğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Huzur hakkı ücret sayılır ve ücret hükümlerine göre vergilendirilir.",
    ["Huzur hakkı ticari kazanç sayılır ve bilanço esasına göre vergilendirilir.",
     "Huzur hakkı menkul sermaye iradı olduğundan yarısı istisnadır.",
     "Huzur hakkı arızi kazanç sayılır ve istisna tutarı kadarı vergi dışı kalır.",
     "Huzur hakkı serbest meslek kazancı sayılır ve geçici vergiye tabidir."],
    "Md. 61'e göre ücret sayılan ödemeler arasında yönetim kurulu üyelerine ödenen huzur hakları da yer alır; bu ödemeler "
    "ücret hükümlerine göre tevkifata ve beyan kurallarına (md. 86/1-b) tabidir.")

# ================================================================ serbest meslek
sm = 2_000_000 - 240_000 - 360_000 - 100_000 * 0.70
P.sayisal("GVK md. 67-68",
    "Mali müşavir Bayan (G)’nin 2025 yılında tahsil ettiği serbest meslek hasılatı 2.000.000 ₺’dir. Aynı yıl ödediği ve "
    "belgelendirdiği giderler şunlardır: büro kirası 240.000 ₺, personel ücretleri 360.000 ₺, mesleğinde kullandığı binek "
    f"otomobilin akaryakıt ve bakım giderleri 100.000 ₺.\n\n{K26}, Bayan (G)’nin 2025 yılı serbest meslek kazancı kaç "
    "₺’dir?",
    tl(sm), secenekler(sm, 2_000_000 - 700_000, 2_000_000 - 600_000, 2_000_000 - 600_000 - 30_000, 2_000_000 - 360_000 - 70_000),
    "Md. 67'ye göre serbest meslek kazancı tahsil edilen hasılattan giderlerin indirilmesiyle bulunur. Md. 68/5'e göre "
    "binek otomobil giderlerinin en fazla %70'i (70.000 ₺) indirilebilir: 2.000.000 − 240.000 − 360.000 − 70.000 = "
    "1.330.000 ₺.")

P.q("GVK md. 65",
    f"{K}, serbest meslek faaliyetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Serbest meslek faaliyeti bir işverene tabi olarak ve onun hesabına yürütülen faaliyettir.",
    ["Sermayeden ziyade şahsi mesaiye, ilmi veya mesleki bilgiye dayanır.",
     "Faaliyet ticari mahiyette olmayan işlerin şahsi sorumluluk altında kendi nam ve hesabına yapılmasıdır.",
     "Bu faaliyeti mutat meslek hâlinde ifa edenler serbest meslek erbabıdır.",
     "Serbest meslek kazancı serbest meslek faaliyetinden doğan kazançtır."],
    "Md. 65'e göre serbest meslek faaliyeti, sermayeden ziyade şahsi mesaiye, ilmi veya mesleki bilgiye veya ihtisasa "
    "dayanan ve ticari mahiyette olmayan işlerin işverene tabi olmaksızın şahsi sorumluluk altında kendi nam ve hesabına "
    "yapılmasıdır.")

P.q("GVK md. 70, 18",
    "Bestekâr Bay (H), bestelediği şarkıların kullanım hakkını bir yapım şirketine kiralamış, ayrıca başka bir besteciden "
    f"satın aldığı bir eserin kullanım hakkını da aynı yıl kiraya vermiştir.\n\n{K}, bu iki gelirin niteliğine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Kendi eserinin kirası serbest meslek kazancı, satın aldığınınki gayrimenkul sermaye iradıdır.",
    ["Her iki gelir de gayrimenkul sermaye iradıdır.",
     "Her iki gelir de serbest meslek kazancıdır.",
     "Kendi eserinin kiralanması gayrimenkul sermaye iradı, satın aldığı eserin kiralanması ticari kazançtır.",
     "Her iki gelir de menkul sermaye iradıdır ve yarısı istisnadır."],
    "Md. 70/6'ya göre telif haklarının kiraya verilmesi gayrimenkul sermaye iradıdır; ancak bu hakların müellifleri veya "
    "kanuni mirasçıları tarafından kiralanmasından doğan kazançlar serbest meslek kazancıdır. Müellifin kazancı md. 18 "
    "istisnasının da konusu olabilir.", zorluk="hard")

# ================================================================ gayrimenkul sermaye iradı
ek = 2_000_000 * 0.05
P.sayisal("GVK md. 73",
    "Bay (K), sahibi olduğu ve emlak vergi değeri 2.000.000 ₺ olan bir konutu 2025 yılı boyunca iş ortağının kullanımına "
    "bedelsiz olarak bırakmıştır. Konutun yetkili mercilerce takdir edilmiş bir kirası yoktur; durum emsal kira bedeli "
    f"uygulanmayan hâllerden biri değildir.\n\n{K}, Bay (K) açısından 2025 yılı için dikkate alınacak emsal kira bedeli "
    "kaç ₺’dir?",
    tl(ek), secenekler(ek, 200_000, 50_000, 2_000_000 * 0.15, 20_000, 2_000_000 * 0.08),
    "Md. 73'e göre bedelsiz olarak başkalarının intifaına bırakılan mal ve hakların emsal kira bedeli kira sayılır; bina ve "
    "arazide emsal kira bedeli, takdir edilmiş kira yoksa VUK'a göre belirlenen vergi değerinin %5'idir: 2.000.000 × %5 = "
    "100.000 ₺.")

gms = (480_000 - 60_000 - 40_000)
P.sayisal("GVK md. 74",
    "Bay (S), işyeri olarak kiraya verdiği dükkândan 2025 yılında brüt 480.000 ₺ kira tahsil etmiştir. Dükkân için aynı "
    "yıl 60.000 ₺ onarım gideri yapmış, ayrıca VUK’a göre 40.000 ₺ amortisman hesaplanmıştır. Gerçek gider yöntemini "
    f"seçmiştir; başka kira geliri yoktur.\n\n{K}, Bay (S)’nin 2025 yılı safi gayrimenkul sermaye iradı kaç ₺’dir?",
    tl(gms), secenekler(gms, 480_000 * 0.85, 480_000 - 60_000, 480_000 - 40_000, 480_000 * 0.85 - 60_000),
    "Md. 74'e göre gerçek gider yönteminde onarım giderleri ve amortismanlar hasılattan indirilir: 480.000 − 60.000 − "
    "40.000 = 380.000 ₺. İşyeri kirasına md. 21'deki konut istisnası uygulanmaz.")

P.q("GVK md. 73",
    f"{K}, aşağıdakilerden hangisi emsal kira bedeli esasının uygulanmadığı hâllerden biri değildir?",
    "Bir konutun arkadaşa bedelsiz olarak kullandırılması",
    ["Boş kalan gayrimenkullerin muhafazası amacıyla bedelsiz olarak başkalarının ikametine bırakılması",
     "Mal sahibi ile birlikte akrabalarının da aynı evde veya dairede ikamet etmesi",
     "Binaların mal sahibinin usul, füru veya kardeşlerinin ikametine tahsis edilmesi",
     "Genel bütçeli daireler, il özel idareleri ve belediyelerce yapılan kiralamalar"],
    "Md. 73'e göre boş kalan gayrimenkulün muhafaza amacıyla bedelsiz başkasının ikametine bırakılması, binanın usul, "
    "füru veya kardeşlerin ikametine tahsisi, mal sahibiyle akrabaların aynı evde oturması ve kamu idarelerince yapılan "
    "kiralamalarda emsal kira bedeli uygulanmaz; arkadaşa bedelsiz kullandırma bunlardan değildir.")

P.q("GVK md. 72",
    "Bay (L), işyeri olarak kiraya verdiği dükkânın 2025, 2026 ve 2027 yıllarına ait kiralarını 2025 yılında peşin olarak "
    f"tahsil etmiştir.\n\n{K}, peşin tahsil edilen kiraların vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gelecek yıllara ait peşin tahsil edilen kiralar ilgili oldukları yılların hasılatı sayılır.",
    ["Gayrimenkul sermaye iradında tahsil esası geçerli olduğundan kiraların tamamı 2025 yılının hasılatıdır.",
     "Peşin kiralar gayrimenkul sermaye iradı değil, arızi kazanç sayılır.",
     "Peşin kiraların tamamı son yıl olan 2027 yılında vergilendirilir.",
     "Peşin tahsil edilen kiralar vergiden istisnadır."],
    "Md. 72'ye göre gayrisafi hasılat bir takvim yılında o yıla veya geçmiş yıllara ait olarak tahsil edilen kiralardır; "
    "gelecek yıllara ait olup peşin tahsil edilen kiralar ilgili bulundukları yılların hasılatı sayılır (ölüm ve memleketi "
    "terk hâlleri hariç).", zorluk="hard")

P.q("GVK md. 70",
    f"{K}, aşağıdakilerden hangisinin kiraya verilmesinden elde edilen irat gayrimenkul sermaye iradı sayılmaz?",
    "Ticari işletmenin envanterine kayıtlı iş makinesi",
    ["Döşeli olarak kiraya verilen binalar (döşeme bedeli dahil)",
     "Madenler, taş, kum ve çakıl ocakları ile bunlara ait tesisler",
     "Motorlu nakil vasıtaları ile her türlü motorlu araç",
     "Gayrimenkul olarak tescil edilen haklar"],
    "Md. 70'e göre arazi, bina, gemi, motorlu taşıtlar ve gayrimenkul olarak tescil edilen hakların sahipleri tarafından "
    "kiraya verilmesinden elde edilen iratlar gayrimenkul sermaye iradıdır. Ticari işletmeye dahil iktisadi kıymetlerin "
    "kiralanmasından elde edilen gelir ticari kazançtır.")

# ================================================================ menkul sermaye iradı
P.q("GVK md. 75",
    "Tam mükellef Bayan (V), ticari, zirai veya mesleki faaliyeti bulunmaksızın birikimlerini farklı yatırım araçlarında "
    "değerlendirmekte; 2025 yılında bu araçlardan hem dönemsel gelir hem de satış bedeli elde etmektedir."
    f"\n\n{K}, aşağıdakilerden hangisi menkul sermaye iradı sayılmaz?",
    "Hisse senedinin satış bedeli",
    ["Her nevi hisse senedinin kâr payları",
     "İştirak hisselerinden doğan kazançlar",
     "Mevduat faizleri",
     "Repo gelirleri"],
    "Md. 75 kâr payları, iştirak hisselerinden doğan kazançlar, mevduat faizleri ve repo gelirlerini menkul sermaye iradı "
    "sayar. Md. 76'ya göre menkul kıymetin satılması karşılığında alınan paralar menkul sermaye iradı sayılmaz; bu "
    "kazançlar değer artışı veya ticari kazanç hükümlerine tabidir.")

kp = 1_200_000 / 2
P.sayisal("GVK md. 22/3, 86",
    "Tam mükellef Bayan (H), 2025 yılında tam mükellef bir anonim şirketten brüt 1.200.000 ₺ kâr payı elde etmiş, dağıtım "
    "sırasında tevkifat yapılmıştır. Başka geliri yoktur. (2025 yılında tevkifata tabi menkul sermaye iratları için beyan "
    f"sınırı 330.000 ₺ olarak alınacaktır.)\n\n{K}, Bayan (H)’nin yıllık beyannameye dahil edeceği kâr payı tutarı kaç ₺’dir?",
    tl(kp), secenekler(kp, 1_200_000, 0, 1_200_000 - 330_000, 600_000 - 330_000),
    "Md. 22/3'e göre tam mükellef kurumlardan elde edilen kâr paylarının yarısı istisnadır; kalan 600.000 ₺ beyan sınırını "
    "(330.000 ₺) aştığından md. 86 uyarınca beyan edilir ve tevkif edilen vergi mahsup edilir.")

P.q("GVK md. 75, 22/3",
    "Bayan (M), tam mükellef bir anonim şirketin ortağı olarak 2025 yılında şirketten brüt 1.000.000 ₺ kâr payı almış, "
    f"ayrıca Türkiye'deki bir bankada bulunan mevduatından tevkifata tabi faiz elde etmiştir.\n\n{K}, bu gelirlerin "
    "niteliğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her ikisi de menkul sermaye iradıdır; kâr payının yarısı istisnadır.",
    ["Kâr payı ticari kazanç, faiz menkul sermaye iradıdır.",
     "Her ikisi de menkul sermaye iradıdır; faiz gelirinin yarısı istisnadır.",
     "Kâr payı değer artışı kazancı, faiz ise arızi kazançtır.",
     "Her ikisi de gayrimenkul sermaye iradıdır ve beyan edilmez."],
    "Md. 75'e göre hisse senedi kâr payları ve mevduat faizleri menkul sermaye iradıdır; md. 22/3'e göre tam mükellef "
    "kurumlardan elde edilen kâr paylarının yarısı istisnadır. Mevduat faizi için böyle bir istisna yoktur.")

# ================================================================ değer artışı
end_maliyet = 2_000_000 * 2_640 / 1_200
kazanc = 5_000_000 - end_maliyet - 60_000
vergiye = kazanc - 120_000
P.sayisal("GVK mük. 80, mük. 81",
    "Bay (N) Mart 2022’de 2.000.000 ₺’ye satın aldığı konutu Kasım 2025’te 5.000.000 ₺’ye satmış, satış nedeniyle "
    "üzerinde kalan 60.000 ₺ tapu harcı ödemiştir. Yİ-ÜFE değerleri: iktisap ayından önceki ay 1.200, elden çıkarma ayından "
    "önceki ay 2.640’tır. (2025 yılı değer artışı kazancı istisna tutarı 120.000 ₺ olarak alınacaktır.)"
    f"\n\n{K}, Bay (N)’nin beyan edeceği vergiye tabi değer artışı kazancı kaç ₺’dir?",
    tl(vergiye), secenekler(vergiye, 5_000_000 - 2_000_000 - 60_000 - 120_000, kazanc, 5_000_000 - end_maliyet - 120_000,
                            5_000_000 - 2_000_000 - 120_000),
    "Mük. 80/6'ya göre gayrimenkulün beş yıl içinde elden çıkarılmasından doğan kazanç değer artışı kazancıdır. Mük. 81'e "
    "göre endeks artışı %10'u aştığından (2.640/1.200 = 2,2) maliyet 2.000.000 × 2,2 = 4.400.000 ₺'ye endekslenir; satıcının "
    "ödediği harç da indirilir: 5.000.000 − 4.400.000 − 60.000 = 540.000 ₺. İstisna düşülünce 420.000 ₺.", zorluk="hard")

P.q("GVK mük. 80",
    "Bay (P) 2018 yılında satın aldığı bir arsayı 2025 yılında önemli bir kazançla satmıştır. Arsa ticari işletmeye dahil "
    f"değildir.\n\n{K}, bu satıştan doğan kazanca ilişkin aşağıdakilerden hangisi doğrudur?",
    "Beş yıl geçtikten sonra satıldığından değer artışı kazancı doğmaz.",
    ["Elde tutma süresine bakılmaksızın değer artışı kazancı olarak beyan edilir.",
     "Satış kazancının yarısı istisna, kalanı değer artışı kazancıdır.",
     "Arsa satışları arızi kazanç olarak vergilendirilir.",
     "Satış kazancı gayrimenkul sermaye iradı olarak vergilendirilir."],
    "Mük. 80/6'ya göre md. 70/1'de yazılı mal ve hakların iktisap tarihinden başlayarak beş yıl içinde elden çıkarılmasından "
    "doğan kazançlar değer artışı kazancıdır; 2018'de alınıp 2025'te satılan arsa bu süreyi aştığından vergilendirilmez.")

P.q("GVK mük. 80",
    "Bay (Y)’nin mali müşaviri, müşterisinin 2025 yılında çeşitli mal ve haklarını elden çıkarmasından doğan kazançların "
    "hangilerinin değer artışı kazancı olarak beyan edileceğini, iktisap şekli ve elde tutma sürelerini dikkate alarak "
    f"belirlemektedir.\n\n{K}, aşağıdakilerden hangisi değer artışı kazancı sayılmaz?",
    "Miras yoluyla intikal eden bir dairenin iki yıl içinde satılmasından doğan kazanç",
    ["Ortaklık haklarının elden çıkarılmasından doğan kazanç",
     "Faaliyeti durdurulan bir işletmenin elden çıkarılmasından doğan kazanç",
     "Telif hakkının müellif dışında bir kişi tarafından elden çıkarılmasından doğan kazanç",
     "Satın alınan bir konutun beş yıl içinde satılmasından doğan kazanç"],
    "Mük. 80'e göre ortaklık hakları, faaliyeti durdurulan işletme, müellif dışındakilerce elden çıkarılan telif hakları ve "
    "beş yıl içinde satılan gayrimenkuller değer artışı kazancı doğurur. İvazsız olarak (miras, bağış) iktisap edilen "
    "gayrimenkullerin elden çıkarılması kapsam dışıdır.")

P.q("GVK mük. 80/3",
    "Taksi şoförü Bay (R), 2025 yılında sahibi olduğu ticari taksi plakasını 5.000.000 ₺’ye satmıştır. Plaka ticari işletmeye "
    f"dahil değildir.\n\n{K}, bu satıştan doğan kazanca ilişkin aşağıdakilerden hangisi doğrudur?",
    "Taksi plakalarının elden çıkarılmasından doğan kazancın tamamı istisnadır.",
    ["Kazancın değer artışı istisna tutarını aşan kısmı beyan edilir.",
     "Plaka satışı arızi bir işlem olduğundan kazancın tamamı arızi kazanç olarak beyan edilir.",
     "Kazanç ancak plaka beş yıldan fazla elde tutulmuşsa istisnadır.",
     "Kazancın yarısı istisna, kalanı değer artışı kazancıdır."],
    "Mük. 80/3'e göre taksi, dolmuş, minibüs ve umum servis araçlarına ait ticari plakaların elden çıkarılmasından doğan "
    "kazançların tamamı gelir vergisinden müstesnadır (2026/2 kitapçığındaki örnekte olduğu gibi).", zorluk="easy")

P.q("GVK mük. 81",
    f"{K}, değer artışı kazancının hesaplanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Endeksleme, Yİ-ÜFE’deki artış oranına bakılmaksızın her satışta yapılır.",
    ["Safi kazanç, elden çıkarma bedelinden maliyet bedeli ile satıcının uhdesinde kalan giderler ve vergiler düşülerek bulunur.",
     "Maliyet bedeli tespit edilemezse takdir komisyonunca tespit edilecek bedel esas alınır.",
     "İşletmeye dahil amortismana tabi kıymetlerde maliyet yerine amortismanlar düşüldükten sonraki net değer esas alınır.",
     "Menkul kıymetlerde iktisap bedeli tevsik edilemezse itibari değer iktisap bedeli kabul edilir."],
    "Mük. 81'e göre iktisap bedeli fiyat endeksindeki artış oranında artırılır; ancak endekslemenin yapılabilmesi için artış "
    "oranının %10 veya üzerinde olması şarttır. Diğer ifadeler maddeye uygundur.")

P.q("GVK md. 81",
    f"{K}, aşağıdakilerden hangisinde değer artışı kazancı hesaplanmaz ve vergilendirilmez?",
    "Ölen işletme sahibinin işletmesinin mirasçılarca kayıtlı değerlerle devralınması",
    ["Bir hissenin iki yıl içinde satılması",
     "Faaliyeti durdurulmuş bir ferdi işletmenin bütün olarak başka bir kişiye satılması",
     "Bedel ödenerek satın alınan bir konutun üç yıl sonra satılması",
     "Ortaklık haklarının bedel karşılığında devredilmesi"],
    "Md. 81'e göre ferdi işletme sahibinin ölümü hâlinde kanuni mirasçıların faaliyete devam etmesi ve işletmeye dahil "
    "kıymetleri kayıtlı değerleriyle devralması, ferdi işletmenin bütün hâlinde sermaye şirketine devri ve şahıs "
    "şirketlerinin sermaye şirketine dönüşmesi hâllerinde değer artışı kazancı hesaplanmaz.")

# ================================================================ arızi kazanç
az = 500_000 - 30_000 - 280_000
P.sayisal("GVK md. 82",
    "Bay (S), işyeri olarak kiraladığı dükkânı süre bitmeden tahliye etmesi karşılığında mal sahibinden 2025 yılında "
    "500.000 ₺ tazminat almış; tahliye nedeniyle belgelendirilmiş 30.000 ₺ nakliye gideri yapmıştır. Aynı yıl başka arızi "
    "kazancı yoktur. (2025 yılı arızi kazanç istisna tutarı 280.000 ₺ olarak alınacaktır.)"
    f"\n\n{K}, Bay (S)’nin vergiye tabi arızi kazancı kaç ₺’dir?",
    tl(az), secenekler(az, 500_000 - 280_000, 500_000 - 30_000, 500_000, 280_000 - 30_000),
    "Md. 82/3'e göre gayrimenkullerin tahliyesi karşılığında alınan tazminatlar arızi kazançtır; tevsik edilen giderler "
    "hasılattan indirilir (470.000 ₺). Bu bentteki kazançlar için istisna tutarı düşülür: 470.000 − 280.000 = 190.000 ₺.")

ih = 350_000
P.sayisal("GVK md. 82",
    "İnşaat firması sahibi olmayan Bay (M), 2025 yılında bir kamu ihalesine katılmaması karşılığında rakip bir kişiden "
    "350.000 ₺ almıştır. Aynı yıl başka arızi kazancı yoktur. (2025 yılı arızi kazanç istisna tutarı 280.000 ₺ olarak "
    f"alınacaktır.)\n\n{K}, Bay (M)’nin vergiye tabi arızi kazancı kaç ₺’dir?",
    tl(ih), secenekler(ih, 350_000 - 280_000, 0, 350_000 / 2, 280_000),
    "Md. 82/2'ye göre ihale, artırma ve eksiltmelere iştirak edilmemesi karşılığında elde edilen hasılat arızi kazançtır; "
    "maddedeki istisna bu kazançlara uygulanmaz. Tutarın tamamı (350.000 ₺) vergiye tabidir.", zorluk="hard")

P.q("GVK md. 82",
    f"{K}, arızi kazanç istisnasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Henüz başlamamış bir faaliyete girişilmemesi karşılığında alınan tazminat da istisna kapsamındadır.",
    ["Arızi olarak yapılan ticari muamelelerden elde edilen kazançlar istisna kapsamındadır.",
     "Gayrimenkulün tahliyesi karşılığında alınan tazminatlar istisna kapsamındadır.",
     "Arızi olarak yapılan serbest meslek faaliyetlerinden tahsil edilen hasılat istisna kapsamındadır.",
     "İstisna, bir takvim yılında elde edilen kapsamdaki kazançların toplamına uygulanır."],
    "Md. 82'ye göre (1), (2), (3) ve (4) numaralı bentlerdeki kazançlar toplamının kanunda belirtilen kısmı istisnadır; "
    "ancak henüz başlamamış bir faaliyete girişilmemesi ile ihale, artırma ve eksiltmelere iştirak edilmemesi karşılığında "
    "elde edilen kazançlar istisna dışıdır.", zorluk="hard")

P.q("GVK md. 82",
    "Herhangi bir ticari veya mesleki faaliyeti bulunmayan Bay (T), 2025 yılında sürekli bir faaliyete bağlı olmayan "
    "çeşitli gelirler elde etmiş ve bunların hangilerinin arızi kazanç olarak değerlendirileceğini mali müşavirine "
    f"sormuştur.\n\n{K}, aşağıdakilerden hangisi arızi kazanç sayılmaz?",
    "Bir konutun kiraya verilmesinden elde edilen kira geliri",
    ["Bir ihaleye katılmama karşılığında alınan tazminat",
     "Kiracılık hakkının devri karşılığında alınan peştemallık",
     "Arızi olarak yapılan serbest meslek faaliyetinden tahsil edilen hasılat",
     "Gerçek usulde vergilendirilen mükellefin terk ettiği işiyle ilgili sonradan tahsil ettiği şüpheli alacak"],
    "Md. 82'ye göre ihaleye katılmama karşılığı alınan tazminat, peştemallık, arızi serbest meslek hasılatı ve terk edilen "
    "işle ilgili sonradan elde edilen kazançlar arızi kazançtır. Konut kira geliri gayrimenkul sermaye iradıdır (md. 70).")

# ================================================================ karma sınıflandırma
P.oncul("GVK md. 70, 75, mük. 80, 82",
    f"{K} aşağıdaki eşleştirmeler değerlendirilmektedir:",
    ["İşyeri kira geliri – gayrimenkul sermaye iradı",
     "Hisse senedi kâr payı – menkul sermaye iradı",
     "Ortaklık hissesinin satış kazancı – arızi kazanç",
     "Peştemallık – arızi kazanç"],
    "Yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 70'e göre işyeri kirası gayrimenkul sermaye iradı (I), md. 75'e göre kâr payı menkul sermaye iradı (II), md. 82'ye "
    "göre peştemallık arızi kazançtır (IV). Mük. 80/4'e göre ortaklık haklarının elden çıkarılması değer artışı kazancıdır "
    "(III yanlış).", zorluk="hard")

P.q("GVK md. 18",
    "Yazar Bayan (T), 2025 yılında yayımlanan romanının telif hakkı karşılığında yayınevinden 1.800.000 ₺ almıştır; başka "
    "telif kazancı yoktur. Yayınevi ödeme sırasında tevkifat yapmıştır. (2025 yılı için tarifenin dördüncü gelir dilimindeki "
    f"tutar 4.300.000 ₺’dir.)\n\n{K}, bu gelire ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kazanç istisnadır; ancak istisna tevkifatı kapsamadığından yapılan tevkifat nihai vergidir.",
    ["Kazanç istisna olduğundan yayınevinin tevkifat yapması hatalıdır.",
     "Kazanç serbest meslek kazancı olarak yıllık beyannameyle beyan edilir ve kesilen vergi mahsup edilir.",
     "Kazancın yarısı istisna, kalanı beyan edilir.",
     "Kazanç arızi kazanç sayılır ve istisna tutarını aşan kısmı beyan edilir."],
    "Md. 18'e göre müelliflerin eserlerinin yayımlanmasından elde ettikleri hasılat istisnadır; bu kapsamdaki kazanç toplamı "
    "dördüncü dilim tutarını aşmadığından istisna uygulanır. İstisnanın md. 94 uyarınca tevkif suretiyle ödenecek vergiye "
    "şümulü yoktur; tevkifat yapılır ve istisna kazanç beyan edilmediğinden kesinti nihai vergi olur.", zorluk="hard")

P.q("GVK md. 38",
    f"{K}, bilanço esasına göre ticari kazancın tespitine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dönem içinde işletmeden çekilen değerler dönem başı ve sonu öz sermaye farkından indirilir.",
    ["Ticari kazanç, teşebbüsteki öz sermayenin dönem sonu ve dönem başındaki değerleri arasındaki müspet farktır.",
     "Dönem içinde işletmeye ilave olunan değerler bu farktan indirilir.",
     "Kazancın tespitinde VUK’un değerlemeye ait hükümlerine uyulur.",
     "Kazancın tespitinde md. 40 ve 41 hükümlerine uyulur."],
    "Md. 38'e göre bilanço esasında ticari kazanç öz sermaye farkıdır; dönem içinde işletmeye ilave edilen değerler farktan "
    "indirilir, işletmeden çekilen değerler ise farka ilave olunur. VUK değerleme hükümleri ile md. 40-41'e uyulur.")

# ================================================================ ek hesap soruları
az2 = 400_000 - 280_000
P.sayisal("GVK md. 82",
    "Mimar olmayan Bay (U), 2025 yılında bir defaya mahsus olmak üzere arkadaşının iş yerinin iç tasarımını yapmış ve "
    "karşılığında 400.000 ₺ almıştır; bu işle ilgili belgelendirilmiş gideri yoktur. Aynı yıl başka arızi kazancı yoktur. "
    f"(2025 yılı arızi kazanç istisna tutarı 280.000 ₺ olarak alınacaktır.)\n\n{K}, Bay (U)’nun vergiye tabi arızi "
    "kazancı kaç ₺’dir?",
    tl(az2), secenekler(az2, 400_000, 400_000 * 0.85, 280_000, 400_000 - 140_000),
    "Md. 82/4'e göre arızi olarak yapılan serbest meslek faaliyetlerinden tahsil edilen hasılat arızi kazançtır; bu "
    "kazançlar için istisna tutarı düşülür: 400.000 − 280.000 = 120.000 ₺.", zorluk="easy")

em = 3_600_000 * 0.05
P.sayisal("GVK md. 73",
    "Bayan (V), emlak vergi değeri 3.600.000 ₺ olan ve boş durmayan bir dairesini 2025 yılı boyunca iş arkadaşına bedelsiz "
    "olarak kullandırmıştır; takdir edilmiş bir kira bulunmamaktadır. Bayan (V) götürü gider yöntemini seçmiştir. (2025 "
    f"yılı konut kira istisnası 47.000 ₺’dir; Bayan (V)’nin başka geliri yoktur.)\n\n{K}, Bayan (V)’nin beyan edeceği safi "
    "kira geliri kaç ₺’dir?",
    tl((em - 47_000) * 0.85), secenekler((em - 47_000) * 0.85, em, em * 0.85, em - 47_000, 3_600_000 * 0.10),
    "Md. 73'e göre bedelsiz kullandırılan konut için emsal kira bedeli (vergi değerinin %5'i = 180.000 ₺) kira sayılır. "
    "Md. 21 istisnası (47.000 ₺) ve md. 74'teki %15 götürü gider uygulanır: (180.000 − 47.000) × 0,85 = 113.050 ₺.",
    zorluk="hard")

# ================================================================ olumsuz karma
P.q("GVK md. 6-7",
    f"{K}, dar mükellefler bakımından kazanç ve iradın Türkiye'de elde edilmesine ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "İşyeri ve daimi temsilci olmasa da dar mükellefin Türkiye’ye her satışı ticari kazanç doğurur.",
    ["Dar mükellefler sadece Türkiye’de elde ettikleri kazanç ve iratlar üzerinden vergilendirilir.",
     "Zirai kazançta zirai faaliyetin Türkiye’de icra edilmesi gerekir.",
     "Ücrette hizmetin Türkiye’de ifa edilmesi veya Türkiye’de değerlendirilmesi gerekir.",
     "Ticari kazançta işyeri veya daimi temsilci ve kazancın bunlar vasıtasıyla sağlanması aranır."],
    "Md. 6'ya göre dar mükellefler sadece Türkiye'de elde ettikleri kazançlar üzerinden vergilendirilir. Md. 7'ye göre "
    "ticari kazançta Türkiye'de işyeri veya daimi temsilci bulunması ve kazancın bunlar vasıtasıyla sağlanması, zirai "
    "kazançta faaliyetin Türkiye'de icrası, ücrette hizmetin Türkiye'de ifası veya değerlendirilmesi aranır.")

P.q("GVK md. 9",
    f"{K26}, esnaf muaflığına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Evde üretilen ürünlerin internetten satışında muafiyet için satış tutarı sınırı yoktur.",
    ["Gezici perakende ticarette muafiyet için motorlu nakil vasıtası kullanılmaması şarttır.",
     "Pazar takibi suretiyle gıda maddesi satanlar muaflıktan yararlanamaz.",
     "Evde üretim yapanlarda muharrik kuvvet kullanmamak ve dışarıdan işçi almamak şarttır.",
     "Hayvanla veya tek bir hayvan arabasıyla nakliyecilik yapanlar da esnaf muaflığından yararlanır."],
    "Md. 9/6'ya göre evde üretilen ürünlerin internet ve benzeri ortamlardan satışında yıllık satış tutarının asgari ücretin "
    "yıllık brüt tutarını aşmaması şartı vardır. Motorlu araç kullanmama, pazar takibi istisnası, muharrik kuvvet ve işçi "
    "şartı ile hayvan arabası muafiyeti maddede yer alır.", zorluk="hard")

P.q("GVK md. 40, 68",
    f"{K26}, binek otomobil giderlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Binek otomobil kiralama işiyle uğraşanlar da kiraladıkları araçların giderlerinin %30’unu indiremez.",
    ["Binek otomobillere ilişkin giderlerin en fazla %70’i indirilebilir.",
     "Kiralanan binek otomobillerde aylık kira bedelinin kanunda belirtilen tutara kadarlık kısmı gider yazılabilir.",
     "Binek otomobilin iktisabındaki ÖTV ve KDV toplamının kanunda belirtilen tutara kadarlık kısmı gider yazılabilir.",
     "Serbest meslek erbabının mesleğinde kullandığı binek otomobil giderleri için de benzer sınırlama vardır."],
    "Md. 40/5 ve 68/5'e göre binek otomobillere ilişkin giderlerin en fazla %70'i indirilebilir; kira bedeli ile ÖTV ve KDV "
    "için de tutar sınırları vardır. Ancak faaliyeti kısmen veya tamamen binek otomobil kiralanması veya işletilmesi olanların "
    "bu amaçla kullandıkları araçlar sınırlama dışındadır.", zorluk="hard")

P.q("GVK md. 61",
    "Bir işveren, çalışanlarına 2025 yılında nakit ücretin yanında ayni yardımlar ve çeşitli menfaatler sağlamış; "
    "yönetim kurulu üyelerine de huzur hakkı ödemiştir. Bu ödemelerin vergilendirilmesi için ücret kavramının kapsamı "
    f"değerlendirilmektedir.\n\n{K}, ücrete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ücretin ödenme şekli, ayni veya nakdi olması onun ücret niteliğini değiştirir.",
    ["Ücret, işverene tabi ve belirli bir işyerine bağlı çalışanlara hizmet karşılığı verilen para ve ayınlardır.",
     "Ücretin ödeyen tarafından verilmiş olması hizmetin nerede yapıldığından bağımsız olarak ücret niteliğini etkilemez.",
     "Yönetim kurulu üyelerine ödenen huzur hakları ücret sayılır.",
     "Emekli, dul ve yetim aylıkları ücret sayılan ödemelerdendir."],
    "Md. 61'e göre ücret, hizmet karşılığı verilen para ve ayınlar ile sağlanan ve para ile temsil edilebilen menfaatlerdir; "
    "ödemenin ayni veya nakdi olması, ödeme şekli veya adı ücretin mahiyetini değiştirmez. Huzur hakları ile emekli, dul ve "
    "yetim aylıkları ücret sayılır.", zorluk="hard")

P.q("GVK md. 67",
    f"{K}, serbest meslek kazancının tespitine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Serbest meslek kazancında hasılat, tahakkuk esasına göre hak edildiği yılda dikkate alınır.",
    ["Serbest meslek kazancı, faaliyet dolayısıyla tahsil edilen hasılattan giderlerin indirilmesiyle bulunur.",
     "Hasılat, faaliyet dolayısıyla tahsil edilen para ve ayınlar ile para ile temsil edilen menfaatlerdir.",
     "Mesleki faaliyette kullanılan binek otomobil giderleri için sınırlama uygulanır.",
     "Serbest meslek erbabı mesleki kazanç elde etmese de yıllık beyanname verir."],
    "Md. 67'ye göre serbest meslek kazancı tahsil esasına göre, bir takvim yılı içinde tahsil edilen hasılattan giderlerin "
    "indirilmesiyle bulunur. Md. 68/5 binek otomobil sınırlamasını, md. 85 kazanç olmasa da beyan yükümlülüğünü düzenler.")

P.q("GVK md. 75",
    f"{K}, menkul sermaye iradına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ticari işletmeye dahil hisse senetlerinden elde edilen kâr payları da menkul sermaye iradı sayılır.",
    ["Menkul sermaye iradı, sahibinin ticari, zirai veya mesleki faaliyeti dışında elde edilir.",
     "İştirak hisselerinden doğan kazançlar menkul sermaye iradıdır.",
     "Mevduat faizleri menkul sermaye iradıdır.",
     "Menkul kıymetin satılması karşılığında alınan paralar menkul sermaye iradı sayılmaz."],
    "Md. 75'e göre menkul sermaye iradı, sahibinin ticari, zirai veya mesleki faaliyeti dışında nakdi sermaye dolayısıyla "
    "elde ettiği iratlardır; ticari işletmeye dahil kıymetlerden elde edilen gelirler ticari kazancın unsurudur. Md. 76 "
    "satış bedellerini menkul sermaye iradı saymaz.")

P.q("GVK md. 70",
    f"{K}, gayrimenkul sermaye iradına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İhtira beratının mucidi tarafından kiralanmasından doğan kazanç gayrimenkul sermaye iradıdır.",
    ["Arazi ve binaların kiraya verilmesinden elde edilen iratlar gayrimenkul sermaye iradıdır.",
     "Döşeli kiraya verilen binalarda döşeme için alınan bedeller de kira bedeline dahildir.",
     "Gayrimenkul olarak tescil edilen hakların kiraya verilmesi gayrimenkul sermaye iradı doğurur.",
     "Gemi ve gemi paylarının kiraya verilmesinden elde edilen iratlar gayrimenkul sermaye iradıdır."],
    "Md. 70/5'e göre ihtira beratının mucitleri veya kanuni mirasçıları tarafından kiralanmasından doğan kazançlar serbest "
    "meslek kazancıdır. Arazi, bina (döşeme bedeli dahil), tescilli haklar ve gemiler gayrimenkul sermaye iradının konusudur.")

P.q("GVK mük. 80",
    f"{K}, değer artışı kazancına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ticari işletmeye dahil amortismana tabi bir kıymetin satışından doğan kazanç değer artışı kazancıdır.",
    ["Elden çıkarma; satış, ivaz karşılığında devir, trampa, takas ve kamulaştırmayı kapsar.",
     "Mal ve hakların ticaret şirketlerine sermaye olarak konulması da elden çıkarma sayılır.",
     "Tam mükellef kurum hisselerinden iki yıldan fazla elde tutulanların satış kazancı kapsam dışıdır.",
     "İvazsız olarak iktisap edilen gayrimenkullerin elden çıkarılması kapsam dışıdır."],
    "Mük. 80'e göre elden çıkarma satış, ivazlı devir, trampa, takas, kamulaştırma ve şirkete sermaye olarak konulmayı "
    "kapsar; iki yıldan fazla elde tutulan tam mükellef kurum hisseleri ve ivazsız iktisaplar kapsam dışıdır. Ticari "
    "işletmeye dahil amortismana tabi kıymetlerin elden çıkarılmasından doğan kazanç ticari kazanç sayılır.")

P.q("GVK md. 42, mük. 120",
    f"{K}, yıllara yaygın inşaat ve onarım işlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu işlerden doğan kazançlar her yıl geçici vergi matrahına dahil edilir.",
    ["Kazanç işin bittiği yılda tespit edilir.",
     "Kazanç işin bittiği yılın geliri olarak beyan edilir.",
     "İşin birden fazla takvim yılına yaygın olması gerekir.",
     "Bu işlerle ilgili olarak yapılan hakediş ödemelerinden gelir vergisi tevkifatı yapılır."],
    "Md. 42'ye göre birden fazla takvim yılına yaygın inşaat ve onarım işlerinde kazanç işin bittiği yılda tespit edilip "
    "beyan edilir; md. 94/3'e göre hakedişlerden tevkifat yapılır. Mük. 120'ye göre bu kazançlar geçici vergi matrahına "
    "dahil edilmez.")

P.q("GVK md. 72",
    f"{K}, gayrimenkul sermaye iradında gayrisafi hasılata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kiracının bedelsiz bıraktığı kalıcı ilaveler, kiralayan açısından hasılat sayılmaz.",
    ["Gayrisafi hasılat, o yıla veya geçmiş yıllara ait olarak tahsil edilen kira bedelleridir.",
     "Ayın olarak tahsil edilen kiralar VUK hükümlerine göre emsal bedeliyle paraya çevrilir.",
     "Gelecek yıllara ait peşin tahsil edilen kiralar ilgili oldukları yılların hasılatı sayılır.",
     "Ölüm ve memleketi terk hâllerinde peşin tahsil edilen kiralara ilişkin özel hüküm vardır."],
    "Md. 72'ye göre kiracının gayrimenkulü genişleten veya iktisadi değerini devamlı artıran ilaveleri kira süresi sonunda "
    "bedelsiz devretmesi hâlinde bu kıymetler kiralayan bakımından o tarihte aynen tahsil edilmiş sayılır.", zorluk="hard")

P.q("GVK md. 23",
    f"{K26}, ücret istisnalarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Asgari ücrete isabet eden istisna serbest meslek kazançlarına da uygulanır.",
    ["Emekli, malullük, dul ve yetim aylıkları istisnadır.",
     "Asgari ücrete isabet eden kısım için öngörülen istisna hizmet erbabının ücretine uygulanır.",
     "Köy muhtarlarına ödenen ücretler istisnadır.",
     "İşverence iş yerinde verilen yemek bedelleri kanundaki şartlar dahilinde istisnadır."],
    "Md. 23'e göre emekli aylıkları, köy muhtarlarına ödenen ücretler, iş yerinde verilen yemek ve hizmet erbabının asgari "
    "ücretin aylık brüt tutarından SGK ve işsizlik primleri düşüldükten sonra kalan kısma isabet eden ücreti istisnadır. "
    "Bu istisna serbest meslek kazançlarına uygulanmaz.", zorluk="hard")

# ================================================================ ek sayısal sorular
kk = (45_000 - 37_000) * 12
P.sayisal("GVK md. 40/5",
    "Tüccar Bay (Y), işinde kullanmak üzere 2025 yılının tamamında aylık 45.000 ₺ (KDV hariç) bedelle bir binek otomobil "
    "kiralamış ve kira bedellerinin tamamını gider yazmıştır. Faaliyeti binek otomobil kiralama değildir. (2025 yılı için "
    f"binek otomobil aylık kira bedeli gider sınırı 37.000 ₺ olarak alınacaktır.)\n\n{K26}, bu kira giderlerinden kanunen "
    "kabul edilmeyen gider olarak dikkate alınacak tutar kaç ₺’dir?",
    tl(kk), secenekler(kk, 45_000 * 12 * 0.30, 8_000, 37_000 * 12, 45_000 * 12 * 0.70),
    "Md. 40/5'e göre kiralanan binek otomobillerde aylık kira bedelinin kanunda belirtilen tutarı aşan kısmı gider "
    "yazılamaz; bu kira bedeline ayrıca %70 sınırı uygulanmaz: (45.000 − 37.000) × 12 = 96.000 ₺.", zorluk="hard")

bk = (5_000_000 - 3_500_000) - 600_000 + 400_000
P.sayisal("GVK md. 38",
    "Bilanço esasına göre defter tutan ferdi işletme sahibi Bayan (Z)’nin öz sermayesi 1 Ocak 2025’te 3.500.000 ₺, 31 Aralık "
    "2025’te 5.000.000 ₺’dir. Yıl içinde işletmeye 600.000 ₺ nakit sermaye eklemiş, işletmeden kişisel ihtiyaçları için "
    "400.000 ₺ çekmiştir. Kanunen kabul edilmeyen gider ve istisna kazanç bulunmamaktadır."
    f"\n\n{K}, Bayan (Z)’nin 2025 yılı ticari kazancı kaç ₺’dir?",
    tl(bk), secenekler(bk, 1_500_000, 1_500_000 - 600_000 - 400_000, 1_500_000 + 600_000 - 400_000, 1_500_000 + 600_000 + 400_000),
    "Md. 38'e göre bilanço esasında ticari kazanç öz sermaye farkıdır; dönem içinde işletmeye ilave edilen değerler bu "
    "farktan indirilir, çekilen değerler farka eklenir: 1.500.000 − 600.000 + 400.000 = 1.300.000 ₺.")

smt = 1_600_000 - 450_000 - 300_000
P.sayisal("GVK md. 66-67",
    "Avukat Bay (F), 2025 yılında toplam 2.100.000 ₺ tutarında serbest meslek makbuzu düzenlemiştir; bunun 500.000 ₺’si 2026 "
    "Ocak ayında tahsil edilmiş, kalanı 2025 yılı içinde tahsil edilmiştir. Önceki yıllardan tahsil edilen alacağı yoktur. 2025 yılında ödediği büro gideri 450.000 ₺, personel gideri 300.000 ₺’dir."
    f"\n\n{K}, Bay (F)’nin 2025 yılı serbest meslek kazancı kaç ₺’dir?",
    tl(smt), secenekler(smt, 2_100_000 - 750_000, 2_100_000 - 450_000, 1_600_000 - 450_000, 2_100_000 - 500_000),
    "Md. 67'ye göre serbest meslek kazancı tahsil esasına göre tespit edilir; 2026'da tahsil edilen 500.000 ₺ 2025 "
    "hasılatına girmez: (2.100.000 − 500.000) − 450.000 − 300.000 = 850.000 ₺.")

ea = 1_500_000 * 0.10
P.sayisal("GVK md. 73",
    "Bay (G), 1.500.000 ₺’ye satın aldığı ve ticari işletmesine dahil olmayan bir hafif ticari aracını 2025 yılı boyunca bir "
    "arkadaşının kullanımına bedelsiz olarak bırakmıştır. Aracın VUK’a göre belirlenen değeri 1.200.000 ₺’dir."
    f"\n\n{K}, Bay (G) açısından 2025 yılı için dikkate alınacak emsal kira bedeli kaç ₺’dir?",
    tl(ea), secenekler(ea, 1_500_000 * 0.05, 1_200_000 * 0.10, 1_200_000 * 0.05, 1_500_000 * 0.15),
    "Md. 73'e göre bina ve arazi dışındaki mal ve haklarda emsal kira bedeli, maliyet bedelinin (bilinmiyorsa VUK'a göre "
    "belirlenen değerin) %10'udur: 1.500.000 × %10 = 150.000 ₺. Maliyet bilindiği için VUK değeri kullanılmaz.",
    zorluk="hard")

hs = 900_000 - 700_000
P.sayisal("GVK mük. 80, mük. 81",
    "Bay (K), 2024 yılında 700.000 ₺’ye satın aldığı ve borsada işlem görmeyen tam mükellef bir anonim şirket hisse "
    "senetlerini 2025 yılında 900.000 ₺’ye satmıştır. Yİ-ÜFE değerleri: iktisap ayından önceki ay 1.000, elden çıkarma "
    "ayından önceki ay 1.080’dir. Hisseler ticari işletmeye dahil değildir. (2025 yılı değer artışı kazancı istisna tutarı "
    f"120.000 ₺ olarak alınacaktır.)\n\n{K}, Bay (K)’nin vergiye tabi değer artışı kazancı kaç ₺’dir?",
    tl(hs), secenekler(hs, hs - 120_000, 900_000 - 700_000 * 1.08, 900_000 - 700_000 * 1.08 - 120_000, 0),
    "Hisseler iki yıl dolmadan satıldığından mük. 80/1 kapsamında değer artışı doğar. Endeks artışı %8 olup %10'un altında "
    "kaldığından mük. 81'e göre endeksleme yapılmaz. Mük. 80'deki istisna menkul kıymetlerin elden çıkarılmasından "
    "sağlanan kazançlara uygulanmaz: 900.000 − 700.000 = 200.000 ₺.", zorluk="hard")

gd = 3_600_000 - 3_000_000 - 120_000
P.sayisal("GVK mük. 80, mük. 81",
    "Bayan (L), 2023 yılında 3.000.000 ₺’ye satın aldığı arsayı 2025 yılında 3.600.000 ₺’ye satmıştır. Yİ-ÜFE değerleri: "
    "iktisap ayından önceki ay 2.000, elden çıkarma ayından önceki ay 2.160’tır. Satış giderine katlanmamıştır. (2025 yılı "
    f"değer artışı kazancı istisna tutarı 120.000 ₺ olarak alınacaktır.)\n\n{K}, Bayan (L)’nin vergiye tabi değer artışı "
    "kazancı kaç ₺’dir?",
    tl(gd), secenekler(gd, 600_000, 3_600_000 - 3_000_000 * 1.08 - 120_000, 3_600_000 - 3_000_000 * 1.08, 0),
    "Arsa beş yıl dolmadan satıldığından mük. 80/6 kapsamındadır. Endeks artışı %8'dir; %10'un altında kaldığından maliyet "
    "endekslenmez (mük. 81): 3.600.000 − 3.000.000 = 600.000 ₺; istisna düşülünce 480.000 ₺.")

ar = 200_000 + 150_000 - 280_000
P.sayisal("GVK md. 82",
    "Bay (N), 2025 yılında arızi olarak bir partiden aldığı malı satarak 200.000 ₺ kazanç elde etmiş, ayrıca arızi olarak "
    "bir çeviri işi yapıp 150.000 ₺ tahsil etmiştir. Bu işlerle ilgili belgelendirilmiş gideri yoktur. (2025 yılı arızi "
    f"kazanç istisna tutarı 280.000 ₺ olarak alınacaktır.)\n\n{K}, Bay (N)’nin vergiye tabi arızi kazancı kaç ₺’dir?",
    tl(ar), secenekler(ar, 350_000, 350_000 - 140_000, 0, 150_000),
    "Md. 82/1 ve 82/4'e göre arızi ticari muameleler ve arızi serbest meslek hasılatı arızi kazançtır; istisna bu bentlerdeki "
    "kazançların toplamına bir kez uygulanır: 200.000 + 150.000 − 280.000 = 70.000 ₺.")

if __name__ == "__main__":
    sys.exit(P.yaz())
