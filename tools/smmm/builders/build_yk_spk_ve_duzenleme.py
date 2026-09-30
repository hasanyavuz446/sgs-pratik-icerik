# -*- coding: utf-8 -*-
"""SPK Mevzuatı · SPK ve Düzenleme — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · 6362 s. Sermaye Piyasası Kanunu m. 3/v, 35, 37-45, 62-76, 87-98, 117-135
  · Yatırım Hizmetleri ve Faaliyetleri ile Yan Hizmetlere İlişkin Esaslar Hakkında Tebliğ (III-37.1)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_spk_ve_duzenleme_2026.json", lesson="sermaye_piyasasi_ve_finans", topic="spk_ve_duzenleme",
          konu_adi="SPK ve Düzenleme", seed=2026092825,
          surum="6362 s. Sermaye Piyasası Kanunu; Yatırım Hizmetleri ve Faaliyetleri Tebliği (III-37.1); 28.09.2026 kontrolü")

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"
YH = "Yatırım Hizmetleri ve Faaliyetleri ile Yan Hizmetlere İlişkin Esaslar Hakkında Tebliğ (III-37.1)’e göre"

# ================================================================ Kurulun yapısı (m. 117-135)
P.q("6362 s. SPKn m. 117",
    f"{K}, Sermaye Piyasası Kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurulun kararları Bakanlıkça yerindelik denetimine tabi tutulabilir.",
    ["Kurul kamu tüzel kişiliğini haiz, idari ve mali özerkliğe sahiptir.",
     "Kurulun merkezi İstanbul’dadır.",
     "Kurul, Kurul Karar Organı ve Başkanlık teşkilatından oluşur.",
     "Kurulun para, evrak ve her türlü malları devlet malı hükmündedir."],
    "Kanun m. 117'ye göre Kurul kamu tüzel kişiliğini haiz, idari ve mali özerkliğe sahiptir; merkezi İstanbul'dadır ve Kurul "
    "Karar Organı ile Başkanlık teşkilatından oluşur. Kurulun kararları yerindelik denetimine tabi tutulamaz ve hiçbir merci "
    "karar almaya yönelik talimat veremez; malları devlet malı hükmündedir.", zorluk="easy")

P.sayisal("6362 s. SPKn m. 118",
    f"{K}, biri başkan, biri ikinci başkan olmak üzere Kurul Karar Organı kaç üyeden oluşur?",
    "7", ["5", "9", "11", "15"],
    "Kanun m. 118'e göre Kurul Karar Organı biri başkan, biri ikinci başkan olmak üzere yedi üyeden oluşur; Kurul Başkanı "
    "Başkanlık teşkilatının da başıdır.", zorluk="easy")

P.q("6362 s. SPKn m. 119-120",
    f"{K}, Kurul Başkan ve üyelerinin atanmasına ve göreve başlamasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üyeler, ilgili Bakan huzurunda yemin ederek göreve başlar.",
    ["Başkan, ikinci başkan ve üyeler Cumhurbaşkanınca atanır.",
     "Üyelerin en az lisans düzeyinde öğrenim görmüş olması gerekir.",
     "Yemin etmedikçe göreve başlamış sayılmazlar.",
     "Boşalan üyeliğe en geç iki ay içinde atama yapılır."],
    "Kanun m. 119'a göre Başkan ve üyeler Cumhurbaşkanınca atanır, en az lisans mezunu olmalıdır ve Yargıtay Birinci Başkanlık "
    "Kurulu huzurunda yemin ederler; yemin etmedikçe göreve başlamış sayılmazlar. m. 120'ye göre boşalan üyeliğe en geç iki "
    "ay içinde atama yapılır.")

P.q("6362 s. SPKn m. 121/1",
    f"{K}, Kurul Başkan ve üyelerinin görevleri süresince uyacakları yasaklara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurulun denetlediği ortaklıklarda pay sahibi olabilirler.",
    ["Asli görevlerini aksatmamak kaydıyla bilimsel yayın yapabilir ve telif alabilirler.",
     "Ticaretle uğraşamaz ve serbest meslek faaliyetinde bulunamazlar.",
     "Hakemlik ve bilirkişilik yapamazlar.",
     "Dernek, vakıf ve kooperatiflerde yöneticilik yapamazlar."],
    "Kanun m. 121/1'e göre Başkan ve üyeler bilimsel yayın yapabilir, ders ve konferans verebilir; ancak başka görev alamaz, "
    "dernek ve vakıflarda yöneticilik yapamaz, ticaretle uğraşamaz, serbest meslek faaliyetinde bulunamaz, Kurulun düzenlediği "
    "ve denetlediği ortaklıklarda pay sahibi olamaz, hakemlik ve bilirkişilik yapamaz.")

P.sayisal("6362 s. SPKn m. 121/2",
    "Kurul üyeliğine atanan bir kişinin portföyünde, Kurulun düzenlediği bir ortaklığın payları bulunmaktadır. "
    f"{K}, bu kişi göreve başladığı tarihten itibaren söz konusu payları kaç gün içinde elden çıkarmalıdır?",
    "30", ["7", "15", "60", "90"],
    "Kanun m. 121/2'ye göre Başkan ve üyeler göreve başlamalarından itibaren kendilerinin, eşlerinin ve velayet altındaki "
    "çocuklarının sahip olduğu, Kurulun düzenlediği kuruluşların sermaye piyasası araçlarını (Hazine borçlanma araçları ve "
    "emeklilik fonu payları hariç) otuz gün içinde yakınları dışındakilere satmak zorundadır; aksi hâlde üyelikten çekilmiş sayılır.")

P.q("6362 s. SPKn m. 121/4, 6",
    "Kurul üyeliği görevi sona eren bir kişiye, ayrılmasından bir yıl sonra bir aracı kurumda genel müdürlük teklif edilmiştir. "
    f"{K}, bu teklife ilişkin aşağıdakilerden hangisi doğrudur?",
    "İzleyen iki yıl dolmadan yatırım kuruluşunda görev alamaz.",
    ["Görevden ayrıldığı için herhangi bir kısıtlamaya tabi değildir.",
     "Kurulun izniyle hemen görev alabilir.",
     "Sadece üyelik süresince incelediği kuruluşlarda görev alamaz.",
     "Görevden ayrılmayı izleyen beş yıl boyunca yatırım kuruluşunda görev alamaz."],
    "Kanun m. 121/4'e göre Kurul Başkan ve üyeleri görevden ayrılmalarını izleyen iki yıl içinde yatırım kuruluşlarında görev "
    "alamaz; aykırılıkta 2531 sayılı Kanundaki cezalar uygulanır. m. 121/6 meslek personeli için ayrıca son iki yılda "
    "denetledikleri kuruluşlarda iki yıl görev alma yasağı öngörür.")

P.q("6362 s. SPKn m. 123",
    f"{K}, Kurul Karar Organının çalışma esaslarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üyeler çekimser oy kullanabilir.",
    ["Karar Organının en az iki haftada bir toplanması esastır.",
     "Karar Organı en az beş üyeyle toplanır.",
     "Kararlar en az dört üyenin aynı yöndeki oyuyla alınır.",
     "Karar Organı toplantılarının gizliliği esastır."],
    "Kanun m. 123'e göre Karar Organı en az iki haftada bir gündemli toplanır, en az beş üyeyle toplanır ve en az dört üyenin "
    "aynı yöndeki oyuyla karar alır. Üyeler çekimser oy kullanamaz; eşitlikte Başkanın oyu belirleyicidir ve toplantıların "
    "gizliliği esastır.")

P.sayisal("6362 s. SPKn m. 123/2",
    f"{K}, görev, izin ve hastalık gibi geçerli bir mazereti olmaksızın bir takvim yılında toplam kaç toplantıya katılmayan "
    "Kurul üyesi üyelikten çekilmiş sayılır?",
    "5", ["2", "3", "7", "10"],
    "Kanun m. 123/2'ye göre geçerli mazereti olmaksızın bir takvim yılında toplam beş toplantıya katılmayan Kurul üyesi "
    "üyelikten çekilmiş sayılır; durum Kurul kararıyla tespit edilir ve ilgili Bakana bildirilir.")

P.q("6362 s. SPKn m. 123/4",
    "Kurul Karar Organının gündeminde, bir üyenin kardeşinin yönetim kurulu başkanı olduğu bir aracı kurum hakkında tedbir "
    f"kararı bulunmaktadır. {K}, bu üyenin durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Üye müzakere ve oylamaya katılamaz ve bu durum karar metninde belirtilir.",
    ["Üye müzakereye katılabilir, ancak oylamada çekimser kalır.",
     "Kardeşlik ilişkisi yasak kapsamında olmadığından üye oylamaya katılabilir.",
     "Üyenin katılıp katılmayacağına Kurul Başkanı karar verir.",
     "Üye oylamaya katılır, ancak oyu karar yeter sayısında dikkate alınmaz."],
    "Kanun m. 123/4'e göre Kurul Başkan ve üyeleri kendileri, eşleri, evlatlıkları ve üçüncü derece dahil kan ve ikinci derece "
    "dahil kayın hısımlarıyla ilgili konularda müzakere ve oylamaya katılamaz; bu durum karar metninde ayrıca belirtilir. "
    "Kardeş ikinci derece kan hısımıdır.")

P.oncul("6362 s. SPKn m. 122/2, 128/1",
    "Kurul Karar Organının aşağıdaki yetkileri değerlendirilmektedir:",
    ["Yabancı muadil kurumlarla karşılıklı bilgi değişimi için mutabakat zaptı imzalamak",
     "Yönetmelik ve tebliğ taslaklarını görüşüp karara bağlamak",
     "Sermaye piyasalarına ilişkin bilimsel araştırmalar yaptırmak",
     "Kurulun bütçesini ve kesin hesabını karara bağlamak"],
    f"{K}, yukarıdaki yetkilerden hangileri kapsamı açıkça belirtilmek ve yazılı olmak kaydıyla Kurul Başkanına devredilebilir?",
    "I ve III", ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 122/2'ye göre Karar Organı, m. 128/1'deki (d) yabancı kurumlarla iş birliği ve mutabakat, (e) yeni kurum ve "
    "araçlara ilişkin düzenleme ve (ı) bilimsel araştırma yaptırma yetkilerini yazılı olarak Başkana devredebilir. Düzenleyici "
    "işlem taslakları ile bütçe ve kesin hesap Karar Organının devredilemeyen görevleridir.", zorluk="hard")

P.q("6362 s. SPKn m. 129",
    f"{K}, Kurulun şeffaflık ve hesap verebilirliğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurul, yılda en az bir defa TBMM Plan ve Bütçe Komisyonuna bilgi verir.",
    ["Yıllık faaliyet raporu izleyen yılın mart ayı sonuna kadar Resmî Gazete’de yayımlanır.",
     "Kurul, faaliyetleri hakkında sadece Cumhurbaşkanlığına bilgi verir.",
     "Kurulun yaptığı düzenlemelerin güncel metinlerini yayımlama zorunluluğu yoktur.",
     "Faaliyet raporu Kurulun onayından sonra Sayıştayca kamuoyuna duyurulur."],
    "Kanun m. 129'a göre yıllık faaliyet raporu izleyen yılın haziran ayı sonuna kadar Kurulun internet sitesinde yayınlanır "
    "ve ilgili Bakana gönderilir; Kurul yılda en az bir defa TBMM Plan ve Bütçe Komisyonuna bilgi verir ve düzenlemeleri "
    "güncel hâliyle internet sitesinde yayımlar.")

P.q("6362 s. SPKn m. 133, 134",
    "Kurulun bir meslek personeli hakkında, yürüttüğü denetimle bağlantılı bir suç iddiası ileri sürülmüştür. "
    f"{K}, bu personel hakkında soruşturma yapılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Soruşturma, Kurul Başkanının izin vermesi kaydıyla genel hükümlere göre yapılır.",
    ["Soruşturma için ilgili Bakanın izni gerekir.",
     "Soruşturma izni Kurul Karar Organının oybirliğiyle verilir.",
     "Kurul personeli hakkında görevleriyle bağlantılı suçlardan soruşturma yapılamaz.",
     "Soruşturma Danıştay tarafından yürütülür."],
    "Kanun m. 133'e göre Kurul Başkan ve üyeleri ile personelin görevleriyle bağlantılı suçlarına ilişkin soruşturmalar, "
    "Başkan ve üyeler için ilgili Bakanın, personel için Başkanın izni kaydıyla genel hükümlere göre yapılır; üyelerle "
    "iştirak hâlinde işlenen suçlarda personel için izin yetkisi Bakana aittir.")

P.q("6362 s. SPKn m. 134",
    f"Bir aracı kurum, faaliyet izninin iptaline ilişkin Kurul kararına karşı dava açmak istemektedir. {K}, bu davaya ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Dava idare mahkemesinde görülür ve acele işlerden sayılır.",
    ["Dava asliye ticaret mahkemesinde görülür.",
     "Dava doğrudan Danıştayda ilk derece mahkemesi olarak görülür.",
     "Dava açılmadan önce Kurula itiraz edilmesi zorunludur.",
     "Dava tüketici mahkemesinde görülür."],
    "Kanun m. 134'e göre Kurul kararlarına karşı açılacak idari davalar idare mahkemelerinde görülür ve Kurul kararlarına "
    "karşı yapılan başvurular acele işlerden sayılır.", zorluk="easy")

P.sayisal("6362 s. SPKn m. 130/3",
    "Nominal değeri 50 milyon TL olan paylar, Kurul onaylı izahname ile 80 milyon TL ihraç değeri üzerinden halka arz "
    f"edilecektir. {K} öngörülen kanuni oranın uygulandığı varsayımıyla, ihraççının Kurul bütçesine yatıracağı ücret kaç TL’dir?",
    "240.000", ["150.000", "400.000", "800.000", "2.400.000"],
    "Kanun m. 130/3'e göre ihraççılar veya halka arz edenler, satışı yapılacak araçların varsa nominal değerinden aşağı olmamak "
    "üzere ihraç değerinin binde üçü tutarında ücret yatırır: 80.000.000 × 3 / 1.000 = 240.000 TL. Kurul Karar Organı daha "
    "düşük oran, Cumhurbaşkanı kanuni oranın iki katına kadar artırma belirleyebilir.", zorluk="hard")

P.q("6362 s. SPKn m. 128/1-k",
    "Halka açık bir ortaklığın yönetim kurulu üyelerinin çoğunluğunun görev süresi dolmuş, toplantı yeter sayısı "
    f"sağlanamamış ve genel kurul otuz gün içinde yeni üye seçememiştir. {K}, bu durumda Kurulun yetkisi aşağıdakilerden hangisidir?",
    "Bağımsızlık kriterlerini sağlayan yeter sayıda yönetim kurulu üyesini resen atamak",
    ["Ortaklığın tasfiyesine karar vermek",
     "Ortaklığın paylarının borsada işlem görmesini sürekli olarak durdurmak",
     "Genel kurul yerine yönetim kurulunu doğrudan Yatırımcı Tazmin Merkezine devretmek",
     "Görev süresi dolan üyelerin görevlerini sona erdirerek ortaklığı temsilcisiz bırakmak"],
    "Kanun m. 128/1-k'ye göre görev süresi dolan veya boşalan üyeliklerin yerine otuz gün içinde genel kurulca seçim "
    "yapılamazsa Kurul, toplantı yeter sayısını sağlayacak asgari sayıda bağımsızlık kriterlerini sağlayan üyeyi resen atar; "
    "atamaya kadar süresi dolan üyeler görevine devam eder.", zorluk="hard")

# ================================================================ denetim ve arama (m. 87-90)
P.q("6362 s. SPKn m. 88-89",
    f"{K}, Kurulun denetim faaliyetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Görevli personel denetlenenlerin vergi kayıtlarını inceleyemez.",
    ["Denetim yetkisi Kurul Başkanınca görevlendirilen meslek personelince kullanılır.",
     "Kurul Başkanı program dışında da denetim yaptırabilir.",
     "İlgililer denetim sırasında düzenlenen tutanakları imzalamakla yükümlüdür.",
     "İmzadan kaçınılırsa bunun sebepleri tutanakta açıkça belirtilir."],
    "Kanun m. 88'e göre denetim yetkisi Başkanca görevlendirilen meslek personelince kullanılır ve Başkan program dışı denetim "
    "yaptırabilir. m. 89'a göre personel vergi kayıtları dahil tüm defter, belge ve elektronik kayıtları inceleyebilir; "
    "ilgililer tutanakları imzalamakla yükümlüdür, imzadan kaçınma sebepleri tutanağa yazılır.", zorluk="easy")

P.q("6362 s. SPKn m. 89/3",
    "Kurul denetim elemanları, bir şirketin iş yerinde bulunan ve incelenmesi gereken belgelere ulaşmak için arama yapılmasını "
    f"gerekli görmektedir. {K}, aramanın yapılabilmesi için aşağıdakilerden hangisi gerekir?",
    "Kurul Başkanının talebi ve sulh ceza hâkiminin kararı",
    ["Denetim elemanının doğrudan kolluk görevlilerine başvurması",
     "Kurul Karar Organının kararı",
     "Cumhuriyet savcısının yazılı emri, hâkim kararı aranmaksızın",
     "İlgili Bakanın izni ve Kurul Başkanının onayı"],
    "Kanun m. 89/3'e göre Kurul Başkanının talepte bulunması ve sulh ceza hâkiminin kararı üzerine gerekli yerlerde kolluk "
    "yardımıyla arama yapılabilir; bulunan defter ve belgeler ayrıntılı tutanakla tespit edilir, yerinde incelenemeyenler "
    "muhafaza altına alınarak sevk edilir.")

P.q("6362 s. SPKn m. 87",
    f"{K}, veri depolama kuruluşlarına ve bildirim yükümlülüğüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Veri depolama kuruluşundaki bilgiler kamu kurumlarıyla Kurul onayı aranmaksızın paylaşılabilir.",
    ["Kurul, sistemik riskin gözetimi amacıyla işlem bilgilerinin kendisine bildirilmesini isteyebilir.",
     "Bildirimin Kurulun yetkilendireceği bir veri depolama kuruluşuna yapılması istenebilir.",
     "Bildirim yükümlüleri özel mevzuattaki sır saklama hükümlerini ileri süremez.",
     "Kurul, finansal işlem yapanların tanımlayıcı bir kod almasını zorunlu tutabilir."],
    "Kanun m. 87'ye göre Kurul sistemik risk ve finansal istikrar amacıyla işlem bilgilerinin kendisine veya yetkilendireceği "
    "veri depolama kuruluşuna bildirilmesini isteyebilir; yükümlüler gizlilik ileri süremez ve tanımlayıcı kod zorunlu "
    "tutulabilir. Bilgilerin kamu tüzel kişileri dahil üçüncü kişilerle paylaşımı Kurul onayına tabidir.")

# ================================================================ tedbirler (m. 91-98)
P.sayisal("6362 s. SPKn m. 91/2",
    "Kurul, bir şirketin izahname olmaksızın halktan para toplayarak Kanuna aykırı ihraç yaptığını tespit etmiştir. "
    f"{K}, Kurul sonuçların ortadan kaldırılması için ihracı yapana tespit tarihinden itibaren kaç gün içinde yazılı ihbarda bulunur?",
    "30", ["7", "15", "60", "90"],
    "Kanun m. 91/2'ye göre Kurul, Kanuna aykırı ihracın sonuçlarının ortadan kaldırılması ve varlıkların iadesi için tespit "
    "tarihinden itibaren otuz gün içinde yazılı ihbarda bulunur; muhatap da ihbardan itibaren otuz gün içinde para "
    "topladığı kişileri ve tutarları ilan eder.")

P.q("6362 s. SPKn m. 91",
    f"{K}, Kanuna aykırı ihraçlarda uygulanacak tedbirlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Para toplananlar ilanı takip eden üç ay içinde asliye ceza mahkemesine itiraz edebilir.",
    ["Kurul, her türlü harç ve teminattan muaf olarak ihtiyati tedbir ve ihtiyati haciz isteyebilir.",
     "Muhatap, ihbardan itibaren otuz gün içinde para topladığı kişileri ve tutarları ilan eder.",
     "Hak sahiplerine iade tamamlanmadan ihtiyati tedbir ve haciz kaldırılamaz.",
     "İhbardan itibaren bir yıl içinde sonuçlar giderilmezse Kurul tasfiye davası açabilir."],
    "Kanun m. 91'e göre Kurul harç ve teminattan muaf olarak ihtiyati tedbir ve haciz isteyebilir; muhatap otuz gün içinde "
    "ilan yapar, ilanı izleyen üç ay içinde para toplananlar ortaklığın bulunduğu yer asliye hukuk mahkemesine itiraz "
    "edebilir. İade tamamlanmadan tedbirler kalkmaz; bir yılda sonuçlar giderilmezse iade veya tasfiye davası açılabilir.",
    zorluk="hard")

P.sayisal("6362 s. SPKn m. 91/3",
    "Halka arzdan elde edilen fonun izahnamede taahhüt edilen yatırımlar yerine ortakların ilişkili şirketlerine aktarıldığı "
    f"tespit edilmiştir. {K}, Kurulun bu işlemin iptali için açabileceği dava, her hâlde izahnamenin onay tarihinden itibaren "
    "kaç yıl içinde açılmalıdır?",
    "2", ["1", "3", "5", "10"],
    "Kanun m. 91/3'e göre Kurul, ihraçtan elde edilen tutarın izahnameye aykırı kullanılması sonucunu doğuran işlemlerin iptali "
    "ve varlıkların iadesi için tespit tarihinden itibaren üç ay ve her hâlde izahnamenin onay tarihinden itibaren iki yıl "
    "içinde dava açabilir.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 92/1-b",
    "Kurul, bir ihraççının esas sözleşmeye aykırı bir işlemi nedeniyle mal varlığının azaldığını tespit etmiş ve işlemin "
    f"butlanının tespiti için dava açmayı değerlendirmektedir. {K}, bu dava her hâlde işlemin vukuu tarihinden itibaren kaç "
    "yıl içinde açılmalıdır?",
    "5", ["1", "2", "3", "10"],
    "Kanun m. 92/1-b'ye göre Kurul, hukuka aykırılığın tespitinden itibaren üç ay ve her hâlde işlemin vukuundan itibaren üç "
    "yıl içinde iptal davası, beş yıl içinde butlan veya yokluğun tespiti davası açabilir.", zorluk="hard")

P.q("6362 s. SPKn m. 92",
    "Kurul, halka açık bir ortaklığın yönetiminin mevzuata aykırı işlemlerle ortaklık sermayesini azalttığını tespit etmiştir. "
    f"{K}, Kurulun bu durumdaki yetkilerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurul, suç duyurusu olmaksızın yönetim kurulu üyelerini süresiz görevden alabilir.",
    ["Kurul, ilgililerden aykırılıkların giderilmesi için tedbir almasını isteyebilir.",
     "Kurul, bu işlemlerin iptali için dava açabilir.",
     "Sorumluluğun mahkemece tespiti hâlinde sorumluların imza yetkileri kaldırılabilir.",
     "Görevden alınan üyelerin yerine ilk genel kurula kadar yenileri atanabilir."],
    "Kanun m. 92/1'e göre Kurul aykırılıkların giderilmesini isteyebilir, iptal ve butlan davası açabilir; mahkeme kararıyla "
    "tespit hâlinde imza yetkilerini kaldırabilir, suç duyurusunda bulunulmuşsa yargılama sonuçlanıncaya kadar ilgilileri "
    "görevden alıp ilk genel kurula kadar yenilerini atayabilir. Suç duyurusu olmaksızın süresiz görevden alma yetkisi yoktur.")

P.q("6362 s. SPKn m. 93",
    "Kayıtlı sermaye sistemindeki halka açık bir ortaklığın yönetim kurulu, pay sahiplerinin yeni pay alma haklarını "
    f"eşitsizliğe yol açacak şekilde kısıtlayan bir karar almış ve kamuya duyurmuştur. {K}, Kurulun bu karara karşı yetkisi "
    "aşağıdakilerden hangisidir?",
    "Otuz gün içinde asliye ticaret mahkemesinde iptal davası açmak",
    ["Duyurudan itibaren bir yıl içinde idare mahkemesinde iptal davası açmak",
     "Kararı kendi kararıyla doğrudan iptal etmek",
     "Duyurudan itibaren üç ay içinde asliye hukuk mahkemesinde tespit davası açmak",
     "Yönetim kurulunu tamamen görevden alıp YTM’yi görevlendirmek"],
    "Kanun m. 93'e göre Kurul, kayıtlı sermaye sistemindeki yönetim kurulu kararları aleyhine kararların kamuya duyurulduğu "
    "tarihten itibaren otuz gün içinde ortaklık merkezinin bulunduğu yer asliye ticaret mahkemesinde iptal davası açabilir "
    "ve teminatsız olarak icranın geri bırakılmasını isteyebilir.")

P.q("6362 s. SPKn m. 95-96",
    f"{K}, Kurulun halka açık ortaklıklar ve sermaye piyasası kurumları üzerindeki yetkilerine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Kurul, halka açık ortaklık genel kuruluna oy hakkı olmaksızın gözlemci gönderebilir.",
    ["Kurulun gönderdiği gözlemci genel kurulda Kurul adına oy kullanır.",
     "Kurul, sermaye piyasası kurumlarının faaliyetlerini ancak mahkeme kararıyla sınırlandırabilir.",
     "Kurul, hukuka aykırılıkta sorumlu çalışanların lisanslarını sadece geçici olarak iptal edebilir.",
     "Kurul, banka yönetim kurulu üyelerini BDDK’nın görüşü aranmaksızın görevden alabilir."],
    "Kanun m. 95'e göre Kurul halka açık ortaklık genel kurullarına oy hakkı bulunmaksızın gözlemci gönderebilir. m. 96'ya göre "
    "Kurul aykırılıkların giderilmesini isteyebilir veya faaliyetleri doğrudan sınırlandırıp durdurabilir, lisansları geçici "
    "veya sürekli iptal edebilir; banka yönetim kurulu üyelerinin görevden alınmasında BDDK'nın görüşü alınır.")

P.q("6362 s. SPKn m. 96",
    f"{K}, sermaye piyasası kurumlarının hukuka aykırı faaliyetlerinde uygulanacak tedbirlere ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Kurul, sorumlu yönetim kurulu üyelerini mahkeme kararı aranmaksızın görevden alabilir.",
    ["Kurul, aykırılıkların belirlediği sürede giderilmesini isteyebilir.",
     "Kurul, kurumun faaliyetlerini doğrudan sınırlandırabilir veya geçici olarak durdurabilir.",
     "Kurul, sorumlu yönetici ve çalışanların lisanslarını geçici veya sürekli iptal edebilir.",
     "Suç duyurusu kararından itibaren yargılama sonuçlanıncaya kadar imza yetkileri kaldırılabilir."],
    "Kanun m. 96'ya göre Kurul aykırılığın giderilmesini isteyebilir, faaliyetleri sınırlandırıp geçici durdurabilir veya "
    "yetkileri iptal edebilir; lisansları geçici veya sürekli iptal edebilir ve suç duyurusundan itibaren imza yetkilerini "
    "kaldırabilir. Yönetim kurulu üyelerini ancak sorumlulukları mahkeme kararıyla tespit edilmişse görevden alabilir.",
    zorluk="hard")

P.sayisal("6362 s. SPKn m. 97/4",
    "Bir aracı kurumun faaliyetleri, kendi talebi doğrultusunda Kurulca geçici olarak durdurulmuştur. "
    f"{K}, bu kurumun geçici kapalılık süresi en fazla kaç yıl olabilir?",
    "2", ["1", "3", "5", "10"],
    "Kanun m. 97/4'e göre faaliyetleri Kurulca veya kendi talepleri doğrultusunda geçici olarak durdurulan sermaye piyasası "
    "kurumlarının geçici kapalılık süresi iki yılı geçemez.")

P.q("6362 s. SPKn m. 97/2",
    "Kurul, sermaye yeterliliğini sağlayamayan bir aracı kurumun yetkilerini sürekli olarak kaldırmış, ardından kurumun "
    f"iflasına karar verilmiştir. {K}, YTM’nin bu kurum nedeniyle yaptığı ödemelerden doğan alacağının sırası nedir?",
    "Devletin ve sosyal güvenlik kuruluşlarının amme alacaklarından sonra gelen imtiyazlı alacaktır.",
    ["Tüm alacaklardan önce gelen birinci sıra imtiyazlı alacaktır.",
     "Adi alacaklarla birlikte garameten ödenir.",
     "Sadece iflas masasında artan olursa ödenir.",
     "Rehinli alacaklardan önce, amme alacaklarıyla birlikte garameten ödenir."],
    "Kanun m. 97/2'ye göre iflas kararı hâlinde YTM'nin ödemelerinden doğan alacakları, Devletin ve sosyal güvenlik "
    "kuruluşlarının 6183 sayılı Kanun kapsamındaki alacaklarından sonra gelmek üzere imtiyazlı alacak olarak öncelikle tahsil "
    "edilir ve sıra cetvelinin kesinleşmesi beklenmeksizin ödenir.", zorluk="hard")

P.q("6362 s. SPKn m. 98",
    "Tedricî tasfiyeye giren bir aracı kurumda, sorumlulukları m. 97 uyarınca tespit edilmiş bazı kişiler bulunmaktadır. "
    f"{K}, Kurulun şahsen iflasını isteyebileceği kişiler arasında aşağıdakilerden hangisi yer alır?",
    "Doğrudan veya dolaylı yüzde onundan fazla paya sahip ortaklar",
    ["Yüzde birden az paya sahip ortaklar",
     "Aracı kurumun müşterileri",
     "Aracı kurumun bağımsız denetimini yapan kuruluş",
     "Aracı kurumun kredi kullandığı bankalar"],
    "Kanun m. 98'e göre sermaye piyasası kurumlarının iflası veya tedricî tasfiyeye girmesi hâlinde, sorumlulukları m. 97'ye "
    "göre tespit edilmiş olmak kaydıyla, doğrudan veya dolaylı yüzde onundan fazla paya sahip ortakların, yönetim kurulu "
    "üyelerinin ve imzaya yetkili yöneticilerin şahsen iflası istenebilir.")

# ================================================================ sermaye piyasası kurumları, yatırım hizmetleri (m. 3/v, 35, 37-45)
P.q("6362 s. SPKn m. 35",
    f"{K}, aşağıdakilerden hangisi Kanunda sayılan sermaye piyasası kurumları arasında yer almaz?",
    "Halka açık ortaklıklar",
    ["Varlık kiralama şirketleri", "Merkezî takas kuruluşları", "Veri depolama kuruluşları",
     "İpotek finansmanı kuruluşları"],
    "Kanun m. 35'e göre sermaye piyasası kurumları; yatırım kuruluşları, kolektif yatırım kuruluşları, bağımsız denetim, "
    "değerleme ve derecelendirme kuruluşları, portföy yönetim şirketleri, ipotek finansmanı kuruluşları, konut ve varlık "
    "finansmanı fonları, varlık kiralama şirketleri, merkezî takas ve saklama kuruluşları ile veri depolama kuruluşlarıdır. "
    "Halka açık ortaklıklar ihraççıdır.", zorluk="easy")

P.q("6362 s. SPKn m. 3/v",
    f"{K}, aşağıdakilerden hangisi “yatırım kuruluşu” tanımı kapsamında değildir?",
    "Portföy yönetim şirketleri",
    ["Aracı kurumlar", "Mevduat bankaları", "Kalkınma ve yatırım bankaları", "Katılım bankaları"],
    "Kanun m. 3/v'ye göre yatırım kuruluşu, aracı kurumlar ile Kurulca esasları belirlenen diğer sermaye piyasası kurumları ve "
    "bankalardır. Portföy yönetim şirketleri m. 35'te ayrıca sayılan sermaye piyasası kurumlarıdır; yatırım kuruluşu değildir.",
    zorluk="hard")

P.oncul("6362 s. SPKn m. 39/9",
    "Bir mevduat bankası aşağıdaki yatırım hizmetlerini sunmayı planlamaktadır:",
    ["Sermaye piyasası araçlarına ilişkin emirlerin alınması ve iletilmesi",
     "Emirlerin müşteri adına ve hesabına gerçekleştirilmesi",
     "Portföy yöneticiliği",
     "Sermaye piyasası araçlarının müşteri namına saklanması"],
    f"{K}, yukarıdaki hizmetlerden hangileri bankalarca da yürütülebilir?",
    "I, II ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 39/9'a göre m. 37/1'in (a), (b), (c), (ğ) ve (h) bentlerindeki hizmetler bankalarca da yürütülebilir; portföy "
    "yöneticiliği (ç), yatırım danışmanlığı (d) ve halka arza aracılık (e, f) ise yatırım ve kalkınma bankalarınca "
    "sunulabilir.", zorluk="hard")

P.q("6362 s. SPKn m. 39/9",
    "Bir kalkınma ve yatırım bankası, bir şirketin paylarının halka arzında yüklenimde bulunarak satışa aracılık etmek "
    f"istemektedir. {K}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kalkınma ve yatırım bankaları Kurul izniyle halka arza aracılık hizmeti sunabilir.",
    ["Halka arza aracılık münhasıran aracı kurumlara ait olduğundan banka bu hizmeti sunamaz.",
     "Banka ancak yüklenimde bulunmaksızın satışa aracılık edebilir.",
     "Banka bu hizmeti BDDK izniyle ve Kurul izni aranmaksızın sunabilir.",
     "Banka ancak bir aracı kurumla konsorsiyum kurarak bu hizmeti sunabilir."],
    "Kanun m. 39/9'a göre yatırım ve kalkınma bankaları m. 37/1'in (ç), (d), (e) ve (f) bentlerindeki hizmetleri de sunabilir; "
    "III-37.1 m. 52'ye göre aracılık yüklenimi ve en iyi gayret aracılığı Kurul izniyle aracı kurumlar ile kalkınma ve yatırım "
    "bankalarınca yapılabilir.")

P.sayisal("6362 s. SPKn m. 39/4",
    f"{K}, yatırım hizmetleri ve faaliyetleri için yapılan faaliyet izni başvuruları, gerekli belgelerin Kurula eksiksiz "
    "sunulmasından itibaren azami kaç ay içinde karara bağlanır?",
    "6", ["1", "2", "3", "12"],
    "Kanun m. 39/4'e göre faaliyet izni başvuruları gerekli belgelerin eksiksiz sunulmasından itibaren azami altı ay içinde "
    "Kurul tarafından karara bağlanır; m. 39/1 yatırım hizmetlerinin düzenli uğraş olarak yapılmasını Kurul iznine bağlar.")

P.q("6362 s. SPKn m. 41",
    f"{K}, yetki belgesi ve faaliyet izninin iptaline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İznin verildiği tarihten itibaren bir yıl faaliyette bulunulmaması iptal sebebidir.",
    ["Faaliyette bulunma yetkisinden açıkça feragat edilmesi iptal sebebidir.",
     "İznin yanlış veya yanıltıcı beyanla alınmış olması iptal sebebidir.",
     "Kaybedilen şartların tespitten itibaren üç ay içinde yeniden sağlanamaması iptal sebebidir.",
     "Tüm izinleri iptal edilenler üç ay içinde unvan ve faaliyet konularını değiştirir veya sona erme kararı alır."],
    "Kanun m. 41'e göre açık feragat veya iznin verildiği tarihten itibaren iki yıl süreyle faaliyette bulunulmaması, iznin "
    "yanıltıcı beyan veya hukuka aykırı yollarla alınması ve kaybedilen şartların üç ay içinde sağlanamaması iptal sebebidir; "
    "tüm izinleri iptal edilenler üç ay içinde esas sözleşmelerini değiştirir veya sona erme kararı alır.")

P.q("6362 s. SPKn m. 40/2",
    "Kuruldan yatırım hizmetleri için izin almamış bir danışmanlık şirketi, ticaret unvanında “Yatırım ve Aracılık” ibaresini "
    f"kullanmak istemektedir. {K}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu hizmetlerde bulunduğu intibaını uyandıracak ibare kullanamaz.",
    ["Fiilen aracılık yapmadığı sürece ibareyi kullanabilir.",
     "Ticaret sicili müdürlüğünün onayıyla ibareyi kullanabilir.",
     "İbareyi kullanabilir, ancak ilanlarında izinsiz olduğunu belirtmesi gerekir.",
     "Türkiye Sermaye Piyasaları Birliğine üye olursa ibareyi kullanabilir."],
    "Kanun m. 40/2'ye göre Kuruldan izin almayanlar ile izinleri iptal olanlar yatırım hizmetlerinde bulunamayacakları gibi "
    "esas sözleşmelerinde, ticaret unvanlarında veya ilan ve reklamlarında bu hizmetlerde bulundukları intibaını uyandıracak "
    "kelime veya ibare kullanamazlar.", zorluk="easy")

P.q("6362 s. SPKn m. 43",
    f"{K}, aracı kurumların kuruluş şartlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Paylarının bir kısmı hamiline yazılı olarak çıkarılabilir.",
    ["Anonim ortaklık şeklinde kurulmaları gerekir.",
     "Paylarının nakit karşılığı çıkarılması gerekir.",
     "Sermayelerinin Kurulca belirlenen miktardan az olmaması gerekir.",
     "Ortaklık yapısının şeffaf ve açık olması gerekir."],
    "Kanun m. 43/1'e göre aracı kurumların anonim ortaklık şeklinde kurulması, paylarının tamamının nama yazılı ve nakit "
    "karşılığı çıkarılması, sermayenin Kurulca belirlenen miktardan az olmaması, esas sözleşmenin mevzuata uygunluğu, "
    "kurucuların şartları taşıması ve ortaklık yapısının şeffaf olması gerekir.", zorluk="easy")

P.sayisal("6362 s. SPKn m. 44/1",
    "Hakkındaki iflas kararı kaldırılmış bir kişi, bir aracı kuruma kurucu ortak olmak istemektedir. "
    f"{K}, iflasın kaldırılmasına ilişkin kararın kesinleşmesinden itibaren kaç yıl geçmesi hâlinde iflas şartı dikkate alınmaz?",
    "10", ["2", "3", "5", "15"],
    "Kanun m. 44/1'e göre müflis olmama, konkordato ilan etmemiş olma ve iflasın ertelenmemiş olma şartları; iflasın "
    "kaldırılmasına, kapatılmasına veya konkordato teklifinin tasdikine ilişkin kararın kesinleşmesinden itibaren on yıl "
    "geçmesi hâlinde dikkate alınmaz.", zorluk="hard")

P.q("6362 s. SPKn m. 44/3",
    f"{K}, aracı kurumlarda yapılacak işlemlere ilişkin aşağıdaki eşleştirmelerden hangisi doğrudur?",
    "Pay devri – Kurul izni",
    ["Esas sözleşme değişikliği – Kurula bildirim",
     "Dönüşüm işlemi – Ticaret sicili onayı",
     "Pay devri – Kurula sonradan bildirim",
     "Dışarıdan destek hizmeti alımı – BDDK izni"],
    "Kanun m. 44/3'e göre aracı kurumların dönüşüm işlemleri ile esas sözleşme değişikliklerinde Kurulun uygun görüşü, pay "
    "devirlerinde Kurul izni zorunludur; aykırı devirler pay defterine kaydolunmaz. m. 44/4 dışarıdan destek hizmeti "
    "esaslarını Kurula bırakır.")

P.q("6362 s. SPKn m. 45/3-5",
    f"{K}, yatırım kuruluşlarının faaliyet şartlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Borsada işlem yapacak yatırım kuruluşlarının ilgili borsadan işlem yapma yetkisi alması zorunludur.",
    ["Yatırım kuruluşları yatırımcıları sınıflandıramaz; tüm yatırımcılara aynı koruma sağlanır.",
     "İç kontrol birimi kurulması, sadece halka açık yatırım kuruluşları için zorunludur.",
     "Yatırım kuruluşu yöneticilerinde tecrübe ve eğitim şartı aranmaz.",
     "Borsada işlem yapma yetkisi Kurul izniyle birlikte ayrıca başvuru gerekmeksizin doğar."],
    "Kanun m. 45'e göre yöneticiler m. 44'teki şartlar ile Kurulca belirlenen tecrübe ve eğitim şartlarını taşır; borsada işlem "
    "yapacak yatırım kuruluşları ilgili borsadan işlem yapma yetkisi almak zorundadır; Kurul yatırımcıları sınıflandırabilir ve "
    "yatırım kuruluşları iç kontrol sistemleri kurmakla yükümlüdür.")

# ================================================================ III-37.1 Tebliği
P.oncul("III-37.1 m. 8",
    "Aracı kurumların yetki gruplarına ilişkin aşağıdaki eşleştirmeler verilmiştir:",
    ["Dar yetkili – Emir iletimine aracılık ve yatırım danışmanlığı",
     "Dar yetkili – Bireysel portföy yöneticiliği",
     "Kısmi yetkili – İşlem aracılığı, en iyi gayret aracılığı, sınırlı saklama ve portföy yöneticiliği",
     "Geniş yetkili – Portföy aracılığı, genel saklama ve aracılık yüklenimi"],
    f"{YH}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Tebliğ m. 8'e göre emir iletimine aracılık ve yatırım danışmanlığı yapanlar dar yetkili; işlem aracılığı, en iyi gayret "
    "aracılığı, sınırlı saklama ve portföy yöneticiliği yapanlar kısmi yetkili; portföy aracılığı, genel saklama ve aracılık "
    "yüklenimi yapanlar geniş yetkili aracı kurumdur. Portföy yöneticiliği dar yetki kapsamında değildir.")

P.q("III-37.1 m. 40, 48",
    "Bir aracı kurum, yeni bir müşterisiyle yatırım danışmanlığı çerçeve sözleşmesi imzalamaya hazırlanmaktadır. "
    f"{YH}, sözleşme imzalanmadan önce aşağıdakilerden hangisi zorunludur?",
    "Müşteriye yerindelik testi uygulanması",
    ["Müşterinin nitelikli yatırımcı olduğunun belgelenmesi",
     "Müşterinin portföyünün bağımsız denetimden geçirilmesi",
     "Müşterinin TSPB sicil kaydının yapılması",
     "Müşterinin kredi derecelendirme notunun alınması"],
    "Tebliğ m. 48'e göre yatırım danışmanlığı çerçeve sözleşmesi imzalanmadan önce, m. 40'a göre de bireysel portföy "
    "yöneticiliği sözleşmesinden önce yerindelik testi uygulanması zorunludur; test hizmetin müşterinin yatırım amaçları, "
    "mali durumu ile bilgi ve tecrübesiyle uyumunu değerlendirir.", zorluk="easy")

P.q("III-37.1 m. 40",
    f"{YH}, yerindelik testine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müşteri istenen bilgileri vermezse hizmet, müşterinin yazılı talebi üzerine yine de sunulabilir.",
    ["Test, hizmetin müşterinin yatırım amaçları, mali durumu ile bilgi ve tecrübesiyle uyumunu değerlendirir.",
     "Müşteri test için verdiği bilgilerin doğruluğundan sorumludur.",
     "Mali durum değerlendirmesi müşterinin gelir düzeyi ve yatırım amaçlı varlığına ilişkin bilgilerle sınırlıdır.",
     "Test sonucuna uygun olmayan portföy yöneticiliği veya danışmanlık hizmeti sunulamaz."],
    "Tebliğ m. 40'a göre yerindelik testi hizmetin müşterinin yatırım amaçları, mali durumu ve bilgi ve tecrübesiyle uyumunu "
    "değerlendirir; mali durum değerlendirmesi sunulan bilgilerle sınırlıdır ve müşteri bilgilerin doğruluğundan sorumludur. "
    "Sonuca uygun olmayan hizmet sunulamaz; bilgi verilmezse hizmet sunulamaz ve müşteriye yazılı bildirim yapılır.")

P.oncul("III-37.1 m. 38, 46, 52",
    "Aşağıda bazı yatırım hizmetleri ile bu hizmetleri Kurul izniyle yürütebilecek kuruluşlar eşleştirilmiştir:",
    ["Bireysel portföy yöneticiliği – Mevduat bankaları",
     "Yatırım danışmanlığı – Portföy yönetim şirketleri",
     "Aracılık yüklenimi – Kalkınma ve yatırım bankaları",
     "En iyi gayret aracılığı – Aracı kurumlar"],
    f"{YH}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "II, III ve IV", ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Tebliğ m. 38 ve 46'ya göre bireysel portföy yöneticiliği ve yatırım danışmanlığı Kurul izniyle aracı kurumlar, yatırım "
    "ve kalkınma bankaları ile portföy yönetim şirketlerince; m. 52'ye göre aracılık yüklenimi ve en iyi gayret aracılığı "
    "aracı kurumlar ile kalkınma ve yatırım bankalarınca yapılabilir. Mevduat bankaları portföy yöneticiliği yapamaz.",
    zorluk="hard")

P.q("III-37.1 m. 59",
    "Bir aracı kurum, yalnız işlem aracılığı yaptığı müşterilerinin aracılığa konu paylarını saklamaktadır. "
    f"{YH}, bu saklama hizmetinin niteliği aşağıdakilerden hangisidir?",
    "Sınırlı saklama hizmeti",
    ["Genel saklama hizmeti", "Portföy saklama hizmeti", "Merkezî saklama hizmeti", "Kripto varlık saklama hizmeti"],
    "Tebliğ m. 59/3'e göre sınırlı saklama, işlem ve portföy aracılığı, bireysel portföy yöneticiliği ve halka arza aracılıkla "
    "ilgili olarak aracılık hizmetine konu araçların saklanmasıdır; genel saklama ise yetkili olunan hizmetlerden bağımsız "
    "sunulan saklama hizmetidir.")

P.sayisal("III-37.1 m. 7/3",
    "Faaliyet izni bulunan bir aracı kurum, sunmayı planladığı yeni bir yan hizmeti Kurula bildirmiştir. "
    f"{YH}, Kurulca aksi yönde görüş bildirilmedikçe bu yan hizmet bildirimi takiben kaç iş günü sonra yürütülmeye başlanabilir?",
    "20", ["5", "10", "30", "60"],
    "Tebliğ m. 7'ye göre yan hizmetler ayrıca yetki belgesine tabi değildir; Kurula yapılan bildirimi takiben 20 iş günü içinde "
    "Kurulca aksi yönde görüş bildirilmedikçe bildirilen yan hizmetler yürütülmeye başlanır.")

# ================================================================ borsalar ve diğer kurumlar (m. 62-76)
P.q("6362 s. SPKn m. 65",
    f"{K}, borsalar ve piyasa işleticilerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Borsaların kuruluşuna Kurul Karar Organı izin verir.",
    ["Borsaların faaliyete geçmesi Kurulun iznine tabidir.",
     "Borsalara karşı açılacak davalar adli yargıda görülür.",
     "Borsa personeliyle ihtilaflarda iş mahkemeleri görevlidir.",
     "Borsaların pay devirleri Kurulun iznine tabidir."],
    "Kanun m. 65'e göre borsaların ve piyasa işleticilerinin kuruluşuna Kurulun uygun görüşü üzerine Cumhurbaşkanı izin "
    "verir, faaliyete geçmeleri Kurul iznine tabidir. Esas sözleşme değişiklikleri ve pay devirleri Kurul iznine bağlıdır; "
    "borsalara karşı davalar adli yargıda, personel ihtilafları iş mahkemelerinde görülür.")

P.q("6362 s. SPKn m. 65/4",
    "Kuruluş izni alan bir borsa, izni izleyen bir yıl içinde faaliyet izni için Kurula başvurmamıştır ve bunun kuruluşa "
    f"yüklenemeyecek bir sebebi de bulunmamaktadır. {K}, bu durumun sonucu aşağıdakilerden hangisidir?",
    "Kuruluş izni iptal olur; Kurul süreyi ancak zorunlu sebeplerle uzatabilir.",
    ["Kuruluş izni bir yıl daha Kurul kararı aranmaksızın uzar.",
     "Borsaya idari para cezası verilir ve izin geçerliliğini korur.",
     "Borsa faaliyet izni olmaksızın faaliyete başlayabilir.",
     "Kuruluş izni Cumhurbaşkanı kararıyla faaliyet iznine dönüşür."],
    "Kanun m. 65/4'e göre kuruluş izninin alınmasını takiben en geç bir yıl içinde faaliyet izni başvurusu yapılması şarttır; "
    "bu sürede başvurmayanların veya başvurusu uygun görülmeyenlerin kuruluş izni iptal olur. Zorunlu sebepler veya kuruluşa "
    "yüklenemeyecek sebepler varsa Kurul süreyi bir yıl uzatabilir.")

P.q("6362 s. SPKn m. 69",
    "Borsa, kendi düzenlemelerindeki şartların oluşması nedeniyle bir ortaklığın paylarının işlem görmesini durdurmuştur. "
    f"{K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Durum derhâl Kurula bildirilir ve kamuya açıklanır; Kurulun yetkisi saklıdır.",
    ["Borsa işlem durdurma kararını ancak Kurulun önceden onayıyla alabilir.",
     "Borsa işlemleri durdurabilir, ancak kottan çıkarma yetkisi sadece Kurula aittir.",
     "Durdurma kararı kamuya açıklanmaz, sadece ihraççıya bildirilir.",
     "Kurul, borsanın durdurma kararını ancak mahkeme kararıyla kaldırabilir."],
    "Kanun m. 69'a göre borsa veya piyasa işleticisi, kendi düzenlemelerindeki şartların oluşması hâlinde ilgili aracın işlem "
    "görmesini durdurabileceği gibi kottan da çıkarabilir; bu durum derhâl Kurula bildirilir ve kamuya açıklanır. Kurulun "
    "durdurma ve kottan çıkarma yetkisi saklıdır.")

P.oncul("6362 s. SPKn m. 66, 72, 73",
    "Borsa ve diğer pazar yerlerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Teşkilatlanmış diğer pazar yerlerinin gözetim ve denetim mercii Kuruldur.",
     "Borsaların mali denetimi Kurulca ilan edilen listedeki bağımsız denetim kuruluşlarınca yapılır.",
     "Borsalar gerekli iç kontrol birim ve sistemlerini oluşturmakla yükümlüdür.",
     "Borsalar kamu idaresine ilişkin mali mevzuat kısıtlamalarına tabidir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III", ["I ve II", "II ve IV", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 66'ya göre teşkilatlanmış diğer pazar yerlerinin gözetim ve denetim mercii Kuruldur; m. 72/2'ye göre borsaların "
    "mali denetimi listedeki bağımsız denetim kuruluşlarınca yapılır; m. 73/1 iç kontrol sistemi kurulmasını zorunlu kılar. "
    "m. 65/10'a göre borsalar kamu idaresine ilişkin mevzuat hükümlerine ve kısıtlamalarına tabi tutulamaz.")

P.q("6362 s. SPKn m. 74",
    f"{K}, Türkiye Sermaye Piyasaları Birliğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üyelik başvurusu yetki belgesinin alınmasından itibaren bir yıl içinde yapılır.",
    ["Birlik, tüzel kişiliği haiz kamu kurumu niteliğinde bir meslek kuruluşudur.",
     "Birlik, üyelerin uyuşmazlıklarının tahkim yoluyla çözümü için altyapı kurar.",
     "Birlik, statüsünde öngörülen disiplin cezalarını verir.",
     "Üyelik başvurusu yapmayan kuruluşların faaliyetleri Kurulca durdurulur."],
    "Kanun m. 74'e göre yatırım kuruluşları ve Kurulca uygun görülenler ile kitle fonlama platformları ve kripto hizmet "
    "sağlayıcıları, kamu kurumu niteliğindeki TSPB'ye yetki belgelerini almalarından itibaren üç ay içinde başvurmak "
    "zorundadır; başvurmayanların faaliyetleri durdurulur. Birlik disiplin cezası verir ve tahkim altyapısı kurar.")

P.sayisal("6362 s. SPKn m. 75/7",
    "Türkiye Sermaye Piyasaları Birliği yönetim kurulu, bir üye aracı kuruma disiplin cezası vermiştir. "
    f"{K}, aracı kurum bu karara karşı kararın tebliğini izleyen kaç iş günü içinde Kurul nezdinde itiraz edebilir?",
    "10", ["5", "15", "30", "60"],
    "Kanun m. 75/7'ye göre Birliğin yetkili organlarınca alınan kararlara karşı kararın ilgiliye tebliğini izleyen on iş günü "
    "içinde Kurul nezdinde itiraz edilebilir; itiraza ilişkin Kurul kararları kesindir.")

P.q("6362 s. SPKn m. 76",
    "Gayrimenkul değerleme uzmanlığı lisansı almaya hak kazanan bir kişi, Türkiye Değerleme Uzmanları Birliğine üyelik için "
    f"başvuru yapmamıştır. {K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Üç ay içinde başvurmayanın lisansı Kurulca iptal edilir.",
    ["Üyelik isteğe bağlı olduğundan lisans geçerliliğini korur.",
     "Başvurmayan kişiye Birlik tarafından uyarma cezası verilir, lisans iptal edilmez.",
     "Lisans, bir yıl içinde başvurulmazsa askıya alınır.",
     "Başvuru süresi lisans sahibinin ilk değerleme raporunu imzalamasıyla başlar."],
    "Kanun m. 76/2'ye göre lisans sahibi lisans almaya hak kazandığı tarihten itibaren üç ay içinde Türkiye Değerleme Uzmanları "
    "Birliğine üyelik başvurusu yapmakla yükümlüdür; bu yükümlülüğe uymayanların lisansı Kurulca iptal edilir.")

P.q("6362 s. SPKn m. 62-63",
    f"{K}, sermaye piyasasında faaliyet gösterecek bağımsız denetim kuruluşlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bağımsız denetim kuruluşlarını yetkilendirme yetkisi münhasıran Kurula aittir.",
    ["Kurul, ilave şartları taşıyan bağımsız denetim kuruluşlarının listesini kamuya açıklar.",
     "Kurul, kalite kontrolde aykırılık tespit ettiği kuruluşları listeden çıkarabilir.",
     "Kurul, kalite kontrol ve denetim sonuçlarını Kamu Gözetimi Kurumuna bildirir.",
     "Denetim kuruluşları görev kapsamıyla sınırlı olarak raporu imzalayanlarla birlikte sorumludur."],
    "Kanun m. 62'ye göre bağımsız denetim kuruluşlarını Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu yetkilendirir; "
    "Kurul sermaye piyasasında denetim yapacaklar için ilave şartları belirler, listeyi ilan eder, aykırılıkta listeden çıkarır "
    "ve sonuçları KGK'ya bildirir. m. 63 raporu imzalayanlarla birlikte sorumluluğu düzenler.", zorluk="hard")

P.q("6362 s. SPKn m. 64",
    "Bir aracı kurumun finansal tablolarını denetleyen bağımsız denetçi, kurumun sermaye yeterliliği şartını ihlal ettiğini ve "
    f"bu durumun olumsuz görüş gerektirdiğini tespit etmiştir. {K}, denetçinin yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Durumu Kurula derhâl bildirir; bu bildirim sır saklama yükümlülüğünün ihlali sayılmaz.",
    ["Durumu sadece denetim raporunda belirtir, Kurula ayrıca bildirim yapmaz.",
     "Bildirim için aracı kurumun yönetim kurulunun onayını alır.",
     "Bildirim yaparsa sözleşmeye aykırılık nedeniyle tazminat sorumluluğu doğar.",
     "Durumu önce Kamu Gözetimi Kurumuna, Kurumun onayıyla Kurula bildirir."],
    "Kanun m. 64'e göre yatırım kuruluşu veya kolektif yatırım kuruluşunda görev yapan bağımsız denetçiler, yetkilendirme "
    "şartlarını ihlal eden, faaliyetin sürekliliğini engelleyebilecek veya olumsuz görüş ya da görüş bildirmekten kaçınma "
    "gerektiren durumları Kurula derhâl bildirir; bildirim hukuki ve cezai sorumluluk doğurmaz.")

P.q("6362 s. SPKn m. 70/1",
    "Bir yatırımcı ile aracı kurumu arasında borsada gerçekleştirilen emirlerin eşleştirilmesinden doğan bir uyuşmazlık "
    f"çıkmıştır. {K}, bu tür uyuşmazlıkların çözümüne ilişkin usul ve esasları kim belirler?",
    "İlgili borsanın yönetim kurulu",
    ["Türkiye Sermaye Piyasaları Birliği", "Kurul Karar Organı", "Merkezî Kayıt Kuruluşu",
     "Yatırımcı Tazmin Merkezi"],
    "Kanun m. 70/1'e göre yatırım kuruluşlarının kendi aralarında veya müşterileriyle emirlerin iletilmesi ve eşleştirilmesi ile "
    "yükümlülüklerin yerine getirilmesine ilişkin borsa işlemlerinden doğan uyuşmazlıkların çözümüne ilişkin usul ve esaslar "
    "borsa yönetim kurullarınca belirlenir; belirli tutarı aşan kararlara karşı Kurula itiraz edilebilir.")

P.q("6362 s. SPKn m. 38-39/2",
    "Faaliyet izni bulunan bir aracı kurum, müşterilerine servet yönetimi ve finansal planlama hizmeti de sunmak istemektedir. "
    f"{K}, bu hizmete ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yan hizmettir; ayrı yetki belgesi gerekmeksizin sunulabilir.",
    ["Yatırım hizmetidir; ayrı bir yetki belgesi alınması gerekir.",
     "Aracı kurumların yapamayacağı, sadece bankalara özgü bir hizmettir.",
     "Portföy yönetim şirketlerine özgü bir faaliyettir.",
     "Türkiye Sermaye Piyasaları Birliğinin iznine tabidir."],
    "Kanun m. 38'e göre servet yönetimi ve finansal planlama, yatırım kuruluşları ve portföy yönetim şirketlerinin "
    "yapabileceği yan hizmetlerdendir; m. 39/2'ye göre yan hizmetler ayrıca yetki belgesine tabi olmaksızın Kurulca belirlenen "
    "esaslar çerçevesinde yapılır.")

P.q("6362 s. SPKn m. 39/1, 5",
    f"{K}, yatırım hizmetleri ve faaliyetlerinde izin zorunluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Özel kanunuyla yetkili kılınan kuruluşlar Kurul izni olmadan da bu hizmetleri sunabilir.",
    ["Yatırım hizmetlerinin düzenli uğraş olarak icrası Kurul iznine bağlıdır.",
     "Yatırım hizmetleri ancak yatırım kuruluşlarınca yerine getirilebilir.",
     "Kurul, her hizmetin ayrı kuruluşlarca yapılmasına ilişkin düzenleme yapabilir.",
     "Kurul, hizmetlerin sunulması için mesleki sorumluluk sigortasını zorunlu tutabilir."],
    "Kanun m. 39/1'e göre yatırım hizmetlerinin düzenli uğraş olarak icrası Kurul iznine bağlıdır ve ancak yatırım kuruluşlarınca "
    "yapılabilir. m. 39/5'e göre özel kanunlarıyla yetkili kılınmış olsalar dahi Kanundaki şartları taşımayan ve Kurulca izin "
    "verilmeyenler bu hizmetlerde bulunamaz; m. 39/6 sigorta zorunluluğuna imkân verir.")

P.q("III-37.1 m. 45",
    "Bir aracı kurum, belirli bir müşterisine, müşterinin talebi olmaksızın belirli bir payı almasını teşvik eden yazılı bir "
    f"değerlendirme göndermiştir. {YH}, bu faaliyet aşağıdakilerden hangisidir?",
    "Yatırım danışmanlığı",
    ["Genel yatırım tavsiyesi", "Emir iletimine aracılık", "Bireysel portföy yöneticiliği", "Finansal planlama"],
    "Tebliğ m. 45'e göre yatırım danışmanlığı, yetkili kuruluşun yatırımcı talebi doğrultusunda veya talep olmaksızın belli "
    "bir kişiye ya da benzer nitelikteki bir gruba yönelik yönlendirici nitelikte yorum ve tavsiyelerde bulunmasıdır; kişiye "
    "özgü olmayan genel tavsiyeler yan hizmettir.")

P.q("III-37.1 m. 11",
    f"{YH}, aşağıdakilerden hangisi emir iletimine aracılık faaliyeti kapsamında sayılmaz?",
    "Müşteri emirlerinin karşı taraf olarak kendi portföyünden yerine getirilmesi",
    ["Halka arzda taleplerin toplanıp ilgili yatırım kuruluşuna iletilmesi (gişe hizmeti)",
     "Lehine faaliyet gösterilen kuruluşun hizmetlerinin yatırımcılara tanıtılması",
     "Sözleşme yapmak isteyen tarafların komisyon karşılığında bir araya getirilmesi",
     "Müşteri emirlerinin yetkili bir yatırım kuruluşuna iletilmesi ve sonuçlarının bildirilmesi"],
    "Tebliğ m. 11'e göre emir iletimine aracılık, müşteri emirlerinin yetkili yatırım kuruluşuna iletilmesi ve sonuçların "
    "bildirilmesidir; gişe hizmeti, hizmetlerin tanıtılması ve tarafların bir araya getirilmesi de bu kapsamdadır. Emirlerin "
    "karşı taraf olarak yerine getirilmesi m. 21'deki portföy aracılığıdır.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
