# -*- coding: utf-8 -*-
"""SPK Mevzuatı · Sermaye Piyasası Araçları — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · 6362 s. Sermaye Piyasası Kanunu m. 3, 12, 16, 31, 31/A, 31/B, 35/A, 35/B, 35/C, 57-61/B, 74/1, 99/A-2, 99/B, 130/5
    (7222 s. Kanunla 2020 ve 7518 s. Kanunla 2024 değişiklikleri işlenmiş)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_sermaye_piyasasi_araclari_2026.json", lesson="sermaye_piyasasi_ve_finans",
          topic="sermaye_piyasasi_araclari", konu_adi="Sermaye Piyasası Araçları", seed=2026092824,
          surum="6362 s. Sermaye Piyasası Kanunu (7222 s. 2020 ve 7518 s. 2024 değişiklikleri dahil); 28.09.2026 kontrolü")

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"

# ================================================================ temel tanımlar (m. 3, 16)
P.q("6362 s. SPKn m. 3/o",
    "Bir yatırımcının portföyünde aşağıdaki kıymetler bulunmaktadır. "
    f"{K}, bunlardan hangisi menkul kıymet sayılmaz?",
    "Bir şirketin ödeme aracı olarak keşide ettiği çek",
    ["Borsada işlem gören bir anonim ortaklığın payı",
     "Bir bankanın ihraç ettiği tahvil",
     "Yabancı bir şirketin paylarını temsil eden depo sertifikası",
     "Menkul kıymetleştirilmiş varlıklara dayalı borçlanma aracı"],
    "Kanun m. 3/o'ya göre menkul kıymetler; para, çek, poliçe ve bono hariç olmak üzere paylar, pay benzeri kıymetler ve "
    "bunlara ilişkin depo sertifikaları ile borçlanma araçları veya menkul kıymetleştirilmiş varlık ve gelirlere dayalı "
    "borçlanma araçları ve bunlara ilişkin depo sertifikalarıdır.", zorluk="easy")

P.q("6362 s. SPKn m. 3/ş",
    f"{K}, “sermaye piyasası araçları” tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Menkul kıymetleri, türev araçları, yatırım sözleşmelerini ve Kurulca belirlenenleri kapsar.",
    ["Borsada işlem gören menkul kıymetlerle sınırlıdır.",
     "Menkul kıymetleri kapsar, türev araçlar ayrı bir kategori olarak tanımın dışındadır.",
     "Para, çek, poliçe ve bono gibi kambiyo senetlerini de kapsar.",
     "Kurulun onayladığı izahnameye veya ihraç belgesine konu olan ve borsada işlem gören araçlarla sınırlıdır."],
    "Kanun m. 3/ş'ye göre sermaye piyasası araçları, menkul kıymetler ve türev araçlar ile yatırım sözleşmeleri de dâhil olmak "
    "üzere Kurulca bu kapsamda olduğu belirlenen diğer sermaye piyasası araçlarıdır; kambiyo senetleri menkul kıymet sayılmaz.")

P.q("6362 s. SPKn m. 3/u",
    f"{K}, aşağıdakilerden hangisi türev araç tanımı kapsamında değildir?",
    "Getirisi ihraç anında sabit faizle belirlenmiş bir devlet tahvili",
    ["Menkul kıymetleri satın alma hakkı veren araçlar",
     "Değeri faiz oranındaki değişikliğe bağlı olan araçlar",
     "İklim değişkenlerinden oluşan bir endekse bağlı araçlar",
     "Döviz üzerine yapılan kaldıraçlı işlemler"],
    "Kanun m. 3/u'ya göre menkul kıymetleri alma, satma veya değiştirme hakkı veren araçlar; değeri menkul kıymet, döviz, faiz, "
    "kıymetli maden, mal, istatistik, kredi riski, enerji fiyatı ve iklim değişkenleri gibi dayanaklara bağlı araçlar ile döviz "
    "ve kıymetli madenler üzerine kaldıraçlı işlemler türev araçtır. Sabit getirili tahvil bir borçlanma aracıdır.")

P.q("6362 s. SPKn m. 3/i",
    f"{K}, aşağıdakilerden hangisi “ipotekli sermaye piyasası aracı” tanımı kapsamında sayılmaz?",
    "Varlık kiralama şirketinin ihraç ettiği kira sertifikası",
    ["İpotek teminatlı menkul kıymet",
     "İpoteğe dayalı menkul kıymet",
     "İpotek finansmanı kuruluşunun ihraç ettiği pay dışındaki sermaye piyasası aracı",
     "Konut finansmanından kaynaklanan alacakların teminatı altında ihraç edilen araç"],
    "Kanun m. 3/i'ye göre ipotekli sermaye piyasası araçları; ipotek teminatlı ve ipoteğe dayalı menkul kıymetler, ipotek "
    "finansmanı kuruluşlarının ihraç ettiği pay dışındaki araçlar ile konut finansmanından kaynaklanan alacaklara dayalı veya "
    "bunların teminatı altında ihraç edilen diğer araçlardır. Kira sertifikası m. 61'de ayrıca düzenlenir.")

P.oncul("6362 s. SPKn m. 3",
    "Kanunda yer alan bazı tanımlar aşağıda eşleştirilmiştir:",
    ["Başlangıç sermayesi – Kayıtlı sermayeli anonim ortaklıkların sahip olması zorunlu asgari çıkarılmış sermaye",
     "Çıkarılmış sermaye – Kayıtlı sermayeli anonim ortaklıkların satışı yapılmış paylarını temsil eden sermaye",
     "Kayıtlı sermaye – Yönetim kurulu kararıyla pay çıkarılabilecek, sicilde tescil ve ilan edilmiş azami miktar",
     "Halka arz eden – Sermaye piyasası araçlarını ihraç eden veya ihraç için Kurula başvuran tüzel kişi"],
    f"{K}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, II ve III", ["I ve II", "II ve IV", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 3/b, d ve l'deki tanımlar ilk üç eşleştirmeyle uyumludur. m. 3/g'ye göre halka arz eden, sahip olduğu araçları "
    "halka arz etmek üzere Kurula başvuran gerçek veya tüzel kişidir; araçları ihraç eden veya başvuran tüzel kişi m. 3/h'deki "
    "ihraççı tanımıdır.")

P.q("6362 s. SPKn m. 3/f-h",
    "Halka açık olmayan bir anonim ortaklığın gerçek kişi ortağı, sahip olduğu payların bir kısmını halka satmak üzere Kurula "
    f"başvurmuş; ortaklık ise aynı anda sermaye artırımıyla yeni pay çıkaracaktır. {K}, bu işlemde tarafların sıfatlarına "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ortak halka arz eden, ortaklık ihraççı sıfatını taşır.",
    ["Ortak ihraççı, ortaklık halka arz eden sıfatını taşır.",
     "Her ikisi de ihraççı sıfatını taşır.",
     "Her ikisi de halka arz eden sıfatını taşır.",
     "Gerçek kişiler ihraççı veya halka arz eden sıfatını taşıyamaz."],
    "Kanun m. 3/g'ye göre halka arz eden, sahip olduğu araçları halka arz etmek üzere Kurula başvuran gerçek veya tüzel kişidir; "
    "m. 3/h'ye göre ihraççı, araçları ihraç eden veya ihraç için başvuran tüzel kişidir. Mevcut paylarını satan ortak halka "
    "arz eden, yeni pay çıkaran ortaklık ihraççıdır.")

P.sayisal("6362 s. SPKn m. 16/1",
    "Payları borsada işlem görmeyen ve kitle fonlaması yoluyla para toplamamış bir anonim ortaklığın pay sahibi sayısı "
    f"zamanla artmıştır. {K}, pay sahibi sayısı kaçı aştığında bu ortaklığın payları halka arz olunmuş sayılır?",
    "500", ["100", "250", "1.000", "5.000"],
    "Kanun m. 16/1'e göre payları borsada işlem gören ortaklıklar ile kitle fonlaması yoluyla para toplayanlar hariç, pay sahibi "
    "sayısı beş yüzü aşan anonim ortaklıkların payları halka arz olunmuş sayılır ve bu ortaklıklar halka açık ortaklık "
    "hükümlerine tabi olur.", zorluk="easy")

P.q("6362 s. SPKn m. 3/e, 16/1",
    "Bir girişim şirketi, Kurulca izin verilmiş bir kitle fonlama platformu aracılığıyla paya dayalı fon toplamış ve pay "
    f"sahibi sayısı 1.200’e ulaşmıştır. {K}, bu şirketin statüsüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kitle fonlaması yoluyla para topladığı için halka açık ortaklık sayılmaz.",
    ["Pay sahibi sayısı beş yüzü aştığı için halka açık ortaklık sayılır.",
     "İki yıl içinde paylarının borsada işlem görmesi için başvurmakla yükümlüdür.",
     "Kurulun kararıyla halka açık ortaklık statüsünden çıkarılıncaya kadar halka açık sayılır.",
     "Pay sahibi sayısı bin kişiyi aştığı için izahname hazırlamakla yükümlüdür."],
    "Kanun m. 3/e ve m. 16/1'e göre kitle fonlaması platformları aracılığıyla para toplayan ortaklıklar, pay sahibi sayısı beş "
    "yüzü aşsa da halka açık ortaklık sayılmaz; m. 4/1 kitle fonlamasını izahname yükümlülüğü dışında tutar.")

# ================================================================ borçlanma araçları (m. 31, 31/A, 31/B)
P.q("6362 s. SPKn m. 31",
    f"{K}, borçlanma aracı niteliğindeki sermaye piyasası araçlarının ihracına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Borçlanma aracı ihraç yetkisi yönetim kuruluna ancak süreli olarak devredilebilir.",
    ["İhraç edilebilecek toplam tutar Kurulca belirlenecek limiti geçemez.",
     "Kurul, ihracın ve ihraççının niteliğine göre farklı limitler belirleyebilir.",
     "Belediye ve il özel idareleri için kendi kanunlarındaki limitler saklıdır.",
     "Ödeme yapılmaması hâlinde MKK’nın düzenlediği belge İİK m. 68’deki belgelerden sayılır."],
    "Kanun m. 31/1-2'ye göre ihraç tutarı Kurulca belirlenen limiti geçemez ve farklı limitler belirlenebilir; diğer "
    "kanunlardaki limitler (233 s. KHK ile belediye ve il özel idaresi limitleri hariç) uygulanmaz. m. 31/3'e göre ihraç "
    "yetkisi esas sözleşmeyle yönetim kuruluna süreli veya süresiz devredilebilir; m. 31/4 MKK belgesini düzenler.")

P.q("6362 s. SPKn m. 31/A",
    f"{K}, borçlanma aracı sahipleri kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurulun toplantıya çağrılma esasları, ihraççının esas sözleşmesinde belirlenir.",
    ["İhraççının tedavüldeki borçlanma araçlarının sahipleri borçlanma aracı sahipleri kurulunu oluşturur.",
     "Her bir tertip borçlanma aracının sahipleri ayrı bir kurul oluşturabilir.",
     "Borçlanma aracı sahiplerini temsil etmek üzere temsilci atanabilir.",
     "Nitelikli çoğunlukla alınan kararlar olumlu oy vermeyenler için de hüküm ifade eder."],
    "Kanun m. 31/A'ya göre tedavüldeki borçlanma araçlarının sahipleri kurulu oluşturur, her tertip ayrı kurul oluşturabilir, "
    "temsilci atanabilir ve nitelikli çoğunlukla alınan kararlar olumlu oy vermeyenleri de bağlar. Toplantıya çağrı ve karar "
    "esaslarının izahname ve/veya ihraç belgesinde belirlenmesi zorunludur.")

P.sayisal("6362 s. SPKn m. 31/A-3",
    "Bir ihraççının tek tertip tahvillerinin hüküm ve şartlarının değiştirilmesi borçlanma aracı sahipleri kurulunda "
    f"görüşülecektir. {K}, izahnamede daha ağır bir nisap öngörülmemişse karar için bu tertibin nominal bedeller toplamının "
    "asgari yüzde kaçını temsil eden sahiplerin olumlu oyu gerekir?",
    "%50", ["%25", "%33", "%67", "%75"],
    "Kanun m. 31/A-3'e göre Kurulca veya izahname ve/veya ihraç belgesinde daha ağır nisap öngörülmedikçe, her bir tertip için "
    "nominal bedeller toplamının asgari yarısını temsil eden borçlanma aracı sahiplerinin olumlu oyu şarttır.", zorluk="hard")

P.q("6362 s. SPKn m. 31/A-5",
    "Bir ihraççı tahvillerinin anapara ödemesinde temerrüde düşmüş, ardından borçlanma aracı sahipleri kurulu vade ve faiz "
    f"koşullarının değiştirilmesine karar vermiştir. {K}, bu değişikliğin sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Başlatılmış takipler devam eder; ancak yeni takip başlatılamaz.",
    ["Temerrüt nedeniyle başlatılmış tüm takipler durur.",
     "İhtiyati tedbir ve ihtiyati haciz kararları uygulanmaz.",
     "Bir takip muamelesiyle kesilebilen zamanaşımı ve hak düşürücü süreler işlemez.",
     "Borçlanma aracından doğan tüm borçlar ifa edildikten sonra duran takipler düşer."],
    "Kanun m. 31/A-5'e göre temerrütten sonra hüküm ve şartların değiştirilmesi hâlinde başlatılmış tüm takipler değişiklik "
    "tarihi itibarıyla durur, ihtiyati tedbir ve haciz kararları uygulanmaz, zamanaşımı ve hak düşürücü süreler işlemez; "
    "borçlar ifa edilince duran takipler düşer.", zorluk="hard")

P.q("6362 s. SPKn m. 31/A-1",
    "Bir ihraççının tedavülde farklı vadelerde üç tertip tahvili bulunmaktadır. Yalnız ikinci tertibin sahiplerini ilgilendiren "
    f"bir değişiklik görüşülecektir. {K}, bu görüşmeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "İkinci tertibin sahipleri ayrı bir borçlanma aracı sahipleri kurulu oluşturabilir.",
    ["Değişiklik, üç tertibin sahiplerinin birlikte oluşturduğu kurulda görüşülmek zorunluluğundadır.",
     "Değişiklik borçlanma aracı sahipleri kurulunda değil ihraççının genel kurulunda görüşülür.",
     "Değişiklik için tertip sahiplerinin oybirliği aranır.",
     "Değişiklik sadece Kurulun kararıyla yapılabilir."],
    "Kanun m. 31/A-1'e göre ihraççının tedavüldeki borçlanma araçlarının sahipleri borçlanma aracı sahipleri kurulunu oluşturur; "
    "her bir tertip borçlanma aracı sahipleri de ayrı bir kurul oluşturabilir. Karar nisabı m. 31/A-3'te düzenlenmiştir.")

P.q("6362 s. SPKn m. 31/B-1",
    "Bir ihraççı, tahvillerinin teminatı olarak bir gayrimenkulünün mülkiyetini teminat yöneticisine devretmek istemektedir. "
    f"{K}, teminat yöneticisi olarak atanabilecek kuruluş aşağıdakilerden hangisidir?",
    "Genel saklama yetkisi bulunan yatırım kuruluşu",
    ["Emir iletimine aracılık yetkisi bulunan dar yetkili aracı kurum",
     "Kurulca listeye alınmış bağımsız denetim kuruluşu",
     "Yatırım fonu kurma yetkisine sahip portföy yönetim şirketi",
     "Gayrimenkul değerleme uzmanlığı lisansına sahip değerleme kuruluşu"],
    "Kanun m. 31/B-1'e göre teminata konu varlıkların mülkiyeti teminaten genel saklama yetkisine sahip yatırım kuruluşu "
    "niteliğini haiz teminat yöneticisine devredilir veya bu varlıklar üzerinde teminat yöneticisi lehine sınırlı ayni hak "
    "tesis edilir; devir ilgili sicilde beyanlar hanesine kaydedilir.")

P.sayisal("6362 s. SPKn m. 31/B-10",
    "Bir teminat yöneticisi, tahvil sahipleri lehine teminaten mülkiyeti kendisine devredilen varlıkları kendi borcu için "
    f"kullanmıştır. {K}, bu fiil nedeniyle güveni kötüye kullanma suçundan hükmolunacak ceza kaç yıldan az olamaz?",
    "5", ["1", "2", "3", "8"],
    "Kanun m. 31/B-10'a göre teminat yöneticisinin teminaten mülkiyeti devredilen varlıkları tasarruf amacı dışında kullanması "
    "durumunda TCK m. 155/2'ye göre hükmolunacak ceza beş yıldan az olamaz.", zorluk="hard")

P.oncul("6362 s. SPKn m. 31/B",
    "Teminat yönetim sözleşmesine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Sözleşme, ihraçtan önce ihraççı ile teminat yöneticisi arasında yazılı olarak akdedilir.",
     "Teminat yöneticisinin sorumluluğunu hafifleten anlaşmalar geçerlidir.",
     "Teminata konu varlığın teminaten devredildiği ilgili sicilde beyanlar hanesine kaydedilir.",
     "Teminat yöneticisinin unvanı ve yetkileri ihraççının merkezinin bulunduğu yerin ticaret siciline tescil edilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 31/B-2'ye göre teminat yönetim sözleşmesi ihraçtan önce yazılı akdedilir; m. 31/B-1'e göre devir sicilde "
    "beyanlar hanesine kaydedilir; m. 31/B-4 teminat yöneticisinin unvanı ve yetkilerinin tescil ve ilanını ihraççıya yükler. "
    "m. 31/B-8'e göre sorumluluğu hafifleten veya kaldıran anlaşmalar geçersizdir.")

P.q("6362 s. SPKn m. 31/B-6",
    "Tahvil sahipleri lehine teminat yöneticisine mülkiyeti devredilen varlıklar bulunduğu sırada teminat yöneticisi hakkında "
    f"iflas kararı verilmiştir. {K}, bu varlıklara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Varlıklar teminat yöneticisinin iflas masasına dâhil edilemez.",
    ["Varlıklar iflas masasına girer, tahvil sahipleri imtiyazlı alacaklı olur.",
     "Varlıklar kamu alacakları için haczedilebilir, özel alacaklar için haczedilemez.",
     "Varlıklar iflas idaresince paraya çevrilip garameten dağıtılır.",
     "Varlıkların iflas masasından ayrılması için tahvil sahiplerinin dava açması gerekir."],
    "Kanun m. 31/B-6'ya göre teminat konusu varlıklar teminat yöneticisinin mal varlığından ayrıdır ve ayrı izlenir; teminat "
    "yöneticisinin borçları nedeniyle kamu alacakları için olsa dahi haczedilemez, rehnedilemez, iflas masasına dâhil "
    "edilemez ve üzerlerine ihtiyati tedbir ve haciz konulamaz.")

# ================================================================ kira sertifikası, gayrimenkul sertifikası, proje finansmanı (m. 61-61/B)
P.q("6362 s. SPKn m. 61",
    f"{K}, varlık kiralama şirketlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Varlık kiralama şirketleri varlığa dayalı menkul kıymet de ihraç edebilir.",
    ["Varlık kiralama şirketleri münhasıran kira sertifikası ihraç etmek üzere kurulur.",
     "Esas sözleşmesinde belirtilen faaliyetler dışında ticari faaliyette bulunamaz.",
     "Portföyündeki varlıklar kira sertifikaları itfa edilinceye kadar haczedilemez.",
     "Anonim ortaklık şeklinde kurulur."],
    "Kanun m. 61/2-3'e göre varlık kiralama şirketleri münhasıran kira sertifikası ihraç etmek üzere kurulan anonim "
    "ortaklıklardır; esas sözleşmedeki faaliyetler dışında ticari faaliyette bulunamaz. Portföydeki varlıklar sertifikalar "
    "itfa edilinceye kadar haczedilemez ve iflas masasına girmez.")

P.q("6362 s. SPKn m. 61/4",
    "Bir varlık kiralama şirketi, ihraç ettiği kira sertifikalarının kira ödemesini vadesinde yapamamıştır. "
    f"{K}, bu durumda portföydeki varlıklardan elde edilen gelirin kullanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gelir öncelikle kira sertifikası sahiplerine yapılacak ödemelerde kullanılır.",
    ["Gelir öncelikle kamu alacaklarının ödenmesinde kullanılır.",
     "Gelir, şirketin tüm alacaklıları arasında garameten paylaştırılır.",
     "Gelir, önce fon kullanıcısının borçlarının ödenmesinde, kalanı sertifika sahiplerine kullanılır.",
     "Gelir, Yatırımcı Tazmin Merkezine devredilerek tazminde kullanılır."],
    "Kanun m. 61/4'e göre ihraççının kira sertifikalarından doğan yükümlülüklerini vadesinde yerine getirememesi, yönetiminin "
    "kamuya devri, faaliyet izninin kaldırılması veya iflası hâlinde portföydeki varlıklardan elde edilen gelir öncelikle "
    "kira sertifikası sahiplerine yapılacak ödemelerde kullanılır; Kurul gerekli tedbirleri alabilir.")

P.q("6362 s. SPKn m. 61/A",
    "Bir inşaat şirketi, yapımına başlanacak konut projesinin finansmanı için, projedeki belirli bağımsız bölümlerin alan "
    f"birimlerini temsil eden ve nominal değeri eşit araçlar ihraç etmek istemektedir. {K}, bu araç aşağıdakilerden hangisidir?",
    "Gayrimenkul sertifikası",
    ["Kira sertifikası", "Projeye dayalı menkul kıymet", "İpotek teminatlı menkul kıymet", "Gayrimenkul yatırım fonu katılma payı"],
    "Kanun m. 61/A'ya göre gayrimenkul sertifikası, ihraççıların inşa edilecek veya edilmekte olan gayrimenkul projelerinin "
    "finansmanında kullanılmak üzere ihraç ettikleri, projenin belirli bağımsız bölümlerini veya bağımsız bölümlerin belirli "
    "bir alan birimini temsil eden nominal değeri eşit sermaye piyasası aracıdır.", zorluk="easy")

P.oncul("6362 s. SPKn m. 61/A",
    "Gayrimenkul sertifikalarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Sertifika ihracıyla elde edilen fon, sertifikalar itfa edilinceye kadar haczedilemez.",
     "Vadede edimler yerine getirilemezse sertifika sahipleri toplantısı yapılır.",
     "Sahipler toplantısında Kurulca belirlenmeyen konularda TTK’nın genel kurul hükümleri uygulanır.",
     "Sertifikaya konu bağımsız bölümler ihraççının borçları için rehnedilebilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III", ["I ve IV", "II ve III", "II ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 61/A-2'ye göre ihraçla elde edilen fon ve sertifikaya konu bağımsız bölümler, ihraççının yönetimi kamuya devredilse "
    "dahi amacı dışında tasarruf edilemez, rehnedilemez, teminat gösterilemez ve haczedilemez. m. 61/A-3'e göre vadede edimler "
    "yerine getirilemezse sahipler toplantısı yapılır ve TTK'nın genel kurul hükümleri tamamlayıcı olarak uygulanır.")

P.q("6362 s. SPKn m. 61/B",
    f"{K}, proje finansman fonlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Proje finansman fonları portföy yönetim şirketleri tarafından kurulur ve tüzel kişiliğe sahiptir.",
    ["Proje finansmanına konu projenin gelirleri ve diğer hakları fona temlik edilir.",
     "Fon, sicil işlemleriyle sınırlı olarak tüzel kişiliği haiz addolunur.",
     "Fon adına sicil işlemleri kurucu ile fon kurulunu temsil eden birer yetkilinin müşterek imzasıyla yapılır.",
     "Fon portföyündeki varlıklar projeye dayalı menkul kıymet itfa edilinceye kadar haczedilemez."],
    "Kanun m. 61/B'ye göre proje finansman fonu, yatırım kuruluşları tarafından inançlı mülkiyet esaslarına göre fon iç tüzüğü "
    "ile kurulan ve tüzel kişiliği olmayan mal varlığıdır; sicil işlemleriyle sınırlı olarak tüzel kişi addolunur. Proje "
    "gelirleri fona temlik edilir, işlemler müşterek imzayla yapılır ve varlıklar haczedilemez.")

P.q("6362 s. SPKn m. 61/B-1",
    f"{K}, aşağıdaki yatırımlardan hangisi Kanundaki proje finansmanı tanımına en uygun olanıdır?",
    "Yoğun sermaye gerektiren uzun vadeli bir rüzgâr santrali yatırımı",
    ["Bir perakende şirketinin mevsimsel satışları için kısa vadeli stok finansmanı ihtiyacı",
     "Bir bireyin konut edinmek amacıyla kullandığı kredi",
     "Bir portföy yönetim şirketinin fon kuruluş giderleri",
     "Bir aracı kurumun işletme sermayesi ihtiyacı"],
    "Kanun m. 61/B-1'e göre proje finansmanı, uzun vadeli ve yoğun sermaye isteyen altyapı, enerji, sanayi veya teknoloji "
    "yatırımları gibi projelerin gerçekleştirilmesi için proje finansman fonu yoluyla finansman sağlanmasıdır.", zorluk="easy")

# ================================================================ konut ve varlık finansmanı (m. 57-60)
P.q("6362 s. SPKn m. 57/1",
    f"{K}, aşağıdakilerden hangisi konut finansmanı kapsamında değildir?",
    "İşyeri edinmek isteyen bir tacire ticari kredi kullandırılması",
    ["Konut edinmek isteyen tüketiciye kredi kullandırılması",
     "Konutun finansal kiralama yoluyla tüketiciye kiralanması",
     "Tüketicinin sahip olduğu konutun teminatı altında kredi kullandırılması",
     "Konut kredilerinin yeniden finansmanı amacıyla kredi kullandırılması"],
    "Kanun m. 57/1'e göre konut finansmanı; konut edinmeleri amacıyla tüketicilere kredi kullandırılması, konutların "
    "finansal kiralama yoluyla tüketicilere kiralanması, sahip oldukları konutların teminatı altında tüketicilere kredi "
    "kullandırılması ve bu kredilerin yeniden finansmanıdır. Ticari işyeri kredisi kapsam dışıdır.", zorluk="easy")

P.q("6362 s. SPKn m. 57/2",
    f"{K}, aşağıdakilerden hangisi konut finansmanı kuruluşları arasında sayılmamıştır?",
    "Portföy yönetim şirketleri",
    ["Konut finansmanı kapsamında doğrudan tüketiciye kredi kullandıran bankalar",
     "BDDK’nın uygun gördüğü finansal kiralama şirketleri",
     "BDDK’nın uygun gördüğü finansman şirketleri",
     "BDDK’nın uygun gördüğü tasarruf finansman şirketleri"],
    "Kanun m. 57/2'ye göre konut finansmanı kuruluşları, doğrudan tüketiciye kredi kullandıran veya finansal kiralama yapan "
    "bankalar ile BDDK'nın uygun gördüğü finansal kiralama, finansman ve tasarruf finansman şirketleridir (7292 s. Kanunla "
    "2021 değişikliği). Portföy yönetim şirketleri bu kapsamda değildir.")

P.q("6362 s. SPKn m. 57/3",
    "Bir banka, tüketiciye konut edinmesi için kredi kullandırmaktadır. "
    f"{K}, bu kredi kullandırımında bankanın yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Konut edinme amacını tespit etmesi ve krediyi ipotek veya uygun teminatla güvenceye alması",
    ["Kredinin tamamını ipoteğe dayalı menkul kıymet ihracıyla fonlaması",
     "Krediyi kullandırmadan önce Kuruldan izin alması",
     "Konutun değerlemesini sadece banka personeline yaptırması",
     "Kredi tutarını, bağımsız değerleme raporunda belirlenen konut değerinin yarısıyla sınırlaması"],
    "Kanun m. 57/3'e göre konut finansmanı kuruluşları, konut edinme amacını yeterli bilgi ve belgeyle tespit etmek ve "
    "kullandırılan krediyi veya finansal kiralamayı ipotek veya Kurulca uygun görülen teminatlarla güvence altına almak "
    "zorundadır; m. 57/5'e göre Kurul yetkili değerleme kuruluşlarınca değerleme yapılmasını zorunlu tutabilir.")

P.oncul("6362 s. SPKn m. 58",
    "Konut finansmanı ve varlık finansmanı fonlarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Fon, tüzel kişiliği olmayan bir mal varlığıdır.",
     "Fon kurulu, menkul kıymet sahiplerinin haklarını koruyacak şekilde fonu temsil eder ve yönetir.",
     "Fon portföyüne alınan varlıkların kayıtlarının doğruluğundan fon kurucusu sorumludur.",
     "Fon mal varlığı, menkul kıymetler itfa edilinceye kadar kamu alacakları için dahi haczedilemez."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 58/1'e göre konut ve varlık finansmanı fonları tüzel kişiliği olmayan mal varlıklarıdır; m. 58/3'e göre fon "
    "kurulu fonu temsil eder ve yönetir, varlıkların kayıtlarının doğruluğundan ve korunmasından da fon kurulu sorumludur. "
    "m. 58/2'ye göre fon mal varlığı itfaya kadar haczedilemez.", zorluk="hard")

P.q("6362 s. SPKn m. 58/5",
    "Bir varlık finansmanı fonu, ipotekle teminat altına alınmış konut kredisi alacaklarını portföyüne almıştır. "
    f"{K}, bu devrin sicile yansıtılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Devir sicilde beyanlar hanesine kaydedilir; Kurul fon adına tescili zorunlu tutabilir.",
    ["Devrin geçerliliği için mevcut ipoteğin terkin edilip fon adına yeniden kurulması ve tescili gerekir.",
     "Devir sicile yansıtılmaz, fon kurulunun defterine kaydedilmesi yeterlidir.",
     "İpotek, fon kurucusu adına yeniden tescil edilir.",
     "Devir için borçlu tüketicinin noter onaylı muvafakati aranır."],
    "Kanun m. 58/5'e göre ipotekle teminat altına alınmış bir varlığın fon portföyüne alınması hâlinde, devrin gerçekleştiği "
    "ilgili sicilde beyanlar hanesine kaydedilir; Kurul bu hâlde ipoteğin veya mülkiyetin fon adına sicile tescil ettirilmesini "
    "zorunlu tutabilir.")

P.q("6362 s. SPKn m. 58/1",
    f"{K}, konut finansmanı veya varlık finansmanı fonunun portföyündeki varlıklar karşılık gösterilerek ihraç edilen "
    "sermaye piyasası aracı aşağıdakilerden hangisidir?",
    "İpoteğe veya varlığa dayalı menkul kıymet",
    ["İpotek veya varlık teminatlı menkul kıymet", "Kira sertifikası", "Gayrimenkul sertifikası", "Projeye dayalı menkul kıymet"],
    "Kanun m. 58/1'e göre ipoteğe ve varlığa dayalı menkul kıymetler, ilgili fonların veya ipotek finansmanı kuruluşlarının "
    "portföyündeki varlıklar karşılık gösterilerek ihraç edilir. Teminatlı menkul kıymetler (m. 59) ise ihraççının genel "
    "yükümlülüğüdür.")

P.q("6362 s. SPKn m. 59/1",
    f"{K}, ihraççıların genel yükümlülüğü niteliğinde olan ve teminatlar karşılık gösterilerek ihraç edilen sermaye piyasası "
    "aracı aşağıdakilerden hangisidir?",
    "İpotek ve varlık teminatlı menkul kıymet",
    ["İpoteğe ve varlığa dayalı menkul kıymet", "Varlık kiralama şirketinin ihraç ettiği kira sertifikası", "Projeye dayalı menkul kıymet", "Yatırım fonu katılma payı"],
    "Kanun m. 59/1'e göre ipotek ve varlık teminatlı menkul kıymetler, ihraççıların genel yükümlülüğü niteliğinde olan ve "
    "teminatlar karşılık gösterilerek ihraç edilen araçlardır; teminatla karşılanmayan alacak için ihraççının diğer mal "
    "varlığına başvurulabilir.")

P.q("6362 s. SPKn m. 59",
    f"{K}, ipotek ve varlık teminatlı menkul kıymetlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Teminat varlıklarla karşılanmayan alacak için ihraççının diğer mal varlığına başvurulamaz.",
    ["İhraççılar teminat varlıkları diğer varlıklarından ayrı izlemekle yükümlüdür.",
     "Kurul, teminat varlık kayıtlarının ayrı bir kuruluş nezdinde de tutulmasını zorunlu tutabilir.",
     "İtfaya kadar teminat varlıklar teminat amacı dışında tasarruf edilemez.",
     "Temerrütte teminat varlık gelirleri öncelikle menkul kıymet sahiplerine ödenir."],
    "Kanun m. 59'a göre teminat varlıklar ayrı izlenir, Kurul kayıtların ayrı kuruluşta da tutulmasını isteyebilir ve itfaya "
    "kadar teminat amacı dışında tasarruf edilemez. Temerrütte gelir öncelikle menkul kıymet sahiplerine ve riskten korunma "
    "sözleşmelerinin karşı taraflarına ödenir; karşılanmayan alacak için ihraççının diğer mal varlığına başvurulabilir.")

P.q("6362 s. SPKn m. 59/4",
    "Teminatlı menkul kıymet ihraç eden bir banka yükümlülüklerini yerine getirememiş ve teminat varlıklardan gelir elde "
    f"edilmiştir. {K}, bu gelir öncelikle kimlere yapılacak ödemelerde kullanılır?",
    "Menkul kıymet sahiplerine ve riskten korunma sözleşmesi taraflarına",
    ["Bankanın mevduat sahiplerine ve Tasarruf Mevduatı Sigorta Fonuna",
     "Bankanın kamu borçlarına ve çalışanlarının alacaklarına",
     "Bankanın imtiyazlı ve adi tüm alacaklılarına, alacakları oranında garameten",
     "Yatırımcı Tazmin Merkezine ve Kurula"],
    "Kanun m. 59/4'e göre ihraççının yükümlülüklerini yerine getirememesi, yönetiminin kamuya devri, faaliyet izninin "
    "kaldırılması veya iflası hâlinde teminat varlıklardan elde edilen gelir öncelikle menkul kıymet sahiplerine ve teminat "
    "varlıkların riskten korunması amacıyla yapılmış sözleşmelerin karşı taraflarına ödenir.")

P.q("6362 s. SPKn m. 60",
    f"{K}, aşağıdakilerden hangisi ipotek finansmanı kuruluşlarının Kanunda sayılan faaliyetleri arasında yer almaz?",
    "Tüketicilere doğrudan konut kredisi kullandırmak",
    ["Konut finansmanı kapsamındaki varlıkları devralmak",
     "Devraldığı varlıkları başka kuruluşlara devretmek",
     "Devraldığı varlıkların yönetimini yürütmek",
     "Belirlenen varlıkları teminat olarak almak"],
    "Kanun m. 60/1'e göre ipotek finansmanı kuruluşları, konut ve varlık finansmanı kapsamında Kurulca belirlenen varlıkların "
    "devralınması, devredilmesi, yönetimi, teminat olarak alınması ve Kurulca uygun görülen diğer faaliyetler için kurulan "
    "anonim ortaklıklardır. Tüketiciye doğrudan kredi konut finansmanı kuruluşlarının faaliyetidir.")

P.sayisal("6362 s. SPKn m. 60/2",
    f"{K}, ipotek finansmanı kuruluşlarının sermayesinin veya oy haklarının doğrudan veya dolaylı olarak yüzde kaç veya daha "
    "fazlasını teşkil eden payların sahipleri, bankacılık mevzuatında banka kurucuları için aranan şartları taşımalıdır?",
    "%10", ["%5", "%20", "%25", "%50"],
    "Kanun m. 60/2'ye göre ipotek finansmanı kuruluşlarının sermayesinin nakden ve muvazaadan âri ödenmiş olması ve Kurulca "
    "belirlenen miktardan az olmaması; kurucuları ile yüzde on veya daha fazla paya sahip olanların 5411 sayılı Kanunda "
    "banka kurucu ortakları için aranan şartları taşıması zorunludur.", zorluk="hard")

# ================================================================ kitle fonlaması (m. 3/z, 35/A)
P.q("6362 s. SPKn m. 3/z, 35/A",
    f"{K}, kitle fonlamasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kitle fonlamasıyla toplanan fonlar Yatırımcı Tazmin Merkezinin güvencesi altındadır.",
    ["Kitle fonlaması bir projenin veya girişim şirketinin fon ihtiyacı için yapılır.",
     "Kurul, faaliyetlerin ortaklığa veya borçlanmaya dayalı yapılması konusunda belirleme yapabilir.",
     "Platformların kurulması ve faaliyete başlaması Kurul iznine tabidir.",
     "Bilgi formunu imzalayanlar yanlış veya eksik bilgilerden doğan zarardan müteselsilen sorumludur."],
    "Kanun m. 3/z'ye göre kitle fonlaması, bir projenin veya girişim şirketinin fon ihtiyacı için Kanunun yatırımcı tazminine "
    "ilişkin hükümlerine tabi olmaksızın platformlar aracılığıyla halktan para toplanmasıdır. m. 35/A platformları Kurul "
    "iznine bağlar, ortaklığa veya borçlanmaya dayalı model belirlemesini Kurula bırakır ve bilgi formundan müteselsil "
    "sorumluluk öngörür.")

P.oncul("6362 s. SPKn m. 4/1, 35/A",
    "Kitle fonlaması faaliyetlerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Kitle fonlaması suretiyle para toplanması izahname hazırlama yükümlülüğüne tabi değildir.",
     "Kitle fonlaması ve buna bağlı işlemler yatırım hizmetleri ve faaliyetleri kapsamında değerlendirilir.",
     "Platformlar ile fon sağlayanlar arasındaki ilişkiler genel hükümlere tabidir.",
     "Platformların hukuka aykırı işlemlerinde uygulanacak tedbirlerde Kanunun sermaye piyasası kurumlarına ilişkin tedbir hükmü kıyasen uygulanır."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Kanun m. 4/1 kitle fonlamasını izahname ve ihraç belgesi yükümlülüğü dışında tutar. m. 35/A'ya göre kitle fonlaması ve "
    "platformlar m. 37-38 kapsamında değerlendirilmez ve borsa hükümlerine tabi değildir; ilişkiler genel hükümlere tabidir, "
    "hukuka aykırı işlemlerde m. 96 kıyasen uygulanır.", zorluk="hard")

P.q("6362 s. SPKn m. 35/A-1",
    "Bir girişimci, geliştirdiği yazılım projesi için halktan borçlanmaya dayalı olarak fon toplamak istemektedir. "
    f"{K}, bu faaliyete ilişkin aşağıdakilerden hangisi doğrudur?",
    "İzinli platform aracılığıyla yapılır; bankacılık mevzuatına tabi değildir.",
    ["Borçlanmaya dayalı olduğu için bankacılık mevzuatına tabidir ve BDDK izniyle yapılır.",
     "Kurul onaylı izahname yayımlanması şartıyla doğrudan halktan yapılabilir.",
     "Aracı kurum aracılığıyla halka arz yoluyla yapılması zorunludur.",
     "Borçlanmaya dayalı kitle fonlaması Kanunda yasaklanmıştır."],
    "Kanun m. 35/A-1'e göre Kurul, kitle fonlamasının ortaklığa veya borçlanmaya dayalı olarak yapılması konusunda belirleme "
    "yapabilir ve borçlanmaya dayalı kitle fonlaması faaliyetlerine bankacılık mevzuatı hükümleri uygulanmaz; faaliyet Kurulca "
    "izin verilen platformlar aracılığıyla yürütülür.")

# ================================================================ kripto varlıklar (m. 3/aa-ee, 35/B, 35/C, 99/A-2, 99/B, 130/5, 74/1)
P.oncul("6362 s. SPKn m. 3/aa-dd",
    "Kripto varlıklara ilişkin Kanunda yer alan tanımlar aşağıda eşleştirilmiştir:",
    ["Platform – Kripto varlıkların ve anahtarların depolanmasını sağlayan donanım",
     "Cüzdan – Kripto varlıkların transferini ve anahtarların çevrim içi veya dışı depolanmasını sağlayan yazılım ya da donanım",
     "Kripto varlık saklama hizmeti – Platform müşterilerinin kripto varlıklarının veya özel anahtarlarının saklanması",
     "Kripto varlık hizmet sağlayıcı – Platformlar, saklama kuruluşları ve Kurulca belirlenen diğer kuruluşlar"],
    f"{K}, yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "II, III ve IV", ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 3/aa cüzdanı, çç saklama hizmetini, cc hizmet sağlayıcıyı son üç eşleştirmedeki gibi tanımlar. "
    "m. 3/dd'ye göre platform, kripto varlık alım satım, ilk satış veya dağıtım, takas, transfer ve saklama işlemlerinin "
    "gerçekleştirildiği kuruluştur; depolamayı sağlayan donanım cüzdan tanımına girer.")

P.q("6362 s. SPKn m. 35/B-3",
    "Bir kripto varlık platformunun kuruluş başvurusunda ortakların nitelikleri incelenmektedir. "
    f"{K}, aşağıdakilerden hangisi kripto varlık hizmet sağlayıcılarının ortaklarında aranan şartlardan biri değildir?",
    "Sermaye piyasası faaliyetleri lisansına sahip olmak",
    ["Müflis olmamak ve konkordato ilan etmemiş olmak",
     "Kanun uyarınca işlem yasaklı olmamak",
     "Gerekli mali güç ve işin gerektirdiği dürüstlük ve itibara sahip olmak",
     "Ortaklık yapısının şeffaf ve açık olması"],
    "Kanun m. 35/B-3-a'ya göre ortaklarda; müflis olmamak, konkordato ve yeniden yapılandırma tasdiki bulunmamak, faaliyet izni "
    "iptal edilmiş kuruluşlarda %10 veya daha fazla paya sahip olmamak, sayılan suçlardan hükümlü olmamak, işlem yasaklı "
    "olmamak, mali güç, dürüstlük ve itibar ile şeffaf ortaklık yapısı aranır. Lisans şartı aranmaz.")

P.sayisal("6362 s. SPKn m. 35/B-3-d",
    "Bir kripto varlık platformunda %15 paya sahip bir ortak, sonradan hakkında kesinleşen bir mahkûmiyet nedeniyle Kanunda "
    f"ortaklar için aranan şartları kaybetmiştir. {K}, bu ortak paylarını şartları taşıyan kişilere en geç kaç ay içinde "
    "devretmelidir?",
    "6", ["1", "3", "12", "24"],
    "Kanun m. 35/B-3-d'ye göre %10 veya daha fazla paya ya da yönetim kurulunda temsil imtiyazına sahip ortaklar mali güç "
    "şartı dışındaki nitelikleri kaybederse paylarını şartları taşıyan kişilere altı ay içinde devretmelidir; bu sürede oy "
    "haklarının kullanımını Kurul belirler.", zorluk="hard")

P.q("6362 s. SPKn m. 35/B-1, 2",
    "Bir kripto varlık platformunun kuruluş ve faaliyet izni başvurusu değerlendirilmektedir. "
    f"{K}, platformun bilgi sistemleri ve teknolojik altyapısının uygunluğunda hangi kurumun belirlediği kriterler aranır?",
    "Türkiye Bilimsel ve Teknolojik Araştırma Kurumu",
    ["Bilgi Teknolojileri ve İletişim Kurumu", "Bankacılık Düzenleme ve Denetleme Kurumu",
     "Türkiye Cumhuriyet Merkez Bankası", "Mali Suçları Araştırma Kurulu Başkanlığı"],
    "Kanun m. 35/B-2'ye göre kripto varlık hizmet sağlayıcıların kuruluşuna ve/veya faaliyete başlamasına izin verilebilmesi "
    "için bilgi sistemleri ve teknolojik altyapıları konusunda TÜBİTAK'ın belirleyeceği kriterlere uygunluk aranır; kuruluş "
    "ve faaliyet izni Kurula aittir.", zorluk="easy")

P.q("6362 s. SPKn m. 35/B-1",
    "Bir kripto varlık platformunun ortağı, Kurulun iznini almadan paylarını bir yatırım şirketine devretmiş ve devir pay "
    f"defterine işlenmiştir. {K}, bu kayda ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurul izni olmayan devre ilişkin pay defteri kaydı hükümsüzdür.",
    ["Kayıt geçerlidir; Kurula sonradan bildirim yapılması yeterlidir.",
     "Kayıt geçerlidir; ancak devralanın oy hakları bir yıl süreyle donar.",
     "Kayıt, devralanın TÜBİTAK kriterlerini sağlaması hâlinde geçerli olur.",
     "Kayıt, genel kurulun onayıyla geçerlilik kazanır."],
    "Kanun m. 35/B-1'e göre kripto varlık hizmet sağlayıcılarında pay devirleri Kurul iznine tabidir; buna aykırı devirler "
    "pay defterine kaydolunmaz ve bu hükme aykırı olarak pay defterine yapılan kayıtlar hükümsüzdür.")

P.q("6362 s. SPKn m. 35/B-6, 8",
    f"{K}, Kanunun kripto varlıklara uygulanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bir kripto varlığın satışına izin verilmesi, o varlığın kamuca tekeffülü anlamına gelir.",
    ["Sermaye piyasası araçlarına özgü haklar sağlayan kripto varlıklar için Kurul düzenleme yapmaya yetkilidir.",
     "Kurul, belirli kripto varlıkların satışının araçlara ilişkin hükümlere tabi olmaksızın platformlarda yapılmasına esas belirleyebilir.",
     "Bilgilendirme dokümanını imzalayanlar yanlış veya eksik bilgilerden müteselsilen sorumludur.",
     "Kripto varlıklarla yapılan işlemlerde Türk Parasının Kıymetini Koruma mevzuatı saklıdır."],
    "Kanun m. 35/B-6'ya göre araçlara özgü haklar sağlayan kripto varlıklarda Kurul yetkilidir; diğer bazı kripto varlıkların "
    "platformlarda satışına esas belirleyebilir ve bu izin kamuca tekeffül anlamına gelmez. Bilgilendirme dokümanını "
    "imzalayanlar müteselsilen sorumludur; m. 35/B-9 TPKK mevzuatını saklı tutar.")

P.q("6362 s. SPKn m. 35/B-10",
    "Bir yatırımcı, platformdaki kripto varlıklarını bir krediye teminat olarak göstermek üzere rehin sözleşmesi yapmak "
    f"istemektedir. {K}, bu sözleşmeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu sözleşmelere Taşınır Rehni Kanunu uygulanmaz.",
    ["Sözleşme Taşınır Rehin Siciline tescil edilerek kurulur.",
     "Kripto varlıklar üzerinde hukuken rehin kurulamaz.",
     "Rehin, MKK’ya bildirimle üçüncü kişilere karşı ileri sürülebilir.",
     "Rehin sözleşmesi Kurul onayıyla geçerlilik kazanır."],
    "Kanun m. 35/B-10'a göre kripto varlıkları konu edinen rehin sözleşmelerine 6750 sayılı Ticari İşlemlerde Taşınır Rehni "
    "Kanunu uygulanmaz; bu sözleşmeler Taşınır Rehin Sicili sistemine tabi değildir.", zorluk="hard")

P.q("6362 s. SPKn m. 35/C-1",
    f"{K}, kripto varlık hizmet sağlayıcıları ile müşterileri arasındaki ilişkilere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hizmet sağlayıcının sorumluluğunu sınırlandıran sözleşme şartları geçerlidir.",
    ["Sözleşmeler yazılı şekilde veya uzaktan iletişim araçlarıyla mesafeli olarak kurulabilir.",
     "Kurul, sözleşmelerin içeriğinde yer alması gereken asgari hususları belirleyebilir.",
     "Platformlar müşteri itiraz ve şikâyetlerini çözecek dâhili mekanizmalar kurar.",
     "Hizmet sağlayıcılar müşterilerin kimliklerini 5549 sayılı Kanun kapsamında tespit eder."],
    "Kanun m. 35/C-1'e göre sözleşmeler yazılı veya kimlik doğrulamaya imkân veren uzaktan iletişim yöntemleriyle kurulabilir; "
    "Kurul asgari içeriği belirleyebilir. Hizmet sağlayıcıların müşterilere karşı sorumluluğunu kaldıran veya sınırlandıran her "
    "türlü sözleşme şartı geçersizdir; şikâyet mekanizması ve 5549 s. Kanuna göre kimlik tespiti zorunludur.")

P.q("6362 s. SPKn m. 35/C-2",
    "Bir kripto varlık platformu, yeni bir kripto varlığı kendi nezdinde işleme açmak istemektedir. "
    f"{K}, bu işleme açma sürecine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Platformun yazılı bir listeleme prosedürü oluşturması zorunludur.",
    ["Her kripto varlığın listelenmesi için Kurulun ayrı onayı gerekir.",
     "Listeleme kararı TÜBİTAK tarafından verilir.",
     "Listeleme, kripto varlığın kamuca tekeffülü anlamına gelir.",
     "Listelemeden önce kripto varlık için izahname onaylatılması gerekir."],
    "Kanun m. 35/C-2'ye göre platformlarca işlem görecek veya ilk satışı yapılacak kripto varlıkların belirlenmesine ve "
    "işlem görmesinin sonlandırılmasına ilişkin yazılı listeleme prosedürü oluşturulması zorunludur; Kurul TÜBİTAK görüşüyle "
    "teknik kriterler belirleyebilir. Listeleme kamuca tekeffül anlamına gelmez.")

P.q("6362 s. SPKn m. 35/C-5",
    f"{K}, kripto varlık transferlerine ilişkin kayıt ve bilgi yükümlülüklerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gönderici ve alıcı bilgilerinin mesajlara eklenmesi hizmet sağlayıcının takdirindedir.",
    ["Cüzdan ve hesap kayıtları güvenli, erişilebilir ve takip edilebilir şekilde tutulur.",
     "Tüm işlem kayıtlarının bütünlüğü, doğruluğu ve gizliliği sağlanır.",
     "Müşterilerin kripto varlık transfer işlemlerinde Kurul ve MASAK tarafından yapılan düzenlemelere uyulur.",
     "Mesajlaşma için dağıtık defter teknolojisi veya uygulama ara yüzleri kullanılabilir."],
    "Kanun m. 35/C-5'e göre kayıtlar güvenli, erişilebilir ve takip edilebilir tutulur; bütünlük, doğruluk ve gizlilik "
    "sağlanır. Transferlerde Kurul ve MASAK düzenlemelerine uyulur ve transfer mesajlarında öngörülen gönderici ve alıcı "
    "bilgileri belirlenen sürelerde güvenli şekilde gönderilir; bu bir takdir değil yükümlülüktür.", zorluk="hard")

P.q("6362 s. SPKn m. 35/C-10, 74/1",
    "Kurulca faaliyet izni verilen bir kripto varlık platformu faaliyete başlamaya hazırlanmaktadır. "
    f"{K}, bu platforma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yetki belgesi alır ve Türkiye Sermaye Piyasaları Birliğine üyelik için başvurur.",
    ["Türkiye Değerleme Uzmanları Birliğine üye olmakla yükümlüdür.",
     "Yetki belgesi TÜBİTAK tarafından verilir.",
     "Birlik üyeliği isteğe bağlıdır; başvuru yapmaması faaliyet izninin devamını etkilemez.",
     "Yetki belgesi yerine ticaret siciline tescil yeterlidir."],
    "Kanun m. 35/C-10'a göre kripto varlık hizmet sağlayıcılarına icra edecekleri faaliyetleri gösteren yetki belgesi verilir; "
    "m. 74/1'e (2024) göre kitle fonlama platformları ve kripto varlık hizmet sağlayıcıları TSPB'ye üye olmak için başvurmak "
    "zorundadır ve başvurmayanların faaliyetleri durdurulur.")

P.q("6362 s. SPKn m. 99/B-3, 4",
    "Bir kripto varlık platformu siber saldırıya uğramış ve müşterilerin kripto varlıkları kaybolmuştur. "
    f"{K}, bu kayıplardan sorumluluğa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Platform, kusurunun bulunmadığını ispat ederse siber saldırı kayıplarından sorumlu tutulamaz.",
    ["Platform bu kayıplardan Türk Borçlar Kanunu m. 71 kapsamında sorumludur.",
     "Kayıplar platformdan tazmin edilemezse mensuplar kusurlarına göre sorumlu olur.",
     "Mensupların şahsi sorumluluğunda Kanunun şahsi iflasa ilişkin hükmü uygulanır.",
     "Kusur olmaksızın yaşanan geçici emir iletim kesintilerinden doğan zararlar bu kapsamda değildir."],
    "Kanun m. 99/B-4'e göre hizmet sağlayıcılar bilişim sistemlerinin işletilmesi, siber saldırı, bilgi güvenliği ihlali veya "
    "personel davranışlarından kaynaklanan kayıplardan TBK m. 71 (tehlike sorumluluğu) kapsamında sorumludur; kusursuzluk "
    "ispatı sorumluluğu kaldırmaz. Tazmin edilemeyen kısım için mensuplar kusurlarına göre sorumludur ve m. 110/B uygulanır.",
    zorluk="hard")

P.q("6362 s. SPKn m. 99/B-2",
    f"{K}, kripto varlık hizmet sağlayıcılarının mali denetimi ve bilgi sistemleri bağımsız denetimi kim tarafından yapılır?",
    "Kurulca ilan edilen listede yer alan bağımsız denetim kuruluşları",
    ["TÜBİTAK’ın görevlendirdiği uzmanlar",
     "Türkiye Sermaye Piyasaları Birliği denetçileri",
     "Hizmet sağlayıcının yönetim kuruluna bağlı olarak çalışan iç denetim birimi",
     "Bankacılık Düzenleme ve Denetleme Kurumu denetçileri"],
    "Kanun m. 99/B-2'ye göre kripto varlık hizmet sağlayıcılarının mali denetimi ve bilgi sistemleri bağımsız denetimi Kurulca "
    "ilan edilen listedeki bağımsız denetim kuruluşlarınca yapılır; Kurul personeli bu denetimlere izleyici sıfatıyla eşlik edebilir.")

P.sayisal("6362 s. SPKn m. 99/A-2",
    "Kurul, bir kripto varlık platformunun mali yapısının ciddi surette zayıfladığını tespit etmiştir. "
    f"{K}, Kurulun platformdan mali yapısını güçlendirmesini istemesi hâlinde vereceği süre en fazla kaç aydır?",
    "3", ["1", "2", "6", "12"],
    "Kanun m. 99/A-2'ye göre Kurul, kripto varlık hizmet sağlayıcıların mali yapısının zayıflaması hâlinde üç ayı geçmemek "
    "üzere uygun süre içinde güçlendirilmesini isteyebilir veya süre vermeksizin faaliyetleri geçici olarak durdurabilir, "
    "yetkilerini kaldırabilir.")

P.sayisal("6362 s. SPKn m. 130/5",
    f"{K}, kripto varlık platformlarının bir önceki yıl faiz gelirleri hariç tüm gelirlerinin yüzde kaçı blokzincir "
    "teknolojilerinin geliştirilmesinde kullanılmak üzere TÜBİTAK bütçesine gelir kaydedilir?",
    "%1", ["%0,5", "%2", "%5", "%10"],
    "Kanun m. 130/5'e (7518 s. Kanun) göre her yıl platformların bir önceki yıl faiz gelirleri hariç tüm gelirlerinin yüzde "
    "biri Kurul bütçesine, yüzde biri de blokzincir ve ilgili bilişim teknolojilerinin geliştirilmesi için TÜBİTAK bütçesine "
    "mayıs ayı sonuna kadar ödenir.", zorluk="hard")

P.q("6362 s. SPKn m. 35/B-5",
    f"{K}, kripto varlık hizmet sağlayıcılarının Kanun hükümlerine tabiiyetine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Atıf yapılan hükümler dışında Kanunun diğer hükümlerine tabi değildir.",
    ["Kanunun tüm hükümlerine yatırım kuruluşları gibi tabidir.",
     "Kanunun sadece ceza hükümlerine tabidir.",
     "Kanuna değil, bankacılık mevzuatına tabidir.",
     "Payları halka arz edilmişse Kanunun halka açık ortaklıklara ilişkin hükümlerine tabidir."],
    "Kanun m. 35/B-5'e göre kripto varlık hizmet sağlayıcıları bu Kanunda atıf yapılan hükümler dışında Kanunun diğer "
    "hükümlerine tabi değildir; açıklık bulunmayan hususlarda Kurul düzenleyici işlem ve özel kararlarla uygulamayı yönlendirir; "
    "bankalara yükümlülük getiren düzenlemelerde BDDK'nın görüşü alınır.")

P.q("6362 s. SPKn m. 12/1-2",
    "Halka açık bir ortaklığın paylarının borsa fiyatı nominal değerinin oldukça altındadır ve ortaklık sermaye artırımı "
    f"yapmak istemektedir. {K}, yeni payların ihraç fiyatına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurul, belirlediği esaslar çerçevesinde nominal değerin altında ihraca izin verebilir.",
    ["Paylar TTK gereği nominal değerin altında ihraç edilemez.",
     "Paylar, borsa fiyatı ne olursa olsun primli ihraç edilmek zorunluluğundadır.",
     "Paylar nominal değerin altında ihraç edilirse bedelleri ayni olarak ödenebilir.",
     "Nominal değerin altında ihraç için genel kurulda oybirliği gerekir."],
    "Kanun m. 12/2'ye göre Kurul, payların piyasa fiyatı veya defter değeri nominal değerin üzerindeyse primli ihracı "
    "isteyebilir; altındaysa belirlediği esaslar çerçevesinde nominal değerin altında ihraca izin verebilir. m. 12/1'e göre "
    "pay bedellerinin tamamen ve nakden ödenmesi şarttır.", zorluk="hard")

P.q("6362 s. SPKn m. 12/1",
    f"{K}, ihraç olunan payların bedellerinin ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bedeller tamamen ve nakden ödenir; Kurul birleşme gibi hâllerde istisna belirleyebilir.",
    ["TTK’daki genel kurala göre bedellerin dörtte biri tescilden önce, kalanı iki yıl içinde ödenebilir.",
     "Bedeller ayni olarak ödenebilir, Kurulun onayı aranmaz.",
     "Bedellerin ödenme şekli ihraççının yönetim kurulunca tek başına belirlenir.",
     "Bedeller, satış süresi sonunda satılamayan paylar için ödenmez."],
    "Kanun m. 12/1'e göre ihraç olunan payların bedellerinin tamamen ve nakden ödenmesi şarttır; Kurul satılamayan payların "
    "alınacağının taahhüt edilmesini isteyebilir ve birleşme, bölünme, hisse değişimi gibi yapılandırmalarda nakden ödemenin "
    "zorunlu olmadığı durumları belirleyebilir.")

P.q("6362 s. SPKn m. 61/1",
    "Bir yatırımcı, bir hastane binasının finansmanı amacıyla bir varlık kiralama şirketinin ihraç ettiği kira sertifikalarını "
    f"satın almıştır. {K}, bu yatırımcının sertifikadan doğan hakkı aşağıdakilerden hangisidir?",
    "Varlıktan elde edilen gelirlerden sertifikadaki payı oranında hak sahibi olmak",
    ["Varlık kiralama şirketinin genel kurulunda oy kullanmak",
     "Hastane binasının tapuda paylı mülkiyetine sahip olmak",
     "Varlık kiralama şirketinin dağıtılabilir kârından kâr payı almak",
     "Varlığın getirisinden bağımsız sabit faiz almak"],
    "Kanun m. 61/1'e göre kira sertifikaları, her türlü varlık veya hakkın finansmanını sağlamak amacıyla varlık kiralama "
    "şirketlerince ihraç edilen ve sahiplerinin bu varlık veya haklardan elde edilen gelirlerden payları oranında hak sahibi "
    "olmalarını sağlayan araçlardır; ortaklık hakkı vermez.", zorluk="easy")

P.q("6362 s. SPKn m. 60/3",
    "Bir banka, konut kredisi alacaklarını teminat göstererek bir ipotek finansmanı kuruluşundan kaynak temin etmiştir. "
    f"Sonrasında bankanın yönetimi kamuya devredilmiştir. {K}, teminat gösterilen alacaklara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Başka bir amaçla tasarruf edilemez ve üçüncü kişilerce haczedilemez.",
    ["Yönetimin devriyle teminat ilişkisi sona erer ve alacaklar bankaya döner.",
     "Kamu alacakları için haczedilebilir, özel alacaklar için haczedilemez.",
     "Tasarruf Mevduatı Sigorta Fonunun onayıyla başka amaçla kullanılabilir.",
     "Alacaklar ipotek finansmanı kuruluşunun iflas masasına dâhil edilir."],
    "Kanun m. 60/3'e göre ipotek finansmanı kuruluşundan kaynak temini için teminat gösterilen varlıklar, kaynak temin eden "
    "kurumun yönetim veya denetiminin kamuya devri hâlinde dahi başka amaçla tasarruf edilemez, rehnedilemez, kamu "
    "alacakları dahil üçüncü kişilerce haczedilemez, ihtiyati tedbir konulamaz ve iflas masasına dâhil edilemez.")

P.q("6362 s. SPKn m. 99/B-1",
    "Kurul, bir kripto varlık platformunun bilişim altyapısına ilişkin kapsamlı bir denetim başlatmıştır. "
    f"{K}, bu denetime katılacak personele ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurulun talebiyle kamu kurumlarından personel görevlendirilebilir.",
    ["Denetimi sadece Kurul meslek personeli yürütebilir.",
     "Denetim, platformun seçeceği bağımsız bilişim uzmanlarına bırakılır.",
     "Denetime TÜBİTAK personeli ancak mahkeme kararıyla katılabilir.",
     "Görevlendirilen personel Kanunun sır saklama hükümlerine tabi değildir."],
    "Kanun m. 99/B-1'e göre kripto hizmet sağlayıcıların denetiminde m. 88-90 uygulanır; Kurulun talebi üzerine bakanlıklara "
    "bağlı, ilgili ve ilişkili kurumlar ile diğer kamu kurumlarından, meslek personeli olma şartı aranmaksızın personel "
    "görevlendirilebilir ve bunlar hakkında da m. 89, 90, 111 ve 113 uygulanır.", zorluk="hard")

P.q("6362 s. SPKn Geçici m. 11/4-5",
    f"{K}, 2024 yılında kripto varlık hizmet sağlayıcılarına ilişkin getirilen geçiş hükümleri bakımından aşağıdakilerden "
    "hangisi doğrudur?",
    "Kripto varlıkları nakde çeviren yurt içindeki ATM ve benzeri cihazların faaliyeti üç ay içinde sonlandırılır.",
    ["Yurt dışında yerleşik platformlar Türkiye’deki faaliyetlerini bir yıl içinde sonlandırır.",
     "Mevcut hizmet sağlayıcılar herhangi bir beyan vermeksizin faaliyetlerine devam eder.",
     "Tasfiyeye giden kuruluşlar tasfiye süresince yeni müşteri kabul edebilir.",
     "Kripto ATM’leri bankaların gözetiminde faaliyetine süresiz devam eder."],
    "Kanun Geçici m. 11'e göre mevcut hizmet sağlayıcılar bir ay içinde izin başvurusu veya tasfiye beyanı vermek zorundadır ve "
    "tasfiyede yeni müşteri kabul edemez; yurt dışında yerleşik platformlar Türkiye'ye yönelik faaliyetlerini ve kripto "
    "ATM'leri faaliyetlerini üç ay içinde sonlandırır.", zorluk="hard")

P.q("6362 s. SPKn m. 3/bb",
    f"{K}, aşağıdakilerden hangisi “kripto varlık” tanımının unsurlarından biri değildir?",
    "Bir merkez bankası tarafından ihraç edilmiş olması",
    ["Dağıtık defter veya benzer bir teknoloji kullanılması",
     "Elektronik olarak oluşturulup saklanabilmesi",
     "Dijital ağlar üzerinden dağıtımının yapılması",
     "Değer veya hak ifade edebilen gayri maddi varlık olması"],
    "Kanun m. 3/bb'ye göre kripto varlık, dağıtık defter teknolojisi veya benzer bir teknoloji kullanılarak elektronik olarak "
    "oluşturulup saklanabilen, dijital ağlar üzerinden dağıtımı yapılan ve değer veya hak ifade edebilen gayri maddi varlıklardır; "
    "ihraççının niteliği tanımın unsuru değildir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
