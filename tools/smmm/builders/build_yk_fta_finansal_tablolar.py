# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi · Finansal Tablolar — 60 soru, 2026 test biçimi.

Hesap bakiyelerinden (MSUGT kodlarıyla) bilanço ve gelir tablosu gruplarının kurulması (düzenleyici
hesaplar, 159 ve 371 gibi sınıflandırma tuzakları, 12 ay kuralı), öz kaynak değişim tablosu ve toplam
kapsamlı gelir hesapları; TMS 1 Finansal Tabloların Sunuluşu ve Kavramsal Çerçeve'nin temel hükümleri
sorulur. Tutarlar builder içinde hesaplanır; bilanço denkliği denetlenir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl
from fta_ortak import Fta, Hesap

P = Paket("questions_topic_finansal_tablolar_2026.json", lesson="mali_tablolar_analizi", topic="finansal_tablolar",
          konu_adi="Finansal Tablolar", seed=2026093106,
          surum="TMS 1 Finansal Tabloların Sunuluşu; Finansal Raporlamaya İlişkin Kavramsal Çerçeve; MSUGT; "
                "30.09.2026 kontrolü")
F = Fta(P, "yet-fta-tablo-")
R = "TMS 1 ve MSUGT finansal tablo sunumu"

# ------------------------------------------------------------------ MZA: bilanço hesap bakiyeleri
MZA = [(100, "Kasa", 25_000), (102, "Bankalar", 140_000), (103, "Verilen Çekler ve Ödeme Emirleri (-)", 15_000),
       (110, "Hisse Senetleri", 30_000), (120, "Alıcılar", 260_000), (121, "Alacak Senetleri", 60_000),
       (128, "Şüpheli Ticari Alacaklar", 20_000), (129, "Şüpheli Ticari Alacaklar Karşılığı (-)", 20_000),
       (153, "Ticari Mallar", 310_000), (159, "Verilen Sipariş Avansları", 25_000),
       (180, "Gelecek Aylara Ait Giderler", 12_000), (190, "Devreden KDV", 18_000),
       (220, "Alıcılar (uzun vadeli)", 40_000), (252, "Binalar", 600_000), (253, "Tesis, Makine ve Cihazlar", 350_000),
       (254, "Taşıtlar", 180_000), (257, "Birikmiş Amortismanlar (-)", 330_000), (260, "Haklar", 50_000),
       (268, "Birikmiş Amortismanlar (-) (MODV)", 10_000), (280, "Gelecek Yıllara Ait Giderler", 16_000),
       (300, "Banka Kredileri", 180_000), (320, "Satıcılar", 210_000), (321, "Borç Senetleri", 40_000),
       (335, "Personele Borçlar", 22_000), (340, "Alınan Sipariş Avansları", 30_000),
       (360, "Ödenecek Vergi ve Fonlar", 26_000), (361, "Ödenecek Sosyal Güvenlik Kesintileri", 14_000),
       (370, "Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları", 45_000),
       (371, "Dönem Kârının Peşin Ödenen Vergi ve Diğer Yükümlülükleri (-)", 30_000),
       (381, "Gider Tahakkukları", 8_000), (400, "Banka Kredileri (uzun vadeli)", 300_000),
       (472, "Kıdem Tazminatı Karşılığı", 40_000), (500, "Sermaye", 650_000), (540, "Yasal Yedekler", 40_000),
       (590, "Dönem Net Kârı", 135_000)]
b = {k: v for k, _, v in MZA}
hd = b[100] + b[102] - b[103]
ta = b[120] + b[121] + b[128] - b[129]
stok = b[153] + b[159]
dv = hd + b[110] + ta + stok + b[180] + b[190]
mdv = b[252] + b[253] + b[254] - b[257]
duran = b[220] + mdv + b[260] - b[268] + b[280]
aktif = dv + duran
kvyk = b[300] + b[320] + b[321] + b[335] + b[340] + b[360] + b[361] + b[370] - b[371] + b[381]
uvyk = b[400] + b[472]
ok = aktif - kvyk - uvyk
gyk = ok - b[500] - b[540] - b[590]
assert gyk > 0 and (hd, ta, stok, dv, mdv, duran, aktif, kvyk, uvyk) == (
    150_000, 320_000, 335_000, 865_000, 800_000, 896_000, 1_761_000, 545_000, 340_000)
tablo = ("| Hesap | Tutar (₺) |\n|---|---|\n" + "\n".join(f"| {k} {ad} | {tl(v)} |" for k, ad, v in MZA)
         + f"\n| 570 Geçmiş Yıllar Kârları | ? |")
S_A = F.uyaran({"id": "yet-fta-tablo-mza", "title": "MZA A.Ş. — 31.12.2025 Hesap Bakiyeleri", "kind": "table",
                "bodyMarkdown": tablo,
                "caption": "MZA A.Ş.’nin bilanço hesaplarının 31.12.2025 kalanları verilmiştir. Soruları MSUGT bilanço "
                           "düzenine göre cevaplayınız; 570 hesabının kalanı bilanço denkliğinden bulunur."})
A = [
    ("bilançosunda hazır değerler grubunun toplamı", Hesap(hd, "tutar", [b[100] + b[102] + b[103], b[100] + b[102],
                                                                        hd + b[110], b[102] - b[103]],
     "MZA A.Ş. hazır değerleri = 100 Kasa + 102 Bankalar − 103 Verilen Çekler = 25.000 + 140.000 − 15.000 = 150.000 ₺. "
     "103 düzenleyici hesaptır, gruptan düşülür.")),
    ("bilançosunda kısa vadeli ticari alacaklar grubunun net tutarı",
     Hesap(ta, "tutar", [ta + b[129], ta + b[220], b[120] + b[121], ta + b[159]],
           "MZA A.Ş. ticari alacakları = 120 + 121 + 128 − 129 = 260.000 + 60.000 + 20.000 − 20.000 = 320.000 ₺. 220 uzun "
           "vadeli olduğundan duran varlıklarda, 159 ise stoklar grubunda yer alır.")),
    ("bilançosunda stoklar grubunun toplamı", Hesap(stok, "tutar", [b[153], stok + b[180], b[153] - b[159], stok + b[190]],
     "MZA A.Ş. stokları = 153 Ticari Mallar + 159 Verilen Sipariş Avansları = 310.000 + 25.000 = 335.000 ₺. MSUGT’de "
     "stok alımı için verilen avanslar stoklar grubunda gösterilir.")),
    ("dönen varlıklar toplamı", Hesap(dv, "tutar", [dv + b[220] + b[280], dv - b[159], dv + b[129] + b[103], dv - b[190]],
     "MZA A.Ş. dönen varlıkları = hazır değerler 150.000 + menkul kıymetler 30.000 + ticari alacaklar 320.000 + stoklar "
     "335.000 + gelecek aylara ait giderler 12.000 + devreden KDV 18.000 = 865.000 ₺.")),
    ("maddi duran varlıklarının net tutarı", Hesap(mdv, "tutar", [mdv + b[257], mdv + b[260] - b[268], mdv - b[254],
                                                                 mdv + b[280]],
     "MZA A.Ş. MDV = 252 + 253 + 254 − 257 = 600.000 + 350.000 + 180.000 − 330.000 = 800.000 ₺.")),
    ("duran varlıklar toplamı", Hesap(duran, "tutar", [duran - b[220], duran + b[268], duran - b[280], duran + b[257]],
     "MZA A.Ş. duran varlıkları = uzun vadeli alacaklar 40.000 + MDV 800.000 + MODV (50.000 − 10.000) 40.000 + gelecek "
     "yıllara ait giderler 16.000 = 896.000 ₺.")),
    ("kısa vadeli yabancı kaynaklar toplamı", Hesap(kvyk, "tutar", [kvyk + 2 * b[371], kvyk - b[340], kvyk + b[472],
                                                                    kvyk - b[370] + b[371]],
     "MZA A.Ş. KVYK = 180.000 + (210.000 + 40.000) + 22.000 + 30.000 + (26.000 + 14.000) + (45.000 − 30.000) + 8.000 = "
     "545.000 ₺. 371 hesabı 370’ten indirilerek gösterilir.")),
    ("uzun vadeli yabancı kaynaklar toplamı", Hesap(uvyk, "tutar", [b[400], uvyk + b[300], uvyk - b[472] + b[381],
                                                                    uvyk + b[340]],
     "MZA A.Ş. UVYK = 400 Banka Kredileri 300.000 + 472 Kıdem Tazminatı Karşılığı 40.000 = 340.000 ₺.")),
    ("öz kaynaklar toplamı", Hesap(ok, "tutar", [b[500] + b[540] + b[590], aktif - kvyk, ok + b[371], aktif - uvyk - kvyk - b[590]],
     f"MZA A.Ş. aktif toplamı {tl(aktif)} ₺; öz kaynaklar = aktif − KVYK − UVYK = {tl(aktif)} − 545.000 − 340.000 = "
     f"{tl(ok)} ₺.")),
    ("570 Geçmiş Yıllar Kârları hesabının kalanı", Hesap(gyk, "tutar", [gyk + b[590], gyk + b[540], gyk + 2 * b[371], gyk + b[129]],
     f"MZA A.Ş. öz kaynakları {tl(ok)} ₺; 570 = {tl(ok)} − sermaye 650.000 − yasal yedekler 40.000 − dönem net kârı "
     f"135.000 = {tl(gyk)} ₺.")),
    ("net işletme sermayesi", Hesap(dv - kvyk, "tutar", [dv - kvyk - uvyk, dv, dv - kvyk - 2 * b[371], dv + b[220] - kvyk],
     "MZA A.Ş. net işletme sermayesi = dönen varlıklar − KVYK = 865.000 − 545.000 = 320.000 ₺.")),
]
KALIP = ["{ad}’nin {ifade} kaç ₺’dir?", "Hesap bakiyelerine göre {ad}’nin {ifade} kaç ₺ olur?",
         "{ad} için {ifade} kaç ₺ olarak hesaplanır?"]
for i, (ifade, h) in enumerate(A):
    F.hesap(R, KALIP[i % 3].format(ad="MZA A.Ş.", ifade=ifade), h, stimulus_id=S_A)

# ------------------------------------------------------------------ MZB: gelir tablosu hesap bakiyeleri
MZB = [(600, "Yurt İçi Satışlar", 3_200_000), (601, "Yurt Dışı Satışlar", 800_000), (610, "Satıştan İadeler (-)", 120_000),
       (611, "Satış İskontoları (-)", 40_000), (612, "Diğer İndirimler (-)", 20_000),
       (620, "Satılan Mamuller Maliyeti (-)", 2_600_000), (630, "Araştırma ve Geliştirme Giderleri (-)", 60_000),
       (631, "Pazarlama, Satış ve Dağıtım Giderleri (-)", 280_000), (632, "Genel Yönetim Giderleri (-)", 320_000),
       (640, "İştiraklerden Temettü Gelirleri", 30_000), (642, "Faiz Gelirleri", 25_000), (646, "Kambiyo Kârları", 40_000),
       (649, "Diğer Olağan Gelir ve Kârlar", 15_000), (653, "Komisyon Giderleri (-)", 12_000),
       (654, "Karşılık Giderleri (-)", 18_000), (656, "Kambiyo Zararları (-)", 35_000),
       (660, "Kısa Vadeli Borçlanma Giderleri (-)", 90_000), (661, "Uzun Vadeli Borçlanma Giderleri (-)", 50_000),
       (671, "Önceki Dönem Gelir ve Kârları", 20_000), (679, "Diğer Olağandışı Gelir ve Kârlar", 10_000),
       (681, "Önceki Dönem Gider ve Zararları (-)", 8_000), (689, "Diğer Olağandışı Gider ve Zararlar (-)", 22_000)]
g = {k: v for k, _, v in MZB}
brut = g[600] + g[601]
ns = brut - g[610] - g[611] - g[612]
bk = ns - g[620]
fgid = g[630] + g[631] + g[632]
fk = bk - fgid
dg = g[640] + g[642] + g[646] + g[649]
dgid = g[653] + g[654] + g[656]
fin = g[660] + g[661]
olagan = fk + dg - dgid - fin
dk = olagan + g[671] + g[679] - g[681] - g[689]
vergi = round(dk * 0.25)
nk = dk - vergi
assert (ns, bk, fk, olagan, dk) == (3_820_000, 1_220_000, 560_000, 465_000, 465_000)
S_B = F.uyaran({"id": "yet-fta-tablo-mzb", "title": "MZB A.Ş. — 2025 Gelir Tablosu Hesap Bakiyeleri", "kind": "table",
                "bodyMarkdown": "| Hesap | Tutar (₺) |\n|---|---|\n" + "\n".join(f"| {k} {ad} | {tl(v)} |" for k, ad, v in MZB),
                "caption": "MZB A.Ş.’nin 2025 yılı gelir tablosu hesap kalanları verilmiştir. Soruları MSUGT gelir "
                           "tablosu düzenine göre cevaplayınız; dönem kârı vergi karşılığı oranı %25 kabul edilecektir."})
B = [
    ("brüt satışları", Hesap(brut, "tutar", [g[600], ns, brut + g[640], brut - g[610]],
     "MZB A.Ş. brüt satışları = 600 Yurt İçi + 601 Yurt Dışı Satışlar = 3.200.000 + 800.000 = 4.000.000 ₺.")),
    ("net satışları", Hesap(ns, "tutar", [brut - g[610], brut - g[610] - g[611], brut + g[610] + g[611] + g[612], ns - g[620] + ns * 0],
     "MZB A.Ş. net satışları = 4.000.000 − (120.000 + 40.000 + 20.000) = 3.820.000 ₺.")),
    ("brüt satış kârı", Hesap(bk, "tutar", [brut - g[620], bk - fgid, ns - g[620] + g[610], bk + g[611]],
     "MZB A.Ş. brüt satış kârı = net satışlar − satışların maliyeti = 3.820.000 − 2.600.000 = 1.220.000 ₺.")),
    ("faaliyet giderleri toplamı", Hesap(fgid, "tutar", [g[631] + g[632], fgid + dgid, fgid + fin, fgid - g[630] + g[653]],
     "MZB A.Ş. faaliyet giderleri = 630 + 631 + 632 = 60.000 + 280.000 + 320.000 = 660.000 ₺.")),
    ("faaliyet kârı", Hesap(fk, "tutar", [fk + g[630], fk - fin, fk + dg, fk + dg - dgid],
     "MZB A.Ş. faaliyet kârı = brüt satış kârı − faaliyet giderleri = 1.220.000 − 660.000 = 560.000 ₺.")),
    ("diğer faaliyetlerden olağan gelir ve kârlar toplamı", Hesap(dg, "tutar", [dg - g[640], dg + g[671] + g[679], dg - dgid, dg + g[642]],
     "MZB A.Ş. 64 grubu = 640 + 642 + 646 + 649 = 30.000 + 25.000 + 40.000 + 15.000 = 110.000 ₺.")),
    ("diğer faaliyetlerden olağan gider ve zararlar toplamı", Hesap(dgid, "tutar", [dgid + fin, dgid - g[654], dgid + g[681] + g[689],
                                                                                    dgid - g[656]],
     "MZB A.Ş. 65 grubu = 653 + 654 + 656 = 12.000 + 18.000 + 35.000 = 65.000 ₺. Borçlanma giderleri 66 grubunda ayrıca "
     "gösterilir.")),
    ("finansman giderleri toplamı", Hesap(fin, "tutar", [g[660], fin + g[653], fin + g[656], fin + dgid],
     "MZB A.Ş. finansman giderleri (66) = 660 + 661 = 90.000 + 50.000 = 140.000 ₺. Komisyon ve kambiyo zararları 65 "
     "grubundadır.")),
    ("olağan kârı", Hesap(olagan, "tutar", [fk + dg - dgid, fk + dg - fin, olagan + g[671] + g[679], olagan - g[681] - g[689] + fin],
     "MZB A.Ş. olağan kârı = 560.000 + 110.000 − 65.000 − 140.000 = 465.000 ₺.")),
    ("dönem net kârı", Hesap(nk, "tutar", [dk, dk - round(olagan * 0.20), dk + g[671] - vergi, nk - g[679]],
     f"MZB A.Ş. dönem kârı = olağan kâr 465.000 + olağandışı gelir 30.000 − olağandışı gider 30.000 = 465.000 ₺; vergi "
     f"karşılığı %25 = {tl(vergi)} ₺; dönem net kârı = {tl(nk)} ₺.")),
]
for i, (ifade, h) in enumerate(B):
    F.hesap(R, KALIP[(i + 1) % 3].format(ad="MZB A.Ş.", ifade=ifade), h, stimulus_id=S_B)

# ------------------------------------------------------------------ MZC: öz kaynak değişim tablosu
bas = {"sermaye": 1_000_000, "yda": 100_000, "kar": 400_000}
art, tem, nkc, dkg = 200_000, 120_000, 260_000, 60_000
son = {"sermaye": bas["sermaye"] + art, "yda": bas["yda"] + dkg, "kar": bas["kar"] + nkc - tem}
ozc = ("| Kalem | Sermaye | Yeniden Değerleme Artışları | Birikmiş Kârlar |\n|---|---|---|---|\n"
       f"| 1 Ocak 2025 bakiyesi | {tl(bas['sermaye'])} | {tl(bas['yda'])} | {tl(bas['kar'])} |")
ek = (f"2025 yılında nakit karşılığı {tl(art)} ₺ sermaye artırımı yapılmış, ortaklara {tl(tem)} ₺ kâr payı "
      f"dağıtılmıştır. Yılın net kârı {tl(nkc)} ₺’dir; binaların yeniden değerlemesinden vergi sonrası {tl(dkg)} ₺ "
      "değer artışı diğer kapsamlı gelir olarak muhasebeleştirilmiştir.")
S_C = F.uyaran({"id": "yet-fta-tablo-mzc", "title": "MZC A.Ş. — Öz Kaynak Hareketleri", "kind": "table",
                "bodyMarkdown": ozc + "\n\n" + ek,
                "caption": "MZC A.Ş.’ye ait soruları bu bilgilere ve TMS 1 hükümlerine göre cevaplayınız."})
C = [
    ("31 Aralık 2025 öz kaynak toplamı", Hesap(sum(son.values()), "tutar",
     [sum(son.values()) - dkg, sum(son.values()) + tem, sum(bas.values()) + nkc, sum(son.values()) - art],
     "MZC A.Ş. yıl sonu öz kaynakları = 1.500.000 + 200.000 − 120.000 + 260.000 + 60.000 = 1.900.000 ₺.")),
    ("2025 yılı toplam kapsamlı geliri", Hesap(nkc + dkg, "tutar", [nkc, nkc + dkg + art - tem, nkc - tem + dkg, dkg + art],
     "MZC A.Ş. toplam kapsamlı gelir = net kâr + diğer kapsamlı gelir = 260.000 + 60.000 = 320.000 ₺. Ortaklarla "
     "işlemler (sermaye artırımı, kâr payı) toplam kapsamlı gelire girmez.")),
    ("ortaklarla yapılan işlemlerin öz kaynağa net etkisi", Hesap(art - tem, "tutar", [art + tem, art, art - tem + nkc, art - tem + dkg],
     "MZC A.Ş. ortaklarla işlemler = sermaye artırımı 200.000 − kâr payı dağıtımı 120.000 = +80.000 ₺.")),
    ("31 Aralık 2025 birikmiş kârlar tutarı", Hesap(son["kar"], "tutar", [bas["kar"] + nkc, son["kar"] + dkg, bas["kar"] - tem, son["kar"] - art],
     "MZC A.Ş. birikmiş kârlar = 400.000 + 260.000 − 120.000 = 540.000 ₺. Yeniden değerleme artışı ayrı öz kaynak "
     "kaleminde izlenir.")),
    ("2025 yılında öz kaynaklarındaki toplam artış", Hesap(sum(son.values()) - sum(bas.values()), "tutar",
     [nkc + dkg, nkc + art, nkc + dkg + art + tem, art + dkg],
     "MZC A.Ş. öz kaynak artışı = toplam kapsamlı gelir 320.000 + ortaklarla işlemler 80.000 = 400.000 ₺ (1.500.000 → "
     "1.900.000).")),
]
for i, (ifade, h) in enumerate(C):
    F.hesap(R, KALIP[(i + 2) % 3].format(ad="MZC A.Ş.", ifade=ifade), h, stimulus_id=S_C)

# ------------------------------------------------------------------ bağımsız hesaplar
smm = 800_000 + 3_000_000 - 100_000 + 50_000 - 950_000
F.hesap(R,
    "Bir ticari işletmenin 2025 yılı verileri şöyledir: dönem başı ticari mal stoku 800.000 ₺, alışlar 3.000.000 ₺, "
    "alıştan iadeler 100.000 ₺, alış giderleri (nakliye, sigorta) 50.000 ₺ ve dönem sonu ticari mal stoku 950.000 ₺."
    "\n\nSatılan ticari mallar maliyeti kaç ₺’dir?",
    Hesap(smm, "tutar", [smm + 100_000 + 100_000, smm - 50_000, 800_000 + 3_000_000 - 950_000, smm + 150_000 - 50_000],
          "SMM = dönem başı stok + alışlar − alıştan iadeler + alış giderleri − dönem sonu stok = 800.000 + 3.000.000 − "
          "100.000 + 50.000 − 950.000 = 2.800.000 ₺."))

F.hesap(R,
    "Bir işletmenin 2025 yılında brüt satışları 5.000.000 ₺’dir. Yıl içinde 150.000 ₺ satıştan iade, 60.000 ₺ satış "
    "iskontosu yapılmış; ayrıca 90.000 ₺ satış komisyonu ödenmiştir.\n\nGelir tablosunda gösterilecek net satışlar "
    "kaç ₺’dir?",
    Hesap(5_000_000 - 150_000 - 60_000, "tutar", [5_000_000 - 150_000 - 60_000 - 90_000, 5_000_000 - 150_000,
                                                   5_000_000 - 60_000, 5_000_000 + 150_000 - 60_000],
          "Net satışlar = brüt satışlar − satış indirimleri (iade + iskonto) = 5.000.000 − 210.000 = 4.790.000 ₺. Satış "
          "komisyonu pazarlama giderleridir, satış indirimi değildir."), zorluk="easy")

F.hesap("TMS 1 md. 69-71",
    "Bir işletmenin 31.12.2025 itibarıyla 900.000 ₺ tutarında uzun vadeli banka kredisi vardır. Bu kredinin 250.000 "
    "₺’lik anapara taksidi 2026 yılı içinde ödenecektir.\n\nBilançoda uzun vadeli yabancı kaynaklar içinde "
    "gösterilecek kredi tutarı kaç ₺’dir?",
    Hesap(900_000 - 250_000, "tutar", [900_000, 250_000, 900_000 + 250_000, 900_000 - 250_000 * 2],
          "Raporlama tarihinden sonraki 12 ay içinde ödenecek taksit (250.000 ₺) kısa vadeli yabancı kaynaklara "
          "aktarılır; uzun vadede 650.000 ₺ kalır."))

F.hesap(R,
    "Bir işletmenin öz kaynak kalemleri şöyledir: sermaye 500.000 ₺, sermaye yedekleri 50.000 ₺, kâr yedekleri 80.000 "
    "₺, geçmiş yıllar zararları 30.000 ₺ ve dönem net zararı 20.000 ₺.\n\nİşletmenin öz kaynak toplamı kaç ₺’dir?",
    Hesap(500_000 + 50_000 + 80_000 - 30_000 - 20_000, "tutar",
          [500_000 + 50_000 + 80_000 + 30_000 + 20_000, 500_000 + 50_000 + 80_000, 500_000 + 50_000 + 80_000 - 30_000 + 20_000,
           500_000 - 30_000 - 20_000],
          "Geçmiş yıllar zararları ve dönem net zararı öz kaynaktan indirilir: 500.000 + 50.000 + 80.000 − 30.000 − "
          "20.000 = 580.000 ₺."), zorluk="easy")

F.hesap(R,
    "Bir anonim şirketin esas sözleşmesindeki taahhüt edilen sermaye 1.000.000 ₺’dir. Ortaklar bu tutarın 300.000 "
    "₺’sini henüz ödememiştir.\n\nBilançoda öz kaynaklar içinde gösterilecek ödenmiş sermaye tutarı kaç ₺’dir?",
    Hesap(700_000, "tutar", [1_000_000, 300_000, 1_300_000, 850_000],
          "Ödenmemiş sermaye (501) sermaye hesabından indirilerek gösterilir: 1.000.000 − 300.000 = 700.000 ₺."),
    zorluk="easy")

F.hesap(R,
    "Bir işletmenin 31.12.2025 tarihinde müşterilerinden 400.000 ₺ senetsiz alacağı vardır. Bu alacağın 150.000 "
    "₺’sinin vadesi 18 ay sonradır, geri kalanı 2026 yılında tahsil edilecektir.\n\nBilançoda dönen varlıklar "
    "içindeki ticari alacaklar kaç ₺ olarak gösterilir?",
    Hesap(250_000, "tutar", [400_000, 150_000, 400_000 + 150_000, 400_000 - 150_000 / 2],
          "12 aydan uzun vadeli alacak (150.000 ₺) duran varlıklarda (220) gösterilir; dönen varlıklarda 250.000 ₺ "
          "kalır."))

F.hesap(R,
    "Bir işletmenin 2025 yılı verileri şöyledir: net satışlar 2.000.000 ₺, satışların maliyeti 1.300.000 ₺, pazarlama "
    "giderleri 150.000 ₺, genel yönetim giderleri 180.000 ₺ ve kısa vadeli borçlanma giderleri 60.000 ₺.\n\nGelir "
    "tablosunda faaliyet kârı kaç ₺ olarak gösterilir?",
    Hesap(2_000_000 - 1_300_000 - 150_000 - 180_000, "tutar",
          [2_000_000 - 1_300_000 - 150_000 - 180_000 - 60_000, 2_000_000 - 1_300_000, 2_000_000 - 1_300_000 - 180_000,
           2_000_000 - 1_300_000 - 150_000],
          "Faaliyet kârı = 2.000.000 − 1.300.000 − 150.000 − 180.000 = 370.000 ₺. Borçlanma giderleri faaliyet kârından "
          "sonra finansman giderleri olarak düşülür."), zorluk="easy")

F.hesap(R,
    "Bir işletmenin 2025 yılı gelir tablosunda faaliyet kârı 370.000 ₺, diğer faaliyetlerden olağan gelir ve kârlar "
    "40.000 ₺, diğer faaliyetlerden olağan gider ve zararlar 25.000 ₺ ve finansman giderleri 60.000 ₺’dir.\n\n"
    "İşletmenin olağan kârı kaç ₺’dir?",
    Hesap(370_000 + 40_000 - 25_000 - 60_000, "tutar", [370_000 + 40_000 - 25_000, 370_000 - 60_000, 370_000 + 40_000 + 25_000 - 60_000,
                                                          370_000 + 40_000 - 60_000],
          "Olağan kâr = 370.000 + 40.000 − 25.000 − 60.000 = 325.000 ₺."))

F.hesap(R,
    "Bir işletme 2025 yılı için 100.000 ₺ dönem kârı vergi karşılığı ayırmıştır. Yıl içinde 70.000 ₺ geçici vergi "
    "ödenmiştir.\n\nBilançoda kısa vadeli yabancı kaynaklar içinde dönem kârı vergi yükümlülüğü olarak gösterilecek net "
    "tutar kaç ₺’dir?",
    Hesap(100_000 - 70_000, "tutar", [100_000, 70_000, 100_000 + 70_000, 100_000 - 35_000],
          "371 Dönem Kârının Peşin Ödenen Vergileri hesabı 370’ten indirilerek gösterilir: 100.000 − 70.000 = 30.000 ₺."))

F.hesap(R,
    "Bir işletmenin makinelerinin maliyeti 1.200.000 ₺, birikmiş amortismanı 450.000 ₺’dir. Dönem sonunda makineler "
    "için 50.000 ₺ değer düşüklüğü karşılığı ayrılmıştır.\n\nBilançoda makinelerin net defter değeri kaç ₺’dir?",
    Hesap(1_200_000 - 450_000 - 50_000, "tutar", [1_200_000 - 450_000, 1_200_000 - 50_000, 1_200_000 - 450_000 + 50_000,
                                                   450_000 + 50_000],
          "Net defter değeri = maliyet − birikmiş amortisman − değer düşüklüğü = 1.200.000 − 450.000 − 50.000 = 700.000 ₺."),
    zorluk="easy")

F.hesap(R,
    "Bir işletmenin bilançosunda kısa vadeli yabancı kaynaklar 420.000 ₺, uzun vadeli yabancı kaynaklar 380.000 ₺ ve "
    "öz kaynaklar 1.200.000 ₺’dir. Dönen varlıklar 640.000 ₺’dir.\n\nİşletmenin duran varlıklar toplamı kaç ₺’dir?",
    Hesap(420_000 + 380_000 + 1_200_000 - 640_000, "tutar", [1_200_000 + 380_000 - 640_000, 2_000_000, 1_200_000 - 640_000 + 420_000,
                                                             1_200_000 + 380_000],
          "Aktif toplamı = pasif toplamı = 420.000 + 380.000 + 1.200.000 = 2.000.000 ₺; duran varlıklar = 2.000.000 − "
          "640.000 = 1.360.000 ₺."), zorluk="easy")

F.hesap(R,
    "Bir ticari işletmenin 2025 yılında net satışları 3.600.000 ₺’dir. Dönem başı ticari mal stoku 500.000 ₺, yıl içindeki "
    "alışları 2.900.000 ₺ ve dönem sonu ticari mal stoku 600.000 ₺’dir.\n\nİşletmenin brüt satış kârı kaç ₺’dir?",
    Hesap(3_600_000 - (500_000 + 2_900_000 - 600_000), "tutar", [3_600_000 - 2_900_000, 3_600_000 - (500_000 + 2_900_000 + 600_000),
                                                                   3_600_000 - (2_900_000 - 500_000 + 600_000), 3_600_000 - 3_400_000],
          "SMM = 500.000 + 2.900.000 − 600.000 = 2.800.000 ₺; brüt satış kârı = 3.600.000 − 2.800.000 = 800.000 ₺."))

# ------------------------------------------------------------------ TMS 1 ve Kavramsal Çerçeve
F.q("TMS 1 md. 10",
    "Bir işletmenin muhasebe müdürü, yıl sonunda yayımlanacak tam finansal tablo setini hazırlamak için belge listesi "
    "oluşturmaktadır.\n\nTMS 1 Finansal Tabloların Sunuluşu’na göre aşağıdakilerden hangisi tam bir finansal tablo "
    "setinin unsurudur?",
    "Döneme ait öz kaynak değişim tablosu",
    ["Döneme ait satılan malın maliyeti tablosu", "Döneme ait kâr dağıtım tablosu", "Yönetim kurulu faaliyet raporu",
     "Döneme ait fon akım tablosu"],
    "TMS 1 md. 10’a göre tam set; finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, öz kaynak "
    "değişim tablosu, nakit akış tablosu ve dipnotlardan (gerektiğinde karşılaştırmalı dönem başı finansal durum "
    "tablosu) oluşur.", zorluk="easy")

F.q(R,
    "Bir işletme 2025 yılında 260.000 ₺ net kâr elde etmiş, ayrıca binalarının yeniden değerlemesinden 60.000 ₺ değer "
    "artışını öz kaynakta muhasebeleştirmiştir. Yıl içinde ortaklara 120.000 ₺ kâr payı dağıtılmıştır.\n\n"
    "Net kâr ile yeniden değerleme artışının toplamı (320.000 ₺) aşağıdaki kavramlardan hangisini ifade eder?",
    "Toplam kapsamlı gelir",
    ["Dağıtılabilir kâr", "Birikmiş kârlar", "Ortaklarla yapılan işlemler", "Faaliyet kârı"],
    "Toplam kapsamlı gelir; ortaklarla ortaklık sıfatıyla yapılan işlemler hariç, dönem boyunca öz kaynakta meydana "
    "gelen değişimdir ve kâr veya zarar ile diğer kapsamlı gelirden oluşur. Kâr payı dağıtımı ortaklarla işlemdir.")

F.q("TMS 1 md. 32",
    "Bir işletmenin aynı bankada 300.000 ₺ vadesiz mevduatı ve 450.000 ₺ kısa vadeli kredi borcu bulunmaktadır. "
    "Muhasebe müdürü bilançoda yalnızca 150.000 ₺ net banka borcu göstermek istemektedir; aralarında mahsup hakkı "
    "doğuran bir sözleşme yoktur.\n\nTMS 1’e göre bu uygulamayla ilgili aşağıdakilerden hangisi doğrudur?",
    "Mevduat ve kredi ayrı ayrı gösterilir.",
    ["Aynı bankaya ait olduğundan net tutarın gösterilmesi zorunludur.",
     "Net gösterim önemlilik ilkesi gereği tercih edilmelidir.",
     "Varlık gösterilmez, yükümlülük brüt tutarıyla gösterilir.",
     "Net tutar gösterilir, brüt tutarlar dipnotta verilir."],
    "TMS 1 md. 32’ye göre bir standart gerektirmedikçe ya da izin vermedikçe varlıklar ile yükümlülükler, gelirler ile "
    "giderler netleştirilmez; mevduat ve kredi ayrı ayrı sunulur.")

F.q(R,
    "Yönetimin faaliyetlere son verme niyeti olmadan finansal tabloların hazırlanmasının dayandığı varsayım "
    "aşağıdakilerden hangisidir?",
    "İşletmenin sürekliliği",
    ["Tahakkuk esası", "Önemlilik", "Tutarlılık", "Karşılaştırılabilirlik"],
    "Finansal tablolar, yönetim işletmeyi tasfiye etme ya da faaliyetlerine son verme niyetinde değilse işletmenin "
    "sürekliliği esasına göre hazırlanır; önemli belirsizlikler açıklanır.", zorluk="easy")

F.q(R,
    "İşlemlerin etkilerinin nakit tahsil veya ödeme anında değil gerçekleştikleri dönemde tanınması "
    "aşağıdaki esaslardan hangisidir?",
    "Tahakkuk esası",
    ["Nakit esası", "İşletmenin sürekliliği", "Tarihi maliyet", "Netleştirme"],
    "Tahakkuk esasında işlemlerin etkileri nakit tahsil ya da ödeme anında değil, gerçekleştikleri dönemde "
    "tanınır. Nakit akış bilgisi dışındaki finansal tablolar bu esasa göre hazırlanır.", zorluk="easy")

F.q("TMS 1 md. 66",
    "Bir işletmenin normal faaliyet döngüsü on iki aydan kısadır. Bilançosunda raporlama tarihinden itibaren 8 ay, 14 "
    "ay ve 20 ay sonra tahsil edilecek ticari alacaklar ile alım satım amaçlı elde tutulan hisse senetleri "
    "bulunmaktadır.\n\nTMS 1’e göre aşağıdakilerden hangisi dönen varlık olarak sınıflandırılmaz?",
    "20 ay sonra tahsil edilecek ticari alacak",
    ["8 ay sonra tahsil edilecek ticari alacak", "Alım satım amaçlı elde tutulan hisse senetleri",
     "Kullanımı kısıtlanmamış banka mevduatı", "Normal faaliyet döngüsünde satılacak stoklar"],
    "Dönen varlık; normal faaliyet döngüsünde gerçekleşmesi beklenen, alım satım amaçlı tutulan, raporlama "
    "tarihinden sonraki 12 ay içinde gerçekleşecek varlık ya da nakittir. 20 ay sonra tahsil edilecek alacak duran "
    "varlıktır (14 aylık alacak da duran varlıktır).", zorluk="hard")

F.q(R,
    "TMS 1’e göre finansal tablolarda raporlanan tutarlar için önceki döneme ait bilgi verilmesi hangi gerekliliğin "
    "sonucudur?",
    "Karşılaştırmalı bilgi",
    ["İşletmenin sürekliliği varsayımı", "Netleştirme yasağı", "Tahakkuk esası", "Önemlilik ve birleştirme"],
    "TMS 1’e göre finansal tablolarda raporlanan tüm tutarlar için önceki döneme ait karşılaştırmalı bilgi sunulur; "
    "bu, kullanıcıların eğilimleri değerlendirmesini sağlar.")

F.q(R,
    "Önemsiz ve benzer gider kalemlerinin tek satırda birleştirilip önemli kalemlerin ayrı gösterilmesi hangi ilkeyle "
    "açıklanır?",
    "Önemlilik",
    ["Netleştirme yasağı", "Tutarlılık ilkesi", "İhtiyatlılık ilkesi", "Tahakkuk esası"],
    "Önemli her benzer kalem sınıfı ayrı sunulur; niteliği ya da işlevi farklı önemsiz kalemler birleştirilerek "
    "gösterilebilir. Bu, TMS 1’deki önemlilik ve birleştirme ilkesidir.", zorluk="easy")

F.q(R,
    "Bir işletme yıl içinde, binalarının gerçeğe uygun değerinin defter değerini aştığını belirleyerek yeniden "
    "değerleme modeline göre değer artışı kaydetmiştir. Artış kâr veya zararda değil öz kaynakta izlenmiştir.\n\n"
    "Bu değer artışı kapsamlı gelir tablosunda nerede gösterilir?",
    "Diğer kapsamlı gelir bölümünde",
    ["Esas faaliyet gelirleri içinde", "Finansman gelirleri içinde", "Olağandışı gelirler içinde",
     "Satış gelirlerinin düzeltmesi olarak"],
    "Maddi duran varlık yeniden değerleme artışları kâr veya zarara yansıtılmaz; diğer kapsamlı gelir olarak sunulur ve "
    "öz kaynakta yeniden değerleme artışları kaleminde birikir.")

F.q(R,
    "Bir işletmenin yönetimi, bir deprem sonucu oluşan büyük tutarlı hasar zararını gelir tablosunda 'olağanüstü "
    "kalem' başlığıyla ayrıca göstermek istemektedir. Denetçi bu sunumun TMS 1’e uygun olmadığını belirtmiştir.\n\n"
    "Denetçinin gerekçesi aşağıdakilerden hangisidir?",
    "Gelir ve gider kalemleri olağanüstü kalem olarak sunulamaz.",
    ["Deprem zararları finansal tablolarda gösterilemez.",
     "Olağanüstü kalemler öz kaynakta doğrudan gösterilmelidir.",
     "Olağanüstü kalemler nakit akış tablosunda gösterilmelidir.",
     "Deprem zararları diğer kapsamlı gelir olarak gösterilmelidir."],
    "TMS 1 md. 87’ye göre işletme hiçbir gelir veya gider kalemini kâr veya zarar tablosunda ya da dipnotlarda "
    "olağanüstü kalem olarak sunamaz; önemli kalemlerin niteliği ve tutarı ayrıca açıklanır.", zorluk="hard")

F.q(R,
    "Kavramsal Çerçeve’ye göre yararlı finansal bilginin temel niteliksel özellikleri aşağıdakilerden hangisidir?",
    "İhtiyaca uygunluk ve gerçeğe uygun sunum",
    ["Karşılaştırılabilirlik ve doğrulanabilirlik", "Zamanında sunum ve anlaşılabilirlik",
     "İhtiyatlılık ve tutarlılık", "Önemlilik ve maliyet kısıtı"],
    "Kavramsal Çerçeve’ye göre temel niteliksel özellikler ihtiyaca uygunluk ve gerçeğe uygun sunumdur; "
    "karşılaştırılabilirlik, doğrulanabilirlik, zamanında sunum ve anlaşılabilirlik destekleyici özelliklerdir.")

F.q(R,
    "Aşağıdakilerden hangisi yararlı finansal bilginin destekleyici niteliksel özelliklerinden biri değildir?",
    "Gerçeğe uygun sunum",
    ["Karşılaştırılabilirlik", "Doğrulanabilirlik", "Zamanında sunum", "Anlaşılabilirlik"],
    "Gerçeğe uygun sunum temel niteliksel özelliktir. Karşılaştırılabilirlik, doğrulanabilirlik, zamanında sunum ve "
    "anlaşılabilirlik bilginin yararını artıran destekleyici özelliklerdir.")

F.q(R,
    "Bir işletme, geçmişte imzaladığı sözleşme uyarınca kontrol ettiği ve ekonomik fayda yaratma potansiyeli taşıyan "
    "bir yazılım lisansını bilançoya almayı değerlendirmektedir.\n\nKavramsal Çerçeve’ye göre varlık tanımı "
    "aşağıdakilerden hangisidir?",
    "Geçmiş olaylar sonucunda işletmenin kontrolündeki mevcut ekonomik kaynak",
    ["Gelecekte satın alınması planlanan ve fayda sağlaması beklenen kaynak",
     "İşletmenin mülkiyetinde olan ve nakit ödenerek alınmış kaynak",
     "Geçmiş olaylardan doğan ve ekonomik kaynak transferi gerektiren mevcut yükümlülük",
     "Tüm yükümlülükler düşüldükten sonra varlıklarda kalan pay"],
    "Kavramsal Çerçeve’ye göre varlık, geçmiş olayların sonucu olarak işletme tarafından kontrol edilen mevcut ekonomik "
    "kaynaktır; ekonomik kaynak, ekonomik fayda yaratma potansiyeli olan haktır. Mülkiyet ya da nakit ödeme şartı "
    "yoktur.")

F.q(R,
    "Bir işletme giderlerini gelir tablosunda fonksiyon esasına göre (satışların maliyeti, pazarlama, genel yönetim) "
    "sınıflandırmaktadır.\n\nTMS 1’e göre bu durumda işletmenin ayrıca açıklaması gereken bilgi aşağıdakilerden "
    "hangisidir?",
    "Amortisman ve personel giderlerinin niteliğine ilişkin bilgi",
    ["Her gider kaleminin nakit olarak ödenen kısmı",
     "Giderlerin vergi matrahından indirilen kısmı",
     "Giderlerin bir sonraki yıl için bütçelenen tutarı",
     "Giderlerin sabit ve değişken olarak ayrımı"],
    "Giderlerini fonksiyon esasına göre sınıflandıran işletmeler, amortisman ve itfa ile çalışanlara sağlanan fayda "
    "giderleri dâhil giderlerin niteliğine ilişkin ek bilgi açıklar (TMS 1 md. 104).", zorluk="hard")

F.q(R,
    "Ticari mal alımı için tedarikçiye ödenen avans MSUGT bilanço düzenine göre hangi grupta gösterilir?",
    "159 hesapla stoklar grubunda",
    ["Ticari alacaklar grubunda", "Diğer alacaklar grubunda", "Hazır değerler grubunda",
     "Gelecek aylara ait giderler grubunda"],
    "MSUGT’de stok alımı için verilen avanslar 159 Verilen Sipariş Avansları hesabında izlenir ve stoklar grubunda "
    "gösterilir; mal alındığında ilgili stok hesabına aktarılır.")

F.q(R,
    "370 ve 371 hesaplarının bilançoda sunumuyla ilgili aşağıdakilerden hangisi doğrudur?",
    "371, 370’ten indirilerek net tutar KVYK’de gösterilir.",
    ["371 hesabı dönen varlıklarda, 370 hesabı KVYK’de brüt gösterilir.",
     "İki hesap toplanarak kısa vadeli yabancı kaynaklarda gösterilir.",
     "371 hesabı öz kaynaklardan indirilerek gösterilir.",
     "370 hesabı uzun vadeli yabancı kaynaklarda gösterilir."],
    "371 Dönem Kârının Peşin Ödenen Vergi ve Diğer Yükümlülükleri hesabı 370’in düzenleyici hesabıdır; bilançoda 370’ten "
    "indirilerek net tutar KVYK’de gösterilir (peşin ödeme karşılığı aşarsa fark 193’e aktarılır).")

F.q(R,
    "Bir finansal raporlama kursunda finansal tabloların sunuluşuna ilişkin ifadeler tartışılmış ve katılımcılardan "
    "hatalı olanı bulmaları istenmiştir.\n\nFinansal tabloların sunuluşuyla ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Tablolar en az iki yılda bir sunulur.",
    ["Finansal tablolar en az yılda bir kez sunulur.",
     "Finansal tablolar ve dipnotlar açıkça tanımlanır.",
     "Raporlanan tutarlar için önceki dönem bilgisi verilir.",
     "Sunumun para birimi ve yuvarlama düzeyi belirtilir."],
    "TMS 1 md. 36’ya göre tam set finansal tablolar en az yılda bir kez sunulur; iki yıllık sunum aralığı standarda "
    "aykırıdır.")

F.q(R,
    "Bir işletmenin öz kaynak değişim tablosunda sermaye artırımı ve kâr payı dağıtımı ayrı satırlarda, net kâr ve "
    "yeniden değerleme artışı ise 'toplam kapsamlı gelir' satırında gösterilmiştir.\n\nBu ayrımın amacı "
    "aşağıdakilerden hangisidir?",
    "Ortaklarla işlemleri işletmenin performansından ayırmak",
    ["Nakit girişleri ve çıkışlarını faaliyet türüne göre ayırmak",
     "Vergiye tabi ve tabi olmayan gelirleri ayırmak",
     "Kısa ve uzun vadeli kaynakları ayırmak",
     "Gerçekleşmiş ve gerçekleşmemiş zararları gizlemek"],
    "Öz kaynak değişim tablosu, ortaklarla ortaklık sıfatıyla yapılan işlemleri (sermaye artırımı, kâr payı) toplam "
    "kapsamlı gelirden (işletmenin dönem performansı) ayrı gösterir.")

F.q(R,
    "Muhasebe politikalarını ve açıklayıcı bilgileri içeren dipnotların finansal tablolar içindeki yeri "
    "aşağıdakilerden hangisidir?",
    "Tam finansal tablo setinin ayrılmaz bir parçasıdır.",
    ["Yönetimin isteğine bağlı ek bir rapordur.",
     "Bağımsız denetçiye ayrıca sunulan bir belgedir.",
     "Finansal tabloların dışında faaliyet raporu bölümüdür.",
     "Sadece halka açık şirketlerin hazırladığı bir tablodur."],
    "Dipnotlar, muhasebe politikaları ve diğer açıklayıcı bilgileri içerir ve tam finansal tablo setinin ayrılmaz "
    "parçasıdır; tablolarda sunulan kalemlerin anlaşılmasını sağlar.", zorluk="easy")

F.q(R,
    "MSUGT gelir tablosunda brüt satış kârından faaliyet giderleri düşülerek bulunan kâr aşağıdakilerden hangisidir?",
    "Faaliyet kârı",
    ["Brüt satış kârı", "Olağan kâr", "Dönem kârı", "Dönem net kârı"],
    "MSUGT düzeninde brüt satış kârından faaliyet giderleri düşülerek faaliyet kârı bulunur; ardından diğer "
    "faaliyetlerden olağan gelir ve kârlar (64) eklenir, gider ve zararlar (65) ile finansman giderleri (66) "
    "düşülerek olağan kâra ulaşılır.")

F.q(R,
    "Bir işletme bir müşterisine karşı açılan tazminat davasını kaybetmesinin muhtemel olduğunu, ödenecek tutarın "
    "güvenilir biçimde tahmin edilebildiğini belirlemiştir.\n\nKavramsal Çerçeve’deki yükümlülük tanımına göre bu "
    "durumun temel özelliği aşağıdakilerden hangisidir?",
    "Geçmiş olaydan doğan mevcut sorumluluk",
    ["Gelecekte yapılması planlanan bir harcama",
     "İşletmenin kontrol ettiği ekonomik kaynak",
     "Ortaklara dağıtılacak kâr payı",
     "Diğer kapsamlı gelir kalemi"],
    "Yükümlülük, geçmiş olayların sonucu olarak bir ekonomik kaynağı transfer etmeye yönelik mevcut sorumluluktur. Dava "
    "geçmiş bir olaydan doğmuş ve muhtemel bir çıkış gerektirmektedir.")

F.q(R,
    "Bir işletmenin muhasebe müdürü finansal durum tablosunda varlıkları dönen ve duran olarak sınıflandırmakta, ancak "
    "bir bankacılık kuruluşu olan iştiraki likidite sırasına göre sunum yapmaktadır.\n\nTMS 1’e göre bu iki "
    "uygulamayla ilgili aşağıdakilerden hangisi doğrudur?",
    "Likidite sırası daha uygun bilgi veriyorsa dönen-duran yerine kullanılır.",
    ["Tüm işletmeler istisnasız dönen-duran ayrımını kullanır.",
     "Likiditeye göre sunum kâr amacı gütmeyen kuruluşlara özgüdür.",
     "Dönen-duran ayrımı nakit akış tablosunda uygulanır.",
     "Likiditeye göre sunumda varlıklar ve yükümlülükler netleştirilir."],
    "TMS 1 md. 60’a göre işletme dönen-duran ayrımı yapar; ancak likiditeye dayalı sunum güvenilir ve daha ihtiyaca "
    "uygun bilgi sağlıyorsa (örneğin finansal kuruluşlarda) tüm varlık ve yükümlülükler likidite sırasıyla sunulur.")

if __name__ == "__main__":
    sys.exit(F.yaz())
