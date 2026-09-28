# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Hile ve Mevzuata Aykırılık — 60 soru, 2026 test biçimi.

Gerçek 2026/2 kitapçığında BDS 240'ın giriş paragraflarından (hile kaynaklı yanlışlığı tespit edememe riski,
yönetim hilesi, mesleki şüphecilik) “hangisi yanlıştır” biçiminde soru sorulmuştur.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · BDS 240 Finansal Tabloların Bağımsız Denetiminde Bağımsız Denetçinin Hileye İlişkin Sorumlulukları
  · BDS 250 Finansal Tabloların Bağımsız Denetiminde Mevzuatın Dikkate Alınması
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_hile_2026.json", lesson="denetim", topic="hile",
          konu_adi="Hile", seed=2026092846,
          surum="BDS 240 ve BDS 250 güncel metinleri; 28.09.2026 kontrolü")

H = "BDS 240 “Bağımsız Denetçinin Hileye İlişkin Sorumlulukları”na göre"
M = "BDS 250 “Finansal Tabloların Bağımsız Denetiminde Mevzuatın Dikkate Alınması”na göre"

# ================================================================ hilenin niteliği ve sorumluluk
P.q("BDS 240 prg. 2",
    f"{H}, finansal tablolarda yanlışlığa sebep olan hata ile hileyi birbirinden ayıran temel unsur aşağıdakilerden "
    "hangisidir?",
    "Eylemin kasıtlı olup olmaması",
    ["Tutarın önemliliği aşıp aşmaması", "Yönetim veya çalışanca yapılması",
     "Bilanço ya da gelir tablosunda olması", "Denetçice tespit edilip edilmemesi"],
    "BDS 240 prg. 2'ye göre finansal tablolardaki yanlışlıklar hata veya hileden kaynaklanabilir; ikisini ayıran unsur, "
    "yanlışlığa sebep olan eylemin kasıtlı olarak yapılıp yapılmadığıdır.", zorluk="easy")

P.q("BDS 240 prg. 3",
    f"{H}, denetçiyi ilgilendiren iki tür kasıtlı yanlışlık aşağıdakilerin hangisinde doğru verilmiştir?",
    "Hileli finansal raporlama ve varlıkların kötüye kullanılması",
    ["Muhasebe hataları ve kasıtlı mevzuat aykırılıkları",
     "Vergi kaçakçılığı ve kara para aklama",
     "Yönetim hilesi ve üçüncü taraf dolandırıcılığı",
     "Kayıt dışı satışlar ve hayali personel ödemeleri"],
    "BDS 240 prg. 3'e göre hile geniş bir hukuki kavram olsa da denetçi finansal tablolarda önemli yanlışlığa sebep olan "
    "hileyle ilgilenir ve bu kapsamda iki tür kasıtlı yanlışlık bulunur: hileli finansal raporlamadan ve varlıkların kötüye "
    "kullanılmasından kaynaklanan yanlışlıklar.")

P.q("BDS 240 prg. 3",
    f"{H}, hilenin varlığına ilişkin denetçinin konumuyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Denetçi hileden şüphelenebilir, ancak hilenin gerçekten olup olmadığına dair yasal bir hüküm veremez.",
    ["Denetçi, tespit ettiği her hilenin yasal niteliğine hükmederek sorumluları belirler.",
     "Denetçi hileyi tespit ettiğinde cezai sorumluluk için doğrudan savcılığa ihbarda bulunur ve kesin karar verir.",
     "Denetçi, hileyi ancak mahkeme kararı varsa denetim çalışmasında dikkate alabilir.",
     "Denetçinin hileyle ilgilenmesi, hile tutarının önemliliği aşıp aşmadığına bakılmaksızın yasal bir tespittir."],
    "BDS 240 prg. 3'e göre denetçi hilenin varlığından şüphelenebilir veya ender durumlarda hileyi tespit edebilir; ancak "
    "hilenin gerçekten olup olmadığına dair yasal bir hüküm veremez.")

P.q("BDS 240 prg. 4",
    f"{H}, hilenin önlenmesi ve tespit edilmesine ilişkin esas sorumluluk aşağıdakilerden hangisine aittir?",
    "Yönetime ve üst yönetimden sorumlu olanlara",
    ["Bağımsız denetçiye",
     "İç denetim birimine ve bağımsız denetçiye ortaklaşa",
     "Kamu Gözetimi Kurumuna",
     "Sadece işletmenin muhasebe müdürüne"],
    "BDS 240 prg. 4'e göre hilenin önlenmesi ve tespit edilmesine ilişkin esas sorumluluk yönetime ve üst yönetimden "
    "sorumlu olanlara aittir; bu, dürüstlük ve etik davranış kültürü oluşturma taahhüdünü içerir.", zorluk="easy")

P.q("BDS 240 prg. 6",
    f"{H}, hile kaynaklı önemli yanlışlığın tespit edilememe riskinin hata kaynaklı yanlışlığa göre daha yüksek "
    "olmasının sebebi aşağıdakilerden hangisidir?",
    "Hilenin, saklanmak üzere dikkatle tasarlanmış karmaşık planlar içerebilmesi",
    ["Hile kaynaklı yanlışlıkların tutarının genellikle daha büyük olması",
     "Hilenin sadece yıl sonu kapanış kayıtlarında ortaya çıkması",
     "Denetçilerin hileye yönelik prosedür uygulamasının standartlarca sınırlandırılmış olması",
     "Hile kaynaklı yanlışlıkların dipnotlarda değil sadece bilançoda yer alması"],
    "BDS 240 prg. 6'ya göre hile; sahtekârlık, işlemlerin kasten kaydedilmemesi veya denetçiye kasten gerçeğe aykırı "
    "açıklama yapılması gibi, saklanması amacıyla dikkatle tasarlanmış ve karmaşık planlar içerebilir; muvazaalı "
    "işlemlerle desteklendiğinde tespiti daha da zorlaşır.")

P.q("BDS 240 prg. 6-7",
    f"{H}, hilenin tespit edilebilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Çalışan hilesini tespit edememe riski, yönetim hilesine göre daha yüksektir.",
    ["Hilenin tespiti; suç işleyenin becerisine, manipülasyonun sıklığına ve kapsamına bağlıdır.",
     "Olaya karışan kişilerin kıdemi ve manipüle edilen tutarların nispî büyüklüğü tespiti etkiler.",
     "Muvazaalı işlemler, yanlış bir kanıtın ikna edici görünmesine yol açabilir.",
     "Tahmin gibi yargıya dayalı alanlarda yanlışlığın hata mı hile mi olduğuna karar vermek daha zordur."],
    "BDS 240 prg. 6'ya göre tespit; becerisine, sıklık ve kapsama, muvazaanın niteliğine, tutarların büyüklüğüne ve "
    "kişilerin kıdemine bağlıdır. Prg. 7'ye göre yönetim, kontrolleri ihlal edebilecek konumda olduğundan yönetim "
    "hilesini tespit edememe riski çalışan hilesine göre daha yüksektir.")

P.q("BDS 240 prg. 8",
    f"{H}, makul güvence elde ederken denetçinin mesleki şüpheciliğini denetim boyunca sürdürmesinin gerekçeleri "
    "arasında aşağıdakilerden hangisi yer alır?",
    "Hatayı ortaya çıkaran prosedürlerin hileyi ortaya çıkarmada etkin olmayabilmesi",
    ["Yönetimin kontrolleri ihlal etmesinin sadece halka açık işletmelerde mümkün olması",
     "Hile riskinin sadece denetimin planlama aşamasında değerlendirilmesi gerekliliği",
     "Mesleki şüpheciliğin denetim ücretini artırarak denetim kalitesini yükseltmesi",
     "Hata ve hileyi tespit eden prosedürlerin genellikle aynı olması"],
    "BDS 240 prg. 8'e göre denetçi, yönetimin kontrolleri ihlal etme ihtimalini ve hataların ortaya çıkarılmasında etkin "
    "olan prosedürlerin hilenin ortaya çıkarılmasında etkin olmayabileceğini göz önünde bulundurarak mesleki şüpheciliğini "
    "sürdürür.")

P.q("BDS 240 prg. 11",
    f"{H}, “hile riski faktörleri” aşağıdakilerden hangisinde doğru tanımlanmıştır?",
    "Hileye teşvik eden, baskı oluşturan veya fırsat sağlayan olay ya da durumlar",
    ["Denetçinin hileyi tespit edemediğinde karşılaşacağı hukuki yaptırımlar",
     "Hile sonucunda işletmenin uğradığı zararın tutarını gösteren göstergeler",
     "İşletmenin hile nedeniyle vergi idaresine ödediği ceza ve faizler",
     "Hileyi gerçekleştiren kişilerin eğitim ve kıdem düzeylerini gösteren kayıtlar"],
    "BDS 240 prg. 11-b'ye göre hile riski faktörleri, hile yapmaya teşvik eden, hile için baskı oluşturan veya hile "
    "yapma fırsatı sağlayan olay veya durumlardır. Prg. 11-a hileyi, haksız veya yasalara aykırı menfaat elde etmek için "
    "aldatma içeren kasıtlı eylemler olarak tanımlar.")

P.q("BDS 240 A1",
    f"{H}, hileli finansal raporlama ile varlıkların kötüye kullanılmasının ortak olarak içerdiği üç unsur aşağıdakilerin "
    "hangisinde doğru verilmiştir?",
    "Teşvik veya baskı, algılanan fırsat ve rasyonelleştirme",
    ["Kasıt, zarar ve illiyet bağı", "Fırsat, gizlilik ve yüksek tutar",
     "Baskı, muvazaa ve yönetim onayı", "Teşvik, iç kontrol eksikliği ve yasal hüküm"],
    "BDS 240 A1'e göre hile, ister hileli finansal raporlama ister varlıkların kötüye kullanılması şeklinde olsun; hile "
    "yapmaya yönelik teşvik veya baskıyı, algılanan bir fırsatı ve eylemin bir ölçüde rasyonelleştirilmesini içerir.")

P.q("BDS 240 A1",
    "Bir satış müdürünün prim sistemi tamamen yıl sonu satış hedefine bağlanmıştır. Müdür, hedefin gerisinde kalınca "
    f"yeni yılın ilk haftasındaki sevkiyatları eski yıl satışı olarak kaydettirmiştir. {H} prim sistemi hile üçgeninin "
    "hangi unsuruna örnektir?",
    "Teşvik veya baskı",
    ["Algılanan fırsat", "Rasyonelleştirme", "Muvazaa", "Kontrol ihlali"],
    "BDS 240 A1'e göre beklenen kazanç hedefine veya finansal sonuca ulaşma baskısı, özellikle prim veya ücret buna "
    "bağlıysa hileli finansal raporlamaya yönelik teşvik veya baskı oluşturur. Dönem kaydırması yoluyla hasılatın "
    "şişirilmesi hileli finansal raporlamaya örnektir.")

# ================================================================ mesleki şüphecilik ve ekip müzakeresi
P.q("BDS 240 prg. 12-14",
    f"{H}, hileye ilişkin mesleki şüphecilikle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetimin geçmişte dürüst olduğu biliniyorsa denetçi hile ihtimalini değerlendirmez.",
    ["Denetçi, yönetimin dürüstlüğüne ilişkin geçmiş tecrübesine bakmaksızın mesleki şüpheciliğini sürdürür.",
     "Aksini gerektiren bir gerekçe yoksa denetçi kayıt ve belgeleri gerçek kabul edebilir.",
     "Bir belgenin gerçek olmayabileceğine dair bulgu varsa denetçi araştırmasını derinleştirir.",
     "Yönetim ve üst yönetimden alınan cevaplar tutarsızsa denetçi bu tutarsızlıkları araştırır."],
    "BDS 240 prg. 12'ye göre denetçi, yönetimin ve üst yönetimin dürüstlüğüne ilişkin geçmiş tecrübesine bakmaksızın "
    "hile ihtimalinin bilinciyle mesleki şüpheciliğini sürdürür. Prg. 13 belgelerin gerçekliğini, prg. 14 tutarsız "
    "cevapların araştırılmasını düzenler.")

P.q("BDS 240 prg. 15",
    f"{H}, denetim ekibi içinde hileye ilişkin yapılan müzakereyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Müzakere, ekibin yönetimin dürüstlüğüne ilişkin kanaatlerinden bağımsız olarak yapılır.",
    ["Müzakere sadece yönetimin dürüstlüğünden şüphe edilen işletmelerde yapılır.",
     "Müzakereye sadece sorumlu denetçi ve kaliteyi gözden geçiren kişi katılır.",
     "Müzakere, tabloların nerede hataya açık olduğuyla sınırlıdır; hile konu edilmez.",
     "Müzakere sonuçları yönetimle paylaşılarak yönetimin görüşü alınır ve buna göre plan yapılır."],
    "BDS 240 prg. 15'e göre BDS 315 kapsamındaki ekip müzakeresinde hilenin nasıl meydana gelebileceği dahil tabloların "
    "nasıl ve nerede hile kaynaklı önemli yanlışlığa açık olabileceğine özel önem verilir ve müzakere ekip üyelerinin "
    "yönetimin dürüstlüğüne ilişkin kanaatlerinden bağımsız olarak yapılır.")

# ================================================================ risk değerlendirme
P.q("BDS 240 prg. 17",
    f"{H}, denetçinin hile risklerine ilişkin yönetimi sorgulaması gereken konular arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Yönetimin hile nedeniyle geçmişte işten çıkardığı personelin kişisel bilgileri",
    ["Tabloların hile kaynaklı önemli yanlışlık içerebileceği riskine ilişkin yönetimin yaptığı değerlendirmeler",
     "Yönetimin hile risklerini belirleme ve bunlara karşılık verme süreci",
     "Bu süreçlere ilişkin yönetimin üst yönetimden sorumlu olanlarla kurduğu iletişimler",
     "Yönetimin işletme uygulamaları ve etik davranış konusunda çalışanlarla kurduğu iletişimler"],
    "BDS 240 prg. 17'ye göre denetçi yönetimi; hile riskine ilişkin değerlendirmeleri, hile risklerini belirleme ve "
    "karşılık verme süreci, üst yönetimle ve çalışanlarla kurduğu iletişimler hakkında sorgular. Prg. 18 gerçekleşmiş veya "
    "şüphelenilen hileler hakkında sorgulamayı düzenler.")

P.q("BDS 240 prg. 18",
    f"{H}, denetçinin işletmeyi etkileyen gerçekleşmiş, şüphelenilen veya iddia edilen hileler hakkında bilgi olup "
    "olmadığını belirlemek için sorgulaması gerekenler aşağıdakilerden hangisidir?",
    "Yönetim ve uygun hâllerde işletmedeki diğer kişiler",
    ["Sadece işletmenin dış hukuk müşaviri",
     "Sadece işletmenin önceki yıllardaki denetçisi",
     "İşletmenin en büyük müşterileri ve tedarikçileri",
     "Vergi idaresi ve sosyal güvenlik kurumu yetkilileri"],
    "BDS 240 prg. 18'e göre denetçi, işletmeyi etkileyen gerçekleşmiş, şüphelenilen veya iddia edilen herhangi bir hile "
    "hakkında bilgileri olup olmadığını belirlemek amacıyla yönetimi ve uygun hâllerde işletmedeki diğer kişileri sorgular; "
    "iç denetim fonksiyonu ve üst yönetimden sorumlu olanlar da sorgulanır (prg. 19-21).")

P.q("BDS 240 prg. 26",
    f"{H}, hasılatın muhasebeleştirilmesine ilişkin hile riskine dair aşağıdakilerden hangisi doğrudur?",
    "Denetçi, hasılatın muhasebeleştirilmesinde hile riski bulunduğu varsayımıyla hareket eder.",
    ["Hasılat hile riski sadece hasılatı önceki yıla göre artan işletmelerde değerlendirilir.",
     "Hasılat hile riski iç kontrol eksikliği olarak raporlanır.",
     "Hasılat hile riski, satışlar nakden yapılıyorsa değerlendirilmez.",
     "Denetçi bu varsayımı uygulamadığında herhangi bir belgelendirme yapmaz."],
    "BDS 240 prg. 26'ya göre denetçi, hasılatın muhasebeleştirilmesinde hile risklerinin bulunduğu varsayımıyla hangi tür "
    "hasılatın veya işlemlerin bu riske sebep olabileceğini değerlendirir. Prg. 47'ye göre varsayımın geçerli olmadığına "
    "karar verirse bunun gerekçesini belgelendirir.")

P.q("BDS 240 prg. 26, 47",
    "Denetçi, tek bir kiracıdan sabit tutarlı kira geliri elde eden bir gayrimenkul şirketinde hasılatın "
    f"muhasebeleştirilmesine ilişkin hile riski varsayımının geçerli olmadığına karar vermiştir. {H} bu durumda "
    "denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Varsayımın geçerli olmadığına ilişkin kararının gerekçesini belgelendirir.",
    ["Kararı yönetimin onayına sunar ve onay alınmazsa varsayımı uygular.",
     "Varsayımı yine uygular; standart bu varsayımdan ayrılmaya izin vermez.",
     "Kararı üst yönetimden sorumlu olanlara yazılı olarak bildirerek dosyayı kapatır.",
     "Hasılatı risk değerlendirmesinden tamamen çıkarır ve prosedür uygulamaz."],
    "BDS 240 prg. 26 hasılatta hile riski bulunduğunu varsaymayı ister; prg. 47'ye göre denetçi, içinde bulunulan "
    "şartlarda bu varsayımın geçerli olmadığına karar vermişse bu kararın gerekçelerini belgelendirir.", zorluk="hard")

P.q("BDS 240 prg. 27",
    f"{H}, değerlendirilmiş hile kaynaklı önemli yanlışlık risklerinin ele alınmasıyla ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "Bu riskler ciddi risk olarak ele alınır.",
    ["Bu riskler sadece kontrol riski yüksekse ciddi risk sayılır.",
     "Bu riskler genellikle düşük riskli kabul edilerek analitik prosedürlerle test edilir.",
     "Bu risklere ilişkin işletmenin kontrollerini anlamak zorunlu değildir.",
     "Bu riskler sadece tutarı önemliliği aşıyorsa değerlendirmeye alınır."],
    "BDS 240 prg. 27'ye göre denetçi, değerlendirilmiş hile kaynaklı önemli yanlışlık risklerini ciddi riskler olarak ele "
    "alır ve henüz yapılmadıysa kontrol faaliyetleri dahil bu risklere yönelik kontrolleri anlar.", zorluk="easy")

P.q("BDS 240 prg. 21-24",
    f"{H}, hile riski faktörleri ve olağan dışı ilişkilere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hile riski faktörü bulunması, hilenin gerçekleştiğinin kanıtı sayılır.",
    ["Denetçi, elde ettiği bilgilerin bir veya daha fazla hile riski faktörünün varlığını gösterip göstermediğini değerlendirir.",
     "Analitik prosedürlerde belirlenen olağan dışı veya beklenmeyen ilişkiler hile riskine işaret edebilir.",
     "Üst yönetimden sorumlu olanların hile risklerini nasıl gözettiğine ilişkin bilgi edinilir.",
     "Hile riski faktörleri, hile olmasa da hilenin gerçekleşebileceği durumları gösterebilir."],
    "BDS 240 prg. 22-24'e göre denetçi hile riski faktörlerinin varlığını ve olağan dışı ilişkileri değerlendirir. A24'e "
    "göre hile riski faktörleri hilenin varlığını göstermez; ancak hilenin gerçekleştiği durumlarda sıkça bulunur ve hile "
    "kaynaklı risklerin göstergesi olabilir.")

# ================================================================ karşılıklar ve yönetim ihlali
P.q("BDS 240 prg. 29",
    f"{H}, finansal tablo düzeyindeki hile kaynaklı risklere karşı genel işler belirlenirken denetçinin yapması "
    "gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Hile riskini azaltmak için önemlilik düzeyini yükseltip test edilecek kalem sayısını azaltmak",
    ["Personeli risk değerlendirmesini ve kişilerin bilgi, beceri ve kabiliyetlerini dikkate alarak görevlendirmek",
     "Muhasebe politikalarının seçim ve uygulamasının kazanç yönetimine işaret edip etmediğini değerlendirmek",
     "Prosedürlerin niteliği, zamanlaması ve kapsamının seçimine öngörülemezlik unsuru eklemek",
     "Önemli sorumluluk verilen kişileri risk düzeyine uygun şekilde yönlendirmek ve gözetmek"],
    "BDS 240 prg. 29'a göre denetçi personeli risk ve yetkinliklere göre görevlendirir, yönlendirir ve gözetir; subjektif "
    "ölçüm ve karmaşık işlemlerdeki muhasebe politikalarının kazanç yönetimine işaret edip etmediğini değerlendirir ve "
    "öngörülemezlik unsuru ekler.")

P.q("BDS 240 prg. 31",
    f"{H}, kontrollerin yönetim tarafından ihlal edilmesi riskine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu risk sadece iç kontrol sistemi zayıf olan işletmelerde bulunur.",
    ["Yönetim, etkin görünen kontrolleri ihlal ederek kayıtları manipüle edebilecek özel bir konumdadır.",
     "Riskin seviyesi işletmeden işletmeye farklılık gösterir.",
     "İhlallerin nasıl ortaya çıkacağı öngörülebilir olmadığından bu risk ciddi bir risktir.",
     "Bu risk hile kaynaklı önemli bir yanlışlık riskidir."],
    "BDS 240 prg. 31'e göre yönetim etkin görünen kontrolleri ihlal edebilecek özel bir konumdadır; riskin seviyesi "
    "işletmeden işletmeye değişse de bu risk tüm işletmelerde mevcuttur ve öngörülemez olduğundan hile kaynaklı ciddi bir "
    "risktir.")

P.q("BDS 240 prg. 32",
    f"{H}, kontrollerin yönetim tarafından ihlal edilmesi riskine karşı denetçinin, risk değerlendirmesinden bağımsız "
    "olarak uygulaması gereken prosedürler arasında aşağıdakilerden hangisi yer almaz?",
    "Satış gelirlerinin tamamı için müşterilere olumsuz teyit gönderilmesi",
    ["Defteri kebire aktarılan yevmiye kayıtlarının ve diğer düzeltmelerin uygunluğunun test edilmesi",
     "Muhasebe tahminlerinin taraflılık açısından gözden geçirilmesi",
     "Olağan iş akışı dışındaki önemli işlemlerin iş mantığının değerlendirilmesi",
     "Önceki yıl önemli tahminlerindeki yargı ve varsayımların geriye dönük gözden geçirilmesi"],
    "BDS 240 prg. 32'ye göre denetçi, riske ilişkin değerlendirmesinden bağımsız olarak yevmiye kayıtları ve "
    "düzeltmelerin test edilmesi, tahminlerin (geriye dönük gözden geçirme dahil) taraflılık açısından gözden geçirilmesi "
    "ve olağan dışı önemli işlemlerin iş mantığının değerlendirilmesi prosedürlerini uygular.")

P.q("BDS 240 prg. 32-a",
    f"{H}, yevmiye kayıtları ve diğer düzeltmelerin test edilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Raporlama dönemi sonunda yapılan kayıt ve düzeltmeler seçilerek test edilir.",
    ["Sadece dönem içindeki sistem tarafından üretilen kayıtlar test edilir; kapanış kayıtları kapsam dışıdır.",
     "Yevmiye kayıtları sadece yönetimin talep ettiği hesaplarda test edilir.",
     "Kayıtlar test edilmez; sadece muhasebe personeline sorgulama yapılır.",
     "Yevmiye kayıtları testi sadece iç kontrolü zayıf işletmelerde uygulanır."],
    "BDS 240 prg. 32-a'ya göre denetçi, yevmiye kayıtlarına ilişkin uygun olmayan veya olağan dışı işlemler hakkında "
    "finansal raporlama sürecindeki kişileri sorgular, dönem sonunda yapılan kayıt ve düzeltmeleri seçer ve dönem boyunca "
    "yapılanları test etmenin gerekli olup olmadığını mütalaa eder.")

P.q("BDS 240 prg. 32-b",
    "Denetçi, işletmenin şüpheli alacak, stok değer düşüklüğü ve garanti karşılığı tahminlerinin her birinin tek tek "
    "makul aralıkta olduğunu, ancak hepsinin kârı artıracak yönde aralığın uç noktasına yakın seçildiğini tespit etmiştir. "
    f"{H} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Muhtemel yönetim taraflılığı nedeniyle tahminleri bir bütün olarak yeniden değerlendirir.",
    ["Her tahmin tek başına makul olduğundan başka bir değerlendirme yapmaz.",
     "Tahminlerin tamamını aralığın orta noktasına çekecek düzeltme kayıtlarını kendisi yapar.",
     "Durumu tahmin belirsizliği sayarak raporunda dikkat çekilen hususlarda açıklar.",
     "Tahminleri gelecek yıl gerçekleşen sonuçlarla karşılaştırmak üzere değerlendirmeyi erteler."],
    "BDS 240 prg. 32-b-i'ye göre denetçi, tahminlerdeki muhakeme ve kararların münferit olarak makul olsalar bile yönetimin "
    "muhtemel taraflılığına işaret edip etmediğini değerlendirir; böyle bir ihtimal varsa muhasebe tahminlerini bir bütün "
    "olarak yeniden değerlendirir.", zorluk="hard")

P.q("BDS 240 prg. 32-c",
    "Bir işletme, yıl sonundan birkaç gün önce ilişkili olmayan bir şirkete iş mantığı açıklanamayan yüksek tutarlı bir "
    f"danışmanlık ödemesi yapmış ve ödeme ocak ayında aynı şirketten iade alınmıştır. {H} denetçinin bu işleme ilişkin "
    "yapması gereken aşağıdakilerden hangisidir?",
    "İşlemin iş mantığının hile amacına işaret edip etmediğini değerlendirir.",
    ["İşlem tutarı faturayla desteklendiği için başka bir değerlendirme yapmaz.",
     "İşlemi, sonraki dönemde iade edildiği için denetim kapsamı dışında bırakır.",
     "İşlemi, yönetimin yazılı açıklamasını alarak olağan işlem kabul eder.",
     "İşlemi doğrudan hile olarak niteleyip savcılığa bildirir."],
    "BDS 240 prg. 32-c'ye göre olağan iş akışı dışında gerçekleştirilen veya olağan dışı görünen önemli işlemlerde denetçi, "
    "iş mantığının veya iş mantığından yoksunluğun hileli finansal raporlama ya da varlıkların kötüye kullanımının "
    "gizlenmesi amacına işaret edip etmediğini değerlendirir.")

P.q("BDS 240 prg. 34",
    f"{H}, denetimin sonuna doğru uygulanan analitik prosedürlerle ilgili aşağıdakilerden hangisi doğrudur?",
    "Daha önce belirlenmemiş bir hile riskine işaret edip etmedikleri değerlendirilir.",
    ["Bu prosedürler sadece önemlilik düzeyinin yeniden hesaplanması için kullanılır.",
     "Bu aşamada hile riskinin yeniden değerlendirilmesi standartça yasaklanmıştır.",
     "Analitik prosedürler denetimin sonunda uygulanmaz; sadece planlamada kullanılır.",
     "Bu prosedürlerin sonuçları yönetimin onayı olmadan dikkate alınmaz."],
    "BDS 240 prg. 34'e göre denetçi, tabloların işletme hakkındaki bilgilerle tutarlı olup olmadığına ilişkin genel sonuca "
    "ulaşırken denetimin sonuna doğru uygulanan analitik prosedürlerin daha önce belirlenmemiş bir hile riskine işaret edip "
    "etmediğini değerlendirir.")

# ================================================================ yanlışlıkların değerlendirilmesi
P.q("BDS 240 prg. 35",
    f"Denetçi, tespit ettiği bir yanlışlığın hile göstergesi olabileceği kanaatine varmıştır. {H} bu durumda denetçinin "
    "yaklaşımı aşağıdakilerden hangisidir?",
    "Hilenin münferit bir vaka olma ihtimalinin düşük olduğunu kabul eder.",
    ["Yanlışlığı münferit bir vaka kabul ederek sadece o kaydı düzelttirir.",
     "Yanlışlık önemsizse hile göstergesini dikkate almadan denetime devam eder.",
     "Yönetimin açıklamalarının güvenilirliğini sorgulamaz; sadece tutarı değerlendirir.",
     "Hile göstergesini üst yönetime bildirmeden, bir sonraki yılın denetim planına not eder."],
    "BDS 240 prg. 35'e göre yanlışlık hile göstergesi ise denetçi, gerçekleşmiş bir hilenin münferit bir vaka olma "
    "ihtimalinin düşük olduğunu kabul ederek, özellikle yönetimin beyan ve açıklamalarının güvenilirliği olmak üzere "
    "denetimin tüm aşamalarına etkisini değerlendirir.")

P.q("BDS 240 prg. 36",
    "Denetçi, tutarı önemsiz olan bir yanlışlığın hileden kaynaklandığına ve buna üst düzey bir yöneticinin dahil "
    f"olduğuna inanmak için gerekçesi bulunduğunu tespit etmiştir. {H} bu duruma ilişkin aşağıdakilerden hangisi "
    "yanlıştır?",
    "Yanlışlık önemsiz olduğundan risk değerlendirmesinde değişiklik yapılmaz.",
    ["Denetçi, hile kaynaklı risklere ilişkin değerlendirmesini yeniden değerlendirir.",
     "Denetçi, değerlendirilmiş risklere karşılık veren prosedürlere etkisini yeniden değerlendirir.",
     "Denetçi, önceki kanıtların güvenilirliğini değerlendirirken muvazaalı bir işlem ihtimalini mütalaa eder.",
     "Yönetimin dahil olduğu hile şüphesi üst yönetimden sorumlu olanlara bildirilir."],
    "BDS 240 prg. 36'ya göre önemli ya da önemsiz bir yanlışlığın hileden kaynaklandığına ve yönetimin (özellikle üst "
    "düzey yöneticilerin) dahil olduğuna inanmak için gerekçe varsa denetçi risk değerlendirmesini ve prosedürlere etkisini "
    "yeniden değerlendirir ve muvazaa ihtimalini mütalaa eder; prg. 41 üst yönetime bildirimi düzenler.", zorluk="hard")

P.q("BDS 240 prg. 38",
    "Hile şüphesi nedeniyle denetçi, denetime devam etme imkânının sorgulanmasına sebep olan istisnai bir durumla "
    f"karşılaşmıştır. {H} denetçinin yapması gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Mevzuata bakmaksızın denetimden derhâl ve gerekçe bildirmeden çekilmek",
    ["Denetçiyi seçenlere veya düzenleyici kurumlara raporlama zorunluluğu dahil mesleki ve yasal sorumluluklarını belirlemek",
     "Mevzuata göre mümkünse denetimden çekilmenin uygun olup olmadığını mütalaa etmek",
     "Çekilirse bunu ve gerekçelerini uygun yöneticiler ve üst yönetimden sorumlu olanlarla müzakere etmek",
     "Çekilme ve gerekçelerini denetçiyi seçenlere veya düzenleyicilere raporlama yükümlülüğü olup olmadığına karar vermek"],
    "BDS 240 prg. 38'e göre denetçi mesleki ve yasal sorumluluklarını belirler, mevzuat izin veriyorsa çekilmenin "
    "uygunluğunu mütalaa eder; çekilirse bunu ve gerekçelerini yönetim ve üst yönetimle müzakere eder ve seçenlere veya "
    "düzenleyici kurumlara raporlama yükümlülüğü olup olmadığına karar verir.")

# ================================================================ yazılı açıklama ve iletişim
P.q("BDS 240 prg. 39",
    f"{H}, denetçinin hileye ilişkin olarak yönetimden alacağı yazılı açıklamalar arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Denetçinin hileyi tespit etmek için yeterli prosedür uyguladığının yönetimce onaylanması",
    ["Hilenin önlenmesi ve tespiti için iç kontrolü tasarlama, uygulama ve sürdürme sorumluluğunu kabul ettikleri",
     "Tabloların hile kaynaklı yanlışlık içerebileceği riskine ilişkin değerlendirmelerinin sonuçlarını açıkladıkları",
     "Yönetimi veya kilit çalışanları içeren bilinen ya da şüphelenilen hileleri açıkladıkları",
     "Çalışanlar veya düzenleyiciler tarafından iletilen hile iddialarına ilişkin bilgileri açıkladıkları"],
    "BDS 240 prg. 39'a göre denetçi yönetimden; iç kontrol sorumluluğunu kabul ettiklerine, hile riskine ilişkin "
    "değerlendirmelerinin sonuçlarını ve bilinen ya da şüphelenilen hileler ile hile iddialarına ilişkin bilgileri "
    "açıkladıklarına dair yazılı açıklama alır. Prosedürlerin yeterliliği denetçinin sorumluluğudur.")

P.q("BDS 240 prg. 40-41",
    "Denetçi, satın alma müdürünün tedarikçilerle muvazaalı fatura düzenleyerek işletmeyi zarara uğrattığına dair bilgi "
    f"edinmiştir. {H} denetçinin bu durumdaki iletişim yükümlülüğü aşağıdakilerden hangisidir?",
    "Konuyu zamanında yönetimin uygun kademesine bildirir.",
    ["Konuyu sadece denetim raporunun diğer hususlar paragrafında açıklar ve başkaca bildirimde bulunmaz.",
     "Sır saklama yükümlülüğü nedeniyle konuyu işletme içinde kimseye bildirmez.",
     "Konuyu doğrudan satın alma müdürüyle görüşerek tazminat ödemesini sağlar.",
     "Konuyu bildirmeden önce hilenin mahkeme kararıyla kesinleşmesini bekler."],
    "BDS 240 prg. 40'a göre denetçi hileyi tespit ettiğinde veya hile olabileceğine dair bilgi edindiğinde, hilenin "
    "önlenmesinden esas sorumlu kişileri bilgilendirmek için konuyu yönetimin uygun kademesine zamanında bildirir. Prg. "
    "41'e göre iç kontrolde önemli görevi olan çalışanların dahil olduğu hileler üst yönetimden sorumlu olanlara da "
    "bildirilir.", zorluk="hard")

P.q("BDS 240 prg. 43",
    f"{H}, hile veya hile şüphesinin işletme dışındaki bir tarafa raporlanmasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Denetçi raporlama sorumluluğu olup olmadığına karar verir; yasal sorumluluk gizliliği kaldırabilir.",
    ["Sır saklama yükümlülüğü, hangi koşulda olursa olsun dış taraflara raporlama yapılmasına izin vermez.",
     "Denetçi her hile şüphesini yönetime danışmadan vergi idaresine raporlar.",
     "Dış taraflara raporlama sadece hile tutarı önemliliği aşarsa zorunludur.",
     "Dış taraflara raporlama kararı denetlenen işletmenin yönetimine aittir."],
    "BDS 240 prg. 43'e göre denetçi, hile veya hile şüphesini işletme dışındaki bir tarafa raporlama sorumluluğu olup "
    "olmadığına karar verir; sır saklama yükümlülüğü bu raporlamayı engelleyebilir, ancak bazı durumlarda yasal "
    "sorumluluklar gizlilik yükümlülüğünü ortadan kaldırabilir.")

P.oncul("BDS 240 prg. 6-8",
    f"{H} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Hile kaynaklı önemli yanlışlığı tespit edememe riski, hata kaynaklı yanlışlığı tespit edememe riskinden yüksektir.",
     "Yönetim hilesini tespit edememe riski, çalışan hilesini tespit edememe riskinden yüksektir.",
     "Hataları ortaya çıkaran prosedürler hileyi ortaya çıkarmada da aynı ölçüde etkilidir.",
     "Hile yapılmasına fırsat oluşturan durumlar, tahmin gibi yargı alanlarındaki yanlışlığın niteliğine göre daha kolay belirlenir."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "BDS 240 prg. 6'ya göre hile kaynaklı yanlışlığı tespit edememe riski daha yüksektir (I) ve fırsat oluşturan "
    "durumlar, yargı alanlarındaki yanlışlığın hata mı hile mi olduğundan daha kolay belirlenir (IV). Prg. 7 yönetim "
    "hilesine ilişkin riski daha yüksek sayar (II). Prg. 8'e göre hatayı ortaya çıkaran prosedürler hilede etkin "
    "olmayabilir (III yanlış).", zorluk="hard")

# ================================================================ BDS 250: mevzuat
P.q("BDS 250 prg. 6",
    f"{M}, vergi ve sosyal güvenlik mevzuatı gibi hükümlerin sınıflandırılmasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Tablolardaki önemli tutar ve açıklamalar üzerinde doğrudan etkisi olan mevzuattır.",
    ["Tablolar üzerinde doğrudan etkisi olmayan, sadece faaliyet izniyle ilgili mevzuattır.",
     "Denetçinin uygunluğuna dair kanıt toplamadığı mevzuattır.",
     "Sadece yönetimin sorumluluğunda olduğu için denetim kapsamı dışındaki mevzuattır.",
     "Uygunluğu sadece yönetimin yazılı açıklamasıyla değerlendirilen mevzuattır."],
    "BDS 250 prg. 6'ya göre denetçi iki sınıf mevzuatı ayırır: (a) vergi ve sosyal güvenlik mevzuatı gibi tablolardaki "
    "önemli tutar ve açıklamaların belirlenmesinde doğrudan etkisi olduğu genel kabul gören mevzuat, (b) doğrudan etkisi "
    "olmayan ancak uygunluğu faaliyetler veya ceza riski bakımından önemli olabilecek diğer mevzuat.")

P.q("BDS 250 prg. 14",
    f"{M}, tablolardaki önemli tutar ve açıklamalar üzerinde doğrudan etkisi olduğu genel kabul gören mevzuata ilişkin "
    "denetçinin sorumluluğu aşağıdakilerden hangisidir?",
    "Uygunluk sağlandığına dair yeterli ve uygun kanıt elde etmek",
    ["Sadece yönetimi sorgulamak ve cevabı kayda almak",
     "Mevzuata uygunluk hakkında ayrı bir güvence raporu düzenlemek",
     "Aykırılık şüphesi yoksa herhangi bir prosedür uygulamamak",
     "Uygunluğu vergi müfettişinin raporuna dayanarak kabul etmek"],
    "BDS 250 prg. 14'e göre denetçi, tablolardaki önemli tutar ve açıklamaların belirlenmesinde doğrudan etkisi olduğu "
    "genel kabul gören mevzuat hükümlerine uygunluk sağlandığına dair yeterli ve uygun denetim kanıtı elde eder.", zorluk="easy")

P.q("BDS 250 prg. 15, 18",
    f"{M}, tablolar üzerinde doğrudan etkisi olmayan diğer mevzuata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Şüphe olmasa da bu mevzuata uygunluk için kapsamlı prosedür uygulanır.",
    ["Denetçi, yönetimi ve uygun hâllerde üst yönetimden sorumlu olanları uygunluk konusunda sorgular.",
     "Denetçi, varsa lisans veren veya düzenleyici kurumlarla yapılan yazışmaları tetkik eder.",
     "Tespit edilen veya şüphelenilen aykırılık yoksa denetçi belirtilen prosedürler dışında prosedür uygulamaz.",
     "Diğer prosedürler de denetçinin dikkatini aykırılık olabilecek durumlara çekebilir."],
    "BDS 250 prg. 15'e göre diğer mevzuat için denetçi yönetimi sorgular ve düzenleyici kurumlarla yazışmaları tetkik eder; "
    "prg. 16'ya göre diğer prosedürler de aykırılıklara dikkat çekebilir. Prg. 18'e göre aykırılık tespiti veya şüphesi "
    "yoksa bu prosedürler dışında uygunluk prosedürü uygulanmaz.")

P.q("BDS 250 prg. 19",
    f"Denetçi, işletmenin çevre mevzuatına aykırı atık depolaması yaptığından şüphelenmektedir. {M} denetçinin ilk "
    "yapması gereken aşağıdakilerden hangisidir?",
    "Fiilin niteliği ve şartları hakkında kanaat edinip muhtemel etkileri için bilgi toplamak",
    ["Konuyu doğrudan çevre bakanlığına yönetime haber vermeden ihbar etmek",
     "Denetimi derhâl durdurmak ve sözleşmeyi feshetmek",
     "Şüpheyi yönetimin sorumluluğunda sayarak dikkate almamak",
     "Aykırılık kesinleşene kadar olumsuz görüş vermek"],
    "BDS 250 prg. 19'a göre mevzuata aykırı olan veya aykırı olduğundan şüphelenilen bir durumdan haberdar olan denetçi, "
    "fiilin niteliğine ve hangi şartlar altında gerçekleştiğine dair kanaat edinir ve tablolar üzerindeki muhtemel "
    "etkilerini değerlendirmek için daha fazla bilgi elde eder.")

P.q("BDS 250 prg. 23",
    f"{M}, tespit edilen veya şüphelenilen aykırılıkların üst yönetimden sorumlu olanlara bildirilmesine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Açıkça önemsiz olanlar dışında, mevzuat yasaklamadıkça bildirilir.",
    ["Sadece tutarı önemliliği aşan aykırılıklar bildirilir.",
     "Aykırılıklar üst yönetime değil, sadece vergi idaresine bildirilir.",
     "Aykırılıklar, yönetim onay verirse üst yönetime bildirilir.",
     "Aykırılıklar sadece denetçi raporunda açıklanır; ayrıca bildirilmez."],
    "BDS 250 prg. 23'e göre üst yönetimden sorumlu olanların tamamı yönetimde yer almıyorsa denetçi, açıkça önemsiz "
    "olanlar dışında, denetim sırasında dikkatini çeken tespit edilen veya şüphelenilen aykırılıkları mevzuatla "
    "yasaklanmadığı sürece üst yönetimden sorumlu olanlara bildirir.")

P.q("BDS 250 prg. 28",
    "Denetçi, işletmenin kontrolü dışındaki şartlar nedeniyle (ör. belgelerin yangında yok olması) önemli bir mevzuat "
    f"aykırılığının gerçekleşip gerçekleşmediğine karar verememektedir. {M} denetçinin yapması gereken aşağıdakilerden "
    "hangisidir?",
    "BDS 705'e göre görüşü üzerindeki etkisini değerlendirir.",
    ["Aykırılığın gerçekleşmediğini varsayarak olumlu görüş verir.",
     "Aykırılığın gerçekleştiğini varsayarak olumsuz görüş verir.",
     "Kararı yönetime bırakır ve yönetimin açıklamasını raporuna aynen alır.",
     "Durumu raporunda açıklamaz, bir sonraki yıl yeniden değerlendirir."],
    "BDS 250 prg. 28'e göre denetçi, yönetim veya üst yönetimden ziyade şartların getirdiği kısıtlamalar sebebiyle "
    "aykırılığın gerçekleşip gerçekleşmediğine karar veremezse BDS 705'e uygun olarak bunun görüşü üzerindeki etkisini "
    "değerlendirir.")

P.q("BDS 250 prg. 29",
    f"{M}, tespit edilen veya şüphelenilen bir aykırılığın yetkili bir kuruma rapor edilmesine ilişkin denetçinin "
    "karar vermesi gereken husus aşağıdakilerden hangisidir?",
    "Mevzuat ve etik hükümlerin raporlamayı gerektirip gerektirmediği",
    ["Aykırılığın işletmenin vergi yükünü artırıp artırmadığı",
     "Yönetimin raporlamaya itiraz edip etmediği",
     "Aykırılık tutarının denetim ücretini aşıp aşmadığı",
     "Rapor etmenin denetim şirketinin itibarını etkileyip etkilemeyeceği"],
    "BDS 250 prg. 29'a göre denetçi, mevzuat ve etik hükümlerin durumu yetkili bir kuruma rapor etmesini zorunlu kılıp "
    "kılmadığına ve içinde bulunulan şartlarda rapor etmenin uygun olup olmadığı konusunda sorumluluk yükleyip "
    "yüklemediğine karar verir.")

P.q("BDS 250 prg. 13",
    f"{M}, denetçinin işletme ve çevresini tanıma sürecinin parçası olarak mevzuata ilişkin edinmesi gereken kanaat "
    "aşağıdakilerden hangisidir?",
    "Geçerli yasal ve düzenleyici çerçeve ile işletmenin bu çerçeveye nasıl uyduğu",
    ["Sadece işletmenin ödemediği vergi borçlarının listesi",
     "İşletmenin rakiplerinin mevzuata uyum düzeyi",
     "Mevzuatın gelecekte nasıl değişeceğine ilişkin tahminler",
     "Denetçinin kendi şirketinin mevzuata uyum politikası"],
    "BDS 250 prg. 13'e göre denetçi, işletme ve faaliyet gösterdiği sektör için geçerli olan yasal ve düzenleyici çerçeve "
    "ile işletmenin bu çerçeveye nasıl uygunluk sağladığına dair genel bir kanaat edinir.")

P.q("BDS 250 prg. 22",
    f"{M}, tespit edilen veya şüphelenilen aykırılıkların denetimin diğer alanlarına etkisine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Açıklamaların güvenilirliği ve risk değerlendirmesi dahil etkiler değerlendirilir.",
    ["Aykırılıklar sadece ilgili hesap bakiyesini etkiler; diğer alanlara bakılmaz.",
     "Aykırılıklar tespit edilince yazılı açıklama alma yükümlülüğü ortadan kalkar.",
     "Aykırılıkların etkisini yönetim değerlendirir; denetçi bu değerlendirmeyi aynen kabul eder.",
     "Aykırılıklar sadece bir sonraki yılın risk değerlendirmesinde dikkate alınır."],
    "BDS 250 prg. 22'ye göre denetçi, yazılı açıklamaların güvenilirliği ile yaptığı risk değerlendirmesi dahil tespit "
    "edilen veya şüphelenilen aykırılıkların denetimin diğer alanları üzerindeki etkilerini değerlendirir ve uygun "
    "adımları atar.")

P.q("BDS 250 prg. 24",
    "Denetçi, üst yönetimden sorumlu olanlara bildirdiği bir mevzuat aykırılığının kasıtlı ve önemli olduğu yargısına "
    f"varmıştır. {M} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Konuyu en kısa sürede üst yönetimden sorumlu olanlara bildirir.",
    ["Aykırılığı yönetimle gizlice uzlaşarak dosyadan çıkarır.",
     "Konuyu sadece bir sonraki yılın denetim sözleşmesinde yer verilmek üzere not eder.",
     "Aykırılığı bildirmeden önce yönetimin yazılı onayını alır ve onay yoksa bildirmez.",
     "Kasıtlı aykırılıklar denetçinin sorumluluğu dışında olduğundan işlem yapmaz."],
    "BDS 250 prg. 24'e göre denetçi, aykırılığın kasıtlı ve önemli olduğu yargısına varırsa konuyu mümkün olan en kısa "
    "sürede üst yönetimden sorumlu olanlara bildirir; prg. 25'e göre yönetimin veya üst yönetimin dahil olduğundan "
    "şüphelenirse daha üst bir yetkiliye bildirmeyi değerlendirir.")

P.q("BDS 240 prg. 44",
    f"{H}, hileye ilişkin belgelendirmede yer alması gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Hile şüphesi bulunan çalışanların maaş bordrolarının tamamı",
    ["Ekip içinde hileye ilişkin yapılan müzakerede alınan önemli kararlar",
     "Finansal tablo ve yönetim beyanı düzeyinde belirlenen ve değerlendirilen hile riskleri",
     "Değerlendirilen risklere karşı yapılan genel işler ve prosedürlerin riskle bağlantısı",
     "Hileye ilişkin yönetim, üst yönetim ve düzenleyicilerle kurulan iletişimler"],
    "BDS 240 prg. 44-47'ye göre denetçi, ekip müzakeresindeki önemli kararları, belirlenen ve değerlendirilen hile "
    "risklerini, bunlara karşı yapılan işleri ve prosedürlerin riskle bağlantısını, prosedür sonuçlarını ve hileye ilişkin "
    "iletişimleri belgelendirir.")

P.q("BDS 240 A1",
    "Bir depo sorumlusu, işletmenin stok sayımı kontrolünün yılda bir kez yapıldığını ve sayım farklarının "
    f"araştırılmadığını bildiği için stoklardan ürün almaktadır. {H} bu durumda kontrol zayıflığı hile üçgeninin hangi "
    "unsurunu oluşturur?",
    "Algılanan fırsat",
    ["Teşvik veya baskı", "Rasyonelleştirme", "Yönetimin kontrol ihlali", "Hileli finansal raporlama"],
    "BDS 240 A1'e göre hile, teşvik veya baskıyı, algılanan fırsatı ve rasyonelleştirmeyi içerir. Kontrollerin zayıf "
    "olması veya kontrollerin ihlal edilebileceğine dair inanç fırsat oluşturur. Stoktan ürün alınması varlıkların kötüye "
    "kullanılmasına örnektir.")

P.q("BDS 240 A1-A5",
    f"{H}, aşağıdakilerden hangisi varlıkların kötüye kullanılmasına örnektir?",
    "Çalışanın müşteri tahsilatlarını kendi hesabına aktarması",
    ["Yönetimin yıl sonu satışlarını erken muhasebeleştirmesi",
     "Karşılıkların kâr hedefine göre düşük hesaplanması",
     "Önemli bir ilişkili taraf işleminin dipnotlarda gizlenmesi",
     "Muhasebe politikalarının kasten yanlış uygulanması"],
    "BDS 240 A5'e göre varlıkların kötüye kullanılması; tahsilatların zimmete geçirilmesi, varlıkların çalınması veya "
    "işletmenin almadığı mal ve hizmetler için ödeme yapılması gibi yollarla gerçekleşir. Diğer seçenekler hileli "
    "finansal raporlamaya örnektir (A3-A4).")

P.q("BDS 240 prg. 19-20",
    f"{H}, iç denetim fonksiyonu olan bir işletmede denetçinin hile risklerine ilişkin iç denetim fonksiyonundaki "
    "kişileri sorgulama amacı aşağıdakilerden hangisidir?",
    "Gerçekleşmiş, şüphelenilen veya iddia edilen hileler hakkındaki bilgilerini öğrenmek",
    ["İç denetçilerin hileyi tespit etme sorumluluğunu denetçiye devretmesini sağlamak",
     "İç denetim raporlarının tamamını denetim görüşünün yerine kullanmak",
     "İç denetçilerin ücretlerini ve performanslarını değerlendirmek",
     "İç denetim birimine hile incelemesi yapma talimatı vermek"],
    "BDS 240 prg. 19'a göre iç denetim fonksiyonu olan işletmelerde denetçi, iç denetim fonksiyonundaki uygun kişileri "
    "gerçekleşmiş, şüphelenilen veya iddia edilen hileler ve hile risklerine ilişkin görüşleri hakkında sorgular; prg. 20 "
    "üst yönetimin gözetimi hakkında kanaat edinilmesini düzenler.")

# ================================================================ ek sorular (olumsuz kök)
P.q("BDS 240 prg. 11-a",
    f"{H}, hile kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hile sadece yönetim tarafından yapılabilir; çalışanların kasıtlı eylemleri hata sayılır.",
    ["Hile, haksız veya yasalara aykırı menfaat elde etmek amacıyla yapılan kasıtlı eylemlerdir.",
     "Hile, yönetim, üst yönetim, çalışanlar veya üçüncü taraflarca yapılabilir.",
     "Hile aldatma içerir ve bir veya birden fazla kişi tarafından gerçekleştirilebilir.",
     "Hile ile hatayı ayıran unsur, eylemin kasıtlı olarak yapılıp yapılmadığıdır."],
    "BDS 240 prg. 11-a'ya göre hile; yönetim, üst yönetimden sorumlu olanlar, çalışanlar veya üçüncü taraflardan bir veya "
    "birden fazla kişinin haksız veya yasalara aykırı menfaat elde etmek amacıyla yaptığı aldatma içeren kasıtlı "
    "eylemleridir; prg. 2'ye göre hatadan farkı kasıttır.")

P.q("BDS 240 prg. 4-5",
    f"{H}, hileye ilişkin sorumluluklarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "BDS'lere uygun denetim yapan denetçi, tüm hile kaynaklı yanlışlıkları tespit etmekle sorumludur.",
    ["Hilenin önlenmesi ve tespitine ilişkin esas sorumluluk yönetime ve üst yönetimden sorumlu olanlara aittir.",
     "Denetçi, tabloların bir bütün olarak hile kaynaklı önemli yanlışlık içermediğine dair makul güvence elde eder.",
     "Yapısal kısıtlamalar nedeniyle bazı önemli yanlışlıkların tespit edilememe riski kaçınılmaz olarak vardır.",
     "Üst yönetimin gözetimi, yönetimin kontrolleri ihlal etme ihtimalinin dikkate alınmasını kapsar."],
    "BDS 240 prg. 4'e göre esas sorumluluk yönetim ve üst yönetimdedir; prg. 5'e göre denetçi, tabloların bir bütün olarak "
    "önemli yanlışlık içermediğine dair makul güvence elde etmekle sorumludur ve yapısal kısıtlamalar nedeniyle bazı önemli "
    "yanlışlıkların tespit edilememe riski kaçınılmazdır.")

P.q("BDS 240 prg. 13, A9",
    f"{H}, belgelerin gerçekliğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, her belgenin gerçekliğini bir uzmana doğrulatmakla ve bunu belgelendirmekle yükümlüdür.",
    ["Aksini gerektiren bir gerekçe yoksa denetçi kayıt ve belgeleri gerçek kabul edebilir.",
     "Bir belgenin tahrif edilmiş olabileceğine dair bulgu varsa denetçi araştırmasını derinleştirir.",
     "Denetim, belgelerin gerçekliğini tespit etmeye yönelik uzmanlık gerektiren bir çalışma değildir.",
     "Şüphe hâlinde denetçi üçüncü taraftan teyit almayı veya bir uzman kullanmayı değerlendirebilir."],
    "BDS 240 prg. 13'e göre denetçi, aksini gerektiren gerekçe yoksa belgeleri gerçek kabul edebilir; bir belgenin gerçek "
    "olmayabileceğine dair bulgu varsa araştırmasını derinleştirir. A9'a göre denetim belgelerin gerçekliğinin tespitini "
    "içermez ve denetçi bu konuda uzman değildir; şüphe hâlinde teyit veya uzman kullanımı değerlendirilebilir.")

P.q("BDS 240 A3",
    f"{H}, aşağıdakilerden hangisi hileli finansal raporlamaya örnek değildir?",
    "Bir çalışanın kasadaki parayı alıp kaydı değiştirmeden işten ayrılması",
    ["Yıl sonu satışlarını artırmak için sevk edilmemiş malların satış olarak kaydedilmesi",
     "Karşılıkların kâr hedefine ulaşmak için bilerek düşük hesaplanması",
     "Önemli bir koşullu yükümlülüğün dipnotlarda kasten açıklanmaması",
     "Muhasebe politikalarının tutar ve sunumu etkileyecek şekilde kasıtlı yanlış uygulanması"],
    "BDS 240 A3'e göre hileli finansal raporlama; kayıtların manipülasyonu, olay ve işlemlerin kasten yanlış sunulması "
    "veya açıklanmaması ve muhasebe ilkelerinin kasten yanlış uygulanmasıyla gerçekleşir. Kasadan para alınması ise "
    "varlıkların kötüye kullanılmasıdır (A5).")

P.q("BDS 240 A4",
    f"{H}, yönetimin kontrolleri ihlal ederek hile yapma yöntemleri arasında aşağıdakilerden hangisi yer almaz?",
    "Denetçiye tabloları hazırlama sorumluluğunu kabul ettiğine dair yazılı açıklama vermek",
    ["Özellikle dönem sonuna yakın hayali yevmiye kayıtları yapmak",
     "Bakiyeleri tahmin etmekte kullanılan varsayımları uygunsuz biçimde değiştirmek",
     "Dönem içinde gerçekleşen olay ve işlemleri kaydetmemek veya kayıt zamanını değiştirmek",
     "Önemli ve olağan dışı işlemlerin şartlarını değiştirmek veya gizlemek"],
    "BDS 240 A4'e göre yönetimin kontrolleri ihlali; hayali yevmiye kayıtları, tahmin varsayımlarının uygunsuz "
    "değiştirilmesi, olayların kaydedilmemesi veya kayıt zamanının değiştirilmesi, işlem şartlarının gizlenmesi gibi "
    "yöntemlerle yapılır. Yazılı açıklama vermek bir hile yöntemi değil, BDS 580 kapsamında bir yükümlülüktür.")

P.q("BDS 240 prg. 30, A37",
    f"{H}, yönetim beyanı düzeyinde değerlendirilmiş hile kaynaklı risklere karşı prosedürlerin değiştirilmesine ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hile riski yüksekse maddi doğrulamanın dönem sonu yerine ara dönemde uygulanması genellikle daha etkilidir.",
    ["Daha güvenilir ve ihtiyaca uygun kanıt elde etmek için prosedürlerin niteliği değiştirilebilir.",
     "Hile riski yüksekse maddi doğrulama prosedürleri dönem sonuna yakın uygulanabilir.",
     "Örneklem büyüklüğünün artırılması veya daha ayrıntılı analitik prosedürler kapsamı genişletebilir.",
     "Habersiz stok sayımları veya beklenmeyen lokasyonlarda sayım yapılması öngörülemezlik sağlar."],
    "BDS 240 prg. 30 ve A37-A40'a göre hile riskine karşı prosedürlerin niteliği, zamanlaması ve kapsamı değiştirilir; "
    "kasıtlı yanlışlık riski yüksekken ara dönem prosedürleri yerine dönem sonuna yakın prosedürler daha etkilidir. "
    "Örneklem büyüklüğü ve habersiz sayımlar kapsam ve öngörülemezlik sağlar.", zorluk="hard")

P.q("BDS 240 Ek 1",
    f"{H}, aşağıdakilerden hangisi hileli finansal raporlamaya yönelik teşvik veya baskı oluşturan hile riski "
    "faktörlerine örnek değildir?",
    "İşletmede etkin bir iç denetim fonksiyonu ve güçlü bir etik kültür bulunması",
    ["Yönetimin primlerinin büyük ölçüde agresif kâr hedeflerine bağlı olması",
     "Kredi sözleşmelerindeki şartları sağlama konusunda ciddi finansal baskı bulunması",
     "Sektördeki hızlı değişim nedeniyle kârlılığın tehdit altında olması",
     "Analist beklentilerini karşılama yönünde yönetim üzerinde yoğun baskı bulunması"],
    "BDS 240 Ek 1'e göre finansal istikrar veya kârlılığı tehdit eden durumlar, analist ve kredi verenlerin beklentilerini "
    "karşılama baskısı ve yönetimin kişisel finansal durumunun işletme sonuçlarına bağlanması teşvik veya baskı "
    "faktörleridir. Etkin iç denetim ve güçlü etik kültür hile riskini azaltan unsurlardır.")

P.q("BDS 240 prg. 41",
    f"{H}, yönetimin dahil olduğu bir hile şüphesinin iletilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetimin dahil olduğu hile şüphesi, yönetimin yazılı onayı alınmadan üst yönetime bildirilemez.",
    ["Üst yönetimin tamamı yönetimde görev almıyorsa yönetimin dahil olduğu hileler onlara zamanında bildirilir.",
     "İç kontrolde önemli görevi olan çalışanların dahil olduğu hileler de üst yönetime bildirilir.",
     "Denetçi, yönetimin dahil olduğu hile şüphesinde tamamlanacak prosedürleri üst yönetimle görüşür.",
     "Tablolarda önemli etki oluşturabilecek konumdaki diğer kişilerin hileleri de üst yönetime bildirilir."],
    "BDS 240 prg. 41'e göre yönetimin, iç kontrolde önemli görevi olan çalışanların veya tablolarda önemli etki "
    "yaratabilecek diğer kişilerin dahil olduğu hileler üst yönetimden sorumlu olanlara zamanında bildirilir; yönetimin "
    "dahil olduğu şüphede denetimin tamamlanması için gerekli prosedürler de onlarla görüşülür. Yönetimin onayı aranmaz.")

P.q("BDS 250 prg. 3-5",
    f"{M}, mevzuata uygunluğa ilişkin sorumluluklarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, işletmenin mevzuata aykırılıklarını önlemekten ve bunları tek tek tespit etmekten sorumludur.",
    ["İşletmenin faaliyetlerinin mevzuata uygun yürütülmesini sağlamak yönetimin sorumluluğundadır.",
     "Denetçi, tabloların bir bütün olarak aykırılıklardan kaynaklananlar dahil önemli yanlışlık içermediğine dair makul güvence elde eder.",
     "Yapısal kısıtlamalar nedeniyle, denetim BDS'lere uygun yürütülse de bazı önemli yanlışlıklar tespit edilemeyebilir.",
     "Mevzuata aykırılığın tablolara etkisi, aykırılığın niteliğine göre büyük farklılık gösterir."],
    "BDS 250 prg. 3'e göre faaliyetlerin mevzuata uygun yürütülmesini sağlamak üst yönetimin gözetiminde yönetimin "
    "sorumluluğudur. Prg. 4-5'e göre denetçi aykırılıkları önlemekten sorumlu değildir; tabloların önemli yanlışlık "
    "içermediğine dair makul güvence elde eder ve yapısal kısıtlamalar nedeniyle tespit edilemeyen yanlışlık olabilir.")

P.q("BDS 250 prg. 16-17",
    f"{M}, mevzuata ilişkin yazılı açıklamalar ve diğer prosedürler bakımından aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, mevzuata aykırılıklarla ilgili yönetimden yazılı açıklama talep etmez.",
    ["Denetçi, bilinen tüm aykırılıkların kendisine açıklandığına dair yazılı açıklama talep eder.",
     "Yazılı açıklama, tabloları hazırlarken etkileri dikkate alınması gereken aykırılıkları kapsar.",
     "Denetim sırasında uygulanan diğer prosedürler de denetçinin dikkatini aykırılıklara çekebilir.",
     "Denetçi, diğer prosedürleri uygularken aykırılık olabilecek durumlara karşı dikkatli olur."],
    "BDS 250 prg. 16'ya göre diğer prosedürler denetçinin dikkatini aykırılıklara çekebilir ve denetçi bu konuda dikkatli "
    "olur. Prg. 17'ye göre denetçi, tabloları hazırlarken etkileri dikkate alınması gereken bilinen veya şüphelenilen tüm "
    "aykırılıkların kendisine açıklandığına dair yönetimden yazılı açıklama talep eder.")

P.q("BDS 250 prg. 20-21",
    f"{M}, aykırılık şüphesi hâlinde denetçinin yapacağı işlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetim uygunluğa dair yeterli bilgi vermese de denetçi yönetimin sözlü beyanını yeterli kabul eder.",
    ["Denetçi, mevzuat yasaklamadıkça konuyu yönetimle ve uygun hâllerde üst yönetimle görüşür.",
     "Yönetim yeterli bilgi sağlamazsa denetçi hukuki danışmanlık almayı değerlendirebilir.",
     "Yeterli bilgi elde edilemezse denetçi bunun görüşü üzerindeki etkisini değerlendirir.",
     "Denetçi, aykırılığın tablolar üzerindeki muhtemel etkisini değerlendirmek için daha fazla bilgi elde eder."],
    "BDS 250 prg. 20'ye göre aykırılık şüphesinde denetçi konuyu yönetim ve uygun hâllerde üst yönetimle görüşür; yönetim "
    "uygunluğa dair yeterli bilgi sağlamazsa ve etkisi önemli olabilecekse hukuki danışmanlık almayı değerlendirir. Prg. "
    "21'e göre yeterli bilgi elde edilemezse bunun görüşe etkisi değerlendirilir.", zorluk="hard")

P.q("BDS 240 prg. 20-21",
    f"{H}, üst yönetimden sorumlu olanlara ilişkin prosedürlerle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üst yönetimden sorumlu olanlar, yönetim sorgulandığı için ayrıca sorgulanmaz ve gözetim süreci anlaşılmaz.",
    ["Denetçi, üst yönetimin hile risklerini belirleme ve karşılık verme sürecini nasıl gözettiğini anlar.",
     "Üst yönetimin tamamı yönetimde değilse denetçi onları gerçekleşmiş veya şüphelenilen hileler hakkında sorgular.",
     "Üst yönetimden alınan cevaplar yönetimin cevaplarını doğrulamaya da yardımcı olabilir.",
     "Üst yönetimin gözetim faaliyetleri, kontrollerin ihlal edilme ihtimalinin dikkate alınmasını kapsar."],
    "BDS 240 prg. 20'ye göre denetçi, üst yönetimin hile risklerini belirleme ve karşılık verme sürecini nasıl gözettiğini "
    "anlar; prg. 21'e göre üst yönetimin tamamı yönetimde değilse onları da gerçekleşmiş, şüphelenilen veya iddia edilen "
    "hileler hakkında sorgular. Bu sorgulama yönetimin cevaplarını doğrulamaya da yardımcı olur (A20).")

P.q("BDS 240 prg. 37",
    f"{H}, tabloların hile kaynaklı önemli yanlışlık içerdiğinin doğrulanması veya bu konuda sonuca ulaşılamaması "
    "hâline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi bu durumda denetime etkisini değerlendirmez; sadece yönetime bir mektup yazar.",
    ["Denetçi, durumun denetime olan etkilerini değerlendirir.",
     "Durum, BDS 705 uyarınca görüşün değiştirilmesini gerektirebilir.",
     "Durum, istisnai hâllerde denetime devam edilip edilemeyeceğinin sorgulanmasına yol açabilir.",
     "Denetçi, yazılı açıklamaların ve diğer kanıtların güvenilirliğini yeniden değerlendirebilir."],
    "BDS 240 prg. 37'ye göre denetçi, tabloların hile kaynaklı önemli yanlışlık içerip içermediği konusunda sonuca "
    "ulaşamaz veya bunu doğrularsa denetime etkilerini değerlendirir; bu, görüşün değiştirilmesini (BDS 705) veya istisnai "
    "hâllerde prg. 38 kapsamında denetime devam imkânının sorgulanmasını gerektirebilir.")

P.q("BDS 250 prg. 30",
    f"{M}, tespit edilen veya şüphelenilen aykırılıklara ilişkin belgelendirmeyle ilgili aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Aykırılıklar sadece yönetime sözlü bildirilir; çalışma kâğıtlarına alınmaz.",
    ["Uygulanan denetim prosedürleri çalışma kâğıtlarına dahil edilir.",
     "Önemli mesleki muhakemeler ve ulaşılan sonuçlar belgelendirilir.",
     "Yönetim ve üst yönetimle yapılan görüşmeler belgelendirilir.",
     "İşletme dışındaki taraflarla yapılan görüşmeler de belgelendirilir."],
    "BDS 250 prg. 30'a göre denetçi tespit edilen veya şüphelenilen aykırılıklar ile uygulanan prosedürleri, önemli mesleki "
    "muhakemeleri ve ulaşılan sonuçları, yönetim, üst yönetim ve işletme dışındaki taraflarla yapılan görüşmeleri çalışma "
    "kâğıtlarına dahil eder.")

if __name__ == "__main__":
    sys.exit(P.yaz())
