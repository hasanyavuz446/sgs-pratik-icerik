#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Hukuk — Ticari Defterler konu havuzu (3×20).

Dayanak: 17.07.2026 tarihinde mevzuat.gov.tr'den alınan güncel 6102 sayılı
TTK m.64–88. Değişmiş eski süreler kullanılmamış; zıya belgesi süresi güncel
metindeki otuz gün olarak ele alınmıştır.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors, "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref, "difficulty": difficulty,
    }


RULES = [
    r(
        "Bir tacirin defterlerinden işletmenin faaliyetlerinin oluşumu ve mali durumunun uzmanlarca makul sürede anlaşılması mümkün değildir. Defter tutma amacına göre hangisi doğrudur?",
        "Ticari defterlerin üçüncü kişi uzmanlar bakımından taşıması gereken temel nitelik aşağıdakilerden hangisidir?",
        "Defterler işletmenin faaliyet ve finansal durumu hakkında makul sürede fikir vermelidir",
        ["Defterler yalnız tacirin anlayacağı özel işaretlerle ve mutlaka açıklamasız tutulmalıdır", "Defterler sadece vergi borcunu gösterip ticari işlemleri dışarıda bırakmalıdır", "Defterlerin işletme faaliyetlerinin gelişimini izlenemez kılması yeterlidir", "Defterler yalnız kapanış günündeki nakit miktarını göstermekle sınırlıdır"],
        "TTK m.64/1, defterlerin üçüncü kişi uzmanlara makul sürede işletmenin faaliyetleri ve finansal durumu hakkında fikir verecek ve faaliyet gelişimini izletecek şekilde tutulmasını ister.",
        "Defter tutma yalnız rakamları depolama işi değildir. Bağımsız bir uzmanın işletmenin iktisadi ve mali görünümünü makul sürede kavrayabilmesi gerekir.",
        "6102 sayılı TTK m.64/1", "medium",
    ),
    r(
        "Tacir, işletmesiyle ilgili olarak gönderdiği belgelerin hiçbir kopyasını saklamadığını, asılların muhataplarda bulunduğunu ileri sürmektedir. TTK m.64/2 bakımından hangisi doğrudur?",
        "Tacirin işletmesiyle ilgili gönderilen belgeler bakımından saklama yükümlülüğünün kapsamı nedir?",
        "Gönderilen işletme belgelerinin yazılı, görsel veya elektronik bir kopyası saklanmalıdır",
        ["Gönderilen belgenin kopyası hiçbir ortamda saklanamaz ve kesinlikle derhâl yok edilmelidir", "Yalnız muhatap yabancıysa belgenin aslının noterde bırakılması gerekir", "Sadece ödeme yapılmamış belgelerin sözlü bir listesi tutulmalıdır", "Belge gönderildiğinde bütün saklama yükümlülüğü kesin olarak muhataba geçer"],
        "TTK m.64/2 taciri, işletmesiyle ilgili gönderilmiş her türlü belgenin fotokopi, bilgisayar kaydı veya benzeri kopyasını yazılı, görsel ya da elektronik ortamda saklamakla yükümlü tutar.",
        "Belgenin aslının muhataba gitmesi tacirin iz bırakma ödevini kaldırmaz. Kanun gönderilen belgenin uygun bir kopyasının işletmede korunmasını öngörür.",
        "6102 sayılı TTK m.64/2", "easy",
    ),
    r(
        "Bir anonim şirket, pay defteri ile genel kurul toplantı ve müzakere defterinin muhasebe kaydı içermediği için ticari defter sayılamayacağını savunmaktadır. Hangisi doğrudur?",
        "Muhasebeyle doğrudan ilgili olmayan şirket defterlerinin ticari defter niteliği bakımından doğru ifade hangisidir?",
        "Pay ve genel kurul toplantı defterleri de Kanun gereği ticari defter sayılır",
        ["Muhasebe kaydı içermeyen hiçbir şirket defteri kesinlikle ticari defter sayılamaz", "Pay defteri yalnız vergi incelemesinde geçici olarak ticari defter sayılır", "Genel kurul defteri ancak şirket tasfiye edilirse ticari deftere dönüşür", "Yönetim kurulu kararları yalnız noter arşivinde tutulursa defter sayılır"],
        "TTK m.64/4, pay defteri, yönetim kurulu karar defteri ve genel kurul toplantı ve müzakere defteri gibi muhasebeyle ilgili olmayan defterleri de ticari defter kabul eder.",
        "Ticari defter kavramı yalnız muhasebe kayıtlarıyla sınırlı değildir. Şirket iradesi ve pay sahipliği düzenini izleyen defterler de bu statüdedir.",
        "6102 sayılı TTK m.64/4", "easy",
    ),
    r(
        "Tacir, fiziki yevmiye, defteri kebir ve envanter defterlerini kullanmaya başlamış; ancak açılış onayı yaptırmamıştır. Açılış onayının zamanı ve mercii bakımından hangisi doğrudur?",
        "Fiziki yevmiye, defteri kebir ve envanter defterlerinin açılış onayı kural olarak ne zaman ve kim tarafından yapılır?",
        "Defterler kullanılmadan önce açılış onayı kural olarak noter tarafından yapılır",
        ["Açılış onayı defterler tamamen dolduktan sonra vergi dairesince yapılır ve yeterlidir", "Açılış onayı yalnız mahkeme kararıyla ve tasfiye aşamasında yapılabilir", "Fiziki defterlerde hiçbir açılış onayı aranmaz ve sonradan da yapılamaz", "Onay ilk kâr dağıtımından sonra meslek odası tarafından yapılır"],
        "TTK m.64/3 fiziki yevmiye, defteri kebir ve envanter defterinin açılış onayını kuruluşta ve kullanılmaya başlamadan önce kural olarak notere bırakır.",
        "Açılış onayı defter kullanılmaya başlamadan önce tamamlanır. Anonim ve limited şirketin tescili sırasındaki sicil müdürlüğü onayı gibi özel düzenlemeler saklıdır.",
        "6102 sayılı TTK m.64/3", "medium",
    ),
    r(
        "Ticari defterler elektronik ortamda tutulmaktadır. Tacir, elektronik yevmiye defterinin açılışı ve kapanışı için ayrıca noter onayı gerektiğini düşünmektedir. Hangisi doğrudur?",
        "Elektronik ticari defterlerin açılışı ile elektronik yevmiye ve yönetim kurulu karar defterlerinin kapanışında onay kuralı nasıldır?",
        "Elektronik defterlerde belirtilen açılış ve kapanışlar için noter veya sicil onayı aranmaz",
        ["Elektronik defterlerin her sayfası aylık olarak her zaman hem noter hem mahkemece onaylanır", "Elektronik yevmiye defteri yalnız kâğıda basılırsa hukuken varlık kazanır", "Elektronik defterde açılış onayı aranmaz fakat her gün sicil onayı gerekir", "Elektronik kayıtlar yalnız vergi dairesinin fiziki mührüyle geçerli olabilir"],
        "TTK m.64/3, elektronik tutulan ticari defterlerin açılışlarında ve elektronik yevmiye ile yönetim kurulu karar defterlerinin kapanışlarında noter veya sicil müdürlüğü onayı aramaz.",
        "Elektronik defter rejimi fiziki defterin onay modelini aynen tekrar etmez. Usul ve esaslar ilgili tebliğlerle belirlenir; maddede sayılan noter ve sicil onayı kaldırılmıştır.",
        "6102 sayılı TTK m.64/3", "medium",
    ),
    r(
        "Tacir defterlerini yabancı dilde tutmuş ve kullandığı kısaltmaların anlamlarını hiçbir yerde açıklamamıştır. TTK m.65/1 bakımından hangisi doğrudur?",
        "Ticari defterlerde kullanılacak dil ile kısaltma, harf ve sembollerin kullanımına ilişkin kural hangisidir?",
        "Kayıtlar Türkçe tutulmalı; kullanılan kısaltma ve sembollerin anlamı açıklanmalıdır",
        ["Kayıt dili tamamen serbesttir ve sembollerin anlamı hiçbir zaman açıklanamaz", "Defterler yalnız Latince tutulur ve rakam kullanılmasına izin verilmez", "Türkçe kayıt sadece tacir gerçek kişiyse aranır, şirketlerde aranmaz", "Kısaltmalar her durumda sadece mahkemenin önceden izin verdiği uyuşmazlıklarda kullanılabilir"],
        "TTK m.65/1 defter ve gerekli kayıtların Türkçe tutulmasını; kullanılan kısaltma, rakam, harf ve sembollerin anlamlarının açıkça belirtilmesini emreder.",
        "Okunabilirlik için ortak dil ve açıklık gerekir. Teknik işaret kullanılabilir; ancak ne anlama geldiklerinin defter veya kayıt düzeninde belirlenebilir olması şarttır.",
        "6102 sayılı TTK m.65/1", "easy",
    ),
    r(
        "İşletmenin kayıtları aylar sonra topluca, bazı işlemler atlanarak ve tarih sırası bozulmuş biçimde yapılmıştır. Defterlerin tutulma ilkeleri bakımından hangisi doğrudur?",
        "Ticari defterlere yapılacak yazım ve kayıtların taşıması gereken dört temel nitelik hangisidir?",
        "Yazım ve kayıtlar eksiksiz, doğru, zamanında ve düzenli yapılmalıdır",
        ["Kayıtlar seçmeli, yaklaşık, gecikmeli ve rastgele sırayla yapılmalıdır", "Yalnız gelir doğuran işlemler doğru, borçlar ise topluca yazılmalıdır", "Kayıtların zamanı ve doğruluğu tamamen tacirin isteğine bırakılmıştır", "Deftere yalnız nakit işlemler yazılır ve diğer işlemler saklanmaz"],
        "TTK m.65/2, yazım ve diğer gerekli kayıtların eksiksiz, doğru, zamanında ve düzenli yapılmasını zorunlu tutar. Olaydaki toplu ve eksik kayıt bu ölçülere uymaz.",
        "Dört nitelik birlikte aranır: tamlık, doğruluk, zamanlılık ve düzen. Bir kaydın sonradan yapılması diğer niteliklerin bulunmasıyla tek başına telafi edilemez.",
        "6102 sayılı TTK m.65/2", "easy",
    ),
    r(
        "Yanlış kayıt düzeltilirken önceki içerik tamamen silinmiş ve değişikliğin ne zaman yapıldığı anlaşılamaz hâle gelmiştir. TTK m.65/3 bakımından hangisi doğrudur?",
        "Ticari defterde yanlış bir kaydın düzeltilmesinde korunması gereken özellik aşağıdakilerden hangisidir?",
        "Düzeltme önceki içeriği ve değişikliğin zamanını belirlenebilir bırakmalıdır",
        ["Yanlış kayıt iz bırakmadan silinmeli ve önceki içerik tamamen yok edilmelidir", "Düzeltmenin zamanı yalnız tacirin belleğine bırakılmalı ve kayda alınmamalıdır", "Eski kayıt okunamaz kılındığında düzeltme kendiliğinden geçerli hâle gelir", "Her yanlışlık için defterin tamamı imha edilip yeni defter açılmalıdır"],
        "TTK m.65/3 önceki içeriği belirlenemez kılan çizme ve değiştirmeyi, ayrıca kaydın ilk anda mı sonra mı değiştirildiği anlaşılmayan düzeltmeleri yasaklar.",
        "Düzeltilebilirlik, kayıt izinin yok edilmesi anlamına gelmez. Denetim izi korunmalı; eski içerik ile düzeltmenin sonradan yapıldığı anlaşılabilmelidir.",
        "6102 sayılı TTK m.65/3", "medium",
    ),
    r(
        "Elektronik defter kayıtlarına saklama süresi içinde erişilememekte ve veriler okunur hâle getirilememektedir. Elektronik kayıtların şartı bakımından hangisi doğrudur?",
        "Ticari defter ve kayıtlar elektronik tutulduğunda saklama süresi boyunca hangi teknik sonuç sağlanmalıdır?",
        "Bilgilere erişilebilmeli ve kayıtlar her zaman kolaylıkla okunabilir olmalıdır",
        ["Veriler saklama süresince şifrelenip tacir dâhil herkes için erişilemez kalmalıdır", "Elektronik kayıt yalnız ilk oluşturulduğu gün okunabilir olmak zorundadır", "Kayıtlar erişilemese de sunucunun fiziksel olarak varlığı tek başına yeterlidir", "Elektronik verinin okunabilmesi yalnız tasfiye tarihinden sonra aranır"],
        "TTK m.65/4, elektronik kayıt bilgilerinin saklama süresince ulaşılabilir ve her zaman kolaylıkla okunabilir olmasını şart koşar.",
        "Elektronik ortam, saklama ve ibraz işlevini zayıflatamaz. Verinin yalnız var olması değil, süre boyunca erişilip anlaşılabilir biçimde görüntülenebilmesi gerekir.",
        "6102 sayılı TTK m.65/4", "medium",
    ),
    r(
        "Tacir işletmesini açmış fakat taşınmazlarını, alacaklarını, borçlarını ve nakdini gösteren bir liste düzenlememiştir. Açılış envanteri bakımından hangisi doğrudur?",
        "Ticari işletmenin açılışında düzenlenen envanterin temel kapsamı aşağıdakilerden hangisidir?",
        "Varlıklar ve borçlar eksiksiz gösterilmeli, değerleri ayrı ayrı belirtilmelidir",
        ["Envanter yalnız kasadaki parayı gösterir, borç ve diğer varlıkları kapsamaz", "Envantere de yalnız tacirin kişisel eşyaları yazılır, işletme varlıkları dışlanır", "Açılışta envanter düzenlenmez; ilk tasfiye gününe kadar beklenir", "Envanterde değer gösterilmesi yasaktır ve yalnız eşya adları yazılır"],
        "TTK m.66/1 açılışta taşınmaz, alacak, borç, nakit ve diğer varlıkları eksiksiz ve doğru gösteren; varlık ve borç değerlerini tek tek belirten envanter ister.",
        "Envanter işletmenin açılış mali fotoğrafıdır. Sadece varlık listesi değil, borçları ve her kalemin değerini de içeren eksiksiz bir tespit yapılmalıdır.",
        "6102 sayılı TTK m.66/1", "easy",
    ),
    r(
        "Tacir, hesap yılını on sekiz ay olarak belirlemiş ve bu sürenin sonunda envanter çıkarmayı planlamıştır. Faaliyet dönemi ve envanter zamanı bakımından hangisi doğrudur?",
        "Açılıştan sonraki envanter sıklığı ve hesap yılının azami uzunluğu bakımından kural hangisidir?",
        "Her faaliyet dönemi sonunda envanter çıkarılır ve hesap yılı on iki ayı geçemez",
        ["Envanter yalnız işletme kapanırken çıkarılır ve hesap yılı sınırsız olabilir", "Hesap yılı en az yirmi dört ay olmalı ve ara envanter yasaktır", "Envanter yalnız vergi incelemesi başlatılırsa ve beş yılda bir çıkarılır", "Faaliyet dönemi süresi de ortakların sözlü kararıyla her zaman sınırsız uzatılır"],
        "TTK m.66/2 açılıştan sonra her faaliyet dönemi sonunda envanter düzenlenmesini ve faaliyet dönemi ya da hesap yılının on iki ayı geçmemesini öngörür.",
        "Envanter dönem sonu yükümlülüğüdür. Tacir hesap yılını on sekiz aya uzatarak yıllık tespit zorunluluğunu bertaraf edemez.",
        "6102 sayılı TTK m.66/2", "medium",
    ),
    r(
        "İşletmede düzenli yenilenen ve toplam değeri ikinci derecede önemli malzeme, küçük değişikliklerle sabit değer üzerinden envantere alınmaktadır. Fiziksel sayım aralığı bakımından hangisi doğrudur?",
        "TTK m.66/3'teki koşulları taşıyan, değişmeyen miktar ve değerle izlenen varlıklarda fiziksel sayım kural olarak ne sıklıkta yapılır?",
        "Bu yöntem kullanılsa da kural olarak üç yılda bir fiziksel sayım yapılır",
        ["Bu varlıklar için hiçbir zaman fiziksel sayım yapılmasına izin verilmez", "Fiziksel sayım yalnız elli yılda bir ve tasfiye memurunca yapılır", "Sabit değer yöntemi kullanıldığında her gün tam sayım yapılması zorunludur", "Sayım aralığı kanunen yalnız on iki yılda bir olarak belirlenmiştir"],
        "TTK m.66/3 belirli koşullardaki varlıkların değişmeyen miktar ve değerle envantere alınmasına izin verir; buna rağmen kural olarak üç yılda bir fiziksel sayım gerekir.",
        "Kolaylaştırma kalıcı sayım muafiyeti yaratmaz. Miktar, değer ve bileşimdeki küçük değişiklik varsayımı üç yıllık fiziksel sayımla sınanır.",
        "6102 sayılı TTK m.66/3", "medium",
    ),
    r(
        "İşletme, genel kabul gören matematiksel-istatistiksel yöntemle örnekleme yaparak envanter miktarını belirlemiştir. Sonucun fiziksel sayıma eş düşmesi şartıyla hangisi doğrudur?",
        "Sondaj yöntemine dayanan envanterin kullanılabilmesi için sonuç bakımından aranan ölçüt nedir?",
        "Sonuç fiziksel sayım yapılsaydı elde edilecek envanter sonucuna eş düşmelidir",
        ["Sonucun fiziksel sayımdan mümkün olduğunca farklı olması zorunludur", "Yöntem hiçbir matematiksel veya istatistiksel dayanak içermemelidir", "Sondaj yöntemi yalnız borçları envanterden çıkarmak için kullanılabilir", "Sonucun doğruluğu değil tek başına yalnızca işlemin ucuz olması yeterli kabul edilir"],
        "TTK m.67/1 genel kabul gören matematiksel-istatistiksel sondaj yöntemine izin verir; yöntem TMS'ye uygun ve sonucu fiziksel sayım sonucuna eş değer olmalıdır.",
        "Örnekleme tam sayımın keyfî alternatifi değildir. Güvenilirlik ölçütü, fiziksel sayım yapılsaydı ortaya çıkacak çeşit, miktar ve değer sonucuna eş düşmesidir.",
        "6102 sayılı TTK m.67/1", "hard",
    ),
    r(
        "Tacir faaliyet dönemini kapatmış, yalnız bilanço düzenlemiş fakat gelir tablosu hazırlamamıştır. Yılsonu finansal tablolarının bileşimi bakımından hangisi doğrudur?",
        "TTK m.68'e göre yılsonu finansal tablolarını oluşturan iki temel tablo hangisidir?",
        "Yılsonu finansal tabloları bilanço ile gelir tablosundan oluşur",
        ["Yılsonu tabloları yalnız kasa sayım tutanağı ile faturadan oluşur", "Yılsonu tabloları sadece pay defteri ile yönetim kurulu karar defteridir", "Yılsonu tabloları yalnız ticaret sicili ilanı ve vergi levhasıdır", "Yılsonu tabloları sadece banka ekstresi ile stok listesinden oluşur"],
        "TTK m.68/2-3 tacire gelir tablosu hazırlama yükümü getirir ve bilanço ile gelir tablosunu yılsonu finansal tabloları olarak tanımlar.",
        "Bilanço finansal durumun, gelir tablosu dönem performansının temel görünümünü verir. İkisinden yalnız birini hazırlamak Kanundaki bileşimi tamamlamaz.",
        "6102 sayılı TTK m.68/2-3", "easy",
    ),
    r(
        "Yılsonu finansal tabloları anlaşılmaz biçimde, Türkiye Muhasebe Standartları gözetilmeden ve olağan işletme akışını aşan gecikmeyle çıkarılmıştır. Hangisi doğrudur?",
        "Yılsonu finansal tablolarının düzenlenmesine ilişkin TTK m.69 ilkeleri hangileridir?",
        "Tablolar TMS'ye uygun, açık, anlaşılır ve gerekli süre içinde düzenlenmelidir",
        ["Tablolar yalnız ortakların anlayacağı biçimde ve sınırsız gecikmeyle düzenlenebilir", "Tabloların açık olması yasaktır; yalnız vergi idaresi okuyabilmelidir", "TMS yalnız yabancı şirketlere uygulanır ve yerli taciri hiçbir şekilde bağlamaz", "Düzenleme zamanı ve anlaşılabilirlik tamamen tacirin gizli tercihine bırakılmıştır"],
        "TTK m.69 yılsonu finansal tablolarının TMS'ye uyularak, açık ve anlaşılır biçimde ve düzenli işletme akışının gerekli kıldığı sürede çıkarılmasını ister.",
        "Standartlara uygunluk, açıklık-anlaşılabilirlik ve zamanlılık birlikte aranır. Birinin bulunması diğer eksiklikleri gidermez.",
        "6102 sayılı TTK m.69", "medium",
    ),
    r(
        "Tacir yılsonu finansal tablolarını yalnız yabancı dil ve yabancı para birimiyle düzenlemiştir; olayda özel bir kanuni istisna yoktur. Hangisi doğrudur?",
        "Yılsonu finansal tablolarında kural olarak kullanılacak dil ve para birimi hangisidir?",
        "Tablolar kural olarak Türkçe ve Türk Lirası ile düzenlenmelidir",
        ["Tablolar yalnız İngilizce ve avro ile düzenlenebilir", "Dil ile para birimi her işlem için mahkemece ayrı belirlenir", "Tablolar hiçbir yazı ve para birimi kullanılmadan hazırlanmalıdır", "Yalnız ortakların seçtiği yabancı dil ve kripto varlık birimi kullanılabilir"],
        "TTK m.70, diğer kanunlardaki istisnaları saklı tutarak yılsonu finansal tablolarının Türkçe ve Türk Lirası ile düzenlenmesini öngörür.",
        "Genel kural hem dil hem para birimi bakımından yerlilik öngörür. Başka kanundaki açık istisna bulunmadıkça yabancı dil ve para tek başına yeterli değildir.",
        "6102 sayılı TTK m.70", "easy",
    ),
    r(
        "Finansal tablolar hazırlanmış ancak tacir tarafından tarihlenip imzalanmamıştır. TTK m.71 bakımından tamamlanması gereken işlem hangisidir?",
        "Finansal tabloların tacir tarafından onaylanma biçimi aşağıdakilerden hangisidir?",
        "Finansal tablolar tacir tarafından tarih atılarak imzalanmalıdır",
        ["Tablolar yalnız sözlü olarak kabul edilmeli ve imzasız bırakılmalıdır", "Tablolar ancak bütün müşterilerce imzalanırsa geçerli olabilir", "İmza yerine açıklamasız boş bir sayfa eklenmesi yeterlidir", "Tarih ve imza yalnız şirket tasfiyeye girerse kullanılabilir"],
        "TTK m.71 finansal tabloların tacir tarafından tarih atılarak imzalanmasını emreder. Hazırlanmış ancak tarihsiz ve imzasız tablolar bu şekli tamamlamaz.",
        "İmza ve tarih, tablonun tacirce benimsenmesini ve hangi anda tamamlandığını gösterir. Bu görev müşteri veya sicil müdürüne aktarılamaz.",
        "6102 sayılı TTK m.71", "easy",
    ),
    r(
        "İşletme, bilançoda aktif ve pasif kalemleri karşılıklı mahsup ederek bazı varlık ve borçları göstermemiştir. Mahsup yasağı bakımından hangisi doğrudur?",
        "Finansal tablolarda kalemlerin birbirinden ayrı gösterilmesine ilişkin temel kural hangisidir?",
        "Aktif pasifle, gider gelirle ve taşınmaz hakkı ilgili yükle mahsup edilemez",
        ["Bütün aktif ve pasif kalemler tek tutarda birleştirilerek ayrıntısız gösterilmelidir", "Gelir ve giderler her durumda birbirinden düşülüp yalnız net sonuç yazılmalıdır", "Taşınmaz hakları ilgili yüklerle zorunlu olarak mahsup edilip gizlenmelidir", "Mahsup yasağı yalnız tacirin zarar ettiği dönemlerde uygulanabilir"],
        "TTK m.72/2 aktif-pasif, gider-gelir ve taşınmaz haklarıyla ilgili yüklerin mahsup edilemeyeceğini düzenler; kanuni ve standart istisnaları saklıdır.",
        "Mahsup yasağı finansal görünümün brüt unsurlarını korur. Birbirinden farklı nitelikteki kalemlerin netleştirilmesi varlık, borç, gelir ve gider bilgisini örter.",
        "6102 sayılı TTK m.72/2", "medium",
    ),
    r(
        "Bilanço yalnız toplam varlık ve toplam borç rakamını göstermekte; duran-dönen ayrımı ile özkaynak ve dönem ayırıcı hesaplar ayrı sunulmamaktadır. Hangisi doğrudur?",
        "Türkiye Muhasebe Standartlarında aksi yoksa bilançoda ayrı kalemler olarak gösterilecek ana gruplar hangileridir?",
        "Duran-dönen varlıklar, özkaynak, borçlar ve dönem ayırıcı hesaplar ayrı gösterilir",
        ["Yalnız nakit ile ortakların kişisel malları ayrı gösterilir ve diğer tüm ayrıntılar gizlenir", "Sadece satış faturaları ve banka hesapları bilançoya alınır", "Bütün kalemler ayrım yapılmadan tek bir net tutarda gösterilir", "Yalnız vergi borcu ile personel sayısı bilanço kalemi sayılır"],
        "TTK m.73/1, TMS'de aksi öngörülmedikçe duran ve dönen varlıkları, özkaynakları, borçları ve dönem ayırıcı hesapları ayrı ve yeterli ayrıntıyla göstermeyi ister.",
        "Bilanço şeması yalnız toplam büyüklüklerden oluşmaz. Likidite, finansman ve dönem ayrımını açıklayan ana gruplar birbirinden ayrılarak sunulur.",
        "6102 sayılı TTK m.73/1", "medium",
    ),
    r(
        "Bilanço gününe kadar doğmuş muhtemel zarar sonradan öğrenilmiş; işletme bunu dikkate almamış, henüz gerçekleşmemiş kazancı ise kaydetmiştir. İhtiyat ilkesi bakımından hangisi doğrudur?",
        "TTK m.78'deki ihtiyatlı değerleme ilkesi risk, zarar ve kazançların dikkate alınmasını nasıl düzenler?",
        "Doğmuş muhtemel risk ve zararlar dikkate alınır; kazanç gerçekleşmişse hesaba katılır",
        ["Muhtemel zararlar daima gizlenir, gerçekleşmemiş kazançların tamamı kaydedilir", "Risk ve kazançlar da yalnız nakden ödendiğinde veya tahsil edildiğinde değerlendirilir", "Bilanço gününden sonra öğrenilen hiçbir olay geçmiş dönemle ilişkilendirilemez", "İhtiyat ilkesi yalnız ortakların kişisel vergi beyannamesinde uygulanır"],
        "TTK m.78/1-d ihtiyatlı değerleme gereği bilanço gününe kadar doğan muhtemel risk ve zararların, sonradan öğrenilse bile dikkate alınmasını; kazancın gerçekleşmişse hesaba katılmasını öngörür.",
        "İhtiyat, zarar ihtimalini görmezden gelmek veya gerçekleşmemiş kârı öne çekmek değildir. Risk ve zararda doğum, kazançta gerçekleşme esas alınır.",
        "6102 sayılı TTK m.78/1-d", "hard",
    ),
    r(
        "Bir gider dönem içinde doğmuş fakat ödeme sonraki yıl yapılacaktır. Tacir gideri ödeme tarihine göre sonraki döneme bırakmak istemektedir. Dönemsellik bakımından hangisi doğrudur?",
        "Faaliyet yılının gelir ve giderlerinin finansal tablolara alınmasında ödeme ve tahsilat tarihinin rolü nedir?",
        "Gelir ve giderler ödeme ve tahsilat tarihinden bağımsız olarak ilgili döneme alınır",
        ["Gelir ve giderler kesinlikle yalnız nakit hareketi gerçekleşen dönemde kaydedilebilir", "Ödenmemiş giderler hiçbir dönemin finansal tablosunda yer alamaz", "Tahsil edilmemiş gelirler daima işletme sahibinin kişisel hesabına yazılır", "Dönemsellik yalnız şirketin tasfiyeye girdiği yıl uygulanır"],
        "TTK m.78/1-e faaliyet yılının gider ve gelirlerinin ödeme ve tahsilat tarihlerine bakılmaksızın yılsonu finansal tablolarına alınmasını düzenler.",
        "Tahakkuk ve dönemsellik yaklaşımında nakit tarihi belirleyici değildir. Ekonomik olay hangi faaliyet dönemine aitse gelir veya gider o dönemin sonucuna yansır.",
        "6102 sayılı TTK m.78/1-e", "medium",
    ),
    r(
        "Tacir, ticari defterleri ile alınan ticari mektupları ve kayıtların dayandığı belgeleri üç yıl sonra imha etmeyi planlamaktadır. Saklama süresi bakımından hangisi doğrudur?",
        "TTK m.82/5 uyarınca ticari defterler ve maddede sayılan belgeler kaç yıl saklanmalıdır?",
        "Ticari defter ve sayılan belgeler on yıl süreyle saklanmalıdır",
        ["Ticari defter ve belgeler yalnız bir yıl saklandıktan sonra imha edilmelidir", "Belgeler iki ay saklanır ve ardından sicil müdürlüğüne bırakılır", "Saklama süresi her durumda üç yıl olup uzatılamaz", "Defterler yalnız işletme açıkken saklanır, kapanışta hemen yok edilir"],
        "TTK m.82/1 saklanacak defter ve belge gruplarını sayar; m.82/5 bunlar için on yıllık saklama süresi öngörür.",
        "Saklama yükümlülüğü yalnız defterlerle sınırlı değildir; ticari yazışmalar ve kayıt dayanakları da kapsamdadır. Kanuni süre on yıldır.",
        "6102 sayılı TTK m.82/1 ve 82/5", "easy",
    ),
    r(
        "Defterler sel nedeniyle kanuni saklama süresi içinde zayi olmuş ve tacir kaybı bugün öğrenmiştir. Zıya belgesi istemi bakımından hangisi doğrudur?",
        "Defter ve belgeleri afet veya hırsızlık nedeniyle zayi olan tacir, öğrendiği tarihten itibaren kaç gün içinde hangi merciden belge isteyebilir?",
        "Tacir otuz gün içinde işletme yerindeki yetkili mahkemeden zıya belgesi isteyebilir",
        ["Tacir kural olarak iki gün içinde vergi dairesinden şirket kuruluş belgesi istemelidir", "Tacir bir yıl içinde meslek odasından faaliyet belgesi almak zorundadır", "Tacir süre olmaksızın yalnız noter huzurunda sözlü açıklama yapmalıdır", "Tacir on gün içinde müşterilerinden defter onayı toplamalıdır"],
        "TTK m.82/7'nin güncel metni, afet veya hırsızlık nedeniyle zıyaı öğrenen tacire otuz gün içinde işletmenin bulunduğu yer yetkili mahkemesinden belge isteme imkânı tanır.",
        "Süre zıya olayından değil, tacirin zıyaı öğrendiği tarihten başlar. İstem hasımsız dava yoluyla yetkili mahkemeye yöneltilir.",
        "6102 sayılı TTK m.82/7 (7417 sayılı Kanunla güncel)", "medium",
    ),
    r(
        "Ticari uyuşmazlıkta taraflardan hiçbiri talepte bulunmamış olsa da mahkeme defterlerin görülmesini gerekli bulmuştur. İbraz kararı bakımından hangisi doğrudur?",
        "Ticari uyuşmazlıkta tarafların ticari defterlerinin ibrazına kim, hangi yollarla karar verebilir?",
        "Mahkeme resen veya taraflardan birinin istemi üzerine ibraza karar verebilir",
        ["İbraz ancak iki tarafın aynı anda noter onayı vermesiyle mümkün olabilir", "Mahkeme yabancı tarafın defterlerini hiçbir durumda ibraz ettiremez", "Defter ibrazına yalnız ticaret sicili müdürü ve vergi dairesi birlikte karar verir", "Ticari uyuşmazlıkta defter ibrazı kanunen tamamen yasaktır"],
        "TTK m.83/1 ticari uyuşmazlıklarda mahkemenin, taraf yabancı olsa dahi, ticari defterlerin ibrazına resen veya taraf istemiyle karar verebilmesini düzenler.",
        "İbraz yalnız taraf talebine bağlı değildir. Uyuşmazlığın aydınlatılması için mahkeme kendiliğinden de karar verebilir; yabancılık bu yetkiyi kaldırmaz.",
        "6102 sayılı TTK m.83/1", "medium",
    ),
    r(
        "Miras ve şirket tasfiyesine ilişkin malvarlığı uyuşmazlığında yalnız tek işlem değil, defterlerin tamamının incelenmesi gerekmektedir. Mahkemenin yetkisi bakımından hangisi doğrudur?",
        "Mahkeme ticari defterlerin teslimine ve bütün içeriğinin incelenmesine özellikle hangi tür uyuşmazlıklarda karar verebilir?",
        "Miras, mal ortaklığı ve şirket tasfiyesi gibi malvarlığı uyuşmazlıklarında",
        ["Yalnızca trafik cezaları ve nüfus kaydının düzeltilmesi işlemlerinde", "Sadece seçim sonuçları ve vatandaşlık başvurularında", "Yalnız ceza soruşturmasından bağımsız idari izinlerde", "Sadece tüketicinin garanti belgesi istemine ilişkin işlemlerde"],
        "TTK m.85, malvarlığı hukukuna ilişkin, özellikle miras, mal ortaklığı ve şirket tasfiyesi uyuşmazlıklarında defterlerin teslimine ve tüm içeriğinin incelenmesine karar verilebileceğini söyler.",
        "Olağan ibrazda uyuşmazlıkla ilgili kısım incelenir; malvarlığının bütünüyle ortaya konduğu özel uyuşmazlıklarda tam içerik incelemesi mümkündür.",
        "6102 sayılı TTK m.85", "hard",
    ),
    r(
        "İşletmesini ticaret siciline tescil ettirme yükümlülüğü bugün doğan bir girişimci, ticari defter hükümlerinin ancak fiilî satıştan sonra uygulanacağını düşünmektedir. Hangisi doğrudur?",
        "Ticarete yeni başlayan ve işletmesini tescil ettirmekle yükümlü kişi için ticari defter hükümleri hangi andan itibaren uygulanır?",
        "Hükümler ticaret siciline tescil ettirme yükümlülüğünün doğduğu andan itibaren uygulanır",
        ["Hükümler mutlaka yalnız ilk kâr dağıtımından ve beş faaliyet yılı geçtikten sonra uygulanır", "Defter hükümleri işletme tasfiye edilince geçmişe etkili biçimde uygulanır", "Yeni başlayanlar ticari defter hükümlerinden süresiz ve koşulsuz muaftır", "Uygulama ancak tacirin ilk kez dava edilmesiyle ve mahkeme kararıyla başlar"],
        "TTK m.87, işletmesini tescil ettirmekle yükümlü işletme sahipleri için ticari defterler kısmını tescil ettirme yükümlülüğünün doğduğu andan itibaren uygular.",
        "Başlangıç ölçütü ilk satış veya ilk kâr değildir. Tescil yükümlülüğünün doğmasıyla birlikte defter, envanter ve finansal raporlama düzeni devreye girer.",
        "6102 sayılı TTK m.87", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Ticari defterlerin tutulmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kayıtlar Türkçe tutulur.\n\nII. Kısaltma ve sembollerin anlamı açıklanır.\n\nIII. Kayıtlar eksiksiz, doğru, zamanında ve düzenli yapılır.",
        "correct": "I, II ve III", "why": "TTK m.65/1 dil ve işaret açıklığını; m.65/2 kayıtların eksiksiz, doğru, zamanında ve düzenli yapılmasını öngörür. Üç ifade de doğrudur.",
        "ref": "6102 sayılı TTK m.65/1-2", "difficulty": "medium",
    },
    {
        "stem": "Envanter yükümlülüğüyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşletmenin açılışında envanter çıkarılır.\n\nII. Her faaliyet dönemi sonunda envanter düzenlenir.\n\nIII. Hesap yılı on iki ayı geçemez.",
        "correct": "I, II ve III", "why": "TTK m.66/1 açılış envanterini, m.66/2 dönem sonu envanterini ve hesap yılının on iki ayı geçemeyeceğini birlikte düzenler.",
        "ref": "6102 sayılı TTK m.66/1-2", "difficulty": "medium",
    },
    {
        "stem": "Yılsonu finansal tablolarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bilanço ile gelir tablosundan oluşur.\n\nII. Kural olarak Türkçe ve Türk Lirası ile düzenlenir.\n\nIII. Tacir tarafından tarihsiz ve imzasız bırakılmalıdır.",
        "correct": "I ve II", "why": "TTK m.68 ve 70 uyarınca I ve II doğrudur. TTK m.71 tabloların tacir tarafından tarih atılarak imzalanmasını istediğinden III yanlıştır.",
        "ref": "6102 sayılı TTK m.68, 70 ve 71", "difficulty": "easy",
    },
    {
        "stem": "Finansal tablolardaki değerleme ilkeleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Açılış değerleri önceki kapanış değerleriyle aynı olmalıdır.\n\nII. Değerlemede işletmenin sürekliliğinden hareket edilir.\n\nIII. Gelir ve giderler yalnız nakit hareketi olduğunda kaydedilir.",
        "correct": "I ve II", "why": "TTK m.78/1-a ve b, bilanço bağlantısı ile sürekliliği öngörür. Gelir ve giderler ödeme-tahsilattan bağımsız ilgili döneme alınır; III yanlıştır.",
        "ref": "6102 sayılı TTK m.78/1-a, b ve e", "difficulty": "hard",
    },
    {
        "stem": "Saklama yükümlülüğüyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ticari defterler saklanır.\n\nII. Alınan ticari mektuplar saklanır.\n\nIII. Gönderilen ticari mektupların suretleri saklanmaz.",
        "correct": "I ve II", "why": "TTK m.82/1 ticari defterleri, alınan ticari mektupları ve gönderilen ticari mektupların suretlerini saklama kapsamına alır. III bu nedenle yanlıştır.",
        "ref": "6102 sayılı TTK m.82/1", "difficulty": "easy",
    },
    {
        "stem": "Defterlerin mahkemede incelenmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mahkeme ticari uyuşmazlıkta resen ibraza karar verebilir.\n\nII. İbrazda kural olarak uyuşmazlıkla ilgili kısımlar incelenir.\n\nIII. Miras uyuşmazlığında tüm içeriğin incelenmesine karar verilemez.",
        "correct": "I ve II", "why": "TTK m.83 mahkemeye resen ibraz yetkisi, m.84 ilgili kısımların incelenmesi kuralı verir. TTK m.85 mirasta tam incelemeye izin verdiğinden III yanlıştır.",
        "ref": "6102 sayılı TTK m.83-85", "difficulty": "hard",
    },
    {
        "stem": "Elektronik ticari kayıtlarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Saklama süresince bilgilere erişilebilmelidir.\n\nII. Kayıtların kolaylıkla okunabilir olması gerekmez.\n\nIII. Önceki kaydı görünmez kılan değişiklik yasaktır.",
        "correct": "I ve III", "why": "TTK m.65/4 erişilebilirlik gerektirdiğinden I, m.65/3 önceki içeriği görünmez kılan değişikliği yasakladığından III doğrudur. Okunabilirlik de zorunlu olduğu için II yanlıştır.",
        "ref": "6102 sayılı TTK m.65/3-4", "difficulty": "medium",
    },
    {
        "stem": "Defter ve belgelerin zıyaıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tacirin belgeleri isteyerek imha etmesi zıya belgesi nedenidir.\n\nII. Süre zıyaın öğrenilmesinden itibaren otuz gündür.\n\nIII. İstem işletmenin bulunduğu yer yetkili mahkemesine yöneltilir.",
        "correct": "II ve III", "why": "TTK m.82/7 uyarınca öğrenmeden itibaren otuz günlük süre ve işletme yerindeki yetkili mahkeme kuralı nedeniyle II ve III doğrudur. İsteyerek imha zıya nedeni değildir; I yanlıştır.",
        "ref": "6102 sayılı TTK m.82/7", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="ticaret_hukuku", topic_id="ticari_defterler",
        label="Ticari Defterler", slug="ticari_defterler", prefix="kh-tic-def",
        seed=20260723,
        legislation_version="6102 sayılı TTK m.64–88 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
