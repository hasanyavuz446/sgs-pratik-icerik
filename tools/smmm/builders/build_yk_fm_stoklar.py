# -*- coding: utf-8 -*-
"""Finansal Muhasebe · Stoklar — 60 soru, 2026 test biçimi.

Gerçek kitapçıklarda stok soruları alış-satış tablosu veya maliyet unsurları veren bir olayla gelir;
FIFO/ortalama maliyet, net gerçekleşebilir değer, sayım farkı ve normal kapasite hesabı sorulur, şıklar
çoğunlukla yevmiye kaydı ya da hesap-taraf-tutar biçimindedir.

Dayanak: TMS 2 Stoklar (maliyet unsurları, maliyet formülleri, NGD, kalem bazında indirim, iptal);
MSUGT Tekdüzen Hesap Planı (150-159, 197/397, 620-621, 654/644); VUK md. 274 ve 278 (maliyet bedeli,
emsal bedel). Bütün tutarlar builder içinde hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K, taraf as T, hk

P = Paket("questions_topic_finansal_stoklar_2026.json", lesson="finansal_muhasebe",
          topic="finansal_stoklar", konu_adi="Stoklar", seed=2026093062,
          surum="TMS 2 Stoklar, MSUGT Tekdüzen Hesap Planı ve VUK md. 274-278; 29.09.2026 kontrolü")

R = "TMS 2 ve MSUGT Tekdüzen Hesap Planı"
KAYIT = "Bu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?"
DOGRU = "Bu işleme ilişkin kayıt için aşağıdakilerden hangisi doğrudur?"


def fifo_kalan(partiler, kalan):
    """partiler: [(adet, birim)] en eskiden yeniye; kalan adedin FIFO değeri (en yeni partilerden)."""
    deger = 0
    for adet, birim in reversed(partiler):
        al = min(adet, kalan)
        deger += al * birim
        kalan -= al
        if not kalan:
            return deger
    raise AssertionError("yetersiz stok")


# 1 — FIFO, aralıklı envanter, dönem sonu SMM kaydı
p = [(200, 50), (300, 55), (500, 60)]
top = sum(a * b for a, b in p)                 # 56.500
ds = fifo_kalan(p, 300)                        # 18.000
smm = top - ds                                 # 38.500
ort_smm = 700 * top // 1000                    # 39.550
P.q(f"{R}: FIFO, 621/153",
    "Aralıklı envanter yöntemini ve ilk giren ilk çıkar (FIFO) maliyet formülünü uygulayan işletmenin yıl içi hareketleri "
    "şöyledir: dönem başı stok 200 adet × 50 ₺; mart alışı 300 adet × 55 ₺; eylül alışı 500 adet × 60 ₺. Yıl içinde "
    "toplam 700 adet satılmış, yıl sonu sayımında 300 adet bulunmuştur.\n\nDönem sonunda satılan malın maliyetine ilişkin "
    "günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(621, smm)], [(153, smm)]),
    [K([(621, ds)], [(153, ds)]),
     K([(621, ort_smm)], [(153, ort_smm)]),
     K([(153, smm)], [(621, smm)]),
     K([(620, smm)], [(152, smm)])],
    f"Mal mevcudu {tl(top)} ₺’dir. FIFO’da eldeki 300 adet en son alışlardan kalır: 300 × 60 = {tl(ds)} ₺. SMM "
    f"{tl(top)} − {tl(ds)} = {tl(smm)} ₺ olup 621 borç, 153 alacak yazılır. Ortalama maliyet {tl(ort_smm)} ₺ verirdi.",
    zorluk="hard")

# 2 — ağırlıklı ortalama, dönem sonu stok (sayısal)
p = [(400, 30), (600, 35), (1_000, 38)]
adet = sum(a for a, _ in p); top = sum(a * b for a, b in p)   # 2.000 adet, 71.000
ort = top / adet                                              # 35,5
kalan = 500
P.sayisal(f"{R}: ağırlıklı ortalama",
    "Dönemsel ağırlıklı ortalama maliyet formülünü kullanan işletmenin dönem başı stoku 400 adet × 30 ₺’dir. Dönem "
    "içinde 600 adet × 35 ₺ ve 1.000 adet × 38 ₺ olmak üzere iki alış yapılmış, 1.500 adet satılmıştır. Alışlarda iade "
    "veya iskonto yoktur ve dönem sonu sayımında fire saptanmamıştır.\n\nDönem sonu stokunun değeri kaç ₺’dir?",
    tl(kalan * ort), secenekler(kalan * ort, kalan * 38, kalan * 30, kalan * 35, 500 * 34.5),
    f"Ağırlıklı ortalama birim maliyet {tl(top)} / {adet} = {tl(ort)} ₺’dir. Dönem sonu stoku 500 adet × {tl(ort)} = "
    f"{tl(kalan * ort)} ₺; FIFO 500 × 38 = {tl(kalan * 38)} ₺ verirdi.", zorluk="medium")

# 3 — hareketli ortalama, satış maliyeti kaydı
a1, b1 = 100, 200          # stok
a2, b2 = 300, 240          # alış
ort = (a1 * b1 + a2 * b2) / (a1 + a2)       # 230
sat = 150
P.q(f"{R}: hareketli ortalama, 621/153",
    "Sürekli envanter ve hareketli ortalama maliyet yöntemini uygulayan işletmenin ayın başında 100 adet × 200 ₺ stoku "
    "vardır. Ayın 5’inde 300 adet × 240 ₺’den alış yapılmış, ayın 12’sinde 150 adet mal tanesi 320 ₺ + KDV’den vadeli "
    f"satılmıştır. Satış kaydı yapılmıştır.\n\n12’sindeki satışa ilişkin maliyet kaydı aşağıdakilerden hangisidir?",
    K([(621, sat * ort)], [(153, sat * ort)]),
    [K([(621, sat * b1)], [(153, sat * b1)]),
     K([(621, sat * b2)], [(153, sat * b2)]),
     K([(621, sat * 320)], [(153, sat * 320)]),
     K([(621, 100 * b1 + 50 * b2)], [(153, 100 * b1 + 50 * b2)])],
    f"Alıştan sonraki hareketli ortalama: (20.000 + 72.000) / 400 = {tl(ort)} ₺. Satılan 150 adedin maliyeti "
    f"150 × {tl(ort)} = {tl(sat * ort)} ₺ olup 621 borç, 153 alacak yazılır; FIFO {tl(100 * b1 + 50 * b2)} ₺ verirdi.")

# 4 — fiyat artışı döneminde FIFO etkisi
P.q(f"{R}: maliyet formülleri",
    "Hammadde fiyatlarının yıl boyunca sürekli arttığı bir dönemde, aynı stok hareketlerine sahip iki işletmeden biri "
    "FIFO’yu, diğeri dönemsel ağırlıklı ortalama maliyet formülünü uygulamaktadır. Satış tutarları, dönem başı stokları, "
    "alış miktarları ve alış fiyatları iki işletmede aynıdır.\n\nFIFO uygulayan işletme için aşağıdakilerden hangisi "
    "doğrudur?",
    "Dönem sonu stoku daha yüksek, brüt kârı daha yüksek çıkar.",
    ["Dönem sonu stoku daha düşük, brüt kârı daha yüksek çıkar.",
     "Satılan malın maliyeti daha yüksek, brüt kârı daha düşük çıkar.",
     "Dönem sonu stoku ve brüt kârı ortalama yöntemle aynı çıkar.",
     "Dönem sonu stoku daha yüksek, brüt kârı daha düşük çıkar."],
    "Fiyatlar artarken FIFO’da eldeki stok en son ve pahalı alışlardan oluşur; dönem sonu stoku yüksek, satılan malın "
    "maliyeti düşük olur. Satışlar aynı olduğundan brüt kâr da ortalama yönteme göre daha yüksek çıkar.")

# 5 — NGD, değer düşüklüğü
mal, sf, sm = 240_000, 230_000, 14_000
ngd = sf - sm
P.q(f"{R}: NGD, 654/158",
    f"Dönem sonunda işletmenin ambarındaki bir parti hazır giyim ürününün maliyeti {tl(mal)} ₺’dir. Moda değişimi nedeniyle "
    f"bu ürünlerin olağan faaliyet akışı içinde tahmini satış fiyatı {tl(sf)} ₺’ye inmiş, satışın gerçekleştirilmesi için "
    f"{tl(sm)} ₺ pazarlama ve nakliye gideri yapılacağı öngörülmüştür.\n\n{KAYIT}",
    K([(654, mal - ngd)], [(158, mal - ngd)]),
    [K([(654, mal - sf)], [(158, mal - sf)]),
     K([(689, mal - ngd)], [(153, mal - ngd)]),
     K([(158, mal - ngd)], [(654, mal - ngd)]),
     K([(654, mal - ngd)], [(119, mal - ngd)])],
    f"Net gerçekleşebilir değer {tl(sf)} − {tl(sm)} = {tl(ngd)} ₺’dir. Stok maliyeti ile NGD’den düşük olanla ölçülür; "
    f"{tl(mal - ngd)} ₺ indirim 654 Karşılık Giderleri borç, 158 Stok Değer Düşüklüğü Karşılığı alacak ile kaydedilir.",
    zorluk="hard")

# 6 — NGD iptali
P.q(f"{R}: iptal, 158/644",
    "Geçen yıl sonunda maliyeti 180.000 ₺ olan ürünler için 25.000 ₺ stok değer düşüklüğü karşılığı ayrılmıştır. Bu yıl "
    "sonunda ürünlerin tamamı hâlâ ambardadır; fiyatların toparlanmasıyla NGD 170.000 ₺ olarak hesaplanmıştır. Önceki "
    "indirimin iptali, başlangıçtaki indirim tutarıyla sınırlıdır.\n\nBu durumda yapılacak kayıt için aşağıdakilerden "
    "hangisi doğrudur?",
    T(644, "alacak", 15_000),
    [T(644, "alacak", 25_000), T(153, "borç", 15_000), T(654, "alacak", 15_000), T(158, "alacak", 10_000)],
    "Yeni NGD’ye göre gereken indirim 180.000 − 170.000 = 10.000 ₺’dir; mevcut karşılık 25.000 ₺ olduğundan 15.000 ₺ "
    "iptal edilir: 158 borç, 644 Konusu Kalmayan Karşılıklar alacak. İptal önceki indirimi aşamaz.", zorluk="hard")

# 7 — maliyete girmeyen unsurlar (olumsuz)
P.q(f"{R}: maliyet unsurları",
    "Mobilya üreten işletme dönem içinde şu harcamaları yapmıştır: kereste alış bedeli, kerestenin fabrikaya taşınması, "
    "üretimde çalışan işçilerin ücretleri, fabrika binasının amortismanı ve bitmiş ürünlerin satış mağazasına sevki için "
    "ödenen nakliye bedeli.\n\nBu harcamalardan hangisi stok maliyetine dâhil edilmez?",
    "Bitmiş ürünlerin mağazaya sevki için ödenen nakliye",
    ["Kerestenin fabrikaya getirilmesi için ödenen taşıma",
     "Üretim hattındaki işçilere ödenen ücretler",
     "Fabrika binası için ayrılan amortisman payı",
     "Kereste alışı için satıcıya ödenen bedel"],
    "Stok maliyeti satın alma, dönüştürme ve stokları mevcut konum ve durumuna getirmek için katlanılan diğer maliyetlerden "
    "oluşur. Bitmiş ürünün satış yerine sevki satış gideridir, oluştuğu dönemde gider yazılır.")

# 8 — anormal fire
P.q(f"{R}: anormal fire",
    "Bir gıda üreticisinde normal fire oranı %2’dir. Dönem içinde üretime alınan 50.000 kg hammaddenin 1.000 kg’ı normal "
    "fire olarak, soğutma sistemindeki arıza yüzünden ayrıca 1.500 kg’ı bozularak kullanılamaz hâle gelmiştir. Bozulan "
    "hammaddenin maliyeti 60.000 ₺’dir.\n\nBozulan hammaddenin maliyeti için aşağıdakilerden hangisi doğrudur?",
    "Dönem gideri olarak kaydedilir.",
    ["Mamul maliyetine eklenerek stoka alınır.",
     "Gelecek yıllara ait gider olarak ertelenir.",
     "Normal fireyle birlikte birim maliyete yayılır.",
     "Hammadde stokunda maliyet olarak bırakılır."],
    "Normal fire (1.000 kg) üretim maliyetinin parçasıdır. Arızadan doğan anormal tutardaki kayıp stok maliyetine dâhil "
    "edilmez, oluştuğu dönemde gider olarak kaydedilir.")

# 9 — sayım noksanı, stok
P.q(f"{R}: 197/153",
    "Yıl sonu stok sayımında ticari mal kayıtlarında 12.400 ₺ tutarında görünen bir ürün grubundan ambarda 11.200 ₺’lik "
    "mal bulunmuştur. Farkın hırsızlık, kayıt hatası veya teslim eksikliğinden hangisinden doğduğu henüz "
    f"araştırılmaktadır.\n\n{KAYIT}",
    K([(197, 1_200)], [(153, 1_200)]),
    [K([(153, 1_200)], [(397, 1_200)]),
     K([(689, 1_200)], [(153, 1_200)]),
     K([(621, 1_200)], [(153, 1_200)]),
     K([(197, 1_200)], [(100, 1_200)])],
    "Kayıtlı stok 12.400 ₺, fiilî mevcut 11.200 ₺ olduğundan 1.200 ₺ noksan vardır. Neden belirleninceye kadar 197 Sayım "
    "ve Tesellüm Noksanları borç, 153 Ticari Mallar alacak yazılır; neden anlaşılınca ilgili hesaba aktarılır.")

# 10 — sayım fazlası, stok
P.q(f"{R}: 153/397",
    "Hırdavat ticareti yapan işletmenin yıl sonu sayımında bir ürün grubunda kayıtlarda bulunmayan 40 adet mal tespit "
    "edilmiştir. Malların birim maliyeti 85 ₺ olup fazlalığın bir alış iadesinin yanlış kaydından doğup doğmadığı henüz "
    f"belirlenememiştir.\n\n{DOGRU}",
    T(397, "alacak", 3_400),
    [T(679, "alacak", 3_400), T(153, "alacak", 3_400), T(197, "alacak", 3_400), T(621, "alacak", 3_400)],
    "Fazlalık 40 × 85 = 3.400 ₺’dir. Nedeni araştırılırken 153 Ticari Mallar borç, 397 Sayım ve Tesellüm Fazlaları alacak "
    "yazılır; dönem sonuna kadar neden bulunamazsa 679 hesabına aktarılır.")

# 11 — normal fire kararı
P.q(f"{R}: 621/197",
    "Önceki ay stok sayımında bulunan ve 197 Sayım ve Tesellüm Noksanları hesabına alınan 2.600 ₺’lik farkın, yapılan "
    "incelemede ürünlerin doğal nem kaybından kaynaklanan ve sektör oranları içinde kalan normal fire olduğu anlaşılmıştır. "
    f"İşletme normal fireleri satılan malın maliyetinde izlemektedir.\n\n{KAYIT}",
    K([(621, 2_600)], [(197, 2_600)]),
    [K([(689, 2_600)], [(197, 2_600)]),
     K([(197, 2_600)], [(153, 2_600)]),
     K([(621, 2_600)], [(153, 2_600)]),
     K([(135, 2_600)], [(197, 2_600)])],
    "Normal fire maliyet unsurudur ve işletmenin politikasına göre 621 Satılan Ticari Mallar Maliyeti hesabına aktarılır; "
    "197 hesabı alacaklandırılarak kapatılır. 153 sayım tarihinde zaten alacaklandırılmıştır.")

# 12 — aralıklı envanter SMM formülü (tablo)
db, al, iad, isk, ds = 85_000, 420_000, 12_000, 8_000, 96_000
smm = db + al - iad - isk - ds
P.q(f"{R}: aralıklı envanter",
    "Aralıklı envanter yöntemini uygulayan işletmenin ticari mallarına ilişkin yıllık bilgiler şöyledir:\n\n"
    f"| Kalem | Tutar (₺) |\n|---|---|\n| Dönem başı stok | {tl(db)} |\n| Dönem içi alışlar | {tl(al)} |\n"
    f"| Alıştan iadeler | {tl(iad)} |\n| Alış iskontoları | {tl(isk)} |\n| Dönem sonu sayım stoku | {tl(ds)} |\n\n"
    "Satılan ticari mallar maliyeti için yapılacak kayıtta aşağıdakilerden hangisi doğrudur?",
    T(621, "borç", smm),
    [T(621, "borç", db + al - ds), T(621, "borç", al - iad - isk), T(153, "alacak", db + al - iad - isk),
     T(621, "borç", db + al + iad + isk - ds)],
    f"SMM = dönem başı + alışlar − iadeler − iskontolar − dönem sonu = {tl(db)} + {tl(al)} − {tl(iad)} − {tl(isk)} − "
    f"{tl(ds)} = {tl(smm)} ₺; 621 borç, 153 alacak yazılır.")

# 13 — ithalatta maliyet
fob, nav, sig, gv, ard = 500_000, 30_000, 5_000, 53_500, 12_000
maliyet = fob + nav + sig + gv + ard
P.sayisal(f"{R}: satın alma maliyeti",
    f"İşletme yurt dışından ticari mal ithal etmiştir. Malların FOB bedeli {tl(fob)} ₺, navlun {tl(nav)} ₺, taşıma "
    f"sigortası {tl(sig)} ₺, gümrük vergisi {tl(gv)} ₺, gümrükten depoya taşıma {tl(ard)} ₺’dir. İthalde ödenen KDV "
    "indirilecek, mallar ambara girdikten sonra ayrıca 4.000 ₺ depolama gideri yapılmıştır.\n\nMalların stok maliyeti "
    "kaç ₺’dir?",
    tl(maliyet), secenekler(maliyet, fob + nav + sig, maliyet + 4_000, fob + nav + sig + gv, maliyet + (fob + nav + sig + gv) // 5),
    f"Satın alma maliyeti alış bedeli, ithalat vergileri ve malın ambara gelmesine kadarki taşıma-sigorta giderlerinden "
    f"oluşur: {tl(fob)} + {tl(nav)} + {tl(sig)} + {tl(gv)} + {tl(ard)} = {tl(maliyet)} ₺. Sonraki depolama gideri ve "
    "indirilecek KDV maliyete girmez.", zorluk="medium")

# 14 — normal kapasite, sabit GÜG
sabit, nk, fiili = 900_000, 30_000, 24_000
birim = sabit // nk
P.q(f"{R}: normal kapasite",
    f"Tek ürün üreten işletmenin yıllık sabit genel üretim giderleri {tl(sabit)} ₺, normal üretim kapasitesi 30.000 "
    f"birimdir. Talep daralması nedeniyle yıl içinde 24.000 birim üretilmiştir. Değişken giderler üretim miktarına göre "
    f"yüklenmektedir.\n\nSabit genel üretim giderlerinin muhasebeleştirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    f"{tl(fiili * birim)} ₺ mamul maliyetine, {tl(sabit - fiili * birim)} ₺ dönem giderine yazılır.",
    [f"{tl(sabit)} ₺ tamamı mamul maliyetine yüklenir.",
     f"{tl(sabit)} ₺ tamamı oluştuğu dönemde gider yazılır.",
     f"{tl(sabit - fiili * birim)} ₺ mamul maliyetine, {tl(fiili * birim)} ₺ dönem giderine yazılır.",
     f"{tl(fiili * birim)} ₺ mamul maliyetine, {tl(sabit - fiili * birim)} ₺ gelecek dönemlere ertelenir."],
    f"Sabit GÜG normal kapasiteye göre dağıtılır: birim başına {tl(sabit)} / 30.000 = {birim} ₺. Üretilen 24.000 birime "
    f"{tl(fiili * birim)} ₺ yüklenir; kullanılmayan kapasiteye düşen {tl(sabit - fiili * birim)} ₺ dönem gideri olur.",
    zorluk="hard")

# 15 — hammadde kullanımı
P.q(f"{R}: 710/150",
    "Üretim işletmesi ay içinde ambardan üretim bölümüne malzeme çıkış fişiyle 160.000 ₺’lik direkt hammadde, 18.000 ₺’lik "
    "yardımcı malzeme göndermiştir. İşletme 7/A seçeneğini uygulamakta, yardımcı malzemeyi genel üretim gideri olarak "
    "izlemektedir.\n\nBu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(710, 160_000), (730, 18_000)], [(150, 178_000)]),
    [K([(710, 178_000)], [(150, 178_000)]),
     K([(151, 160_000), (730, 18_000)], [(150, 178_000)]),
     K([(710, 160_000), (770, 18_000)], [(150, 178_000)]),
     K([(150, 178_000)], [(710, 160_000), (730, 18_000)])],
    "7/A’da doğrudan üretime giren hammadde 710 Direkt İlk Madde ve Malzeme Giderleri, yardımcı malzeme 730 Genel Üretim "
    "Giderleri hesabına borç; 150 İlk Madde ve Malzeme 178.000 ₺ alacak yazılır.")

# 16 — mamul tamamlanması ve satış maliyeti (taraf)
P.q(f"{R}: 152/151, 620/152",
    "Üretim işletmesinde ay içinde tamamlanan 2.000 adet mamulün üretim maliyeti 151 Yarı Mamuller – Üretim hesabında "
    "360.000 ₺ olarak birikmiştir. Tamamlanan mamuller ambara alınmış ve aynı ay bunların 1.500 adedi tanesi 260 ₺ + KDV "
    "fiyatla satılmıştır. İşletme sürekli envanter yöntemini uygulamaktadır.\n\nSatışa ilişkin maliyet kaydında "
    "aşağıdakilerden hangisi doğrudur?",
    T(620, "borç", 270_000),
    [T(621, "borç", 270_000), T(620, "borç", 390_000), T(152, "borç", 270_000), T(151, "alacak", 270_000)],
    "Birim maliyet 360.000 / 2.000 = 180 ₺’dir. Satılan 1.500 adet mamulün maliyeti 270.000 ₺ olup 620 Satılan Mamuller "
    "Maliyeti borç, 152 Mamuller alacak yazılır. 621 ticari malların maliyetini izler.")

# 17 — konsinye mallar
P.q(f"{R}: konsinye",
    "Elektronik ürün üreticisi, bir perakendeciyle yaptığı konsinye satış sözleşmesi uyarınca 400.000 ₺ maliyetli ürünleri "
    "perakendecinin mağazasına göndermiştir. Perakendeci ürünleri sattıkça üreticiye bildirecek ve komisyonunu düşerek "
    "bedeli aktaracaktır; satılmayan ürünler iade edilebilecektir.\n\nDönem sonunda perakendecinin mağazasında satılmadan "
    "duran ürünler için aşağıdakilerden hangisi doğrudur?",
    "Üreticinin stoklarında yer alır.",
    ["Perakendecinin stoklarında yer alır.",
     "Üreticinin satılan malın maliyetine aktarılır.",
     "Perakendeciden alacak olarak izlenir.",
     "Taraflar arasında yarı yarıya paylaştırılır."],
    "Konsinye gönderimde kontrol ve önemli riskler ürün satılana kadar gönderende kalır; ürünler üreticinin stoklarında "
    "(ayrı alt hesapta) izlenir ve hasılat son müşteriye satışta kaydedilir.", zorluk="easy")

# 18 — yoldaki mallar, teslim şekli
P.q(f"{R}: yoldaki mallar",
    "İşletme 28 Aralık’ta yurt içindeki bir tedarikçiden 150.000 ₺’lik ticari mal satın almıştır. Sözleşmeye göre mülkiyet ve "
    "hasar malın tedarikçinin deposunda taşıyıcıya tesliminde alıcıya geçmektedir. Mallar 29 Aralık’ta taşıyıcıya teslim "
    "edilmiş, işletmenin deposuna 3 Ocak’ta ulaşmıştır.\n\n31 Aralık tarihli finansal tablolar için aşağıdakilerden "
    "hangisi doğrudur?",
    "Mallar alıcı işletmenin stoklarına dâhil edilir.",
    ["Mallar tedarikçinin stoklarında gösterilir.",
     "Mallar depoya ulaşınca kayda alınır.",
     "Bedel ödenene kadar stoklara alınmaz.",
     "Mallar sadece dipnotta açıklanır."],
    "Kontrol taşıyıcıya teslimde alıcıya geçtiğinden, 31 Aralık’ta yolda olan mallar alıcının stokudur ve 150.000 ₺ "
    "borçla birlikte kayda alınır; malın fiziksel olarak depoya ulaşması beklenmez.")

# 19 — kalem bazında NGD (tablo)
kal = [("Ürün X", 60_000, 72_000), ("Ürün Y", 45_000, 38_000), ("Ürün Z", 30_000, 26_500)]
ind = sum(max(0, m - n) for _, m, n in kal)          # 7.000 + 3.500 = 10.500
top_m = sum(m for _, m, _ in kal); top_n = sum(n for _, _, n in kal)
tablo = "| Kalem | Maliyet (₺) | NGD (₺) |\n|---|---|---|\n" + "\n".join(f"| {a} | {tl(m)} | {tl(n)} |" for a, m, n in kal)
P.q(f"{R}: kalem bazında indirim",
    "Birbirinden farklı nitelikte üç ürün grubu satan işletmenin yıl sonu stok bilgileri aşağıdadır:\n\n" + tablo +
    "\n\nStokların net gerçekleşebilir değere indirgenmesi için yapılacak kayıtta aşağıdakilerden hangisi doğrudur?",
    T(158, "alacak", ind),
    [T(158, "alacak", ind + 5_000), T(654, "borç", 3_500), T(153, "alacak", ind),
     T(654, "borç", 7_000)],
    f"İndirim kalem bazında yapılır: Y için 7.000 ₺, Z için 3.500 ₺; X’in NGD’si maliyetinin üstünde olduğundan artış "
    f"kaydedilmez. Toplam {tl(ind)} ₺ 654 borç, 158 alacak yazılır. Toplam bazda ({tl(top_m)} ₺ maliyet, {tl(top_n)} ₺ "
    "NGD) bakılsaydı X’teki değer artışı diğer kalemlerdeki kaybı gizlerdi.", zorluk="hard")

# 20 — LIFO (olumsuz)
P.q("TMS 2 md. 23-27",
    "Farklı ürün grupları bulunan bir işletme, TMS 2 Stoklar standardını uygulayarak maliyet formülü seçimi yapacaktır. "
    "Bazı ürünler birbirinin yerine kullanılabilir nitelikte, bazıları ise belirli projeler için özel olarak sipariş "
    "edilmiş ve birbirinden ayırt edilebilir durumdadır.\n\nAşağıdaki maliyet belirleme yöntemlerinden hangisi bu "
    "işletme tarafından kullanılamaz?",
    "Son giren ilk çıkar (LIFO)",
    ["İlk giren ilk çıkar (FIFO)", "Ağırlıklı ortalama maliyet", "Özel tanımlama yöntemi", "Hareketli ortalama maliyet"],
    "TMS 2 özel projeler için ayrılmış ve birbirinin yerine geçemeyen kalemlerde özel tanımlamayı, diğerlerinde FIFO veya "
    "ağırlıklı ortalamayı (hareketli ortalama dâhil) öngörür; LIFO standartta yer almaz.", zorluk="easy")

# 21 — yangın, sigorta tazmini
mal, taz = 320_000, 250_000
P.q(f"{R}: 136, 689, 153",
    f"Deposunda yangın çıkan işletmenin maliyeti {tl(mal)} ₺ olan ticari malları tamamen yanmıştır. Sigorta şirketi "
    f"ekspertiz raporuna göre {tl(taz)} ₺ tazminat ödemeyi kabul etmiş ancak tutarı henüz ödememiştir. Yanan mallar "
    f"için KDV düzeltmesi bu soruda dikkate alınmayacaktır.\n\n{KAYIT}",
    K([(136, taz), (689, mal - taz)], [(153, mal)]),
    [K([(136, taz), (659, mal - taz)], [(153, mal)]),
     K([(689, mal)], [(153, mal)]),
     K([(136, mal)], [(153, taz), (679, mal - taz)]),
     K([(120, taz), (689, mal - taz)], [(153, mal)])],
    f"Yanan mallar 153’ten çıkarılır. Sigortadan alınacak {tl(taz)} ₺ 136 Diğer Çeşitli Alacaklar hesabına, "
    f"karşılanmayan {tl(mal - taz)} ₺ olağandışı kayıp olarak 689 Diğer Olağandışı Gider ve Zararlar hesabına borç yazılır.",
    zorluk="hard")

# 22 — brüt kâr yöntemiyle stok tahmini
db, al, sat, oran = 140_000, 610_000, 800_000, 0.25
tahmin = db + al - sat * (1 - oran)
P.q(f"{R}: brüt kâr yöntemi",
    f"Ambarı su baskınına uğrayan işletmenin baskın tarihine kadarki kayıtlarına göre dönem başı stoku {tl(db)} ₺, "
    f"alışları {tl(al)} ₺, net satışları {tl(sat)} ₺’dir. İşletmenin geçmiş yıllardaki brüt kâr oranı satışların %25’i "
    "olarak istikrarlıdır ve sigorta şirketi kaybı bu yöntemle tahmin etmektedir.\n\nBaskın tarihinde ambarda bulunması "
    "gereken stokun tahmini maliyeti ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Satılan malın tahmini maliyeti {tl(sat * (1 - oran))} ₺, stok {tl(tahmin)} ₺’dir.",
    [f"Satılan malın tahmini maliyeti {tl(sat * oran)} ₺, stok {tl(db + al - sat * oran)} ₺’dir.",
     f"Satılan malın tahmini maliyeti {tl(sat / (1 + oran))} ₺, stok {tl(db + al - sat / (1 + oran))} ₺’dir.",
     f"Satılan malın tahmini maliyeti {tl(sat * 0.7)} ₺, stok {tl(db + al - sat * 0.7)} ₺’dir.",
     f"Satılan malın tahmini maliyeti {tl(al)} ₺, stok {tl(db)} ₺’dir."],
    f"Brüt kâr oranı satışların %25’i ise SMM satışların %75’idir: {tl(sat)} × 0,75 = {tl(sat * (1 - oran))} ₺. Tahmini "
    f"stok {tl(db)} + {tl(al)} − {tl(sat * (1 - oran))} = {tl(tahmin)} ₺’dir.", zorluk="hard")

# 23 — dönem sonu stok hatası etkisi
P.q(f"{R}: stok hatası",
    "Bir işletme 2025 yıl sonu sayımında bir depoyu yanlışlıkla iki kez saymış ve dönem sonu stokunu 90.000 ₺ fazla "
    "göstermiştir. Hata 2026 yılı kapanışında fark edilmiştir; 2026 yılı sonu stoku doğru sayılmıştır. Vergi etkisi "
    "dikkate alınmayacaktır.\n\nBu hatanın düzeltilmemiş hâliyle etkisi için aşağıdakilerden hangisi doğrudur?",
    "2025 kârı 90.000 ₺ fazla, 2026 kârı 90.000 ₺ eksiktir.",
    ["2025 kârı 90.000 ₺ eksik, 2026 kârı 90.000 ₺ fazladır.",
     "2025 ve 2026 kârları 90.000 ₺ fazladır.",
     "2025 kârı 90.000 ₺ fazla, 2026 kârı doğrudur.",
     "Sadece 2025 bilançosundaki stok etkilenir."],
    "Dönem sonu stokunun fazla gösterilmesi 2025 SMM’sini düşürüp kârı artırır. Bu stok 2026’nın dönem başı stoku olduğundan "
    "2026 SMM’si artar ve kâr aynı tutarda azalır; iki yıl toplamında hata kendini dengeler.")

# 24 — ticari malın demirbaş olarak kullanılması
P.q(f"{R}: 255/153",
    "Bilgisayar satan işletme, satış amacıyla aldığı ve stok kartlarında maliyeti 38.000 ₺ görünen bir dizüstü "
    "bilgisayarı muhasebe bölümünde kullanılmak üzere ambardan çıkarmıştır. Bilgisayar birkaç yıl kullanılacak ve "
    f"amortismana tabi tutulacaktır.\n\n{KAYIT}",
    K([(255, 38_000)], [(153, 38_000)]),
    [K([(770, 38_000)], [(153, 38_000)]),
     K([(255, 38_000)], [(600, 38_000)]),
     K([(253, 38_000)], [(153, 38_000)]),
     K([(621, 38_000)], [(153, 38_000)])],
    "Satış amacı ortadan kalkan ve bir yıldan fazla kullanılacak mal duran varlığa sınıflandırılır: 255 Demirbaşlar borç, "
    "153 Ticari Mallar alacak, maliyet bedeliyle. Satış gerçekleşmediğinden hasılat kaydı yapılmaz.")

# 25 — satıştan iade, sürekli envanter maliyet düzeltmesi
P.q(f"{R}: 153/621",
    "Sürekli envanter yöntemini uygulayan işletme, geçen hafta 50.000 ₺ + KDV’ye sattığı ve maliyeti 34.000 ₺ olan "
    "malların tamamının kusurlu olduğu gerekçesiyle müşteri tarafından iade edildiğini kaydetmektedir. Satış iadesi ve KDV "
    "kaydı yapılmıştır.\n\nİade edilen malların maliyetine ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(153, 34_000)], [(621, 34_000)]),
    [K([(621, 34_000)], [(153, 34_000)]),
     K([(153, 50_000)], [(621, 50_000)]),
     K([(153, 34_000)], [(610, 34_000)]),
     K([(157, 34_000)], [(621, 34_000)])],
    "Satışta 621 borç, 153 alacak yazılmıştı. İadeyle mal yeniden stoka girer; maliyet tutarıyla (34.000 ₺) 153 borç, "
    "621 alacak kaydedilir. Satış tutarındaki iade 610’da ayrıca izlenir.")

# 26 — perakende yöntemi
P.q("TMS 2 md. 21-22",
    "Yüzlerce farklı ürün satan ve ürünlerin kâr marjları birbirine yakın olan bir süpermarket zinciri, her ürün için "
    "ayrı maliyet takibinin pratik olmadığını düşünmektedir. Zincir, stokları satış fiyatı üzerinden uygun brüt kâr yüzdesi "
    "düşülerek ölçmeyi değerlendirmektedir.\n\nBu ölçüm tekniğiyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Sonuçlar maliyete yaklaşıyorsa kullanılabilir.",
    ["Perakendecilerde kullanılması yasaktır.",
     "Stoklar satış fiyatıyla raporlanır.",
     "Ortalama marj değil en yüksek marj kullanılır.",
     "Maliyet formülü seçimini gereksiz kılar ve NGD testi yapılmaz."],
    "Standart maliyet ve perakende yöntemi gibi teknikler sonuçları maliyete yaklaşıyorsa kolaylık için kullanılabilir. "
    "Perakende yönteminde stok satış değerinden uygun brüt kâr yüzdesi indirilerek bulunur; NGD testi yine uygulanır.")

# 27 — depolama gideri
P.q(f"{R}: maliyete girmeyen",
    "Şarap üreticisi dönem içinde şu giderlere katlanmıştır: olgunlaşma süresince fıçılarda bekletilen şarabın mahzen "
    "giderleri, bitmiş ve şişelenmiş ürünlerin satış deposunda bekletilmesine ilişkin kira ve üretim yönetimi dışındaki "
    "genel yönetim giderleri.\n\nAşağıdakilerden hangisi stok maliyetine dâhil edilir?",
    "Olgunlaşma aşamasındaki mahzen giderleri",
    ["Bitmiş ürünlerin satış deposu kirası",
     "Merkez ofis yönetim giderleri",
     "Satış personelinin ücretleri",
     "Bayilere yapılan tanıtım giderleri"],
    "Depolama giderleri, bir üretim aşamasından diğerine geçmeden önce üretim süreci için gerekliyse (olgunlaşma gibi) "
    "stok maliyetine girer. Bitmiş ürün depolama, genel yönetim ve satış giderleri dönem gideridir.")

# 28 — üretim miktarı ve yarı mamul hesabı (hesap)
P.q(f"{R}: stok hesapları",
    "Tekstil üreticisinin ambarında dönem sonunda şunlar bulunmaktadır: satın alınmış ham pamuk ipliği, dokuma "
    "tezgâhında işlemi yarım kalmış kumaş topları, satışa hazır paketlenmiş havlu setleri ve paketlemede kullanılacak "
    "karton kutular.\n\nİşlemi yarım kalmış kumaş toplarının izlendiği hesap aşağıdakilerden hangisidir?",
    hk(151), [hk(150), hk(152), hk(157), hk(153)],
    "Üretim süreci tamamlanmamış ürünler 151 Yarı Mamuller – Üretim hesabında izlenir. İplik ve karton kutu 150, satışa "
    "hazır havlu setleri 152 Mamuller hesabındadır.", zorluk="easy")

# 29 — alış iskontosu sonradan, mal kısmen satılmış
alis, isk = 200_000, 10_000
P.q(f"{R}: alış iskontosu",
    f"İşletme {tl(alis)} ₺ + KDV’ye aldığı malların yarısını satmışken satıcıdan, toplam alış bedelinin %5’i oranında "
    f"{tl(isk)} ₺ + %20 KDV ciro iskontosu faturası almıştır. Sürekli envanter uygulanmakta, iskontonun kalan ve satılan "
    f"mallar arasında oranlı dağıtılması benimsenmektedir.\n\n{DOGRU}",
    T(621, "alacak", isk // 2),
    [T(153, "alacak", isk), T(649, "alacak", isk), T(611, "alacak", isk // 2), T(191, "alacak", isk)],
    f"İskonto stok maliyetini azaltır. Mallar yarı yarıya satıldığından {tl(isk // 2)} ₺ 153’ten, {tl(isk // 2)} ₺ "
    f"621’den düşülür; KDV düzeltmesi 191 alacak {tl(isk // 5)} ₺ olur. Satıcıya borç 320 borç ile azalır.", zorluk="hard")

# 30 — VUK maliyet bedeli / emsal bedel
P.q("VUK md. 274 ve 278",
    "Vergi Usul Kanunu’na göre değerleme yapan bir ticaret işletmesinin deposundaki malların bir kısmı yangın nedeniyle "
    "ciddi hasar görmüş ve satış bedelleri maliyetlerinin önemli ölçüde altına düşmüştür. İşletme bu mallar için değer "
    "düşüklüğünü vergi matrahında dikkate almak istemektedir.\n\nBu durumda aşağıdakilerden hangisi doğrudur?",
    "Mallar emsal bedelle değerlenebilir.",
    ["Mallar maliyet bedeliyle değerlenmeye devam eder.",
     "Mallar satış bedeliyle kayıttan çıkarılır.",
     "Mallar yıl sonunda değerlemeye tabi tutulmaz.",
     "Değer düşüklüğü gelecek yıla ertelenir."],
    "VUK md. 274’e göre emtia maliyet bedeliyle değerlenir; ancak yangın, deprem, su basması gibi afetler veya bozulma "
    "nedeniyle kıymeti önemli ölçüde düşen emtia md. 278 uyarınca emsal bedelle değerlenebilir.")

# 31 — standart maliyet farkı / birim maliyet üretim
P.sayisal(f"{R}: birim maliyet",
    "Üretim işletmesinde ay içinde 5.000 birim ürün tamamlanmış, dönem başı ve dönem sonu yarı mamul bulunmamaktadır. Ay "
    "içinde direkt hammadde 240.000 ₺, direkt işçilik 110.000 ₺, değişken genel üretim gideri 50.000 ₺ oluşmuştur. Sabit "
    "genel üretim gideri 120.000 ₺ olup normal kapasite 6.000 birimdir.\n\nTamamlanan ürünlerin birim maliyeti kaç ₺’dir?",
    tl(100), secenekler(100, 104, 80, 96, 90),
    "Sabit GÜG normal kapasiteye göre yüklenir: 120.000 / 6.000 = 20 ₺/birim, 5.000 birime 100.000 ₺. Toplam maliyet "
    "240.000 + 110.000 + 50.000 + 100.000 = 500.000 ₺; birim maliyet 500.000 / 5.000 = 100 ₺. Kalan 20.000 ₺ gider olur.",
    zorluk="hard")

# 32 — hammadde alımı
P.q(f"{R}: 150/191/320",
    "Üretim işletmesi 12 ton çelik levhayı tonu 30.000 ₺ + %20 KDV’den vadeli satın almıştır. Levhaların fabrikaya "
    "taşınması için nakliye firmasına 9.000 ₺ + %20 KDV peşin ödenmiş, levhalar ilk madde ambarına alınmıştır.\n\n"
    "Bu işlemlere ilişkin tek bir günlük defter kaydı yapılırsa kayıt aşağıdakilerden hangisidir?",
    K([(150, 369_000), (191, 73_800)], [(320, 432_000), (100, 10_800)]),
    [K([(150, 360_000), (760, 9_000), (191, 73_800)], [(320, 432_000), (100, 10_800)]),
     K([(153, 369_000), (191, 73_800)], [(320, 432_000), (100, 10_800)]),
     K([(150, 369_000), (191, 73_800)], [(320, 442_800)]),
     K([(150, 442_800)], [(320, 432_000), (100, 10_800)])],
    "Hammadde maliyeti alış bedeli ile taşıma giderinden oluşur: 360.000 + 9.000 = 369.000 ₺ (150). KDV 72.000 + 1.800 "
    "= 73.800 ₺ 191’e yazılır; satıcıya 432.000 ₺ borç, nakliyeciye 10.800 ₺ peşin ödeme yapılır.")

# 33 — stok değer düşüklüğünün sunumu (hesap türü)
P.q(f"{R}: 158",
    "Dönem sonunda stokları için değer düşüklüğü karşılığı ayıran işletme, bilançosunu hazırlamaktadır. Stoklar hesap "
    "grubunda ticari mallar 820.000 ₺, 158 Stok Değer Düşüklüğü Karşılığı hesabı 45.000 ₺ bakiye vermektedir.\n\nBu "
    "karşılık hesabının bilançoda gösterimiyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Stoklar grubunda indirim olarak gösterilir.",
    ["Kısa vadeli borç karşılıkları arasında gösterilir.",
     "Özkaynaklarda ayrı kalem olarak gösterilir.",
     "Duran varlıklarda eksi bakiye olarak gösterilir.",
     "Gelir tablosunda satışlardan düşülür."],
    "158 Stok Değer Düşüklüğü Karşılığı düzenleyici (pasif karakterli) bir aktif hesaptır; stoklar grubunda eksi olarak "
    "gösterilir ve net stok 820.000 − 45.000 = 775.000 ₺ olur.", zorluk="easy")

# 34 — FIFO sürekli envanter, ikinci satış
# 10’unda 150 adet satış: 100 × 40 + 50 × 44; elde 150 × 44 kalır. 18’inde 100 × 50 alış, 25’inde 180 adet satış.
sat2 = 150 * 44 + 30 * 50
P.q(f"{R}: FIFO sürekli envanter",
    "FIFO ve sürekli envanter uygulayan işletmenin ay başı stoku 100 adet × 40 ₺’dir. 3’ünde 200 adet × 44 ₺ alış, "
    "10’unda 150 adet satış, 18’inde 100 adet × 50 ₺ alış ve 25’inde 180 adet satış yapılmıştır. Satışlar tanesi 70 ₺ "
    "+ KDV’dendir.\n\n25’indeki satışın maliyet kaydında aşağıdakilerden hangisi doğrudur?",
    T(621, "borç", sat2),
    [T(621, "borç", 180 * 44), T(621, "borç", 100 * 50 + 80 * 44), T(621, "borç", 180 * 70), T(153, "borç", sat2)],
    "10’undaki satış 100 × 40 + 50 × 44 ile karşılanır; elde 150 × 44 kalır. 25’indeki 180 adet önce bu 150 adetten "
    f"(6.600 ₺), kalan 30 adet 50 ₺’lik partiden (1.500 ₺) çıkar: {tl(sat2)} ₺ 621 borç, 153 alacak.", zorluk="hard")

# 35 — stok maliyetine borçlanma maliyeti (özellikli varlık değil)
P.q("TMS 2 md. 17 ve TMS 23",
    "Toptan gıda satan işletme, rutin olarak kısa sürede satın alıp sattığı ürünlerin alımını finanse etmek için "
    "kullandığı banka kredisine dönem içinde 85.000 ₺ faiz ödemiştir. Ürünler satın alındıktan sonra birkaç hafta içinde "
    "satılmaktadır.\n\nBu faiz tutarının muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Finansman gideri olarak dönem sonucuna yansıtılır.",
    ["Ticari malların maliyetine eklenir.",
     "Özellikli varlık olarak aktifleştirilir.",
     "Gelecek aylara ait gider olarak ertelenir.",
     "Satış iskontosu olarak satışlardan düşülür."],
    "Kısa sürede rutin olarak üretilen veya alınan stoklar özellikli varlık değildir; bunların finansmanına ilişkin faiz "
    "stok maliyetine eklenmez, 780 Finansman Giderleri üzerinden dönem sonucuna yansır.")

# 36 — ambalaj malzemesi hesabı
P.q(f"{R}: 150",
    "Deterjan üreticisi, ürünlerini doldurduğu plastik şişeleri ve etiketleri bir tedarikçiden 84.000 ₺ + KDV’ye satın "
    "almıştır. Şişe ve etiketler üretim sürecinde ürünün bir parçası olarak kullanılacak, ürünle birlikte satılacaktır."
    "\n\nBu alımda borçlandırılacak stok hesabı aşağıdakilerden hangisidir?",
    hk(150), [hk(730), hk(151), hk(710), hk(159)],
    "Üretimde kullanılmak üzere alınan hammadde, yardımcı madde, işletme malzemesi ve ambalaj malzemesi 150 İlk Madde ve "
    "Malzeme hesabında izlenir; kullanıldıkça 710 veya 730’a aktarılır. 151 üretimdeki yarı mamulleri, 159 verilen "
    "sipariş avanslarını izler.", zorluk="easy")

# 37 — sayım noksanı kasiyer değil depo sorumlusu (taraf)
P.q(f"{R}: 197/135",
    "Stok sayımında belirlenip 197 hesabına alınan 7.500 ₺’lik ticari mal noksanlığının, depo sorumlusunun ihmali "
    "sonucu çalınan mallardan kaynaklandığı anlaşılmıştır. Sorumlu tutarı iki ay içinde işletmeye ödemeyi kabul etmiş, "
    f"bu yönde bir taahhütname imzalamıştır.\n\n{DOGRU}",
    T(135, "borç", 7_500),
    [T(689, "borç", 7_500), T(153, "alacak", 7_500), T(621, "borç", 7_500), T(196, "borç", 7_500)],
    "Sorumludan tahsil edilecek tutar 135 Personelden Alacaklar hesabına borç, 197 Sayım ve Tesellüm Noksanları hesabına "
    "alacak yazılır. Stok sayım tarihinde zaten azaltılmıştır.")

# 38 — ağırlıklı ortalama SMM, satış iadeli (sayısal değil: kayıt)
p = [(1_000, 12), (3_000, 15)]
adet = 4_000; top = 1_000 * 12 + 3_000 * 15      # 57.000 → 14,25
satilan = 3_200 - 200                              # 200 iade
P.q(f"{R}: ağırlıklı ortalama SMM",
    "Dönemsel ağırlıklı ortalama maliyet ve aralıklı envanter uygulayan işletmenin dönem başı stoku 1.000 adet × 12 ₺, "
    "dönem içi alışı 3.000 adet × 15 ₺’dir. Yıl içinde 3.200 adet satılmış, bunlardan 200 adedi müşteriler tarafından "
    "iade edilerek yeniden stoka alınmıştır.\n\nDönem sonu SMM kaydı aşağıdakilerden hangisidir?",
    K([(621, satilan * 14.25)], [(153, satilan * 14.25)]),
    [K([(621, 3_200 * 14.25)], [(153, 3_200 * 14.25)]),
     K([(621, 3_000 * 15)], [(153, 3_000 * 15)]),
     K([(621, 1_000 * 12 + 2_000 * 15)], [(153, 1_000 * 12 + 2_000 * 15)]),
     K([(153, satilan * 14.25)], [(621, satilan * 14.25)])],
    f"Ortalama birim maliyet 57.000 / 4.000 = 14,25 ₺. Net satılan 3.200 − 200 = 3.000 adet; SMM "
    f"3.000 × 14,25 = {tl(satilan * 14.25)} ₺ olup 621 borç, 153 alacak yazılır. Dönem sonu stoku 1.000 adet "
    f"× 14,25 = 14.250 ₺’dir.")

# 39 — hammaddede NGD istisnası
P.q("TMS 2 md. 32",
    "Mobilya üreticisinin ambarındaki kontrplak stokunun maliyeti 300.000 ₺’dir. Dönem sonunda kontrplağın piyasa "
    "fiyatı 270.000 ₺’ye düşmüştür. Bu kontrplakla üretilecek mobilyaların ise maliyetlerinin üzerinde, kârlı bir fiyatla "
    "satılacağı sözleşmelerle belgelenmiştir.\n\nKontrplak stoku için aşağıdakilerden hangisi doğrudur?",
    "Kontrplak için değer düşüklüğü kaydedilmez.",
    ["Kontrplak 270.000 ₺’ye indirgenir.",
     "30.000 ₺ mamul maliyetine eklenir.",
     "Kontrplak piyasa fiyatına göre yeniden değerlenir.",
     "30.000 ₺ gelecek dönemlere ertelenir."],
    "Üretimde kullanılacak hammadde ve malzemeler, dâhil edilecekleri mamullerin maliyetinin üzerinde bir fiyatla satılması "
    "bekleniyorsa maliyetin altına indirgenmez. Hammadde fiyatındaki düşüş mamul maliyetinin NGD’yi aşacağını gösterseydi "
    "indirim yapılırdı.", zorluk="hard")

# 40 — stok maliyetine giren işçilik (hesap tarafı, 7/A)
P.q(f"{R}: 720",
    "Üretim işletmesinde ay içinde üretim hattında doğrudan ürün üzerinde çalışan işçilere 280.000 ₺, fabrika "
    "müdürüne 70.000 ₺, satış temsilcilerine 90.000 ₺ brüt ücret tahakkuk ettirilmiştir. İşletme 7/A seçeneğini "
    f"uygulamaktadır.\n\n{DOGRU}".replace("kayıt için", "ücret tahakkuku kaydı için"),
    T(720, "borç", 280_000),
    [T(720, "borç", 350_000), T(730, "borç", 90_000), T(770, "borç", 70_000), T(760, "borç", 70_000)],
    "Doğrudan üretimde çalışan işçilerin ücreti 720 Direkt İşçilik Giderleri (280.000 ₺), fabrika müdürünün ücreti 730 "
    "Genel Üretim Giderleri (70.000 ₺), satış temsilcilerinin ücreti 760 hesabına (90.000 ₺) borç yazılır.")

# 41 — tanıtım amaçlı dağıtılan ticari mal
P.q(f"{R}: 760/153",
    "Kozmetik ürünleri satan işletme, yeni açılan bir alışveriş merkezindeki tanıtım etkinliğinde stok kartlarında "
    "maliyeti 14.000 ₺ görünen ürünleri ziyaretçilere ücretsiz olarak dağıtmıştır. Dağıtılan ürünlere ilişkin KDV etkisi "
    f"bu soruda dikkate alınmayacaktır.\n\n{KAYIT}",
    K([(760, 14_000)], [(153, 14_000)]),
    [K([(621, 14_000)], [(153, 14_000)]),
     K([(760, 14_000)], [(600, 14_000)]),
     K([(689, 14_000)], [(153, 14_000)]),
     K([(770, 14_000)], [(153, 14_000)])],
    "Tanıtım amacıyla bedelsiz dağıtılan mallar satış değildir; maliyetleri pazarlama gideri olarak 760 Pazarlama, Satış ve "
    "Dağıtım Giderleri hesabına borç, 153 Ticari Mallar hesabına alacak yazılır.", zorluk="easy")

# 42 — yarı mamul NGD
mal, sf, tam, satg = 180_000, 230_000, 45_000, 20_000
ngd = sf - tam - satg
P.q(f"{R}: yarı mamul NGD",
    f"Dönem sonunda üretim hattında bulunan yarı mamullerin o güne kadar biriken maliyeti {tl(mal)} ₺’dir. Bu ürünlerin "
    f"tamamlanması için {tl(tam)} ₺ daha üretim maliyetine katlanılacak, tamamlanan ürünler {tl(sf)} ₺’ye satılacak ve "
    f"satış için {tl(satg)} ₺ dağıtım gideri yapılacaktır.\n\n{DOGRU}",
    T(158, "alacak", mal - ngd),
    [T(158, "alacak", tam), T(151, "alacak", mal - ngd), T(654, "alacak", mal - ngd),
     T(158, "alacak", mal - ngd + satg)],
    f"Yarı mamulün NGD’si tahmini satış fiyatından tamamlama ve satış maliyetleri düşülerek bulunur: {tl(sf)} − {tl(tam)} "
    f"− {tl(satg)} = {tl(ngd)} ₺. {tl(mal - ngd)} ₺ indirim 654 borç, 158 alacak ile kaydedilir.", zorluk="hard")

# 43 — 7/A yansıtma
dimm, dis, gug = 160_000, 280_000, 130_000
P.q(f"{R}: 7/A yansıtma",
    f"7/A seçeneğini uygulayan üretim işletmesinde ay içinde 710 hesabında {tl(dimm)} ₺, 720 hesabında {tl(dis)} ₺, 730 "
    f"hesabında {tl(gug)} ₺ tutarında üretim gideri birikmiştir. Ay sonunda üretim giderleri üretim maliyetine aktarılacak, "
    "üretim henüz tamamlanmamıştır.\n\nAy sonunda maliyet hesaplarına aktarım kaydı aşağıdakilerden hangisidir?",
    K([(151, dimm + dis + gug)], [(711, dimm), (721, dis), (731, gug)]),
    [K([(152, dimm + dis + gug)], [(711, dimm), (721, dis), (731, gug)]),
     K([(151, dimm + dis + gug)], [(710, dimm), (720, dis), (730, gug)]),
     K([(620, dimm + dis + gug)], [(711, dimm), (721, dis), (731, gug)]),
     K([(711, dimm), (721, dis), (731, gug)], [(151, dimm + dis + gug)])],
    "7/A’da gider hesapları dönem sonuna kadar bakiye taşır; üretim maliyetine aktarım yansıtma hesapları üzerinden "
    f"yapılır: 151 Yarı Mamuller – Üretim {tl(dimm + dis + gug)} ₺ borç, 711, 721 ve 731 alacak. Dönem sonunda 710 ile 711 "
    "birbirine kapatılır.", zorluk="hard")

# 44 — mamul sayım fazlası
P.q(f"{R}: 152/397",
    "Yıl sonunda mamul ambarında yapılan sayımda kayıtlara göre 2.400 adet olması gereken bir üründen 2.450 adet "
    "bulunmuştur. Ürünün birim üretim maliyeti 120 ₺’dir; fazlalığın bir üretim fişinin kaydedilmemesinden kaynaklanıp "
    f"kaynaklanmadığı araştırılmaktadır.\n\n{KAYIT}",
    K([(152, 6_000)], [(397, 6_000)]),
    [K([(153, 6_000)], [(397, 6_000)]),
     K([(152, 6_000)], [(679, 6_000)]),
     K([(397, 6_000)], [(152, 6_000)]),
     K([(152, 6_000)], [(620, 6_000)])],
    "Fazla bulunan 50 adet × 120 ₺ = 6.000 ₺ mamul, nedeni araştırılırken 152 Mamuller borç, 397 Sayım ve Tesellüm "
    "Fazlaları alacak ile kaydedilir. 153 ticari malları izler.", zorluk="easy")

# 45 — benzer kalemlerin gruplanması
P.q("TMS 2 md. 29",
    "Tek bir üretim hattında üretilen, aynı amaçla kullanılan, aynı pazarda satılan ve diğer ürünlerden ayrı olarak "
    "değerlendirilmesi pratik olmayan beş farklı renk ve boyuttaki boya ürünü için işletme NGD testi yapacaktır. "
    "İşletmenin toplam stok tutarı 12 ürün grubundan oluşmaktadır.\n\nİndirimin uygulanacağı düzeyle ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Benzer boya ürünleri bir grup olarak değerlendirilebilir.",
    ["Tüm stoklar tek bir toplam olarak değerlendirilir.",
     "Mamuller grubu bütünüyle tek kalem sayılır.",
     "Coğrafi bölge bazında toplu indirim yapılır.",
     "Her renk ayrı değerlendirilir, gruplama yasaktır."],
    "İndirim genellikle kalem bazında yapılır; aynı ürün hattına ait, benzer amaçlı ve ayrı değerlendirilmesi pratik "
    "olmayan kalemler gruplanabilir. Tüm mamuller veya bir coğrafi bölge tek kalem olarak ele alınamaz.")

# 46 — sipariş avansının sınıflandırılması
P.q(f"{R}: 159",
    "İşletme dönem sonundan önce, gelecek ay teslim alınacak 250.000 ₺ + KDV’lik ticari mal siparişi için satıcıya "
    "75.000 ₺ avans ödemiş ve bunu 159 hesabına kaydetmiştir. Mallar 31 Aralık itibarıyla henüz yola çıkmamıştır.\n\n"
    "Bu avansın bilançoda gösterildiği yer aşağıdakilerden hangisidir?",
    "Dönen varlıklar – Stoklar grubu",
    ["Dönen varlıklar – Ticari alacaklar grubu",
     "Duran varlıklar – Verilen avanslar",
     "Kısa vadeli borçlar – Alınan avanslar",
     "Dönen varlıklar – Hazır değerler grubu"],
    "159 Verilen Sipariş Avansları stok alımına ilişkin olduğundan THP’de Stoklar grubunda yer alır. Duran varlık "
    "alımına ilişkin avanslar 259 hesabında, alınan avanslar ise kısa vadeli borçlarda (340) izlenir.", zorluk="easy")

# 47 — vadeli alımda finansman unsuru
pesin, vadeli = 400_000, 424_000
P.q("TMS 2 md. 18",
    f"İşletme ticari mal alımında satıcının peşin fiyatı {tl(pesin)} ₺ iken, 6 ay vadeli ödeme seçeneğini tercih ederek "
    f"{tl(vadeli)} ₺ üzerinden anlaşmıştır. Bu vade farkı olağan kredi koşullarını aşan bir finansman unsuru içermektedir; "
    "KDV etkisi dikkate alınmayacaktır.\n\nAlım tarihinde stokların maliyetiyle ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    f"Stok {tl(pesin)} ₺ ile kaydedilir, fark vade süresince faiz gideridir.",
    [f"Stok {tl(vadeli)} ₺ ile kaydedilir, fark stok maliyetine girer.",
     f"Stok {tl(pesin)} ₺ ile kaydedilir, fark alım tarihinde gider yazılır.",
     f"Stok {tl(vadeli - pesin)} ₺ tutarında maliyet düzeltmesiyle azaltılır.",
     f"Stok {tl(vadeli)} ₺ ile kaydedilir, fark satışta hasılattan düşülür."],
    f"Vadeli alım bir finansman unsuru içeriyorsa normal kredi koşullarındaki alış fiyatı ({tl(pesin)} ₺) ile vadeli "
    f"tutar arasındaki {tl(vadeli - pesin)} ₺, finansman süresi boyunca faiz gideri olarak muhasebeleştirilir.",
    zorluk="hard")

# 48 — hizmet sağlayıcıların stokları
P.q("TMS 2 md. 19",
    "Bir mühendislik danışmanlık şirketi yıl sonunda tamamlanmamış ve henüz hasılatı kaydedilmemiş bir proje için "
    "şu maliyetlere katlanmıştır: projede doğrudan çalışan mühendislerin ücretleri, projeye ilişkin sahaya ulaşım gideri, "
    "satış bölümü çalışanlarının ücretleri ve merkez genel yönetim giderleri.\n\nBu maliyetlerden hangisi hizmet "
    "stoklarının maliyetine dâhil edilir?",
    "Projede çalışan mühendislerin ücretleri",
    ["Satış bölümü çalışanlarının ücretleri",
     "Merkez genel yönetim giderlerinin tamamı",
     "Teklif hazırlığında oluşan pazarlama giderleri",
     "Tamamlanmış diğer projelerin genel giderleri"],
    "Hizmet sağlayıcıların stok maliyeti, hizmeti doğrudan veren personelin işçilik ve diğer maliyetleri ile ilgili genel "
    "giderlerden oluşur; satış ve genel yönetim personeline ilişkin giderler dâhil edilmez.")

# 49 — emanet mallar
P.q(f"{R}: emanet mal",
    "Soğuk hava deposu işleten işletme, bir tarım kooperatifine ait 900 ton elmayı aylık ücret karşılığında kendi "
    "deposunda saklamaktadır. Elmaların mülkiyeti kooperatifte kalmakta, kooperatif istediği zaman elmaları çekip "
    "satabilmektedir.\n\nDepo işletmecisi açısından elmalarla ilgili aşağıdakilerden hangisi doğrudur?",
    "Elmalar işletmenin stoklarına alınmaz.",
    ["Elmalar ticari mal olarak kaydedilir.",
     "Elmalar mamul olarak kaydedilir.",
     "Elmalar diğer stoklarda izlenir.",
     "Elmaların yarısı stoklara alınır."],
    "Kontrolü ve mülkiyeti başkasına ait olan emanet mallar işletmenin varlığı değildir; stok olarak kaydedilmez, gerekirse "
    "nazım hesaplarda izlenir. İşletmenin geliri depolama hizmet bedelidir.", zorluk="easy")

# 50 — sürekli envanterin özelliği
P.q(f"{R}: envanter yöntemleri",
    "Bir işletme stok izleme yöntemini değiştirmeyi düşünmektedir. Mevcut sistemde satılan malın maliyeti ancak yıl sonu "
    "sayımından sonra bulunabilmekte, ara dönem mali tablolarda tahmin kullanılmaktadır. Yönetim her an stok mevcudunu ve "
    "satış maliyetini kayıtlardan izleyebilmek istemektedir.\n\nYönetimin geçmeyi düşündüğü yöntemle ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Her satışta maliyet kaydı yapılır, sayım farkları ayrıca görülür.",
    ["Maliyet dönem sonunda formülle tek kayıtla bulunur.",
     "Dönem sonu sayımı gereksiz hâle gelir.",
     "Satılan malın maliyeti hesabı kullanılmaz.",
     "Stok hesabı dönem içinde alışlarla artar, satışlarla azalmaz."],
    "Sürekli envanterde her giriş ve çıkış stok hesabına işlenir; satışta 621 borç, 153 alacak yazılır. Sayım yine yapılır "
    "ve kayıtlı mevcutla fiilî mevcut arasındaki farklar 197/397 aracılığıyla ortaya çıkar.")

# 51 — indirilemeyen KDV
bed, kdv = 150_000, 30_000
P.q("TMS 2 md. 11",
    f"Yalnızca KDV’den istisna teslimlerde bulunan ve bu alımına ilişkin KDV’yi indirim konusu yapma hakkı olmayan "
    f"işletme, satmak üzere {tl(bed)} ₺ + %20 KDV bedelle ticari mal satın almış, bedeli banka havalesiyle ödemiştir. "
    f"Alışta başka gider yoktur.\n\n{DOGRU}".replace("Yalnızca KDV’den", "Sadece KDV’den"),
    T(153, "borç", bed + kdv),
    [T(153, "borç", bed), T(191, "borç", kdv), T(770, "borç", kdv), T(193, "borç", kdv)],
    f"Satın alma maliyeti, işletmenin vergi idaresinden geri alamayacağı vergileri de kapsar. İndirilemeyen {tl(kdv)} ₺ KDV "
    f"maliyete eklenir: 153 borç {tl(bed + kdv)} ₺, 102 alacak.", zorluk="hard")

# 52 — hammadde iadesi
P.q(f"{R}: 320/150/191",
    "Üretim işletmesi geçen hafta vadeli olarak aldığı 250.000 ₺ + %20 KDV tutarındaki ilk madde ve malzemenin "
    "40.000 ₺’lik kısmını kalite kontrolde standart dışı bulmuş ve iade faturası düzenleyerek satıcıya geri göndermiştir. "
    f"İade edilen malzeme üretime alınmamıştır.\n\n{KAYIT}",
    K([(320, 48_000)], [(150, 40_000), (191, 8_000)]),
    [K([(320, 48_000)], [(153, 40_000), (191, 8_000)]),
     K([(320, 48_000)], [(150, 40_000), (391, 8_000)]),
     K([(320, 48_000)], [(710, 40_000), (191, 8_000)]),
     K([(150, 40_000), (191, 8_000)], [(320, 48_000)])],
    "Üretime alınmamış malzemenin iadesi 150 İlk Madde ve Malzeme hesabını 40.000 ₺ azaltır; indirilen KDV’nin 8.000 ₺’lik "
    "kısmı 191’e alacak yazılarak düzeltilir, satıcı borcu 48.000 ₺ azalır.")

# 53 — kullanılan hammadde hesabı
db, al, ds = 70_000, 510_000, 95_000
P.q(f"{R}: 710",
    f"7/A seçeneğini uygulayan ve ilk madde çıkışlarını dönem sonu sayımıyla belirleyen işletmenin hammadde ambarına "
    f"ilişkin yıllık bilgileri şöyledir: dönem başı stok {tl(db)} ₺, alışlar {tl(al)} ₺, alıştan iadeler 15.000 ₺, dönem "
    f"sonu sayım stoku {tl(ds)} ₺. Hammaddenin tamamı doğrudan üretimde kullanılmıştır.\n\n{DOGRU}".replace(
        "kayıt için", "hammadde kullanım kaydı için"),
    T(710, "borç", db + al - 15_000 - ds),
    [T(710, "borç", db + al - ds), T(730, "borç", db + al - 15_000 - ds), T(150, "borç", db + al - 15_000 - ds),
     T(710, "borç", al - 15_000)],
    f"Kullanılan hammadde = {tl(db)} + {tl(al)} − 15.000 − {tl(ds)} = {tl(db + al - 15_000 - ds)} ₺. Doğrudan üretimde "
    "kullanıldığı için 710 borç, 150 İlk Madde ve Malzeme alacak yazılır.")

# 54 — satın alma komisyonu
P.sayisal(f"{R}: satın alma maliyeti",
    "İşletme bir aracı firma aracılığıyla 800 adet ürünü tanesi 450 ₺ + KDV’den satın almıştır. Aracı firmaya alış "
    "bedelinin %2’si oranında komisyon ödenmiş, satıcı toplu alım nedeniyle faturada %5 miktar iskontosu uygulamıştır. "
    "Ürünlerin depoya taşınması 6.000 ₺ tutmuştur.\n\nÜrünlerin stok maliyeti kaç ₺’dir?",
    tl(800 * 450 * 0.95 + 800 * 450 * 0.95 * 0.02 + 6_000),
    secenekler(800 * 450 * 0.95 + 800 * 450 * 0.95 * 0.02 + 6_000, 800 * 450 + 7_200 + 6_000, 800 * 450 * 0.95 + 6_000,
               800 * 450 * 0.95 + 800 * 450 * 0.95 * 0.02, 800 * 450 * 0.97 + 6_000),
    "Faturadaki iskonto düşülür: 360.000 × 0,95 = 342.000 ₺. Komisyon alış bedelinin %2’si: 6.840 ₺. Taşıma 6.000 ₺. "
    "Maliyet 342.000 + 6.840 + 6.000 = 354.840 ₺; KDV indirilebilir olduğundan dâhil edilmez.", zorluk="hard")

# 55 — açıklama: teminat verilen stok
P.q("TMS 2 md. 36",
    "İşletme kullandığı işletme kredisine karşılık 2.000.000 ₺ tutarındaki ticari mal stokunu bankaya rehin olarak "
    "göstermiştir. Finansal tablolar hazırlanırken muhasebe müdürü rehinli stoklarla ilgili hangi bilgilerin sunulacağını "
    "belirlemektedir.\n\nTMS 2’ye göre bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Rehinli stokların defter değeri açıklanır.",
    ["Rehinli stoklar bilanço dışına çıkarılır.",
     "Rehinli stoklar alacak olarak sınıflandırılır.",
     "Rehinli stoklar gerçeğe uygun değere çekilir.",
     "Rehin tutarı stoklardan düşülerek gösterilir."],
    "TMS 2, borçlar karşılığında teminat olarak rehnedilen stokların defter değerinin açıklanmasını ister; stoklar "
    "işletmenin varlığı olmaya devam eder, ölçüm esası değişmez.", zorluk="easy")

# 56 — stokların gider olarak kaydı
P.q("TMS 2 md. 34",
    "Bir ticaret işletmesinin yıl içinde sattığı malların maliyeti 4.200.000 ₺, yıl içinde ayrılan stok değer "
    "düşüklüğü 60.000 ₺, önceki yıl ayrılan ve bu yıl fiyat artışıyla iptal edilen değer düşüklüğü 15.000 ₺’dir.\n\n"
    "Bu tutarların gelir tablosuna yansıtılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Satılan stokun defter değeri hasılatın kaydedildiği dönemde gider yazılır.",
    ["Satılan stokun maliyeti tahsilatın yapıldığı dönemde gider yazılır.",
     "Değer düşüklüğü iptali doğrudan özkaynakta gösterilir.",
     "Değer düşüklüğü bir sonraki yıl satış olunca gider yazılır.",
     "Satılan stokun maliyeti ilgili alışın yapıldığı dönemde gider yazılır."],
    "Stoklar satıldığında defter değerleri ilgili hasılatın muhasebeleştirildiği dönemde gider yazılır. Değer düşüklüğü "
    "oluştuğu dönemde gider, iptali ise iptalin olduğu dönemde gider azalışı olarak kaydedilir.")

# 57 — mamul tamamlanması yevmiye
P.q(f"{R}: 152/151",
    "Tekstil üreticisinin ay başında üretimde bulunan 90.000 ₺’lik yarı mamulüne ay içinde 410.000 ₺ üretim maliyeti "
    "eklenmiştir. Ay sonunda 60.000 ₺ maliyetli yarı mamul üretim hattında kalmış, geri kalan ürünler tamamlanarak mamul "
    f"ambarına alınmıştır.\n\n{KAYIT}",
    K([(152, 440_000)], [(151, 440_000)]),
    [K([(152, 410_000)], [(151, 410_000)]),
     K([(152, 500_000)], [(151, 500_000)]),
     K([(620, 440_000)], [(151, 440_000)]),
     K([(151, 440_000)], [(152, 440_000)])],
    "Tamamlanan üretimin maliyeti = dönem başı yarı mamul + dönem üretim maliyeti − dönem sonu yarı mamul = 90.000 + "
    "410.000 − 60.000 = 440.000 ₺; 152 Mamuller borç, 151 alacak yazılır.")

# 58 — satış taşıma gideri satıcıya ait
P.q(f"{R}: 760",
    "İşletme bir müşterisine sattığı malları, sözleşme gereği masrafları kendisine ait olmak üzere müşterinin deposuna "
    "teslim etmiştir. Nakliyeciye 7.500 ₺ + %20 KDV taşıma bedeli peşin ödenmiştir; satış faturası daha önce "
    f"kaydedilmiştir.\n\n{KAYIT}",
    K([(760, 7_500), (191, 1_500)], [(100, 9_000)]),
    [K([(153, 7_500), (191, 1_500)], [(100, 9_000)]),
     K([(760, 9_000)], [(100, 9_000)]),
     K([(120, 9_000)], [(100, 9_000)]),
     K([(621, 7_500), (191, 1_500)], [(100, 9_000)])],
    "Satılan malın alıcıya ulaştırılması satıcı açısından dağıtım gideridir, stok maliyetine eklenmez: 760 borç 7.500 ₺, "
    "191 borç 1.500 ₺, 100 Kasa alacak 9.000 ₺.")

# 59 — KDV’nin stoka yazılması hatasının düzeltilmesi
P.q(f"{R}: hata düzeltme 191/153",
    "Muhasebe servisi aynı ay içinde yaptığı bir kontrolde, KDV’si indirilebilir 55.000 ₺ + %20 KDV tutarındaki ticari mal "
    "alışının KDV dâhil 66.000 ₺ olarak 153 Ticari Mallar hesabına borç yazıldığını fark etmiştir. Beyanname henüz "
    "verilmemiş ve mallar henüz satılmamıştır.\n\nDüzeltme kaydı aşağıdakilerden hangisidir?",
    K([(191, 11_000)], [(153, 11_000)]),
    [K([(153, 11_000)], [(191, 11_000)]),
     K([(191, 11_000)], [(391, 11_000)]),
     K([(191, 11_000)], [(320, 11_000)]),
     K([(689, 11_000)], [(153, 11_000)])],
    "Mal maliyeti 55.000 ₺ olmalıyken 66.000 ₺ yazılmıştır. Fazla yazılan 11.000 ₺ KDV 153’ten çıkarılıp 191 İndirilecek "
    "KDV hesabına aktarılır: 191 borç, 153 alacak.")

# 60 — sürekli envanterde sayım noksanı nedeninin satış olması
P.q(f"{R}: 197",
    "Sürekli envanter uygulayan işletmenin yıl sonu sayımında bir ürün grubunda 18.000 ₺ maliyetli noksanlık bulunmuş "
    "ve 197 hesabına alınmıştır. Ocak ayı incelemesinde bu malların aralık ayında faturası kesilip kaydedilen bir satışa "
    "ait olduğu, ancak maliyet kaydının unutulduğu anlaşılmıştır.\n\nBu durumda yapılacak kayıtta alacaklandırılan hesap "
    "aşağıdakilerden hangisidir?",
    hk(197), [hk(153), hk(621), hk(600), hk(689)],
    "Sayımda 197 borç, 153 alacak yazılmıştı. Noksanlığın nedeni kaydedilmemiş satış maliyeti olduğundan 621 Satılan "
    "Ticari Mallar Maliyeti borç, 197 alacak yazılarak geçici hesap kapatılır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
