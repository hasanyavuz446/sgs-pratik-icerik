# -*- coding: utf-8 -*-
"""Finansal Muhasebe · Dönem Sonu İşlemleri — 60 soru, 2026 test biçimi.

Gerçek kitapçıklarda dönem sonu soruları tutar veren bir olayla gelir: amortisman (özel fon dâhil),
reeskont, şüpheli alacak karşılığı, gider/gelir tahakkuku, gelecek dönem hesapları, kur değerlemesi,
KDV mahsubu, vergi karşılığı ve kapanış kayıtları sorulur; şıklar yevmiye kaydı ya da hesap-taraf-tutardır.

Dayanak: MSUGT Tekdüzen Hesap Planı (18/28, 38/48 grupları, 122/322, 129, 190/191/391, 370/371,
590/591, 690-692, 7/A yansıtma hesapları); VUK md. 281 (reeskont, iç iskonto), 313-315 ve 320
(amortisman), 322-323 (değersiz ve şüpheli alacak), 327 (özel maliyetler), 328 (yenileme fonu).
Oran ve tutarlar soruda verilir; bütün hesaplar builder içinde yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K, taraf as T, hk

P = Paket("questions_topic_finansal_donem_sonu_2026.json", lesson="finansal_muhasebe",
          topic="donem_sonu_islemleri", konu_adi="Dönem Sonu İşlemleri", seed=2026093063,
          surum="MSUGT Tekdüzen Hesap Planı; VUK md. 281, 313-328; 29.09.2026 kontrolü")

R = "MSUGT Tekdüzen Hesap Planı"
KAYIT = "Bu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?"
DS = "Dönem sonunda yapılacak düzeltme kaydı aşağıdakilerden hangisidir?"
DOGRU = "Bu işleme ilişkin kayıt için aşağıdakilerden hangisi doğrudur?"


def reeskont(nominal, gun, oran):
    """VUK md. 281 uygulamasında iç iskonto: N × n × r / (36.000 + n × r)."""
    v = nominal * gun * oran / (36_000 + gun * oran)
    assert v == int(v), v
    return int(v)


# 1 — bina amortismanının 7/A dağıtımı
amo = 1_200_000 // 50
u, y, s_ = amo * 60 // 100, amo * 25 // 100, amo * 15 // 100
assert u + y + s_ == amo
P.q(f"{R}: 257, 7/A",
    "7/A seçeneğini uygulayan üretim işletmesinin 1.200.000 ₺ maliyetli ve 50 yıl faydalı ömürlü binasının %60’ı "
    "üretim, %25’i yönetim, %15’i satış bölümü olarak kullanılmaktadır. İşletme normal (eşit tutarlı) amortisman "
    f"yöntemini uygulamaktadır.\n\n{DS}",
    K([(730, u), (770, y), (760, s_)], [(257, amo)]),
    [K([(770, amo)], [(257, amo)]),
     K([(730, u), (770, y), (760, s_)], [(252, amo)]),
     K([(151, u), (770, y), (760, s_)], [(257, amo)]),
     K([(257, amo)], [(730, u), (770, y), (760, s_)])],
    f"Yıllık amortisman 1.200.000 / 50 = {tl(amo)} ₺’dir. Kullanım oranlarına göre üretime düşen {tl(u)} ₺ 730, yönetime "
    f"düşen {tl(y)} ₺ 770, satışa düşen {tl(s_)} ₺ 760 hesabına borç, toplam 257 Birikmiş Amortismanlar hesabına alacak yazılır.",
    zorluk="hard")

# 2 — azalan bakiyeler 2. yıl
P.q("VUK md. 315; THP 257",
    "Vergi Usul Kanunu’na göre azalan bakiyeler yöntemini seçen işletme, 500.000 ₺’ye aldığı ve faydalı ömrü 5 yıl olarak "
    "belirlenen makinesi için ilk yıl 200.000 ₺ amortisman ayırmıştır. Makine üretimde kullanılmakta olup işletme yöntemi "
    "değiştirmemiştir.\n\nİkinci yılın sonunda yapılacak amortisman kaydı için aşağıdakilerden hangisi doğrudur?",
    T(257, "alacak", 120_000),
    [T(257, "alacak", 100_000), T(257, "alacak", 200_000), T(257, "alacak", 60_000), T(253, "alacak", 120_000)],
    "Azalan bakiyeler oranı normal oranın iki katıdır: %20 × 2 = %40. İkinci yıl amortismanı kalan değer üzerinden "
    "hesaplanır: (500.000 − 200.000) × %40 = 120.000 ₺ ve 257 hesabına alacak yazılır.", zorluk="hard")

# 3 — satış taşıtı amortismanı
P.q(f"{R}: 760, 257",
    "Dağıtım işinde kullanılan ve 450.000 ₺ maliyetle aktifleştirilen kamyonun faydalı ömrü 5 yıldır. İşletme normal "
    "amortisman yöntemini uygulamakta, amortisman giderlerini fonksiyonlarına göre ilgili 7/A hesaplarında izlemektedir. "
    f"Kamyon yıl başında hizmete girmiştir.\n\n{DS}",
    K([(760, 90_000)], [(257, 90_000)]),
    [K([(770, 90_000)], [(257, 90_000)]),
     K([(760, 90_000)], [(254, 90_000)]),
     K([(257, 90_000)], [(760, 90_000)]),
     K([(760, 90_000)], [(268, 90_000)])],
    "Yıllık amortisman 450.000 / 5 = 90.000 ₺’dir. Dağıtımda kullanılan taşıtın amortismanı 760 Pazarlama, Satış ve "
    "Dağıtım Giderleri hesabına borç, 257 Birikmiş Amortismanlar hesabına alacak yazılır; 268 maddi olmayan varlıklar içindir.",
    zorluk="easy")

# 4 — hakların itfası
P.q(f"{R}: 260, 268",
    "İşletme muhasebe bölümünde kullanmak üzere 150.000 ₺ bedelle üç yıl süreli bir yazılım kullanım lisansı satın almış "
    "ve 260 Haklar hesabına kaydetmiştir. Lisans yıl başında kullanılmaya başlanmış, eşit tutarlarla itfa "
    f"edilecektir.\n\n{DS}",
    K([(770, 50_000)], [(268, 50_000)]),
    [K([(770, 50_000)], [(257, 50_000)]),
     K([(770, 50_000)], [(260, 50_000)]),
     K([(263, 50_000)], [(268, 50_000)]),
     K([(770, 150_000)], [(260, 150_000)])],
    "Maddi olmayan duran varlıkların itfa payları 268 Birikmiş Amortismanlar hesabında toplanır. Yıllık pay 150.000 / 3 = "
    "50.000 ₺ olup idari kullanım nedeniyle 770 Genel Yönetim Giderleri hesabına borç yazılır.")

# 5 — özel maliyetler
P.q("VUK md. 327; THP 264, 268",
    "İşletme dört yıllığına kiraladığı dükkânı mağaza olarak kullanmak için 240.000 ₺ tadilat harcaması yapmış ve bu "
    "tutarı 264 Özel Maliyetler hesabına almıştır. Kira sözleşmesi yıl başında başlamış olup harcama kira süresi boyunca "
    f"eşit tutarlarla itfa edilecektir.\n\n{DOGRU}",
    T(760, "borç", 60_000),
    [T(770, "borç", 240_000), T(264, "alacak", 60_000), T(760, "borç", 48_000), T(257, "alacak", 60_000)],
    "Özel maliyet bedelleri kira süresine göre itfa edilir: 240.000 / 4 = 60.000 ₺. Satış mağazası olduğundan 760 hesabına "
    "borç, 268 Birikmiş Amortismanlar hesabına alacak yazılır.")

# 6 — amortismana tabi olmayan varlık (olumsuz)
P.q(f"{R}: 250-258",
    "Yıl sonunda amortisman hesaplayan işletmenin duran varlıkları arasında fabrika binası (2.400.000 ₺), fabrikanın "
    "üzerinde bulunduğu arsa (1.800.000 ₺), üretim makineleri (900.000 ₺), dağıtım kamyonu (450.000 ₺) ve büro "
    "mobilyaları (120.000 ₺) bulunmaktadır.\n\nBu varlıklardan hangisi için amortisman ayrılmaz?",
    "Fabrikanın üzerinde bulunduğu arsa",
    ["Fabrika binası", "Üretim makineleri", "Dağıtım kamyonu", "Büro mobilyaları"],
    "Arazi ve arsaların sınırsız ömürlü olduğu kabul edilir, amortismana tabi tutulmaz; bina, makine, taşıt ve demirbaşlar "
    "faydalı ömürleri boyunca amortismana tabidir.", zorluk="easy")

# 7 — yapılmakta olan yatırım
P.q(f"{R}: 258",
    "İşletmenin yıl içinde başladığı ve yıl sonu itibarıyla %70’i tamamlanan depo inşaatı için 1.400.000 ₺ harcama "
    "yapılmış ve 258 Yapılmakta Olan Yatırımlar hesabında izlenmiştir. İnşaatın gelecek yılın ikinci yarısında bitmesi "
    "beklenmektedir.\n\nBu tutarla ilgili yıl sonu işlemi için aşağıdakilerden hangisi doğrudur?",
    "Kullanıma hazır olmadığı için amortisman ayrılmaz.",
    ["Tamamlanma oranı kadar amortisman ayrılır.",
     "Harcamalar dönem gideri olarak kapatılır.",
     "Tutar 252 Binalar hesabına aktarılıp amortismana başlanır.",
     "Harcamaların yarısı için amortisman ayrılır."],
    "Amortisman varlık kullanıma hazır olduğunda başlar. 258’deki harcamalar inşaat tamamlanınca 252 Binalar hesabına "
    "aktarılır; o tarihe kadar amortisman ayrılmaz.")

# 8 — yenileme fonu
mal, bir, sat = 200_000, 120_000, 100_000
kdv, kar = sat // 5, sat - (mal - bir)
P.q("VUK md. 328; THP 549",
    f"İşletme yenilemek amacıyla sattığı dağıtım kamyonunun satış kazancını, yeni kamyon alımında kullanmak üzere "
    f"yenileme fonuna almaya karar vermiştir. Kamyonun maliyeti {tl(mal)} ₺, birikmiş amortismanı {tl(bir)} ₺ olup "
    f"{tl(sat)} ₺ + %20 KDV bedelle banka aracılığıyla satılmıştır.\n\n{KAYIT}",
    K([(102, sat + kdv), (257, bir)], [(254, mal), (391, kdv), (549, kar)]),
    [K([(102, sat + kdv), (257, bir)], [(254, mal), (391, kdv), (679, kar)]),
     K([(102, sat + kdv), (257, bir)], [(254, mal), (391, kdv), (542, kar)]),
     K([(102, sat + kdv)], [(254, sat), (391, kdv)]),
     K([(102, sat + kdv), (257, bir)], [(254, mal), (191, kdv), (549, kar)])],
    f"Net değer {tl(mal - bir)} ₺, satış bedeli {tl(sat)} ₺ olduğundan kazanç {tl(kar)} ₺’dir. Yenileme amacı nedeniyle "
    "kazanç gelir tablosuna değil 549 Özel Fonlar hesabına alacak yazılır; yeni varlığın amortismanıyla itfa edilir.",
    zorluk="hard")

# 9 — alacak senedi reeskontu
rs = reeskont(110_000, 90, 40)
P.q("VUK md. 281; THP 122, 657",
    "Yıl sonunda işletmenin portföyünde 110.000 ₺ nominal değerli ve vadesine 90 gün kalan bir alacak senedi "
    "bulunmaktadır. İşletme senetli alacaklarını reeskonta tabi tutmakta ve iç iskonto yöntemini kullanmaktadır; "
    f"uygulanacak yıllık faiz oranı %40’tır.\n\n{DS}",
    K([(657, rs)], [(122, rs)]),
    [K([(122, rs)], [(647, rs)]),
     K([(657, 11_000)], [(122, 11_000)]),
     K([(780, rs)], [(121, rs)]),
     K([(657, rs)], [(322, rs)])],
    f"İç iskonto: 110.000 × 90 × 40 / (36.000 + 90 × 40) = {tl(rs)} ₺. Alacak senedinin bugünkü değere indirilmesi gider "
    "doğurur: 657 Reeskont Faiz Giderleri borç, 122 Alacak Senetleri Reeskontu alacak. Dış iskonto 11.000 ₺ verirdi.",
    zorluk="hard")

# 10 — borç senedi reeskontu
rs2 = reeskont(55_000, 45, 80)
P.q("VUK md. 285; THP 322, 647",
    "Yıl sonunda işletmenin satıcısına verdiği 55.000 ₺ nominal değerli ve vadesine 45 gün kalan bir borç senedi "
    "bulunmaktadır. İşletme borç senetlerini de reeskonta tabi tutmaktadır; iç iskonto yöntemi ve yıllık %80 faiz oranı "
    f"uygulanacaktır.\n\n{DS}",
    K([(322, rs2)], [(647, rs2)]),
    [K([(647, rs2)], [(322, rs2)]),
     K([(657, rs2)], [(322, rs2)]),
     K([(322, 5_500)], [(647, 5_500)]),
     K([(321, rs2)], [(642, rs2)])],
    f"İç iskonto: 55.000 × 45 × 80 / (36.000 + 45 × 80) = {tl(rs2)} ₺. Borcun bugünkü değere indirilmesi gelir doğurur: "
    "322 Borç Senetleri Reeskontu borç, 647 Reeskont Faiz Gelirleri alacak.", zorluk="hard")

# 11 — reeskontun yeni dönemde iptali
P.q(f"{R}: 122, 647",
    f"Önceki yıl sonunda portföydeki alacak senetleri için {tl(rs)} ₺ reeskont ayrılmış, 657 hesabı dönem sonunda "
    "kapatılmıştır. İşletme yeni yılın ilk iş günü reeskont kaydını ters kayıtla iptal etme politikasını "
    f"uygulamaktadır.\n\n{DOGRU}",
    T(647, "alacak", rs),
    [T(657, "alacak", rs), T(122, "alacak", rs), T(121, "borç", rs), T(642, "alacak", rs)],
    f"Yeni dönemde reeskont iptal edilince 122 Alacak Senetleri Reeskontu {tl(rs)} ₺ borçlandırılır; karşılığında 657 "
    "önceki yıl kapatıldığından yeni yılın geliri olarak 647 Reeskont Faiz Gelirleri alacaklandırılır.", zorluk="hard")

# 12 — şüpheli alacak karşılığı, teminatlı kısım
P.q("VUK md. 323; THP 129, 654",
    "Yıl sonunda işletmenin 128 Şüpheli Ticari Alacaklar hesabında, hakkında dava açılmış tek bir müşteriden 80.000 ₺ "
    "alacağı bulunmaktadır. Bu alacağın 20.000 ₺’lik kısmı için müşteriden banka teminat mektubu alınmıştır; alacak için "
    f"daha önce karşılık ayrılmamıştır.\n\n{DOGRU}",
    T(654, "borç", 60_000),
    [T(654, "alacak", 60_000), T(129, "borç", 60_000), T(689, "borç", 60_000), T(128, "alacak", 60_000)],
    "Şüpheli alacak karşılığı alacağın teminatsız kısmı için ayrılır: 80.000 − 20.000 = 60.000 ₺. 654 Karşılık Giderleri "
    "borç, 129 Şüpheli Ticari Alacaklar Karşılığı alacak yazılır.")

# 13 — değersiz alacak
P.q("VUK md. 322; THP 689",
    "İşletmenin karşılık ayırmadığı 15.000 ₺’lik bir ticari alacağı hakkında yürütülen icra takibi borçlunun hiçbir "
    "malvarlığı bulunmadığı gerekçesiyle aciz vesikasıyla sonuçlanmış ve alacağın tahsil imkânı kalmamıştır. Alacak 128 "
    f"hesabında izlenmektedir.\n\n{KAYIT}",
    K([(689, 15_000)], [(128, 15_000)]),
    [K([(654, 15_000)], [(129, 15_000)]),
     K([(129, 15_000)], [(128, 15_000)]),
     K([(689, 15_000)], [(120, 15_000)]),
     K([(659, 15_000)], [(129, 15_000)])],
    "Kaza kararı veya aciz vesikasıyla tahsili imkânsızlaşan alacak değersiz alacaktır ve kayıtlı değeriyle gider yazılır. "
    "Karşılık ayrılmadığı için 689 Diğer Olağandışı Gider ve Zararlar borç, 128 alacak yazılır.")

# 14 — menkul kıymet değer düşüklüğü
P.q(f"{R}: 119, 654",
    "Alım satım amacıyla elde tutulan hisse senetlerinin toplam maliyeti 80.000 ₺’dir. Yıl sonunda borsada oluşan değer "
    "65.000 ₺ olup işletme değer düşüklüğünü karşılık yoluyla kayda almaktadır; senetler yeni yılda satılmak üzere elde "
    f"tutulmaya devam edecektir.\n\n{DS}",
    K([(654, 15_000)], [(119, 15_000)]),
    [K([(655, 15_000)], [(110, 15_000)]),
     K([(654, 15_000)], [(110, 15_000)]),
     K([(119, 15_000)], [(644, 15_000)]),
     K([(654, 15_000)], [(129, 15_000)])],
    "Değer düşüklüğü 80.000 − 65.000 = 15.000 ₺’dir. Senetler satılmadığı için satış zararı yazılmaz; 654 Karşılık "
    "Giderleri borç, 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı alacak ile kaydedilir.")

# 15 — 180 → gider
P.q(f"{R}: 180, 770",
    "İşletme 1 Eylül’de idari binasının bir yıllık yangın sigortası için 36.000 ₺ ödemiş ve tutarın tamamını 180 Gelecek "
    "Aylara Ait Giderler hesabına kaydetmiştir. İşletme giderleri ay sonları yerine yalnız dönem sonunda "
    f"aktarmaktadır.\n\n{DS}",
    K([(770, 12_000)], [(180, 12_000)]),
    [K([(770, 24_000)], [(180, 24_000)]),
     K([(180, 12_000)], [(770, 12_000)]),
     K([(770, 12_000)], [(280, 12_000)]),
     K([(770, 12_000)], [(381, 12_000)])],
    "Eylül-aralık dört aylık sigorta payı 36.000 × 4/12 = 12.000 ₺ cari yılın gideridir: 770 borç, 180 alacak. Kalan "
    "24.000 ₺ gelecek yılın gideri olarak 180’de kalır.", zorluk="easy")

# 16 — 280 → 180
P.q(f"{R}: 180, 280",
    "İşletme 1 Ocak 2026’da üç yıllık depo kirası olarak 1.080.000 ₺ peşin ödemiş; ilk yılın payını 180, kalan iki yılın "
    "payını 280 Gelecek Yıllara Ait Giderler hesabına almıştır. 2026 yılına ait kira aylar itibarıyla gidere aktarılmış "
    "ve 180 hesabı yıl sonunda kapanmıştır.\n\n2026 yılı sonunda yapılacak sınıflandırma kaydı aşağıdakilerden hangisidir?",
    K([(180, 360_000)], [(280, 360_000)]),
    [K([(280, 360_000)], [(180, 360_000)]),
     K([(180, 720_000)], [(280, 720_000)]),
     K([(770, 360_000)], [(280, 360_000)]),
     K([(180, 360_000)], [(380, 360_000)])],
    "Yıl sonunda 280’de kalan 720.000 ₺’nin izleyen on iki aya ait kısmı (360.000 ₺) kısa vadeli hâle gelir ve 180 "
    "Gelecek Aylara Ait Giderler hesabına aktarılır: 180 borç, 280 alacak.")

# 17 — 380 → gelir
P.q(f"{R}: 380, 649",
    "İşletme 1 Kasım’da, esas faaliyeti dışında kiraya verdiği depo için altı aylık kira bedeli olan 60.000 ₺’yi peşin "
    "tahsil etmiş ve 380 Gelecek Aylara Ait Gelirler hesabına kaydetmiştir. Dönem içinde bu hesaptan gelir hesabına "
    f"aktarım yapılmamıştır.\n\nDönem sonu kaydı için aşağıdakilerden hangisi doğrudur?",
    T(649, "alacak", 20_000),
    [T(649, "alacak", 60_000), T(380, "alacak", 20_000), T(600, "alacak", 20_000), T(181, "borç", 20_000)],
    "Kasım ve aralık iki aylık kira 60.000 × 2/6 = 20.000 ₺ cari dönemin gelirdir: 380 borç, 649 Diğer Olağan Gelir ve "
    "Kârlar alacak. Kalan 40.000 ₺ gelecek yılın geliri olarak 380’de kalır.")

# 18 — kredi faizi tahakkuku
fz = 400_000 * 48 * 3 // (100 * 12)
P.q(f"{R}: 381, 780",
    "İşletme 1 Ekim’de 6 ay vadeli 400.000 ₺ banka kredisi kullanmıştır. Yıllık basit faiz oranı %48 olup faizin tamamı "
    "vade sonunda anaparayla birlikte ödenecektir. Kredi dönem içinde 300 Banka Kredileri hesabına kaydedilmiştir.\n\n"
    f"{DS}",
    K([(780, fz)], [(381, fz)]),
    [K([(780, fz * 2)], [(381, fz * 2)]),
     K([(780, fz)], [(300, fz)]),
     K([(181, fz)], [(642, fz)]),
     K([(780, fz)], [(180, fz)])],
    f"Ekim-aralık üç aylık faiz 400.000 × %48 × 3/12 = {tl(fz)} ₺ cari dönemin gideridir ve henüz ödenmemiştir: 780 "
    "Finansman Giderleri borç, 381 Gider Tahakkukları alacak.")

# 19 — mevduat faizi tahakkuku
fg = 500_000 * 36 * 1 // (100 * 12)
P.q(f"{R}: 181, 642",
    "İşletme 1 Aralık’ta 500.000 ₺’yi üç ay vadeli ve yıllık %36 basit faizli mevduata yatırmıştır. Faiz vade sonunda "
    "anaparayla birlikte tahsil edilecektir; tahakkuk kaydında gelir vergisi kesintisi dikkate alınmayacaktır.\n\n"
    f"{DS}",
    K([(181, fg)], [(642, fg)]),
    [K([(181, fg * 3)], [(642, fg * 3)]),
     K([(642, fg)], [(181, fg)]),
     K([(102, fg)], [(642, fg)]),
     K([(181, fg)], [(380, fg)])],
    f"Aralık ayına düşen faiz 500.000 × %36 × 1/12 = {tl(fg)} ₺’dir; tahsil edilmemiş olsa da cari dönemin gelirdir: 181 "
    "Gelir Tahakkukları borç, 642 Faiz Gelirleri alacak.")

# 20 — elektrik tahakkuku
P.q(f"{R}: 381, 770",
    "İşletmenin merkez ofisine ait aralık ayı elektrik faturası dağıtım şirketi tarafından ocak ayında düzenlenecektir. "
    "Sayaç okumalarına göre aralık tüketiminin bedeli KDV hariç 8.500 ₺ olarak tahmin edilmiş ve cari döneme "
    f"yansıtılmasına karar verilmiştir.\n\n{DOGRU}",
    T(381, "alacak", 8_500),
    [T(180, "borç", 8_500), T(320, "alacak", 8_500), T(191, "borç", 1_700), T(381, "borç", 8_500)],
    "Aralık tüketimi cari dönemin gideridir ancak fatura henüz gelmemiştir: 770 Genel Yönetim Giderleri borç, 381 Gider "
    "Tahakkukları alacak 8.500 ₺. KDV fatura geldiğinde indirilir.")

# 21 — dövizli alacak değerleme
usd, k1, k2 = 20_000, 40, 41.2
P.q(f"{R}: 120, 646",
    f"İşletmenin yıl sonunda yurt dışındaki bir müşteriden 20.000 ABD doları alacağı bulunmaktadır. Alacak işlem "
    f"tarihindeki {k1} ₺ kurla kaydedilmiştir; değerleme günü kuru {tl(k2)} ₺’dir. İşletme parasal kalemleri dönem sonu "
    f"kuruyla değerlemektedir.\n\n{DS}",
    K([(120, usd * (k2 - k1))], [(646, usd * (k2 - k1))]),
    [K([(120, usd * (k2 - k1))], [(649, usd * (k2 - k1))]),
     K([(120, usd * k2)], [(646, usd * k2)]),
     K([(120, usd * (k2 - k1))], [(679, usd * (k2 - k1))]),
     K([(120, usd * (k2 - k1))], [(601, usd * (k2 - k1))])],
    f"Alacak 20.000 × {tl(k2)} = {tl(usd * k2)} ₺ olmalıdır; kayıtlı değer {tl(usd * k1)} ₺. Aradaki "
    f"{tl(usd * (k2 - k1))} ₺ artış 120 borç, 646 Kambiyo Kârları alacak ile kaydedilir.")

# 22 — dövizli borç değerleme
P.q(f"{R}: 320, 656",
    "İşletmenin yıl sonunda Almanya’daki bir tedarikçiye 15.000 avro ticari borcu vardır. Borç işlem tarihindeki 45 ₺ "
    "kurla kaydedilmiş, değerleme günü kuru 46 ₺ olarak belirlenmiştir. Borç ocak ayında ödenecektir.\n\n"
    f"Dönem sonu değerleme kaydı için aşağıdakilerden hangisi doğrudur?",
    T(656, "borç", 15_000),
    [T(646, "alacak", 15_000), T(320, "borç", 15_000), T(780, "borç", 15_000), T(656, "borç", 690_000)],
    "Borç 15.000 × 46 = 690.000 ₺ olmalıdır; kayıtlı değer 675.000 ₺. Borçtaki 15.000 ₺ artış 656 Kambiyo Zararları "
    "borç, 320 Satıcılar alacak ile kaydedilir.")

# 23 — döviz kredisi, kur düşüşü
P.q(f"{R}: 300, 646",
    "İşletme yıl içinde 50.000 ABD doları tutarında bir yıl vadeli kredi kullanmış ve krediyi 40 ₺ kurla kaydetmiştir. "
    "Yıl sonunda ABD dolarının değerleme kuru 39 ₺’ye gerilemiştir; kredinin faizi ayrıca tahakkuk ettirilmiştir.\n\n"
    f"{DS}",
    K([(300, 50_000)], [(646, 50_000)]),
    [K([(656, 50_000)], [(300, 50_000)]),
     K([(300, 50_000)], [(642, 50_000)]),
     K([(400, 50_000)], [(646, 50_000)]),
     K([(300, 1_950_000)], [(646, 1_950_000)])],
    "Kredi 50.000 × 39 = 1.950.000 ₺’ye inmiştir; kayıtlı değer 2.000.000 ₺. Borçtaki 50.000 ₺ azalış 300 Banka "
    "Kredileri borç, 646 Kambiyo Kârları alacak ile kaydedilir.")

# 24 — döviz kasası
P.q(f"{R}: 100, 646",
    "İşletmenin kasasında yıl sonunda 3.000 avro bulunmaktadır. Bu dövizler kasaya girdiği tarihteki 44 ₺ kurla "
    "kaydedilmiştir. Değerleme günü kuru 46 ₺’dir ve dövizlerin ocak ayında bir satıcıya ödenmesi planlanmaktadır."
    f"\n\nDönem sonu değerleme kaydı için aşağıdakilerden hangisi doğrudur?",
    T(646, "alacak", 6_000),
    [T(646, "alacak", 138_000), T(100, "alacak", 6_000), T(656, "borç", 6_000), T(642, "alacak", 6_000)],
    "Kasadaki dövizler 3.000 × 46 = 138.000 ₺ olmalıdır; kayıtlı değer 132.000 ₺. 6.000 ₺ artış 100 Kasa borç, 646 "
    "Kambiyo Kârları alacak ile kaydedilir.", zorluk="easy")

# 25 — devreden KDV
P.q(f"{R}: 190, 191, 391",
    "Kasım ayı sonunda işletmenin 391 Hesaplanan KDV hesabının bakiyesi 60.000 ₺, 191 İndirilecek KDV hesabının bakiyesi "
    "85.000 ₺’dir. Önceki aydan devreden KDV yoktur ve iade hakkı doğuran bir işlem bulunmamaktadır.\n\n"
    "Ay sonu mahsup kaydı aşağıdakilerden hangisidir?",
    K([(391, 60_000), (190, 25_000)], [(191, 85_000)]),
    [K([(391, 60_000)], [(191, 60_000)]),
     K([(391, 60_000), (360, 25_000)], [(191, 85_000)]),
     K([(191, 85_000)], [(391, 60_000), (190, 25_000)]),
     K([(391, 60_000), (193, 25_000)], [(191, 85_000)])],
    "İndirilecek KDV hesaplanandan 25.000 ₺ fazladır. 391 ve 191 kapatılır; indirilemeyen fark sonraki aya aktarılmak "
    "üzere 190 Devreden KDV hesabına borç yazılır. Ödenecek KDV doğmaz.")

# 26 — devreden KDV’nin kullanımı
P.q(f"{R}: 190, 191, 360, 391",
    "Kasım ayından 190 Devreden KDV hesabına 25.000 ₺ aktarılmıştır. Aralık sonunda 391 Hesaplanan KDV hesabının bakiyesi "
    "70.000 ₺, 191 İndirilecek KDV hesabının bakiyesi 30.000 ₺’dir.\n\nAralık ayı mahsup kaydı aşağıdakilerden hangisidir?",
    K([(391, 70_000)], [(191, 30_000), (190, 25_000), (360, 15_000)]),
    [K([(391, 70_000)], [(191, 30_000), (360, 40_000)]),
     K([(391, 70_000)], [(191, 55_000), (360, 15_000)]),
     K([(391, 70_000), (190, 25_000)], [(191, 30_000), (360, 65_000)]),
     K([(391, 45_000)], [(191, 30_000), (360, 15_000)])],
    "Hesaplanan KDV 70.000 ₺’den önce bu ayın indirilecek KDV’si (30.000 ₺), sonra devreden KDV (25.000 ₺) düşülür; "
    "kalan 15.000 ₺ 360 Ödenecek Vergi ve Fonlar hesabına alacak yazılır.", zorluk="hard")

# 27 — kurumlar vergisi karşılığı
tk, kkeg, ist = 800_000, 50_000, 30_000
mtr = tk + kkeg - ist
kv = mtr * 25 // 100
P.q(f"{R}: 370, 691",
    f"İşletmenin ticari bilanço kârı {tl(tk)} ₺’dir. Kanunen kabul edilmeyen giderler {tl(kkeg)} ₺, iştirak kazancı "
    f"istisnası {tl(ist)} ₺ olup kurumlar vergisi oranı %25’tir. Başka indirim ve istisna bulunmamaktadır.\n\n"
    "Dönem sonunda ayrılacak vergi karşılığının kaydı aşağıdakilerden hangisidir?",
    K([(691, kv)], [(370, kv)]),
    [K([(691, tk * 25 // 100)], [(370, tk * 25 // 100)]),
     K([(691, kv)], [(360, kv)]),
     K([(370, kv)], [(691, kv)]),
     K([(691, (tk + kkeg) * 25 // 100)], [(370, (tk + kkeg) * 25 // 100)])],
    f"Mali kâr = {tl(tk)} + {tl(kkeg)} − {tl(ist)} = {tl(mtr)} ₺; vergi {tl(mtr)} × %25 = {tl(kv)} ₺. 691 Dönem Kârı "
    "Vergi ve Diğer Yasal Yükümlülük Karşılıkları borç, 370 aynı adlı pasif hesap alacak yazılır.", zorluk="hard")

# 28 — geçici vergi mahsubu
P.q(f"{R}: 370, 371, 360",
    f"Yıl sonunda {tl(kv)} ₺ kurumlar vergisi karşılığı 370 hesabına alınmıştır. Yıl içinde ödenen 150.000 ₺ geçici vergi "
    "371 Dönem Kârının Peşin Ödenen Vergi ve Diğer Yükümlülükleri hesabında toplanmıştır. Başka mahsup edilecek vergi "
    "yoktur.\n\nKarşılık ile peşin ödenen verginin mahsubuna ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(370, kv)], [(371, 150_000), (360, kv - 150_000)]),
    [K([(370, kv)], [(193, 150_000), (360, kv - 150_000)]),
     K([(371, 150_000), (360, kv - 150_000)], [(370, kv)]),
     K([(370, kv)], [(360, kv)]),
     K([(691, kv)], [(371, 150_000), (360, kv - 150_000)])],
    f"370 karşılık hesabı kapatılır; yıl içinde ödenen geçici vergi 371’den mahsup edilir, kalan {tl(kv - 150_000)} ₺ "
    "ödenecek vergi olarak 360 hesabına alacak yazılır.")

# 29 — net kârın 590’a aktarılması
nk = 800_000 - kv
P.q(f"{R}: 590, 690, 691, 692",
    f"Yıl sonunda gelir tablosu hesapları kapatılmış ve 690 Dönem Kârı veya Zararı hesabı 800.000 ₺ alacak bakiye "
    f"vermiştir. {tl(kv)} ₺ vergi karşılığı 691 hesabına alınmış, 690 ve 691 hesapları 692 hesabına devredilmiştir.\n\n"
    "692 hesabının kapatılmasına ilişkin kayıt için aşağıdakilerden hangisi doğrudur?",
    T(590, "alacak", nk),
    [T(690, "alacak", nk), T(580, "borç", nk), T(570, "alacak", nk), T(692, "alacak", nk)],
    f"Dönem net kârı 800.000 − {tl(kv)} = {tl(nk)} ₺’dir. 692 Dönem Net Kârı veya Zararı hesabı borçlandırılarak kapatılır, "
    "590 Dönem Net Kârı hesabına alacak yazılır.")

# 30 — dönem zararı
P.q(f"{R}: 591, 692",
    "Yıl sonunda gelir tablosu hesaplarının kapatılmasıyla 690 Dönem Kârı veya Zararı hesabı 120.000 ₺ borç bakiye "
    "vermiştir. Zarar nedeniyle vergi karşılığı ayrılmamış, 690 hesabı 692 hesabına devredilmiştir.\n\n692 hesabının "
    "kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(591, 120_000)], [(692, 120_000)]),
    [K([(692, 120_000)], [(591, 120_000)]),
     K([(580, 120_000)], [(692, 120_000)]),
     K([(591, 120_000)], [(690, 120_000)]),
     K([(692, 120_000)], [(590, 120_000)])],
    "Zarar hâlinde 692 borç bakiye verir; kapatmak için 692 alacaklandırılır ve 591 Dönem Net Zararı (-) hesabı "
    "borçlandırılır. Zarar yeni dönemde 580’e aktarılır.")

# 31 — 591 → 580
P.q(f"{R}: 580, 591",
    "Geçen yıl 120.000 ₺ dönem net zararıyla kapanan işletmenin 591 Dönem Net Zararı hesabı yeni yıla borç bakiyeyle "
    "devretmiştir. Genel kurul zararın gelecek yıl kârlarından mahsup edilmek üzere geçmiş yıl zararlarına aktarılmasına "
    f"karar vermiştir.\n\n{KAYIT}",
    K([(580, 120_000)], [(591, 120_000)]),
    [K([(591, 120_000)], [(580, 120_000)]),
     K([(570, 120_000)], [(591, 120_000)]),
     K([(580, 120_000)], [(590, 120_000)]),
     K([(580, 120_000)], [(500, 120_000)])],
    "Geçmiş yıl zararı 580 Geçmiş Yıllar Zararları (-) hesabında izlenir: 580 borç, 591 alacak 120.000 ₺. İleride "
    "kârlardan mahsup edildiğinde 580 alacaklandırılır.", zorluk="easy")

# 32 — kâr dağıtımı
gyk, yy, kp = 500_000, 25_000, 300_000
st, ou = kp * 15 // 100, gyk - yy - kp
P.q(f"{R}: 540, 542, 570, 331, 360",
    f"Geçmiş yıllar kârları hesabında {tl(gyk)} ₺ bulunan anonim şirketin genel kurulu şu dağıtımı kararlaştırmıştır: "
    f"{tl(yy)} ₺ yasal yedek, gerçek kişi ortaklara {tl(kp)} ₺ brüt kâr payı (%15 gelir vergisi kesintisi yapılacak) ve "
    f"kalan tutar olağanüstü yedek. Kâr payı henüz ödenmemiştir.\n\n{KAYIT}",
    K([(570, gyk)], [(540, yy), (542, ou), (331, kp - st), (360, st)]),
    [K([(570, gyk)], [(540, yy), (542, ou), (331, kp)]),
     K([(590, gyk)], [(540, yy), (542, ou), (331, kp - st), (360, st)]),
     K([(570, gyk)], [(541, yy), (542, ou), (331, kp - st), (360, st)]),
     K([(570, gyk)], [(540, yy), (542, ou), (331, kp - st), (193, st)])],
    f"570 kapatılır; yasal yedek 540’a, kalan {tl(ou)} ₺ 542’ye alacak yazılır. Kâr payının {tl(st)} ₺’lik kesintisi 360’a, "
    f"net {tl(kp - st)} ₺ 331 Ortaklara Borçlar hesabına alacak kaydedilir.", zorluk="hard")

# 33 — 590 → 570
P.q(f"{R}: 570, 590",
    f"Geçen yıl {tl(nk)} ₺ dönem net kârıyla kapanan işletmenin 590 hesabı yeni yıla alacak bakiyeyle devretmiştir. Kâr "
    "dağıtım kararı alınmadan önce kârın geçmiş yıllar kârlarına aktarılması gerekmektedir.\n\nBu aktarıma ilişkin kayıt "
    "için aşağıdakilerden hangisi doğrudur?",
    T(570, "alacak", nk),
    [T(590, "alacak", nk), T(542, "alacak", nk), T(580, "borç", nk), T(692, "alacak", nk)],
    f"Önceki yılın net kârı 590’dan 570 Geçmiş Yıllar Kârları hesabına aktarılır: 590 borç, 570 alacak {tl(nk)} ₺. "
    "Dağıtım bu hesap üzerinden yapılır.", zorluk="easy")

# 34 — gelir tablosu hesaplarının kapatılması
ys, fg2, si, smm, gy = 1_500_000, 30_000, 40_000, 900_000, 200_000
P.q(f"{R}: 690",
    f"Yıl sonunda gelir tablosu hesaplarının bakiyeleri şöyledir: 600 Yurt İçi Satışlar {tl(ys)} ₺, 642 Faiz Gelirleri "
    f"{tl(fg2)} ₺, 610 Satıştan İadeler {tl(si)} ₺, 621 Satılan Ticari Mallar Maliyeti {tl(smm)} ₺, 632 Genel Yönetim "
    f"Giderleri {tl(gy)} ₺.\n\nBu hesapların kapatılmasına ilişkin kayıtlar için aşağıdakilerden hangisi doğrudur?",
    T(690, "alacak", ys + fg2),
    [T(690, "alacak", ys), T(690, "borç", smm + gy), T(690, "alacak", ys + fg2 - si), T(690, "borç", ys + fg2)],
    f"Gelir hesapları (600, 642) borçlandırılıp 690’a alacak yazılır: {tl(ys + fg2)} ₺. Gider ve indirim hesapları (610, "
    f"621, 632) alacaklandırılıp 690’a borç yazılır: {tl(si + smm + gy)} ₺. 690 hesabı {tl(ys + fg2 - si - smm - gy)} ₺ "
    "kâr verir.", zorluk="hard")

# 35 — 770 yansıtma
P.q(f"{R}: 632, 770, 771",
    "7/A seçeneğini uygulayan işletmede yıl içinde 770 Genel Yönetim Giderleri hesabında 200.000 ₺ gider birikmiştir. "
    "Dönem sonunda bu giderlerin gelir tablosuna aktarılması ve 7 grubu hesaplarının kapatılması işlemleri "
    "yapılacaktır.\n\nYansıtma kaydı aşağıdakilerden hangisidir?",
    K([(632, 200_000)], [(771, 200_000)]),
    [K([(632, 200_000)], [(770, 200_000)]),
     K([(771, 200_000)], [(632, 200_000)]),
     K([(690, 200_000)], [(771, 200_000)]),
     K([(631, 200_000)], [(761, 200_000)])],
    "7/A’da gider hesapları yansıtma hesapları aracılığıyla gelir tablosuna aktarılır: 632 Genel Yönetim Giderleri borç, "
    "771 Genel Yönetim Giderleri Yansıtma Hesabı alacak. Ardından 771 ile 770 birbirine kapatılır.")

# 36 — 780 yansıtma
P.q(f"{R}: 660, 780, 781",
    "7/A seçeneğini uygulayan işletmede yıl içinde kısa vadeli banka kredileriyle ilgili 780 Finansman Giderleri "
    "hesabında 96.000 ₺ faiz gideri birikmiştir. Finansman giderlerinin tamamı kısa vadeli borçlanmaya aittir ve "
    "aktifleştirilecek tutar yoktur.\n\nDönem sonu yansıtma kaydı aşağıdakilerden hangisidir?",
    K([(660, 96_000)], [(781, 96_000)]),
    [K([(661, 96_000)], [(781, 96_000)]),
     K([(660, 96_000)], [(780, 96_000)]),
     K([(781, 96_000)], [(660, 96_000)]),
     K([(656, 96_000)], [(781, 96_000)])],
    "Kısa vadeli borçlanmaya ait finansman giderleri 660 Kısa Vadeli Borçlanma Giderleri hesabına borç, 781 Finansman "
    "Giderleri Yansıtma Hesabına alacak yazılarak gelir tablosuna aktarılır; 661 uzun vadeli borçlanma içindir.")

# 37 — uzun vadeli kredinin kısa vadeye aktarılması
P.q(f"{R}: 303, 400",
    "İşletmenin 400 Banka Kredileri hesabında 480.000 ₺ tutarında, dört yıl vadeli ve yıllık eşit anapara taksitli bir "
    "yatırım kredisi bulunmaktadır. Yıl sonu itibarıyla kredinin 120.000 ₺’lik taksidi izleyen on iki ay içinde "
    f"ödenecektir.\n\n{DS}",
    K([(400, 120_000)], [(303, 120_000)]),
    [K([(303, 120_000)], [(400, 120_000)]),
     K([(400, 120_000)], [(300, 120_000)]),
     K([(400, 480_000)], [(303, 480_000)]),
     K([(400, 120_000)], [(102, 120_000)])],
    "Uzun vadeli kredinin bir yıl içinde ödenecek anapara taksidi kısa vadeli yabancı kaynağa sınıflandırılır: 400 borç, "
    "303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri alacak 120.000 ₺.")

# 38 — 480 → 380
P.q(f"{R}: 380, 480",
    "İşletme kiraya verdiği depo için üç yıllık kirayı peşin tahsil etmiş; izleyen yılın payını 380, sonraki yılların "
    "payını 480 Gelecek Yıllara Ait Gelirler hesabına kaydetmiştir. Yıl sonunda 480 hesabında 150.000 ₺ bulunmakta olup "
    "bunun yarısı izleyen yıla aittir.\n\nYıl sonu sınıflandırma kaydı için aşağıdakilerden hangisi doğrudur?",
    T(380, "alacak", 75_000),
    [T(480, "alacak", 75_000), T(649, "alacak", 75_000), T(380, "alacak", 150_000), T(180, "borç", 75_000)],
    "480’deki tutarın izleyen on iki aya ait kısmı (75.000 ₺) kısa vadeli hâle gelir: 480 borç, 380 Gelecek Aylara Ait "
    "Gelirler alacak. Gelir, ilgili aylar geçtikçe 649’a aktarılır.")

# 39 — kasa noksanı yıl sonu
P.q(f"{R}: 197, 689",
    "Yıl içinde kasa sayımında saptanan 1.750 ₺ noksan 197 Sayım ve Tesellüm Noksanları hesabına alınmış, yapılan "
    "araştırmaya rağmen yıl sonuna kadar farkın nedeni ve sorumlusu belirlenememiştir. Tutarın personelden tahsili de "
    f"söz konusu değildir.\n\n{DS}",
    K([(689, 1_750)], [(197, 1_750)]),
    [K([(197, 1_750)], [(100, 1_750)]),
     K([(135, 1_750)], [(197, 1_750)]),
     K([(689, 1_750)], [(100, 1_750)]),
     K([(770, 1_750)], [(397, 1_750)])],
    "Nedeni bulunamayan sayım noksanları dönem sonunda olağan dışı zarar olarak kapatılır: 689 Diğer Olağandışı Gider ve "
    "Zararlar borç, 197 alacak. Kasa sayım tarihinde zaten alacaklandırılmıştır.", zorluk="easy")

# 40 — sayım fazlası yıl sonu
P.q(f"{R}: 397, 679",
    "Yıl içinde stok sayımında bulunan ve 397 Sayım ve Tesellüm Fazlaları hesabına alınan 4.200 ₺’lik fazlalığın nedeni "
    "yıl sonuna kadar belirlenememiştir. Fazlalığın bir tedarikçiye ya da müşteriye ait olduğuna ilişkin bir kanıt "
    f"bulunmamaktadır.\n\nDönem sonu kaydı için aşağıdakilerden hangisi doğrudur?",
    T(679, "alacak", 4_200),
    [T(649, "alacak", 4_200), T(153, "alacak", 4_200), T(397, "alacak", 4_200), T(644, "alacak", 4_200)],
    "Nedeni belirlenemeyen sayım fazlası dönem sonunda olağan dışı gelir olarak kapatılır: 397 borç, 679 Diğer "
    "Olağandışı Gelir ve Kârlar alacak 4.200 ₺.")

# 41 — dönem sonu işlemlerinin sırası
P.q("MSUGT: dönem sonu işlemleri",
    "Muhasebe müdürü yeni başlayan bir çalışana yıl sonunda yapılacak işleri anlatmaktadır: kesin mizanın çıkarılması, "
    "envanter işlemleri ve düzeltme kayıtları, geçici mizanın düzenlenmesi, finansal tabloların hazırlanması ve kapanış "
    "kaydı.\n\nBu işlerin doğru sırası aşağıdakilerden hangisidir?",
    "Geçici mizan → envanter ve düzeltme → kesin mizan → tablolar → kapanış",
    ["Envanter ve düzeltme → geçici mizan → kesin mizan → tablolar → kapanış",
     "Geçici mizan → kesin mizan → envanter ve düzeltme → tablolar → kapanış",
     "Kesin mizan → envanter ve düzeltme → geçici mizan → kapanış → tablolar",
     "Geçici mizan → envanter ve düzeltme → tablolar → kesin mizan → kapanış"],
    "Önce dönem içi kayıtların kontrolü için geçici mizan düzenlenir, sonra envanter ve düzeltme kayıtları yapılır, "
    "kesin mizan çıkarılır, finansal tablolar hazırlanır ve en son hesaplar kapanış kaydıyla kapatılır.")

# 42 — dönem sonu kaydı olmayan (olumsuz)
P.q("MSUGT: dönem sonu işlemleri",
    "Yıl sonunda muhasebe servisi 31 Aralık tarihli bir dizi kayıt hazırlamaktadır: amortisman ayrılması, alacak "
    "senetlerinin reeskontu, tahakkuk etmiş faizin kaydı, dövizli kalemlerin değerlemesi ve aynı gün yapılan peşin bir "
    "mal satışının faturasının kaydı.\n\nBu kayıtlardan hangisi dönem sonu envanter (düzeltme) kaydı niteliğinde değildir?",
    "Aynı gün yapılan peşin mal satışının kaydı",
    ["Amortisman ayrılmasına ilişkin kayıt",
     "Alacak senetlerinin reeskont kaydı",
     "Tahakkuk etmiş faizin kaydı",
     "Dövizli kalemlerin değerleme kaydı"],
    "Peşin satış 31 Aralık’ta gerçekleşse de olağan bir dönem içi işlemdir. Amortisman, reeskont, tahakkuk ve kur "
    "değerlemesi ise envanter sonuçlarına göre yapılan dönem sonu düzeltme kayıtlarıdır.")

# 43 — çalışmayan kısım amortismanı
P.q(f"{R}: 680, 730",
    "Üretimde kullanılan bir makinenin yıllık amortismanı 90.000 ₺’dir. Talep yetersizliği nedeniyle makine yılın dört "
    "ayında tamamen durdurulmuş, kalan sekiz ay normal kapasiteyle çalışmıştır. İşletme 7/A seçeneğini "
    f"uygulamaktadır.\n\n{DS}",
    K([(730, 60_000), (680, 30_000)], [(257, 90_000)]),
    [K([(730, 90_000)], [(257, 90_000)]),
     K([(730, 60_000), (689, 30_000)], [(257, 90_000)]),
     K([(730, 60_000), (770, 30_000)], [(257, 90_000)]),
     K([(730, 30_000), (680, 60_000)], [(257, 90_000)])],
    "Çalışılan sekiz aya düşen 90.000 × 8/12 = 60.000 ₺ üretim maliyetidir (730). Çalışılmayan dört aya düşen 30.000 ₺ "
    "maliyete yüklenmez, 680 Çalışmayan Kısım Gider ve Zararları hesabına borç yazılır.", zorluk="hard")

# 44 — hurdaya ayrılan tam amortismanlı demirbaş
P.q(f"{R}: 255, 257",
    "İşletmenin 45.000 ₺ maliyetli ve tamamı amortismana tabi tutulmuş bilgisayarları kullanılamaz hâle gelmiş ve "
    "hurdaya ayrılmıştır. Hurda için herhangi bir satış bedeli elde edilmemiş ve ek masraf yapılmamıştır.\n\n"
    f"{KAYIT}",
    K([(257, 45_000)], [(255, 45_000)]),
    [K([(689, 45_000)], [(255, 45_000)]),
     K([(257, 45_000)], [(253, 45_000)]),
     K([(770, 45_000)], [(257, 45_000)]),
     K([(257, 45_000)], [(679, 45_000)])],
    "Tamamen amortismana tabi tutulmuş varlığın net değeri sıfırdır; kayıttan çıkarılırken birikmiş amortisman 257 borç, "
    "varlık 255 Demirbaşlar alacak 45.000 ₺ ile kapatılır. Zarar doğmaz.", zorluk="easy")

# 45 — kısmen amortismanlı varlığın hurdaya ayrılması
P.q(f"{R}: 689",
    "Maliyeti 60.000 ₺, birikmiş amortismanı 48.000 ₺ olan bir üretim makinesi arıza nedeniyle kullanılamaz hâle gelmiş "
    "ve bedelsiz olarak hurdaya ayrılmıştır. Makine için sigorta tazminatı söz konusu değildir.\n\n"
    f"{DOGRU}",
    T(689, "borç", 12_000),
    [T(689, "borç", 60_000), T(257, "alacak", 48_000), T(253, "alacak", 48_000), T(730, "borç", 12_000)],
    "Net defter değeri 60.000 − 48.000 = 12.000 ₺’dir ve olağan dışı zarar olarak 689 hesabına borç yazılır; 257 hesabı "
    "48.000 ₺ borçlandırılır, 253 hesabı 60.000 ₺ alacaklandırılır.")

# 46 — 193 → 371
P.q(f"{R}: 193, 371",
    "Yıl içinde işletmenin mevduat faizlerinden kesilen 18.000 ₺ gelir vergisi 193 Peşin Ödenen Vergiler ve Fonlar "
    "hesabında toplanmıştır. Bu tutar yıl sonunda hesaplanacak kurumlar vergisinden mahsup edilecektir.\n\n"
    f"Dönem sonu sınıflandırma kaydı için aşağıdakilerden hangisi doğrudur?",
    T(371, "borç", 18_000),
    [T(370, "borç", 18_000), T(360, "alacak", 18_000), T(193, "borç", 18_000), T(371, "alacak", 18_000)],
    "Vergiden mahsup edilecek peşin ödenen vergiler dönem sonunda 193’ten 371 Dönem Kârının Peşin Ödenen Vergi ve Diğer "
    "Yükümlülükleri hesabına aktarılır: 371 borç, 193 alacak 18.000 ₺.")

# 47 — satış mağazası kira tahakkuku
P.q(f"{R}: 381, 760",
    "İşletme satış mağazası için aylık 25.000 ₺ kira ödemektedir. Aralık ayı kirası sözleşme gereği ocak ayının ilk "
    "haftasında ödenecek ve kiraya veren şirket faturasını ödeme tarihinde düzenleyecektir. KDV bu soruda dikkate "
    f"alınmayacaktır.\n\nDönem sonu kaydı için aşağıdakilerden hangisi doğrudur?",
    T(381, "alacak", 25_000),
    [T(180, "borç", 25_000), T(320, "alacak", 25_000), T(770, "borç", 25_000), T(381, "alacak", 300_000)],
    "Aralık kirası cari dönemin gideridir ancak henüz ödenmemiş ve faturalanmamıştır: 760 Pazarlama, Satış ve Dağıtım "
    "Giderleri borç, 381 Gider Tahakkukları alacak 25.000 ₺.")

# 48 — 760 yansıtma
P.q(f"{R}: 631, 760, 761",
    "7/A seçeneğini uygulayan ticaret işletmesinde yıl içinde 760 Pazarlama, Satış ve Dağıtım Giderleri hesabında "
    "340.000 ₺ gider birikmiştir. Dönem sonunda bu giderler gelir tablosuna aktarılacak ve 7 grubu kapatılacaktır.\n\n"
    "Yansıtma kaydı aşağıdakilerden hangisidir?",
    K([(631, 340_000)], [(761, 340_000)]),
    [K([(632, 340_000)], [(761, 340_000)]),
     K([(631, 340_000)], [(760, 340_000)]),
     K([(761, 340_000)], [(631, 340_000)]),
     K([(621, 340_000)], [(761, 340_000)])],
    "Pazarlama, satış ve dağıtım giderleri 631 hesabı aracılığıyla gelir tablosuna aktarılır: 631 borç, 761 Pazarlama, "
    "Satış ve Dağıtım Giderleri Yansıtma Hesabı alacak; ardından 761 ile 760 birbirine kapatılır.")

# 49 — kapanış kaydı
P.q("MSUGT: kapanış kaydı",
    "Finansal tablolarını hazırlayan işletme, bilanço hesaplarını kapatmak için kapanış kaydını yapacaktır. Aktif "
    "hesapların toplamı 5.600.000 ₺, düzenleyici hesaplar düşülmeden önceki pasif karakterli hesapların toplamı da aynı "
    "tutardadır.\n\nKapanış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Borç bakiyeli hesaplar alacaklandırılır, alacak bakiyeliler borçlandırılır.",
    ["Tüm bilanço hesapları borçlandırılarak kapatılır.",
     "Sadece gelir tablosu hesapları kapatılır.",
     "Aktif hesaplar borçlandırılır, pasif hesaplar alacaklandırılır.",
     "Düzenleyici hesaplar kapanış kaydında yer almaz."],
    "Kapanış kaydında her hesap bakiyesinin tersi yönde kaydedilir: borç bakiyeli (aktif) hesaplar alacaklandırılır, "
    "alacak bakiyeli (pasif ve düzenleyici aktif) hesaplar borçlandırılır; kayıt yeni yılın açılış kaydının tersidir.")

# 50 — mizan türleri
P.q("MSUGT: mizan",
    "Bir işletmede 31 Aralık itibarıyla dönem içi kayıtlar tamamlanmış, ancak amortisman, reeskont, tahakkuk ve değerleme "
    "kayıtları henüz yapılmamıştır. Yönetim bu aşamada tüm hesapların borç-alacak toplamlarını ve bakiyelerini gösteren "
    "bir liste istemiştir.\n\nİstenen listeyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Bu liste geçici mizandır; düzeltmelerden sonra kesin mizan düzenlenir.",
    ["Bu liste kesin mizandır; tablolar doğrudan buradan hazırlanır.",
     "Bu liste kapanış mizanıdır; yeni yıla devredilir.",
     "Bu liste envanter defteridir; tasdik ettirilmesi gerekir.",
     "Bu liste yevmiye defteridir; kayıtlar tarih sırasıyla yer alır."],
    "Dönem içi kayıtlar sonrası, envanter ve düzeltme kayıtlarından önce düzenlenen mizan geçici mizandır. Düzeltme "
    "kayıtlarından sonra hazırlanan kesin mizan finansal tabloların dayanağıdır.")

# 51 — azalan bakiyeler son yıl
P.sayisal("VUK md. 315",
    "Azalan bakiyeler yöntemiyle amortismana tabi tutulan 500.000 ₺ maliyetli, 5 yıl faydalı ömürlü bir makine için "
    "ilk dört yılda sırasıyla 200.000 ₺, 120.000 ₺, 72.000 ₺ ve 43.200 ₺ amortisman ayrılmıştır. Makine beşinci yılda da "
    "kullanılmaktadır.\n\nBeşinci yılda ayrılacak amortisman kaç ₺’dir?",
    tl(64_800), secenekler(64_800, 25_920, 100_000, 43_200, 38_880),
    "Azalan bakiyeler yönteminde son yıla kalan değer tamamen amortismana tabi tutulur: 500.000 − (200.000 + 120.000 + "
    "72.000 + 43.200) = 64.800 ₺. %40 uygulanırsa 25.920 ₺ bulunurdu, ancak kalan değer tamamen itfa edilir.",
    zorluk="hard")

# 52 — 181’in tahsili
P.q(f"{R}: 102, 181, 642",
    f"Önceki yıl sonunda üç ay vadeli mevduatın aralık ayı faizi olan {tl(fg)} ₺ 181 Gelir Tahakkukları hesabına "
    f"alınmıştır. Şubat sonunda vade dolmuş ve üç aylık faizin tamamı olan {tl(fg * 3)} ₺ banka hesabına geçmiştir; "
    f"gelir vergisi kesintisi bu soruda dikkate alınmayacaktır.\n\n{KAYIT}",
    K([(102, fg * 3)], [(181, fg), (642, fg * 2)]),
    [K([(102, fg * 3)], [(642, fg * 3)]),
     K([(102, fg * 3)], [(181, fg * 3)]),
     K([(102, fg * 3)], [(181, fg), (649, fg * 2)]),
     K([(181, fg), (102, fg * 2)], [(642, fg * 3)])],
    f"Aralık payı ({tl(fg)} ₺) önceki yıl gelir yazıldığı için 181 kapatılır; yeni yıla ait ocak-şubat faizi "
    f"({tl(fg * 2)} ₺) 642 Faiz Gelirleri hesabına alacak yazılır.")

# 53 — kıst amortisman yok (VUK)
P.q("VUK md. 320",
    "Vergi Usul Kanunu’na göre değerleme yapan işletme 1 Ekim’de 300.000 ₺’ye bir üretim makinesi satın alarak hemen "
    "kullanmaya başlamıştır. Makinenin faydalı ömrü 5 yıl olup normal amortisman uygulanacaktır; makine binek otomobil "
    "değildir.\n\nİlk yıl için ayrılacak amortisman ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Tam yıllık amortisman olarak 60.000 ₺ ayrılır.",
    ["Kıst amortisman olarak 15.000 ₺ ayrılır.",
     "Kıst amortisman olarak 45.000 ₺ ayrılır.",
     "İlk yıl amortisman ayrılmaz, ertesi yıl başlar.",
     "Tam yıllık amortisman olarak 75.000 ₺ ayrılır."],
    "VUK’ta amortisman yıllık olarak ayrılır; yıl içinde alınan varlık için gün ya da ay hesabı yapılmaz ve binek "
    "otomobiller dışında tam yıllık amortisman ayrılır: 300.000 / 5 = 60.000 ₺.", zorluk="hard")

# 54 — menkul kıymet değer artışı (karşılık iptali)
P.q(f"{R}: 119, 644",
    "Geçen yıl sonunda maliyeti 80.000 ₺ olan hisse senetleri için 15.000 ₺ değer düşüklüğü karşılığı ayrılmıştır. Bu "
    "yıl sonunda senetler hâlâ elde tutulmakta olup borsa değerleri 74.000 ₺’ye yükselmiştir.\n\n"
    f"Dönem sonu kaydı için aşağıdakilerden hangisi doğrudur?",
    T(644, "alacak", 9_000),
    [T(644, "alacak", 15_000), T(110, "borç", 9_000), T(645, "alacak", 9_000), T(119, "alacak", 6_000)],
    "Gereken karşılık 80.000 − 74.000 = 6.000 ₺’dir; mevcut 15.000 ₺ karşılığın 9.000 ₺’lik kısmı konusu kalmamıştır: "
    "119 borç, 644 Konusu Kalmayan Karşılıklar alacak.", zorluk="hard")

# 55 — şüpheli alacak karşılığının koşulları
P.q("VUK md. 323",
    "İşletmenin yıl sonunda üç müşteriden tahsil edilemeyen alacakları bulunmaktadır: A müşterisi için dava açılmıştır; B "
    "müşterisine sadece ihtarname gönderilmiştir; C müşterisinin borcu ise tamamen ipotekle teminat altındadır.\n\n"
    "Vergi Usul Kanunu’na göre şüpheli alacak karşılığı ayrılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Sadece A’nın alacağı için karşılık ayrılır.",
    ["Üç müşteriden olan alacakların tamamı için karşılık ayrılır.",
     "A ve B müşterilerinden olan alacaklar için karşılık ayrılır.",
     "Sadece C müşterisinden olan alacak için karşılık ayrılır.",
     "Üçüne de karşılık ayrılmaz, alacaklar zarar yazılır."],
    "Şüpheli alacak karşılığı dava veya icra safhasındaki alacaklar ile yapılan protestoya veya yazı ile istenmesine "
    "rağmen bir defadan fazla ödenmemiş küçük alacaklar için ayrılır; teminatlı kısım için karşılık ayrılmaz. Bu verilerle "
    "karşılığa konu olan A’nın alacağıdır.", zorluk="hard")

# 56 — döviz tevdiat hesabı, kur düşüşü
P.q(f"{R}: 102, 656",
    "İşletmenin banka hesabında yıl sonunda 10.000 ABD doları bulunmaktadır. Dövizler hesaba 41 ₺ kurla girmiş olup "
    "değerleme günü kuru 39,50 ₺’dir. İşletme dövizleri ocak ayında ithalat bedeli olarak ödemeyi planlamaktadır.\n\n"
    f"Dönem sonu değerleme kaydı için aşağıdakilerden hangisi doğrudur?",
    T(656, "borç", 15_000),
    [T(646, "alacak", 15_000), T(102, "borç", 15_000), T(780, "borç", 15_000), T(656, "borç", 395_000)],
    "Dövizlerin değeri 10.000 × 39,50 = 395.000 ₺’ye inmiştir; kayıtlı değer 410.000 ₺. 15.000 ₺ azalış 656 Kambiyo "
    "Zararları borç, 102 Bankalar alacak ile kaydedilir.")

# 57 — yıl sonu 180 bakiyesi
P.sayisal(f"{R}: 180",
    "İşletme 1 Ekim’de bir reklam ajansıyla 12 aylık hizmet sözleşmesi imzalamış ve bedeli olan 48.000 ₺’yi peşin "
    "ödeyerek 180 Gelecek Aylara Ait Giderler hesabına kaydetmiştir. Ekim, kasım ve aralık payları ay sonlarında gidere "
    "aktarılmıştır.\n\nYıl sonunda 180 hesabının bakiyesi kaç ₺’dir?",
    tl(36_000), secenekler(36_000, 12_000, 48_000, 44_000, 32_000),
    "Aylık pay 48.000 / 12 = 4.000 ₺’dir. Üç ay (12.000 ₺) gidere aktarıldığından 180 hesabında 48.000 − 12.000 = "
    "36.000 ₺ kalır.", zorluk="easy")

# 58 — kira gelir tahakkuku
P.q(f"{R}: 181, 649",
    "Esas faaliyeti dışında bir depo kiraya veren işletme, aralık ayı kirası olan 18.000 ₺’yi sözleşme gereği ocak "
    "ayında tahsil edecek ve faturasını tahsil tarihinde düzenleyecektir. KDV bu soruda dikkate alınmayacaktır.\n\n"
    f"Dönem sonu kaydı için aşağıdakilerden hangisi doğrudur?",
    T(181, "borç", 18_000),
    [T(380, "alacak", 18_000), T(120, "borç", 18_000), T(600, "alacak", 18_000), T(181, "alacak", 18_000)],
    "Aralık kirası cari dönemin gelirdir ancak henüz tahsil edilmemiş ve faturalanmamıştır: 181 Gelir Tahakkukları borç, "
    "649 Diğer Olağan Gelir ve Kârlar alacak 18.000 ₺.")

# 59 — normal amortisman oranı
P.sayisal("VUK md. 315",
    "Faydalı ömrü 8 yıl olarak belirlenen bir tesis için işletme normal amortisman yöntemini seçmiştir. Tesisin maliyeti "
    "2.400.000 ₺ olup yıl başında hizmete girmiştir ve işletme yöntemi amortisman süresince değiştirmeyecektir.\n\n"
    "Tesis için yıllık amortisman tutarı kaç ₺’dir?",
    tl(300_000), secenekler(300_000, 600_000, 240_000, 480_000, 200_000),
    "Normal amortisman oranı 1 / 8 = %12,5’tir: 2.400.000 × %12,5 = 300.000 ₺. Azalan bakiyeler seçilseydi oran %25 "
    "olur ve ilk yıl 600.000 ₺ ayrılırdı.", zorluk="easy")

# 60 — kasa kapanışı değil: 7 grubu kapanışı (770-771)
P.q(f"{R}: 770, 771",
    "7/A seçeneğini uygulayan işletmede dönem sonunda 770 Genel Yönetim Giderleri hesabının 200.000 ₺ borç bakiyesi 771 "
    "Genel Yönetim Giderleri Yansıtma Hesabı aracılığıyla 632’ye aktarılmıştır. Şimdi 7 grubundaki bu iki hesabın "
    "kapatılması gerekmektedir.\n\nBu kapanış kaydı aşağıdakilerden hangisidir?",
    K([(771, 200_000)], [(770, 200_000)]),
    [K([(770, 200_000)], [(771, 200_000)]),
     K([(632, 200_000)], [(770, 200_000)]),
     K([(690, 200_000)], [(771, 200_000)]),
     K([(771, 200_000)], [(632, 200_000)])],
    "Yansıtma sonrasında 771 alacak, 770 borç bakiye verir; iki hesap birbirine kapatılır: 771 borç, 770 alacak "
    "200.000 ₺. Gider gelir tablosuna 632 aracılığıyla aktarılmıştır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
