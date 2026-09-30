# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi · Gider Dağıtımları — 60 soru, 2026 test biçimi.

Gerçek kitapçıklarda bu konu tablo ağırlıklıdır: genel üretim gideri dağıtım tablosu (I. ve II. dağıtım),
yükleme katsayıları, yüklenen ile gerçekleşen GÜG farkı, faaliyet tabanlı maliyetlemede faaliyet yükleme
oranları ve MSUGT'nin gider yeri tanımları sorulur.

Dayanak: MSUGT 7/A gider yerleri (esas üretim, yardımcı üretim, yardımcı hizmet); gider dağıtımının genel
kabul görmüş yöntemleri (doğrudan, basamaklı, karşılıklı/cebirsel dağıtım); faaliyet tabanlı maliyetleme.
Tutarlar builder içinde hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_gider_dagitimlari_2026.json", lesson="maliyet_muhasebesi", topic="gider_dagitimlari",
          konu_adi="Gider Dağıtımları", seed=2026093083,
          surum="MSUGT 7/A gider yerleri; gider dağıtım yöntemleri; faaliyet tabanlı maliyetleme; 30.09.2026 kontrolü")

R = "Gider dağıtımı"
RY = "MSUGT: gider yerleri"
ABC = "Faaliyet tabanlı maliyetleme"

# ------------------------------------------------------------------ gider yerleri
P.q(RY,
    "Bir tekstil fabrikasında kesim, dikim ve ütü-paketleme bölümleri doğrudan ürün üzerinde çalışmaktadır. Bakım "
    "atölyesi makinelerin onarımını, buhar kazanı üretim bölümlerine enerji sağlamakta; yemekhane ve personel bölümü ise "
    "tüm çalışanlara hizmet vermektedir.\n\nBu işletmede buhar kazanı hangi tür gider yeridir?",
    "Yardımcı üretim gider yeri",
    ["Esas üretim gider yeri", "Yardımcı hizmet gider yeri", "Satış gider yeri", "Yönetim gider yeri"],
    "Esas üretim gider yerleri doğrudan mamul üretir; yardımcı üretim gider yerleri (bakım, enerji, buhar) esas üretime "
    "teknik destek verir; yardımcı hizmet gider yerleri (yemekhane, personel, bekçilik) tüm işletmeye hizmet sunar.",
    zorluk="easy")

P.q(RY,
    "Muhasebe Sistemi Uygulama Genel Tebliği’ne göre gider yerleri esas üretim, yardımcı üretim ve yardımcı hizmet gider "
    "yerleri olarak ayrılmaktadır. Bir otomotiv yan sanayi işletmesinde pres, kaynak, boya, kalıphane ve güvenlik "
    "birimleri bulunmaktadır.\n\nBu birimlerden hangisi yardımcı hizmet gider yeridir?",
    "Güvenlik birimi",
    ["Pres (sac kesme) bölümü", "Kaynak hattı bölümü", "Boya ve kurutma bölümü", "Kalıp atölyesi (kalıphane)"],
    "Pres, kaynak ve boya doğrudan ürün üzerinde çalışan esas üretim gider yerleridir; kalıphane üretime teknik destek "
    "veren yardımcı üretim, güvenlik ise tüm işletmeye hizmet veren yardımcı hizmet gider yeridir.")

P.q(RY,
    "Gider yerleri muhasebesini yeni uygulamaya başlayan işletmenin muhasebe müdürü, gider yerlerinin kuruluş amaçlarını "
    "ve dağıtım işlemlerini yönetim kuruluna anlatmaktadır. Hazırlanan açıklamalardan biri hatalıdır.\n\nGider yerleri ile "
    "ilgili aşağıdakilerden hangisi yanlıştır?",
    "Yardımcı gider yerlerinin giderleri doğrudan mamullere yüklenir.",
    ["Giderlerin doğduğu yerde izlenmesini ve kontrolünü sağlar.",
     "Birinci dağıtımda giderler esas ve yardımcı tüm gider yerlerine paylaştırılır.",
     "İkinci dağıtımda yardımcı gider yerlerinin giderleri dağıtılır.",
     "Mamullere yükleme esas üretim gider yerlerinden yapılır."],
    "Yardımcı gider yerlerinin giderleri doğrudan mamullere yüklenmez; ikinci dağıtımla esas üretim gider yerlerine "
    "aktarılır, mamullere yükleme esas üretim gider yerlerinden yükleme oranlarıyla yapılır.", zorluk="hard")

# ------------------------------------------------------------------ birinci dağıtım
m2 = {"Kesim": 400, "Montaj": 300, "Bakım": 200, "Yemekhane": 100}
kira = 120_000
P.sayisal(R,
    "Bir işletmenin aylık fabrika kirası 120.000 ₺ olup birinci dağıtımda gider yerlerinin kullandığı alana göre "
    "dağıtılmaktadır. Gider yerlerinin kullandığı alanlar şöyledir:\n\n| Gider yeri | Alan (m²) |\n|---|---|\n"
    "| Kesim | 400 |\n| Montaj | 300 |\n| Bakım | 200 |\n| Yemekhane | 100 |\n\nKesim bölümüne düşen kira payı kaç ₺’dir?",
    tl(kira * 400 // 1_000), secenekler(48_000, 30_000, 40_000, 68_571, 36_000),
    "Dağıtım oranı 120.000 / 1.000 m² = 120 ₺/m²; Kesim 400 × 120 = 48.000 ₺. Montaj 36.000, Bakım 24.000, Yemekhane "
    "12.000 ₺ alır.", zorluk="easy")

P.q(R,
    "Bir fabrikada birinci dağıtım yapılırken ortak giderler için dağıtım anahtarları seçilmektedir. Giderler arasında "
    "fabrika binası kirası, elektrik (makine gücü) gideri, personel yemek gideri ve bina sigortası bulunmaktadır.\n\n"
    "Aşağıdaki gider-dağıtım anahtarı eşleştirmelerinden hangisi uygun değildir?",
    "Yemek gideri – makine gücü (kW)",
    ["Fabrika kirası – kullanılan alan (m²)", "Elektrik gideri – makine gücü veya kWh",
     "Bina sigortası – bina alanı veya değeri", "Aydınlatma gideri – aydınlatılan alan"],
    "Dağıtım anahtarı gider ile gider yeri arasındaki neden-sonuç ilişkisini yansıtmalıdır. Yemek gideri çalışan sayısına "
    "göre dağıtılmalıdır; makine gücü bu giderle ilişkili değildir.", zorluk="hard")

P.q(R,
    "Birinci dağıtım aşamasındaki bir işletmede dönem içinde oluşan genel üretim giderleri gider yerlerine "
    "paylaştırılacaktır. Bazı giderler (bakım ustasının ücreti gibi) tek bir gider yerine aittir, bazıları (fabrika kirası "
    "gibi) birden fazla gider yerince paylaşılmaktadır.\n\nBirinci dağıtımla ilgili aşağıdakilerden hangisi doğrudur?",
    "Direkt giderler doğrudan, ortakları anahtarla dağıtılır.",
    ["Tüm giderler sadece esas üretim gider yerlerine dağıtılır.",
     "Giderler mamullere doğrudan yüklenir.",
     "Yardımcı gider yerlerinin giderleri esas üretime aktarılır.",
     "Ortak giderler eşit olarak paylaştırılır."],
    "Birinci dağıtımda GÜG tüm gider yerlerine (esas ve yardımcı) dağıtılır: tek gider yerine ait olanlar doğrudan o yere "
    "yazılır, ortak giderler uygun dağıtım anahtarlarıyla paylaştırılır. Yardımcıların esas üretime aktarılması ikinci "
    "dağıtımdır.")

# ------------------------------------------------------------------ ikinci dağıtım: basamaklı/doğrudan
ilk = {"Kesim": 400_000, "Montaj": 300_000, "Bakım": 120_000, "Yemekhane": 80_000}
tbl = ("| Gider yeri | Birinci dağıtım sonrası (₺) | Personel sayısı | Bakım saati |\n|---|---|---|---|\n"
       "| Kesim (esas) | 400.000 | 30 | 600 |\n| Montaj (esas) | 300.000 | 50 | 400 |\n"
       "| Bakım (yardımcı üretim) | 120.000 | 20 | — |\n| Yemekhane (yardımcı hizmet) | 80.000 | — | — |")
yb = 80_000
bb = 120_000 + yb * 20 // 100
k_bas = 400_000 + yb * 30 // 100 + bb * 60 // 100
m_bas = 300_000 + yb * 50 // 100 + bb * 40 // 100
P.sayisal(R,
    "Bir işletmenin birinci dağıtım sonrası genel üretim gideri dağıtım tablosu verileri şöyledir:\n\n" + tbl +
    "\n\nİkinci dağıtımda basamaklı yöntem uygulanmakta; önce yemekhane giderleri personel sayısına göre, ardından bakım "
    "giderleri bakım saatine göre dağıtılmaktadır. İkinci dağıtım sonunda Kesim bölümünün toplam gideri kaç ₺’dir?",
    tl(k_bas), secenekler(k_bas, 502_000, 472_000, 400_000, 544_000),
    f"Yemekhane 80.000 ₺ personel sayısına göre: Kesim 24.000, Montaj 40.000, Bakım 16.000 ₺. Bakım {tl(bb)} ₺ bakım "
    f"saatine göre: Kesim %60 → {tl(bb * 60 // 100)} ₺. Kesim toplamı 400.000 + 24.000 + {tl(bb * 60 // 100)} = "
    f"{tl(k_bas)} ₺.", zorluk="hard")

P.q(R,
    "Aynı işletmenin verileri aşağıdadır:\n\n" + tbl +
    "\n\nİşletme ikinci dağıtımda bu kez doğrudan dağıtım yöntemini kullanmak, yani yardımcı gider yerleri arasında "
    "karşılıklı hizmeti dikkate almadan giderleri sadece esas üretim gider yerlerine dağıtmak istemektedir. Kesim ve Montaj "
    "bölümlerinin toplam giderleri sırasıyla kaç ₺’dir?",
    "502.000; 398.000",
    [f"{tl(k_bas)}; {tl(m_bas)}", "472.000; 428.000", "400.000; 300.000", "520.000; 380.000"],
    "Doğrudan dağıtımda yemekhane sadece esas bölümlere personel oranına göre (30:50) dağıtılır: Kesim 30.000, Montaj "
    "50.000 ₺. Bakım 120.000 ₺ bakım saatine göre: Kesim 72.000, Montaj 48.000 ₺. Kesim 502.000, Montaj 398.000 ₺.",
    zorluk="hard")

P.q(R,
    "İkinci dağıtımda yardımcı gider yerlerinin birbirlerine verdikleri hizmetlerin ölçülüp ölçülmeyeceği "
    "tartışılmaktadır. Bir yöntemde yardımcı gider yerleri belirli bir sırayla dağıtılmakta ve dağıtılan bir gider yerine "
    "bir daha pay verilmemektedir.\n\nTanımlanan dağıtım yöntemi aşağıdakilerden hangisidir?",
    "Basamaklı (kademeli) dağıtım",
    ["Doğrudan dağıtım", "Karşılıklı (cebirsel) dağıtım", "Birinci dağıtım", "Faaliyet tabanlı dağıtım"],
    "Basamaklı dağıtımda yardımcı gider yerleri genellikle en çok hizmet verenden başlanarak sırayla dağıtılır ve "
    "dağıtılmış gider yerine tekrar pay verilmez; doğrudan dağıtım karşılıklı hizmetleri tamamen yok sayar, karşılıklı "
    "dağıtım ise denklemlerle tümünü dikkate alır.", zorluk="easy")

# karşılıklı dağıtım
P.q(R,
    "Bir fabrikada iki yardımcı gider yeri vardır: Bakım (birinci dağıtım sonrası 120.000 ₺) ve Enerji (72.000 ₺). "
    "Bakım hizmetlerinin %20’si Enerjiye, %50’si Kesime, %30’u Montaja; Enerji hizmetlerinin %20’si Bakıma, %40’ı Kesime, "
    "%40’ı Montaja verilmektedir.\n\nKarşılıklı (cebirsel) dağıtım yöntemine göre Bakım ve Enerjinin dağıtılacak toplam "
    "giderleri sırasıyla kaç ₺’dir?",
    "140.000; 100.000",
    ["120.000; 72.000", "134.400; 96.000", "144.000; 96.000", "134.400; 100.000"],
    "B = 120.000 + 0,2E ve E = 72.000 + 0,2B denklemleri birlikte çözülür: E = (72.000 + 24.000) / 0,96 = 100.000 ₺, "
    "B = 120.000 + 20.000 = 140.000 ₺. Bu tutarlar hizmet oranlarına göre esas bölümlere dağıtılır.", zorluk="hard")

P.sayisal(R,
    "Karşılıklı dağıtım uygulayan işletmede denklemlerin çözümüyle Bakımın dağıtılacak toplam gideri 140.000 ₺, Enerjinin "
    "100.000 ₺ bulunmuştur. Bakım hizmetlerinin %50’si, Enerji hizmetlerinin %40’ı Kesim bölümüne verilmektedir; "
    "Kesimin birinci dağıtım sonrası gideri 350.000 ₺’dir.\n\nİkinci dağıtım sonunda Kesim bölümünün toplam gideri kaç "
    "₺’dir?",
    tl(350_000 + 70_000 + 40_000), secenekler(460_000, 446_000, 410_000, 390_000, 590_000),
    "Kesim, Bakımdan 140.000 × %50 = 70.000 ₺, Enerjiden 100.000 × %40 = 40.000 ₺ pay alır: 350.000 + 70.000 + 40.000 = "
    "460.000 ₺.")

# ------------------------------------------------------------------ yükleme oranları
P.sayisal("Genel üretim gideri yükleme oranı",
    "İkinci dağıtım sonunda Kesim bölümünde 505.600 ₺ genel üretim gideri toplanmıştır. Kesim bölümünde ay içinde 6.320 "
    "makine saati çalışılmış olup bölüm giderleri mamullere makine saatine göre yüklenmektedir.\n\nKesim bölümünün GÜG "
    "yükleme katsayısı makine saati başına kaç ₺’dir?",
    tl(505_600 // 6_320), secenekler(80, 70, 90, 64, 100),
    "Yükleme katsayısı = bölümün ikinci dağıtım sonrası gideri / dağıtım ölçüsü = 505.600 / 6.320 = 80 ₺/makine saati.",
    zorluk="easy")

P.q("Genel üretim gideri yükleme oranı",
    "Bir işletmede Kesim bölümü GÜG’ü 80 ₺/makine saati, Montaj bölümü 50 ₺/direkt işçilik saati oranıyla yüklemektedir. "
    "A siparişi Kesimde 120 makine saati ve 20 işçilik saati, Montajda 10 makine saati ve 90 işçilik saati "
    "kullanmıştır.\n\nA siparişine yüklenecek toplam GÜG kaç ₺’dir?",
    "14.100 ₺",
    ["10.400 ₺", "11.600 ₺", "16.000 ₺", "17.500 ₺"],
    "Her bölüm kendi ölçüsüyle yükler: Kesim 120 × 80 = 9.600 ₺, Montaj 90 × 50 = 4.500 ₺; toplam 14.100 ₺. Kesimdeki "
    "işçilik saati ve Montajdaki makine saati bu yüklemede kullanılmaz.", zorluk="hard")

P.q("Genel üretim gideri yükleme oranı",
    "Bir işletme iki üretim bölümüne sahiptir: A bölümü makine yoğun, B bölümü işçilik yoğundur ve ürünler bölümlerden "
    "farklı oranlarda geçmektedir. Yönetim fabrika genelinde tek bir GÜG yükleme oranı kullanmayı düşünmektedir.\n\nBu "
    "durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Bölüm bazında oranlar daha doğru maliyet sağlar.",
    ["Tek oran bu durumda en doğru sonucu verir.",
     "Oran seçimi mamul maliyetini etkilemez.",
     "Tek oran sadece hizmet işletmelerinde kullanılabilir.",
     "Bölüm oranları sadece standart maliyette kullanılır."],
    "Bölümlerin gider yapıları ve ürünlerin bölümleri kullanma oranları farklıysa tek fabrika oranı maliyetleri "
    "çarpıtır; her bölümün kendi gider sürücüsüne göre hesaplanan oranlar daha doğru mamul maliyeti verir.")

# ------------------------------------------------------------------ fazla/eksik yükleme (tablo)
ykd, yks, grd, grs = 482_500, 360_000, 461_300, 367_400
P.q("Yüklenen ve gerçekleşen GÜG",
    "Bir mobilya işletmesinde nisan ayında mamullere yüklenen ve gerçekleşen genel üretim giderleri şöyledir:\n\n"
    "| | Değişken GÜG (₺) | Sabit GÜG (₺) | Toplam (₺) |\n|---|---|---|---|\n"
    f"| Yüklenen | {tl(ykd)} | {tl(yks)} | {tl(ykd + yks)} |\n| Gerçekleşen | {tl(grd)} | {tl(grs)} | {tl(grd + grs)} |\n\n"
    "Değişken, sabit ve toplam GÜG’de fazla (+) veya eksik (−) yükleme sırasıyla aşağıdakilerden hangisidir?",
    f"Fazla {tl(ykd - grd)}; eksik {tl(grs - yks)}; fazla {tl(ykd + yks - grd - grs)}",
    [f"Eksik {tl(ykd - grd)}; fazla {tl(grs - yks)}; eksik {tl(ykd + yks - grd - grs)}",
     f"Fazla {tl(ykd - grd)}; fazla {tl(grs - yks)}; fazla {tl(ykd - grd + grs - yks)}",
     f"Eksik {tl(ykd - grd)}; eksik {tl(grs - yks)}; eksik {tl(ykd + yks - grd - grs)}",
     f"Fazla {tl(grd)}; eksik {tl(grs)}; fazla {tl(grd + grs)}"],
    f"Yüklenen gerçekleşenden büyükse fazla yükleme vardır: değişkende {tl(ykd)} − {tl(grd)} = {tl(ykd - grd)} ₺ fazla; "
    f"sabitte {tl(grs)} − {tl(yks)} = {tl(grs - yks)} ₺ eksik; toplamda {tl(ykd + yks - grd - grs)} ₺ fazla yükleme.",
    zorluk="hard")

P.sayisal("Yüklenen ve gerçekleşen GÜG",
    "Bir işletme GÜG’ü direkt işçilik saati başına 45 ₺ oranla yüklemektedir. Dönem içinde 26.000 direkt işçilik saati "
    "çalışılmış, gerçekleşen GÜG 1.230.000 ₺ olmuştur. Fark önemli kabul edilmiş ve stoklar ile SMM arasında dağıtılacak "
    "tutar belirlenecektir.\n\nEksik yüklenen GÜG tutarı kaç ₺’dir?",
    tl(1_230_000 - 45 * 26_000), secenekler(60_000, 1_170_000, 30_000, 90_000, 1_230_000),
    "Yüklenen GÜG 45 × 26.000 = 1.170.000 ₺; gerçekleşen 1.230.000 ₺. Gerçekleşen yüklenenden büyük olduğundan "
    "1.230.000 − 1.170.000 = 60.000 ₺ eksik yükleme vardır.", zorluk="hard")

P.q("Yüklenen ve gerçekleşen GÜG",
    "Yıl sonunda önemli tutarda 90.000 ₺ eksik yüklenmiş GÜG bulunan işletmede, yılın yüklenen GÜG’ünün %20’si yarı "
    "mamullerde, %30’u mamullerde, %50’si satılan mamullerde bulunmaktadır.\n\nFarkın oranlı dağıtılması ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Yarı mamul 18.000, mamul 27.000, SMM 45.000 ₺ artırılır.",
    ["SMM 90.000 ₺ artırılır, stoklar değişmez.",
     "Yarı mamul 18.000, mamul 27.000, SMM 45.000 ₺ azaltılır.",
     "Yarı mamul 30.000, mamul 30.000, SMM 30.000 ₺ artırılır.",
     "Fark gelecek yılın yükleme oranına eklenir."],
    "Önemli farklar yüklenen GÜG’ün bulunduğu hesaplar arasında oranlı dağıtılır. Eksik yükleme maliyetleri artırır: "
    "yarı mamul 90.000 × %20 = 18.000, mamul 27.000, SMM 45.000 ₺.", zorluk="hard")

# ------------------------------------------------------------------ ABC
pools = [("Makine ayarı", 900_000, 1_500, "ayar"), ("Malzeme taşıma", 400_000, 2_000, "taşıma"),
         ("Kalite testi", 600_000, 3_000, "test"), ("Sipariş işleme", 300_000, 600, "sipariş")]
tabloabc = ("| Faaliyet | Bütçelenen GÜG (₺) | Maliyet sürücüsü | Bütçelenen işlem |\n|---|---|---|---|\n" +
            "\n".join(f"| {a} | {tl(g)} | {s} sayısı | {tl(n)} |" for a, g, n, s in pools))
oran = [g // n for _, g, n, _ in pools]
P.q(ABC,
    "Faaliyet tabanlı maliyetleme uygulayan işletmenin bütçe verileri aşağıdadır:\n\n" + tabloabc +
    "\n\nFaaliyet yükleme oranları sırasıyla aşağıdakilerden hangisidir?",
    f"{oran[0]} ₺/ayar; {oran[1]} ₺/taşıma; {oran[2]} ₺/test; {oran[3]} ₺/sipariş",
    [f"{tl(1_500)} ₺/ayar; {tl(2_000)} ₺/taşıma; {tl(3_000)} ₺/test; {oran[3] * 2} ₺/sipariş",
     "0,0017 ₺/ayar; 0,005 ₺/taşıma; 0,005 ₺/test; 0,002 ₺/sipariş",
     f"{oran[0] // 2} ₺/ayar; {oran[1] * 2} ₺/taşıma; {oran[2]} ₺/test; {oran[3]} ₺/sipariş",
     f"{tl(2_200_000 // 7_100)} ₺/ayar; {tl(2_200_000 // 7_100)} ₺/taşıma; {tl(2_200_000 // 7_100)} ₺/test; "
     f"{tl(2_200_000 // 7_100)} ₺/sipariş"],
    f"Faaliyet yükleme oranı = faaliyet havuzunun bütçelenen gideri / bütçelenen sürücü miktarı: 900.000 / 1.500 = "
    f"{oran[0]}; 400.000 / 2.000 = {oran[1]}; 600.000 / 3.000 = {oran[2]}; 300.000 / 600 = {oran[3]} ₺.", zorluk="hard")

use = [300, 500, 1_000, 120]
yuk = sum(u * o for u, o in zip(use, oran))
P.sayisal(ABC,
    "Faaliyet yükleme oranları makine ayarı 600 ₺/ayar, malzeme taşıma 200 ₺/taşıma, kalite testi 200 ₺/test ve sipariş "
    "işleme 500 ₺/sipariş olarak belirlenmiştir. X ürünü dönem içinde 300 ayar, 500 taşıma, 1.000 test ve 120 sipariş "
    "işlemi kullanmıştır.\n\nX ürününe yüklenecek toplam GÜG kaç ₺’dir?",
    tl(yuk), secenekler(yuk, 480_000, 600_000, 380_000, 2_200_000),
    f"X’e yüklenen GÜG = 300 × 600 + 500 × 200 + 1.000 × 200 + 120 × 500 = 180.000 + 100.000 + 200.000 + 60.000 = "
    f"{tl(yuk)} ₺.")

P.q(ABC,
    "Geleneksel yöntemde tüm GÜG’ü direkt işçilik saatine göre yükleyen bir işletme, çok çeşitli ve küçük partili "
    "ürünlerinin maliyetlerinin düşük, büyük partili standart ürünlerinin ise yüksek hesaplandığını fark etmiştir. Yönetim "
    "faaliyet tabanlı maliyetlemeye geçmeyi değerlendirmektedir.\n\nFaaliyet tabanlı maliyetleme ile ilgili "
    "aşağıdakilerden hangisi yanlıştır?",
    "GÜG tek bir hacim tabanlı ölçüyle yüklenir.",
    ["Giderler önce faaliyetlerde toplanır.",
     "Her faaliyet için ayrı maliyet sürücüsü belirlenir.",
     "Küçük partili ürünlerin maliyeti daha doğru hesaplanır.",
     "Parti ve ürün düzeyindeki faaliyetler ayrı izlenir."],
    "Faaliyet tabanlı maliyetleme GÜG’ü tek bir hacim ölçüsüyle değil, faaliyetlerin kendi maliyet sürücüleriyle "
    "yükler; böylece kurulum ve sipariş gibi parti düzeyindeki giderler küçük partili ürünlere doğru biçimde yansır.",
    zorluk="hard")

P.q(ABC,
    "Faaliyet tabanlı maliyetleme sistemi kuran bir işletmede makine ayarı, satın alma siparişi, ürün tasarımı ve fabrika "
    "binası bakımı faaliyetleri tanımlanmıştır. Faaliyetler, maliyetin doğduğu düzeye göre sınıflandırılacaktır.\n\nMakine "
    "ayarı faaliyeti hangi faaliyet düzeyindedir?",
    "Parti düzeyi",
    ["Birim düzeyi", "Ürün (destek) düzeyi", "Tesis düzeyi", "Müşteri düzeyi"],
    "Makine ayarı her üretim partisi için yapılır ve maliyeti parti sayısına bağlıdır; parti düzeyi faaliyettir. Ürün "
    "tasarımı ürün düzeyinde, fabrika bina bakımı tesis düzeyinde yer alır.", zorluk="easy")

P.sayisal(ABC,
    "Faaliyet tabanlı maliyetleme uygulayan işletmede kalite kontrol faaliyetinin yıllık bütçesi 1.260.000 ₺ ve "
    "bütçelenen test sayısı 4.200’dür. Y ürünü yıl içinde 350 test kullanmış ve 10.000 birim üretilmiştir.\n\nY ürününün "
    "birim başına kalite kontrol maliyeti kaç ₺’dir?",
    tl(1_260_000 // 4_200 * 350 / 10_000), secenekler(10.5, 300, 126, 35, 1.05),
    "Faaliyet oranı 1.260.000 / 4.200 = 300 ₺/test; Y’ye yüklenen 350 × 300 = 105.000 ₺; birim başına 105.000 / 10.000 = "
    "10,5 ₺.", zorluk="hard")

# ------------------------------------------------------------------ çeşitli hesaplar
P.sayisal(R,
    "Bir işletmede bina aydınlatma gideri 54.000 ₺ olup aydınlatılan alana göre dağıtılmaktadır. Dokuma bölümü 1.200 m², "
    "boya bölümü 900 m², depo 600 m², idari bölüm 300 m² alan kullanmaktadır.\n\nBoya bölümüne düşen aydınlatma payı kaç "
    "₺’dir?",
    tl(54_000 * 900 // 3_000), secenekler(16_200, 21_600, 10_800, 5_400, 13_500),
    "Dağıtım oranı 54.000 / 3.000 m² = 18 ₺/m²; boya bölümü 900 × 18 = 16.200 ₺.", zorluk="easy")

P.sayisal(R,
    "Yemekhane giderleri 96.000 ₺ olup yemek yiyen personel sayısına göre dağıtılmaktadır. Kesimde 25, dikimde 55, "
    "paketlemede 20 kişi çalışmakta; ayrıca yemekhanede 4 aşçı çalışmakta ve kendi bölümüne pay verilmemektedir.\n\n"
    "Dikim bölümüne düşen yemekhane payı kaç ₺’dir?",
    tl(96_000 * 55 // 100), secenekler(52_800, 50_769, 24_000, 19_200, 48_000),
    "Pay verilmeyen yemekhane personeli hariç 100 kişi dikkate alınır: 96.000 / 100 = 960 ₺/kişi; dikim 55 × 960 = "
    "52.800 ₺.", zorluk="hard")

P.q(RY,
    "Bir işletmede genel yönetim, satış ve Ar-Ge birimleri de gider yeri olarak izlenmektedir. Muhasebe müdürü bu birimlerin "
    "giderlerinin de ikinci dağıtımla esas üretim gider yerlerine aktarılıp aktarılmayacağını sormaktadır.\n\nBu birimlerin "
    "giderleri ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Üretim maliyetine yüklenmez, dönem gideri olur.",
    ["İkinci dağıtımla esas üretim gider yerlerine aktarılır.",
     "Doğrudan mamullere yüklenir.",
     "Yardımcı üretim gider yeri olarak dağıtılır.",
     "Birinci dağıtımda sadece esas üretime paylaştırılır."],
    "Genel yönetim, pazarlama-satış ve Ar-Ge gider yerlerinin giderleri üretim maliyetine yüklenmez; 7/A’da kendi gider "
    "hesaplarında (750, 760, 770) izlenir ve dönem gideri olarak gelir tablosuna aktarılır.")

P.q(R,
    "Yardımcı gider yerlerinin sayısı fazla olan ve bu yerlerin birbirine önemli ölçüde hizmet verdiği bir işletme, ikinci "
    "dağıtımda en doğru sonucu verecek yöntemi aramaktadır; hesaplama yükü bir sorun oluşturmamaktadır.\n\nİşletmenin "
    "seçmesi gereken yöntem aşağıdakilerden hangisidir?",
    "Karşılıklı dağıtım",
    ["Doğrudan (tek yönlü) dağıtım", "Basamaklı (kademeli) dağıtım", "Tek fabrika yükleme oranı",
     "Birinci dağıtımın tekrarı"],
    "Karşılıklı dağıtım yardımcı gider yerleri arasındaki tüm karşılıklı hizmetleri denklemlerle dikkate aldığından en "
    "doğru sonucu verir; doğrudan dağıtım bu hizmetleri yok sayar, basamaklı dağıtım kısmen dikkate alır.", zorluk="easy")

P.sayisal(R,
    "Birinci dağıtım sonrası bakım bölümünün gideri 150.000 ₺’dir. Bakım hizmetleri bakım saatine göre dağıtılmakta olup "
    "Kesim 1.200, Montaj 1.800 saat hizmet almıştır; doğrudan dağıtım uygulanmaktadır.\n\nMontaj bölümüne düşen bakım "
    "payı kaç ₺’dir?",
    tl(150_000 * 1_800 // 3_000), secenekler(90_000, 60_000, 75_000, 150_000, 112_500),
    "Bakım saati başına oran 150.000 / 3.000 = 50 ₺; Montaj 1.800 × 50 = 90.000 ₺, Kesim 60.000 ₺.", zorluk="easy")

P.q(R,
    "Bir işletmede ikinci dağıtımda basamaklı yöntem uygulanacak ve hangi yardımcı gider yerinin önce dağıtılacağına "
    "karar verilecektir. Personel bölümü diğer tüm bölümlere, bakım bölümü sadece üretim bölümlerine hizmet "
    "vermektedir.\n\nBasamaklı yöntemde dağıtım sırası ile ilgili uygun olan aşağıdakilerden hangisidir?",
    "Önce en çok bölüme hizmet veren personel bölümü dağıtılır.",
    ["Önce en az gideri olan gider yeri dağıtılır.",
     "Sıra sonuçları etkilemez, rastgele seçilir.",
     "Önce esas üretim gider yerleri dağıtılır.",
     "Önce bakım bölümü, sonra personel bölümü dağıtılır."],
    "Basamaklı dağıtımda genellikle en çok gider yerine hizmet veren (veya en yüksek tutarlı) yardımcı gider yeri önce "
    "dağıtılır; sıra sonuçları etkilediğinden gelişigüzel seçilmez.")

# ------------------------------------------------------------------ kapasite ve yükleme
P.q("Genel üretim gideri yükleme oranı",
    "Bir işletme sabit GÜG’ü yükleme oranını belirlerken hangi kapasite düzeyini kullanacağını tartışmaktadır. Fiilî "
    "kapasite yıldan yıla dalgalanmakta, bu da birim maliyetlerin mevsimsel değişimine yol açmaktadır.\n\nMaliyetlerin "
    "dönemler arasında istikrarlı olması için yükleme oranında kullanılması uygun kapasite aşağıdakilerden hangisidir?",
    "Normal kapasite",
    ["Teorik kapasite", "Fiilî kapasite", "Boş kapasite", "Azami kapasite"],
    "Normal kapasite birkaç dönemin ortalama faaliyet düzeyini yansıttığından sabit GÜG yükleme oranlarında kullanılır; "
    "fiilî kapasite oranları dalgalandırır, teorik kapasite ise ulaşılamaz bir düzeydir.", zorluk="easy")

P.sayisal("Genel üretim gideri yükleme oranı",
    "Bir işletmenin yıllık bütçelenen sabit GÜG’ü 720.000 ₺, bütçelenen değişken GÜG’ü makine saati başına 12 ₺’dir. "
    "Normal kapasite 60.000 makine saatidir.\n\nToplam GÜG yükleme oranı makine saati başına kaç ₺’dir?",
    tl(720_000 // 60_000 + 12), secenekler(24, 12, 36, 18, 30),
    "Sabit GÜG oranı 720.000 / 60.000 = 12 ₺; değişken oran 12 ₺. Toplam yükleme oranı 24 ₺/makine saati.",
    zorluk="easy")

P.q("Genel üretim gideri yükleme oranı",
    "GÜG’ü normal kapasiteye göre belirlenen oranla yükleyen işletmede bu yıl fiilî faaliyet normal kapasitenin altında "
    "kalmış, gerçekleşen sabit GÜG bütçeye eşit çıkmıştır. Değişken GÜG’de fark oluşmamıştır.\n\nBu durumda sabit GÜG ile "
    "ilgili aşağıdakilerden hangisi doğrudur?",
    "Eksik yükleme oluşur.",
    ["Fazla yükleme oluşur.", "Fark oluşmaz.", "Sabit GÜG yükleme oranı artar.",
     "Değişken GÜG’de fazla yükleme oluşur."],
    "Yüklenen sabit GÜG = oran × fiilî faaliyettir. Fiilî faaliyet normal kapasitenin altında kaldığında yüklenen tutar "
    "bütçelenen (ve gerçekleşen) sabit GÜG’den az olur; eksik yükleme (kapasite farkı) doğar.", zorluk="hard")

# ------------------------------------------------------------------ gider yerleri + kayıt
P.q("MSUGT: gider yerleri",
    "7/A seçeneğini uygulayan işletme genel üretim giderlerini gider yerlerine göre izlemek istemektedir. Muhasebe "
    "servisi 730 hesabının alt hesaplarını kesim, montaj, bakım ve yemekhane bölümlerine göre açmayı "
    "planlamaktadır.\n\nMSUGT’ye göre gider yerleri ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Fonksiyon hesaplarının alt hesaplarında izlenir.",
    ["Gider yerleri sadece 7/B seçeneğinde izlenir.",
     "Gider yerleri için ayrı bir hesap sınıfı açılır.",
     "Gider yerleri gelir tablosunda ayrı gösterilir.",
     "Gider yerleri sadece hizmet işletmelerinde kullanılır."],
    "MSUGT’ye göre 7/A seçeneğinde giderler fonksiyonel gider hesaplarında, bu hesapların altında gider yerlerine ve gider "
    "çeşitlerine göre açılan alt hesaplarda izlenir.")

P.q(R,
    "İkinci dağıtım sonunda işletmenin yardımcı gider yerlerinin (bakım ve yemekhane) bakiyeleri sıfırlanmış, tüm genel "
    "üretim giderleri kesim ve montaj bölümlerinde toplanmıştır. Toplam GÜG birinci dağıtımdakiyle aynıdır.\n\nBu aşamadan "
    "sonra yapılacak işlem aşağıdakilerden hangisidir?",
    "Esas bölüm giderleri oranlarla mamullere yüklenir.",
    ["Yardımcı gider yerlerinin giderleri yeniden hesaplanır.",
     "Giderler gelir tablosuna dönem gideri olarak aktarılır.",
     "Birinci dağıtım yeniden yapılır.",
     "Giderler satış bölümüne aktarılır."],
    "İkinci dağıtımdan sonra her esas üretim gider yerinin toplam gideri kendi dağıtım ölçüsüne bölünerek yükleme oranı "
    "bulunur ve bu oranlarla mamullere yükleme yapılır (üçüncü aşama).")

P.q(R,
    "Bir işletmede birinci dağıtım sonunda gider yerlerinin toplamı 900.000 ₺’dir. İkinci dağıtımda basamaklı yöntem "
    "kullanılmış ve yardımcı gider yerlerinin tamamı esas üretim yerlerine dağıtılmıştır.\n\nİkinci dağıtım sonunda esas "
    "üretim gider yerlerinin toplam gideri ile ilgili aşağıdakilerden hangisi doğrudur?",
    "900.000 ₺’ye eşittir; toplam değişmez.",
    ["900.000 ₺’den fazladır; yardımcı giderler eklenir.",
     "900.000 ₺’den azdır; yardımcı giderler düşülür.",
     "Yöntemin seçimine göre toplam değişir.",
     "Sadece yardımcı gider yerlerinin toplamına eşittir."],
    "İkinci dağıtım giderleri gider yerleri arasında yer değiştirir, toplamı değiştirmez; yöntem seçimi sadece esas "
    "bölümler arasındaki paylaşımı etkiler.", zorluk="easy")

# ------------------------------------------------------------------ ek sayısal ve olumsuz
P.sayisal(R,
    "Bir işletmede ortak bir kazan dairesinin buhar gideri 210.000 ₺ olup buhar tüketimine göre dağıtılmaktadır. Boya "
    "bölümü 1.800 ton, apre bölümü 1.200 ton, idari bina ısıtması 500 ton buhar kullanmıştır.\n\nApre bölümüne düşen buhar "
    "payı kaç ₺’dir?",
    tl(210_000 * 1_200 // 3_500), secenekler(72_000, 84_000, 108_000, 30_000, 70_000),
    "Oran 210.000 / 3.500 ton = 60 ₺/ton; apre 1.200 × 60 = 72.000 ₺. İdari binaya düşen 30.000 ₺ genel yönetim "
    "gideridir.")

P.q(R,
    "Bir işletmede yardımcı gider yerlerinin giderleri esas üretim yerlerine bütçelenmiş (normal) tutarlar üzerinden, "
    "gerçekleşen tutarlar yerine dağıtılmaktadır. Yönetim bu uygulamanın gerekçesini sormaktadır.\n\nBu uygulamanın temel "
    "yararı aşağıdakilerden hangisidir?",
    "Yardımcı bölümün verimsizliği esas bölümlere aktarılmaz.",
    ["Toplam GÜG azalır.",
     "Yardımcı bölümün giderleri mamul maliyetine girmez.",
     "Birinci dağıtıma gerek kalmaz.",
     "Esas bölümlerin giderleri sabitlenir."],
    "Bütçelenen oranlarla dağıtım, yardımcı bölümdeki fazla harcamaların (verimsizliğin) esas bölümlere yansımasını önler; "
    "fark yardımcı bölümde kalır ve yöneticisinden sorulur.", zorluk="hard")

P.q(ABC,
    "Faaliyet tabanlı maliyetleme uygulayan işletme bir faaliyet için maliyet sürücüsü seçecektir. Sipariş işleme "
    "faaliyetinin maliyetleri sipariş başına harcanan zamandan çok alınan sipariş sayısına bağlı olarak "
    "değişmektedir.\n\nBu faaliyet için en uygun maliyet sürücüsü aşağıdakilerden hangisidir?",
    "Sipariş sayısı",
    ["Üretilen birim sayısı", "Direkt işçilik saati", "Makine saati", "Satış tutarı"],
    "Maliyet sürücüsü faaliyetin maliyetini fiilen doğuran etkendir; sipariş işleme maliyetleri sipariş sayısıyla "
    "değiştiğinden sipariş sayısı uygun sürücüdür.", zorluk="easy")

P.q(ABC,
    "Geleneksel yöntemle GÜG’ü birim sayısına göre yükleyen işletmede A ürünü 10.000 birim ve 10 parti, B ürünü 1.000 "
    "birim ve 10 partide üretilmiştir. Toplam 220.000 ₺ makine ayar gideri parti sayısından kaynaklanmaktadır.\n\n"
    "Faaliyet tabanlı maliyetlemeye geçildiğinde B ürününe yüklenen ayar gideri ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "20.000 ₺’den 110.000 ₺’ye çıkar.",
    ["110.000 ₺’den 20.000 ₺’ye iner.",
     "20.000 ₺’de kalır.",
     "200.000 ₺’den 110.000 ₺’ye iner.",
     "Ayar gideri B’ye yüklenmez."],
    "Birim sayısına göre B’ye 220.000 × 1.000 / 11.000 = 20.000 ₺ düşer. Parti sayısına göre (10:10) yarısı, 110.000 ₺ "
    "düşer; küçük partili ürünün maliyeti geleneksel yöntemde düşük hesaplanmaktadır.", zorluk="hard")

P.q(RY,
    "Bir işletmede bakım bölümü sadece üretim bölümlerine, personel bölümü ise üretim bölümleriyle birlikte bakım bölümüne "
    "de hizmet vermektedir. Yönetim yardımcı gider yerlerini sınıflandırmak istemektedir.\n\nAşağıdakilerden hangisi "
    "yardımcı gider yeri değildir?",
    "Montaj bölümü",
    ["Bakım bölümü", "Personel bölümü", "Yemekhane", "Bekçilik ve güvenlik"],
    "Montaj doğrudan ürün üzerinde çalışan esas üretim gider yeridir. Bakım yardımcı üretim; personel, yemekhane ve "
    "güvenlik yardımcı hizmet gider yerleridir.", zorluk="easy")

P.sayisal(R,
    "Bir işletmede bakım bölümünün ikinci dağıtımda dağıtılacak toplam gideri 136.000 ₺’dir. Bakım hizmetleri makine "
    "saatine göre dağıtılmakta olup Kesim 5.100, Montaj 3.400 makine saati kullanmıştır.\n\nKesim bölümüne düşen bakım "
    "payı kaç ₺’dir?",
    tl(136_000 * 5_100 // 8_500), secenekler(81_600, 54_400, 68_000, 76_500, 136_000),
    "Oran 136.000 / 8.500 = 16 ₺/makine saati; Kesim 5.100 × 16 = 81.600 ₺, Montaj 54.400 ₺.")

P.q(R,
    "Bir işletmede ikinci dağıtımda doğrudan dağıtım yöntemi kullanılmaktadır. Yardımcı bölümlerden bakım, personel "
    "bölümüne de hizmet vermekte, ancak bu hizmet dağıtımda dikkate alınmamaktadır.\n\nDoğrudan dağıtım yöntemi ile ilgili "
    "aşağıdakilerden hangisi doğrudur?",
    "Yardımcı gider yerleri arasındaki hizmetler yok sayılır.",
    ["Yardımcı gider yerleri sırayla birbirine de dağıtılır.",
     "Karşılıklı hizmetler denklemlerle hesaplanır.",
     "Giderler doğrudan mamullere yüklenir.",
     "Esas üretim gider yerleri de birbirine dağıtılır."],
    "Doğrudan dağıtımda yardımcı gider yerlerinin giderleri sadece esas üretim gider yerlerine dağıtılır; yardımcı "
    "bölümler arasındaki karşılıklı hizmetler dikkate alınmaz.")

P.sayisal("Genel üretim gideri yükleme oranı",
    "Montaj bölümünün ikinci dağıtım sonrası gideri 394.400 ₺’dir. Bölümde ay içinde 9.860 direkt işçilik saati "
    "çalışılmış olup bölüm giderleri direkt işçilik saatine göre mamullere yüklenmektedir.\n\nMontaj bölümünün GÜG yükleme "
    "katsayısı direkt işçilik saati başına kaç ₺’dir?",
    tl(394_400 // 9_860), secenekler(40, 45, 36, 50, 30),
    "Yükleme katsayısı = 394.400 / 9.860 = 40 ₺/direkt işçilik saati.", zorluk="easy")

P.q("Yüklenen ve gerçekleşen GÜG",
    "Bir işletmede ay sonunda yüklenen GÜG 612.000 ₺, gerçekleşen GÜG 598.000 ₺’dir. Fark önemsiz kabul edilmekte olup "
    "işletme 7/A seçeneğini uygulamaktadır.\n\nFarkın muhasebeleştirilmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "14.000 ₺ fazla yükleme SMM’den düşülür.",
    ["14.000 ₺ eksik yükleme SMM’ye eklenir.",
     "14.000 ₺ fazla yükleme gelir yazılır.",
     "Fark yarı mamullere eklenir.",
     "Fark gelecek ayın yükleme oranına eklenir."],
    "Yüklenen gerçekleşenden 14.000 ₺ fazladır; önemsiz fazla yükleme satılan mamuller maliyetinden düşülerek kapatılır.",
    zorluk="hard")

P.q(RY,
    "Tekdüzen Muhasebe Sistemi Uygulama Genel Tebliği’ne göre gider yerlerinin tanımı ve kuruluşu değerlendirilmektedir. "
    "Bir işletme gider yerlerini organizasyon şemasındaki bölümlerle aynı tutmayı, her gider yeri için sorumlu bir yönetici "
    "belirlemeyi planlamaktadır.\n\nGider yerleriyle ilgili aşağıdakilerden hangisi doğrudur?",
    "Giderin doğduğu, sorumluluğu belli birimlerdir.",
    ["Sadece mamul üreten esas üretim bölümleridir.",
     "Maliyetin yüklendiği mamullerin kendisidir.",
     "Sadece satış geliri elde eden kâr merkezleridir.",
     "Muhasebe servisinin kayıt birimleridir."],
    "Gider yerleri, giderlerin doğduğu ve izlenip kontrol edilebildiği, sorumluluğu belirli işletme bölümleridir; esas ve "
    "yardımcı üretim ile hizmet bölümlerini kapsar.", zorluk="easy")

P.q(R,
    "Bir işletme birinci dağıtımda fabrika binası amortismanını gider yerlerinin kullandığı alana göre dağıtmaktadır. "
    "Bölüm alanları kesim 500, montaj 300, bakım 200 m²’dir; aylık amortisman 80.000 ₺’dir. Montaj bölümüne ayrıca 12.000 ₺ "
    "doğrudan ait bakım malzemesi gideri vardır.\n\nMontaj bölümünün birinci dağıtımdan aldığı toplam pay kaç ₺’dir?",
    "36.000 ₺",
    ["24.000 ₺", "28.000 ₺", "40.000 ₺", "92.000 ₺"],
    "Amortisman payı 80.000 × 300 / 1.000 = 24.000 ₺; doğrudan ait malzeme gideri 12.000 ₺ eklenir: 36.000 ₺.")

P.sayisal(ABC,
    "Faaliyet tabanlı maliyetlemede bir işletmenin satın alma faaliyetinin yıllık gideri 480.000 ₺, satın alma siparişi "
    "sayısı 1.600’dür. Z ürünü için yıl içinde 240 satın alma siparişi verilmiştir.\n\nZ ürününe yüklenecek satın alma "
    "faaliyeti gideri kaç ₺’dir?",
    tl(480_000 // 1_600 * 240), secenekler(72_000, 48_000, 96_000, 120_000, 300),
    "Faaliyet oranı 480.000 / 1.600 = 300 ₺/sipariş; Z’ye yüklenen 240 × 300 = 72.000 ₺.", zorluk="easy")

P.q(R,
    "Bir işletmede ikinci dağıtımda yardımcı gider yerlerinin giderleri esas üretim yerlerine aktarılırken bazı kayıtlar "
    "yapılmaktadır. Muhasebe müdürü, bu aktarımların genel üretim giderleri toplamını ve mamul maliyetlerini nasıl "
    "etkileyeceğini sormaktadır.\n\nİkinci dağıtım ile ilgili aşağıdakilerden hangisi yanlıştır?",
    "İkinci dağıtım toplam GÜG’ü artırır.",
    ["Yardımcı gider yerlerinin bakiyesi sıfırlanır.",
     "Esas üretim gider yerlerinin gideri artar.",
     "Dağıtım yöntemi esas bölümler arası payı etkiler.",
     "Mamullere yükleme bu aşamadan sonra yapılır."],
    "İkinci dağıtım giderleri gider yerleri arasında aktarır; toplam GÜG değişmez. Yardımcı yerlerin bakiyesi sıfırlanır, "
    "esas bölümlerin gideri artar.", zorluk="easy")

P.q(R,
    "Bir işletme iki esas üretim bölümüne sahiptir. Kesim bölümünün gideri makine saatiyle, Montaj bölümünün gideri direkt "
    "işçilik saatiyle yakından ilişkilidir. Muhasebe bölümü her bölüm için ayrı yükleme ölçüsü belirlemektedir.\n\nBu "
    "uygulamanın mamul maliyetleri üzerindeki etkisi aşağıdakilerden hangisidir?",
    "Mamuller bölümleri kullanma oranında maliyet alır.",
    ["Tüm mamuller eşit GÜG alır.",
     "GÜG toplamı azalır.",
     "Mamul maliyeti yükleme ölçüsünden etkilenmez.",
     "Sadece Montajdan geçen mamuller GÜG alır."],
    "Her bölümün giderini o bölümün faaliyetini en iyi ölçen ölçüyle yüklemek, mamullerin bölüm kaynaklarını ne ölçüde "
    "kullandıklarını maliyete yansıtır.")

P.sayisal("Genel üretim gideri yükleme oranı",
    "Bir işletmede tek fabrika oranı kullanıldığında GÜG makine saati başına 60 ₺ yüklenmektedir. Bir parti ürün 150 "
    "makine saati kullanmış, partiye ayrıca 90.000 ₺ direkt ilk madde ve 45.000 ₺ direkt işçilik harcanmıştır.\n\nPartinin "
    "toplam üretim maliyeti kaç ₺’dir?",
    tl(90_000 + 45_000 + 150 * 60), secenekler(144_000, 135_000, 225_000, 153_000, 99_000),
    "Yüklenen GÜG 150 × 60 = 9.000 ₺; parti maliyeti 90.000 + 45.000 + 9.000 = 144.000 ₺.", zorluk="easy")

P.q(ABC,
    "Faaliyet tabanlı maliyetlemede fabrika binasının güvenliği ve genel aydınlatması gibi tüm üretime yönelik "
    "faaliyetlerin maliyetleri belirli bir ürün, parti veya birimle ilişkilendirilememektedir.\n\nBu faaliyetler hangi "
    "düzeyde yer alır?",
    "Tesis düzeyi",
    ["Birim düzeyi", "Parti düzeyi", "Ürün (destek) düzeyi", "Sipariş düzeyi"],
    "Tüm tesisin varlığını sürdürmeye yönelik ve ürünlerle doğrudan ilişkilendirilemeyen faaliyetler tesis düzeyindedir; "
    "bunların maliyetleri genellikle keyfi ölçülerle dağıtılır veya dönem gideri sayılır.")

P.q("Genel üretim gideri yükleme oranı",
    "Bir işletme yıl başında GÜG yükleme oranını bütçelenmiş tutarlarla belirlemiştir. Yıl ortasında enerji fiyatlarında "
    "beklenmedik bir artış olmuş, gerçekleşen GÜG bütçenin önemli ölçüde üzerine çıkmıştır.\n\nBu durumun sonucu "
    "aşağıdakilerden hangisidir?",
    "Eksik yükleme oluşur, yıl sonunda düzeltilir.",
    ["Fazla yükleme oluşur; SMM azaltılır.",
     "Yükleme oranı her ay yeniden hesaplanmalıdır.",
     "Mamul maliyeti etkilenmez.",
     "Fark doğrudan özkaynağa alınır."],
    "Önceden belirlenen oranla yüklenen GÜG, gerçekleşen GÜG’ün altında kalır; eksik yükleme oluşur ve yıl sonunda "
    "önemliliğe göre SMM’ye ya da stoklar ve SMM’ye dağıtılarak düzeltilir.")

P.sayisal(R,
    "Bir işletmede personel bölümünün gideri 60.000 ₺ olup çalışan sayısına göre dağıtılmaktadır. Kesim 40, montaj 60, "
    "bakım 20 çalışana sahiptir; basamaklı yöntemde personel bölümü ilk sırada dağıtılmaktadır.\n\nBakım bölümüne düşen "
    "personel gideri payı kaç ₺’dir?",
    tl(60_000 * 20 // 120), secenekler(10_000, 12_000, 20_000, 15_000, 6_000),
    "Oran 60.000 / 120 = 500 ₺/çalışan; bakım 20 × 500 = 10.000 ₺ alır. Basamaklı yöntemde bu tutar bakımın gideriyle "
    "birlikte sonra esas bölümlere dağıtılır.", zorluk="easy")

P.q(R,
    "Bir işletme GÜG dağıtım tablosunu hazırlamaktadır. Tablo; birinci dağıtım, ikinci dağıtım ve yükleme oranlarının "
    "hesaplanması bölümlerinden oluşmakta, her gider yeri için dağıtım ölçüsü ve ölçü birimi belirtilmektedir.\n\nGÜG "
    "dağıtım tablosunun temel amacı aşağıdakilerden hangisidir?",
    "GÜG’ü gider yerleri yoluyla mamullere yüklemek",
    ["Direkt ilk madde ve işçilik tutarlarını hesaplamak",
     "Mamullerin satış fiyatını doğrudan belirlemek",
     "Faaliyet dönemi giderlerini ayrıca hesaplamak",
     "Vergi matrahını belirlemek"],
    "Dağıtım tablosu ürüne doğrudan izlenemeyen GÜG’ü önce gider yerlerine, sonra esas üretim gider yerlerinde toplayıp "
    "yükleme oranlarıyla mamullere yüklemek için düzenlenir.", zorluk="easy")

P.q(ABC,
    "Faaliyet tabanlı maliyetleme uygulayan işletme, bir ürün hattını tasarlama ve mühendislik değişiklikleri yapma "
    "faaliyetlerinin maliyetlerini izlemektedir. Bu maliyetler üretilen birim veya parti sayısından bağımsız olup ürünün "
    "varlığını sürdürmek için katlanılmaktadır.\n\nBu faaliyetler hangi düzeydedir?",
    "Ürün (destek) düzeyi",
    ["Birim düzeyi", "Parti düzeyi", "Tesis düzeyi", "Müşteri siparişi düzeyi"],
    "Belirli bir ürünü destekleyen ve üretim hacmiyle değişmeyen tasarım ve mühendislik faaliyetleri ürün (destek) "
    "düzeyindedir.")

P.sayisal(R,
    "Bir işletmede bakım bölümünün gideri 90.000 ₺, yemekhane bölümünün gideri 45.000 ₺’dir. Doğrudan dağıtım uygulanmakta, "
    "bakım makine saatine (Kesim 2.000, Montaj 1.000), yemekhane personel sayısına (Kesim 20, Montaj 25) göre "
    "dağıtılmaktadır.\n\nMontaj bölümünün ikinci dağıtımdan aldığı toplam pay kaç ₺’dir?",
    tl(90_000 * 1_000 // 3_000 + 45_000 * 25 // 45), secenekler(55_000, 80_000, 30_000, 25_000, 67_500),
    "Montaj, bakımdan 90.000 × 1.000 / 3.000 = 30.000 ₺, yemekhaneden 45.000 × 25 / 45 = 25.000 ₺ alır; toplam 55.000 ₺.")

P.q("Yüklenen ve gerçekleşen GÜG",
    "İşletmenin yıl sonunda GÜG yükleme farkı analizi şöyledir: değişken GÜG’de 12.000 ₺ fazla yükleme, sabit GÜG’de "
    "20.000 ₺ eksik yükleme oluşmuştur. Farklar önemsiz kabul edilmektedir.\n\nToplam fark ve muhasebeleştirilmesi ile "
    "ilgili aşağıdakilerden hangisi doğrudur?",
    "8.000 ₺ net eksik yükleme SMM’ye eklenir.",
    ["32.000 ₺ eksik yükleme SMM’ye eklenir.",
     "8.000 ₺ net fazla yükleme SMM’den düşülür.",
     "12.000 ₺ SMM’den düşülür, 20.000 ₺ stoklara eklenir.",
     "Farklar birbirini götürür, kayıt yapılmaz."],
    "Net fark = 20.000 eksik − 12.000 fazla = 8.000 ₺ eksik yüklemedir; önemsiz olduğundan satılan mamuller maliyetine "
    "eklenerek kapatılır.", zorluk="hard")

P.q(R,
    "Bir işletme birinci dağıtımda enerji giderlerini, gider yerlerindeki makinelerin kurulu gücüne (kW) göre dağıtmaktadır. "
    "Ancak bazı makineler kurulu güçlerine göre çok az çalışmaktadır ve fiilî tüketim sayaçlarla ölçülebilmektedir.\n\n"
    "Enerji gideri dağıtımı ile ilgili uygun yaklaşım aşağıdakilerden hangisidir?",
    "Fiilî tüketime (kWh) göre dağıtmak",
    ["Kurulu güce göre dağıtmaya devam etmek",
     "Eşit olarak dağıtmak",
     "Çalışan sayısına göre dağıtmak",
     "Alan büyüklüğüne göre dağıtmak"],
    "Dağıtım ölçüsü giderin doğuşunu en iyi yansıtan ölçü olmalıdır; fiilî tüketim ölçülebiliyorsa kWh esaslı dağıtım "
    "kurulu güce göre daha doğrudur.", zorluk="easy")

P.q(ABC,
    "Faaliyet tabanlı maliyetleme sistemini tasarlayan işletme önce kaynak giderlerini faaliyetlere, sonra faaliyet "
    "maliyetlerini ürünlere aktaracaktır. İlk aşamada personel ücretleri, çalışanların faaliyetlere ayırdığı süreye göre "
    "paylaştırılacaktır.\n\nKaynak giderlerini faaliyetlere aktarmada kullanılan ölçüye ne ad verilir?",
    "Kaynak sürücüsü",
    ["Faaliyet (maliyet) sürücüsü", "Yükleme katsayısı", "Dağıtım tablosu", "Maliyet taşıyıcısı"],
    "Kaynak giderlerinin faaliyetlere aktarılmasında kullanılan ölçü kaynak sürücüsü, faaliyet maliyetlerinin ürünlere "
    "aktarılmasında kullanılan ölçü faaliyet (maliyet) sürücüsüdür.")

P.q(R,
    "Birinci dağıtımda bir fabrikada 7 gider yeri tanımlanmıştır. İşletme, ortak giderlerin dağıtımında kullanılacak "
    "anahtarların seçiminde tutarlılık ve kolaylık gözetmektedir; anahtarlar dönemden döneme değiştirilmek "
    "istenmemektedir.\n\nDağıtım anahtarlarının seçimi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Giderle nedensellik ilişkisi en güçlü ölçü seçilir.",
    ["Her gider için aynı ölçü kullanılır.",
     "Ölçü her ay en düşük maliyeti verecek biçimde seçilir.",
     "Ölçü sadece esas üretim yerleri için belirlenir.",
     "Ölçü seçimi toplam GÜG’ü değiştirir."],
    "Dağıtım anahtarı gider ile gider yeri arasındaki neden-sonuç ilişkisini en iyi yansıtmalı ve tutarlı uygulanmalıdır; "
    "anahtar seçimi paylaşımı etkiler, toplamı değiştirmez.")

P.sayisal("Genel üretim gideri yükleme oranı",
    "Bir işletme bölüm oranları yerine fabrika genelinde tek bir GÜG yükleme oranı kullanmaktadır. Yıllık bütçelenen "
    "toplam GÜG 900.000 ₺, bütçelenen toplam direkt işçilik saati 30.000’dir; oran direkt işçilik saatine göre "
    "hesaplanmaktadır.\n\nFabrika geneli GÜG yükleme oranı direkt işçilik saati başına kaç ₺’dir?",
    tl(900_000 // 30_000), secenekler(30, 25, 36, 45, 20),
    "Tek fabrika oranı = bütçelenen toplam GÜG / bütçelenen toplam dağıtım ölçüsü = 900.000 / 30.000 = 30 ₺/DİS. Bu oran "
    "bölümlerin farklı gider yapılarını dikkate almaz.", zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
