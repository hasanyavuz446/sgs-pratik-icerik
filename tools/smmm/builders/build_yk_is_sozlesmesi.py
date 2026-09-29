# -*- coding: utf-8 -*-
"""Hukuk · İş Hukuku · İş Sözleşmesi ve Ücret — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında İş Kanunu soruları; deneme süresi, çalışma süreleri, yeni iş arama izni, toplu işçi
çıkarma bildirimi ve yönetmelik yetkisi gibi kısa, kanun adıyla başlayan ve süre soran kalıplarla gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 4857 sayılı İş Kanunu md. 1-4, 6-16, 22, 28, 32-39.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_is_sozlesmesi_2026.json", lesson="is_hukuku", topic="is_sozlesmesi",
          konu_adi="İş Sözleşmesi", seed=2026093001,
          surum="4857 sayılı İş Kanunu güncel metni; 29.09.2026 kontrolü")

K = "4857 sayılı İş Kanunu’na göre"
K26 = "4857 sayılı İş Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İK md. 15",
    f"{K}, iş sözleşmesine konulan deneme süresi, toplu iş sözleşmesiyle uzatılmadıkça en çok kaç ay olabilir?",
    "2", ["1", "3", "4", "6"],
    "Md. 15'e göre deneme süresi en çok iki ay olabilir; toplu iş sözleşmeleriyle dört aya kadar uzatılabilir.",
    zorluk="easy")

P.q("İK md. 4",
    f"{K26}, aşağıdaki işlerden hangisinde Kanun hükümleri uygulanır?",
    "Havacılık yer tesislerindeki işler",
    ["Ev hizmetleri", "Deniz taşıma işleri", "Profesyonel sporcuların çalışmaları", "Çırakların çalışmaları"],
    "Md. 4'e göre deniz ve hava taşıma işleri, ev hizmetleri, sporcular ve çıraklar Kanun kapsamı dışındadır; ancak havacılığın "
    "bütün yer tesislerinde yürütülen işler Kanuna tabidir.", zorluk="hard")

P.q("İK md. 4",
    f"{K26}, aşağıdakilerden hangisi Kanunun uygulanmadığı iş ve iş ilişkilerinden biri değildir?",
    "Limanlarda gemiden karaya yükleme işleri",
    ["Ev hizmetleri", "Sporculara ilişkin iş ilişkileri", "Rehabilite edilenler",
     "50 ve daha az işçi çalıştıran tarım işyerleri"],
    "Md. 4'e göre ev hizmetleri, sporcular, rehabilite edilenler ve 50'den az (50 dahil) işçili tarım ve orman işyerleri kapsam "
    "dışıdır; kıyı, liman ve iskelelerde gemilerden karaya yükleme ve boşaltma işleri ise Kanuna tabidir.")

P.sayisal("İK md. 8",
    f"{K26}, süresi en az kaç yıl olan iş sözleşmelerinin yazılı şekilde yapılması zorunludur?",
    "1", ["2", "3", "5", "10"],
    "Md. 8'e göre süresi bir yıl ve daha fazla olan iş sözleşmelerinin yazılı yapılması zorunludur; bu belgeler damga vergisi "
    "ile her çeşit resim ve harçtan muaftır.", zorluk="easy")

P.q("İK md. 2",
    f"{K26}, işveren vekilinin işçilere karşı işlem ve yükümlülüklerinden kim sorumludur?",
    "Doğrudan işveren",
    ["Sadece işveren vekili", "İşveren vekili ve işçi temsilcisi", "Çalışma ve Sosyal Güvenlik Bakanlığı",
     "İşyerinin bağlı olduğu belediye"],
    "Md. 2'ye göre işveren vekilinin bu sıfatla işçilere karşı işlem ve yükümlülüklerinden doğrudan işveren sorumludur; işveren "
    "için öngörülen sorumluluklar işveren vekilleri hakkında da uygulanır.", zorluk="easy")

P.q("İK md. 2",
    "Bir fabrika, ürettiği malla nitelik yönünden bağlılığı olan ve aynı yönetim altında örgütlenen depoyu, işçilerin yemek "
    f"yediği yemekhaneyi ve servis araçlarını kullanmaktadır.\n\n{K}, bunlar hakkında aşağıdakilerden hangisi doğrudur?",
    "Hepsi işyerinden sayılır.",
    ["Sadece depo işyerinden sayılır.",
     "Servis araçları işyerinden sayılmaz.",
     "Yemekhane işyerinin eklentisi değildir.",
     "Sadece üretimin yapıldığı bina işyeridir."],
    "Md. 2'ye göre işyerine bağlı yerler ile dinlenme, emzirme, yemek, uyku, yıkanma, muayene ve eğitim gibi eklentiler ve "
    "araçlar da işyerinden sayılır; işyeri bunlarla birlikte bir bütündür.")

P.sayisal("İK md. 8",
    "Bir işveren, yazılı sözleşme yapmadan belirsiz süreli olarak işe aldığı işçiye çalışma koşullarını gösteren belgeyi "
    f"vermemiştir.\n\n{K}, işveren bu belgeyi işçiye en geç kaç ay içinde vermekle yükümlüdür?",
    "2", ["1", "3", "4", "6"],
    "Md. 8'e göre yazılı sözleşme yapılmayan hâllerde işveren işçiye en geç iki ay içinde genel ve özel çalışma koşullarını, "
    "çalışma süresini, ücreti ve fesih hükümlerini gösteren yazılı bir belge verir.")

P.q("İK md. 2",
    f"{K26}, asıl işveren-alt işveren ilişkisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Asıl işin tamamı alt işverene verilebilir.",
    ["Yardımcı işlerde alt işveren ilişkisi kurulabilir.",
     "Asıl iş, teknolojik nedenlerle uzmanlık gerektiriyorsa kısmen verilebilir.",
     "Asıl işveren, alt işveren işçilerine karşı birlikte sorumludur.",
     "Önceki işçiler alt işverene alınarak hakları kısıtlanamaz."],
    "Md. 2'ye göre alt işverene yardımcı işler veya asıl işin işletmenin ve işin gereği ile teknolojik nedenlerle uzmanlık "
    "gerektiren bir bölümü verilebilir; asıl işin tamamı verilemez. Asıl işveren alt işveren işçilerine karşı birlikte "
    "sorumludur.", zorluk="hard")

P.q("İK md. 6",
    f"{K26}, işyeri devrine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Devir, işçi yönünden haklı fesih sebebidir.",
    ["İş sözleşmeleri bütün hak ve borçlarıyla devralana geçer.",
     "Kıdeme bağlı haklarda işe başlama tarihi esas alınır.",
     "İşveren sözleşmeyi sırf devir nedeniyle feshedemez.",
     "İflas tasfiyesi yoluyla devirde bu hükümler uygulanmaz."],
    "Md. 6'ya göre devir hâlinde iş sözleşmeleri hak ve borçlarıyla devralana geçer, kıdem işçinin devredende işe başladığı "
    "tarihe göre hesaplanır; işveren sırf devir nedeniyle feshedemez ve devir işçi için haklı fesih sebebi oluşturmaz.")

P.sayisal("İK md. 10",
    f"{K26}, nitelikleri bakımından en çok kaç iş günü süren işler süreksiz iş sayılır?",
    "30", ["7", "15", "45", "60"],
    "Md. 10'a göre nitelikleri bakımından en çok otuz iş günü süren işlere süreksiz iş, bundan fazla devam edenlere sürekli "
    "iş denir.")

P.q("İK md. 6",
    "(GHI) A.Ş., (JKL) A.Ş. ile birleşerek tüzel kişiliğini kaybetmiştir. Birleşmeden önce doğmuş işçi alacakları "
    f"bulunmaktadır.\n\n{K}, bu durumda birlikte sorumluluk hükümleri hakkında aşağıdakilerden hangisi doğrudur?",
    "Birlikte sorumluluk hükümleri uygulanmaz.",
    ["Devreden ve devralan iki yıl birlikte sorumludur.",
     "Devreden şirket beş yıl sorumlu kalır.",
     "Sadece devreden şirket sorumludur.",
     "Sorumluluk işçilerin onayına bağlıdır."],
    "Md. 6'ya göre tüzel kişiliğin birleşme veya katılma ya da türünün değişmesiyle sona ermesi hâlinde birlikte sorumluluk "
    "hükümleri uygulanmaz; alacaklar birleşilen kişiye geçer.", zorluk="hard")

P.q("İK md. 7",
    f"{K}, aşağıdaki işyerlerinden hangisinde özel istihdam bürosu aracılığıyla geçici iş ilişkisi kurulamaz?",
    "Yer altında maden çıkarılan işyeri",
    ["Mevsimlik tarım işleri", "Ev hizmetleri", "Aralıklı gördürülen işler", "Acil iş sağlığı ve güvenliği işleri"],
    "Md. 7'ye göre toplu işçi çıkarılan işyerlerinde sekiz ay süresince, kamu kurumlarında ve yer altında maden çıkarılan "
    "işyerlerinde özel istihdam bürosu aracılığıyla geçici iş ilişkisi kurulamaz.", zorluk="hard")

P.sayisal("İK md. 14",
    "Çağrı üzerine çalışmaya dayalı bir iş sözleşmesinde taraflar, işçinin hafta, ay veya yıl gibi bir zaman diliminde ne "
    f"kadar çalışacağını belirlememiştir.\n\n{K}, bu durumda haftalık çalışma süresi kaç saat kararlaştırılmış sayılır?",
    "20", ["10", "15", "30", "45"],
    "Md. 14'e göre çağrı üzerine çalışmada süre belirlenmemişse haftalık çalışma süresi yirmi saat kararlaştırılmış sayılır; "
    "işçi çalıştırılsın veya çalıştırılmasın bu süre için ücrete hak kazanır.")

P.q("İK md. 7",
    f"{K26}, geçici iş ilişkisinin kurulabileceği yollar arasında aşağıdakilerden hangisi yer alır?",
    "Holding bünyesinde başka işyerinde görevlendirme",
    ["İşçinin rızası olmadan rakip işyerine devri",
     "Belediye aracılığıyla vatandaşlara işçi kiralanması",
     "Ticaret odası aracılığıyla işçi devri",
     "Sendika aracılığıyla geçici işçi sağlanması"],
    "Md. 7'ye göre geçici iş ilişkisi, özel istihdam bürosu aracılığıyla ya da holding bünyesinde veya aynı şirketler "
    "topluluğuna bağlı başka bir işyerinde görevlendirme yapılarak kurulabilir.")

P.q("İK md. 11",
    f"{K26}, belirli süreli iş sözleşmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Esaslı neden olmasa da zincirleme yapılabilir.",
    ["Objektif koşullara bağlı olarak yapılır.",
     "Yazılı şekilde yapılır.",
     "Esaslı nedenle zincirleme yapılabilir.",
     "Süreye bağlanmayan sözleşme belirsiz sayılır."],
    "Md. 11'e göre belirli süreli sözleşme objektif koşullara bağlı ve yazılı yapılır; esaslı neden olmadıkça zincirleme "
    "yapılamaz, aksi hâlde başlangıçtan itibaren belirsiz süreli kabul edilir.")

P.sayisal("İK md. 14",
    f"{K}, çağrı üzerine çalışmada işveren, aksi kararlaştırılmadıkça çağrıyı işçinin çalışacağı zamandan en az kaç gün "
    "önce yapmalıdır?",
    "4", ["1", "2", "3", "7"],
    "Md. 14'e göre işveren çağrıyı, aksi kararlaştırılmadıkça işçinin çalışacağı zamandan en az dört gün önce yapar; "
    "sözleşmede günlük süre yoksa her çağrıda işçi en az dört saat üst üste çalıştırılır.")

P.q("İK md. 11",
    "Bir işveren, esaslı bir neden olmaksızın aynı işçiyle üst üste dört kez altışar aylık belirli süreli iş sözleşmesi "
    f"yapmıştır.\n\n{K}, bu sözleşmenin niteliği nedir?",
    "Başlangıçtan itibaren belirsiz süreli sayılır.",
    ["Son sözleşmeden itibaren belirsiz süreli sayılır.",
     "Belirli süreli olma niteliğini korur.",
     "Kısmi süreli iş sözleşmesine dönüşür.",
     "Süreksiz iş sözleşmesi sayılır."],
    "Md. 11'e göre belirli süreli iş sözleşmesi esaslı bir neden olmadıkça zincirleme yapılamaz; aksi hâlde iş sözleşmesi "
    "başlangıçtan itibaren belirsiz süreli kabul edilir.", zorluk="hard")

P.q("İK md. 9",
    f"{K26}, iş sözleşmesinin türüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tür, ihtiyaca göre Kanun sınırları içinde belirlenir.",
    ["İş sözleşmesi sadece belirsiz süreli yapılabilir.",
     "Kısmi süreli sözleşme deneme süreli olamaz.",
     "Tür, Bakanlık onayıyla belirlenir.",
     "Belirli süreli sözleşme sadece kamu kurumlarında yapılır."],
    "Md. 9'a göre taraflar iş sözleşmesini Kanunun getirdiği sınırlamalar saklı kalmak koşuluyla ihtiyaçlarına uygun türde "
    "düzenleyebilir; sözleşmeler belirli veya belirsiz, tam veya kısmi süreli ya da deneme süreli olabilir.")

P.sayisal("İK md. 6",
    "(ABC) Ltd. Şti. işyerini 1 Mart 2026’da (DEF) A.Ş.’ye hukuki bir işlemle devretmiştir. Devirden önce doğmuş ve devir "
    f"tarihinde ödenmesi gereken işçi alacakları bulunmaktadır.\n\n{K}, devreden işverenin bu borçlardan sorumluluğu devir "
    "tarihinden itibaren kaç yıl ile sınırlıdır?",
    "2", ["1", "3", "5", "10"],
    "Md. 6'ya göre devirden önce doğmuş ve devir tarihinde ödenmesi gereken borçlardan devreden ve devralan birlikte sorumludur; "
    "devreden işverenin sorumluluğu devir tarihinden itibaren iki yıl ile sınırlıdır.", zorluk="hard")

P.q("İK md. 13",
    f"{K26}, kısmi süreli çalışmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kısmi süreliye salt bu nedenle farklı işlem yapılabilir.",
    ["Kısmi süreli işçinin bölünebilir menfaatleri orantılı ödenir.",
     "Emsal işçi, aynı işte tam süreli çalışan işçidir.",
     "Tam süreliye geçme istekleri işverence dikkate alınır.",
     "Açık yerler zamanında duyurulur."],
    "Md. 13'e göre kısmi süreli işçi, ayrımı haklı kılan bir neden olmadıkça salt sözleşmesinin kısmi süreli olmasından dolayı "
    "tam süreli emsal işçiye göre farklı işleme tabi tutulamaz.")

P.q("İK md. 13",
    "Doğum izninin bitmesinden sonra Bayan (N), çocuğu mecburi ilköğretim çağına gelinceye kadar kısmi süreli çalışmak "
    f"istemektedir; eşi de çalışmaktadır.\n\n{K}, bu talep hakkında aşağıdakilerden hangisi doğrudur?",
    "Talep işverence karşılanır.",
    ["Talebi kabul etmek işverenin takdirindedir.",
     "Talep geçerli fesih nedeni sayılır.",
     "Hak sadece babaya tanınır.",
     "Talep en fazla altı ay için kabul edilir."],
    "Md. 13'e göre doğum izinlerinin bitiminden sonra mecburi ilköğretim çağının başladığı tarihi takip eden ay başına kadar "
    "ebeveynlerden biri kısmi süreli çalışma talebinde bulunabilir; talep işverence karşılanır ve geçerli fesih nedeni "
    "sayılmaz.", zorluk="hard")

P.sayisal("İK md. 7",
    "Özel istihdam bürosu aracılığıyla, üretim kapasitesindeki öngörülemeyen artış nedeniyle geçici iş ilişkisi kurulacaktır."
    f"\n\n{K}, bu hâlde geçici işçi sağlama sözleşmesi ilk olarak en fazla kaç ay süreyle kurulabilir?",
    "4", ["2", "6", "8", "12"],
    "Md. 7'ye göre bu tür hâllerde geçici işçi sağlama sözleşmesi en fazla dört ay süreyle kurulabilir; sözleşme toplam sekiz "
    "ayı geçmemek üzere en fazla iki defa yenilenebilir.", zorluk="hard")

P.q("İK md. 13",
    f"{K26}, ebeveynin kısmi süreli çalışma hakkına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eşi çalışmayan işçi de bu talepte bulunabilir.",
    ["Talep işverene en az bir ay önce yazılı bildirilir.",
     "Aynı çocuk için tam zamanlıya dönen bir daha yararlanamaz.",
     "Üç yaşını doldurmamış çocuğu evlat edinenler de yararlanır.",
     "Yerine alınan işçinin sözleşmesi, asıl işçi dönünce sona erer."],
    "Md. 13'e göre ebeveynlerden birinin çalışmaması hâlinde çalışan eş kısmi süreli çalışma talebinde bulunamaz. Bildirim en az "
    "bir ay önce yazılı yapılır; tam zamanlıya dönen aynı çocuk için tekrar yararlanamaz.", zorluk="hard")

P.q("İK md. 14",
    f"{K26}, çağrı üzerine çalışmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşçi çalıştırılmadığı sürede ücrete hak kazanmaz.",
    ["Sözleşme yazılı yapılır.",
     "Çağrı üzerine çalışma kısmi süreli bir sözleşmedir.",
     "Süreye uygun çağrıya işçi uymakla yükümlüdür.",
     "Günlük süre yoksa en az dört saat üst üste çalıştırılır."],
    "Md. 14'e göre çağrı üzerine çalıştırılmak için belirlenen sürede işçi çalıştırılsın veya çalıştırılmasın ücrete hak "
    "kazanır.")

P.sayisal("İK md. 7",
    f"{K}, geçici işçi çalıştıran işveren, sürenin sonunda aynı iş için en az kaç ay geçmedikçe yeniden geçici işçi "
    "çalıştıramaz?",
    "6", ["2", "3", "4", "12"],
    "Md. 7'ye göre geçici işçi çalıştıran işveren, belirtilen sürenin sonunda aynı iş için altı ay geçmedikçe yeniden geçici "
    "işçi çalıştıramaz.", zorluk="hard")

P.q("İK md. 14",
    f"{K26}, uzaktan çalışmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yazılı olarak kurulan bir iş ilişkisidir.",
    ["Sözlü olarak da kurulabilir.",
     "Uzaktan çalışan işçiye emsalden farklı işlem yapılabilir.",
     "İşveren, iş sağlığı ve güvenliği yükümlülüğünden kurtulur.",
     "Uzaktan çalışma sadece kamu kurumlarında uygulanır."],
    "Md. 14'e göre uzaktan çalışma, işçinin iş görme edimini evinde veya teknolojik araçlarla işyeri dışında yerine getirmesine "
    "dayalı ve yazılı olarak kurulan iş ilişkisidir; esaslı neden olmadıkça emsal işçiden farklı işlem yapılamaz.")

P.q("İK md. 15",
    f"{K26}, deneme süresine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Deneme süresinde fesih için bildirim süresine uyulur.",
    ["Deneme süresi toplu iş sözleşmesiyle dört aya uzatılabilir.",
     "Deneme süresinde sözleşme tazminatsız feshedilebilir.",
     "İşçinin çalıştığı günlerin ücreti saklıdır.",
     "Deneme kaydı sözleşmeye taraflarca konulur."],
    "Md. 15'e göre deneme süresi içinde taraflar iş sözleşmesini bildirim süresine gerek olmaksızın ve tazminatsız "
    "feshedebilir; işçinin çalıştığı günlere ait ücret ve hakları saklıdır.", zorluk="easy")

P.sayisal("İK md. 22",
    "İşveren, çalışma koşullarında esaslı değişiklik yapacağını işçiye yazılı olarak bildirmiştir."
    f"\n\n{K}, işçi bu değişikliği kaç iş günü içinde yazılı olarak kabul etmezse değişiklik işçiyi bağlamaz?",
    "6", ["3", "10", "15", "30"],
    "Md. 22'ye göre yazılı bildirime uygun yapılmayan ve işçi tarafından altı iş günü içinde yazılı olarak kabul edilmeyen "
    "değişiklikler işçiyi bağlamaz.", zorluk="easy")

P.q("İK md. 16",
    f"{K26}, takım sözleşmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Takım kılavuzu, ücretlerden aracılık kesintisi yapabilir.",
    ["Takım sözleşmesi yazılı yapılır.",
     "Her işçinin kimliği ve ücreti ayrı ayrı gösterilir.",
     "İşe başlayan her işçiyle ayrı iş sözleşmesi kurulmuş sayılır.",
     "Ücretler her işçiye ayrı ayrı ödenir."],
    "Md. 16'ya göre takım sözleşmesi yazılı yapılır, işçilerin kimliği ve ücreti ayrı gösterilir ve ücretler ayrı ayrı ödenir; "
    "takım kılavuzu için işçilerin ücretlerinden aracılık veya benzeri nedenle kesinti yapılamaz.")

P.q("İK md. 8",
    f"{K26}, iş sözleşmesinin şekline ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kanunda aksi belirtilmedikçe özel bir şekle tabi değildir.",
    ["Tüm iş sözleşmeleri noterde yapılır.",
     "Sözleşmeler damga vergisine tabidir.",
     "Sözlü sözleşme kural olarak geçersizdir.",
     "Süreksiz işlerde yazılı şekil şarttır."],
    "Md. 8'e göre iş sözleşmesi Kanunda aksi belirtilmedikçe özel bir şekle tabi değildir; bir yıl ve daha uzun süreli "
    "sözleşmeler yazılı yapılır ve bu belgeler damga vergisi ile resim ve harçtan muaftır.", zorluk="easy")

P.sayisal("İK md. 34",
    f"{K}, ücreti ödeme gününden itibaren mücbir neden dışında kaç gün içinde ödenmeyen işçi iş görme borcunu yerine "
    "getirmekten kaçınabilir?",
    "20", ["7", "10", "15", "30"],
    "Md. 34'e göre ücreti ödeme gününden itibaren yirmi gün içinde mücbir bir neden dışında ödenmeyen işçi iş görme borcunu "
    "yerine getirmekten kaçınabilir; bu grev sayılmaz.")

P.q("İK md. 32",
    f"{K26}, ücretin ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak Türk parası ile ödenir.",
    ["Sadece yabancı para ile ödenebilir.",
     "Ücret mal olarak ödenebilir.",
     "Ücret ancak elden ödenebilir.",
     "Yabancı para olarak kararlaştırılırsa Türk parası ile ödenemez."],
    "Md. 32'ye göre ücret, prim ve ikramiye kural olarak Türk parası ile işyerinde veya özel olarak açılan banka hesabına "
    "ödenir; yabancı para olarak kararlaştırılmışsa ödeme günündeki rayiçle Türk parası ile ödenebilir.", zorluk="easy")

P.q("İK md. 34",
    f"{K}, ücreti geciken işçilerin iş görmekten kaçınmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaçınma toplu nitelik kazanırsa grev sayılır.",
    ["Bu işçilerin sözleşmeleri çalışmadıkları için feshedilemez.",
     "Yerlerine yeni işçi alınamaz.",
     "Gününde ödenmeyen ücrete en yüksek mevduat faizi uygulanır.",
     "Mücbir neden varsa kaçınma hakkı doğmaz."],
    "Md. 34'e göre ücreti yirmi gün içinde ödenmeyen işçilerin kişisel kararlarıyla iş görmemesi sayısal olarak toplu nitelik "
    "kazansa dahi grev sayılmaz; bu işçilerin sözleşmeleri bu nedenle feshedilemez ve yerlerine işçi alınamaz.")

P.sayisal("İK md. 3",
    f"{K}, işyerini kuran veya faaliyetine son veren işveren, işyerine ilişkin bilgileri en geç ne kadar süre içinde "
    "bölge müdürlüğüne bildirmelidir? (ay)",
    "1", ["2", "3", "6", "12"],
    "Md. 3'e göre işyerini kuran, devralan, çalışma konusunu değiştiren veya kapatan işveren işyerinin unvan, adres, işçi "
    "sayısı ve diğer bilgilerini bir ay içinde bölge müdürlüğüne bildirmek zorundadır.")

P.q("İK md. 37",
    f"{K26}, ücret hesap pusulasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Pusula damga vergisine tabidir.",
    ["Pusula imzalı veya işyerinin özel işaretini taşır.",
     "Ödemenin günü ve ilişkin olduğu dönem gösterilir.",
     "Fazla çalışma ücretleri ayrı ayrı gösterilir.",
     "Vergi ve sigorta kesintileri ayrı ayrı gösterilir."],
    "Md. 37'ye göre işveren işçiye ücret hesabını gösteren imzalı veya özel işaretli bir pusula verir; pusulada ödeme günü, "
    "dönem, eklemeler ve kesintiler ayrı ayrı gösterilir ve bu işlemler damga vergisi ile resim ve harçtan muaftır.")

P.q("İK md. 38",
    f"{K26}, ücret kesme cezasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kesilen paralar işverenin gelirine kaydedilir.",
    ["Sözleşmede gösterilmeyen sebeple ceza verilemez.",
     "Kesinti işçiye derhal sebebiyle bildirilir.",
     "Kesinti ayda iki gündeliği aşamaz.",
     "Paralar bir ay içinde Bakanlık hesabına yatırılır."],
    "Md. 38'e göre ücret kesme cezası paraları işçilerin eğitimi ve sosyal hizmetleri için kullanılmak üzere kesildiği tarihten "
    "itibaren bir ay içinde Bakanlık hesabına yatırılır; işverenin geliri değildir.")

P.sayisal("İK md. 3",
    "İş müfettişi, asıl işveren-alt işveren ilişkisinin muvazaalı olduğunu gerekçeli raporla tespit etmiş ve rapor "
    f"işverenlere tebliğ edilmiştir.\n\n{K}, işverenler bu rapora tebliğden itibaren kaç iş günü içinde iş mahkemesine "
    "itiraz edebilir?",
    "30", ["6", "10", "15", "60"],
    "Md. 3'e göre muvazaa tespitine ilişkin müfettiş raporuna tebliğ tarihinden itibaren otuz iş günü içinde yetkili iş "
    "mahkemesine itiraz edilebilir; dava basit yargılama usulüyle dört ayda sonuçlandırılır.", zorluk="hard")

P.q("İK md. 28",
    f"{K26}, işten ayrılan işçiye verilen çalışma belgesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Belge, işin çeşidini ve süresini gösterir.",
    ["Belge sadece işçinin talebi üzerine verilir.",
     "Belge harca tabidir.",
     "Yanlış bilgi için sadece işçi tazminat isteyebilir.",
     "Belge işçinin performans notunu gösterir."],
    "Md. 28'e göre işten ayrılan işçiye işinin çeşidini ve süresini gösteren belge verilir; belgenin geç verilmesi veya yanlış "
    "bilgi içermesinden zarar gören işçi veya işçiyi işe alan yeni işveren tazminat isteyebilir; belge resim ve harçtan muaftır.")

P.q("İK md. 22",
    f"{K26}, çalışma koşullarında değişikliğe ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Değişiklik geçmişe etkili olarak yürürlüğe konulabilir.",
    ["Esaslı değişiklik işçiye yazılı bildirilir.",
     "İşçinin yazılı kabulü aranır.",
     "Taraflar anlaşarak koşulları değiştirebilir.",
     "Kabul edilmezse işveren geçerli nedenle feshedebilir."],
    "Md. 22'ye göre esaslı değişiklik yazılı bildirim ve işçinin yazılı kabulüyle yapılır; taraflar anlaşarak koşulları "
    "değiştirebilir; ancak değişiklik geçmişe etkili olarak yürürlüğe konulamaz.")

P.sayisal("İK md. 39",
    f"{K26}, ücretlerin asgari sınırları Asgari Ücret Tespit Komisyonu aracılığıyla en geç kaç yılda bir belirlenir?",
    "2", ["1", "3", "4", "5"],
    "Md. 39'a göre ücretlerin asgari sınırları Asgari Ücret Tespit Komisyonu aracılığıyla en geç iki yılda bir belirlenir; "
    "komisyon kararları kesindir.", zorluk="easy")

P.q("İK md. 12",
    f"{K26}, belirli süreli işçiye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kıdem şartında emsal işçiden farklı kıdem uygulanabilir.",
    ["Salt süreli olması nedeniyle farklı işleme tabi tutulamaz.",
     "Bölünebilir menfaatler çalışılan süreye orantılı verilir.",
     "Emsal işçi, aynı işte belirsiz süreli çalışan işçidir.",
     "Emsal yoksa işkolundaki benzer işçi dikkate alınır."],
    "Md. 12'ye göre bir çalışma şartından yararlanmak için kıdem arandığında, farklı kıdemi haklı gösteren bir neden olmadıkça "
    "belirli süreli işçi için belirsiz süreli emsal işçi hakkında esas alınan kıdem uygulanır.", zorluk="hard")

P.oncul("İK md. 4",
    f"{K} aşağıdaki işler değerlendirilmektedir:",
    ["Ev hizmetleri", "Havacılık yer tesislerindeki işler", "Deniz taşıma işleri",
     "Halka açık park ve bahçe işleri"],
    "Yukarıdakilerden hangilerinde Kanun hükümleri uygulanır?",
    "II ve IV",
    ["I ve II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"],
    "Md. 4'e göre ev hizmetleri (I) ve deniz taşıma işleri (III) kapsam dışıdır; havacılığın yer tesislerindeki işler (II) ile "
    "halkın faydalanmasına açık park ve bahçe işleri (IV) Kanuna tabidir.", zorluk="hard")

hc = 60_000 / 4
P.sayisal("İK md. 35",
    "İşçi Bay (K)’nın aylık ücreti 60.000 ₺’dir. Bay (K)’nın nafaka borcu yoktur ve bakmakla yükümlü olduğu aile üyeleri için "
    f"hâkimce takdir edilmiş bir tutar bulunmamaktadır.\n\n{K}, bu ücretin en fazla ne kadarı haczedilebilir? (₺)",
    tl(hc), secenekler(hc, 20_000, 30_000, 6_000, 60_000),
    "Md. 35'e göre işçilerin aylık ücretlerinin dörtte birinden fazlası haczedilemez veya başkasına devir ve temlik olunamaz: "
    "60.000 / 4 = 15.000 ₺. Nafaka alacaklılarının hakları saklıdır.")

P.q("İK md. 10",
    f"{K26}, süreksiz işlerde yapılan iş sözleşmelerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kanunun sayılan maddeleri yerine Borçlar Kanunu uygulanır.",
    ["İş Kanununun tüm hükümleri aynen uygulanır.",
     "Süreksiz işlerde sözleşme yapılamaz.",
     "Süreksiz işler en fazla altmış iş günü sürer.",
     "Süreksiz işlerde ücret ödenmez."],
    "Md. 10'a göre süreksiz işlerde Kanunun sayılan maddeleri (ör. fesih, kıdem ve izin hükümleri) uygulanmaz; bu konularda "
    "Borçlar Kanunu hükümleri uygulanır.")

P.q("İK md. 3",
    "Bir alt işveren, kendi işyerinin tescili için bölge müdürlüğüne başvuracaktır."
    f"\n\n{K}, alt işverenin bildirim sırasında sunması gereken belge aşağıdakilerden hangisidir?",
    "Asıl işverenden aldığı yazılı alt işverenlik sözleşmesi",
    ["Belediyeden alınan iş yeri açma ruhsatı",
     "Vergi dairesinden alınan borcu yoktur yazısı",
     "Sendikadan alınan yetki belgesi",
     "Ticaret odasından alınan faaliyet belgesi"],
    "Md. 3'e göre alt işveren, kendi işyerinin tescili için asıl işverenden aldığı yazılı alt işverenlik sözleşmesi ve gerekli "
    "belgelerle birlikte bildirim yapmakla yükümlüdür.")

kc = 1_500 * 2
P.sayisal("İK md. 38",
    "Günlük ücreti 1.500 ₺ olan işçiye, iş sözleşmesinde gösterilen bir sebep nedeniyle ücret kesme cezası verilecektir."
    f"\n\n{K}, bu işçinin ücretinden bir ayda ceza olarak en fazla ne kadar kesinti yapılabilir? (₺)",
    tl(kc), secenekler(kc, 1_500, 4_500, 7_500, 750),
    "Md. 38'e göre işçi ücretlerinden ceza olarak yapılacak kesintiler bir ayda iki gündelikten fazla olamaz: 1.500 × 2 = "
    "3.000 ₺.")

P.q("İK md. 3",
    f"{K26}, muvazaalı alt işverenlik tespitinin kesinleşmesi hâlinde aşağıdakilerden hangisi doğrudur?",
    "Alt işveren işçileri başlangıçtan itibaren asıl işverenin işçisi sayılır.",
    ["Alt işveren işçileri tespit tarihinden itibaren asıl işverenin işçisi olur.",
     "İşçilerin sözleşmeleri tespitle sona erer.",
     "Sadece idari para cezası uygulanır, işçilerin durumu değişmez.",
     "İşçiler alt işverenin işçisi olarak kalır."],
    "Md. 3'e göre rapora süresinde itiraz edilmemiş veya mahkeme muvazaa tespitini onamışsa tescil iptal edilir ve alt "
    "işverenin işçileri başlangıçtan itibaren asıl işverenin işçileri sayılır.", zorluk="hard")

P.q("İK md. 1",
    f"{K26}, işyerlerinin Kanun hükümleriyle bağlı olması hakkında aşağıdakilerden hangisi doğrudur?",
    "Bildirim gününe bakılmaksızın Kanunla bağlıdırlar.",
    ["Sadece bölge müdürlüğüne bildirildikten sonra bağlı olurlar.",
     "Sadece belirli faaliyet konularındaki işyerleri bağlıdır.",
     "İşveren vekilleri Kanun hükümleriyle bağlı değildir.",
     "Kanun sadece kamu işyerlerine uygulanır."],
    "Md. 1'e göre Kanun, istisnalar dışındaki bütün işyerlerine faaliyet konularına bakılmaksızın uygulanır; işyerleri, "
    "işverenler, işveren vekilleri ve işçiler md. 3'teki bildirim gününe bakılmaksızın Kanun hükümleriyle bağlıdır.")

ks = 30_000 * 15 / 45
P.sayisal("İK md. 13",
    "Bir işyerinde tam süreli işçiler haftada 45 saat çalışmakta ve yılda 30.000 ₺ ikramiye almaktadır. Aynı işte kısmi "
    f"süreli çalışan Bayan (L) haftada 15 saat çalışmaktadır.\n\n{K}, Bayan (L)’ye ödenmesi gereken yıllık ikramiye kaç "
    "₺’dir?",
    tl(ks), secenekler(ks, 30_000, 15_000, 5_000, 7_500),
    "Md. 13'e göre kısmi süreli çalışan işçinin ücret ve paraya ilişkin bölünebilir menfaatleri, tam süreli emsal işçiye göre "
    "çalıştığı süreye orantılı ödenir: 30.000 × 15/45 = 10.000 ₺.", zorluk="hard")

P.q("İK md. 2",
    f"{K26}, işçi ve işveren tanımlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tüzel kişiler de işçi olabilir.",
    ["İşçi, iş sözleşmesine dayanarak çalışan gerçek kişidir.",
     "Tüzel kişiler işveren olabilir.",
     "Tüzel kişiliği olmayan kurumlar da işveren olabilir.",
     "İşçi ile işveren arasındaki ilişki iş ilişkisidir."],
    "Md. 2'ye göre işçi, bir iş sözleşmesine dayanarak çalışan gerçek kişidir; işveren ise işçi çalıştıran gerçek veya tüzel kişi "
    "ya da tüzel kişiliği olmayan kurum ve kuruluşlardır.", zorluk="easy")

P.q("İK md. 7",
    f"{K}, geçici iş ilişkisinde geçici işçi çalıştıran işverenin durumuna ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Grev süresince geçici işçiyle grevdeki işçilerin işini yaptırabilir.",
    ["Sözleşme toplam sekiz ayı geçmemek üzere en fazla iki kez yenilenebilir.",
     "Sürenin sonunda aynı iş için altı ay geçmeden yeniden geçici işçi çalıştıramaz.",
     "Toplu işçi çıkarılan işyerinde sekiz ay süreyle geçici iş ilişkisi kurulamaz.",
     "Mevsimlik tarım işlerinde süre sınırı olmaksızın kurulabilir."],
    "Md. 7'ye göre geçici işçi çalıştıran işveren grev ve lokavtın uygulanması sırasında (6356 sayılı Kanunun 65. maddesi saklı "
    "kalmak kaydıyla) geçici iş ilişkisiyle işçi çalıştıramaz.", zorluk="hard")

bs = 24_000 * 6 / 12
P.sayisal("İK md. 12",
    "Bir işyerinde belirsiz süreli çalışan işçilere yılda 24.000 ₺ yakacak yardımı yapılmaktadır. Aynı işte altı ay süreli iş "
    f"sözleşmesiyle çalışan Bay (M) bu dönemin tamamında çalışmıştır.\n\n{K}, Bay (M)’ye ödenmesi gereken tutar kaç "
    "₺’dir?",
    tl(bs), secenekler(bs, 24_000, 6_000, 18_000, 2_000),
    "Md. 12'ye göre belirli süreli çalışan işçiye, belirli bir zaman ölçüt alınarak ödenecek ücret ve paraya ilişkin "
    "bölünebilir menfaatler çalıştığı süreye orantılı verilir: 24.000 × 6/12 = 12.000 ₺.")

P.q("İK md. 35",
    f"{K26}, ücretin korunmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Nafaka alacaklıları da dörtte birden fazlasını haczettiremez.",
    ["Aylık ücretin dörtte birinden fazlası haczedilemez.",
     "Ücretin dörtte birinden fazlası başkasına devredilemez.",
     "Aile üyeleri için hâkimin takdir ettiği miktar hesaba dahil edilmez.",
     "Ücretin dörtte birinden fazlası temlik edilemez."],
    "Md. 35'e göre işçilerin aylık ücretlerinin dörtte birinden fazlası haczedilemez veya devir ve temlik olunamaz; ancak nafaka "
    "borcu alacaklılarının hakları saklıdır.", zorluk="hard")

P.q("İK md. 8",
    "Bir işçi yirmi günlük belirli süreli bir iş sözleşmesiyle işe alınmış ve yazılı sözleşme yapılmamıştır."
    f"\n\n{K}, işverenin çalışma koşullarını gösteren yazılı belge verme yükümlülüğü hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Süresi bir ayı geçmediği için bu yükümlülük uygulanmaz.",
    ["Belge işe başlama günü verilmelidir.",
     "Belge iki ay içinde verilmelidir.",
     "Belge sözleşme sona erdikten sonra bir ay içinde verilir.",
     "Belge vermek işçinin talebine bağlıdır."],
    "Md. 8'e göre süresi bir ayı geçmeyen belirli süreli iş sözleşmelerinde yazılı belge verme yükümlülüğü uygulanmaz.",
    zorluk="hard")

P.sayisal("İK md. 32",
    f"{K26}, ücret alacaklarında zamanaşımı süresi kaç yıldır?",
    "5", ["1", "2", "3", "10"],
    "Md. 32'ye göre ücret alacaklarında zamanaşımı süresi beş yıldır.", zorluk="easy")

P.q("İK md. 13",
    f"{K26}, kısmi süreli iş sözleşmesinin tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Haftalık süre emsal işçiye göre önemli ölçüde azdır.",
    ["Günlük süre sekiz saati aşar.",
     "Sözleşme en fazla bir ay süreyle yapılabilir ve yenilenemez.",
     "Sadece çağrı üzerine çalışılır.",
     "İşçi ücret almaz, prim alır."],
    "Md. 13'e göre işçinin normal haftalık çalışma süresinin tam süreli emsal işçiye göre önemli ölçüde daha az belirlenmesi "
    "durumunda sözleşme kısmi süreli iş sözleşmesidir.", zorluk="easy")

P.q("İK md. 32",
    f"{K26}, ücretin ödenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ücret bono ile ödenebilir.",
    ["Ücret en geç ayda bir ödenir.",
     "Ödeme süresi sözleşmeyle bir haftaya indirilebilir.",
     "Sözleşme sona erince ücret tam olarak ödenir.",
     "Meyhane gibi yerlerde kural olarak ücret ödenemez."],
    "Md. 32'ye göre bono, kupon veya parayı temsil ettiği iddia olunan senetle ücret ödemesi yapılamaz; ücret en geç ayda bir "
    "ödenir ve bu süre sözleşmelerle bir haftaya kadar indirilebilir.")

P.sayisal("İK md. 40",
    "Bir işyerinde sel nedeniyle işler durmuş ve işçiler zorlayıcı sebeple çalıştırılamamıştır."
    f"\n\n{K}, bu bekleme süresi içinde işçilere en çok kaç gün süreyle her gün için yarım ücret ödenir?",
    "7", ["3", "5", "10", "15"],
    "Md. 40'a göre md. 24 ve 25'in (III) numaralı bentlerinde gösterilen zorlayıcı sebepler dolayısıyla çalışamayan veya "
    "çalıştırılmayan işçiye bekleme süresi içinde bir haftaya kadar her gün için yarım ücret ödenir.")

P.q("İK md. 11",
    f"{K}, aşağıdakilerden hangisi belirli süreli iş sözleşmesi yapılmasını haklı kılan objektif koşullardan biri değildir?",
    "İşverenin gerekçesiz tercihi",
    ["Belli bir işin tamamlanması",
     "Belirli bir olgunun ortaya çıkması",
     "İşin belirli süreli bir iş olması",
     "İzindeki işçinin yerine geçici çalıştırma"],
    "Md. 11'e göre belirli süreli iş sözleşmesi belirli süreli işlerde veya belli bir işin tamamlanması ya da belirli bir "
    "olgunun ortaya çıkması gibi objektif koşullara bağlı olarak yapılır; işverenin gerekçesiz tercihi yeterli değildir.")

P.sayisal("İK md. 36",
    "Bir belediyeden yol yapım işi alan müteahhit, işçilerinin ücretlerini ödememiştir; işçiler belediyeye başvurmuştur."
    f"\n\n{K}, belediyenin sorumluluğu her hakediş dönemi için ücret alacaklarının en fazla kaç aylık tutarıyla sınırlıdır?",
    "3", ["1", "2", "6", "12"],
    "Md. 36'ya göre kamu idareleri müteahhidin ödemediği ücretleri hakedişinden öder; her hakediş dönemi için ücret "
    "alacaklarının üç aylık tutarından fazlası hakkında idareye sorumluluk düşmez.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
