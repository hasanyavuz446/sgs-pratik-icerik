# -*- coding: utf-8 -*-
"""Vergi · Kurumlar Vergisi · Kurum Kazancı — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında kurum kazancı; matrah hesabı (iştirak kazancı, KKEG, geçmiş yıl zararı), yurt içi
asgari kurumlar vergisi, örtülü sermaye ve finansman gideri kısıtlaması üzerinden, uzun olay kurgularıyla sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 5520 sayılı KVK md. 5, 6, 8, 9, 10, 11, 12, 13, 32, 32/C.
7582 sayılı Kanunun (21.05.2026) 2026 dönemine yönelik değişiklikleri nedeniyle hesap soruları 2025 hesap dönemi
üzerinden kurulur; oran ve tutarlar vergi_ortak.py ile hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_kurum_kazanci_2026.json", lesson="kurumlar_vergisi", topic="kurum_kazanci",
          konu_adi="Kurum Kazancı", seed=2026092903,
          surum="5520 sayılı KVK güncel metni (7582 dahil); hesaplar 2025 hesap dönemi; 29.09.2026 kontrolü")

K = "5520 sayılı Kurumlar Vergisi Kanunu’na göre"
K26 = "5520 sayılı Kurumlar Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

m1 = 8_000_000 + 700_000 - 1_500_000 - 500_000
P.sayisal("KVK md. 5/1-a, 9",
    "Tam mükellef (KLM) A.Ş.’nin 2025 hesap dönemi ticari bilanço kârı 8.000.000 ₺’dir. Bu kârın 1.500.000 ₺’si tam mükellef "
    "(NOP) A.Ş.’den elde edilen iştirak kazancıdır. Gider hesaplarında izlenen tutarların 700.000 ₺’si kanunen kabul "
    "edilmeyen giderdir. Şirketin beyannamelerde yıllar itibarıyla ayrı ayrı gösterilmiş olan 2019 yılı zararından 400.000 ₺ "
    f"ve 2020 yılı zararından 500.000 ₺ mahsup edilmemiş olarak kalmıştır.\n\n{K}, (KLM) A.Ş.’nin 2025 hesap dönemi "
    "kurumlar vergisi matrahı kaç ₺’dir?",
    tl(m1), secenekler(m1, m1 - 400_000, m1 + 1_500_000, 8_000_000 - 1_500_000 - 900_000, 8_000_000 - 1_500_000 - 500_000),
    "Ticari bilanço kârına KKEG eklenir, iştirak kazancı (md. 5/1-a) düşülür: 8.000.000 + 700.000 − 1.500.000 = 7.200.000 ₺. "
    "Md. 9'a göre zararlar beş yıldan fazla nakledilemez; 2020 zararı 2025'te son kez mahsup edilebilir, 2019 zararının süresi "
    "dolmuştur: 7.200.000 − 500.000 = 6.700.000 ₺.", zorluk="hard")

P.q("KVK md. 8",
    "Yeni kurulan ve sermayesini halka arzla artıran (YZA) A.Ş.’nin muhasebe müdürü, 2025 yılında yapılan harcamaların "
    "hangilerinin kurum kazancının tespitinde ayrıca indirilebileceğini değerlendirmektedir.\n\n"
    f"{K}, aşağıdakilerden hangisi kurum kazancının tespitinde indirilebilecek giderlerden biri değildir?",
    "Dönem kârı üzerinden hesaplanan kurumlar vergisi",
    ["Menkul kıymet ihraç giderleri", "Kuruluş ve örgütlenme giderleri",
     "Genel kurul toplantıları için yapılan giderler",
     "Sermayesi paylara bölünmüş komandit şirkette komandite ortağın kâr payı"],
    "Md. 8'e göre menkul kıymet ihraç giderleri, kuruluş ve örgütlenme giderleri, genel kurul, birleşme, devir, bölünme, fesih "
    "ve tasfiye giderleri ile komandite ortağın kâr payı indirilebilir. Md. 11/1-d'ye göre hesaplanan kurumlar vergisi "
    "indirilemez.", zorluk="easy")

P.q("KVK md. 11",
    "Bir vergi müfettişi, (BCD) A.Ş.’nin 2025 hesap dönemi gider hesaplarını incelemekte ve kurum kazancının tespitinde "
    "indirilmesi kabul edilmeyen tutarları belirlemektedir.\n\n"
    f"{K}, aşağıdakilerden hangisi kanunen kabul edilmeyen giderlerden biri değildir?",
    "Sözleşmede ceza şartı olarak konulan ve karşı tarafa ödenen tazminat",
    ["Öz sermaye üzerinden hesaplanan faiz",
     "Vergi Usul Kanunu hükümlerine göre ödenen gecikme faizi",
     "Esas faaliyetle ilgisi olmayan yatın giderleri ve amortismanı",
     "Kurumun yöneticisinin suçundan doğan maddi ve manevi zarar tazminatı"],
    "Md. 11'e göre öz sermaye faizi, gecikme faizleri, esas faaliyetle ilgisiz deniz ve hava taşıtlarının giderleri ile "
    "kurumun, ortaklarının, yöneticilerinin ve çalışanlarının suçlarından doğan tazminatlar indirilemez. Sözleşmelerde ceza "
    "şartı olarak konulan tazminatlar md. 11/1-g'de açıkça hariç tutulmuştur.", zorluk="hard")

kv2 = (4_000_000 + 400_000 - 600_000) * 0.25
P.sayisal("KVK md. 5/1-a, 32",
    "Ticaret sektöründe faaliyet gösteren tam mükellef (RST) A.Ş.’nin 2025 hesap dönemi ticari bilanço kârı 4.000.000 ₺’dir. "
    "Kârın 600.000 ₺’si tam mükellef bir iştirakten alınan kâr payıdır; gider hesaplarında izlenen 400.000 ₺ ise kanunen kabul "
    "edilmeyen giderdir. Şirket banka, finans veya sigorta kuruluşu değildir; indirimli oran ve geçmiş yıl zararı yoktur."
    f"\n\n{K}, (RST) A.Ş.’nin 2025 hesap dönemi için hesaplanan kurumlar vergisi kaç ₺’dir?",
    tl(kv2), secenekler(kv2, 4_400_000 * 0.25, 4_000_000 * 0.25, 3_400_000 * 0.25, 3_800_000 * 0.30),
    "Matrah: 4.000.000 + 400.000 − 600.000 = 3.800.000 ₺. Md. 32'ye göre genel oran %25'tir: 3.800.000 × %25 = 950.000 ₺. "
    "Bu tutar indirim ve istisnalar düşülmeden önceki kazancın (4.400.000 ₺) %10'unu aştığından asgari vergi farkı çıkmaz.")

P.q("KVK md. 11/1-k",
    "(EFG) A.Ş. 2026 yılında faaliyetleriyle ilgili çeşitli ilan ve reklam giderlerine katlanmıştır. Şirketin mali müşaviri, "
    "2026 yılında Kanuna eklenen yeni bir bent nedeniyle bu giderlerin bir kısmının indirilemeyeceğini belirtmiştir."
    f"\n\n{K26}, aşağıdaki reklam giderlerinden hangisinin tamamı kurum kazancından indirilemez?",
    "Şans ve bahis oyunlarına ait reklam giderleri",
    ["Alkollü içkilere ait ilan ve reklam giderleri",
     "Gıda ürünlerine ait televizyon reklam giderleri",
     "Kurum adına yapılan sosyal medya tanıtım giderleri",
     "Tütün mamullerine ait ilan ve reklam giderleri"],
    "7577 sayılı Kanunla 2026'da eklenen md. 11/1-k'ye göre her türlü şans ve bahis oyunlarına ait ilan ve reklam giderleri "
    "indirilemez. Alkol ve tütün reklam giderlerinde md. 11/1-ı gereği yalnızca %50'si indirilemez; gıda ve kurumsal tanıtım "
    "reklamları olağan giderdir.", zorluk="hard")

P.q("KVK md. 11/1-ç, d",
    f"{K}, kurum kazancının tespitinde kanunen kabul edilmeyen giderlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "TTK’ya göre ayrılan yasal yedek akçeler gider olarak indirilebilir.",
    ["Her türlü para cezaları ve vergi cezaları indirilemez.",
     "6183 sayılı Kanuna göre ödenen gecikme zamları indirilemez.",
     "Transfer fiyatlandırması yoluyla örtülü dağıtılan kazançlar indirilemez.",
     "Örtülü sermaye üzerinden hesaplanan kur farkları indirilemez."],
    "Md. 11/1-ç'ye göre Türk Ticaret Kanunu'na, ana sözleşmeye veya kuruluş kanunlarına göre ayrılanlar dahil her ne isimle "
    "olursa olsun ayrılan yedek akçeler indirilemez. Para ve vergi cezaları, gecikme zamları, örtülü kazanç ve örtülü sermaye "
    "kur farkları da md. 11'de sayılmıştır.")

bg = 2_000_000 * 0.05
P.sayisal("KVK md. 10/1-c",
    "Tam mükellef (UVY) A.Ş.’nin 2025 hesap dönemine ait, bağış indirimi öncesi kurum kazancı 2.000.000 ₺’dir. Şirket yıl "
    "içinde kamu yararına çalışan bir derneğe makbuz karşılığında 150.000 ₺ nakdi bağış yapmış, bu tutarı gider yazmayıp "
    "beyannamede indirim olarak göstermek istemektedir. Başka indirim, istisna veya zarar bulunmamaktadır."
    f"\n\n{K}, (UVY) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı kaç ₺’dir?",
    tl(2_000_000 - bg), secenekler(2_000_000 - bg, 2_000_000 - 150_000, 2_000_000, 2_000_000 - 75_000, 2_000_000 - 50_000),
    "Md. 10/1-c'ye göre kamu yararına çalışan derneklere makbuz karşılığı yapılan bağışların o yıla ait kurum kazancının %5'ine "
    "kadar olan kısmı indirilir: 2.000.000 × %5 = 100.000 ₺. Matrah 2.000.000 − 100.000 = 1.900.000 ₺'dir.")

P.q("KVK md. 6",
    "(HIJ) A.Ş.’nin genel müdürü, kurum kazancının tespitinde hangi kanunun hükümlerine başvurulacağını ve safi kurum "
    "kazancının nasıl belirleneceğini mali müşavirine sormuştur.\n\n"
    f"{K}, safi kurum kazancının tespitine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gelir Vergisi Kanunu’nun ticari kazanç hakkındaki hükümlerine göre tespit edilir.",
    ["Gelir Vergisi Kanunu’nun serbest meslek kazancı hükümlerine göre tespit edilir.",
     "Sadece ticari bilanço kârı esas alınır, vergi kanunlarına göre düzeltme yapılmaz.",
     "Kurumun seçimine göre işletme hesabı veya bilanço esası uygulanır.",
     "Dağıtılan kâr esas alınarak tespit edilir."],
    "Md. 6'ya göre kurumlar vergisi mükellefiyet türlerine göre kurum kazancı üzerinden hesaplanır; safi kurum kazancının "
    "tespitinde Gelir Vergisi Kanunu'nun ticari kazanç hakkındaki hükümleri uygulanır.", zorluk="easy")

P.q("KVK md. 9",
    f"{K}, geçmiş yıl zararlarının mahsubuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zararlar beyannamede tek toplam tutar olarak gösterilse de mahsup hakkı korunur.",
    ["Zararlar beş yıldan fazla nakledilemez.",
     "Zararların beyannamede her yıla ilişkin tutarlar ayrı ayrı gösterilerek indirilmesi gerekir.",
     "Kurumlar vergisinden istisna kazançlarla ilgili yurt dışı zararlar mahsup edilemez.",
     "Yurt dışı zararların mahsubu için o ülkedeki denetim raporunun ibrazı gerekir."],
    "Md. 9'a göre geçmiş yıl zararları, beyannamede her yıla ilişkin tutarlar ayrı ayrı gösterilmek şartıyla ve beş yıldan "
    "fazla nakledilmemek kaydıyla indirilir. Yurt dışı zararlar istisna kazançlarla ilgili değilse ve denetim raporu ibraz "
    "edilirse mahsup edilir.")

sp = 200_000 + 300_000 * 0.5
P.sayisal("KVK md. 10/1-b",
    "Tam mükellef (ZAB) A.Ş. 2025 yılında ilgili kanunlar kapsamında amatör bir spor dalına 200.000 ₺, profesyonel bir futbol "
    "kulübüne 300.000 ₺ sponsorluk harcaması yapmış ve bunları gider yazmayıp beyannamede indirim olarak göstermiştir. "
    f"Sponsorluk indirimi öncesi kurum kazancı 5.000.000 ₺’dir.\n\n{K}, (ZAB) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi "
    "matrahı kaç ₺’dir?",
    tl(5_000_000 - sp), secenekler(5_000_000 - sp, 5_000_000 - 500_000, 5_000_000 - 250_000, 5_000_000 - 200_000, 5_000_000 - 150_000),
    "Md. 10/1-b'ye göre sponsorluk harcamalarının amatör spor dalları için tamamı, profesyonel spor dalları için %50'si "
    "indirilir: 200.000 + 150.000 = 350.000 ₺. Matrah 5.000.000 − 350.000 = 4.650.000 ₺.")

P.q("KVK md. 9",
    "(KLM) A.Ş., 2025 yılında (NOP) A.Ş.’yi Kanunun 19 ve 20. maddelerine uygun olarak devralmıştır. Devralınan kurumun devir "
    f"tarihindeki öz sermayesini aşan tutarda geçmiş yıl zararı bulunmaktadır.\n\n{K}, devralınan kurumun zararlarının "
    "devralan kurumca mahsubuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Devralınan kurumun faaliyetine en az beş yıl devam edilmesi şartlarından biridir.",
    ["Devralınan kurumun zararları devir işlemiyle birlikte şartsız olarak mahsup edilir.",
     "Devralınan kurumun zararlarının tamamı, öz sermaye tutarına bakılmaksızın mahsup edilebilir.",
     "Devralınan kurumun son üç yıla ilişkin beyannamelerinin süresinde verilmiş olması yeterlidir.",
     "Devralınan kurumun zararları ancak devralan kurumun zararı yoksa mahsup edilebilir."],
    "Md. 9/1-a'ya göre devralınan kurumun devir tarihindeki öz sermaye tutarını geçmeyen zararları, son beş yıla ilişkin "
    "beyannamelerin kanuni süresinde verilmiş olması ve devralınan kurumun faaliyetine en az beş yıl devam edilmesi şartıyla "
    "indirilebilir.", zorluk="hard")

P.q("KVK md. 12",
    "Tam mükellef (QRS) A.Ş.’nin 2025 hesap dönemi başı öz sermayesi 2.000.000 ₺’dir. Şirketin yıl içinde yaptığı borçlanmalar "
    "şunlardır: ortağı Bay (T)’den 3.000.000 ₺ borç; ortağı Bay (U)’nun arsasını teminat göstererek bir finans kuruluşu "
    "dışındaki Bay (V)’den 1.000.000 ₺ borç; iştiraki (WXY) A.Ş.’nin bankadan aynı şartlarla temin edip kullandırdığı "
    f"2.000.000 ₺ kredi.\n\n{K}, (QRS) A.Ş.’nin örtülü sermaye tespitine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İştirakin bankadan temin edip aynı şartlarla kullandırdığı kredi dikkate alınmaz.",
    ["Ortaktan alınan borç %50 oranında dikkate alınır.",
     "Ortağın gayrinakdi teminatıyla üçüncü kişiden alınan borç %50 oranında dikkate alınır.",
     "Ortaklardan alınan borçların toplamı öz sermayenin üç katını aştığından örtülü sermaye oluşmuştur.",
     "Karşılaştırmada dönem sonu öz sermaye esas alınır."],
    "Md. 12/6'ya göre iştiraklerin, ortakların veya ilişkili kişilerin bankalardan temin ederek aynı şartlarla kullandırdığı "
    "borçlar ile ortakların gayrinakdi teminatları karşılığında üçüncü kişilerden yapılan borçlanmalar örtülü sermaye "
    "sayılmaz. Dikkate alınan borç yalnız ortaktan alınan 3.000.000 ₺ olup dönem başı öz sermayenin üç katını "
    "(6.000.000 ₺) aşmaz.", zorluk="hard")

isat = 6_000_000 - 4_000_000 * 0.75
P.sayisal("KVK md. 5/1-e",
    "Tam mükellef (CDE) A.Ş., üç yıldır aktifinde bulunan iştirak hisselerini 2025 yılında peşin bedelle satmış ve 4.000.000 ₺ "
    "satış kazancı elde etmiştir. Şirket menkul kıymet ticaretiyle uğraşmamaktadır; istisnaya isabet eden tutarı pasifte özel "
    "fon hesabına almıştır. 2025 ticari bilanço kârı (satış kazancı dahil) 6.000.000 ₺’dir; KKEG ve zarar yoktur."
    f"\n\n{K}, (CDE) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı kaç ₺’dir?",
    tl(isat), secenekler(isat, 6_000_000 - 4_000_000, 6_000_000 - 2_000_000, 6_000_000, 6_000_000 - 3_000_000 * 0.75),
    "Md. 5/1-e'ye göre en az iki tam yıl aktifte bulunan iştirak hisselerinin satış kazancının %75'i istisnadır (3.000.000 "
    "₺); şartlardan biri de satış bedelinin satış yılını izleyen ikinci takvim yılı sonuna kadar tahsilidir, bedel peşin "
    "alınmıştır: 6.000.000 − 3.000.000 = 3.000.000 ₺.", zorluk="hard")

P.q("KVK md. 12/7",
    f"{K}, örtülü sermayenin sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Örtülü sermayeye ilişkin kur farkları da dağıtılmış kâr payı sayılır.",
    ["Örtülü sermaye üzerinden hesaplanan faizler borç alan kurumda indirilemez.",
     "Kur farkı hariç faiz ve benzeri ödemeler dağıtılmış kâr payı sayılır.",
     "Dar mükellefler için bu tutarlar ana merkeze aktarılan tutar sayılır.",
     "Dağıtım, şartların gerçekleştiği hesap döneminin son günü itibarıyla yapılmış sayılır."],
    "Md. 12/7'ye göre örtülü sermaye üzerinden kur farkı hariç faiz ve benzeri ödemeler, şartların gerçekleştiği hesap "
    "döneminin son günü itibarıyla dağıtılmış kâr payı veya ana merkeze aktarılan tutar sayılır; kur farkları bu nitelemenin "
    "dışında bırakılmıştır.", zorluk="hard")

P.q("KVK md. 12/3",
    "(ZAB) A.Ş.’nin ortağı Bay (Y), (CDE) Ltd. Şti.’nin sermayesinin %15’ine sahiptir. (ZAB) A.Ş. 2025 yılında (CDE) Ltd. "
    f"Şti.’den borç almıştır.\n\n{K}, örtülü sermaye uygulamasında ortakla ilişkili kişiye ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Ortağın en az %10 oranında ortağı olduğu kurum ortakla ilişkili kişi sayılır.",
    ["Ortakla ilişkili kişi sayılmak için en az %50 ortaklık payı gerekir.",
     "Ortakla ilişkili kişi kavramı sadece ortağın eşi ve çocuklarını kapsar.",
     "Ortakla ilişkili kişi sayılmak için kurumun oy haklarının en az %25’ine sahip olunması gerekir.",
     "Ortağın ortağı olduğu kurumlar ilişkili kişi sayılmaz."],
    "Md. 12/3-a'ya göre ortakla ilişkili kişi, ortağın doğrudan veya dolaylı olarak en az %10 oranında ortağı olduğu veya en "
    "az bu oranda oy ya da kâr payı hakkına sahip olduğu kurumdur. Bay (Y)'nin %15 payı nedeniyle (CDE) Ltd. Şti. ilişkili "
    "kişidir.")

em = 5_000_000 - 2_000_000
P.sayisal("KVK md. 5/1-ç",
    "Tam mükellef (FGH) A.Ş., 2025 yılında yaptığı sermaye artırımında itibari değeri toplam 1.000.000 ₺ olan payları 3.000.000 "
    "₺ bedelle ihraç etmiş ve itibari değeri aşan kısmı gelir hesaplarına kaydetmiştir. Bu tutar dahil 2025 ticari bilanço "
    f"kârı 5.000.000 ₺’dir; KKEG, zarar ve başka istisna yoktur.\n\n{K}, (FGH) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi "
    "matrahı kaç ₺’dir?",
    tl(em), secenekler(em, 5_000_000, 5_000_000 - 3_000_000, 5_000_000 - 1_000_000, 5_000_000 - 2_000_000 * 0.75),
    "Md. 5/1-ç'ye göre anonim şirketlerin sermaye artırımında çıkardıkları payların bedelinin itibari değeri aşan kısmı "
    "(emisyon primi, 2.000.000 ₺) istisnadır: 5.000.000 − 2.000.000 = 3.000.000 ₺.")

P.q("KVK md. 12/6",
    f"{K}, aşağıdaki borçlanmalardan hangisi örtülü sermaye sayılabilir?",
    "Ortaktan doğrudan alınan ve dönem başı öz sermayenin üç katını aşan borcun aşan kısmı",
    ["Ortağın verdiği gayrinakdi teminat karşılığında üçüncü kişiden alınan borç",
     "İştirakin bankadan temin edip aynı şartlarla kullandırdığı borç",
     "Bankacılık Kanunu’na göre faaliyette bulunan bankalar tarafından yapılan borçlanmalar",
     "Ortakla ilişkili kişinin sermaye piyasasından temin edip aynı şartlarla kullandırdığı borç"],
    "Md. 12/1'e göre ortaklardan veya ilişkili kişilerden temin edilen borçların öz sermayenin üç katını aşan kısmı örtülü "
    "sermayedir. Md. 12/6 gayrinakdi teminat karşılığı üçüncü kişi borçlarını, aynı şartlarla kullandırılan banka ve sermaye "
    "piyasası borçlarını ve bankaların kendi borçlanmalarını örtülü sermaye saymaz.")

P.q("KVK md. 13",
    f"{K}, transfer fiyatlandırması yoluyla örtülü kazanç dağıtımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Emsallere uygun fiyat, kurumun kendi belirlediği herhangi bir yöntemle tespit edilebilir.",
    ["İlişkili kişilerle emsallere aykırı fiyatla mal veya hizmet alım satımı örtülü kazanç dağıtımı sayılır.",
     "Mal veya hizmet alım satımı; kiralama, ödünç para verme, ikramiye, ücret gibi işlemleri de kapsar.",
     "Örtülü dağıtılan kazanç hesap dönemi sonu itibarıyla dağıtılmış kâr payı sayılır.",
     "Taraflar nezdinde düzeltme için örtülü kazanç dağıtan kurum adına tarh edilen vergilerin kesinleşip ödenmesi gerekir."],
    "Md. 13'e göre emsallere uygun fiyat; karşılaştırılabilir fiyat, maliyet artı, yeniden satış fiyatı yöntemlerinden işlemin "
    "mahiyetine en uygun olanıyla, bunlar uygulanamıyorsa işlemin mahiyetine uygun olarak mükellefçe belirlenecek yöntemle "
    "tespit edilir; yöntem seçimi serbest değildir.", zorluk="hard")

tf = 3_000_000 + (1_600_000 - 1_000_000)
P.sayisal("KVK md. 13",
    "Tam mükellef (IJK) A.Ş., 2025 yılında ortağının %60 oranında hissedarı olduğu ilişkili bir kuruma emsal bedeli 1.600.000 ₺ "
    "olan malı 1.000.000 ₺’ye satmıştır. Şirketin 2025 ticari bilanço kârı 3.000.000 ₺’dir; başka KKEG, istisna veya zarar "
    f"yoktur.\n\n{K}, (IJK) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı kaç ₺’dir?",
    tl(tf), secenekler(tf, 3_000_000, 3_000_000 + 1_000_000, 3_000_000 - 600_000, 3_000_000 + 1_600_000),
    "Md. 13'e göre ilişkili kişiyle emsallere aykırı bedelle yapılan işlemde kazanç transfer fiyatlandırması yoluyla örtülü "
    "dağıtılmış sayılır; aradaki 600.000 ₺ md. 11/1-c gereği kanunen kabul edilmeyen giderdir: 3.000.000 + 600.000 = "
    "3.600.000 ₺.")

P.q("KVK md. 13",
    "(FGH) A.Ş., ilişkili kişisi olan (IJK) Ltd. Şti.’ye 2025 yılında sattığı mallarda bağımsız taraflar arasında oluşacak "
    "fiyattan daha düşük bedel uygulamıştır. Mali müşavir hangi fiyat tespit yönteminin kullanılacağını "
    f"değerlendirmektedir.\n\n{K}, aşağıdakilerden hangisi Kanunda sayılan emsallere uygun fiyat tespit yöntemlerinden biri "
    "değildir?",
    "VUK’taki ortalama fiyat esası",
    ["Karşılaştırılabilir fiyat yöntemi", "Maliyet artı yöntemi", "Yeniden satış fiyatı yöntemi",
     "Mükellefçe belirlenecek diğer yöntemler"],
    "Md. 13/4'e göre emsallere uygun fiyat karşılaştırılabilir fiyat, maliyet artı ve yeniden satış fiyatı yöntemlerinden "
    "birisiyle, bunlarla belirlenemiyorsa mükellefçe belirlenecek yöntemle tespit edilir. Ortalama fiyat esası VUK'taki "
    "değerleme ölçüleriyle ilgilidir.")

P.q("KVK md. 5/1-a",
    "(LMN) A.Ş. 2025 yılında çeşitli kaynaklardan kâr payı elde etmiştir. Şirketin mali müşaviri, bu kâr paylarının hangilerine "
    f"iştirak kazançları istisnasının uygulanacağını belirlemektedir.\n\n{K}, aşağıdakilerden hangisi iştirak kazançları "
    "istisnası kapsamında değildir?",
    "Tam mükellef bir menkul kıymetler yatırım fonunun katılma paylarından elde edilen kâr payı",
    ["Tam mükellef bir anonim şirketin sermayesine katılımdan elde edilen kâr payı",
     "Tam mükellef bir kurumun kurucu senetlerinden elde edilen kâr payı",
     "Tam mükellef girişim sermayesi yatırım ortaklığının hisse senetlerinden elde edilen kâr payı",
     "Tam mükellef bir limited şirketin sermayesine katılımdan elde edilen kâr payı"],
    "Md. 5/1-a'ya göre tam mükellef kurumlara iştirakten, kurucu ve intifa senetlerinden ve girişim sermayesi yatırım fon ve "
    "ortaklıklarından elde edilen kâr payları istisnadır. Diğer yatırım fonu katılma payları ile yatırım ortaklıklarının "
    "hisse senetlerinden elde edilen kâr payları bu istisnadan yararlanamaz.", zorluk="hard")

ak1 = (60_000_000 + 4_000_000) * 0.10
P.sayisal("KVK md. 32/C",
    "Tam mükellef (LMN) A.Ş.’nin 2025 hesap dönemine ilişkin ticari bilanço kârı 60.000.000 ₺, kanunen kabul edilmeyen gideri "
    "4.000.000 ₺’dir. Şirket aynı dönemde md. 5/1-h kapsamında 50.000.000 ₺ yurt dışı inşaat ve teknik hizmet kazancı "
    "istisnasından yararlanmıştır. Şirket faaliyetine 2015 yılında başlamıştır; başka indirim ve istisna yoktur."
    f"\n\n{K}, (LMN) A.Ş.’nin 2025 hesap dönemi için ödeyeceği kurumlar vergisi kaç ₺’dir?",
    tl(ak1), secenekler(ak1, 14_000_000 * 0.25, 60_000_000 * 0.10, 14_000_000 * 0.10, 64_000_000 * 0.25),
    "Normal hesap: (60.000.000 + 4.000.000 − 50.000.000) × %25 = 3.500.000 ₺. Md. 32/C'ye göre vergi, indirim ve istisnalar "
    "düşülmeden önceki kazancın (ticari kâr + KKEG = 64.000.000 ₺) %10'undan az olamaz; md. 5/1-h istisnası asgari vergi "
    "matrahından düşülebilecekler arasında sayılmaz. Asgari vergi 6.400.000 ₺ olduğundan bu tutar ödenir.", zorluk="hard")

P.q("KVK md. 5/1-b",
    f"{K26}, yurt dışı iştirak kazançları istisnasının şartlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İştirak payının kazancın elde edildiği tarih itibarıyla en az iki yıl süreyle elde tutulması gerekir.",
    ["İştirak payını elinde tutan şirketin yurt dışı iştirakin ödenmiş sermayesinin en az %10’una sahip olması gerekir.",
     "İştirak kazancının en az %15 oranında gelir ve kurumlar vergisi benzeri toplam vergi yükü taşıması gerekir.",
     "İştirak kazancının beyannamenin verilmesi gereken tarihe kadar Türkiye’ye transfer edilmesi gerekir.",
     "Yurt dışı iştirakin anonim veya limited şirket olması gerekir."],
    "Md. 5/1-b'ye göre iştirak payının kazancın elde edildiği tarih itibarıyla kesintisiz olarak en az bir yıl süreyle elde "
    "tutulması gerekir. %10 sermaye payı, %15 vergi yükü, beyanname tarihine kadar transfer ve anonim ya da limited şirket "
    "niteliği diğer şartlardır.", zorluk="hard")

P.q("KVK md. 5/1-e",
    f"{K26}, iştirak hissesi satış kazancı istisnasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Satış bedelinin satışın yapıldığı yıl içinde tahsil edilmesi şarttır; aksi hâlde istisna uygulanmaz.",
    ["Hisselerin en az iki tam yıl süreyle aktifte bulunması gerekir.",
     "Satış kazancının %75’lik kısmı istisnadır.",
     "İstisna tutarı satışı izleyen beşinci yılın sonuna kadar pasifte özel bir fon hesabında tutulur.",
     "Menkul kıymet ticaretiyle uğraşan kurumların bu amaçla elde tuttukları değerlerin satış kazancı kapsam dışıdır."],
    "Md. 5/1-e'ye göre satış bedelinin satışın yapıldığı yılı izleyen ikinci takvim yılının sonuna kadar tahsil edilmesi "
    "şarttır; bu süre içinde tahsil edilmeyen bedele isabet eden istisna nedeniyle tahakkuk ettirilmeyen vergiler ziyaa "
    "uğramış sayılır. Diğer ifadeler maddeye uygundur.", zorluk="hard")

ak2 = (20_000_000 + 2_000_000 - 12_000_000) * 0.10
P.sayisal("KVK md. 32/C",
    "Tam mükellef (OPR) A.Ş.’nin 2025 hesap dönemi ticari bilanço kârı 20.000.000 ₺, kanunen kabul edilmeyen gideri 2.000.000 "
    "₺’dir. Kârın 12.000.000 ₺’si tam mükellef iştiraklerden alınan kâr paylarıdır. Şirket 2010’dan beri faaliyettedir; "
    f"başka indirim ve istisna yoktur.\n\n{K}, (OPR) A.Ş.’nin 2025 hesap dönemi yurt içi asgari kurumlar vergisi kaç ₺’dir?",
    tl(ak2), secenekler(ak2, 22_000_000 * 0.10, 20_000_000 * 0.10, 10_000_000 * 0.25, 8_000_000 * 0.10),
    "Md. 32/C'ye göre asgari vergi, ticari bilanço kârına KKEG eklenerek bulunan tutarın %10'udur; ancak md. 5/1-a "
    "kapsamındaki iştirak kazançları bu tutardan düşülür: (20.000.000 + 2.000.000 − 12.000.000) × %10 = 1.000.000 ₺. "
    "Normal hesaplanan vergi 2.500.000 ₺ olduğundan şirket bunu öder.", zorluk="hard")

P.q("KVK md. 5/1-e",
    "(OPR) A.Ş. 2025 yılında, 2024 Eylül ayında satın aldığı bir iştirak hissesini satmış ve kazanç elde etmiştir. Şirket menkul "
    f"kıymet ticaretiyle uğraşmamaktadır.\n\n{K}, bu satış kazancına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hisse iki tam yıl aktifte bulunmadığından satış kazancının tamamı kurum kazancına dahildir.",
    ["Satış kazancının %75’i istisnadır; istisna tutarı beş yıl özel fon hesabında tutulur.",
     "Satış kazancının %50’si istisnadır.",
     "Satış kazancı, iştirak kazançları istisnası kapsamında değerlendirildiğinden tamamen vergi dışıdır.",
     "Satış kazancı ancak fon hesabına alınırsa %75 oranında istisnadır."],
    "Md. 5/1-e'deki %75 istisnası için iştirak hisselerinin en az iki tam yıl (730 gün) süreyle aktifte bulunması gerekir. "
    "2024 Eylül'de alınıp 2025'te satılan hisse bu şartı sağlamadığından kazancın tamamı vergilendirilir.")

P.q("KVK md. 5/1-ç",
    f"{K}, emisyon primi kazancına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Anonim şirketlerde payların itibari değeri aşan ihraç bedeli istisnadır.",
    ["Limited şirketlerin sermaye artırımında ortaklardan alınan fazla bedel istisnadır.",
     "Payların itibari değerinin altında ihracından doğan zarar gider yazılabilir.",
     "Emisyon primi ticari kazanç sayılır ve vergiye tabidir.",
     "Emisyon primi istisnası sadece halka açık şirketlere uygulanır."],
    "Md. 5/1-ç'ye göre anonim şirketlerin kuruluşlarında veya sermaye artırımlarında çıkardıkları payların bedelinin itibari "
    "değeri aşan kısmı istisnadır. Md. 11/1-e'ye göre menkul kıymetlerin itibari değerin altında ihracından doğan zararlar "
    "indirilemez.", zorluk="easy")

fg = 1_200_000 * (8_000_000 - 5_000_000) / 8_000_000 * 0.10
P.sayisal("KVK md. 11/1-i",
    "İnşaat malzemeleri üreten (STU) A.Ş.’nin 2025 hesap dönemi sonunda öz kaynakları 5.000.000 ₺, kısa vadeli yabancı "
    "kaynakları 3.000.000 ₺, uzun vadeli yabancı kaynakları 5.000.000 ₺’dir. Döneme ait ve yatırım maliyetine eklenmeyen "
    "finansman giderleri 1.200.000 ₺’dir. (Cumhurbaşkanınca belirlenen oran %10 olarak alınacaktır.)"
    f"\n\n{K}, (STU) A.Ş.’nin dikkate alması gereken kanunen kabul edilmeyen gider tutarı kaç ₺’dir?",
    tl(fg), secenekler(fg, 1_200_000 * 0.10, 450_000, 1_200_000 * 3 / 5 * 0.10, 1_200_000 * 5 / 8 * 0.10),
    "Md. 11/1-i'ye göre yabancı kaynakları öz kaynaklarını aşan işletmelerde, aşan kısma isabet eden finansman giderinin "
    "%10'u indirilemez. Yabancı kaynak 8.000.000 ₺, aşan kısım 3.000.000 ₺: 1.200.000 × 3/8 = 450.000 ₺; bunun %10'u "
    "45.000 ₺'dir.", zorluk="hard")

P.q("KVK md. 32/C",
    f"{K26}, yurt içi asgari kurumlar vergisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yeni faaliyete başlayan kurumlara ilk beş hesap dönemi uygulanmaz.",
    ["Hesaplanan kurumlar vergisi, indirim ve istisnalar düşülmeden önceki kurum kazancının %10’undan az olamaz.",
     "İndirim ve istisnalar düşülmeden önceki kurum kazancı, ticari bilanço kârına KKEG eklenerek bulunur.",
     "Madde hükmü geçici vergi dönemleri için de uygulanır.",
     "Yurt içi iştirak kazançları asgari vergi matrahından düşülebilir."],
    "Md. 32/C/5'e göre ilk defa faaliyete başlayan kurumlar hakkında faaliyete başlanılan hesap döneminden itibaren üç hesap "
    "dönemi boyunca bu madde uygulanmaz. %10 oranı, ticari kâr + KKEG tanımı, geçici vergi uygulaması ve md. 5/1-a "
    "istisnasının düşülebilmesi maddede yer alır.", zorluk="hard")

P.q("KVK md. 32/C",
    "(STU) A.Ş., 2025 hesap dönemine ait kurumlar vergisi beyannamesini hazırlarken yurt içi asgari kurumlar vergisini "
    f"hesaplamaktadır.\n\n{K}, aşağıdaki istisna ve indirimlerden hangisi asgari vergi hesabında kurum kazancından "
    "düşülemez?",
    "Yurt dışı inşaat ve teknik hizmet kazancı istisnası",
    ["Tam mükellef kurumlardan elde edilen iştirak kazançları istisnası",
     "Anonim şirketlerin emisyon primi kazançları istisnası",
     "Serbest Bölgeler Kanunu kapsamında vergiden istisna edilen kazançlar",
     "Ar-Ge ve tasarım indirimleri"],
    "Md. 32/C/2'ye göre md. 5/1-a (iştirak kazancı), 5/1-ç (emisyon primi), serbest bölge ve Türk Uluslararası Gemi Sicili "
    "kazançları ile Ar-Ge ve tasarım indirimleri asgari vergi hesabında düşülür. Md. 5/1-h kapsamındaki yurt dışı inşaat "
    "kazançları bu listede yoktur.", zorluk="hard")

os_ = 900_000 * (4_500_000 - 3 * 1_000_000) / 4_500_000
P.sayisal("KVK md. 12, 11/1-b",
    "Tam mükellef (VYZ) A.Ş.’nin VUK’a göre tespit edilen 2025 hesap dönemi başı öz sermayesi 1.000.000 ₺’dir. Şirket 2025 "
    "yılında ortağı Bay (K)’dan 4.500.000 ₺ borç almış ve işletmede kullanmıştır; bu borç için yıl içinde 900.000 ₺ faiz "
    "hesaplayıp gider yazmıştır. Ortaktan veya ilişkili kişilerden başka borç yoktur."
    f"\n\n{K}, (VYZ) A.Ş.’nin örtülü sermaye nedeniyle kanunen kabul edilmeyen gider olarak dikkate alacağı faiz kaç ₺’dir?",
    tl(os_), secenekler(os_, 900_000, 600_000, 900_000 * 1 / 4.5, 900_000 * 3.5 / 4.5),
    "Md. 12'ye göre ortaktan alınan borcun dönem başı öz sermayenin üç katını (3.000.000 ₺) aşan kısmı (1.500.000 ₺) örtülü "
    "sermayedir. Bu kısma isabet eden faiz: 900.000 × 1.500.000 / 4.500.000 = 300.000 ₺; md. 11/1-b gereği indirilemez.",
    zorluk="hard")

P.q("KVK md. 32",
    f"{K26}, kurumlar vergisi oranlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sigorta şirketlerinin kurum kazançları %25 oranında vergilendirilir.",
    ["Kurumlar vergisi genel oranı %25’tir.",
     "Bankaların kurum kazançları %30 oranında vergilendirilir.",
     "Geçici vergi cari dönemin kurumlar vergisi oranında ödenir.",
     "Münhasıran ihracattan elde edilen kazançlara oran 5 puan indirimli uygulanır."],
    "Md. 32/1'e göre genel oran %25'tir; bankalar, finansman şirketleri, sermaye piyasası kurumları, sigorta ve reasürans "
    "şirketleri ile emeklilik şirketlerinde oran %30'dur. Geçici vergi cari dönem oranıyla ödenir; md. 32/7 ihracat "
    "kazançlarına 5 puan indirim öngörür.")

P.q("KVK md. 10/1-c, ç",
    "(VYZ) A.Ş. 2025 yılında bir belediyeye yaptırıp bağışladığı okul binası için 3.000.000 ₺ harcamış, ayrıca kamu yararına "
    f"çalışan bir derneğe 200.000 ₺ nakdi bağışta bulunmuştur.\n\n{K}, bu bağışların indirimine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Okul harcamasının tamamı, dernek bağışının ise kurum kazancının %5’ine kadarı indirilir.",
    ["Her iki bağış da, toplamı o yıla ait kurum kazancının %5’ine kadar olan kısmıyla indirilir.",
     "Her iki bağışın tamamı sınırsız olarak indirilir.",
     "Okul inşası harcamasının %50’si, kamu yararına çalışan derneğe yapılan bağışın ise tamamı indirilir.",
     "Bağışlar gider yazılamaz ve beyanname üzerinde de indirilemez."],
    "Md. 10/1-ç'ye göre kamu idarelerine bağışlanan okul, sağlık tesisi, yurt gibi tesislerin inşası için yapılan harcamaların "
    "tamamı indirilir. Md. 10/1-c'ye göre kamu yararına çalışan derneklere yapılan bağışlar kurum kazancının %5'ine kadar "
    "indirilebilir.")

os2 = 10_000_000 * 0.5 + 2_000_000 - 3 * 2_000_000
P.sayisal("KVK md. 12/2",
    "Tam mükellef (ABC) A.Ş.’nin 2025 hesap dönemi başı öz sermayesi 2.000.000 ₺’dir. Şirket yıl içinde ana faaliyet "
    "konusuna uygun olarak faaliyette bulunan ve ortağı olan (XBank) A.Ş.’den 10.000.000 ₺ kredi, ortağı (QRS) Ltd. "
    "Şti.’den 2.000.000 ₺ borç almıştır. (XBank) sadece ilişkili şirketlere finansman sağlayan bir kredi şirketi değildir."
    f"\n\n{K}, (ABC) A.Ş.’nin 2025 hesap dönemi için örtülü sermaye tutarı kaç ₺’dir?",
    tl(os2), secenekler(os2, 12_000_000 - 6_000_000, 0, 7_000_000, 5_000_000),
    "Md. 12/2'ye göre ortak sayılan ve ana faaliyet konusuna uygun faaliyet gösteren bankalardan yapılan borçlanmalar %50 "
    "oranında dikkate alınır: 5.000.000 + 2.000.000 = 7.000.000 ₺. Öz sermayenin üç katı 6.000.000 ₺ olduğundan aşan "
    "1.000.000 ₺ örtülü sermayedir.", zorluk="hard")

P.q("KVK md. 10",
    f"{K26}, kurum kazancından yapılan diğer indirimlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu indirimler beyannamede gösterilmeden doğrudan gider yazılarak yapılır.",
    ["Profesyonel spor dallarına yapılan sponsorluk harcamalarının %50’si indirilebilir.",
     "Amatör spor dallarına yapılan sponsorluk harcamalarının tamamı indirilebilir.",
     "Kamu yararına çalışan derneklere yapılan bağışlar kurum kazancının %5’ine kadar indirilebilir.",
     "Belediyelere bağışlanan sağlık tesisinin inşası için yapılan harcamaların tamamı indirilebilir."],
    "Md. 10/1'e göre bu indirimler kurumlar vergisi beyannamesi üzerinde ayrıca gösterilmek şartıyla, kurum kazancından "
    "sırasıyla yapılır. Sponsorluk ve bağış oranları maddeye uygundur.")

P.oncul("KVK md. 11",
    f"{K} aşağıdaki giderler değerlendirilmektedir:",
    ["Öz sermaye üzerinden hesaplanan faiz",
     "Genel kurul toplantısı için yapılan giderler",
     "Esas faaliyetle ilgisi olmayan helikopterin amortismanı",
     "Menkul kıymet ihraç giderleri"],
    "Yukarıdakilerden hangileri kurum kazancının tespitinde indirilemez?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 11/1-a'ya göre öz sermaye faizi (I) ve md. 11/1-f'ye göre esas faaliyetle ilgisiz hava taşıtlarının giderleri ve "
    "amortismanları (III) indirilemez. Genel kurul giderleri (II) ve menkul kıymet ihraç giderleri (IV) md. 8'e göre "
    "indirilebilir.")

bn = (400_000 + 60_000 + 40_000) * 0.30 + 30_000
P.sayisal("KVK md. 6, GVK md. 40/5",
    "Mobilya üreticisi (DEF) A.Ş.’nin aktifinde kayıtlı ve faaliyette kullanılan binek otomobilleri için 2025 yılında yaptığı "
    "ve gider hesaplarında izlediği harcamalar şöyledir: akaryakıt 400.000 ₺, sigorta 60.000 ₺, bakım-onarım 40.000 ₺, "
    f"motorlu taşıtlar vergisi 30.000 ₺.\n\n{K}, (DEF) A.Ş.’nin bu harcamalardan kanunen kabul edilmeyen gider olarak "
    "dikkate alacağı tutar kaç ₺’dir?",
    tl(bn), secenekler(bn, 530_000 * 0.30, 500_000 * 0.30, 30_000, 530_000 * 0.70),
    "Md. 6 gereği kurum kazancı GVK ticari kazanç hükümlerine göre bulunur. GVK md. 40/5'e göre binek otomobil giderlerinin "
    "%30'u (500.000 × %30 = 150.000 ₺) ve GVK md. 41'e göre binek otomobiller için ödenen MTV'nin tamamı (30.000 ₺) "
    "indirilemez: 180.000 ₺.")

P.q("KVK md. 11/1-g",
    "(ABC) A.Ş.’nin çalışanı, iş sırasında trafik kazasına sebep olmuş ve şirket mahkeme kararıyla zarar görene 500.000 ₺ "
    "maddi tazminat ödemiştir. Ayrıca şirket, bir tedarikçisiyle yaptığı sözleşmede ceza şartı olarak belirlenen 200.000 ₺’yi "
    f"sözleşmeyi ihlal ettiği için ödemiştir.\n\n{K26}, bu ödemelerin kurum kazancının tespitindeki durumu hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Çalışanın suçundan doğan tazminat indirilemez, ceza şartı tazminatı indirilebilir.",
    ["Her iki tazminat da işle ilgili olduğundan indirilebilir.",
     "Her iki tazminat da kanunen kabul edilmeyen gider sayılır.",
     "Çalışanın suçundan doğan tazminat indirilebilir, ceza şartı tazminatı indirilemez.",
     "Her iki tazminatın %50’si gider olarak indirilebilir."],
    "Md. 11/1-g'ye göre sözleşmelerde ceza şartı olarak konulan tazminatlar hariç olmak üzere kurumun, ortaklarının, "
    "yöneticilerinin ve çalışanlarının suçlarından doğan maddi ve manevi zarar tazminat giderleri indirilemez.", zorluk="hard")

P.q("KVK md. 11/1-i",
    "Faktoring şirketi olmayan ve yabancı kaynakları öz kaynaklarını aşan (DEF) A.Ş., 2025 yılında yatırım maliyetine "
    f"eklenmeyen finansman giderlerine katlanmıştır.\n\n{K}, finansman gideri kısıtlamasına ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Kısıtlama toplam finansman giderlerinin tamamına uygulanır.",
    ["Kredi kuruluşları ve finansal kuruluşlar kısıtlamanın kapsamı dışındadır.",
     "Yatırım maliyetine eklenen finansman giderleri kısıtlamaya konu edilmez.",
     "Kısıtlama oranı %10’u aşmamak üzere Cumhurbaşkanınca belirlenir.",
     "Kısıtlama yabancı kaynakların öz kaynakları aşan kısmına münhasırdır."],
    "Md. 11/1-i'ye göre kısıtlama, kullanılan yabancı kaynakları öz kaynaklarını aşan işletmelerde aşan kısma münhasır olmak "
    "üzere uygulanır; finansman giderlerinin tamamına değil, aşan kısma isabet eden tutara %10'u aşmayan oran uygulanır.")

al = 800_000 * 0.50
P.sayisal("KVK md. 11/1-ı",
    "İçecek sektöründe faaliyet gösteren (GHI) A.Ş. 2025 yılında alkollü içki markaları için 800.000 ₺, alkolsüz içecekleri "
    "için 600.000 ₺ ilan ve reklam gideri yapmış ve tamamını gider yazmıştır. Cumhurbaşkanı kanundaki oranı "
    f"değiştirmemiştir.\n\n{K}, (GHI) A.Ş.’nin bu giderlerden kanunen kabul edilmeyen gider olarak dikkate alacağı tutar kaç "
    "₺’dir?",
    tl(al), secenekler(al, 800_000, 1_400_000 * 0.50, 800_000 * 0.30, 1_400_000 * 0.30),
    "Md. 11/1-ı'ya göre her türlü alkol ve alkollü içkiler ile tütün ve tütün mamullerine ait ilan ve reklam giderlerinin "
    "%50'si indirilemez: 800.000 × %50 = 400.000 ₺. Alkolsüz içecek reklamları bu sınırlamaya girmez.")

P.q("KVK md. 8/1-ç",
    "Sermayesi paylara bölünmüş komandit şirket olan (GHI) Sermayesi Paylara Bölünmüş Komandit Şirketi, 2025 yılında komandite "
    f"ortağına kâr payı ödemiştir.\n\n{K}, bu kâr payının kurum kazancının tespitindeki durumu hakkında aşağıdakilerden "
    "hangisi doğrudur?",
    "Komandite ortağın kâr payı kurum kazancından indirilebilir.",
    ["Komandite ortağın kâr payı kanunen kabul edilmeyen giderdir.",
     "Komandite ortağın kâr payının %50’si indirilebilir.",
     "Komandite ortağın kâr payı iştirak kazancı istisnasına konu olur.",
     "Komandite ortağın kâr payı örtülü kazanç dağıtımı sayılır."],
    "Md. 8/1-ç'ye göre sermayesi paylara bölünmüş komandit şirketlerde komandite ortağın kâr payı kurum kazancının tespitinde "
    "indirilebilir; bu kâr payı komandite ortak nezdinde ticari kazanç olarak vergilendirilir.", zorluk="easy")

P.q("KVK md. 11/1-e",
    "(JKL) A.Ş., 2025 yılında itibari değeri 5.000.000 ₺ olan payları 4.500.000 ₺ bedelle ihraç etmiş ve ihraçla ilgili "
    f"olarak aracı kuruma 100.000 ₺ komisyon ödemiştir.\n\n{K}, bu işlemin kurum kazancının tespitindeki sonucu hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "İtibari değerin altında ihraçtan doğan zarar ile bu ihraçla ilgili komisyon indirilemez.",
    ["İtibari değerin altında ihraçtan doğan zarar indirilebilir, komisyon indirilemez.",
     "Hem zarar hem de komisyon menkul kıymet ihraç gideri olarak indirilebilir.",
     "Zararın %75’i istisna kazançlardan mahsup edilir.",
     "Komisyon indirilebilir, zarar ise emisyon primi istisnasından düşülür."],
    "Md. 11/1-e'ye göre kanunlardaki hadler saklı kalmak kaydıyla menkul kıymetlerin itibari değerlerinin altında ihracından "
    "doğan zararlar ile bu menkul kıymetlere ilişkin olarak ödenen komisyonlar ve benzeri giderler indirilemez.", zorluk="hard")

ihr = 4_000_000 * 0.20 + 2_000_000 * 0.25
P.sayisal("KVK md. 32/7",
    "Dış ticaretle uğraşan ve sanayi sicil belgesi bulunmayan (JKL) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı "
    "6.000.000 ₺’dir. Bu matrahın 4.000.000 ₺’si münhasıran ihracattan, 2.000.000 ₺’si yurt içi satışlardan elde edilmiştir. "
    f"Şirket halka açık değildir; başka indirimli oran uygulaması yoktur.\n\n{K}, (JKL) A.Ş.’nin 2025 hesap dönemi "
    "kurumlar vergisi kaç ₺’dir?",
    tl(ihr), secenekler(ihr, 6_000_000 * 0.25, 6_000_000 * 0.20, 4_000_000 * 0.24 + 2_000_000 * 0.25, 4_000_000 * 0.25 + 2_000_000 * 0.20),
    "Md. 32/7'ye göre ihracat yapan kurumların münhasıran ihracattan elde ettikleri kazançlara kurumlar vergisi oranı 5 puan "
    "indirimli uygulanır: 4.000.000 × %20 + 2.000.000 × %25 = 800.000 + 500.000 = 1.300.000 ₺.", zorluk="hard")

P.q("KVK md. 12/3-b",
    f"{K}, örtülü sermaye hesabında öz sermayeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurumun VUK’a göre tespit edilen dönem başı öz sermayesi esas alınır.",
    ["Karşılaştırmada hesap dönemi sonundaki öz sermaye esas alınır.",
     "Karşılaştırmada hesap dönemi içindeki ortalama öz sermaye esas alınır.",
     "Karşılaştırmada ödenmiş sermaye esas alınır, yedekler dikkate alınmaz.",
     "Karşılaştırmada TFRS’ye göre hazırlanan finansal tablolardaki öz kaynak esas alınır."],
    "Md. 12/3-b'ye göre öz sermaye, kurumun Vergi Usul Kanunu uyarınca tespit edilmiş hesap dönemi başındaki öz sermayesidir; "
    "borçların bu tutarın üç katını hesap dönemi içinde herhangi bir tarihte aşan kısmı örtülü sermayedir.", zorluk="easy")

P.q("KVK md. 5/1-b",
    "(MNO) A.Ş., Almanya’daki (PQR) GmbH’nin ödenmiş sermayesinin %60’ına sahiptir. (PQR) GmbH’nin kazançları %15’in altında "
    "vergi yükü taşımaktadır. (MNO) A.Ş. 2025 yılında aldığı kâr payını beyanname verme süresi içinde Türkiye’ye transfer "
    f"etmiştir.\n\n{K26}, bu kâr payının vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi yükü şartı aranmaksızın kâr payının %50’si istisnadır.",
    ["Vergi yükü şartı sağlanmadığından kâr payının tamamı vergilendirilir.",
     "Kâr payının tamamı iştirak kazancı istisnasına konu olur.",
     "Kâr payının %75’i istisnadır.",
     "Kâr payı sadece Almanya’da vergilendirilir."],
    "Md. 5/1-b'ye 7491 sayılı Kanunla eklenen hükme göre yurt dışı iştirakin ödenmiş sermayesinin en az %50'sine sahip olunması "
    "ve kazancın beyanname verme süresine kadar Türkiye'ye transfer edilmesi şartıyla, diğer şartlar aranmaksızın iştirak "
    "kazancının %50'si istisnadır.", zorluk="hard")

ha = 10_000_000 * 0.23
P.sayisal("KVK md. 32/6",
    "Payları 2025 yılında Borsa İstanbul Pay Piyasasında ilk defa işlem görmek üzere %25 oranında halka arz edilen üretici "
    "(MNO) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı 10.000.000 ₺’dir. Şirket banka, finans veya sigorta "
    "kuruluşu değildir. Başka indirimli oran uygulaması dikkate alınmayacaktır."
    f"\n\n{K}, (MNO) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi kaç ₺’dir?",
    tl(ha), secenekler(ha, 10_000_000 * 0.25, 10_000_000 * 0.20, 10_000_000 * 0.24, 10_000_000 * 0.22),
    "Md. 32/6'ya göre payları ilk defa en az %20 oranında halka arz edilen kurumların kazançlarına, halka arz edildiği "
    "dönemden başlamak üzere beş hesap dönemi boyunca kurumlar vergisi oranı 2 puan indirimli uygulanır: 10.000.000 × %23 = "
    "2.300.000 ₺.")

P.q("KVK md. 5/1-d",
    f"{K}, aşağıdakilerden hangisinin kazancı kurumlar vergisinden istisna edilmemiştir?",
    "Türkiye’de kurulu bir anonim şirketin menkul kıymet alım satımından elde ettiği kazanç",
    ["Türkiye’de kurulu menkul kıymetler yatırım fonunun portföy işletmeciliği kazancı",
     "Türkiye’de kurulu emeklilik yatırım fonunun kazancı",
     "Türkiye’de kurulu girişim sermayesi yatırım ortaklığının kazancı",
     "Türkiye’de kurulu konut finansmanı fonunun kazancı"],
    "Md. 5/1-d'ye göre Türkiye'de kurulu menkul kıymetler yatırım fon ve ortaklıklarının portföy işletmeciliği kazançları, "
    "girişim sermayesi, emeklilik, konut finansmanı ve varlık finansmanı fonlarının kazançları istisnadır. Olağan bir anonim "
    "şirketin menkul kıymet alım satım kazancı ticari kazançtır.")

P.q("KVK md. 9",
    "(STU) A.Ş., 2025 hesap döneminde kâr etmiştir. Şirketin yurt dışındaki şubesinin 2024 yılında uğradığı ve o ülke "
    "mevzuatına göre denetim raporuna bağlanan zararı bulunmaktadır; şubenin kazançları Türkiye’de kurumlar vergisinden "
    f"istisna değildir.\n\n{K}, bu yurt dışı zararın mahsubuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Denetim raporu ve tercümesi ibraz edilirse beş yılı aşmamak üzere mahsup edilebilir.",
    ["Yurt dışı zararlar Türkiye’deki kazançtan mahsup edilemez.",
     "Yurt dışı zararlar sadece aynı ülkedeki kazançlardan mahsup edilebilir.",
     "Yurt dışı zararlar, rapora bağlanmış olmaları kaydıyla süre sınırı olmaksızın mahsup edilebilir.",
     "Yurt dışı zararlar ancak Türkiye’de de zarar varsa mahsup edilebilir."],
    "Md. 9/1-b'ye göre Türkiye'de istisna edilen kazançlarla ilgili olanlar hariç yurt dışı faaliyet zararları, beş yıldan fazla "
    "nakledilmemek şartıyla ve o ülke mevzuatına göre yetkili kuruluşlarca rapora bağlanıp raporun aslı ve tercümesi vergi "
    "dairesine ibraz edilirse indirilir.", zorluk="hard")

gv = 3_200_000 * 0.25 - 650_000
P.sayisal("KVK md. 32/2, 34",
    "Tam mükellef (PRS) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı 3.200.000 ₺’dir. Şirket yıl içinde toplam 650.000 "
    "₺ geçici kurumlar vergisi ödemiştir. Kesinti yoluyla ödenen vergi ve asgari vergi farkı bulunmamaktadır; genel oran "
    f"uygulanacaktır.\n\n{K}, (PRS) A.Ş.’nin 2025 hesap dönemi beyannamesi üzerine ödeyeceği kurumlar vergisi kaç ₺’dir?",
    tl(gv), secenekler(gv, 3_200_000 * 0.25, 3_200_000 * 0.20 - 650_000, 3_200_000 * 0.25 + 650_000, 650_000, 3_200_000 * 0.30 - 650_000),
    "Kurumlar vergisi 3.200.000 × %25 = 800.000 ₺'dir. Md. 32/2'ye göre geçici vergi cari dönemin kurumlar vergisine mahsup "
    "edilir: 800.000 − 650.000 = 150.000 ₺.", zorluk="easy")

P.q("KVK md. 32/C",
    "(VYZ) A.Ş. 2024 yılında kurulmuş ve aynı yıl faaliyete başlamıştır. Şirketin 2025 hesap döneminde hesaplanan kurumlar "
    f"vergisi, indirim ve istisnalar öncesi kazancının %10’unun altında kalmıştır.\n\n{K}, (VYZ) A.Ş. hakkında yurt içi "
    "asgari kurumlar vergisi uygulamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Faaliyete başlanılan hesap döneminden itibaren üç hesap dönemi uygulanmadığından 2025’te asgari vergi hesaplanmaz.",
    ["Asgari vergi 2025’te uygulanır; ilk yıl muafiyeti sadece 2024 için geçerlidir.",
     "Asgari vergi yeni kurulan şirketlere süresiz olarak uygulanmaz.",
     "Asgari vergi ancak geçici vergi dönemlerinde uygulanır, yıllık beyanda uygulanmaz.",
     "Asgari vergi uygulanır ancak oran %5 olarak dikkate alınır."],
    "Md. 32/C/5'e göre ilk defa faaliyete başlayan kurumlar hakkında faaliyete başlanılan hesap döneminden itibaren üç hesap "
    "dönemi boyunca (2024, 2025, 2026) bu madde uygulanmaz.", zorluk="hard")

P.q("KVK md. 13/7",
    "(ABC) A.Ş., ilişkili kişisi (DEF) A.Ş.’ye emsal bedelin altında mal satmış ve vergi incelemesi sonucunda adına "
    f"tarh edilen vergiler kesinleşerek ödenmiştir.\n\n{K}, bu durumda taraflar nezdinde yapılacak işlem hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Daha önce yapılan vergilendirme işlemleri taraf olan mükellefler nezdinde düzeltilir.",
    ["Alıcı kurum nezdinde düzeltme yapılamaz.",
     "Düzeltme vergilerin kesinleşmesi beklenmeden yapılmalıdır.",
     "Örtülü kazanç ticari kazanç sayılır, kâr payı sayılmaz.",
     "Düzeltme için alıcı kurumun da ayrıca inceleme talep etmesi şarttır."],
    "Md. 13/7'ye göre transfer fiyatlandırması yoluyla örtülü dağıtılan kazanç, dağıtılmış kâr payı veya ana merkeze aktarılan "
    "tutar sayılır; örtülü kazanç dağıtan kurum adına tarh edilen vergilerin kesinleşmiş ve ödenmiş olması şartıyla taraflar "
    "nezdinde düzeltme yapılır.")

gz = 1_000_000 - 1_000_000
P.sayisal("KVK md. 9",
    "(TUV) A.Ş.’nin 2025 hesap dönemi zarar mahsubu öncesi kurum kazancı 1.000.000 ₺’dir. Şirketin beyannamelerinde yıllar "
    "itibarıyla ayrı gösterilmiş geçmiş yıl zararları şöyledir: 2021 yılı 700.000 ₺, 2022 yılı 600.000 ₺. Bu zararlardan önceki "
    f"yıllarda hiç mahsup yapılmamıştır.\n\n{K}, (TUV) A.Ş.’nin 2026 hesap dönemine devredecek mahsup edilmemiş zararı kaç "
    "₺’dir?",
    tl(300_000), secenekler(300_000, 0, 600_000, 1_300_000, 700_000),
    "Md. 9'a göre beş yıldan fazla nakledilmemek şartıyla geçmiş yıl zararları indirilir; 2021 ve 2022 zararları 2025'te "
    "mahsup edilebilir. 1.000.000 ₺ kazançtan önce 2021 zararı (700.000 ₺), sonra 2022 zararının 300.000 ₺'si düşülür; "
    "2022 zararından kalan 300.000 ₺ sonraki döneme devreder (2027'ye kadar).", zorluk="hard")

P.q("KVK md. 8",
    "Yeni kurulan (FGH) A.Ş.’nin ilk hesap döneminde yaptığı harcamaların vergisel niteliği incelenmektedir. Mali müşavir, "
    f"bazı giderlerin Kanunun özel hükmüyle ayrıca indirilebildiğini belirtmiştir.\n\n{K}, aşağıdakilerden hangisi kurum "
    "kazancından indirilebilir?",
    "Kuruluş ve örgütlenme giderleri",
    ["Kurucu ortaklara sermayeleri için hesaplanan faiz",
     "Kuruluş aşamasında kesilen vergi ziyaı cezası",
     "Kuruluş işlemleri gecikmeli yapıldığı için ödenen gecikme faizi",
     "Esas faaliyetle ilgisiz olarak kiralanan teknenin giderleri"],
    "Md. 8/1-b'ye göre kuruluş ve örgütlenme giderleri kurum kazancından indirilebilir. Öz sermaye faizi, vergi cezaları, "
    "gecikme faizleri ve esas faaliyetle ilgisiz deniz taşıtlarının giderleri md. 11 gereği indirilemez.", zorluk="easy")

P.q("KVK md. 11/1-d",
    "(IJK) A.Ş.’nin 2025 yılında ödediği ve gider hesaplarına kaydettiği vergi, ceza ve faizler şunlardır: 2024 yılı kurumlar "
    "vergisi, bir vergi ziyaı cezası, 6183 sayılı Kanuna göre hesaplanan gecikme zammı, VUK’a göre ödenen gecikme faizi ve "
    f"sözleşmelere ait damga vergisi.\n\n{K}, bunlardan hangisi kurum kazancının tespitinde gider olarak indirilebilir?",
    "Sözleşmelere ait damga vergisi",
    ["2024 yılına ait kurumlar vergisi", "Vergi ziyaı cezası", "6183 sayılı Kanuna göre hesaplanan gecikme zammı",
     "VUK’a göre ödenen gecikme faizi"],
    "Md. 11/1-d'ye göre kurumlar vergisi, her türlü para ve vergi cezaları, 6183 sayılı Kanuna göre ödenen gecikme zamları ve "
    "VUK'a göre ödenen gecikme faizleri indirilemez. İşletmeyle ilgili damga vergisi GVK md. 40 kapsamında gider yazılır.")

kv3 = (3_000_000 + 200_000 - 400_000 - 300_000) * 0.25
P.sayisal("KVK md. 5/1-a, 9, 32",
    "Tam mükellef (WXY) A.Ş.’nin 2025 hesap dönemi ticari bilanço kârı 3.000.000 ₺’dir. Kârın 400.000 ₺’si tam mükellef bir "
    "kurumdan alınan kâr payıdır; gider hesaplarında 200.000 ₺ kanunen kabul edilmeyen gider bulunmaktadır. Beyannamelerde "
    "ayrı gösterilen 2023 yılı zararı 300.000 ₺’dir. Şirket genel orana tabidir ve asgari vergi farkı çıkmamaktadır."
    f"\n\n{K}, (WXY) A.Ş.’nin 2025 hesap dönemi için hesaplanan kurumlar vergisi kaç ₺’dir?",
    tl(kv3), secenekler(kv3, 3_200_000 * 0.25, 2_800_000 * 0.25, 3_000_000 * 0.25, 2_900_000 * 0.25),
    "Matrah: 3.000.000 + 200.000 − 400.000 − 300.000 = 2.500.000 ₺. Kurumlar vergisi: 2.500.000 × %25 = 625.000 ₺.")

P.q("KVK md. 32/C/6",
    "(LMN) A.Ş.’nin mali müşaviri 2025 hesap dönemi için yurt içi asgari kurumlar vergisini hesaplamaktadır. Kanunda "
    "“indirim ve istisnalar düşülmeden önceki kurum kazancı” ibaresinin tanımlandığını belirtmiştir."
    f"\n\n{K}, bu ibare aşağıdakilerden hangisini ifade eder?",
    "Ticari bilanço kârı ile KKEG toplamı",
    ["Beyan edilen kurumlar vergisi matrahı ile geçmiş yıl zararlarının toplamı",
     "Ticari bilanço kârından iştirak kazançlarının düşülmesiyle bulunan tutar",
     "Hasılattan satışların maliyetinin düşülmesiyle bulunan brüt satış kârı",
     "Dağıtılan kâr payları ile ayrılan yedek akçelerin toplamı"],
    "Md. 32/C/6'ya göre indirim ve istisnalar düşülmeden önceki kurum kazancı, hesap dönemi sonundaki ticari bilanço kârına "
    "kanunen kabul edilmeyen giderlerin eklenmesiyle bulunan tutardır.")

P.q("KVK md. 12/2",
    "(OPR) A.Ş.’nin 2025 yılındaki borçlanmaları örtülü sermaye yönünden incelenmektedir. Şirketin ortakları arasında bir "
    f"banka ve sadece ilişkili şirketlere finansman sağlayan bir kredi şirketi bulunmaktadır.\n\n{K}, aşağıdakilerden hangisi "
    "örtülü sermaye karşılaştırmasında %50 oranında dikkate alınır?",
    "Ortak sayılan bankadan alınan kredi",
    ["Sadece ilişkili şirketlere finansman temin eden ortak kredi şirketinden alınan borç",
     "Ortağın gayrinakdi teminatıyla üçüncü kişiden alınan borç",
     "Ortak olan gerçek kişiden doğrudan alınan borç",
     "İştirakin sermaye piyasasından temin edip aynı şartlarla kullandırdığı borç"],
    "Md. 12/2'ye göre sadece ilişkili şirketlere finansman temin eden kredi şirketleri hariç, ana faaliyet konusuna uygun "
    "faaliyet gösteren ve ortak sayılan bankalardan yapılan borçlanmalar %50 oranında dikkate alınır. Ortaktan doğrudan borç "
    "tam dikkate alınır; gayrinakdi teminatlı ve aynı şartlarla kullandırılan borçlar hiç dikkate alınmaz.", zorluk="hard")

tf2 = 1_000_000 + (2_000_000 - 1_500_000)
P.sayisal("KVK md. 13",
    "Tam mükellef (ZAB) A.Ş., 2025 yılında ilişkili kişisi olan yurt dışındaki ana şirketinden emsal bedeli 1.500.000 ₺ olan "
    "malları 2.000.000 ₺’ye satın almış ve bu malların tamamını aynı yıl satarak maliyetini satılan malın maliyetine "
    "almıştır. Şirketin 2025 ticari bilanço kârı 1.000.000 ₺’dir; başka düzeltme yoktur."
    f"\n\n{K}, (ZAB) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı kaç ₺’dir?",
    tl(tf2), secenekler(tf2, 1_000_000, 1_000_000 + 2_000_000, 1_000_000 - 500_000, 1_000_000 + 1_500_000),
    "Md. 13'e göre ilişkili kişiden emsal bedelin üzerinde yapılan alımda aradaki 500.000 ₺ transfer fiyatlandırması yoluyla "
    "örtülü dağıtılmış kazançtır ve md. 11/1-c gereği matraha eklenir: 1.000.000 + 500.000 = 1.500.000 ₺.")

P.q("KVK md. 11/1-f",
    "Tekstil üreticisi (STU) A.Ş., yöneticilerinin tatil amaçlı kullandığı bir yatı aktifinde kayıtlı tutmakta; ayrıca turizm "
    "işletmecisi olan iştiraki (VYZ) A.Ş. esas faaliyeti kapsamında müşterilerine kiraladığı tekneleri aktifinde "
    f"bulundurmaktadır.\n\n{K26}, bu taşıtların giderlerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tekstil şirketinin yat giderleri indirilemez; turizm şirketinin tekne giderleri indirilebilir.",
    ["Her iki şirketin deniz taşıtı giderleri de indirilemez.",
     "Her iki şirketin deniz taşıtı giderlerinin %70’i indirilebilir.",
     "Tekstil şirketinin yat giderleri indirilebilir; turizm şirketinin tekne giderleri indirilemez.",
     "Deniz taşıtlarının giderleri indirilebilir, amortismanları indirilemez."],
    "Md. 11/1-f'ye göre kiralama yoluyla edinilen veya işletmede kayıtlı yat, tekne ve benzeri deniz taşıtları ile hava "
    "taşıtlarından işletmenin esas faaliyet konusu ile ilgili olmayanların giderleri ve amortismanları indirilemez; esas "
    "faaliyetle ilgili olanlar indirilebilir.", zorluk="hard")

okf = (500_000 + 300_000) * 0.40
P.sayisal("KVK md. 11/1-b, 12",
    "Tam mükellef (CDE) A.Ş.’nin 2025 yılında ortağından aldığı döviz cinsinden borcun, dönem başı öz sermayenin üç katını "
    "aşması nedeniyle %40’ının örtülü sermaye olduğu tespit edilmiştir. Şirket bu borç için yıl içinde 500.000 ₺ faiz ve "
    f"300.000 ₺ kur farkı gideri yazmıştır.\n\n{K}, (CDE) A.Ş.’nin örtülü sermaye nedeniyle kanunen kabul edilmeyen gider "
    "olarak dikkate alacağı tutar kaç ₺’dir?",
    tl(okf), secenekler(okf, 500_000 * 0.40, 800_000, 500_000, 300_000 * 0.40),
    "Md. 11/1-b'ye göre örtülü sermaye üzerinden ödenen veya hesaplanan faiz, kur farkları ve benzeri giderler indirilemez; "
    "örtülü sermayeye isabet eden kısım: (500.000 + 300.000) × %40 = 320.000 ₺. Kur farkının dağıtılmış kâr payı sayılmaması "
    "(md. 12/7) indirilememesini değiştirmez.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
