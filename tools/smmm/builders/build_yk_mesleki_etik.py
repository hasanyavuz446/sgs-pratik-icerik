# -*- coding: utf-8 -*-
"""Meslek Hukuku · Mesleki Etik — 60 soru, 2026 test biçimi.

Dayanak: SMMM ve YMM'lerin Mesleki Faaliyetlerinde Uyacakları Etik İlkeler Hakkında Yönetmelik
(RG 19.10.2007/26675; 25.12.2012-28508 ve 08.04.2018-30385 değişiklikleri işlenmiş) ve
Ek-1 Etik İlkeler (Birinci Kısım: temel ilkeler ve kavramsal çerçeve; İkinci Kısım: bağımsız
çalışanlar; Üçüncü Kısım: bağımlı çalışanlar). 28.09.2026 kontrolü, TÜRMOB derlemesi.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_mesleki_etik_2026.json", lesson="meslek_hukuku", topic="mesleki_etik",
          konu_adi="Mesleki Etik", seed=2026092803,
          surum="Etik İlkeler Hakkında Yönetmelik ve Ek-1 Etik İlkeler (08.04.2018-30385 işlenmiş), 28.09.2026 kontrolü")

Y = "Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirlerin Mesleki Faaliyetlerinde Uyacakları Etik İlkeler Hakkında Yönetmelik’e göre"
E = "Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirlerin Mesleki Faaliyetlerinde Uyacakları Etik İlkeler Hakkında Yönetmelik’e ekli Etik İlkeler’e göre"

# ================================================================ temel ilkeler
P.q("Etik İlkeler Birinci Kısım m. 1",
    f"{Y}, aşağıdakilerden hangisi tüm meslek mensuplarının uyması zorunlu temel etik ilkelerinden biri değildir?",
    "Objektiflik",
    ["Dürüstlük", "Tarafsızlık", "Gizlilik", "Mesleki Davranış"],
    "Ek-1 Birinci Kısım m. 1 temel etik ilkelerini dürüstlük, tarafsızlık, mesleki yeterlilik ve özen, gizlilik ve "
    "mesleki davranış olarak sayar. Objektiflik ayrı bir temel ilke olarak sayılmamıştır.",
    zorluk="easy")

P.q("Etik İlkeler Birinci Kısım m. 1/b",
    f"{E}, “yanlı veya önyargılı davranarak; üçüncü kişilerin haksız ve uygunsuz biçimde yaptıkları baskıların meslek "
    "mensuplarının mesleki kararlarını etkilememesi veya engellememesi” hangi temel ilkenin tanımıdır?",
    "Tarafsızlık",
    ["Dürüstlük", "Mesleki Davranış", "Mesleki Yeterlilik ve Özen", "Gizlilik"],
    "Birinci Kısım m. 1/b bu tanımı tarafsızlık ilkesi için yapar. Dürüstlük doğru sözlü ve dürüst davranmayı, "
    "mesleki davranış yasalara uyma ve itibarı zedelememeyi ifade eder.",
    zorluk="easy")

P.q("Etik İlkeler Birinci Kısım m. 1",
    f"{E}, temel etik ilkeler ile tanımları aşağıdaki eşleştirmelerden hangisinde yanlış verilmiştir?",
    "Mesleki Davranış – Meslek mensubunun tüm mesleki ve iş ilişkilerinde doğru sözlü ve dürüst davranması",
    ["Gizlilik – Mesleki ilişki sonucu elde edilen bilginin hak veya görev olmadıkça üçüncü kişilere açıklanmaması",
     "Mesleki Yeterlilik ve Özen – Faaliyetlerin teknik ve mesleki standartlara uygun, özen ve gayretle yürütülmesi",
     "Tarafsızlık – Üçüncü kişilerin haksız ve uygunsuz baskılarının mesleki kararları etkilememesi",
     "Dürüstlük – Meslek mensubunun tüm mesleki ve iş ilişkilerinde doğru sözlü ve dürüst davranması"],
    "Doğru sözlülük ve dürüstlük, dürüstlük ilkesinin tanımıdır (m. 1/a). Mesleki davranış ise mevcut yasa ve "
    "yönetmeliklere uyulmasını ve mesleğin itibarını zedeleyecek davranışlardan kaçınılmasını ifade eder (m. 1/d).",
    zorluk="hard")

P.q("Etik İlkeler Birinci Kısım m. 11",
    f"{E}, mesleki yeterliliğin iki aşamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Elde edilmesi Kanundaki mesleğe giriş şartlarını, korunması ise gelişmelerin sürekli izlenmesini gerektirir.",
    ["Elde edilmesi Birlik sınavını, korunması ise her yıl oda tarafından yapılan yeterlik değerlendirmesini gerektirir.",
     "Elde edilmesi staj sonrası mentorluk süresini, korunması ise beş yılda bir ruhsat yenilemesini gerektirir.",
     "Elde edilmesi yüksek lisans derecesini, korunması ise uluslararası sertifika programlarını gerektirir.",
     "Elde edilmesi ve korunması, meslek mensubunun müşterisine sunduğu hizmet sayısına göre ölçülür."],
    "Birinci Kısım m. 11'e göre mesleki yeterliliğin elde edilmesi Kanunda belirtilen mesleğe giriş şartlarının "
    "sağlanmasını, korunması ise mesleki konulardaki ulusal ve uluslararası gelişmelerin sürekli izlenmesini gerektirir.")

P.q("Etik İlkeler Birinci Kısım m. 7",
    "Bağımsız çalışan meslek mensubu (A), müşterisinin kendisine ilettiği stok sayım raporunun önemli ölçüde yanıltıcı "
    f"ifadeler içerdiğini düşünmektedir. {E}, dürüstlük ilkesi uyarınca (A)'nın bu bilgiye yaklaşımı nasıl olmalıdır?",
    "Bu bilgiyi ve bu bilgiyle hazırlanmış rapor veya sonucu dikkate almamalıdır.",
    ["Bilgiyi kullanıp raporunun sonuna müşterinin sorumluluğunu belirten bir not eklemelidir.",
     "Bilgiyi kullanmalı, ancak rapor tarihini izleyen ay içinde durumu odaya bildirmelidir.",
     "Bilgiyi dikkate almadan önce müşteriden yazılı teyit almalı, teyit gelirse kullanmalıdır.",
     "Bilginin önemlilik düzeyini hesaplayıp tutar düşükse rapora olduğu gibi yansıtmalıdır."],
    "Birinci Kısım m. 7'ye göre meslek mensubu bir bilginin önemli hata veya yanıltıcı ifadeler içerdiğini düşünüyorsa "
    "bu bilgiyi veya bu bilgiyle hazırlanmış rapor, haber veya sonucu dikkate almamalıdır.")

P.q("Etik İlkeler Birinci Kısım m. 13",
    f"{E}, gizlilik ilkesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gizlilik sorumluluğu, ilişki bittikten sonra iki yıl sürer.",
    ["Gizli bilgi kişisel çıkar veya üçüncü kişilerin yararına kullanılamaz.",
     "Meslek mensubu, kontrolü altındaki elemanların da gizliliğe saygı göstermesini sağlar.",
     "Müşteri veya işveren izni ile yapılan açıklama gizlilik ihlali oluşturmaz.",
     "Kanuna aykırı bir durumu kamu otoritesine açıklamak kanun gereği açıklamadır."],
    "Birinci Kısım m. 13'e göre gizlilik sorumluluğu müşteri ya da işveren ile ilişki sona erdiği zaman bile devam eder; "
    "süreyle sınırlanmamıştır. Diğer ifadeler m. 12, 13 ve 14'te yer alır.")

P.oncul("Etik İlkeler Birinci Kısım m. 14",
    "Bir meslek mensubunun aşağıdaki açıklamaları değerlendirilmektedir:",
    ["Bir meslek odasının kalite raporuna veri sağlamak",
     "Yasal bir süreçte kendi mesleki çıkarlarını korumak amacıyla açıklama yapmak",
     "Müşterisinin rakibine, iş teklifi karşılığında müşterinin maliyet verilerini aktarmak",
     "Düzenleyici bir organın yürüttüğü soruşturmaya veri sağlamak"],
    f"{E}, yukarıdakilerden hangileri kanunun yasaklamadığı hallerde mesleki bir görev ya da hak dahilinde yapılan açıklama örnekleridir?",
    "I, II ve IV",
    ["Yalnız I", "I ve III", "II ve III", "I, II ve IV", "II, III ve IV"],
    "Birinci Kısım m. 14/c'de meslek odasının kalite raporuna veri sağlamak, düzenleyici organın soruşturmasına veri "
    "sağlamak, yasal süreçte mesleki çıkarları korumak ve standartları karşılamak için açıklama yapmak sayılmıştır. "
    "Rakibe veri aktarmak gizlilik ilkesinin açık ihlalidir.",
    zorluk="hard")

P.q("Etik İlkeler Birinci Kısım m. 15",
    f"{E}, gizli bir bilgiyi açıklama kararı verecek meslek mensubunun dikkate alması gereken hususlar arasında aşağıdakilerden hangisi sayılmamıştır?",
    "Açıklamanın meslek mensubunun ücret gelirini artırıp artırmayacağı",
    ["Açıklama hâlinde üçüncü kişiler dahil tarafların çıkarlarının zarar görüp görmeyeceği",
     "Açıklanacak bilgilerin tamamının uygun ve doğrulanmış olup olmadığı",
     "Bilginin kime ve hangi yöntemle verileceği",
     "Bilginin verileceği kişinin doğru kişi olduğundan tatmin olunması"],
    "Birinci Kısım m. 15 tarafların çıkarlarının zarar görüp görmeyeceğini, bilginin doğrulanmış olup olmadığını ve "
    "bilginin kime, hangi yöntemle verileceğini sayar. Meslek mensubunun gelir etkisi bir değerlendirme ölçütü değildir.")

P.q("Etik İlkeler Birinci Kısım m. 17",
    f"{E}, mesleki davranış ilkesi uyarınca kendisinin ve işinin tanıtımını yapan meslek mensubu için aşağıdakilerden hangisi doğru değildir?",
    "Doğrulanmamış verilerle meslektaşlarıyla karşılaştırma yapabilir.",
    ["Tanıtım sırasında dürüst ve güvenilir olmalıdır.",
     "Hizmetleri ve iş tecrübesi hakkında abartılı iddialarda bulunmamalıdır.",
     "Diğer meslek mensuplarına küçültücü atıflar yapmamalıdır.",
     "Tanıtımı yaparken mesleğe zarar vermemelidir."],
    "Birinci Kısım m. 17'ye göre meslek mensubu tanıtımda dürüst ve güvenilir olmalı, abartılı iddialarda bulunmamalı "
    "ve diğer meslek mensuplarına yönelik doğrulanmamış karşılaştırmalar ve küçültücü atıflar yapmamalıdır.")

# ================================================================ kavramsal çerçeve ve tehditler
P.q("Etik İlkeler Birinci Kısım m. 3",
    f"{Y}, aşağıdakilerden hangisi temel etik ilkelere yönelik oluşabilecek tehditlerden biri değildir?",
    "Kurumsal itibar tehdidi",
    ["Kişisel çıkar tehdidi", "Yeniden değerlendirme tehdidi", "Yıldırma amaçlı tehdit", "Taraf tutma tehdidi"],
    "Birinci Kısım m. 3 tehditleri kişisel çıkar, yeniden değerlendirme, taraf tutma, yakınlık ve yıldırma amaçlı "
    "tehditler olarak sınıflandırır. Kurumsal itibar tehdidi sayılmamıştır.",
    zorluk="easy")

P.q("Etik İlkeler Birinci Kısım m. 3/c",
    f"{E}, meslek mensubunun bir durum ya da fikri, tarafsızlığını tehlikeye düşürecek bir noktaya taşıması sonucu oluşan tehdit hangisidir?",
    "Taraf tutma tehdidi",
    ["Yakınlık tehdidi", "Yeniden değerlendirme tehdidi", "Kişisel çıkar tehdidi", "Yıldırma amaçlı tehdit"],
    "Birinci Kısım m. 3/c bu tanımı taraf tutma tehditleri için yapar. Yakınlık tehdidi üçüncü kişilerle kurulan yakın "
    "ilişkiler sonucu bu kişilerin çıkarına davranmaktan doğar.")

P.q("Etik İlkeler Birinci Kısım m. 2",
    f"{E}, kavramsal çerçeveye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Etik İlkeler, tehdit oluşturabilecek bütün durumları ve karşılık gelen önlemleri tam liste hâlinde sayar.",
    ["Saptanan tehditler önemsiz değilse, meslek mensubu bunları kaldıracak veya kabul edilebilir düzeye indirecek önlemleri uygular.",
     "Tehdidin önemi değerlendirilirken hem niteliksel hem niceliksel faktörler dikkate alınır.",
     "Uygun önlem alınamıyorsa bağımsız çalışan meslek mensubu ilgili hizmeti azaltır veya sona erdirir.",
     "İstemeden yapılan bir ihlal tespit edildiğinde kısa sürede düzeltilir ve gerekli önlemler alınır."],
    "Birinci Kısım m. 2'ye göre tehdit oluşturacak bütün durumları ve uygun davranışı belirlemek mümkün değildir; "
    "örnekler tam liste değildir ve kavramsal çerçeve bu yüzden gereklidir. Diğer ifadeler aynı maddededir.",
    zorluk="hard")

P.q("Etik İlkeler Birinci Kısım m. 2/3",
    "Bağımlı çalışan meslek mensubu (B), işveren işletmede temel etik ilkelere yönelik önemli bir tehdit saptamış, ancak "
    f"uygun önlemleri alamamaktadır. {E}, (B)'nin bu durumda yapması gereken aşağıdakilerden hangisidir?",
    "İşveren işletmedeki görevinden istifa etmelidir.",
    ["Tehdidi bir yıl izleyip sonra odaya bildirmelidir.",
     "Hizmetin kapsamını daraltarak görevine devam etmelidir.",
     "İşverenden yazılı talimat alarak görevine devam etmelidir.",
     "Durumu Birlik Etik Kuruluna bildirip kararını beklemelidir."],
    "Birinci Kısım m. 2/3'e göre uygun önlemler alınamıyorsa bağımsız çalışan meslek mensubu belirli bir hizmetin "
    "ifasını azaltmalı veya sona erdirmeli; bağımlı çalışan meslek mensubu ise işveren işletmedeki görevinden istifa "
    "etmelidir.",
    zorluk="hard")

P.q("Etik İlkeler Birinci Kısım m. 4",
    f"{Y} Ek-1’inde, tehditleri ortadan kaldıran veya kabul edilebilir bir düzeye indiren önlemler iki büyük gruba ayrılır. "
    "Aşağıdakilerden hangisi bu gruplardan biri olan mevzuat ile oluşturulabilecek önlemlere verilebilecek örneklerden biri değildir?",
    "Firmanın tek bir müşteriden elde ettiği gelirin izlenmesi",
    ["Sürekli mesleki gelişim gereksinimleri",
     "Mesleğe giriş için gerekli eğitim ve staj gereksinimleri",
     "Mesleki veya düzenleyici izleme ve disiplin prosedürleri",
     "Raporların yetkili üçüncü bir kurumca dış kontrolden geçirilmesi"],
    "Birinci Kısım m. 4/a mevzuat ile oluşturulabilecek önlemlere eğitim-staj gereksinimleri, sürekli mesleki gelişim, "
    "kurumsal yönetim, mesleki standartlar, izleme ve disiplin prosedürleri ile dış kontrolü örnek verir. Tek müşteriden "
    "gelirin izlenmesi İkinci Kısım m. 29/g'de iş çevresinde firma çapında alınabilecek önlemdir.",
    zorluk="hard")

P.q("Etik İlkeler Birinci Kısım m. 5",
    f"{E}, etik çatışmanın çözümlenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Çatışma işletme içinde çözülemezse meslek mensubu önce vergi idaresinden görüş alır.",
    ["Meslek mensubu çatışmayı temel etik ilkeleri esas alarak çözüme kavuşturur.",
     "Sorun sürerse firma veya işveren işletmedeki diğer uygun kişilerden yardım istenebilir.",
     "Çatışma çözülemezse meslek mensubu bağlı olduğu odadan mesleki öneriler alabilir.",
     "Seçenekler tükenirse meslek mensubu sözleşme ekibinden veya görevden çekilebilir."],
    "Birinci Kısım m. 5'te çözüm süreci; temel ilkeler, firma içi yardım, yönetim kurulu veya denetim komitesi ile "
    "görüşme, meslek odasından öneri alma ve son olarak görevden çekilme ya da ilişkiyi kesme olarak düzenlenmiştir. "
    "Vergi idaresinden görüş alma bir aşama olarak sayılmamıştır.")

# ================================================================ bağımsız çalışan: tehdit örnekleri (uygulama)
P.q("Etik İlkeler İkinci Kısım m. 21",
    f"{Y} Ek-1’inde yer alan etik ilkeler uyarınca, bağımsız çalışan meslek mensubu için kişisel çıkar tehdidi yaratabilecek durumlara verilebilecek örneklerden biri değildir?",
    "Müşteriden önemli değerde hediye alınması",
    ["Tek bir müşteriden alınacak toplam ücrete aşırı bağlılık",
     "Müşteriyi kaybetme olasılığını dikkate alma",
     "Güvence sağlama sözleşmesi ile ilgili şarta bağlı ücretler",
     "Müşteri tarafından istihdam edilme olasılığı"],
    "Değeri önemsiz olmayan hediye veya ayrıcalıklı hizmet alınması İkinci Kısım m. 24/ç'de yakınlık tehdidi örneğidir. "
    "Ücrete aşırı bağlılık, müşteriyi kaybetme olasılığı, şarta bağlı ücret ve istihdam edilme olasılığı m. 21'de "
    "kişisel çıkar tehdidi örnekleridir.")

P.q("Etik İlkeler İkinci Kısım m. 22/b",
    "SMMM (C), müşterisi (K) A.Ş.'nin muhasebe bilgi sistemini tasarlayıp kurmuş; bir yıl sonra aynı sistemin işleyişi "
    f"hakkında (K) A.Ş.'ye güvence raporu vermesi istenmiştir. {E}, bu durum hangi tehdidi yaratır?",
    "Yeniden değerlendirme tehdidi",
    ["Yıldırma amaçlı tehdit", "Taraf tutma tehdidi", "Yakınlık tehdidi", "Kişisel çıkar tehdidi"],
    "İkinci Kısım m. 22/b'ye göre bir finansal sistemin tasarım ve uygulamasına katıldıktan sonra sistemin işleyişi "
    "hakkında rapor verilmesi yeniden değerlendirme tehdidi örneğidir: meslek mensubu kendi işini değerlendirir.")

P.q("Etik İlkeler İkinci Kısım m. 23",
    "Bağımsız çalışan meslek mensubu (D), güvence sağlama sözleşmesi müşterisinin bir tedarikçiyle yaşadığı hukuki "
    f"uyuşmazlıkta müşteri adına taraf olarak hareket etmiştir. {E}, bu durum hangi tehdidi yaratır?",
    "Taraf tutma tehdidi",
    ["Yeniden değerlendirme tehdidi", "Yakınlık tehdidi", "Yıldırma amaçlı tehdit", "Kişisel çıkar tehdidi"],
    "İkinci Kısım m. 23/b'ye göre üçüncü taraflarla ilgili hukuki itilaf ve anlaşmazlıklarda güvence sağlama sözleşme "
    "müşterisi adına taraf olmak taraf tutma tehdidi örneğidir. Borsaya kote denetim müşterisinin kurucu hisse "
    "senedini almak da aynı maddededir.")

P.q("Etik İlkeler İkinci Kısım m. 24/c",
    "Denetim firmasından yakın zamanda ayrılan eski ortak (E), firmanın denetim müşterisi (L) A.Ş.'de finansal tablolar "
    f"üzerinde doğrudan etkisi olan finans direktörlüğüne getirilmiştir. {E}, bu durum firma açısından hangi tehdidi yaratır?",
    "Yakınlık tehdidi",
    ["Kişisel çıkar tehdidi", "Taraf tutma tehdidi", "Yıldırma amaçlı tehdit", "Yeniden değerlendirme tehdidi"],
    "İkinci Kısım m. 24/c'ye göre firmanın eski bir ortağının müşterinin yöneticisi veya sözleşme konusu üzerinde "
    "doğrudan ve önemli etki yapabilecek çalışanı olması yakınlık tehdidi örneğidir.")

P.q("Etik İlkeler İkinci Kısım m. 25",
    "Müşteri (M) A.Ş.'nin genel müdürü, bağımsız çalışan meslek mensubu (F)'ye, raporundaki bir çekinceyi kaldırmazsa "
    f"sözleşmeyi başka bir meslek mensubuna vereceğini söylemiştir. {E}, bu durum hangi tehdidi yaratır?",
    "Yıldırma amaçlı tehdit",
    ["Kişisel çıkar tehdidi", "Taraf tutma tehdidi", "Yeniden değerlendirme tehdidi", "Yakınlık tehdidi"],
    "İkinci Kısım m. 25/a'ya göre müşteri sözleşmesi ile ilgili olarak azledilme veya görevi başkasına verme ile tehdit "
    "edilmek yıldırma tehdidi örneğidir.")

P.q("Etik İlkeler İkinci Kısım m. 24 ve 25",
    f"{E}, bağımsız çalışan meslek mensubu için aşağıdaki durum–tehdit eşleştirmelerinden hangisi yanlıştır?",
    "Güvence sağlama müşterisinin yöneticisinden borç alınması – Yakınlık tehdidi",
    ["Hizmet kapsamının düşük ücret için uygunsuz biçimde daraltılması baskısı – Yıldırma tehdidi",
     "Üst düzey personel ile müşteri arasında uzun süreli arkadaşlık – Yakınlık tehdidi",
     "Ekip üyesinin daha önce o müşterinin çalışanı olması – Yeniden değerlendirme tehdidi",
     "Borsaya kote denetim müşterisinin kurucu hisse senedini almak – Taraf tutma tehdidi"],
    "Güvence sağlama müşterisinden veya yöneticilerinden borç alınması ya da onlara borç verilmesi İkinci Kısım m. 21/f'de "
    "kişisel çıkar tehdidi örneğidir. Diğer eşleştirmeler m. 25/b, 24/d, 22/ç ve 23/a ile uyumludur.",
    zorluk="hard")

P.q("Etik İlkeler İkinci Kısım m. 22",
    f"{E}, aşağıdakilerden hangisi bağımsız çalışan meslek mensubu için yeniden değerlendirme (tekrar değerlendirme) tehdidi yaratabilecek durumlardan biri değildir?",
    "Sözleşme ekibi üyesinin müşterinin muhasebe müdürüyle birinci derece akraba olması",
    ["Meslek mensubunun yaptığı işin tekrar değerlendirilmesi sırasında önemli bir hatanın tespit edilmesi",
     "Sözleşme konusu kayıtlarda kullanılan ilk verilerin meslek mensubunca hazırlanmış olması",
     "Güvence sözleşmesi ekibinden bir üyenin daha önceden o müşterinin çalışanı olması",
     "Müşteriye güvence sözleşmesinin esas konusunu doğrudan etkileyen bir hizmet sunulması"],
    "Ekip üyesinin müşterinin yöneticisi veya çalışanıyla yakın ya da birinci derece ailevi ilişkisi İkinci Kısım m. 24/a-b "
    "uyarınca yakınlık tehdididir. Diğer seçenekler m. 22'de yeniden değerlendirme tehdidi örnekleridir.",
    zorluk="hard")

P.q("Etik İlkeler İkinci Kısım m. 27 ve 29-30",
    f"{E}, aşağıdakilerden hangisi bağımsız çalışan meslek mensubu için iş çevresinde sözleşmeye özgü olarak alınabilecek önlemlerden biridir?",
    "Üst düzey güvence sağlama sözleşmesi ekibinin rotasyona tabi tutulması",
    ["Sürekli mesleki gelişim gereksinimlerinin yönetmelikle belirlenmesi",
     "Mesleğe giriş için gerekli eğitim ve staj şartlarının artırılması",
     "Mesleki veya düzenleyici izleme ve disiplin prosedürlerinin uygulanması",
     "Mesleki standartların kurumlar tarafından yayımlanması"],
    "İkinci Kısım m. 30 sözleşmeye özgü önlemleri sayar; üst düzey ekibin rotasyonu (m. 30/e) bunlardandır. Diğer "
    "seçenekler Birinci Kısım m. 4/a'daki mevzuat ile oluşturulabilecek önlemlerdir.")

P.q("Etik İlkeler İkinci Kısım m. 31",
    f"{E}, bağımsız çalışan meslek mensubunun müşterinin kendi sistem ve süreçlerindeki önlemlere güvenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Müşterinin önlemlerine de güvenebilir; ancak tehditleri indirmek için bunlarla yetinemez.",
    ["Müşterinin önlemleri kurumsal yönetişim yapısı içeriyorsa başka önlem almadan bunlara dayanabilir.",
     "Müşterinin önlemlerine güvenmesi bağımsızlığı zedeleyeceği için bu önlemleri dikkate almaz.",
     "Müşterinin önlemlerine ancak oda yönetim kurulunun onayı alınmışsa güvenebilir.",
     "Müşterinin önlemleri yeterliyse firma çapındaki önlemleri uygulamaktan vazgeçebilir."],
    "İkinci Kısım m. 31'e göre sözleşmenin özelliğine bağlı olarak müşterinin aldığı önlemlere de güvenilebilir; ancak "
    "tehditlerin kabul edilebilir düzeye indirilmesinde sadece bu önlemlere güvenilmesi mümkün değildir.")

# ================================================================ atamalar, çıkar çatışması, ikincil görüş
P.q("Etik İlkeler İkinci Kısım m. 33",
    f"{E}, müşteri kabulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Müşteri kabulüne ilişkin kararlar ilk sözleşmede verilir, yenilenen sözleşmelerde yeniden gözden geçirilmez.",
    ["Meslek mensubu, iş kabulünün temel etik ilkelere tehdit yaratmayacağından emin olmalıdır.",
     "Müşterinin para aklama gibi yasa dışı faaliyetleri temel ilkeleri tehdit eden konulardandır.",
     "Tehditler kabul edilebilir düzeye indirilemezse meslek mensubu müşteriyi kabul etmekten kaçınmalıdır.",
     "Önlem olarak müşterinin sahipleri, yöneticileri ve faaliyetleri hakkındaki bilgi geliştirilebilir."],
    "İkinci Kısım m. 33/6'ya göre müşteri kabulü ile ilgili kararlarda yenilenen sözleşmeler periyodik olarak gözden "
    "geçirilmelidir. Diğer ifadeler aynı maddenin önceki fıkralarındadır.")

P.q("Etik İlkeler İkinci Kısım m. 34",
    f"{E}, sözleşmenin kabulünde sözleşme ekibinin sözleşme şartlarını yerine getirecek yeterliliğe sahip olmaması hangi ilkeye yönelik hangi tehdidi yaratır?",
    "Mesleki yeterlilik ve özen ilkesine yönelik kişisel çıkar tehdidi",
    ["Gizlilik ilkesine yönelik yakınlık tehdidi",
     "Tarafsızlık ilkesine yönelik taraf tutma tehdidi",
     "Dürüstlük ilkesine yönelik yıldırma amaçlı tehdit",
     "Mesleki davranış ilkesine yönelik yeniden değerlendirme tehdidi"],
    "İkinci Kısım m. 34'te sözleşme ekibinin gerekli yeterliliğe sahip olmaması, mesleki yeterlilik ve özen ilkesine "
    "yönelik kişisel çıkar tehdidi örneği olarak verilmiştir.")

P.q("Etik İlkeler İkinci Kısım m. 35",
    "Başka bir meslek mensubunun yürüttüğü denetim işi için teklif vermeyi düşünen SMMM (G), mevcut meslek mensubuyla "
    f"görüşmek istemektedir. {E}, bu görüşmeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Görüşmenin kapsamı müşterinin iznine veya buna izin veren yasal ya da etik gerekliliklere bağlıdır.",
    ["Mevcut meslek mensubu, iş sahibinin izni aranmadan müşterinin bütün kayıtlarını (G)'ye aktarmakla yükümlüdür.",
     "Mevcut meslek mensubu gizlilik ilkesi nedeniyle (G) ile müşteri hakkında görüşme yapamaz.",
     "Görüşme ancak oda yönetim kurulu temsilcisinin katılımıyla yapılabilir ve tutanağa bağlanır.",
     "Görüşme yapılmadan teklif verilmesi, (G) hakkında uyarma cezası uygulanmasını gerektirir."],
    "İkinci Kısım m. 35'e göre işi alması önerilen meslek mensubu mevcut meslek mensubuyla doğrudan iletişim kurarak "
    "gerçekleri öğrenir; mevcut meslek mensubu gizlilik ilkesine uymakla yükümlü olduğundan görüşmenin kapsamı "
    "müşterinin iznine veya bu iletişime izin veren yasal ya da etik gerekliliklere bağlıdır.",
    zorluk="hard")

P.q("Etik İlkeler İkinci Kısım m. 36 ve 37",
    f"{E}, çıkar çatışmalarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Çatışan iki müşteriye, onlara bilgi vermeden hizmet verilebilir.",
    ["Meslek mensubunun müşterisinin rakibiyle ortak yatırım yapması tarafsızlık ilkesini tehdit edebilir.",
     "Çatışma yaratabilecek faaliyetler konusunda müşteriye bilgi verilip onayı alınabilir.",
     "Farklı sözleşme ekiplerinin kullanılması bir önlemdir.",
     "Firma ortakları ve çalışanlarınca imzalanan gizlilik anlaşmaları bir önlemdir."],
    "İkinci Kısım m. 37/b'ye göre çıkar çatışması içindeki iki ya da daha fazla müşteriye hizmet verilmesi hâlinde ilgili "
    "tüm taraflara bilgi verilmeli ve onayları alınmalıdır. Diğer ifadeler m. 36 ve 37'de yer alır.")

P.q("Etik İlkeler İkinci Kısım m. 39",
    "SMMM (H)'den, müşterisi olmayan (N) A.Ş. adına bir muhasebe standardının uygulanması konusunda ikincil görüş istenmiştir; "
    f"ancak (N) A.Ş. mevcut meslek mensubuyla iletişime izin vermemektedir. {E}, (H)'nin izleyeceği yol aşağıdakilerden hangisidir?",
    "Tüm koşulları dikkate alarak görüş bildirmenin uygun olup olmayacağına karar verir.",
    ["İzin verilmediği için ikincil görüş talebini reddeder.",
     "Mevcut meslek mensubuyla izin almadan görüşüp görüşünü ona göre bildirir.",
     "Görüşünü bildirip bir kopyasını ilgili odaya gönderir.",
     "Görüşünü ancak Birlik Etik Kurulunun onayını alarak bildirebilir."],
    "İkinci Kısım m. 39/3'e göre ikincil görüş isteyen müşteri mevcut meslek mensubuyla iletişime izin vermiyorsa, "
    "bağımsız çalışan meslek mensubu tüm koşulları dikkate alarak görüş bildirmenin uygun olup olmayacağına karar verir.")

# ================================================================ ücretler, hediyeler, varlıklar
P.q("Etik İlkeler İkinci Kısım m. 40",
    f"{E}, ücretlere ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Diğer meslek mensubundan daha düşük ücret istemek, kendi içinde etik dışı sayılmaz.",
    ["Diğer meslek mensubundan daha düşük ücret istemek mesleki davranış ilkesine aykırıdır.",
     "Birlikçe ilan edilen en az ücret düzeyi, meslek mensupları için bağlayıcı olmayan bir tavsiyedir.",
     "Talep edilen ücretin düzeyi, sunulan hizmetten bağımsız olarak etik bir tehdit yaratmaz.",
     "Düşük ücret talep eden meslek mensubu tarafsızlık ilkesini ihlal etmiş kabul edilir."],
    "İkinci Kısım m. 40'a göre daha düşük ücret talep etmek kendi içinde etik dışı değildir; ancak ücret çok düşükse "
    "mesleki yeterlilik ve özen ilkesine yönelik kişisel çıkar tehdidi doğabilir ve ücret Birlikçe ilan edilen asgari "
    "düzeyin altında olamaz.")

P.q("Etik İlkeler İkinci Kısım m. 42",
    f"{E}, güvence sağlama sözleşmelerinde şarta bağlı ücretten doğan tehditlere karşı alınabilecek önlemler arasında aşağıdakilerden hangisi sayılmamıştır?",
    "Şarta bağlı ücretin tutarının müşterinin yıllık cirosuna oranlanması",
    ["Müşteriyle ücret esaslarını gösteren ön anlaşma yapılması",
     "İş ve ücretlendirme esaslarının hedef kullanıcılara açıklanması",
     "Kalite kontrol politika ve süreçlerinin uygulanması",
     "Hizmetin tarafsız üçüncü bir grupça incelenmesi"],
    "İkinci Kısım m. 42/2 önlem olarak ücret esaslarını gösteren ön anlaşma, iş ve ücret esaslarının hedef kullanıcılara "
    "açıklanması, kalite kontrol politikaları ve hizmetin tarafsız üçüncü grupça incelenmesini sayar.")

P.q("Etik İlkeler İkinci Kısım m. 43",
    "SMMM (İ), belirli bir hizmeti veremediği için müşterisini başka bir meslek mensubuna yönlendirmiş ve bunun karşılığında "
    f"müşteri gönderme bedeli almıştır. {E}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Kişisel çıkar tehdidi yaratır; bu bedelin alınması uygun değildir.",
    ["Hizmet verilemediği için yönlendirme zorunludur; bedelin alınması bir tehdit yaratmaz.",
     "Bedel, müşteriye yazıyla bildirilmek koşuluyla alınabilir ve bir tehdit yaratmaz.",
     "Gizlilik ilkesine yönelik yakınlık tehdidi yaratır; bedel odaya bildirilirse alınabilir.",
     "Yıldırma tehdidi yaratır; bedelin yarısı iade edilirse tehdit ortadan kalkar."],
    "İkinci Kısım m. 43'e göre müşteri gönderme bedeli veya komisyon kabul edilmesi tarafsızlık ile mesleki yeterlilik ve "
    "özen ilkelerine yönelik kişisel çıkar tehditleri yaratabilir; meslek mensubunun bu tür ücret veya komisyonları "
    "alması veya ödemesi uygun değildir.",
    zorluk="hard")

P.q("Etik İlkeler İkinci Kısım m. 46",
    f"{E}, müşteriden hediye kabul edilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hediye teklifi, değeri ve amacı dikkate alınmaksızın reddedilmelidir.",
    ["Müşteriden hediye kabulü objektiflik ilkesine yönelik kişisel çıkar tehdidi oluşturabilir.",
     "Tehdidin önemi hediyenin özelliğine, değerine ve teklifin amacına bağlıdır.",
     "Bilgili üçüncü kişilerce önemsiz sayılan hediye iş hayatının olağan hareketi kabul edilebilir.",
     "Önlemlere rağmen tehdit giderilemezse meslek mensubu hediyeyi kabul etmemelidir."],
    "İkinci Kısım m. 46'ya göre bilgili üçüncü kişilerce önemsiz kabul edilen hediye temel ilkelere tehdit oluşturmaz; "
    "hediye ancak önlemlere rağmen tehdit giderilemezse reddedilmelidir.")

P.q("Etik İlkeler İkinci Kısım m. 47",
    "Müşterisi (P) Ltd. Şti.'nin ortakları, SMMM (J)'den şirkete ait 500.000 ₺'yi vergi ödemeleri yapılana kadar kendi "
    f"hesabında emanet olarak tutmasını istemiştir. {E}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yasal olarak izin verilmedikçe (J) müşterisine ait parayı emanet olarak alamaz.",
    ["Müşteriyle yazılı emanet sözleşmesi yapılırsa (J) parayı kendi hesabında tutabilir.",
     "Tutar asgari ücret tarifesindeki yıllık ücretin altında kalırsa emanet alınabilir.",
     "(J) parayı ancak odaya bildirerek ve ayrı bir banka hesabında tutarak alabilir.",
     "Vergi ödemeleri için alınan paralar emanet sayılmadığından (J) talebi kabul edebilir."],
    "İkinci Kısım m. 47'ye göre yasal olarak izin verilmediği sürece bağımsız çalışan meslek mensubu müşterisine ait para "
    "veya diğer varlıkları emanet olarak alamaz; ayrıca bunu yasaklayan 1996 tarihli Mecburi Meslek Kararına uymak "
    "zorundadır.")

# ================================================================ bağımsızlık
P.q("Etik İlkeler İkinci Kısım m. 53",
    f"{E}, “görünümde bağımsızlık” aşağıdakilerden hangisini ifade eder?",
    "Bilgili üçüncü kişilerin firmanın tarafsızlık ve şüpheciliğini onaylamasını",
    ["Mesleki kararın dış etkilerden bağımsız verilmesi ve meslek mensubunun şüphecilik içinde davranmasını",
     "Meslek mensubunun müşteriyle arasında herhangi bir finansal çıkar ilişkisi bulunmadığını beyan etmesini",
     "Denetim raporunun Kamu Gözetimi Kurumu tarafından onaylanarak kamuya ilan edilmesini",
     "Sözleşme ekibinin her yıl rotasyona tabi tutulması ve bunun raporda açıklanmasını"],
    "İkinci Kısım m. 53'e göre bağımsızlık fikren ve görünümde bağımsızlık olarak ikiye ayrılır. Görünümde bağımsızlık, "
    "gerekli bilgilere sahip ve önlemleri bilen üçüncü bir grubun firmanın ve ekibin dürüstlük, tarafsızlık ve mesleki "
    "şüpheciliğini onaylamasıdır. İkinci seçenek fikren bağımsızlığın tanımıdır.",
    zorluk="hard")

P.q("Etik İlkeler İkinci Kısım m. 59 ve 60",
    f"{E}, güvence sağlama sözleşmelerinde sözleşme dönemine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Finansal tablo denetiminde sözleşme dönemine finansal tabloların kapsadığı dönem de dahil edilir.",
    ["Sözleşme dönemi, güvence raporunun yayımlanmasından sonraki bir yıllık süreyi de kapsar.",
     "Sözleşme dönemi, sözleşmenin imzalandığı değil, müşterinin ilk ödemeyi yaptığı tarihte başlar.",
     "Finansal tablo denetiminde bağımsızlık, rapor tarihinden itibaren aranmaya başlanır.",
     "Sözleşme dönemi, finansal tabloların kapsadığı dönem hariç, saha çalışmasının yapıldığı süredir."],
    "İkinci Kısım m. 59'a göre sözleşme dönemi ekibin güvence hizmetlerine başlamasıyla başlar ve güvence raporunun "
    "yayımlanmasıyla sona erer; m. 60'a göre finansal tablo denetiminde bu döneme finansal tabloların kapsadığı dönem "
    "de dahil edilir.")

P.q("Etik İlkeler İkinci Kısım m. 55",
    f"{E}, güvence sağlama sözleşmelerinde yer alan üç farklı grup aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Bağımsız çalışan meslek mensubu, sorumlu taraf ve hedef kullanıcılar",
    ["Bağımsız çalışan meslek mensubu, meslek odası ve vergi idaresi",
     "Sorumlu taraf, denetim komitesi ve Kamu Gözetimi Kurumu",
     "Hedef kullanıcılar, iç denetçi ve bağımsız denetim kuruluşu",
     "Meslek mensubu, işletme ortakları ve kredi veren kuruluşlar"],
    "İkinci Kısım m. 55'e göre beyana dayalı ya da doğrudan raporlama biçimindeki güvence sağlama sözleşmelerinde üç "
    "grup vardır: bağımsız çalışan meslek mensubu, güvence sağlama sözleşmesi müşterisi (sorumlu taraf) ve hedef "
    "kullanıcılar.")

P.q("Etik İlkeler İkinci Kısım m. 58",
    f"{E}, bağımsızlığa yönelik tehditlerin varlığına rağmen güvence sağlama sözleşmesinin kabul edilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kabul kararı belgelenir; belgede saptanan tehdit ve uygulanan önlemler tanımlanır.",
    ["Kabul kararı sözlü olarak müşteriye bildirilir; belgeleme yapılmaz.",
     "Kabul için Birlik Etik Kurulunun ön izni alınır ve karar kurula gönderilir.",
     "Kabul kararı, tehdit ortadan kalkana kadar askıda tutulur ve sözleşme imzalanmaz.",
     "Kabul kararı borsaya kote işletmelerde belgelenir, diğer işletmelerde belgeleme aranmaz."],
    "İkinci Kısım m. 58/2'ye göre bağımsızlığa yönelik tehditlerin mevcut olduğu durumlarda firma sözleşmeyi kabul etme "
    "kararı verirse bu karar belgelenir ve belgede saptanan tehdit ile uygulanan önlemler tanımlanır.")

# ================================================================ bağımlı çalışanlar
P.q("Etik İlkeler Üçüncü Kısım m. 63",
    f"{E}, aşağıdakilerden hangisi bağımlı çalışan meslek mensubu için kişisel çıkar tehdidi yaratabilecek durumlara verilen örnekler arasında yer almaz?",
    "Politika anlaşmazlığı nedeniyle işten çıkarılma tehdidi",
    ["Finansal çıkar, krediler ve garantiler",
     "Şirket varlıklarının uygunsuz biçimde kişisel amaçla kullanımı",
     "İstihdam güvenliği ile ilgili endişeler",
     "İşveren dışından gelen ticari baskılar"],
    "Muhasebe politikası anlaşmazlığı nedeniyle işten çıkarılma veya işin değiştirilmesi ile tehdit edilmek Üçüncü Kısım "
    "m. 67/a'da yıldırma tehdidi örneğidir. Diğer seçenekler m. 63'te kişisel çıkar tehdidi örnekleridir.")

P.q("Etik İlkeler Üçüncü Kısım m. 65",
    f"{E}, bağımlı çalışan meslek mensubunun işverenin hedeflerini gerçekleştirmek için çalışırken işletmenin durumunu daha iyi gösterecek ifadeler kullanmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hatalı veya yanıltıcı olmaması kaydıyla bu tür ifadeler genellikle taraf tutma tehdidi yaratmaz.",
    ["Bu tür ifadeler taraf tutma tehdidi yaratır ve kullanılamaz.",
     "Bu tür ifadeler ancak bağımsız denetçinin onayı ile kullanılabilir.",
     "Bu tür ifadeler dürüstlük ilkesinin ihlali sayılır ve odaya bildirilir.",
     "Bu tür ifadeler yeniden değerlendirme tehdidi yaratır ve istifayı gerektirir."],
    "Üçüncü Kısım m. 65'e göre bağımlı çalışan meslek mensupları hatalı ya da yanıltıcı olmaması kaydıyla işletmenin "
    "durumunu daha iyi gösterecek ifadeler kullanabilir; bu tür hareketler genellikle taraf tutma tehdidi yaratmaz.")

P.q("Etik İlkeler Üçüncü Kısım m. 71 ve 72",
    "Bağımlı çalışan meslek mensubu (K)'ye genel müdür, dönem kârını hedefe ulaştırmak için bir karşılığı ayırmamasını "
    f"açıkça söylemektedir. {E}, (K)'nin bu baskıdan doğan tehdide karşı alabileceği önlemler arasında aşağıdakilerden hangisi sayılmamıştır?",
    "Karşılığı ayırmayıp denetçiye bu konuda bilgi vermemek",
    ["İşletme içinden veya meslek örgütünden tavsiye almak",
     "Bağımsız bir mesleki danışmandan tavsiye almak",
     "Yasal tavsiye almak",
     "İşletmedeki formel anlaşmazlık çözüm sürecini işletmek"],
    "Üçüncü Kısım m. 71 baskıları sayar ve m. 72 önlem olarak işletme içinden, bağımsız danışmandan veya meslek "
    "örgütünden tavsiye almayı, yasal tavsiye almayı ve formel anlaşmazlık çözüm sürecini gösterir. Denetçiyi yanlış "
    "yönlendirmek önlem değil, m. 71/ç'de sayılan baskının sonucudur.")

P.q("Etik İlkeler Üçüncü Kısım m. 74",
    f"{E}, bağımlı çalışan meslek mensubunun yanıltıcı bilgi sunumunun önemli derecede ve sürekli olduğu durumlarda yapması gerekenlere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Durumu ilgili otoritelere bildirir; yasal tavsiye alabilir veya istifa edebilir.",
    ["Durumu gizlilik ilkesi nedeniyle otoritelere bildirmez; işverene yazılı ihtarda bulunmakla yetinir.",
     "Durumu bir sonraki olağan genel kurulda ortaklara açıklar ve görevine devam eder.",
     "Yanıltıcı bilgiyle ilişkisini sürdürür; sorumluluk işletme yönetimine aittir.",
     "Durumu meslek odasına bildirir; oda izin verene kadar istifa edemez."],
    "Üçüncü Kısım m. 74/3'e göre tehdit makul düzeye indirilemezse meslek mensubu yanıltıcı bilgiyle ilişkisini "
    "sürdürmeyi reddedebilir; yanıltıcı sunum önemli ve sürekliyse ilgili otoritelere bildirme yükümlülüğü vardır ve "
    "yasal tavsiye alabilir veya istifa edebilir.",
    zorluk="hard")

P.q("Etik İlkeler Üçüncü Kısım m. 76",
    f"{E}, aşağıdakilerden hangisi bağımlı çalışan meslek mensubunun görevlerini mesleki yeterlilik ve özen içinde yerine getirmesini tehdit eden durumlara verilen örnekler arasında yer almaz?",
    "Meslek mensubunun kâr üzerinden prim alması",
    ["Görevler için yeterli zaman verilmemesi",
     "Gerekli bilgilerin eksik veya sınırlı olması",
     "Yetersiz deneyim ve eğitim",
     "Kullanılacak kaynakların yetersizliği"],
    "Kâr üzerinden prim alınması Üçüncü Kısım m. 79/b'de finansal çıkarlardan doğan kişisel çıkar tehdidi örneğidir. "
    "Diğer seçenekler m. 76'da mesleki yeterlilik ve özeni tehdit eden durumlardır.")

P.q("Etik İlkeler Üçüncü Kısım m. 84 ve 85",
    f"{E}, bağımlı çalışan meslek mensubuna teşvik teklif edilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tehdit teşvikin kabulüyle doğar; teklifin yapılmış olması tek başına ek önlem gerektirmez.",
    ["Teşvikler hediye, ağırlama veya ayrıcalıklı davranış biçiminde olabilir.",
     "Kararları etkileme amaçlı teşvik tarafsızlık ve gizliliğe yönelik kişisel çıkar tehdidi yaratır.",
     "Tehditler giderilemiyorsa meslek mensubu teşviki kabul etmemelidir.",
     "Teklif yapıldığında üst yönetime veya yönetişimden sorumlulara bilgi verilebilir."],
    "Üçüncü Kısım m. 85'e göre gerçek tehditler sadece teşvikin kabul edilmesinden kaynaklanmaz; bazen yalnız teklifin "
    "yapılmış olması bile ilave önlem alınmasını gerektirebilir.")

P.q("Etik İlkeler Üçüncü Kısım m. 62/3",
    f"{E}, bağımlı çalışan meslek mensubunun işveren işletme ile ilişkisinin yasal biçiminin etik sorumluluklarına etkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlişkinin yasal biçimi, uyulması gereken etik sorumluluklar üzerinde bir etki yapmaz.",
    ["Gönüllü olarak çalışanlar etik ilkelerin Üçüncü Kısmına tabi değildir.",
     "İşletmenin sahibi olan meslek mensubu mesleki davranış dışındaki ilkelerden muaftır.",
     "Ortak sıfatıyla çalışanlar bağımsız çalışanlara ilişkin kurallara tabidir.",
     "Maaşlı işgörenler için gizlilik ilkesi işverenin izniyle kaldırılabilir."],
    "Üçüncü Kısım m. 62/3'e göre bağımlı çalışan meslek mensubu maaşlı işgören, ortak, yönetici, işletme sahibi veya "
    "gönüllü olabilir; işveren işletme ile ilişkisinin yasal biçimi uyması gereken etik sorumluluklar üzerinde bir "
    "etki yapmaz.")

P.q("Etik İlkeler Üçüncü Kısım m. 87",
    f"{E}, bağımlı çalışan meslek mensubunun üçüncü bir grubun mesleki kararını uygunsuz biçimde etkileyecek bir teşvik vermeyi teklif etmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bağımlı çalışan meslek mensubu bu tür bir teşvik vermeyi teklif edemez.",
    ["Teşvik, işverenin yazılı talimatına dayanıyorsa teklif edilebilir.",
     "Teşvikin değeri önemsizse, amacına bakılmaksızın teklif edilebilir.",
     "Teşvik teklifi ancak yönetim kuruluna önceden bilgi verilerek yapılabilir.",
     "Teşvik teklifi, rakip işletmelerin de benzer uygulaması varsa yapılabilir."],
    "Üçüncü Kısım m. 87'ye göre bağımlı çalışan meslek mensubu üçüncü bir grubun mesleki kararını uygunsuz biçimde "
    "etkileyecek bir teşvik vermeyi teklif edemez; baskı işletme içinden geliyorsa m. 88 uyarınca etik çatışma çözüm "
    "süreci işletilir.")

# ================================================================ Etik Kurulu (Yönetmelik ana metni)
P.sayisal("Etik İlkeler Hakkında Yönetmelik m. 5 (08.04.2018 değişikliği)",
    f"{Y}, TÜRMOB Yönetim Kurulu tarafından atanan Etik Kurulu en fazla kaç üyeden oluşur?",
    "11", ["5", "7", "9", "15"],
    "Yönetmelik m. 5'e göre Etik Kurulu, meslek mensupları arasından Birlik Yönetim Kurulunca atanan, biri başkan, biri "
    "başkan yardımcısı ve biri sekreter olmak üzere en az yedi, en fazla 11 üyeden oluşur.")

P.q("Etik İlkeler Hakkında Yönetmelik m. 5 ve 6",
    f"{Y}, Etik Kurulu üyelerinin görev süresi ve kurulun toplanma sıklığı aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Birlik Yönetim Kurulunun görev süresiyle sınırlı olmak üzere üç yıl; ayda en az bir kez",
    ["Birlik Yönetim Kurulunun görev süresiyle sınırlı olmak üzere iki yıl; üç ayda en az bir kez",
     "Birlik Genel Kurulunun görev süresiyle sınırlı olmak üzere dört yıl; ayda en az bir kez",
     "Oda yönetim kurullarının görev süresiyle sınırlı olmak üzere üç yıl; iki ayda en az bir kez",
     "Görev süresi sınırsız olmak üzere; yılda en az dört kez"],
    "Yönetmelik m. 5'e göre üyelerin görev süresi TÜRMOB Yönetim Kurulunun görev süresi ile sınırlı olmak üzere üç yıldır; "
    "m. 6'ya göre Etik Kurulu düzenli olarak ayda en az bir kez toplanır.")

P.q("Etik İlkeler Hakkında Yönetmelik m. 7",
    f"{Y}, aşağıdakilerden hangisi Etik Kurulunun görev ve yetkileri arasında yer almaz?",
    "Etik ilkeleri ihlal eden meslek mensuplarına disiplin cezası vermek",
    ["Etik ilke ve uygulamalarına ilişkin tebliğ ve sirküler taslakları hazırlamak",
     "Mesleki etiğin yaygınlaştırılması için eğitim programları hazırlamak",
     "Meslekte etik kültürünü yerleştirmek üzere çalışmalar yapmak",
     "Odalardan gelen ihlal başvurularını inceleyip sonuçları bildirmek"],
    "Yönetmelik m. 7'ye göre Etik Kurulu taslak hazırlar, eğitim programı geliştirir, etik kültürünü yerleştirir ve "
    "odalardan gelen başvuruları inceleyip sonuçlarını Birlik Yönetim Kurulu aracılığıyla odalara bildirir. Disiplin "
    "cezası vermek disiplin kurullarının görevidir.")

P.q("Etik İlkeler Hakkında Yönetmelik m. 2 ve 4",
    f"{Y}, Yönetmeliğin kapsamına ve tanımlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetmelik, çalışanlar listesine kayıtlı bağımsız çalışanlarla sınırlı olarak uygulanır.",
    ["Bağımlı veya bağımsız çalışan tüm meslek mensupları ile kurdukları şirketler kapsamdadır.",
     "Şarta bağlı ücret, hizmet veya işlemin sonucuna göre sonradan hesaplanan ücrettir.",
     "Bağımlı çalışan meslek mensubu, iş sahibine ücret karşılığı hizmet veren meslek mensubudur.",
     "Sözleşme ortağı, belli bir sözleşme ve rapordan sorumlu ortak ya da kişilerdir."],
    "Yönetmelik m. 2'ye göre meslek unvanına sahip, bağımsız veya bağımlı çalışan tüm meslek mensupları ile kurdukları "
    "şirketler kapsamdadır; Ek-1'in Üçüncü Kısmı bağımlı çalışanlara ayrılmıştır. Diğer tanımlar m. 4'tedir.")

P.q("Etik İlkeler Hakkında Yönetmelik Ek Madde 1",
    f"{Y}, Uluslararası Muhasebeciler Federasyonu (IFAC) tarafından Uluslararası Etik Standartlarında yapılan değişikliklerle ilgili aşağıdakilerden hangisi doğrudur?",
    "Değişiklikler TÜRMOB tarafından meslek mensuplarına duyurulur.",
    ["Değişiklikler Resmî Gazete'de yayımlanmadıkça meslek mensuplarına duyurulmaz.",
     "Değişiklikler Kamu Gözetimi Kurumu kararıyla doğrudan Yönetmeliğe eklenir.",
     "Değişiklikler her oda yönetim kurulu tarafından ayrı ayrı onaylanarak uygulanır.",
     "Değişiklikler Hazine ve Maliye Bakanlığınca tebliğle ilan edilerek yürürlüğe girer."],
    "Yönetmeliğin 25.12.2012'de eklenen Ek Madde 1'ine göre IFAC tarafından Uluslararası Etik Standartlarında yapılan "
    "değişiklikler TÜRMOB tarafından meslek mensuplarına duyurulur.")

P.oncul("Etik İlkeler Birinci Kısım m. 3",
    "Temel etik ilkelere yönelik tehditlerle ilgili aşağıdaki tanımlar verilmiştir:",
    ["Meslek mensubunun veya yakın ailesinden bir üyenin finansal ya da diğer çıkarlarından doğan tehdit kişisel çıkar tehdididir.",
     "Önceden alınmış bir kararın o karardan sorumlu meslek mensubunca yeniden değerlendirilmesinden doğan tehdit yeniden değerlendirme tehdididir.",
     "Meslek mensubunun gerçek veya hissedilen tehditler nedeniyle tarafsız davranmaktan kaçınmaya zorlanması yakınlık tehdididir.",
     "Üçüncü kişilerle kurulan yakın ilişkiler sonucu bu kişilerin çıkarına davranılması taraf tutma tehdididir."],
    f"{E}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve II",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, II ve IV"],
    "Birinci Kısım m. 3'e göre I ve II doğrudur. Gerçek veya hissedilen tehditlerle tarafsız davranmaktan kaçınmaya "
    "zorlanma yıldırma amaçlı tehdit (m. 3/d), üçüncü kişilerle yakın ilişki sonucu onların çıkarına davranma yakınlık "
    "tehdididir (m. 3/ç).",
    zorluk="hard")

P.oncul("Etik İlkeler İkinci Kısım m. 50",
    "Bağımsız çalışan meslek mensubunun sunduğu bir hizmette tarafsızlığa yönelik tehditlere karşı aşağıdaki önlemler düşünülmektedir:",
    ["Sözleşme ekibinden çekilme",
     "Tehdide neden olan finansal veya iş ilişkisinin ortadan kaldırılması",
     "Konunun müşterinin yönetiminden sorumlu kişilerle tartışılması",
     "Hizmet ücretinin şarta bağlı ücrete dönüştürülmesi"],
    f"{E}, yukarıdakilerden hangileri tarafsızlığa yönelik tehditlere karşı alınabilecek önlemler arasında sayılmıştır?",
    "I, II ve III",
    ["Yalnız I", "I ve IV", "II ve III", "I, II ve III", "II, III ve IV"],
    "İkinci Kısım m. 50/2 önlemler olarak sözleşme ekibinden çekilme, gözetim süreçleri, tehdide neden olan ilişkinin "
    "kaldırılması, konunun firma içinde üst düzeyde ve müşterinin yönetiminden sorumlu kişilerle tartışılmasını sayar. "
    "Şarta bağlı ücret ise m. 42'ye göre kendisi bir tehdit kaynağıdır.")

P.q("Etik İlkeler İkinci Kısım m. 61",
    "Denetim firması, (R) A.Ş.'ye finansal tabloların kapsadığı dönem içinde ancak denetim hizmeti başlamadan önce "
    f"güvence amaçlı olmayan bir danışmanlık hizmeti vermiştir. {E}, bu hizmete ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hizmet denetim süresince verilmemeli ve bağımsızlık tehditleri değerlendirilmelidir.",
    ["Hizmet denetimden önce verildiği için bağımsızlık açısından değerlendirme gerektirmez.",
     "Hizmeti veren personelin denetim ekibinde yer alması bağımsızlığı güçlendirir.",
     "Hizmetin ifası denetim süresince sürdürülebilir; rapora açıklama notu eklenmesi yeterlidir.",
     "Hizmet bedeli denetim ücretinden mahsup edilirse tehdit ortadan kalkar."],
    "İkinci Kısım m. 61'e göre bu durumda hizmetin ifası denetim sözleşmesi süresince yasaklanmalı ve bağımsızlık "
    "tehditleri dikkate alınmalıdır; önlem olarak konunun denetim komitesiyle tartışılması, müşterinin sorumluluk onayı "
    "ve bu hizmeti veren personelin denetimde görev almaması sayılmıştır.",
    zorluk="hard")

P.q("Etik İlkeler Birinci Kısım m. 11/3 ve 16",
    f"{E}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Meslek mensubu, altında çalışanların eğitimini ve gözetimini sağlamalıdır.",
    ["Meslek mensubunun çalışanlarının eğitimi, işverenin değil odanın sorumluluğundadır.",
     "Mesleki davranış ilkesi, meslek mensubunun müşterisine karşı davranışlarıyla sınırlıdır.",
     "Mesleğin itibarını zedeleyecek davranış, meslek mensubunun kendi değerlendirmesiyle belirlenir.",
     "Mesleki özen, hizmetin müşterinin istediği sürede tamamlanmasını ifade eder."],
    "Birinci Kısım m. 11/3'e göre meslek mensubu, otoritesi altında çalışanların uygun mesleki eğitim almasını ve gözetim "
    "altında tutulmasını sağlar. M. 16'ya göre itibarı zedeleyecek davranışlar, gerekli bilgilere sahip üçüncü kişilerce "
    "de mesleğin adını olumsuz etkileyeceği düşünülen davranışları kapsar.")

P.q("Etik İlkeler Birinci Kısım m. 13/2",
    f"{E}, meslek mensubunun kontrolü altında çalışan elemanların ve danışmanlık aldığı üçüncü kişilerin gizlilik ilkesine uymasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Meslek mensubu bu kişilerin gizlilik ilkesine saygı göstermesini sağlamakla yükümlüdür.",
    ["Bu kişilerin gizlilik yükümlülüğü, meslek mensubu ile aralarındaki sözleşmeye bırakılmıştır.",
     "Bu kişiler meslek mensubu olmadıkları için gizlilik ilkesi kapsamında değerlendirilmez.",
     "Bu kişilerin gizliliğe uyup uymadığını odanın haksız rekabet kurulu denetler.",
     "Bu kişilerin gizlilik ihlalinden meslek mensubu değil, ihlali yapan kişi sorumlu tutulur."],
    "Birinci Kısım m. 13/2'ye göre meslek mensubu, kendi kontrolü altında çalışan elemanların ve danışmanlık veya tavsiye "
    "hizmeti aldığı diğer meslek mensuplarının veya üçüncü kişilerin gizlilik ilkesinin gereklerine saygı göstermelerini "
    "sağlamakla yükümlüdür.")

P.q("Etik İlkeler İkinci Kısım m. 29",
    f"{E}, aşağıdakilerden hangisi bağımsız çalışan meslek mensubu için iş çevresinde firma çapında alınabilecek önlemlerden biri değildir?",
    "Güvence sağlama müşterisinin kurucu hisse senetlerinin firma ortaklarınca satın alınması",
    ["Tek bir müşteriden elde edilen gelirin izlenmesini sağlayacak politika ve süreçler",
     "Kalite güvence sisteminin yeterliliğinden sorumlu bir üst yöneticinin görevlendirilmesi",
     "Politika ve süreçlere uyum için gerekli disiplin mekanizmasının kurulması",
     "Güvence dışı hizmetlerde farklı ortak ve sözleşme ekiplerinin kullanılması"],
    "İkinci Kısım m. 29 firma çapındaki önlemleri sayar: gelir bağımlılığının izlenmesi, kalite güvenceden sorumlu üst "
    "yönetici, disiplin mekanizması, güvence dışı hizmetlerde ayrı ekipler bunlardandır. Denetim müşterisinin kurucu "
    "hisse senedini almak ise m. 23/a'da taraf tutma tehdidi örneğidir.",
    zorluk="hard")

P.q("Etik İlkeler İkinci Kısım m. 34/2",
    f"{E}, sözleşme kabulünde mesleki yeterlilik ve özen ilkesine yönelik tehditleri azaltmak için alınabilecek önlemler arasında aşağıdakilerden hangisi sayılmamıştır?",
    "Sözleşme ücretinin asgari tarifenin iki katı olarak belirlenmesi",
    ["Gerekli yeterliliğe sahip personelin atanması",
     "Gerekli olduğunda uzman kullanılması",
     "Sözleşmenin gerçekçi bir zaman diliminde yerine getirilmesi",
     "Müşterinin işi ve faaliyetlerinin karmaşıklığı hakkında yeterli bilgi sahibi olmak"],
    "İkinci Kısım m. 34/2 önlemleri müşterinin işi hakkında yeterli bilgi, raporlama usullerinde deneyim, yeterli personel "
    "atanması, uzman kullanımı, gerçekçi zaman dilimi ve kalite güvence sistemi olarak sayar. Ücret düzeyi bir önlem "
    "olarak sayılmamıştır.")

P.q("Etik İlkeler Üçüncü Kısım m. 69",
    f"{E}, aşağıdakilerden hangisi bağımlı çalışan meslek mensubu için iş çevresinde alınabilecek önlemlere verilen örnekler arasında yer almaz?",
    "Meslek mensubunun primini, raporladığı kârla doğrudan ilişkilendiren ücret politikası",
    ["İşverenin şirket gözetim ve kontrol yapıları",
     "İşverenin etik ve davranış programları",
     "Güçlü iç kontrol uygulamaları",
     "Çalışanların etik sorunları cezalandırılma korkusu duymadan üst yönetime iletebilmesi"],
    "Üçüncü Kısım m. 69 önlem olarak gözetim ve kontrol yapıları, etik ve davranış programları, güçlü iç kontrol, uygun "
    "disiplin süreçleri ve çalışanların etik sorunları cezalandırılma korkusu olmadan iletebilmesini sayar. Kârla "
    "doğrudan ilişkili prim ise m. 79/b'de kişisel çıkar tehdidi örneğidir.",
    zorluk="hard")

P.q("Etik İlkeler Üçüncü Kısım m. 78",
    "Bağımlı çalışan meslek mensubu (L)'ye, yeterli deneyimi olmadığı karmaşık bir türev ürün değerlemesi verilmiş; ek "
    f"eğitim ve uzman desteği de sağlanamamıştır. {E}, (L)'nin izleyebileceği yol aşağıdakilerden hangisidir?",
    "Kuşku duyduğu bu görevi yerine getirmeyi kabul etmeyebilir ve kararının nedenlerini açıklar.",
    ["Görevi üstlenir; deneyim eksikliğini işverene bildirmesi gerekmez.",
     "Görevi üstlenir ve sonuç raporunda sorumluluğun işverene ait olduğunu belirtir.",
     "Görevi reddeder ancak nedenini gizlilik ilkesi gereği açıklamaz.",
     "Görevi, meslek odasından yazılı izin alana kadar askıya alır."],
    "Üçüncü Kısım m. 75'e göre meslek mensubu yalnızca yeterli eğitim ve deneyimi olan görevleri üstlenmelidir; m. 78'e "
    "göre tehditler giderilemiyorsa kuşku duyduğu görevi yerine getirmeyi kabul etmeyebilir ve bu kararının "
    "nedenlerini açıklar.")

if __name__ == "__main__":
    sys.exit(P.yaz())
