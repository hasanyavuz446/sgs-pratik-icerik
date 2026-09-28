# -*- coding: utf-8 -*-
"""SPK Mevzuatı · Piyasa Suçları ve Bozucu Eylemler — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · 6362 s. Sermaye Piyasası Kanunu m. 35/C-3, 99, 99/A, 100-116, 110/A, 115/A
    (7518 s. Kanunla 2024 kripto varlık değişiklikleri işlenmiş)
Tutar içeren hükümler (m. 103/1, 104) yıllık yeniden değerlendiği için tutar sorulmaz.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_piyasa_suclari_2026.json", lesson="sermaye_piyasasi_ve_finans", topic="piyasa_suclari",
          konu_adi="Piyasa Suçları ve Bozucu Eylemler", seed=2026092821,
          surum="6362 s. Sermaye Piyasası Kanunu (7518 s. Kanunla 2024 değişiklikleri dahil); 28.09.2026 kontrolü")

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"

# ================================================================ piyasa bozucu eylemler (m. 104)
P.q("6362 s. SPKn m. 104",
    f"{K}, piyasa bozucu eylemlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eylemin piyasa bozucu sayılması için aynı zamanda suç oluşturması aranır.",
    ["Makul bir ekonomik veya finansal gerekçeyle açıklanamaması eylemin niteliğini belirler.",
     "Piyasa bozucu eylemlerin kapsamı Kurulca belirlenir.",
     "Bu eylemlerde bulunanlara Kurul tarafından idari para cezası verilir.",
     "Eylemle menfaat temin edilmişse ceza bu menfaatin iki katından az olamaz."],
    "Kanun m. 104'e göre makul bir ekonomik veya finansal gerekçeyle açıklanamayan ve piyasaların güven, açıklık ve "
    "istikrar içinde çalışmasını bozan eylemler, bir suç oluşturmadığı takdirde piyasa bozucu eylem sayılır. Kurulca "
    "belirlenen bu eylemlere idari para cezası verilir; menfaat temin edilmişse ceza menfaatin iki katından az olamaz.")

P.sayisal("6362 s. SPKn m. 104",
    "Borsada işlem gören bir payda, makul bir ekonomik gerekçesi bulunmayan ve suç oluşturmayan emirlerle fiyat "
    "oynaklığı yaratan bir yatırımcının bu eylem sonucunda menfaat temin ettiği tespit edilmiştir. "
    f"{K}, bu yatırımcıya verilecek idari para cezası elde edilen menfaatin en az kaç katı olmalıdır?",
    "2", ["1", "3", "5", "10"],
    "Kanun m. 104'e göre piyasa bozucu eylemde bulunanlara idari para cezası verilir; bu suretle menfaat temin edilmişse "
    "cezanın miktarı menfaatin iki katından az olamaz. Üç kat alt sınırı m. 105'te düzenlenen tekrarlanan kabahatler "
    "içindir.", zorluk="easy")

P.q("6362 s. SPKn m. 104, 106, 107",
    "Bir yatırımcının, herhangi bir içsel bilgiye dayanmadığı ve fiyatı yanıltma amacı ispatlanamadığı hâlde, seans "
    "kapanışına yakın saatlerde makul bir ekonomik gerekçeyle açıklanamayan emirlerle kapanış fiyatını etkilediği tespit "
    f"edilmiştir. {K}, bu fiil aşağıdakilerden hangisi olarak değerlendirilir?",
    "Piyasa bozucu eylem",
    ["Bilgi suistimali suçu", "İşlem bazlı piyasa dolandırıcılığı suçu",
     "Güveni kötüye kullanma suçunun nitelikli hâli", "Usulsüz halka arz suçu"],
    "İçsel bilgiye dayanılmadığı için bilgi suistimali (m. 106), yanıltıcı izlenim uyandırma amacı ispatlanamadığı için "
    "işlem bazlı piyasa dolandırıcılığı (m. 107/1) oluşmaz. Makul gerekçeyle açıklanamayan ve suç oluşturmayan bu eylem "
    "m. 104 kapsamında piyasa bozucu eylemdir ve idari para cezası gerektirir.", zorluk="hard")

# ================================================================ bilgi suistimali (m. 106)
P.q("6362 s. SPKn m. 106",
    "Bir ihraççının henüz kamuya duyurulmamış birleşme görüşmelerine ilişkin bilgilere dayanılarak ihraççının paylarında "
    f"alım emirleri verilmiş ve menfaat sağlanmıştır. {K}, aşağıdakilerden hangisi bu fiil nedeniyle bilgi suistimali "
    "suçunun faili olabilecek kişiler arasında sayılmamıştır?",
    "Bilgiyi ihraççının KAP’ta yayımladığı açıklamadan öğrenen yatırımcı",
    ["İhraççının bağlı ortaklığında yönetici olarak görev yapan kişi",
     "Bilgiye ihraççıdaki pay sahipliği nedeniyle ulaşan kişi",
     "Bilgiye ihraççıya verdiği hukuki danışmanlık sırasında ulaşan avukat",
     "Bilgiyi ihraççının bilişim sistemine izinsiz girerek elde eden kişi"],
    "Kanun m. 106'ya göre suçun konusu henüz kamuya duyurulmamış bilgidir. İhraççı veya bağlı/hâkim ortaklık yöneticileri, "
    "pay sahipliği nedeniyle bilgiye sahip olanlar, iş, meslek ve görev nedeniyle bilgiye ulaşanlar ile bilgiyi suç "
    "işleyerek elde edenler fail olabilir. KAP'ta açıklanmış bilgi artık içsel bilgi değildir.")

P.sayisal("6362 s. SPKn m. 106",
    f"{K}, bilgi suistimali suçu için öngörülen hapis cezasının üst sınırı kaç yıldır?",
    "5", ["2", "3", "7", "10"],
    "Kanun m. 106'ya göre bilgi suistimali suçunu işleyenler üç yıldan beş yıla kadar hapis veya adli para cezası ile "
    "cezalandırılır; adli para cezası elde edilen menfaatin iki katından az olamaz.", zorluk="easy")

P.q("6362 s. SPKn m. 106",
    f"{K}, bilgi suistimali suçuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Adli para cezası elde edilen menfaatin yarısından az olamaz.",
    ["Suçun konusu, henüz kamuya duyurulmamış ve yatırım kararlarını etkileyebilecek bilgidir.",
     "Verilen emrin değiştirilmesi veya iptal edilmesi de suçun hareketleri arasındadır.",
     "Menfaatin failin kendisine veya bir başkasına temin edilmesi arasında fark yoktur.",
     "Suç için hapis veya adli para cezası seçimlik olarak öngörülmüştür."],
    "Kanun m. 106'ya göre bilgi suistimali, kamuya duyurulmamış bilgiye dayanarak emir verme, emri değiştirme veya iptal "
    "etme ve bu suretle kendisine veya başkasına menfaat temin etmedir. Ceza üç yıldan beş yıla kadar hapis veya adli "
    "para cezasıdır; adli para cezası menfaatin iki katından az olamaz.")

P.oncul("6362 s. SPKn m. 106",
    "İçsel bilgiye sahip bir kişinin aşağıdaki davranışları değerlendirilmektedir:",
    ["Bilgiye dayanarak verdiği satış emrini, bilgi açıklanmadan önce iptal ederek zarardan kaçınması",
     "Bilgiye dayanarak bir başkası hesabına alım emri vererek o kişiye kazanç sağlaması",
     "Kamuya açıklanmış finansal tabloları analiz ederek alım yapması ve kazanç sağlaması",
     "Bilgiyi kamuya açıklandıktan sonra kullanarak işlem yapması ve kazanç sağlaması"],
    f"{K}, yukarıdaki davranışlardan hangileri bilgi suistimali suçunu oluşturur?",
    "I ve II", ["Yalnız I", "I ve II", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 106 emir vermenin yanında verilen emri değiştirmeyi veya iptal etmeyi de suç hareketi sayar; zarardan "
    "kaçınmak da menfaattir. Menfaatin bir başkasına temin edilmesi de yeterlidir. Kamuya açıklanmış bilgiye dayalı "
    "analiz ve işlemler suçun konusunu oluşturmaz.", zorluk="hard")

P.q("6362 s. SPKn m. 106/1-d",
    "Bir yatırımcı, arkadaşından aldığı bilginin bir ihraççının henüz açıklanmamış satın alma kararı olduğunu bilerek "
    f"ihraççının paylarını almış ve kazanç sağlamıştır. {K}, bu yatırımcının durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bilginin niteliğini bildiği için bilgi suistimali suçunun faili olabilir.",
    ["İhraççıyla görev veya pay sahipliği bağı bulunmadığı için bilgi suistimali suçunun faili olamaz.",
     "Fiil piyasa bozucu eylem olarak idari para cezasını gerektirir.",
     "Bilgiyi suç işleyerek elde etmediği için fiil cezalandırılmaz.",
     "Fiil ancak bilgiyi veren arkadaşı açısından suç oluşturur."],
    "Kanun m. 106/1-d'ye göre sahip olduğu bilginin kamuya açıklanmamış ve fiyatı etkileyebilecek nitelikte olduğunu "
    "bilen veya ispat edilmesi hâlinde bilmesi gereken kişiler de fail olabilir; ihraççıyla bağ aranmaz.", zorluk="hard")

# ================================================================ piyasa dolandırıcılığı (m. 107-108)
P.q("6362 s. SPKn m. 107/1",
    "Bir yatırımcı, işlem hacmi düşük bir payda yoğun talep varmış izlenimi uyandırmak amacıyla kendisine ve yakınlarına ait "
    f"hesaplar arasında karşılıklı alım satım emirleri vermiş, ardından yükselen fiyattan satış yapmıştır. {K}, bu fiil "
    "aşağıdakilerden hangisinin kapsamına girer?",
    "İşlem bazlı piyasa dolandırıcılığı",
    ["Bilgi bazlı piyasa dolandırıcılığı", "Bilgi suistimali", "Güveni kötüye kullanmanın nitelikli hâli",
     "İzinsiz sermaye piyasası faaliyeti"],
    "Kanun m. 107/1'e göre sermaye piyasası araçlarının fiyatına, arz ve talebine ilişkin yanlış veya yanıltıcı izlenim "
    "uyandırmak amacıyla alım satım yapmak, emir vermek, iptal etmek veya hesap hareketi gerçekleştirmek işlem bazlı "
    "piyasa dolandırıcılığıdır.", zorluk="easy")

P.q("6362 s. SPKn m. 107/2",
    "Bir kişi, sahibi olduğu payların fiyatını yükseltmek amacıyla ihraççının büyük bir kamu ihalesini kazandığına dair "
    "gerçeğe aykırı bir haberi sosyal medya hesaplarından yaymış ve fiyat yükselince paylarını satarak kazanç elde etmiştir. "
    f"{K}, bu fiil için öngörülen yaptırım aşağıdakilerden hangisidir?",
    "Üç yıldan beş yıla kadar hapis ve beş bin güne kadar adli para cezası",
    ["Üç yıldan beş yıla kadar hapis veya adli para cezası",
     "İki yıldan beş yıla kadar hapis ve beş bin günden on bin güne kadar adli para cezası",
     "Bir yıldan üç yıla kadar hapis cezası",
     "Kurulca belirlenecek tutarda idari para cezası"],
    "Fiil, m. 107/2'de düzenlenen bilgi bazlı piyasa dolandırıcılığıdır: fiyatı etkilemek amacıyla yalan, yanlış veya "
    "yanıltıcı bilgi vermek, söylenti çıkarmak veya bunları yaymak ve bu suretle menfaat sağlamak üç yıldan beş yıla kadar "
    "hapis ve beş bin güne kadar adli para cezası gerektirir.")

P.q("6362 s. SPKn m. 107",
    f"{K}, piyasa dolandırıcılığı suçuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşlem bazlı piyasa dolandırıcılığında adli para cezası elde edilen menfaatin üç katından az olamaz.",
    ["İşlem bazlı piyasa dolandırıcılığı için hapis ve adli para cezası birlikte öngörülmüştür.",
     "Emir iptal etmek veya hesap hareketleri gerçekleştirmek de işlem bazlı suçun hareketleri arasındadır.",
     "Bilgi bazlı piyasa dolandırıcılığında söylenti çıkarmak veya yaymak suçun hareketleri arasındadır.",
     "Bilgi bazlı piyasa dolandırıcılığının oluşması için menfaat sağlanması gerekir."],
    "Kanun m. 107/1'e göre işlem bazlı piyasa dolandırıcılığında üç yıldan beş yıla kadar hapis ve beş bin günden on bin "
    "güne kadar adli para cezası verilir; adli para cezası suçla elde edilen menfaatten az olamaz. Bilgi bazlı suç "
    "(m. 107/2) menfaat sağlanmasını şart koşar.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 107/1",
    f"{K}, işlem bazlı piyasa dolandırıcılığı suçu için öngörülen adli para cezasının üst sınırı kaç gündür?",
    "10.000", ["2.000", "5.000", "7.500", "20.000"],
    "Kanun m. 107/1'e göre işlem bazlı piyasa dolandırıcılığı üç yıldan beş yıla kadar hapis ve beş bin günden on bin güne "
    "kadar adli para cezası gerektirir. Bilgi bazlı suçta (m. 107/2) adli para cezası beş bin güne kadardır.")

P.oncul("6362 s. SPKn m. 107/3",
    "İşlem bazlı piyasa dolandırıcılığı suçunu işleyen bir kişinin, elde ettiği menfaatin iki katı tutarındaki parayı "
    "Hazineye ödemesine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Ödeme soruşturma başlamadan önce yapılırsa hakkında cezaya hükmolunmaz.",
     "Ödeme soruşturma evresinde yapılırsa verilecek ceza üçte biri oranında indirilir.",
     "Ödeme kovuşturma evresinde hüküm verilinceye kadar yapılırsa verilecek ceza üçte biri oranında indirilir.",
     "Aynı pişmanlık hükümleri bilgi bazlı piyasa dolandırıcılığı için de uygulanır."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve III", ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 107/3'e göre birinci fıkradaki suçu işleyen kişi pişmanlık göstererek menfaatin iki katını Hazineye öderse: "
    "soruşturma başlamadan önce ödemede cezaya hükmolunmaz, soruşturma evresinde ceza yarı oranında, kovuşturma evresinde "
    "hükümden önce üçte bir oranında indirilir. Hüküm yalnız işlem bazlı suça uygulanır.", zorluk="hard")

P.q("6362 s. SPKn m. 108",
    f"{K}, aşağıdakilerden hangisi bilgi suistimali veya piyasa dolandırıcılığı sayılmayan hâller arasında yer almaz?",
    "Bir ihraççı yöneticisinin açıklanmamış olumsuz finansal sonuçları öğrenince paylarını satması",
    ["Türkiye Cumhuriyet Merkez Bankasının döviz kuru politikası amacıyla işlem yapması",
     "Kurul düzenlemelerine göre uygulanan bir pay geri alım programı kapsamında alım yapılması",
     "Çalışanlara pay edindirme programı çerçevesinde pay tahsis edilmesi",
     "Kurul düzenlemelerine uygun fiyat istikrarını sağlayıcı işlemler kapsamında alım yapılması"],
    "Kanun m. 108; TCMB veya yetkili resmî kurumların para, döviz kuru, kamu borç yönetimi ve finansal istikrar amaçlı "
    "işlemlerini, Kurul düzenlemelerine uygun geri alım ve çalışanlara pay edindirme programlarını ve fiyat istikrarını "
    "sağlayıcı işlemleri suç saymaz. Açıklanmamış bilgiye dayanan satış m. 106 kapsamındadır.")

# ================================================================ usulsüz halka arz, izinsiz faaliyet (m. 99, 99/A, 109, 109/A)
P.q("6362 s. SPKn m. 109",
    "Kuruldan izin almaksızın aracılık faaliyeti yürüten bir kişinin, bu faaliyet kapsamında onaylı izahname olmaksızın bir "
    f"şirketin paylarını da halka arz ettiği anlaşılmıştır. {K}, bu kişinin cezalandırılmasına ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "İzinsiz faaliyet suçundan cezaya hükmedilir ve bu ceza yarı oranında artırılır.",
    ["Her iki suçtan ayrı ayrı cezaya hükmedilir ve cezalar toplanır.",
     "Usulsüz halka arz suçundan cezaya hükmedilir, izinsiz faaliyet ayrıca cezalandırılmaz.",
     "İzinsiz faaliyet suçundan cezaya hükmedilir ve bu ceza üçte bir oranında artırılır.",
     "Fiil tek suç sayılır ve Kurulca idari para cezası uygulanmasıyla yetinilir."],
    "Kanun m. 109/2'ye göre izinsiz faaliyette bulunan kişi bu suçun icrası kapsamında usulsüz halka arz suçunu da işlerse "
    "sadece izinsiz faaliyet suçundan cezaya hükmedilir ve ceza yarı oranında artırılır. Her iki suç için öngörülen ceza "
    "iki yıldan beş yıla kadar hapis ve adli para cezasıdır.", zorluk="hard")

P.q("6362 s. SPKn m. 99",
    "Kuruldan izin almaksızın portföy yöneticiliği faaliyeti yürüten bir şirket tespit edilmiştir. "
    f"{K}, bu şirkete ve sorumlulara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sorumlu yöneticiler hakkında tedbir alınabilmesi için faaliyetten doğan zararın kesinleşmesi gerekir.",
    ["Kurul, faaliyetin durdurulması için gerekli her türlü tedbiri alabilir.",
     "Kurul, faaliyetin sonuçlarının iptali için dava açabilir.",
     "İzinsiz faaliyette bulunanlar iki yıldan beş yıla kadar hapis cezası ile cezalandırılır.",
     "Faaliyetin internet üzerinden yürütülmesi hâlinde erişimin engellenmesine karar verilebilir."],
    "Kanun m. 99'a göre Kurul izinsiz faaliyetin durdurulması için her türlü tedbiri alır ve sonuçların iptali için dava "
    "açabilir; sorumlu ortak ve yöneticiler hakkında m. 96/2, zararın kesinleşmesi şartı aranmaksızın kıyasen uygulanır. "
    "İnternet yayınlarında içerik çıkarma veya erişim engeli kararı verilebilir; m. 109/2 hapis cezası öngörür.")

P.sayisal("6362 s. SPKn m. 99/1",
    "Kurul, izinsiz sermaye piyasası faaliyetinin doğurduğu sonuçların iptali ve nakdin hak sahiplerine iadesi için dava "
    f"açmayı değerlendirmektedir. {K}, bu dava faaliyetin tespit tarihinden itibaren en geç kaç yıl içinde açılabilir?",
    "1", ["2", "3", "5", "10"],
    "Kanun m. 99/1'e göre Kurul, izinsiz faaliyetin sonuçlarının iptali ve varlıkların hak sahiplerine iadesi için tespit "
    "tarihinden itibaren bir yıl ve her hâlde vukuu tarihinden itibaren beş yıl içinde dava açabilir.")

P.q("6362 s. SPKn m. 99/4",
    "Kuruldan izin alınmaksızın bir internet sitesi üzerinden Türkiye’de yerleşik kişilere kaldıraçlı işlem yaptırıldığı "
    f"tespit edilmiştir. {K}, bu siteye ilişkin içeriğin çıkarılması veya erişimin engellenmesi kararına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Karar Kurul tarafından verilir ve uygulanmak üzere Erişim Sağlayıcıları Birliğine gönderilir.",
    ["Karar, Kurulun başvurusu üzerine sulh ceza hâkimliği tarafından verilir.",
     "Karar, Kurulun başvurusu üzerine Bilgi Teknolojileri ve İletişim Kurumu Başkanlığı tarafından verilir.",
     "Karar Kurul tarafından verilir ve uygulanmak üzere Cumhuriyet başsavcılığına gönderilir.",
     "Karar, Yatırımcı Tazmin Merkezinin talebi üzerine Kurul Başkanı tarafından verilir."],
    "Kanun m. 99/4'e (7518 s. Kanunla 2024 değişikliği) göre içeriğin çıkarılmasına ve/veya erişimin engellenmesine Kurul "
    "tarafından karar verilir ve karar uygulanmak üzere Erişim Sağlayıcıları Birliğine gönderilir. Değişiklikten önce "
    "Kurulun başvurusu üzerine erişimi Bilgi Teknolojileri ve İletişim Kurumu engelliyordu.")

P.q("6362 s. SPKn m. 99/A",
    "Yurt dışında yerleşik bir kripto varlık platformunun Kuruldan izin almaksızın faaliyet gösterdiği ileri sürülmektedir. "
    f"{K}, aşağıdakilerden hangisi bu platformun faaliyetlerinin Türkiye’de yerleşik kişilere yönelik olduğunun kabulünü "
    "gerektiren durumlardan biri değildir?",
    "Platformun yabancı dildeki internet sitesine Türkiye’den erişilebilmesi",
    ["Platform tarafından Türkiye’de iş yeri açılması",
     "Platform tarafından Türkçe internet sitesi oluşturulması",
     "Hizmetlerinin Türkiye’de yerleşik bir kişi aracılığıyla tanıtılması",
     "Hizmetlerinin doğrudan Türkiye’deki yatırımcılara pazarlanması"],
    "Kanun m. 99/A'ya göre yurt dışında yerleşik platformun Türkiye'de iş yeri açması, Türkçe internet sitesi oluşturması "
    "veya doğrudan ya da Türkiye'de yerleşik kişi ve kurumlar aracılığıyla tanıtım ve pazarlama yapması hâllerinden "
    "birinin varlığında faaliyet Türkiye'de yerleşik kişilere yönelik kabul edilir; bu durum izinsiz hizmet sağlayıcılık sayılır.")

P.sayisal("6362 s. SPKn m. 109/A",
    f"{K}, izin almaksızın kripto varlık hizmet sağlayıcı olarak faaliyet yürüten bir tüzel kişinin yetkilileri için "
    "öngörülen hapis cezasının alt sınırı kaç yıldır?",
    "3", ["1", "2", "5", "8"],
    "Kanun m. 109/A'ya göre izin almaksızın kripto varlık hizmet sağlayıcı olarak faaliyet yürüten gerçek kişiler ve tüzel "
    "kişilerin yetkilileri üç yıldan beş yıla kadar hapis ve beş bin günden on bin güne kadar adli para cezası ile cezalandırılır.")

P.q("6362 s. SPKn m. 99/A-3",
    "Kurulca belirlenen esaslara aykırı olarak internet üzerinden kripto varlık reklamı yapıldığı bilgisi edinilmiştir. "
    f"{K}, Kurulun bu reklamlara ilişkin yetkisi aşağıdakilerden hangisidir?",
    "İçeriğin çıkarılmasına veya erişimin engellenmesine karar vermek",
    ["Reklam veren hakkında Cumhuriyet başsavcılığına doğrudan dava açmak",
     "Reklamı yapan platformun tedrici tasfiyesine karar vermek",
     "Reklam içeriğini sulh ceza hâkimliğinin onayına sunmak",
     "Reklamın yayımlandığı sitenin alan adını askıya almak"],
    "Kanun m. 99/A-3'e göre Kurulca belirlenen esaslara aykırı internet ilan ve reklamları, kripto varlıklara yönelik "
    "esaslara aykırı danışmanlık veya portföy yöneticiliği ve izinsiz hizmet sağlayıcılık hâllerinde Kurul içeriğin "
    "çıkarılmasına ve/veya erişimin engellenmesine karar verir; karar Erişim Sağlayıcıları Birliğine gönderilir.")

P.q("6362 s. SPKn m. 100",
    "Faaliyet izni iptal edildiği hâlde ticaret unvanında ve ilanlarında sermaye piyasasında faaliyette bulunduğu izlenimini "
    f"uyandıran ibareler kullanmaya devam eden bir şirket tespit edilmiştir. {K}, gecikmesinde sakınca bulunan hâllerde bu "
    "şirketin iş yerinin geçici olarak kapatılmasına kim karar verir?",
    "Kurulun talebi üzerine ilgili yerin en büyük mülki amiri",
    ["Kurulun başvurusu üzerine sulh ceza hâkimi", "Kurul Karar Organı",
     "Ticaret sicili müdürlüğünün talebi üzerine belediye başkanı",
     "Türkiye Sermaye Piyasaları Birliği yönetim kurulu"],
    "Kanun m. 100/1'e göre izinsiz veya yetkisi iptal edilmiş olduğu hâlde faaliyette bulunduğu izlenimini uyandıran "
    "sorumlular hakkında cezai kovuşturma yapılmakla birlikte, gecikmesinde sakınca bulunan hâllerde ilan ve reklamlar "
    "durdurulabilir ve Kurulun talebi üzerine ilgili yer en büyük mülki amirince iş yerleri geçici olarak kapatılabilir.")

# ================================================================ güveni kötüye kullanma, zimmet (m. 110, 110/A)
P.sayisal("6362 s. SPKn m. 110/1-a",
    "Bir aracı kurumun çalışanı, müşterilerin kayden tevdi ettiği payları kendi kişisel borcu için teminat olarak "
    f"rehnetmiştir. {K}, bu fiil nedeniyle güveni kötüye kullanma suçundan hükmolunacak hapis cezası kaç yıldan az olamaz?",
    "3", ["1", "2", "5", "8"],
    "Kanun m. 110/1-a'ya göre yatırım kuruluşuna tevdi edilen sermaye piyasası araçlarını kendisinin veya başkasının "
    "menfaatine satmak, kullanmak, rehnetmek, gizlemek veya inkâr etmek güveni kötüye kullanmanın nitelikli hâlidir; TCK "
    "m. 155/2'ye göre hükmolunacak ceza üç yıldan az olamaz.")

P.q("6362 s. SPKn m. 110",
    f"{K}, güveni kötüye kullanma ve sahtecilik suçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırım kuruluşu kayıtlarını erişilmez kılan kişiye ancak idari para cezası verilir.",
    ["Yatırım kuruluşuna tevdi edilen nakdi kendi menfaatine kullanmak nitelikli hâl oluşturur.",
     "Halka açık ortaklığın kârını örtülü işlemlerle azaltmak nitelikli hâl oluşturur.",
     "Nitelikli hâlde hükmolunacak hapis cezası üç yıldan az olamaz.",
     "Kayıtları bozan kişilere belgede sahteciliğe bağlanan kanuni sonuçlar da uygulanır."],
    "Kanun m. 110/1 tevdi edilen varlıkların kötüye kullanılmasını ve örtülü işlemlerle kârın azaltılmasını güveni kötüye "
    "kullanmanın nitelikli hâli sayar; ceza üç yıldan az olamaz. m. 110/2'ye göre kayıtları bozan, yok eden, değiştiren "
    "veya erişilmez kılanlar iki yıldan beş yıla kadar hapis ve adli para cezası alır; sahteciliğin kanuni sonuçları da uygulanır.")

P.oncul("6362 s. SPKn m. 106, 110",
    "Sermaye piyasasında aşağıdaki fiiller işlenmiştir:",
    ["Aracı kurum çalışanının müşteriye ait payları gizleyerek kendi hesabına satması",
     "Halka açık ortaklığın, yöneticisinin şirketine emsallerine göre bariz şekilde yüksek kira ödemesi",
     "Yatırım kuruluşu kayıtlarının bir çalışan tarafından erişilmez kılınması",
     "Henüz açıklanmamış bilgiye dayanarak pay alım emri verilmesi ve menfaat temin edilmesi"],
    f"{K}, yukarıdaki fiillerden hangileri güveni kötüye kullanma suçunun nitelikli hâlini oluşturur?",
    "I ve II", ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, II ve III"],
    "Kanun m. 110/1-a tevdi edilen araçların satılmasını veya gizlenmesini, m. 110/1-b ilişkili kişilerle emsallerine göre "
    "bariz farklı bedelli örtülü işlemlerle kârın azaltılmasını nitelikli hâl sayar. Kayıtların erişilmez kılınması m. 110/2'de "
    "ayrı suçtur; açıklanmamış bilgiye dayalı işlem bilgi suistimalidir.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 110/3",
    "Halka açık bir ortaklıktan ilişkili tarafına örtülü kazanç aktarımı yoluyla güveni kötüye kullanma suçunu işleyen kişi, "
    "soruşturma başlamadan önce etkin pişmanlık göstermek istemektedir. "
    f"{K}, bu kişinin m. 21/4 kapsamındaki iadenin yanı sıra bu tutarın kaç katını Hazineye ödemesi hâlinde hakkında cezaya "
    "hükmolunmaz?",
    "2", ["1", "3", "4", "5"],
    "Kanun m. 110/3'e göre m. 110/1-b ve c kapsamındaki suçu işleyen kişi, m. 21/4'teki iadenin yanı sıra bunun iki katı "
    "parayı soruşturma başlamadan önce Hazineye öderse cezaya hükmolunmaz; soruşturma evresinde ceza yarı, kovuşturma "
    "evresinde üçte bir oranında indirilir.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 110/A-1",
    f"{K}, kripto varlık hizmet sağlayıcı yönetim kurulu üyesinin koruma ve saklamakla yükümlü olduğu kripto varlıkları "
    "zimmetine geçirmesi hâlinde öngörülen hapis cezasının alt sınırı kaç yıldır?",
    "8", ["3", "5", "12", "14"],
    "Kanun m. 110/A-1'e göre kripto varlık hizmet sağlayıcıda zimmet sekiz yıldan on dört yıla kadar hapis ve beş bin güne "
    "kadar adli para cezası gerektirir; fail ayrıca hizmet sağlayıcının zararını tazmine mahkûm edilir.")

P.sayisal("6362 s. SPKn m. 110/A-2",
    f"{K}, kripto varlık hizmet sağlayıcıda zimmet suçunun zimmetin açığa çıkmamasını sağlamaya yönelik hileli "
    "davranışlarla işlenmesi hâlinde öngörülen hapis cezasının alt sınırı kaç yıldır?",
    "14", ["8", "10", "12", "20"],
    "Kanun m. 110/A-2'ye göre hileli davranışlarla işlenen zimmette on dört yıldan yirmi yıla kadar hapis ve yirmi bin güne "
    "kadar adli para cezası verilir; adli para cezası hizmet sağlayıcının ve müşterilerinin zararının üç katından az olamaz.",
    zorluk="hard")

P.q("6362 s. SPKn m. 110/A-3",
    "Faaliyet izni kaldırılan bir kripto varlık platformunun fiilen yönetimini elinde bulunduran gerçek kişi ortağının, "
    "müşteri kaynaklarını platformun emin çalışmasını tehlikeye düşürecek biçimde kendi şirketlerine kullandırdığı tespit "
    f"edilmiştir. {K}, bu duruma ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fiil, güveni kötüye kullanmanın nitelikli hâli olarak cezalandırılır.",
    ["Fiil zimmet olarak kabul edilir.",
     "Fail hakkında on iki yıldan yirmi iki yıla kadar hapis cezasına hükmolunur.",
     "Adli para cezası, platformun ve müşterilerin zararının üç katından az olamaz.",
     "Meydana gelen zararın müteselsilen ödettirilmesine karar verilir."],
    "Kanun m. 110/A-3'e göre faaliyet izni kaldırılan kripto varlık hizmet sağlayıcının yönetim veya kontrolünü elinde "
    "bulunduran gerçek kişi ortaklarının kaynakları bu şekilde kullandırması zimmet sayılır; on iki yıldan yirmi iki yıla "
    "kadar hapis ve yirmi bin güne kadar adli para cezası verilir, zarar müteselsilen ödettirilir.", zorluk="hard")

P.oncul("6362 s. SPKn m. 110/A-4, 5, 6",
    "Kripto varlık hizmet sağlayıcıda zimmet suçunda zimmete geçirilen varlıkların iadesine ve değerine ilişkin aşağıdaki "
    "eşleştirmeler verilmiştir:",
    ["Soruşturma başlamadan önce aynen iade – cezanın üçte ikisi indirilir",
     "Kovuşturma başlamadan önce gönüllü iade – cezanın yarısı indirilir",
     "Kovuşturma başladıktan sonra, hükümden önce iade – cezanın dörtte biri indirilir",
     "Suç konusu değerin azlığı – ceza üçte birden yarıya kadar indirilir"],
    f"{K}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 110/A'ya göre soruşturma başlamadan önce aynen iade veya zararın tamamen tazmininde cezanın üçte ikisi, "
    "kovuşturma başlamadan önce gönüllü iadede yarısı, hükümden önce iadede üçte biri indirilir. Değerin azlığı nedeniyle "
    "ceza üçte birden yarıya kadar indirilir.", zorluk="hard")

# ================================================================ diğer suçlar (m. 111-114)
P.q("6362 s. SPKn m. 103/7, 111",
    "Kurul denetim elemanlarının bir aracı kurumdan istediği elektronik kayıtlar verilmemiş, denetim elemanlarının iş yerine "
    f"girişi de engellenmiştir. {K}, bu fiillere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetimi engelleyen kişiye bir yıldan üç yıla kadar hapis cezası verilir.",
    ["Kayıtları vermeyen kişiye bir yıldan üç yıla kadar hapis cezası verilir.",
     "Kayıtların elektronik ortamda tutulması bu suçun oluşmasını engellemez.",
     "Engelleme sırasında cebir kullanılmışsa ayrıca TCK hükümlerine göre ceza verilir.",
     "Belgeleri istenen şekilde vermeyenlere idari para cezası da verilebilir."],
    "Kanun m. 111/1'e göre istenen bilgi, belge ve elektronik kayıtları vermeyen kişi bir yıldan üç yıla kadar, m. 111/2'ye "
    "göre denetimi engelleyen kişi altı aydan iki yıla kadar hapis cezası alır; cebir veya tehdit hâlinde TCK'ya göre ayrıca "
    "ceza verilir. m. 103/7 bu kişilere idari para cezası da öngörür.")

P.q("6362 s. SPKn m. 112",
    f"{K}, yasal defterlerde, muhasebe kayıtlarında ve finansal tablolarda usulsüzlüğe ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Özel belgede sahtecilik nedeniyle ceza verilebilmesi için sahte belgenin kullanılması gerekir.",
    ["Defter ve kayıtları kasıtlı olarak usulüne uygun tutmayanlar hapis ve adli para cezası ile cezalandırılır.",
     "Saklanması gereken belgeleri kanuni süresince kasıtlı olarak saklamayanlar da cezalandırılır.",
     "Gerçeğe aykırı hesap açanlar Türk Ceza Kanunu’nun ilgili hükümlerine göre cezalandırılır.",
     "Yanıltıcı bağımsız denetim raporunun düzenlenmesini sağlayan sorumlu yönetim kurulu üyeleri de cezalandırılır."],
    "Kanun m. 112/1'e göre defterleri usulüne uygun tutmayanlar ve belgeleri saklamayanlar altı aydan iki yıla kadar hapis "
    "ve adli para cezası alır; m. 112/2'deki fiiller TCK'ya göre cezalandırılır ve özel belgede sahtecilik için sahte "
    "belgenin kullanılmış olması şartı aranmaz.")

P.oncul("6362 s. SPKn m. 112",
    "Kasıtlı olarak işlenen aşağıdaki fiiller verilmiştir:",
    ["Kanunen tutulması gereken defterlerin usulüne uygun tutulmaması",
     "Finansal tabloların gerçeği yansıtmayan şekilde düzenlenmesi",
     "Saklanması gereken belgelerin kanuni süresince saklanmaması",
     "Gerçeğe aykırı hesap açılması"],
    f"{K}, yukarıdaki fiillerden hangileri için Kanunda altı aydan iki yıla kadar hapis ve beş bin güne kadar adli para "
    "cezası öngörülmüştür?",
    "I ve III", ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 112/1 defter ve kayıtları usulüne uygun tutmamayı ve belgeleri kanuni süresince saklamamayı altı aydan iki "
    "yıla kadar hapis ve beş bin güne kadar adli para cezasıyla cezalandırır. Finansal tabloları gerçeği yansıtmayan şekilde "
    "düzenlemek ve gerçeğe aykırı hesap açmak m. 112/2 uyarınca TCK hükümlerine göre cezalandırılır.")

P.q("6362 s. SPKn m. 112/3",
    f"{K}, Türk Ceza Kanunu’ndaki bilişim sistemini engelleme, bozma, verileri yok etme veya değiştirme suçu bakımından "
    "aşağıdakilerden hangisi banka veya kredi kurumu sayılır?",
    "Yatırım kuruluşları",
    ["Halka açık ortaklıklar", "Bağımsız denetim kuruluşları", "Kitle fonlama platformları", "Derecelendirme kuruluşları"],
    "Kanun m. 112/3'e göre yatırım kuruluşları ile Kanunun Üçüncü Kısım Dördüncü Bölümünde yer alan kolektif yatırım "
    "kuruluşları TCK m. 244'teki suç açısından banka veya kredi kurumu sayılır; bu durum cezanın ağırlaştırılmasını sağlar.",
    zorluk="easy")

P.sayisal("6362 s. SPKn m. 113",
    "Kurulun yürüttüğü bir inceleme kapsamında istenen belgelerin içeriğini basına açıklayan bir kişi için "
    f"{K} öngörülen hapis cezasının üst sınırı kaç yıldır?",
    "3", ["1", "2", "5", "7"],
    "Kanun m. 113'e göre Kurulca yürütülen inceleme veya denetim kapsamında istenen bilgi veya belgelere ilişkin başkalarına "
    "açıklamada bulunanlar bir yıldan üç yıla kadar hapis ve beş bin güne kadar adli para cezası ile cezalandırılır.")

P.q("6362 s. SPKn m. 90, 113",
    f"{K}, Kurulun inceleme ve denetim faaliyetlerinde gizliliğe ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İncelemeye konu kişiler, incelemenin varlığını kamuya açıklayabilir.",
    ["Kendilerinden bilgi istenen kişiler özel kanunlardaki sır saklama hükümlerini ileri süremez.",
     "Bilgi istenen kamu kurumları da incelemenin varlığını sır olarak saklar.",
     "İnceleme kapsamında istenen belgeleri başkalarına açıklayanlar hapis cezası ile cezalandırılır.",
     "İstenen belgeleri başkalarına açıklayanlara adli para cezası da verilir."],
    "Kanun m. 90'a göre bilgi istenenler gizlilik hükümlerini ileri sürerek bilgi vermekten kaçınamaz; incelemeye konu "
    "kişiler ile bilgi istenen kamu kurumları dahil herkes incelemenin varlığını ve niteliğini sır olarak saklamak zorundadır. "
    "m. 113 açıklamada bulunanlara hapis ve adli para cezası öngörür.")

P.q("6362 s. SPKn m. 114",
    "Bir anonim şirket yararına bilgi suistimali suçu işlendiği mahkemece tespit edilmiştir. "
    f"{K}, bu durumda şirket hakkında aşağıdakilerden hangisine hükmolunur?",
    "Tüzel kişilere özgü güvenlik tedbirlerine",
    ["Şirketin tasfiyesine ilişkin Kurul kararına",
     "Şirket yöneticileri için hapis cezası yerine adli para cezasına",
     "Şirketin tüm faaliyet izinlerinin iptaline",
     "Şirketin paylarının borsa kotundan çıkarılmasına"],
    "Kanun m. 114'e göre m. 106 ve 107'deki suçların bir tüzel kişinin yararına işlenmesi hâlinde ilgili tüzel kişi hakkında "
    "tüzel kişilere özgü güvenlik tedbirlerine hükmolunur. Tüzel kişilere ceza sorumluluğu yüklenmez.", zorluk="easy")

# ================================================================ soruşturma, görevli mahkeme (m. 115, 115/A, 116)
P.q("6362 s. SPKn m. 115",
    f"{K}, sermaye piyasası suçlarında soruşturma ve kovuşturma usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Cumhuriyet savcısı, Kurulun başvurusunu beklemeksizin resen soruşturma başlatabilir.",
    ["Soruşturma yapılması, Kurulun Cumhuriyet başsavcılığına yazılı başvurusuna bağlıdır.",
     "Kurulun yazılı başvurusu bir muhakeme şartıdır.",
     "Kamu davası açılırsa Kurul iddianamenin kabulüyle katılan sıfatını kazanır.",
     "Kovuşturmaya yer olmadığı kararına karşı Kurul itiraz edebilir."],
    "Kanun m. 115'e göre Kanunda tanımlanan veya atıfta bulunulan suçlardan soruşturma yapılması Kurulun Cumhuriyet "
    "başsavcılığına yazılı başvurusuna bağlıdır ve başvuru muhakeme şartıdır. İddianamenin kabulüyle Kurul katılan sıfatını "
    "kazanır; kovuşturmaya yer olmadığı kararına itiraz edebilir.")

P.q("6362 s. SPKn m. 115/3",
    f"Bir piyasa dolandırıcılığı soruşturmasında şüphelilerin ifadesi alınacaktır. {K}, bu soruşturmaya Kurulun katkısına "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "İfade alınırken Kurul meslek personelinin hazır bulunması sağlanabilir.",
    ["İfadeler Kurul meslek personeli tarafından alınır ve savcılığa gönderilir.",
     "Kurul personeli soruşturmada ancak bilirkişi olarak dinlenebilir.",
     "Kurul personelinin soruşturmada görev alması Adalet Bakanlığı iznine bağlıdır.",
     "Kurul, soruşturma dosyasını inceleyerek kovuşturma kararı verir."],
    "Kanun m. 115/3'e göre Kanunda tanımlanan suçlardan yapılan soruşturmada Cumhuriyet savcısı Kurul meslek personelinden "
    "yararlanabilir; şüpheli veya tanık ifadesi alınırken Kurul meslek personelinin hazır bulunması sağlanabilir. Kovuşturma "
    "kararı savcılığa aittir.")

P.q("6362 s. SPKn m. 116",
    f"Bir yatırımcı hakkında piyasa dolandırıcılığı suçundan kamu davası açılacaktır. {K}, bu davaya bakmakla görevli "
    "mahkeme aşağıdakilerden hangisidir?",
    "İhtisas mahkemesi olarak görevlendirilen asliye ceza mahkemesi",
    ["İhtisas mahkemesi olarak görevlendirilen ağır ceza mahkemesi",
     "Ortaklık merkezinin bulunduğu yerdeki asliye ticaret mahkemesi",
     "Kurul merkezinin bulunduğu yer idare mahkemesi",
     "Fiilin işlendiği yer asliye hukuk mahkemesi"],
    "Kanun m. 116'ya göre Kanunda tanımlanan veya atıfta bulunulan suçlardan dolayı yargılama yapmaya Hâkimler ve Savcılar "
    "Kurulunun ihtisas mahkemesi olarak görevlendireceği asliye ceza mahkemeleri yetkilidir. Kripto varlık zimmet davaları "
    "ise m. 115/A uyarınca ağır ceza mahkemelerinde görülür.", zorluk="easy")

P.q("6362 s. SPKn m. 115, 115/A",
    "Bir kripto varlık platformunun yöneticileri hakkında müşteri varlıklarını zimmetlerine geçirdikleri iddiasıyla dava "
    f"açılacaktır. {K}, bu davalara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Davalar ihtisas mahkemesi olarak görevlendirilen asliye ceza mahkemesinde görülür.",
    ["Davalar fiilin işlendiği yerin bağlı olduğu ilin adıyla anılan (1) numaralı ağır ceza mahkemesinde görülür.",
     "Gerekli yerlerde bu suçlara bakmak üzere diğer ağır ceza mahkemeleri de görevlendirilebilir.",
     "Mahkûmun Hazineye olan borç ve tazminatları ödenmedikçe koşullu salıverilme uygulanmaz.",
     "İddianamenin kabulü hâlinde bir örneği Kurula tebliğ edilir ve Kurul katılan sıfatını kazanır."],
    "Kanun m. 115/A-3'e göre Kanunda tanımlanan zimmet suçuna ait davalar fiilin işlendiği yerin bağlı olduğu ilin adıyla "
    "anılan (1) numaralı ağır ceza mahkemelerinde görülür; gerekli yerlerde diğer ağır ceza mahkemeleri de görevlendirilebilir. "
    "m. 115/A-5 koşullu salıverilmeyi borç ödenmesine bağlar; iddianame Kurula tebliğ edilir.", zorluk="hard")

P.oncul("6362 s. SPKn m. 105/4, 115/A, 116",
    "Sermaye piyasasına ilişkin uyuşmazlıklar ile görevli yargı yerleri aşağıda eşleştirilmiştir:",
    ["Bilgi suistimali – Asliye ceza mahkemesi",
     "İzinsiz kripto varlık hizmet sağlayıcılığı – Asliye ceza mahkemesi",
     "Kripto varlık hizmet sağlayıcıda zimmet – Ağır ceza mahkemesi",
     "Kurulun idari para cezası kararına itiraz – Asliye ticaret mahkemesi"],
    f"{K}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, II ve III", ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 116'ya göre Kanunda tanımlanan suçlar (bilgi suistimali ve m. 109/A'daki izinsiz kripto hizmet sağlayıcılığı "
    "dahil) ihtisas asliye ceza mahkemelerinde, m. 115/A'ya göre kripto zimmet davaları ağır ceza mahkemelerinde görülür. "
    "m. 105/4'e göre idari para cezası kararlarına karşı idari yargı yoluna başvurulur.")

# ================================================================ tedbirler ve bildirim (m. 101-102, 35/C)
P.q("6362 s. SPKn m. 101/1",
    "Bir payda piyasa dolandırıcılığı yapıldığına dair makul şüphe bulunan kişiler hakkında Kurul tedbir almayı "
    f"değerlendirmektedir. {K}, aşağıdakilerden hangisi Kurulun bu kişiler ve ilgili sermaye piyasası araçları hakkında "
    "alabileceği tedbirler arasında sayılmamıştır?",
    "Kişilerin malvarlıklarına Kurul kararıyla el konulması",
    ["Borsalarda geçici veya sürekli işlem yasağı getirilmesi", "Takas yöntemlerinin değiştirilmesi",
     "Piyasa verilerinin dağıtım kapsamının sınırlanması", "İşlem veya pozisyon limiti getirilmesi"],
    "Kanun m. 101/1'e göre m. 104, 106 ve 107'deki fiilleri işlediğine dair makul şüphe bulunanlar hakkında Kurul işlem "
    "yasağı, takas yöntemlerinin değiştirilmesi, kredili işlem ve açığa satış sınırlaması, teminat yükümlülüğü, farklı pazar, "
    "piyasa verisi sınırlaması ve işlem/pozisyon limiti gibi tedbirler alır. El koyma yargısal bir tedbirdir.")

P.oncul("6362 s. SPKn m. 101",
    "Bilgi suistimali incelemesi sürerken Kurulun alabileceği önlemlere ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Tedbir alınabilmesi için fiilin işlendiğine dair makul şüphe yeterlidir.",
     "Kredili alım ve açığa satış işlemlerine sınırlama getirilebilir.",
     "İnceleme kapsamında internet yayınlarında içeriğin çıkarılmasına karar verilebilir.",
     "Tedbir kararı alınabilmesi için mahkeme onayı gerekir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III", ["Yalnız II", "I ve IV", "II ve III", "I, II ve III", "II, III ve IV"],
    "Kanun m. 101/1 makul şüphe bulunan kişiler hakkında kredili alım ve açığa satış sınırlaması dahil tedbirleri Kurula "
    "bırakır; m. 101/3 (2024) inceleme kapsamında içerik çıkarma ve erişim engeli kararını da Kurula tanır. Mahkeme onayı aranmaz.")

P.q("6362 s. SPKn m. 101/2",
    "Payları borsada işlem gören bir ortaklık, Kurul düzenlemeleri çerçevesinde kendi paylarını satın almak üzere bir program "
    f"başlatmıştır. {K}, Kurulun bu durumda alabileceği önleme ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlişkili kişilerin bu paylarda işlem yapmasına sınırlama getirebilir.",
    ["Geri alım süresince ortaklık paylarının borsada işlem görmesini durdurur.",
     "Geri alınan payların ortaklık tarafından itfa edilmesine karar verir.",
     "Programa katılan yatırımcılara teminat yükümlülüğü getirir.",
     "Programın uygulanmasını YTM’nin onayına bağlar."],
    "Kanun m. 101/2'ye göre Kurul, halka açık ortaklığın kendi paylarını satın alma programı uygulaması hâlinde ortaklıkla "
    "yönetim, denetim veya sermaye bakımından ilişkili gerçek veya tüzel kişiler ile diğer ilgili kişilerin bu paylarda "
    "işlem yapmasına sınırlama getirebilir.")

P.q("6362 s. SPKn m. 102",
    "Bir aracı kurum, müşterisinin işlemlerinin bilgi suistimali niteliği taşıdığından şüphelenmektedir. "
    f"{K}, bu duruma ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Aracı kurum, bildirimde bulunduğunu işleme taraf olan müşterisine bildirebilir.",
    ["Aracı kurum bu şüpheyi Kurula veya Kurulca belirlenecek kuruma bildirmekle yükümlüdür.",
     "Bildirim yükümlülüğünün usul ve esasları Kurulca belirlenir.",
     "Aracı kurum bildirim hakkında mahkemeye bilgi verebilir.",
     "Özel kanunlardaki hükümler, bildirime ilişkin gizlilik yükümlülüğünü ortadan kaldırmaz."],
    "Kanun m. 102'ye göre m. 106 ve 107'deki suçlara ilişkin bilgi veya şüphe hâlinde yatırım kuruluşları Kurula bildirimde "
    "bulunur. Bildirimde bulunanlar, özel kanunlarda hüküm bulunsa dahi, mahkeme, savcılık ve MASAK dışında işleme taraf "
    "olanlar dahil üçüncü kişilere bilgi veremez.")

P.q("6362 s. SPKn m. 35/C-3",
    "Kurulca yurt dışı piyasalarda yaygın işlem gördüğü değerlendirilmeyen bir kripto varlıkta, bir platform nezdinde makul "
    f"ekonomik gerekçesi bulunmayan işlemler yapıldığı görülmüştür. {K}, bu duruma ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Platform işlemlerine piyasa bozucu eylem hükümleri uygulanmaz.",
    ["Platform, bu nitelikteki işlemleri tespit etmekle yükümlüdür.",
     "Platform, işlemleri gerçekleştiren hesapları kısıtlayabilir veya kapatabilir.",
     "Platform, ulaştığı tespitleri rapora bağlayarak Kurula bildirir.",
     "Platformlar, piyasa bozucu işlemleri önlemek için gözetim sistemi kurar."],
    "Kanun m. 35/C-3'e göre yurt dışında yaygın işlem gören kripto varlıklar hariç, platformlarda makul gerekçeyle "
    "açıklanamayan ve güveni bozan eylemlere m. 104 uygulanır. Platformlar gözetim sistemi kurar, bu işlemleri tespit eder, "
    "hesapları kısıtlar veya kapatır ve tespitleri rapora bağlayarak Kurula bildirir.", zorluk="hard")

# ================================================================ idari para cezaları (m. 103, 105)
P.sayisal("6362 s. SPKn m. 103/1",
    "Bir tüzel kişinin Kurul düzenlemelerine aykırı hareket ettiği tespit edilmiştir. "
    f"{K}, bu tüzel kişiye verilecek idari para cezasının üst sınırı belirlenirken son bağımsız denetimden geçmiş yıllık "
    "finansal tablolardaki brüt satış hasılatının yüzde biri ile vergi öncesi kârın yüzde kaçından yüksek olanı esas alınır?",
    "%20", ["%5", "%10", "%25", "%50"],
    "Kanun m. 103/1'e göre tüzel kişilere, aykırılığın ağırlığı ve etkilediği mağdur sayısı dikkate alınarak, aykırılık "
    "tarihinden önceki son bağımsız denetimden geçmiş yıllık finansal tablolarındaki brüt satış hasılatının %1'i ile vergi "
    "öncesi kârının %20'sinden yüksek olanına kadar idari para cezası verilir.", zorluk="hard")

P.q("6362 s. SPKn m. 103/2",
    "Bir aracı kurumun genel müdürü, kurum adına hareket ederken Kurulun bir tebliğine aykırı işlem yapmış; bu aykırılık "
    f"aracı kurumun zararına sonuç doğurmuştur. {K}, idari para cezası uygulamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Genel müdüre ceza verilir, aracı kuruma ayrıca ceza verilmez.",
    ["Genel müdüre ve aracı kuruma ayrı ayrı ceza verilir.",
     "Ceza genel müdüre değil, aracı kuruma verilir.",
     "Aracı kuruma verilecek ceza iki kat artırılır.",
     "Genel müdüre verilecek ceza, aracı kurumun zararının üç katından az olamaz."],
    "Kanun m. 103/2'ye göre aykırılığı yapan kişi tüzel kişinin organı veya temsilcisiyse tüzel kişiye de ceza verilir; ancak "
    "aykırılık temsil edilen tüzel kişinin zararına sonuç doğurmuşsa tüzel kişiye idari para cezası verilmez.", zorluk="hard")

P.q("6362 s. SPKn m. 103/3",
    "Halka açık bir ortaklıkta yönetim kontrolünü sağlayan payları iktisap eden bir kişi, Kurulca verilen ek süre içinde de "
    f"pay alım teklifi zorunluluğunu yerine getirmemiştir. {K}, bu kişi hakkında verilecek idari para cezasının üst sınırı "
    "aşağıdakilerden hangisidir?",
    "Pay alım teklifine konu payların toplam bedeli",
    ["Kişinin iktisap ettiği payların nominal değeri",
     "Pay alım teklifine konu payların toplam bedelinin iki katı",
     "Ortaklığın son yıllık brüt satış hasılatının yüzde biri",
     "Kişinin elde ettiği menfaatin üç katı"],
    "Kanun m. 103/3'e göre m. 26 uyarınca ve gerekirse Kurulca verilen ek süre içinde pay alım teklifi zorunluluğunu yerine "
    "getirmeyenlere pay alım teklifine konu payların toplam bedeline kadar idari para cezası verilir. m. 26/6'ya göre oy "
    "hakları da donar.")

P.sayisal("6362 s. SPKn m. 103/4",
    "Bir ihraççının yönetim kurulu üyesi, Kurulca belirlenen zaman dilimi içinde ihraççı paylarının alım satımından net "
    f"kazanç elde etmiş ve bu kazancı ihraççıya vermemiştir. {K}, bu yükümlülüğün kaç gün içinde yerine getirilmemesi "
    "hâlinde üyeye elde ettiği menfaatin iki katı idari para cezası verilir?",
    "30", ["7", "10", "15", "60"],
    "Kanun m. 103/4'e göre içsel bilgi aranmaksızın, Kurulca belirlenen zaman dilimi içinde ihraççı paylarının alım "
    "satımından kazanç elde eden yönetim kurulu üyeleri ve yöneticiler net kazancı ihraççıya verir; otuz gün içinde "
    "vermeyenlere menfaatin iki katı idari para cezası uygulanır.", zorluk="hard")

P.q("6362 s. SPKn m. 103/6",
    "Halka açık bir ortaklığın, basiretli bir tacirden beklenen ihaleye katılmayarak işi ilişkili olduğu bir şirkete bıraktığı "
    f"ve bu şirketin kârının arttığı tespit edilmiştir. {K}, bu duruma ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Aktif bir işlem yapılmadığı için örtülü kazanç aktarımı oluşmaz.",
    ["Ortaklığa idari para cezası verilir.",
     "Verilecek ceza elde edilen menfaatin iki katından az olamaz.",
     "Ceza, ilişkili şirketin kârının artmasının sağlanması nedeniyle verilir.",
     "Beklenen faaliyetin yapılmaması da kazanç aktarımı sayılır."],
    "Kanun m. 21/2'ye göre basiretli tacirden beklenen faaliyetin yapılmaması yoluyla ilişkili kişilerin kârının artırılması "
    "da örtülü kazanç aktarımıdır. m. 103/6 bu durumda ilgili tüzel kişiye idari para cezası öngörür; ceza menfaatin iki "
    "katından az olamaz.", zorluk="hard")

P.q("6362 s. SPKn m. 103/8",
    "Bir kişinin Kurula gerçeğe aykırı bilgi vererek gereksiz yere denetim yapılmasına neden olduğu anlaşılmıştır. "
    f"{K}, bu kişiye uygulanacak yaptırım aşağıdakilerden hangisidir?",
    "İdari para cezası",
    ["Bir yıldan üç yıla kadar hapis cezası", "Altı aydan iki yıla kadar hapis cezası",
     "Üç yıldan beş yıla kadar hapis ve adli para cezası", "Borsalarda sürekli işlem yasağı"],
    "Kanun m. 103/8'e göre Kurula gerçeğe aykırı veya yanıltıcı bilgi, belge veya açıklama vererek gereksiz olarak m. 88 "
    "uyarınca denetim yapılmasına neden olanlara idari para cezası verilir. Hapis cezaları m. 111'deki bilgi vermeme ve "
    "denetimi engelleme suçlarına aittir.")

P.q("6362 s. SPKn m. 103/9",
    "Kurul, piyasa bozucu eylemde bulunan bir yatırımcının elde ettiği menfaati hesaplamaktadır. "
    f"{K}, bu hesaplamaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşlemler için ödenen komisyon ve vergiler menfaatten düşülür.",
    ["İşlemlerde kullanılan kredilerin faizleri dikkate alınmaz.",
     "Danışmanlık ücretleri menfaatin hesabında dikkate alınmaz.",
     "Menfaatin nakde çevrilip çevrilmediğine bakılmaz.",
     "Hesaplamada dikkate alınacak fiyat ve maliyet yöntemlerini Kurul belirler."],
    "Kanun m. 103/9'a (7518 s. Kanunla 2024) göre m. 103 ve 104'teki menfaat hesaplamalarında komisyonlar, vergiler, kredi "
    "faizleri, danışmanlık ücretleri ve benzeri maliyetler dikkate alınmaz ve menfaatin nakde çevrilip çevrilmediğine "
    "bakılmaz; fiyat ve maliyet yöntemlerini Kurul belirler.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 105/1",
    "Kurul, idari para cezası uygulamadan önce ilgiliden savunma istemiştir. "
    f"{K}, savunma istendiğine ilişkin yazının tebliğinden itibaren kaç gün içinde savunma verilmemesi hâlinde ilgili "
    "savunma hakkından feragat etmiş sayılır?",
    "30", ["10", "15", "45", "60"],
    "Kanun m. 105/1'e göre idari para cezalarının uygulanmasından önce ilgilinin savunması alınır; savunma istendiğine "
    "ilişkin yazının tebliğinden itibaren otuz gün içinde savunma verilmezse savunma hakkından feragat edildiği kabul edilir.",
    zorluk="easy")

P.q("6362 s. SPKn m. 105/2",
    "Bir yatırımcının, hakkında idari yaptırım kararı verilinceye kadar aynı kabahati üç kez işlediği ve bu yolla menfaat "
    f"temin ettiği tespit edilmiştir. {K}, verilecek idari para cezasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Her bir kabahat için ayrı ayrı idari para cezası verilir.",
    ["Tek bir idari para cezası verilir.",
     "Verilecek ceza iki kat artırılır.",
     "Ceza, temin edilen menfaatin üç katından az olamaz.",
     "Zarara sebebiyet verilmişse ceza zararın üç katından az olamaz."],
    "Kanun m. 105/2'ye göre kabahatin idari yaptırım kararı verilinceye kadar birden çok işlenmesi hâlinde tek bir idari para "
    "cezası verilir ve ceza iki kat artırılır; menfaat temin edilmesi veya zarara sebebiyet verilmesi hâlinde ceza bu menfaat "
    "veya zararın üç katından az olamaz.")

P.sayisal("6362 s. SPKn m. 105/3",
    f"{K}, tahsil edilen idari para cezalarının yüzde kaçı gelir kaydedilmek üzere Yatırımcı Tazmin Merkezine aktarılır?",
    "%50", ["%10", "%25", "%40", "%75"],
    "Kanun m. 105/3'e göre tahsil edilen idari para cezalarının yüzde ellisi genel bütçeye gelir kaydedilir, yüzde ellisi "
    "gelir kaydedilmek üzere Yatırımcı Tazmin Merkezine aktarılır.", zorluk="easy")

P.oncul("6362 s. SPKn m. 103/7, 105",
    "Sermaye piyasası mevzuatına aykırılık nedeniyle Kurulca idari para cezası verilmesine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Cezanın uygulanmasından önce ilgilinin savunması alınır.",
     "Ceza kararlarına karşı adli yargı yoluna başvurulur.",
     "Tahsil edilen cezaların yarısı genel bütçeye gelir kaydedilir.",
     "Kurulun talep ettiği belgeleri eksik veya yanıltıcı veren kişilere de idari para cezası verilebilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 105'e göre idari para cezasından önce savunma alınır, tahsil edilen cezaların yarısı genel bütçeye, yarısı "
    "YTM'ye aktarılır ve kararlara karşı idari yargı yoluna başvurulur. m. 103/7 bilgi ve belgeleri eksik, gerçeğe aykırı "
    "veya yanıltıcı verenlere idari para cezası öngörür.")

P.q("6362 s. SPKn m. 4, 109/1",
    "Bir şirket, Kurula başvurmaksızın internet üzerinden yaptığı genel çağrıyla halktan pay satışı yapmış ve topladığı "
    f"parayı yatırımlarında kullanmıştır. {K}, bu fiile ilişkin aşağıdakilerden hangisi doğrudur?",
    "Onaylı izahname olmaksızın halka arz suçu oluşur ve hapis ile adli para cezası öngörülür.",
    ["Kurul onaylı ihraç belgesi alınmış olsaydı satış hukuka uygun olurdu.",
     "Fiil kitle fonlaması sayılır ve genel hükümlere tabidir.",
     "Fiil piyasa bozucu eylemdir ve idari para cezası gerektirir.",
     "Fiil ancak yatırımcılar zarara uğrarsa cezalandırılır."],
    "Kanun m. 4'e göre halka arz için onaylı izahname zorunludur; ihraç belgesi halka arz edilmeksizin satış içindir. "
    "m. 109/1'e göre onaylı izahname yayımlamaksızın halka arz edenler iki yıldan beş yıla kadar hapis ve beş bin günden "
    "on bin güne kadar adli para cezası ile cezalandırılır; kitle fonlaması yalnız izinli platformlar aracılığıyla yapılabilir.")

P.q("6362 s. SPKn m. 105/4",
    "Kurul, bir aracı kuruma sermaye piyasası mevzuatına aykırılık nedeniyle idari para cezası vermiştir. "
    f"{K}, aracı kurumun bu karara karşı başvurabileceği yol aşağıdakilerden hangisidir?",
    "İdari yargı yoluna başvurarak iptal davası açmak",
    ["Asliye ceza mahkemesine itiraz etmek",
     "Sulh ceza hâkimliğine itiraz etmek",
     "Asliye ticaret mahkemesinde tespit davası açmak",
     "Türkiye Sermaye Piyasaları Birliği hakem heyetine başvurmak"],
    "Kanun m. 105/4'e göre Kanun uyarınca verilen idari para cezası kararlarına karşı idari yargı yoluna başvurulabilir; "
    "m. 134'e göre Kurul kararlarına karşı açılacak idari davalar idare mahkemelerinde görülür ve acele işlerden sayılır.",
    zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
