#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM İş Hukuku — Çalışma Süreleri konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde Çalışma ve Sosyal Güvenlik Bakanlığından alınan
güncel 4857 sayılı İş Kanunu m.41–47 ve m.63–69 metnidir.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors,
        "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r(
        "Taraflar haftalık çalışma süresini ayrıca kararlaştırmamıştır. İşveren genel kanuni üst sınırın elli saat olduğunu savunmaktadır. Hangisi doğrudur?",
        "İş Kanununa göre genel bakımdan haftalık çalışma süresinin üst sınırı kaç saattir?",
        "Genel haftalık çalışma süresi en çok kırk beş saattir",
        ["Haftalık süre sınırsızdır", "Genel üst sınır altmış saattir", "Çalışma süresi yalnız günlük belirlenir ve haftalık sınır bulunmaz", "Kırk beş saatlik sınır yalnız kamu işyerlerinde ve yöneticiler için uygulanır"],
        "İş Kanunu m.63 genel bakımdan çalışma süresini haftada en çok kırk beş saat olarak belirler.",
        "Taraflar daha kısa süre kararlaştırabilir; kanuni üst sınırın üzerindeki çalışma fazla çalışma rejimine tabidir.",
        "4857 sayılı İş Kanunu m.63", "easy",
    ),
    r(
        "Yer altı maden işçisi günde sekiz, haftada kırk saat normal çalıştırılmıştır. Kanuni özel sınırlar bakımından değerlendirme nedir?",
        "Yer altı maden işlerinde günlük ve haftalık normal çalışma üst sınırları nedir?",
        "Günde yedi buçuk, haftada otuz yedi buçuk saat sınırı uygulanır",
        ["Günde on iki saat sınırı vardır", "Yer altı işinde haftalık süre sınırsızdır", "Yalnız genel kırk beş saat sınırı uygulanır ve günlük sınır yoktur", "Maden işçisine günde on bir, haftada altmış altı saat normal çalışma yaptırılabilir"],
        "İş Kanunu m.63 yer altı maden işlerinde günlük en çok yedi buçuk ve haftalık en çok otuz yedi buçuk saatlik özel sınır koyar.",
        "Bu sınır yer altı maden işçisini genel rejimden daha güçlü korur; normal süre olarak aşılamaz.",
        "4857 sayılı İş Kanunu m.63", "medium",
    ),
    r(
        "Haftalık kırk beş saat tarafların anlaşmasıyla çalışılan günlere farklı dağıtılacaktır. Bir gün için on iki saat planlanmıştır. Hangisi doğrudur?",
        "Haftalık sürenin günlere farklı dağıtılmasında günlük çalışma üst sınırı kaç saattir?",
        "Taraflar anlaşsa bile günlük çalışma on bir saati aşamaz",
        ["Günlük süre sınırsız dağıtılabilir", "Günlük üst sınır yalnız dört saattir", "Haftalık ortalama korunursa bir günde yirmi dört saat çalışma mümkündür", "On bir saat sınırı yalnız işçinin ücret istemediği hâllerde dikkate alınır"],
        "İş Kanunu m.63, tarafların anlaşmasıyla farklı dağıtıma izin verir; ancak günlük çalışma on bir saati aşamaz.",
        "Denkleştirme haftalar arasında esneklik sağlar, günlük sağlık sınırını kaldırmaz.",
        "4857 sayılı İş Kanunu m.63", "medium",
    ),
    r(
        "Haftalık sürenin günlere dağılımına ilişkin farklı anlaşma yoktur. İşveren bazı günlere çok daha fazla süre yüklemiştir. Varsayılan dağıtım nasıl olmalıdır?",
        "Aksi kararlaştırılmamışsa haftalık çalışma süresi çalışılan günlere nasıl bölünür?",
        "Haftanın çalışılan günlerine eşit ölçüde bölünür",
        ["Bütün süre tek güne yüklenir", "Dağıtımı her gün işveren gizlice değiştirir", "Haftalık sürenin günlere dağıtılması kanunen yasaktır", "Süre yalnız hafta tatili gününe ayrılır ve diğer günlerde çalışma yapılamaz"],
        "İş Kanunu m.63 uyarınca aksi kararlaştırılmamışsa haftalık süre haftanın çalışılan günlerine eşit bölünür.",
        "Eşit dağılım yedek kuraldır. Tarafların anlaşmasıyla günlük on bir saat sınırı içinde farklı dağılım yapılabilir.",
        "4857 sayılı İş Kanunu m.63", "easy",
    ),
    r(
        "Taraflar denkleştirme uygulamış; iki aylık dönemde bazı haftalar kırk beş saati aşmış, fakat haftalık ortalama normal süreyi geçmemiştir. Sonuç nedir?",
        "Genel denkleştirmede ortalama hangi dönem ve hangi haftalık sınır içinde kalmalıdır?",
        "İki aylık dönemde haftalık ortalama normal çalışma süresini aşmamalıdır",
        ["Denkleştirme yalnız bir gün sürer", "Ortalama haftada yüz saate kadar çıkabilir", "Denkleştirme işçinin çalışma süresini ölçmeyi tamamen gereksiz kılar", "Bazı haftalardaki her kırk beş saat aşımı ortalamaya bakılmadan daima fazla çalışma sayılır"],
        "İş Kanunu m.63 genel denkleştirme dönemini iki ay kabul eder; haftalık ortalama normal haftalık süreyi aşamaz.",
        "Toplu iş sözleşmesi genel denkleştirme süresini dört aya kadar çıkarabilir. Dönem içindeki tek haftaya değil ortalamaya bakılır.",
        "4857 sayılı İş Kanunu m.63", "hard",
    ),
    r(
        "Turizm işyerinde toplu iş sözleşmesiyle beş aylık denkleştirme dönemi belirlenmiştir. Haftalık ortalama normal süreyi aşmamaktadır. Süre geçerli midir?",
        "Turizm sektöründe denkleştirme dönemi ve toplu iş sözleşmesiyle artırılabilecek üst sınır nedir?",
        "Genel dönem dört ay, toplu iş sözleşmesiyle altı aya kadar olabilir",
        ["Turizmde denkleştirme yasaktır", "Dönem her durumda yalnız iki gündür", "Toplu iş sözleşmesi turizmde süreyi değiştiremez", "Turizmde işveren tek taraflı olarak denkleştirmeyi on iki yıla çıkarabilir"],
        "İş Kanunu m.63 turizm sektöründe denkleştirme dönemini dört ay; toplu iş sözleşmesiyle en çok altı ay olarak düzenler.",
        "Turizm için genel işyerlerinden daha uzun özel dönem kabul edilmiştir; yine haftalık ortalama normal süreyi aşamaz.",
        "4857 sayılı İş Kanunu m.63", "hard",
    ),
    r(
        "İşçi denkleştirme uygulanmayan bir haftada elli saat çalışmıştır. Sözleşmedeki normal haftalık süre kırk beş saattir. Beş saat nasıl nitelendirilir?",
        "Fazla çalışma kavramı kural olarak hangi haftalık eşiğin aşılmasına bağlanmıştır?",
        "Haftalık kırk beş saati aşan çalışma fazla çalışmadır",
        ["Fazla çalışma yalnız yüz saatten sonra başlar", "Kırk beş saat aşımı normal çalışma sayılır", "Fazla çalışma sadece hafta tatilinde yapılan iştir", "Haftalık eşik bulunmaz; işverenin fazla çalışma adını vermesi yeterlidir"],
        "İş Kanunu m.41, kanuni koşullarda haftalık kırk beş saati aşan çalışmayı fazla çalışma sayar.",
        "Denkleştirmede dönem ortalaması normal süreyi aşmıyorsa bazı haftalardaki kırk beş saat aşımı fazla çalışma oluşturmayabilir.",
        "4857 sayılı İş Kanunu m.41", "easy",
    ),
    r(
        "Geçerli denkleştirmede işçi bir hafta kırk sekiz saat, diğer haftalarda daha az çalışmış; dönem ortalaması normal haftalık süreyi aşmamıştır. İlk haftadaki üç saat fazla çalışma mıdır?",
        "Denkleştirme döneminde bazı haftalarda kırk beş saatin aşılmasının fazla çalışmaya etkisi nedir?",
        "Dönem ortalaması normal süreyi aşmıyorsa tek haftadaki aşım fazla çalışma sayılmaz",
        ["Her aşım iki kat fazla çalışmadır", "Denkleştirme fazla çalışma hesabında dikkate alınamaz", "İlk haftadaki bütün çalışma ücretsiz sayılır", "Ortalama korunmuş olsa bile kırk beş saati aşan her dakika yıllık izne dönüşür"],
        "İş Kanunu m.41, m.63'e uygun denkleştirmede haftalık ortalama normal süreyi aşmıyorsa bazı haftalardaki aşımı fazla çalışma saymaz.",
        "Denkleştirme hesabı dönem bütününde yapılır; günlük on bir saat gibi mutlak sınırlar ayrıca korunur.",
        "4857 sayılı İş Kanunu m.41 ve 63", "hard",
    ),
    r(
        "İşçinin normal saat ücreti 200 TL'dir ve bir saat fazla çalışma yapmıştır. Zamlı ücret yerine serbest zaman istememiştir. Saatlik ödeme kaç TL'dir?",
        "Fazla çalışmanın her saati için normal saat ücretine uygulanacak artış oranı nedir?",
        "Yüzde elli artışla 300 TL ödenir",
        ["200 TL ödenir", "Yüzde on artışla 220 TL ödenir", "Fazla çalışma karşılıksızdır", "Normal ücretin yüzde ellisi kesilerek yalnız 100 TL ödeme yapılır"],
        "İş Kanunu m.41, her fazla çalışma saatini normal saat ücretinin yüzde elli yükseltilmesiyle ödetir. 200 × 1,50 = 300 TL'dir.",
        "Fazla çalışma zammı yüzde ellidir; bu, yalnız zam kısmı değil toplam saat ücretinin yüzde yüz ellisi anlamına gelir.",
        "4857 sayılı İş Kanunu m.41", "easy",
    ),
    r(
        "Sözleşmeyle haftalık süre kırk saat belirlenmiştir. İşçi o hafta kırk üç saat çalışmış ve denkleştirme yoktur. Üç saat nasıl ücretlendirilir?",
        "Sözleşmedeki normal süreyi aşan fakat kırk beş saate kadar kalan çalışma hangi zam oranına tabidir?",
        "Fazla sürelerle çalışma sayılır ve saat ücreti yüzde yirmi beş artırılır",
        ["Hiçbir ücret ödenmez", "Fazla çalışma sayılıp yüzde yüz artırılır", "Kırk beş saate kadar her çalışma ücretsiz normal süredir", "Sözleşmedeki kırk saatlik sınır işverenin tek taraflı kararıyla yok sayılır"],
        "İş Kanunu m.41, sözleşmeyle kırk beş saatin altında belirlenen normal süreyi aşıp kırk beşe kadar kalan çalışmayı fazla sürelerle çalışma sayar ve yüzde yirmi beş zam öngörür.",
        "Kırk beş saat üstü fazla çalışma, sözleşmesel sınır ile kırk beş arasındaki bölüm fazla sürelerle çalışmadır.",
        "4857 sayılı İş Kanunu m.41", "medium",
    ),
    r(
        "İşçi iki saat fazla çalışma karşılığında zamlı ücret yerine serbest zaman seçmiştir. Ne kadar serbest zaman hakkı doğar?",
        "Fazla çalışmanın her saati karşılığında işçi zamlı ücret yerine ne kadar serbest zaman kullanabilir?",
        "Her saat için bir saat otuz dakika; iki saat için üç saat serbest zaman",
        ["İki saat için yalnız bir saat", "Her saat için on beş dakika", "Serbest zaman seçimi kanunen yasaktır", "İki saat fazla çalışma karşılığında tam iki hafta ücretsiz izin kullanılır"],
        "İş Kanunu m.41, fazla çalışmanın her saati için bir saat otuz dakika serbest zaman verir. İki saat karşılığı üç saattir.",
        "Fazla sürelerle çalışmanın her saati için ise bir saat on beş dakika serbest zaman öngörülür.",
        "4857 sayılı İş Kanunu m.41", "medium",
    ),
    r(
        "İşçi fazla çalışma karşılığı hak ettiği serbest zamanı sekiz ay sonra ve ücretinden kesinti yapılarak kullanabilmiştir. Uygulama doğru mudur?",
        "Fazla çalışma karşılığı serbest zaman hangi süre içinde ve ücret yönünden nasıl kullandırılır?",
        "Altı ay içinde, çalışma süresinde ve ücret kesintisi olmadan kullandırılır",
        ["Süre sınırı yoktur", "Serbest zaman yalnız ücretsiz kullandırılır", "İşveren serbest zamanı emeklilikten sonra kullandırabilir", "Serbest zaman çalışma saatleri dışında ve işçinin ücretinin tamamı kesilerek kullandırılır"],
        "İş Kanunu m.41, hak edilen serbest zamanı altı ay içinde, çalışma süreleri içinde ve ücret kesintisi olmadan kullandırır.",
        "Serbest zaman zamlı ücretin alternatifidir; işçinin dinlenme hakkına dönüşür ve ücretsiz izin sayılamaz.",
        "4857 sayılı İş Kanunu m.41", "medium",
    ),
    r(
        "Olağan fazla çalışma için işçinin onayı alınmamış; işveren üretim ihtiyacını gerekçe göstermiştir. Hangisi doğrudur?",
        "Kanundaki zorunlu ve olağanüstü hâller dışında fazla saatlerle çalışma için hangi koşul aranır?",
        "İşçinin onayı alınmalıdır",
        ["Onay hiçbir zaman aranmaz", "Yalnız işveren vekilinin kendine verdiği izin yeterlidir", "İşçinin sessiz kalması ömür boyu sınırsız fazla çalışma onayıdır", "Onay sadece fazla çalışmanın yıllık üst sınırı aşıldıktan sonra alınabilir"],
        "İş Kanunu m.41, fazla saatlerle çalışma için işçinin onayını arar. m.42 ve m.43'teki özel hâller ayrı rejime tabidir.",
        "Olağan işletme ihtiyaçları işçinin onayını ortadan kaldırmaz. Onayın usulü ilgili yönetmelikte düzenlenir.",
        "4857 sayılı İş Kanunu m.41-43", "easy",
    ),
    r(
        "İşçi bir takvim yılında olağan fazla çalışma kapsamında toplam 300 saat çalıştırılmıştır. Kanuni yıllık üst sınır bakımından hangisi doğrudur?",
        "Olağan fazla çalışma süresinin bir işçi için yıllık toplam üst sınırı kaç saattir?",
        "Yıllık fazla çalışma toplamı iki yüz yetmiş saati aşamaz",
        ["Yıllık fazla çalışma için hiçbir üst sınır bulunmaz", "Yıllık üst sınır yalnız on saat olarak uygulanır", "Yıllık sınır tam beş yüz saattir", "İşçinin onayı varsa iki yüz yetmiş saatlik sınır sınırsız biçimde aşılabilir"],
        "İş Kanunu m.41, fazla çalışma süresinin toplamını yılda iki yüz yetmiş saatle sınırlar.",
        "İşçinin onayı üst sınırı kaldırmaz. Sınır işçi bazında yıllık toplam fazla çalışma süresini korur.",
        "4857 sayılı İş Kanunu m.41", "easy",
    ),
    r(
        "İşveren, gece çalışan işçiye olağan üretim artışı gerekçesiyle fazla çalışma yaptırmak istemektedir. Kanuni yasak bakımından hangisi doğrudur?",
        "İş Kanunu m.41'e göre hangi çalışma türlerinde olağan fazla çalışma yapılamaz?",
        "Sağlık nedeniyle kısa veya sınırlı işlerde ve gece çalışmasında fazla çalışma yapılamaz",
        ["Bütün işlerde sınırsız yapılabilir", "Yasak yalnız gündüz büro işlerinde uygulanır", "Gece çalışmasında işçi onayı her yasağı kendiliğinden kaldırır", "Sağlık nedeniyle kısaltılmış işlerde fazla çalışma yapmak işverenin tercihine bırakılmıştır"],
        "İş Kanunu m.41, m.63'ün sağlık nedenli kısa-sınırlı işleri ile m.69'daki gece çalışmasında fazla çalışmayı yasaklar.",
        "Bu koruyucu yasak olağan onayla aşılamaz. Özel sektör gece süresi istisnaları normal gece çalışmasının sınırına ilişkindir.",
        "4857 sayılı İş Kanunu m.41", "medium",
    ),
    r(
        "Yer altı maden işçisine olağan üretim artışı nedeniyle fazla çalışma yaptırılmıştır. Arıza, zorlayıcı neden veya seferberlik yoktur. Hangisi doğrudur?",
        "Yer altı maden işçilerine fazla çalışma hangi özel hâller dışında yaptırılamaz?",
        "Yalnız zorunlu neden ve olağanüstü hâl istisnaları dışında yasaktır",
        ["Her gün sınırsız yapılabilir", "Yasak yalnız işçinin kıdemi bir yıldan azsa geçerlidir", "Üretim artışı tek başına yer altı fazla çalışmasını zorunlu kılar", "Maden işçisi yazılı onay verirse m.42 ve m.43 dışındaki her fazla çalışma serbest olur"],
        "İş Kanunu m.41, yer altı maden işçilerine m.42'deki zorunlu ve m.43'teki olağanüstü hâller dışında fazla çalışmayı yasaklar.",
        "İstisnai fazla çalışmada haftalık otuz yedi buçuk saati aşan her saat için en az yüzde yüz zam uygulanır.",
        "4857 sayılı İş Kanunu m.41-43", "hard",
    ),
    r(
        "İşyerindeki ani arıza normal çalışmayı durdurmuştur. İşveren yalnız normal düzeni sağlayacak ölçüde fazla çalışma yaptırmış, ardından uygun dinlenme vermiştir. Hangi rejim uygulanır?",
        "Zorunlu nedenlerle fazla çalışmanın oluşabileceği durum ve sınır nedir?",
        "Arıza, acil iş veya zorlayıcı nedende normal çalışmayı sağlayacak ölçüde yapılabilir",
        ["Her ticari sipariş zorunlu nedendir", "Zorunlu çalışmada dinlenme verilmesi yasaktır", "Fazla çalışma işyeri normalini aşacak sınırsız üretim için yapılır", "Arıza ihtimali bulunsa bile işveren hiçbir koruyucu işlem veya fazla çalışma yaptıramaz"],
        "İş Kanunu m.42; arıza, arıza ihtimali, makineler için acil iş veya zorlayıcı nedenlerde normal çalışmayı sağlayacak dereceyi aşmayan fazla çalışmaya izin verir.",
        "Bu çalışmadan sonra uygun dinlenme verilmesi zorunludur; ücrette m.41'in temel hükümleri uygulanır.",
        "4857 sayılı İş Kanunu m.42", "medium",
    ),
    r(
        "Ulusal bayram gününde çalışma hakkında iş veya toplu iş sözleşmesinde hüküm yoktur. İşveren işçiyi onaysız çalıştırmak istemektedir. Hangisi doğrudur?",
        "Ulusal bayram ve genel tatil çalışması sözleşmede düzenlenmemişse hangi koşul aranır?",
        "İşçinin onayı gerekir",
        ["Onay hiçbir zaman gerekmez", "İşçi her tatilde ücretsiz çalışmak zorundadır", "Yalnız işverenin müşterisinin onayı yeterlidir", "Sözleşmede hüküm yoksa ulusal bayram günü otomatik olarak normal iş gününe dönüşür"],
        "İş Kanunu m.44, tatil gününde çalışma konusunu sözleşmelere bırakır; hüküm yoksa işçinin onayını arar.",
        "Çalışmaya ilişkin onay ile ücret hakkı farklı konulardır; tatil ücretleri m.47'ye göre ayrıca ödenir.",
        "4857 sayılı İş Kanunu m.44", "easy",
    ),
    r(
        "İşçi, tatilden önceki kanuni iş günlerinde çalışmıştır. Yedi günlük dönem içinde yalnız on sekiz saat kesintisiz dinlenme verilmiştir. Hafta tatili uygun mudur?",
        "Hafta tatilinde yedi günlük zaman dilimi içinde verilmesi gereken kesintisiz asgari dinlenme kaç saattir?",
        "Kesintisiz en az yirmi dört saat dinlenme verilmelidir",
        ["Altı saat yeterlidir", "Hafta tatilinde dinlenme zorunlu değildir", "Dinlenme ayda bir kez iki saat verilebilir", "Yirmi dört saatlik dinlenme yalnız işverenin ücret ödememesi şartıyla mümkündür"],
        "İş Kanunu m.46, gerekli iş günlerinde çalışan işçiye yedi günlük dönem içinde kesintisiz en az yirmi dört saat hafta tatili verir.",
        "Çalışılmayan hafta tatili günü için bir iş karşılığı olmadan tam günlük ücret ödenir.",
        "4857 sayılı İş Kanunu m.46", "easy",
    ),
    r(
        "İşçi ulusal bayram gününde çalışmamıştır. Başka özel düzenleme yoktur. O güne ait ücret hakkı nedir?",
        "Ulusal bayram veya genel tatil gününde çalışmayan ve çalışan işçinin ücret hakkı nasıl ayrılır?",
        "Çalışmazsa tam günlük ücret, çalışırsa buna ek bir günlük ücret alır",
        ["Çalışmayan hiç ücret alamaz", "Çalışan yalnız normal tek günlük ücret alır", "Tatil ücreti yalnız ücretsiz izin olarak verilir", "Çalışma hâlinde işçi işverene ayrıca bir günlük ücret ödemek zorundadır"],
        "İş Kanunu m.47, çalışmayana iş karşılığı olmadan tam günlük ücret; çalışana bunun yanında ayrıca bir günlük ücret öngörür.",
        "Tatil günü çalışılması iki günlük toplam tutar sonucu doğurur: tatil ücreti ve çalışmanın karşılığı.",
        "4857 sayılı İş Kanunu m.47", "medium",
    ),
    r(
        "Zorunlu nedenle iş durmuş; işveren çalışılmayan süreler için altı ay sonra telafi çalışması yaptırmıştır. Cumhurbaşkanınca süre uzatılmamıştır. Uygulama uygun mudur?",
        "Telafi çalışması kural olarak çalışılmayan süreden sonra hangi süre içinde yaptırılabilir?",
        "Dört ay içinde yaptırılabilir ve fazla çalışma sayılmaz",
        ["Süre sınırsızdır", "Yalnız aynı gün yaptırılabilir", "Telafi çalışması her durumda yıllık fazla çalışma sınırına eklenir", "İşveren telafiyi yalnız işçi yıllık iznini kullandıktan on yıl sonra yaptırabilir"],
        "İş Kanunu m.64, zorunlu durma, tatil veya işçinin talebiyle izin gibi hâllerde dört ay içinde telafi çalışmasına izin verir ve bunu fazla çalışma saymaz.",
        "Cumhurbaşkanı dört aylık süreyi iki katına kadar artırabilir. Somut uzatma yoksa genel dört aylık süre uygulanır.",
        "4857 sayılı İş Kanunu m.64", "medium",
    ),
    r(
        "İşveren telafi çalışmasını günde dört saat ve hafta tatilinde yaptırmıştır. Günlük genel üst süre aşılmamıştır. Hangisi doğrudur?",
        "Telafi çalışmasının günlük ek süre ve tatil günü bakımından sınırları nedir?",
        "Günde en çok üç saat olabilir ve tatil günlerinde yaptırılamaz",
        ["Günde sınırsız olabilir", "Tatil günü yapılması zorunludur", "Telafi yalnız gece yarısından sonra yaptırılır", "Günlük üç saat sınırı işverenin tek taraflı bildirimiyle yirmi saate çıkarılabilir"],
        "İş Kanunu m.64, günlük en çok çalışma süresi aşılmamak üzere telafiyi günde üç saatle sınırlar ve tatil gününde yasaklar.",
        "Telafi geçmişte çalışılmayan sürenin karşılığıdır; dinlenme gününü ortadan kaldıracak şekilde uygulanamaz.",
        "4857 sayılı İş Kanunu m.64", "medium",
    ),
    r(
        "İşçi işveren tarafından başka şehirde çalıştırılmak üzere gönderilmiş ve yolda zaman geçirmiştir. Bu süre çalışma süresinden sayılır mı?",
        "İşveren tarafından başka yerde çalıştırılmak üzere gönderilen işçinin yolda geçen süresi nasıl değerlendirilir?",
        "Yolda geçen süre günlük çalışma süresinden sayılır",
        ["Hiçbir yol süresi sayılmaz", "Yol süresi yalnız işçi ücret istemezse çalışma olur", "Başka yere gönderme iş sözleşmesini kendiliğinden sona erdirir", "Yolda geçen süre çalışma süresinden düşülüp işçinin yıllık izninden mahsup edilir"],
        "İş Kanunu m.66, işveren tarafından başka yerde çalıştırılmak üzere gönderilen işçinin yolda geçen süresini çalışma süresinden sayar.",
        "İşçinin her an iş görmeye hazır beklediği süre ve işverenin başka yerde meşgul ettiği süre de çalışma süresine dâhildir.",
        "4857 sayılı İş Kanunu m.66", "easy",
    ),
    r(
        "İşveren sırf sosyal yardım amacıyla, işin niteliği gerektirmediği hâlde çalışanlara servis sağlamıştır. Serviste geçen süre çalışma süresi midir?",
        "İşverenin yalnız sosyal yardım amacıyla sağladığı ulaşımda araçta geçen süre nasıl değerlendirilir?",
        "İşin niteliğinden doğmuyorsa çalışma süresinden sayılmaz",
        ["Her servis süresi fazla çalışmadır", "Süre daima günlük iki kat çalışma sayılır", "Sosyal servis kullanımı işçiyi işveren vekiline dönüştürür", "Araçta geçen sürenin sayılmaması için işçinin ücretinden servis bedeli kesilmesi zorunludur"],
        "İş Kanunu m.66, işin niteliğinden doğmayan ve sırf sosyal yardım amaçlı götürülüp getirilmede araçta geçen süreyi çalışma süresinden saymaz.",
        "Uzak işyerine işin gereği toplu ve düzenli taşıma ile sosyal servis birbirinden ayrılır; ilkinde süre çalışma sayılabilir.",
        "4857 sayılı İş Kanunu m.66", "hard",
    ),
    r(
        "İşçi günlük sekiz saat çalışmaktadır. İşveren yalnız yarım saat ara dinlenmesi vermiştir. Kanuni asgari süre nedir?",
        "Dört, yedi buçuk ve sekiz saatlik günlük çalışmalarda ara dinlenmesi basamakları nasıl uygulanır?",
        "Yedi buçuk saati aşan işte en az bir saat ara dinlenmesi verilir",
        ["Ara dinlenmesi hiç verilmez", "Sekiz saatlik işte yalnız beş dakika yeterlidir", "Bütün günlük sürelerde zorunlu ara tam üç saattir", "Ara dinlenmesi yalnız işçi ücretinden iki saat kesinti yapılırsa kullandırılabilir"],
        "İş Kanunu m.68; dört saate kadar on beş dakika, dört saatten fazla-yedi buçuk saate kadar yarım saat, daha uzun işte bir saat asgari ara verir.",
        "Sekiz saat yedi buçuk saati aştığı için en az bir saat ara dinlenmesi gerekir. Ara dinlenmesi çalışma süresinden sayılmaz.",
        "4857 sayılı İş Kanunu m.68", "medium",
    ),
    r(
        "İşçi genel bir işte gece postasında dokuz saat çalıştırılmış ve yazılı onayı alınmamıştır. İş turizm, güvenlik, sağlık veya petrol faaliyeti değildir. Hangisi doğrudur?",
        "Gece çalışmasının genel azami süresi ve bu sürenin üzerindeki özel sektör istisnaları nelerdir?",
        "Genel sınır yedi buçuk saattir; sayılan özel işlerde yazılı onayla aşılabilir",
        ["Gece süresi sınırsızdır", "Bütün işlerde sözlü onayla on altı saat gece çalışılır", "Yedi buçuk saat sınırı yalnız gündüz postalarında uygulanır", "Özel sektör istisnası her işyerini ve işçinin onayı olmadan yapılan tüm gece çalışmalarını kapsar"],
        "İş Kanunu m.69 gece çalışmasını genel olarak yedi buçuk saatle sınırlar; turizm, özel güvenlik, sağlık ve kanundaki petrol faaliyetlerinde yazılı onayla aşılabilir.",
        "İstisna sektör ve yazılı onay koşullarına bağlıdır. Posta değişiminde ayrıca kesintisiz en az on bir saat dinlenme gerekir.",
        "4857 sayılı İş Kanunu m.69", "hard",
    ),
]


PREMISES = [
    {
        "stem": "Normal çalışma süresiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel haftalık üst sınır kırk beş saattir.\n\nII. Farklı dağıtımda günlük süre on bir saati aşamaz.\n\nIII. Yer altı maden işinde haftalık üst sınır otuz yedi buçuk saattir.",
        "correct": "I, II ve III", "why": "İş Kanunu m.63 uyarınca üç ifade de doğrudur.",
        "ref": "4857 sayılı İş Kanunu m.63", "difficulty": "medium",
    },
    {
        "stem": "Fazla çalışma ücretleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fazla çalışma saat ücreti yüzde elli artırılır.\n\nII. Fazla sürelerle çalışma saat ücreti yüzde yirmi beş artırılır.\n\nIII. İşçi zamlı ücret yerine kanuni serbest zamanı seçebilir.",
        "correct": "I, II ve III", "why": "İş Kanunu m.41 uyarınca üç ifade de doğrudur.",
        "ref": "4857 sayılı İş Kanunu m.41", "difficulty": "medium",
    },
    {
        "stem": "Fazla çalışma sınırlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Olağan fazla çalışmada işçi onayı aranır.\n\nII. Yıllık toplam iki yüz yetmiş saati aşamaz.\n\nIII. Gece çalışmasında olağan fazla çalışma yapılabilir.",
        "correct": "I ve II", "why": "İş Kanunu m.41 nedeniyle I ve II doğrudur. Gece çalışmasında fazla çalışma yasak olduğundan III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.41", "difficulty": "medium",
    },
    {
        "stem": "Telafi çalışmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel olarak dört ay içinde yaptırılır.\n\nII. Günde en çok üç saat olabilir.\n\nIII. Tatil günlerinde yaptırılması zorunludur.",
        "correct": "I ve II", "why": "İş Kanunu m.64 nedeniyle I ve II doğrudur. Tatil günlerinde telafi çalışması yasak olduğundan III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.64", "difficulty": "medium",
    },
    {
        "stem": "Çalışma süresinden sayılan hâllerle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Başka yerde çalıştırılmak üzere gönderilirken yolda geçen süre sayılır.\n\nII. İşçinin iş görmeye hazır beklediği süre sayılmaz.\n\nIII. Süt izni süreleri çalışma süresinden sayılır.",
        "correct": "I ve III", "why": "İş Kanunu m.66 nedeniyle I ve III doğrudur. İş görmeye hazır bekleme süresi de çalışma sayıldığından II yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.66", "difficulty": "hard",
    },
    {
        "stem": "Ara dinlenmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dört saate kadar en az on beş dakikadır.\n\nII. Yedi buçuk saati aşan işte en az bir saattir.\n\nIII. Ara dinlenmesi çalışma süresinden sayılır.",
        "correct": "I ve II", "why": "İş Kanunu m.68 nedeniyle I ve II doğrudur. Ara dinlenmesi çalışma süresinden sayılmadığından III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.68", "difficulty": "medium",
    },
    {
        "stem": "Gece çalışmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel gece çalışma sınırı yedi buçuk saattir.\n\nII. Sayılı özel işlerde yalnız sözlü onayla sınır aşılabilir.\n\nIII. Posta değişiminde en az on bir saat kesintisiz dinlenme gerekir.",
        "correct": "I ve III", "why": "İş Kanunu m.69 nedeniyle I ve III doğrudur. Sayılı özel işlerde yazılı onay gerektiğinden II yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.69", "difficulty": "hard",
    },
    {
        "stem": "Tatil çalışmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sözleşmede hüküm yoksa ulusal bayram çalışması için işçi onayı gerekir.\n\nII. Hafta tatili kesintisiz en az yirmi dört saattir.\n\nIII. Genel tatilde çalışan işçiye yalnız tatil ücreti ödenir, ek günlük ücret verilmez.",
        "correct": "I ve II", "why": "İş Kanunu m.44 ve 46 nedeniyle I ve II doğrudur. Çalışılan tatil günü için ayrıca bir günlük ücret gerektiğinden III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.44, 46-47", "difficulty": "medium",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="is_hukuku", topic_id="calisma_sureleri",
        label="Çalışma Süreleri", slug="calisma_sureleri",
        prefix="kh-cal-sure", seed=20260730,
        legislation_version="4857 sayılı İş Kanunu m.41–47 ve 63–69 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
