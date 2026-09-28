# -*- coding: utf-8 -*-
"""Meslek Hukuku · Çalışma Usul ve Esasları — 60 soru, 2026 test biçimi.

Dayanak metinler (28.09.2026 kontrolü, TÜRMOB 2026 derlemesi):
  · SMMM ve YMM'lerin Çalışma Usul ve Esasları Hakkında Yönetmelik (RG 03.01.1990/20391;
    24.02.2025-32823 ve 14.01.2026-33137 değişiklikleri işlenmiş)
  · SMMM ve YMM Mesleklerine İlişkin Haksız Rekabet ve Reklam Yasağı Yönetmeliği
    (RG 21.11.2007/26707; 24.02.2025-32823 değişikliği işlenmiş)
  · SM, SMMM ve YMM Ücretlerinin Esasları Hakkında Yönetmelik (RG 02.01.1990/20390)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_calisma_usulleri_2026.json", lesson="meslek_hukuku", topic="calisma_usulleri",
          konu_adi="Çalışma Usul ve Esasları", seed=2026092802,
          surum="Çalışma Usul ve Esasları Yön. (14.01.2026-33137 işlenmiş), Haksız Rekabet ve Reklam Yasağı Yön. (24.02.2025 işlenmiş), Ücret Esasları Yön.; 28.09.2026 kontrolü")

CU = "Serbest Muhasebeci Mali Müşavir ve Yeminli Mali Müşavirlerin Çalışma Usul ve Esasları Hakkında Yönetmelik’e göre"
HR = "Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Mesleklerine İlişkin Haksız Rekabet ve Reklam Yasağı Yönetmeliği’ne göre"
UY = "Serbest Muhasebeci, Serbest Muhasebeci Mali Müşavir ve Yeminli Mali Müşavir Ücretlerinin Esasları Hakkında Yönetmelik’e göre"

# ================================================================ Çalışma Usul ve Esasları
P.q("Çalışma Usul ve Esasları Yön. m. 11 (14.01.2026 değişikliği)",
    f"{CU}, odada tutulan kayıtlara ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Kayıtlı her üye meslek kütüğüne, fiilen faaliyette bulunanlar ayrıca çalışanlar listesine yazılır.",
    ["Meslek kütüğüne fiilen mesleki faaliyette bulunanlar, çalışanlar listesine ise ruhsat alıp faaliyette bulunmayanlar kaydedilir.",
     "Ortaklık büroları ve şirketler çalışanlar listesine değil, meslek kütüğünün ayrı bir bölümüne kaydedilir.",
     "Çalışanlar listesine kayıt için başvuru ruhsatın verildiği odaya yapılır, işyerinin bağlı olduğu oda yetkili değildir.",
     "Meslek kütüğü Birlik tarafından, çalışanlar listesi ise her oda tarafından ayrı ayrı tutulur."],
    "2026 değişikliğiyle m. 11'e göre odada, odaya kayıtlı her meslek mensubunun kaydedildiği meslek kütüğü ile "
    "fiilen mesleki faaliyette bulunanların yazıldığı çalışanlar listesi tutulur; ortaklık büroları ve şirketler "
    "çalışanlar listesinin ayrı bölümüne kaydolur. Başvuru işyerinin bağlı olduğu odaya yapılır.")

P.q("Çalışma Usul ve Esasları Yön. m. 11",
    f"{CU}, çalışanlar listesine kayıt başvurusunda dilekçeye eklenecek belgelerle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Adli sicil belgesinin 90 günden eski olmaması yeterlidir.",
    ["Başvuru dilekçesi elektronik sistemler üzerinden de alınabilir.",
     "Dilekçeye bildirim formu eklenir.",
     "Yeminli mali müşavirler yemin ettiklerine dair belgeyi ekler.",
     "Adli sicil belgesi e-Devlet sistemi üzerinden de alınabilir."],
    "M. 11'e göre dilekçeye bildirim formu, arşiv bilgisini içeren ve alınmasının üzerinden 30 gün geçmemiş adli "
    "sicil belgesi ve YMM'ler için yemin belgesi eklenir; dilekçe elektronik sistemler üzerinden de alınabilir.")

P.sayisal("Çalışma Usul ve Esasları Yön. m. 14 (24.02.2025 değişikliği)",
    f"{CU}, her meslek mensubu mesleki faaliyetine başlamadan önce bağlı olduğu oda bilgisinde iş yeri açmak zorundadır. "
    "İşyeri açılış ve kapanışları en geç kaç gün içinde odaya bildirilir?",
    "30", ["7", "15", "45", "60"],
    "24.02.2025 değişikliğiyle m. 14'e eklenen hükme göre işyeri açılış ve kapanışları en geç otuz gün içinde odaya "
    "bildirilir. Adres değişikliklerinin bildirimi için de aynı maddede otuz günlük süre öngörülür.")

P.q("Çalışma Usul ve Esasları Yön. m. 14 (14.01.2026 değişikliği)",
    f"{CU}, meslek mensuplarının büroları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Meslek mensupları ve ortaklık büroları, odaya bildirmek koşuluyla irtibat bürosu açabilir.",
    ["Açılan işyerleri bağımsız büro şeklinde olup başka bir serbest meslek faaliyetiyle iç içe olamaz.",
     "Bir meslek mensubunun birden fazla bürosu olamaz; birlikte çalışanlar da ayrı büro edinemez.",
     "Büro edinen meslek mensupları odaya kayıttan itibaren üç ay içinde Büro Tescil Belgesi alır.",
     "Birlik Yönetim Kurulu ev-ofis veya paylaşımlı ofis kullanım şartlarını belirlemeye yetkilidir."],
    "M. 14'e göre meslek mensupları, ortaklık büroları ve şirketler hiçbir şekilde irtibat bürosu açamaz. Bağımsız büro, "
    "tek büro, üç ay içinde Büro Tescil Belgesi alınması ve 2026'da eklenen ev-ofis/paylaşımlı ofis yetkisi aynı "
    "maddededir.")

P.q("Çalışma Usul ve Esasları Yön. m. 14 (24.02.2025 değişikliği)",
    "İstanbul Serbest Muhasebeci Mali Müşavirler Odasına kayıtlı (M) Muhasebe ve Danışmanlık Ltd. Şti., Bursa'da şube "
    f"açmak istemektedir. {CU}, şube açılabilmesi için aşağıdakilerden hangisi gerekir?",
    "Bursa odasının çalışanlar listesine kayıtlı, şirketi temsil ve ilzama yetkili ve Bursa'da ikamet eden bir ortağın görevlendirilmesi",
    ["Bursa odasının çalışanlar listesine kayıtlı ve şirkette bağımlı olarak çalışan bir meslek mensubunun, ortaklık şartı aranmadan şube sorumlusu yapılması",
     "İstanbul odasının çalışanlar listesine kayıtlı herhangi bir ortağın şube sorumlusu olarak Bursa odasına bildirilmesi",
     "Birlik Yönetim Kurulundan izin alınması ve şubede en az iki meslek mensubunun istihdam edilmesi",
     "Bursa odasının yönetim kurulunun, şubenin açılacağı ildeki meslek mensubu sayısını dikkate alarak onay vermesi"],
    "M. 14'e göre şirket kayıtlı olduğu il sınırları içinde şube açamaz; başka ilde şube açabilmesi o ildeki odanın "
    "çalışanlar listesine kayıtlı, şirketi temsil ve ilzama yetkili bir ortak görevlendirmesine bağlıdır. 2025 "
    "değişikliğiyle şubeden sorumlu ortağın o ilde ikamet etmesi de zorunludur.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 14",
    f"{CU}, Büro Tescil Belgesine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Odaya kayıttan itibaren üç ay içinde alınır ve iki yılda bir vize ettirilir.",
    ["Odaya kayıttan itibaren bir ay içinde alınır ve her yıl vize ettirilir.",
     "Odaya kayıttan itibaren altı ay içinde alınır ve üç yılda bir vize ettirilir.",
     "Vergi dairesinde mükellefiyet tesisinden sonra alınır ve beş yılda bir yenilenir.",
     "Odaya kayıttan itibaren üç ay içinde alınır ve dört yılda bir vize ettirilir."],
    "M. 14'e göre büro edinen meslek mensupları odaya kayıt olduktan itibaren üç ay içinde Büro Tescil Belgesi alır; "
    "belge iki yılda bir vize ettirilir. 2026 değişikliğiyle odalar bu işlemleri elektronik ortamda da yapabilir.")

P.q("Çalışma Usul ve Esasları Yön. m. 15",
    f"{CU}, meslek mensuplarının tabela kullanımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tabela asılması zorunludur ve tabelada büro telefon numarasına yer verilemez.",
    ["Tabelaların mavi zemin üzerine beyaz yazılı olması zorunludur.",
     "Tabelada Birlik adına tescilli Mm logosunun kullanılması zorunludur.",
     "Bina cephelerine birden fazla tabela asılamaz, ışıklı tabela kullanılamaz.",
     "Ortaklık şeklinde çalışılıyorsa ortaklık unvanının tabelada yer alması zorunludur."],
    "M. 15'e göre tabela asılması ihtiyaridir; asılırsa telefon numarası, adres, internet ve e-posta adresi yer "
    "alabilir. Mavi zemin-beyaz yazı, Mm logosu, cephe ve ışıklı tabela yasağı ile ortaklık unvanı zorunluluğu aynı "
    "maddededir.")

P.q("Çalışma Usul ve Esasları Yön. m. 15/e (24.02.2025 değişikliği)",
    f"{CU}, meslek mensuplarının mesleki unvanları yanında kamu tüzel kişilerinden aldıkları lisans ve ruhsat gibi "
    "belgelerle edindikleri unvanları tabelada kullanmalarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu unvanlardan biri, o işi fiilen icra etmek koşuluyla kullanılabilir.",
    ["Bu unvanların tamamı, mesleki unvan kullanılmasa da tabelada gösterilebilir.",
     "Bu unvanlar tabelada gösterilemez; basılı evrakta ise iki tanesine kadar kullanılabilir.",
     "Bu unvanlardan en çok ikisi, odaya bildirilmek koşuluyla tabelada kullanılabilir.",
     "Bu unvanlar ancak akademik unvan bulunmayan meslek mensuplarınca kullanılabilir."],
    "2025 değişikliğiyle eklenen m. 15/e'ye göre meslek mensupları mesleki unvanlarını kullanmak şartıyla, mesleğin "
    "konusuna giren alanlarda kamu tüzel kişilerinden edindikleri unvanlardan sadece birini kullanabilir; bu unvana "
    "ilişkin işi fiilen icra ediyor olmaları şarttır.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 16 (24.02.2025 değişikliği)",
    f"{CU}, aşağıdaki durumlardan hangisinde meslek mensubuna yeni kimlik belgesi verilmez?",
    "Aynı oda bölgesi içinde büro adresinin değişmesi",
    ["İşyerinin başka bir oda bölgesine nakledilmesi",
     "Meslek mensubunun soyadının evlilik nedeniyle değişmesi",
     "Meslek mensubunun adının mahkeme kararıyla değişmesi",
     "Meslek mensubunun işyerini başka bir ildeki odaya taşıması"],
    "M. 16'ya göre işyerinin başka oda bölgesine nakli ile isim veya soyadı değişikliğinde yeni kimlik belgesi verilir, "
    "eskisi iptal edilir. Aynı oda bölgesinde adres değişikliği yeni kimlik belgesi gerektirmez; odaya otuz gün "
    "içinde bildirilir.")

P.q("Çalışma Usul ve Esasları Yön. m. 18 ve 19",
    f"{CU}, aşağıdakilerden hangisi serbest muhasebeci mali müşavirlerin çalışma konuları arasında yer almaz?",
    "Mali tablo ve beyannameleri tasdik etmek",
    ["İşletmelerin defterlerini tutmak, mali tablo ve beyannamelerini düzenlemek",
     "İşletmelerin muhasebe sistemlerini kurmak ve geliştirmek",
     "Mali tablo ve beyannamelerle ilgili konularda yazılı görüş vermek",
     "Tahkim, bilirkişilik, değerleme ve derecelendirme işlerini yapmak"],
    "Tasdik m. 19/c'de yalnız yeminli mali müşavirlerin çalışma konusu olarak sayılmıştır. Defter tutma, sistem kurma, "
    "yazılı görüş, tahkim, bilirkişilik, değerleme ve derecelendirme m. 18'de SMMM'lerin çalışma konularıdır.")

P.q("Çalışma Usul ve Esasları Yön. m. 20",
    f"{CU}, bildirim mecburiyeti ve defterlerin tutulma yerine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Defter tutma ve sistem kurma işleri işletme sahibinin işyerinde de yapılabilir.",
    ["SMMM'ler defter tutma işini bürolarında yapar; işletmenin işyerinde defter tutulamaz.",
     "Müşterilerle yapılan sözleşmelerin bilgileri odaya değil, doğrudan vergi dairesine iletilir.",
     "Sözleşme bilgilerinin odaya iletilmesi, sözleşme bedeli asgari tarifeyi aşıyorsa gerekir.",
     "Tutulan defter ve belgelerin muhafazası, sözleşmede açıkça düzenlenmişse meslek mensubuna aittir."],
    "M. 20'ye göre meslek mensupları sözleşme bilgilerini Birliğin belirlediği usulle odalara iletir; SMMM'ler Kanun "
    "m. 2/A-a ve b'deki işleri bürolarında veya işletme sahiplerinin işyerlerinde yapabilir ve tuttukları defter ve "
    "belgeleri itinalı şekilde muhafaza eder.")

P.q("Çalışma Usul ve Esasları Yön. m. 22",
    f"{CU}, meslek mensuplarının işyerlerinde çalıştırabilecekleri kişilere ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Mesleki faaliyet için gerekli yardımcı elemanları çalıştırabilirler; öncelik ruhsatlı veya stajyer meslek mensubunundur.",
    ["Yardımcı eleman sayısı, meslek mensubunun müşteri sayısına göre oda yönetim kurulunca belirlenir.",
     "Mesleği yapmaları yasaklananlar, oda yönetim kurulunun izniyle yardımcı eleman olarak çalıştırılabilir.",
     "Yardımcı eleman olarak ancak stajyer meslek mensupları çalıştırılabilir; diğer kişiler istihdam edilemez.",
     "Yardımcı elemanların işe alınması, bağlı olunan oda tarafından açılan sınavda başarılı olmalarına bağlıdır."],
    "M. 22'ye göre meslek mensupları mesleki faaliyetleri için gerekli yardımcı elemanları çalıştırabilir, mesleği "
    "yapmaları yasaklananları çalıştıramaz; çalıştırılacak kişilerde öncelik ruhsatlı veya stajyer meslek mensubunundur.")

P.q("Çalışma Usul ve Esasları Yön. m. 23",
    f"{CU}, iş kabulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Meslek mensubu iş teklifini reddederse gerekçesini yazılı olarak iş sahibine ve odaya bildirir.",
    ["Meslek mensubu gerek duyarsa müşterinin kim olduğunu önceki meslek mensubundan sorup öğrenebilir.",
     "İki meslek mensubu tarafından reddedilen iş sahibine oda meslek mensubu belirler.",
     "İş kabulü ve reddine ilişkin uygulama esasları Birlikçe mecburi meslek kararıyla belirlenir.",
     "Bağımlı çalıştığı bürodan ayrılan meslek mensubu iki yıl, eski işvereninin rızası olmadan onun müşterisine hizmet veremez."],
    "M. 23'e göre meslek mensupları iş teklifini gerekçe göstermeden reddedebilir; ret kararı iş sahibine gecikmeden "
    "bildirilir. Önceki meslek mensubuyla görüşme, iki retten sonra odanın görevlendirmesi, iki yıllık rıza kuralı ve "
    "mecburi meslek kararı aynı maddededir.")

P.q("Çalışma Usul ve Esasları Yön. m. 25",
    f"{CU}, aşağıdakilerden hangisi sözleşmede bulunması gereken asgari bilgiler arasında sayılmamıştır?",
    "Tarafların banka hesap numaraları",
    ["Tarafların vergi daireleri ve sicil numaraları",
     "Yapılacak işlerin amacı ve kapsamı",
     "Tarafların karşılıklı sorumlulukları",
     "Sözleşme yeri, tarihi ve süresi"],
    "M. 25'e göre sözleşmede tarafların açık adresleri, vergi daireleri ve sicil numaraları; işlerin amacı ve kapsamı; "
    "karşılıklı sorumluluk ve yükümlülükler; ücret tutarı ve ödeme şekli; sözleşme yeri, tarihi ve süresi bulunur. "
    "Banka hesap numarası sayılmamıştır.")

P.q("Çalışma Usul ve Esasları Yön. m. 26",
    f"{CU}, sözleşmenin feshine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ücretin ödenmemesi, meslek mensubu açısından haklı fesih sebebi sayılmaz.",
    ["Taraflar haklı nedenlerle veya karşılıklı rızayla sözleşmeyi feshedebilir.",
     "Fesihte defter ve belgeler bir ay içinde devir teslim tutanağıyla sahibine verilir.",
     "Devir teslim gerçekleşmezse durum meslek mensubunca odaya bildirilir.",
     "Tarafların tazminat hakları genel hukuk kurallarına tabidir."],
    "M. 26'ya göre ücretin ödenmemesi ve tevdi edilen belgelerin sağlıklı ve güvenilir olmaması meslek mensubunun "
    "haklı fesih gerekçesidir. Diğer ifadeler aynı maddede düzenlenmiştir.")

P.sayisal("Çalışma Usul ve Esasları Yön. m. 27",
    f"{CU}, meslek mensubu defter ve belgelerin geri alınmasını sahibine yazı ile bildirmişse, saklama yükümlülüğü "
    "bildirme tarihinden itibaren kaç ay içinde sona erer?",
    "1", ["2", "3", "6", "12"],
    "M. 27'ye göre defter ve belgelerin geri alınması sahibine yazıyla bildirilmişse saklama mükellefiyeti bildirimden "
    "itibaren bir ay içinde sona erer. İşin bitiminden itibaren bir ay içinde alınmayan defter ve belgeler yazıyla "
    "ilgilinin vergi dairesine teslim edilir.")

P.q("Çalışma Usul ve Esasları Yön. m. 27",
    "Serbest muhasebeci mali müşavir (K), müşterisiyle sözleşmesi sona erdiği hâlde müşteri defter ve belgelerini işin "
    f"bitiminden itibaren bir ay içinde almamıştır. {CU}, (K)'nin bu defter ve belgeler için yapması gereken işlem aşağıdakilerden hangisidir?",
    "Defter ve belgeleri bir yazı ile müşterinin bağlı olduğu vergi dairesine teslim eder.",
    ["Defter ve belgeleri noter aracılığıyla müşterinin iş adresine gönderir.",
     "Defter ve belgeleri odaya teslim eder ve oda müşteriyi yazıyla bilgilendirir.",
     "Defter ve belgeleri beş yıl süreyle kendi bürosunda saklamaya devam eder.",
     "Defter ve belgeleri müşterinin yeni meslek mensubuna tutanakla devreder."],
    "M. 27'ye göre işin bitiminden itibaren bir ay içinde sahipleri tarafından alınmayan defter ve belgeler bir yazı ile "
    "ilgililerin bağlı olduğu vergi dairesine teslim edilir.")

P.q("Çalışma Usul ve Esasları Yön. m. 30/b (24.02.2025 değişikliği)",
    f"{CU}, yeminli mali müşavirler ile serbest muhasebeci mali müşavirlerin birlikte kurdukları şirketlere ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu şirketlerde tasdik hizmeti verilebilir; defter tutma işi ise yapılamaz.",
    ["Bu şirketlerde Kanun m. 2/A-a'da yazılı defter tutma işleri yapılamaz.",
     "Şirket, merkezinin bulunduğu ilde hisse çoğunluğuna sahip meslek grubunun odasına kaydedilir.",
     "Ortaklar, şirketin tescilini takip eden 30 gün içinde ortaklık durumlarını kayıtlı oldukları odaya bildirir.",
     "Şirket unvanında hisselerin yarısından fazlasına sahip meslek grubunun unvanı kullanılır."],
    "2025 değişikliğiyle m. 30/b'ye göre YMM ve SMMM'lerin birlikte kurduğu şirketlerde tasdik hizmeti verilemez ve "
    "defter tutma işleri yapılamaz. Oda kaydı, 30 günlük bildirim ve unvan kuralı m. 30/b ve g'de düzenlenmiştir.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 30",
    f"{CU}, ortaklık bürosu veya şirket kurarak mesleki faaliyette bulunmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Varislere intikal eden hisseler üç yıl içinde tasfiye edilir.",
    ["Meslek mensuplarının bu büro veya şirketlerde sürdürdükleri faaliyetler ticari faaliyet sayılmaz.",
     "Ortaklık bürosu ancak aynı unvana sahip meslek mensupları arasında kurulabilir.",
     "Ortaklık bürosu veya şirketlerde yapılan işlerden doğan cezai sorumluluk işi yapan meslek mensubuna aittir.",
     "Mesleki şirketler ve ortaklık büroları başka mesleki şirket ve ortaklık bürolarına ortak olmazlar."],
    "M. 30/e'ye göre varislere intikal eden hisseler en geç bir yıl içinde tasfiye edilir; bu süre içinde mirasçılar "
    "meslek mensubu sayılmaz ve mesleki faaliyette bulunamaz. Diğer ifadeler m. 30 ve 2026'da eklenen fıkrada yer alır.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 30 (14.01.2026 ek fıkra)",
    "SMMM (L), Konya'daki bürosunda bireysel olarak mesleki faaliyet yürütmektedir. (L), farklı bir adreste kurulu bir "
    f"mesleki şirkete ortak olarak orada da faaliyette bulunmak istemektedir. {CU}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Farklı adresteki şirkette mesleki faaliyette bulunamaz; aynı adreste kurulu şirkete ortak olarak faaliyet yürütebilir.",
    ["Farklı adresteki şirkete ortak olabilir ve bireysel bürosunu kapatmadan orada da mesleki faaliyet yürütebilir.",
     "Şirketin ortaklarının çoğunluğu aynı unvana sahipse farklı adresteki şirkette de faaliyet yürütebilir.",
     "Oda yönetim kurulundan izin alırsa farklı adresteki şirkette ve bireysel bürosunda birlikte çalışabilir.",
     "Bireysel büro faaliyeti bulunan meslek mensubu, adresi ne olursa olsun mesleki şirkete ortak olamaz."],
    "2026'da m. 30'a eklenen fıkraya göre bireysel büro faaliyeti bulunan meslek mensubu farklı bir adreste mesleki "
    "şirket kurarak veya kurulu şirkete ortak olarak orada faaliyette bulunamaz; aynı adreste şirket kurması veya "
    "ortak olması mümkündür. Bağımsız denetim amaçlı mesleki şirkette yetki kullanımı ayrıca serbesttir.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 33 ve 34",
    f"{CU}, başka odaya nakle ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Nakil talebinin reddine karşı otuz gün içinde oda genel kuruluna itiraz edilir.",
    ["Başvurulan oda yönetim kurulu bir ay içinde karar vermezse nakil talebi kabul edilmiş sayılır.",
     "Eski oda, kayıt bildirimi üzerine meslek mensubunun adını kayıtlardan siler ve dosyasını gönderir.",
     "Devam eden disiplin soruşturması eski odaca sürdürülür ve sonucu yeni odaya bildirilir.",
     "Mesleki faaliyette bulunmayanların ikametgâh değişikliğinde nakil yoluyla kayıt ihtiyaridir."],
    "M. 34'e göre nakil talebinin reddine karşı meslek mensubu tebliğden itibaren on beş gün içinde Birliğe itiraz eder; "
    "Birlik on beş gün içinde nihai karar verir. Bir aylık zımni kabul, dosya nakli ve devam eden soruşturma m. 33'te, "
    "ihtiyari nakil m. 32'dedir.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 35",
    f"{CU}, aşağıdakilerden hangisi meslek mensubunun adının çalışanlar listesinden silinmesini gerektiren haller arasında yer almaz?",
    "Meslek mensubuna kınama cezası verilmiş olması",
    ["Meslek mensubunun faaliyette bulunmayacağını yazıyla bildirmesi",
     "Çalışma bürosunun oda bölgesi dışına nakledilmiş olması",
     "Meslek mensubunun meslekten çıkarma cezasına çarptırılması",
     "Kanunun aradığı şartların sonradan kaybedilmiş olması"],
    "M. 35'e göre faaliyette bulunmama bildirimi veya büronun kapatılması, büronun oda bölgesi dışına nakli, meslekten "
    "çıkarma cezası, şartların sonradan kaybı ve ruhsat verilmemesini gerektiren sebebin sonradan tespiti silme "
    "sebebidir. Kınama cezası silme sebebi değildir.")

P.q("Çalışma Usul ve Esasları Yön. m. 35/2",
    f"{CU}, mesleki şirketlerin kayıtlarının çalışanlar listesinin şirketler bölümünden silinmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tasfiye üç yılda bitmezse veya şirket üç yıl gayri faal kalırsa kayıt silinir.",
    ["Tasfiyesine karar verilen şirketin tasfiyesi bir yılda tamamlanmazsa kayıt Birlik kararıyla silinir.",
     "Şirket beş yıl gayri faal kalırsa kaydı oda genel kurulunun kararıyla silinir.",
     "Üyelik yükümlülüklerini yerine getiren şirket de iki yıl iş almamışsa gayri faal sayılarak silinir.",
     "Şirketin kaydı, ortaklardan birinin çalışanlar listesinden silinmesiyle birlikte silinir."],
    "M. 35/2'ye göre tasfiyesine karar verilen şirketin tasfiyesi üç yılda tamamlanmazsa veya şirketin üç yıl gayri faal "
    "olduğu tespit edilirse kayıt yönetim kurulu kararıyla silinir; üyelik yükümlülüklerini yerine getiren şirket gayri "
    "faal sayılmaz.")

P.q("Çalışma Usul ve Esasları Yön. m. 36 (14.01.2026 değişikliği)",
    "Oda yönetim kurulu, bürosunu kapattığını tespit ettiği meslek mensubunu çalışanlar listesinden silmiştir. "
    f"{CU}, meslek mensubunun bu karara karşı başvuru yolu aşağıdakilerden hangisidir?",
    "Tebliğden itibaren on beş gün içinde Birliğe itiraz eder; Birlik on beş gün içinde nihai karar verir.",
    ["Tebliğden itibaren otuz gün içinde Birlik Disiplin Kuruluna itiraz eder; kurul bir ay içinde karar verir.",
     "Tebliğden itibaren on beş gün içinde oda disiplin kuruluna itiraz eder; kurulun kararı kesindir.",
     "Tebliğden itibaren altmış gün içinde doğrudan idare mahkemesinde dava açar; itiraz yolu yoktur.",
     "Tebliğden itibaren otuz gün içinde oda genel kuruluna itiraz eder; genel kurul ilk toplantıda karar verir."],
    "2026'da değişen m. 36'ya göre silme kararı gerekçeli olur; m. 35/1-a'daki tespit ve b bendi uyarınca verilen karara "
    "karşı meslek mensubu tebliğden itibaren on beş gün içinde Birliğe itiraz eder, Birlik on beş gün içinde nihai "
    "olarak karar verir.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 36",
    f"{CU}, çalışanlar listesinden silme kararının meslek mensubunun faaliyetine etkisi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Meslek mensubu karar kesinleşinceye kadar mesleğini yapar; ancak disiplin kurulu kamu yararı gerekirse geçici yasak koyabilir.",
    ["Silme kararı yönetim kurulunca verildiği anda meslek mensubu mesleki faaliyette bulunamaz.",
     "Meslek mensubu, karara itiraz ettiği sürece idari yargı kararı kesinleşinceye kadar faaliyetine devam eder ve kendisine geçici yasak konulamaz.",
     "Meslek mensubu karar tebliğ edilinceye kadar faaliyette bulunabilir; tebliğden sonra yeni iş kabul edemez.",
     "Meslek mensubunun faaliyetine devam edip etmeyeceğine Birlik Yönetim Kurulu karar verir."],
    "M. 36'ya göre meslek mensubu silme kararı kesinleşinceye kadar mesleğini yapma hakkına sahiptir; kesinleşmeden sonra "
    "faaliyette bulunamaz. Oda disiplin kurulu kamu yararı bakımından gerekli görürse geçici olarak faaliyette "
    "bulunmayı yasaklayabilir.")

P.sayisal("Çalışma Usul ve Esasları Yön. m. 40",
    f"{CU}, meslekten ayrılan veya yeminli mali müşavir sıfatını kaybedenler mühürlerini ayrılma veya tebligat tarihinden "
    "itibaren kaç gün içinde Birliğe iade etmek zorundadır?",
    "10", ["5", "15", "30", "60"],
    "M. 40'a göre meslekten ayrılan veya YMM sıfatını kaybedenler mühürlerini on gün içinde Birliğe iade eder. Vefat "
    "hâlinde bu yükümlülük mirasçılara geçer ve süre tebligattan itibaren bir aydır.")

P.q("Çalışma Usul ve Esasları Yön. m. 41",
    f"{CU}, yeminli mali müşavirlerin tasdikten doğan sorumluluğu aşağıdakilerden hangisinde doğru olarak verilmiştir?",
    "Tasdikin kapsamı ile sınırlı olarak ziyaa uğratılan vergi ve cezalardan mükellefle müştereken ve müteselsilen sorumludur.",
    ["Tasdikin kapsamına bakılmaksızın mükellefin bütün vergi borçlarından mükellefle müştereken ve müteselsilen sorumludur.",
     "Tasdikin kapsamı ile sınırlı olarak vergi aslından sorumludur; kesilen cezalar mükellefe aittir.",
     "Tasdikin kapsamı ile sınırlı olarak mükelleften tahsil edilemeyen kısım için ikinci derecede sorumludur.",
     "Tasdik doğru olmasa da mali sorumluluk mükellefe aittir; YMM hakkında disiplin hükümleri uygulanır."],
    "M. 41'e göre YMM'ler tasdikin doğruluğundan sorumludur; tasdik doğru değilse tasdikin kapsamı ile sınırlı olarak "
    "ziyaa uğratılan vergiler ve kesilecek cezalardan mükellefle birlikte müştereken ve müteselsilen sorumlu olurlar.")

P.q("Çalışma Usul ve Esasları Yön. m. 42",
    f"{CU}, aşağıdakilerden hangisi meslekle ve meslek onuru ile bağdaşmayan haller arasında sayılmamıştır?",
    "Tarifenin üzerinde ücret kararlaştırılması",
    ["Yanında çalıştırdığı kişilere karşı uygunsuz davranışlarda bulunmak",
     "Aşırı içki ve kumar düşkünlüğü ile tanınmak",
     "Mevzuat gereği bilgi vermesi gereken kuruluşa kasten yanıltıcı bilgi vermek",
     "Mesleki etik ve mesleki bağımsızlık kurallarını ihlal etmek"],
    "M. 42 meslekle bağdaşmayan halleri uygunsuz davranış, aşırı içki ve kumar düşkünlüğü, bilgi vermemek veya kasten "
    "yanıltıcı bilgi vermek, kanunen yasak işleri yapmak ve etik/bağımsızlık kurallarını ihlal olarak sayar. Tarifenin "
    "üzerinde ücret kararlaştırmak m. 46'ya göre mümkündür.")

P.q("Çalışma Usul ve Esasları Yön. m. 43 (14.01.2026 değişikliği)",
    f"{CU} Yasak Haller ve İstisnaları çerçevesinde sayılan Ticari Faaliyette Bulunamama kapsamında aşağıdaki ifadelerden hangisi yanlıştır?",
    "Limited şirketlerde müdür olarak görev alabilirler.",
    ["Ticari mümessillik, ticari vekillik ve acentelik yapamazlar.",
     "Adi ve kollektif şirketlerde ortak olamazlar.",
     "Komandit şirketlerde komandite ortak olamazlar.",
     "Anonim şirketlerde yönetim kurulu başkanı olamazlar."],
    "14.01.2026'da değişen m. 43'e göre meslek mensupları limited şirketlerde müdürlük, anonim şirketlerde yönetim kurulu "
    "üyeliği ve başkanlığı görevinde bulunamaz. Ticari mümessillik, vekillik, acentelik, adi ve kollektif şirket "
    "ortaklığı ile komandite ortaklık da yasaktır.")

P.q("Çalışma Usul ve Esasları Yön. m. 43/2 (14.01.2026 ek fıkra)",
    "SMMM (N), halka açık (Z) A.Ş.'de bağımsız yönetim kurulu üyesi olarak görev almıştır. "
    f"{CU}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Bu görev ticari faaliyet sayılmaz; ancak (N), (Z) A.Ş.'ye ve onun iştiraklerine mesleki hizmet veremez.",
    ["Bu görev ticari faaliyet sayılır; (N) ruhsatını odaya teslim ederek bu görevi üstlenebilir.",
     "Bu görev ticari faaliyet sayılmaz; (N) oda izniyle (Z) A.Ş.'nin defterlerini de tutabilir.",
     "Bu görev ticari faaliyet sayılmaz ve (N)'nin (Z) A.Ş.'ye hizmet vermesine engel oluşturmaz.",
     "Bu görev ticari faaliyet sayılır; ancak (N) şirketin denetim komitesinde görev almamak koşuluyla üstlenebilir."],
    "2026'da m. 43'e eklenen fıkraya göre anonim şirketlerde bağımsız yönetim kurulu üyeliği ticari faaliyet sayılmaz; "
    "ancak bu görevi alan meslek mensupları o şirkete ve doğrudan veya dolaylı hissedarı ya da iştiraki olduğu "
    "şirketlere Kanun m. 2 kapsamında hizmet veremez.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 44 (14.01.2026 değişikliği)",
    f"{CU}, hizmet akdiyle çalışma yasağına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hizmet akdiyle bağımsız denetim kuruluşlarının denetim ekiplerinde çalışmak bu yasak kapsamında değerlendirilir.",
    ["Çalışanlar listesine kayıtlı SMMM'ler unvanlarıyla Kanun m. 2'deki işler için hizmet akdiyle çalışamaz.",
     "Ortağı oldukları mesleki şirketlerde hizmet akdiyle yapılan çalışmalar bu yasak kapsamında değildir.",
     "Hizmet akdiyle çalışan meslek mensubu çalıştığı işletmeye Kanun m. 2 kapsamında hizmet veremez.",
     "Hizmet akdiyle çalışan meslek mensubu, çalıştığı işletmenin doğrudan veya dolaylı hissedarı ya da iştiraki olan işletmelere de hizmet veremez."],
    "2026'da değişen m. 44'e göre hizmet akdiyle olsa dahi ortağı olunan mesleki şirketlerde veya bağımsız denetim "
    "kuruluşlarının denetim ekiplerinde yapılan çalışmalar yasak kapsamında değerlendirilmez.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 45",
    f"{CU}, reklam yasağı kapsamında aşağıdakilerden hangisi meslek mensupları için reklam sayılır?",
    "Tanıtıcı broşürde evvelce veya hâlen iş yapılan müşterilerin açıklanması",
    ["Kartvizitte meslek unvanı, akademik unvan ve internet adresine yer verilmesi",
     "Unvan kullanılarak mesleki konularda devamlılık arz etmeyen gazete yazısı yazılması",
     "Ortaklık adına işin gerektirdiği ciddiyette eleman arama ilanı verilmesi",
     "Raporlarda iletişim numaraları ile açık adresin yazılması"],
    "M. 45'e göre iş tekliflerinde kullanılmak üzere tanıtıcı broşür bastırılabilir; ancak bu broşürlerde evvelce veya "
    "hâlen iş yapılan müşteriler açıklanamaz. Unvan ve iletişim bilgilerinin yazılması, devamlılık arz etmeyen "
    "yazı ve eleman ilanı reklam sayılmaz.")

P.q("Çalışma Usul ve Esasları Yön. m. 47",
    f"{CU}, aşağıdakilerden hangisi meslekle bağdaşan işler arasında sayılmamıştır?",
    "Kollektif şirkette ortak olmak",
    ["Limited şirkette ortak olmak",
     "Komandit şirkette komanditer ortak olmak",
     "Tasfiye memurluğu görevinde bulunmak",
     "Öğretim amacıyla ders vermek"],
    "M. 47'ye göre bilirkişilik, tasfiye memurluğu, limited ve anonim şirketlerde ortaklık, komandit şirkette komanditer "
    "ortaklık, ders vermek meslekle bağdaşan işlerdir. Kollektif şirkette ortaklık m. 43'e göre ticari faaliyet yasağı "
    "kapsamındadır.")

P.oncul("Çalışma Usul ve Esasları Yön. m. 43 ve 47",
    "Meslek mensuplarının üstlendiği aşağıdaki görevler verilmiştir:",
    ["Anonim şirkette ortak olmak",
     "Komandit şirkette komandite ortak olmak",
     "Kurumlar vergisinden muaf yapı kooperatifinde denetim kurulu üyeliği",
     "Ticari vekillik yapmak"],
    f"{CU}, yukarıdakilerden hangileri meslekle bağdaşan işlerdendir?",
    "I ve III",
    ["Yalnız I", "I ve III", "II ve III", "II ve IV", "I, III ve IV"],
    "M. 47'ye göre anonim şirkette ortaklık ile üyesi olunan ve kurumlar vergisinden muaf yapı kooperatifinin yönetim veya "
    "denetim kurulu üyeliği meslekle bağdaşır. Komandite ortaklık ve ticari vekillik m. 43'te yasak sayılmıştır.")

P.sayisal("Çalışma Usul ve Esasları Yön. m. 56",
    f"{CU}, denetim çalışma kâğıtları çalışma dosyası içinde yetkililerin isteği hâlinde ibraz edilmek üzere kaç yıl süre ile saklanmalıdır?",
    "10", ["3", "5", "7", "15"],
    "M. 56'ya göre çalışma kâğıtları çalışma dosyası içinde on yıl süreyle yetkililerin isteği hâlinde ibraz edilmek "
    "üzere saklanır. Bir yılı kapsayan denetimlerde denetimin en az her ay yapılması ve çalışma kâğıtlarının aylık "
    "faaliyeti göstermesi de zorunludur.")

P.q("Çalışma Usul ve Esasları Yön. m. 57 ve 59",
    "Denetim sırasında müşterisinin kayıtlarında mevzuata aykırı hileli bir işlem tespit eden meslek mensubu, "
    f"düzeltme önerisine rağmen işlemin düzeltilmediğini görmüştür. {CU}, meslek mensubunun bu durumda izleyeceği yol aşağıdakilerden hangisidir?",
    "Durumu olumsuz raporla ilgili mali mercilere aksettirir; suç oluşturan hâlleri yetkili mercilere duyurur.",
    ["Sır saklama yükümlülüğü nedeniyle durumu raporunda belirtmeden sözleşmeyi feshetmekle yetinir.",
     "Şartlı denetim raporu düzenler ve konuyu işletmenin yönetim kuruluna yazıyla bildirmekle yetinir.",
     "Durumu Birlik Haksız Rekabetle Mücadele Kuruluna bildirir ve raporu kurulun kararına göre düzenler.",
     "Olumlu rapor düzenler; hileli işlem hakkında ayrı bir yazıyla oda yönetim kurulunu bilgilendirir."],
    "M. 57'ye göre meslek mensubu hata ve hilelerin düzeltilmesini önerir; düzeltilmezse durum m. 59/c'deki olumsuz "
    "raporla ilgili mali mercilere aksettirilir; suç oluşturan hallerin yetkili mercilere duyurulması mecburidir.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 60",
    f"{CU}, denetim raporlarında “ilgili mevzuata uygundur” ibaresinin kullanılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu ibare ancak yeminli mali müşavirlerin tasdiki ihtiva eden raporlarında kullanılabilir.",
    ["Bu ibare serbest muhasebeci mali müşavirlerin tüm denetim raporlarında kullanılabilir.",
     "Bu ibare, olumlu rapor düzenlendiğinde raporu imzalayan meslek mensubunca unvan farkı gözetilmeden kullanılabilir.",
     "Bu ibare yeminli mali müşavirlerin tasdiki ihtiva etmeyen raporlarında da kullanılabilir.",
     "Bu ibare, ilgili mevzuat hükümleri raporda ayrıca sayılmışsa her iki unvan için de kullanılabilir."],
    "M. 60'a göre SMMM raporları ile YMM'lerin tasdiki ihtiva etmeyen raporlarında bu ibare kullanılmaz; ilgili mevzuat "
    "hükümleri açıkça yazılır. İbare ancak YMM'lerin tasdiki ihtiva eden raporlarında kullanılabilir.")

P.q("Çalışma Usul ve Esasları Yön. m. 61 (24.02.2025 ek fıkralar)",
    f"{CU}, hizmet akdiyle çalışan meslek mensuplarının unvan kullanımına ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Mesleğin konusuna giren alanlarda çalışanlar, çalıştıkları işyerinin unvanını belirterek mesleki unvanlarını kullanabilir.",
    ["Mesleğin konusuna giren alanlarda çalışanlar mesleki unvanlarını kullanabilir ve tasdik yetkilerini sürdürebilir.",
     "Mesleğin konusuna girmeyen alanlarda çalışanlar da işyerinin unvanını belirtmek koşuluyla mesleki unvanlarını kartvizitlerinde kullanabilir.",
     "Hizmet akdiyle çalışan meslek mensupları, meslek kütüğündeki kayıtları silindiği için unvan kullanamaz.",
     "Ticari faaliyette bulunan meslek mensupları, odaya bildirim yaparak mesleki unvanlarını kullanabilir."],
    "2025'te m. 61'e eklenen fıkralara göre mesleğin konusuna giren alanlarda hizmet akdiyle çalışanlar işyerinin unvanını "
    "belirterek mesleki unvanlarını kullanabilir, ancak tasdik yapamaz ve mesleki yetkilerini kullanamaz. Mesleğin "
    "konusuna girmeyen alanlarda çalışanlar veya ticari faaliyette bulunanlar unvan kullanamaz.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 62 (24.02.2025 değişikliği)",
    f"{CU}, ruhsat alan meslek mensuplarının ödevlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ölüm hâlinde mirasçılar kimlik, kaşe, mühür ve ruhsatları 30 gün içinde odaya iade eder.",
    ["Başka oda bölgesine naklolanlar nakilden sonraki 30 gün içinde ruhsatlarını değiştirir.",
     "Evlenme veya boşanmadan kaynaklanan soyadı değişikliğinde ruhsat değişimi için ayrıca ücret alınmaz.",
     "Meslekten çıkarılanlar kimlik, kaşe, mühür ve ruhsatlarını 30 gün içinde tutanakla odaya iade eder.",
     "Başvurmaları hâlinde vefat eden meslek mensubunun ruhsatının onaylı bir örneği mirasçılara verilir."],
    "2025'te değişen m. 62'ye göre ölüm hâlinde mirasçılar iade işlemlerini 4 ay içinde gerçekleştirir. Nakil ve isim "
    "değişikliğinde 30 günlük ruhsat değişimi, soyadı değişikliğinde ücret alınmaması ve meslekten çıkarılanların "
    "30 günlük iade yükümlülüğü aynı maddededir.",
    zorluk="hard")

P.q("Çalışma Usul ve Esasları Yön. m. 63/A (24.02.2025 ek madde)",
    f"{CU}, aşağıdakilerden hangisi meslek mensubunun ruhsatının Birlik Yönetim Kurulu kararıyla iptal edilmesini gerektiren haller arasında yer almaz?",
    "Üç yıl mesleki faaliyette bulunmamak",
    ["Meslekten ayrılma talebini içeren dilekçe ile başvurulması",
     "Meslek mensubunun ölümü",
     "Ruhsat verilmemesini gerektiren sebebin sonradan tespiti",
     "Kanunun aradığı şartların sonradan kaybedilmesi"],
    "2025'te eklenen m. 63/A'ya göre ruhsat; ayrılma talebi veya ölüm, ruhsat verilmemesini gerektiren sebebin sonradan "
    "tespiti ve Kanunun aradığı şartların sonradan kaybı hâllerinde Birlik Yönetim Kurulu kararıyla iptal edilir; bu "
    "kararlar kesindir. Faaliyette bulunmamak iptal sebebi değildir.")

# ================================================================ Haksız Rekabet ve Reklam Yasağı
P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 6",
    f"{HR}, aşağıdakilerden hangisi “meslek mensupları arasında ve iş sahipleriyle ilişkilerde haksız rekabet” başlığı altında özellikle haksız rekabet teşkil eden haller arasında sayılmamıştır?",
    "Asgari ücret tarifesinin altında ücret talep etmek veya ücretsiz hizmet vermek",
    ["Başka meslek mensubuyla sözleşmesi olan iş sahibini sözleşmeyi feshetmeye yöneltmek",
     "Faaliyeti geçici olarak durdurulduğu hâlde mesleki faaliyete doğrudan devam etmek",
     "Mesleği yapmaları yasaklananları çalıştırmak veya onlarla işbirliği yapmak",
     "Bağımlı çalışan meslek mensubu olarak aynı anda birden çok işletmede sorumluluk üstlenmek"],
    "Asgari ücret tarifesinin altında ücret talep etmek veya ücretsiz hizmet vermek m. 7/a'da “ücret ve diğer mali "
    "nitelikteki uygulamalar” başlığı altında sayılmıştır. Diğerleri m. 6/b, c, e ve h'de yer alır.",
    zorluk="hard")

P.sayisal("Haksız Rekabet ve Reklam Yasağı Yön. m. 6/i (24.02.2025 ek bent)",
    f"{HR}, devir teslim işleminin gerçekleşmediğinin odaya bildirilmesi durumu hariç, işin sonlanması hâlinde e-Birlik "
    "yazılımı üzerinden kaç gün içinde defter teslim tutanağı düzenlenmemesi haksız rekabet teşkil eder?",
    "30", ["7", "10", "15", "45"],
    "2025'te m. 6'ya eklenen (i) bendine göre işin sonlanması hâlinde e-Birlik yazılımı üzerinden 30 gün içinde defter "
    "teslim tutanağı düzenlenmemesi haksız rekabettir; devir teslimin gerçekleşmediğinin odaya bildirilmesi hâli hariçtir.")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 7",
    f"{HR}, aşağıdakilerden hangisi “ücret ve diğer mali nitelikteki uygulamalar ile haksız rekabet” örneği olarak sayılan haller arasında yer almaz?",
    "Bir diğer meslek mensubunun çalışanlarını iş sırlarını açıklamaya yöneltmek",
    ["Sözleşme değerinin altında serbest meslek makbuzu veya fatura düzenlemek",
     "Bir meslek mensubuna olan ücret borcunu ödememiş iş sahibine hizmet vermek",
     "İş sahiplerinden elde edilen bilgileri kullanarak ekonomik çıkar sağlamak",
     "Çalışanlara iş mevzuatında öngörülen ücret ve sosyal hakları vermemek"],
    "Diğer meslek mensubunun çalışanlarını iş sırlarını ele geçirmeye veya açıklamaya yöneltmek m. 6/ğ'de, meslek "
    "mensupları arası ilişkiler başlığı altındadır. Diğer seçenekler m. 7/d, c, g ve ğ'de sayılmıştır.")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 8",
    f"{HR}, aşağıdakilerden hangisi “reklam yoluyla haksız rekabete neden olacak eylem ve davranış” örneği olarak sayılan haller arasında yer almaz?",
    "Üçüncü kişilere menfaat vaat ederek iş almak",
    ["Meslek mensupları hakkında asılsız ihbar ve şikâyette bulunmak",
     "Sahip olmadığı meslek unvanını kullanmak",
     "Kendi hizmetleri hakkında yanıltıcı açıklama yapmak",
     "Mesleki ve akademik unvan dışında başka unvan kullanmak"],
    "Üçüncü kişilere ücret ya da menfaat sağlamak veya vaat ederek iş almak m. 7/e'de ücret ve mali uygulamalar başlığı "
    "altındadır. Asılsız ihbar (m. 8/c), sahip olunmayan unvan (m. 8/d), yanıltıcı açıklama (m. 8/ç) ve başka unvan "
    "kullanma (m. 8/f) reklam yoluyla haksız rekabettir.")

P.oncul("Haksız Rekabet ve Reklam Yasağı Yön. m. 13 ve 19",
    "Bir meslek mensubunun aşağıdaki davranışları değerlendirilmektedir:",
    ["Nesnel ve mesleğine ilişkin olmak koşuluyla işi ve şahsı hakkında açıklama yapmak",
     "Düzenlediği eğitim seminerini basın ve yayın yoluyla üçüncü kişilere duyurmak",
     "Mesleki konulardaki kitabında çalıştığı büronun unvanını kullanmak",
     "Aldığı bir sanat ödülünü kamuya duyurmak"],
    f"{HR}, yukarıdaki davranışlardan hangileri reklam yasağına aykırı değildir?",
    "I ve IV",
    ["Yalnız I", "I ve III", "I ve IV", "II ve III", "I, II ve IV"],
    "M. 13'e göre meslek mensubu nesnel ve mesleğine ilişkin açıklama yapabilir; mesleki alan dışındaki bir ödülünün "
    "duyurulması reklam sayılmaz. Seminerler basın ve yayın yoluyla duyurulamaz (m. 13/2); kitapta çalışılan büronun "
    "unvanı kullanılamaz (m. 19/1).",
    zorluk="hard")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 15",
    f"{HR}, başlıklı kâğıt, kartvizit ve diğer basılı evraka ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Oda ve Birlik organlarında geçmişte görev almış meslek mensupları bu unvanlarını kartvizitlerinde kullanabilir.",
    ["Basılı evrakta mesleki unvan, varsa akademik unvan, sicil ve ruhsat numarası yer alabilir.",
     "Ortaklık şeklinde çalışılıyorsa basılı evrakta ortaklığın unvanının yazılması zorunludur.",
     "Kamu kurumları ve siyasi partilerdeki geçmiş veya mevcut görevler basılı evrakta belirtilemez.",
     "Ortak sıfatı taşıyan meslek mensupları başlıklı kâğıt ve kartvizitlerde ortaklık adının yanında kendi ad ve soyadlarını da kullanır."],
    "M. 15/5'e göre oda ve Birlik organlarında geçmişte görev alanlar bu unvanlarını kullanamaz; hâlen görevli olanlar "
    "ancak görevin ifasıyla sınırlı olarak kullanabilir.")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 18 ve 21",
    f"{HR}, meslek mensuplarının tanıtım ve medya ilişkilerine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Sirkülerler, müşteri olmayanlara yazılı talepleri hâlinde verilebilir.",
    ["Büro açılışı, basın ve yayın yoluyla bir kez duyurulabilir.",
     "Tanıtım broşürlerinde mevcut müşterilerin unvanları, izinleri alınarak açıklanabilir.",
     "Eski müşterisi hakkında çıkan haberlere karşı meslek mensubu gazetede tekzip yayımlayabilir.",
     "Sirkülerler, müşterisi olmayan kişi ve kurumlara posta yoluyla talep aranmaksızın gönderilebilir."],
    "M. 18'e göre sirküler ve broşürler mevcut müşterilere ve meslek mensuplarına dağıtılabilir, müşterisi olmayanlara "
    "ancak yazılı talepleri hâlinde verilebilir; müşteri isimleri açıklanamaz. M. 21'e göre büro açılışları basın ve "
    "yayın yoluyla duyurulamaz, müşteriler hakkında tekzip yayımlanamaz.")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 22",
    f"{HR}, meslek mensuplarının internet sitelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İnternet sitesini arama motorlarına kaydederken hizmet verdiği sektörleri anahtar kelime olarak kullanabilir.",
    ["Mesleki faaliyet amacıyla meslekiunvanı.tr uzantılı internet sitesi kurulabilir.",
     "Sitede bağlı olunan oda, büro ve sicil numaraları ile mesleğe başlama tarihi yer alır.",
     "Sitenin geri planında, şifre-algoritma ile korunan ve ilgili kişinin erişebildiği kişiselleştirilmiş sanal ofis uygulamaları kullanılabilir.",
     "Kullanıcıları başka siteye yönlendiren, iş sağlama amaçlı kısa yollar kullanılamaz."],
    "M. 22/3-b'ye göre arama motoru kaydında ad, soyad, büro/ortaklık/şirket unvanı, şehir ve kayıtlı olunan oda dışında "
    "sözcük veya tanıtım amaçlı ibare kullanılamaz. Diğer ifadeler aynı maddede düzenlenmiştir.")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 25 ve 28 (24.02.2025 değişikliği)",
    f"{HR}, haksız rekabetle mücadele kurullarının oluşumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Oda kurulu en az üç yıl, Birlik kurulu en az beş yıl kıdemli meslek mensupları arasından görevlendirilir.",
    ["Oda kurulu en az beş yıl, Birlik kurulu en az on yıl kıdemli meslek mensupları arasından görevlendirilir.",
     "Oda kurulu en az iki yıl, Birlik kurulu en az üç yıl kıdemli meslek mensupları arasından seçilir.",
     "Oda kurulu oda genel kurulunca, Birlik kurulu ise Birlik genel kurulunca seçimle belirlenir.",
     "Oda kurulu en az beş, Birlik kurulu en az yedi üyeden oluşur ve üyeler üç yıl için seçilir."],
    "M. 25'e göre oda kurulu en az üç üyeden oluşur ve üyeler (2025 değişikliğiyle) en az üç yıl kıdemli meslek "
    "mensupları arasından oda yönetim kurulunca görevlendirilir; m. 28'e göre Birlik kurulu en az beş üyedir ve en az "
    "beş yıl kıdemli meslek mensupları arasından Birlik Yönetim Kurulunca görevlendirilir.",
    zorluk="hard")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 9, 10 ve 11",
    f"{HR}, haksız rekabete karşı hak ve sorumluluklara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Meslek mensubu, istihdam ettiği personelin gerçekleştirdiği haksız rekabet eylemlerinden sorumlu tutulamaz.",
    ["Odalar, haksız rekabetin men’i ve fiilin haksız olup olmadığının tespiti davalarını açmaya yetkilidir.",
     "Haksız rekabet nedeniyle zarar gören meslek mensubu ilgili odaya şikâyette bulunabilir ve/veya 6102 sayılı TTK'daki dava haklarını kullanabilir.",
     "Odalar, yanıltıcı beyanlarla yapılan haksız rekabette beyanların düzeltilmesi davasını açabilir.",
     "Yönetmeliğe aykırılık tespitinde odalarca resen veya şikâyet üzerine disiplin soruşturması başlatılır."],
    "M. 11'e göre meslek mensubu, istihdam ettiği personelin haksız rekabet eylemleri sebebiyle de odaya ve zarar "
    "görenlere karşı sorumludur. Odaların dava yetkisi m. 9'da, meslek mensubunun hakları m. 10'da, soruşturma m. 32'de "
    "düzenlenmiştir.")

P.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 16 ve 19",
    f"{HR}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Meslek mensuplarının kendi yazdıkları kitapları bastırıp satmaları yayıncılık faaliyeti sayılmaz.",
    ["SMMM ve YMM hizmeti, oda izni alınarak marka olarak tescil ettirilebilir.",
     "Meslek mensupları, mesleki şirketlerinin unvanını yayınevlerine kullandırabilir.",
     "Meslek mensupları, kitaplarında çalıştıkları büronun faaliyetlerini tanıtabilir.",
     "Meslek mensupları, mesleki yayın yapan bir yayınevi kurarak yayıncılık yapabilir."],
    "M. 19/2'ye göre meslek mensupları yayıncılık yapamaz; ancak tek başına veya başka meslek mensubuyla yazdıkları "
    "kitapları bastırıp satmaları yayıncılık sayılmaz. M. 16'ya göre SMMM ve YMM hizmeti hiçbir sıfat altında marka "
    "olarak tescil ettirilemez; şirket unvanı yayınevlerine kullandırılamaz.")

# ================================================================ Ücret Esasları
P.q("Ücret Esasları Yön. m. 13",
    f"{UY}, ücret sözleşmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yabancı firmalarla yapılan ücret sözleşmelerinin Türk Lirası cinsinden düzenlenmesi şarttır.",
    ["Ücret sözleşmesinin yazılı şekilde yapılması şarttır.",
     "Ücret sözleşmesinin belli bir meblağı kapsaması şarttır.",
     "Ücret sözleşmesine meslek mensubuna ortaklık payı verileceğine dair hüküm konulamaz.",
     "Ücret sözleşmesinin sözlü yapıldığı belirlenirse meslek mensubuna disiplin cezası uygulanır."],
    "M. 13'e göre yabancı firmalarla sözleşmeler yabancı dilde ve yabancı paralı yapılabilir; bu durumda en az ücret "
    "kontrolü sözleşme anındaki döviz kuruna göre yapılır. Yazılılık, belli meblağ, ortaklık payı yasağı ve sözlü "
    "sözleşmede disiplin cezası aynı maddededir.")

P.q("Ücret Esasları Yön. m. 14 ve 21",
    f"{UY}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Süreli ücret sözleşmelerinin en az bir yıllık olması şarttır ve ücretin peşin ödenmesi esastır.",
    ["Süreli ücret sözleşmeleri en az altı aylık yapılır ve ücret, aksine hüküm yoksa işin bitiminde toplu olarak ödenir.",
     "Süreli ücret sözleşmeleri en az üç yıllık yapılır ve ücret taksitle ödenemez.",
     "Süreli ücret sözleşmelerinde asgari süre aranmaz ve ücret aylık olarak ödenir.",
     "Süreli ücret sözleşmeleri en az iki yıllık yapılır ve ücret işin yarısında ödenir."],
    "M. 14'e göre ücret sözleşmeleri münferit veya süreli yapılabilir; süreli sözleşmelerin en az bir yıllık olması "
    "şarttır. M. 21'e göre ücretin peşin ödenmesi esastır; sözleşmeye iş yapıldıkça taksitle ödeme hükmü konulabilir.")

P.q("Ücret Esasları Yön. m. 17",
    f"{UY}, işin devri ve ücrete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sözleşme iş sahibince feshedilirse meslek mensubu, kusuru bulunsa dahi ücretin tamamını alır.",
    ["Üzerine aldığı işi haklı sebep olmadan bırakan meslek mensubu ücret talep edemez.",
     "Haklı sebep olmadan işi bırakan meslek mensubu peşin aldığı ücreti ve avansları geri verir.",
     "Peşin verilmesi gereken ücret ödenmezse meslek mensubu işe başlamak veya işi sürdürmekle yükümlü değildir.",
     "İş, meslek mensupları arasında devir ve teslim edilir ya da iş sahibine geri verilir."],
    "M. 17'ye göre sözleşmenin iş sahibince feshinde ücretin tamamı ödenir; ancak meslek mensubu bu duruma kendi kusur "
    "ve ihmaliyle yol açmışsa ücret ödenmez.")

P.q("Ücret Esasları Yön. m. 19",
    "İş sahibi (P) Ltd. Şti., sözleşme yaptığı SMMM (R)'nin faaliyetine zorunlu bir nedenle başka bir meslek mensubunu "
    f"da katmak istemektedir. {UY}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "(R)'nin oluru alınır; yazılı istemden itibaren bir hafta içinde muvafakat verilmezse sözleşme sona ermiş sayılır.",
    ["(R)'nin oluru aranmaz; (P), ücretin yeni meslek mensubuyla paylaşılmasını talep edebilir.",
     "(R)'nin oluru alınır; muvafakat bir ay içinde verilmezse oda yeni meslek mensubunu görevlendirir.",
     "(R)'nin oluru alınır ve sözleşmedeki ücret, yeni meslek mensubunun payı kadar azaltılır.",
     "(R)'nin oluru alınır; muvafakat verilmezse (P) sözleşmeyi ancak üç ay sonra feshedebilir."],
    "M. 19'a göre iş sahibi başka meslek mensubunu katmak isterse sözleşme yaptığı meslek mensubunun olurunu alır; "
    "ücretin azaltılmasını veya paylaşılmasını isteyemez. Muvafakat yazılı istemden itibaren bir hafta içinde verilmez "
    "veya cevapsız kalırsa sözleşme sona ermiş sayılır.")

P.q("Ücret Esasları Yön. m. 18",
    f"{UY}, meslek mensubunun işyeri merkezi dışındaki işleri o yerdeki başka meslek mensuplarına yaptırmasına ilişkin aşağıdakilerden hangisi yanlıştır?",
    "İş sahibinden, diğer meslek mensubunun payı kadar ek ücret talep edilebilir.",
    ["Ücretin paylaşılması tarifedeki esaslara göre yapılır.",
     "Tarifedeki esaslara aykırı sözleşmeyle diğer yerdeki meslek mensubunun ücreti azaltılamaz.",
     "Tarifedeki esaslara aykırı sözleşmeyle diğer meslek mensubunun ücreti artırılabilir.",
     "Meslek mensupları işin o kesiminden müşterek ve müteselsil sorumludur."],
    "M. 18'e göre bu durumda iş sahibinden sözleşmeyle belirlenmiş ücrete ek ödeme talep edilmez; paylaşım tarifedeki "
    "esaslara göre yapılır, diğer meslek mensubunun ücreti azaltılamaz fakat artırılabilir ve meslek mensupları o "
    "kesimden müştereken ve müteselsilen sorumludur.")

P.q("Ücret Esasları Yön. m. 9, 10 ve 11",
    f"{UY}, ücret tarifesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tarifelerde genel ilke olarak ücretler işin yüzdesi biçiminde belirlenir.",
    ["Tarifedeki ücretler eleman/saat esasına göre hizmet maliyeti ve bölgedeki ücret düzeyi gözetilerek belirlenir.",
     "Bir yıl sonra uygulanacak tarife en geç önceki yılın Aralık ayının 20'sine kadar Resmî Gazete'de ilan olunur.",
     "Kesinleşmiş tarifeler ilgili odalarca ilan tahtalarına asılarak da ilan olunur.",
     "Meslek mensupları ücretsiz işlem yapamaz; tarifedeki asgari miktarın altında çalışmak yasaktır."],
    "M. 9'a göre tarifelerde genel ilke olarak yüzde oranı biçiminde ücret belirlenemez; ancak hizmetin özelliğine göre "
    "ücret işin yüzdesi olarak belirlenebilir. İlan süresi m. 10'da, ücretsiz işlem ve asgari ücret yasağı m. 11'dedir.")

P.oncul("Ücret Esasları Yön. m. 20",
    "Meslek mensubu ücretine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Sözleşmede aksine hüküm yoksa, kararlaştırılan ücret yalnız sözleşmede belirtilen işlerin karşılığıdır.",
     "İş sahibine ait vergi, resim, harç ve giderler meslek mensubunun sorumluluğundadır.",
     "Bu giderler için meslek mensubunca istenirse avans verilmesi zorunludur.",
     "Meslek mensubunun işle ilgili seyahat giderleri iş sahibince ödenir."],
    f"{UY}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV",
    ["Yalnız I", "I ve II", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "M. 20'ye göre sözleşmede aksine hüküm yoksa ücret yalnız belirtilen işlerin karşılığıdır; iş sahibine ait vergi, "
    "resim, harç ve giderler iş sahibinin sorumluluğundadır, istenirse avans verilir ve seyahat giderleri iş sahibince "
    "ödenir.",
    zorluk="hard")

P.q("Ücret Esasları Yön. m. 23",
    f"{UY}, iş sahibinin adres değişikliğini meslek mensubuna bildirmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "En geç üç gün içinde taahhütlü mektupla bildirir; aksi hâlde sözleşmedeki adrese yapılan tebligat geçerlidir.",
    ["En geç on beş gün içinde elektronik posta ile bildirir; aksi hâlde tebligat odaya yapılır.",
     "En geç bir ay içinde noter aracılığıyla bildirir; aksi hâlde tebligat vergi dairesine yapılır.",
     "En geç yedi gün içinde odaya bildirir; oda yeni adresi meslek mensubuna iletir.",
     "Adres değişikliği sözleşmeyi sona erdireceğinden yeni sözleşme yapılması gerekir."],
    "M. 23'e göre iş sahibinin tebligat adresi sözleşmede belirttiği adrestir; adres değişiklikleri en geç üç gün içinde "
    "iş sahibi tarafından taahhütlü mektupla meslek mensubuna bildirilmelidir.")

P.q("3568 s. Kanun m. 46; Ücret Esasları Yön. m. 5-7",
    f"3568 sayılı Kanun ve {UY.replace('’e göre', '')} ücret tarifesinin hazırlanıp yürürlüğe girmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Oda yönetim kurullarının önerileri dikkate alınarak Birlikçe hazırlanan tarife Bakanlıkça tasdik edilip Resmî Gazete'de yayımlanır.",
    ["Her oda kendi tarifesini hazırlar ve oda genel kurulunda kabul edildiği tarihte yürürlüğe girer.",
     "Tarife Birlik Genel Kurulunca kabul edilir ve Bakanlık onayı aranmaksızın Birliğin internet sitesinde yayımlandığı tarihte yürürlüğe girer.",
     "Tarife Hazine ve Maliye Bakanlığınca doğrudan hazırlanır ve odaların görüşü alınmadan yayımlanır.",
     "Yeni tarife tasdik edilmezse eski tarife uygulanamaz ve ücret taraflarca belirlenir."],
    "Kanun m. 46'ya göre oda yönetim kurulları tarife hazırlayıp Birliğe gönderir; Birlik yönetim kurulu grupları ve "
    "tarifeleri hazırlayarak Bakanlığa gönderir; Bakanlık aynen veya değiştirerek tasdik eder ve tarifeler Resmî "
    "Gazete'de yayımlanarak yürürlüğe girer. Yeni tarife tasdik edilinceye kadar mevcut tarife uygulanır.",
    zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
