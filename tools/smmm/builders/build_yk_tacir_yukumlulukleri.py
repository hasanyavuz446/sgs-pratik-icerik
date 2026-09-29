# -*- coding: utf-8 -*-
"""Hukuk · Ticaret Hukuku · Tacir Olmanın Hükümleri, Ticaret Unvanı ve Haksız Rekabet — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında bu konular "6102 sayılı Türk Ticaret Kanunu’na göre …" kalıbıyla; haksız rekabette
"dürüstlük kuralına aykırı davranış ile ticari uygulamalardan biri değildir" gibi olumsuz köklerle sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6102 sayılı TTK md. 18-23, 39-63. Yıllık yeniden
değerlemeye tabi idari para cezası tutarları soru konusu yapılmamıştır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_tacir_yukumluluklari_2026.json", lesson="ticaret_hukuku", topic="tacir_yukumluluklari",
          konu_adi="Tacirin Yükümlülükleri", seed=2026093011, surum="6102 sayılı TTK güncel metni; 29.09.2026 kontrolü")

K = "6102 sayılı Türk Ticaret Kanunu’na göre"

P.sayisal("TTK md. 21",
    "Tacir (A), ticari işletmesi için aldığı mallara ilişkin faturayı 3 Mart’ta almıştır."
    f"\n\n{K}, (A) faturanın içeriğine aldığı tarihten itibaren kaç gün içinde itiraz etmezse içeriği kabul etmiş sayılır?",
    "8", ["3", "7", "10", "15"],
    "Md. 21/2'ye göre fatura alan kişi aldığı tarihten itibaren sekiz gün içinde faturanın içeriğine itiraz etmemişse bu "
    "içeriği kabul etmiş sayılır.", zorluk="easy")

P.q("TTK md. 18",
    f"{K}, tacir olmanın hükümleri arasında aşağıdakilerden hangisi yer almaz?",
    "Adi borçları için iflasa tabi olmamak",
    ["Kanuna uygun ticaret unvanı seçmek",
     "İşletmesini ticaret siciline tescil ettirmek",
     "Gerekli ticari defterleri tutmak",
     "Basiretli bir iş adamı gibi hareket etmek"],
    "Md. 18'e göre tacir her türlü borcu için iflasa tabidir; ayrıca unvan seçmek, sicile tescil ettirmek, ticari defter "
    "tutmak ve basiretli iş adamı gibi hareket etmekle yükümlüdür.", zorluk="easy")

P.q("TTK md. 18",
    f"{K}, tacirler arasında temerrüde düşürme, fesih veya dönme ihbarlarının yapılma şekilleri arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Adi posta ile gönderilen mektup",
    ["Noter aracılığıyla ihbar",
     "Taahhütlü mektup",
     "Telgraf",
     "Güvenli e-imzalı kayıtlı elektronik posta"],
    "Md. 18/3'e göre bu ihbar ve ihtarlar noter aracılığıyla, taahhütlü mektupla, telgrafla veya güvenli elektronik imzalı "
    "kayıtlı elektronik posta ile yapılır.")

P.sayisal("TTK md. 21",
    f"{K}, telefonla kurulan bir sözleşmenin içeriğini doğrulayan teyit mektubunu alan kişi, aldığı tarihten itibaren kaç "
    "gün içinde itiraz etmezse mektubun sözleşmeye uygun olduğunu kabul etmiş sayılır?",
    "8", ["2", "5", "10", "30"],
    "Md. 21/3'e göre teyit mektubunu alan kişi aldığı tarihten itibaren sekiz gün içinde itirazda bulunmamışsa mektubun "
    "sözleşmeye uygun olduğunu kabul etmiş sayılır.")

P.q("TTK md. 18",
    f"{K}, tacirin ticaretine ait faaliyetlerinde uyması gereken özen ölçüsü aşağıdakilerden hangisidir?",
    "Basiretli bir iş adamı gibi hareket etmek",
    ["Olağan bir kişi gibi hareket etmek",
     "Kendi işlerindeki özeni göstermek",
     "Sadece kasten zarar vermemek",
     "Ağır kusurdan kaçınmak"],
    "Md. 18/2'ye göre her tacirin ticaretine ait bütün faaliyetlerinde basiretli bir iş adamı gibi hareket etmesi gerekir.",
    zorluk="easy")

P.q("TTK md. 19",
    f"{K}, ticari iş karinesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tüzel kişi tacir de borcu adi saydırabilir.",
    ["Tacirin borçlarının ticari olması asıldır.",
     "Gerçek kişi tacir, işlem anında adi olduğunu bildirebilir.",
     "Durum elverişli değilse borç adi sayılır.",
     "Bir taraf için ticari olan iş diğeri için de ticaridir."],
    "Md. 19/1'e göre işlemin ticari işletmesiyle ilgili olmadığını diğer tarafa açıkça bildirerek borcu adi saydırma imkânı "
    "gerçek kişi tacire tanınmıştır.", zorluk="hard")

P.sayisal("TTK md. 23",
    "Tacirler arasındaki satışta teslim edilen malın ayıbı teslim sırasında açıkça belli olmaktadır."
    f"\n\n{K}, alıcı durumu satıcıya kaç gün içinde ihbar etmelidir?",
    "2", ["1", "3", "5", "8"],
    "Md. 23/1-c'ye göre malın ayıbı teslim sırasında açıkça belli ise alıcı iki gün içinde durumu satıcıya ihbar etmelidir.",
    zorluk="hard")

P.q("TTK md. 19",
    "Tacir (B), kendisi için ticari iş niteliğinde olan bir satışı tacir olmayan (C) ile yapmıştır; Kanunda aksine hüküm "
    f"yoktur.\n\n{K}, bu sözleşme (C) için nasıl nitelendirilir?",
    "Ticari iş sayılır.",
    ["Adi iş sayılır.", "Tüketici işlemi sayılır, TTK uygulanmaz.", "Kesin hükümsüzdür.", "Karma iş sayılır."],
    "Md. 19/2'ye göre taraflardan yalnız biri için ticari iş niteliğinde olan sözleşmeler, Kanunda aksine hüküm bulunmadıkça "
    "diğeri için de ticari iş sayılır.")

P.q("TTK md. 20",
    f"{K}, tacirin ücret isteme hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Uygun ücret isteyebilir; avans için faize hak kazanır.",
    ["Sadece tacirlere yaptığı işler için ücret isteyebilir.",
     "Ücret için önceden yazılı sözleşme şarttır.",
     "Verdiği avanslar için faiz isteyemez.",
     "Bu hak esnafa tanınmaz."],
    "Md. 20'ye göre tacir olan veya olmayan bir kişiye ticari işletmesiyle ilgili iş veya hizmet gören tacir uygun ücret "
    "isteyebilir; verdiği avanslar ve yaptığı giderler için ödeme tarihinden itibaren faize hak kazanır.")

P.sayisal("TTK md. 23",
    "Tacirler arasındaki satışta malın ayıbı teslim sırasında açıkça belli değildir."
    f"\n\n{K}, alıcı malı teslim aldıktan sonra kaç gün içinde incelemek veya incelettirmek ve ayıbı ihbar etmekle "
    "yükümlüdür?",
    "8", ["2", "3", "15", "30"],
    "Md. 23/1-c'ye göre ayıp açıkça belli değilse alıcı malı teslim aldıktan sonra sekiz gün içinde inceler veya inceletir ve "
    "ayıplı çıkarsa bu süre içinde satıcıya ihbar eder.", zorluk="hard")

P.q("TTK md. 21",
    f"{K}, faturaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fatura isteme hakkı sadece tacir alıcıya aittir.",
    ["Diğer taraf fatura verilmesini isteyebilir.",
     "Bedel ödenmişse faturada gösterilmesi istenebilir.",
     "Sekiz gün içinde itiraz edilmezse içerik kabul edilmiş sayılır.",
     "Fatura, işletme bağlamındaki satış için verilir."],
    "Md. 21/1'e göre ticari işletmesi bağlamında mal satan veya iş gören tacirden diğer taraf, tacir olsun olmasın, fatura "
    "verilmesini isteyebilir.")

P.q("TTK md. 22",
    f"{K}, tacir sıfatını haiz borçlunun kararlaştırılan sözleşme cezasının aşırı olduğunu ileri sürmesine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Mahkemeden indirim isteyemez.",
    ["Mahkemeden indirim isteyebilir.",
     "Ceza doğrudan yarıya iner.",
     "Ceza hükümsüz sayılır.",
     "İndirim ancak alacaklının rızasıyla istenir."],
    "Md. 22'ye göre tacir sıfatını haiz borçlu, TBK'daki ilgili hâllerde aşırı ücret veya ceza kararlaştırıldığı iddiasıyla "
    "ücret veya sözleşme cezasının indirilmesini mahkemeden isteyemez.")

P.sayisal("TTK md. 60",
    f"{K}, haksız rekabete ilişkin hukuk davaları, hak sahibinin haklarının doğumunu öğrendiği günden itibaren kaç yıl "
    "geçmekle zamanaşımına uğrar?",
    "1", ["2", "3", "5", "10"],
    "Md. 60'a göre md. 56'daki davalar öğrenmeden itibaren bir yıl ve her hâlde doğumdan itibaren üç yıl geçmekle zamanaşımına "
    "uğrar; fiil daha uzun ceza zamanaşımına tabi suçsa o süre uygulanır.")

P.q("TTK md. 23",
    f"{K}, tacirler arasında kısım kısım ifası mümkün satışta bir kısmın teslim edilmemesi hâlinde aşağıdakilerden "
    "hangisi doğrudur?",
    "Sadece o kısım için hak kullanılır.",
    ["Alıcı tüm sözleşmeyi feshedebilir.",
     "Satıcı tüm bedeli isteyemez ve sözleşme düşer.",
     "Alıcı teslim edilen kısmı da iade etmelidir.",
     "Sözleşme doğrudan sona erer."],
    "Md. 23/1-a'ya göre kısmi ifa mümkünse alıcı haklarını sadece teslim edilmeyen kısım hakkında kullanabilir; ancak amaç "
    "ortadan kalkıyorsa sözleşmeyi feshedebilir.", zorluk="hard")

P.q("TTK md. 23",
    f"{K}, tacirler arasındaki satışta alıcının temerrüdü hâlinde satıcının hakkına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Mahkemeden satış izni isteyebilir.",
    ["Malı dilediği fiyata doğrudan satabilir.",
     "Malı imha edebilir.",
     "Malı kendi malı gibi kullanabilir.",
     "Bir işlem yapamaz."],
    "Md. 23/1-b'ye göre alıcı mütemerrit olursa satıcı malın satışına izin verilmesini mahkemeden isteyebilir; mahkeme açık "
    "artırmayla veya yetkilendirilen kişi aracılığıyla satışa karar verir.")

P.sayisal("TTK md. 60",
    f"{K}, haksız rekabete ilişkin hukuk davaları, her hâlde hakların doğumundan itibaren kaç yıl geçmekle zamanaşımına "
    "uğrar?",
    "3", ["1", "2", "5", "10"],
    "Md. 60'a göre haksız rekabet davaları her hâlde hakların doğumundan itibaren üç yıl geçmekle zamanaşımına uğrar.")

P.q("TTK md. 39",
    f"{K}, ticaret unvanını kullanma zorunluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Belgeler başka adla da imzalanabilir.",
    ["İşletme işlemleri ticaret unvanıyla yapılır.",
     "Unvan işletmenin görülebilir yerine yazılır.",
     "Ticari mektuplarda sicil numarası gösterilir.",
     "Ticari mektuplarda işletme merkezi gösterilir."],
    "Md. 39/1'e göre her tacir ticari işletmesine ilişkin işlemleri ticaret unvanıyla yapmak ve senet ve belgeleri bu unvan "
    "altında imzalamak zorundadır.")

P.q("TTK md. 41",
    f"{K}, gerçek kişi tacirin ticaret unvanı nasıl oluşur?",
    "Tam ad ve soyadından",
    ["Sadece soyadından",
     "Ad ve soyadının baş harflerinden",
     "Dilediği gibi seçilen bir addan",
     "İşletme konusunu gösteren bir addan"],
    "Md. 41'e göre gerçek kişi tacirin ticaret unvanı, md. 46'ya uygun ekler ile kısaltılmadan yazılacak adı ve soyadından "
    "oluşur.", zorluk="easy")

P.sayisal("TTK md. 61",
    "Haksız rekabet konusu mallara ithalat sırasında gümrük idaresince ihtiyati tedbir niteliğinde el konulmuştur."
    f"\n\n{K}, kararın tebliğinden itibaren kaç gün içinde esas hakkında dava açılmaz veya mahkemeden tedbir kararı "
    "alınmazsa el koyma kararı ortadan kalkar?",
    "10", ["3", "7", "15", "30"],
    "Md. 61/4'e göre gümrük idaresinin el koyma kararının tebliğinden itibaren on gün içinde dava açılmaz veya mahkemeden "
    "tedbir kararı alınmazsa idarenin el koyma kararı ortadan kalkar.", zorluk="hard")

P.q("TTK md. 42",
    f"{K}, kollektif şirketin ticaret unvanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "En az bir ortağın ad ve soyadını içerir.",
    ["Ortakların adlarını içeremez.",
     "Sadece işletme konusunu gösterir.",
     "Unvanda şirket türü belirtilmez.",
     "Tüm ortakların adlarını içermesi şarttır."],
    "Md. 42/1'e göre kollektif şirketin ticaret unvanı bütün ortakların veya en az birinin adı ve soyadıyla şirketi ve türünü "
    "gösteren bir ibareyi içerir.")

P.q("TTK md. 42",
    f"{K}, komandit şirketin ticaret unvanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Unvanda komanditer ortağın adı bulunabilir.",
    ["En az bir komandite ortağın adı unvanda yer alır.",
     "Unvan şirketin türünü gösterir.",
     "Paylı komandit şirkete de aynı kural uygulanır.",
     "Komandite ortağın soyadı unvanda yer alır."],
    "Md. 42/2'ye göre komandit şirketlerin ticaret unvanlarında komanditer ortakların adları ve soyadları veya ticaret "
    "unvanları bulunamaz.")

P.sayisal("TTK md. 62",
    f"{K}, md. 55’te yazılı haksız rekabet fiillerinden birini kasten işleyenler, şikâyet üzerine kaç yıla kadar hapis "
    "veya adli para cezasıyla cezalandırılır?",
    "2", ["1", "3", "5", "7"],
    "Md. 62'ye göre haksız rekabet fiillerini kasten işleyenler, dava açma hakkı olanlardan birinin şikâyeti üzerine iki yıla "
    "kadar hapis veya adli para cezasıyla cezalandırılır.")

P.q("TTK md. 43",
    f"{K}, anonim, limited ve kooperatif şirketlerin ticaret unvanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Konu gösterilerek unvan seçilebilir.",
    ["Unvanda ortağın adı bulunması şarttır.",
     "Şirket türü unvanda gösterilmez.",
     "Gerçek kişi adı varsa tür kısaltılabilir.",
     "Unvanı Ticaret Bakanlığı belirler."],
    "Md. 43'e göre bu şirketler işletme konusu gösterilmek ve md. 46 saklı kalmak şartıyla ticaret unvanlarını seçebilir; "
    "unvanda şirket türü bulunur ve gerçek kişi adı varsa tür ibaresi kısaltılamaz.")

P.q("TTK md. 43",
    f"{K}, ticaret unvanında gerçek bir kişinin adı bulunan limited şirkete ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tür ibaresi kısaltılamaz.",
    ["“Ltd. Şti.” kısaltması şarttır.",
     "Tür ibaresi yazılmaz.",
     "Kişinin adı kısaltılarak yazılır.",
     "Unvan Bakanlık izniyle seçilir."],
    "Md. 43/2'ye göre ticaret unvanında gerçek bir kişinin adı veya soyadı yer alırsa şirket türünü gösteren ibareler baş "
    "harflerle veya başka şekilde kısaltılarak yazılamaz.", zorluk="hard")

P.q("TTK md. 44",
    f"{K}, ticari işletmesi olan dernek ve vakıfların ticaret unvanı aşağıdakilerden hangisidir?",
    "Kendi adları",
    ["Kurucularının adları", "Yöneticilerinin adları", "İşletme konuları", "Bakanlıkça verilen ad"],
    "Md. 44/1'e göre ticari işletmeye sahip dernek, vakıf ve diğer tüzel kişilerin ticaret unvanları adlarıdır.")

P.q("TTK md. 46",
    f"{K}, ticaret unvanına yapılacak eklere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tek tacir “ve Ortakları” ekini kullanabilir.",
    ["Ekler gerçeğe aykırı olamaz.",
     "Hayalî adlardan oluşan ekler yapılabilir.",
     "“Türk” kelimesi ancak Cumhurbaşkanı kararıyla konabilir.",
     "Ekler üçüncü kişileri yanıltamaz."],
    "Md. 46/2'ye göre tek başına ticaret yapan gerçek kişiler ticaret unvanlarına bir şirketin var olduğu izlenimini "
    "uyandıracak ekler yapamaz.")

P.q("TTK md. 46",
    f"{K}, aşağıdaki kelimelerden hangisi bir ticaret unvanına ancak Cumhurbaşkanı kararıyla konabilir?",
    "Cumhuriyet",
    ["Anadolu", "Uluslararası", "Holding", "Global"],
    "Md. 46/3'e göre “Türk”, “Türkiye”, “Cumhuriyet” ve “Millî” kelimeleri bir ticaret unvanına ancak Cumhurbaşkanı kararıyla "
    "konabilir.")

P.q("TTK md. 48",
    f"{K}, şubelerin ticaret unvanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Merkezin unvanı şube ibaresiyle",
    ["Şube tamamen ayrı bir unvan seçer.",
     "Şube unvan kullanamaz.",
     "Şube unvanında merkez gösterilmez.",
     "Şube unvanı Bakanlıkça verilir."],
    "Md. 48/1'e göre her şube, kendi merkezinin ticaret unvanını şube olduğunu belirterek kullanmak zorundadır; unvana şube ile "
    "ilgili ekler yapılabilir.")

P.q("TTK md. 48",
    f"{K}, merkezi yabancı ülkede bulunan işletmenin Türkiye’deki şubesinin ticaret unvanında aşağıdakilerden hangisinin "
    "gösterilmesi şart değildir?",
    "Şube müdürünün adı",
    ["Merkezin bulunduğu yer", "Şubenin bulunduğu yer", "Şube olduğu", "Merkezin ticaret unvanı"],
    "Md. 48/3'e göre merkezi yabancı ülkede bulunan işletmenin Türkiye'deki şubesinin unvanında merkezin ve şubenin bulunduğu "
    "yerlerin ve şube olduğunun gösterilmesi şarttır.", zorluk="hard")

P.q("TTK md. 49",
    f"{K}, ticaret unvanının devrine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ticaret unvanı işletmeden ayrı olarak devredilebilir.",
    ["İşletmenin devri kural olarak unvanın devrini de kapsar.",
     "Devralan unvanı aynen kullanabilir.",
     "Taraflar unvanın devredilmediğini kararlaştırabilir.",
     "Unvanın ayrı devri idari para cezasını gerektirir."],
    "Md. 49/1'e göre ticaret unvanı işletmeden ayrı olarak başkasına devredilemez.")

P.q("TTK md. 50",
    f"{K}, usulen tescil ve ilan edilmiş ticaret unvanını kullanma hakkı kime aittir?",
    "Sadece unvan sahibine",
    ["Aynı sektördeki tüm tacirlere", "Ticaret odasına", "Unvanı ilk kullanan herkese", "Sicil müdürlüğüne"],
    "Md. 50'ye göre usulen tescil ve ilan edilmiş ticaret unvanını kullanma hakkı sadece sahibine aittir.", zorluk="easy")

P.q("TTK md. 52",
    f"{K}, ticaret unvanının ticari dürüstlüğe aykırı biçimde başkası tarafından kullanılması hâlinde hak sahibinin "
    "açabileceği davalar arasında aşağıdakilerden hangisi yer almaz?",
    "Unvanın kendisine devri",
    ["Kullanımın tespiti",
     "Kullanımın yasaklanması",
     "Tescilli unvanın silinmesi",
     "Maddi ve manevi tazminat"],
    "Md. 52'ye göre hak sahibi tespit, yasaklama, tescilli unvanın değiştirilmesi veya silinmesi, maddi durumun ortadan "
    "kaldırılması ve tazminat isteyebilir; unvanın kendisine devri bu davalar arasında sayılmamıştır.")

P.q("TTK md. 53",
    f"{K}, işletme adına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tescil ettirilmesi gerekir.",
    ["Tescil edilmesi yasaktır.",
     "Sadece anonim şirketler kullanabilir.",
     "Unvan korumasından yararlanamaz.",
     "İşletme sahibini tanıtmak için kullanılır."],
    "Md. 53'e göre doğrudan işletmeyi tanıtmak ve benzerlerinden ayırt etmek için kullanılan işletme adlarının da sahiplerince "
    "tescil ettirilmesi gerekir; tescilli işletme adları unvan korumasına ilişkin hükümlerden yararlanır.")

P.q("TTK md. 51",
    f"{K}, bir ticaret unvanının kanuna aykırı kullanıldığını görevleri sırasında öğrenince durumu yetkili makamlara "
    "bildirmekle yükümlü olanlar arasında aşağıdakilerden hangisi yer almaz?",
    "Özel sektör çalışanları",
    ["Mahkemeler", "Noterler", "Ticaret ve sanayi odaları", "Memurlar"],
    "Md. 51/1'e göre bütün mahkemeler, memurlar, ticaret ve sanayi odaları, noterler ve Türk Patent Enstitüsü bu durumu "
    "yetkili makamlara bildirmek zorundadır.")

P.q("TTK md. 54",
    f"{K}, haksız rekabete ilişkin hükümlerin amacı aşağıdakilerden hangisidir?",
    "Dürüst ve bozulmamış rekabetin sağlanması",
    ["Sadece rakiplerin korunması",
     "Fiyatların Devletçe belirlenmesi",
     "Tekel oluşumunun teşviki",
     "Vergi gelirlerinin artırılması"],
    "Md. 54/1'e göre haksız rekabet hükümlerinin amacı bütün katılanların menfaatine dürüst ve bozulmamış rekabetin "
    "sağlanmasıdır.", zorluk="easy")

P.q("TTK md. 55",
    f"{K}, aşağıdakilerden hangisi dürüstlük kuralına aykırı reklam ve satış yöntemlerinden biri değildir?",
    "Malın gerçek özelliklerini doğru biçimde tanıtmak",
    ["Rakibin mallarını yanıltıcı açıklamalarla kötülemek",
     "Almadığı ödülü almış gibi davranmak",
     "Saldırgan satış yöntemleri kullanmak",
     "Başkasının mallarıyla karıştırılmaya yol açmak"],
    "Md. 55/1-a'ya göre kötüleme, gerçek dışı ödül iddiası, saldırgan satış yöntemleri ve karıştırılmaya yol açma haksız "
    "rekabettir; malın özelliklerini doğru tanıtmak dürüstlüğe aykırı değildir.", zorluk="easy")

P.q("TTK md. 55",
    f"{K}, aşağıdakilerden hangisi sözleşmeyi ihlale veya sona erdirmeye yöneltme suretiyle yapılan haksız rekabet "
    "hâllerinden biridir?",
    "İşçileri iş sırlarını ifşa etmeye yöneltmek",
    ["Emanet edilen planlardan yetkisiz yararlanmak",
     "Genel işlem şartlarını dürüstlüğe aykırı kullanmak",
     "Meslek dalındaki iş şartlarına uymamak",
     "Taksitli satış ilanında unvanı belirtmemek"],
    "Md. 55/1-b'ye göre işçileri, vekilleri veya yardımcı kişileri işverenlerinin üretim ve iş sırlarını ifşa etmeye veya ele "
    "geçirmeye yöneltmek, sözleşmeyi ihlale yöneltme suretiyle haksız rekabettir.", zorluk="hard")

P.q("TTK md. 55",
    f"{K}, bazı malları birden çok kez tedarik fiyatının altında satışa sunup bunu reklamlarda vurgulamaya ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Yanıltıyorsa haksız rekabettir.",
    ["Serbest bir fiyat politikasıdır.",
     "Sadece vergi kaçakçılığı sayılır.",
     "Sadece tüketici mahkemesinde incelenir.",
     "Tedarik fiyatı karine oluşturmaz."],
    "Md. 55/1-a-6'ya göre seçilmiş malları birden çok kez tedarik fiyatının altında sunup reklamda vurgulayarak müşteriyi "
    "yanıltmak haksız rekabettir; satış fiyatı benzer hacimdeki tedarik fiyatının altındaysa yanıltma karine olarak kabul "
    "edilir.", zorluk="hard")

P.q("TTK md. 55",
    f"{K}, başkalarının iş ürünlerinden yetkisiz yararlanma hâllerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kendi katkılı ürünü kullanmak haksız rekabettir.",
    ["Emanet edilen teklif veya plandan yetkisiz yararlanmak",
     "Yetkisiz sağlandığını bilmesi gereken plandan yararlanmak",
     "Katkısı olmadan pazarlanmaya hazır ürünü çoğaltmak",
     "Başkasına ait hesap çalışmasından yetkisiz yararlanmak"],
    "Md. 55/1-c'ye göre yetkisiz yararlanma; emanet edilen veya yetkisiz sağlanan iş ürünlerinden yararlanmak ile kendi uygun "
    "katkısı olmaksızın başkasının hazır ürününü teknik yöntemlerle çoğaltmaktır.")

P.q("TTK md. 56",
    f"{K}, haksız rekabet nedeniyle ekonomik çıkarları zarar gören müşterilerin açabileceği davalara ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "İmha talep edemezler.",
    ["Bu tür dava açamazlar.",
     "Sadece manevi tazminat isteyebilirler.",
     "Sadece ceza davası açabilirler.",
     "Sadece tespit davası açabilirler."],
    "Md. 56/2'ye göre ekonomik çıkarları zarar gören müşteriler de md. 56/1'deki davaları açabilir; ancak araçların ve "
    "malların imhasını isteyemezler.", zorluk="hard")

P.q("TTK md. 56",
    f"{K}, haksız rekabet nedeniyle açılabilecek davalar arasında aşağıdakilerden hangisi yer almaz?",
    "Rakibin ticaret sicilinden silinmesi",
    ["Fiilin haksız olup olmadığının tespiti",
     "Haksız rekabetin men’i",
     "Maddi durumun ortadan kaldırılması",
     "Kusur varsa zararın tazmini"],
    "Md. 56/1'e göre tespit, men, maddi durumun ortadan kaldırılması, yanlış beyanların düzeltilmesi, zararın tazmini ve "
    "manevi tazminat istenebilir; rakibin sicilden silinmesi sayılmamıştır.")

P.q("TTK md. 57",
    "Bir şirketin satış elemanı, görevi sırasında rakip firmanın ürünlerini yanıltıcı açıklamalarla kötülemiştir."
    f"\n\n{K}, rakip firma md. 56’daki tespit, men ve maddi durumun ortadan kaldırılması davalarını kime karşı açabilir?",
    "Çalışana ve çalıştırana",
    ["Sadece çalışana", "Sadece ticaret odasına", "Sadece Rekabet Kurumuna", "Kimseye"],
    "Md. 57/1'e göre haksız rekabet fiili çalışanlar tarafından işlerini gördükleri sırada işlenirse md. 56/1-a, b ve c "
    "davaları çalıştıranlara karşı da açılabilir.")

P.q("TTK md. 61",
    f"{K}, haksız rekabette ihtiyati tedbirlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "HMK tedbir hükümlerine göre karar verilir.",
    ["İhtiyati tedbir kararı verilemez.",
     "Tedbir kararını sadece ticaret odası verir.",
     "Tedbir için ceza mahkümiyeti şarttır.",
     "Tedbir kararı idare mahkemesince verilir."],
    "Md. 61/1'e göre dava açma hakkı olanın talebi üzerine mahkeme HMK'nın ihtiyati tedbir hükümlerine göre mevcut durumun "
    "korunmasına ve haksız rekabetin önlenmesine karar verebilir.")

P.q("TTK md. 62",
    f"{K}, cezayı gerektiren haksız rekabet fiillerinin kovuşturulmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hak sahibinin şikâyeti gerekir.",
    ["Kovuşturma resen yapılır.",
     "Sadece Ticaret Bakanlığı şikâyet edebilir.",
     "Kovuşturma için idari izin gerekir.",
     "Bu fiiller suç oluşturmaz."],
    "Md. 62'ye göre cezayı gerektiren haksız rekabet fiilleri md. 56'ya göre hukuk davası açma hakkını haiz olanlardan "
    "birinin şikâyeti üzerine cezalandırılır.")

P.q("TTK md. 63",
    f"{K}, tüzel kişilerin işleri görülürken haksız rekabet fiili işlenmesi hâlinde ceza hükmü kimler hakkında uygulanır?",
    "Organ üyeleri ve ortaklar",
    ["Sadece tüzel kişinin kendisi",
     "Tüzel kişinin tüm çalışanları",
     "Tüzel kişinin alacaklıları",
     "Tüzel kişinin müşterileri"],
    "Md. 63'e göre tüzel kişilerin işlerini görmeleri sırasında haksız rekabet fiili işlenirse md. 62, tüzel kişi adına hareket "
    "eden veya etmesi gereken organ üyeleri veya ortaklar hakkında uygulanır.")

P.oncul("TTK md. 55",
    f"{K} aşağıdaki davranışlar değerlendirilmektedir:",
    ["Rakibin iş sırlarını hukuka aykırı ele geçirip kullanmak",
     "Rakibinden daha düşük fiyatla dürüstçe rekabet etmek",
     "Genel işlem şartlarında diğer taraf aleyhine yanıltıcı düzenleme yapmak",
     "Ürününü doğru bilgilerle tanıtan reklam vermek"],
    "Yukarıdakilerden hangileri haksız rekabet hâlidir?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 55'e göre iş sırlarını hukuka aykırı ifşa veya kullanma (I) ve dürüstlüğe aykırı genel işlem şartları (III) haksız "
    "rekabettir; dürüst fiyat rekabeti (II) ve doğru bilgili reklam (IV) haksız rekabet değildir.", zorluk="hard")

P.q("TTK md. 20",
    f"{K}, tacirin ticari işletmesiyle ilgili verdiği avans ve yaptığı giderler için faize hak kazanma zamanı "
    "aşağıdakilerden hangisidir?",
    "Ödeme tarihinden itibaren",
    ["Dava tarihinden itibaren", "İhtar tarihinden itibaren", "Takvim yılı sonundan itibaren",
     "İşin bitim tarihinden itibaren"],
    "Md. 20'ye göre tacir verdiği avanslar ve yaptığı giderler için ödeme tarihinden itibaren faize hak kazanır.")

P.q("TTK md. 45",
    f"{K}, ticaret unvanına ayırt edici ek yapılması hangi durumda gereklidir?",
    "Daha önce tescilli bir unvandan ayırt etmek için",
    ["Unvan Türkçe değilse",
     "İşletme iki yıldan eskiyse",
     "Tacir iki ayrı işletmeye sahipse",
     "Tacir yabancı uyrukluysa"],
    "Md. 45'e göre bir ticaret unvanına, Türkiye'nin herhangi bir sicil dairesinde daha önce tescil edilmiş diğer bir unvandan "
    "ayırt edilmesi için gerekli olduğu takdirde ek yapılır.")

P.q("TTK md. 40",
    f"{K}, merkezi Türkiye’de bulunan ticari işletmelerin şubelerinin tescili hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Bulundukları yerin ticaret siciline tescil edilir.",
    ["Sadece merkezin siciline kaydedilir.",
     "Şubeler tescil edilmez.",
     "Ticaret Bakanlığına tescil edilir.",
     "Şubeler vergi dairesine tescil edilir."],
    "Md. 40/3'e göre merkezi Türkiye'de bulunan ticari işletmelerin şubeleri de bulundukları yerin ticaret siciline tescil ve "
    "ilan olunur.")

P.q("TTK md. 18",
    f"{K}, tacirin iflasa tabi olmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Adi borçları için de iflasa tabidir.",
    ["Sadece ticari borçları için iflasa tabidir.",
     "İflasa tabi değildir.",
     "Sadece vergi borçları için iflasa tabidir.",
     "Ancak tescilden sonra iflasa tabidir."],
    "Md. 18/1'e göre tacir her türlü borcu için iflasa tabidir; borcun ticari veya adi olması bu sonucu değiştirmez.")

P.q("TTK md. 21",
    f"{K}, teyit mektubuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sadece noter aracılığıyla gönderilir.",
    ["Sözlü sözleşmenin içeriğini doğrular.",
     "Telefonla kurulan sözleşmeler için gönderilebilir.",
     "Sekiz gün içinde itiraz edilebilir.",
     "İtiraz edilmezse içerik kabul edilmiş sayılır."],
    "Md. 21/3'e göre teyit mektubu telefon, telgraf, bilişim aracı veya sözlü kurulan sözleşmelerdeki açıklamaların içeriğini "
    "doğrulayan bir yazıdır; noter aracılığıyla gönderilmesi şartı yoktur.")

P.q("TTK md. 39",
    f"{K}, tacirin ticari mektuplarında ve kayıtların dayandığı belgelerde gösterilmesi gerekenler arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Tacirin yıllık cirosu",
    ["Sicil numarası", "Ticaret unvanı", "İşletmenin merkezi", "Tescilli internet sitesi adresi"],
    "Md. 39/2'ye göre ticari mektuplarda ve kayıtların dayandığı belgelerde sicil numarası, ticaret unvanı, işletme merkezi ve "
    "yükümlüyse tescilli internet sitesi adresi gösterilir.")

P.q("TTK md. 44",
    f"{K}, donatma iştirakinin ticaret unvanı aşağıdakilerden hangisini içerir?",
    "Bir donatanın adı veya gemi adı",
    ["Sadece geminin bayrağı",
     "Kaptanın adı ve soyadı",
     "Liman başkanlığının adı",
     "Tüm donatanların adları ve gemi adı"],
    "Md. 44/2'ye göre donatma iştirakinin ticaret unvanı ortak donatanlardan en az birinin adı ve soyadını veya geminin adını "
    "ve donatma iştirakini gösteren bir ibareyi içerir.", zorluk="hard")

P.q("TTK md. 56",
    f"{K}, ticaret ve sanayi odaları ile tüketicileri koruyan sivil toplum kuruluşlarının haksız rekabete karşı "
    "açabileceği davalar aşağıdakilerden hangisidir?",
    "Tespit, men ve ortadan kaldırma davaları",
    ["Sadece tazminat davası",
     "Sadece ceza şikâyeti",
     "Sadece imha davası",
     "Manevi tazminat ve ceza davaları"],
    "Md. 56/3'e göre odalar, borsalar, meslek birlikleri ve tüketicileri koruyan kuruluşlar md. 56/1'in (a), (b) ve (c) "
    "bentlerindeki tespit, men ve maddi durumun ortadan kaldırılması davalarını açabilir.", zorluk="hard")

P.q("TTK md. 23",
    f"{K}, md. 23’teki özel hükümler saklı kalmak şartıyla tacirler arasındaki satışlarda hangi hükümler uygulanır?",
    "TBK satış ve mal değişimi hükümleri",
    ["Tüketici Kanunu hükümleri",
     "Sadece ticari örf ve âdet",
     "Kamu İhale Kanunu hükümleri",
     "Ticaret odası tarifeleri ve borsa kuralları"],
    "Md. 23/1'e göre tacirler arasındaki satış ve mal değişimlerinde de TBK'nın satış ve mal değişim sözleşmelerine ilişkin "
    "hükümleri uygulanır.")

P.q("TTK md. 51",
    f"{K}, ticaret unvanına ilişkin md. 39-45 veya md. 48 hükümlerini ihlal edenlere uygulanan yaptırım aşağıdakilerden "
    "hangisidir?",
    "İdari para cezası",
    ["Hapis cezası", "Ticaret yasağı", "Sicilden resen silinme", "Mülki amirce işyeri kapatma"],
    "Md. 51/2'ye göre md. 39-45 veya 48 hükümlerini ihlal edenler idari para cezasıyla cezalandırılır; tutar her yıl yeniden "
    "değerleme oranında güncellenir.")

P.q("TTK md. 57",
    f"{K}, haksız rekabetten doğan maddi ve manevi tazminat davaları hakkında hangi Kanun hükümleri uygulanır?",
    "Türk Borçlar Kanunu",
    ["Türk Ceza Kanunu", "Tüketici Kanunu", "Rekabet Kanunu", "Hukuk Muhakemeleri Kanunu"],
    "Md. 57/2'ye göre md. 56/1'in (d) ve (e) bentlerindeki tazminat davaları hakkında Türk Borçlar Kanunu hükümleri uygulanır.")

P.q("TTK md. 18",
    f"{K}, aşağıdaki bildirimlerden hangisi tacirler arasında md. 18/3’teki şekillerle yapılmalıdır?",
    "Temerrüde düşürme ihtarı",
    ["Genel bilgi yazısı", "Bayram kutlama mesajı", "Katalog gönderimi", "Fiyat listesi güncelleme duyurusu"],
    "Md. 18/3'e göre tacirler arasında temerrüde düşürme, sözleşmeyi fesih ve sözleşmeden dönme ihbar ve ihtarları noter, "
    "taahhütlü mektup, telgraf veya kayıtlı elektronik posta ile yapılır.")

P.q("TTK md. 46",
    f"{K}, aşağıdakilerden hangisi bir ticaret unvanına eklenebilecek eklerden biridir?",
    "Hayalî bir ad",
    ["Yanıltıcı büyüklük ifadesi",
     "Gerçeğe aykırı faaliyet ibaresi",
     "Kamu düzenine aykırı ifade",
     "İzinsiz “Millî” kelimesi"],
    "Md. 46/1'e göre yanıltıcı, gerçeğe ve kamu düzenine aykırı olmamak şartıyla işletmenin özelliklerini belirten, kişilerin "
    "kimliğini gösteren veya hayalî adlardan oluşan ekler yapılabilir.")

P.q("TTK md. 55",
    f"{K}, kanun veya sözleşmeyle rakiplere de yüklenmiş iş şartlarına uymamak hangi haksız rekabet hâlidir?",
    "İş şartlarına uymamak",
    ["Sözleşmeyi ihlale yöneltmek",
     "Yetkisiz yararlanma",
     "Sır ifşası",
     "Karıştırılmaya yol açmak"],
    "Md. 55/1-e'ye göre kanun veya sözleşmeyle rakiplere de yüklenmiş ya da meslek dalında olağan iş şartlarına uymayanlar "
    "dürüstlüğe aykırı davranmış olur.")

if __name__ == "__main__":
    sys.exit(P.yaz())
