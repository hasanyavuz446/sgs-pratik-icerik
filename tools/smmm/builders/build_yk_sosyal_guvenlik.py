# -*- coding: utf-8 -*-
"""Hukuk · Sosyal Güvenlik Mevzuatı · Sigortalılık, Bildirim ve Denetim — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında 5510 sayılı Kanun soruları Hukuk dersinin en kalabalık kümesidir; bakmakla yükümlü
kişiler, 4/a-b-c ayrımı, sigortalı sayılmayanlar, işe giriş bildirgesinin süresi, denetim ve idari para cezaları
"5510 sayılı … Kanunu’na göre … hangisi … değildir / yanlıştır" kalıbıyla sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 5510 sayılı Kanun md. 3-9, 11-14, 59, 102.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_sosyal_guvenlik_2026.json", lesson="sosyal_guvenlik_mevzuati", topic="sosyal_guvenlik",
          konu_adi="Sosyal Güvenlik", seed=2026093005,
          surum="5510 sayılı Kanun güncel metni; 29.09.2026 kontrolü")

K = "5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu’na göre"
K26 = ("5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu’nun 2026 yılında yürürlükte olan hükümlerine "
       "göre")

P.sayisal("SGK md. 13",
    f"{K}, 4/a kapsamındaki sigortalının iş kazası, işveren tarafından Kuruma en geç kazadan sonraki kaç iş günü içinde "
    "bildirilmelidir?",
    "3", ["1", "2", "5", "10"],
    "Md. 13'e göre iş kazası işveren tarafından kolluk kuvvetlerine derhal, Kuruma da en geç kazadan sonraki üç iş günü "
    "içinde bildirilir.", zorluk="easy")

P.q("SGK md. 3",
    f"{K}, aşağıdakilerden hangisi genel sağlık sigortalısının bakmakla yükümlü olduğu kişiler arasında değildir?",
    "Geçimi sigortalıca sağlanmayan kardeşi",
    ["Kendi sigortalılığı olmayan eşi",
     "18 yaşını doldurmamış evli olmayan çocuğu",
     "Geçimi sigortalıca sağlanan annesi",
     "Yaşına bakılmaksızın malul, evli olmayan çocuğu"],
    "Md. 3/10'a göre bakmakla yükümlü olunan kişiler eş, yaş ve öğrenim şartlarını taşıyan veya malul olan evli olmayan "
    "çocuklar ile geçimi sigortalı tarafından sağlanan ana ve babadır; kardeş sayılmamıştır.", zorluk="easy")

P.q("SGK md. 3",
    f"{K}, sosyal sigorta kollarının sınıflandırılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hastalık sigortası kısa vadeli bir sigorta koludur.",
    ["Yaşlılık sigortası kısa vadeli bir sigorta koludur.",
     "Analık sigortası uzun vadeli bir sigorta koludur.",
     "Malullük sigortası kısa vadeli bir sigorta koludur.",
     "Ölüm sigortası kısa vadeli bir sigorta koludur."],
    "Md. 3'e göre kısa vadeli sigorta kolları iş kazası ve meslek hastalığı, hastalık ve analık sigortası; uzun vadeli sigorta "
    "kolları malullük, yaşlılık ve ölüm sigortasıdır.", zorluk="easy")

P.sayisal("SGK md. 14",
    f"{K}, işveren, sigortalının meslek hastalığına tutulduğunu öğrendiği günden başlayarak kaç iş günü içinde Kuruma "
    "bildirmelidir?",
    "3", ["2", "5", "7", "10"],
    "Md. 14'e göre meslek hastalığı, durumu öğrenen işveren tarafından öğrenildiği günden başlayarak üç iş günü içinde iş "
    "kazası ve meslek hastalığı bildirgesiyle Kuruma bildirilir.")

P.q("SGK md. 3",
    f"{K}, 4/a ve 4/c kapsamında sigortalı sayılanlar için ücretin tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Para ile ödenen sürekli brüt tutar",
    ["Ayni olarak verilen her türlü yardım",
     "Kesintiler sonrası kalan net tutar",
     "Sadece yılda bir ödenen ikramiye",
     "İşverenin ödediği prim tutarı"],
    "Md. 3/12'ye göre ücret, 4/a ve 4/c kapsamındaki sigortalılara saatlik, günlük, haftalık, aylık veya yıllık olarak para "
    "ile ödenen ve süreklilik niteliği taşıyan brüt tutardır.")

P.q("SGK md. 3",
    f"{K}, “hak sahibi” kavramı kapsamında aşağıdakilerden hangisi yer almaz?",
    "Sigortalının kardeşi",
    ["Sigortalının eşi", "Sigortalının çocuğu", "Sigortalının annesi", "Sigortalının babası"],
    "Md. 3/7'ye göre hak sahibi, sigortalının veya gelir ya da aylık almakta olanların ölümü hâlinde gelir veya aylığa ya da "
    "toptan ödemeye hak kazanan eş, çocuk, ana ve babadır.", zorluk="easy")

P.sayisal("SGK md. 9",
    f"{K}, hizmet akdi sona eren 4/a sigortalısının durumu işveren tarafından en geç kaç gün içinde Kuruma bildirilir?",
    "10", ["3", "5", "15", "30"],
    "Md. 9'a göre (a), (c) ve (d) bentlerine göre sigortalılığı sona erenlerin durumu işverenleri tarafından en geç on gün "
    "içinde Kuruma bildirilir.")

P.q("SGK md. 4",
    f"{K}, aşağıdakilerden hangisi 4/a sigortalısı kapsamında değildir?",
    "Esnaf siciline kayıtlı, vergiden muaf kişi",
    ["Hizmet akdiyle çalışan işçi",
     "Sendika yönetim kuruluna seçilen işçi",
     "Hizmet akdiyle çalışan tiyatro sanatçısı",
     "İŞKUR toplum yararına programa katılan kişi"],
    "Md. 4'e göre gelir vergisinden muaf olup esnaf ve sanatkâr siciline kayıtlı olanlar 4/b kapsamındadır; sendika "
    "yöneticileri, sanatçılar ve İŞKUR programı katılımcıları 4/a hükümlerine tabidir.")

P.q("SGK md. 4",
    f"{K}, aşağıdakilerden hangisi 4/b kapsamında sigortalı sayılır?",
    "Anonim şirketin yönetim kurulu üyesi ortağı",
    ["Anonim şirkette hizmet akdiyle çalışan müdür",
     "Kamu idaresinde kadrolu memur",
     "Yabancı uyruklu hizmet akdiyle çalışan işçi",
     "Çiftçi Mallarının Korunması Kanununa göre çalışan"],
    "Md. 4/b-3'e göre anonim şirketlerin yönetim kurulu üyesi olan ortakları 4/b kapsamında sigortalıdır; hizmet akdiyle "
    "çalışanlar 4/a, kadrolu memurlar 4/c kapsamındadır.")

P.sayisal("SGK md. 8",
    f"{K}, sigortalılar çalışmaya başladıklarını en geç kaç ay içinde Kuruma bildirirler?",
    "1", ["2", "3", "6", "12"],
    "Md. 8'e göre sigortalılar çalışmaya başladıkları tarihten itibaren en geç bir ay içinde bunu Kuruma bildirir; ancak "
    "sigortalının kendini bildirmemesi aleyhine delil teşkil etmez.")

P.q("SGK md. 4",
    f"{K}, aşağıdaki şirket ortaklarından hangisi 4/b kapsamında sigortalı sayılmaz?",
    "Yönetim kurulu dışındaki AŞ ortağı",
    ["Limited şirket ortağı",
     "Kolektif şirket ortağı",
     "Paylı komandit şirketin komandite ortağı",
     "Adi komandit şirket ortağı"],
    "Md. 4/b-3'e göre anonim şirketlerin sadece yönetim kurulu üyesi olan ortakları, paylı komandit şirketlerin komandite "
    "ortakları ve diğer şirketlerin tüm ortakları 4/b kapsamındadır.", zorluk="hard")

P.q("SGK md. 4",
    f"{K}, aşağıdakilerden hangisi 4/c kapsamında sigortalı sayılanlara ilişkin hükümlere tabidir?",
    "Belediye başkanları",
    ["Esnaf ve sanatkârlar", "Köy muhtarları", "Serbest meslek erbabı", "Jokeyler"],
    "Md. 4'e göre belediye başkanları, bakanlar ve TBMM üyeleri 4/c hükümlerine tabidir; köy ve mahalle muhtarları ile "
    "bağımsız çalışanlar 4/b, jokeyler de 4/b hükümlerine tabidir.", zorluk="hard")

P.sayisal("SGK md. 8",
    "Kuruma ilk defa işyeri bildirgesi verilecek bir işyerinde işveren, ilk sigortalıyı 3 Mart’ta çalıştırmaya başlamıştır."
    f"\n\n{K}, bu tarihten itibaren kaç ay içinde çalışmaya başlayan sigortalıların işe giriş bildirgesi, sürenin sonuna "
    "kadar verilirse süresinde verilmiş sayılır?",
    "1", ["2", "3", "4", "6"],
    "Md. 8/b'ye göre ilk defa işyeri bildirgesi verilecek işyerlerinde ilk sigortalı çalıştırılan tarihten itibaren bir ay "
    "içinde çalışmaya başlayanların bildirgesi, en geç bu bir aylık sürenin dolduğu tarihe kadar verilebilir.", zorluk="hard")

P.q("SGK md. 4",
    f"{K}, 4/c kapsamında sigortalı sayılanlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kısa vadeli kollar uygulanmaz.",
    ["Sadece kısa vadeli sigorta kolları uygulanır.",
     "Genel sağlık sigortası hükümleri uygulanmaz.",
     "Bu kişiler 4/b kapsamında sayılır.",
     "Sigortalılık vergi mükellefiyetiyle başlar."],
    "Md. 4'e göre kısa vadeli sigorta kollarına ilişkin hükümler 4/c kapsamında sigortalı sayılanlara bu kapsamda oldukları "
    "sürece uygulanmaz.")

P.q("SGK md. 5",
    f"{K}, ceza infaz kurumlarının atölyelerinde çalıştırılan hükümlü ve tutuklular hakkında hangi sigorta kolları "
    "uygulanır?",
    "İş kazası-meslek hastalığı ve analık",
    ["Sadece hastalık sigortası",
     "Malullük, yaşlılık ve ölüm sigortası",
     "Tüm kısa ve uzun vadeli kollar",
     "Sadece genel sağlık sigortası"],
    "Md. 5/a'ya göre hükümlü ve tutuklular hakkında iş kazası ve meslek hastalığı ile analık sigortası uygulanır ve bunlar 4/a "
    "kapsamında sigortalı sayılır.", zorluk="hard")

P.sayisal("SGK md. 8",
    f"{K}, 4/c kapsamında sigortalı sayılan kişileri ilk defa çalıştıran kamu idaresi, sigortalılık başlangıcından "
    "itibaren kaç gün içinde işe giriş bildirgesi vermelidir?",
    "15", ["3", "10", "20", "30"],
    "Md. 8'e göre 4/c kapsamındaki kişileri ilk defa veya tekrar çalıştıran işverenler sigortalılık başlangıcından itibaren "
    "on beş gün içinde işe giriş bildirgesi verir.", zorluk="hard")

P.q("SGK md. 5",
    f"{K}, 3308 sayılı Kanuna göre aday çırak ve çıraklar hakkında hangi sigorta kolları uygulanır?",
    "İş kazası-meslek hastalığı ve hastalık",
    ["Sadece malullük sigortası",
     "Yaşlılık ve ölüm sigortası",
     "Malullük, yaşlılık ve ölüm sigortaları",
     "Tüm uzun vadeli sigorta kolları"],
    "Md. 5/b'ye göre aday çırak, çırak ve işletmelerde mesleki eğitim gören öğrenciler hakkında iş kazası ve meslek hastalığı "
    "ile hastalık sigortası uygulanır.")

P.q("SGK md. 6",
    f"{K}, aşağıdakilerden hangisi kısa ve uzun vadeli sigorta kolları bakımından sigortalı sayılmayanlar arasında "
    "değildir?",
    "Ücretle çalışan eş",
    ["İşyerinde ücretsiz çalışan eş",
     "Er ve erbaş olarak askerlik yapanlar",
     "Rehabilite edilen hasta veya malul",
     "18 yaşını doldurmamış 4/b’liler"],
    "Md. 6'ya göre işverenin işyerinde ücretsiz çalışan eşi sigortalı sayılmaz; ücretle çalışan eş ise bu istisnanın "
    "kapsamında değildir.", zorluk="hard")

P.sayisal("SGK md. 11",
    f"{K}, işyeri başka bir işverene devredildiğinde yeni işveren, devraldığı tarihi takip eden kaç gün içinde işyeri "
    "bildirgesini Kuruma vermelidir?",
    "10", ["3", "5", "15", "30"],
    "Md. 11'e göre işyerinin başka bir ile nakli veya başka bir işverene devri hâlinde, nakil veya devir tarihini takip eden "
    "on gün içinde işyeri bildirgesi verilir.")

P.oncul("SGK md. 6",
    f"{K} aşağıdaki kişiler değerlendirilmektedir:",
    ["Yedek subay okulu öğrencisi",
     "Ücretle aynı kişi yanında ayda 12 gün ev hizmeti yapan",
     "Yaşlılık aylığı alırken 4/b kapsamında çalışan",
     "Anonim şirketin yönetim kurulu üyesi ortağı"],
    "Yukarıdakilerden hangileri 4. ve 5. maddelere göre sigortalı sayılmaz?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 6'ya göre yedek subay okulu öğrencileri (I) ve yaşlılık aylığı alırken 4/b kapsamında çalışanlar (III) sigortalı "
    "sayılmaz; ayda on gün ve fazla ev hizmetinde çalışan (II) ve yönetim kurulu üyesi ortak (IV) sigortalıdır.",
    zorluk="hard")

P.q("SGK md. 7",
    f"{K}, 4/b kapsamındaki sigortalılar için sigortalılığın başlangıcına ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Limited şirket ortağında hisse devralma tarihi esastır.",
    ["Gelir vergisi mükellefinde mükellefiyet başlangıcı esastır.",
     "Yönetim kurulu üyesi ortakta seçilme tarihi esastır.",
     "Vergiden muaf esnafta sicile kayıt tarihi esastır.",
     "Köy muhtarında seçilme tarihi esastır."],
    "Md. 7/b'ye göre limited şirket ortaklarının sigortalılığı şirketin ticaret sicil memurluğunca tescil edildiği tarihten "
    "başlar.", zorluk="hard")

P.sayisal("SGK md. 11",
    "İşveren Bay (A) vefat etmiş ve işyeri miras yoluyla mirasçılarına intikal etmiştir."
    f"\n\n{K}, mirasçılar işyeri bildirgesini ölüm tarihinden itibaren en geç kaç ay içinde Kuruma vermelidir?",
    "3", ["1", "2", "6", "12"],
    "Md. 11'e göre işyerinin miras yoluyla intikali hâlinde mirasçılar ölüm tarihinden itibaren en geç üç ay içinde işyeri "
    "bildirgesini Kuruma verir.", zorluk="hard")

P.q("SGK md. 7",
    f"{K}, 4/a kapsamındaki sigortalılar için sigorta hak ve yükümlülükleri ne zaman başlar?",
    "Çalışmaya başladıkları tarihten",
    ["İşe giriş bildirgesinin verildiği tarihten",
     "İlk ücretin ödendiği tarihten",
     "Deneme süresinin bittiği tarihten",
     "İşyeri bildirgesinin onaylandığı tarihten"],
    "Md. 7/a'ya göre 4/a kapsamındakiler için sigorta hak ve yükümlülükleri çalışmaya, mesleki ve teknik eğitime, staja veya "
    "bursiyer olarak göreve başladıkları tarihten itibaren başlar.", zorluk="easy")

P.q("SGK md. 8",
    f"{K}, sigortalı işe giriş bildirgesinin verilme zamanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tarım işyerlerinde çalışmadan bir ay sonra verilebilir.",
    ["Kural olarak işe başlamadan önce verilir.",
     "İnşaat işyerlerinde en geç çalışmaya başlanan gün verilir.",
     "Balıkçılık işyerlerinde en geç işe başlanan gün verilir.",
     "Sigortalının kendini bildirmemesi aleyhine delil olmaz."],
    "Md. 8'e göre işe giriş bildirgesi kural olarak sigortalılık başlangıcından önce verilir; inşaat, balıkçılık ve tarım "
    "işyerlerinde en geç çalışmaya başlatıldığı gün verilir.")

P.sayisal("SGK md. 102",
    f"{K26}, idari para cezaları tebliğ tarihinden itibaren kaç gün içinde Kuruma ödenir veya aynı süre içinde Kuruma "
    "itiraz edilebilir?",
    "15", ["7", "10", "30", "60"],
    "Md. 102'ye göre idari para cezaları tebliğle tahakkuk eder; tebliğden itibaren on beş gün içinde ödenir veya aynı süre "
    "içinde Kuruma itiraz edilir. İtiraz takibi durdurur.")

P.q("SGK md. 9",
    f"{K}, hastalık ve analık hükümlerinin uygulanmasında sigortalılığın yitirilmesine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Takip eden onuncu günden itibaren yitirilir.",
    ["Sona erme tarihinde derhal yitirilir.",
     "Sona ermeden altı ay sonra yitirilir.",
     "Sadece ölüm hâlinde yitirilir.",
     "Grev süresince yitirilmiş sayılır."],
    "Md. 9'a göre hastalık ve analık hükümlerinin uygulanmasında sigortalılık, ücretsiz izin, grev veya lokavt hâllerinde "
    "bunların sona ermesini, diğer hâllerde sona erme tarihini takip eden onuncu günden başlanarak yitirilmiş sayılır.",
    zorluk="hard")

P.q("SGK md. 9",
    f"{K}, 4/b kapsamındaki sigortalılar için sigortalılığın sona ermesine ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Muhtarda seçim yılının sonu esas alınır.",
    ["Gelir vergisi mükellefinde faaliyete son verme tarihi esastır.",
     "Muaf esnafta sicil kaydının silinme tarihi esastır.",
     "Yönetim kurulu üyesi ortakta üyeliğin sona erdiği tarih esastır.",
     "Limited şirkette tüm hisse devrine karar tarihi esastır."],
    "Md. 9'a göre köy ve mahalle muhtarlarının sigortalılığı muhtarlık görevlerinin sona erdiği tarihten itibaren sona erer.")

P.sayisal("SGK md. 102",
    f"{K26}, idari para cezasına itirazı Kurumca reddedilen ilgili, kararın tebliğinden itibaren kaç gün içinde yetkili "
    "idare mahkemesine başvurabilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 102'ye göre Kurumca itirazı reddedilenler kararın tebliğinden itibaren otuz gün içinde yetkili idare mahkemesine "
    "başvurabilir; bu süre içinde başvurulmazsa ceza kesinleşir.")

P.q("SGK md. 11",
    f"{K}, işyeri ve işyeri bildirgesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bildirgenin verilmemesi sigortalıların haklarını ortadan kaldırır.",
    ["İşyeri bildirgesi en geç sigortalı çalıştırılan tarihte verilir.",
     "Yemek ve dinlenme yerleri işyerinden sayılır.",
     "Ticaret siciline yapılan kuruluş bildirimi Kuruma yapılmış sayılır.",
     "Aynı ilde adres değişikliği yazıyla bildirilebilir."],
    "Md. 11'e göre işyeri bildirgesinin verilmemesi veya geç verilmesi Kanunda belirtilen hak ve yükümlülükleri ortadan "
    "kaldırmaz.")

P.q("SGK md. 11",
    f"{K}, alt işveren, asıl işverenin işyerinde çalıştırdığı sigortalıları nasıl bildirir?",
    "Özel numarayla asıl işverenin dosyasından",
    ["Kendi işyeri adresine açtığı ayrı dosyadan",
     "Asıl işverenin sigortalısı gibi, özel numara almadan",
     "Asıl işverenin yazılı talimatıyla vergi dairesinden",
     "Her sigortalı için ayrı işyeri dosyası açarak"],
    "Md. 11'e göre alt işveren, asıl işverenle yaptığı sözleşmenin ibrazı kaydıyla Kurumdan alacağı özel bir numara ile "
    "sigortalıları asıl işverenin kayıtlı olduğu dosyadan bildirir.", zorluk="hard")

P.sayisal("SGK md. 102",
    f"{K26}, idari para cezaları kaç yıllık zamanaşımı süresine tabidir?",
    "10", ["2", "3", "5", "15"],
    "Md. 102'ye göre idari para cezaları on yıllık zamanaşımı süresine tabidir; süre fiilin işlendiği tarihten başlar.",
    zorluk="easy")

P.q("SGK md. 12",
    f"{K}, işveren ve işveren vekilinin sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşveren vekili işverenle birlikte sorumlu değildir.",
    ["Geçici iş ilişkisi kurulan işveren müteselsilen sorumludur.",
     "Asıl işveren, alt işverenle birlikte sorumludur.",
     "Kanundaki işveren deyimi işveren vekilini de kapsar.",
     "Tüzel kişiliği olmayan kuruluşlar da işveren olabilir."],
    "Md. 12'ye göre işveren vekili ve geçici iş ilişkisi kurulan işveren, bu Kanundaki yükümlülüklerden dolayı işverenle "
    "birlikte müştereken ve müteselsilen sorumludur.")

P.q("SGK md. 12",
    f"{K}, muhtasar ve prim hizmet beyannamesinin defter ve belgelere uygun olmamasından işverenle birlikte müştereken "
    "ve müteselsilen kim sorumludur?",
    "Yazılı sözleşmeyle yetkili meslek mensubu",
    ["İşyerinde çalışan sigortalılar",
     "İşyeri sendika temsilcisi",
     "İşyerinin bağlı olduğu vergi dairesi",
     "Beyannameyi alan Kurum personeli"],
    "Md. 12'ye göre beyannamenin defter, kayıt ve belgelere uygun olmamasından işverenlerle birlikte yazılı sözleşmeyle yetki "
    "verilmiş serbest muhasebeci, SMMM ve YMM'ler de müştereken ve müteselsilen sorumludur.")

P.sayisal("SGK md. 102",
    "Kurumun denetim ve kontrolle görevli memurunun tespitiyle, bir işverenin 4 sigortalı için işe giriş bildirgesi "
    f"vermediği anlaşılmıştır.\n\n{K26}, işverene uygulanacak idari para cezası aylık asgari ücretin kaç katıdır?",
    "8", ["2", "4", "10", "20"],
    "Md. 102/a-2'ye göre bildirgenin verilmediğinin denetimle anlaşılması hâlinde her bir sigortalı için asgari ücretin iki "
    "katı ceza uygulanır: 4 × 2 = 8 kat.", zorluk="hard")

P.q("SGK md. 13",
    f"{K}, aşağıdakilerden hangisi iş kazası sayılmaz?",
    "Kendi aracıyla tatile giderken olan kaza",
    ["İşverence sağlanan servisle işe giderken olan kaza",
     "Görevli gönderildiği yerde asıl işini yapmaksızın olan kaza",
     "Emziren sigortalının süt izni sırasında geçirdiği kaza",
     "Sigortalının işyerinde bulunduğu sırada geçirdiği kaza"],
    "Md. 13'e göre işyerinde bulunma, işverence sağlanan taşıtla gidiş-geliş, görevli gönderilme ve süt izni sırasında olan "
    "olaylar iş kazasıdır; kendi aracıyla tatile giderken olan kaza bu hâllerden değildir.", zorluk="easy")

P.q("SGK md. 13",
    f"{K}, iş kazasının bildirimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "4/b sigortalısı adına kazayı işveren bildirir.",
    ["İşveren kolluk kuvvetlerine derhal bildirir.",
     "İşveren Kuruma en geç üç iş günü içinde bildirir.",
     "Kaza işveren kontrolü dışında olduysa süre öğrenmeden başlar.",
     "Bildirim taahhütlü posta ile de yapılabilir."],
    "Md. 13'e göre 4/b kapsamındaki sigortalının iş kazası, bir ayı geçmemek şartıyla bildirim yapmaya engel hâlinin kalktığı "
    "günden sonra üç iş günü içinde kendisi tarafından bildirilir.")

P.sayisal("SGK md. 102",
    "Tespit tarihinden itibaren bir yıl içinde aynı işyerinde, denetimle 2 sigortalı için yine işe giriş bildirgesi "
    f"verilmediği anlaşılmıştır.\n\n{K26}, bu defa uygulanacak idari para cezası aylık asgari ücretin kaç katıdır?",
    "10", ["2", "4", "6", "20"],
    "Md. 102/a-3'e göre bir yıl içinde tekrar bildirge verilmediğinin anlaşılması hâlinde her bir sigortalı için asgari "
    "ücretin beş katı ceza uygulanır: 2 × 5 = 10 kat.", zorluk="hard")

P.q("SGK md. 14",
    f"{K}, meslek hastalığına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Meslek hastalığını işyeri hekimi tek başına belirler.",
    ["Kurum Sağlık Kurulunca tespit edilmesi zorunludur.",
     "Tekrarlanan bir sebeple uğranan hastalıktır.",
     "İşten ayrıldıktan sonra da ortaya çıkabilir.",
     "Liste dışı hastalıklarda Yüksek Sağlık Kurulu karar verir."],
    "Md. 14'e göre sigortalının meslek hastalığına tutulduğunun Kurum Sağlık Kurulu tarafından tespit edilmesi zorunludur; "
    "işyeri hekimi bu tespiti tek başına yapamaz.")

P.q("SGK md. 59",
    f"{K}, Kurumun denetim ve kontrolle görevli memurlarının düzenlediği tutanaklar hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Aksi sabit oluncaya kadar geçerlidir.",
    ["Mahkeme onayıyla geçerlilik kazanır.",
     "Sadece işveren imzalarsa geçerlidir.",
     "Yeminle desteklenmedikçe delil sayılmaz.",
     "Bir yıl içinde geçerliliğini yitirir."],
    "Md. 59'a göre denetim memurlarının tespitleri yemin hariç her türlü delile dayandırılabilir ve düzenledikleri tutanaklar "
    "aksi sabit oluncaya kadar geçerlidir.")

P.sayisal("SGK md. 102",
    f"{K26}, Kurumun denetim memurlarının görevini yapmasına engel olanlara, eylemleri başka bir suç oluştursa dahi "
    "asgari ücretin kaç katı tutarında idari para cezası uygulanır?",
    "5", ["1", "2", "3", "10"],
    "Md. 102'ye göre denetim memurlarının inceleme ve soruşturma görevlerine engel olanlara asgari ücretin beş katı, cebir ve "
    "tehdit kullananlara ayrıca on katı tutarında idari para cezası uygulanır.")

P.q("SGK md. 59",
    f"{K}, denetim ve kontrole ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetim memurları İş Kanunu teftiş yetkisine sahip değildir.",
    ["Tespitler yemin hariç her türlü delile dayandırılabilir.",
     "Kamu görevlileri denetim memurlarına yardımcı olur.",
     "İşverenler istenen defter ve belgeleri getirip gösterir.",
     "Askerî işyerlerini askerî iş müfettişleri de denetleyebilir."],
    "Md. 59'a göre Kurumun denetim ve kontrolle görevli memurları, Kanunun uygulanması bakımından 4857 sayılı İş Kanunundaki "
    "denetim, teftiş ve kontrol yetkisini de haizdir.", zorluk="hard")

P.q("SGK md. 59",
    f"{K}, ihaleli işlerde ilişiksizlik belgesi verilmesinde işçilik tutarlarının uygunluğunu inceleyerek rapor "
    "düzenleyebilecek meslek mensupları kimlerdir?",
    "Yetkili SMMM ve yeminli mali müşavirler",
    ["Serbest muhasebeciler ve avukatlar",
     "Bağımsız denetçiler ve noterler",
     "Vergi müfettişleri ve iş müfettişleri",
     "Sadece yeminli mali müşavirler"],
    "Md. 59'a göre ilişiksizlik belgesi verilmesinde 3568 sayılı Kanuna göre yetkili serbest muhasebeci mali müşavirler ile "
    "yeminli mali müşavirlerin işyeri kayıtlarını inceleyerek bildirdiği işçilik tutarları esas alınabilir.")

P.sayisal("SGK md. 3",
    f"{K}, yüksek öğrenim gören ve evli olmayan çocuk, genel sağlık sigortalısının bakmakla yükümlü olduğu kişi olarak "
    "kaç yaşını doldurana kadar kabul edilir?",
    "25", ["18", "20", "22", "26"],
    "Md. 3/10'a göre çocuklar 18 yaşını, lise ve dengi öğrenimde 20 yaşını, yüksek öğrenimde 25 yaşını doldurmamış ve evli "
    "olmamak koşuluyla bakmakla yükümlü olunan kişidir; malul evli olmayan çocukta yaş aranmaz.")

P.q("SGK md. 59",
    f"{K}, gerçeğe aykırı rapor düzenleyen serbest muhasebeci mali müşavir ve yeminli mali müşavirlerin sorumluluğu "
    "hakkında aşağıdakilerden hangisi doğrudur?",
    "İşverenle müteselsilen sorumludur.",
    ["Sadece disiplin cezası alırlar.",
     "Kurum zararından sorumlu tutulamazlar.",
     "Sorumluluk sadece işverene aittir.",
     "Zararın yarısından sorumlu olurlar."],
    "Md. 59'a göre gerçeğe aykırı rapor düzenleyen SMMM ve YMM'ler Kurumun uğradığı zarardan işverenle birlikte müştereken ve "
    "müteselsilen sorumludur.")

P.q("SGK md. 102",
    f"{K26}, idari para cezalarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mahkemeye başvuru tahsili durdurur.",
    ["Kuruma itiraz takibi durdurur.",
     "Cezalar tebliğ ile tahakkuk eder.",
     "Zamanaşımı fiilin işlendiği tarihte başlar.",
     "Hüküm yoksa Kabahatler Kanunu uygulanır."],
    "Md. 102'ye göre Kuruma itiraz takibi durdurur; ancak mahkemeye başvurulması idari para cezasının takip ve tahsilini "
    "durdurmaz.")

P.sayisal("SGK md. 3",
    f"{K}, lise ve dengi öğrenim gören evli olmayan çocuk, bakmakla yükümlü olunan kişi olarak kaç yaşını doldurana "
    "kadar kabul edilir?",
    "20", ["16", "18", "22", "25"],
    "Md. 3/10'a göre lise ve dengi öğrenim veya mesleki eğitim gören evli olmayan çocuklar 20 yaşını doldurana kadar bakmakla "
    "yükümlü olunan kişidir.")

P.q("SGK md. 102",
    f"{K26}, idari para cezasının tebliğden itibaren on beş gün içinde, itiraz ve yargı yoluna başvurulmadan peşin "
    "ödenmesi hâlinde aşağıdakilerden hangisi doğrudur?",
    "Cezanın dörtte üçü tahsil edilir.",
    ["Cezanın yarısı tahsil edilir.",
     "Cezanın tamamı tahsil edilir.",
     "Cezanın dörtte biri tahsil edilir.",
     "Yargı yoluna başvurma hakkı düşer."],
    "Md. 102'ye göre idari para cezalarının itiraz veya yargı yoluna başvurulmadan önce tebliğden itibaren on beş gün içinde "
    "peşin ödenmesi hâlinde dörtte üçü tahsil edilir; peşin ödeme yargı yoluna başvurma hakkını etkilemez.")

P.q("SGK md. 102",
    "İşveren, süresi geçtikten sonra ve herhangi bir tespit olmaksızın işe giriş bildirgesini kendiliğinden 20 gün içinde "
    f"vermiş, cezayı da tebliğden itibaren 15 gün içinde ödemiştir.\n\n{K26}, uygulanacak ceza hakkında aşağıdakilerden "
    "hangisi doğrudur?",
    "Ceza dörtte bir oranında uygulanır.",
    ["Ceza iki katı olarak uygulanır.",
     "Ceza tam olarak uygulanır.",
     "Ceza yarı oranında uygulanır.",
     "Ceza beş katı olarak uygulanır."],
    "Md. 102'nin ikinci fıkrasına göre bildirge yasal süreden sonra kendiliğinden 30 gün içinde verilir ve ceza tebliğden "
    "itibaren 15 gün içinde ödenirse (a), (b), (g), (h) ve (j) bentlerindeki cezalar dörtte bir oranında uygulanır.",
    zorluk="hard")

P.sayisal("SGK md. 6",
    f"{K}, ev hizmetlerinde ücretle aynı kişi yanında ay içinde en az kaç gün çalışanlar sigortalı sayılır?",
    "10", ["5", "7", "15", "20"],
    "Md. 6/c'ye göre ev hizmetlerinde çalışanlar sigortalı sayılmaz; ancak ücretle aynı kişi yanında ay içinde on gün ve daha "
    "fazla süreyle çalışanlar bu istisnanın dışındadır.", zorluk="hard")

P.q("SGK md. 102",
    f"{K26}, işyeri bildirgesini süresinde vermeyen işverenlere uygulanacak idari para cezasına ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Bilanço esasında defter tutanlara asgari ücretin üç katı",
    ["Bilanço esasında defter tutanlara asgari ücretin on katı",
     "Defter tutmayanlara asgari ücretin iki katı",
     "İşletme defteri tutanlara asgari ücretin beş katı",
     "Tüm işverenlere aynı tutarda asgari ücretin yarısı"],
    "Md. 102/b'ye göre işyeri bildirgesini süresinde vermeyen kamu idareleri ve bilanço esasına göre defter tutanlara asgari "
    "ücretin üç katı, diğer defterleri tutanlara iki katı, defter tutmayanlara bir aylık asgari ücret tutarında ceza "
    "uygulanır.", zorluk="hard")

P.q("SGK md. 102",
    f"{K26}, idari para cezalarına itiraz sürecine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Reddedilirse idare mahkemesine gidilir.",
    ["İtiraz doğrudan vergi mahkemesine yapılır.",
     "Kuruma itiraz takibi durdurmaz.",
     "İtiraz süresi tebliğden itibaren altmış gündür.",
     "Reddedilen itiraz için asliye hukuka gidilir."],
    "Md. 102'ye göre tebliğden itibaren on beş gün içinde Kuruma itiraz edilebilir; itiraz takibi durdurur ve itirazı "
    "reddedilenler otuz gün içinde yetkili idare mahkemesine başvurabilir.")

P.sayisal("SGK md. 6",
    "Yabancı ülkede kurulu bir şirket, yabancı ülkede sosyal sigortaya tabi olduğunu belgeleyen çalışanını bir iş için "
    f"Türkiye’ye göndermiştir.\n\n{K}, bu kişi en çok kaç ay süreyle Türkiye’de sigortalı sayılmaz?",
    "3", ["1", "2", "6", "12"],
    "Md. 6/e'ye göre yabancı ülkede kurulu kuruluş tarafından Türkiye'ye üç ayı geçmemek üzere bir iş için gönderilen ve "
    "yabancı ülkede sosyal sigortaya tabi olduğunu belgeleyenler sigortalı sayılmaz.")

P.q("SGK md. 8",
    f"{K}, işe giriş bildirgesiyle ilgili yükümlülüklere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sigortalının kendini bildirmemesi aleyhine delil olmaz.",
    ["Bildirim yükümlülüğü sadece sigortalıya aittir.",
     "Kamu idareleri sigortasız kişiyi bildirmekle yükümlü değildir.",
     "İşveren bildirgeyi işe başladıktan üç ay sonra verir.",
     "Bildirge verilmezse sigortalılık kural olarak başlamaz."],
    "Md. 8'e göre sigortalılar çalışmaya başladıklarını bir ay içinde Kuruma bildirir; ancak sigortalının kendini bildirmemesi "
    "sigortalı aleyhine delil teşkil etmez.")

P.q("SGK md. 6",
    f"{K}, tarımda kendi adına ve hesabına bağımsız çalışanlardan hangisi talebi hâlinde sigortalı sayılmaz?",
    "65 yaşını doldurmuş olan",
    ["Tarımsal geliri yüksek olan", "Kooperatif ortağı olan", "Yirmi yaşında olan", "Hayvancılık yapan"],
    "Md. 6/ı'ya göre tarımda bağımsız çalışanlardan net aylık tarımsal geliri prime esas günlük kazanç alt sınırının otuz "
    "katından az olduğunu belgeleyenler ile 65 yaşını dolduranlardan talepte bulunanlar sigortalı sayılmaz.", zorluk="hard")

P.sayisal("SGK md. 102",
    "Bir işyeri sahibi, Kurumun denetim memurunun görevini yapmasını engellemek amacıyla cebir ve tehdit kullanmıştır."
    f"\n\n{K26}, bu kişiye ceza kovuşturmasından ayrı olarak asgari ücretin kaç katı tutarında idari para cezası uygulanır?",
    "10", ["2", "3", "5", "20"],
    "Md. 102'ye göre denetim memurlarının görevini engellemek amacıyla cebir ve tehdit kullananlar TCK md. 265/2'ye göre "
    "cezalandırılır; ayrıca asgari ücretin on katı tutarında idari para cezası uygulanır.", zorluk="hard")

P.q("SGK md. 3",
    f"{K}, bakmakla yükümlü olunan kişiye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Evli çocuk da bakmakla yükümlü olunan kişidir.",
    ["Malul, evli olmayan çocukta yaş aranmaz.",
     "Ana ve babada geçimin sigortalıca sağlanması aranır.",
     "Kendi sigortalılığıyla aylık alan eş bu kapsamda değildir.",
     "Yüksek öğrenim gören çocukta yaş sınırı yirmi beştir."],
    "Md. 3/10'a göre çocukların bakmakla yükümlü olunan kişi sayılması için evli olmamaları şarttır.")

P.q("SGK md. 13",
    f"{K}, bir olayın iş kazası sayılıp sayılmayacağına ilişkin soruşturmayı kimler yapabilir?",
    "Kurum denetim memurları veya iş müfettişleri",
    ["Sadece işyeri hekimi",
     "İşyeri sendika temsilcisi",
     "Cumhuriyet savcılığı ve belediye zabıta müdürlüğü",
     "Sadece işveren vekili"],
    "Md. 13'e göre olayın iş kazası sayılıp sayılmayacağına karar vermek için gerektiğinde Kurumun denetim ve kontrolle "
    "yetkilendirilen memurları veya Bakanlık iş müfettişleri soruşturma yapabilir.")

P.q("SGK md. 13",
    "Soruşturma sonunda, işveren tarafından iş kazası olarak bildirilen olayın gerçekte iş kazası olmadığı ve bildirimin "
    f"gerçeğe aykırı olduğu anlaşılmıştır.\n\n{K}, Kurumca yersiz yapılan ödemeler hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Bildirimi yapandan tahsil edilir.",
    ["Sigortalıdan faizsiz olarak geri alınır.",
     "Kurum zararı olarak silinir.",
     "Sadece sigortalının hak sahiplerinden alınır.",
     "Ödemeler Hazine tarafından karşılanır."],
    "Md. 13'e göre olayın iş kazası olmadığı anlaşılırsa Kurumca yersiz yapılan ödemeler, ödeme tarihinden itibaren gerçeğe "
    "aykırı bildirimde bulunanlardan md. 96'ya göre tahsil edilir.")

P.q("SGK md. 14",
    f"{K}, meslek hastalığını bildirmeyen veya kasten yanlış bildiren işverene ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Masraflar işverene rücu edilir.",
    ["İşverenin sorumluluğu doğmaz.",
     "Sigortalının hakları düşer.",
     "Masraflar sigortalıdan tahsil edilir.",
     "Sadece uyarı cezası verilir."],
    "Md. 14'e göre bildirim yükümlülüğünü yerine getirmeyen veya kasten eksik ya da yanlış bildiren işverene, Kurumca yapılan "
    "masraflar ile ödenmişse geçici iş göremezlik ödenekleri rücu edilir.")

P.q("SGK md. 12",
    f"{K}, alt işveren tanımı ve asıl işverenin sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Asıl işveren birlikte sorumludur.",
    ["Asıl işveren kural olarak sorumlu değildir.",
     "Sorumluluk sadece alt işverene aittir.",
     "Alt işveren sadece ilk yıl sorumludur.",
     "Sigortalılar alt işverenin işçisi sayılmaz."],
    "Md. 12'ye göre sigortalılar üçüncü kişi aracılığıyla işe girmiş olsalar dahi asıl işveren, Kanunun işverene yüklediği "
    "yükümlülüklerden dolayı alt işveren ile birlikte sorumludur.", zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
