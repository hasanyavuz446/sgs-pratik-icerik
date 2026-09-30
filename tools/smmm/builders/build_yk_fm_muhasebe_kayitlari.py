# -*- coding: utf-8 -*-
"""Finansal Muhasebe · Muhasebe Kayıtları (dönem içi işlemler) — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında Finansal Muhasebe soruları tutar ve KDV oranı veren bir olay
anlatıp "günlük defter kaydı aşağıdakilerden hangisidir?" diye sorar; şıklar ya tam yevmiye kaydıdır
ya da "… hesabının alacak tarafına X ₺ kaydedilir" biçimindedir. Mevzuat atfı azdır (%15).

Dayanak: Muhasebe Sistemi Uygulama Genel Tebliği (MSUGT) Tekdüzen Hesap Planı ve hesap işleyiş
kuralları; 3065 s. KDV Kanunu genel oran %20 (soruda verilir). Tutarlar builder içinde hesaplanır,
her doğru kaydın borç/alacak eşitliği fm_ortak.kayit() tarafından denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K, taraf as T, ad, hk

P = Paket("questions_topic_finansal_muhasebe_kayitlari_2026.json", lesson="finansal_muhasebe",
          topic="muhasebe_kayitlari", konu_adi="Muhasebe Kayıtları", seed=2026093061,
          surum="MSUGT Tekdüzen Hesap Planı ve hesap işleyiş kuralları; KDV genel oranı %20; 29.09.2026 kontrolü")

R = "MSUGT Tekdüzen Hesap Planı"
KAYIT = "Bu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?"
DOGRU = "Bu işleme ilişkin günlük defter kaydı için aşağıdakilerden hangisi doğrudur?"

# 1 — kredili satış, bedelin bir kısmı müşteri çekiyle
s, kdv = 50_000, 10_000
cek = 24_000
P.q(f"{R}: 101, 120, 391, 600",
    f"Ticari mal alım satımı yapan bir işletme, tanesi 2.500 ₺ olan 20 adet ürünü %20 KDV ile bir müşterisine satmıştır. "
    f"Müşteri satış bedelinin {tl(cek)} ₺’lik kısmı için kendi bankasına çekilmiş bir çeki ciro ederek vermiş, kalan "
    f"tutarın bir ay sonra ödenmesi kararlaştırılmıştır.\n\n{KAYIT}",
    K([(101, cek), (120, s + kdv - cek)], [(600, s), (391, kdv)]),
    [K([(103, cek), (120, s + kdv - cek)], [(600, s), (391, kdv)]),
     K([(101, cek), (120, s + kdv - cek)], [(600, s), (191, kdv)]),
     K([(121, cek), (120, s + kdv - cek)], [(600, s), (391, kdv)]),
     K([(101, cek), (120, s - cek)], [(600, s)])],
    f"Müşteriden alınan çek 101 Alınan Çekler, vadeli kısım 120 Alıcılar hesabına borç yazılır. Satış bedeli {tl(s)} ₺ "
    f"600 Yurt İçi Satışlar, {tl(kdv)} ₺ KDV 391 Hesaplanan KDV hesabına alacak yazılır; 103 işletmenin kendi keşide ettiği "
    "çekleri, 121 senetli alacakları izler.")

# 2 — verilen çekin bankaca ödenmesi
P.q(f"{R}: 103, 102",
    "İşletme 5 Mart’ta satıcısına olan 36.000 ₺ borcu için 30 Mart vadeli ve kendi banka hesabına çekilmiş bir çek "
    "düzenleyip vermiştir. Satıcı çeki vadesinde bankaya ibraz etmiş, banka da 30 Mart’ta işletmenin vadesiz hesabından "
    "çek bedelini ödeyerek işletmeye hesap özetini göndermiştir.\n\n30 Mart tarihinde yapılacak günlük defter kaydı "
    "aşağıdakilerden hangisidir?",
    K([(103, 36_000)], [(102, 36_000)]),
    [K([(320, 36_000)], [(102, 36_000)]),
     K([(320, 36_000)], [(103, 36_000)]),
     K([(101, 36_000)], [(102, 36_000)]),
     K([(102, 36_000)], [(103, 36_000)])],
    "Çek verildiğinde 320 Satıcılar borç, 103 Verilen Çekler ve Ödeme Emirleri alacak yazılmıştı. Banka çeki ödediğinde "
    "pasif karakterli düzenleyici 103 hesabı borçlandırılarak kapatılır ve 102 Bankalar hesabı alacaklandırılır.")

# 3 — kasa sayım noksanı: nedeni araştırılıyor
P.q(f"{R}: 197, 100",
    "Ay sonunda yapılan kasa sayımında kasada 18.450 ₺ nakit bulunmuş, kasa hesabının kayıtlı bakiyesi ise 19.200 ₺ "
    "olarak saptanmıştır. Farkın bir ödeme belgesinin kaydedilmemesinden mi yoksa kasiyer hatasından mı kaynaklandığı "
    "henüz belirlenememiş, konu araştırmaya alınmıştır.\n\nBu tespit üzerine yapılacak günlük defter kaydı "
    "aşağıdakilerden hangisidir?",
    K([(197, 750)], [(100, 750)]),
    [K([(100, 750)], [(397, 750)]),
     K([(689, 750)], [(100, 750)]),
     K([(135, 750)], [(100, 750)]),
     K([(770, 750)], [(100, 750)])],
    "Kayıtlı bakiye 19.200 ₺, fiilî mevcut 18.450 ₺ olduğundan 750 ₺ noksan vardır. Nedeni belirleninceye kadar 197 Sayım "
    "ve Tesellüm Noksanları hesabına borç, 100 Kasa hesabına alacak yazılır; neden anlaşılınca ilgili hesaba aktarılır.")

# 4 — noksanın kasiyerden tahsil edilmesi kararı
P.q(f"{R}: 197, 135",
    "Kasa sayımında saptanan ve 197 Sayım ve Tesellüm Noksanları hesabına alınan 1.200 ₺’lik farkın, kasiyerin para "
    "üstü hatasından doğduğu anlaşılmıştır. Yönetim bu tutarın kasiyerin şubat ayı ücretinden kesilmek üzere kasiyerden "
    f"alacak olarak izlenmesine karar vermiştir.\n\n{DOGRU}",
    T(135, "borç", 1_200),
    [T(689, "borç", 1_200), T(197, "borç", 1_200), T(100, "alacak", 1_200), T(335, "alacak", 1_200)],
    "Nedeni anlaşılan noksan 197 hesabından çıkarılır: kasiyerden alınacak tutar 135 Personelden Alacaklar hesabına borç, "
    "197 hesabına alacak yazılır. Kasa daha önce alacaklandırıldığı için yeniden kayıt gerekmez.")

# 5 — borç senedinin faizle yenilenmesi
eski, yeni = 40_000, 42_400
P.q(f"{R}: 321, 780",
    f"İşletme, vadesi gelen {tl(eski)} ₺ nominal değerli borç senedini ödeyememiş ve satıcısıyla anlaşarak iki ay "
    f"sonrasına vadeli, {tl(yeni)} ₺ nominal değerli yeni bir senet düzenleyerek eski senedi geri almıştır. Aradaki fark "
    f"iki aylık vade farkıdır.\n\n{KAYIT}",
    K([(321, eski), (780, yeni - eski)], [(321, yeni)]),
    [K([(321, eski), (657, yeni - eski)], [(321, yeni)]),
     K([(321, yeni)], [(321, eski), (642, yeni - eski)]),
     K([(320, eski), (780, yeni - eski)], [(321, yeni)]),
     K([(121, yeni)], [(121, eski), (642, yeni - eski)])],
    f"Eski senet 321 Borç Senetleri hesabına borç yazılarak kapatılır, yeni senet aynı hesaba {tl(yeni)} ₺ alacak yazılır. "
    f"{tl(yeni - eski)} ₺ vade farkı borçlanma maliyeti olduğundan 780 Finansman Giderleri hesabına borç kaydedilir.")

# 6 — alacak senedinin iskontoya verilmesi
nom, isk = 60_000, 3_150
P.q(f"{R}: 121, 102, 780",
    f"İşletme, müşterisinden aldığı ve vadesine 90 gün bulunan {tl(nom)} ₺ nominal değerli senedi nakit ihtiyacı nedeniyle "
    f"bankaya iskonto ettirmiştir. Banka {tl(isk)} ₺ iskonto faizini keserek kalan tutarı işletmenin vadesiz mevduat "
    f"hesabına aktarmıştır.\n\n{KAYIT}",
    K([(102, nom - isk), (780, isk)], [(121, nom)]),
    [K([(102, nom - isk), (122, isk)], [(121, nom)]),
     K([(102, nom)], [(121, nom - isk), (642, isk)]),
     K([(102, nom - isk), (657, isk)], [(121, nom)]),
     K([(102, nom - isk), (780, isk)], [(101, nom)])],
    f"Senet elden çıktığı için 121 Alacak Senetleri {tl(nom)} ₺ alacaklandırılır. Bankaya yatan {tl(nom - isk)} ₺ 102 "
    f"Bankalar, kesilen {tl(isk)} ₺ iskonto faizi finansman maliyeti olarak 780 Finansman Giderleri hesabına borç yazılır.")

# 7 — alacak senedinin ciro edilmesi
P.q(f"{R}: 320, 121",
    "İşletme, 12.000 ₺ ve 8.000 ₺ nominal değerli iki müşteri senedinden 12.000 ₺’lik olanı, 15.000 ₺ tutarındaki satıcı "
    "borcunun bir kısmını kapatmak üzere ciro ederek satıcısına vermiş; kalan 3.000 ₺’yi aynı gün banka havalesiyle "
    f"ödemiştir.\n\n{KAYIT}",
    K([(320, 15_000)], [(121, 12_000), (102, 3_000)]),
    [K([(320, 15_000)], [(321, 12_000), (102, 3_000)]),
     K([(320, 15_000)], [(121, 15_000)]),
     K([(321, 12_000), (320, 3_000)], [(102, 15_000)]),
     K([(320, 15_000)], [(101, 12_000), (102, 3_000)])],
    "Ciro edilen müşteri senedi işletmenin aktifinden çıktığı için 121 Alacak Senetleri 12.000 ₺, havale edilen tutar "
    "102 Bankalar 3.000 ₺ alacaklandırılır; kapanan borç için 320 Satıcılar 15.000 ₺ borçlandırılır.")

# 8 — protestolu senet
P.q(f"{R}: 128, 121",
    "Vadesinde ödenmeyen 25.000 ₺ nominal değerli müşteri senedi protesto edilmiş, işletme alacağın tahsili için dava "
    "açmaya karar vermiştir. Protesto işlemi için notere nakit olarak 600 ₺ masraf ödenmiş ve bu masrafın da müşteriden "
    f"istenmesine karar verilmiştir.\n\n{KAYIT}",
    K([(128, 25_600)], [(121, 25_000), (100, 600)]),
    [K([(128, 25_000), (770, 600)], [(121, 25_000), (100, 600)]),
     K([(129, 25_600)], [(121, 25_000), (100, 600)]),
     K([(128, 25_600)], [(120, 25_000), (100, 600)]),
     K([(654, 25_600)], [(129, 25_600)])],
    "Protestolu ve dava safhasındaki senet 128 Şüpheli Ticari Alacaklar hesabına aktarılır; müşteriden istenecek protesto "
    "masrafı da alacağa eklenir: 128 borç 25.600 ₺, 121 alacak 25.000 ₺, 100 Kasa alacak 600 ₺. Karşılık dönem sonunda ayrılır.")

# 9 — şüpheli alacağın kısmen tahsili (karşılık önceki yıl ayrılmış)
alac, kars, tahsil = 30_000, 30_000, 12_000
P.q(f"{R}: 102, 128, 129, 644",
    f"İşletme geçen yıl dava safhasındaki {tl(alac)} ₺’lik alacağının tamamı için şüpheli alacak karşılığı ayırmıştır. "
    f"Bu yıl mahkeme süreci devam ederken borçlu müşteri {tl(tahsil)} ₺ ödeme yapmış ve tutar işletmenin banka "
    "hesabına yatırılmıştır; kalan alacak için dava sürmektedir.\n\nBu tahsilata ilişkin kayıtlar için aşağıdakilerden "
    "hangisi doğrudur?",
    T(644, "alacak", tahsil),
    [T(129, "alacak", tahsil), T(654, "alacak", tahsil), T(128, "borç", tahsil), T(671, "alacak", tahsil)],
    f"Tahsilat 102 Bankalar borç, 128 alacak ile kaydedilir. Önceki yıl ayrılan karşılığın {tl(tahsil)} ₺’lik kısmı konusu "
    "kalmadığından 129 hesabına borç, 644 Konusu Kalmayan Karşılıklar hesabına alacak yazılır.", zorluk="hard")

# 10 — satış iskontosu faturası
isk, kdv = 4_000, 800
P.q(f"{R}: 611, 391, 120",
    "İşletme, yıl içinde toplam 400.000 ₺ + KDV tutarında vadeli satış yaptığı bir müşterisine, sözleşmedeki ciro "
    "hedefine ulaştığı için satış tutarının %1’i oranında iskonto tanımış ve %20 KDV’li iskonto faturası düzenleyerek "
    f"tutarı müşterinin cari hesabına yansıtmıştır.\n\n{KAYIT}",
    K([(611, isk), (391, kdv)], [(120, isk + kdv)]),
    [K([(610, isk), (391, kdv)], [(120, isk + kdv)]),
     K([(611, isk), (191, kdv)], [(120, isk + kdv)]),
     K([(760, isk + kdv)], [(120, isk + kdv)]),
     K([(120, isk + kdv)], [(611, isk), (391, kdv)])],
    "Ciro primi niteliğindeki sonradan verilen iskonto 611 Satış İskontoları hesabına borç yazılır; satışta hesaplanan KDV "
    "de o ölçüde azaldığı için 391 Hesaplanan KDV borçlandırılır. Müşteri alacağı 4.800 ₺ azalır: 120 alacak.")

# 11 — satıştan iade (aralıklı envanter)
iade, kdv = 7_500, 1_500
P.q(f"{R}: 610, 391, 120",
    "Aralıklı envanter yöntemini uygulayan işletme, geçen hafta vadeli olarak sattığı malların 7.500 ₺ + %20 KDV "
    "tutarındaki kısmının ambalaj hatası nedeniyle müşteri tarafından iade edildiğini, müşterinin gönderdiği iade faturası "
    f"üzerinden kayda almıştır.\n\n{KAYIT}",
    K([(610, iade), (391, kdv)], [(120, iade + kdv)]),
    [K([(600, iade), (391, kdv)], [(120, iade + kdv)]),
     K([(153, iade), (191, kdv)], [(120, iade + kdv)]),
     K([(610, iade), (191, kdv)], [(120, iade + kdv)]),
     K([(611, iade + kdv)], [(120, iade + kdv)])],
    "Satıştan iadeler brüt satışları doğrudan azaltmaz, 610 Satıştan İadeler hesabına borç yazılır; iade edilen malın KDV’si "
    "391 Hesaplanan KDV’yi azaltır. Aralıklı envanterde maliyet kaydı dönem sonunda yapılır.")

# 12 — alıştan iade
P.q(f"{R}: 320, 153, 191",
    "İşletme, vadeli olarak satın aldığı 90.000 ₺ + %20 KDV tutarındaki ticari mallardan 15.000 ₺’lik kısmının sipariş "
    "şartnamesine uymadığını saptamış ve bu malları iade faturası düzenleyerek satıcısına geri göndermiştir. Satıcı iadeyi "
    f"kabul etmiş, cari hesaptan düşmüştür.\n\n{KAYIT}",
    K([(320, 18_000)], [(153, 15_000), (191, 3_000)]),
    [K([(320, 18_000)], [(153, 15_000), (391, 3_000)]),
     K([(320, 18_000)], [(610, 15_000), (191, 3_000)]),
     K([(153, 15_000), (191, 3_000)], [(320, 18_000)]),
     K([(320, 18_000)], [(153, 18_000)])],
    "Alıştan iadeler THP’de ayrı bir hesapta izlenmez, stok hesabından düşülür: 153 Ticari Mallar 15.000 ₺ alacak. Alışta "
    "indirilen KDV’nin iadeye isabet eden 3.000 ₺’si 191 İndirilecek KDV hesabına alacak yazılarak düzeltilir.")

# 13 — sipariş avansı mahsubu
av, mal = 20_000, 80_000
P.q(f"{R}: 159, 153, 191, 320",
    f"İşletme şubat ayında vereceği mal siparişi için satıcısına {tl(av)} ₺ avans ödemiş ve bunu kayda almıştır. Mart "
    f"ayında {tl(mal)} ₺ + %20 KDV tutarındaki malların faturasıyla birlikte teslim alınmasıyla avans mahsup edilmiş, kalan "
    "tutarın vadeli ödenmesi kararlaştırılmıştır.\n\nMart ayındaki teslim alma kaydı için aşağıdakilerden hangisi doğrudur?",
    T(159, "alacak", av),
    [T(320, "alacak", mal + mal // 5), T(340, "borç", av), T(153, "borç", mal + mal // 5), T(191, "borç", mal // 5 - av // 5)],
    f"Mallar 153 hesabına {tl(mal)} ₺, KDV 191 hesabına {tl(mal // 5)} ₺ borç yazılır. Verilen avans 159 Verilen Sipariş "
    f"Avansları hesabına {tl(av)} ₺ alacak yazılarak kapatılır, kalan {tl(mal + mal // 5 - av)} ₺ 320 Satıcılar hesabına "
    "alacak kaydedilir.", zorluk="hard")

# 14 — alınan sipariş avansı
P.q(f"{R}: 102, 340",
    "Mobilya üretimi yapan bir işletme, bir otel zincirinden aldığı ve teslimi üç ay sonra yapılacak 300.000 ₺ + KDV "
    "tutarındaki siparişe karşılık, sözleşme gereği sipariş bedelinin %25’i olan 75.000 ₺’yi banka havalesiyle avans "
    f"olarak tahsil etmiştir. Avans için fatura düzenlenmemiştir.\n\n{KAYIT}",
    K([(102, 75_000)], [(340, 75_000)]),
    [K([(102, 75_000)], [(600, 75_000)]),
     K([(102, 75_000)], [(380, 75_000)]),
     K([(159, 75_000)], [(102, 75_000)]),
     K([(102, 75_000)], [(120, 75_000)])],
    "Henüz teslim edilmemiş mal için alınan tutar gelir değil yükümlülüktür; 102 Bankalar borç, 340 Alınan Sipariş "
    "Avansları alacak yazılır. Mal teslim edilip fatura düzenlendiğinde avans mahsup edilir ve satış kaydedilir.")

# 15 — ücret tahakkuku
brut, sgk, iss, gv, dv = 120_000, 16_800, 1_200, 12_600, 910
net = brut - sgk - iss - gv - dv
P.q(f"{R}: 770, 335, 360, 361",
    f"İdari personele ilişkin ocak ayı ücret bordrosunda brüt ücret {tl(brut)} ₺; SGK primi işçi payı {tl(sgk)} ₺, "
    f"işsizlik sigortası işçi payı {tl(iss)} ₺, gelir vergisi {tl(gv)} ₺ ve damga vergisi {tl(dv)} ₺ olarak "
    f"hesaplanmıştır. Ücretler şubat başında ödenecektir.\n\nİşçi payları dikkate alınarak yapılacak ücret tahakkuku "
    "kaydı aşağıdakilerden hangisidir?",
    K([(770, brut)], [(335, net), (360, gv + dv), (361, sgk + iss)]),
    [K([(770, brut)], [(335, net), (361, gv + dv + sgk + iss)]),
     K([(770, brut)], [(102, net), (360, gv + dv), (361, sgk + iss)]),
     K([(720, brut)], [(335, net), (360, gv + dv), (361, sgk + iss)]),
     K([(770, net), (360, gv + dv), (361, sgk + iss)], [(335, brut)])],
    f"Brüt ücret idari personel için 770 Genel Yönetim Giderleri hesabına borç yazılır. Vergiler ({tl(gv + dv)} ₺) 360, "
    f"SGK ve işsizlik işçi payları ({tl(sgk + iss)} ₺) 361 hesabına, net ücret {tl(net)} ₺ 335 Personele Borçlar hesabına "
    "alacak kaydedilir.", zorluk="hard")

# 16 — personel avansının ücretten mahsubu
P.sayisal(f"{R}: 196, 335",
    "Bir çalışana ocak ortasında 5.000 ₺ personel avansı verilmiştir. Ocak sonunda çalışanın net ücreti 32.400 ₺ olarak "
    "tahakkuk ettirilmiş, avansın tamamı ücretinden mahsup edilmiş ve kalan tutar 2 Şubat’ta banka aracılığıyla "
    "çalışanın hesabına gönderilmiştir.\n\n2 Şubat tarihli ödeme kaydında 102 Bankalar hesabına kaç ₺ alacak yazılır?",
    tl(27_400), secenekler(27_400, 32_400, 37_400, 22_400, 30_000),
    "Net ücret 32.400 ₺ ile 335 Personele Borçlar alacaklandırılmıştı. Mahsupta 335 borç, 196 Personel Avansları alacak "
    "5.000 ₺; ödemede 335 borç, 102 alacak 32.400 − 5.000 = 27.400 ₺ yazılır.", zorluk="easy")

# 17 — iş avansının kapatılması
av, gider, kdv = 10_000, 7_000, 1_400
P.q(f"{R}: 195, 770, 191, 100",
    f"Satın alma sorumlusuna fuar ziyaretinde yapılacak harcamalar için {tl(av)} ₺ iş avansı verilmiştir. Sorumlu dönüşte "
    f"idari nitelikli {tl(gider)} ₺ + %20 KDV tutarında faturalı harcama belgesi teslim etmiş ve artan parayı kasaya iade "
    f"etmiştir.\n\n{KAYIT}",
    K([(770, gider), (191, kdv), (100, av - gider - kdv)], [(195, av)]),
    [K([(770, gider + kdv), (100, av - gider - kdv)], [(195, av)]),
     K([(770, gider), (191, kdv), (100, av - gider - kdv)], [(196, av)]),
     K([(195, av)], [(770, gider), (191, kdv), (100, av - gider - kdv)]),
     K([(760, gider), (391, kdv), (100, av - gider - kdv)], [(195, av)])],
    f"Belgelenen gider 770’e {tl(gider)} ₺, indirilebilir KDV 191’e {tl(kdv)} ₺ ve kasaya iade edilen "
    f"{tl(av - gider - kdv)} ₺ 100 Kasa’ya borç yazılır; iş avansı 195 İş Avansları hesabına {tl(av)} ₺ alacak yazılarak "
    "kapatılır.")

# 18 — depozito verilmesi
P.q(f"{R}: 126, 180, 191, 102",
    "İşletme yeni kiraladığı depo için 1 Ekim’de mal sahibine üç aylık kira tutarı olan 45.000 ₺ + %20 KDV’yi peşin "
    "ödemiş, ayrıca sözleşme sonunda iade edilmek üzere 30.000 ₺ güvence bedeli yatırmıştır. Ödemelerin tamamı banka "
    f"havalesiyle yapılmıştır.\n\n{KAYIT}",
    K([(126, 30_000), (180, 45_000), (191, 9_000)], [(102, 84_000)]),
    [K([(326, 30_000), (180, 45_000), (191, 9_000)], [(102, 84_000)]),
     K([(760, 75_000), (191, 9_000)], [(102, 84_000)]),
     K([(126, 30_000), (280, 45_000), (191, 9_000)], [(102, 84_000)]),
     K([(126, 39_000), (180, 45_000)], [(102, 84_000)])],
    "İade edilecek güvence bedeli 126 Verilen Depozito ve Teminatlar hesabına, gelecek üç aya ait kira 180 Gelecek Aylara "
    "Ait Giderler hesabına, KDV 191’e borç yazılır; 102 Bankalar 84.000 ₺ alacaklandırılır. Kira aylar geçtikçe gidere aktarılır.")

# 19 — alınan depozito
P.q(f"{R}: 102, 326",
    "Kiraya verdiği bir dükkân için kiracıdan, sözleşme bitiminde hasar tespiti yapıldıktan sonra iade edilmek üzere "
    "60.000 ₺ güvence bedeli tahsil eden işletme, tutarı vadesiz mevduat hesabına yatırmıştır. Aynı gün kiracıya ayrıca "
    "aylık 20.000 ₺ + KDV kira faturası da kesilmiştir.\n\nGüvence bedelinin tahsili için yapılacak kayıtta alacaklandırılan "
    "hesap aşağıdakilerden hangisidir?",
    hk(326),
    [hk(126), hk(649), hk(380), hk(340)],
    "İade yükümlülüğü taşıyan güvence bedeli gelir değildir; 102 Bankalar borç, 326 Alınan Depozito ve Teminatlar alacak "
    "yazılır. 126 işletmenin verdiği teminatları, 380 ise peşin tahsil edilen gelirleri izler.", zorluk="easy")

# 20 — hisse senedi satışı kârlı
alis, satis = 84_000, 96_500
P.q(f"{R}: 102, 110, 645",
    f"Kısa vadeli fiyat artışından yararlanmak amacıyla borsadan {tl(alis)} ₺’ye satın aldığı ve dönem içinde değerlemeye "
    f"tabi tutmadığı hisse senetlerini, iki ay sonra aracı kurum kanalıyla {tl(satis)} ₺’ye satan işletmenin satış bedeli "
    f"banka hesabına aktarılmıştır.\n\n{KAYIT}",
    K([(102, satis)], [(110, alis), (645, satis - alis)]),
    [K([(102, satis)], [(110, satis)]),
     K([(102, satis)], [(242, alis), (645, satis - alis)]),
     K([(102, satis)], [(110, alis), (679, satis - alis)]),
     K([(102, satis)], [(110, alis), (642, satis - alis)])],
    f"Satılan hisseler maliyetiyle 110 Hisse Senetleri hesabından çıkarılır; satış bedeli ile maliyet arasındaki "
    f"{tl(satis - alis)} ₺ fark 645 Menkul Kıymet Satış Kârları hesabına alacak yazılır. 242 uzun vadeli iştirak paylarını izler.")

# 21 — hisse senedi satışı zararlı, taraf
alis, satis = 55_000, 47_800
P.q(f"{R}: 655",
    f"İşletme alım satım amacıyla elinde tuttuğu ve maliyeti {tl(alis)} ₺ olan hisse senetlerini, piyasanın düşüşe "
    f"geçmesi üzerine {tl(satis)} ₺’ye satmıştır. Satış bedeli aracı kurumun işletme adına açtığı hesaba geçmiş ve aynı gün "
    f"işletmenin banka hesabına aktarılmıştır.\n\n{DOGRU}",
    T(655, "borç", alis - satis),
    [T(110, "alacak", satis), T(689, "borç", alis - satis), T(645, "borç", alis - satis), T(102, "borç", alis)],
    f"110 Hisse Senetleri maliyetiyle {tl(alis)} ₺ alacaklandırılır, banka {tl(satis)} ₺ borçlandırılır; aradaki "
    f"{tl(alis - satis)} ₺ 655 Menkul Kıymet Satış Zararları hesabına borç yazılır.")

# 22 — tahvil faizi, stopajlı
brt, st = 18_000, 1_800
P.q(f"{R}: 102, 193, 642",
    f"İşletmenin kısa vadeli yatırım amacıyla elinde bulundurduğu özel sektör tahvillerinin kupon ödemesi yapılmıştır. "
    f"Brüt faiz tutarı {tl(brt)} ₺ olup üzerinden %10 oranında gelir vergisi tevkifatı yapılmış, kalan {tl(brt - st)} ₺ "
    f"işletmenin banka hesabına yatırılmıştır.\n\n{KAYIT}",
    K([(102, brt - st), (193, st)], [(642, brt)]),
    [K([(102, brt - st)], [(642, brt - st)]),
     K([(102, brt - st), (770, st)], [(642, brt)]),
     K([(102, brt - st), (193, st)], [(111, brt)]),
     K([(102, brt - st), (360, st)], [(642, brt)])],
    f"Faiz geliri brüt {tl(brt)} ₺ olarak 642 Faiz Gelirleri hesabına alacak yazılır. Kesilen {tl(st)} ₺ vergi işletmenin "
    "beyannamesinde mahsup edileceğinden 193 Peşin Ödenen Vergiler ve Fonlar hesabına borç kaydedilir.")

# 23 — iştirakten temettünün tahsili
P.q(f"{R}: 102, 132",
    "İşletme, %30 oranında pay sahibi olduğu şirketin genel kurulunda dağıtılmasına karar verilen kârdan kendisine düşen "
    "42.000 ₺’yi karar tarihinde tahakkuk ettirerek kaydetmiştir. İki hafta sonra bu tutar ortaklık tarafından işletmenin "
    "banka hesabına havale edilmiştir.\n\nHavale tarihinde yapılacak günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(102, 42_000)], [(132, 42_000)]),
    [K([(102, 42_000)], [(640, 42_000)]),
     K([(102, 42_000)], [(133, 42_000)]),
     K([(132, 42_000)], [(640, 42_000)]),
     K([(102, 42_000)], [(242, 42_000)])],
    "Kâr payı karar tarihinde 132 İştiraklerden Alacaklar borç, 640 İştiraklerden Temettü Gelirleri alacak ile gelir "
    "yazılmıştır. Tahsilatta alacak kapatılır: 102 Bankalar borç, 132 alacak. %30 pay iştirak (242) niteliğindedir.")

# 24 — sermaye taahhüdü
P.q(f"{R}: 501, 500",
    "Kuruluş aşamasındaki bir anonim şirketin ortakları 2.000.000 ₺ esas sermayenin tamamını taahhüt etmiştir. Taahhüt "
    "edilen sermayenin %25’i tescilden önce bankaya yatırılmış, kalan kısmın 24 ay içinde ödenmesi kararlaştırılmıştır."
    "\n\nSermaye taahhüdünün kaydında borçlandırılan hesap ve tutar aşağıdakilerden hangisidir?",
    f"{hk(501)} – 2.000.000 ₺",
    [f"{hk(131)} – 1.500.000 ₺", f"{hk(500)} – 2.000.000 ₺", f"{hk(102)} – 500.000 ₺", f"{hk(501)} – 1.500.000 ₺"],
    "Taahhüt anında sermayenin tamamı 500 Sermaye hesabına alacak, 501 Ödenmemiş Sermaye hesabına borç yazılır. Ödenen "
    "500.000 ₺ ayrı kayıtla 102 borç, 501 alacak yazılır; kalan 1.500.000 ₺ 501’de izlenir.", zorluk="easy")

# 25 — ayni sermaye
P.q(f"{R}: 254, 501",
    "Sermaye artırımında 400.000 ₺ taahhütte bulunan bir ortak, taahhüdünü bilirkişice 400.000 ₺ değer biçilen ve "
    "şirket adına tescil edilen bir kamyonet ile yerine getirmiştir. Taahhüt daha önce 501 Ödenmemiş Sermaye ve 500 "
    f"Sermaye hesaplarıyla kayda alınmıştır.\n\n{KAYIT}",
    K([(254, 400_000)], [(501, 400_000)]),
    [K([(254, 400_000)], [(500, 400_000)]),
     K([(254, 400_000)], [(331, 400_000)]),
     K([(501, 400_000)], [(254, 400_000)]),
     K([(255, 400_000)], [(501, 400_000)])],
    "Ayni sermaye ile taahhüt borcu ifa edilir: kamyonet 254 Taşıtlar hesabına borç, ortağın taahhüt borcu 501 Ödenmemiş "
    "Sermaye hesabına alacak yazılır. 500 Sermaye taahhüt kaydında alacaklandırıldığı için yeniden kullanılmaz.")

# 26 — hisse senedi primli ihraç, ödeme
P.q(f"{R}: 102, 501, 520",
    "Sermayesini 500.000 ₺ artırmaya karar veren anonim şirket, 1 ₺ nominal değerli payları 1,40 ₺’den ihraç etmiştir. "
    "Artırım tutarı 501 ve 500 hesaplarıyla kaydedilmiş; payların bedeli ortaklar tarafından tam olarak banka hesabına "
    "yatırılmıştır.\n\nPay bedelinin tahsiline ilişkin günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(102, 700_000)], [(501, 500_000), (520, 200_000)]),
    [K([(102, 700_000)], [(500, 500_000), (520, 200_000)]),
     K([(102, 700_000)], [(501, 700_000)]),
     K([(102, 700_000)], [(501, 500_000), (649, 200_000)]),
     K([(102, 700_000)], [(501, 500_000), (549, 200_000)])],
    "Tahsil edilen 500.000 × 1,40 = 700.000 ₺ bankaya borç yazılır. Nominal kısım 501 Ödenmemiş Sermaye hesabını kapatır; "
    "nominali aşan 200.000 ₺ 520 Hisse Senedi İhraç Primleri hesabına alacak kaydedilir. Prim gelir değildir.", zorluk="hard")

# 27 — kısa vadeli kredi kullanımı ve masraf
P.q(f"{R}: 102, 780, 300",
    "İşletme 6 ay vadeli 500.000 ₺ tutarında rotatif kredi kullanmıştır. Banka kredi tahsis ücreti olarak 2.500 ₺ ile "
    "banka ve sigorta muameleleri vergisi 125 ₺’yi keserek kalan tutarı işletmenin vadesiz hesabına aktarmıştır. Faiz vade "
    f"sonunda anapara ile birlikte ödenecektir.\n\n{KAYIT}",
    K([(102, 497_375), (780, 2_625)], [(300, 500_000)]),
    [K([(102, 497_375), (780, 2_625)], [(400, 500_000)]),
     K([(102, 497_375)], [(300, 497_375)]),
     K([(102, 497_375), (770, 2_625)], [(300, 500_000)]),
     K([(102, 500_000)], [(300, 497_375), (642, 2_625)])],
    "Kredi anaparası 300 Banka Kredileri hesabına 500.000 ₺ alacak yazılır. Kesilen tahsis ücreti ve BSMV (2.625 ₺) "
    "borçlanma maliyeti olarak 780 Finansman Giderleri hesabına, kalan 497.375 ₺ 102 Bankalar hesabına borç kaydedilir.")

# 28 — makine alımı maliyet unsurları
fiyat, nak, mon = 800_000, 24_000, 16_000
mal = fiyat + nak + mon
P.q(f"{R}: 253, 191",
    f"Üretim işletmesi {tl(fiyat)} ₺ + %20 KDV bedelli bir makineyi vadeli satın almıştır. Makinenin fabrikaya taşınması "
    f"için {tl(nak)} ₺ + KDV, kurulumu ve deneme çalıştırması için {tl(mon)} ₺ + KDV peşin ödenmiş; makine kullanıma "
    f"hazır hâle getirilmiştir.\n\nBu işlemler sonucunda {hk(253)} hesabına borç yazılan toplam tutar kaç ₺’dir?",
    tl(mal), [tl(fiyat), tl(fiyat + nak), tl(mal * 12 // 10), tl(fiyat * 12 // 10)],
    f"Maddi duran varlığın maliyeti, kullanıma hazır hâle getirilinceye kadar katlanılan tüm giderleri kapsar: "
    f"{tl(fiyat)} + {tl(nak)} + {tl(mon)} = {tl(mal)} ₺. KDV indirilebildiği için maliyete girmez, 191’de izlenir.")

# 29 — duran varlık satışı kârlı
mal, bir, sat = 300_000, 210_000, 120_000
kdv = sat // 5
kar = sat - (mal - bir)
P.q(f"{R}: 102, 257, 254, 391, 679",
    f"İşletme {tl(mal)} ₺ maliyetli ve satış tarihine kadar {tl(bir)} ₺ birikmiş amortisman ayrılmış ve alışında KDV’si indirilmiş bir kamyoneti "
    f"{tl(sat)} ₺ + %20 KDV bedelle satmış, bedeli banka havalesiyle tahsil etmiştir. Satış kazancı için yenileme fonu "
    f"ayrılmayacaktır.\n\n{KAYIT}",
    K([(102, sat + kdv), (257, bir)], [(254, mal), (391, kdv), (679, kar)]),
    [K([(102, sat + kdv), (257, bir)], [(254, mal), (391, kdv), (649, kar)]),
     K([(102, sat + kdv)], [(254, sat), (391, kdv)]),
     K([(102, sat + kdv), (257, bir)], [(254, mal), (391, kdv), (549, kar)]),
     K([(102, sat + kdv), (257, bir)], [(254, mal), (191, kdv), (679, kar)])],
    f"Net defter değeri {tl(mal)} − {tl(bir)} = {tl(mal - bir)} ₺, satış bedeli {tl(sat)} ₺; kâr {tl(kar)} ₺. Taşıt ve "
    "birikmiş amortisman kapatılır, KDV 391’e, kâr 679 Diğer Olağandışı Gelir ve Kârlar hesabına alacak yazılır.",
    zorluk="hard")

# 30 — duran varlık satışı zararlı (taraf)
mal, bir, sat = 90_000, 54_000, 30_000
P.q(f"{R}: 689",
    f"İşletme, {tl(mal)} ₺ maliyetli ve {tl(bir)} ₺ birikmiş amortismanı bulunan büro mobilyalarını yeni mobilyalar "
    f"almadan önce {tl(sat)} ₺ + %20 KDV bedelle peşin satmıştır. Satış bedelinin tamamı kasaya alınmış ve aynı gün "
    f"bankaya yatırılmıştır.\n\n{DOGRU}",
    T(689, "borç", mal - bir - sat),
    [T(679, "alacak", mal - bir - sat), T(255, "alacak", mal - bir), T(257, "alacak", bir), T(659, "borç", mal - bir - sat)],
    f"Net defter değeri {tl(mal - bir)} ₺, satış bedeli {tl(sat)} ₺ olduğundan {tl(mal - bir - sat)} ₺ zarar oluşur ve 689 "
    f"Diğer Olağandışı Gider ve Zararlar hesabına borç yazılır. 255 {tl(mal)} ₺ alacak, 257 {tl(bir)} ₺ borç kaydedilir.")

# 31 — yapılmakta olan yatırım tamamlanması
P.q(f"{R}: 252, 258",
    "İşletme yıl başında başladığı depo binası inşaatı için yıl içinde müteahhide hak ediş karşılığı toplam 2.400.000 ₺, "
    "proje ve ruhsat giderleri için 160.000 ₺ ödemiş, bu tutarları 258 Yapılmakta Olan Yatırımlar hesabında biriktirmiştir. "
    f"Kasım ayında bina tamamlanarak kullanılmaya başlanmıştır.\n\n{KAYIT}",
    K([(252, 2_560_000)], [(258, 2_560_000)]),
    [K([(252, 2_400_000), (770, 160_000)], [(258, 2_560_000)]),
     K([(258, 2_560_000)], [(252, 2_560_000)]),
     K([(252, 2_560_000)], [(102, 2_560_000)]),
     K([(251, 2_560_000)], [(258, 2_560_000)])],
    "İnşaat süresince biriktirilen tüm maliyet unsurları (hak ediş 2.400.000 ₺ ve proje-ruhsat 160.000 ₺) bina kullanıma "
    "hazır olduğunda 258’den 252 Binalar hesabına aktarılır; amortisman bu tarihten itibaren başlar.")

# 32 — duran varlık için avans (hesap adı)
P.q(f"{R}: 259",
    "İşletme, yurt dışından sipariş ettiği ve teslimi beş ay sonra yapılacak bir üretim hattı için sözleşme bedeli "
    "1.200.000 ₺’nin %30’u olan 360.000 ₺’yi sipariş aşamasında satıcıya havale etmiştir. Hat teslim alındığında avans "
    "bedelden düşülecektir.\n\nHavale edilen tutar aşağıdaki hesaplardan hangisine borç yazılır?",
    hk(259), [hk(159), hk(253), hk(258), hk(126)],
    "Maddi duran varlık alımı için verilen avanslar 259 Verilen Avanslar hesabında izlenir; 159 stok alımına ilişkin sipariş "
    "avanslarını izler. Varlık teslim alınınca avans 253’e mahsup edilir.", zorluk="easy")

# 33 — peşin tahsil edilen kira (380)
P.q(f"{R}: 102, 380, 391",
    "Kullanmadığı depo bölümünü kiraya veren işletme, 1 Kasım’da kiracıdan dört aylık kira bedeli olan 40.000 ₺ + %20 "
    "KDV’yi peşin tahsil ederek banka hesabına almış ve faturasını düzenlemiştir. İşletme hesap dönemi takvim yılıdır ve "
    "dönem içi kayıtlarda tahsil edilen kirayı ilk aşamada gelecek dönem geliri olarak izlemektedir.\n\n"
    f"{KAYIT}",
    K([(102, 48_000)], [(380, 40_000), (391, 8_000)]),
    [K([(102, 48_000)], [(480, 40_000), (391, 8_000)]),
     K([(102, 48_000)], [(649, 40_000), (391, 8_000)]),
     K([(102, 48_000)], [(380, 48_000)]),
     K([(102, 48_000)], [(181, 40_000), (391, 8_000)])],
    "Peşin tahsil edilen ve izleyen aylara ait kira 380 Gelecek Aylara Ait Gelirler hesabına alacak yazılır; KDV fatura "
    "düzenlendiği için 391’e aktarılır. Kasım ve aralık payları ay sonlarında 649 hesabına aktarılır.")

# 34 — KDV mahsubu
hes, ind = 185_000, 142_000
P.q(f"{R}: 391, 191, 360",
    f"Ekim ayı sonunda işletmenin 391 Hesaplanan KDV hesabının bakiyesi {tl(hes)} ₺, 191 İndirilecek KDV hesabının "
    f"bakiyesi {tl(ind)} ₺’dir. Önceki aydan devreden KDV bulunmamaktadır ve ay içinde KDV tevkifatlı bir işlem "
    "yapılmamıştır.\n\nBeyanname dönemi sonunda yapılacak mahsup kaydı aşağıdakilerden hangisidir?",
    K([(391, hes)], [(191, ind), (360, hes - ind)]),
    [K([(191, ind), (360, hes - ind)], [(391, hes)]),
     K([(391, hes)], [(191, ind), (190, hes - ind)]),
     K([(391, ind)], [(191, ind)]),
     K([(391, hes)], [(191, ind), (193, hes - ind)])],
    f"Hesaplanan KDV indirilecek KDV’den {tl(hes - ind)} ₺ fazladır. 391 borçlandırılarak, 191 alacaklandırılarak kapatılır; "
    "fark ödenecek vergi olarak 360 Ödenecek Vergi ve Fonlar hesabına alacak yazılır. 190 ters durumda kullanılır.")

# 35 — ihracat
P.q(f"{R}: 120, 601",
    "Tekstil ürünleri satan işletme, Almanya’daki bir müşterisine fatura bedeli 20.000 avro olan malları vadeli olarak "
    "ihraç etmiştir. Fiilî ihracat tarihinde avronun Türk lirası karşılığı 38 ₺’dir; alacak bu kurla kayda alınacak ve "
    "tahsilatta oluşacak kur farkı ayrıca izlenecektir. İhracat KDV’den istisnadır.\n\n"
    f"{KAYIT}",
    K([(120, 760_000)], [(601, 760_000)]),
    [K([(102, 760_000)], [(601, 760_000)]),
     K([(120, 760_000)], [(600, 760_000)]),
     K([(120, 912_000)], [(601, 760_000), (391, 152_000)]),
     K([(120, 760_000)], [(649, 760_000)])],
    "Dövizli satış işlem tarihindeki kurla ölçülür: 20.000 × 38 = 760.000 ₺. Bedel vadeli olduğundan 120 Alıcılar "
    "borçlandırılır; yurt dışı satışlar 601 hesabında izlenir ve istisna nedeniyle 391’e tutar aktarılmaz.")

# 36 — ithalat maliyeti
cif, gv = 400_000, 40_000
kdv = (cif + gv) // 5
P.q(f"{R}: 153, 191",
    f"İşletme ticari mal ithal etmiştir. Malların gümrük kıymeti {tl(cif)} ₺ olup bu tutar üzerinden %10 gümrük vergisi "
    f"({tl(gv)} ₺) ve (gümrük kıymeti + gümrük vergisi) üzerinden %20 KDV ödenmiştir. Satıcıya olan döviz borcu henüz "
    f"ödenmemiştir.\n\n{DOGRU}",
    T(153, "borç", cif + gv),
    [T(153, "borç", cif), T(191, "borç", cif // 5), T(770, "borç", gv), T(153, "borç", cif + gv + kdv)],
    f"Gümrük vergisi malın maliyetine eklenir: 153 Ticari Mallar {tl(cif)} + {tl(gv)} = {tl(cif + gv)} ₺ borç. KDV "
    f"({tl(cif + gv)} × %20 = {tl(kdv)} ₺) indirilebildiği için 191 İndirilecek KDV hesabına borç yazılır.", zorluk="hard")

# 37 — ortağın şahsi harcaması
P.q(f"{R}: 131, 100",
    "Limited şirket ortaklarından biri, yurt dışı tatili için şirket kasasından 35.000 ₺ almış ve bu tutarı üç ay içinde "
    "iade edeceğini belirten bir belge imzalamıştır. Harcama şirketin faaliyetiyle ilgili değildir ve kâr payı avansı "
    f"olarak verilmemiştir.\n\n{KAYIT}",
    K([(131, 35_000)], [(100, 35_000)]),
    [K([(770, 35_000)], [(100, 35_000)]),
     K([(331, 35_000)], [(100, 35_000)]),
     K([(196, 35_000)], [(100, 35_000)]),
     K([(580, 35_000)], [(100, 35_000)])],
    "Ortağın şirketten kişisel amaçla aldığı ve iade edeceği tutar şirketin ortaktan alacağıdır; 131 Ortaklardan Alacaklar "
    "borç, 100 Kasa alacak yazılır. İşletme kişiliği kavramı gereği gider yazılamaz.", zorluk="easy")

# 38 — ortaktan borç alma
P.q(f"{R}: 102, 331",
    "Nakit sıkıntısı yaşayan anonim şirkete, yönetim kurulu üyesi olmayan bir pay sahibi altı ay sonra geri ödenmek üzere "
    "300.000 ₺ borç vermiş ve tutarı şirketin banka hesabına havale etmiştir. Borç için senet düzenlenmemiş, faiz "
    "işletilmeyeceği kararlaştırılmıştır.\n\nBu işlemde alacaklandırılan hesap aşağıdakilerden hangisidir?",
    hk(331), [hk(131), hk(405), hk(520), hk(336)],
    "Şirketin ortaklarına olan ticari olmayan borçları 331 Ortaklara Borçlar hesabında izlenir; kayıt 102 Bankalar borç, "
    "331 alacak şeklindedir. Tutar sermaye artışı veya ihraç edilmiş menkul kıymet olmadığından 520 ya da 405’e yazılamaz.", zorluk="easy")

# 39 — dövizli alacak tahsili, kambiyo kârı
kur1, kur2, usd = 40, 41.5, 10_000
P.q(f"{R}: 102, 120, 646",
    f"İşletme, 1 Eylül’de 10.000 ABD doları tutarında vadeli ihracat yapmış ve alacağı o tarihteki {kur1} ₺ kurundan "
    f"kaydetmiştir. Alacak 20 Eylül’de tahsil edilmiş, dövizler işletmenin döviz tevdiat hesabına aktarılmıştır; tahsil "
    f"tarihinde kur {tl(kur2)} ₺’dir.\n\n{KAYIT}",
    K([(102, usd * kur2)], [(120, usd * kur1), (646, usd * (kur2 - kur1))]),
    [K([(102, usd * kur2)], [(120, usd * kur2)]),
     K([(102, usd * kur2)], [(120, usd * kur1), (642, usd * (kur2 - kur1))]),
     K([(102, usd * kur1), (656, usd * (kur2 - kur1))], [(120, usd * kur2)]),
     K([(102, usd * kur2)], [(601, usd * kur1), (646, usd * (kur2 - kur1))])],
    f"Alacak {tl(usd * kur1)} ₺ ile kayıtlıdır; tahsil edilen dövizin karşılığı {tl(usd * kur2)} ₺’dir. Aradaki "
    f"{tl(usd * (kur2 - kur1))} ₺ kur artışı 646 Kambiyo Kârları hesabına alacak yazılır.")

# 40 — kredi kartıyla satış
P.q(f"{R}: 108, 600, 391",
    "Perakende mağazası gün içinde müşterilerine 25.000 ₺ + %20 KDV tutarında mal satmış ve bedelin tamamı müşterilerin "
    "kredi kartlarıyla tahsil edilmiştir. Anlaşmalı banka tutarı 30 gün sonra işletmenin hesabına aktaracaktır.\n\n"
    f"{KAYIT}",
    K([(108, 30_000)], [(600, 25_000), (391, 5_000)]),
    [K([(102, 30_000)], [(600, 25_000), (391, 5_000)]),
     K([(120, 30_000)], [(600, 25_000), (391, 5_000)]),
     K([(108, 30_000)], [(600, 30_000)]),
     K([(101, 30_000)], [(600, 25_000), (391, 5_000)])],
    "Kredi kartıyla yapılan satışlardan bankadan alınacak tutarlar 108 Diğer Hazır Değerler hesabında izlenir; satış 600, "
    "KDV 391 hesabına alacak yazılır. Tutar hesaba geçtiğinde 102 borç, 108 alacak kaydedilir.")

# 41 — mal alış fiyat farkı
P.q(f"{R}: 153, 191, 320",
    "İşletme geçen ay satın aldığı ticari mallar için satıcıdan, sözleşmedeki hammadde endeksi maddesi uyarınca "
    "düzenlenmiş 6.000 ₺ + %20 KDV tutarında fiyat farkı faturası almıştır. Mallar henüz satılmamış olup ambarda "
    f"bulunmaktadır ve tutar vadeli ödenecektir.\n\n{KAYIT}",
    K([(153, 6_000), (191, 1_200)], [(320, 7_200)]),
    [K([(621, 6_000), (191, 1_200)], [(320, 7_200)]),
     K([(780, 6_000), (191, 1_200)], [(320, 7_200)]),
     K([(153, 7_200)], [(320, 7_200)]),
     K([(153, 6_000), (391, 1_200)], [(320, 7_200)])],
    "Satın alınan mala ilişkin sonradan gelen fiyat farkı, mal henüz satılmadığı için stok maliyetine eklenir: 153 borç "
    "6.000 ₺, 191 borç 1.200 ₺, 320 Satıcılar alacak 7.200 ₺.")

# 42 — serbest meslek hizmeti, stopaj
brut, st, kdv = 30_000, 6_000, 6_000
P.q(f"{R}: 770, 191, 360, 102",
    f"İşletme, hukuk danışmanlığı aldığı serbest avukattan {tl(brut)} ₺ brüt ücret ve %20 KDV içeren serbest meslek "
    f"makbuzu almıştır. Ücret üzerinden %20 gelir vergisi tevkifatı ({tl(st)} ₺) yapılmış, KDV tevkifatı uygulanmamış ve "
    f"kalan tutar avukatın hesabına havale edilmiştir.\n\n{KAYIT}",
    K([(770, brut), (191, kdv)], [(360, st), (102, brut + kdv - st)]),
    [K([(770, brut), (191, kdv)], [(193, st), (102, brut + kdv - st)]),
     K([(770, brut + kdv)], [(360, st), (102, brut)]),
     K([(770, brut - st), (191, kdv)], [(102, brut + kdv - st)]),
     K([(770, brut), (191, kdv)], [(361, st), (102, brut + kdv - st)])],
    f"Brüt ücret 770’e, KDV 191’e borç yazılır. Kesilen {tl(st)} ₺ vergi işletme tarafından vergi dairesine ödeneceği için "
    f"360 Ödenecek Vergi ve Fonlar hesabına alacak kaydedilir; avukata {tl(brut + kdv - st)} ₺ ödenir.")

# 43 — karşılıksız çek
P.q(f"{R}: 128, 101",
    "Müşteriden alınan ve bankaya tahsile verilen 48.000 ₺’lik çek, keşidecinin hesabında karşılık bulunmadığı için "
    "banka tarafından karşılıksız işlemi yapılarak işletmeye iade edilmiştir. İşletme alacağı için icra takibi başlatmaya "
    f"karar vermiştir.\n\n{KAYIT}",
    K([(128, 48_000)], [(101, 48_000)]),
    [K([(120, 48_000)], [(101, 48_000)]),
     K([(689, 48_000)], [(101, 48_000)]),
     K([(128, 48_000)], [(102, 48_000)]),
     K([(654, 48_000)], [(129, 48_000)])],
    "Karşılıksız çıkan ve takibe alınan çek, şüpheli hâle gelen alacak olarak 101 Alınan Çekler hesabından 128 Şüpheli "
    "Ticari Alacaklar hesabına aktarılır. Karşılık gideri ise dönem sonunda değerlemede ayrılır.")

# 44 — alınan çekin ciro edilmesi
P.q(f"{R}: 320, 101",
    "İşletme, müşterisinden aldığı 22.000 ₺ tutarlı ve henüz vadesi gelmemiş bir çeki, 30.000 ₺ olan satıcı borcuna "
    "karşılık ciro ederek satıcıya vermiştir. Kalan borç için aynı gün kendi banka hesabına çekilmiş 8.000 ₺ tutarlı bir "
    f"çek düzenlenmiştir.\n\n{KAYIT}",
    K([(320, 30_000)], [(101, 22_000), (103, 8_000)]),
    [K([(320, 30_000)], [(103, 30_000)]),
     K([(320, 30_000)], [(101, 22_000), (102, 8_000)]),
     K([(320, 30_000)], [(101, 30_000)]),
     K([(321, 30_000)], [(101, 22_000), (103, 8_000)])],
    "Ciro edilen müşteri çeki 101 Alınan Çekler hesabından çıkar (22.000 ₺ alacak), işletmenin kendi düzenlediği çek 103 "
    "Verilen Çekler ve Ödeme Emirleri hesabına 8.000 ₺ alacak yazılır; 320 Satıcılar 30.000 ₺ borçlandırılır.")

# 45 — SGK primlerinin ödenmesi
P.q(f"{R}: 361, 102",
    "Mart ayı bordrosunda tahakkuk ettirilen 27.600 ₺ işçi payı ve 32.400 ₺ işveren payından oluşan sosyal güvenlik "
    "kesintileri, yasal süresi içinde Sosyal Güvenlik Kurumuna işletmenin banka hesabından ödenmiştir. İşveren payı "
    f"tahakkuk tarihinde gidere yazılmıştır.\n\n{KAYIT}",
    K([(361, 60_000)], [(102, 60_000)]),
    [K([(361, 27_600), (770, 32_400)], [(102, 60_000)]),
     K([(360, 60_000)], [(102, 60_000)]),
     K([(335, 60_000)], [(102, 60_000)]),
     K([(361, 27_600)], [(102, 27_600)])],
    "Hem işçi hem işveren payı tahakkuk tarihinde 361 Ödenecek Sosyal Güvenlik Kesintileri hesabına alacak yazılmıştır. "
    "Ödemede 361 hesabı 60.000 ₺ borçlandırılır, 102 Bankalar alacaklandırılır.", zorluk="easy")

# 46 — sürekli envanter satış maliyeti
sat, mal = 150_000, 96_000
P.q(f"{R}: 621, 153",
    f"Sürekli envanter yöntemini uygulayan işletme, stok kartlarında maliyeti {tl(mal)} ₺ görünen malları "
    f"{tl(sat)} ₺ + %20 KDV bedelle vadeli satmıştır. Satış faturası kaydedilmiş; stok kartı yöntemine göre satılan malın "
    "maliyetinin de aynı tarihte kayda alınması gerekmektedir.\n\nMaliyet kaydı aşağıdakilerden hangisidir?",
    K([(621, mal)], [(153, mal)]),
    [K([(153, mal)], [(621, mal)]),
     K([(621, sat)], [(153, sat)]),
     K([(620, mal)], [(152, mal)]),
     K([(621, mal)], [(600, mal)])],
    f"Sürekli envanterde her satışta satılan malın maliyeti 621 Satılan Ticari Mallar Maliyeti hesabına borç, 153 Ticari "
    f"Mallar hesabına alacak yazılır; tutar satış fiyatı değil maliyettir ({tl(mal)} ₺).", zorluk="easy")

# 47 — borç senedinin vadesinde ödenmesi (taraf)
P.q(f"{R}: 321, 102",
    "İşletme, satıcısına ticari mal alımı karşılığında verdiği 45.000 ₺ nominal değerli borç senedini vadesinde banka "
    "havalesiyle ödemiştir. Önceki dönem sonunda bu senet için 1.800 ₺ reeskont ayrılmış ve yeni dönem başında reeskont "
    f"kaydı ters kayıtla kapatılmıştır.\n\n{DOGRU}",
    T(321, "borç", 45_000),
    [T(322, "borç", 1_800), T(321, "borç", 43_200), T(657, "borç", 1_800), T(320, "borç", 45_000)],
    "Dönem başında reeskont ters kayıtla kapatıldığından senet nominal değeriyle izlenir. Ödemede 321 Borç Senetleri "
    "45.000 ₺ borç, 102 Bankalar 45.000 ₺ alacak yazılır.")

# 48 — mevduat faizi
brt, st = 25_000, 3_750
P.q(f"{R}: 102, 193, 642",
    f"İşletmenin 32 gün vadeli mevduat hesabı vade sonunda yenilenmemiştir. Banka {tl(brt)} ₺ brüt faizi, "
    f"{tl(st)} ₺ gelir vergisi kesintisi yaptıktan sonra anaparayla birlikte işletmenin vadesiz hesabına aktarmıştır; "
    f"kesinti oranı soruda verilen tutarla sınırlıdır.\n\n{DOGRU}",
    T(642, "alacak", brt),
    [T(193, "alacak", st), T(360, "alacak", st), T(770, "borç", st), T(649, "alacak", brt)],
    f"Faiz geliri brüt tutarla 642 Faiz Gelirleri hesabına alacak yazılır ({tl(brt)} ₺). Kesilen {tl(st)} ₺ 193 Peşin "
    f"Ödenen Vergiler ve Fonlar hesabına, net {tl(brt - st)} ₺ 102’ye borç kaydedilir.")

# 49 — hizmet satışı hesabı
P.q(f"{R}: 600",
    "Ana faaliyet konusu muhasebe yazılımı kurulumu ve eğitimi olan bir işletme, bir müşterisine verdiği iki günlük "
    "kurulum hizmeti için 18.000 ₺ + %20 KDV fatura düzenlemiş, bedelin 30 gün sonra ödenmesi kararlaştırılmıştır. "
    "Hizmet faturada belirtilen tarihte tamamlanmıştır.\n\nHizmet bedeli aşağıdaki hesaplardan hangisine alacak yazılır?",
    hk(600), [hk(649), hk(643), hk(380), hk(740)],
    "Esas faaliyet konusu olan hizmetin bedeli hasılattır ve 600 Yurt İçi Satışlar hesabına alacak yazılır; 649 ve 643 esas "
    "faaliyet dışı gelirleri, 740 hizmet üretim maliyetini izler.", zorluk="easy")

# 50 — kasadaki fazlalık (taraf)
P.q(f"{R}: 100, 397",
    "Dönem içinde yapılan ani kasa sayımında kasada 42.300 ₺ bulunmuş, kasa defterindeki kayıtlı bakiye 41.500 ₺ olarak "
    "belirlenmiştir. Fazlalığın bir tahsilatın kaydedilmemesinden kaynaklanıp kaynaklanmadığı araştırılmaktadır ve "
    f"tutarın kime ait olduğu henüz bilinmemektedir.\n\n{DOGRU}",
    T(397, "alacak", 800),
    [T(679, "alacak", 800), T(197, "alacak", 800), T(100, "alacak", 800), T(649, "alacak", 800)],
    "Fiilî mevcut kayıtlı bakiyeden 800 ₺ fazladır. Nedeni belirleninceye kadar 100 Kasa borç, 397 Sayım ve Tesellüm "
    "Fazlaları alacak yazılır; neden bulunamazsa dönem sonunda 679 hesabına aktarılır.")

# 51 — peşin mal alımı, kullanılmayan hesap (olumsuz)
liste, isk = 50_000, 2_000
net = liste - isk
P.q(f"{R}: 153, 191, 100, 102",
    f"İşletme liste fiyatı {tl(liste)} ₺ olan ticari malları fatura üzerinde gösterilen %4 miktar iskontosuyla ve %20 KDV "
    f"ile satın almıştır. Fatura bedelinin yarısı kasadan, yarısı banka havalesiyle ödenmiş; alıcıya ait 2.000 ₺ + KDV "
    "taşıma gideri de nakliyeciye kasadan ödenmiştir.\n\nBu işlemlerin kaydında aşağıdaki hesaplardan hangisi kullanılmaz?",
    hk(611), [hk(153), hk(191), hk(100), hk(102)],
    f"Fatura üzerindeki iskonto ayrı hesapta izlenmez, mal net bedelle ({tl(net)} ₺) 153’e alınır; taşıma gideri de 153’e "
    "eklenir, KDV’ler 191’e yazılır, ödemeler 100 ve 102’den yapılır. 611 satıcının verdiği satış iskontolarını izler.",
    zorluk="medium")

# 52 — senetli satış (taraf)
P.q(f"{R}: 121, 600, 391",
    "İşletme bir müşterisine 70.000 ₺ + %20 KDV tutarında ticari mal satmış; müşteri bedelin tamamı için 60 gün vadeli "
    "ve 84.000 ₺ nominal değerli bir bono düzenleyerek işletmeye vermiştir. Satış faturası aynı gün düzenlenmiş, vade "
    f"farkı alınmamıştır.\n\n{DOGRU}",
    T(121, "borç", 84_000),
    [T(120, "borç", 84_000), T(101, "borç", 84_000), T(121, "borç", 70_000), T(391, "borç", 14_000)],
    "Müşteriden alınan bono 121 Alacak Senetleri hesabına nominal değeri 84.000 ₺ ile borç yazılır; satış 600’e 70.000 ₺, "
    "KDV 391’e 14.000 ₺ alacak kaydedilir. Çek 101’de, senetsiz alacak 120’de izlenir.")

# 53 — kredi taksit ve faiz ödemesi
P.q(f"{R}: 300, 780, 102",
    "İşletme bir yıl vadeli, aylık eşit anapara taksitli ticari kredinin mart ayı taksiti olarak bankaya 50.000 ₺ anapara "
    "ve 12.400 ₺ faiz ödemiştir. Faiz için ay sonuna kadar tahakkuk kaydı yapılmamıştır; ödeme vadesiz hesaptan "
    f"talimat üzerine gerçekleşmiştir.\n\n{KAYIT}",
    K([(300, 50_000), (780, 12_400)], [(102, 62_400)]),
    [K([(300, 62_400)], [(102, 62_400)]),
     K([(400, 50_000), (780, 12_400)], [(102, 62_400)]),
     K([(300, 50_000), (381, 12_400)], [(102, 62_400)]),
     K([(300, 50_000), (660, 12_400)], [(102, 62_400)])],
    "Anapara taksidi kısa vadeli kredi borcunu azaltır: 300 Banka Kredileri 50.000 ₺ borç. Faiz tahakkuk ettirilmediği için "
    "doğrudan 780 Finansman Giderleri hesabına 12.400 ₺ borç yazılır; 102 toplam 62.400 ₺ alacaklandırılır.")

# 54 — tahvil ihracı
P.q(f"{R}: 102, 780, 405",
    "Anonim şirket, Sermaye Piyasası Kurulu onayıyla dört yıl vadeli, yıllık faiz ödemeli ve 2.000.000 ₺ nominal değerli "
    "tahvilleri nominal değerinden ihraç etmiştir. Aracı kurum 30.000 ₺ ihraç komisyonunu keserek kalan tutarı işletmenin "
    "hesabına aktarmıştır; işletme ihraç giderlerini dönem gideri olarak izlemektedir.\n\n"
    f"{KAYIT}",
    K([(102, 1_970_000), (780, 30_000)], [(405, 2_000_000)]),
    [K([(102, 1_970_000), (780, 30_000)], [(305, 2_000_000)]),
     K([(102, 1_970_000)], [(405, 1_970_000)]),
     K([(102, 1_970_000), (653, 30_000)], [(400, 2_000_000)]),
     K([(102, 2_000_000)], [(405, 1_970_000), (643, 30_000)])],
    "Bir yıldan uzun vadeli tahviller 405 Çıkarılmış Tahviller hesabında nominal değerle (2.000.000 ₺) izlenir. Kesilen "
    "30.000 ₺ komisyon 780 Finansman Giderleri hesabına, net tutar 102 Bankalar hesabına borç yazılır.")

# 55 — gerçek kişiden kira, stopaj
brut, st = 50_000, 10_000
P.q(f"{R}: 770, 360, 102",
    f"İşletme merkez ofisini bir gerçek kişiden kiralamıştır. Ocak ayı brüt kira bedeli {tl(brut)} ₺ olup kira "
    f"sözleşmesi gereği %20 oranında gelir vergisi tevkifatı yapılmış ({tl(st)} ₺), KDV hesaplanmamış ve net kira mal "
    f"sahibinin banka hesabına havale edilmiştir.\n\n{KAYIT}",
    K([(770, brut)], [(360, st), (102, brut - st)]),
    [K([(770, brut - st)], [(102, brut - st)]),
     K([(770, brut)], [(193, st), (102, brut - st)]),
     K([(770, brut), (191, st)], [(102, brut + st)]),
     K([(760, brut)], [(360, st), (102, brut - st)])],
    f"İdari ofis kirası brüt tutarla 770 Genel Yönetim Giderleri hesabına borç yazılır. İşletme vergi sorumlusu olarak "
    f"kestiği {tl(st)} ₺’yi 360 Ödenecek Vergi ve Fonlar hesabına, ödediği {tl(brut - st)} ₺’yi 102 hesabına alacak yazar.")

# 56 — reklam gideri (hesap)
P.q(f"{R}: 760",
    "Ev tekstili satan işletme, yeni sezon ürünlerinin tanıtımı için bir ajansla anlaşarak sosyal medya reklam "
    "kampanyası düzenletmiştir. Ajans kampanya tamamlandıktan sonra 40.000 ₺ + %20 KDV fatura düzenlemiş, tutarın 15 gün "
    "sonra ödenmesi kararlaştırılmıştır.\n\nFatura tutarının KDV hariç kısmı aşağıdaki hesaplardan hangisine borç yazılır?",
    hk(760), [hk(770), hk(730), hk(180), hk(740)],
    "Satış ve tanıtım amaçlı reklam harcamaları faaliyet gideridir ve 760 Pazarlama, Satış ve Dağıtım Giderleri hesabına "
    "borç yazılır. 770 yönetim, 730 üretim giderlerini, 740 hizmet üretim maliyetini izler.", zorluk="easy")

# 57 — erken ödeme iskontosu
borc, isk, kdv = 60_000, 1_000, 200
P.q(f"{R}: 320, 153, 191, 102",
    f"İşletme satıcısına olan {tl(borc)} ₺ borcunu vadesinden 45 gün önce ödemeyi teklif etmiş; satıcı da bu nedenle "
    f"{tl(isk)} ₺ + %20 KDV tutarında iskonto faturası düzenlemiştir. İskontoya konu mallar henüz satılmamıştır ve kalan "
    f"tutar aynı gün bankadan ödenmiştir.\n\n{KAYIT}",
    K([(320, borc)], [(153, isk), (191, kdv), (102, borc - isk - kdv)]),
    [K([(320, borc)], [(642, isk), (191, kdv), (102, borc - isk - kdv)]),
     K([(320, borc)], [(611, isk), (391, kdv), (102, borc - isk - kdv)]),
     K([(320, borc)], [(153, isk + kdv), (102, borc - isk - kdv)]),
     K([(320, borc)], [(649, isk), (191, kdv), (102, borc - isk - kdv)])],
    f"Alınan iskonto satın alınan malın maliyetini düşürür (mallar ambarda olduğundan 153 alacak {tl(isk)} ₺); alışta "
    f"indirilen KDV de {tl(kdv)} ₺ azalır (191 alacak). Borç {tl(borc)} ₺ kapanır, bankadan {tl(borc - isk - kdv)} ₺ ödenir.",
    zorluk="hard")

# 58 — dövizli borç ödemesi, kambiyo zararı
usd, k1, k2 = 5_000, 40, 41
P.q(f"{R}: 320, 656, 102",
    f"İşletme ithal ettiği mallar için yurt dışındaki satıcısına olan 5.000 ABD doları tutarındaki borcunu, işlem "
    f"tarihinde dolar kuru {k1} ₺ iken kayda almıştır. Borç, kurun {k2} ₺ olduğu tarihte işletmenin Türk lirası "
    f"hesabından döviz alınarak ödenmiştir.\n\n{KAYIT}",
    K([(320, usd * k1), (656, usd * (k2 - k1))], [(102, usd * k2)]),
    [K([(320, usd * k2)], [(102, usd * k2)]),
     K([(320, usd * k1), (780, usd * (k2 - k1))], [(102, usd * k2)]),
     K([(320, usd * k1), (656, usd * (k2 - k1))], [(100, usd * k2)]),
     K([(320, usd * k2)], [(102, usd * k1), (646, usd * (k2 - k1))])],
    f"Borç {tl(usd * k1)} ₺ ile kayıtlıdır; ödeme için {tl(usd * k2)} ₺ çıkmıştır. Kur artışından doğan "
    f"{tl(usd * (k2 - k1))} ₺ 656 Kambiyo Zararları hesabına borç yazılır; 320 kayıtlı tutarıyla kapatılır.")

# 59 — esas faaliyet dışı kira geliri (taraf)
P.q(f"{R}: 649",
    "Hırdavat ticaretiyle uğraşan işletme, kullanmadığı ikinci katını bir sigorta acentesine kiralamıştır. Ağustos ayı "
    "kira bedeli olan 30.000 ₺ + %20 KDV için ay sonunda fatura düzenlenmiş ve bedel aynı gün kiracı tarafından işletmenin "
    f"banka hesabına yatırılmıştır.\n\n{DOGRU}",
    T(649, "alacak", 30_000),
    [T(600, "alacak", 30_000), T(380, "alacak", 30_000), T(642, "alacak", 30_000), T(649, "alacak", 36_000)],
    "Esas faaliyet konusu dışındaki kira geliri 649 Diğer Olağan Gelir ve Kârlar hesabına KDV hariç 30.000 ₺ alacak "
    "yazılır; 6.000 ₺ KDV 391’e, 36.000 ₺ 102 Bankalar hesabına kaydedilir.")

# 60 — müşterinin borcunu çekle ödemesi (hesap tarafı)
P.q(f"{R}: 101, 120",
    "Önceki ay 96.000 ₺ tutarında vadeli mal satılan müşteri, borcunun 60.000 ₺’lik kısmı için bir hafta sonra ödenecek "
    "şekilde düzenlenmiş kendi çekini vermiş, kalan 36.000 ₺’yi aynı gün kasaya nakit olarak ödemiştir. Çek henüz bankaya "
    f"ibraz edilmemiştir.\n\n{DOGRU}",
    T(101, "borç", 60_000),
    [T(103, "borç", 60_000), T(121, "borç", 60_000), T(127, "borç", 60_000), T(128, "borç", 60_000)],
    "Müşteriden alınan çek 101 Alınan Çekler hesabına 60.000 ₺, nakit 100 Kasa hesabına 36.000 ₺ borç yazılır; müşteri "
    "alacağı 120 Alıcılar hesabına 96.000 ₺ alacak kaydedilerek kapatılır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
