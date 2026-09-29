# -*- coding: utf-8 -*-
"""Vergi · Vergi Hukuku · Temel İlkeler ve Vergi Borcunun Tarafları — 60 soru, 2026 test biçimi.

Kapsam: Anayasa md. 73 (kanunilik, mali güç), VUK md. 1-12 (uygulama alanı, yorum ve ispat, vergi mahremiyeti,
mükellef ve vergi sorumlusu, vergi ehliyeti, kanuni temsilciler, vergi kesenler, mirasçılar), vergiyi doğuran olay ve
vergi alacağının sona ermesi (VUK md. 19, 113; 6183 md. 23, 102).

Dayanak: 2709 sayılı Anayasa md. 73; 213 sayılı VUK güncel metni; 6183 sayılı Kanun (29.09.2026 kontrolü).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_vergi_hukuku_ilkeleri_2026.json", lesson="vergi_hukuku", topic="vergi_hukuku_ilkeleri",
          konu_adi="Vergi Hukuku İlkeleri", seed=2026092911,
          surum="Anayasa md. 73, 213 sayılı VUK ve 6183 sayılı Kanun güncel metni; 29.09.2026 kontrolü")

V = "213 sayılı Vergi Usul Kanunu’na göre"
AY = "Türkiye Cumhuriyeti Anayasası’na göre"
A = "6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun’a göre"

mb = 400_000 / 4
P.sayisal("VUK md. 12",
    "Mükellef Bay (K) 2026 yılında vefat etmiştir. Bay (K)’nın ödenmemiş 400.000 ₺ vergi borcu bulunmaktadır. Mirasçıları "
    "eşi ile üç çocuğudur; hiçbiri mirası reddetmemiştir ve her birinin miras hissesi dörtte birdir."
    f"\n\n{V}, çocuklardan birinin bu vergi borcundan sorumlu olduğu tutar kaç ₺’dir?",
    tl(mb), secenekler(mb, 400_000, 400_000 / 3, 200_000, 0),
    "Md. 12'ye göre ölüm hâlinde mükellefin ödevleri mirası reddetmemiş kanuni ve mansup mirasçılarına geçer; her mirasçı "
    "ölünün vergi borçlarından miras hissesi oranında sorumludur: 400.000 × 1/4 = 100.000 ₺.")

P.q("Anayasa md. 73",
    "Bir milletvekili, belirli bir sektöre yeni bir vergi getirilmesinin Cumhurbaşkanı kararıyla yapılmasını önermiştir."
    f"\n\n{AY}, bu öneriye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi kanunla konulur; Cumhurbaşkanı yeni vergi koyamaz.",
    ["Cumhurbaşkanı kararıyla yeni vergi konulabilir.",
     "Vergi Bakanlık tebliğiyle konulabilir.",
     "Yeni vergi yönetmelikle getirilebilir.",
     "Vergi, TBMM kararıyla kanun olmadan konulabilir."],
    "Anayasa md. 73/3'e göre vergi, resim, harç ve benzeri mali yükümlülükler kanunla konulur, değiştirilir veya kaldırılır; "
    "Cumhurbaşkanına sadece kanunun belirttiği sınırlar içinde değişiklik yetkisi verilebilir.", zorluk="easy")

P.q("Anayasa md. 73",
    f"Bir vergi kanununda belirli bir istisnanın oranının Cumhurbaşkanı kararıyla değiştirilebileceği öngörülmüştür.\n\n{AY}, Cumhurbaşkanına verilebilecek vergisel düzenleme yetkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kanunun belirttiği sınırlar içinde oranlarda değişiklik yapabilir.",
    ["Kanunda yer almayan yeni bir vergi türü ihdas edebilir.",
     "Vergi kanunlarını tamamen yürürlükten kaldırabilir.",
     "Vergi mükelleflerini kanun dışında belirleyebilir.",
     "Kanunda öngörülmeyen istisnalar getirebilir."],
    "Anayasa md. 73/4'e göre vergi, resim, harç ve benzeri mali yükümlülüklerin muafiyet, istisna ve indirimleriyle oranlarına "
    "ilişkin hadleri içinde, kanunun belirttiği yukarı ve aşağı sınırlar içinde değişiklik yapma yetkisi Cumhurbaşkanına "
    "verilebilir.")

mb2 = 600_000 * 0.50
P.sayisal("VUK md. 12",
    "Ölen mükellef Bayan (L)’nin 600.000 ₺ vergi borcu vardır. Mirasçılarından eşinin hissesi %50, iki çocuğunun hisseleri "
    f"%25’er olup kimse mirası reddetmemiştir.\n\n{V}, eşin bu vergi borcundan sorumlu olduğu tutar kaç ₺’dir?",
    tl(mb2), secenekler(mb2, 600_000, 200_000, 150_000, 450_000),
    "Md. 12'ye göre mirasçılardan her biri ölünün vergi borçlarından miras hisseleri nispetinde sorumludur: 600.000 × %50 = "
    "300.000 ₺. Vergi cezaları ise md. 372 gereği ölümle düşer.")

P.q("Anayasa md. 73",
    f"Bir kamu maliyesi dersinde vergi yükünün toplum içinde nasıl dağıtılması gerektiği tartışılmakta; bazı öğrenciler herkesin eşit tutarda vergi ödemesi gerektiğini savunmaktadır.\n\n{AY}, aşağıdakilerden hangisi vergilendirme ilkeleri arasında yer alır?",
    "Herkes kamu giderlerini karşılamak üzere mali gücüne göre vergi öder.",
    ["Herkes eşit tutarda vergi öder.",
     "Vergi yükü sadece tüzel kişilere yüklenir.",
     "Vergiler idarenin takdirine göre belirlenir.",
     "Vergi yükünün dağılımı maliye politikasının amacı değildir."],
    "Anayasa md. 73'e göre herkes kamu giderlerini karşılamak üzere mali gücüne göre vergi ödemekle yükümlüdür; vergi yükünün "
    "adaletli ve dengeli dağılımı maliye politikasının sosyal amacıdır.", zorluk="easy")

P.q("Anayasa md. 73",
    f"Bir anayasa hukuku dersinde Anayasa’nın vergi ödevini düzenleyen maddesi incelenmekte; öğrenciler maddenin her fıkrasının hangi ilkeyi düzenlediğini tartışmaktadır.\n\n{AY}, vergilendirmeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Vergi yükünün adaletli dağılımı maliye politikasının ekonomik amacıdır.",
    ["Herkes mali gücüne göre vergi ödemekle yükümlüdür.",
     "Vergiler kanunla konulur, değiştirilir veya kaldırılır.",
     "Cumhurbaşkanına kanuni sınırlar içinde oranları değiştirme yetkisi verilebilir.",
     "Harç ve benzeri mali yükümlülükler de kanunla konulur."],
    "Anayasa md. 73/2'ye göre vergi yükünün adaletli ve dengeli dağılımı maliye politikasının sosyal amacıdır.", zorluk="hard")

kt = 250_000 - 90_000
P.sayisal("VUK md. 10",
    "(ABC) A.Ş.’nin 250.000 ₺ kesinleşmiş vergi borcunun, şirket varlığından ancak 90.000 ₺’lik kısmı tahsil edilebilmiştir. "
    "Borcun ödenmemesi, şirketin kanuni temsilcisi Bay (M)’nin ödevlerini yerine getirmemesinden kaynaklanmıştır."
    f"\n\n{V}, Bay (M)’nin varlığından alınabilecek tutar kaç ₺’dir?",
    tl(kt), secenekler(kt, 250_000, 90_000, 125_000, 0),
    "Md. 10'a göre kanuni temsilcilerin ödevlerini yerine getirmemeleri yüzünden mükellefin varlığından tamamen veya kısmen "
    "alınamayan vergi ve bağlı alacaklar, ödevi yerine getirmeyenlerin varlığından alınır: 250.000 − 90.000 = 160.000 ₺. "
    "Temsilci ödediği tutar için şirkete rücu edebilir.", zorluk="hard")

P.q("Vergi hukuku ilkeleri",
    "Bir vergi kanununda, yayım tarihinden önceki yıllara ait kazançları da kapsayacak şekilde yeni bir vergi getirilmek "
    f"istenmektedir.\n\n{AY} ve vergi hukukunun genel ilkelerine göre bu düzenleme hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Aleyhe geriye yürüme hukuk güvenliğine aykırıdır.",
    ["Vergi kanunları kural olarak geriye yürür.",
     "Geriye yürüme sadece tüzel kişiler için yasaktır.",
     "Geriye yürüme mükellef aleyhine olsa da serbesttir.",
     "Vergi kanunlarında zaman bakımından uygulama sorunu yoktur."],
    "Vergi kanunları kural olarak yürürlüğe girdikten sonra doğan vergiyi doğuran olaylara uygulanır; mükellef aleyhine "
    "geriye yürüme hukuk devleti ve hukuki güvenlik ilkeleriyle bağdaşmaz.", zorluk="hard")

P.q("Vergi hukuku ilkeleri",
    f"Bir hukuk fakültesinde vergi hukukunun temel ilkeleri anlatılırken verginin unsurlarının hangi işlemle belirlenmesi "
    f"gerektiği tartışılmaktadır.\n\n{AY} ve kanunilik ilkesine göre aşağıdakilerden hangisi yanlıştır?",
    "Kıyasla yeni vergi yükümlülüğü getirilebilir.",
    ["Verginin konusu kanunla belirlenir.",
     "Mükellef ve vergi sorumlusu kanunla belirlenir.",
     "Verginin matrahı ve oranı kanunla belirlenir.",
     "Muafiyet ve istisnalar kanunla düzenlenir."],
    "Kanunilik ilkesi gereği verginin konusu, mükellefi, matrahı, oranı, muafiyet ve istisnaları kanunla belirlenir; kıyas "
    "yoluyla yeni bir vergi yükümlülüğü getirilemez.", zorluk="hard")

vk = 800_000 * 0.20
P.sayisal("VUK md. 11",
    "(DEF) Ltd. Şti., bir yazara 800.000 ₺ brüt telif ödemesi yapmış, ancak kesmesi gereken vergiyi kesmemiştir. (Uygulanacak "
    f"tevkifat oranı %20 olarak alınacaktır.)\n\n{V}, şirketin vergi sorumlusu olarak ödemek zorunda olduğu vergi kaç "
    "₺’dir?",
    tl(vk), secenekler(vk, 0, 800_000 * 0.15, 800_000 * 0.10, 800_000 * 0.25),
    "Md. 11'e göre ödemelerden vergi kesmeye mecbur olanlar verginin tam olarak kesilip ödenmesinden sorumludur; bu "
    "sorumluluk asıl mükellefe rücu hakkını kaldırmaz: 800.000 × %20 = 160.000 ₺.")

P.q("VUK md. 1-2",
    f"Bir ithalatçı, gümrükte ödediği vergilere ilişkin uyuşmazlıkta hangi kanunun usul hükümlerinin uygulanacağını sormaktadır.\n\n{V}, aşağıdakilerden hangisi Kanunun uygulama alanı dışındadır?",
    "Gümrük idarelerince alınan vergi ve resimler",
    ["Genel bütçeye giren vergiler",
     "Belediyelere ait vergi, resim ve harçlar",
     "İl özel idarelerine ait vergi ve harçlar",
     "Kaldırılan vergi, resim ve harçlar"],
    "Md. 1'e göre Kanun genel bütçeye giren vergi, resim ve harçlar ile il özel idareleri ve belediyelere ait vergiler ve "
    "kaldırılan vergiler hakkında uygulanır; md. 2'ye göre gümrük idarelerince alınan vergi ve resimler bu Kanuna tabi "
    "değildir.")

P.q("VUK md. 3/A",
    "Bir vergi kanunu hükmünün lafzı, bir işlemin kapsama girip girmediği konusunda açık değildir."
    f"\n\n{V}, bu hükmün uygulanmasında aşağıdakilerden hangisi dikkate alınır?",
    "Hükmün konuluş maksadı ve kanundaki yeri",
    ["Mükellefin lehine olan sonuç",
     "İdarenin gelir ihtiyacı",
     "Kanunun yayımından sonraki yargı içtihatlarının tamamı",
     "Benzer işlemlere kıyasen uygulanan vergi"],
    "Md. 3/A'ya göre vergi kanunları lafzı ve ruhu ile hüküm ifade eder; lafzın açık olmadığı hâllerde hükümler, konuluşundaki "
    "maksat, kanunun yapısındaki yeri ve diğer maddelerle bağlantısı gözetilerek uygulanır.")

P.sayisal("VUK md. 6",
    "Bir vergi müfettişine, annesinin kardeşinin (dayısının) şirketinde vergi incelemesi yapma görevi verilmiştir."
    f"\n\n{V}, müfettişin hangi dereceye kadar kan hısımlarına ait vergi inceleme işleriyle uğraşması yasaktır?",
    "3", ["1", "2", "4", "5"],
    "Md. 6'ya göre md. 5'teki görevliler kan hısımlığında üçüncü derece (bu derece dahil) civar hısımlarına ait vergi inceleme "
    "ve takdir işleriyle uğraşamaz. Dayı üçüncü derece kan hısmıdır.", zorluk="hard")

P.q("VUK md. 3/B",
    f"Bir vergi incelemesinde mükellef, işlemlerinin gerçek mahiyetini çeşitli delillerle ispat etmek istemektedir.\n\n{V}, vergilendirmede ispata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gerçek mahiyet yemin dahil her delille ispatlanabilir.",
    ["Vergilendirmede vergiyi doğuran olayın gerçek mahiyeti esastır.",
     "Olayla ilgisi tabii ve açık olmayan şahit ifadesi ispat vasıtası olamaz.",
     "Olağan dışı bir durumu iddia eden taraf bunu ispatla yükümlüdür.",
     "İktisadi ve ticari icaplara uymayan durumlarda ispat külfeti iddia edene düşer."],
    "Md. 3/B'ye göre vergiyi doğuran olay ve buna ilişkin muamelelerin gerçek mahiyeti yemin hariç her türlü delille "
    "ispatlanabilir.", zorluk="easy")

P.q("VUK md. 3/B",
    "(JKL) A.Ş., piyasa değeri 5.000.000 ₺ olan bir gayrimenkulü ortağına 500.000 ₺’ye sattığını, bunun olağan bir işlem "
    f"olduğunu ileri sürmektedir.\n\n{V}, ispat yükü hakkında aşağıdakilerden hangisi doğrudur?",
    "İddia eden şirket ispatlamalıdır.",
    ["İspat yükü kural gereği vergi idaresindedir.",
     "Şirketin beyanı esas alınır, ispat gerekmez.",
     "İşlem sözleşmeye dayandığından sorgulanamaz.",
     "Sadece yemin ile ispat mümkündür."],
    "Md. 3/B'ye göre iktisadi, ticari ve teknik icaplara uymayan veya olayın özelliğine göre normal ve mutat olmayan bir "
    "durumun iddia olunması hâlinde ispat külfeti bunu iddia eden tarafa aittir.", zorluk="hard")

P.sayisal("6183 md. 102",
    "Bay (N)’nin vadesi 30 Haziran 2024 olan vergi borcu için hiçbir takip işlemi yapılmamıştır."
    f"\n\n{A}, bu alacak en geç hangi yılın sonunda tahsil zamanaşımıyla sona erer?",
    "2029", ["2027", "2028", "2030", "2034"],
    "Vergi alacağını sona erdiren sebeplerden biri zamanaşımıdır. 6183 md. 102'ye göre amme alacağı vadenin rastladığı yılı "
    "takip eden yıl başından itibaren beş yıl içinde tahsil edilmezse zamanaşımına uğrar: 2025-2029.")

P.q("VUK md. 3/B",
    f"Bir şirket, kira sözleşmesi şeklinde yaptığı ancak ekonomik olarak satış niteliği taşıyan işlemin nasıl vergilendirileceğini sormaktadır.\n\n{V}, vergilendirmede “gerçek mahiyet” ilkesi aşağıdakilerden hangisini ifade eder?",
    "Görünüş değil iktisadi gerçek esastır.",
    ["Sözleşmede yazan hukuki şekil esas alınır.",
     "Mükellefin beyanı kural olarak esas alınır.",
     "İdarenin ilk tespiti değiştirilemez.",
     "Tapuda gösterilen değer tartışılamaz."],
    "Md. 3/B'ye göre vergilendirmede vergiyi doğuran olay ve buna ilişkin muamelelerin gerçek mahiyeti esastır; işlemin "
    "görünen şekli değil ekonomik özü vergilendirilir.")

P.q("VUK md. 5",
    f"Bir mükellef, beyannamelerine ilişkin bilgilerin kimler tarafından gizli tutulması gerektiğini öğrenmek istemektedir.\n\n{V}, vergi mahremiyetine uymakla yükümlü olanlar arasında aşağıdakilerden hangisi yer almaz?",
    "Mükellefin kendi muhasebecisi",
    ["Vergi muameleleri ve incelemeleriyle uğraşan memurlar",
     "Vergi mahkemelerinde görevli olanlar",
     "Vergi kanunlarına göre kurulan komisyonlara katılanlar",
     "Vergi işlerinde kullanılan bilirkişiler"],
    "Md. 5'e göre vergi memurları, vergi yargısında görevli olanlar, vergi komisyonlarına katılanlar ve vergi işlerinde "
    "kullanılan bilirkişiler öğrendikleri sırları ifşa edemez. Mükellefin muhasebecisi bu maddenin muhatabı değildir; meslek "
    "sırrı kendi meslek mevzuatında düzenlenir.")

tk = 150_000 - 60_000
P.sayisal("6183 md. 23",
    "Bay (P)’nin vadesi gelmiş 150.000 ₺ vergi borcu bulunmaktadır. Aynı vergi dairesince daha önce tahsil edilen ve kanuni "
    f"sebeplerle kendisine iadesi gereken 60.000 ₺ bulunmaktadır.\n\n{A}, mahsup sonucu Bay (P)’nin ödemesi gereken vergi "
    "borcu kaç ₺’dir?",
    tl(tk), secenekler(tk, 150_000, 210_000, 60_000, 0),
    "6183 md. 23'e göre tahsil edilip de kanuni sebeplerle reddi gereken amme alacakları, istihkak sahibinin reddiyatı "
    "yapacak idareye olan muaccel borçlarına mahsup edilerek reddolunur: 150.000 − 60.000 = 90.000 ₺.")

P.q("VUK md. 5",
    "Uzun yıllar vergi müfettişi olarak çalışan Bay (R), emekli olduktan sonra görevi sırasında öğrendiği bir şirketin "
    f"ticari sırlarını kitabında yayımlamak istemektedir.\n\n{V}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Sır saklama yasağı görevden ayrıldıktan sonra da devam eder.",
    ["Emekli olduğu için sır saklama yükümlülüğü sona ermiştir.",
     "Şirket izin vermese de bilgiler bilimsel amaçla yayımlanabilir.",
     "Yasak sadece görev süresince geçerlidir.",
     "Beş yıl geçtikten sonra sırlar yayımlanabilir."],
    "Md. 5'e göre vergi mahremiyeti yasağı, sayılan kişiler görevlerinden ayrılsalar dahi devam eder.")

P.q("VUK md. 6",
    f"Bir vergi müfettişine, yakın akrabalarından birinin işlettiği şirkette inceleme yapma görevi verilmiştir; müfettiş görevi üstlenip üstlenemeyeceğini sormaktadır.\n\n{V}, vergi mahremiyetine tabi görevlilerin vergi inceleme ve takdir işleriyle uğraşamayacağı kişiler arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Dördüncü derece kan hısmı",
    ["Nişanlısı", "Boşanmış eşi", "Evlatlığı", "Kanuni temsilcisi veya vekili olduğu kişi"],
    "Md. 6'ya göre bu görevliler kendilerine, nişanlılarına, boşanmış olsalar bile eşlerine, usul ve füruuna, evlatlığına, kan "
    "hısımlığında üçüncü dereceye kadar civar hısımlarına ve temsilcisi veya vekili oldukları kişilere ait işlerle uğraşamaz.",
    zorluk="hard")

vg = 30_000 * 0.20
P.sayisal("VUK md. 9",
    "13 yaşındaki çocuk oyuncu (T), bir dizide rol almış ve kendisine 30.000 ₺ ücret ödenmiştir; işveren tevkifat "
    f"yapmıştır. (Tevkifat oranı %20 olarak alınacaktır.)\n\n{V}, (T)’nin ücreti üzerinden kesilecek vergi kaç ₺’dir?",
    tl(vg), secenekler(vg, 0, 30_000 * 0.15, 30_000 * 0.10, 30_000),
    "Md. 9'a göre mükellefiyet ve vergi sorumluluğu için kanuni ehliyet şart değildir; küçük olması vergilendirilmesine engel "
    "değildir: 30.000 × %20 = 6.000 ₺. Ödevler md. 10 gereği kanuni temsilcisince yerine getirilir.")

P.q("VUK md. 6",
    "Vergi mahkemesinde görevli bir hâkim, bir arkadaşının vergi beyannamesini ücret almadan hazırlamak istemektedir."
    f"\n\n{V}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Ücretsiz de olsa bu işi yapması yasaktır.",
    ["Ücret almadığı için yapabilir.",
     "Mahkeme başkanının izniyle yapabilir.",
     "Sadece mesai dışında yapabilir.",
     "Arkadaşı mükellef olduğu için yapabilir."],
    "Md. 6/2'ye göre vergi muameleleri ve incelemeleri ile vergi mahkemeleri, bölge idare mahkemeleri ve Danıştayda görevli "
    "olanlar, mükelleflerin vergi kanunlarının uygulanmasıyla ilgili hesap, yazı ve sair özel işlerini ücretsiz de olsa "
    "yapamaz.")

P.q("VUK md. 7",
    f"Bir yoklama memuru, bir köyde faaliyet gösteren mükellefin adresini tespit etmek için muhtar, jandarma ve belediyeden destek istemiş; bu kurumlar yardım yükümlülükleri bulunup bulunmadığını sormuştur.\n\n{V}, vergi kanunlarının uygulanmasında idarenin yardımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mülki amirler yardımla yükümlüdür.",
    ["Sadece vergi daireleri birbirine yardım eder.",
     "Yardım yükümlülüğü sadece mahkemelere aittir.",
     "Köy muhtarları yardım yükümlülüğü dışındadır.",
     "Emniyet amirlerinin yardım yükümlülüğü yoktur."],
    "Md. 7'ye göre mülkiye amirleri, emniyet amir ve memurları, belediye başkanları, köy muhtarları ve kamu müesseseleri "
    "vergi kanunlarının uygulanmasında ilgili memur ve komisyonlara kolaylık göstermeye ve yardımda bulunmaya mecburdur.")

yv = 500_000 * 0.25
P.sayisal("VUK md. 9",
    "Kaçak (yasadışı) olarak işlettiği bir yerden 500.000 ₺ kazanç elde ettiği tespit edilen (GHI) Ltd. Şti.’nin bu kazancı "
    f"üzerinden kurumlar vergisi hesaplanacaktır. (Kurumlar vergisi oranı %25 olarak alınacaktır.)\n\n{V}, bu kazanç "
    "üzerinden hesaplanacak vergi kaç ₺’dir?",
    tl(yv), secenekler(yv, 0, 500_000 * 0.20, 500_000 * 0.50, 500_000 * 0.15),
    "Md. 9'a göre vergiyi doğuran olayın kanunlarla yasak edilmiş olması mükellefiyeti ve vergi sorumluluğunu kaldırmaz: "
    "500.000 × %25 = 125.000 ₺.")

P.q("VUK md. 8",
    f"Bir işveren, çalışanlarının ücretinden kestiği vergiler bakımından kendisinin hukuki konumunu merak etmektedir.\n\n{V}, mükellef ve vergi sorumlusu kavramlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sorumlu, ödeme bakımından daireye karşı muhataptır.",
    ["Mükellef, vergiyi başkası adına ödeyen kişidir.",
     "Vergi sorumlusu vergi borcunun asıl sahibidir.",
     "Mükellef sadece tüzel kişiler için kullanılan bir kavramdır.",
     "Vergi sorumlusu sadece kamu kurumlarıdır."],
    "Md. 8'e göre mükellef, vergi kanunlarına göre kendisine vergi borcu terettüp eden gerçek veya tüzel kişidir; vergi "
    "sorumlusu, verginin ödenmesi bakımından alacaklı vergi dairesine karşı muhatap olan kişidir.")

P.q("VUK md. 8",
    "(MNO) A.Ş. ile kiracısı, kira sözleşmesine “kiraya ilişkin tüm vergileri kiracı ödeyecektir” şeklinde bir hüküm "
    f"koymuşlardır.\n\n{V}, bu sözleşme hükmünün vergi dairesi karşısındaki durumu nedir?",
    "Özel sözleşmeler vergi dairesini bağlamaz.",
    ["Sözleşme hükmü vergi dairesini de bağlar.",
     "Sözleşme noterde yapılmışsa vergi dairesini bağlar.",
     "Vergi dairesi kiracıyı mükellef kabul etmekle yükümlüdür.",
     "Sözleşme sadece kira stopajı için geçerlidir."],
    "Md. 8'e göre vergi kanunlarıyla kabul edilen hâller dışında, mükellefiyete veya vergi sorumluluğuna ilişkin özel "
    "sözleşmeler vergi dairelerini bağlamaz.")

P.sayisal("VUK md. 5",
    "Gelir İdaresi, vergi güvenliğini sağlamak amacıyla 2026 yılında verilen yıllık beyannamelere ait bazı bilgileri ilan "
    f"etmek istemektedir.\n\n{V}, bu ilan hangi yıl içinde yapılır?",
    "2026", ["2025", "2027", "2028", "2031"],
    "Md. 5'e göre gelir ve kurumlar vergisi mükelleflerinin beyannamelerinde gösterdikleri matrahlar ve bunlar üzerinden tarh "
    "olunan vergiler ile ad ve unvanları, beyannamelerin verildiği yıl içinde cetvellerle ilan olunur.", zorluk="hard")

P.q("VUK md. 9",
    f"Kısıtlı olan bir kişi adına kanuni temsilcisi kira geliri elde etmekte; kısıtlının vergi mükellefi olup olamayacağı ve ödevleri kimin yerine getireceği tartışılmaktadır.\n\n{V}, vergi ehliyetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mükellefiyet için medeni hakları kullanma ehliyeti şarttır.",
    ["Kısıtlılar da mükellef olabilir.",
     "Küçükler vergi mükellefi olabilir.",
     "Yasak bir faaliyetten kazanç elde edilmesi mükellefiyeti kaldırmaz.",
     "Küçüklerin ödevleri kanuni temsilcilerince yerine getirilir."],
    "Md. 9'a göre mükellefiyet ve vergi sorumluluğu için kanuni ehliyet şart değildir; vergiyi doğuran olayın kanunlarla "
    "yasaklanmış olması mükellefiyeti kaldırmaz.")

P.q("VUK md. 10",
    f"Borçları ödenmeden tasfiyeye giren bir anonim şirketin yönetim kurulu üyeleri, vergi borçlarından sorumluluklarını sormaktadır.\n\n{V}, kanuni temsilcilerin sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tasfiye, temsilcinin önceki sorumluluğunu kaldırır.",
    ["Temsilciler mükellefin ödevlerini yerine getirmekle yükümlüdür.",
     "Ödev yerine getirilmezse alınamayan vergi temsilcinin varlığından alınır.",
     "Temsilci ödediği vergi için asıl mükellefe rücu edebilir.",
     "Hüküm Türkiye’de bulunmayan mükelleflerin temsilcilerine de uygulanır."],
    "Md. 10'a göre tüzel kişilerin tasfiye hâline girmiş veya tasfiye edilmiş olmaları, kanuni temsilcilerin tasfiyeye giriş "
    "tarihinden önceki zamanlara ait sorumluluklarını kaldırmaz.")

br = 80_000 / 0.80 * 0.20
P.sayisal("VUK md. 11",
    "(ABC) A.Ş., bir serbest meslek erbabına yapacağı ödemede kesilmesi gereken vergiyi kendisi üstlenmiş ve serbest meslek "
    f"erbabına net 80.000 ₺ ödemiştir. (Tevkifat oranı %20 olarak alınacaktır.)\n\n{V}, şirketin vergi sorumlusu olarak "
    "yatıracağı vergi kaç ₺’dir?",
    tl(br), secenekler(br, 80_000 * 0.20, 25_000, 80_000 * 0.15, 100_000),
    "Md. 11'e göre vergi kesmeye mecbur olanlar verginin tam kesilip ödenmesinden sorumludur. Vergi üstlenildiğinden brüt "
    "tutar 80.000 / 0,80 = 100.000 ₺; kesilmesi gereken vergi 100.000 × %20 = 20.000 ₺'dir.", zorluk="hard")

P.q("VUK md. 10",
    "(PRS) Ltd. Şti. tasfiye edilerek ticaret sicilinden silinmiştir. Sonradan şirketin tasfiye öncesine ait vergi borcu "
    f"tespit edilmiştir.\n\n{V}, bu borca ilişkin tarhiyat kime yapılır?",
    "Kanuni temsilciler ve tasfiye memurları adına müteselsilen",
    ["Kimseye yapılamaz, borç sona erer.",
     "Şirketin son dönemde mal sattığı müşterilere oransal olarak",
     "Ticaret sicili müdürlüğüne",
     "Şirketin bağlı olduğu vergi dairesi müdürüne"],
    "Md. 10'a 7103 sayılı Kanunla eklenen fıkraya göre tasfiye edilerek ticaret sicilinden silinmiş mükelleflerin tasfiye "
    "öncesi ve tasfiye dönemlerine ilişkin tarhiyat ve ceza kesme işlemleri, müteselsilen sorumlu olmak üzere kanuni "
    "temsilciler ve tasfiye memurları adına yapılır.", zorluk="hard")

P.q("VUK md. 11",
    f"Bir şirket, yaptığı ödemelerden vergi kesme yükümlülüğünü yerine getirmediği için vergi dairesiyle uyuşmazlık yaşamaktadır.\n\n{V}, vergi kesenlerin sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi kesen, ödediği vergi için asıl mükellefe rücu edebilir.",
    ["Vergi kesen, kesmediği vergiden sorumlu tutulamaz.",
     "Vergi kesenin sorumluluğu asıl mükellefin borcunu tamamen ortadan kaldırır.",
     "Nihai tüketiciler de alım satımda müteselsilen sorumludur.",
     "Mal üreten çiftçiler de müteselsil sorumluluğa tabidir."],
    "Md. 11'e göre vergi kesmeye mecbur olanlar verginin tam kesilip ödenmesinden sorumludur; bu sorumluluk asıl mükellefe "
    "rücu hakkını kaldırmaz. Müteselsil sorumluluk mal üreten çiftçiler ile nihai tüketiciler için söz konusu değildir.",
    zorluk="hard")

mh = 90_000 - 70_000
P.sayisal("6183 md. 23",
    "Bayan (R)’ye kanuni sebeplerle iadesi gereken 90.000 ₺ vardır. Aynı vergi dairesine vadesi gelmiş 70.000 ₺ vergi "
    f"borcu bulunmaktadır.\n\n{A}, mahsup işleminden sonra Bayan (R)’ye nakden iade edilecek tutar kaç ₺’dir?",
    tl(mh), secenekler(mh, 90_000, 70_000, 160_000, 0),
    "6183 md. 23'e göre reddi gereken amme alacakları istihkak sahibinin aynı idareye olan muaccel borçlarına mahsup edilerek "
    "reddolunur: 90.000 − 70.000 = 20.000 ₺ nakden iade edilir.")

P.q("VUK md. 11",
    "Bir şirket, hizmet aldığı ve kendisiyle hısımlık ilişkisi bulunan bir firmaya yaptığı ödemeden kesmesi gereken vergiyi "
    f"kesmemiştir.\n\n{V}, bu verginin ödenmesinden kimler sorumlu tutulabilir?",
    "İşlemin tarafları müteselsilen sorumlu tutulabilir.",
    ["Sadece hizmeti veren firma sorumludur.",
     "Kimse sorumlu tutulamaz, vergi terkin edilir.",
     "Sadece şirketin ortakları sorumludur.",
     "Sadece vergi dairesi memuru sorumludur."],
    "Md. 11'e göre vergi kesintisi yapmak zorunda olanların yükümlülüklerini yerine getirmemesi hâlinde verginin ödenmesinden, "
    "alım satıma taraf olanlar, hizmetten yararlananlar ve aralarında doğrudan veya dolaylı ilişki bulunanlar müteselsilen "
    "sorumludur.")

P.q("VUK md. 12",
    f"Vergi borcu bulunan bir tüccar vefat etmiş; mirasçılarından biri mirası reddetmiş, diğerleri kabul etmiştir.\n\n{V}, mükellefin ölümü hâlinde vergi ödevlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mirası reddeden de borçtan sorumludur.",
    ["Ödevler kanuni ve mansup mirasçılara geçer.",
     "Mirasçılar miras hisseleri oranında sorumludur.",
     "Mirası reddetmeyen mirasçılar ödevlerden sorumludur.",
     "Ölüm hâlinde vergi cezaları düşer."],
    "Md. 12'ye göre ölüm hâlinde mükellefin ödevleri mirası reddetmemiş kanuni ve mansup mirasçılarına geçer ve her mirasçı "
    "miras hissesi oranında sorumludur; md. 372'ye göre ölümle vergi cezası düşer.")

mc = 500_000 / 2
P.sayisal("VUK md. 12, 372",
    "Ölen mükellef Bay (S)’nin 500.000 ₺ vergi borcu ile 100.000 ₺ vergi ziyaı cezası bulunmaktadır. İki mirasçısı eşit "
    f"hisseye sahiptir ve mirası reddetmemiştir.\n\n{V}, mirasçılardan birinin sorumlu olduğu toplam tutar kaç ₺’dir?",
    tl(mc), secenekler(mc, 300_000, 600_000, 500_000, 50_000),
    "Md. 12'ye göre mirasçılar vergi borcundan miras hisseleri oranında sorumludur: 500.000 / 2 = 250.000 ₺. Md. 372'ye göre "
    "ölüm hâlinde vergi cezası düştüğünden 100.000 ₺ ceza mirasçılara geçmez.", zorluk="hard")

P.q("VUK md. 19",
    f"Bir mükellef, vergi borcunun ihbarname kendisine ulaşmadan önce doğup doğmadığını sormaktadır; mükellefe göre borç ancak tebliğle doğmaktadır.\n\n{V}, vergi alacağının doğumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergiyi doğuran olayın vukuu ile doğar.",
    ["Vergi dairesinin tarh işlemiyle doğar.",
     "Vergi ihbarnamesinin tebliğiyle doğar.",
     "Verginin tahsil edilmesiyle doğar.",
     "Mükellefin beyannameyi imzalamasıyla doğar."],
    "Md. 19'a göre vergi alacağı, vergi kanunlarının vergiyi bağladıkları olayın vukuu veya hukuki durumun tekemmülü ile "
    "doğar; vergi alacağı mükellef bakımından vergi borcunu teşkil eder.")

P.q("Vergi alacağının sona ermesi",
    "Bir vergi hukuku dersinde, vergi borcunu sona erdiren sebepler tartışılmaktadır."
    f"\n\n{V} ve {A}, aşağıdakilerden hangisi vergi borcunu sona erdiren sebeplerden biri değildir?",
    "Borcun tecil edilmesi",
    ["Ödeme", "Tahsil zamanaşımının dolması", "Terkin", "Mahsup"],
    "Vergi borcu ödeme (mahsup dahil), zamanaşımı ve terkin gibi yollarla sona erer. Tecil (6183 md. 48) borcun ödeme süresini "
    "uzatır, borcu sona erdirmez.", zorluk="hard")

P.sayisal("VUK md. 10",
    "(DEF) Ltd. Şti. tasfiye edilerek ticaret sicilinden silinmiştir. Tasfiye öncesi döneme ait 300.000 ₺ vergi tarh "
    "edilecektir. Şirketin kanuni temsilcisi ve tasfiye memuru olmak üzere iki sorumlusu vardır."
    f"\n\n{V}, vergi dairesi bu kişilerden birinden en fazla kaç ₺ talep edebilir?",
    tl(300_000), secenekler(300_000, 150_000, 100_000, 0, 600_000),
    "Md. 10'a göre sicilden silinmiş mükelleflerin tasfiye öncesi ve tasfiye dönemlerine ilişkin tarhiyatı, müteselsilen "
    "sorumlu olmak üzere kanuni temsilciler ve tasfiye memurları adına yapılır; müteselsil sorumlulukta alacağın tamamı "
    "sorumlulardan herhangi birinden istenebilir.", zorluk="hard")

P.q("VUK md. 113",
    f"Borcu ödenmeden uzun süre geçen bir mükellef, vergi dairesinin artık tarhiyat yapamayacağını ileri sürmekte, ancak bu konuda vergi dairesine herhangi bir başvuruda bulunmamıştır.\n\n{V}, zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mükellefin başvurusu aranmaksızın hüküm ifade eder.",
    ["Sadece mükellefin talebiyle uygulanır.",
     "Vergi mahkemesi kararıyla uygulanır.",
     "Sadece usulsüzlük cezalarında uygulanır.",
     "Zamanaşımı vergi alacağını ortadan kaldırmaz."],
    "Md. 113'e göre zamanaşımı, süre geçmesi suretiyle vergi alacağının kalkmasıdır ve mükellefin bu hususta bir müracaatı "
    "olup olmadığına bakılmaksızın hüküm ifade eder.")

P.q("6183 md. 23",
    f"Bir mükellefin fazla ödediği vergi kanuni sebeplerle iade edilecektir; aynı mükellefin aynı idareye vadesi gelmiş başka vergi borçları da bulunmakta ve iadenin nasıl yapılacağı sorulmaktadır.\n\n{A}, reddi gereken amme alacaklarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Muaccel borçlara mahsup edilerek reddolunur.",
    ["Borçlunun her türlü şahsi alacağına mahsup edilir.",
     "Sadece belediye vergilerinde mahsup yapılabilir.",
     "Mahsup vergi borcunu sona erdirmez.",
     "Mahsup için mahkeme kararı gerekir."],
    "6183 md. 23'e göre tahsil edilip de kanuni sebeplerle reddi icap eden amme alacakları, istihkak sahiplerinin reddiyatı "
    "yapacak amme idaresine olan muaccel borçlarına mahsup edilmek suretiyle reddolunur; mahsup edilen kısım için borç "
    "sona erer.")

P.sayisal("VUK md. 114",
    "Bay (U)’nun 2021 yılında doğan vergi alacağı için vergi dairesi takdir komisyonuna başvurmuş ve komisyon kararı 18 ay "
    f"sonra vergi dairesine tevdi edilmiştir.\n\n{V}, bu verginin tarh zamanaşımı en geç hangi yılın sonunda dolar?",
    "2027", ["2026", "2028", "2025", "2029"],
    "Md. 114'e göre normal süre 2022-2026'dır; takdir komisyonuna başvuru zamanaşımını durdurur ancak işlemeyen süre bir "
    "yıldan fazla olamaz. 18 aylık bekleme bir yılla sınırlandığından süre 2027 yılı sonuna uzar.", zorluk="hard")

P.q("VUK md. 4",
    f"Yeni işe başlayan bir mükellef, vergi işlemlerinde muhatap olacağı vergi dairesinin görevlerini ve hangi işlemleri yapmaya yetkili olduğunu öğrenmek istemektedir.\n\n{V}, vergi dairesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tespit, tarh, tahakkuk ve tahsil eden dairedir.",
    ["Sadece vergi cezası kesen dairedir.",
     "Sadece vergi mahkemesi kararlarını uygulayan dairedir.",
     "Vergi incelemesi yapan müfettişlerin bağlı olduğu kuruldur.",
     "Mükellefin kendi seçtiği dairedir."],
    "Md. 4'e göre vergi dairesi mükellefi tespit eden, vergi tarh eden, tahakkuk ettiren ve tahsil eden dairedir; "
    "mükelleflerin bağlı olacakları vergi dairesi kanunlarla ve Bakanlık düzenlemeleriyle belirlenir.")

P.oncul("VUK md. 8-12",
    f"{V} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Mükellefiyet için kanuni ehliyet şart değildir.",
     "Özel sözleşmeler vergi dairesini bağlar.",
     "Ölüm hâlinde ödevler mirası reddetmemiş mirasçılara geçer.",
     "Vergi kesenin sorumluluğu asıl mükellefe rücu hakkını kaldırır."],
    "Yukarıdakilerden hangileri doğrudur?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 9'a göre kanuni ehliyet şart değildir (I) ve md. 12'ye göre ödevler mirası reddetmemiş mirasçılara geçer (III). Md. "
    "8'e göre özel sözleşmeler vergi dairesini bağlamaz (II yanlış); md. 11'e göre vergi kesenin rücu hakkı saklıdır (IV "
    "yanlış).", zorluk="hard")

P.sayisal("6183 md. 102-103",
    "Vadesi 2021 yılında olan bir amme alacağı için borçluya 2023 yılında ödeme emri tebliğ edilmiş, başka işlem "
    f"yapılmamıştır.\n\n{A}, bu alacak en geç hangi yılın sonunda zamanaşımına uğrar?",
    "2028", ["2026", "2027", "2029", "2031"],
    "6183 md. 103'e göre ödeme emri tebliği zamanaşımını keser ve süre kesilmenin rastladığı yılı takip eden yıl başından "
    "itibaren yeniden işler: 2024-2028.")

P.q("Vergi hukuku ilkeleri",
    f"Bir vergi dairesi, kanunda açıkça düzenlenmemiş bir işleme benzer bir hükmü uygulayarak vergi istemek "
    f"istemektedir.\n\n{V}, vergi kanunlarının yorumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi kanunları lafzı ve ruhu ile hüküm ifade eder.",
    ["Vergi kanunları sadece lafzi yorumla uygulanır.",
     "Kıyas yoluyla vergi istisnası genişletilebilir.",
     "İdare kanunda olmayan bir vergi yükünü yorumla getirebilir.",
     "Vergi kanunlarında amaçsal yorum yasaktır."],
    "VUK md. 3/A'ya göre vergi kanunları lafzı ve ruhu ile hüküm ifade eder; lafız açık değilse konuluş maksadı ve sistematik "
    "yeri dikkate alınır. Kanunilik ilkesi gereği yorum veya kıyasla vergi yükü getirilemez.")

P.q("VUK md. 5",
    "Bir gazeteci, vergi dairesinde çalışan bir memurdan ünlü bir iş insanının vergi borcu hakkında bilgi istemiştir."
    f"\n\n{V}, memurun bu bilgiyi vermesi hakkında aşağıdakilerden hangisi doğrudur?",
    "Vergi mahremiyeti gereği bilgiyi açıklayamaz.",
    ["Kamuoyunu ilgilendirdiği için açıklayabilir.",
     "Gazeteci basın kartı gösterirse açıklayabilir.",
     "Sadece borç tutarını açıklayabilir.",
     "Amirinin sözlü izniyle açıklayabilir."],
    "Md. 5'e göre vergi muameleleri ve incelemeleriyle uğraşan memurlar, görevleri dolayısıyla öğrendikleri mükellefe ait "
    "sırları veya gizli kalması gereken hususları ifşa edemez.", zorluk="easy")

P.q("Anayasa md. 73",
    "Bir belediye meclisi, kanunda öngörülmeyen yeni bir “çevre katkı payı”nı meclis kararıyla işletmelerden almaya karar "
    f"vermiştir.\n\n{AY}, bu karar hakkında aşağıdakilerden hangisi doğrudur?",
    "Kanunsuz mali yükümlülük konulamaz.",
    ["Belediyeler kendi gelirleri için yükümlülük koyabilir.",
     "Meclis kararı kanun hükmündedir.",
     "Katkı payı vergi sayılmadığından kanun gerekmez.",
     "Valilik onayıyla uygulanabilir."],
    "Anayasa md. 73/3'e göre vergi, resim, harç ve benzeri mali yükümlülükler kanunla konulur, değiştirilir veya kaldırılır; "
    "kanuni dayanağı olmayan mali yükümlülük getirilemez.", zorluk="hard")

P.q("VUK md. 3/B",
    f"Bir vergi incelemesinde inceleme elemanı ve mükellef, farklı delillere dayanarak iddialarını ispat etmeye çalışmaktadır.\n\n{V}, aşağıdakilerden hangisi vergilendirmede ispat aracı olarak kullanılamaz?",
    "Olayla ilgisi tabii ve açık olmayan şahit ifadesi",
    ["Ticari defter kayıtları", "Fatura ve belgeler", "Bankalardan alınan hesap hareketleri ve ödeme dekontları", "Yoklama tutanakları"],
    "Md. 3/B'ye göre vergiyi doğuran olay yemin hariç her türlü delille ispatlanabilir; ancak olayla ilgisi tabii ve açık "
    "bulunmayan şahit ifadesi ispat vasıtası olarak kullanılamaz.")

P.q("VUK md. 10",
    "Türkiye’de bulunmayan yabancı bir şirketin Türkiye’deki temsilcisi, şirket adına beyanname vermemiş ve vergi şirket "
    f"varlığından tahsil edilememiştir.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Temsilciden alınır; şirkete rücu edilebilir.",
    ["Yabancı şirketin temsilcisi kural gereği sorumlu tutulamaz.",
     "Vergi terkin edilir.",
     "Vergi sadece yabancı ülkedeki merkezden istenebilir.",
     "Temsilci sadece usulsüzlük cezasından sorumludur."],
    "Md. 10'a göre kanuni temsilcilerin sorumluluğuna ilişkin hüküm Türkiye'de bulunmayan mükelleflerin Türkiye'deki "
    "temsilcileri hakkında da uygulanır; temsilciler ödedikleri vergiler için asıl mükelleflere rücu edebilir.", zorluk="hard")

P.q("VUK md. 8",
    f"Yurt dışından dönerek Türkiye’de iş kurmak isteyen bir kişi, vergi numarası alma yükümlülüğünü ve bu numaranın hangi işlemlerde kullanılacağını araştırmaktadır.\n\n{V}, vergi numarasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her gerçek ve tüzel kişiye bir vergi numarası verilir.",
    ["Vergi numarası sadece tüzel kişilere verilir.",
     "Vergi numarası sadece ticari kazanç sahiplerine verilir.",
     "Vergi numarası her yıl yenilenir.",
     "Vergi numarası kullanımı sadece beyannamelerde yer alır."],
    "Md. 8'e göre Türkiye Cumhuriyeti tabiyetindeki her gerçek kişi ile tüzel kişilere bir vergi numarası verilir; Bakanlık "
    "vergi numarasının kayıt ve belgelerde kullanılmasını zorunlu kılmaya yetkilidir.")

P.q("Vergi hukuku ilkeleri",
    f"Bir mükellef, kendisinden daha yüksek gelirli olanların daha yüksek oranda vergilendirilmesinin eşitliğe aykırı "
    f"olduğunu ileri sürmektedir.\n\n{AY}, vergilendirmede eşitlik ilkesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aynı durumdakiler aynı yüke tabi tutulur.",
    ["Tüm mükelleflerden aynı tutarda vergi alınır.",
     "Mali güç farkı vergilendirmede dikkate alınamaz.",
     "Artan oranlı tarife eşitlik ilkesine aykırıdır.",
     "Eşitlik ilkesi sadece kurumlar vergisinde uygulanır."],
    "Anayasa md. 10 ve 73 çerçevesinde eşitlik, aynı durumdakilerin aynı, farklı durumdakilerin mali güçlerine göre farklı "
    "vergilendirilmesini ifade eder; artan oranlı tarife mali güç ilkesinin aracıdır.")

P.q("VUK md. 11",
    "Bir tüccar, mal üreten çiftçiden yaptığı alımda kesmesi gereken vergiyi kesmemiştir. Vergi dairesi, kesilmeyen verginin "
    "tahsili için işlemin tarafları arasında sorumluların belirlenmesini istemektedir."
    f"\n\n{V}, müteselsil sorumluluk bakımından aşağıdakilerden hangisi doğrudur?",
    "Mal üreten çiftçi müteselsil sorumlu tutulmaz.",
    ["Çiftçi, tüccarla birlikte müteselsilen sorumludur.",
     "Sadece çiftçi sorumlu tutulur.",
     "Tüccarın sorumluluğu ortadan kalkar.",
     "Vergi alıcı nihai tüketiciden istenir."],
    "Md. 11'e göre vergi kesintisi yükümlülüğünü yerine getirmeyenlerle birlikte işlemin taraflarının müteselsil sorumluluğu, "
    "mal üreten çiftçiler ile nihai tüketiciler için söz konusu değildir.", zorluk="hard")

P.q("VUK md. 3/A",
    "Bir vergi kanunu hükmünün lafzı açık ve tereddütsüzdür; ancak mükellef, hükmün amacının farklı olduğunu ileri sürerek "
    f"lafza aykırı bir uygulama talep etmektedir.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Lafız açık olduğundan hüküm lafzına göre uygulanır.",
    ["Mükellefin talebi doğrultusunda amaca göre uygulanır.",
     "Vergi dairesi hükmü uygulamaktan kaçınabilir.",
     "Hüküm kıyasen başka bir maddeye göre uygulanır.",
     "Uyuşmazlık uzlaşma komisyonunca yorumlanır."],
    "Md. 3/A'ya göre vergi kanunları lafzı ve ruhu ile hüküm ifade eder; ancak konuluş maksadı, sistematik yer ve bağlantılar "
    "lafzın açık olmadığı hâllerde dikkate alınır.")

P.q("VUK md. 8, 11",
    f"Bir vergi dairesi, beyannamesini kendisi veren mükellefler ile başkası adına vergi kesip ödeyenleri ayrı listelerde izlemekte ve bu iki grubun hukuki konumlarını karşılaştırmaktadır.\n\n{V}, aşağıdakilerden hangisi vergi sorumlusuna örnektir?",
    "Çalışanının ücretinden vergi kesen işveren",
    ["Kendi ticari kazancı için beyanname veren tüccar",
     "Emlak vergisini ödeyen konut sahibi",
     "Motorlu taşıtlar vergisini ödeyen araç sahibi",
     "Kurumlar vergisi beyannamesi veren şirket"],
    "Md. 8'e göre vergi sorumlusu, verginin ödenmesi bakımından vergi dairesine karşı muhatap olan kişidir; md. 11'e göre "
    "yaptığı ödemelerden vergi kesmeye mecbur olan işveren tipik vergi sorumlusudur. Diğerleri kendi vergileri bakımından "
    "mükelleftir.")

P.q("Anayasa md. 73",
    f"Bir belediye, gelirlerini artırmak için yeni bir mali yükümlülük getirmenin hukuki yolunu araştırmaktadır.\n\n{AY}, kanunla konulması gereken mali yükümlülükler arasında aşağıdakilerden hangisi yer alır?",
    "Vergi, resim ve harçlar ile benzeri yükümlülükler",
    ["Sadece gelir ve kurumlar vergisi",
     "Sadece belediyelerin kendi bütçelerine gelir kaydettiği vergiler",
     "Sadece gümrük vergileri",
     "Sadece dolaysız vergiler"],
    "Anayasa md. 73/3'e göre vergi, resim, harç ve benzeri mali yükümlülükler kanunla konulur, değiştirilir veya kaldırılır.",
    zorluk="easy")

P.q("VUK md. 1",
    f"Kaldırılmış bir harca ilişkin eski bir uyuşmazlıkta hangi usul hükümlerinin uygulanacağı tartışılmaktadır.\n\n{V}, Kanunun uygulanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaldırılan vergiler hakkında Kanun hükümleri uygulanmaz.",
    ["Genel bütçeye giren vergilerde uygulanır.",
     "İl özel idarelerine ait vergilerde uygulanır.",
     "Belediyelere ait vergi, resim ve harçlarda uygulanır.",
     "Bu vergi, resim ve harçlara bağlı olan vergi, resim ve zamlarda da uygulanır."],
    "Md. 1'e göre Kanun genel bütçeye giren vergiler ile il özel idarelerine ve belediyelere ait vergi, resim ve harçlar ve "
    "bunlara bağlı zamlar hakkında uygulanır; Kanunun hükümleri kaldırılan vergi, resim ve harçlar hakkında da uygulanır.")

P.q("Vergi hukuku ilkeleri",
    f"Bir stajyer meslek mensubu, vergi borcu ilişkisinde alacaklı ve borçlu tarafların kimler olduğunu "
    f"incelemektedir.\n\n{V}, vergi borcu ilişkisinin taraflarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Alacaklı taraf vergi alacağı hakkı olan kamu idaresidir.",
    ["Alacaklı taraf vergiyi ödeyen mükelleftir.",
     "Vergi borcu ilişkisinde sadece tek taraf vardır.",
     "Borçlu taraf her durumda vergi dairesidir.".replace("her durumda ", "kural olarak "),
     "Vergi sorumlusu vergi alacaklısıdır."],
    "Vergi borcu ilişkisinde alacaklı taraf vergi alacağı hakkına sahip kamu idaresi (Devlet, il özel idaresi, belediye), "
    "borçlu taraf ise mükellef ve kanunda öngörülen hâllerde vergi sorumlusudur (VUK md. 8).", zorluk="easy")

P.q("VUK md. 9",
    "Kaçak (ruhsatsız) olarak kumarhane işleten Bay (Y), faaliyetin yasadışı olduğunu, bu nedenle vergilendirilemeyeceğini "
    f"ileri sürmektedir.\n\n{V}, bu iddia hakkında aşağıdakilerden hangisi doğrudur?",
    "Faaliyetin yasak olması mükellefiyeti kaldırmaz.",
    ["Yasadışı faaliyet vergilendirilemez.",
     "Sadece ceza mahkemesi kararından sonra vergilendirilir.",
     "Yasadışı kazanç sadece müsadere edilir, vergilendirilmez.",
     "Bay (Y) mükellef değil, vergi sorumlusudur."],
    "Md. 9'a göre vergiyi doğuran olayın kanunlarla yasak edilmiş bulunması mükellefiyeti ve vergi sorumluluğunu kaldırmaz.")

if __name__ == "__main__":
    sys.exit(P.yaz())
