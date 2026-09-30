# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Denetim Kanıtı — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında denetim kanıtının yeterliliği ve uygunluğu (“daha fazla kanıt düşük kaliteyi
telafi etmez”) ile yazılı beyanlara ilişkin öncüllü soru yer almıştır.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · BDS 500 Denetim Kanıtları; BDS 501 Belirli Kalemler; BDS 505 Dış Teyitler; BDS 520 Analitik Prosedürler
  · BDS 550 İlişkili Taraflar; BDS 560 Bilanço Tarihinden Sonraki Olaylar; BDS 570 İşletmenin Sürekliliği
  · BDS 580 Yazılı Açıklamalar; BDS 620 Denetçinin Faydalandığı Uzmanın Çalışmalarının Kullanılması
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_denetim_kaniti_2026.json", lesson="denetim", topic="denetim_kaniti",
          konu_adi="Denetim Kanıtı", seed=2026092845,
          surum="BDS 500, 501, 505, 520, 550, 560, 570, 580, 620 güncel metinleri; 28.09.2026 kontrolü")

B500 = "BDS 500 “Bağımsız Denetim Kanıtları”na göre"
B501 = "BDS 501 “Belirli Kalemlere İlişkin Denetim Kanıtları”na göre"
B505 = "BDS 505 “Dış Teyitler”e göre"
B520 = "BDS 520 “Analitik Prosedürler”e göre"
B550 = "BDS 550 “İlişkili Taraflar”a göre"
B560 = "BDS 560 “Bilanço Tarihinden Sonraki Olaylar”a göre"
B570 = "BDS 570 “İşletmenin Sürekliliği”ne göre"
B580 = "BDS 580 “Yazılı Açıklamalar”a göre"
B620 = "BDS 620 “Denetçinin Faydalandığı Uzmanın Çalışmalarının Kullanılması”na göre"

# ================================================================ BDS 500: yeterlilik, uygunluk, güvenilirlik
P.q("BDS 500 A4-A5",
    f"{B500}, denetim kanıtının yeterliliği ve uygunluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Daha fazla kanıt elde edilmesi, düşük kaliteli kanıtın yetersizliğini giderir.",
    ["Yeterlilik kanıtın miktarının, uygunluk ise kanıtın kalitesinin ölçütüdür.",
     "İhtiyaç duyulan kanıt miktarı, önemli yanlışlık riski değerlendirmesinden ve kanıtın kalitesinden etkilenir.",
     "Risk ne kadar yüksek değerlendirilirse genellikle o kadar fazla kanıt gerekir.",
     "Kanıtın kalitesi arttıkça daha az kanıt gerekebilir; uygunluk ihtiyaca uygunluk ve güvenilirliği kapsar."],
    "BDS 500 A4-A5'e göre yeterlilik miktarın, uygunluk ise ihtiyaca uygunluk ve güvenilirlik bakımından kalitenin "
    "ölçütüdür; gerekli miktar risk değerlendirmesinden ve kanıtın kalitesinden etkilenir. Ancak daha fazla kanıt elde "
    "edilmesi düşük olan kaliteyi telafi etmeyebilir.")

P.q("BDS 500 A31",
    f"{B500}, denetim kanıtının güvenilirliğine ilişkin genellemelerden hangisi yanlıştır?",
    "Sorgulama yoluyla elde edilen kanıt, kontrolün uygulanmasının gözlemlenmesinden daha güvenilirdir.",
    ["İşletme dışındaki bağımsız kaynaklardan elde edilen kanıtın güvenilirliği artar.",
     "Kanıtın hazırlanması ve korunması üzerindeki kontroller etkinse işletme içi kanıtın güvenilirliği artar.",
     "Belge şeklindeki kanıt, sözlü olarak elde edilen kanıttan daha güvenilirdir.",
     "Orijinal belgelerle sağlanan kanıt, fotokopi veya faks gibi kopyalardan daha güvenilirdir."],
    "BDS 500 A31'e göre dış bağımsız kaynaklardan, etkin kontrollerle korunan kaynaklardan, belge şeklinde ve orijinal "
    "belgelerle elde edilen kanıt daha güvenilirdir. Doğrudan denetçi tarafından elde edilen kanıt (ör. gözlem), dolaylı "
    "veya çıkarım yoluyla elde edilen kanıttan (ör. sorgulama) daha güvenilirdir.")

P.q("BDS 500 A31",
    "Bir işletmenin ticari alacaklarına ilişkin bakiye, müşterinin denetçiye doğrudan gönderdiği bir teyit mektubuyla "
    "doğrulanmıştır. Ancak denetçi, teyit eden müşterinin işletmenin ilişkili tarafı olduğunu ve konuya ilişkin yeterli "
    f"bilgisi olmadığını öğrenmiştir. {B500} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Dış kaynaktan alınsa da kaynağın bilgisi ve tarafsızlığı kanıtın güvenilirliğini zayıflatabilir.",
    ["Dış kaynaktan elde edilen kanıt, kaynağın niteliğine bakılmaksızın en güvenilir kanıttır.",
     "Teyit doğrudan denetçiye geldiği için teyit edenin ilişkili taraf olmasının ve bilgisinin bir önemi yoktur.",
     "İlişkili taraftan gelen teyitler denetim kanıtı olarak kullanılamaz ve dosyadan çıkarılır.",
     "Denetçi, teyidi yönetimin yazılı açıklamasıyla destekleyerek en güvenilir kanıt hâline getirir."],
    "BDS 500 A31'e göre güvenilirliğe ilişkin genellemeler önemli istisnalara tabidir; işletme dışından elde edilen bilgi "
    "de kaynağın yeterli bilgiye sahip olmaması veya tarafsız olmaması durumunda güvenilir olmayabilir. Prg. 11 "
    "güvenilirlik şüphesi hâlinde prosedürlerde değişiklik veya ekleme yapılmasını ister.", zorluk="hard")

P.q("BDS 500 A14-A25",
    "Denetçi, işletmenin sabit kıymet amortisman hesaplamasını, işletmenin kullandığı yöntem ve oranlarla bağımsız "
    f"olarak kendisi yeniden hesaplamıştır. {B500} bu prosedür aşağıdakilerden hangisidir?",
    "Yeniden hesaplama",
    ["Yeniden uygulama", "Analitik prosedür", "Tetkik (inceleme)", "Gözlem"],
    "BDS 500 A23'e göre yeniden hesaplama, belge veya kayıtların matematiksel doğruluğunun kontrol edilmesidir. Yeniden "
    "uygulama ise işletmenin iç kontrolünün bir parçası olarak uygulanan prosedür veya kontrollerin denetçi tarafından "
    "bağımsız biçimde tekrar uygulanmasıdır (A24).", zorluk="easy")

P.q("BDS 500 A24",
    "Denetçi, işletmede her ay yapılan banka mutabakatı kontrolünün etkin işleyip işlemediğini test etmek için seçtiği "
    f"üç ayın banka mutabakatını bağımsız olarak kendisi yeniden yapmıştır. {B500} bu prosedür aşağıdakilerden "
    "hangisidir?",
    "Yeniden uygulama",
    ["Yeniden hesaplama", "Dış teyit", "Analitik prosedür", "Sorgulama"],
    "BDS 500 A24'e göre yeniden uygulama, işletme iç kontrolünün bir parçası olarak uygulanan prosedür veya kontrollerin "
    "denetçi tarafından bağımsız olarak tekrar uygulanmasıdır. Banka mutabakatının denetçi tarafından yeniden yapılması "
    "kontrol testi olarak yeniden uygulamaya örnektir.")

P.q("BDS 500 A18",
    f"{B500}, gözlem prosedürüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gözlemden elde edilen kanıt, gözlemin yapıldığı an dışındaki dönemi de kanıtlar.",
    ["Gözlem, başkaları tarafından uygulanan bir süreç veya prosedürün izlenmesidir.",
     "Stok sayımının denetçi tarafından izlenmesi gözleme örnektir.",
     "Kontrol faaliyetlerinin uygulanmasının izlenmesi de gözlem kapsamındadır.",
     "Gözlem kanıtı, kişilerin gözlemlendiklerini bilmeleri nedeniyle sınırlı olabilir."],
    "BDS 500 A18'e göre gözlem, başkaları tarafından uygulanan süreç veya prosedürün izlenmesidir; stok sayımı ve kontrol "
    "faaliyetlerinin izlenmesi örnektir. Gözlem, gözlemin yapıldığı zamanla sınırlı kanıt sağlar ve gözlemlendiğini bilen "
    "kişilerin davranışı nedeniyle sınırlanabilir.")

P.q("BDS 500 A22",
    f"{B500}, sorgulama prosedürüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sorgulama tek başına önemli yanlışlık bulunmadığına dair yeterli kanıt sağlamaz.",
    ["Sorgulama yazılı yapılmışsa tek başına yeterli ve uygun kanıt sağlar.",
     "Sorgulama sadece yönetime yöneltilebilir; işletme dışındaki kişiler sorgulanamaz.",
     "Sorgulamaya verilen cevaplar diğer kanıtlarla çelişse de denetçi cevapları esas alır.",
     "Sorgulama sadece risk değerlendirme aşamasında, yönetim beyanlarını test etmek için kullanılır."],
    "BDS 500 A22'ye göre sorgulama, işletme içinden veya dışından bilgili kişilerden bilgi talep edilmesidir ve denetim "
    "boyunca kullanılır; ancak tek başına yönetim beyanı düzeyinde önemli yanlışlığın bulunmadığına ya da kontrollerin "
    "etkinliğine dair yeterli kanıt sağlamaz. Çelişkili cevaplar prosedürlerin değiştirilmesini gerektirebilir.")

P.q("BDS 500 prg. 8",
    "İşletme, yatırım amaçlı gayrimenkullerinin gerçeğe uygun değerini belirlemek için bir değerleme uzmanıyla çalışmıştır. "
    f"{B500} denetçinin bu uzmanın çalışmasını kanıt olarak kullanmadan önce yapması gerekenler arasında aşağıdakilerden "
    "hangisi yer almaz?",
    "Uzmanın değerini kabul etmeden önce ayrıca bir değerleme şirketi tutmak",
    ["Uzmanın yeterliğini, kabiliyetini ve tarafsızlığını değerlendirmek",
     "Uzmanın çalışmasını anlamak",
     "Uzman çalışmasının ilgili yönetim beyanı için kanıt olarak uygunluğunu değerlendirmek",
     "Uzmanın çalışmasının önemini dikkate alarak bu değerlendirmelerin kapsamını belirlemek"],
    "BDS 500 prg. 8'e göre yönetimin faydalandığı uzmanın çalışması kanıt olarak kullanılacaksa denetçi, çalışmanın "
    "önemini dikkate alarak uzmanın yeterliğini, kabiliyetini ve tarafsızlığını değerlendirir, çalışmasını anlar ve "
    "kanıt olarak uygunluğunu değerlendirir. Ayrı bir değerleme şirketi tutmak zorunlu değildir.", zorluk="hard")

P.q("BDS 500 prg. 9",
    "Denetçi, işletmenin ERP sisteminden aldığı yaşlandırılmış alacak listesini şüpheli alacak karşılığı testinde "
    f"kullanacaktır. {B500} denetçinin bu listeye ilişkin yapması gereken aşağıdakilerden hangisidir?",
    "Listenin doğruluğu ve tamlığı hakkında kanıt elde eder, ayrıntısını değerlendirir.",
    ["İşletmenin sisteminden alındığı için listeyi test etmeden kullanır.",
     "Listeyi kullanamaz; kendi alacak listesini baştan oluşturur.",
     "Listenin doğruluğu için sadece bilgi işlem müdürünün sözlü teyidini alır.",
     "Listeyi, yönetimin yazılı açıklamasıyla desteklediği sürece test etmeden kabul eder."],
    "BDS 500 prg. 9'a göre işletme tarafından oluşturulan bilgi kullanılacaksa denetçi, bilginin yeterince güvenilir "
    "olup olmadığını değerlendirir; bunun için gerekli ölçüde bilginin doğruluğu ve tamlığı hakkında kanıt elde eder ve "
    "amacına uygun kesinlik ve ayrıntıda olup olmadığını değerlendirir.")

P.q("BDS 500 prg. 10, A52",
    f"{B500}, test edilecek kalemlerin seçilmesinde kullanılabilecek yöntemler arasında aşağıdakilerden hangisi yer "
    "almaz?",
    "Yönetimin denetçiye önerdiği kalemlerin test edilmesi",
    ["Tüm kalemlerin seçilmesi (yüzde yüz inceleme)",
     "Belirli kalemlerin seçilmesi",
     "Denetim örneklemesi",
     "Tutarı belirli bir sınırın üzerindeki kalemlerin seçilmesi"],
    "BDS 500 prg. 10 ve A52'ye göre test edilecek kalemler tüm kalemlerin seçilmesi, belirli kalemlerin (ör. yüksek "
    "tutarlı veya kilit kalemler) seçilmesi ve denetim örneklemesi yöntemleriyle belirlenir. Seçimin yönetim önerisine "
    "bırakılması tarafsızlığı zedeler.")

P.q("BDS 500 prg. 11",
    "Denetçi, satış müdürünün sorgulamada verdiği cevabın dış teyit sonucuyla çeliştiğini tespit etmiştir. "
    f"{B500} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Prosedürlerde değişiklik veya ekleme yapar, diğer yönlere etkisini mütalaa eder.",
    ["Yönetim temsilcisinin sözlü cevabını esas alır ve teyidi dikkate almaz.",
     "Çelişkiyi dosyaya not eder, başka bir işlem yapmaz.",
     "Teyit sonucunu geçersiz sayar ve yeni teyit göndermeden testi tamamlar.",
     "Çelişkiyi doğrudan önemli iç kontrol eksikliği olarak raporlar ve testi sonlandırır."],
    "BDS 500 prg. 11'e göre bir kaynaktan elde edilen kanıt başka bir kaynaktan elde edilenle tutarsızsa veya "
    "güvenilirlik şüphesi varsa denetçi, sorunun çözümü için prosedürlerde hangi değişiklik veya eklemelerin yapılacağına "
    "karar verir ve varsa denetimin diğer yönlerine etkisini mütalaa eder.")

# ================================================================ BDS 501: stok, dava, bölüm bilgisi
P.q("BDS 501 prg. 4",
    f"{B501}, stokların önemli olması durumunda fiziki sayıma katılan denetçinin yapması gerekenler arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Sayımı işletme personeli yerine kendisi yürütmek ve sayım sonuçlarını kendisi kayda almak",
    ["Yönetimin sayım sonuçlarının kaydı ve kontrolüne ilişkin talimat ve prosedürlerini değerlendirmek",
     "Yönetimin sayıma ilişkin prosedürlerinin uygulanmasını gözlemlemek",
     "Stokları tetkik etmek",
     "Test sayımları yapmak"],
    "BDS 501 prg. 4'e göre mümkünse fiziki sayıma katılım; yönetimin talimat ve prosedürlerini değerlendirmeyi, "
    "uygulanmasını gözlemlemeyi, stokları tetkik etmeyi ve test sayımları yapmayı içerir; ayrıca nihai stok kayıtları "
    "üzerinde prosedür uygulanır. Sayımı yürütmek yönetimin sorumluluğudur.")

P.q("BDS 501 prg. 5-7",
    "Denetçi, yıl sonu stok sayımına öngörülemeyen bir durum nedeniyle katılamamıştır. "
    f"{B501} bu durumda denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Başka bir tarihte sayım yapar veya gözlemler; aradaki işlemleri test eder.",
    ["Sayım tutanaklarını yönetimden alarak stokları sayılmış kabul eder.",
     "Stoklara ilişkin olumsuz görüş verir, çünkü sayıma katılım zorunludur.",
     "Katılamadığı sayımın sonuçlarını bir sonraki yıl kontrol etmek üzere erteler.",
     "Stokları kapsam dışında bırakır ve durumu raporunun diğer hususlar bölümünde açıklar."],
    "BDS 501 prg. 5'e göre öngörülemeyen şartlar nedeniyle sayıma katılamayan denetçi başka bir tarihte bazı fiziki "
    "sayımlar yapar veya gözlemler ve aradaki işlemlere ilişkin prosedürler uygular. Prg. 6'ya göre sayıma katılım "
    "uygulanabilir değilse alternatif prosedürler; bunlar da mümkün değilse BDS 705'e göre görüş değişikliği gerekir.",
    zorluk="hard")

P.q("BDS 501 prg. 9-10",
    f"{B501}, dava ve iddialara ilişkin denetim prosedürleriyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dış hukuk müşavirine denetçinin kendi yazdığı ve yanıtın işletmeye verildiği mektup gönderilir.",
    ["Yönetim ve uygun hâllerde iç hukuk müşaviri sorgulanır.",
     "Üst yönetim toplantı tutanakları ve dış hukuk müşaviriyle yazışmalar gözden geçirilir.",
     "Dava giderlerine ilişkin hesaplar gözden geçirilir.",
     "Önemli yanlışlık riski değerlendirilen dava varsa dış hukuk müşaviriyle doğrudan iletişim kurulur."],
    "BDS 501 prg. 9'a göre yönetim ve iç hukuk müşaviri sorgulanır, tutanak ve yazışmalar ile dava gider hesapları gözden "
    "geçirilir. Prg. 10'a göre gerektiğinde dış hukuk müşaviriyle doğrudan iletişim, yönetim tarafından hazırlanıp denetçi "
    "tarafından gönderilen ve müşavirin denetçiyle doğrudan iletişime geçmesini talep eden sorgulama mektubuyla kurulur.",
    zorluk="hard")

# ================================================================ BDS 505: dış teyit
P.q("BDS 505 prg. 6",
    f"{B505}, denetçi tarafından üçüncü bir kişiden fiziki, elektronik veya başka bir ortamda doğrudan yazılı yanıt "
    "şeklinde elde edilen denetim kanıtı aşağıdakilerden hangisidir?",
    "Dış teyit",
    ["Yazılı açıklama", "Sorgulama", "Olumsuz teyit istisnası", "Yeniden hesaplama"],
    "BDS 505 prg. 6'ya göre dış teyit, denetçi tarafından teyit eden taraftan fiziki, elektronik veya başka bir ortamda "
    "doğrudan yazılı yanıt şeklinde elde edilen kanıttır. Yazılı açıklama ise yönetimden alınır (BDS 580).", zorluk="easy")

P.q("BDS 505 prg. 7",
    f"{B505}, dış teyit prosedürlerini uygularken denetçinin kontrolü sürdürmesi gereken hususlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Teyitleri işletmenin postalatması ve yanıtları işletmenin teslim alması",
    ["Teyit veya talep edilecek bilgilere karar vermek",
     "Uygun teyit eden tarafı seçmek",
     "Teyit taleplerini doğru adresleri de içerecek şekilde denetçinin tasarlaması",
     "Talepleri teyit eden tarafa, takipleri dahil denetçi göndermek"],
    "BDS 505 prg. 7'ye göre denetçi, teyit edilecek bilgilere karar verme, teyit eden tarafı seçme, talepleri tasarlama "
    "ve takip talepleri dahil talepleri kendisi gönderme konusunda kontrolü sürdürür. Yanıtların işletmeye gönderilmesi "
    "kanıtın güvenilirliğini zedeler.")

P.q("BDS 505 prg. 8-9",
    "Yönetim, en büyük müşterisine alacak teyidi gönderilmesine izin vermemektedir. "
    f"{B505} denetçinin bu durumda yapması gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Yönetimin kararını gerekçe sormadan kabul ederek bu alacağı test etmemek",
    ["Yönetimin gerekçelerini sorgulamak ve geçerliliğine dair kanıt elde etmeye çalışmak",
     "İzin vermemenin hile riski dahil risk değerlendirmesine etkisini değerlendirmek",
     "İhtiyaca uygun ve güvenilir kanıt için alternatif prosedürler uygulamak",
     "Gerekçe makul değilse durumu üst yönetimden sorumlu olanlara bildirmek"],
    "BDS 505 prg. 8'e göre yönetim izin vermezse denetçi gerekçeleri sorgular ve geçerliliğine dair kanıt arar, hile riski "
    "dahil risk değerlendirmesine etkisini değerlendirir ve alternatif prosedürler uygular. Prg. 9'a göre gerekçe makul "
    "değilse veya alternatif kanıt elde edilemezse üst yönetimle iletişim kurar ve BDS 705'e göre raporu değerlendirir.")

P.q("BDS 505 prg. 15",
    f"{B505}, olumsuz teyit taleplerinin tek başına maddi doğrulama prosedürü olarak kullanılabilmesi için gerekli "
    "şartlar arasında aşağıdakilerden hangisi yer almaz?",
    "Anakitlenin az sayıda ve yüksek tutarlı hesap bakiyelerinden oluşması",
    ["Önemli yanlışlık riskinin düşük değerlendirilmiş ve kontrollerin etkinliğine dair yeterli kanıt elde edilmiş olması",
     "Beklenen istisna oranının düşük olması",
     "Denetçinin, taleplerin göz ardı edilmesine sebep olacak durumlardan haberdar olmaması",
     "Anakitlenin çok sayıda küçük ve aynı türden kalemden oluşması"],
    "BDS 505 prg. 15'e göre olumsuz teyitler daha az ikna edici kanıt sağlar ve tek başına ancak şu şartların tümü "
    "varsa kullanılabilir: risk düşük ve kontroller test edilmiş, anakitle çok sayıda küçük ve aynı türden kalemden "
    "oluşuyor, beklenen istisna oranı düşük ve taleplerin göz ardı edileceğine dair bir bilgi yok.", zorluk="hard")

P.q("BDS 505 prg. 12-13",
    "Denetçi, olumlu alacak teyidi gönderdiği bir müşteriden yanıt alamamıştır. "
    f"{B505} bu durumda denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Güvenilir kanıt elde etmek için alternatif prosedürler uygular.",
    ["Yanıt gelmeyen teyidi olumlu yanıt kabul eder ve bakiyeyi doğrulanmış sayar.",
     "Yanıt gelmeyen bakiyeyi yanlışlık kabul ederek tamamını düzeltme olarak önerir.",
     "Yönetimden yanıt gelmediğine dair yazılı açıklama alarak testi tamamlar.",
     "Aynı müşteriye yanıt gelene kadar süresiz olarak teyit göndermeye devam eder."],
    "BDS 505 prg. 12'ye göre yanıt alınamayan her durumda denetçi, ihtiyaca uygun ve güvenilir kanıt elde etmek için "
    "alternatif prosedürler (ör. sonraki tahsilatların incelenmesi) uygular. Prg. 13'e göre olumlu teyit yanıtının "
    "zorunlu olduğu durumlarda alternatif prosedürler yeterli kanıt sağlamaz.")

P.q("BDS 505 prg. 6",
    f"{B505}, teyit edilmesi talep edilen bilgiler ile teyit eden tarafın sunduğu bilgiler arasında farklılık olduğunu "
    "gösteren yanıt aşağıdakilerden hangisidir?",
    "İstisna",
    ["Yanıtsızlık", "Olumsuz teyit", "Anormallik", "Sapma"],
    "BDS 505 prg. 6'ya göre istisna, teyit edilmesi talep edilen veya kayıtlarda bulunan bilgiler ile teyit eden tarafın "
    "sunduğu bilgiler arasında farklılık olduğunu gösteren yanıttır. Prg. 14'e göre denetçi istisnaların yanlışlık "
    "göstergesi olup olmadığını araştırır. Sapma ve anormallik BDS 530'daki örnekleme terimleridir.", zorluk="easy")

# ================================================================ BDS 520: analitik prosedürler
P.q("BDS 520 prg. 5",
    f"{B520}, maddi analitik prosedürlerin tasarlanması ve uygulanmasına ilişkin aşağıdakilerden hangisi yanlıştır?",
    "Beklenti oluşturulurken veri güvenilirliği değerlendirilmez; önemli olan fark tutarıdır.",
    ["Prosedürün ilgili yönetim beyanları için uygun olup olmadığına karar verilir.",
     "Beklenen değerin oluşturulmasında kullanılan verilerin güvenilirliği değerlendirilir.",
     "Kayıtlı tutarlar veya oranlar için yeterince kesin bir beklenen değer oluşturulur.",
     "Kayıtlı tutarlarla beklenen değerler arasındaki kabul edilebilir fark tutarı belirlenir."],
    "BDS 520 prg. 5'e göre denetçi prosedürün yönetim beyanları için uygunluğuna karar verir, beklenen değerin "
    "oluşturulmasında kullanılan verilerin kaynağı, karşılaştırılabilirliği, niteliği ve kontrolleri dikkate alarak "
    "güvenilirliğini değerlendirir, yeterince kesin bir beklenti oluşturur ve kabul edilebilir fark tutarını belirler.")

P.q("BDS 520 prg. 6",
    f"{B520}, denetimin sonuna doğru analitik prosedürlerin uygulanmasının amacı aşağıdakilerden hangisidir?",
    "Tabloların işletme hakkındaki anlayışla tutarlılığına dair genel sonuç oluşturmak",
    ["Denetim ekibinin verimliliğini ölçmek ve sonraki yılın bütçesini hazırlamak",
     "Önceki denetimlerde test edilen kontrollerin cari yılda etkin olduğunu kanıtlamak",
     "Yönetimin yazılı açıklamalarına ihtiyaç olmadığını teyit etmek",
     "Önemlilik düzeyini yeniden belirleyerek test edilen kalem sayısını azaltmak"],
    "BDS 520 prg. 6'ya göre denetçi, tabloların işletme hakkındaki anlayışıyla tutarlı olup olmadığına dair genel bir "
    "sonuç oluştururken denetimin sonuna doğru kendisine yardımcı olacak analitik prosedürleri tasarlar ve uygular.")

P.q("BDS 520 prg. 7",
    "Denetçi, uyguladığı analitik prosedür sonucunda brüt kâr marjının sektör ve önceki yıllarla tutarsız biçimde "
    f"yükseldiğini ve beklenen değerden ciddi ölçüde saptığını tespit etmiştir. {B520} denetçinin yapması gereken "
    "aşağıdakilerden hangisidir?",
    "Yönetimi sorgular, cevaplara ilişkin kanıt elde eder, gerekli prosedürleri uygular.",
    ["Farkı yönetimin açıklamasıyla kapatır; ek kanıt aramaz.",
     "Farkı önemli yanlışlık kabul ederek doğrudan düzeltme önerir.",
     "Analitik prosedürün güvenilir olmadığı sonucuna varır ve sonucunu değerlendirme dışında tutar.",
     "Farkı bir sonraki yılın risk değerlendirmesine not ederek cari yılda işlem yapmaz."],
    "BDS 520 prg. 7'ye göre beklenen değerlerden ciddi ölçüde farklı dalgalanmalar tespit edilirse denetçi yönetimi "
    "sorgular ve cevaplara ilişkin uygun kanıt elde eder, şartların gerektirdiği diğer prosedürleri uygular.")

P.q("BDS 520 A1",
    f"{B520}, “analitik prosedürler” kavramına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Finansal ve finansal olmayan veriler arasındaki makul ilişkilerin analizidir.",
    ["Sadece cari yıl rakamlarının önceki yıl rakamlarıyla karşılaştırılmasından ibarettir.",
     "Belgelerin matematiksel doğruluğunun tek tek kontrol edilmesidir.",
     "Sadece risk değerlendirme aşamasında kullanılabilen, kanıt sağlamayan bir tekniktir.",
     "İşletmenin kontrollerinin denetçi tarafından bağımsız olarak yeniden uygulanmasıdır."],
    "BDS 520 prg. 4'e göre analitik prosedürler, finansal ve finansal olmayan veriler arasındaki makul ilişkilerin "
    "analizi yoluyla finansal bilgilerin değerlendirilmesidir; diğer ilgili bilgilerle tutarsız dalgalanmaların "
    "araştırılmasını da kapsar ve maddi doğrulama amacıyla da kullanılabilir.")

# ================================================================ BDS 550: ilişkili taraflar
P.q("BDS 550 prg. 18",
    "Denetçi, işletmenin olağan iş akışı dışında, ana ortağın kontrolündeki bir şirkete piyasa değerinin altında önemli "
    f"tutarda bir arazi sattığını tespit etmiştir. {B550} bu işleme ilişkin aşağıdakilerden hangisi doğrudur?",
    "Olağan iş akışı dışındaki önemli ilişkili taraf işlemi ciddi riske yol açan işlemdir.",
    ["İşlem ilişkili tarafla yapıldığı için ek bir değerlendirme gerektirmez.",
     "İşlem piyasa değerinin altında olduğu sürece önemli yanlışlık riski doğurmaz.",
     "İlişkili taraf işlemleri sadece dipnotlarda açıklandığı için denetim kapsamında değildir.",
     "İşlem yönetim kurulunca onaylandıysa denetçinin değerlendirmesine gerek kalmaz."],
    "BDS 550 prg. 18'e göre denetçi ilişkili taraflarla bağlantılı önemli yanlışlık risklerini belirleyip ciddi risk olup "
    "olmadıklarına karar verir; işletmenin olağan iş akışı dışında gerçekleşen belirlenmiş önemli ilişkili taraf "
    "işlemlerini ciddi risklere yol açan işlemler olarak değerlendirir.")

P.q("BDS 550 prg. 15",
    f"{B550}, yönetimin daha önce belirlemediği veya açıklamadığı ilişkili taraf ilişkilerine yönelik denetçinin tutumu "
    "aşağıdakilerden hangisidir?",
    "Tetkik sırasında bu ilişkilere işaret edebilecek düzenlemelere karşı dikkatli olur.",
    ["Yönetimin açıklamadığı ilişkili tarafları araştırmaz; bu tamamen yönetimin sorumluluğudur.",
     "Tüm tedarikçi ve müşterilerin ortaklık yapısını ticaret sicilinden tek tek araştırır.",
     "Yönetimin sunduğu listeyi, üst yönetim onayı alındıysa tek kaynak olarak kabul eder.",
     "İlişkili tarafları sadece önceki yılın denetim dosyasından belirler ve günceller."],
    "BDS 550 prg. 15'e göre yönetimin belirlemediği veya açıklamadığı ilişkili taraf ilişkileri bulunabilir; denetçi kayıt "
    "ve belgeleri tetkik ederken bunlara işaret edebilecek düzenlemelere ve bilgilere karşı dikkatli olur.")

# ================================================================ BDS 560: sonraki olaylar
P.q("BDS 560 prg. 6",
    f"{B560}, finansal tabloların tarihi ile denetçi raporu tarihi arasında gerçekleşen olaylara ilişkin denetçinin "
    "sorumluluğu aşağıdakilerden hangisidir?",
    "Düzeltme veya açıklama gerektiren tüm olayların belirlendiğine dair kanıt elde eder.",
    ["Bu dönemdeki olaylar için sorumluluğu yoktur; sadece yönetim sorumludur.",
     "Sadece yönetimin kendisine bildirdiği olayları değerlendirir.",
     "Daha önce tatmin edici sonuç veren konularda da tüm prosedürleri rapor tarihine kadar yeniden uygular.",
     "Bu dönemdeki olayları bir sonraki yılın denetiminde değerlendirmek üzere not eder."],
    "BDS 560 prg. 6'ya göre denetçi, finansal tabloların tarihi ile rapor tarihi arasında gerçekleşen ve düzeltme veya "
    "açıklama gerektiren tüm olayların belirlendiğine dair yeterli ve uygun kanıt elde etmek için prosedürler uygular; "
    "ancak daha önce tatmin edici sonuç veren konularda ilave prosedür uygulaması beklenmez.")

P.q("BDS 560 prg. 10",
    f"{B560}, denetçi raporu tarihinden sonra ancak finansal tablolar yayımlanmadan önce öğrenilen olaylara ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Rapor tarihinden sonra, yayıma kadar yeni prosedürler uygulamakla yükümlüdür.",
    ["Denetçinin rapor tarihinden sonra tablolarla ilgili prosedür uygulama yükümlülüğü yoktur.",
     "Raporunu değiştirebilecek bir durumdan haberdar olursa konuyu yönetimle müzakere eder.",
     "Tablolarda değişiklik gerekip gerekmediğine karar verir.",
     "Değişiklik gerekiyorsa yönetimin bu konuyu tablolarda nasıl ele alacağını sorgular."],
    "BDS 560 prg. 10'a göre denetçinin rapor tarihinden sonra tablolarla ilgili prosedür uygulama yükümlülüğü yoktur; "
    "ancak rapor tarihinde bilseydi raporunu değiştirebilecek bir durumu tablolar yayımlanmadan önce öğrenirse yönetimle "
    "müzakere eder, değişiklik gerekip gerekmediğine karar verir ve gerekiyorsa yönetimin nasıl ele alacağını sorgular.")

P.q("BDS 560 prg. 14",
    "Finansal tablolar ve denetçi raporu yayımlandıktan iki ay sonra denetçi, rapor tarihinde var olan ve bilseydi "
    f"raporunu değiştireceği önemli bir hususu öğrenmiştir. {B560} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Yönetimle müzakere eder ve tablolarda değişiklik gerekip gerekmediğine karar verir.",
    ["Tablolar yayımlandığı için yükümlülüğü sona ermiştir; işlem yapmaz.",
     "Doğrudan yeni bir denetçi raporu düzenleyerek bunu yönetime danışmadan kamuya duyurur.",
     "Durumu sadece bir sonraki yılın raporunda diğer hususlar paragrafında açıklar.",
     "Yönetimle görüşmeden denetim sözleşmesini fesheder ve Kuruma bildirir."],
    "BDS 560 prg. 14'e göre tablolar yayımlandıktan sonra denetçinin prosedür uygulama yükümlülüğü yoktur; ancak rapor "
    "tarihinde bilseydi raporunu değiştirebilecek bir durumu öğrenirse yönetimle müzakere eder, değişiklik gerekip "
    "gerekmediğine karar verir ve gerekiyorsa yönetimin nasıl ele alacağını sorgular.")

# ================================================================ BDS 570: süreklilik değerlendirmesi
P.sayisal("BDS 570 prg. 13",
    "Yönetim, işletmenin sürekliliğini devam ettirme kabiliyetine ilişkin değerlendirmesini finansal tablo tarihinden "
    f"itibaren sekiz aylık bir dönem için yapmıştır. {B570} denetçi, yönetimden değerlendirmeyi finansal tablo tarihinden "
    "itibaren en az kaç aylık dönemi kapsayacak şekilde genişletmesini talep eder?",
    "12", ["6", "9", "18", "24"],
    "BDS 570 prg. 13'e göre yönetimin değerlendirmesi finansal tablo tarihinden itibaren on iki aydan daha kısa bir "
    "süreyi kapsıyorsa denetçi, yönetimden değerlendirmeyi en az on iki aylık dönemi kapsayacak şekilde genişletmesini "
    "talep eder.", zorluk="easy")

P.q("BDS 570 prg. 16",
    f"{B570}, sürekliliğe ilişkin ciddi şüphe oluşturabilecek olay veya şartlar belirlendiğinde denetçinin uygulayacağı "
    "ilave prosedürler arasında aşağıdakilerden hangisi yer almaz?",
    "Olay ve şartları azaltan etkenleri dikkate almadan belirsizliğin varlığını kabul etmek",
    ["Yönetim değerlendirme yapmamışsa yönetimden değerlendirme yapmasını talep etmek",
     "Yönetimin geleceğe yönelik faaliyet planlarının uygulanabilirliğini değerlendirmek",
     "Nakit akış tahmini kullanılmışsa verilerin güvenilirliğini ve varsayımların desteklenip desteklenmediğini değerlendirmek",
     "Değerlendirme tarihinden sonra ek bilgi ortaya çıkıp çıkmadığını mütalaa etmek ve yazılı açıklama talep etmek"],
    "BDS 570 prg. 16'ya göre denetçi, olay ve şartların etkisini azaltan etkenler dahil önemli belirsizliğin varlığına "
    "karar vermek için ilave prosedürler uygular: yönetimden değerlendirme istemek, planların uygulanabilirliğini ve nakit "
    "akış tahminlerini değerlendirmek, ek bilgileri mütalaa etmek ve yazılı açıklama talep etmek.", zorluk="hard")

P.q("BDS 570 prg. 21",
    "Finansal tablolar işletmenin sürekliliği esasına göre hazırlanmıştır; ancak denetçi, işletmenin faaliyetlerini "
    f"durdurma kararı aldığı için bu esasın kullanılmasının uygun olmadığı yargısına varmıştır. {B570} denetçi hangi "
    "görüşü verir?",
    "Olumsuz görüş",
    ["Olumlu görüş", "Sınırlı olumlu görüş", "Görüş bildirmekten kaçınma",
     "Belirsizlik bölümlü olumlu görüş"],
    "BDS 570 prg. 21'e göre tablolar süreklilik esasına göre hazırlanmış ancak bu esasın kullanılması denetçinin "
    "yargısına göre uygun değilse denetçi olumsuz görüş verir.", zorluk="easy")

# ================================================================ BDS 580: yazılı açıklamalar
P.q("BDS 580 prg. 14",
    f"{B580}, yazılı açıklamaların tarihine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Rapor tarihinden sonra olmamak üzere ona en yakın tarihtir.",
    ["Finansal tabloların bilanço tarihiyle aynıdır.",
     "Denetim sözleşmesinin imzalandığı tarihtir.",
     "Denetçi raporu tarihinden en az otuz gün sonrası ile genel kurul tarihi arasıdır.",
     "Genel kurul toplantısının yapıldığı tarihtir."],
    "BDS 580 prg. 14'e göre yazılı açıklamaların tarihi, denetçi raporu tarihinden sonra olmamakla birlikte bu tarihe "
    "mümkün olan en yakın tarihtir ve raporda atıf yapılan tüm tabloları ve dönemleri kapsar.")

P.q("BDS 580 prg. 20",
    f"{B580}, aşağıdaki durumlardan hangisinde denetçi görüş bildirmekten kaçınır?",
    "Yönetim, hazırlama sorumluluğuna ilişkin yazılı açıklamayı sunmazsa",
    ["Yönetim, yazılı açıklamayı rapor tarihinden birkaç gün önce imzalarsa",
     "Yazılı açıklamada, denetçinin talep etmediği ek bilgilere de yer verilirse",
     "Yazılı açıklama, genel müdür yerine mali işlerden sorumlu yönetici tarafından da imzalanırsa",
     "Yazılı açıklamalar, önceki yıldakiyle aynı ifadeler kullanılarak hazırlanırsa"],
    "BDS 580 prg. 20'ye göre yönetimin dürüstlüğü konusunda yeterli şüphe nedeniyle prg. 10-11'deki açıklamaların "
    "güvenilir olmadığı sonucuna varılırsa veya yönetim bu açıklamaları sunmazsa denetçi BDS 705 uyarınca görüş "
    "bildirmekten kaçınır.", zorluk="hard")

P.q("BDS 580 prg. 10-11",
    f"{B580}, denetçinin yönetimden talep etmesi gereken yazılı açıklamalar arasında aşağıdakilerden hangisi yer almaz?",
    "Denetçinin uyguladığı prosedürlerin yeterli olduğuna dair yönetimin güvencesi",
    ["Tabloların geçerli çerçeveye uygun hazırlanması sorumluluğunun yerine getirildiği",
     "Sözleşmede mutabık kalındığı üzere ilgili tüm bilgilerin ve erişim imkânının sağlandığı",
     "Tüm işlemlerin kaydedildiği ve finansal tablolara yansıtıldığı",
     "Gerçeğe uygun sunum dahil sorumlulukların sözleşme şartlarında belirtildiği şekilde açıklandığı"],
    "BDS 580 prg. 10-12'ye göre denetçi, tabloları çerçeveye uygun hazırlama sorumluluğunun, tüm bilgilerin ve erişimin "
    "sağlandığının ve tüm işlemlerin kaydedildiğinin yazılı açıklamasını talep eder; sorumluluklar sözleşme şartlarında "
    "belirtildiği şekilde açıklanır. Prosedürlerin yeterliliği denetçinin sorumluluğundadır.")

P.oncul("BDS 580 prg. 3-4, A1",
    f"{B580} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Yazılı açıklamalar, finansal tabloları, yönetim beyanlarını ve bunları destekleyen defter ve kayıtları kapsamaz.",
     "Yazılı açıklamalar denetçinin talep ettiği gerekli bilgilerdir ve denetim kanıtı niteliğindedir.",
     "Yazılı açıklamalar, ele aldıkları konularda tek başına yeterli ve uygun denetim kanıtı sağlar.",
     "Güvenilir yazılı açıklama sunulması, diğer kanıtların niteliğini veya kapsamını etkilemez."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "BDS 580 prg. 7'ye göre yazılı açıklamalar tabloları, yönetim beyanlarını ve destekleyici defter ve kayıtları kapsamaz "
    "(I); prg. 3 ve A1'e göre denetim kanıtı niteliğindedir (II). Prg. 4'e göre tek başına yeterli ve uygun kanıt "
    "sağlamaz (III yanlış) ve güvenilir açıklama sunulması diğer kanıtların niteliğini veya kapsamını etkilemez (IV).",
    zorluk="hard")

# ================================================================ BDS 620: denetçinin uzmanı
P.q("BDS 620 prg. 14",
    f"{B620}, olumlu görüş içeren denetçi raporunda denetçinin faydalandığı uzmana atıf yapılmasıyla ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Mevzuat zorunlu tutmadıkça atıf yapılmaz; zorunluysa sorumluluğun azalmadığı belirtilir.",
    ["Uzmanın adı ve çalışmasının sonuçları raporda ayrıca açıklanarak sorumluluk paylaşılır.",
     "Uzmana atıf yapıldığında denetçinin o alandaki sorumluluğu uzmana geçer.",
     "Uzmana atıf, sadece uzman denetim şirketinin ortağıysa yapılabilir.",
     "Atıf yapılıp yapılmayacağına denetlenen işletmenin yönetimi karar verir."],
    "BDS 620 prg. 14'e göre mevzuat zorunlu tutmadıkça denetçi olumlu görüş içeren raporunda uzmanın çalışmasına atıf "
    "yapmaz; zorunluysa atfın denetçinin görüşe ilişkin sorumluluğunu azaltmadığını belirtir. Prg. 3'e göre denetçi, "
    "görüşünden tek başına sorumludur.")

P.q("BDS 620 prg. 9",
    f"{B620}, denetçinin dış uzmanın tarafsızlığını değerlendirmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tarafsızlığı tehdit edebilecek çıkar ve ilişkiler hakkında sorgulama yapılmasını içerir.",
    ["Dış uzmanlar bağımsız sayıldığından tarafsızlıkları ayrıca değerlendirilmez.",
     "Tarafsızlık sadece uzmanın ücretinin denetim ücretini aşıp aşmadığına bakılarak değerlendirilir.",
     "Tarafsızlık değerlendirmesi, uzmanın mesleki kuruluşunun yazılı onayıyla yapılır.",
     "Tarafsızlık, uzman denetim şirketinin çalışanı değilse değerlendirilmez."],
    "BDS 620 prg. 9'a göre denetçi uzmanın gerekli yeterlik, kabiliyet ve tarafsızlığa sahip olup olmadığını değerlendirir; "
    "dış uzmanın tarafsızlığının değerlendirilmesi, tarafsızlığı tehdit edebilecek çıkar ve ilişkiler hakkında sorgulama "
    "yapılmasını içerir.")

# ================================================================ karma: TDS
P.q("BDS 500 prg. 6, BDS 330 prg. 26",
    f"KGK düzenlemeleri ve Türkiye Denetim Standartları’na göre denetim kanıtıyla ilgili aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Denetçi görüşünü oluştururken sadece yönetim beyanlarını doğrulayan kanıtları dikkate alır.",
    ["Denetim kanıtları yapı olarak kümülatiftir ve öncelikle denetim prosedürlerinden elde edilir.",
     "Kanıtlar, denetimin TDS çerçevesinde ve mesleki şüphecilik içinde planlanıp yürütülmesiyle elde edilir ve tevsik edilir.",
     "Önceki denetimlerden ve kabul prosedürlerinden elde edilen bilgiler de kanıt olabilir.",
     "Yönetimin belirli bir beyanını desteklemeyen bilgi yokluğu da kanıt olarak kullanılabilir."],
    "BDS 330 prg. 26'ya göre denetçi görüşünü oluştururken yönetim beyanlarını doğrulayan veya onlarla çelişen tüm ilgili "
    "kanıtları mütalaa eder. BDS 500 A1-A2 kanıtın kümülatif olduğunu, önceki denetimlerden ve bilgi yokluğundan da "
    "elde edilebileceğini açıklar; Yönetmelik m. 9 kanıtların mesleki şüphecilik içinde elde edilip tevsik edilmesini ister.")

P.q("BDS 500 A2",
    f"{B500}, aşağıdakilerden hangisi denetim kanıtı olarak kullanılabilecek bilgi kaynaklarından biri değildir?",
    "İşletmeyi incelemeden, sektöre ilişkin genel izlenime dayanan tahmin",
    ["Önceki denetimlerde elde edilen bilgiler (hâlâ ilgili ve güvenilirse)",
     "Müşteri kabul ve devam prosedürlerinden elde edilen bilgiler",
     "Yönetimin faydalandığı uzman tarafından hazırlanan bilgiler",
     "Denetçinin, işletme dışındaki bağımsız kaynaklardan elde ettiği bilgiler"],
    "BDS 500 A2-A3'e göre kanıt; denetim prosedürlerinden, önceki denetimlerden (hâlâ ilgili ve güvenilir olmak "
    "şartıyla), kabul ve devam prosedürlerinden, işletme içi ve dışı kaynaklardan ve yönetimin uzmanından elde edilebilir. "
    "Dayanaksız genel izlenim kanıt değildir.")

P.q("BDS 505 A23",
    f"{B505}, olumlu ve olumsuz teyitlerin ikna ediciliği bakımından aşağıdakilerden hangisi doğrudur?",
    "Olumsuz teyitler, olumlu teyitlere göre daha az ikna edici kanıt sağlar.",
    ["Olumsuz teyitler, yanıt gerektirmediği için olumlu teyitlerden daha güvenilirdir.",
     "Olumlu ve olumsuz teyitler eşit derecede ikna edicidir.",
     "Olumsuz teyitlere yanıt gelmemesi, bakiyenin doğru olduğunu tartışmasız kanıtlar.",
     "Olumsuz teyit sadece yüksek riskli bakiyelerde kullanılabilir."],
    "BDS 505 prg. 15 ve A23'e göre olumsuz teyitler olumlu teyitlere göre daha az ikna edici kanıt sağlar; yanıt "
    "gelmemesi, teyit eden tarafın talebi aldığını ve bilgileri doğruladığını açıkça göstermez. Bu yüzden tek başına "
    "kullanımı düşük risk ve belirli şartlarla sınırlıdır.")

# ================================================================ ek sorular
P.q("BDS 500 A14-A16",
    f"{B500}, tetkik prosedürüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Stokların fiziki tetkiki, mülkiyetin işletmeye ait olduğunu da kanıtlar.",
    ["Tetkik, basılı veya elektronik ortamdaki kayıt ve belgelerin ya da varlıkların fiziki olarak incelenmesini içerir.",
     "Kayıt ve belgelerin tetkiki, bunların nitelik ve kaynağına göre farklı güvenilirlik derecelerinde kanıt sağlar.",
     "Yetkilendirmeye ilişkin kanıt elde etmek için kayıtların tetkiki kontrol testi olarak kullanılabilir.",
     "Somut varlıkların tetkiki, varlığın mevcudiyetine ilişkin güvenilir denetim kanıtı sağlayabilir."],
    "BDS 500 A14-A16'ya göre tetkik, kayıt ve belgelerin veya varlıkların fiziki olarak incelenmesidir; güvenilirliği "
    "kaynağa ve kontrollere bağlıdır ve kontrol testi olarak da kullanılabilir. Somut varlıkların tetkiki mevcudiyete dair "
    "güvenilir kanıt sağlar, ancak hak ve yükümlülükler ile değerleme hakkında kanıt sağlamayabilir.")

P.q("BDS 501 prg. 8",
    f"İşletmenin önemli tutardaki stokları üçüncü bir kişinin gözetim ve kontrolündeki bir depoda bulunmaktadır. {B501} "
    "denetçinin bu stokların mevcudiyeti ve durumuna ilişkin yapması gereken aşağıdakilerden hangisidir?",
    "Üçüncü kişiden teyit alır, tetkik yapar veya ikisini birlikte uygular.",
    ["Stokları, işletmenin kendi kayıtlarında yer aldığı için doğrulanmış kabul eder.",
     "Stokları kapsam dışı bırakır; üçüncü kişideki stoklar denetimin konusu değildir.",
     "Üçüncü kişinin depo sözleşmesini inceler, fiziki sayım veya teyite gerek görmez.",
     "İşletme yönetiminden, stokların depoda bulunduğuna dair sözlü açıklama almakla yetinir."],
    "BDS 501 prg. 8'e göre üçüncü kişinin gözetimindeki stoklar önemliyse denetçi, üçüncü kişiden bu stokların miktar ve "
    "durumuna ilişkin teyit alarak ve/veya tetkik veya şartlara uygun diğer prosedürleri uygulayarak yeterli ve uygun "
    "kanıt elde eder.")

P.q("BDS 505 prg. 6, 10",
    f"{B505}, dış teyitlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Elektronik ortamda alınan teyit yanıtları dış teyit olarak kabul edilmez.",
    ["Dış teyit, teyit eden taraftan fiziki, elektronik veya başka bir ortamda doğrudan alınan yazılı yanıttır.",
     "Denetçi, yanıtın güvenilirliğine ilişkin şüphe varsa bu şüpheyi gidermek için ilave kanıt elde eder.",
     "Yanıtın güvenilir olmadığına karar verilirse bunun risk değerlendirmesine ve diğer prosedürlere etkisi değerlendirilir.",
     "Teyit prosedürleri, sözleşme şartları veya yan sözleşmelerin varlığının teyidi için de kullanılabilir."],
    "BDS 505 prg. 6'ya göre dış teyit fiziki, elektronik veya başka bir ortamda doğrudan alınan yazılı yanıttır. Prg. "
    "10-11 yanıtın güvenilirliğine ilişkin şüphede ilave kanıt ve etkinin değerlendirilmesini ister; A1'e göre teyitler "
    "sözleşme şartlarının veya yan sözleşmelerin teyidinde de kullanılabilir.")

P.q("BDS 505 prg. 14",
    f"{B505}, teyit yanıtlarında ortaya çıkan istisnalara ilişkin denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "İstisnaların yanlışlık göstergesi olup olmadığını belirlemek için bunları araştırır.",
    ["İstisnaları, tutarları önemsiz olsa dahi doğrudan yanlışlık kabul edip düzeltme önerir.",
     "İstisnaları, teyit eden tarafın hatası sayarak araştırma yapmadan dosyaya kaldırır.",
     "İstisnaları sadece üst yönetimden sorumlu olanlara bildirir ve prosedürü tamamlanmış sayar.",
     "İstisna oranı yüksekse teyit prosedürünü geçersiz sayarak sonuçları değerlendirme dışında bırakır."],
    "BDS 505 prg. 14'e göre denetçi, istisnaların yanlışlık göstergesi olup olmadığını belirlemek üzere bunları araştırır. "
    "A21-A22'ye göre bazı istisnalar zamanlama farkı gibi yanlışlık dışı nedenlerden kaynaklanabilir; bazıları ise hile "
    "göstergesi olabilir.")

P.q("BDS 520 A6",
    f"{B520}, aşağıdaki kalemlerden hangisi maddi analitik prosedürlerin uygulanmasına genellikle en uygun olanıdır?",
    "Personel sayısı ve ücret artışıyla tahmin edilebilen ücret giderleri",
    ["Yıl içinde bir kez yapılan ve tutarı müzakereye bağlı önemli bir iştirak satışı",
     "Bilanço tarihinden sonra sonuçlanan, tutarı belirsiz tek bir dava karşılığı",
     "Yönetimin taraflılığına açık, tek seferlik bir şerefiye değer düşüklüğü tahmini",
     "Olağan iş akışı dışında ilişkili tarafla yapılan önemli bir arsa satışı"],
    "BDS 520 A6'ya göre maddi analitik prosedürler genellikle zaman içinde tahmin edilebilir olma eğiliminde olan büyük "
    "hacimli işlemlere uygulanır. Ücret giderleri gibi kalemler personel sayısı ve ücret oranlarıyla tahmin edilebilir; "
    "tek seferlik, muhakemeye dayalı veya ilişkili taraf işlemleri detay testi gerektirir.")

P.q("BDS 540 prg. 9",
    f"BDS 540 “Muhasebe Tahminlerinin Denetimi”ne göre, önceki dönem finansal tablolarında yer alan muhasebe "
    "tahminlerinin sonuçlarının gözden geçirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Denetçi, önceki dönem tahminlerinin sonucunu veya yeniden oluşturulan tahminleri gözden geçirir.",
    ["Bu gözden geçirmenin amacı, önceki yıl yapılan yargıların hatalı olduğunu kanıtlayarak görüşü değiştirmektir.",
     "Gözden geçirme sadece tahminin gerçekleşen sonuçla birebir aynı olduğu durumlarda yapılır.",
     "Önceki dönem tahminleri kesinleştiği için cari denetimde gözden geçirilmez.",
     "Gözden geçirme, sadece yönetim değiştiğinde ve yeni yönetim talep ettiğinde yapılır."],
    "BDS 540 prg. 9'a göre denetçi, önceki dönem tablolarındaki muhasebe tahminlerinin sonucunu veya cari dönem için "
    "yeniden oluşturulmuşsa sonraki tahminleri gözden geçirir. Bu gözden geçirmenin amacı önceki yargıları sorgulamak "
    "değil, yönetimin tahmin sürecine ilişkin bilgi edinmek ve risk değerlendirmesine dayanak oluşturmaktır.", zorluk="hard")

P.q("BDS 550 prg. 13",
    f"{B550}, denetçinin ilişkili taraflarla ilgili olarak yönetimi sorgulaması gereken konular arasında aşağıdakilerden "
    "hangisi yer almaz?",
    "İlişkili tarafların kendi denetçilerine ödedikleri denetim ücretleri",
    ["İşletmenin ilişkili taraflarının kimliği ve önceki dönemden bu yana değişiklikler",
     "İşletme ile ilişkili taraflar arasındaki ilişkilerin niteliği",
     "Dönem içinde ilişkili taraflarla işlem yapılıp yapılmadığı ile işlemlerin türü ve amacı",
     "İlişkili taraflarla yapılan önemli işlemlere yetki ve onay verilmesine ilişkin kontroller"],
    "BDS 550 prg. 13'e göre denetçi yönetimi ilişkili tarafların kimliği, ilişkilerin niteliği ve dönem içindeki işlemlerin "
    "türü ve amacı hakkında sorgular; prg. 14'e göre bu işlemlere yetki ve onay verilmesine ilişkin kontrolleri de "
    "sorgular. İlişkili tarafların kendi denetim ücretleri bu kapsamda değildir.")

P.q("BDS 550 prg. 24",
    "Yönetim, finansal tablo dipnotlarında ana ortağa yapılan hizmet satışının piyasa şartlarında gerçekleşen işlemlerle "
    f"eşdeğer şartlarda yapıldığını beyan etmiştir. {B550} denetçinin bu beyana ilişkin yükümlülüğü aşağıdakilerden "
    "hangisidir?",
    "Bu beyanla ilgili yeterli ve uygun denetim kanıtı elde eder.",
    ["Beyan yönetime ait olduğundan denetçi bu konuda kanıt aramaz.",
     "Beyanın doğruluğunu ana ortağın denetçisinden alacağı sözlü teyitle kabul eder.",
     "Beyanı, işlemin yönetim kurulunca onaylandığını gösteren karar örneğiyle yeterli sayar.",
     "Beyan dipnotta yer aldığı için denetçi raporunda ayrıca dikkat çekilen hususlarda açıklanır."],
    "BDS 550 prg. 24'e göre yönetim, bir ilişkili taraf işleminin piyasa şartlarındaki işlemlerle eşdeğer şartlarda "
    "yapıldığı anlamına gelen bir beyanda bulunursa denetçi bu beyanla ilgili yeterli ve uygun denetim kanıtı elde eder.")

P.q("BDS 560 prg. 7",
    f"{B560}, finansal tabloların tarihi ile denetçi raporu tarihi arasındaki olayları belirlemek için uygulanabilecek "
    "prosedürler arasında aşağıdakilerden hangisi yer almaz?",
    "Sonraki yılın bütün satış işlemlerinin tek tek detay testine tabi tutulması",
    ["Yönetimin sonraki olayları belirlemek için oluşturduğu prosedürlerin anlaşılması",
     "Yönetimin ve uygun hâllerde üst yönetimden sorumlu olanların sonraki olaylar hakkında sorgulanması",
     "Bilanço tarihinden sonra yapılan ortaklar, yönetim ve üst yönetim toplantılarının tutanaklarının okunması",
     "Varsa işletmenin en son ara dönem finansal tablolarının okunması"],
    "BDS 560 prg. 7'ye göre prosedürler; yönetimin sonraki olaylara ilişkin prosedürlerinin anlaşılması, yönetimin "
    "sorgulanması, toplantı tutanaklarının okunması ve en son ara dönem tablolarının okunmasını içerebilir ve risk "
    "değerlendirmesi dikkate alınarak belirlenir. Sonraki yılın tüm işlemlerinin detay testi gerekmez.")

P.q("BDS 560 prg. 5-a",
    f"{B560}, “bilanço tarihinden sonraki olaylar” kavramı aşağıdakilerden hangisini kapsar?",
    "Tablo tarihi ile rapor tarihi arasındaki olaylar ve rapor tarihinden sonra öğrenilen durumlar",
    ["Sadece finansal tablo tarihi ile genel kurul tarihi arasındaki olaylar",
     "Sadece denetçi raporu tarihinden sonra işletme lehine gerçekleşen olaylar",
     "Sadece bilanço tarihinden önce başlayıp sonra biten sözleşmeler",
     "Sadece yönetimin yazılı olarak denetçiye bildirdiği sonraki dönem işlemleri"],
    "BDS 560 prg. 5-a'ya göre bilanço tarihinden sonraki olaylar, finansal tabloların tarihi ile denetçi raporu tarihi "
    "arasındaki dönemde gerçekleşen olaylar ile denetçinin rapor tarihinden sonra haberdar olduğu durumlardır.")

P.q("BDS 570 A3",
    f"{B570}, aşağıdakilerden hangisi işletmenin sürekliliğine ilişkin ciddi şüphe oluşturabilecek olay veya şartlara "
    "örnek değildir?",
    "Yeni bir ürünün pazar payını hızla artırması",
    ["Kredi sözleşmelerinin şartlarına uyulamaması",
     "Tedarikçilerle vadeli ödemeden peşin ödemeye geçilmesi",
     "Alacaklılara vade tarihinde ödeme yapılamaması",
     "Kredi verenlerin finansal desteği geri çekeceğine dair belirtiler"],
    "BDS 570 A3 finansal durumla ilgili örnekler arasında kredi sözleşmesi şartlarına uyulamamasını, peşin ödemeye "
    "geçilmesini, alacaklılara ödeme yapılamamasını ve finansal desteğin geri çekileceğine dair belirtileri sayar. Pazar "
    "payının artması olumlu bir göstergedir.", zorluk="easy")

P.q("BDS 570 prg. 10",
    f"{B570}, denetçinin risk değerlendirme prosedürlerini uygularken süreklilikle ilgili yapması gereken "
    "aşağıdakilerden hangisidir?",
    "Ciddi şüphe oluşturabilecek olay veya şartların var olup olmadığını mütalaa eder.",
    ["Sürekliliği sadece yönetim talep ettiğinde değerlendirir; aksi hâlde değerlendirme yapmaz.",
     "Sürekliliğe ilişkin değerlendirmeyi yönetim adına kendisi yapar ve tablolara yansıtır.",
     "Süreklilik değerlendirmesini sadece işletme zarar ettiği yıllarda yapar ve kârlı yıllarda atlar.",
     "Sürekliliği denetimin sonunda, rapor tarihinden sonra ayrı bir çalışma olarak değerlendirir."],
    "BDS 570 prg. 10'a göre denetçi risk değerlendirme prosedürlerini uygularken işletmenin sürekliliğini devam ettirme "
    "kabiliyetine ilişkin ciddi şüphe oluşturabilecek olay veya şartların bulunup bulunmadığını mütalaa eder; yönetim ön "
    "değerlendirme yapmışsa bunu yönetimle görüşür. Değerlendirme yapmak yönetimin sorumluluğudur.")

P.q("BDS 580 prg. 17",
    f"Denetçi, yönetimin yazılı açıklamasının diğer denetim kanıtlarıyla tutarlı olmadığını tespit etmiştir. {B580} "
    "denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Sorunu çözmek için denetim prosedürleri uygular.",
    ["Yazılı açıklama yönetimden alındığı için diğer kanıtları dikkate almaz.",
     "Tutarsızlığı görmezden gelir ve yazılı açıklamayı olduğu gibi dosyaya ekler.",
     "Diğer kanıtları geçersiz sayar ve yazılı açıklamaya dayanarak olumlu görüş verir.",
     "Yönetimden yeni bir yazılı açıklama alarak tutarsızlığı çözülmüş kabul eder."],
    "BDS 580 prg. 17'ye göre yazılı açıklamalar diğer kanıtlarla tutarlı değilse denetçi sorunu çözmek için prosedürler "
    "uygular; çözülemezse yönetimin yeterliği, dürüstlüğü ve etik değerlerine ilişkin değerlendirmesini yeniden gözden "
    "geçirir ve bunun açıklamaların ve kanıtların güvenilirliğine etkisini belirler.")

P.q("BDS 580 prg. 9",
    f"{B580}, yazılı açıklamalar kimden talep edilir?",
    "Tablolara ilişkin uygun sorumluluğu olan ve konular hakkında bilgisi bulunan yöneticilerden",
    ["İşletmenin muhasebe servisinde çalışan tüm personelden ayrı ayrı",
     "Sadece işletmenin hukuk müşavirinden ve iç denetim yöneticisinden",
     "İşletmenin en büyük pay sahiplerinden ve kredi veren bankalardan",
     "Denetim ekibinin, yönetim adına hazırlayacağı bir beyan metni olarak kendisinden"],
    "BDS 580 prg. 9'a göre denetçi yazılı açıklamaları, finansal tablolara ilişkin uygun sorumluluğu bulunan ve ilgili "
    "konular hakkında bilgiye sahip olan yöneticilerden talep eder.")

P.q("BDS 620 prg. 12",
    f"{B620}, denetçinin faydalandığı uzmanın çalışmasının yeterliliğini değerlendirirken ele alması gereken hususlar "
    "arasında aşağıdakilerden hangisi yer almaz?",
    "Uzmanın ücretinin sektördeki diğer uzmanlarla karşılaştırılması",
    ["Uzmanın bulgularının ihtiyaca uygunluğu, makullüğü ve diğer kanıtlarla tutarlılığı",
     "Önemli varsayım ve yöntemlerin şartlar altında ihtiyaca uygunluğu ve makullüğü",
     "Önemli kaynak verilerin ihtiyaca uygunluğu, tamlığı ve doğruluğu",
     "Uzmanın vardığı sonuçların denetçinin amaçlarına uygunluğu"],
    "BDS 620 prg. 12'ye göre denetçi uzmanın çalışmasının yeterliliğini; bulgu ve sonuçların ihtiyaca uygunluğu, "
    "makullüğü ve diğer kanıtlarla tutarlılığı, önemli varsayım ve yöntemlerin uygunluğu ile önemli kaynak verilerin "
    "ihtiyaca uygunluğu, tamlığı ve doğruluğu bakımından değerlendirir.")

P.q("BDS 620 prg. 6, BDS 500 prg. 8",
    "Denetçi, işletmenin kıdem tazminatı karşılığını test etmek için kendi denetim şirketinin anlaşmalı olduğu bir "
    "aktüerden destek almıştır. İşletme ise karşılığı hesaplarken başka bir aktüerin raporunu kullanmıştır. Türkiye Denetim "
    "Standartları’na göre bu iki aktüer sırasıyla aşağıdakilerden hangisiyle nitelendirilir?",
    "Denetçinin faydalandığı uzman; yönetimin faydalandığı uzman",
    ["Yönetimin faydalandığı uzman; denetçinin faydalandığı uzman",
     "Denetim ekibinin üyesi; hizmet kuruluşu denetçisi",
     "Kaliteyi gözden geçiren kişi; iç denetçi",
     "Hizmet kuruluşu; denetim ekibinin üyesi"],
    "BDS 620 prg. 6-a'ya göre denetçinin kanıt elde etmesine yardım etmek üzere çalışması kullanılan muhasebe veya denetim "
    "dışı alandaki kişi denetçinin faydalandığı uzmandır. BDS 500 prg. 5 ve 8'e göre işletmenin tabloları hazırlarken "
    "faydalandığı uzman yönetimin uzmanıdır ve çalışması BDS 500 prg. 8'e göre değerlendirilir.")

P.q("BDS 501 prg. 4-b",
    f"{B501}, stok sayımına katılımın yanı sıra denetçinin stoklara ilişkin yapması gereken aşağıdakilerden hangisidir?",
    "Nihai stok kayıtlarının gerçek sayım sonuçlarını doğru yansıtıp yansıtmadığını belirlemek",
    ["Sayım sonrası stok kayıtlarını yönetimin onayını alarak kendisi düzeltmek",
     "Stokların satış fiyatlarını belirleyerek yönetime önermek",
     "Sayımdan sonra stok hareketlerinin tamamını ertesi yıla devretmek",
     "Stok değerlemesini işletme adına yaparak tablolara kaydetmek"],
    "BDS 501 prg. 4-b'ye göre denetçi, sayıma katılımın yanı sıra işletmenin nihai stok kayıtları üzerinde, bu kayıtların "
    "gerçek stok sayım sonuçlarını doğru yansıtıp yansıtmadığını belirlemek üzere denetim prosedürleri uygular.")

P.q("BDS 505 prg. 13",
    f"{B505}, olumlu teyit yanıtının yeterli ve uygun kanıt elde etmek için zorunlu olduğu bir durumda yanıt "
    "alınamamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Alternatif prosedürler gerekli kanıtı sağlamaz; denetçi rapora etkisini değerlendirir.",
    ["Alternatif prosedürler olumlu teyitle eşdeğer kanıt sağlar.",
     "Yanıt alınamaması, bakiyenin doğru olduğunu gösterir ve test tamamlanır.",
     "Denetçi, yönetimden alacağı yazılı açıklamayla olumlu teyidin yerini doldurur.",
     "Denetçi teyit prosedürünü olumsuz teyide çevirerek sonucu olumlu kabul eder."],
    "BDS 505 prg. 13'e göre olumlu teyit yanıtının yeterli ve uygun kanıt için zorunlu olduğuna karar verilen durumda "
    "alternatif prosedürler gerekli kanıtı sağlamaz; yanıt alınamazsa denetçi BDS 705 uyarınca rapor ve görüş üzerindeki "
    "etkiyi belirler.", zorluk="hard")

P.q("BDS 620 prg. 13-15",
    f"{B620}, uzmanın çalışmasının denetçinin amaçları bakımından yeterli olmadığı durumlara ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Denetçi, raporunda uzmana atıf yaparak bu alandaki sorumluluğunu uzmana devreder.",
    ["Denetçi, uzmanın yapacağı ilave çalışmanın niteliği ve kapsamı hakkında uzmanla mutabakata varabilir.",
     "Denetçi, içinde bulunulan şartlara uygun ilave denetim prosedürlerini kendisi uygulayabilir.",
     "Olumlu dışında görüşün anlaşılması için uzmana atıf yapılırsa atfın sorumluluğu azaltmadığı belirtilir.",
     "Denetçi, denetim görüşünden uzmanın çalışmasını kullanmış olsa da tek başına sorumludur."],
    "BDS 620 prg. 13'e göre uzmanın çalışması yeterli değilse denetçi, ilave çalışma üzerinde uzmanla mutabakata varır "
    "veya şartlara uygun ilave prosedürler uygular. Prg. 3 ve 15'e göre denetçi görüşünden tek başına sorumludur; olumlu "
    "dışında görüşte uzmana atıf yapılırsa bu atıf sorumluluğu azaltmaz.")

if __name__ == "__main__":
    sys.exit(P.yaz())
