# -*- coding: utf-8 -*-
"""Vergi · VUK · Vergi Cezaları (vergi ziyaı, usulsüzlük, kaçakçılık, pişmanlık, izaha davet, indirim) — 60 soru.

Gerçek 2026/1-2026/2 kitapçıklarında bu konu; kaçakçılık fiilleri, pişmanlık ve ıslah şartları (öncüllü), izaha davette
ceza oranı ve vergi ziyaı cezasında zamanaşımı üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 213 sayılı VUK md. 331-377 (7524 sayılı Kanunla değişik
md. 344 ve 376 dahil). Yeniden değerlenen tutarlar kökte verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_vergi_cezalari_2026.json", lesson="vergi_usul_kanunu", topic="vergi_cezalari",
          konu_adi="Vergi Cezaları", seed=2026092909,
          surum="213 sayılı VUK güncel metni (7524 dahil); tutarlar kökte; 29.09.2026 kontrolü")

V = "213 sayılı Vergi Usul Kanunu’na göre"
V26 = "213 sayılı Vergi Usul Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("VUK md. 344",
    "Vergi incelemesi sonucunda Bay (K)’nın 2024 yılı gelir vergisi beyannamesinde hasılatın bir kısmını unuttuğu ve bu "
    "nedenle 200.000 ₺ verginin eksik tahakkuk ettiği tespit edilmiştir. Kaçakçılık fiili ve kayıt dışı faaliyet yoktur."
    f"\n\n{V26}, Bay (K) adına kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(200_000), secenekler(200_000, 100_000, 600_000, 300_000, 40_000),
    "Md. 344/1'e göre vergi ziyaına sebebiyet verildiğinde ziyaa uğratılan verginin bir katı tutarında vergi ziyaı cezası "
    "kesilir: 200.000 ₺.", zorluk="easy")

P.q("VUK md. 359",
    "Bir vergi incelemesinde, (DEF) Ltd. Şti. yetkililerinin çeşitli fiilleri tespit edilmiştir."
    f"\n\n{V}, aşağıdakilerden hangisi kaçakçılık suçunu oluşturan fiillerden biri değildir?",
    "Faturayı alıcıya vermemek",
    ["Belgelerin asıl veya suretlerini sahte olarak düzenlemek",
     "Varlığı sabit olan defterleri incelemede ibraz etmemek",
     "Defterlerde hesap ve muhasebe hilesi yapmak",
     "Muhteviyatı itibarıyla yanıltıcı belge düzenlemek"],
    "Md. 359'a göre sahte belge düzenleme, varlığı sabit defterlerin ibraz edilmemesi (gizleme), hesap ve muhasebe hilesi ve "
    "yanıltıcı belge düzenleme kaçakçılık suçudur. Faturayı vermemek md. 353'e göre özel usulsüzlüktür.", zorluk="easy")

P.q("VUK md. 359",
    f"{V}, sahte belge ile muhteviyatı itibarıyla yanıltıcı belge ayrımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gerçek işlemi farklı yansıtan belge yanıltıcı belgedir.",
    ["Gerçek bir işlemi farklı yansıtan belge sahte belgedir.",
     "Gerçekte yapılmamış işlem için düzenlenen belge yanıltıcı belgedir.",
     "Her iki belge türü için de aynı hapis cezası öngörülmüştür.",
     "Yanıltıcı belge kullanmak kaçakçılık suçu değildir."],
    "Md. 359'a göre gerçek bir muamele olmadığı hâlde varmış gibi düzenlenen belge sahte belge, gerçek bir muameleye dayanmakla "
    "birlikte bunu mahiyet veya miktar itibarıyla gerçeğe aykırı yansıtan belge yanıltıcı belgedir. Sahte belgede ceza üç "
    "yıldan sekiz yıla, yanıltıcı belgede on sekiz aydan beş yıla kadar hapistir.", zorluk="hard")

P.sayisal("VUK md. 344, 359",
    "Bir incelemede (ABC) Ltd. Şti.’nin sahte belge kullanarak 150.000 ₺ katma değer vergisini ziyaa uğrattığı "
    "tespit edilmiştir. Şirket kayıtlı mükelleftir."
    f"\n\n{V26}, şirket adına kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(450_000), secenekler(450_000, 150_000, 300_000, 675_000, 225_000),
    "Md. 344/2'ye göre vergi ziyaına md. 359'da yazılı fiillerle (sahte belge kullanma) sebebiyet verilmesi hâlinde ceza üç "
    "kat uygulanır: 150.000 × 3 = 450.000 ₺.")

P.q("VUK md. 341",
    f"Bir inceleme raporunda, mükellefin çeşitli nedenlerle vergisinin eksik tahakkuk ettiği ve bir kısmının haksız iade edildiği tespit edilmiştir.\n\n{V}, vergi ziyaına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Verginin sonradan tahakkuk ettirilmesi ceza kesilmesine engeldir.",
    ["Ödevlerin zamanında yerine getirilmemesi nedeniyle verginin zamanında tahakkuk etmemesidir.",
     "Aile durumu hakkında gerçeğe aykırı beyanla verginin eksik tahakkuku vergi ziyaıdır.",
     "Verginin haksız yere geri verilmesine sebebiyet vermek vergi ziyaı hükmündedir.",
     "Ödevlerin eksik yerine getirilmesiyle verginin eksik tahakkuku vergi ziyaıdır."],
    "Md. 341'e göre vergi ziyaı hâllerinde verginin sonradan tahakkuk ettirilmesi veya tamamlanması ya da haksız iadenin geri "
    "alınması ceza uygulanmasına mani teşkil etmez.")

P.q("VUK md. 344",
    f"{V26}, vergi ziyaı cezasının uygulanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaçakçılık fiillerine iştirak edenlere ceza üç kat uygulanır.",
    ["Genel kural olarak ceza ziyaa uğratılan verginin bir katıdır.",
     "Kaçakçılık fiilleriyle ziyada ceza üç kat uygulanır.",
     "İnceleme öncesi süresinden sonra verilen beyannamelerde ceza yüzde elli uygulanır.",
     "Kayıt dışı faaliyetle ziyada ceza yüzde elli artırılır."],
    "Md. 344/2'ye göre md. 359'daki fiillerle ziyada ceza üç kat, bu fiillere iştirak edenlere ise bir kat olarak uygulanır.",
    zorluk="hard")

P.sayisal("VUK md. 344",
    "Bay (L), 2025 yılı gelir vergisi beyannamesini kanuni süresinden sonra, hakkında vergi incelemesine başlanmadan ve "
    "takdire sevk edilmeden kendiliğinden vermiştir; ancak pişmanlık şartlarını yerine getirmemiştir. Beyannamede "
    f"hesaplanan vergi 100.000 ₺’dir.\n\n{V26}, Bay (L) adına kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(50_000), secenekler(50_000, 100_000, 0, 20_000, 150_000),
    "Md. 344/3'e göre vergi incelemesine başlanılmasından veya takdire sevkten sonra verilenler hariç, kanuni süresi geçtikten "
    "sonra verilen beyannameler için vergi ziyaı cezası yüzde elli oranında uygulanır: 100.000 × %50 = 50.000 ₺.",
    zorluk="hard")

P.q("VUK md. 351-352",
    f"Yoklama ve inceleme sırasında bir mükellef nezdinde şekil ve usule ilişkin çeşitli aykırılıklar tespit edilmiştir.\n\n{V}, aşağıdakilerden hangisi birinci derece usulsüzlüklerden biri değildir?",
    "Muhasebe fişlerinin yetkili amirlerce imza edilmemesi",
    ["Beyannamenin süresinde verilmemesi",
     "Tutulması mecburi defterlerden birinin tutulmaması",
     "Kayıtların doğru incelemeye imkân vermeyecek derecede karışık olması",
     "Çiftçilerin muhtar ve ihtiyar heyetinin davetine süresinde icabet etmemesi"],
    "Md. 352'ye göre beyannamenin süresinde verilmemesi, mecburi defterlerin tutulmaması, kayıtların incelemeye imkân "
    "vermeyecek derecede noksan veya karışık olması ve çiftçilerin davete icabet etmemesi birinci derece usulsüzlüktür; "
    "fişlerin imzasız olması gibi hâller ikinci derecededir.", zorluk="hard")

P.q("VUK md. 351",
    f"Bir mükellefin defter ve belge düzenine ilişkin çeşitli aykırılıkları tespit edilmiş, ancak bu aykırılıklar vergi kaybına yol açmamıştır.\n\n{V}, usulsüzlüğün tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Şekil ve usul hükümlerine uyulmamasıdır.",
    ["Verginin eksik tahakkuk etmesine yol açan her fiildir.",
     "Sadece defter tutmama fiilidir.",
     "Hapis cezasını gerektiren vergi suçudur.",
     "Sadece beyannamenin verilmemesidir."],
    "Md. 351'e göre usulsüzlük, vergi kanunlarının şekle ve usule ilişkin hükümlerine riayet edilmemesidir; verginin eksik "
    "tahakkuku ise vergi ziyaıdır (md. 341).", zorluk="easy")

P.sayisal("VUK md. 344",
    "Bay (M), vergi dairesine hiç kayıt yaptırmadan ve dairenin ıttılaı dışında ticari faaliyette bulunmuş; yapılan tespitte "
    f"100.000 ₺ gelir vergisinin ziyaa uğratıldığı belirlenmiştir. Kaçakçılık fiili yoktur.\n\n{V26}, Bay (M) adına "
    "kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(150_000), secenekler(150_000, 100_000, 300_000, 450_000, 200_000),
    "7524 sayılı Kanunla eklenen md. 344/4'e göre mükellefiyet tesis ettirmeden vergi dairesinin ıttılaı dışında faaliyette "
    "bulunarak vergi ziyaına sebebiyet verilmesi hâlinde ceza yüzde elli artırılır: 100.000 × 1,5 = 150.000 ₺.",
    zorluk="hard")

P.q("VUK md. 353",
    f"Bir vergi müfettişi, mükellefin belge düzenine ilişkin aykırılıklarını tespit etmiş ve hangi cezaların uygulanacağını değerlendirmektedir.\n\n{V}, özel usulsüzlük cezası gerektiren fiiller arasında aşağıdakilerden hangisi yer almaz?",
    "Beyannamenin süresinde verilmemesi",
    ["Faturanın verilmemesi veya alınmaması",
     "Belgede gerçek meblağdan farklı meblağa yer verilmesi",
     "Elektronik düzenlenmesi gerekirken belgenin kâğıt olarak düzenlenmesi",
     "Müstahsil makbuzunun düzenlenmemesi"],
    "Md. 353'e göre fatura, gider pusulası, müstahsil makbuzu ve serbest meslek makbuzunun verilmemesi, alınmaması, farklı "
    "meblağ yazılması veya elektronik yerine kâğıt düzenlenmesi özel usulsüzlüktür. Beyannamenin süresinde verilmemesi md. "
    "352'ye göre birinci derece usulsüzlüktür.")

P.q("VUK md. 336",
    "Bay (Y)’nin daha önce usulsüzlük cezası kesilen bir fiili nedeniyle vergi ziyaına da sebebiyet verdiği sonradan "
    f"anlaşılmıştır.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Cezalar mukayese edilir, noksan kısım ikmal edilir.",
    ["Usulsüzlük cezası kesildiği için vergi ziyaı cezası kesilemez.",
     "Her iki ceza da ayrı ayrı ve tam olarak kesilir.",
     "Usulsüzlük cezası iade edilir, sadece vergi ziyaı cezası kesilir.",
     "Vergi ziyaı cezası usulsüzlük cezasının iki katı olarak kesilir."],
    "Md. 336'ya göre usulsüzlük cezası kesilen bir fiil ile vergi ziyaına da sebebiyet verildiği sonradan anlaşılırsa, evvelce "
    "usulsüzlük cezası kesilmiş olması, bu cezanın vergi ziyaı cezasıyla mukayesesine ve noksan kesilen cezanın ikmaline "
    "mani değildir.", zorluk="hard")

P.sayisal("VUK md. 344",
    "Kayıt dışı faaliyet gösteren Bay (N)’nin sahte belge kullanarak 100.000 ₺ vergiyi ziyaa uğrattığı tespit edilmiştir."
    f"\n\n{V26}, Bay (N) adına kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(450_000), secenekler(450_000, 300_000, 150_000, 400_000, 600_000),
    "Md. 344/2'ye göre md. 359'daki fiillerle ziyada ceza üç kattır (300.000 ₺); md. 344/4'e göre mükellefiyet tesis "
    "ettirmeden faaliyette bulunulmuşsa bu ceza yüzde elli artırılır: 300.000 × 1,5 = 450.000 ₺.", zorluk="hard")

P.q("VUK md. 335",
    "(ZAB) A.Ş.’nin tek bir fiili hem kurumlar vergisinin hem de katma değer vergisinin ziyaına sebep olmuştur."
    f"\n\n{V}, vergi ziyaı cezası nasıl kesilir?",
    "Her vergi bakımından ayrı ayrı ceza kesilir.",
    ["Sadece tutarı büyük olan vergi için ceza kesilir.",
     "İki vergi toplamı üzerinden tek bir ceza kesilir.",
     "Tek fiil olduğundan sadece usulsüzlük cezası kesilir.",
     "Ceza vergiler toplamının yarısı üzerinden kesilir."],
    "Md. 335'e göre vergi ziyaı cezasında cezayı gerektiren tek bir fiil ile başka nevinden birkaç vergi ziyaa uğramışsa her "
    "vergi bakımından ayrı ayrı ceza kesilir.")

P.q("VUK md. 332-333",
    f"Bir anonim şirketin ve velayet altındaki bir çocuğun vergi işlemlerinde kanuna aykırılıklar tespit edilmiş, cezanın kime kesileceği tartışılmaktadır.\n\n{V}, vergi cezalarının muhatabına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tüzel kişilerin idaresinden doğan vergi cezaları kanuni temsilcileri adına kesilir.",
    ["Veli, vasi veya kayyımın aykırı hareketlerinde cezanın muhatabı veli, vasi veya kayyımdır.",
     "Küçükler veli veya vasinin aykırı hareketlerinden dolayı cezaya muhatap tutulmaz.",
     "Kaçakçılık fiillerinde hapis cezası fiili işleyenler hakkında hükmolunur.",
     "Kanuni temsilcilerin sorumluluğuna ilişkin md. 10 hükmü cezalar için de uygulanır."],
    "Md. 333'e göre tüzel kişilerin idaresinde vergi kanunlarına aykırı hareketlerden doğan vergi cezaları tüzel kişiler "
    "adına kesilir; kanuni temsilcilerin sorumluluğu md. 10 çerçevesinde uygulanır.", zorluk="hard")

tk = 80_000 + min(80_000 * 0.50, 30_000)
P.sayisal("VUK md. 339",
    "Bay (P)’ye 2023 yılında kesilen 30.000 ₺ vergi ziyaı cezası aynı yıl kesinleşmiştir. 2026 yılında yeniden vergi ziyaına "
    f"sebebiyet verdiği için 80.000 ₺ vergi ziyaı cezası kesilecektir.\n\n{V}, tekerrür hükmü uygulanarak kesilecek toplam "
    "vergi ziyaı cezası kaç ₺’dir?",
    tl(tk), secenekler(tk, 120_000, 80_000, 90_000, 100_000),
    "Md. 339'a göre vergi ziyaı cezası kesinleşme tarihini izleyen günden itibaren beşinci yılın isabet ettiği takvim yılı "
    "sonuna kadar yeniden ceza kesilirse ceza %50 artırılır; ancak artırım kesinleşen cezadan fazla olamaz: 40.000 ₺ artırım "
    "30.000 ₺ ile sınırlanır; 80.000 + 30.000 = 110.000 ₺.", zorluk="hard")

P.q("VUK md. 372-373",
    f"{V}, vergi cezalarının kesilmesine engel olan hâllere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ölüm hâlinde vergi cezası düşer.",
    ["Ölüm hâlinde ceza mirasçılardan tahsil edilir.",
     "Mücbir sebep ispatlansa da ceza kesilir.",
     "Mükellefin ekonomik durumunun kötüleşmesi cezayı düşürür.",
     "Cezanın vergi aslından yüksek olması cezayı düşürür."],
    "Md. 372'ye göre ölüm hâlinde vergi cezası düşer; md. 373'e göre mücbir sebeplerden birinin varlığı malum ise veya "
    "ispat olunursa vergi cezası kesilmez.", zorluk="easy")

P.q("VUK md. 371",
    f"Beyannamesindeki bir hatayı fark eden bir mükellef, pişmanlık hükümlerinden yararlanarak durumu vergi dairesine bildirmeyi düşünmektedir.\n\n{V}, pişmanlık ve ıslah hükümlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Pişmanlıkla beyanname veren mükellefe usulsüzlük cezası da kesilmez.",
    ["Pişmanlık şartları sağlanırsa vergi ziyaı cezası kesilmez.",
     "Haber verme dilekçesinin inceleme başlamadan önce verilmesi gerekir.",
     "Vergi gecikme zammı oranında pişmanlık zammıyla ödenmelidir.",
     "Pişmanlık hükümleri emlak vergisine uygulanmaz."],
    "Md. 371'e göre pişmanlık şartları sağlandığında sadece vergi ziyaı cezası kesilmez; süresinde verilmeyen beyanname "
    "nedeniyle usulsüzlük cezası kesilir. Diğer ifadeler maddeye uygundur.", zorluk="hard")

P.sayisal("VUK md. 339",
    "(DEF) A.Ş.’ye 2025 yılında kesilen usulsüzlük cezası aynı yıl kesinleşmiştir. 2026 yılında yine usulsüzlük nedeniyle "
    f"4.000 ₺ ceza kesilecektir; önceki ceza 4.000 ₺’den azdır.\n\n{V}, tekerrür nedeniyle kesilecek toplam usulsüzlük "
    "cezası kaç ₺’dir? (Artırım, önceki cezayı aşmamaktadır.)",
    tl(5_000), secenekler(5_000, 4_000, 6_000, 8_000, 4_400),
    "Md. 339'a göre usulsüzlükte cezanın kesinleştiği tarihi izleyen günden itibaren ikinci yılın isabet ettiği takvim yılı "
    "sonuna kadar tekrar ceza kesilirse usulsüzlük cezası yüzde yirmi beş artırılır: 4.000 × 1,25 = 5.000 ₺.")

P.q("VUK md. 371",
    "(GHI) A.Ş., bir vergi dairesine ihbar yapılmasından sonra aynı konuyu dilekçeyle haber vermiştir. İhbar dilekçesi resmî "
    f"kayıtlara geçmiştir.\n\n{V}, şirketin pişmanlıktan yararlanma durumu hakkında aşağıdakilerden hangisi doğrudur?",
    "İhbar önce yapıldığından pişmanlıktan yararlanamaz.",
    ["İhbarın varlığı pişmanlığı etkilemez.",
     "Pişmanlık zammı iki kat ödenirse yararlanabilir.",
     "Sadece usulsüzlük cezası kesilmez.",
     "İhbar sözlü yapıldığında tutanak olsa da yararlanır."],
    "Md. 371/1'e göre mükellefin haber verdiği tarihten önce bir muhbir tarafından resmî bir makama dilekçe veya tutanakla "
    "tevsik edilen şifahi beyanla ihbarda bulunulmamış olması gerekir; ihbar resmî kayıtlara geçmişse pişmanlık uygulanmaz.")

P.q("VUK md. 370",
    f"Gelir İdaresi, bazı mükellefler hakkında vergi ziyaına delalet eden emareler tespit etmiş ve bunları izaha davet edip etmemeyi değerlendirmektedir.\n\n{V26}, izaha davete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaçakçılık fiiline ilişkin tüm ön tespitlerde mükellefler izaha davet edilebilir.",
    ["İzaha davet vergi incelemesine başlanmadan önce yapılır.",
     "İzaha davet edilen mükellef davet konusu tespitle sınırlı olarak pişmanlıktan yararlanamaz.",
     "İzah yeterli bulunursa mükellef o tespitle ilgili incelemeye tabi tutulmaz.",
     "İzah yetersizse şartlar sağlanınca ceza %20 oranında kesilir."],
    "Md. 370/b'ye göre ön tespitin verginin md. 359'daki fiillerle ziyaa uğratılmış olabileceğine ilişkin olması hâlinde "
    "mükellefler izaha davet edilmez; Kanunda sahte veya yanıltıcı belge kullanmaya ilişkin sınırlı bir istisna öngörülmüştür.",
    zorluk="hard")

P.sayisal("VUK md. 337",
    "(GHI) Ltd. Şti. aynı takvim yılı içinde, Kanunun 352. maddesindeki aynı derece ve fıkraya giren üç ayrı usulsüzlük "
    "fiili işlemiştir. (Birinci fiil için 1 sayılı cetvele göre kesilecek ceza 2.000 ₺ olarak alınacaktır.)"
    f"\n\n{V26}, bu üç usulsüzlük için kesilecek toplam ceza kaç ₺’dir?",
    tl(2_000 + 500 * 2), secenekler(3_000, 6_000, 2_000, 4_000, 2_500),
    "Md. 337'ye göre md. 352'deki usulsüzlüklerden aynı takvim yılı içinde aynı nevinden birden fazla yapılırsa, birinciden "
    "sonrakilerin her biri için birincisine ait cezanın dörtte biri kesilir: 2.000 + 500 + 500 = 3.000 ₺.", zorluk="hard")

P.q("VUK md. 376",
    f"{V26}, cezalarda indirime ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mükellef dava açsa da indirim hakkını korur.",
    ["Başvuru ihbarnamenin tebliğinden itibaren otuz gün içinde yapılır.",
     "Vergi ve cezanın indirimli kısmı vadesinde veya teminatla vadeden itibaren üç ay içinde ödenmelidir.",
     "Vergi aslına bağlı olmayan usulsüzlük cezalarında da uygulanır.",
     "Şartlar sağlanırsa kesilen cezanın yarısı indirilir."],
    "Md. 376'ya göre mükellef ödeyeceğini bildirdiği vergi ve cezayı süresinde ödemez veya dava konusu yaparsa indirimden "
    "yararlandırılmaz.")

P.q("VUK md. 374",
    f"Bir vergi dairesi, geçmiş yıllarda işlenmiş fiiller için ceza kesme yetkisinin devam edip etmediğini araştırmaktadır.\n\n{V}, ceza kesmede zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Süre içinde ceza ihbarnamesinin tebliği zamanaşımını keser.",
    ["Usulsüzlük cezalarında süre beş yıldır.",
     "Vergi ziyaı cezasında süre iki yıldır.",
     "Zamanaşımı ancak mükellefin başvurusuyla uygulanır.",
     "Özel usulsüzlükte süre iki yıldır."],
    "Md. 374'e göre vergi ziyaı ve md. 353 ile mük. 355'teki cezalarda süre beş, genel usulsüzlükte iki yıldır; bu süreler "
    "içinde ceza ihbarnamesinin tebliğiyle zamanaşımı kesilir.")

P.sayisal("VUK md. 353",
    "(JKL) A.Ş.’nin 2026 yılında bir müşterisine 300.000 ₺ bedelli satış için fatura vermediği ilk kez tespit edilmiştir. "
    f"(Kanunda ilk tespit için belirtilen asgari tutar 17.000 ₺ olarak alınacaktır.)\n\n{V26}, (JKL) A.Ş.’ye bu fatura için "
    "kesilecek özel usulsüzlük cezası kaç ₺’dir?",
    tl(30_000), secenekler(30_000, 17_000, 47_000, 60_000, 3_000),
    "Md. 353/1'e göre verilmesi gereken faturanın verilmemesi hâlinde, ilk tespitte Kanundaki asgari tutardan aşağı olmamak "
    "üzere belgeye yazılması gereken meblağın %10'u oranında özel usulsüzlük cezası kesilir: 300.000 × %10 = 30.000 ₺, "
    "asgari tutarın üzerindedir.")

P.q("VUK md. 367",
    "Vergi müfettişi, (JKL) A.Ş. nezdindeki incelemede sahte belge düzenleme suçunun işlendiğini tespit etmiştir."
    f"\n\n{V}, bu durumda yapılacak işleme ilişkin aşağıdakilerden hangisi doğrudur?",
    "Cumhuriyet başsavcılığına bildirim zorunludur.",
    ["Bildirim, vergi mahkemesi kararı kesinleştikten sonra yapılır.",
     "Suç sadece vergi dairesince ceza kesilerek sonuçlandırılır.",
     "Bildirim mükellefin talebine bağlıdır.",
     "Bildirim için uzlaşma sürecinin tamamlanması gerekir."],
    "Md. 367'ye göre inceleme sırasında md. 359'daki suçların işlendiğini tespit eden vergi müfettişleri, ilgili rapor "
    "değerlendirme komisyonunun mütalaasıyla keyfiyeti doğrudan Cumhuriyet başsavcılığına bildirmek zorundadır.")

P.q("VUK md. 339",
    f"Daha önce cezası kesinleşmiş olan bir mükellefe yeni bir vergi cezası kesilmesi gündemdedir ve cezanın artırılıp artırılmayacağı değerlendirilmektedir.\n\n{V}, tekerrüre ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tekerrür için önceki cezanın kesinleşmiş olması gerekmez.",
    ["Vergi ziyaı cezasında artırım oranı yüzde ellidir.",
     "Usulsüzlük cezasında artırım oranı yüzde yirmi beştir.",
     "Artırım tutarı kesinleşen cezadan fazla olamaz.",
     "Sürelerin hesabında önceki cezanın kesinleşme tarihi dikkate alınır."],
    "Md. 339'a göre tekerrür, ceza kesilen ve cezası kesinleşenlere belirli süreler içinde tekrar ceza kesilmesi hâlinde "
    "uygulanır; önceki cezanın kesinleşmiş olması şarttır.")

P.sayisal("VUK md. 353",
    "Avukat Bay (G)’nin 2026 yılında müvekkilinden tahsil ettiği 100.000 ₺ ücret için serbest meslek makbuzu düzenlemediği "
    f"ilk kez tespit edilmiştir. (Kanunda ilk tespit için belirtilen asgari tutar 17.000 ₺ olarak alınacaktır.)\n\n{V26}, kesilecek özel "
    "usulsüzlük cezası kaç ₺’dir?",
    tl(17_000), secenekler(17_000, 10_000, 27_000, 20_000, 34_000),
    "Md. 353/1 serbest meslek makbuzunun düzenlenmemesini de kapsar; ceza belge tutarının %10'udur (10.000 ₺), ancak ilk "
    "tespitte Kanundaki asgari tutardan aşağı olamaz: 17.000 ₺.", zorluk="hard")

P.oncul("VUK md. 370-371",
    f"{V} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Hiç verilmemiş beyanname haber verme tarihinden itibaren otuz gün içinde verilmelidir.",
     "İzaha davet edilen mükellef davet konusu tespitle sınırlı olarak pişmanlıktan yararlanamaz.",
     "Pişmanlık şartlarını sağlayan mükellefe vergi ziyaı cezası kesilmez.",
     "Pişmanlıkla beyanname verilmesi hâlinde usulsüzlük cezası da kesilmez."],
    "Yukarıdakilerden hangileri doğrudur?",
    "II ve III",
    ["I ve II", "I ve III", "II ve III", "II ve IV", "III ve IV"],
    "Md. 371'e göre hiç verilmemiş beyanname on beş gün içinde verilmelidir (I yanlış); pişmanlıkta sadece vergi ziyaı "
    "cezası kesilmez, usulsüzlük cezası kesilir (III doğru, IV yanlış). Md. 370'e göre izaha davet edilen mükellef davet "
    "konusu tespitle sınırlı olarak pişmanlıktan yararlanamaz (II doğru).", zorluk="hard")

P.q("VUK md. 344",
    "Vergi incelemesi başladıktan sonra Bay (Z), 2025 yılı beyannamesini vermiştir. İnceleme sonucu 80.000 ₺ vergi ziyaı "
    f"tespit edilmiştir.\n\n{V26}, bu beyanname için vergi ziyaı cezasının yüzde elli oranında uygulanması hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "İnceleme sonrası verildiğinden oran indirilmez.",
    ["Süresinden sonra verildiği için ceza yüzde elli uygulanır.",
     "İnceleme sırasında verilen beyannamelerde ceza kesilmez.",
     "Ceza yüzde yirmi oranında uygulanır.",
     "Ceza üç kat uygulanır."],
    "Md. 344/3'e göre süresinden sonra verilen beyannamelerde cezanın yüzde elli oranında uygulanması, vergi incelemesine "
    "başlanılmasından veya takdire sevkten sonra verilen beyannameler için geçerli değildir; ceza bir kat uygulanır.",
    zorluk="hard")

ind = 200_000 + 200_000 / 2
P.sayisal("VUK md. 376",
    "Vergi incelemesi sonucunda (OPR) A.Ş. adına 200.000 ₺ ikmalen vergi tarh edilmiş ve 200.000 ₺ vergi ziyaı cezası "
    "kesilmiştir. Şirket ihbarnamenin tebliğinden itibaren 30 gün içinde vergi dairesine başvurarak vergi ile cezanın "
    f"indirimli kısmını vadesinde ödeyeceğini bildirmiş ve süresinde ödemiştir.\n\n{V26}, şirketin ödediği vergi ve ceza "
    "toplamı kaç ₺’dir?",
    tl(ind), secenekler(ind, 400_000, 200_000, 200_000 + 200_000 / 3, 200_000 + 200_000 * 2 / 3),
    "Md. 376/1'e göre tarh edilen vergiyi ve cezaların yarısını tebliğden itibaren 30 gün içinde başvurarak vadesinde "
    "ödeyeceğini bildiren ve ödeyen mükellefin cezasının yarısı indirilir: 200.000 + 100.000 = 300.000 ₺.")

P.q("VUK md. 353",
    "(MNO) A.Ş.’nin aynı tespitte, düzenlemesi gereken beş ayrı faturayı düzenlemediği belirlenmiştir."
    f"\n\n{V26}, özel usulsüzlük cezası uygulamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her bir belge için ayrı ayrı ceza kesilir.",
    ["Beş fatura için tek bir ceza kesilir.",
     "Sadece en yüksek tutarlı fatura için ceza kesilir.",
     "Aynı neviden olduğundan sonraki faturalar için dörtte bir oranında ceza kesilir.",
     "Tek tespitte özel usulsüzlük cezası kesilmez."],
    "Md. 353/1'e 7524 sayılı Kanunla eklenen cümleye göre tek tespitte aynı neviden birden fazla belgenin düzenlenmediğinin "
    "tespiti hâlinde her bir belge için ayrı ayrı ceza kesilir.", zorluk="hard")

P.q("VUK md. 331",
    f"Vergi Usul Kanunu’nun ceza hükümlerini inceleyen stajyer bir meslek mensubu, Kanunda düzenlenen ceza türlerini sınıflandırmaktadır.\n\n{V}, vergi cezalarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi cezaları, vergi ziyaı cezası ve usulsüzlük cezalarıdır.",
    ["Vergi cezaları sadece hapis cezalarından ibarettir.",
     "Usulsüzlük cezaları vergi cezası sayılmaz.",
     "Vergi ziyaı cezası sadece kaçakçılıkta kesilir.",
     "Vergi cezaları mahkeme kararıyla kesilir."],
    "Md. 331'e göre vergi kanunlarına aykırı hareket edenler vergi cezaları (vergi ziyaı cezası ve usulsüzlük cezaları) ve "
    "diğer cezalarla cezalandırılır.", zorluk="easy")

P.sayisal("VUK md. 370",
    "İzaha davet edilen Bayan (R)’nin izahı yeterli bulunmamış; değerlendirme yazısının tebliğinden itibaren 30 gün içinde "
    "beyanını düzeltmiş ve ziyaa uğrattığı 100.000 ₺ vergiyi izah zammıyla ödemiştir."
    f"\n\n{V26}, Bayan (R) adına kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(20_000), secenekler(20_000, 100_000, 50_000, 0, 10_000),
    "Md. 370/a-2'ye göre izahın yeterli bulunmaması hâlinde 30 gün içinde beyan tamamlanır ve vergi izah zammıyla ödenirse "
    "vergi ziyaı cezası ziyaa uğratılan vergi üzerinden %20 oranında kesilir: 20.000 ₺.")

P.q("VUK md. 337",
    f"(ABC) Ltd. Şti.’nin aynı yıl içinde farklı tarihlerde işlediği birden fazla fiil nedeniyle kesilecek cezalar değerlendirilmektedir.\n\n{V}, fiil ayrılığına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ayrı ayrı yapılan her fiil için ayrı ayrı ceza kesilir.",
    ["Ayrı fiiller için sadece en ağır ceza kesilir.",
     "Aynı yıl içindeki tüm usulsüzlüklere tek ceza kesilir.",
     "Farklı nevideki usulsüzlüklere dörtte bir oranında ceza kesilir.",
     "Fiil ayrılığı sadece özel usulsüzlükte uygulanır."],
    "Md. 337'ye göre ayrı ayrı yapılmış vergi ziyaı veya usulsüzlüklerden dolayı ayrı ayrı ceza kesilir; ancak md. 352'deki "
    "aynı nevi usulsüzlüklerde aynı yıl içindeki sonrakiler için birincisinin dörtte biri kesilir.")

P.q("VUK md. 359",
    f"{V}, aşağıdaki fiillerden hangisi en ağır hapis cezasını (üç yıldan sekiz yıla kadar) gerektirir?",
    "Sahte belge düzenlemek",
    ["Muhteviyatı itibarıyla yanıltıcı belge düzenlemek",
     "Defterlerde hesap hilesi yapmak",
     "Defter ve belgeleri gizlemek",
     "Gerçek olmayan kişiler adına hesap açmak"],
    "Md. 359/b'ye göre defter ve belgeleri yok edenler veya belgeleri sahte düzenleyen ya da kullananlar üç yıldan sekiz yıla "
    "kadar; md. 359/a'daki hesap hilesi, gizleme ve yanıltıcı belge fiilleri on sekiz aydan beş yıla kadar hapisle "
    "cezalandırılır.")

P.sayisal("VUK md. 352",
    "(PRS) A.Ş.’nin işlediği bir usulsüzlük fiili, matrahın resen takdirini gerektirecek niteliktedir. (Bu fiil için 1 sayılı "
    f"cetvelde yer alan ceza 3.000 ₺ olarak alınacaktır.)\n\n{V26}, bu usulsüzlük için kesilecek ceza kaç ₺’dir?",
    tl(6_000), secenekler(6_000, 3_000, 9_000, 4_500, 12_000),
    "Md. 352'ye göre usulsüzlük fiili resen takdiri gerektirirse 1 sayılı cetvelde yazılı cezalar iki kat olarak kesilir: "
    "3.000 × 2 = 6.000 ₺.")

P.q("VUK md. 370",
    f"Vergi dairesi, bir mükellefin beyanlarında vergi ziyaına işaret eden emareler tespit etmiş, ancak henüz inceleme başlatmamıştır.\n\n{V}, izaha davet edilebilmenin şartlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ön tespitle ilgili tespit tarihine kadar ihbarda bulunulmamış olmalıdır.",
    ["İzaha davet vergi incelemesi sürerken yapılır.",
     "İzaha davet için mükellefin talebi gerekir.",
     "İzaha davet sadece kaçakçılık fiillerinde yapılır.",
     "İzaha davet takdir komisyonuna sevkten sonra yapılır."],
    "Md. 370/a'ya göre vergi incelemesine başlanılmadan veya takdir komisyonuna sevk edilmeden önce, verginin ziyaa uğradığına "
    "delalet eden emarelere ilişkin ön tespitler hakkında tespit tarihine kadar ihbarda bulunulmamışsa mükellefler izaha "
    "davet edilebilir.")

P.q("VUK md. 371",
    "Bay (F), incelemeye başlanmadan önce eksik beyan ettiği geliri dilekçeyle haber vermiş, 15 gün içinde düzeltme "
    f"beyannamesi vermiş ancak vergiyi 25. günde ödemiştir.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Ödeme 15 gün içinde yapılmadığından pişmanlık şartları sağlanmamıştır.",
    ["Beyanname süresinde verildiğinden pişmanlık şartları sağlanmıştır.",
     "Ödemenin gecikmesi sadece pişmanlık zammını artırır.",
     "Pişmanlıkta ödeme için süre öngörülmemiştir.",
     "Pişmanlık hükümleri eksik beyanda uygulanmaz."],
    "Md. 371/5'e göre haber verilen ve ödeme süresi geçmiş vergilerin pişmanlık zammıyla birlikte haber verme tarihinden "
    "başlayarak on beş gün içinde ödenmesi şarttır; ödeme süresinde yapılmazsa pişmanlıktan yararlanılamaz.", zorluk="hard")

P.sayisal("VUK md. 336",
    "(TUV) Ltd. Şti.’nin tek bir fiili hem 30.000 ₺ vergi ziyaı cezasını hem de 5.000 ₺ usulsüzlük cezasını gerektirmektedir."
    f"\n\n{V}, bu fiil nedeniyle kesilecek ceza toplamı kaç ₺’dir?",
    tl(30_000), secenekler(30_000, 35_000, 5_000, 17_500, 25_000),
    "Md. 336'ya göre cezayı gerektiren tek bir fiil ile vergi ziyaı ve usulsüzlük birlikte işlenmişse bunlara ait cezalardan "
    "sadece miktar itibarıyla en ağırı kesilir: 30.000 ₺.")

P.q("VUK md. 344",
    f"{V}, kayıt dışı faaliyet nedeniyle ceza artırımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sonraki tarhiyatlarda da artırım uygulanır.",
    ["Artırım sadece ilk tarhiyatta uygulanır.",
     "Artırım oranı yüzde yirmi beştir.",
     "Artırım sadece kaçakçılık fiillerinde uygulanır.",
     "Artırım mükellefiyet tesis ettirmiş olanlara uygulanır."],
    "Md. 344/4'e göre mükellefiyet tesis ettirmeden vergi dairesinin ıttılaı dışında faaliyette bulunarak vergi ziyaına "
    "sebebiyet verilmesinde ceza yüzde elli artırılır; aynı vergi türü ve dönemine ilişkin sonraki tarhiyatlarda kesilecek "
    "cezalara da aynı artırım uygulanır.", zorluk="hard")

P.sayisal("VUK md. 374",
    f"Bay (S)’nin 2021 yılında doğan vergi alacağına bağlı olarak vergi ziyaı cezası kesilmesi gerekmektedir.\n\n{V}, bu ceza "
    "en geç hangi yılın sonuna kadar kesilebilir?",
    "2026", ["2023", "2025", "2027", "2031"],
    "Md. 374/1'e göre vergi ziyaı cezasında zamanaşımı, cezanın bağlı olduğu vergi alacağının doğduğu takvim yılını takip "
    "eden yılın birinci gününden başlayarak beş yıldır: 2022-2026.")

P.q("VUK md. 359/c",
    f"{V}, Maliye Bakanlığı ile anlaşması olmadığı hâlde belge basanlar hakkında aşağıdakilerden hangisi doğrudur?",
    "İki yıldan sekiz yıla kadar hapis cezası öngörülmüştür.",
    ["Sadece özel usulsüzlük cezası kesilir.",
     "Bir yıldan üç yıla kadar hapis cezası öngörülmüştür.",
     "Sadece bu belgeleri kullananlar cezalandırılır.",
     "Fiil vergi ziyaı cezası gerektirir, hapis öngörülmemiştir."],
    "Md. 359/c'ye göre ancak Bakanlıkla anlaşması bulunan kişilerin basabileceği belgeleri anlaşma olmadan basanlar veya "
    "bilerek kullananlar iki yıldan sekiz yıla kadar hapis cezası ile cezalandırılır.")

P.sayisal("VUK md. 374",
    f"(VYZ) A.Ş. 2025 yılında Kanunun 352. maddesindeki bir usulsüzlüğü işlemiştir.\n\n{V}, bu usulsüzlük cezası en geç "
    "hangi yılın sonuna kadar kesilebilir?",
    "2027", ["2026", "2028", "2030", "2031"],
    "Md. 374/2'ye göre usulsüzlükte zamanaşımı, usulsüzlüğün yapıldığı yılı takip eden yılın birinci gününden başlayarak "
    "iki yıldır: 2026-2027. Md. 353 ve mük. 355'teki özel usulsüzlüklerde ise süre beş yıldır.", zorluk="hard")

P.q("VUK md. 367",
    f"Bir vergi incelemesinde kaçakçılık suçu oluşturan fiiller tespit edilmiş ve ceza sürecinin nasıl işleyeceği değerlendirilmektedir.\n\n{V}, kaçakçılık suçlarında kovuşturmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kamu davası, inceleme sonucu beklenmeden açılır.",
    ["Suçun tespitinde vergi müfettişleri başsavcılığa bildirimde bulunmakla yükümlüdür.",
     "Başsavcılık başka yolla öğrendiğinde vergi dairesinden inceleme talep eder.",
     "Bildirim, rapor değerlendirme komisyonunun mütalaasıyla yapılır.",
     "Belirli suçlarda inceleme tamamlanmadan da bildirim yapılabilir."],
    "Md. 367'ye göre kamu davasının açılması, inceleme neticesinin Cumhuriyet başsavcılığına bildirilmesine talik olunur; md. "
    "359/ç ve d'deki suçlarda ise inceleme tamamlanmadan bildirim yapılabilir.", zorluk="hard")

P.sayisal("VUK md. 374",
    f"(ZAB) Ltd. Şti. 2024 yılında fatura vermeme fiilini işlemiştir.\n\n{V}, bu fiil için kesilecek özel usulsüzlük cezası en "
    "geç hangi yılın sonuna kadar kesilebilir?",
    "2029", ["2026", "2027", "2028", "2030"],
    "Md. 374/1'e göre md. 353 uyarınca kesilecek usulsüzlük cezalarında zamanaşımı, usulsüzlüğün yapıldığı yılı takip eden "
    "yılın birinci gününden başlayarak beş yıldır: 2025-2029.", zorluk="hard")

P.q("VUK md. 371",
    f"Eksik beyanda bulunduğunu fark eden bir mükellef, pişmanlık dilekçesini ne zamana kadar verebileceğini araştırmaktadır.\n\n{V}, pişmanlık için haber vermenin zamanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Haber verme, ilgili vergi türüne ilişkin incelemeye başlanmadan önce yapılmalıdır.",
    ["Haber verme vergi incelemesi sürerken de yapılabilir.",
     "Haber verme takdir komisyonuna sevkten sonra yapılabilir.",
     "Haber verme için süre sınırı yoktur.",
     "Haber verme sadece yıl sonunda yapılabilir."],
    "Md. 371/2'ye göre haber verme dilekçesinin, haber verilen olayın ilgili olduğu vergi türüne ilişkin incelemeye "
    "başlandığı veya olayın takdir komisyonuna intikal ettirildiği günden (kaçakçılıkta fiilin tespitinden) önce verilmiş ve "
    "resmî kayıtlara geçmiş olması gerekir.")

P.sayisal("VUK md. 371",
    "Bay (T), 2025 yılı gelir vergisi beyannamesini hiç vermediğini 10 Mayıs 2026’da dilekçeyle vergi dairesine kendiliğinden "
    f"haber vermiştir.\n\n{V}, pişmanlıktan yararlanabilmesi için beyannameyi haber verme tarihinden itibaren en geç kaç "
    "gün içinde vermelidir?",
    "15", ["7", "10", "30", "60"],
    "Md. 371/3'e göre hiç verilmemiş olan vergi beyannamelerinin haber verme dilekçesinin verildiği tarihten başlayarak on beş "
    "gün içinde verilmesi gerekir.", zorluk="easy")

P.q("VUK md. 374, 114",
    f"Bir vergi dairesi, takdir komisyonuna sevk ettiği bir mükellefe ilişkin cezaların hâlâ kesilip kesilemeyeceğini değerlendirmektedir.\n\n{V}, ceza zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Takdir komisyonuna başvuru, vergi ziyaı cezası zamanaşımını da durdurur.",
    ["Takdir komisyonuna başvuru ceza zamanaşımını etkilemez.",
     "Ceza zamanaşımı ihbarname tebliği ile kesilmez.",
     "Vergi ziyaı cezası zamanaşımı iki yıldır.",
     "Ceza zamanaşımı cezanın kesinleşmesinden itibaren başlar."],
    "Md. 374/1'e göre md. 114'ün ikinci fıkrası (takdir komisyonuna başvurunun zamanaşımını durdurması) ceza zamanaşımı için "
    "de geçerlidir; süreler içinde ceza ihbarnamesinin tebliğiyle zamanaşımı kesilir.", zorluk="hard")

P.sayisal("VUK md. 370",
    "(CDE) A.Ş.’ye, vergi ziyaına delalet eden bir ön tespite ilişkin izaha davet yazısı tebliğ edilmiştir."
    f"\n\n{V}, şirketin izahta bulunması için izaha davet yazısının tebliğinden itibaren kaç günlük süresi vardır?",
    "30", ["7", "15", "45", "60"],
    "Md. 370/a'ya göre izaha davet yazısının tebliğ tarihinden itibaren otuz günlük süre içinde izahta bulunulabilir; izah "
    "yetersiz bulunursa değerlendirme yazısının tebliğinden itibaren otuz gün içinde beyan tamamlanır.")

P.q("VUK md. 339",
    "Bay (C)’ye kesilen usulsüzlük cezası 15 Mart 2024’te kesinleşmiştir. 2026 yılının Kasım ayında yeniden usulsüzlük "
    f"cezası kesilecektir.\n\n{V}, bu yeni cezada tekerrür hükmü uygulanır mı?",
    "Evet; süre 2026 yılı sonuna kadar olduğundan %25 artırım uygulanır.",
    ["Hayır; usulsüzlükte tekerrür uygulanmaz.",
     "Hayır; tekerrür süresi bir yıldır.",
     "Evet; %50 artırım uygulanır.",
     "Hayır; tekerrür süresi 2025 sonunda dolmuştur."],
    "Md. 339'a göre usulsüzlükte cezanın kesinleştiği tarihi izleyen günden itibaren ikinci yılın isabet ettiği takvim yılı "
    "sonuna kadar tekrar ceza kesilirse %25 artırım uygulanır: 16 Mart 2024'ten itibaren ikinci yıl 2026'ya isabet eder, süre "
    "2026 sonuna kadardır.", zorluk="hard")

P.sayisal("VUK md. 359",
    "Defter kayıtlarında hesap hilesi yaptığı ve muhteviyatı itibarıyla yanıltıcı belge kullandığı tespit edilen Bay (U) "
    f"hakkında kamu davası açılmıştır.\n\n{V}, bu fiiller için öngörülen hapis cezasının alt sınırı kaç aydır?",
    "18", ["6", "12", "24", "36"],
    "Md. 359/a'ya göre defter ve kayıtlarda hesap hileleri yapanlar ile muhteviyatı itibarıyla yanıltıcı belge düzenleyen veya "
    "kullananlar hakkında on sekiz aydan beş yıla kadar hapis cezasına hükmolunur.")

P.q("VUK md. 341",
    "Mükellef Bay (D), gelir vergisi beyannamesinde bekâr olduğu hâlde evli gibi göstererek bazı indirimlerden haksız "
    f"yararlanmış ve vergisi eksik tahakkuk etmiştir.\n\n{V}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Medeni hâle ilişkin gerçeğe aykırı beyan vergi ziyaı hükmündedir.",
    ["Medeni hâl beyanı usul hükmü olduğundan sadece usulsüzlük cezası kesilir.",
     "Vergi sonradan tahakkuk ettirilirse ceza kesilmez.",
     "Beyan mükellefin kendi bilgisi olduğundan ceza kesilemez.",
     "Durum kaçakçılık suçu olarak hapis cezası gerektirir."],
    "Md. 341'e göre şahsi, medeni hâller veya aile durumu hakkında gerçeğe aykırı beyanlarla verginin noksan tahakkukuna "
    "sebebiyet vermek vergi ziyaı hükmündedir; verginin sonradan tahakkuku ceza uygulanmasına engel değildir.")

P.sayisal("VUK md. 376",
    "(PRS) Ltd. Şti. adına vergi aslına bağlı olmaksızın 6.000 ₺ usulsüzlük cezası kesilmiştir. Şirket ihbarnamenin "
    "tebliğinden itibaren 30 gün içinde başvurarak cezanın indirimli kısmını vadesinde ödeyeceğini bildirmiş ve ödemiştir."
    f"\n\n{V26}, şirketin ödediği ceza tutarı kaç ₺’dir?",
    tl(3_000), secenekler(3_000, 6_000, 4_000, 2_000, 1_500),
    "Md. 376'ya göre indirim hükümleri vergi aslına bağlı olmaksızın kesilen usulsüzlük cezaları hakkında da uygulanır; "
    "cezanın yarısı indirilir: 6.000 / 2 = 3.000 ₺.")

P.q("VUK md. 352",
    f"Bir mükellef nezdinde tespit edilen usulsüzlük nedeniyle kesilecek cezanın tutarı belirlenmektedir.\n\n{V}, usulsüzlük cezasının iki kat kesilmesini gerektiren hâl aşağıdakilerden hangisidir?",
    "Usulsüzlük fiilinin resen takdiri gerektirmesi",
    ["Usulsüzlüğün ilk defa işlenmesi",
     "Usulsüzlüğün mücbir sebeple işlenmesi",
     "Usulsüzlüğün pişmanlıkla bildirilmesi",
     "Usulsüzlüğün aynı yıl içinde tekrarı"],
    "Md. 352'ye göre usulsüzlük fiili resen takdiri gerektirirse 1 sayılı cetvelde yazılı cezalar iki kat olarak kesilir. "
    "Aynı yıl içindeki tekrarlarda md. 337'ye göre dörtte bir, tekerrürde md. 339'a göre %25 artırım uygulanır.")

pz = 100_000 * 0.037 * 3
P.sayisal("VUK md. 371",
    "Bayan (B), 2026 yılında pişmanlıkla eksik beyanını düzeltmiş ve ödeme süresi üç ay önce geçmiş 100.000 ₺ vergiyi "
    "haber verme tarihinden itibaren 15 gün içinde ödemiştir. (Aylık gecikme zammı oranı %3,7 olarak alınacak, ay kesri "
    f"bulunmamaktadır.)\n\n{V26}, Bayan (B)’nin vergiyle birlikte ödeyeceği pişmanlık zammı kaç ₺’dir?",
    tl(pz), secenekler(pz, 3_700, 100_000 * 0.037 * 4, 20_000, 100_000 * 0.04 * 3),
    "Md. 371/5'e göre vergi, ödemenin geciktiği her ay ve kesri için 6183 sayılı Kanunun 51. maddesindeki gecikme zammı "
    "oranında bir zamla ödenir: 100.000 × %3,7 × 3 = 11.100 ₺.")

P.q("VUK md. 376",
    "(GHI) A.Ş., adına kesilen vergi ziyaı cezası için 376. madde uyarınca indirim talebinde bulunmuş, ardından aynı "
    f"tarhiyata karşı dava açmıştır.\n\n{V26}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Dava konusu yapıldığından indirimden yararlanamaz.",
    ["İndirim talebi dava açılmasına rağmen korunur.",
     "Dava sonuçlanana kadar indirim askıya alınır.",
     "Dava açıldığında indirim oranı üçte bire düşer.",
     "Sadece vergi aslı için dava açılabilir, ceza indirimi korunur."],
    "Md. 376'ya göre indirim talebinde bulunan mükellef tarhiyatı dava konusu yaparsa indirim hükmünden faydalandırılmaz; "
    "indirim, vergi ve indirimli cezanın süresinde ödenmesi ve tarhiyatın dava konusu yapılmaması şartına bağlıdır.")

iz = 50_000 * 0.037 * 2 + 50_000 * 0.20
P.sayisal("VUK md. 370",
    "İzahı yeterli bulunmayan (TUV) A.Ş., 30 gün içinde beyanını düzeltmiş ve ödeme süresi iki ay önce geçmiş 50.000 ₺ vergiyi "
    "izah zammıyla ödemiştir. (Aylık gecikme zammı oranı %3,7 olarak alınacak, ay kesri bulunmamaktadır.)"
    f"\n\n{V26}, şirketin ödeyeceği izah zammı ile kesilecek vergi ziyaı cezasının toplamı kaç ₺’dir?",
    tl(iz), secenekler(iz, 50_000 * 0.20, 3_700, 50_000 * 0.50 + 3_700, 50_000 + 3_700),
    "Md. 370/a-2'ye göre vergi, gecikme zammı oranında izah zammıyla ödenir (50.000 × %3,7 × 2 = 3.700 ₺) ve vergi ziyaı "
    "cezası %20 oranında kesilir (10.000 ₺): toplam 13.700 ₺.", zorluk="hard")

P.q("VUK md. 344",
    "Bay (E), bir mükellefin sahte fatura düzenlemesine yardım ederek bu fiile iştirak etmiştir. Asıl mükellef nezdinde "
    f"100.000 ₺ vergi ziyaa uğramıştır.\n\n{V26}, Bay (E)’ye kesilecek vergi ziyaı cezası hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "Ceza bir kat olarak uygulanır.",
    ["Ceza üç kat olarak uygulanır.",
     "İştirak edenlere ceza kesilmez.",
     "Ceza yüzde elli oranında uygulanır.",
     "Ceza iki kat olarak uygulanır."],
    "Md. 344/2'ye göre vergi ziyaına md. 359'daki fiillerle sebebiyet verilmesi hâlinde ceza üç kat, bu fiillere iştirak "
    "edenlere ise bir kat olarak uygulanır.")

tk2 = 50_000 * 1.5
P.sayisal("VUK md. 339",
    "(JKL) Ltd. Şti.’ye 2022 yılında kesilen 100.000 ₺ vergi ziyaı cezası 2023 yılında kesinleşmiştir. Şirkete 2026 yılında "
    f"yeniden 50.000 ₺ vergi ziyaı cezası kesilecektir.\n\n{V}, tekerrür hükmü uygulanarak kesilecek vergi ziyaı cezası kaç "
    "₺’dir?",
    tl(tk2), secenekler(tk2, 50_000, 150_000, 62_500, 100_000),
    "Md. 339'a göre vergi ziyaı cezası kesinleşme tarihini izleyen günden itibaren beşinci yılın isabet ettiği takvim yılı "
    "sonuna kadar yeniden ceza kesilirse %50 artırılır; artırım (25.000 ₺) önceki kesinleşen cezayı aşmadığından tamamı "
    "uygulanır: 50.000 × 1,5 = 75.000 ₺.")

if __name__ == "__main__":
    sys.exit(P.yaz())
