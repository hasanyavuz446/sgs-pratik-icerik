# -*- coding: utf-8 -*-
"""Hukuk · İş Hukuku · Çalışma Süreleri — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında İş Kanunu çalışma süresi soruları haftalık süre, denkleştirme, fazla çalışma sınırı
ve gece çalışması gibi sayı ve süre soran kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 4857 sayılı İş Kanunu md. 41-47, 63-73 (7553 sayılı Kanunla
2025'te md. 46'ya eklenen turizm konaklama tesisi hafta tatili hükmü dahil).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_calisma_sureleri_2026.json", lesson="is_hukuku", topic="calisma_sureleri",
          konu_adi="Çalışma Süreleri", seed=2026093002,
          surum="4857 sayılı İş Kanunu güncel metni (7553 s. Kanun değişikliği dahil); 29.09.2026 kontrolü")

K = "4857 sayılı İş Kanunu’na göre"
K26 = "4857 sayılı İş Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İK md. 63",
    f"{K26}, genel bakımdan haftalık çalışma süresi en çok kaç saattir?",
    "45", ["40", "48", "50", "55"],
    "Md. 63'e göre genel bakımdan çalışma süresi haftada en çok kırk beş saattir; aksi kararlaştırılmamışsa bu süre haftanın "
    "çalışılan günlerine eşit bölünerek uygulanır.", zorluk="easy")

P.q("İK md. 63",
    f"{K26}, yer altı maden işlerinde çalışan işçilerin çalışma süresi aşağıdakilerden hangisidir?",
    "Günde en çok 7,5, haftada en çok 37,5 saat",
    ["Günde en çok 8, haftada en çok 45 saat",
     "Günde en çok 6, haftada en çok 36 saat",
     "Günde en çok 11, haftada ortalama en çok 45 saat",
     "Günde en çok 7, haftada en çok 35 saat"],
    "Md. 63'e göre yer altı maden işlerinde çalışan işçilerin çalışma süresi günde en çok yedi buçuk, haftada en çok otuz yedi "
    "buçuk saattir.")

P.q("İK md. 41",
    f"{K26}, fazla çalışmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fazla çalışma için işçinin onayı aranmaz.",
    ["Gece çalışmasında fazla çalışma yapılamaz.",
     "Yıllık toplam süre 270 saati geçemez.",
     "İşçi zamlı ücret yerine serbest zaman seçebilir.",
     "Serbest zaman ücret kesintisi olmadan kullanılır."],
    "Md. 41'e göre fazla saatlerle çalışmak için işçinin onayının alınması gerekir; gece çalışmasında fazla çalışma yapılamaz "
    "ve yıllık toplam iki yüz yetmiş saati geçemez.", zorluk="easy")

P.sayisal("İK md. 63",
    "Taraflar, haftalık normal çalışma süresini haftanın çalışılan günlerine farklı şekilde dağıtmayı kararlaştırmıştır."
    f"\n\n{K}, bu dağıtımda günlük çalışma süresi en çok kaç saat olabilir?",
    "11", ["8", "9", "10", "12"],
    "Md. 63'e göre tarafların anlaşmasıyla haftalık normal çalışma süresi, günde on bir saati aşmamak koşuluyla günlere farklı "
    "şekilde dağıtılabilir.")

P.q("İK md. 41",
    f"{K}, aşağıdaki işlerden hangisinde fazla çalışma yaptırılamaz?",
    "Md. 69'da belirtilen gece çalışmasında",
    ["Üretimin artırılması amacıyla gündüz işlerinde",
     "Ülkenin genel yararı gereği gündüz işlerinde",
     "Arıza sırasında yapılan acele işlerde",
     "Zorlayıcı sebeplerin ortaya çıkmasında"],
    "Md. 41'e göre md. 63'ün son fıkrasındaki sağlık nedenlerine dayanan kısa veya sınırlı süreli işlerde ve md. 69'daki gece "
    "çalışmasında fazla çalışma yapılamaz.")

P.q("İK md. 41",
    f"{K26}, yer altı maden işlerinde çalışan işçilere fazla çalışma yaptırılmasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Md. 42 ve 43’teki hâller dışında yaptırılamaz.",
    ["İşçinin onayıyla her dönem yaptırılabilir.",
     "Yıllık 270 saate kadar yaptırılabilir.",
     "Toplu iş sözleşmesiyle sınırsız düzenlenir.",
     "Bakanlık izniyle haftada 45 saate kadar yaptırılabilir."],
    "Md. 41'e göre md. 42 ve 43'te sayılan zorunlu nedenler ve olağanüstü hâller dışında yer altında maden işlerinde çalışan "
    "işçilere fazla çalışma yaptırılamaz.", zorluk="hard")

P.sayisal("İK md. 63",
    f"{K}, denkleştirme uygulanan bir işyerinde işçinin haftalık ortalama çalışma süresi, toplu iş sözleşmesiyle "
    "artırılmadıkça kaç aylık süre içinde normal haftalık süreyi aşamaz?",
    "2", ["1", "3", "4", "6"],
    "Md. 63'e göre denkleştirmede iki aylık süre içinde işçinin haftalık ortalama çalışma süresi normal haftalık çalışma "
    "süresini aşamaz; bu süre toplu iş sözleşmeleriyle dört aya kadar artırılabilir.")

P.q("İK md. 42",
    f"{K}, bir arıza sırasında veya zorlayıcı sebeplerin ortaya çıkmasında yaptırılan fazla çalışmaya ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Fazla çalışma yapan işçilere dinlenme verilmez.",
    ["İşçilerin hepsine veya bir kısmına yaptırılabilir.",
     "Normal çalışmayı sağlayacak dereceyi aşamaz.",
     "Zamlı ücret hükümleri bu çalışmalara da uygulanır.",
     "Makineler için acele işlerde de yaptırılabilir."],
    "Md. 42'ye göre zorunlu nedenlerle fazla çalışma yapan işçilere uygun bir dinlenme süresi verilmesi zorunludur; bu "
    "çalışmalar için md. 41'in ücrete ilişkin hükümleri uygulanır.")

P.q("İK md. 43",
    f"{K}, seferberlik sırasında yurt savunmasının gereklerini karşılayan işyerlerinde günlük çalışma süresini işçinin en "
    "çok çalışma gücüne çıkarmaya kim yetkilidir?",
    "Cumhurbaşkanı",
    ["Çalışma ve Sosyal Güvenlik Bakanı", "İşveren", "Mülki amir", "Türkiye Büyük Millet Meclisi Başkanı"],
    "Md. 43'e göre seferberlik sırasında yurt savunmasının gereklerini karşılayan işyerlerinde Cumhurbaşkanı günlük çalışma "
    "süresini işçinin en çok çalışma gücüne çıkarabilir.")

P.sayisal("İK md. 63",
    "Bir otel işletmesi turizm sektöründe faaliyet göstermekte ve toplu iş sözleşmesiyle denkleştirme süresini uzatmak "
    f"istemektedir.\n\n{K}, turizm sektöründe denkleştirme süresi toplu iş sözleşmesiyle en fazla kaç aya kadar "
    "artırılabilir?",
    "6", ["2", "3", "4", "8"],
    "Md. 63'e göre turizm sektöründe dört aylık süre içinde haftalık ortalama süre normal süreyi aşamaz; denkleştirme süresi "
    "toplu iş sözleşmeleriyle altı aya kadar artırılabilir.", zorluk="hard")

P.q("İK md. 44",
    "Bir işyerinde toplu iş sözleşmesi ve iş sözleşmelerinde ulusal bayram ve genel tatil günlerinde çalışılıp "
    f"çalışılmayacağına ilişkin bir hüküm yoktur.\n\n{K}, bu günlerde çalışılması için aşağıdakilerden hangisi gereklidir?",
    "İşçinin onayı",
    ["Bölge müdürlüğünün izni", "Sendikanın onayı", "Valiliğin izni", "İşverenin tek taraflı kararı"],
    "Md. 44'e göre ulusal bayram ve genel tatil günlerinde çalışılıp çalışılmayacağı sözleşmelerle kararlaştırılır; "
    "sözleşmelerde hüküm yoksa bu günlerde çalışılması için işçinin onayı gereklidir.", zorluk="easy")

P.q("İK md. 45",
    f"{K}, aşağıdakilerden hangisine aykırı hükümler toplu iş sözleşmesine veya iş sözleşmesine konulabilir?",
    "İşçiye daha elverişli izin hakları",
    ["Hafta tatiline ilişkin haklar",
     "Ulusal bayram ve genel tatil hakları",
     "Kanunla tanınan ücretli izinler",
     "Yüzde usulüyle çalışanların hakları"],
    "Md. 45'e göre sözleşmelere hafta tatili, bayram ve genel tatil, ücretli izin ve yüzde usulüyle tanınan haklara aykırı "
    "hükümler konulamaz; işçilere daha elverişli hak sağlayan kazanılmış haklar ise saklıdır.", zorluk="hard")

P.sayisal("İK md. 41",
    f"{K26}, fazla çalışma için verilecek ücret, normal çalışma ücretinin saat başına düşen miktarının yüzde kaç "
    "yükseltilmesiyle ödenir?",
    "50", ["10", "25", "75", "100"],
    "Md. 41'e göre her bir saat fazla çalışma için verilecek ücret, normal çalışma ücretinin saat başına düşen miktarının yüzde "
    "elli yükseltilmesiyle ödenir.", zorluk="easy")

P.q("İK md. 46",
    f"{K}, hafta tatili ücretine hak kazanılmasında aşağıdakilerden hangisi çalışılmış gün gibi hesaba katılmaz?",
    "İşçinin mazeretsiz devamsızlık yaptığı gün",
    ["Hekim raporuyla verilen hastalık izni",
     "Kanunen çalışma süresinden sayılan zamanlar",
     "Ek 2. maddede sayılan izin süreleri",
     "Kanundan doğan tatil günleri"],
    "Md. 46'ya göre kanunen çalışma süresinden sayılan zamanlar, kanun veya sözleşmeden doğan tatil günleri, Ek 2. maddedeki "
    "izinler ve bir hafta içinde verilen izinlerle hekim raporlu hastalık izinleri çalışılmış gibi hesaba katılır.")

P.q("İK md. 46",
    f"{K26}, turizm işletmesi belgeli konaklama tesislerindeki hafta tatiline ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Hafta tatili işverenin tek taraflı kararıyla ertelenebilir.",
    ["Erteleme için işçinin yazılı talebi veya onayı aranır.",
     "Tatil, hak kazanılan günü izleyen dört gün içinde kullandırılır.",
     "İşçi onayını otuz gün önceden yazılı bildirimle geri alabilir.",
     "Tatil gününde normal süre kadarlık çalışma fazla çalışmaya katılmaz."],
    "Md. 46'ya 2025'te eklenen hükme göre bu tesislerde hafta tatili ancak işçinin yazılı talebi veya onayıyla dört gün "
    "içinde kullandırılabilir; işveren tek başına erteleyemez.", zorluk="hard")

P.sayisal("İK md. 41",
    "Sözleşmede haftalık çalışma süresi 40 saat olarak belirlenen işçi, denkleştirme uygulanmayan bir haftada 44 saat "
    f"çalışmıştır.\n\n{K26}, 40 saati aşan her bir saat için ücret yüzde kaç yükseltilerek ödenir?",
    "25", ["10", "15", "50", "100"],
    "Md. 41'e göre haftalık süre sözleşmeyle kırk beş saatin altında belirlenmişse, bu süreyi aşan ve kırk beş saate kadar "
    "yapılan çalışmalar fazla sürelerle çalışmadır ve her saat için ücret yüzde yirmi beş yükseltilerek ödenir.")

P.q("İK md. 46",
    f"{K}, zorlayıcı ve ekonomik bir sebep olmadan işveren tarafından haftanın bazı günlerinde çalışma tatil edilirse "
    "çalışılmayan bu günler hakkında aşağıdakilerden hangisi doğrudur?",
    "Hafta tatili için çalışılmış sayılır.",
    ["Hafta tatili ücretini ortadan kaldırır.",
     "İşçinin yıllık izninden düşülür.",
     "Ücretsiz izin olarak kabul edilir.",
     "Telafi çalışmasıyla karşılanması şarttır."],
    "Md. 46'ya göre zorlayıcı ve ekonomik bir sebep olmadan işyerindeki çalışmanın haftanın bazı günlerinde işverence tatil "
    "edilmesi hâlinde bu günler ücretli hafta tatiline hak kazanmak için çalışılmış sayılır.")

P.q("İK md. 47",
    f"{K}, yüzde usulünün uygulandığı işyerlerinde ulusal bayram ve genel tatil ücretleri kim tarafından ödenir?",
    "İşveren",
    ["Yüzde havuzundan müşteri", "İşçi sendikası", "Sosyal Güvenlik Kurumu", "Türkiye İş Kurumu"],
    "Md. 47'ye göre yüzde usulünün uygulandığı işyerlerinde işçilerin ulusal bayram ve genel tatil ücretleri işverence işçiye "
    "ödenir.")

P.sayisal("İK md. 41",
    f"{K26}, fazla çalışma süresinin toplamı bir yılda en çok kaç saat olabilir?",
    "270", ["180", "200", "220", "300"],
    "Md. 41'e göre fazla çalışma süresinin toplamı bir yılda iki yüz yetmiş saatten fazla olamaz.", zorluk="easy")

P.q("İK md. 64",
    f"{K}, telafi çalışmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Telafi çalışması fazla çalışma sayılır.",
    ["Tatil günlerinde telafi çalışması yaptırılamaz.",
     "İşçinin talebiyle verilen izin için de yaptırılabilir.",
     "Günde üç saati aşamaz.",
     "Genel tatil öncesi işyeri tatil edilirse yaptırılabilir."],
    "Md. 64'e göre telafi çalışmaları fazla çalışma veya fazla sürelerle çalışma sayılmaz; günde üç saati aşamaz ve tatil "
    "günlerinde yaptırılamaz.", zorluk="easy")

P.q("İK md. 66",
    f"{K}, aşağıdakilerden hangisi işçinin günlük çalışma süresinden sayılmaz?",
    "Sosyal yardım amacıyla servisle taşınma süresi",
    ["İşverence başka yerde çalışmak üzere yolda geçen süre",
     "Her an iş görmeye hazır bekleyerek geçen süre",
     "Kadın işçinin çocuğuna süt verme süresi",
     "Maden işçisinin kuyuya inip çıkma süresi"],
    "Md. 66'ya göre işin niteliğinden doğmayıp işveren tarafından sırf sosyal yardım amacıyla işyerine götürülüp getirilme "
    "esnasında araçlarda geçen süre çalışma süresinden sayılmaz.")

P.sayisal("İK md. 41",
    f"{K}, fazla çalışma karşılığı zamlı ücret yerine serbest zaman seçen işçi, hak ettiği serbest zamanı kaç ay "
    "içinde kullanır?",
    "6", ["1", "2", "3", "12"],
    "Md. 41'e göre işçi hak ettiği serbest zamanı altı ay zarfında, çalışma süreleri içinde ve ücretinde kesinti olmadan "
    "kullanır.")

P.oncul("İK md. 66",
    f"{K} aşağıdaki süreler değerlendirilmektedir:",
    ["İşçinin işveren evinde asıl işini yapmaksızın geçirdiği süre",
     "Ara dinlenmesi süresi",
     "Uzak yol yapım işinde işçilerin toplu taşınma süresi",
     "İşçinin evinden işyerine kendi imkânıyla gidiş süresi"],
    "Yukarıdakilerden hangileri günlük çalışma süresinden sayılır?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 66'ya göre işverenle ilgili bir yerde asıl işini yapmaksızın geçirilen süre (I) ve uzak yol, köprü gibi işlerde "
    "toplu ve düzenli taşınma süresi (III) çalışma süresinden sayılır; ara dinlenmesi (II) md. 68'e göre sayılmaz.",
    zorluk="hard")

P.q("İK md. 67",
    f"{K}, günlük çalışmanın başlama ve bitiş saatlerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İşin niteliğine göre farklı düzenlenebilir.",
    ["Bütün işçiler için aynı olması şarttır.",
     "Bölge müdürlüğünce belirlenir.",
     "İşçilere duyurulması gerekmez.",
     "Toplu iş sözleşmesiyle belirlenmesi şarttır."],
    "Md. 67'ye göre günlük çalışmanın başlama ve bitiş saatleri ile dinlenme saatleri işçilere duyurulur; işin niteliğine göre "
    "işçiler için farklı şekilde düzenlenebilir.", zorluk="easy")

P.sayisal("İK md. 41",
    "Bir işçi, denkleştirme uygulanmayan bir dönemde toplam 10 saat fazla çalışma yapmış ve zamlı ücret yerine serbest "
    f"zaman kullanmak istemiştir.\n\n{K}, bu işçinin kullanabileceği serbest zaman kaç saattir?",
    "15", ["10", "12", "20", "25"],
    "Md. 41'e göre fazla çalışan işçi isterse fazla çalıştığı her saat karşılığında bir saat otuz dakika serbest zaman "
    "kullanabilir: 10 × 1,5 = 15 saat.")

P.q("İK md. 68",
    f"{K}, ara dinlenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ara dinlenmesi çalışma süresinden sayılır.",
    ["Kanundaki süreler en az sürelerdir.",
     "Kural olarak aralıksız verilir.",
     "Sözleşmeyle aralı kullandırılabilir.",
     "İşçilere değişik saatlerde kullandırılabilir."],
    "Md. 68'e göre ara dinlenmeleri çalışma süresinden sayılmaz; süreler en az olup aralıksız verilir, ancak sözleşmelerle "
    "aralı kullandırılabilir.", zorluk="easy")

P.q("İK md. 69",
    f"{K}, çalışma hayatındaki gece dönemine ilişkin aşağıdakilerden hangisi doğrudur?",
    "En geç 20.00’de başlar, en erken 06.00’da biter.",
    ["En geç 22.00’de başlar, en erken 07.00’de biter.",
     "En geç 18.00’de başlar, en erken 06.00’da biter.",
     "En geç 21.00’de başlar, en erken 05.00’te biter.",
     "En geç 24.00’te başlar, en erken 08.00’de biter."],
    "Md. 69'a göre gece, en geç saat 20.00'de başlayarak en erken saat 06.00'ya kadar geçen ve en fazla on bir saat süren "
    "dönemdir.")

fc = 200 * 1.5 * 6
P.sayisal("İK md. 41",
    "Saat ücreti 200 ₺ olan işçi, haftalık 45 saatlik normal süresinin üzerine, denkleştirme uygulanmayan bir haftada 6 saat "
    f"daha çalışmıştır.\n\n{K26}, bu 6 saat için ödenecek fazla çalışma ücreti kaç ₺’dir?",
    tl(fc), secenekler(fc, 1_200, 1_500, 2_400, 300),
    "Md. 41'e göre kırk beş saati aşan çalışmalar fazla çalışmadır ve her saat için ücret yüzde elli yükseltilerek ödenir: "
    "200 × 1,5 × 6 = 1.800 ₺.")

P.q("İK md. 69",
    f"{K26}, aşağıdaki işlerin hangisinde işçinin yazılı onayı alınsa dahi yedi buçuk saatin üzerinde gece çalışması "
    "yaptırılamaz?",
    "İnşaat işleri",
    ["Turizm işleri", "Özel güvenlik işleri", "Sağlık hizmeti işleri", "Petrol arama ve sondaj işleri"],
    "Md. 69'a göre işçilerin gece çalışmaları yedi buçuk saati geçemez; ancak turizm, özel güvenlik, sağlık hizmeti ve 6491 "
    "sayılı Kanun kapsamındaki petrol arama ve sondaj işlerinde yazılı onayla bu süre aşılabilir.", zorluk="hard")

fs = 240 * 1.25 * 3
P.sayisal("İK md. 41",
    "Saat ücreti 240 ₺ olan işçinin sözleşmesinde haftalık çalışma süresi 40 saattir. İşçi denkleştirme uygulanmayan bir "
    f"haftada 43 saat çalışmıştır.\n\n{K26}, fazladan çalıştığı 3 saat için ödenecek ücret kaç ₺’dir?",
    tl(fs), secenekler(fs, 720, 1_080, 1_440, 180),
    "Md. 41'e göre sözleşmeyle belirlenen haftalık süreyi aşan ve kırk beş saate kadar yapılan çalışmalar fazla sürelerle "
    "çalışmadır; ücret yüzde yirmi beş yükseltilerek ödenir: 240 × 1,25 × 3 = 900 ₺.", zorluk="hard")

P.q("İK md. 69",
    f"{K}, gece ve gündüz işletilen ve nöbetleşe işçi postaları kullanılan işlere ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Gece postasındaki işçi sürekli gece çalıştırılabilir.",
    ["Bir hafta gece çalışan işçi sonraki hafta gündüz çalıştırılır.",
     "İki haftalık nöbetleşme esası da uygulanabilir.",
     "Posta değişiminde en az on bir saat dinlenme verilir.",
     "Gece çalışması kural olarak yedi buçuk saati geçemez."],
    "Md. 69'a göre bir çalışma haftası gece çalıştırılan işçiler sonraki çalışma haftası gündüz çalıştırılarak postalar sıraya "
    "konur; iki haftalık nöbetleşme de uygulanabilir.")

P.sayisal("İK md. 41",
    "Denkleştirme esası uygulanan bir işyerinde işçi, iki aylık dönemin ilk dört haftasında 50’şer saat, sonraki dört "
    f"haftasında 40’ar saat çalışmıştır.\n\n{K}, bu dönemde fazla çalışma ücretine esas saat toplamı kaçtır?",
    "0", ["5", "10", "20", "40"],
    "Md. 41 ve 63'e göre denkleştirmede haftalık ortalama süre normal süreyi aşmadıkça bazı haftalarda kırk beş saat aşılsa da "
    "fazla çalışma sayılmaz: (4 × 50 + 4 × 40) / 8 = 45 saat; fazla çalışma yoktur.", zorluk="hard")

P.q("İK md. 72",
    f"{K}, maden ocakları ile kablo döşemesi, kanalizasyon ve tünel inşaatı gibi yer altı veya su altı işlerinde "
    "aşağıdakilerden hangisinin çalıştırılması yasaktır?",
    "On sekiz yaşını doldurmamış erkekler",
    ["On sekiz yaşını doldurmuş erkekler",
     "Yirmi yaşını doldurmuş erkekler",
     "Mühendis unvanlı erkek işçiler",
     "Sağlık raporu olan erkek işçiler"],
    "Md. 72'ye göre yer altında veya su altında çalışılacak işlerde on sekiz yaşını doldurmamış erkeklerin ve her yaştaki "
    "kadınların çalıştırılması yasaktır.")

P.sayisal("İK md. 41",
    f"{K26}, yer altı maden işlerinde zorunlu nedenlerle yaptırılan fazla çalışmada, haftalık 37,5 saati aşan her saat "
    "için ücret en az yüzde kaç artırılarak ödenir?",
    "100", ["25", "50", "75", "150"],
    "Md. 41'e göre yer altı maden işçilerine md. 42 ve 43'teki hâllerde haftalık otuz yedi buçuk saati aşan her saat fazla "
    "çalışma için ücret, saat başına düşen miktarın yüzde yüzden az olmamak üzere artırılmasıyla ödenir.", zorluk="hard")

P.q("İK md. 73",
    f"{K}, sanayiye ait işlerde gece çalıştırma yasağına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kadın işçiler her yaşta gece çalıştırılamaz.",
    ["On sekiz yaşından küçükler gece çalıştırılamaz.",
     "Kadınların gece postası usulü yönetmelikle belirlenir.",
     "Bu yönetmelikte Sağlık Bakanlığının görüşü alınır.",
     "Yasak, çocuk ve genç işçileri kapsar."],
    "Md. 73'e göre sanayiye ait işlerde on sekiz yaşını doldurmamış çocuk ve genç işçilerin gece çalıştırılması yasaktır; "
    "on sekiz yaşını doldurmuş kadın işçilerin gece postalarındaki çalışma usulü yönetmelikle belirlenir.")

gt = 1_000 * 2
P.sayisal("İK md. 47",
    "Günlük ücreti 1.000 ₺ olan işçi, bir genel tatil gününde tatil yapmayarak çalışmıştır."
    f"\n\n{K}, işçiye o gün için ödenecek toplam ücret kaç ₺’dir?",
    tl(gt), secenekler(gt, 1_000, 1_500, 3_000, 500),
    "Md. 47'ye göre genel tatil gününde çalışmayan işçiye o günün ücreti tam ödenir; tatil yapmayarak çalışana ayrıca "
    "çalışılan her gün için bir günlük ücret ödenir: 1.000 + 1.000 = 2.000 ₺.")

P.q("İK md. 71",
    f"{K}, on dört yaşını doldurmamış çocukların sanat, kültür ve reklam faaliyetlerinde çalıştırılmasına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Yazılı sözleşme ve faaliyet başına ayrı izin gerekir.",
    ["Bu faaliyetlerde çalıştırılmaları yasaktır.",
     "Velinin sözlü onayı yeterlidir.",
     "Tek bir genel izin bütün faaliyetler için yeterlidir.",
     "Haftada kırk beş saate kadar çalıştırılabilirler."],
    "Md. 71'e göre on dört yaşını doldurmamış çocuklar, gelişmelerine ve okula devamlarına engel olmayacak sanat, kültür ve "
    "reklam faaliyetlerinde yazılı sözleşme yapmak ve her faaliyet için ayrı izin almak şartıyla çalıştırılabilir.")

P.sayisal("İK md. 64",
    f"{K}, zorunlu nedenlerle işin durması hâlinde işveren, çalışılmayan süreler için en geç kaç ay içinde telafi "
    "çalışması yaptırabilir?",
    "4", ["1", "2", "3", "6"],
    "Md. 64'e göre işveren dört ay içinde çalışılmayan süreler için telafi çalışması yaptırabilir; Cumhurbaşkanı bu süreyi iki "
    "katına kadar artırmaya yetkilidir.")

P.q("İK md. 71",
    f"{K}, çocuk ve genç işçilerin çalıştırılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Okula devam eden çocuk, eğitim saatlerinde de çalıştırılabilir.",
    ["Çocuğun gördüğü iş okula gitmesine engel olamaz.",
     "On beş yaşını tamamlayana günde sekiz saate kadar çalışma mümkündür.",
     "İşe yerleştirmede kişisel yatkınlık dikkate alınır.",
     "Sanat ve reklam işlerinde süre günde beş saati aşamaz."],
    "Md. 71'e göre okula devam eden çocukların eğitim dönemindeki çalışma süreleri eğitim saatleri dışında olmak üzere en fazla "
    "günde iki, haftada on saattir.", zorluk="hard")

P.sayisal("İK md. 64",
    f"{K}, telafi çalışması günlük en çok çalışma süresini aşmamak koşuluyla günde en çok kaç saat olabilir?",
    "3", ["1", "2", "4", "5"],
    "Md. 64'e göre telafi çalışmaları, günlük en çok çalışma süresini aşmamak koşuluyla günde üç saatten fazla olamaz.")

P.q("İK md. 63",
    f"{K}, çalışma sürelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Haftalık süre TİS ile 50 saate çıkarılabilir.",
    ["Aksi kararlaştırılmamışsa süre günlere eşit bölünür.",
     "Denkleştirme süresi TİS ile dört aya çıkarılabilir.",
     "Uygulama şekilleri Bakanlık yönetmeliğiyle düzenlenir.",
     "Farklı dağıtımda günlük süre on bir saati aşamaz."],
    "Md. 63'e göre haftalık çalışma süresi en çok kırk beş saattir; toplu iş sözleşmesiyle artırılabilen süre haftalık süre "
    "değil, denkleştirme süresidir (iki aydan dört aya).")

P.sayisal("İK md. 46",
    f"{K}, işçilere yedi günlük bir zaman dilimi içinde kesintisiz en az kaç saat hafta tatili verilir?",
    "24", ["12", "18", "36", "48"],
    "Md. 46'ya göre tatil gününden önce md. 63'e göre belirlenen iş günlerinde çalışmış işçilere yedi günlük bir zaman dilimi "
    "içinde kesintisiz en az yirmi dört saat dinlenme verilir.", zorluk="easy")

P.q("İK md. 41",
    f"{K26}, denkleştirme uygulanan bir işyerinde bazı haftalarda kırk beş saatin aşılmasına ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Ortalama normal süreyi aşmıyorsa fazla çalışma sayılmaz.",
    ["Aşılan her saat için yüzde elli zamlı ödenir.",
     "Aşan saatler yıllık izne eklenir.",
     "Aşan saatler fazla sürelerle çalışma sayılır.",
     "Aşan her hafta için Bakanlık izni gerekir."],
    "Md. 41'e göre denkleştirme esasının uygulandığı hâllerde işçinin haftalık ortalama çalışma süresi normal haftalık süreyi "
    "aşmadıkça bazı haftalarda kırk beş saat aşılsa da bu çalışmalar fazla çalışma sayılmaz.")

P.sayisal("İK md. 46",
    "Turizm işletmesi belgeli bir otelde çalışan işçi, hak kazandığı hafta tatilinin sonraya bırakılmasına yazılı onay "
    f"vermiştir.\n\n{K26}, bu hafta tatili hak kazanılan günü takip eden en çok kaç gün içinde kullandırılabilir?",
    "4", ["2", "3", "7", "15"],
    "Md. 46'ya 2025'te eklenen hükme göre turizm işletmesi belgeli konaklama tesislerinde hafta tatili, işçinin yazılı talebi "
    "veya onayıyla hak kazandığı günü takip eden dört gün içinde kullandırılabilir.", zorluk="hard")

P.q("İK md. 41",
    f"{K26}, fazla sürelerle çalışmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sözleşmedeki süreyi aşan, 45 saate kadarki çalışmadır.",
    ["Haftalık 45 saati aşan her çalışmadır.",
     "Sadece gece yapılan çalışmadır.",
     "Hafta tatilinde yapılan çalışmadır.",
     "Günlük on bir saati aşan çalışmadır."],
    "Md. 41'e göre haftalık süre sözleşmeyle kırk beş saatin altında belirlenmişse, ortalama haftalık süreyi aşan ve kırk beş "
    "saate kadar yapılan çalışmalar fazla sürelerle çalışmadır.")

P.sayisal("İK md. 46",
    "Turizm işletmesi belgeli bir otelde çalışan işçi, hafta tatilinin sonraya bırakılmasına verdiği onayı geri almak "
    f"istemektedir.\n\n{K26}, işçi bu onayı işverene en az kaç gün önceden yazılı bildirimle geri alabilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 46'ya göre işçi verdiği onayı otuz gün önceden işverene yazılı bildirimde bulunmak kaydıyla geri alabilir.",
    zorluk="hard")

P.q("İK md. 41",
    f"{K26}, fazla sürelerle çalışma yapan ve zamlı ücret yerine serbest zaman seçen işçiye her bir saat için ne kadar "
    "serbest zaman verilir?",
    "Bir saat on beş dakika",
    ["Bir saat otuz dakika", "Bir saat", "İki saat", "Kırk beş dakika"],
    "Md. 41'e göre işçi fazla çalıştığı her saat için bir saat otuz dakikayı, fazla sürelerle çalıştığı her saat için bir saat "
    "on beş dakikayı serbest zaman olarak kullanabilir.")

P.sayisal("İK md. 68",
    f"{K}, günlük çalışma süresi yedi buçuk saatten fazla olan işlerde işçiye en az kaç dakika ara dinlenmesi verilir?",
    "60", ["15", "30", "45", "90"],
    "Md. 68'e göre dört saat veya daha kısa işlerde on beş dakika, dört saatten fazla ve yedi buçuk saate kadar işlerde yarım "
    "saat, yedi buçuk saatten fazla işlerde bir saat ara dinlenmesi verilir.", zorluk="easy")

P.q("İK md. 64",
    f"{K}, telafi çalışması yaptırılabilecek süreyi iki katına kadar artırmaya kim yetkilidir?",
    "Cumhurbaşkanı",
    ["Çalışma ve Sosyal Güvenlik Bakanı", "İşveren", "İşyeri sendika temsilcisi", "Türkiye İş Kurumu"],
    "Md. 64'e göre işveren dört ay içinde telafi çalışması yaptırabilir; Cumhurbaşkanı bu süreyi iki katına kadar artırmaya "
    "yetkilidir.")

P.sayisal("İK md. 68",
    f"{K}, günlük çalışma süresi altı saat olan bir işte işçiye en az kaç dakika ara dinlenmesi verilir?",
    "30", ["15", "20", "45", "60"],
    "Md. 68'e göre dört saatten fazla ve yedi buçuk saate kadar (yedi buçuk saat dahil) süreli işlerde yarım saat ara "
    "dinlenmesi verilir.")

P.q("İK md. 70",
    f"{K}, hazırlama, tamamlama veya temizleme işlerinde çalışan işçiler için işin düzenlenmesine ilişkin hükümlerin "
    "uygulanma şekli nerede gösterilir?",
    "Bakanlıkça hazırlanan yönetmelikte",
    ["İşyeri iç yönetmeliğinde", "Cumhurbaşkanı kararında", "İş sözleşmesinde", "Valilik genelgesinde"],
    "Md. 70'e göre bu işlerde çalışanlar için işin düzenlenmesine ilişkin hükümlerden hangilerinin uygulanmayacağı veya hangi "
    "şartlarla uygulanacağı Çalışma ve Sosyal Güvenlik Bakanlığınca hazırlanacak yönetmelikte gösterilir.")

P.sayisal("İK md. 69",
    f"{K}, çalışma hayatında “gece” en fazla kaç saat süren dönemdir?",
    "11", ["7", "8", "10", "12"],
    "Md. 69'a göre gece en geç saat 20.00'de başlayarak en erken saat 06.00'ya kadar geçen ve her hâlükârda en fazla on bir "
    "saat süren dönemdir.")

P.oncul("İK md. 69",
    f"{K26} aşağıdaki işler değerlendirilmektedir:",
    ["Özel güvenlik", "Tekstil üretimi", "Sağlık hizmeti", "Turizm"],
    "Yukarıdakilerden hangilerinde işçinin yazılı onayıyla yedi buçuk saatin üzerinde gece çalışması yaptırılabilir?",
    "I, III ve IV",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 69'a göre turizm, özel güvenlik, sağlık hizmeti ve petrol arama işlerinde yazılı onayla yedi buçuk saatin üzerinde "
    "gece çalışması yaptırılabilir; tekstil üretimi (II) bu işlerden değildir.", zorluk="hard")

P.sayisal("İK md. 69",
    "Gece ve gündüz işletilen bir fabrikada işçi postaları nöbetleşe çalışmakta ve bir işçinin postası değiştirilecektir."
    f"\n\n{K}, bu işçi kesintisiz en az kaç saat dinlendirilmeden diğer postada çalıştırılamaz?",
    "11", ["8", "10", "12", "24"],
    "Md. 69'a göre postası değiştirilecek işçi kesintisiz en az on bir saat dinlendirilmeden diğer postada çalıştırılamaz.")

P.q("İK md. 72",
    f"{K}, aşağıdakilerden hangisinin yer altı veya su altı işlerinde çalıştırılması yasak değildir?",
    "On dokuz yaşındaki erkek işçi",
    ["On yedi yaşındaki erkek işçi", "Yirmi yaşındaki kadın işçi", "Kırk yaşındaki kadın işçi",
     "On altı yaşındaki erkek işçi"],
    "Md. 72'ye göre yer altı veya su altı işlerinde on sekiz yaşını doldurmamış erkeklerin ve her yaştaki kadınların "
    "çalıştırılması yasaktır; on dokuz yaşındaki erkek işçi bu yasak kapsamında değildir.")

P.sayisal("İK md. 71",
    f"{K}, kural olarak kaç yaşını doldurmamış çocukların çalıştırılması yasaktır?",
    "15", ["12", "14", "16", "18"],
    "Md. 71'e göre on beş yaşını doldurmamış çocukların çalıştırılması yasaktır; on dört yaşını doldurmuş ve zorunlu "
    "ilköğretimi tamamlamış çocuklar hafif işlerde çalıştırılabilir.", zorluk="easy")

P.q("İK md. 44",
    f"{K}, ulusal bayram ve genel tatil günlerinde çalışmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sözleşmede hüküm yoksa işveren tek başına karar verir.",
    ["Çalışılıp çalışılmayacağı sözleşmelerle kararlaştırılır.",
     "Çalışmayan işçiye o günün ücreti tam ödenir.",
     "Çalışan işçiye ayrıca bir günlük ücret ödenir.",
     "Yüzde usulünde bu ücretler işverence ödenir."],
    "Md. 44 ve 47'ye göre sözleşmelerde hüküm yoksa bu günlerde çalışılması için işçinin onayı gerekir; çalışmayan işçiye o "
    "günün ücreti tam, çalışana ayrıca bir günlük ücret ödenir.")

P.sayisal("İK md. 71",
    "Zorunlu ilköğretim çağını tamamlamış, örgün eğitime devam etmeyen ve henüz on beş yaşını tamamlamamış bir çocuk hafif "
    f"işlerde çalışmaktadır.\n\n{K}, bu çocuğun haftalık çalışma süresi en çok kaç saat olabilir?",
    "35", ["20", "30", "40", "45"],
    "Md. 71'e göre zorunlu ilköğretim çağını tamamlamış ve örgün eğitime devam etmeyen çocukların çalışma saatleri günde yedi ve "
    "haftada otuz beş saatten fazla olamaz; on beş yaşını tamamlamış çocuklar için günde sekiz ve haftada kırk saate kadar "
    "artırılabilir.", zorluk="hard")

P.q("İK md. 46",
    "Bir işyerinde sel felaketi nedeniyle işin bir haftadan uzun süre tatil edilmesini gerektiren zorlayıcı sebep ortaya "
    f"çıkmıştır.\n\n{K}, bu dönemde hafta tatili günü için işçilere ne ödenir?",
    "Yarım ücret",
    ["Tam ücret", "Ücret ödenmez", "İki kat ücret", "Ücretin dörtte biri"],
    "Md. 46'ya göre işin bir haftadan fazla tatilini gerektiren zorlayıcı sebeplerde, çalışılmayan günler için ödenen yarım "
    "ücret hafta tatili günü için de ödenir.")

P.sayisal("İK md. 71",
    f"{K}, okula devam eden bir çocuğun eğitim dönemindeki çalışma süresi, eğitim saatleri dışında olmak üzere haftada "
    "en çok kaç saat olabilir?",
    "10", ["5", "8", "15", "20"],
    "Md. 71'e göre okul öncesi çocuklar ile okula devam eden çocukların eğitim dönemindeki çalışma süreleri, eğitim saatleri "
    "dışında olmak üzere en fazla günde iki saat ve haftada on saat olabilir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
