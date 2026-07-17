# -*- coding: utf-8 -*-
"""vergi_hukuku/kdv.json — şık boyu dengeleme (kör öğrenci %85 → hedef ≤%30).

SORUN: 51 öncüllü-olmayan sorunun 49'unda doğru şık EN UZUN. Aday soruyu
okumadan en uzunu işaretleyip %85 alıyor. Kaynak: doğru cevap yasal kesinlik
için niteleme taşırken ("Türkiye'de ticari, sınai, zirai faaliyet ve serbest
meslek faaliyeti çerçevesinde…"), yanlış iddia kısa söylenebiliyor.

ÇÖZÜM: Çeldiricileri İÇERİKLE uzat — dolguyla DEĞİL. Her uzatma, o çeldiricinin
temsil ettiği yanlış kavramın kendi içinde tutarlı bir açılımıdır: "KDV bir
gelir vergisidir" → "…; artan oranlı tarifeye göre yıllık beyanname ile ödenir"
(gelir vergisinin DOĞRU tarifi, KDV sorusuna YANLIŞ cevap). Bilmeyeni cezbeder,
bileni cezbetmez — yani soruyu zorlaştırır, sulandırmaz.

🔴 "…zorunda bulunmaktadır" gibi dolgu kalıbı KULLANILMAZ: muhasebe_standartları
dersini o bitirdi (ipucu boydan üsluba taşındı, kör öğrenci %52).

Hedef dağılım: doğru şık en-uzun ~%20, en-kısa ~%20. Bu yüzden bazı sorularda
TEK çeldirici doğruyu geçecek kadar, bazılarında DÖRDÜ birden geçecek kadar
uzatılır (doğru en kısa olsun diye). Yön çeşitliliği kasıtlı.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/kdv.json"

# qid → {harf: yeni tam metin}. Yalnız ÇELDİRİCİLER değişir; doğru şıkka,
# köke ve çözüme dokunulmaz.
YAMA = {
    # doğru A=135 → B ve C doğruyu geçsin, doğru ortaya insin
    "kdv-gen-0001": {
        "B": "KDV, kişilerin bir takvim yılı içinde elde ettikleri gelir üzerinden alınan dolaysız bir gelir vergisidir; artan oranlı tarifeye göre yıllık beyanname ile ödenir",
        "C": "KDV, yalnızca lüks sayılan belirli malların ithal ve tesliminde bir kez alınan özel bir tüketim vergisidir; genel tüketim üzerinden alınmaz",
    },
    # doğru C=170 → A ve E doğruyu geçsin
    "kdv-gen-0002": {
        "A": "Yalnızca ticari faaliyet çerçevesinde yapılan mal teslimleri verginin konusuna girer; hizmetler ile sınai, zirai ve serbest meslek faaliyetleri kapsam dışında kalır",
        "E": "Yalnızca serbest meslek faaliyeti çerçevesinde yapılan hizmetler verginin konusuna girer; mal teslimleri ile ticari, sınai ve zirai faaliyetler kapsam dışındadır",
    },
    # doğru C=126 → D doğruyu geçsin
    "kdv-gen-0003": {
        "D": "Bir malın mülkiyeti devredilmeksizin yalnızca zilyetliğinin geçici olarak karşı tarafa bırakılması; malın iade edilecek olması teslimi engellemez",
    },
    # doğru D=90 (kısa) → hepsini geçirmeye gerek yok, biri yetsin
    "kdv-gen-0004": {
        "A": "Bir malın işletme içinde bir üretim aşamasından diğerine aktarılması; aşamalar arası her aktarım ayrı bir teslim sayılır",
    },
    # doğru A=121 → B, C ve D doğruyu geçsin (doğru en kısaya insin)
    "kdv-gen-0005": {
        "B": "Yalnızca bir malın mülkiyetinin bedel karşılığında devredildiği işlemler; kiralama, onarım ve taahhüt işlemleri hizmet sayılmaz",
        "C": "Yalnızca serbest meslek erbabının verdiği ve bir belgeye bağlanan danışmanlık işlemleri; ticari nitelikteki onarım ve kiralama işlemleri kapsam dışıdır",
        "D": "Bir malın üretilip stoklara alınması hizmet sayılır; kiralama, onarım ve yapmamayı taahhüt etme işlemleri ise hizmet kapsamına girmez",
    },
    # doğru D=127 → A doğruyu geçsin
    "kdv-gen-0006": {
        "A": "İşlemin, mükellefin vatandaşı olduğu ülkede yapılmış olması gerekir; işlemin fiilen yapıldığı yer ile malın bulunduğu yer verginin konusu bakımından önem taşımaz",
    },
    # doğru B=109 → A ve C doğruyu geçsin
    "kdv-gen-0008": {
        "A": "KDV'nin mükellefi her hâlde vergiyi fiilen ödeyen nihai tüketicidir; teslim ve hizmeti yapanın beyan ve ödeme yükümlülüğü bulunmaz",
        "C": "KDV'de mükellef yalnızca ithalat yapanlardır; yurt içinde teslim ve hizmet yapanlar vergiyi hesaplasa da mükellef sıfatını taşımaz",
    },
    # doğru C=147 → B ve D doğruyu geçsin
    "kdv-gen-0009": {
        "B": "Bu durumda vergiyi, işlemi yapan yurt dışındaki mükellef kendi ülkesinde beyan ederek öder; Türkiye'deki muhatabın bir yükümlülüğü doğmaz",
        "D": "Bu hâllerde vergi, yalnızca işlemi yapanın Türkiye'ye gelip bizzat mükellefiyet tesis ettirmesi ve beyanname vermesiyle alınabilir; başka bir yol yoktur",
    },
    # doğru D=160 → A ve B doğruyu geçsin
    "kdv-gen-0010": {
        "A": "Yalnızca malın veya hizmetin bedelinin fiilen tahsil edildiği anda; teslim, ifa ve fatura anları vergiyi doğuran olay bakımından sonuç doğurmaz",
        "B": "Yalnızca ilgili vergilendirme döneminin sonunda; dönem içindeki teslim ve ifaların ayrı ayrı anı ile önceden düzenlenen faturalar dikkate alınmaz",
    },
    # doğru D=128 → E doğruyu geçsin
    "kdv-gen-0011": {
        "E": "Vergiyi doğuran olay, yalnızca abonenin bedeli fiilen ödediği anda gerçekleşir; dönemsel tahakkuk ve düzenlenen fatura tek başına yeterli sayılmaz",
    },
    # doğru C=136 → A ve E doğruyu geçsin
    "kdv-gen-0012": {
        "A": "İthal edilen malın Türkiye'de ilk kez satıldığı anda vergiyi doğuran olay gerçekleşir; gümrük beyannamesinin tescili bu bakımdan sonuç doğurmaz",
        "E": "İthalatta vergiyi doğuran olay, malın ithalatçının stoklarına girip kayda alındığı anda gerçekleşir; gümrük yükümlülüğünün başlaması dikkate alınmaz",
    },
    # doğru A=118 → B ve E doğruyu geçsin
    "kdv-gen-0013": {
        "B": "İhraç edilen mallar da tıpkı yurt içi teslimler gibi her hâlde KDV'ye tabidir; ihracata tanınmış bir istisna bulunmadığından yüklenilen vergi iade edilmez",
        "E": "İhracat istisnası yalnızca ithal edilip yeniden ihraç edilen mallar için geçerlidir; yerli üretim malların ihracı istisna kapsamına alınmamıştır",
    },

    # ── 2. tur: ilk turda uzattıklarım doğrunun ALTINDA kalmıştı (0002, 0010) ──
    "kdv-gen-0002-ek": {},   # yer tutucu değil; aşağıda gerçek qid ile ezilir
    "kdv-gen-0014": {
        "B": "Her türlü taşımacılık işlemi, yurt içi veya uluslararası ayrımı olmaksızın KDV'den istisnadır; taşımanın başlangıç ve bitiş noktası sonuç doğurmaz",
        "E": "Taşımacılık istisnası yalnızca yolcu taşımacılığında geçerlidir; yük ve eşya taşımacılığı, uluslararası olsa bile istisna kapsamı dışında tutulur",
    },
    "kdv-gen-0015": {
        "A": "BSMV kapsamına giren işlemler hem banka ve sigorta muameleleri vergisine hem de ayrıca KDV'ye tabi tutulur; aynı işlem iki dolaylı vergiyle birden vergilendirilir",
        "D": "Banka ve sigorta işlemleri BSMV'den istisna olup yalnızca KDV'ye tabidir; bu işlemlerde genel oran üzerinden vergi hesaplanır",
    },
    "kdv-gen-0016": {
        "A": "Tam istisnada da kısmi istisnada da işlemle ilgili yüklenilen KDV indirilir ve iade edilebilir; iki istisna türü arasında indirim bakımından bir fark bulunmaz",
        "B": "Tam istisnada yüklenilen KDV indirilemeyip gider veya maliyet yazılırken; kısmi istisnada yüklenilen KDV indirilebilir ve şartları varsa iade alınabilir",
    },
    "kdv-gen-0017": {
        "A": "İstisnadan vazgeçmek hiçbir hâlde mümkün değildir; istisna mükellefin iradesinden bağımsız olarak kanun gereği kendiliğinden uygulanır ve talep aranmaz",
        "B": "İstisnadan vazgeçen mükellef bu kararından hiçbir zaman geri dönemez; vazgeçme süresiz olduğundan mükellef ömür boyu vergiye tabi kalır",
    },
    "kdv-gen-0019": {
        "D": "İhraç kaydıyla teslim, ancak malın imalatçının kendisi tarafından bizzat ihraç edilmesi hâlinde söz konusu olur; aracı ihracatçıya yapılan teslimler kapsam dışıdır",
        "E": "İhraç kaydıyla teslimde imalatçı, teslime ait vergiyi hiçbir koşulda geri alamaz veya terkin ettiremez; tahsil edilen vergi kesin olarak hazineye kalır",
    },
    "kdv-gen-0020": {
        "A": "Matrah her hâlde malın veya hizmetin maliyet bedelidir; alıcıdan alınan veya borçlanılan bedelin matrahın tespitinde bir etkisi bulunmaz",
        "D": "Matrah, malın piyasadaki en yüksek satış fiyatıdır; taraflar arasında kararlaştırılan bedel bunun altında kalsa bile dikkate alınmaz",
    },
    "kdv-gen-0021": {
        "A": "Satıcının ticari teamüle uygun olarak yaptığı ve faturada ayrıca gösterdiği iskontolar; bu tutarlar bedelin bir parçası sayılarak matraha eklenir",
        "D": "Alıcının, malı kendi imkânlarıyla ve satıcıdan bağımsız olarak taşıması hâlinde katlandığı nakliye gideri; bu gider satıcının matrahına dâhil edilir",
    },
    "kdv-gen-0022": {
        "B": "Teslim edilen mal karşılığında alınan vade farkı, fiyat farkı ve faiz gelirleri; bunlar bedelin unsuru sayılmayıp matrah dışında tutulur",
    },
    "kdv-gen-0023": {
        "B": "Bu hâllerde matrah her zaman tarafların beyan ettiği düşük bedeldir; emsal bedel ya da emsal ücret gibi başka bir ölçüye başvurulmaz",
        "E": "Bu hâllerde matrah, mükellefin o yılki toplam cirosunun işlem sayısına bölünmesiyle bulunan ortalama tutardır; işlemin kendi niteliği aranmaz",
    },
    "kdv-gen-0026": {
        "A": "İşlemle ilgili hiçbir vergi, resim veya harç matraha dâhil edilmez; matrah yalnızca salt mal bedelinden oluşur ve yan yükümlülükler dışarıda kalır",
        "E": "Vergi, resim ve harçların matraha dâhil olup olmayacağını mükellef her işlemde serbestçe belirler; bu konuda bağlayıcı bir kural bulunmaz",
    },
    "kdv-gen-0027": {
        "B": "Mükellef yalnızca ithal ettiği mallara ilişkin KDV'yi indirebilir; yurt içi alışlarında yüklendiği vergi indirilemeyip doğrudan gider veya maliyet yazılır",
        "C": "Mükellef, yüklendiği KDV'yi doğrudan alıcılarından tahsil ederek karşılar; devletle bir indirim ilişkisi kurulmadığından beyannamede indirim satırı yer almaz",
    },
}
# 0002 ve 0010: ilk turda uzattığım çeldiriciler doğrunun ALTINDA kaldı (164/161 ↔ 170,
# 143/145 ↔ 160). Ölçüp görmesem fark etmeyecektim — bir çeldiriciyi doğrunun ÜSTÜNE çıkar.
YAMA.pop("kdv-gen-0002-ek")
YAMA["kdv-gen-0002"]["B"] = ("Yalnızca yurt dışından yapılan mal ithalatı verginin konusuna girer; "
                             "Türkiye'de yapılan teslim ve hizmetler, faaliyet hangi çerçevede "
                             "olursa olsun verginin konusu dışında kalır")
YAMA["kdv-gen-0010"]["C"] = ("Malın sipariş edildiği veya sözleşmenin imzalandığı anda; teslim, "
                             "ifa ve fatura anlarının vergiyi doğuran olay bakımından bir önemi "
                             "bulunmaz ve bunlar dikkate alınmaz")

# ── 3. tur: kalan 28 soru ────────────────────────────────────────────────────
# ★ Bunların 10'unda DÖRT çeldirici birden uzatılır → doğru şık EN KISA olur.
#   Hepsinde tek yönde çalışırsam "doğru hep en uzun" ipucunu "doğru hep ortada"
#   ipucuna çevirmiş olurum; dağılımın iki uca da yayılması gerekiyor.
YAMA.update({
    "kdv-gen-0020": {"C": "Matrah, mükellefin o dönemde elde ettiği toplam kârdır; tek tek işlemlerin bedeli değil, dönem sonucu esas alınarak vergi hesaplanır"},
    "kdv-gen-0021": {"B": "İşlem üzerinden hesaplanan katma değer vergisinin kendisi; verginin kendisi de bedelin bir unsuru sayılarak matraha eklenir ve üzerinden yeniden vergi alınır"},

    # ↓ doğru EN KISA olsun (dört çeldirici de uzatıldı)
    "kdv-gen-0028": {
        "B": "Aradaki fark, o dönem sonunda mükellefe hiçbir koşul aranmaksızın derhâl ve nakden iade edilir; sonraki döneme devir söz konusu olmaz",
        "C": "İndirilecek KDV'nin hesaplanan KDV'den fazla olması mümkün değildir; hesaplanan vergi her dönemde zorunlu olarak daha büyük çıkar",
        "D": "Aradaki fark mükellefin o dönemki ticari kârına eklenir ve gelir veya kurumlar vergisi matrahının bir unsuru olarak vergilendirilir",
        "E": "Fazla indirilecek KDV dönem sonunda iptal edilir; sonraki vergilendirme dönemlerine hiçbir biçimde aktarılamaz ve mükellef üzerinde kalır",
    },
    "kdv-gen-0029": {
        "A": "Mükellefin ticari faaliyeti kapsamında satmak üzere satın aldığı ticari mallara ilişkin yüklenilen KDV; bu vergi indirim konusu yapılamaz",
        "B": "İşletmede kullanılmak üzere alınan ve vergiye tabi faaliyetle doğrudan ilgili olan hammaddelere ilişkin yüklenilen KDV; bu vergi indirilemez",
        "D": "Vergiye tabi teslimlerde kullanılan makine ve teçhizat alımına ilişkin yüklenilen KDV; amortismana tabi olduğundan indirimi kabul edilmez",
        "E": "Mükellefin verdiği vergiye tabi hizmetlerle doğrudan ilgili olan alışlara ilişkin yüklenilen KDV; hizmet alışlarında indirim hakkı doğmaz",
    },
    "kdv-gen-0030": {"C": "Binek otomobil alışındaki KDV yalnızca aracın ikinci el olarak satışı yapıldığında geriye dönük olarak indirim konusu yapılabilir; alış döneminde indirilemez"},
    "kdv-gen-0031": {"A": "İndirim için herhangi bir belge aranmaz; mükellefin beyanı tek başına yeterli olup faturanın deftere kaydedilmesi de gerekmez"},
    "kdv-gen-0032": {"A": "Tam istisna kapsamındaki işlemler için yüklenilen KDV hiçbir biçimde indirilemez ve iade edilmez; bu vergi gider veya maliyet olarak yazılır"},
    "kdv-gen-0033": {"A": "Zayi olan mallara ait yüklenilen KDV, malların akıbetine ve zayi sebebine bakılmaksızın her hâlde indirilmeye devam edilir; düzeltme gerekmez"},

    # ↓ doğru EN KISA olsun
    "kdv-gen-0034": {
        "A": "Ödenecek KDV, mükellefin o dönemde yaptığı toplam satış tutarıdır; alışlarda yüklenilen indirilecek vergi bu tutardan düşülmez",
        "B": "Ödenecek KDV, indirilecek KDV'ye hesaplanan KDV'nin eklenmesiyle bulunur; iki tutarın toplamı dönemin vergi borcunu verir",
        "C": "Ödenecek KDV, mükellefin o dönemki ticari kârının kanunda belirlenen bir oranı olarak hesaplanır; teslim bedelleri dikkate alınmaz",
        "E": "Ödenecek KDV, yalnızca alışlarda yüklenilen KDV'nin toplamıdır; dönem içinde yapılan satışların vergi borcuna bir etkisi bulunmaz",
    },
    "kdv-gen-0037": {
        "A": "KDV, mükellefin beyanına gerek olmaksızın vergi dairesince resen ve maktu olarak tarh edilir; beyanname verme yükümlülüğü bulunmaz",
        "E": "KDV'yi mükellef değil, işleme taraf olan alıcı beyan eder ve öder; teslim veya hizmeti yapanın beyan yükümlülüğü doğmaz",
    },

    # ↓ doğru EN KISA olsun (hesap soruları)
    "kdv-gen-0042": {
        "A": "Ödenecek KDV, hesaplanan KDV ile indirilecek KDV'nin toplamı olan 16.000 TL'dir; iki tutar birbirinden düşülmez, toplanır",
        "B": "Mükellef bu dönemde 6.000 TL'lik indirimi nedeniyle vergi dairesinden 6.000 TL tutarında nakden iade almaya hak kazanır",
        "C": "Ödenecek KDV doğrudan hesaplanan KDV kadar olup 10.000 TL'dir; alışlarda yüklenilen 6.000 TL indirim olarak dikkate alınmaz",
        "D": "Ödenecek KDV, indirilecek KDV kadar olup 6.000 TL'dir; satışlar üzerinden hesaplanan 10.000 TL bu hesapta göz önüne alınmaz",
    },
    "kdv-gen-0043": {
        "B": "Mükellef aradaki 3.000 TL'lik farkı bu dönem sonunda hiçbir koşul aranmadan derhâl ve nakden iade alarak tahsil eder",
        # ⚠ Burada önce "…ödemek zorundadır" yazmıştım. "zorunda" doğal Türkçedir ve
        # tek başına dolgu değildir; ama dedektörün DOLGU kalıbına takılıyor. Kalıbı
        # dosyada hiç bulundurmamak sinyali temiz tutuyor — ucuz, o yüzden kaçınıldı.
        "C": "Mükellef bu dönem 3.000 TL tutarında KDV öder; indirilecek verginin fazla olması ödenecek tutarı azaltmaz, artırır",
        "D": "İndirilecek KDV'nin hesaplanan KDV'den fazla olması mümkün olmadığından kayıtlarda bir hata bulunduğu kabul edilir",
        "E": "Aradaki 3.000 TL'lik fark mükellefin ticari gelirine eklenir ve dönem kazancının bir unsuru olarak vergilendirilir",
    },
    "kdv-gen-0044": {"A": "Malın bedeli tahsil edilmediğinden bu işlem KDV'ye tabi değildir; teslim yalnızca bedel karşılığı yapılan devirlerde gerçekleşmiş sayılır"},
    "kdv-gen-0045": {"C": "İhracat KDV'den istisna olduğu için firma, ihracatla ilgili yüklendiği KDV'yi hiçbir biçimde indiremez veya iade alamaz; bu vergi maliyete eklenir ve üzerinde kalır"},

    # ↓ doğru EN KISA olsun
    "kdv-gen-0046": {
        "A": "Vade farkı bir finansman geliri niteliğinde olduğundan KDV matrahına dâhil edilmez; yalnızca peşin bedel vergiye tabi tutulur",
        "B": "Vade farkı yalnızca gelir vergisi matrahını ilgilendirir; katma değer vergisi matrahıyla hiçbir ilişkisi bulunmadığından dikkate alınmaz",
        "C": "Vade farkı matraha dâhil edilmez; vergi yalnızca malın peşin satış bedeli üzerinden hesaplanır ve vadeden doğan fark dışarıda kalır",
        "D": "Vade farkı üzerinden KDV, mal bedelinden ayrı olarak ve genel orana göre iki kat oranında hesaplanıp beyan edilir",
    },
    "kdv-gen-0047": {"A": "İskonto her hâlde matraha dâhildir; katma değer vergisi, iskonto düşülmeden önceki brüt bedel üzerinden hesaplanır ve faturada gösterilen indirim dikkate alınmaz"},
    "kdv-gen-0048": {"D": "İthalatta KDV yalnızca malı ithal eden tarafından değil, o malı sonradan yurt içinde satın alan kişi tarafından gümrük idaresine ödenir"},

    # ↓ doğru EN KISA olsun
    "kdv-gen-0049": {
        "A": "İşletme bu KDV'yi hiçbir sınır olmaksızın ve aracın kullanım amacına bakılmaksızın her hâlde indirim konusu yapabilir",
        "B": "İşletme bu KDV'yi aracın alış bedelinin iki katı değeri üzerinden hesaplayarak indirim konusu yapma hakkına sahiptir",
        "D": "Binek otomobil alışında katma değer vergisi hesaplanmadığından ortada indirilecek bir vergi ve indirim sorunu doğmaz",
        "E": "Bu KDV yalnızca araç ikinci el olarak satıldığında indirilebilir hâle gelir; alış döneminde indirim hakkı doğmaz",
    },
    "kdv-gen-0050": {"A": "KDV her aşamada malın toplam bedeli üzerinden yeniden alındığından zincir boyunca mükerrer vergileme oluşur; indirim mekanizması bu birikimi önlemez"},
    "kdv-gen-0051": {"A": "Hizmeti veren yurt dışındaki firma bu vergiyi kendi ülkesinde beyan edip ödeyeceğinden Türkiye'de KDV doğmaz; hizmetten yararlananın bir yükümlülüğü olmaz"},

    # ↓ doğru EN KISA olsun
    "kdv-gen-0052": {
        "A": "Taraflar bedeli serbestçe belirleyebildiğinden matrah her hâlde beyan edilen düşük bedeldir; emsal bedele başvurulmaz",
        "B": "Bu durumda işlem katma değer vergisinin konusundan tümüyle çıkar ve hiçbir matrah üzerinden vergilendirilmez",
        "C": "Matrah, malın gelecekte satılabileceği en yüksek fiyat olarak belirlenir; işlem tarihindeki emsal bedel aranmaz",
        "D": "Matrah, mükellefin toplam yıllık cirosunun teslim sayısına bölünmesiyle bulunan ortalama tutar olarak hesaplanır",
    },
    "kdv-gen-0053": {"A": "Fatura teslimden önce düzenlense bile vergiyi doğuran olay her hâlde malın fiilen teslim edildiği anda gerçekleşir; erken düzenlenen fatura vergiyi doğurmaz"},
    "kdv-gen-0054": {"B": "KDV nihai olarak malı ilk üreten imalatçının üzerinde kalır; sonraki aşamalardaki satıcılar indirim yoluyla vergiyi hiç yüklenmez"},
    "kdv-gen-0055": {"A": "Personele verilen mallar bir ücret unsuru olduğundan yalnızca gelir vergisi stopajına tabidir; teslim sayılmadığından KDV hesaplanmaz"},
    "kdv-gen-0056": {"D": "Hesaplanan KDV mükellefin dönem kârını, indirilecek KDV ise dönem zararını gösteren muhasebe kalemleridir; ikisinin farkı ticari sonucu verir"},
    "kdv-gen-0058": {"B": "KDV'de mükellef ile vergiyi fiilen yüklenen her zaman aynı kişidir; vergi hiçbir biçimde bir sonraki aşamaya yansıtılamaz"},
    "kdv-gen-0059": {"A": "İndirim hakkı süresizdir; mükellef yüklendiği KDV'yi vergiyi doğuran olayın üzerinden kaç yıl geçerse geçsin her zaman indirebilir"},

    # ↓ doğru EN KISA olsun
    "kdv-gen-0060": {
        "B": "Kişilerin birbirlerine yaptığı ve hiçbir ticari, sınai veya zirai faaliyetle ilişkisi bulunmayan karşılıksız bağışlar",
        "C": "Kamu kurumlarının vergi, resim ve harç tahsil etmesi gibi doğrudan kamu gücüne dayanarak yaptığı işlemler",
        "D": "Bir kişinin kendi konutunu bizzat kullanması gibi ortada hiçbir teslim veya hizmet bulunmayan kişisel fiiller",
        "E": "Yalnızca yurt dışında yapılan ve Türkiye ile hiçbir bağlantısı bulunmayan teslim ve hizmet işlemleri",
    },
})

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    idx = {q["id"]: q for q in qs}
    for qid, degisim in YAMA.items():
        q = idx[qid]
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            assert harf in q["options"], f"{qid}: {harf} yok"
            q["options"][harf] = yeni
        assert len(set(q["options"].values())) == 5, f"{qid}: şık çakışması"

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yamalanan soru: {len(YAMA)} | değişen çeldirici: "
          f"{sum(len(v) for v in YAMA.values())}")
