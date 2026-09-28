# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Denetim Temelleri — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında BDS 200 tanımları (makul güvence, mesleki muhakeme, mesleki şüphecilik,
denetim riski ve bileşenleri), BDS 210 ön kabul sorumlulukları ve kapsam sınırlandırması sık sorulmuştur.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · BDS 200 Bağımsız Denetçinin Genel Amaçları; BDS 210 Bağımsız Denetim Sözleşmesinin Şartlarının Kabulü
  · BDS 220 (Revize) Finansal Tabloların Bağımsız Denetiminde Kalite Yönetimi (sorumlu denetçinin genel sorumlulukları)
  · BDS 230 Bağımsız Denetimin Belgelendirilmesi; BDS 300 Planlama; BDS 260 Üst Yönetimle İletişim
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_denetim_temelleri_2026.json", lesson="denetim", topic="denetim_temelleri",
          konu_adi="Denetim Temelleri", seed=2026092843,
          surum="BDS 200, 210, 220 (Revize), 230, 260, 300 güncel metinleri; 28.09.2026 kontrolü")

B200 = "BDS 200 “Bağımsız Denetçinin Genel Amaçları”na göre"
B210 = "BDS 210 “Bağımsız Denetim Sözleşmesinin Şartlarının Kabulü”ne göre"
B230 = "BDS 230 “Bağımsız Denetimin Belgelendirilmesi”ne göre"
B300 = "BDS 300 “Finansal Tabloların Bağımsız Denetiminin Planlanması”na göre"
B260 = "BDS 260 “Üst Yönetimden Sorumlu Olanlarla Kurulacak İletişim”e göre"
B220 = "BDS 220 (Revize) “Finansal Tabloların Bağımsız Denetiminde Kalite Yönetimi”ne göre"
TDS = "Türkiye Denetim Standartları’na göre"

# ================================================================ BDS 200: amaçlar ve temel kavramlar
P.q("BDS 200 prg. 11",
    f"{B200}, finansal tabloların denetiminde denetçinin genel amaçları arasında aşağıdakilerden hangisi yer alır?",
    "Tabloların bütün olarak önemli yanlışlık içerip içermediğine dair makul güvence elde etmek",
    ["Finansal tablolardaki bütün hata ve hileleri tespit ederek yönetime raporlamak",
     "İşletmenin iç kontrol sisteminin etkinliği hakkında finansal tablo görüşünden ayrı bir güvence raporu düzenlemek",
     "İşletmenin gelecekteki faaliyetlerinin sürdürülebilirliğine dair mutlak güvence vermek",
     "Yönetimin iş kararlarının etkinliğini ve verimliliğini değerlendirerek görüş bildirmek"],
    "BDS 200 prg. 11'e göre denetçinin genel amaçları, finansal tabloların bir bütün olarak hata veya hile kaynaklı önemli "
    "bir yanlışlık içerip içermediğine ilişkin makul güvence elde ederek çerçeveye uygunluk hakkında görüş bildirmek ve "
    "bulgularına uygun olarak raporlama ve bildirimlerde bulunmaktır.", zorluk="easy")

P.q("BDS 200 prg. 5, 13-e",
    f"{B200}, makul güvenceye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Makul güvence, denetim riskinin sıfıra indirildiği güvence seviyesidir.",
    ["Makul güvence, finansal tabloların denetimi çerçevesinde yüksek ancak mutlak olmayan güvence seviyesidir.",
     "Denetçi, denetim riskini kabul edilebilir düşük seviyeye indirecek yeterli ve uygun kanıt elde ettiğinde makul güvence sağlar.",
     "Kanıtların çoğunun kesin olmaktan çok ikna edici olması, makul güvencenin mutlak olmamasının sebebidir.",
     "Makul güvence, denetimin yapısal kısıtlamaları nedeniyle mutlak bir güvence seviyesi değildir."],
    "BDS 200 prg. 5 ve 13-e'ye göre makul güvence yüksek ancak mutlak olmayan güvencedir; denetçi denetim riskini kabul "
    "edilebilir düşük seviyeye indirecek kanıt elde ettiğinde sağlanır. A45'e göre denetim riski sıfıra indirilemez.")

P.q("BDS 200 prg. 13-g",
    "“Sorgulayıcı bir yaklaşımla hareket ederek, hata veya hile kaynaklı yanlışlığa işaret eden durumlara karşı dikkatli "
    "olmayı ve denetim kanıtlarını titiz bir biçimde değerlendirmeyi içeren tutum”\n\n"
    f"{B200} yukarıda tanımlanan kavram aşağıdakilerden hangisidir?",
    "Mesleki şüphecilik",
    ["Mesleki muhakeme", "Esasta bağımsızlık", "Tarafsızlık", "Mesleki özen"],
    "BDS 200 prg. 13-g mesleki şüpheciliği sorgulayıcı bir yaklaşımla hareket ederek yanlışlığa işaret eden durumlara karşı "
    "dikkatli olma ve kanıtları titizlikle değerlendirme tutumu olarak tanımlar. Mesleki muhakeme ise bilgiye dayalı karar "
    "alırken eğitim, bilgi ve deneyimin kullanılmasıdır (prg. 13-f).", zorluk="easy")

P.q("BDS 200 prg. 15, A20-A22",
    f"{B200}, denetçinin mesleki şüpheciliği sürdürmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, yönetimin dürüst olduğuna dair geçmiş deneyimi varsa mesleki şüpheciliği azaltabilir.",
    ["Mesleki şüphecilik, elde edilen diğer kanıtlarla çelişen kanıtlara karşı dikkatli olmayı içerir.",
     "Belgelerin ve sorgulama cevaplarının güvenilirliğini sorgulamak mesleki şüpheciliğin parçasıdır.",
     "Denetçi, aksine bir sebep yoksa kayıt ve belgeleri gerçek kabul edebilir; şüphe varsa araştırır.",
     "Mesleki şüphecilik, ek denetim prosedürleri gerektirebilecek durumlara karşı uyanık olmayı gerektirir."],
    "BDS 200 prg. 15 ve A20-A22'ye göre denetçi mesleki şüpheciliği denetim boyunca sürdürür; aksini gösteren durum "
    "yoksa kayıt ve belgeleri gerçek kabul edebilir (A21). A22'ye göre yönetimin doğru ve dürüst olduğuna ilişkin kanaat, "
    "mesleki şüpheciliği devam ettirme sorumluluğunu ortadan kaldırmaz ve denetçi gerekli kanıttan daha azıyla yetinemez.")

P.q("BDS 200 prg. 13-f",
    f"{B200}, aşağıdakilerden hangisi “mesleki muhakeme” kavramını doğru tanımlar?",
    "Bilgiye dayalı kararlarda, mevzuat ve standartlar çerçevesinde eğitim, bilgi ve deneyimin kullanılmasıdır.",
    ["Yeterli ve uygun kanıtla desteklenmeyen kararlara, denetçinin kişisel tecrübesine dayanarak gerekçe bulma imkânı veren yargıdır.",
     "Hata veya hile kaynaklı yanlışlığa işaret eden durumlara karşı dikkatli olmayı içeren tutumdur.",
     "Denetim riskini sıfıra indirmek için gerekli olan prosedürlerin bütününü seçme yetkisidir.",
     "Bağımsız ve tarafsız bir yaklaşımla kanıtları titizlikle değerlendirmeyi içeren yargıdır."],
    "BDS 200 prg. 13-f'ye göre mesleki muhakeme, denetim sırasındaki şartlara uygun adımlara yönelik bilgiye dayalı "
    "kararlar alınırken ilgili mevzuat, BDS'ler, muhasebe ve etik standartlar çerçevesinde eğitim, bilgi ve deneyimin "
    "kullanılmasıdır. A27'ye göre muhakeme, kanıtla desteklenmeyen kararların gerekçesi olarak kullanılamaz.", zorluk="hard")

P.q("BDS 200 prg. 13-c",
    f"{B200}, “denetim riski” aşağıdakilerden hangisidir?",
    "Tablolar önemli yanlışlık içerirken denetçinin duruma uygun olmayan görüş vermesi riski",
    ["Tablolar önemli yanlışlık içermediği hâlde denetçinin olumsuz görüş vermesi riski",
     "Denetçinin, denetim ücretini tahsil edememesi veya sözleşmenin feshedilmesi riski",
     "İç kontrolün, bir yönetim beyanındaki önemli yanlışlığı zamanında önleyememesi riski",
     "Denetçinin uyguladığı prosedürlerle mevcut önemli bir yanlışlığı tespit edememesi riski"],
    "BDS 200 prg. 13-c'ye göre denetim riski, finansal tabloların önemli bir yanlışlık içermesine rağmen denetçinin duruma "
    "uygun olmayan bir görüş vermesi riskidir ve önemli yanlışlık riski ile tespit edememe riskinin bir fonksiyonudur. "
    "Diğer seçenekler kontrol riski ve tespit edememe riskini ya da denetim riskine dahil edilmeyen riskleri anlatır.")

P.q("BDS 200 prg. 13-h",
    f"{B200}, “önemli yanlışlık” riskinin yönetim beyanı düzeyindeki iki bileşeni aşağıdakilerin hangisinde doğru "
    "verilmiştir?",
    "Yapısal risk ve kontrol riski",
    ["Kontrol riski ve tespit edememe riski", "Yapısal risk ve tespit edememe riski",
     "Örnekleme riski ve örnekleme dışı risk", "İş riski ve denetim riski"],
    "BDS 200 prg. 13-h'ye göre önemli yanlışlık riski, finansal tabloların denetim öncesinde önemli yanlışlık içermesi "
    "riskidir ve yönetim beyanı düzeyinde yapısal risk ile kontrol riskinden oluşur. Tespit edememe riski denetçiye aittir "
    "ve denetim riskinin diğer bileşenidir.")

P.q("BDS 200 prg. 13-h-i",
    "Bir işletmenin türev finansal araçlarının gerçeğe uygun değeri, karmaşık modellere ve belirsiz varsayımlara "
    "dayanmaktadır. İşletmenin bu alandaki kontrolleri henüz dikkate alınmadan önce bile, ilgili yönetim beyanının önemli "
    f"yanlışlık içermeye açık olduğu değerlendirilmektedir. {B200} bu durum aşağıdakilerden hangisini ifade eder?",
    "Yapısal risk",
    ["Kontrol riski", "Tespit edememe riski", "Denetim riski", "Örnekleme riski"],
    "BDS 200 prg. 13-h-i'ye göre yapısal risk, ilgili kontroller dikkate alınmadan önce bir yönetim beyanının tek başına "
    "veya diğer yanlışlıklarla birlikte önemli olabilecek bir yanlışlık içermeye açık olmasıdır. Karmaşıklık ve belirsizlik "
    "BDS 315'teki yapısal risk faktörlerindendir.")

P.q("BDS 200 prg. 13-j, A42",
    f"{B200}, tespit edememe riskine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tespit edememe riski, denetçinin uyguladığı prosedürlerden bağımsız olarak işletmenin kontrollerine göre belirlenir.",
    ["Denetçi, belirli bir denetim riski düzeyinde önemli yanlışlık riski arttıkça daha düşük tespit edememe riskini kabul eder.",
     "Yeterli planlama ve ekibe uygun personel atanması, prosedürlerin etkinliğini artırarak bu riski azaltır.",
     "Tespit edememe riski azaltılabilir, ancak denetimin yapısal kısıtlamaları nedeniyle sıfıra indirilemez.",
     "Mesleki şüphecilik ile çalışmanın gözetimi ve gözden geçirilmesi de bu riskin azaltılmasına yardımcı olur."],
    "BDS 200 prg. 13-j'ye göre tespit edememe riski, denetçinin uyguladığı prosedürler neticesinde önemli bir yanlışlığın "
    "tespit edilememesi riskidir; prosedürlerin niteliği, zamanlaması ve kapsamıyla belirlenir. A42-A44 yeterli planlama, "
    "uygun personel, mesleki şüphecilik ve gözetimin bu riski azalttığını, ancak sıfırlanamayacağını açıklar.")

P.q("BDS 200 A45",
    f"{B200}, aşağıdakilerden hangisi denetimin yapısal kısıtlamalarının kaynakları arasında sayılmaz?",
    "Denetçinin önemlilik düzeyini mesleki muhakemesiyle belirlemesi",
    ["Finansal raporlamanın niteliği ve muhasebe tahminlerindeki belirsizlik",
     "Denetim prosedürlerinin niteliği",
     "Denetimin makul bir sürede yürütülmesi gerekliliği",
     "Denetimin makul bir maliyetle yürütülmesi gerekliliği"],
    "BDS 200 A45'e göre denetimin yapısal kısıtlamaları finansal raporlamanın niteliğinden, denetim prosedürlerinin "
    "niteliğinden ve denetimin makul süre ve maliyetle yürütülmesi gerekliliğinden kaynaklanır. Önemliliğin muhakemeyle "
    "belirlenmesi bir kısıtlama değil, BDS 320'nin gereğidir.")

P.q("BDS 200 A48",
    "Denetçi, zaman darlığı ve maliyet nedeniyle bir yönetim beyanı için ikna edici kanıt elde etmenin güç olduğunu "
    f"düşünmektedir. {B200} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zorluk, süre veya maliyet tek başına daha az ikna edici kanıtla yetinmek için geçerli sebep değildir.",
    ["Maliyet kanıtın faydasını aşıyorsa denetçi ilgili yönetim beyanını denetim kapsamından çıkarabilir.",
     "Zaman kısıtı varsa denetçi yönetimin yazılı beyanını tek başına yeterli kanıt olarak kabul edebilir.",
     "Denetçi, ek süre ve maliyet gerektiren prosedürleri bir sonraki yılın denetimine erteleyebilir.",
     "Makul güvence mutlak olmadığından denetçi bu alanda kanıt toplamadan olumlu görüş verebilir."],
    "BDS 200 A48'e göre alternatifi bulunmayan bir denetim prosedürünün zorluğu, süresi veya maliyeti kendi başına, "
    "denetçinin o prosedürü ihmal etmesi veya ikna edicilikten uzak kanıtla yetinmesi için geçerli bir sebep oluşturmaz.",
    zorluk="hard")

P.q("BDS 200 prg. 4",
    f"{B200}, denetlenen finansal tablolar ve yönetimin sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Tabloların denetlenmiş olması yönetimin ve üst yönetimin sorumluluklarını kaldırmaz.",
    ["Denetim raporu imzalandıktan sonra tabloların doğruluğundan sadece denetçi sorumlu olur.",
     "BDS'ler, yönetimin sorumluluklarını düzenleyen mevzuat hükümlerinin yerine geçer.",
     "Denetçi tabloların hazırlanmasına katıldığında yönetimin sorumluluğu denetçiye geçer.",
     "Üst yönetimden sorumlu olanlar, denetim yapıldığında finansal raporlama sürecini gözetmez."],
    "BDS 200 prg. 4'e göre denetime tabi tablolar üst yönetimin gözetiminde yönetim tarafından hazırlanır; BDS'ler "
    "yönetime sorumluluk yüklemez ve mevzuatın yerine geçmez; tabloların denetlenmiş olması yönetimin ve üst yönetimden "
    "sorumlu olanların sorumluluklarını ortadan kaldırmaz.")

P.q("BDS 200 prg. 13-k",
    f"{B200}, finansal tabloların gerçeğe uygun sunumu için yönetimin çerçevenin belirli bir hükmünden sapmasının gerekli "
    "olabileceğini açıkça kabul eden finansal raporlama çerçevesi aşağıdakilerden hangisidir?",
    "Gerçeğe uygun sunum çerçevesi",
    ["Uygunluk çerçevesi", "Özel amaçlı çerçeve", "Genel amaçlı olmayan çerçeve", "Vergi esaslı raporlama çerçevesi"],
    "BDS 200 prg. 13-k'ye göre gerçeğe uygun sunum çerçevesi, çerçevenin gerektirdiğinin ötesinde açıklama yapılmasını veya "
    "çok istisnai durumlarda belirli bir hükümden sapılmasını kabul eden çerçevedir. Bu kabulleri içermeyen çerçeve "
    "uygunluk çerçevesidir.")

P.q("BDS 200 prg. 13-m",
    f"{B200}, “yanlışlık” kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yanlışlık sadece tutar farklılıklarını kapsar; sınıflandırma farkı yanlışlık sayılmaz.",
    ["Yanlışlık, raporlanan kalem ile çerçeveye göre olması gereken kalem arasındaki farklılıktır.",
     "Yanlışlıklar hata veya hileden kaynaklanabilir.",
     "Bir kalemin sunumunun çerçeveye aykırı olması da yanlışlık oluşturur.",
     "Eksik yapılan açıklamalar da yanlışlık tanımının kapsamına girer."],
    "BDS 200 prg. 13-m'ye göre yanlışlık, raporlanan bir kalemin tutarı, sınıflandırılması, sunumu veya açıklaması ile "
    "çerçeveye göre olması gereken tutarı, sınıflandırılması, sunumu veya açıklaması arasındaki farklılıktır ve hata ya da "
    "hileden kaynaklanabilir.")

P.q("BDS 200 prg. 13-l",
    f"{B200}, işletmenin stratejik yönetimi ve hesap verebilirliğine ilişkin yükümlülüklerin ve finansal raporlama "
    "sürecinin gözetiminden sorumlu kişi, kişiler veya yapılar aşağıdakilerden hangisi ile ifade edilir?",
    "Üst yönetimden sorumlu olanlar",
    ["Yönetim", "İç denetim birimi", "Kilit yöneticiler", "Genel kurul"],
    "BDS 200 prg. 13-l'ye göre üst yönetimden sorumlu olanlar, işletmenin stratejik yönetimi ve hesap verebilirliğine "
    "ilişkin yükümlülüklerin gözetiminden sorumlu kişi veya yapılardır; bu sorumluluk finansal raporlama sürecinin "
    "gözetimini de içerir. Bazı durumlarda icracı yöneticiler de bu grupta yer alabilir.", zorluk="easy")

P.q("BDS 200 prg. 12",
    "Denetçi, makul güvence elde edememiş ve raporunda vereceği sınırlı olumlu görüşün hedeflenen kullanıcılar bakımından "
    f"yetersiz kalacağı sonucuna varmıştır. {B200} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Görüş bildirmekten kaçınmak veya mevzuat izin veriyorsa çekilmek",
    ["Sınırlı olumlu görüşü dikkat çekilen hususlar paragrafıyla desteklemek",
     "Olumlu görüş verip sınırlamayı diğer hususlar paragrafında açıklamak",
     "Raporu düzenlemeyip durumu sözlü olarak üst yönetime bildirmek",
     "Makul güvence elde edilene kadar denetimi süresiz olarak uzatmak"],
    "BDS 200 prg. 12'ye göre makul güvencenin elde edilemediği ve sınırlı olumlu görüşün kullanıcılara raporlama amaçları "
    "bakımından yetersiz kaldığı durumlarda denetçi görüş bildirmekten kaçınır veya mevzuat izin veriyorsa denetimden "
    "çekilir.")

P.q("BDS 200 prg. 18-19",
    f"{B200}, denetçinin BDS'lere uyumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Denetçi, denetimle ilgili tüm BDS'lere uyar.",
    ["Denetçi, işletmenin büyüklüğüne göre uygun gördüğü BDS'leri seçerek uygulayabilir.",
     "Denetçi raporunda BDS'lere uyulduğunu belirtebilmek için BDS'lerin çoğuna uyması yeterlidir.",
     "Sadece KAYİK denetimlerinde bütün BDS'lere uyulması zorunludur.",
     "BDS'lerin uygulama bölümleri bağlayıcı olmadığından ana hükümlere uyulması gerekmez."],
    "BDS 200 prg. 18-20'ye göre denetçi denetimle ilgili tüm BDS'lere uyar; bir BDS yürürlükteyse ve ele aldığı şartlar "
    "mevcutsa denetimle ilgilidir. Denetçi, ilgili tüm BDS'lere uymadıkça raporunda BDS'lere uyulduğunu belirtemez.")

# ================================================================ BDS 210: ön şartlar ve sözleşme
P.q("BDS 210 prg. 6",
    f"{B210}, aşağıdakilerden hangisi yönetimin denetimin ön şartı olarak anlayıp üstlendiğini teyit ettiği "
    "sorumluluklardan biri değildir?",
    "Denetçinin tespit ettiği iç kontrol eksikliklerini üst yönetime raporlama sorumluluğu",
    ["Finansal tabloların geçerli finansal raporlama çerçevesine uygun hazırlanması sorumluluğu",
     "Hata veya hile kaynaklı önemli yanlışlık içermeyen tablolar için gerekli gördüğü iç kontrole ilişkin sorumluluk",
     "Denetçiye, tabloların hazırlanmasıyla ilgili muttali olduğu tüm bilgilere erişim sağlama sorumluluğu",
     "Denetçinin kanıt toplamak için gerekli gördüğü kişilerle kısıtlamasız görüşme imkânı sağlama sorumluluğu"],
    "BDS 210 prg. 6-b'ye göre yönetim; tabloların çerçeveye uygun hazırlanması, gerekli gördüğü iç kontrol ve denetçiye "
    "bilgiye erişim, ilave bilgi ve kısıtlamasız görüşme imkânı sağlama sorumluluklarını kabul eder. İç kontrol "
    "eksikliklerini üst yönetime bildirmek BDS 265'e göre denetçinin sorumluluğudur.")

P.q("BDS 210 prg. 7",
    "Bir işletmenin yönetimi, denetim sözleşmesinin kabulünden önce, denetçinin satış gelirlerine ilişkin dış teyit "
    "göndermesini yasaklayan bir şart önermiştir. Denetçi bu kısıtlamanın görüş bildirmekten kaçınmayı gerektireceğine "
    f"inanmaktadır. {B210} denetçi ne yapmalıdır?",
    "Mevzuatla zorunlu değilse bu sözleşmeyi bağımsız denetim sözleşmesi olarak kabul etmez.",
    ["Sözleşmeyi kabul eder ve raporunda kapsam sınırlamasını dikkat çekilen hususlarda açıklar.",
     "Sözleşmeyi, sadece satış gelirleri dışındaki alanlar için şartlı olarak imzalar.",
     "Kısıtlamayı makul bulursa sınırlı bağımsız denetim sözleşmesi teklif ederek işe başlar.",
     "Durumu KGK'ya bildirir ve Kurumun vereceği karara göre sözleşmeyi imzalar."],
    "BDS 210 prg. 7'ye göre yönetim veya üst yönetim, sözleşmenin kabulünden önce denetçinin çalışma kapsamını görüş "
    "bildirmekten kaçınmasını gerektirecek şekilde sınırlandıran bir şart önerirse denetçi, mevzuatla zorunlu kılınmadıkça "
    "bu sınırlı sözleşmeyi bağımsız denetim sözleşmesi olarak kabul etmez.")

P.q("BDS 210 prg. 10",
    f"{B210}, aşağıdakilerden hangisi yazılı denetim sözleşmesinde yer alması gereken hususlardan biri değildir?",
    "Denetçinin vereceği görüşün türüne ilişkin önceden verilen taahhüt",
    ["Finansal tabloların denetiminin amacı ve kapsamı",
     "Denetçinin ve yönetimin sorumlulukları",
     "Tabloların hazırlanmasında kullanılacak geçerli finansal raporlama çerçevesini belirten açıklama",
     "Raporların beklenen şekil ve içeriğine atıf ile bunlardan farklı olabileceğine ilişkin açıklama"],
    "BDS 210 prg. 10'a göre sözleşme; denetimin amacı ve kapsamını, denetçinin ve yönetimin sorumluluklarını, geçerli "
    "çerçeveyi ve raporların beklenen şekil ve içeriğine atıf ile farklılık gösterebileceği açıklamasını içerir. Görüşün "
    "türü önceden taahhüt edilemez; kanıtlara göre belirlenir.")

P.q("BDS 210 prg. 13",
    f"{B210}, tekrarlayan denetimlerde denetim sözleşmesi şartlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Şartların revize edilmesi veya işletmeye hatırlatılması gerekip gerekmediğini değerlendirir.",
    ["Tekrarlayan denetimlerde sözleşme, önceki yılın şartları aynı kalsa da her yıl baştan yazılı olarak yeniden imzalanır.",
     "Sözleşme şartları ilk yıl belirlendikten sonra değişmez; denetçi değerlendirme yapmaz.",
     "Tekrarlayan denetimlerde yönetimin sorumluluklarını yeniden kabul etmesi aranmaz.",
     "Sözleşme şartları sadece denetçi değiştiğinde yeniden değerlendirilir."],
    "BDS 210 prg. 13'e göre tekrarlayan denetimlerde denetçi, sözleşme şartlarının revize edilmesini gerektiren durumlar "
    "olup olmadığını ve mevcut şartların işletmeye hatırlatılması gerekip gerekmediğini değerlendirir; her yıl yeni "
    "sözleşme zorunlu değildir.")

P.q("BDS 210 prg. 14-15",
    "Denetimin tamamlanmasına kısa bir süre kala yönetim, stoklara ilişkin kanıt sağlayamayacağını anlamış ve denetçiden "
    f"sözleşmeyi sınırlı bağımsız denetime dönüştürmesini istemiştir. {B210} bu talebe ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Yeterli kanıtın elde edilememesine dayanan bu değişiklik talebi genellikle makul gerekçe sayılmaz.",
    ["Yönetim talep ettiğinden denetçi değişikliği kabul eder.",
     "Daha düşük güvence talebi, yönetimden geldiği için makul gerekçe sayılır.",
     "Denetçi değişikliği kabul eder ve raporunda orijinal sözleşmeye ve değişiklik gerekçesine atıf yapar.",
     "Sözleşme değişikliği ancak Kurumun onayıyla kabul edilebilir."],
    "BDS 210 prg. 14-15 ve A32-A33'e göre denetçi makul gerekçe olmadıkça şartlarda değişikliği kabul etmez. Kullanıcının "
    "ihtiyacının değişmesi makul gerekçe olabilir; ancak değişiklik talebi yanlış, eksik veya tatmin edici olmayan "
    "bilgiye veya kapsam sınırlamasına dayanıyorsa makul kabul edilmez.", zorluk="hard")

P.q("BDS 210 prg. 17",
    "Denetçi, sözleşme şartlarında önerilen bir değişikliği kabul etmemiş; yönetim ise denetimin mevcut sözleşmeye göre "
    f"devam etmesine izin vermemektedir. {B210} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Mevzuat izin veriyorsa çekilir; durumu diğer taraflara raporlama yükümlülüğünü değerlendirir.",
    ["Yönetimin önerdiği değişikliği kabul ederek denetimi yeni şartlarla tamamlar ve raporunda bu durumu açıklar.",
     "Denetime devam eder ve raporunda olumsuz görüş bildirir.",
     "Denetimden çekilir; durumu başka taraflara raporlama yükümlülüğünü değerlendirmez.",
     "Denetimi askıya alır ve yönetimin fikrini değiştirmesini süresiz olarak bekler."],
    "BDS 210 prg. 17'ye göre denetçi mevzuatın izin vermesi hâlinde denetimden çekilir ve durumu üst yönetimden sorumlu "
    "olanlar, şirket sahipleri veya düzenleyici kurumlar gibi diğer taraflara raporlama yükümlülüğü olup olmadığına karar "
    "verir.")

P.q("BDS 210 prg. 6-a",
    f"{B210}, denetimin ön şartlarının mevcut olup olmadığını belirlerken denetçinin yapması gereken aşağıdakilerden "
    "hangisidir?",
    "Uygulanacak finansal raporlama çerçevesinin kabul edilebilir olup olmadığını belirlemek",
    ["İşletmenin önceki yıllara ait vergi incelemesi raporlarının tamamını inceleyip vergi riskini ölçmek",
     "Yönetimin denetim ücretini peşin ödemeyi kabul edip etmediğini belirlemek",
     "İç kontrol sisteminin etkin çalıştığına dair makul güvence elde etmek",
     "Önceki denetçinin bir sonraki yıla ilişkin görüşünü almak"],
    "BDS 210 prg. 6'ya göre denetimin ön şartlarının varlığı için denetçi, uygulanacak finansal raporlama çerçevesinin "
    "kabul edilebilir olup olmadığını belirler ve yönetimin sorumluluklarını anladığı ve üstlendiği konusunda mutabakat "
    "sağlar.")

# ================================================================ BDS 220 (Revize): sorumlu denetçi
P.q("BDS 220 (Revize)",
    f"{B220}, denetimde kalitenin yönetilmesi ve sağlanmasına ilişkin nihai sorumluluk aşağıdakilerden hangisine aittir?",
    "Sorumlu denetçiye",
    ["Kaliteyi gözden geçiren kişiye", "Denetim ekibindeki başdenetçiye",
     "Denetlenen işletmenin üst yönetimine", "Kamu Gözetimi Kurumuna"],
    "BDS 220 (Revize)'ye göre sorumlu denetçi, denetimde kalitenin yönetilmesi ve sağlanmasına ilişkin genel sorumluluğu "
    "üstlenir ve denetim boyunca yeterli ve uygun şekilde sürece dahil olur. Kalitenin gözden geçirilmesi bu sorumluluğu "
    "değiştirmez.", zorluk="easy")

P.q("BDS 220 (Revize)",
    f"{B220}, sorumlu denetçinin sorumluluklarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gözden geçirmeyi kaliteyi gözden geçiren kişiye devreden sorumlu denetçinin bu alanda sorumluluğu kalmaz.",
    ["Sorumlu denetçi, ekibin yönlendirilmesi, gözetimi ve yapılan işin gözden geçirilmesinden sorumludur.",
     "Sorumlu denetçi, zor veya tartışmalı konularda ekibin gerekli istişareleri yapmasını sağlar.",
     "Sorumlu denetçi, rapor tarihinde veya öncesinde çalışma kâğıtlarını gözden geçirerek kanıtın yeterliliğinden emin olur.",
     "Sorumlu denetçi, ekip içinde veya kaliteyi gözden geçiren kişiyle görüş ayrılıklarının çözülmesini sağlar."],
    "BDS 220 (Revize)'ye göre sorumlu denetçi yönlendirme, gözetim ve gözden geçirmeden, istişarelerden ve görüş "
    "ayrılıklarının çözümünden sorumludur; bazı görevleri ekip üyelerine verebilir, ancak kalitenin yönetilmesi ve "
    "sağlanmasına ilişkin genel sorumluluk sorumlu denetçide kalır.")

# ================================================================ BDS 230: belgelendirme
P.q("BDS 230 prg. 8",
    f"{B230}, denetim belgelendirmesinin yeterliliğini değerlendirmede esas alınan ölçüt aşağıdakilerden hangisidir?",
    "Denetimle önceden bağlantısı olmayan deneyimli bir denetçinin çalışmayı anlayabilmesi",
    ["Belgelerin, denetlenen işletmenin yönetimi tarafından her sayfada imzalanmış olması",
     "Çalışma kâğıtlarının, denetim ekibi dışındaki kişilerin anlayamayacağı kadar özet olması",
     "Belgelendirmenin, denetim raporu yayımlandıktan sonra tüm ekip tarafından toplu hâlde hazırlanmış olması",
     "Denetim dosyasında sadece olumlu sonuç veren prosedürlerin yer alması"],
    "BDS 230 prg. 8'e göre denetçi, denetimle daha önce bağlantısı olmayan deneyimli bir denetçinin uygulanan prosedürlerin "
    "niteliği, zamanlaması ve kapsamını, sonuçlarını, elde edilen kanıtları ve önemli konularla ulaşılan sonuçları "
    "anlayabilmesine yetecek belgelendirmeyi hazırlar.")

P.sayisal("BDS 230 A21",
    f"{B230}, çalışma kâğıtlarının nihai denetim dosyasında birleştirilmesi için uygun süre genellikle denetçi raporu "
    "tarihinden itibaren en fazla kaç gündür?",
    "60", ["15", "30", "90", "120"],
    "BDS 230 prg. 14 ve A21'e göre denetçi, rapor tarihinden sonra nihai dosyanın oluşturulmasına yönelik idari süreci "
    "zamanında tamamlar; bunun için uygun süre genellikle rapor tarihinden itibaren en fazla altmış gündür.", zorluk="easy")

P.q("BDS 230 prg. 15-16",
    f"{B230}, nihai denetim dosyası tamamlandıktan sonraki işlemlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Nihai dosya tamamlandıktan sonra gereksiz kâğıtlar saklama süresi dolmadan imha edilebilir.",
    ["Denetçi, çalışma kâğıtlarını saklama süresi sona ermeden silemez, atamaz veya yok edemez.",
     "Dosya tamamlandıktan sonra değişiklik veya ekleme gerekirse bunun özel sebepleri belgelendirilir.",
     "Sonradan yapılan değişikliklerin ne zaman ve kim tarafından yapılıp gözden geçirildiği belgelendirilir.",
     "Rapor tarihinden sonra dosyada birleştirme işlemi, yeni denetim prosedürlerinin uygulanmasını içermez."],
    "BDS 230 prg. 15'e göre nihai dosya birleştirildikten sonra çalışma kâğıtları saklama süresi sona ermeden silinemez, "
    "atılamaz veya yok edilemez. Prg. 16 sonradan yapılan değişikliklerin sebebini, zamanını ve yapanı belgelendirmeyi "
    "ister; A22'ye göre birleştirme idari bir süreçtir ve yeni prosedür içermez.")

P.q("BDS 230 prg. 13",
    "Denetçi raporu tarihinden sonra, denetçinin rapor tarihinde var olan ve bilseydi raporunu değiştirebileceği bir olayı "
    f"öğrendiği ve yeni prosedürler uyguladığı istisnai bir durum ortaya çıkmıştır. {B230} bu durumda aşağıdakilerden "
    "hangisi belgelendirilmez?",
    "Denetim ekibindeki denetçilerin o döneme ait çalışma saatleri ve ücret dökümü",
    ["Karşılaşılan şartlar",
     "Uygulanan yeni veya ek prosedürler, elde edilen kanıtlar ve ulaşılan sonuçlar ile bunların rapora etkisi",
     "Çalışma kâğıtlarında yapılan değişikliklerin ne zaman ve kim tarafından yapılıp gözden geçirildiği",
     "Değişiklik yapmayı gerektiren olayla ilgili yönetimle yapılan önemli görüşmeler"],
    "BDS 230 prg. 13'e göre istisnai durumlarda denetçi karşılaşılan şartları, uygulanan yeni prosedürleri, elde edilen "
    "kanıtları, ulaşılan sonuçları ve rapora etkisini, değişikliklerin ne zaman ve kim tarafından yapılıp gözden "
    "geçirildiğini belgelendirir. Ücret dökümü bu kapsamda değildir.", zorluk="hard")

P.q("BDS 230 prg. 9",
    f"{B230}, belirli kalemlerin veya konuların test edilmesini belgelendirirken denetçinin kaydetmesi gereken hususlar "
    "arasında aşağıdakilerden hangisi yer alır?",
    "Test edilen kalemlerin ayırt edici özellikleri, çalışmayı yapan ve tarihi",
    ["Test edilen kalemlerin bulunduğu belgelerin asıllarının tamamı",
     "Test edilen her kalem için yönetimin ayrı ayrı imzaladığı yazılı beyan",
     "Test edilmeyen kalemlerin neden test edilmediğine ilişkin yönetim açıklaması",
     "Test edilen kalemlerin denetlenen işletmeye maliyetinin ayrıntılı dökümü"],
    "BDS 230 prg. 9'a göre denetçi, test edilen kalemlerin ayırt edici özelliklerini, çalışmayı yapan kişiyi ve tarihini, "
    "çalışmayı gözden geçiren kişiyi ve gözden geçirmenin tarihini ve kapsamını kaydeder.")

# ================================================================ BDS 300: planlama
P.q("BDS 300 prg. 7-9",
    f"{B300}, genel denetim stratejisi ile denetim planı arasındaki ilişkiye dair aşağıdakilerden hangisi doğrudur?",
    "Strateji kapsam, zamanlama ve yönü belirler; plan prosedürlerin niteliği, zamanlaması ve kapsamını içerir.",
    ["Denetim planı önce hazırlanır; genel strateji ise denetim sonunda plana göre yazılır.",
     "Genel strateji risk değerlendirme prosedürlerinin ayrıntısını, denetim planı ise ekip üyelerinin ücret ve sürelerini içerir.",
     "Strateji ve plan bir kez hazırlanır ve denetim boyunca değiştirilemez.",
     "Denetim planı sadece ilk denetimlerde, genel strateji ise tekrarlayan denetimlerde hazırlanır."],
    "BDS 300 prg. 7'ye göre genel denetim stratejisi denetimin kapsamını, zamanlamasını ve yönünü belirler ve planın "
    "geliştirilmesine rehberlik eder; prg. 9'a göre denetim planı risk değerlendirme prosedürleri ile müteakip "
    "prosedürlerin niteliği, zamanlaması ve kapsamını içerir. Prg. 10'a göre ikisi de gerektiğinde güncellenir.", zorluk="hard")

P.q("BDS 300 prg. 10",
    "Denetim sırasında denetçi, işletmenin önemli bir bağlı ortaklığını satmak üzere olduğunu beklenmedik şekilde öğrenmiştir. "
    f"{B300} bu gelişme karşısında denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Gerekirse genel stratejiyi ve denetim planını güncelleyip değiştirir.",
    ["Planlama tamamlandığından stratejiyi değiştirmez, bilgiyi gelecek yıla not eder.",
     "Denetim planını değiştirmez, ancak durumu raporunda dikkat çekilen hususlarda açıklar.",
     "Denetimi durdurur ve yeni bir sözleşme imzalanmasını bekler.",
     "Bilgiyi yönetimin sorumluluğunda sayarak değerlendirme dışında bırakır."],
    "BDS 300 prg. 10'a göre genel denetim stratejisi ve denetim planı gerektiğinde denetim sırasında güncellenir ve "
    "değiştirilir. Beklenmedik olaylar, şartlardaki değişiklikler veya elde edilen kanıtlar bunu gerektirebilir; önemli "
    "değişiklikler ve nedenleri belgelendirilir (prg. 12).")

P.q("BDS 300 prg. 13",
    f"{B300}, ilk defa yapılan bir denetimde planlama aşamasında denetçinin ilave olarak yapması gereken aşağıdakilerden "
    "hangisidir?",
    "Etik hükümlere uygun olarak önceki denetçiyle iletişime geçmek",
    ["Önceki dönem tablolarını baştan denetleyerek ayrı bir görüş bildirmek",
     "Önceki denetçinin çalışma kâğıtlarını izin aranmaksızın incelemek",
     "Planlamayı atlayarak doğrudan maddi doğrulama testlerine başlamak",
     "Önceki denetçinin görüşünü aynen kabul ederek açılış bakiyelerini test etmemek"],
    "BDS 300 prg. 13'e göre ilk denetimlerde denetçi, müşteri ilişkisinin kabulü prosedürlerini uygular ve önceki denetçi "
    "değişikliği varsa mevzuata uygun olarak önceki denetçiyle iletişim kurar. Açılış bakiyeleri ise BDS 510 uyarınca "
    "ayrıca ele alınır.")

P.q("BDS 300 prg. 2, A1",
    f"{B300}, yeterli planlamanın denetime sağladığı katkılar arasında aşağıdakilerden hangisi yer almaz?",
    "Denetim riskinin sıfıra indirilmesini güvence altına almak",
    ["Denetimin önemli alanlarına dikkatin yoğunlaştırılmasına yardımcı olmak",
     "Muhtemel problemlerin zamanında belirlenip çözüme kavuşturulmasına yardımcı olmak",
     "Denetimin etkin ve verimli yürütülmesi için uygun organize edilmesine yardımcı olmak",
     "Ekip üyelerinin uygun şekilde yönlendirilmesine, gözetimine ve işlerinin gözden geçirilmesine yardımcı olmak"],
    "BDS 300 prg. 2'ye göre yeterli planlama önemli alanlara odaklanmaya, sorunların zamanında çözümüne, denetimin etkin "
    "organize edilmesine, uygun ekip seçimine ve ekibin yönlendirilmesi ile gözden geçirilmesine yardımcı olur. Denetim "
    "riski hiçbir planlama ile sıfırlanamaz (BDS 200 A45).")

P.q("BDS 300 prg. 5",
    f"{B300}, denetimin planlanmasına kimlerin katılması gerekir?",
    "Sorumlu denetçi ve denetim ekibinin diğer kilit üyeleri",
    ["Sadece denetim ekibindeki denetçi yardımcıları",
     "Denetlenen işletmenin iç denetim birimi yöneticileri",
     "Kaliteyi gözden geçiren kişi ve denetim şirketinin ortakları",
     "Denetlenen işletmenin yönetim kurulu üyeleri"],
    "BDS 300 prg. 5'e göre sorumlu denetçi ve denetim ekibinin diğer kilit üyeleri, ekip üyelerinin tartışmalarının "
    "planlanması ve bunlara katılım dahil denetimin planlanmasına katılır.", zorluk="easy")

P.q("BDS 300 A3",
    f"{B300}, denetim planının bazı unsurlarının yönetimle görüşülmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Görüşülebilir; ancak prosedürlerin öngörülebilir hâle gelmemesine dikkat edilir.",
    ["Denetim planının tamamı ve uygulanacak her prosedür yönetimle önceden paylaşılır.",
     "Denetim planı denetçiye ait olduğundan unsurları yönetimle görüşülemez.",
     "Görüşülen unsurlar hakkında sorumluluk yönetime geçer.",
     "Planın görüşülmesi durumunda denetim sözleşmesi yeniden imzalanır."],
    "BDS 300 A3'e göre denetçi planın bazı unsurlarını yönetimle görüşebilir; ancak genel strateji ve plan denetçinin "
    "sorumluluğundadır ve görüşmelerde, prosedürlerin öngörülebilir hâle gelerek denetimin etkinliğini zedelememesine "
    "dikkat edilir.")

# ================================================================ BDS 260: üst yönetimle iletişim
P.q("BDS 260 prg. 14-16",
    f"{B260}, denetçinin üst yönetimden sorumlu olanlarla iletişim kuracağı konular arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Denetim ekibi üyelerinin kişisel performans değerlendirmeleri",
    ["Finansal tabloların denetimine ilişkin denetçinin sorumlulukları",
     "Denetimin planlanan kapsamı ve zamanlaması",
     "Denetimden kaynaklanan önemli bulgular",
     "Borsada işlem gören işletmelerde bağımsızlığa ilişkin hususlar"],
    "BDS 260 prg. 14-17'ye göre denetçi üst yönetimle denetçinin sorumlulukları, planlanan kapsam ve zamanlama, denetimden "
    "kaynaklanan önemli bulgular ve borsada işlem gören işletmelerde bağımsızlık hususlarında iletişim kurar. Ekip "
    "üyelerinin performansı şirketin iç konusudur.")

P.q("BDS 260 prg. 19",
    f"{B260}, önemli bulgulara ilişkin iletişimin şekline dair aşağıdakilerden hangisi doğrudur?",
    "Sözlü iletişim yetersiz kalacaksa önemli bulgular yazılı olarak bildirilir.",
    ["Önemli bulgular sözlü bildirilir; yazılı bildirim sadece yönetim talep ederse yapılır.",
     "Önemli bulgular sadece denetim raporunda açıklanır; ayrı bir iletişim kurulmaz.",
     "Önemli bulguların yazılı bildirimi, denetim raporunun yerine geçer.",
     "Denetim sırasında görüşülen ve çözülen konular da ayrıca yazılı olarak bildirilir."],
    "BDS 260 prg. 19'a göre denetçi, mesleki muhakemesine göre sözlü iletişimin yeterli olmayacağı durumlarda önemli "
    "bulgular hakkında yazılı iletişim kurar. Yazılı iletişim, denetim sırasında ele alınıp çözülen konuların tamamını "
    "içermek zorunda değildir.", zorluk="hard")

P.q("BDS 260 prg. 22",
    f"{B260}, denetçi ile üst yönetimden sorumlu olanlar arasındaki iki yönlü iletişimin yeterliliğine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Denetçi yeterliliği değerlendirir; yetersizse bunun risk değerlendirmesine etkisini değerlendirir.",
    ["İletişimin yeterliliğini üst yönetimden sorumlu olanlar değerlendirir ve sonucu yazılı olarak denetçiye bildirir.",
     "İki yönlü iletişim yetersiz kalırsa denetçi görüş bildirmekten kaçınır.",
     "İletişim, denetim raporunun yayımlanmasından sonra kurulur ve değerlendirilir.",
     "İletişimin yeterliliği, sadece KAYİK denetimlerinde değerlendirilir."],
    "BDS 260 prg. 22'ye göre denetçi, iki yönlü iletişimin denetimin amacı bakımından yeterli olup olmadığını değerlendirir; "
    "yeterli değilse önemli yanlışlık risklerine ve yeterli ve uygun kanıt elde etme becerisine etkisini değerlendirir ve "
    "uygun adımları atar.")

# ================================================================ karma: TDS kavramları
P.q("BDS 200, BDS 210 prg. 6-b",
    f"{TDS}, aşağıdakilerden hangisi yönetimin ve uygun hâllerde üst yönetimden sorumlu olanların “ön kabul” "
    "sorumluluklarından biri değildir?",
    "Denetçinin önerdiği düzeltmelerin tamamını tartışmasız kabul etme sorumluluğu",
    ["Denetçinin talep edebileceği ilave bilgileri sağlama sorumluluğu",
     "Gerçeğe uygun sunum dahil tabloları geçerli çerçeveye uygun hazırlama sorumluluğu",
     "Denetçiye muttali olunan tüm kayıt ve belgelere erişim imkânı sağlama sorumluluğu",
     "Kanıt toplamak için işletme içinde gerekli görülen kişilerle kısıtlamasız görüşme sağlama sorumluluğu"],
    "BDS 200 prg. 4 ve BDS 210 prg. 6-b'ye göre ön kabul sorumlulukları; tabloların çerçeveye uygun hazırlanması, gerekli iç "
    "kontrol ve denetçiye bilgi erişimi, ilave bilgi ile kısıtlamasız görüşme imkânı sağlanmasıdır. Düzeltmeleri kabul "
    "yönetimin kararıdır; düzeltilmeyen yanlışlıklar BDS 450'ye göre değerlendirilir.")

P.q("BDS 200 prg. A42",
    f"{TDS}, aşağıdakilerden hangisi tespit edememe riskini kabul edilebilir düzeye indirmek bağlamında bir denetim "
    "prosedürünün ve uygulanmasının etkinliğini artırmaya yardımcı olmaz?",
    "Denetim ücretinin denetim sonucuna bağlı olarak belirlenmesi",
    ["Yeterli planlama yapılması",
     "Denetim ekibine uygun personelin atanması",
     "Mesleki şüpheciliğin uygulanması",
     "Yürütülen çalışmanın yönlendirilmesi, gözetimi ve gözden geçirilmesi"],
    "BDS 200 A42'ye göre yeterli planlama, ekibe uygun personel atanması, mesleki şüpheciliğin uygulanması ve çalışmanın "
    "yönlendirilmesi, gözetimi ve gözden geçirilmesi prosedürlerin etkinliğini artırarak tespit edememe riskini azaltır. "
    "Sonuca bağlı ücret ise bağımsızlığı zedeler.")

P.oncul("BDS 200 prg. 13",
    f"{B200} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Denetim kanıtının yeterliliği, kanıtın miktarının ölçütüdür.",
     "Denetim kanıtının uygunluğu, kanıtın ihtiyaca uygunluğu ve güvenilirliğiyle ilgili kalitesinin ölçütüdür.",
     "Daha fazla kanıt elde edilmesi, düşük kaliteli kanıtı telafi eder.",
     "Kanıt, muhasebe kayıtlarındaki bilgiler ile diğer bilgileri içerir."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "BDS 200 prg. 13-b'ye göre kanıt, muhasebe kayıtlarındaki ve diğer bilgilerdir; yeterlilik miktarın, uygunluk ihtiyaca "
    "uygunluk ve güvenilirlik bakımından kalitenin ölçütüdür (I, II, IV). BDS 500 A4'e göre daha fazla kanıt elde "
    "edilmesi düşük kaliteli kanıtı telafi etmeyebilir (III yanlış).")

P.q("BDS 200 prg. 6",
    f"{B200}, önemlilik kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, tabloların bütünü açısından önemli olmayan yanlışlıkların da tespit edilmesinden sorumludur.",
    ["Önemlilik, belirlenen yanlışlıkların denetime ve düzeltilmeyenlerin tablolara etkisinin değerlendirilmesinde uygulanır.",
     "Yanlışlıklar kullanıcıların ekonomik kararlarını etkilemesi makul ölçüde bekleniyorsa önemli kabul edilir.",
     "Önemlilik yargılarına içinde bulunulan şartlar ışığında ulaşılır.",
     "Önemlilik yargıları, yanlışlığın büyüklüğü veya mahiyeti ya da ikisinin birleşiminden etkilenir."],
    "BDS 200 prg. 6'ya göre önemlilik yanlışlıkların etkisinin değerlendirilmesinde uygulanır; kullanıcıların ekonomik "
    "kararlarını etkilemesi makul ölçüde beklenen yanlışlıklar önemlidir. Denetçi görüşü tabloları bir bütün olarak ele "
    "alır ve denetçi bütün açısından önemli olmayan yanlışlıkların tespitinden sorumlu değildir.")

P.q("BDS 200 prg. 7",
    f"{B200}, denetçinin makul güvence elde etmesi için BDS'lerin zorunlu kıldığı işler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Tüm işlemleri ve hesap bakiyelerini tek tek inceleyerek yanlışlık bulunmadığını kanıtlamak",
    ["İşletme ve çevresine ilişkin bilgilere dayanarak önemli yanlışlık risklerini belirlemek ve değerlendirmek",
     "Değerlendirilen risklere uygun karşılıklar tasarlayıp uygulayarak yeterli ve uygun kanıt elde etmek",
     "Elde edilen kanıtlardan çıkardığı sonuçlara dayanarak tablolar hakkında bir görüş oluşturmak",
     "Denetimin planlanması ve yürütülmesi süresince mesleki muhakeme kullanıp mesleki şüpheciliği sürdürmek"],
    "BDS 200 prg. 7'ye göre BDS'ler denetçinin mesleki muhakeme ve şüphecilikle; riskleri belirleyip değerlendirmesini, "
    "risklere karşılık vererek yeterli ve uygun kanıt elde etmesini ve sonuçlara dayanarak görüş oluşturmasını zorunlu "
    "kılar. Tüm işlemlerin tek tek incelenmesi gerekmez; A48'e göre denetim yapısı gereği seçici testlere dayanır.")

P.q("BDS 200 prg. 14",
    f"{B200}, finansal tabloların denetimine ilişkin etik hükümlere uyum bakımından aşağıdakilerden hangisi doğrudur?",
    "Denetçi, bağımsızlık dahil finansal tablo denetimleriyle ilgili etik hükümlere uyar.",
    ["Bağımsızlık sadece KAYİK denetimlerinde aranır; diğer denetimlerde etik hükümler bağlayıcı değildir.",
     "Denetçi, etik hükümlerle BDS'ler çatıştığında BDS'leri esas alır.",
     "Etik hükümlere uyum, denetim ekibindeki sorumlu denetçi dışındaki kişiler için aranmaz.",
     "Etik hükümler sadece denetim sözleşmesi imzalanmadan önce dikkate alınır."],
    "BDS 200 prg. 14'e göre denetçi, bağımsızlığa ilişkin olanlar dahil finansal tablo denetimleriyle ilgili etik "
    "hükümlere uyar. Etik hükümler denetimin tamamı boyunca ve ekibin tüm üyeleri için geçerlidir.")

P.q("BDS 210 prg. 11",
    f"{B210}, sözleşme şartlarının ilgili mevzuatta yeterince ayrıntılı düzenlendiği durumlarla ilgili aşağıdakilerden "
    "hangisi doğrudur?",
    "Bu düzenlemelerin geçerli olduğunu ve yönetimin sorumluluklarını üstlendiğini belirtmekle yetinebilir.",
    ["Mevzuat ne kadar ayrıntılı olursa olsun bütün şartlar sözleşmede ayrıca ve eksiksiz olarak tekrar yazılır.",
     "Mevzuat ayrıntılıysa yazılı sözleşme düzenlenmez, sözlü mutabakat yeterlidir.",
     "Mevzuat şartları ayrıntılıysa yönetimin sorumluluklarını kabul etmesi aranmaz.",
     "Bu durumda denetçi sözleşme şartlarını tek taraflı olarak belirler."],
    "BDS 210 prg. 11'e göre mevzuatta sözleşme şartları yeterince ayrıntılı belirlenmişse denetçi, bu düzenlemelerin "
    "denetim için geçerli olduğunu ve yönetimin prg. 6-b'deki sorumluluklarını anladığını ve üstlendiğini belirtmekle "
    "yetinebilir; diğer şartların sözleşmede tekrarlanması gerekmez.")

P.q("BDS 210 prg. 8",
    f"{B210}, denetimin ön şartlarının mevcut olmaması hâlinde denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Mevzuatla zorunlu değilse durumu yönetimle görüşür, sözleşmeyi kabul etmez.",
    ["Sözleşmeyi kabul eder ve ön şartların eksikliğini raporunun diğer hususlar bölümünde açıklar.",
     "Ön şartları kendisi tamamlayarak sözleşmeyi kabul eder.",
     "Sözleşmeyi kabul eder, ön şartların yıl sonuna kadar sağlanmasını bekler.",
     "Durumu yönetimle görüşmeden sözleşmeyi sınırlı denetim olarak kabul eder."],
    "BDS 210 prg. 8'e göre ön şartlar mevcut değilse denetçi durumu yönetimle görüşür; mevzuatla zorunlu kılınmadıkça "
    "önerilen denetim sözleşmesini kabul etmez.")

P.q("BDS 230 prg. 10",
    "Denetçi, yönetimin bir karşılık tutarına ilişkin önemli bir konuyu yönetim ve üst yönetimden sorumlu olanlarla "
    f"görüşmüştür. {B230} bu görüşmeye ilişkin belgelendirmede yer alması gerekenler aşağıdakilerden hangisidir?",
    "Görüşülen önemli konunun niteliği, görüşmenin ne zaman ve kimlerle yapıldığı",
    ["Görüşmenin ses kaydının tamamı ve görüşmeye katılanların imzaladığı ayrıntılı tutanak",
     "Görüşmeye katılan yöneticilerin kişisel bilgileri ve ücretleri",
     "Sadece yönetimin görüşünü kabul ettiği konuların listesi",
     "Görüşmenin denetim ücreti üzerindeki etkisinin hesaplanması"],
    "BDS 230 prg. 10'a göre denetçi, yönetim, üst yönetimden sorumlu olanlar ve diğerleriyle görüşülen önemli konuları, "
    "görüşülen konuların niteliğini ve görüşmelerin ne zaman ve kimlerle yapıldığını belgelendirir.")

P.q("BDS 230 prg. 11",
    f"{B230}, denetçinin önemli bir konuda nihai sonucuyla tutarsız bilgi tespit etmesi hâlinde belgelendirmeye ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Tutarsızlığı nasıl ele aldığını belgelendirir.",
    ["Tutarsız bilgiyi içeren çalışma kâğıtlarını dosyadan çıkarır.",
     "Tutarsızlığı sadece sonuç değişirse belgelendirir.",
     "Tutarsızlığı yönetimin yazılı beyanıyla giderir ve belgelendirmez.",
     "Tutarsızlığın belgelendirilmesi kaliteyi gözden geçiren kişinin sorumluluğundadır."],
    "BDS 230 prg. 11'e göre denetçi, önemli bir konuya ilişkin nihai sonucuyla tutarsız bilgi tespit etmişse bu "
    "tutarsızlığı nasıl ele aldığını belgelendirir; A15'e göre bu, geçersiz hâle gelen çalışma kâğıtlarının saklanmasını "
    "gerektirmez.", zorluk="hard")

P.q("BDS 200 prg. A10",
    f"{B200}, üst yönetimden sorumlu olanlar ile yönetim arasındaki ilişkiye dair aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Üst yönetimden sorumlu olanlar ile yönetim, her işletmede farklı kişilerden oluşur.",
    ["Küçük işletmelerde işletme sahibi-yönetici, üst yönetimden sorumlu olanların rolünü de üstlenebilir.",
     "Bazı işletmelerde yönetim kurulunun icracı üyeleri üst yönetimden sorumlu olanlar arasında yer alabilir.",
     "Üst yönetimden sorumlu olanların sorumluluğu finansal raporlama sürecinin gözetimini de içerir.",
     "Tablolar, üst yönetimden sorumlu olanların gözetiminde yönetim tarafından hazırlanır."],
    "BDS 200 prg. 4 ve 13-l'ye göre tablolar üst yönetimin gözetiminde yönetimce hazırlanır ve üst yönetimin sorumluluğu "
    "finansal raporlama sürecinin gözetimini içerir. Bazı işletmelerde icracı yöneticiler veya sahip-yöneticiler üst "
    "yönetimden sorumlu olanlar arasında yer alabilir; ayrı kişilerden oluşma zorunluluğu yoktur.")

P.q("BDS 200 prg. 24",
    f"{B200}, bir BDS'deki ilgili amaca ulaşılamaması durumunda denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Bunun genel amaçlara ulaşmayı engelleyip engellemediğini değerlendirir.",
    ["Amaca ulaşılamayan BDS'yi uygulanmamış sayar ve denetimi olağan şekilde tamamlar.",
     "Durumu raporunun diğer hususlar paragrafında açıklar ve olumlu görüş verir.",
     "Amaca ulaşılamadığını yönetime bildirir; yönetim kabul ederse denetime devam eder.",
     "İlgili BDS'nin yerine benzer bir uluslararası standardı uygular."],
    "BDS 200 prg. 24'e göre ilgili bir BDS'deki amaca ulaşılamazsa denetçi, bunun genel amaçlara ulaşmasını engelleyip "
    "engellemediğini değerlendirir; engelliyorsa BDS'lere uygun olarak görüşünü değiştirir veya mevzuat izin veriyorsa "
    "denetimden çekilir. Bu durum BDS 230 uyarınca önemli bir konu olarak belgelendirilir.", zorluk="hard")

P.q("BDS 300 prg. 11",
    f"{B300}, denetim ekibi üyelerinin yönlendirilmesi, gözetimi ve çalışmalarının gözden geçirilmesine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Bunların niteliği, zamanlaması ve kapsamı planlanır ve çeşitli etkenlere göre değişir.",
    ["Yönlendirme ve gözetim sadece denetçi yardımcıları için planlanır.",
     "Gözden geçirmenin kapsamı her denetimde aynıdır ve standart tarafından belirlenmiştir.",
     "Gözetim ve gözden geçirme denetim raporu yayımlandıktan sonra yapılır.",
     "Yönlendirme ve gözetimin planlanması kaliteyi gözden geçiren kişinin görevidir."],
    "BDS 300 prg. 11'e göre denetçi, ekip üyelerinin yönlendirilmesi ve gözetimi ile çalışmalarının gözden geçirilmesinin "
    "niteliğini, zamanlamasını ve kapsamını planlar. A14-A15'e göre bunlar işletmenin büyüklüğü ve karmaşıklığı, "
    "değerlendirilen riskler ve ekip üyelerinin yetkinliği gibi etkenlere göre değişir.")

P.q("BDS 260 prg. 17",
    f"{B260}, borsada işlem gören işletmelerin denetiminde bağımsızlığa ilişkin iletişimde denetçinin bildirmesi "
    "gerekenler arasında aşağıdakilerden hangisi yer alır?",
    "Ekibin ve şirketin bağımsızlığa ilişkin etik hükümlere uyduğuna dair açıklama",
    ["Denetim şirketinin tüm müşterilerinden elde ettiği gelirlerin ayrıntılı listesi",
     "Denetim ekibi üyelerinin diğer müşterilerdeki finansal çıkarlarının dökümü",
     "Denetçinin, işletmenin rakiplerine verdiği hizmetlerin kapsamı",
     "Denetçinin bir sonraki yıl için önerdiği denetim ücreti"],
    "BDS 260 prg. 17'ye göre borsada işlem gören işletmelerde denetçi, ekip ve şirket dahil ilgili kişilerin bağımsızlığa "
    "ilişkin etik hükümlere uyduğuna dair açıklamayı ve bağımsızlığı etkileyebilecek ilişkiler ile alınan önlemleri üst "
    "yönetimden sorumlu olanlara bildirir.")

P.oncul("BDS 210 prg. 6, 7, 8",
    f"{B210} aşağıdaki durumlar değerlendirilmektedir:",
    ["Yönetim, tabloların hazırlanmasında kabul edilebilir bir çerçeve kullanmamaktadır.",
     "Yönetim, denetçinin stok sayımına katılmasına izin vermeyeceğini sözleşme öncesinde bildirmiştir ve bu sınırlama "
     "görüş bildirmekten kaçınmayı gerektirecektir.",
     "Yönetim, denetim ücretinin iki taksitte ödenmesini önermiştir.",
     "Yönetim, iç kontrole ilişkin sorumluluğunu anladığını yazılı olarak kabul etmiştir."],
    "Mevzuatla zorunlu olmadıkça yukarıdakilerden hangileri denetçinin sözleşmeyi kabul etmemesini gerektirir?",
    "I ve II",
    ["Yalnız I", "I ve II", "II ve III", "I, II ve III", "II, III ve IV"],
    "BDS 210 prg. 6-8'e göre kabul edilebilir çerçevenin bulunmaması ön şartların eksikliğidir (I); görüş bildirmekten "
    "kaçınmayı gerektirecek kapsam sınırlaması içeren sözleşme de kabul edilmez (II). Ücretin taksitle ödenmesi ön şart "
    "sorunu değildir (III); yönetimin sorumluluğunu kabul etmesi ön şartın sağlandığını gösterir (IV).")

# ================================================================ ek sorular
P.q("BDS 220 (Revize)",
    "Denetim ekibi ile kaliteyi gözden geçiren kişi arasında bir şerefiye değer düşüklüğü testine ilişkin görüş ayrılığı "
    f"ortaya çıkmış ve rapor tarihi yaklaşmıştır. {B220} sorumlu denetçinin bu durumdaki yükümlülüğü aşağıdakilerden "
    "hangisidir?",
    "Görüş ayrılığı çözülmeden denetçi raporuna tarih atmaz.",
    ["Kendi görüşü esas olduğundan ayrılığı dikkate almadan raporu tarihlendirir.",
     "Raporu tarihlendirir, görüş ayrılığını dikkat çekilen hususlarda açıklar.",
     "Görüş ayrılığını üst yönetimden sorumlu olanların oylamasına sunar.",
     "Kaliteyi gözden geçiren kişiyi değiştirerek raporu zamanında tarihlendirir."],
    "BDS 220 (Revize)'ye göre görüş ayrılıklarında ekip şirketin politika ve prosedürlerini izler; sorumlu denetçi "
    "ayrılıkların ele alınıp çözülmesinden ve sonuçların belgelendirilip uygulanmasından sorumludur ve görüş ayrılığı "
    "çözülmeden denetçi raporuna tarih atmaz.")

P.q("BDS 300 prg. 12",
    f"{B300}, aşağıdakilerden hangisi planlamaya ilişkin olarak çalışma kâğıtlarına dahil edilmesi gerekenler arasında "
    "yer almaz?",
    "Planlama toplantılarına katılan ekip üyelerinin imza listesi",
    ["Genel denetim stratejisi",
     "Denetim planı",
     "Denetim sırasında strateji veya planda yapılan önemli değişiklikler",
     "Strateji veya planda yapılan önemli değişikliklerin nedenleri"],
    "BDS 300 prg. 12'ye göre denetçi genel denetim stratejisini, denetim planını ve denetim sırasında bunlarda yapılan "
    "önemli değişiklikler ile bu değişikliklerin nedenlerini çalışma kâğıtlarına dahil eder.", zorluk="easy")

P.q("BDS 260 prg. 21",
    f"{B260}, denetçinin üst yönetimden sorumlu olanlarla iletişiminin zamanlamasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Denetçi iletişimi zamanında kurar; uygun zamanlama konunun önemine ve niteliğine göre değişir.",
    ["İletişim sadece denetim raporu imzalandıktan sonra kurulur.",
     "İletişim, denetimin tüm konularını kapsayacak şekilde yılda bir kez yapılır.",
     "Önemli bulgular denetim bitene kadar bekletilir ve raporla birlikte iletilir.",
     "İletişimin zamanlamasını üst yönetimden sorumlu olanlar tek başına belirler."],
    "BDS 260 prg. 21'e göre denetçi üst yönetimden sorumlu olanlarla zamanında iletişim kurar. A40-A41'e göre uygun "
    "zamanlama, konunun önemi ve niteliği ile üst yönetimin alması beklenen işlem gibi etkenlere göre değişir.")

P.q("BDS 200 A48",
    f"{B200}, finansal raporlamanın zamanında yapılması ve fayda-maliyet dengesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Bilginin ihtiyaca uygunluğu ve değeri zamanla azalma eğilimindedir; güvenilirlik ile maliyet arasında denge kurulur.",
    ["Maliyet dengesi, denetçiye alternatifi olmayan prosedürleri atlama hakkı verir.",
     "Zamanında raporlama gerekliliği, kanıtın ikna ediciliğinden daha önemlidir.",
     "Bilginin değeri zamanla artar; bu nedenle denetim süresi sınırlandırılmaz.",
     "Fayda-maliyet dengesi sadece KAYİK denetimlerinde dikkate alınır."],
    "BDS 200 A48'e göre bilginin ihtiyaca uygunluğu ve değeri zaman içinde azalma eğilimi gösterir ve güvenilirlik ile "
    "maliyet arasında bir denge vardır; ancak alternatifi bulunmayan bir prosedürün zorluğu, süresi veya maliyeti "
    "prosedürü ihmal etmek için geçerli sebep değildir.", zorluk="hard")

P.q("BDS 230 prg. 12",
    "Denetçi istisnai bir durumda, bir BDS'deki ilgili bir hükümden sapmanın gerekli olduğuna karar vermiş ve alternatif "
    f"prosedürler uygulamıştır. {B230} denetçi bu durumda neyi belgelendirir?",
    "Sapmanın sebeplerini ve alternatif prosedürlerin ilgili hükmün amacına nasıl ulaştığını",
    ["Sadece uygulanan alternatif prosedürlerin listesini",
     "Sapma için yönetimden alınan yazılı onayı ve onay tarihini",
     "Sapmanın denetim ücretine etkisini ve ek süre hesabını",
     "Sapmayı; denetim raporunda ayrıca açıklandığından belgelendirmez"],
    "BDS 230 prg. 12'ye göre istisnai durumlarda bir BDS hükmünden sapmanın gerekli olduğuna karar veren denetçi, "
    "sapmanın sebeplerini ve uygulanan alternatif prosedürlerin ilgili hükmün amacına nasıl ulaştığını belgelendirir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
