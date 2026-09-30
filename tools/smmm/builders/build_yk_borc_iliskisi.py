# -*- coding: utf-8 -*-
"""Hukuk · Borçlar Hukuku · Borcun Sona Ermesi, Zamanaşımı, Teselsül, Ceza Koşulu ve Taraf Değişiklikleri — 60 soru.

Gerçek 2026/1-2026/2 kitapçıklarında TBK soruları "6098 sayılı Türk Borçlar Kanunu’na göre, 'Birden çok …'" gibi tanım
ve zamanaşımı soran kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6098 sayılı TBK md. 132-206.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_borc_iliskisi_2026.json", lesson="borclar_hukuku", topic="borc_iliskisi",
          konu_adi="Borç İlişkisi", seed=2026093017, surum="6098 sayılı TBK güncel metni; 29.09.2026 kontrolü")

K = "6098 sayılı Türk Borçlar Kanunu’na göre"

P.sayisal("TBK md. 146",
    f"{K}, Kanunda aksine hüküm bulunmadıkça her alacak kaç yıllık zamanaşımına tabidir?",
    "10", ["2", "3", "5", "20"],
    "Md. 146'ya göre Kanunda aksine hüküm bulunmadıkça her alacak on yıllık zamanaşımına tabidir.", zorluk="easy")

P.q("TBK md. 132",
    f"{K}, ibra sözleşmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Şekle bağlı borç şekilsiz ibra edilebilir.",
    ["İbra, borcu doğuran işlemle aynı şekle bağlıdır.",
     "İbra sadece borcun tamamı için yapılabilir.",
     "İbra için noter onayı gerekir.",
     "İbra tek taraflı bir irade açıklamasıdır."],
    "Md. 132'ye göre borcu doğuran işlem şekle bağlı olsa bile borç tarafların şekle bağlı olmaksızın yapacakları ibra "
    "sözleşmesiyle tamamen veya kısmen ortadan kaldırılabilir.")

P.q("TBK md. 133",
    f"{K}, yenilemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mevcut borç için poliçe verilmesi yenileme sayılır.",
    ["Yenileme tarafların açık iradesiyle olur.",
     "Yeni alacak senedi düzenlenmesi tek başına yenileme değildir.",
     "Yeni kefalet senedi tek başına yenileme değildir.",
     "Kesilip kabul edilen cari hesapta borç yenilenmiş olur."],
    "Md. 133'e göre mevcut borç için kambiyo taahhüdünde bulunulması, tarafların açık yenileme iradesi olmadıkça yenileme "
    "sayılmaz.")

P.sayisal("TBK md. 147",
    f"{K}, kira bedelleri ve anapara faizleri gibi dönemsel edimler kaç yıllık zamanaşımına tabidir?",
    "5", ["1", "2", "3", "10"],
    "Md. 147'ye göre kira bedelleri, anapara faizleri ve ücret gibi dönemsel edimler beş yıllık zamanaşımına tabidir.")

P.q("TBK md. 134",
    f"{K}, cari hesapta yenilemeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kesilip kabul edilince yenilenir.",
    ["Kalemlerin hesaba yazılmasıyla borç yenilenir.",
     "Cari hesapta yenileme olmaz.",
     "Hesap kesilince güvenceler doğrudan sona erer.",
     "Yenileme için noter onayı şarttır."],
    "Md. 134'e göre kalemlerin cari hesaba kaydedilmesi yenileme değildir; hesabın kesilip sonucunun kabul edilmesiyle borç "
    "yenilenir; kalemlerin güvencesi aksi kararlaştırılmadıkça sona ermez.", zorluk="hard")

P.q("TBK md. 135",
    f"{K}, birleşmeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birleşme üçüncü kişi haklarını da kaldırır.",
    ["Alacaklı ve borçlu sıfatının birleşmesiyle borç sona erer.",
     "Birleşme geçmişe etkili kalkarsa borç sürer.",
     "Taşınmaz rehnine ilişkin özel hükümler saklıdır.",
     "Kıymetli evraka ilişkin özel hükümler saklıdır."],
    "Md. 135'e göre üçüncü kişilerin alacak üzerinde önceden mevcut olan hakları birleşmeden etkilenmez.")

P.sayisal("TBK md. 156",
    "Borçlu, borcunu bir senetle ikrar etmiş ve böylece zamanaşımı kesilmiştir."
    f"\n\n{K}, kesilmeyle işlemeye başlayan yeni zamanaşımı süresi kaç yıldır?",
    "10", ["2", "3", "5", "20"],
    "Md. 156'ya göre borç bir senetle ikrar edilmiş veya mahkeme ya da hakem kararına bağlanmışsa yeni süre her zaman on "
    "yıldır.", zorluk="hard")

P.q("TBK md. 136",
    f"{K}, borçlunun sorumlu tutulamayacağı sebeplerle ifanın imkânsızlaşmasına ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Borçlu, karşı edimi yine de isteyebilir.",
    ["Borç sona erer.",
     "Alınan edim sebepsiz zenginleşmeye göre geri verilir.",
     "Borçlu durumu gecikmeksizin bildirmelidir.",
     "Hasarın alacaklıya yüklendiği hâller istisnadır."],
    "Md. 136'ya göre karşılıklı borç yükleyen sözleşmelerde imkânsızlık nedeniyle borçtan kurtulan borçlu henüz kendisine ifa "
    "edilmemiş edimi isteme hakkını kaybeder.")

P.q("TBK md. 137",
    f"{K}, borcun borçlunun sorumlu tutulamayacağı sebeplerle kısmen imkânsızlaşmasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Borçlu sadece imkânsızlaşan kısımdan kurtulur.",
    ["Borcun tamamı sona erer.",
     "Borçlu kalan kısmı ifadan kaçınabilir.",
     "Alacaklı karşı edimin tamamını öder.",
     "Kısmi imkânsızlık sözleşmeyi kesin hükümsüz kılar."],
    "Md. 137'ye göre borç kısmen imkânsızlaşırsa borçlu sadece imkânsızlaşan kısımdan kurtulur; ancak bu öngörülseydi sözleşme "
    "yapılmayacaksa borcun tamamı sona erer.")

P.sayisal("TBK md. 158",
    "Alacaklının açtığı dava, mahkemenin görevli olmaması nedeniyle reddedilmiş; bu arada zamanaşımı süresi dolmuştur."
    f"\n\n{K}, alacaklı haklarını kaç günlük ek süre içinde kullanabilir?",
    "60", ["15", "30", "45", "90"],
    "Md. 158'e göre dava görev, yetki, düzeltilebilir yanlışlık veya erken açılma nedeniyle reddedilmiş ve bu arada süre "
    "dolmuşsa alacaklı altmış günlük ek süre içinde haklarını kullanabilir.", zorluk="hard")

P.q("TBK md. 138",
    f"{K}, aşırı ifa güçlüğünde borçlunun öncelikli hakkı aşağıdakilerden hangisidir?",
    "Sözleşmenin uyarlanmasını istemek",
    ["Sözleşmeden derhal dönmek",
     "Borcu tek taraflı indirmek",
     "Alacaklıdan tazminat almak",
     "Borcu ifa etmeden sona erdirmek"],
    "Md. 138'e göre koşulları oluşan aşırı ifa güçlüğünde borçlu hâkimden sözleşmenin yeni koşullara uyarlanmasını, bu mümkün "
    "değilse sözleşmeden dönmeyi isteyebilir; sürekli edimli sözleşmelerde kural olarak fesih hakkı vardır.")

P.q("TBK md. 138",
    f"{K}, aşırı ifa güçlüğünün koşulları arasında aşağıdakilerden hangisi yer almaz?",
    "Durumun borçludan kaynaklanması",
    ["Durumun sözleşmede öngörülmemiş olması",
     "Durumun öngörülmesinin beklenmemesi",
     "İfa isteminin dürüstlüğe aykırı düşmesi",
     "Borcun henüz ifa edilmemiş olması"],
    "Md. 138'e göre olağanüstü durumun borçludan kaynaklanmayan bir sebeple ortaya çıkması gerekir.", zorluk="hard")

P.sayisal("TBK md. 202",
    f"{K}, bir işletmeyi aktif ve pasifleriyle devralanın sorumluluğunun yanında önceki borçlu kaç yıl süreyle "
    "müteselsilen sorumlu kalır?",
    "2", ["1", "3", "5", "10"],
    "Md. 202'ye göre işletmeyi aktif ve pasifleriyle devralan bildirim veya ilandan itibaren borçlardan sorumlu olur; önceki "
    "borçlu da iki yıl süreyle devralanla birlikte müteselsilen sorumlu kalır.")

P.q("TBK md. 139",
    f"{K}, takasın koşullarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Çekişmeli alacakla takas yapılamaz.",
    ["Borçlar karşılıklı olmalıdır.",
     "Borçlar para veya özdeş edim olmalıdır.",
     "Her iki borç muaccel olmalıdır.",
     "Zamanaşımlı alacak koşuluyla takas edilebilir."],
    "Md. 139'a göre alacaklardan biri çekişmeli olsa bile takas ileri sürülebilir.")

P.q("TBK md. 141",
    f"{K}, üçüncü kişi yararına borçlanan kişinin takas hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Diğer taraftan alacağıyla takas edemez.",
    ["Kural olarak takas edebilir.",
     "Sadece üçüncü kişinin onayıyla takas eder.",
     "Takası mahkeme karar verirse yapabilir.",
     "Borcu iki katına çıkararak takas eder."],
    "Md. 141'e göre üçüncü kişi yararına borçlanan kişi bu borcu ile sözleşmenin diğer tarafından olan alacağını takas edemez.")

cp = 10_000 * 2
P.sayisal("TBK md. 178",
    "Sözleşme yapılırken (A), (B)’ye 10.000 ₺ cayma parası vermiştir. Daha sonra cayma parasını alan (B) sözleşmeden "
    f"caymıştır.\n\n{K}, (B) (A)’ya kaç ₺ geri vermelidir?",
    tl(cp), secenekler(cp, 10_000, 15_000, 30_000, 5_000),
    "Md. 178'e göre cayma parası kararlaştırılmışsa parayı veren cayarsa verdiğini bırakır; parayı alan cayarsa aldığının iki "
    "katını geri verir: 10.000 × 2 = 20.000 ₺.")

P.q("TBK md. 142",
    f"{K}, borçlunun iflası hâlinde alacaklıların takas hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Muaccel olmasa da takas edebilirler.",
    ["Takas edemezler.",
     "Sadece muaccel alacakları takas ederler.",
     "Takas için masanın onayı gerekir.",
     "Sadece rehinli alacakları takas ederler."],
    "Md. 142'ye göre borçlunun iflası hâlinde alacaklılar alacakları muaccel olmasa bile müflise olan borçlarıyla takas "
    "edebilir.", zorluk="hard")

P.q("TBK md. 143",
    f"{K}, takasın gerçekleşmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Takas iradesinin bildirimiyle gerçekleşir.",
    ["Koşullar oluşunca bildirimsiz gerçekleşir.",
     "Mahkeme kararıyla gerçekleşir.",
     "Noter tespitiyle gerçekleşir.",
     "Alacaklının onayıyla gerçekleşir."],
    "Md. 143'e göre takas ancak borçlunun takas iradesini alacaklıya bildirmesiyle gerçekleşir; borçlar takas edilebilecekleri "
    "anda daha az olan tutarda sona erer.")

tk = 80_000 - 50_000
P.sayisal("TBK md. 143",
    "(A)’nın (B)’ye 80.000 ₺, (B)’nin (A)’ya 50.000 ₺ muaccel para borcu vardır. (A), takas iradesini (B)’ye bildirmiştir."
    f"\n\n{K}, takastan sonra (A)’nın (B)’ye kalan borcu kaç ₺’dir?",
    tl(tk), secenekler(tk, 0, 50_000, 80_000, 130_000),
    "Md. 139 ve 143'e göre karşılıklı muaccel para borçları takas edilebilir; takas bildirimiyle iki borç daha az olan tutar "
    "kadar sona erer: 80.000 − 50.000 = 30.000 ₺.")

P.q("TBK md. 144",
    f"{K}, aşağıdaki alacaklardan hangisi alacaklının rızası olmadan takas edilebilir?",
    "Ticari satıştan doğan bedel alacağı",
    ["Tevdi edilmiş eşyanın geri verilmesi alacağı",
     "Haksız alınmış eşyanın bedeli alacağı",
     "Nafaka alacağı",
     "İşçi ücreti alacağı"],
    "Md. 144'e göre tevdi edilmiş veya haksız alınmış eşyanın iadesi ile nafaka ve işçi ücreti gibi alacaklar ancak alacaklının "
    "rızasıyla takas edilebilir.", zorluk="hard")

P.q("TBK md. 145",
    f"{K}, takas hakkından feragate ilişkin aşağıdakilerden hangisi doğrudur?",
    "Borçlu önceden de feragat edebilir.",
    ["Takas hakkından feragat edilemez.",
     "Feragat sadece mahkeme önünde yapılır.",
     "Feragat alacaklının iflasına bağlıdır.",
     "Feragat için noter onayı şarttır."],
    "Md. 145'e göre borçlu takas hakkından önceden de feragat edebilir.")

mp = 90_000 / 3
P.sayisal("TBK md. 167",
    "(A), (B) ve (C) alacaklıya karşı 90.000 ₺’lik bir borçtan müteselsilen sorumludur; aralarında paylaşıma ilişkin "
    f"bir anlaşma yoktur. (A) borcun tamamını ödemiştir.\n\n{K}, (A) (B)’den en çok kaç ₺ isteyebilir?",
    tl(mp), secenekler(mp, 90_000, 60_000, 45_000, 15_000),
    "Md. 167'ye göre aksi kararlaştırılmadıkça müteselsil borçlular iç ilişkide eşit paylarla sorumludur ve fazla ödeyen her "
    "borçluya ancak payı oranında rücu edebilir: 90.000 / 3 = 30.000 ₺.", zorluk="hard")

P.q("TBK md. 147",
    f"{K}, aşağıdaki alacaklardan hangisi beş yıllık zamanaşımına tabi değildir?",
    "Ödünç verilen paranın anaparası",
    ["Kira bedelleri",
     "Otel konaklama bedelleri",
     "Lokanta yeme içme bedelleri",
     "Küçük çaplı perakende satış alacakları"],
    "Md. 147'ye göre kira bedelleri, faizler, konaklama ve yeme içme bedelleri, küçük perakende satış alacakları beş yıllık "
    "zamanaşımına tabidir; ödünç anaparası md. 146'daki genel on yıllık süreye tabidir.")

P.q("TBK md. 148",
    f"{K}, Kanunda belirlenen zamanaşımı sürelerinin sözleşmeyle değiştirilmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Sözleşmeyle değiştirilemez.",
    ["Sözleşmeyle kısaltılabilir.",
     "Sözleşmeyle uzatılabilir.",
     "Noter onayıyla değiştirilebilir.",
     "Tacirler arasında değiştirilir."],
    "Md. 148'e göre bu ayırımda belirlenen zamanaşımı süreleri sözleşmeyle değiştirilemez.", zorluk="easy")

P.q("TBK md. 149",
    f"{K}, zamanaşımının başlangıcına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Alacağın muaccel olmasıyla başlar.",
    ["Sözleşmenin kurulmasıyla başlar.",
     "Alacaklının ihtarıyla başlar.",
     "Dava tarihinde başlar.",
     "Takvim yılı sonunda başlar."],
    "Md. 149'a göre zamanaşımı alacağın muaccel olmasıyla işlemeye başlar; muacceliyet bildirime bağlıysa bildirimin "
    "yapılabileceği günden başlar.", zorluk="easy")

P.q("TBK md. 152",
    f"{K}, asıl alacak zamanaşımına uğrayınca ona bağlı faiz alacakları hakkında aşağıdakilerden hangisi doğrudur?",
    "Onlar da zamanaşımına uğramış olur.",
    ["Bağımsız olarak on yıl daha istenebilir.",
     "Faizler iki katına çıkar.",
     "Faizler asıl alacağa eklenir.",
     "Faizler sadece mahkeme kararıyla düşer."],
    "Md. 152'ye göre asıl alacak zamanaşımına uğrayınca ona bağlı faiz ve diğer alacaklar da zamanaşımına uğramış olur.")

P.q("TBK md. 153",
    f"{K}, aşağıdakilerden hangisi zamanaşımının durması hâllerinden biri değildir?",
    "Borçlunun borcu ikrar etmesi",
    ["Velayet süresince çocuğun ana-babasından alacağı",
     "Evlilik süresince eşlerin birbirinden alacağı",
     "Ev hizmetlisinin hizmet süresince alacağı",
     "Alacağın Türk mahkemelerinde ileri sürülemediği süre"],
    "Md. 153'e göre velayet, vesayet, evlilik, ev hizmeti ve alacağın Türk mahkemelerinde ileri sürülememesi gibi hâllerde "
    "zamanaşımı durur; borcun ikrarı md. 154'e göre zamanaşımını keser.")

P.q("TBK md. 154",
    f"{K}, aşağıdakilerden hangisi zamanaşımını kesen hâllerden biri değildir?",
    "Sözlü hatırlatma yapılması",
    ["Borçlunun faiz ödemesi",
     "Borçlunun kısmen ifada bulunması",
     "Alacaklının icra takibi başlatması",
     "Alacaklının dava açması"],
    "Md. 154'e göre borçlunun ikrarı (faiz ödeme, kısmi ifa, rehin veya kefil gösterme) ile alacaklının dava, def'i, icra "
    "takibi veya iflas masasına başvurması zamanaşımını keser; sözlü hatırlatma kesmez.")

P.q("TBK md. 155",
    f"{K}, zamanaşımının kesilmesinin birlikte borçlulara etkisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kefile karşı kesilme asıl borçluya karşı da keser.",
    ["Müteselsil borçlulardan birine karşı kesilme diğerlerine de etkilidir.",
     "Bölünemeyen borçta birine karşı kesilme diğerlerine etkilidir.",
     "Asıl borçluya karşı kesilme kefile karşı da keser.",
     "Kesilmeyle yeni bir süre işlemeye başlar."],
    "Md. 155'e göre zamanaşımı kefile karşı kesilince asıl borçluya karşı kesilmiş olmaz.", zorluk="hard")

P.q("TBK md. 160",
    f"{K}, zamanaşımından feragate ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zamanaşımından önceden feragat edilebilir.",
    ["Bir müteselsil borçlunun feragati diğerlerine ileri sürülemez.",
     "Bölünemeyen borçta bir borçlunun feragati diğerlerini bağlamaz.",
     "Asıl borçlunun feragati kefile ileri sürülemez.",
     "Zamanaşımı gerçekleştikten sonra feragat mümkündür."],
    "Md. 160'a göre zamanaşımından önceden feragat edilemez; bir borçlunun feragati diğer borçlulara ve kefile karşı ileri "
    "sürülemez.", zorluk="easy")

P.q("TBK md. 161",
    f"{K}, zamanaşımının mahkemece dikkate alınmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İleri sürülmedikçe hâkim dikkate alamaz.",
    ["Hâkim resen dikkate alır.",
     "Sadece alacaklı ileri sürebilir.",
     "Sadece ilk duruşmada dikkate alınır.",
     "Hâkim tarafların rızası olmadan dikkate alır."],
    "Md. 161'e göre zamanaşımı ileri sürülmedikçe hâkim bunu kendiliğinden göz önüne alamaz.")

P.q("TBK md. 162",
    f"{K}, müteselsil borçluluğun doğumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bildirim veya kanunla doğar.",
    ["Birden çok borçlu varsa doğrudan doğar.",
     "Sadece mahkeme kararıyla doğar.",
     "Sadece tacirler arasında doğar.",
     "Alacaklının tek taraflı beyanıyla doğar."],
    "Md. 162'ye göre birden çok borçludan her biri borcun tamamından sorumlu olmayı kabul ettiğini bildirirse müteselsil "
    "borçluluk doğar; böyle bir bildirim yoksa ancak kanunda öngörülen hâllerde doğar.")

P.q("TBK md. 163",
    f"{K}, müteselsil borçlulukta dış ilişkiye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Alacaklı sadece eşit paylarla isteyebilir.",
    ["Alacaklı borcun tamamını bir borçludan isteyebilir.",
     "Alacaklı borcun bir kısmını birinden isteyebilir.",
     "Sorumluluk borç tamamen ödenene kadar sürer.",
     "Alacaklı borçluların hepsinden isteyebilir."],
    "Md. 163'e göre alacaklı borcun tamamının veya bir kısmının ifasını dilerse borçluların hepsinden, dilerse sadece birinden "
    "isteyebilir.")

P.q("TBK md. 165",
    f"{K}, müteselsil borçlulardan birinin kendi davranışıyla diğerlerinin durumunu ağırlaştırmasına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Kural olarak ağırlaştıramaz.",
    ["Dilediği gibi ağırlaştırabilir.",
     "Alacaklının onayıyla ağırlaştırır.",
     "Mahkeme izniyle ağırlaştırır.",
     "Sadece faiz yönünden ağırlaştırabilir."],
    "Md. 165'e göre kanun veya sözleşmeyle aksi belirlenmedikçe borçlulardan biri kendi davranışıyla diğer borçluların durumunu "
    "ağırlaştıramaz.")

P.q("TBK md. 166",
    f"{K}, alacaklının müteselsil borçlulardan biriyle yaptığı ibra sözleşmesinin diğer borçlulara etkisi nedir?",
    "İbra edilenin payı oranında kurtarır.",
    ["Diğer borçluları tamamen kurtarır.",
     "Diğer borçlulara bir etkisi olmaz.",
     "Diğerlerinin borcunu artırır.",
     "Diğer borçluları yarı oranda kurtarır."],
    "Md. 166'ya göre alacaklının borçlulardan biriyle yaptığı ibra sözleşmesi diğer borçluları da ibra edilen borçlunun iç "
    "ilişkideki payı oranında borçtan kurtarır.", zorluk="hard")

P.q("TBK md. 167",
    f"{K}, müteselsil borçlulardan birinden alınamayan payın paylaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Diğer borçlular eşit olarak üstlenir.",
    ["Alacaklı üstlenir.",
     "Ödeyen borçlu tek başına üstlenir.",
     "Pay düşer.",
     "Mahkeme hakkaniyete göre alacaklıya yükler."],
    "Md. 167'ye göre borçlulardan birinden alınamayan miktarı diğer borçlular eşit olarak üstlenmekle yükümlüdür.")

P.q("TBK md. 169",
    f"{K}, müteselsil alacaklılığa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birine ifa diğerlerine karşı borcu sürdürür.",
    ["Her alacaklı borcun tamamını isteyebilir.",
     "Birine yapılan ifa borçluyu kurtarır.",
     "Kural olarak alacaklıların hakları eşittir.",
     "Fazlasını alan alacaklı fazlayı paylaştırır."],
    "Md. 169'a göre borçlu alacaklılardan birine yaptığı ifayla bütün alacaklılara karşı borcundan kurtulur.")

P.q("TBK md. 170",
    f"{K}, geciktirici koşula bağlı sözleşme aksi kararlaştırılmamışsa ne zamandan itibaren hüküm doğurur?",
    "Koşulun gerçekleştiği andan",
    ["Sözleşmenin kurulduğu andan",
     "Koşulun gerçekleşmesinden bir ay sonra",
     "Tarafların yeniden anlaştığı andan",
     "Koşulun gerçekleşmeyeceği anlaşıldığında"],
    "Md. 170'e göre geciktirici koşula bağlı sözleşme, aksi kararlaştırılmamışsa ancak koşulun gerçekleştiği andan başlayarak "
    "hüküm ifade eder.")

P.q("TBK md. 171",
    f"{K}, koşulun askıda olduğu süreye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Borçlu ifayı engelleyici davranabilir.",
    ["Alacaklı hakkını korumak için önlem alabilir.",
     "Koşulu zedeleyen tasarruflar o oranda geçersizdir.",
     "Borçlu gereği gibi ifayı engellememelidir.",
     "Koşul gerçekleşirse yararlar alacaklıya kalır."],
    "Md. 171'e göre koşul gerçekleşinceye kadar borçlu borcun gereği gibi ifasını engelleyecek her türlü davranıştan kaçınmakla "
    "yükümlüdür.")

P.q("TBK md. 177",
    f"{K}, sözleşme yapılırken verilen bir miktar para aksine anlaşma yoksa ne sayılır?",
    "Bağlanma parası",
    ["Cayma parası", "Ceza koşulu", "Teminat parası", "Kaparo iadesi zorunlu avans"],
    "Md. 177'ye göre sözleşme yapılırken verilen para cayma parası olarak değil sözleşmenin yapıldığına kanıt olarak verilmiş "
    "sayılır; aksine anlaşma veya yerel âdet yoksa esas alacaktan düşülür.", zorluk="easy")

P.q("TBK md. 179",
    "Sözleşmede borcun hiç ifa edilmemesi hâli için ceza kararlaştırılmış, sözleşmeden aksi anlaşılmamaktadır."
    f"\n\n{K}, borç ifa edilmezse alacaklı ne isteyebilir?",
    "Ya borcun ya da cezanın ifasını",
    ["Borç ve cezayı birlikte",
     "Sadece cezanın yarısını",
     "Cezanın iki katını",
     "Sadece gecikme faizini"],
    "Md. 179'a göre sözleşmenin hiç veya gereği gibi ifa edilmemesi için ceza kararlaştırılmışsa, aksi anlaşılmadıkça alacaklı ya "
    "borcun ya da cezanın ifasını isteyebilir.")

P.q("TBK md. 179",
    f"{K}, borcun belirlenen zaman veya yerde ifa edilmemesi için kararlaştırılan cezada alacaklının hakkı "
    "aşağıdakilerden hangisidir?",
    "Borçla birlikte cezayı istemek",
    ["Sadece asıl borcu istemek",
     "Sadece cezayı istemek",
     "Cezanın yarısını istemek",
     "Sözleşmeden dönüp ceza istememek"],
    "Md. 179'a göre ceza borcun belirlenen zaman veya yerde ifa edilmemesi için kararlaştırılmışsa alacaklı, feragat etmemiş veya "
    "ifayı çekincesiz kabul etmemişse asıl borçla birlikte cezanın ifasını da isteyebilir.", zorluk="hard")

P.q("TBK md. 180",
    f"{K}, ceza koşulunda zarar ile ceza ilişkisine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Alacaklı zarara uğramamışsa ceza istenemez.",
    ["Zarar olmasa da kararlaştırılan ceza ödenir.",
     "Zarar cezayı aşarsa kusur ispatıyla aşan kısım istenir.",
     "Ceza tutarını taraflar belirler.",
     "Hâkim aşırı cezayı indirir."],
    "Md. 180'e göre alacaklı herhangi bir zarara uğramamış olsa bile kararlaştırılan cezanın ifası gerekir.")

P.q("TBK md. 182",
    f"{K}, ceza koşulunun geçersizliği ve indirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ceza geçersizse asıl borç da geçersizdir.",
    ["Asıl borç geçersizse ceza istenemez.",
     "Hâkim aşırı cezayı resen indirir.",
     "Taraflar ceza miktarını belirleyebilir.",
     "Sorumsuz imkânsızlıkta kural olarak ceza istenemez."],
    "Md. 182'ye göre ceza koşulunun geçersiz olması veya sonradan imkânsızlaşması asıl borcun geçerliliğini etkilemez.")

P.q("TBK md. 183",
    f"{K}, alacağın devrine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak rıza aranmaz.",
    ["Borçlunun yazılı rızası şarttır.",
     "Devir sadece mahkeme kararıyla olur.",
     "Her alacak devredilebilir.",
     "Devir için noter onayı şarttır."],
    "Md. 183'e göre kanun, sözleşme veya işin niteliği engel olmadıkça alacaklı borçlunun rızasını aramaksızın alacağını üçüncü "
    "kişiye devredebilir.")

P.q("TBK md. 184",
    f"{K}, alacağın devrinin şekline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Devir sözü verme de yazılı şekle tabidir.",
    ["Devrin geçerliliği yazılı şekle bağlıdır.",
     "Yasal devir özel şekle bağlı değildir.",
     "Yargısal devir özel şekle bağlı değildir.",
     "Yasal devirde önceki alacaklının rızası aranmaz."],
    "Md. 184'e göre alacağın devrinin geçerliliği yazılı şekle bağlıdır; ancak alacağın devri sözü verme şekle bağlı değildir.",
    zorluk="hard")

P.q("TBK md. 186",
    "Alacak devredilmiş ancak devir borçluya bildirilmemiştir; borçlu iyiniyetle önceki alacaklıya ödeme yapmıştır."
    f"\n\n{K}, borçlunun durumu nedir?",
    "Borcundan kurtulur.",
    ["Devralana yeniden ödemelidir.",
     "Borcun yarısından kurtulur.",
     "Önceki alacaklıyla müteselsilen sorumludur.",
     "Ödeme kesin hükümsüzdür."],
    "Md. 186'ya göre devir bildirilmemişse borçlu önceki alacaklıya iyiniyetle ifada bulunarak borcundan kurtulur.")

P.q("TBK md. 188",
    f"{K}, alacağın devrinde borçlunun savunmalarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Devredene karşı savunmaları ileri sürer.",
    ["Devirden sonra bir savunma ileri süremez.",
     "Sadece devralana özgü savunmaları ileri sürer.",
     "Takas hakkı devirle doğrudan düşer.",
     "Savunmalar sadece noter aracılığıyla ileri sürülür."],
    "Md. 188'e göre borçlu devri öğrendiği sırada devredene karşı sahip olduğu savunmaları devralana karşı da ileri sürebilir.")

P.q("TBK md. 189",
    f"{K}, alacağın devriyle devralana geçen haklar arasında aşağıdakilerden hangisi yer almaz?",
    "Devredenin kişiliğine özgü öncelik hakları",
    ["Rehin gibi bağlı haklar",
     "Kefalet gibi bağlı haklar",
     "İşlemiş faizler",
     "Kişiliğe özgü olmayan öncelik hakları"],
    "Md. 189'a göre devredenin kişiliğine özgü olanlar dışındaki öncelik hakları ve bağlı haklar ile işlemiş faizler devralana "
    "geçer.", zorluk="hard")

P.q("TBK md. 191",
    f"{K}, bir edim karşılığında alacağını devreden kişinin garanti yükümlülüğü aşağıdakilerden hangisidir?",
    "Alacağın varlığı ve borçlunun ödeme gücü",
    ["Sadece borçlunun ödeme gücü",
     "Bir şeyi garanti etmez.",
     "Sadece faizlerin ödenmesi",
     "Sadece alacağın vadesi"],
    "Md. 191'e göre alacak bir edim karşılığında devredilmişse devreden alacağın varlığını ve borçlunun ödeme gücünü garanti "
    "etmiş olur; karşılıksız devirde bu sorumluluk yoktur.")

P.q("TBK md. 196",
    f"{K}, borçlunun yerine yenisinin geçmesi ve borcundan kurtarılması hangi sözleşmeyle olur?",
    "Üstlenen ile alacaklının sözleşmesi",
    ["Borçlu ile üstlenen arasındaki iç üstlenme",
     "Borçlu ile alacaklı arasındaki ibra",
     "Alacaklı ile üçüncü kişi arasındaki devir",
     "Borçlu ile kefil arasındaki anlaşma"],
    "Md. 196'ya göre borçlunun yerine yenisinin geçmesi ve borcundan kurtarılması, borcu üstlenen ile alacaklı arasında yapılacak "
    "dış üstlenme sözleşmesiyle olur.", zorluk="hard")

P.q("TBK md. 198",
    f"{K}, borcun üstlenilmesinde kefilin sorumluluğunun devamı için aşağıdakilerden hangisi gerekir?",
    "Kefilin yazılı rızası",
    ["Alacaklının bildirimi", "Yeni borçlunun onayı", "Mahkeme kararı", "Kefilin sözlü kabulü"],
    "Md. 198'e göre borcun güvencesi olarak rehin veren üçüncü kişinin ve kefilin sorumlulukları ancak borcun üstlenilmesine "
    "yazılı olarak rıza göstermeleri hâlinde devam eder.")

P.q("TBK md. 201",
    f"{K}, borca katılmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Katılan ile borçlu müteselsilen sorumlu olur.",
    ["Borçlu borçtan kurtulur.",
     "Katılan sadece yarı oranda sorumludur.",
     "Katılma borçlunun rızasıyla alacaklısız yapılır.",
     "Katılan sadece faizlerden sorumludur."],
    "Md. 201'e göre borca katılma katılan ile alacaklı arasında yapılır ve katılan ile borçlu alacaklıya karşı müteselsilen "
    "sorumlu olur.")

P.q("TBK md. 205",
    f"{K}, sözleşmenin devrine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Devrin geçerliliği bir şekle bağlı değildir.",
    ["Devralan, devreden ve kalan taraf arasında yapılır.",
     "Taraf sıfatı ile tüm hak ve borçlar geçer.",
     "Kalan tarafın önceden izni de yeterlidir.",
     "Kalan tarafın sonradan onayı da yeterlidir."],
    "Md. 205'e göre sözleşmenin devrinin geçerliliği devredilen sözleşmenin şekline bağlıdır.")

P.oncul("TBK md. 154",
    f"{K} aşağıdaki durumlar değerlendirilmektedir:",
    ["Borçlunun kefil göstermesi",
     "Alacaklının iflas masasına başvurması",
     "Alacaklının borçluya e-posta ile hatırlatma yapması",
     "Borçlunun rehin vermesi"],
    "Yukarıdakilerden hangileri zamanaşımını keser?",
    "I, II ve IV",
    ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, II, III ve IV"],
    "Md. 154'e göre borçlunun kefil göstermesi (I) ve rehin vermesi (IV) ikrar niteliğindedir; alacaklının iflas masasına "
    "başvurması (II) da zamanaşımını keser; basit hatırlatma (III) kesmez.", zorluk="hard")

P.q("TBK md. 150",
    f"{K}, ömür boyu gelir gibi dönemsel edimlerde alacağın tamamı için zamanaşımı ne zaman işlemeye başlar?",
    "İfa edilmeyen ilk edimin muaccel olduğu gün",
    ["Sözleşmenin kurulduğu gün",
     "Son dönemsel edimin muaccel olduğu gün",
     "Alacaklının ölüm tarihi",
     "Her dönemsel edim için ayrı ayrı ve sadece o dönemde"],
    "Md. 150'ye göre ömür boyunca gelir ve benzeri dönemsel edimlerde alacağın tamamı için zamanaşımı ifa edilmemiş ilk dönemsel "
    "edimin muaccel olduğu günde işlemeye başlar.", zorluk="hard")

P.q("TBK md. 151",
    f"{K}, zamanaşımı sürelerinin hesaplanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zamanaşımının başladığı gün süreye dahil edilir.",
    ["Son gün hak kullanılmadan geçince zamanaşımı gerçekleşir.",
     "İfa sürelerine ilişkin hükümler uygulanır.",
     "Başlangıç günü sayılmaz.",
     "Son gün tatilse ilk iş gününe geçer."],
    "Md. 151'e göre süreler hesaplanırken zamanaşımının başladığı gün sayılmaz; zamanaşımı son gün de hak kullanılmaksızın "
    "geçince gerçekleşir.")

P.q("TBK md. 159",
    f"{K}, taşınır rehniyle güvenceye bağlanmış alacakta zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zamanaşımı işler; rehinden alma yetkisi sürer.",
    ["Rehin varken zamanaşımı işlemez.",
     "Zamanaşımıyla rehin hakkı da düşer.",
     "Zamanaşımı süresi yarıya iner.",
     "Rehinli alacak zamanaşımına uğramaz ve süresiz korunur."],
    "Md. 159'a göre alacağın taşınır rehniyle güvenceye bağlanmış olması zamanaşımının işlemesine engel olmaz; ancak alacaklının "
    "hakkını rehinden alma yetkisi devam eder.", zorluk="hard")

P.q("TBK md. 172",
    f"{K}, geciktirici koşul gerçekleşmezse koşulun gerçekleşmesinden önce kendisine şey verilen alacaklının durumu "
    "nedir?",
    "Elde ettiği yararları geri verir.",
    ["Yararlar kendisinde kalır.",
     "Yararların iki katını öder.",
     "Şeyin mülkiyetini kazanır.",
     "Yararların yarısını borçluya verip kalanını tutar."],
    "Md. 172'ye göre koşul gerçekleşirse alacaklı elde ettiği yararların sahibi olur; koşul gerçekleşmezse elde ettiği yararları "
    "geri vermekle yükümlüdür.")

P.q("TBK md. 181",
    f"{K}, dönme durumunda ifa edilmiş kısmın alacaklıya kalacağını öngören sözleşmelere hangi hükümler uygulanır?",
    "Ceza koşuluna ilişkin hükümler",
    ["Cayma parası hükümleri",
     "Bağlanma parası hükümleri",
     "Sebepsiz zenginleşme hükümleri",
     "Kira sözleşmesi hükümleri"],
    "Md. 181'e göre ceza koşuluna ilişkin hükümler dönme durumunda ifa edilmiş kısmın alacaklıya kalacağını öngören sözleşmelere "
    "de uygulanır; taksitle satış hükümleri saklıdır.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
