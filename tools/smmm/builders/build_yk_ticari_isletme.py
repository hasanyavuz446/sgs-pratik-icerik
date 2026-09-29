# -*- coding: utf-8 -*-
"""Hukuk · Ticaret Hukuku · Ticari İşletme, Tacir ve Ticaret Sicili — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında TTK soruları "6102 sayılı Türk Ticaret Kanunu’na göre …" kalıbıyla; ticari
davalarda görevli mahkeme, tacir sıfatı ve sicil gibi kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6102 sayılı TTK md. 1-17, 24-38. Yıllık yeniden değerlemeye
tabi idari para cezası ve parasal sınırlar soru konusu yapılmamıştır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_ticari_isletme_2026.json", lesson="ticaret_hukuku", topic="ticari_isletme",
          konu_adi="Ticari İşletme", seed=2026093010, surum="6102 sayılı TTK güncel metni; 29.09.2026 kontrolü")

K = "6102 sayılı Türk Ticaret Kanunu’na göre"
K26 = "6102 sayılı Türk Ticaret Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("TTK md. 5/A",
    f"{K}, ticari davalarda dava şartı olarak başvurulan arabulucu, başvuruyu görevlendirildiği tarihten itibaren kaç "
    "hafta içinde sonuçlandırır?",
    "6", ["2", "3", "4", "8"],
    "Md. 5/A'ya göre arabulucu başvuruyu görevlendirildiği tarihten itibaren altı hafta içinde sonuçlandırır; bu süre zorunlu "
    "hâllerde en fazla iki hafta uzatılabilir.")

P.q("TTK md. 1",
    f"{K}, hakkında ticari bir hüküm bulunmayan ticari işlerde mahkeme öncelikle neye göre karar verir?",
    "Ticari örf ve âdete",
    ["Genel hükümlere", "Teamüle", "Doktrine", "Hakkaniyete"],
    "Md. 1/2'ye göre mahkeme hakkında ticari hüküm bulunmayan ticari işlerde ticari örf ve âdete, bu da yoksa genel "
    "hükümlere göre karar verir.", zorluk="easy")

P.q("TTK md. 2",
    f"{K}, ticari örf ve âdete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Genel örf ve âdet, bölgesel olana üstün tutulur.",
    ["Bölgesel örf ve âdet genel olana üstün tutulur.",
     "Teamül, irade açıklamalarının yorumunda dikkate alınır.",
     "Farklı bölgelerde ifa yerindeki örf uygulanır.",
     "Tacir olmayana ancak bilmesi gerekiyorsa uygulanır."],
    "Md. 2/2'ye göre bir bölgeye veya ticaret dalına özgü ticari örf ve âdetler genel olanlara üstün tutulur.")

P.sayisal("TTK md. 5/A",
    f"{K}, ticari davalarda arabuluculuk süresi zorunlu hâllerde arabulucu tarafından en fazla kaç hafta uzatılabilir?",
    "2", ["1", "3", "4", "6"],
    "Md. 5/A'ya göre altı haftalık süre zorunlu hâllerde arabulucu tarafından en fazla iki hafta uzatılabilir.")

P.q("TTK md. 2",
    "Farklı illerde bulunan iki tacir arasındaki sözleşmede uygulanacak ticari örf ve âdet konusunda bir düzenleme yoktur."
    f"\n\n{K}, uyuşmazlıkta hangi yerin ticari örf ve âdeti uygulanır?",
    "İfa yerindeki",
    ["Davacının bulunduğu yerdeki", "Sözleşmenin yapıldığı yerdeki", "Davalının merkezindeki", "Ankara’daki"],
    "Md. 2/2'ye göre ilgililer aynı bölgede değillerse, kanunda veya sözleşmede aksi öngörülmedikçe ifa yerindeki ticari örf "
    "ve âdet uygulanır.")

P.q("TTK md. 3",
    f"{K}, ticari işlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "İşletmeyle ilgili tüm işlem ve fiiller ticaridir.",
    ["Sadece tacirler arasındaki işlemler ticari iştir.",
     "Haksız fiiller ticari iş sayılmaz.",
     "Sadece yazılı sözleşmeler ticari iştir.",
     "Esnafın işlemleri de doğrudan ticari iştir."],
    "Md. 3'e göre TTK'da düzenlenen hususlarla bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller ticari işlerdendir.")

P.sayisal("TTK md. 8",
    f"{K}, bileşik faiz şartı, cari hesaplarla ve her iki taraf için ticari iş niteliğindeki ödünç sözleşmelerinde en az "
    "kaç aylık dönemler için geçerlidir?",
    "3", ["1", "2", "6", "12"],
    "Md. 8/2'ye göre üç aydan aşağı olmamak üzere faizin anaparaya eklenerek tekrar faiz yürütülmesi şartı yalnız cari "
    "hesaplarla her iki taraf bakımından ticari iş niteliğindeki ödünç sözleşmelerinde geçerlidir.", zorluk="hard")

P.q("TTK md. 4",
    f"{K}, tarafların tacir olup olmadığına bakılmaksızın ticari dava sayılan davalar arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "İşletmeyle ilgisiz havaleden doğan dava",
    ["TTK’da öngörülen hususlardan doğan dava",
     "Fikrî mülkiyet mevzuatından doğan dava",
     "Bankalara ilişkin düzenlemelerden doğan dava",
     "TBK’daki komisyon sözleşmesinden doğan dava"],
    "Md. 4/1'e göre herhangi bir ticari işletmeyi ilgilendirmeyen havale, vedia ve fikir ve sanat eserlerine ilişkin haklardan "
    "doğan davalar ticari dava sayılmaz.", zorluk="hard")

P.q("TTK md. 4",
    f"{K}, her iki taraf bakımından ticari işletmeyle ilgili olmasa da ticari dava sayılanlar arasında aşağıdakilerden "
    "hangisi vardır?",
    "TBK saklama sözleşmesinden doğan dava",
    ["TBK’daki kira sözleşmesinden doğan dava",
     "Aile hukukundan doğan dava",
     "Miras paylaşımından doğan dava",
     "Kat mülkiyetinden doğan dava"],
    "Md. 4/1-c'ye göre TBK'nın işletme devri, rekabet yasağı, yayın, kredi mektubu, komisyon, tacir yardımcıları, havale ve "
    "saklama sözleşmelerine ilişkin hükümlerinden doğan davalar tarafların tacir olup olmadığına bakılmaksızın ticari davadır.",
    zorluk="hard")

P.sayisal("TTK md. 30",
    f"{K}, Kanunda aksine hüküm bulunmadıkça ticaret siciline tescili isteme süresi kaç gündür?",
    "15", ["7", "10", "30", "60"],
    "Md. 30'a göre tescili isteme süresi on beş gündür; sicil müdürlüğünün yetki çevresi dışında oturanlar için bir aydır.",
    zorluk="easy")

P.q("TTK md. 5",
    f"{K}, ticari davalara bakmakla görevli mahkemeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Asliye ticaret mahkemesi",
    ["Değeri düşük davalarda sulh hukuk mahkemesi",
     "Kural olarak asliye hukuk mahkemesi",
     "Tacirler arasında tüketici mahkemesi",
     "Deniz ticaretinde idare mahkemesi"],
    "Md. 5/1'e göre aksine hüküm bulunmadıkça dava olunan şeyin değerine veya tutarına bakılmaksızın asliye ticaret "
    "mahkemesi tüm ticari davalara bakmakla görevlidir.", zorluk="easy")

P.q("TTK md. 5/A",
    f"{K}, aşağıdaki ticari davalardan hangisinde dava açılmadan önce arabulucuya başvurulması dava şartı değildir?",
    "Ticaret unvanının silinmesi davası",
    ["Konusu para olan alacak davası",
     "Konusu para olan tazminat davası",
     "Konusu para olan itirazın iptali davası",
     "Konusu para olan menfi tespit davası"],
    "Md. 5/A'ya göre konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat davalarında "
    "arabuluculuk dava şartıdır; ticaret unvanının silinmesi davası konusu para olan bir dava değildir.")

P.sayisal("TTK md. 30",
    f"{K}, ticaret sicili müdürlüğünün yetki çevresi dışında oturanlar için tescili isteme süresi kaç aydır?",
    "1", ["2", "3", "4", "6"],
    "Md. 30/3'e göre sicil müdürlüğünün yetki çevresi dışında oturanlar için tescil isteme süresi bir aydır.")

P.q("TTK md. 6",
    f"{K}, ticari hükümler koyan kanunlardaki zamanaşımı sürelerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aksine düzenleme yoksa değiştirilemez.",
    ["Taraflar sözleşmeyle diledikleri gibi kısaltabilir.",
     "Taraflar sözleşmeyle iki katına çıkarabilir.",
     "Tacirler arasında kural olarak uygulanmaz.",
     "Mahkeme hakkaniyete göre değiştirebilir."],
    "Md. 6'ya göre ticari hükümler koyan kanunlarda öngörülen zamanaşımı süreleri, Kanunda aksine düzenleme yoksa sözleşme "
    "ile değiştirilemez.")

P.q("TTK md. 7",
    "Tacir (A) ile tacir olmayan (B), yalnız (A) için ticari nitelik taşıyan bir iş nedeniyle (C)’ye karşı birlikte borç "
    f"altına girmiştir; sözleşmede aksine hüküm yoktur.\n\n{K}, (A) ve (B)’nin (C)’ye karşı sorumluluğu nasıldır?",
    "Müteselsil sorumluluk",
    ["Kısmi sorumluluk", "Sadece (A) sorumludur.", "Sadece (B) sorumludur.", "Sorumluluk doğmaz."],
    "Md. 7/1'e göre iki veya daha fazla kişi, içlerinden yalnız biri veya hepsi için ticari nitelikte bir iş dolayısıyla "
    "birlikte borç altına girerse, aksi öngörülmemişse müteselsilen sorumlu olurlar.")

P.sayisal("TTK md. 32",
    "Sicil müdürü, kesin olarak tescilinde duraksadığı bir hususu ilgililerin istemi üzerine geçici olarak tescil etmiştir."
    f"\n\n{K}, ilgililer kaç ay içinde mahkemeye başvurduklarını veya anlaştıklarını ispat etmezlerse geçici tescil resen "
    "silinir?",
    "3", ["1", "2", "6", "12"],
    "Md. 32/4'e göre geçici tescilde ilgililer üç ay içinde mahkemeye başvurduklarını veya aralarında anlaştıklarını ispat "
    "etmezlerse geçici tescil resen silinir.", zorluk="hard")

P.q("TTK md. 7",
    f"{K}, ticari borçlara kefalet hâlinde kefillere temerrüt faizi yürütülmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Borcun ödenmediği kefile ihbar edilmelidir.",
    ["Kefile ihbar gerekmez, faiz vadede işler.",
     "Kefile temerrüt faizi yürütülemez.",
     "Faiz ancak mahkeme kararıyla işler.",
     "Kefile ancak noter ihtarı sonrası bir yıl beklenir."],
    "Md. 7/1'e göre kefil ve kefillere, taahhüt veya ödemenin yapılmadığı ihbar edilmeden temerrüt faizi yürütülemez.")

P.q("TTK md. 8",
    f"{K}, ticari işlerde faize ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bileşik faiz şartı tacir olmayanlara da uygulanır.",
    ["Faiz oranı taraflarca belirlenir.",
     "Bileşik faiz cari hesaplarda geçerli olabilir.",
     "Aykırı işletilen bileşik faiz yok hükmündedir.",
     "Tüketicinin korunmasına ilişkin hükümler saklıdır."],
    "Md. 8/2'ye göre bileşik faize ilişkin fıkra sözleşenleri tacir olmayanlara uygulanmaz; buna aykırı işletilen faiz yok "
    "hükmündedir.")

P.sayisal("TTK md. 34",
    f"{K}, ilgililer sicil müdürlüğünün tescil kararlarına karşı tebliğden itibaren kaç gün içinde asliye ticaret "
    "mahkemesine itiraz edebilir?",
    "8", ["3", "7", "15", "30"],
    "Md. 34'e göre sicil müdürlüğünün tescil, değişiklik veya silinme kararlarına karşı tebliğden itibaren sekiz gün içinde "
    "asliye ticaret mahkemesine dilekçeyle itiraz edilebilir.")

P.q("TTK md. 10",
    f"{K}, aksine sözleşme yoksa belli bir vadesi olmayan ticari borcun faizi ne zaman işlemeye başlar?",
    "İhtar gününden itibaren",
    ["Sözleşme tarihinden itibaren", "Dava tarihinden itibaren", "Takvim yılı başından itibaren",
     "Borcun doğduğu aydan itibaren"],
    "Md. 10'a göre aksine sözleşme yoksa ticari bir borcun faizi vadenin bitiminden, belli bir vade yoksa ihtar gününden "
    "itibaren işlemeye başlar.")

P.q("TTK md. 11",
    f"{K}, ticari işletmenin tanımında yer alan unsurlar arasında aşağıdakilerden hangisi bulunmaz?",
    "Ticaret siciline tescil edilmiş olma",
    ["Esnaf sınırını aşan gelir hedefi",
     "Faaliyetin devamlı olması",
     "Faaliyetin bağımsız yürütülmesi",
     "Gelir sağlamayı hedef tutma"],
    "Md. 11/1'e göre ticari işletme esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir sağlamayı hedef tutan "
    "faaliyetlerin devamlı ve bağımsız şekilde yürütüldüğü işletmedir; tescil tanım unsuru değildir.")

P.sayisal("TTK md. 40",
    f"{K}, tacir ticari işletmesini ve ticaret unvanını işletmenin açıldığı günden itibaren kaç gün içinde tescil ve ilan "
    "ettirir?",
    "15", ["7", "10", "30", "45"],
    "Md. 40/1'e göre her tacir ticari işletmesini ve seçtiği ticaret unvanını işletmenin açıldığı günden itibaren on beş gün "
    "içinde işletme merkezinin bulunduğu yer ticaret siciline tescil ve ilan ettirir.")

P.q("TTK md. 11",
    f"{K26}, ticari işletme ile esnaf işletmesi arasındaki sınırı belirlemeye yetkili makam aşağıdakilerden hangisidir?",
    "Cumhurbaşkanı",
    ["Ticaret Bakanlığı", "Türkiye Odalar ve Borsalar Birliği", "Gelir İdaresi Başkanlığı", "Türkiye İstatistik Kurumu"],
    "Md. 11/2'ye göre ticari işletme ile esnaf işletmesi arasındaki sınır Cumhurbaşkanı kararıyla belirlenir.", zorluk="easy")

P.q("TTK md. 11",
    f"{K}, ticari işletmenin bütün hâlinde devrine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Devir sözleşmesi sözlü olarak yapılabilir.",
    ["Unsurlar için ayrı tasarruf işlemi gerekmez.",
     "Aksi öngörülmedikçe kiracılık hakkını kapsar.",
     "Aksi öngörülmedikçe ticaret unvanını kapsar.",
     "Sözleşme ticaret siciline tescil ve ilan edilir."],
    "Md. 11/3'e göre ticari işletmeyi bir bütün hâlinde konu alan devir sözleşmesi yazılı olarak yapılır, ticaret siciline "
    "tescil ve ilan edilir.")

P.sayisal("TTK md. 5/A",
    f"{K}, ticari davalarda dava şartı arabuluculukta, uzatma dahil arabuluculuk süreci en fazla kaç hafta sürebilir?",
    "8", ["4", "6", "10", "12"],
    "Md. 5/A'ya göre arabulucu başvuruyu altı hafta içinde sonuçlandırır; zorunlu hâllerde en fazla iki hafta uzatılabilir: "
    "6 + 2 = 8 hafta.", zorluk="hard")

P.q("TTK md. 11",
    f"{K}, aksi öngörülmemişse ticari işletme devir sözleşmesinin kapsamına aşağıdakilerden hangisi girmez?",
    "İşletme sahibinin özel konutu",
    ["Duran malvarlığı",
     "İşletme değeri",
     "Kiracılık hakkı",
     "Ticaret unvanı"],
    "Md. 11/3'e göre aksi öngörülmemişse devir sözleşmesi duran malvarlığını, işletme değerini, kiracılık hakkını, ticaret "
    "unvanı ile diğer fikrî mülkiyet haklarını ve işletmeye sürekli özgülenen unsurları içerir; özel konut bu kapsamda "
    "değildir.")

P.q("TTK md. 12",
    f"{K}, tacir sıfatının kazanılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fiilen işletmeye başlamadan tacir olunmaz.",
    ["Ticari işletmeyi kısmen kendi adına işleten tacirdir.",
     "Açılışı ilanla halka bildiren tacir sayılır.",
     "İşletmesini tescil ettirip ilan eden tacir sayılır.",
     "Adi şirket adına tacir gibi davranan sorumlu olur."],
    "Md. 12/2'ye göre ticari işletmeyi kurup açtığını ilan araçlarıyla halka bildiren veya tescil ettirip ilan eden kimse "
    "fiilen işletmeye başlamamış olsa bile tacir sayılır.")

P.q("TTK md. 12",
    "Bay (A), gerçekte bir ticari işletmesi olmadığı hâlde adi şirket ortağı sıfatıyla ticari işletme açmış gibi "
    f"işlemlerde bulunmuştur.\n\n{K}, Bay (A)’nın iyiniyetli üçüncü kişilere karşı durumu nedir?",
    "Tacir gibi sorumlu olur.",
    ["Herhangi bir sorumluluğu yoktur.",
     "Sadece ceza sorumluluğu vardır.",
     "Esnaf gibi sorumlu olur.",
     "Sorumluluk adi şirkete aittir."],
    "Md. 12/3'e göre ticari işletme açmış gibi kendi adına veya adi şirket adına ortak sıfatıyla işlem yapan kimse iyiniyetli "
    "üçüncü kişilere karşı tacir gibi sorumlu olur.", zorluk="hard")

P.q("TTK md. 13",
    "On altı yaşındaki (K)’ya ait ticari işletmeyi velisi Bay (L), (K) adına işletmektedir."
    f"\n\n{K}, tacir sıfatı hakkında aşağıdakilerden hangisi doğrudur?",
    "Tacir sıfatı (K)’ya aittir.",
    ["Tacir sıfatı Bay (L)’ye aittir.",
     "İkisi birlikte tacir sayılır.",
     "Küçük olduğu için kimse tacir sayılmaz.",
     "Tacir sıfatı mahkemece belirlenir."],
    "Md. 13'e göre küçük ve kısıtlılara ait ticari işletmeyi onlar adına işleten yasal temsilci tacir sayılmaz; tacir sıfatı "
    "temsil edilene aittir.")

P.q("TTK md. 13",
    f"{K}, küçüğe ait ticari işletmeyi işleten yasal temsilcinin hukuki durumuna ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Ceza hükümlerinde tacir gibi sorumludur.",
    ["Her bakımdan tacir sayılır.",
     "İflasa tabi tacirdir.",
     "Ticari defter tutma ve tescil yükümlüsüdür.",
     "Herhangi bir sorumluluğu yoktur."],
    "Md. 13'e göre yasal temsilci tacir sayılmaz; ancak ceza hükümlerinin uygulanması yönünden tacir gibi sorumlu olur.",
    zorluk="hard")

P.q("TTK md. 14",
    "Devlet memuru Bay (M), kanuni yasağa rağmen izin almadan bir ticari işletme işletmektedir."
    f"\n\n{K}, Bay (M)’nin durumu hakkında aşağıdakilerden hangisi doğrudur?",
    "Tacir sayılır; disiplin sorumluluğu saklıdır.",
    ["Yasak nedeniyle tacir sayılmaz.",
     "Esnaf sayılır.",
     "İşlemleri kesin hükümsüzdür.",
     "Sadece disiplin cezası alır, tacir sayılmaz."],
    "Md. 14'e göre kanundan doğan yasağa aykırı olarak veya izin almadan ticari işletme işleten kişi de tacir sayılır; "
    "hukuki, cezai ve disipline ilişkin sorumluluğu saklıdır.")

P.q("TTK md. 15",
    f"{K}, esnafa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Esnafa tacirlere özgü bir hüküm uygulanmaz.",
    ["Ekonomik faaliyeti bedenî çalışmasına dayanır.",
     "Geliri kararnamedeki sınırı aşmaz.",
     "Gezici olarak da faaliyet gösterebilir.",
     "Uygun ücret isteme hakkı esnafa da uygulanır."],
    "Md. 15'e göre tacirlere özgü md. 20 (ücret isteme) ve md. 53 (işletme adı) ile TMK md. 950/2 hükmü esnafa da uygulanır.")

P.q("TTK md. 16",
    f"{K}, aşağıdakilerden hangisi tacir sayılmaz?",
    "Ticari işletme işleten belediye",
    ["Anonim şirket",
     "Ticari işletme işleten vakıf",
     "Ticari işletme işleten dernek",
     "Özel hukuka göre yönetilen kamu kuruluşu"],
    "Md. 16/2'ye göre Devlet, il özel idaresi, belediye, köy ve diğer kamu tüzel kişileri ticari işletme işletseler de "
    "kendileri tacir sayılmaz.", zorluk="easy")

P.q("TTK md. 16",
    f"{K}, aşağıdakilerden hangisi ticari işletme işletse bile kendisi tacir sayılmaz?",
    "Kamu yararına çalışan dernek",
    ["Limited şirket",
     "Kollektif şirket",
     "Amacı için ticari işletme işleten vakıf",
     "Kooperatif"],
    "Md. 16/2'ye göre kamu yararına çalışan dernekler ile gelirinin yarısından fazlasını kamu görevi niteliğindeki işlere "
    "harcayan vakıflar bir ticari işletme işletseler de tacir sayılmaz.", zorluk="hard")

P.q("TTK md. 17",
    f"{K}, donatma iştirakine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tacire ilişkin hükümler aynen uygulanır.",
    ["Esnafa ilişkin hükümler uygulanır.",
     "Tacir hükümleri uygulanmaz.",
     "Sadece sicil hükümleri uygulanır.",
     "Donatma iştiraki kamu tüzel kişisidir."],
    "Md. 17'ye göre tacire ilişkin hükümler donatma iştirakine de aynen uygulanır.")

P.q("TTK md. 24",
    f"{K}, ticaret sicilinin tutulmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bakanlık denetiminde sicil müdürlüklerince",
    ["Asliye ticaret mahkemelerince tutulur.",
     "Vergi dairelerince mükellef kayıtlarıyla birlikte tutulur.",
     "Noterlerce tutulur.",
     "Belediyelerce tutulur."],
    "Md. 24/2'ye göre ticaret sicili Bakanlığın gözetim ve denetiminde ticaret sicili müdürlükleri ve şubeleri tarafından "
    "tutulur.")

P.q("TTK md. 27",
    f"{K}, ticaret siciline tescile ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tescil kural olarak resen yapılır.",
    ["Harca tabi işlerde harç makbuzu tarihi belirleyicidir.",
     "Kurumlar vergisi mükellefinin evrakı vergi dairesine iletilir.",
     "Tescil istemi temsilci tarafından da yapılabilir.",
     "Birden çok yükümlüden birinin istemi yeterlidir."],
    "Md. 27/1'e göre ticaret siciline tescil kural olarak istem üzerine yapılır; resen veya yetkili kurumun bildirmesiyle "
    "yapılacak tesciller saklıdır.", zorluk="easy")

P.q("TTK md. 27",
    f"{K}, ticaret siciline tescil için başvuran kurumlar vergisi mükellefinin işe başlamayı bildirme yükümlülüğü "
    "hakkında aşağıdakilerden hangisi doğrudur?",
    "Yerine getirilmiş sayılır.",
    ["Ayrıca vergi dairesine bildirilmelidir.",
     "Tescilden bir ay sonra doğar.",
     "Tacirin ayrı beyanıyla yerine getirilir.",
     "Ancak vergi dairesinin davetiyle doğar."],
    "Md. 27/2'ye göre sicil müdürlükleri kurumlar vergisi mükelleflerinin başvuru evrakının suretini vergi dairesine iletir ve "
    "bu mükelleflerin işe başlamayı bildirme yükümlülükleri yerine getirilmiş sayılır.")

P.q("TTK md. 28",
    f"{K}, bir hususun tescilini istemeye birden çok kişinin yükümlü olması hâlinde aşağıdakilerden hangisi doğrudur?",
    "Birinin istemi hepsince istenmiş sayılır.",
    ["Tüm yükümlülerin birlikte başvurması şarttır.",
     "Tescil ancak noter onaylı ortak dilekçeyle yapılır.",
     "Yükümlülerin çoğunluğunun başvurusu gerekir.",
     "Tescil mahkeme kararıyla yapılır."],
    "Md. 28/2'ye göre kanunda aksine hüküm bulunmadıkça yükümlülerden birinin talebi üzerine yapılan tescil tümü tarafından "
    "istenmiş sayılır.")

P.q("TTK md. 30",
    f"{K}, tescil isteme süresinin başlangıcına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Olgunun gerçekleştiği tarih",
    ["Sicil müdürünün davet tarihi",
     "Takvim yılının başı",
     "Vergi mükellefiyetinin başladığı tarih",
     "Ticaret odasına kayıt tarihi"],
    "Md. 30/2'ye göre tescil isteme süresi tescili gerekli işlem veya olgunun gerçekleştiği, belgeye bağlı durumlarda belgenin "
    "düzenlendiği tarihten başlar.")

P.q("TTK md. 32",
    f"{K}, sicil müdürünün incelemesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kamu düzenine aykırı hususlar da tescil edilebilir.",
    ["Tescilin kanuni şartlarını inceler.",
     "Şirket sözleşmesinin emredici hükümlere uygunluğunu inceler.",
     "Tescil edilecek hususlar gerçeği yansıtmalıdır.",
     "Yanlış izlenim yaratacak hususlar tescil edilmez."],
    "Md. 32/3'e göre tescil edilecek hususların gerçeği yansıtması, üçüncü kişilerde yanlış izlenim yaratmaması ve kamu "
    "düzenine aykırı olmaması şarttır.")

P.q("TTK md. 33",
    "Sicil müdürünün verdiği sürede tescil isteminde bulunmayan kişi, süresi içinde kaçınma sebeplerini bildirmiştir."
    f"\n\n{K}, bu durumda tescilin gerekli olup olmadığına kim karar verir?",
    "Asliye ticaret mahkemesi",
    ["Sicil müdürü", "Mülki amir", "Ticaret Bakanlığı", "Ticaret odası meclisi"],
    "Md. 33/3'e göre süresi içinde kaçınma sebepleri bildirilirse asliye ticaret mahkemesi dosya üzerinden inceleyerek tescili "
    "emreder veya istemi reddeder.", zorluk="hard")

P.q("TTK md. 34",
    f"{K}, sicil müdürlüğü kararlarına karşı itirazın incelenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Dosya üzerinden karara bağlanır.",
    ["Duruşma yapılması her dosyada şarttır.",
     "İtirazı Ticaret Bakanlığı inceler.",
     "İtiraz idare mahkemesinde görülür.",
     "İtiraz üzerine karar verilmez."],
    "Md. 34/2'ye göre itiraz mahkemece dosya üzerinden incelenerek karara bağlanır; sicil müdürünün kararı üçüncü kişilerin "
    "menfaatine aykırıysa itiraz eden ve üçüncü kişi de dinlenir.")

P.q("TTK md. 35",
    f"{K}, ticaret sicilinin açıklığına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sicili sadece ilgili tacir inceleyebilir.",
    ["Herkes sicilin içeriğini inceleyebilir.",
     "Belgelerin onaylı sureti alınabilir.",
     "Kayıt olmadığına dair belge istenebilir.",
     "İlan Türkiye Ticaret Sicili Gazetesi ile yapılır."],
    "Md. 35/2'ye göre herkes ticaret sicilinin içeriğini ve müdürlükte saklanan belgeleri inceleyebilir ve giderini ödeyerek "
    "onaylı suretlerini alabilir.")

P.q("TTK md. 36",
    f"{K}, ticaret sicili kayıtları üçüncü kişiler hakkında ne zamandan itibaren hukuki sonuç doğurur?",
    "İlanı izleyen iş gününden itibaren",
    ["Tescil başvurusu gününden itibaren",
     "Sicil müdürünün onay gününden itibaren",
     "İlandan bir ay sonra",
     "Takvim yılı sonundan itibaren"],
    "Md. 36/1'e göre sicil kayıtları üçüncü kişiler hakkında tescilin Türkiye Ticaret Sicili Gazetesinde ilan edildiği günü "
    "izleyen iş gününden itibaren hukuki sonuçlarını doğurur.")

P.q("TTK md. 37",
    f"{K}, tescil kaydı ile ilan edilen durum arasında aykırılık bulunması hâlinde aşağıdakilerden hangisi doğrudur?",
    "Üçüncü kişilerin ilana güveni korunur.",
    ["Kural olarak tescil kaydı esas alınır.",
     "İlan doğrudan hükümsüz olur.",
     "Üçüncü kişiler tescil kaydını araştırmakla yükümlüdür.",
     "Aykırılık varsa sicil kaydı silinir."],
    "Md. 37'ye göre tescil edilmiş gerçek durumu bildikleri ispat edilmediği sürece üçüncü kişilerin ilan edilen duruma "
    "güvenleri korunur.", zorluk="hard")

P.q("TTK md. 38",
    f"{K}, tescil ettirme yükümlülüğünü yerine getirmeyenlerin sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kusurlu oldukları zararı tazmin ederler.",
    ["Sorumlulukları sadece idari para cezasıyla sınırlıdır.",
     "Üçüncü kişilere karşı sorumlulukları yoktur.",
     "Zarardan sicil müdürü sorumludur.",
     "Sorumluluk tescilden sonra doğar."],
    "Md. 38/2'ye göre kayıtların düzeltilmesini veya değişikliklerin tescilini istemekle yükümlü olup bunu yapmayanlar, bu "
    "kusurları nedeniyle üçüncü kişilerin uğradıkları zararları tazmin ile yükümlüdür.")

P.oncul("TTK md. 16",
    f"{K} aşağıdaki kişi ve kuruluşlar değerlendirilmektedir:",
    ["Anonim şirket",
     "Ticari işletme işleten il özel idaresi",
     "Amacı için ticari işletme işleten dernek",
     "Kamu yararına çalışan dernek"],
    "Yukarıdakilerden hangileri tacir sayılır?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 16'ya göre ticaret şirketleri (I) ve amacına varmak için ticari işletme işleten dernekler (III) tacir sayılır; il özel "
    "idaresi (II) ve kamu yararına çalışan dernek (IV) ticari işletme işletse de tacir sayılmaz.", zorluk="hard")

P.q("TTK md. 4",
    f"{K}, ticari davalarda deliller ve basit yargılama usulüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Deliller Hukuk Muhakemeleri Kanununa tabidir.",
    ["Ticari davalarda tanık dinlenemez.",
     "Deliller Ceza Muhakemesi Kanununa tabidir.",
     "Ticari davalarda sadece yazılı delil kabul edilir.",
     "Tüm ticari davalarda sözlü yargılama uygulanır."],
    "Md. 4/2'ye göre ticari davalarda deliller ile sunulması HMK hükümlerine tabidir; Kanundaki parasal sınırı geçmeyen "
    "ticari davalarda basit yargılama usulü uygulanır.")

P.q("TTK md. 5",
    f"{K}, asliye ticaret mahkemesi ile asliye hukuk mahkemesi arasındaki ilişkiye ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Aralarındaki ilişki görev ilişkisidir.",
    ["Aralarındaki ilişki iş bölümü ilişkisidir.",
     "Aralarındaki ilişki yetki ilişkisidir.",
     "Aralarında bir ilişki bulunmaz.",
     "Asliye hukuk üst mahkemedir."],
    "Md. 5/3'e göre asliye ticaret mahkemesi ile asliye hukuk mahkemesi ve diğer hukuk mahkemeleri arasındaki ilişki görev "
    "ilişkisidir.", zorluk="hard")

P.q("TTK md. 2",
    f"{K}, teamülün hukuki değerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Örf ve âdet olmadıkça yargıya esas olmaz.",
    ["Kural olarak mahkemeyi bağlar.",
     "Kanun hükmünden önce uygulanır.",
     "Sadece tüketici işlemlerinde uygulanır.",
     "İrade açıklamalarının yorumunda dikkate alınmaz."],
    "Md. 2/1'e göre kanunda aksine hüküm yoksa ticari örf ve âdet olarak kabul edildiği belirlenmedikçe teamül mahkemenin "
    "yargısına esas olamaz; ancak irade açıklamalarının yorumunda dikkate alınır.")

P.q("TTK md. 32",
    f"{K}, tüzel kişilerin tescilinde sicil müdürünün özellikle incelemesi gereken husus aşağıdakilerden hangisidir?",
    "Emredici hükümlere uygunluk",
    ["Ortakların kredi notları",
     "Şirketin kârlılık beklentisi",
     "Ortakların eğitim durumu",
     "Şirketin pazar payı"],
    "Md. 32/2'ye göre tüzel kişilerin tescilinde özellikle şirket sözleşmesinin emredici hükümlere aykırı olup olmadığı ve "
    "kanunun zorunlu kıldığı hükümleri içerip içermediği incelenir.")

P.q("TTK md. 36",
    f"{K}, üçüncü kişilerin tescil ve ilan edilmiş bir hususu bilmediklerini ileri sürmelerine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Kaydı bilmediklerini ileri süremezler.",
    ["Kural olarak bilmediklerini ileri sürebilirler.",
     "Ancak tacir değillerse ileri sürebilirler.",
     "İlandan bir yıl sonra ileri sürebilirler.",
     "Sadece yabancılar ileri sürebilir."],
    "Md. 36/3'e göre üçüncü kişiler, sonuç doğurmaya başlamış bir sicil kaydını bilmediklerini ileri süremezler.",
    zorluk="hard")

P.q("TTK md. 5",
    f"{K}, asliye ticaret mahkemesi bulunmayan yargı çevresinde açılan ticari davaya ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Asliye hukuk mahkemesi görevsizlik kararı verir.",
    ["Asliye hukuk mahkemesi davaya devam eder.",
     "Görev kuralına dayanılmamış olması sorun oluşturmaz.",
     "Dava ticari dava niteliğini korur.",
     "Deliller HMK hükümlerine tabidir."],
    "Md. 5/4'e göre asliye ticaret mahkemesi bulunmayan yargı çevresindeki bir ticari davada görev kuralına dayanılmamış "
    "olması görevsizlik kararı verilmesini gerektirmez; asliye hukuk mahkemesi davaya devam eder.")

P.q("TTK md. 36",
    f"{K}, tescili zorunlu olduğu hâlde tescil edilmemiş bir husus üçüncü kişilere karşı ne zaman ileri sürülebilir?",
    "Bildikleri veya bilmeleri gerektiği ispatlanırsa",
    ["Tescil olmadan ileri sürülemez.",
     "Doğrudan ileri sürülebilir.",
     "Sadece tacir olmayanlara karşı",
     "Sadece mahkeme izniyle"],
    "Md. 36/4'e göre tescili zorunlu olduğu hâlde tescil edilmemiş veya ilan olunmamış bir husus, ancak üçüncü kişilerin "
    "bunu bildikleri veya bilmeleri gerektiği ispat edilirse onlara karşı ileri sürülebilir.", zorluk="hard")

P.q("TTK md. 1",
    f"{K}, Türk Ticaret Kanunu hangi kanunun ayrılmaz bir parçasıdır?",
    "Türk Medenî Kanunu",
    ["Türk Borçlar Kanunu", "Hukuk Muhakemeleri Kanunu", "Vergi Usul Kanunu", "İcra ve İflas Kanunu"],
    "Md. 1/1'e göre Türk Ticaret Kanunu, 4721 sayılı Türk Medenî Kanununun ayrılmaz bir parçasıdır.", zorluk="easy")

P.q("TTK md. 24",
    f"{K}, ticaret sicili müdürlüklerinin kuruluşuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müdürlükler sadece Ankara’da kurulabilir.",
    ["İl merkezindeki ticaret ve sanayi odalarında kurulur.",
     "Bakanlık il merkezi dışındaki odalarda da kurabilir.",
     "Müdürlüklere bağlı şubeler kurulabilir.",
     "Merkezi ortak veri tabanı oluşturulur."],
    "Md. 24/1'e göre ticaret sicili müdürlükleri il merkezindeki ticaret ve sanayi odaları ile ticaret odalarında kurulur; "
    "Bakanlık il merkezleri dışındaki odalarda da müdürlük ve şube kurabilir.")

P.q("TTK md. 26",
    f"{K26}, ticaret sicilinin tutulmasına ilişkin usul ve esasları düzenleyen yönetmelik kim tarafından çıkarılır?",
    "Cumhurbaşkanı",
    ["Ticaret sicili müdürü", "Türkiye Odalar ve Borsalar Birliği", "Yargıtay", "Asliye ticaret mahkemesi"],
    "Md. 26'ya göre ticaret sicili müdürlüğünün kurulması, defterlerin tutulması ve tescil usullerine ilişkin esaslar "
    "Cumhurbaşkanınca çıkarılacak yönetmelikte düzenlenir.")

P.q("TTK md. 9",
    f"{K}, ticari işlerde kanuni faiz ve temerrüt faizi hakkında hangi hükümler uygulanır?",
    "İlgili mevzuat hükümleri",
    ["Tarafların iradesi",
     "Ticari örf ve âdet",
     "Mahkemenin takdiri",
     "Ticaret odasının tarifesi"],
    "Md. 9'a göre ticari işlerde kanuni faiz, anapara ile temerrüt faizi hakkında ilgili mevzuat hükümleri uygulanır.")

P.q("TTK md. 36",
    "Bir tescil ilanı Türkiye Ticaret Sicili Gazetesinin iki ayrı nüshasında kısım kısım yayımlanmıştır."
    f"\n\n{K}, tescil üçüncü kişiler hakkında ne zamandan itibaren sonuç doğurur?",
    "Son kısmın yayımını izleyen iş gününden",
    ["İlk kısmın yayımlandığı günden",
     "İlk kısmın yayımını izleyen iş gününden",
     "Tescil başvurusunun yapıldığı günden",
     "Son kısmın yayımından bir ay sonra"],
    "Md. 36/1'e göre ilanın tamamı aynı nüshada yayımlanmamışsa sicil kaydı son kısmının yayımlandığı günü izleyen iş "
    "gününden itibaren hukuki sonuçlarını doğurur.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
