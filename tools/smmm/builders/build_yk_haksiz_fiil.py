# -*- coding: utf-8 -*-
"""Hukuk · Borçlar Hukuku · Haksız Fiil ve Sebepsiz Zenginleşme — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında TBK soruları "6098 sayılı Türk Borçlar Kanunu’na göre, haksız bir fiil …" gibi
kısa köklerle; zamanaşımı ve sorumluluk türleri üzerinden gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6098 sayılı TBK md. 49-82. 7589 sayılı Kanunla (16.07.2026)
md. 55'e faiz başlangıcı ve ödemelerin mahsubuna ilişkin fıkralar eklenmiştir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_haksiz_fiil_2026.json", lesson="borclar_hukuku", topic="haksiz_fiil",
          konu_adi="Haksız Fiil", seed=2026093015,
          surum="6098 sayılı TBK güncel metni (7589 s. Kanun değişikliği dahil); 29.09.2026 kontrolü")

K = "6098 sayılı Türk Borçlar Kanunu’na göre"
K26 = "6098 sayılı Türk Borçlar Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("TBK md. 72",
    f"{K}, haksız fiilden doğan tazminat istemi, zarar görenin zararı ve tazminat yükümlüsünü öğrendiği tarihten "
    "başlayarak kaç yıl geçmekle zamanaşımına uğrar?",
    "2", ["1", "3", "5", "10"],
    "Md. 72'ye göre tazminat istemi zararı ve tazminat yükümlüsünü öğrenmeden itibaren iki yıl ve her hâlde fiilden itibaren on "
    "yıl geçmekle zamanaşımına uğrar.", zorluk="easy")

P.q("TBK md. 49",
    f"{K}, genel haksız fiil sorumluluğunun unsurları arasında aşağıdakilerden hangisi yer almaz?",
    "Taraflar arasında sözleşme bulunması",
    ["Hukuka aykırı fiil",
     "Kusur",
     "Zarar",
     "Fiil ile zarar arasında illiyet bağı"],
    "Md. 49'a göre kusurlu ve hukuka aykırı bir fiille başkasına zarar veren bu zararı gidermekle yükümlüdür; sözleşme ilişkisi "
    "haksız fiilin unsuru değildir.", zorluk="easy")

P.q("TBK md. 49",
    f"{K}, zarar verici fiili yasaklayan bir hukuk kuralı bulunmadığı hâlde başkasına zarar verenin sorumluluğuna ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Ahlaka aykırı kasıtlı zararda sorumludur.",
    ["Hukuk kuralı yoksa sorumluluk doğmaz.",
     "İhmalle zarar veren de sorumludur.",
     "Sadece ceza sorumluluğu doğar.",
     "Sorumluluk için zarar görenin rızası aranır."],
    "Md. 49/2'ye göre zarar verici fiili yasaklayan bir hukuk kuralı bulunmasa bile ahlaka aykırı bir fiille başkasına kasten "
    "zarar veren de bu zararı gidermekle yükümlüdür.")

P.sayisal("TBK md. 72",
    f"{K}, haksız fiilden doğan tazminat istemi her hâlde fiilin işlendiği tarihten başlayarak kaç yıl geçmekle "
    "zamanaşımına uğrar?",
    "10", ["2", "3", "5", "20"],
    "Md. 72'ye göre tazminat istemi her hâlde fiilin işlendiği tarihten başlayarak on yıl geçmekle zamanaşımına uğrar; ceza "
    "kanunları daha uzun süre öngörüyorsa o süre uygulanır.")

P.q("TBK md. 50",
    f"{K}, haksız fiilde ispat yüküne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zarar veren kusursuzluğunu ispatla yükümlüdür.",
    ["Zarar gören zararını ispat eder.",
     "Zarar gören zarar verenin kusurunu ispat eder.",
     "Miktar ispatlanamazsa hâkim hakkaniyete göre belirler.",
     "Hâkim olayların olağan akışını gözetir."],
    "Md. 50'ye göre zarar gören zararını ve zarar verenin kusurunu ispat yükü altındadır; genel haksız fiilde kusursuzluğu ispat "
    "yükü zarar verene ait değildir.")

P.q("TBK md. 51",
    f"{K}, tazminatın belirlenmesinde hâkimin özellikle göz önüne alacağı unsur aşağıdakilerden hangisidir?",
    "Kusurun ağırlığı",
    ["Zarar verenin mesleği",
     "Zarar görenin yaşı",
     "Davanın açıldığı yer",
     "Tarafların medeni hâli"],
    "Md. 51'e göre hâkim tazminatın kapsamını ve ödenme biçimini durumun gereğini ve özellikle kusurun ağırlığını göz önüne "
    "alarak belirler; irat biçiminde ödemede borçlu güvence gösterir.", zorluk="easy")

P.sayisal("TBK md. 73",
    "Aynı zarardan müteselsilen sorumlu olan (A), tazminatın tamamını ödemiş ve birlikte sorumlu olan (B)’yi öğrenmiştir."
    f"\n\n{K}, (A)’nın rücu istemi bu tarihten başlayarak kaç yıl geçmekle zamanaşımına uğrar?",
    "2", ["1", "3", "5", "10"],
    "Md. 73'e göre rücu istemi tazminatın tamamının ödendiği ve birlikte sorumlunun öğrenildiği tarihten başlayarak iki yıl ve "
    "her hâlde ödemeden itibaren on yıl geçmekle zamanaşımına uğrar.", zorluk="hard")

P.q("TBK md. 52",
    f"{K}, aşağıdakilerden hangisi tazminatın indirilmesi veya kaldırılması sebeplerinden biri değildir?",
    "Zarar görenin zengin olması",
    ["Zarar görenin fiile razı olması",
     "Zarar görenin zararın artmasında etkili olması",
     "Zarar görenin yükümlünün durumunu ağırlaştırması",
     "Hafif kusurlu yükümlünün yoksulluğa düşecek olması"],
    "Md. 52'ye göre zarar görenin rızası, zararın doğması veya artmasında etkisi, yükümlünün durumunu ağırlaştırması ve hafif "
    "kusurlu yükümlünün yoksulluğa düşecek olması indirim sebebidir; zarar görenin zenginliği sayılmamıştır.")

P.q("TBK md. 53",
    f"{K}, aşağıdakilerden hangisi ölüm hâlinde uğranılan zararlar arasında sayılmamıştır?",
    "Mirasçıların miras vergisi",
    ["Cenaze giderleri",
     "Ölüm hemen gerçekleşmemişse tedavi giderleri",
     "Çalışma gücünün yitirilmesinden doğan kayıplar",
     "Destekten yoksun kalma zararı"],
    "Md. 53'e göre ölüm hâlinde uğranılan zararlar özellikle cenaze giderleri, tedavi giderleri ve çalışma gücü kayıpları ile "
    "destekten yoksun kalanların kayıplarıdır.", zorluk="easy")

P.sayisal("TBK md. 75",
    f"{K}, bedensel zararın kapsamı karar sırasında tam belirlenemiyorsa hâkim, kararın kesinleşmesinden başlayarak kaç "
    "yıl içinde tazminat hükmünü değiştirme yetkisini saklı tutabilir?",
    "2", ["1", "3", "5", "10"],
    "Md. 75'e göre bedensel zararın kapsamı tam belirlenemiyorsa hâkim kararın kesinleşmesinden başlayarak iki yıl içinde "
    "tazminat hükmünü değiştirme yetkisini saklı tutabilir.")

P.q("TBK md. 54",
    f"{K}, bedensel zararlar arasında aşağıdakilerden hangisi yer almaz?",
    "Cenaze giderleri",
    ["Tedavi giderleri",
     "Kazanç kaybı",
     "Çalışma gücünün azalmasından doğan kayıp",
     "Ekonomik geleceğin sarsılmasından doğan kayıp"],
    "Md. 54'e göre bedensel zararlar tedavi giderleri, kazanç kaybı, çalışma gücünün azalması ve ekonomik geleceğin "
    "sarsılmasından doğan kayıplardır; cenaze gideri ölüm hâlindeki zarardır.")

P.q("TBK md. 55",
    f"{K}, destekten yoksun kalma ve bedensel zararların hesabına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tazminat hakkaniyetle artırılabilir.",
    ["Rücu edilemeyen sosyal güvenlik ödemeleri indirilemez.",
     "İfa amacı taşımayan ödemeler zarardan indirilemez.",
     "Hesap sorumluluk hukuku ilkelerine göre yapılır.",
     "Hükümler idarenin sorumluluğunda da uygulanır."],
    "Md. 55'e göre hesaplanan tazminat miktar esas alınarak hakkaniyet düşüncesiyle artırılamaz veya azaltılamaz.",
    zorluk="hard")

P.sayisal("TBK md. 82",
    f"{K}, sebepsiz zenginleşmeden doğan istem hakkı, hak sahibinin geri isteme hakkını öğrendiği tarihten başlayarak kaç "
    "yıl geçmekle zamanaşımına uğrar?",
    "2", ["1", "3", "5", "10"],
    "Md. 82'ye göre sebepsiz zenginleşmeden doğan istem öğrenmeden itibaren iki yıl ve her hâlde zenginleşmeden itibaren on "
    "yıl geçmekle zamanaşımına uğrar.")

P.q("TBK md. 55",
    f"{K26}, destekten yoksun kalma tazminatında destekten kazancının bilindiği döneme ilişkin hesaplanan tutara kanuni "
    "faiz hangi tarihten itibaren işletilir?",
    "Olay tarihinden",
    ["Karar tarihinden",
     "Dava tarihinden",
     "İhtar tarihinden",
     "Kararın kesinleştiği tarihten"],
    "Md. 55'e 7589 sayılı Kanunla 2026'da eklenen fıkraya göre kazancın bilindiği döneme ilişkin tazminat toplamına haksız fiil "
    "veya zarar doğuran olayın meydana geldiği tarihten, bilinemediği döneme ilişkin toplama ise karar tarihinden kanuni faiz "
    "işletilir.", zorluk="hard")

P.q("TBK md. 55",
    f"{K26}, çalışma gücü kaybına bağlı tazminat için tahkikat başlayıncaya kadar ifa amacıyla ödenen bedel hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Oransal olarak mahsup edilir.",
    ["Tazminattan mahsup edilemez.",
     "Tazminata eklenir.",
     "Zarar görene ayrıca iade ettirilir.",
     "Sadece manevi tazminattan düşülür."],
    "Md. 55'e 7589 sayılı Kanunla 2026'da eklenen fıkraya göre ifa amacıyla tahkikat başlayıncaya kadar ödenen bedel, ödeme "
    "tarihine göre belirlenecek tazminat miktarından oransal olarak mahsup edilir.", zorluk="hard")

P.sayisal("TBK md. 73",
    f"{K}, müteselsil sorumlunun rücu istemi her hâlde tazminatın tamamının ödendiği tarihten başlayarak kaç yıl geçmekle "
    "zamanaşımına uğrar?",
    "10", ["2", "3", "5", "20"],
    "Md. 73'e göre rücu istemi her hâlde tazminatın tamamının ödendiği tarihten başlayarak on yıl geçmekle zamanaşımına uğrar.",
    zorluk="hard")

P.q("TBK md. 56",
    f"{K}, bedensel bütünlüğün zedelenmesi hâlinde manevi tazminata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ölümde yakınlara ödenemez.",
    ["Zarar görene uygun miktarda para ödenebilir.",
     "Hâkim olayın özelliklerini gözetir.",
     "Ağır bedensel zararda yakınlara da ödenebilir.",
     "Manevi tazminat para olarak ödenir."],
    "Md. 56'ya göre ağır bedensel zarar veya ölüm hâlinde zarar görenin veya ölenin yakınlarına da manevi tazminat ödenmesine "
    "karar verilebilir.")

P.q("TBK md. 58",
    f"{K}, kişilik hakkının zedelenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kınama kararının yayımlanması istenebilir.",
    ["Sadece maddi tazminat istenebilir.",
     "Hâkim para dışında giderim biçimi belirleyemez.",
     "Manevi tazminat ancak ceza mahkümiyetiyle istenir.",
     "Kişilik hakkı zedelenmesi tazminat doğurmaz."],
    "Md. 58'e göre kişilik hakkı zedelenen manevi tazminat isteyebilir; hâkim bunun yerine veya buna ek olarak başka giderim "
    "biçimi, özellikle saldırıyı kınayan bir karar ve yayımlanmasına hükmedebilir.")

P.q("TBK md. 59",
    f"{K}, ayırt etme gücünü geçici olarak kaybeden kişinin bu sırada verdiği zarara ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Kusursuzluğunu ispatlarsa kurtulur.",
    ["Kural olarak sorumlu olmaz.",
     "Sadece hakkaniyet gereği sorumlu olur.",
     "Sorumluluk velisine geçer.",
     "Sorumluluk için kast aranır."],
    "Md. 59'a göre ayırt etme gücünü geçici olarak kaybeden kişi bu sırada verdiği zararları gidermekle yükümlüdür; ancak "
    "kaybetmede kusuru olmadığını ispat ederse sorumluluktan kurtulur.", zorluk="hard")

P.q("TBK md. 60",
    f"{K}, sorumluluğun birden çok sebebe dayandırılabildiği hâlde hâkim hangi sebebe göre karar verir?",
    "En iyi giderimi sağlayana",
    ["Zarar verene en az yük getirene",
     "İlk ileri sürülen sebebe",
     "Kusur sorumluluğuna",
     "Tarafların ortak seçimine"],
    "Md. 60'a göre sorumluluk birden çok sebebe dayandırılabiliyorsa hâkim, zarar gören aksini istemedikçe veya kanunda aksi "
    "öngörülmedikçe zarar görene en iyi giderim imkânı sağlayan sebebe göre karar verir.")

P.q("TBK md. 61",
    f"{K}, birden çok kişinin birlikte bir zarara sebebiyet vermesi hâlinde zarar görene karşı sorumlulukları nasıldır?",
    "Müteselsil sorumluluk",
    ["Kusurları oranında kısmi sorumluluk",
     "Sadece en kusurlunun sorumluluğu",
     "Eşit paylı sorumluluk",
     "Sorumluluk doğmaz"],
    "Md. 61'e göre birden çok kişi birlikte bir zarara sebebiyet verdikleri veya aynı zarardan çeşitli sebeplerle sorumlu "
    "oldukları takdirde müteselsil sorumluluk hükümleri uygulanır.", zorluk="easy")

P.q("TBK md. 62",
    f"{K}, müteselsil sorumlular arasındaki iç ilişkiye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Payından fazla ödeyen rücu hakkına sahip değildir.",
    ["Kusurun ağırlığı paylaştırmada gözetilir.",
     "Yaratılan tehlikenin yoğunluğu gözetilir.",
     "Fazla ödeyen zarar görenin haklarına halef olur.",
     "Paylaştırmada bütün durum ve koşullar dikkate alınır."],
    "Md. 62'ye göre tazminatın kendi payına düşeninden fazlasını ödeyen kişi fazla ödemesi için diğer sorumlulara rücu hakkına "
    "sahiptir ve zarar görenin haklarına halef olur.")

P.q("TBK md. 63",
    f"{K}, aşağıdakilerden hangisi fiilin hukuka aykırılığını kaldıran hâllerden biri değildir?",
    "Zarar verenin ekonomik zorluğu",
    ["Zarar görenin rızası",
     "Üstün özel veya kamusal yarar",
     "Haklı savunma",
     "Zorunluluk hâli"],
    "Md. 63'e göre kanundan doğan yetki, zarar görenin rızası, üstün yarar, haklı savunma, kendi gücüyle hakkı koruma ve "
    "zorunluluk hâlleri hukuka aykırılığı kaldırır.", zorluk="easy")

P.q("TBK md. 64",
    f"{K}, haklı savunmada bulunan kişinin saldırana verdiği zarardan sorumluluğu nasıldır?",
    "Sorumlu tutulamaz.",
    ["Tam sorumludur.",
     "Hakkaniyete göre yarı oranında sorumludur.",
     "Sadece manevi zarardan sorumludur.",
     "Kusur oranında sorumludur."],
    "Md. 64'e göre haklı savunmada bulunan saldıranın şahsına veya mallarına verdiği zarardan sorumlu tutulamaz.")

P.q("TBK md. 64",
    "(A), kendisini yakın bir zarar tehlikesinden korumak için (B)’nin arabasının camını kırmıştır."
    f"\n\n{K}, (A)’nın bu zararı giderme yükümlülüğü nasıl belirlenir?",
    "Hâkimce hakkaniyete göre belirlenir.",
    ["(A) sorumlu olmaz.",
     "(A) zararın iki katını öder.",
     "Zarar (B)’nin kendi sigortasına kalır.",
     "(A) zararın tamamını öder."],
    "Md. 64'e göre kendisini veya başkasını açık ya da yakın zarar tehlikesinden korumak için başkasının mallarına zarar verenin "
    "giderim yükümlülüğünü hâkim hakkaniyete göre belirler.", zorluk="hard")

P.q("TBK md. 65",
    f"{K}, ayırt etme gücü bulunmayan kişinin verdiği zarara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hakkaniyet gerekirse giderilir.",
    ["Kural olarak giderim istenemez.",
     "Tam kusur sorumluluğu uygulanır.",
     "Sorumluluk sadece velisine aittir.",
     "Giderim ceza mahkümiyetine bağlıdır."],
    "Md. 65'e göre hakkaniyet gerektiriyorsa hâkim ayırt etme gücü bulunmayan kişinin verdiği zararın tamamen veya kısmen "
    "giderilmesine karar verir.")

P.q("TBK md. 66",
    f"{K}, adam çalıştıranın sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Adam çalıştıran, çalışana tamamen rücu eder.",
    ["Çalışanın iş sırasında verdiği zarardan sorumludur.",
     "Seçme, talimat ve denetimde özeni ispatlarsa kurtulur.",
     "İşletmede çalışma düzeninin elverişliliğini ispatlamalıdır.",
     "Rücu, çalışanın bizzat sorumlu olduğu ölçüdedir."],
    "Md. 66'ya göre adam çalıştıran ödediği tazminat için zarar veren çalışana ancak onun bizzat sorumlu olduğu ölçüde rücu "
    "hakkına sahiptir.")

P.q("TBK md. 66",
    "Bir fabrikanın işçisi, forklift kullanırken iş sırasında yoldan geçen birini yaralamıştır."
    f"\n\n{K}, işveren hangi durumda sorumluluktan kurtulabilir?",
    "Gereken özeni ispatlarsa",
    ["İşçiyi hemen işten çıkarırsa",
     "Zarar görenle ceza davası sürerse",
     "İşçi deneme süresindeyse",
     "Zarar göreni daha önce tanımıyorsa"],
    "Md. 66'ya göre adam çalıştıran, çalışanını seçerken, talimat verirken, gözetim ve denetimde zararın doğmasını engellemek için "
    "gerekli özeni gösterdiğini ispat ederse sorumlu olmaz.")

P.q("TBK md. 67",
    f"{K}, hayvan bulunduranın sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gerekli özeni ispatlarsa sorumlu olmaz.",
    ["Sadece hayvanın maliki sorumludur.",
     "Kusur ispatlanmadıkça sorumlu değildir.",
     "Geçici bakım üstlenen sorumlu olmaz.",
     "Hayvan ürkütülse de rücu hakkı yoktur."],
    "Md. 67'ye göre hayvanın bakımını ve yönetimini sürekli veya geçici üstlenen kişi zararı giderir; gerekli özeni gösterdiğini "
    "ispat ederse sorumlu olmaz; ürkütenlere rücu hakkı saklıdır.")

P.q("TBK md. 68",
    f"{K}, başkasının hayvanı taşınmazda zarar verdiğinde taşınmaz zilyedinin hakkı aşağıdakilerden hangisidir?",
    "Zarar giderilene dek alıkoymak",
    ["Hayvanı mülkiyetine geçirmek",
     "Hayvanı satıp bedelini almak",
     "Hayvan sahibine para cezası kesmek",
     "Hayvanı bilgi vermeden süresiz saklamak"],
    "Md. 68'e göre taşınmazın zilyedi hayvanı yakalayıp zarar giderilinceye kadar alıkoyabilir; derhâl hayvan sahibine bilgi "
    "vermek zorundadır.")

P.q("TBK md. 69",
    f"{K}, yapı malikinin sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Malik kusursuzluğunu ispatla sorumluluktan kurtulur.",
    ["Yapım bozukluğundan doğan zararı giderir.",
     "Bakım eksikliğinden doğan zararı giderir.",
     "İntifa hakkı sahibi malikle müteselsilen sorumludur.",
     "Sorumlu olanlara rücu hakkı saklıdır."],
    "Md. 69'a göre yapı malikinin sorumluluğu kusursuz sorumluluktur; malik kusursuz olsa da yapım bozukluğu veya bakım "
    "eksikliğinden doğan zarardan sorumludur.", zorluk="hard")

P.q("TBK md. 70",
    f"{K}, başkasına ait yapıdan zarar görme tehlikesiyle karşılaşan kişi aşağıdakilerden hangisini isteyebilir?",
    "Gerekli önlemlerin alınmasını",
    ["Yapının kendisine devrini",
     "Malikin yapıyı derhal satmasını",
     "Belediyeden tazminat ödenmesini",
     "Yapının kendisi tarafından yıkılmasını"],
    "Md. 70'e göre başkasına ait yapıdan zarar görme tehlikesiyle karşılaşan kişi tehlikenin giderilmesi için gerekli önlemlerin "
    "alınmasını hak sahiplerinden isteyebilir.")

P.q("TBK md. 71",
    f"{K}, önemli ölçüde tehlike arz eden işletmenin faaliyetinden doğan zarardan kim sorumludur?",
    "Sahibi ve işleten müteselsilen",
    ["Sadece işletmede çalışan işçi",
     "Sadece işletmenin sigortacısı",
     "Sadece işletmeye izin veren idare",
     "İşletmenin alacaklıları"],
    "Md. 71'e göre önemli ölçüde tehlike arz eden bir işletmenin faaliyetinden zarar doğarsa işletme sahibi ve varsa işleten "
    "müteselsilen sorumludur.", zorluk="easy")

P.q("TBK md. 71",
    f"{K}, bir işletmenin önemli ölçüde tehlike arz ettiğinin kabulüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Uzman özenine rağmen zarar doğurabilmesi",
    ["İşletmenin büyük sermayeli olması",
     "İşletmenin çok işçi çalıştırması",
     "İşletmenin şehir merkezinden uzakta kurulmuş olması",
     "İşletmenin sigortasının bulunmaması"],
    "Md. 71'e göre işletme, uzman bir kişiden beklenen tüm özen gösterilse bile sıkça veya ağır zararlar doğurmaya elverişliyse "
    "önemli ölçüde tehlike arz eden işletme sayılır.")

P.q("TBK md. 72",
    f"{K}, tazminat ceza kanunlarının daha uzun zamanaşımı öngördüğü bir fiilden doğmuşsa hangi süre uygulanır?",
    "Ceza zamanaşımı süresi",
    ["İki yıllık süre",
     "On yıllık süre",
     "Beş yıllık süre",
     "Tarafların sözleşmeyle belirleyeceği süre"],
    "Md. 72'ye göre tazminat, ceza kanunlarının daha uzun bir zamanaşımı öngördüğü cezayı gerektiren bir fiilden doğmuşsa bu "
    "zamanaşımı uygulanır.")

P.q("TBK md. 72",
    "Haksız fiil sonucu zarar gören (A), aldatılarak bir borç altına sokulmuştur; tazminat istemi zamanaşımına uğramıştır."
    f"\n\n{K}, (A) bu borç hakkında ne yapabilir?",
    "Borcu ifadan süresiz olarak kaçınabilir.",
    ["Borcu ifa etmekle yükümlüdür.",
     "Borç doğrudan düşer.",
     "Sadece yarısını öder.",
     "Borcu faizsiz öder."],
    "Md. 72/3'e göre haksız fiil dolayısıyla zarar gören bakımından bir borç doğmuşsa zarar gören, tazminat istemi zamanaşımına "
    "uğramış olsa bile her zaman bu borcu ifadan kaçınabilir.", zorluk="hard")

P.q("TBK md. 73",
    f"{K}, tazminatın ödenmesi kendisinden istenen kişinin birlikte sorumlulara bildirim yükümlülüğüne ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Zamanaşımı bildirim zamanında başlar.",
    ["Bildirim yükümlülüğü yoktur.",
     "Bildirmezse rücu hakkı düşer.",
     "Bildirim sadece noter aracılığıyla yapılır.",
     "Bildirmezse tazminatın iki katını öder."],
    "Md. 73'e göre tazminatın ödenmesi istenen kişi durumu birlikte sorumlulara bildirmek zorundadır; aksi hâlde zamanaşımı "
    "bildirimin dürüstlük kurallarına göre yapılabileceği tarihte işlemeye başlar.", zorluk="hard")

P.q("TBK md. 74",
    f"{K}, hukuk hâkiminin ceza hukukuyla ilişkisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hukuk hâkimi ceza mahkemesinin beraat kararıyla bağlıdır.",
    ["Kusur konusunda ceza hükümleriyle bağlı değildir.",
     "Ayırt etme gücü konusunda ceza hükümleriyle bağlı değildir.",
     "Ceza hâkiminin zarar tespiti hukuk hâkimini bağlamaz.",
     "Ceza hâkiminin kusur değerlendirmesi hukuk hâkimini bağlamaz."],
    "Md. 74'e göre hâkim kusur ve ayırt etme gücü hakkında karar verirken ceza hâkimince verilen beraat kararıyla bağlı değildir.")

P.q("TBK md. 76",
    f"{K}, geçici ödemeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hükmedilmezse faiziyle iade edilir.",
    ["Kural olarak geri istenmez.",
     "Hâkim istem olmadan resen karar verir.",
     "Geçici ödeme tazminattan mahsup edilmez.",
     "Geçici ödeme için kanıt aranmaz."],
    "Md. 76'ya göre inandırıcı kanıt ve ekonomik durum gerektirirse istem üzerine geçici ödemeye karar verilebilir; ödemeler "
    "tazminattan mahsup edilir, tazminata hükmedilmezse yasal faiziyle geri verilir.")

P.q("TBK md. 77",
    f"{K}, sebepsiz zenginleşmenin doğduğu hâller arasında aşağıdakilerden hangisi yer almaz?",
    "Geçerli bir sözleşmeye dayanan ödeme",
    ["Geçerli olmayan sebebe dayanan zenginleşme",
     "Gerçekleşmemiş sebebe dayanan zenginleşme",
     "Sona ermiş sebebe dayanan zenginleşme",
     "Başkasının emeğinden haksız zenginleşme"],
    "Md. 77'ye göre haklı bir sebep olmaksızın zenginleşen geri vermekle yükümlüdür; yükümlülük özellikle geçerli olmayan, "
    "gerçekleşmemiş veya sona ermiş bir sebebe dayanan zenginleşmede doğar.", zorluk="easy")

P.q("TBK md. 78",
    f"{K}, borçlanılmamış edimi kendi isteğiyle ifa eden kişinin geri isteyebilmesi için ne ispat etmesi gerekir?",
    "Kendisini borçlu sanarak ifa ettiğini",
    ["Karşı tarafın kötü niyetli olduğunu",
     "Ödemenin nakit yapıldığını",
     "Ödemenin bir yıl içinde yapıldığını",
     "Ödemeyi noter aracılığıyla yaptığını"],
    "Md. 78'e göre borçlanmadığı edimi kendi isteğiyle yerine getiren, bunu ancak kendisini borçlu sanarak yerine getirdiğini "
    "ispat ederse geri isteyebilir.")

P.q("TBK md. 78",
    f"{K}, aşağıdaki ödemelerden hangisi sebepsiz zenginleşme hükümlerine göre geri istenemez?",
    "Zamanaşımına uğramış borcun ifası",
    ["Borçlu sanılarak yapılan ödeme",
     "Hükümsüz sözleşmeye dayanan ödeme",
     "İki kez yapılan aynı ödeme",
     "Gerçekleşmeyen sebebe dayanan ödeme"],
    "Md. 78'e göre zamanaşımına uğramış bir borcun ifasından veya ahlaki bir ödevin yerine getirilmesinden kaynaklanan "
    "zenginleşmeler geri istenemez.")

P.q("TBK md. 79",
    f"{K}, iyiniyetli olmaksızın zenginleşmeyi elden çıkaran kişinin geri verme yükümlülüğüne ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Zenginleşmenin tamamını geri verir.",
    ["Elinde kalan kısmı geri verir.",
     "Geri verme yükümlülüğü sona erer.",
     "Yarısını geri verir.",
     "Sadece faizini öder."],
    "Md. 79'a göre zenginleşen, zenginleşmeyi iyiniyetli olmaksızın veya geri vermeyi hesaba katması gerekirken elden çıkarmışsa "
    "tamamını geri vermekle yükümlüdür.", zorluk="hard")

P.q("TBK md. 80",
    f"{K}, iyiniyetli olmayan zenginleşenin giderleri isteme hakkına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yararlı giderlerin tamamını isteyebilir.",
    ["Zorunlu giderlerini isteyebilir.",
     "Yararlı giderlerden mevcut değer artışını isteyebilir.",
     "Diğer giderlerini isteyemez.",
     "Zararsızca ayrılabilen eklemeleri alabilir."],
    "Md. 80'e göre iyiniyetli olmayan zenginleşen zorunlu giderlerini ve yararlı giderlerinden sadece geri verme zamanında mevcut "
    "olan değer artışını isteyebilir.", zorluk="hard")

P.q("TBK md. 81",
    f"{K}, hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Geri istenemez.",
    ["Kural olarak geri istenebilir.",
     "Yarısı geri istenebilir.",
     "Faiziyle birlikte geri verilir.",
     "Verenin mülkiyetinde kalır."],
    "Md. 81'e göre hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey geri istenemez; açılan davada hâkim "
    "bu şeyin Devlete mal edilmesine karar verebilir.")

P.q("TBK md. 82",
    f"{K}, sebepsiz zenginleşme istemi her hâlde zenginleşmenin gerçekleştiği tarihten başlayarak kaç yıl geçmekle "
    "zamanaşımına uğrar?",
    "On yıl",
    ["İki yıl", "Beş yıl", "Bir yıl", "Yirmi yıl"],
    "Md. 82'ye göre sebepsiz zenginleşme istemi her hâlde zenginleşmenin gerçekleştiği tarihten başlayarak on yıl geçmekle "
    "zamanaşımına uğrar.")

P.oncul("TBK md. 66-71",
    f"{K} aşağıdaki sorumluluk hâlleri değerlendirilmektedir:",
    ["Adam çalıştıranın sorumluluğu",
     "Hayvan bulunduranın sorumluluğu",
     "Önemli ölçüde tehlike arz eden işletme sahibinin sorumluluğu",
     "Genel haksız fiil sorumluluğu"],
    "Yukarıdakilerden hangileri özen sorumluluğu niteliğindedir?",
    "I ve II",
    ["Yalnız I", "I ve II", "II ve III", "III ve IV", "I, II ve III"],
    "TBK sistematiğinde adam çalıştıran (I) ve hayvan bulunduran (II) sorumluluğu özen sorumluluğu başlığı altındadır; tehlike "
    "sorumluluğu (III) ayrı bir kusursuz sorumluluk türü, genel haksız fiil (IV) ise kusur sorumluluğudur.", zorluk="hard")

P.q("TBK md. 57",
    f"{K}, gerçek olmayan haberlerin yayılması yüzünden müşterileri azalan kişinin istemlerine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Sona erdirilmesini isteyebilir.",
    ["Sadece ceza davası açabilir.",
     "Kusur olmasa da tazminat alır.",
     "Ticari işlerde de sadece TBK uygulanır.",
     "Bir istemde bulunamaz."],
    "Md. 57'ye göre müşterileri azalan kişi bu davranışlara son verilmesini ve kusur varsa zararının giderilmesini isteyebilir; "
    "ticari işlerde TTK hükümleri saklıdır.")

P.q("TBK md. 69",
    "Bir apartman dairesinin intifa hakkı sahibi, balkondaki bakım eksikliği nedeniyle düşen saksının yayaya zarar vermesinden "
    f"dolayı dava edilmiştir.\n\n{K}, intifa hakkı sahibinin sorumluluğu nasıldır?",
    "Malikle birlikte müteselsilen sorumludur.",
    ["Sorumlu değildir.",
     "Sadece malik sorumludur.",
     "Sadece kusuru varsa yarı oranda sorumludur.",
     "Sadece yöneticiye rücu edebilir, kendisi sorumlu değildir."],
    "Md. 69'a göre intifa ve oturma hakkı sahipleri binanın bakımındaki eksikliklerden doğan zararlardan malikle birlikte "
    "müteselsilen sorumludur.", zorluk="hard")

P.q("TBK md. 51",
    f"{K}, tazminatın irat biçiminde ödenmesine hükmedilmesi hâlinde borçlunun yükümlülüğü aşağıdakilerden hangisidir?",
    "Güvence göstermek",
    ["Tazminatı peşin ödemek",
     "Faiz ödememek",
     "Sigorta yaptırmamak",
     "Tazminatın yarısını mahkemeye yatırmak"],
    "Md. 51'e göre tazminatın irat biçiminde ödenmesine hükmedilirse borçlu güvence göstermekle yükümlüdür.")

P.q("TBK md. 80",
    f"{K}, iyiniyetli zenginleşenin gider isteme hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zorunlu ve yararlı giderlerini isteyebilir.",
    ["Bir gider isteyemez.",
     "Sadece lüks giderlerini isteyebilir.",
     "Sadece zorunlu giderlerin yarısını isteyebilir.",
     "Tüm giderlerini, lüks olanlar dahil isteyebilir."],
    "Md. 80'e göre iyiniyetli zenginleşen yaptığı zorunlu ve yararlı giderleri geri verme isteminde bulunandan isteyebilir; "
    "diğer giderlerini isteyemez.")

P.q("TBK md. 53",
    f"{K}, ölüm hâlinde destekten yoksun kalma zararının giderilmesini kimler isteyebilir?",
    "Ölenin desteğinden yoksun kalan kişiler",
    ["Sadece ölenin mirasçıları",
     "Sadece ölenin eşi",
     "Ölenin alacaklıları",
     "Ölenin işvereni"],
    "Md. 53'e göre ölenin desteğinden yoksun kalan kişilerin bu sebeple uğradıkları kayıplar ölüm hâlinde giderilecek zararlar "
    "arasındadır; destek ilişkisi mirasçılıktan bağımsızdır.")

P.q("TBK md. 62",
    f"{K}, müteselsil sorumlular arasında tazminatın paylaştırılmasında özellikle gözetilen unsurlar aşağıdakilerden "
    "hangisidir?",
    "Kusurun ağırlığı ve tehlikenin yoğunluğu",
    ["Sorumluların ekonomik gücü",
     "Sorumluların yaşları",
     "Sorumluların sayısına göre eşit pay",
     "Zarar görenin tercihi"],
    "Md. 62'ye göre paylaştırmada bütün durum ve koşullar, özellikle her birine yüklenebilecek kusurun ağırlığı ve yarattıkları "
    "tehlikenin yoğunluğu göz önünde tutulur.")

P.q("TBK md. 64",
    f"{K}, hakkını kendi gücüyle koruyan kişinin verdiği zarardan sorumlu tutulmaması için aranan koşullar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Karşı tarafın rıza göstermesi",
    ["Kolluk yardımının zamanında sağlanamaması",
     "Hakkın kaybını önleyecek başka yol olmaması",
     "Hakkın kullanılmasının önemli ölçüde zorlaşacak olması",
     "Durum ve koşulların bunu gerektirmesi"],
    "Md. 64'e göre hakkını kendi gücüyle koruyan kişi, kolluk yardımını zamanında sağlayamayacaksa ve hakkının kaybını veya "
    "kullanılmasının önemli ölçüde zorlaşmasını önleyecek başka yol yoksa verdiği zarardan sorumlu tutulamaz.", zorluk="hard")

P.q("TBK md. 66",
    f"{K}, bir işletmede adam çalıştıran, işletme faaliyetinden doğan zarardan hangi durumda sorumlu olmaz?",
    "Çalışma düzeni zararı önlemeye elverişliyse",
    ["İşletmenin sigortası bulunuyorsa",
     "Zarar gören işletme müşterisiyse",
     "Zarara çalışanlardan biri yol açtıysa",
     "İşletme kâr amacı gütmüyorsa"],
    "Md. 66'ya göre bir işletmede adam çalıştıran, işletmenin çalışma düzeninin zararın doğmasını önlemeye elverişli olduğunu "
    "ispat etmedikçe işletme faaliyetinden doğan zarardan sorumludur.", zorluk="hard")

P.q("TBK md. 71",
    f"{K}, tehlike sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşletme sahibi özen ispatıyla kurtulur.",
    ["Sahibi ve işleten müteselsilen sorumludur.",
     "Özel kanundaki tehlike hâli de kapsama girer.",
     "Özel sorumluluk hükümleri saklıdır.",
     "Uzman özenine rağmen zarar doğabilen işletmedir."],
    "Md. 71'e göre tehlike sorumluluğu kusursuz bir sorumluluktur; işletme sahibi ve işleten, gerekli özeni gösterdiğini ispat "
    "ederek sorumluluktan kurtulamaz.", zorluk="hard")

P.q("TBK md. 79",
    f"{K}, sebepsiz zenginleşen kural olarak neyi geri vermekle yükümlüdür?",
    "Elinden çıktığını ispatladığı kısım dışında kalanı",
    ["Zenginleşmenin faiziyle birlikte iki katını",
     "Sadece zenginleşmenin elden çıkan kısmını",
     "Zenginleşmenin yarısını ve giderleri",
     "Sadece zenginleşmeden doğan faizleri"],
    "Md. 79'a göre sebepsiz zenginleşen, geri istenmesi sırasında elinden çıkmış olduğunu ispat ettiği kısmın dışında kalanı "
    "geri vermekle yükümlüdür.")

P.q("TBK md. 82",
    "Sebepsiz zenginleşme, zenginleşenin (B)’ye karşı bir alacak hakkı kazanmasıyla gerçekleşmiştir; (B)’nin geri isteme "
    f"hakkı zamanaşımına uğramıştır.\n\n{K}, (B) bu borç hakkında ne yapabilir?",
    "Borcunu ifadan kaçınabilir.",
    ["Borcu ifa etmekle yükümlüdür.",
     "Alacak doğrudan düşer.",
     "Borcun yarısını öder.",
     "Borcu faiziyle öder."],
    "Md. 82'ye göre zenginleşme zenginleşenin bir alacak hakkı kazanmasıyla gerçekleşmişse diğer taraf istem hakkı zamanaşımına "
    "uğramış olsa bile her zaman bu borcunu ifadan kaçınabilir.", zorluk="hard")

P.q("TBK md. 50",
    f"{K}, uğranılan zararın miktarı tam olarak ispat edilemiyorsa hâkim ne yapar?",
    "Hakkaniyete uygun olarak belirler.",
    ["Davayı reddeder.",
     "Emsal kira bedelini esas alır.",
     "Bilirkişisiz tazminata hükmedemez.",
     "Zarar görenin beyanını esas alır."],
    "Md. 50'ye göre zararın miktarı tam olarak ispat edilemiyorsa hâkim olayların olağan akışını ve zarar görenin aldığı "
    "önlemleri göz önünde tutarak miktarı hakkaniyete uygun olarak belirler.")

P.q("TBK md. 54",
    f"{K}, aşağıdakilerden hangisi bedensel zararlar arasında sayılmıştır?",
    "Ekonomik geleceğin sarsılması",
    ["Cenaze giderleri",
     "Mirasın paylaşım gideri",
     "Destekten yoksun kalma",
     "Ölenin borçlarının ödenmesi"],
    "Md. 54'e göre bedensel zararlar tedavi giderleri, kazanç kaybı, çalışma gücünün azalmasından ve ekonomik geleceğin "
    "sarsılmasından doğan kayıplardır.", zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
