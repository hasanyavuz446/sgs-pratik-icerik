# -*- coding: utf-8 -*-
"""SPK Mevzuatı · Kaydi Sistem ve MKK — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · 6362 s. Sermaye Piyasası Kanunu m. 12/3, 13, 30, 31/4, 35/C-4, 6, 7, 46-47, 73/2, 77-86, 99/B-7, Geçici m. 10
    (7518 s. Kanunla 2024 değişiklikleri: kripto varlık olarak ihraç, müşteri nakitlerinin bankada münferit izlenmesi)
Yeniden değerlenen azami tazmin tutarı sorulmaz; artırma mekanizması sorulur.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_kaydi_sistem_2026.json", lesson="sermaye_piyasasi_ve_finans", topic="kaydi_sistem",
          konu_adi="Kaydi Sistem ve MKK", seed=2026092822,
          surum="6362 s. Sermaye Piyasası Kanunu (7518 s. Kanunla 2024 değişiklikleri dahil); 28.09.2026 kontrolü")

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"

# ================================================================ kaydileştirme (m. 13)
P.q("6362 s. SPKn m. 13/1-3",
    f"{K}, sermaye piyasası araçlarının kaydileştirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaydi araçlar, hamiline yazılı olanlar hariç isme açılmış hesaplarda izlenir.",
    ["Sermaye piyasası araçlarının senede bağlanmaksızın kayden ihracı esastır.",
     "Kurul, belirli araçlar için hak sahibi ismine hesap açılmaksızın toplu hesap tutulmasına karar verebilir.",
     "Kaydi sermaye piyasası araçlarına ilişkin haklar MKK tarafından izlenir.",
     "Kayıtlar, MKK tarafından oluşturulan elektronik ortamda MKK üyelerince tutulur."],
    "Kanun m. 13'e göre kayden ihraç esastır; kaydi araçlar nama veya hamiline yazılı olmalarına bakılmaksızın isme açılmış "
    "hesaplarda izlenir, Kurul toplu hesap tutulmasına karar verebilir. Haklar MKK'ca izlenir, kayıtlar MKK'nın elektronik "
    "ortamında üyelerce tutulur.")

P.q("6362 s. SPKn m. 13/5",
    "Bir yatırımcı, MKK nezdinde kayden izlenen payları üzerinde bir banka lehine rehin tesis etmiştir. "
    f"{K}, bu rehin hakkının üçüncü kişilere karşı ileri sürülebilmesinde hangi tarih esas alınır?",
    "MKK’ya yapılan bildirim tarihi",
    ["Rehin sözleşmesinin imzalandığı tarih", "Rehnin ticaret siciline tescil edildiği tarih",
     "Rehnin ihraççının pay defterine kaydedildiği tarih", "Rehnin KAP’ta ilan edildiği tarih"],
    "Kanun m. 13/5'e göre kayden izlenen sermaye piyasası araçları üzerindeki hakların üçüncü kişilere karşı ileri "
    "sürülebilmesinde MKK'ya yapılan bildirim tarihi esas alınır.", zorluk="easy")

P.q("6362 s. SPKn m. 13/4",
    f"{K}, kaydileştirilmesine karar verilen fiziki sermaye piyasası araçlarının teslimine ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Teslim edilmeyen senetler borsada işlem görmeye devam eder.",
    ["Bu araçların Kurulca belirlenen esaslar çerçevesinde teslimi zorunludur.",
     "Teslim edilen sermaye piyasası araçları hükümsüz hâle gelir.",
     "Teslim edilmeyen araçların alım satımına aracı kurumlarca aracılık edilemez.",
     "Teslimin esasları Kurul tarafından belirlenir."],
    "Kanun m. 13/4'e göre kaydileştirilmesine karar verilen araçların teslimi zorunludur ve teslim edilenler hükümsüz hâle "
    "gelir. Teslim edilmeyen araçlar kaydileştirme kararından sonra borsada işlem göremez ve aracı kurumlarca alım satımına "
    "aracılık edilemez.")

P.q("6362 s. SPKn m. 13/6",
    "Kayden izlenen payları devralan bir yatırımcı, ortaklığın pay defterine kaydedilmek için ortaklığa ayrıca başvurmamıştır. "
    f"{K}, payların devrinin pay defterine kaydına ilişkin aşağıdakilerden hangisi doğrudur?",
    "MKK nezdinde izlenen kayıtlar esas alınır.",
    ["Devralanın ortaklığa yazılı başvurusu olmadan kayıt yapılamaz.",
     "Kayıt, devrin noterce onaylanmasından sonra yapılır.",
     "Kayıt, ortaklık yönetim kurulunun onay kararına bağlıdır.",
     "Kayıt için devrin ticaret sicilinde ilan edilmesi gerekir."],
    "Kanun m. 13/6'ya göre payların devrinin TTK hükümleri çerçevesinde pay defterine kaydında, ilgililerin başvurusuna gerek "
    "kalmaksızın MKK nezdinde izlenen kayıtlar esas alınır.")

P.q("6362 s. SPKn m. 13/7",
    "Bir vergi dairesi, borçlu bir mükellefin MKK nezdinde kayden izlenen paylarına haciz koymak istemektedir. "
    f"{K}, bu haciz talebi kim tarafından yerine getirilir?",
    "Hesabın bulunduğu MKK üyesi aracı kurum",
    ["Merkezî Kayıt Kuruluşu Anonim Şirketi", "Payları ihraç eden ortaklığın yönetim kurulu",
     "Payların işlem gördüğü Borsa İstanbul", "Sermaye Piyasası Kurulu Başkanlığı"],
    "Kanun m. 13/7'ye göre kayden izlenen sermaye piyasası araçlarına ilişkin tedbir, haciz ve benzeri her türlü idari ve "
    "adli talepler münhasıran MKK'nın üyeleri tarafından yerine getirilir; elektronik tebligatla yapılan takiplere ilişkin "
    "hükümler saklıdır.")

P.q("6362 s. SPKn m. 13/1 (2024)",
    "Kurul, belirli sermaye piyasası araçlarının MKK’da kayden izlenmesi yerine kripto varlık olarak ihracına ilişkin esaslar "
    f"belirlemiştir. {K}, bu şekilde ihraç edilen araçlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hakların devrinde hizmet sağlayıcının elektronik kayıtları esas alınır.",
    ["Hakların üçüncü kişilere karşı ileri sürülebilmesinde MKK’ya bildirim tarihi esas alınır.",
     "Bu araçlar MKK kaydına alınmadıkça devredilemez.",
     "Kurul, bu kayıtlarla MKK sistemi arasında entegrasyon sağlanmasını zorunlu tutamaz.",
     "Bu araçlar kripto varlık olarak ihraç edildikleri için sermaye piyasası aracı sayılmaz."],
    "Kanun m. 13/1'e 7518 s. Kanunla eklenen cümlelere göre Kurul, araçların kripto varlık olarak ihracına ve hizmet "
    "sağlayıcıların elektronik ortamında izlenmesine esas belirleyebilir; hakların izlenmesi, üçüncü kişilere karşı ileri "
    "sürülmesi ve devrinde bu kayıtlar esas alınır. Kurul MKK ile entegrasyonu zorunlu tutabilir.", zorluk="hard")

P.oncul("6362 s. SPKn m. 12/3, 13",
    "Kaydi sisteme ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Sermaye piyasası araçlarının satış esnasında alıcıya teslimi şarttır; Kurulun kaydileştirme düzenlemeleri saklıdır.",
     "Kaydi araçlara ilişkin kayıtlar MKK üyeleri tarafından tutulur.",
     "Kaydi araçlar üzerindeki haciz talepleri ihraççı tarafından yerine getirilir.",
     "Kurul, üyelik şartlarını kaybeden ihraççıların paylarının kayden izlenmesinin sona erdirilmesine ilişkin esasları düzenler."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 12/3 teslimi şart koşar ve kaydileştirme düzenlemelerini saklı tutar; m. 13/3'e göre kayıtlar MKK üyelerince "
    "tutulur; m. 13/1 Kurula üyelik şartlarını kaybeden ihraççıların paylarının kayden izlenmesinin sona erdirilmesi "
    "esaslarını düzenleme yetkisi verir. Haciz talepleri m. 13/7'ye göre MKK üyelerince yerine getirilir.")

# ================================================================ yatırımcı varlıkları ve teminatlar (m. 46-47)
P.q("6362 s. SPKn m. 46/5-6",
    f"{K}, yatırımcıların yatırım kuruluşları nezdinde bulunan nakit ve sermaye piyasası araçlarına ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Bu varlıklar, yatırım kuruluşunun kamuya olan borçları nedeniyle haczedilebilir.",
    ["Bu varlıklar yatırım kuruluşunun malvarlığından ayrı izlenir.",
     "Yatırımcının yazılı açık izni olmadan tevdi amacı dışında kullanılamaz.",
     "Yatırım kuruluşunun malvarlığı yatırımcıların borçları nedeniyle haczedilemez.",
     "Yatırımcının yazılı ön izni olmadan rehnedilemez ve iflas masasına dâhil edilemez."],
    "Kanun m. 46/5-6'ya göre yatırımcı varlıkları yatırım kuruluşunun malvarlığından ayrı izlenir, yazılı açık izin olmadan "
    "tevdi amacı dışında kullanılamaz; kamu alacakları için olsa dahi yatırım kuruluşunun borçları nedeniyle haczedilemez, "
    "yazılı ön izin olmadan rehnedilemez ve iflas masasına girmez. Yatırım kuruluşunun malvarlığı da yatırımcı borçları "
    "nedeniyle haczedilemez.")

P.q("6362 s. SPKn m. 46/7-8 (2024)",
    "Bir aracı kurum, müşterilerinden tahsil ettiği nakitleri bir bankada tutmaktadır. "
    f"{K}, bu hesaplara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müşteri hesapları aracı kurumun kullandığı krediler için teminat gösterilebilir.",
    ["Müşteri nakitleri müşteriler için açılan münferit hesaplarda kurumun kendi nakdinden ayrı izlenir.",
     "Müşteri hesaplarının bankalarda nemalandırılmasına ilişkin esasları Kurul belirler.",
     "Bankanın bu kapsamdaki sorumluluğu aracı kurumun yaptığı bildirimlerle sınırlıdır.",
     "Bu hesaplardaki müşterilere ilişkin haciz talepleri aracı kuruma bildirilir ve kurumca yerine getirilir."],
    "Kanun m. 46/7'ye (7518 s. Kanun) göre müşteri nakitleri münferit hesaplarda kurumun kendi nakdinden ayrı izlenir; müşteri "
    "hesapları kredi teminatı gösterilemez ve üzerlerinde kurum lehine blokaj veya rehin tesis edilemez. Nemalandırma "
    "esaslarını Kurul belirler, bankanın sorumluluğu bildirimlerle sınırlıdır, haciz talepleri yatırım kuruluşuna bildirilir.")

P.oncul("6362 s. SPKn m. 46/2",
    "Sermaye piyasasında teminat istenmesine ilişkin aşağıdaki durumlar verilmiştir:",
    ["Yatırım kuruluşunun, kredili işlem yapan yatırımcıdan teminat istemesi",
     "Borsanın, yatırım hizmetleri kapsamında yatırımcılardan teminat istemesi",
     "Takas kuruluşunun, yatırım kuruluşlarından teminat istemesi",
     "Yatırımcı Tazmin Merkezinin, işlem yapan yatırımcılardan teminat istemesi"],
    f"{K}, yukarıdakilerden hangileri Kanunda öngörülen teminat isteme yetkileri arasındadır?",
    "I, II ve III", ["Yalnız I", "I ve IV", "II ve III", "I, II ve III", "II, III ve IV"],
    "Kanun m. 46/2'ye göre yatırım kuruluşları kredili işlemler, ödünç ve açığa satış işlemleri ile diğer hizmetler nedeniyle "
    "yatırımcılardan; borsalar ile takas ve saklama kuruluşları yatırım kuruluşları ve yatırımcılardan teminat isteyebilir. "
    "YTM'ye böyle bir yetki tanınmamıştır; yatırım kuruluşları YTM'ye aidat öder.")

P.q("6362 s. SPKn m. 46/4",
    "Bir aracı kurumun, Kurul düzenlemeleri uyarınca yatırdığı teminatlar üzerine bir alacaklısı haciz koydurmak istemektedir. "
    f"{K}, bu teminatlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kamu alacakları için olsa dahi haczedilemez ve iflas masasına dâhil edilemez.",
    ["Aracı kurumun kamu borçları için haczedilebilir.",
     "Kurul izniyle üçüncü kişilere devredilebilir.",
     "Aracı kurum iflas ederse iflas masasına dâhil edilir ve alacaklılar arasında paylaştırılır.",
     "Mahkeme kararıyla ihtiyati tedbir konulabilir."],
    "Kanun m. 46/4'e göre bu maddedeki teminatlar tevdi amaçları dışında kullanılamaz, üçüncü kişilere devredilemez, kamu "
    "alacakları için olsa dahi haczedilemez, rehnedilemez, iflas masasına dâhil edilemez ve üzerlerine ihtiyati tedbir konulamaz.")

P.q("6362 s. SPKn m. 47/1",
    "MKK’da kayden izlenen paylar üzerinde yazılı bir teminat sözleşmesi yapılmış, ancak sözleşmede payların mülkiyetinin "
    f"kimde kalacağına ilişkin bir hüküm bulunmamaktadır. {K}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Payların mülkiyeti teminat alana geçmemiş sayılır.",
    ["Payların mülkiyeti sözleşmenin kurulduğu anda teminat alana geçer.",
     "Sözleşme mülkiyet hükmü içermediği için geçersizdir.",
     "Mülkiyetin kimde kalacağına MKK karar verir.",
     "Paylar teminat alan ile veren arasında paylı mülkiyete tabi olur."],
    "Kanun m. 47/1'e göre teminat sözleşmeleri yazılı yapılır; mülkiyet sözleşmeye bağlı olarak teminat alana devredilebilir "
    "veya teminat verende kalabilir. Sözleşmede hüküm yoksa teminat konusu araçların mülkiyeti teminat alana geçmemiş sayılır.")

P.q("6362 s. SPKn m. 47/4",
    "Mülkiyetin teminat verende kaldığı bir teminat sözleşmesinde borçlu temerrüde düşmüştür. "
    f"{K}, teminat alanın haklarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Teminatın paraya çevrilmesi için icra dairesi aracılığıyla açık artırma yapılması gerekir.",
    ["Teminat alan, borsada kote araçları piyasa değerinden aşağı olmamak üzere satabilir.",
     "Teminat alanın araçları mülkiyetine geçirebilmesi için bu hakkın sözleşmede açıkça öngörülmesi gerekir.",
     "Kote olmayan araçlarda değerlemenin nasıl yapılacağı sözleşmede öngörülmelidir.",
     "Alacak karşılandıktan sonra arta kalan değer teminat verene iade edilir."],
    "Kanun m. 47/4'e göre temerrüt hâlinde ihbar, süre verme, merci izni veya açık artırma gibi ön şart aranmaksızın teminat "
    "alan kote araçları piyasa değerinin altında olmamak üzere satabilir; mülkiyetine geçirme için bu hakkın ve kote "
    "olmayanlarda değerleme yönteminin sözleşmede açıkça öngörülmesi gerekir. Arta kalan değer iade edilir.", zorluk="hard")

P.q("6362 s. SPKn m. 47/4-c",
    "Borsada kote payların teminat olarak verildiği bir sözleşmede borçlu vade tarihinde yükümlülüğünü yerine getirmemiştir. "
    f"{K}, teminat alanın temerrüt nedeniyle doğan haklarını kullanmasında payların hangi değeri esas alınır?",
    "Vade tarihindeki en yüksek değeri",
    ["Sözleşmenin kurulduğu tarihteki değeri", "Vade tarihindeki kapanış değeri",
     "Temerrüdü izleyen ilk seanstaki ağırlıklı ortalama değeri", "Son altı aylık ortalama değeri"],
    "Kanun m. 47/4-c'ye göre (a) ve (b) bentlerinin uygulanmasında, borsaya veya teşkilatlanmış diğer piyasalara kote olan "
    "teminat konusu araçlar bakımından vade tarihindeki en yüksek değer esas alınır; arta kalan değer teminat verene iade edilir.",
    zorluk="hard")

P.q("6362 s. SPKn m. 47/5",
    "Kayden izlenen paylarını bir teminat sözleşmesiyle teminat olarak veren bir şirket hakkında mahkemece tasfiye kararı "
    f"verilmiştir. {K}, bu kararın teminata etkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Teminat ve tarafların hakları bu karardan etkilenmez.",
    ["Teminat sözleşmesi tasfiye kararıyla sona erer.",
     "Teminat konusu paylar tasfiye masasına dâhil edilir.",
     "Teminat alan, alacağını diğer alacaklılarla garameten tahsil eder.",
     "Teminat alanın hakları tasfiye memurunun onayına bağlanır."],
    "Kanun m. 47/5'e göre teminat alan veya veren hakkında yeniden yapılandırma veya tasfiye kararı verilmesi hâlinde teminat "
    "olarak verilen araçlar ile tarafların hakları bu karardan etkilenmez ve tasfiye makamına karşı da geçerli olur.")

P.oncul("6362 s. SPKn m. 47",
    "MKK nezdinde kayden izlenen sermaye piyasası araçlarını konu alan teminat sözleşmelerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Sözleşmeler yazılı şekilde yapılır.",
     "Mülkiyetin devredildiği sözleşmede teminat alan, sözleşme sona erince araçların eş değerini de iade edebilir.",
     "Temerrüt hâlinde satış için önceden ihtarda bulunulması gerekir.",
     "Hükümleri özel kanunlarla düzenlenen teminat sözleşmelerine de bu madde uygulanır."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve II", ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Kanun m. 47/1'e göre sözleşmeler yazılı yapılır; m. 47/2'ye göre mülkiyetin devredildiği sözleşmede teminat alan araçları "
    "veya eş değerini iade eder. m. 47/4 temerrüt hâlinde ihbar ve ihtar gibi ön şartları aramaz; m. 47/6 özel kanunlarla "
    "düzenlenen teminat sözleşmelerini kapsam dışında tutar.")

# ================================================================ merkezi takas, MKT, takas kesinliği (m. 73, 77-79)
P.q("6362 s. SPKn m. 77",
    f"{K}, merkezî takas kuruluşlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Merkezî takas kuruluşlarının kuruluşuna Kurul Karar Organı izin verir.",
    ["Anonim ortaklık şeklinde kurulan özel hukuk tüzel kişileridir.",
     "Faaliyete geçmeleri Kurulun iznine tabidir.",
     "Yetkilendirilmeleri kaydıyla lisanslı depoların ürün senetleri için de takas yürütebilirler.",
     "Takas hizmeti verebilecekleri borsaları Kurul belirler."],
    "Kanun m. 77'ye göre merkezî takas kuruluşları anonim ortaklık şeklindeki özel hukuk tüzel kişileridir; kuruluşlarına "
    "Kurulun teklifi üzerine ilgili Bakan izin verir, faaliyete geçmeleri Kurul iznine tabidir. Ürün senetleri için de takas "
    "yürütebilir; takas hizmeti verecekleri borsaları, borsaların uygun görüşünü alarak Kurul belirler.")

P.q("6362 s. SPKn m. 78",
    f"{K}, merkezî karşı taraf hizmetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Takas kuruluşu, üyelerinin müşterilerine olan yükümlülüklerinden de sorumludur.",
    ["Merkezî karşı taraf hizmeti kapsamında alınan teminatların mülkiyeti takas kuruluşuna geçer.",
     "Merkezî karşı taraf, her işlemde taraflarla ayrı ayrı sözleşme yapmak zorunluluğunda değildir.",
     "Kurul, merkezî karşı taraf uygulamasını piyasalar itibarıyla zorunlu tutabilir.",
     "Temerrüt yönetiminde pozisyonlar resen kapatılabilir."],
    "Kanun m. 78'e göre MKT hizmetinde alınan teminatların mülkiyeti takas kuruluşuna geçer; takas kuruluşu üyelerinin "
    "müşterilerine olan yükümlülüklerinden sorumlu değildir. Kurul uygulamayı zorunlu tutabilir, her işlem için ayrı "
    "sözleşme şartı yoktur ve temerrüt yönetiminde pozisyonlar resen kapatılabilir.")

P.sayisal("6362 s. SPKn m. 78/5",
    "Merkezî karşı taraf hizmeti veren bir takas kuruluşunun iç denetim birimi, risk yönetimi ve bilgi işlem altyapısının "
    f"güvenilirliğini düzenli olarak kontrol etmektedir. {K}, bu kontrol asgari kaç aylık dönemler itibarıyla yapılır?",
    "6", ["1", "3", "12", "24"],
    "Kanun m. 78/5'e göre MKT hizmeti verecek kuruluşların iç denetim birimleri, risk yönetim ve bilgi işlem altyapılarının "
    "güvenilirliğini ve yeterliliğini asgari altı aylık dönemler itibarıyla kontrol ederek sonuçlarını Kurula bildirir; "
    "Kurul daha sık kontrol isteyebilir.", zorluk="hard")

P.q("6362 s. SPKn m. 78/10",
    "Bir merkezî takas kuruluşu hem sermaye piyasasında hem organize para piyasasında merkezî karşı taraf hizmeti "
    f"vermektedir. {K}, bu kuruluşun aldığı teminatlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "İki piyasa için alınan teminatlar ve garanti fonu varlıkları birbirinden ayrı izlenir.",
    ["İki piyasanın teminatları tek havuzda izlenir ve birbirinin açığını kapatabilir.",
     "Para piyasası teminatları TCMB nezdinde, sermaye piyasası teminatları Kurul nezdinde izlenir.",
     "Garanti fonu varlıkları kuruluşun genel giderleri için kullanılabilir.",
     "Tahsis edilen sermaye, her iki piyasadaki temerrütler için ortak kullanılır."],
    "Kanun m. 78/10'a göre her piyasa için tahsis edilen sermaye, alınan teminatlar ve garanti fonları amaçları dışında "
    "kullanılamaz; sermaye piyasalarına ilişkin teminatlar ve garanti fonu varlıkları para piyasalarına ilişkin olanlardan "
    "ayrı izlenir.")

P.q("6362 s. SPKn m. 79/1",
    "Bir takas üyesi aracı kurumun faaliyetleri, verdiği takas talimatlarından sonra Kurulca geçici olarak durdurulmuştur. "
    f"{K}, bu talimatlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Talimatlar durdurma kararından etkilenmez; geri alınamaz ve iptal edilemez.",
    ["Talimatlar durdurma kararıyla birlikte iptal olur.",
     "Talimatlar Kurulun onayıyla geri alınabilir.",
     "Talimatların yerine getirilmesi mahkeme kararına bağlanır.",
     "Talimatlar YTM’nin tazmin kararına kadar askıya alınır."],
    "Kanun m. 79/1'e göre takas talimat ve işlemleri ile ödeme işlemleri, üyelerin faaliyetlerinin geçici veya sürekli "
    "durdurulması ve tasfiye işlemlerine başlanması durumunda da geri alınamaz ve iptal edilemez (takas kesinliği).",
    zorluk="easy")

P.q("6362 s. SPKn m. 79/2-3",
    f"{K}, merkezî takas kuruluşunun teminat olarak aldığı mal varlığı değerleri üzerindeki haklarına ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Teminatı veren üyeye konkordato mühleti verilmesi bu hakların kullanılmasını durdurur.",
    ["Teminat üzerinde tasarruf yetkisinin bulunmaması takas kuruluşunun iyi niyetle ayni hak iktisabına engel olmaz.",
     "Üçüncü kişilerin istihkak iddiaları takas kuruluşuna karşı ileri sürülemez.",
     "Teminatı tesis eden kişinin iflası bu hakların kullanılmasını sınırlandıramaz.",
     "Türk Medeni Kanunu’nun iyi niyetle iktisaba ilişkin hükümleri kaydi araçlar için de uygulanır."],
    "Kanun m. 79/2'ye göre TMK m. 988-991 kaydi teminatlara uygulanır; tasarruf yetkisinin yokluğu iyi niyetli iktisaba engel "
    "olmaz ve istihkak iddiaları takas kuruluşuna karşı ileri sürülemez. m. 79/3'e göre konkordato, iflas, uzlaşma yoluyla "
    "yeniden yapılandırma veya tedrici tasfiye takas kuruluşunun teminat üzerindeki hak ve yetkilerini sınırlandıramaz.",
    zorluk="hard")

P.q("6362 s. SPKn m. 73/2",
    "Bir aracı kurumun borsa ve takas kuruluşu nezdindeki teminatları ile garanti fonuna yatırdığı varlıklar hakkında, "
    f"aracı kurumun vergi borcu nedeniyle haciz talep edilmiştir. {K}, bu varlıklara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kamu alacakları için olsa dahi haczedilemez.",
    ["Kamu alacakları için haczedilebilir, özel alacaklar için haczedilemez.",
     "Garanti fonundaki varlıklar haczedilebilir, teminatlar haczedilemez.",
     "Kurulun onayı alınarak haczedilebilir.",
     "Aracı kurumun iflası hâlinde iflas masasına dâhil edilir."],
    "Kanun m. 73/2'ye göre borsalar ve takas kuruluşları nezdinde takas risklerinin önlenmesi amacıyla tutulan teminatlar ve "
    "garanti fonundaki varlıklar amaçları dışında kullanılamaz, kamu alacakları için olsa dahi haczedilemez, rehnedilemez, "
    "idari mercilerin tasfiye kararlarından etkilenmez ve iflas masasına dâhil edilemez.")

# ================================================================ merkezi saklama ve MKK (m. 80-81, 30, 31/4)
P.q("6362 s. SPKn m. 80",
    f"{K}, merkezî saklama kuruluşlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaydileştirilen sermaye piyasası araçlarının merkezî saklama kuruluşu Takasbank’tır.",
    ["Merkezî saklama kuruluşları anonim ortaklık şeklindeki özel hukuk tüzel kişileridir.",
     "Kuruluşlarına Kurulun uygun görüşü üzerine ilgili Bakan izin verir.",
     "Faaliyete geçmeleri Kurul iznine tabidir.",
     "Kurul, belirli araçların bir veya birden fazla merkezî saklama kuruluşunda saklanmasını zorunlu tutabilir."],
    "Kanun m. 80'e göre merkezî saklama kuruluşları anonim ortaklık şeklindeki özel hukuk tüzel kişileridir; kuruluşlarına "
    "Kurulun uygun görüşü üzerine ilgili Bakan izin verir, faaliyete geçmeleri Kurul iznine tabidir. Kurul saklama "
    "zorunluluğu getirebilir; kaydileştirilen araçların merkezî saklama kuruluşu MKK'dır.")

P.q("6362 s. SPKn m. 81/3",
    f"{K}, aşağıdakilerden hangisi Merkezî Kayıt Kuruluşunun Kanunda sayılan görevleri arasında yer almaz?",
    "Borsada işlem gören payların alım satım emirlerini eşleştirmek",
    ["Şirketler ile ortakları ve yatırımcılarının iletişimi için elektronik platform oluşturmak",
     "Sermaye piyasalarına ilişkin verilerin tek noktada toplanması için veri bankası oluşturmak",
     "Yetkilendirilmesi kaydıyla lisanslı depo ürün senetlerini kaydileştirmek",
     "Kaydileştirilen araçların merkezî saklamasını yapmak"],
    "Kanun m. 81'e göre MKK kaydileştirme işlemlerini yürütür, araçları ve hakları kayden izler ve merkezî saklamasını yapar; "
    "ayrıca kurumsal yönetim için elektronik platform, sermaye piyasası veri bankası ve ürün senetlerinin kaydileştirilmesi "
    "görevleri vardır. Emir eşleştirmek borsaların görevidir.", zorluk="easy")

P.q("6362 s. SPKn m. 81/5",
    "Bir aracı kurumun MKK sistemindeki hatalı kaydı nedeniyle bir yatırımcının payları başka bir hesaba aktarılmış ve "
    f"yatırımcı zarara uğramıştır. {K}, bu zarardan sorumluluğa ilişkin aşağıdakilerden hangisi doğrudur?",
    "MKK ve üyeleri kayıtların yanlış tutulmasından kusurları oranında sorumludur.",
    ["Zarardan münhasıran MKK sorumludur, üye aracı kurum sorumlu tutulamaz.",
     "Zararı Yatırımcı Tazmin Merkezi karşılar, taraflar sorumlu tutulamaz.",
     "MKK ile üyeler, kusur aranmaksızın ve zararın tamamından müteselsilen sorumludur.",
     "Zarardan ihraççı ortaklık sorumludur."],
    "Kanun m. 81/5'e göre MKK ve üyeleri, kayıtların yanlış tutulmasından dolayı hak sahiplerinin uğrayacağı zararlardan "
    "kusurları oranında sorumludur.")

P.q("6362 s. SPKn m. 81/4, 77/6",
    "MKK, bir üyesinden müşteri hesaplarına ilişkin bilgi ve belge istemiş; üye, bankacılık mevzuatındaki sır saklama "
    f"hükümlerini gerekçe göstererek bilgi vermeyi reddetmiştir. {K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Üye, özel mevzuatına dayanarak bilgi vermekten kaçınamaz.",
    ["Üyenin reddi haklıdır; bilgi ancak mahkeme kararıyla alınabilir.",
     "MKK bilgiyi ancak Kurul aracılığıyla isteyebilir.",
     "Bilgi, müşterinin yazılı onayı alınmadan paylaşılamaz.",
     "Talep ancak BDDK’nın uygun görüşüyle yerine getirilir."],
    "Kanun m. 81/4'e göre MKK, Kurul düzenlemeleri çerçevesinde üyelerinden bilgi ve belge istemeye ve inceleme yapmaya "
    "yetkilidir; üyeler MKK'nın görev alanına giren hususlarda özel mevzuatlarındaki hükümlere dayanarak bilgi vermekten "
    "imtina edemez. Aynı kural m. 77/6'da merkezî takas kuruluşları için de öngörülmüştür.")

P.q("6362 s. SPKn m. 30/2, 30/5",
    "Payları kayden izlenen halka açık bir ortaklığın genel kurul toplantısı yapılacaktır. "
    f"{K}, toplantıya katılım ve oy kullanmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Genel kurula katılım, payların bir kuruluş nezdinde depo edilmesi şartına bağlanabilir.",
    ["Hazır bulunanlar listesi, MKK’dan sağlanan pay sahipleri listesi dikkate alınarak oluşturulur.",
     "Listede adı bulunan hak sahipleri kimlik göstererek genel kurula katılır.",
     "Elektronik ortamda katılım MKK tarafından sağlanan sistem üzerinden gerçekleştirilir.",
     "Oy hakkı sahipleri haklarını vekil tayin ettikleri kişiler aracılığıyla da kullanabilir."],
    "Kanun m. 30/1'e göre halka açık ortaklık genel kuruluna katılma ve oy kullanma hakkı payların depo edilmesi şartına "
    "bağlanamaz. m. 30/2'ye göre hazır bulunanlar listesi MKK'dan sağlanan listeye göre oluşturulur; m. 30/4 vekâleti, "
    "m. 30/5 MKK elektronik ortamı üzerinden katılımı düzenler.")

P.q("6362 s. SPKn m. 31/4",
    "Bir ihraççı, tedavüldeki tahvillerinin kupon ve anapara ödemesini vadesinde yapmamıştır. "
    f"{K}, MKK tarafından düzenlenip tahvil sahiplerine verilen belgenin hukuki niteliği aşağıdakilerden hangisidir?",
    "İcra ve İflas Kanunu m. 68/1’de sayılan belgelerden sayılır.",
    ["Kambiyo senedi hükmündedir.", "İlamlı icraya konu mahkeme ilamı hükmündedir.",
     "Ancak alacağın varlığına ilişkin karine oluşturur.", "İhraççının ticaret siciline tescil edilmesi gereken belgedir."],
    "Kanun m. 31/4'e göre ihraççıların borçlanma araçlarına ilişkin ödeme yükümlülüklerini yerine getirmemesi nedeniyle MKK "
    "tarafından düzenlenip hak sahiplerine verilen belge İİK m. 68/1'de belirtilen belgelerden sayılır; itirazın kaldırılmasında "
    "dayanak belge olarak kullanılabilir.", zorluk="hard")

# ================================================================ yatırımcı tazmini ve YTM (m. 82-85, 83/4, Geçici m. 10)
P.q("6362 s. SPKn m. 82",
    f"{K}, yatırımcıların tazmin kararına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bankalar hakkında tazmin kararı verilebilmesi için TMSF’nin onayı alınır.",
    ["Tazmin kararı, yatırım kuruluşunun nakit ödeme veya araç teslim yükümlülüğünü yerine getiremediğinin tespitinde alınır.",
     "Yükümlülüğün kısa sürede yerine getirilemeyeceğinin tespiti de tazmin kararı için yeterlidir.",
     "Bankacılık mevzuatına göre mevduat sayılan nakit yükümlülükleri tazmin hükümlerinin dışındadır.",
     "Kurulun tazmin kararı dışındaki tedbir yetkileri saklıdır."],
    "Kanun m. 82'ye göre Kurul, yatırım kuruluşlarının nakit ödeme veya araç teslim yükümlülüklerini yerine getiremediğinin "
    "veya kısa sürede getiremeyeceğinin tespitinde tazmin kararı alır ve tedbir yetkileri saklıdır. Bankalar hakkında karar "
    "için BDDK'nın görüşü alınır; mevduat ve katılım fonu niteliğindeki yükümlülükler kapsam dışıdır.")

P.q("6362 s. SPKn m. 83",
    f"{K}, Yatırımcı Tazmin Merkezine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "YTM, özel hukuk tüzel kişiliğine sahip bir anonim şirkettir.",
    ["YTM, Kurulun çıkaracağı yönetmelik çerçevesinde Kurul tarafından idare ve temsil olunur.",
     "Yatırım kuruluşlarının YTM’ye katılması zorunludur.",
     "YTM’nin mal varlığı kamu alacakları için olsa dahi haczedilemez.",
     "YTM’nin bu Kanun kapsamındaki işlemleri harçtan müstesnadır."],
    "Kanun m. 83'e göre YTM kamu tüzel kişiliğini haiz olup Kurul tarafından idare ve temsil olunur; yatırım kuruluşlarının "
    "katılımı zorunludur. Mal varlığı amacı dışında kullanılamaz ve kamu alacakları için olsa dahi haczedilemez; işlemleri "
    "harçtan, kâğıtları damga vergisinden müstesnadır.", zorluk="easy")

P.oncul("6362 s. SPKn m. 83",
    "Yatırımcı Tazmin Merkezine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Yatırım kuruluşlarının giriş aidatı, yıllık aidat ve ek aidat yükümlülükleri yönetmelikle belirlenir.",
     "Aidat tutarı belirlenirken kuruluşların tür ve risk durumlarına göre farklı esaslar öngörülebilir.",
     "YTM’nin faaliyetleri dolayısıyla kurumlar vergisi açısından iktisadi işletme oluşur.",
     "YTM, tazmin kararı verilen kuruluşun ödemelerinin durmasına karar verebilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 83/2 aidat yükümlülüklerini ve risk bazlı farklılaştırmayı yönetmeliğe bırakır; m. 83/3 YTM'ye tazmin kararı "
    "verilen kuruluşun ödemelerinin durmasına ve mal varlığı üzerinde yalnız YTM'nin tasarrufuna karar verme yetkisi tanır. "
    "m. 83/6'ya göre YTM'nin faaliyetleri dolayısıyla iktisadi işletme oluşmuş sayılmaz.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 83/4",
    "Bir yatırımcı, aracı kurumdaki hesabında bulunan paylara ilişkin uzun süredir herhangi bir talepte bulunmamış ve talimat "
    f"vermemiştir. {K}, yatırımcının son talep veya talimat tarihinden itibaren kaç yıl içinde talep ve tahsil edilmeyen "
    "emanet ve alacaklar YTM’ye emaneten devredilir?",
    "10", ["3", "5", "7", "20"],
    "Kanun m. 83/4'e (7316 s. Kanunla 2021) göre yatırım hizmetlerinden kaynaklanan emanet ve alacaklar, hesap sahibinin son "
    "talep, işlem veya yazılı talimat tarihinden başlayarak on yıl içinde talep ve tahsil edilmezse YTM'ye emaneten devredilir.")

P.q("6362 s. SPKn m. 83/4",
    "Talep edilmediği için YTM’ye emaneten devredilen paylar, hak sahibine iade edilinceye kadar YTM nezdinde izlenmektedir. "
    f"{K}, bu paylara bağlı haklara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bedelsiz pay iktisabı ve kâr payı alma hakkı dışındaki pay sahipliği hakları donar.",
    ["Tüm pay sahipliği hakları YTM tarafından hak sahibi adına kullanılır.",
     "Paylar YTM’ye gelir kaydedilir ve hak sahibine iade edilmez.",
     "Oy hakları YTM tarafından kullanılır, kâr payları Hazineye aktarılır.",
     "Paylara bağlı tüm haklar iade tarihine kadar donar."],
    "Kanun m. 83/4'e göre YTM'ye devredilen sermaye piyasası araçlarından doğan bedelsiz pay iktisabı ve kâr payı alma hakkı "
    "dışındaki pay sahipliği hakları, hak sahiplerine iadeye kadar donar; iade esaslarını Kurul belirler.", zorluk="hard")

P.sayisal("6362 s. SPKn Geçici m. 10",
    "Fiziki pay senetlerini kaydileştirme sürecinde teslim etmeyen bir yatırımcının paylarının mülkiyeti YTM’ye intikal "
    f"etmiştir. {K}, bu intikalin ölçütü olarak kayden izlenmeye başlandığı tarihi izleyen kaçıncı yılın sonuna kadar teslim "
    "edilmeme esas alınmıştır?",
    "7", ["2", "3", "5", "10"],
    "Kanun Geçici m. 10'a göre kayden izlenmeye başlandığı tarihi izleyen yedinci yılın sonuna kadar teslim edilmediği için "
    "mülkiyeti YTM'ye intikal etmiş araçların iadesi veya satış bedellerinin ödenmesine ilişkin esasları Kurul belirler.",
    zorluk="hard")

P.q("6362 s. SPKn m. 84/1-2",
    "Tazmin kararı verilen bir aracı kurumun müşterisi, aracı kurumun önerisiyle aldığı payların fiyatının düşmesi nedeniyle "
    f"uğradığı zararın tazminini talep etmektedir. {K}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Piyasadaki fiyat hareketlerinden kaynaklanan zararlar tazmin kapsamında değildir.",
    ["Zarar, azami tazmin tutarına kadar YTM tarafından karşılanır.",
     "Yatırım danışmanlığı kaynaklı zararlar tazmin kapsamındadır.",
     "Zarar, aracı kurum ortaklarından tahsil edilmek üzere YTM’ce ödenir.",
     "Talep, fiyat düşüşünün yarısı oranında ve azami tazmin tutarını aşmamak üzere karşılanır."],
    "Kanun m. 84/1'e göre tazminin kapsamını yatırım kuruluşunca saklanan veya yönetilen nakit ve araçların teslim "
    "yükümlülüğünün yerine getirilmemesinden doğan talepler oluşturur; m. 84/2'ye göre yatırım danışmanlığı veya piyasadaki "
    "fiyat hareketlerinden kaynaklanan zararlar tazmin kapsamında değildir.")

P.q("6362 s. SPKn m. 84/4",
    "Tazmin kararı verilen bir aracı kurumun aşağıdaki müşterileri YTM’ye başvurmuştur. "
    f"{K}, bu müşterilerden hangisi tazmin edilebilecekler arasındadır?",
    "Sermayenin yüzde ikisine sahip, yönetimde görevi olmayan ortak",
    ["Aracı kurumun yönetim kurulu üyesinin eşi",
     "Aracı kurumda sermayenin yüzde beşine sahip olan ortak",
     "Aracı kurumla aynı grupta yer alan bir finansman şirketi",
     "Aracı kurumun mali sıkıntıya düşmesine neden olan işlemlerden menfaat sağlayan kişi"],
    "Kanun m. 84/4'e göre yönetim kurulu üyeleri ve yöneticiler, yüzde beş veya daha fazla paya sahip ortaklar ve bunların "
    "eşleri ile hısımları, aynı gruptaki şirketler ve mali sıkıntıda sorumluluğu olan veya menfaat sağlayan kişiler tazmin "
    "edilmez. Yüzde beşin altında paya sahip, görevsiz ortak tazmin kapsamındadır.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 84/4-c",
    f"{K}, tazmin kararı verilen yatırım kuruluşunun yönetim kurulu üyelerinin yüzde kaç veya daha fazla paya sahip olduğu "
    "şirketler tazmin edilmeyecekler arasında sayılmıştır?",
    "%25", ["%5", "%10", "%20", "%50"],
    "Kanun m. 84/4-c'ye göre (a) bendinde sayılan gerçek ve tüzel kişilerin (yönetim kurulu üyeleri, yöneticiler, yüzde beş "
    "ve üzeri ortaklar ve yakınları) yüzde yirmi beş veya daha fazla paya sahip olduğu şirketler tazmin edilmez.",
    zorluk="hard")

P.sayisal("6362 s. SPKn m. 84/4-a",
    f"{K}, tazmin kararı verilen bir yatırım kuruluşunda yüzde kaç veya daha fazla paya sahip ortaklar tazmin edilmez?",
    "%5", ["%1", "%10", "%20", "%25"],
    "Kanun m. 84/4-a'ya göre yatırım kuruluşunun yönetim kurulu üyeleri, yöneticileri ve şahsen sorumlu ortakları ile yüzde "
    "beş veya daha fazla paya sahip ortakları, denetim kurulu üyeleri, bunların eşleri ve ikinci dereceye kadar kan ve "
    "kayın hısımları tazmin edilmez.")

P.q("6362 s. SPKn m. 84/5",
    f"{K}, hak sahibi her bir yatırımcıya ödenecek azami tazmin tutarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Azami tutar, yatırımcının aynı kuruluştaki her bir hesabı için ayrı ayrı uygulanır.",
    ["Azami tutar her yıl ilan edilen yeniden değerleme katsayısı oranında artırılır.",
     "Kurulun teklifi üzerine Cumhurbaşkanı toplam tazmin tutarını beş katına kadar artırabilir.",
     "Azamiyi aşan tutarın başka bir yatırımcıya devri hâlinde devralana YTM ödeme yapmaz.",
     "Sınır, yatırımcının aynı kuruluştan olan taleplerinin tümünü kapsar."],
    "Kanun m. 84/5'e göre azami tazmin tutarı yeniden değerleme katsayısı oranında artırılır ve Cumhurbaşkanınca beş katına "
    "kadar artırılabilir. Sınır hesap sayısı, türü ve para birimine bakılmaksızın bir yatırımcının aynı kuruluştan olan "
    "taleplerinin tümünü kapsar; devredilen fazla tutar için devralana ödeme yapılmaz.")

P.sayisal("6362 s. SPKn m. 84/5",
    f"{K}, Kurulun teklifi üzerine Cumhurbaşkanı, hak sahibi yatırımcılara ödenecek toplam tazmin tutarını kaç katına kadar "
    "artırabilir?",
    "5", ["2", "3", "4", "10"],
    "Kanun m. 84/5'e göre azami tazmin tutarı her yıl yeniden değerleme katsayısı oranında artırılır; ayrıca Kurulun teklifi "
    "üzerine Cumhurbaşkanı toplam tazmin tutarını beş katına kadar artırabilir.", zorluk="easy")

P.q("6362 s. SPKn m. 84/3",
    "Tazmin kararı verilen bir aracı kurumun müşterisi hakkında piyasa dolandırıcılığı suçundan suç duyurusunda "
    f"bulunulmuştur. {K}, bu müşterinin tazmin talebine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Soruşturmanın başlamasından mahkeme kararının kesinleşmesine kadar ödemeler durur.",
    ["Talep, suç duyurusu yapıldığı için reddedilir.",
     "Ödeme yapılır; yatırımcı mahkûm olursa YTM ödenen tutarı kanuni faiziyle geri ister.",
     "Talebin tamamı suç duyurusundan bağımsız olarak karşılanır.",
     "Ödeme, Cumhuriyet başsavcılığının iznine bağlanır."],
    "Kanun m. 84/3'e göre m. 106 ve 107'deki suçlardan veya aklama suçundan mahkûm olan yatırımcıların talepleri, bu eylemlerle "
    "ilgili alacaklarla sınırlı olarak tazmin dışındadır; suç duyurusunda bulunulan kişilere ödemeler soruşturmanın "
    "başlamasından mahkeme kararının kesinleşmesine kadar durur.")

P.q("6362 s. SPKn m. 85",
    f"{K}, tazmin sürecine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Talep hakkı, tazmin kararının ilanından itibaren altı ay sonra zamanaşımına uğrar.",
    ["Yatırımcılar tazmin taleplerini YTM’ye yazılı olarak yaparlar.",
     "YTM, hak sahiplerini ve tutarları belirledikten sonra üç ay içinde ödemeleri yapar.",
     "Zorunlu hâllerde ödeme süresi Kurulun onayıyla en fazla üç ay daha uzatılabilir.",
     "YTM, yatırımcıların haklarına ödediği tazmin tutarı kadar halef olur."],
    "Kanun m. 85'e göre tazmin talepleri YTM'ye yazılı yapılır ve talep hakkı tazmin kararının ilanından itibaren bir yıl "
    "sonra zamanaşımına uğrar. YTM ödemeleri üç ay içinde yapar, süre Kurul onayıyla en fazla üç ay uzatılabilir; YTM ödediği "
    "tutar kadar yatırımcılara halef olur.")

P.sayisal("6362 s. SPKn m. 85/2",
    "YTM, tazmin kararı verilen bir aracı kurumun hak sahibi yatırımcılarını ve tazmin tutarlarını belirlemiştir. "
    f"{K}, zorunlu bir uzatma kararı bulunmadığında YTM ödemeleri bu tarihten itibaren en geç kaç ay içinde yapmalıdır?",
    "3", ["1", "2", "6", "12"],
    "Kanun m. 85/2'ye göre YTM, hak sahiplerini ve tazmin tutarlarını belirledikten sonra üç ay içinde ödemeleri "
    "gerçekleştirir; zorunlu hâllerde bu süre Kurulun onayıyla en fazla üç ay daha uzatılabilir.")

P.q("6362 s. SPKn m. 85/5",
    "Yatırımcıları YTM tarafından kısmen tazmin edilen bir aracı kurum yeniden yatırım hizmetleri vermek istemektedir. "
    f"{K}, bunun için aşağıdakilerden hangisi zorunludur?",
    "YTM’nin yaptığı tüm ödeme ve giderlerin anapara ve kanuni faiziyle ödenmesi",
    ["YTM’nin yaptığı ödemelerin anaparasının ödenmesi, faizin affedilmesi",
     "Aracı kurumun sermayesinin iki katına çıkarılması",
     "Yatırımcıların yazılı onayının alınması",
     "Tazmin sürecinin kapatılmasından itibaren beş yıl geçmesi"],
    "Kanun m. 85/5'e göre yatırımcıları kısmen veya tamamen tazmin edilenlerin yeniden yatırım hizmetleri ve faaliyetlerinde "
    "bulunabilmesi için, diğer şartlar saklı kalmak üzere, YTM'nin yaptığı tüm ödeme ve giderlerin anapara ve kanuni faiziyle "
    "ödenmesi zorunludur.")

P.q("6362 s. SPKn m. 85/4",
    "Kurulun tazmin kararı verdiği bir aracı kurumda tazmin süreci tamamlanmak üzeredir. "
    f"{K}, bu aşamaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurul, YTM’nin bildirimi üzerine tazmin sürecini kapatma kararı verir.",
    ["Tazmin süreci, YTM’nin son ödemeyi yapmasıyla Kurul kararı aranmaksızın sona erer.",
     "Tedricî tasfiye kararı verilmesi, tazmin sürecinin işleyişini durdurur.",
     "YTM, tazmin sürecinin sonuçlarını Hazine ve Maliye Bakanlığına sunar.",
     "Aracı kurumun iflası ancak tazmin süreci başlamadan istenebilir."],
    "Kanun m. 85/4'e göre Kurul, tazmin sürecinin tamamlanmasından sonra YTM'nin bildirimi üzerine süreci kapatma kararı "
    "verir; YTM sonuçları, tedrici tasfiye veya iflasın yararlı olup olmayacağına ilişkin önerisiyle Kurula sunar. Tedrici "
    "tasfiye veya iflas kararı tazmin sürecinin işleyişini engellemez.")

P.oncul("6362 s. SPKn m. 84/4",
    "Tazmin kararı verilen bir aracı kurumla ilişkili aşağıdaki kişiler YTM’ye başvurmuştur:",
    ["Aracı kurumun yönetim kurulu üyesinin kardeşi",
     "Aracı kurumun genel müdürünün kuzeni",
     "Aracı kurumun şahsen sorumlu ortağı adına hareket eden üçüncü kişi",
     "Aracı kurumla aynı grupta yer alan portföy yönetim şirketi"],
    f"{K}, yukarıdakilerden hangileri tazmin edilmez?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 84/4'e göre yönetim kurulu üyeleri, yöneticiler ve şahsen sorumlu ortaklar ile bunların eşleri ve ikinci "
    "dereceye kadar kan ve kayın hısımları, bu kişiler adına hareket eden üçüncü kişiler ve aynı gruptaki şirketler tazmin "
    "edilmez. Kardeş ikinci derece kan hısımıdır; kuzen dördüncü derece olduğundan kapsam dışında kalır.", zorluk="hard")

# ================================================================ tedrici tasfiye (m. 86)
P.q("6362 s. SPKn m. 86",
    f"{K}, tedricî tasfiyeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tedricî tasfiye işlemleri Kurulun atadığı tasfiye memurlarınca TTK hükümlerine göre yürütülür.",
    ["Kurul, bankalar hariç olmak üzere, tazmin sürecinin kapanmasına ilişkin kararıyla birlikte tedricî tasfiye kararı verebilir.",
     "Tedricî tasfiye kararından sonuçlanıncaya kadar kanuni organların görev ve yetkileri YTM tarafından yerine getirilir.",
     "Tedricî tasfiye kararı verilmesi hâlinde tasfiyenin kapatılmasına kadar iflas kararı verilemez.",
     "Tedricî tasfiye kararı verilenler hakkında evvelce başlamış icra takipleri durur."],
    "Kanun m. 86'ya göre tedricî tasfiye kararı bankalar hariç tazmin sürecinin kapanmasıyla birlikte verilebilir ve işlemler "
    "YTM tarafından yürütülür; TTK, İİK ve diğer mevzuatın tasfiye hükümleri uygulanmaz. Kanuni organların yetkileri YTM'ye "
    "geçer, tasfiye kapatılana kadar iflas kararı verilemez ve takipler durur.")

P.q("6362 s. SPKn m. 86/5",
    f"Tedricî tasfiyesine karar verilen bir aracı kurumun aktifleri paraya çevrilmiştir. {K}, elde edilen tutarın ödenmesinde "
    "izlenecek sıra aşağıdakilerden hangisinde doğru verilmiştir?",
    "Müşteri alacakları – kamu alacakları – YTM’nin ödemeleri ve tasfiye giderleri – diğer alacaklar",
    ["Kamu alacakları – müşteri alacakları – YTM’nin ödemeleri ve tasfiye giderleri – diğer alacaklar",
     "YTM’nin ödemeleri ve tasfiye giderleri – müşteri alacakları – kamu alacakları – diğer alacaklar",
     "Müşteri alacakları – YTM’nin ödemeleri ve tasfiye giderleri – kamu alacakları – diğer alacaklar",
     "Müşteri alacakları ile kamu alacakları garameten – YTM’nin ödemeleri – diğer alacaklar"],
    "Kanun m. 86/5'e göre aktiflerden öncelikle müşteri alacakları ödenir, tamamı karşılanamazsa garameten ödeme yapılır; "
    "artan kısımdan öncelikle garameten kamu alacakları, kalandan YTM'nin m. 85 kapsamındaki ödemeleri ve tasfiye giderleri "
    "karşılanır; bakiye diğer alacaklılara tahsis edilir.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 86/7",
    "YTM, tedricî tasfiyesine karar verilen bir aracı kurumun yönetim ve denetimini elinde bulunduran ortaklarından mal "
    f"beyannamesi vermelerini istemiştir. {K}, istenen mal beyannamesi en geç kaç gün içinde YTM’ye verilmelidir?",
    "7", ["3", "10", "15", "30"],
    "Kanun m. 86/7'ye göre YTM'nin istediği mal beyannamesinin en geç yedi gün içinde verilmesi zorunludur; beyan, tedrici "
    "tasfiye kararının ilanından önceki iki yıl içindeki devir ve iktisapları da kapsar.")

P.sayisal("6362 s. SPKn m. 86/7",
    "YTM, tedricî tasfiye kapsamında hâkim ortakların malvarlıkları üzerine ihtiyati haciz kararı aldırmıştır. "
    f"{K}, bu karardan itibaren kaç ay içinde dava açılmaması veya takipte bulunulmaması hâlinde karar kendiliğinden kalkar?",
    "6", ["1", "3", "12", "24"],
    "Kanun m. 86/7'ye göre YTM'nin talebiyle alınan tedbir ve haciz kararlarından itibaren altı ay içinde dava açılmaması veya "
    "icra ya da iflas takibinde bulunulmaması hâlinde bu kararlar kendiliğinden ortadan kalkar.", zorluk="hard")

P.q("6362 s. SPKn m. 86/8, 86/10",
    "Tedricî tasfiyesi yürütülen bir aracı kurumun aktiflerinin, müşteri alacaklarını, tazmin ödemelerini ve tasfiye "
    f"giderlerini karşılamaya yetmediği tespit edilmiştir. {K}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "YTM, Kurulun uygun görüşüyle aracı kurumun iflasını isteyebilir.",
    ["Tedricî tasfiye, Kurul kararı aranmaksızın iflas tasfiyesine dönüşür.",
     "Eksik kalan tutar Kurul bütçesinden karşılanır.",
     "Müşteri alacakları Hazine garantisiyle ödenir.",
     "Aracı kurumun ortakları eksik tutarı eşit olarak öder."],
    "Kanun m. 86/8'e göre aktiflerin hak sahiplerinin alacaklarını, tazmin ödemelerini ve tasfiye giderlerini karşılamaya "
    "yetmediğinin tespiti hâlinde YTM, Kurulun uygun görüşüyle ilgililerin iflasını isteyebilir; m. 86/10'a göre YTM aciz "
    "vesikası aranmaksızın iptal davası açabilir.")

# ================================================================ kripto varlıklar: saklama ve haciz (m. 35/C, 99/B)
P.q("6362 s. SPKn m. 35/C-4, 6, 7",
    f"{K}, kripto varlık platformlarında müşteri varlıklarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Platformun temerrüdünde müşterilerin kripto varlıkları YTM tarafından tazmin edilir.",
    ["Müşterilere ait kripto varlıkların müşterilerin kendi cüzdanlarında bulundurulması esastır.",
     "Müşterilere ait nakitlerin bankalarda tutulması zorunludur.",
     "Bankalar nezdinde saklanan kripto varlıklar mevduat sigortası kapsamında değildir.",
     "Müşteri nakit ve kripto varlıkları hizmet sağlayıcının malvarlığından ayrıdır."],
    "Kanun m. 35/C-4'e göre kripto varlıklar m. 82'deki yatırımcı tazmin hükümlerine tabi değildir. m. 35/C-6 müşteri "
    "varlıklarının kendi cüzdanlarında bulundurulmasını esas alır, nakitlerin bankalarda tutulmasını zorunlu kılar ve bankada "
    "saklanan varlıkları mevduat sigortası dışında tutar; m. 35/C-7 malvarlığı ayrılığını düzenler.")

P.q("6362 s. SPKn m. 99/B-7",
    "Bir icra dairesi, kripto varlık platformunda hesabı bulunan bir borçlunun kripto varlıklarına haciz koymak istemektedir. "
    f"{K}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Haciz talebi münhasıran kripto varlık hizmet sağlayıcısı tarafından yerine getirilir.",
    ["Haciz talebi MKK aracılığıyla yerine getirilir.",
     "Kripto varlıklar haczedilemez, borçlunun nakdi haczedilebilir.",
     "Haciz ancak Kurulun onayıyla uygulanabilir.",
     "Haciz talebi, platformun müşteri nakitlerini tuttuğu bankaya yöneltilir ve banka tarafından uygulanır."],
    "Kanun m. 99/B-7'ye göre müşterilere ait nakit ve kripto varlıklara ilişkin tedbir, haciz ve benzeri talepler münhasıran "
    "kripto varlık hizmet sağlayıcıları tarafından yerine getirilir; İİK m. 78 elektronik haciz hükümleri uygulanır ve el "
    "konulan varlıklar yetkili saklama kuruluşlarının cüzdanlarında muhafaza edilir.")

P.oncul("6362 s. SPKn m. 35/C-6, 7",
    "Kripto varlık hizmet sağlayıcıları nezdindeki müşteri varlıklarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Müşterilerin kendi cüzdanlarında bulundurmayı tercih etmediği kripto varlıklar yetkilendirilmiş kuruluşlarca saklanır.",
     "Müşteri nakitleri hizmet sağlayıcının kendi kasasında tutulabilir.",
     "Müşteri varlıkları hizmet sağlayıcının borçları nedeniyle kamu alacakları için olsa dahi haczedilemez.",
     "Hizmet sağlayıcının malvarlığı müşterilerin borçları nedeniyle haczedilebilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve III", ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 35/C-6'ya göre müşterinin cüzdanında tutmadığı kripto varlıklar BDDK'nın uygun gördüğü bankalar veya Kurulca "
    "yetkilendirilmiş kuruluşlarca saklanır, nakitlerin bankalarda tutulması zorunludur. m. 35/C-7'ye göre müşteri "
    "varlıkları hizmet sağlayıcının, hizmet sağlayıcının malvarlığı da müşterilerin borçları nedeniyle haczedilemez.")

P.q("6362 s. SPKn m. 13, 46, 81",
    "Bir yatırımcının aracı kurumu, müşterinin talimatı olmadan müşteriye ait payları başka bir müşterinin kredili işlemine "
    f"teminat olarak kullanmıştır. {K}, bu işleme ilişkin aşağıdakilerden hangisi doğrudur?",
    "İşlem, yazılı açık izin olmadan tevdi amacı dışında kullanım olduğundan mevzuata aykırıdır.",
    ["Kaydi paylar aracı kurumun malvarlığına dâhil olduğundan işlem geçerlidir.",
     "Kredili işlemin teminatı olarak kullanıldığından işlem, YTM’nin sonradan vereceği onayla geçerlilik kazanır.",
     "İşlem, MKK’ya bildirildiği tarihten itibaren hukuka uygun hâle gelir.",
     "İşlem, müşteriye sonradan bilgi verilirse mevzuata uygundur."],
    "Kanun m. 46/5'e göre yatırımcıların yatırım kuruluşları nezdindeki nakit ve araçları kuruluşun malvarlığından ayrı izlenir "
    "ve yatırımcının yazılı açık izni olmadan tevdi amacı dışında kendilerine veya üçüncü kişilere menfaat sağlayacak şekilde "
    "kullanılamaz. Fiil ayrıca m. 110/1-a kapsamında güveni kötüye kullanma oluşturabilir.")

P.q("6362 s. SPKn m. 81/2, 81/6",
    f"{K}, Merkezî Kayıt Kuruluşunun düzenlenmesine ve gözetimine ilişkin aşağıdakilerden hangisi doğrudur?",
    "MKK’nın faaliyet ve denetim esasları Kurulca çıkarılacak yönetmelikle düzenlenir.",
    ["MKK, kamu tüzel kişiliğine sahip bir kurum olarak doğrudan Cumhurbaşkanlığına bağlıdır.",
     "MKK’nın gözetim ve denetim mercii Hazine ve Maliye Bakanlığıdır.",
     "MKK’nın çalışma esasları kendi genel kurulunca kabul edilen iç tüzükle belirlenir.",
     "MKK’nın gelir ve kâr payı dağıtım esaslarını Borsa İstanbul belirler."],
    "Kanun m. 81'e göre MKK özel hukuk tüzel kişiliğini haiz bir anonim şirkettir; kuruluş, faaliyet, üyelik, çalışma ve "
    "denetim esasları, gelirleri ve kâr payı dağıtım esasları Kurulca çıkarılacak yönetmelikle düzenlenir. Kurul, MKK'nın "
    "gözetim ve denetim merciidir.")

P.q("6362 s. SPKn m. 77/1, 80/1",
    f"{K}, merkezî takas kuruluşları ile merkezî saklama kuruluşlarının kuruluş izinlerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Takas kuruluşunda Kurulun teklifi, saklama kuruluşunda Kurulun uygun görüşü üzerine ilgili Bakan izin verir.",
    ["Her ikisinin kuruluşuna da Kurulun teklifi üzerine Cumhurbaşkanı izin verir.",
     "Her ikisinin kuruluşuna da Kurul izin verir, faaliyete geçmeleri Bakanlık iznine tabidir.",
     "Takas kuruluşunun kuruluşuna TCMB, saklama kuruluşunun kuruluşuna Kurul izin verir.",
     "Her ikisinin kuruluşu ticaret siciline tescille tamamlanır, ayrıca izin aranmaz."],
    "Kanun m. 77/1'e göre merkezî takas kuruluşlarının kuruluşuna Kurulun teklifi üzerine, m. 80/1'e göre merkezî saklama "
    "kuruluşlarının kuruluşuna Kurulun uygun görüşü üzerine ilgili Bakan izin verir; her ikisinin faaliyete geçmesi Kurul "
    "iznine tabidir. Borsalarda ise izin Cumhurbaşkanınca verilir.", zorluk="hard")

P.q("6362 s. SPKn m. 82/1",
    "Kurul, bir aracı kurumun sermaye piyasası faaliyetinden kaynaklanan araç teslim yükümlülüklerini yerine getiremediğini "
    f"tespit etmiştir. {K}, yatırımcıları tazmin kararının alınmasına ilişkin süre aşağıdakilerden hangisidir?",
    "Durumun tespitinden itibaren üç ay içinde",
    ["Durumun tespitinden itibaren bir ay içinde",
     "Durumun tespitinden itibaren altı ay içinde",
     "YTM’nin başvurusundan itibaren üç ay içinde",
     "Aracı kurumun iflasının açılmasından itibaren bir yıl içinde"],
    "Kanun m. 82/1'e göre Kurul, yatırım kuruluşlarının nakit ödeme veya araç teslim yükümlülüklerini yerine getiremediğinin "
    "veya kısa sürede getiremeyeceğinin tespitinde yatırımcıları tazmin kararı alır; bu karar durumun tespitinden itibaren "
    "üç ay içinde alınır. Kurulun diğer tedbir yetkileri saklıdır.")

P.q("6362 s. SPKn m. 86/9",
    "Tedricî tasfiyesi YTM tarafından yürütülen bir aracı kurumun bir alacaklısı, tasfiye işlemleri nedeniyle zarara "
    f"uğradığını ileri sürerek tazminat davası açmak istemektedir. {K}, bu dava kime karşı açılır?",
    "Görevin ifası nedeniyle doğrudan YTM aleyhine",
    ["YTM’nin kanuni temsilcisi aleyhine şahsen",
     "Tasfiye işlemlerini yürüten YTM personeli aleyhine",
     "Sermaye Piyasası Kurulu ve Hazine aleyhine birlikte",
     "Tasfiye edilen aracı kurumun eski yönetim kurulu aleyhine"],
    "Kanun m. 86/9'a göre tedricî tasfiye sırasındaki görevlerinin ifası sebebiyle YTM kanuni temsilcisi, yönetici ve "
    "personeli aleyhine açılacak her türlü tazminat ve alacak davaları YTM aleyhine açılır; YTM'nin ağır ihmali veya kastı "
    "bulunan personeline rücu hakkı saklıdır.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
