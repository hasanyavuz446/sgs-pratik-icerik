# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Risk Değerlendirme — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında kontrol riski tanımı, iç kontrol eksikliği boşluk doldurma, denetim riski
ve önemli yanlışlık riskinin iki düzeyi sorulmuştur.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · BDS 315 (Revize, 2022) “Önemli Yanlışlık” Risklerinin Belirlenmesi ve Değerlendirilmesi
  · BDS 330 Bağımsız Denetçinin Değerlendirilmiş Risklere Karşı Yapacağı İşler
  · BDS 265 İç Kontrol Eksikliklerinin Bildirilmesi; BDS 402 Hizmet Kuruluşu Kullanan İşletmeler
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_risk_degerlendirme_2026.json", lesson="denetim", topic="risk_degerlendirme",
          konu_adi="Risk Değerlendirme", seed=2026092844,
          surum="BDS 315 (Revize 2022), BDS 330, BDS 265, BDS 402 güncel metinleri; 28.09.2026 kontrolü")

B315 = "BDS 315 “Önemli Yanlışlık Risklerinin Belirlenmesi ve Değerlendirilmesi”ne göre"
B330 = "BDS 330 “Bağımsız Denetçinin Değerlendirilmiş Risklere Karşı Yapacağı İşler”e göre"
B265 = "BDS 265 “İç Kontrol Eksikliklerinin Bildirilmesi”ne göre"
B402 = "BDS 402 “Hizmet Kuruluşu Kullanan İşletmelerde Denetim”e göre"

# ================================================================ BDS 315: risk değerlendirme prosedürleri
P.q("BDS 315 prg. 14",
    f"{B315}, aşağıdakilerden hangisi risk değerlendirme prosedürleri arasında sayılmaz?",
    "Ticari alacaklar için dış teyit mektubu gönderilmesi",
    ["Yönetimin ve iç denetim fonksiyonundaki kişilerin sorgulanması",
     "Analitik prosedürler",
     "Faaliyetlerin gözlemi ve belgelerin tetkiki",
     "İşletme içindeki diğer uygun kişilerin sorgulanması"],
    "BDS 315 prg. 14'e göre risk değerlendirme prosedürleri; yönetim ve iç denetim dahil işletme içindeki uygun kişilerin "
    "sorgulanması, analitik prosedürler ile gözlem ve tetkiktir. Dış teyit, BDS 505 kapsamında değerlendirilmiş risklere "
    "karşılık olarak uygulanan maddi doğrulama prosedürüdür.", zorluk="easy")

P.q("BDS 315 prg. 13",
    f"{B315}, risk değerlendirme prosedürlerinin tasarlanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Prosedürler, yönetimin beyanlarını doğrulayacak kanıtları öne çıkaracak biçimde tasarlanır.",
    ["Prosedürler, önemli yanlışlık risklerinin belirlenmesi ve değerlendirilmesine uygun dayanak sağlayacak şekilde tasarlanır.",
     "Prosedürler, BDS 330'a uygun müteakip prosedürlerin tasarlanmasına da dayanak oluşturur.",
     "Prosedürler, çelişkili olabilecek kanıtları hariç tutma eğiliminde olmayacak şekilde uygulanır.",
     "Riskler hem finansal tablo düzeyinde hem de yönetim beyanı düzeyinde belirlenip değerlendirilir."],
    "BDS 315 prg. 13'e göre risk değerlendirme prosedürleri, riskleri iki düzeyde belirlemek ve müteakip prosedürleri "
    "tasarlamak için uygun dayanak sağlayacak şekilde; doğrulayıcı kanıt elde etme veya çelişkili kanıtı hariç tutma "
    "eğiliminde olmayan, yani taraflı olmayan bir şekilde tasarlanır ve uygulanır.")

P.q("BDS 315 prg. 16",
    "Denetçi, üçüncü yılını denetlediği işletmede önceki yıllarda edindiği bilgileri ve uyguladığı prosedürlerin sonuçlarını "
    f"cari denetimde kullanmayı düşünmektedir. {B315} bu durumda denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Bu bilgilerin cari denetim için hâlen ihtiyaca uygun ve güvenilir olup olmadığını değerlendirir.",
    ["Önceki yıl bilgilerini cari yıl kanıtı olarak doğrudan kullanır; ek değerlendirme gerekmez.",
     "Önceki yıllara ait bilgileri cari denetimde kullanamaz; risk değerlendirmesini her yıl tamamen sıfırdan yapar.",
     "Bilgileri, yönetimden bunların hâlâ geçerli olduğuna dair yazılı beyan alarak kullanır.",
     "Bilgileri sadece kontrol çevresinde değişiklik olmadığını KGK'ya bildirerek kullanır."],
    "BDS 315 prg. 16'ya göre işletmeyle ilgili önceki deneyimlerden ve önceki denetimlerde uygulanan prosedürlerden elde "
    "edilen bilgileri kullanmayı düşünen denetçi, bu bilgilerin cari denetim için hâlen ihtiyaca uygun ve güvenilir olup "
    "olmadığını değerlendirir.")

P.q("BDS 315 prg. 17-18",
    f"{B315}, denetim ekibi içinde yapılan müzakereye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müzakereye katılmayan üyelere bilgi verilmez; herkes kendi prosedüründen sorumludur.",
    ["Sorumlu denetçi ve ekibin diğer kilit üyeleri müzakerede bulunur.",
     "Müzakere, geçerli finansal raporlama çerçevesinin işletmenin durum ve gerçeklerine uygulanmasını kapsar.",
     "Müzakere, tabloların önemli yanlışlıklara olan açıklığını da kapsar.",
     "Müzakerede alınan önemli kararlar çalışma kâğıtlarına dahil edilir."],
    "BDS 315 prg. 17'ye göre sorumlu denetçi ve kilit üyeler çerçevenin uygulanması ve tabloların önemli yanlışlıklara "
    "açıklığı konularında müzakere eder. Prg. 18'e göre müzakereye katılmayan üyelere hangi konuların bildirileceğine "
    "sorumlu denetçi karar verir; prg. 38-a müzakere ve kararların belgelendirilmesini ister.")

P.q("BDS 315 prg. 19-a",
    f"{B315}, denetçinin işletme ve çevresi hakkında kanaat edinmesi gereken yönler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Denetim ekibinin bu işletme için harcayacağı sürenin ücret karşılığı",
    ["BT kullanımının entegrasyon derecesi dahil işletmenin organizasyon yapısı ve iş modeli",
     "Sektöre, mevzuata ilişkin etkenler ve diğer dış etkenler",
     "İşletmenin finansal performansını değerlendirmek için kullanılan iç ve dış ölçümler",
     "Ortaklık ve üst yönetim yapısı"],
    "BDS 315 prg. 19-a'ya göre denetçi işletmenin organizasyon, ortaklık ve üst yönetim yapısı ile BT kullanımı dahil iş "
    "modeli; sektör, mevzuat ve diğer dış etkenler ile finansal performans ölçümleri hakkında kanaat edinir. Ücret, "
    "denetim şirketinin kendi konusudur.")

# ================================================================ iç kontrol sistemi
P.q("BDS 315 prg. 12-e",
    f"{B315}, aşağıdakilerden hangisi iç kontrol sistemini oluşturan beş bileşenden biri değildir?",
    "Bağımsız denetim",
    ["Kontrol çevresi", "İşletmenin risk değerlendirme süreci", "İşletmenin iç kontrol sistemini izleme süreci",
     "Bilgi sistemi ve iletişim"],
    "BDS 315 prg. 12-e'ye göre iç kontrol sistemi; kontrol çevresi, işletmenin risk değerlendirme süreci, iç kontrol "
    "sistemini izleme süreci, bilgi sistemi ve iletişim ile kontrol faaliyetlerinden oluşur. Bağımsız denetim işletmenin "
    "iç kontrol sisteminin bir bileşeni değildir.", zorluk="easy")

P.q("BDS 315 prg. 12-e",
    f"{B315}, iç kontrol sistemine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Finansal raporlama, faaliyet etkinliği ve mevzuata uygunluk amaçları için makul güvence hedefler.",
    ["Sadece finansal raporlamanın güvenilirliğine yönelik olup faaliyet etkinliğiyle ilgilenmez.",
     "Bağımsız denetçi tarafından tasarlanır ve yönetim tarafından onaylanarak uygulanır.",
     "Doğru tasarlandığında hata ve hilenin tamamını önlediğine dair yönetime ve denetçiye mutlak güvence sağlar.",
     "Sadece yönetim tarafından tasarlanır; diğer personel ve üst yönetimin bir rolü yoktur."],
    "BDS 315 prg. 12-e'ye göre iç kontrol sistemi, finansal raporlamanın güvenilirliği, faaliyetlerin etkinliği ve "
    "verimliliği ile mevzuata uygunluk bakımından işletmenin amaçlarına ulaştığına dair makul güvence sağlamak amacıyla üst "
    "yönetimden sorumlu olanlar, yönetim ve diğer personelce tasarlanan, uygulanan ve sürdürülen sistemdir.")

P.q("BDS 315 prg. 21",
    "Denetçi, işletme kültürünü, yönetimin dürüstlük ve etik değerlere bağlılığını, yetki ve sorumlulukların nasıl "
    f"belirlendiğini ve yetkin personelin nasıl istihdam edildiğini anlamaya çalışmaktadır. {B315} denetçi iç kontrol "
    "sisteminin hangi bileşeni hakkında kanaat edinmektedir?",
    "Kontrol çevresi",
    ["Kontrol faaliyetleri", "Bilgi sistemi ve iletişim", "İşletmenin risk değerlendirme süreci",
     "İç kontrol sistemini izleme süreci"],
    "BDS 315 prg. 21'e göre kontrol çevresi hakkında kanaat edinilirken işletme kültürü ve yönetimin dürüstlük ve etik "
    "değerlere bağlılığı, üst yönetimin gözetimi, yetki ve sorumlulukların belirlenmesi, yetkin kişilerin istihdamı ve "
    "hesap verebilirlik ele alınır.", zorluk="easy")

P.q("BDS 315 prg. 22",
    f"{B315}, işletmenin risk değerlendirme sürecine ilişkin denetçinin kanaat edinmesi gereken hususlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Denetçinin tespit edemediği yanlışlıkların oluşturduğu tespit edememe riskinin ölçülmesi",
    ["Finansal raporlama amaçlarıyla ilgili iş hayatına ilişkin risklerin belirlenmesi",
     "Bu risklerin gerçekleşme ihtimalleri dahil ciddiyetlerinin değerlendirilmesi",
     "Söz konusu risklerin ele alınması",
     "Sürecin işletmenin niteliği ve karmaşıklığı dikkate alındığında duruma uygun olup olmadığı"],
    "BDS 315 prg. 22'ye göre denetçi işletmenin iş risklerini belirleme, ciddiyetlerini ve ihtimallerini değerlendirme ve "
    "bunları ele alma süreci hakkında kanaat edinir ve sürecin duruma uygunluğunu değerlendirir. Tespit edememe riski "
    "denetçiye ait bir risktir, işletmenin sürecinin parçası değildir.")

P.q("BDS 315 prg. 23",
    f"Denetçi, yönetimin kendi risk değerlendirme sürecinde belirleyemediği bir önemli yanlışlık riski belirlemiştir. {B315} "
    "denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Riskin sürecin belirlemesi beklenen türden olup olmadığına karar verir ve sebebini anlar.",
    ["Riski yönetimin sorumluluğunda sayar ve risk değerlendirmesine dahil etmez.",
     "Durumu derhâl önemli iç kontrol eksikliği olarak raporlar ve olumsuz görüş verir.",
     "Yönetimden riski kendi sürecine eklemesini ister; eklenmezse sözleşmeyi feshetmesi gerekir.",
     "Riski sadece bir sonraki yılın denetim planına not olarak ekler."],
    "BDS 315 prg. 23'e göre denetçi, riskin işletmenin sürecinin belirlemesini beklediği türden olup olmadığına karar "
    "verir; öyleyse sürecin bu riski neden belirleyemediğine ilişkin kanaat edinir ve bunun sürecin uygunluğu "
    "değerlendirmesine etkisini dikkate alır.", zorluk="hard")

P.q("BDS 315 prg. 24",
    f"{B315}, işletmenin iç kontrol sistemini izleme sürecine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kontrollerin sürekli ve ayrı değerlendirmelerle izlenmesini, eksikliklerin giderilmesini ve varsa iç denetimi kapsar.",
    ["Sadece bağımsız denetçinin yıllık olarak yaptığı kontrol testlerinden oluşur.",
     "İç denetim fonksiyonu izleme sürecinin değil, kontrol faaliyetlerinin bir parçasıdır.",
     "İzleme sürecinde kullanılan bilgilerin güvenilirliği denetçinin ilgi alanı dışındadır.",
     "Belirlenen kontrol eksikliklerinin giderilmesi izleme sürecinin kapsamında değildir."],
    "BDS 315 prg. 24'e göre denetçi; kontrollerin etkinliğinin sürekli ve ayrı değerlendirmelerle izlenmesi ve "
    "eksikliklerin giderilmesi, varsa iç denetim fonksiyonu, izlemede kullanılan bilgi kaynakları ve bunların "
    "güvenilirliği hakkında kanaat edinir.")

P.q("BDS 315 prg. 25",
    "Denetçi; satış işlemlerinin nasıl başlatıldığını, kaydedildiğini, defteri kebire nasıl aktarıldığını ve finansal "
    f"tablolarda nasıl raporlandığını anlamaya çalışmaktadır. {B315} bu çalışma iç kontrol sisteminin hangi bileşeniyle "
    "ilgilidir?",
    "Bilgi sistemi ve iletişim",
    ["Kontrol çevresi", "İşletmenin risk değerlendirme süreci", "İç kontrol sistemini izleme süreci",
     "Kontrol faaliyetleri"],
    "BDS 315 prg. 25'e göre bilgi sistemi ve iletişim hakkında kanaat edinilirken, kritik önem taşıyan işlem sınıfları "
    "için işlemlerin nasıl başlatıldığı, kaydedildiği, işlendiği, defteri kebire aktarıldığı ve raporlandığı dahil bilgi "
    "akışı anlaşılır.", zorluk="easy")

P.q("BDS 315 prg. 26-a",
    f"{B315}, denetçinin kontrol faaliyetleri bileşeninde belirlemesi gereken kontroller arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "İşletmedeki bütün kontroller, finansal raporlamayla ilgisine bakılmaksızın",
    ["Ciddi risk olduğuna karar verilen riski ele alan kontroller",
     "Standart olmayan yevmiye kayıtları dahil yevmiye kayıtları üzerindeki kontroller",
     "İşleyiş etkinliğini test etmeyi planladığı kontroller",
     "Mesleki muhakemesine göre amaçlarına ulaşmak için uygun gördüğü diğer kontroller"],
    "BDS 315 prg. 26-a'ya göre denetçi; ciddi riskleri ele alan kontrolleri, yevmiye kayıtları üzerindeki kontrolleri, "
    "işleyiş etkinliğini test etmeyi planladığı kontrolleri ve muhakemesine göre uygun diğer kontrolleri belirler. "
    "İşletmedeki bütün kontrolleri belirlemesi gerekmez.")

P.q("BDS 315 prg. 26-ç",
    "Denetçi, satın alma siparişlerinin onaylanmasına ilişkin bir kontrolün tasarımını değerlendirmiş ve kontrolün "
    f"uygulanıp uygulanmadığına karar vermek istemektedir. {B315} bu karar için aşağıdakilerden hangisi doğrudur?",
    "İşletme personelinin sorgulanmasına ek prosedürler uygulanır.",
    ["Personelin sorgulanması tek başına yeterli kanıt sağlar.",
     "Kontrolün uygulandığı, yönetimin yazılı beyanıyla kanıtlanır.",
     "Kontrolün tasarımı uygunsa uygulandığı ayrıca araştırılmaz.",
     "Karar, kontrolün işleyiş etkinliği test edilmeden verilemez."],
    "BDS 315 prg. 26-ç'ye göre denetçi belirlenen her kontrol için tasarımın etkin olup olmadığını değerlendirir ve "
    "işletme personelinin sorgulanmasına ek prosedürler uygulayarak kontrolün uygulanıp uygulanmadığına karar verir. "
    "Uygulanmanın değerlendirilmesi işleyiş etkinliği testiyle aynı şey değildir.")

P.q("BDS 315 prg. 12-d",
    f"{B315}, işletmenin BT süreçleri üzerinde bulunan ve bilgi işleme kontrollerinin etkin biçimde işlemeye devam "
    "etmesini destekleyen kontroller aşağıdakilerden hangisidir?",
    "Genel BT kontrolleri",
    ["Bilgi işleme kontrolleri", "Kontrol çevresi", "Uygulama kontrolleri üzerindeki izleme",
     "BT kullanımından kaynaklanan riskler"],
    "BDS 315 prg. 12-d'ye göre genel BT kontrolleri, bilgi işleme kontrollerinin etkin biçimde işlemeye devam etmesini ve "
    "bilginin bütünlüğü dahil BT çevresinin sürekli doğru çalışmasını destekleyen, BT süreçleri üzerindeki kontrollerdir. "
    "Bilgi işleme kontrolleri ise doğrudan bilginin bütünlüğüyle ilgili riskleri ele alır (prg. 12-a).")

P.q("BDS 315 prg. 12-b",
    f"{B315}, “BT çevresi” kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "BT çevresi sadece donanım ve yazılımdan oluşur; BT süreçleri ve personel bu kavrama dahil değildir.",
    ["BT uygulamaları, veri ambarlarını ve rapor yazıcılarını da içerir.",
     "BT altyapısı ağ, işletim sistemleri, veri tabanları ile ilgili donanım ve yazılımlardan oluşur.",
     "BT süreçleri erişimin, program değişikliklerinin ve BT operasyonlarının yönetimine ilişkin süreçlerdir.",
     "BT çevresi işletmenin faaliyetlerini ve iş stratejilerini desteklemek için kullandığı unsurları kapsar."],
    "BDS 315 prg. 12-b'ye göre BT çevresi; BT uygulamaları ve destekleyici BT altyapısının yanı sıra BT süreçleri ve bu "
    "süreçlerde yer alan personeldir. BT uygulamaları veri ambarlarını ve rapor yazıcılarını da içerir.")

P.q("BDS 315 prg. 27",
    f"{B315}, iç kontrol sisteminin bileşenlerine ilişkin değerlendirmesine dayanarak denetçinin karar vermesi gereken "
    "husus aşağıdakilerden hangisidir?",
    "Bir veya daha fazla kontrol eksikliği belirlenip belirlenmediği",
    ["İç kontrol sisteminin etkinliği hakkında ayrı bir görüş verilip verilmeyeceği",
     "İşletmenin iç denetim biriminin kapatılması gerekip gerekmediği",
     "Kontrollerin yeniden tasarımında yönetime hangi yazılımın önerileceği",
     "Kontrol çevresinin yasal düzenlemelere uygunluğunun tasdik edilip edilmeyeceği"],
    "BDS 315 prg. 27'ye göre denetçi iç kontrol sisteminin her bir bileşenine ilişkin değerlendirmesine dayanarak bir veya "
    "daha fazla kontrol eksikliğinin belirlenip belirlenmediğine karar verir. Finansal tablo denetiminde iç kontrol "
    "hakkında ayrı görüş verilmez.")

# ================================================================ yapısal risk, ciddi risk, ilgili beyanlar
P.q("BDS 315 prg. 12-i",
    f"{B315}, aşağıdakilerden hangisi yapısal risk faktörleri arasında sayılmaz?",
    "İlgili kontrolün yıl içinde etkin işlememesi",
    ["İşlemin karmaşık bir hesaplama gerektirmesi", "Tutarın ölçümünün subjektif yargıya dayanması",
     "Hesabı etkileyen mevzuatın yıl içinde değişmesi", "Ölçümün gelecekteki olaylara bağlı belirsizlik içermesi"],
    "BDS 315 prg. 12-i'ye göre yapısal risk faktörleri, kontroller dikkate alınmadan önce yanlışlığa açıklığı etkileyen "
    "olay veya şartların özellikleridir: karmaşıklık, subjektiflik, değişiklik, belirsizlik ile yönetimin taraflılığı veya "
    "diğer hile riski faktörleri nedeniyle yanlışlığa açıklık. Kontrollerin etkinliği kontrol riskiyle ilgilidir.",
    zorluk="easy")

P.q("BDS 315 prg. 12-ç",
    f"{B315}, “ciddi risk” aşağıdakilerden hangisinde doğru tanımlanmıştır?",
    "Yapısal risk değerlendirmesi aralığın üst sınırına yakın olan veya diğer BDS'lere göre ciddi sayılan risk",
    ["Kontrol riski değerlendirmesi en yüksek düzeyde olan ve iç kontrolle önlenemeyen her risk",
     "Tespit edilen yanlışlık tutarının performans önemliliğini ve açıkça önemsiz eşiğini birlikte aştığı her hesap bakiyesi",
     "Yönetimin kendi risk değerlendirme sürecinde en yüksek olasılık verdiği iş riski",
     "Denetim ücretinin tahsil edilememesi ihtimali yüksek olan müşterilere ilişkin risk"],
    "BDS 315 prg. 12-ç'ye göre ciddi risk, yapısal risk faktörlerinin olasılık ile büyüklük bileşimini etkileme derecesi "
    "nedeniyle yapısal risk değerlendirmesi aralığın üst sınırına yakın olan veya diğer BDS'ler (ör. BDS 240, BDS 550) "
    "uyarınca ciddi risk olarak ele alınması gereken önemli yanlışlık riskidir.", zorluk="hard")

P.q("BDS 315 prg. 12-f",
    f"{B315}, “ilgili yönetim beyanı” kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bir beyanın ilgili olup olmadığına kontroller dikkate alındıktan sonra karar verilir.",
    ["Bir yönetim beyanı, ona ilişkin belirlenmiş bir önemli yanlışlık riski varsa ilgilidir.",
     "İlgili olup olmama kararı, yapısal risk esas alınarak verilir.",
     "Bir veya daha fazla ilgili yönetim beyanı bulunan kalem kritik önem taşıyan kalemdir.",
     "Yönetim beyanları, olası yanlışlık türlerinin mütalaa edilmesinde kullanılır."],
    "BDS 315 prg. 12-f'ye göre bir yönetim beyanı, ona ilişkin belirlenmiş bir önemli yanlışlık riski bulunuyorsa "
    "ilgilidir ve bu karar ilgili kontroller dikkate alınmadan önce (yapısal risk esas alınarak) verilir. Prg. 12-h kritik "
    "önem taşıyan kalemi, prg. 12-j yönetim beyanlarını tanımlar.", zorluk="hard")

P.q("BDS 315 prg. 12-h",
    f"{B315}, bir veya daha fazla ilgili yönetim beyanı bulunan işlem sınıfı, hesap bakiyesi veya açıklama aşağıdakilerden "
    "hangisiyle ifade edilir?",
    "Kritik önem taşıyan işlem sınıfı, hesap bakiyesi veya açıklama",
    ["Ciddi risk içeren hesap bakiyesi veya işlem sınıfı", "Performans önemliliğini aşan işlem sınıfı veya açıklama",
     "Kontrol riski yüksek işlem sınıfı, hesap bakiyesi veya açıklama", "Açıkça önemsiz olmayan açıklama"],
    "BDS 315 prg. 12-h'ye göre bir ya da daha fazla ilgili yönetim beyanı bulunan işlem sınıfı, hesap bakiyesi veya "
    "açıklama kritik önem taşıyan işlem sınıfı, hesap bakiyesi veya açıklamadır.")

P.q("BDS 315 prg. 31",
    f"{B315}, yönetim beyanı düzeyinde belirlenen bir önemli yanlışlık riskinin yapısal risk değerlendirmesinde denetçinin "
    "esas aldığı unsurlar aşağıdakilerden hangisidir?",
    "Yanlışlık ihtimali ve yanlışlığın büyüklüğü",
    ["Kontrollerin tasarımı ve uygulanıp uygulanmadığı",
     "Yönetimin dürüstlüğü ve denetim ücreti",
     "Örneklem büyüklüğü ve seçim yöntemi",
     "Önceki yıl görüşü ve sektör ortalaması"],
    "BDS 315 prg. 31'e göre denetçi, yanlışlık ihtimalini ve yanlışlığın büyüklüğünü değerlendirerek yapısal riski "
    "değerlendirir; bunu yaparken yapısal risk faktörlerinin açıklığı nasıl etkilediğini ve finansal tablo düzeyindeki "
    "risklerin etkisini dikkate alır.")

P.q("BDS 315 prg. 34",
    "Denetçi, stoklar için kontrollerin işleyiş etkinliğini test etmeyi planlamamakta ve sadece maddi doğrulama "
    f"prosedürleri uygulayacaktır. {B315} bu durumda kontrol riskine ilişkin değerlendirme nasıl olur?",
    "Önemli yanlışlık riski değerlendirmesi, yapısal risk değerlendirmesiyle aynı olur; kontrol riski ayrıca düşürülmez.",
    ["Kontrol riski sıfır kabul edilir ve önemli yanlışlık riski yapısal riskin altına iner.",
     "Kontrol riski orta düzeyde varsayılır ve buna göre tespit edememe riski belirlenir.",
     "Kontrol riski, yönetimin kontrollerin etkin olduğuna ilişkin beyanına göre belirlenir.",
     "Kontrol riski değerlendirilmeden müteakip prosedürler tasarlanamaz; kontrol testi yapılır."],
    "BDS 315 prg. 34'e göre denetçi kontrollerin işleyiş etkinliğini test etmeyi planlıyorsa kontrol riskini değerlendirir; "
    "planlamıyorsa kontrol riskine ilişkin değerlendirmesi, önemli yanlışlık riski değerlendirmesinin yapısal risk "
    "değerlendirmesiyle aynı olacağı şekildedir.", zorluk="hard")

P.q("BDS 315 prg. 30",
    f"{B315}, finansal tablo düzeyinde belirlenen önemli yanlışlık risklerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yaygın etkileri ile yönetim beyanı düzeyindeki risklere etkisini değerlendirir.",
    ["Bu riskler sadece belirli bir hesap bakiyesini etkilediğinden ayrıca değerlendirilmez.",
     "Finansal tablo düzeyindeki riskler, yönetim beyanı düzeyindeki riskleri etkilemez.",
     "Bu risklere karşı sadece kontrol testleri uygulanır.",
     "Bu riskler BDS 265'e göre iç kontrol eksikliği olarak raporlanır ve başka işlem yapılmaz."],
    "BDS 315 prg. 30'a göre finansal tablo düzeyindeki riskler için denetçi, bunların yönetim beyanı düzeyindeki risklerin "
    "değerlendirmesini etkileyip etkilemediğine karar verir ve tablolar üzerindeki yaygın etkilerinin niteliğini ve "
    "kapsamını değerlendirir.")

P.q("BDS 315 prg. 33",
    "Bir e-ticaret şirketinde satış işlemleri insan müdahalesi olmadan tamamen otomatik olarak başlatılıp kaydedilmekte ve "
    f"işlem hacmi çok yüksektir. {B315} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Maddi doğrulamanın tek başına yeterli kanıt sağlayıp sağlayamayacağına karar verilir.",
    ["Makine tarafından işlenen işlemlerde kontrol riski bulunmadığından yapısal risk değerlendirilmez.",
     "Yüksek hacimli işlemlerde sadece analitik prosedürler uygulanır, kontroller dikkate alınmaz.",
     "Sistem tarafından işlenen satışlarda yanlışlık olmayacağı varsayılarak bunlar risk değerlendirmesi dışında tutulur.",
     "Bu tür işlemler BDS 402 kapsamında sayılır ve hizmet kuruluşu denetçisinin raporu istenir."],
    "BDS 315 prg. 33'e göre denetçi, yönetim beyanı düzeyindeki riskler için maddi doğrulama prosedürlerinin tek başına "
    "yeterli ve uygun kanıt sağlayamamasının söz konusu olup olmadığına karar verir. Yüksek hacimli ve otomatik işlenen "
    "işlemler bu durumun tipik örneğidir; bu riskleri ele alan kontroller prg. 26'ya göre belirlenir.")

P.q("BDS 315 prg. 35, 37",
    f"{B315}, risk değerlendirmesinin dayanağı ve revizyonu ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Risk değerlendirmesi planlamada bir kez yapılır; sonradan edinilen ve ilk değerlendirmeyle tutarsız bilgi onu değiştirmez.",
    ["Risk değerlendirme kanıtları uygun dayanak sağlamıyorsa ilave risk değerlendirme prosedürleri uygulanır.",
     "Riskler belirlenirken yönetim beyanlarını doğrulayan ve onlarla çelişen tüm kanıtlar mütalaa edilir.",
     "İlk değerlendirmenin dayandığı kanıtlarla tutarsız yeni bilgi edinilirse değerlendirme revize edilir.",
     "Kritik önem taşımayan ancak önemli kalemler için yapılan değerlendirmenin geçerliliği sorgulanır."],
    "BDS 315 prg. 35'e göre kanıtlar uygun dayanak sağlamıyorsa ilave prosedürler uygulanır ve doğrulayıcı veya çelişkili "
    "tüm kanıtlar mütalaa edilir. Prg. 36 önemli ama kritik önem taşımayan kalemlerin yeniden değerlendirilmesini, "
    "prg. 37 tutarsız yeni bilgi hâlinde risk değerlendirmesinin revizyonunu ister.")

P.q("BDS 315 prg. 12-g",
    f"{B315}, iş hayatına ilişkin risklerle önemli yanlışlık riskleri arasındaki ilişkiye dair aşağıdakilerden hangisi "
    "doğrudur?",
    "Çoğu iş riski finansal sonuç doğurur, ancak her iş riski önemli yanlışlık riskine yol açmaz.",
    ["Her iş riski doğrudan önemli yanlışlık riski oluşturur ve her biri ayrı ayrı maddi doğrulamayla test edilir.",
     "İş riskleri sadece yönetimi ilgilendirir; denetçi bunlarla ilgilenmez.",
     "İş riskleri, denetçinin tespit edememe riskinin bir bileşenidir.",
     "İş riskleri sadece işletmenin sürekliliği ile ilgili olduğunda dikkate alınır."],
    "BDS 315 prg. 12-g iş hayatına ilişkin riskleri işletmenin amaçlarına ulaşma kabiliyetini olumsuz etkileyebilecek "
    "riskler olarak tanımlar. Uygulama hükümlerine göre iş riskleri önemli yanlışlık risklerinden daha geniştir; çoğu "
    "finansal sonuç doğursa da tamamı önemli yanlışlık riskine yol açmaz.")

P.q("BDS 315 prg. 20",
    f"{B315}, işletmenin muhasebe politikalarıyla ilgili denetçinin yapması gereken değerlendirme aşağıdakilerden "
    "hangisidir?",
    "Uygun ve geçerli çerçeveyle tutarlı olup olmadıkları",
    ["Politikaların sektördeki diğer işletmelerle birebir aynı olup olmadığı",
     "Politikaların vergi matrahını en aza indirecek şekilde seçilip seçilmediği",
     "Politikaların son beş yılda değiştirilmemiş olup olmadığı",
     "Politikaların yönetim kurulu kararıyla tescil ettirilip ettirilmediği"],
    "BDS 315 prg. 20'ye göre denetçi, işletmenin muhasebe politikalarının uygun olup olmadığını ve geçerli finansal "
    "raporlama çerçevesiyle tutarlı olup olmadığını değerlendirir; prg. 19-b'ye göre politika değişikliklerinin "
    "sebepleri hakkında da kanaat edinir.")

P.q("BDS 315 prg. 38",
    f"{B315}, aşağıdakilerden hangisi risk değerlendirmesine ilişkin çalışma kâğıtlarına dahil edilmesi gerekenler "
    "arasında yer almaz?",
    "İşletme personelinin sorgulamalarda kullandığı her e-postanın tam metni",
    ["Ekip içinde yapılan müzakereler ve alınan önemli kararlar",
     "Edinilen kanaatin temel unsurları, bilgi kaynakları ve uygulanan risk değerlendirme prosedürleri",
     "Belirlenen kontrollerin tasarımının değerlendirilmesi ve uygulanmasına ilişkin karar",
     "Ciddi riskler dahil belirlenen ve değerlendirilen riskler ile önemli yargıların gerekçesi"],
    "BDS 315 prg. 38'e göre çalışma kâğıtlarına ekip müzakereleri ve önemli kararlar, kanaatin temel unsurları, bilgi "
    "kaynakları ve prosedürler, kontrollerin tasarımı ve uygulanmasına ilişkin değerlendirme ile belirlenen riskler ve "
    "önemli yargıların gerekçesi dahil edilir.")

# ================================================================ BDS 330: risklere karşılık
P.q("BDS 330 A1",
    f"{B330}, finansal tablo düzeyinde değerlendirilmiş önemli yanlışlık risklerine karşı yapılabilecek genel işler "
    "arasında aşağıdakilerden hangisi yer almaz?",
    "Önemlilik düzeyini yükselterek test edilecek kalem sayısını azaltmak",
    ["Ekibe mesleki şüpheciliği korumanın gerekliliğini vurgulamak",
     "Daha deneyimli personel görevlendirmek veya uzman kullanmak",
     "Daha fazla yönlendirme ve gözetim yapmak",
     "Müteakip prosedürlerin seçimine ilave öngörülemezlik unsurları katmak"],
    "BDS 330 A1'e göre genel işler; mesleki şüpheciliğin vurgulanması, deneyimli personel veya uzman görevlendirilmesi, "
    "daha fazla yönlendirme ve gözetim, öngörülemezlik unsurları ve prosedürlerde genel değişikliklerdir. Risk "
    "arttığında önemliliği yükseltmek riske uygun bir karşılık değildir.")

P.q("BDS 330 prg. 8",
    f"{B330}, denetçinin kontrol testlerini tasarlayıp uygulaması aşağıdaki durumlardan hangisinde gereklidir?",
    "Maddi doğrulama tek başına yeterli ve uygun kanıt sağlayamıyorsa",
    ["İşletmenin kontrol çevresi zayıf olduğunda ve kontrollere güvenilmeyecekse",
     "Denetçi, maddi doğrulama prosedürlerinin kapsamını genişletmeyi planladığında",
     "Kontrollerin tasarımı etkin değilse ve uygulanmadığı tespit edilmişse",
     "İşletme küçük ölçekli olup iş bölümü sınırlıysa"],
    "BDS 330 prg. 8'e göre kontrol testleri, denetçinin risk değerlendirmesi kontrollerin etkin işlediği beklentisini "
    "içeriyorsa veya maddi doğrulama prosedürleri tek başına yönetim beyanına ilişkin yeterli ve uygun kanıt "
    "sağlayamıyorsa tasarlanıp uygulanır. Tasarımı etkin olmayan kontroller test edilmez.")

P.q("BDS 330 prg. 18",
    f"{B330}, maddi doğrulama prosedürlerinin kapsamına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kontrol riski düşük değerlendirilen önemli hesap bakiyeleri için maddi doğrulama prosedürü uygulanmaz.",
    ["Denetçi, değerlendirilmiş risklerden bağımsız olarak önemli her işlem sınıfı, bakiye ve açıklama için maddi doğrulama uygular.",
     "Denetçi, dış teyit prosedürlerinin maddi doğrulama prosedürü olarak kullanılıp kullanılmayacağını mütalaa eder.",
     "Maddi doğrulama, tabloların muhasebe kayıtlarıyla uygunluğunun veya mutabakatının sağlanmasını içerir.",
     "Maddi doğrulama, tabloların hazırlanması sırasında yapılan önemli yevmiye kayıtlarının incelenmesini içerir."],
    "BDS 330 prg. 18'e göre denetçi, değerlendirilmiş önemli yanlışlık risklerinden bağımsız olarak önemli her işlem "
    "sınıfı, hesap bakiyesi ve açıklama için maddi doğrulama prosedürleri uygular; bunun sebebi risk değerlendirmesinin "
    "muhakemeye dayanması ve iç kontrolün yapısal sınırlamalarıdır. Prg. 19 dış teyiti, prg. 20 kapanış prosedürlerini "
    "düzenler.")

P.q("BDS 330 prg. 21",
    "Denetçi, bir inşaat şirketinde tamamlanma derecesine göre hasılat muhasebeleştirilmesine ilişkin riski ciddi risk "
    f"olarak değerlendirmiş ve bu riske karşı sadece maddi doğrulama prosedürleri uygulamaya karar vermiştir. {B330} "
    "bu prosedürlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Prosedürler detay testlerini de içerir.",
    ["Sadece maddi analitik prosedürler uygulanması yeterlidir.",
     "Kontroller test edilmediği için yönetimin yazılı beyanı yeterlidir.",
     "Ciddi riskte maddi doğrulama yapılmaz; sadece kontrol testleri uygulanır.",
     "Prosedürler ara dönemde uygulanır ve dönem sonuna kadar güncellenmez."],
    "BDS 330 prg. 21'e göre ciddi risk için denetçi özellikle o riske karşılık veren bir maddi doğrulama prosedürü uygular; "
    "ciddi riske karşı sadece maddi doğrulama prosedürleri uygulanacaksa bu prosedürler detay testlerini de içerir.")

P.q("BDS 330 prg. 15",
    "Denetçi, ciddi risk olarak değerlendirdiği ilişkili taraf işlemlerine yönelik kontrollere güvenmeyi planlamaktadır. "
    f"Bu kontroller geçen yıl test edilmiş ve etkin bulunmuştur. {B330} denetçi bu kontrollere ilişkin ne yapmalıdır?",
    "Kontrolleri cari dönemde test eder.",
    ["Geçen yılın test sonuçlarını kullanarak üç yıl daha test etmez.",
     "Kontrollerde değişiklik yoksa geçen yılın kanıtıyla yetinir.",
     "Kontrolleri test etmez, yönetimin yazılı beyanını alır.",
     "Kontrolleri sadece ara dönemde test eder; dönem sonu için kanıt aramaz."],
    "BDS 330 prg. 15'e göre denetçi ciddi risk olduğuna karar verdiği bir riske yönelik kontrollere güvenmeyi planlıyorsa "
    "bu kontrolleri cari dönemde test eder; önceki denetimlerden elde edilen kanıta dayanma imkânı (prg. 13-14) bu "
    "kontroller için kullanılamaz.")

P.sayisal("BDS 330 prg. 14-b",
    "Denetçi, işleyiş etkinliğini önceki bir denetimde test ettiği ve o tarihten bu yana değişmediğini doğruladığı bir "
    f"kontrole güvenmektedir. Kontrol ciddi bir riske yönelik değildir. {B330} denetçi bu kontrolü en az kaç denetimden "
    "birinde yeniden test etmek zorundadır?",
    "3", ["2", "4", "5", "6"],
    "BDS 330 prg. 14-b'ye göre değişiklik olmayan kontroller en az her üç denetimden birinde test edilir; ayrıca sonraki "
    "iki dönemde hiç test yapılmaması ihtimalini önlemek için bazı kontroller her denetimde test edilir. Değişiklik "
    "olmuşsa kontrol cari denetimde test edilir (prg. 14-a); ciddi risk kontrolleri her yıl test edilir (prg. 15).")

P.q("BDS 330 prg. 16",
    "Denetçi, satın alma döngüsünde uyguladığı maddi doğrulama prosedürlerinde herhangi bir yanlışlık tespit etmemiştir. "
    f"{B330} bu sonucun ilgili kontroller bakımından anlamı aşağıdakilerden hangisidir?",
    "Yanlışlık bulunmaması, kontrollerin etkin olduğuna dair kanıt sağlamaz.",
    ["Kontrollerin etkin işlediğini kanıtlar; kontrol testine gerek kalmaz.",
     "Kontrol riskinin sıfır olduğunu gösterir ve önemlilik yükseltilebilir.",
     "Kontrollerin tasarımının uygun olduğunu, ancak uygulanmadığını gösterir.",
     "Kontrollerin gelecek iki yıl için test edilmesine gerek olmadığını gösterir."],
    "BDS 330 prg. 16'ya göre maddi doğrulama prosedürleriyle tespit edilen yanlışlıklar kontrollerin etkin işlemediğine "
    "işaret edebilir; ancak yanlışlık tespit edilmemiş olması test edilen yönetim beyanlarına ilişkin kontrollerin etkin "
    "olduğuna dair kanıt sağlamaz.")

P.q("BDS 330 prg. 17",
    f"Denetçi, güvenmeyi düşündüğü bir onay kontrolünde sapmalar tespit etmiştir. {B330} denetçinin bu durumda yapması "
    "gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Sapmaları dikkate almadan kontrole planlandığı gibi tam olarak güvenmek",
    ["Sapmaları ve muhtemel sonuçlarını anlamak için özel sorgulamalar yapmak",
     "Kontrol testlerinin güven için uygun dayanak oluşturup oluşturmadığına karar vermek",
     "İlave kontrol testlerinin gerekip gerekmediğine karar vermek",
     "Riske maddi doğrulama prosedürleriyle karşılık verme gereğine karar vermek"],
    "BDS 330 prg. 17'ye göre güvenilmesi düşünülen kontrollerde sapma tespit eden denetçi, özel sorgulamalar yaparak "
    "testlerin güven için uygun dayanak oluşturup oluşturmadığına, ilave kontrol testleri veya maddi doğrulama "
    "prosedürleri gerekip gerekmediğine karar verir.")

P.q("BDS 330 prg. 22",
    f"{B330}, maddi doğrulama prosedürlerinin ara dönemde uygulanması hâlinde aşağıdakilerden hangisi doğrudur?",
    "Kalan süre kontrol testiyle birlikte maddi doğrulamayla ya da yeterliyse ilave maddi doğrulamayla kapsanır.",
    ["Ara dönem sonuçları dönem sonuna ek prosedür gerekmeksizin taşınır; kalan süre için yönetimin sözlü açıklaması yeterlidir.",
     "Ara dönemde maddi doğrulama yapılamaz; prosedürler sadece dönem sonunda uygulanır.",
     "Ara dönemden sonraki süre, sadece yönetimin yazılı beyanı alınarak kapsanır.",
     "Ara dönem prosedürleri sadece ciddi risk içeren hesaplar için uygulanabilir."],
    "BDS 330 prg. 22'ye göre maddi doğrulama ara dönemde uygulanmışsa denetçi, aradan geçen süreyi kontrol testleriyle "
    "birlikte maddi doğrulama prosedürleri uygulayarak veya yeterli görürse sadece ilave maddi doğrulama prosedürleri "
    "uygulayarak kapsar.")

P.q("BDS 330 prg. 25-27",
    "Denetimin sonunda denetçi, önemli bir yönetim beyanına ilişkin yeterli ve uygun kanıt elde edemediğini ve ilave "
    f"çabaların da sonuç vermediğini tespit etmiştir. {B330} denetçi ne yapmalıdır?",
    "Sınırlı olumlu görüş verir veya görüş bildirmekten kaçınır.",
    ["Olumlu görüş verir ve durumu dikkat çekilen hususlar paragrafında açıklar.",
     "Yönetimden yazılı beyan alarak eksik kanıtı tamamlar ve olumlu görüş verir.",
     "Olumsuz görüş verir, çünkü kanıt eksikliği yanlışlık anlamına gelir.",
     "Kanıt eksikliğini bir sonraki yılın denetiminde tamamlamak üzere not eder."],
    "BDS 330 prg. 26-27'ye göre denetçi, önemli bir yönetim beyanına ilişkin yeterli ve uygun kanıt elde edememişse daha "
    "fazla kanıt elde etmeye çalışır; elde edemezse sınırlı olumlu görüş verir veya görüş bildirmekten kaçınır. Olumsuz "
    "görüş, kanıt elde edildikten sonra yaygın yanlışlık tespit edildiğinde verilir.")

P.q("BDS 330 prg. 7-b",
    f"{B330}, denetçinin değerlendirdiği risk ile elde etmesi gereken kanıt arasındaki ilişkiye dair aşağıdakilerden "
    "hangisi doğrudur?",
    "Risk yüksek değerlendirildikçe daha ikna edici kanıt elde edilir.",
    ["Risk yüksek değerlendirildikçe daha az kanıt yeterli olur.",
     "Risk düzeyi kanıtın niteliğini değil, sadece denetim ücretini etkiler.",
     "Risk yüksekse kanıt sadece yönetimin sorgulanmasıyla elde edilir.",
     "Risk düzeyinden bağımsız olarak her kalem için aynı kanıt toplanır."],
    "BDS 330 prg. 7-b'ye göre denetçi, risk değerlendirmesi ne kadar yüksekse o kadar ikna edici denetim kanıtı elde eder; "
    "bu, kanıtın miktarını artırmayı veya daha ihtiyaca uygun ya da güvenilir kanıt elde etmeyi gerektirebilir.")

P.q("BDS 330 prg. 20",
    f"{B330}, finansal tabloların kapanış işlemleriyle ilgili maddi doğrulama prosedürleri aşağıdakilerden hangisini "
    "içerir?",
    "Tabloların kayıtlarla mutabakatını ve önemli kapanış kayıtlarının incelenmesini",
    ["Sadece gelir tablosu kalemlerinin önceki yılla karşılaştırılmasını",
     "Yönetimin kapanış sürecine ilişkin yazılı beyanının alınmasını",
     "Kapanış sürecini yürüten personelin performansının ve iş yükünün değerlendirilmesini",
     "Kapanış işlemlerinde kullanılan yazılımın lisanslarının kontrolünü"],
    "BDS 330 prg. 20'ye göre maddi doğrulama prosedürleri, finansal tabloların dayanağı olan muhasebe kayıtlarıyla "
    "uygunluğunu veya mutabakatını ve tabloların hazırlanması sırasında yapılan önemli yevmiye kayıtlarının ve diğer "
    "düzeltmelerin incelenmesini içerir.")

P.q("BDS 330 prg. 12",
    f"Denetçi, kontrollerin işleyiş etkinliğine ilişkin kanıtı ara dönemde elde etmiştir. {B330} bu durumda denetçinin "
    "yapması gereken aşağıdakilerden hangisidir?",
    "Sonraki önemli değişiklikler hakkında kanıt toplar, kalan dönem için ilave kanıtı belirler.",
    ["Ara dönem sonuçlarını tüm dönem için geçerli sayar; başka işlem yapmaz.",
     "Kontrolleri dönem sonunda baştan ve aynı kapsamda yeniden test eder.",
     "Ara dönemde elde edilen kanıtı kullanamaz; dönem sonu kanıtı esas alınır.",
     "Kalan dönem için yönetimden kontrollerin değişmediğine dair yazılı beyan alır ve yetinir."],
    "BDS 330 prg. 12'ye göre kontrollerin işleyiş etkinliğine ilişkin kanıt ara dönemde elde edilmişse denetçi, ara "
    "dönemden sonra bu kontrollerde meydana gelen önemli değişiklikler hakkında kanıt toplar ve kalan dönem için "
    "toplanması gereken ilave kanıtları belirler.")

# ================================================================ BDS 265: iç kontrol eksiklikleri
P.q("BDS 265 prg. 6-b",
    "(i)----: Bir kontrolün yanlışlıkları zamanında önleyemeyecek veya tespit edip düzeltemeyecek şekilde tasarlanması, "
    "uygulanması veya kullanılması ya da gerekli bir kontrolün bulunmaması durumunda mevcuttur. (ii)----: Denetçinin "
    "mesleki muhakemesi sonucunda üst yönetimden sorumlu olanların dikkatini çekmeyi gerektirecek kadar önemli olduğuna "
    f"kanaat getirdiği eksiklik veya eksikliklerin bileşimidir.\n\n{B265} boşluklara sırasıyla aşağıdakilerden hangisi "
    "gelmelidir?",
    "(i) İç kontrol eksikliği (ii) Önemli iç kontrol eksikliği",
    ["(i) Kontrol riski (ii) Önemli iç kontrol eksikliği",
     "(i) İç kontrol eksikliği (ii) Ciddi risk",
     "(i) Yapısal risk (ii) Kontrol riski",
     "(i) Kontrol faaliyeti eksikliği (ii) Önemli iç kontrol zafiyeti"],
    "BDS 265 prg. 6-a iç kontrol eksikliğini, prg. 6-b önemli iç kontrol eksikliğini tanımlar. Kontrol riski bir risk "
    "değerlendirmesidir; ciddi risk ise BDS 315'teki yapısal risk kavramıyla ilgilidir.")

P.q("BDS 265 prg. 9-10",
    f"{B265}, iç kontrol eksikliklerinin bildirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Önemli iç kontrol eksiklikleri denetim raporunun görüş paragrafında açıklanarak bildirilir.",
    ["Önemli iç kontrol eksiklikleri üst yönetimden sorumlu olanlara zamanında ve yazılı olarak bildirilir.",
     "Önemli eksiklikler, uygun olmayan durumlar hariç, uygun yönetim kademesine de yazılı olarak bildirilir.",
     "Yönetimin dikkatini çekmeyi gerektirecek diğer eksiklikler de yönetime zamanında bildirilir.",
     "Bildirim, denetçinin iç kontrolün etkinliği hakkında görüş verdiği anlamına gelmez."],
    "BDS 265 prg. 9-10'a göre önemli iç kontrol eksiklikleri üst yönetimden sorumlu olanlara ve uygun yönetim kademesine "
    "zamanında ve yazılı olarak; diğer önemli görülen eksiklikler yönetime bildirilir. Prg. 11'e göre yazılı bildirim, "
    "denetimin iç kontrolün etkinliği hakkında görüş bildirme amacı taşımadığını açıklar. Denetim raporunda açıklama "
    "öngörülmemiştir.")

P.q("BDS 265 prg. 7-8",
    f"{B265}, denetçinin iç kontrol eksikliklerine ilişkin sorumluluğu aşağıdakilerden hangisidir?",
    "Tespit ettiği eksikliklerin tek başına veya birlikte önemli olup olmadığına karar vermek",
    ["İç kontrolün tüm eksikliklerini tespit etmek için finansal tablo denetiminden ayrı bir iç kontrol denetimi yapmak",
     "Eksiklikleri kendisi gidererek yönetimin iş yükünü azaltmak",
     "Eksikliklerin giderilmesi için gerekli yazılımı işletmeye temin etmek",
     "İç kontrolün etkin olduğuna dair üst yönetime güvence vermek"],
    "BDS 265 prg. 7-8'e göre denetçi, yaptığı çalışmaya dayanarak bir veya daha fazla iç kontrol eksikliği tespit edip "
    "etmediğine ve tespit ettiyse bunların tek başına veya birlikte önemli iç kontrol eksikliği oluşturup oluşturmadığına "
    "karar verir. Denetçi iç kontrol hakkında görüş vermez.")

# ================================================================ BDS 402: hizmet kuruluşu
P.q("BDS 402 prg. 8-c",
    "Bir işletme, bordro işlemlerini bir hizmet kuruluşuna yaptırmaktadır. İşletmenin denetçisi, hizmet kuruluşu "
    "denetçisinden kontrollerin tanımı ve tasarımının yanı sıra belirli bir dönemdeki işleyiş etkinliği hakkında görüş ve "
    f"kontrol testlerinin sonuçlarını içeren bir rapor almıştır. {B402} bu rapor aşağıdakilerden hangisidir?",
    "2 nci tip rapor",
    ["1 inci tip rapor", "Sınırlı güvence raporu", "Hizmet alan işletme denetçisi raporu", "İç denetim raporu"],
    "BDS 402 prg. 8-b'ye göre 1 inci tip rapor kontrollerin tanımı ve tasarımına, prg. 8-c'ye göre 2 nci tip rapor ise "
    "tanım, tasarım ve belirli bir dönemdeki işleyiş etkinliğine ilişkindir ve kontrol testlerinin tanımı ile sonuçlarını "
    "içerir. Kontrollere güvenmek isteyen denetçi için işleyiş etkinliğine ilişkin kanıt 2 nci tip rapordan elde edilir.",
    zorluk="hard")

P.q("BDS 402 prg. 8-f",
    f"{B402}, “hizmet kuruluşu” aşağıdakilerden hangisidir?",
    "Hizmet alan işletmelerin finansal raporlama bilgi sistemine hizmet sunan üçüncü taraf",
    ["Hizmet alan işletmenin finansal tablolarını denetleyen bağımsız denetim kuruluşu",
     "Hizmet alan işletmenin iç denetim faaliyetlerini yürüten organizasyon birimi",
     "Hizmet alan işletmeye sadece temizlik ve güvenlik hizmeti veren, muhasebe ile ilgisi olmayan tedarikçi",
     "Hizmet alan işletmenin ilişkili tarafı olan ve ona finansman sağlayan banka"],
    "BDS 402 prg. 8-f'ye göre hizmet kuruluşu, hizmet alan işletmelerin finansal raporlamaya ilişkin bilgi sistemlerinin "
    "bir parçası olan hizmetleri bu işletmelere sunan üçüncü taraf kuruluştur. Finansal raporlamayla ilgisiz hizmetler "
    "bu kapsamda değildir.")

# ================================================================ öncüllü ve ek
P.oncul("BDS 315 prg. 12, BDS 200 prg. 13",
    f"{B315} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Yapısal risk, ilgili kontroller dikkate alınmadan önce bir yönetim beyanının yanlışlığa açık olmasıdır.",
     "Kontrol riski, denetçinin uyguladığı prosedürlerle önemli bir yanlışlığı tespit edememesi riskidir.",
     "Önemli yanlışlık riski yapısal risk ve kontrol riskinden oluşur.",
     "Tespit edememe riski, denetçinin kontrolü altındaki prosedürlerin niteliği ve kapsamıyla ilgilidir."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV",
    ["I ve II", "II ve IV", "I, II ve III", "I, III ve IV", "II, III ve IV"],
    "BDS 200 prg. 13'e göre yapısal risk kontrollerden önceki açıklıktır (I), önemli yanlışlık riski yapısal ve kontrol "
    "riskinden oluşur (III) ve tespit edememe riski denetçinin prosedürleriyle ilgilidir (IV). II'deki tanım tespit edememe "
    "riskine aittir; kontrol riski iç kontrolün yanlışlığı önleyememe veya tespit edememe riskidir.")

P.oncul("BDS 330 prg. 8, 15, 18",
    f"{B330} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Ciddi riske yönelik kontrollere güvenilecekse bu kontroller cari dönemde test edilir.",
     "Tasarımı etkin olmayan bir kontrolün işleyiş etkinliği test edilerek güvence sağlanır.",
     "Önemli her hesap bakiyesi için risk değerlendirmesinden bağımsız olarak maddi doğrulama uygulanır.",
     "Maddi doğrulamada yanlışlık bulunmaması, kontrollerin etkin olduğunu kanıtlar."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve III",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "I, III ve IV"],
    "BDS 330 prg. 15 ciddi riske yönelik kontrollerin cari dönemde test edilmesini (I), prg. 18 önemli kalemler için "
    "maddi doğrulamayı (III) ister. Tasarımı etkin olmayan kontrol test edilmez (II yanlış); prg. 16'ya göre yanlışlık "
    "bulunmaması kontrollerin etkinliğine kanıt sağlamaz (IV yanlış).", zorluk="hard")

P.q("BDS 330 prg. 19",
    f"{B330}, dış teyit prosedürlerine ilişkin denetçinin yükümlülüğü aşağıdakilerden hangisidir?",
    "Dış teyitlerin maddi doğrulamada kullanılıp kullanılmayacağını mütalaa etmek",
    ["Her denetimde bütün hesap bakiyeleri için ayrım yapmaksızın dış teyit göndermek",
     "Dış teyitleri sadece kontrol testi olarak kullanmak",
     "Dış teyit göndermeden önce Kurumdan izin almak",
     "Dış teyitleri sadece ilişkili taraflara ve kamu kurumlarına göndermek"],
    "BDS 330 prg. 19'a göre denetçi, dış teyit prosedürlerinin maddi doğrulama prosedürü olarak kullanılıp "
    "kullanılmayacağını mütalaa eder; dış teyit prosedürleri BDS 505'te düzenlenir.", zorluk="easy")

P.q("BDS 315 prg. 12-j",
    f"{B315}, yönetim beyanları ile BDS 580 uyarınca alınan yazılı beyanlar arasındaki farka ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Yönetim beyanları risk mütalaasında kullanılır; yazılı beyanlar ayrı bir kanıttır.",
    ["İkisi de aynı kavramdır ve denetçiye imzalı bir mektupla verilir.",
     "Yönetim beyanları sadece gelir tablosu kalemleri için geçerlidir.",
     "Yazılı beyanlar, yönetim beyanlarının yerine geçer ve risk değerlendirmesini sonlandırır.",
     "Yönetim beyanları, denetçinin kendi hazırladığı risk kategorileridir; yönetimle ilgisi yoktur."],
    "BDS 315 prg. 12-j'ye göre yönetim beyanları, tabloların çerçeveye uygun hazırlandığına ilişkin beyanda yapısal olarak "
    "bulunan, alma, ölçme, sunma ve açıklamaya ilişkin açık veya zımni beyanlardır ve denetçi bunları olası yanlışlık "
    "türlerini mütalaa etmek için kullanır. A1'e göre bunlar BDS 580'in zorunlu kıldığı yazılı beyanlardan farklıdır.",
    zorluk="hard")

P.q("BDS 315 prg. 12-c",
    f"{B315}, aşağıdakilerden hangisi “BT kullanımından kaynaklanan riskler” kavramını doğru ifade eder?",
    "BT süreç kontrollerindeki zayıflıktan doğan, bilgi işleme kontrollerine ve bilgi bütünlüğüne yönelik riskler",
    ["İşletmenin BT yatırımlarının beklenen getiriyi sağlamaması nedeniyle ortaya çıkan ve kârlılığı etkileyen iş riskleri",
     "Denetçinin veri analitiği araçlarını kullanırken yaptığı hesaplama hataları",
     "İşletmenin BT personeline ödediği ücretlerin sektör ortalamasının üzerinde olması",
     "BT sistemlerinin amortisman süresinin kısa olması nedeniyle oluşan finansman ihtiyacı"],
    "BDS 315 prg. 12-c'ye göre BT kullanımından kaynaklanan riskler, BT süreçlerindeki kontrollerin etkin olmayan tasarım "
    "veya işleyişi nedeniyle bilgi işleme kontrollerinin etkin olmayan tasarım ve işleyişe açıklığı veya işlemlerin ve "
    "bilgilerin tamlığı, doğruluğu ve geçerliliğine yönelik risklerdir.", zorluk="hard")

# ================================================================ ek sorular (olumsuz kök)
P.q("BDS 315 prg. 21-b",
    f"{B315}, kontrol çevresine ilişkin denetçinin değerlendirmesiyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kontrol çevresindeki eksiklikler, iç kontrol sisteminin diğer bileşenlerini zayıflatmaz.",
    ["Denetçi, yönetimin üst yönetim gözetiminde dürüstlük ve etik davranış kültürü oluşturup oluşturmadığını değerlendirir.",
     "Denetçi, kontrol çevresinin diğer bileşenler için uygun bir zemin oluşturup oluşturmadığını değerlendirir.",
     "Değerlendirmede işletmenin niteliği ve karmaşıklığı dikkate alınır.",
     "Üst yönetimden sorumlu olanların iç kontrol sistemini nasıl gözettiği kontrol çevresinin parçasıdır."],
    "BDS 315 prg. 21-b'ye göre denetçi, dürüstlük ve etik davranış kültürünü, kontrol çevresinin diğer bileşenler için "
    "uygun zemin oluşturup oluşturmadığını ve kontrol çevresindeki eksikliklerin diğer bileşenleri zayıflatıp "
    "zayıflatmadığını değerlendirir; eksiklikler diğer bileşenleri zayıflatabilir.")

P.q("BDS 315 prg. 25-b",
    f"{B315}, denetçinin bilgi sistemi ve iletişim kapsamında kanaat edinmesi gereken iletişim türleri arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Denetçinin, denetim ücret teklifini işletme personeliyle paylaşması",
    ["Finansal raporlamaya ilişkin görev ve sorumlulukların işletmedeki kişiler arasında iletilmesi",
     "Yönetim ile üst yönetimden sorumlu olanlar arasındaki iletişim",
     "Düzenleyici kurumlar gibi işletme dışındaki taraflarla kurulan iletişim",
     "Bilgi sistemindeki raporlama sorumluluklarına ilişkin iletişim"],
    "BDS 315 prg. 25-b'ye göre denetçi, işletmenin kendi içindeki kişiler arasında, yönetim ile üst yönetimden sorumlu "
    "olanlar arasında ve düzenleyici kurumlar gibi dış taraflarla, tabloların hazırlanmasını destekleyen önemli hususlar ve "
    "raporlama sorumlulukları hakkında nasıl iletişim kurduğuna dair kanaat edinir.")

P.q("BDS 330 prg. 4",
    f"{B330}, aşağıdakilerden hangisi müteakip denetim prosedürleri arasında yer almaz?",
    "Risklerin belirlenmesi amacıyla yönetime yöneltilen ilk sorgulamalar",
    ["Kontrollerin işleyiş etkinliğini sınamaya yönelik kontrol testleri",
     "Önemli yanlışlıkları yönetim beyanı düzeyinde tespit etmeye yönelik detay testleri",
     "Maddi analitik prosedürler",
     "Kapanış sürecindeki önemli yevmiye kayıtlarının incelenmesi"],
    "BDS 330 prg. 4'e göre müteakip denetim prosedürleri, değerlendirilen risklere karşılık olarak uygulanan kontrol "
    "testleri ile detay testleri ve maddi analitik prosedürlerden oluşan maddi doğrulama prosedürleridir. Riskleri "
    "belirlemek için yapılan sorgulamalar BDS 315'teki risk değerlendirme prosedürleridir.")

P.q("BDS 330 prg. 13",
    f"{B330}, önceki denetimlerden elde edilen kontrol kanıtının kullanılıp kullanılmayacağına karar verirken denetçinin "
    "mütalaa ettiği hususlar arasında aşağıdakilerden hangisi yer almaz?",
    "Denetim ücretinin önceki yıla göre artmış olması",
    ["Kontrol çevresi ve izleme dahil iç kontrolün diğer unsurlarının etkinliği",
     "Kontrolün manuel ya da BT tabanlı olması gibi özelliklerinden kaynaklanan riskler",
     "Genel BT kontrollerinin etkinliği",
     "Şartlar değiştiği hâlde kontrolün değişmemesinden doğan riskler"],
    "BDS 330 prg. 13'e göre denetçi; iç kontrolün diğer unsurlarının etkinliğini, kontrolün özelliklerinden kaynaklanan "
    "riskleri, genel BT kontrollerinin etkinliğini, kontrolün ve uygulanmasının etkinliğini, şartlar değiştiği hâlde "
    "kontrolün değişmemesi riskini ve önemli yanlışlık risklerini mütalaa eder. Ücret bu kapsamda değildir.")

P.q("BDS 265 prg. 11",
    f"{B265}, önemli iç kontrol eksikliklerine ilişkin yazılı bildirimde yer alması gerekenler arasında aşağıdakilerden "
    "hangisi yer almaz?",
    "Eksikliklerin giderilmesi için denetçinin sunacağı danışmanlık hizmetinin ücreti",
    ["Eksikliklerin tanımlanması ve muhtemel etkilerine ilişkin açıklama",
     "Denetimin amacının finansal tablolar hakkında görüş vermek olduğu",
     "İç kontrolün, etkinliği hakkında görüş vermek amacıyla değil prosedür tasarlamak için dikkate alındığı",
     "Raporlanan hususların, denetim sırasında tespit edilen ve bildirilmeye değer görülen eksikliklerle sınırlı olduğu"],
    "BDS 265 prg. 11'e göre yazılı bildirim, eksikliklerin tanımı ve muhtemel etkileri ile bildirimin kapsamını "
    "anlamaya yetecek bilgiyi (denetimin amacı, iç kontrolün hangi amaçla dikkate alındığı, raporlananların sınırı) "
    "içerir. Danışmanlık teklifi bildirim içeriği değildir ve bağımsızlık sorunu doğurabilir.")

P.q("BDS 402 prg. 20-21",
    f"{B402}, hizmet kuruluşu kullanan bir işletmenin denetçisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi olumlu görüş içeren raporunda hizmet kuruluşu denetçisinin çalışmasına atıf yaparak sorumluluğunu paylaşır.",
    ["Hizmet kuruluşunun sunduğu hizmetlere ilişkin yeterli kanıt elde edilemezse olumlu dışında görüş verilir.",
     "Mevzuat zorunlu kılmadıkça olumlu görüşte hizmet kuruluşu denetçisinin çalışmasına atıf yapılmaz.",
     "Mevzuat atfı zorunlu kılarsa rapor, atfın denetçinin sorumluluğunu azaltmadığını belirtir.",
     "Denetçi, hizmet kuruluşunun sunduğu hizmetleri iç kontrol dahil BDS 315'e uygun olarak anlar."],
    "BDS 402 prg. 20'ye göre yeterli kanıt elde edilemezse BDS 705 uyarınca olumlu dışında görüş verilir. Prg. 21'e göre "
    "mevzuat zorunlu kılmadıkça olumlu görüşte hizmet kuruluşu denetçisinin çalışmasına atıf yapılmaz; zorunluysa atfın "
    "sorumluluğu azaltmadığı belirtilir. Prg. 9 hizmetlerin BDS 315'e göre anlaşılmasını ister.")

P.q("BDS 315 A220",
    f"{B315}, ciddi risklere karar verilmesiyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gerçekleşme ihtimali yüksek olan her yanlışlık riski, büyüklüğüne bakılmaksızın ciddi risktir.",
    ["Hangi risklerin ciddi risk olduğuna karar verilmesi, başka bir BDS belirlemedikçe mesleki muhakemenin konusudur.",
     "Yapısal risk aralığının üst sınırına yakınlık işletmeden işletmeye ve dönemden döneme değişebilir.",
     "Ciddi risklere karar verilmesi, aralığın üst sınırındaki risklere daha fazla dikkat edilmesini sağlar.",
     "Ciddi riskleri ele alan kontrollerin belirlenmesi ve tasarımlarının değerlendirilmesi zorunludur."],
    "BDS 315 A218-A220'ye göre ciddi risk kararı, başka bir BDS belirlemedikçe mesleki muhakemeye dayanır ve olasılık ile "
    "büyüklüğün bileşimine bakılır. A220'deki örneğe göre süpermarketteki nakit gibi ihtimali yüksek fakat büyüklüğü düşük "
    "bir risk ciddi risk olmayabilir.", zorluk="hard")

P.q("BDS 330 A1",
    f"{B330}, denetim prosedürlerine öngörülemezlik unsuru katılmasıyla ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Öngörülemezlik için uygulanacak prosedürlerin ayrıntıları yönetime önceden bildirilir.",
    ["Öngörülemezlik unsurları finansal tablo düzeyindeki risklere karşı genel işler arasında yer alabilir.",
     "Önemlilik düzeyinin altındaki hesaplar için de prosedür seçmek öngörülemezlik sağlayabilir.",
     "Prosedürlerin zamanlamasını beklenenden farklı belirlemek öngörülemezlik unsuru olabilir.",
     "Farklı örnekleme yöntemleri veya habersiz ziyaretler öngörülemezliği artırabilir."],
    "BDS 330 A1'e göre öngörülemezlik unsurlarının katılması genel işlerdendir; beklenmeyen hesap, zamanlama, örnekleme "
    "yöntemi veya habersiz ziyaret bu amaca hizmet eder. Prosedürlerin ayrıntılarının yönetimle önceden paylaşılması "
    "öngörülebilirliği artırır ve etkinliği zedeler (BDS 300 A3).")

if __name__ == "__main__":
    sys.exit(P.yaz())
