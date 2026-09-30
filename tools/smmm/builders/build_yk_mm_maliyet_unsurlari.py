# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi · Maliyet Unsurları — 60 soru, 2026 test biçimi.

Direkt ilk madde ve malzeme (stok çıkış yöntemleri, alış maliyeti, fire, ihtiyaç hesabı), direkt işçilik
(ücret unsurları, fazla çalışma primi, boş geçen zaman, işveren payları, parça başı ücret) ve genel üretim
giderleri (kapsam, sabit/değişken ayrımı) gerçek kitapçıklardaki gibi tutar ve tablo veren olaylarla
sorulur.

Dayanak: MSUGT Tekdüzen Hesap Planı 7/A (710-731) ve 150 İlk Madde ve Malzeme hesabı işleyişi; TMS 2
maliyet unsurları; maliyet muhasebesinin genel kabul görmüş esasları. Tutarlar builder içinde hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K

P = Paket("questions_topic_maliyet_unsurlari_2026.json", lesson="maliyet_muhasebesi", topic="maliyet_unsurlari",
          konu_adi="Maliyet Unsurları", seed=2026093082,
          surum="MSUGT 7/A (710-731), TMS 2 maliyet unsurları; 30.09.2026 kontrolü")

R = "Maliyet unsurları"
R7 = "MSUGT 7/A seçeneği"

# ------------------------------------------------------------------ DİMM: stok çıkış yöntemleri
# ocak hareketleri
p1 = [(1_000, 20), (2_000, 23), (1_500, 26)]   # başı, 8 ocak, 20 ocak
cik1, cik2 = 1_800, 1_600                       # 12 ocak, 28 ocak
# FIFO
fifo_cik = 1_000 * 20 + 800 * 23 + (1_200 * 23 + 400 * 26)
fifo_kalan = 1_100 * 26
tablo = ("| Tarih | Hareket | Miktar (kg) | Birim fiyat (₺) |\n|---|---|---|---|\n"
         "| 1 Ocak | Dönem başı | 1.000 | 20 |\n| 8 Ocak | Alış | 2.000 | 23 |\n| 12 Ocak | Üretime çıkış | 1.800 | — |\n"
         "| 20 Ocak | Alış | 1.500 | 26 |\n| 28 Ocak | Üretime çıkış | 1.600 | — |")
P.sayisal("TMS 2 md. 25; FIFO",
    "Bir boya üreticisinin pigment hammaddesine ilişkin ocak ayı hareketleri şöyledir:\n\n" + tablo +
    "\n\nİşletme sürekli envanter ve ilk giren ilk çıkar (FIFO) yöntemini uygulamaktadır. Ocak ayında üretime verilen "
    "hammaddenin toplam maliyeti kaç ₺’dir?",
    tl(fifo_cik), secenekler(fifo_cik, 3_400 * 26, 3_400 * 20, 3_400 * 23, fifo_cik + 2_000),
    f"FIFO’da 12 Ocak çıkışı 1.000 × 20 + 800 × 23 = 38.400 ₺, 28 Ocak çıkışı 1.200 × 23 + 400 × 26 = 38.000 ₺’dir; "
    f"toplam {tl(fifo_cik)} ₺. Elde 1.100 kg × 26 = {tl(fifo_kalan)} ₺ kalır.", zorluk="hard")

# hareketli ortalama
o1 = (1_000 * 20 + 2_000 * 23) / 3_000          # 22
c1 = cik1 * o1                                   # 39.600
kal = 1_200; deg = kal * o1                      # 26.400
o2 = (deg + 1_500 * 26) / (kal + 1_500)          # (26.400+39.000)/2.700
c2 = round(cik2 * o2, 2)
P.q("TMS 2 md. 27; hareketli ortalama",
    "Bir boya üreticisinin ocak ayı pigment hareketleri aşağıdadır:\n\n" + tablo +
    "\n\nİşletme sürekli envanterde hareketli (tartılı) ortalama maliyet yöntemini uygulamaktadır. 12 Ocak ve 28 Ocak "
    "çıkışlarının birim maliyetleri ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"12 Ocak {tl(o1)} ₺, 28 Ocak yaklaşık {tl(round(o2, 2))} ₺",
    [f"12 Ocak {tl(o1)} ₺, 28 Ocak {tl((20 + 23 + 26) / 3)} ₺", f"12 Ocak 20 ₺, 28 Ocak 23 ₺",
     f"12 Ocak {tl(21.5)} ₺, 28 Ocak {tl(24.5)} ₺", f"12 Ocak {tl(o1)} ₺, 28 Ocak {tl(24.5)} ₺"],
    f"İlk ortalama (20.000 + 46.000) / 3.000 = 22 ₺; çıkış sonrası 1.200 kg × 22 = 26.400 ₺ kalır. 20 Ocak alışından sonra "
    f"(26.400 + 39.000) / 2.700 ≈ {tl(round(o2, 2))} ₺ yeni ortalama olur ve 28 Ocak çıkışı bu birimle değerlenir.",
    zorluk="hard")

# dönemsel ağırlıklı ortalama
top_adet, top_tut = 4_500, 1_000 * 20 + 2_000 * 23 + 1_500 * 26
agort = top_tut / top_adet
P.sayisal("TMS 2 md. 27; ağırlıklı ortalama",
    "Aynı pigment hareketleri için işletme bu kez dönemsel ağırlıklı ortalama yöntemini uygulamak istemektedir:\n\n" + tablo +
    "\n\nOcak ayında üretime verilen 3.400 kg hammaddenin maliyeti kaç ₺’dir?",
    tl(round(3_400 * agort)), secenekler(round(3_400 * agort), fifo_cik, 3_400 * 23, 3_400 * 26, 3_400 * 22),
    f"Dönemsel ağırlıklı ortalama birim maliyet (20.000 + 46.000 + 39.000) / 4.500 ≈ {tl(round(agort, 2))} ₺; üretime "
    f"verilen 3.400 kg ≈ {tl(round(3_400 * agort))} ₺.", zorluk="hard")

P.q("Stok çıkış yöntemleri",
    "Bir işletme hammadde stoklarını her satın almadan sonra yeni bir ortalama birim maliyet hesaplayarak izlemekte ve "
    "bir sonraki üretime çıkışları bu güncel ortalamayla değerlemektedir. Yönetim bu yöntemin adını ve özelliğini "
    "raporda belirtmek istemektedir.\n\nİşletmenin uyguladığı yöntem aşağıdakilerden hangisidir?",
    "Hareketli (tartılı) ortalama maliyet yöntemi",
    ["Dönemsel ağırlıklı ortalama maliyet yöntemi", "İlk giren ilk çıkar yöntemi", "Özel tanımlama yöntemi",
     "Standart maliyet yöntemi"],
    "Her girişten sonra yeni ortalama hesaplanıp çıkışların güncel ortalamayla değerlendiği yöntem hareketli (tartılı) "
    "ortalamadır; dönemsel ağırlıklı ortalamada birim maliyet dönem sonunda bir kez hesaplanır.", zorluk="easy")

# ------------------------------------------------------------------ DİMM: alış maliyeti, fire, ihtiyaç
fob, nak, sig, isk = 400_000, 18_000, 4_000, 12_000
P.sayisal(R,
    f"Bir üretim işletmesi 10.000 kg çelik levhayı kg’ı 40 ₺’den satın almıştır. Satıcı faturada {tl(isk)} ₺ miktar "
    f"iskontosu uygulamış; alıcıya ait {tl(nak)} ₺ nakliye ve {tl(sig)} ₺ taşıma sigortası ödenmiştir. KDV indirilebilir, "
    "levhalar ilk madde ambarına alınmıştır.\n\nLevhaların ilk madde stokuna alınacak maliyeti kaç ₺’dir?",
    tl(fob - isk + nak + sig), secenekler(fob - isk + nak + sig, fob, fob + nak + sig, fob - isk, (fob - isk + nak + sig) * 12 // 10),
    f"Satın alma maliyeti = alış bedeli − iskonto + alışla ilgili taşıma ve sigorta: 400.000 − 12.000 + 18.000 + 4.000 = "
    f"{tl(fob - isk + nak + sig)} ₺. İndirilebilir KDV maliyete girmez.", zorluk="easy")

net, fire = 9_500, 0.05
brut = net / (1 - fire)
P.sayisal("İlk madde ihtiyacı",
    "Bir tekstil işletmesi gelecek ay 1.900 adet ceket üretecektir. Her ceket için mamulde 5 metre kumaş yer almakta, "
    "kesim sırasında kullanılan kumaşın %5’i normal fire olarak kaybolmaktadır; fire oranı üretime verilen toplam kumaş "
    "üzerinden hesaplanmaktadır.\n\nGelecek ay üretime verilmesi gereken kumaş miktarı kaç metredir?",
    tl(round(brut)), secenekler(round(brut), net, round(net * 1.05), 9_975 + 500, 9_025),
    f"Net ihtiyaç 1.900 × 5 = 9.500 m’dir. Fire üretime verilen toplamın %5’i olduğundan brüt ihtiyaç 9.500 / 0,95 = "
    f"{tl(round(brut))} m’dir; 9.500 × 1,05 hesabı fireyi yanlış tabanla bulur.", zorluk="hard")

P.q(R,
    "Bir ekmek fabrikasında üretime verilen 20.000 kg undan, hamur yoğurma ve pişirme sürecinin doğası gereği 400 kg’lık "
    "kayıp olağan kabul edilmektedir. Ayrıca depoda nem nedeniyle 300 kg un bozulmuş ve kullanılamaz hâle gelmiştir.\n\n"
    "Bu kayıplarla ilgili aşağıdakilerden hangisi doğrudur?",
    "400 kg mamul maliyetine girer, 300 kg dönem gideri yazılır.",
    ["700 kg’ın tamamı mamul maliyetine girer.",
     "700 kg’ın tamamı dönem gideri yazılır.",
     "300 kg mamul maliyetine girer, 400 kg dönem gideri yazılır.",
     "Kayıplar kaydedilmez, stok miktarı düzeltilmez."],
    "Üretim sürecinin doğasından kaynaklanan olağan fire mamul maliyetine dâhil edilir; depoda bozulma gibi olağan dışı "
    "kayıplar maliyete girmez, oluştuğu dönemde gider yazılır.")

# ------------------------------------------------------------------ DİMM: kayıtlar
P.q(R7,
    "MSUGT’nin 7/A seçeneğini uygulayan işletmede ay içinde ambardan malzeme çıkış fişleriyle üretim hattına 360.000 ₺ "
    "direkt hammadde, bakım bölümüne 24.000 ₺ yedek parça ve satış mağazasına 6.000 ₺ ambalaj malzemesi verilmiştir.\n\n"
    "Bu çıkışlara ilişkin günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(710, 360_000), (730, 24_000), (760, 6_000)], [(150, 390_000)]),
    [K([(710, 390_000)], [(150, 390_000)]),
     K([(710, 360_000), (730, 30_000)], [(150, 390_000)]),
     K([(710, 360_000), (770, 24_000), (760, 6_000)], [(150, 390_000)]),
     K([(151, 360_000), (730, 24_000), (760, 6_000)], [(150, 390_000)])],
    "Doğrudan üretime giren hammadde 710, üretim bölümündeki bakım malzemesi 730 Genel Üretim Giderleri, satış mağazasının "
    "ambalajı 760 hesabına borç yazılır; 150 İlk Madde ve Malzeme 390.000 ₺ alacaklandırılır.", zorluk="hard")

P.q(R7,
    "Üretim hattına fazla verilen 15.000 ₺’lik direkt hammadde, ay içinde kullanılmadan ambara iade edilmiştir. Çıkış "
    "sırasında tutar 710 Direkt İlk Madde ve Malzeme Giderleri hesabına borç yazılmıştır ve iade malzemenin kalitesi "
    "bozulmamıştır.\n\nİade işlemine ilişkin kayıt aşağıdakilerden hangisidir?",
    K([(150, 15_000)], [(710, 15_000)]),
    [K([(710, 15_000)], [(150, 15_000)]),
     K([(150, 15_000)], [(730, 15_000)]),
     K([(153, 15_000)], [(710, 15_000)]),
     K([(150, 15_000)], [(151, 15_000)])],
    "Kullanılmadan ambara geri dönen malzeme stoka alınır ve çıkışta yapılan gider kaydı ters çevrilir: 150 borç, 710 "
    "alacak 15.000 ₺.", zorluk="easy")

P.q(R,
    "Bir mobilya işletmesinde masa üretiminde kullanılan meşe kereste, masa ayaklarına takılan metal pabuçlar ve montajda "
    "kullanılan tutkal değerlendirilmektedir. Kereste ve pabuçlar ürün başına ölçülebilmekte, tutkal ise ölçülememektedir."
    "\n\nBu kalemlerin maliyet unsurlarına göre sınıflandırılması ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kereste ve pabuç DİMM, tutkal GÜG kapsamındadır.",
    ["Üçü de direkt ilk madde ve malzemedir.",
     "Kereste DİMM, pabuç ve tutkal GÜG kapsamındadır.",
     "Üçü de genel üretim gideridir.",
     "Tutkal DİMM, kereste ve pabuç GÜG kapsamındadır."],
    "Mamulün bünyesine giren ve ürün başına ekonomik biçimde ölçülebilen malzemeler direkt ilk madde ve malzemedir; "
    "ölçülmesi ekonomik olmayan yardımcı malzemeler endirekt malzeme olarak GÜG’e girer.")

# ------------------------------------------------------------------ DİŞ: ücret hesapları
saat, ucret, fm_saat = 180, 250, 20
normal, fm_prim = saat * ucret, fm_saat * ucret * 50 // 100
P.q("Direkt işçilik",
    f"Bir üretim işçisi ay içinde normal çalışma süresi olan {saat} saatin yanında, genel sipariş yoğunluğu nedeniyle "
    f"{fm_saat} saat fazla çalışma yapmıştır. Saat ücreti {ucret} ₺, fazla çalışma için ödenen ek ücret saat ücretinin "
    "%50’sidir; fazla çalışma belirli bir siparişten kaynaklanmamaktadır.\n\nBu işçiye ödenen ücretin maliyet "
    "unsurlarına dağılımı ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"{tl(normal + fm_saat * ucret)} ₺ DİŞ, {tl(fm_prim)} ₺ fazla çalışma primi GÜG’dür.",
    [f"{tl(normal + fm_saat * ucret + fm_prim)} ₺’nin tamamı DİŞ’dir.",
     f"{tl(normal)} ₺ DİŞ, {tl(fm_saat * ucret + fm_prim)} ₺ GÜG’dür.",
     f"{tl(normal + fm_saat * ucret)} ₺ DİŞ, {tl(fm_prim)} ₺ genel yönetim gideridir.",
     f"{tl(normal + fm_saat * ucret + fm_prim)} ₺’nin tamamı GÜG’dür."],
    f"Toplam çalışılan 200 saatin normal ücreti ({tl(normal + fm_saat * ucret)} ₺) direkt işçiliktir. Genel yoğunluktan "
    f"doğan fazla çalışma primi ({tl(fm_prim)} ₺) belirli bir ürüne ait olmadığından GÜG’e yüklenir.", zorluk="hard")

P.q("Direkt işçilik",
    "Bir işletmede belirli bir müşterinin acil siparişini zamanında yetiştirmek için işçiler bir hafta boyunca fazla "
    "çalışma yapmış ve 36.000 ₺ fazla çalışma primi ödenmiştir. Fazla çalışma sadece bu siparişin üretimi için "
    "yapılmıştır.\n\nBu prim ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Siparişin direkt işçilik maliyetine eklenir.",
    ["Tüm üretime GÜG olarak dağıtılır.",
     "Genel yönetim gideri olarak kaydedilir.",
     "Pazarlama gideri olarak kaydedilir.",
     "Dönem sonunda satılan mamul maliyetinden düşülür."],
    "Fazla çalışma belirli bir siparişin gereği olarak yapılmışsa prim o siparişin direkt maliyetidir; genel yoğunluktan "
    "doğan fazla çalışma primi ise GÜG’e yüklenir.")

bos = 12
P.q("Direkt işçilik",
    f"Saat ücreti 300 ₺ olan bir torna işçisi ayda 176 saat işbaşında bulunmuştur. Bu sürenin {bos} saatinde makine "
    "arızası ve malzeme beklemesi nedeniyle üretim yapılamamıştır; bu tür beklemeler işletmede olağan kabul "
    "edilmektedir.\n\nİşçiye ödenen ücretin maliyet unsurlarına dağılımı ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"{tl((176 - bos) * 300)} ₺ DİŞ, {tl(bos * 300)} ₺ GÜG’dür.",
    [f"{tl(176 * 300)} ₺’nin tamamı direkt işçiliktir.", f"{tl((176 - bos) * 300)} ₺ DİŞ, {tl(bos * 300)} ₺ dönem gideridir.",
     f"{tl(176 * 300)} ₺’nin tamamı genel üretim gideridir.",
     f"{tl(bos * 300)} ₺ DİŞ, {tl((176 - bos) * 300)} ₺ genel üretim gideridir."],
    f"Ürün üzerinde fiilen çalışılan {176 - bos} saatin ücreti ({tl((176 - bos) * 300)} ₺) direkt işçiliktir. Olağan "
    f"sayılan boş geçen zamanın ücreti ({tl(bos * 300)} ₺) ürüne izlenemediğinden GÜG’e yüklenir.", zorluk="hard")

adet, bf = 1_250, 18
P.sayisal("Direkt işçilik",
    f"Parça başı ücret sisteminin uygulandığı bir konfeksiyon atölyesinde bir işçi ay içinde {tl(adet)} adet gömlek "
    f"dikmiştir. Gömlek başına ücret {bf} ₺’dir; kalite kontrolden geçemeyen 50 gömlek için ücret ödenmemektedir. İşçi "
    "ayrıca 2.000 ₺ yol yardımı almaktadır.\n\nİşçinin direkt işçilik olarak kaydedilecek ücreti kaç ₺’dir?",
    tl((adet - 50) * bf), secenekler((adet - 50) * bf, adet * bf, (adet - 50) * bf + 2_000, adet * bf + 2_000, 50 * bf),
    f"Parça başı ücret kabul edilen ürün sayısıyla hesaplanır: ({tl(adet)} − 50) × {bf} = {tl((adet - 50) * bf)} ₺. Yol "
    "yardımı gibi sosyal ödemeler işletme politikasına göre genellikle GÜG’e yüklenir.")

P.q("Direkt işçilik",
    "Bir fabrikada üretim hattındaki işçiler için ay içinde brüt ücretin yanında SGK işveren payı, işsizlik sigortası "
    "işveren payı ve yıllık izin ücreti karşılıkları da oluşmaktadır. İşletme bu ek işçilik maliyetlerini ürünlere "
    "doğrudan izleyememektedir.\n\nBu ek işçilik maliyetleri ile ilgili yaygın uygulama aşağıdakilerden hangisidir?",
    "Genel üretim giderlerine dâhil edilir.",
    ["Genel yönetim giderlerine dâhil edilir.",
     "Finansman giderlerine dâhil edilir.",
     "Mamul maliyetine yüklenmez.",
     "Pazarlama giderlerine dâhil edilir."],
    "Direkt işçiler için ödenen işveren payları, izin ve bayram ücretleri gibi ek maliyetler ürüne doğrudan izlenemiyorsa "
    "genel üretim giderlerine dâhil edilerek dağıtım yoluyla mamullere yüklenir.")

brut2, sgk2, iss2, gv2, dv2 = 400_000, 56_000, 4_000, 42_000, 3_036
net2 = brut2 - sgk2 - iss2 - gv2 - dv2
P.q(R7,
    f"MSUGT’nin 7/A seçeneğini uygulayan işletmede üretim hattı işçilerinin brüt ücreti {tl(brut2)} ₺’dir. Bu ücretten "
    f"SGK işçi payı {tl(sgk2)} ₺, işsizlik sigortası işçi payı {tl(iss2)} ₺, gelir vergisi {tl(gv2)} ₺ ve damga vergisi "
    f"{tl(dv2)} ₺ kesilmiştir. Ücretler ay sonunda ödenecektir.\n\nÜcret tahakkuku kaydı aşağıdakilerden hangisidir?",
    K([(720, brut2)], [(335, net2), (360, gv2 + dv2), (361, sgk2 + iss2)]),
    [K([(730, brut2)], [(335, net2), (360, gv2 + dv2), (361, sgk2 + iss2)]),
     K([(720, net2)], [(335, net2)]),
     K([(720, brut2)], [(335, net2), (361, gv2 + dv2 + sgk2 + iss2)]),
     K([(770, brut2)], [(335, net2), (360, gv2 + dv2), (361, sgk2 + iss2)])],
    f"Üretim hattı işçilerinin brüt ücreti 720 Direkt İşçilik Giderleri hesabına borç yazılır; net ücret {tl(net2)} ₺ 335’e, "
    f"vergiler {tl(gv2 + dv2)} ₺ 360’a, SGK ve işsizlik işçi payları {tl(sgk2 + iss2)} ₺ 361’e alacak kaydedilir.",
    zorluk="hard")

P.q(R7,
    "7/A seçeneğini uygulayan işletmede ay sonunda 720 Direkt İşçilik Giderleri hesabında 680.000 ₺ birikmiştir. Bu tutar "
    "üretim maliyetine aktarılacak; üretim henüz tamamlanmamış olup ürünler yarı mamul hâlindedir.\n\nAy sonu aktarım "
    "kaydı aşağıdakilerden hangisidir?",
    K([(151, 680_000)], [(721, 680_000)]),
    [K([(151, 680_000)], [(720, 680_000)]),
     K([(152, 680_000)], [(721, 680_000)]),
     K([(721, 680_000)], [(151, 680_000)]),
     K([(730, 680_000)], [(721, 680_000)])],
    "720’de toplanan direkt işçilik 721 Direkt İşçilik Giderleri Yansıtma Hesabı aracılığıyla 151 Yarı Mamuller – Üretim "
    "hesabına aktarılır; dönem sonunda 721 ile 720 birbirine kapatılır.")

# ------------------------------------------------------------------ GÜG
P.q(R,
    "Bir otomotiv yan sanayi fabrikasında ay içindeki üretim giderleri arasında kalıp bakım ustasının ücreti, fabrika "
    "binasının amortismanı, makine yağları, fabrika enerji gideri ve genel müdürlük muhasebe personelinin ücreti "
    "bulunmaktadır.\n\nAşağıdakilerden hangisi genel üretim gideri değildir?",
    "Genel müdürlük muhasebecisinin ücreti",
    ["Kalıp bakım ustasının ücreti", "Fabrika binasının amortismanı", "Makinelerde kullanılan yağlar",
     "Fabrikanın elektrik ve doğalgaz gideri"],
    "Genel üretim giderleri üretim yerinde oluşan endirekt malzeme, endirekt işçilik ve diğer fabrika giderleridir. Genel "
    "müdürlük muhasebe personelinin ücreti yönetim fonksiyonuna aittir, 770’te izlenir.", zorluk="easy")

gs, gd = 180_000, 12
P.q(R,
    f"Bir işletmenin aylık genel üretim giderleri {tl(gs)} ₺ sabit kısım ile makine saati başına {gd} ₺ değişken kısımdan "
    "oluşmaktadır. Ekim ayında 9.000 makine saati, kasım ayında 12.000 makine saati çalışılmıştır ve fiyat değişikliği "
    "olmamıştır.\n\nİki aydaki toplam genel üretim giderleri sırasıyla kaç ₺’dir?",
    f"{tl(gs + gd * 9_000)}; {tl(gs + gd * 12_000)}",
    [f"{tl(gd * 9_000)}; {tl(gd * 12_000)}", f"{tl(gs + gd * 9_000)}; {tl(gs + gd * 9_000)}",
     f"{tl(gs)}; {tl(gs)}", f"{tl((gs + gd * 9_000) * 12 // 9)}; {tl(gs + gd * 12_000)}"],
    f"Karma GÜG = sabit + birim değişken × makine saati: ekim {tl(gs)} + {gd} × 9.000 = {tl(gs + gd * 9_000)} ₺; kasım "
    f"{tl(gs)} + {gd} × 12.000 = {tl(gs + gd * 12_000)} ₺.")

P.sayisal(R,
    "Bir işletmede ay içinde şu giderler oluşmuştur: direkt hammadde 540.000 ₺, üretim hattı işçileri 310.000 ₺, üretim "
    "şefi maaşı 45.000 ₺, fabrika kira gideri 70.000 ₺, makine amortismanı 55.000 ₺, yardımcı malzeme 18.000 ₺, satış "
    "personeli 64.000 ₺ ve genel müdürlük kirası 50.000 ₺.\n\nAyın genel üretim giderleri toplamı kaç ₺’dir?",
    tl(45_000 + 70_000 + 55_000 + 18_000),
    secenekler(188_000, 302_000, 170_000, 238_000, 1_038_000),
    "GÜG = üretim şefi maaşı 45.000 + fabrika kirası 70.000 + makine amortismanı 55.000 + yardımcı malzeme 18.000 = "
    "188.000 ₺. Hammadde DİMM, hat işçileri DİŞ; satış personeli ve genel müdürlük kirası dönem gideridir.")

P.q(R7,
    "7/A seçeneğini uygulayan işletmede ay içinde fabrika binası için 90.000 ₺ amortisman, üretim bölümü için 40.000 ₺ "
    "enerji gideri (fatura ödenmemiş) ve üretim şefi için 60.000 ₺ brüt ücret tahakkuk ettirilecektir.\n\nBu giderlerin "
    "kaydedileceği gider hesabı aşağıdakilerden hangisidir?",
    "730 Genel Üretim Giderleri",
    ["720 Direkt İşçilik Giderleri", "770 Genel Yönetim Giderleri", "710 Direkt İlk Madde ve Malzeme Giderleri",
     "151 Yarı Mamuller – Üretim"],
    "Fabrika amortismanı, üretim bölümünün enerji gideri ve üretim şefinin ücreti üretimle ilgili ancak ürüne doğrudan "
    "izlenemeyen giderlerdir; 7/A’da 730 Genel Üretim Giderleri hesabına borç yazılır.", zorluk="easy")

P.q("Maliyet unsurları",
    "Bir yazılım şirketi hizmet üretiminde çalışan yazılımcıların ücretlerini, kullanılan bulut sunucu kiralarını ve "
    "ofis giderlerinin hizmet üretimine düşen payını izlemektedir. Şirket MSUGT’nin 7/A seçeneğini uygulamaktadır.\n\n"
    "Bu hizmet maliyetleri hangi hesapta toplanır?",
    "740 Hizmet Üretim Maliyeti",
    ["720 Direkt İşçilik Giderleri", "730 Genel Üretim Giderleri", "770 Genel Yönetim Giderleri",
     "622 Satılan Hizmet Maliyeti"],
    "Hizmet işletmelerinde hizmet üretimine ilişkin maliyetler 740 Hizmet Üretim Maliyeti hesabında toplanır; dönem "
    "sonunda 741 aracılığıyla 622 Satılan Hizmet Maliyeti hesabına aktarılır.")

# 25 — birim maliyet unsurlarından toplam (bileşik)
P.q(R,
    "Bir işletmede bir birim mamul için 3 kg hammadde (kg’ı 40 ₺), 2 saat direkt işçilik (saati 150 ₺) kullanılmakta, GÜG "
    "direkt işçilik saati başına 90 ₺ oranıyla yüklenmektedir. Ay içinde 2.000 birim üretilmiştir.\n\nBirim ilk (asal) "
    "maliyet ve birim üretim maliyeti sırasıyla kaç ₺’dir?",
    "420; 600",
    ["300; 420", "420; 510", "300; 600", "480; 600"],
    "Birim DİMM 3 × 40 = 120 ₺, birim DİŞ 2 × 150 = 300 ₺; ilk maliyet 420 ₺. Birim GÜG 2 × 90 = 180 ₺; birim üretim "
    "maliyeti 420 + 180 = 600 ₺.")

# 26 — DİMM toplamı üretim miktarından
P.sayisal("İlk madde ihtiyacı",
    "Bir içecek üreticisi haziran ayında 50.000 şişe üretecektir. Her şişe için 0,4 kg şeker kullanılmakta ve şekerin kg "
    "fiyatı 28 ₺’dir. Ay başında 3.000 kg şeker stoku olup ay sonunda 5.000 kg stok bulundurulması "
    "hedeflenmektedir.\n\nHaziran ayında satın alınması gereken şeker miktarı kaç kg’dır?",
    tl(50_000 * 0.4 + 5_000 - 3_000), secenekler(22_000, 20_000, 18_000, 25_000, 28_000),
    "Üretim ihtiyacı 50.000 × 0,4 = 20.000 kg; satın alma = üretim ihtiyacı + hedef dönem sonu stoku − dönem başı stoku "
    "= 20.000 + 5.000 − 3.000 = 22.000 kg.")

# 27 — direkt işçilik saati x ücret
P.sayisal("Direkt işçilik",
    "Bir montaj hattında ay içinde 40 işçi, her biri 170 saat olmak üzere üretimde çalışmıştır. Saat ücreti 220 ₺ olup "
    "işçilerin toplam 300 saati hattaki bir arıza nedeniyle boş geçmiştir ve bu süre olağan kabul edilmektedir.\n\n"
    "Ayın direkt işçilik gideri kaç ₺’dir?",
    tl((40 * 170 - 300) * 220), secenekler((40 * 170 - 300) * 220, 40 * 170 * 220, 300 * 220, (40 * 170 + 300) * 220, 40 * 170 * 200),
    "Toplam 40 × 170 = 6.800 saat işbaşında bulunulmuş, 300 saat boş geçmiştir. Direkt işçilik = 6.500 × 220 = "
    "1.430.000 ₺; boş geçen 300 saatin ücreti (66.000 ₺) GÜG’e yüklenir.")

# 28 — ikramiye dağıtımı
P.q("Direkt işçilik",
    "Bir fabrika üretim işçilerine yılda iki kez, haziran ve aralık aylarında toplam 1.200.000 ₺ ikramiye ödemektedir. "
    "Yönetim, ikramiye ödenen ayların maliyetlerinin diğer aylara göre yükselmesini önlemek istemektedir.\n\nİkramiyelerin "
    "maliyetlere yansıtılması ile ilgili aşağıdakilerden hangisi uygundur?",
    "Aylık 100.000 ₺ olarak GÜG’e tahakkuk ettirilir.",
    ["Ödendiği aylarda doğrudan direkt işçiliğe yazılır.",
     "Aralık ayında tamamı genel yönetim gideri yazılır.",
     "Ödendiği aylarda finansman gideri yazılır.",
     "Mamul maliyetine yüklenmez."],
    "Yıl içine düzensiz dağılan işçilik ödemeleri maliyetleri dönemler arasında dengelemek için aylık olarak tahakkuk "
    "ettirilip genel üretim giderlerine yüklenir: 1.200.000 / 12 = 100.000 ₺.")

# 29 — 710 hesabının işleyişi (olumsuz)
P.q(R7,
    "7/A seçeneğinde 710 Direkt İlk Madde ve Malzeme Giderleri hesabının işleyişi yeni bir çalışana anlatılmaktadır. "
    "Çalışana hesaba borç ve alacak kaydedilen işlemler ile dönem sonunda hesabın kapanış şekli hakkında bilgi "
    "verilmiştir.\n\n710 hesabıyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Satış mağazasında kullanılan ambalajlar bu hesaba borç yazılır.",
    ["Üretime verilen direkt hammadde tutarı hesaba borç yazılır.",
     "Kullanılmadan ambara iade edilen malzeme hesaba alacak yazılır.",
     "Dönem sonunda 711 yansıtma hesabıyla karşılıklı kapatılır.",
     "Standart maliyet uygulanırsa farklar 712 ve 713’te izlenir."],
    "710 hesabına sadece üretime doğrudan giren ilk madde ve malzeme borç yazılır. Satış mağazasındaki ambalaj pazarlama "
    "gideridir, 760 hesabında izlenir.", zorluk="hard")

# 30 — hammadde fiyat farkı (alış sonrası) mal üretimde kullanılmış
P.q(R,
    "Bir işletme geçen ay 200.000 ₺’ye aldığı hammaddenin tamamını üretimde kullanmış ve mamuller de satılmıştır. Bu ay "
    "satıcıdan sözleşmedeki endeks maddesine göre 8.000 ₺ + KDV fiyat farkı faturası gelmiştir; tutar önemsiz kabul "
    "edilmektedir.\n\nFiyat farkının muhasebeleştirilmesi ile ilgili uygun uygulama aşağıdakilerden hangisidir?",
    "Satılan mamuller maliyetine eklenir.",
    ["İlk madde ve malzeme stokuna eklenir.",
     "Genel yönetim gideri olarak kaydedilir.",
     "Finansman gideri olarak kaydedilir.",
     "Gelecek yıla ait gider olarak ertelenir."],
    "Hammaddenin kullanıldığı ve mamullerin satıldığı durumda sonradan gelen önemsiz fiyat farkı, stok artık bulunmadığı "
    "için satılan mamuller maliyetine yansıtılır; malzeme stokta olsaydı stok maliyetine eklenirdi.", zorluk="hard")

# 31 — üretim hattında direkt işçilik oranı
P.sayisal(R,
    "Bir işletmenin dönem üretim maliyeti 1.500.000 ₺’dir. Bu maliyetin %40’ı direkt ilk madde, kalan kısmın 2/3’ü "
    "direkt işçilik, geri kalanı genel üretim giderleridir. İşletme dönüşüm maliyetini hesaplamak istemektedir.\n\n"
    "İşletmenin dönüşüm (şekillendirme) maliyeti kaç ₺’dir?",
    tl(900_000), secenekler(900_000, 600_000, 300_000, 1_200_000, 1_500_000),
    "DİMM = 1.500.000 × %40 = 600.000 ₺; kalan 900.000 ₺’nin 2/3’ü DİŞ (600.000 ₺), 1/3’ü GÜG (300.000 ₺). Dönüşüm "
    "maliyeti = DİŞ + GÜG = 900.000 ₺.", zorluk="hard")

# 32 — malzeme sayım farkı
P.q(R,
    "Yıl sonunda yapılan hammadde sayımında kayıtlarda 8.400 kg görünen bir malzemeden ambarda 8.250 kg bulunmuştur. "
    "Aradaki farkın buharlaşmadan kaynaklandığı ve sektörde kabul edilen normal oranlar içinde kaldığı tespit "
    "edilmiştir.\n\nBu fark ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Olağan fire olarak üretim maliyetine yüklenir.",
    ["Olağan dışı zarar olarak kaydedilir.",
     "Ambar sorumlusundan tahsil edilir.",
     "Kayıtlar düzeltilmeden bırakılır.",
     "Satıcıdan alacak olarak izlenir."],
    "Malzemenin doğası gereği oluşan ve normal oranlar içinde kalan sayım noksanı olağan firedir; üretim maliyetine "
    "(GÜG aracılığıyla) yüklenir. Olağan dışı kayıplar ise dönem gideri yazılır.")

# 33 — DİŞ/ DİMM ayrımı: kalite kontrol işçisi
P.q("Direkt işçilik",
    "Bir fabrikada ürünleri tek tek monte eden işçiler, bu işçilere malzeme taşıyan forklift operatörü, hattın sonunda "
    "rastgele örnek seçip test eden kalite kontrol teknisyeni ve fabrika temizlik personeli çalışmaktadır.\n\nBu "
    "çalışanlardan hangisinin ücreti direkt işçilik olarak izlenir?",
    "Ürünleri monte eden işçilerin",
    ["Forklift operatörünün", "Kalite kontrol teknisyeninin", "Temizlik personelinin",
     "Forklift operatörü ve temizlik personelinin"],
    "Doğrudan ürün üzerinde çalışan ve emeği ürüne izlenebilen montaj işçileri direkt işçiliktir; taşıma, kontrol ve "
    "temizlik gibi destek işlerinde çalışanların ücretleri endirekt işçilik olarak GÜG’e girer.", zorluk="easy")

# 34 — prim sistemi
P.sayisal("Direkt işçilik",
    "Bir işletmede işçilere standart süreden tasarruf edilen her saat için saat ücretinin %50’si kadar prim ödenmektedir. "
    "Bir işin standart süresi 40 saat, işçinin fiilî çalışma süresi 32 saat, saat ücreti 200 ₺’dir.\n\nİşçinin bu iş için "
    "alacağı toplam ücret (ücret + prim) kaç ₺’dir?",
    tl(32 * 200 + 8 * 100), secenekler(7_200, 6_400, 8_000, 8_800, 800),
    "Fiilî süre ücreti 32 × 200 = 6.400 ₺; tasarruf edilen 8 saat için prim 8 × 200 × %50 = 800 ₺. Toplam 7.200 ₺.")

# 35 — GÜG sabit/değişken sınıfı (olumsuz)
P.q(R,
    "Bir işletme genel üretim giderlerini sabit ve değişken olarak ayırmaktadır. Listede fabrika binası sigortası, üretim "
    "müdürünün maaşı, makine başına kullanılan enerji, fabrika binasının doğrusal amortismanı ve fabrika bekçilerinin "
    "ücreti vardır.\n\nAşağıdakilerden hangisi sabit genel üretim gideri değildir?",
    "Makine başına kullanılan enerji",
    ["Fabrika binası sigortası", "Üretim müdürünün maaşı", "Fabrika binasının doğrusal amortismanı",
     "Fabrika bekçilerinin ücreti"],
    "Makinelerin çalıştığı süreyle orantılı değişen enerji değişken GÜG’dür; sigorta, sabit maaşlar, doğrusal amortisman "
    "ve bekçi ücretleri üretim hacminden bağımsız sabit GÜG’dür.", zorluk="easy")

# 36 — yansıtma farkı: 731 fazlası
P.q(R7,
    "7/A seçeneğini uygulayan işletmede dönem sonunda 730 Genel Üretim Giderleri hesabı 520.000 ₺ borç, 731 Genel Üretim "
    "Giderleri Yansıtma Hesabı ise önceden belirlenmiş oranlarla yükleme sonucu 500.000 ₺ alacak bakiye vermektedir. Fark "
    "önemsiz kabul edilmektedir.\n\nBu farka ilişkin aşağıdakilerden hangisi doğrudur?",
    "20.000 ₺ eksik yükleme vardır; SMM’ye eklenir.",
    ["20.000 ₺ fazla yükleme vardır; SMM’den düşülür.",
     "Fark yoktur; hesaplar doğrudan kapatılır.",
     "20.000 ₺ eksik yükleme vardır; özkaynağa alınır.",
     "20.000 ₺ fazla yükleme vardır; stoklara eklenir."],
    "Gerçekleşen GÜG (520.000 ₺) yüklenenden (500.000 ₺) büyük olduğundan 20.000 ₺ eksik yükleme vardır; önemsiz fark "
    "satılan mamuller maliyetine eklenerek kapatılır.", zorluk="hard")

# 37 — hammadde stok değerleme yöntemi etkisi (bileşik)
P.q("Stok çıkış yöntemleri",
    "Hammadde fiyatlarının yıl boyunca sürekli yükseldiği bir yılda iki işletme aynı alış ve üretim miktarlarına "
    "sahiptir; birincisi FIFO, ikincisi dönemsel ağırlıklı ortalama yöntemini uygulamaktadır. Satış fiyatları ve diğer "
    "giderler de aynıdır.\n\nFIFO uygulayan işletme için aşağıdakilerden hangisi doğrudur?",
    "Üretim maliyeti daha düşük, dönem sonu stoku daha yüksektir.",
    ["Üretim maliyeti daha yüksek, dönem sonu stoku daha düşüktür.",
     "Üretim maliyeti ve dönem sonu stoku aynıdır.",
     "Üretim maliyeti daha düşük, dönem sonu stoku da daha düşüktür.",
     "Üretim maliyeti daha yüksek, dönem sonu stoku da daha yüksektir."],
    "Fiyatlar artarken FIFO’da üretime önce eski ve ucuz partiler verilir; üretime giden maliyet düşük, elde kalan stok "
    "yeni ve pahalı partilerden oluştuğundan yüksek olur.")

# 38 — hammadde maliyetine girmeyen (olumsuz)
P.q(R,
    "Bir işletme ithal ettiği bir hammadde için şu ödemeleri yapmıştır: satıcıya ödenen bedel, navlun, gümrük vergisi, "
    "gümrükten fabrikaya taşıma ve malzeme ambara girdikten iki ay sonra ödenen depolama kirası.\n\nBu ödemelerden hangisi "
    "hammaddenin satın alma maliyetine dâhil edilmez?",
    "Ambara girdikten sonra ödenen depolama kirası",
    ["Satıcıya ödenen bedel", "Navlun", "Gümrük vergisi", "Gümrükten fabrikaya taşıma"],
    "Satın alma maliyeti malın işletmeye gelinceye kadar katlanılan bedel, vergi, taşıma ve sigortayı kapsar. Ambara "
    "girdikten sonraki olağan depolama giderleri maliyete girmez, dönem gideri veya GÜG olarak izlenir.")

# 39 — DİŞ tahakkukunda işveren payı kaydı (hesap)
P.q(R7,
    "Üretim hattı işçilerine ilişkin SGK işveren payı ay içinde 58.000 ₺, işsizlik sigortası işveren payı 8.000 ₺ olarak "
    "hesaplanmıştır. İşletme işveren paylarını ürünlere doğrudan izleyememekte ve genel üretim giderlerine "
    "yüklemektedir.\n\nİşveren payları tahakkuk kaydı aşağıdakilerden hangisidir?",
    K([(730, 66_000)], [(361, 66_000)]),
    [K([(720, 66_000)], [(361, 66_000)]),
     K([(730, 66_000)], [(360, 66_000)]),
     K([(770, 66_000)], [(361, 66_000)]),
     K([(361, 66_000)], [(730, 66_000)])],
    "İşveren payları işletmenin gideridir; üretim işçileri için olup ürüne izlenemediğinden 730 Genel Üretim Giderleri "
    "borç, 361 Ödenecek Sosyal Güvenlik Kesintileri alacak 66.000 ₺ yazılır.")

# 40 — malzeme iadesi satıcıya (stok)
P.q(R,
    "Bir işletme ay başında 150.000 ₺ + KDV’ye aldığı hammaddenin 20.000 ₺’lik kısmını, kalite kontrolde standart dışı "
    "bulduğu için üretime vermeden satıcıya iade etmiştir. Satıcı iadeyi kabul etmiş ve borçtan düşmüştür.\n\nBu iade "
    "işlemi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "İlk madde stoku 20.000 ₺ azalır, maliyete etkisi olmaz.",
    ["710 hesabı 20.000 ₺ alacaklandırılır.",
     "Genel üretim giderleri 20.000 ₺ azalır.",
     "İlk madde stoku 20.000 ₺ artar.",
     "Satılan mamul maliyeti 20.000 ₺ azalır."],
    "Üretime verilmeden satıcıya iade edilen malzeme sadece 150 İlk Madde ve Malzeme hesabını azaltır; üretime "
    "girmediğinden maliyet hesaplarına etkisi yoktur.")

# 41 — üretim bütçesi ile hammadde (değer)
P.sayisal("İlk madde ihtiyacı",
    "Bir işletme temmuz ayında 6.000 birim mamul üretecektir. Her birim için 2,5 kg hammadde gerekmekte, hammaddenin "
    "kg fiyatı 60 ₺’dir. Temmuz başında 4.000 kg stok bulunmakta ve ay sonunda 3.000 kg stok tutulması "
    "planlanmaktadır.\n\nTemmuz ayı hammadde satın alma tutarı kaç ₺’dir?",
    tl((6_000 * 2.5 + 3_000 - 4_000) * 60), secenekler(840_000, 900_000, 960_000, 780_000, 1_020_000),
    "Üretim ihtiyacı 6.000 × 2,5 = 15.000 kg; alım miktarı = 15.000 + 3.000 − 4.000 = 14.000 kg; alım tutarı 14.000 × "
    "60 = 840.000 ₺.")

# 42 — endirekt işçilik GÜG oranı
P.q("Direkt işçilik",
    "Bir fabrikada ay içinde toplam 900.000 ₺ işçilik ödenmiştir. Bunun 620.000 ₺’si doğrudan ürün üzerinde çalışan hat "
    "işçilerine, 180.000 ₺’si bakım ve depo personeline, 100.000 ₺’si satış ve yönetim personeline aittir.\n\nİşçiliğin "
    "maliyet unsurlarına dağılımı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "620.000 ₺ DİŞ, 180.000 ₺ GÜG, 100.000 ₺ dönem gideridir.",
    ["800.000 ₺ DİŞ, 100.000 ₺ dönem gideridir.",
     "620.000 ₺ DİŞ, 280.000 ₺ GÜG’dür.",
     "900.000 ₺’nin tamamı DİŞ’dir.",
     "620.000 ₺ DİŞ, 180.000 ₺ dönem gideri, 100.000 ₺ GÜG’dür."],
    "Hat işçileri direkt işçiliktir; üretim bölümündeki bakım ve depo personeli endirekt işçilik olarak GÜG’e girer; satış "
    "ve yönetim personeli ücretleri dönem gideridir.")

# 43 — hammadde FIFO dönem sonu değeri
P.sayisal("TMS 2 md. 25; FIFO",
    "Hammadde stoklarını FIFO ile değerleyen işletmede ay başı stok 500 kg × 30 ₺’dir. Ay içinde 1.500 kg × 34 ₺ ve "
    "1.000 kg × 38 ₺ alış yapılmış, toplam 2.200 kg üretime verilmiştir.\n\nAy sonu hammadde stokunun değeri kaç ₺’dir?",
    tl(800 * 38), secenekler(30_400, 800 * 30, 800 * 34, 800 * 36, 28_000),
    "Toplam 3.000 kg mevcuttan 2.200 kg çıkmış, 800 kg kalmıştır. FIFO’da kalan en son alışlardandır: 800 × 38 = "
    "30.400 ₺.", zorluk="easy")

# 44 — DİMM + DİŞ = ilk maliyet; GÜG yüzde
P.sayisal(R,
    "Bir işletmede genel üretim giderleri direkt işçilik maliyetinin %150’si oranında mamullere yüklenmektedir. Bir "
    "siparişte 80.000 ₺ direkt ilk madde ve 40.000 ₺ direkt işçilik kullanılmıştır.\n\nSiparişin toplam üretim maliyeti "
    "kaç ₺’dir?",
    tl(80_000 + 40_000 + 60_000), secenekler(180_000, 120_000, 300_000, 240_000, 160_000),
    "Yüklenen GÜG = 40.000 × %150 = 60.000 ₺; sipariş maliyeti 80.000 + 40.000 + 60.000 = 180.000 ₺.", zorluk="easy")

# 45 — yarı mamul hesabı kapsamı
P.q(R7,
    "Ay sonunda 151 Yarı Mamuller – Üretim hesabına 711, 721 ve 731 yansıtma hesapları aracılığıyla toplam 1.450.000 ₺ "
    "aktarılmıştır. Ay başında hesapta 180.000 ₺ bakiye bulunmakta, tamamlanan ürünlerin maliyeti 1.370.000 ₺’dir.\n\n"
    "Ay sonunda 151 hesabının bakiyesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "260.000 ₺ borç bakiye verir.",
    ["80.000 ₺ borç bakiye verir.", "260.000 ₺ alacak bakiye verir.", "Bakiye vermez.", "1.630.000 ₺ borç bakiye verir."],
    "151 hesabı = dönem başı 180.000 + aktarılan 1.450.000 − tamamlanan 1.370.000 = 260.000 ₺ borç bakiye; bu tutar ay "
    "sonu yarı mamul stokudur.")

# 46 — malzeme kalite: ıskarta değil — GÜG vs DİMM, direkt malzeme tanımı olumsuz
P.q(R,
    "Maliyet muhasebesi eğitiminde direkt ilk madde ve malzemenin özellikleri tartışılmaktadır. Katılımcılar mamulün "
    "bünyesine girme, ürün başına ölçülebilme ve maliyet içinde önemli paya sahip olma gibi ölçütler üzerinde durmuştur."
    "\n\nDirekt ilk madde ve malzeme ile ilgili aşağıdakilerden hangisi yanlıştır?",
    "Üretimde kullanılan her malzeme direkt ilk maddedir.",
    ["Mamulün bünyesine girer ve ürüne izlenebilir.",
     "Ürün başına ekonomik olarak ölçülebilir.",
     "7/A’da 710 hesabında izlenir.",
     "Mamul maliyetinde genellikle önemli paya sahiptir."],
    "Üretimde kullanılan malzemenin ürüne ekonomik biçimde izlenemeyen kısmı (yardımcı malzeme, işletme malzemesi) "
    "endirekt malzemedir ve GÜG’e girer; her malzeme direkt ilk madde sayılmaz.", zorluk="easy")

# 47 — hareketli ortalama: dönem sonu stok
P.sayisal("TMS 2 md. 27; hareketli ortalama",
    "Hareketli ortalama yöntemini uygulayan işletmenin ay başı stoku 2.000 kg × 15 ₺’dir. 5’inde 3.000 kg × 20 ₺ alış, "
    "10’unda 2.500 kg üretime çıkış, 18’inde 1.500 kg × 22 ₺ alış yapılmıştır.\n\n18’indeki alıştan sonra hammaddenin yeni "
    "birim maliyeti kaç ₺’dir?",
    tl((2_500 * 18 + 1_500 * 22) / 4_000), secenekler(19.5, 18, 20, 22, 19),
    "5’indeki alıştan sonra ortalama (30.000 + 60.000) / 5.000 = 18 ₺; 10’undaki çıkıştan sonra 2.500 kg × 18 = 45.000 ₺ "
    "kalır. 18’indeki alışla (45.000 + 33.000) / 4.000 = 19,5 ₺ olur.", zorluk="hard")

# 48 — GÜG dağıtım ölçüsü seçimi
P.q(R,
    "Bir fabrikada üretim büyük ölçüde otomatik makinelerle yapılmakta, işçiler sadece makinelerin gözetiminde "
    "bulunmaktadır. Genel üretim giderlerinin önemli kısmını makine amortismanı, bakım ve enerji oluşturmaktadır.\n\nGÜG’ün "
    "mamullere yüklenmesinde en uygun dağıtım ölçüsü aşağıdakilerden hangisidir?",
    "Makine saati",
    ["Direkt işçilik saati", "Direkt işçilik tutarı", "Üretilen birim sayısı",
     "Direkt ilk madde tutarı"],
    "Giderlerin ana kaynağı makine kullanımıysa, GÜG ile en güçlü neden-sonuç ilişkisini makine saati kurar. İşçilik "
    "yoğun üretimde ise direkt işçilik saati uygun olabilir.", zorluk="easy")

# 49 — yardımcı malzeme kayıt
P.q(R7,
    "7/A seçeneğini uygulayan işletmede ay içinde üretim bölümüne makine yağı, temizlik malzemesi ve eldiven olmak üzere "
    "14.000 ₺’lik yardımcı malzeme verilmiştir. Bu malzemeler ürüne ekonomik olarak izlenememektedir.\n\nBu çıkışın kaydı "
    "aşağıdakilerden hangisidir?",
    K([(730, 14_000)], [(150, 14_000)]),
    [K([(710, 14_000)], [(150, 14_000)]),
     K([(770, 14_000)], [(150, 14_000)]),
     K([(730, 14_000)], [(153, 14_000)]),
     K([(150, 14_000)], [(730, 14_000)])],
    "Ürüne izlenemeyen yardımcı malzeme endirekt malzemedir: 730 Genel Üretim Giderleri borç, 150 İlk Madde ve Malzeme "
    "alacak 14.000 ₺.", zorluk="easy")

# 50 — dönüşüm maliyetinden GÜG (ters hesap)
P.sayisal(R,
    "Bir işletmenin ilk (asal) maliyeti 700.000 ₺, dönüşüm (şekillendirme) maliyeti 550.000 ₺, dönem üretim maliyeti ise "
    "950.000 ₺’dir. Dönem başı ve dönem sonu yarı mamul stoku bulunmamaktadır.\n\nDönemin genel üretim giderleri kaç "
    "₺’dir?",
    tl(250_000), secenekler(250_000, 300_000, 400_000, 150_000, 550_000),
    "Üretim maliyeti = DİMM + DİŞ + GÜG = 950.000; ilk maliyet DİMM + DİŞ = 700.000 → GÜG = 250.000 ₺. Dönüşüm maliyeti "
    "DİŞ + GÜG = 550.000 → DİŞ = 300.000 ₺, DİMM = 400.000 ₺.", zorluk="hard")

# 51 — malzeme fire olağan dışı kayıt
P.q(R,
    "Bir kimya fabrikasında bir tankın patlaması sonucu 45.000 ₺ değerindeki hammadde kullanılamaz hâle gelmiştir. "
    "Olay üretim sürecinin olağan bir sonucu değildir ve sigorta kapsamı bulunmamaktadır.\n\nBu kaybın muhasebeleştirilmesi "
    "ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Olağan dışı gider olarak dönem sonucuna yansıtılır.",
    ["Genel üretim giderlerine eklenerek mamullere yüklenir.",
     "Direkt ilk madde maliyetine eklenir.",
     "Kalan hammadde stokunun maliyetine eklenir.",
     "Gelecek dönemlere ertelenir."],
    "Olağan dışı nedenlerle oluşan malzeme kayıpları üretim maliyetine yüklenmez; oluştuğu dönemde olağan dışı gider ve "
    "zarar olarak kaydedilir (THP’de 689).")

# 52 — işçilik: eğitim süresi
P.q("Direkt işçilik",
    "Yeni işe alınan üretim işçileri ilk ay 40 saat eğitim almış, bu sürede üretim yapmamışlardır. Eğitim süresince "
    "ödenen ücretler toplam 96.000 ₺’dir; eğitim işletmenin olağan personel politikasının parçasıdır.\n\nBu ücretlerle ilgili "
    "aşağıdakilerden hangisi uygundur?",
    "GÜG olarak mamullere dağıtılır.",
    ["Eğitim alan işçilerin sonraki üretimine DİŞ olarak eklenir.",
     "Genel yönetim gideri olarak yazılır.",
     "Finansman gideri olarak yazılır.",
     "Gelecek yıllara ait gider olarak aktifleştirilir."],
    "Üretim işçilerinin ürün üzerinde çalışmadığı eğitim süresine ait ücretler belirli bir ürüne izlenemez; olağan bir "
    "üretim maliyeti olarak GÜG’e dâhil edilip mamullere dağıtılır.")

# 53 — DİŞ ücret farklı saat (fazla mesai + gece)
P.sayisal("Direkt işçilik",
    "Bir işçi ay içinde 160 saat normal, 20 saat fazla çalışma yapmıştır. Saat ücreti 240 ₺, fazla çalışma ek ücreti saat "
    "ücretinin %50’si olup fazla çalışma belirli bir siparişe ait değildir.\n\nBu işçi için GÜG’e yüklenecek fazla çalışma "
    "primi kaç ₺’dir?",
    tl(20 * 240 * 50 // 100), secenekler(2_400, 4_800, 7_200, 1_200, 43_200),
    "Fazla çalışma primi = 20 saat × 240 × %50 = 2.400 ₺; genel yoğunluktan doğduğu için GÜG’e yüklenir. 180 saatin "
    "normal ücreti (43.200 ₺) direkt işçiliktir.", zorluk="easy")

# 54 — 7/A yansıtma kavramı (atıf)
P.q(R7,
    "Muhasebe Sistemi Uygulama Genel Tebliği’nin 7/A seçeneğinde 710, 720 ve 730 hesaplarının yanında 711, 721 ve 731 "
    "yansıtma hesapları da kullanılmaktadır. Stajyer, yansıtma hesaplarının neden gerekli olduğunu sormaktadır.\n\n"
    "Yansıtma hesaplarının işlevi aşağıdakilerden hangisidir?",
    "Gider hesaplarını kapatmadan tutarları 151’e aktarmak",
    ["Giderleri fonksiyonları yerine çeşitlerine göre izlemek",
     "Gelir tablosunu hazırlamadan dönem kârını hesaplamak",
     "Vergi matrahını gider türlerine göre hesaplamak",
     "Stokları gerçeğe uygun değerle göstermek"],
    "Yansıtma hesapları, gider hesaplarının dönem boyunca toplam bakiye göstermesini sağlarken tutarların maliyet "
    "hesaplarına (151) aktarılmasına imkân verir; dönem sonunda gider ve yansıtma hesapları birbirine kapatılır.")

# 55 — işçilik ücret değil: işe alım gideri
P.q("Direkt işçilik",
    "Bir fabrika üretim hattı için işçi alımında ilan, mülakat ve sağlık muayenesi giderleri olarak 45.000 ₺ harcamıştır. "
    "İşe alınan işçiler bir ay sonra üretime başlamıştır.\n\nBu işe alım giderlerinin maliyet sınıflandırması ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Endirekt işçilik gideri olarak GÜG’e girer.",
    ["Direkt işçilik gideri olarak ürünlere izlenir.",
     "Direkt ilk madde ve malzeme gideridir.",
     "Finansman gideri olarak kaydedilir.",
     "Kaydedilmez, dipnotta açıklanır."],
    "Üretim personelinin işe alınmasıyla ilgili giderler üretimle bağlantılıdır ancak ürüne doğrudan izlenemez; endirekt "
    "işçilik niteliğinde GÜG’e dâhil edilir.")

# 56 — üretim hacmi, DİMM toplamı
P.sayisal(R,
    "Bir işletmede her birim mamul için 4 kg hammadde kullanılmaktadır. Hammaddenin kg fiyatı 55 ₺’dir ve üretim "
    "sürecinde ayrıca kullanılan hammaddenin %4’ü olağan fire olarak kaybolmaktadır. Ay içinde 4.800 birim mamul "
    "üretilmiştir.\n\nAyın direkt ilk madde ve malzeme maliyeti kaç ₺’dir?",
    tl(round(4_800 * 4 / 0.96 * 55)), secenekler(round(4_800 * 4 / 0.96 * 55), 4_800 * 4 * 55, round(4_800 * 4 * 1.04 * 55), 4_800 * 55, 1_155_000),
    "Mamulde yer alan net hammadde 4.800 × 4 = 19.200 kg; fire kullanılan toplamın %4’ü olduğundan kullanılan = 19.200 / "
    "0,96 = 20.000 kg. DİMM = 20.000 × 55 = 1.100.000 ₺ (olağan fire maliyete dâhil).", zorluk="hard")

# 57 — hizmet işletmesi maliyet unsuru olumsuz
P.q("Maliyet unsurları",
    "Bir hastane hizmet maliyetlerini hesaplamaktadır. Listede ameliyatlarda kullanılan tıbbi sarf malzemesi, hemşire "
    "ücretleri, tıbbi cihazların amortismanı, poliklinik binasının enerji gideri ve hastanenin reklam giderleri "
    "vardır.\n\nAşağıdakilerden hangisi hizmet üretim maliyetine dâhil edilmez?",
    "Hastanenin reklam giderleri",
    ["Tıbbi sarf malzemesi", "Hemşire ücretleri", "Tıbbi cihazların amortismanı", "Poliklinik binasının enerji gideri"],
    "Hizmet üretimine ilişkin malzeme, personel ve tesis giderleri 740’ta hizmet maliyetine girer; reklam giderleri "
    "pazarlama gideridir, 760’ta izlenir.", zorluk="easy")

# 58 — DİŞ + GÜG oran ile bulma
P.sayisal("Direkt işçilik",
    "Bir işletmede GÜG direkt işçilik saati başına 80 ₺ oranla yüklenmektedir. Ay içinde yüklenen GÜG 320.000 ₺ ve "
    "direkt işçilik saat ücreti ortalama 180 ₺’dir; boş geçen zaman yoktur.\n\nAyın direkt işçilik maliyeti kaç ₺’dir?",
    tl(320_000 // 80 * 180), secenekler(720_000, 400_000, 576_000, 1_040_000, 320_000),
    "Çalışılan DİS = 320.000 / 80 = 4.000 saat; direkt işçilik = 4.000 × 180 = 720.000 ₺.")

# 59 — kayıt: 152 → 620 (sürekli envanter)
P.q(R7,
    "Sürekli envanter uygulayan üretim işletmesi ay içinde birim maliyeti 250 ₺ olan 3.200 adet mamulü tanesi 400 ₺ + "
    "KDV’den satmıştır. Satış faturası kaydedilmiş olup satılan mamullerin maliyeti de aynı gün kayda alınacaktır.\n\n"
    "Maliyet kaydı aşağıdakilerden hangisidir?",
    K([(620, 800_000)], [(152, 800_000)]),
    [K([(621, 800_000)], [(152, 800_000)]),
     K([(620, 1_280_000)], [(152, 1_280_000)]),
     K([(620, 800_000)], [(151, 800_000)]),
     K([(152, 800_000)], [(620, 800_000)])],
    "Satılan mamullerin maliyeti 3.200 × 250 = 800.000 ₺’dir: 620 Satılan Mamuller Maliyeti borç, 152 Mamuller alacak. "
    "621 ticari malların maliyetini izler.")

# 60 — işçilik ücretinde değişken/sabit
P.q("Direkt işçilik",
    "Bir işletme üretim işçilerine üretim miktarından bağımsız olarak sabit aylık ücret ödemekte, ayrıca üretilen her "
    "birim için 5 ₺ performans primi vermektedir. Ay içinde 10.000 birim üretilmiş, sabit ücretler toplamı 400.000 ₺’dir."
    "\n\nBu işçilik maliyetinin davranışı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Karma maliyettir: 400.000 ₺ sabit, 50.000 ₺ değişken.",
    ["Tamamen değişken maliyettir: 450.000 ₺.",
     "Tamamen sabit maliyettir: 450.000 ₺.",
     "Karma maliyettir: 50.000 ₺ sabit, 400.000 ₺ değişken.",
     "Kademeli maliyettir: her 10.000 birimde 450.000 ₺."],
    "Üretimden bağımsız aylık ücret sabit, birim başına prim değişken kısımdır; toplam 450.000 ₺’lik işçilik maliyeti "
    "karma nitelik taşır.")

# 61 — dönüşüm maliyeti unsuru
P.q(R,
    "Bir döküm fabrikasında maliyet analizi yapılmaktadır. Yönetim, hammaddenin mamule dönüştürülmesi için katlanılan "
    "maliyetleri ayrıca izlemek istemekte ve bu maliyetlerin hangi unsurlardan oluştuğunu sormaktadır; genel üretim "
    "giderleri listede ayrıca yer almamaktadır.\n\nAşağıdakilerden hangisi dönüşüm (şekillendirme) maliyetinin "
    "unsurudur?",
    "Direkt işçilik",
    ["Direkt ilk madde ve malzeme", "Pazarlama, satış ve dağıtım gideri", "Genel yönetim giderleri",
     "Finansman giderleri"],
    "Dönüşüm maliyeti hammaddeyi mamule dönüştürmek için katlanılan direkt işçilik ve genel üretim giderlerinden oluşur; "
    "DİMM ilk maliyetin unsurudur, faaliyet ve finansman giderleri mamul maliyetine girmez.", zorluk="easy")

# 62 — parça başı ücretin davranışı
P.q("Direkt işçilik",
    "Bir oyuncak atölyesinde işçilere sadece ürettikleri her oyuncak için 12 ₺ ödenmekte, sabit bir aylık ücret "
    "verilmemektedir. Üretim nisan ayında 20.000 adet, mayıs ayında 26.000 adet olmuştur ve birim ücret "
    "değişmemiştir.\n\nBu işçilik maliyetinin davranışı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Değişken maliyettir.",
    ["Sabit maliyettir, üretimden bağımsızdır.", "Kademeli sabit maliyettir.",
     "Karma maliyettir, sabit kısmı ağır basar.", "Batık maliyettir, karara girmez."],
    "Parça başı ücrette toplam işçilik üretim miktarıyla doğru orantılı değişir (nisan 240.000 ₺, mayıs 312.000 ₺); birim "
    "işçilik maliyeti 12 ₺’de sabit kalır, bu nedenle değişken maliyettir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
