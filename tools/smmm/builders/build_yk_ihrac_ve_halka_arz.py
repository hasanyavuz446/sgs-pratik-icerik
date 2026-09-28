# -*- coding: utf-8 -*-
"""SPK Mevzuatı · İhraç ve Halka Arz — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · 6362 s. Sermaye Piyasası Kanunu m. 4-11, 16, 18, 23-28, 33
  · İzahname ve İhraç Belgesi Tebliği (II-5.1), Sermaye Piyasası Araçlarının Satışı Tebliği (II-5.2)
  · Önemli Nitelikteki İşlemler ve Ayrılma Hakkı Tebliği (II-23.3), Birleşme ve Bölünme Tebliği (II-23.2)
Yeniden değerlenen TL tutarları (muafiyet limitleri) sorulmaz.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_ihrac_ve_halka_arz_2026.json", lesson="sermaye_piyasasi_ve_finans", topic="ihrac_ve_halka_arz",
          konu_adi="İhraç ve Halka Arz", seed=2026092826,
          surum="6362 s. Kanun; II-5.1, II-5.2, II-23.2 ve II-23.3 Tebliğleri güncel metinleri; 28.09.2026 kontrolü")

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"
IZ = "İzahname ve İhraç Belgesi Tebliği (II-5.1)’ne göre"
ST = "Sermaye Piyasası Araçlarının Satışı Tebliği (II-5.2)’ne göre"
ON = "Önemli Nitelikteki İşlemler ve Ayrılma Hakkı Tebliği (II-23.3)’ne göre"
BB = "Birleşme ve Bölünme Tebliği (II-23.2)’ne göre"

# ================================================================ izahname: Kanun (m. 4-11)
P.q("6362 s. SPKn m. 4-6",
    f"{K}, izahnameye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İzahnamenin onaylanması, içindeki bilgilerin doğruluğunun Kurulca tekeffülü anlamına gelir.",
    ["Sermaye piyasası araçlarının halka arzı veya borsada işlem görmesi için izahname onayı zorunludur.",
     "İzahnameden sorumlu gerçek kişilerin isimleri ve görevleri izahnamede açıkça belirtilir.",
     "İzahname, özet bölümü de içermek üzere bir veya birden fazla belge şeklinde düzenlenebilir.",
     "İzahname ayrı belgelerden oluşuyorsa her bir belge ayrıca onaylanır."],
    "Kanun m. 4'e göre halka arz veya borsada işlem görme için izahnamenin Kurulca onaylanması zorunludur; sorumluların isimleri "
    "izahnamede belirtilir ve izahname birden fazla belgeden oluşabilir. m. 6'ya göre her belge ayrıca onaylanır; onay, "
    "bilgilerin doğruluğunun Kurulca tekeffülü veya araca ilişkin tavsiye anlamına gelmez.", zorluk="easy")

P.sayisal("6362 s. SPKn m. 6/2",
    "Payları ilk kez halka arz edilecek bir anonim ortaklık, Kurul düzenlemelerine uygun izahname ve gerekli tüm belgeleri "
    f"Kurula sunmuştur. {K}, bu başvuru belgelerin sunulmasından itibaren kaç iş günü içinde karara bağlanır?",
    "20", ["5", "10", "30", "60"],
    "Kanun m. 6/2'ye göre izahname onay başvurusu belgelerin sunulmasından itibaren on iş günü içinde karara bağlanır; ilk "
    "halka arzlarda bu süre yirmi iş günüdür. Eksiklik varsa m. 6/3'e göre süre eksiklerin sunulduğu tarihten itibaren işler.")

P.q("6362 s. SPKn m. 6",
    f"{K}, izahnamenin onaylanması sürecine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eksik başvurularda karar süresi, eksikler tamamlansa da ilk başvuru tarihinden işlemeye devam eder.",
    ["Onay başvurusu, belgelerin sunulmasından itibaren on iş günü içinde karara bağlanır.",
     "Başvuruda eksiklik varsa başvuru sahibi başvurudan itibaren on iş günü içinde bilgilendirilir.",
     "Kurul, bilgilerin tutarlı, anlaşılabilir ve standartlara göre eksiksiz olduğunu tespit ederse onay verir.",
     "Onaylanmayan başvurular gerekçesi belirtilerek ilgilisine bildirilir."],
    "Kanun m. 6'ya göre başvuru on iş günü (ilk halka arzda yirmi iş günü) içinde karara bağlanır; eksiklik varsa başvuru sahibi "
    "on iş günü içinde bilgilendirilir ve karar süreleri eksik belgelerin sunulduğu tarihten itibaren işlemeye başlar. Onay, "
    "tutarlılık ve eksiksizlik tespitine bağlıdır; ret gerekçeli bildirilir.")

P.q("6362 s. SPKn m. 7",
    f"{K}, izahnamenin yayımlanmasına ve ilan ve reklamlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İzahnamenin tamamı ticaret siciline tescil ve TTSG’de ilan edilir.",
    ["İzahname onaylandıktan sonra Kurulca belirlenecek esaslara göre yayımlanır.",
     "İzahnamenin nerede yayımlandığı ticaret siciline tescil ve TTSG’de ilan edilir.",
     "İzahname, onaylanmadan önce Kurulca belirlenecek esaslara göre ilan edilebilir.",
     "İhraca ilişkin ilan ve reklamlar izahname ile tutarlı olmalıdır."],
    "Kanun m. 7'ye göre izahname onaylandıktan sonra Kurulca belirlenen esaslara göre yayımlanır; ayrıca ticaret siciline "
    "tescil ve TTSG'de ilan edilmez, yalnızca nerede yayımlandığı tescil ve ilan edilir. Onaydan önce ilan mümkündür; ilan ve "
    "reklamlar izahnameyle tutarlı, gerçeğe uygun ve yanıltıcı olmayan nitelikte olmalıdır.")

P.sayisal("6362 s. SPKn m. 8/3",
    "Halka arz sürecinde ihraççı aleyhine önemli bir dava açılmış ve ihraççı durumu derhâl Kurula bildirmiştir. "
    f"{K}, izahnamede değiştirilecek veya yeni eklenecek hususlar bildirim tarihinden itibaren kaç iş günü içinde onaylanır?",
    "7", ["2", "5", "10", "15"],
    "Kanun m. 8'e göre satıştan önce veya satış süresince yatırım kararını etkileyebilecek değişiklikler derhâl Kurula bildirilir, "
    "satış durdurulabilir; değiştirilecek veya eklenecek hususlar bildirimden itibaren yedi iş günü içinde onaylanıp yayımlanır. "
    "Önceden talepte bulunanlar yayımdan itibaren iki iş günü içinde taleplerini geri alabilir.")

P.q("6362 s. SPKn m. 8",
    "Bir halka arzın talep toplama süreci devam ederken ihraççının en büyük müşterisiyle olan sözleşmesi feshedilmiştir. "
    f"{K}, bu duruma ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Değişiklikten önce talepte bulunan yatırımcıların taleplerini geri alma hakkı yoktur.",
    ["Durum ihraççı veya halka arz eden tarafından en uygun haberleşme vasıtasıyla derhâl Kurula bildirilir.",
     "Değişiklik gerektiren bu durum nedeniyle satış süreci durdurulabilir.",
     "İzahnameye eklenecek hususlar onaylandıktan sonra izahname gibi yayımlanır.",
     "Taleplerin geri alınma süresi, ek ve değişikliklerin yayımlanmasından itibaren hesaplanır."],
    "Kanun m. 8'e göre yatırım kararını etkileyebilecek yeni hususlar derhâl Kurula bildirilir, satış süreci durdurulabilir, "
    "değişiklikler onaylanıp yayımlanır. Yayımdan önce talepte bulunmuş yatırımcılar ek ve değişikliklerin yayımlanmasından "
    "itibaren iki iş günü içinde taleplerini geri alma hakkına sahiptir.")

P.q("6362 s. SPKn m. 9; II-5.1 m. 17",
    f"{K}, izahnamenin geçerlilik süresine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "On iki aylık süre içinde yapılan her halka arzda izahnamenin tümü yeniden onaylanır.",
    ["İzahname ilk yayım tarihinden itibaren on iki ay boyunca yapılacak ihraçlar için geçerlidir.",
     "Geçerlilik süresi içinde ek ve değişikliklerin onaylanıp ilan edilmesi yeterlidir.",
     "Süre geçtikten sonraki halka arzlarda izahnamenin tümünün onaylanması gerekir.",
     "Çok belgeli izahnamede geçerlilik, ihraççı bilgi dokümanının ilk yayımıyla başlar."],
    "Kanun m. 9'a göre izahname ilk yayımından itibaren on iki ay boyunca yapılacak ihraçlar için geçerlidir ve bu sürede ek ve "
    "değişikliklerin onaylanıp ilan edilmesi yeterlidir; süre geçtikten sonra tümünün onaylanması gerekir. Tebliğ m. 17'ye göre "
    "çok belgeli izahnamede süre ihraççı bilgi dokümanının ilk yayımıyla başlar.")

P.q("6362 s. SPKn m. 10",
    "Halka arz edilen payların izahnamesindeki finansal bilgilerin yanıltıcı olduğu anlaşılmış ve yatırımcılar zarara uğramıştır. "
    f"{K}, bu zarardan sorumluluğa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Önce ihraççı sorumludur; ondan tazmin edilemeyen zarardan diğerleri kusurlarına göre sorumludur.",
    ["Halka arz eden, ihraççıdan önce ve kusuru aranmaksızın sorumludur.",
     "Lider aracı kurum, ihraççı ile birlikte kusur aranmaksızın müteselsilen sorumludur.",
     "İzahnameyi onaylayan Kurul, ihraççıyla birlikte sorumludur.",
     "Bağımsız denetim kuruluşu, kendi raporu dışında izahnamedeki tüm bilgilerden de sorumludur."],
    "Kanun m. 10'a göre izahnamedeki yanlış, yanıltıcı ve eksik bilgilerden doğan zarardan ihraççı sorumludur; zarar ondan "
    "tazmin edilemez veya edilemeyeceği açıkça belli olursa halka arz edenler, lider aracı kurum, varsa garantör ve yönetim "
    "kurulu üyeleri kusurlarına göre sorumludur. Rapor hazırlayanlar kendi raporlarıyla sınırlı sorumludur.")

P.q("6362 s. SPKn m. 11",
    "Bir şirket, borçlanma araçlarını halka arz etmeksizin belirli kurumsal yatırımcılara satmak istemektedir. "
    f"{K}, bu ihraca ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İhraç belgesi Kurul onayına tabi değildir; Kurula bildirilmesi yeterlidir.",
    ["Halka arz edilmeksizin ihraçta ihraç belgesi hazırlanması zorunludur.",
     "İhraç belgesi araçların niteliği ve satış şartları hakkında bilgileri içerir.",
     "Kurul gerekli gördüğü hâllerde ihraç belgesinin kamuya duyurulmasına ilişkin esas belirleyebilir.",
     "İhraç belgesindeki yanlış bilgilerden sorumlulukta kamuyu aydınlatma belgelerine ilişkin hüküm uygulanır."],
    "Kanun m. 11'e göre halka arz edilmeksizin ihraçta araçların niteliği ve satış şartlarını içeren ihraç belgesinin hazırlanması "
    "ve Kurulca onaylanması zorunludur; Kurul kamuya duyuru esaslarını belirleyebilir ve ihraç belgesinden doğan sorumlulukta "
    "m. 32 uygulanır.")

# ================================================================ İzahname ve İhraç Belgesi Tebliği (II-5.1)
P.q("II-5.1 m. 6",
    f"{IZ}, aşağıdaki durumların hangisinde izahname hazırlanması gerekir?",
    "Payların ilk defa halka arzında, satış bedeli ne olursa olsun",
    ["Kâr payının pay olarak dağıtımı dahil bedelsiz paylar çıkarılması",
     "Sermaye piyasası araçlarının sadece nitelikli yatırımcılara satışı",
     "Sermayeyi değiştirmeyecek şekilde payların birleştirilmesi veya bölünmesi",
     "Sermaye piyasası araçlarının tahsisli satışı"],
    "Tebliğ m. 6/2'ye göre bedelsiz pay ihracında, sadece nitelikli yatırımcıya ve tahsisli satışta, sermayeyi değiştirmeyen "
    "pay birleştirme veya bölünmesinde izahname hazırlanmaz. m. 6/3'teki düşük tutarlı ihraç muafiyeti payların ilk halka "
    "arzını kapsamaz; ilk halka arzda izahname zorunludur.", zorluk="hard")

P.sayisal("II-5.1 m. 10/1",
    f"{IZ}, ortaklık hakkı veren sermaye piyasası araçlarına ilişkin hazırlanan izahnamede, bağımsız denetimden ve/veya sınırlı "
    "incelemeden geçirilmiş son kaç yıla ait finansal tablolara yer verilmesi esastır?",
    "3", ["1", "2", "4", "5"],
    "Tebliğ m. 10/1'e göre ortaklık hakkı veren araçların izahnamesinde son üç yıla ve varsa ilgili ara döneme, ortaklık hakkı "
    "vermeyen araçların (varant ve sertifikalar dahil) izahnamesinde son iki yıla ve varsa ara döneme ait bağımsız denetimden "
    "geçmiş finansal tablolar yer alır.")

P.q("II-5.1 m. 11/1-a",
    "Halka açık olmayan bir ortaklığın payları, Gelişen İşletmeler Piyasası dışında işlem görmek üzere ilk defa halka arz "
    f"edilecek ve satış 20 Mart tarihinde başlayacaktır. {IZ}, izahnamede yer alacak finansal tablolar aşağıdakilerden hangisidir?",
    "Son üç yıllık finansal tablolar",
    ["Son üç yıllık ve üç aylık ara dönem finansal tablolar",
     "Son iki yıllık finansal tablolar",
     "Son üç yıllık ve dokuz aylık ara dönem finansal tablolar",
     "Son yıllık ve altı aylık ara dönem finansal tablolar"],
    "Tebliğ m. 11/1-a'daki tabloya göre ilk halka arzlarda satış dönemi 16 Şubat - 15 Mayıs arasında ise son üç yıllık finansal "
    "tablolar; 16 Mayıs - 15 Ağustos arasında son üç yıllık ve üç aylık ara dönem; 1 Ocak - 15 Şubat ile 16 Kasım - 31 Aralık "
    "arasında dokuz aylık ara dönem tabloları da yer alır.", zorluk="hard")

P.q("II-5.1 m. 9, 13",
    f"{IZ}, birden fazla belge şeklinde hazırlanan izahnameye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Özette, izahnamede yer almayan bilgilere atıfta bulunulabilir.",
    ["İzahname ihraççı bilgi dokümanı, sermaye piyasası aracı notu ve özetten oluşur.",
     "İhraççı bilgi dokümanı ile sermaye piyasası aracı notundaki bilgilerin birbirini tekrar etmemesi esastır.",
     "Özetin izahnameye giriş olarak okunması gerektiğine ilişkin uyarı özette yer alır.",
     "Sermaye piyasası aracı notu ile özetin geçerlilik süresi ihraççı bilgi dokümanını geçemez."],
    "Tebliğ m. 13'e göre çok belgeli izahname ihraççı bilgi dokümanı, sermaye piyasası aracı notu ve özetten oluşur; belgeler "
    "birbirini tekrar etmez ve özette giriş niteliğine ilişkin uyarı bulunur. m. 17'ye göre not ve özetin geçerliliği ihraççı "
    "bilgi dokümanını geçemez. m. 9'a göre özette izahnamede yer alan bilgiler dışındaki bilgilere atıf yapılamaz.",
    zorluk="hard")

P.q("II-5.1 m. 14",
    f"{IZ}, arz programı izahnamesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Arz programı izahnamesi hazırlanması bankalar için zorunludur.",
    ["Arz programı azami beş yıllık süre içinde yapılacak ihraçları kapsar.",
     "Arz programı ihraççının genel kurulunda ayrı bir gündem maddesiyle onaylanır.",
     "Program kapsamındaki her ihraçtan önce arz programı sirküleri Kurulca onaylanır.",
     "Mükerrer ihraç, on iki ayda benzer araçların en az iki defa ihracını kapsar."],
    "Tebliğ m. 14'e göre bankalar ortaklık hakkı vermeyen araçları mükerrer ihraç ederken ihtiyari olarak arz programı izahnamesi "
    "hazırlayabilir; mükerrer ihraç on iki ayda en az iki ihracı ifade eder. Program azami beş yıllık ihraçları kapsar, genel "
    "kurulda ayrı gündem maddesiyle onaylanır ve her ihraçtan önce sirküler onaylanır.", zorluk="hard")

P.q("II-5.1 m. 19",
    f"{IZ}, izahname onay başvurusunun Kurulca incelenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eksikler süresinde tamamlanmazsa başvuru Kurulca resen tamamlanarak karara bağlanır ve sonuçlandırılır.",
    ["Eksiklik varsa başvuru sahibi başvurudan itibaren on iş günü içinde bilgilendirilir.",
     "Eksiklerin yirmi iş günü içinde giderilmesi istenir.",
     "Makul sebeplerle talep üzerine yirmi iş gününe kadar ek süre verilebilir.",
     "Süresi içinde karar alınmaması izahnamenin onaylandığı anlamına gelmez."],
    "Tebliğ m. 19'a göre eksiklik hâlinde başvuru sahibi on iş günü içinde bilgilendirilir, eksiklerin yirmi iş günü içinde "
    "giderilmesi istenir ve talep üzerine yirmi iş gününe kadar ek süre verilebilir. Eksikler süresinde tamamlanmazsa başvuru "
    "işlemden kaldırılır; süresinde karar alınmaması onay veya ret anlamına gelmez.")

P.q("II-5.1 m. 22/5, 23",
    "Bir ihraççı, izahnamesinin onaylanmasına karar verilmesinden sonra onaylı izahnameyi teslim almamış ve halka arzdan "
    f"vazgeçmiştir. {IZ}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yirmi iş günü içinde teslim alınmayan izahname için yeniden onay gerekir.",
    ["İzahname onay tarihinden itibaren on iki ay boyunca teslim alınabilir.",
     "Yatırılan Kurul ücreti, satıştan vazgeçildiği için talep üzerine iade edilir.",
     "Kurul ücreti, bir sonraki ihraçta ödenecek ücretten mahsup edilir.",
     "Teslim alınmayan izahname Kurul tarafından resen ilan edilir."],
    "Tebliğ m. 22/5'e göre onay kararını takip eden yirmi iş günü içinde teslim alınmayan veya süresinde ilan edilmeyen izahname "
    "için yeniden onay gerekir. m. 23/2'ye göre yatırılan Kurul ücretinin iadesi veya başka ihraçlara mahsubu talep edilemez.",
    zorluk="hard")

P.q("II-5.1 m. 25/3",
    "İzahnamenin özet bölümünde bir bilgi eksik verilmiş, ancak aynı bilgi izahnamenin diğer kısımlarında doğru ve tam olarak "
    f"yer almaktadır. {IZ}, sadece özete dayalı sorumluluğa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Özet diğer kısımlarla birlikte yanıltıcı değilse tek başına sorumluluk doğurmaz.",
    ["Özetteki her eksiklik ihraççının ve lider aracı kurumun müteselsil sorumluluğunu doğurur.",
     "Özet ayrı bir kamuyu aydınlatma belgesi olduğundan eksiklik tek başına tazminat sebebidir.",
     "Özetten doğan sorumluluk sadece bağımsız denetim kuruluşuna aittir.",
     "Özetteki eksiklik izahnamenin geçersizliğine yol açar."],
    "Tebliğ m. 25/3'e göre izahnamenin diğer kısımlarıyla birlikte okunduğunda özetin yanıltıcı, hatalı veya tutarsız olması "
    "hâli hariç, sadece özete bağlı olarak ilgililere hukuki sorumluluk yüklenemez.")

P.oncul("II-5.1 m. 27",
    "Halka arzı planlanan bir ortaklığın tanıtım ve reklam faaliyetlerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Reklamlarda yatırım kararlarının izahnamenin incelenmesiyle verilmesi gerektiğine dair uyarı yer alır.",
     "Başvurudan sonra, izahname yayımlanmadan önce halka arz fiyatı reklamlarda duyurulabilir.",
     "Halka arz fiyatına yer verilirse fiyatta Kurulun takdir yetkisinin bulunmadığı vurgulanır.",
     "Belirli bir yatırımcı grubuna açıklanan bilgilere izahnamede de yer verilir."],
    f"{IZ}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Tebliğ m. 27'ye göre reklamlarda izahnameyi inceleme uyarısı zorunludur; fiyata yer verilirse Kurul veya borsanın takdiri "
    "bulunmadığı vurgulanır ve bir gruba açıklanan bilgiler izahnamede de yer alır. Başvurudan sonra, yayımdan önce yapılan "
    "reklamlar sadece sektör, konum, faaliyet ve ürünler hakkında olabilir.")

P.sayisal("II-5.1 m. 28/2",
    "Payların halka arzı için Kurula izahname onay başvurusu yapılmıştır. "
    f"{IZ}, onaylanması için sunulan izahname Kurula başvuru tarihinden itibaren kaç iş günü içinde ihraççının internet "
    "sitesinde ve KAP’ta ilan edilir?",
    "5", ["2", "10", "15", "20"],
    "Tebliğ m. 28/2'ye göre onaylanması için sunulan izahname başvurudan itibaren beş iş günü içinde ihraççının internet sitesi, "
    "KAP ve varsa yetkili kuruluşun sitesinde, henüz onaylanmadığını belirten ifadeyle ilan edilir; m. 28/3'e göre onaylı "
    "izahname teslimden itibaren on beş iş günü içinde ilan edilir.", zorluk="hard")

P.q("II-5.1 m. 28",
    f"{IZ}, onaylı izahnamenin ilanı ve geçerliliğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Satışa başlamak için yayım yerinin tescil edilmiş olması gerekir.",
    ["Onaylı izahname teslimden itibaren on beş iş günü içinde ilan edilir.",
     "KAP üyesi ihraççılarda izahnamenin geçerliliği KAP’ta ilan tarihinde başlar.",
     "İzahname internet sitesinde onaylandığı şekliyle asgari beş yıl korunur.",
     "Elektronik yayımlanan izahnamenin basılı nüshası talep eden yatırımcıya bedelsiz verilir."],
    "Tebliğ m. 28'e göre onaylı izahname teslimden itibaren on beş iş günü içinde ilan edilir, geçerliliği KAP'ta ilanla başlar "
    "ve internet sitesinde asgari beş yıl korunur; basılı nüsha bedelsiz verilir. İzahnamenin nerede yayımlandığı ilandan "
    "itibaren on iş günü içinde tescil edilir, ancak satışa başlamak için tescil gerekmez.", zorluk="hard")

# ================================================================ Satış Tebliği (II-5.2)
P.q("II-5.2 m. 6",
    f"{ST}, sermaye piyasası araçlarının satış şekillerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Araçlar halka arz edilerek veya halka arz edilmeksizin tahsisli ya da nitelikli yatırımcıya satılabilir.",
    ["Araçlar ancak halka arz yoluyla satılabilir.",
     "Tahsisli satış ve nitelikli yatırımcıya satış aynı ihraçta birlikte kullanılamaz.",
     "Nitelikli yatırımcıya satış halka arz sayılır ve bu nedenle Kurul onaylı izahname hazırlanmasını gerektirir.",
     "Halka arz edilmeksizin satış sadece kamu kurumlarına yapılabilir."],
    "Tebliğ m. 6'ya göre sermaye piyasası araçları halka arz edilerek veya halka arz edilmeksizin tahsisli olarak ya da "
    "nitelikli yatırımcılara satılabilir; Kurul düzenlemelerinde aksine hüküm yoksa bu satış şekilleri bir arada kullanılabilir.")

P.sayisal("II-5.2 m. 8/1",
    f"{ST}, payların ikincil piyasa işlemleri hariç, tahsisli olarak satılan sermaye piyasası araçlarını belirli bir anda "
    "elinde bulunduran yatırımcı sayısının (nitelikli yatırımcılar hariç) kaçı geçmemesi esastır?",
    "150", ["50", "100", "250", "500"],
    "Tebliğ m. 8'e göre tahsisli satılan araçları belirli bir anda elinde bulunduran yatırımcı sayısının yüz elliyi geçmemesi "
    "esastır; bu sayının hesabında nitelikli yatırımcılar dikkate alınmaz, müşterek hesap sahipleri ayrı sayılır.")

P.q("II-5.2 m. 8/3",
    "Tahsisli olarak satılan bir borçlanma aracını elinde bulunduran yatırımcı sayısının Tebliğdeki sınırı aştığı MKK tarafından "
    f"tespit edilmiştir. {ST}, bu durumda ihraççının yükümlülüğü aşağıdakilerden hangisidir?",
    "Yirmi iş günü içinde izahname onayı ve borsada işlem görme için başvurmak",
    ["Sınırı aşan sayıdaki yatırımcıdan araçları nominal değer üzerinden geri alıp itfa etmek",
     "Aracın tahsisli satışını iptal ederek bedelleri iade etmek",
     "Kurula bildirimde bulunmak; başka bir işlem yapmaya gerek yoktur",
     "Bildirimden itibaren altı ay içinde aracı itfa etmek"],
    "Tebliğ m. 8/3'e göre sayının aşıldığı MKK tarafından derhâl ihraççıya ve Kurula bildirilir; ihraççı bildirimden itibaren "
    "yirmi iş günü içinde hazırlayacağı izahnamenin onayı için Kurula ve aracın borsada işlem görmesi için borsaya başvurur.",
    zorluk="hard")

P.q("II-5.2 m. 10/1, 3",
    "Payları borsada işlem gören bir ortaklık, sermaye artırımında yeni pay alma haklarının kullanılmasından sonra kalan payları "
    f"halka arz edecektir. {ST}, izahnamenin yayımlanmasından sonra satışa en erken ne zaman başlanabilir?",
    "İzahnamenin yayımını takip eden iş günü",
    ["İzahnamenin yayımını takip eden üçüncü gün",
     "İzahnamenin yayımından itibaren on iş günü sonra",
     "İzahnamenin yayımlandığı gün, yayımdan bir saat sonra",
     "İzahnamenin yayımından itibaren bir ay sonra"],
    "Tebliğ m. 10/1'e göre halka arza en erken izahname ve fiyat tespit raporunun yayımını takip eden üçüncü gün başlanabilir; "
    "m. 10/3'e göre halka arz ettiği araçları borsada işlem gören ihraççılar için bu süre takip eden iş günüdür. Payların ilk "
    "defa halka arzında üç günlük süre uygulanır.", zorluk="hard")

P.oncul("II-5.2 m. 10, 23",
    "Talep toplama yoluyla yapılan bir halka arzın satış ve dağıtım sürelerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Halka arz yoluyla satış süresi en az iki, en fazla yirmi iş günüdür.",
     "Talep toplama süresi içinde yeterli talep gelirse talep toplama erken sona erdirilir.",
     "Dağıtım listesi talep toplama süresinin bitimini izleyen iki iş günü içinde düzenlenir.",
     "İhraççı veya halka arz eden, dağıtım listesini tesliminden itibaren iki iş günü içinde onaylar."],
    f"{ST}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Tebliğ m. 10/7'ye göre halka arz satış süresi iki iş gününden az, yirmi iş gününden fazla olamaz ve yeterli talep gelse "
    "dahi talep toplamaya süre sonuna kadar devam edilir. m. 23'e göre dağıtım listesi talep toplamanın bitiminden itibaren iki "
    "iş günü içinde düzenlenir ve ihraççı listeyi iki iş günü içinde onaylar.", zorluk="hard")

P.q("II-5.2 m. 10/8",
    "Bir ortaklığın payları halka arzda borsada satış yöntemiyle ve talep toplanmaksızın satılacaktır. "
    f"{ST}, bu satışın süresine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Süre iki iş günüdür; paylar önceden satılırsa satış sona erdirilir.",
    ["Satış süresi en az beş iş günüdür.",
     "Satış süresi borsa tarafından her halka arz için ayrıca belirlenir.",
     "Satış süresi yirmi iş günüdür ve erken sona erdirilemez.",
     "Satış, payların tamamı satılıncaya kadar süre sınırı olmaksızın devam eder."],
    "Tebliğ m. 10/8'e göre borsada satış yönteminde talep toplanmaksızın satışta süre iki iş günüdür ve tamamı daha önce "
    "satılırsa satış sona erdirilir; talep toplama suretiyle satışta talep toplama süresi en az iki, en fazla üç iş günüdür.")

P.sayisal("II-5.2 m. 10/7",
    f"{ST}, sermaye piyasası araçlarının halka arz yoluyla satış süresi en az kaç iş günü olarak belirlenebilir?",
    "2", ["1", "3", "5", "10"],
    "Tebliğ m. 10/7'ye göre halka arz yoluyla satış süresi, iki iş gününden az ve yirmi iş gününden fazla olmamak üzere "
    "ihraççı ve/veya halka arz eden tarafından belirlenir.", zorluk="easy")

P.q("II-5.2 m. 14-15",
    "Payları borsada işlem görmeyen bir halka açık ortaklık, paylarını izahnamede belirlenen bir usulle ve belirli bir "
    f"fiyattan, önceden talep toplamaksızın halka arz etmek istemektedir. {ST}, bu yöntem aşağıdakilerden hangisidir?",
    "Talep toplamaksızın satış yöntemi",
    ["Sabit fiyatla talep toplama yöntemi", "Fiyat aralığı ile talep toplama yöntemi",
     "Borsada satış yöntemi", "Tahsisli satış yöntemi"],
    "Tebliğ m. 15'e göre talep toplamaksızın satış, payları borsada işlem görmeyen halka açık ortaklıkların (niteliği "
    "belirlenmiş ortaklıklar hariç) paylarının belirli bir fiyattan, izahnamede belirlenen ve yatırımcılar arasında "
    "eşitsizliğe yol açmayan bir usulle halka arz edilmesidir.")

# ================================================================ halka açık ortaklık statüsü ve kayıtlı sermaye (m. 16, 18, 33)
P.sayisal("6362 s. SPKn m. 33/1",
    "Payları halka arz edilmeksizin pay sahibi sayısı Kanundaki sınırı aşan bir anonim ortaklık, halka açık ortaklık "
    f"statüsünü kazandığını öğrenmiştir. {K}, ortaklık bu durumu öğrendiği tarihten itibaren kaç iş günü içinde Kurula bildirmelidir?",
    "10", ["3", "5", "15", "30"],
    "Kanun m. 33/1'e göre ortaklıklar, araçlarının halka satıldığını veya halka açık ortaklık statüsünü kazandığını "
    "öğrendikleri tarihten itibaren on iş günü içinde Kurula bildirmek zorundadır.")

P.q("6362 s. SPKn m. 33/4",
    "Pay sahibi sayısı nedeniyle halka açık sayılan bir anonim ortaklık, paylarının borsada işlem görmesini istememekte ve "
    f"Kanun kapsamından çıkmak istemektedir. {K}, bu karara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Pay sahibi tam sayısının 2/3’ü veya toplam oyların 3/4’ü ile genel kurul kararı gerekir.",
    ["Yönetim kurulu kararı ve Kurula bildirim yeterlidir.",
     "Toplantı nisabı aranmaksızın genel kurula katılanların salt çoğunluğunun olumlu oyu yeterlidir.",
     "Kapsamdan çıkma kararı için tüm pay sahiplerinin oybirliği gerekir.",
     "Kapsamdan çıkma kararına olumlu oy vermeyen pay sahiplerine ayrılma hakkı tanınmaz."],
    "Kanun m. 33/4'e göre pay sahibi sayısı sebebiyle halka açık sayılan ve paylarının borsada işlem görmesini istemeyen "
    "ortaklıklar, pay sahibi tam sayısının en az üçte ikisinin olumlu oyu veya toplam oyların dörtte üçü ile alınacak genel "
    "kurul kararıyla Kanun kapsamından çıkabilir; olumlu oy vermeyenlere ayrılma hakkı tanınır.", zorluk="hard")

P.q("6362 s. SPKn m. 18",
    f"{K}, halka açık ortaklıklarda kayıtlı sermaye sistemine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kayıtlı sermaye tavanı dahilindeki artırımlarda imtiyazlı pay sahipleri özel kurulu kararı aranır.",
    ["Halka açık ortaklıklar Kuruldan izin alarak kayıtlı sermaye sistemini kabul edebilir.",
     "Çıkarılan paylar satılarak bedelleri ödenmedikçe veya iptal edilmedikçe yeni pay çıkarılamaz.",
     "Yönetim kurulunun yeni pay alma hakkını kısıtlaması için esas sözleşmeyle yetkili kılınması şarttır.",
     "Yönetim kurulu kararlarına karşı ilandan itibaren otuz gün içinde iptal davası açılabilir."],
    "Kanun m. 18'e göre halka açık ortaklıklar Kurul izniyle kayıtlı sermaye sistemine geçer; çıkarılan paylar satılmadıkça yeni "
    "pay çıkarılamaz, yeni pay alma hakkının kısıtlanması esas sözleşmede yetki gerektirir ve kararlara karşı otuz gün içinde "
    "iptal davası açılabilir. m. 18/4'e göre tavan dahilindeki artırımlarda imtiyazlı pay sahipleri özel kurulu kararı aranmaz.",
    zorluk="hard")

P.sayisal("6362 s. SPKn m. 18/9",
    "Kayıtlı sermaye sistemindeki halka açık bir ortaklığın kayıtlı sermaye tavanı 100 milyon TL, çıkarılmış sermayesi 70 "
    f"milyon TL’dir. Ortaklık, pay ile değiştirilebilir tahvil ihraç etmek istemektedir. {K}, değiştirme sonucunda verilecek "
    "payların toplam nominal değeri en fazla kaç milyon TL olabilir?",
    "30", ["20", "70", "100", "170"],
    "Kanun m. 18/9'a göre kayıtlı sermaye sistemindeki halka açık ortaklıkların pay ile değiştirilebilir tahvil veya paya "
    "dönüştürülebilir türev araç çıkarması hâlinde verilecek paylar ile çıkarılmış sermayenin toplamı kayıtlı sermayeyi "
    "aşamaz: 100 − 70 = 30 milyon TL.", zorluk="hard")

P.q("6362 s. SPKn m. 18/1, 7-10",
    f"{K}, kayıtlı sermaye sistemine geçişe ve sistemin işleyişine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Daha önce TTK uyarınca sisteme geçmiş ortaklıklar da ayrıca Kurul iznine tabidir.",
    ["Halka açık ortaklıklar Kuruldan izin alarak kayıtlı sermaye sistemini kabul edebilir.",
     "Halka arz için Kurula başvuran ortaklıklar da Kurul izniyle sisteme geçebilir.",
     "Sistemden çıkma ve Kurulca çıkarılma esaslarını Kurul belirler.",
     "Yönetim kurulunun bu sistemdeki kararları Kurulca belirlenecek şekilde kamuya duyurulur."],
    "Kanun m. 18/1'e göre halka açık ortaklıklar ile halka arz için başvuranlar Kurul izniyle kayıtlı sermaye sistemine geçer; "
    "daha önce TTK uyarınca geçmiş ortaklıklar için ayrıca Kurul izni aranmaz. m. 18/8 yönetim kurulu kararlarının duyurulmasını, "
    "m. 18/10 sistemden çıkma ve çıkarılma esaslarını düzenler.", zorluk="hard")

# ================================================================ önemli nitelikteki işlemler ve ayrılma hakkı (m. 23-24, II-23.3)
P.q("II-23.3 m. 4",
    f"{ON}, aşağıdakilerden hangisi halka açık bir ortaklığın önemli nitelikteki işlemleri arasında sayılmaz?",
    "Olağan ticari faaliyet kapsamında stoklarının satılması",
    ["Devrolunan taraf olarak birleşme işlemine taraf olması",
     "Anonim şirket türünden başka bir türe dönüşmesi",
     "Esas sözleşmesinde yeni bir imtiyaz öngörmesi",
     "Önemlilik ölçütünü aşan mal varlığını devretmesi"],
    "Tebliğ m. 4'e göre birleşme veya bölünme işlemlerine (m. 5'teki hâllerde) taraf olma, tür değiştirme, önemlilik "
    "ölçütlerini sağlayan mal varlığı devri veya üzerinde sınırlı ayni hak tesisi ile imtiyaz öngörülmesi veya değiştirilmesi "
    "önemli nitelikteki işlemdir. Olağan ticari faaliyet bu kapsamda değildir.", zorluk="easy")

P.q("II-23.3 m. 5",
    f"Halka açık bir ortaklığın aşağıdaki birleşme ve bölünme işlemleri değerlendirilmektedir. {ON}, hangisi önemli "
    "nitelikteki işlem sayılır?",
    "Devralma şeklindeki birleşmede devralan olarak sermayesini %60 artırması",
    ["Devralma şeklindeki birleşmede devralan olarak sermayesini %40 artırması",
     "Kısmi bölünmede devralan olarak sermayesini %30 artırması",
     "Kısmi bölünmede önemlilik ölçütünü sağlamayan bir mal varlığını devretmesi",
     "Tam bölünmede devralan olarak sermayesini %20 artırması"],
    "Tebliğ m. 5'e göre yeni kuruluş şeklinde birleşmeye taraf olma, devrolunan taraf olma veya devralan olarak %50 ya da daha "
    "fazla sermaye artırımı yapma önemli nitelikteki işlemdir. Bölünmelerde de devralan taraf için %50 ölçütü, kısmi bölünen "
    "taraf için önemlilik ölçütü aranır.", zorluk="hard")

P.sayisal("II-23.3 m. 6/1",
    "Payları borsada işlem gören ve Kurumsal Yönetim Tebliği uyarınca Birinci Grupta yer alan bir ortaklık, bir fabrikasını "
    f"satmayı planlamaktadır. {ON}, bu satışın önemli nitelikteki işlem sayılması için işleme konu mal varlığının kayıtlı "
    "değerinin aktif toplamına oranının yüzde kaçtan fazla olması gerekir?",
    "%75", ["%25", "%50", "%67", "%90"],
    "Tebliğ m. 6/1'e göre mal varlığı devrinde önemlilik ölçütü; işleme konu varlığın kayıtlı değerinin aktif toplamına, işlem "
    "tutarının ortaklık değerine veya varlıktan elde edilen gelirin toplam gelirlere oranından birinin %75'ten fazla olmasıdır. "
    "Fiili dolaşımı %50'nin üstündeki bazı ortaklıklarda oran %50 uygulanır.", zorluk="hard")

P.q("II-23.3 m. 6/6",
    "Payları borsada işlem gören, Kurumsal Yönetim Tebliğine göre Üçüncü Grupta yer alan ve fiili dolaşımdaki pay oranı %65 "
    f"olan bir sanayi ortaklığı, bir mal varlığı devrini değerlendirmektedir. {ON}, bu ortaklık için önemlilik oranı nasıl uygulanır?",
    "Önemlilik oranı %75 yerine %50 olarak uygulanır.",
    ["Önemlilik oranı %75 olarak uygulanır.",
     "Önemlilik oranı %90 olarak uygulanır.",
     "Önemlilik ölçütü aranmaz; tüm mal varlığı devirleri önemli nitelikte sayılır.",
     "Önemlilik oranı fiili dolaşım oranına eşit olarak %65 uygulanır."],
    "Tebliğ m. 6/6'ya göre Birinci ve İkinci Grup ile GYO ve GSYO dışındaki, fiili dolaşımdaki pay oranı %50'nin üstünde olan "
    "borsa ortaklıklarında önemlilik oranı %50 olarak uygulanır; ayrıca fiili faaliyet konusunu tümüyle değiştiren mal varlığı "
    "devirleri orana bakılmaksızın önemli nitelikteki işlem sayılır.", zorluk="hard")

P.q("II-23.3 m. 10/2",
    "Halka açık bir ortaklığın önemli nitelikteki işlemi görüştüğü genel kurula, oy hakkını haiz payların %40’ı katılmış; "
    f"katılan oyların %60’ı olumlu kullanılmıştır. Esas sözleşmede daha ağır nisap yoktur. {ON}, bu işlem hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Katılan oyların üçte ikisi aranacağından karar alınamamıştır.",
    ["Toplantı nisabı sağlanmadığı için genel kurul açılamaz.",
     "Katılan oyların çoğunluğu olumlu olduğu için karar alınmıştır.",
     "Sermayenin yarısı hazır bulunmadığı için karar Kurul onayıyla geçerli olur.",
     "Olumlu oylar sermayenin dörtte birini aştığı için karar alınmıştır."],
    "Tebliğ m. 10/2'ye göre toplantı nisabı aranmaksızın katılan oy hakkını haiz payların üçte ikisinin olumlu oyu gerekir; "
    "sermayenin en az yarısı hazırsa katılanların çoğunluğu yeterlidir. Katılım %40 olduğu için üçte iki aranır; %60 olumlu oy "
    "bunu karşılamaz.", zorluk="hard")

P.oncul("II-23.3 m. 11",
    "Payları borsada işlem gören bir ortaklığın önemli nitelikteki işleminde ayrılma hakkına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Ayrılma hakkı için genel kurula katılıp olumsuz oy vermek ve muhalefeti tutanağa geçirtmek gerekir.",
     "Hak sahipleri, işleme ilişkin yönetim kurulu kararının kamuya açıklandığı tarihteki pay sahipleridir.",
     "Oy hakkı intifa hakkı sahibince kullanılıyorsa ayrılma hakkını intifa hakkı sahibi kullanır.",
     "Hak sahipleri ve pay tutarlarına ilişkin liste genel kuruldan bir önceki iş günü MKK tarafından ortaklığa verilir."],
    f"{ON}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Tebliğ m. 11'e göre olumsuz oy verip muhalefetini tutanağa geçirten ve kamuya açıklama tarihinde pay sahibi olanlar "
    "ayrılma hakkına sahiptir; listeyi MKK genel kuruldan bir önceki iş günü ortaklığa verir. Oy hakkı intifa hakkı sahibince "
    "kullanılıyorsa intifa hakkı sahibi ayrılma hakkını kullanamaz.", zorluk="hard")

P.sayisal("II-23.3 m. 12/2",
    f"{ON}, ayrılma hakkının kullanım süresi, başlangıç tarihinden itibaren kaç iş günüdür?",
    "10", ["3", "5", "15", "30"],
    "Tebliğ m. 12/2'ye göre ayrılma hakkının kullandırılması genel kurul tarihinden itibaren en geç altı iş günü içinde başlar "
    "ve kullanım süresi başlangıç tarihinden itibaren on iş günüdür; hak aracı kurum vasıtasıyla kullandırılır.")

P.q("II-23.3 m. 14/1",
    "Payları Borsa İstanbul Yıldız Pazarda işlem gören bir ortaklığın önemli nitelikteki işlemi kamuya açıklanmıştır. "
    f"{ON}, ayrılma hakkı kullanım fiyatı nasıl belirlenir?",
    "Açıklama tarihinden önceki son bir aylık düzeltilmiş ağırlıklı ortalama fiyatların aritmetik ortalaması",
    ["Açıklama tarihinden önceki son altı aylık düzeltilmiş ağırlıklı ortalama fiyatların aritmetik ortalaması",
     "Genel kurul tarihindeki kapanış fiyatı",
     "Bağımsız değerleme kuruluşunun belirlediği adil değer",
     "Açıklama tarihinden önceki son bir yıldaki en yüksek fiyat"],
    "Tebliğ m. 14/1'e göre ayrılma hakkı kullanım fiyatı, esas alınan tarih itibarıyla Yıldız Pazardaki ortaklıklar için son "
    "bir aylık, diğer ortaklıklar için son altı aylık dönemdeki günlük düzeltilmiş ağırlıklı ortalama fiyatların aritmetik "
    "ortalamasıdır. Borsada işlem görmeyenlerde değerleme raporu esas alınır.", zorluk="hard")

P.q("II-23.3 m. 15",
    f"{ON}, aşağıdakilerden hangisi ayrılma hakkının doğmadığı kabul edilen hâller arasında sayılmamıştır?",
    "Ortaklığın yeni kuruluş şeklindeki bir birleşmeye taraf olması",
    ["Mevzuat uyarınca yapılması zorunlu olan işlemler",
     "Yönetim kontrolüne bir kamu kurumunun sahip olduğu ortaklıkların işlemleri",
     "Ortaklığın sermayesinin en az %90’ına sahip olduğu bağlı ortaklığıyla yaptığı mal varlığı işlemleri",
     "Kolaylaştırılmış usulde gerçekleştirilen birleşme ve bölünme işlemleri"],
    "Tebliğ m. 15'e göre mevzuat gereği zorunlu işlemler, kamu kurumu kontrolündeki ortaklıkların işlemleri, %90 ve üzeri bağlı "
    "ortaklıkla yapılan işlemler ve kolaylaştırılmış usulde birleşme ve bölünmelerde ayrılma hakkı doğmaz. Yeni kuruluş "
    "şeklinde birleşme ayrılma hakkı doğuran önemli nitelikteki işlemdir.")

P.q("II-23.3 m. 16",
    "Muaccel banka borçlarını ödeyemeyen halka açık bir ortaklık, finansal güçlükten kurtulmak için önemli bir mal varlığını "
    f"devretmeye ve ayrılma hakkı kullandırma yükümlülüğünden muafiyet istemeye karar vermiştir. {ON}, bu başvuruya ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "On iş günü içinde başvurulur ve bağımsız güvence raporu sunulur.",
    ["Muafiyet yönetim kurulu kararıyla doğar, Kurula başvuru gerekmez.",
     "Başvuru genel kurul tarihinden sonra otuz gün içinde yapılır.",
     "Başvuru için bağımsız denetim raporu yerine yönetim kurulu beyanı yeterlidir.",
     "Muafiyet başvurusu kamuya açıklanmaz."],
    "Tebliğ m. 16'ya göre finansal güçlükten kurtulma amaçlı işlemler muafiyet konusu olabilir; başvuru yönetim kurulu karar "
    "tarihini izleyen on iş günü içinde yapılır, finansal güçlük ve işlemin olumlu etkisini gösteren bağımsız güvence raporu "
    "sunulur ve başvuru ile sonucu kamuya açıklanır.", zorluk="hard")

P.q("6362 s. SPKn m. 24/2",
    "Önemli nitelikteki bir işlemin görüşüleceği genel kurulun gündemi usulüne uygun ilan edilmemiş ve bu nedenle bir pay "
    f"sahibi toplantıya katılamamıştır. {K}, bu pay sahibinin ayrılma hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Muhalefet şerhi şartı aranmaksızın ayrılma hakkını kullanabilir.",
    ["Toplantıya katılmadığı için ayrılma hakkını kullanamaz.",
     "Ayrılma hakkını ancak genel kurul kararının iptaline ilişkin dava kazanılırsa kullanabilir.",
     "Ayrılma hakkını kullanabilmesi için Kurulun onayı gerekir.",
     "Ayrılma hakkı yerine ortaklıktan kâr payı avansı talep edebilir."],
    "Kanun m. 24/2'ye göre pay sahibinin önemli nitelikteki işlemlere ilişkin genel kurula katılmasına haksız biçimde izin "
    "verilmemesi, çağrının usulüne göre yapılmaması veya gündemin gereği gibi ilan edilmemesi hâllerinde muhalif kalma ve "
    "muhalefet şerhi şartı aranmaksızın ayrılma hakkı kullanılabilir.")

# ================================================================ pay alım teklifi, çıkarma ve satma, imtiyaz (m. 25-28)
P.q("6362 s. SPKn m. 26/2",
    "Bir yatırımcının halka açık bir ortaklıktaki durumu aşağıdaki seçeneklerde verilmiştir. "
    f"{K}, hangisi yönetim kontrolünün elde edilmesi olarak kabul edilmez?",
    "Oy haklarının %45’ine sahip olunması, başka bir imtiyaz bulunmaması",
    ["Oy haklarının %51’ine birlikte hareket edilen kişilerle beraber sahip olunması",
     "Yönetim kurulu üyelerinin salt çoğunluğunu seçme hakkı veren imtiyazlı paylara sahip olunması",
     "Genel kurulda yönetim kurulu üyelerinin çoğunluğu için aday gösterme imtiyazına sahip olunması",
     "Oy haklarının %55’ine dolaylı olarak sahip olunması"],
    "Kanun m. 26/2'ye göre oy haklarının yüzde ellisinden fazlasına tek başına veya birlikte hareket edilenlerle doğrudan veya "
    "dolaylı sahip olunması ya da yönetim kurulu üye sayısının salt çoğunluğunu seçme veya aday gösterme imtiyazına sahip "
    "olunması yönetim kontrolüdür. %45 oy hakkı tek başına yönetim kontrolü değildir.")

P.q("6362 s. SPKn m. 26/6, 103/3",
    "Halka açık bir ortaklıkta yönetim kontrolünü sağlayan payları iktisap eden bir kişi, Kurulca belirlenen süre içinde pay "
    f"alım teklifinde bulunmamıştır. {K}, bu durumun sonuçlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kişinin oy hakları donar ve bu paylar genel kurul toplantı nisabında dikkate alınmaz.",
    ["İktisap geçersiz sayılır ve paylar önceki sahiplerine iade edilir.",
     "Oy hakları devam eder, ancak kâr payı hakları donar.",
     "Ortaklık Kurul kararıyla halka açık ortaklık statüsünden çıkarılır.",
     "Kişi hakkında bilgi suistimali suçundan kovuşturma başlatılır."],
    "Kanun m. 26/6'ya göre zorunluluğun Kurulca belirlenen süre içinde yerine getirilmemesi hâlinde pay alım teklifi yükümlüsü "
    "ile birlikte hareket edenlerin oy hakları donar ve bu paylar genel kurul toplantı nisabında dikkate alınmaz; m. 103/3 "
    "ayrıca idari para cezası öngörür.", zorluk="hard")

P.oncul("6362 s. SPKn m. 25, 27",
    "Pay alım teklifi ile ortaklıktan çıkarma ve satma haklarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Pay alım teklifi Kurul tarafından yasaklanmışsa bu teklife dayanılarak yapılan işlemler geçersizdir.",
     "Oy haklarının Kurulca belirlenen orana ulaşmasıyla hâkim ortak için ortaklıktan çıkarma hakkı doğar.",
     "Çıkarma hakkının doğduğu durumlarda azınlık pay sahipleri için satma hakkı doğar.",
     "Halka açık ortaklıklarda Türk Ticaret Kanunu’nun ortaklıktan çıkarma hükmü uygulanır."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III", ["I ve II", "II ve IV", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 25/2'ye göre yasaklanan teklife dayanılarak yapılan işlemler geçersizdir. m. 27'ye göre oy hakları Kurulca "
    "belirlenen orana ulaşan kişiler için çıkarma hakkı, azınlıktaki pay sahipleri için de satma hakkı doğar; m. 27/3'e göre "
    "TTK m. 208 halka açık ortaklıklara uygulanmaz.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 28/2",
    "Payları halka arz edilmiş bir ortaklık, mevzuata uygun finansal tablolarına göre art arda dönem zararı açıklamaktadır. "
    f"{K}, oy hakkına ve yönetim kurulunda temsile ilişkin imtiyazların Kurul kararıyla kalkması için ortaklığın üst üste en az "
    "kaç yıl dönem zararı etmesi gerekir?",
    "5", ["2", "3", "4", "10"],
    "Kanun m. 28/2'ye göre faaliyetlerin makul ve zorunlu kıldığı hâller saklı kalmak kaydıyla, üst üste beş yıl dönem zararı "
    "eden halka açık ortaklıklarda oy hakkına ve yönetim kurulunda temsile ilişkin imtiyazlar Kurul kararıyla kalkar; imtiyazlı "
    "paylar kamu kurumlarına aitse bu hüküm uygulanmaz.")

P.q("6362 s. SPKn m. 28/1",
    "Bir anonim ortaklığın A grubu payları yönetim kurulunda temsil ve oyda imtiyaz taşımaktadır ve ortaklık ilk kez halka "
    f"arz edilecektir. {K}, bu imtiyazlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlk halka arzda mevcut tüm imtiyazların anlaşılır biçimde kamuya duyurulması zorunludur.",
    ["İlk halka arzdan önce tüm imtiyazların kaldırılması zorunludur.",
     "İmtiyazlar ilk halka arzla birlikte Kurul kararıyla kalkar.",
     "İmtiyazların kamuya duyurulması, payların borsada işlem görmesinden sonra yapılır.",
     "Oy imtiyazı halka açık ortaklıklarda öngörülemez; sadece temsil imtiyazı korunur."],
    "Kanun m. 28/1'e göre ortaklıkların araçlarının ilk halka arzında mevcut tüm imtiyazların şeffaf ve anlaşılır ayrıntıda "
    "kamuya duyurulması zorunludur; imtiyazın kalkması m. 28/2'deki beş yıl üst üste zarar şartına bağlıdır.")

# ================================================================ Birleşme ve Bölünme Tebliği (II-23.2)
P.q("II-23.2 m. 4",
    "Halka açık bir ortaklık, bir işletmesini ayni sermaye olarak yeni kurulan bir şirkete koymuş ve karşılığında bu yeni "
    f"şirketin paylarını kendisi edinmiştir; bölünen ortaklık varlığını sürdürmektedir. {BB}, bu işlem aşağıdakilerden hangisidir?",
    "İştirak modeliyle kısmi bölünme",
    ["Ortaklara pay devri modeliyle kısmi bölünme", "Tam bölünme", "Devralma şeklinde birleşme",
     "Yeni kuruluş şeklinde birleşme"],
    "Tebliğ m. 4'e göre iştirak modeliyle kısmi bölünmede bölünen şirket, bölünmeye konu malvarlığını başka bir şirkete ayni "
    "sermaye olarak koyar ve karşılığında devralan şirkette kendisi pay sahibi olur. Ortaklara pay devri modelinde ise paylar "
    "bölünen şirketin ortaklarına verilir; tam bölünmede bölünen şirket sona erer.")

P.sayisal("II-23.2 m. 13",
    f"{BB}, bir veya birden fazla sermaye şirketinin oy hakkı veren paylarının yüzde kaçına veya daha fazlasına sahip bir halka "
    "açık ortaklık tarafından devralınması suretiyle birleşmede, belirli şartlarla kolaylaştırılmış usul uygulanabilir?",
    "%95", ["%50", "%67", "%75", "%90"],
    "Tebliğ m. 13'e göre oy hakkı veren payların %95 veya daha fazlasına sahip halka açık ortaklığın devralması suretiyle "
    "birleşmede, devrolunan şirket ortaklarına pay verilmesi gerekmeyen veya payların nakit karşılığının seçimlik hak olarak "
    "önerildiği durumlarda kolaylaştırılmış usul uygulanabilir. İştirak modeliyle kısmi bölünmede de %95 ölçütü aranır.",
    zorluk="hard")

P.oncul("II-23.2 m. 6-7",
    "Halka açık bir ortaklığın taraf olduğu birleşme işlemine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Genel kurul hesap döneminin sonunu takip eden dördüncü ayın başı ile sekizinci ayın sonu arasında yapılırsa son yıllık finansal tablolar esas alınır.",
     "Esas alınacak finansal tablolar hakkında olumsuz görüş verilmişse bu tablolar birleşmeye esas alınmaz.",
     "Uzman kuruluş raporunda değişim oranının adil ve makul olduğuna ilişkin görüş verilir.",
     "Uzman kuruluş görüşünde tek bir değerleme yönteminin kullanılması yeterlidir."],
    f"{BB}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III", ["I ve II", "II ve IV", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Tebliğ m. 6'ya göre genel kurul dördüncü ayın başı ile sekizinci ayın sonu arasında yapılırsa son yıllık tablolar esas "
    "alınır; olumsuz görüş veya görüş bildirmekten kaçınılan tablolar esas alınmaz. m. 7'ye göre uzman kuruluş raporu değişim "
    "oranının adil ve makul olduğuna ilişkin görüş içerir ve en az üç değerleme yöntemi kullanılır.", zorluk="hard")

P.q("II-23.2 m. 5",
    f"Halka açık bir ortaklık, başka bir şirketle devralma yoluyla birleşmeye hazırlanmaktadır. {BB}, bu sürece ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birleşme için izahname hazırlanması ve onaylatılması zorunludur.",
    ["Duyuru metninin hazırlanması ve Kurulca onaylanması zorunludur.",
     "İşleme başlamak için taraf şirketlerin yönetim organlarının karar alması gerekir.",
     "Duyuru metninin onaylanması, bilgilerin doğruluğunun Kurulca tekeffülü anlamına gelmez.",
     "Başvuruda varsa sermaye artırımına ilişkin yönetim organı kararları da sunulur."],
    "Tebliğ m. 5'e göre halka açık ortaklıkların taraf olduğu birleşme ve bölünmelerde içeriği Kurulca belirlenen duyuru "
    "metninin hazırlanması ve onaylanması zorunludur; onay tekeffül anlamına gelmez. İşlem yönetim organı kararıyla başlar ve "
    "sermaye artırımı kararları başvuruda sunulur. II-5.1 m. 6 bu işlemlerde duyuru metni şartıyla izahname hazırlanmamasına imkân verir.")

P.q("II-23.2 m. 4, 17",
    "Halka açık bir ortaklık, bir bölümünü iştirak modeliyle kısmi bölünme yoluyla yeni kurulan bir şirkete devredecek ve "
    f"devralan şirketin oy hakkı veren paylarının tamamına sahip olacaktır. {BB}, bu işleme ilişkin aşağıdakilerden hangisi doğrudur?",
    "Devralanın en az %95’ine sahip olunacağından kolaylaştırılmış usul uygulanabilir.",
    ["İştirak modeliyle kısmi bölünmede kolaylaştırılmış usul uygulanamaz.",
     "Kolaylaştırılmış usul için bölünen ortaklığın devralanın tüm paylarını borsada satması gerekir.",
     "İşlem tam bölünme sayılır ve bölünen ortaklık sona erer.",
     "Devralan şirketin payları bölünen ortaklığın pay sahiplerine dağıtılır."],
    "Tebliğ m. 17'ye göre iştirak modeliyle kısmi bölünmede bölünen halka açık ortaklık işlem sonucunda devralanın oy hakkı veren "
    "paylarının en az %95'ine sahip olursa kolaylaştırılmış usulde bölünme uygulanabilir; m. 4'e göre bu modelde paylar bölünen "
    "şirkete verilir ve bölünen şirket sona ermez.")

P.q("6362 s. SPKn m. 23/2",
    "Halka açık bir ortaklık, Kurulun önemli nitelikteki işlemlere ilişkin usullerine uymaksızın bir mal varlığı devrini "
    f"gerçekleştirmiştir. {K}, Kurulun bu durumdaki yetkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Otuz gün içinde eski durum sağlanmazsa idari para cezası verebilir ve dava açabilir.",
    ["İşlemi doğrudan kendi kararıyla hükümsüz sayabilir.",
     "İşleme müdahale edemez; sadece yönetim kurulu üyeleri hakkında suç duyurusunda bulunabilir.",
     "İşlemi ancak pay sahiplerinin başvurusu üzerine inceleyebilir.",
     "Ortaklığın tüm faaliyetlerini süresiz olarak durdurur."],
    "Kanun m. 23/2'ye göre Kurul, zorunluluklara uyulmaksızın yapılan işlemlerin ortadan kaldırılmasına yönelik kararının "
    "tebliğinden itibaren otuz gün içinde işlem öncesi durum aynen sağlanmazsa idari para cezası verebilir ve TTK'nın genel kurul "
    "kararlarının iptaline ilişkin hükümleri çerçevesinde iptal davası açabilir.", zorluk="hard")

P.q("II-23.3 m. 7",
    "Halka açık bir ortaklığın genel kurulu, yönetim kuruluna gelecekte yapılacak mal varlığı devirleri için önceden genel "
    f"yetki vermiştir. {ON}, bu yetkiye dayanılarak yapılacak önemli nitelikteki bir işlem için aşağıdakilerden hangisi doğrudur?",
    "Genel yetki, ayrıca genel kurul onayı alınması zorunluluğunu kaldırmaz.",
    ["Önceden verilen genel yetki nedeniyle ayrıca genel kurul onayı aranmaz.",
     "Genel yetki varsa sadece Kurul onayı yeterlidir.",
     "Genel yetki varsa ayrılma hakkı doğmaz.",
     "Genel yetki beş yıl süreyle geçerlidir ve bu süre içindeki işlemlerde ayrıca onay aranmaz."],
    "Tebliğ m. 7'ye göre önemli nitelikteki işlem için işlemin esaslarını belirleyen yönetim kurulu kararı alınması ve işlemin "
    "genel kurulca onaylanması zorunludur; ön izin mahiyetinde genel yetki veren genel kurul kararı bu onay zorunluluğunu "
    "ortadan kaldırmaz.")

P.q("II-5.1 m. 2",
    f"{IZ}, aşağıdaki sermaye piyasası araçlarından hangisinin ihracı Tebliğ hükümlerine tabi değildir?",
    "Bir yatırım fonunun katılma payı",
    ["Bir yatırım kuruluşunun ihraç ettiği varant",
     "Bir yatırım kuruluşunun ihraç ettiği sertifika",
     "Borsada işlem görecek bir şirket tahvili",
     "Halka arz edilecek bir anonim ortaklık payı"],
    "Tebliğ m. 2'ye göre yatırım kuruluşu varant ve sertifikaları ile şirketlerin pay ve borçlanma araçları Tebliğe tabidir. "
    "Genel bütçeli idareler ve TCMB ihraçları, Hazine garantili araçlar ile yatırım fonu, emeklilik fonu ve DSYO payları kapsam "
    "dışıdır; bunlarda kendi düzenlemeleri uygulanır.", zorluk="easy")

P.q("II-5.1 m. 24/2",
    "Halka arz sırasında izahnamede değişiklik yapılmış ve değişiklik yayımlanmıştır. İzahnamede taleplerin geri alınmasına "
    f"ilişkin ayrı bir düzenleme bulunmaktadır. {IZ}, taleplerin geri alınma süresine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Süre iki iş günüdür; izahnamede belirtilmek şartıyla daha uzun belirlenebilir.",
    ["Süre iki iş günüdür ve ihraççı tarafından uzatılamaz.",
     "Süre yedi iş günüdür ve Kurul kararıyla uzatılabilir.",
     "Süre beş iş günüdür; izahnamede daha kısa belirlenebilir.",
     "Talepler ancak satış süresi sona ermeden önce geri alınabilir; ayrı süre yoktur."],
    "Tebliğ m. 24/2'ye göre değişiklikten önce talepte bulunmuş yatırımcılar ek ve değişikliklerin yayımlanmasından itibaren "
    "iki iş günü içinde taleplerini geri alabilir; izahnamede bilgi verilmesi koşuluyla bu süre ihraççı ve/veya halka arz "
    "eden tarafından daha uzun belirlenebilir.", zorluk="hard")

P.q("6362 s. SPKn m. 12/5",
    "Halka açık bir ortaklığın sermaye artırımı başvurusu Kurulda dört ay incelenmiştir. TTK uyarınca sermaye artırımının "
    f"belirli süre içinde tescil edilmesi gerekmektedir. {K}, bu süre hesabına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurulda geçen inceleme süresi tescil süresinin hesabında dikkate alınmaz.",
    ["Kurulda geçen süre tescil süresine dahildir; süre aşıldığı için artırım geçersizdir.",
     "Kurulda geçen sürenin yarısı tescil süresine eklenir.",
     "Tescil süresi Kurul onayından itibaren bir ay olarak uygulanır.",
     "Süre aşımında artırım Kurul kararıyla tescil olunur."],
    "Kanun m. 12/5'e göre sermaye artırımı nedeniyle Kurula yapılan başvurularda Kurulda geçen inceleme süresi, TTK m. 456'daki "
    "sermayenin tescil edilmesine ilişkin sürenin hesaplanmasında dikkate alınmaz.")

P.q("II-5.1 m. 10/2",
    "Bağımsız denetimden geçmiş finansal tablolarını KAP’ta düzenli olarak yayımlama yükümlülüğü bulunan bir ihraççı, yeni "
    f"bir borçlanma aracı izahnamesi hazırlamaktadır. {IZ}, finansal tablolara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tablolara izahnamede ayrıca yer verilmesi gerekmez; KAP’ta ilan edildikleri ve ilan tarihleri belirtilir.",
    ["Son beş yıllık finansal tabloların izahnamede tam metin olarak yer alması zorunludur.",
     "KAP’ta yayımlanan tablolar izahnamede kullanılamaz; yeni özel denetim yapılır.",
     "Tablolar yerine yönetim kurulunun onayladığı özet mali veriler yeterlidir.",
     "İzahname finansal tablo içermez; tablolar sadece Kurula ayrıca gönderilir."],
    "Tebliğ m. 10/2'ye göre bağımsız denetimden veya sınırlı incelemeden geçmiş tablolarını KAP'ta düzenli yayımlama yükümlülüğü "
    "olan ihraççıların izahnamesinde bu tablolara yer verilmesi gerekmez; tabloların KAP'ta ilan edildiğine dair bilgiye ilan "
    "tarihiyle birlikte yer verilir. m. 9 atıf yoluyla bilgi dahil etmeye imkân tanır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
