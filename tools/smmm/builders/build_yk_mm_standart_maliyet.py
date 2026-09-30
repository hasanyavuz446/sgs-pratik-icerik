# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi · Standart Maliyet — 60 soru, 2026 test biçimi.

Standart türleri ve belirlenmesi; DİMM fiyat/miktar, DİŞ ücret/zaman ve GÜG bütçe/kapasite/verimlilik
farklarının hesaplanması, yorumlanması ve sorumluluk birimleri; MSUGT 7/A seçeneğindeki fark hesapları
(712-713, 722-723, 732-734) ve farkların dönem sonunda stoklar ile satış maliyeti arasında dağıtılması
gerçek kitapçıklardaki gibi tutar veren olaylarla sorulur.

Dayanak: TMS 2 md. 21 (standart maliyetin ölçüm tekniği olarak kullanılması); MSUGT Tekdüzen Hesap Planı
7/A seçeneği; standart maliyet farklarının genel kabul görmüş hesaplama esasları (fiyat ve ücret farkı fiili
miktar/saat, miktar ve zaman farkı standart fiyat/ücret üzerinden). Tutarlar builder içinde hesaplanır ve
farkların toplamı denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K

P = Paket("questions_topic_standart_maliyet_2026.json", lesson="maliyet_muhasebesi", topic="standart_maliyet",
          konu_adi="Standart Maliyet", seed=2026093086,
          surum="TMS 2 md. 21; MSUGT 7/A fark hesapları; standart maliyet fark analizi esasları; 30.09.2026 kontrolü")

R = "Standart maliyet sistemi"
DM = "DİMM standart maliyet farkları"
DI = "DİŞ standart maliyet farkları"
GG = "GÜG standart maliyet farkları"
MK = "Standart maliyet kayıtları (MSUGT 7/A)"


def yon(x):
    return "olumsuz" if x > 0 else "olumlu"


def guc(normal, sabit, degisken, fiili_saat, std_saat, fiili_gug):
    """Üçlü analiz: bütçe (fiili saate göre esnek bütçe), kapasite, verimlilik; toplam denkliği denetlenir."""
    oran = sabit / normal + degisken
    butce_fiili = sabit + degisken * fiili_saat
    b = fiili_gug - butce_fiili
    k = butce_fiili - fiili_saat * oran
    v = (fiili_saat - std_saat) * oran
    t = fiili_gug - std_saat * oran
    assert abs(b + k + v - t) < 0.01
    return oran, b, k, v, t


# ------------------------------------------------------------------ kavramlar
P.q(R,
    "Bir beyaz eşya üreticisi, üretime başlamadan önce her ürün için kullanılacak malzeme miktarını, işçilik süresini "
    "ve genel üretim gideri payını mühendislik ve iş etüdü çalışmalarıyla belirlemektedir. Dönem sonunda gerçekleşen "
    "maliyetler bu önceden belirlenmiş tutarlarla karşılaştırılmakta ve farkların nedenleri sorumlu birimlerle birlikte "
    "araştırılmaktadır.\n\nBu işletmenin uyguladığı maliyet yaklaşımı aşağıdakilerden hangisidir?",
    "Standart maliyet sistemi",
    ["Fiili (gerçek) maliyet sistemi", "Faaliyet tabanlı maliyet sistemi", "Değişken (direkt) maliyet sistemi",
     "Tahmini maliyet sistemi"],
    "Maliyetlerin üretimden önce bilimsel incelemelerle (mühendislik, iş etüdü) saptanması ve gerçekleşen maliyetlerle "
    "karşılaştırılıp farkların analiz edilmesi standart maliyet sisteminin özüdür. Tahmini maliyet de üretimden önce "
    "belirlenir ancak geçmiş deneyime dayanır.", zorluk="easy")

P.q(R,
    "Bir işletmenin yöneticisi, önceden belirlenen maliyetlerle çalışan iki sistemi karşılaştırmaktadır. Birinci sistemde "
    "tutarlar geçmiş yılların ortalamalarına göre, ikinci sistemde ise zaman etüdü ve malzeme testleri gibi teknik "
    "çalışmalarla saptanmaktadır.\n\nTahmini maliyet ile standart maliyet arasındaki temel fark aşağıdakilerden "
    "hangisidir?",
    "Standart maliyet teknik incelemeye, tahmini maliyet geçmiş deneyime dayanır.",
    ["Tahmini maliyet üretimden sonra, standart maliyet üretimden önce belirlenir.",
     "Standart maliyet dış raporlamada, tahmini maliyet iç raporlamada kullanılır.",
     "Standart maliyet sipariş, tahmini maliyet safha yöntemiyle birlikte uygulanır.",
     "Standart maliyet değişken giderleri, tahmini maliyet sabit giderleri kapsar."],
    "Her iki sistemde de maliyetler üretimden önce belirlenir. Tahmini maliyet geçmiş verilere ve deneyime dayanan "
    "yaklaşık bir hesaptır; standart maliyet ise mühendislik ve iş etüdü gibi teknik incelemelerle saptanan, olması "
    "gereken maliyettir.")

P.q(R,
    "Bir işletme standartlarını; makinelerin arızasız çalıştığı, işçilerin boş beklemediği ve malzemenin firesiz "
    "kullanıldığı en iyi çalışma koşullarına göre belirlemiştir. Yönetim, bu standartlara neredeyse hiçbir dönemde "
    "ulaşılamadığını ve her ay yüksek tutarlı olumsuz farklar çıktığını gözlemlemektedir.\n\nBu işletmenin kullandığı "
    "standart türü ve bundan doğan sakınca aşağıdakilerden hangisinde doğru verilmiştir?",
    "İdeal standart; sürekli olumsuz fark çalışanların motivasyonunu düşürür.",
    ["Normal standart; farklar dönemler arasında dengelenip kaybolur.",
     "Temel standart; yıllarca değiştirilmediğinden güncelliğini yitirir.",
     "Ulaşılabilir standart; olumlu farklar maliyetleri düşük gösterir.",
     "Tarihî standart; geçmiş dönem verimsizliklerini standarda taşır."],
    "Hiçbir kaybı öngörmeyen, en iyi koşullara göre belirlenen standart ideal standarttır. Ulaşılması neredeyse "
    "imkânsız olduğundan sürekli olumsuz fark verir; bu da çalışanlarda standarda ulaşılamayacağı düşüncesini "
    "yaratarak motivasyonu düşürür.")

P.q(R,
    "Bir gıda işletmesinin yönetim kurulu, standart maliyet sistemine geçmeden önce sistemin sağlayacağı yararları ve "
    "gerektirdiği koşulları tartışmaktadır.\n\nStandart maliyet sistemiyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Standartlar bir kez belirlenince koşullar değişse de güncellenmez.",
    ["Sapmaların sorumlu birimlere göre izlenmesini sağlar.",
     "Bütçe hazırlama ve fiyatlandırma kararlarına dayanak oluşturur.",
     "Yönetimin dikkatini olağan dışı sapmalara yöneltir.",
     "Stok değerlemesini ve kayıt işlemlerini hızlandırır."],
    "Standartlar fiyat, teknoloji ve üretim yöntemindeki değişikliklere göre düzenli olarak gözden geçirilip "
    "güncellenmelidir; aksi hâlde farklar anlamını yitirir. Diğer ifadeler sistemin bilinen yararlarıdır.")

P.q(R,
    "Bir mobilya işletmesinde ay sonunda direkt ilk madde ve malzemede önemli tutarda aleyhte bir fark saptanmıştır. "
    "İnceleme, satın alma biriminin acil sipariş nedeniyle keresteyi piyasa fiyatının üzerinde aldığını ortaya "
    "koymuştur. Üretimde birim başına kullanılan kereste miktarı ise standarda uygundur.\n\nBu sapmanın niteliği ve "
    "sorumlusu bakımından aşağıdakilerden hangisi doğrudur?",
    "Olumsuz fiyat farkıdır; satın alma birimi sorumludur.",
    ["Olumsuz miktar farkıdır; üretim birimi sorumludur.",
     "Olumsuz fiyat farkıdır; üretim birimi sorumludur.",
     "Olumlu fiyat farkıdır; satın alma birimi sorumludur.",
     "Olumsuz verimlilik farkıdır; bakım birimi sorumludur."],
    "Malzemenin standarttan yüksek fiyatla alınması olumsuz fiyat farkı doğurur. Fiyat farkları, alım kararını veren "
    "ve fiyatı kontrol edebilen satın alma biriminin sorumluluğundadır; kullanım standarda uygun olduğundan miktar "
    "farkı yoktur.", zorluk="easy")

P.q(R,
    "Bir tekstil işletmesinde satın alma birimi, standarttan daha ucuz ancak daha düşük kaliteli iplik almıştır. Bu "
    "iplikler dokuma sırasında sık koptuğu için standarttan fazla iplik tüketilmiş, işçiler de kopan iplikleri "
    "bağlamak için standart süreden fazla çalışmıştır. Saat ücretlerinde değişiklik olmamıştır.\n\nBu durumda ortaya "
    "çıkması beklenen farklar aşağıdakilerden hangisidir?",
    "Olumlu fiyat, olumsuz miktar ve olumsuz zaman farkı",
    ["Olumsuz fiyat, olumlu miktar ve olumlu zaman farkı",
     "Olumlu fiyat, olumlu miktar ve olumsuz ücret farkı",
     "Olumsuz fiyat, olumsuz miktar ve olumlu zaman farkı",
     "Olumlu fiyat, olumsuz miktar ve olumsuz ücret farkı"],
    "Ucuz alım olumlu fiyat farkı verir; düşük kalite fazla tüketime (olumsuz miktar farkı) ve fazla çalışmaya "
    "(olumsuz zaman farkı) yol açar. Ücret değişmediğinden ücret farkı doğmaz. Olumlu fiyat farkı bu nedenle gerçek "
    "bir başarı sayılmaz.", zorluk="hard")

P.q(DI,
    "Bir otomotiv yan sanayi işletmesinde, izne ayrılan acemi işçilerin yerine geçici olarak standart ücretten daha "
    "yüksek saat ücreti alan deneyimli ustalar çalıştırılmıştır. Ustalar işi standart süreden daha kısa sürede "
    "tamamlamış, malzeme kullanımı ise standarda uygun gerçekleşmiştir.\n\nBu durumun direkt işçilik farklarına "
    "etkisi aşağıdakilerden hangisidir?",
    "Ücret farkı olumsuz, zaman farkı olumlu",
    ["Ücret farkı olumlu, zaman farkı olumsuz",
     "Ücret farkı ve zaman farkı olumsuz",
     "Ücret farkı ve zaman farkı olumlu",
     "Ücret farkı olumsuz, miktar farkı olumlu"],
    "Standarttan yüksek saat ücreti olumsuz ücret farkı doğurur; işin standart süreden kısa sürede bitmesi ise "
    "olumlu zaman farkıdır. Miktar farkı DİMM’e ilişkindir ve malzeme kullanımı standarda uygundur.")

P.q(GG,
    "Bir işletmede ay içinde siparişlerin azalması nedeniyle makineler normal kapasitenin altında çalıştırılmıştır. "
    "Sabit genel üretim giderleri bütçelendiği tutarda gerçekleşmiş, ancak fiili çalışma saati normal kapasite "
    "saatinin belirgin biçimde altında kalmıştır.\n\nBu durumun ortaya çıkardığı GÜG farkı ve anlamı "
    "aşağıdakilerden hangisidir?",
    "Olumsuz kapasite farkı; atıl kapasitenin maliyetini gösterir.",
    ["Olumsuz bütçe farkı; giderlerin bütçeyi aştığını gösterir.",
     "Olumlu kapasite farkı; sabit giderin fazla yüklendiğini gösterir.",
     "Olumsuz verimlilik farkı; işçilerin yavaş çalıştığını gösterir.",
     "Olumlu bütçe farkı; sabit giderlerde tasarruf edildiğini gösterir."],
    "Sabit GÜG normal kapasiteye göre belirlenen oranla yüklenir. Fiili çalışma normal kapasitenin altında kalınca sabit "
    "giderin bir kısmı mamullere yüklenemez; bu tutar olumsuz kapasite farkıdır ve atıl kapasitenin maliyetini "
    "gösterir.")

P.q(GG,
    "Bir işletmede genel üretim giderleri direkt işçilik saati esasına göre yüklenmektedir. Ay içindeki fiili üretim "
    "için standart olarak 8.000 saat gerekirken işçiler 8.600 saat çalışmıştır; gider kalemleri ise fiili saate göre "
    "bütçelenen tutarlarda gerçekleşmiştir.\n\nBu 600 saatlik fazla çalışmanın GÜG farkları içindeki karşılığı "
    "aşağıdakilerden hangisidir?",
    "Olumsuz verimlilik farkı",
    ["Olumsuz kapasite farkı", "Olumsuz bütçe farkı", "Olumlu verimlilik farkı", "Olumsuz ücret farkı"],
    "Fiili saat ile fiili üretim için izin verilen standart saat arasındaki farkın standart GÜG oranıyla çarpımı "
    "verimlilik farkıdır. Fazla çalışıldığından fark olumsuzdur; ücret farkı ise direkt işçiliğe ilişkindir.")

P.q(MK,
    "Tekdüzen Hesap Planı’nın 7/A seçeneğini ve standart maliyet sistemini uygulayan bir işletmenin muhasebe "
    "müdürü, yeni çalışanlara fark hesaplarının işleyişini anlatmaktadır.\n\n712 Direkt İlk Madde ve Malzeme Fiyat "
    "Farkı hesabı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Olumsuz farklar borcuna, olumlu farklar alacağına yazılır; dönem sonunda stok ve satış maliyeti hesaplarına "
    "aktarılır.",
    ["Olumsuz farklar alacağına, olumlu farklar borcuna yazılır; dönem sonunda 689 hesabına aktarılarak kapatılır.",
     "Olumlu ve olumsuz farklar borcuna yazılır; dönem sonunda 150 İlk Madde ve Malzeme hesabına aktarılır.",
     "Fiyat ve miktar farkları birlikte izlenir; dönem sonunda kapatılmaz ve bilançoda aktif olarak kalır.",
     "Olumsuz farklar borcuna yazılır; olumlu farklar bu hesapta değil 649 hesabında gelir olarak izlenir."],
    "MSUGT 7/A’da 712 hesabı DİMM fiyat farklarını izler: olumsuz farklar borca, olumlu farklar alacağa kaydedilir. "
    "Dönem sonunda hesap, farkın ilgili olduğu stok ve satış maliyeti hesaplarına aktarılarak kapatılır; miktar "
    "farkları ayrıca 713 hesabında izlenir.")

P.q(MK,
    "Tekdüzen Hesap Planı’nın 7/A seçeneğini uygulayan bir işletmede ay sonu analizinde, işçilerin fiili üretim için "
    "izin verilen standart süreden daha uzun çalıştığı ve bu nedenle aleyhte bir direkt işçilik farkı doğduğu "
    "anlaşılmıştır.\n\nBu fark hangi hesabın hangi tarafına kaydedilir?",
    "723 hesabının borç tarafına",
    ["723 hesabının alacak tarafına", "722 hesabının borç tarafına", "713 hesabının borç tarafına",
     "733 hesabının alacak tarafına"],
    "Standart süreden uzun çalışma olumsuz direkt işçilik süre (zaman) farkıdır ve 723 Direkt İşçilik Süre Farkları "
    "hesabının borcuna kaydedilir. 722 ücret farklarını, 713 DİMM miktar farklarını, 733 GÜG verimlilik farklarını "
    "izler.")

P.q(MK,
    "Bir işletme standart maliyet sistemini uygulamaktadır. Dönem sonunda fark hesaplarında hem önemli hem de önemsiz "
    "tutarlar birikmiştir; üretilen mamullerin bir kısmı satılmış, bir kısmı stokta ve yarı mamul olarak "
    "kalmıştır.\n\nStandart maliyet farklarının dönem sonu işlemleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Önemli farklar bütünüyle dönem gideri yazılır, stoklara pay verilmez.",
    ["Fark hesapları dönem sonunda kapatılır ve bilançoda yer almaz.",
     "Önemsiz farklar satılan mamul maliyetine aktarılabilir.",
     "Önemli farklar yarı mamul, mamul ve satış maliyeti arasında dağıtılır.",
     "Farkların nedenleri sorumluluk merkezleri itibarıyla araştırılır."],
    "Stokların gerçek maliyete yakın değerle raporlanması için önemli farklar yarı mamul, mamul ve satılan mamul "
    "maliyeti arasında dağıtılır; önemsiz farklar doğrudan satış maliyetine aktarılabilir. Önemli farkların tamamının "
    "gider yazılması stokları yanlış ölçer.", zorluk="hard")

P.q(R,
    "Bir otomotiv parçası üreticisi, stoklarını kolaylık sağladığı gerekçesiyle standart maliyetle ölçmek "
    "istemektedir. Bağımsız denetçi, bu uygulamanın TMS 2 Stoklar Standardı’na uygunluğunu incelemektedir.\n\nTMS 2’ye "
    "göre standart maliyet yönteminin stok ölçümünde kullanılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Sonuçları gerçek maliyete yakınsa kullanılabilir; standartlar düzenli gözden geçirilir.",
    ["Stoklar standart maliyetle ölçülür; farklar dipnotta açıklanır, stoğa yansıtılmaz.",
     "Kullanılması yasaktır; stoklar sadece fiili maliyetle ölçülebilir.",
     "Standart maliyet net gerçekleşebilir değerden yüksekse onun yerine kullanılır.",
     "Standartlar normal kapasite yerine ideal kapasiteye göre belirlenmelidir."],
    "TMS 2 md. 21’e göre standart maliyet gibi teknikler, sonuçları maliyete yaklaştığı takdirde kolaylık amacıyla "
    "kullanılabilir. Standartlar normal düzeydeki malzeme, işçilik, verimlilik ve kapasite kullanımını dikkate alır; "
    "düzenli olarak gözden geçirilir ve gerektiğinde güncellenir.")

P.q(R,
    "Bir holdingin üretim direktörü, her ay yüzlerce maliyet kalemini tek tek incelemek yerine yalnızca standarttan "
    "önceden belirlenmiş sınırı aşan ölçüde sapan kalemleri inceleyerek zamanını etkin kullanmaktadır. Standarda yakın "
    "gerçekleşen kalemler rapor özetinde toplu olarak gösterilmektedir.\n\nStandart maliyet sisteminin sağladığı bu "
    "yönetim anlayışı aşağıdakilerden hangisidir?",
    "İstisnalara göre yönetim",
    ["Amaçlara göre yönetim", "Katılımcı yönetim anlayışı", "Toplam kalite yönetimi", "Tam zamanında üretim"],
    "Yöneticinin dikkatini yalnızca standarttan önemli ölçüde sapan kalemlere yöneltmesi istisnalara göre yönetim "
    "ilkesidir; standart maliyet sistemi farkları raporlayarak bu yaklaşımı mümkün kılar.", zorluk="easy")

P.q(GG,
    "Bir işletme GÜG farklarını, dönem başında tek bir faaliyet düzeyi için hazırlanan sabit (statik) bütçe yerine "
    "fiili faaliyet düzeyine uyarlanmış esnek bütçeyle karşılaştırarak analiz etmektedir. Ay içinde üretim, planlanan "
    "düzeyin %15 üzerinde gerçekleşmiştir.\n\nBu yaklaşımın gerekçesi aşağıdakilerden hangisidir?",
    "Değişken GÜG faaliyet hacmiyle değiştiğinden karşılaştırma aynı hacimde yapılmalıdır.",
    ["Sabit GÜG faaliyet hacmiyle orantılı değiştiğinden bütçe her ay yenilenmelidir.",
     "Esnek bütçe kapasite farkını ortadan kaldırarak toplam farkı sıfıra indirir.",
     "Statik bütçe vergi mevzuatına uygun olmadığından fark analizinde kullanılamaz.",
     "Esnek bütçe fiili giderleri standarda eşitleyerek fark çıkmasını engeller."],
    "Üretim planlanandan fazla gerçekleştiğinde değişken giderlerin de artması doğaldır. Fiili gideri statik bütçeyle "
    "karşılaştırmak hacim etkisini verimsizlik gibi gösterir; esnek bütçe, karşılaştırmayı fiili faaliyet düzeyinde "
    "yaparak bu etkiyi ayırır.")

P.oncul(R,
    "Bir maliyet muhasebesi eğitiminde standart maliyet sistemiyle ilgili aşağıdaki ifadeler tartışılmıştır:",
    ["Standart maliyetler üretime başlamadan önce belirlenir.",
     "İdeal standartlar hiçbir kayıp ve beklemeye yer vermeyen en iyi çalışma koşullarını esas alır.",
     "Olumlu bir fark her zaman işletme lehine bir performansı gösterir.",
     "Standart saat, fiili üretim miktarı ile birim başına standart sürenin çarpımıdır."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve II", "I, II ve III", "I, II ve IV", "II, III ve IV", "I, III ve IV"],
    "I, II ve IV doğrudur. III yanlıştır: örneğin düşük kaliteli ucuz malzemeden doğan olumlu fiyat farkı, olumsuz "
    "miktar ve zaman farklarıyla işletmenin aleyhine sonuç verebilir.")

P.q(DI,
    "Bir işletmenin iç denetçisi, direkt işçilik fark raporunu hazırlayan maliyet uzmanının kullandığı formülleri "
    "kontrol etmektedir. İşletmede ücret ve zaman farkları ayrı hesaplarda izlenmektedir.\n\nDirekt işçilik "
    "farklarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Ücret farkı, saat farkının standart ücretle çarpımıdır.",
    ["Zaman farkı, fiili ve standart saat farkının standart ücretle çarpımıdır.",
     "Ücret farkı, saat ücreti farkının fiili saatle çarpımıdır.",
     "Toplu sözleşmeyle artan ücretler olumsuz ücret farkı doğurur.",
     "Makine arızası nedeniyle bekleme süreleri zaman farkını artırır."],
    "Saat farkının standart ücretle çarpımı zaman farkını verir; ücret farkı ise fiili ve standart saat ücreti "
    "arasındaki farkın fiili saatle çarpımıdır. Bu nedenle soru konusu ifade iki farkı birbirine karıştırmaktadır.")

P.q(GG,
    "Genel üretim giderlerini direkt işçilik saatine göre yükleyen bir işletme, GÜG farklarını bütçe, kapasite ve "
    "verimlilik farkı olarak üçlü analizle incelemektedir.\n\nGenel üretim gideri farklarıyla ilgili "
    "aşağıdakilerden hangisi yanlıştır?",
    "Kapasite farkı, değişken GÜG’ün bütçeden sapmasından doğar.",
    ["Bütçe farkı, fiili GÜG ile fiili saate göre bütçe arasındaki farktır.",
     "Verimlilik farkı, fiili ve standart saat farkından doğar.",
     "Kapasite farkı, atıl kapasitenin sabit GÜG maliyetini gösterir.",
     "Üç farkın toplamı, fiili ve yüklenen GÜG arasındaki farka eşittir."],
    "Kapasite farkı, fiili çalışmanın normal kapasiteden sapması nedeniyle sabit GÜG’ün eksik ya da fazla "
    "yüklenmesinden doğar. Değişken GÜG’ün bütçeden sapması bütçe farkının konusudur.")

P.q(MK,
    "Standart maliyet sistemini uygulayan bir işletmenin muhasebe birimi, MSUGT’deki 7/A seçeneğine göre fark "
    "hesaplarını açmaktadır. Hesap kodları yeni stajyere tablo hâlinde anlatılmıştır.\n\nTekdüzen Hesap Planı’nın 7/A "
    "seçeneğinde standart maliyet farklarının izlenmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "GÜG kapasite farkları 732 hesabında izlenir.",
    ["DİMM miktar farkları 713 hesabında izlenir.",
     "Direkt işçilik ücret farkları 722 hesabında izlenir.",
     "GÜG verimlilik farkları 733 hesabında izlenir.",
     "DİMM fiyat farkları 712 hesabında izlenir."],
    "732 hesabı GÜG bütçe farklarını izler; kapasite farkları 734 Genel Üretim Giderleri Kapasite Farkları hesabında "
    "izlenir. Diğer eşleştirmeler MSUGT 7/A’ya uygundur.")

bf = 9 / 0.9 * 30
P.sayisal(DM,
    "Bir bisküvi üreticisinde bir koli ürünün bileşiminde net 9 kg un bulunmaktadır. Üretim sürecinde brüt olarak "
    "kullanılan unun %10’u normal fire olarak kaybolmaktadır. Unun standart fiyatı 30 ₺/kg’dır.\n\nBir koli ürünün "
    "standart direkt ilk madde ve malzeme maliyeti kaç ₺’dir?",
    tl(bf), secenekler(bf, 270, 297, 330, 243),
    "Standart miktar normal fireyi içerir: brüt miktar = 9 ÷ (1 − 0,10) = 10 kg. Standart DİMM maliyeti = 10 × 30 = "
    "300 ₺.", zorluk="hard")

# ------------------------------------------------------------------ DİMM
ff, sf, fm, sm = 42, 40, 15_600, 5_000 * 3
fiyat = (ff - sf) * fm
P.sayisal(DM,
    "Bir plastik ambalaj üreticisinde bir birim ürün için standart olarak 3 kg granül kullanılması öngörülmüş, "
    "granülün standart fiyatı 40 ₺/kg olarak belirlenmiştir. Ay içinde 5.000 birim ürün üretilmiş; bunun için 15.600 "
    "kg granül kullanılmış ve kilogram başına 42 ₺ ödenmiştir. Fiyat farkı, kullanılan miktar üzerinden "
    "hesaplanmaktadır.\n\nDirekt ilk madde ve malzeme fiyat farkının tutarı kaç ₺’dir?",
    tl(fiyat), secenekler(fiyat, (ff - sf) * sm, (fm - sm) * sf, ff * fm - sf * sm, (fm - sm) * ff),
    "Fiyat farkı = (fiili fiyat − standart fiyat) × fiili miktar = (42 − 40) × 15.600 = 31.200 ₺ olumsuz. Miktar "
    "farkı ayrıca (15.600 − 15.000) × 40 = 24.000 ₺ olumsuzdur.")

ff, sf, fm, sm = 12.5, 12, 14_700, 2_500 * 6
f1, m1 = (ff - sf) * fm, (fm - sm) * sf
assert (f1, m1) == (7_350, -3_600)
P.q(DM,
    "Bir cam şişe fabrikasında bir birim ürün için standart olarak 6 kg kum karışımı kullanılması öngörülmüş, "
    "karışımın standart fiyatı 12 ₺/kg’dır. Ay içinde 2.500 birim üretilmiş; 14.700 kg karışım kullanılmış ve "
    "kilogram başına 12,50 ₺ ödenmiştir.\n\nBu bilgilere göre DİMM fiyat ve miktar farkları sırasıyla "
    "aşağıdakilerden hangisidir?",
    "7.350 ₺ olumsuz; 3.600 ₺ olumlu",
    ["7.350 ₺ olumlu; 3.600 ₺ olumsuz", "7.500 ₺ olumsuz; 3.750 ₺ olumlu", "7.350 ₺ olumsuz; 3.750 ₺ olumlu",
     "3.750 ₺ olumsuz; 3.600 ₺ olumlu"],
    "Standart miktar = 2.500 × 6 = 15.000 kg. Fiyat farkı = (12,50 − 12) × 14.700 = 7.350 ₺ olumsuz; miktar farkı = "
    "(14.700 − 15.000) × 12 = 3.600 ₺ olumlu. Toplam fark 3.750 ₺ olumsuzdur.")

fm, toplam, sf, sm = 4_920, 1_205_400, 250, 6_000 * 0.8
ff = toplam / fm
assert ff == 245
miktar = (fm - sm) * sf
P.sayisal(DM,
    "Bir ayakkabı üreticisinde bir çift ayakkabı için standart olarak 0,8 m² deri kullanılması ve deri için m² başına "
    "250 ₺ ödenmesi öngörülmüştür. Ay içinde 6.000 çift ayakkabı üretilmiş; bunun için 4.920 m² deri kullanılmış ve "
    "kullanılan derinin fiili maliyeti toplam 1.205.400 ₺ olmuştur.\n\nDirekt ilk madde ve malzeme miktar farkı kaç "
    "₺’dir?",
    tl(miktar), secenekler(miktar, (fm - sm) * ff, (sf - ff) * fm, toplam - sm * sf, miktar + (sf - ff) * fm),
    "Standart miktar = 6.000 × 0,8 = 4.800 m². Miktar farkı = (4.920 − 4.800) × 250 = 30.000 ₺ olumsuz. Fiili fiyat "
    "1.205.400 ÷ 4.920 = 245 ₺ olduğundan fiyat farkı 24.600 ₺ olumlu, toplam fark 5.400 ₺ olumsuzdur.",
    zorluk="hard")

ff, sf, alis, kull = 14.2, 14, 20_000, 18_500
fiyat = round((ff - sf) * alis, 2)
P.sayisal(DM,
    "Bir işletme DİMM fiyat farkını, malzemenin satın alındığı anda ve satın alınan miktar üzerinden ayırmakta; "
    "malzemeyi stoklara standart fiyatla almaktadır. Ay içinde standart fiyatı 14 ₺/kg olan hammaddeden 20.000 kg "
    "kilogramı 14,20 ₺’den satın alınmış, bunun 18.500 kg’ı üretimde kullanılmıştır.\n\nAy içinde ayrılacak DİMM "
    "fiyat farkı kaç ₺’dir?",
    tl(fiyat), secenekler(fiyat, round((ff - sf) * kull, 2), round((ff - sf) * (alis - kull), 2), 7_700,
                          (alis - kull) * ff),
    "Fiyat farkı satın alma anında ayrıldığında satın alınan miktar esas alınır: (14,20 − 14) × 20.000 = 4.000 ₺ "
    "olumsuz. Böylece stoktaki 1.500 kg da standart fiyatla izlenir.")

sf, fiili_birim, std_kg = 45, 2_000, 3.5
fm = 2_000 * 3.5 + 9_000 / sf
P.sayisal(DM,
    "Bir boya üreticisinde bir kutu ürün için standart olarak 3,5 kg pigment öngörülmüş, pigmentin standart fiyatı "
    "45 ₺/kg’dır. Ay içinde 2.000 kutu üretilmiş ve ay sonu raporunda DİMM miktar farkı 9.000 ₺ olumsuz olarak "
    "hesaplanmıştır.\n\nBu bilgilere göre ay içinde üretimde kullanılan pigment miktarı kaç kg’dır?",
    f"{tl(fm)} kg", [f"{tl(x)} kg" for x in (6_800, 7_000, 7_400, 7_100)],
    "Standart miktar = 2.000 × 3,5 = 7.000 kg. Olumsuz miktar farkı fazla kullanım demektir: 9.000 ÷ 45 = 200 kg. "
    "Fiili kullanım = 7.000 + 200 = 7.200 kg.")

sm, sf, fm, ff = 7_500 * 1.2, 85, 9_300, 83
yuk = sm * sf
P.sayisal(MK,
    "Bir işletmede bir birim mamul için standart olarak 1,2 kg hammadde öngörülmüş, standart fiyat 85 ₺/kg olarak "
    "belirlenmiştir. Ay içinde 7.500 birim mamul üretilmiş; 9.300 kg hammadde kilogramı 83 ₺’den kullanılmıştır. "
    "İşletme 7/A seçeneğine göre maliyetleri üretime standart tutarlarla yüklemektedir.\n\n711 Direkt İlk Madde ve "
    "Malzeme Yansıtma hesabına alacak kaydedilecek tutar kaç ₺’dir?",
    tl(yuk), secenekler(yuk, fm * sf, fm * ff, sm * ff, 7_500 * sf),
    "Standart maliyet sisteminde yarı mamullere, fiili üretim için izin verilen standart miktar ile standart fiyatın "
    "çarpımı yüklenir: 7.500 × 1,2 = 9.000 kg × 85 = 765.000 ₺. Bu tutar 151’in borcuna, 711’in alacağına yazılır.")

# ------------------------------------------------------------------ DİŞ
fs, fu, ss, su = 4_200, 185, 4_000, 180
u, z = (fu - su) * fs, (fs - ss) * su
assert (u, z) == (21_000, 36_000)
P.q(DI,
    "Bir mobilya işletmesinde ay içinde fiilen 4.200 direkt işçilik saati çalışılmış ve saat başına 185 ₺ ücret "
    "ödenmiştir. Ayın fiili üretimi için izin verilen standart süre 4.000 saat, standart saat ücreti ise 180 ₺’dir."
    "\n\nBu bilgilere göre direkt işçilik ücret ve zaman farkları sırasıyla aşağıdakilerden hangisidir?",
    "21.000 ₺ olumsuz; 36.000 ₺ olumsuz",
    ["21.000 ₺ olumlu; 36.000 ₺ olumsuz", "20.000 ₺ olumsuz; 37.000 ₺ olumsuz", "21.000 ₺ olumsuz; 37.000 ₺ olumsuz",
     "36.000 ₺ olumsuz; 21.000 ₺ olumsuz"],
    "Ücret farkı = (185 − 180) × 4.200 = 21.000 ₺ olumsuz; zaman farkı = (4.200 − 4.000) × 180 = 36.000 ₺ olumsuz. "
    "Toplam direkt işçilik farkı 57.000 ₺ olumsuzdur.")

fs, toplam, su, ss = 4_650, 767_250, 160, 3_200 * 1.5
fu = toplam / fs
assert fu == 165
z = (fs - ss) * su
P.sayisal(DI,
    "Bir elektronik montaj işletmesinde bir birim ürün için standart süre 1,5 direkt işçilik saati, standart ücret "
    "saat başına 160 ₺’dir. Ay içinde 3.200 birim ürün üretilmiş; bunun için 4.650 saat çalışılmış ve toplam 767.250 "
    "₺ direkt işçilik ücreti ödenmiştir.\n\nDirekt işçilik zaman farkının tutarı kaç ₺’dir?",
    tl(-z), secenekler(-z, (ss - fs) * fu, (fu - su) * fs, ss * su - toplam, -z + (fu - su) * fs),
    "Standart saat = 3.200 × 1,5 = 4.800 saat. Zaman farkı = (4.650 − 4.800) × 160 = 24.000 ₺ olumlu. Fiili ücret "
    "767.250 ÷ 4.650 = 165 ₺ olduğundan ücret farkı 23.250 ₺ olumsuz, toplam fark 750 ₺ olumludur.")

P.sayisal(DI,
    "Bir dokuma işletmesinde ay içinde 6.300 direkt işçilik saati çalışılmıştır. Standart saat ücreti 150 ₺’dir ve ay "
    "sonu raporunda direkt işçilik ücret farkı 18.900 ₺ olumlu olarak hesaplanmıştır. Zaman farkı ayrıca "
    "raporlanmıştır.\n\nBu işletmede ay içinde ödenen fiili saat ücreti kaç ₺’dir?",
    tl(150 - 18_900 / 6_300), secenekler(147, 153, 150, 144, 156),
    "Ücret farkı = (fiili ücret − standart ücret) × fiili saat. Olumlu fark fiili ücretin düşük olduğunu gösterir: "
    "18.900 ÷ 6.300 = 3 ₺. Fiili saat ücreti = 150 − 3 = 147 ₺.")

su, z, ss = 175, 12_250, 9_000
fs = ss - z / su
P.sayisal(DI,
    "Bir konserve fabrikasında ay içindeki fiili üretim için izin verilen standart süre 9.000 direkt işçilik saati, "
    "standart saat ücreti 175 ₺’dir. Ay sonunda direkt işçilik zaman farkı 12.250 ₺ olumlu, ücret farkı ise 4.465 ₺ "
    "olumsuz olarak raporlanmıştır.\n\nAy içinde fiilen çalışılan direkt işçilik saati kaçtır?",
    f"{tl(fs)} saat", [f"{tl(x)} saat" for x in (9_070, 8_860, 9_140, 9_000)],
    "Zaman farkı = (fiili saat − standart saat) × standart ücret. Olumlu fark daha az çalışıldığını gösterir: 12.250 ÷ "
    "175 = 70 saat. Fiili saat = 9.000 − 70 = 8.930 saattir.")

fs, toplam, ss, su = 3_100, 527_000, 1_500 * 2, 172
fu = toplam / fs
assert fu == 170
t = toplam - ss * su
P.sayisal(DI,
    "Bir kalıp üreticisinde bir birim ürün için standart süre 2 direkt işçilik saati, standart ücret saat başına 172 "
    "₺’dir. Ay içinde 1.500 birim ürün üretilmiş; 3.100 saat çalışılmış ve toplam 527.000 ₺ direkt işçilik ücreti "
    "ödenmiştir.\n\nToplam direkt işçilik farkı kaç ₺’dir?",
    tl(t), secenekler(t, (fs - ss) * su, (su - fu) * fs, (fs - ss) * fu, (fs - ss) * su + (su - fu) * fs),
    "Standart maliyet = 1.500 × 2 × 172 = 516.000 ₺. Toplam fark = 527.000 − 516.000 = 11.000 ₺ olumsuz. Bu fark "
    "17.200 ₺ olumsuz zaman farkı ile (170 − 172) × 3.100 = 6.200 ₺ olumlu ücret farkının toplamıdır.")

su, fs, z, sure = 160, 5_490, 14_400, 1.8
ss = fs - z / su
uretim = ss / sure
assert uretim == 3_000
P.sayisal(DI,
    "Bir hazır giyim işletmesinde bir birim ürün için standart süre 1,8 direkt işçilik saati, standart ücret saat "
    "başına 160 ₺’dir. Ay içinde 5.490 saat çalışılmış ve direkt işçilik zaman farkı 14.400 ₺ olumsuz olarak "
    "hesaplanmıştır.\n\nBu işletmenin ay içindeki fiili üretim miktarı kaç birimdir?",
    f"{tl(uretim)} birim", [f"{tl(x)} birim" for x in (3_100, 3_050, 2_900, 2_950)],
    "Olumsuz zaman farkı fazla çalışmayı gösterir: 14.400 ÷ 160 = 90 saat. Standart saat = 5.490 − 90 = 5.400 saat; "
    "fiili üretim = 5.400 ÷ 1,8 = 3.000 birimdir.", zorluk="hard")

net, pay, ucret = 48, 0.20, 180
std = net / (1 - pay) / 60 * ucret
P.sayisal(DI,
    "Bir işletmede zaman etüdü sonucunda bir birim ürünün net işlem süresi 48 dakika olarak ölçülmüştür. Dinlenme, "
    "kişisel ihtiyaç ve makine hazırlık payının standart sürenin %20’si olması öngörülmektedir. Standart saat ücreti "
    "180 ₺’dir.\n\nBir birim ürünün standart direkt işçilik maliyeti kaç ₺’dir?",
    tl(std), secenekler(std, 48 / 60 * 1.2 * ucret, 48 / 60 * ucret, 1.2 * ucret, ucret / 0.8),
    "Paylar standart sürenin %20’si olduğundan net süre standart sürenin %80’idir: 48 ÷ 0,80 = 60 dakika = 1 saat. "
    "Standart DİŞ maliyeti = 1 × 180 = 180 ₺.", zorluk="hard")

# ------------------------------------------------------------------ GÜG
oran = 300_000 / 10_000 + 18
P.sayisal(GG,
    "Bir işletme genel üretim giderlerini direkt işçilik saati (DİS) esasına göre yüklemektedir. Normal kapasite aylık "
    "10.000 DİS’tir; bu kapasitede bütçelenen sabit GÜG 300.000 ₺, değişken GÜG ise DİS başına 18 ₺’dir. Ay içinde "
    "fiilen 9.400 DİS çalışılmıştır.\n\nDİS başına standart GÜG yükleme oranı kaç ₺’dir?",
    tl(oran), secenekler(oran, 30, 18, 300_000 / 9_400 + 18, 66),
    "Standart GÜG oranı normal kapasiteye göre hesaplanır: sabit oran 300.000 ÷ 10.000 = 30 ₺, değişken oran 18 ₺; "
    "toplam 48 ₺/DİS. Fiili saat oran hesabında kullanılmaz.", zorluk="easy")

o, b, k, v, t = guc(8_000, 240_000, 20, 7_600, 7_400, 395_000)
assert (o, b, k, v, t) == (50, 3_000, 12_000, 10_000, 25_000)
P.sayisal(GG,
    "Bir işletmede normal kapasite 8.000 DİS, bu kapasitede sabit GÜG bütçesi 240.000 ₺ ve değişken GÜG oranı DİS "
    "başına 20 ₺’dir. Ay içinde fiili üretim için izin verilen standart süre 7.400 DİS olmuş, fiilen 7.600 DİS "
    "çalışılmış ve 395.000 ₺ genel üretim gideri gerçekleşmiştir.\n\nToplam GÜG farkı kaç ₺’dir?",
    tl(t), secenekler(t, 395_000 - 7_600 * o, k, v, b),
    "Standart oran = 240.000 ÷ 8.000 + 20 = 50 ₺. Yüklenen GÜG = 7.400 × 50 = 370.000 ₺. Toplam fark = 395.000 − "
    "370.000 = 25.000 ₺ olumsuz (bütçe 3.000 + kapasite 12.000 + verimlilik 10.000).")

o, b, k, v, t = guc(12_000, 480_000, 15, 11_500, 11_200, 660_000)
assert (b, k, v) == (7_500, 20_000, 16_500)
P.sayisal(GG,
    "Bir döküm işletmesi GÜG’ü makine saati esasına göre yüklemektedir. Normal kapasite 12.000 makine saati, sabit "
    "GÜG bütçesi 480.000 ₺ ve değişken GÜG oranı makine saati başına 15 ₺’dir. Ay içinde fiili üretim için standart "
    "süre 11.200 saat olmuş, fiilen 11.500 saat çalışılmış ve 660.000 ₺ GÜG gerçekleşmiştir.\n\nÜçlü analize göre "
    "GÜG bütçe farkı kaç ₺’dir?",
    tl(b), secenekler(b, 660_000 - (480_000 + 15 * 11_200), t, 660_000 - 11_500 * o, k),
    "Fiili saate göre esnek bütçe = 480.000 + 15 × 11.500 = 652.500 ₺. Bütçe farkı = 660.000 − 652.500 = 7.500 ₺ "
    "olumsuz. Kapasite farkı 20.000 ₺, verimlilik farkı 16.500 ₺ olumsuzdur.", zorluk="hard")

o, b, k, v, t = guc(20_000, 700_000, 25, 21_000, 20_400, 1_230_000)
assert (b, k, v, t) == (5_000, -35_000, 36_000, 6_000)
P.q(GG,
    "Bir işletmede normal kapasite 20.000 DİS, bu kapasitede sabit GÜG bütçesi 700.000 ₺ ve değişken GÜG oranı DİS "
    "başına 25 ₺’dir. Yoğun sipariş nedeniyle ay içinde fiilen 21.000 DİS çalışılmış; fiili üretim için standart süre "
    "20.400 DİS, fiili GÜG 1.230.000 ₺ olmuştur.\n\nÜçlü analize göre GÜG kapasite farkı aşağıdakilerden "
    "hangisidir?",
    "35.000 ₺ olumlu",
    ["35.000 ₺ olumsuz", "14.000 ₺ olumlu", "36.000 ₺ olumsuz", "60.000 ₺ olumlu"],
    "Sabit oran = 700.000 ÷ 20.000 = 35 ₺. Fiili saat normal kapasiteyi 1.000 saat aştığından sabit gider fazla "
    "yüklenmiştir: kapasite farkı = 35 × 1.000 = 35.000 ₺ olumlu. Verimlilik farkı 36.000 ₺ olumsuz, bütçe farkı "
    "5.000 ₺ olumsuzdur.", zorluk="hard")

o, b, k, v, t = guc(5_000, 160_000, 40, 4_850, 4_600, 355_000)
assert (o, v) == (72, 18_000)
P.sayisal(GG,
    "Bir işletmede bir birim ürün için standart süre 2 makine saatidir. Normal kapasite 5.000 makine saati; standart "
    "GÜG oranı makine saati başına 72 ₺’dir (sabit 32 ₺, değişken 40 ₺). Ay içinde 2.300 birim ürün üretilmiş, 4.850 "
    "makine saati çalışılmış ve 355.000 ₺ GÜG gerçekleşmiştir.\n\nGÜG verimlilik farkı kaç ₺’dir?",
    tl(v), secenekler(v, 250 * 40, 250 * 32, (5_000 - 4_600) * 72, t),
    "Standart saat = 2.300 × 2 = 4.600. Verimlilik farkı = (4.850 − 4.600) × 72 = 18.000 ₺ olumsuz. Toplam fark "
    "23.800 ₺ olup 1.000 ₺ bütçe ve 4.800 ₺ kapasite farkını da içerir.")

o, b, k, v, t = guc(6_000, 180_000, 12, 5_900, 5_700, 255_000)
assert (b, k, v, t) == (4_200, 3_000, 8_400, 15_600)
P.q(GG,
    "Bir işletmede normal kapasite 6.000 DİS, sabit GÜG bütçesi 180.000 ₺ ve değişken GÜG oranı DİS başına 12 ₺’dir. "
    "Ay içinde fiili üretim için standart süre 5.700 DİS olmuş, fiilen 5.900 DİS çalışılmış ve 255.000 ₺ GÜG "
    "gerçekleşmiştir. Farkların tamamı olumsuzdur.\n\nÜçlü analize göre bütçe, kapasite ve verimlilik farkları "
    "sırasıyla kaç ₺’dir?",
    "4.200; 3.000; 8.400",
    ["4.200; 8.400; 3.000", "6.600; 3.000; 6.000", "4.200; 3.000; 2.400", "3.000; 4.200; 8.400"],
    "Standart oran = 30 + 12 = 42 ₺. Bütçe farkı = 255.000 − (180.000 + 12 × 5.900) = 4.200 ₺; kapasite farkı = 30 × "
    "(6.000 − 5.900) = 3.000 ₺; verimlilik farkı = (5.900 − 5.700) × 42 = 8.400 ₺. Toplam 15.600 ₺ = 255.000 − "
    "5.700 × 42.", zorluk="hard")

yuk = 9_000 * 0.5 * 45
P.sayisal(GG,
    "Bir işletmede standart GÜG oranı DİS başına 45 ₺’dir (sabit 25 ₺, değişken 20 ₺); normal kapasite 5.000 DİS’tir. "
    "Bir birim ürün için standart süre 0,5 DİS’tir. Ay içinde 9.000 birim ürün üretilmiş ve fiilen 4.700 DİS "
    "çalışılmıştır.\n\nStandart maliyet sistemine göre ay içinde mamullere yüklenecek GÜG kaç ₺’dir?",
    tl(yuk), secenekler(yuk, 4_700 * 45, 5_000 * 45, 4_500 * 25, 4_500 * 20),
    "Standart sistemde GÜG, fiili üretim için izin verilen standart saat üzerinden yüklenir: 9.000 × 0,5 = 4.500 DİS "
    "× 45 = 202.500 ₺. Fiili saat (4.700) ve normal kapasite (5.000) yükleme tabanı değildir.")

o = 150_000 + 22 * 3_800 - 6_000
P.sayisal(GG,
    "Bir işletmede sabit GÜG bütçesi aylık 150.000 ₺, değişken GÜG oranı DİS başına 22 ₺’dir. Ay içinde fiilen 3.800 "
    "DİS çalışılmış ve üçlü analizde GÜG bütçe farkı 6.000 ₺ olumlu olarak hesaplanmıştır.\n\nAy içinde gerçekleşen "
    "genel üretim gideri kaç ₺’dir?",
    tl(o), secenekler(o, o + 12_000, o + 6_000, o - 6_000, 150_000 + 22 * 4_000),
    "Fiili saate göre esnek bütçe = 150.000 + 22 × 3.800 = 233.600 ₺. Olumlu bütçe farkı fiili giderin bütçenin "
    "altında kaldığını gösterir: 233.600 − 6.000 = 227.600 ₺.")

o = 270_000 / 9_000 + 16
butce_ss = 270_000 + 16 * 8_500
hacim = butce_ss - 8_500 * o
assert (412_000 - butce_ss, hacim) == (6_000, 15_000)
P.sayisal(GG,
    "Bir işletme GÜG farklarını ikili analizle incelemektedir: bütçe (kontrol edilebilir) farkı fiili GÜG ile standart "
    "saate göre esnek bütçe arasındaki fark, hacim farkı ise esnek bütçe ile yüklenen GÜG arasındaki farktır. Normal "
    "kapasite 9.000 DİS, sabit GÜG 270.000 ₺, değişken oran 16 ₺/DİS’tir. Fiili üretim için standart süre 8.500 DİS, "
    "fiili GÜG 412.000 ₺’dir.\n\nHacim farkı kaç ₺’dir?",
    tl(hacim), secenekler(hacim, 6_000, 21_000, 8_000, 30_000),
    "Standart oran = 30 + 16 = 46 ₺. Standart saate göre esnek bütçe = 270.000 + 16 × 8.500 = 406.000 ₺; yüklenen "
    "GÜG = 8.500 × 46 = 391.000 ₺. Hacim farkı = 406.000 − 391.000 = 15.000 ₺ olumsuz (= 30 × 500 atıl saat).",
    zorluk="hard")

P.q(GG,
    "Bir işletmede değişken GÜG için 412.000 ₺ yüklenmiş, 398.500 ₺ gerçekleşmiştir. Sabit GÜG için ise 360.000 ₺ "
    "yüklenmiş, 371.200 ₺ gerçekleşmiştir.\n\nBu bilgilere göre toplam GÜG farkının tutarı ve niteliği "
    "aşağıdakilerden hangisidir?",
    "2.300 ₺ fazla yükleme (olumlu)",
    ["2.300 ₺ eksik yükleme (olumsuz)", "24.700 ₺ fazla yükleme (olumlu)", "13.500 ₺ fazla yükleme (olumlu)",
     "11.200 ₺ eksik yükleme (olumsuz)"],
    "Değişken GÜG’de 412.000 − 398.500 = 13.500 ₺ fazla, sabit GÜG’de 371.200 − 360.000 = 11.200 ₺ eksik yükleme "
    "vardır. Toplamda yüklenen 772.000 ₺, gerçekleşen 769.700 ₺ olduğundan 2.300 ₺ fazla yükleme (olumlu fark) "
    "oluşur.")

P.q(GG,
    "Genel üretim giderlerini direkt işçilik saatine göre yükleyen bir işletmede ay sonu raporu, direkt işçilik zaman "
    "farkının önemli tutarda olumsuz çıktığını göstermektedir. Gider kalemlerinin fiyatlarında ve normal kapasitede "
    "değişiklik olmamıştır.\n\nBu durum GÜG farklarından hangisini aynı yönde etkiler?",
    "Verimlilik farkı olumsuz çıkar.",
    ["Kapasite farkı olumsuz çıkar.", "Bütçe farkı olumlu çıkar.", "Verimlilik farkı olumlu çıkar.",
     "Bütçe farkı olumsuz çıkar."],
    "GÜG direkt işçilik saatine göre yüklendiğinde standarttan fazla çalışılan her saat hem direkt işçilik zaman "
    "farkını hem de GÜG verimlilik farkını olumsuz yönde etkiler; iki fark aynı saat farkından doğar.")

P.q(GG,
    "Bir işletmede ay sonunda GÜG bütçe farkının önemli tutarda olumsuz çıktığı görülmüştür. Fiili çalışma saati "
    "hem normal kapasiteye hem de fiili üretim için izin verilen standart saate eşit gerçekleşmiştir.\n\nBu farkın "
    "nedeni aşağıdakilerden hangisi olabilir?",
    "Endirekt malzeme ve enerji harcamalarının bütçeyi aşması",
    ["Fiili çalışma saatinin normal kapasitenin altında kalması",
     "İşçilerin standart süreden uzun çalışması",
     "Hammadde alış fiyatının standarttan yüksek olması",
     "Birim başına standarttan fazla hammadde kullanılması"],
    "Bütçe farkı, fiili GÜG’ün fiili saate göre bütçelenen tutardan sapmasıdır ve gider kalemlerindeki fazla "
    "harcamadan doğar. Saatler normal ve standart düzeyde olduğundan kapasite ve verimlilik farkı yoktur; hammadde "
    "farkları DİMM’e aittir.")

P.q(GG,
    "Bir işletmede siparişlerin düşmesi nedeniyle fabrika üç ay boyunca normal kapasitenin %70’inde çalışmış ve her ay "
    "önemli tutarda olumsuz kapasite farkı oluşmuştur. Üretim bölümü, siparişe göre üretim yaptığını ve verimlilikte "
    "bir sorun bulunmadığını raporlamıştır.\n\nBu fark için öncelikle hangi birim sorumlu tutulmalıdır?",
    "Satış ve üst yönetim",
    ["Satın alma birimi", "Üretim bölümü ustabaşıları", "İnsan kaynakları birimi", "Kalite kontrol birimi"],
    "Talep düşüşünden doğan atıl kapasite, üretim bölümünün kontrolü dışındadır; kapasite farkı genellikle satış "
    "hacmini ve kapasite kararlarını yöneten satış birimi ile üst yönetimin sorumluluğundadır.")

# ------------------------------------------------------------------ kayıt ve dağıtım
ss = 60 + 300 + 200
P.sayisal(R,
    "Bir işletmenin bir birim mamul için hazırladığı standart maliyet kartında şu bilgiler yer almaktadır: DİMM 3 kg, "
    "kilogramı 20 ₺; DİŞ 2 saat, saati 150 ₺; GÜG direkt işçilik saatine göre, değişken oran 40 ₺/saat ve normal "
    "kapasiteye göre sabit oran 60 ₺/saat.\n\nBir birim mamulün standart maliyeti kaç ₺’dir?",
    tl(ss), secenekler(ss, 60 + 300 + 80, 60 + 300, 60 + 300 + 100, 660),
    "DİMM = 3 × 20 = 60 ₺; DİŞ = 2 × 150 = 300 ₺; GÜG = 2 × (40 + 60) = 200 ₺. Standart birim maliyet = 60 + 300 + "
    "200 = 560 ₺.", zorluk="easy")

fark, ym, mm, smm = 48_000, 120_000, 280_000, 800_000
pay = fark * smm / (ym + mm + smm)
P.sayisal(MK,
    "Bir işletmede dönem sonunda fark hesaplarında toplam 48.000 ₺ olumsuz fark birikmiştir ve fark önemli "
    "bulunmuştur. Standart maliyetle değerlenmiş tutarlar yarı mamul 120.000 ₺, mamul 280.000 ₺ ve satılan mamuller "
    "maliyeti 800.000 ₺’dir. Farklar bu tutarlar oranında dağıtılmaktadır.\n\n620 Satılan Mamuller Maliyeti "
    "hesabına aktarılacak fark kaç ₺’dir?",
    tl(pay), secenekler(pay, fark * mm / 1_200_000, fark * ym / 1_200_000, fark, fark / 3),
    "Toplam standart tutar 1.200.000 ₺’dir. SMM payı = 48.000 × 800.000 ÷ 1.200.000 = 32.000 ₺. Mamule 11.200 ₺, "
    "yarı mamule 4.800 ₺ düşer.")

stok = 1_500 * 560 + 42_000 * 1_500 / 6_000
P.sayisal(MK,
    "Standart birim maliyeti 560 ₺ olan bir mamulden dönem içinde 6.000 birim üretilmiş, 4.500 birim satılmıştır; "
    "dönem başı stok ve yarı mamul yoktur. Dönem sonunda 42.000 ₺ olumsuz fark önemli bulunmuş ve mamul stoku ile "
    "satılan mamuller arasında birim sayısına göre dağıtılmıştır.\n\nBilançoda mamul stoku kaç ₺ tutarla yer "
    "alır?",
    tl(stok), secenekler(stok, 1_500 * 560, 1_500 * 560 - 10_500, 1_500 * 560 + 42_000, 1_500 * 560 + 31_500),
    "Mamul stoku standart maliyetle 1.500 × 560 = 840.000 ₺’dir. Fark payı = 42.000 × 1.500 ÷ 6.000 = 10.500 ₺ "
    "olumsuz olduğundan stok 840.000 + 10.500 = 850.500 ₺ ile raporlanır.")

P.q(MK,
    "7/A seçeneğini ve standart maliyet sistemini uygulayan bir işletmede ay içinde 12.400 kg hammadde kilogramı 26 "
    "₺’den kullanılmış ve 710 hesabına 322.400 ₺ fiili gider kaydedilmiştir. Fiili üretim için standart miktar "
    "12.000 kg, standart fiyat 25 ₺/kg’dır; fiyat farkı 12.400 ₺, miktar farkı 10.000 ₺ olumsuzdur.\n\n710 hesabının "
    "ay sonunda yansıtma ve fark hesaplarıyla kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(711, 300_000), (712, 12_400), (713, 10_000)], [(710, 322_400)]),
    [K([(711, 300_000)], [(712, 12_400), (713, 10_000), (710, 277_600)]),
     K([(710, 322_400)], [(711, 300_000), (712, 12_400), (713, 10_000)]),
     K([(711, 300_000), (712, 10_000), (713, 12_400)], [(710, 322_400)]),
     K([(711, 322_400)], [(710, 322_400)])],
    "710 hesabı fiili tutarla (322.400 ₺) alacaklandırılarak kapatılır. Standart tutar 12.000 × 25 = 300.000 ₺ 711’in "
    "borcuna; olumsuz fiyat farkı (26 − 25) × 12.400 = 12.400 ₺ 712’nin, olumsuz miktar farkı 400 × 25 = 10.000 ₺ "
    "713’ün borcuna yazılır.", zorluk="hard")

fs, fu, ss, su = 2_050, 195, 2_000, 200
u, z = (fu - su) * fs, (fs - ss) * su
assert (u, z) == (-10_250, 10_000)
P.q(MK,
    "7/A seçeneğini uygulayan bir işletmede ay içinde 2.050 direkt işçilik saati saat başına 195 ₺’den çalışılmış ve "
    "720 hesabına 399.750 ₺ kaydedilmiştir. Fiili üretim için standart süre 2.000 saat, standart ücret 200 ₺’dir."
    "\n\n720 hesabının ay sonunda yansıtma ve fark hesaplarıyla kapatılmasına ilişkin kayıt aşağıdakilerden "
    "hangisidir?",
    K([(721, 400_000), (723, 10_000)], [(722, 10_250), (720, 399_750)]),
    [K([(721, 400_000), (722, 10_250)], [(723, 10_000), (720, 400_250)]),
     K([(720, 399_750), (722, 10_250)], [(721, 400_000), (723, 10_000)]),
     K([(721, 399_750), (723, 10_250)], [(722, 10_000), (720, 400_000)]),
     K([(721, 410_000)], [(722, 10_250), (720, 399_750)])],
    "Standart tutar 2.000 × 200 = 400.000 ₺ 721’in borcuna yazılır. Ücret farkı (195 − 200) × 2.050 = 10.250 ₺ olumlu "
    "olduğundan 722’nin alacağına, zaman farkı (2.050 − 2.000) × 200 = 10.000 ₺ olumsuz olduğundan 723’ün borcuna "
    "kaydedilir; 720 fiili tutarla kapatılır.", zorluk="hard")

P.q(MK,
    "7/A seçeneğini ve standart maliyet sistemini uygulayan bir işletmede ay içinde üretimde kullanılan hammaddenin "
    "fiili maliyeti 1.000.000 ₺’dir; fiili üretim için standart miktar ve fiyata göre hesaplanan tutar ise 960.000 "
    "₺’dir.\n\nHammaddenin yarı mamullere yüklenmesine ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(151, 960_000)], [(711, 960_000)]),
    [K([(151, 1_000_000)], [(711, 1_000_000)]),
     K([(151, 960_000)], [(710, 960_000)]),
     K([(710, 1_000_000)], [(150, 1_000_000)]),
     K([(151, 1_000_000)], [(711, 960_000), (713, 40_000)])],
    "Standart maliyet sisteminde yarı mamullere standart tutar yüklenir: 151 borç, 711 alacak 960.000 ₺. Fiili "
    "maliyet 710’da izlenir; 40.000 ₺’lik fark dönem sonunda 710’un kapatılmasıyla 712-713 hesaplarına ayrılır.")

P.q(MK,
    "Standart maliyet sistemini uygulayan ve GÜG farklarını bütçe, verimlilik ve kapasite farkı olarak üçlü analizle "
    "izleyen bir işletme, MSUGT’deki 7/A seçeneğine göre hesap açmaktadır. İşletme DİMM ve DİŞ farklarını da ayrı "
    "hesaplarda izlemektedir.\n\nGÜG farkları için kullanılacak hesaplar aşağıdakilerden hangisidir?",
    "732, 733 ve 734",
    ["712, 722 ve 732", "731, 732 ve 733", "722, 723 ve 733", "730, 731 ve 732"],
    "MSUGT 7/A’da GÜG farkları 732 Bütçe Farkları, 733 Verimlilik Farkları ve 734 Kapasite Farkları hesaplarında "
    "izlenir; 712-713 DİMM, 722-723 DİŞ farklarına aittir, 730-731 ise gider ve yansıtma hesaplarıdır.",
    zorluk="easy")

P.oncul(MK,
    "Tekdüzen Hesap Planı’nın 7/A seçeneğinde standart maliyet hesaplarının işleyişine ilişkin aşağıdaki ifadeler "
    "verilmiştir:",
    ["711 hesabı, üretime yüklenen standart tutarla alacaklandırılır.",
     "713 hesabında olumlu miktar farkları hesabın borcuna kaydedilir.",
     "734 hesabı genel üretim giderlerinin kapasite farklarını izler.",
     "Fark hesapları dönem sonunda ilgili hesaplara aktarılarak kapatılır."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve III", "II ve IV", "I, II ve III", "I, III ve IV", "II, III ve IV"],
    "I, III ve IV doğrudur. II yanlıştır: fark hesaplarında olumsuz farklar borca, olumlu farklar alacağa "
    "kaydedilir.")

# ------------------------------------------------------------------ nedenler ve belirleme
P.q(DI,
    "Bir işletmede ay sonunda direkt işçilikte önemli tutarda olumsuz ücret farkı çıkmıştır. Aynı ay içinde çalışılan "
    "toplam saat, fiili üretim için izin verilen standart saate eşittir.\n\nAşağıdakilerden hangisi bu ücret farkının "
    "nedeni olabilir?",
    "Planlanmayan fazla mesai için zamlı ücret ödenmesi",
    ["Makine arızası nedeniyle işçilerin boş beklemesi",
     "Düşük kaliteli malzeme nedeniyle ürünlerin yeniden işlenmesi",
     "Üretim planlamasındaki aksaklıklar nedeniyle iş akışının durması",
     "Hammadde tedarikçisinin fiyatları artırması"],
    "Ücret farkı saat ücretinin standarttan sapmasından doğar; fazla mesai zammı saat ücretini yükseltir. Bekleme, "
    "yeniden işleme ve iş akışı aksaklığı zaman farkına; hammadde fiyatı ise DİMM fiyat farkına yol açar.")

P.q(DM,
    "Bir işletmenin üretim müdürü, ay sonunda çıkan önemli DİMM miktar farkının nedenlerini araştırmaktadır. Aynı "
    "dönemde satın alma fiyatlarında, makine parkında ve işçi kadrosunda çeşitli değişiklikler olmuştur.\n\n"
    "Aşağıdakilerden hangisi DİMM miktar farkının nedenlerinden biri değildir?",
    "Tedarikçinin satış fiyatını artırması",
    ["Makine ayarlarının bozulmasıyla fire oranının artması",
     "Deneyimsiz işçilerin malzemeyi israf etmesi",
     "Düşük kaliteli malzeme kullanılması",
     "Hatalı ürünlerin yeniden işlenmesi"],
    "Miktar farkı, kullanılan malzeme miktarının standarttan sapmasıdır; fire, israf, düşük kalite ve yeniden işleme "
    "tüketimi artırır. Fiyat artışı ise miktarı değil birim fiyatı etkilediğinden fiyat farkı doğurur.",
    zorluk="easy")

P.q(R,
    "Bir işletme standart maliyet sistemine geçmek için malzeme, işçilik ve genel üretim gideri standartlarını "
    "belirleyecek bir çalışma grubu kurmuştur. Grup, raporunda standartların nasıl saptanacağına ilişkin ilkeleri "
    "sıralamıştır.\n\nStandartların belirlenmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "DİMM standart miktarına fire payı katılmaz, net miktar esas alınır.",
    ["Standart süreye normal dinlenme ve makine hazırlık payları eklenir.",
     "Standart fiyat beklenen piyasa koşulları ve alış giderleri dikkate alınarak belirlenir.",
     "Standart GÜG oranı normal kapasite esas alınarak hesaplanır.",
     "Standartların belirlenmesinde mühendislik ve iş etüdü çalışmalarından yararlanılır."],
    "Standart miktar, üretim sürecinde kaçınılmaz olan normal fire payını da içerir; aksi hâlde her dönem olumsuz "
    "miktar farkı çıkar. Diğer ifadeler standart belirlemenin genel kabul görmüş ilkeleridir.")

P.q(R,
    "Bir işletme her ay yüzlerce kalemde standart maliyet farkı hesaplamaktadır. Yönetim, farkların tamamını değil, "
    "yalnızca standart tutarın %5’ini aşan ya da art arda üç ay aynı yönde gerçekleşen farkları "
    "araştırmaktadır.\n\nBu uygulamanın dayandığı gerekçe aşağıdakilerden hangisidir?",
    "Küçük farkları araştırmanın maliyeti, sağlayacağı yarardan fazladır.",
    ["Küçük farklar dönem sonunda stoklara aktarılmaz, bu nedenle önemsizdir.",
     "TMS 2 standart tutarın %5’ini aşmayan farkların araştırılmasını yasaklar.",
     "Olumlu farklar dönem kârını artırdığından araştırmaya gerek duyulmaz.",
     "Küçük farklar kapasite farkından doğduğundan üst yönetimin sorumluluğundadır."],
    "Fark araştırması zaman ve kaynak gerektirir; önemsiz ve rastlantısal farkları incelemenin maliyeti yararını "
    "aşar. Önemlilik sınırı ve süreklilik ölçütü, dikkatin kontrol edilebilir ve kalıcı sapmalara yöneltilmesini "
    "sağlar.")

P.q(R,
    "Bir işletme hem siparişe göre özel makine üretmekte hem de seri üretimle yedek parça imal etmektedir. Yönetim, "
    "iki üretim hattında da maliyet kontrolünü güçlendirmek için standart maliyet sistemine geçmeyi "
    "düşünmektedir.\n\nStandart maliyet sistemiyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Sipariş ve safha maliyet yöntemleriyle birlikte uygulanabilir.",
    ["Safha maliyet yöntemini uygulayan işletmelerde kullanılamaz.",
     "Fiili maliyet kayıtlarını ortadan kaldırarak kayıt tutmayı sona erdirir.",
     "Farklar hesaplanmadan stoklar gerçek maliyetle raporlanır.",
     "Genel üretim giderlerini kapsamaz, direkt giderlerle sınırlıdır."],
    "Standart maliyet bir maliyet hesaplama yöntemi değil, maliyet kontrol sistemidir; sipariş ve safha maliyet "
    "yöntemleriyle birlikte uygulanabilir. Fiili maliyetler yine kaydedilir ve standartla karşılaştırılır.")

P.q(R,
    "Bir işletmede her mamul için gereken malzeme miktarı ve fiyatı, işçilik süresi ve ücreti ile genel üretim gideri "
    "oranı tek bir belgede gösterilmekte; bu belge hem üretime maliyet yüklemede hem de fark analizinde "
    "kullanılmaktadır.\n\nBu belge aşağıdakilerden hangisidir?",
    "Standart maliyet kartı",
    ["Malzeme istek fişi", "İşçilik zaman kartı", "Sipariş maliyet kartı", "Gider dağıtım tablosu"],
    "Bir birim mamulün standart miktar, fiyat, süre, ücret ve GÜG oranlarını bir arada gösteren belge standart "
    "maliyet kartıdır. İstek fişi malzeme çıkışını, zaman kartı çalışılan süreyi, sipariş maliyet kartı ise bir "
    "siparişin fiili maliyetini izler.", zorluk="easy")

P.serpistir()

if __name__ == "__main__":
    sys.exit(P.yaz())
