# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarının ağırlığını izler: KGK Bağımsız Denetim Yönetmeliği ~10, Etik Kurallar ve
KYS ~2, BDS'ler ~8 (temeller, risk, kanıt, hile, önemlilik/örnekleme, rapor). Konu havuzundaki kökler tekrar
edilmez; aynı hüküm farklı görevle ölçülür. Dayanaklar konu builder'larıyla aynıdır (build_yk_*.py başlıklarına bkz.);
28.09.2026 kontrolü.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

SURUM = ("KGK Bağımsız Denetim Yönetmeliği (15.6.2024 değişiklikleri dahil); Etik Kurallar (11.08.2025); KYS 1-2; "
         "BDS 200-720 güncel metinleri; 28.09.2026 kontrolü")

def paket(dosya, seed, ek=()):
    return Paket(dosya, lesson="denetim", topic="bagimsiz_denetim_yonetmeligi",
                 konu_adi="Muhasebe Denetimi", seed=seed, surum=SURUM, havuz="bolum", ek_idler=ek)

B = "KGK Bağımsız Denetim Yönetmeliği’ne göre"
E = "Bağımsız Denetçiler İçin Etik Kurallar (Bağımsızlık Standartları Dâhil)’a göre"
TDS = "Türkiye Denetim Standartları’na göre"
BDY, ETK, TML, RSK, KNT, HIL, ONM, RPR = ("bagimsiz_denetim_yonetmeligi", "bagimsizlik_ve_etik", "denetim_temelleri",
                                          "risk_degerlendirme", "denetim_kaniti", "hile", "onemlilik_ve_ornekleme",
                                          "denetci_raporu")

# =============================================================================== TEST 1
T1 = paket("questions_muhasebe_denetimi_2026.json", 2026092851, ["demo-denetim-021", "demo-denetim-022"])

T1.q("BDY m. 4/1-c",
    "“Belirli bir bağımsız denetim görevini yerine getirmek üzere, sorumlu denetçi ve onun sorumluluğu altında görev yapan "
    "bağımsız denetçiler ile denetim prosedürlerini uygulayan diğer kişilerden oluşan ekip”\n\n"
    f"{B} yukarıdaki tanım aşağıdakilerden hangisine aittir?",
    "Bağımsız denetim ekibi",
    ["Denetim ağı", "Denetim kuruluşunun yönetim organı", "Kalite yönetim ekibi", "İlişkili denetim kuruluşu"],
    "Yönetmelik m. 4/1-c'ye göre bağımsız denetim ekibi, belirli bir denetim görevini yerine getirmek üzere sorumlu denetçi "
    "ve onun sorumluluğu altındaki bağımsız denetçiler ile denetim prosedürlerini uygulayan diğer kişilerden oluşur.",
    topic=BDY, zorluk="easy")

T1.q("BDY m. 6/2",
    f"{B}, aşağıdakilerden hangisi Yönetmelik kapsamındaki denetimin konusu arasında sayılmaz?",
    "Mükellefin vergi beyannamelerinin 3568 sayılı Kanun uyarınca tasdiki",
    ["TTK hükümlerine göre denetlenmesi öngörülen finansal tablolar",
     "Yıllık faaliyet raporları",
     "Riskin erken saptanması ve yönetimine ilişkin sistemler",
     "Sair mevzuat uyarınca veya ihtiyari olarak denetlenmesi öngörülen diğer hususlar"],
    "Yönetmelik m. 6/2'ye göre denetim; TTK'ya göre denetlenmesi öngörülen finansal tablolar, yıllık faaliyet raporları, "
    "riskin erken saptanması ve yönetimine ilişkin sistemler ile sair mevzuat uyarınca veya ihtiyari olarak denetlenmesi "
    "öngörülen hususları kapsar. Beyanname tasdiki 3568 sayılı Kanun kapsamındaki ayrı bir hizmettir.", topic=BDY)

T1.q("BDY m. 14/2",
    f"{B}, denetçi olmak isteyen meslek mensubuna tescil işleminden sonra verilenler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Sigorta poliçesi",
    ["Bağımsız Denetçi Belgesi", "Denetçi kimliği", "Denetçi mührü", "Sicil numarası"],
    "Yönetmelik m. 14/2'ye göre tescil işleminden sonra bağımsız denetçiye Bağımsız Denetçi Belgesi, denetçi kimliği ve "
    "denetçi mührü verilir; m. 17/2'ye göre ayrıca bir sicil numarası verilir. Sigorta m. 33'e göre denetim üstlenenlerce "
    "yaptırılır.", topic=BDY, zorluk="easy")

T1.q("BDY m. 22/2",
    "Bir denetçi, denetlediği şirketin yatırım komitesine “gözlemci üye” sıfatıyla katılmakta ve önemli yatırım "
    f"kararlarında oy kullanmaktadır. {B} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Karar alma mekanizmalarına katılım yasak olduğundan bu durum aykırıdır.",
    ["Komite yönetim kurulundan ayrı olduğu için katılım bağımsızlığı etkilemez.",
     "Denetçi oy kullanmayıp sadece görüş bildirirse katılım uygundur.",
     "Katılım, denetim sözleşmesinde açıkça belirtilmişse Yönetmeliğe uygundur.",
     "Katılım, üst yönetimden sorumlu olanlar onay verdiği sürece Yönetmeliğe uygundur."],
    "Yönetmelik m. 22/2'ye göre denetim kuruluşları ve denetçiler denetlenen kuruluştan bağımsız ve tarafsız olmak zorunda "
    "olup denetlenen kuruluşların karar alma mekanizmalarına katılamazlar.", topic=BDY)

T1.q("BDY m. 26/1-c, e",
    f"{B}, denetim faaliyetine ilişkin kısıtlamalarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kadro yetersizliği, ücret artırılırsa üstlenmeye engel olmaz.",
    ["Kadronun sayı, nitelik veya tecrübe bakımından yetersiz olduğu denetimler üstlenilemez.",
     "Mevcut iş yükü nedeniyle sağlıklı yürütülemeyecek denetimler üstlenilemez.",
     "Sözleşme kabul süreçlerine ilişkin Kurum düzenlemelerine aykırı denetimler üstlenilemez.",
     "Bağımsızlığı zedeleyecek denetimler üstlenilemez."],
    "Yönetmelik m. 26/1'e göre TTK uyarınca üstlenilemeyecek, bağımsızlığı zedeleyecek, kadronun yetersiz olduğu, "
    "rotasyon süresine takılan, kabul süreçlerine aykırı ve iş yükü nedeniyle sağlıklı yürütülemeyecek denetimler "
    "üstlenilemez. Ücret artışı kadro yetersizliğini gidermez.", topic=BDY)

T1.q("BDY m. 29/1-f, 29/2",
    f"{B}, denetim sözleşmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ücretin ödenmesi, işletmeye verilecek muhasebe hizmetine bağlanabilir.",
    ["Sözleşme denetimi üstlenen ile denetlenen işletme arasında yazılı olarak düzenlenir.",
     "Sözleşmede yedekler dahil ekip üyelerinin isim ve unvanları ile her biri için ücret dökümü yer alır.",
     "Sözleşmede denetimin başlangıç ve bitiş tarihleri ile raporun teslim tarihi yer alır.",
     "Sözleşmede denetim hizmeti dışında başka bir hizmet yapılması öngörülemez."],
    "Yönetmelik m. 29/1'e göre sözleşme yazılıdır ve ekip, ücret dökümü ile tarihleri içerir. m. 29/2'ye göre sözleşmede "
    "denetim dışı hizmet öngörülemez ve ücretin ödenmesi denetim hizmeti dışında başka bir şarta bağlanamaz.", topic=BDY)

T1.q("BDY m. 36/2",
    f"{B}, şeffaflık raporunda yer alması gereken bilgiler arasında aşağıdakilerden hangisi yoktur?",
    "Denetlenen her KAYİK'ten alınan denetim ücretinin müşteri bazında dökümü",
    ["Kalite güvence sistemi incelemesinin en son ne zaman yapıldığı",
     "Denetçilerin sürekli eğitimine yönelik izlenen politikalar",
     "Toplam gelirlerin denetim, diğer denetim, defter tutma ve danışmanlık faaliyetlerine göre dağılımı",
     "Sorumlu denetçilerin ücretlendirilme esasları"],
    "Yönetmelik m. 36/2'ye göre şeffaflık raporu; hukuki yapı ve ortaklar, kilit yöneticiler ve sorumlu denetçiler, denetim "
    "ağı, kalite güvence incelemesinin tarihi, önceki yıl KAYİK listesi, sürekli eğitim politikaları, bağımsızlık "
    "uygulamaları, gelirlerin faaliyet türlerine göre dağılımı ve sorumlu denetçilerin ücretlendirme esaslarını içerir; "
    "müşteri bazında ücret dökümü istenmez.", topic=BDY, zorluk="hard")

T1.q("BDY m. 39/1-c",
    "“Denetim kuruluşlarının yetkili oldukları alanların, denetim üstlenenlerin üstlenebilecekleri denetimlerin, sorumlu "
    f"denetçilerin sorumlu denetçilik görevlerinin belirlenen süreyle sınırlandırılması”\n\n{B} yukarıda tanımlanan "
    "idari yaptırım aşağıdakilerden hangisidir?",
    "Faaliyetin kısıtlanması",
    ["Faaliyet izninin askıya alınması", "Uyarı", "Faaliyet izninin iptali", "İkaz"],
    "Yönetmelik m. 39/1-c faaliyetin kısıtlanmasını bu şekilde tanımlar; m. 40/A'ya göre bu yaptırım iki yılı geçmemek "
    "üzere uygulanır. Askıya alma faaliyet izninin belirlenen süreyle askıya alınmasıdır (m. 39/1-ç).", topic=BDY)

T1.sayisal("BDY m. 45/3",
    "Bir denetim kuruluşunun merkezinin bulunduğu binada 3 Şubat'ta yangın çıkmış ve kuruluşun Kuruma yapacağı bildirimleri "
    f"yerine getirmesi imkânsız hâle gelmiştir. {B} mücbir sebep, meydana geldiği tarihi izleyen kaç gün içinde Kuruma "
    "bildirilir?",
    "20", ["7", "10", "15", "30"],
    "Yönetmelik m. 45/3'e göre mücbir sebep, meydana geldiği tarihi izleyen yirmi gün içinde Kuruma bildirilir; bildirim "
    "imkânsızsa süre imkânsızlığın ortadan kalktığı tarihten başlar. Herkesçe malum hâllerde bildirim ve belge aranmaz.",
    topic=BDY, zorluk="easy")

T1.oncul("BDY m. 29/1",
    f"{B} aşağıdaki hususlar değerlendirilmektedir:",
    ["Denetimin başlangıç ve bitiş tarihleri ile raporun teslim tarihi",
     "Denetim ekibindeki denetçilerin yedekleri dahil isim ve unvanları ile ücret dökümü",
     "Denetlenen işletmeye verilecek vergi danışmanlığının kapsamı",
     "Mesleki sorumluluk sigortası yapılacağına ilişkin hüküm"],
    "Yukarıdakilerden hangileri denetim sözleşmesinde yer alması zorunlu hususlardandır?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "Yönetmelik m. 29/1-ğ, f ve h'ye göre tarihler, ekip ve ücret dökümü ile sigorta hükmü sözleşmenin asgari "
    "unsurlarıdır. m. 29/2'ye göre sözleşmede denetim hizmeti dışında başka bir hizmet öngörülemez.", topic=BDY)

T1.q("Etik Kurallar A115.2",
    "Bir denetim şirketi, web sitesinde “Sektörün en hızlı ve en ucuz denetimini biz yapıyoruz; rakip X Denetim'in "
    f"raporları sık sık düzeltiliyor” ifadelerine yer vermiştir. {E} bu tanıtım öncelikle hangi temel ilkeye aykırıdır?",
    "Mesleğe uygun davranış",
    ["Sır saklama", "Tarafsızlık", "Mesleki yeterlik ve özen", "Bağımsızlık"],
    "Etik Kurallar A115.2'ye göre denetçiler pazarlama ve tanıtımda mesleğin itibarına gölge düşüremez; hizmetleri ve "
    "nitelikleri hakkında aşırıya kaçan iddialarda bulunamaz, başkalarının işleri hakkında kötüleyici referans veremez ve "
    "mesnetsiz karşılaştırma yapamaz. Bu hüküm mesleğe uygun davranış ilkesinin parçasıdır.", topic=ETK)

T1.q("KYS 1 prg. 20-21",
    "Türkiye Denetim Standartları – Kalite Yönetim Standardı 1’e göre, bir denetim şirketinde bağımsızlık hükümlerine "
    "uygunluğun işleyişinden sorumlu olarak görevlendirilecek kişide aranan özellikler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Şirketin en yüksek ücretli ortağı olması",
    ["Şirket içinde uygun deneyim ve bilgiye sahip olması",
     "Sorumluluklarını yerine getirmek için yeterli etki ve yetkiye sahip olması",
     "Görevini yerine getirmek için yeterli zamanı olması",
     "Görevini anlaması ve bu görevden hesap verebilir olması"],
    "KYS 1 prg. 20-c'ye göre şirket bağımsızlık hükümlerine uygunluk dahil belirli yönlerin işleyişinden sorumluları "
    "görevlendirir; prg. 21'e göre bu kişiler uygun deneyim, bilgi, etki, yetki ve zamana sahip olmalı, görevlerini anlamalı "
    "ve hesap verebilir olmalıdır. Ücret düzeyi bir kıstas değildir.", topic=ETK, zorluk="hard")

T1.q("BDS 200 A47",
    f"{TDS}, aşağıdakilerden hangisi denetimin yapısal kısıtlamalarından “denetim prosedürlerinin niteliği”ne örnek "
    "değildir?",
    "Önemlilik düzeyinin mesleki muhakemeyle belirlenmesi",
    ["Yönetimin gerekli bilgilerin tamamını kasıtlı veya kasıtsız olarak vermeme ihtimali",
     "Hilenin gizlenmek üzere karmaşık ve dikkatle organize edilmiş planlar içerebilmesi",
     "Denetimin, iddia edilen bir usulsüzlüğe ilişkin resmî bir soruşturma olmaması",
     "Denetçinin arama gibi özel yasal yetkilere sahip olmaması"],
    "BDS 200 A47'ye göre denetim prosedürlerinin niteliğinden kaynaklanan kısıtlamalar; yönetimin bilgileri vermeme "
    "ihtimali, hilenin gizlenmeye yönelik karmaşık planlar içerebilmesi ve denetimin resmî bir soruşturma olmayıp "
    "denetçinin özel yasal yetkilerinin bulunmamasıdır.", topic=TML, zorluk="hard")

T1.q("BDS 315 prg. 14-c",
    "Denetçi, üretim sürecini anlamak için fabrikayı gezmiş, üretim hattındaki işleyişi izlemiş ve yönetimin iş planı "
    f"belgelerini incelemiştir. BDS 315'e göre bu işlemler hangi risk değerlendirme prosedürüne örnektir?",
    "Gözlem ve tetkik",
    ["Analitik prosedür", "Dış teyit", "Yeniden uygulama", "Maddi doğrulama testi"],
    "BDS 315 prg. 14'e göre risk değerlendirme prosedürleri sorgulama, analitik prosedürler ile gözlem ve tetkiktir. "
    "İşletmenin faaliyetlerinin ve tesislerinin izlenmesi ile belgelerin incelenmesi gözlem ve tetkike örnektir.",
    topic=RSK, zorluk="easy")

T1.q("BDS 330 prg. 4",
    "Denetçi, satış faturalarından örnek seçerek her birinde kredi limitinin aşılması hâlinde satış müdürünün onayının "
    f"alınıp alınmadığını incelemektedir. BDS 330'a göre bu prosedür aşağıdakilerden hangisidir?",
    "Kontrol testi",
    ["Detay testi", "Maddi analitik prosedür", "Risk değerlendirme prosedürü", "Dış teyit"],
    "BDS 330 prg. 4'e göre kontrol testi, yönetim beyanı düzeyinde önemli yanlışlıkları önleme veya tespit edip düzeltmede "
    "kontrollerin işleyiş etkinliğini değerlendirmek için tasarlanan prosedürdür. Onay imzasının incelenmesi bir kontrolün "
    "işleyişini test eder.", topic=RSK)

T1.q("BDS 505 prg. 6",
    "Teyit eden tarafın sadece, talepte yer alan bilgilerle mutabık olmaması durumunda doğrudan denetçiye yanıt verdiği "
    f"talep BDS 505'e göre aşağıdakilerden hangisidir?",
    "Olumsuz teyit talebi",
    ["Olumlu teyit talebi", "Yanıt verilmemesi", "İstisna", "Yazılı açıklama"],
    "BDS 505 prg. 6'ya göre olumsuz teyit talebi, teyit eden tarafın sadece talepteki bilgilerle mutabık olmaması durumunda "
    "doğrudan denetçiye yanıt verdiği taleptir. Olumlu teyit talebinde taraf her durumda yanıt verir.", topic=KNT, zorluk="easy")

T1.q("BDS 500 A31",
    f"{TDS}, alacaklara ilişkin aşağıdaki kanıtlardan hangisi genellikle en güvenilir olanıdır?",
    "Müşterinin doğrudan denetçiye gönderdiği yazılı teyit",
    ["Muhasebe müdürünün bakiyeye ilişkin sözlü açıklaması",
     "İşletmenin hazırladığı ve fotokopisi verilen alacak yaşlandırma listesi",
     "Satış müdürünün tahsilat beklentisini anlatan e-postası",
     "İşletme içinde hazırlanıp denetçiye faksla iletilen mutabakat"],
    "BDS 500 A31'e göre işletme dışındaki bağımsız kaynaklardan doğrudan denetçi tarafından elde edilen belge şeklindeki "
    "orijinal kanıt; işletme içinden, sözlü veya kopya olarak elde edilen kanıttan daha güvenilirdir.", topic=KNT)

T1.q("BDS 240 prg. 31-32",
    f"{TDS}, kontrollerin yönetim tarafından ihlal edilmesi riskine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kontrol çevresi güçlü işletmelerde yevmiye kayıtlarının test edilmesine gerek yoktur.",
    ["Bu risk tüm işletmelerde mevcuttur ve ciddi bir risktir.",
     "Denetçi, riske ilişkin değerlendirmesinden bağımsız olarak yevmiye kayıtlarını test eder.",
     "Muhasebe tahminleri yönetimin taraflılığı açısından gözden geçirilir.",
     "Olağan iş akışı dışındaki önemli işlemlerin iş mantığı değerlendirilir."],
    "BDS 240 prg. 31'e göre yönetimin kontrolleri ihlal etme riski tüm işletmelerde vardır ve ciddi risktir. Prg. 32'ye göre "
    "denetçi bu riske ilişkin değerlendirmesinden bağımsız olarak yevmiye kayıtlarını test eder, tahminleri taraflılık "
    "açısından gözden geçirir ve olağan dışı işlemlerin iş mantığını değerlendirir.", topic=HIL)

T1.q("BDS 450 prg. 5, A2",
    "Denetçi bariz biçimde önemsiz tutarı 5.000 ₺ olarak belirlemiştir. Denetim sırasında 3.200 ₺ tutarında bir kesim "
    "hatası bulmuş, ancak hatanın hileden kaynaklanıp kaynaklanmadığı konusunda belirsizlik bulunmaktadır. BDS 450'ye göre "
    "denetçinin bu yanlışlığa ilişkin yapması gereken aşağıdakilerden hangisidir?",
    "Belirsizlik olduğundan önemsiz saymaz, bir araya getirir.",
    ["Tutar eşiğin altında olduğu için yanlışlığı dikkate almaz.",
     "Yanlışlığı doğrudan önemli sayarak olumsuz görüş verir.",
     "Yanlışlığı sadece yönetime sözlü bildirir, kayda almaz.",
     "Eşik tutarını 3.000 ₺'ye düşürerek değerlendirmeyi yeniden başlatır."],
    "BDS 450 A2'ye göre bariz biçimde önemsiz yanlışlıklar tek başına veya toplu olarak açıkça sonuçsuzdur; bir veya daha "
    "fazla kalemin bariz biçimde önemsiz olup olmadığı konusunda belirsizlik varsa yanlışlık önemsiz sayılmaz. Prg. 5'e "
    "göre bu yanlışlık bir araya getirilir.", topic=ONM, zorluk="hard")

T1.q("BDS 706 prg. 8, A5",
    "Yeterli ve uygun kanıt elde eden denetçi, tablolarda önemli yanlışlık tespit etmemiştir. Ancak işletmenin ana üretim "
    "tesisi bilanço tarihinden sonra bir depremde ağır hasar görmüş ve bu durum dipnotlarda uygun şekilde açıklanmıştır. "
    f"BDS 706'ya göre denetçi raporuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Olumlu görüş verip dikkat çekilen hususlar paragrafıyla atıf yapabilir.",
    ["Deprem nedeniyle sınırlı olumlu görüş verir.",
     "Deprem yaygın etki doğurduğundan olumsuz görüş verir.",
     "Belirsizlik nedeniyle görüş vermekten kaçınır.",
     "Durumu diğer hususlar paragrafında açıklar, çünkü tablolarda yer almamaktadır."],
    "BDS 706 prg. 8 ve A5'e göre tablolarda uygun şekilde açıklanan ve anlama açısından temel öneme sahip bir husus (ör. "
    "önemli bir sonraki olay veya ciddi afet) için, görüş değişikliği gerektirmemesi şartıyla dikkat çekilen hususlar "
    "paragrafı eklenebilir; görüş olumlu kalır.", topic=RPR)

# =============================================================================== TEST 2
T2 = paket("questions_muhasebe_denetimi_test2_2026.json", 2026092852)

T2.q("BDY m. 5/3",
    "Denetim; denetimin konusu hakkında, (i)---- bağlı kalmak ve (ii)---- içinde bulunmak suretiyle, TDS çerçevesinde "
    "yeterli ve uygun denetim kanıtı toplanmasını, bu kanıtlara dayandırılarak bir görüş oluşturulmasını ve görüşün "
    f"raporlanmasını kapsar.\n\n{B} boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
    "(i) mesleki etik ilkelere (ii) mesleki şüphecilik",
    ["(i) yönetimin talimatlarına (ii) mesleki şüphecilik",
     "(i) mesleki etik ilkelere (ii) tam güvence",
     "(i) sözleşme şartlarına (ii) mesleki muhakeme",
     "(i) Kurum kararlarına (ii) bağımsızlık"],
    "Yönetmelik m. 5/3'e göre denetim; mesleki etik ilkelere bağlı kalmak ve mesleki şüphecilik içinde bulunmak suretiyle, "
    "TDS çerçevesinde yeterli ve uygun kanıt toplanmasını, görüş oluşturulmasını ve raporlanmasını kapsar.", topic=BDY)

T2.q("BDY m. 11, 17/4",
    "Kurulun yetkilendirme kararı çıkmış, ancak henüz sicile kayıt ve ilan yapılmamış bir denetim kuruluşu, bir şirketle "
    f"denetim sözleşmesi imzalamış ve çalışmaya başlamıştır. {B} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlan ve sicil kaydı olmadan yetki kullanılamayacağından aykırıdır.",
    ["Kurul kararı alındığı için kuruluş denetim yetkisini kullanabilir.",
     "Sözleşme geçerlidir; ilan sadece kamuoyunu bilgilendirme amacı taşır.",
     "Kuruluş, sicile kayıt yapılana kadar sadece KAYİK denetimlerini üstlenebilir.",
     "Kuruluş, belge teslim alınana kadar sorumlu denetçileri aracılığıyla denetim yapabilir."],
    "Yönetmelik m. 11/2'ye göre yetkilerin kullanımı yetkilendirmenin Kurum tarafından ilanıyla başlar; m. 17/1'e göre "
    "yetkilendirme işlemleri sicile kayıt ve ilanla yürürlüğe girer ve m. 17/4'e göre sicile kayıtlı olmayanlar denetim "
    "faaliyetinde bulunamaz.", topic=BDY)

T2.q("BDY m. 13/1-i",
    "ABC Bağımsız Denetim A.Ş.'nin ortağı olan bir denetçi, aynı zamanda XYZ Bağımsız Denetim A.Ş.'de denetçi olarak "
    f"çalışmaktadır. {B} bu durum ABC'nin faaliyet izni şartları bakımından aşağıdakilerden hangisidir?",
    "Aykırıdır; denetçiler başka bir denetim kuruluşunda görev alamaz.",
    ["Aykırı değildir; ortaklık ile başka kuruluşta çalışmak farklı sıfatlar olduğundan birlikte yürütülebilir.",
     "Denetçi ABC'de yönetim organında değilse aykırı değildir.",
     "XYZ'nin KAYİK denetimi yapmaması hâlinde aykırı değildir.",
     "Kurum izin verirse iki kuruluşta birden faaliyet mümkündür."],
    "Yönetmelik m. 13/1-i'ye göre denetim kuruluşunun denetçilerinin, ortaklarının ve kilit yöneticilerinin başka bir denetim "
    "kuruluşunda veya denetim üstlenen bağımsız denetçi yanında denetçi, ortak ya da kilit yönetici olmaması şarttır; "
    "m. 26/4 da denetçilerin tek bir kuruluş adına denetim yapabileceğini düzenler.", topic=BDY)

T2.q("BDY m. 20/1",
    f"{B}, kalite yönetim sisteminin tasarlanması, uygulanması ve işletilmesine ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Yazılı politika ve süreçler bir kez oluşturulduktan sonra Kurum düzenlemeleri değişse de güncellenmez.",
    ["Denetim kuruluşları faaliyetlerini asgari şartları Kurumca belirlenen bir kalite yönetim sistemi içinde yürütür.",
     "Kurum düzenlemelerine göre tasarlanıp Kuruma bildirilen yazılı politika ve süreçlere uyulur.",
     "Denetim üstlenen bağımsız denetçiler de kalite yönetim sistemi çerçevesinde faaliyet yürütür.",
     "Politika ve süreçler etkin bir şekilde işletilir."],
    "Yönetmelik m. 20/1'e göre denetim kuruluşları ve denetim üstlenen bağımsız denetçiler asgari şartları Kurumca "
    "belirlenen kalite yönetim sistemi çerçevesinde faaliyet yürütür; Kuruma bildirilen yazılı politika ve süreçlere uyulur "
    "ve bunlar Kurum düzenlemelerine paralel olarak güncellenerek etkin biçimde işletilir.", topic=BDY)

T2.q("BDY m. 23/3",
    f"{B}, denetim kuruluşlarının izin verilen tanıtım faaliyetlerini yürütürken uyması gereken kurallar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Tanıtım metinlerinin yayımlanmadan önce Kurum tarafından onaylanması",
    ["İşin sonucu ile ilgili vaat ve taahhütlerde bulunulmaması",
     "İşin gerektirdiği ciddiyette ve ölçüde kalınması, abartılı ifadelerden kaçınılması",
     "Somut temeli olmayan bekleyişler yaratılmaması",
     "Kuruluşun diğer kuruluş veya denetçilerle karşılaştırılmaması"],
    "Yönetmelik m. 23/3'e göre izin verilen faaliyetlerde vaat ve taahhütte bulunulmaması, ciddiyet ve ölçüde kalınması, "
    "yanıltıcı unsurlara yer verilmemesi, somut temeli olmayan beklenti yaratılmaması ve karşılaştırma yapılmaması "
    "gerekir. Kurumun ön onayı öngörülmemiştir.", topic=BDY)

T2.q("BDY m. 25",
    f"{B}, denetçilerin sürekli eğitimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sürekli eğitim yükümlülüğü, denetçinin sicile tescil edildiği gün başlar.",
    ["Denetçiler her yıl, yıllık ve üçer yıllık dönemler için Kurumun öngördüğü şartları karşılar.",
     "Denetim kuruluşları, denetçilerinin eğitim programlarını tamamlamaları için gerekli tedbirleri alır.",
     "Yükümlülüğü yerine getirmeyen denetçiler, tamamlayana kadar denetim yapamaz.",
     "Yetkilendirme ile tescil arasında iki yıl veya daha fazla süre bulunanlara ilave yükümlülük getirilebilir."],
    "Yönetmelik m. 25/2'ye göre sürekli eğitim yükümlülüğü, tescil tarihini izleyen ikinci takvim yılının başından "
    "itibaren başlar; tescil ile yetkilendirme arasında iki yıl veya fazla süre bulunanlara ilave yükümlülük getirilebilir. "
    "m. 25/3, 25/4 ve 25/7 yıllık ve üç yıllık şartları, kuruluşların tedbir yükümlülüğünü ve yaptırımı düzenler.", topic=BDY)

T2.q("BDY m. 27/2",
    "Kurum, bankaların denetimi için bankacılık alanında ilave şartlar belirlemiştir. Bir denetim kuruluşu bir bankanın "
    f"denetim ekibine bu şartları taşımayan bir denetçiyi de dahil etmek istemektedir. {B} aşağıdakilerden hangisi "
    "doğrudur?",
    "Ekipteki tüm denetçiler ilave şartları taşımalıdır; bu mümkün değildir.",
    ["Sorumlu denetçi şartları taşıyorsa diğer denetçilerin taşıması gerekmez.",
     "Ekibin çoğunluğu şartları taşıyorsa bir denetçi eksik olabilir.",
     "İlave şartlar sadece bilgi sistemleri uzmanları için aranır.",
     "Denetçi yedek olarak gösterilirse şartları taşıması gerekmez."],
    "Yönetmelik m. 27/2'ye göre Kurum, ilgili kurumların görüşünü alarak belirli alanlarda denetim yapacaklar için ilave "
    "şartlar belirleyebilir ve denetim ekibindeki tüm denetçiler işletmenin özelliğine uygun bu ilave şartları taşır.",
    topic=BDY)

T2.q("BDY m. 28",
    f"{B}, sorumlu denetçilerin görevlendirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sorumlu denetçi onay talebini Kuruma adayın kendisi doğrudan gönderir.",
    ["Onay talebi, şartları gösteren belgelerle denetim kuruluşu veya denetim üstlenen denetçi tarafından gönderilir.",
     "Sorumlu denetçiler, Yönetmelikteki şartları sağlayanlar arasından Kurumun onayıyla görevlendirilir.",
     "Sorumlu denetçinin raporu imzalamaya yönetim organınca yetkilendirilmiş olması gerekir.",
     "Denetim üstlenen bağımsız denetçi, üstlendiği denetimlerin sorumlu denetçisidir."],
    "Yönetmelik m. 28/1'e göre sorumlu denetçiler şartları sağlayanlar arasından Kurum onayıyla görevlendirilir ve rapor "
    "imzalamaya yetkilendirilmiş olmalıdır; m. 28/2'ye göre onay talebi denetim kuruluşu veya denetim üstlenen bağımsız "
    "denetçi tarafından gönderilir. m. 27/6'ya göre denetim üstlenen bağımsız denetçi üstlendiği denetimlerin sorumlu "
    "denetçisidir.", topic=BDY)

T2.sayisal("BDY m. 34/1-c",
    "Bir anonim şirketin genel kurulu, TTK m. 399 uyarınca denetçinin görevden alınmasına ilişkin işlemi 12 Mayıs'ta "
    f"tamamlamıştır. {B} denetim kuruluşu bu işlemi, işlem tarihini takip eden günden itibaren en geç kaç gün içinde "
    "Kuruma bildirir?",
    "10", ["5", "15", "20", "30"],
    "Yönetmelik m. 34/1-c'ye göre TTK m. 399 uyarınca görevden alma ve sözleşmenin feshine ilişkin işlemler, işlem tarihini "
    "takip eden günden itibaren en geç 10 gün içinde Kuruma bildirilir.", topic=BDY)

T2.q("BDY m. 44",
    f"{B}, denetimlerde sorumluluğa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Rapordaki yanlış kanaatlerden doğan zarardan sadece denetim kuruluşu sorumludur; denetçiler sorumlu tutulamaz.",
    ["TDS'ye aykırı raporlardan doğan zararlardan denetim kuruluşları ve denetçiler ayrı ayrı hukuken sorumludur.",
     "İdari yaptırımlar, aykırılıkları tespit edilen denetim kuruluşları ve denetim üstlenen bağımsız denetçiler hakkında uygulanır.",
     "Kurumca gerekli görülen hâllerde aykırılığa neden olan ekip denetçileri hakkında da yaptırım uygulanır.",
     "Yardımcı kişilerin sebep olduğu aykırılıklardan idari yaptırım bakımından gözetimindeki kuruluş sorumludur."],
    "Yönetmelik m. 44/1'e göre TDS'ye aykırı raporlar ile yanlış, eksik ve yanıltıcı bilgi ve kanaatlerden doğan zararlardan "
    "denetim kuruluşları ve denetçiler ayrı ayrı hukuken sorumludur; m. 44/2-3 idari yaptırımların kime uygulanacağını "
    "düzenler.", topic=BDY)

T2.q("Etik Kurallar 120.6 U3-a",
    f"Bir denetim ekibi üyesinin eşi, denetim müşterisinin paylarından önemli bir miktara sahiptir. {E} bu durum öncelikle "
    "hangi tehdidi oluşturur?",
    "Kişisel çıkar tehdidi",
    ["Kendi kendini denetleme tehdidi", "Taraf tutma tehdidi", "Yıldırma tehdidi", "Yakınlık tehdidi"],
    "Etik Kurallar 120.6 U3-a'ya göre kişisel çıkar tehdidi, finansal veya finansal olmayan bir çıkarın denetçinin "
    "muhakemesini veya davranışını uygun olmayan şekilde etkilemesi tehdididir. Ekip üyesinin yakın aile üyesinin "
    "müşterideki finansal çıkarı bu tehdidi oluşturur.", topic=ETK, zorluk="easy")

T2.q("KYS 2 prg. 25",
    "Türkiye Denetim Standartları – Kalite Yönetim Standardı 2’ye göre, kaliteyi gözden geçiren kişinin gözden geçirme "
    "sırasında yaptığı işler arasında aşağıdakilerden hangisi yer almaz?",
    "Denetim ekibinin yerine önemli hesaplar için detay testlerini kendisi yürütmek",
    ["Denetim ekibi ve şirket tarafından iletilen bilgileri okumak ve anlamak",
     "Sorumlu denetçiyle ve uygun hâllerde ekibin diğer üyeleriyle önemli konuları görüşmek",
     "Önemli muhakemelere ilişkin seçilmiş belgeleri gözden geçirmek",
     "Finansal tabloları ve bunlara ilişkin denetçi raporunu okumak"],
    "KYS 2 prg. 25'e göre kaliteyi gözden geçiren kişi; iletilen bilgileri okur ve anlar, sorumlu denetçi ve ekip üyeleriyle "
    "önemli konuları görüşür, önemli muhakemelere ilişkin seçilmiş belgeleri gözden geçirir ve tabloları ve raporu okur. "
    "Prg. 9'a göre ekip üyesi olmadığından kanıt toplamaz.", topic=ETK)

T2.q("BDS 210 A28",
    f"{TDS}, tekrarlayan denetimlerde denetim sözleşmesi şartlarının revize edilmesini gerektirebilecek durumlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Denetim ekibindeki bir denetçi yardımcısının başka bir müşteriye kaydırılması",
    ["İşletmenin denetimin amacını ve kapsamını yanlış anladığına dair gösterge bulunması",
     "Yakın bir tarihte kıdemli yöneticilerde değişiklik olması",
     "İşletmenin ortaklık yapısında önemli bir değişiklik olması",
     "İşletmenin faaliyetlerinin niteliği veya büyüklüğünde önemli bir değişiklik olması"],
    "BDS 210 A28'e göre yanlış anlama göstergesi, revize veya özel şartlar, kıdemli yöneticilerde değişiklik, ortaklık "
    "yapısında önemli değişiklik, faaliyetlerin niteliği veya büyüklüğündeki değişiklik ve mevzuat ile çerçeve "
    "değişiklikleri sözleşmenin revizyonunu gerektirebilir. Ekip içi personel değişikliği bu kapsamda değildir.",
    topic=TML)

T2.q("BDS 315 prg. 12-i",
    "Bir işletmenin faaliyet gösterdiği sektörde yıl içinde gelir tanımasını doğrudan etkileyen yeni bir düzenleme "
    f"yürürlüğe girmiştir. BDS 315'e göre bu durum, ilgili yönetim beyanlarının yanlışlığa açıklığını etkileyen hangi "
    "yapısal risk faktörüne örnektir?",
    "Değişiklik",
    ["Subjektiflik", "Karmaşıklık", "Kontrol riski", "Tespit edememe riski"],
    "BDS 315 prg. 12-i'ye göre yapısal risk faktörleri karmaşıklık, subjektiflik, değişiklik, belirsizlik ve yönetimin "
    "taraflılığına veya hileye açıklıktır. Yeni bir düzenlemenin yürürlüğe girmesi, değişiklik faktörüne örnektir.",
    topic=RSK)

T2.q("BDS 330 A1",
    "Denetçi, kontrol çevresinde ciddi zayıflıklar tespit etmiş ve finansal tablo düzeyinde önemli yanlışlık riskini yüksek "
    f"değerlendirmiştir. BDS 330'a göre aşağıdakilerden hangisi bu duruma uygun bir genel karşılık değildir?",
    "Kontrollere daha fazla güvenerek maddi doğrulama prosedürlerini azaltmak",
    ["Maddi doğrulamayı ara dönem yerine dönem sonunda ve daha kapsamlı uygulamak",
     "Daha deneyimli personel ve gerekirse uzman görevlendirmek",
     "Ekibin daha fazla yönlendirilmesi ve gözetilmesi",
     "Prosedürlerin seçimine öngörülemezlik unsurları eklemek"],
    "BDS 330 A1-A3'e göre kontrol çevresi etkin değilse denetçi maddi doğrulama prosedürlerini ara dönem yerine dönem "
    "sonunda uygulayabilir, daha fazla kanıt toplayabilir ve daha deneyimli personel görevlendirebilir; öngörülemezlik "
    "unsurlarını artırır.", topic=RSK)

T2.q("BDS 501 prg. 10",
    "Denetçi, işletmenin taraf olduğu önemli bir tazminat davasına ilişkin önemli yanlışlık riski bulunduğunu "
    f"değerlendirmiştir. BDS 501'e göre denetçinin ilave olarak yapması gereken aşağıdakilerden hangisidir?",
    "Yönetimin hazırladığı mektupla dış hukuk müşaviriyle doğrudan iletişim kurmak",
    ["Davanın sonucunu yönetimin tahminine göre kabul edip karşılığı değerlendirmemek",
     "Davayı mahkeme kararı kesinleşene kadar değerlendirme dışında bırakmak",
     "Karşı tarafın avukatından davanın muhtemel sonucunu sormak",
     "Dava dosyasının tamamını mahkemeden resmî olarak talep etmek"],
    "BDS 501 prg. 10'a göre belirlenmiş dava veya iddialarla ilgili önemli yanlışlık riski değerlendirilirse denetçi, "
    "yönetim tarafından hazırlanan, denetçi tarafından gönderilen ve dış hukuk müşavirinin denetçiyle doğrudan iletişime "
    "geçmesini talep eden bir sorgulama mektubuyla dış hukuk müşaviriyle doğrudan iletişim kurar.", topic=KNT)

T2.q("BDS 530 Ek 4",
    "Denetçi, 5.000 satış faturasından 100 faturalık bir örneklem seçmek için örnekleme aralığını 50 olarak belirlemiş, "
    f"ilk 50 fatura içinden rastgele bir başlangıç noktası seçmiş ve sonrasında her 50. faturayı seçmiştir. BDS 530'a göre "
    "bu seçim yöntemi aşağıdakilerden hangisidir?",
    "Sistematik seçim",
    ["Gelişigüzel seçim", "Blok seçim", "Parasal birim örneklemesi", "Belirli kalemlerin seçilmesi"],
    "BDS 530 Ek 4'e göre sistematik seçimde anakitledeki birim sayısı örneklem büyüklüğüne bölünerek örnekleme aralığı "
    "belirlenir (5.000 / 100 = 50) ve bir başlangıç noktasından sonra her 50. birim seçilir.", topic=ONM, zorluk="easy")

T2.q("BDS 705 prg. 7-b",
    "Denetçi, işletmenin yurt dışındaki bir şubesinin stoklarına ilişkin yeterli ve uygun kanıt elde edememiştir. Şube "
    f"stokları önemlidir, ancak tabloların geri kalanı üzerinde yaygın bir etkisi yoktur. BDS 705'e göre denetçinin vereceği "
    "görüş aşağıdakilerden hangisidir?",
    "Sınırlı olumlu görüş",
    ["Görüş vermekten kaçınma", "Olumsuz görüş", "Olumlu görüş", "Diğer hususlarla olumlu görüş"],
    "BDS 705 prg. 7-b'ye göre yeterli ve uygun kanıt elde edilemeyen hususun muhtemel etkisi önemli ancak yaygın değilse "
    "sınırlı olumlu görüş verilir; önemli ve yaygın olabilecekse görüş vermekten kaçınılır.", topic=RPR, zorluk="easy")

T2.oncul("BDS 240 A1, Ek 1",
    f"{TDS} aşağıdaki durumlar değerlendirilmektedir:",
    ["Nakit tahsilatı yapan kişinin aynı zamanda kayıtları da tutması",
     "Yönetimin priminin tamamen yıllık kâr hedefine bağlı olması",
     "Önemli işlemlerin karmaşık ve kolay denetlenemeyen yapılar üzerinden yürütülmesi",
     "Yönetimin, üst yönetimden sorumlu olanlarca etkin biçimde gözetilmemesi"],
    "Yukarıdakilerden hangileri hile üçgeninde “fırsat” unsuruna ilişkin hile riski faktörlerine örnektir?",
    "I, III ve IV",
    ["I ve II", "II ve IV", "I, II ve III", "I, III ve IV", "II, III ve IV"],
    "BDS 240 A1 ve Ek 1'e göre görevler ayrılığının bulunmaması (I), karmaşık işlem yapıları (III) ve yönetimin etkin "
    "gözetilmemesi (IV) hile yapma fırsatı oluşturan faktörlerdir. Primin kâr hedefine bağlanması (II) teşvik veya baskı "
    "unsuruna örnektir.", topic=HIL, zorluk="hard")

T2.q("BDS 320 prg. 10, A10",
    "Denetçi, bir şirkette yönetim kurulu üyelerine ödenen ücretlerin kullanıcılar açısından özel önem taşıdığını ve bu "
    "alandaki genel önemlilikten çok daha küçük tutarlı yanlışlıkların bile kullanıcı kararlarını etkileyebileceğini "
    f"değerlendirmiştir. BDS 320'ye göre denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Bu açıklama için ayrıca daha düşük önemlilik düzeyi belirlemek",
    ["Genel önemliliği bu açıklamaya göre yükseltmek",
     "Açıklamayı önemsiz sayarak denetim kapsamından çıkarmak",
     "Açıklamanın tutarını yönetimin belirlediği önemliliğe göre test etmek",
     "Performans önemliliğini genel önemliliğe eşitlemek"],
    "BDS 320 prg. 10 ve A10'a göre mevzuat veya çerçevenin kullanıcı beklentilerini etkilediği kalemler (ör. yönetime ve "
    "üst yönetime ödenen ücretler, ilişkili taraf işlemleri) için genel önemlilikten düşük önemlilik düzeyi belirlenebilir.",
    topic=ONM)

# =============================================================================== TEST 3
T3 = paket("questions_muhasebe_denetimi_test3_2026.json", 2026092853)

T3.q("BDY m. 7",
    f"{B}, denetimin tarafları aşağıdakilerin hangisinde doğru verilmiştir?",
    "Denetlenen, denetimi yapan ve hedeflenen kullanıcılar",
    ["Denetlenen, Kamu Gözetimi Kurumu ve vergi idaresi",
     "Denetimi yapan, denetim ağı ve denetlenen işletmenin alacaklıları",
     "Denetlenen işletmenin yönetim kurulu, genel kurulu ve iç denetim birimi",
     "Denetimi yapan, sorumlu denetçi ve kaliteyi gözden geçiren kişi"],
    "Yönetmelik m. 7'ye göre denetlenen, denetimi yapan ve ilgili mevzuatında hedeflenen kullanıcılar denetimin taraflarını "
    "oluşturur.", topic=BDY, zorluk="easy")

T3.q("BDY m. 14/1-c",
    "Almanya'da yerleşik olup Türkiye'de serbest muhasebeci mali müşavir ruhsatına sahip, denetçilik sınavını geçmiş ve "
    f"uygulamalı eğitimini tamamlamış bir meslek mensubu Bağımsız Denetçi Belgesi almak istemektedir. {B} bu başvuruya "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "Türkiye'de yerleşik olma şartını taşımadığından yetkilendirilemez.",
    ["Tüm diğer şartları taşıdığından yetkilendirilir.",
     "Yurt dışında yerleşik olduğundan sadece ihtiyari denetimlerde yetkilendirilir.",
     "Türkiye'de bir denetim kuruluşunda istihdam edilirse yerleşik olma şartı aranmaz.",
     "Başvuru için sadece Türkiye'de bir tebligat adresi göstermesi yeterlidir."],
    "Yönetmelik m. 14/1-c'ye göre denetim faaliyetinde bulunmak isteyenlerin Türkiye'de yerleşik olması gerekir; bu şartı "
    "taşımayan meslek mensubu diğer şartları sağlasa da yetkilendirilemez.", topic=BDY)

T3.q("BDY m. 17/2, 18/3",
    f"{B}, bağımsız denetim resmi siciline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sicile kaydedilen tüm bilgilerin kamuya ilan edilmesi zorunludur.",
    ["Kurum tarafından her denetim kuruluşuna ve denetçiye bir sicil numarası verilir.",
     "Sicil Kurumca elektronik ortamda tutulur.",
     "Sicilde denetim kuruluşlarının faal veya gayri faal olma durumları yer alır.",
     "Sicilde denetçilerin denetim üstlenen bağımsız denetçi olup olmadıkları gösterilir."],
    "Yönetmelik m. 17/2'ye göre her denetim kuruluşuna ve denetçiye sicil numarası verilir; m. 18 faal veya gayri faal olma "
    "durumu ile denetim üstlenen bağımsız denetçi olma bilgilerini sayar. m. 18/3'e göre sicile kaydedilen bilgilerden "
    "Kurumca belirlenenler kamuya ilan edilmeyebilir.", topic=BDY)

T3.q("BDY m. 22/1-a",
    "(i)----: Denetçinin dürüstlük, tarafsızlık ve mesleki şüphecilik içinde hareket etmesini teminen, mesleki muhakemesini "
    f"olumsuz etkileyebilecek tesirlerden ari olarak görüş açıklamasıdır.\n\n{B} boşluğa aşağıdakilerden hangisi "
    "gelmelidir?",
    "Esasta bağımsızlık",
    ["Şekilde bağımsızlık", "Tarafsızlık", "Mesleki muhakeme", "Dürüstlük"],
    "Yönetmelik m. 22/1-a esasta bağımsızlığı, mesleki muhakemeyi olumsuz etkileyebilecek tesirlerden ari olarak görüş "
    "açıklanması olarak tanımlar; m. 22/1-b şekilde bağımsızlığı makul ve bilgi sahibi üçüncü kişilerde oluşacak intiba "
    "bakımından tanımlar.", topic=BDY, zorluk="easy")

T3.q("BDY m. 29/4",
    "Denetlenen şirket, yazılı taleplere rağmen denetçiye stok ve alacak kayıtlarına erişim imkânı vermemiş; denetim "
    f"kuruluşu bu nedenle haklı sebeple sözleşmeyi feshetmiştir. {B} kuruluşun yapması gereken aşağıdakilerden hangisidir?",
    "Feshi ve gerekçelerini yazılı olarak 10 gün içinde Kuruma bildirmek",
    ["Feshi sadece şirketin genel kuruluna sözlü olarak bildirmek",
     "Fesihten önce Kurumun yazılı onayını almak",
     "Feshi 60 gün içinde ticaret sicil müdürlüğüne tescil ettirmek",
     "Fesihten sonra çalışma notlarını şirkete iade edip dosyayı kapatmak"],
    "Yönetmelik m. 29/4'e göre denetimi üstlenen sözleşmeyi sadece haklı sebep varsa veya görevden alınma davası açılmışsa "
    "feshedebilir; fesih ve gerekçeleri yazılı olarak 10 gün içinde Kuruma bildirilir. m. 29/5'e göre çalışma notları yerine "
    "geçecek denetçiye teslim edilir.", topic=BDY)

T3.q("BDY m. 31/3",
    "Finansal tablolar ve yıllık faaliyet raporu ilan edildikten iki ay sonra denetçi, tabloları etkileyecek önemli bir "
    f"olaydan haberdar olmuştur. {B} denetçinin yükümlülüğü aşağıdakilerden hangisidir?",
    "Düzeltme veya açıklama gerekliliğini değerlendirip gerekli işlemleri yapar.",
    ["İlandan sonra sorumluluğu sona erdiğinden işlem yapmaz.",
     "Durumu sadece bir sonraki yılın denetim raporunda açıklar.",
     "Olayı doğrudan kamuya duyurarak yatırımcıları bilgilendirir ve raporu geçersiz sayar.",
     "Denetim raporunu geri çektiğini ticaret siciline tescil ettirir."],
    "Yönetmelik m. 31/3'e göre denetim kuruluşu ve denetçi, tabloların veya faaliyet raporunun ilan tarihinden sonraki "
    "dönemde gerçekleşen ve bunları etkileyecek olaylardan haberdar olursa düzeltme veya açıklama gerekliliğini "
    "değerlendirir ve TDS ile mevzuat uyarınca gerekli işlemleri yapar (BDS 560 prg. 14).", topic=BDY)

T3.q("BDY m. 38/8",
    f"{B}, inceleme için görevlendirilenlerce istenen bilgi ve belgelerin verilmemesi hâlinde denetim kuruluşları, "
    "denetçiler, denetlenen işletmeler ve üçüncü kişiler nezdinde arama hangi karar üzerine yapılabilir?",
    "Sulh ceza hâkiminin kararıyla",
    ["Kurul Başkanının yazılı talimatıyla",
     "Denetim kuruluşunun yönetim organının onayıyla",
     "Cumhuriyet savcısının sözlü talimatıyla",
     "İnceleme görevlisinin kendi takdiriyle"],
    "Yönetmelik m. 38/8'e göre istenen bilgi ve belgelerin verilmemesi veya gerekli görülen diğer hâllerde, Kurumun talebi "
    "ve yetkili sulh ceza hâkiminin kararı üzerine denetim kuruluşları, denetçiler, denetlenen işletmeler ve üçüncü kişiler "
    "nezdinde arama yapılabilir.", topic=BDY, zorluk="hard")

T3.q("BDY m. 42/1",
    f"{B}, aşağıdaki aykırılıklardan hangisi faaliyet izninin iptalini gerektiren hâller arasında yer almaz?",
    "Şeffaflık raporunun Kuruma zamanında bildirilmemesi",
    ["Olumsuz görüş verilmesi gerekirken kasıtlı olarak olumlu görüş bildirilmesi",
     "Yetki belgesinin kasten yanlış veya yanıltıcı beyanla alınması",
     "Yetkilendirme şartlarının sonradan kaybedilmesi",
     "Denetime olan güveni sarsacak derecede bağımsızlığın ve tarafsızlığın kaybedilmesi"],
    "Yönetmelik m. 42/1'e göre kasıtlı yanlış görüş, yetki belgesinin kasten yanıltıcı beyanla alınması, şartların sonradan "
    "kaybedilmesi ve güveni sarsacak derecede bağımsızlığın kaybedilmesi iptal sebebidir. Şeffaflık raporuna aykırılık "
    "m. 40/1-g'ye göre uyarı yaptırımı gerektirir.", topic=BDY)

T3.q("BDY m. 43/9-b",
    "Kurum, ihbar üzerine yaptığı ilk değerlendirmede bir denetim kuruluşunun faaliyete devam etmesinin telafisi zor "
    f"zararlara yol açabileceğini tespit etmiştir. {B} Kurulun bu durumda uygulayabileceği tedbir aşağıdakilerden "
    "hangisidir?",
    "Denetim faaliyetini en fazla bir yıl süreyle durdurmak",
    ["Faaliyet iznini savunma almadan süresiz iptal etmek",
     "Kuruluşa ikaz vererek faaliyetine devam etmesine izin vermek",
     "Kuruluşun ortaklarını sicilden silmek",
     "Kuruluşun yetki alanını beş yıl süreyle kısıtlamak"],
    "Yönetmelik m. 43/9-b'ye göre gözetim faaliyetleri veya ihbar ve şikâyetlerle ilgili ilk değerlendirmeler sonucunda, "
    "askıya alma veya iptali gerektiren durum nedeniyle faaliyete devamın telafisi zor zararlara yol açma ihtimali varsa "
    "Kurul denetim faaliyetini en fazla bir yıl süreyle durdurabilir.", topic=BDY, zorluk="hard")

T3.q("Etik Kurallar 120.6 U3-d",
    "Denetlenen işletmenin yönetimi, önerilen düzeltme kaydı yapılmadığı sürece denetçinin görüşünü değiştirmesi hâlinde "
    f"denetim şirketi aleyhine dava açacağını bildirmiştir. {E} bu durum aşağıdaki tehditlerden hangisini oluşturur?",
    "Yıldırma tehdidi",
    ["Taraf tutma tehdidi", "Yakınlık tehdidi", "Kendi kendini denetleme tehdidi", "Kişisel çıkar tehdidi"],
    "Etik Kurallar 120.6 U3-d'ye göre yıldırma tehdidi, başkalarının nüfuzlarını kötüye kullanma çabaları dahil, "
    "denetçinin mevcut veya hissettiği baskılar nedeniyle tarafsız hareket edebilmesinin engellenmesi tehdididir. Dava "
    "tehdidi bu türün örneğidir.", topic=ETK, zorluk="easy")

T3.q("KYS 1 prg. 35",
    "Türkiye Denetim Standartları – Kalite Yönetim Standardı 1’e göre, denetim şirketinin izleme ve düzeltme sürecinin "
    "amacı aşağıdakilerden hangisidir?",
    "Sistem hakkında güvenilir ve zamanında bilgi sağlamak ve eksiklikleri düzeltmek",
    ["Denetim ücretlerinin tahsilatını izlemek ve gecikmeleri yönetime bildirmek",
     "Denetlenen işletmelerin iç kontrol sistemlerini yıl boyunca sürekli izleyip raporlamak",
     "Denetçilerin çalışma saatlerini izleyerek maliyetleri azaltmak",
     "Kurum incelemelerinin sonuçlarını kamuoyuna duyurmak"],
    "KYS 1 prg. 35'e göre izleme ve düzeltme süreci, kalite yönetim sisteminin tasarımı, uygulanması ve işleyişi hakkında "
    "ihtiyaca uygun, güvenilir ve zamanında bilgi sağlamak ve tespit edilen eksikliklerin zamanında düzeltilmesini "
    "teminen uygun adımları atmak amacıyla oluşturulur.", topic=ETK)

T3.q("BDS 200 A27",
    f"{TDS}, mesleki muhakemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mesleki muhakeme, yeterli kanıtla desteklenmeyen kararların gerekçesi olarak kullanılabilir.",
    ["Mesleki muhakeme, denetimin uygun şekilde yürütülmesi için şarttır.",
     "Mesleki muhakeme, eğitim, bilgi ve deneyimle geliştirilmiş kişilerce kullanılır.",
     "Mesleki muhakemenin değerlendirilmesi, durum ve gerçeklere göre uygun olup olmadığına bakılarak yapılır.",
     "Mesleki muhakeme denetim boyunca kullanılır ve uygun şekilde belgelendirilir."],
    "BDS 200 A23-A27'ye göre mesleki muhakeme denetim için şarttır; eğitim, bilgi ve deneyimle kullanılır, denetim boyunca "
    "uygulanır ve belgelendirilir. A27'ye göre mesleki muhakeme, durum ve gerçeklerle veya yeterli ve uygun kanıtla "
    "desteklenmeyen kararların gerekçesi olarak kullanılamaz.", topic=TML)

T3.q("BDS 315 prg. 12-e",
    f"{TDS}, iç kontrolün yapısal sınırlamalarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Doğru tasarlanan bir iç kontrol sistemi, yanlışlıkları önlediğine dair mutlak güvence sağlar.",
    ["İç kontrol, ne kadar etkin olursa olsun, işletmenin amaçlarına ulaştığına dair sadece makul güvence sağlar.",
     "İnsan hatası ve yanlış muhakeme kontrollerin etkin işlemesini engelleyebilir.",
     "Kontroller iki veya daha fazla kişinin muvazaasıyla etkisiz hâle getirilebilir.",
     "Yönetim kontrolleri uygun olmayan biçimde ihlal edebilir."],
    "BDS 315 prg. 12-e ve uygulama hükümlerine göre iç kontrol sistemi amaçlara ulaşıldığına dair makul güvence sağlar; "
    "insan hatası, muvazaa ve yönetimin kontrolleri ihlali gibi yapısal sınırlamalar nedeniyle mutlak güvence sağlamaz.",
    topic=RSK)

T3.q("BDS 505 A14",
    "Denetçinin gönderdiği alacak teyidinin yanıtı, doğrudan denetçiye değil işletmenin muhasebe müdürüne gelmiş ve müdür "
    f"yanıtı denetçiye iletmiştir. BDS 505'e göre bu durumda denetçinin yaklaşımı aşağıdakilerden hangisi olmalıdır?",
    "Güvenilirliği sorgular; gerekirse teyit edenle doğrudan iletişim kurar.",
    ["Yanıt yazılı olduğundan başka bir değerlendirme yapmadan kanıt olarak kabul eder.",
     "Yanıtı yok sayar ve bakiyeyi yanlışlık kabul eder.",
     "Yanıtı yönetimin yazılı açıklamasıyla destekleyerek güvenilir sayar.",
     "Teyit prosedürünü tamamen bırakıp analitik prosedürle yetinir."],
    "BDS 505 prg. 10 ve A14'e göre yanıtın doğrudan denetçiye gelmemesi gibi durumlar güvenilirlik şüphesi doğurur; "
    "denetçi ilave kanıt elde eder, örneğin teyit eden tarafla doğrudan iletişime geçerek yanıtın kaynağını ve içeriğini "
    "doğrular.", topic=KNT)

T3.q("BDS 580 prg. 19-20",
    "Yönetim, tüm işlemlerin kaydedildiğine ve finansal tablolara yansıtıldığına dair yazılı açıklamayı imzalamayı "
    f"reddetmiştir. BDS 580'e göre bu durumun denetçi raporuna etkisi aşağıdakilerden hangisidir?",
    "Görüş vermekten kaçınılır.",
    ["Olumlu görüş verilir, reddetme diğer hususlarda açıklanır.",
     "Sınırlı olumlu görüş verilir.",
     "Olumsuz görüş verilir.",
     "Olumlu görüş verilir ve yönetimin sözlü beyanı yeterli sayılır."],
    "BDS 580 prg. 19'a göre yönetim talep edilen yazılı açıklamayı sunmazsa denetçi konuyu müzakere eder ve dürüstlüğü "
    "yeniden değerlendirir; prg. 20'ye göre prg. 10-11'deki açıklamalar sunulmazsa BDS 705 uyarınca görüş vermekten "
    "kaçınılır.", topic=KNT)

T3.q("BDS 530 prg. 10, A14",
    "Denetçi, ödeme onay kontrolünü test etmek için seçtiği kalemler arasında gerektiği gibi iptal edilmiş bir çek "
    f"bulunduğunu tespit etmiştir. BDS 530'a göre bu kalemle ilgili denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "İptale ikna olursa prosedürü yerine seçilen başka bir kaleme uygular.",
    ["İptal edilen çeki sapma olarak kabul eder.",
     "İptal edilen çeki yanlışlık olarak anakitleye öngörür.",
     "Örneklemi tamamen geçersiz sayarak yeniden seçim yapar.",
     "İptal edilen çeki anomali olarak değerlendirip örneklemden çıkarır ve yerine kalem seçmez."],
    "BDS 530 prg. 10 ve A14'e göre prosedür seçilen kaleme uygulanamazsa, yerini alan başka bir kaleme uygulanır; ödemeye "
    "yetkili kişilerin onayı test edilirken usulüne uygun iptal edilmiş bir çek seçilmişse ve denetçi bunun sapma "
    "oluşturmadığına ikna olursa, yerine uygun şekilde seçilen başka bir çek incelenir.", topic=ONM, zorluk="hard")

T3.q("BDS 701 prg. 9-10",
    f"BDS 701'e göre, aşağıdakilerden hangisi kilit denetim konusu belirlenirken dikkate alınan konulardan biri değildir?",
    "Üst yönetimden sorumlu olanlara bildirilmemiş rutin bir kasa sayımı",
    ["Ciddi riskli olduğu belirlenen hasılat alanı",
     "Yüksek tahmin belirsizliği içeren şerefiye değer düşüklüğü testi",
     "Dönem içinde gerçekleşen önemli bir işletme birleşmesinin denetime etkisi",
     "Önemli yönetim yargıları içeren bir karşılık tutarına ilişkin denetçi yargıları"],
    "BDS 701 prg. 9-10'a göre kilit denetim konuları, üst yönetime bildirilen konular arasından; ciddi riskli alanlar, yüksek "
    "tahmin belirsizliği içeren yönetim yargıları ve dönemdeki önemli olay ve işlemler göz önünde bulundurularak belirlenir. "
    "Üst yönetime bildirilmemiş rutin bir işlem aday değildir.", topic=RPR)

T3.oncul("BDS 706 prg. 8, 10, A5",
    f"BDS 706'ya göre aşağıdaki hususlar değerlendirilmektedir:",
    ["Tablolarda uygun açıklanmış istisnai bir davanın sonucuna ilişkin belirsizlik",
     "Önceki dönem tablolarının başka bir denetçi tarafından denetlenmiş olması",
     "Tablolar üzerinde önemli etkisi olan yeni bir standardın erken uygulanması",
     "Tablolardaki önemli ve yaygın bir yanlışlık"],
    "Yukarıdakilerden hangileri dikkat çekilen hususlar paragrafına konu olabilir?",
    "I ve III",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "I, III ve IV"],
    "BDS 706 A5'e göre istisnai dava belirsizliği (I) ve yeni standardın erken uygulanması (III) DÇH paragrafına konu "
    "olabilir. Önceki dönemin başka denetçi tarafından denetlenmesi tablolarda sunulan bir husus olmadığından diğer hususlar "
    "paragrafına (II), önemli ve yaygın yanlışlık ise BDS 705 uyarınca olumsuz görüşe (IV) konu olur.", topic=RPR, zorluk="hard")

T3.q("BDS 560 prg. 6, 10",
    f"{TDS}, bilanço tarihinden sonraki olaylara ilişkin denetçinin sorumluluklarıyla ilgili aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Denetçi, rapor tarihinden sonra da tablolar yayımlanana kadar olayları araştırmak için prosedür uygulamakla yükümlüdür.",
    ["Denetçi, tablo tarihi ile rapor tarihi arasındaki düzeltme gerektiren tüm olayların belirlendiğine dair kanıt elde eder.",
     "Rapor tarihinden sonra raporunu değiştirebilecek bir durumu öğrenirse konuyu yönetimle müzakere eder.",
     "Rapor tarihinden sonra öğrendiği durumda tablolarda değişiklik gerekip gerekmediğine karar verir.",
     "Daha önce tatmin edici sonuç veren konularda ilave prosedür uygulaması beklenmez."],
    "BDS 560 prg. 6'ya göre denetçi tablo tarihi ile rapor tarihi arasındaki olayların belirlendiğine dair kanıt elde eder; "
    "prg. 10'a göre rapor tarihinden sonra prosedür uygulama yükümlülüğü yoktur, ancak raporunu değiştirebilecek bir "
    "durumu öğrenirse yönetimle müzakere eder ve değişiklik gerekip gerekmediğine karar verir.", topic=KNT)

T3.q("BDS 570 prg. 13",
    "Yönetim, işletmenin sürekliliğine ilişkin değerlendirmesini finansal tablo tarihinden itibaren dokuz aylık bir dönem "
    f"için yapmış ve genişletmeyi reddetmiştir. BDS 570'e göre bu duruma ilişkin aşağıdakilerden hangisi yanlıştır?",
    "Değerlendirme dönemi denetçinin sorumluluğunda olduğundan denetçi on iki aylık değerlendirmeyi kendisi yapar.",
    ["Denetçi, değerlendirmenin en az on iki ayı kapsayacak şekilde genişletilmesini talep eder.",
     "Yönetim genişletmeye istekli değilse denetçi bunun rapora etkilerini mütalaa eder.",
     "Denetçi, değerlendirilen dönemden sonrası için ciddi şüphe oluşturabilecek olaylar hakkında yönetimi sorgular.",
     "Süreklilik değerlendirmesini yapmak yönetimin sorumluluğundadır."],
    "BDS 570 prg. 13'e göre yönetimin değerlendirmesi on iki aydan kısa bir dönemi kapsıyorsa denetçi en az on iki ayı "
    "kapsayacak şekilde genişletilmesini talep eder; prg. 15 sonraki dönem sorgulamasını, prg. 24 yönetimin isteksizliğinin "
    "rapora etkisinin mütalaasını düzenler. Değerlendirme yönetimin sorumluluğudur; denetçi yerine yapmaz.", topic=KNT,
    zorluk="hard")

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
