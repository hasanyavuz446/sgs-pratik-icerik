# -*- coding: utf-8 -*-
"""Meslek Hukuku · Mesleki Sorumluluklar — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü):
  · Çalışma Usul ve Esasları Yön. m. 4-10, 21, 28 (genel mesleki standartlar, sır, bağımsızlık)
  · SMMM ve YMM'lerce Tutulacak Defter ve Kayıtlar ile Bildirim Mecburiyeti Hakkında Yön.
  · 3568 s. Kanun m. 12, 43, 44
  · 213 s. VUK mükerrer m. 227, m. 153/A, 359, 360 (7524 s. Kanunla 2024 değişikliği işlenmiş)
  · 5549 s. Suç Gelirlerinin Aklanmasının Önlenmesi Hakkında Kanun m. 3, 4, 7, 8, 10, 13, 14
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_mesleki_sorumluluk_2026.json", lesson="meslek_hukuku", topic="mesleki_sorumluluk",
          konu_adi="Mesleki Sorumluluklar", seed=2026092807,
          surum="Çalışma Usul ve Esasları Yön., Defter ve Kayıtlar Yön., 3568 s. Kanun, 213 s. VUK (2024), 5549 s. Kanun; 28.09.2026 kontrolü")

CU = "Serbest Muhasebeci Mali Müşavir ve Yeminli Mali Müşavirlerin Çalışma Usul ve Esasları Hakkında Yönetmelik’e göre"
DK = "Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirlerce Tutulacak Defter ve Kayıtlar ile Meslek Mensuplarının Bildirim Mecburiyeti Hakkında Yönetmelik’e göre"
K = "3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu’na göre"
V = "213 sayılı Vergi Usul Kanunu’na göre"
A = "5549 sayılı Suç Gelirlerinin Aklanmasının Önlenmesi Hakkında Kanun’a göre"

# ================================================================ genel mesleki standartlar
P.q("Çalışma Usul ve Esasları Yön. m. 4-10",
    f"{CU}, aşağıdakilerden hangisi “genel mesleki standartlar” başlığı altında düzenlenen ilkelerden biri değildir?",
    "Asgari ücret tarifesinin belirlenmesi",
    ["Meslek unvanı ile yeterlilik ilkesi", "Dürüstlük, güvenilirlik ve tarafsızlık",
     "Sır saklama", "Bağımsızlık"],
    "Çalışma Usul ve Esasları Yönetmeliği'nin “Genel Mesleki Standartlar” kısmı (m. 4-10) unvan ile yeterlilik, mesleki "
    "eğitim ve bilgi, dürüstlük-güvenilirlik-tarafsızlık, sır saklama, sorumluluk, bağımsızlık ve haksız rekabet "
    "ilkelerini düzenler. Asgari ücret tarifesi ayrı yönetmelikle düzenlenir.",
    zorluk="easy")

P.q("Çalışma Usul ve Esasları Yön. m. 6",
    f"{CU}, dürüstlük, güvenilirlik ve tarafsızlık ilkesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müşterinin çıkarı gerektirirse çıkar çatışmasına girilebilir.",
    ["Dürüstlük, güvenilirlik ve tarafsız olma şartı mesleğin temelini oluşturur.",
     "Mesleki başarı dürüstlük, güvenilirlik ve tarafsızlıkla mümkündür.",
     "Meslek mensupları çalışmaları sırasında çıkar çatışmalarından uzak kalır.",
     "Meslek mensupları görevlerini sürdürürken mesleki özen ve titizliği gösterir."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 6'ya göre meslek mensupları çıkar çatışmalarından uzak kalır ve gereken "
    "mesleki özen ve titizliği gösterir; dürüstlük, güvenilirlik ve tarafsızlık mesleğin temelidir.")

P.q("Çalışma Usul ve Esasları Yön. m. 7; 3568 s. Kanun m. 43",
    f"{CU}, sır saklama yükümlülüğüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sır saklama yükümlülüğü faaliyete son verilince biter.",
    ["Yükümlülük meslek mensuplarının yanında çalışanları da kapsar.",
     "Adli yargıya göre suç oluşturan hâllerin yetkili mercilere duyurulması mecburidir.",
     "Adli veya idari inceleme ve soruşturmalar sır saklama hükmünün dışındadır.",
     "Tanıklık sırrın ifşası sayılmaz."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 7'ye göre meslek mensupları ve yanlarında çalışanlar öğrendikleri bilgi ve "
    "sırları mesleki faaliyetlerine son verseler bile ifşa edemez. Suçun bildirilmesi, adli-idari inceleme istisnası ve "
    "tanıklık aynı maddede ve Kanun m. 43'te yer alır.")

P.q("Çalışma Usul ve Esasları Yön. m. 8",
    f"{CU}, meslek mensuplarının sorumluluk türleri ile içerikleri aşağıdaki eşleştirmelerden hangisinde yanlış verilmiştir?",
    "Meslektaşlara karşı sorumluluk – Müşteri bilgilerini meslektaşlarla paylaşmak",
    ["Sosyal sorumluluk – Mesleği ifa ederken topluma ve Devlete karşı sorumluluk taşımak",
     "İşletme sahip ve yöneticilerine karşı sorumluluk – İsabetli karar için doğru ve güvenilir bilgi sağlamak",
     "Meslektaşlara karşı sorumluluk – Mesleki eğitimde birbirine bilgi aktarmak ve dayanışmak",
     "Sosyal sorumluluk – Mesleki faaliyetin kamu yararı gözetilerek yürütülmesi"],
    "Çalışma Usul ve Esasları Yönetmeliği m. 8/c'ye göre meslektaşlara karşı sorumluluk, ilgili yönetmelikler çerçevesinde "
    "ve mesleki eğitimde birbirine bilgi vermek, aktarmak ve dayanışmaktır; müşteri bilgilerinin paylaşılması sır saklama "
    "yükümlülüğüne aykırıdır.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 10",
    "SMMM (A), başka bir meslek mensubuyla sözleşmesi devam eden (B) Ltd. Şti.'ye, sözleşme bitmeden daha düşük ücretle "
    f"defter tutma hizmeti vermeyi teklif etmiştir. {CU}, bu davranış hangi ilkeye aykırıdır?",
    "Haksız rekabet yasağına",
    ["Sır saklama yükümlülüğüne", "Meslek unvanı ile yeterlilik ilkesine",
     "Mesleki eğitim ve bilgi ilkesine", "Hukuki sorumluluk hükmüne"],
    "Çalışma Usul ve Esasları Yönetmeliği m. 10'a göre meslek mensupları başka bir meslek mensubu ile mesleki sözleşmesi "
    "devam eden kişilere mesleki hizmet vermeye girişemez; bu davranış haksız rekabettir.",
    zorluk="easy")

P.q("Çalışma Usul ve Esasları Yön. m. 28",
    f"{CU}, meslek mensuplarının işlerini yaptıkları kişiler için tutacakları dosyalara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her müşteri için düzenli dosya tutulur; çalışma kâğıtları burada saklanır.",
    ["Dosya tutulması ihtiyaridir; müşteri talep ederse dosya açılır.",
     "Dosyalar her yıl sonunda müşteriye teslim edilir ve meslek mensubunda kopya kalmaz.",
     "Dosyalar oda tarafından tutulur; meslek mensubu dosya düzeninden sorumlu değildir.",
     "Dosyada sözleşme ve fatura örnekleri dışında belge saklanmaz."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 28'e göre meslek mensupları işlerini yaptığı gerçek ve tüzel kişiler için "
    "düzenli dosya tutmak zorundadır; bu dosyalarda çalışma kâğıtları, yazışmalar ve diğer lüzumlu bilgiler saklanır.")

P.q("Defter ve Kayıtlar Yön. m. 6",
    f"{DK}, meslek mensuplarının kendilerine gelen ve kendilerinin gönderdiği mesleki yazışmaları kaydedecekleri defter aşağıdakilerden hangisidir?",
    "Gelen-giden evrak defteri",
    ["Yevmiye defteri", "Envanter defteri", "Müşteri cari hesap takip defteri", "Karar defteri"],
    "Defter ve Kayıtlar Yönetmeliği m. 6'ya göre meslek mensupları mesleki faaliyetleriyle ilgili gelen ve giden her türlü "
    "yazıyı gelen-giden evrak defterine kaydeder; defterlere yazışmanın ilgili olduğu dosya sayısı yazılır.",
    zorluk="easy")

P.q("Defter ve Kayıtlar Yön. m. 7",
    f"{DK}, dosya düzenine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dosyalar her müşteri için yıllara bağlı olmaksızın tek numarayla izlenir.",
    ["Dosyalara yıl başından sonuna kadar teselsül eden numaralar verilir.",
     "Her mesleki faaliyet konusu için ayrı bir çalışma dosyası açılır.",
     "Genel konularla ilgili yazılar ayrıca dosyalanır.",
     "Başka meslek mensuplarınca istenilen işlemler için de ayrı dosya açılır."],
    "Defter ve Kayıtlar Yönetmeliği m. 7'ye göre dosyalara yıl başından sonuna kadar teselsül eden numaralar verilir; her "
    "mesleki faaliyet konusu için ayrı çalışma dosyası açılır, genel yazılar ve başka meslek mensuplarının istediği "
    "işlemler için ayrı dosya tutulur.")

P.q("Defter ve Kayıtlar Yön. m. 10",
    f"{DK}, yeminli mali müşavirlerin tasdik işlemleriyle ilgili düzenleyecekleri tutanaklarda aşağıdakilerden hangisinin bulunması zorunlu değildir?",
    "Tasdik ücretinin tutarı",
    ["Bilgi verenin kimliği", "Tutanağın düzenlendiği yer",
     "Tutanağın düzenlendiği tarih", "Bilgi verenin ve YMM'nin imzası"],
    "Defter ve Kayıtlar Yönetmeliği m. 10'a göre tasdikle ilgili tutanaklarda bilgi verenin kimliği, düzenlendiği yer ve "
    "tarih bulunur; tutanaklar bilgi verenler ve YMM tarafından imzalanıp mühürlenir. Ücret tutarı sayılmamıştır.")

P.q("Defter ve Kayıtlar Yön. m. 11",
    f"{DK}, meslek mensuplarının yazışmalarına verecekleri sayılarda aşağıdakilerden hangisi yer almaz?",
    "Müşterinin vergi kimlik numarası",
    ["Meslek mensubunun kısaltılmış unvanı", "Meslek mensubunun sicil numarası",
     "Giden evrak defteri sıra numarası", "Meslek mensubunun unvan kısaltması ile sicil bilgisi"],
    "Defter ve Kayıtlar Yönetmeliği m. 11'e göre yazışma sayılarında meslek mensubunun kısaltılmış unvanı, sicil numarası "
    "ve giden evrak defteri sıra numarası yer alır; müşterinin vergi kimlik numarası sayılmamıştır.")

P.q("Defter ve Kayıtlar Yön. m. 13",
    f"{DK}, aşağıdakilerden hangisi meslek mensuplarının düzenledikleri rapor türleri arasında sayılmamıştır?",
    "Vergi inceleme raporu",
    ["Özet standart denetim raporu", "Tasdik raporu", "Özel amaçlı rapor", "Yardımcı rapor"],
    "Defter ve Kayıtlar Yönetmeliği m. 13'e göre meslek mensupları özet standart rapor, tasdik raporu, özel amaçlı rapor ve "
    "yardımcı rapor düzenler. Vergi inceleme raporu vergi inceleme elemanlarınca düzenlenir.")

P.q("Defter ve Kayıtlar Yön. m. 13",
    f"{DK}, mali analiz, denetleme ve tasdik işlemleri sırasında başka meslek mensuplarınca düzenlenen teknik ve mali raporlar aşağıdakilerden hangisidir?",
    "Yardımcı raporlar",
    ["Özel amaçlı raporlar", "Özet standart raporlar", "Tasdik raporları", "Dönemsel raporlar"],
    "Defter ve Kayıtlar Yönetmeliği m. 13'e göre yardımcı raporlar mali analiz, denetleme ve tasdik işlemleri sırasında "
    "başka meslek mensuplarınca düzenlenmiş teknik ve mali raporlardır; denetim ve tasdik raporlarında bunlardaki bilgiler "
    "esas alınır.")

P.q("Defter ve Kayıtlar Yön. m. 14",
    f"{DK}, raporlama ilkelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Rapor ekleri raporun parçası sayılmaz ve ayrıca teslim edilir.",
    ["Raporlarda düzenleme amacı belirtilmelidir.",
     "Yardımcı, ayrıntılı ve özet raporlar birbiriyle ilişkili ve uyumlu olmalıdır.",
     "Raporlar kısa sürede hazırlanmalı ve belirli standartlara bağlanmalıdır.",
     "Raporların dili maliye ve muhasebe dili olmalıdır."],
    "Defter ve Kayıtlar Yönetmeliği m. 14'e göre rapor ekleri raporun parçasıdır ve tüm örneklerine eklenir; raporların "
    "alınıp verilmesi tutanakla veya rapor örneğine konulan şerhle yapılır.")

P.q("Defter ve Kayıtlar Yön. m. 16",
    f"{DK}, iş sahibi firmanın daha önce yapılan tasdik işine ait rapordan örnek istemesi hâlinde aşağıdakilerden hangisi uygulanır?",
    "Örnek, ücret tarifesindeki ücretin %1'i karşılığında onaylanıp verilir.",
    ["Örnek ücretsiz verilir ve asıl rapor yerine geçmez.",
     "Örnek, ücret tarifesindeki ücretin %10'u karşılığında verilir.",
     "Örnek verilemez; firmanın yeni bir tasdik raporu düzenletmesi gerekir.",
     "Örnek, oda onayı alınarak ücret tarifesindeki ücretin yarısı karşılığında verilir."],
    "Defter ve Kayıtlar Yönetmeliği m. 16'ya göre iş sahibi firmalar önceki raporlardan örnek isteyebilir; örnekler ücret "
    "tarifesindeki ücretin %1'i karşılığında onaylanıp verilir ve tasdikli rapor örnekleri asılları gibi işlem görür.")

P.q("Defter ve Kayıtlar Yön. m. 8 ve 9",
    f"{DK}, aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yazışmalarda meslek mensubunun imzası aranmaz; büro kaşesi yeterlidir.",
    ["Yönetmelik gereği düzenlenen tutanak ve raporlar da gelen-giden evrak defterine yazılır.",
     "Yazışmalar hizmet sunulan firmaya, üçüncü kişilere ve kuruluşlara gönderilen yazılar ile gelen cevaplardır.",
     "Yazışmaların meslek mensubunun imzasını ve varsa mührünü taşıması gerekir.",
     "Meslek mensupları ilgili kanunlardaki defter, belge ve kayıt düzenlerine uyar."],
    "Defter ve Kayıtlar Yönetmeliği m. 9'a göre yazışmaların meslek mensubunun imzasını ve varsa mührünü taşıması gerekir. "
    "Diğer ifadeler m. 5, 8 ve 9'da yer alır.")

# ================================================================ VUK
P.q("VUK mük. m. 227",
    f"{V}, Hazine ve Maliye Bakanlığının beyannamelerin meslek mensuplarınca imzalanmasına ilişkin yetkisi aşağıdakilerden hangisinde doğru olarak verilmiştir?",
    "İmza mecburiyetini beyanname ve mükellef grupları itibarıyla ayrı uygulatabilir.",
    ["İmza mecburiyeti Kanunla getirilmiş olup Bakanlığın düzenleme yetkisi bulunmamaktadır.",
     "Bakanlık, beyannamelerin yeminli mali müşavirlere imzalatılmasını zorunlu kılamaz.",
     "İmza mecburiyeti bütün mükellefler için tek tip olarak getirilebilir, ayrım yapılamaz.",
     "İmza mecburiyeti ancak kurumlar vergisi mükellefleri için getirilebilir."],
    "VUK mükerrer m. 227'ye göre Bakanlık, vergi beyannamelerinin 3568 sayılı Kanuna göre yetkili meslek mensuplarınca da "
    "imzalanması mecburiyetini getirmeye ve bunu beyanname çeşitleri, mükellef grupları ve faaliyet konuları itibarıyla "
    "ayrı ayrı uygulatmaya yetkilidir.")

P.q("VUK mük. m. 227",
    "SMMM (C)'nin imzaladığı KDV beyannamesindeki bilgiler, mükellefin defter kayıtlarına ve belgelerine uygun "
    f"olmadığından vergi ziyaı doğmuştur. {V}, (C)'nin sorumluluğu aşağıdakilerden hangisidir?",
    "Vergi, ceza ve faizden mükellefle müteselsilen sorumludur.",
    ["Vergi aslından sorumlu değildir; kesilecek cezanın yarısından sorumludur.",
     "Sorumluluğu, beyanname ücretinin iadesiyle sınırlıdır.",
     "Mükelleften tahsil edilemeyen kısım için ikinci derecede sorumludur.",
     "Sorumluluğu, oda tarafından verilecek disiplin cezasıyla sınırlıdır."],
    "VUK mükerrer m. 227'ye göre beyannameyi imzalayan meslek mensupları, beyannamedeki bilgilerin defter kayıtlarına ve "
    "dayanağı belgelere uygun olmamasından doğan vergi ziyaına bağlı olarak salınacak vergi, ceza ve gecikme "
    "faizlerinden mükellefle birlikte müştereken ve müteselsilen sorumludur.",
    zorluk="hard")

P.q("VUK mük. m. 227 (7338 s. Kanunla değişik)",
    f"{V}, bir haktan yararlanılması YMM tasdik raporu şartına bağlanan konularda raporun zamanında ibraz edilmemesi hâlinde aşağıdakilerden hangisi uygulanır?",
    "60 günlük mühlet verilir; yine verilmezse haktan yararlanılamaz.",
    ["Mükellef haktan yararlanır, ancak usulsüzlük cezası kesilir.",
     "Mükellefe 15 günlük mühlet verilir; ibraz edilmezse rapor aranmadan hak kullandırılır.",
     "Rapor bir sonraki yılın beyannamesiyle birlikte ibraz edilebilir.",
     "Rapor zamanında verilmezse hak kalıcı olarak kaybedilir ve mühlet verilmez."],
    "VUK mükerrer m. 227'ye göre tasdik raporunun zamanında ibrazı şarttır; zamanında ibraz edilmezse mükellefe tebliğ "
    "edilmek şartıyla 60 günlük mühlet verilir, bu sürede de ibraz edilmezse mükellef tasdike konu haktan yararlanamaz.",
    zorluk="hard")

P.q("VUK m. 360",
    f"{V}, 359. maddede yazılı kaçakçılık suçlarının işlenişine iştirak eden ve bu suçların işlenmesinde menfaati bulunmayan suç ortağı hakkında aşağıdakilerden hangisi uygulanır?",
    "TCK'nın iştirak hükümlerine göre verilecek cezanın yarısı indirilir.",
    ["Ceza verilmez; vergi ziyaı cezası kesilmesiyle yetinilir.",
     "Verilecek cezanın üçte biri indirilir.",
     "Verilecek ceza bir kat artırılır.",
     "Ceza, mükellefe verilen cezayla aynı olur ve indirim yapılmaz."],
    "VUK m. 360'a göre 359. maddede yazılı suçların işlenişine iştirak eden suç ortaklarının bu suçların işlenmesinde "
    "menfaatinin bulunmaması hâlinde TCK'nın iştirak hükümlerine göre verilecek cezanın yarısı indirilir.")

P.q("VUK m. 359/a",
    "SMMM (D), müşterisinin defterlerine, gerçek bir satışı miktar itibarıyla gerçeğe aykırı gösteren muhteviyatı itibarıyla "
    f"yanıltıcı faturayı bilerek kaydetmiştir. {V}, bu fiil için öngörülen hapis cezası aşağıdakilerden hangisidir?",
    "On sekiz aydan beş yıla kadar",
    ["Üç aydan bir yıla kadar", "Bir yıldan üç yıla kadar", "Üç yıldan sekiz yıla kadar", "Beş yıldan on yıla kadar"],
    "VUK m. 359/a-2'ye göre muhteviyatı itibarıyla yanıltıcı belge düzenleyenler veya kullananlar hakkında on sekiz aydan "
    "beş yıla kadar hapis cezasına hükmolunur. Sahte belge düzenleme veya kullanma (m. 359/b) üç yıldan sekiz yıla kadar "
    "hapis gerektirir.",
    zorluk="hard")

P.q("VUK m. 153/A",
    f"{V}, sahte belge nedeniyle mükellefiyeti terkin edilenlerin fiillerine iştirak ettiği inceleme raporuyla tespit edilen ve bu durumu kesinleşen 3568 sayılı Kanun kapsamındaki meslek mensubu hakkında aşağıdakilerden hangisi uygulanır?",
    "Üç yıl süreyle geçici olarak mesleki faaliyetten alıkoyma cezası uygulanır.",
    ["Beş yıl süreyle meslekten men cezası verilir ve ruhsatı iptal edilir.",
     "Bir yıl süreyle geçici olarak mesleki faaliyetten alıkoyma cezası uygulanır.",
     "Kınama cezası verilir ve durumu oda internet sitesinde ilan edilir.",
     "Meslek mensubunun beyanname imzalama yetkisi süresiz olarak kaldırılır."],
    "VUK m. 153/A'ya göre bu durumda meslek mensubu hakkında üç yıl süreyle geçici olarak mesleki faaliyetten alıkoyma "
    "cezası uygulanır ve 3568 sayılı Kanundaki usuller tatbik edilir. Aynı hüküm Disiplin Yönetmeliği m. 7'nin son "
    "fıkrasında da yer alır.")

P.q("VUK m. 362",
    f"{V}, vergi mahremiyetine uymaya mecbur olan kimselerden bu mahremiyeti ihlal edenler hakkında hangi hüküm uygulanır?",
    "Türk Ceza Kanunu’nun 239. maddesi hükümlerine göre cezalandırılırlar.",
    ["Vergi ziyaı cezası kesilir ve ceza üç kat uygulanır.",
     "Özel usulsüzlük cezası kesilmekle yetinilir.",
     "Disiplin cezası verilir; ceza hükümleri uygulanmaz.",
     "Türk Ticaret Kanunu’nun haksız rekabet hükümleri uygulanır."],
    "VUK m. 362'ye göre vergi mahremiyetine uymaya mecbur olan kimselerden bu mahremiyeti ihlal edenler TCK m. 239 "
    "hükümlerine göre cezalandırılır.")

# ================================================================ 3568: tasdik sorumluluğu
P.q("3568 s. Kanun m. 12/4",
    f"{K}, yeminli mali müşavirin yaptığı tasdikin doğru olmaması hâlindeki sorumluluğunun sınırı aşağıdakilerden hangisidir?",
    "Tasdikin kapsamı",
    ["Tasdik ücretinin tutarı", "Mükellefin bir yıllık cirosu",
     "Mükellefin ödenmemiş vergi borcunun yarısı", "Oda tarafından belirlenen azami tutar"],
    "Kanun m. 12/4'e göre YMM'ler tasdikin doğruluğundan sorumludur; tasdik doğru değilse tasdikin kapsamı ile sınırlı "
    "olmak üzere ziyaa uğratılan vergiler ve kesilecek cezalardan mükellefle birlikte müştereken ve müteselsilen sorumlu "
    "olurlar.",
    zorluk="easy")

P.q("3568 s. Kanun m. 43",
    f"{K}, meslek mensuplarının çeşitli kanunlarla muhbirlere tanınan hak ve menfaatlere ilişkin durumu aşağıdakilerden hangisidir?",
    "Bu hak ve menfaatlerden, yaptıkları ihbarlar için de faydalanamazlar.",
    ["Bu hak ve menfaatlerden odaya bildirmek koşuluyla faydalanabilirler.",
     "Bu hak ve menfaatlerden, müşterileri dışındaki kişileri ihbar ettiklerinde faydalanabilirler.",
     "Bu hak ve menfaatlerin yarısından faydalanabilirler.",
     "Bu hak ve menfaatlerden ancak YMM'ler faydalanabilir."],
    "Kanun m. 43'e göre meslek mensupları ve yanlarında çalışanlar işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa "
    "edemez ve çeşitli kanunlarla muhbirlere tanınan hak ve menfaatlerden faydalanamaz.")

# ================================================================ 5549
P.q("5549 s. Kanun m. 3",
    f"{A}, yükümlülerin müşterinin tanınması kapsamında işlem yapılmadan önce yapması gereken aşağıdakilerden hangisidir?",
    "Tarafların ve hesabına işlem yapılanların kimliğini tespit etmek",
    ["İşlem tutarını vergi dairesine bildirip onay almak",
     "Müşterinin son üç yıllık gelir vergisi beyannamelerini incelemek",
     "İşlem yapanların adli sicil kaydını savcılıktan istemek",
     "İşlemi Mali Suçları Araştırma Kurulu Başkanlığına önceden bildirmek"],
    "5549 sayılı Kanun m. 3'e göre yükümlüler kendileri nezdinde yapılan veya aracılık ettikleri işlemlerde işlem "
    "yapılmadan önce, işlem yapanlar ile nam veya hesaplarına işlem yapılanların kimliklerini tespit etmek ve gerekli "
    "diğer tedbirleri almak zorundadır.")

P.q("5549 s. Kanun m. 4",
    f"{A}, şüpheli işlem bildirimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yükümlü, bildirimde bulunduğunu işleme taraf olan müşterisine yazılı olarak haber verir.",
    ["İşleme konu malvarlığının yasa dışı elde edildiğine dair şüphe varsa bildirim zorunludur.",
     "Bildirim, yapılmaya teşebbüs edilen işlemler için de gereklidir.",
     "Bildirimde bulunulduğu, denetim elemanları ve mahkemeler dışında kimseye açıklanamaz.",
     "Hangi faaliyetlerden dolayı bildirim yapılacağı yönetmelikle belirlenir."],
    "5549 sayılı Kanun m. 4/2'ye göre yükümlüler Başkanlığa şüpheli işlem bildiriminde bulunduklarını, yükümlülük "
    "denetimi elemanları ile yargılama sırasında mahkemeler dışında, işleme taraf olanlar dahil hiç kimseye açıklayamaz.",
    zorluk="hard")

P.sayisal("5549 s. Kanun m. 8",
    f"{A}, yükümlüler kimlik tespitine ilişkin belgeleri son işlem tarihinden itibaren kaç yıl süreyle muhafaza etmekle yükümlüdür?",
    "8", ["3", "5", "10", "15"],
    "5549 sayılı Kanun m. 8'e göre yükümlüler belgeleri düzenleme tarihinden, defter ve kayıtları son kayıt tarihinden, "
    "kimlik tespitine ilişkin belgeleri son işlem tarihinden itibaren sekiz yıl süreyle muhafaza eder ve istenirse ibraz "
    "eder.")

P.q("5549 s. Kanun m. 7",
    "Mali Suçları Araştırma Kurulu Başkanlığı denetim elemanı, SMMM (E)'den bir müşterisine ait defter kayıtlarını "
    f"istemiştir. (E), meslek sırrı gerekçesiyle bilgi vermekten kaçınmak istemektedir. {A}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Özel kanunlardaki sır hükümleri ileri sürülerek kaçınılamaz.",
    ["3568 sayılı Kanun m. 43'teki sır saklama yükümlülüğü gereği bilgi verilmez.",
     "Bilgi, müşterinin yazılı onayı alınmadıkça verilemez.",
     "Bilgi ancak mahkeme kararıyla istenebilir; denetim elemanına verilmez.",
     "Bilgi, oda yönetim kurulunun izniyle verilebilir."],
    "5549 sayılı Kanun m. 7'ye göre gerçek ve tüzel kişiler Başkanlık ve denetim elemanlarınca istenen her türlü bilgi ve "
    "belgeyi vermekle yükümlüdür ve savunma hakkına ilişkin hükümler saklı kalmak kaydıyla özel kanunlardaki hükümleri "
    "ileri sürerek bilgi vermekten kaçınamaz. 3568 sayılı Kanun m. 43 de adli ve idari soruşturmaları sır saklama "
    "yükümlülüğünün dışında tutar.",
    zorluk="hard")

P.q("5549 s. Kanun m. 14",
    f"{A}, şüpheli işlem bildiriminde bulunulduğunu açıklama yasağı ile bilgi-belge verme ve muhafaza yükümlülüklerini ihlal eden kimse hakkında öngörülen ceza aşağıdakilerden hangisidir?",
    "Bir yıldan üç yıla kadar hapis ve beş bin güne kadar adli para cezası",
    ["Altı aydan bir yıla kadar hapis cezası",
     "Üç yıldan beş yıla kadar hapis ve on bin güne kadar adli para cezası",
     "Yüz güne kadar adli para cezası",
     "Beş yıldan on yıla kadar hapis cezası"],
    "5549 sayılı Kanun m. 14'e göre m. 4'ün ikinci fıkrası ile m. 7 ve 8'deki yükümlülükleri ihlal eden kimse bir yıldan üç "
    "yıla kadar hapis ve beş bin güne kadar adli para cezası ile cezalandırılır.",
    zorluk="hard")

P.oncul("Çalışma Usul ve Esasları Yön. m. 7; 3568 s. Kanun m. 43",
    "Bir meslek mensubunun müşterisine ilişkin aşağıdaki açıklamaları değerlendirilmektedir:",
    ["Vergi müfettişinin yürüttüğü inceleme kapsamında istenen bilgileri vermesi",
     "Mahkemede tanık olarak dinlenirken bildiklerini anlatması",
     "Müşterisinin rakibine müşterinin fiyat politikasını anlatması",
     "Müşterisinin suç teşkil eden bir fiilini yetkili mercie bildirmesi"],
    f"{CU}, yukarıdakilerden hangileri sır saklama yükümlülüğünün ihlali sayılmaz?",
    "I, II ve IV",
    ["Yalnız IV", "I ve II", "I, II ve IV", "II ve III", "I, III ve IV"],
    "Çalışma Usul ve Esasları Yönetmeliği m. 7 ve Kanun m. 43'e göre adli veya idari inceleme ve soruşturmalar sır saklama "
    "hükmünün dışındadır, tanıklık sırrın ifşası sayılmaz ve suç oluşturan hâllerin yetkili mercilere duyurulması "
    "mecburidir. Rakibe bilgi vermek ihlaldir.",
    zorluk="hard")

P.oncul("Defter ve Kayıtlar Yön. m. 13",
    "Meslek mensuplarının düzenlediği raporlarla ilgili aşağıdaki ifadeler verilmiştir:",
    ["Tasdik raporları kazıntısız, silintisiz ve açık ifadelerle düzenlenir.",
     "Dönemsel raporlar özel amaçlı raporlardandır.",
     "Özet standart denetim raporu ayrıntılı denetim raporundan yararlanılarak düzenlenir.",
     "Yardımcı raporlardaki bilgiler denetim ve tasdik raporlarında dikkate alınmaz."],
    f"{DK}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Defter ve Kayıtlar Yönetmeliği m. 13'e göre tasdik raporları kazıntısız ve silintisiz düzenlenir; dönemsel raporlar "
    "özel amaçlı raporlardandır; özet standart rapor ayrıntılı rapordan yararlanılarak düzenlenir. Yardımcı raporlardaki "
    "bilgiler ise denetim ve tasdik raporlarında esas alınır.",
    zorluk="hard")

P.oncul("5549 s. Kanun m. 3, 4, 8 ve 10",
    "5549 sayılı Kanun kapsamında yükümlü olan bir meslek mensubuna ilişkin aşağıdaki ifadeler verilmiştir:",
    ["İşlem yapılmadan önce müşterinin kimliğini tespit eder.",
     "Şüpheli işlem bildiriminde bulunduğunu müşterisine açıklayabilir.",
     "Kimlik tespitine ilişkin belgeleri son işlem tarihinden itibaren sekiz yıl saklar.",
     "Yükümlülüğünü yerine getirdiği için hukuki ve cezai bakımdan sorumlu tutulamaz."],
    f"{A}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV",
    ["Yalnız I", "I ve III", "I, III ve IV", "II ve IV", "II, III ve IV"],
    "5549 sayılı Kanun m. 3'e göre kimlik tespiti işlemden önce yapılır; m. 8'e göre kimlik belgeleri son işlemden itibaren "
    "sekiz yıl saklanır; m. 10'a göre yükümlülüğünü yerine getirenler sorumlu tutulamaz. M. 4/2'ye göre bildirim "
    "yapıldığı müşteriye açıklanamaz.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 4 ve 5",
    f"{CU}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Mesleki bilgi eğitimle geliştirilir; bu eğitim çalışmalarını Birlik ve odalar yürütür.",
    ["Mesleki eğitim çalışmaları üniversitelerce yürütülür ve Birliğin görevi değildir.",
     "Meslek unvanını alanlar yeterliliği kanıtlamış sayıldığından eğitim yükümlülüğü yoktur.",
     "Meslek mensupları unvanlarının gerektirdiği saygı ve güveni koruma yükümlülüğü taşımaz.",
     "Mesleki eğitim çalışmaları vergi idaresi tarafından düzenlenir."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 4'e göre meslek mensupları unvanlarının gerektirdiği saygı ve güvene yakışır "
    "şekilde hareket eder; m. 5'e göre mesleki bilgi mesleki konularda eğitim yapılarak geliştirilir ve bu eğitim Birlik ve "
    "odalarca yürütülür.")

P.q("Etik İlkeler Birinci Kısım m. 10; Çalışma Usul Yön. m. 6",
    "SMMM (F), yeni tanıştığı bir holdinge ait karmaşık konsolidasyon işini, bu alanda deneyimi olmadığı hâlde kabul etmiş ve "
    "işi uzman desteği almadan eksik yürütmüştür. Aşağıdakilerden hangisi (F)'nin ihlal ettiği ilkedir?",
    "Mesleki yeterlilik ve özen",
    ["Gizlilik", "Bağımsızlık", "Haksız rekabet yasağı", "Reklam yasağı"],
    "Etik İlkeler Birinci Kısım m. 10'a göre mesleki yeterlilik ve özen, etkin hizmet için gerekli bilgi ve beceri "
    "düzeyine sahip olmayı ve standartlara uygun özenli davranmayı gerektirir; Çalışma Usul ve Esasları Yönetmeliği m. 6 "
    "da gereken mesleki özen ve titizliği arar.")

P.q("Çalışma Usul ve Esasları Yön. m. 41; VUK mük. m. 227",
    f"{V} ve Çalışma Usul ve Esasları Yönetmeliği’ne göre, yeminli mali müşavirlerin tasdik raporlarında belirtmesi gereken aşağıdakilerden hangisidir?",
    "Tasdikin kapsamı",
    ["Mükellefin önceki meslek mensubunun adı", "Tasdik ücretinin tutarı",
     "Mükellefin banka hesapları", "Oda disiplin sicili"],
    "Çalışma Usul ve Esasları Yönetmeliği m. 41 ve Kanun m. 12'ye göre YMM'ler yaptıkları tasdikin kapsamını raporda "
    "açıkça belirtir; mali sorumlulukları da tasdikin kapsamıyla sınırlıdır.")

P.q("3568 s. Kanun m. 8/A; VUK mük. m. 227",
    f"{V} ve 3568 sayılı Kanun’a göre, aşağıdaki meslek mensubu–sorumluluk eşleştirmelerinden hangisi yanlıştır?",
    "Beyannameyi imzalayan SMMM – Mükelleften tahsil edilemeyen vergi için ikinci derecede sorumluluk",
    ["Beyannameyi imzalayan SMMM – Belgeye aykırılıktan doğan vergi, ceza ve faizden müteselsil sorumluluk",
     "Tasdik raporu düzenleyen YMM – Tasdikin kapsamıyla sınırlı müteselsil sorumluluk",
     "KDV iade raporu düzenleyen SMMM – Rapor kapsamıyla sınırlı müteselsil sorumluluk",
     "Tasdik raporu düzenleyen YMM – Mali ve disiplin sorumluluğunun ayrı raporlarla tespiti"],
    "VUK mükerrer m. 227'ye göre beyannameyi imzalayan meslek mensubu mükellefle birlikte müştereken ve müteselsilen "
    "sorumludur; ikinci derecede (tali) sorumluluk öngörülmemiştir. Diğer eşleştirmeler Kanun m. 8/A ve 12 ile uyumludur.",
    zorluk="hard")

P.q("Defter ve Kayıtlar Yön. m. 1-3",
    f"{DK}, Yönetmeliğin dayanağı aşağıdakilerden hangisidir?",
    "3568 sayılı Kanunun 50/j maddesi",
    ["213 sayılı VUK'un 227. maddesi", "6102 sayılı TTK'nın 64. maddesi",
     "3568 sayılı Kanunun 45. maddesi", "5549 sayılı Kanunun 3. maddesi"],
    "Defter ve Kayıtlar Yönetmeliği m. 3'e göre Yönetmelik, 3568 sayılı Kanunun meslek mensuplarınca tutulacak defter ve "
    "kayıtlar ile bunların bildirim mecburiyetinin yönetmelikle düzenleneceğini öngören 50/j maddesine dayanır.")

P.q("3568 s. Kanun m. 43; 5549 s. Kanun m. 4",
    "SMMM (G), müşterisinin kasasından yapılan yüksek tutarlı nakit işlemlerin yasa dışı bir kaynaktan geldiğinden "
    f"şüphelenmektedir. {A}, 5549 sayılı Kanun kapsamında yükümlü olan (G)'nin izleyeceği yol aşağıdakilerden hangisidir?",
    "Şüpheli işlemi Başkanlığa bildirir ve bildirimi müşteriye açıklamaz.",
    ["Sır saklama yükümlülüğü gereği durumu kimseye bildirmez.",
     "Müşteriyi uyarır; işlem tekrarlanırsa oda yönetim kuruluna bildirir.",
     "Durumu vergi dairesine bildirir ve müşteriye bilgi verir.",
     "Sözleşmeyi fesheder; bildirim yükümlülüğü sözleşmeyle sona erer."],
    "5549 sayılı Kanun m. 4'e göre işleme konu malvarlığının yasa dışı elde edildiğine dair şüphe varsa yükümlü bunu "
    "Başkanlığa bildirir ve bildirimde bulunduğunu işleme taraf olanlar dahil kimseye açıklayamaz. Kanun m. 43 de suç "
    "oluşturan hâllerin yetkili mercilere duyurulmasını sır saklamanın istisnası sayar.",
    zorluk="hard")

P.q("VUK m. 359/b",
    f"{V}, belgelerin asıl veya suretlerini tamamen veya kısmen sahte olarak düzenleyenler için öngörülen hapis cezası aşağıdakilerden hangisidir?",
    "Üç yıldan sekiz yıla kadar",
    ["On sekiz aydan beş yıla kadar", "Bir yıldan üç yıla kadar", "İki yıldan beş yıla kadar", "Beş yıldan on iki yıla kadar"],
    "VUK m. 359/b'ye göre defter, kayıt ve belgeleri yok edenler veya belgelerin asıl veya suretlerini tamamen veya kısmen "
    "sahte olarak düzenleyen ya da kullananlar üç yıldan sekiz yıla kadar hapis cezası ile cezalandırılır.")

P.q("Çalışma Usul ve Esasları Yön. m. 20",
    f"{CU}, meslek mensuplarının müşterileriyle düzenledikleri sözleşmelere ilişkin bildirim yükümlülüğü aşağıdakilerden hangisidir?",
    "Sözleşme bilgilerini Birliğin belirlediği usulle bağlı oldukları odalara iletirler.",
    ["Sözleşme örneklerini her yıl vergi dairesine elden teslim ederler.",
     "Sözleşmeleri noterde onaylatıp Birlik Genel Kuruluna sunarlar.",
     "Sözleşme bilgilerini, müşteri izin verirse odaya iletirler.",
     "Sözleşme bildirimini müşterinin kendisi yapar; meslek mensubunun yükümlülüğü yoktur."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 20'ye göre meslek mensupları hizmet verdikleri müşterilerle düzenledikleri "
    "sözleşmelerin bilgilerini Birliğin belirlediği usul ve esaslar çerçevesinde bağlı oldukları odalara iletmekle "
    "yükümlüdür.")

P.q("Çalışma Usul ve Esasları Yön. m. 10/3",
    f"{CU}, haksız rekabet kapsamında meslek mensuplarının birbirlerine zarar verecek davranışlarda bulunamayacakları konular aşağıdakilerin hangisinde birlikte verilmiştir?",
    "Ücret ve eleman temini",
    ["Tabela ve kartvizit", "Mesleki yayın ve internet sitesi", "Aidat ve bağış", "Tasdik ve denetim"],
    "Çalışma Usul ve Esasları Yönetmeliği m. 10'a göre meslek mensupları haksız rekabete neden olacak davranışlardan "
    "kaçınır; sözleşmesi devam eden kişilere hizmet vermeye girişemez ve ücret ve eleman temini gibi konularda "
    "birbirlerine zarar verecek davranışlarda bulunamaz.")

P.q("VUK mük. m. 227/2",
    f"{V}, Hazine ve Maliye Bakanlığının vergi kanunlarındaki bazı hükümlerden yararlanılmasını YMM tasdik raporu ibrazı şartına bağlayabileceği konular arasında aşağıdakilerden hangisi sayılmamıştır?",
    "Elektronik beyanname",
    ["Muafiyet", "İstisna", "Yeniden değerleme", "Geçmiş yıl zararlarının mahsubu"],
    "VUK mükerrer m. 227/2'ye göre Bakanlık muafiyet, istisna, yeniden değerleme, zarar mahsubu ve benzeri hükümlerden "
    "yararlanılmasını belirlediği şartlara uygun olarak YMM'lerce düzenlenmiş tasdik raporu ibrazı şartına bağlayabilir.")

P.q("VUK mük. m. 227",
    f"{V}, mükerrer 227. madde hükümlerinin uygulanmadığı kuruluşlar aşağıdakilerden hangisidir?",
    "Kamu iktisadi teşebbüsleri",
    ["Halka açık anonim şirketler", "Serbest bölgede faaliyet gösteren şirketler",
     "Kooperatifler", "Yabancı sermayeli limited şirketler"],
    "VUK mükerrer m. 227'nin son fıkrasına göre 233 sayılı Kanun Hükmünde Kararname hükümlerine tabi kamu iktisadi "
    "teşebbüsleri ile bunlara ait müesseseler hakkında bu madde hükümleri uygulanmaz.")

P.q("VUK m. 359/a",
    f"{V}, aşağıdaki durumlardan hangisi 359. madde bakımından “gizleme” olarak kabul edilir?",
    "Noterce tasdiki sabit defterlerin incelemede ibraz edilmemesi",
    ["Defterlerin muhasebe bürosunda değil işletmenin merkezinde saklanması",
     "Defterlerin tasdikinin yeni hesap dönemine ait süre içinde yaptırılması",
     "Belgelerin elektronik ortamda arşivlenerek saklanması",
     "Defterlerin inceleme elemanına tutanakla ve gecikmeden teslim edilmesi"],
    "VUK m. 359/a'ya göre varlığı noter tasdik kayıtları veya sair suretlerle sabit olduğu hâlde inceleme sırasında "
    "defter ve belgelerin vergi incelemesine yetkili kimselere ibraz edilmemesi, bu fıkra hükmünün uygulanmasında "
    "gizleme olarak kabul edilir.")

P.q("VUK m. 359",
    f"{V}, sahte belge ile muhteviyatı itibarıyla yanıltıcı belge arasındaki ayrım aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Gerçek işlem yokken düzenlenen sahte; gerçek işlemi miktarca gerçeğe aykırı gösteren yanıltıcıdır.",
    ["Gerçek işlemi miktarca gerçeğe aykırı gösteren sahte; gerçek işlem yokken düzenlenen yanıltıcıdır.",
     "Elektronik ortamda düzenlenen sahte, kâğıt ortamında düzenlenen yanıltıcıdır.",
     "Tutarı yüksek olan sahte, tutarı düşük olan yanıltıcı belgedir.",
     "Mükellefin düzenlediği sahte, meslek mensubunun düzenlediği yanıltıcı belgedir."],
    "VUK m. 359'a göre gerçek bir muamele veya durum olmadığı hâlde bunlar varmış gibi düzenlenen belge sahte belgedir; "
    "gerçek bir muamele veya duruma dayanmakla birlikte bunu mahiyet veya miktar itibarıyla gerçeğe aykırı yansıtan belge "
    "muhteviyatı itibarıyla yanıltıcı belgedir.",
    zorluk="hard")

P.q("VUK m. 359 (7394 s. Kanunla ek fıkra)",
    f"{V}, kaçakçılık fiilleriyle ziyaa uğratılan verginin, gecikme faizi ve zammının tamamı ile kesilen cezaların yarısının soruşturma evresinde ödenmesi hâlinde verilecek hapis cezası nasıl etkilenir?",
    "Ceza yarı oranında indirilir.",
    ["Ceza üçte bir oranında indirilir.", "Hapis cezası verilmez.",
     "Ceza dörtte bir oranında indirilir.", "Ceza ertelenir; indirim yapılmaz."],
    "VUK m. 359'a 7394 sayılı Kanunla eklenen fıkraya göre gerekli tutarların soruşturma evresinde ödenmesi hâlinde "
    "verilecek ceza yarı oranında, kovuşturma evresinde hüküm verilinceye kadar ödenmesi hâlinde üçte bir oranında "
    "indirilir.",
    zorluk="hard")

P.q("VUK m. 359",
    f"{V}, 371. maddedeki pişmanlık şartlarına uygun olarak durumu ilgili makamlara bildirenler hakkında 359. madde bakımından aşağıdakilerden hangisi doğrudur?",
    "359. madde hükmü uygulanmaz.",
    ["359. maddedeki ceza yarı oranında uygulanır.",
     "Hapis cezası adli para cezasına çevrilir.",
     "359. madde uygulanır, ancak vergi ziyaı cezası kesilmez.",
     "Ceza, meslek mensubu için iki kat uygulanır."],
    "VUK m. 359'a göre 371. maddedeki pişmanlık şartlarına uygun olarak durumu ilgili makamlara bildirenler hakkında bu "
    "madde hükmü uygulanmaz.")

P.q("5549 s. Kanun m. 6",
    f"{A}, yükümlülerin “devamlı bilgi verme” yükümlülüğü aşağıdakilerden hangisini ifade eder?",
    "Belirlenen tutarı aşan işlemleri Başkanlığa bildirmek",
    ["Her ay sonunda bütün müşterilerinin listesini vergi dairesine göndermek",
     "Şüpheli işlemleri müşteriye bildirerek açıklama istemek",
     "Yıllık faaliyet raporlarını oda internet sitesinde yayımlamak",
     "Kimlik tespiti belgelerini her yıl noterden onaylatmak"],
    "5549 sayılı Kanun m. 6'ya göre yükümlüler taraf oldukları veya aracılık ettikleri işlemlerden Bakanlıkça belirlenecek "
    "tutarı aşanları Başkanlığa bildirmek zorundadır; kapsam ve süreler Bakanlıkça belirlenir.")

P.q("VUK mük. m. 227/3",
    f"{V}, Hazine ve Maliye Bakanlığının yeminli mali müşavirlik tasdik işlemlerine ilişkin yetkisi aşağıdakilerden hangisidir?",
    "Tasdik işlemlerini elektronik ortamda gerçekleştirmeye yetkilidir.",
    ["Tasdik işlemlerini kaldırarak bu işleri vergi dairelerine devretmeye yetkilidir.",
     "Tasdik ücretlerini her yıl tek tip olarak belirlemeye yetkilidir.",
     "Tasdik yetkisini serbest muhasebeci mali müşavirlere de vermeye yetkilidir.",
     "Tasdik raporlarının kamuya açıklanmasına karar vermeye yetkilidir."],
    "VUK mükerrer m. 227/3'e (6009 sayılı Kanunla eklenen) göre Bakanlık vergi kanunları kapsamındaki YMM tasdik "
    "işlemlerini elektronik ortamda gerçekleştirmeye ve tasdike konu işlemleri mükellef grupları, faaliyet ve tasdik "
    "konuları itibarıyla ayrı ayrı belirleyip uygulatmaya yetkilidir.")

P.q("Çalışma Usul ve Esasları Yön. m. 7 ve 8",
    "SMMM (H), müşterisi (K) A.Ş.'nin bir hissedarının talebi üzerine, şirketin yönetim kurulunca paylaşılmamış maliyet "
    f"verilerini bu hissedara vermiştir. {CU}, (H)'nin davranışı hakkında aşağıdakilerden hangisi doğrudur?",
    "Sır saklama yükümlülüğüne aykırı bir davranıştır.",
    ["Hissedar şirketin sahibi olduğundan sır saklama yükümlülüğü doğmaz.",
     "Meslektaşlara karşı sorumluluk ilkesinin gereğidir.",
     "Sosyal sorumluluk ilkesi gereği bilginin paylaşılması zorunludur.",
     "Bağımsızlık ilkesi gereği meslek mensubu bilgiyi dilediğine verebilir."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 7'ye göre meslek mensupları mesleki faaliyetleri dolayısıyla öğrendikleri "
    "bilgi ve sırları ifşa edemez; m. 8/b'ye göre bilgi işletme sahip ve yöneticilerine isabetli karar için verilir, "
    "yönetimin paylaşmadığı verinin tek bir hissedara verilmesi sır saklama yükümlülüğüne aykırıdır.")

P.q("Çalışma Usul ve Esasları Yön. m. 9 ve 6",
    f"{CU}, bağımsızlık ve tarafsızlık ilkelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bağımsızlık, meslek mensubunun müşteri talimatlarına göre çalışmasını ifade eder.",
    ["Meslek mensupları çalışmalarını kendi sorumlulukları altında tam bir bağımsızlıkla yürütür.",
     "Bağımsızlık mesleğin temeli ve vazgeçilmez bir unsurudur.",
     "Meslek mensupları bağımsızlıklarına gölge düşürecek ilişkilerden kaçınmalıdır.",
     "Meslek mensupları çalışmaları sırasında çıkar çatışmalarından uzak kalır."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 9'a göre meslek mensupları çalışmalarını kendi sorumlulukları altında tam bir "
    "bağımsızlıkla yürütür; bağımsızlık mesleğin temeli ve vazgeçilmez unsurudur. Müşteri talimatına bağlı çalışma "
    "bağımsızlıkla bağdaşmaz; m. 6 çıkar çatışmalarından uzak kalmayı arar.")

P.q("Çalışma Usul ve Esasları Yön. m. 21; 3568 s. Kanun m. 47",
    f"{CU} ve 3568 sayılı Kanun’a göre, meslek mensuplarının hukuki ve cezai sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "VUK'taki iştirak ve teşvik hükümleri meslek mensuplarına uygulanmaz.",
    ["Meslek mensupları VUK'taki iştirak, teşvik ve yardım hükümlerine uyan fiillerinden sorumludur.",
     "Kanun ve yönetmeliklerdeki ceza hükümleri hukuki sorumluluktan ayrı olarak uygulanır.",
     "Görev sırasında işlenen suçlarda TCK'nın kamu görevlilerine ilişkin hükümleri uygulanır.",
     "Ortaklık bürosu veya şirkette yapılan işlerden doğan cezai sorumluluk işi yapana aittir."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 21'e göre meslek mensupları VUK'ta yer alan iştirak, teşvik ve yardım "
    "hükümlerine uyan fiilleri sebebiyle sorumludur ve ceza hükümleri ayrıca uygulanır. Kanun m. 47'ye göre TCK'nın kamu "
    "görevlilerine ilişkin hükümleri, m. 45'e göre şirketlerde cezai sorumluluk işi yapan meslek mensubuna aittir.")

P.q("3568 s. Kanun m. 44; SMGE Yön. m. 10",
    f"{K} ve Sürekli Mesleki Geliştirme Eğitimi Yönetmeliği’ne göre, mesleki geliştirme eğitimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eğitime katılmayan meslek mensubunun ruhsatı iptal edilir.",
    ["Fiilen faaliyette bulunmak için Birlik ve odaların eğitim seminerlerine katılım zorunludur.",
     "Eğitim konuları, programları ve süreleri yönetmelikle belirlenir.",
     "Yükümlülük yerine getirilinceye kadar büro tescil belgesi vize edilmez.",
     "Eğitimi tamamlamayan meslek mensubu stajyer mentorluğu yapamaz."],
    "Kanun m. 44'e göre fiilen faaliyette bulunmak için mesleki geliştirme seminerlerine katılım zorunludur ve usul "
    "yönetmelikle belirlenir. SMGE Yönetmeliği m. 10'a göre yükümlülük yerine getirilinceye kadar büro tescil belgesi "
    "vize edilmez ve mentorluk yapılamaz; ruhsat iptali öngörülmemiştir.",
    zorluk="hard")

P.q("Defter ve Kayıtlar Yön. m. 13-14",
    f"{DK}, tasdik raporlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tasdik raporu tek örnek düzenlenir ve bu örnek firmaya verilir.",
    ["Tasdik raporları kazıntısız, silintisiz ve açık ifadeli düzenlenir.",
     "Tasdik raporlarının en az üç örnek düzenlenmesi zorunludur.",
     "Rapor örneklerinden biri saklanır, ikisi hizmet sunulan firmaya verilir.",
     "Rapor ekleri raporun parçası sayılır ve tüm örneklerine eklenir."],
    "Defter ve Kayıtlar Yönetmeliği m. 13-14'e göre tasdik raporları kazıntısız ve silintisiz, en az üç örnek düzenlenir; "
    "biri meslek mensubunca saklanır, ikisi firmaya verilir; rapor ekleri tüm örneklere eklenir.")

P.q("Defter ve Kayıtlar Yön. m. 15",
    f"{DK}, meslek mensuplarının mali analiz, denetleme ve tasdik işleri dolayısıyla düzenledikleri dosyalara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bakanlık bu dosyaları ancak mahkeme kararıyla inceleyebilir.",
    ["Bu dosyalar gizlidir.",
     "Bu dosyalarla ilgili yazışmalar da gizli yapılır.",
     "Gerek duyulursa ilgili disiplin kurulları dosyaları isteyebilir.",
     "Gerek duyulursa Hazine ve Maliye Bakanlığı dosyaları incelemek üzere isteyebilir."],
    "Defter ve Kayıtlar Yönetmeliği m. 15'e göre bu dosyalar ve yazışmalar gizlidir; gerek duyulduğunda ilgili disiplin "
    "kurulları ile Bakanlık dosyaları incelemek üzere isteyebilir, mahkeme kararı aranmaz.")

P.q("VUK m. 153/A (7524 s. Kanunla değişik)",
    f"{V}, sahte belge düzenleme fiiline iştirak ettiği kesinleşen meslek mensubuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Alıkoyma süresi sonunda teminat istenmeden faaliyete dönülür.",
    ["Mükellefiyeti terkin edilenlerin fiillerine iştirak edene üç yıl alıkoyma cezası uygulanır.",
     "Alıkoyma cezasının uygulanmasında 3568 sayılı Kanundaki usuller tatbik edilir.",
     "Tekrar faaliyete başlamak isteyenden sahte belge tutarının %10'u tutarında teminat istenir.",
     "Teminat, kanunda belirtilen alt ve üst tutar sınırları içinde istenir."],
    "VUK m. 153/A'ya göre iştirakı kesinleşen meslek mensubuna üç yıl alıkoyma cezası uygulanır ve 3568 sayılı Kanun "
    "usulleri tatbik edilir; süre sonunda tekrar faaliyete başlamak isteyenden bir ay içinde, kanundaki sınırlar içinde "
    "sahte belge tutarının %10'u tutarında teminat istenir.",
    zorluk="hard")

P.q("5549 s. Kanun m. 10 ve 7",
    f"{A}, yükümlülere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bildirimde bulunan yükümlü, bildirim yanlış çıkarsa tazminatla sorumlu olur.",
    ["Yükümlülüklerini yerine getirenler hukuki ve cezai bakımdan sorumlu tutulamaz.",
     "Bildirimde bulunanlara dair mahkeme dışında bilgi verilemez.",
     "İstenen bilgi ve belgeler özel kanun hükümleri ileri sürülerek esirgenemez.",
     "Bilgi vermede savunma hakkına ilişkin hükümler saklıdır."],
    "5549 sayılı Kanun m. 10'a göre yükümlülüklerini yerine getiren gerçek ve tüzel kişiler hukuki ve cezai bakımdan "
    "sorumlu tutulamaz ve bildirimde bulunanlara dair mahkeme dışında bilgi verilemez; m. 7'ye göre savunma hakkı saklı "
    "kalmak kaydıyla özel kanunlar ileri sürülerek bilgi vermekten kaçınılamaz.")

P.q("5549 s. Kanun m. 13",
    f"{A}, idari para cezalarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Başkanlıkça verilen idari para cezası kararlarına karşı yargı yolu kapalıdır.",
    ["Kimlik tespiti yükümlülüğünü ihlal eden yükümlülere idari para cezası verilir.",
     "Şüpheli işlem bildirimi yükümlülüğünün ihlaline idari para cezası uygulanır.",
     "Yükümlülüğün ihlalinden itibaren sekiz yıl geçtikten sonra idari para cezası verilemez.",
     "Kanundaki maktu idari para cezası tutarları her yıl güncellenerek uygulanır."],
    "5549 sayılı Kanun m. 13'e göre m. 3, 4 ve 6'daki yükümlülüklerin ihlaline idari para cezası verilir; ihlalden itibaren "
    "sekiz yıl geçtikten sonra ceza verilemez ve 2024'te eklenen fıkraya göre bu kararlara karşı idari yargı yoluna "
    "başvurulabilir. M. 28'e göre maktu tutarlar yeniden değerleme oranında artırılır.",
    zorluk="hard")

P.q("5549 s. Kanun m. 4 ve 10/2",
    "SMMM (J), bir müşterisinin olağan dışı nakit hareketleri nedeniyle Başkanlığa şüpheli işlem bildiriminde bulunmuştur. "
    f"{A}, bu bildirime ve bildirimde bulunana ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bildirimde bulunanın kimliği işleme taraf olan kişiye bildirilir.",
    ["Bildirim, yapılmaya teşebbüs edilen işlemler için de gereklidir.",
     "Bildirimde bulunulduğu işlemin taraflarına açıklanamaz.",
     "Bildirimde bulunanlara dair mahkeme dışında üçüncü kişilere bilgi verilmez.",
     "Bildirimde bulunanların kimliğinin saklı tutulması için mahkemece önlem alınır."],
    "5549 sayılı Kanun m. 4'e göre bildirim teşebbüs aşamasındaki işlemleri de kapsar ve bildirim yapıldığı işleme taraf "
    "olanlara açıklanamaz; m. 10/2'ye göre bildirimde bulunanlara dair mahkeme dışında bilgi verilemez ve kimliklerinin "
    "saklı tutulması için mahkemece önlem alınır.")

P.q("Defter ve Kayıtlar Yön. m. 14",
    "Bir denetim sözleşmesinde raporların örnek sayısı ve teslim usulü düzenlenmektedir. "
    f"{DK}, raporların düzenlenmesi ve teslimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Raporların kaç örnek düzenleneceğini oda yönetim kurulu belirler.",
    ["Raporların kaç örnek düzenleneceği sözleşmelerde belirtilir.",
     "Raporların alınıp verilmesi tutanakla ya da örneğe konulan şerhle yapılır.",
     "Raporlarda düzenleme amacı belirtilmelidir.",
     "Raporlar belirli standartlara bağlanmalıdır."],
    "Defter ve Kayıtlar Yönetmeliği m. 14'e göre raporların kaç örnek düzenleneceği sözleşmelerde belirtilir; raporların "
    "alınıp verilmesi tutanakla ya da rapor örneğine konulan şerhle yapılır; raporlarda amaç belirtilir ve raporlar "
    "standartlara bağlanır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
