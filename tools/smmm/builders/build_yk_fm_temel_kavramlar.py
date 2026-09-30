# -*- coding: utf-8 -*-
"""Finansal Muhasebe · Temel Kavramlar ve Muhasebe Süreci — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında Finansal Muhasebe çıplak tanım sormaz; kavramlar bile bir olay ve
tutarla gelir. Bu paket muhasebenin temel kavramlarını, temel eşitliği, hesap işleyişini, hesap planı
yapısını, defter-belge düzenini, gelir tablosu kademelerini ve hata düzeltme kayıtlarını olay üzerinden
sorar.

Dayanak: Muhasebe Sistemi Uygulama Genel Tebliği (MSUGT) — Muhasebenin Temel Kavramları, Tekdüzen
Hesap Planı ve gelir tablosu ilkeleri; VUK md. 174 (hesap dönemi), 219 (kayıt süresi), 229-236
(fatura, gider pusulası, serbest meslek makbuzu). Tutarlar builder içinde hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler
from fm_ortak import kayit as K, taraf as T, hk

P = Paket("questions_topic_finansal_temel_kavramlar_2026.json", lesson="finansal_muhasebe",
          topic="temel_kavramlar", konu_adi="Temel Kavramlar", seed=2026093064,
          surum="MSUGT temel kavramlar ve Tekdüzen Hesap Planı; VUK md. 174, 219, 229-236; 29.09.2026 kontrolü")

KV = "MSUGT: Muhasebenin Temel Kavramları"
R = "MSUGT Tekdüzen Hesap Planı"
HANGI = "Bu durum aşağıdaki muhasebe temel kavramlarından hangisiyle ilgilidir?"
AYKIRI = "Bu uygulama aşağıdaki muhasebe temel kavramlarından hangisine aykırıdır?"
KAVRAMLAR = ["Sosyal sorumluluk", "Kişilik", "İşletmenin sürekliliği", "Dönemsellik", "Parayla ölçülme",
             "Maliyet esası", "Tarafsızlık ve belgelendirme", "Tutarlılık", "Tam açıklama", "İhtiyatlılık",
             "Önemlilik", "Özün önceliği"]


def kavram(dogru, *celdirici):
    for c in (dogru, *celdirici):
        assert c in KAVRAMLAR, c
    return dogru, list(celdirici)


# 1 — kişilik
d, c = kavram("Kişilik", "Dönemsellik", "Tam açıklama", "Maliyet esası", "Sosyal sorumluluk")
P.q(KV,
    "Tek ortaklı bir limited şirketin muhasebe kayıtları incelenirken, şirket ortağının ailesiyle yaptığı 42.000 ₺’lik "
    "tatil harcamasının 770 Genel Yönetim Giderleri hesabına kaydedildiği görülmüştür. Harcamanın şirketin faaliyetiyle "
    f"bir ilgisi yoktur.\n\n{AYKIRI}",
    d, c,
    "Kişilik kavramına göre işletme, sahip ve ortaklarından ayrı bir kişiliktir; ortağın özel harcaması işletme gideri "
    "sayılamaz, ortaktan alacak (131) olarak izlenir.", zorluk="easy")

# 2 — işletmenin sürekliliği
d, c = kavram("İşletmenin sürekliliği", "İhtiyatlılık", "Dönemsellik", "Önemlilik", "Tutarlılık")
P.q(KV,
    "Faaliyetlerine süresiz devam etmesi beklenen bir işletme, yıl sonu bilançosunda 3.200.000 ₺ maliyetli ve 1.100.000 ₺ "
    "birikmiş amortismanlı fabrika binasını tasfiye hâlinde elde edilebilecek 1.500.000 ₺ yerine net defter değeriyle "
    f"göstermiştir.\n\n{HANGI}",
    d, c,
    "İşletmenin sürekliliği kavramına göre işletmenin faaliyetlerini süresiz sürdüreceği varsayılır; bu yüzden varlıklar "
    "tasfiye değerleriyle değil, maliyet esasına göre izlenen değerleriyle raporlanır.", zorluk="easy")

# 3 — dönemsellik
d, c = kavram("Dönemsellik", "Maliyet esası", "Kişilik", "Önemlilik", "Tam açıklama")
P.q(KV,
    "İşletme 1 Kasım 2026’da altı aylık depo kirası olarak 90.000 ₺ ödemiş, bunun 30.000 ₺’sini 2026 yılı gideri, "
    "60.000 ₺’sini 180 Gelecek Aylara Ait Giderler hesabında 2027 yılı gideri olarak izlemiştir.\n\n"
    f"{HANGI}",
    d, c,
    "Dönemsellik kavramı gelir ve giderlerin tahsil ya da ödeme anına değil ait oldukları döneme göre "
    "muhasebeleştirilmesini gerektirir: iki aylık pay 2026’ya, dört aylık pay 2027’ye aittir.", zorluk="easy")

# 4 — parayla ölçülme
d, c = kavram("Parayla ölçülme", "Önemlilik", "Tam açıklama", "Sosyal sorumluluk", "İhtiyatlılık")
P.q(KV,
    "Bir çağrı merkezi işletmesinin yönetimi, deneyimli ve yüksek müşteri memnuniyeti sağlayan 120 kişilik çalışan "
    "kadrosunun işletme için en değerli varlık olduğunu belirtmiş, ancak muhasebe servisi bu değeri bilançoya "
    f"varlık olarak almamıştır.\n\n{HANGI}",
    d, c,
    "Parayla ölçülme kavramına göre ancak para birimiyle güvenilir biçimde ölçülebilen işlemler kayda alınır; çalışanların "
    "deneyimi ve bağlılığı önemli olsa da güvenilir biçimde ölçülemediğinden varlık olarak kaydedilmez.")

# 5 — maliyet esası
d, c = kavram("Maliyet esası", "Özün önceliği", "Tutarlılık", "Dönemsellik", "Tam açıklama")
P.q(KV,
    "İşletme 2024’te 900.000 ₺’ye aldığı arsanın 2026 yılı sonunda ekspertiz raporuyla 1.600.000 ₺ değer kazandığını "
    "öğrenmiştir. Muhasebe müdürü, arsa satılmadığı sürece değer artışının kayıtlara alınmayacağını ve arsanın "
    f"900.000 ₺’den izlenmeye devam edeceğini belirtmiştir.\n\n{HANGI}",
    d, c,
    "Maliyet esası kavramına göre varlıklar edinme maliyetleriyle kaydedilir; gerçekleşmemiş değer artışları kayda "
    "alınmaz. Arsa satıldığında kazanç ortaya çıkar.", zorluk="easy")

# 6 — tarafsızlık ve belgelendirme
d, c = kavram("Tarafsızlık ve belgelendirme", "Kişilik", "Önemlilik", "Dönemsellik", "Parayla ölçülme")
P.q(KV,
    "İşletmenin satın alma sorumlusu bir tedarikçiden 18.500 ₺’lik temizlik malzemesi aldığını, ancak faturasını "
    "kaybettiğini belirterek tutarın gider olarak kaydedilmesini istemiştir. Muhasebe servisi herhangi bir belge "
    f"olmaksızın 770 hesabına kayıt yapmıştır.\n\n{AYKIRI}",
    d, c,
    "Tarafsızlık ve belgelendirme kavramına göre kayıtlar gerçek durumu yansıtan, objektif belgelere dayanmalıdır; belgesiz "
    "gider kaydı bu kavrama aykırıdır.")

# 7 — tutarlılık
d, c = kavram("Tutarlılık", "İhtiyatlılık", "Maliyet esası", "Tam açıklama", "Önemlilik")
P.q(KV,
    "Bir ticaret işletmesi 2024’te stoklarını FIFO, 2025’te ağırlıklı ortalama, 2026’da yeniden FIFO yöntemiyle "
    "değerlemiş; yöntem değişikliklerinin gerekçesini ve etkisini dipnotlarda açıklamamıştır. Bu nedenle yıllar arası "
    f"karşılaştırma yapılamamaktadır.\n\n{AYKIRI}",
    d, c,
    "Tutarlılık kavramı benzer olaylarda aynı muhasebe politikalarının dönemden döneme uygulanmasını, haklı nedenle "
    "değişiklik yapılırsa bunun açıklanmasını gerektirir.")

# 8 — tam açıklama
d, c = kavram("Tam açıklama", "İhtiyatlılık", "Özün önceliği", "Tarafsızlık ve belgelendirme", "Tutarlılık")
P.q(KV,
    "İşletme aleyhine bir müşteri tarafından 2.500.000 ₺ tazminat davası açılmıştır. Hukuk müşaviri davanın sonucunun "
    "belirsiz olduğunu bildirmiş, işletme karşılık ayırmamış ancak davanın niteliğini ve olası etkisini finansal tablo "
    f"dipnotlarında açıklamıştır.\n\n{HANGI}",
    d, c,
    "Tam açıklama kavramına göre finansal tablolar, kullanıcıların karar vermesini etkileyecek bilgileri yeterli, açık ve "
    "anlaşılır biçimde içermelidir; sonucu belirsiz önemli dava dipnotta açıklanır.")

# 9 — ihtiyatlılık
d, c = kavram("İhtiyatlılık", "Tam açıklama", "Maliyet esası", "Özün önceliği", "Dönemsellik")
P.q(KV,
    "Yıl sonunda işletmenin kur riski taşıyan iki kalemi vardır: dövizli alacağında beklenen 40.000 ₺’lik muhtemel bir "
    "kayıp için karşılık ayrılmış, sözleşme gereği gelecek yıl doğması muhtemel 60.000 ₺’lik bir kazanç ise "
    f"gerçekleşmediği için kayda alınmamıştır.\n\n{HANGI}",
    d, c,
    "İhtiyatlılık kavramı muhtemel giderler ve zararlar için karşılık ayrılmasını, gerçekleşmemiş kârların ise kayda "
    "alınmamasını öngörür; bu kavram gizli yedek yaratmayı haklı kılmaz.")

# 10 — önemlilik
d, c = kavram("Önemlilik", "Maliyet esası", "İşletmenin sürekliliği", "Tutarlılık", "Parayla ölçülme")
P.q(KV,
    "Yıllık cirosu 480.000.000 ₺ olan işletme, her biri birkaç yüz lira değerindeki zımba, makas ve hesap makinesi "
    "gibi büro araçlarını demirbaş olarak aktifleştirip amortismana tabi tutmak yerine alındıkları dönemde doğrudan "
    f"gider yazmaktadır.\n\n{HANGI}",
    d, c,
    "Önemlilik kavramına göre bir kalemin göreli ağırlığı, kararları etkilemeyecek düzeydeyse ayrıntılı muhasebe işlemleri "
    "yerine daha basit bir yöntemle kaydedilebilir.")

# 11 — özün önceliği
d, c = kavram("Özün önceliği", "Maliyet esası", "Kişilik", "Tam açıklama", "İhtiyatlılık")
P.q(KV,
    "İşletme elindeki 5.000.000 ₺ değerli bir binayı bir finans kuruluşuna satmış görünmekte, ancak sözleşmeye göre iki "
    "yıl sonra önceden belirlenmiş bedelle geri almayı taahhüt etmekte ve bina süresince kullanmaya devam etmektedir. "
    f"Muhasebe bu işlemi borçlanma olarak kaydetmiştir.\n\n{HANGI}",
    d, c,
    "Özün önceliği kavramı işlemlerin biçiminden çok özlerine göre muhasebeleştirilmesini gerektirir: riskler ve "
    "yararlar işletmede kaldığından işlem özünde teminatlı bir borçlanmadır.", zorluk="hard")

# 12 — sosyal sorumluluk
d, c = kavram("Sosyal sorumluluk", "Tarafsızlık ve belgelendirme", "Tam açıklama", "Kişilik", "Önemlilik")
P.q(KV,
    "Bir işletmenin yöneticileri, ana ortağın talebiyle kredi kuruluşlarına sunulacak finansal tabloları ortağın "
    "çıkarlarına göre, çalışanlar, kreditörler ve devlet gibi diğer ilgililerin bilgi ihtiyacını gözetmeden hazırlamak "
    f"istemektedir.\n\n{AYKIRI}",
    d, c,
    "Sosyal sorumluluk kavramına göre muhasebe bilgileri belli kişi veya grupların değil, toplumun tüm kesimlerinin "
    "çıkarlarını gözetecek biçimde tarafsız ve doğru olarak üretilmelidir.")

# 13 — temel kavramlardan biri değil (olumsuz)
P.q(KV,
    "Muhasebe Sistemi Uygulama Genel Tebliği’ni işleyen bir eğitimde katılımcılardan tebliğde sayılan on iki temel "
    "kavramı sıralamaları istenmiş, bir katılımcı listeye uluslararası kavramsal çerçeveden bir nitel özellik "
    "eklemiştir.\n\nAşağıdakilerden hangisi tebliğde sayılan temel kavramlardan biri değildir?",
    "Karşılaştırılabilirlik",
    ["Önemlilik", "Tutarlılık", "Özün önceliği", "İhtiyatlılık"],
    "MSUGT’deki on iki temel kavram sosyal sorumluluk, kişilik, işletmenin sürekliliği, dönemsellik, parayla ölçülme, "
    "maliyet esası, tarafsızlık ve belgelendirme, tutarlılık, tam açıklama, ihtiyatlılık, önemlilik ve özün önceliğidir; "
    "karşılaştırılabilirlik kavramsal çerçevenin nitel özelliğidir.", zorluk="hard")

# 14 — temel eşitlik (tablo)
v, b = 850_000, 320_000
P.q("Temel muhasebe eşitliği",
    "Yeni kurulan bir işletmenin yıl sonu hesap bakiyeleri şöyledir:\n\n| Hesap | Tutar (₺) |\n|---|---|\n"
    "| Kasa ve bankalar | 120.000 |\n| Ticari mallar | 230.000 |\n| Taşıtlar (net) | 500.000 |\n"
    "| Satıcılar | 180.000 |\n| Banka kredileri | 140.000 |\n\n"
    "Bu verilere göre işletmenin özkaynakları ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Varlıklar {tl(v)} ₺, özkaynaklar {tl(v - b)} ₺’dir.",
    [f"Varlıklar {tl(v)} ₺, özkaynaklar {tl(v + b)} ₺’dir.",
     f"Varlıklar {tl(v - 500_000)} ₺, özkaynaklar {tl(v - 500_000 - b)} ₺’dir.",
     f"Varlıklar {tl(v)} ₺, özkaynaklar {tl(v - 180_000)} ₺’dir.",
     f"Varlıklar {tl(v + b)} ₺, özkaynaklar {tl(v)} ₺’dir."],
    f"Varlıklar = 120.000 + 230.000 + 500.000 = {tl(v)} ₺; yabancı kaynaklar = 180.000 + 140.000 = {tl(b)} ₺. "
    f"Özkaynaklar = varlıklar − yabancı kaynaklar = {tl(v - b)} ₺.", zorluk="easy")

# 15 — işlemin eşitliğe etkisi: kredili mal alımı
P.q("Temel muhasebe eşitliği",
    "İşletme 60.000 ₺ + %20 KDV tutarında ticari malı 30 gün vadeyle satın almıştır. Alış bedelinin ödenmesi gelecek ay "
    "yapılacak, malın satışı ise henüz gerçekleşmemiştir; KDV indirim konusu yapılabilecektir.\n\nBu işlemin temel "
    "muhasebe eşitliğine etkisi aşağıdakilerden hangisidir?",
    "Varlıklar ve yabancı kaynaklar 72.000 ₺ artar.",
    ["Varlıklar 72.000 ₺ artar, özkaynaklar 72.000 ₺ artar.",
     "Varlıklar 60.000 ₺ artar, yabancı kaynaklar 72.000 ₺ artar, özkaynaklar azalır.",
     "Varlık hesapları arasında 72.000 ₺ değişim olur, toplam değişmez.",
     "Yabancı kaynaklar 72.000 ₺ artar, özkaynaklar 72.000 ₺ azalır."],
    "Ticari mallar (60.000 ₺) ve indirilecek KDV (12.000 ₺) varlıkları artırır; satıcılara borç 72.000 ₺ artar. "
    "Özkaynak değişmez, eşitlik korunur.")

# 16 — peşin gider
P.q("Temel muhasebe eşitliği",
    "İşletme aralık ayına ait idari personel eğitimi için bir danışmanlık firmasına 25.000 ₺ tutarı banka havalesiyle "
    "peşin ödemiştir. Eğitim aynı ay tamamlanmış, KDV bu soruda dikkate alınmayacaktır.\n\nBu işlemin temel muhasebe "
    "eşitliğine etkisi aşağıdakilerden hangisidir?",
    "Varlıklar ve özkaynaklar 25.000 ₺ azalır.",
    ["Varlıklar ve yabancı kaynaklar 25.000 ₺ azalır.",
     "Varlıklar 25.000 ₺ azalır, yabancı kaynaklar 25.000 ₺ artar.",
     "Varlık hesapları arasında 25.000 ₺ değişim olur, toplam değişmez.",
     "Özkaynaklar 25.000 ₺ azalır, yabancı kaynaklar 25.000 ₺ artar."],
    "Banka hesabı (varlık) azalır; gider dönem sonucunu, dolayısıyla özkaynağı azaltır. Yabancı kaynaklar etkilenmez.")

# 17 — borç ödemesi
P.q("Temel muhasebe eşitliği",
    "İşletme vadesi gelen 150.000 ₺ tutarındaki banka kredisi anapara taksidini, faiz tahakkuku daha önce ayrıca "
    "kaydedilmiş olduğundan, sadece anapara olarak vadesiz hesabından ödemiştir. Başka bir işlem yapılmamıştır.\n\nBu "
    "işlemin temel muhasebe eşitliğine etkisi aşağıdakilerden hangisidir?",
    "Varlıklar ve yabancı kaynaklar 150.000 ₺ azalır.",
    ["Varlıklar ve özkaynaklar 150.000 ₺ azalır.",
     "Yabancı kaynaklar 150.000 ₺ azalır, özkaynaklar 150.000 ₺ artar.",
     "Varlık hesapları arasında değişim olur, toplam değişmez.",
     "Varlıklar 150.000 ₺ azalır, yabancı kaynaklar değişmez."],
    "Anapara ödemesinde banka hesabı (varlık) ve banka kredileri (yabancı kaynak) aynı tutarda azalır; gider oluşmadığı "
    "için özkaynak değişmez.", zorluk="easy")

# 18 — alacak bakiye veren hesap
P.q(R,
    "Yıl sonu mizanını inceleyen stajyer, bazı aktif hesapların alacak bakiye vermesinin hata olup olmadığını "
    "sormaktadır. Mizanda 100 Kasa, 153 Ticari Mallar, 180 Gelecek Aylara Ait Giderler, 255 Demirbaşlar ve 257 Birikmiş "
    "Amortismanlar hesapları yer almaktadır.\n\nBu hesaplardan hangisinin alacak bakiye vermesi olağandır?",
    hk(257), [hk(100), hk(153), hk(180), hk(255)],
    "257 Birikmiş Amortismanlar düzenleyici (pasif karakterli) bir aktif hesaptır; artışları alacağa yazılır ve alacak "
    "bakiye verir. Diğer hesaplar borç bakiye verir; kasanın alacak bakiye vermesi kayıt hatasıdır.")

# 19 — borç bakiyeli pasif hesap
P.q(R,
    "Kuruluş aşamasındaki anonim şirketin mizanında 500 Sermaye hesabı 2.000.000 ₺ alacak, 501 Ödenmemiş Sermaye hesabı "
    "1.500.000 ₺ borç, 320 Satıcılar hesabı 90.000 ₺ alacak, 102 Bankalar hesabı 590.000 ₺ borç bakiye vermektedir.\n\n"
    "Bu hesaplardan hangisi pasif karakterli olmasına karşın borç bakiye veren düzenleyici hesaptır?",
    hk(501), [hk(500), hk(320), hk(102), hk(542)],
    "501 Ödenmemiş Sermaye, özkaynaklar grubunda yer alan ancak ortakların taahhüt borcunu izleyen düzenleyici (aktif "
    "karakterli) bir hesaptır; borç bakiye verir ve bilançoda sermayeden indirilir.")

# 20 — gelir tablosu indirim hesabı
P.q(R,
    "Yıl sonunda işletmenin gelir tablosu hesaplarından 600 Yurt İçi Satışlar 3.000.000 ₺ alacak, 610 Satıştan İadeler "
    "85.000 ₺, 611 Satış İskontoları 40.000 ₺ ve 621 Satılan Ticari Mallar Maliyeti 1.900.000 ₺ bakiye vermektedir.\n\n"
    "Aşağıdakilerden hangisi doğrudur?",
    "610 ve 611 borç bakiye verir, brüt satışlardan indirilir.",
    ["610 ve 611 alacak bakiye verir, brüt satışlara eklenir.",
     "621 alacak bakiye verir, net satışlara eklenir.",
     "610 borç, 611 alacak bakiye verir.",
     "600 borç bakiye verir, brüt satışlar böyle bulunur."],
    "Satış indirimleri (610, 611) gelir tablosunda brüt satışlardan indirilen, borç bakiyeli hesaplardır. Net satışlar "
    "3.000.000 − 85.000 − 40.000 = 2.875.000 ₺’dir; 621 de borç bakiye verir.")

# 21 — nazım hesaplar
P.q(R,
    "İşletme bir ihaleye katılmak için bankasından 750.000 ₺ tutarında teminat mektubu almış ve ihale makamına "
    "vermiştir. Mektup işletmenin varlık veya kaynaklarında doğrudan bir değişiklik yaratmamakla birlikte izlenmesi "
    "istenmektedir.\n\nBu tutar Tekdüzen Hesap Planı’nda hangi hesap sınıfında izlenir?",
    "9 Nazım hesaplar",
    ["8 Serbest hesaplar sınıfı", "3 Kısa vadeli yabancı kaynaklar", "2 Duran varlıklar sınıfı", "7 Maliyet hesapları"],
    "Varlık ve kaynaklarda değişiklik yaratmayan ancak izlenmesi gereken teminat mektubu, emanet ve benzeri işlemler 9 "
    "Nazım Hesaplar sınıfında izlenir; 8 sınıfı serbest bırakılmıştır.")

# 22 — hesap kodu yapısı
P.q(R,
    "Tekdüzen Hesap Planı’nda 153 Ticari Mallar hesabının kodunu inceleyen bir öğrenci, kodun her hanesinin ne ifade "
    "ettiğini sormaktadır. Birinci hane sınıfı, ilk iki hane birlikte grubu, üç hane birlikte ana hesabı "
    "göstermektedir.\n\n153 kodundaki “15” neyi ifade eder?",
    "Stoklar hesap grubunu",
    ["Dönen varlıklar hesap sınıfını",
     "Ticari mallar ana hesabını",
     "Ticari alacaklar hesap grubunu",
     "Stokların alt hesabını ve yardımcı hesabını"],
    "Hesap kodunda ilk hane sınıfı (1 Dönen Varlıklar), ilk iki hane grubu (15 Stoklar), üç hane ana hesabı (153 Ticari "
    "Mallar) gösterir; alt hesaplar ana hesap kodundan sonra gelir.", zorluk="easy")

# 23 — mizanı bozmayan hata (olumsuz)
P.q("Mizan denkliği",
    "Muhasebe servisinde ay içinde dört ayrı hata yapılmıştır: bir tahsilat sadece kasa hesabına borç yazılmış; bir "
    "ödemede borç 5.000 ₺, alacak 500 ₺ yazılmış; bir satış iki kez sadece alacak tarafa kaydedilmiş; 12.000 ₺’lik idari "
    "gider ise 760 hesabına borç yazılmıştır.\n\nBu hatalardan hangisi mizanın borç-alacak denkliğini bozmaz?",
    "İdari giderin 760 hesabına borç yazılması",
    ["Tahsilatın sadece kasa hesabına borç yazılması",
     "Ödemede borç ve alacak tutarlarının farklı yazılması",
     "Satışın iki kez sadece alacak tarafa kaydedilmesi",
     "Tahsilat ve ödeme hatalarının aynı ay yapılması"],
    "Yanlış hesaba ama doğru tarafa ve eşit tutarla yapılan kayıt mizan denkliğini bozmaz, mizan bu hatayı göstermez. "
    "Tek taraflı veya farklı tutarlı kayıtlar borç ve alacak toplamlarını farklılaştırır.", zorluk="hard")

# 24 — yanlış hesaba kayıt düzeltmesi
P.q(R,
    "Ay sonu kontrolünde, merkez ofisin 12.000 ₺’lik temizlik hizmeti giderinin yanlışlıkla 760 Pazarlama, Satış ve "
    "Dağıtım Giderleri hesabına borç yazıldığı anlaşılmıştır. Kaydın alacak tarafı doğrudur ve dönem henüz "
    "kapanmamıştır.\n\nDüzeltme kaydı aşağıdakilerden hangisidir?",
    K([(770, 12_000)], [(760, 12_000)]),
    [K([(760, 12_000)], [(770, 12_000)]),
     K([(770, 12_000)], [(100, 12_000)]),
     K([(770, 24_000)], [(760, 24_000)]),
     K([(681, 12_000)], [(760, 12_000)])],
    "Gider yanlış hesaba yazıldığından 760 alacaklandırılarak hata giderilir, doğru hesap 770 Genel Yönetim Giderleri "
    "borçlandırılır. Alacak tarafı doğru olduğundan ona dokunulmaz.")

# 25 — tutar hatası düzeltmesi
P.q(R,
    "Müşteriden kasaya yapılan 12.000 ₺’lik tahsilat, rakamların yer değiştirmesi sonucu 100 Kasa borç, 120 Alıcılar "
    "alacak olarak 21.000 ₺ şeklinde kaydedilmiştir. Hata aynı ay içinde kasa sayımı sırasında fark edilmiştir.\n\n"
    "Düzeltme kaydı aşağıdakilerden hangisidir?",
    K([(120, 9_000)], [(100, 9_000)]),
    [K([(100, 9_000)], [(120, 9_000)]),
     K([(120, 21_000)], [(100, 21_000)]),
     K([(197, 9_000)], [(100, 9_000)]),
     K([(120, 12_000)], [(100, 12_000)])],
    "Kayıt 9.000 ₺ fazla yapılmıştır: kasa 9.000 ₺ fazla, alıcılar 9.000 ₺ eksik görünür. Fazlalığı ters yönde kayıtla "
    "gidermek için 120 borç, 100 alacak 9.000 ₺ yazılır.")

# 26 — açılış kaydı
P.q(R,
    "Şahıs işletmesi olarak faaliyete başlayan işletmenin sahibi işletmeye 50.000 ₺ nakit, bankadaki 200.000 ₺ ve "
    "300.000 ₺ değerinde bir kamyonet koymuş; kamyonetin 100.000 ₺ taşıt kredisi borcunu da işletme üstlenmiştir. "
    "Kredi iki yılda ödenecektir.\n\nAçılış kaydı aşağıdakilerden hangisidir?",
    K([(100, 50_000), (102, 200_000), (254, 300_000)], [(400, 100_000), (500, 450_000)]),
    [K([(100, 50_000), (102, 200_000), (254, 300_000)], [(500, 550_000)]),
     K([(100, 50_000), (102, 200_000), (254, 300_000)], [(300, 100_000), (500, 450_000)]),
     K([(400, 100_000), (500, 450_000)], [(100, 50_000), (102, 200_000), (254, 300_000)]),
     K([(100, 50_000), (102, 200_000), (254, 200_000)], [(500, 450_000)])],
    "Varlıklar toplamı 550.000 ₺, üstlenilen kredi 100.000 ₺’dir; sermaye 450.000 ₺ olur. Kredi iki yıl vadeli "
    "olduğundan 400 Banka Kredileri hesabına alacak yazılır (bir yıl içinde ödenecek kısım dönem sonunda 303’e aktarılır).",
    zorluk="hard")

# 27 — brüt satış kârı
bs, iad, isk, smm = 1_000_000, 20_000, 10_000, 600_000
ns = bs - iad - isk
P.q("MSUGT: gelir tablosu ilkeleri",
    f"Yıl içinde işletmenin brüt satışları {tl(bs)} ₺, satıştan iadeleri {tl(iad)} ₺, satış iskontoları {tl(isk)} ₺, "
    f"satılan ticari mallar maliyeti {tl(smm)} ₺, pazarlama giderleri 110.000 ₺ ve genel yönetim giderleri 90.000 ₺’dir."
    "\n\nGelir tablosuyla ilgili aşağıdakilerden hangisi doğrudur?",
    f"Net satışlar {tl(ns)} ₺, brüt satış kârı {tl(ns - smm)} ₺’dir.",
    [f"Net satışlar {tl(bs)} ₺, brüt satış kârı {tl(bs - smm)} ₺’dir.",
     f"Net satışlar {tl(ns)} ₺, brüt satış kârı {tl(ns - smm - 200_000)} ₺’dir.",
     f"Net satışlar {tl(bs - iad)} ₺, brüt satış kârı {tl(bs - iad - smm)} ₺’dir.",
     f"Net satışlar {tl(ns + 30_000)} ₺, brüt satış kârı {tl(ns - smm - 110_000)} ₺’dir."],
    f"Net satışlar = {tl(bs)} − {tl(iad)} − {tl(isk)} = {tl(ns)} ₺; brüt satış kârı = {tl(ns)} − {tl(smm)} = "
    f"{tl(ns - smm)} ₺. Faaliyet giderleri düşülünce faaliyet kârı {tl(ns - smm - 200_000)} ₺ olur.")

# 28 — olağan kâr
fk, dfg, dfgi, fin = 170_000, 45_000, 25_000, 60_000
P.q("MSUGT: gelir tablosu ilkeleri",
    f"İşletmenin faaliyet kârı {tl(fk)} ₺’dir. Ayrıca diğer faaliyetlerden olağan gelir ve kârlar {tl(dfg)} ₺, olağan gider "
    f"ve zararlar {tl(dfgi)} ₺, finansman giderleri {tl(fin)} ₺ ve olağandışı gelirler 15.000 ₺ olarak "
    "gerçekleşmiştir.\n\nİşletmenin olağan kâr veya zararı ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Olağan kâr {tl(fk + dfg - dfgi - fin)} ₺’dir.",
    [f"Olağan kâr {tl(fk + dfg - dfgi - fin + 15_000)} ₺’dir.",
     f"Olağan kâr {tl(fk + dfg - dfgi)} ₺’dir.",
     f"Olağan kâr {tl(fk - dfgi - fin)} ₺’dir.",
     f"Olağan zarar {tl(fin + dfgi - dfg)} ₺’dir."],
    f"Olağan kâr = faaliyet kârı + diğer olağan gelirler − diğer olağan giderler − finansman giderleri = {tl(fk)} + "
    f"{tl(dfg)} − {tl(dfgi)} − {tl(fin)} = {tl(fk + dfg - dfgi - fin)} ₺. Olağandışı gelirler olağan kârdan sonra eklenir.",
    zorluk="hard")

# 29 — kasa hesabı bakiyesi (taraf değil, bakiye)
P.q("Hesap işleyişi",
    "Ay içinde işletmenin 100 Kasa hesabına ay başı bakiyesi dâhil toplam 180.000 ₺ borç, 135.000 ₺ alacak kaydı "
    "yapılmıştır. Ay sonunda yapılan sayımda kasada 45.000 ₺ nakit bulunmuş ve fark saptanmamıştır.\n\nKasa hesabının ay "
    "sonu bakiyesi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "45.000 ₺ borç bakiyesi verir.",
    ["45.000 ₺ alacak bakiyesi verir.",
     "315.000 ₺ borç bakiyesi verir.",
     "135.000 ₺ alacak bakiyesi verir.",
     "180.000 ₺ borç bakiyesi verir."],
    "Aktif karakterli kasa hesabında borç toplamı alacak toplamından büyüktür: 180.000 − 135.000 = 45.000 ₺ borç bakiye; "
    "sayım sonucu kayıtlarla uyumludur.", zorluk="easy")

# 30 — gider pusulası
P.q("VUK md. 235",
    "Zeytinyağı üreten işletme, vergi mükellefi olmayan bir çiftçiden 8.000 kg zeytini 280.000 ₺ bedelle satın almış ve "
    "bedeli çiftçinin banka hesabına göndermiştir. Çiftçi fatura düzenleyememektedir.\n\nİşletmenin bu alış için "
    "düzenlemesi gereken belge aşağıdakilerden hangisidir?",
    "Müstahsil makbuzu",
    ["Gider pusulası", "Serbest meslek makbuzu", "Sevk irsaliyesi", "Perakende satış fişi"],
    "Vergi mükellefi olmayan çiftçilerden zirai ürün alan ve defter tutan işletmeler müstahsil makbuzu düzenler; gider "
    "pusulası ise vergiden muaf esnaf ve mükellef olmayan kişilerden yapılan diğer mal ve hizmet alımlarında kullanılır.",
    zorluk="hard")

# 31 — gider pusulası (diğer)
P.q("VUK md. 234",
    "Bir işletme, vergi mükellefi olmayan bir kişiden kullanılmış bir çalışma masasını 6.500 ₺’ye satın almış, bedeli nakit "
    "ödemiştir. Satıcı herhangi bir ticari faaliyette bulunmamakta ve fatura düzenlememektedir; ürün zirai ürün "
    "değildir.\n\nİşletmenin bu alış için düzenlemesi gereken belge aşağıdakilerden hangisidir?",
    "Gider pusulası",
    ["Müstahsil makbuzu", "Serbest meslek makbuzu", "Perakende satış fişi", "Sevk irsaliyesi"],
    "Vergi mükellefi olmayan kişilerden yapılan mal ve hizmet alımlarında alıcı işletme gider pusulası düzenler ve bir "
    "nüshasını satıcıya verir; zirai ürün alımlarında ise müstahsil makbuzu kullanılır.")

# 32 — fatura düzenleme süresi
P.q("VUK md. 231",
    "Bir toptancı 10 Mart’ta müşterisine mal teslim etmiş, satış faturasını ise müşterinin talebiyle 25 Mart’ta "
    "düzenlemiştir. Vergi incelemesinde faturanın süresinde düzenlenip düzenlenmediği sorgulanmaktadır.\n\nVergi Usul "
    "Kanunu’na göre bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Fatura teslimden itibaren 7 gün içinde düzenlenmeliydi.",
    ["Fatura ayın sonuna kadar düzenlenebilirdi.",
     "Fatura teslimden itibaren 15 gün içinde düzenlenmeliydi.",
     "Fatura müşterinin talep ettiği tarihte düzenlenebilir.",
     "Fatura teslimden itibaren 30 gün içinde düzenlenmeliydi."],
    "VUK md. 231’e göre fatura, malın teslimi veya hizmetin yapıldığı tarihten itibaren azami yedi gün içinde "
    "düzenlenir; bu süre içinde düzenlenmeyen fatura hiç düzenlenmemiş sayılır.")

# 33 — yevmiye defteri özelliği
P.q("VUK md. 183-219",
    "Bilanço esasına göre defter tutan işletmenin muhasebe servisi, günlük işlemlerin hangi defterde tarih sırasıyla ve "
    "maddeler hâlinde yer aldığını, hangi defterde ise bu kayıtların hesaplara göre toplandığını yeni bir çalışana "
    "anlatmaktadır.\n\nAşağıdakilerden hangisi doğrudur?",
    "Yevmiye defteri tarih sırasıyla, büyük defter hesaplara göre tutulur.",
    ["Büyük defter tarih sırasıyla, yevmiye defteri hesaplara göre tutulur.",
     "Envanter defteri tarih sırasıyla, yevmiye defteri hesaplara göre tutulur.",
     "Yevmiye ve büyük defter aynı bilgiyi aynı düzende içerir.",
     "Büyük defter envanter sonuçlarını, yevmiye mizanı içerir."],
    "Yevmiye defteri işlemlerin tarih sırasıyla ve maddeler hâlinde kaydedildiği defterdir; büyük defter yevmiyedeki "
    "kayıtları hesaplara göre sınıflandırır. Envanter defteri envanter ve bilançoyu içerir.")

# 34 — kayıt süresi
P.q("VUK md. 219",
    "Bilanço esasına göre defter tutan işletmenin 3 Mart’ta gerçekleşen bir satış işlemi, muhasebe servisinin yoğunluğu "
    "nedeniyle 30 Nisan’da, yani işlemden 58 gün sonra yevmiye defterine kaydedilmiştir. İşlem belgeleri eksiksizdir ve "
    "mali tatil söz konusu değildir.\n\nVergi Usul Kanunu’na göre bu kayıt ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kayıt yasal kayıt süresi aşılarak yapılmıştır.",
    ["Kayıt 45 günlük yasal süre içinde yapılmıştır.",
     "Kayıt ay sonuna kadar yapılabileceğinden süresindedir.",
     "Kayıt için bir süre sınırı öngörülmemiştir.",
     "Kayıt 60 günlük yasal süre içinde yapılmıştır."],
    "VUK md. 219’a göre muameleler deftere 10 günden fazla geciktirilmeden kaydedilir; belgelerin muhasebeciye verildiği "
    "hâllerde bile kayıt belge tarihinden itibaren 45 günü aşamaz. 58 günlük gecikme her iki süreyi de aşar.",
    zorluk="hard")

# 35 — hesap dönemi
P.q("VUK md. 174",
    "Tarım ürünleri işleyen bir şirketin faaliyetleri hasat döneminde yoğunlaştığından, şirket hesap döneminin 1 Temmuz "
    "ile 30 Haziran arası olarak belirlenmesini istemektedir. Şirket takvim yılı esasına göre defter tutmaktadır.\n\n"
    "Vergi Usul Kanunu’na göre bu talep ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Hazine ve Maliye Bakanlığının izniyle özel hesap dönemi belirlenebilir.",
    ["Şirket genel kurul kararıyla hesap dönemini dilediği gibi belirleyebilir.",
     "Hesap dönemi takvim yılı dışında belirlenemez.",
     "Özel hesap dönemi sadece bankalar için mümkündür.",
     "Hesap dönemi ticaret sicili müdürlüğünün onayıyla değiştirilir."],
    "VUK md. 174’e göre hesap dönemi kural olarak takvim yılıdır; faaliyetin özelliği gerektiren hâllerde mükellefin "
    "talebi üzerine Hazine ve Maliye Bakanlığınca özel hesap dönemi tayin edilebilir.")

# 36 — tahakkuk esası
P.q(KV,
    "Aralık ayında bir müşteriye 150.000 ₺ + KDV’lik danışmanlık hizmeti tamamlanmış, bedelin tahsili izleyen yılın "
    "şubat ayında yapılacaktır. Aynı ay kullanılan elektriğin 9.000 ₺’lik faturası ise ocak ayında ödenecektir.\n\n"
    "Bu işlemlerin cari yıl gelir tablosuna yansıtılması ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Hizmet geliri ve elektrik gideri cari yılın sonucuna yansıtılır.",
    ["İkisi de tahsil ya da ödeme yapılan izleyen yılın sonucuna yansıtılır.",
     "Hizmet geliri izleyen yıla, elektrik gideri cari yıla yansıtılır.",
     "Hizmet geliri cari yıla, elektrik gideri izleyen yıla yansıtılır.",
     "Sadece nakit hareketi olan tutarlar gelir tablosuna yansıtılır."],
    "Tahakkuk esası ve dönemsellik kavramı gereği gelir ve giderler nakit hareketine göre değil gerçekleştikleri döneme "
    "göre kaydedilir; ikisi de aralık ayında gerçekleştiğinden cari yıla aittir.")

# 37 — dönen/duran varlık ayrımı
P.q(R,
    "İşletme 1 Aralık 2026’da sattığı bir makine karşılığında alıcıdan her biri 200.000 ₺ olan iki senet almıştır: "
    "birinin vadesi 1 Haziran 2027, diğerinin vadesi 1 Mart 2028’dir. Senetler ticari faaliyetten doğmuştur.\n\n2026 yılı "
    "sonu bilançosunda Mart 2028 vadeli senet hangi hesapta gösterilir?",
    hk(221), [hk(121), hk(101), hk(126), hk(240)],
    "Vadesi bilanço tarihinden itibaren bir yıldan uzun olan senetli ticari alacaklar duran varlıklarda 221 Alacak "
    "Senetleri hesabında gösterilir; Haziran 2027 vadeli senet ise dönen varlıklarda 121’de yer alır.")

# 38 — hesabın bilançodaki yeri
P.q(R,
    "Yıl sonu bilançosunu düzenleyen işletmenin mizanında 255 Demirbaşlar hesabı 400.000 ₺ borç, 257 Birikmiş "
    "Amortismanlar hesabı 160.000 ₺ alacak bakiyesi vermektedir. Demirbaşların tamamı idari amaçla "
    "kullanılmaktadır.\n\nBu hesapların bilançoda gösterimi ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Duran varlıklarda 400.000 ₺ eksi 160.000 ₺ olarak gösterilir.",
    ["Demirbaşlar aktifte, birikmiş amortismanlar pasifte gösterilir.",
     "Sadece net tutar olan 240.000 ₺ aktifte gösterilir.",
     "Birikmiş amortismanlar gelir tablosunda gider olarak gösterilir.",
     "Demirbaşlar dönen varlıklarda, amortisman duran varlıklarda yer alır."],
    "257 düzenleyici bir aktif hesaptır; bilançoda maddi duran varlıklar grubunda ilgili varlıkların altında eksi olarak "
    "gösterilir ve net değer 240.000 ₺ olur.")

# 39 — satışın hasılat olarak kaydı: tahakkuk (yevmiye)
P.q(R,
    "Hizmet işletmesi aralık ayında bir müşterisine 80.000 ₺ + %20 KDV tutarında bakım hizmeti vermiş ve faturasını "
    "düzenlemiştir. Müşteri bedeli ocak ayında ödeyecektir; hizmet işletmenin esas faaliyet konusudur.\n\n"
    "Aralık ayında yapılacak günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(120, 96_000)], [(600, 80_000), (391, 16_000)]),
    [K([(181, 96_000)], [(600, 80_000), (391, 16_000)]),
     K([(120, 96_000)], [(380, 80_000), (391, 16_000)]),
     K([(120, 96_000)], [(649, 80_000), (391, 16_000)]),
     K([(120, 80_000)], [(600, 80_000)])],
    "Hizmet tamamlanıp fatura düzenlendiğinden gelir cari döneme aittir ve alacak doğmuştur: 120 Alıcılar 96.000 ₺ borç; "
    "600 Yurt İçi Satışlar 80.000 ₺ ve 391 Hesaplanan KDV 16.000 ₺ alacak.", zorluk="easy")

# 40 — hesap işleyişi: pasif hesapta artış
P.q("Hesap işleyişi",
    "İşletme bir tedarikçiden 45.000 ₺’lik mal almış, bedelin tamamı için 90 gün vadeli bir bono düzenleyerek "
    "tedarikçiye vermiştir. KDV bu soruda dikkate alınmayacak, mal ambara girmiştir.\n\nBu işlemin kaydında borç senetleri "
    "hesabı ile ilgili aşağıdakilerden hangisi doğrudur?",
    T(321, "alacak", 45_000),
    [T(321, "borç", 45_000), T(121, "borç", 45_000), T(320, "alacak", 45_000), T(103, "alacak", 45_000)],
    "Borç senetleri pasif karakterli bir hesaptır; artışları alacak tarafına yazılır: 153 Ticari Mallar borç, 321 Borç "
    "Senetleri alacak 45.000 ₺. Senetsiz borç 320’de, çek 103’te izlenir.", zorluk="easy")

# 41 — şahıs işletmesine taşıt koyma
P.q(R,
    "Kuruluşundan bir yıl sonra şahıs işletmesinin sahibi, kendi adına kayıtlı ve piyasa değeri 350.000 ₺ olan hafif "
    "ticari aracını sermaye artırımı olarak işletmeye devretmiştir. Araç işletmenin dağıtım işlerinde kullanılacaktır."
    "\n\nBu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(254, 350_000)], [(500, 350_000)]),
    [K([(254, 350_000)], [(331, 350_000)]),
     K([(500, 350_000)], [(254, 350_000)]),
     K([(760, 350_000)], [(500, 350_000)]),
     K([(254, 350_000)], [(649, 350_000)])],
    "Ayni sermaye konulması hem varlıkları hem özkaynağı artırır: 254 Taşıtlar borç, 500 Sermaye alacak 350.000 ₺. "
    "Araç iade edilmeyeceği için ortağa borç (331) doğmaz.", zorluk="easy")

# 42 — kapanan-açılan hesaplar: gelir tablosu hesapları geçici
P.q("Hesap işleyişi",
    "Yıl sonu kapanış işlemlerinde muhasebe müdürü, bazı hesapların yeni yıla bakiyeyle devredeceğini, bazılarının ise "
    "her yıl sıfırlanacağını açıklamaktadır. Sorulan hesaplar 102 Bankalar, 320 Satıcılar, 500 Sermaye, 600 Yurt İçi "
    "Satışlar ve 257 Birikmiş Amortismanlar’dır.\n\nBu hesaplardan hangisi yeni yıla bakiyeyle devretmez?",
    hk(600), [hk(102), hk(320), hk(500), hk(257)],
    "Gelir tablosu hesapları (6 grubu) dönem sonucunu bulmak için 690 hesabına kapatılır ve yeni yıla bakiye taşımaz; "
    "bilanço hesapları (102, 320, 500, 257) yeni yıla açılış kaydıyla devreder.")

# 43 — önemlilik: finansal tablolarda birleştirme
d, c = kavram("Önemlilik", "Tam açıklama", "Tutarlılık", "Özün önceliği", "Maliyet esası")
P.q(KV,
    "Toplam varlıkları 90.000.000 ₺ olan işletme, bilançosunda tutarları birkaç bin lirayı geçmeyen verilen depozitolar, "
    "iş avansları ve personel avanslarını ayrı ayrı göstermek yerine “diğer dönen varlıklar” başlığında toplu olarak "
    f"sunmuştur.\n\n{HANGI}",
    d, c,
    "Önemlilik kavramına göre tek başına karar almayı etkilemeyecek küçük tutarlı kalemler benzerleriyle birleştirilerek "
    "sunulabilir; önemli kalemler ise ayrıca gösterilir.")

# 44 — ihtiyatlılık aşırı uygulama (gizli yedek)
P.q(KV,
    "Kârı yüksek çıkan bir işletmenin yönetimi, gelecek yıllarda kârı dengelemek amacıyla gerçekçi tahminlerin çok "
    "üzerinde, 1.200.000 ₺ şüpheli alacak karşılığı ayırmak istemektedir. Oysa alacakların geçmiş tahsil oranları bu "
    "tutarın dörtte birinin bile riskli olmadığını göstermektedir.\n\nBu uygulama ile ilgili aşağıdakilerden hangisi "
    "doğrudur?",
    "İhtiyatlılık kavramı gizli yedek yaratmayı haklı kılmaz.",
    ["İhtiyatlılık kavramı gereği karşılık ne kadar yüksekse o kadar doğrudur.",
     "Önemlilik kavramı gereği karşılık tutarı yönetimce belirlenir.",
     "Tutarlılık kavramı gereği karşılık her yıl aynı tutarda ayrılmalıdır.",
     "Maliyet esası kavramı gereği karşılık ayrılmaz."],
    "İhtiyatlılık muhtemel kayıplar için makul karşılık ayrılmasını gerektirir; ancak bu kavram gerçek dışı karşılık "
    "ayırarak gizli yedek yaratmanın ve kârı dönemler arasında kaydırmanın gerekçesi olamaz.", zorluk="hard")

# 45 — işletmenin sürekliliği bozulduğunda
P.q(KV,
    "Genel kurul, borçlarını ödeyemeyen şirketin altı ay içinde tasfiye edilmesine karar vermiştir. Şirketin makine ve "
    "binalarının defter değeri 6.400.000 ₺, tasfiye hâlinde elde edilmesi beklenen tutar ise 3.900.000 ₺’dir.\n\n"
    "Finansal tabloların hazırlanması ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Süreklilik varsayımı geçersiz olduğundan uygun esas açıklanarak uygulanır.",
    ["Varlıklar defter değerleriyle gösterilmeye devam eder, açıklama gerekmez.",
     "Tasfiye kararı finansal tabloları etkilemez, sonraki yıl dikkate alınır.",
     "Varlıklar maliyet bedeline yükseltilerek gösterilir.",
     "Sadece dipnotta tasfiye kararından söz edilir, ölçüm değişmez."],
    "İşletmenin sürekliliği kavramı faaliyetlerin süresiz devamını varsayar; tasfiye kararıyla bu varsayım geçersizleşir. "
    "Tablolar farklı bir esasla (tasfiye değerleri) hazırlanır ve bu durum açıklanır.", zorluk="hard")

# 46 — belgelendirme: serbest meslek makbuzu
P.q("VUK md. 236",
    "Bir şirket serbest çalışan bir mimardan ofis tadilat projesi için hizmet almış ve 60.000 ₺ brüt ücret ödemeyi "
    "kabul etmiştir. Mimar serbest meslek faaliyeti nedeniyle gelir vergisi mükellefidir.\n\nBu hizmet karşılığında "
    "düzenlenmesi gereken belge ve düzenleyeni ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Mimar serbest meslek makbuzu düzenler.",
    ["Şirket gider pusulası düzenler.",
     "Şirket müstahsil makbuzu düzenler.",
     "Mimar sevk irsaliyesi düzenler.",
     "Şirket serbest meslek makbuzu düzenler."],
    "Serbest meslek erbabı mesleki faaliyetine ilişkin tahsil ettiği ücret için iki nüsha serbest meslek makbuzu "
    "düzenleyerek bir nüshasını müşteriye verir; belgeyi hizmeti veren düzenler.", zorluk="easy")

# 47 — muhasebenin fonksiyonları
P.q("Muhasebenin fonksiyonları",
    "Yeni kurulan bir işletmede muhasebe servisi ay boyunca işlemlere ait belgeleri toplamış, bunları yevmiyeye "
    "kaydetmiş, büyük defterde hesaplara göre ayırmış, ay sonunda mizan ve finansal tablolar hazırlamış, ardından "
    "oranlarla yorumlayarak yönetime sunmuştur.\n\nMizan ve finansal tabloların hazırlanması muhasebenin hangi "
    "fonksiyonudur?",
    "Özetleme",
    ["Kaydetme", "Sınıflandırma", "Analiz ve yorumlama", "Belgeleme"],
    "Muhasebenin fonksiyonları kaydetme, sınıflandırma, özetleme ve analiz-yorumlamadır. Mizan ve finansal tabloların "
    "düzenlenmesi özetleme; büyük defterde hesaplara ayırma sınıflandırmadır.", zorluk="easy")

# 48 — çift taraflı kayıt
P.q("Hesap işleyişi",
    "İşletme bir makineyi 400.000 ₺’ye satın almış; bedelin 100.000 ₺’sini bankadan havaleyle ödemiş, kalanı için 12 ay "
    "vadeli bir senet vermiştir. KDV bu soruda dikkate alınmayacaktır.\n\nBu işlemin çift taraflı kayıt yöntemine göre "
    "kaydı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Bir hesaba 400.000 ₺ borç, iki hesaba toplam 400.000 ₺ alacak yazılır.",
    ["Bir hesaba 400.000 ₺ borç, bir hesaba 100.000 ₺ alacak yazılır.",
     "İki hesaba toplam 400.000 ₺ borç, bir hesaba 400.000 ₺ alacak yazılır.",
     "Bir hesaba 400.000 ₺ borç, iki hesaba toplam 300.000 ₺ alacak yazılır.",
     "Üç hesaba toplam 800.000 ₺ borç ve alacak yazılır, fark kasaya yazılır."],
    "Makine 253 hesabına 400.000 ₺ borç; 102 Bankalar 100.000 ₺ ve 321 Borç Senetleri 300.000 ₺ alacak yazılır. Her "
    "kayıtta borç ve alacak toplamları eşittir.")

# 49 — bilanço ve gelir tablosu bağlantısı
P.q("Temel muhasebe eşitliği",
    "Yıl başında özkaynakları 1.200.000 ₺ olan işletmeye yıl içinde ortaklar 300.000 ₺ ek sermaye koymuş, ortaklara "
    "150.000 ₺ kâr payı dağıtılmıştır. Yıl sonunda özkaynaklar 1.620.000 ₺ olarak belirlenmiştir; başka özkaynak hareketi "
    "yoktur.\n\nİşletmenin dönem net kârı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Dönem net kârı 270.000 ₺’dir.",
    ["Dönem net kârı 420.000 ₺’dir.",
     "Dönem net kârı 120.000 ₺’dir.",
     "Dönem net kârı 570.000 ₺’dir.",
     "Dönem net zararı 30.000 ₺’dir."],
    "Dönem sonu özkaynak = dönem başı + sermaye artışı − dağıtılan kâr + net kâr: 1.620.000 = 1.200.000 + 300.000 − "
    "150.000 + net kâr → net kâr 270.000 ₺.", zorluk="hard")

# 50 — dönemsellik: gelir tahsil (380)
d, c = kavram("Dönemsellik", "Maliyet esası", "İhtiyatlılık", "Tam açıklama", "Kişilik")
P.q(KV,
    "Bir yazılım işletmesi 1 Aralık’ta bir yıllık bakım hizmeti için müşterisinden 120.000 ₺ tahsil etmiştir. İşletme bu "
    "tutarın 10.000 ₺’sini aralık ayı geliri olarak kaydetmiş, kalan 110.000 ₺’yi gelecek aylara ait gelir olarak "
    f"izlemiştir.\n\n{HANGI}",
    d, c,
    "Tahsil edilen tutarın sadece cari döneme düşen kısmı o dönemin geliridir; kalanı hizmet verildikçe izleyen aylara "
    "aktarılır. Bu, dönemsellik kavramının gereğidir.")

# 51 — tutarlılık: değişiklik açıklaması
P.q(KV,
    "Stoklarını beş yıldır FIFO ile değerleyen işletme, maliyetleri daha gerçekçi yansıttığı gerekçesiyle bu yıl "
    "ağırlıklı ortalama yöntemine geçmiş ve bu değişiklik nedeniyle dönem kârının 180.000 ₺ azaldığını hesaplamıştır."
    "\n\nBu değişiklikle ilgili aşağıdakilerden hangisi doğrudur?",
    "Değişiklik yapılabilir; nedeni ve etkisi açıklanmalıdır.",
    ["Tutarlılık kavramı gereği yöntem asla değiştirilemez.",
     "Değişiklik yapılabilir, açıklanması gerekmez.",
     "Değişiklik sadece kâr artırıyorsa yapılabilir.",
     "Değişiklik yapılırsa önceki beş yılın defterleri yeniden açılmalıdır."],
    "Tutarlılık kavramı politikaların sürekli uygulanmasını ister ancak haklı nedenle değişikliğe izin verir; bu durumda "
    "değişikliğin nedeni ve finansal etkisi dipnotlarda açıklanmalıdır.")

# 52 — maliyet esası: satın alma maliyeti
P.q(KV,
    "İşletme 700.000 ₺ liste fiyatlı bir makineyi pazarlıkla 640.000 ₺’ye satın almıştır. Aynı gün bir rakip firma "
    "makineyi 720.000 ₺’ye satın almayı teklif etmiş, işletme teklifi reddetmiştir. Makinenin taşıma ve kurulum gideri "
    "20.000 ₺’dir.\n\nMaliyet esası kavramına göre makine hangi tutarla kaydedilir?",
    "660.000 ₺ ile kaydedilir.",
    ["640.000 ₺ ile kaydedilir.",
     "700.000 ₺ ile kaydedilir.",
     "720.000 ₺ ile kaydedilir.",
     "740.000 ₺ ile kaydedilir."],
    "Maliyet esası kavramına göre varlıklar edinme maliyetiyle kaydedilir: fiilen ödenen 640.000 ₺ ile kullanıma hazır "
    "hâle getirme giderleri 20.000 ₺, toplam 660.000 ₺. Liste fiyatı ve teklif edilen tutar dikkate alınmaz.")

# 53 — THP sınıfları: maliyet hesapları
P.q(R,
    "Üretim işletmesinin muhasebe servisi, üretimde kullanılan hammadde, işçilik ve genel üretim giderlerini dönem "
    "içinde ayrı hesaplarda toplamak istemektedir. İşletme bu amaçla Tekdüzen Hesap Planı’ndaki ilgili sınıfı "
    "kullanacaktır.\n\nBu giderler Tekdüzen Hesap Planı’nın hangi hesap sınıfında izlenir?",
    "7 Maliyet hesapları",
    ["6 Gelir tablosu hesapları", "1 Dönen varlıklar", "9 Nazım hesaplar", "8 Serbest hesaplar"],
    "Üretim ve faaliyet giderleri 7 Maliyet Hesapları sınıfında (7/A veya 7/B seçeneğine göre) toplanır; 6 grubu gelir "
    "tablosu hesaplarını, 9 grubu nazım hesapları içerir.", zorluk="easy")

# 54 — kasa alacak bakiye (hata)
P.q("Hesap işleyişi",
    "Ay sonu mizanında 100 Kasa hesabı 3.400 ₺ alacak bakiye vermiştir. Kasada fiziken nakit bulunmaktadır ve işletme "
    "kasadan avans çekme gibi bir uygulama yapmamaktadır.\n\nBu durum ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kayıt hatası vardır; kasa alacak bakiye veremez.",
    ["Kasa hesabı olağan olarak alacak bakiye verebilir.",
     "Kasada 3.400 ₺ fazla para olduğunu gösterir.",
     "Tutar dönem sonunda 689’a aktarılarak kapatılır.",
     "Kasa hesabı pasif karakterli olduğundan durum olağandır."],
    "Kasa aktif karakterli bir hesaptır ve kasadan fiilen var olandan fazla para çıkamayacağı için alacak bakiye veremez; "
    "alacak bakiye kayıt hatasına işaret eder ve hatalı kaydın bulunup düzeltilmesi gerekir.")

# 55 — gelir tablosunda net kâr hesaplama
ok, odg, odz, vk = 300_000, 20_000, 40_000, 70_000
P.q("MSUGT: gelir tablosu ilkeleri",
    f"İşletmenin olağan kârı {tl(ok)} ₺’dir. Ayrıca olağandışı gelir ve kârlar {tl(odg)} ₺, olağandışı gider ve zararlar "
    f"{tl(odz)} ₺’dir. Dönem kârı üzerinden hesaplanan vergi ve diğer yasal yükümlülük karşılıkları {tl(vk)} ₺’dir.\n\n"
    "Dönem net kârı ile ilgili aşağıdakilerden hangisi doğrudur?",
    f"Dönem kârı {tl(ok + odg - odz)} ₺, dönem net kârı {tl(ok + odg - odz - vk)} ₺’dir.",
    [f"Dönem kârı {tl(ok)} ₺, dönem net kârı {tl(ok - vk)} ₺’dir.",
     f"Dönem kârı {tl(ok + odg)} ₺, dönem net kârı {tl(ok + odg - vk)} ₺’dir.",
     f"Dönem kârı {tl(ok + odg - odz)} ₺, dönem net kârı {tl(ok + odg - odz)} ₺’dir.",
     f"Dönem kârı {tl(ok - odz)} ₺, dönem net kârı {tl(ok - odz - vk)} ₺’dir."],
    f"Dönem kârı = olağan kâr + olağandışı gelirler − olağandışı giderler = {tl(ok + odg - odz)} ₺; dönem net kârı = "
    f"dönem kârı − vergi karşılıkları = {tl(ok + odg - odz - vk)} ₺.")

# 56 — özün önceliği: finansal kiralama
d, c = kavram("Özün önceliği", "Maliyet esası", "Tutarlılık", "Dönemsellik", "Parayla ölçülme")
P.q(KV,
    "İşletme bir üretim makinesini beş yıl süreyle kiralamıştır. Kira süresi makinenin ekonomik ömrüne eşittir ve süre "
    "sonunda makinenin mülkiyeti sembolik bir bedelle işletmeye geçecektir. İşletme makineyi varlık, kira borcunu "
    f"yükümlülük olarak kaydetmiştir.\n\n{HANGI}",
    d, c,
    "Hukuki biçim kiralama olsa da makinenin riskleri ve yararları işletmeye geçmiştir; işlem özünde kredili alımdır. "
    "Özün önceliği kavramı gereği varlık ve yükümlülük olarak kaydedilir.")

# 57 — büyük defter bakiyesi (tablo)
P.q("Hesap işleyişi",
    "İşletmenin 320 Satıcılar hesabına ait büyük defter hareketleri şöyledir:\n\n| Tarih | Borç (₺) | Alacak (₺) |\n"
    "|---|---|---|\n| 1 Mart (devir) | — | 85.000 |\n| 9 Mart | — | 60.000 |\n| 18 Mart | 70.000 | — |\n"
    "| 27 Mart | 15.000 | — |\n\nAy sonunda Satıcılar hesabı ile ilgili aşağıdakilerden hangisi doğrudur?",
    "60.000 ₺ alacak bakiye verir.",
    ["60.000 ₺ borç bakiye verir.",
     "145.000 ₺ alacak bakiye verir.",
     "85.000 ₺ borç bakiye verir.",
     "230.000 ₺ alacak bakiye verir."],
    "Alacak toplamı 85.000 + 60.000 = 145.000 ₺, borç toplamı 70.000 + 15.000 = 85.000 ₺’dir. Pasif karakterli hesap "
    "145.000 − 85.000 = 60.000 ₺ alacak bakiye verir: satıcılara olan borç.", zorluk="easy")

# 58 — yevmiye kaydı: ücret tahsili? — işletme hesabından kişisel harcama (131)
P.q(R,
    "Tek ortaklı bir limited şirkette ortak, kendi evinin kira bedeli olan 22.000 ₺’yi şirketin banka hesabından ödemiş; "
    "yıl sonunda bu tutarın kâr payından mahsup edileceği kararlaştırılmıştır. Ödeme şirket faaliyetiyle ilgili "
    "değildir.\n\nBu ödemeye ilişkin günlük defter kaydı aşağıdakilerden hangisidir?",
    K([(131, 22_000)], [(102, 22_000)]),
    [K([(770, 22_000)], [(102, 22_000)]),
     K([(331, 22_000)], [(102, 22_000)]),
     K([(500, 22_000)], [(102, 22_000)]),
     K([(180, 22_000)], [(102, 22_000)])],
    "Kişilik kavramı gereği ortağın özel harcaması şirket gideri değildir; şirketin ortaktan alacağı olarak 131 "
    "Ortaklardan Alacaklar hesabına borç, 102 Bankalar hesabına alacak yazılır.")

# 59 — THP 5 grubu: yedekler
P.q(R,
    "Genel kurul kararıyla dönem kârından ayrılan 40.000 ₺ yasal yedek, esas sözleşme gereği ayrılan 25.000 ₺ statü "
    "yedeği ve serbestçe kullanılmak üzere ayrılan 60.000 ₺ olağanüstü yedek kayda alınacaktır.\n\nEsas sözleşme gereği "
    "ayrılan yedek hangi hesapta izlenir?",
    hk(541), [hk(540), hk(542), hk(549), hk(570)],
    "Esas sözleşme hükmüne göre ayrılan yedekler 541 Statü Yedekleri, kanun gereği ayrılanlar 540 Yasal Yedekler, "
    "serbestçe ayrılanlar 542 Olağanüstü Yedekler hesabında izlenir.", zorluk="easy")

# 60 — geçici hesap (197/397) niteliği
P.q("Hesap işleyişi",
    "Yıl içinde kasa sayımında bulunan 1.250 ₺ noksan, nedeni araştırılmak üzere geçici bir hesaba alınmıştır. Muhasebe "
    "müdürü bu hesabın dönem sonunda bakiye vermemesi, nedeni bulunamazsa ilgili gelir tablosu hesabına aktarılması "
    "gerektiğini hatırlatmıştır.\n\nBu tutarın geçici olarak izlendiği hesap aşağıdakilerden hangisidir?",
    hk(197), [hk(397), hk(689), hk(135), hk(196)],
    "Nedeni belirlenemeyen sayım noksanları geçici olarak 197 Sayım ve Tesellüm Noksanları hesabında izlenir; neden "
    "anlaşılınca ilgili hesaba, anlaşılamazsa dönem sonunda 689 hesabına aktarılır. 397 fazlalar içindir.", zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
