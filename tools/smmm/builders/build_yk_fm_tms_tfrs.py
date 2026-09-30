# -*- coding: utf-8 -*-
"""Finansal Muhasebe · TMS/TFRS — 60 soru, 2026 test biçimi.

Gerçek kitapçıklarda standart soruları çoğunlukla standardın adı anılmadan, tutar veren bir olayla gelir
(yeniden değerleme, geliştirme maliyeti, yatırım amaçlı gayrimenkul, karşılık, hasılat); mevzuat/standart
atfı Finansal Muhasebe genelinde %15 düzeyindedir. Bu paket atfı yaklaşık üçte bir oranında tutar.

Dayanak (KGK tarafından yayımlanan 2026 yılında geçerli TMS/TFRS metinleri): TMS 1, 7, 8, 10, 16, 20, 21,
23, 36, 37, 38, 40, 41; TFRS 5, 9, 15, 16. Bütün tutarlar builder içinde hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K, taraf as T, hk

P = Paket("questions_topic_finansal_tms_tfrs_2026.json", lesson="finansal_muhasebe",
          topic="tms_tfrs", konu_adi="TMS/TFRS", seed=2026093065,
          surum="KGK TMS/TFRS 2026 seti (TMS 1, 7, 8, 10, 16, 20, 21, 23, 36-38, 40, 41; TFRS 5, 9, 15, 16)")

DOGRU = "Bu durumla ilgili aşağıdakilerden hangisi doğrudur?"

# ------------------------------------------------------------------ TMS 16
fiyat, gv, zemin, montaj, muh, rek, egt = 900_000, 90_000, 40_000, 35_000, 20_000, 25_000, 15_000
mal = fiyat + gv + zemin + montaj + muh
P.q("TMS 16 md. 16-20",
    f"İşletme yurt dışından {tl(fiyat)} ₺’ye bir makine satın almıştır. Makine için {tl(gv)} ₺ gümrük vergisi, {tl(zemin)} ₺ "
    f"zemin hazırlama, {tl(montaj)} ₺ montaj ve {tl(muh)} ₺ mühendislik ücreti ödenmiş; ayrıca yeni ürün için {tl(rek)} ₺ "
    f"reklam ve personele {tl(egt)} ₺ kullanım eğitimi verilmiştir.\n\nTMS 16 Maddi Duran Varlıklar’a göre makinenin "
    "ilk kayıt tutarı ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Makine {tl(mal)} ₺ ile aktifleştirilir.",
    [f"Makine {tl(mal + rek + egt)} ₺ ile aktifleştirilir.", f"Makine {tl(fiyat)} ₺ ile aktifleştirilir.",
     f"Makine {tl(mal + egt)} ₺ ile aktifleştirilir.", f"Makine {tl(fiyat + gv)} ₺ ile aktifleştirilir."],
    f"Maliyet; satın alma bedeli, iade edilmeyen vergiler ve varlığı kullanıma hazır hâle getirmek için doğrudan "
    f"katlanılan giderlerden oluşur: {tl(fiyat)} + {tl(gv)} + {tl(zemin)} + {tl(montaj)} + {tl(muh)} = {tl(mal)} ₺. Reklam "
    "ve personel eğitimi dönem gideridir.", zorluk="hard")

P.q("TMS 16 md. 16(c)",
    "Enerji şirketi kurduğu rüzgâr santrali için arazi sahibiyle yaptığı sözleşme gereği, santrali 20 yıl sonra söküp "
    "araziyi eski hâline getirmeyi taahhüt etmiştir. Söküm ve restorasyon maliyetinin bugünkü değeri 1.200.000 ₺ olarak "
    f"tahmin edilmiştir.\n\n{DOGRU}",
    "Bugünkü değer santralin maliyetine eklenir, karşılık ayrılır.",
    ["Tutar söküm yapıldığı yıl gider yazılır.",
     "Tutar sadece dipnotlarda açıklanır.",
     "Bugünkü değer özkaynaklarda yedek olarak ayrılır.",
     "Tutar 20 yıl boyunca her yıl eşit gider tahakkuk ettirilir, maliyete eklenmez."],
    "Varlığın sökülmesi ve yerinin restorasyonu için üstlenilen yükümlülüğün ilk tahmini maliyet unsurudur; bugünkü "
    "değeri varlığın maliyetine eklenir ve aynı tutarda karşılık (yükümlülük) kaydedilir.")

P.q("TMS 16 md. 39",
    "Yeniden değerleme modelini uygulayan işletmenin idari binasının net defter değeri 2.000.000 ₺’dir. Yıl sonunda "
    "yapılan değerlemede binanın gerçeğe uygun değeri 2.600.000 ₺ olarak belirlenmiştir; bina daha önce yeniden "
    f"değerlemeye tabi tutulmamış ve değer düşüklüğü kaydedilmemiştir.\n\n{DOGRU}",
    T(522, "alacak", 600_000),
    [T(649, "alacak", 600_000), T(679, "alacak", 600_000), T(522, "alacak", 2_600_000), T(252, "alacak", 600_000)],
    "Yeniden değerlemeyle oluşan artış kâr veya zarara değil diğer kapsamlı gelire alınır ve özkaynakta birikir; THP’de "
    "522 MDV Yeniden Değerleme Artışları hesabına 600.000 ₺ alacak yazılır.")

P.q("TMS 16 md. 40",
    "Yeniden değerleme modelini uygulayan işletmenin deposu için önceki yıl 150.000 ₺ yeniden değerleme artışı "
    "özkaynağa alınmıştır. Bu yıl yapılan değerlemede deponun gerçeğe uygun değeri defter değerinin 200.000 ₺ altına "
    f"düşmüştür.\n\n{DOGRU}",
    "150.000 ₺ artıştan düşülür, 50.000 ₺ gider yazılır.",
    ["200.000 ₺’nin tamamı gider yazılır.",
     "200.000 ₺’nin tamamı yeniden değerleme artışından düşülür.",
     "50.000 ₺ artıştan düşülür, 150.000 ₺ gider yazılır.",
     "Değer azalışı kaydedilmez, dipnotta açıklanır."],
    "Değer azalışı önce aynı varlık için özkaynakta birikmiş yeniden değerleme artışından (150.000 ₺) düşülür; bu tutarı "
    "aşan 50.000 ₺ kâr veya zarara gider olarak yansıtılır.", zorluk="hard")

P.q("TMS 16 md. 43-47",
    "Havayolu şirketinin 400.000.000 ₺ maliyetli uçağının gövdesinin faydalı ömrü 25 yıl, motorlarının 8 yıl, kabin iç "
    "donanımının ise 5 yıldır. Şirket uçağı tek kalem olarak 25 yılda amortismana tabi tutmayı düşünmektedir.\n\n"
    f"{DOGRU}",
    "Önemli parçalar ayrı ayrı amortismana tabi tutulmalıdır.",
    ["Uçak tek kalem olarak 25 yılda amortismana tabi tutulur.",
     "Uçak en kısa ömür olan 5 yılda amortismana tabi tutulur.",
     "Parçaların ömürleri ortalanarak tek oran uygulanır.",
     "Motor ve kabin gider yazılır, sadece gövde aktifleştirilir."],
    "Toplam maliyet içinde önemli tutarı olan ve farklı faydalı ömre sahip her parça ayrı ayrı amortismana tabi tutulur "
    "(bileşen yaklaşımı); gövde, motor ve kabin kendi ömürlerine göre itfa edilir.")

P.q("TMS 16 md. 12",
    "Bir lojistik işletmesi kamyonlarının yağ değişimi, filtre yenileme ve lastik rotasyonu gibi düzenli bakımları için "
    "yıl içinde 180.000 ₺ harcamıştır. Bu harcamalar araçların faydalı ömrünü uzatmamakta ve kapasitesini "
    f"artırmamaktadır.\n\n{DOGRU}",
    "Harcamalar oluştukları dönemde gider yazılır.",
    ["Harcamalar kamyonların maliyetine eklenir.",
     "Harcamalar ayrı bir maddi duran varlık olarak aktifleştirilir.",
     "Harcamalar gelecek yıllara ait gider olarak ertelenir.",
     "Harcamalar birikmiş amortismandan düşülür."],
    "Günlük bakım ve onarım maliyetleri (işçilik, sarf malzemesi, küçük parçalar) maddi duran varlığın defter değerine "
    "eklenmez; oluştukları dönemde kâr veya zararda gider olarak muhasebeleştirilir.", zorluk="easy")

m, omur, gecen, yeni_kalan = 600_000, 10, 4, 4
ndd = m - m * gecen // omur
P.q("TMS 16 md. 51; TMS 8 md. 36",
    f"İşletme {tl(m)} ₺’ye aldığı makineyi 10 yıllık faydalı ömürle eşit tutarlı yöntemle amortismana tabi tutmaktadır. "
    f"Dört yıl sonra yapılan incelemede teknolojik gelişmeler nedeniyle makinenin kalan faydalı ömrünün 4 yıl olduğu "
    "tahmin edilmiştir; kalıntı değer yoktur.\n\nBeşinci yıl ayrılacak amortisman ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    f"Kalan {tl(ndd)} ₺ dört yıla bölünür: yıllık {tl(ndd // yeni_kalan)} ₺.",
    [f"Maliyet yeni toplam ömre bölünür: yıllık {tl(m // 8)} ₺.",
     f"Eski oranla devam edilir: yıllık {tl(m // omur)} ₺.",
     f"Geçmiş yıllar düzeltilir, bu yıl yıllık {tl(m // 8)} ₺ ayrılır.",
     f"Kalan {tl(ndd)} ₺ bu yıl tamamen gider yazılır."],
    f"Faydalı ömür değişikliği muhasebe tahmini değişikliğidir ve ileriye dönük uygulanır: net defter değeri {tl(ndd)} ₺ "
    f"kalan 4 yıla dağıtılır, yıllık {tl(ndd // yeni_kalan)} ₺. Geçmiş dönemler düzeltilmez.", zorluk="hard")

P.q("TMS 16 md. 50-53",
    "İşletme 500.000 ₺’ye aldığı bir iş makinesinin 9 yıl kullanılacağını ve sonunda 50.000 ₺’ye satılabileceğini "
    "tahmin etmiştir. Eşit tutarlı amortisman yöntemi uygulanacak ve kalıntı değer tahmini güvenilir kabul edilmiştir."
    "\n\nYıllık amortisman tutarı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kalıntı değer düşülür, yıllık 50.000 ₺ amortisman ayrılır.",
    ["Kalıntı değer dikkate alınmaz, yıllık 55.555 ₺ amortisman ayrılır.",
     "Kalıntı değer eklenir, yıllık 61.111 ₺ amortisman ayrılır.",
     "Son yıl kalıntı değer kadar ek amortisman ayrılır.",
     "Kalıntı değer ilk yıl gelir yazılır, yıllık 55.555 ₺ ayrılır."],
    "Amortismana tabi tutar, maliyetten kalıntı değer düşülerek bulunur: (500.000 − 50.000) / 9 = 50.000 ₺ yıllık "
    "amortisman.")

# ------------------------------------------------------------------ TMS 38
ar, gel_once, gel_sonra = 300_000, 120_000, 450_000
P.q("TMS 38 md. 54-57",
    f"İlaç şirketi yıl içinde yeni bir etken madde için {tl(ar)} ₺ laboratuvar araştırması yapmıştır. Ardından ürünün "
    f"geliştirme aşamasında, teknik uygulanabilirlik ve ticarileştirme koşulları sağlanmadan önce {tl(gel_once)} ₺, "
    f"koşulların tamamı sağlandıktan sonra {tl(gel_sonra)} ₺ harcanmıştır.\n\nTMS 38 Maddi Olmayan Duran Varlıklar’a "
    "göre aktifleştirilecek tutar ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Sadece {tl(gel_sonra)} ₺ maddi olmayan duran varlık olarak kaydedilir.",
    [f"{tl(ar + gel_once + gel_sonra)} ₺ maddi olmayan duran varlık olarak kaydedilir.",
     f"{tl(gel_once + gel_sonra)} ₺ maddi olmayan duran varlık olarak kaydedilir.",
     f"{tl(ar)} ₺ maddi olmayan duran varlık olarak kaydedilir.",
     "Tutarların hepsi gider yazılır, aktifleştirme yapılmaz."],
    f"Araştırma harcamaları gider yazılır. Geliştirme harcamaları ancak standarttaki koşulların tamamı sağlandıktan sonra "
    f"aktifleştirilir; öncesinde yapılan {tl(gel_once)} ₺ geriye dönük aktifleştirilemez. Aktifleşen tutar {tl(gel_sonra)} ₺.",
    zorluk="hard")

P.q("TMS 38 md. 48-64",
    "Bir hazır giyim şirketinin yönetimi, yıllar içinde kendi çabasıyla bilinirliğini artırdığı markasının değerinin "
    "15.000.000 ₺ olduğunu bir danışmanlık raporuyla belirlemiştir. Şirket ayrıca bir yıl önce başka bir firmadan bir "
    "marka satın almıştır.\n\nAşağıdakilerden hangisi finansal durum tablosunda varlık olarak gösterilemez?",
    "İşletmenin kendi yarattığı markanın değeri",
    ["Başka firmadan satın alınan marka",
     "Satın alınan bir yazılım lisansı",
     "Koşulları sağlanmış geliştirme maliyeti",
     "Satın alınan bir patent hakkı"],
    "İşletme içinde yaratılan markalar, yayın hakları ve müşteri listeleri maliyeti işletmenin bütününden ayrılamadığı "
    "için maddi olmayan duran varlık olarak kaydedilemez; satın alınan marka ise kaydedilir.")

P.q("TMS 38 md. 88-108",
    "İşletme süresiz olarak yenilenebilen ve yenileme maliyeti önemsiz olan bir yayın lisansını 6.000.000 ₺’ye satın "
    "almıştır. Lisansın nakit girişi sağlayacağı sürenin öngörülebilir bir sınırı bulunmamaktadır.\n\n"
    f"{DOGRU}",
    "İtfa edilmez; en az yılda bir değer düşüklüğü testi yapılır.",
    ["Kanuni olarak 20 yılda eşit tutarlarla itfa edilir.",
     "Satın alındığı yıl tamamen gider yazılır.",
     "Maliyet modeli seçilemez, gerçeğe uygun değerle izlenir.",
     "10 yıllık varsayımsal ömürle itfa edilir, test yapılmaz."],
    "Sınırsız yararlı ömürlü maddi olmayan duran varlıklar itfa edilmez; her yıl ve değer düşüklüğü belirtisi olduğunda "
    "değer düşüklüğü testine tabi tutulur ve ömrün sınırsız olup olmadığı her dönem gözden geçirilir.")

P.q("TMS 38 md. 57; THP 263",
    "Yazılım şirketi geliştirdiği muhasebe programı için teknik uygulanabilirlik, satma niyeti ve yeterli kaynak dâhil "
    "tüm koşulların sağlandığı tarihten sonra 780.000 ₺ personel ve test gideri harcamıştır. Şirket THP kullanmaktadır ve "
    "harcamalar bankadan ödenmiştir.\n\nAktifleştirmeye ilişkin kayıt için aşağıdakilerden hangisi doğrudur?",
    T(263, "borç", 780_000),
    [T(180, "borç", 780_000), T(770, "borç", 780_000), T(260, "borç", 780_000), T(263, "alacak", 780_000)],
    "Koşulları sağlanmış geliştirme harcamaları maddi olmayan duran varlık olarak aktifleştirilir; THP’de 263 Araştırma "
    "ve Geliştirme Giderleri hesabına borç yazılır ve ürün kullanıma hazır olunca itfa edilir.")

# ------------------------------------------------------------------ TMS 40
P.q("TMS 40 md. 35",
    "Gerçeğe uygun değer modelini seçen işletmenin kira geliri elde etmek için elinde tuttuğu iş merkezinin yıl başındaki "
    "değeri 12.000.000 ₺, yıl sonundaki gerçeğe uygun değeri 13.500.000 ₺’dir. Bina işletme tarafından "
    f"kullanılmamaktadır.\n\n{DOGRU}",
    "1.500.000 ₺ artış kâr veya zarara yansıtılır; amortisman ayrılmaz.",
    ["1.500.000 ₺ artış özkaynakta yeniden değerleme fonuna alınır.",
     "Artış kaydedilmez, bina maliyetle izlenir ve amortisman ayrılır.",
     "1.500.000 ₺ artış kâra yansıtılır ve ayrıca amortisman ayrılır.",
     "Artış bina satılınca gelir yazılır, o zamana kadar dipnotta açıklanır."],
    "Yatırım amaçlı gayrimenkulde gerçeğe uygun değer modelinde değer değişimleri oluştukları dönemde kâr veya zarara "
    "yansıtılır ve amortisman ayrılmaz.", zorluk="hard")

P.q("TMS 40 md. 5-9",
    "İnşaat şirketinin elinde üç gayrimenkul vardır: satmak amacıyla inşa ettiği konutlar, genel müdürlük olarak "
    "kullandığı bina ve uzun süreli faaliyet kiralamasıyla başka bir şirkete kiraladığı ofis katları.\n\nBu "
    "gayrimenkullerden hangisi yatırım amaçlı gayrimenkul olarak sınıflandırılır?",
    "Faaliyet kiralamasıyla kiraya verilen ofis katları",
    ["Satmak amacıyla inşa edilen konutlar",
     "Genel müdürlük olarak kullanılan bina",
     "Konutlar ve genel müdürlük binası birlikte",
     "Üç gayrimenkulün tamamı"],
    "Kira geliri veya değer artışı amacıyla elde tutulan gayrimenkul yatırım amaçlıdır. Olağan faaliyet akışında satılmak "
    "üzere inşa edilenler stok, işletmenin kendi kullanımındakiler maddi duran varlıktır.", zorluk="easy")

P.q("TMS 40 md. 56-79",
    "Yatırım amaçlı gayrimenkulleri için maliyet modelini seçen işletme, bu gayrimenkulleri 8.000.000 ₺ maliyet ve "
    "1.200.000 ₺ birikmiş amortismanla izlemektedir. Bağımsız değerleme şirketi yıl sonunda gerçeğe uygun değeri "
    f"9.100.000 ₺ olarak belirlemiştir.\n\n{DOGRU}",
    "Maliyetle izlenir, gerçeğe uygun değer dipnotta açıklanır.",
    ["Gerçeğe uygun değere yükseltilir, fark kâra yansıtılır.",
     "Gerçeğe uygun değere yükseltilir, fark özkaynağa alınır.",
     "Amortisman durdurulur, değer artışı ertelenir.",
     "Maliyet modeli seçilse de değerleme yıl sonunda kayda alınır."],
    "Maliyet modelinde yatırım amaçlı gayrimenkuller maddi duran varlıklardaki maliyet modeline göre (amortismanla) "
    "izlenir; gerçeğe uygun değer kayda alınmaz ancak dipnotlarda açıklanır.")

# ------------------------------------------------------------------ TMS 36
dd, gus, kd = 900_000, 780_000, 820_000
P.q("TMS 36 md. 18-59",
    f"Yıl sonunda değer düşüklüğü belirtisi bulunan bir üretim hattının defter değeri {tl(dd)} ₺’dir. Hattın gerçeğe uygun "
    f"değerinden satış maliyetleri düşülmüş tutarı {tl(gus)} ₺, gelecekte sağlayacağı nakit akışlarının bugünkü değeri "
    f"(kullanım değeri) {tl(kd)} ₺’dir.\n\nTMS 36 Varlıklarda Değer Düşüklüğü’ne göre aşağıdakilerden hangisi "
    "doğrudur?",
    f"Geri kazanılabilir tutar {tl(kd)} ₺, değer düşüklüğü {tl(dd - kd)} ₺’dir.",
    [f"Geri kazanılabilir tutar {tl(gus)} ₺, değer düşüklüğü {tl(dd - gus)} ₺’dir.",
     f"Geri kazanılabilir tutar {tl((gus + kd) // 2)} ₺, değer düşüklüğü {tl(dd - (gus + kd) // 2)} ₺’dir.",
     f"Geri kazanılabilir tutar {tl(dd)} ₺, değer düşüklüğü yoktur.",
     f"Geri kazanılabilir tutar {tl(kd)} ₺, değer düşüklüğü {tl(dd - gus)} ₺’dir."],
    f"Geri kazanılabilir tutar, gerçeğe uygun değerden satış maliyetleri düşülmüş tutar ile kullanım değerinden yüksek "
    f"olanıdır: {tl(kd)} ₺. Defter değeri bunu {tl(dd - kd)} ₺ aştığından bu tutar değer düşüklüğü zararıdır.",
    zorluk="hard")

P.q("TMS 36 md. 12",
    "Bir işletme varlıklarında değer düşüklüğü belirtisi olup olmadığını değerlendirmektedir. Dönem içinde piyasa faiz "
    "oranları belirgin biçimde artmış, bir makine fiziksel hasar görmüş, bir tesisin yeniden yapılandırılması planlanmış "
    "ve rakip ürün nedeniyle satışlar düşmüştür.\n\nAşağıdakilerden hangisi değer düşüklüğü için iç kaynaklı bir "
    "belirtidir?",
    "Makinenin fiziksel hasar görmesi",
    ["Piyasa faiz oranlarının belirgin biçimde artması",
     "Rakip ürün nedeniyle pazar koşullarının kötüleşmesi",
     "Varlığın piyasa değerinin beklenenden fazla düşmesi",
     "Net varlıkların piyasa değerinin üzerinde olması"],
    "Varlığın fiziksel hasarı, eskimesi veya yeniden yapılandırma planı iç kaynaklı belirtilerdir; faiz oranlarındaki "
    "artış, piyasa değerinin düşmesi ve olumsuz pazar koşulları dış kaynaklı belirtilerdir.")

P.q("TMS 36 md. 124",
    "İşletme geçmiş yıllarda şerefiye, bir makine, bir marka ve bir yatırım amaçlı olmayan bina için değer düşüklüğü "
    "zararı kaydetmiştir. Bu yıl koşullar düzelmiş ve varlıkların geri kazanılabilir tutarları belirgin biçimde "
    "artmıştır.\n\nAşağıdakilerden hangisi için kaydedilmiş değer düşüklüğü zararı iptal edilemez?",
    "Şerefiye",
    ["Makine", "Marka", "Bina", "Makine ve bina birlikte"],
    "Şerefiye için ayrılan değer düşüklüğü zararı sonraki dönemlerde iptal edilemez. Diğer varlıklarda iptal, değer "
    "düşüklüğü hiç kaydedilmeseydi oluşacak defter değerini aşmamak koşuluyla yapılır.", zorluk="easy")

P.q("TMS 36 md. 60-61",
    "Yeniden değerleme modelini uygulayan işletmenin bir binası için özkaynakta 300.000 ₺ yeniden değerleme artışı "
    "bulunmaktadır. Yıl sonunda yapılan testte binada 380.000 ₺ değer düşüklüğü tespit edilmiştir.\n\n"
    f"{DOGRU}",
    "300.000 ₺ artıştan düşülür, 80.000 ₺ kâr veya zarara yansır.",
    ["380.000 ₺’nin tamamı kâr veya zarara yansıtılır.",
     "380.000 ₺’nin tamamı yeniden değerleme artışından düşülür.",
     "80.000 ₺ artıştan düşülür, 300.000 ₺ kâr veya zarara yansır.",
     "Değer düşüklüğü yeniden değerlenen varlıkta kaydedilmez."],
    "Yeniden değerlenmiş varlıktaki değer düşüklüğü, önce aynı varlığa ait yeniden değerleme artışı (300.000 ₺) "
    "tutarına kadar diğer kapsamlı gelirde azalış olarak, aşan kısım (80.000 ₺) kâr veya zararda muhasebeleştirilir.",
    zorluk="hard")

# ------------------------------------------------------------------ TMS 37
P.q("TMS 37 md. 14-26",
    "Bir müşteri işletmeye ayıplı mal teslimi nedeniyle tazminat davası açmıştır. Hukuk müşaviri yıl sonunda davanın "
    "kaybedilme olasılığını %70 olarak değerlendirmiş ve ödenmesi gereken tutarın güvenilir biçimde 400.000 ₺ olacağını "
    f"tahmin etmiştir.\n\n{DOGRU}",
    "400.000 ₺ karşılık ayrılır ve gider yazılır.",
    ["Tutar sadece dipnotta koşullu yükümlülük olarak açıklanır.",
     "280.000 ₺ karşılık ayrılır, kalan kısım dipnotta açıklanır.",
     "Dava sonuçlanana kadar kayıt yapılmaz ve açıklama gerekmez.",
     "400.000 ₺ özkaynaklarda yedek olarak ayrılır."],
    "Geçmiş bir olaydan doğan mevcut bir yükümlülük vardır, kaynak çıkışı muhtemeldir (%50’den fazla) ve tutar güvenilir "
    "tahmin edilebilmektedir; bu nedenle en iyi tahmin olan 400.000 ₺ karşılık ayrılır.", zorluk="hard")

P.q("TMS 37 md. 27-30",
    "İşletme aleyhine açılan bir davada hukuk müşaviri, davanın kaybedilme olasılığının %20 olduğunu ve kaybedilmesi "
    "hâlinde yaklaşık 900.000 ₺ ödeme yapılacağını bildirmiştir. Olasılık uzak değildir ancak muhtemel de "
    "sayılmamaktadır.\n\nTMS 37 Karşılıklar, Koşullu Borçlar ve Koşullu Varlıklar’a göre aşağıdakilerden hangisi "
    "doğrudur?",
    "Koşullu yükümlülük olarak dipnotta açıklanır.",
    ["900.000 ₺ karşılık ayrılır ve gider yazılır.",
     "180.000 ₺ karşılık ayrılır ve gider yazılır.",
     "Açıklama yapılmaz, dava sonucu beklenir.",
     "Tutar gelecek yıllara ait gider olarak ertelenir."],
    "Kaynak çıkışı muhtemel olmadığından karşılık ayrılmaz; olasılık uzak da olmadığından koşullu yükümlülük olarak "
    "dipnotlarda niteliği ve tahmini etkisiyle açıklanır.")

adet, p1, k1, p2, k2 = 10_000, 0.05, 200, 0.02, 1_000
gar = int(adet * (p1 * k1 + p2 * k2))
P.q("TMS 37 md. 39",
    "İşletme yıl içinde bir yıl garantili 10.000 adet ürün satmıştır." +
    " Geçmiş verilere göre ürünlerin %5’inde küçük arıza (ürün başına 200 ₺ onarım), %2’sinde büyük arıza (ürün başına "
    "1.000 ₺ onarım) çıkması, kalanında arıza çıkmaması beklenmektedir.\n\nAyrılacak garanti karşılığı ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    f"Beklenen değer yöntemiyle {tl(gar)} ₺ karşılık ayrılır.",
    [f"En olası sonuç arıza çıkmaması olduğundan karşılık ayrılmaz.",
     f"Büyük arızalar için {tl(adet * p2 * k2)} ₺ karşılık ayrılır.",
     f"Tüm ürünlerin büyük arıza vereceği varsayımıyla {tl(adet * k2)} ₺ ayrılır.",
     f"Küçük arızalar için {tl(adet * p1 * k1)} ₺ karşılık ayrılır."],
    f"Çok sayıda kalemden oluşan yükümlülükte en iyi tahmin beklenen değerdir: 10.000 × (%5 × 200 + %2 × 1.000) = "
    f"{tl(gar)} ₺.", zorluk="hard")

P.q("TMS 37 md. 31-35",
    "Bir işletme rakibine karşı açtığı patent ihlali davasında, avukatlarının değerlendirmesine göre yaklaşık 2.000.000 ₺ "
    "tazminat kazanma olasılığının yüksek olduğunu öğrenmiştir. Ancak yıl sonu itibarıyla mahkeme kararı "
    f"verilmemiştir.\n\n{DOGRU}",
    "Koşullu varlık olarak dipnotta açıklanır, kayda alınmaz.",
    ["2.000.000 ₺ alacak ve gelir olarak kaydedilir.",
     "Olasılık oranında alacak ve gelir kaydedilir.",
     "Açıklama yapılmaz, kayıt da yapılmaz.",
     "Tutar özkaynaklarda ayrı bir fonda gösterilir."],
    "Koşullu varlıklar kaydedilmez, çünkü hiç gerçekleşmeyecek bir gelirin kaydına yol açabilir; ekonomik yarar girişi "
    "muhtemel ise dipnotlarda açıklanır. Gerçekleşmesi neredeyse kesinleşirse varlık kaydedilir.")

P.q("TMS 37 md. 63-65",
    "Bir perakende zinciri gelecek yıl açacağı yeni mağazaların ilk yılında yaklaşık 3.000.000 ₺ faaliyet zararı "
    "oluşacağını, ayrıca bir tedarikçiyle yaptığı ve iptal edilemeyen bir sözleşmeden 400.000 ₺ kayıp doğacağını tahmin "
    "etmektedir.\n\nAşağıdakilerden hangisi için karşılık ayrılmaz?",
    "Yeni mağazaların beklenen faaliyet zararları",
    ["İptal edilemeyen dezavantajlı sözleşmeden doğacak kayıp",
     "Kaybedilmesi muhtemel bir dava tazminatı",
     "Satılan ürünlerin garanti yükümlülüğü",
     "Yasal zorunluluk olan çevre temizliği maliyeti"],
    "Gelecekteki faaliyet zararları için karşılık ayrılmaz; yükümlülük değildir. Ekonomik açıdan dezavantajlı "
    "sözleşmelerde ise mevcut yükümlülük karşılık olarak muhasebeleştirilir.", zorluk="hard")

# ------------------------------------------------------------------ TFRS 15
P.q("TFRS 15 md. IN7",
    "Bir yazılım şirketinin muhasebe ekibi, müşteri sözleşmelerinden doğan hasılatı yeni standarda göre ölçerken "
    "izlenecek adımları sıraya koymaktadır: işlem bedelinin belirlenmesi, sözleşmenin belirlenmesi, edim "
    "yükümlülüklerinin belirlenmesi, hasılatın muhasebeleştirilmesi ve işlem bedelinin dağıtılması.\n\nDoğru sıralama "
    "aşağıdakilerden hangisidir?",
    "Sözleşme → edim yükümlülükleri → işlem bedeli → dağıtım → hasılat",
    ["Edim yükümlülükleri → sözleşme → işlem bedeli → dağıtım → hasılat",
     "Sözleşme → işlem bedeli → edim yükümlülükleri → hasılat → dağıtım",
     "İşlem bedeli → sözleşme → dağıtım → edim yükümlülükleri → hasılat",
     "Sözleşme → dağıtım → işlem bedeli → edim yükümlülükleri → hasılat"],
    "Beş adım: müşteriyle sözleşmenin belirlenmesi, edim yükümlülüklerinin belirlenmesi, işlem bedelinin belirlenmesi, "
    "işlem bedelinin edim yükümlülüklerine dağıtılması ve edim yükümlülükleri yerine getirildikçe hasılatın kaydı.")

bedel, t1, t2 = 30_000, 20_000, 20_000
P.q("TFRS 15 md. 73-80",
    f"Bir operatör 24 ay taahhütlü paketinde müşteriye bir telefon ve iletişim hizmetini toplam {tl(bedel)} ₺’ye "
    f"satmaktadır. Telefonun tek başına satış fiyatı {tl(t1)} ₺, 24 aylık hizmetin tek başına satış fiyatı "
    f"{tl(t2)} ₺’dir; telefon sözleşme başında teslim edilmiştir.\n\nTFRS 15 Müşteri Sözleşmelerinden Hasılat’a göre "
    "aşağıdakilerden hangisi doğrudur?",
    f"Telefon teslimde {tl(bedel * t1 // (t1 + t2))} ₺, hizmet 24 ayda {tl(bedel * t2 // (t1 + t2))} ₺ hasılat olur.",
    [f"Telefon teslimde {tl(bedel)} ₺ hasılat olur, hizmet bedelsizdir.",
     f"Telefon teslimde {tl(t1)} ₺, hizmet 24 ayda {tl(bedel - t1)} ₺ hasılat olur.",
     f"Hizmet 24 ayda {tl(bedel)} ₺ hasılat olur, telefon için hasılat yoktur.",
     f"Telefon teslimde {tl(bedel - t2)} ₺, hizmet 24 ayda {tl(t2)} ₺ hasılat olur."],
    f"İşlem bedeli edim yükümlülüklerine tek başına satış fiyatları oranında dağıtılır: {tl(bedel)} × 20/40 = "
    f"{tl(bedel // 2)} ₺ telefona (teslimde), {tl(bedel // 2)} ₺ hizmete (24 ay boyunca) düşer.", zorluk="hard")

P.q("TFRS 15 md. 35-37",
    "Bir spor salonu 1 Ekim’de müşterisinden 12 aylık üyelik bedeli olarak 12.000 ₺ peşin tahsil etmiştir. Müşteri salon "
    "hizmetinden yıl boyunca istediği zaman yararlanabilmekte, salon da hizmeti her gün sunmaya hazır "
    "bulunmaktadır.\n\nİşletmenin yıl sonu itibarıyla hasılat ve yükümlülüğü ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "3.000 ₺ hasılat, 9.000 ₺ sözleşme yükümlülüğü vardır.",
    ["12.000 ₺ hasılat, yükümlülük yoktur.",
     "Hasılat yoktur, 12.000 ₺ sözleşme yükümlülüğü vardır.",
     "9.000 ₺ hasılat, 3.000 ₺ sözleşme yükümlülüğü vardır.",
     "6.000 ₺ hasılat, 6.000 ₺ sözleşme yükümlülüğü vardır."],
    "Hizmet zamanla yerine getirildiğinden hasılat zamana yayılır: ekim-aralık üç ay için 12.000 × 3/12 = 3.000 ₺. "
    "Kalan 9.000 ₺ henüz sunulmamış hizmet için sözleşme yükümlülüğüdür.")

P.q("TFRS 15 md. B34-B38",
    "Bir çevrim içi pazaryeri, üçüncü taraf satıcıların ürünlerini kendi sitesinde listeleyip satışlara aracılık "
    "etmektedir. Ürünlerin kontrolü satış sürecinde pazaryerine geçmemekte, pazaryeri 1.000 ₺’lik her satıştan 120 ₺ "
    "komisyon almaktadır.\n\nPazaryerinin kaydedeceği hasılat ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Satış başına 120 ₺ komisyon hasılat olarak kaydedilir.",
    ["Satış başına 1.000 ₺ hasılat, 880 ₺ satış maliyeti kaydedilir.",
     "Satış başına 880 ₺ hasılat kaydedilir.",
     "Satış başına 1.000 ₺ hasılat kaydedilir, komisyon gider yazılır.",
     "Hasılat kaydedilmez, komisyon özkaynağa alınır."],
    "Malların kontrolünü müşteriye devretmeden önce elde bulundurmayan işletme vekil konumundadır ve hasılatı net "
    "tutar, yani aldığı 120 ₺ komisyon üzerinden kaydeder.")

adet2, fiyat2, iade = 100, 500, 0.05
P.q("TFRS 15 md. 50-58; B20-B27",
    f"İşletme 30 gün içinde koşulsuz iade hakkı tanıyarak {adet2} adet ürünü tanesi {fiyat2} ₺’den nakit satmıştır. "
    "Geçmiş deneyime göre ürünlerin %5’inin iade edileceği güvenilir biçimde tahmin edilmektedir; iade dönemi yıl "
    "sonunda dolmamıştır.\n\nBu satışla ilgili aşağıdakilerden hangisi doğrudur?",
    f"{tl(adet2 * fiyat2 * (1 - iade))} ₺ hasılat ve {tl(adet2 * fiyat2 * iade)} ₺ iade yükümlülüğü kaydedilir.",
    [f"{tl(adet2 * fiyat2)} ₺ hasılat kaydedilir, iadeler gerçekleşince düzeltilir.",
     f"İade süresi dolana kadar hasılat kaydedilmez, {tl(adet2 * fiyat2)} ₺ yükümlülük kaydedilir.",
     f"{tl(adet2 * fiyat2 * (1 - iade))} ₺ hasılat kaydedilir, fark özkaynağa alınır.",
     f"{tl(adet2 * fiyat2)} ₺ hasılat ve {tl(adet2 * fiyat2 * iade)} ₺ gider karşılığı kaydedilir."],
    f"İade hakkı değişken bedel doğurur; hasılat iade beklenmeyen ürünler için kaydedilir: 50.000 × %95 = "
    f"{tl(adet2 * fiyat2 * (1 - iade))} ₺. İade edilmesi beklenen {tl(adet2 * fiyat2 * iade)} ₺ iade yükümlülüğüdür.",
    zorluk="hard")

P.q("TFRS 15 md. 60-65",
    "Bir makine üreticisi, peşin fiyatı 1.000.000 ₺ olan makineyi müşterisine iki yıl sonra tek seferde 1.210.000 ₺ "
    "ödenmek üzere satmış ve teslim etmiştir. Aradaki fark piyasa faiz oranını yansıtmakta ve önemli bir finansman "
    f"bileşeni oluşturmaktadır.\n\n{DOGRU}",
    "Teslimde 1.000.000 ₺ hasılat, fark iki yılda faiz geliri olur.",
    ["Teslimde 1.210.000 ₺ hasılat kaydedilir.",
     "Hasılat tahsil tarihinde 1.210.000 ₺ olarak kaydedilir.",
     "Hasılat iki yıla eşit dağıtılarak kaydedilir.",
     "Teslimde 1.000.000 ₺ hasılat, 210.000 ₺ bugün faiz geliri olur."],
    "Önemli finansman bileşeni içeren sözleşmede hasılat, malın nakit satış fiyatını yansıtan tutarla (1.000.000 ₺) "
    "kaydedilir; 210.000 ₺ fark vade boyunca etkin faiz yöntemiyle faiz geliri olarak tanınır.", zorluk="hard")

P.q("TFRS 15 md. B28-B33",
    "Beyaz eşya üreticisi ürünlerini yasal iki yıllık garantiyle satmakta, ayrıca müşterilere ücret karşılığında üç yıl "
    "daha uzatılmış garanti ve periyodik bakım hizmeti sunmaktadır. Uzatılmış garanti ayrıca satın alınabilmektedir."
    f"\n\n{DOGRU}",
    "Uzatılmış garanti ayrı bir edim yükümlülüğüdür.",
    ["Uzatılmış garanti ürün satışının parçasıdır, ayrılmaz.",
     "Yasal garanti ayrı bir edim yükümlülüğüdür.",
     "Her iki garanti için sadece karşılık ayrılır.",
     "Garantiler için hasılat satış anında tamamen kaydedilir."],
    "Müşteriye ayrıca satın alma seçeneği sunulan ve ürünün şartnameye uygunluğu güvencesinin ötesinde hizmet sağlayan "
    "garanti ayrı edim yükümlülüğüdür; işlem bedelinin bir kısmı buna dağıtılır. Güvence türü yasal garanti ise TMS 37’ye "
    "göre karşılıkla izlenir.")

P.q("TFRS 15 md. 91-94",
    "Bir danışmanlık şirketi üç yıllık bir hizmet sözleşmesi kazanmış ve satış temsilcisine sadece sözleşmenin "
    "imzalanmasına bağlı olarak 90.000 ₺ komisyon ödemiştir. Sözleşmeden elde edilecek gelirlerin bu maliyeti "
    "karşılaması beklenmektedir.\n\nKomisyonun muhasebeleştirilmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Varlık olarak kaydedilir ve sözleşme süresince itfa edilir.",
    ["Ödendiği dönemde tamamen gider yazılır.",
     "Hasılattan indirilerek net hasılat gösterilir.",
     "Özkaynaklardan doğrudan düşülür.",
     "Sözleşme bitince tek seferde gider yazılır."],
    "Sözleşme elde etmenin ek maliyetleri (sözleşme kazanılmasaydı katlanılmayacak komisyon), geri kazanılması "
    "bekleniyorsa varlık olarak kaydedilir ve ilgili hizmetin devri boyunca itfa edilir; itfa süresi bir yıldan kısaysa "
    "gider yazılabilir.", zorluk="hard")

# ------------------------------------------------------------------ TFRS 16
bd, pesin, komis = 380_000, 20_000, 10_000
khv = bd + pesin + komis
P.q("TFRS 16 md. 23-24",
    f"İşletme bir depoyu beş yıllığına kiralamıştır. Kira ödemelerinin kiralamanın başlangıcındaki bugünkü değeri "
    f"{tl(bd)} ₺’dir. Başlangıç tarihinde kiraya verene {tl(pesin)} ₺ peşin kira ödenmiş, emlakçıya {tl(komis)} ₺ komisyon "
    "verilmiştir; kiralama teşviki alınmamıştır.\n\nTFRS 16 Kiralamalar’a göre kullanım hakkı varlığının ilk ölçümü "
    "ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Kullanım hakkı varlığı {tl(khv)} ₺, kira yükümlülüğü {tl(bd)} ₺’dir.",
    [f"Kullanım hakkı varlığı {tl(bd)} ₺, kira yükümlülüğü {tl(bd)} ₺’dir.",
     f"Kullanım hakkı varlığı {tl(bd + pesin)} ₺, kira yükümlülüğü {tl(bd + pesin)} ₺’dir.",
     f"Kullanım hakkı varlığı {tl(khv)} ₺, kira yükümlülüğü {tl(khv)} ₺’dir.",
     "Kullanım hakkı varlığı kaydedilmez, kira ödemeleri gider yazılır."],
    f"Kullanım hakkı varlığı = kira yükümlülüğünün ilk ölçümü ({tl(bd)} ₺) + başlangıçta yapılan kira ödemeleri "
    f"({tl(pesin)} ₺) + başlangıçtaki doğrudan maliyetler ({tl(komis)} ₺) = {tl(khv)} ₺.", zorluk="hard")

P.q("TFRS 16 md. 5-8",
    "İşletme bir fuar için 6 aylık süreyle bir stand alanı kiralamış (satın alma opsiyonu yoktur) ve çalışanları için "
    "yeni olarak birim değeri düşük tablet bilgisayarlar kiralamıştır. Her iki kiralama için de standardın izin verdiği "
    f"muafiyet seçilmiştir.\n\n{DOGRU}",
    "Kira ödemeleri kiralama süresince gider olarak kaydedilir.",
    ["Her iki kiralama için kullanım hakkı varlığı kaydedilir.",
     "Sadece tabletler için kullanım hakkı varlığı kaydedilir.",
     "Kira ödemeleri özkaynaktan doğrudan düşülür.",
     "Kira ödemeleri gelecek yıllara ait gider olarak ertelenir."],
    "Kısa vadeli kiralamalar (12 ay veya daha kısa) ile dayanak varlığın düşük değerli olduğu kiralamalarda kiracı "
    "muafiyeti seçebilir; bu durumda ödemeler doğrusal olarak gider yazılır, kullanım hakkı varlığı kaydedilmez.")

P.q("TFRS 16 md. 36-38",
    f"Kiracı işletmenin başlangıçta {tl(bd)} ₺ olarak ölçtüğü kira yükümlülüğü için zımni faiz oranı yıllık %10’dur. İlk "
    "yıl sonunda 100.000 ₺ kira ödemesi yapılmıştır; ödeme yıl sonunda gerçekleşmiştir.\n\nİlk yıl sonunda kira "
    "yükümlülüğü ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Faiz gideri {tl(bd // 10)} ₺, yıl sonu yükümlülüğü {tl(bd + bd // 10 - 100_000)} ₺’dir.",
    [f"Faiz gideri {tl(bd // 10)} ₺, yıl sonu yükümlülüğü {tl(bd - 100_000)} ₺’dir.",
     f"Faiz gideri yoktur, yıl sonu yükümlülüğü {tl(bd - 100_000)} ₺’dir.",
     f"Faiz gideri {tl(10_000)} ₺, yıl sonu yükümlülüğü {tl(bd + 10_000 - 100_000)} ₺’dir.",
     f"Faiz gideri {tl(bd // 10)} ₺, yıl sonu yükümlülüğü {tl(bd + bd // 10)} ₺’dir."],
    f"Faiz gideri = açılış yükümlülüğü × %10 = {tl(bd // 10)} ₺. Yıl sonu yükümlülük = {tl(bd)} + {tl(bd // 10)} − "
    f"100.000 = {tl(bd + bd // 10 - 100_000)} ₺.", zorluk="hard")

P.q("TFRS 16 md. 61-66",
    "Bir leasing şirketi bir iş makinesini ekonomik ömrünün büyük bölümünü kapsayan bir süreyle kiraya vermiştir. Süre "
    "sonunda mülkiyet kiracıya geçecek, kira ödemelerinin bugünkü değeri makinenin gerçeğe uygun değerine neredeyse "
    "eşittir.\n\nKiraya veren açısından bu kiralama ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Finansal kiralamadır; makine yerine kira alacağı kaydedilir.",
    ["Faaliyet kiralamasıdır; makine kiraya verenin bilançosunda kalır.",
     "Finansal kiralamadır; makine kiraya verende amortismana tabi tutulur.",
     "Kiraya veren sınıflama yapmaz, tüm kiralamalar faaliyet kiralamasıdır.",
     "Kira tahsilatları tahsil edildikçe tamamen hasılat yazılır."],
    "Dayanak varlığın mülkiyetine ilişkin risk ve getirilerin önemli ölçüde tamamını devreden kiralama finansal "
    "kiralamadır; kiraya veren varlığı bilançodan çıkarır ve net kiralama yatırımı tutarında alacak kaydeder.")

P.q("TFRS 16 md. 31-32",
    f"Kiracı işletme beş yıllık kiralama için kullanım hakkı varlığını {tl(khv)} ₺ olarak ölçmüştür. Süre sonunda "
    "mülkiyet devri veya satın alma opsiyonu yoktur; dayanak varlığın ekonomik ömrü 8 yıldır ve doğrusal yöntem "
    "uygulanacaktır.\n\nYıllık amortisman ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Kiralama süresi olan 5 yılda yıllık {tl(khv // 5)} ₺ amortisman ayrılır.",
    [f"Ekonomik ömür olan 8 yılda yıllık {tl(khv // 8)} ₺ amortisman ayrılır.",
     "Kullanım hakkı varlığı için amortisman ayrılmaz.",
     f"Kira yükümlülüğü üzerinden yıllık {tl(bd // 5)} ₺ amortisman ayrılır.",
     f"İlk yıl {tl(khv)} ₺’nin tamamı gider yazılır."],
    f"Mülkiyet devri veya kullanılması makul ölçüde kesin satın alma opsiyonu yoksa kullanım hakkı varlığı, kiralama "
    f"süresi ile yararlı ömürden kısa olanında amortismana tabi tutulur: {tl(khv)} / 5 = {tl(khv // 5)} ₺.")

# ------------------------------------------------------------------ TMS 23
ozf, gecici = 240_000, 30_000
P.q("TMS 23 md. 12-13",
    f"İşletme dokuz ay sürecek bir otel inşaatı için özel olarak kredi kullanmış ve inşaat döneminde {tl(ozf)} ₺ faiz "
    f"oluşmuştur. Kullanılmayan kredi tutarının geçici olarak mevduatta değerlendirilmesinden {tl(gecici)} ₺ faiz geliri "
    "elde edilmiştir.\n\nAktifleştirilecek borçlanma maliyeti ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"{tl(ozf - gecici)} ₺ otelin maliyetine eklenir.",
    [f"{tl(ozf)} ₺ otelin maliyetine eklenir, faiz geliri gelir yazılır.",
     f"{tl(ozf)} ₺ gider yazılır, aktifleştirme yapılmaz.",
     f"Faiz ve faiz geliri toplanarak {tl(ozf + gecici)} ₺ otelin maliyetine eklenir.",
     f"{tl(gecici)} ₺ otelin maliyetine eklenir, kalanı gider yazılır."],
    f"Özellikli varlık için özel olarak alınan borcun gerçekleşen maliyetinden, bu borcun geçici yatırımından elde edilen "
    f"gelir düşülerek aktifleştirilir: {tl(ozf)} − {tl(gecici)} = {tl(ozf - gecici)} ₺.", zorluk="hard")

P.q("TMS 23 md. 20-21",
    "Bir alışveriş merkezi inşaatı, işletmenin finansman sorunları nedeniyle altı ay süreyle tamamen durdurulmuştur. "
    "Durdurma teknik ya da idari bir zorunluluktan kaynaklanmamaktadır; bu sürede krediye 180.000 ₺ faiz "
    f"işlemiştir.\n\n{DOGRU}",
    "Duraklama süresindeki faiz aktifleştirilmez, gider yazılır.",
    ["Faiz inşaat maliyetine eklenmeye devam eder.",
     "Faiz inşaat bitince toplu olarak aktifleştirilir.",
     "Faizin yarısı aktifleştirilir, yarısı gider yazılır.",
     "Faiz özkaynaklarda ayrı bir fonda biriktirilir."],
    "Özellikli varlığın aktif geliştirilmesine uzun süre ara verilen dönemlerde borçlanma maliyetlerinin "
    "aktifleştirilmesine ara verilir; teknik veya idari zorunlu gecikmeler bu kuralın dışındadır.")

harc, oran, gercek = 1_000_000, 12, 150_000
P.q("TMS 23 md. 14",
    "İşletme özellikli bir varlık için yıl boyunca ortalama 1.000.000 ₺ harcama yapmış, bu harcamayı genel amaçlı "
    "borçlarından finanse etmiştir. Genel amaçlı borçların ağırlıklı ortalama maliyet oranı %12, dönem boyunca bu "
    "borçlar için katlanılan toplam faiz 150.000 ₺’dir.\n\nAktifleştirilecek tutar ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    f"{tl(harc * oran // 100)} ₺ aktifleştirilir, kalanı gider yazılır.",
    [f"{tl(gercek)} ₺’nin tamamı aktifleştirilir.",
     "Genel amaçlı borçlarda aktifleştirme yapılmaz.",
     f"{tl(gercek - harc * oran // 100)} ₺ aktifleştirilir, kalanı gider yazılır.",
     f"{tl(harc * oran // 100 + gercek)} ₺ aktifleştirilir."],
    f"Genel amaçlı borçlarda aktifleştirme oranı harcamalara uygulanır: 1.000.000 × %12 = {tl(harc * oran // 100)} ₺. "
    f"Bu tutar dönemde katlanılan toplam faizi ({tl(gercek)} ₺) aşamaz; kalan {tl(gercek - harc * oran // 100)} ₺ gider olur.",
    zorluk="hard")

# ------------------------------------------------------------------ TMS 20
mk, tes, om = 1_000_000, 200_000, 5
P.q("TMS 20 md. 24-27",
    f"İşletme bölgesel kalkınma programı kapsamında {tl(mk)} ₺’lik bir makine alımı için {tl(tes)} ₺ hibe almıştır; hibe "
    f"koşullarının tamamı yerine getirilmiştir. Makinenin faydalı ömrü {om} yıl, kalıntı değeri sıfırdır ve işletme "
    "hibeyi ertelenmiş gelir olarak sunmayı seçmiştir.\n\nHibeyle ilgili aşağıdakilerden hangisi doğrudur?",
    f"Hibe 5 yılda yılda {tl(tes // om)} ₺ gelire aktarılır.",
    [f"Hibe alındığı yıl {tl(tes)} ₺ gelir olarak kaydedilir.",
     f"Hibe {tl(tes)} ₺ olarak özkaynağa alınır.",
     f"Hibe makine maliyetine eklenir, amortisman {tl((mk + tes) // om)} ₺ olur.",
     "Hibe makine satılınca gelir olarak kaydedilir."],
    f"Varlıkla ilgili devlet teşvikleri ertelenmiş gelir olarak sunulur ve varlığın yararlı ömrü boyunca sistematik "
    f"olarak kâr veya zarara aktarılır: {tl(tes)} / {om} = {tl(tes // om)} ₺ yıllık gelir. Alternatif, varlıktan "
    "düşülerek sunumdur.")

P.q("TMS 20 md. 20-22",
    "İşletme, işsiz gençleri istihdam etmesi karşılığında bir kamu kurumundan, önceki yıl ödediği sosyal güvenlik "
    "primlerinin bir kısmını karşılamak üzere 120.000 ₺ destek almaya hak kazanmıştır. Destek için yerine getirilecek "
    f"başka bir koşul yoktur.\n\n{DOGRU}",
    "Tahsil hakkı doğduğu dönemde kâr veya zarara yansıtılır.",
    ["Özkaynaklarda ayrı bir fon olarak gösterilir.",
     "Ertelenmiş gelir olarak beş yıla yayılır.",
     "İlgili sosyal güvenlik giderlerinin geçmiş yıllarını düzeltir.",
     "Sadece nakit tahsil edildiğinde dipnotta açıklanır."],
    "Önceden katlanılmış giderler veya zararlar için ya da gelecekte ilgili maliyeti olmayan anında finansal destek "
    "amacıyla alınan teşvik, tahsil hakkının doğduğu dönemde kâr veya zarara yansıtılır.")

# ------------------------------------------------------------------ TMS 10
P.q("TMS 10 md. 8-9",
    "Raporlama dönemi 31 Aralık’ta sona eren işletmenin finansal tabloları 20 Mart’ta yayımlanacaktır. Aleyhine yıl "
    "içinde açılmış ve 250.000 ₺ karşılık ayrılmış bir dava 15 Şubat’ta sonuçlanmış, mahkeme 330.000 ₺ tazminata "
    f"hükmetmiştir.\n\n{DOGRU}",
    "Düzeltme gerektiren olaydır; karşılık 330.000 ₺’ye yükseltilir.",
    ["Düzeltme gerektirmeyen olaydır, sadece dipnotta açıklanır.",
     "Karşılık 250.000 ₺ bırakılır, fark gelecek yıl gider yazılır.",
     "Düzeltme gerektiren olaydır; karşılık iptal edilip 330.000 ₺ gelecek yıla ertelenir.",
     "Olay raporlama döneminden sonra olduğu için dikkate alınmaz."],
    "Raporlama dönemi sonunda var olan yükümlülüğü teyit eden sonraki mahkeme kararı düzeltme gerektiren olaydır; karşılık "
    "yeni bilgiye göre 330.000 ₺’ye düzeltilir.", zorluk="hard")

P.q("TMS 10 md. 10-11",
    "Raporlama dönemi 31 Aralık’ta sona eren işletmenin ana deposu 10 Şubat’ta çıkan yangında zarar görmüş ve 1.800.000 ₺ "
    "stok kaybı oluşmuştur. Finansal tablolar henüz yayımlanmamıştır ve yangın dönem sonundaki koşullarla ilgili "
    f"değildir.\n\n{DOGRU}",
    "Düzeltme gerektirmeyen olaydır, önemliyse dipnotta açıklanır.",
    ["Düzeltme gerektiren olaydır; stoklar 31 Aralık itibarıyla azaltılır.",
     "Stok kaybı geçmiş yıl zararı olarak özkaynaktan düşülür.",
     "Olay finansal tabloları etkilemez, açıklama gerekmez.",
     "Stoklar için 31 Aralık itibarıyla değer düşüklüğü karşılığı ayrılır."],
    "Raporlama döneminden sonra ortaya çıkan ve dönem sonundaki koşullarla ilgisi olmayan yangın düzeltme gerektirmeyen "
    "olaydır; tutarlar düzeltilmez, önemli ise niteliği ve finansal etkisi açıklanır.")

P.q("TMS 10 md. 12-13",
    "Raporlama dönemi 31 Aralık’ta sona eren şirketin yönetim kurulu, finansal tablolar yayımlanmadan önce 25 Şubat’ta "
    "geçen yılın kârından ortaklara 2.000.000 ₺ kâr payı dağıtılmasını önermiş ve genel kurul Mart sonunda "
    f"toplanacaktır.\n\n{DOGRU}",
    "31 Aralık itibarıyla yükümlülük kaydedilmez, dipnotta açıklanır.",
    ["31 Aralık itibarıyla kâr payı borcu olarak kaydedilir.",
     "Kâr payı 31 Aralık itibarıyla gider yazılır.",
     "Kâr payı geçmiş yıl kârından 31 Aralık itibarıyla düşülür.",
     "Kâr payı önerisi finansal tabloları etkilemez, açıklama yapılmaz."],
    "Raporlama döneminden sonra önerilen veya ilan edilen kâr payları dönem sonunda mevcut bir yükümlülük olmadığından "
    "yükümlülük olarak kaydedilmez; TMS 1 uyarınca dipnotlarda açıklanır.")

# ------------------------------------------------------------------ TMS 8
P.q("TMS 8 md. 32-38",
    "İşletme geçmiş yıllarda ticari alacaklarının %2’si oranında şüpheli alacak karşılığı ayırmaktaydı. Bu yıl "
    "müşterilerin ödeme performansındaki kötüleşme nedeniyle oran %4’e yükseltilmiş ve bu değişiklik karşılık giderini "
    f"160.000 ₺ artırmıştır.\n\n{DOGRU}",
    "Tahmin değişikliğidir; etkisi ileriye yönelik yansıtılır.",
    ["Politika değişikliğidir; geçmiş yıllar yeniden düzenlenir.",
     "Hata düzeltmesidir; geçmiş yıl kârları düzeltilir.",
     "Tahmin değişikliğidir; geçmiş yıllar yeniden düzenlenir.",
     "Değişiklik yapılamaz, önceki oran korunmalıdır."],
    "Yeni bilgi veya gelişmelerden kaynaklanan tahmin revizyonu muhasebe tahmininde değişikliktir; etkisi değişikliğin "
    "yapıldığı dönem ve etkilenen gelecek dönemlerde kâr veya zarara yansıtılır.")

P.q("TMS 8 md. 19-22",
    "İşletme stok maliyet formülünü FIFO’dan ağırlıklı ortalamaya değiştirmiştir; değişiklik daha güvenilir ve ihtiyaca "
    "uygun bilgi sağlamaktadır. Önceki dönemler için yeni formülün etkisini belirlemek mümkündür ve etki önemlidir."
    f"\n\n{DOGRU}",
    "Politika değişikliğidir; geriye dönük uygulanır.",
    ["Tahmin değişikliğidir; ileriye yönelik uygulanır.",
     "Politika değişikliğidir; ileriye yönelik uygulanır.",
     "Hata düzeltmesidir; sadece cari dönem düzeltilir.",
     "Değişiklik yapılamaz; tutarlılık kavramı engeller."],
    "Stok maliyet formülünün değiştirilmesi muhasebe politikası değişikliğidir; uygulanabilir olduğu ölçüde geriye dönük "
    "uygulanır, karşılaştırmalı tutarlar ve en erken dönemin açılış özkaynağı düzeltilir.", zorluk="hard")

P.q("TMS 8 md. 42",
    "İşletme 2026 yılında, 2025 yılında aktifleştirilen bir makine için hiç amortisman ayrılmadığını ve bu nedenle 2025 "
    "kârının 80.000 ₺ fazla gösterildiğini fark etmiştir. Hata önemlidir ve 2025 tabloları yayımlanmıştır.\n\n"
    f"{DOGRU}",
    "Karşılaştırmalı tutarlar yeniden düzenlenerek geriye dönük düzeltilir.",
    ["80.000 ₺ 2026 yılının amortisman gideri olarak kaydedilir.",
     "Hata tahmin değişikliği olarak ileriye yönelik düzeltilir.",
     "2025 tabloları yayımlandığı için hata düzeltilmez.",
     "Hata sadece dipnotta açıklanır, tutarlar değişmez."],
    "Önemli önceki dönem hataları, keşfedildikleri dönemden sonra yayımlanan ilk finansal tablolarda karşılaştırmalı "
    "tutarlar yeniden düzenlenerek geriye dönük düzeltilir; cari dönem kârına yansıtılmaz.")

# ------------------------------------------------------------------ TMS 21
P.q("TMS 21 md. 16, 23",
    "İşletmenin yıl sonunda iki dövizli kalemi vardır: işlem tarihinde 40 ₺ kurla alınan 10.000 ABD doları tutarındaki "
    "bir makine ve 40 ₺ kurla kaydedilen 10.000 ABD doları tutarındaki bir ticari alacak. Yıl sonu kuru 42 ₺’dir; makine "
    "maliyet modeliyle izlenmektedir.\n\nYıl sonu çevrimi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Alacak 42 ₺’den çevrilir, makine 40 ₺’de kalır.",
    ["Makine ve alacak 42 ₺’den çevrilir.",
     "Makine 42 ₺’den çevrilir, alacak 40 ₺’de kalır.",
     "Makine ve alacak işlem kurunda bırakılır.",
     "Makine ve alacak ortalama kurla çevrilir."],
    "Parasal kalemler (ticari alacak) kapanış kuruyla çevrilir ve fark kâr veya zarara yansır. Tarihi maliyetle ölçülen "
    "parasal olmayan kalemler (makine) işlem tarihindeki kurla bırakılır.", zorluk="hard")

P.q("TMS 21 md. 21-22",
    "İşletme 5 Kasım’da Almanya’daki bir tedarikçiden 20.000 avro tutarında vadeli ticari mal satın almıştır. Mallar "
    "ambara girmiş, avronun işlem tarihindeki kuru 45 ₺, kasım ortalaması 45,50 ₺, yıl sonu kuru ise 47 ₺’dir.\n\n"
    "Malların ilk kayıt tutarı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Mallar 900.000 ₺ ile kaydedilir.",
    ["Mallar kasım ortalama kuruyla 910.000 ₺ ile kaydedilir.",
     "Mallar yıl sonu kuruyla 940.000 ₺ ile kaydedilir.",
     "Mallar işlem ve yıl sonu kurlarının ortalamasıyla 920.000 ₺ ile kaydedilir.",
     "Mallar yıl sonunda 940.000 ₺’ye yükseltilir, fark kâra yansır."],
    "Yabancı para işlemleri işlem tarihindeki spot kurla kaydedilir: 20.000 × 45 = 900.000 ₺. Stok parasal olmayan kalem "
    "olduğundan yıl sonunda yeniden çevrilmez; borç ise parasal olduğundan 47 ₺’den değerlenir.")

# ------------------------------------------------------------------ TFRS 5
dd5, gud5 = 600_000, 540_000
P.q("TFRS 5 md. 15, 25",
    f"İşletme bir ay içinde satılması yüksek olasılıklı olan bir üretim tesisini satış amaçlı elde tutulan duran varlık "
    f"olarak sınıflandırmıştır. Tesisin defter değeri {tl(dd5)} ₺, gerçeğe uygun değerinden satış maliyetleri düşülmüş "
    f"tutarı {tl(gud5)} ₺’dir.\n\nTFRS 5 Satış Amaçlı Elde Tutulan Duran Varlıklar ve Durdurulan Faaliyetler’e göre "
    "aşağıdakilerden hangisi doğrudur?",
    f"Tesis {tl(gud5)} ₺’den ölçülür, {tl(dd5 - gud5)} ₺ zarar yazılır, amortisman durur.",
    [f"Tesis {tl(dd5)} ₺’den ölçülür, amortismana devam edilir.",
     f"Tesis {tl(gud5)} ₺’den ölçülür, fark özkaynaktan düşülür, amortisman sürer.",
     f"Tesis {tl(dd5)} ₺’den ölçülür, {tl(dd5 - gud5)} ₺ dipnotta açıklanır.",
     f"Tesis {tl(gud5 + 60_000)} ₺’den ölçülür, fark gelir yazılır."],
    "Satış amaçlı elde tutulan duran varlık, defter değeri ile gerçeğe uygun değerden satış maliyetleri düşülmüş tutardan "
    "düşük olanıyla ölçülür; fark değer düşüklüğü zararıdır ve bu varlık için amortisman ayrılmaz.", zorluk="hard")

P.q("TFRS 5 md. 6-8",
    "İşletme yönetimi eski merkez binasını satmaya karar vermiş ancak henüz alıcı aramaya başlamamış, bina için bir satış "
    "fiyatı belirlememiş ve binanın taşınma tamamlanana kadar 18 ay daha kullanılacağını öngörmüştür.\n\n"
    f"{DOGRU}",
    "Satış amaçlı sınıflama koşulları henüz sağlanmamıştır.",
    ["Satış kararıyla bina satış amaçlı elde tutulan varlığa aktarılır.",
     "Bina stok olarak yeniden sınıflandırılır.",
     "Bina gerçeğe uygun değerle yatırım amaçlı gayrimenkule aktarılır.",
     "Bina için amortisman satış kararı tarihinde durdurulur."],
    "Satış amaçlı sınıflama için varlığın mevcut durumuyla hemen satılabilir olması, satışın yüksek olasılıklı olması "
    "(aktif alıcı arayışı, makul fiyat, genellikle bir yıl içinde satış) gerekir; bu koşullar sağlanmamıştır.")

# ------------------------------------------------------------------ TMS 41 / TMS 7 / TMS 1 / TFRS 9
bas, gud41, sm41 = 200, 30_000, 1_000
P.q("TMS 41 md. 12, 26",
    f"Süt üretimi yapan işletmenin yıl sonunda {bas} baş ineği vardır. Bir ineğin aktif piyasadaki gerçeğe uygun değeri "
    f"{tl(gud41)} ₺, satış için katlanılacak nakliye ve komisyon maliyeti baş başına {tl(sm41)} ₺’dir. Yıl başındaki "
    "toplam değer 5.500.000 ₺ olup yıl içinde alım satım yapılmamıştır.\n\nTMS 41 Tarımsal Faaliyetler’e göre "
    "aşağıdakilerden hangisi doğrudur?",
    f"İnekler {tl(bas * (gud41 - sm41))} ₺ ile ölçülür, {tl(bas * (gud41 - sm41) - 5_500_000)} ₺ kazanç kâra yansır.",
    [f"İnekler {tl(bas * gud41)} ₺ ile ölçülür, {tl(bas * gud41 - 5_500_000)} ₺ kazanç kâra yansır.",
     f"İnekler {tl(bas * (gud41 - sm41))} ₺ ile ölçülür, {tl(bas * (gud41 - sm41) - 5_500_000)} ₺ özkaynağa alınır.",
     "İnekler maliyetle izlenir, amortisman ayrılır, değer değişimi kaydedilmez.",
     f"İnekler {tl(5_500_000)} ₺’de bırakılır, değer artışı satışta kaydedilir."],
    f"Canlı varlıklar gerçeğe uygun değerden satış maliyetleri düşülerek ölçülür: {bas} × ({tl(gud41)} − {tl(sm41)}) = "
    f"{tl(bas * (gud41 - sm41))} ₺. Değişim ({tl(bas * (gud41 - sm41) - 5_500_000)} ₺) oluştuğu dönemde kâr veya zarara "
    "yansıtılır.", zorluk="hard")

P.q("TMS 7 md. 16",
    "İşletmenin yıl içindeki nakit hareketleri şunlardır: müşterilerden tahsilat, tedarikçilere ödeme, yeni bir üretim "
    "makinesi için 750.000 ₺ ödeme, banka kredisi kullanımı ve ortaklara kâr payı ödemesi.\n\nMakine alımı için yapılan "
    "ödeme nakit akış tablosunda hangi bölümde gösterilir?",
    "Yatırım faaliyetlerinden nakit akışları",
    ["İşletme faaliyetlerinden nakit akışları",
     "Finansman faaliyetlerinden nakit akışları",
     "Nakit ve nakit benzerlerindeki kur farkı",
     "Olağandışı faaliyetlerden nakit akışları"],
    "Maddi duran varlık edinimi için yapılan ödemeler yatırım faaliyetlerinden nakit çıkışıdır; müşteri tahsilatları ve "
    "tedarikçi ödemeleri işletme, kredi ve kâr payı hareketleri finansman faaliyetlerindedir.", zorluk="easy")

P.q("TMS 1 md. 10",
    "Halka açık bir şirketin finans ekibi yıl sonu raporlama paketini hazırlamaktadır. Paket finansal durum tablosu, kâr "
    "veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim tablosu, nakit akış tablosu, dipnotlar ve yönetim "
    "kurulu faaliyet raporundan oluşmaktadır.\n\nBu belgelerden hangisi tam bir finansal tablo setinin parçası değildir?",
    "Yönetim kurulu faaliyet raporu",
    ["Nakit akış tablosu", "Özkaynak değişim tablosu", "Finansal tablo dipnotları", "Finansal durum tablosu"],
    "Tam finansal tablo seti finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim "
    "tablosu, nakit akış tablosu ve dipnotlardan (karşılaştırmalı bilgiyle) oluşur; faaliyet raporu bu setin dışındadır.",
    zorluk="easy")

P.q("TFRS 9 md. 4.1.2",
    "Bir şirket vadeye kadar elde tutup kupon ve anapara tahsil etmek amacıyla özel sektör tahvilleri satın almıştır. "
    "Tahvillerin sözleşmeye bağlı nakit akışları sadece anapara ve anapara bakiyesine ilişkin faiz ödemelerinden "
    f"oluşmaktadır.\n\n{DOGRU}",
    "Tahviller itfa edilmiş maliyetinden ölçülür.",
    ["Tahviller gerçeğe uygun değer farkı kâr veya zarara yansıtılarak ölçülür.",
     "Tahviller gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak ölçülür.",
     "Tahviller nominal değerle ölçülür, faiz tahsil edildikçe gelir yazılır.",
     "Tahviller stok olarak sınıflandırılır."],
    "İş modeli sözleşmeye bağlı nakit akışlarını tahsil etmek olan ve nakit akışları sadece anapara ve faiz "
    "ödemelerinden oluşan finansal varlıklar itfa edilmiş maliyetinden ölçülür; faiz geliri etkin faiz yöntemiyle kaydedilir.")

# ------------------------------------------------------------------ ek: TMS 16 kayıttan çıkarma / TMS 36 yevmiye
mal16, bir16, sat16 = 500_000, 320_000, 210_000
P.q("TMS 16 md. 67-72; THP 679",
    f"İşletme maliyeti {tl(mal16)} ₺, birikmiş amortismanı {tl(bir16)} ₺ olan bir makineyi {tl(sat16)} ₺ + %20 KDV bedelle "
    "vadeli satmıştır. Makine için daha önce değer düşüklüğü kaydedilmemiş ve yeniden değerleme yapılmamıştır.\n\n"
    "Bu satışa ilişkin günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(120, sat16 * 12 // 10), (257, bir16)], [(253, mal16), (391, sat16 // 5), (679, sat16 - (mal16 - bir16))]),
    [K([(120, sat16 * 12 // 10), (257, bir16)], [(253, mal16), (391, sat16 // 5), (600, sat16 - (mal16 - bir16))]),
     K([(120, sat16 * 12 // 10)], [(253, sat16), (391, sat16 // 5)]),
     K([(120, sat16 * 12 // 10), (257, bir16)], [(253, mal16), (391, sat16 // 5), (522, sat16 - (mal16 - bir16))]),
     K([(120, sat16 * 12 // 10), (257, bir16)], [(253, mal16), (191, sat16 // 5), (679, sat16 - (mal16 - bir16))])],
    f"Kayıttan çıkarma kazancı = satış bedeli − net defter değeri = {tl(sat16)} − {tl(mal16 - bir16)} = "
    f"{tl(sat16 - (mal16 - bir16))} ₺; hasılat değil kazançtır ve THP’de 679 hesabına alacak yazılır.", zorluk="hard")

P.q("TMS 38 md. 97-98; THP 268",
    "İşletme 3 yıl önce 900.000 ₺’ye aldığı ve 5 yıllık yararlı ömürle doğrusal itfa ettiği bir patentin kalan yararlı "
    "ömrünü, pazar koşulları nedeniyle bu yıl başında 1 yıl olarak revize etmiştir. Kalıntı değer yoktur ve patent "
    "üretimde kullanılmaktadır.\n\nBu yıl ayrılacak itfa payına ilişkin kayıt için aşağıdakilerden hangisi doğrudur?",
    T(268, "alacak", 360_000),
    [T(268, "alacak", 180_000), T(268, "alacak", 900_000), T(260, "alacak", 360_000), T(263, "alacak", 360_000)],
    "Üç yılda 900.000 × 3/5 = 540.000 ₺ itfa edilmiş, kalan 360.000 ₺’dir. Yararlı ömür revizyonu ileriye dönük "
    "uygulanır; kalan tutarın tamamı bu yıl itfa edilir ve 268 Birikmiş Amortismanlar hesabına alacak yazılır.",
    zorluk="hard")

# ek — TFRS 15 zaman içinde: tamamlanma oranı
sb, tm, kt = 10_000_000, 8_000_000, 2_000_000
P.q("TFRS 15 md. 35, 39-45",
    f"İnşaat şirketi müşterinin arsası üzerinde, müşterinin kontrolündeki bir binayı {tl(sb)} ₺ sabit bedelle inşa "
    f"etmektedir. Toplam maliyetin {tl(tm)} ₺ olacağı tahmin edilmekte, ilk yıl {tl(kt)} ₺ maliyete katlanılmıştır. "
    "Şirket ilerlemeyi katlanılan maliyetler yöntemiyle ölçmektedir.\n\nİlk yıl kaydedilecek hasılat ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    f"Tamamlanma %25; {tl(sb * kt // tm)} ₺ hasılat kaydedilir.",
    [f"Bina teslim edilene kadar hasılat kaydedilmez.",
     f"Tamamlanma %25; {tl(kt)} ₺ hasılat kaydedilir.",
     f"Tamamlanma %20; {tl(sb * 20 // 100)} ₺ hasılat kaydedilir.",
     f"Tamamlanma %25; {tl(sb * kt // tm - kt)} ₺ hasılat kaydedilir."],
    f"Müşteri inşa edilen varlığı kontrol ettiğinden edim yükümlülüğü zaman içinde yerine getirilir. İlerleme = "
    f"{tl(kt)} / {tl(tm)} = %25; hasılat {tl(sb)} × %25 = {tl(sb * kt // tm)} ₺.", zorluk="hard")

# ek — TMS 37 yeniden yapılanma karşılığı
P.q("TMS 37 md. 70-83",
    "Yönetim kurulu yıl sonundan önce bir fabrikanın kapatılmasına karar vermiş; ancak yıl sonu itibarıyla ayrıntılı "
    "resmî bir plan hazırlanmamış, çalışanlara ve müşterilere herhangi bir duyuru yapılmamış ve uygulamaya "
    "başlanmamıştır. Kapatma maliyetinin 2.400.000 ₺ olacağı tahmin edilmektedir.\n\n"
    f"{DOGRU}",
    "Yeniden yapılanma karşılığı ayrılmaz.",
    ["2.400.000 ₺ yeniden yapılanma karşılığı ayrılır.",
     "Karşılığın yarısı ayrılır, kalanı dipnotta açıklanır.",
     "Tutar özkaynaklarda yedek olarak ayrılır.",
     "Karar tarihinde 2.400.000 ₺ gider tahakkuk ettirilir."],
    "Yeniden yapılanma için zımni yükümlülük; ayrıntılı resmî plan hazırlanmış olmasını ve uygulamaya başlanması ya da "
    "ana unsurlarının etkilenenlere duyurulmasıyla geçerli bir beklenti yaratılmasını gerektirir. Sadece yönetim kararı "
    "yükümlülük doğurmaz.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
