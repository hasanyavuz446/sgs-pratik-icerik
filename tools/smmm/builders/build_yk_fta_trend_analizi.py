# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Trend (Eğilim Yüzdeleri) Analizi — 60 soru, 2026 test biçimi.

Gerçek kitapçıklardaki gibi dört-beş yıllık özet tablolarda farklı baz yıllara göre eğilim yüzdeleri; trend
yüzdesinden tutara, baz yıl değiştirmeye ve iki serinin ilişkisinden oran yorumuna giden hesaplar; iki
serinin trend grafiğini yorumlama soruları sorulur.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from fta_ortak import Seri, Sirket, Fta, Hesap, grafik, AD

P = Paket("questions_topic_trend_analizi_2026.json", lesson="mali_tablolar_analizi", topic="trend_analizi",
          konu_adi="Trend Analizi", seed=2026093103,
          surum="Finansal tablolar analizi: trend (eğilim yüzdeleri) yöntemi; 30.09.2026 kontrolü")
F = Fta(P, "yet-fta-trend-")
R = "Trend (eğilim yüzdeleri) analizi"

tra = Seri("TRA A.Ş.", range(2021, 2026), [
    ("Net Satışlar", "ns", [800_000, 920_000, 1_040_000, 1_200_000, 1_360_000]),
    ("Satışların Maliyeti", "smm", [560_000, 660_000, 770_000, 900_000, 1_040_000]),
    ("Ticari Alacaklar", "ta", [120_000, 150_000, 170_000, 210_000, 250_000]),
    ("Stoklar", "stok", [100_000, 110_000, 130_000, 150_000, 160_000]),
    ("Dönen Varlıklar", "dv", [300_000, 330_000, 380_000, 440_000, 480_000]),
    ("Kısa Vadeli Yabancı Kaynaklar", "kvyk", [200_000, 230_000, 260_000, 310_000, 350_000]),
    ("Faaliyet Kârı", "fk", [90_000, 96_000, 100_000, 110_000, 118_000]),
    ("Dönem Net Kârı", "nk", [50_000, 52_000, 60_000, 58_000, 66_000])])
trb = Seri("TRB A.Ş.", range(2021, 2026), [
    ("Net Satışlar", "ns", [2_500_000, 2_400_000, 2_750_000, 3_100_000, 3_500_000]),
    ("Satışların Maliyeti", "smm", [1_800_000, 1_740_000, 2_020_000, 2_300_000, 2_590_000]),
    ("Hazır Değerler", "hd", [60_000, 45_000, 50_000, 40_000, 30_000]),
    ("Ticari Alacaklar", "ta", [400_000, 420_000, 480_000, 520_000, 560_000]),
    ("Stoklar", "stok", [350_000, 380_000, 400_000, 470_000, 540_000]),
    ("Kısa Vadeli Yabancı Kaynaklar", "kvyk", [600_000, 640_000, 700_000, 790_000, 900_000]),
    ("Faaliyet Giderleri", "fg", [350_000, 360_000, 400_000, 450_000, 500_000]),
    ("Dönem Net Kârı", "nk", [150_000, 120_000, 140_000, 160_000, 180_000])])
trc = Seri("TRC A.Ş.", range(2022, 2026), [
    ("Ticari Alacaklar", "ta", [200_000, 230_000, 260_000, 240_000]),
    ("Stoklar", "stok", [180_000, 162_000, 150_000, 225_000]),
    ("Net Satışlar", "ns", [500_000, 575_000, 640_000, 700_000]),
    ("Maddi Duran Varlıklar", "mdv", [900_000, 950_000, 1_020_000, 1_080_000]),
    ("Öz Kaynaklar", "ok", [700_000, 740_000, 800_000, 850_000])])
trm = Sirket("TRM A.Ş.", ("2023", "2024", "2025"),
             hd=[70_000, 50_000, 90_000], ta=[240_000, 290_000, 330_000], stok=[210_000, 260_000, 250_000],
             mdv=[750_000, 800_000, 880_000], modv=[50_000, 60_000, 70_000], tb=[160_000, 190_000, 230_000],
             uvmb=[300_000, 330_000, 290_000], sermaye=[550_000] * 3, gyk=[30_000, 60_000, 90_000],
             brut=[1_850_000, 2_230_000, 2_520_000], ind=[50_000, 30_000, 20_000],
             smm=[1_300_000, 1_580_000, 1_760_000], fg=[290_000, 350_000, 400_000], fin=[70_000, 80_000, 90_000])
trn = Sirket("TRN A.Ş.", ("2023", "2024", "2025"),
             hd=[20_000, 35_000, 25_000], mk=[15_000, 10_000, 30_000], ta=[330_000, 360_000, 420_000],
             da=[10_000, 20_000, 15_000], stok=[280_000, 300_000, 370_000], mdv=[980_000, 1_050_000, 1_100_000],
             modv=[70_000, 80_000, 90_000], tb=[250_000, 270_000, 330_000], db=[30_000, 35_000, 40_000],
             uvmb=[420_000, 400_000, 450_000], sermaye=[700_000] * 3, gyk=[50_000, 70_000, 100_000],
             brut=[2_650_000, 2_950_000, 3_420_000], ind=[50_000, 50_000, 120_000],
             smm=[1_950_000, 2_150_000, 2_480_000], fg=[380_000, 420_000, 480_000], fin=[100_000, 120_000, 140_000])


def ifadeler(s, a, y, baz):
    k = s.adi(a) if isinstance(s, Seri) else AD[a]
    return [f"{baz} yılı baz alındığında {y} yılı {k} trend yüzdesi",
            f"{baz} baz yıllı trend analizinde {k} kaleminin {y} yılı eğilim yüzdesi",
            f"{y} yılında {k} kaleminin {baz} yılına göre trend yüzdesi"]


# Aynı şirkette her kalem bir kez sorulur: yıl değiştirilerek tekrarlanan soru yalnız sayı değiştirmek olur.
for s, sid, v, secim in [
    (tra, "yet-fta-trend-tra", 0, [("ns", 2025, 2021), ("smm", 2024, 2021), ("ta", 2025, 2022), ("stok", 2023, 2021),
                                   ("dv", 2025, 2023), ("kvyk", 2024, 2022), ("fk", 2025, 2021), ("nk", 2024, 2021)]),
    (trb, "yet-fta-trend-trb", 1, [("ns", 2022, 2021), ("smm", 2025, 2022), ("hd", 2025, 2021), ("ta", 2024, 2022),
                                   ("stok", 2025, 2023), ("kvyk", 2023, 2021), ("fg", 2025, 2022), ("nk", 2022, 2021)]),
    (trc, "yet-fta-trend-trc", 6, [("ta", 2024, 2022), ("stok", 2025, 2022), ("ns", 2025, 2023), ("mdv", 2025, 2022),
                                   ("ok", 2024, 2023)]),
    (trm, "yet-fta-trend-trm", 7, [("ns", 2025, 2023), ("smm", 2024, 2023), ("bk", 2025, 2023), ("fg", 2025, 2024),
                                   ("fk", 2024, 2023), ("nk", 2025, 2023), ("hd", 2025, 2024), ("ta", 2025, 2023),
                                   ("stok", 2024, 2023), ("dv", 2025, 2023), ("mdv", 2025, 2024), ("kvyk", 2025, 2023),
                                   ("ok", 2025, 2023)]),
    (trn, "yet-fta-trend-trn", 9, [("brut", 2025, 2023), ("ind", 2025, 2024), ("fin", 2025, 2023), ("dk", 2024, 2023),
                                   ("tb", 2025, 2023), ("kvmb", 2025, 2024), ("uvyk", 2025, 2023), ("aktif", 2025, 2023),
                                   ("duran", 2024, 2023), ("modv", 2025, 2023), ("gyk", 2025, 2023), ("mk", 2025, 2024),
                                   ("da", 2024, 2023)]),
]:
    F.uyaran(s.uyaran(sid))
    for a, y, baz in secim:
        F.ifade(s, sid, s.trend(a, str(y), str(baz)), ifadeler(s, a, y, baz), v, R)

# ------------------------------------------------------------------ trend yüzdesinden hesap
F.hesap(R,
    "Bir işletmenin 2022 yılı baz alınarak yapılan trend analizinde stokların 2025 yılı eğilim yüzdesi %132 olarak "
    "hesaplanmıştır. İşletmenin 2022 yılı sonundaki stok tutarı 250.000 ₺’dir.\n\n2025 yılı sonundaki stok tutarı "
    "kaç ₺’dir?",
    Hesap(250_000 * 1.32, "tutar", [250_000 * 0.32, 250_000 / 1.32, 250_000 * 1.68, 250_000 * 2.32],
          "Trend yüzdesi = cari yıl ÷ baz yıl × 100; 2025 stoku = 250.000 × 1,32 = 330.000 ₺. Artış tutarı 80.000 ₺’dir."),
    zorluk="easy")

F.hesap(R,
    "Bir işletmenin 2021 yılı baz alınarak hazırlanan trend analizinde net satışların eğilim yüzdesi 2023 yılında "
    "%125, 2025 yılında %150’dir.\n\n2023 yılı baz alınırsa net satışların 2025 yılı trend yüzdesi kaç olur?",
    Hesap(150 / 125 * 100, "yuzde", [150 - 125, 125, 150 + 25, 125 / 150 * 100],
          "Baz yıl değiştirilirken iki eğilim yüzdesi birbirine bölünür: 150 ÷ 125 × 100 = %120. Puan farkı (25) "
          "yüzde değişim değildir."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin trend analizinde faaliyet giderlerinin eğilim yüzdesi 2024 yılında %140, 2025 yılında %154 "
    "olarak hesaplanmıştır; baz yıl her iki hesapta aynıdır.\n\nFaaliyet giderleri 2025 yılında bir önceki yıla "
    "göre yüzde kaç artmıştır?",
    Hesap((154 / 140 - 1) * 100, "yuzde", [14, 54, 40, 154 / 140 * 100],
          "Yıllık artış = 154 ÷ 140 − 1 = %10. Eğilim yüzdeleri arasındaki 14 puanlık fark baz yıla göre ölçülür, yıllık "
          "artış oranı değildir."))

F.hesap(R,
    "Bir işletmenin 2025 yılı sonunda ticari alacakları 390.000 ₺’dir ve bu kalemin trend yüzdesi %130 olarak "
    "hesaplanmıştır.\n\nBaz yıldaki ticari alacak tutarı kaç ₺’dir?",
    Hesap(390_000 / 1.30, "tutar", [390_000 * 0.70, 390_000 * 1.30, 390_000 - 130_000, 390_000 * 0.30],
          "Baz yıl tutarı = cari yıl tutarı ÷ trend oranı = 390.000 ÷ 1,30 = 300.000 ₺. %30 düşülerek hesaplamak "
          "(273.000 ₺) hatalıdır."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin baz yılda dönem sonu ticari alacaklara göre hesaplanan tahsil süresi 48 gündür. Baz yıla göre "
    "trend analizinde 2025 yılı için net satışların eğilim yüzdesi %150, ticari alacakların eğilim yüzdesi %180’dir."
    "\n\nAynı yöntemle hesaplanan 2025 yılı tahsil süresi kaç gündür?",
    Hesap(48 * 180 / 150, "gun", [48 * 150 / 180, 48 * 1.30, 48 + 30, 48 * 1.8],
          "Tahsil süresi = 360 × alacak ÷ net satış olduğundan alacaklar 1,8, satışlar 1,5 kat arttığında süre 1,8 ÷ 1,5 "
          "= 1,2 katına çıkar: 48 × 1,2 = 57,60 gün."), zorluk="hard")

bk0, bk1 = 1_000_000 - 700_000, 1_400_000 - 1_050_000
F.hesap(R,
    "Bir işletmenin baz yılda net satışları 1.000.000 ₺, satışların maliyeti 700.000 ₺’dir. Baz yıla göre 2025 "
    "yılında net satışların trend yüzdesi %140, satışların maliyetinin trend yüzdesi %150’dir.\n\nBrüt satış kârının "
    "2025 yılı trend yüzdesi kaçtır?",
    Hesap(bk1 / bk0 * 100, "yuzde", [140 - 150 + 100, 145, 140 / 150 * 100, 150 - 140 + 100],
          "2025 net satışları 1.400.000 ₺, satışların maliyeti 1.050.000 ₺; brüt kâr 350.000 ₺. Baz yıl brüt kârı "
          "300.000 ₺ olduğundan trend yüzdesi = 350.000 ÷ 300.000 = %116,67."), zorluk="hard")

# ------------------------------------------------------------------ grafik yorumu
G = [
    ("tra-g1", "TRE A.Ş.", "Net Satışlar ve Satışların Maliyeti (2021 = 100)",
     [("Net Satışlar", [100, 112, 126, 138, 150]), ("Satışların Maliyeti", [100, 118, 137, 155, 172])],
     "2021'de iki seri 100'dür; net satışlar 2025'te 150'ye, satışların maliyeti 172'ye yükselmektedir.",
     "Brüt satış kârlılığı yıllar itibarıyla azalma eğilimindedir.",
     ["Satışların maliyeti net satışlardan yavaş artmaktadır.",
      "Brüt satış kârlılığı yıllar itibarıyla artış eğilimindedir.",
      "Net satışlar yıllar itibarıyla azalma eğilimindedir.",
      "Faaliyet kârı her yıl aynı oranda artmaktadır."],
     "Satışların maliyeti (%72 artış) net satışlardan (%50 artış) hızlı büyüdüğünden brüt kârın satışlara oranı "
     "düşmektedir. Faaliyet kârı hakkında grafik bilgi vermez."),
    ("trb-g2", "TRF A.Ş.", "Net Satışlar ve Ticari Alacaklar (2022 = 100)",
     [("Net Satışlar", [100, 108, 115, 120]), ("Ticari Alacaklar", [100, 125, 150, 170])],
     "2022'de iki seri 100'dür; net satışlar 2025'te 120'ye, ticari alacaklar 170'e yükselmektedir.",
     "Ortalama tahsil süresi uzamaktadır.",
     ["Ortalama tahsil süresi kısalmaktadır.",
      "Alacak devir hızı artmaktadır.",
      "Müşterilere tanınan vade kısalmaktadır.",
      "Tahsil süresi yıllar itibarıyla değişmemektedir."],
     "Alacaklar satışlardan çok daha hızlı arttığından alacak devir hızı düşer, tahsil süresi uzar; müşterilere daha "
     "uzun vade tanındığı ya da tahsilatın yavaşladığı anlaşılır."),
    ("trc-g3", "TRG A.Ş.", "Dönen Varlıklar, KVYK ve Stoklar (2022 = 100)",
     [("Dönen Varlıklar", [100, 115, 132, 150]), ("KVYK", [100, 104, 110, 115]), ("Stoklar", [100, 102, 105, 108])],
     "2022'de üç seri 100'dür; 2025'te dönen varlıklar 150, KVYK 115, stoklar 108 düzeyindedir.",
     "Likidite gücü iyileşmektedir.",
     ["Likidite oranı azalmaktadır.",
      "Cari oran azalma eğilimindedir.",
      "Stoklar dönen varlıklardan hızlı artmaktadır.",
      "KVYK dönen varlıklardan hızlı artmaktadır."],
     "Dönen varlıklar KVYK’den hızlı, stoklar dönen varlıklardan yavaş artmaktadır; hem cari oran hem stok dışı "
     "dönen varlıklara dayanan likidite oranı yükselir."),
    ("trd-g4", "TRH A.Ş.", "Net Satışlar ve Dönem Net Kârı (2021 = 100)",
     [("Net Satışlar", [100, 120, 140, 165, 190]), ("Dönem Net Kârı", [100, 104, 110, 112, 118])],
     "2021'de iki seri 100'dür; 2025'te net satışlar 190, dönem net kârı 118 düzeyindedir.",
     "Net kâr marjı yıllar itibarıyla azalmaktadır.",
     ["Net kâr marjı yıllar itibarıyla artmaktadır.",
      "Dönem net kârı yıllar itibarıyla azalmaktadır.",
      "Net satışlar dönem net kârından yavaş artmaktadır.",
      "Net kâr marjı yıllar itibarıyla değişmemektedir."],
     "Dönem net kârı artsa da (%18) net satışlardaki artışın (%90) çok gerisinde kaldığından net kârın satışlara "
     "oranı düşmektedir."),
    ("tre-g5", "TRJ A.Ş.", "Stoklar ve Satışların Maliyeti (2022 = 100)",
     [("Stoklar", [100, 130, 165, 200]), ("Satışların Maliyeti", [100, 110, 118, 125])],
     "2022'de iki seri 100'dür; 2025'te stoklar 200, satışların maliyeti 125 düzeyindedir.",
     "Stok devir süresi uzamaktadır.",
     ["Stok devir hızı artmaktadır.",
      "Stoklar daha hızlı satılmaktadır.",
      "Stok devir süresi kısalmaktadır.",
      "Stok devir hızı değişmemektedir."],
     "Stoklar satışların maliyetinden çok hızlı arttığından stok devir hızı (SMM ÷ ortalama stok) düşer ve devir "
     "süresi uzar; stoklarda birikme vardır."),
]
def kucuk(metin):
    """Başlığı cümle içine alır; KVYK gibi kısaltmalar büyük harfle kalır."""
    return " ".join(w if w.isupper() and len(w) > 1 else w.replace("I", "ı").replace("İ", "i").lower() for w in metin.split())


for kod, ad, baslik, seriler, alt, dogru, cel, coz in G:
    yil0 = int(baslik.split("(")[1][:4])
    labels = [str(yil0 + i) for i in range(len(seriler[0][1]))]
    sid = F.uyaran(grafik(f"yet-fta-trend-{kod}", ad, baslik, labels, seriler, alt,
                          f"Grafikte {ad}’nin {kucuk(baslik.split(' (')[0])} için {yil0} yılı 100 kabul edilerek "
                          "hesaplanan eğilim yüzdeleri gösterilmiştir."))
    F.q(R, f"{ad}’nin trend grafiğine göre aşağıdaki yorumlardan hangisi doğrudur?", dogru, cel, coz,
        stimulus_id=sid)

# ------------------------------------------------------------------ kavram
F.q(R,
    "Bir analist, işletmenin beş yıllık finansal tablolarında her kalemin seçilen bir yıla göre nasıl geliştiğini "
    "görmek için o yılın tutarlarını 100 kabul edip diğer yılları buna oranlamaktadır.\n\nBu yöntemde baz yıl "
    "seçimiyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Olağan dışı olaylardan etkilenmemiş normal bir yıl seçilmelidir.",
    ["Kalemlerin en yüksek değer aldığı yıl seçilmelidir.",
     "Her kalem için farklı bir baz yıl seçilmelidir.",
     "Kalemlerin en düşük değer aldığı yıl seçilmelidir.",
     "Son yıl baz alınarak geçmiş yıllar geriye doğru hesaplanmalıdır."],
    "Trend analizinde baz yıl, karşılaştırmaları çarpıtmaması için olağan faaliyet koşullarını yansıtan normal bir "
    "yıl olmalıdır; tüm kalemlerde aynı baz yıl kullanılır.")

F.q(R,
    "Bir finansal analiz eğitiminde trend analizine ilişkin ifadeler tartışılmış ve katılımcılardan hatalı olanı "
    "bulmaları istenmiştir.\n\nTrend analiziyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Baz yılı negatif ya da sıfır olan kalemlerde trend yüzdesi anlamlı yorumlanır.",
    ["Kalemlerin uzun dönemli gelişim yönünü gösterir.",
     "Baz yıl tutarı 100 kabul edilerek diğer yıllar buna oranlanır.",
     "İlişkili kalemlerin eğilimleri birlikte değerlendirilmelidir.",
     "Enflasyon dönemlerinde tutarların reel gelişimi ayrıca değerlendirilir."],
    "Baz değer negatif ya da sıfırsa oran hesaplanamaz ya da yanıltıcı işaret verir; bu kalemlerde trend yüzdesi "
    "yorumlanmaz, mutlak tutar değişimi incelenir.")

if __name__ == "__main__":
    sys.exit(F.yaz())
