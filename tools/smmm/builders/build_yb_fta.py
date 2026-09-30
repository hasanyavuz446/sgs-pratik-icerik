# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

2026/1 kitapçığındaki gibi her testin ilk 15 sorusu tek bir şirketin üç yıllık bilanço ve gelir tablosuna
bağlıdır (likidite, faaliyet ve kârlılık oranları, dikey ve trend yüzdeleri, karşılaştırmalı değişim, satışlardan
nakit girişi); ardından iki hedef değer hesabı, bir trend grafiği yorumu ve iki TMS 1 sorusu gelir. Konu
havuzundaki şirketler ve olaylar tekrar edilmez; dayanaklar konu builder'larıyla aynıdır (build_yk_fta_*.py).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from fta_ortak import Sirket, Fta, Hesap, grafik, AD, IFADE, kok

SURUM = "TMS 1; TMS 7; finansal tablolar analizi genel kabul görmüş yöntemleri; 30.09.2026 kontrolü"
L = "mali_tablolar_analizi"
R = "Finansal tablolar analizi"
Y = ("2023", "2024", "2025")


def paket(dosya, seed, ek=()):
    return Paket(dosya, lesson=L, topic="oran_analizi", konu_adi="Finansal Tablolar ve Analizi", seed=seed,
                 surum=SURUM, havuz="bolum", ek_idler=ek)


T = [Fta(paket("questions_finansal_analiz_2026.json", 2026093111,
               ek=("yet-analiz-t1-0018", "yet-analiz-t1-0019", "yet-analiz-t1-0020")), "yet-fta-yb1-"),
     Fta(paket("questions_analiz_test2_2026.json", 2026093112), "yet-fta-yb2-"),
     Fta(paket("questions_analiz_test3_2026.json", 2026093113), "yet-fta-yb3-")]

SIRKET = [
    Sirket("YBA A.Ş.", Y, hd=[35_000, 50_000, 25_000], ta=[310_000, 350_000, 410_000], stok=[240_000, 290_000, 380_000],
           mdv=[700_000, 730_000, 780_000], modv=[90_000, 110_000, 130_000], tb=[210_000, 260_000, 330_000],
           uvmb=[420_000, 380_000, 350_000], sermaye=[500_000] * 3, gyk=[30_000, 55_000, 80_000],
           brut=[2_350_000, 2_880_000, 3_460_000], ind=[50_000, 80_000, 60_000], smm=[1_720_000, 2_100_000, 2_550_000],
           fg=[330_000, 410_000, 470_000], fin=[80_000, 95_000, 110_000]),
    Sirket("YBB A.Ş.", Y, hd=[45_000, 25_000, 40_000], mk=[10_000, 15_000, 5_000], ta=[260_000, 300_000, 290_000],
           stok=[180_000, 240_000, 260_000], ddv=[15_000, 20_000, 25_000], mdv=[820_000, 860_000, 900_000],
           modv=[60_000, 55_000, 70_000], tb=[190_000, 230_000, 250_000], db=[25_000, 30_000, 20_000],
           uvmb=[350_000, 330_000, 380_000], sermaye=[600_000] * 3, gyk=[40_000, 60_000, 85_000],
           brut=[2_030_000, 2_260_000, 2_590_000], ind=[30_000, 60_000, 90_000], smm=[1_460_000, 1_650_000, 1_850_000],
           fg=[300_000, 330_000, 380_000], fin=[70_000, 80_000, 90_000]),
    Sirket("YBC A.Ş.", Y, hd=[60_000, 40_000, 55_000], ta=[450_000, 520_000, 610_000], da=[20_000, 25_000, 15_000],
           stok=[390_000, 450_000, 480_000], mdv=[1_300_000, 1_380_000, 1_420_000], modv=[110_000, 120_000, 140_000],
           tb=[340_000, 400_000, 470_000], uvmb=[520_000, 600_000, 560_000], sermaye=[1_000_000] * 3,
           gyk=[70_000, 110_000, 150_000], brut=[3_620_000, 4_080_000, 4_660_000], ind=[20_000, 80_000, 60_000],
           smm=[2_700_000, 3_050_000, 3_450_000], fg=[520_000, 580_000, 640_000], fin=[130_000, 150_000, 170_000]),
]
# (tür, kalem/ölçü, yıl, baz) — her şirkette her ölçü ve kalem bir kez
SECIM = [
    [("o", "nis", 2025), ("o", "cari", 2025), ("o", "likidite", 2025), ("o", "stok_sure", 2025), ("o", "alacak_sure", 2025),
     ("o", "borc_sure", 2025), ("o", "brut_marj", 2025), ("o", "faal_marj", 2023), ("o", "varlik_karl", 2024),
     ("d", "brut", 2023), ("d", "kvmb", 2024), ("t", "dv", 2025, 2023), ("t", "ns", 2024, 2023),
     ("o", "satis_nakit", 2025), ("k", "hd", 2024)],
    [("t", "stok", 2024, 2023), ("t", "ns", 2025, 2024), ("o", "stok_hiz", 2025), ("o", "nis", 2024), ("o", "cari", 2024),
     ("o", "alacak_sure", 2024), ("o", "brut_marj", 2024), ("d", "nk", 2025), ("d", "kvmb", 2025), ("d", "ind", 2025),
     ("k", "tb", 2025), ("k", "uvyk", 2025), ("o", "kaldirac", 2025), ("o", "ds_oran", 2024), ("o", "alim_nakit", 2025)],
    [("o", "cari", 2023), ("o", "likidite", 2024), ("o", "nakit_orani", 2025), ("o", "stok_sure", 2024),
     ("o", "borc_sure", 2025), ("o", "aktif_hiz", 2025), ("o", "net_marj", 2025), ("o", "ozk_karl", 2024),
     ("o", "borc_ozk", 2025), ("d", "smm", 2024), ("d", "ta", 2025), ("t", "ta", 2025, 2023), ("k", "stok", 2025),
     ("o", "satis_nakit", 2024), ("o", "faal_marj", 2025)],
]
for F, s, secim, v in zip(T, SIRKET, SECIM, (0, 5, 7)):
    sid = F.uyaran(s.uyaran(f"{F.onek}{s.ad[:3].lower()}"))
    for tur, a, y, *baz in secim:
        y = str(y)
        if tur == "o":
            F.olcu(s, sid, a, y, v, R, topic="nakit_akim_analizi" if a.endswith("nakit") else "oran_analizi")
        elif tur == "d":
            F.ifade(s, sid, s.dikey(a, y), f"{y} yılı dikey yüzde analizinde {AD[a]} kaleminin payı", v, R,
                    topic="dikey_analiz")
        elif tur == "t":
            F.ifade(s, sid, s.trend(a, y, str(baz[0])), f"{baz[0]} yılı baz alındığında {y} yılı {AD[a]} trend yüzdesi",
                    v, R, topic="trend_analizi")
        else:
            F.ifade(s, sid, s.degisim(a, y), f"karşılaştırmalı analizde {AD[a]} kaleminin {s.onceki(y)}-{y} değişim "
                    "oranı", v, R, topic="karsilastirmali_analiz")

KURAL = "(Devir hızlarında ortalama değeri kullanınız ve bir yılı 360 gün kabul ediniz.)"
T1, T2, T3 = T
# =============================================================================================== TEST 1 ek
o1 = 540_000 * 45 / 360
T1.hesap(R,
    "Bir firmanın 2025 yılı sonunda ticari alacakları 50.000 ₺’dir. 2026 yılı net satışlarının 540.000 ₺ olacağı "
    "öngörülmekte ve ortalama tahsil süresinin 45 gün olması hedeflenmektedir.\n\nBu hedef için 2026 yılı sonunda "
    f"ticari alacak tutarı kaç ₺ olmalıdır?\n{KURAL}",
    Hesap(2 * o1 - 50_000, "tutar", [o1, 2 * o1, 50_000 + o1, 2 * 540_000 * 45 / 365 - 50_000],
          f"Ortalama alacak = 540.000 × 45 ÷ 360 = {o1:,.0f} ₺. (50.000 + X) ÷ 2 = {o1:,.0f} olduğundan X = "
          f"{2 * o1 - 50_000:,.0f} ₺.".replace(",", ".")), topic="oran_analizi", zorluk="hard")
T1.hesap(R,
    "Bir firmanın izleyen dönem sonunda dönen varlıklarının 360.000 ₺, kısa vadeli yabancı kaynaklarının 240.000 ₺ "
    "olması, likidite oranının ise 0,75 olması hedeflenmektedir.\n\nLikidite oranı hedefine ulaşmak için dönem sonu "
    "stok tutarı kaç ₺ olmalıdır?",
    Hesap(360_000 - 0.75 * 240_000, "tutar", [0.75 * 240_000, 240_000, 360_000 - 240_000, 360_000 * 0.25],
          "0,75 = (360.000 − S) ÷ 240.000; 360.000 − S = 180.000 ve S = 180.000 ₺. Cari oran 1,5 olarak kalır."),
    topic="oran_analizi")
sid = T1.uyaran(grafik("yet-fta-yb1-g", "YBD A.Ş.", "Net Satışlar ve Satışların Maliyeti (2021 = 100)",
                       [str(y) for y in range(2021, 2026)],
                       [("Net Satışlar", [100, 118, 135, 150, 170]), ("Satışların Maliyeti", [100, 110, 121, 130, 140])],
                       "2021'de iki seri 100'dür; 2025'te net satışlar 170, satışların maliyeti 140 düzeyindedir.",
                       "Grafikte YBD A.Ş.’nin net satışları ve satışların maliyeti için 2021 yılı 100 kabul edilerek "
                       "hesaplanan eğilim yüzdeleri gösterilmiştir."))
T1.q(R, "YBD A.Ş.’nin trend grafiğine göre aşağıdaki yorumlardan hangisi doğrudur?",
     "Brüt satış kârlılığı artış eğilimindedir.",
     ["Brüt satış kârlılığı azalma eğilimindedir.", "Satışların maliyeti net satışlardan hızlı artmaktadır.",
      "Net satışlar yıllar itibarıyla azalmaktadır.", "Faaliyet giderleri azalma eğilimindedir."],
     "Net satışlar (%70) satışların maliyetinden (%40) hızlı arttığından brüt kârın satışlara oranı yükselmektedir. "
     "Faaliyet giderleri hakkında grafik bilgi vermez.", stimulus_id=sid, topic="trend_analizi")
T1.q("TMS 1 md. 10",
    "TMS 1 Finansal Tabloların Sunuluşu’na göre aşağıdakilerden hangisi tam bir finansal tablo setinde yer almaz?",
    "Katma değer tablosu",
    ["Nakit akış tablosu", "Finansal durum tablosu", "Öz kaynak değişim tablosu", "Dipnotlar"],
    "Tam set; finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, öz kaynak değişim tablosu, nakit "
    "akış tablosu ve dipnotlardan oluşur. Katma değer tablosu standardın öngördüğü tablolardan değildir.",
    topic="finansal_tablolar", zorluk="easy")
T1.q(R,
    "Bir işletme yıl içinde yabancı para cinsinden faaliyet gösteren bağlı ortaklığının tablolarını çevirmiş, oluşan "
    "çevrim farkını kâr veya zarara değil öz kaynakta izlemiştir.\n\nBu çevrim farkı hangi kalemde sunulur?",
    "Diğer kapsamlı gelir",
    ["Esas faaliyet gelirleri", "Finansman gelirleri", "Satış gelirleri", "Olağandışı gelirler"],
    "Yurt dışı faaliyetin çevriminden doğan kur farkları diğer kapsamlı gelir olarak sunulur ve öz kaynakta birikir; "
    "kâr veya zarar tablosuna yansıtılmaz.", topic="finansal_tablolar")

# =============================================================================================== TEST 2 ek
o2 = 1_440_000 * 30 / 360
T2.hesap(R,
    "Bir ticari firmanın 2025 yılı sonunda ticari borçları 90.000 ₺’dir. 2026 yılında satışların maliyetinin "
    "1.440.000 ₺ olacağı tahmin edilmekte ve ortalama borç ödeme süresinin 30 gün olması hedeflenmektedir.\n\nBu hedefi "
    f"karşılamak için 2026 yılı sonunda ticari borç tutarı kaç ₺ olmalıdır?\n{KURAL}",
    Hesap(2 * o2 - 90_000, "tutar", [o2, 2 * o2, 90_000, 2 * 1_440_000 * 30 / 365 - 90_000],
          "Ortalama ticari borç = 1.440.000 × 30 ÷ 360 = 120.000 ₺. (90.000 + X) ÷ 2 = 120.000 olduğundan X = 150.000 ₺."),
    topic="oran_analizi", zorluk="hard")
T2.hesap(R,
    "Kaldıraç oranı toplam yabancı kaynakların pasif toplamına bölünmesiyle hesaplanmaktadır. Bir mali analizde pasif "
    "toplamına göre devamlı sermaye oranı %64, uzun vadeli yabancı kaynak oranı %18 olarak bulunmuştur.\n\nBu verilere "
    "göre kaldıraç oranı yüzde (%) kaçtır?",
    Hesap(100 - (64 - 18), "yuzde", [36, 46, 82, 18],
          "Öz kaynak oranı = %64 − %18 = %46; kaldıraç oranı = %100 − %46 = %54 (KVYK %36 + UVYK %18)."),
    topic="oran_analizi")
sid = T2.uyaran(grafik("yet-fta-yb2-g", "YBE A.Ş.", "Net Satışlar ve Ticari Alacaklar (2022 = 100)",
                       [str(y) for y in range(2022, 2026)],
                       [("Net Satışlar", [100, 125, 150, 180]), ("Ticari Alacaklar", [100, 110, 118, 126])],
                       "2022'de iki seri 100'dür; 2025'te net satışlar 180, ticari alacaklar 126 düzeyindedir.",
                       "Grafikte YBE A.Ş.’nin net satışları ve ticari alacakları için 2022 yılı 100 kabul edilerek "
                       "hesaplanan eğilim yüzdeleri gösterilmiştir."))
T2.q(R, "YBE A.Ş.’nin trend grafiğine göre aşağıdaki yorumlardan hangisi doğrudur?",
     "Ortalama tahsil süresi kısalmaktadır.",
     ["Ortalama tahsil süresi uzamaktadır.", "Alacak devir hızı azalmaktadır.", "Müşterilere tanınan vadeler uzamaktadır.",
      "Tahsil süresi yıllar itibarıyla değişmemektedir."],
     "Net satışlar (%80) ticari alacaklardan (%26) çok daha hızlı arttığından alacak devir hızı yükselir, tahsil süresi "
     "kısalır.", stimulus_id=sid, topic="trend_analizi")
T2.q("TMS 1 md. 69",
    "TMS 1’e göre aşağıdakilerden hangisi bir yükümlülüğün kısa vadeli olarak sınıflandırılması için yeterli bir "
    "koşuldur?",
    "Raporlama tarihinden sonraki on iki ay içinde ödenecek olması",
    ["Yükümlülüğün bir banka kredisi olması", "Faiz oranının değişken olması",
     "Yükümlülüğün yabancı para cinsinden olması", "Teminat gösterilmeden alınmış olması"],
    "TMS 1 md. 69’a göre yükümlülük; normal faaliyet döngüsünde ödenmesi bekleniyorsa, alım satım amaçlı tutuluyorsa, "
    "raporlama tarihinden sonraki on iki ay içinde ödenecekse ya da ertelenme hakkı yoksa kısa vadelidir.",
    topic="finansal_tablolar")
T2.q(R,
    "Bir işletme sattığı ticari malın bedeli ile satılan malın maliyetini gelir tablosunda netleştirerek yalnızca "
    "satış kârını göstermek istemektedir.\n\nBu uygulama hakkında aşağıdakilerden hangisi doğrudur?",
    "Hasılat ve maliyet ayrı gösterilir, netleştirme yapılmaz.",
    ["Net sunum önemlilik ilkesi gereği tercih edilir.",
     "Satış kârının gösterilmesi yeterli kabul edilir.",
     "Satılan malın maliyeti dipnotta verilir, tabloda gösterilmez.",
     "Hasılat nakit tahsil edildiği dönemde gösterilir."],
    "Olağan faaliyetlerden elde edilen hasılat ile satışların maliyeti netleştirilmez; her ikisi ayrı kalemler olarak "
    "sunulur. Netleştirme ancak bir standart izin verdiğinde ya da gerektirdiğinde yapılır.", topic="finansal_tablolar")

# =============================================================================================== TEST 3 ek
T3.hesap(R,
    "Bir işletmenin ortak ölçekli gelir tablosunda satış indirimleri %4, dönem net kârı %7 olarak yer almaktadır. "
    "İşletmenin brüt satışları 780.000 ₺’dir.\n\nİşletmenin dönem net kârı kaç ₺’dir?",
    Hesap(780_000 / 1.04 * 0.07, "tutar", [780_000 * 0.07, 780_000 * 0.96 * 0.07, 780_000 / 1.04 * 0.11, 780_000 * 0.03],
          "Brüt satışların dikey yüzdesi %104 olduğundan net satışlar = 780.000 ÷ 1,04 = 750.000 ₺; dönem net kârı = "
          "750.000 × %7 = 52.500 ₺."),
    topic="dikey_analiz", zorluk="hard")
T3.hesap(R,
    "Bir firmanın dönem sonunda kısa vadeli yabancı kaynaklarının 320.000 ₺ olması beklenmektedir. Banka ile yapılan "
    "kredi sözleşmesi cari oranın en az 1,25 olmasını şart koşmaktadır.\n\nFirmanın dönem sonunda sahip olması gereken "
    "en düşük dönen varlık tutarı kaç ₺’dir?",
    Hesap(320_000 * 1.25, "tutar", [320_000 / 1.25, 320_000 + 125_000, 320_000 * 1.5, 320_000 * 0.25],
          "Cari oran = dönen varlıklar ÷ KVYK ≥ 1,25; dönen varlıklar ≥ 320.000 × 1,25 = 400.000 ₺."),
    topic="oran_analizi", zorluk="easy")
sid = T3.uyaran(grafik("yet-fta-yb3-g", "YBF A.Ş.", "Dönen Varlıklar, KVYK ve Stoklar (2022 = 100)",
                       [str(y) for y in range(2022, 2026)],
                       [("Dönen Varlıklar", [100, 104, 108, 112]), ("KVYK", [100, 115, 132, 150]),
                        ("Stoklar", [100, 118, 140, 165])],
                       "2022'de üç seri 100'dür; 2025'te dönen varlıklar 112, KVYK 150, stoklar 165 düzeyindedir.",
                       "Grafikte YBF A.Ş.’nin dönen varlıkları, kısa vadeli yabancı kaynakları ve stokları için 2022 yılı "
                       "100 kabul edilerek hesaplanan eğilim yüzdeleri gösterilmiştir."))
T3.q(R, "YBF A.Ş.’nin trend grafiğine göre aşağıdaki yorumlardan hangisi doğrudur?",
     "Likidite gücü zayıflamaktadır.",
     ["Likidite gücü iyileşmektedir.", "Cari oran artış eğilimindedir.", "Stoklar dönen varlıklardan yavaş artmaktadır.",
      "Likidite oranı artış eğilimindedir."],
     "KVYK dönen varlıklardan hızlı arttığından cari oran düşer; stoklar dönen varlıklardan da hızlı arttığı için stok "
     "dışı dönen varlıklar azalır ve likidite oranı daha da düşer.", stimulus_id=sid, topic="trend_analizi")
T3.q(R,
    "Bir işletmenin yönetimi, işletmenin faaliyetlerini sürdürebilmesi konusunda önemli şüphe doğuran olaylar "
    "bulunduğunu, ancak tasfiye niyeti olmadığını belirlemiştir.\n\nTMS 1’e göre bu durumda yapılması gereken "
    "aşağıdakilerden hangisidir?",
    "Önemli belirsizlikler finansal tablolarda açıklanır.",
    ["Finansal tablolar tasfiye esasına göre hazırlanır.",
     "Belirsizlikler yönetim raporunda gizli tutulur.",
     "Finansal tablolar yayımlanmadan ertelenir.",
     "Varlıklar hurda değerleriyle ölçülür."],
    "Yönetim, süreklilik konusunda önemli şüphe doğuran olay ve koşullara ilişkin önemli belirsizlikleri açıklar; "
    "tasfiye niyeti yoksa tablolar süreklilik esasına göre hazırlanmaya devam eder (TMS 1 md. 25).",
    topic="finansal_tablolar")
T3.q(R,
    "Bir işletme finansal durum tablosunda sunulacak kalemleri belirlerken, standardın asgari olarak ayrı satırda "
    "gösterilmesini istediği kalemleri kontrol etmektedir.\n\nAşağıdakilerden hangisi finansal durum tablosunda ayrıca "
    "sunulması gereken kalemlerdendir?",
    "Stoklar",
    ["Satış gelirleri", "Amortisman giderleri", "Kâr payı gelirleri", "Satışların maliyeti"],
    "TMS 1 md. 54 finansal durum tablosunda asgari olarak maddi duran varlıklar, stoklar, ticari alacaklar, nakit ve "
    "nakit benzerleri, ticari borçlar gibi kalemleri sayar. Diğer seçenekler gelir tablosu kalemleridir.",
    topic="finansal_tablolar", zorluk="easy")

if __name__ == "__main__":
    rc = 0
    for F in T:
        rc |= F.yaz()
    sys.exit(rc)
