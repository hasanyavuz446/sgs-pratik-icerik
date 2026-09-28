# -*- coding: utf-8 -*-
"""Meslek Hukuku · Ruhsat, Sınav ve Staj — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, TÜRMOB 2026 derlemesi):
  · SMMM Staj Yönetmeliği (RG 23.08.1997; 24.02.2025-32823 değişiklikleri işlenmiş)
  · YMM ve SMMM Sınav Yönetmeliği (RG 16.01.2005; 24.02.2025-32823 değişiklikleri işlenmiş)
  · TÜRMOB Sürekli Mesleki Geliştirme Eğitimi Yönetmeliği (RG 23.06.2018; 29.03.2023 ve
    14.01.2026 değişiklikleri işlenmiş) — kredi yükümlülüğü 30/yıl, 120/3 yıl
Not: 2026/1 kitapçığındaki "üç yılda 90 kredi" 2023 değişikliğinden önceki metindir;
2026/2 kitapçığı güncel 120 krediyi sormuştur.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_ruhsat_ve_staj_2026.json", lesson="meslek_hukuku", topic="ruhsat_ve_staj",
          konu_adi="Ruhsat, Sınav ve Staj", seed=2026092806,
          surum="Staj Yön. ve Sınav Yön. (24.02.2025-32823 işlenmiş), SMGE Yön. (29.03.2023 ve 14.01.2026 işlenmiş); 28.09.2026 kontrolü")

SY = "Serbest Muhasebeci Mali Müşavirlik Staj Yönetmeliği’ne göre"
NY = "Yeminli Mali Müşavirlik ve Serbest Muhasebeci Mali Müşavirlik Sınav Yönetmeliği’ne göre"
GY = "Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği Sürekli Mesleki Geliştirme Eğitimi Yönetmeliği’ne göre"

# ================================================================ STAJ
P.q("Staj Yön. m. 5",
    "TESMER şubesi, bölgesindeki staj uygulamalarını denetlerken Yönetmelikte sayılan ilkeleri esas almaktadır. "
    f"{SY}, staja ilişkin ilkeler arasında aşağıdakilerden hangisi yer almaz?",
    "Stajın, meslek mensubunun büro iş yükünü karşılayacak biçimde planlanması",
    ["Stajın amacı, mesleki disiplin, bilgi ve deneyime sahip meslek mensubu yetiştirmektir.",
     "Staj, aday meslek mensubunun kendini yetiştirmesine imkân verecek biçimde uygulanır.",
     "Staj TESMER'in hazırladığı program çerçevesinde fiilen tamamlanır.",
     "Tezkiyede olumlu değerlendirme ölçütü 100 üzerinden 80 ve üzeri nottur."],
    "Staj Yönetmeliği m. 5 stajın amacını, adayın kendini yetiştirmesini ve meslek mensubunun faaliyetini aksatmayan bir "
    "uygulamayı, TESMER programını ve 80 puanlık tezkiye ölçütünü sayar. Stajın büro iş yükünü karşılamaya göre "
    "planlanması bir ilke değildir.")

P.q("Staj Yön. m. 5/d (24.02.2025 değişikliği)",
    "Aday meslek mensubu (A)'ya, stajının ikinci yılının bir dönemi için 100 üzerinden 75 tezkiye notu verilmiştir. "
    f"{SY}, bu durumun sonucu aşağıdakilerden hangisidir?",
    "O dönemi kapsayan staj geçersiz sayılır ve eksik süre tamamlatılır.",
    ["(A)'nın bütün stajı iptal edilir ve staja giriş sınavına yeniden girer.",
     "Not ortalamaya katılmaz; staj süresi etkilenmeden devam eder.",
     "(A) sınava girebilir, ancak tezkiye notu ayrı ders olarak sayılmaz.",
     "Tezkiye notu Birlik Disiplin Kurulunca yeniden değerlendirilir."],
    "2025 değişikliğiyle Staj Yönetmeliği m. 5/d'ye göre tezkiye notu 80 puanın altında olan adayların, 80'in altında "
    "not verilen dönemi kapsayan stajları geçersiz sayılır ve eksik süre tamamlatılır.",
    zorluk="hard")

P.q("Staj Yön. m. 6",
    "Bir oda, yeni staj dönemine başlayan adaylar için hazırladığı bilgilendirme notunda stajın hedeflerini "
    f"açıklamaktadır. {SY}, aşağıdakilerden hangisi stajın hedefleri arasında sayılmamıştır?",
    "Adaya müşteri portföyü oluşturma imkânı sağlamak",
    ["Meslek etiğini ve meslek bilincini yerleştirmek",
     "İlgili mevzuatı ve uygulamayı doğru ve etkili biçimde öğretmek",
     "Yabancı dil ve bilgi teknolojileri eğitimine olanak sağlamak",
     "Mesleki uygulamalarda uluslararası ve ulusal standartları etkin kılmak"],
    "Staj Yönetmeliği m. 6 hedefleri meslek etiği ve bilinci, mevzuat ve uygulamanın öğretilmesi, yabancı dil ve bilgi "
    "teknolojileri eğitimi ve standartların etkin kılınması olarak sayar. Müşteri portföyü oluşturma bir hedef değildir.")

P.sayisal("Staj Yön. m. 7",
    f"{SY}, serbest muhasebeci mali müşavirlik stajına başlayabilmek için staja giriş sınavından en az kaç puan alınmış olması gerekir?",
    "60", ["50", "65", "70", "80"],
    "Staj Yönetmeliği m. 7'ye göre staja başlamak için Kanun m. 4'teki genel şartlar ile m. 5/A-a'daki öğrenim şartını "
    "taşımak, staja giriş sınavından en az 60 puan almak ve Birlikçe belirlenen staj giderlerini yatırmış olmak gerekir.")

P.q("Staj Yön. m. 7 (24.02.2025 ek fıkra)",
    f"{SY}, staja giriş sınavına ve sonucuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Adaylar, ilk sınavın sonuç ilanından itibaren beş yıl içinde açılan sınavlara girebilir.",
    ["Staja giriş sınavına katılma süresi uzatılamaz.",
     "Başarılı olanlar, sonraki staja başlama döneminden itibaren üç yıl içinde staja başlayabilir.",
     "Üç yıl içinde staja başlamayanların sınav sonucu geçersiz sayılır.",
     "Süresi içinde staja başlamayanların dosyaları işlemden kaldırılır."],
    "2025'te m. 7'ye eklenen fıkraya göre adaylar katıldıkları ilk sınavın sonuçlarının ilanından itibaren 3 yıl içinde "
    "açılan tüm sınavlara katılabilir ve bu süre uzatılamaz. Başarılı olanlar üç yıl içinde staja başlamazsa sonuçları "
    "geçersiz olur ve dosyaları işlemden kaldırılır.",
    zorluk="hard")

P.q("Staj Yön. m. 8",
    f"{SY}, staj süresi ve stajın kesintisizliğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Staja toplamda en fazla iki yıl ara verilebilir.",
    ["Serbest muhasebeci mali müşavir adayları için staj süresi üç yıldır.",
     "Staj, mücbir sebepler ve yurt dışı eğitim ile çalışma dışında kesintisiz yapılır.",
     "Mücbir sebep kalktıktan sonra 15 gün içinde durum TESMER şubesine veya odaya bildirilir.",
     "Yurt dışı eğitim ve çalışma öncesinde TESMER'den izin alınması gerekir."],
    "Staj Yönetmeliği m. 8'e göre işyerinin kapanması, askerlik sonrası başlama, nakil veya işten çıkma gibi durumlar "
    "nedeniyle staja toplamda en fazla bir yıl ara verilebilir.")

P.q("Staj Yön. m. 8",
    "Aday meslek mensubu (G), stajının ikinci yılında staja bir süre devam edememiş ve bunun mücbir sebep sayılmasını "
    f"talep etmiştir. {SY}, aşağıdakilerden hangisi mücbir sebep sayılmaz?",
    "Başka bir işte çalışmak",
    ["Stajın fiilen yapılmasına engel ağır hastalık",
     "Tutukluluk hâli",
     "Yer sarsıntısı veya su basması gibi afetler",
     "Askerlik"],
    "Staj Yönetmeliği m. 8'e göre mücbir sebepler; ağır kaza, ağır hastalık, tutukluluk, yangın, yer sarsıntısı, su "
    "basması gibi afetler, kişinin iradesi dışında gelişen durumlar ve askerliktir. Kendi tercihiyle başka işte "
    "çalışmak mücbir sebep değildir.",
    zorluk="easy")

P.q("Staj Yön. m. 9/d (24.02.2025 değişikliği)",
    "Staj başvurusu yapan adaylar, önceki eğitimlerinde geçen sürelerin stajdan sayılmasını talep etmektedir. "
    f"{SY} stajdan sayılan hallerle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Birlikçe akredite yabancı dil programlarında geçen sürelerin tamamı stajdan sayılır.",
    ["Sayılan alanlarda tezli yüksek lisans yapanların bu eğitimde geçen sürelerinin bir yılı stajdan sayılır.",
     "Sayılan alanlarda tezsiz yüksek lisans yapanların sürelerinin altı ayı stajdan sayılır.",
     "Uzaktan eğitim yöntemiyle yüksek lisans yapanların sürelerinin altı ayı stajdan sayılır.",
     "Sayılan alanlarda doktora yapanların 18 ayı stajdan sayılır."],
    "2025'te değişen m. 9/d'ye göre Birlik tarafından akredite edilen yabancı dil eğitim programlarında geçen sürelerin "
    "üç ayı stajdan sayılır; tamamı değil. Yüksek lisans ve doktora süreleri aynı bentte düzenlenmiştir.",
    zorluk="hard")

P.q("Staj Yön. m. 9/d",
    "İşletme alanında tezli yüksek lisans yapan (B), bu eğitimden bir yıl stajdan saydırmıştır. (B) ayrıca Birlikçe "
    f"akredite bir yabancı dil programına katılmıştır. {SY}, yabancı dil programındaki süresinin stajdan sayılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yabancı dil süresi ayrıca stajdan sayılmaz.",
    ["Yabancı dil programının üç ayı ayrıca stajdan sayılır.",
     "Yabancı dil programının altı ayı ayrıca stajdan sayılır.",
     "Yabancı dil süresi, yüksek lisans süresinden mahsup edilerek sayılır.",
     "Yabancı dil süresi TESMER Yönetim Kurulunun takdiriyle stajdan sayılabilir."],
    "Staj Yönetmeliği m. 9/d-2'ye göre yüksek lisans süresi hakkından yararlananlar, (1) numaralı alt bentteki yabancı "
    "dil programı hakkından yararlanamaz.",
    zorluk="hard")

P.q("Staj Yön. m. 9/b",
    f"{SY}, Kanunun 6. maddesinin ikinci fıkrasının (a) bendindeki vergi inceleme görevinin vekâleten yerine getirilmesi hâlinde vekâlet sürelerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vekâlet süreleri staj süresinden sayılmaz.",
    ["Vekâlet sürelerinin yarısı staj süresinden sayılır.",
     "Vekâlet süreleri, altı ayı aşmamak üzere stajdan sayılır.",
     "Vekâlet süreleri, TESMER onayıyla tamamen stajdan sayılır.",
     "Vekâlet süreleri ancak yeminli mali müşavirlik için dikkate alınır."],
    "Staj Yönetmeliği m. 9/b'ye göre Kanun m. 6/2-a'da belirtilen görevin vekâleten yerine getirilmesi durumunda vekâlet "
    "süreleri staj süresinden sayılmaz; süreler kurumlarca düzenlenen hizmet cetveliyle belgelendirilir.")

P.q("Staj Yön. m. 10",
    "TESMER'in zorunlu eğitim programının bazı derslerine katılmayan aday (L) hakkında oda işlem yapacaktır. "
    f"{SY}, zorunlu eğitim programına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zorunlu eğitime katılmayan adayın stajı bir yıl süreyle durdurulur.",
    ["Staj konuları, çalışma programları ve zorunlu eğitim programı TESMER tarafından hazırlanır.",
     "Adaylar stajın başladığı tarihten itibaren staj süresince zorunlu eğitime tabi tutulur.",
     "Zorunlu eğitim programı staj süresinin tamamı için bir bütün olarak uygulanır.",
     "TESMER şubeleri ve odalar programları duyurur ve uygulanmasını denetler."],
    "Staj Yönetmeliği m. 10'a göre zorunlu eğitime katılmayan adayların stajı iptal edilir.")

P.q("Staj Yön. m. 11 ve 16",
    f"{SY}, staj başvurusu ve staja başlama dönemleri aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Başvuru nisan, ağustos ve aralıkta; staja başlama mayıs, eylül ve ocakta",
    ["Başvuru ocak, mayıs ve eylülde; staja başlama şubat, haziran ve ekimde",
     "Başvuru mart, temmuz ve kasımda; staja başlama nisan, ağustos ve aralıkta",
     "Başvuru nisan, ağustos ve aralıkta; staja başlama haziran, ekim ve şubatta",
     "Başvuru her ay yapılır; staja başlama başvuruyu izleyen ayın ilk günüdür"],
    "Staj Yönetmeliği m. 11'e göre staj başvuruları her yılın nisan, ağustos ve aralık aylarında yapılır; m. 16'ya göre "
    "staja her yılın mayıs, eylül ve ocak aylarında başlanır.",
    zorluk="hard")

P.q("Staj Yön. m. 11",
    f"{SY}, staj başvuru dilekçesine eklenmesi gereken belgeler arasında aşağıdakilerden hangisi yer almaz?",
    "Adayın mezuniyet not ortalamasını gösteren transkript",
    ["Kanunun aradığı şartları ispata yarayan Birlikçe belirlenen belgeler",
     "Cumhuriyet savcılığından veya e-Devlet üzerinden alınan adli sicil belgesi",
     "Yanında staj yapılacak meslek mensubundan alınan staj onay belgesi",
     "Staj giderlerinin ödendiğini gösteren belge"],
    "Staj Yönetmeliği m. 11'e göre başvuru dilekçesine Birlikçe belirlenen şart belgeleri, adli sicil belgesi, staj onay "
    "belgesi ve staj giderlerinin ödendiğini gösteren belge eklenir. Transkript sayılmamıştır.")

P.q("Staj Yön. m. 13 ve 24",
    "Oda yönetim kurulu, aday meslek mensubu (C)'nin stajını iptal etmiştir. "
    f"{SY}, (C)'nin bu karara karşı başvuru yolu aşağıdakilerden hangisidir?",
    "15 gün içinde Birliğe itiraz; Birliğin 60 günde vereceği karar kesindir.",
    ["Tebliğden itibaren 30 gün içinde TESMER'e itiraz eder; TESMER'in kararı kesindir.",
     "Tebliğden itibaren 7 gün içinde oda disiplin kuruluna itiraz eder.",
     "Tebliğden itibaren 60 gün içinde doğrudan idare mahkemesinde dava açar.",
     "Karar tarihinden itibaren 15 gün içinde oda genel kuruluna itiraz eder."],
    "Staj Yönetmeliği m. 24'e göre iptal kararları 15 gün içinde tebliğ edilir; bu kararlara tebliğden itibaren 15 gün "
    "içinde Birliğe itiraz edilir ve Birliğin 60 gün içinde vereceği karar kesindir (m. 13).")

P.q("Staj Yön. m. 14",
    "(M) Serbest Muhasebeci Mali Müşavirler Odasına bu dönem çok sayıda staj başvurusu gelmiştir. "
    f"{SY}, staj başvurularının incelenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Başvurular üç ay içinde incelenir; yıllık başvurusu bini aşan odalarda 5 kişilik komisyon araştırma yapar.",
    ["Başvurular bir ay içinde incelenir; araştırma her odada oda disiplin kurulunca yapılır.",
     "Başvurular altı ay içinde incelenir; araştırma TESMER tarafından merkezden yapılır.",
     "Başvurular iki ay içinde incelenir; yıllık başvurusu beş yüzü aşan odalarda 3 kişilik komisyon kurulur.",
     "Başvurular üç ay içinde incelenir; araştırma adayın yanında staj yapacağı meslek mensubunca yapılır."],
    "Staj Yönetmeliği m. 14'e göre oda yönetim kurulu, adayın niteliklerini ve meslekle bağdaşmayan işlerle uğraşıp "
    "uğraşmadığını araştırmak üzere bir üyesini görevlendirir; yıllık başvurusu bini aşan odalarda araştırmayı 5 kişilik "
    "inceleme komisyonu yapar; başvurular üç ay içinde incelenir.",
    zorluk="hard")

P.q("Staj Yön. m. 16 ve 24",
    f"{SY}, aday meslek mensubunun stajının iptal edilmesini gerektiren haller arasında aşağıdakilerden hangisi yer almaz?",
    "Staj sırasında bir kez hastalık raporu alınması",
    ["Denetimlerde bir yılda üç kez mücbir sebep olmadan staj yerinde bulunamamak",
     "Verilen belgelerin doğru olmaması veya belgelerde tahrifat yapılması",
     "Eğitim programlarına katılmamak ya da değerlendirmelerde başarısız olmak",
     "Yönetmelikte öngörülen süreyi aşacak şekilde stajına ara vermek"],
    "Staj Yönetmeliği m. 24 staj iptal hâllerini şartların sonradan kaybı, süreyi aşan ara, eğitimlere katılmama veya "
    "başarısızlık, gerçeğe aykırı belge, yılda üç kez mücbir sebepsiz yokluk ve m. 23'e aykırılık olarak sayar. Hastalık "
    "raporu mücbir sebep niteliğinde olup iptal sebebi değildir.")

P.q("Staj Yön. m. 17 (24.02.2025 değişikliği)",
    "Aday meslek mensubu (D)'nin yanında staj yaptığı SMMM vefat etmiş ve (D), kalan staj süresi için yanında staj "
    f"yapabileceği yeni bir meslek mensubu bulamamıştır. {SY}, bu durumda ne olur?",
    "Staj durdurulur; süre bir yıllık ara verme sınırına sayılır.",
    ["Staj tamamlanmış sayılır ve (D) sınava girebilir.",
     "Staj iptal edilir ve (D) staja giriş sınavına yeniden girer.",
     "(D) kalan süreyi TESMER şubesinde eğitim alarak tamamlar.",
     "Staj, oda tarafından görevlendirilen bir meslek mensubunun yanında sürer."],
    "2025'te değişen m. 17'ye göre staj yapılan meslek mensubunun ölümü, işi terki veya meslekten ayrılması hâlinde yeni "
    "bir meslek mensubu bulunamazsa staj durdurulur; durdurma süresi m. 8'deki bir yıllık süre kapsamında değerlendirilir "
    "ve bu süre aşılamaz.",
    zorluk="hard")

P.q("Staj Yön. m. 17/1",
    "Tezkiye notları yüksek olan aday (K), stajını erken bitirebilmek için odaya dilekçe vermiştir. "
    f"{SY}, staj süresinin kısaltılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Staja devam zorunludur; staj süresi kısaltılamaz.",
    ["Başarılı adayların staj süresi TESMER kararıyla altı ay kısaltılabilir.",
     "Staj süresi, tezkiye notu 90'ın üzerindeyse bir yıl kısaltılabilir.",
     "Oda yönetim kurulu, kıdemli meslek mensubu yanında yapılan stajı kısaltabilir.",
     "Staj süresi, aday talep ederse yanında staj yapılan meslek mensubunun onayıyla kısaltılır."],
    "Staj Yönetmeliği m. 17'ye göre staja devam zorunludur ve staj süresi hiçbir şekilde kısaltılamaz; aday, gösterilen "
    "işleri zamanında yapmakla yükümlüdür.")

P.sayisal("Staj Yön. m. 18 (24.02.2025 değişikliği)",
    f"{SY}, Temel Eğitim ve Staj Merkezi (TESMER), Birlik Yönetim Kurulunca meslek mensupları arasından seçilen kaç üye tarafından yönetilir?",
    "7", ["3", "5", "9", "11"],
    "2025'te değişen m. 18'e göre TESMER, Birlik Yönetim Kurulunca meslek mensupları arasından seçilen yedi üye tarafından "
    "yönetilir; üyelerin ücret veya huzur hakları Birlik Yönetim Kurulunca belirlenir.")

P.q("Staj Yön. m. 19",
    "Staja giriş sınavını kazanan (İ), eylül dönemi için yanında staj yapacağı meslek mensubunu belirlemiş ve "
    f"odaya bilgi vermiştir. {SY}, staja başlamaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aday, staj döneminin ilk on günü içinde fiilen başlar.",
    ["Aday, staj dönemini izleyen üç ay içinde istediği tarihte staja başlayabilir.",
     "Aday, staja giriş sınavı sonucunun ilanını izleyen gün staja başlar.",
     "Aday, yanında staj yapacağı meslek mensubunun bildirdiği herhangi bir tarihte başlayabilir.",
     "Aday, staj döneminin ilk otuz günü içinde odaya bildirmek koşuluyla başlayabilir."],
    "Staj Yönetmeliği m. 19'a göre aday meslek mensubu ilgili staj döneminin ilk on günü içinde staja fiilen başlamak "
    "zorundadır; yanında staja başlanan meslek mensubu durumu bir yazıyla odaya bildirir.")

P.q("Staj Yön. m. 20-22",
    f"{SY}, aday meslek mensuplarının özlük hakları ve izinlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Adaya staj süresince ücreti TESMER öder.",
    ["Adaya 4857 sayılı İş Kanunu’na göre izin kullandırılır.",
     "Staj değerlendirmeleri ve odalar arası nakil için ayrıca yedişer gün izin verilir.",
     "Sigorta primlerine ilişkin bildirgeler staj süresince TESMER tarafından takip edilir.",
     "Adaylar TESMER eğitim programlarının giderlerini kendileri karşılar."],
    "Staj Yönetmeliği m. 22'ye göre adaya staj süresince yanında staj yaptığı meslek mensubu tarafından ücret ödenir; "
    "primi ödenmeyen adayın staj yeri değiştirilir ve primi ödemeyen meslek mensubu hakkında disiplin hükümleri "
    "uygulanır.")

P.q("Staj Yön. m. 21 ve 23",
    "Staja devam eden (J), yanında staj yaptığı meslek mensubunun bir müşterisinin kendisine ayrıca iş teklif "
    f"ettiğini belirtmektedir. {SY}, aday meslek mensuplarına ilişkin aşağıdakilerden hangisi yanlıştır?",
    "Aday, izin alarak başka meslek mensubu hesabına çalışabilir.",
    ["Meslek mensupları için öngörülen disiplin esasları adaylara da uygulanır.",
     "Staj sırasında miras yoluyla gelen ticari edinimler bir yıl içinde devredilir.",
     "Aday kendi nam ve hesabına meslek mensuplarının yapabileceği işleri yapamaz.",
     "Kanundaki bağdaşmayan işler adaylar için de geçerlidir."],
    "Staj Yönetmeliği m. 23'e göre adaylar yanında staj yaptıkları kişiler dışındaki meslek mensupları nam ve hesabına "
    "çalışamaz; kendi nam ve hesaplarına da meslek mensuplarının yapabileceği işleri yapamaz.")

P.q("Staj Yön. m. 25",
    f"{SY}, stajın bitimi ve sınava katılmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Stajın bitiminden itibaren ilk beş yıl içinde sınava katılmayanlar güncelleme eğitimi alır.",
    ["Sınava katılmak için stajın son başvuru günü itibarıyla süre yönüyle tamamlanmış olması zorunludur.",
     "Stajını tamamlayanların staj bitiminden itibaren en geç bir yıl içinde sınavlara katılması gerekir.",
     "Güncelleme eğitimi 3 ay süreli olup geçerlilik süresi 2 yıldır.",
     "Bir yıl içinde sınava katılmayanların sınav süresi, sonraki ilk sınav tarihinden resen başlatılır."],
    "Staj Yönetmeliği m. 25'e göre SMMM sınavına stajın bitiminden itibaren ilk 3 yıllık süre içinde katılmayan adayların "
    "sınava girebilmesi için 3 ay süreli güncelleme eğitimini başarıyla tamamlaması gerekir; eğitimin geçerlilik süresi "
    "2 yıldır.",
    zorluk="hard")

P.q("Staj Yön. m. 27 (24.02.2025 değişikliği)",
    "Yanında iki aday meslek mensubu staj yapan SMMM (H), dönem sonunda adaylar için tezkiye düzenleyecektir. "
    f"{SY}, tezkiyelere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tezkiye notları dönem bitimini izleyen bir ay içinde teslim edilir.",
    ["Tezkiye açık olarak düzenlenir ve adaya imzalatılarak odaya gönderilir.",
     "Yanında iki aydan az staj yapan aday için de tezkiye düzenlenir.",
     "Tezkiye notu, adayın talebiyle Birlik Yönetim Kurulunca yükseltilebilir.",
     "80'in altında not veren meslek mensubunun gerekçe bildirmesi gerekmez."],
    "2025 değişiklikleriyle m. 27'ye göre tezkiyeler 100 puan üzerinden, üç aydan az olmamak üzere belirlenen süreler için "
    "gizli olarak düzenlenir; notlar her dönemin bitimini izleyen bir ay içinde teslim edilir; üç aydan az staj yapan "
    "için tezkiye düzenlenmez; 80'in altında not veren meslek mensubu gerekçesini ayrı raporla odaya sunar.",
    zorluk="hard")

P.sayisal("Staj Yön. m. 27",
    f"{SY}, stajdan sayılan hizmet süresi üç yıldan az olan adaylar hakkında tezkiye düzenlenebilmesi için meslek mensubu yanında tamamlanan staj süresinin kaç aydan fazla olması gerekir?",
    "18", ["6", "12", "24", "30"],
    "Staj Yönetmeliği m. 27'nin son fıkrasına göre stajdan sayılan hizmet süresi üç yıldan az olan adaylar hakkında tezkiye "
    "düzenlenmesi ve tezkiyenin yeterlilik sınavında ayrı bir ders gibi ortalamaya katılabilmesi için meslek mensubu "
    "yanında tamamlanan staj süresinin 18 aydan fazla olması gerekir.",
    zorluk="hard")

P.oncul("Staj Yön. m. 8, 16, 19 ve 20",
    "Staja ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Staja her yılın mayıs, eylül ve ocak aylarında başlanır.",
     "Aday meslek mensubu staj döneminin ilk on günü içinde staja fiilen başlar.",
     "Staja toplamda en fazla iki yıl ara verilebilir.",
     "Staj değerlendirmeleri için adaya ayrıca yedi gün izin verilir."],
    f"{SY}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV",
    ["Yalnız II", "I ve III", "II ve IV", "I, II ve IV", "I, III ve IV"],
    "Staj Yönetmeliği m. 16'ya göre staja mayıs, eylül ve ocakta başlanır; m. 19'a göre aday ilk on gün içinde fiilen "
    "başlar; m. 20'ye göre değerlendirme ve nakil için yedişer gün izin verilir. M. 8'e göre ara verme süresi toplamda "
    "en fazla bir yıldır.",
    zorluk="hard")

# ================================================================ SINAV
P.q("Sınav Yön. m. 5/c (24.02.2025 değişikliği)",
    f"{NY}, serbest muhasebeci mali müşavirlik sınavlarında sınav türüne kim karar verir?",
    "Sınav konularına göre sınav türüne Birlik Yönetim Kurulu karar verir.",
    ["Sınav türüne her dönem için Hazine ve Maliye Bakanlığı karar verir.",
     "Sınav türünü sınav komisyonu her ders için oy çokluğuyla belirler.",
     "Sınav türüne TESMER Yönetim Kurulu adayların görüşünü alarak karar verir.",
     "Sınav türü Kanunda test olarak belirlenmiş olup değiştirilemez."],
    "2025'te değişen Sınav Yönetmeliği m. 5/c'ye göre SMMM sınavlarında sınav konularına göre klasik yazılı, test veya "
    "her ikisinin birlikte kullanımına Birlik Yönetim Kurulu karar verir. 2026'dan itibaren test biçimine geçiş bu "
    "yetkiye dayanır.",
    zorluk="hard")

P.q("Sınav Yön. m. 6",
    f"{NY}, aşağıdakilerden hangisi için sınav şartı aranmaz?",
    "Kanunun 8. maddesinde belirtilen yabancı serbest muhasebeci mali müşavirler",
    ["Kanunda sayılan dallarda doktora yapmış olanlar",
     "Beş yıl birinci derece imza yetkili muhasebe müdürü olanlar",
     "TESMER eğitimini dereceyle tamamlayanlar",
     "Staj süresinin yarısını yurt dışında geçirenler"],
    "Sınav Yönetmeliği m. 6'ya göre Kanun m. 8'deki yabancı SMMM'ler ile Geçici 9. maddenin birinci fıkrasının (a) ve (b) "
    "bentlerinde belirtilenler için sınav şartı aranmaz.")

P.q("Sınav Yön. m. 8",
    f"{NY}, sınav zamanlarına ve ilanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yılda üç kez yapılır; en az bir ay önce Resmî Gazete'de ilan edilir.",
    ["SMMM sınavları yılda iki kez yapılır; gün ve yerleri en az on beş gün önce ilan edilir.",
     "YMM sınavları yılda bir kez, SMMM sınavları yılda üç kez yapılır.",
     "Sınavlar yılda dört kez yapılır; ilan Birliğin internet sitesinde yapılır.",
     "Sınav tarihleri her yıl Hazine ve Maliye Bakanlığınca tebliğle ilan edilir."],
    "Sınav Yönetmeliği m. 8'e göre Birlik YMM sınavlarını yılda üç kez, SMMM sınavlarını staj dönemlerini gözeterek yılda "
    "üç kez yapar; sınav günleri ve yerleri en az bir ay önce Resmî Gazete'de ve Birlik ile odaların internet sitelerinde "
    "ilan edilir.")

P.sayisal("Sınav Yön. m. 9 (24.02.2025 değişikliği)",
    f"{NY}, serbest muhasebeci mali müşavirlik sınavına girebilmek için adayın staj değerlendirme notu olarak 100 üzerinden en az kaç almış olması gerekir?",
    "80", ["50", "60", "65", "70"],
    "2025'te değişen Sınav Yönetmeliği m. 9'a göre SMMM sınavına girebilmek için stajı tamamlamış ve yanında staj yapılan "
    "meslek mensubundan 100 üzerinden en az 80 staj değerlendirme notu almış olmak gerekir.")

P.q("Sınav Yön. m. 11 (24.02.2025 değişikliği)",
    f"{NY}, sınav başvurusuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlk sınava tüm konulardan, sonrakilere istenen konulardan başvurulur.",
    ["Adaylar ilk sınava en az dört konudan başvurur; kalan konuları sonraki sınavlarda seçer.",
     "Adaylar her sınava tüm konulardan başvurur; ders seçimi yapılamaz.",
     "Adaylar ilk sınavda istediği konuları seçer; tüm konular iki yıl içinde tamamlanır.",
     "Başvurular odalara dilekçeyle yapılır; elektronik başvuru kabul edilmez."],
    "2025'te değişen m. 11'e göre başvurular Birliğin elektronik sistemleri üzerinden yapılır; adayların ilk sınava "
    "m. 14'teki konuların tümünden başvurmaları zorunludur, müteakip sınavlara istedikleri konulardan başvurabilirler.")

P.q("Sınav Yön. m. 14/b",
    f"{NY}, aşağıdakilerden hangisi serbest muhasebeci mali müşavirlik sınav konuları arasında yer almaz?",
    "Dış Ticaret ve Kambiyo Mevzuatı",
    ["Sermaye Piyasası Mevzuatı", "Finansal Tablolar ve Analizi",
     "Muhasebe Denetimi", "Maliyet Muhasebesi"],
    "Sınav Yönetmeliği m. 14/b'ye göre SMMM sınav konuları Finansal Muhasebe, Finansal Tablolar ve Analizi, Maliyet "
    "Muhasebesi, Muhasebe Denetimi, Vergi Mevzuatı ve Uygulaması, Hukuk, Meslek Hukuku ve Sermaye Piyasası Mevzuatıdır. "
    "Dış Ticaret ve Kambiyo Mevzuatı YMM sınav konusudur.",
    zorluk="easy")

P.q("Sınav Yön. m. 14/a",
    f"{NY}, aşağıdakilerden hangisi yeminli mali müşavirlik sınav konuları arasında yer almaz?",
    "Maliyet Muhasebesi",
    ["Revizyon", "Vergi Tekniği", "Finansal Yönetim", "Yönetim Muhasebesi"],
    "Sınav Yönetmeliği m. 14/a'ya göre YMM sınav konuları İleri Düzeyde Finansal Muhasebe, Finansal Yönetim, Yönetim "
    "Muhasebesi, Denetim-Raporlama ve Meslek Hukuku, Revizyon, Vergi Tekniği, Gelir ve Harcama-Servet Üzerinden Alınan "
    "Vergiler, Dış Ticaret ve Kambiyo Mevzuatı ile Sermaye Piyasası Mevzuatıdır. Maliyet Muhasebesi SMMM sınav konusudur.")

P.q("Sınav Yön. m. 15",
    "SMMM sınavında kopya çektiği tespit edilen (E) hakkında tutanak düzenlenmiştir. "
    f"{NY}, (E) hakkında uygulanacak sonuç aşağıdakilerden hangisidir?",
    "Sınavı geçersiz sayılır ve bir yıl süreyle sınavlara alınmaz.",
    ["Sınavı geçersiz sayılır ve altı ay süreyle sınavlara alınmaz.",
     "Sınav kâğıdı sıfır puanla değerlendirilir ve sonraki sınava girebilir.",
     "Sınavı geçersiz sayılır ve iki yıl süreyle sınavlara alınmaz.",
     "Sınavı geçerli sayılır; hakkında disiplin soruşturması açılır."],
    "Sınav Yönetmeliği m. 15'e göre kopya çekenler ve verenler hakkında tutanak düzenlenir, sınavları geçersiz sayılır, "
    "sınav mahallinden çıkarılır ve bir yıl süreyle sınavlara alınmazlar.")

P.q("Sınav Yön. m. 16",
    f"{NY}, Serbest Muhasebeci Mali Müşavirlik sınavında başarılı olmanın koşulunu gösteren aşağıdaki ifadelerden hangisi doğrudur?",
    "Her konudan en az 50 ve tüm konuların ortalaması en az 60 olmalıdır; tezkiye ayrı ders gibi ortalamaya katılır.",
    ["Her konudan en az 50 ve tüm konuların ortalaması en az 50 olmalıdır; tezkiye ortalamaya katılmaz.",
     "Her konudan en az 60 ve tüm konuların ortalaması en az 60 olmalıdır; tezkiye ortalamaya katılır.",
     "Her konudan en az 50 ve tüm konuların ortalaması en az 65 olmalıdır; tezkiye ortalamaya katılmaz.",
     "Her konudan en az 45 ve tüm konuların ortalaması en az 60 olmalıdır; tezkiye ayrı değerlendirilir."],
    "Sınav Yönetmeliği m. 16/b'ye göre SMMM sınavında her konudan 100 üzerinden en az 50 almak şartıyla tüm konuların "
    "ortalaması en az 60 olmalıdır; tezkiye not ortalaması ayrı bir ders gibi ortalamaya dahil edilir. YMM'de ortalama "
    "şartı 65'tir.")

P.q("Sınav Yön. m. 16/a",
    f"{NY}, yeminli mali müşavirlik sınavında başarılı sayılmak için gereken ortalama aşağıdakilerden hangisidir?",
    "Her konudan en az 50 almak şartıyla ortalamanın en az 65 olması",
    ["Her konudan en az 60 almak şartıyla ortalamanın en az 70 olması",
     "Her konudan en az 50 almak şartıyla ortalamanın en az 60 olması",
     "Her konudan en az 45 almak şartıyla ortalamanın en az 65 olması",
     "Her konudan en az 50 almak şartıyla ortalamanın en az 75 olması"],
    "Sınav Yönetmeliği m. 16/a'ya göre YMM sınavında başarılı sayılmak için her konudan en az 50 almak şartıyla notların "
    "aritmetik ortalamasının en az 65 olması gerekir.")

P.q("Sınav Yön. m. 17",
    f"{NY}, sınav sonuçlarının ilanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sonuçlar sınavın bitiminden itibaren iki ay içinde internet sitelerinde 15 gün süreyle ilan edilir.",
    ["Sonuçlar sınavın bitiminden itibaren bir ay içinde Resmî Gazete'de ilan edilir.",
     "Sonuçlar sınavın bitiminden itibaren üç ay içinde adaylara posta ile bildirilir.",
     "Sonuçlar sınav gününü izleyen on gün içinde odalarda ilan tahtasına asılır.",
     "Sonuçlar sınavın bitiminden itibaren altı hafta içinde internette 30 gün ilan edilir."],
    "Sınav Yönetmeliği m. 17'ye göre sonuçlar sınavın bitiminden itibaren iki ay içinde Birlik ve odaların internet "
    "sitelerinde 15 gün süreyle ilan edilir; sınava girenlerin sayısında artış olursa süre yirmi gün uzatılır.")

P.q("Sınav Yön. m. 20 (24.02.2025 değişikliği)",
    f"{NY}, sınav sonuçlarına itiraz aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Sonuçların açıklanmasından itibaren 7 gün içinde elektronik ortamda Birliğe; 30 gün içinde karara bağlanır.",
    ["Sonuçların açıklanmasından itibaren 15 gün içinde odaya; 60 gün içinde karara bağlanır.",
     "Sonuçların açıklanmasından itibaren 30 gün içinde Bakanlığa; 30 gün içinde karara bağlanır.",
     "Sonuçların açıklanmasından itibaren 10 gün içinde sınav komisyonuna; 15 gün içinde karara bağlanır.",
     "Sonuçların açıklanmasından itibaren 60 gün içinde idare mahkemesine dava açılır."],
    "2025'te değişen Sınav Yönetmeliği m. 20'ye göre itirazlar sonuçların açıklandığı tarihten itibaren 7 gün içinde "
    "elektronik sistemler üzerinden Birliğe yapılır; en geç 30 gün içinde incelenip karara bağlanır ve sonuç elektronik "
    "ortamda bildirilir.",
    zorluk="hard")

P.q("Sınav Yön. m. 21",
    f"{NY}, Serbest Muhasebeci Mali Müşavirlik sınavında başarılı olamayanlar; I. İlk sınav tarihinden itibaren ---- yıl içerisinde, II. Yılda ---- kez açılacak sınavlara girebilirler. III. Bu haklarını süresinde kullanmayanlar veya başarılı olamayanlar ---- ay süreyle meslek sınavlarına alınmazlar. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
    "2, 3, 6",
    ["1, 3, 12", "2, 2, 6", "3, 3, 6", "3, 3, 12"],
    "Sınav Yönetmeliği m. 21'e göre SMMM sınavında başarılı olamayanlar ilk sınav tarihinden itibaren 2 yıl içinde yılda 3 "
    "kez açılacak tüm sınavlara girebilir; bu süre uzatılamaz. Haklarını süresinde kullanmayanlar veya başarısız olanlar "
    "altı ay süreyle meslek sınavlarına alınmaz.")

P.q("Sınav Yön. m. 19",
    f"{NY}, sınavların geçersiz sayılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sorular önceden bilinirse sınav, bilen adaylar için iptal edilir.",
    ["Genel ve özel şartları taşımadığı sonradan anlaşılanların sınavı geçersiz sayılır.",
     "Geçersiz sayılan sınava dayanılarak yapılan işlemler iptal edilir.",
     "Sınavı geçersiz sayılanlar bu sınava dayalı hak talep edemez.",
     "Gerçeğe aykırı beyanda bulunanlar hakkında suç duyurusunda bulunulur."],
    "Sınav Yönetmeliği m. 19'a göre soruların önceden bilindiğinin tespiti hâlinde sınav, katılanların tümü için geçerli "
    "olmak üzere iptal edilir.")

P.q("Sınav Yön. m. 22 (24.02.2025 değişikliği)",
    f"{NY}, sınavlara katılanların belgelerinin saklanmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Birlik 5 yıl saklar; sonra tutanaklar dışındakiler imha edilir.",
    ["Belgeler Birlikçe 10 yıl saklanır ve süre sonunda odalara devredilir.",
     "Belgeler odalarca 3 yıl saklanır ve süre sonunda imha edilir.",
     "Belgeler süresiz saklanır; imha edilmez.",
     "Belgeler Devlet Arşivleri Başkanlığına 2 yıl sonra teslim edilir."],
    "2025'te değişen m. 22'ye göre sınav belgeleri Birlik tarafından 5 yıl saklanır; sürenin bitiminde komisyonca "
    "düzenlenen sonuç tutanakları hariç dijitalleştirilmiş diğer belgeler imha edilir.")

P.q("Sınav Yön. m. 13 ve 15 (24.02.2025 değişikliği)",
    f"{NY}, sınav komisyonu ve sınavların yapılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sınav komisyonu üyelerinin ücretleri her yıl Hazine ve Maliye Bakanlığınca belirlenir.",
    ["Sınav komisyonu gerek gördüğünde üyeleri arasında uzmanlığa göre görev dağılımı yapabilir.",
     "Sınav soruları mühürlü zarflarda saklanır ve adayların huzurunda açılır.",
     "Sınavların yapılmasında ÖSYM'den veya sınav merkezi olan üniversitelerden hizmet alınabilir.",
     "Sınavların hangi illerde yapılacağını Birlik belirler."],
    "Sınav Yönetmeliği m. 13'e göre sınav komisyonu üyelerinin ücretleri Birlik Yönetim Kurulu tarafından her yıl ocak "
    "ayında belirlenir. Görev dağılımı ve ÖSYM'den hizmet alınması 2025 değişiklikleriyle eklenmiştir.")

P.oncul("Sınav Yön. m. 10",
    "Sınav başvurusunda aşağıdaki belgeler değerlendirilmektedir:",
    ["Mükellefiyet tesis tarihini gösterir belge ile kaçakçılık suçlarından hüküm giyilmediğini gösterir belge",
     "Kanun m. 4/d'deki suçları kapsayan ve arşiv bilgilerini içeren adli sicil belgesi",
     "Adayın son üç yıla ait gelir vergisi beyannameleri",
     "SMMM adaylarında stajın tamamlandığına dair belge"],
    f"{NY}, yukarıdakilerden hangileri sınav dosyası için adaylardan istenen belgelerdendir?",
    "I, II ve IV",
    ["Yalnız II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"],
    "Sınav Yönetmeliği m. 10'a göre vergi dairesinden mükellefiyet ve kaçakçılık belgesi, arşiv bilgili adli sicil "
    "belgesi, SMMM adaylarında staj bitirme belgesi, YMM adaylarında on yıllık çalışma belgesi ve Birlikçe istenen diğer "
    "belgeler istenir. Gelir vergisi beyannameleri sayılmamıştır.",
    zorluk="hard")

# ================================================================ SMGE
P.q("SMGE Yön. m. 11 (29.03.2023 değişikliği)",
    f"{GY} kapsamındaki bir meslek mensubunun sürekli mesleki geliştirme eğitimi yükümlülüğü aşağıdakilerden hangisinde doğru olarak verilmiştir?",
    "Yılda en az 30 kredi ve her üç yılda en az 120 kredi",
    ["Yılda en az 15 kredi ve her üç yılda en az 30 kredi",
     "Yılda en az 15 kredi ve her üç yılda en az 45 kredi",
     "Yılda en az 30 kredi ve her üç yılda en az 60 kredi",
     "Yılda en az 30 kredi ve her üç yılda en az 90 kredi"],
    "29.03.2023'te değişen SMGE Yönetmeliği m. 11'e göre meslek mensubu yılda en az 30 ve her üç yılda en az 120 kredilik "
    "eğitim alır; bunların yıllık en az 15, üç yılda en az 60 kredilik kısmı doğrulanabilir olmalıdır. Üç yılda 90 "
    "kredi değişiklikten önceki düzenlemedir.")

P.q("SMGE Yön. m. 11",
    f"{GY}, aşağıdaki ifadelerden hangisi yanlıştır?",
    "Doğrulanabilir eğitimlerin yıllık en az 30 kredi ve üç yılda en az 90 kredi olması gerekir.",
    ["Üç yıllık dönemde Mesleki Çalışma Standartları ve Etik İlkeler konusundan en az 3 kredi gerekir.",
     "Üç yıllık dönemde Denetim ve Güvence Standartları konusundan en az 2 kredi gerekir.",
     "Doğrulanabilir krediler dışındaki en çok 60 kredilik kısım diğer faaliyetlerle ikmal edilir.",
     "Geçici olarak mesleki faaliyetten alıkoyma cezası döneminde de eğitim yükümlülüğü devam eder."],
    "SMGE Yönetmeliği m. 11'e göre doğrulanabilir eğitimlerin yıllık en az 15, üç yılda en az 60 kredilik kısmı "
    "olmalıdır. Etik ve denetim konularındaki asgari krediler, diğer faaliyetlerle ikmal ve alıkoyma döneminde devam eden "
    "yükümlülük aynı maddededir.",
    zorluk="hard")

P.q("SMGE Yön. m. 12",
    f"{GY}, doğrulanabilir eğitimlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üç yıllık dönemde 60 krediyi aşan doğrulanabilir krediler izleyen üç yıla devredilir.",
    ["Yüz yüze ve uzaktan eğitimde her 50 dakikalık ders bir kredi kabul edilir.",
     "Yüz yüze ve uzaktan eğitimlerde bir günde en fazla 7 kredi elde edilebilir.",
     "KGK zorunlu eğitiminde temel konulardan kazanılan krediler doğrulanabilir kredi sayılır.",
     "Doğrulanabilir eğitimler SÜRGEM'in planladığı uzaktan veya odalarda yüz yüze eğitimlerdir."],
    "SMGE Yönetmeliği m. 12/4'e göre üç yıllık dönemde 60 kredinin üzerinde alınan doğrulanabilir krediler izleyen üç "
    "yıla devredilmez; fazla krediler m. 13/a'ya göre kazanıldıkları yıl ve izleyen iki yılda diğer faaliyetler "
    "kapsamında değerlendirilebilir.",
    zorluk="hard")

P.q("SMGE Yön. m. 13",
    f"{GY}, diğer faaliyetler kapsamında elde edilen kredilerle ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?",
    "Stajyer mentorluğu – her ay için 2 kredi, yıllık üst sınır yok",
    ["Birlik veya odaların seminerine katılım – 3 kredi",
     "Birlik veya odaların seminerinde konuşmacılık – 5 kredi",
     "Başarılı olunan her YMM sınav konusu – bir kereye mahsus 10 kredi",
     "Mevzuatın zorunlu kıldığı lisans veya sertifika belgesi – belge başına 5 kredi"],
    "SMGE Yönetmeliği m. 13/d'ye göre stajyer mentorluğu yapanlar her ay için 1 kredi kazanır ve bu krediler yılda 7'yi "
    "geçemez. Diğer eşleştirmeler m. 13/b, e ve g ile uyumludur.",
    zorluk="hard")

P.q("SMGE Yön. m. 13/f",
    f"{GY}, işbaşı eğitimleri kapsamında meslek mensubunun hizmet verdiği müşteriler üzerinden elde edeceği krediye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bir yıl hizmet verilen her müşteri için yıllık 1 kredi; üç yıllık dönemde en fazla 30 kredi",
    ["Hizmet verilen her müşteri için aylık 1 kredi; üç yıllık dönemde en fazla 60 kredi",
     "Hizmet verilen her müşteri için yıllık 2 kredi; üç yıllık dönemde sınır yok",
     "Bir yıl hizmet verilen her müşteri için yıllık 1 kredi; üç yıllık dönemde en fazla 15 kredi",
     "Hizmet verilen her on müşteri için yıllık 1 kredi; üç yıllık dönemde en fazla 10 kredi"],
    "SMGE Yönetmeliği m. 13/f'ye göre meslek mensupları bir yıl süreyle hizmet verdikleri her müşteri için yıllık 1 kredi "
    "elde eder; bu şekilde elde edilen kredi üç yıllık dönemde 30 krediyi geçemez.")

P.q("SMGE Yön. m. 10",
    f"{GY}, eğitim katılım zorunluluğunu yerine getirmeyen çalışanlar listesine kayıtlı meslek mensubu için öngörülen sonuçlar arasında aşağıdakilerden hangisi yer almaz?",
    "Ruhsatının Birlik Yönetim Kurulu kararıyla iptal edilmesi",
    ["Büro tescil belgesinin vize edilmemesi",
     "Çalışanlar listesi kayıt talebinin yerine getirilmemesi",
     "Faaliyet belgesi alma talebinin yerine getirilmemesi",
     "Stajyer mentorluğu yapamaması"],
    "SMGE Yönetmeliği m. 10'a göre katılım zorunluluğu yerine getirilinceye kadar büro tescil belgesi vize edilmez, "
    "çalışanlar listesi kaydı ve faaliyet belgesi talepleri karşılanmaz; eğitimi tamamlamayanlar stajyer mentorluğu "
    "yapamaz. Ruhsat iptali öngörülmemiştir.")

P.q("SMGE Yön. m. 9 ve 24",
    f"{GY}, eğitim yükümlülüğünün başlangıcına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ruhsatın edinildiği yılı izleyen yılın ilk gününden başlar.",
    ["Ruhsatın edinildiği gün başlar ve ilk yıl 30 kredi tam aranır.",
     "Çalışanlar listesine kaydı izleyen üçüncü yıldan başlar.",
     "Staja başlanan tarihten itibaren başlar ve staj süresince devam eder.",
     "Meslek mensubunun talep ettiği yılın başından itibaren başlar."],
    "SMGE Yönetmeliği m. 9'a göre katılım zorunluluğu ruhsatın edinildiği yılı takip eden yılın ilk gününden başlar. "
    "M. 24'e göre ruhsatlı olup çalışmayanlar faaliyete başladıkları yıl yükümlü olur ve ilk yıl 30 kredi şartı aranmaz.")

P.q("SMGE Yön. m. 6 ve 7",
    f"{GY}, Sürekli Mesleki Geliştirme Eğitimi Merkezine (SÜRGEM) ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "SÜRGEM'in işlem ve hesapları Hazine ve Maliye Bakanlığınca denetlenir.",
    ["SÜRGEM Yönetim Kurulu, Birlik Yönetim Kurulunca seçilen yedi üyeden oluşur.",
     "Yönetim kurulu ayda en az iki kez olağan toplantı yapar.",
     "Yönetim kurulu ilk toplantısında başkan, başkan yardımcısı, sekreter ve sayman seçer.",
     "SÜRGEM'in mali kaynakları Birlik bütçesi içinde yer alır."],
    "SMGE Yönetmeliği m. 7'ye göre SÜRGEM'in işlem ve hesapları Birlik Denetleme Kurulu tarafından denetlenir. Yedi üyeli "
    "yönetim kurulu ve ayda iki toplantı m. 6'da, mali kaynaklar m. 22'dedir.")

P.q("SMGE Yön. m. 15",
    f"{GY}, eğitim sertifikasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sertifikanın meslek ruhsatıyla birlikte işyerinde görülebilecek yerde asılı bulundurulması zorunludur.",
    ["Sertifika her yıl yenilenir ve meslek mensubunun evinde saklanır.",
     "Sertifika her beş yıllık dönem için Birlik Genel Kurulunca verilir.",
     "Sertifika ancak doğrulanabilir kredisi 120'yi aşan meslek mensuplarına verilir.",
     "Sertifikada krediler üç yıl için toplu olarak ve oda vizesi olmadan gösterilir."],
    "SMGE Yönetmeliği m. 15'e göre her üç yıllık süreç için ilk yılın tamamlanmasından itibaren oda tarafından eğitim "
    "sertifikası verilir; krediler her yıl ayrı belirtilir ve oda tarafından vize edilir; sertifikanın meslek ruhsatıyla "
    "birlikte işyerinde görülebilecek yerde asılı bulundurulması zorunludur.")

P.q("SMGE Yön. Geçici m. 2 (14.01.2026 ek madde)",
    f"{GY}, 14.01.2026'da eklenen geçici maddeye göre eğitim yükümlülüklerini tamamlamamış olan meslek mensuplarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İzleyen yıl içinde eksiği tamamlarsa süresinde tamamlamış sayılır.",
    ["Eksik kredileri silinir ve yeni üç yıllık dönem baştan başlar.",
     "Eksik krediler için bir kereye mahsus idari para cezası ödenerek yükümlülük sona erer.",
     "Eksik kredilerin iki katını izleyen üç yıl içinde tamamlaması gerekir.",
     "Eksik kredisi olanların büro tescil belgesi iptal edilir."],
    "SMGE Yönetmeliğine 14.01.2026'da eklenen Geçici Madde 2'ye göre maddenin yürürlüğe girdiği tarihte m. 11'deki "
    "yükümlülükleri tamamlamamış olanlar, yürürlük tarihini izleyen yıl içinde eksik kredilerini tamamlarlarsa "
    "yükümlülüklerini süresinde tamamlamış kabul edilir.",
    zorluk="hard")

P.oncul("SMGE Yön. m. 11 ve 12",
    "Sürekli mesleki geliştirme eğitimine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Meslek mensubu yılda en az 30 kredilik eğitim almalıdır.",
     "Her üç yılda alınması gereken asgari kredi 90'dır.",
     "Yüz yüze eğitimde bir günde en fazla 7 kredi elde edilebilir.",
     "Doğrulanabilir eğitimlerin üç yılda en az 60 kredilik kısmı olmalıdır."],
    f"{GY}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV",
    ["Yalnız I", "I ve II", "II ve III", "I, III ve IV", "II, III ve IV"],
    "SMGE Yönetmeliği m. 11'e göre yılda en az 30, üç yılda en az 120 kredi alınır ve doğrulanabilir kısım üç yılda en az "
    "60 kredidir; m. 12'ye göre günde en fazla 7 kredi elde edilebilir. Üç yılda 90 kredi 2023 değişikliğinden önceki "
    "düzenlemedir.",
    zorluk="hard")

P.q("SMGE Yön. m. 2 ve 24",
    f"{GY}, sürekli mesleki geliştirme eğitiminden muafiyete ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kapsam dışındakiler SÜRGEM'e bildirerek muaf tutulur.",
    ["Muafiyet ancak altmış yaşını dolduran meslek mensupları için oda kararıyla verilir.",
     "Muafiyet Birlik Genel Kurulunun her dönem aldığı kararla belirlenir.",
     "Ruhsatlı olup çalışmayanlar da eğitime katılır; muafiyet yoktur.",
     "Muaf olan meslek mensupları eğitimlere katılamaz."],
    "SMGE Yönetmeliği m. 2/2 ve m. 24'e göre kapsam dışındaki meslek mensupları eğitimden muaftır ve SÜRGEM'e bildirerek "
    "muaf tutulur; dilerlerse eğitimlere katılabilirler.")

P.q("Staj Yön. m. 15 (24.02.2025 değişikliği)",
    f"{SY}, adayların yanında staj yapabileceği meslek mensuplarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "YMM veya SMMM yanında ya da denetim ve gözetiminde yapılır.",
    ["Staj, en az on yıl kıdemli SMMM'ler yanında yapılır; kuralları oda genel kurulu belirler.",
     "Staj, TESMER şubelerinde yapılır; meslek mensubu yanında staj istisnai olarak mümkündür.",
     "Staj, çalışanlar listesine kayıtlı olmayan meslek mensupları yanında da yapılabilir.",
     "Staj, yeminli mali müşavirlerin denetim ve gözetimiyle sınırlı olarak yapılabilir."],
    "Staj Yönetmeliği m. 15'e göre SMMM adayları stajlarını YMM veya SMMM'lerin yanında ve/veya onların denetim ve "
    "gözetiminde yapabilir; 2025 değişikliğiyle yanında staj yapılacaklara ilişkin kuralları Birlik Yönetim Kurulu "
    "belirler.")

P.q("Staj Yön. m. 17/2 (24.02.2025 değişikliği)",
    "Aday meslek mensubu (F), yanında staj yaptığı meslek mensubunun staj programına uymadığı ve kendisine uygunsuz "
    f"davrandığı kanaatindedir. {SY}, (F)'nin başvuracağı yol aşağıdakilerden hangisidir?",
    "Durumu dilekçeyle oda yönetim kuruluna bildirir; oda soruşturma yapar.",
    ["Durumu doğrudan Birlik Disiplin Kuruluna şikâyet eder ve karar verilene kadar staja ara verir.",
     "Stajı bırakıp başka bir meslek mensubunun yanında oda onayı aramaksızın devam eder.",
     "Durumu TESMER Yönetim Kuruluna bildirir; TESMER meslek mensubuna disiplin cezası verir.",
     "Staj sözleşmesini feshederek iş mahkemesinde dava açar ve sonucunu bekler."],
    "2025'te değişen m. 17'ye göre staj programına uyulmadığı veya meslek mensubunun uygun olmayan davranışlarda "
    "bulunduğu kanaatine varan aday durumu dilekçeyle oda yönetim kuruluna bildirir; oda gerekli soruşturmayı yapar ve "
    "staja ilişkin tedbirleri alır.")

P.q("Sınav Yön. m. 21",
    f"{NY}, sınav haklarını süresinde kullanmayanlar veya başarılı olamayanlar altı aylık süreyi doldurduktan sonra nasıl sınava katılır?",
    "Dilerlerse tüm konuları kapsamak üzere yeniden sınavlara katılabilir.",
    ["Başarısız oldukları konulardan sınava girer; başarılı konular saklı kalır.",
     "Stajı yeniden yapmadan sınava katılamazlar.",
     "Bir kereye mahsus olarak tek oturumlu bir telafi sınavına girerler.",
     "Oda yönetim kurulunun izniyle en fazla iki konudan sınava girebilirler."],
    "Sınav Yönetmeliği m. 21'e göre altı aylık süreyi dolduranlardan dileyenler yeniden tüm konuları kapsamak üzere "
    "sınavlara katılabilir; önceki başarılı konular saklı kalmaz.")

P.q("SMGE Yön. m. 8",
    f"{GY}, aşağıdakilerden hangisi sürekli mesleki geliştirme eğitim programlarının sınıflandırmasında yer almaz?",
    "Ticari Faaliyet ve Şirket Yönetimi Eğitim Programı",
    ["Mesleki Çalışma Standartları ve Etik İlkeler Eğitim Programı",
     "Mevzuat Eğitim Programı",
     "Muhasebe ve Finansal Raporlama Eğitim Programı",
     "Denetim; Denetim ve Güvence Standartları Eğitim Programı"],
    "SMGE Yönetmeliği m. 8 programları mesleki ve teknik bilgiler, yeni teknikler, kamu güveni ve kalite, çalışma "
    "standartları ve etik, kişisel gelişim, ulusal ve uluslararası standartlar, bilgi teknolojileri ve yabancı dil, "
    "mevzuat, muhasebe ve finansal raporlama ile denetim programları olarak sınıflandırır.")

P.q("SMGE Yön. m. 11/5",
    f"{GY}, 120 kredilik üç yıllık yükümlülüğün sağlanıp sağlanmadığının değerlendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Değerlendirme her yıl, eğitime tabi olunan önceki iki yıl da dahil edilerek yapılır.",
    ["Değerlendirme üç yılda bir, dönem sonunda toplu olarak yapılır.",
     "Değerlendirme her yıl, o yılın kredileriyle sınırlı olarak yapılır.",
     "Değerlendirme meslek mensubunun talebi hâlinde oda yönetim kurulunca yapılır.",
     "Değerlendirme beş yıllık dönemler itibarıyla Birlik Genel Kurulunca yapılır."],
    "SMGE Yönetmeliği m. 11/5'e göre 120 kredinin sağlanıp sağlanmadığına ilişkin değerlendirme her yıl, eğitime tabi "
    "olunan önceki iki yıl da dahil edilerek yapılır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
