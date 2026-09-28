# -*- coding: utf-8 -*-
"""SPK Mevzuatı · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarının konu ağırlığını izler: ihraç ve halka açık ortaklık ~5, kamuyu aydınlatma ~3,
kolektif yatırım ~3, sermaye piyasası araçları ve kripto ~3, kaydi sistem ve YTM ~2, Kurul ve yatırım hizmetleri ~2,
piyasa suçları ve idari yaptırımlar ~2. Konu havuzundaki kökler tekrar edilmez; aynı hüküm farklı görevle ölçülür.
Dayanaklar konu builder'larıyla aynıdır (build_yk_*.py başlıklarına bkz.); 28.09.2026 kontrolü.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

SURUM = ("6362 s. Sermaye Piyasası Kanunu (2024 değişiklikleri dahil); II-5.1, II-5.2, II-15.1, II-23.2, II-23.3, "
         "III-37.1, III-52.1 Tebliğleri; 28.09.2026 kontrolü")

def paket(dosya, seed, ek):
    return Paket(dosya, lesson="sermaye_piyasasi_ve_finans", topic="spk_ve_duzenleme",
                 konu_adi="Sermaye Piyasası Mevzuatı", seed=seed, surum=SURUM, havuz="bolum", ek_idler=ek)

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"
IZ = "İzahname ve İhraç Belgesi Tebliği (II-5.1)’ne göre"
ST = "Sermaye Piyasası Araçlarının Satışı Tebliği (II-5.2)’ne göre"
ON = "Önemli Nitelikteki İşlemler ve Ayrılma Hakkı Tebliği (II-23.3)’ne göre"
BB = "Birleşme ve Bölünme Tebliği (II-23.2)’ne göre"
OD = "Özel Durumlar Tebliği (II-15.1)’ne göre"
YF = "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1)’ne göre"
YH = "Yatırım Hizmetleri ve Faaliyetleri ile Yan Hizmetlere İlişkin Esaslar Hakkında Tebliğ (III-37.1)’e göre"

IH, KA, KY, AR, KS, DZ, PS = ("ihrac_ve_halka_arz", "kamuyu_aydinlatma", "kolektif_yatirim", "sermaye_piyasasi_araclari",
                              "kaydi_sistem", "spk_ve_duzenleme", "piyasa_suclari")

# =============================================================================== TEST 1
T1 = paket("questions_sermaye_piyasasi_2026.json", 2026092831, ["demo-sermaye-021", "demo-sermaye-022"])

T1.sayisal("6362 s. SPKn m. 6/2",
    "Payları borsada işlem gören bir ortaklık, bedelli sermaye artırımı için Kurul düzenlemelerine uygun izahname ve gerekli "
    f"tüm belgeleri Kurula sunmuştur. {K}, bu onay başvurusu belgelerin sunulmasından itibaren kaç iş günü içinde karara bağlanır?",
    "10", ["5", "15", "20", "30"],
    "Kanun m. 6/2'ye göre izahname onay başvurusu, düzenlemelere uygun izahname ve gerekli belgelerin sunulmasından itibaren "
    "on iş günü içinde karara bağlanır; yirmi iş günlük süre sadece ilk halka arzlar içindir.", topic=IH, zorluk="easy")

T1.q("6362 s. SPKn m. 10",
    "Bir halka arzın izahnamesine eklenen gayrimenkul değerleme raporunda bir taşınmazın değeri gerçeğe aykırı biçimde yüksek "
    f"gösterilmiş ve yatırımcılar zarara uğramıştır. {K}, bu zarardan sorumluluğa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Değerleme kuruluşu izahnamenin tamamından ihraççıyla birlikte kusursuz sorumludur.",
    ["Değerleme kuruluşu raporundaki yanlış ve yanıltıcı bilgilerden Kanun çerçevesinde sorumludur.",
     "İzahnamedeki yanlış bilgilerden doğan zarardan öncelikle ihraççı sorumludur.",
     "Zarar ihraççıdan tazmin edilemezse lider aracı kurum kusuruna göre sorumlu olabilir.",
     "Bağımsız denetim ve derecelendirme kuruluşları da raporlarıyla sınırlı olarak sorumludur."],
    "Kanun m. 10/1'e göre izahnamedeki yanlış bilgilerden ihraççı sorumludur; tazmin edilemeyen zarardan halka arz eden, lider "
    "aracı kurum, garantör ve yönetim kurulu üyeleri kusurlarına göre sorumludur. m. 10/2'ye göre değerleme, denetim ve "
    "derecelendirme kuruluşları sadece hazırladıkları raporlardaki bilgilerden sorumludur.", topic=IH)

T1.q("II-23.3 m. 10/3",
    "Halka açık bir ortaklığın genel kurulunda, hâkim ortak olan gerçek kişiye ait şirketten bir fabrikanın satın alınması "
    f"(önemli nitelikteki işlem) görüşülmektedir. {ON}, bu oylamaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birleşme ve tür değiştirme işlemleri de kişisel nitelikte sonuç doğuran işlemler olarak kabul edilir.",
    ["İşlem hâkim ortak için kişisel sonuç doğuruyorsa hâkim ortak ve kontrolündeki şirketler oy kullanamaz.",
     "Karar için esas sözleşmede daha ağır nisap yoksa katılanların üçte ikisinin olumlu oyu aranır.",
     "Sermayenin en az yarısı hazırsa katılanların çoğunluğuyla karar alınabilir.",
     "Tebliğdeki nisapları hafifleten esas sözleşme hükümleri geçersizdir."],
    "Tebliğ m. 10'a göre TTK m. 436/1 kapsamında işleme taraf olan nihai kontrol eden gerçek kişi pay sahipleri ve kontrolündeki "
    "şirketler, işlem kendileri için kişisel sonuç doğuruyorsa oy kullanamaz; ancak m. 4'teki birleşme, bölünme ve tür "
    "değiştirmenin kişisel sonuç doğurmadığı kabul edilir. Nisap üçte iki, yarısı hazırsa çoğunluktur.", topic=IH, zorluk="hard")

T1.sayisal("II-5.2 m. 10/10",
    "Halka açık bir ortaklığın bedelli sermaye artırımında yeni pay alma hakkı kullanım süresi sona ermiş ve kullanılmayan "
    f"paylar kalmıştır. {ST}, kalan payların satışına yeni pay alma haklarının kullanımının bitiminden itibaren en geç kaç iş "
    "günü içinde başlanır?",
    "10", ["2", "5", "15", "30"],
    "Tebliğ m. 10/10'a göre halka açık ortaklıkların sermaye artırımlarında yeni pay alma hakkının kullanımından sonra kalan "
    "payların satışına, yeni pay alma haklarının kullanımının bitiminden itibaren on iş günü içinde başlanır.", topic=IH)

T1.q("II-23.2 m. 4",
    "Halka açık bir holding şirketi, tüm malvarlığını mevcut iki şirkete devretmiş, sona ermiş ve ortakları bu iki şirketin "
    f"ortağı olmuştur. {BB}, bu işlem aşağıdakilerden hangisidir?",
    "Tam bölünme",
    ["İştirak modeliyle kısmi bölünme", "Ortaklara pay devri modeliyle kısmi bölünme",
     "Devralma şeklinde birleşme", "Yeni kuruluş şeklinde birleşme"],
    "Tebliğ m. 4'e göre tam bölünme, bölünen şirketin malvarlığının tümünün mevcut veya yeni kurulacak en az iki şirkete "
    "geçmesi, bölünen şirketin sona ermesi ve ortaklarının devralan şirketlerin ortağı olmasıdır; kısmi bölünmede bölünen "
    "şirket varlığını sürdürür.", topic=IH, zorluk="easy")

T1.q("II-15.1 m. 6/4-5",
    "Bir ihraççının yönetim kurulu, süren bir satın alma müzakeresine ilişkin içsel bilginin açıklanmasını ertelemeyi "
    f"görüşmektedir. {OD}, ertelemenin usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Erteleme kararı ihraççının genel kurulunca alınır.",
    ["Ertelemenin meşru çıkarlara etkisi ve gizlilik tedbirleri yönetim kurulu kararına bağlanır.",
     "Yönetim kurulu yetki vermişse yetkilendirilen kişinin yazılı onayı alınır.",
     "İhraççının bilgisi dışında bilgiyi öğrenen %10 pay sahipleri de erteleme hakkından yararlanabilir.",
     "Pay sahibinin ertelemesinde ihraççıya bildirim yapılır ve aynı karar usulü uygulanır."],
    "Tebliğ m. 6/4'e göre ertelemenin meşru çıkarlara etkisi, yatırımcıları yanıltma riski taşımadığı ve gizlilik tedbirleri "
    "yönetim kurulu kararına veya yetkilendirilen kişinin yazılı onayına bağlanır. m. 6/5'e göre m. 5/2'deki pay sahipleri de "
    "erteleme hakkından yararlanır ve ihraççıya bildirim üzerine aynı usul uygulanır.", topic=KA, zorluk="hard")

T1.oncul("6362 s. SPKn m. 32/1",
    "Halka açık bir ortaklıkla ilgili aşağıdaki belgeler verilmiştir:",
    ["Pay alım teklifinde hazırlanan bilgi formu",
     "Birleşme işleminde hazırlanan duyuru metni",
     "Borsada işlem görme duyurusu",
     "Ortaklığın internet sitesinde yayımladığı ürün tanıtım broşürü"],
    f"{K}, yukarıdakilerden hangileri imzalayanlarının yanlış veya eksik bilgilerden müteselsilen sorumlu olduğu kamuyu "
    "aydınlatma belgeleri arasındadır?",
    "I, II ve III", ["I ve II", "II ve IV", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 32/1'e göre izahname, pay alım tekliflerinde hazırlanan bilgi formu, özel durum açıklaması, birleşme ve "
    "bölünme duyuru metinleri, borsada işlem görme duyurusu ve finansal raporlar gibi Kurulca öngörülen kamuyu aydınlatma "
    "belgelerini imzalayanlar müteselsilen sorumludur. Ürün broşürü bu nitelikte değildir.", topic=KA)

T1.q("6362 s. SPKn m. 29/6",
    f"{K}, halka açık ortaklıklarda yeni pay alma haklarının kısıtlanması ve sermaye azaltımı kararlarına ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Esas sözleşmeyle bu kararlar için Kanundakinden daha hafif nisaplar öngörülebilir.",
    ["Bu kararlar için toplantı nisabı aranmaz.",
     "Katılan oy hakkını haiz payların üçte ikisinin olumlu oyu aranır.",
     "Sermayenin en az yarısı hazırsa katılanların çoğunluğuyla karar alınır.",
     "Önemli nitelikteki işleme TTK m. 436/1 uyarınca taraf olan ortaklar oy kullanamaz."],
    "Kanun m. 29/6'ya göre bu kararlarda toplantı nisabı aranmaz, katılanların üçte ikisi gerekir; sermayenin yarısı hazırsa "
    "çoğunluk yeterlidir ve önemli nitelikteki işlemlerde taraf ortaklar oy kullanamaz. Nisapları hafifleten esas sözleşme "
    "hükümleri geçersizdir; sadece daha ağır nisap öngörülebilir.", topic=KA)

T1.q("6362 s. SPKn m. 52/3",
    "Bir portföy yönetim şirketi, yönettiği yatırım fonu adına bir borsada pay satın almakta ve bu paylardan doğan oy haklarını "
    f"kullanmaktadır. {K}, şirketin bu işlemlerdeki hukuki konumu aşağıdakilerden hangisidir?",
    "Fona ait varlıklar üzerinde kendi adına ve fon hesabına tasarrufta bulunur.",
    ["Katılma payı sahiplerinin adına ve hesabına vekil olarak tasarrufta bulunur.",
     "Fonun tüzel kişiliğini temsil eden organ sıfatıyla işlem yapar.",
     "Portföy saklayıcısının talimatıyla ve onun adına tasarrufta bulunur.",
     "Kendi adına ve kendi hesabına işlem yapıp kazancı fona aktarır."],
    "Kanun m. 52/3'e göre portföy yönetim şirketi fonu katılma payı sahiplerinin haklarını koruyacak şekilde temsil eder ve "
    "yönetir; fona ait varlıklar üzerinde kendi adına ve fon hesabına mevzuat ve iç tüzüğe uygun olarak tasarrufta bulunmaya "
    "ve bundan doğan hakları kullanmaya yetkilidir. Yatırım fonunun tüzel kişiliği yoktur.", topic=KY)

T1.sayisal("III-52.1 m. 17/1-d",
    "Bir borçlanma araçları fonu, portföyünün önemli bir kısmını Hazine ve Maliye Bakanlığının ihraç ettiği devlet tahvillerine "
    f"yatırmaktadır. {YF}, bu kapsamda tek bir varlığa yapılan yatırım fon toplam değerinin en fazla yüzde kaçı olabilir?",
    "%35", ["%10", "%20", "%25", "%50"],
    "Tebliğ m. 17/1-d'ye göre TCMB, Hazine ve Maliye Bakanlığı, ipotek finansmanı kuruluşları ve Türkiye Varlık Fonunun ihraç "
    "ettiği araçlar için tek ihraççı ve toplam sınırlamaları uygulanmaz; ancak bu kapsamda tek bir varlığa yapılan yatırım fon "
    "toplam değerinin %35'ini aşamaz.", topic=KY, zorluk="hard")

T1.q("6362 s. SPKn m. 50/5",
    "Sabit sermayeli bir menkul kıymet yatırım ortaklığı, değişken sermayeli yatırım ortaklığına dönüşmek istemektedir. "
    f"{K}, bu dönüşüme ilişkin aşağıdakilerden hangisi doğrudur?",
    "Dönüşüm mümkündür; prosedür, nisaplar ve pay alım teklifi esaslarını Kurul belirler.",
    ["Yatırım ortaklıkları değişken sermayeli yatırım ortaklığına dönüşemez.",
     "Dönüşüm için tüm pay sahiplerinin oybirliği ve mahkeme onayı gerekir.",
     "Dönüşüm yönetim kurulu kararıyla gerçekleşir, genel kurul kararı aranmaz.",
     "Dönüşüm hâlinde ortaklık önce tasfiye edilir, sonra yeniden kurulur."],
    "Kanun m. 50/5'e göre yatırım ortaklıkları değişken sermayeli yatırım ortaklıklarına dönüşebilir; dönüşüm prosedürü, genel "
    "kurul toplantı ve karar nisapları, ortaklara pay alım teklifi ve teklif fiyatı ile ortakların hak ve yükümlülüklerinin "
    "korunmasına ilişkin esasları Kurul belirler.", topic=KY)

T1.q("6362 s. SPKn m. 61/2-3",
    f"{K}, varlık kiralama şirketlerinin faaliyet sınırlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Esas sözleşmede izin olmasa da portföydeki varlıklar üçüncü kişiler lehine ipotek edilebilir.",
    ["Varlık kiralama şirketleri münhasıran kira sertifikası ihraç etmek üzere kurulur.",
     "Esas sözleşmede belirtilen faaliyetler dışında ticari faaliyette bulunamazlar.",
     "Varlıkları sertifika sahiplerinin menfaatine aykırı şekilde kiralayamaz veya devredemezler.",
     "Esas sözleşmelerine Kurul tarafından uygun görüş verilir."],
    "Kanun m. 61'e göre varlık kiralama şirketleri münhasıran kira sertifikası ihracı için kurulan anonim ortaklıklardır; Kurulun "
    "uygun görüş verdiği esas sözleşmedeki faaliyetler dışında ticari faaliyette bulunamaz, esas sözleşmede izin verilenler "
    "hariç varlıklar üzerinde üçüncü kişiler lehine ayni hak tesis edemez ve sertifika sahiplerinin menfaatine aykırı "
    "kiralama veya devir yapamaz.", topic=AR)

T1.q("6362 s. SPKn m. 35/B-3-c",
    "Bir kripto varlık platformunun esas sözleşmesine göre yönetim kurulu üyelerinin çoğunluğunu seçme hakkı bir gerçek kişiye "
    f"aittir; bu kişinin ortaklıktaki pay oranı %8’dir. {K}, bu kişiye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ortaklar için Kanunda aranan şartları taşıması zorunludur.",
    ["Pay oranı %10’un altında olduğu için herhangi bir şart aranmaz.",
     "Sadece mali güç şartını taşıması yeterlidir.",
     "Şartlar sadece tüzel kişi ortaklar için aranır.",
     "Şartları taşıması Kurulun takdirine bağlıdır."],
    "Kanun m. 35/B-3-c'ye göre dağıtılabilir kârın yarısından fazlasını alma hakkına veya yönetim kurulunda üye sayısının "
    "yarısından fazlasını seçme ya da aday gösterme hakkına sahip gerçek kişilerin, pay oranlarına bakılmaksızın, ortaklar "
    "için (a) bendinde aranan şartları taşıması zorunludur.", topic=AR, zorluk="hard")

T1.q("6362 s. SPKn m. 31/B-3",
    "Tahvil ihracında atanan teminat yöneticisi, teminat olarak gösterilen bir gemi üzerindeki ipoteğin gemi siciline tescilini "
    f"yaptırmak istemektedir. {K}, teminat yöneticisinin bu işlemi yapma yetkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tescil işlemlerini kendi adına ve yatırımcılar hesabına yapmaya yetkilidir.",
    ["Tescil işlemleri sadece ihraççı tarafından kendi adına yapılabilir.",
     "Tescil için her yatırımcıdan ayrı vekâletname alınması gerekir.",
     "Tescil işlemi Kurul adına ve Kurulun talimatıyla yapılır.",
     "Teminat yöneticisi sadece tapu sicilinde işlem yapabilir, diğer sicillerde yetkisi yoktur."],
    "Kanun m. 31/B-3'e göre teminat yöneticisi; tapu, gemi sicili, araç sicili ve taşınır rehin sicili dahil özel sicillerdeki "
    "rehin, ipotek ve ayni hakların tescili, terkini ve sona erdirilmesine ilişkin tüm iş ve muameleleri kendi adına ve "
    "yatırımcılar hesabına yerine getirmeye yetkilidir.", topic=AR)

T1.q("6362 s. SPKn m. 84/1-2",
    f"{K}, yatırımcıların tazmininin kapsamına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırım danışmanlığı nedeniyle uğranılan zararlar tazmin kapsamındadır.",
    ["Tazmin kapsamını, yatırım kuruluşunca saklanan nakit ve araçların teslim edilmemesinden doğan talepler oluşturur.",
     "Yatırım kuruluşunca yönetilen varlıkların teslim edilmemesinden doğan talepler de kapsamdadır.",
     "Piyasadaki fiyat hareketlerinden kaynaklanan zararlar tazmin kapsamında değildir.",
     "Tazmin kararı verilen kuruluşun yatırımcıları tazmin talep etme hakkına sahiptir."],
    "Kanun m. 84/1'e göre tazmin kapsamını, yatırım hizmetleri veya yan hizmetlerle bağlantılı olarak yatırımcı adına saklanan "
    "veya yönetilen nakit ve araçların teslim yükümlülüğünün yerine getirilmemesinden doğan talepler oluşturur; m. 84/2'ye göre "
    "yatırım danışmanlığı veya fiyat hareketlerinden kaynaklanan zararlar tazmin kapsamında değildir.", topic=KS)

T1.oncul("6362 s. SPKn m. 78/2",
    "Merkezî karşı taraf hizmeti veren bir takas kuruluşunun temerrüt yönetiminde kullanabileceği araçlara ilişkin aşağıdaki "
    "ifadeler verilmiştir:",
    ["Pozisyonlar ancak temerrüde düşen üyenin yazılı onayıyla kapatılabilir.",
     "Temerrüde düşen üyenin teminatları kullanılabilir.",
     "Garanti fonu ve takas kuruluşunun kendi sermayesi kullanılabilir.",
     "Müşterilerin pozisyonları temerrüde düşen üyenin rızası aranmaksızın diğer üyelere taşınabilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "II, III ve IV", ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 78/2'ye göre takas kuruluşları temerrüt yönetiminde üyelerin teminatlarını, garanti fonunu ve kendi sermayelerini, "
    "sigorta sözleşmelerini kullanabilir; müşterilerin pozisyon ve teminatlarını temerrüde düşen üyenin rızası aranmaksızın "
    "diğer üyelere taşıyabilir ve pozisyonları resen kapatabilir.", topic=KS, zorluk="hard")

T1.q("6362 s. SPKn m. 122, 124",
    f"{K}, Kurul Karar Organı ile Kurul Başkanının görevlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurul personelinin tamamını atama yetkisi münhasıran Kurul Karar Organına aittir.",
    ["Karar Organı, Başkanın önerisi üzerine başkan yardımcıları ve daire başkanlarını atar.",
     "Karar Organı Kurulun bütçesini ve yıllık faaliyet raporunu karara bağlar.",
     "Başkan, Karar Organı toplantılarının gündemini, gün ve saatini belirler.",
     "Başkan, Kurul adına basın ve yayın organlarına beyan ve açıklamada bulunur."],
    "Kanun m. 122'ye göre Karar Organı düzenleyici işlemleri, bütçe ve faaliyet raporunu karara bağlar ve Başkanın önerisiyle "
    "başkan yardımcıları ile daire başkanlarını atar. m. 124'e göre Başkan gündemi belirler, Kurulu temsil eder ve Karar "
    "Organınca atanması öngörülenler dışındaki personeli atar.", topic=DZ, zorluk="hard")

T1.q("III-37.1 m. 5/3",
    "Bir aracı kurum, hiçbir müşteriye hizmet sunma amacı olmaksızın kendi portföyü için başka bir yatırım kuruluşu aracılığıyla "
    f"pay alım satımı yapmaktadır. {YH}, bu işlemlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Müşteri dışı taraflarla kendi portföyü için yapılan bu işlemler Kurul iznine tabi değildir.",
    ["Bu işlemler portföy aracılığı faaliyeti sayılır ve ayrı izin gerektirir.",
     "Aracı kurumların kendi portföyleri için işlem yapması yasaktır.",
     "Bu işlemler sadece geniş yetkili aracı kurumlarca yapılabilir.",
     "Her işlem için Kurula önceden bildirim yapılması gerekir."],
    "Tebliğ m. 5/3'e göre yatırım kuruluşlarının müşterileri dışındaki taraflarla, herhangi bir yatırım hizmeti sunma amacı "
    "olmaksızın kendi portföyleri için sermaye piyasası araçlarına ilişkin işlem yapmaları Kurul iznine tabi değildir.",
    topic=DZ)

T1.q("6362 s. SPKn m. 107/2",
    "Bir aracı kurumun analisti, bir ortaklığın paylarını önceden satın aldıktan sonra, fiyatı yükseltmek amacıyla gerçeğe aykırı "
    f"verilere dayanan olumlu bir araştırma raporu hazırlayıp yaymış ve paylarını satarak kazanç sağlamıştır. {K}, bu fiil "
    "aşağıdakilerden hangisini oluşturur?",
    "Bilgi bazlı piyasa dolandırıcılığı",
    ["Bilgi suistimali", "Piyasa bozucu eylem", "Güveni kötüye kullanmanın nitelikli hâli",
     "İzinsiz yatırım danışmanlığı"],
    "Kanun m. 107/2'ye göre araçların fiyatını veya yatırımcı kararlarını etkilemek amacıyla yalan, yanlış veya yanıltıcı bilgi "
    "veren, rapor hazırlayan veya bunları yayan ve bu suretle menfaat sağlayanlar üç yıldan beş yıla kadar hapis ve beş bin "
    "güne kadar adli para cezası ile cezalandırılır.", topic=PS, zorluk="easy")

T1.sayisal("6362 s. SPKn m. 105/2",
    "Bir yatırımcının, hakkında idari yaptırım kararı verilinceye kadar aynı kabahati birden çok kez işlediği ve bu yolla 1 "
    f"milyon TL menfaat temin ettiği tespit edilmiştir. {K}, verilecek idari para cezası en az kaç TL olmalıdır?",
    "3.000.000", ["1.000.000", "2.000.000", "4.000.000", "6.000.000"],
    "Kanun m. 105/2'ye göre kabahatin idari yaptırım kararından önce birden çok işlenmesi hâlinde tek ceza verilir ve iki kat "
    "artırılır; bu suretle menfaat temin edilmişse ceza menfaatin üç katından az olamaz: 1.000.000 × 3 = 3.000.000 TL.",
    topic=PS, zorluk="hard")

# =============================================================================== TEST 2
T2 = paket("questions_sermaye_piyasasi_test2_2026.json", 2026092832, ["spk-t2-0020"])

T2.q("6362 s. SPKn m. 4/5",
    "Bir ortaklığın büyük pay sahibi, sahip olduğu payları halka arz etmek üzere Kurula başvurmuştur; ortaklık ise izahname "
    f"için gerekli finansal bilgileri vermekte isteksiz davranmaktadır. {K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "İhraççının izahname hazırlanmasında kolaylaştırıcı tedbirleri alması zorunludur.",
    ["İhraççı bilgi vermeye zorlanamaz; halka arz eden izahnameyi kendi bilgileriyle hazırlar.",
     "Halka arz eden, ancak ihraççının genel kurul onayıyla izahname hazırlayabilir.",
     "Bu durumda izahname yerine ihraç belgesi hazırlanır.",
     "Kurul, ihraççıya bilgi verme yükümlülüğünü ancak mahkeme kararıyla getirebilir."],
    "Kanun m. 4/5'e göre halka arz eden tarafından izahnamenin düzenlenmesi sırasında ihraççının izahname hazırlanmasında "
    "kolaylaştırıcı tedbirleri alması zorunludur.", topic=IH)

T2.sayisal("II-5.1 m. 6/5",
    "Payları borsada işlem gören bir ortaklığın borsada işlem görmeyen nitelikteki payları borsada işlem gören niteliğe "
    f"dönüştürülerek halka arz edilecektir. {IZ}, halka arz edilen bu payların aynı gruptaki mevcut borsada işlem gören "
    "paylara oranı on iki aylık süre içinde yüzde kaçın altında kalırsa halka arz edenler izahname hazırlamaktan muaftır?",
    "%10", ["%1", "%5", "%20", "%25"],
    "Tebliğ m. 6/5'e göre dönüştürülen payların halka arzında, bu payların nominal değerinin borsada işlem gören aynı grup "
    "mevcut payların toplam nominal değerine oranı yüzde ondan düşükse halka arz edenler izahname hazırlama yükümlülüğünden "
    "muaftır; oran on iki aylık süredeki tüm satışlar dikkate alınarak hesaplanır.", topic=IH, zorluk="hard")

T2.q("II-5.1 m. 7/4",
    f"{IZ}, izahnamenin imzalanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Konsorsiyum oluşturulmuşsa izahnameyi konsorsiyumdaki tüm aracı kurumlar imzalar.",
    ["İzahname ihraççı tarafından imzalanır.",
     "Varsa halka arz eden de izahnameyi imzalar.",
     "Satışa aracılık eden yetkili kuruluş izahnameyi imzalar.",
     "Yetkili kuruluş değişirse izahname yeni yetkili kuruluşça imzalanıp önceki gibi ilan edilir."],
    "Tebliğ m. 7/4'e göre izahnameyi ihraççı, varsa halka arz eden ve yetkili kuruluş imzalar; konsorsiyum varsa konsorsiyum "
    "lideri ve varsa eş liderler imzalar. Geçerlilik süresinde yetkili kuruluş değişirse izahname yeni kuruluşça imzalanıp "
    "önceki gibi ilan edilir ve nerede yayımlandığı tescil edilir.", topic=IH)

T2.q("II-5.2 m. 23/4",
    "Talep toplama yoluyla yapılan bir halka arzda yatırımcıların taleplerinin bir kısmı karşılanamamıştır. "
    f"{ST}, karşılanamayan taleplere ilişkin bedel iadelerinin zamanlaması aşağıdakilerden hangisidir?",
    "Dağıtım listesinin teslim alınmasını izleyen iş günü",
    ["Talep toplama süresinin bitimini izleyen iş günü",
     "Payların borsada işlem görmeye başladığı gün",
     "Dağıtım listesinin onaylanmasından itibaren on iş günü içinde",
     "İzahnamenin nerede yayımlandığının tescilinden sonra"],
    "Tebliğ m. 23/4'e göre karşılanamayan taleplere ilişkin bedel iadeleri, onaylanan dağıtım listesinin yetkili kuruluş "
    "tarafından teslim alınmasını izleyen iş günü içinde yerine getirilir; konsorsiyumda lider aynı gün üyelere bildirimde bulunur.",
    topic=IH)

T2.q("II-23.3 m. 8/3",
    "Halka açık bir ortaklığın yönetim kurulu, önemli nitelikteki bir işlem nedeniyle çok sayıda pay sahibinin ayrılma hakkı "
    f"kullanmasından ve ortaklığın yüksek maliyete katlanmasından endişe etmektedir. {ON}, yönetim kurulunun bu riske karşı "
    "alabileceği önlem aşağıdakilerden hangisidir?",
    "Maliyet sınırı aşılırsa işlemden vazgeçmeyi genel kurul onayına sunmak",
    ["Ayrılma hakkı kullanım fiyatını genel kurul kararıyla borsa fiyatının altında belirlemek",
     "Ayrılma hakkını sadece belirli oranın üzerinde pay sahibi olanlara tanımak",
     "Ayrılma hakkının kullanım süresini tek iş gününe indirmek",
     "Ayrılma hakkını kullananlara payların bedelini iki yıl içinde taksitle ödemek"],
    "Tebliğ m. 8/3'e göre yönetim kurulu, gündemin ilanından önce, ayrılma hakkı kullanımlarının maliyetinin belirlenen tutarı "
    "aşması veya belirli oranda ya da nitelikteki ortakların olumsuz oy kullanması hâlinde işlemden vazgeçilmesinin genel "
    "kurul onayına sunulmasını kararlaştırabilir. Bedel m. 14'e göre tam ve nakden ödenir.", topic=IH, zorluk="hard")

T2.sayisal("II-15.1 m. 24/5",
    "Sermaye piyasası araçları borsada işlem görmeyen bir ihraççının kendine ait bir internet sitesi bulunmaktadır. "
    f"{OD}, bu ihraççı özel durum açıklamalarını, açıklamayı izleyen en geç kaç iş günü içinde internet sitesinde ilan etmelidir?",
    "5", ["1", "2", "10", "15"],
    "Tebliğ m. 24/5'e göre borsada işlem görmeyen ihraççılar, internet siteleri varsa özel durum açıklamalarını en geç kamuya "
    "açıklamayı izleyen beş iş günü içinde sitelerinde ilan eder ve beş yıl süreyle bulundurur; borsada işlem gören ihraççılarda "
    "süre izleyen iş günüdür.", topic=KA, zorluk="hard")

T2.q("6362 s. SPKn m. 17/1",
    f"{K}, Kurulun halka açık ortaklıklarda kurumsal yönetim ilkelerine ilişkin yetkisini kullanırken gözeteceği ilke "
    "aşağıdakilerden hangisidir?",
    "Haksız rekabete yol açmamak ve eşit koşullara eşit kural uygulamak",
    ["Tüm halka açık ortaklıklara aynı ilkeleri istisnasız uygulamak",
     "Sadece bankacılık ve sigortacılık sektörüne ilkeleri zorunlu tutmak",
     "İlkelerin uygulanmasını ortaklıkların genel kurul kararına bırakmak",
     "Kurumsal yönetim derecelendirmesi yüksek şirketleri ilkelerden muaf tutmak"],
    "Kanun m. 17/1'e göre Kurul kurumsal yönetim ilkelerine, uyum raporlarına, derecelendirmeye ve bağımsız üyeliklere ilişkin "
    "esasları belirler; bu yetkilerini halka açık şirketler arasında haksız rekabet ile sonuçlanmayacak şekilde ve eşit "
    "koşullardaki şirketlere eşit kuralların uygulanması prensibini gözeterek kullanır.", topic=KA)

T2.oncul("6362 s. SPKn m. 21",
    "Halka açık bir ortaklığın ilişkili taraflarıyla yaptığı aşağıdaki işlemler incelenmektedir:",
    ["Ana ortağın şirketiyle kârı azaltacak şekilde yapay işlem hacmi üretilmesi",
     "İlişkili bir şirkete emsallerine uygun faizle borç verilmesi",
     "Kazanılması beklenen bir ihaleye katılmayarak işin ilişkili şirkete bırakılması",
     "İlişkili bir şirkete emsallerinin açıkça üzerinde kira ödenmesi"],
    f"{K}, yukarıdaki işlemlerden hangileri örtülü kazanç aktarımı oluşturur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 21/1'e göre ilişkili kişilerle emsallere ve piyasa teamüllerine aykırı fiyat veya şartlar içeren işlemler ve işlem "
    "hacmi üretmek gibi yollarla kârın azaltılması, m. 21/2'ye göre basiretli tacirden beklenen faaliyetin yapılmayarak ilişkili "
    "kişinin kazancının artırılması örtülü kazanç aktarımıdır. Emsallere uygun işlemler yasak kapsamında değildir.", topic=KA)

T2.q("III-52.1 m. 15/2",
    f"{YF}, katılma paylarının alım satımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurucunun kendi fonlarına yatırımda giriş-çıkış komisyonu ödenir.",
    ["Katılma paylarının günlük olarak alım satımı esastır.",
     "İzahnamede şartları belirlenmek kaydıyla giriş ve çıkış komisyonu uygulanabilir.",
     "Kurul fon türüne göre günlük alım satıma istisna getirebilir.",
     "Kurucu, fonun katılma paylarını kendi portföyüne dahil edebilir."],
    "Tebliğ m. 15/2'ye göre katılma paylarının günlük alım satımı esastır, Kurul istisna getirebilir ve izahnamede belirlenen "
    "şartlarla giriş-çıkış komisyonu uygulanabilir; ancak kurucu, yönetici ve ilişkililerce kurulan veya yönetilen fonların "
    "payları portföye alınırsa bu fonlara giriş veya çıkış komisyonu ödenemez. m. 15/6 kurucunun pay edinmesine imkân verir.",
    topic=KY, zorluk="hard")

T2.q("6362 s. SPKn m. 56",
    f"{K}, kolektif yatırım kuruluşlarında portföy saklama hizmetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Varlıklar Kurul kararıyla takas kuruluşunda izlenirse saklayıcının yükümlülükleri sona erer.",
    ["Kurul, uygun görülen varlıkların merkezî takas kuruluşunda izlenmesini zorunlu tutabilir.",
     "Portföy saklayıcısı ile portföy yönetim şirketi aynı tüzel kişi olamaz.",
     "Saklayıcı, varlıkları başka portföy saklama kuruluşları nezdinde saklayabilir.",
     "Alt saklama hâlinde saklama hizmeti veren tüm kuruluşlar müteselsilen sorumludur."],
    "Kanun m. 56/5'e göre Kurul uygun görülen varlıkların merkezî saklama veya takas kuruluşunda izlenmesini zorunlu tutabilir; "
    "saklayıcının yükümlülükleri bu durumda da devam eder. m. 56/4 alt saklamayı ve müteselsil sorumluluğu, m. 56/6 saklayıcı "
    "ile portföy yönetim şirketinin ayrı tüzel kişi olmasını düzenler.", topic=KY)

T2.sayisal("III-52.1 m. 20/3",
    f"{YF}, orta vadeli ve uzun vadeli borçlanma araçları fonlarında vadeye kalan gün sayısı hesaplanamayan varlıklar fon "
    "toplam değerinin en fazla yüzde kaçı oranında portföye dahil edilebilir?",
    "%20", ["%5", "%10", "%25", "%40"],
    "Tebliğ m. 20'ye göre para piyasası ve kısa vadeli borçlanma araçları fonlarında vadeye kalan gün sayısı hesaplanamayan "
    "varlıklar portföye alınamaz; orta ve uzun vadeli fonlarda bu varlıklar en fazla %20 oranında alınabilir ve ağırlıklı "
    "ortalama vade hesabında dikkate alınmaz.", topic=KY, zorluk="hard")

T2.q("6362 s. SPKn m. 58/7, 60",
    f"{K}, ipotek finansmanı kuruluşlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İpotek finansmanı kuruluşları ancak konut finansmanı fonu kurarak ipoteğe dayalı araç ihraç edebilir.",
    ["İpotek finansmanı kuruluşları anonim ortaklık şeklinde kurulur.",
     "Sermayelerinin nakden ve her türlü muvazaadan âri olarak ödenmiş olması gerekir.",
     "Yüzde on ve üzeri pay sahipleri banka kurucuları için aranan şartları taşır.",
     "Bu kuruluşların ipotekli araç ihracına ilişkin esasları Kurul belirler."],
    "Kanun m. 60'a göre ipotek finansmanı kuruluşları anonim ortaklık olup sermayeleri nakden ve muvazaadan âri ödenmiş olmalı, "
    "kurucuları ve yüzde on ve üzeri pay sahipleri banka kurucusu şartlarını taşımalıdır. m. 58/7'ye göre bu kuruluşlar konut "
    "veya varlık finansmanı fonu kurmaksızın ipoteğe veya varlığa dayalı araç ihraç edebilir.", topic=AR)

T2.q("6362 s. SPKn m. 61/A",
    f"{K}, gayrimenkul sertifikalarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gayrimenkul sertifikaları farklı nominal değerlerle ihraç edilebilir.",
    ["Sertifikalar projenin belirli bağımsız bölümlerini veya alan birimlerini temsil eder.",
     "Kurul, genel esaslara ihraççı bazında muafiyet verebilir veya farklı esaslar belirleyebilir.",
     "İhraçla elde edilen fon, sertifikalar itfa edilinceye kadar haczedilemez.",
     "Vadede edimler yerine getirilemezse sertifika sahipleri toplantısı yapılır."],
    "Kanun m. 61/A'ya göre gayrimenkul sertifikası, projenin belirli bağımsız bölümlerini veya alan birimini temsil eden nominal "
    "değeri eşit bir araçtır; Kurul ihraççı bazında muafiyet veya farklı esas belirleyebilir. Elde edilen fon ve bölümler "
    "itfaya kadar haczedilemez; vadede edimler yerine getirilemezse sahipler toplantısı yapılır.", topic=AR)

T2.oncul("6362 s. SPKn m. 31/A",
    "Bir ihraççının tahvil sahipleri, faiz ödemelerindeki gecikme üzerine borçlanma aracı sahipleri kurulunu toplamak "
    "istemektedir. Bu kurula ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Kurul, ihraççının yönetim kurulu veya tahvil sahipleri tarafından toplantıya çağrılabilir.",
     "Toplantıya çağrı ve karar alma esaslarının izahname veya ihraç belgesinde belirlenmesi zorunludur.",
     "Borçlanma aracı sahiplerini temsil etmek üzere temsilci atanamaz.",
     "İhraççının her bir tertip borçlanma aracının sahipleri ayrı bir kurul oluşturabilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 31/A'ya göre kurul ihraççının yönetim kurulu veya borçlanma aracı sahiplerince toplantıya çağrılabilir ve çağrı ile "
    "karar esaslarının izahname ve/veya ihraç belgesinde belirlenmesi zorunludur; her tertip ayrı kurul oluşturabilir ve "
    "sahipleri temsil etmek üzere temsilci atanabilir.", topic=AR)

T2.q("6362 s. SPKn m. 85/3",
    "Tazmin kararı verilen bir aracı kurumda bir yatırımcının hesabında saklanan paylar bulunmakta, yatırımcının da aracı kuruma "
    f"yerine getirilmemiş takas borcu vardır. {K}, bu yatırımcının tazmin tutarının belirlenmesine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Saklanan paylar önce hak sahibine dağıtılır ve takas borcu için mahsup edilir.",
    ["Saklanan paylar satılarak YTM’ye gelir kaydedilir.",
     "Takas borcu dikkate alınmaz, tazmin brüt tutar üzerinden yapılır.",
     "Saklanan paylar tazmin tutarına eklenmez; tazmin sadece yatırımcının nakit alacakları üzerinden yapılır.",
     "Tazmin tutarı, payların tazmin kararı tarihindeki değerinin iki katıdır."],
    "Kanun m. 85/3'e göre tazmin, kuruluşça karşılanmayan nakit ve araç iade yükümlülükleri üzerinden hesaplanır; yatırımcılar "
    "adına saklanan araçlar öncelikle hak sahiplerine dağıtılır, bulundukları hesap bazında ve özellikle yerine getirilmemiş "
    "takas yükümlülükleri için mahsup edilir ve kuruluşun mahsup talepleri dikkate alınır.", topic=KS, zorluk="hard")

T2.q("6362 s. SPKn m. 46/1-3",
    f"{K}, yatırım hizmetleri kapsamında teminat yatırılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Teminatların türü ve miktarı her yatırım kuruluşunun kendi yönetim kurulunca belirlenir.",
    ["Kurul, yatırım hizmetlerinde bulunacaklara teminat yatırma veya bulundurma zorunluluğu getirebilir.",
     "Yatırım kuruluşları açığa satış işlemleri nedeniyle yatırımcılardan teminat isteyebilir.",
     "Borsalar yatırımcılardan yatırım hizmetleri kapsamında teminat isteyebilir.",
     "Bu teminatlar tevdi amaçları dışında kullanılamaz."],
    "Kanun m. 46'ya göre Kurul teminat zorunluluğu getirebilir; yatırım kuruluşları, borsalar ve takas ve saklama kuruluşları "
    "teminat isteyebilir ve teminatlar tevdi amacı dışında kullanılamaz. Teminatların türü, miktarı, kullanımı, yatırılması ve "
    "serbest bırakılmasına ilişkin esasları Kurul belirler.", topic=KS)

T2.sayisal("6362 s. SPKn m. 97/1",
    "Kurul, bir aracı kurumun sermaye yeterliliği yükümlülüğünü sağlayamadığını tespit etmiş ve faaliyetleri durdurmak yerine "
    f"mali yapının güçlendirilmesi için süre vermeye karar vermiştir. {K}, verilecek bu süre en fazla kaç ay olabilir?",
    "3", ["1", "6", "9", "12"],
    "Kanun m. 97/1'e göre Kurul, sermaye piyasası kurumlarının sermaye yeterliliğini sağlayamaması veya mali yapısının zayıflaması "
    "hâlinde üç ayı geçmemek üzere uygun süre içinde mali yapının güçlendirilmesini isteyebilir ya da süre vermeksizin "
    "faaliyetleri geçici olarak durdurmak dahil tedbirler alabilir.", topic=DZ)

T2.q("6362 s. SPKn m. 121/5, 135",
    f"{K}, Kurul Başkan ve üyelerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mal bildiriminde bulunulması ve yolsuzlukla mücadeleye ilişkin kanuna tabidirler.",
    ["Görevleri sırasında öğrendikleri sırları görevden ayrıldıktan sonra açıklayabilirler.",
     "Görev süreleri dolmadan hastalık dahil herhangi bir sebeple görevden alınamazlar.",
     "Kurulun denetlediği ortaklıklarda yönetim kurulu üyeliği yapabilirler.",
     "Kurul kararlarına karşı açılan davalarda şahsen davalı olurlar."],
    "Kanun m. 121/5'e göre Kurul Başkan ve üyeleri 3628 sayılı Mal Bildiriminde Bulunulması, Rüşvet ve Yolsuzluklarla Mücadele "
    "Kanununa tabidir. m. 135'e göre sır saklama yükümlülüğü görevden ayrıldıktan sonra da devam eder; m. 120 ağır hastalık gibi "
    "hâllerde görevden almayı düzenler.", topic=DZ)

T2.q("6362 s. SPKn m. 109/1",
    "Bir şirket, Kurul onaylı ihraç belgesi almadan, halka arz etmeksizin belirli yatırımcılara tahvil satmıştır. "
    f"{K}, bu fiile ilişkin aşağıdakilerden hangisi doğrudur?",
    "Onaylı ihraç belgesi olmaksızın satış hapis ve adli para cezası gerektirir.",
    ["Halka arz yapılmadığı için fiil suç oluşturmaz, sadece idari para cezası verilir.",
     "Fiil ancak yatırımcı sayısı beş yüzü aşarsa suç oluşturur.",
     "Fiil güveni kötüye kullanma suçunun nitelikli hâlini oluşturur.",
     "Fiil, tahviller vadesinde ödendiği sürece yaptırımsız kalır."],
    "Kanun m. 109/1'e göre onaylı izahname yayımlamaksızın halka arz edenler gibi onaylı ihraç belgesi olmaksızın sermaye "
    "piyasası araçlarını satanlar da iki yıldan beş yıla kadar hapis ve beş bin günden on bin güne kadar adli para cezası ile "
    "cezalandırılır.", topic=PS)

T2.q("6362 s. SPKn m. 103/4",
    f"{K}, ihraççı yöneticilerinin kısa vadeli kazançlarına ilişkin hükme göre aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yükümlülüğün doğması için kazancın içsel bilgiye dayanması gerekir.",
    ["Yükümlülük, Kurulca belirlenen zaman dilimindeki alım satımlardan elde edilen kazanç için doğar.",
     "Yönetim kurulu üyeleri ve yöneticiler net kazancı ihraççıya vermekle yükümlüdür.",
     "Kurulca izin verilen hâllerdeki işlemler bu yükümlülüğün dışındadır.",
     "Süresinde ödeme yapmayanlara menfaatin iki katı idari para cezası verilir."],
    "Kanun m. 103/4'e göre m. 106'daki nitelikte bir bilginin varlığı aranmaksızın, Kurulca izin verilen hâller hariç ve Kurulca "
    "belirlenen zaman dilimi içinde ihraççı paylarının alım satımından kazanç elde eden yönetim kurulu üyeleri ve yöneticiler "
    "net kazancı ihraççıya verir; otuz gün içinde vermeyenlere menfaatin iki katı idari para cezası uygulanır.", topic=PS,
    zorluk="hard")

# =============================================================================== TEST 3
T3 = paket("questions_sermaye_piyasasi_test3_2026.json", 2026092833, ["spk-t3-0020"])

T3.q("6362 s. SPKn m. 12/1, 3",
    f"{K}, sermaye piyasası araçlarının satışına ve pay bedellerinin ödenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Pay bedellerinin dörtte biri peşin, kalanı iki yıl içinde ödenebilir.",
    ["İhraç olunan payların bedellerinin tamamen ve nakden ödenmesi şarttır.",
     "Kurul, satılamayan payların alınacağının ortaklığa karşı taahhüt edilmesini isteyebilir.",
     "Kurul, birleşme ve bölünme gibi hâllerde nakden ödeme zorunluluğu olmayan durumları belirleyebilir.",
     "Sermaye piyasası araçlarının satış esnasında alıcıya teslimi şarttır."],
    "Kanun m. 12/1'e göre ihraç olunan payların bedelleri tamamen ve nakden ödenir; Kurul satılamayan payların alınacağının "
    "taahhüdünü isteyebilir ve nakdi ödemenin zorunlu olmadığı yapılandırmaları belirleyebilir. m. 12/3'e göre araçların satış "
    "esnasında alıcıya teslimi şarttır. TTK'daki taksitli ödeme imkânı halka açık ihraçlarda uygulanmaz.", topic=IH)

T3.q("II-5.1 m. 11/1-b",
    "Halka açık olmayan bir ortaklığın payları Gelişen İşletmeler Piyasasında işlem görmek üzere ilk defa halka arz edilecek, "
    f"satış 1 Mart’ta başlayacaktır. {IZ}, izahnamede yer alacak finansal tablolar aşağıdakilerden hangisidir?",
    "Son yıllık karşılaştırmalı finansal tablolar",
    ["Son üç yıllık finansal tablolar",
     "Son yıllık ve altı aylık ara dönem karşılaştırmalı finansal tablolar",
     "Son üç yıllık ve dokuz aylık ara dönem finansal tablolar",
     "Son iki yıllık finansal tablolar"],
    "Tebliğ m. 11/1-b'ye göre GİP'te işlem görmek üzere ilk halka arzda satış 16 Şubat - 15 Ağustos arasında ise son yıllık "
    "karşılaştırmalı finansal tablolar; 16 Ağustos - 31 Aralık arasında altı aylık ara dönem de eklenir; 1 Ocak - 15 Şubat "
    "arasında önceki yıllık tablolarla altı aylık ara dönem yer alır.", topic=IH, zorluk="hard")

T3.q("II-5.2 m. 8/1-2",
    "Tahsisli satılan bir borçlanma aracı belirli bir gün sonunda 140 bireysel yatırımcı ile 30 nitelikli yatırımcının "
    f"hesabında bulunmaktadır. {ST}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Nitelikli yatırımcılar hesaba katılmadığından yatırımcı sayısı sınırı aşılmamıştır.",
    ["Toplam 170 yatırımcı olduğu için sınır aşılmış ve izahname başvurusu gerekmiştir.",
     "Sınır sadece bireysel yatırımcılar için 100 olduğundan aşılmıştır.",
     "Tahsisli satılan araçları nitelikli yatırımcılar satın alamaz.",
     "Yatırımcı sayısı sadece ihraç tarihinde kontrol edilir, sonraki değişiklikler dikkate alınmaz."],
    "Tebliğ m. 8'e göre tahsisli satılan araçları belirli bir anda elinde bulunduran yatırımcı sayısı yüz elliyi geçmemelidir; "
    "bu araçlar nitelikli yatırımcılarca da alınabilir ve yüz elli kişinin hesaplanmasında nitelikli yatırımcılar dikkate "
    "alınmaz. Kontrol vade boyunca günlük yapılır; 140 kişi sınırın altındadır.", topic=IH, zorluk="hard")

T3.sayisal("II-23.3 m. 13/3",
    "Payları borsada işlem gören bir ortaklık, ayrılma hakkına konu payları kendisi almadan önce diğer pay sahiplerine önermeye "
    f"karar vermiştir. {ON}, bu payları almak isteyenler genel kurul tarihinden itibaren kaç iş günü içinde yazılı taleplerini "
    "aracı kuruma iletmelidir?",
    "3", ["1", "5", "6", "10"],
    "Tebliğ m. 13/3'e göre ayrılma hakkına konu payları satın almak isteyen pay sahipleri veya yatırımcılar genel kurul "
    "tarihinden itibaren üç iş günü içinde taleplerini ortaklığın belirlediği aracı kuruma iletir ve fonu bloke eder; yönetim "
    "kurulu dördüncü iş gününde karar alıp KAP'ta ilan eder.", topic=IH, zorluk="hard")

T3.q("II-23.2 m. 16",
    "Bir bölünme sözleşmesinin imzalanmasından sonra, genel kurula sunulmadan önce, bölünmeye taraf şirketlerden birinin "
    f"devre konu malvarlığında önemli bir değer kaybı olmuştur. {BB}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Durum genel kurula, diğer tarafların yönetim organlarına ve Kurula yazılı bildirilir.",
    ["Değişiklik bölünmeyi etkilemez; sözleşme aynen genel kurula sunulur.",
     "Bölünme Kurul kararıyla iptal edilir.",
     "Durum sadece bağımsız denetçiye bildirilir; denetçinin ek raporu genel kurula sunulur.",
     "Taraflar sözleşmeyi değiştiremez; sadece bölünmeden vazgeçebilir."],
    "Tebliğ m. 16'ya göre bölünme sözleşmesi veya planının imzalanması ile genel kurul arasında önemli bir değişiklik olursa "
    "ilgili şirketin yönetim organı bunu kendi genel kuruluna, diğer tarafların yönetim organlarına ve Kurula yazılı bildirir; "
    "yönetim organları sözleşmenin değiştirilmesi veya bölünmeden vazgeçilmesi gereğini inceler.", topic=IH)

T3.q("II-15.1 m. 11/1",
    "Payları borsada işlem gören bir ihraççının aşağıdaki kişileri, ihraççının paylarında işlem yapmıştır. "
    f"{OD}, bu kişilerden hangisinin işlemleri idari sorumluluğu bulunan kişilerin işlemlerine ilişkin açıklama yükümlülüğü "
    "kapsamında değildir?",
    "İhraççının idari karar yetkisi bulunmayan muhasebe uzmanının kardeşi",
    ["İhraççının tüzel kişi ana ortağı",
     "Yönetim kurulu üyesinin aynı evde yaşayan yetişkin çocuğu",
     "Yönetim kurulu üyesinin kontrol ettiği bir şirket",
     "İdari karar yetkisi bulunan ve içsel bilgilere düzenli erişen genel müdür yardımcısı"],
    "Tebliğ m. 4 ve 11'e göre açıklama yükümlülüğü idari sorumluluğu bulunan kişileri (yönetim kurulu üyeleri ve içsel bilgiye "
    "düzenli erişip idari karar veren yöneticiler), bunlarla yakından ilişkili kişileri (eş, çocuk, aynı evde yaşayanlar, "
    "kontrol edilen şirketler) ve ihraççının ana ortağını kapsar. Karar yetkisi olmayan çalışanın kardeşi kapsam dışındadır.",
    topic=KA, zorluk="hard")

T3.q("6362 s. SPKn m. 30/4-5",
    f"{K}, halka açık ortaklık genel kurullarında vekâleten ve elektronik ortamda oy kullanılmasına ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "TTK’nın temsil yoluyla oy kullanmaya ilişkin m. 428 hükmü aynen uygulanır.",
    ["Oy hakkı sahipleri haklarını vekil tayin ettikleri kişiler aracılığıyla kullanabilir.",
     "Saklama hizmeti sunanların vekil sıfatıyla oy kullanmasında da vekâlet hükümleri uygulanır.",
     "Çağrı yoluyla vekâlet toplanmasına ilişkin esaslar Kurulca belirlenir.",
     "Payları kayden izlenen ortaklıklarda elektronik katılım MKK sistemi üzerinden gerçekleşir."],
    "Kanun m. 30/4'e göre oy hakları vekil aracılığıyla kullanılabilir, saklama hizmeti sunanların vekâleten oy kullanmasında "
    "da bu hüküm uygulanır ve çağrı yoluyla vekâlet toplama esaslarını Kurul belirler; TTK m. 428 uygulanmaz. m. 30/5 "
    "elektronik katılımı MKK sistemine bağlar.", topic=KA)

T3.oncul("6362 s. SPKn m. 14",
    "İhraççıların finansal raporlamasına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Bağımsız denetim, Türkiye Denetim Standartları çerçevesinde yapılır.",
     "Denetim, Kanun uyarınca listeye alınan bağımsız denetim kuruluşlarınca yapılır.",
     "Bağımsız denetim raporları kamuya duyurulmaz, sadece Kurula gönderilir.",
     "Finansal tabloların hazırlanmasından ihraççının yönetim kurulu üyeleri kusurlarına göre sorumludur."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 14/3'e göre Kurulca belirlenen tablolar listedeki bağımsız denetim kuruluşlarına Türkiye Denetim Standartları "
    "çerçevesinde denetletilir; m. 14/2 ihraççı ve yönetim kurulu üyelerinin sorumluluğunu düzenler. m. 14/5'e göre tablolar ve "
    "bağımsız denetim raporu Kurulca belirlenen esaslara göre kamuya duyurulur.", topic=KA)

T3.sayisal("III-52.1 m. 17/6",
    "Bir fonun kurucusunun grup şirketi olan aracı kurum, borsa dışında bir ortaklığın paylarının halka arzına aracılık etmiştir. "
    f"{YF}, fon bu paylara borsada işlem görmesi şartıyla fon toplam değerinin en fazla yüzde kaçı oranında yatırım yapabilir?",
    "%5", ["%1", "%10", "%20", "%25"],
    "Tebliğ m. 17/6'ya göre kurucunun grup şirketlerinin borsa dışında halka arzına aracılık ettiği ortaklık paylarına, borsada "
    "işlem görmesi şartıyla ihraç miktarının azami %10'u ve fon toplam değerinin azami %5'i oranında yatırım yapılabilir.",
    topic=KY, zorluk="hard")

T3.oncul("6362 s. SPKn m. 52, 58",
    "Yatırım fonları ile konut ve varlık finansmanı fonlarına ilişkin aşağıdaki eşleştirmeler verilmiştir:",
    ["Yatırım fonunu temsil eden ve yöneten – Portföy yönetim şirketi",
     "Konut finansmanı fonunu temsil eden ve yöneten – Fon kurulu",
     "Varlık finansmanı fonunda sicil işlemlerini imzalayanlar – Fon kurucusu ile fon kurulunun yetkilileri",
     "Yatırım fonunun tapu işlemlerini imzalayanlar – Sadece portföy saklayıcısının yetkilisi"],
    f"{K}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, II ve III", ["I ve II", "II ve IV", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 52'ye göre yatırım fonunu portföy yönetim şirketi temsil eder ve yönetir; tapu işlemleri şirket ile saklayıcıyı "
    "temsil eden birer yetkilinin müşterek imzasıyla yapılır. m. 58'e göre konut ve varlık finansmanı fonlarını fon kurulu "
    "temsil eder ve sicil işlemleri kurucu ile fon kurulunu temsil eden yetkililerin müşterek imzasıyla yapılır.", topic=KY)

T3.q("6362 s. SPKn m. 48/4",
    "Bir girişim sermayesi yatırım ortaklığı, belirli bir gruba yönetim kurulunda temsil ve oyda imtiyaz tanıyan paylar "
    f"ihraç etmek istemektedir. {K}, bu ihraca ilişkin aşağıdakilerden hangisi doğrudur?",
    "Esaslarını Kurul belirler; TTK m. 360 ve m. 479/2 uygulanmaz.",
    ["Yatırım ortaklıklarının imtiyazlı pay ihraç etmesi yasaktır.",
     "İmtiyazlı pay ihracı için TTK’daki oyda imtiyaz sınırı aynen uygulanır.",
     "İmtiyazlı paylar sadece halka arz edilmeyen yatırım ortaklıklarınca ihraç edilebilir.",
     "İmtiyazlı pay ihracı Hazine ve Maliye Bakanlığının iznine tabidir."],
    "Kanun m. 48/4'e göre yatırım ortaklıklarının imtiyazlı pay ihracına ilişkin esaslar Kurulca belirlenir; yönetim kurulunda "
    "temsil imtiyazı ile oyda imtiyaz tanıyan pay ihracında TTK'nın m. 360 ile m. 479/2 hükümleri uygulanmaz.", topic=KY,
    zorluk="hard")

T3.q("6362 s. SPKn m. 3/ğ",
    "Bir anonim ortaklık, yeni çıkardığı borçlanma araçlarını halka arz etmeksizin sadece üç kurumsal yatırımcıya satmıştır. "
    f"{K}, bu işlemin niteliği aşağıdakilerden hangisidir?",
    "Halka arz edilmeksizin yapılan bir ihraçtır.",
    ["İhraç sayılmaz; özel hukuk kapsamında borç sözleşmesidir.",
     "Halka arz sayılır, çünkü birden fazla yatırımcıya satış yapılmıştır.",
     "Kitle fonlaması sayılır.",
     "Borsa dışı teşkilatlanmış pazar yeri işlemi sayılır."],
    "Kanun m. 3/ğ'ye göre ihraç, sermaye piyasası araçlarının ihraççılar tarafından çıkarılıp halka arz edilerek veya halka arz "
    "edilmeksizin satışıdır; m. 3/f'ye göre halka arz genel bir çağrı ve bu çağrı devamında satışı gerektirir. Belirli "
    "yatırımcılara satış halka arz edilmeksizin ihraçtır ve m. 11 uyarınca ihraç belgesi gerektirir.", topic=AR, zorluk="easy")

T3.q("6362 s. SPKn m. 35/B-3-a-2",
    "Bir kişi, iradi tasfiye dışında faaliyet izni iptal edilmiş bir faktoring şirketinde %15 pay sahibidir ve bir kripto "
    f"varlık platformuna kurucu ortak olmak istemektedir. {K}, bu kişinin durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Faaliyet izni iptal edilen bir kuruluşta %10 ve üzeri paya sahip olduğundan platforma ortak olamaz.",
    ["Pay oranı %25’in altında olduğu için ortak olabilir.",
     "Faktoring şirketi sermaye piyasası kurumu olmadığı için bu durum şart kapsamında değildir.",
     "Ortak olabilir, ancak yönetim kuruluna seçilemez.",
     "Kurulun onayı alınırsa bu şarttan muaf tutularak ortak olabilir."],
    "Kanun m. 35/B-3-a-2'ye göre kripto varlık hizmet sağlayıcı ortaklarının, iradi tasfiye dışında faaliyet izni iptal edilmiş "
    "faktoring, finansal kiralama, finansman, varlık yönetim, sigorta şirketleri ile para ve sermaye piyasası kurumlarında "
    "doğrudan veya dolaylı %10 veya daha fazla paya sahip olmaması veya kontrolü elinde bulundurmaması şarttır.", topic=AR,
    zorluk="hard")

T3.q("6362 s. SPKn m. 35/A",
    f"{K}, kitle fonlama platformlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fon sağlayıcı başına yatırım limiti Kanunda tutar olarak belirlenmiştir.",
    ["Platformların kurulması ve faaliyete başlaması Kurul iznine tabidir.",
     "Platformların ortaklarına ve pay devirlerine ilişkin esasları Kurul belirler.",
     "Toplanan fonların amacına uygun kullanımının denetim esaslarını Kurul belirler.",
     "Platformların hukuka aykırı işlemlerinde Kanunun m. 96 hükümleri kıyasen uygulanır."],
    "Kanun m. 35/A'ya göre platformlar Kurul iznine tabidir; kuruluş, ortaklar, pay devirleri, fon sağlayıcı başına ve girişim "
    "başına azami tutarlar ile fonların amacına uygun kullanımının denetimine ilişkin esasları Kurul belirler. Hukuka aykırı "
    "işlemlerde m. 96 kıyasen uygulanır; limitler Kanunda tutar olarak yer almaz.", topic=AR)

T3.q("6362 s. SPKn m. 13/2-3",
    f"{K}, kaydi sermaye piyasası araçlarının hesaplarda izlenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Toplu hesap tutulmasına MKK yönetim kurulu karar verir.",
    ["Kaydi araçlar nama veya hamiline yazılı olmalarına bakılmaksızın isme açılmış hesaplarda izlenir.",
     "Kurul, aracın türüne ve MKK üyesinin niteliğine göre toplu hesap tutulmasına karar verebilir.",
     "Kayıtlar MKK’nın oluşturduğu elektronik ortamda MKK üyelerince tutulur.",
     "Kaydi araçlara ilişkin haklar MKK tarafından izlenir."],
    "Kanun m. 13/2'ye göre kaydi araçlar isme açılmış hesaplarda izlenir; Kurul aracın türüne ve ihraççının veya MKK üyesinin "
    "niteliğine göre hak sahibi ismine hesap açılmaksızın toplu hesap tutulmasına karar verebilir. m. 13/3'e göre haklar MKK "
    "tarafından izlenir, kayıtlar üyelerce tutulur.", topic=KS)

T3.q("6362 s. SPKn m. 86/4",
    f"{K}, hakkında tedricî tasfiye kararı verilen bir sermaye piyasası kurumuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Amme alacakları için başlamış takipler devam eder.",
    ["Kurumun ödemeleri durur ve mal varlığı üzerinde sadece YTM tasarruf edebilir.",
     "Tasfiyenin kapatılması kararına kadar kurum hakkında iflas kararı verilemez.",
     "Tazmin ile tasfiye arasındaki süreçte uygulanacak temerrüt faizini Kurul belirler.",
     "Bir takip muamelesiyle kesilebilen zamanaşımı süreleri işlemez."],
    "Kanun m. 86/4'e göre tedricî tasfiye kararı verilenlerin ödemeleri durur ve mal varlığı üzerinde sadece YTM tasarruf eder; "
    "kapatmaya kadar iflas kararı verilemez, temerrüt faizini Kurul belirler. Hakkında İİK ve 6183 sayılı Kanun kapsamında "
    "takip yapılamaz, başlamış takipler durur ve zamanaşımı süreleri işlemez.", topic=KS, zorluk="hard")

T3.q("6362 s. SPKn m. 123/5-6",
    "Kurul Karar Organı, bir düzenleme taslağını görüşürken bir akademisyeni toplantıya davet etmiştir. "
    f"{K}, Karar Organı toplantılarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurul kararları davet edilen kişilerin huzurunda alınabilir.",
    ["Karar Organı toplantılarının gizliliği esastır.",
     "Görüşlerinden yararlanmak üzere Kurul personeli toplantıya davet edilebilir.",
     "Katılımında fayda görülen Kurul dışından kişiler toplantıya davet edilebilir.",
     "Sakıncalı görülenler dışındaki kararlar internet başta olmak üzere kamuoyuna duyurulur."],
    "Kanun m. 123/5'e göre toplantıların gizliliği esastır; Kurul personeli ve Kurul dışından kişiler davet edilebilir, ancak "
    "kararlar dışarıdan katılanların yanında alınamaz. m. 123/6'ya göre ülke ekonomisi ve kamu düzeni açısından sakıncalı "
    "görülenler dışındaki kararlar kamuoyuna duyurulur.", topic=DZ)

T3.sayisal("6362 s. SPKn m. 75/2",
    "Türkiye Sermaye Piyasaları Birliğinin organlarının seçimi yapılmış ve seçim sonuçları tutanağa bağlanmıştır. "
    f"{K}, seçimlere yapılacak itirazlar tutanağın düzenlenmesinden itibaren kaç iş günü içinde seçim kurulu başkanı hâkime yapılır?",
    "2", ["1", "3", "5", "10"],
    "Kanun m. 75/2'ye göre seçim sonuçları tutanakla tespit edilir; tutanağın düzenlenmesinden itibaren iki iş günü içinde "
    "seçimlere yapılacak itirazlar hâkim tarafından aynı gün incelenerek kesin olarak karara bağlanır; Kurulun da itiraz hakkı "
    "vardır.", topic=DZ, zorluk="hard")

T3.q("6362 s. SPKn m. 110/1-c",
    "Halka açık bir ortaklığın yöneticileri, ilişkili bir şirketle piyasa teamüllerine aykırı biçimde yapay işlem hacmi "
    f"üreterek ortaklığın kârının artmasını engellemiştir. {K}, bu fiil aşağıdakilerden hangisini oluşturur?",
    "Güveni kötüye kullanma suçunun nitelikli hâli",
    ["Bilgi suistimali suçu", "İşlem bazlı piyasa dolandırıcılığı suçu", "Sadece idari para cezası gerektiren kabahat",
     "Usulsüz halka arz suçu"],
    "Kanun m. 110/1-c'ye göre halka açık ortaklıklar ve kolektif yatırım kuruluşlarının ilişkili kişilerle emsallere ve piyasa "
    "teamüllerine aykırı anlaşmalar veya işlem hacmi üretmek gibi işlemlerle kârlarını azaltması veya artışını engellemesi "
    "güveni kötüye kullanma suçunun nitelikli hâlidir; ceza üç yıldan az olamaz.", topic=PS)

T3.oncul("6362 s. SPKn m. 106, 107, 109",
    "Sermaye piyasası suçları ile öngörülen cezalar aşağıda eşleştirilmiştir:",
    ["Bilgi bazlı piyasa dolandırıcılığı – Sadece idari para cezası",
     "Bilgi suistimali – Hapis veya adli para cezası (seçimlik)",
     "İşlem bazlı piyasa dolandırıcılığı – Hapis ve adli para cezası (birlikte)",
     "İzinsiz sermaye piyasası faaliyeti – Hapis ve adli para cezası (birlikte)"],
    f"{K}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "II, III ve IV", ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 106'ya göre bilgi suistimali üç yıldan beş yıla kadar hapis veya adli para cezası; m. 107/1 işlem bazlı piyasa "
    "dolandırıcılığı ve m. 109/2 izinsiz faaliyet hapis ve adli para cezası birlikte; m. 107/2 bilgi bazlı piyasa dolandırıcılığı "
    "da üç yıldan beş yıla kadar hapis ve beş bin güne kadar adli para cezası gerektirir.", topic=PS, zorluk="hard")

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
