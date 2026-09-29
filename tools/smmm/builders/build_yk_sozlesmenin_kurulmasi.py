# -*- coding: utf-8 -*-
"""Hukuk · Borçlar Hukuku · Sözleşmenin Kurulması, Şekil, İrade Bozuklukları ve Temsil — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında TBK soruları "6098 sayılı Türk Borçlar Kanunu’na göre …" kalıbıyla; kısa kök ve
kısa şıklarla gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6098 sayılı TBK md. 1-48.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_sozlesmenin_kurulmasi_2026.json", lesson="borclar_hukuku", topic="sozlesmenin_kurulmasi",
          konu_adi="Sözleşmenin Kurulması", seed=2026093014, surum="6098 sayılı TBK güncel metni; 29.09.2026 kontrolü")

K = "6098 sayılı Türk Borçlar Kanunu’na göre"

P.sayisal("TBK md. 28",
    "Deneyimsizliğinden yararlanılarak açık oransızlık içeren bir sözleşme yapan kişi, deneyimsizliğini sonradan fark "
    f"etmiştir.\n\n{K}, bu kişi aşırı yararlanmaya dayanan hakkını öğrendiği tarihten itibaren kaç yıl içinde kullanabilir?",
    "1", ["2", "3", "5", "10"],
    "Md. 28'e göre zarar gören hakkını düşüncesizlik veya deneyimsizliğini öğrendiği, zor durumda kalmada durumun ortadan "
    "kalktığı tarihten başlayarak bir yıl ve her hâlde sözleşmenin kurulmasından başlayarak beş yıl içinde kullanabilir.")

P.q("TBK md. 1",
    f"{K}, sözleşmenin kurulmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İrade açıklaması örtülü de olabilir.",
    ["İrade açıklaması sadece yazılı olabilir.",
     "Tek tarafın iradesi yeterlidir.",
     "İradelerin birbirine uygun olması aranmaz.",
     "Sözleşme ancak noter huzurunda kurulabilir ve taraflar bunu yazılı teyit eder."],
    "Md. 1'e göre sözleşme tarafların iradelerini karşılıklı ve birbirine uygun olarak açıklamalarıyla kurulur; irade "
    "açıklaması açık veya örtülü olabilir.", zorluk="easy")

P.q("TBK md. 2",
    f"{K}, esaslı noktalarda uyuşan tarafların ikinci derecedeki noktalarda uyuşamaması hâlinde aşağıdakilerden hangisi "
    "doğrudur?",
    "Uyuşmazlığı hâkim işin özelliğine göre çözer.",
    ["Sözleşme kurulmamış sayılır.",
     "Sözleşme kesin hükümsüzdür.",
     "Öneren tarafın görüşü esas alınır.",
     "Uyuşmazlığı ticaret odası hakemi çözer."],
    "Md. 2'ye göre esaslı noktalarda uyuşulmuşsa ikinci derecedeki noktalar üzerinde durulmamış olsa bile sözleşme kurulur; "
    "bu noktalarda uyuşulamazsa hâkim işin özelliğine bakarak karar verir.")

P.sayisal("TBK md. 28",
    f"{K}, aşırı yararlanmaya dayanan hak, her hâlde sözleşmenin kurulduğu tarihten başlayarak kaç yıl içinde "
    "kullanılmalıdır?",
    "5", ["1", "2", "3", "10"],
    "Md. 28'e göre aşırı yararlanmada hak her hâlde sözleşmenin kurulduğu tarihten başlayarak beş yıl içinde kullanılabilir.",
    zorluk="hard")

P.q("TBK md. 3",
    f"{K}, kabul için süre belirleyerek öneride bulunan kişiye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Süre sonuna kadar önerisiyle bağlıdır.",
    ["Her an önerisinden dönebilir.",
     "Süre bittikten sonra da bağlı kalır.",
     "Öneri kabul edilince bile bağlanmaz.",
     "Süre içinde ancak mahkeme izniyle önerisinden dönebilir."],
    "Md. 3'e göre kabul için süre belirleyerek öneren bu sürenin sona ermesine kadar önerisiyle bağlıdır; kabul süre içinde "
    "ulaşmazsa bağlılıktan kurtulur.", zorluk="easy")

P.q("TBK md. 4",
    "(A), telefonda görüştüğü (B)’ye kabul için süre belirlemeden bir mal satmayı önermiş; (B) görüşme sırasında öneriyi "
    f"kabul etmemiştir.\n\n{K}, (A)’nın önerisi hakkında aşağıdakilerden hangisi doğrudur?",
    "(A) önerisiyle bağlı değildir.",
    ["(A) bir hafta bağlıdır.",
     "(A) bir ay bağlıdır.",
     "(A) (B) yanıt verene kadar bağlıdır.",
     "(A) makul bir süre boyunca ve yazılı ret gelinceye kadar bağlıdır."],
    "Md. 4'e göre süre belirlenmeksizin hazır olana yapılan öneri hemen kabul edilmezse öneren bağlılıktan kurtulur; telefon "
    "gibi araçlarla doğrudan iletişim hazır olanlar arasında sayılır.")

P.sayisal("TBK md. 39",
    "Aldatma sonucu sözleşme yapan (A), aldatıldığını 10 Mart’ta öğrenmiştir."
    f"\n\n{K}, (A) öğrenmeden itibaren kaç yıl içinde sözleşmeyle bağlı olmadığını bildirmezse sözleşmeyi onamış sayılır?",
    "1", ["2", "3", "5", "10"],
    "Md. 39'a göre yanılma veya aldatmayı öğrendiği ya da korkutmanın etkisinin ortadan kalktığı andan başlayarak bir yıl "
    "içinde bildirimde bulunmayan taraf sözleşmeyi onamış sayılır.", zorluk="easy")

P.q("TBK md. 5",
    f"{K}, kabul için süre belirlenmeksizin hazır olmayan kişiye yapılan öneri öneren kişiyi ne zamana kadar bağlar?",
    "Yanıtın ulaşması beklenebilecek ana kadar",
    ["Önerinin gönderildiği güne kadar",
     "Bir yıl süreyle",
     "Muhatap açıkça reddedinceye kadar",
     "Sadece bir hafta"],
    "Md. 5'e göre süresiz olarak hazır olmayana yapılan öneri, zamanında ve usulüne uygun gönderilmiş bir yanıtın ulaşmasının "
    "beklenebileceği ana kadar önereni bağlar.")

P.q("TBK md. 5",
    f"{K}, zamanında gönderilen kabulün önerene geç ulaşması hâlinde aşağıdakilerden hangisi doğrudur?",
    "Bağlanmak istemeyen öneren bunu hemen bildirmelidir.",
    ["Sözleşme doğrudan hükümsüzdür.",
     "Öneren bir bildirim yapmadan bağlılıktan kurtulur.",
     "Kabul eden taraf kabulünü yenilemelidir.",
     "Sözleşme ancak noter ihtarıyla kurulur."],
    "Md. 5'e göre zamanında gönderilen kabul önerene geç ulaşır ve öneren onunla bağlı olmak istemezse durumu hemen kabul edene "
    "bildirmek zorundadır.", zorluk="hard")

P.q("TBK md. 6",
    f"{K}, örtülü kabule ilişkin aşağıdakilerden hangisi doğrudur?",
    "Açık kabul beklenmiyorsa ret yoksa sözleşme kurulur.",
    ["Susma kural olarak kabul sayılmaz.",
     "Örtülü kabul sadece tacirler arasında geçerlidir.",
     "Örtülü kabul yazılı şekle bağlıdır.",
     "Sözleşme ancak açık kabulle kurulabilir."],
    "Md. 6'ya göre öneren açık bir kabulü beklemek zorunda değilse, öneri uygun bir sürede reddedilmediği takdirde sözleşme "
    "kurulmuş sayılır.")

P.q("TBK md. 7",
    "Bir şirket, sipariş vermeyen (C)’ye bir kitap göndermiş ve iade etmezse bedelini ödemiş sayılacağını bildirmiştir."
    f"\n\n{K}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Gönderim öneri sayılmaz.",
    ["(C) kitabı iade etmekle yükümlüdür.",
     "(C) bedeli ödemekle yükümlüdür.",
     "(C) kitabı saklamakla yükümlüdür.",
     "Sözleşme (C)’nin sessiz kalmasıyla kurulur."],
    "Md. 7'ye göre ısmarlanmamış bir şeyin gönderilmesi öneri sayılmaz; bu şeyi alan kişi onu geri göndermek veya saklamakla "
    "yükümlü değildir.")

P.q("TBK md. 8",
    f"{K}, fiyatı gösterilerek vitrinde mal sergilenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aksi açıkça anlaşılmadıkça öneri sayılır.",
    ["Öneriye davet sayılır.",
     "Hukuki bir anlam taşımaz.",
     "Sadece tacirler için öneri sayılır.",
     "Sadece fiyat etiketinin noterce onaylı olması hâlinde öneri sayılır."],
    "Md. 8'e göre fiyatı gösterilerek mal sergilenmesi veya tarife, fiyat listesi gönderilmesi, aksi açıkça ve kolaylıkla "
    "anlaşılmadıkça öneri sayılır.")

P.q("TBK md. 9",
    f"{K}, ilan yoluyla ödül sözü veren kişinin sonuç gerçekleşmeden sözünden cayması hâlinde aşağıdakilerden hangisi "
    "doğrudur?",
    "Dürüstlükle yapılan giderleri öder.",
    ["Bir yükümlülüğü kalmaz.",
     "Ödülün iki katını öder.",
     "Ödülün tamamını herkese öder.",
     "Giderleri ödülün değerini aşsa bile öder."],
    "Md. 9'a göre ödül sözü veren sonuç gerçekleşmeden cayarsa dürüstlük kurallarına uygun yapılan giderleri öder; ancak "
    "giderlerin toplamı ödülün değerini aşamaz.")

P.q("TBK md. 10",
    f"{K}, önerinin geri alınmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Geri alma öneriden önce ulaşırsa öneri yapılmamış sayılır.",
    ["Öneri geri alınamaz.",
     "Geri alma sadece noter aracılığıyla yapılır.",
     "Geri alma öneriden sonra ulaşsa da geçerlidir.",
     "Kabulün geri alınması mümkün değildir."],
    "Md. 10'a göre geri alma açıklaması öneriden önce veya aynı anda ulaşmışsa ya da sonra ulaşıp öneriden önce öğrenilmişse "
    "öneri yapılmamış sayılır; aynı kural kabulün geri alınmasında da uygulanır.")

P.q("TBK md. 11",
    f"{K}, hazır olmayanlar arasında kurulan sözleşme ne zamandan itibaren hüküm doğurur?",
    "Kabulün gönderildiği andan",
    ["Kabulün önerene ulaştığı andan",
     "Önerinin gönderildiği andan",
     "Sözleşmenin imzalandığı günden",
     "Kabulün önerence okunup yazılı olarak teyit edildiği andan"],
    "Md. 11'e göre hazır olmayanlar arasında kurulan sözleşmeler kabulün gönderildiği andan başlayarak hüküm doğurur.")

P.q("TBK md. 12",
    f"{K}, sözleşmelerin şekline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kanundaki şekil kural olarak ispat şeklidir.",
    ["Kanunda aksi yoksa sözleşme şekle bağlı değildir.",
     "Kanundaki şekle uyulmayan sözleşme hüküm doğurmaz.",
     "Yazılı sözleşmenin değişikliği de yazılı olmalıdır.",
     "Çelişmeyen tamamlayıcı yan hükümler şekle tabi değildir."],
    "Md. 12'ye göre kanunda sözleşmeler için öngörülen şekil kural olarak geçerlilik şeklidir.", zorluk="easy")

P.q("TBK md. 14",
    f"{K}, yazılı şekilde yapılması öngörülen sözleşmelerde kimlerin imzası zorunludur?",
    "Borç altına girenlerin",
    ["Sadece alacaklının",
     "Tüm tanıkların",
     "Sadece noterin",
     "Tarafların ve iki tanığın birlikte"],
    "Md. 14'e göre yazılı şekilde yapılması öngörülen sözleşmelerde borç altına girenlerin imzalarının bulunması zorunludur.",
    zorluk="easy")

P.q("TBK md. 14",
    f"{K}, aşağıdakilerden hangisi kural olarak yazılı şekil yerine geçmez?",
    "İmzasız e-posta metni",
    ["İmzalı mektup",
     "Asılları imzalanmış telgraf",
     "Teyit edilmiş faks",
     "Güvenli elektronik imzalı metin"],
    "Md. 14'e göre imzalı mektup, asılları imzalanmış telgraf, teyitli faks ve güvenli elektronik imzalı metinler yazılı şekil "
    "yerine geçer; imzasız e-posta bu nitelikte değildir.")

P.q("TBK md. 15",
    f"{K}, imzaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Güvenli elektronik imza el yazısı imzanın yerini tutmaz.",
    ["İmza kural olarak el yazısıyla atılır.",
     "Çok sayıda kıymetli evrakta başka araç yeterli olabilir.",
     "Görme engellinin talebiyle imzasında şahit aranır.",
     "Örf ve âdetçe kabul edilen hâllerde araçla imza yeterlidir."],
    "Md. 15'e göre güvenli elektronik imza el yazısıyla atılmış imzanın bütün hukuki sonuçlarını doğurur.")

P.q("TBK md. 16",
    f"{K}, imza atamayan kişi aşağıdakilerden hangisini imza yerine kullanabilir?",
    "Usulüne göre onaylı parmak izi",
    ["Tanık beyanı",
     "Sözlü açıklama",
     "Fotoğraf",
     "Başka birinin kendi adına attığı onaysız imza"],
    "Md. 16'ya göre imza atamayanlar imza yerine usulüne göre onaylanmış olması koşuluyla parmak izi, el ile yapılmış bir "
    "işaret veya mühür kullanabilir.")

P.q("TBK md. 17",
    "Taraflar, kanunda şekle bağlanmamış bir sözleşmenin herhangi bir ayrıntı belirlemeden yazılı yapılmasını "
    f"kararlaştırmışlardır.\n\n{K}, bu durumda hangi hükümler uygulanır?",
    "Yasal yazılı şekil hükümleri",
    ["Resmî şekil hükümleri",
     "Sözlü sözleşme hükümleri",
     "Ticari örf ve âdet",
     "Tarafların sonradan anlaşacağı şekil kuralları"],
    "Md. 17'ye göre herhangi bir belirleme olmaksızın yazılı şekil kararlaştırılmışsa yasal yazılı şekle ilişkin hükümler "
    "uygulanır; kararlaştırılan şekle uyulmazsa sözleşme tarafları bağlamaz.")

P.q("TBK md. 18",
    f"{K}, borcun sebebini içermeyen borç tanımasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Geçerlidir.",
    ["Kesin hükümsüzdür.",
     "Sadece noter onayıyla geçerlidir.",
     "İptal edilebilir.",
     "Sadece tacirler arasında geçerlidir."],
    "Md. 18'e göre borcun sebebini içermemiş olsa bile borç tanıması geçerlidir.")

P.q("TBK md. 19",
    f"{K}, sözleşmenin yorumlanmasında esas alınan unsur aşağıdakilerden hangisidir?",
    "Tarafların gerçek ve ortak iradesi",
    ["Kullanılan sözcüklerin sözlük anlamı",
     "Sadece yazılı metnin başlığı",
     "Öneren tarafın iradesi",
     "Sözleşmeyi hazırlayan avukatın açıklaması"],
    "Md. 19'a göre sözleşmenin türünün ve içeriğinin belirlenmesinde ve yorumunda, yanlışlıkla veya gizleme amacıyla kullanılan "
    "sözcüklere bakılmaksızın tarafların gerçek ve ortak iradeleri esas alınır.")

P.q("TBK md. 19",
    f"{K}, muvazaalı bir yazılı borç tanımasına güvenerek alacağı kazanan üçüncü kişiye karşı borçlunun durumu "
    "aşağıdakilerden hangisidir?",
    "Muvazaa savunmasında bulunamaz.",
    ["Muvazaa savunmasıyla borçtan kurtulur.",
     "Borcun yarısını öder.",
     "Üçüncü kişi alacağı kazanamaz.",
     "Borç tanıması üçüncü kişiye karşı yok hükmündedir."],
    "Md. 19'a göre borçlu, yazılı bir borç tanımasına güvenerek alacağı kazanmış olan üçüncü kişiye karşı işlemin muvazaalı "
    "olduğu savunmasında bulunamaz.", zorluk="hard")

P.q("TBK md. 20",
    f"{K}, genel işlem koşullarının tanımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tartışıldığına ilişkin kayıt onları bu nitelikten çıkarır.",
    ["Düzenleyen tarafından önceden hazırlanır.",
     "Çok sayıda benzer sözleşmede kullanılmak amacıyla hazırlanır.",
     "Metinlerin özdeş olmaması nitelendirmeyi engellemez.",
     "Sözleşmenin ekinde yer alması nitelendirmeyi etkilemez."],
    "Md. 20'ye göre koşulların her birinin tartışılarak kabul edildiğine ilişkin kayıtlar tek başına onları genel işlem koşulu "
    "olmaktan çıkarmaz.", zorluk="hard")

P.q("TBK md. 21",
    f"{K}, karşı tarafın menfaatine aykırı genel işlem koşullarının sözleşme kapsamına girmesi için aşağıdakilerden hangisi "
    "aranmaz?",
    "Koşulların noterce onaylanması",
    ["Karşı tarafa açıkça bilgi verilmesi",
     "İçeriği öğrenme imkânı sağlanması",
     "Karşı tarafın koşulları kabul etmesi",
     "Koşulların sözleşmenin niteliğine yabancı olmaması"],
    "Md. 21'e göre açık bilgilendirme, içeriği öğrenme imkânı ve karşı tarafın kabulü gerekir; niteliğe yabancı koşullar "
    "yazılmamış sayılır. Noter onayı aranmaz.")

P.q("TBK md. 22",
    f"{K}, bazı genel işlem koşullarının yazılmamış sayılması sözleşmenin diğer hükümlerini nasıl etkiler?",
    "Diğer hükümler geçerliliğini korur.",
    ["Sözleşmenin tamamı hükümsüz olur.",
     "Düzenleyen sözleşmeden dönebilir.",
     "Sözleşme askıya alınır.",
     "Düzenleyen sözleşmeyi ortadan kaldırabilir."],
    "Md. 22'ye göre yazılmamış sayılan koşullar dışındaki hükümler geçerliliğini korur; düzenleyen, bu koşullar olmasaydı "
    "sözleşmeyi yapmayacağını ileri süremez.")

P.q("TBK md. 23",
    f"{K}, açık ve anlaşılır olmayan bir genel işlem koşulu nasıl yorumlanır?",
    "Düzenleyenin aleyhine",
    ["Düzenleyenin lehine",
     "Hâkimin takdirine göre tarafsız",
     "Ticari örf ve âdete göre",
     "Sözleşmenin tamamen geçersiz sayılacağı şekilde"],
    "Md. 23'e göre açık ve anlaşılır olmayan veya birden çok anlama gelen genel işlem koşulu düzenleyenin aleyhine ve karşı "
    "tarafın lehine yorumlanır.", zorluk="easy")

P.q("TBK md. 24",
    f"{K}, düzenleyene sözleşmeyi karşı taraf aleyhine tek yanlı değiştirme yetkisi veren kayıtların hukuki sonucu "
    "aşağıdakilerden hangisidir?",
    "Yazılmamış sayılır.",
    ["Geçerlidir.",
     "Sadece yazılıysa geçerlidir.",
     "Tüm sözleşmeyi kesin hükümsüz kılar.",
     "Karşı tarafın imzası varsa ve noterce onaylıysa geçerlidir."],
    "Md. 24'e göre düzenleyene tek yanlı olarak karşı taraf aleyhine değiştirme veya yeni düzenleme yetkisi veren kayıtlar "
    "yazılmamış sayılır.")

P.q("TBK md. 27",
    f"{K}, aşağıdakilerden hangisi kesin hükümsüzlük sebeplerinden biri değildir?",
    "Aşırı yararlanma",
    ["Emredici hükümlere aykırılık",
     "Ahlaka aykırılık",
     "Kamu düzenine aykırılık",
     "Konunun imkânsızlığı"],
    "Md. 27'ye göre emredici hükümlere, ahlaka, kamu düzenine, kişilik haklarına aykırı veya konusu imkânsız sözleşmeler kesin "
    "hükümsüzdür; aşırı yararlanma md. 28'e göre iptal edilebilirlik doğurur.", zorluk="easy")

P.q("TBK md. 27",
    f"{K}, sözleşmedeki bazı hükümlerin kesin hükümsüz olmasının diğer hükümlere etkisi nedir?",
    "Kural olarak diğerleri geçerliliğini korur.",
    ["Sözleşmenin tamamı hükümsüz olur.",
     "Diğer hükümler askıda kalır.",
     "Hâkim tüm sözleşmeyi yeniden yazar.",
     "Diğerleri ancak noter onayıyla geçerli olur."],
    "Md. 27'ye göre bir kısım hükümlerin hükümsüzlüğü diğerlerinin geçerliliğini etkilemez; ancak bunlar olmaksızın sözleşmenin "
    "yapılmayacağı açıkça anlaşılırsa sözleşmenin tamamı kesin hükümsüz olur.")

P.q("TBK md. 28",
    f"{K}, aşırı yararlanmanın koşulları arasında aşağıdakilerden hangisi yer almaz?",
    "Karşı tarafın tacir olması",
    ["Edimler arasında açık oransızlık",
     "Zarar görenin zor durumda kalması",
     "Zarar görenin düşüncesizliği",
     "Zarar görenin deneyimsizliğinden yararlanılması"],
    "Md. 28'e göre aşırı yararlanma için edimler arasında açık oransızlık ve bunun zarar görenin zor durumu, düşüncesizliği veya "
    "deneyimsizliğinden yararlanılarak gerçekleştirilmesi gerekir.")

P.q("TBK md. 28",
    f"{K}, aşırı yararlanmada zarar görenin seçimlik hakları aşağıdakilerden hangisinde doğru verilmiştir?",
    "Bağlı olmamak ya da oransızlığın giderilmesi",
    ["Sadece tazminat istemek",
     "Sadece cezai şart istemek",
     "Sadece sözleşmeyi feshetmek",
     "Şikâyet edip sözleşmeyi askıya almak"],
    "Md. 28'e göre zarar gören durumun özelliğine göre ya sözleşmeyle bağlı olmadığını bildirerek ediminin geri verilmesini ya "
    "da sözleşmeye bağlı kalarak oransızlığın giderilmesini isteyebilir.")

P.q("TBK md. 29",
    f"{K}, önsözleşmenin geçerliliğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak asıl sözleşmenin şekline bağlıdır.",
    ["Önsözleşme şekle bağlı değildir.",
     "Önsözleşme geçersizdir.",
     "Önsözleşme sadece sözlü yapılabilir.",
     "Önsözleşme ancak resmî şekilde yapılabilir."],
    "Md. 29'a göre bir sözleşmenin ileride kurulmasına ilişkin önsözleşmeler geçerlidir; kanundaki istisnalar dışında geçerliliği "
    "ileride kurulacak sözleşmenin şekline bağlıdır.")

P.q("TBK md. 31",
    f"{K}, aşağıdakilerden hangisi esaslı yanılma hâllerinden biri değildir?",
    "Basit hesap yanlışlığı",
    ["İstenenden başka bir sözleşme için irade açıklanması",
     "İstenenden başka bir konu için irade açıklanması",
     "İstenenden başka kişiye irade açıklanması",
     "Edimde önemli ölçüde fazlası için irade açıklanması"],
    "Md. 31'e göre basit hesap yanlışlıkları sözleşmenin geçerliliğini etkilemez, düzeltilmeleri gerekir; sayılan diğer hâller "
    "esaslı yanılmadır.", zorluk="easy")

P.q("TBK md. 32",
    f"{K}, saikte yanılmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak esaslı yanılma sayılmaz.",
    ["Kural olarak esaslı yanılmadır.",
     "Sözleşmeyi kesin hükümsüz kılar.",
     "Sadece tacirler için esaslıdır.",
     "Karşı taraf bilmese bile sözleşmeyi geçersiz kılar."],
    "Md. 32'ye göre saikte yanılma esaslı sayılmaz; yanılanın saiki sözleşmenin temeli sayması dürüstlüğe uygunsa ve karşı "
    "tarafça bilinebilirse esaslı sayılır.")

P.q("TBK md. 33",
    f"{K}, sözleşme iradesinin çevirmen tarafından yanlış iletilmesi hâlinde hangi hükümler uygulanır?",
    "Yanılma hükümleri",
    ["Aldatma hükümleri", "Korkutma hükümleri", "Aşırı yararlanma hükümleri",
     "Haksız fiil ve sebepsiz zenginleşme hükümleri"],
    "Md. 33'e göre sözleşmenin kurulmasına yönelik iradenin haberci veya çevirmen gibi bir aracı ya da araç tarafından yanlış "
    "iletilmesi hâlinde de yanılma hükümleri uygulanır.")

P.q("TBK md. 34",
    "Yanılan (A), yanıldığını ileri sürmüş; karşı taraf ise sözleşmenin (A)’nın kastettiği anlamda kurulmasına razı "
    f"olduğunu bildirmiştir.\n\n{K}, sözleşme hakkında aşağıdakilerden hangisi doğrudur?",
    "Kastedilen anlamda kurulmuş sayılır.",
    ["Kesin hükümsüzdür.",
     "(A) yine de bağlı olmadığını ileri sürebilir.",
     "Hâkim sözleşmeyi feshetmelidir.",
     "Sözleşme karşı tarafın anladığı anlamda kurulmuş sayılır."],
    "Md. 34'e göre yanılan, yanıldığını dürüstlük kurallarına aykırı olarak ileri süremez; karşı taraf kastedilen anlamda "
    "kurulmasına razı olursa sözleşme bu anlamda kurulmuş sayılır.", zorluk="hard")

P.q("TBK md. 35",
    f"{K}, yanılmasında kusurlu olan tarafın sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Karşı taraf yanılmayı bilse de tazminat istenebilir.",
    ["Hükümsüzlükten doğan zararı giderir.",
     "Hâkim hakkaniyete göre daha fazla tazminata hükmedebilir.",
     "Artırılan tazminat ifa yararını aşamaz.",
     "Kusurlu yanılma sorumluluk doğurur."],
    "Md. 35'e göre diğer taraf yanılmayı biliyor veya bilmesi gerekiyorsa tazminat istenemez.", zorluk="hard")

P.q("TBK md. 36",
    f"{K}, aldatmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yanılma esaslı olmasa da aldatılan bağlı değildir.",
    ["Sadece esaslı yanılma varsa aldatılan bağlı olmaz.",
     "Üçüncü kişinin aldatmasında karşı tarafın bilgisi aranmaz.",
     "Aldatma sözleşmeyi kesin hükümsüz kılar.",
     "Aldatılan taraf ancak mahkeme kararıyla ve beş yıl içinde sözleşmeden kurtulur."],
    "Md. 36'ya göre diğerinin aldatması sonucu sözleşme yapan, yanılması esaslı olmasa bile sözleşmeyle bağlı değildir; üçüncü "
    "kişinin aldatmasında karşı tarafın bunu bilmesi veya bilecek durumda olması gerekir.")

P.q("TBK md. 36",
    "(A), üçüncü kişi (C)’nin aldatması sonucu (B) ile sözleşme yapmıştır; (B) aldatmayı bilmemekte ve bilecek durumda "
    f"da değildir.\n\n{K}, (A)’nın durumu nedir?",
    "(A) sözleşmeyle bağlıdır.",
    ["(A) sözleşmeyle bağlı değildir.",
     "Sözleşme kesin hükümsüzdür.",
     "Sözleşme (B) aleyhine iptal edilir.",
     "(A) sözleşmeyi dilediği zaman bir tazminat ödemeden bozabilir."],
    "Md. 36'ya göre üçüncü kişinin aldatması hâlinde aldatılan ancak karşı tarafın aldatmayı bilmesi veya bilecek durumda "
    "olması hâlinde sözleşmeyle bağlı değildir.", zorluk="hard")

P.q("TBK md. 37",
    "Üçüncü kişi (D)’nin korkutması sonucu sözleşme yapan (A), karşı tarafın korkutmayı bilmediği ve bilecek durumda "
    f"olmadığı hâlde sözleşmeyle bağlı kalmak istememektedir.\n\n{K}, aşağıdakilerden hangisi doğrudur?",
    "Hakkaniyet gerektiriyorsa tazminat öder.",
    ["Sözleşmeyle bağlı kalmalıdır.",
     "Karşı taraftan tazminat alır.",
     "Sözleşme kesin hükümsüzdür.",
     "Korkutma üçüncü kişiden geldiği için bir hak doğmaz."],
    "Md. 37'ye göre korkutan üçüncü kişi olup diğer taraf bunu bilmiyor ve bilecek durumda değilse, bağlı kalmak istemeyen "
    "korkutulan hakkaniyet gerektiriyorsa diğer tarafa tazminat öder.", zorluk="hard")

P.q("TBK md. 38",
    f"{K}, korkutmanın gerçekleşmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ağır ve yakın zarar tehlikesine haklı inanç aranır.",
    ["Sadece malvarlığına yönelik tehlike yeterlidir.",
     "Hafif ve uzak tehlike yeterlidir.",
     "Hakkın kullanılacağını söylemek doğrudan korkutmadır.",
     "Korkutmanın yakınlara yönelmesi korkutma sayılmaz."],
    "Md. 38'e göre korkutulan, kendisinin veya yakınlarının kişilik haklarına ya da malvarlığına yönelik ağır ve yakın bir zarar "
    "tehlikesinin doğduğuna inanmakta haklıysa korkutma gerçekleşmiş sayılır.")

P.q("TBK md. 39",
    f"{K}, aldatma veya korkutma nedeniyle bağlayıcı olmayan sözleşmenin onanmış sayılmasının tazminat hakkına etkisi "
    "nedir?",
    "Tazminat hakkını ortadan kaldırmaz.",
    ["Tazminat hakkını ortadan kaldırır.",
     "Tazminat yarıya iner.",
     "Tazminat hakkı sadece ceza davasıyla korunur.",
     "Tazminat hakkı ancak karşı tarafın rızasıyla ve yazılı olarak korunur."],
    "Md. 39'a göre aldatma veya korkutmadan dolayı bağlayıcılığı olmayan bir sözleşmenin onanmış sayılması tazminat hakkını "
    "ortadan kaldırmaz.")

P.q("TBK md. 40",
    f"{K}, yetkili temsilcinin temsil sıfatını bildirmeden yaptığı işlemin sonuçlarına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Kural olarak temsilciye ait olur.",
    ["Kural olarak temsil olunanı bağlar.",
     "İşlem kesin hükümsüzdür.",
     "Sonuçlar üçüncü kişiye ait olur.",
     "İşlem ancak noter onayıyla geçerli olur."],
    "Md. 40'a göre temsilci sıfatını bildirmezse sonuçlar kendisine ait olur; ancak karşı taraf temsil ilişkisini durumdan "
    "çıkarıyor veya işlemi kiminle yaptığı farksızsa sonuçlar temsil olunana ait olur.")

P.q("TBK md. 42",
    f"{K}, hukuki işlemden doğan temsil yetkisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Temsil olunan geri alma hakkından önceden feragat edebilir.",
    ["Temsil olunan yetkiyi sınırlayabilir.",
     "Temsil olunan yetkiyi geri alabilir.",
     "Hizmet sözleşmesinden doğan haklar saklıdır.",
     "Bildirilen yetkinin geri alınması iyiniyetlilere bildirilmelidir."],
    "Md. 42'ye göre temsil olunan, yetkiyi sınırlama veya geri alma hakkından önceden feragat edemez.")

P.q("TBK md. 43",
    f"{K}, aşağıdakilerden hangisi aksi kararlaştırılmadıkça hukuki işlemden doğan temsil yetkisini sona erdirmez?",
    "Temsilcinin başka şehre taşınması",
    ["Temsil olunanın ölümü",
     "Temsilcinin fiil ehliyetini kaybetmesi",
     "Temsil olunanın iflası",
     "Temsilcinin gaipliğine karar verilmesi"],
    "Md. 43'e göre temsil yetkisi temsil olunanın veya temsilcinin ölümü, gaipliği, fiil ehliyetini kaybetmesi veya iflası "
    "hâllerinde sona erer.", zorluk="easy")

P.q("TBK md. 44",
    f"{K}, yetkisi sona eren temsilcinin yetki belgesine ilişkin yükümlülüğü aşağıdakilerden hangisidir?",
    "Temsil olunana geri vermek",
    ["Belgeyi imha etmek",
     "Belgeyi saklamaya devam etmek",
     "Belgeyi üçüncü kişiye vermek",
     "Belgeyi noterde onaylatarak kendi arşivinde süresiz saklamak"],
    "Md. 44'e göre yetkinin sona ermesi durumunda temsilci yetki belgesini temsil olunana geri vermekle veya hâkimin belirleyeceği "
    "yere bırakmakla yükümlüdür.")

P.q("TBK md. 45",
    "Temsil olunanın öldüğünden habersiz olan temsilci, bu durumu bilmeyen üçüncü kişiyle bir sözleşme yapmıştır."
    f"\n\n{K}, bu sözleşmenin sonuçları hakkında aşağıdakilerden hangisi doğrudur?",
    "Mirasçılar işlemle bağlıdır.",
    ["İşlem kesin hükümsüzdür.",
     "Sonuçlar temsilciye aittir.",
     "Üçüncü kişi zarara katlanır.",
     "İşlem ancak mirasçı onayıyla geçerli olur."],
    "Md. 45'e göre temsilci yetkisinin sona erdiğini bilmediği sürece temsil olunan veya halefleri yapılan işlemlerin sonuçlarıyla "
    "bağlıdır; üçüncü kişi sona ermeyi biliyorsa bu kural uygulanmaz.", zorluk="hard")

P.q("TBK md. 46",
    f"{K}, yetkisiz temsilcinin yaptığı işlem temsil olunanı ne zaman bağlar?",
    "Temsil olunan onadığı takdirde",
    ["İşlem yapıldığı anda",
     "Sadece mahkeme kararıyla",
     "Üçüncü kişi iyiniyetliyse",
     "Temsilci işlemi noterde yaptıysa"],
    "Md. 46'ya göre yetkisiz temsilcinin yaptığı işlem ancak temsil olunan onadığı takdirde onu bağlar; karşı taraf uygun sürede "
    "onay istenebilir, onanmazsa bağlılıktan kurtulur.", zorluk="easy")

P.q("TBK md. 47",
    f"{K}, yetkisiz temsilcinin sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Karşı taraf yetkisizliği bilse de temsilci zararı öder.",
    ["İşlem onanmazsa zarar temsilciden istenebilir.",
     "Hakkaniyet gerekirse kusurlu temsilciden diğer zararlar istenebilir.",
     "Sebepsiz zenginleşmeden doğan haklar saklıdır.",
     "Onamama açık veya örtülü olabilir."],
    "Md. 47'ye göre yetkisiz temsilci, karşı tarafın yetkisizliğini bildiğini veya bilmesi gerektiğini ispat ederse kendisinden "
    "zararın giderilmesi istenemez.")

P.q("TBK md. 41",
    f"{K}, üçüncü kişilere bildirilmiş olan temsil yetkisinin içeriği neye göre belirlenir?",
    "Bu bildirime göre",
    ["Temsilcinin beyanına göre",
     "Ticaret sicili kaydına göre",
     "Hâkimin takdirine göre",
     "Bildirilmeyen sonraki açıklamaya göre"],
    "Md. 41'e göre temsil yetkisi üçüncü kişilere bildirilmişse yetkinin içeriği ve derecesi bu bildirime göre belirlenir.")

P.oncul("TBK md. 27",
    f"{K} aşağıdaki sözleşmeler değerlendirilmektedir:",
    ["Konusu baştan imkânsız olan sözleşme",
     "Aşırı yararlanma içeren sözleşme",
     "Ahlaka aykırı sözleşme",
     "Aldatma sonucu yapılan sözleşme"],
    "Yukarıdakilerden hangileri kesin hükümsüzdür?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 27'ye göre konusu imkânsız (I) ve ahlaka aykırı (III) sözleşmeler kesin hükümsüzdür; aşırı yararlanma (II) ve aldatma "
    "(IV) sözleşmeyi iptal edilebilir kılar.", zorluk="hard")

P.q("TBK md. 13",
    f"{K}, kanunda yazılı şekle bağlanan bir sözleşmenin sonradan değiştirilmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Değişiklik de yazılı şekle tabidir.",
    ["Değişiklik sözlü yapılabilir.",
     "Değişiklik resmî şekilde yapılmalıdır.",
     "Değişiklik yapılamaz.",
     "Metinle çelişen yan hükümler de sözlü olarak eklenebilir."],
    "Md. 13'e göre kanunda yazılı şekilde yapılması öngörülen sözleşmenin değiştirilmesinde de yazılı şekle uyulması zorunludur; "
    "metinle çelişmeyen tamamlayıcı yan hükümler bu kuralın dışındadır.")

P.q("TBK md. 26",
    f"{K}, sözleşme özgürlüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "İçerik kanuni sınırlar içinde özgürce belirlenir.",
    ["İçerik sadece kanunla belirlenir.",
     "Taraflar sadece tip sözleşme yapabilir.",
     "İçeriği noter belirler.",
     "Taraflar emredici hükümlere aykırı hükümleri de özgürce koyabilir."],
    "Md. 26'ya göre taraflar bir sözleşmenin içeriğini kanunda öngörülen sınırlar içinde özgürce belirleyebilir.",
    zorluk="easy")

P.q("TBK md. 21",
    f"{K}, sözleşmenin niteliğine ve işin özelliğine yabancı olan genel işlem koşullarının hukuki sonucu nedir?",
    "Yazılmamış sayılır.",
    ["Kesin hükümsüzdür.",
     "Geçerlidir.",
     "İptal edilebilir.",
     "Sadece düzenleyen lehine yorumlanır."],
    "Md. 21'e göre sözleşmenin niteliğine ve işin özelliğine yabancı olan genel işlem koşulları da yazılmamış sayılır.")

P.q("TBK md. 25",
    f"{K}, genel işlem koşullarının içerik denetimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Karşı taraf aleyhine ağırlaştırıcı koşul konabilir.",
    ["Dürüstlüğe aykırı koşul konulamaz.",
     "Belirsiz koşul düzenleyen aleyhine yorumlanır.",
     "Tek yanlı değiştirme yetkisi yazılmamış sayılır.",
     "Bilgi verilmeyen aleyhe koşullar yazılmamış sayılır."],
    "Md. 25'e göre genel işlem koşullarına dürüstlük kurallarına aykırı olarak karşı tarafın aleyhine veya durumunu ağırlaştırıcı "
    "nitelikte hükümler konulamaz.")

P.q("TBK md. 30",
    f"{K}, sözleşme kurulurken esaslı yanılmaya düşen tarafın durumu aşağıdakilerden hangisidir?",
    "Sözleşmeyle bağlı olmaz.",
    ["Sözleşme kesin hükümsüzdür.",
     "Sözleşmeyle bağlı kalır.",
     "Sadece bedel indirimi isteyebilir.",
     "Karşı tarafa cezai şart öder."],
    "Md. 30'a göre sözleşme kurulurken esaslı yanılmaya düşen taraf sözleşme ile bağlı olmaz.", zorluk="easy")

P.q("TBK md. 38",
    "Alacaklı, borçlunun zor durumundan yararlanarak alacağını dava edeceğini söyleyip borçluyu aşırı menfaat sağlayan bir "
    f"sözleşmeye razı etmiştir.\n\n{K}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Korkutmanın varlığı kabul edilir.",
    ["Hak kullanımı olduğundan korkutma yoktur.",
     "Sözleşme kural olarak geçerlidir.",
     "Sadece aşırı yararlanma hükümleri uygulanır.",
     "Sözleşme kesin hükümsüzdür."],
    "Md. 38'e göre bir hakkın kullanılacağı korkutmasıyla sözleşme yapıldığında, hakkı kullanacağını açıklayan diğer tarafın zor "
    "durumundan aşırı menfaat sağlamışsa korkutmanın varlığı kabul edilir.", zorluk="hard")

P.q("TBK md. 40",
    "Temsilci, temsil sıfatını açıkça bildirmeden bir işlem yapmış; ancak karşı taraf temsil ilişkisini durumdan "
    f"çıkarabilecek konumdadır.\n\n{K}, işlemin sonuçları kime aittir?",
    "Temsil olunana",
    ["Temsilciye", "Karşı tarafa", "Temsilci ve karşı tarafa birlikte", "Temsilcinin mirasçılarına"],
    "Md. 40'a göre karşı taraf temsil ilişkisinin varlığını durumdan çıkarıyor veya çıkarması gerekiyorsa işlemin sonuçları "
    "doğrudan temsil olunana ait olur.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
