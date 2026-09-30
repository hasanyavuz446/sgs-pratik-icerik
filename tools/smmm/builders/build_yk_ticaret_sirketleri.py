# -*- coding: utf-8 -*-
"""Hukuk · Ticaret Hukuku · Ticaret Şirketleri — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında şirketler hukuku soruları "6102 sayılı Türk Ticaret Kanunu’na göre yukarıdakilerden
hangileri sermaye şirketidir?" gibi öncüllü ve kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6102 sayılı TTK md. 124-137, 181, 211-243, 304-307, 329-445,
519, 529, 573-639. Cumhurbaşkanı kararıyla güncellenen asgari sermaye tutarları soru konusu yapılmamıştır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_ticaret_sirketleri_2026.json", lesson="ticaret_hukuku", topic="ticaret_sirketleri",
          konu_adi="Ticaret Şirketleri", seed=2026093013, surum="6102 sayılı TTK güncel metni; 29.09.2026 kontrolü")

K = "6102 sayılı Türk Ticaret Kanunu’na göre"

P.sayisal("TTK md. 362",
    f"{K}, anonim şirket yönetim kurulu üyeleri en çok kaç yıl süreyle görev yapmak üzere seçilir?",
    "3", ["1", "2", "4", "5"],
    "Md. 362'ye göre yönetim kurulu üyeleri en çok üç yıl süreyle görev yapmak üzere seçilir; esas sözleşmede aksine hüküm "
    "yoksa yeniden seçilebilir.", zorluk="easy")

P.q("TTK md. 124",
    f"{K}, aşağıdakilerden hangisi ticaret şirketlerinden biri değildir?",
    "Adi şirket",
    ["Kollektif şirket", "Komandit şirket", "Limited şirket", "Kooperatif şirket"],
    "Md. 124/1'e göre ticaret şirketleri kollektif, komandit, anonim, limited ve kooperatif şirketlerden ibarettir; adi şirket "
    "TBK'da düzenlenen bir ortaklıktır.", zorluk="easy")

P.oncul("TTK md. 124",
    f"{K} aşağıdaki şirketler değerlendirilmektedir:",
    ["Kollektif şirket", "Limited şirket", "Sermayesi paylara bölünmüş komandit şirket", "Adi komandit şirket"],
    "Yukarıdakilerden hangileri sermaye şirketidir?",
    "II ve III",
    ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "II, III ve IV"],
    "Md. 124/2'ye göre anonim, limited ve sermayesi paylara bölünmüş komandit şirketler sermaye şirketi; kollektif ve komandit "
    "şirketler şahıs şirketidir.", zorluk="easy")

P.sayisal("TTK md. 409",
    f"{K}, anonim şirket olağan genel kurul toplantısı her faaliyet dönemi sonundan itibaren kaç ay içinde yapılır?",
    "3", ["1", "2", "4", "6"],
    "Md. 409/1'e göre olağan genel kurul toplantısı her faaliyet dönemi sonundan itibaren üç ay içinde yapılır.", zorluk="easy")

P.q("TTK md. 125",
    f"{K}, ticaret şirketlerinin hukuki niteliğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tüzel kişiliğe sahiptir.",
    ["Tüzel kişiliği yoktur.",
     "Sadece sermaye şirketleri tüzel kişidir.",
     "Sadece tescilden bir yıl sonra tüzel kişi olur.",
     "Tüzel kişiliği ortakların oybirliğine bağlıdır."],
    "Md. 125'e göre ticaret şirketleri tüzel kişiliği haizdir ve TMK md. 48 çerçevesinde bütün haklardan yararlanabilir.",
    zorluk="easy")

P.q("TTK md. 126",
    f"{K}, ticaret şirketlerine ilişkin bu Kısımda hüküm bulunmayan hususlarda niteliğine uygun olduğu oranda hangi "
    "hükümler uygulanır?",
    "TBK’nın adi şirket hükümleri",
    ["Kooperatifler Kanunu", "TBK’nın kira hükümleri", "Tüketici Kanunu", "İcra ve İflas Kanunu"],
    "Md. 126'ya göre TMK'nın tüzel kişilere ilişkin genel hükümleri ile bu Kısımda hüküm bulunmayan hususlarda TBK'nın adi "
    "şirkete dair hükümleri ticaret şirketlerine de uygulanır.")

P.sayisal("TTK md. 414",
    f"{K}, anonim şirket genel kurulu, ilan ve toplantı günleri hariç, toplantı tarihinden en az kaç hafta önce çağrılır?",
    "2", ["1", "3", "4", "6"],
    "Md. 414/1'e göre çağrı ilan ve toplantı günleri hariç olmak üzere toplantı tarihinden en az iki hafta önce yapılır.")

P.q("TTK md. 127",
    f"{K}, aşağıdakilerden hangisi kural olarak ticaret şirketlerine sermaye olarak konulamaz?",
    "Devredilemeyen kişisel bir hak",
    ["Fikrî mülkiyet hakları",
     "Kişisel emek",
     "Ticari itibar",
     "Maden ruhsatnameleri"],
    "Md. 127'ye göre para, alacak, fikrî haklar, taşınır ve taşınmazlar, kişisel emek, ticari itibar, işletmeler, maden "
    "ruhsatları ile devrolunabilen ve nakden değerlendirilebilen her türlü değer sermaye olarak konabilir.")

P.q("TTK md. 128",
    f"{K}, sermaye olarak taşınmaz mülkiyetinin konulmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Şirket sözleşmesindeki taahhüt resmî şekle tabidir.",
    ["Şirketin tasarrufu için tapuya tescil gerekir.",
     "Tescil istemini sicil müdürü resen yapar.",
     "Taşınmaz tapuya şerh verilirse ayni sermaye sayılır.",
     "Şirketin tek taraflı istem hakkı saklıdır."],
    "Md. 128/3'e göre sermaye olarak taşınmaz konulması borcunu içeren şirket sözleşmesi hükümleri resmî şekil aranmaksızın "
    "geçerlidir.", zorluk="hard")

P.sayisal("TTK md. 411",
    "Halka açık olmayan bir anonim şirkette pay sahipleri, genel kurulun toplantıya çağrılmasını istemek için azlık hakkını "
    f"kullanacaktır.\n\n{K}, bu pay sahipleri esas sermayenin en az yüzde kaçına sahip olmalıdır?",
    "10", ["5", "20", "25", "50"],
    "Md. 411/1'e göre sermayenin en az onda birini, halka açık şirketlerde yirmide birini oluşturan pay sahipleri genel kurulun "
    "toplantıya çağrılmasını isteyebilir; esas sözleşmeyle bu oran düşürülebilir.")

P.q("TTK md. 130",
    "Bir ortak, vadesi gelmiş bir alacağını sermaye olarak şirkete devretmiştir; alacak henüz tahsil edilmemiştir."
    f"\n\n{K}, ortağın sermaye koyma borcu hakkında aşağıdakilerden hangisi doğrudur?",
    "Tahsil edilmedikçe borç sürer.",
    ["Devirle birlikte borç sona erer.",
     "Borç tescille sona erer.",
     "Tahsil riski şirkete aittir.",
     "Borç yarı oranında sona erer."],
    "Md. 130/1'e göre sermaye olarak alacaklarını devreden ortak, alacaklar şirketçe tahsil edilmedikçe sermaye koyma borcundan "
    "kurtulmaz.")

P.q("TTK md. 131",
    f"{K}, sermaye olarak konulan ayınlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ayınların mülkiyeti kural olarak ortakta kalır.",
    ["Bilirkişi değerleri ilgililerce kabul edilmiş sayılır.",
     "Aksi kararlaştırılmamışsa haklar şirkete geçer.",
     "Kâra katılımla ücret çalışana ortaklık vermez.",
     "Şirket sözleşmesiyle aksi kararlaştırılabilir."],
    "Md. 131/2'ye göre şirket sözleşmesinde aksi kararlaştırılmamışsa sermaye olarak konan ayınların mülkiyeti şirkete ait ve "
    "haklar şirkete devredilmiş olur.")

P.sayisal("TTK md. 411",
    f"{K}, azlığın çağrı istemini kabul eden yönetim kurulu genel kurulu en geç kaç gün içinde yapılacak şekilde "
    "toplantıya çağırır?",
    "45", ["15", "30", "60", "90"],
    "Md. 411/4'e göre yönetim kurulu çağrıyı kabul ederse genel kurul en geç kırk beş gün içinde yapılacak şekilde toplantıya "
    "çağrılır; aksi hâlde çağrıyı istem sahipleri yapar.", zorluk="hard")

P.q("TTK md. 133",
    f"{K}, bir şahıs şirketi devam ettiği sürece ortağın kişisel alacaklısı alacağını nereden alabilir?",
    "Ortağın kâr payından",
    ["Şirketin tüm malvarlığından",
     "Diğer ortakların mallarından",
     "Şirket kasasından doğrudan",
     "Şirketin taşınmazlarının satışından"],
    "Md. 133/1'e göre şahıs şirketi devam ettiği sürece ortağın kişisel alacaklısı hakkını bilanço gereğince o ortağa düşen kâr "
    "payından, şirket fesholunmuşsa tasfiye payından alabilir.")

P.q("TTK md. 136",
    f"{K}, birleşmeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birleşmede devrolunan şirket varlığını sürdürür.",
    ["Devralma veya yeni kuruluş şeklinde olabilir.",
     "Devralan, malvarlığını bir bütün olarak devralır.",
     "Birleşme sözleşmesi ayrılma akçesi öngörebilir.",
     "Ortaklar devralanın paylarını doğrudan edinir."],
    "Md. 136/4'e göre birleşmeyle devrolunan şirket sona erer ve ticaret sicilinden silinir.")

P.sayisal("TTK md. 445",
    f"{K}, kanuna, esas sözleşmeye veya dürüstlük kuralına aykırı genel kurul kararlarına karşı karar tarihinden itibaren "
    "kaç ay içinde iptal davası açılabilir?",
    "3", ["1", "2", "6", "12"],
    "Md. 445'e göre iptal davası karar tarihinden itibaren üç ay içinde şirket merkezinin bulunduğu yerdeki asliye ticaret "
    "mahkemesinde açılır.")

P.q("TTK md. 137",
    f"{K}, şahıs şirketlerinin sermaye şirketleriyle birleşmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sadece devrolunan olarak birleşebilir.",
    ["Sadece devralan şirket olarak birleşebilir.",
     "Sermaye şirketleriyle birleşemez.",
     "Her iki sıfatla da birleşebilir.",
     "Sadece kooperatif aracılığıyla birleşebilir."],
    "Md. 137/2'ye göre şahıs şirketleri sermaye şirketleri ve kooperatiflerle ancak devrolunan şirket olmaları şartıyla "
    "birleşebilir.", zorluk="hard")

P.q("TTK md. 181",
    f"{K}, aşağıdaki tür değiştirmelerden hangisi mümkün değildir?",
    "Kooperatifin kollektif şirkete dönüşmesi",
    ["Anonim şirketin limited şirkete dönüşmesi",
     "Kollektif şirketin komandit şirkete dönüşmesi",
     "Komandit şirketin anonim şirkete dönüşmesi",
     "Kooperatifin sermaye şirketine dönüşmesi"],
    "Md. 181'e göre kooperatif sadece bir sermaye şirketine dönüşebilir; kollektif veya komandit şirkete dönüşemez.",
    zorluk="hard")

P.sayisal("TTK md. 418",
    f"{K}, Kanunda veya esas sözleşmede daha ağır nisap öngörülmemişse anonim şirket genel kurulu sermayenin en az yüzde "
    "kaçını karşılayan payların sahiplerinin varlığıyla toplanır?",
    "25", ["10", "20", "33", "50"],
    "Md. 418/1'e göre genel kurullar sermayenin en az dörtte birini karşılayan pay sahiplerinin varlığıyla toplanır; ilk "
    "toplantıda nisap sağlanamazsa ikinci toplantıda nisap aranmaz.")

P.q("TTK md. 211",
    f"{K}, kollektif şirketin ortaklarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sadece gerçek kişiler ortak olabilir.",
    ["Tüzel kişiler de ortak olabilir.",
     "Ortakların sorumluluğu sınırlıdır.",
     "Tek ortakla kurulabilir.",
     "Ortaklardan biri sınırlı sorumlu olmalıdır."],
    "Md. 211'e göre kollektif şirket gerçek kişiler arasında kurulan ve ortaklarından hiçbirinin sorumluluğu şirket "
    "alacaklılarına karşı sınırlanmamış olan şirkettir.")

P.q("TTK md. 212",
    f"{K}, kollektif şirket sözleşmesinin şekline ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yazılıdır; imzalar noterce onaylanır.",
    ["Sözlü olarak yapılabilir.",
     "Resmî senetle ve tapuda yapılır.",
     "Adi yazılı şekil yeterlidir, onay gerekmez.",
     "Mahkeme huzurunda yapılır."],
    "Md. 212'ye göre kollektif şirket sözleşmesi yazılı şekle tabidir; imzaların noterce onaylanması veya sözleşmenin sicil "
    "müdürü ya da yardımcısı huzurunda imzalanması şarttır.")

P.sayisal("TTK md. 519",
    f"{K}, anonim şirkette yıllık kârın yüzde kaçı ödenmiş sermayenin yüzde yirmisine ulaşıncaya kadar genel kanuni yedek "
    "akçeye ayrılır?",
    "5", ["2", "10", "15", "20"],
    "Md. 519/1'e göre yıllık kârın yüzde beşi, ödenmiş sermayenin yüzde yirmisine ulaşıncaya kadar genel kanuni yedek akçeye "
    "ayrılır.")

P.q("TTK md. 216",
    f"{K}, tescil yükümlülüğü yerine getirilmeden kollektif şirket adına işlere başlanması hâlinde ortakların sorumluluğu "
    "nasıldır?",
    "Müteselsil sorumluluk",
    ["Sorumluluk doğmaz.", "Sadece yönetici sorumludur.", "Sermaye payı oranında sorumluluk", "Sadece şirket sorumludur."],
    "Md. 216'ya göre tescil yükümlülüğü yerine getirilmeksizin şirket adına işlere başlanmışsa ortaklar giriştikleri işlerden "
    "dolayı üçüncü kişilere karşı müteselsilen sorumludur.")

P.q("TTK md. 223",
    f"{K}, kollektif şirkette aşağıdaki işlemlerden hangisi için ortakların oybirliği gerekmez?",
    "Olağan ticari satış yapılması",
    ["Bağışta bulunulması",
     "Kefil olunması",
     "Ticari mümessil atanması",
     "Konu dışı taşınmaz satılması"],
    "Md. 223'e göre yönetim olağan işlerle sınırlıdır; bağış, kefalet, üçüncü kişi lehine garanti, ticari mümessil tayini ve "
    "konu dışı taşınmaz işlemleri gibi olağan dışı işlerde oybirliği şarttır.")

ya = 2_000_000 * 0.05
P.sayisal("TTK md. 519",
    "Ödenmiş sermayesi 10.000.000 ₺ olan bir anonim şirketin genel kanuni yedek akçesi 500.000 ₺’dir. Şirketin yıllık kârı "
    f"2.000.000 ₺’dir.\n\n{K}, bu yıl kârdan ayrılması gereken genel kanuni yedek akçe kaç ₺’dir?",
    "100.000", ["50.000", "200.000", "400.000", "20.000"],
    "Md. 519/1'e göre kârın %5'i, ödenmiş sermayenin %20'sine (2.000.000 ₺) ulaşıncaya kadar ayrılır: 2.000.000 × %5 = "
    "100.000 ₺; bu tutar sınırı aşmamaktadır.", zorluk="hard")

P.q("TTK md. 230",
    f"{K}, kollektif şirket ortağının rekabet yasağına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İzinsiz aynı tür iş yapamaz.",
    ["Rekabet yasağı yoktur.",
     "Sadece yönetici ortak için yasak vardır.",
     "Yasak şirketin tescilinden önce geçerlidir.",
     "Aynı tür işle uğraşan şirkete sınırsız sorumlu ortak olabilir."],
    "Md. 230'a göre ortak, şirketin yaptığı ticari işler türünden bir işi diğer ortakların izni olmaksızın yapamaz ve aynı tür "
    "işle uğraşan bir şirkete sorumluluğu sınırsız ortak olarak giremez.")

P.q("TTK md. 236",
    f"{K}, kollektif şirkete yeni giren ortağın, girişinden önce doğmuş şirket borçlarından sorumluluğu nasıldır?",
    "Diğer ortaklarla birlikte müteselsilen sorumludur.",
    ["Sorumlu değildir.",
     "Sadece sermayesi oranında sorumludur.",
     "Sadece girişten sonraki borçlardan sorumludur.",
     "Sorumluluğu sözleşmeyle üçüncü kişilere karşı kaldırılabilir."],
    "Md. 236/2'ye göre şirkete yeni giren kişi, giriş tarihinden önce doğmuş borçlardan da diğer ortaklarla birlikte "
    "müteselsilen ve bütün malvarlığı ile sorumludur.")

P.sayisal("TTK md. 344",
    f"{K}, anonim şirkette nakden taahhüt edilen payların itibari değerlerinin geri kalanı şirketin tescilini izleyen kaç "
    "ay içinde ödenir?",
    "24", ["6", "12", "18", "36"],
    "Md. 344/1'e göre nakden taahhüt edilen payların itibari değerlerinin en az yüzde yirmi beşi tescilden önce, gerisi "
    "tescili izleyen yirmi dört ay içinde ödenir.", zorluk="hard")

P.q("TTK md. 237",
    f"{K}, kollektif şirketin borçlarından sorumluluğun derecesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Birinci derecede şirket sorumludur.",
    ["Birinci derecede ortaklar sorumludur.",
     "Şirket ve ortaklar aynı anda takip edilir.",
     "Ortaklar takip edilemez.",
     "Önce yönetici ortak takip edilir."],
    "Md. 237/1'e göre şirketin borçlarından birinci derecede şirket sorumludur; şirkete karşı takip semeresiz kalır veya şirket "
    "sona ererse ortak aleyhine dava ve takip yapılabilir.")

P.q("TTK md. 243",
    f"{K}, aşağıdakilerden hangisi kollektif şirketin sona erme sebeplerinden biri değildir?",
    "Bir ortağın evlenmesi",
    ["Şirketin iflası",
     "Sermayenin üçte ikisinin kaybı ve önlem alınmaması",
     "Başka bir şirketle birleşme",
     "Bir ortağın iflası"],
    "Md. 243'e göre kollektif şirket iflas, sermayenin tamamının veya üçte ikisinin kaybı ve önlem alınmaması, birleşme, tescil "
    "yapılmaması hâlinde mahkeme kararı ve bir ortağın iflası gibi sebeplerle sona erer.", zorluk="easy")

P.sayisal("TTK md. 344",
    f"{K}, anonim şirkette nakden taahhüt edilen payların itibari değerlerinin en az yüzde kaçı tescilden önce ödenir?",
    "25", ["10", "20", "50", "100"],
    "Md. 344/1'e göre nakden taahhüt edilen payların itibari değerlerinin en az yüzde yirmi beşi tescilden önce ödenir; bu şart "
    "limited şirketlere uygulanmaz.")

P.q("TTK md. 304",
    f"{K}, komandit şirkete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tüzel kişiler komandite ortak olabilir.",
    ["Komandite ortakların sorumluluğu sınırsızdır.",
     "Komanditer ortakların sorumluluğu sınırlıdır.",
     "Komandite ortaklar gerçek kişi olmalıdır.",
     "Tüzel kişiler komanditer ortak olabilir."],
    "Md. 304/3'e göre komandite ortakların gerçek kişi olmaları gerekir; tüzel kişiler ancak komanditer ortak olabilir.")

P.q("TTK md. 306",
    f"{K}, komandit olduğu açıkça saptanamayan bir şirket hangi tür sayılır?",
    "Kollektif şirket",
    ["Limited şirket", "Anonim şirket", "Adi şirket", "Kooperatif şirket"],
    "Md. 306/2'ye göre bir şirketin komandit olduğu açıkça saptanamıyorsa o şirket kollektif sayılır.", zorluk="hard")

P.sayisal("TTK md. 574",
    f"{K}, limited şirkette ortakların sayısı en çok kaç olabilir?",
    "50", ["20", "30", "75", "100"],
    "Md. 574/1'e göre limited şirkette ortakların sayısı elliyi aşamaz.", zorluk="easy")

P.q("TTK md. 307",
    f"{K}, komanditer ortağın sermaye olarak koyamayacağı değer aşağıdakilerden hangisidir?",
    "Kişisel emek",
    ["Para", "Taşınmaz", "Alacak", "Fikrî mülkiyet hakkı"],
    "Md. 307/2'ye göre bir komanditer kişisel emeğini ve ticari itibarını sermaye olarak koyamaz.")

P.q("TTK md. 329",
    f"{K}, anonim şirkete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Pay sahipleri alacaklılara karşı sorumludur.",
    ["Sermayesi belirli ve paylara bölünmüştür.",
     "Borçlarından sadece malvarlığıyla sorumludur.",
     "Pay sahipleri taahhüt ettikleri payla sorumludur.",
     "Pay sahipleri sadece şirkete karşı sorumludur."],
    "Md. 329'a göre anonim şirket borçlarından dolayı sadece malvarlığıyla sorumludur; pay sahipleri sadece taahhüt ettikleri "
    "sermaye payları ile ve şirkete karşı sorumludur.")

P.sayisal("TTK md. 617",
    f"{K}, limited şirket genel kurulu, şirket sözleşmesinde farklı bir süre öngörülmemişse toplantı gününden en az kaç "
    "gün önce toplantıya çağrılır?",
    "15", ["7", "10", "21", "30"],
    "Md. 617/2'ye göre limited şirket genel kurulu toplantı gününden en az on beş gün önce çağrılır; şirket sözleşmesi bu süreyi "
    "uzatabilir veya on güne kadar kısaltabilir.")

P.q("TTK md. 333",
    f"{K}, anonim şirketin kuruluşunda Bakanlık izni hangi şirketler için aranır?",
    "Tebliğle belirlenen alanlardaki şirketler",
    ["Tüm anonim şirketler",
     "Sermayesi belirli tutarı aşanlar",
     "Tek pay sahipli şirketler",
     "Yabancı ortaklı olanlar"],
    "Md. 333'e göre Bakanlıkça yayımlanacak tebliğle faaliyet alanları belirlenen anonim şirketler Bakanlık izniyle kurulur; "
    "bunun dışında kuruluş herhangi bir makamın iznine bağlanamaz.")

P.q("TTK md. 338",
    f"{K}, anonim şirketin kurucularına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tek pay sahibiyle kurulabilir.",
    ["En az beş kurucu gerekir.",
     "En az üç kurucu gerekir.",
     "En az iki kurucu gerekir.",
     "Kurucuların tamamı tüzel kişi olmalıdır."],
    "Md. 338/1'e göre anonim şirketin kurulabilmesi için pay sahibi olan bir veya daha fazla kurucunun varlığı şarttır.",
    zorluk="easy")

P.sayisal("TTK md. 583",
    f"{K}, limited şirket esas sermaye paylarının itibari değeri en az kaç Türk lirası olarak belirlenebilir?",
    "25", ["1", "10", "50", "100"],
    "Md. 583/1'e göre esas sermaye paylarının itibari değerleri en az yirmi beş Türk lirası olarak belirlenebilir ve yirmi beş "
    "liranın katları olmalıdır.")

P.q("TTK md. 359",
    f"{K}, anonim şirket yönetim kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tüzel kişi yönetim kuruluna seçilemez.",
    ["Yönetim kurulu bir kişiden oluşabilir.",
     "Üyeler tam ehliyetli olmalıdır.",
     "Tüzel kişi adına bir gerçek kişi tescil edilir.",
     "Esas sözleşmeyle üye atanabilir."],
    "Md. 359/2'ye göre bir tüzel kişi yönetim kuruluna üye seçilebilir; bu durumda tüzel kişi adına belirlenen bir gerçek kişi "
    "de tescil ve ilan olunur.")

P.q("TTK md. 376",
    "Son yıllık bilançoya göre bir anonim şirketin sermaye ile kanuni yedek akçeler toplamının yarısı zarar sebebiyle "
    f"karşılıksız kalmıştır.\n\n{K}, yönetim kurulu ne yapmalıdır?",
    "Genel kurulu hemen toplamalıdır.",
    ["Şirketin iflasını istemelidir.",
     "Bir işlem yapmamalıdır.",
     "Şirketi doğrudan tasfiye etmelidir.",
     "Sermayeyi tek başına azaltmalıdır."],
    "Md. 376/1'e göre sermaye ile kanuni yedek akçeler toplamının yarısı karşılıksız kalırsa yönetim kurulu genel kurulu hemen "
    "toplantıya çağırır ve iyileştirici önlemleri sunar.")

P.sayisal("TTK md. 574",
    "Bir limited şirketin ortak sayısı, pay devri sonucunda bire düşmüştür."
    f"\n\n{K}, durum bu sonucu doğuran işlem tarihinden itibaren kaç gün içinde müdürlere yazıyla bildirilir?",
    "7", ["3", "10", "15", "30"],
    "Md. 574/2'ye göre ortak sayısı bire düşerse durum işlem tarihinden itibaren yedi gün içinde müdürlere bildirilir; müdürler "
    "de yedinci günün sonuna kadar tescil ve ilan ettirir.")

P.q("TTK md. 376",
    f"{K}, sermaye ile kanuni yedek akçeler toplamının üçte ikisinin karşılıksız kalması hâlinde genel kurul sermayenin "
    "tamamlanmasına veya üçte biriyle yetinmeye karar vermezse ne olur?",
    "Şirket kanunen sona erer.",
    ["Şirket limited şirkete dönüşür.",
     "Yönetim kurulu görevden alınır.",
     "Şirket faaliyetine olduğu gibi devam eder.",
     "Pay sahipleri ek ödemeyle yükümlü olur."],
    "Md. 376/2'ye göre üçte iki kaybında genel kurul sermayenin üçte biriyle yetinme veya tamamlanmasına karar vermezse şirket "
    "kendiliğinden sona erer.", zorluk="hard")

P.q("TTK md. 409",
    f"{K}, anonim şirket olağan genel kurul toplantısında müzakere edilip karara bağlanan konular arasında aşağıdakilerden "
    "hangisi yer almaz?",
    "Personelin günlük izin çizelgesi",
    ["Organların seçimi",
     "Finansal tablolar",
     "Kârın kullanım şekli",
     "Yönetim kurulu üyelerinin ibrası"],
    "Md. 409/1'e göre olağan toplantıda organların seçimi, finansal tablolar, yıllık rapor, kârın kullanımı ve yönetim kurulunun "
    "ibrası gibi konular görüşülür.", zorluk="easy")

P.sayisal("TTK md. 639",
    f"{K}, limited şirkette bir ortağın çıkma istemi diğer ortaklara bildirildiğinde, diğer ortaklar haberin ulaştığı "
    "tarihten itibaren kaç ay içinde çıkmaya katılabilir?",
    "1", ["2", "3", "6", "12"],
    "Md. 639/2'ye göre diğer ortakların her biri haberin kendisine ulaştığı tarihten itibaren bir ay içinde çıkmaya katılma "
    "hakkına sahiptir.", zorluk="hard")

P.q("TTK md. 410",
    f"{K}, yönetim kurulunun devamlı olarak toplanamaması hâlinde genel kurulun toplantıya çağrılmasına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Mahkeme izniyle tek pay sahibi çağırır.",
    ["Genel kurul bu durumda toplanamaz.",
     "Sadece Bakanlık çağırabilir.",
     "Sadece denetçi çağırabilir.",
     "Mahkemenin izin kararına itiraz edilebilir."],
    "Md. 410/2'ye göre yönetim kurulunun devamlı toplanamaması veya nisabın oluşmaması hâllerinde mahkemenin izniyle tek bir "
    "pay sahibi genel kurulu çağırabilir; mahkeme kararı kesindir.", zorluk="hard")

P.q("TTK md. 519",
    f"{K}, genel kanuni yedek akçenin kullanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak zarar kapatmada kullanılır.",
    ["Doğrudan kâr payı olarak dağıtılabilir.",
     "Sadece yönetim kurulu ücretlerine ayrılır.",
     "Bir amaçla kullanılamaz.",
     "Sadece bağış yapmak için kullanılır."],
    "Md. 519/3'e göre genel kanuni yedek akçe sermayenin yarısını aşmadıkça sadece zararların kapatılması, işletmeyi devam "
    "ettirme veya işsizliği önleme önlemleri için kullanılabilir.", zorluk="hard")

P.q("TTK md. 529",
    f"{K}, aşağıdakilerden hangisi anonim şirketin sona erme sebeplerinden biri değildir?",
    "Yönetim kurulu başkanının değişmesi",
    ["Esas sözleşmedeki sürenin sona ermesi",
     "İşletme konusunun gerçekleşmesi",
     "Genel kurulun fesih kararı",
     "Şirketin iflası"],
    "Md. 529'a göre anonim şirket esas sözleşmedeki sürenin sona ermesi, işletme konusunun gerçekleşmesi veya imkânsızlaşması, "
    "genel kurul kararı ve iflas gibi sebeplerle sona erer.", zorluk="easy")

P.q("TTK md. 573",
    f"{K}, limited şirket ortaklarının sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Taahhüt ettikleri esas sermaye paylarını öderler.",
    ["Şirket borçlarından sınırsız sorumludurlar.",
     "Şirket borçlarından müteselsilen sorumludurlar.",
     "Ek ödeme yükümlülüğü kanundan doğar.",
     "Borçlardan sermaye payının iki katı kadar sorumludurlar."],
    "Md. 573/2'ye göre ortaklar şirket borçlarından sorumlu değildir; sadece taahhüt ettikleri esas sermaye paylarını ödemek ve "
    "şirket sözleşmesindeki ek ödeme ve yan edim yükümlülüklerini yerine getirmekle yükümlüdür.")

P.q("TTK md. 575",
    f"{K}, limited şirket sözleşmesinin imzalanmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sicil müdürlüğü personeli huzurunda imzalanabilir.",
    ["Sözlü olarak yapılabilir.",
     "Noterde düzenleme şeklinde yapılır.",
     "Adi yazılı şekil yeterlidir.",
     "Mahkeme huzurunda imzalanır."],
    "Md. 575'e göre şirket sözleşmesinin yazılı şekilde yapılması ve kurucular tarafından ticaret sicili müdürlüğünde "
    "yetkilendirilmiş personelin huzurunda imzalanması şarttır.")

P.q("TTK md. 576",
    f"{K}, limited şirket sözleşmesinde yer alması zorunlu kayıtlar arasında aşağıdakilerden hangisi bulunmaz?",
    "Ortakların meslekleri",
    ["Ticaret unvanı ve merkez",
     "İşletme konusu",
     "Esas sermayenin itibari tutarı",
     "Müdürlerin adları ve soyadları"],
    "Md. 576'ya göre şirket sözleşmesinde ticaret unvanı ve merkez, işletme konusu, esas sermaye ve paylar, müdürlerin kimlik "
    "bilgileri ve ilanların şekli yer alır.")

P.q("TTK md. 585",
    f"{K}, limited şirkette nakden taahhüt edilen payların bir kısmının tescilden önce ödenmesi şartına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Bu şart limited şirketlere uygulanmaz.",
    ["Tamamı tescilden önce ödenmelidir.",
     "Yarısı tescilden önce ödenmelidir.",
     "Dörtte biri tescilden önce ödenmelidir.",
     "Onda biri tescilden önce ödenmelidir."],
    "Md. 585'e göre (7099 sayılı Kanunla 2018'de eklenen cümle) nakden taahhüt edilen payların en az yüzde yirmi beşinin "
    "tescilden önce ödenmesi şartı limited şirketler bakımından uygulanmaz.", zorluk="hard")

P.q("TTK md. 595",
    f"{K}, limited şirkette esas sermaye payının devrine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Devir adi yazılı şekilde yapılabilir.",
    ["Tarafların imzaları noterce onanır.",
     "Kural olarak genel kurul onayı gerekir.",
     "Genel kurul sebep göstermeden reddedebilir.",
     "Şirket sözleşmesiyle devir yasaklanabilir."],
    "Md. 595/1'e göre esas sermaye payının devri ve devir borcunu doğuran işlemler yazılı yapılır ve tarafların imzaları noterce "
    "onanır.")

P.q("TTK md. 616",
    f"{K}, aşağıdakilerden hangisi limited şirket genel kurulunun devredilemez yetkilerinden biri değildir?",
    "Günlük satış fiyatlarının belirlenmesi",
    ["Şirket sözleşmesinin değiştirilmesi",
     "Müdürlerin atanması",
     "Esas sermaye payı devirlerinin onayı",
     "Şirketin feshi"],
    "Md. 616'ya göre sözleşme değişikliği, müdürlerin atanması ve görevden alınması, pay devirlerinin onayı ve şirketin feshi "
    "gibi konular genel kurulun devredilemez yetkileridir.")

P.q("TTK md. 623",
    f"{K}, limited şirketin yönetimine ilişkin aşağıdakilerden hangisi doğrudur?",
    "En az bir ortak yetkili olmalıdır.",
    ["Yönetim sadece üçüncü kişilere verilebilir.",
     "Tüzel kişi müdür olamaz.",
     "Müdürlerin tamamı ortak olmayan kişiler olmalıdır.",
     "Yönetim ve temsil sadece genel kurula aittir."],
    "Md. 623/1'e göre yönetim ve temsil şirket sözleşmesiyle ortaklara veya üçüncü kişilere verilebilir; ancak en az bir ortağın "
    "yönetim hakkı ve temsil yetkisi bulunmalıdır.")

P.q("TTK md. 630",
    f"{K}, limited şirkette müdürün yönetim hakkının kaldırılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Haklı sebeple mahkemeye başvurulabilir.",
    ["Sadece müdürün rızasıyla kaldırılabilir.",
     "Genel kurul müdürü görevden alamaz.",
     "Görevden alınan müdürün tazminat hakkı düşer.",
     "Sadece Bakanlık görevden alabilir."],
    "Md. 630'a göre genel kurul müdürleri görevden alabilir; her ortak haklı sebeplerin varlığında yönetim ve temsil yetkisinin "
    "kaldırılmasını mahkemeden isteyebilir; görevden alınanın tazminat hakları saklıdır.")

P.q("TTK md. 638",
    f"{K}, limited şirket ortağının şirketten çıkmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Haklı sebeple çıkma davası açabilir.",
    ["Ortak kural olarak şirketten çıkamaz.",
     "Çıkma sadece genel kurul kararıyla olur.",
     "Çıkma hakkı sözleşmeyle tanınamaz.",
     "Çıkma için Bakanlık izni gerekir."],
    "Md. 638'e göre şirket sözleşmesi çıkma hakkı tanıyabilir; ayrıca her ortak haklı sebeplerin varlığında şirketten çıkmasına "
    "karar verilmesi için dava açabilir.")

P.q("TTK md. 574",
    f"{K}, limited şirketin tek ortaklı olmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Şirket, tek ortaklılığa yol açan pay edinebilir.",
    ["Şirket tek ortakla kurulabilir.",
     "Tek ortaklılık tescil ve ilan edilir.",
     "Müdürler tescil etmezse zarardan sorumludur.",
     "Ortak sayısı bire düşerse müdürlere bildirilir."],
    "Md. 574/3'e göre şirket, tek ortağının kendisinin olacağı bir şirkete dönüşeceği sonucunu doğuracak şekilde esas sermaye "
    "payını iktisap edemez.", zorluk="hard")

P.q("TTK md. 620",
    f"{K}, limited şirket genel kurul kararlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak salt çoğunlukla alınır.",
    ["Tüm kararlar oybirliğiyle alınır.",
     "Kararlar ortak sayısının üçte ikisiyle alınır.",
     "Seçim kararları müdürlerce alınır.",
     "Kararlar için Bakanlık temsilcisi şarttır."],
    "Md. 620/1'e göre kanun veya şirket sözleşmesinde aksi öngörülmedikçe seçim kararları dahil tüm genel kurul kararları "
    "toplantıda temsil edilen oyların salt çoğunluğuyla alınır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
