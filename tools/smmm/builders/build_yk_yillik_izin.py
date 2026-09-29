# -*- coding: utf-8 -*-
"""Hukuk · İş Hukuku · Yıllık İzin ve Diğer İzinler — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında izin soruları süre ve gün sayısı soran kısa, kanun adıyla başlayan köklerle
gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 4857 sayılı İş Kanunu md. 53-61, 74, Ek md. 2-3.
22.04.2026 tarihli 7578 sayılı Kanunla doğum sonrası analık izni 16 haftaya (toplam 24 hafta), doğum öncesi çalışma
imkânı iki haftaya, eşin doğumu izni on güne çıkarılmış; koruyucu aileye on gün ücretsiz izin eklenmiştir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_yillik_izin_2026.json", lesson="is_hukuku", topic="yillik_izin",
          konu_adi="Yıllık İzin", seed=2026093003,
          surum="4857 sayılı İş Kanunu güncel metni (7578 s. Kanun değişikliği dahil); 29.09.2026 kontrolü")

K = "4857 sayılı İş Kanunu’na göre"
K26 = "4857 sayılı İş Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İK md. 53",
    f"{K26}, hizmet süresi bir yıldan beş yıla kadar (beş yıl dahil) olan işçiye verilecek yıllık ücretli izin en az "
    "kaç gündür?",
    "14", ["10", "12", "20", "26"],
    "Md. 53'e göre yıllık ücretli izin süresi hizmet süresi bir yıldan beş yıla kadar (beş yıl dahil) olanlara on dört günden, "
    "beş yıldan fazla on beş yıldan az olanlara yirmi günden, on beş yıl ve fazla olanlara yirmi altı günden az olamaz.",
    zorluk="easy")

P.q("İK md. 53",
    f"{K}, yıllık ücretli izne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşçi, izin hakkından yazılı olarak vazgeçebilir.",
    ["Deneme süresi hak kazanma süresine dahildir.",
     "İzin süreleri sözleşmelerle artırılabilir.",
     "Yer altı işçilerinin izni dörder gün artırılır.",
     "Hak kazanmak için en az bir yıl çalışmak gerekir."],
    "Md. 53'e göre yıllık ücretli izin hakkından vazgeçilemez; deneme süresi de dahil en az bir yıl çalışan işçiye izin verilir "
    "ve izin süreleri sözleşmelerle artırılabilir.", zorluk="easy")

P.q("İK md. 53",
    f"{K}, yıllık ücretli izin hükümleri aşağıdaki işlerin hangisinde çalışanlara uygulanmaz?",
    "Bir yıldan az süren mevsimlik işler",
    ["Yer altı maden işleri",
     "Haftada üç gün çalışılan kısmi süreli işler",
     "Belirsiz süreli büro işleri",
     "Bir yılı aşan belirli süreli işler"],
    "Md. 53'e göre niteliklerinden ötürü bir yıldan az süren mevsimlik veya kampanya işlerinde çalışanlara yıllık ücretli izin "
    "hükümleri uygulanmaz.")

P.sayisal("İK md. 53",
    "Kırk yaşındaki işçi Bay (A), aynı işyerinde sekiz yıldır yer üstünde çalışmaktadır ve sözleşmesinde daha uzun bir izin "
    f"öngörülmemiştir.\n\n{K26}, Bay (A)’ya verilecek yıllık ücretli izin en az kaç gündür?",
    "20", ["14", "18", "24", "26"],
    "Md. 53'e göre hizmet süresi beş yıldan fazla on beş yıldan az olanlara yirmi günden az yıllık izin verilemez.")

P.q("İK md. 54",
    f"{K}, yıllık izne hak kazanma süresinin hesabına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Aynı işverenin farklı işyerlerindeki süreler birleştirilmez.",
    ["Aynı işverenin kapsam dışı işyerindeki süreler de sayılır.",
     "Devamsızlık boşlukları kadar süre hizmet yılına eklenir.",
     "Yeni hizmet yılı önceki izin hakkının doğduğu günden başlar.",
     "İzin, hak kazanılan yılı izleyen hizmet yılında kullanılır."],
    "Md. 54'e göre yıllık izne hak kazanma süresinin hesabında işçinin aynı işverenin bir veya çeşitli işyerlerinde çalıştığı "
    "süreler birleştirilerek göz önüne alınır.")

P.q("İK md. 55",
    f"{K}, aşağıdakilerden hangisi yıllık ücretli izin hakkının hesabında çalışılmış gibi sayılmaz?",
    "Doğum sonrası altı aylık ücretsiz izin",
    ["Hafta tatili ve genel tatil günleri",
     "Doğum öncesi ve sonrası analık izni",
     "Ek 2. maddedeki mazeret izinleri",
     "İşveren tarafından verilen diğer izinler"],
    "Md. 55'e göre analık izni, hafta tatili ve genel tatiller, Ek 2. madde izinleri ve işverence verilen diğer izinler "
    "çalışılmış sayılır; md. 74'teki altı aya kadar ücretsiz izin ise yıllık izin hesabında dikkate alınmaz.", zorluk="hard")

P.sayisal("İK md. 53",
    "Otuz sekiz yaşındaki işçi Bay (B), on altı yıldır aynı işverenin maden ocağında yer altı işlerinde çalışmaktadır."
    f"\n\n{K26}, Bay (B)’ye verilecek yıllık ücretli izin en az kaç gündür?",
    "30", ["20", "24", "26", "34"],
    "Md. 53'e göre on beş yıl ve daha fazla hizmeti olanlara yirmi altı günden az izin verilemez; yer altı işlerinde çalışan "
    "işçilerin izin süreleri dörder gün artırılır: 26 + 4 = 30 gün.", zorluk="hard")

P.oncul("İK md. 55",
    f"{K} aşağıdaki süreler değerlendirilmektedir:",
    ["İşçinin arabuluculuk toplantısına katıldığı gün",
     "Kısa çalışma süreleri",
     "Önceki yıl kullandırılan yıllık izin süresi",
     "İşçinin mazeretsiz işe gelmediği gün"],
    "Yukarıdakilerden hangileri yıllık izin hakkının hesabında çalışılmış gibi sayılır?",
    "I, II ve III",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "I, III ve IV"],
    "Md. 55'e göre arabuluculuk toplantısına katılma (h), kısa çalışma süreleri (j) ve Kanuna göre verilmiş yıllık izin süresi "
    "(k) çalışılmış sayılır; mazeretsiz devamsızlık sayılmaz ve md. 54'e göre hizmet yılına eklenir.", zorluk="hard")

P.q("İK md. 56",
    f"{K}, yıllık ücretli iznin uygulanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hastalık izinleri yıllık izne mahsup edilebilir.",
    ["İzin işveren tarafından bölünemez.",
     "İzne rastlayan genel tatiller izin süresinden sayılmaz.",
     "İşveren izin kayıt belgesi tutar.",
     "İzin, taraflar anlaşırsa bölümler hâlinde kullanılabilir."],
    "Md. 56'ya göre işverence yıl içinde verilen diğer ücretli ve ücretsiz izinler veya dinlenme ve hastalık izinleri yıllık "
    "izne mahsup edilemez.")

P.sayisal("İK md. 53",
    "Elli iki yaşındaki işçi Bayan (C), aynı işyerinde üç yıldır yer üstünde çalışmaktadır."
    f"\n\n{K26}, Bayan (C)’ye verilecek yıllık ücretli izin en az kaç gündür?",
    "20", ["14", "16", "18", "26"],
    "Md. 53'e göre on sekiz ve daha küçük yaştaki işçilerle elli ve daha yukarı yaştaki işçilere verilecek yıllık ücretli izin "
    "süresi yirmi günden az olamaz; üç yıllık kıdeme göre hesaplanan on dört gün bu nedenle yirmi güne çıkar.", zorluk="hard")

P.q("İK md. 56",
    "Bir alt işverenin işçisi, alt işveren değiştiği hâlde aynı işyerinde çalışmaya devam etmektedir."
    f"\n\n{K}, bu işçinin yıllık ücretli izin süresi nasıl hesaplanır?",
    "Aynı işyerindeki süreler dikkate alınarak",
    ["Yeni alt işverenle başladığı tarih esas alınarak",
     "Sadece son alt işverendeki süre dikkate alınarak",
     "Asıl işverenin işçilerinin ortalaması alınarak",
     "Her alt işveren için ayrı ayrı sıfırdan"],
    "Md. 56'ya göre alt işvereni değiştiği hâlde aynı işyerinde çalışmaya devam eden alt işveren işçilerinin yıllık izin süresi, "
    "aynı işyerinde çalıştıkları süreler dikkate alınarak hesaplanır.")

P.q("İK md. 56",
    f"{K}, alt işveren işçilerinin yıllık izinlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Asıl işverenin izinlerin kullanımını denetleme yükümü yoktur.",
    ["Asıl işveren izinlerin ilgili yıl kullanılmasını sağlar.",
     "Alt işveren izin kayıt belgesinin örneğini asıl işverene verir.",
     "Alt işveren değişse de aynı işyerindeki süreler birleştirilir.",
     "Alt işveren de izin kayıt belgesi tutar."],
    "Md. 56'ya göre asıl işveren, alt işveren işçilerinin hak kazandığı yıllık izinlerin kullanılıp kullanılmadığını kontrol "
    "etmek ve ilgili yıl içinde kullanılmasını sağlamakla yükümlüdür.", zorluk="hard")

P.sayisal("İK md. 55",
    "İşçi Bay (D), muvazzaf askerlik dışında bir kanundan doğan ödev nedeniyle bir yıl içinde 120 gün işine gidememiştir."
    f"\n\n{K}, bu sürenin kaç günü yıllık ücretli izin hakkının hesabında çalışılmış gibi sayılır?",
    "90", ["30", "60", "100", "120"],
    "Md. 55/c'ye göre muvazzaf askerlik dışında manevra veya bir kanundan dolayı ödevlendirilme sırasında işe gidilemeyen "
    "günler çalışılmış sayılır; ancak yılda doksan günden fazlası sayılmaz.", zorluk="hard")

P.q("İK md. 57",
    f"{K}, yıllık izin ücretine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İzne başlamadan önce peşin veya avans ödenir.",
    ["İzin dönüşünü izleyen ilk ücret gününde ödenir.",
     "İzin bitiminden sonra bir ay içinde ödenir.",
     "Yüzde usulünde yüzdelerden toplanan paradan ödenir.",
     "İzne rastlayan hafta tatili ücreti ayrıca ödenmez."],
    "Md. 57'ye göre işveren yıllık izin ücretini işçinin izne başlamasından önce peşin ödemek veya avans olarak vermek "
    "zorundadır; izne rastlayan hafta tatili ve genel tatil ücretleri ayrıca ödenir.", zorluk="easy")

P.q("İK md. 57",
    f"{K}, akort veya komisyon gibi belirli olmayan tutar üzerinden ücret alan işçinin izin ücreti nasıl hesaplanır?",
    "Son bir yılın ücreti fiilen çalışılan günlere bölünerek",
    ["Sözleşmedeki taban tutar esas alınarak",
     "Son ayın ücreti otuza bölünerek",
     "İşe giriş tarihindeki ücret esas alınarak",
     "Emsal işçinin ücreti esas alınarak"],
    "Md. 57'ye göre belirli olmayan süre ve tutar üzerinden ücret alan işçinin izin ücreti, son bir yılda kazandığı ücretin "
    "fiilen çalıştığı günlere bölünmesiyle bulunacak ortalama üzerinden hesaplanır.")

P.sayisal("İK md. 55",
    "Bir işyerinde zorlayıcı sebeplerle iş aralıksız üç hafta tatil edilmiş, işçi daha sonra yeniden işe başlamıştır."
    f"\n\n{K}, işçinin çalışmadan geçirdiği bu sürenin en çok kaç günü yıllık izin hesabında çalışılmış gibi sayılır?",
    "15", ["7", "10", "21", "30"],
    "Md. 55/d'ye göre zorlayıcı sebeplerle işin aralıksız bir haftadan çok tatil edilmesi sonucu çalışmadan geçen zamanın, "
    "işçinin yeniden işe başlaması şartıyla on beş günü çalışılmış gibi sayılır.")

P.q("İK md. 57",
    f"{K}, yüzde usulünün uygulandığı yerlerde yıllık izin ücretine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yüzdeler dışında işverence ödenir.",
    ["Yüzdelerden toplanan paradan ödenir.",
     "Müşterilerden ayrıca tahsil edilir.",
     "İşçi sendikası tarafından ödenir.",
     "Yüzde usulündeki işçiye izin ücreti ödenmez."],
    "Md. 57'ye göre yüzde usulünün uygulandığı yerlerde yıllık izin ücreti, yüzdelerden toplanan para dışında işveren "
    "tarafından ödenir.")

P.q("İK md. 58",
    "Yıllık ücretli iznini kullanan işçi Bay (K)’nın izin süresi içinde başka bir işyerinde ücret karşılığı çalıştığı "
    f"anlaşılmıştır.\n\n{K}, işveren bu durumda ne yapabilir?",
    "İzin süresi için ödediği ücreti geri alabilir.",
    ["Sözleşmeyi derhal ve tazminatsız fesheder.",
     "İzni bir sonraki yıla aktarabilir.",
     "İşçiye ücret kesme cezası uygular.",
     "İzin süresini ikiye katlayarak mahsup edebilir."],
    "Md. 58'e göre yıllık ücretli izni içinde ücret karşılığı bir işte çalıştığı anlaşılan işçiye bu süre için ödenen ücret "
    "işveren tarafından geri alınabilir.")

P.sayisal("İK md. 56",
    "İşçi ile işveren, yirmi günlük yıllık ücretli iznin bölümler hâlinde kullanılması konusunda anlaşmıştır."
    f"\n\n{K26}, bölümlerden biri en az kaç gün olmalıdır?",
    "10", ["3", "5", "7", "14"],
    "Md. 56'ya göre yıllık izin süreleri tarafların anlaşmasıyla bir bölümü on günden aşağı olmamak üzere bölümler hâlinde "
    "kullanılabilir.")

P.q("İK md. 59",
    f"{K}, iş sözleşmesinin sona ermesinde kullanılmayan yıllık izin ücretine ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Ücret, hakkın doğduğu tarihteki ücretle ödenir.",
    ["Sözleşme hangi nedenle sona ererse ersin ödenir.",
     "İşçinin ölümünde hak sahiplerine ödenir.",
     "Zamanaşımı sözleşmenin sona erdiği tarihte başlar.",
     "Bildirim süresi yıllık izinle iç içe giremez."],
    "Md. 59'a göre kullanılmayan yıllık izin ücreti sözleşmenin sona erdiği tarihteki ücret üzerinden ödenir; zamanaşımı "
    "sözleşmenin sona erdiği tarihten başlar.")

P.q("İK md. 59",
    "İşveren, işçinin iş sözleşmesini bildirimli olarak feshetmiş ve bildirim süresini işçinin yıllık izniyle aynı döneme "
    f"denk getirmiştir.\n\n{K}, bu uygulama hakkında aşağıdakilerden hangisi doğrudur?",
    "Bildirim süresi ile yıllık izin iç içe giremez.",
    ["İşveren bildirim süresini izinle birleştirebilir.",
     "İşçinin onayı varsa iç içe kullanılabilir.",
     "Yeni iş arama izni yıllık izinden düşülür.",
     "Yıllık izin bildirim süresinin yarısını karşılar."],
    "Md. 59'a göre işveren tarafından feshedilmesi hâlinde md. 17'deki bildirim süresi ve md. 27'deki yeni iş arama izinleri "
    "yıllık ücretli izin süreleri ile iç içe giremez.", zorluk="hard")

P.sayisal("İK md. 56",
    "İşçi, yıllık iznini işyerinin bulunduğu şehirden başka bir yerde geçireceğini belgeleyerek yol izni istemiştir."
    f"\n\n{K}, işveren gidiş ve dönüş için toplam en çok kaç gün ücretsiz izin vermek zorundadır?",
    "4", ["2", "3", "5", "7"],
    "Md. 56'ya göre yıllık iznini başka yerde geçirecek işçiye istemde bulunması ve belgelemesi koşuluyla, yolda geçecek "
    "süreler için işveren toplam dört güne kadar ücretsiz izin vermek zorundadır.", zorluk="easy")

P.q("İK md. 60",
    f"{K}, yıllık izinlerin hangi dönemlerde ve ne suretle kullanılacağına ilişkin usuller nerede gösterilir?",
    "Bakanlıkça hazırlanan yönetmelikte",
    ["İşyeri iç yönergesinde", "Cumhurbaşkanı kararında", "Valilik genelgesinde", "Sendika tüzüğünde"],
    "Md. 60'a göre yıllık izinlerin kullanılacağı dönemler, verilme şekli ve tutulacak kayıtlar Çalışma ve Sosyal Güvenlik "
    "Bakanlığınca hazırlanacak yönetmelikle gösterilir.", zorluk="easy")

P.q("İK md. 61",
    f"{K}, yıllık izin süresi için ödenen ücretler üzerinden aşağıdaki sigorta primlerinden hangisinin ödenmesine devam "
    "olunmaz?",
    "İş kazası ve meslek hastalığı primi",
    ["Malullük, yaşlılık ve ölüm primi", "Genel sağlık sigortası primi", "İşsizlik sigortası primi",
     "Uzun vadeli sigorta primi"],
    "Md. 61'e göre yıllık izin ücretleri üzerinden iş kazaları ile meslek hastalıkları primleri hariç diğer sigorta "
    "primlerinin ödenmesine devam olunur.", zorluk="hard")

P.sayisal("İK md. 74",
    f"{K26}, tekil gebelikte kadın işçinin doğumdan önce ve sonra çalıştırılmaması esas olan toplam süre kaç haftadır?",
    "24", ["16", "18", "20", "26"],
    "Md. 74'e göre (7578 sayılı Kanunla 2026'da değişik) kadın işçilerin doğumdan önce sekiz ve doğumdan sonra on altı hafta "
    "olmak üzere toplam yirmi dört haftalık süre için çalıştırılmamaları esastır.", zorluk="hard")

P.q("İK md. 74",
    f"{K26}, analık hâlinde çalışmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Doğumda anne ölürse kalan süre kullandırılmaz.",
    ["Erken doğumda kullanılmayan süre doğum sonrasına eklenir.",
     "Hamile işçiye periyodik kontroller için ücretli izin verilir.",
     "Hafif işe geçirilen hamile işçinin ücretinden indirim yapılmaz.",
     "Süreler hekim raporuyla gerekirse artırılabilir."],
    "Md. 74'e göre doğumda veya doğum sonrasında annenin ölümü hâlinde doğum sonrası kullanılamayan süreler babaya "
    "kullandırılır.")

P.q("İK md. 74",
    f"{K}, süt iznine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kullanım saatlerini işveren belirler.",
    ["Bir yaşından küçük çocuğu emziren kadın işçiye verilir.",
     "Günde toplam bir buçuk saattir.",
     "Günlük çalışma süresinden sayılır.",
     "Yarım çalışma izni sırasında uygulanmaz."],
    "Md. 74'e göre süt izninin hangi saatler arasında ve kaça bölünerek kullanılacağını işçi kendisi belirler; bu süre günlük "
    "çalışma süresinden sayılır.")

P.sayisal("İK md. 74",
    "İkiz bebek bekleyen kadın işçi Bayan (E)’nin doğum öncesi analık izni planlanmaktadır."
    f"\n\n{K26}, Bayan (E)’nin doğumdan önce çalıştırılmayacağı süre kaç haftadır?",
    "10", ["6", "8", "12", "16"],
    "Md. 74'e göre çoğul gebelik hâlinde doğumdan önce çalıştırılmayacak sekiz haftalık süreye iki hafta eklenir: 8 + 2 = 10 "
    "hafta.")

P.q("İK md. 74",
    f"{K}, analık hâlinde çalışma ve süt iznine ilişkin hükümlerin uygulama alanı hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Kanun kapsamı dışındaki işçilere de uygulanır.",
    ["Sadece Kanun kapsamındaki işçilere uygulanır.",
     "Sadece kamu işyerlerinde uygulanır.",
     "Sadece belirsiz süreli işçilere uygulanır.",
     "Sadece elli işçiden fazla işyerlerinde uygulanır."],
    "Md. 74'ün son fıkrasına göre bu madde hükümleri iş sözleşmesiyle çalışan ve Kanunun kapsamında olan veya olmayan her "
    "türlü işçi için uygulanır.", zorluk="hard")

P.q("İK Ek md. 2",
    f"{K}, aşağıdaki yakınlarından hangisinin ölümü hâlinde işçiye üç gün ücretli izin verilmez?",
    "Amcası",
    ["Annesi", "Kardeşi", "Eşi", "Çocuğu"],
    "Ek md. 2'ye göre ana veya babasının, eşinin, kardeşinin veya çocuğunun ölümü hâlinde işçiye üç gün ücretli izin verilir; "
    "amca bu yakınlar arasında sayılmamıştır.", zorluk="easy")

P.sayisal("İK md. 74",
    f"{K26}, sağlık durumu uygun olan kadın işçi doktorun onayıyla doğumdan önceki kaç haftaya kadar işyerinde "
    "çalışabilir?",
    "2", ["1", "3", "4", "6"],
    "Md. 74'e göre (7578 sayılı Kanunla 2026'da üç haftadan iki haftaya indirildi) sağlık durumu uygunsa doktor onayıyla kadın "
    "işçi doğumdan önceki iki haftaya kadar çalışabilir; çalıştığı süreler doğum sonrasına eklenir.", zorluk="hard")

P.q("İK Ek md. 2",
    f"{K26}, mazeret izinlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tedavi izni iki ebeveyne ayrı ayrı verilir.",
    ["Evlenen işçiye üç gün ücretli izin verilir.",
     "Evlat edinen işçiye üç gün ücretli izin verilir.",
     "Eşi doğum yapan işçiye on gün ücretli izin verilir.",
     "Tedavi izni toptan veya bölümler hâlinde kullanılabilir."],
    "Ek md. 2'ye göre engelli veya süreğen hastalığı olan çocuğun tedavisi için verilen izin, çalışan ebeveynlerden sadece biri "
    "tarafından kullanılabilir.", zorluk="hard")

P.q("İK md. 53",
    "İşçi Bay (L) on yedi yaşındadır ve aynı işyerinde bir buçuk yıldır çalışmaktadır."
    f"\n\n{K26}, Bay (L)’ye verilecek yıllık izin hakkında aşağıdakilerden hangisi doğrudur?",
    "Yirmi günden az olamaz.",
    ["On dört günden az olamaz.",
     "Yer altında çalışmıyorsa on gündür.",
     "Bir yılı doldurduğu için on sekiz gündür.",
     "On sekiz yaşına kadar izne hak kazanamaz."],
    "Md. 53'e göre on sekiz ve daha küçük yaştaki işçilerle elli ve daha yukarı yaştaki işçilere verilecek yıllık ücretli izin "
    "yirmi günden az olamaz.")

P.sayisal("İK md. 74",
    "Kadın işçi Bayan (F), doğum sonrası analık izninin bitiminden itibaren ikinci çocuğunun bakımı için haftalık çalışma "
    f"süresinin yarısı kadar ücretsiz izin istemektedir.\n\n{K}, bu izin kaç gün süreyle verilir?",
    "120", ["60", "90", "180", "360"],
    "Md. 74'e göre bu izin birinci doğumda altmış, ikinci doğumda yüz yirmi, sonraki doğumlarda yüz seksen gün süreyle verilir; "
    "çoğul doğumda otuzar gün eklenir, çocuk engelli doğarsa üç yüz altmış gündür.", zorluk="hard")

P.q("İK md. 55",
    f"{K}, işçinin tutulduğu hastalık nedeniyle işine gidemediği günlerin yıllık izin hesabında sayılmasına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Md. 25/I-b’deki süreyi aşan kısım sayılmaz.",
    ["Hastalık günleri kural olarak sayılmaz.",
     "Sadece ilk otuz günü sayılır.",
     "Hepsi, süre sınırı olmaksızın sayılır.",
     "Rapor süresinin yarısı sayılır."],
    "Md. 55/a'ya göre kaza veya hastalık nedeniyle işe gidilemeyen günler çalışılmış gibi sayılır; ancak md. 25/I-b'de "
    "öngörülen süreden fazlası sayılmaz.", zorluk="hard")

P.sayisal("İK md. 74",
    f"{K}, bir yaşından küçük çocuğunu emziren kadın işçiye günde toplam kaç dakika süt izni verilir?",
    "90", ["30", "45", "60", "120"],
    "Md. 74'e göre kadın işçilere bir yaşından küçük çocuklarını emzirmeleri için günde toplam bir buçuk saat süt izni verilir; "
    "bu süre günlük çalışma süresinden sayılır.")

P.q("İK md. 56",
    "İşçinin on dört günlük yıllık izni bir ulusal bayrama ve iki hafta tatiline denk gelmektedir."
    f"\n\n{K}, bu günler yıllık izin süresinin hesabında nasıl değerlendirilir?",
    "İzin süresinden sayılmaz.",
    ["İzin süresinden düşülür.",
     "Yarısı izin süresinden sayılır.",
     "Sadece bayram günü izinden sayılır.",
     "İşverenin tercihine göre sayılır."],
    "Md. 56'ya göre yıllık ücretli izin günlerinin hesabında izin süresine rastlayan ulusal bayram, hafta tatili ve genel "
    "tatil günleri izin süresinden sayılmaz.", zorluk="easy")

P.sayisal("İK md. 74",
    f"{K26}, isteği hâlinde kadın işçiye analık izni süresinin tamamlanmasından sonra en çok kaç ay ücretsiz izin "
    "verilir?",
    "6", ["2", "3", "4", "12"],
    "Md. 74'e göre isteği hâlinde kadın işçiye yirmi dört haftalık sürenin (çoğul gebelikte yirmi altı haftanın) "
    "tamamlanmasından sonra altı aya kadar ücretsiz izin verilir.")

P.q("İK md. 54",
    f"{K}, aynı bakanlığa bağlı işyerlerinde geçen sürelerin yıllık izin hakkının hesabındaki yerine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Bu süreler hesapta göz önünde bulundurulur.",
    ["Bu süreler hesaba katılmaz.",
     "Sadece son işyerindeki süre dikkate alınır.",
     "Süreler yarı oranında dikkate alınır.",
     "Süreler işçinin talebi olmadıkça hesaba katılmaz."],
    "Md. 54'e göre aynı bakanlığa bağlı işyerlerinde, kamu iktisadi teşebbüslerinde ve bunlara bağlı işyerlerinde geçen "
    "süreler yıllık izin hakkının hesabında göz önünde bulundurulur.")

P.sayisal("İK md. 74",
    "İşçi Bay (G) ve eşi, iki yaşındaki bir çocuğu evlat edinmiş; çocuk aileye fiilen teslim edilmiştir."
    f"\n\n{K}, eşlerden birine kaç hafta analık hâli izni kullandırılır?",
    "8", ["2", "4", "6", "16"],
    "Md. 74'e göre üç yaşını doldurmamış çocuğu evlat edinen eşlerden birine veya evlat edinene, çocuğun aileye fiilen teslim "
    "edildiği tarihten itibaren sekiz hafta analık hâli izni kullandırılır.")

P.q("İK md. 74",
    f"{K}, analık izni sonrası verilen altı aya kadar ücretsiz izne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu süre yıllık izin hesabında çalışılmış sayılır.",
    ["İzin kadın işçinin isteği hâlinde verilir.",
     "Evlat edinmede eşlerden birine verilebilir.",
     "Çoğul gebelikte yirmi altı haftadan sonra başlar.",
     "İzin, çocuğu evlat edinene de verilebilir."],
    "Md. 74'e göre analık izni sonrası altı aya kadar verilen ücretsiz izin süresi yıllık ücretli izin hakkının hesabında "
    "dikkate alınmaz.")

P.sayisal("İK md. 74",
    "İşçi Bayan (H), eşiyle birlikte bir çocuğa koruyucu aile olmuş ve çocuk kendilerine teslim edilmiştir."
    f"\n\n{K26}, Bayan (H)’ye isteği üzerine kaç gün ücretsiz izin verilir?",
    "10", ["3", "5", "7", "15"],
    "Md. 74'e 7578 sayılı Kanunla 2026'da eklenen hükme göre bir veya daha fazla çocuğa koruyucu aile olan işçiye, çocuğun "
    "teslim edildiği tarihten sonra isteği üzerine on gün ücretsiz izin verilir.", zorluk="hard")

P.q("İK md. 74",
    f"{K}, doğum sonrası yarım çalışma ödeneğine esas ücretsiz izinden yararlanabilecek kişiler arasında aşağıdakilerden "
    "hangisi yer almaz?",
    "Beş yaşındaki çocuğu evlat edinen işçi",
    ["Doğum yapan kadın işçi",
     "İki yaşındaki çocuğu evlat edinen kadın işçi",
     "Bir yaşındaki çocuğu evlat edinen erkek işçi",
     "Çoğul doğum yapan kadın işçi"],
    "Md. 74'e göre yarım çalışma şeklindeki ücretsiz izin doğum yapan kadın işçi ile üç yaşını doldurmamış çocuğu evlat edinen "
    "kadın veya erkek işçilere verilir.", zorluk="hard")

P.sayisal("İK Ek md. 2",
    f"{K26}, eşi doğum yapan işçiye kaç gün ücretli izin verilir?",
    "10", ["3", "5", "7", "14"],
    "Ek md. 2'ye göre (7578 sayılı Kanunla 2026'da beş günden on güne çıkarıldı) eşinin doğum yapması hâlinde işçiye on gün "
    "ücretli izin verilir.", zorluk="hard")

P.q("İK md. 53",
    f"{K}, yer altı işlerinde çalışan işçilerin yıllık ücretli izin sürelerine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Süreler dörder gün artırılarak uygulanır.",
    ["Süreler ikişer gün artırılarak uygulanır.",
     "Süreler iki katı olarak uygulanır.",
     "Yer üstü işçileriyle aynı süreler uygulanır.",
     "Süreler yarım gün artırılarak uygulanır."],
    "Md. 53'e göre yer altı işlerinde çalışan işçilerin yıllık ücretli izin süreleri dörder gün artırılarak uygulanır.",
    zorluk="easy")

P.sayisal("İK Ek md. 2",
    f"{K}, evlenen işçiye kaç gün ücretli izin verilir?",
    "3", ["1", "2", "5", "7"],
    "Ek md. 2'ye göre işçiye evlenmesi veya evlat edinmesi ya da ana, baba, eş, kardeş veya çocuğunun ölümü hâlinde üç gün "
    "ücretli izin verilir.", zorluk="easy")

P.q("İK md. 56",
    f"{K}, yıllık ücretli iznin işveren tarafından verilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İzin kesintisiz verilir.",
    ["İşveren izni dilediği gibi bölebilir.",
     "İzin ancak iki yılda bir verilebilir.",
     "İzin sadece yaz aylarında kullanılabilir.",
     "İzin günlük saatler hâlinde verilir."],
    "Md. 56'ya göre yıllık ücretli izin işveren tarafından bölünemez ve md. 53'teki süreler içinde sürekli bir şekilde "
    "verilmesi zorunludur.", zorluk="easy")

P.sayisal("İK Ek md. 2",
    "İşçi Bay (I)’nın yüzde yetmiş oranında engelli çocuğu vardır; eşi de çalışmaktadır ve izni yalnızca Bay (I) "
    f"kullanacaktır.\n\n{K}, bu çocuğun tedavisi için bir yıl içinde en çok kaç gün ücretli izin verilir?",
    "10", ["3", "5", "7", "15"],
    "Ek md. 2'ye göre işçilerin en az yüzde yetmiş engelli veya süreğen hastalığı olan çocuğunun tedavisinde, rapora dayalı ve "
    "ebeveynlerden sadece biri kullanmak kaydıyla bir yıl içinde on güne kadar ücretli izin verilir.")

P.q("İK md. 53",
    f"{K26}, yıllık ücretli izin sürelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Elli yaşındaki işçiye en az on dört gün verilir.",
    ["Beş yıla kadar kıdemde en az on dört gündür.",
     "On beş yıl kıdemde en az yirmi altı gündür.",
     "Süreler iş sözleşmesiyle artırılabilir.",
     "Yer altı işçisine dörder gün fazla verilir."],
    "Md. 53'e göre elli ve daha yukarı yaştaki işçilere verilecek yıllık ücretli izin süresi yirmi günden az olamaz.")

P.sayisal("İK Ek md. 3",
    f"{K}, iş sözleşmesinden kaynaklanan yıllık izin ücretinin zamanaşımı süresi kaç yıldır?",
    "5", ["1", "2", "3", "10"],
    "Ek md. 3'e göre iş sözleşmesinden kaynaklanan yıllık izin ücreti ile kıdem, ihbar, kötüniyet ve eşit davranmaya aykırı "
    "fesih tazminatlarının zamanaşımı süresi beş yıldır.")

P.q("İK md. 57",
    f"{K}, yıllık izin ücretine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İzne rastlayan genel tatil ücreti ayrıca ödenmez.",
    ["Ücret izinden önce peşin ödenebilir.",
     "Ücret avans olarak da verilebilir.",
     "Hesabında md. 50 hükmü uygulanır.",
     "Yüzde usulünde ücreti işveren öder."],
    "Md. 57'ye göre yıllık ücretli izin süresine rastlayan hafta tatili, ulusal bayram ve genel tatil ücretleri ayrıca "
    "ödenir.")

iu = 1_500 * 28
P.sayisal("İK md. 59",
    "İşçi Bay (J)’nin iş sözleşmesi feshedilmiştir. Bay (J), hak kazandığı hâlde kullanmadığı toplam 28 günlük yıllık izne "
    "sahiptir. Fesih tarihindeki günlük ücreti 1.500 ₺, izin hakkının doğduğu tarihteki günlük ücreti 1.100 ₺’dir."
    f"\n\n{K}, Bay (J)’ye ödenecek yıllık izin ücreti kaç ₺’dir?",
    tl(iu), secenekler(iu, 30_800, 21_000, 15_400, 36_400),
    "Md. 59'a göre sözleşmenin sona ermesinde hak kazanılıp kullanılmayan yıllık izin sürelerinin ücreti sözleşmenin sona "
    "erdiği tarihteki ücret üzerinden ödenir: 28 × 1.500 = 42.000 ₺.", zorluk="hard")

P.q("İK md. 74",
    f"{K26}, hamile kadın işçinin çalıştırılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Doktor onayıyla çalışılan süre doğum sonrasına eklenmez.",
    ["Hekim raporuyla daha hafif işlerde çalıştırılabilir.",
     "Hafif işe geçirilince ücretinde indirim yapılmaz.",
     "Çoğul gebelikte doğum öncesi süreye iki hafta eklenir.",
     "Periyodik kontroller için ücretli izin verilir."],
    "Md. 74'e göre doktor onayıyla doğumdan önceki iki haftaya kadar çalışan kadın işçinin çalıştığı süreler doğum sonrası "
    "sürelere eklenir.")

P.sayisal("İK md. 74",
    "Kadın işçi Bayan (M), ilk doğumunda ikiz bebek dünyaya getirmiş ve analık izninin bitiminden itibaren yarım çalışma "
    f"şeklindeki ücretsiz izni istemiştir.\n\n{K}, bu izin kaç gün süreyle verilir?",
    "90", ["60", "120", "150", "180"],
    "Md. 74'e göre bu izin birinci doğumda altmış gündür; çoğul doğum hâlinde otuz gün eklenir: 60 + 30 = 90 gün.",
    zorluk="hard")

P.q("İK md. 55",
    f"{K}, aşağıdakilerden hangisi yıllık izin hakkının hesabında çalışılmış gibi sayılır?",
    "Röntgen çalışanlarına verilen yarım günlük izinler",
    ["Mazeretsiz devamsızlık günleri",
     "Tutukluluk nedeniyle işe gelinmeyen günler",
     "Muvazzaf askerlikte geçen süre",
     "Analık izni sonrası altı aylık ücretsiz izin"],
    "Md. 55/g'ye göre röntgen muayenehanelerinde çalışanlara pazardan başka verilmesi gereken yarım günlük izinler çalışılmış "
    "gibi sayılır; muvazzaf askerlik md. 55/c'de açıkça dışarıda bırakılmıştır.", zorluk="hard")

P.sayisal("İK md. 74",
    f"{K}, çocuğun engelli doğması hâlinde haftalık çalışma süresinin yarısı kadar verilen ücretsiz izin kaç gün "
    "süreyle uygulanır?",
    "360", ["120", "180", "240", "720"],
    "Md. 74'e göre çocuğun engelli doğması hâlinde yarım çalışma şeklindeki ücretsiz izin üç yüz altmış gün olarak "
    "uygulanır.")

P.q("İK md. 54",
    "İşçi Bay (O), bir yıllık hizmet süresi içinde md. 55’te sayılmayan sebeplerle yirmi gün işe devam etmemiştir."
    f"\n\n{K}, izin hakkı için gereken bir yıllık sürenin bitiş tarihi nasıl belirlenir?",
    "Devamsızlık süresi kadar ileri kayar.",
    ["Değişmez; izin hakkı aynen doğar.",
     "Bir yıl ertelenir.",
     "Devamsızlığın yarısı kadar ileri kayar.",
     "İzin hakkı o yıl için düşer."],
    "Md. 54'e göre bir yıllık süre içinde md. 55 dışındaki sebeplerle devamın kesilmesi hâlinde bu boşlukları karşılayacak "
    "kadar hizmet süresi eklenir ve bir yıllık sürenin bitiş tarihi ileriye aktarılır.")

P.sayisal("İK md. 53",
    "Otuz beş yaşındaki işçi Bay (N), aynı işyerinde tam on beş yıldır yer üstünde çalışmaktadır."
    f"\n\n{K26}, Bay (N)’ye verilecek yıllık ücretli izin en az kaç gündür?",
    "26", ["20", "22", "24", "30"],
    "Md. 53'e göre on beş yıl (dahil) ve daha fazla hizmeti olan işçilere yirmi altı günden az yıllık izin verilemez.")

P.q("İK md. 74",
    "Kadın işçi doğum sırasında hayatını kaybetmiş, doğum sonrası analık izninin kullanılamayan kısmı kalmıştır."
    f"\n\n{K}, bu süre kime kullandırılır?",
    "Babaya",
    ["Anneanneye", "Kullandırılmaz", "Vasiye", "İşverenin belirleyeceği yakına"],
    "Md. 74'ün 2016'da eklenen hükmüyle, annenin doğumda veya doğumdan sonra ölmesi durumunda kullanılamayan doğum sonrası "
    "analık izni babanın kullanımına geçer.", zorluk="easy")

P.sayisal("İK md. 53",
    f"{K}, işçinin yıllık ücretli izne hak kazanması için işe başladığı günden itibaren, deneme süresi de dahil olmak "
    "üzere en az kaç yıl çalışmış olması gerekir?",
    "1", ["2", "3", "4", "5"],
    "Md. 53'e göre işyerinde işe başladığı günden itibaren deneme süresi de içinde olmak üzere en az bir yıl çalışmış olan "
    "işçilere yıllık ücretli izin verilir.", zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
