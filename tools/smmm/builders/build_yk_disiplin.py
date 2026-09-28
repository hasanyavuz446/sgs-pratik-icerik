# -*- coding: utf-8 -*-
"""Meslek Hukuku · Disiplin Hükümleri — 60 soru, 2026 test biçimi.

Dayanak metinler (28.09.2026 kontrolü, TÜRMOB 2026 derlemesi):
  · 3568 sayılı Kanun m. 43, 47, 48, 49 (27.03.2025-7546 değişiklikleri işlenmiş)
  · SMMM ve YMM Kanunu Disiplin Yönetmeliği (RG 31.10.2000/24216; 07.10.2023-32332
    ve 14.01.2026-33137 değişiklikleri işlenmiş)
Gerçek sınav profili: Meslek Hukuku olumsuz kök %50, atıf %65, süre/sayı %18.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_disiplin_2026.json", lesson="meslek_hukuku", topic="disiplin",
          konu_adi="Disiplin Hükümleri", seed=2026092801,
          surum="3568 s. Kanun (27.03.2025-7546 işlenmiş) ve Disiplin Yönetmeliği (14.01.2026-33137 işlenmiş), 28.09.2026 kontrolü")

DY = "Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu Disiplin Yönetmeliği’ne göre"
K = "3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu’na göre"

# ---------------------------------------------------------------- ceza türleri
P.q("Disiplin Yönetmeliği m. 4",
    f"{DY}, aşağıdakilerden hangisi meslek mensuplarına ve aday meslek mensuplarına uygulanabilecek disiplin cezaları arasında yer almaz?",
    "Para cezası",
    ["Uyarma", "Kınama", "Geçici olarak mesleki faaliyetten alıkoyma", "Meslekten çıkarma"],
    "Yönetmeliğin 4. maddesi disiplin cezalarını uyarma, kınama, geçici olarak mesleki faaliyetten alıkoyma, "
    "yeminli sıfatını kaldırma ve meslekten çıkarma olarak sayar. Para cezası bir disiplin cezası değildir; "
    "Kanun'un 49. maddesindeki adli para cezası ceza mahkemesince verilen bir yaptırımdır.",
    zorluk="easy")

P.q("3568 s. Kanun m. 48/2-c; Disiplin Yönetmeliği m. 4/c",
    f"{DY}, geçici olarak mesleki faaliyetten alıkoyma cezasının tanımı aşağıdakilerden hangisinde doğru olarak verilmiştir?",
    "Mesleki sıfatı saklı kalmak koşuluyla altı aydan az, bir yıldan fazla olmamak üzere mesleki faaliyetten alıkoymadır.",
    ["Mesleki sıfatı saklı kalmak koşuluyla bir aydan az, altı aydan fazla olmamak üzere mesleki faaliyetten alıkoymadır.",
     "Mesleki sıfatı saklı kalmak koşuluyla üç aydan az, altı aydan fazla olmamak üzere mesleki faaliyetten alıkoymadır.",
     "Ruhsatname geri alınarak bir yıldan az, üç yıldan fazla olmamak üzere mesleki faaliyetten alıkoymadır.",
     "Ruhsatname ve kaşe geri alınarak altı aydan az, iki yıldan fazla olmamak üzere mesleki faaliyetten alıkoymadır."],
    "Kanun m. 48 ve Yönetmelik m. 4/c'ye göre alıkoyma cezasında mesleki sıfat saklı kalır; süre altı aydan az, "
    "bir yıldan fazla olamaz. Ruhsatnamenin geri alınması meslekten çıkarma cezasının unsurudur.")

P.q("Disiplin Yönetmeliği m. 4/d ve 4/e",
    f"{DY}, yeminli sıfatını kaldırma ve meslekten çıkarma cezalarının sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yeminli sıfatını kaldırma cezasında yeminli mali müşavirin ruhsatnamesi geri alınarak mesleği yürütmesine bir daha izin verilmez.",
    ["Yeminli sıfatını kaldırma cezasında yeminli mali müşavirin yeminli sıfatı kaldırılır ve mührü geri alınır.",
     "Meslekten çıkarma cezasında meslek mensubunun ruhsatnamesi geri alınarak mesleği bir daha yürütmesine izin verilmez.",
     "Yeminli sıfatını kaldırma cezası, yeminli mali müşavir unvanı taşıyan meslek mensuplarına özgü bir cezadır.",
     "Meslekten çıkarma cezası kesinleştikten sonra meslek mensubu iş kabul edemez, mühür ya da kaşe kullanamaz ve işlerini odaya teslim eder."],
    "Ruhsatnamenin geri alınıp mesleğin bir daha yürütülmesine izin verilmemesi meslekten çıkarma cezasının tanımıdır "
    "(m. 4/e). Yeminli sıfatını kaldırma cezasında yeminli sıfat kaldırılır ve mühür geri alınır (m. 4/d, m. 8).",
    zorluk="hard")

# ---------------------------------------------------------------- uyarma
P.q("Disiplin Yönetmeliği m. 5",
    f"{DY}, aşağıdakilerden hangisi uyarma cezasını gerektiren haller arasında sayılmamıştır?",
    "Meslek mensubunca reklam yasağına uyulmaması",
    ["Mevzuata aykırı tabela kullanılması",
     "Adres değişikliğinin süresinde bildirilmemesi",
     "Oda kurullarının istediği belge ve bilginin verilmemesi",
     "Yazıyla iki kez istenen aidat borcunun ödenmemesi"],
    "Reklam yasağına uyulmaması m. 6/f uyarınca kınama cezası gerektirir. Tabela (m. 5/e), adres değişikliği "
    "(m. 5/i), oda kurullarına belge vermeme (m. 5/k) ve en az iki kez yazıyla istendiği hâlde aidatın haklı "
    "gerekçe olmadan ödenmemesi (m. 5/h) uyarma halleridir.")

P.sayisal("Disiplin Yönetmeliği m. 5/a",
    f"{DY}, sözleşmenin taraflarca feshi hâlinde iş sahibinin defter ve belgelerinin en geç kaç gün içinde devir ve "
    "teslim tutanağı düzenlenerek teslim edilmemesi uyarma cezasını gerektirir?",
    "30", ["7", "15", "45", "60"],
    "Yönetmelik m. 5/a'ya göre sözleşmenin feshinde defter ve belgelerin otuz gün içinde devir ve teslim tutanağıyla "
    "teslim edilmemesi uyarma cezası gerektirir. Devir ve teslimin gerçekleşemediğinin meslek mensubunca odaya "
    "bildirildiği durum bu hükmün dışındadır.")

P.q("Disiplin Yönetmeliği m. 5/h",
    "Serbest muhasebeci mali müşavir (A), oda aidat borcunu haklı bir gerekçe göstermeden ödememektedir. "
    f"{DY}, (A) hakkında uyarma cezası uygulanabilmesi için aşağıdaki koşullardan hangisinin gerçekleşmiş olması gerekir?",
    "Aidat borcunun en az iki kez yazı ile istenmiş olması",
    ["Aidat borcunun en az üç kez yazı ile istenmiş olması",
     "Aidat borcunun bir takvim yılını aşmış olması",
     "Aidat borcunun icra takibine konu edilmiş olması",
     "Aidat borcunun Birlik Yönetim Kurulunca ilan edilmiş olması"],
    "Yönetmelik m. 5/h uyarma cezasını, en az iki kez yazı ile istenmesine rağmen oda aidat borçlarının haklı gerekçe "
    "olmaksızın ödenmemesine bağlar. Borcun süresi, icra takibi veya ilan şart olarak aranmaz.")

P.q("Disiplin Yönetmeliği m. 5/c ve 10",
    f"{DY}, aday meslek mensubunun mesleğin vakar ve onuru ile bağdaşmayan işler yapmasına bilerek izin veren "
    "meslek mensubuna hangi disiplin cezası uygulanır?",
    "Uyarma",
    ["Kınama", "Geçici olarak mesleki faaliyetten alıkoyma", "Meslekten çıkarma", "Yeminli sıfatını kaldırma"],
    "Aday meslek mensubunun vakar ve onurla bağdaşmayan işler yapmasına neden olunması, bilerek izin verilmesi veya "
    "göz yumulması m. 5/c'de uyarma hâli olarak sayılmıştır.")

# ---------------------------------------------------------------- kınama
P.q("Disiplin Yönetmeliği m. 6",
    f"{DY}, aşağıdakilerden hangisi kınama cezasını gerektiren haller arasında yer almaz?",
    "Ticari faaliyet yasağına uyulmaması",
    ["Sahip olunmayan unvanların kullanılması",
     "Asgari ücret tarifesinin altında iş kabul edilmesi",
     "Büro tescil belgesinin süresinde vize ettirilmemesi",
     "Yazılı hizmet sözleşmesi yapılmadan iş kabul edilmesi"],
    "Ticari faaliyet yasağına uyulmaması m. 7/e uyarınca geçici olarak mesleki faaliyetten alıkoyma cezası gerektirir. "
    "Unvan (m. 6/b), asgari ücret altında iş (m. 6/g), büro tescil belgesi (m. 6/r) ve yazılı sözleşme (m. 6/d) "
    "kınama halleridir.")

P.q("Disiplin Yönetmeliği m. 6/a",
    f"{DY}, uyarma cezası gerektiren eylemlerin yinelenmesi hâlinde kınama cezası uygulanabilmesi için aşağıdakilerden hangisi gerekir?",
    "Üç yıllık bir dönem içinde uyarma cezası gerektiren bir eylemin üçüncü kez yinelenmesi",
    ["Beş yıllık bir dönem içinde uyarma cezası gerektiren bir eylemin üçüncü kez yinelenmesi",
     "Üç yıllık bir dönem içinde uyarma cezası gerektiren bir eylemin ikinci kez yinelenmesi",
     "Bir takvim yılı içinde uyarma cezası gerektiren bir eylemin ikinci kez yinelenmesi",
     "İki yıllık bir dönem içinde uyarma cezası gerektiren bir eylemin dördüncü kez yinelenmesi"],
    "M. 6/a'ya göre üç yıllık dönem içinde üçüncü kez uyarma cezası gerektiren bir eylemin yinelenmesi kınama sebebidir. "
    "M. 11 uyarınca bunun için ilk iki cezanın kesinleşip ilgiliye bildirilmiş olması da gerekir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 6/ş",
    "Yanında staj yaptığı meslek mensubunun müşterilerine, ruhsatını aldıktan kısa süre sonra onun rızası olmadan hizmet "
    f"vermeye başlayan yeni meslek mensubu için {DY.replace('’ne göre', '’nde')} öngörülen bekleme süresi ve ceza aşağıdakilerin hangisinde birlikte doğru verilmiştir?",
    "İki yıl; kınama",
    ["Bir yıl; uyarma", "Bir yıl; kınama", "İki yıl; uyarma", "Üç yıl; kınama"],
    "M. 6/ş'ye göre stajını tamamlayıp mesleği yapmaya hak kazananlar ruhsatı aldıkları tarihten itibaren iki yıl "
    "geçmedikçe, yanında staj yaptıkları meslek mensubunun rızası olmadan onun müşterilerine hizmet veremez; "
    "aykırılık kınama cezası gerektirir.")

P.q("Disiplin Yönetmeliği m. 6/n ve 7/f",
    "Serbest muhasebeci mali müşavir (B), kasıt olmaksızın gerekli özeni göstermeden ilan olunmuş standartlara aykırı bir "
    f"beyannameyi imzalamıştır. {DY}, (B)'ye uygulanacak ceza aşağıdakilerden hangisidir?",
    "Kınama",
    ["Uyarma", "Geçici olarak mesleki faaliyetten alıkoyma", "Meslekten çıkarma", "Üç yıl süreyle mesleki faaliyetten alıkoyma"],
    "Kasıt bulunmadan özen eksikliğiyle standartlara aykırı beyanname imzalanması m. 6/n'de kınama hâlidir. Aynı "
    "aykırılık kasten yapılsaydı m. 7/f uyarınca geçici olarak mesleki faaliyetten alıkoyma cezası gerekirdi.")

P.q("Disiplin Yönetmeliği m. 6/s",
    f"{DY}, aşağıdaki büro düzenine ilişkin aykırılıklardan hangisi kınama cezasını gerektiren haller arasında sayılmamıştır?",
    "Büronun kira sözleşmesiyle kullanılan bir taşınmazda bulunması",
    ["Açılan işyerinin bağımsız büro şeklinde olmaması",
     "Büronun başka bir ticari faaliyet ile iç içe olması",
     "Ev olarak kullanılan ikametgâhın aynı zamanda büro olması",
     "Ortaklık durumu dışında meslek mensubunun birden fazla bürosunun bulunması"],
    "M. 6/s büro standartlarına uyulmamasını, işyerinin bağımsız olmamasını, başka faaliyetle iç içe olmasını, "
    "ikametgâhın büro olarak kullanılmasını ve ortaklık dışında birden fazla büro bulunmasını kınama hâli sayar. "
    "Büronun kiralık olması bir aykırılık değildir.")

P.q("Disiplin Yönetmeliği m. 6/t, 6/u, 6/v",
    f"{DY}, aşağıdakilerden hangisi kınama cezası gerektiren haksız rekabet eylemlerinden biri değildir?",
    "Meslek ruhsatnamesinin başka bir kişiye bedelsiz kullandırılması",
    ["Üçüncü kişilere ücret ya da başka bir çıkar vaat edilerek iş alınması",
     "Meslektaş hakkında asılsız ihbarda bulunulması",
     "Hizmetler hakkında yanıltıcı açıklama yapılması",
     "Emredici kurallara aykırılıkla rekabet avantajı yaratılması"],
    "Ruhsatnamenin bedelli veya bedelsiz başkasına kullandırılması Kanun m. 48 (7546 s. Kanunla eklenen fıkra) ve "
    "Yönetmelik m. 9/d uyarınca meslekten çıkarma cezası gerektirir. Diğerleri m. 6/u, v, t ve ü'de kınama halleridir.",
    zorluk="hard")

# ---------------------------------------------------------------- alıkoyma
P.q("Disiplin Yönetmeliği m. 7",
    f"{DY}, aşağıdakilerden hangisi geçici olarak mesleki faaliyetten alıkoyma cezasını gerektiren haller arasında yer almaz?",
    "Çalışanlar listesine kaydolmadan unvan kullanılarak mesleki faaliyette bulunulması",
    ["Meslek dışı kişilerle mevzuata aykırı işbirliği yapılması",
     "Müşteriden toplanan paranın kendisine mal edilmesi",
     "Kesinleşen alıkoyma cezasına rağmen faaliyete devam edilmesi",
     "Unvanla, gerçek veya tüzel kişilere bağlı olarak hizmet sözleşmesiyle çalışılması"],
    "Çalışanlar listesine kaydolmadan unvan kullanılarak mesleki faaliyette bulunulması m. 6/i'de kınama hâlidir. "
    "Diğer seçenekler m. 7/c, d, h ve b'de sayılan alıkoyma halleridir.")

P.sayisal("Disiplin Yönetmeliği m. 7 son fıkra; VUK m. 153/A",
    f"{DY}, 213 sayılı Vergi Usul Kanunu’nun 153/A maddesinin birinci fıkrasında sayılan haller nedeniyle mükellefiyeti "
    "terkin edilenlerin fiillerine iştirak ettiği inceleme raporuyla tespit edilen ve bu durumu kesinleşen meslek "
    "mensubu hakkında kaç yıl süreyle geçici olarak mesleki faaliyetten alıkoyma cezası uygulanır?",
    "3", ["1", "2", "4", "5"],
    "07.10.2023 değişikliğiyle m. 7'ye eklenen fıkraya göre VUK 153/A kapsamında terkin edilen mükelleflerin fiillerine "
    "iştiraki kesinleşen meslek mensubuna üç yıl süreyle alıkoyma cezası uygulanır. Bu süre, genel alıkoyma "
    "cezasındaki altı ay–bir yıl sınırının istisnasıdır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 48/4; Disiplin Yönetmeliği m. 7/a",
    f"{K}, görevini bağımsızlık, tarafsızlık ve dürüstlükle yapmayan veya Kanun'da yer alan mesleğin genel "
    "prensiplerine aykırı harekette bulunan meslek mensuplarına hangi disiplin cezası uygulanır?",
    "Geçici olarak mesleki faaliyetten alıkoyma",
    ["Kınama", "Uyarma", "Meslekten çıkarma", "Yeminli sıfatını kaldırma"],
    "Kanun m. 48'e göre görevini bağımsızlık, tarafsızlık ve dürüstlükle yapmayan veya mesleğin genel prensiplerine "
    "aykırı davranan meslek mensupları için geçici olarak mesleki faaliyetten alıkoyma cezası uygulanır.")

P.q("3568 s. Kanun m. 48/5; Disiplin Yönetmeliği m. 7/g ve 8",
    f"{K}, tasdik yetkisini gerçeğe aykırı olarak kullandığı Hazine ve Maliye Bakanlığınca ilk defa tespit edilip "
    "rapora bağlanan yeminli mali müşavir hakkında hangi ceza verilir?",
    "Geçici olarak mesleki faaliyetten alıkoyma",
    ["Yeminli sıfatını kaldırma", "Meslekten çıkarma", "Kınama", "Uyarma"],
    "Kanun m. 48'e göre tasdik yetkisinin gerçeğe aykırı kullanıldığının ilk tespitinde alıkoyma cezası verilir. "
    "Bu durum tekerrür eder ve mahkeme kararıyla kesinleşirse yeminli sıfatını kaldırma cezası uygulanır.")

# ---------------------------------------------------------------- çıkarma
P.q("3568 s. Kanun m. 48; Disiplin Yönetmeliği m. 9",
    f"{K} ve Disiplin Yönetmeliği'ne göre aşağıdakilerden hangisi meslekten çıkarma cezasını gerektiren haller arasında yer almaz?",
    "Üç yıllık dönem içinde üçüncü kez kınama cezası gerektiren eylemin yinelenmesi",
    ["Başka meslek mensubunun ad ve unvanı kullanılarak beyanname imzalanması",
     "Mükellefle birlikte kasten vergi ziyaına sebebiyet verildiğinin mahkeme kararıyla kesinleşmesi",
     "Meslek ruhsatnamesinin bir başkasına kiraya verilmesi",
     "Beş yılda iki alıkoyma cezasından sonra aynı fiilin yeniden işlenmesi"],
    "Üç yıllık dönemde üçüncü kez kınama cezası gerektiren eylem m. 7/a'ya göre geçici olarak mesleki faaliyetten "
    "alıkoyma sebebidir. Diğerleri Kanun m. 48 ve Yönetmelik m. 9'da meslekten çıkarma halleridir.",
    zorluk="hard")

P.sayisal("3568 s. Kanun m. 48; Disiplin Yönetmeliği m. 9/a",
    f"{DY}, kaç yıllık dönem içinde iki defa mesleki faaliyetten alıkoyma cezası ile cezalandırıldıktan sonra bu cezayı "
    "gerektiren eylemi yeniden işleyen meslek mensubuna meslekten çıkarma cezası uygulanır?",
    "5", ["2", "3", "4", "10"],
    "Kanun m. 48 ve Yönetmelik m. 9/a'ya göre beş yıllık dönemde iki alıkoyma cezasından sonra aynı cezayı gerektiren "
    "eylemin yeniden işlenmesi meslekten çıkarma sebebidir. Uyarma ve kınama yinelemesinde dönem üç yıldır.")

P.q("3568 s. Kanun m. 48 (7546 s. Kanunla eklenen fıkra); Disiplin Yönetmeliği m. 9/d",
    "Serbest muhasebeci mali müşavir (C), mesleğini bizzat yapmayıp kaşesini ve e-beyanname yetkisini, meslek mensubu "
    f"olmayan kardeşinin kullanmasına bedelsiz olarak izin vermiştir. {K} (C)'ye uygulanacak ceza aşağıdakilerden hangisidir?",
    "Meslekten çıkarma",
    ["Kınama", "Uyarma", "Geçici olarak mesleki faaliyetten alıkoyma", "Üç yıl süreyle mesleki faaliyetten alıkoyma"],
    "27.03.2025 tarihli 7546 sayılı Kanunla m. 48'e eklenen fıkraya göre meslek ruhsatnamesini bir başkasına bedelli "
    "veya bedelsiz kullandıranlara meslekten çıkarma cezası verilir. Yönetmelik m. 9/d de yetkilerin meslek mensubu "
    "olmayan kişilere kullandırılmasını meslekten çıkarma hâli sayar.")

# ---------------------------------------------------------------- takdir, tekerrür, aday
P.q("Disiplin Yönetmeliği m. 11",
    f"{DY}, disiplin kurullarının takdir hakkı ve tekerrüre ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Disiplin kurulları uyarma cezasını bir derece hafif ceza takdiri yoluyla ortadan kaldırabilir.",
    ["Disiplin kurulları gerekçesini kararda belirterek bir derece ağır veya bir derece hafif ceza uygulayabilir.",
     "Üç yıl içinde aynı cezayı gerektiren yeni eylemde daha ağır ceza uygulanabilir.",
     "Tekerrür için ilk iki cezanın kesinleşip ilgiliye bildirilmiş olması gerekir.",
     "Takdir hakkı kullanıldığında bunun gerekçesine kararda ayrıca yer verilir."],
    "M. 11'e göre uyarma cezası, bir derece hafif ceza takdiri suretiyle ortadan kaldırılamaz. Diğer ifadeler "
    "m. 11 ve m. 27'deki düzenlemelerle uyumludur.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 12/2",
    f"{DY}, aşağıdaki disiplin cezalarından hangisi Hazine ve Maliye Bakanlığı ile diğer ilgili kurum ve kuruluşlara duyurulmaz?",
    "Kınama",
    ["Geçici olarak mesleki faaliyetten alıkoyma", "Yeminli sıfatını kaldırma", "Meslekten çıkarma",
     "Üç yıl süreyle mesleki faaliyetten alıkoyma"],
    "M. 12'ye göre uyarma ve kınama cezaları hariç diğer disiplin cezaları Hazine ve Maliye Bakanlığı ile ilgili "
    "kurum ve kuruluşlara duyurulur. Kınama bu nedenle duyurulmaz.",
    zorluk="easy")

P.oncul("Disiplin Yönetmeliği m. 12/2 (14.01.2026 değişikliği işlenmiş)",
    "Disiplin Yönetmeliği’nde yer alan cezalardan bazıları aşağıda sıralanmıştır:",
    ["Kınama", "Geçici olarak mesleki faaliyetten alıkoyma", "Yeminli sıfatını kaldırma", "Meslekten çıkarma"],
    f"{DY}, yukarıdaki cezalardan hangileri Resmî Gazete’de ilan olunur?",
    "II, III ve IV",
    ["Yalnız IV", "I ve II", "II ve IV", "III ve IV", "II, III ve IV"],
    "M. 12/2'ye göre geçici olarak mesleki faaliyetten alıkoyma, meslekten çıkarma ve yeminli sıfatının kaldırılması "
    "cezaları Resmî Gazete’de ilan olunur. Uyarma ve kınama cezaları ilan edilmez ve Bakanlığa da duyurulmaz.")

P.sayisal("Disiplin Yönetmeliği m. 12/1",
    f"{DY}, oda disiplin kurulu kararlarının birer onaylı örneği karar tarihinden itibaren kaç gün içinde Birlik "
    "Disiplin Kurulu Başkanlığına gönderilir?",
    "30", ["10", "15", "45", "60"],
    "M. 12/1'e göre disiplin cezalarını ilgili oda yönetim kurulu başkanlığı uygular; oda disiplin kurulu kararlarının "
    "onaylı örnekleri karar tarihinden itibaren 30 gün içinde Birlik Disiplin Kurulu Başkanlığına gönderilir.")

P.q("3568 s. Kanun m. 48 son fıkra; Disiplin Yönetmeliği m. 12/3",
    f"{DY}, disiplin cezalarının uygulanmasına hangi tarihten itibaren başlanır?",
    "Kesinleşme yazısının oda tarafından tebliğ edildiği tarihi izleyen birinci günden",
    ["Oda disiplin kurulunun karar tarihini izleyen birinci günden",
     "Oda disiplin kurulu kararının Birlik Disiplin Kurulu Başkanlığına gönderildiği tarihten",
     "Kararın Resmî Gazete’de ilan edildiği tarihi izleyen ay başından",
     "İtiraz süresinin bittiği tarihi izleyen otuzuncu günden"],
    "M. 12/3'e göre uygulama, cezanın kesinleştiğine ilişkin yazının oda tarafından meslek mensubuna tebliğ edildiği "
    "tarihi izleyen birinci günden başlar. Kanun m. 48'in 7546 sayılı Kanunla değişen son fıkrası da cezaların "
    "kesinleştiğinin bildirilmesinden sonra uygulanacağını hükme bağlar.",
    zorluk="hard")

P.sayisal("Disiplin Yönetmeliği m. 12/5",
    "Geçici olarak mesleki faaliyetten alıkoyma cezası alan bir meslek mensubu elindeki işleri, cezanın kesinleşme "
    f"tarihinden itibaren kaç gün içinde bağlı bulunduğu odaya teslim eder? ({DY.replace(' göre', '')})",
    "60", ["15", "30", "45", "90"],
    "M. 12'ye göre alıkoyma, meslekten çıkarma veya yeminli sıfatının kaldırılması cezasını alan meslek mensubu "
    "elindeki işleri kesinleşme tarihinden itibaren 60 gün içinde odaya teslim eder; oda işleri iş sahiplerine geri "
    "verir veya iş sahibinin isteğiyle görevlendirilen meslek mensubuna teslim eder.")

P.q("Disiplin Yönetmeliği m. 12/3",
    "Geçici olarak mesleki faaliyetten alıkoyma cezası kesinleşen serbest muhasebeci mali müşavire oda tarafından "
    f"gönderilecek kesinleşme yazısında, {DY.replace('’ne göre', '’ne göre bulunması gereken hususlara ilişkin')} aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ruhsat ve kaşenin cezanın sona ereceği tarihte odaya teslim edileceği belirtilir.",
    ["Yazının tebliğinden itibaren yeni iş kabul edilemeyeceği belirtilir.",
     "Mevcut işlerin 60 gün içinde tasfiye edilmesi gerektiği belirtilir.",
     "E-beyanname şifresinin tebliğ ayını izleyen ay sonunda iptal edileceği belirtilir.",
     "Zorunluluklara uyulmazsa suç duyurusunda bulunulacağı belirtilir."],
    "M. 12'ye göre SMMM'ye gönderilen kesinleşme yazısında ruhsat ve kaşenin, e-beyanname şifresinin iptal edildiği "
    "süre içinde, yani tebliğ ayını izleyen ay sonuna kadar odaya teslim edilmesi gerektiği belirtilir; cezanın sona "
    "ereceği tarih beklenmez.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 13",
    f"{DY}, meslekten çıkarılan veya geçici olarak mesleki faaliyetten alıkonulan meslek mensubunun bu yasakların gereğini "
    "yerine getirmemesi hâlinde odalar veya Birlik tarafından ne yapılır?",
    "Cumhuriyet Savcılığına suç duyurusunda bulunulur.",
    ["Meslek mensubuna ek olarak kınama cezası verilir.",
     "Birlik Genel Kurulunca meslek mensubunun sicili kapatılır.",
     "Meslek mensubunun oda üyeliği bir yıl süreyle askıya alınır.",
     "Meslek mensubu hakkında idari para cezası uygulanması istenir."],
    "M. 13'e göre meslekten çıkarılanlar, yeminli sıfatı kaldırılanlar ve alıkonulanlar yasakların gereğini derhal "
    "yerine getirir; getirmeyenler hakkında odalar veya Birlik Cumhuriyet Savcılığına suç duyurusunda bulunur.")

# ---------------------------------------------------------------- soruşturma
P.q("Disiplin Yönetmeliği m. 3",
    f"{DY}, “disiplin kovuşturması” aşağıdakilerden hangisini ifade eder?",
    "Dosyanın disiplin kuruluna intikalinden, disiplin kurulu kararının kesinleşmesine kadar olan aşamayı",
    ["İhbar veya şikâyet dilekçesinin odaya intikalinden, dosyanın disiplin kuruluna sevkine kadar olan aşamayı",
     "Oda yönetim kurulunun soruşturma kararından, soruşturma raporunun teslimine kadar olan aşamayı",
     "Disiplin kurulu kararının verilmesinden, cezanın Resmî Gazete’de ilanına kadar olan aşamayı",
     "İtirazın Birlik Disiplin Kuruluna ulaşmasından, idari yargı kararına kadar olan aşamayı"],
    "M. 3'e göre disiplin soruşturması, ihbar/şikâyetin odaya intikalinden dosyanın disiplin kuruluna sevkine kadar; "
    "disiplin kovuşturması ise dosyanın disiplin kuruluna intikalinden kararın kesinleşmesine kadar olan aşamadır.")

P.q("Disiplin Yönetmeliği m. 14/1",
    "Serbest muhasebeci mali müşavir (D) hakkında şikâyet, Ankara'da kayıtlı olduğu dönemde işlediği iddia edilen bir "
    "eylem için yapılmıştır; ancak şikâyet sabit olduğunda (D) İzmir odasının çalışanlar listesine kayıtlıdır. "
    f"{DY}, disiplin soruşturmasına karar verme ve yürütme yetkisi hangi merciye aittir?",
    "İzmir odasına",
    ["Ankara odasına", "Eylemin işlendiği yerdeki vergi dairesine", "Birlik Yönetim Kuruluna", "Birlik Disiplin Kuruluna"],
    "M. 14'e göre yetki, şikâyetin sabit olduğu, savcılık isteminin yapıldığı veya eylemin resen haber alındığı tarihte "
    "meslek mensubunun hangi odanın çalışanlar listesinde veya meslek kütüğünde kayıtlı olduğuna göre belirlenir.")

P.q("Disiplin Yönetmeliği m. 14/2",
    f"{DY}, disiplin soruşturmasında zamanaşımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zamanaşımı, oda yönetim kurulunun soruşturma açılmasına karar verdiği tarihten itibaren durur.",
    ["Eylemin işlenmesinden itibaren beş yıl geçmiş ise soruşturma yapılamaz.",
     "Şikâyet dilekçesinin oda kayıtlarına girdiği tarihten itibaren zamanaşımı durur.",
     "Eylem aynı zamanda suç oluşturuyor ve Kanun daha uzun bir zamanaşımı öngörüyorsa o süre uygulanır.",
     "Meslek mensubunun ölümü hâlinde soruşturma açılmaz, açılmış olan düşer."],
    "M. 14'e göre zamanaşımı, şikâyet dilekçesinin oda kayıtlarına girdiği tarihten itibaren durur; yönetim kurulu "
    "kararı beklenmez. Beş yıllık süre, suçlarda daha uzun sürenin uygulanması ve ölüm hâli aynı maddede düzenlenir.",
    zorluk="hard")

P.sayisal("Disiplin Yönetmeliği m. 14/2",
    f"{DY}, disiplin cezasını gerektiren eylemin işlenmesinden itibaren kaç yıl geçmiş ise, eylem ayrıca daha uzun "
    "zamanaşımına bağlı bir suç oluşturmadıkça soruşturma yapılamaz?",
    "5", ["1", "2", "3", "10"],
    "M. 14/2'ye göre eylemin işlenmesinden itibaren beş yıl geçmişse soruşturma yapılamaz. Şikâyetin oda kayıtlarına "
    "girmesiyle süre durur; eylem aynı zamanda daha uzun zamanaşımı öngörülen bir suçsa o süre uygulanır.")

P.q("Disiplin Yönetmeliği m. 15",
    f"{DY}, aşağıdakilerden hangisi meslek mensubu hakkında disiplin soruşturması yapılmasına dayanak olabilecek başvuru veya istemler arasında sayılmamıştır?",
    "Meslek mensubunun müşterisinin vergi dairesinden aldığı ceza ihbarnamesi",
    ["İlgilinin ihbar veya şikâyeti",
     "Birlik kurullarından birinin kurul kararına dayanan isteği",
     "Hazine ve Maliye Bakanlığının rapora dayanan isteği",
     "Hükümlülükle sonuçlanan ceza davasının odaya ulaşması"],
    "M. 15 disiplin soruşturmasını ihbar veya şikâyet, oda veya Birlik kurullarının isteği, Bakanlığın veya diğer kamu "
    "kurumlarının isteği ve hükümlülükle sonuçlanan ceza davasının odaya ulaşmasına bağlar. Müşteriye kesilen vergi "
    "cezası kendiliğinden bir soruşturma sebebi olarak sayılmamıştır.")

P.q("Disiplin Yönetmeliği m. 16 (14.01.2026 değişikliği)",
    f"{DY}, oda yönetim ve denetleme kurulu başkan ve üyeleri hakkında bu görevleriyle ilgili yapılan şikâyetlere ilişkin "
    "aşağıdaki ifadelerden hangisi doğrudur?",
    "Şikâyetin oda genel kuruluna sunulması gerekip gerekmediğini Birlik Yönetim Kurulu inceler.",
    ["Şikâyeti doğrudan ilgili odanın disiplin kurulu inceler ve karara bağlar.",
     "Şikâyetin oda genel kuruluna sunulup sunulmayacağına Birlik Disiplin Kurulu karar verir.",
     "Şikâyet, oda yönetim kurulunca soruşturmacı atanarak altı ay içinde sonuçlandırılır.",
     "Birlik Yönetim Kurulunun şikâyeti sunmama kararına karşı Birlik Disiplin Kuruluna itiraz edilir."],
    "14.01.2026'da değişen m. 16'ya göre bu şikâyetler, oda genel kuruluna sunulmasının gerekip gerekmediği yönünden "
    "Birlik Yönetim Kurulunca incelenir; aksi yöndeki kararlar kesindir. Genel kurul soruşturmaya karar verirse "
    "odanın disiplin kurulu karar verir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 17",
    f"{DY}, ihbar ve şikâyete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kimliği ve adresi bulunmayan yazılı şikâyetler oda yönetim kurulunca disiplin kuruluna gönderilir.",
    ["İhbar veya şikâyet sözlü ya da yazılı olarak yapılabilir.",
     "Sözlü şikâyet, kurul başkanı veya üyesi ile şikâyetçinin imzaladığı tutanağa geçirilir.",
     "Birlik kurullarına yapılan sözlü veya yazılı şikâyetler gerekli görülürse 30 gün içinde ilgili odaya gönderilir.",
     "Oda yönetim kurulu gerek gördüğünde şikâyet konusunu resen soruşturabilir."],
    "M. 17'ye göre ihbarda bulunanın kimliği, adresi ve imzası bulunmayan ihbar ve şikâyetler işleme konulmaz. Oda "
    "yönetim kurulu gerek gördüğünde konuyu kendiliğinden soruşturabilir; ancak kimliksiz dilekçe disiplin kuruluna "
    "sevk edilmez.")

P.sayisal("Disiplin Yönetmeliği m. 18/1",
    f"{DY}, ilgili oda yönetim kurulu ivedi durumlar hariç ihbar, şikâyet veya istem konusunu bildirilmesinden itibaren "
    "en geç kaç ay içinde incelemek zorundadır?",
    "2", ["1", "3", "4", "6"],
    "M. 18'e göre oda yönetim kurulu, ivedi durumlar hariç, ihbar, şikâyet veya istem konusunu bildirilmesinden "
    "itibaren en geç iki ay içinde inceler. Soruşturmanın sonuçlandırılma süresi ise m. 19'a göre altı aydır.")

P.q("Disiplin Yönetmeliği m. 18/2",
    "Oda yönetim kurulu, meslek mevzuatından kaynaklanmayan bir şikâyet hakkında gerekçe göstererek soruşturma "
    f"açılmasına yer olmadığına karar vermiştir. {DY}, başvuru sahibinin bu karara karşı başvuru yolu aşağıdakilerden hangisidir?",
    "Tebliğ tarihinden itibaren 30 gün içinde Birlik Disiplin Kuruluna itiraz",
    ["Tebliğ tarihinden itibaren 15 gün içinde oda disiplin kuruluna itiraz",
     "Karar tarihinden itibaren 30 gün içinde oda genel kuruluna itiraz",
     "Tebliğ tarihinden itibaren 60 gün içinde doğrudan idari yargıya dava",
     "Tebliğ tarihinden itibaren 30 gün içinde Birlik Yönetim Kuruluna itiraz"],
    "M. 18/2'ye göre soruşturma açılmasına yer olmadığı kararı derhal başvuru sahibine bildirilir; başvuru sahibi "
    "tebliğden itibaren 30 gün içinde Birlik Disiplin Kuruluna itiraz edebilir.")

P.q("Disiplin Yönetmeliği m. 19",
    f"{DY}, disiplin soruşturmasının yürütülmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hakkında soruşturma yapılan meslek mensubundan bilgi almak için verilecek süre 7 günden az olamaz.",
    ["Soruşturma, yönetim kurulunun kendi üyeleri arasından görevlendireceği bir veya daha fazla üyece yürütülebilir.",
     "Haksız rekabet şikâyetlerinde soruşturma görevi Haksız Rekabetle Mücadele Kuruluna verilebilir.",
     "Yönetim kurulu soruşturmayı ihbar, şikâyet veya istek tarihinden itibaren en geç altı ayda sonuçlandırır.",
     "Yönetim kurulu üyeleri kendileri hakkındaki soruşturmaya ilişkin görüşme ve kararlara katılamaz."],
    "M. 19'a göre meslek mensubundan bilgi almak için verilecek süre 15 günden az olamaz. Soruşturmacı görevlendirme, "
    "Haksız Rekabetle Mücadele Kurulu, altı aylık süre ve üyelerin kendi dosyalarına katılamaması aynı maddededir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 20",
    f"{DY}, oda yönetim kurulunun disiplin kovuşturması açılmasına yer olmadığına ilişkin kararı, soruşturma geçiren "
    "meslek mensubuna ve varsa şikâyetçiye karar tarihinden itibaren en geç ne kadar süre içinde yazılı olarak bildirilir?",
    "3 ay", ["15 gün", "30 gün", "2 ay", "6 ay"],
    "M. 20/3'e göre kovuşturmaya yer olmadığı kararı, soruşturma sonucu verilecek karar tarihinden itibaren en geç "
    "3 ay içinde yazılı olarak bildirilir. Kovuşturma açılması kararı ise kesindir ve dosya disiplin kuruluna gönderilir.")

P.q("Disiplin Yönetmeliği m. 20/4 ve 21",
    f"{DY}, oda yönetim kurulunun soruşturma sonunda verdiği kararlara ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Disiplin kovuşturması açılması kararı kesindir ve dosya oda disiplin kuruluna gönderilir.",
    ["Disiplin kovuşturması açılması kararına karşı meslek mensubu 30 gün içinde Birlik Disiplin Kuruluna itiraz eder.",
     "Kovuşturmaya yer olmadığı kararına karşı soruşturma geçiren meslek mensubu itiraz eder, şikâyetçi itiraz edemez.",
     "Kovuşturmaya yer olmadığı kararına karşı itiraz, Birlik Genel Kurulunda görüşülerek karara bağlanır.",
     "Birlik Disiplin Kurulunun itirazı kabul eden kararına karşı oda yönetim kurulu idari yargıya başvurur."],
    "M. 20'ye göre kovuşturma açılması kararı kesindir. Kovuşturmaya yer olmadığı kararına karşı m. 21 uyarınca "
    "şikâyetçi, ihbarcı veya istemde bulunan 30 gün içinde Birlik Disiplin Kuruluna itiraz edebilir; Birlik Disiplin "
    "Kurulunun bu kararları kesindir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 22",
    f"{DY}, aşağıdakilerden hangisi meslek mensubu hakkında disiplin kovuşturması yapılmasının dayanakları arasında yer almaz?",
    "Şikâyetçinin doğrudan oda disiplin kuruluna verdiği dilekçe",
    ["Oda yönetim kurulunun kovuşturma açılması kararı",
     "İtiraz üzerine Birlik Disiplin Kurulunun kovuşturma açılması kararı",
     "Sorumlu kurul üyeleri hakkında oda genel kurulu kararı",
     "Sorumlu kurul üyeleri hakkında Birlik Genel Kurulu kararı"],
    "M. 22'ye göre kovuşturma; oda yönetim kurulunun kovuşturma kararı, itiraz üzerine Birlik Disiplin Kurulunun "
    "kararı veya kurul üyeleri hakkında oda ya da Birlik genel kurulunun kararı üzerine yapılır. Şikâyetçi disiplin "
    "kuruluna doğrudan başvurarak kovuşturma başlatamaz.")

# ---------------------------------------------------------------- kovuşturma, savunma
P.q("3568 s. Kanun m. 48; Disiplin Yönetmeliği m. 23",
    f"Savunma süresine ilişkin olarak {K.replace('’na göre', '’nda')} ve Disiplin Yönetmeliği’nde öngörülen asgari süreler "
    "aşağıdakilerin hangisinde sırasıyla doğru verilmiştir?",
    "10 gün / 15 gün",
    ["7 gün / 10 gün", "10 gün / 10 gün", "15 gün / 15 gün", "15 gün / 30 gün"],
    "Kanun m. 48'e göre yetkili disiplin kurulunun vereceği savunma süresi 10 günden az olamaz; Yönetmelik m. 23 bu "
    "süreyi 15 günden az olmamak üzere belirler. Yönetmelik Kanundaki asgariyi aşan bir güvence getirmiştir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 23",
    f"{DY}, disiplin kovuşturmasında savunma hakkına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Savunma hakkını kullanmayan meslek mensubu hakkında bu nedenle ayrıca disiplin kovuşturması açılır.",
    ["Savunması alınmadan meslek mensubuna disiplin cezası verilemez.",
     "Verilen süre içinde savunma yapmayan savunma hakkından vazgeçmiş sayılır.",
     "Mali tatil dönemi içinde savunma istenemez ve duruşma yapılamaz.",
     "Savunma süresi geçmiş olsa da karar verilmeden önce sunulan savunma ve deliller süresinde verilmiş sayılır."],
    "M. 23'e göre meslek mensubu, savunma hakkını kullanmaması veya istenen bilgi ve belgeleri vermemesi nedeniyle "
    "ayrıca disiplin kovuşturmasına tabi tutulamaz. Diğer ifadeler aynı maddede yer alır.")

P.q("Disiplin Yönetmeliği m. 23",
    f"{DY}, disiplin kovuşturmasında duruşmaya ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Duruşma gün ve saati en az 15 gün önce ilgiliye bildirilir ve duruşma gizli olur.",
    ["Duruşma gün ve saati en az 7 gün önce ilgiliye bildirilir ve duruşma açık yapılır.",
     "Duruşma gün ve saati en az 30 gün önce ilgiliye bildirilir ve duruşma açık yapılır.",
     "Duruşma gün ve saati en az 10 gün önce ilgiliye bildirilir ve duruşma gizli olur.",
     "Duruşma gün ve saati en az 15 gün önce ilgiliye bildirilir ve duruşma açık yapılır."],
    "M. 23'e göre inceleme kural olarak evrak üzerinde yapılır; meslek mensubunun istemi veya kurulun uygun görmesiyle "
    "duruşmalı yapılır. Duruşma gün ve saati en az 15 gün önce bildirilir ve duruşma gizli olur.")

P.sayisal("Disiplin Yönetmeliği m. 23",
    f"{DY}, oda disiplin kurulu, ceza davasının sonucunun beklenmesini gerektiren haller saklı kalmak üzere, incelemeyi "
    "yönetim kurulu kararından itibaren en geç kaç ay içinde sonuçlandırmak zorundadır?",
    "12", ["3", "6", "9", "18"],
    "M. 23'e göre oda disiplin kurulu incelemeyi ivedilikle ve her hâlde yönetim kurulu kararından itibaren en geç bir "
    "yıl (12 ay) içinde sonuçlandırır. Ceza davasının beklenmesi gereken durumlar saklıdır.")

P.q("Disiplin Yönetmeliği m. 27",
    f"{DY}, disiplin kurulunun verdiği cezalandırma kararında aşağıdakilerden hangisinin gösterilmesi zorunlu değildir?",
    "Şikâyetçinin meslek mensubundan talep ettiği tazminat tutarı",
    ["Disiplin suçu oluşturduğu kanaatine varılan fiil veya hal",
     "Aykırılık teşkil ettiği mevzuat hükmü",
     "Tekerrür varsa önceki kararlar ve tebliğ tarihleri",
     "Takdir hakkı kullanılmışsa bunun gerekçesi"],
    "M. 27'ye göre cezalandırma kararında fiil veya hal, aykırılık oluşturduğu mevzuat, uygulanan madde ve bent, "
    "tekerrür varsa önceki kararlar ve tebliğ tarihleri ile takdir hakkının gerekçesi gösterilir. Tazminat talebi "
    "disiplin kararının unsuru değildir.")

# ---------------------------------------------------------------- itiraz ve kesinleşme
P.q("Disiplin Yönetmeliği m. 28",
    f"{DY}, oda disiplin kurulu kararlarına karşı ilgililerin itiraz süresi ve mercii aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Bildirim tarihinden itibaren 30 gün içinde Birlik Disiplin Kuruluna",
    ["Karar tarihinden itibaren 30 gün içinde Birlik Disiplin Kuruluna",
     "Bildirim tarihinden itibaren 15 gün içinde Birlik Yönetim Kuruluna",
     "Bildirim tarihinden itibaren 60 gün içinde Birlik Disiplin Kuruluna",
     "Karar tarihinden itibaren 45 gün içinde oda genel kuruluna"],
    "M. 28'e göre oda disiplin kurulu kararlarına karşı ilgililer bildirim tarihinden itibaren 30 gün içinde ilgili oda "
    "aracılığıyla veya doğrudan Birlik Disiplin Kuruluna itiraz edebilir.",
    zorluk="easy")

P.q("Disiplin Yönetmeliği m. 28 (14.01.2026 değişikliği)",
    f"{DY}, oda disiplin kurulu kararına posta yoluyla yapılan itirazlarda itiraz tarihi olarak hangi tarih esas alınır?",
    "İtiraz dilekçesinin kurum evrakına girdiği tarih",
    ["İtiraz dilekçesinin postaya verildiği tarih",
     "İtiraz dilekçesinin düzenlendiği tarih",
     "Oda disiplin kurulu kararının tebliğ edildiği tarih",
     "Birlik Disiplin Kurulunun dosyayı incelemeye aldığı tarih"],
    "14.01.2026 tarihli değişiklikle m. 28'e göre posta ile yapılan itirazlarda itiraz dilekçesinin kurum evrakına "
    "girdiği tarih itiraz tarihi kabul edilir. Aynı değişiklikle Birlik itirazları elektronik ortamda almaya da "
    "yetkilendirilmiştir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 29",
    f"{DY}, disiplin kararlarının kesinleşmesine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Birlik Disiplin Kurulunun itirazların reddine ilişkin kararları Hazine ve Maliye Bakanlığının onayı ile kesinleşir.",
    ["Otuz gün içinde itiraz edilmeyen oda disiplin kurulu kararları Birlik Yönetim Kurulunun onayı ile kesinleşir.",
     "Birlik Disiplin Kurulunun itirazların reddine ilişkin kararları Birlik Genel Kurulunun onayı ile kesinleşir ve ilan edilir.",
     "Birlik Disiplin Kurulunun kararlarına karşı ilgililer Danıştay'a temyiz yoluyla başvurur.",
     "Süresinde itiraz edilen dosyalarda oda disiplin kurulunun kararı Birlik kararından önce kesinleşir."],
    "M. 29'a göre süresinde itiraz edilmeyen oda disiplin kurulu kararları itiraz süresinin geçmesiyle kesinleşir; "
    "itiraz edilen dosyalarda Birlik Disiplin Kurulu kararları kesindir. Ancak itirazların reddine ilişkin kararlar "
    "Hazine ve Maliye Bakanlığının onayıyla kesinleşir ve bunlara karşı idari yargıya başvurulabilir.",
    zorluk="hard")

P.oncul("Disiplin Yönetmeliği m. 30 (14.01.2026 değişikliği)",
    "Meslek mensubu hakkında disiplin işlemine konu eylemden dolayı ceza mahkemesinde dava açılmıştır.",
    ["Başlamış olan ceza kovuşturması disiplin işlem ve kararlarının uygulanmasına engel oluşturmaz.",
     "Disiplin kovuşturması ceza davasının sonuna kadar bekletilebilir.",
     "Disiplin kovuşturması bekletiliyorsa disiplin kurulunun karar verme süresi dava sonucu kurula ulaşana kadar durur.",
     "Tedbir niteliğinde alıkoyma kararlarına karşı Birlik Genel Kuruluna itiraz edilir."],
    f"{DY}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III",
    ["Yalnız I", "I ve II", "II ve IV", "I, II ve III", "II, III ve IV"],
    "M. 30'a göre ceza kovuşturması disiplin işlemlerine engel değildir; aynı eylemden dava açılmışsa disiplin "
    "kovuşturması davanın sonuna kadar bekletilebilir ve bu hâlde karar süresi durur. Tedbir niteliğindeki alıkoyma "
    "kararları kesindir; bunlara karşı idari yargıya başvurulur, genel kurula itiraz yolu yoktur.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 30/3",
    f"{DY}, tedbir niteliğinde geçici olarak mesleki faaliyetten alıkoymaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tedbir, ceza davası açılmış eylemler için ve ceza mahkemesinin talebi üzerine uygulanabilir.",
    ["Alıkoyma veya meslekten çıkarma gerektiren eylemler için son karara kadar uygulanabilir.",
     "Oda yönetim kurulunun isteği ve disiplin kurulunun uygun görmesiyle uygulanabilir.",
     "Ceza soruşturması sırasında savcılık talebiyle oda disiplin kurulu kararıyla uygulanabilir.",
     "Tedbir uygulanan dosyalar yönetim ve disiplin kurullarınca öncelikle incelenir."],
    "M. 30'a göre tedbir, fiil ceza davasına konu olsun olmasın alıkoyma veya meslekten çıkarma gerektiren eylemlerde "
    "uygulanabilir; oda yönetim kurulunun isteği, disiplin kurulunun kendi görmesi veya savcılık talebi dayanak "
    "olabilir. 2026 değişikliğiyle tedbirli dosyalara öncelik verilir.",
    zorluk="hard")

P.q("Disiplin Yönetmeliği m. 31 ve 32",
    f"{DY}, aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kovuşturmaya yer olmadığı kararı verilen eylem, yeni kanıt gerekmeksizin disiplin kurulunca yeniden incelenebilir.",
    ["Disiplin kurulu üyeleri Ceza Muhakemesi Kanunu’nda yazılı sebeplerle reddedilebilir.",
     "Ret istemi, reddi istenen üye dışındaki disiplin kurulu üyelerinin toplanması suretiyle incelenip karara bağlanır.",
     "Ret veya çekilme nedeniyle kurul toplanamazsa yetkili disiplin kurulunu Birlik belirler.",
     "Reddedilen veya çekilen üyelerin yerine yedek üyeler kurula katılır."],
    "M. 31'e göre kovuşturmaya yer olmadığı kararının konusu olan eylem için yeniden inceleme yapılabilmesi yeni "
    "kanıtların elde edilmesine bağlıdır. Ret ve çekilmeye ilişkin diğer ifadeler m. 32'de düzenlenmiştir.")

# ---------------------------------------------------------------- bildirim (2026)
P.q("Disiplin Yönetmeliği m. 34/2 (14.01.2026 değişikliği)",
    "Meslek mensubunun odaya bildirdiği adresi değiştiği için disiplin işlemine ilişkin bildirim yapılamamıştır. "
    f"{DY}, izlenecek usule ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Duyuru ilan tahtasında 15 iş günü süreyle asılı kalır.",
    ["Oda, e-Birlik yazılımı aracılığıyla bildirim gönderir.",
     "Kayıtlı cep telefonuna eş zamanlı kısa mesaj gönderilir.",
     "E-Birlik işlemini izleyen 7 gün içinde ilan tahtasına duyuru asılır.",
     "İlanın indirilmesinden itibaren 5 gün içinde başvurulmazsa bildirim yapılmış sayılır."],
    "M. 34/2'ye göre e-Birlik bildirimi ve eş zamanlı kısa mesajın ardından 7 gün içinde odanın ilan tahtasına "
    "duyuru asılır ve 5 iş günü süreyle ilan edilir; ilgili, ilanın indirilmesinden itibaren 5 gün içinde başvurmazsa "
    "bildirim yapılmış sayılır.",
    zorluk="hard")

P.sayisal("Disiplin Yönetmeliği m. 34 son fıkra (14.01.2026 değişikliği)",
    f"{DY}, bir meslek mensubu hakkında aynı yıl içinde kaçtan fazla disiplin soruşturması açılmış ise o meslek "
    "mensubuna yapılacak tüm tebligatlar e-Birlik ve ilan tahtası usulüyle yapılır?",
    "5", ["2", "3", "4", "10"],
    "14.01.2026 değişikliğiyle m. 34'e göre aynı yıl içinde beşten fazla disiplin soruşturması bulunan meslek "
    "mensubuna yapılacak tüm tebligatlar ikinci fıkradaki e-Birlik ve ilan usulüyle yapılır.")

# ---------------------------------------------------------------- Kanun: sır, ceza
P.q("3568 s. Kanun m. 43",
    f"{K}, meslek sırlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Meslek mensupları, çeşitli kanunlarla muhbirlere tanınan hak ve menfaatlerden yararlanabilir.",
    ["Meslek mensupları ve yanlarında çalışanlar işleri dolayısıyla öğrendikleri sırları ifşa edemez.",
     "Suç oluşturan hâllerin yetkili mercilere duyurulması mecburidir.",
     "Adli veya idari inceleme ve soruşturmalar sır saklama hükmünün dışındadır.",
     "Tanıklık sırrın ifşası sayılmaz ve bu hükümler oda personelini de kapsar."],
    "Kanun m. 43'e göre meslek mensupları muhbirlere tanınan hak ve menfaatlerden faydalanamaz. Suçun yetkili "
    "mercilere duyurulması zorunluluğu, adli/idari incelemelerin istisna olması ve tanıklığın ifşa sayılmaması aynı "
    "maddededir.")

P.q("3568 s. Kanun m. 47",
    f"{K}, meslek mensuplarının görevleri sırasında veya görevleri sebebiyle işledikleri suçlardan dolayı nasıl cezalandırılacağı aşağıdakilerden hangisinde doğru verilmiştir?",
    "Fiilin niteliğine göre Türk Ceza Kanunu’nun kamu görevlilerine ait hükümleri uyarınca",
    ["Fiilin niteliğine göre Disiplin Yönetmeliği hükümleri uyarınca",
     "Vergi Usul Kanunu’nun kaçakçılık suçlarına ilişkin hükümleri uyarınca",
     "Türk Ceza Kanunu’nun genel hükümleri uyarınca, kamu görevlisi sayılmaksızın",
     "Türk Ticaret Kanunu’nun tacirlerin sorumluluğuna ilişkin hükümleri uyarınca"],
    "Kanun m. 47'ye göre meslek mensupları görevleri sırasında veya görevleri sebebiyle işledikleri suçlardan dolayı "
    "fiillerinin niteliğine göre TCK'nın kamu görevlilerine ait hükümleri uyarınca cezalandırılır.")

P.q("3568 s. Kanun m. 49/1",
    f"{K}, Kanun'un 3. maddesinin birinci fıkrasına aykırı olarak unvan kullanmadan ve ruhsat almadan meslek faaliyetinde "
    "bulunanlar hakkında hangi yaptırım öngörülmüştür?",
    "Altı aydan bir yıla kadar hapis ve adli para cezası",
    ["Yüz güne kadar adli para cezası",
     "Üç aydan altı aya kadar hapis cezası",
     "Bir yıldan üç yıla kadar hapis cezası",
     "İdari para cezası ve işyerinin kapatılması"],
    "Kanun m. 49/1'e göre 3. maddenin birinci fıkrasına aykırı davrananlar hakkında altı aydan bir yıla kadar hapis ve "
    "adli para cezasına hükmolunur. Yüz güne kadar adli para cezası ise m. 49/2'de sayılan diğer aykırılıklar içindir.",
    zorluk="hard")

P.oncul("Disiplin Yönetmeliği m. 5, 6 ve 7",
    "Meslek mensuplarının aşağıdaki eylemleri tespit edilmiştir:",
    ["Mevzuata aykırı tabela kullanmak",
     "Reklam yasağına uymamak",
     "Ücret yönetmeliğine aykırılık nedeniyle ismi ilan edilmiş iş sahibinin işini kabul etmek",
     "Ticari faaliyet yasağına uymamak"],
    f"{DY}, yukarıdaki eylemlerden hangileri kınama cezasını gerektirir?",
    "II ve III",
    ["Yalnız II", "I ve II", "II ve III", "III ve IV", "I, II ve IV"],
    "Reklam yasağına uymamak (m. 6/f) ve Ücret Yönetmeliğine aykırılık nedeniyle ismi ilan edilmiş iş sahibinin işini "
    "kabul etmek (m. 6/h) kınama halleridir. Tabela aykırılığı uyarma (m. 5/e), ticari faaliyet yasağına uymamak "
    "alıkoyma (m. 7/e) cezası gerektirir.",
    zorluk="hard")

P.oncul("Disiplin Yönetmeliği m. 14/3",
    "Disiplin soruşturma ve kovuşturmasında gizliliğe ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Disiplin soruşturma ve kovuşturmasında gizlilik esastır.",
     "Taraflar yazılı dilekçe ile dosyanın bir örneğini talep edebilir.",
     "Taraflar dışında üçüncü kişilere dosya hakkında bilgi verilebilir.",
     "Oda çalışanları görevleri sırasında edindikleri bilgileri yetkili mercilerden başkasına açıklayamaz."],
    f"{DY}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve IV", "I, III ve IV"],
    "M. 14/3'e göre gizlilik esastır; görevliler ve oda çalışanları edindikleri bilgileri yetkili mercilerden başkasına "
    "açıklayamaz; taraflar dışında üçüncü kişilere bilgi verilemez; taraflar yazılı dilekçeyle dosyanın örneğini "
    "isteyebilir.")

P.q("Disiplin Yönetmeliği m. 6/c; 3568 s. Kanun m. 45/2",
    "Yeminli mali müşavir (E), boşanmış olduğu eşinin annesinin ortak olduğu şirketin kurumlar vergisi beyannamesini tasdik "
    f"etmiştir. {DY}, (E)'ye uygulanacak ceza aşağıdakilerden hangisidir?",
    "Kınama",
    ["Uyarma", "Geçici olarak mesleki faaliyetten alıkoyma", "Yeminli sıfatını kaldırma", "Meslekten çıkarma"],
    "Kanun m. 45'e göre YMM'ler eşinin (boşanmış dahi olsa) usul ve füruu ile üçüncü dereceye kadar kan ve sıhri "
    "hısımlarının veya bunların ortak olduğu firmaların işlerine bakamaz. Eski eşin annesi birinci derece sıhri "
    "hısımdır; Yönetmelik m. 6/c bu yasağa aykırılığı kınama hâli sayar.",
    zorluk="hard")


if __name__ == "__main__":
    sys.exit(P.yaz())
