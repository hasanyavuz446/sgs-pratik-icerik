# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi · Maliyetleme Sistemleri — 60 soru, 2026 test biçimi.

Sipariş maliyeti, safha (evre) maliyeti (ağırlıklı ortalama ve FIFO eşdeğer birim) ile ortak ve yan ürün
maliyetleri gerçek kitapçıklardaki gibi tablo veren olaylarla sorulur; çok tutarlı şıklar ("A 9.500, B
10.000") ve tamamlanma derecesi soruları vardır.

Dayanak: maliyet muhasebesinin genel kabul görmüş esasları (sipariş ve safha maliyet sistemleri, eşdeğer
birim, ortak maliyet dağıtım yöntemleri); TMS 2 md. 14 (birlikte üretilen ve yan ürünler); MSUGT 7/A
(151 Yarı Mamuller – Üretim). Tutarlar builder içinde hesaplanır ve maliyet denkliği denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_maliyet_sistemleri_2026.json", lesson="maliyet_muhasebesi", topic="maliyet_sistemleri",
          konu_adi="Maliyetleme Sistemleri", seed=2026093084,
          surum="Sipariş ve safha maliyet sistemleri; TMS 2 md. 14; MSUGT 7/A; 30.09.2026 kontrolü")

SP = "Sipariş maliyet sistemi"
SF = "Safha (evre) maliyet sistemi"
OR = "TMS 2 md. 14; ortak ve yan ürün maliyeti"

# =============================================================================== SİPARİŞ
dimm, dis, oran = 45_000, 30_000, 120
gug = dis * oran // 100
P.sayisal(SP,
    f"Sipariş maliyet sistemini uygulayan bir matbaada 500 adet katalogdan oluşan S-14 siparişi için {tl(dimm)} ₺ kâğıt ve "
    f"mürekkep, {tl(dis)} ₺ direkt işçilik harcanmıştır. Genel üretim giderleri direkt işçilik tutarının %{oran}’si "
    "oranında siparişlere yüklenmektedir.\n\nS-14 siparişinin toplam maliyeti kaç ₺’dir?",
    tl(dimm + dis + gug), secenekler(dimm + dis + gug, dimm + dis, dimm + dis + dis * 20 // 100, dimm + dis + dimm * oran // 100, dis + gug),
    f"Yüklenen GÜG = {tl(dis)} × %{oran} = {tl(gug)} ₺; sipariş maliyeti {tl(dimm)} + {tl(dis)} + {tl(gug)} = "
    f"{tl(dimm + dis + gug)} ₺.", zorluk="easy")

top = dimm + dis + gug
P.q(SP,
    f"Bir matbaanın S-14 siparişinin toplam maliyeti {tl(top)} ₺ olup sipariş 500 adet katalogdan oluşmaktadır. İşletme "
    "fiyatlandırmada birim maliyetin üzerine %25 kâr eklemekte, ayrıca müşteriden katalog başına 5 ₺ kargo bedeli "
    "almaktadır.\n\nKatalog başına birim maliyet ve kargo hariç birim satış fiyatı sırasıyla kaç ₺’dir?",
    f"{tl(top / 500)}; {tl(top / 500 * 1.25)}",
    [f"{tl(top / 500)}; {tl(top / 500 * 1.25 + 5)}", f"{tl(top / 500 * 1.25)}; {tl(top / 500 * 1.5)}",
     f"{tl((dimm + dis) / 500)}; {tl((dimm + dis) / 500 * 1.25)}", f"{tl(top / 500)}; {tl(top / 500 + 25)}"],
    f"Birim maliyet {tl(top)} / 500 = {tl(top / 500)} ₺; %25 kârla satış fiyatı {tl(top / 500)} × 1,25 = "
    f"{tl(top / 500 * 1.25)} ₺. Kargo bedeli ayrıca faturalandığından fiyata dâhil edilmez.")

sip = {"A": (60_000, 40_000, 3_000), "B": (35_000, 22_000, 1_600), "C": (18_000, 9_000, 700)}
yk = 20
tbl = ("| Sipariş | DİMM (₺) | DİŞ (₺) | DİS |\n|---|---|---|---|\n"
       "| A | 60.000 | 40.000 | 3.000 |\n| B | 35.000 | 22.000 | 1.600 |\n| C | 18.000 | 9.000 | 700 |\n\n"
       "A siparişi tamamlanıp müşteriye teslim edilmiş, B tamamlanıp depoda beklemekte, C’nin üretimi ise "
       "sürmektedir.")
mal = {k: d + i + h * yk for k, (d, i, h) in sip.items()}
P.sayisal(SP,
    "Sipariş maliyet sistemini uygulayan işletmede ay içindeki siparişler şöyledir:\n\n" + tbl +
    f"\n\nGÜG direkt işçilik saati başına {yk} ₺ oranla yüklenmekte, ay başında yarı mamul ve mamul stoku "
    "bulunmamaktadır. Ay sonu yarı mamul stoku kaç ₺’dir?",
    tl(mal["C"]), secenekler(mal["C"], mal["B"], mal["B"] + mal["C"], 27_000, mal["A"]),
    f"Ay sonunda tamamlanmamış tek sipariş C’dir: 18.000 + 9.000 + 700 × {yk} = {tl(mal['C'])} ₺. B tamamlandığı için "
    "mamul stokunda, A ise satılan mamul maliyetindedir.")

P.sayisal(SP,
    "Sipariş maliyet sistemini uygulayan işletmede ay içindeki siparişler şöyledir:\n\n" + tbl +
    f"\n\nGÜG direkt işçilik saati başına {yk} ₺ oranla yüklenmektedir; ay başında stok yoktur. Ayın satılan mamuller "
    "maliyeti kaç ₺’dir?",
    tl(mal["A"]), secenekler(mal["A"], mal["A"] + mal["B"], 100_000, mal["A"] + mal["B"] + mal["C"], mal["B"]),
    f"Sadece teslim edilen A siparişi satılmıştır: 60.000 + 40.000 + 3.000 × {yk} = {tl(mal['A'])} ₺. B mamul stokunda, "
    "C yarı mamul stokunda kalır.", zorluk="easy")

P.q(SP,
    "Bir işletmede her müşterinin talebine göre farklı özelliklerde yat üretilmekte, her yatın maliyeti ayrı bir kartta "
    "izlenmektedir. Başka bir işletmede ise çimento sürekli ve aynı özelliklerde üretilmekte, maliyetler üretim "
    "aşamalarına göre toplanmaktadır.\n\nİki işletmenin uygulaması gereken maliyet sistemleri sırasıyla hangileridir?",
    "Sipariş maliyet; safha maliyet",
    ["Safha maliyet; sipariş maliyet", "Sipariş maliyet; sipariş maliyet", "Safha maliyet; safha maliyet",
     "Standart maliyet; faaliyet tabanlı maliyet"],
    "Müşteriye özel, birbirinden farklı ürünlerde her iş ayrı izlenir (sipariş maliyet); sürekli ve homojen seri "
    "üretimde maliyetler üretim aşamalarında toplanıp eşdeğer birimlere bölünür (safha maliyet).", zorluk="easy")

P.q(SP,
    "Sipariş maliyet sistemini yeni kuran bir mobilya atölyesi, her sipariş için tutulacak kayıtları "
    "tasarlamaktadır. Muhasebe bölümü sipariş maliyet kartında hangi bilgilerin yer alacağını belirlemek "
    "istemektedir.\n\nAşağıdakilerden hangisi sipariş maliyet kartında yer almaz?",
    "Dönemin eşdeğer birim hesaplamaları",
    ["Siparişe verilen direkt ilk madde tutarı", "Siparişe harcanan direkt işçilik tutarı",
     "Siparişe yüklenen genel üretim gideri", "Siparişin başlama ve bitiş tarihleri"],
    "Sipariş maliyet kartında siparişe ait DİMM, DİŞ, yüklenen GÜG ve sipariş bilgileri yer alır. Eşdeğer birim "
    "hesaplaması safha maliyet sisteminin aracıdır.")

P.sayisal(SP,
    "Bir işletmede genel üretim giderleri makine saatine göre yüklenmektedir. Yıllık bütçelenen GÜG 1.440.000 ₺, "
    "bütçelenen makine saati 36.000’dir. M-7 siparişi 250 makine saati kullanmış; siparişe 62.000 ₺ DİMM ve 28.000 ₺ DİŞ "
    "harcanmıştır.\n\nM-7 siparişinin toplam maliyeti kaç ₺’dir?",
    tl(62_000 + 28_000 + 250 * 40), secenekler(100_000, 90_000, 105_000, 110_000, 128_000),
    "Yükleme oranı 1.440.000 / 36.000 = 40 ₺/makine saati; M-7’ye 250 × 40 = 10.000 ₺ GÜG yüklenir. Toplam 62.000 + "
    "28.000 + 10.000 = 100.000 ₺.")

P.q(SP,
    "Sipariş maliyet sistemini uygulayan işletme, ay sonunda tamamlanan ancak henüz müşteriye teslim edilmeyen bir "
    "siparişin maliyetini (84.000 ₺) muhasebeleştirecektir. İşletme 7/A seçeneğini uygulamakta ve sürekli envanter "
    "yöntemini kullanmaktadır.\n\nBu tutar ay sonunda hangi hesapta yer alır?",
    "152 Mamuller",
    ["151 Yarı Mamuller – Üretim", "620 Satılan Mamuller Maliyeti", "153 Ticari Mallar",
     "730 Genel Üretim Giderleri"],
    "Tamamlanıp teslim edilmemiş sipariş mamul stokudur ve 152 Mamuller hesabında yer alır; tamamlanmamış siparişler "
    "151’de, teslim edilenler 620’de izlenir.", zorluk="easy")

P.q(SP,
    "Sipariş maliyet sistemini uygulayan bir işletmenin muhasebe müdürü, sistemin temel özelliklerini yeni çalışanlara "
    "anlatmaktadır. Hazırlanan listede bir hata vardır.\n\nSipariş maliyet sistemi ile ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Maliyetler dönem sonunda eşdeğer birimlere bölünür.",
    ["Her siparişin maliyeti ayrı izlenir.",
     "Müşteri isteğine göre üretimde kullanılır.",
     "Siparişin maliyeti tamamlandığında belirlenir.",
     "GÜG siparişlere yükleme oranıyla yüklenir."],
    "Sipariş maliyet sisteminde maliyetler siparişler bazında toplanır ve sipariş tamamlanınca birim maliyet bulunur; "
    "eşdeğer birim hesaplaması safha maliyet sisteminde yapılır.", zorluk="easy")

# 10 — sipariş: GÜG yükleme farkı sonrası
P.q(SP,
    "Sipariş maliyet sistemini uygulayan işletmede yıl boyunca siparişlere 980.000 ₺ GÜG yüklenmiş, gerçekleşen GÜG "
    "1.010.000 ₺ olmuştur. Farkın önemsiz olduğu değerlendirilmiş ve siparişlerin tamamı yıl içinde teslim "
    "edilmiştir.\n\nYıl sonu düzeltmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "30.000 ₺ eksik yükleme SMM’ye eklenir.",
    ["30.000 ₺ fazla yükleme SMM’den düşülür.",
     "30.000 ₺ siparişlere eşit dağıtılarak yeniden fiyatlanır.",
     "Fark mamul stoklarına eklenir.",
     "Fark gelecek yılın yükleme oranına eklenir."],
    "Gerçekleşen GÜG yüklenenden 30.000 ₺ fazladır (eksik yükleme); önemsiz fark satılan mamuller maliyetine eklenerek "
    "kapatılır.")

# =============================================================================== SAFHA — ağırlıklı ortalama (S1)
s1 = ("| Kalem | Miktar (birim) | Dönüşüm |\n|---|---|---|\n"
      "| Dönem başı yarı mamul | 1.000 | %40 |\n| Dönemde üretime başlanan | 9.000 | — |\n"
      "| Tamamlanıp sonraki aşamaya devredilen | 8.000 | %100 |\n| Dönem sonu yarı mamul | 2.000 | %50 |")
S1 = ("Safha maliyet sistemini ve ağırlıklı ortalama yöntemini uygulayan bir işletmenin karıştırma safhasına ait veriler "
      "şöyledir:\n\n" + s1 + "\n\nDirekt ilk madde safha başında tamamen verilmekte, dönüşüm maliyetleri (DİŞ ve GÜG) üretim "
      "boyunca eşit oluşmaktadır. ")
P.q(SF,
    S1 + "Direkt ilk madde ve dönüşüm maliyetleri açısından eşdeğer birim miktarları sırasıyla aşağıdakilerden "
    "hangisidir?",
    "10.000; 9.000",
    ["9.000; 8.600", "10.000; 10.000", "8.000; 9.000", "9.000; 9.000"],
    "Ağırlıklı ortalamada eşdeğer birim = tamamlanan + dönem sonu yarı mamulün eşdeğeri. DİMM: 8.000 + 2.000 × %100 = "
    "10.000; dönüşüm: 8.000 + 2.000 × %50 = 9.000.", zorluk="hard")

P.q(SF,
    S1 + "Dönem başı yarı mamulde 20.000 ₺ DİMM ve 8.000 ₺ dönüşüm maliyeti, dönem içinde 180.000 ₺ DİMM ve 262.000 ₺ "
    "dönüşüm maliyeti vardır. Birim DİMM ve birim dönüşüm maliyeti sırasıyla kaç ₺’dir?",
    "20; 30",
    ["18; 29,11", "20; 29,11", "22,5; 30", "18; 30"],
    "Ağırlıklı ortalamada dönem başı maliyetler dönem maliyetleriyle birleştirilir: DİMM (20.000 + 180.000) / 10.000 = "
    "20 ₺; dönüşüm (8.000 + 262.000) / 9.000 = 30 ₺.", zorluk="hard")

P.q(SF,
    S1 + "Birim DİMM maliyeti 20 ₺, birim dönüşüm maliyeti 30 ₺ olarak hesaplanmıştır. Sonraki safhaya devredilen "
    "mamullerin maliyeti ve dönem sonu yarı mamul maliyeti sırasıyla kaç ₺’dir?",
    "400.000; 70.000",
    ["400.000; 100.000", "450.000; 20.000", "360.000; 110.000", "420.000; 50.000"],
    "Devredilen 8.000 × (20 + 30) = 400.000 ₺. Dönem sonu yarı mamul: DİMM 2.000 × 20 = 40.000 ₺ + dönüşüm 1.000 × 30 = "
    "30.000 ₺ = 70.000 ₺. Toplam 470.000 ₺ katlanılan maliyete eşittir.", zorluk="hard")

# =============================================================================== SAFHA — FIFO (S2)
s2 = ("| Kalem | Miktar (birim) | Dönüşüm tamamlanma |\n|---|---|---|\n"
      "| Dönem başı yarı mamul | 2.000 | %60 |\n| Dönemde üretime başlanan | 10.000 | — |\n"
      "| Tamamlanıp devredilen | 9.000 | %100 |\n| Dönem sonu yarı mamul | 3.000 | %40 |")
S2 = ("Safha maliyet sistemini ve ilk giren ilk çıkar (FIFO) yöntemini uygulayan bir işletmenin şekillendirme safhası "
      "verileri şöyledir:\n\n" + s2 + "\n\nDirekt ilk madde safha başında tamamen verilmekte, dönüşüm maliyetleri üretim "
      "boyunca eşit oluşmaktadır. ")
P.q(SF,
    S2 + "Dönemde yapılan iş açısından DİMM ve dönüşüm maliyetleri eşdeğer birim miktarları sırasıyla "
    "aşağıdakilerden hangisidir?",
    "10.000; 9.000",
    ["12.000; 10.200", "9.000; 9.000", "10.000; 10.200", "12.000; 9.000"],
    "FIFO’da sadece bu dönemde yapılan iş sayılır. DİMM: dönem başı mamuller DİMM’i önceki dönemde almıştır; 9.000 − 2.000 "
    "+ 3.000 = 10.000. Dönüşüm: 9.000 − 2.000 × %60 + 3.000 × %40 = 9.000.", zorluk="hard")

P.q(SF,
    S2 + "Dönem başı yarı mamulün maliyeti 60.000 ₺, dönem içinde katlanılan DİMM 250.000 ₺ ve dönüşüm maliyeti 324.000 ₺’dir. "
    "FIFO’ya göre birim DİMM ve birim dönüşüm maliyeti sırasıyla kaç ₺’dir?",
    "25; 36",
    ["26; 36", "25; 31,76", "20,83; 27", "25,83; 36"],
    "FIFO’da dönem başı maliyet ayrı tutulur ve birim maliyetler sadece dönem maliyetlerinden bulunur: DİMM 250.000 / "
    "10.000 = 25 ₺; dönüşüm 324.000 / 9.000 = 36 ₺.", zorluk="hard")

P.sayisal(SF,
    "FIFO yöntemini uygulayan bir şekillendirme safhasında dönem başında dönüşüm açısından %60 tamamlanmış 2.000 birim "
    "yarı mamul vardır ve maliyeti 60.000 ₺’dir. Bu dönem 9.000 birim tamamlanıp devredilmiştir; dönemin birim DİMM "
    "maliyeti 25 ₺, birim dönüşüm maliyeti 36 ₺ olarak hesaplanmış, DİMM safha başında verilmektedir.\n\nDevredilen "
    "9.000 birimin toplam maliyeti kaç ₺’dir?",
    tl(515_800), secenekler(515_800, 549_000, 609_000, 427_000, 487_000),
    "Dönem başı 2.000 birim: 60.000 + kalan %40 dönüşüm 800 × 36 = 88.800 ₺. Dönemde başlanıp tamamlanan 7.000 birim: "
    "7.000 × (25 + 36) = 427.000 ₺. Toplam 515.800 ₺; dönem sonu yarı mamul 118.200 ₺ ile toplam 634.000 ₺’dir.",
    zorluk="hard")

P.sayisal(SF,
    "Bir safhada dönem sonunda 3.000 birim yarı mamul kalmıştır. Direkt ilk madde safhanın başında tamamen verilmiş, "
    "dönüşüm maliyetleri açısından ise ürünler %40 tamamlanmıştır. FIFO ile hesaplanan dönem birim maliyetleri DİMM için "
    "25 ₺, dönüşüm için 36 ₺’dir.\n\nDönem sonu yarı mamullerin maliyeti kaç ₺’dir?",
    tl(118_200), secenekler(118_200, 183_000, 75_000, 108_000, 131_400),
    "Dönem sonu 3.000 birim: DİMM 3.000 × 25 = 75.000 ₺; dönüşüm 3.000 × %40 = 1.200 eşdeğer × 36 = 43.200 ₺; toplam "
    "118.200 ₺.", zorluk="hard")

P.q(SF,
    "Safha maliyet sistemi uygulayan bir işletmede eşdeğer birim tablosu hazırlanmaktadır. Stajyer, bu tablonun neden "
    "gerekli olduğunu ve safha maliyet raporundaki yerini sormaktadır.\n\nEşdeğer birim tablosu hangi amaçla düzenlenir?",
    "Kısmen tamamlanmış ürünleri tam ürün cinsinden ifade etmek",
    ["Siparişlerin maliyetlerini ayrı ayrı izlemek",
     "Standart ve gerçek maliyetleri karşılaştırmak",
     "Ortak maliyetleri ürünlere dağıtmak",
     "Satış fiyatlarını belirlemek"],
    "Eşdeğer birim, dönem sonunda kısmen tamamlanmış ürünleri tamamlanmış birim cinsinden ifade eder ve dönem "
    "maliyetlerinin birim başına bölünmesini sağlar.", zorluk="easy")

P.sayisal(SF,
    "Safha maliyet sistemini uygulayan işletmede dönem başı yarı mamul 1.500 birim, dönemde üretime başlanan 12.000 "
    "birim, sonraki safhaya devredilen 11.200 birimdir. Dönem içinde üretim kaybı yaşanmamıştır.\n\nDönem sonu yarı mamul "
    "miktarı kaç birimdir?",
    tl(1_500 + 12_000 - 11_200), secenekler(2_300, 800, 1_500, 13_500, 2_800),
    "Miktar denkliği: dönem başı + başlanan = devredilen + dönem sonu → 1.500 + 12.000 = 11.200 + X; X = 2.300 birim.",
    zorluk="easy")

P.q(SF,
    "İki safhalı üretim yapan işletmede birinci safhada tamamlanan ürünler 400.000 ₺ maliyetle ikinci safhaya "
    "devredilmektedir. İkinci safhada ek malzeme sürecin sonunda eklenmekte, dönüşüm maliyetleri üretim boyunca "
    "oluşmaktadır.\n\nİkinci safhanın eşdeğer birim hesabında önceki safhadan devralınan maliyetlerin tamamlanma derecesi "
    "aşağıdakilerden hangisidir?",
    "%100 kabul edilir.",
    ["Dönüşüm derecesiyle aynı alınır.", "Sıfır kabul edilir.", "Sürecin sonunda eklendiği için sıfırdır.",
     "Dönem sonu yarı mamul için %50 kabul edilir."],
    "Önceki safhadan devralınan ürünler ikinci safhaya girdiği anda bu maliyet açısından tamamlanmıştır; devralınan "
    "maliyetin eşdeğer birim hesabında tamamlanma derecesi %100’dür.", zorluk="hard")

P.q(SF,
    "Bir işletmede ek malzeme ikinci safhanın sonunda (%100 tamamlanma noktasında) eklenmektedir. Dönem sonunda ikinci "
    "safhada dönüşüm açısından %70 tamamlanmış 1.000 birim yarı mamul bulunmaktadır.\n\nBu yarı mamuller için ek malzeme "
    "açısından eşdeğer birim sayısı kaçtır?",
    "0",
    ["700", "1.000", "300", "500"],
    "Malzeme sürecin sonunda eklendiğinden henüz bitmemiş (%70) ürünler bu malzemeyi almamıştır; ek malzeme açısından "
    "eşdeğer birim sıfırdır.", zorluk="hard")

P.q(SF,
    "Safha maliyet sistemini uygulayan bir işletme ağırlıklı ortalama yöntemi ile FIFO yöntemini karşılaştırmaktadır. "
    "Dönem başı yarı mamul stoku bulunmakta ve girdi fiyatları dönemden döneme değişmektedir.\n\nİki yöntem arasındaki "
    "temel fark aşağıdakilerden hangisidir?",
    "FIFO dönem başı yarı mamul maliyetini dönem maliyetinden ayrı tutar.",
    ["Ağırlıklı ortalama dönem başı stoku dikkate almaz.",
     "FIFO’da eşdeğer birim sayısı daha büyüktür.",
     "İki yöntemde toplam maliyet farklıdır.",
     "Ağırlıklı ortalama sadece sipariş maliyetinde kullanılır."],
    "Ağırlıklı ortalama dönem başı maliyetleri dönem maliyetleriyle birleştirir; FIFO ise bunları ayrı tutarak birim "
    "maliyeti sadece bu dönemde yapılan işe göre hesaplar. Dönem başı stok yoksa iki yöntem aynı sonucu verir.",
    zorluk="hard")

P.q(SF,
    "Aynı dönemde dönem başı yarı mamul stoku bulunmayan bir safhada hem ağırlıklı ortalama hem FIFO yöntemiyle eşdeğer "
    "birim ve birim maliyet hesaplanmıştır.\n\nİki yöntemin sonuçları ile ilgili aşağıdakilerden hangisi doğrudur?",
    "İki yöntem aynı sonucu verir.",
    ["FIFO daha yüksek birim maliyet verir.",
     "Ağırlıklı ortalama daha yüksek eşdeğer birim verir.",
     "FIFO’da eşdeğer birim sıfır çıkar.",
     "Ağırlıklı ortalamada dönem sonu stok sıfırdır."],
    "İki yöntem arasındaki fark dönem başı yarı mamulün işlenişinden doğar; dönem başı yarı mamul yoksa eşdeğer birimler "
    "ve birim maliyetler aynı çıkar.", zorluk="easy")

P.q(SF,
    "Safha maliyet sistemini uygulayan işletmenin muhasebecisi, safha maliyet raporunun bölümlerini düzenlemektedir. "
    "Raporda miktar denkliği, eşdeğer birimler, birim maliyetler ve maliyetlerin dağıtımı yer alacaktır.\n\nSafha maliyet "
    "raporunda yer alan “maliyetlerin dağıtımı” bölümünde aşağıdakilerden hangisi gösterilir?",
    "Devredilen ürünlerin ve dönem sonu yarı mamulün maliyetleri",
    ["Siparişlerin sipariş maliyet kartları",
     "Standart maliyet sapmaları",
     "Faaliyet yükleme oranları",
     "Ortak maliyetin mamuller arasındaki payı"],
    "Maliyetlerin dağıtımı bölümünde safhada katlanılan toplam maliyet, sonraki safhaya/mamul ambarına devredilen ürünler "
    "ile dönem sonu yarı mamulleri arasında paylaştırılır.")

P.q(SF,
    "Bir boya fabrikasında ürünler karıştırma, öğütme ve dolum safhalarından geçmektedir. Her safhanın maliyetleri ayrı "
    "toplanmakta ve safha sonunda tamamlanan ürünler bir sonraki safhaya aktarılmaktadır.\n\nSafha maliyet sistemi için "
    "aşağıdakilerden hangisi yanlıştır?",
    "Maliyetler her müşteri siparişi için ayrı izlenir.",
    ["Maliyetler üretim safhalarında toplanır.",
     "Homojen ve sürekli üretimde kullanılır.",
     "Önceki safhanın maliyeti sonraki safhaya aktarılır.",
     "Birim maliyet eşdeğer birimle hesaplanır."],
    "Safha maliyet sisteminde maliyetler siparişlere göre değil üretim safhalarına göre toplanır; siparişe göre izleme "
    "sipariş maliyet sisteminin özelliğidir.", zorluk="easy")

P.sayisal(SF,
    "Safha maliyet sistemini ve ağırlıklı ortalama yöntemini uygulayan bir işletmede dönem sonu yarı mamul 4.000 birim "
    "olup dönüşüm açısından %25 tamamlanmıştır. Devredilen ürün 16.000 birimdir.\n\nDönüşüm maliyetleri açısından eşdeğer "
    "birim sayısı kaçtır?",
    tl(16_000 + 1_000), secenekler(17_000, 20_000, 16_000, 19_000, 13_000),
    "Ağırlıklı ortalamada eşdeğer birim = devredilen + dönem sonu yarı mamul × tamamlanma: 16.000 + 4.000 × %25 = "
    "17.000.", zorluk="easy")

P.q(SF,
    "FIFO yöntemini uygulayan işletmede dönem başı yarı mamuller dönüşüm açısından %30 tamamlanmış durumdadır. Bu "
    "yarı mamuller dönem içinde tamamlanıp devredilmiştir.\n\nBu yarı mamullerin dönem içinde dönüşüm açısından "
    "tamamlanma derecesi aşağıdakilerden hangisidir?",
    "%70",
    ["%30", "%100", "%0", "%130"],
    "FIFO’da dönem başı yarı mamulün bu dönemde yapılan işi, tamamlanmak için gereken kısımdır: %100 − %30 = %70.",
    zorluk="easy")

# ekstra safha: birim maliyet sonraki safhada
P.q(SF,
    "İkinci safhada dönem başı stok yoktur. Birinci safhadan 5.000 birim 150.000 ₺ maliyetle devralınmış, dönem içinde "
    "4.000 birim tamamlanmış, 1.000 birim %50 tamamlanmış olarak kalmıştır. İkinci safhanın dönüşüm maliyeti 135.000 ₺ "
    "olup safhada malzeme eklenmemektedir.\n\nİkinci safhada devralınan ve dönüşüm maliyeti için birim maliyetler "
    "sırasıyla kaç ₺’dir?",
    "30; 30",
    ["30; 27", "37,5; 30", "30; 33,75", "25; 30"],
    "Devralınan maliyet açısından eşdeğer birim 5.000 (tamamlanma %100): 150.000 / 5.000 = 30 ₺. Dönüşüm eşdeğeri 4.000 + "
    "1.000 × %50 = 4.500: 135.000 / 4.500 = 30 ₺.", zorluk="hard")

P.sayisal(SF,
    "İkinci safhada birim devralınan maliyet 30 ₺, birim dönüşüm maliyeti 30 ₺’dir. Safhada 4.000 birim tamamlanıp mamul "
    "ambarına devredilmiş, 1.000 birim dönüşüm açısından %50 tamamlanmış olarak kalmıştır.\n\nİkinci safhanın dönem sonu "
    "yarı mamul maliyeti kaç ₺’dir?",
    tl(1_000 * 30 + 500 * 30), secenekler(45_000, 60_000, 30_000, 15_000, 240_000),
    "Dönem sonu yarı mamul: devralınan 1.000 × 30 = 30.000 ₺ + dönüşüm 500 × 30 = 15.000 ₺ = 45.000 ₺.", zorluk="hard")

# =============================================================================== ORTAK VE YAN ÜRÜN
P.q(OR,
    "Bir süt işletmesinde çiğ süt işlenerek aynı süreçten tereyağı ve ayran elde edilmektedir. Ayrılma noktasına kadar "
    "katlanılan ortak maliyet 240.000 ₺’dir; ayrılma noktasında 3.000 kg tereyağı ve 5.000 kg ayran elde "
    "edilmiştir.\n\nFiziksel miktar yöntemine göre tereyağı ve ayranın ortak maliyetten payları sırasıyla kaç ₺’dir?",
    "Tereyağı 90.000, ayran 150.000",
    ["Tereyağı 150.000, ayran 90.000", "Tereyağı 120.000, ayran 120.000", "Tereyağı 80.000, ayran 160.000",
     "Tereyağı 96.000, ayran 144.000"],
    "Fiziksel miktar yönteminde ortak maliyet miktara göre dağıtılır: 240.000 / 8.000 kg = 30 ₺/kg; tereyağı 3.000 × 30 = "
    "90.000 ₺, ayran 5.000 × 30 = 150.000 ₺.", zorluk="easy")

P.q(OR,
    "Bir işletmede ortak maliyet 168.000 ₺’dir. Ayrılma noktasında A mamulü 3.000 kg (satış fiyatı 40 ₺/kg), B mamulü "
    "5.000 kg (satış fiyatı 18 ₺/kg) elde edilmiştir. Mamuller ayrılma noktasında satılabilmektedir.\n\nSatış değeri "
    "yöntemine göre A ve B mamullerinin ortak maliyetten payları sırasıyla kaç ₺’dir?",
    "A 96.000, B 72.000",
    ["A 63.000, B 105.000", "A 72.000, B 96.000", "A 84.000, B 84.000", "A 105.000, B 63.000"],
    "Satış değerleri: A 3.000 × 40 = 120.000 ₺, B 5.000 × 18 = 90.000 ₺, toplam 210.000 ₺. A payı 168.000 × 120/210 = "
    "96.000 ₺, B payı 72.000 ₺. Fiziksel miktar yöntemi A’ya 63.000 ₺ verirdi.", zorluk="hard")

P.q(OR,
    "Bir işletmede ortak maliyet 150.000 ₺’dir. A mamulü ayrılma noktasından sonra 30.000 ₺ ek işlemle 150.000 ₺’ye, B "
    "mamulü 20.000 ₺ ek işlemle 100.000 ₺’ye satılabilmektedir; ayrılma noktasında satış değerleri "
    "bilinmemektedir.\n\nNet gerçekleşebilir değer yöntemine göre A ve B’nin ortak maliyetten payları sırasıyla kaç "
    "₺’dir?",
    "A 90.000, B 60.000",
    ["A 75.000, B 75.000", "A 60.000, B 90.000", "A 93.750, B 56.250", "A 100.000, B 50.000"],
    "NGD = nihai satış değeri − ayrılma sonrası maliyet: A 150.000 − 30.000 = 120.000 ₺, B 100.000 − 20.000 = 80.000 ₺; "
    "toplam 200.000 ₺. A payı 150.000 × 120/200 = 90.000 ₺, B 60.000 ₺.", zorluk="hard")

ym_sat, ym_ek, ym_sg, ym_kar, ortak = 50_000, 8_000, 4_000, 6_000, 500_000
ym_pay = ym_sat - ym_ek - ym_sg - ym_kar
P.q(OR,
    f"Bir işletmede ana ürünle birlikte önemsiz değerde bir yan ürün elde edilmektedir. Ortak maliyet {tl(ortak)} ₺’dir. "
    f"Yan ürünün satış değeri {tl(ym_sat)} ₺, ayrılma sonrası ek işlem maliyeti {tl(ym_ek)} ₺, satış giderleri {tl(ym_sg)} ₺ "
    f"ve normal kâr payı {tl(ym_kar)} ₺’dir.\n\nSatış fiyatından geriye doğru hesaplama yöntemine göre yan ürüne düşen "
    "ortak maliyet ve ana ürünün maliyeti sırasıyla kaç ₺’dir?",
    f"{tl(ym_pay)}; {tl(ortak - ym_pay)}",
    [f"{tl(ym_sat)}; {tl(ortak - ym_sat)}", f"{tl(ym_sat - ym_ek - ym_sg)}; {tl(ortak - ym_sat + ym_ek + ym_sg)}",
     f"{tl(ym_sat - ym_ek)}; {tl(ortak - ym_sat + ym_ek)}", f"{tl(ym_pay)}; {tl(ortak)}"],
    f"Yan ürün payı = satış değeri − ek işlem − satış gideri − normal kâr = {tl(ym_sat)} − {tl(ym_ek)} − {tl(ym_sg)} − "
    f"{tl(ym_kar)} = {tl(ym_pay)} ₺; ana ürüne kalan {tl(ortak)} − {tl(ym_pay)} = {tl(ortak - ym_pay)} ₺.", zorluk="hard")

P.q(OR,
    "Bir un fabrikasında buğday öğütülerek un elde edilmekte, aynı süreçte satış değeri una göre çok düşük olan kepek de "
    "çıkmaktadır. İşletme kepek maliyetini ayrıca hesaplamamakta, kepek satış gelirini ana ürünün maliyetinden "
    "düşmektedir.\n\nBu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Kepek yan üründür; net değeri ana ürün maliyetinden düşülebilir.",
    ["Kepek ortak mamuldür; satış değerine göre ortak maliyet alır.",
     "Kepek firedir; maliyetten düşülmez.",
     "Kepek ana üründür; un yan üründür.",
     "Kepek ıskarta mamuldür; dönem gideri yazılır."],
    "Satış değeri ana ürüne göre önemsiz olan ve ana ürünle birlikte ortaya çıkan ürün yan üründür; TMS 2’ye göre yan "
    "ürünler genellikle NGD’leriyle ölçülüp bu tutar ana ürünün maliyetinden düşülür.", zorluk="easy")

P.q(OR,
    "Birlikte üretim yapan bir rafineride ham petrol işlenerek benzin, motorin ve fuel-oil aynı süreçte elde edilmekte, "
    "belirli bir aşamadan sonra ürünler ayrı ayrı tanımlanabilir hâle gelmektedir.\n\nÜrünlerin ayrı ayrı tanımlanabildiği "
    "bu aşamaya ne ad verilir?",
    "Ayrılma noktası",
    ["Başabaş noktası", "Sipariş noktası", "Kapasite sınırı", "Eşdeğer birim noktası"],
    "Birlikte üretimde ürünlerin birbirinden ayrı olarak tanımlanabildiği aşama ayrılma noktasıdır; bu noktaya kadar "
    "katlanılan maliyetler ortak maliyettir.", zorluk="easy")

P.q(OR,
    "Ortak ürünlerden A, ayrılma noktasında 60.000 ₺’ye satılabilmekte ya da 25.000 ₺ ek işlem maliyetiyle 95.000 ₺’ye "
    "satılabilecek bir ürüne dönüştürülebilmektedir. A’nın ortak maliyetten payı 40.000 ₺’dir.\n\nEk işleme kararı ile "
    "ilgili aşağıdakilerden hangisi doğrudur?",
    "Ek işlem 10.000 ₺ fazla kâr sağlar; işlenmelidir.",
    ["Ek işlem 30.000 ₺ fazla kâr sağlar; işlenmelidir.",
     "Ek işlem kârı 5.000 ₺ azaltır; işlenmemelidir.",
     "Karar ortak maliyet payına göre verilir; işlenmemelidir.",
     "Ek işlem kârı değiştirmez; farksızdır."],
    "Ortak maliyet her iki seçenekte de aynı olduğundan karar için ilgisizdir. Ek gelir 95.000 − 60.000 = 35.000 ₺, ek "
    "maliyet 25.000 ₺; ek işlem 10.000 ₺ fazla kâr sağlar.", zorluk="hard")

P.sayisal(OR,
    "X, Y ve Z mamullerini birlikte üreten işletmede ortak maliyet 330.000 ₺’dir. Ayrılma noktasında X 2.000 kg, Y 4.000 "
    "kg, Z 5.000 kg elde edilmiştir. İşletme fiziksel miktar (ortalama birim maliyet) yöntemini kullanmaktadır.\n\nZ "
    "mamulünün ortak maliyetten kg başına alacağı pay kaç ₺’dir?",
    tl(330_000 // 11_000), secenekler(30, 150, 66, 33, 27.5),
    "Fiziksel miktar yönteminde tüm ürünler kg başına aynı payı alır: 330.000 / (2.000 + 4.000 + 5.000) = 30 ₺/kg. Z’nin "
    "toplam payı 5.000 × 30 = 150.000 ₺’dir.", zorluk="easy")

P.q(OR,
    "Bir işletme ortak ürünleri için katsayılı (ağırlıklı ortalama) dağıtım yöntemini kullanmaktadır. Ortak maliyet "
    "176.000 ₺’dir; A mamulünden 3.000 birim (katsayı 2), B mamulünden 5.000 birim (katsayı 1) üretilmiştir.\n\nA ve B "
    "mamullerinin ortak maliyetten payları sırasıyla kaç ₺’dir?",
    "A 96.000, B 80.000",
    ["A 66.000, B 110.000", "A 88.000, B 88.000", "A 80.000, B 96.000", "A 105.600, B 70.400"],
    "Ağırlıklı birimler: A 3.000 × 2 = 6.000, B 5.000 × 1 = 5.000; toplam 11.000. Birim başına 176.000 / 11.000 = 16 ₺; A "
    "6.000 × 16 = 96.000 ₺, B 5.000 × 16 = 80.000 ₺.", zorluk="hard")

P.q(OR,
    "TMS 2 Stoklar’a göre birlikte üretilen ürünlerin dönüştürme maliyetleri her ürün için ayrı ayrı belirlenemiyorsa "
    "bu maliyetler ürünler arasında dağıtılmalıdır. Bir işletme ortak maliyetleri her dönem farklı bir yöntemle "
    "dağıtmayı düşünmektedir.\n\nTMS 2’ye göre bu dağıtım ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Mantıklı ve tutarlı bir esasa göre dağıtılmalıdır.",
    ["Her dönem en düşük maliyeti verecek yöntem seçilir.",
     "Ortak maliyetler dağıtılmaz, dönem gideri yazılır.",
     "Ortak maliyetler sadece ana ürüne yüklenir.",
     "Dağıtım yöntemi her yıl vergi idaresince belirlenir."],
    "TMS 2 md. 14’e göre birlikte üretilen ürünlerin maliyetleri mantıklı ve tutarlı bir esasa göre (örneğin ayrılma "
    "noktasındaki satış değerleri) dağıtılır; yöntem dönemden döneme keyfi değiştirilmez.")

P.q(OR,
    "Bir işletmede ortak maliyet dağıtımı için fiziksel miktar yöntemi kullanılmaktadır. Ürünlerden birinin kg başına "
    "satış fiyatı diğerinin beş katı olmasına karşın iki ürün kg başına aynı ortak maliyeti almaktadır.\n\nBu yöntemin "
    "zayıf yönü aşağıdakilerden hangisidir?",
    "Ürünlerin gelir yaratma gücünü dikkate almaz.",
    ["Hesaplaması çok karmaşıktır.",
     "Toplam ortak maliyeti değiştirir.",
     "Sadece yan ürünlere uygulanabilir.",
     "Miktar bilgisi gerektirmez."],
    "Fiziksel miktar yöntemi ortak maliyeti miktara göre dağıttığından değerli ürün ile değersiz ürüne kg başına aynı "
    "maliyeti yükler; değersiz ürün zararlı görünebilir. Satış değeri yöntemi gelir yaratma gücünü dikkate alır.")

P.q(OR,
    "Bir işletmede yan ürün satışlarından elde edilen 35.000 ₺, yan ürüne maliyet yüklenmeden doğrudan diğer olağan "
    "gelirler hesabına kaydedilmektedir. Yan ürün önemsiz tutardadır.\n\nBu uygulama ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "Ana ürün tüm ortak maliyeti taşır.",
    ["Yan ürün ortak maliyetin yarısını alır.",
     "Ana ürünün maliyeti 35.000 ₺ azalır.",
     "Ortak maliyet ikiye bölünerek dağıtılır.",
     "Yan ürün satışları ana ürün satışlarına eklenir."],
    "Yan ürün satışları gelir olarak kaydedildiğinde yan ürüne maliyet ayrılmaz; ortak maliyetin tamamı ana ürüne yüklenir. "
    "Alternatif yöntemde yan ürün NGD’si ana ürün maliyetinden düşülür.", zorluk="hard")

P.q(OR,
    "Bir işletme ortak mamul ve yan ürün ayrımı yapmaktadır. Aynı süreçte çıkan ürünlerden birinin satış değeri toplam "
    "satış değerinin %2’si, diğerlerininki ise %45 ve %53’üdür.\n\nBu ürünlerin sınıflandırılması ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "%2’lik ürün yan ürün, diğer ikisi ortak mamuldür.",
    ["Üçü de ortak mamuldür.",
     "%53’lük ürün ana ürün, diğer ikisi yan üründür.",
     "Üçü de yan üründür.",
     "%45 ve %2’lik ürünler yan üründür."],
    "Satış değerleri birbirine yakın ve önemli olan ürünler ortak mamul, satış değeri diğerlerine göre önemsiz olan ürün yan "
    "üründür.")

P.sayisal(OR,
    "İki ortak mamul üreten işletmede ortak maliyet 320.000 ₺’dir. Satış değeri yöntemine göre dağıtım yapılmakta olup A "
    "mamulünün ayrılma noktasındaki satış değeri 300.000 ₺, B mamulünün satış değeri 500.000 ₺’dir.\n\nB mamulüne düşen "
    "ortak maliyet payı kaç ₺’dir?",
    tl(320_000 * 5 // 8), secenekler(200_000, 120_000, 160_000, 187_500, 180_000),
    "Toplam satış değeri 800.000 ₺; B’nin payı 320.000 × 500.000 / 800.000 = 200.000 ₺, A’nın payı 120.000 ₺.")

P.sayisal(OR,
    "Bir işletmede ortak maliyet 260.000 ₺’dir. Yan ürünün net gerçekleşebilir değeri 20.000 ₺ olup bu tutar ortak "
    "maliyetten düşülmekte, kalan maliyet A ve B ortak mamullerine satış değerlerine (A 180.000 ₺, B 120.000 ₺) göre "
    "dağıtılmaktadır.\n\nA mamulüne düşen ortak maliyet payı kaç ₺’dir?",
    tl((260_000 - 20_000) * 180 // 300), secenekler(144_000, 156_000, 96_000, 120_000, 104_000),
    "Dağıtılacak ortak maliyet 260.000 − 20.000 = 240.000 ₺; A payı 240.000 × 180.000 / 300.000 = 144.000 ₺, B payı "
    "96.000 ₺.", zorluk="hard")

# =============================================================================== karma
P.q("Maliyet sistemleri",
    "Bir hazır giyim işletmesi mağazaları için standart ürünleri seri olarak üretirken, kurumsal müşterileri için logo "
    "baskılı ve özel ölçülü üniformaları müşteri talebine göre üretmektedir.\n\nBu işletme için uygun maliyet "
    "yaklaşımı aşağıdakilerden hangisidir?",
    "Standart ürünlere safha, özel siparişlere sipariş maliyet sistemi",
    ["Tüm üretime sipariş maliyet sistemi",
     "Tüm üretime safha maliyet sistemi",
     "Standart ürünlere sipariş, özel siparişlere safha maliyet sistemi",
     "Sadece standart maliyet sistemi"],
    "Aynı işletmede homojen seri üretime safha, müşteriye özel işlere sipariş maliyet sistemi uygulanabilir (karma "
    "sistem); sistem seçimi üretimin niteliğine göre yapılır.", zorluk="hard")

P.q("Maliyet sistemleri",
    "Sipariş maliyet sistemi ve safha maliyet sistemi karşılaştırılırken bir öğrenci iki sistemin ortak özelliklerini "
    "listelemiştir. Listedeki ifadelerden biri iki sistem için de geçerli değildir.\n\nAşağıdakilerden hangisi iki sistemin "
    "ortak özelliği değildir?",
    "Birim maliyetin eşdeğer birimle bulunması",
    ["Maliyet unsurlarının DİMM, DİŞ ve GÜG olarak izlenmesi",
     "Tamamlanan ürünlerin mamul hesabına aktarılması",
     "GÜG’ün bir oranla yüklenebilmesi",
     "Yarı mamul stokunun ortaya çıkabilmesi"],
    "Her iki sistemde maliyet unsurları aynıdır, GÜG oranla yüklenebilir ve yarı mamul oluşabilir. Eşdeğer birimle birim "
    "maliyet hesaplama sadece safha maliyet sistemine özgüdür.", zorluk="hard")

P.sayisal(SF,
    "Ağırlıklı ortalama yöntemini uygulayan işletmede toplam DİMM (dönem başı dâhil) 330.000 ₺, DİMM eşdeğer birimi "
    "11.000; toplam dönüşüm maliyeti 486.000 ₺, dönüşüm eşdeğer birimi 10.800’dür. Tamamlanan ürün 10.000 birimdir.\n\n"
    "Tamamlanan ürünlerin toplam maliyeti kaç ₺’dir?",
    tl(10_000 * (30 + 45)), secenekler(750_000, 816_000, 720_000, 780_000, 675_000),
    "Birim DİMM 330.000 / 11.000 = 30 ₺; birim dönüşüm 486.000 / 10.800 = 45 ₺. Tamamlanan 10.000 × 75 = 750.000 ₺.",
    zorluk="hard")

P.q(SP,
    "Sipariş maliyet sistemini uygulayan bir inşaat firmasında bir villa projesinin maliyetleri izlenmektedir. Projede "
    "kullanılan çimento, projeye özgü mühendis ücreti ve şantiye genel giderlerinin projeye düşen payı toplanmaktadır.\n\n"
    "Şantiye genel giderlerinin projeye aktarılması ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Önceden belirlenmiş yükleme oranıyla yüklenir.",
    ["Proje bittikten sonra gider yazılır.",
     "Doğrudan malzeme maliyeti olarak izlenir.",
     "Sadece en büyük projeye yüklenir.",
     "Projelere eşit tutarda dağıtılır."],
    "Siparişe doğrudan izlenemeyen genel giderler, sipariş maliyet sisteminde önceden belirlenmiş yükleme oranlarıyla "
    "siparişlere yüklenir.")

P.q(SF,
    "Safha maliyet sistemini uygulayan işletmede üretim tek safhadan oluşmakta, her ay sonunda tamamlanan ürünler mamul "
    "ambarına aktarılmaktadır. İşletme 7/A seçeneğini uygulamaktadır.\n\nTamamlanan ürünlerin ambara aktarılmasına ilişkin "
    "kayıtta borçlandırılan hesap aşağıdakilerden hangisidir?",
    "152 Mamuller",
    ["151 Yarı Mamuller – Üretim", "620 Satılan Mamuller Maliyeti", "710 Direkt İlk Madde ve Malzeme Giderleri",
     "153 Ticari Mallar"],
    "Tamamlanan ürünlerin maliyeti 151 Yarı Mamuller – Üretim hesabından 152 Mamuller hesabına aktarılır: 152 borç, 151 "
    "alacak.", zorluk="easy")

P.q(SF,
    "Ağırlıklı ortalama yöntemini uygulayan işletmede dönem sonu yarı mamul miktarı ve tamamlanma derecesi yanlış "
    "sayılmış; gerçekte %40 tamamlanmış olan 2.000 birim %80 tamamlanmış olarak raporlanmıştır.\n\nBu hatanın etkisi "
    "aşağıdakilerden hangisidir?",
    "Dönüşüm eşdeğer birimi artar, birim dönüşüm maliyeti düşer.",
    ["Dönüşüm eşdeğer birimi azalır, birim maliyet yükselir.",
     "Eşdeğer birim ve birim maliyet değişmez.",
     "Sadece DİMM eşdeğer birimi değişir.",
     "Toplam katlanılan maliyet artar."],
    "Tamamlanma derecesinin fazla gösterilmesi dönüşüm eşdeğer birimini 800 birim artırır; aynı maliyet daha çok birime "
    "bölündüğünden birim dönüşüm maliyeti düşer ve dönem sonu yarı mamul fazla değerlenir.", zorluk="hard")

P.sayisal(SP,
    "Bir işletmede sipariş K-3’e 38.000 ₺ DİMM ve 1.200 direkt işçilik saati (saat ücreti 150 ₺) harcanmıştır. GÜG direkt "
    "işçilik saati başına 55 ₺ yüklenmekte, sipariş 400 adet üründen oluşmaktadır.\n\nK-3 siparişinin birim maliyeti kaç "
    "₺’dir?",
    tl((38_000 + 1_200 * 150 + 1_200 * 55) / 400), secenekler(710, 545, 615, 750, 640),
    "Sipariş maliyeti 38.000 + 1.200 × 150 + 1.200 × 55 = 38.000 + 180.000 + 66.000 = 284.000 ₺; birim maliyet 284.000 / "
    "400 = 710 ₺.")

P.q(OR,
    "Birlikte üretim yapan bir işletmede ortak maliyetin ürünlere dağıtımı için satış değeri yöntemi uygulanmaktadır. "
    "Yönetim, dağıtılan ortak maliyet paylarını bir ürünün üretimine devam edip etmeme kararında kullanmak "
    "istemektedir.\n\nBu yaklaşım ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Ortak maliyet payları bu karar için ilgili değildir.",
    ["Ortak maliyet payı en yüksek ürünün üretimi durdurulur.",
     "Ortak maliyet payları kararın temel ölçütüdür.",
     "Ortak maliyet sadece zarar eden ürüne yüklenmelidir.",
     "Karar fiziksel miktar yöntemine göre verilmelidir."],
    "Ortak maliyet ürünlerin tümü birlikte üretildiği sürece değişmez; ürün bazında devam veya ek işlem kararlarında "
    "sadece ayrılma sonrası ek gelir ve maliyetler ilgilidir.", zorluk="hard")

P.sayisal(OR,
    "Bir işletmede ortak maliyet 90.000 ₺’dir. A mamulünden 1.500 kg, B mamulünden 3.000 kg elde edilmiştir. A’nın kg "
    "satış fiyatı 50 ₺, B’nin 25 ₺’dir. Satış değeri yöntemi uygulanmaktadır.\n\nA mamulüne düşen ortak maliyet payı kaç "
    "₺’dir?",
    tl(45_000), secenekler(45_000, 30_000, 60_000, 50_000, 22_500),
    "Satış değerleri A 1.500 × 50 = 75.000 ₺, B 3.000 × 25 = 75.000 ₺; eşit olduğundan ortak maliyet yarı yarıya "
    "dağıtılır: A 45.000 ₺. Fiziksel miktar yöntemi A’ya 30.000 ₺ verirdi.", zorluk="easy")

P.q(SF,
    "Bir cam fabrikasında üretim ergitme ve şekillendirme safhalarından geçmektedir. Şekillendirme safhasının dönem "
    "sonunda 600 birim yarı mamulü vardır; bu birimler dönüşüm açısından %30 tamamlanmıştır ve ergitme safhasından "
    "devralınan maliyetleri tamdır.\n\nBu yarı mamuller için devralınan maliyet ve dönüşüm açısından eşdeğer birimler "
    "sırasıyla aşağıdakilerden hangisidir?",
    "600; 180",
    ["180; 600", "600; 600", "180; 180", "0; 180"],
    "Devralınan maliyet açısından tamamlanma %100’dür: 600 eşdeğer birim; dönüşüm açısından 600 × %30 = 180 eşdeğer birim.",
    zorluk="easy")

P.q(SP,
    "Sipariş maliyet sisteminde bir siparişin üretimi sırasında, müşterinin sipariş sonrası talep ettiği tasarım "
    "değişikliği nedeniyle 12.000 ₺’lik malzeme yeniden işlenmiştir. Değişikliğin maliyetini müşteri üstlenmeyi kabul "
    "etmiştir.\n\nBu yeniden işleme maliyeti ile ilgili aşağıdakilerden hangisi doğrudur?",
    "İlgili siparişin maliyetine eklenir.",
    ["Tüm siparişlere GÜG olarak dağıtılır.",
     "Olağan dışı gider olarak yazılır.",
     "Genel yönetim gideri olarak yazılır.",
     "Mamul stoklarına eşit dağıtılır."],
    "Belirli bir siparişe ve müşterinin talebine bağlı yeniden işleme maliyeti o siparişin maliyetine yüklenir; tüm "
    "üretimin olağan sonucu olan yeniden işleme ise GÜG’e dâhil edilir.")

P.q(SF,
    "Safha maliyet sistemini uygulayan işletmenin iki safhası vardır. Birinci safha tamamlanan ürünleri 520.000 ₺ "
    "maliyetle ikinci safhaya devretmiştir. İşletme 7/A seçeneğini ve her safha için 151 hesabının ayrı alt hesabını "
    "kullanmaktadır.\n\nBu devrin kaydı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "151.02 borç, 151.01 alacak 520.000 ₺ yazılır.",
    ["152 borç, 151.01 alacak 520.000 ₺ yazılır.",
     "151.01 borç, 151.02 alacak 520.000 ₺ yazılır.",
     "620 borç, 151.01 alacak 520.000 ₺ yazılır.",
     "Kayıt yapılmaz, safhalar arası aktarım izlenmez."],
    "Safhalar arası aktarımda devralan safhanın yarı mamul alt hesabı borçlandırılır, devreden safhanın alt hesabı "
    "alacaklandırılır; mamul hesabına aktarım son safhadan sonra yapılır.", zorluk="hard")

P.sayisal(SP,
    "Bir işletme özel sipariş üzerine 200 adet ofis dolabı üretmiştir. Siparişin toplam maliyeti 84.000 ₺ olup işletme "
    "fiyatlandırmada birim maliyete %30 kâr eklemektedir. Müşteriye ayrıca KDV ve nakliye faturalanacaktır.\n\nKDV ve "
    "nakliye hariç dolap başına satış fiyatı kaç ₺’dir?",
    tl(84_000 / 200 * 1.3), secenekler(546, 420, 525, 600, 504),
    "Birim maliyet 84.000 / 200 = 420 ₺; %30 kârla satış fiyatı 420 × 1,30 = 546 ₺.", zorluk="easy")

P.sayisal(SF,
    "Safha maliyet sistemini uygulayan işletmede dönem başı yarı mamul 800 birim, dönemde üretime başlanan 10.000 "
    "birimdir. Dönem içinde 9.500 birim sonraki safhaya devredilmiş, dönem sonunda 1.000 birim yarı mamul kalmıştır; "
    "aradaki fark üretim sürecinin olağan kaybıdır.\n\nDönemin normal kayıp miktarı kaç birimdir?",
    tl(800 + 10_000 - 9_500 - 1_000), secenekler(300, 500, 1_300, 200, 800),
    "Miktar denkliği: dönem başı + başlanan = devredilen + dönem sonu + kayıp → 800 + 10.000 = 9.500 + 1.000 + kayıp; "
    "kayıp 300 birim.", zorluk="easy")

P.q(OR,
    "Bir zeytinyağı fabrikasında ana ürün olan zeytinyağıyla birlikte, satış değeri toplam içinde önemsiz kalan pirina "
    "elde edilmektedir. Fabrika finansal raporlamasında TMS 2 Stoklar standardını uygulamaktadır.\n\nTMS 2’ye göre önemsiz "
    "yan ürün olan pirinanın ölçümü ile ilgili aşağıdakilerden hangisi doğrudur?",
    "NGD ile ölçülür, bu tutar ana ürün maliyetinden düşülür.",
    ["Satış değerine göre ortak maliyetten eşit pay alır.",
     "Maliyeti ölçülmez, stoklarda gösterilmez.",
     "Ana ürünle aynı birim maliyetle ölçülür.",
     "Fiziksel miktarına göre ortak maliyetin yarısını alır."],
    "TMS 2 md. 14’e göre önemsiz yan ürünler çoğunlukla net gerçekleşebilir değerleriyle ölçülür ve bu değer ana ürünün "
    "maliyetinden düşülür; böylece ana ürünün defter değeri maliyetinden önemli ölçüde farklılaşmaz.")

P.q(SP,
    "MSUGT’nin 7/A seçeneğini uygulayan ve sipariş maliyet sistemi kullanan işletme, üretimdeki siparişlerin maliyetlerini "
    "ayrı ayrı izlemek istemektedir. Ay sonunda tamamlanmamış üç sipariş bulunmaktadır.\n\nTamamlanmamış siparişlerin "
    "maliyetleri muhasebede nasıl izlenir?",
    "151 hesabının sipariş numaralı alt hesaplarında",
    ["152 hesabının sipariş numaralı alt hesaplarında",
     "730 hesabında tek tutar olarak",
     "620 hesabında dönem gideri olarak",
     "Nazım hesaplarda bilgi amaçlı olarak"],
    "Sipariş maliyet sisteminde üretimdeki siparişlerin maliyetleri 151 Yarı Mamuller – Üretim hesabında, her sipariş için "
    "açılan alt hesaplarda izlenir; tamamlananlar 152’ye aktarılır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
