# -*- coding: utf-8 -*-
"""Finansal Muhasebe · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarındaki Finansal Muhasebe ağırlığını izler: dönem içi kayıt ~8, dönem sonu ~5,
stok ~3, TMS/TFRS ~3, temel kavram ~1; soruların dörtte biri kadarında şıklar tam yevmiye kaydıdır, yaklaşık
yarısı tutar veya tablo taşır. Konu havuzundaki olaylar tekrar edilmez; aynı kural farklı bir olayla ölçülür.
Dayanaklar konu builder'larıyla aynıdır (build_yk_fm_*.py); 29.09.2026 kontrolü.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K, taraf as T, hk

SURUM = ("MSUGT Tekdüzen Hesap Planı; VUK md. 229-236, 274-328; KGK TMS/TFRS 2026 seti; KDV genel oranı %20; "
         "29.09.2026 kontrolü")
KY, ST, DS, TF, TK = ("muhasebe_kayitlari", "finansal_stoklar", "donem_sonu_islemleri", "tms_tfrs", "temel_kavramlar")
R = "MSUGT Tekdüzen Hesap Planı"
KAYIT = "Bu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?"
DOGRU = "Bu işleme ilişkin kayıt için aşağıdakilerden hangisi doğrudur?"


def paket(dosya, seed, ek=()):
    return Paket(dosya, lesson="finansal_muhasebe", topic=KY, konu_adi="Finansal Muhasebe", seed=seed, surum=SURUM,
                 havuz="bolum", ek_idler=ek)


def reeskont(nominal, gun, oran):
    v = nominal * gun * oran / (36_000 + gun * oran)
    assert v == int(v), v
    return int(v)


T1 = paket("questions_finansal_muhasebe_2026.json", 2026093071)
T2 = paket("questions_finansal_muhasebe_test2_2026.json", 2026093072)
T3 = paket("questions_finansal_muhasebe_test3_2026.json", 2026093073)

# =============================================================================================== TEST 1
T1.q(f"{R}: 120, 391, 642",
    "İşletmenin iki ay önce vadeli sattığı malların bedelini müşteri vadesinde ödeyememiş; taraflar ödemenin bir ay "
    "ertelenmesi karşılığında vade farkı uygulanmasında anlaşmıştır. İşletme müşterisine 5.000 ₺ + %20 KDV tutarında "
    f"vade farkı faturası düzenlemiştir.\n\n{KAYIT}",
    K([(120, 6_000)], [(642, 5_000), (391, 1_000)]),
    [K([(120, 6_000)], [(600, 5_000), (391, 1_000)]),
     K([(120, 5_000)], [(642, 5_000)]),
     K([(120, 6_000)], [(647, 5_000), (391, 1_000)]),
     K([(121, 6_000)], [(642, 5_000), (391, 1_000)])],
    "Vade farkı satılan malın bedeli değil, alacağın ertelenmesinin karşılığı olan faiz niteliğinde gelirdir: 642 Faiz "
    "Gelirleri 5.000 ₺ alacak. Vade farkı KDV’ye tabidir (391’e 1.000 ₺); müşteri alacağı 6.000 ₺ artar.")

T1.q(f"{R}: 102, 121, 780",
    "İşletme portföyündeki 45.000 ₺ nominal değerli bir müşteri senedini vadesinde tahsil edilmek üzere bankaya "
    "vermiştir. Banka senedi vadesinde tahsil etmiş, 250 ₺ tahsil masrafını keserek kalanı işletmenin hesabına "
    f"yatırmıştır; işletme banka masraflarını finansman gideri olarak izlemektedir.\n\n{DOGRU}",
    T(780, "borç", 250),
    [T(657, "borç", 250), T(121, "alacak", 44_750), T(642, "alacak", 250), T(102, "borç", 45_000)],
    "Tahsil edilen senet 121 Alacak Senetleri hesabından nominal değeriyle çıkarılır; bankaya yatan 44.750 ₺ 102’ye, "
    "işletmenin politikası gereği 250 ₺ tahsil masrafı 780 Finansman Giderleri hesabına borç yazılır.", topic=KY)

T1.q(f"{R}: 320, 321",
    "İşletme satıcısına olan 80.000 ₺ tutarındaki senetsiz ticari borcu için, satıcının talebi üzerine üç ay vadeli ve "
    "80.000 ₺ nominal değerli bir bono düzenleyerek vermiştir. Vade farkı uygulanmamış ve başka ödeme yapılmamıştır."
    f"\n\n{DOGRU}",
    T(320, "borç", 80_000),
    [T(321, "borç", 80_000), T(121, "borç", 80_000), T(320, "alacak", 80_000), T(103, "alacak", 80_000)],
    "Senetsiz borç senede bağlandığında borç 320 Satıcılar hesabından çıkar (320 borç) ve 321 Borç Senetleri hesabına "
    "alacak yazılır; toplam borç tutarı değişmez.", topic=KY, zorluk="easy")

T1.q(f"{R}: 335, 360, 361, 102",
    "İşletme şubat başında ocak ayı bordrosuna ilişkin ödemeleri tek seferde yapmıştır: çalışanlara 70.000 ₺ net ücret, "
    "Sosyal Güvenlik Kurumuna işçi ve işveren payları toplamı 30.000 ₺, vergi dairesine muhtasar beyanname ile 12.000 ₺ "
    f"gelir ve damga vergisi. Tahakkuk kayıtları ocak sonunda yapılmıştır.\n\n{KAYIT}",
    K([(335, 70_000), (361, 30_000), (360, 12_000)], [(102, 112_000)]),
    [K([(770, 112_000)], [(102, 112_000)]),
     K([(335, 70_000), (360, 42_000)], [(102, 112_000)]),
     K([(335, 82_000), (361, 30_000)], [(102, 112_000)]),
     K([(102, 112_000)], [(335, 70_000), (361, 30_000), (360, 12_000)])],
    "Tahakkukta alacaklandırılan 335 Personele Borçlar, 361 Ödenecek Sosyal Güvenlik Kesintileri ve 360 Ödenecek Vergi "
    "ve Fonlar hesapları ödemeyle borçlandırılarak kapatılır; 102 Bankalar 112.000 ₺ alacaklandırılır.", topic=KY)

T1.q(f"{R}: 610, 391, 100",
    "Perakende mağazası dün peşin sattığı 4.000 ₺ + %20 KDV tutarındaki bir ürünün bozuk çıkması üzerine müşterinin "
    "iadesini kabul etmiş ve bedeli kasadan nakit olarak geri ödemiştir. İade için gerekli belgeler düzenlenmiş, işletme "
    f"aralıklı envanter uygulamaktadır.\n\n{DOGRU}",
    T(391, "borç", 800),
    [T(191, "borç", 800), T(600, "borç", 4_000), T(100, "borç", 4_800), T(610, "alacak", 4_000)],
    "Satıştan iadede 610 Satıştan İadeler 4.000 ₺ ve satışta hesaplanan KDV’nin düzeltilmesi için 391 Hesaplanan KDV "
    "800 ₺ borçlandırılır; 100 Kasa 4.800 ₺ alacaklandırılır.", topic=KY)

T1.q(f"{R}: 197, 770, 191",
    "Ay ortasında yapılan sayımda saptanan ve 197 hesabına alınan 1.500 ₺ kasa noksanının, kasiyerin kaydetmeyi unuttuğu "
    "1.250 ₺ + %20 KDV tutarlı kırtasiye faturasından kaynaklandığı anlaşılmıştır. Kırtasiye idari bölümde "
    f"kullanılmıştır.\n\n{KAYIT}",
    K([(770, 1_250), (191, 250)], [(197, 1_500)]),
    [K([(770, 1_500)], [(197, 1_500)]),
     K([(689, 1_500)], [(197, 1_500)]),
     K([(770, 1_250), (191, 250)], [(100, 1_500)]),
     K([(135, 1_500)], [(197, 1_500)])],
    "Kasa sayım tarihinde zaten alacaklandırılmıştır; nedeni anlaşılan noksan 197’den çıkarılıp ilgili hesaplara "
    "aktarılır: 770 borç 1.250 ₺, 191 İndirilecek KDV borç 250 ₺, 197 alacak 1.500 ₺.", topic=KY)

eur, kk, kt = 20_000, 46, 45.2
T1.q(f"{R}: 102, 120, 656",
    f"İşletme ihracattan doğan 20.000 avro tutarındaki alacağını {kk} ₺ kurla kaydetmiştir. Alacak, avronun {tl(kt)} ₺’ye "
    "gerilediği tarihte tahsil edilmiş ve dövizler işletmenin döviz tevdiat hesabına geçmiştir. Arada dönem sonu "
    f"değerlemesi yapılmamıştır.\n\n{KAYIT}",
    K([(102, eur * kt), (656, eur * (kk - kt))], [(120, eur * kk)]),
    [K([(102, eur * kt)], [(120, eur * kt)]),
     K([(102, eur * kk)], [(120, eur * kt), (646, eur * (kk - kt))]),
     K([(102, eur * kt), (780, eur * (kk - kt))], [(120, eur * kk)]),
     K([(102, eur * kt), (656, eur * (kk - kt))], [(601, eur * kk)])],
    f"Alacak {tl(eur * kk)} ₺ ile kayıtlıdır, tahsil edilen dövizin karşılığı {tl(eur * kt)} ₺’dir. Kur düşüşünden doğan "
    f"{tl(eur * (kk - kt))} ₺ 656 Kambiyo Zararları hesabına borç yazılır; 120 kayıtlı tutarıyla kapatılır.", topic=KY)

T1.q(f"{R}: 340, 120, 600, 391",
    "Mobilya üreticisi bir ay önce bir otelden 50.000 ₺ sipariş avansı tahsil edip 340 hesabına kaydetmiştir. Bu ay "
    "200.000 ₺ + %20 KDV tutarındaki mobilyalar teslim edilip faturası düzenlenmiş, avans mahsup edilmiş ve kalan tutarın "
    f"30 gün sonra tahsili kararlaştırılmıştır.\n\n{KAYIT}",
    K([(340, 50_000), (120, 190_000)], [(600, 200_000), (391, 40_000)]),
    [K([(340, 50_000), (120, 190_000)], [(600, 240_000)]),
     K([(120, 240_000)], [(600, 200_000), (391, 40_000)]),
     K([(159, 50_000), (120, 190_000)], [(600, 200_000), (391, 40_000)]),
     K([(340, 50_000), (120, 150_000)], [(600, 200_000)])],
    "Teslimle satış gerçekleşir: 600’e 200.000 ₺, 391’e 40.000 ₺ alacak. Alınan avans 340 Alınan Sipariş Avansları "
    "borçlandırılarak mahsup edilir, kalan 190.000 ₺ 120 Alıcılar hesabına borç yazılır.", topic=KY, zorluk="hard")

p = [(300, 20), (500, 22), (400, 25)]
ds_fifo = 400 * 25 + 100 * 22
T1.q("TMS 2 md. 25; FIFO",
    "Sürekli envanter ve FIFO uygulayan işletmenin bir ürüne ait yıl içi hareketleri şöyledir:\n\n"
    "| Tarih | Hareket | Adet | Birim maliyet (₺) |\n|---|---|---|---|\n| 1 Ocak | Dönem başı | 300 | 20 |\n"
    "| 12 Mart | Alış | 500 | 22 |\n| 20 Haziran | Satış | 700 | — |\n| 9 Ekim | Alış | 400 | 25 |\n\n"
    "TMS 2 Stoklar’a göre yıl sonu stok değeri ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"500 adet stok {tl(ds_fifo)} ₺’dir.",
    [f"500 adet stok {tl(500 * 25)} ₺’dir.", f"500 adet stok {tl(500 * 22)} ₺’dir.",
     f"500 adet stok {tl(300 * 20 + 200 * 22)} ₺’dir.", f"600 adet stok {tl(400 * 25 + 200 * 22)} ₺’dir."],
    f"Haziran satışı 300 × 20 ve 400 × 22 ile karşılanır; elde 100 × 22 kalır. Ekim alışıyla stok 100 × 22 + 400 × 25 "
    f"= {tl(ds_fifo)} ₺ olur (500 adet).", topic=ST, zorluk="hard")

dimm, dis, gug, dbym, dsym, adet = 300_000, 180_000, 120_000, 40_000, 60_000, 2_000
tam = dimm + dis + gug + dbym - dsym
T1.q("TMS 2; THP 151, 152",
    f"Üretim işletmesinde ay içinde direkt ilk madde {tl(dimm)} ₺, direkt işçilik {tl(dis)} ₺ ve genel üretim gideri "
    f"{tl(gug)} ₺ oluşmuştur. Ay başı yarı mamul stoku {tl(dbym)} ₺, ay sonu yarı mamul stoku {tl(dsym)} ₺’dir ve ay "
    "içinde 2.000 adet mamul tamamlanmıştır.\n\nTamamlanan mamullerle ilgili aşağıdakilerden hangisi doğrudur?",
    f"Maliyet {tl(tam)} ₺, birim maliyet {tl(tam // adet)} ₺’dir.",
    [f"Maliyet {tl(dimm + dis + gug)} ₺, birim maliyet {tl((dimm + dis + gug) // adet)} ₺’dir.",
     f"Maliyet {tl(dimm + dis + gug + dsym - dbym)} ₺, birim maliyet {tl((dimm + dis + gug + dsym - dbym) // adet)} ₺’dir.",
     f"Maliyet {tl(dimm + dis)} ₺, birim maliyet {tl((dimm + dis) // adet)} ₺’dir.",
     f"Maliyet {tl(tam + dsym)} ₺, birim maliyet {tl((tam + dsym) // adet)} ₺’dir."],
    f"Tamamlanan üretim maliyeti = dönem üretim maliyeti + dönem başı yarı mamul − dönem sonu yarı mamul = "
    f"{tl(dimm + dis + gug)} + {tl(dbym)} − {tl(dsym)} = {tl(tam)} ₺; birim maliyet {tl(tam)} / 2.000 = {tl(tam // adet)} ₺.",
    topic=ST, zorluk="hard")

T1.q(f"{R}: 621, 153",
    "Aralıklı envanter uygulayan işletmenin dönem başı ticari mal stoku 60.000 ₺, dönem içi alışları 500.000 ₺’dir. "
    "Alışlarla ilgili taşıma giderleri (15.000 ₺) dönem içinde doğrudan 153 hesabına eklenmemiş, ayrı bir alt hesapta "
    "izlenmiştir. Yıl sonu sayımında 80.000 ₺ stok bulunmuştur.\n\nDönem sonu maliyet kaydı için aşağıdakilerden hangisi "
    "doğrudur?",
    T(621, "borç", 495_000),
    [T(621, "borç", 480_000), T(621, "borç", 575_000), T(153, "borç", 495_000), T(621, "borç", 420_000)],
    "Alış giderleri stok maliyetinin parçasıdır: satılan malın maliyeti = 60.000 + 500.000 + 15.000 − 80.000 = 495.000 ₺; "
    "621 borç, 153 alacak yazılır.", topic=ST)

amo = 600_000 * 40 // 100
T1.q("VUK md. 315; THP 257, 760, 770",
    "7/A seçeneğini uygulayan işletme yıl başında 600.000 ₺’ye aldığı ve faydalı ömrü 5 yıl olan hafif ticari aracı "
    "azalan bakiyeler yöntemiyle amortismana tabi tutmaktadır. Araç zamanın %70’inde dağıtımda, %30’unda idari işlerde "
    "kullanılmaktadır.\n\nİlk yıl sonunda yapılacak amortisman kaydı aşağıdakilerden hangisidir?",
    K([(760, amo * 70 // 100), (770, amo * 30 // 100)], [(257, amo)]),
    [K([(760, 84_000), (770, 36_000)], [(257, 120_000)]),
     K([(770, amo)], [(257, amo)]),
     K([(760, amo * 70 // 100), (770, amo * 30 // 100)], [(254, amo)]),
     K([(760, amo * 30 // 100), (770, amo * 70 // 100)], [(257, amo)])],
    f"Azalan bakiyeler oranı normal oranın iki katıdır: %20 × 2 = %40; ilk yıl 600.000 × %40 = {tl(amo)} ₺. Kullanım "
    f"payına göre {tl(amo * 70 // 100)} ₺ 760’a, {tl(amo * 30 // 100)} ₺ 770’e borç, 257 hesabına alacak yazılır.",
    topic=DS, zorluk="hard")

rs1 = reeskont(62_000, 30, 40)
T1.q("VUK md. 281; THP 122, 657",
    "Yıl sonunda işletmenin elinde, bir müşterisinden aldığı ve vadesine 30 gün kalan 62.000 ₺ nominal değerli tek bir "
    "senet vardır. İşletme senetli alacakları için reeskont uygulamakta, iç iskonto yöntemini ve yıllık %40 oranını "
    "kullanmaktadır.\n\nVergi Usul Kanunu’ndaki reeskont esaslarına göre yıl sonu kaydı aşağıdakilerden hangisidir?",
    K([(657, rs1)], [(122, rs1)]),
    [K([(657, 2_067)], [(122, 2_067)]),
     K([(122, rs1)], [(647, rs1)]),
     K([(657, rs1)], [(121, rs1)]),
     K([(780, rs1)], [(122, rs1)])],
    f"İç iskonto: 62.000 × 30 × 40 / (36.000 + 30 × 40) = {tl(rs1)} ₺. Senet bugünkü değere indirilir: 657 Reeskont Faiz "
    "Giderleri borç, 122 Alacak Senetleri Reeskontu alacak. Dış iskonto yaklaşık 2.067 ₺ verirdi.", topic=DS)

kv, gecici, stopaj = 150_000, 60_000, 8_000
T1.q(f"{R}: 370, 371, 360",
    f"Yıl sonunda {tl(kv)} ₺ kurumlar vergisi karşılığı ayrılmıştır. Yıl içinde {tl(gecici)} ₺ geçici vergi ödenmiş, "
    f"ayrıca mevduat faizlerinden kesilen {tl(stopaj)} ₺ vergi dönem sonunda 193’ten 371 hesabına aktarılmıştır. Beyanname "
    "şubat ayında verilecektir.\n\nKarşılığın mahsubuna ilişkin kayıt için aşağıdakilerden hangisi doğrudur?",
    T(360, "alacak", kv - gecici - stopaj),
    [T(360, "alacak", kv - gecici), T(193, "alacak", stopaj), T(371, "alacak", gecici), T(360, "alacak", kv)],
    f"371’de geçici vergi ile aktarılan tevkifat birlikte ({tl(gecici + stopaj)} ₺) bulunur ve karşılıktan mahsup edilir; "
    f"kalan {tl(kv - gecici - stopaj)} ₺ 360 hesabına alacak yazılır.", topic=DS, zorluk="hard")

T1.q(f"{R}: 120, 656",
    "İşletmenin yıl sonunda bir müşterisinden 8.000 ABD doları alacağı vardır. Alacak 42 ₺ kurla kaydedilmiş, değerleme "
    "günü kuru 41,25 ₺ olarak açıklanmıştır. Alacağın ocak ayında tahsil edilmesi beklenmektedir.\n\nDönem sonu "
    "değerleme kaydı için aşağıdakilerden hangisi doğrudur?",
    T(656, "borç", 6_000),
    [T(646, "alacak", 6_000), T(120, "borç", 6_000), T(656, "borç", 330_000), T(780, "borç", 6_000)],
    "Alacak 8.000 × 41,25 = 330.000 ₺’ye inmiştir; kayıtlı değer 336.000 ₺. 6.000 ₺ azalış 656 Kambiyo Zararları borç, "
    "120 Alıcılar alacak ile kaydedilir.", topic=DS)

T1.q(f"{R}: 690",
    "Yıl sonunda gelir tablosu hesaplarının bakiyeleri şöyledir: 600 Yurt İçi Satışlar 2.400.000 ₺, 611 Satış "
    "İskontoları 60.000 ₺, 621 Satılan Ticari Mallar Maliyeti 1.500.000 ₺, 631 Pazarlama Giderleri 280.000 ₺, 642 Faiz "
    "Gelirleri 40.000 ₺, 660 Kısa Vadeli Borçlanma Giderleri 100.000 ₺.\n\nBu verilere göre aşağıdakilerden hangisi "
    "doğrudur?",
    "690 hesabı 500.000 ₺ kâr gösterir.",
    ["690 hesabı 560.000 ₺ kâr gösterir.",
     "690 hesabı 460.000 ₺ kâr gösterir.",
     "690 hesabı 600.000 ₺ kâr gösterir.",
     "690 hesabı 440.000 ₺ kâr gösterir."],
    "Gelirler: 2.400.000 + 40.000 = 2.440.000 ₺; gider ve indirimler: 60.000 + 1.500.000 + 280.000 + 100.000 = "
    "1.940.000 ₺. 690 Dönem Kârı veya Zararı hesabı 500.000 ₺ alacak bakiye (kâr) verir.", topic=DS, zorluk="hard")

T1.q("TMS 16 md. 41",
    "Yeniden değerleme modelini uygulayan işletme, kalan faydalı ömrü 20 yıl olan idari binasını yıl başında 2.600.000 ₺ "
    "gerçeğe uygun değerle yeniden değerlemiştir. Kalıntı değer yoktur ve eşit tutarlı amortisman "
    "uygulanmaktadır.\n\nTMS 16’ya göre yeniden değerleme sonrasında ayrılacak yıllık amortisman ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Yeniden değerlenmiş tutar üzerinden yıllık 130.000 ₺ ayrılır.",
    ["Tarihi maliyet üzerinden amortisman ayrılmaya devam edilir.",
     "Yeniden değerlenmiş varlık için amortisman ayrılmaz.",
     "Yıllık 130.000 ₺ ayrılır, özkaynaktan düşülür.",
     "Değer artışı kadar ek amortisman ilk yıl ayrılır."],
    "Yeniden değerlenen varlığın amortismanı yeni defter değeri üzerinden kalan ömre göre hesaplanır: 2.600.000 / 20 = "
    "130.000 ₺; amortisman kâr veya zarara gider yazılır.", topic=TF)

T1.q("TFRS 15 md. 22, 76",
    "Yazılım şirketi bir müşterisine lisans ve bir yıllık teknik destek hizmetini birlikte 60.000 ₺’ye satmıştır. "
    "Lisansın tek başına satış fiyatı 50.000 ₺, bir yıllık desteğin tek başına satış fiyatı 25.000 ₺’dir; lisans 1 "
    "Temmuz’da devredilmiş, destek aynı tarihte başlamıştır.\n\nYıl sonu hasılatı ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "Lisans 40.000 ₺, destek 10.000 ₺; toplam 50.000 ₺ hasılat.",
    ["Lisans 50.000 ₺, destek 5.000 ₺; toplam 55.000 ₺ hasılat.",
     "60.000 ₺’nin tamamı 1 Temmuz’da hasılat olur.",
     "Lisans 40.000 ₺, destek 20.000 ₺; toplam 60.000 ₺ hasılat.",
     "Lisans 35.000 ₺, destek 12.500 ₺; toplam 47.500 ₺ hasılat."],
    "İşlem bedeli tek başına satış fiyatları oranında dağıtılır: lisansa 60.000 × 50/75 = 40.000 ₺ (devirde), desteğe "
    "20.000 ₺ (bir yıla yayılır; altı ayı 10.000 ₺). Yıl sonu hasılatı 50.000 ₺.", topic=TF, zorluk="hard")

T1.q("TMS 10 md. 3, 9-11",
    "Raporlama dönemi 31 Aralık’ta biten işletmenin finansal tabloları 25 Mart’ta yayımlanacaktır. Bu tarihler arasında "
    "şu olaylar yaşanmıştır: bir müşterinin iflası, yıl içinde açılmış bir davanın sonuçlanması, yıl sonu stoklarının "
    "maliyetin altında satılması, geçmiş yıl hatasının fark edilmesi ve 20 Şubat’ta depoda çıkan yangın.\n\nTMS 10’a göre "
    "bu olaylardan hangisi düzeltme gerektiren olay değildir?",
    "20 Şubat’ta depoda çıkan yangın",
    ["Yıl sonunda durumu bozuk müşterinin iflası",
     "Yıl içinde açılmış davanın sonuçlanması",
     "Yıl sonu stoklarının maliyetin altında satılması",
     "Önceki dönem hatasının fark edilmesi"],
    "Yangın raporlama döneminden sonra ortaya çıkan ve dönem sonundaki koşullarla ilgisi olmayan bir olaydır; düzeltme "
    "gerektirmez, önemliyse açıklanır. Diğerleri dönem sonunda var olan koşullar hakkında kanıt sağlar.", topic=TF)

T1.q("MSUGT: tam açıklama",
    "İşletme 12.000.000 ₺ tutarındaki yatırım kredisi karşılığında fabrika binasını bankaya ipotek etmiştir. Ayrıca "
    "stoklarını FIFO yöntemiyle değerlediğini ve bir müşterisiyle 3.000.000 ₺’lik bir sözleşme uyuşmazlığı olduğunu "
    "finansal tablolarında belirtmek istememektedir.\n\nBu bilgilerin dipnotlarda açıklanması hangi temel kavramın "
    "gereğidir?",
    "Tam açıklama",
    ["İhtiyatlılık", "Maliyet esası", "Özün önceliği", "Dönemsellik"],
    "Tam açıklama kavramı; teminatlar, uygulanan muhasebe politikaları ve önemli belirsizlikler gibi kararları "
    "etkileyebilecek bilgilerin finansal tablolarda yeterli ve açık biçimde açıklanmasını gerektirir.", topic=TK,
    zorluk="easy")

# =============================================================================================== TEST 2
T2.q(f"{R}: 102, 108, 653",
    "Perakende mağazasının kredi kartıyla yaptığı 30.000 ₺’lik satışların bedeli, anlaşmalı banka tarafından 30 gün sonra "
    "%2 komisyon kesilerek işletmenin hesabına aktarılmıştır. İşletme POS komisyonlarını 653 Komisyon Giderleri "
    f"hesabında izlemektedir; satış kaydı daha önce yapılmıştır.\n\n{KAYIT}",
    K([(102, 29_400), (653, 600)], [(108, 30_000)]),
    [K([(102, 29_400), (653, 600)], [(120, 30_000)]),
     K([(102, 30_000)], [(108, 29_400), (643, 600)]),
     K([(102, 29_400), (653, 600)], [(600, 30_000)]),
     K([(102, 29_400), (780, 600)], [(101, 30_000)])],
    "Kredi kartı satışından bankadan alınacak tutar 108 Diğer Hazır Değerler hesabında izlenmişti; tahsilatta 108 "
    "alacaklandırılır, net tutar 102’ye, kesilen 600 ₺ komisyon işletmenin politikası gereği 653’e borç yazılır.")

T2.q(f"{R}: 331, 360, 102",
    "Genel kurul kararıyla gerçek kişi ortaklara dağıtılacak 300.000 ₺ brüt kâr payı üzerinden %15 gelir vergisi "
    "kesintisi yapılmış; kesinti ile net tutar kayda alınmıştır. Bu ay net kâr payı ortakların hesaplarına, kesilen vergi "
    f"de muhtasar beyanla vergi dairesine ödenmiştir.\n\n{DOGRU}",
    T(331, "borç", 255_000),
    [T(331, "borç", 300_000), T(570, "borç", 300_000), T(360, "alacak", 45_000), T(193, "borç", 45_000)],
    "Kâr dağıtım kaydında net kâr payı 331 Ortaklara Borçlar, kesinti 360 Ödenecek Vergi ve Fonlar hesabına alacak "
    "yazılmıştı. Ödemede bu hesaplar borçlandırılarak kapatılır, 102 Bankalar 300.000 ₺ alacaklandırılır.")

T2.q(f"{R}: 153, 191, 103, 321",
    "İşletme 100.000 ₺ + %20 KDV tutarında ticari mal satın almıştır. Bedelin 50.000 ₺’si için kendi bankasına çekilmiş "
    "bir çek düzenlenmiş, kalan 70.000 ₺ için üç ay vadeli bir bono verilmiştir. Mallar ambara alınmıştır.\n\n"
    f"{KAYIT}",
    K([(153, 100_000), (191, 20_000)], [(103, 50_000), (321, 70_000)]),
    [K([(153, 100_000), (191, 20_000)], [(101, 50_000), (321, 70_000)]),
     K([(153, 100_000), (191, 20_000)], [(103, 50_000), (320, 70_000)]),
     K([(153, 120_000)], [(103, 50_000), (321, 70_000)]),
     K([(153, 100_000), (191, 20_000)], [(102, 50_000), (121, 70_000)])],
    "Mal 153’e, KDV 191’e borç yazılır. İşletmenin kendi düzenlediği çek 103 Verilen Çekler ve Ödeme Emirleri, verdiği "
    "bono 321 Borç Senetleri hesabına alacak yazılır; 101 ve 121 müşterilerden alınan kıymetli evrakı izler.")

T2.q(f"{R}: 100, 153, 191",
    "İşletme geçen hafta peşin olarak satın aldığı 10.000 ₺ + %20 KDV tutarındaki ticari malı, sipariş edilenden farklı "
    "model olduğu için satıcıya iade etmiştir. Satıcı iadeyi kabul ederek bedeli işletmeye nakit olarak geri "
    f"ödemiştir.\n\n{DOGRU}",
    T(191, "alacak", 2_000),
    [T(391, "alacak", 2_000), T(610, "borç", 10_000), T(153, "alacak", 12_000), T(320, "borç", 12_000)],
    "Alıştan iade stoku azaltır (153 alacak 10.000 ₺); alışta indirilen KDV düzeltilir (191 alacak 2.000 ₺). Bedel "
    "nakit iade edildiğinden 100 Kasa borçlandırılır; 610 satıcının kullandığı hesaptır.", zorluk="easy")

T2.q(f"{R}: 102, 400, 780",
    "İşletme üç yıl vadeli 900.000 ₺ yatırım kredisi kullanmıştır. Banka kredi tahsis ücreti olarak 6.000 ₺, ipotek "
    "tesisi için yapılan 4.000 ₺ masrafı keserek kalanı işletmenin hesabına aktarmıştır; işletme bu masrafları dönem "
    f"gideri olarak izlemektedir.\n\n{KAYIT}",
    K([(102, 890_000), (780, 10_000)], [(400, 900_000)]),
    [K([(102, 890_000), (780, 10_000)], [(300, 900_000)]),
     K([(102, 890_000)], [(400, 890_000)]),
     K([(102, 900_000)], [(400, 890_000), (642, 10_000)]),
     K([(102, 890_000), (780, 6_000), (770, 4_000)], [(303, 900_000)])],
    "Üç yıl vadeli kredi uzun vadeli yabancı kaynaktır: 400 Banka Kredileri 900.000 ₺ alacak. Kesilen 10.000 ₺ masraf "
    "780 Finansman Giderleri hesabına, 890.000 ₺ 102’ye borç yazılır.", zorluk="hard")

T2.q(f"{R}: 397, 120",
    "Ay ortasındaki kasa sayımında bulunan ve 397 Sayım ve Tesellüm Fazlaları hesabına alınan 2.500 ₺’nin, bir "
    "müşterinin kasaya yaptığı ancak kaydedilmeyen borç ödemesinden kaynaklandığı anlaşılmıştır. Müşterinin cari hesabı "
    f"120 hesabında izlenmektedir.\n\n{DOGRU}",
    T(120, "alacak", 2_500),
    [T(679, "alacak", 2_500), T(397, "alacak", 2_500), T(100, "borç", 2_500), T(600, "alacak", 2_500)],
    "Kasa sayım tarihinde 100 borç, 397 alacak ile artırılmıştı. Nedeni anlaşılan fazlalık 397’den çıkarılır ve "
    "tahsilat müşterinin hesabına işlenir: 397 borç, 120 Alıcılar alacak 2.500 ₺.")

T2.q(f"{R}: 542, 500",
    "Anonim şirketin genel kurulu, 542 Olağanüstü Yedekler hesabında bulunan 400.000 ₺’nin tamamının sermayeye "
    "eklenmesine karar vermiş, sermaye artırımı ticaret siciline tescil edilmiştir. Ortaklara yeni paylar bedelsiz "
    f"olarak dağıtılacaktır.\n\n{DOGRU}",
    T(542, "borç", 400_000),
    [T(501, "borç", 400_000), T(542, "alacak", 400_000), T(520, "alacak", 400_000), T(102, "borç", 400_000)],
    "İç kaynaklardan sermaye artırımında özkaynak toplamı değişmez, kalemler arasında aktarım olur: 542 Olağanüstü "
    "Yedekler borç, 500 Sermaye alacak 400.000 ₺. Ortaklardan nakit tahsil edilmediği için 501 kullanılmaz.")

T2.q(f"{R}: 102, 128",
    "Protesto edildikten sonra 128 Şüpheli Ticari Alacaklar hesabına aktarılan 36.000 ₺’lik müşteri senedinin bedeli, "
    "icra takibi sonucunda borçlu tarafından banka hesabına ödenmiştir. Bu alacak için daha önce karşılık "
    f"ayrılmamıştır.\n\n{DOGRU}",
    T(128, "alacak", 36_000),
    [T(129, "borç", 36_000), T(644, "alacak", 36_000), T(121, "alacak", 36_000), T(654, "alacak", 36_000)],
    "Tahsilatla 102 Bankalar borç, 128 Şüpheli Ticari Alacaklar alacak 36.000 ₺ yazılır. Karşılık ayrılmadığından 129 ve "
    "644 hesapları kullanılmaz.", zorluk="easy")

ort = (18_000 + 42_000 + 26_000) / 4_000
T2.q("TMS 2 md. 25; ağırlıklı ortalama",
    "Dönemsel ağırlıklı ortalama yöntemini ve aralıklı envanteri uygulayan işletmenin verileri şöyledir:\n\n"
    "| Kalem | Adet | Birim maliyet (₺) |\n|---|---|---|\n| Dönem başı stok | 1.000 | 18 |\n"
    "| Mart alışı | 2.000 | 21 |\n| Ekim alışı | 1.000 | 26 |\n\nYıl içinde 3.200 adet satılmıştır.\n\n"
    "Dönem sonu satılan malın maliyeti kaydı aşağıdakilerden hangisidir?",
    K([(621, 3_200 * ort)], [(153, 3_200 * ort)]),
    [K([(621, 1_000 * 18 + 2_000 * 21 + 200 * 26)], [(153, 1_000 * 18 + 2_000 * 21 + 200 * 26)]),
     K([(621, 3_200 * 21)], [(153, 3_200 * 21)]),
     K([(621, 800 * ort)], [(153, 800 * ort)]),
     K([(153, 3_200 * ort)], [(621, 3_200 * ort)])],
    f"Ağırlıklı ortalama birim maliyet (18.000 + 42.000 + 26.000) / 4.000 = {tl(ort)} ₺; SMM 3.200 × {tl(ort)} = "
    f"{tl(3_200 * ort)} ₺. FIFO {tl(1_000 * 18 + 2_000 * 21 + 200 * 26)} ₺ verirdi.", topic=ST, zorluk="hard")

T2.q("TMS 2 md. 28-33; THP 158, 654",
    "Yıl sonunda işletmenin mamul stokundaki bir ürün grubunun üretim maliyeti 400.000 ₺’dir. Olağan faaliyet akışında "
    "tahmini satış fiyatı 390.000 ₺, satışı gerçekleştirmek için gerekli pazarlama ve dağıtım maliyetleri 25.000 ₺ olarak "
    "öngörülmüştür.\n\nTMS 2 Stoklar’a göre dönem sonunda yapılacak kayıt aşağıdakilerden hangisidir?",
    K([(654, 35_000)], [(158, 35_000)]),
    [K([(654, 10_000)], [(158, 10_000)]),
     K([(654, 35_000)], [(152, 35_000)]),
     K([(689, 35_000)], [(158, 35_000)]),
     K([(158, 35_000)], [(654, 35_000)])],
    "NGD = 390.000 − 25.000 = 365.000 ₺; maliyet ile NGD’den düşük olan esas alınır. 35.000 ₺ indirim 654 Karşılık "
    "Giderleri borç, 158 Stok Değer Düşüklüğü Karşılığı alacak ile kaydedilir.", topic=ST)

T2.q("TMS 21 md. 23, 28",
    "İşletme ithal ettiği ticari malları döviz kuru 44 ₺ iken 10.000 ABD doları vadeli borçla kaydetmiştir. Mallar "
    "henüz satılmamışken borç, kurun 45 ₺ olduğu tarihte ödenmiştir; aradaki fark 10.000 ₺’dir.\n\nOluşan kur farkının "
    "muhasebeleştirilmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kur farkı kâr veya zarara gider olarak yansıtılır.",
    ["Kur farkı ticari malların maliyetine eklenir.",
     "Kur farkı mallar satılınca satış maliyetine eklenir.",
     "Kur farkı özkaynakta ayrı bir fonda izlenir.",
     "Kur farkı borçlanma maliyeti olarak aktifleştirilir."],
    "Parasal kalem olan borcun ödenmesinden doğan kur farkı oluştuğu dönemde kâr veya zarara yansıtılır (THP’de 656); "
    "parasal olmayan stok işlem tarihi kuruyla kalır, maliyetine eklenmez.", topic=ST, zorluk="hard")

T2.q(f"{R}: 268, 730",
    "Üretim işletmesi dört yıl önce 1.000.000 ₺’ye satın aldığı ve 10 yıl süreyle kullanma hakkına sahip olduğu bir "
    "üretim patentini eşit tutarlarla itfa etmektedir. Patent sadece fabrikadaki üretim sürecinde kullanılmaktadır ve "
    "işletme 7/A seçeneğini uygulamaktadır.\n\nYıl sonu itfa kaydı aşağıdakilerden hangisidir?",
    K([(730, 100_000)], [(268, 100_000)]),
    [K([(770, 100_000)], [(268, 100_000)]),
     K([(730, 100_000)], [(260, 100_000)]),
     K([(730, 250_000)], [(268, 250_000)]),
     K([(268, 100_000)], [(730, 100_000)])],
    "Yıllık itfa payı 1.000.000 / 10 = 100.000 ₺’dir. Patent üretimde kullanıldığından pay 730 Genel Üretim Giderleri "
    "hesabına borç, 268 Birikmiş Amortismanlar hesabına alacak yazılır.", topic=DS)

rs2 = reeskont(44_000, 60, 60)
T2.q("VUK md. 285; THP 322, 647",
    "Yıl sonunda işletmenin bir satıcıya verdiği ve vadesine 60 gün kalan 44.000 ₺ nominal değerli bir borç senedi "
    "bulunmaktadır. İşletme borç senetlerini iç iskonto yöntemiyle ve yıllık %60 oranla reeskonta tabi "
    "tutmaktadır.\n\nVergi Usul Kanunu’ndaki reeskont esaslarına göre yıl sonu kaydı aşağıdakilerden hangisidir?",
    K([(322, rs2)], [(647, rs2)]),
    [K([(647, rs2)], [(322, rs2)]),
     K([(322, 4_400)], [(647, 4_400)]),
     K([(657, rs2)], [(322, rs2)]),
     K([(321, rs2)], [(647, rs2)])],
    f"İç iskonto: 44.000 × 60 × 60 / (36.000 + 60 × 60) = {tl(rs2)} ₺. Borcun bugünkü değere indirilmesi gelir doğurur: "
    "322 Borç Senetleri Reeskontu borç, 647 Reeskont Faiz Gelirleri alacak. Dış iskonto 4.400 ₺ verirdi.", topic=DS)

T2.q(f"{R}: 380, 649",
    "Depo kiraya veren işletme 1 Aralık’ta kiracıdan üç aylık kira bedeli olarak 45.000 ₺’yi peşin tahsil etmiş ve "
    "tamamını 380 Gelecek Aylara Ait Gelirler hesabına kaydetmiştir. Kiralama esas faaliyet konusu dışındadır.\n\n"
    "Dönem sonu kaydı için aşağıdakilerden hangisi doğrudur?",
    T(649, "alacak", 15_000),
    [T(380, "borç", 45_000), T(380, "alacak", 15_000), T(600, "alacak", 15_000), T(181, "borç", 15_000)],
    "Aralık ayına ait kira 45.000 / 3 = 15.000 ₺ cari dönemin gelirdir: 380 borç, 649 Diğer Olağan Gelir ve Kârlar "
    "alacak. Kalan 30.000 ₺ izleyen yılın geliri olarak 380’de kalır.", topic=DS)

T2.q("VUK md. 323; THP 129, 654",
    "Yıl sonunda işletmenin dava safhasındaki iki alacağı vardır: A müşterisinden 90.000 ₺ (teminatsız) ve B "
    "müşterisinden 50.000 ₺ (30.000 ₺’lik kısmı ipotekle teminatlı). Bu alacaklar için daha önce karşılık "
    "ayrılmamıştır.\n\nDönem sonu karşılık kaydı için aşağıdakilerden hangisi doğrudur?",
    T(129, "alacak", 110_000),
    [T(129, "alacak", 140_000), T(129, "alacak", 90_000), T(654, "alacak", 110_000), T(128, "alacak", 110_000)],
    "Karşılık alacakların teminatsız kısmı için ayrılır: A için 90.000 ₺, B için 50.000 − 30.000 = 20.000 ₺; toplam "
    "110.000 ₺. 654 Karşılık Giderleri borç, 129 Şüpheli Ticari Alacaklar Karşılığı alacak yazılır.", topic=DS,
    zorluk="hard")

T2.q(f"{R}: 190, 191, 391",
    "Önceki aydan 190 Devreden KDV hesabına 40.000 ₺ aktarılmıştır. Bu ay sonunda 391 Hesaplanan KDV hesabının bakiyesi "
    "90.000 ₺, 191 İndirilecek KDV hesabının bakiyesi 70.000 ₺’dir.\n\nAy sonu mahsup kaydı aşağıdakilerden "
    "hangisidir?",
    K([(391, 90_000)], [(191, 70_000), (190, 20_000)]),
    [K([(391, 90_000)], [(191, 70_000), (360, 20_000)]),
     K([(391, 90_000), (190, 20_000)], [(191, 70_000), (360, 40_000)]),
     K([(391, 90_000)], [(191, 50_000), (190, 40_000)]),
     K([(391, 90_000), (360, 20_000)], [(191, 70_000), (190, 40_000)])],
    "Hesaplanan KDV (90.000 ₺) önce bu ayın indirilecek KDV’siyle (70.000 ₺), kalan 20.000 ₺ devreden KDV’den mahsup "
    "edilir; ödenecek KDV doğmaz ve 190’da 20.000 ₺ gelecek aya devreder.", topic=DS, zorluk="hard")

T2.q("TMS 37 md. 66-69",
    "İşletmenin bir müşteriyle yaptığı ve iptal edilemeyen sözleşmeye göre teslim edeceği ürünlerin üretim maliyeti "
    "900.000 ₺’ye yükselmiş, sözleşme bedeli ise 750.000 ₺’de kalmıştır. Sözleşmeden cayılması hâlinde ödenecek "
    "tazminat 200.000 ₺’dir.\n\nBu sözleşme için ayrılacak karşılık ile ilgili aşağıdakilerden hangisi doğrudur?",
    "150.000 ₺ karşılık ayrılır.",
    ["Cayma tazminatı kadar 200.000 ₺ karşılık ayrılır.",
     "Kayıp ve tazminat toplamı 350.000 ₺ karşılık ayrılır.",
     "Karşılık ayrılmaz, zarar teslimde kaydedilir.",
     "Sözleşme maliyeti kadar 900.000 ₺ karşılık ayrılır."],
    "Ekonomik açıdan dezavantajlı sözleşmede karşılık, sözleşmeden çıkmanın en düşük net maliyetiyle ölçülür: ifa "
    "hâlinde kayıp 900.000 − 750.000 = 150.000 ₺, cayma tazminatı 200.000 ₺; düşük olan 150.000 ₺ karşılık ayrılır.",
    topic=TF, zorluk="hard")

T2.q("TMS 40 md. 35",
    "Gerçeğe uygun değer modelini uygulayan işletmenin kiraya verdiği bir alışveriş merkezinin önceki yıl sonu değeri "
    "18.000.000 ₺’dir. Bu yıl sonunda bölgedeki talep düşüşü nedeniyle gerçeğe uygun değeri 16.500.000 ₺’ye "
    "gerilemiştir.\n\nBu değer değişikliği ile ilgili aşağıdakilerden hangisi doğrudur?",
    "1.500.000 ₺ azalış kâr veya zarara yansıtılır.",
    ["1.500.000 ₺ azalış özkaynaktaki yeniden değerleme fonundan düşülür.",
     "Azalış kaydedilmez, varlık önceki değerde bırakılır.",
     "Azalış amortisman olarak kaydedilir.",
     "Azalış dipnotta açıklanır, satışta dikkate alınır."],
    "Yatırım amaçlı gayrimenkulde gerçeğe uygun değer modelinde değer azalışları da artışlar gibi oluştuğu dönemde kâr "
    "veya zarara yansıtılır; özkaynakta yeniden değerleme fonu kullanılmaz.", topic=TF)

T2.q("TMS 36 md. 117-119",
    "Geçen yıl değer düşüklüğü kaydedilen bir makinenin bu yıl sonundaki defter değeri 300.000 ₺’dir. Değer düşüklüğü "
    "hiç kaydedilmeseydi makinenin bugünkü defter değeri 380.000 ₺ olacaktı. Koşulların düzelmesiyle geri kazanılabilir "
    "tutar 420.000 ₺’ye yükselmiştir.\n\nTMS 36’ya göre değer düşüklüğünün iptali ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "80.000 ₺ iptal edilir, makine 380.000 ₺ olur.",
    ["120.000 ₺ iptal edilir, makine 420.000 ₺ olur.",
     "Değer düşüklüğü iptal edilemez.",
     "40.000 ₺ iptal edilir, makine 340.000 ₺ olur.",
     "120.000 ₺ iptal edilir, fark özkaynağa alınır."],
    "İptal sonrası defter değeri, geçmişte değer düşüklüğü kaydedilmeseydi oluşacak defter değerini (380.000 ₺) aşamaz. "
    "Bu nedenle iptal 380.000 − 300.000 = 80.000 ₺ ile sınırlıdır ve kâr veya zarara yansıtılır.", topic=TF, zorluk="hard")

T2.q("MSUGT: tutarlılık",
    "İşletme makine ve teçhizatını beş yıldır eşit tutarlı yöntemle amortismana tabi tutmaktadır. Bu yıl kârı düşük "
    "çıkacağı için yönetim, hiçbir teknik gerekçe olmaksızın amortisman yöntemini sadece bu yıl için değiştirip gelecek "
    "yıl yeniden eşit tutarlıya dönmek istemektedir.\n\nBu uygulama aşağıdaki temel kavramlardan hangisine aykırıdır?",
    "Tutarlılık",
    ["Dönemsellik", "İhtiyatlılık", "Parayla ölçülme", "Sosyal sorumluluk"],
    "Tutarlılık kavramı muhasebe politikalarının dönemden döneme aynı uygulanmasını gerektirir; kârı yönetmek amacıyla "
    "gerekçesiz ve geçici yöntem değişikliği bu kavrama aykırıdır.", topic=TK, zorluk="easy")

# =============================================================================================== TEST 3
T3.q(f"{R}: 128, 320",
    "İşletme bir müşterisinden aldığı 25.000 ₺’lik çeki satıcısına olan borcu karşılığında ciro etmiştir. Satıcı çeki "
    "bankaya ibraz ettiğinde çekin karşılıksız çıktığı anlaşılmış, satıcı çeki işletmeye iade ederek alacağını yeniden "
    "talep etmiştir; işletme müşterisi hakkında takip başlatacaktır.\n\nÇekin iadesine ilişkin günlük defter kaydı "
    "aşağıdakilerden hangisidir?",
    K([(128, 25_000)], [(320, 25_000)]),
    [K([(101, 25_000)], [(320, 25_000)]),
     K([(320, 25_000)], [(128, 25_000)]),
     K([(128, 25_000)], [(101, 25_000)]),
     K([(689, 25_000)], [(320, 25_000)])],
    "Ciroyla kapanan satıcı borcu yeniden doğar (320 alacak 25.000 ₺). Karşılıksız çek nedeniyle müşteriden olan alacak "
    "takibe alınacağından 128 Şüpheli Ticari Alacaklar hesabına borç yazılır.", zorluk="hard")

T3.q(f"{R}: 102, 112, 642",
    "İşletme üç ay önce 92.000 ₺’ye satın aldığı ve kısa vadeli yatırım olarak elde tuttuğu 100.000 ₺ nominal değerli "
    "hazine bonosunu vadesinde itfa ettirmiş, nominal bedel işletmenin banka hesabına geçmiştir. Dönem içinde faiz "
    f"tahakkuku yapılmamış, vergi kesintisi bu soruda dikkate alınmayacaktır.\n\n{DOGRU}",
    T(642, "alacak", 8_000),
    [T(645, "alacak", 8_000), T(112, "alacak", 100_000), T(111, "alacak", 92_000), T(642, "alacak", 100_000)],
    "Bono alış maliyetiyle 112 Kamu Kesimi Tahvil, Senet ve Bonoları hesabında izlenir; itfada nominal değer ile alış "
    "bedeli arasındaki 8.000 ₺ faiz niteliğindedir ve 642 Faiz Gelirleri hesabına alacak yazılır.")

T3.q(f"{R}: 102, 126",
    "Kira sözleşmesi sona eren işletmenin taşındığı ofis için başlangıçta verdiği 40.000 ₺ depozitonun, mal sahibince "
    "yapılan hasar tespitinde kusur bulunmadığından tamamı işletmenin banka hesabına iade edilmiştir.\n\n"
    f"{DOGRU}",
    T(126, "alacak", 40_000),
    [T(326, "borç", 40_000), T(649, "alacak", 40_000), T(126, "borç", 40_000), T(180, "alacak", 40_000)],
    "Verilen depozito 126 Verilen Depozito ve Teminatlar hesabında alacak olarak izlenmişti; iadesiyle 102 borç, 126 "
    "alacak 40.000 ₺ yazılarak kapatılır. 326 işletmenin aldığı teminatları izler.", zorluk="easy")

T3.q(f"{R}: 195, 770, 100",
    "Yönetim bölümündeki bir çalışana şehir dışı görev için 5.000 ₺ iş avansı verilmiştir. Çalışan görev dönüşünde "
    "toplam 6.200 ₺ tutarında KDV’siz konaklama ve ulaşım belgesi teslim etmiş, aşan 1.200 ₺ kendisine kasadan "
    f"ödenmiştir.\n\n{KAYIT}",
    K([(770, 6_200)], [(195, 5_000), (100, 1_200)]),
    [K([(770, 5_000)], [(195, 5_000)]),
     K([(770, 6_200)], [(196, 5_000), (100, 1_200)]),
     K([(195, 5_000), (100, 1_200)], [(770, 6_200)]),
     K([(760, 6_200)], [(195, 5_000), (100, 1_200)])],
    "Belgelenen 6.200 ₺ idari gider 770’e borç yazılır; iş avansı 195 İş Avansları hesabına 5.000 ₺ alacak yazılarak "
    "kapatılır, çalışana ödenen fark 1.200 ₺ 100 Kasa hesabından çıkar.")

T3.q(f"{R}: 102, 611, 391, 120",
    "İşletme vadesinden önce ödeme yapan bir müşterisine, 60.000 ₺ olan alacak üzerinden 1.000 ₺ + %20 KDV tutarında "
    "erken ödeme iskontosu tanımış ve iskonto faturası düzenlemiştir. Müşteri kalan tutarı banka havalesiyle "
    f"ödemiştir.\n\n{KAYIT}",
    K([(102, 58_800), (611, 1_000), (391, 200)], [(120, 60_000)]),
    [K([(102, 58_800), (780, 1_200)], [(120, 60_000)]),
     K([(102, 58_800), (611, 1_000), (191, 200)], [(120, 60_000)]),
     K([(102, 58_800), (610, 1_000), (391, 200)], [(120, 60_000)]),
     K([(102, 60_000)], [(120, 58_800), (611, 1_200)])],
    "Satıcı açısından tanınan iskonto 611 Satış İskontoları hesabına borç yazılır; satışta hesaplanan KDV 200 ₺ "
    "azalır (391 borç). Bankaya 58.800 ₺ geçer, müşteri alacağı 60.000 ₺ kapanır.", zorluk="hard")

T3.q(f"{R}: 102, 136",
    "Deposundaki mallar sel nedeniyle zarar gören işletme, sigorta şirketinin kabul ettiği 180.000 ₺ tazminatı alacak "
    "olarak 136 Diğer Çeşitli Alacaklar hesabına kaydetmişti. Sigorta şirketi bu ay tazminatın tamamını işletmenin "
    f"banka hesabına ödemiştir.\n\n{DOGRU}",
    T(136, "alacak", 180_000),
    [T(679, "alacak", 180_000), T(153, "borç", 180_000), T(120, "alacak", 180_000), T(689, "alacak", 180_000)],
    "Tazminat hak ediş tarihinde 136 hesabına alacak olarak kaydedilmiştir; tahsilatta 102 Bankalar borç, 136 alacak "
    "180.000 ₺ yazılarak alacak kapatılır. Gelir etkisi hasar kaydında dikkate alınmıştır.", zorluk="easy")

brut_f, st_f = 100_000, 10_000
T3.q(f"{R}: 780, 360, 102",
    f"Tahvil ihraç eden anonim şirket bu ay tahvil sahiplerine {tl(brut_f)} ₺ brüt kupon faizi ödemiştir. Şirket, faiz "
    f"üzerinden %10 oranında gelir vergisi kesintisi ({tl(st_f)} ₺) yapmış ve kalan tutarı yatırımcılara aktarmıştır; "
    f"faiz için daha önce tahakkuk kaydı yapılmamıştır.\n\n{KAYIT}",
    K([(780, brut_f)], [(360, st_f), (102, brut_f - st_f)]),
    [K([(780, brut_f - st_f)], [(102, brut_f - st_f)]),
     K([(780, brut_f), (193, st_f)], [(102, brut_f + st_f)]),
     K([(405, brut_f)], [(360, st_f), (102, brut_f - st_f)]),
     K([(780, brut_f)], [(193, st_f), (102, brut_f - st_f)])],
    f"Faiz gideri brüt tutarla ({tl(brut_f)} ₺) 780 Finansman Giderleri hesabına borç yazılır. Şirket vergi sorumlusu "
    f"olarak kestiği {tl(st_f)} ₺’yi 360 Ödenecek Vergi ve Fonlar hesabına, ödediği {tl(brut_f - st_f)} ₺’yi 102’ye "
    "alacak yazar.")

T3.q(f"{R}: 340, 102",
    "Bir müşteri ay başında verdiği sipariş için 35.000 ₺ avans ödemiş, işletme bunu 340 hesabına kaydetmiştir. Müşteri "
    "sipariş ettiği ürünlerin üretimi başlamadan siparişini iptal etmiş, işletme de sözleşme gereği avansın tamamını "
    f"banka havalesiyle iade etmiştir.\n\n{DOGRU}",
    T(340, "borç", 35_000),
    [T(159, "alacak", 35_000), T(600, "borç", 35_000), T(340, "alacak", 35_000), T(120, "borç", 35_000)],
    "Alınan avans işletmenin yükümlülüğüdür; iade edildiğinde 340 Alınan Sipariş Avansları borçlandırılarak kapatılır ve "
    "102 Bankalar 35.000 ₺ alacaklandırılır. Satış gerçekleşmediğinden gelir hesabı kullanılmaz.", zorluk="easy")

T3.q("TMS 2 md. 25",
    "Fiyatların sürekli yükseldiği bir yılda işletmenin dönem başı stoku 500 adet × 10 ₺’dir; yıl içinde 1.000 adet × 12 ₺ "
    "ve 500 adet × 16 ₺ alış yapılmış, 1.400 adet satılmıştır. İşletme FIFO ile dönemsel ağırlıklı ortalama arasındaki "
    "farkı görmek istemektedir.\n\nTMS 2 Stoklar’a göre dönem sonu stoku ile ilgili aşağıdakilerden hangisi doğrudur?",
    "FIFO’da 9.200 ₺, ağırlıklı ortalamada 7.500 ₺’dir.",
    ["FIFO’da 7.500 ₺, ağırlıklı ortalamada 9.200 ₺’dir.",
     "Her iki yöntemde de 7.500 ₺’dir.",
     "FIFO’da 9.600 ₺, ağırlıklı ortalamada 7.200 ₺’dir.",
     "FIFO’da 9.200 ₺, ağırlıklı ortalamada 8.400 ₺’dir."],
    "Mal mevcudu 2.000 adet, 25.000 ₺; kalan 600 adet. FIFO’da kalan son alışlardan gelir: 500 × 16 + 100 × 12 = "
    "9.200 ₺. Ortalama 25.000 / 2.000 = 12,5 ₺; 600 × 12,5 = 7.500 ₺.", topic=ST, zorluk="hard")

T3.q("TMS 2; eşdeğer birim",
    "Tek aşamalı üretim yapan işletmede dönem başı yarı mamul yoktur. Dönem içinde 1.000 birim üretime başlanmış, "
    "800 birim tamamlanmış, 200 birim %50 tamamlanma düzeyinde yarı mamul olarak kalmıştır. Tüm üretim maliyetleri "
    "üretim boyunca eşit olarak oluşmakta olup toplam 450.000 ₺’dir.\n\nMaliyet dağıtımı ile ilgili aşağıdakilerden "
    "hangisi doğrudur?",
    "Tamamlanan 400.000 ₺, yarı mamul 50.000 ₺’dir.",
    ["Tamamlanan 360.000 ₺, yarı mamul 90.000 ₺’dir.",
     "Tamamlanan 450.000 ₺, yarı mamul yoktur.",
     "Tamamlanan 375.000 ₺, yarı mamul 75.000 ₺’dir.",
     "Tamamlanan 405.000 ₺, yarı mamul 45.000 ₺’dir."],
    "Eşdeğer birim = 800 + 200 × %50 = 900; birim maliyet 450.000 / 900 = 500 ₺. Tamamlanan 800 × 500 = 400.000 ₺, "
    "yarı mamul 100 × 500 = 50.000 ₺.", topic=ST, zorluk="hard")

T3.q(f"{R}: 397, 191, 320",
    "Yıl sonu sayımında bir üründe 10.000 ₺ tutarında fazla bulunmuş ve 397 hesabına alınmıştır. İnceleme sonucunda "
    "fazlalığın, mal teslim alındığı hâlde satıcının 10.000 ₺ + %20 KDV tutarlı faturasının kayda alınmamasından "
    f"kaynaklandığı anlaşılmıştır.\n\n{KAYIT}",
    K([(397, 10_000), (191, 2_000)], [(320, 12_000)]),
    [K([(397, 10_000)], [(679, 10_000)]),
     K([(153, 10_000), (191, 2_000)], [(320, 12_000)]),
     K([(397, 12_000)], [(320, 12_000)]),
     K([(397, 10_000), (191, 2_000)], [(102, 12_000)])],
    "Mal sayımda stoka alınırken 153 borç, 397 alacak yazılmıştı; bu nedenle alış kaydında 153 yerine 397 kapatılır. "
    "KDV 191’e borç, satıcı borcu 320’ye 12.000 ₺ alacak yazılır.", topic=ST, zorluk="hard")

T3.q(f"{R}: 180, 760",
    "İşletme 1 Kasım’da altı ay sürecek bir açık hava reklam kampanyası için 72.000 ₺ ödemiş ve tamamını 180 Gelecek "
    "Aylara Ait Giderler hesabına kaydetmiştir. Kasım payı ay sonunda gidere aktarılmış, aralık payı henüz "
    "aktarılmamıştır.\n\nAralık sonunda yapılacak kayıt aşağıdakilerden hangisidir?",
    K([(760, 12_000)], [(180, 12_000)]),
    [K([(760, 24_000)], [(180, 24_000)]),
     K([(770, 12_000)], [(180, 12_000)]),
     K([(180, 12_000)], [(760, 12_000)]),
     K([(760, 12_000)], [(381, 12_000)])],
    "Aylık pay 72.000 / 6 = 12.000 ₺’dir. Aralık payı reklam gideri olarak 760 Pazarlama, Satış ve Dağıtım Giderleri "
    "hesabına borç, 180 hesabına alacak yazılır; kasım payı zaten aktarılmıştır.", topic=DS, zorluk="easy")

fz3 = 400_000 * 45 * 2 // (100 * 12)
T3.q(f"{R}: 181, 642",
    "İşletme 1 Kasım’da 400.000 ₺ nominal değerli, yıllık %45 faizli ve faizi 30 Nisan’da ödenecek bir özel sektör "
    "tahvili satın almıştır. Tahvil kısa vadeli yatırım amacıyla elde tutulmakta, faiz basit usulle "
    f"işlemektedir.\n\nYıl sonunda yapılacak faiz tahakkuku kaydı aşağıdakilerden hangisidir?",
    K([(181, fz3)], [(642, fz3)]),
    [K([(181, fz3 * 3)], [(642, fz3 * 3)]),
     K([(102, fz3)], [(642, fz3)]),
     K([(642, fz3)], [(181, fz3)]),
     K([(181, fz3)], [(111, fz3)])],
    f"Kasım-aralık iki aylık faiz 400.000 × %45 × 2/12 = {tl(fz3)} ₺ cari dönemin gelirdir ancak henüz tahsil "
    "edilmemiştir: 181 Gelir Tahakkukları borç, 642 Faiz Gelirleri alacak.", topic=DS)

T3.q("VUK md. 322-323; THP 128, 129",
    "İşletme geçen yıl dava safhasındaki 70.000 ₺’lik alacağının tamamı için şüpheli alacak karşılığı ayırmıştır. Bu yıl "
    "mahkeme kararıyla borçlunun ödeme gücü olmadığı kesinleşmiş ve alacak değersiz hâle gelmiştir; tahsilat "
    f"yapılmamıştır.\n\n{KAYIT}",
    K([(129, 70_000)], [(128, 70_000)]),
    [K([(689, 70_000)], [(128, 70_000)]),
     K([(654, 70_000)], [(129, 70_000)]),
     K([(129, 70_000)], [(644, 70_000)]),
     K([(128, 70_000)], [(129, 70_000)])],
    "Tamamı için karşılık ayrılmış alacak değersiz hâle geldiğinde gider daha önce yazılmıştır; karşılık ile alacak "
    "birbirine kapatılır: 129 borç, 128 alacak 70.000 ₺.", topic=DS)

T3.q(f"{R}: 100, 656",
    "İşletmenin kasasında yıl sonunda 5.000 İngiliz sterlini bulunmaktadır. Dövizler kasaya 56 ₺ kurla girmiş, değerleme "
    "günü kuru 54,80 ₺ olarak açıklanmıştır. İşletme dövizleri ocak ayında bir yurt dışı fuar gideri için "
    "kullanacaktır.\n\nDönem sonu değerleme kaydı için aşağıdakilerden hangisi doğrudur?",
    T(100, "alacak", 6_000),
    [T(646, "alacak", 6_000), T(102, "alacak", 6_000), T(656, "borç", 274_000), T(100, "alacak", 274_000)],
    "Dövizlerin değeri 5.000 × 54,80 = 274.000 ₺’ye inmiştir; kayıtlı değer 280.000 ₺. 6.000 ₺ azalış 656 Kambiyo "
    "Zararları borç, 100 Kasa alacak ile kaydedilir.", topic=DS)

T3.q("KVK md. 9, 32; THP 370, 691",
    "Ticari bilanço kârı 500.000 ₺ olan şirketin kanunen kabul edilmeyen giderleri 40.000 ₺’dir. Şirketin önceki yıldan "
    "devreden ve mahsup süresi dolmamış 140.000 ₺ mali zararı bulunmaktadır; kurumlar vergisi oranı %25’tir.\n\n"
    "Kurumlar Vergisi Kanunu’na göre hesaplanan dönem sonu vergi karşılığı kaydı için aşağıdakilerden hangisi doğrudur?",
    T(370, "alacak", 100_000),
    [T(370, "alacak", 125_000), T(370, "alacak", 135_000), T(370, "alacak", 90_000), T(371, "alacak", 100_000)],
    "Mali kâr = 500.000 + 40.000 − 140.000 = 400.000 ₺; vergi 400.000 × %25 = 100.000 ₺. 691 borç, 370 Dönem Kârı Vergi "
    "ve Diğer Yasal Yükümlülük Karşılıkları hesabına alacak yazılır.", topic=DS, zorluk="hard")

T3.q("TFRS 16 md. 26",
    "Kiracı işletme bir makineyi üç yıllığına kiralamıştır; her yıl sonunda 100.000 ₺ kira ödenecektir. Kiralamadaki "
    "zımni faiz oranı yıllık %10’dur, başlangıçta peşin ödeme veya doğrudan maliyet yoktur.\n\nTFRS 16 Kiralamalar’a "
    "göre kira yükümlülüğünün ilk ölçümü ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kira yükümlülüğü yaklaşık 248.685 ₺ olarak ölçülür.",
    ["Kira yükümlülüğü 300.000 ₺ olarak ölçülür.",
     "Kira yükümlülüğü yaklaşık 272.727 ₺ olarak ölçülür.",
     "Kira yükümlülüğü 270.000 ₺ olarak ölçülür.",
     "Kira yükümlülüğü kaydedilmez, ödemeler gider yazılır."],
    "Kira yükümlülüğü ödenmemiş kira ödemelerinin zımni faiz oranıyla indirgenmiş bugünkü değeridir: 100.000 × (1/1,1 + "
    "1/1,21 + 1/1,331) ≈ 248.685 ₺.", topic=TF, zorluk="hard")

T3.q("TMS 23 md. 5, 7",
    "Bir şirketin bu yıl yaptığı yatırımlar şunlardır: tamamlanması 18 ay sürecek bir otel inşaatı, kısa sürede rutin "
    "olarak üretilen ve stoka alınan konserve ürünleri ve satın alındığı gün kullanıma hazır olan bir makine. Tümü "
    "banka kredisiyle finanse edilmiştir.\n\nBorçlanma maliyetinin aktifleştirilebileceği varlık aşağıdakilerden "
    "hangisidir?",
    "Tamamlanması 18 ay sürecek otel inşaatı",
    ["Rutin olarak üretilen konserve stokları",
     "Satın alındığında kullanıma hazır olan makine",
     "Konserve stokları ve makine",
     "Üç varlığın tamamı"],
    "Borçlanma maliyetleri, kullanıma veya satışa hazır hâle gelmesi uzun süre gerektiren özellikli varlıklar için "
    "aktifleştirilir; rutin üretilen stoklar ve alındığında hazır olan varlıklar özellikli değildir.", topic=TF,
    zorluk="easy")

T3.q("TMS 16 md. 16-22",
    "İşletme yeni genel müdürlük binası için arsa üzerinde 8.000.000 ₺ inşaat bedeli, 450.000 ₺ mimarlık ve proje "
    "ücreti, 120.000 ₺ yapı ruhsatı harcı, 300.000 ₺ şantiye güvenliği gideri ve binanın açılışı için 180.000 ₺ tören ve "
    "tanıtım gideri ödemiştir.\n\nBu harcamalardan hangisi binanın maliyetine eklenmez?",
    "Açılış töreni ve tanıtım gideri",
    ["Mimarlık ve proje ücreti", "Yapı ruhsatı harcı", "İnşaat süresince şantiye güvenliği", "Müteahhide ödenen bedel"],
    "Varlığı kullanıma hazır hâle getirmek için doğrudan katlanılan inşaat, proje, ruhsat ve şantiye giderleri maliyete "
    "girer; yeni bir tesisin açılış ve tanıtım maliyetleri ise maliyet unsuru değildir, gider yazılır.", topic=TF,
    zorluk="easy")

T3.q("Temel muhasebe eşitliği",
    "Bir limited şirketin ortağı, piyasa değeri 240.000 ₺ olan ve üzerinde 60.000 ₺ taşıt kredisi borcu bulunan hafif "
    "ticari aracını sermaye taahhüdünü karşılamak üzere şirkete devretmiş, kredi borcunu da şirket üstlenmiştir. "
    "Taahhüt daha önce kayda alınmıştır.\n\nBu işlemin şirketin temel muhasebe eşitliğine etkisi aşağıdakilerden "
    "hangisidir?",
    "Varlıklar 240.000 ₺; yabancı kaynaklar 60.000 ₺, özkaynaklar 180.000 ₺ artar.",
    ["Varlıklar ve özkaynaklar 240.000 ₺ artar, yabancı kaynaklar değişmez.",
     "Varlıklar 240.000 ₺, yabancı kaynaklar 60.000 ₺ artar, özkaynaklar değişmez.",
     "Varlıklar 180.000 ₺, özkaynaklar 180.000 ₺ artar, yabancı kaynaklar değişmez.",
     "Varlıklar 240.000 ₺; yabancı kaynaklar 240.000 ₺ artar, özkaynaklar değişmez."],
    "Taşıt 254’e 240.000 ₺ borç, üstlenilen kredi 60.000 ₺ yabancı kaynak; kalan 180.000 ₺ ile ortağın taahhüt borcu "
    "kapanır (501 alacak). 501 özkaynaktan indirilen bir hesap olduğundan azalması net özkaynağı 180.000 ₺ artırır.",
    topic=TK, zorluk="hard")

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
