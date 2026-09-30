# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Nakit Akış Analizi — 60 soru, 2026 test biçimi.

Dört şirket vakasında iki yıllık bilanço, gelir tablosu ve ek bilgilerden doğrudan yöntemle tahsilat ve
ödemeler, dolaylı yöntemle işletme faaliyetlerinden nakit akışı, yatırım ve finansman nakit akışları
hesaplanır. Her vaka üç yoldan denetlenir: doğrudan = dolaylı yöntem ve üç faaliyet toplamı = hazır
değerlerdeki değişim. TMS 7 sınıflandırmaları, nakit dışı işlemler ve yorum soruları da yer alır.

Dayanak: TMS 7 Nakit Akış Tablosu md. 6-7 (nakit benzeri), 10-17 (faaliyet sınıfları), 18-20 (doğrudan ve
dolaylı yöntem), 31-34 (faiz ve temettü), 43 (nakit dışı işlemler). Faizlerin sınıfı vaka açıklamasında
belirtilir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl
from fta_ortak import Fta, Hesap

P = Paket("questions_topic_nakit_akim_analizi_2026.json", lesson="mali_tablolar_analizi", topic="nakit_akim_analizi",
          konu_adi="Nakit Akış Analizi", seed=2026093105,
          surum="TMS 7 Nakit Akış Tablosu (KGK 2026 seti); 30.09.2026 kontrolü")
F = Fta(P, "yet-fta-nakit-")
R = "TMS 7 Nakit Akış Tablosu"


class Vaka:
    """İki yıllık vaka: 2024 → 2025. Tüm nakit akışları kalemlerden türetilir ve üç yoldan denetlenir."""

    def __init__(self, ad, *, hd0, ta, stok, pod, mdv, bam, tb, ov, gt, kv, uv, sermaye, ns, smm, fg, amort,
                 faiz, vergi, temettu):
        self.ad = ad
        d = lambda t: t[1] - t[0]  # noqa: E731
        self.k = dict(ta=ta, stok=stok, pod=pod, mdv=mdv, bam=bam, tb=tb, ov=ov, gt=gt, kv=kv, uv=uv, sermaye=sermaye)
        assert d(bam) == amort, "MDV satışı yok: birikmiş amortisman artışı dönem amortismanına eşit olmalı"
        self.ns, self.smm, self.fg, self.amort, self.faiz, self.vergi, self.temettu = ns, smm, fg, amort, faiz, vergi, temettu
        self.nk = ns - smm - fg - faiz - vergi
        self.tahsil = ns - d(ta)
        self.mal = smm + d(stok) - d(tb)
        self.fgo = fg - amort + d(pod) - d(gt)
        self.vergio = vergi - d(ov)
        self.isl = self.tahsil - self.mal - self.fgo - faiz - self.vergio
        dolayli = self.nk + amort - d(ta) - d(stok) - d(pod) + d(tb) + d(ov) + d(gt)
        assert dolayli == self.isl, (ad, dolayli, self.isl)
        self.yat = -d(mdv)
        self.fin = d(kv) + d(uv) + d(sermaye) - temettu
        self.degisim = self.isl + self.yat + self.fin
        hd1 = hd0 + self.degisim
        assert hd1 > 0, (ad, hd1)
        self.hd = (hd0, hd1)
        aktif = [hd0 + ta[0] + stok[0] + pod[0] + mdv[0] - bam[0], hd1 + ta[1] + stok[1] + pod[1] + mdv[1] - bam[1]]
        borc = [tb[i] + ov[i] + gt[i] + kv[i] + uv[i] + sermaye[i] for i in (0, 1)]
        self.gyk0 = aktif[0] - borc[0]
        assert self.gyk0 > 0, (ad, self.gyk0)
        self.gyk = (self.gyk0, self.gyk0 + self.nk - temettu)
        assert aktif[1] == borc[1] + self.gyk[1], (ad, aktif, borc, self.gyk)
        self.aktif = aktif
        self.d = {a: d(v) for a, v in self.k.items()}

    def tablo(self):
        satir = [("Hazır Değerler", self.hd), ("Ticari Alacaklar", self.k["ta"]), ("Stoklar", self.k["stok"]),
                 ("Peşin Ödenmiş Giderler", self.k["pod"]), ("Maddi Duran Varlıklar (brüt)", self.k["mdv"]),
                 ("Birikmiş Amortisman (-)", self.k["bam"]), ("AKTİF TOPLAMI", self.aktif),
                 ("Ticari Borçlar", self.k["tb"]), ("Ödenecek Vergiler", self.k["ov"]),
                 ("Gider Tahakkukları", self.k["gt"]), ("Kısa Vadeli Banka Kredileri", self.k["kv"]),
                 ("Uzun Vadeli Banka Kredileri", self.k["uv"]), ("Ödenmiş Sermaye", self.k["sermaye"]),
                 ("Geçmiş Yıllar ve Dönem Kârları", self.gyk), ("PASİF TOPLAMI", self.aktif)]
        b = "**Bilanço**\n\n| Kalem | 31.12.2024 | 31.12.2025 |\n|---|---|---|\n" + "\n".join(
            f"| {e} | {tl(v[0])} | {tl(v[1])} |" for e, v in satir)
        g = ("**2025 Gelir Tablosu**\n\n| Kalem | Tutar |\n|---|---|\n"
             f"| Net Satışlar | {tl(self.ns)} |\n| Satışların Maliyeti (-) | {tl(self.smm)} |\n"
             f"| Faaliyet Giderleri (-) | {tl(self.fg)} |\n| Finansman Giderleri (-) | {tl(self.faiz)} |\n"
             f"| Vergi Gideri (-) | {tl(self.vergi)} |\n| Dönem Net Kârı | {tl(self.nk)} |")
        ek = (f"Ek bilgiler: Faaliyet giderlerinin {tl(self.amort)} ₺’si amortismandır. Yıl içinde maddi duran "
              f"varlık satışı olmamıştır. Finansman giderlerinin tamamı yıl içinde ödenmiş olup işletme faaliyetlerinde "
              f"sınıflandırılmaktadır. Yıl içinde {tl(self.temettu)} ₺ kâr payı nakden ödenmiştir"
              + (f"; ödenmiş sermaye nakden {tl(self.d['sermaye'])} ₺ artırılmıştır." if self.d["sermaye"] else "."))
        self.ek = ek
        return b + "\n\n" + g

    def uyaran(self, sid):
        return {"id": sid, "title": f"{self.ad} — Nakit Akışı Verileri", "kind": "table", "bodyMarkdown": self.tablo(),
                "caption": f"{self.ek} {self.ad}’ye ait soruları bu tablolara göre ve TMS 7 hükümlerine göre cevaplayınız."}

    # ------------------------------------------------------------------ sorular
    def sorular(self):
        d, ad = self.d, self.ad
        return [
            ("2025 yılında müşterilerden tahsil ettiği nakit",
             Hesap(self.tahsil, "tutar", [self.ns + d["ta"], self.ns, self.ns - self.k["ta"][1], self.ns - d["ta"] + d["tb"]],
                   f"{ad} tahsilatı = net satışlar − ticari alacak artışı = {tl(self.ns)} − ({tl(d['ta'])}) = "
                   f"{tl(self.tahsil)} ₺.")),
            ("2025 yılında satıcılara mal alımları için ödediği nakit",
             Hesap(self.mal, "tutar", [self.smm - d["stok"] - d["tb"], self.smm + d["stok"] + d["tb"], self.smm,
                                       self.smm + d["stok"]],
                   f"{ad} mal ödemesi = satışların maliyeti + stok artışı − ticari borç artışı = {tl(self.smm)} + "
                   f"({tl(d['stok'])}) − ({tl(d['tb'])}) = {tl(self.mal)} ₺.")),
            ("2025 yılında faaliyet giderleri için ödediği nakit",
             Hesap(self.fgo, "tutar", [self.fg, self.fg - self.amort, self.fg - self.amort - d["pod"] + d["gt"],
                                       self.fg + d["pod"] - d["gt"]],
                   f"{ad} faaliyet gideri ödemesi = faaliyet giderleri − amortisman + peşin ödenmiş gider artışı − gider "
                   f"tahakkuku artışı = {tl(self.fg)} − {tl(self.amort)} + ({tl(d['pod'])}) − ({tl(d['gt'])}) = "
                   f"{tl(self.fgo)} ₺.")),
            ("2025 yılında ödediği vergi tutarı",
             Hesap(self.vergio, "tutar", [self.vergi, self.vergi + d["ov"], self.k["ov"][1], self.k["ov"][0] + self.vergi],
                   f"{ad} vergi ödemesi = vergi gideri − ödenecek vergi artışı = {tl(self.vergi)} − ({tl(d['ov'])}) = "
                   f"{tl(self.vergio)} ₺.")),
            ("2025 yılı işletme faaliyetlerinden nakit akışı",
             Hesap(self.isl, "tutar", [self.nk + self.amort, self.isl - 2 * self.amort, self.isl + 2 * d["ta"],
                                       self.nk - d["ta"] - d["stok"] + d["tb"], self.isl + 2 * d["stok"]],
                   f"Dolaylı yöntemle {ad}: net kâr {tl(self.nk)} + amortisman {tl(self.amort)} − alacak artışı "
                   f"({tl(d['ta'])}) − stok artışı ({tl(d['stok'])}) − peşin gider artışı ({tl(d['pod'])}) + ticari borç "
                   f"artışı ({tl(d['tb'])}) + vergi borcu artışı ({tl(d['ov'])}) + tahakkuk artışı ({tl(d['gt'])}) = "
                   f"{tl(self.isl)} ₺; doğrudan yöntem de aynı sonucu verir.")),
            ("2025 yılı yatırım faaliyetlerinden nakit akışı",
             Hesap(self.yat, "tutar", [-(d["mdv"] - self.amort), -(d["mdv"] + self.amort), -self.amort,
                                       -(self.k["mdv"][1] - self.k["bam"][1])],
                   f"{ad} için MDV satışı olmadığından brüt MDV artışı yıl içindeki alımdır: −({tl(self.k['mdv'][1])} − "
                   f"{tl(self.k['mdv'][0])}) = {tl(self.yat)} ₺. Amortisman nakit çıkışı değildir.")),
            ("2025 yılı finansman faaliyetlerinden nakit akışı",
             Hesap(self.fin, "tutar", [self.fin + self.temettu, self.fin - self.faiz, d["uv"] - self.temettu,
                                       d["kv"] + d["uv"], self.fin + self.temettu - self.faiz],
                   f"{ad} finansman nakit akışı = kısa vadeli kredi değişimi ({tl(d['kv'])}) + uzun vadeli kredi değişimi "
                   f"({tl(d['uv'])}) + sermaye artırımı ({tl(d['sermaye'])}) − ödenen kâr payı ({tl(self.temettu)}) = "
                   f"{tl(self.fin)} ₺. Faizler vakada işletme faaliyetlerinde sınıflandırılmıştır.")),
            ("2025 yılında üç faaliyetten sağladığı toplam net nakit akışı",
             Hesap(self.degisim, "tutar", [self.isl - self.yat + self.fin, self.isl + self.yat, self.isl + self.fin,
                                           self.isl + self.yat - self.fin],
                   f"{ad}: işletme ({tl(self.isl)}) + yatırım ({tl(self.yat)}) + finansman ({tl(self.fin)}) = "
                   f"{tl(self.degisim)} ₺; bu tutar hazır değerlerdeki değişime ({tl(self.hd[0])} → {tl(self.hd[1])}) "
                   "eşittir.")),
        ]


VAKALAR = [
    Vaka("NKA A.Ş.", hd0=60_000, ta=(300_000, 360_000), stok=(250_000, 290_000), pod=(10_000, 16_000),
         mdv=(900_000, 1_050_000), bam=(300_000, 360_000), tb=(200_000, 230_000), ov=(20_000, 25_000),
         gt=(8_000, 12_000), kv=(100_000, 80_000), uv=(250_000, 320_000), sermaye=(500_000, 500_000),
         ns=2_000_000, smm=1_400_000, fg=380_000, amort=60_000, faiz=40_000, vergi=45_000, temettu=40_000),
    Vaka("NKB A.Ş.", hd0=40_000, ta=(500_000, 470_000), stok=(320_000, 380_000), pod=(20_000, 14_000),
         mdv=(1_200_000, 1_380_000), bam=(400_000, 490_000), tb=(260_000, 300_000), ov=(30_000, 24_000),
         gt=(15_000, 18_000), kv=(150_000, 190_000), uv=(300_000, 260_000), sermaye=(600_000, 700_000),
         ns=3_100_000, smm=2_200_000, fg=560_000, amort=90_000, faiz=50_000, vergi=70_000, temettu=60_000),
    Vaka("NKC A.Ş.", hd0=90_000, ta=(220_000, 290_000), stok=(180_000, 150_000), pod=(5_000, 9_000),
         mdv=(700_000, 760_000), bam=(250_000, 295_000), tb=(140_000, 120_000), ov=(12_000, 18_000),
         gt=(6_000, 5_000), kv=(80_000, 110_000), uv=(150_000, 120_000), sermaye=(400_000, 400_000),
         ns=1_500_000, smm=1_050_000, fg=290_000, amort=45_000, faiz=25_000, vergi=34_000, temettu=40_000),
    Vaka("NKD A.Ş.", hd0=25_000, ta=(410_000, 440_000), stok=(360_000, 420_000), pod=(12_000, 10_000),
         mdv=(1_500_000, 1_620_000), bam=(600_000, 700_000), tb=(330_000, 390_000), ov=(25_000, 30_000),
         gt=(10_000, 14_000), kv=(200_000, 170_000), uv=(400_000, 470_000), sermaye=(700_000, 700_000),
         ns=3_800_000, smm=2_850_000, fg=600_000, amort=100_000, faiz=70_000, vergi=70_000, temettu=80_000),
]
KALIP = ["{ad} verilerine göre şirketin {ifade} kaç ₺’dir?",
         "Tablolara göre {ad}’nin {ifade} kaç ₺ olarak hesaplanır?",
         "{ad}’nin {ifade} kaç ₺ olur?",
         "Verilen tablolar esas alındığında {ad}’nin {ifade} kaç ₺’dir?",
         "{ad} için {ifade} kaç ₺ olarak bulunur?"]
k = 0
for vaka in VAKALAR:
    sid = F.uyaran(vaka.uyaran(f"yet-fta-nakit-{vaka.ad[:3].lower()}"))
    for ifade, h in vaka.sorular():
        k += 1
        F.hesap(R, KALIP[k % 5].format(ad=vaka.ad, ifade=ifade), h, stimulus_id=sid)
    # vaka içi denetim: üç faaliyet toplamı hazır değer değişimine eşittir
    assert vaka.isl + vaka.yat + vaka.fin == vaka.hd[1] - vaka.hd[0]

# ------------------------------------------------------------------ bağımsız hesaplar
F.hesap(R,
    "Bir işletmenin 2025 yılında net satışları 1.200.000 ₺’dir. Yıl içinde ticari alacaklar 80.000 ₺ artmış, "
    "müşterilerden alınan sipariş avansları 20.000 ₺ artmıştır.\n\nİşletmenin 2025 yılında müşterilerden tahsil ettiği "
    "nakit kaç ₺’dir?",
    Hesap(1_200_000 - 80_000 + 20_000, "tutar", [1_200_000 - 80_000 - 20_000, 1_200_000 + 80_000 + 20_000, 1_200_000 - 80_000,
                                                  1_200_000 + 80_000 - 20_000],
          "Tahsilat = net satışlar − alacak artışı + alınan avans artışı = 1.200.000 − 80.000 + 20.000 = 1.140.000 ₺. "
          "Avans artışı henüz satışa dönüşmemiş nakit girişidir."))

F.hesap(R,
    "Bir işletmenin 2025 yılında satışların maliyeti 700.000 ₺’dir. Yıl içinde stoklar 20.000 ₺ azalmış, ticari "
    "borçlar 20.000 ₺ artmış, satıcılara verilen sipariş avansları 10.000 ₺ artmıştır.\n\nİşletmenin mal alımları için "
    "ödediği nakit kaç ₺’dir?",
    Hesap(700_000 - 20_000 - 20_000 + 10_000, "tutar", [700_000 + 20_000 - 20_000 + 10_000, 700_000 - 20_000 + 20_000,
                                                          700_000 - 40_000, 700_000 + 50_000],
          "Mal ödemesi = SMM − stok azalışı − ticari borç artışı + verilen avans artışı = 700.000 − 20.000 − 20.000 + "
          "10.000 = 670.000 ₺."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin 2025 yılı net kârı 250.000 ₺’dir. Dönem amortismanı 40.000 ₺, maddi duran varlık satış kârı 15.000 "
    "₺’dir. Yıl içinde ticari alacaklar 30.000 ₺ artmış, stoklar 20.000 ₺ azalmış, ticari borçlar 10.000 ₺ "
    "azalmıştır.\n\nDolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç ₺’dir?",
    Hesap(250_000 + 40_000 - 15_000 - 30_000 + 20_000 - 10_000, "tutar",
          [250_000 + 40_000 + 15_000 - 30_000 + 20_000 - 10_000, 250_000 + 40_000 - 15_000 + 30_000 - 20_000 + 10_000,
           250_000 + 40_000, 250_000 - 15_000 - 30_000 + 20_000 - 10_000],
          "250.000 + 40.000 (amortisman) − 15.000 (satış kârı, nakit girişi yatırım faaliyetindedir) − 30.000 + 20.000 − "
          "10.000 = 255.000 ₺."), zorluk="hard")

F.hesap(R,
    "Bir işletme maliyeti 200.000 ₺, birikmiş amortismanı 150.000 ₺ olan bir makineyi 20.000 ₺ kârla peşin olarak "
    "satmıştır.\n\nBu satışın nakit akış tablosunda yatırım faaliyetlerinden nakit girişi olarak gösterilecek tutarı "
    "kaç ₺’dir?",
    Hesap(200_000 - 150_000 + 20_000, "tutar", [20_000, 50_000, 200_000 + 20_000, 150_000 + 20_000],
          "Defter değeri = 200.000 − 150.000 = 50.000 ₺; satış bedeli = 50.000 + 20.000 = 70.000 ₺ yatırım "
          "faaliyetlerinden nakit girişidir. Kâr (20.000 ₺) dolaylı yöntemde net kârdan düşülür."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin geçmiş yıllar kârları hesabı yıl başında 400.000 ₺, yıl sonunda 450.000 ₺’dir. Yıl içindeki "
    "dönem net kârı 180.000 ₺ olup kâr dağıtımı dışında öz kaynak hareketi yoktur ve dağıtılan kâr payının tamamı "
    "nakden ödenmiştir.\n\nYıl içinde ödenen kâr payı kaç ₺’dir?",
    Hesap(400_000 + 180_000 - 450_000, "tutar", [180_000 - 50_000 + 50_000, 50_000, 180_000 + 50_000, 450_000 - 180_000],
          "Yıl sonu kârlar = yıl başı + net kâr − dağıtılan kâr payı; 450.000 = 400.000 + 180.000 − X, X = 130.000 ₺ "
          "finansman faaliyetlerinden nakit çıkışıdır."))

F.hesap(R,
    "Bir işletmenin maddi duran varlıklarının brüt tutarı yıl başında 1.000.000 ₺, yıl sonunda 1.300.000 ₺’dir. Yıl "
    "içinde maliyeti 120.000 ₺ olan bir varlık satılmıştır; diğer tüm alımlar peşindir.\n\nYıl içinde maddi duran "
    "varlık alımları için ödenen nakit kaç ₺’dir?",
    Hesap(1_300_000 - 1_000_000 + 120_000, "tutar", [300_000, 300_000 - 120_000, 1_300_000 - 120_000, 120_000],
          "Yıl sonu brüt MDV = yıl başı + alımlar − satılanın maliyeti; 1.300.000 = 1.000.000 + A − 120.000, A = 420.000 "
          "₺. Brüt tutardaki net artış (300.000 ₺) satılan varlığı hesaba katmaz."), zorluk="hard")

F.hesap(R,
    "Bir işletmenin 2025 yılı finansman giderleri (faiz) 60.000 ₺’dir. Ödenecek faizler yıl başında 8.000 ₺, yıl "
    "sonunda 14.000 ₺’dir.\n\nİşletmenin yıl içinde ödediği faiz kaç ₺’dir?",
    Hesap(60_000 - 6_000, "tutar", [60_000 + 6_000, 60_000, 14_000, 60_000 - 14_000],
          "Ödenen faiz = faiz gideri − ödenecek faiz artışı = 60.000 − (14.000 − 8.000) = 54.000 ₺."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin 2025 yılı vergi gideri 90.000 ₺’dir. Ödenecek vergiler yıl başında 30.000 ₺ iken yıl sonunda "
    "20.000 ₺’ye inmiştir.\n\nİşletmenin yıl içinde ödediği vergi kaç ₺’dir?",
    Hesap(90_000 + 10_000, "tutar", [90_000 - 10_000, 90_000, 90_000 + 30_000, 90_000 - 20_000],
          "Ödenen vergi = vergi gideri + ödenecek vergi azalışı = 90.000 + 10.000 = 100.000 ₺; önceki yılın borcu da bu "
          "yıl ödenmiştir."))

F.hesap(R,
    "Bir işletmenin 2025 yılı kira geliri 48.000 ₺’dir. Peşin tahsil edilen kiraları izleyen gelecek aylara ait gelirler "
    "hesabı yıl başında 12.000 ₺, yıl sonunda 20.000 ₺’dir.\n\nİşletmenin yıl içinde tahsil ettiği kira nakdi kaç "
    "₺’dir?",
    Hesap(48_000 + 8_000, "tutar", [48_000 - 8_000, 48_000, 48_000 + 20_000, 20_000 + 12_000],
          "Tahsilat = kira geliri + peşin tahsil edilmiş gelir artışı = 48.000 + 8.000 = 56.000 ₺."))

F.hesap(R,
    "Bir işletmenin 2025 yılı personel ücret giderleri 600.000 ₺’dir. Ödenecek ücretler yıl başında 40.000 ₺, yıl "
    "sonunda 55.000 ₺’dir.\n\nİşletmenin yıl içinde personele ödediği ücret nakdi kaç ₺’dir?",
    Hesap(600_000 - 15_000, "tutar", [600_000 + 15_000, 600_000, 600_000 - 55_000, 600_000 + 40_000],
          "Ödenen ücret = ücret gideri − ödenecek ücret artışı = 600.000 − 15.000 = 585.000 ₺."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin 2025 yılı nakit akış tablosunda işletme faaliyetlerinden 320.000 ₺ nakit girişi, yatırım "
    "faaliyetlerinden 410.000 ₺ nakit çıkışı ve finansman faaliyetlerinden 150.000 ₺ nakit girişi vardır. Yıl başı "
    "nakit ve nakit benzerleri 80.000 ₺’dir.\n\nYıl sonu nakit ve nakit benzerleri kaç ₺’dir?",
    Hesap(80_000 + 320_000 - 410_000 + 150_000, "tutar", [320_000 - 410_000 + 150_000, 80_000 + 320_000 + 410_000 + 150_000,
                                                            80_000 + 320_000 - 410_000 - 150_000 + 300_000, 80_000 + 320_000 - 410_000],
          "Nakitteki değişim = 320.000 − 410.000 + 150.000 = 60.000 ₺; yıl sonu nakit = 80.000 + 60.000 = 140.000 ₺."),
    zorluk="easy")

F.hesap(R,
    "Bir işletmenin 2025 yılı net kârı 300.000 ₺, işletme faaliyetlerinden nakit akışı 360.000 ₺’dir. Analist, kârın "
    "nakde dönüşme derecesini göstermek için işletme faaliyetlerinden nakit akışını net kâra bölmektedir.\n\nBu oran "
    "(nakit akışı/net kâr) kaçtır?",
    Hesap(360_000 / 300_000, "kat", [300_000 / 360_000, 60_000 / 300_000, 660_000 / 300_000, 360_000 / 660_000],
          "Oran = 360.000 ÷ 300.000 = 1,20. Oranın 1’in üzerinde olması kârın nakitle desteklendiğini gösterir."),
    zorluk="easy")

F.hesap(R,
    "Bir işletmenin 2025 yılı net kârı 120.000 ₺’dir. Dönem amortismanı 30.000 ₺, yıl içinde ayrılan ve ödenmeyen "
    "kıdem tazminatı karşılık gideri 10.000 ₺’dir. Ticari alacaklar 25.000 ₺ artmış, ticari borçlar 5.000 ₺ "
    "artmıştır.\n\nDolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç ₺’dir?",
    Hesap(120_000 + 30_000 + 10_000 - 25_000 + 5_000, "tutar",
          [120_000 + 30_000 - 25_000 + 5_000, 120_000 + 30_000 + 10_000 + 25_000 - 5_000, 120_000 + 40_000,
           120_000 - 10_000 + 30_000 - 25_000 + 5_000],
          "Nakit çıkışı gerektirmeyen giderler (amortisman 30.000 ve karşılık 10.000 ₺) net kâra eklenir: 120.000 + "
          "40.000 − 25.000 + 5.000 = 140.000 ₺."))

F.hesap(R,
    "Bir işletmenin doğrudan yöntemle hazırlanan 2025 yılı verileri şöyledir: müşterilerden tahsilat 1.900.000 ₺, "
    "satıcılara ödeme 1.300.000 ₺, personel ödemeleri 250.000 ₺, diğer faaliyet ödemeleri 120.000 ₺, faiz ödemesi "
    "(işletme faaliyetlerinde sınıflanan) 30.000 ₺ ve vergi ödemesi 60.000 ₺.\n\nİşletme faaliyetlerinden nakit akışı "
    "kaç ₺’dir?",
    Hesap(1_900_000 - 1_300_000 - 250_000 - 120_000 - 30_000 - 60_000, "tutar",
          [1_900_000 - 1_300_000 - 250_000 - 120_000, 1_900_000 - 1_300_000, 1_900_000 - 1_300_000 - 250_000 - 120_000 - 60_000,
           1_900_000 - 1_300_000 - 250_000],
          "İşletme faaliyetlerinden nakit akışı = 1.900.000 − 1.300.000 − 250.000 − 120.000 − 30.000 − 60.000 = 140.000 ₺."),
    zorluk="easy")

F.hesap(R,
    "Bir işletme 2025 yılında 450.000 ₺’ye makine satın almış, eski bir aracı 80.000 ₺’ye satmış, başka bir şirketin "
    "hisselerini 120.000 ₺’ye edinmiş ve yatırım faaliyetlerinde sınıfladığı 15.000 ₺ kâr payı tahsil etmiştir. Tüm "
    "işlemler peşindir.\n\nYatırım faaliyetlerinden net nakit akışı kaç ₺’dir?",
    Hesap(-450_000 + 80_000 - 120_000 + 15_000, "tutar", [-450_000 - 120_000, -450_000 + 80_000 - 120_000,
                                                            -450_000 - 80_000 - 120_000 + 15_000, -450_000 + 80_000 + 15_000],
          "Yatırım nakit akışı = −450.000 + 80.000 − 120.000 + 15.000 = −475.000 ₺ (net çıkış)."))

# ------------------------------------------------------------------ TMS 7 sınıflandırma ve yorum
F.q("TMS 7 md. 6-7",
    "Bir işletmenin dönem sonunda kasasında nakit, bankada vadesiz mevduat, 2 ay vadeli bir mevduat ve 9 ay vadeli bir "
    "mevduat bulunmaktadır. Muhasebe müdürü nakit akış tablosunda nakit ve nakit benzerlerini belirlemektedir.\n\n"
    "TMS 7 Nakit Akış Tablosu’na göre aşağıdakilerden hangisi nakit benzeri sayılmaz?",
    "9 ay vadeli banka mevduatı",
    ["2 ay vadeli banka mevduatı", "Bankadaki vadesiz mevduat", "Kasadaki nakit", "Kısa vadeli, değer riski önemsiz fon"],
    "TMS 7’ye göre nakit benzerleri; kolayca nakde çevrilebilen, değer riski önemsiz ve genellikle edinme tarihinden "
    "itibaren üç ay veya daha kısa vadeli yatırımlardır. 9 ay vadeli mevduat bu tanıma girmez.")

F.q("TMS 7 md. 16",
    "Bir işletme yıl içinde yeni bir üretim hattı için 800.000 ₺ tutarında makine satın almış ve bedelini peşin "
    "ödemiştir.\n\nTMS 7’ye göre bu ödeme nakit akış tablosunda hangi bölümde gösterilir?",
    "Yatırım faaliyetleri",
    ["İşletme faaliyetleri", "Finansman faaliyetleri", "Nakit dışı işlemler", "Diğer kapsamlı gelir"],
    "Maddi duran varlık edinimi için yapılan nakit ödemeler TMS 7 md. 16’ya göre yatırım faaliyetlerinden nakit "
    "çıkışıdır.", zorluk="easy")

F.q(R,
    "Bir işletme yıl içinde kısa vadeli banka kredisinin 150.000 ₺’lik anaparasını geri ödemiş, ayrıca nakit karşılığı "
    "sermaye artırımı yaparak 300.000 ₺ tahsil etmiştir.\n\nBu iki işlem nakit akış tablosunda hangi bölümde "
    "gösterilir?",
    "İkisi de finansman faaliyetlerinde",
    ["İkisi de işletme faaliyetlerinde", "Kredi ödemesi işletme, sermaye artırımı finansman faaliyetlerinde",
     "Kredi ödemesi finansman, sermaye artırımı yatırım faaliyetlerinde", "İkisi de yatırım faaliyetlerinde"],
    "Borçlanmalar ve geri ödemeleri ile öz kaynak sahiplerinden sağlanan nakit, işletmenin sermaye ve borç yapısını "
    "değiştirdiğinden finansman faaliyetlerinde gösterilir.")

F.q("TMS 7 md. 16",
    "Bir işletmenin muhasebe birimi, yıl içindeki nakit hareketlerini faaliyet türlerine göre sınıflandırmaktadır. "
    "Listelenen işlemlerden biri diğerlerinden farklı bir bölüme aittir.\n\nTMS 7’ye göre aşağıdakilerden hangisi "
    "yatırım faaliyetlerinden nakit akışı değildir?",
    "Satılmak üzere alınan ticari mal için yapılan ödeme",
    ["Başka bir şirketin hisse senetlerinin edinimi için ödeme", "Kullanılmış bir binanın satışından tahsilat",
     "Üçüncü kişiye verilen uzun vadeli borç", "Yazılım lisansı (maddi olmayan varlık) edinimi için ödeme"],
    "Ticari mal alımları işletmenin esas gelir yaratan faaliyetine ilişkin olduğundan işletme faaliyetlerindendir. "
    "Duran varlık edinim ve satışları, başka işletmelerin payları ve verilen borçlar yatırım faaliyetleridir.")

F.q(R,
    "Bir işletme nakit akış tablosunu dolaylı yöntemle hazırlamaktadır. Yeni bir muhasebe uzmanı, amortismanın neden "
    "net kâra eklendiğini sormaktadır.\n\nDolaylı yöntemde amortismanın net kâra eklenmesinin nedeni aşağıdakilerden "
    "hangisidir?",
    "Amortisman kârı azaltan ancak nakit çıkışı gerektirmeyen bir giderdir.",
    ["Amortisman bir nakit girişi kaynağıdır ve işletmeye fon sağlar.",
     "Amortisman yatırım faaliyetlerinden nakit girişi olarak sınıflanır.",
     "Amortisman ödendiği dönemde gider yazıldığından geri alınır.",
     "Amortisman finansman giderleri içinde yer aldığından düzeltilir."],
    "Dolaylı yöntem net kârdan başlar; amortisman kârı azaltmış ama dönemde nakit çıkışı doğurmamıştır. Bu nedenle "
    "nakit etkisini bulmak için net kâra geri eklenir; kendisi nakit kaynağı değildir.")

F.q(R,
    "Bir analist dolaylı yöntemle işletme faaliyetlerinden nakit akışını hesaplarken net kârı düzelten kalemleri "
    "sıralamaktadır.\n\nAşağıdakilerden hangisi net kâra eklenmez?",
    "Ticari alacaklardaki artış",
    ["Dönem amortisman gideri", "Ticari borçlardaki artış", "Stoklardaki azalış", "Ödenecek vergilerdeki artış"],
    "Alacak artışı, satışların bir kısmının henüz tahsil edilmediğini gösterir; bu tutar net kârdan düşülür. Diğer "
    "kalemler nakit çıkışı olmadan kârı azaltan ya da nakit çıkışını erteleyen kalemlerdir ve eklenir.")

F.q("TMS 7 md. 43-44",
    "Bir işletme yıl içinde 2.000.000 ₺ değerindeki bir binayı, satıcıya beş yıl vadeli senet vererek satın almıştır; "
    "yıl içinde hiçbir ödeme yapılmamıştır.\n\nTMS 7’ye göre bu işlem nakit akış tablosunda nasıl gösterilir?",
    "Tabloda yer almaz, nakit dışı işlem olarak dipnotta açıklanır.",
    ["Yatırım faaliyetlerinden 2.000.000 ₺ çıkış olarak gösterilir.",
     "Finansman faaliyetlerinden 2.000.000 ₺ giriş olarak gösterilir.",
     "Yatırım çıkışı ve finansman girişi olarak ayrı ayrı gösterilir.",
     "İşletme faaliyetlerinden 2.000.000 ₺ çıkış olarak gösterilir."],
    "Nakit veya nakit benzeri kullanılmayan yatırım ve finansman işlemleri nakit akış tablosuna alınmaz; finansal "
    "tabloların başka bir yerinde (dipnotlarda) açıklanır.", zorluk="hard")

F.q(R,
    "Bir işletme üç yıldır net kâr açıklamasına karşın işletme faaliyetlerinden nakit akışı negatiftir. Aynı dönemde "
    "ticari alacaklar ve stoklar satışlardan çok daha hızlı artmıştır.\n\nBu duruma ilişkin aşağıdaki yorumlardan "
    "hangisi doğrudur?",
    "Kâr nakde dönüşmemekte, işletme sermayesine fon bağlanmaktadır.",
    ["Kâr kalitesi yüksektir, nakit yaratma gücü güçlüdür.",
     "Negatif nakit akışı yatırım harcamalarının sonucudur.",
     "Alacak ve stok artışları işletme faaliyetlerinden nakit akışını artırır.",
     "Net kâr pozitif olduğundan finansman ihtiyacı doğmaz."],
    "Alacak ve stok artışları dolaylı yöntemde net kârdan düşülür. Kâr bu varlıklara bağlanıp nakde dönüşmediğinden "
    "işletme faaliyetleri nakit akışı negatiftir; ek finansman gerekir.")

F.q(R,
    "Bir işletmenin son beş yılda yatırım faaliyetlerinden nakit akışı her yıl büyük tutarda negatif, finansman "
    "faaliyetlerinden nakit akışı ise pozitiftir. İşletme faaliyetlerinden nakit akışı düşük düzeyde pozitiftir.\n\nBu "
    "tabloya ilişkin aşağıdaki yorumlardan hangisi doğrudur?",
    "Büyüme yatırımları büyük ölçüde borç ya da sermaye girişiyle finanse edilmektedir.",
    ["Yatırımlar tamamen işletme faaliyetlerinin ürettiği nakitle finanse edilmektedir.",
     "İşletme yatırımlarını azaltmakta ve borçlarını geri ödemektedir.",
     "Finansman nakit girişleri kâr payı ödemelerinden kaynaklanmaktadır.",
     "Negatif yatırım nakit akışı işletmenin zarar ettiğini gösterir."],
    "Yatırım çıkışları işletme faaliyetlerinin ürettiği nakdin çok üzerindedir; aradaki fark finansman girişleriyle "
    "(kredi veya sermaye) kapatılmaktadır. Negatif yatırım nakit akışı zarar göstergesi değildir.")

F.q(R,
    "Bir işletmenin fon (net işletme sermayesi) akım tablosunu hazırlayan analist, net işletme sermayesini artıran "
    "kaynakları belirlemektedir.\n\nAşağıdakilerden hangisi net işletme sermayesi açısından bir fon kaynağıdır?",
    "Uzun vadeli banka kredisi kullanılması",
    ["Kısa vadeli banka kredisiyle stok alınması", "Maddi duran varlık satın alınması",
     "Uzun vadeli kredinin anapara ödemesi", "Kâr payının nakden ödenmesi"],
    "Uzun vadeli kaynak girişi dönen varlıkları (nakit) artırırken kısa vadeli borçları değiştirmediğinden net "
    "işletme sermayesini artırır. KVYK ile stok alımı iki kalemi birlikte artırdığından fonu değiştirmez.")

F.q(R,
    "Bir işletme gün içinde kasasındaki 50.000 ₺’yi vadesiz banka hesabına yatırmış, aynı gün 3 ay vadeli bir mevduat "
    "açmak için bu hesaptan 30.000 ₺ çekmiştir.\n\nBu işlemlerin nakit akış tablosundaki etkisi aşağıdakilerden "
    "hangisidir?",
    "Nakit ve nakit benzerleri arasında aktarım olduğundan tabloda gösterilmez.",
    ["İşletme faaliyetlerinden 50.000 ₺ çıkış olarak gösterilir.",
     "Yatırım faaliyetlerinden 30.000 ₺ çıkış olarak gösterilir.",
     "Finansman faaliyetlerinden 80.000 ₺ çıkış olarak gösterilir.",
     "Yatırım faaliyetlerinden 20.000 ₺ giriş olarak gösterilir."],
    "Kasa, vadesiz mevduat ve üç ay vadeli mevduat nakit ve nakit benzerleri içinde yer alır. Bu kalemler arasındaki "
    "hareketler nakit akışı sayılmaz; işletme, yatırım ya da finansman faaliyetinin parçası değildir.")

F.q(R,
    "Bir işletmenin muhasebe müdürü nakit akış tablosunun doğrudan ve dolaylı yöntemle hazırlanması arasındaki farkı "
    "yönetim kuruluna açıklamaktadır.\n\nİki yöntem arasındaki fark aşağıdakilerden hangisidir?",
    "Fark, işletme faaliyetleri bölümünün sunuluş biçimindedir.",
    ["Yatırım faaliyetleri bölümü dolaylı yöntemde gösterilmez.",
     "Dolaylı yöntemde finansman faaliyetleri net kârdan türetilir.",
     "İki yöntem farklı nakit değişimi toplamı verir.",
     "Doğrudan yöntem nakit dışı işlemleri de tabloya alır."],
    "İki yöntem de aynı nakit değişimini verir; fark işletme faaliyetleri bölümündedir: doğrudan yöntem ana tahsilat "
    "ve ödeme kalemlerini, dolaylı yöntem net kârın düzeltilmesini gösterir.")

F.q(R,
    "Bir finansal analiz eğitiminde nakit akış tablosuna ilişkin ifadeler tartışılmış ve katılımcılardan hatalı olanı "
    "bulmaları istenmiştir.\n\nNakit akış tablosuyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Tahakkuk esasına göre hazırlanır ve dönemin kârını gösterir.",
    ["Nakit girişleri ve çıkışları üç faaliyet türüne göre sınıflandırılır.",
     "Nakit ve nakit benzerlerindeki değişimi açıklar.",
     "İşletmenin nakit yaratma gücünü değerlendirmeye yardım eder.",
     "Dolaylı yöntemde işletme faaliyetleri net kârdan başlanarak bulunur."],
    "Nakit akış tablosu tahakkuk esasına göre değil nakit esasına göre hazırlanır; dönem kârını gelir tablosu "
    "gösterir. Nakit akış tablosu nakit ve nakit benzerlerindeki değişimi faaliyet türlerine göre açıklar.")

if __name__ == "__main__":
    sys.exit(F.yaz())
