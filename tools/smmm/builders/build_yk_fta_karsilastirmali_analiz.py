# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Karşılaştırmalı Tablolar Analizi — 60 soru, 2026 test biçimi.

Ardışık iki dönem arasındaki mutlak ve yüzde değişimler ortak bilanço ve gelir tablolarına bağlı sorulur;
azalışlar negatif yüzdeyle gösterilir. Değişimden geriye tutar hesabı, art arda değişimlerin birleşimi,
kalemler arası değişimlerin yorumu ve baz değeri negatif olan kalemlerde yüzdenin anlamsızlığı da yer alır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from fta_ortak import Sirket, Seri, Fta, Hesap, AD

P = Paket("questions_topic_karsilastirmali_analiz_2026.json", lesson="mali_tablolar_analizi",
          topic="karsilastirmali_analiz", konu_adi="Karşılaştırmalı Analiz", seed=2026093104,
          surum="Finansal tablolar analizi: karşılaştırmalı tablolar (yatay) analizi; 30.09.2026 kontrolü")
F = Fta(P, "yet-fta-kars-")
R = "Karşılaştırmalı tablolar analizi"
Y = ("2023", "2024", "2025")

kra = Sirket("KRA A.Ş.", Y,
             hd=[90_000, 60_000, 75_000], ta=[380_000, 350_000, 420_000], stok=[260_000, 330_000, 300_000],
             mdv=[1_000_000, 1_080_000, 1_150_000], modv=[120_000, 110_000, 100_000], tb=[240_000, 300_000, 270_000],
             uvmb=[450_000, 520_000, 480_000], sermaye=[800_000] * 3, gyk=[60_000, 100_000, 120_000],
             brut=[2_800_000, 3_080_000, 3_350_000], ind=[80_000, 60_000, 50_000],
             smm=[2_000_000, 2_250_000, 2_400_000], fg=[420_000, 470_000, 520_000], fin=[100_000, 120_000, 110_000])
krb = Sirket("KRB A.Ş.", Y,
             hd=[30_000, 42_000, 21_000], mk=[0, 20_000, 10_000], ta=[210_000, 240_000, 300_000],
             stok=[190_000, 170_000, 230_000], ddv=[10_000, 15_000, 12_000], mdv=[640_000, 700_000, 690_000],
             modv=[20_000, 35_000, 40_000], tb=[170_000, 150_000, 210_000], db=[15_000, 20_000, 18_000],
             uvmb=[180_000, 240_000, 200_000], sermaye=[450_000] * 3, gyk=[25_000, 40_000, 60_000],
             brut=[1_460_000, 1_590_000, 1_900_000], ind=[20_000, 30_000, 60_000],
             smm=[1_020_000, 1_110_000, 1_320_000], fg=[250_000, 270_000, 300_000], fin=[40_000, 45_000, 60_000])
krc = Sirket("KRC A.Ş.", Y,
             hd=[55_000, 80_000, 65_000], ta=[500_000, 560_000, 540_000], da=[25_000, 20_000, 30_000],
             stok=[420_000, 460_000, 520_000], mdv=[1_500_000, 1_450_000, 1_600_000], modv=[90_000, 130_000, 120_000],
             tb=[360_000, 410_000, 440_000], uvmb=[600_000, 560_000, 650_000], sermaye=[1_100_000] * 3,
             gyk=[80_000, 120_000, 150_000], brut=[4_150_000, 4_520_000, 4_890_000], ind=[50_000, 70_000, 90_000],
             smm=[3_100_000, 3_360_000, 3_650_000], fg=[600_000, 660_000, 690_000], fin=[150_000, 170_000, 190_000])
krd = Seri("KRD A.Ş.", range(2022, 2026), [
    ("Hazır Değerler", "hd", [64_000, 48_000, 72_000, 54_000]),
    ("Ticari Borçlar", "tb", [280_000, 350_000, 245_000, 294_000]),
    ("Kısa Vadeli Mali Borçlar", "kvmb", [150_000, 200_000, 242_000, 190_000]),
    ("Satış İndirimleri", "ind", [40_000, 36_000, 45_000, 54_000]),
    ("Faaliyet Giderleri", "fg", [520_000, 598_000, 650_000, 715_000]),
    ("Dönem Net Kârı", "nk", [96_000, 72_000, 90_000, 117_000])])


def ifadeler(ad_kalem, p, y):
    return [f"{p}-{y} döneminde {ad_kalem} değişim yüzdesi",
            f"{ad_kalem} kaleminin {p}-{y} değişim oranı",
            f"{y} yılında {ad_kalem} kaleminin önceki yıla göre değişimi"]


# Aynı şirkette her kalem bir kez sorulur (yıl değiştirerek tekrar yalnız sayı değiştirmek olur).
for s, sid, v, secim in [
    (kra, "yet-fta-kars-kra", 0, [("hd", 2024), ("ta", 2025), ("stok", 2024), ("mdv", 2025), ("tb", 2025),
                                  ("uvyk", 2024), ("ok", 2025), ("ns", 2024), ("smm", 2025), ("bk", 2025),
                                  ("dk", 2024), ("fin", 2025), ("nk", 2024)]),
    (krb, "yet-fta-kars-krb", 1, [("hd", 2025), ("ta", 2024), ("stok", 2025), ("dv", 2025), ("modv", 2024),
                                  ("tb", 2024), ("kvmb", 2025), ("uvyk", 2025), ("brut", 2025), ("ind", 2025),
                                  ("fg", 2024), ("dk", 2025), ("aktif", 2025)]),
    (krc, "yet-fta-kars-krc", 5, [("hd", 2025), ("ta", 2025), ("da", 2024), ("stok", 2025), ("mdv", 2024),
                                  ("kvyk", 2025), ("uvyk", 2024), ("ok", 2024), ("ns", 2025), ("smm", 2024),
                                  ("fg", 2025), ("fk", 2025), ("nk", 2025)]),
]:
    F.uyaran(s.uyaran(sid))
    for a, y in secim:
        F.ifade(s, sid, s.degisim(a, str(y)), ifadeler(AD[a], s.onceki(str(y)), y), v, R)

F.uyaran(krd.uyaran("yet-fta-kars-krd"))
for a, y, tur in [("hd", 2024, "yuzde"), ("tb", 2024, "yuzde"), ("kvmb", 2025, "yuzde"), ("ind", 2025, "tutar"),
                  ("fg", 2023, "tutar"), ("nk", 2025, "tutar")]:
    p = krd.onceki(str(y))
    if tur == "yuzde":
        F.ifade(krd, "yet-fta-kars-krd", krd.degisim(a, y), ifadeler(krd.adi(a), p, y), 7, R)
    else:
        F.ifade(krd, "yet-fta-kars-krd", krd.degisim_tutar(a, y),
                f"{p}-{y} yılları arasında {krd.adi(a)} kalemindeki mutlak değişim", 7, R)

# ------------------------------------------------------------------ değişimden hesap
F.hesap(R,
    "Bir işletmenin ticari borçları 2024 yılı sonunda 350.000 ₺’dir. Karşılaştırmalı tablolar analizinde ticari "
    "borçların 2024-2025 değişim yüzdesi −%30 olarak hesaplanmıştır.\n\n2025 yılı sonundaki ticari borç tutarı kaç "
    "₺’dir?",
    Hesap(350_000 * 0.70, "tutar", [350_000 * 1.30, 350_000 / 1.30, 350_000 * 0.30, 350_000 - 30_000],
          "2025 tutarı = 2024 tutarı × (1 − 0,30) = 350.000 × 0,70 = 245.000 ₺; azalış tutarı 105.000 ₺’dir."),
    zorluk="easy")

F.hesap(R,
    "Bir işletmenin kısa vadeli mali borçları 2025 yılı sonunda 242.000 ₺’dir. Bu kalem bir önceki yıla göre %21 "
    "artmıştır.\n\n2024 yılı sonundaki kısa vadeli mali borç tutarı kaç ₺’dir?",
    Hesap(242_000 / 1.21, "tutar", [242_000 * 0.79, 242_000 * 1.21, 242_000 - 21_000, 242_000 * 0.21],
          "Önceki yıl tutarı = cari yıl ÷ (1 + değişim oranı) = 242.000 ÷ 1,21 = 200.000 ₺. %21 düşülerek bulunan "
          "191.180 ₺ yanlış tabanı kullanır."))

F.hesap(R,
    "Bir işletmenin net satışları 2024 yılında bir önceki yıla göre %20 artmış, 2025 yılında ise 2024 yılına göre %10 "
    "azalmıştır.\n\nNet satışların 2023-2025 dönemindeki toplam değişim yüzdesi kaçtır?",
    Hesap((1.20 * 0.90 - 1) * 100, "yuzde", [10, 30, 2, 12],
          "Art arda değişimler çarpılarak birleştirilir: 1,20 × 0,90 = 1,08; toplam değişim %8’dir. Yüzdelerin "
          "toplanması (%10) tabanların farklı olduğunu göz ardı eder."), zorluk="hard")

bk0, bk1 = 800_000 - 560_000, 800_000 * 1.25 - 560_000 * 1.30
F.hesap(R,
    "Bir işletmenin 2024 yılında net satışları 800.000 ₺, satışların maliyeti 560.000 ₺’dir. 2025 yılında net "
    "satışlar %25, satışların maliyeti %30 artmıştır.\n\nBrüt satış kârının 2024-2025 değişim yüzdesi kaçtır?",
    Hesap((bk1 - bk0) / bk0 * 100, "yuzde", [25 - 30 + 25, -5, 25, 30 - 25],
          f"2025 net satışları 1.000.000 ₺, satışların maliyeti 728.000 ₺; brüt kâr 272.000 ₺. 2024 brüt kârı 240.000 ₺ "
          "olduğundan değişim = 32.000 ÷ 240.000 = %13,33."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin 2024 yılı sonunda dönen varlıkları 500.000 ₺, duran varlıkları 1.500.000 ₺’dir. 2025 yılında "
    "dönen varlıklar %10, duran varlıklar %5 artmıştır.\n\nAktif toplamının 2024-2025 değişim yüzdesi kaçtır?",
    Hesap((550_000 + 1_575_000 - 2_000_000) / 2_000_000 * 100, "yuzde", [15, 7.5, 10, 5],
          "2025 aktif toplamı = 550.000 + 1.575.000 = 2.125.000 ₺; değişim = 125.000 ÷ 2.000.000 = %6,25. Oranların "
          "basit ortalaması (%7,5) tutar ağırlıklarını dikkate almaz."))

F.hesap(R,
    "Bir işletmenin stokları 2024 yılı sonunda 480.000 ₺ iken 2025 yılı sonunda 360.000 ₺’ye inmiştir.\n\n"
    "Karşılaştırmalı tablolar analizine göre stokların 2024-2025 değişim yüzdesi kaçtır?",
    Hesap((360_000 - 480_000) / 480_000 * 100, "yuzde", [-(120_000 / 360_000 * 100), 75, 33.33, 133.33],
          "Değişim yüzdesi = (360.000 − 480.000) ÷ 480.000 × 100 = −%25. Taban olarak cari yılın alınması −%33,33 "
          "sonucunu verir."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin ticari alacakları iki yıl içinde 300.000 ₺’den 420.000 ₺’ye çıkmış, aynı dönemde net satışları "
    "1.800.000 ₺’den 2.160.000 ₺’ye yükselmiştir.\n\nTicari alacaklardaki değişim yüzdesi net satışlardaki değişim "
    "yüzdesini kaç puan aşmaktadır?",
    Hesap(40 - 20, "yuzde", [40, 20, 40 / 20 * 10, 120_000 / 360_000 * 100],
          "Alacaklardaki değişim = 120.000 ÷ 300.000 = %40; net satışlardaki değişim = 360.000 ÷ 1.800.000 = %20. Fark "
          "20 puandır; alacaklar satışlardan hızlı arttığından tahsil süresi uzar."))

F.hesap(R,
    "Bir işletmenin öz kaynakları 2024 yılında 1.200.000 ₺, 2025 yılında 1.380.000 ₺’dir. Aynı dönemde yabancı "
    "kaynaklar 800.000 ₺’den 1.020.000 ₺’ye çıkmıştır.\n\nPasif toplamının 2024-2025 değişim yüzdesi kaçtır?",
    Hesap((2_400_000 - 2_000_000) / 2_000_000 * 100, "yuzde", [15, 27.5, (15 + 27.5) / 2, 400_000 / 2_400_000 * 100],
          "Pasif toplamı 2.000.000 ₺’den 2.400.000 ₺’ye çıkmıştır; değişim = 400.000 ÷ 2.000.000 = %20. Öz kaynaklar "
          "%15, yabancı kaynaklar %27,5 artmıştır."))

# ------------------------------------------------------------------ kavram ve yorum
F.q(R,
    "Bir analist, işletmenin iki yıllık bilançosunu yan yana koyup her kalemin tutar olarak ve yüzde olarak ne kadar "
    "değiştiğini ayrı sütunlarda göstermektedir.\n\nBu analiz yöntemi aşağıdakilerden hangisidir?",
    "Karşılaştırmalı tablolar analizi",
    ["Dikey (yüzde) analiz", "Oran analizi", "Nakit akış analizi", "Fon akım analizi"],
    "Aynı işletmenin iki veya daha fazla dönemine ait tabloların yan yana konup kalemlerdeki mutlak ve yüzde "
    "değişimlerin incelenmesi karşılaştırmalı tablolar (yatay) analizidir.", zorluk="easy")

F.q(R,
    "Bir işletme 2024 yılında 40.000 ₺ net zarar, 2025 yılında 60.000 ₺ net kâr bildirmiştir. Analist, karşılaştırmalı "
    "tabloda bu kalem için değişim yüzdesi sütununu doldurmak istemektedir.\n\nBu durumda uygun yaklaşım "
    "aşağıdakilerden hangisidir?",
    "Tutar değişimi gösterilir, yüzde değişim hesaplanmaz.",
    ["Değişim yüzdesi −%250 olarak gösterilir ve kârlılığın düştüğü yorumlanır.",
     "Değişim yüzdesi %150 olarak gösterilir ve kârlılığın arttığı yorumlanır.",
     "Önceki yıl zarar olduğundan her iki yılın tutarı da tablodan çıkarılır.",
     "Değişim yüzdesi 2025 tutarı taban alınarak %166,67 olarak hesaplanır."],
    "Baz değer negatif ya da sıfır olduğunda yüzde değişim yanıltıcı işaret verir (−%250 bir artışı düşüş gibi "
    "gösterir). Bu kalemlerde mutlak değişim gösterilir ve yüzde sütunu boş bırakılır.", zorluk="hard")

F.q(R,
    "Bir işletmenin karşılaştırmalı bilançosunda dönen varlıkların %8, kısa vadeli yabancı kaynakların %35 arttığı "
    "görülmektedir. Önceki yıl cari oran 1,5’tir.\n\nBu gelişmeye ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Cari oran düşmüş, kısa vadeli ödeme gücü zayıflamıştır.",
    ["Cari oran yükselmiş, kısa vadeli ödeme gücü güçlenmiştir.",
     "Dönen varlıklar arttığından likidite iyileşmiştir.",
     "KVYK artışı uzun vadeli finansman yapısını güçlendirmiştir.",
     "İki kalem de arttığından cari oran değişmemiştir."],
    "Yeni cari oran = 1,5 × 1,08 ÷ 1,35 = 1,20’dir. KVYK dönen varlıklardan çok daha hızlı arttığından kısa vadeli "
    "ödeme gücü zayıflamıştır.")

F.q(R,
    "Bir işletmenin karşılaştırmalı tablolarında geçmiş yıllar kârlarının %40, ödenmiş sermayenin %0, uzun vadeli "
    "banka kredilerinin −%15 değiştiği görülmektedir. Aktif toplamı %6 artmıştır.\n\nBu gelişmeye ilişkin aşağıdaki "
    "yorumlardan hangisi doğrudur?",
    "Büyüme işletmede bırakılan kârlarla karşılanmıştır.",
    ["Büyüme sermaye artırımıyla finanse edilmiştir.",
     "Büyüme yeni uzun vadeli kredilerle finanse edilmiştir.",
     "Öz kaynaklar azalırken yabancı kaynaklar artmıştır.",
     "Aktif artışı borçlanmanın artmasından kaynaklanmıştır."],
    "Sermaye değişmemiş, uzun vadeli krediler azalmış, geçmiş yıllar kârları artmıştır. Aktif büyümesi işletmede "
    "bırakılan kârlarla, yani otofinansmanla karşılanmıştır.")

F.q(R,
    "Bir işletmenin karşılaştırmalı tablosunda hazır değerler 20.000 ₺’den 40.000 ₺’ye (%100 artış), maddi duran "
    "varlıklar 5.000.000 ₺’den 5.500.000 ₺’ye (%10 artış) çıkmıştır.\n\nBu tabloya ilişkin aşağıdaki yorumlardan "
    "hangisi doğrudur?",
    "Maddi duran varlık artışı tutar olarak çok daha önemlidir.",
    ["Hazır değerlerdeki artış tutar olarak da en önemli değişimdir.",
     "Yüzde değişimler mutlak tutardan bağımsız olarak önem sırasını gösterir.",
     "Maddi duran varlıklardaki artış yüzde küçük olduğu için önemsizdir.",
     "İki kalemin artışı işletmenin likiditesini aynı ölçüde etkiler."],
    "Karşılaştırmalı analizde yüzde ve mutlak değişim birlikte değerlendirilir. Hazır değerlerdeki %100 artış 20.000 "
    "₺, maddi duran varlıklardaki %10 artış ise 500.000 ₺’dir; küçük tabanlı kalemlerde yüzde yanıltıcı olabilir.")

F.q(R,
    "Bir finansal analiz kursunda karşılaştırmalı tablolar analizine ilişkin ifadeler tartışılmış, katılımcılardan "
    "hatalı olanı bulmaları istenmiştir.\n\nKarşılaştırmalı tablolar analiziyle ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Değişim yüzdesi cari yıl tutarı taban alınarak hesaplanır.",
    ["Karşılaştırma için en az iki dönemin tabloları yan yana konur.",
     "Kalemlerdeki mutlak ve yüzde değişimler gösterilir.",
     "Azalışlar negatif değişim yüzdesiyle gösterilir.",
     "İlişkili kalemlerdeki değişimler birlikte yorumlanır."],
    "Değişim yüzdesi önceki (karşılaştırılan) dönem tutarı taban alınarak hesaplanır: (cari − önceki) ÷ önceki. Cari "
    "yılın taban alınması değişimi olduğundan küçük gösterir.")

F.q(R,
    "Bir işletmenin karşılaştırmalı gelir tablosunda net satışların %12, faaliyet giderlerinin %28 arttığı, brüt satış "
    "kârının ise %12 arttığı görülmektedir.\n\nBu gelişmenin faaliyet kârına etkisiyle ilgili aşağıdakilerden "
    "hangisi doğrudur?",
    "Faaliyet kârı brüt kârdan yavaş artar ya da azalır.",
    ["Faaliyet kârı brüt kârdan hızlı artar.",
     "Faaliyet kârı net satışlarla aynı oranda artar.",
     "Faaliyet giderleri faaliyet kârını etkilemez.",
     "Faaliyet kârı faaliyet giderleriyle aynı oranda artar."],
    "Faaliyet kârı = brüt kâr − faaliyet giderleri. Giderler brüt kârdan hızlı arttığında faaliyet kârındaki artış "
    "brüt kârdaki artıştan düşük kalır; giderlerin ağırlığına göre azalış da görülebilir.")

if __name__ == "__main__":
    sys.exit(F.yaz())
