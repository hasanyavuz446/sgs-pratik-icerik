#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Sermaye Piyasası Mevzuatı — Kaydi Sistem ve MKK, 3×20.

Dayanaklar 17.07.2026 tarihinde 6362 sayılı Kanunun güncel metni ile
Kaydileştirme Tebliği'nin (II-13.1) Ağustos 2025 güncel metni üzerinden
doğrulanmıştır. MKK'nın görevleri güncel Kanunun 80'inci maddesindedir.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors,
        "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r(
        "Bir yatırımcı MKK'yı fiziki menkul kıymetlerin depolandığı bir kamu kurumu olarak nitelendirmiştir. 17.07.2026 itibarıyla doğru nitelendirme hangisidir?",
        "6362 sayılı Kanuna göre MKK'nın hukuki niteliği ve temel işlevi nedir?",
        "Özel hukuk anonim şirketi ve merkezi saklama kuruluşudur",
        ["Fiziki senet basan genel bütçeli kamu idaresidir", "Alım satım emirlerini eşleştiren menkul kıymet borsasıdır", "Mevduat kabul edip kredi veren ticari bankadır", "Bağımsız denetim raporlarını onaylayan meslek odasıdır"],
        "Kanunun güncel 80'inci maddesine göre MKK özel hukuk tüzel kişiliğini haiz anonim şirkettir; kaydi araçları ve hakları izler ve merkezi saklama görevini yürütür.",
        "MKK bir fiyat oluşum platformu veya fiziki depo değildir; kaydi araçlar bakımından merkezi saklama ve hak sahipliği kayıt altyapısıdır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.79-80", "easy",
    ),
    r(
        "Bir ihraççı, Kurulun kaydileştirme kapsamına aldığı sermaye piyasası aracını yine de fiziki sertifikalar basarak ihraç etmek istemektedir. Genel kurala uygun mudur?",
        "Kaydileştirilen sermaye piyasası araçlarının ihracında belge ve elektronik kayıt bakımından genel esas nedir?",
        "Hayır; belge çıkarılmadan elektronik kaydi ihraç esastır",
        ["Evet; her kaydi araç için ayrıca fiziki senet basılması zorunludur", "Evet; belge basımı yalnız yatırımcının sözlü talebine bağlıdır", "Hayır; çünkü sermaye piyasası aracı hiçbir şekilde ihraç edilemez", "Evet; kaydileştirme yalnız borsanın işlem saatlerini düzenler"],
        "Kanun m.13 ve Tebliğ m.14 uyarınca kaydileştirme kapsamındaki araçların senede bağlanmaksızın elektronik ortamda kaydi olarak ihracı esastır.",
        "Hangi araç ve hakların kayden izleneceğini Kurul belirler; kapsam içindeki ihraçta fiziki belge çıkarılması genel model değildir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/1; Kaydileştirme Tebliği m.14", "easy",
    ),
    r(
        "Hamiline yazılı bir payın kaydi sistemde kişi adına izlenemeyeceği, yalnız nama yazılı payların hak sahibi hesaplarında tutulacağı ileri sürülmüştür. Bu görüş doğru mudur?",
        "Kaydi sistemde nama veya hamiline yazılı olma, hak sahibi adına hesapta izlemeyi nasıl etkiler?",
        "Hayır; her ikisi de kural olarak hak sahibi adına izlenir",
        ["Evet; hamiline araçlar kaydi sistemin tamamen dışındadır", "Evet; nama yazılı araçlar yalnız ihraççı adına tutulur", "Hayır; bütün araçlar yalnız MKK'nın kendi mülkiyetinde izlenir", "Evet; hak sahibi hesabı yalnız fiziki tahviller için açılır"],
        "Kanun m.13/2 ve Tebliğ m.11, araçların nama veya hamiline olmasına bakılmaksızın hak sahipleri itibarıyla isimle eşleştirilmiş hesaplarda izlenmesini esas alır.",
        "Kurulun izin verdiği toplu hesap istisnası saklıdır; senedin yazılış türü tek başına kişi bazlı izleme kuralını ortadan kaldırmaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/2; Kaydileştirme Tebliği m.11/1", "medium",
    ),
    r(
        "Aracı kurum, MKK altyapısı dışında kendi yerel tablosunda tuttuğu kaydı resmi kaydi sistem kaydı saymaktadır. Kayıt düzeni bakımından doğru yaklaşım hangisidir?",
        "Kaydi sermaye piyasası araçları ve bunlara bağlı haklara ilişkin kayıtlar kim tarafından, hangi ortamda tutulur?",
        "MKK üyelerince MKK'nın elektronik ortamında tutulur",
        ["Yalnız ihraççının kâğıt pay defterinde tutulur", "Her yatırımcının kendi bilgisayarında bağımsız tutulur", "Borsa üyeliği olmayan herhangi bir gerçek kişi tutar", "Yalnız vergi dairesinin fiziki arşivinde saklanır"],
        "Kanun m.13/3 ve Tebliğ m.5'e göre kayıtlar MKK'nın oluşturduğu elektronik ortamda, MKK üyelerince tutulur; yerel tablo resmi kayıt altyapısının yerini alamaz.",
        "MKK merkezi elektronik altyapıyı oluşturur; ihraççı, yatırım kuruluşu ve diğer üyeler yetkileri ölçüsünde kayıt işlemlerini bu altyapıda yürütür.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/3; Kaydileştirme Tebliği m.5/1", "easy",
    ),
    r(
        "MKK üyesi hatalı kayıt nedeniyle yatırımcıyı zarara uğratmış, MKK'nın da sistem kontrolünde kusuru bulunduğu saptanmıştır. Sorumluluk nasıl belirlenir?",
        "MKK ve üyelerinin kaydi kayıtların yanlış tutulmasından doğan zarardaki sorumluluk esası nedir?",
        "Zarardan kusurları oranında birlikte sorumlu olurlar",
        ["Yalnız yatırımcı her durumda bütün zararı üstlenir", "MKK kusurlu olsa da hiçbir şekilde sorumlu tutulamaz", "Üye yalnız kâr edilmişse zarardan sorumlu olur", "Zarar otomatik olarak ihraççının tüm ortaklarına yüklenir"],
        "Kanun m.80/4, MKK ile üyelerini kaydi kayıtların yanlış tutulmasından doğan zararlardan kusurları oranında sorumlu tutar.",
        "Sorumluluk kayıt zincirindeki görev ve kusura göre dağıtılır; MKK veya üyenin konumu kendiliğinden mutlak sorumsuzluk yaratmaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.80/4", "medium",
    ),
    r(
        "MKK, kaydi kayıtların doğruluğunu denetlemek için üyesinden bilgi istemiş; üye özel kanundaki sır yükümlülüğünü ileri sürerek tamamen reddetmiştir. Sonuç nedir?",
        "MKK'nın üyelerinden bilgi ve belge isteme yetkisi ile Kurulun MKK üzerindeki konumu nasıldır?",
        "Üye bilgiyi vermelidir; MKK ayrıca Kurul gözetimindedir",
        ["Üye her durumda reddeder ve MKK hiçbir kuruma tabi değildir", "Bilgiyi yalnız yatırımcı isterse verir; Kurul denetim yapamaz", "MKK üyeden belge isteyemez, sadece fiyat tavsiyesi verir", "Üye kayıtları siler ve talep kendiliğinden sona erer"],
        "Kanun m.80'e göre MKK görevleri için üyelerinden bilgi ve belge isteyebilir; üyeler özel kanun hükümlerini ileri sürerek kaçınamaz. MKK'nın faaliyetleri Kurulca gözetilir ve denetlenir.",
        "Bilgi isteme yetkisi kayıt sisteminin bütünlüğünü destekler; bu yetki MKK'yı denetimsiz kılmaz, Kurul gözetimi devam eder.",
        "6362 sayılı Sermaye Piyasası Kanunu m.80/3 ve 5", "hard",
    ),
    r(
        "Kaydileştirme kapsamına alınan bir aracın eski fiziki belgesi MKK üyesine teslim edilmiştir. Teslimden sonra belgeyle tekrar devir yapılmak istenmektedir. Hukuki sonuç nedir?",
        "Kaydileştirme amacıyla teslim edilen eski fiziki sermaye piyasası araçlarının belge niteliği ne olur?",
        "Teslimle belge geçersizleşir ve yeniden kullanılamaz",
        ["Belge ikinci kez tedavüle sokulabilir ve iki ayrı hak doğurur", "Belge yalnız noter tasdikiyle yeniden geçerli olur", "Belge MKK'nın pay senedine dönüşüp oy hakkı verir", "Teslim elektronik kaydı geçersiz kılar ve hakkı sona erdirir"],
        "Kanun m.13/4 ve Tebliğ m.15 uyarınca kaydileştirme için teslim edilen fiziki belgeler kendiliğinden geçersiz hâle gelir; aynı hak için yeniden tedavül edilemez.",
        "Geçersizlik, mükerrer hak ve devir riskini önler. Hak ortadan kalkmaz; elektronik kaydi sistemde izlenmeye devam eder.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/4; Kaydileştirme Tebliği m.15", "medium",
    ),
    r(
        "Aynı kaydi pay üzerinde iki ayrı kişiye farklı tarihlerde hak devri yapılmış, bildirimler MKK'ya farklı günlerde ulaşmıştır. Üçüncü kişilere karşı hak ileri sürmede hangi tarih esas alınır?",
        "Kaydi araçlara ilişkin hakların üçüncü kişilere karşı ileri sürülmesinde belirleyici zaman ölçütü nedir?",
        "MKK bildirim tarihi üçüncü kişilere karşı esas alınır",
        ["Tarafların kendi aralarında düşündüğü gizli tarih esas alınır", "Fiziki senedin basılacağı varsayımsal tarih esas alınır", "İhraççının kuruluş sözleşmesinin tarihi esas alınır", "Yatırımcının ilk banka hesabı açma tarihi esas alınır"],
        "Kanun m.13/5 ve Tebliğ m.27, kaydi hakların üçüncü kişilere karşı ileri sürülmesinde MKK'ya yapılan bildirimin tarihini esas alır.",
        "Taraflar arasındaki ilişkinin hükmü ayrı değerlendirilebilir; üçüncü kişilere karşı aleniyet ve öncelik kaydi sisteme bildirimle ilişkilidir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/5; Kaydileştirme Tebliği m.27", "medium",
    ),
    r(
        "Anonim ortaklık, kayden izlenen pay sahibini pay defterine yazmak için ayrıca noter onaylı başvuru şartı koymuştur. Genel kural bakımından bu şart doğru mudur?",
        "Kayden izlenen paylara ilişkin MKK kayıtları anonim şirketin pay defterinde nasıl kullanılır?",
        "MKK kayıtları ek başvuru olmadan pay defterinde esas alınır",
        ["MKK kayıtları pay defterinde hiçbir zaman kullanılamaz", "Yalnız fiziki pay senedi getiren kişi deftere yazılabilir", "Pay defteri tamamen borsa tarafından ve fiyatlara göre tutulur", "Kayıt için bütün pay sahiplerinin oybirliği zorunludur"],
        "Kanun m.13/6'ya göre payların devrinin şirket pay defterine kaydında MKK nezdindeki kayıtlar, ilgililerin ayrıca başvurusu aranmaksızın esas alınır.",
        "Kaydi sistem şirketin pay sahipliği bilgisini güncel tutmasını sağlar; şirket ek başvuruyla kanuni kayıt etkisini geciktiremez.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/6", "easy",
    ),
    r(
        "İcra dairesi kaydi pay üzerindeki haczi doğrudan MKK üyesi dışındaki bir yazılım şirketine uygulatmak istemektedir. Uygulama kanuna uygun mudur?",
        "Kayden izlenen sermaye piyasası araçları üzerindeki haciz ve tedbirler hangi kanal üzerinden uygulanır?",
        "Hayır; işlem münhasıran MKK üyelerince yürütülür",
        ["Evet; herhangi bir yazılım şirketi kayda doğrudan haciz işler", "Evet; haciz yalnız fiziki senedin yakılmasıyla uygulanır", "Hayır; kaydi araçlara hiçbir koşulda haciz konulamaz", "Evet; yalnız ihraççının genel kurulu haciz kararı verebilir"],
        "Kanun m.13/7 ve Tebliğ m.26 uyarınca kaydi araçlar üzerindeki haciz, tedbir ve benzeri idari-adli talepler münhasıran MKK üyelerince ilgili alt hesaplarda yerine getirilir.",
        "Kaydi araç haczedilebilir; ancak uygulama merkezi kayıt bütünlüğünü korumak için yetkili üye kanalıyla yapılır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/7; Kaydileştirme Tebliği m.26", "medium",
    ),
    r(
        "Bir gerçek kişi, MKK'da hiçbir üyeyle bağlantı kurmadan doğrudan yatırım kuruluşu sıfatıyla hesap açmak istemektedir. 17.07.2026 itibarıyla hesap yapısı nasıl kurulur?",
        "17.07.2026 itibarıyla MKK'da ana hesap açabilenler ve yatırımcı hesabının bağlantısı bakımından doğru ifade hangisidir?",
        "Ana hesap üyelerce; yatırımcı hesabı ilgili üyeye bağlı açılır",
        ["Her gerçek kişi MKK üyesi sayılarak sınırsız ana hesap açar", "Yatırımcı hesabı hiçbir üyeyle ilişkilendirilmeden gizli tutulur", "Yalnız borsa ana hesap açar ve tüm yatırımcıları tek kişi sayar", "Hesaplar fiziki senet matbaasınca ve kâğıt ortamında açılır"],
        "Tebliğ m.6 uyarınca TCMB, ihraççılar, yatırım kuruluşları, merkezi takas kuruluşları ve belirlenen diğer üyeler için MKK'da hesap açılır; yatırımcı hesabı kimlik bildirimiyle ilgili üyeye bağlıdır.",
        "Yatırımcı MKK'nın üyesi hâline gelmez; hak sahibi olarak, hizmet aldığı üyenin bağlantısındaki yatırımcı hesabında izlenir.",
        "Kaydileştirme Tebliği (II-13.1) m.6", "medium",
    ),
    r(
        "Aracı kurum müşteriye ait araçları gerçekte havuz hesabında tuttuğu hâlde hesabın adını 'bireysel yatırımcı hesabı' koymuştur. İsimlendirme işlemin niteliğini değiştirir mi?",
        "MKK sisteminde açılan hesapların adlandırılması ve gerçek niteliği bakımından hangi kural geçerlidir?",
        "Hayır; hesap adı gerçek niteliği gizleyemez",
        ["Evet; hesap adı her türlü işlemi hukuka uygun hâle getirir", "Evet; üyeler müşteri varlığını kendi mülkiyeti gibi gösterebilir", "Hayır; çünkü bütün hesaplar yalnız ihraççı havuzu sayılır", "Evet; hesap türleri yalnız yatırımcının takma adına göre belirlenir"],
        "Tebliğ m.6, hesapların işlemlerin gerçek niteliğini gizleyecek biçimde açılamayacağını ve kullanılamayacağını düzenler.",
        "Hesap adı ve teknik etiket, varlığın kime ait olduğu veya işlemin amacı gibi maddi gerçeği değiştirmez.",
        "Kaydileştirme Tebliği (II-13.1) m.6/4", "easy",
    ),
    r(
        "Bir halka açık ortaklık, MKK'daki ihraççı hesabında yeni ihracı geçici izlemek ve kimliği henüz belirlenemeyen eski payları ayrı tutmak istemektedir. Hangi hesaplar kullanılır?",
        "İhraççı hesabının temel alt hesapları hangileridir?",
        "İhraççı havuz, ortak ve bilinmeyen ortak hesapları",
        ["Mevduat, kredi ve çek hesapları", "Takas, repo ve borsa fiyat hesapları", "Vergi, ceza ve gümrük hesapları", "Sigorta, emeklilik ve bağış hesapları"],
        "Tebliğ m.7, ihraççı hesabını ihraççı havuz hesabı, ortak hesabı ve bilinmeyen ortak hesabından oluşturur.",
        "İhraççı havuzu geçici ihraç kayıtlarını; ortak hesabı belirli payları; bilinmeyen ortak hesabı hak sahibi kimliği belirlenemeyen dönüşüm kayıtlarını izler.",
        "Kaydileştirme Tebliği (II-13.1) m.7", "easy",
    ),
    r(
        "Bir yatırım fonunun yeni katılma payları kaydi ihraç edilecek ve iade edilen paylar iptal edilecektir. İhraççı hesabında hangi alt hesap bu geçici işlemlerde kullanılır?",
        "İhraççı havuz hesabı ile fon ihraç ve iptal işlemleri arasındaki ilişki nedir?",
        "Yeni paylar geçici olarak ihraççı havuz hesabında izlenir",
        ["Bilinmeyen ortak hesabı bütün fon işlemlerinde zorunludur", "Yatırımcı blokaj hesabı pay ihracını kendiliğinden yapar", "Haciz alt hesabı yeni payların satış fiyatını belirler", "Ortak hesabı fon yöneticisinin şahsi malvarlığı sayılır"],
        "Tebliğ m.7'de ihraççı havuz hesabı kaydi ihraç edilen araçların geçici kaydı için kullanılır; yatırım fonu paylarının ihraç ve iptal kayıtları da bu hesap üzerinden yürütülür.",
        "Havuz hesabı geçici teknik duraktır; katılma payları yatırımcıya tahsis edildiğinde hak sahibi hesabına aktarılır.",
        "Kaydileştirme Tebliği (II-13.1) m.7/2", "medium",
    ),
    r(
        "Borsada işlem gören paylar ihraççının ortak hesabında sürekli izlenmek, kimliği bilinmeyen dönüşüm payları da yatırımcı hesabına yazılmak istenmektedir. Doğru kayıt düzeni hangisidir?",
        "İhraççı ortak hesabı ve bilinmeyen ortak hesabının kullanım alanları nasıl ayrılır?",
        "Ortak hesabı işlem görmeyen; bilinmeyen hesap kimliği belirsiz paylar içindir",
        ["Ortak hesabı yalnız mevduat; bilinmeyen hesap yalnız tahvil faizi içindir", "Her iki hesap da sadece borsa emirlerinin fiyatını belirler", "Ortak hesabı haciz; bilinmeyen hesap yatırım danışmanlığı içindir", "Her iki hesap MKK personelinin kişisel yatırım hesabıdır"],
        "Tebliğ m.7 uyarınca ortak hesabı borsada işlem görmeyen payların izlenmesinde; bilinmeyen ortak hesabı dönüşümde hak sahibi kimliği tespit edilemeyen kayıtların tutulmasında kullanılır.",
        "Borsada işlem gören yatırımcı payını sürekli ihraççı ortak hesabında tutmak kişi bazlı izleme sisteminin amacına uymaz.",
        "Kaydileştirme Tebliği (II-13.1) m.7/3-4", "hard",
    ),
    r(
        "Aracı kurum, borsa takasında teslim aldığı araçları doğrudan personelinin yatırımcı hesabına geçirmek istemektedir. Yatırım kuruluşu hesabında hangi yapı kullanılmalıdır?",
        "Yatırım kuruluşu hesabında takas ve müşteri varlıklarının izlenmesine hizmet eden temel hesaplar hangileridir?",
        "Takas havuzu, aracı kurum havuzu ve yatırımcı hesapları",
        ["İhraççı ortak, bilinmeyen ortak ve vergi hesapları", "Kredi, mevduat ve sigorta tazminat hesapları", "Borsa fiyat, denetim görüşü ve noter hesapları", "Yalnız personel adına açılan tek bir ortak hesap"],
        "Tebliğ m.10, yatırım kuruluşu hesabında DİBS depo hesabı yanında takas havuzu, aracı kurum havuzu ve yatırımcı hesaplarını öngörür; takas akışı havuzlar üzerinden hak sahibi hesaplarına ayrıştırılır.",
        "Aracı kurum havuzu üyeye ait serbest mülkiyet alanı değildir; takas ve dağıtım amacıyla kullanılan teknik hesaptır.",
        "Kaydileştirme Tebliği (II-13.1) m.10", "medium",
    ),
    r(
        "Yeni müşteri için yatırımcı hesabı açan üye, kimlik bilgisi bildirmeden hesabı anonim biçimde kullanıma açmış ve hakları bu hesaba kaydetmiştir. İşlem uygun mudur?",
        "Yatırımcı hesabının açılması ve hak sahibi adına izlenmesi için hangi temel bilgi gerekir?",
        "Hayır; hak sahibinin kimliği MKK'ya bildirilmelidir",
        ["Evet; bütün yatırımcı hesapları kimliksiz olmak zorundadır", "Evet; kimlik yerine yalnız portföyün piyasa değeri yeterlidir", "Hayır; ancak hesabı yalnız ihraççının çalışanı açabilir", "Evet; kayıtlar sadece takma adla tutulduğunda hukuken üstün olur"],
        "Tebliğ m.6 ve m.11 uyarınca yatırımcı hesabı hak sahibinin kimlik bilgilerinin MKK'ya bildirilmesiyle ve ilgili üyeye bağlı biçimde açılır.",
        "Kişi bazlı kaydi izlemenin temeli hesap ile hak sahibinin eşleştirilmesidir; izinli toplu hesap istisnası bu genel kuraldan ayrıdır.",
        "Kaydileştirme Tebliği (II-13.1) m.6 ve m.11", "easy",
    ),
    r(
        "Aynı yatırımcı iki farklı yatırım kuruluşunda hesap açmış; her kuruluş kendisine yeni ve bağımsız yatırımcı sicil numarası vermiştir. 17.07.2026 itibarıyla doğru uygulama nedir?",
        "17.07.2026 itibarıyla yatırımcı sicil numarası farklı MKK üyelerindeki hesaplar arasında nasıl işler?",
        "Yatırımcıya tek sicil numarası verilir ve kurumlar arasında aynıdır",
        ["Her işlem günü yeni bir sicil numarası verilmesi zorunludur", "Her sermaye piyasası aracı için farklı kimlik numarası üretilir", "Sicil numarası yalnız ihraççının ticaret unvanından oluşur", "Yatırımcı hesabı hiçbir numarayla ilişkilendirilemez"],
        "MKK hesap işleyişinde her yatırımcı için tekil sicil numarası oluşturulur; aynı kişi farklı üyelerdeki hesaplarında aynı sicil numarasıyla ilişkilendirilir.",
        "Tekil sicil, farklı üyelerdeki hesapların aynı hak sahibine ait olduğunun merkezi sistemde tutarlı biçimde izlenmesini sağlar.",
        "Kaydileştirme Tebliği (II-13.1) m.11; MKK Hesap İşlemleri Rehberi", "easy",
    ),
    r(
        "İki kişi birlikte sahip oldukları kaydi araçları ortak hesapta izletmek istemiş, üye ortaklık oranlarını sisteme girmeye gerek olmadığını söylemiştir. Bu yaklaşım doğru mudur?",
        "Müşterek yatırımcı hesabında hak sahipliği oranlarının kaydi sistemde gösterimi nasıl olmalıdır?",
        "Hayır; müşterek sahipler ve oranları kayıtta belirtilir",
        ["Evet; ortak hesapta hak sahiplerinin kimliği tamamen silinir", "Evet; araçların tamamı otomatik olarak üyeye ait sayılır", "Hayır; çünkü kaydi araçlarda müşterek hesap hiçbir zaman açılamaz", "Evet; oranları yalnız borsa başkanı sözlü olarak belirler"],
        "Tebliğ m.11, birden fazla kişinin müşterek hesabına kayda imkân verir; hak sahiplerinin kimliği ve mülkiyet oranları hesapta izlenir.",
        "Müşterek hesap kişi bazlı kaydı ortadan kaldırmaz; her ortağın hak payının kayıt düzeninde görünür olmasını gerektirir.",
        "Kaydileştirme Tebliği (II-13.1) m.11/2", "medium",
    ),
    r(
        "Yabancı bir merkezi saklama kuruluşu, müşterilerinin araçlarını kendi adına fakat hak sahibi olmadığı toplu hesapta izlemek istemektedir. Genel kişi bazlı sistemde bu mümkün müdür?",
        "Hak sahibi adına izleme kuralının toplu hesap istisnası hangi durumda uygulanabilir?",
        "Kurulca izin verilen koşullarda toplu hesap açılabilir",
        ["Her üye hiçbir koşul aranmadan gerçek hak sahibini gizleyebilir", "Toplu hesap yalnız MKK çalışanlarının kişisel payları için açılır", "Yabancı kuruluşlar kaydi sisteme hiçbir biçimde bağlanamaz", "Toplu hesap açılınca kayıt ve bildirim yükümlülükleri tamamen biter"],
        "Kanun m.13/2 ve Tebliğ m.12/A, Kurulca belirlenen şartlarla yabancı merkezi saklama kuruluşu veya genel saklama yetkilisi için hak sahibi olmayan toplu hesap açılmasına imkân verir.",
        "Toplu hesap düzenlenmiş bir istisnadır; gerçek hak sahipliğine ilişkin bilgi ve bildirim yükümlülüklerini sınırsız biçimde ortadan kaldırmaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.13/2; Kaydileştirme Tebliği m.12/A", "hard",
    ),
    r(
        "Yatırımcı, portföyündeki payların üye tarafından iradesi dışında devredilmesini önlemek; alacaklı da aynı pay üzerine rehin kaydı koymak istemektedir. Sistem bunu nasıl ayrıştırır?",
        "Kaydi sistemde yatırımcı blokajı, rehin ve haciz gibi hukuki durumlar hangi yöntemle izlenir?",
        "Rehin, haciz ve blokaj amaca özgü alt hesaplarda ayrı izlenir",
        ["Bütün durumlar kâğıt senedin arkasına el yazısıyla yazılır", "Yalnız üyenin bilançosunda tek bir gelir kalemi yapılır", "Her durumda pay yatırımcının hesabından tamamen silinir", "MKK dışındaki sosyal medya kaydı hukuki hesap sayılır"],
        "Tebliğ m.13, rehin, haciz, yatırımcı blokajı ve satış blokajı gibi durumlar için ayrı alt hesaplar öngörür.",
        "Alt hesaplar mülkiyetin ve tasarruf kısıtlarının birbirine karışmadan, amaçlarına uygun kodlarla izlenmesini sağlar.",
        "Kaydileştirme Tebliği (II-13.1) m.13", "medium",
    ),
    r(
        "Kurulca onaylanan ihraç belgesinden sonra ihraççı, yeni kaydi araçları yatırımcılara dağıtmadan önce kendi kişisel yatırım hesabına kaydetmiştir. Doğru süreç hangisidir?",
        "Kaydi sermaye piyasası aracının ilk ihracında ihraççı bildirimi ve geçici kayıt hangi hesap üzerinden yürütülür?",
        "İhraççı MKK'ya bildirir; araç önce ihraççı havuzuna kaydedilir",
        ["Araç önce ihraççının yöneticisinin şahsi hesabına kaydedilir", "İhraç belgesi onaylanınca MKK kaydına artık gerek kalmaz", "Yeni araç yalnız fiziki sertifika basılarak yatırımcıya verilir", "Araç ihracı yatırımcının haciz alt hesabından başlatılır"],
        "Tebliğ m.16 uyarınca ihraççı, izahname veya ihraç belgesi onayından sonra MKK'ya bildirim yapar; ihraç edilecek araçlar dağıtıma kadar ihraççı havuz hesabında geçici izlenir.",
        "İhraççı havuzu yeni hakların kaynağını ve dağıtımını izleyen teknik hesaptır; yöneticinin kişisel malvarlığına ait değildir.",
        "Kaydileştirme Tebliği (II-13.1) m.16", "medium",
    ),
    r(
        "Borsa işleminin takası tamamlanınca alıcının payı aracı kurumun havuzunda süresiz bırakılmış; satıcının hesabından alıcının hesabına doğrudan kişi transferi için de havuz kullanılmıştır. Hangisi doğrudur?",
        "Borsa takası ile hak sahibinden hak sahibine virmanda yatırım kuruluşu havuz hesaplarının işlevi nasıl ayrılır?",
        "Takas havuzlarla yürür; kişiden kişiye virmanda havuz kullanılmaz",
        ["Her iki işlemde de pay sonsuza kadar üye havuzunda tutulur", "Takas yalnız fiziki senet teslimiyle, virman noter kasasında yapılır", "Kişiden kişiye her transfer önce ihraççı bilinmeyen hesabına gider", "Borsa takasında yatırımcı hesabına hiçbir zaman kayıt yapılmaz"],
        "Tebliğ m.17'ye göre borsa takası, takas ve yatırım kuruluşu havuzları üzerinden sonuçta yatırımcı hesaplarına dağıtılır; hak sahibinden hak sahibine virman üye havuzundan geçirilmez.",
        "Havuz hesabı takasın geçici işlem zinciridir. Doğrudan müşteri virmanında havuzu araya sokmak hak sahipliği izini gereksiz biçimde keser.",
        "Kaydileştirme Tebliği (II-13.1) m.17", "hard",
    ),
    r(
        "İhraççı temettü ödemesinde kendi güncel olmayan listesini kullanmış, MKK kayıtlarını dikkate almamış ve yanlış kişiye ödeme yapmıştır. Sorumluluk ve ödeme esası nedir?",
        "Kaydi araçlara bağlı faiz ve temettü gibi mali hakların dağıtımında hangi kayıt esas alınır; yanlış veya geç ödeme kime yüklenir?",
        "MKK kayıtları esas alınır; yanlış veya geç ödemeden ihraççı sorumludur",
        ["Borsa kapanış fiyatı esas alınır; zarardan yatırımcı sorumludur", "Fiziki senedi basan matbaa esas alınır; kimse sorumlu değildir", "Üyenin reklam listesi esas alınır; MKK her durumda borçludur", "Ödeme rastgele yapılır; sonradan düzeltme yapılması yasaktır"],
        "Tebliğ m.18'e göre faiz, temettü ve benzeri mali haklar MKK kayıtlarındaki hak sahiplerine aktarılır; yanlış veya geç bildirim ve ödeme sonuçlarından ihraççı sorumludur.",
        "Merkezi hak sahipliği kayıtları dağıtımın kime yapılacağını gösterir; ihraççının güncel olmayan özel listesi bu esası değiştirmez.",
        "Kaydileştirme Tebliği (II-13.1) m.18", "medium",
    ),
    r(
        "Halka açık ortaklık genel kuruluna katılabileceklerin listesi toplantıdan üç gün sonra hazırlanmış ve yalnız fiziki senet getirenler listeye alınmıştır. 17.07.2026 itibarıyla doğru uygulama hangisidir?",
        "17.07.2026 itibarıyla kayden izlenen paylarda genel kurula katılabilecekler listesi ne zaman ve hangi kayıtla hazırlanır?",
        "Toplantıdan bir gün önce MKK kayıtlarına göre hazırlanır",
        ["Toplantıdan sonra fiziki senet matbaasının listesine göre hazırlanır", "Her on yılda bir borsa fiyatlarına göre hazırlanır", "Yalnız yönetim kurulu üyelerinin sözlü beyanına göre hazırlanır", "Genel kurul listesi kaydi paylarda hiçbir zaman düzenlenmez"],
        "Tebliğ m.20, genel kurula katılabilecekler listesinin toplantı tarihinden bir gün önce MKK tarafından kayden izlenen pay sahipliği kayıtlarına göre hazırlanmasını öngörür.",
        "Liste, toplantı öncesindeki kaydi hak sahipliği durumunu esas alır; fiziki senet ibrazı kaydileştirilmiş paylarda belirleyici değildir.",
        "Kaydileştirme Tebliği (II-13.1) m.20", "medium",
    ),
    r(
        "Yatırımcı, hesabındaki araçlara kendisi blokaj koyarak üyenin bu araçlar üzerinde talimatı dışında işlem yapmasını sınırlandırmak istemektedir. 17.07.2026 itibarıyla böyle bir imkân var mıdır?",
        "17.07.2026 itibarıyla yatırımcı blokajının temel işlevi nedir?",
        "Evet; yatırımcı üyenin tasarruf yetkisini sınırlandırabilir",
        ["Hayır; üye müşteri varlığı üzerinde sınırsız mülkiyet sahibidir", "Evet; blokaj payın mülkiyetini otomatik olarak MKK'ya geçirir", "Hayır; blokaj yalnız fiziki çekler için kullanılabilir", "Evet; blokaj aracın piyasa fiyatını Kurul adına sabitler"],
        "Tebliğ m.23, hesap sahibinin yatırımcı blokajı koyarak üyenin ilgili araçlar üzerindeki tasarrufunu sınırlamasına imkân verir.",
        "Blokaj mülkiyeti değiştirmez veya fiyatı belirlemez; yatırımcının iradesi dışında işlem yapılmasına karşı kaydi bir koruma sağlar.",
        "Kaydileştirme Tebliği (II-13.1) m.23", "easy",
    ),
]


PREMISES = [
    {
        "stem": "Kaydileştirme sistemi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kaydi ihraçta belge çıkarılmaması esastır\n\nII. Haklar elektronik ortamda izlenir\n\nIII. Hangi araçların kaydileştirileceğini Kurul belirler",
        "correct": "I, II ve III",
        "why": "Kaydi ihraçta fiziki belge çıkarılmaması esastır, haklar elektronik ortamda izlenir ve kaydileştirme kapsamını Kurul belirler.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.13/1", "difficulty": "easy",
    },
    {
        "stem": "MKK'nın hukuki konumu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Özel hukuk tüzel kişiliğini haiz anonim şirkettir\n\nII. Merkezi saklama kuruluşudur\n\nIII. MKK'nın güncel görevleri Kanunun 80'inci maddesinde düzenlenir",
        "correct": "I, II ve III",
        "why": "MKK özel hukuk tüzel kişiliğini haiz anonim şirket ve merkezi saklama kuruluşudur. Güncel 6362 sayılı Kanunda temel görevleri 80'inci maddede yer alır.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.79-80", "difficulty": "easy",
    },
    {
        "stem": "Kaydi kayıtların tutulması bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kayıtlar MKK'nın elektronik ortamında tutulur\n\nII. Kayıt işlemlerini MKK üyeleri yürütür\n\nIII. Üyenin yerel tablosu tek başına MKK kaydının yerini alır",
        "correct": "I ve II",
        "why": "Resmi kayıtlar MKK'nın oluşturduğu elektronik ortamda üyelerce tutulur. Üyenin MKK dışındaki yerel tablosu merkezi kaydın yerini almadığından III doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.13/3; Kaydileştirme Tebliği m.5", "difficulty": "medium",
    },
    {
        "stem": "Kaydi hakların hukuki etkisi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üçüncü kişilere karşı MKK'ya bildirim tarihi esas alınır\n\nII. Kayden izlenen paylara hiçbir zaman haciz konulamaz\n\nIII. Teslim edilen eski fiziki belge geçersiz olur",
        "correct": "I ve III",
        "why": "Üçüncü kişilere karşı MKK'ya bildirim tarihi esastır ve kaydileştirme için teslim edilen belge geçersizleşir. Kaydi pay haczedilebilir; işlem yetkili üyece yürütüldüğünden II doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.13/4-7", "difficulty": "medium",
    },
    {
        "stem": "Yatırımcı hesapları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hesap ilgili üyeye bağlı açılır\n\nII. Aynı kişiye her kurumda farklı sicil numarası verilir\n\nIII. Hak sahibinin kimliği MKK'ya bildirilir",
        "correct": "I ve III",
        "why": "Yatırımcı hesabı ilgili üyeye bağlı açılır ve hak sahibinin kimliği MKK'ya bildirilir. Aynı yatırımcı farklı kurumlardaki hesaplarında tek sicil numarasıyla izlendiğinden II doğru değildir.",
        "ref": "Kaydileştirme Tebliği (II-13.1) m.6 ve m.11; MKK Hesap İşlemleri Rehberi", "difficulty": "easy",
    },
    {
        "stem": "MKK hesap türleri bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatırımcı blokajı mülkiyeti otomatik olarak üyeye geçirir\n\nII. İhraççı havuzu yeni ihraçların geçici kaydında kullanılır\n\nIII. Bilinmeyen ortak hesabı kimliği tespit edilemeyen kayıtları izler",
        "correct": "II ve III",
        "why": "İhraççı havuzu geçici ihraç kaydını, bilinmeyen ortak hesabı kimliği henüz tespit edilemeyen kayıtları izler. Blokaj mülkiyeti üyeye geçirmediğinden I doğru değildir.",
        "ref": "Kaydileştirme Tebliği (II-13.1) m.7, m.13 ve m.23", "difficulty": "medium",
    },
    {
        "stem": "Kaydi sistemde mali ve ortaklık hakları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Temettü yalnız ihraççının eski fiziki listesine göre dağıtılır\n\nII. Genel kurul katılım listesi MKK kayıtlarıyla hazırlanır\n\nIII. Yanlış veya geç mali hak ödemesinden ihraççı sorumludur",
        "correct": "II ve III",
        "why": "Mali hak dağıtımı ve genel kurul katılım listesi MKK kayıtlarına dayanır; yanlış veya geç ödeme sonuçlarından ihraççı sorumludur. Bu nedenle I doğru değildir.",
        "ref": "Kaydileştirme Tebliği (II-13.1) m.18 ve m.20", "difficulty": "medium",
    },
    {
        "stem": "MKK ile üyelerinin görev ve sorumluluğu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. MKK üyelerinden görevleriyle ilgili bilgi isteyebilir\n\nII. Yanlış kayıttan doğan zararda kusur oranı esas alınır\n\nIII. MKK Kurulun gözetim ve denetimi dışındadır",
        "correct": "I ve II",
        "why": "MKK görevleri için üyelerinden bilgi isteyebilir ve yanlış kayıttan doğan zarar kusur oranında paylaşılır. MKK Kurulun gözetim ve denetiminde olduğundan III doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.80/3-5", "difficulty": "hard",
    },
]


if __name__ == "__main__":
    write_topic(
        lesson_id="sermaye_piyasasi_ve_finans",
        topic_id="kaydi_sistem",
        label="Kaydi Sistem ve MKK",
        slug="kaydi_sistem",
        prefix="topic-kys",
        seed=2026071739,
        legislation_version=(
            "6362 sayılı Sermaye Piyasası Kanunu m.13 ve m.79-80; "
            "Kaydileştirme Tebliği II-13.1 (Ağustos 2025 güncel metin); "
            "MKK hesap, ihraç ve yatırımcı hizmetleri rehberleri "
            "(17.07.2026 kontrolü)"
        ),
        rules=RULES,
        premises=PREMISES,
        wrong_banks={},
    )
