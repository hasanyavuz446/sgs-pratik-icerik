# -*- coding: utf-8 -*-
"""Hukuk · Ticaret Hukuku · Ticari Defterler, Envanter ve Finansal Tablolar — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında TTK soruları "6102 sayılı Türk Ticaret Kanunu’na göre …" kalıbıyla; süre ve
elektronik ortamda düzenleme gibi kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6102 sayılı TTK md. 64-88.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_ticari_defterler_2026.json", lesson="ticaret_hukuku", topic="ticari_defterler",
          konu_adi="Ticari Defterler", seed=2026093012, surum="6102 sayılı TTK güncel metni; 29.09.2026 kontrolü")

K = "6102 sayılı Türk Ticaret Kanunu’na göre"

P.sayisal("TTK md. 64",
    f"{K}, fiziki ortamda tutulan yevmiye defterinin kapanış onayı izleyen faaliyet döneminin kaçıncı ayının sonuna "
    "kadar notere yaptırılır?",
    "6", ["1", "2", "3", "12"],
    "Md. 64/3'e göre yevmiye defterinin kapanış onayı izleyen faaliyet döneminin altıncı ayının sonuna kadar, yönetim kurulu "
    "karar defterinin kapanış onayı ise birinci ayının sonuna kadar notere yaptırılır.", zorluk="hard")

P.q("TTK md. 64",
    f"{K}, ticari defterlerin tutulma amacına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Uzmana makul sürede fikir verecek şekilde tutulur.",
    ["Sadece vergi matrahını gösterecek şekilde tutulur.",
     "Sadece tacirin anlayacağı biçimde tutulur.",
     "Sadece nakit hareketlerini gösterir.",
     "Kısaltmalar açıklanmadan kullanılabilir."],
    "Md. 64/1'e göre defterler üçüncü kişi uzmanlara makul bir süre içinde yapacakları incelemede işletmenin faaliyetleri ve "
    "finansal durumu hakkında fikir verebilecek şekilde tutulur.")

P.q("TTK md. 64",
    f"{K}, aşağıdakilerden hangisi ticari defterlerden biri değildir?",
    "Ziyaretçi defteri",
    ["Pay defteri", "Yönetim kurulu karar defteri", "Genel kurul toplantı ve müzakere defteri", "Envanter defteri"],
    "Md. 64/4'e göre pay defteri, yönetim kurulu karar defteri ve genel kurul toplantı ve müzakere defteri gibi muhasebeyle "
    "ilgili olmayan defterler de ticari defterdir; yevmiye, kebir ve envanter defterleri de ticari defterlerdir.",
    zorluk="easy")

P.sayisal("TTK md. 64",
    "(ABC) A.Ş., hesap dönemi takvim yılı olan 2025 faaliyet dönemine ait yönetim kurulu karar defterini fiziki ortamda "
    f"tutmaktadır.\n\n{K}, bu defterin kapanış onayı en geç 2026 yılının kaçıncı ayının sonuna kadar yaptırılmalıdır?",
    "1", ["2", "3", "6", "12"],
    "Md. 64/3'e göre yönetim kurulu karar defterinin kapanış onayı izleyen faaliyet döneminin birinci ayının sonuna kadar "
    "notere yaptırılır.", zorluk="hard")

P.q("TTK md. 64",
    f"{K}, fiziki ortamda tutulan defterlerin açılış onayına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Açılış onayı işlemi mahkemece yapılır.",
    ["Kuruluşta kullanılmadan önce noterce yapılır.",
     "Sonraki dönemlerde dönem başından önceki ayın sonuna kadar yapılır.",
     "Noter ticaret sicili tasdiknamesini arar.",
     "AŞ ve limitedin kuruluşunda sicil müdürlüğünce yapılır."],
    "Md. 64/3'e göre açılış onayları noter tarafından, anonim ve limited şirketlerin kuruluş tescilinde ise ticaret sicili "
    "müdürlüklerince yapılır; mahkemenin böyle bir görevi yoktur.")

P.q("TTK md. 64",
    f"{K}, elektronik ortamda tutulan ticari defterlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Açılış ve kapanışta noter onayı aranmaz.",
    ["Açılışta noter onayı zorunludur.",
     "Kapanışta mahkeme onayı gerekir.",
     "Elektronik defter tutulamaz.",
     "Sadece halka açık şirketler tutabilir."],
    "Md. 64/3'e göre ticari defterlerin elektronik ortamda tutulması hâlinde açılışlarında ve yevmiye ile yönetim kurulu karar "
    "defterinin kapanışında noter veya ticaret sicili müdürlüğü onayı aranmaz.")

P.sayisal("TTK md. 66",
    f"{K}, faaliyet dönemi veya hesap yılı en çok kaç ay olabilir?",
    "12", ["6", "9", "15", "18"],
    "Md. 66/2'ye göre faaliyet dönemi veya başka bir kanuni terimle hesap yılı on iki ayı geçemez.", zorluk="easy")

P.q("TTK md. 64",
    f"{K}, pay defteri ile genel kurul toplantı ve müzakere defterinin sonraki dönemlerde kullanılmasına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Yaprak yeterliyse onaysız kullanılır.",
    ["Her yıl yeniden açılış onayı şarttır.",
     "Her yıl yeni defter alınmalıdır.",
     "Sadece elektronik ortamda kullanılabilir.",
     "Mahkeme izniyle kullanılabilir."],
    "Md. 64/3'e göre pay defteri ile genel kurul toplantı ve müzakere defteri yeterli yaprakları bulunmak kaydıyla izleyen "
    "faaliyet dönemlerinde de açılış onayı yaptırılmaksızın kullanılabilir.", zorluk="hard")

P.q("TTK md. 64",
    f"{K}, TTK’ya tabi kişilerin Vergi Usul Kanunu hükümlerine uyma yükümlülüğüne ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Defter tutma ve kayıt zamanı hükümlerine uyarlar.",
    ["VUK hükümlerine uymaları gerekmez.",
     "TTK hükümleri vergi matrahı tespitini engeller.",
     "VUK sadece esnafa uygulanır.",
     "VUK hükümleri TTK’nın saklama hükümlerini tamamen ortadan kaldırır."],
    "Md. 64/5'e göre TTK'ya tabi kişiler VUK'un defter tutma ve kayıt zamanıyla ilgili hükümlerine uymak zorundadır; TTK "
    "hükümleri vergi kanunlarına uygun matrah tespitine engel değildir.")

P.sayisal("TTK md. 66",
    f"{K}, değişmeyen miktar ve değerle envantere alınan kalemler için kural olarak kaç yılda bir fiziksel sayım yapılması "
    "zorunludur?",
    "3", ["1", "2", "5", "10"],
    "Md. 66/3'e göre düzenli ikame edilen ve ikinci derecede önemli kalemler değişmeyen miktar ve değerle envantere alınabilir; "
    "ancak kural olarak üç yılda bir fiziksel sayım yapılması zorunludur.", zorluk="hard")

P.q("TTK md. 65",
    f"{K}, defterlerin tutulmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Defterler yabancı dilde tutulabilir.",
    ["Kısaltmaların anlamı açıkça belirtilmelidir.",
     "Kayıtlar eksiksiz ve zamanında yapılır.",
     "Önceki içeriği belirsizleştiren çizme yasaktır.",
     "Defterler veri taşıyıcılarıyla da tutulabilir."],
    "Md. 65/1'e göre defterler ve gerekli diğer kayıtlar Türkçe tutulur.", zorluk="easy")

P.q("TTK md. 65",
    f"{K}, defter kayıtlarında yapılacak düzeltmelere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Önceki içerik belirlenemeyecek şekilde değiştirilemez.",
    ["Kayıtlar dilendiği gibi silinebilir.",
     "Düzeltme için noter onayı gerekir.",
     "Hatalı sayfa yırtılarak çıkarılır.",
     "Sonradan yapılan değişikliğin zamanının belli olmaması sorun değildir."],
    "Md. 65/3'e göre bir kayıt önceki içeriği belirlenemeyecek şekilde çizilemez ve değiştirilemez; kayıt sırasında mı "
    "sonradan mı yapıldığı anlaşılmayan değişiklikler yasaktır.")

P.sayisal("TTK md. 67",
    f"{K}, özel envanter faaliyet döneminin kapanışından sonra en çok kaç ay içindeki bir gün itibarıyla "
    "düzenlenebilir?",
    "2", ["1", "3", "4", "6"],
    "Md. 67/3'e göre özel envanter, faaliyet döneminin kapanışından önceki üç veya sonraki iki ay içinde bulunan bir gün "
    "itibarıyla düzenlenebilir.", zorluk="hard")

P.q("TTK md. 65",
    f"{K}, elektronik ortamda tutulan defter ve kayıtlarda aranan şart aşağıdakilerden hangisidir?",
    "Erişilebilir ve okunabilir olmaları",
    ["Her ay notere bildirilmeleri",
     "Kâğıt çıktılarının mahkemeye verilmesi",
     "Sadece yabancı sunucularda tutulmaları",
     "Yıl sonunda silinmeleri"],
    "Md. 65/4'e göre elektronik ortamda tutulan defter ve kayıtlarda bilgilere saklama süresince ulaşılması ve kolaylıkla "
    "okunması temin edilmiş olmalıdır.")

P.q("TTK md. 66",
    f"{K}, tacirin işletmenin açılışında çıkaracağı envanterde gösterilmesi gerekenler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Rakiplerinin pazar payları",
    ["Taşınmazları", "Alacakları", "Borçları", "Nakit parasının tutarı"],
    "Md. 66/1'e göre açılış envanteri taşınmazları, alacakları, borçları, nakit tutarını ve diğer varlıkları değerleriyle "
    "teker teker gösterir.", zorluk="easy")

P.sayisal("TTK md. 67",
    "Hesap dönemi 31 Aralık’ta kapanan bir tacir, kapanış envanterini fiziki sayım yerine kapanıştan önceki bir tarihte "
    f"düzenlenen özel envantere dayandırmak istemektedir.\n\n{K}, bu tarih kapanıştan en çok kaç ay öncesi olabilir?",
    "3", ["1", "2", "4", "6"],
    "Md. 67/3'e göre özel envanter kapanıştan önceki üç ay içindeki bir gün itibarıyla düzenlenebilir.", zorluk="hard")

P.q("TTK md. 66",
    f"{K}, envantere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Envanter sadece açılışta çıkarılır.",
    ["Her faaliyet dönemi sonunda da düzenlenir.",
     "Varlık ve borçlar teker teker gösterilir.",
     "Aynı türdeki stoklar gruplanabilir.",
     "Gruplar ortalama ağırlıklı değerle alınabilir."],
    "Md. 66/2'ye göre tacir açılıştan sonra her faaliyet döneminin sonunda da envanter düzenler.")

P.q("TTK md. 67",
    f"{K}, envanteri kolaylaştırıcı yöntemlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sondaj yöntemi kullanılabilir.",
    ["Fiziksel sayım terk edilemez.",
     "Yöntemin TMS’ye uygunluğu aranmaz.",
     "Sonuçların fiziksel sayımla örtüşmesi aranmaz.",
     "Sadece Bakanlık izniyle yöntem değiştirilebilir."],
    "Md. 67/1'e göre envanter sondaj yöntemi ve genel kabul gören matematiksel-istatistiksel yöntemlerle belirlenebilir; "
    "yöntem TMS'ye uygun olmalı ve sonuçları fiziksel sayım sonuçlarına eş düşmelidir.")

P.sayisal("TTK md. 82",
    f"{K}, tacirin ticari defterlerini ve kayıtların dayandığı belgeleri saklama süresi kaç yıldır?",
    "10", ["3", "5", "7", "15"],
    "Md. 82/5'e göre ticari defterler, envanterler, finansal tablolar, ticari mektuplar ve kayıtların dayandığı belgeler on "
    "yıl saklanır.", zorluk="easy")

P.q("TTK md. 68",
    f"{K}, yılsonu finansal tablolarını oluşturan tablolar aşağıdakilerden hangisinde birlikte verilmiştir?",
    "Bilanço ve gelir tablosu",
    ["Bilanço ve nakit bütçe",
     "Gelir tablosu ve satış raporu",
     "Envanter ve yevmiye defteri",
     "Faaliyet raporu ve bağımsız denetim raporu"],
    "Md. 68/3'e göre bilanço ile gelir tablosu yılsonu finansal tablolarını oluşturur; md. 514 ve TMS hükümleri saklıdır.",
    zorluk="easy")

P.q("TTK md. 69",
    f"{K}, yılsonu finansal tablolarının düzenlenmesine ilişkin ilkeler arasında aşağıdakilerden hangisi yer almaz?",
    "Yabancı para ile düzenlenmesi",
    ["TMS’ye uyularak düzenlenmesi",
     "Açık ve anlaşılır olması",
     "Düzenli faaliyet akışına uygun sürede çıkarılması",
     "Türkçe düzenlenmesi"],
    "Md. 69 ve 70'e göre yılsonu finansal tabloları TMS'ye uygun, açık ve anlaşılır, zamanında ve Türkçe ile Türk Lirası "
    "üzerinden düzenlenir.")

P.sayisal("TTK md. 82",
    "Tacirin saklama süresi içindeki defterleri su baskını nedeniyle zayi olmuştur."
    f"\n\n{K}, tacir zıyaı öğrendiği tarihten itibaren kaç gün içinde mahkemeden kendisine belge verilmesini isteyebilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 82/7'ye göre saklama süresi içindeki defter ve belgeler yangın, su baskını, deprem veya hırsızlık nedeniyle zıyaa "
    "uğrarsa tacir öğrendiği tarihten itibaren otuz gün içinde yetkili mahkemeden belge isteyebilir.")

P.q("TTK md. 71",
    f"{K}, finansal tablolar kim tarafından tarih atılarak imzalanır?",
    "Tacir",
    ["Noter", "Ticaret sicili müdürü", "Vergi dairesi müdürü", "Bağımsız denetçi"],
    "Md. 71'e göre finansal tablolar tacir tarafından tarih atılarak imzalanır.", zorluk="easy")

P.q("TTK md. 72",
    f"{K}, finansal tablolarda mahsup yasağına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aktif kalemler pasif kalemlerle mahsup edilemez.",
    ["Giderler gelirlerle mahsup edilebilir.",
     "Taşınmaz hakları yükleriyle mahsup edilebilir.",
     "Aktif ve pasif net gösterilir.",
     "Mahsup tacirin tercihine bırakılmış olup yasak bulunmaz."],
    "Md. 72/2'ye göre aktif kalemler pasif kalemlerle, giderler gelirlerle, taşınmazlara ilişkin haklar bunlarla ilgili "
    "yüklerle mahsup edilemez.")

P.sayisal("TTK md. 82",
    f"{K}, tüzel kişinin sona ermesi hâlinde defter ve kâğıtlar kaç yıl süreyle sulh mahkemesi tarafından saklanır?",
    "10", ["3", "5", "15", "20"],
    "Md. 82/8'e göre mirasın resmî tasfiyesi hâlinde veya tüzel kişi sona ermişse defter ve kâğıtlar on yıl süreyle sulh "
    "mahkemesince saklanır.", zorluk="hard")

P.q("TTK md. 72",
    f"{K}, mülkiyeti saklı tutularak iktisap edilen ve teminata verilen malvarlığı unsurları kimin bilançosunda "
    "gösterilir?",
    "Teminat verenin",
    ["Teminat alanın", "Bankanın", "Satıcının", "Sicil müdürlüğünün"],
    "Md. 72/1'e göre mülkiyeti saklı tutulması kaydıyla iktisap edilen ve teminata verilen malvarlığı unsurları teminat verenin "
    "bilançosunda; nakdî tevdiler ise teminat alanın bilançosunda gösterilir.", zorluk="hard")

P.q("TTK md. 73",
    f"{K}, TMS’de aksi öngörülmemişse bilançoda ayrı kalemler olarak gösterilmesi gerekenler arasında aşağıdakilerden "
    "hangisi yer almaz?",
    "Tacirin kişisel harcama planı",
    ["Duran varlıklar", "Dönen varlıklar", "Özkaynaklar", "Dönem ayırıcı hesaplar"],
    "Md. 73/1'e göre bilançoda duran ve dönen varlıklar, özkaynaklar, borçlar ve dönem ayırıcı hesaplar ayrı kalemler olarak "
    "gösterilir.")

P.q("TTK md. 74",
    f"{K}, TMS’de aksi öngörülmemişse aşağıdakilerden hangisi için bilançoya aktif kalem konulamaz?",
    "Kuruluş harcamaları",
    ["Satın alınan makineler",
     "Ticari alacaklar",
     "Satın alınan taşınmaz",
     "Kasadaki nakit"],
    "Md. 74/1'e göre TMS'de aksi öngörülmemişse işletmenin kuruluşu ve özkaynak sağlanması amacıyla yapılan harcamalar için "
    "bilançoya aktif kalem konulamaz.")

P.q("TTK md. 74",
    f"{K}, aktifleştirme yasağına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bedelsiz maddi olmayan varlık kural olarak aktifleştirilir.",
    ["Kuruluş harcamaları kural olarak aktifleştirilemez.",
     "Sigorta sözleşmesi giderleri kural olarak aktifleştirilemez.",
     "TMS’de aksi öngörülebilir.",
     "Özkaynak sağlama harcamaları kural olarak aktifleştirilemez."],
    "Md. 74/2'ye göre bedelsiz elde edilmiş maddi olmayan duran varlıklar için, TMS'de aksi öngörülmedikçe, bilançonun aktifine "
    "kalem konulamaz.", zorluk="hard")

P.q("TTK md. 75",
    f"{K}, gerçekleşmesi şüpheli yükümlülükler ve askıdaki işlemlerden doğabilecek muhtemel kayıplar için ne yapılır?",
    "TMS’ye göre karşılık ayrılır.",
    ["Kayıt yapılmaz.",
     "Doğrudan sermayeden düşülür.",
     "Sadece dipnotta belirtilir.",
     "Ertesi yıl gider yazılır."],
    "Md. 75'e göre gerçekleşmesi şüpheli yükümlülükler ve askıdaki işlemlerden doğabilecek muhtemel kayıplar için TMS'deki "
    "kurallara göre karşılık ayrılır.")

P.q("TTK md. 77",
    f"{K}, bono düzenlenmesi ve kefaletler gibi işlemlerden doğan sorumluluklar pasifte gösterilmemişse ne yapılır?",
    "Bilanço altında veya ekte açıklanır.",
    ["gösterilmez.",
     "Gelir tablosunda gelir olarak gösterilir.",
     "Envanterden çıkarılır.",
     "Ticaret siciline ayrıca tescil ettirilir."],
    "Md. 77'ye göre bono, poliçe, çek, kefalet, aval, garanti ve teminatlardan doğan sorumluluklar pasifte gösterilmemişse "
    "bilançonun altında veya ekte TMS'ye göre açıklanır.")

P.q("TTK md. 78",
    f"{K}, genel değerleme ilkelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Değerlemede işletmenin tasfiye edileceği varsayılır.",
    ["Kapanış ve açılış bilançosu değerleri aynı olmalıdır.",
     "Varlık ve borçlar teker teker değerlenir.",
     "Değerleme ihtiyatla yapılır.",
     "Önceki dönemde uygulanan yöntemler korunur."],
    "Md. 78/1-b'ye göre fiilî veya hukuki duruma aykırı olmadıkça değerlemelerde işletme faaliyetinin sürekliliğinden hareket "
    "edilir.")

P.q("TTK md. 78",
    "Bilanço gününden sonra, ancak finansal tablolar düzenlenmeden önce, bilanço gününe kadar doğmuş bir zarar öğrenilmiştir."
    f"\n\n{K}, bu zarar hakkında aşağıdakilerden hangisi doğrudur?",
    "Değerlemede dikkate alınır.",
    ["Sonraki yılın konusudur.",
     "dikkate alınmaz.",
     "Sadece vergi beyannamesinde gösterilir.",
     "Ancak mahkeme kararıyla dikkate alınır."],
    "Md. 78/1-d'ye göre ihtiyat ilkesi gereği bilanço gününe kadar doğmuş bütün muhtemel risk ve zararlar, bilanço günü ile "
    "finansal tabloların düzenlenmesi arasında öğrenilmiş olsalar bile dikkate alınır.", zorluk="hard")

P.q("TTK md. 78",
    f"{K}, faaliyet yılının gider ve gelirlerinin finansal tablolara alınmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tahsil ve ödemeye bakılmaksızın alınır.",
    ["Sadece tahsil edilen gelirler alınır.",
     "Sadece ödenen giderler alınır.",
     "Ödeme tarihine göre ertesi yıla aktarılır.",
     "Tacirin tercihine göre dağıtılır."],
    "Md. 78/1-e'ye göre faaliyet yılının gider ve gelirleri ödeme ve tahsilat tarihlerine bakılmaksızın yılsonu finansal "
    "tablolarına alınır.")

P.q("TTK md. 82",
    f"{K}, tacirin saklamakla yükümlü olduğu belgeler arasında aşağıdakilerden hangisi yer almaz?",
    "Müşterilerin kişisel günlükleri",
    ["Alınan ticari mektuplar",
     "Gönderilen ticari mektupların suretleri",
     "Kayıtların dayandığı belgeler",
     "Yıllık faaliyet raporları"],
    "Md. 82/1'e göre tacir ticari defterlerini, envanter ve finansal tablolarını, faaliyet raporlarını, alınan ticari mektupları, "
    "gönderilenlerin suretlerini ve kayıtların dayandığı belgeleri saklamakla yükümlüdür.", zorluk="easy")

P.q("TTK md. 82",
    f"{K}, saklama süresinin başlangıcına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlgili takvim yılının bitişiyle başlar.",
    ["Belgenin düzenlendiği gün başlar.",
     "Tacirin işletmeyi kapatmasıyla başlar.",
     "Vergi beyannamesinin verilmesiyle başlar.",
     "Finansal tabloların imzalanmasından bir ay sonra başlar."],
    "Md. 82/6'ya göre saklama süresi, son kaydın yapıldığı, envanterin çıkarıldığı, finansal tabloların hazırlandığı veya "
    "belgelerin oluştuğu takvim yılının bitişiyle başlar.")

P.q("TTK md. 82",
    f"{K}, görüntü veya veri taşıyıcılarında saklanamayıp asıllarının saklanması gereken belgeler aşağıdakilerden "
    "hangisidir?",
    "Açılış bilançosu ve finansal tablolar",
    ["Alınan ticari mektuplar",
     "Gönderilen mektup suretleri",
     "Kayıtların dayandığı belgeler",
     "Çalışma talimatları"],
    "Md. 82/3'e göre açılış ve ara bilançoları, finansal tablolar ve topluluk finansal tabloları hariç olmak üzere saklanacak "
    "belgeler şartlarına uygun olarak görüntü veya veri taşıyıcılarda saklanabilir.", zorluk="hard")

P.q("TTK md. 82",
    f"{K}, defterlerin zayi olması hâlinde tacirin mahkemeden belge istemesine ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Dava zayi eden kişiye karşı açılır.",
    ["Dava hasımsız açılır.",
     "İşletmenin bulunduğu yer mahkemesi yetkilidir.",
     "Mahkeme delil toplanmasını emredebilir.",
     "Zayi afet veya hırsızlık sebebiyle olabilir."],
    "Md. 82/7'ye göre zayi belgesi davası hasımsız açılır; tacir ticari işletmesinin bulunduğu yer mahkemesinden belge ister.")

P.q("TTK md. 82",
    f"{K}, gerçek kişi tacirin ölümü hâlinde ticari defter ve kâğıtları saklama yükümlülüğü kime aittir?",
    "Mirasçılarına",
    ["Ticaret sicili müdürlüğüne", "Vergi dairesine", "Ticaret odasına", "Noterliğe"],
    "Md. 82/8'e göre gerçek kişi tacirin ölümü hâlinde mirasçıları, ticareti terk etmesi hâlinde kendisi defter ve kâğıtları "
    "saklamakla yükümlüdür.")

P.q("TTK md. 83",
    f"{K}, ticari uyuşmazlıklarda ticari defterlerin ibrazına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yabancı tacirin defterlerinin ibrazı istenemez.",
    ["Mahkeme resen ibraza karar verebilir.",
     "Taraflardan birinin istemiyle karar verilebilir.",
     "HMK’nın senet ibrazı hükümleri uygulanır.",
     "İbraz ticari uyuşmazlıklarda söz konusudur."],
    "Md. 83/1'e göre ticari uyuşmazlıklarda mahkeme, yabancı gerçek veya tüzel kişi bile olsalar tarafların ticari defterlerinin "
    "ibrazına resen veya istem üzerine karar verebilir.")

P.q("TTK md. 84",
    f"{K}, bir uyuşmazlıkta ibraz edilen ticari defterlerin incelenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlgili kısımlar incelenir.",
    ["Defterin tamamı kural olarak incelenir.",
     "Defterler karşı tarafa teslim edilir.",
     "İnceleme taraflar olmadan yapılır.",
     "Defterlerden suret alınamaz."],
    "Md. 84'e göre ibraz edilen defterlerin uyuşmazlıkla ilgili kısımları tarafların katılımıyla incelenir; gerekirse ilgili "
    "yapraklardan suret alınır.")

P.q("TTK md. 85",
    f"{K}, mahkemenin ticari defterlerin teslimine ve bütün içeriğinin incelenmesine karar verebileceği uyuşmazlıklar "
    "arasında aşağıdakilerden hangisi yer almaz?",
    "Trafik kazasından doğan ceza davası",
    ["Mirasa ilişkin uyuşmazlık",
     "Mal ortaklığına ilişkin uyuşmazlık",
     "Şirket tasfiyesine ilişkin uyuşmazlık",
     "Malvarlığı hukukuna ilişkin uyuşmazlık"],
    "Md. 85'e göre malvarlığı hukukuna ilişkin, özellikle miras, mal ortaklığı ve şirket tasfiyesi uyuşmazlıklarında mahkeme "
    "defterlerin tamamının incelenmesine karar verebilir.")

P.q("TTK md. 86",
    f"{K}, saklanması zorunlu belgeleri sadece veri taşıyıcısıyla ibraz edebilen kişinin yükümlülüğüne ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Okuma araçlarını hazır tutar.",
    ["Giderleri karşı taraf karşılar.",
     "Mahkeme okuma aracını temin eder.",
     "Belgeleri basılı sunma yükümlülüğü yoktur.",
     "Veri taşıyıcıyla ibraz kabul edilmez."],
    "Md. 86'ya göre belgeleri veri taşıyıcısıyla ibraz eden kişi, gideri kendisine ait olmak üzere okuma araçlarını hazır "
    "bulundurur ve gerekirse okunabilir kopyalarını sunar.")

P.q("TTK md. 87",
    f"{K}, ticari defterlere ilişkin hükümler ticarete yeni başlayan ve tescil yükümlüsü olan işletme sahipleri için ne "
    "zaman geçerli olur?",
    "Tescil yükümlülüğü doğunca",
    ["Tescilin ilan edildiği tarihten itibaren",
     "İlk faaliyet yılının sonundan itibaren",
     "İlk vergi beyannamesinden itibaren",
     "Bir yıllık faaliyetten sonra"],
    "Md. 87'ye göre ticari defterlere ilişkin hükümler, ticaret siciline tescil ettirme yükümlülüğünün doğduğu andan itibaren "
    "geçerlidir.", zorluk="hard")

P.q("TTK md. 88",
    f"{K}, Türkiye Muhasebe Standartlarını belirleyip yayımlamaya yetkili kurum aşağıdakilerden hangisidir?",
    "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu",
    ["Sermaye Piyasası Kurulu", "Gelir İdaresi Başkanlığı", "Türkiye Odalar ve Borsalar Birliği", "Türkiye Serbest Muhasebeci Mali Müşavirler Birliği"],
    "Md. 88/2'ye göre TMS, uluslararası standartlarla uyumlu olacak şekilde sadece Kamu Gözetimi, Muhasebe ve Denetim "
    "Standartları Kurumu tarafından belirlenir ve yayımlanır.", zorluk="easy")

P.q("TTK md. 88",
    f"{K}, Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumunun yetkilerine ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Standartları uluslararasından bağımsız belirler.",
    ["Farklı işletme büyüklükleri için özel standart koyabilir.",
     "Kâr amacı gütmeyenler için düzenleme yapabilir.",
     "Sürdürülebilirlik raporlama standartlarını belirleyebilir.",
     "Özel standartlar TMS’nin parçası sayılır."],
    "Md. 88/2'ye göre TMS uygulamada birliği sağlamak ve finansal tablolara milletlerarası geçerlilik kazandırmak amacıyla "
    "uluslararası standartlarla uyumlu olacak şekilde belirlenir.")

P.q("TTK md. 88",
    f"{K}, TMS’de ve ilgili ayrıntı düzenlemesinde hüküm bulunmayan hâllerde aşağıdakilerden hangisi uygulanır?",
    "Milletlerarası genel kabul görmüş muhasebe ilkeleri",
    ["Tacirin kendi belirlediği ilkeler",
     "Vergi dairesinin görüşü",
     "Ticaret odası kararları",
     "Mahkemenin hakkaniyet takdiri"],
    "Md. 88/5'e göre TMS'de ve ilgili ayrıntı düzenlemesinde hüküm bulunmayan hâllerde milletlerarası uygulamada genel kabul "
    "gören muhasebe ilkeleri uygulanır.", zorluk="hard")

P.oncul("TTK md. 74",
    f"{K} TMS’de aksi öngörülmemiş olması kaydıyla aşağıdaki harcama ve varlıklar değerlendirilmektedir:",
    ["Şirket kuruluş giderleri",
     "Satın alınan bilgisayar yazılımı",
     "Sigorta sözleşmesinin yapılması için gerekli giderler",
     "Bedelsiz elde edilen marka"],
    "Yukarıdakilerden hangileri için bilançoya aktif kalem konulamaz?",
    "I, III ve IV",
    ["I ve II", "II ve III", "III ve IV", "I, III ve IV", "I, II, III ve IV"],
    "Md. 74'e göre kuruluş giderleri (I), sigorta sözleşmesi giderleri (III) ve bedelsiz elde edilen maddi olmayan varlıklar "
    "(IV) TMS'de aksi öngörülmedikçe aktifleştirilemez; satın alınan yazılım (II) bu yasak kapsamında değildir.",
    zorluk="hard")

P.q("TTK md. 64",
    f"{K}, tacirin işletmesiyle ilgili olarak gönderdiği belgelere ilişkin yükümlülüğü aşağıdakilerden hangisidir?",
    "Bir kopyasını saklamak",
    ["Aslını notere teslim etmek",
     "Belgeyi imha etmek",
     "Ticaret siciline tescil ettirmek",
     "Karşı tarafın onayını almak"],
    "Md. 64/2'ye göre tacir işletmesiyle ilgili gönderdiği her türlü belgenin kopyasını yazılı, görsel veya elektronik ortamda "
    "saklamakla yükümlüdür.")

P.q("TTK md. 64",
    f"{K}, pay defteri ile yönetim kurulu karar defterinin elektronik ortamda tutulmasını zorunlu kılmaya kim "
    "yetkilidir?",
    "Ticaret Bakanlığı",
    ["Ticaret sicili müdürlüğü", "Noterler Birliği", "Sermaye Piyasası Kurulu", "Türkiye Odalar ve Borsalar Birliği"],
    "Md. 64/4'e 7262 sayılı Kanunla eklenen hükme göre Ticaret Bakanlığı pay defteri, yönetim kurulu karar defteri ile genel "
    "kurul toplantı ve müzakere defterinin elektronik ortamda tutulmasını zorunlu kılabilir.", zorluk="hard")

P.q("TTK md. 66",
    f"{K}, aynı türdeki stok kalemlerinin envantere alınmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gruplanıp ortalama değerle alınabilir.",
    ["Her kalem ayrı ayrı sayılmalıdır.",
     "Stoklar envantere alınmaz, sadece dipnotta gösterilir.",
     "Sadece satış fiyatıyla alınır.",
     "Stoklar sadece yıl ortasında sayılır."],
    "Md. 66/4'e göre aynı türdeki stok kalemleri ve benzer değerdeki taşınır unsurlar gruplar hâlinde toplanabilir ve ortalama "
    "ağırlıklı değerle envantere konulabilir.")

P.q("TTK md. 70",
    f"{K}, yılsonu finansal tabloları kural olarak hangi dil ve para birimiyle düzenlenir?",
    "Türkçe ve Türk Lirası",
    ["İngilizce ve ABD doları",
     "Türkçe ve tacirin seçtiği para",
     "Tacirin seçtiği dil ve Türk Lirası",
     "İki dilde ve iki para birimiyle"],
    "Md. 70'e göre yılsonu finansal tabloları Türkçe ve Türk Lirası ile düzenlenir; diğer kanunlardaki istisnalar saklıdır.",
    zorluk="easy")

P.q("TTK md. 73",
    f"{K}, bilançoda duran varlıklar içinde hangi varlıklar yer alır?",
    "İşletmeye devamlı tahsis edilen varlıklar",
    ["Bir yıl içinde satılacak mallar",
     "Kasadaki nakit",
     "Kısa vadeli alacaklar",
     "Satış amaçlı elde tutulan ve kısa sürede nakde dönüşecek stoklar"],
    "Md. 73/2'ye göre duran varlıklar içinde işletmeye devamlı surette tahsis edilmiş bulunan varlıklar yer alır.")

P.q("TTK md. 76",
    f"{K}, bilanço gününden sonraki belirli bir süre içinde giderleşecek harcamalar hakkında hangi hükümler uygulanır?",
    "TMS hükümleri",
    ["Vergi Usul Kanunu", "Tacirin takdiri", "Ticaret odası kararları", "Borçlar Kanunu"],
    "Md. 76'ya göre bilanço gününden sonraki belirli sürede giderleşecek harcamalar ile gelir oluşturacak tahsilatlar (dönem "
    "ayırıcı hesaplar) hakkında Türkiye Muhasebe Standartları uygulanır.")

P.q("TTK md. 78",
    f"{K}, genel değerleme ilkelerinden ayrılmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Standartlarda öngörülen istisnai durumlarda ayrılınabilir.",
    ["Tacir dilediği gibi ayrılabilir.",
     "Sadece vergi dairesi izniyle ayrılınabilir.",
     "Sadece tasfiye hâlinde ayrılınabilir.",
     "Ticaret sicili müdürünün onayıyla ayrılınabilir ve bu onay her yıl yenilenir."],
    "Md. 78/2'ye göre standartlarda öngörülen hâllerde ve istisnai durumlarda genel değerleme ilkelerinden ayrılınabilir.")

P.q("TTK md. 79",
    f"{K}, duran ve dönen varlıklar hangi ölçülere göre değerlenir?",
    "TMS’deki ölçülere göre",
    ["Vergi Usul Kanunu ölçüsüne göre",
     "Tacirin takdirine göre",
     "Piyasa fiyatına göre",
     "Ticaret odası tarifesine göre"],
    "Md. 79'a göre duran ve dönen varlıklar TMS uyarınca bu standartlarda gösterilen ölçülere göre değerlenir; borçlar ve diğer "
    "kalemler için de aynı standartlar uygulanır.")

P.q("TTK md. 82",
    f"{K}, ticari mektup kavramı aşağıdakilerden hangisini ifade eder?",
    "Bir ticari işe ilişkin tüm yazışmalar",
    ["Sadece tacirler arası mektuplar",
     "Sadece noter ihtarnameleri",
     "Sadece faturalar",
     "Sadece imzalı ve kaşeli olarak gönderilen kâğıt mektuplar"],
    "Md. 82/2'ye göre ticari mektuplar bir ticari işe ilişkin tüm yazışmalardır.", zorluk="easy")

P.q("TTK md. 82",
    f"{K}, elektronik ortama alınan kayıtların saklanmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Basılı olarak da saklanabilir.",
    ["Basılı saklanamaz.",
     "Sadece noter onaylı çıktı saklanır.",
     "Sadece bulutta saklanabilir.",
     "Elektronik kayıt saklanmaz."],
    "Md. 82/4'e göre kayıtlar elektronik ortama alınıyorsa bilgiler bilgisayar yerine basılı olarak da saklanabilir.")

P.q("TTK md. 72",
    f"{K}, teminat olarak nakit tevdi edilmesi hâlinde tevdi edilen nakit kimin bilançosunda gösterilir?",
    "Teminat alanın",
    ["Teminat verenin", "Bankanın", "Noterin", "Her iki tarafın da ayrı ayrı"],
    "Md. 72/1'e göre nakdî tevdilerin söz konusu olduğu hâllerde bunlar teminat alanın bilançosunda yer alır.", zorluk="hard")

P.q("TTK md. 68",
    f"{K}, açılış bilançosunun düzenlenmesinde hangi hükümler uygulanır?",
    "Yılsonu bilançosuna ilişkin hükümler",
    ["Envanter hükümleri",
     "Vergi beyannamesi hükümleri",
     "Ara bilanço hükümleri",
     "Tacirin kendi belirlediği şekil ve içerik kuralları"],
    "Md. 68/1'e göre açılış bilançosunda yılsonu finansal tablolarının yılsonu bilançosuna ilişkin hükümleri uygulanır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
