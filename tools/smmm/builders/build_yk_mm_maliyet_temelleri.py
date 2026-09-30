# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi · Maliyet Temelleri — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında Maliyet Muhasebesi soruları uzun, tutar ya da tablo veren kökle
gelir (medyan kök ~308 karakter); soruların üçte biri kadarı sadece sayısal şıklıdır, bir kısmı
"107.750; 31.000" gibi birden çok tutarı birlikte sorar. Kavram soruları azdır ve olumsuz köklüdür.

Dayanak: MSUGT (Tekdüzen Hesap Planı 7/A ve 7/B seçenekleri, 62 Satışların Maliyeti grubu) ve maliyet
muhasebesinin genel kabul görmüş kavramları (ilk madde, dönüşüm, sabit/değişken/karma maliyet, en
yüksek-en düşük yöntemi, tam ve değişken maliyetleme, kapasite kavramları). Tutarlar builder içinde
hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K

P = Paket("questions_topic_maliyet_temelleri_2026.json", lesson="maliyet_muhasebesi", topic="maliyet_temelleri",
          konu_adi="Maliyet Temelleri", seed=2026093081,
          surum="MSUGT Tekdüzen Hesap Planı 7/A-7/B; maliyet muhasebesi genel kavramları; 30.09.2026 kontrolü")

R = "Maliyet muhasebesi kavramları"
R7 = "MSUGT 7/A ve 7/B seçenekleri"

# 1 — ilk madde ve dönüşüm maliyeti
dimm, dis, gug = 214_000, 96_000, 138_000
P.q(R,
    f"Metal eşya üreten bir işletmede mart ayında direkt ilk madde ve malzeme giderleri {tl(dimm)} ₺, direkt işçilik "
    f"giderleri {tl(dis)} ₺ ve genel üretim giderleri {tl(gug)} ₺ olarak gerçekleşmiştir. Aynı ay pazarlama giderleri "
    "45.000 ₺, genel yönetim giderleri 60.000 ₺’dir.\n\nİşletmenin mart ayı ilk (asal) maliyeti ve dönüşüm "
    "(şekillendirme) maliyeti sırasıyla kaç ₺’dir?",
    f"{tl(dimm + dis)}; {tl(dis + gug)}",
    [f"{tl(dimm)}; {tl(dis)}", f"{tl(dimm + dis)}; {tl(dimm + dis + gug)}", f"{tl(dimm + gug)}; {tl(dis + gug)}",
     f"{tl(dimm + dis + gug)}; {tl(dis + gug + 105_000)}"],
    f"İlk (asal) maliyet = DİMM + DİŞ = {tl(dimm)} + {tl(dis)} = {tl(dimm + dis)} ₺; dönüşüm maliyeti = DİŞ + GÜG = "
    f"{tl(dis)} + {tl(gug)} = {tl(dis + gug)} ₺. Pazarlama ve yönetim giderleri dönem gideridir.", zorluk="easy")

# 2 — dönemde üretilen mamul maliyeti (tablo)
ddb, dal, dds, dis2, gug2, ydb, yds = 20_000, 180_000, 30_000, 90_000, 60_000, 25_000, 35_000
kul = ddb + dal - dds
dum = kul + dis2 + gug2
mum = dum + ydb - yds
P.sayisal(R,
    "Bir mobilya üreticisinin yıllık verileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n"
    f"| İlk madde dönem başı stoku | {tl(ddb)} |\n| Dönem içi ilk madde alışları | {tl(dal)} |\n"
    f"| İlk madde dönem sonu stoku | {tl(dds)} |\n| Direkt işçilik | {tl(dis2)} |\n| Genel üretim giderleri | {tl(gug2)} |\n"
    f"| Yarı mamul dönem başı stoku | {tl(ydb)} |\n| Yarı mamul dönem sonu stoku | {tl(yds)} |\n\n"
    "Dönemde üretilen (tamamlanan) mamullerin maliyeti kaç ₺’dir?",
    tl(mum), secenekler(mum, dum, ddb + dal + dis2 + gug2 + ydb - yds, dum + yds - ydb, kul + dis2 + ydb - yds),
    f"Kullanılan ilk madde {tl(ddb)} + {tl(dal)} − {tl(dds)} = {tl(kul)} ₺; dönem üretim maliyeti {tl(kul)} + {tl(dis2)} + "
    f"{tl(gug2)} = {tl(dum)} ₺. Tamamlanan mamul maliyeti = {tl(dum)} + {tl(ydb)} − {tl(yds)} = {tl(mum)} ₺.", zorluk="hard")

# 3 — satılan mamul maliyeti
mdb, mds = 40_000, 50_000
smm = mdb + mum - mds
P.sayisal(R,
    f"Bir üretim işletmesinde dönemde tamamlanan mamullerin maliyeti {tl(mum)} ₺ olarak hesaplanmıştır. İşletmenin "
    f"mamul dönem başı stoku {tl(mdb)} ₺, mamul dönem sonu stoku {tl(mds)} ₺’dir; net satışlar 520.000 ₺, faaliyet "
    "giderleri 110.000 ₺ olarak gerçekleşmiştir.\n\nDönemin satılan mamuller maliyeti kaç ₺’dir?",
    tl(smm), secenekler(smm, mum, mum + mds - mdb, mum + 110_000, 520_000 - mum),
    f"Satılan mamuller maliyeti = dönem başı mamul + tamamlanan mamul − dönem sonu mamul = {tl(mdb)} + {tl(mum)} − "
    f"{tl(mds)} = {tl(smm)} ₺. Faaliyet giderleri dönem gideridir, SMM’ye girmez.")

# 4 — ilk madde alış tutarı (ters hesap)
P.sayisal(R,
    "Bir işletmede dönem içinde üretimde kullanılan direkt ilk madde ve malzeme tutarı 342.000 ₺’dir. İlk madde ve "
    "malzeme stoku dönem başında 48.000 ₺, dönem sonunda 61.000 ₺ olup dönem içinde ilk madde iadesi veya fire "
    "olmamıştır.\n\nDönem içinde satın alınan ilk madde ve malzeme tutarı kaç ₺’dir?",
    tl(342_000 + 61_000 - 48_000), secenekler(355_000, 329_000, 342_000, 403_000, 390_000),
    "Kullanılan = dönem başı + alış − dönem sonu formülünden alış = kullanılan + dönem sonu − dönem başı = 342.000 + "
    "61.000 − 48.000 = 355.000 ₺.", zorluk="easy")

# 5 — brüt ve faaliyet kârı (bileşik)
ns, pz, gy, fin = 900_000, 70_000, 85_000, 40_000
P.q(R,
    f"Bir üretim işletmesinin net satışları {tl(ns)} ₺, satılan mamuller maliyeti {tl(smm)} ₺’dir. Aynı dönemde "
    f"pazarlama, satış ve dağıtım giderleri {tl(pz)} ₺, genel yönetim giderleri {tl(gy)} ₺, finansman giderleri "
    f"{tl(fin)} ₺ olarak gerçekleşmiştir.\n\nBrüt satış kârı ve faaliyet kârı sırasıyla kaç ₺’dir?",
    f"{tl(ns - smm)}; {tl(ns - smm - pz - gy)}",
    [f"{tl(ns - smm)}; {tl(ns - smm - pz - gy - fin)}", f"{tl(ns - smm - pz)}; {tl(ns - smm - pz - gy)}",
     f"{tl(ns)}; {tl(ns - smm)}", f"{tl(ns - smm)}; {tl(ns - smm - gy)}"],
    f"Brüt satış kârı = {tl(ns)} − {tl(smm)} = {tl(ns - smm)} ₺. Faaliyet kârı = brüt kâr − faaliyet giderleri (pazarlama "
    f"ve yönetim) = {tl(ns - smm - pz - gy)} ₺. Finansman gideri faaliyet kârından sonra düşülür.", zorluk="hard")

# 6 — sabit maliyetin birim davranışı
sb = 240_000
P.q(R,
    f"Bir işletmenin ilgili faaliyet aralığında aylık sabit üretim maliyetleri {tl(sb)} ₺’dir. Üretim ocak ayında 12.000 "
    "birim, şubat ayında 16.000 birim olmuştur; birim değişken maliyet her iki ayda da 18 ₺’dir ve fiyat değişikliği "
    "yaşanmamıştır.\n\nBirim sabit maliyet ve toplam sabit maliyet ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Birim sabit maliyet {tl(sb // 12_000)} ₺’den {tl(sb // 16_000)} ₺’ye iner, toplam {tl(sb)} ₺ kalır.",
    [f"Birim sabit maliyet {tl(sb // 12_000)} ₺ kalır, toplam sabit maliyet artar.",
     f"Birim sabit maliyet {tl(sb // 16_000)} ₺’den {tl(sb // 12_000)} ₺’ye çıkar, toplam değişmez.",
     "Birim ve toplam sabit maliyet üretimle aynı oranda artar.",
     f"Toplam sabit maliyet {tl(sb * 16 // 12)} ₺’ye çıkar, birim sabit maliyet değişmez."],
    "İlgili faaliyet aralığında toplam sabit maliyet üretim miktarından etkilenmez; üretim arttıkça sabit maliyet daha çok "
    f"birime bölündüğünden birim sabit maliyet düşer: 240.000 / 12.000 = 20 ₺, 240.000 / 16.000 = 15 ₺.")

# 7 — değişken maliyet davranışı
P.q(R,
    "Bir gıda üreticisinde ürün başına 6 ₺ ambalaj ve 14 ₺ hammadde kullanılmaktadır. Üretim miktarı nisan ayında 8.000 "
    "birimden mayıs ayında 10.000 birime çıkmış, girdi fiyatları ve ürün reçetesi değişmemiştir.\n\nBu maliyetlerle ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Toplamı 160.000 ₺’den 200.000 ₺’ye çıkar, birimi 20 ₺ kalır.",
    ["Toplamı 160.000 ₺ kalır, birimi 20 ₺’den 16 ₺’ye iner.",
     "Toplamı ve birimi üretimle aynı oranda artar.",
     "Toplamı 200.000 ₺’ye çıkar, birimi 25 ₺’ye yükselir.",
     "Toplamı değişmez, birimi 16 ₺’ye iner."],
    "Değişken maliyetin toplamı üretim miktarıyla doğru orantılı değişir (8.000 × 20 = 160.000 ₺; 10.000 × 20 = "
    "200.000 ₺), birim değişken maliyet ise sabit kalır (20 ₺).", zorluk="easy")

# 8 — en yüksek-en düşük yöntemi
h_x, h_y, l_x, l_y = 8_000, 520_000, 5_000, 400_000
dg = (h_y - l_y) // (h_x - l_x)
sabit = h_y - dg * h_x
P.q("En yüksek-en düşük noktalar yöntemi",
    "Bir işletmenin bakım giderleri karma nitelikte olup son altı ayın en yüksek ve en düşük faaliyet düzeyleri "
    f"şöyledir: en yüksek ayda {tl(h_x)} makine saatinde {tl(h_y)} ₺, en düşük ayda {tl(l_x)} makine saatinde {tl(l_y)} ₺ "
    "bakım gideri oluşmuştur.\n\nEn yüksek-en düşük noktalar yöntemine göre birim değişken maliyet ve aylık sabit maliyet "
    "sırasıyla kaç ₺’dir?",
    f"{tl(dg)}; {tl(sabit)}",
    [f"{tl(h_y // h_x)}; 0", f"{tl(dg)}; {tl(l_y)}", f"{tl(l_y // l_x)}; {tl(sabit)}", f"{tl(dg)}; {tl(h_y - dg * l_x)}"],
    f"Birim değişken maliyet = (520.000 − 400.000) / (8.000 − 5.000) = {tl(dg)} ₺/saat; sabit maliyet = 520.000 − "
    f"{tl(dg)} × 8.000 = {tl(sabit)} ₺.", zorluk="hard")

# 9 — tahmin
P.sayisal("En yüksek-en düşük noktalar yöntemi",
    f"Bir işletme bakım giderlerini en yüksek-en düşük noktalar yöntemiyle ayrıştırmış; birim değişken maliyeti "
    f"{tl(dg)} ₺/makine saati, aylık sabit maliyeti {tl(sabit)} ₺ olarak bulmuştur. Gelecek ay faaliyetin 7.000 makine saati "
    "olması, maliyet yapısının değişmemesi beklenmektedir.\n\nGelecek ay için tahmin edilen bakım gideri kaç ₺’dir?",
    tl(sabit + dg * 7_000), secenekler(sabit + dg * 7_000, dg * 7_000, sabit + 7_000 * (h_y // h_x), 520_000, 400_000),
    f"Toplam maliyet = sabit maliyet + birim değişken × faaliyet = {tl(sabit)} + {tl(dg)} × 7.000 = "
    f"{tl(sabit + dg * 7_000)} ₺.", zorluk="easy")

# 10 — mamul maliyetine girmeyen (olumsuz)
P.q(R,
    "Hazır giyim üreticisinin ay içindeki harcamaları şunlardır: kumaş bedeli, dikiş hattındaki işçilerin ücretleri, "
    "fabrika binasının elektrik gideri, üretim şefinin maaşı ve bayilere satış yapan temsilcilere ödenen satış primleri."
    "\n\nBu harcamalardan hangisi mamul maliyetine dâhil edilmez?",
    "Satış temsilcilerine ödenen primler",
    ["Kumaş bedeli", "Dikiş hattı işçilerinin ücretleri", "Fabrika binasının elektrik gideri", "Üretim şefinin maaşı"],
    "Mamul maliyeti direkt ilk madde, direkt işçilik ve genel üretim giderlerinden oluşur. Satış temsilcilerinin primi "
    "pazarlama, satış ve dağıtım gideridir, oluştuğu dönemde dönem gideri olarak kaydedilir.", zorluk="easy")

# 11 — direkt/endirekt
P.q(R,
    "Bir mobilya fabrikasında masa üretim hattında çalışan işçilerin ücretleri ürün başına izlenebilmektedir. Fabrikanın "
    "üretim müdürüne, bakım teknisyenlerine ve ambar görevlisine ödenen ücretler ise belirli bir ürüne doğrudan "
    "yüklenememektedir.\n\nÜretim müdürü, bakım teknisyenleri ve ambar görevlisinin ücretleri hangi maliyet unsurunda "
    "izlenir?",
    "Genel üretim giderlerinde",
    ["Direkt işçilik giderlerinde", "Genel yönetim giderlerinde", "Direkt ilk madde ve malzeme giderlerinde",
     "Pazarlama, satış ve dağıtım giderlerinde"],
    "Üretimle ilgili olup belirli bir mamule doğrudan izlenemeyen işçilik (endirekt işçilik) genel üretim giderleri "
    "kapsamındadır; ürüne doğrudan izlenen hat işçiliği direkt işçiliktir.")

# 12 — fırsat maliyeti
P.q("Maliyet kavramları",
    "Bir işletme kendi mülkü olan ve aylık 80.000 ₺’ye kiraya verebileceği bir depoyu kiraya vermek yerine yeni bir "
    "ürün hattı için kullanmaya karar vermiştir. Depo için ayrıca bir ödeme yapılmayacak, ürün hattının diğer maliyetleri "
    "ayrıca hesaplanmıştır.\n\nKiraya verilmediği için vazgeçilen 80.000 ₺ hangi maliyet kavramıyla ifade edilir?",
    "Fırsat maliyeti",
    ["Batık (geçmiş) maliyet", "Tarihî (kayıtlı) maliyet", "Kontrol edilemeyen maliyet", "Değişken maliyet"],
    "Bir seçenek tercih edildiğinde vazgeçilen en iyi alternatifin getirisi fırsat maliyetidir; kayıtlara girmez ama "
    "karar verirken dikkate alınır.", zorluk="easy")

# 13 — batık maliyet
P.q("Maliyet kavramları",
    "İşletme iki yıl önce 1.200.000 ₺’ye aldığı ve bugün defter değeri 700.000 ₺ olan bir makineyi yenileyip "
    "yenilememeye karar verecektir. Makinenin bugünkü satış değeri 250.000 ₺, yeni makinenin fiyatı 1.500.000 ₺’dir."
    "\n\nKarar açısından eski makinenin 700.000 ₺ defter değeri için aşağıdakilerden hangisi doğrudur?",
    "Batık maliyettir; karar için ilgisizdir.",
    ["Fırsat maliyetidir; karara dâhil edilir.",
     "Farksal maliyettir; yeni makine fiyatından düşülür.",
     "Gelecekte katlanılacak nakit maliyettir.",
     "Kontrol edilebilir maliyettir; karara dâhil edilir."],
    "Geçmişte katlanılmış ve hangi seçenek seçilirse seçilsin değişmeyecek maliyet batık maliyettir; karar için ilgili "
    "tutarlar eski makinenin bugünkü satış değeri ve yeni makinenin fiyatı gibi geleceğe yönelik farklardır.")

# 14 — farksal maliyet
P.sayisal("Maliyet kavramları",
    "Bir işletme bir parçayı iki farklı yöntemle üretebilecektir. A yönteminde aylık toplam maliyet 250.000 ₺ sabit ve "
    "10.000 birim için birim başına 14 ₺ değişken, B yönteminde 190.000 ₺ sabit ve birim başına 22 ₺ değişken maliyet "
    "oluşmaktadır. Aylık üretim 10.000 birimdir.\n\nİki yöntem arasındaki farksal maliyet kaç ₺’dir?",
    tl(abs((250_000 + 140_000) - (190_000 + 220_000))),
    secenekler(20_000, 60_000, 80_000, 40_000, 140_000),
    "A yöntemi: 250.000 + 10.000 × 14 = 390.000 ₺; B yöntemi: 190.000 + 10.000 × 22 = 410.000 ₺. İki seçenek arasındaki "
    "toplam maliyet farkı 20.000 ₺’dir; A yöntemi daha ucuzdur.", zorluk="hard")

# 15 — maliyet muhasebesinin amaçları (olumsuz)
P.q(R,
    "Yeni kurulan bir üretim işletmesinin yönetimi, maliyet muhasebesi bölümünden beklentilerini listelemektedir: mamul "
    "birim maliyetlerinin belirlenmesi, stokların değerlenmesi, fiyatlandırma kararlarına bilgi sağlanması, maliyetlerin "
    "kontrolü ve vergi matrahının beyan edilmesi.\n\nAşağıdakilerden hangisi maliyet muhasebesinin amaçlarından biri "
    "değildir?",
    "Vergi beyannamelerinin hazırlanıp verilmesi",
    ["Mamul birim maliyetlerinin belirlenmesi",
     "Dönem sonu stoklarının değerlenmesi",
     "Fiyatlandırma kararlarına bilgi sağlanması",
     "Maliyetlerin planlanması ve kontrolü"],
    "Maliyet muhasebesi birim maliyet hesaplama, stok değerleme, gelir tablosuna SMM bilgisi sağlama, planlama, kontrol ve "
    "karar desteği amaçlarını taşır; vergi beyanı vergi mevzuatı ve genel muhasebenin işidir.", zorluk="easy")

# 16 — dönem giderleri dâhil veri listesi, SMM
P.sayisal(R,
    "Bir üretim işletmesinin dönem verileri şöyledir: dönem başı mamul stoku 18.000 ₺, dönem sonu mamul stoku 24.000 ₺, "
    "dönemde üretilen mamuller maliyeti 96.000 ₺, genel yönetim giderleri 14.000 ₺, finansman giderleri 9.000 ₺, "
    "pazarlama giderleri 11.000 ₺ ve net satışlar 160.000 ₺.\n\nDönemin satılan mamuller maliyeti kaç ₺’dir?",
    tl(90_000), secenekler(90_000, 96_000, 102_000, 114_000, 124_000),
    "SMM = dönem başı mamul + üretilen − dönem sonu mamul = 18.000 + 96.000 − 24.000 = 90.000 ₺. Yönetim, finansman ve "
    "pazarlama giderleri dönem gideridir; SMM hesabına katılmaz.", zorluk="easy")

# 17 — 62 grubu (öncüllü)
P.oncul("MSUGT: 62 Satışların Maliyeti",
    "Tekdüzen Hesap Planı’nın 62 Satışların Maliyeti hesap grubunda yer alabilecek kalemler değerlendirilmektedir:",
    ["Satılan Mamuller Maliyeti", "Satılan Ticari Mallar Maliyeti", "Genel Yönetim Giderleri",
     "Satılan Hizmet Maliyeti"],
    "Yukarıdakilerden hangileri satışların maliyeti grubunda yer almaz?",
    "Yalnız III", ["Yalnız I", "Yalnız III", "I ve II", "III ve IV", "I, II ve IV"],
    "62 grubunda 620 Satılan Mamuller Maliyeti, 621 Satılan Ticari Mallar Maliyeti, 622 Satılan Hizmet Maliyeti ve 623 "
    "Diğer Satışların Maliyeti yer alır; genel yönetim giderleri 63 Faaliyet Giderleri grubundadır.")

# 18 — 7/B hesapları
P.q(R7,
    "Muhasebe Sistemi Uygulama Genel Tebliği’nin 7/B seçeneğini uygulayan bir işletme, giderlerini fonksiyonlarına göre "
    "değil çeşitlerine göre izlemektedir. İşletmede dönem içinde üretim işçilerine 450.000 ₺, yönetim memurlarına "
    "180.000 ₺ ücret ödenmiştir.\n\nÜretim işçilerine ödenen ücretler 7/B seçeneğinde hangi hesapta izlenir?",
    "791 İşçi Ücret ve Giderleri",
    ["720 Direkt İşçilik Giderleri", "792 Memur Ücret ve Giderleri", "730 Genel Üretim Giderleri",
     "794 Çeşitli Giderler"],
    "7/B seçeneğinde giderler çeşitlerine göre 790-797 hesaplarında izlenir: işçi ücretleri 791, memur ücretleri 792 "
    "hesabındadır. 720 ve 730 fonksiyon esasına dayanan 7/A seçeneğinin hesaplarıdır.")

# 19 — hizmet maliyetinin 622’ye aktarılması (yevmiye)
P.q(R7,
    "MSUGT’nin 7/A seçeneğini uygulayan bir danışmanlık işletmesinde dönem içinde verilen hizmetlerin maliyetleri 740 Hizmet "
    "Üretim Maliyeti hesabında 380.000 ₺ olarak toplanmıştır. Hizmetlerin tamamı dönem içinde müşterilere sunulmuştur."
    "\n\nDönem sonunda bu maliyetin gelir tablosuna aktarılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(622, 380_000)], [(741, 380_000)]),
    [K([(622, 380_000)], [(740, 380_000)]),
     K([(621, 380_000)], [(741, 380_000)]),
     K([(741, 380_000)], [(622, 380_000)]),
     K([(770, 380_000)], [(740, 380_000)])],
    "7/A’da 740 hesabında toplanan hizmet maliyeti 741 Hizmet Üretim Maliyeti Yansıtma Hesabı aracılığıyla 622 Satılan "
    "Hizmet Maliyeti hesabına aktarılır: 622 borç, 741 alacak; ardından 741 ile 740 birbirine kapatılır.", zorluk="hard")

# 20 — tam ve değişken maliyetleme stok farkı
ur, sat, sgug = 10_000, 8_000, 200_000
bsg = sgug // ur
P.q("Tam ve değişken maliyetleme",
    f"Bir işletme yıl içinde {tl(ur)} birim üretmiş, {tl(sat)} birim satmıştır; dönem başı stok yoktur. Birim değişken "
    f"üretim maliyeti 35 ₺, yıllık sabit genel üretim giderleri {tl(sgug)} ₺’dir ve üretim normal kapasitede "
    "gerçekleşmiştir.\n\nTam maliyetleme ile değişken maliyetleme arasındaki fark ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    f"Tam maliyetlemede dönem sonu stoku ve kâr {tl((ur - sat) * bsg)} ₺ fazladır.",
    [f"Değişken maliyetlemede dönem sonu stoku ve kâr {tl((ur - sat) * bsg)} ₺ fazladır.",
     "İki yöntemde de kâr ve dönem sonu stoku aynıdır.",
     f"Tam maliyetlemede kâr {tl(sgug)} ₺ fazladır.",
     f"Tam maliyetlemede dönem sonu stoku {tl(sat * bsg)} ₺ fazladır."],
    f"Tam maliyetlemede birim sabit GÜG ({tl(bsg)} ₺) stoklara yüklenir; satılmayan {tl(ur - sat)} birimle "
    f"{tl((ur - sat) * bsg)} ₺ sabit gider bir sonraki döneme ertelenir. Bu nedenle stok ve kâr bu tutarda yüksek çıkar.",
    zorluk="hard")

# 21 — tam/değişken birim maliyet
bd, bi, bg, sf, uret = 20, 12, 8, 300_000, 15_000
P.q("Tam ve değişken maliyetleme",
    f"Tek ürün üreten işletmede birim başına direkt ilk madde {bd} ₺, direkt işçilik {bi} ₺ ve değişken genel üretim "
    f"gideri {bg} ₺’dir. Yıllık sabit genel üretim giderleri {tl(sf)} ₺, normal ve fiilî üretim {tl(uret)} birimdir; birim "
    "başına 5 ₺ değişken satış gideri vardır.\n\nTam maliyetleme ve değişken maliyetlemeye göre birim mamul maliyeti "
    "sırasıyla kaç ₺’dir?",
    f"{bd + bi + bg + sf // uret}; {bd + bi + bg}",
    [f"{bd + bi + bg + sf // uret + 5}; {bd + bi + bg + 5}", f"{bd + bi + bg}; {bd + bi}",
     f"{bd + bi + sf // uret}; {bd + bi + bg}", f"{bd + bi + bg + sf // uret}; {bd + bi}"],
    f"Tam maliyetleme: {bd} + {bi} + {bg} + ({tl(sf)} / {tl(uret)} = {sf // uret}) = {bd + bi + bg + sf // uret} ₺. Değişken "
    f"maliyetleme sabit GÜG’ü dönem gideri sayar: {bd + bi + bg} ₺. Satış giderleri mamul maliyetine girmez.",
    zorluk="hard")

# 22 — maliyet fonksiyonu
P.q("Maliyet davranışları",
    "Bir işletmenin ilgili faaliyet aralığındaki toplam maliyet fonksiyonu TM = 50.000 + 12X olarak belirlenmiştir; X "
    "üretim miktarını göstermektedir. İşletme gelecek ay 4.000 birim üretmeyi planlamakta, fiyatların değişmeyeceğini "
    "varsaymaktadır.\n\nPlanlanan üretim için toplam maliyet ve birim maliyet sırasıyla kaç ₺’dir?",
    "98.000; 24,5",
    ["48.000; 12", "98.000; 12", "50.000; 12,5", "62.000; 15,5"],
    "TM = 50.000 + 12 × 4.000 = 98.000 ₺; birim maliyet 98.000 / 4.000 = 24,5 ₺. Birim değişken maliyet 12 ₺, birim sabit "
    "maliyet 12,5 ₺’dir.")

# 23 — kademeli sabit maliyet
P.sayisal("Maliyet davranışları",
    "Bir montaj işletmesinde her 500 birim üretim için bir kalite kontrol teknisyeni gerekmekte, her teknisyenin aylık "
    "maliyeti 30.000 ₺ olmaktadır. Teknisyen sayısı kesirli olamaz ve işletme mart ayında 1.300 birim üretmeyi "
    "planlamaktadır.\n\nMart ayındaki kalite kontrol maliyeti kaç ₺’dir?",
    tl(90_000), secenekler(90_000, 78_000, 60_000, 120_000, 39_000),
    "1.300 birim için 1.300 / 500 = 2,6 → 3 teknisyen gerekir; maliyet 3 × 30.000 = 90.000 ₺. Maliyet belli aralıklarda "
    "sıçrama yapan kademeli (yarı) sabit maliyettir.")

# 24 — ticari işletme SMM
P.sayisal("Satılan ticari mallar maliyeti",
    "Bir ticaret işletmesinin nisan ayı verileri şöyledir: ticari mal alımları 2.400.000 ₺, dönem başı ticari mal stoku "
    "300.000 ₺, dönem sonu ticari mal stoku 450.000 ₺, alış iadeleri 60.000 ₺, alış iskontoları 40.000 ₺ ve alışla "
    "ilgili taşıma giderleri 80.000 ₺.\n\nSatılan ticari mallar maliyeti kaç ₺’dir?",
    tl(300_000 + 2_400_000 + 80_000 - 60_000 - 40_000 - 450_000),
    secenekler(2_230_000, 2_250_000, 2_150_000, 2_330_000, 2_310_000),
    "STMM = dönem başı + alışlar + alış giderleri − alış iadeleri − alış iskontoları − dönem sonu = 300.000 + 2.400.000 + "
    "80.000 − 60.000 − 40.000 − 450.000 = 2.230.000 ₺.")

# 25 — kalite maliyetleri
P.q("Kalite maliyetleri",
    "Bir otomotiv yan sanayi işletmesi kalite maliyetlerini sınıflandırmaktadır. Ürünler müşteriye ulaştıktan sonra "
    "ortaya çıkan kusurlar nedeniyle garanti kapsamında yapılan 640.000 ₺ onarım ve geri çağırma giderleri ayrı bir "
    "kalemde izlenmek istenmektedir.\n\nBu giderler hangi kalite maliyeti sınıfına girer?",
    "Dış başarısızlık maliyetleri",
    ["Önleme maliyetleri", "Değerlendirme (ölçme) maliyetleri", "İç başarısızlık maliyetleri",
     "Tasarım ve eğitim maliyetleri"],
    "Kusurlu ürün müşteriye ulaştıktan sonra katlanılan garanti, onarım ve geri çağırma giderleri dış başarısızlık "
    "maliyetidir; teslimden önce yakalanan kusurların yeniden işleme maliyeti iç başarısızlıktır.")

# 26 — gider, maliyet, zarar ayrımı
P.q("Maliyet kavramları",
    "Bir üretim işletmesinin ay içindeki olayları şunlardır: 900.000 ₺’ye yeni bir makine satın alınmış, üretimde "
    "kullanılan ilk maddelerin 250.000 ₺’lik kısmı mamule dönüşmüş, depoda çıkan yangında 70.000 ₺’lik stok "
    "kullanılamaz hâle gelmiştir.\n\nYangında kullanılamaz hâle gelen stok için aşağıdakilerden hangisi doğrudur?",
    "Karşılığında fayda sağlanmadığından zarardır.",
    ["Mamul maliyetine giren bir maliyettir.",
     "Bir harcamadır; varlık olarak aktifleştirilir.",
     "Genel yönetim gideri olarak kaydedilir.",
     "Gelecek dönem gideri olarak ertelenir."],
    "Makine alımı harcamadır ve varlık olarak aktifleşir; ilk maddelerin üretimde kullanılması maliyete dönüşür. Karşılığında "
    "fayda elde edilmeyen yangın kaybı ise zarardır.")

# 27 — birim dönüşüm maliyeti oranlarından DİŞ (ters hesap)
dimm3, gug3, adet3, birim3 = 120_000, 80_000, 3_000, 100
dis3 = adet3 * birim3 - dimm3 - gug3
P.sayisal(R,
    f"Bir işletmede dönem içinde {tl(adet3)} birim mamul üretilmiş, dönem başı ve dönem sonu yarı mamul stoku "
    f"bulunmamaktadır. Direkt ilk madde ve malzeme gideri {tl(dimm3)} ₺, genel üretim gideri {tl(gug3)} ₺ olup "
    f"mamulün birim maliyeti {tl(birim3)} ₺ olarak hesaplanmıştır.\n\nİşletmenin direkt işçilik gideri kaç ₺’dir?",
    tl(dis3), secenekler(dis3, 300_000, 200_000, 180_000, 80_000),
    f"Toplam üretim maliyeti {tl(adet3)} × {tl(birim3)} = {tl(adet3 * birim3)} ₺’dir. DİŞ = {tl(adet3 * birim3)} − "
    f"{tl(dimm3)} − {tl(gug3)} = {tl(dis3)} ₺.", zorluk="easy")

# 28 — birim GÜG
P.sayisal(R,
    "Dönemde 12.000 birim mamul üreten işletmede üretimle ilgili giderler şöyledir: kumaş 360.000 ₺, dikiş işçileri "
    "ücreti 240.000 ₺, fabrika kirası 96.000 ₺, makine amortismanı 48.000 ₺, fabrika enerji gideri 36.000 ₺ ve satış "
    "mağazası kirası 60.000 ₺.\n\nBirim başına genel üretim gideri kaç ₺’dir?",
    tl((96_000 + 48_000 + 36_000) // 12_000), secenekler(15, 20, 35, 65, 12),
    "Genel üretim giderleri fabrika kirası, makine amortismanı ve fabrika enerjisidir: 96.000 + 48.000 + 36.000 = "
    "180.000 ₺; birim GÜG 180.000 / 12.000 = 15 ₺. Kumaş DİMM, dikiş işçiliği DİŞ, mağaza kirası dönem gideridir.")

# 29 — marjinal maliyet
P.sayisal("Maliyet kavramları",
    "Bir işletmenin toplam üretim maliyeti 10.000 birimlik üretimde 500.000 ₺’dir. Üretimi 10.500 birime çıkarması "
    "hâlinde toplam maliyetin 516.000 ₺ olacağı, sabit maliyetlerin değişmeyeceği hesaplanmıştır.\n\nİlave 500 birim "
    "için birim başına marjinal maliyet kaç ₺’dir?",
    tl(32), secenekler(32, 50, 49, 16, 1),
    "Marjinal maliyet, ilave üretimin toplam maliyette yarattığı artıştır: (516.000 − 500.000) / 500 = 32 ₺. Ortalama "
    "maliyet ise 500.000 / 10.000 = 50 ₺’dir.")

# 30 — muhasebe bilgi sistemi (olumsuz)
P.q("Muhasebe bilgi sistemi",
    "Bir işletmenin muhasebe bilgi sistemi üretim, satın alma, satış ve insan kaynakları alt sistemlerinden veri "
    "toplamaktadır. Yönetim sistemin işleyişini değerlendirirken sistemin girdileri, süreçleri ve çıktılarına ilişkin "
    "ifadeler hazırlamıştır.\n\nMuhasebe bilgi sistemi ile ilgili aşağıdakilerden hangisi yanlıştır?",
    "Sadece iç kullanıcılara bilgi sağlar.",
    ["Mali nitelikteki işlemleri kaydeder ve sınıflandırır.",
     "Karar alıcılara finansal raporlar sunar.",
     "Diğer bilgi alt sistemlerinden veri alır.",
     "Belgeler sistemin temel girdilerini oluşturur."],
    "Muhasebe bilgi sistemi işletme yönetimi gibi iç kullanıcıların yanında ortaklar, kredi verenler, devlet ve yatırımcılar "
    "gibi dış kullanıcılara da bilgi sağlar.")

# 31 — kapasite kavramları
P.q("Kapasite kavramları",
    "Bir fabrikanın makineleri hiç durmadan çalışsaydı yılda 12.000 birim üretebilecekti. Olağan bakım ve vardiya "
    "değişimleri dikkate alındığında ulaşılabilir kapasite 10.500 birim, son üç yılın ortalama talebine göre hesaplanan "
    "kapasite 9.000 birim, bu yıl gerçekleşen üretim 8.200 birimdir.\n\nNormal kapasite aşağıdakilerden hangisidir?",
    "9.000 birim",
    ["12.000 birim", "10.500 birim", "8.200 birim", "11.250 birim"],
    "Teorik (azami) kapasite 12.000, pratik kapasite 10.500 birimdir. Normal kapasite birkaç dönemin ortalama talebine "
    "göre belirlenen 9.000 birimdir; fiilî kapasite 8.200 birimdir.")

P.sayisal("Kapasite kavramları",
    "Normal kapasitesi 9.000 birim olan bir fabrikada yıl içinde 7.200 birim üretim yapılmıştır. Fabrikanın pratik "
    "kapasitesi 10.000 birim, teorik kapasitesi 12.000 birimdir; işletme kapasite kullanım oranını normal kapasiteye göre "
    "hesaplamaktadır.\n\nKapasite kullanım oranı yüzde kaçtır?",
    "%80", ["%60", "%72", "%90", "%125"],
    "Kapasite kullanım oranı = fiilî üretim / normal kapasite = 7.200 / 9.000 = %80. Pratik kapasiteye göre %72, teorik "
    "kapasiteye göre %60 bulunurdu.", zorluk="easy")

# 33 — 710-711-151 (yevmiye)
P.q(R7,
    "MSUGT’nin 7/A seçeneğini uygulayan bir üretim işletmesinde ay içinde 710 Direkt İlk Madde ve Malzeme Giderleri hesabında "
    "420.000 ₺ birikmiştir. Ay sonunda bu tutar maliyet hesaplarına aktarılacak, üretim henüz tamamlanmamıştır.\n\n"
    "Ay sonunda yapılacak aktarım kaydı aşağıdakilerden hangisidir?",
    K([(151, 420_000)], [(711, 420_000)]),
    [K([(152, 420_000)], [(711, 420_000)]),
     K([(151, 420_000)], [(710, 420_000)]),
     K([(711, 420_000)], [(151, 420_000)]),
     K([(620, 420_000)], [(711, 420_000)])],
    "7/A’da 710 hesabında toplanan gider 711 Direkt İlk Madde ve Malzeme Yansıtma Hesabı aracılığıyla 151 Yarı Mamuller – "
    "Üretim hesabına aktarılır; dönem sonunda 711 ile 710 birbirine kapatılır.")

# 34 — normal maliyet yöntemi
P.q("Maliyet yöntemleri",
    "Bir işletme mamul maliyetlerini dönem içinde hızlı hesaplayabilmek için direkt ilk madde ve direkt işçilik "
    "giderlerini gerçekleşen tutarlarıyla, genel üretim giderlerini ise dönem başında belirlenen tahmini yükleme "
    "oranıyla maliyete yüklemektedir.\n\nİşletmenin uyguladığı maliyet yöntemi aşağıdakilerden hangisidir?",
    "Normal maliyet yöntemi",
    ["Fiilî (gerçek) maliyet yöntemi", "Standart maliyet yöntemi", "Değişken maliyet yöntemi",
     "Faaliyet tabanlı maliyet yöntemi"],
    "Normal maliyet yönteminde DİMM ve DİŞ fiilî tutarlarıyla, GÜG önceden belirlenmiş yükleme oranıyla maliyete "
    "yüklenir; fiilî maliyet yönteminde tüm unsurlar gerçekleşen tutarlarla yüklenir.")

# 35 — önceden belirlenmiş yükleme oranı
P.sayisal("Genel üretim gideri yükleme oranı",
    "Bir işletme yılın başında gelecek yıl için 600.000 ₺ genel üretim gideri ve 40.000 direkt işçilik saati tahmin "
    "etmiştir. İşletme GÜG’ü direkt işçilik saatine göre, önceden belirlenen bir oranla mamullere yüklemektedir.\n\n"
    "Önceden belirlenmiş GÜG yükleme oranı direkt işçilik saati başına kaç ₺’dir?",
    tl(15), secenekler(15, 12, 20, 25, 30),
    "Önceden belirlenmiş yükleme oranı = tahmini GÜG / tahmini dağıtım ölçüsü = 600.000 / 40.000 = 15 ₺/DİS.",
    zorluk="easy")

# 36 — fazla/eksik yükleme
yk, fdis, fgug = 15, 38_000, 590_000
P.q("Genel üretim gideri yükleme oranı",
    f"GÜG’ü direkt işçilik saati başına {yk} ₺ oranla mamullere yükleyen işletmede yıl içinde {tl(fdis)} direkt işçilik saati "
    f"çalışılmış, gerçekleşen genel üretim giderleri {tl(fgug)} ₺ olmuştur. Yıl sonunda yüklenen ve gerçekleşen tutarlar "
    "karşılaştırılacaktır.\n\nYüklenen GÜG ve fark ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"{tl(yk * fdis)} ₺ yüklenmiş, {tl(fgug - yk * fdis)} ₺ eksik yüklenmiştir.",
    [f"{tl(yk * fdis)} ₺ yüklenmiş, {tl(fgug - yk * fdis)} ₺ fazla yüklenmiştir.",
     f"{tl(600_000)} ₺ yüklenmiş, {tl(10_000)} ₺ fazla yüklenmiştir.",
     f"{tl(fgug)} ₺ yüklenmiş, fark oluşmamıştır.",
     f"{tl(yk * 40_000)} ₺ yüklenmiş, {tl(fgug - yk * 40_000)} ₺ eksik yüklenmiştir."],
    f"Yüklenen GÜG = {yk} × {tl(fdis)} = {tl(yk * fdis)} ₺. Gerçekleşen ({tl(fgug)} ₺) yüklenenden büyük olduğundan "
    f"{tl(fgug - yk * fdis)} ₺ eksik yükleme vardır.", zorluk="hard")

# 37 — eksik yüklemenin kapatılması
P.q("Genel üretim gideri yükleme oranı",
    "Yıl sonunda işletmede 20.000 ₺ eksik yüklenmiş genel üretim gideri bulunmaktadır. Tutar toplam üretim maliyetinin "
    "%0,5’i kadardır ve önemsiz kabul edilmiştir; mamullerin büyük bölümü yıl içinde satılmıştır.\n\nEksik yüklenen "
    "tutarın muhasebeleştirilmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Satılan mamuller maliyetine eklenerek kapatılır.",
    ["Gelecek yılın yükleme oranına eklenerek ertelenir.",
     "Genel yönetim giderleri hesabına aktarılır.",
     "Özkaynaklarda ayrı bir fonda izlenir.",
     "Mamul stoklarından düşülür."],
    "Önemsiz fark genellikle satılan mamuller maliyetine aktarılır (eksik yüklemede SMM artırılır); önemli farklar ise "
    "yarı mamul, mamul ve SMM arasında oranlı dağıtılır.")

# 38 — 7/A 71 grubu kapsam
P.q(R7,
    "Tekdüzen Hesap Planı’nın 7/A seçeneğini uygulayan işletmenin muhasebe servisi, 7 Maliyet Hesapları sınıfının "
    "fonksiyonel yapısını yeni personele açıklamaktadır. Personel 71 grubunda hangi giderlerin izlendiğini "
    "sormaktadır.\n\n7/A seçeneğinde 71 hesap grubu hangi giderleri izler?",
    "Direkt ilk madde ve malzeme giderlerini",
    ["Direkt işçilik giderlerini", "Genel üretim giderlerini", "Hizmet üretim maliyetini",
     "Pazarlama, satış ve dağıtım giderlerini"],
    "7/A’da 71 grubu direkt ilk madde ve malzeme, 72 direkt işçilik, 73 genel üretim giderleri, 74 hizmet üretim maliyeti, "
    "75 Ar-Ge, 76 pazarlama-satış-dağıtım, 77 genel yönetim, 78 finansman giderleri içindir.", zorluk="easy")

# 39 — sabit maliyet olmayan (olumsuz)
P.q("Maliyet davranışları",
    "Bir ekmek fabrikasının aylık maliyetleri şunlardır: fabrika binasının kirası, makinelerin doğrusal amortismanı, "
    "fabrika müdürünün sabit maaşı, sigorta primi ve ürün başına kullanılan un.\n\nİlgili faaliyet aralığında bu "
    "maliyetlerden hangisi sabit maliyet değildir?",
    "Ürün başına kullanılan un",
    ["Fabrika binasının kirası", "Makinelerin doğrusal amortismanı", "Fabrika müdürünün sabit maaşı",
     "Fabrika sigorta primi"],
    "Un, üretim miktarıyla doğru orantılı değişen değişken maliyettir. Kira, doğrusal amortisman, sabit maaş ve sigorta "
    "primi ilgili faaliyet aralığında üretimden bağımsız sabit maliyetlerdir.", zorluk="easy")

# 40 — endirekt malzeme
P.q(R,
    "Bir mobilya üreticisinde masaların tablası ve ayakları için kullanılan ahşap ürün başına izlenebilmektedir. Montajda "
    "kullanılan vida, tutkal ve zımpara kâğıdı ise az tutarlı olup ürün başına izlenmesi ekonomik "
    "değildir.\n\nVida, tutkal ve zımpara kâğıdı hangi maliyet unsurunda izlenir?",
    "Genel üretim giderlerinde (endirekt malzeme)",
    ["Direkt ilk madde ve malzeme giderlerinde",
     "Direkt işçilik giderlerinde",
     "Pazarlama, satış ve dağıtım giderlerinde",
     "Genel yönetim giderlerinde"],
    "Üretimde kullanılan ancak ürüne ekonomik biçimde izlenemeyen yardımcı malzemeler endirekt malzemedir ve genel üretim "
    "giderleri kapsamında izlenir.")

# 41 — fonksiyonel sınıflama: Ar-Ge
P.q("Maliyetlerin fonksiyonlarına göre sınıflandırılması",
    "Bir ilaç üreticisinin yıl içindeki giderleri şöyledir: yeni etken madde için laboratuvar çalışmaları 900.000 ₺, "
    "fabrikada ilaç üretimi 4.200.000 ₺, eczanelere tanıtım 700.000 ₺ ve genel müdürlük giderleri 600.000 ₺. İşletme 7/A "
    "seçeneğini uygulamaktadır.\n\nLaboratuvar çalışmaları hangi hesapta izlenir?",
    "750 Araştırma ve Geliştirme Giderleri",
    ["730 Genel Üretim Giderleri", "760 Pazarlama, Satış ve Dağıtım Giderleri", "770 Genel Yönetim Giderleri",
     "710 Direkt İlk Madde ve Malzeme Giderleri"],
    "7/A’da giderler fonksiyonlarına göre izlenir: araştırma ve geliştirme faaliyetleri 750, üretim 71-73, tanıtım 760, "
    "genel müdürlük 770 hesabında toplanır.")

# 42 — tam maliyetleme toplam kâr farkı (sayısal)
P.sayisal("Tam ve değişken maliyetleme",
    "Dönem başı stoku olmayan işletme 20.000 birim üretmiş ve 17.000 birim satmıştır. Yıllık sabit genel üretim "
    "giderleri 500.000 ₺, birim değişken üretim maliyeti 40 ₺ ve birim satış fiyatı 90 ₺’dir. Değişken maliyetlemeye "
    "göre dönem kârı 350.000 ₺ bulunmuştur.\n\nTam maliyetlemeye göre dönem kârı kaç ₺’dir?",
    tl(350_000 + 3_000 * 25), secenekler(425_000, 350_000, 275_000, 500_000, 850_000),
    "Birim sabit GÜG 500.000 / 20.000 = 25 ₺’dir. Satılmayan 3.000 birimle 75.000 ₺ sabit gider stokta kalır; tam "
    "maliyetlemede kâr 350.000 + 75.000 = 425.000 ₺ olur.", zorluk="hard")

# 43 — maliyet taşıyıcı
P.q("Maliyet kavramları",
    "Bir matbaa her müşteri siparişinin maliyetini ayrı izlemekte; bir kitabın basımında kullanılan kâğıt, baskı saati "
    "ve ciltleme işçiliği doğrudan o siparişe, fabrika genel giderleri ise bir yükleme oranıyla siparişlere "
    "yüklenmektedir.\n\nBu işletmede maliyetlerin kendisine yüklendiği sipariş, hangi kavramla ifade edilir?",
    "Maliyet taşıyıcı (maliyet nesnesi)",
    ["Gider yeri", "Dağıtım anahtarı", "Maliyet sürücüsü", "Kontrol noktası"],
    "Maliyetlerin kendisine yüklendiği mamul, sipariş veya hizmet maliyet taşıyıcısıdır; gider yeri giderlerin doğduğu "
    "bölüm, dağıtım anahtarı ise giderlerin paylaştırılmasında kullanılan ölçüdür.")

# 44 — kontrol edilebilir maliyet
P.q("Maliyet kavramları",
    "Bir fabrikada kesim bölümü şefi, bölümünde kullanılan malzeme miktarı ve fazla mesai süreleri üzerinde karar "
    "yetkisine sahiptir. Buna karşılık fabrika binasının amortismanı ve genel müdürlükten dağıtılan giderler üzerinde "
    "yetkisi bulunmamaktadır.\n\nKesim bölümü şefi açısından malzeme ve fazla mesai maliyetleri hangi niteliktedir?",
    "Kontrol edilebilir maliyetlerdir.",
    ["Kontrol edilemeyen maliyetlerdir.", "Batık maliyetlerdir.", "Fırsat maliyetleridir.",
     "Ortak maliyetlerdir."],
    "Bir yöneticinin belirli bir dönemde önemli ölçüde etkileyebildiği maliyetler onun için kontrol edilebilir "
    "maliyetlerdir; amortisman ve dağıtılan merkezi giderler şef için kontrol edilemeyen maliyetlerdir.", zorluk="easy")

# 45 — dönem giderleri toplamı
P.sayisal("Dönem giderleri",
    "Bir üretim işletmesinin dönem verileri şöyledir: direkt ilk madde 250.000 ₺, direkt işçilik 180.000 ₺, genel üretim "
    "giderleri 120.000 ₺, satış personeli ücretleri 90.000 ₺, reklam giderleri 40.000 ₺, genel müdürlük kirası 60.000 ₺ "
    "ve banka kredisi faizi 30.000 ₺.\n\nDönemin faaliyet giderleri toplamı kaç ₺’dir?",
    tl(90_000 + 40_000 + 60_000), secenekler(190_000, 220_000, 130_000, 310_000, 740_000),
    "Faaliyet giderleri pazarlama-satış-dağıtım ve genel yönetim giderleridir: 90.000 + 40.000 + 60.000 = 190.000 ₺. "
    "Üretim giderleri mamul maliyetine, kredi faizi finansman giderlerine girer.")

# 46 — değişken maliyetlemede sabit GÜG
P.q("Tam ve değişken maliyetleme",
    "Yönetim raporlarında değişken (direkt) maliyetleme kullanan bir işletme, yıllık 400.000 ₺ sabit genel üretim "
    "giderinin nasıl raporlanacağını değerlendirmektedir. İşletmenin yıl sonunda satılmamış mamul stoku "
    "bulunmaktadır.\n\nDeğişken maliyetlemede sabit genel üretim giderleri için aşağıdakilerden hangisi doğrudur?",
    "Oluştuğu dönemde tamamen gider yazılır.",
    ["Satılan ve satılmayan mamullere oranlı dağıtılır.",
     "Sadece satılmayan mamullere yüklenir.",
     "Gelecek yıllara ait gider olarak ertelenir.",
     "Normal kapasiteye göre stoklara yüklenir."],
    "Değişken maliyetlemede mamul maliyetine sadece değişken üretim maliyetleri girer; sabit GÜG dönem gideri sayılır ve "
    "oluştuğu dönemin gelir tablosuna tamamen yansır.")

# 47 — 151-152 aktarım (yevmiye)
P.q(R7,
    "Üretim işletmesinde ay içinde 151 Yarı Mamuller – Üretim hesabında toplanan maliyetlerden 610.000 ₺’lik kısmı ay "
    "sonunda tamamlanan ürünlere aittir. Tamamlanan ürünler mamul ambarına alınmış, geri kalan tutar yarı mamul olarak "
    "üretim hattında kalmıştır.\n\nTamamlanan ürünlerin ambara alınmasına ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(152, 610_000)], [(151, 610_000)]),
    [K([(151, 610_000)], [(152, 610_000)]),
     K([(620, 610_000)], [(151, 610_000)]),
     K([(153, 610_000)], [(151, 610_000)]),
     K([(152, 610_000)], [(711, 610_000)])],
    "Tamamlanan üretimin maliyeti yarı mamul hesabından mamul hesabına aktarılır: 152 Mamuller borç, 151 Yarı Mamuller – "
    "Üretim alacak 610.000 ₺. Mamuller satılınca 620’ye aktarılır.", zorluk="easy")

# 48 — maliyet dönemi
P.q("Maliyet dönemi",
    "Bir üretim işletmesinin hesap dönemi takvim yılıdır. Yönetim, fiyatlandırma ve kontrol kararları için mamul birim "
    "maliyetlerini yıl sonunu beklemeden görmek istemekte, maliyet muhasebesi bölümü de hesaplamaları daha kısa "
    "aralıklarla yapmayı önermektedir.\n\nMaliyet dönemi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Genellikle ay olarak belirlenir, hesap döneminden kısadır.",
    ["Hesap dönemine eşit olmalıdır.",
     "Vergi mevzuatıyla bir yıl olarak belirlenmiştir.",
     "Sadece yıl sonunda bir kez hesaplanır.",
     "Hesap döneminden uzun olabilir."],
    "Maliyet dönemi mamul maliyetlerinin hesaplandığı süredir; yönetime zamanında bilgi sağlamak için genellikle ay olarak "
    "seçilir ve hesap döneminden kısadır.")

# 49 — kâr marjı
P.sayisal("Brüt kâr",
    "Bir işletmenin net satışları 2.400.000 ₺, satılan mamuller maliyeti 1.680.000 ₺, faaliyet giderleri 360.000 ₺’dir. "
    "Yönetim brüt kârın net satışlara oranını (brüt kâr marjını) rakip işletmelerle karşılaştırmak istemektedir.\n\n"
    "İşletmenin brüt kâr marjı yüzde kaçtır?",
    "%30", ["%15", "%42,9", "%70", "%21,4"],
    "Brüt kâr = 2.400.000 − 1.680.000 = 720.000 ₺; brüt kâr marjı 720.000 / 2.400.000 = %30. Faaliyet giderleri düşülünce "
    "faaliyet kâr marjı %15 olur.", zorluk="easy")

# 50 — GÜG kapsamında olmayan (olumsuz)
P.q(R,
    "Bir işletmenin maliyet muhasebecisi genel üretim giderlerini belirlemektedir. Ay içindeki giderler arasında fabrika "
    "binasının amortismanı, üretim şefinin maaşı, üretim makinelerinin bakımı, fabrikanın ısıtma gideri ve genel müdürlük "
    "binasının temizlik gideri vardır.\n\nAşağıdakilerden hangisi genel üretim giderleri kapsamında değildir?",
    "Genel müdürlük binasının temizlik gideri",
    ["Fabrika binasının amortismanı", "Üretim şefinin maaşı", "Üretim makinelerinin bakımı",
     "Fabrikanın ısıtma gideri"],
    "Üretim yerinde oluşan ve ürüne doğrudan izlenemeyen giderler GÜG’dür. Genel müdürlük binasının temizliği yönetim "
    "fonksiyonuna aittir, 770 Genel Yönetim Giderleri hesabında izlenir.", zorluk="easy")

# 51 — ilgili faaliyet aralığı
P.q("Maliyet davranışları",
    "Bir işletmenin mevcut fabrikası aylık en çok 20.000 birim üretebilmektedir ve bu kapasitede sabit maliyetler 800.000 ₺"
    "’dir. Üretimin 20.000 birimi aşması için ikinci bir vardiya açılması ve sabit maliyetlerin 1.100.000 ₺’ye çıkması "
    "gerekmektedir.\n\nBu durum aşağıdaki kavramlardan hangisiyle açıklanır?",
    "Sabit maliyetler ilgili faaliyet aralığında sabittir.",
    ["Sabit maliyetler her üretim düzeyinde sabittir.",
     "Değişken maliyetler kapasite aşılınca sabitleşir.",
     "Birim sabit maliyet üretimle birlikte artar.",
     "Toplam maliyet üretimden bağımsızdır."],
    "Sabit maliyetlerin sabitliği belirli bir kapasite ve zaman aralığı (ilgili faaliyet aralığı) içindir; kapasite "
    "aşıldığında sabit maliyetler yeni bir düzeye sıçrar.")

# 52 — mamul ve dönem maliyeti ayrımı (öğretici hesap)
P.q(R,
    "Bir üretim işletmesinde ay içinde 300.000 ₺ üretim maliyeti oluşmuş, üretilen mamullerin %80’i aynı ay satılmış, "
    "%20’si ambarda kalmıştır. Aynı ay 50.000 ₺ pazarlama gideri yapılmış; dönem başında stok bulunmamaktadır.\n\n"
    "Bu tutarların ay sonucuna etkisi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "240.000 ₺ SMM ve 50.000 ₺ dönem gideri olarak sonuca yansır.",
    ["300.000 ₺ üretim maliyeti ve 50.000 ₺ pazarlama gideri tamamen sonuca yansır.",
     "240.000 ₺ SMM olarak yansır, pazarlama gideri stoklara eklenir.",
     "60.000 ₺ SMM ve 50.000 ₺ dönem gideri olarak sonuca yansır.",
     "Sadece 50.000 ₺ pazarlama gideri sonuca yansır."],
    "Mamul maliyetleri satıldıkları dönemde SMM olarak gider olur: 300.000 × %80 = 240.000 ₺; kalan 60.000 ₺ stokta "
    "kalır. Pazarlama gideri dönem maliyeti olduğundan oluştuğu ayda tamamen gider yazılır.", zorluk="hard")

# 53 — 7/A GÜG yansıtma kapanış
P.q(R7,
    "MSUGT’nin 7/A seçeneğinde bir işletmenin dönem sonunda 730 Genel Üretim Giderleri hesabında 280.000 ₺, 731 Genel Üretim "
    "Giderleri Yansıtma Hesabında 280.000 ₺ bakiye bulunmaktadır. Yansıtma işlemleri dönem içinde yapılmış, fark "
    "oluşmamıştır.\n\nDönem sonunda bu iki hesabın kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(731, 280_000)], [(730, 280_000)]),
    [K([(730, 280_000)], [(731, 280_000)]),
     K([(151, 280_000)], [(731, 280_000)]),
     K([(620, 280_000)], [(730, 280_000)]),
     K([(731, 280_000)], [(151, 280_000)])],
    "Yansıtma hesabı alacak, gider hesabı borç bakiye verdiğinden dönem sonunda birbirine kapatılır: 731 borç, 730 "
    "alacak 280.000 ₺. Tutar daha önce 151 hesabına aktarılmıştır.")

# 54 — değişken maliyetleme ve MHK ilişkisi
P.q("Tam ve değişken maliyetleme",
    "Bir işletme yönetimi, ürünlerinin katkı payını ve başabaş noktasını gösteren raporlar istemektedir. Muhasebe "
    "bölümü bu amaçla gelir tablosunu satışlardan değişken maliyetleri düşerek katkı payını, ardından sabit maliyetleri "
    "düşerek kârı gösterecek biçimde hazırlamıştır.\n\nBu rapor hangi maliyetleme yaklaşımına dayanır?",
    "Değişken (direkt) maliyetleme",
    ["Tam (absorbe edici) maliyetleme", "Standart maliyetleme", "Sipariş maliyetleme",
     "Safha maliyetleme"],
    "Katkı payı biçimli gelir tablosu değişken maliyetlemenin ürünüdür; maliyetler davranışlarına göre değişken ve sabit "
    "olarak ayrılır ve maliyet-hacim-kâr analizine uygun bilgi verir.", zorluk="easy")

# 55 — üretilen mamul maliyeti formülü
P.q(R,
    "Maliyet muhasebesi dersinde öğrenciler bir işletmenin üretim maliyeti tablosunu düzenlemektedir. Tabloda dönemin "
    "üretim maliyetleri toplamı ile yarı mamul stoklarındaki değişim dikkate alınarak tamamlanan ürünlerin maliyeti "
    "bulunacaktır.\n\nDönemde üretilen mamul maliyeti aşağıdaki formüllerden hangisiyle hesaplanır?",
    "Dönem üretim maliyeti + dönem başı yarı mamul − dönem sonu yarı mamul",
    ["Dönem üretim maliyeti + dönem sonu yarı mamul − dönem başı yarı mamul",
     "Dönem başı mamul + dönem üretim maliyeti − dönem sonu mamul",
     "Direkt ilk madde + direkt işçilik − genel üretim giderleri",
     "Satılan mamuller maliyeti + dönem sonu mamul − dönem başı mamul"],
    "Tamamlanan (üretilen) mamul maliyeti dönemin üretim maliyetine dönem başı yarı mamul eklenip dönem sonu yarı mamul "
    "düşülerek bulunur; mamul stok değişimi ise SMM hesabında kullanılır.")

# 56 — kalite: iç başarısızlık vs değerlendirme
P.q("Kalite maliyetleri",
    "Elektronik kart üreten işletmede sevkiyattan önce yapılan son testlerde kusurlu bulunan kartların söküm, onarım ve "
    "yeniden test işlemleri için ay içinde 220.000 ₺ harcanmıştır. Bu kartlar müşteriye ulaşmadan düzeltilmiştir.\n\n"
    "Bu harcama hangi kalite maliyeti sınıfına girer?",
    "İç başarısızlık maliyetleri",
    ["Dış başarısızlık maliyetleri", "Önleme maliyetleri", "Değerlendirme (ölçme) maliyetleri",
     "Garanti karşılığı giderleri"],
    "Kusurun ürün müşteriye ulaşmadan tespit edilip giderilmesi için yapılan onarım ve yeniden işleme iç başarısızlık "
    "maliyetidir; testin kendisi değerlendirme, müşteride ortaya çıkan kusur dış başarısızlık maliyetidir.")

# 57 — birim maliyet hesaplama (yarı mamul yok)
P.sayisal(R,
    "Tek ürün üreten işletmede ay içinde 8.000 birim üretime başlanmış ve tamamı tamamlanmıştır. Direkt ilk madde "
    "256.000 ₺, direkt işçilik 144.000 ₺, genel üretim gideri 112.000 ₺ olup ayrıca 64.000 ₺ satış gideri ve 48.000 ₺ "
    "yönetim gideri oluşmuştur.\n\nMamulün birim üretim maliyeti kaç ₺’dir?",
    tl((256_000 + 144_000 + 112_000) // 8_000), secenekler(64, 78, 50, 72, 32),
    "Birim üretim maliyeti = (256.000 + 144.000 + 112.000) / 8.000 = 64 ₺. Satış ve yönetim giderleri dönem gideridir; "
    "birim maliyete eklenirse 78 ₺ bulunur ki bu yanlıştır.", zorluk="easy")

# 58 — harcama/gider ayrımı: makine
P.q("Maliyet kavramları",
    "Bir işletme 1 Ocak’ta 1.000.000 ₺’ye bir üretim makinesi satın almış ve bedelini ödemiştir. Makinenin faydalı ömrü "
    "10 yıl olup yıl sonunda 100.000 ₺ amortisman ayrılmıştır; makine tüm yıl boyunca üretimde kullanılmıştır.\n\n"
    "Bu tutarlarla ilgili aşağıdakilerden hangisi doğrudur?",
    "1.000.000 ₺ harcamadır; 100.000 ₺ üretim maliyetine girer.",
    ["1.000.000 ₺ o yılın üretim maliyetine girer.",
     "100.000 ₺ harcamadır; 1.000.000 ₺ dönem gideridir.",
     "1.000.000 ₺ zarardır; amortisman ayrılmaz.",
     "100.000 ₺ genel yönetim gideri olarak yazılır."],
    "Makine alımı bir harcamadır ve varlık olarak aktifleşir. Makinenin yıllık kullanımını gösteren 100.000 ₺ amortisman "
    "üretimle ilgili olduğundan genel üretim giderleri aracılığıyla mamul maliyetine girer.")

# 59 — 7/A ve 7/B seçim ölçütü
P.q(R7,
    "Muhasebe Sistemi Uygulama Genel Tebliği’ne göre maliyet hesaplarını tutacak işletmeler 7/A veya 7/B seçeneklerinden "
    "birini seçmektedir. Küçük ölçekli bir üretim işletmesi, giderlerini fonksiyon esasına göre değil türlerine göre "
    "izlemeyi ve gelir tablosunu bu biçimde hazırlamayı düşünmektedir.\n\nBu işletmenin seçmesi gereken seçenek ve "
    "özelliği aşağıdakilerden hangisidir?",
    "7/B; giderler çeşit esasına göre izlenir.",
    ["7/A; giderler çeşit esasına göre izlenir.",
     "7/B; giderler fonksiyon esasına göre izlenir.",
     "7/A; gelir tablosu gider türlerine göre düzenlenir.",
     "7/B; sadece üretim giderleri izlenir."],
    "7/A seçeneği giderlerin fonksiyon esasına göre, 7/B seçeneği ise çeşit esasına göre izlenmesini öngörür; 7/B "
    "seçen işletmeler gider çeşitlerini 790-797 hesaplarında izler.")

# 60 — üretim miktarı ile birim ortalama maliyet ilişkisi
P.q("Maliyet davranışları",
    "Bir işletmenin aylık sabit maliyetleri 360.000 ₺, birim değişken maliyeti 30 ₺’dir. Üretim 9.000 birimden 12.000 "
    "birime çıkarılırsa birim toplam maliyetin nasıl değişeceği hesaplanmak istenmektedir; fiyatlar değişmeyecektir.\n\n"
    "Birim toplam maliyet ile ilgili aşağıdakilerden hangisi doğrudur?",
    "70 ₺’den 60 ₺’ye iner.",
    ["70 ₺’den 80 ₺’ye çıkar.",
     "30 ₺’de sabit kalır.",
     "40 ₺’den 30 ₺’ye iner.",
     "60 ₺’den 70 ₺’ye çıkar."],
    "Birim toplam maliyet = 30 + 360.000 / X: 9.000 birimde 30 + 40 = 70 ₺, 12.000 birimde 30 + 30 = 60 ₺. Üretim arttıkça "
    "birim sabit maliyet düştüğü için birim toplam maliyet azalır.", zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
