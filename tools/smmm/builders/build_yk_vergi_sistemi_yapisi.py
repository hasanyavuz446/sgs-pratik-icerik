# -*- coding: utf-8 -*-
"""Vergi · Türk Vergi Sistemi · Diğer Vergiler (VİV, Emlak, Damga, MTV, ÖTV) — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında bu konu; damga vergisinde nüsha ve çoklu işlem kuralları, VİV beyanname süreleri,
MTV istisnaları ve bina vergisi mükellefiyetinin başlangıcı üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 7338 sayılı VİVK md. 1-19; 1319 sayılı EVK md. 1-33;
488 sayılı DVK md. 1-25; 197 sayılı MTVK md. 1-4; 4760 sayılı ÖTVK md. 1-4, 14. Yıla bağlı tarife, istisna ve
azami tutarlar kökte verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_vergi_sistemi_yapisi_2026.json", lesson="turk_vergi_sistemi", topic="vergi_sistemi_yapisi",
          konu_adi="Diğer Vergiler (VİV, Emlak, Damga, MTV, ÖTV)", seed=2026092912,
          surum="VİVK, EVK, DVK, MTVK, ÖTVK güncel metni; tutarlar kökte; 29.09.2026 kontrolü")

VI = "7338 sayılı Veraset ve İntikal Vergisi Kanunu’na göre"
EM = "1319 sayılı Emlak Vergisi Kanunu’na göre"
DA = "488 sayılı Damga Vergisi Kanunu’na göre"
MT = "197 sayılı Motorlu Taşıtlar Vergisi Kanunu’na göre"
OT = "4760 sayılı Özel Tüketim Vergisi Kanunu’na göre"

P.sayisal("VİVK md. 9",
    "Türk vatandaşı Bay (K), 2026 yılının Mart ayında Türkiye’de vefat etmiştir. Tek mirasçısı olan oğlu ölüm tarihinde "
    f"Kanada’da yaşamaktadır.\n\n{VI}, mirasçı veraset ve intikal vergisi beyannamesini ölüm tarihini takip eden kaç ay "
    "içinde vermelidir?",
    "6", ["1", "3", "4", "8"],
    "VİVK md. 9/1-a'ya göre ölüm Türkiye'de vuku bulmuşsa mükellefler Türkiye'de ise dört ay, yabancı bir memlekette ise altı "
    "ay içinde beyanname verir.", zorluk="hard")

P.q("VİVK md. 1",
    f"Bir vergi dairesi, vefat eden bir mükellefin mirasçılarına intikal eden mal ve hakların hangilerinin vergiye tabi olduğunu incelemektedir.\n\n{VI}, aşağıdakilerden hangisi veraset ve intikal vergisinin konusuna girmez?",
    "Türkiye’de ikametgâhı olmayan yabancının Türk vatandaşından yurt dışındaki malı ivazsız iktisabı",
    ["Türk vatandaşının yabancı bir ülkede ölen babasından miras yoluyla yurt dışındaki bir evi iktisabı",
     "Türkiye’de bulunan bir dairenin bağış yoluyla intikali",
     "Türk vatandaşından veraset yoluyla Türkiye’deki bir arsanın intikali",
     "Türkiye’deki bir banka hesabındaki paranın bağış yoluyla anneden çocuğa devri"],
    "VİVK md. 1'e göre Türk vatandaşlarına ait mallar ile Türkiye'deki malların veraset veya ivazsız intikali vergiye tabidir; "
    "ancak Türk vatandaşının Türkiye dışındaki malını ivazsız iktisap eden ve Türkiye'de ikametgâhı olmayan yabancı mükellef "
    "tutulmaz.", zorluk="hard")

P.q("VİVK md. 3",
    f"Bir vergi dairesi, vefat eden bir mükellefin mirasçılarına intikal eden mal ve hakların hangilerinin vergiye tabi olduğunu incelemektedir.\n\n{VI}, aşağıdakilerden hangisi veraset ve intikal vergisinden muaf değildir?",
    "Kurumlar vergisine tabi olan bir anonim şirket",
    ["Siyasi partiler",
     "Umumi menfaate hadim cemiyetler",
     "Sosyal sigorta kurumları",
     "Bilim ve eğitim amacıyla kurulan teşekküller"],
    "VİVK md. 3'e göre amme idareleri, sosyal sigorta kurumları, umumi menfaate hadim cemiyetler, siyasi partiler ve bunlara "
    "ait kurumlar vergisine tabi olmayan teşekküller ile ilim, eğitim gibi amaçlarla kurulan teşekküller muaftır.")

P.sayisal("VİVK md. 9",
    "Türk vatandaşı Bayan (L), Fransa’da yaşarken 2026 yılında Fransa’da vefat etmiştir. Mirasçısı olan kızı ise Almanya’da "
    f"yaşamaktadır.\n\n{VI}, beyanname ölüm tarihini takip eden kaç ay içinde verilmelidir?",
    "8", ["1", "4", "6", "12"],
    "VİVK md. 9/1-b'ye göre ölüm yabancı memlekette vuku bulmuşsa mükellefler Türkiye'de ise altı, ölenin bulunduğu memlekette "
    "ise dört, ölenin bulunduğu yerin dışında başka bir yabancı memlekette ise sekiz ay içinde beyanname verir.",
    zorluk="hard")

P.q("VİVK md. 4",
    f"Bir vergi dairesi, vefat eden bir mükellefin mirasçılarına intikal eden mal ve hakların hangilerinin vergiye tabi olduğunu incelemektedir.\n\n{VI}, aşağıdakilerden hangisi vergiden istisna değildir?",
    "Miras kalan kiralık işyeri",
    ["Veraset yoluyla intikal eden ev eşyası",
     "Aile hatırası olarak saklanan madalya",
     "Örf ve adete göre verilen yüzgörümlüğü",
     "Bilumum sadakalar"],
    "VİVK md. 4'e göre veraset yoluyla intikal eden ev eşyası ve aile hatırası eşya, örf ve adete göre verilen hediye ve "
    "yüzgörümlükleri (gayrimenkuller hariç) ve sadakalar istisnadır; işyeri gibi gayrimenkuller istisna tutarı dışında "
    "vergiye tabidir.", zorluk="easy")

P.q("VİVK md. 10-11",
    f"Vefat eden bir tüccarın mirasçıları, veraset ve intikal vergisi beyannamesinde malları hangi tarihteki değerleriyle göstereceklerini sormaktadır.\n\n{VI}, matrah ve değerlemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Veraset yoluyla intikallerde değerleme günü beyannamenin verildiği gündür.",
    ["Matrah, intikal eden malların VUK’a göre bulunan değerleridir.",
     "Tenzili gereken borç ve masraflar değerden düşülür.",
     "Diğer intikallerde değerleme günü malların hukuken iktisap edildiği gündür.",
     "Bilanço esasında ticari sermaye öz sermaye olarak dikkate alınır."],
    "VİVK md. 11'e göre değerleme günü, miras yoluyla intikallerde mirasın açıldığı gün, diğer intikallerde malların hukuken "
    "iktisap edildiği gündür.", zorluk="hard")

P.sayisal("VİVK md. 9",
    f"Uzun süredir haber alınamayan Bay (M) hakkında verilen gaiplik kararı ölüm siciline kaydedilmiştir.\n\n{VI}, "
    "mirasçılar beyannameyi gaiplik kararının ölüm siciline kaydolunduğu tarihi takip eden kaç ay içinde vermelidir?",
    "1", ["2", "3", "4", "6"],
    "VİVK md. 9/1-c'ye göre gaiplik hâlinde beyanname, gaiplik kararının ölüm siciline kaydolunduğu tarihi takip eden bir ay "
    "içinde verilir.")

P.q("VİVK md. 12",
    f"{VI}, veraset yoluyla intikallerde matrahtan indirilebilecek borçlar arasında aşağıdakilerden hangisi yer alır?",
    "Murisin belgeli borçları ile vergi borçları",
    ["Mirasçının kendi kredi kartı borçları",
     "Mirasçının şahsi vergi borçları",
     "Mirasçıların ileride yapacakları tadilat giderleri",
     "Mirasçıya ait işletmenin ticari borçları"],
    "VİVK md. 12/a'ya göre veraset yoluyla intikallerde murisin ispata elverişli belgelere dayanan borçları ile vergi borçları, "
    "beyannamede gösterilmek şartıyla indirilir.")

P.q("VİVK md. 6, 8",
    "Son ikametgâhı İzmir olan Bay (B), Almanya’da ikamet ederken vefat etmiştir; mirasçılar Türkiye’dedir."
    f"\n\n{VI}, vergi hangi yerin vergi dairesince tarh olunur?",
    "Murisin Türkiye’deki son ikametgâhının yerinin",
    ["Mirasçıların ikametgâhının bulunduğu yerin",
     "Almanya’daki Türkiye konsolosluğunun",
     "Mirasa konu malların en değerlisinin bulunduğu yerin",
     "Mirasçıların seçeceği herhangi bir yerin"],
    "VİVK md. 6'ya göre veraset yoluyla intikallerde vergi ölenin ikametgâhının bulunduğu yerin vergi dairesince tarh olunur; "
    "ikametgâh yabancı memlekette ise Türkiye'deki son ikametgâhının bulunduğu yerin vergi dairesi yetkilidir.",
    zorluk="hard")

tk = 600_000 / 6
P.sayisal("VİVK md. 19",
    "Mirasçı Bayan (N) adına 2026 yılında 600.000 ₺ veraset ve intikal vergisi tahakkuk etmiştir. Bayan (N) vergiyi Kanunda "
    f"öngörülen taksitlerle ödemek istemektedir.\n\n{VI}, her bir taksit tutarı kaç ₺’dir?",
    tl(tk), secenekler(tk, 300_000, 200_000, 150_000, 50_000),
    "VİVK md. 19'a göre veraset ve intikal vergisi tahakkukundan itibaren üç yılda ve her yıl Mayıs ve Kasım aylarında iki "
    "eşit taksitte ödenir: toplam altı taksit; 600.000 / 6 = 100.000 ₺.")

P.q("VİVK md. 7",
    f"Bir vakıf ile bir şans oyunu ikramiyesi kazanan kişi, ivazsız iktisapları için beyanname verip vermeyeceklerini sormaktadır.\n\n{VI}, beyanname verme yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Muaf olan kurumlar muaf oldukları iktisaplar için beyanname vermez.",
    ["İstisna kapsamındaki ev eşyası için de beyanname verilmesi şarttır.",
     "Şans oyunu ikramiyesi tevkifata tabi tutulan kişi ayrıca beyanname verir.",
     "Beyanname sadece noter aracılığıyla verilebilir.",
     "Mirasçılar birlikte beyanname veremez, her biri ayrı verir."],
    "VİVK md. 7'ye göre md. 3'teki muaf şahıslar ile tevkifata tabi tutulan ikramiyeler için beyanname verilmez; md. 8'e göre "
    "beyanname her mükellef için ayrı veya müştereken verilebilir.")

P.q("EVK md. 2",
    f"Bir belediye emlak servisi, sahil şeridindeki çeşitli yapıların bina vergisine tabi olup olmadığını belirlemek için yerinde tespit yapmıştır.\n\n{EM}, aşağıdakilerden hangisi bina sayılmaz?",
    "Nakil vasıtasına takılıp çekilebilen seyyar ev",
    ["Su üzerindeki sabit bir restoran yapısı",
     "Betonarme bir apartman dairesi",
     "Ahşap olarak inşa edilmiş sabit bir dağ evi",
     "Bina mütemmimleri ile birlikte bir fabrika binası"],
    "EVK md. 2'ye göre bina, yapıldığı madde ne olursa olsun karada veya su üzerindeki sabit inşaatın hepsidir; yüzer havuzlar, "
    "yüzer yapılar, çadırlar ve nakil vasıtalarına takılıp çekilebilen seyyar evler bina sayılmaz.")

v1 = (5_000_000 - 2_000_000) * 0.01
P.sayisal("VİVK md. 4, 16",
    "Bay (P), 2026 yılında vefat eden babasından veraset yoluyla 5.000.000 ₺ değerinde miras hissesi almıştır. (Füruğa isabet "
    "eden miras hissesi istisnası 2.000.000 ₺; veraset yoluyla intikallerde ilk 3.000.000 ₺ için oran %1, sonra gelen "
    f"7.000.000 ₺ için %3 olarak alınacaktır.)\n\n{VI}, Bay (P)’nin ödeyeceği veraset ve intikal vergisi kaç ₺’dir?",
    tl(v1), secenekler(v1, 5_000_000 * 0.01, 60_000, 3_000_000 * 0.03, 50_000 + 30_000),
    "VİVK md. 4/b'ye göre füruğa isabet eden miras hissesinin Kanundaki tutarı istisnadır: matrah 5.000.000 − 2.000.000 = "
    "3.000.000 ₺. Md. 16 tarifesine göre ilk 3.000.000 ₺ %1: 30.000 ₺.")

P.q("EVK md. 3",
    "Bir dairenin çıplak mülkiyeti Bay (C)’ye, intifa hakkı ise annesi Bayan (D)’ye aittir."
    f"\n\n{EM}, bu dairenin bina vergisi mükellefi kimdir?",
    "İntifa hakkı sahibi Bayan (D)",
    ["Çıplak mülkiyet sahibi Bay (C)",
     "Bay (C) ve Bayan (D) müteselsilen",
     "Dairede kiracı olarak oturan kişi",
     "Binanın bulunduğu yerin belediyesi"],
    "EVK md. 3'e göre bina vergisini binanın maliki, varsa intifa hakkı sahibi, her ikisi de yoksa binaya malik gibi tasarruf "
    "edenler öder; intifa hakkı varsa mükellef intifa hakkı sahibidir.", zorluk="hard")

P.q("EVK md. 3",
    f"Bir apartman dairesi üç kardeşe miras kalmış; kardeşlerin bir kısmı paylı, bir kısmı elbirliği mülkiyeti esasında hak sahibidir.\n\n{EM}, bina vergisi mükellefiyetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Elbirliği mülkiyette malikler hisseleri oranında sorumludur.",
    ["Paylı mülkiyette malikler hisseleri oranında mükelleftir.",
     "Malik ve intifa hakkı sahibi yoksa malik gibi tasarruf eden öder.",
     "İntifa hakkı varsa vergiyi intifa hakkı sahibi öder.",
     "Bina vergisini kural olarak binanın maliki öder."],
    "EVK md. 3'e göre paylı mülkiyette malikler hisseleri oranında mükelleftir; elbirliği mülkiyette ise malikler vergiden "
    "müteselsilen sorumludur.")

v2 = 3_000_000 * 0.01 + 2_000_000 * 0.03
P.sayisal("VİVK md. 16",
    "Bayan (R)’nin veraset yoluyla intikal eden mallar için istisna düşüldükten sonra kalan matrahı 5.000.000 ₺’dir. "
    "(Veraset yoluyla intikallerde ilk 3.000.000 ₺ için oran %1, sonra gelen 7.000.000 ₺ için %3 olarak alınacaktır.)"
    f"\n\n{VI}, Bayan (R)’nin ödeyeceği vergi kaç ₺’dir?",
    tl(v2), secenekler(v2, 5_000_000 * 0.01, 5_000_000 * 0.03, 30_000, 120_000),
    "VİVK md. 16 artan oranlı tarifeye göre ilk 3.000.000 ₺ için %1 (30.000 ₺), kalan 2.000.000 ₺ için %3 (60.000 ₺) "
    "uygulanır: toplam 90.000 ₺.", zorluk="hard")

P.q("EVK md. 4",
    f"Bir belediye, kamu kurumlarına ve derneklere ait olup kiraya verilen binaların bina vergisi muafiyetini yeniden incelemektedir.\n\n{EM}, aşağıdaki binalardan hangisi kiraya verilse de bina vergisinden daimi olarak muaftır?",
    "Devlete ait bina",
    ["Dernek lokali olarak kullanılan bina",
     "Vakfa ait yurt binası",
     "İbadethane olarak kullanılan bina",
     "Kamu yararına çalışan derneğe ait bina"],
    "EVK md. 4'e göre daimi muaflıklar kiraya verilmeme şartına bağlıdır; ancak (a) bendindeki Devlet, belediye, köy tüzel "
    "kişiliği ve üniversitelere ait binalar ile bazı bentler için bu şart aranmaz.", zorluk="hard")

P.q("EVK md. 23",
    f"Yeni bir konut inşaatını tamamlayan bir mükellef, emlak vergisi bildirimini ne zaman ve hangi kuruma vereceğini araştırmaktadır.\n\n{EM}, emlak vergisi bildirimine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İnşaatın bittiği bütçe yılı içinde bildirim verilir.",
    ["Bildirim her yıl yenilenmekir.",
     "Devlete ait arazi için de bildirim verilir.",
     "Bildirim, emlakin bulunduğu yerdeki vergi dairesine verilir.",
     "Bildirim sadece bina satıldığında verilir."],
    "EVK md. 23'e göre vergi değerini tadil eden nedenlerin bulunması hâlinde bildirim verilir; yeni binalar için inşaatın sona "
    "erdiği bütçe yılı içinde, emlakin bulunduğu yerdeki belediyeye verilir; Devlete ait arazi için bildirim verilmez.")

v3 = (500_000 - 60_000) * 0.10 / 2
P.sayisal("VİVK md. 16",
    "Bayan (S), 2026 yılında annesinden bağış yoluyla 500.000 ₺ nakit almıştır. (İvazsız intikaller için istisna tutarı "
    f"60.000 ₺, ivazsız intikallerde ilk dilim oranı %10 olarak alınacaktır.)\n\n{VI}, Bayan (S)’nin ödeyeceği vergi kaç "
    "₺’dir?",
    tl(v3), secenekler(v3, 440_000 * 0.10, 500_000 * 0.05, 440_000 * 0.01, 500_000 * 0.10),
    "VİVK md. 4/d'ye göre ivazsız intikallerin Kanundaki tutarı istisnadır: matrah 440.000 ₺. Md. 16'ya göre ana, baba, eş ve "
    "çocuklardan ivazsız intikalde ivazsız intikal oranlarının yarısı uygulanır: 440.000 × %5 = 22.000 ₺.", zorluk="hard")

P.q("EVK md. 30",
    f"Bir mükellef, adına tahakkuk eden yıllık emlak vergisini hangi aylarda ve kaç taksitte ödeyebileceğini sormaktadır.\n\n{EM}, emlak vergisinin ödeme zamanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlk taksit Mart-Mayıs, ikinci taksit Kasım’da ödenir.",
    ["Vergi tek seferde Ocak ayında ödenir.",
     "Birinci taksit Ocak, ikinci taksit Temmuz ayında ödenir.",
     "Vergi dört eşit taksitte ödenir.",
     "Birinci taksit Mayıs, ikinci taksit Ekim ayında ödenir."],
    "EVK md. 30'a göre emlak vergisinin birinci taksidi Mart, Nisan ve Mayıs aylarında, ikinci taksidi Kasım ayında olmak üzere "
    "iki eşit taksitte ödenir.")

P.q("EVK md. 12",
    f"Bir belediye, sınırları içindeki boş alanların arazi mi arsa mı sayılacağını ve buna göre hangi oranın uygulanacağını belirlemektedir.\n\n{EM}, arazi ve arsa ayrımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Belediyece parsellenmiş arazi arsa sayılır.",
    ["Belediye sınırları dışındaki tüm araziler arsa sayılır.",
     "Arsa tanımı sadece büyükşehirlerde uygulanır.",
     "Tarım yapılan her arazi arsadır.",
     "Parsellenmemiş arazi kural gereği arsa sayılmaz."],
    "EVK md. 12'ye göre belediye sınırları içinde belediyece parsellenmiş arazi arsa sayılır; parsellenmemiş araziden hangilerinin "
    "arsa sayılacağı Cumhurbaşkanı kararıyla belirlenir.")

tv = 400_000 * 0.05
P.sayisal("VİVK md. 17",
    "Bir banka, vefat eden müşterisinin hesabındaki 400.000 ₺’yi mirasçısına ödemek istemektedir. Mirasçı, veraset ve "
    f"intikal vergisinin ödendiğine dair tasdikname ibraz edememiştir.\n\n{VI}, bankanın ödeme öncesinde yapacağı vergi "
    "kesintisi kaç ₺’dir?",
    tl(tv), secenekler(tv, 400_000 * 0.15, 400_000 * 0.01, 400_000 * 0.10, 0),
    "VİVK md. 17'ye göre tasdikname ibraz etmeyen hak sahiplerinin istihkaklarından veraset yoluyla intikallerde %5, ivazsız "
    "intikallerde %15 oranında vergi karşılığı tevkifat yapılır: 400.000 × %5 = 20.000 ₺.")

P.q("EVK md. 5",
    f"2025 yılında tamamlanan bir konutun sahibi, yeni binalara tanınan geçici muafiyetten nasıl yararlanacağını sormaktadır.\n\n{EM}, yeni inşa edilen meskenlerde geçici muafiyete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Muafiyet binanın vergi değerinin tamamını kapsar.",
    ["Muafiyet vergi değerinin dörtte birine uygulanır.",
     "Muafiyet beş yıl süreyle uygulanır.",
     "Süre, inşaatın bittiği yılı takip eden bütçe yılından başlar.",
     "Mesken satın alınırsa kalan süre için muafiyet devam eder."],
    "EVK md. 5/a'ya göre mesken olarak kullanılan binaların vergi değerinin 1/4'ü, inşaatın sona erdiği yılı takip eden bütçe "
    "yılından itibaren beş yıl geçici muafiyetten yararlanır; mesken olarak iktisap hâlinde kalan süre için uygulanır.")

P.q("DVK md. 1",
    f"Bir şirket, elektronik imza ile düzenlediği sözleşmelerin damga vergisine tabi olup olmadığını ve kâğıt tanımını araştırmaktadır.\n\n{DA}, damga vergisine tabi “kâğıt” kavramına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Elektronik imzayla oluşturulan belgeler de kâğıt kapsamındadır.",
    ["Sadece noterde düzenlenen belgeler kâğıt sayılır.",
     "İmzasız belgeler de vergiye tabi kâğıttır.",
     "Elektronik ortamdaki belgeler vergiye tabi değildir.",
     "Yurt dışında düzenlenen kâğıtlar kural olarak vergilendirilmez."],
    "DVK md. 1'e göre kâğıt, yazılıp imzalanarak veya imza yerine geçen işaret konularak düzenlenen ve ispat için ibraz "
    "edilebilen belgeler ile elektronik imza kullanılarak elektronik veri şeklinde oluşturulan belgelerdir.")

e1 = 2_000_000 * 0.001 * 2
P.sayisal("EVK md. 8",
    "Bay (T), büyükşehir belediye sınırları içinde bulunan ve mesken olarak kullandığı dairenin sahibidir. Dairenin 2026 "
    f"yılı vergi değeri 2.000.000 ₺’dir; muafiyet veya indirim bulunmamaktadır.\n\n{EM}, Bay (T)’nin 2026 yılı bina vergisi "
    "kaç ₺’dir?",
    tl(e1), secenekler(e1, 2_000, 8_000, 6_000, 1_000),
    "EVK md. 8'e göre bina vergisi oranı meskenlerde binde birdir ve büyükşehir belediye sınırları içinde %100 artırımlı "
    "uygulanır: 2.000.000 × binde 2 = 4.000 ₺.")

P.q("DVK md. 3",
    "Bir belediye ile Bay (E) arasında bir kira sözleşmesi imzalanmıştır; belediye damga vergisinden muaftır."
    f"\n\n{DA}, bu sözleşmenin damga vergisini kim öder?",
    "Bay (E)",
    ["Belediye", "Belediye ve Bay (E) eşit olarak", "Sözleşmeyi onaylayan noter", "Kimse ödemez, işlem istisnadır"],
    "DVK md. 3'e göre damga vergisinin mükellefi kâğıtları imza edenlerdir; resmi dairelerle kişiler arasındaki işlemlere ait "
    "kâğıtların vergisini kişiler öder.", zorluk="easy")

P.q("DVK md. 5-6",
    f"Bir şirketin muhasebe birimi, düzenlediği sözleşmelerin damga vergisini hesaplarken nüsha ve işlem sayısına ilişkin kuralları gözden geçirmektedir.\n\n{DA}, aşağıdaki ifadelerden hangisi yanlıştır?",
    "Nispi vergiye tabi kâğıtların her bir nüshası ayrı ayrı vergiye tabidir.",
    ["Vergiye tabi kâğıtların uzatılmasına ilişkin şerhler vergiye tabidir.",
     "Resmi dairelerle kişiler arasındaki kâğıtların vergisini kişiler öder.",
     "Bir kâğıttaki birbirinden ayrı işlemlerin her birinden ayrı vergi alınır.",
     "Birbirine bağlı işlemlerde en yüksek vergiyi gerektiren işlemden vergi alınır."],
    "DVK md. 5'e göre birden fazla nüsha düzenlenen kâğıtlardan nispi vergiye tabi olanların sadece bir nüshası vergiye tabidir; "
    "maktu vergiye tabi olanların her nüshası ayrı ayrı vergilendirilir.", zorluk="hard")

e2 = 3_000_000 * 0.002
P.sayisal("EVK md. 8",
    "(ABC) Ltd. Şti., büyükşehir belediyesi bulunmayan bir ilçede işyeri olarak kullandığı binanın sahibidir. Binanın vergi "
    f"değeri 3.000.000 ₺’dir.\n\n{EM}, şirketin yıllık bina vergisi kaç ₺’dir?",
    tl(e2), secenekler(e2, 3_000, 12_000, 9_000, 1_500),
    "EVK md. 8'e göre mesken dışındaki binalarda oran binde ikidir; büyükşehir sınırları dışında artırım uygulanmaz: "
    "3.000.000 × binde 2 = 6.000 ₺.")

P.q("DVK md. 6",
    "Bir kâğıtta bir kira sözleşmesi ile buna bağlı olarak kiracının borcuna kefil olan üçüncü bir kişinin kefalet taahhüdü "
    f"yer almaktadır.\n\n{DA}, bu kâğıdın vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Üçüncü kişinin kefaleti ayrıca vergilendirilir.",
    ["Sadece kira sözleşmesinden vergi alınır.",
     "Sadece en düşük vergiyi gerektiren işlemden vergi alınır.",
     "Kefalet taahhüdü damga vergisi dışındadır.",
     "Kâğıt tek işlem sayılır ve maktu vergi alınır."],
    "DVK md. 6'ya göre birbirine bağlı işlemlerde en yüksek vergiyi gerektiren işlemden vergi alınır; ancak asıl işlemin "
    "taraflarından başka bir şahsın eklenen akit ve işlemi (üçüncü kişinin kefaleti) ayrıca vergiye tabidir.", zorluk="hard")

P.q("DVK md. 8",
    f"Bir belediyenin ayrı tüzel kişiliğe sahip su işletmesi, düzenlediği sözleşmelerde resmi daire sayılıp sayılmayacağını sormaktadır.\n\n{DA}, “resmi daire” kavramına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ayrı tüzel kişilikli işletme resmi daire sayılmaz.",
    ["Belediyeye bağlı her türlü şirket resmi dairedir.",
     "Köyler resmi daire sayılmaz.",
     "Sadece genel bütçeli idareler resmi dairedir.",
     "Kamu iktisadi teşebbüsleri kural olarak resmi dairedir."],
    "DVK md. 8'e göre resmi daire; genel ve özel bütçeli idareler, il özel idareleri, yatırım izleme ve koordinasyon "
    "başkanlıkları, belediyeler ve köylerdir; bunlara bağlı olup ayrı tüzel kişiliği bulunan iktisadi işletmeler resmi daire "
    "sayılmaz.")

e3 = 1_500_000 * 0.003 * 2
P.sayisal("EVK md. 18",
    "Bayan (U), büyükşehir belediye sınırları içinde vergi değeri 1.500.000 ₺ olan bir arsanın sahibidir."
    f"\n\n{EM}, Bayan (U)’nun yıllık arazi vergisi kaç ₺’dir?",
    tl(e3), secenekler(e3, 4_500, 3_000, 1_500, 13_500),
    "EVK md. 18'e göre arazi vergisi oranı binde bir, arsalarda binde üçtür; büyükşehir sınırları içinde %100 artırımlı "
    "uygulanır: 1.500.000 × binde 6 = 9.000 ₺.")

P.q("DVK md. 15, 22",
    f"Düzenli olarak çok sayıda sözleşme imzalayan bir şirket, damga vergisini hangi yöntemle ve ne zaman ödeyeceğini belirlemek istemektedir.\n\n{DA}, damga vergisinin ödenmesine ilişkin aşağıdakilerden hangisi yanlıştır?",
    "Makbuz karşılığı ödemede vergi, kâğıdın düzenlendiği yılın sonunda ödenir.",
    ["Vergi makbuz karşılığı, istihkaktan kesinti veya basılı damga yoluyla ödenebilir.",
     "Bakanlıkça belirlenenler bir aylık kâğıtların vergisini beyannameyle bildirir.",
     "Belirlenenler dışında vergi, kâğıdın düzenlendiği tarihten itibaren 15 gün içinde bildirilir.",
     "Ödeme şekillerinin hangi işlemlerde uygulanacağını Bakanlık belirler."],
    "DVK md. 22'ye göre makbuz karşılığı ödemelerde Bakanlıkça belirlenenler bir ay içinde düzenlenen kâğıtların vergisini "
    "ertesi ayın yirminci günü beyan edip yirmi altıncı günü öder; diğer hâllerde kâğıdın düzenlendiği tarihi izleyen on beş "
    "gün içinde beyan edilip ödenir.", zorluk="hard")

P.q("DVK md. 24",
    f"Üç kişinin birlikte imzaladığı bir sözleşmenin damga vergisi eksik ödenmiş ve vergi dairesi tarhiyat yapmayı planlamaktadır.\n\n{DA}, damga vergisindeki sorumluluğa ilişkin aşağıdakilerden hangisi doğrudur?",
    "İmza edenler vergi ve cezadan müteselsilen sorumludur.",
    ["Kâğıdı imza edenlerden sadece ilki sorumludur.",
     "İmza edenlerden birinin muaf olması vergiyi azaltır.",
     "Kâğıdı ibraz edenler kural gereği sorumlu tutulamaz.",
     "Sorumluluk sadece vergi aslı için geçerlidir, cezayı kapsamaz."],
    "DVK md. 24'e göre birden fazla kişi tarafından imza edilen kâğıtların vergi ve cezasının tamamından imza edenler "
    "müteselsilen sorumludur; aralarında muaf olanların bulunması verginin noksan ödenmesini gerektirmez.")

e4 = 12_000 / 3
P.sayisal("EVK md. 13",
    "Üç kardeş bir arsaya paylı mülkiyetle eşit oranda maliktir. Arsanın yıllık arazi vergisi 12.000 ₺’dir."
    f"\n\n{EM}, kardeşlerden birinin mükellef olduğu vergi tutarı kaç ₺’dir?",
    tl(e4), secenekler(e4, 12_000, 6_000, 3_000, 2_000),
    "EVK md. 13'e göre bir araziye paylı mülkiyet hâlinde malik olanlar hisseleri oranında mükelleftir: 12.000 / 3 = 4.000 ₺. "
    "Elbirliği mülkiyette ise malikler müteselsilen sorumludur.")

P.q("DVK md. 2",
    f"Bir kira sözleşmesine sonradan çeşitli şerhler eklenmiş ve bu şerhlerin ayrıca damga vergisine tabi olup olmadığı sorulmuştur.\n\n{DA}, aşağıdakilerden hangisi damga vergisine tabi değildir?",
    "Vergiye tabi olmayan bir kâğıda eklenen uzatma şerhi",
    ["Vergiye tabi bir sözleşmenin süresini uzatan şerh",
     "Vergiye tabi bir kâğıdın devrine ilişkin mektup",
     "Vergiye tabi bir sözleşmeyi değiştiren şerh",
     "Vergiye tabi bir kâğıdın bozulmasına ilişkin mektup"],
    "DVK md. 2'ye göre vergiye tabi kâğıtların hükümlerinin yenilenmesine, uzatılmasına, değiştirilmesine, devrine veya "
    "bozulmasına ilişkin mektup ve şerhler de vergiye tabidir; asıl kâğıt vergiye tabi değilse şerh de tabi olmaz.",
    zorluk="hard")

P.q("MTVK md. 4",
    f"Bir trafik tescil bürosu, adına kayıtlı taşıtlar için motorlu taşıtlar vergisi istisnası talep eden kurum ve kişilerin başvurularını incelemektedir.\n\n{MT}, aşağıdaki taşıtlardan hangisi vergiden istisna değildir?",
    "Fahri konsoloslar adına tescilli taşıtlar",
    ["Türkiye Kızılay Derneği adına tescil edilen taşıtlar",
     "Köy tüzel kişilikleri adına tescil edilen taşıtlar",
     "Belediyeler adına tescil edilen taşıtlar",
     "Sosyal güvenlik kurumları adına tescil edilen taşıtlar"],
    "MTVK md. 4'e göre kamu idareleri, sosyal güvenlik kurumları, belediyeler, köy tüzel kişilikleri ve Türkiye Kızılay Derneği "
    "adına tescilli taşıtlar ile karşılıklılık şartıyla yabancı elçilik ve konsolosluk taşıtları istisnadır; fahri konsoloslar "
    "bu istisnadan hariç tutulmuştur.")

e5 = (2_000_000 - 2_000_000 / 4) * 0.001
P.sayisal("EVK md. 5, 8",
    "Bay (Y), büyükşehir belediye sınırları dışında 2025 yılında inşası tamamlanan ve mesken olarak kullandığı binanın "
    f"sahibidir. Binanın 2026 yılı vergi değeri 2.000.000 ₺’dir.\n\n{EM}, Bay (Y)’nin 2026 yılı bina vergisi kaç ₺’dir?",
    tl(e5), secenekler(e5, 2_000, 500, 4_000, 3_000),
    "EVK md. 5/a'ya göre mesken olarak kullanılan binaların vergi değerinin 1/4'ü, inşaatın sona erdiği yılı takip eden bütçe "
    "yılından itibaren beş yıl geçici muafiyetten yararlanır: (2.000.000 − 500.000) × binde 1 = 1.500 ₺.", zorluk="hard")

P.q("MTVK md. 3",
    "Bay (F) otomobilini noter satışıyla Bayan (G)’ye satmış, ancak trafik siciline tescil işlemi henüz yapılmamıştır."
    f"\n\n{MT}, bu taşıtın vergi mükellefi kimdir?",
    "Sicilde adına kayıtlı kişi",
    ["Aracı fiilen kullanan kişi",
     "Satış bedelini ödeyen kişi",
     "Aracın bakımını yaptıran kişi",
     "Satışı yapan noter"],
    "MTVK md. 3'e göre motorlu taşıtlar vergisinin mükellefi, trafik sicili ile sivil hava vasıtaları sicilinde adlarına "
    "motorlu taşıt kayıt ve tescil edilmiş gerçek ve tüzel kişilerdir.")

P.q("MTVK md. 1",
    f"Bir şirketin aktifinde çeşitli kara, deniz ve hava taşıtları bulunmakta; hangilerinin motorlu taşıtlar vergisine tabi olduğu değerlendirilmektedir.\n\n{MT}, aşağıdakilerden hangisi motorlu taşıtlar vergisine tabidir?",
    "Sivil Havacılık Genel Müdürlüğüne tescilli helikopter",
    ["Trafiğe tescil edilmemiş yarış otomobili",
     "Tescil edilmemiş tarım traktörü",
     "Yat ve kotralar",
     "Tescilsiz iş makinesi"],
    "MTVK md. 1'e göre trafik şube veya bürolarına kayıt ve tescil edilmiş motorlu kara taşıtları ile Sivil Havacılık Genel "
    "Müdürlüğüne kayıt ve tescil edilmiş uçak ve helikopterler vergiye tabidir; deniz taşıtlarına ilişkin bent mülgadır.",
    zorluk="hard")

P.sayisal("EVK md. 9",
    "Bayan (A) bir arsa üzerinde konut inşaatını 2026 yılının Nisan ayında tamamlamış ve yapı kullanma izin belgesini aynı yıl "
    f"almıştır.\n\n{EM}, bina vergisi mükellefiyeti hangi yılın başından itibaren başlar?",
    "2027", ["2025", "2026", "2028", "2031"],
    "EVK md. 9 ve 33'e göre yeni bina inşa edilmesi vergi değerini tadil eden sebeptir; bina vergisi mükellefiyeti bu "
    "değişikliğin vuku bulduğu tarihi takip eden bütçe yılından itibaren başlar: 2027.")

P.q("ÖTVK md. 1",
    f"Bir otomotiv bayisi ve akaryakıt ithalatçısı, yaptıkları işlemlerden hangilerinin özel tüketim vergisine tabi olduğunu değerlendirmektedir.\n\n{OT}, aşağıdakilerden hangisi ÖTV’ye tabi işlemlerden biri değildir?",
    "Tescilli ikinci el otomobilin iki kişi arasında satışı",
    ["(I) sayılı listedeki akaryakıtın ithalatçı tarafından teslimi",
     "(II) sayılı listedeki yeni otomobilin ilk iktisabı",
     "(III) sayılı listedeki alkollü içkinin imalatçı tarafından teslimi",
     "(IV) sayılı listedeki malın ithalatı"],
    "ÖTVK md. 1'e göre vergi bir defaya mahsus alınır: (I) sayılı liste mallarının ithalatçı ve imalatçılarca teslimi, (II) "
    "sayılı listedeki tescile tabi malların ilk iktisabı, (III) ve (IV) sayılı liste mallarının ithalatı veya imalatçılarca "
    "teslimi vergiye tabidir. Tescilli ikinci el aracın şahıslar arası satışı ilk iktisap değildir.")

d1 = 1_000_000 * 0.00948
P.sayisal("DVK md. 5",
    "(DEF) A.Ş. ile (GHI) Ltd. Şti. 1.000.000 ₺ bedelli bir hizmet sözleşmesini üç nüsha olarak düzenleyip imzalamıştır. "
    f"(Sözleşme için nispi damga vergisi oranı binde 9,48 olarak alınacaktır.)\n\n{DA}, bu sözleşme için ödenecek damga "
    "vergisi kaç ₺’dir?",
    tl(d1), secenekler(d1, d1 * 3, d1 * 2, d1 / 3, 1_000_000 * 0.00189),
    "DVK md. 5'e göre birden fazla nüsha düzenlenen kâğıtlardan nispi vergiye tabi olanların sadece bir nüshası vergiye "
    "tabidir: 1.000.000 × binde 9,48 = 9.480 ₺.")

P.q("ÖTVK md. 3",
    "Alkollü içki üreticisi (PRS) A.Ş., (III) sayılı listedeki ürünlerini satılmak üzere bir komisyoncuya göndermiş; komisyoncu "
    f"ürünleri bir ay sonra alıcılara satmıştır.\n\n{OT}, vergiyi doğuran olay ne zaman meydana gelir?",
    "Malların komisyoncuya teslim edildiği anda",
    ["Komisyoncunun malları alıcıya teslim ettiği anda",
     "Satış bedelinin tahsil edildiği anda",
     "Ay sonunda beyanname verildiği anda",
     "Malların üretildiği anda"],
    "ÖTVK md. 3/d'ye göre komisyoncular vasıtasıyla veya konsinyasyon suretiyle satışlarda (I), (II) ve (IV) sayılı listedeki "
    "mallarda alıcıya teslim, (III) sayılı listedeki mallarda komisyoncuya veya konsinyi işletmeye teslim vergiyi doğuran "
    "olaydır.", zorluk="hard")

d2 = 500 * 3
P.sayisal("DVK md. 5",
    "Bir şirket, maktu damga vergisine tabi bir kâğıdı üç nüsha olarak düzenlemiştir. (Kâğıt için maktu vergi tutarı 500 ₺ "
    f"olarak alınacaktır.)\n\n{DA}, bu kâğıt için ödenecek damga vergisi toplamı kaç ₺’dir?",
    tl(d2), secenekler(d2, 500, 1_000, 2_000, 250),
    "DVK md. 5'e göre maktu vergiye tabi kâğıtların her bir nüshası ayrı ayrı aynı miktarda vergiye tabidir: 500 × 3 = "
    "1.500 ₺.")

P.q("ÖTVK md. 4",
    f"{OT}, (II) sayılı listedeki kayıt ve tescile tabi mallarda verginin mükellefi aşağıdakilerden hangisidir?",
    "Motorlu araç ticareti yapanlar",
    ["Aracı ilk kez kiralayan kişi",
     "Aracı trafik sicilinden silen kişi",
     "Araç için kredi veren banka",
     "Aracın sigortasını yapan şirket"],
    "ÖTVK md. 4/1-b'ye göre (II) sayılı listedeki kayıt ve tescile tabi mallarda mükellef, motorlu araç ticareti yapanlar, "
    "kullanmak üzere ithal edenler veya müzayede yoluyla satışı gerçekleştirenlerdir.", zorluk="easy")

d3 = 20_000_000
P.sayisal("DVK md. 14",
    "(JKL) A.Ş., bedeli çok yüksek bir inşaat sözleşmesi düzenlemiştir; nispi orana göre hesaplanan damga vergisi 45.000.000 "
    "₺ çıkmaktadır. (Bir kâğıt için hesaplanacak azami damga vergisi 20.000.000 ₺ olarak alınacaktır.)"
    f"\n\n{DA}, bu sözleşme için ödenecek damga vergisi kaç ₺’dir?",
    tl(d3), secenekler(d3, 45_000_000, 25_000_000, 22_500_000, 10_000_000),
    "DVK md. 14'e göre her bir kâğıt için hesaplanacak vergi tutarı Kanunda belirtilen ve her yıl yeniden değerleme oranında "
    "artırılan azami tutarı aşamaz; ödenecek vergi 20.000.000 ₺'dir.")

P.q("ÖTVK md. 4",
    "Vergi incelemesi sırasında bir akaryakıt istasyonunda (I) sayılı listedeki mallardan alış belgesi bulunmayan akaryakıt "
    f"tespit edilmiştir.\n\n{OT}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Alış belgelerini ibraz için 10 günlük süre verilir.",
    ["Mal derhal müsadere edilir, süre verilmez.",
     "İbraz için 30 günlük süre verilir.",
     "Belgesiz mal için sadece usulsüzlük cezası kesilir.",
     "Vergi sadece malı satan firmadan aranır."],
    "ÖTVK md. 4/3'e göre fiili veya kaydi envanterde listelerdeki malların belgesiz bulundurulduğunun tespiti hâlinde, "
    "mükellefe alış belgelerinin ibrazı için tespit tarihinden itibaren 10 günlük süre verilir.")

ok = (1_000_000 + 1_000_000 * 0.50) * 0.20
P.sayisal("ÖTVK md. 1, KDVK md. 24",
    "Bir otomotiv bayisi, 2026 yılında vergisiz satış bedeli 1.000.000 ₺ olan yeni bir binek otomobili tüketiciye satmıştır. "
    f"(ÖTV oranı %50, KDV oranı %20 olarak alınacaktır.)\n\n{OT} ve KDV Kanunu’na göre, bu satış için hesaplanacak KDV "
    "kaç ₺’dir?",
    tl(ok), secenekler(ok, 200_000, 500_000, 350_000, 250_000),
    "ÖTVK md. 1/b'ye göre (II) sayılı listedeki kayıt ve tescile tabi malların ilk iktisabı ÖTV'ye tabidir: 1.000.000 × %50 "
    "= 500.000 ₺. KDVK md. 24'e göre vergi, resim ve harçlar KDV matrahına dahildir: (1.000.000 + 500.000) × %20 = "
    "300.000 ₺.", zorluk="hard")

P.q("ÖTVK md. 14",
    f"Hem akaryakıt hem alkollü içki üreten bir şirket, ÖTV beyannamelerini hangi dönemler itibarıyla vereceğini belirlemektedir.\n\n{OT}, vergilendirme dönemine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "(III) sayılı listedeki mallar için vergilendirme dönemi on beş günlüktür.",
    ["(I) sayılı listedeki mallarda dönem ayın ilk on beş günü ve kalan günleridir.",
     "(III) ve (IV) sayılı listedeki mallarda dönem birer aylıktır.",
     "Vergi mükelleflerin yazılı beyanı üzerine tarh olunur.",
     "Vergi beyanname verme süresi içinde ödenir."],
    "ÖTVK md. 14'e göre (I) sayılı listedeki mallar için vergilendirme dönemi on beş günlük, (III) ve (IV) sayılı listelerdeki "
    "mallar ile (II) sayılı listedeki tescile tabi olmayanlar için aylıktır.")

P.sayisal("ÖTVK md. 14",
    "Akaryakıt ithalatçısı (MNO) A.Ş., (I) sayılı listedeki malların 1-15 Mart 2026 vergilendirme dönemine ait ÖTV "
    f"beyannamesini verecektir.\n\n{OT}, beyanname en geç Mart 2026’nın kaçıncı günü akşamına kadar verilmelidir?",
    "25", ["15", "20", "26", "31"],
    "ÖTVK md. 14'e göre (I) sayılı listedeki mallar için vergilendirme dönemi ayın ilk on beş günü ve kalan günleridir; "
    "beyanname vergilendirme dönemini izleyen onuncu gün akşamına kadar verilir: 15 Mart'ı izleyen onuncu gün 25 Mart'tır.",
    zorluk="hard")

P.oncul("DVK md. 3, 5, 6",
    f"{DA} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Damga vergisinin mükellefi kâğıtları imza edenlerdir.",
     "Maktu vergiye tabi kâğıtların sadece bir nüshası vergilendirilir.",
     "Bir kâğıttaki birbirinden tamamen ayrı işlemlerin her birinden ayrı vergi alınır.",
     "Resmi dairelerle kişiler arasındaki kâğıtların vergisini resmi daire öder."],
    "Yukarıdakilerden hangileri doğrudur?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "DVK md. 3'e göre mükellef imza edenlerdir (I), resmi daire işlemlerinde vergiyi kişiler öder (IV yanlış). Md. 5'e göre "
    "maktu vergili kâğıtların her nüshası vergilendirilir (II yanlış); md. 6'ya göre ayrı işlemlerin her birinden vergi alınır "
    "(III).", zorluk="hard")

P.sayisal("EVK md. 30",
    "Bir arsa, imar planında yeşil alan olarak ayrıldığı için mevzuatla tasarrufu kısıtlanmıştır. Kısıtlama olmasaydı arsanın "
    f"yıllık emlak vergisi 10.000 ₺ olacaktı.\n\n{EM}, kısıtlama devam ettiği sürece tahsil edilecek yıllık vergi kaç ₺’dir?",
    tl(1_000), secenekler(1_000, 10_000, 5_000, 2_500, 0),
    "EVK md. 30'a göre kanunlar veya kamu düzeni koyan mevzuatla tasarrufu kısıtlanan bina, arsa ve arazinin vergisi, "
    "kısıtlama devam ettiği sürece 1/10 oranında tahsil olunur: 10.000 × 1/10 = 1.000 ₺.", zorluk="hard")

P.q("VİVK md. 12",
    "Bay (M), borç yükü bulunan bir daireyi oğluna bağışlamış ve daireye ait borcu kendi üzerine alacağını taahhüt etmiştir."
    f"\n\n{VI}, oğlunun vergi matrahının hesabında bu borç hakkında aşağıdakilerden hangisi doğrudur?",
    "Borç matrahtan indirilmez.",
    ["Borç, bağışlayan üstlense de matrahtan indirilir.",
     "Borcun yarısı matrahtan indirilir.",
     "Borç, dairenin değerine eklenir.",
     "Borç ancak ödendikten sonra indirilir."],
    "VİVK md. 12/b'ye göre diğer suretle iktisaplarda malın aynına ait borçlar indirilir; ancak hibe eden, hibe ettiği mala ait "
    "borçları kendi üzerine almış veya taahhüt etmişse bu borçlar dikkate alınmaz.", zorluk="hard")

P.sayisal("VİVK md. 17",
    "Bir sigorta şirketi, bağış yoluyla hak sahibi olan Bayan (H)’ye 200.000 ₺ ödeme yapacaktır. Bayan (H) vergi dairesinden "
    f"alınmış tasdikname ibraz etmemiştir.\n\n{VI}, sigorta şirketinin yapacağı kesinti kaç ₺’dir?",
    tl(30_000), secenekler(30_000, 10_000, 20_000, 2_000, 0),
    "VİVK md. 17'ye göre tasdikname ibraz etmeyen hak sahiplerinin istihkaklarından ivazsız intikallerde %15 oranında vergi "
    "karşılığı tevkifat yapılır: 200.000 × %15 = 30.000 ₺.")

P.q("VİVK md. 18",
    f"{VI}, matraha girmesi gereken malların kaçırılacağına dair karineler bulunması hâlinde vergi dairesi ne isteyebilir?",
    "Tereke defteri yapılmasını isteyebilir.",
    ["Mirasçılar hakkında hapis cezası isteyebilir.",
     "Mirası doğrudan Hazineye devredebilir.",
     "Vergiyi iki katı olarak tarh edebilir.",
     "Mirasçıların pasaportlarına el koyabilir."],
    "VİVK md. 18'e göre vergi matrahına girmesi gereken malların kaçırılacağını anlatan karineler varsa vergi dairesince Türk "
    "Medeni Kanunu'na göre tereke defterinin yapılması istenebilir.")

dd = 600_000 * 0.00189 + 1_000_000 * 0.00948
P.sayisal("DVK md. 6",
    "Bir kâğıtta birbirinden tamamen bağımsız iki işlem yer almaktadır: 600.000 ₺ bedelli bir kira sözleşmesi ile aynı "
    "tarafların 1.000.000 ₺ bedelli ayrı bir hizmet sözleşmesi. (Kira sözleşmesi için oran binde 1,89, hizmet sözleşmesi "
    f"için binde 9,48 olarak alınacaktır.)\n\n{DA}, bu kâğıt için ödenecek damga vergisi toplamı kaç ₺’dir?",
    tl(dd), secenekler(dd, 1_600_000 * 0.00948, 9_480, 1_600_000 * 0.00189, 1_134),
    "DVK md. 6'ya göre bir kâğıtta birbirinden tamamen ayrı birden fazla işlem bulunursa her birinden ayrı ayrı vergi alınır: "
    "600.000 × binde 1,89 = 1.134 ₺; 1.000.000 × binde 9,48 = 9.480 ₺; toplam 10.614 ₺.", zorluk="hard")

P.q("EVK md. 33",
    "Bay (N), mesken olarak kullandığı apartman dairesini tamamen muayenehaneye dönüştürmüştür."
    f"\n\n{EM}, bu değişikliğin bina vergisine etkisi hakkında aşağıdakilerden hangisi doğrudur?",
    "Kullanış tarzının değişmesi vergi değerini tadil eder.",
    ["Kullanım değişikliği bina vergisini etkilemez.",
     "Değişiklik sadece dört yıllık genel takdirde dikkate alınır.",
     "Muayenehaneler bina vergisinden muaftır.",
     "Değişiklik hâlinde bina arsa vergisine tabi olur."],
    "EVK md. 33/3'e göre bir binanın kullanış tarzının tamamen değiştirilmesi, örneğin ikamete mahsus bir dairenin ticaret veya "
    "meslek icrasına mahsus hâle getirilmesi vergi değerini tadil eden sebeptir; md. 23'e göre bildirim verilir.")

eb = 3_000_000 * 0.002 * 0.5
P.sayisal("EVK md. 3, 8",
    "Bay (K) ile kardeşi, büyükşehir belediye sınırları içindeki vergi değeri 3.000.000 ₺ olan bir meskene paylı mülkiyetle "
    f"eşit oranda maliktir.\n\n{EM}, Bay (K)’nın mükellef olduğu yıllık bina vergisi kaç ₺’dir?",
    tl(eb), secenekler(eb, 6_000, 1_500, 12_000, 4_500),
    "EVK md. 8'e göre meskende oran binde bir olup büyükşehirde %100 artırımlıdır: 3.000.000 × binde 2 = 6.000 ₺. Md. 3'e göre "
    "paylı mülkiyette malikler hisseleri oranında mükelleftir: 6.000 × 1/2 = 3.000 ₺.")

P.q("MTVK md. 10",
    f"Bir araç sahibi, 2026 yılında ödeyeceği motorlu taşıtlar vergisinin önceki yıla göre neden arttığını sormaktadır.\n\n197 sayılı Motorlu Taşıtlar Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre, vergi tutarlarının güncellenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vergi miktarları her yıl yeniden değerleme oranında artırılır.",
    ["Vergi miktarları her yıl enflasyon oranının iki katı artırılır.",
     "Vergi miktarları sadece kanun değişikliğiyle artırılabilir.",
     "Vergi miktarları beş yılda bir güncellenir.",
     "Vergi miktarları belediye meclislerince belirlenir."],
    "MTVK md. 10'a göre her takvim yılı başından geçerli olmak üzere önceki yılda uygulanan taşıt değerleri ve vergi miktarları "
    "o yıl için ilan olunan yeniden değerleme oranında artırılır; Cumhurbaşkanı belirli sınırlar içinde farklı oran "
    "belirleyebilir.")

P.sayisal("ÖTVK md. 14",
    "Alkollü içki üreticisi (TUV) A.Ş., (III) sayılı listedeki ürünlerini Mart 2026 ayı boyunca teslim etmiştir. Şirketin "
    "aynı ay (I) sayılı listede yer alan bir mal teslimi bulunmamaktadır."
    f"\n\n{OT}, şirketin Mart 2026 dönemine ait ÖTV beyannamesi en geç Nisan 2026’nın kaçıncı günü akşamına kadar "
    "verilmelidir?",
    "15", ["10", "20", "25", "26"],
    "ÖTVK md. 14'e göre (III) ve (IV) sayılı listelerdeki mallar için vergilendirme dönemi aylıktır ve beyanname dönemi "
    "izleyen ayın on beşinci günü akşamına kadar verilir; (I) sayılı listede ise on beş günlük dönemi izleyen onuncu gündür.")

if __name__ == "__main__":
    sys.exit(P.yaz())
