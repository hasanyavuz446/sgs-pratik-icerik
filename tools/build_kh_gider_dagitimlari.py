# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Maliyet Muhasebesi / Gider Dağıtımları (60 soru = 3×20).
Doğru şık KISA, çeldiriciler UZUN. explanation'da harf atıfı YOK.
Aritmetik python'da hesaplanır. Yıla bağlı oran/tutar YOK."""
import json, random, re

L, T, LBL = "maliyet_muhasebesi", "gider_dagitimlari", "Gider Dağıtımları"
PREFIX, SEED = "kh-mal-dagitim", 20260903
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik/questions_topic_gider_dagitimlari_2026.json"

Q = []


def q(stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why,
                  ref=ref, difficulty=difficulty))


def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9:
        v = round(v)
    return f"{v:,}".replace(",", ".")


# ── A. Birinci dağıtım ve dağıtım anahtarları (20) ────────────────────────
q("Fabrikanın yalnız Pres bölümünde kullanılan bir makinenin amortismanı bölüm bazında güvenilir biçimde belirlenebiliyorsa birinci dağıtımda nasıl işlem görür?",
  "Doğrudan Pres gider yerine yüklenir",
  ["Ortak gider kabul edilerek fabrikadaki bütün gider yerlerine kapladıkları alan oranında dağıtılır",
   "Üretimle ilgili olmasına rağmen genel yönetim gideri sayılarak dönem sonucuna doğrudan aktarılır",
   "İkinci dağıtıma kadar hiçbir gider yerine alınmadan yardımcı gider yerinde geçici olarak bekletilir",
   "Mamul bazında izlenemediği için satış gideri kabul edilerek pazarlama bölümlerine paylaştırılır"],
  "Bir gider hangi gider yerinde doğduğuna doğrudan ve ekonomik biçimde bağlanabiliyorsa dağıtım anahtarı kullanılmadan o gider yerine yüklenir.",
  "1 Sıra No.lu MSUGT - 7/A seçeneği, giderlerin gider yerleri itibarıyla izlenmesi", "easy")

q("Aynı fabrika binasında bulunan üç üretim bölümüne ait ortak kira giderinin tek bir bölüme doğrudan yazılmamasının temel nedeni nedir?",
  "Birden çok gider yerinin ortak kaynak tüketmesidir",
  ["Kira giderinin üretimle hiçbir ilişkisi bulunmadığından stok maliyetine alınmasının yasak olmasıdır",
   "Kiranın yalnız satış hacmine bağlı değişken bir gider olması ve üretim bölümlerini etkilememesidir",
   "Kira tutarının nakden ödenmemiş olması nedeniyle henüz maliyet veya gider doğurmamasıdır",
   "Bina kirasının mamullere doğrudan ilk madde ve malzeme gideri olarak yüklenmesi gereğidir"],
  "Ortak fabrika kirası birden çok gider yerinin kullandığı kaynaktan doğar. Bu nedenle tüketimi temsil eden uygun bir anahtarla ilgili gider yerlerine dağıtılır.",
  "TMS 2 par. 12 - dolaylı üretim maliyetlerinin sistematik dağıtımı")

q("Bir dağıtım havuzunda hem alanla ilişkili kira hem makine çalışmasıyla ilişkili enerji gideri birlikte tutuluyorsa daha güvenilir dağıtım için hangi işlem yapılmalıdır?",
  "Giderler ayrı havuzlara ayrılıp farklı anahtarlarla dağıtılmalıdır",
  ["Bütün giderler tek havuzda bırakılıp yalnız en yüksek tutarlı giderin anahtarı kullanılmalıdır",
   "Herhangi bir tüketim ilişkisi aranmadan toplam tutar gider yerlerine eşit olarak bölünmelidir",
   "Kira ve enerji üretimle ilgili olduğundan dağıtılmadan doğrudan mamullere eşit yüklenmelidir",
   "İki gider de stok maliyetinden çıkarılıp genel yönetim gideri olarak dönem sonucuna aktarılmalıdır"],
  "Farklı maliyet etkenlerine sahip giderlerin homojen havuzlarda toplanması gerekir. Kira için alan, enerji için ölçülen tüketim gibi ayrı anahtarlar daha doğru sonuç verir.",
  "TMS 2 par. 12 - sabit ve değişken genel üretim giderlerinin sistematik dağıtımı", "hard")

q("Fabrika binası sigorta giderinin üretim bölümlerine dağıtımında bölümlerin sigortalanan varlık değerleri güvenilir biçimde ölçülebiliyorsa hangi anahtar en uygundur?",
  "Sigortalanan varlık değerleri",
  ["Bölümlerde çalışan personelin toplam kıdem yılı ve ücretlerinin birlikte oluşturduğu tutar",
   "Üretilen mamullerin satış fiyatları ile dönem sonu stok miktarlarının çarpımından bulunan değer",
   "Bölümlerin kullandığı doğrudan ilk madde miktarı ile satın alma vadelerinin toplamı",
   "Her bölümün satış bölümüne gönderdiği mamul sayısından bağımsız olarak eşit pay yöntemi"],
  "Dağıtım anahtarı giderin oluşumuyla neden-sonuç veya fayda ilişkisi kurmalıdır. Sigorta gideri açısından sigortalanan varlık değeri uygun ölçüdür.",
  "TMS 2 par. 12 - sistematik ve tutarlı dağıtım")

q("Elektrik tüketimi her gider yerinde ayrı sayaçla ölçülüyorsa ortak elektrik giderinin dağıtımında hangi veri öncelikle kullanılmalıdır?",
  "Sayaçlarla ölçülen kilovatsaat tüketimi",
  ["Gider yerlerinin dönem sonunda elde ettiği muhasebe kârlarının birbirine oranı kullanılmalıdır",
   "Her gider yerindeki çalışanların yaş ortalaması ve kıdem toplamı esas alınmalıdır",
   "Elektrik kullanımı ölçülse bile gider bütün bölümlere hiçbir anahtar olmadan eşit dağıtılmalıdır",
   "Üretim miktarı dikkate alınmadan yalnız bölüm yöneticilerinin takdir ettiği yüzdeler kullanılmalıdır"],
  "Doğrudan ölçülen elektrik tüketimi, gider yerlerinin kaynaktan yararlanmasını en güçlü biçimde yansıtır; tahmini veya ilgisiz anahtarlara göre önceliklidir.",
  "TMS 2 par. 12 - değişken genel üretim giderlerinin sistematik dağıtımı")

q("Birinci dağıtımda fabrika aydınlatma gideri için alan, yemekhane gideri için personel sayısı kullanılması hangi ilkeyi gösterir?",
  "Her gider için tüketimi temsil eden ayrı anahtar seçilmesini",
  ["Bütün gider türlerinin yalnız üretim miktarına dayanan tek bir anahtarla dağıtılması gerektiğini",
   "Dağıtım anahtarlarının giderin oluşumuyla ilişkisiz ve her dönem rastgele değiştirilebilir olduğunu",
   "Yardımcı gider yerlerinin maliyetlerinin birinci dağıtımda doğrudan mamullere yüklenmesini",
   "Üretim dışı giderlerin fabrika giderleriyle birlikte stoklara eşit olarak paylaştırılmasını"],
  "Farklı giderler farklı kaynak tüketimlerinden doğar. Alan aydınlatma kullanımını, personel sayısı yemekhane hizmetinden yararlanmayı temsil edebilir.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik dağıtımı")

q("Birinci dağıtım uygulamasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Doğrudan izlenebilen gider ilgili gider yerine yüklenir\n\nII. Ortak gider uygun dağıtım anahtarıyla gider yerlerine paylaştırılır\n\nIII. Yardımcı gider yerlerinde biriken tutarlar bu aşamada doğrudan mamullere yüklenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Birinci dağıtımda doğrudan giderler ilgili gider yerine yüklenir ve ortak giderler uygun anahtarla dağıtılır. Yardımcı gider yeri maliyetlerinin esas yerlere aktarılması ikinci dağıtımın konusudur.",
  "1 Sıra No.lu MSUGT - gider yerleri; TMS 2 par. 12")

kira, alan_p, alan_m, alan_b = 288_000, 540, 360, 300
toplam_alan = alan_p + alan_m + alan_b
pres_kira = kira * alan_p / toplam_alan
assert toplam_alan == 1_200 and pres_kira == 129_600
q(f"Ortak fabrika kirası {tr(kira)} TL'dir. Pres, Montaj ve Bakım gider yerlerinin alanları sırasıyla {tr(alan_p)}, {tr(alan_m)} ve {tr(alan_b)} m²'dir. Alan esasına göre Pres gider yerine düşen kira payı kaç TL'dir?",
  f"{tr(pres_kira)} TL",
  [f"{tr(kira*alan_m/toplam_alan)} TL",
   f"{tr(kira*alan_b/toplam_alan)} TL",
   f"{tr(kira*(alan_p+alan_m)/toplam_alan)} TL",
   f"{tr(kira/3)} TL"],
  f"Toplam alan {tr(toplam_alan)} m²'dir. Pres payı = {tr(kira)} × {tr(alan_p)} / {tr(toplam_alan)} = {tr(pres_kira)} TL'dir.",
  "TMS 2 par. 12 - dolaylı üretim maliyetlerinin sistematik dağıtımı")

enerji, kwh_kesim, kwh_montaj, kwh_bakim = 252_000, 56_000, 28_000, 16_000
toplam_kwh = kwh_kesim + kwh_montaj + kwh_bakim
montaj_enerji = enerji * kwh_montaj / toplam_kwh
assert toplam_kwh == 100_000 and montaj_enerji == 70_560
q(f"Ölçülen toplam elektrik gideri {tr(enerji)} TL'dir. Kesim {tr(kwh_kesim)}, Montaj {tr(kwh_montaj)} ve Bakım {tr(kwh_bakim)} kWh tüketmiştir. Sayaç verisine göre Montaj gider yerine dağıtılacak tutar kaç TL'dir?",
  f"{tr(montaj_enerji)} TL",
  [f"{tr(enerji*kwh_kesim/toplam_kwh)} TL",
   f"{tr(enerji*kwh_bakim/toplam_kwh)} TL",
   f"{tr(enerji/3)} TL",
   f"{tr(enerji*(kwh_montaj+kwh_bakim)/toplam_kwh)} TL"],
  f"Montaj tüketim payı {tr(kwh_montaj)} / {tr(toplam_kwh)}'dir. Dağıtılan enerji gideri {tr(enerji)} × {tr(kwh_montaj)} / {tr(toplam_kwh)} = {tr(montaj_enerji)} TL olur.",
  "TMS 2 par. 12 - değişken genel üretim giderlerinin gerçek kullanıma dayalı dağıtımı")

kira2, enerji2 = 360_000, 240_000
alan_orani_a, enerji_orani_a = 0.40, 0.55
a_kira, a_enerji = kira2 * alan_orani_a, enerji2 * enerji_orani_a
a_toplam = a_kira + a_enerji
assert (a_kira, a_enerji, a_toplam) == (144_000, 132_000, 276_000)
q(f"A gider yeri toplam alanın %{int(alan_orani_a*100)}'ını ve ölçülen elektrik tüketiminin %{int(enerji_orani_a*100)}'ini kullanmaktadır. Ortak kira {tr(kira2)} TL, enerji gideri {tr(enerji2)} TL ise A'ya birinci dağıtımda bu iki giderden toplam kaç TL düşer?",
  f"{tr(a_toplam)} TL",
  [f"{tr((kira2+enerji2)*alan_orani_a)} TL",
   f"{tr((kira2+enerji2)*enerji_orani_a)} TL",
   f"{tr(a_kira)} TL",
   f"{tr(a_enerji)} TL"],
  f"Kira payı {tr(kira2)} × %{int(alan_orani_a*100)} = {tr(a_kira)} TL; enerji payı {tr(enerji2)} × %{int(enerji_orani_a*100)} = {tr(a_enerji)} TL'dir. Toplam {tr(a_toplam)} TL olur.",
  "TMS 2 par. 12 - farklı gider havuzlarının uygun anahtarlarla dağıtımı", "hard")

q("Yalnız Boya bölümünde çalışan bölüm sorumlusunun ücreti başka gider yerlerine hizmet vermiyorsa birinci dağıtımda hangi işlem uygundur?",
  "Ücretin doğrudan Boya gider yerine yüklenmesi",
  ["Ücretin tüm üretim ve yardımcı gider yerlerine personel sayısına göre yeniden dağıtılması",
   "Bölüm sorumlusu yönetici olduğu için ücretin üretimden çıkarılıp genel yönetim gideri yapılması",
   "Ücretin mamul satış fiyatlarına göre pazarlama bölümleri arasında paylaştırılması",
   "Ücretin ikinci dağıtım tamamlanıncaya kadar hiçbir gider yerine kaydedilmemesi"],
  "Gider yalnız Boya gider yerinde doğmuş ve bu yere doğrudan izlenebiliyorsa ortak gider değildir; doğrudan Boya gider yerine yüklenir.",
  "1 Sıra No.lu MSUGT - 730 Genel Üretim Giderleri, gider yerleri itibarıyla izleme")

q("Makine sicil kayıtları belirli bir üretim bölümündeki makinelerin amortismanını ayrı gösteriyorsa alan anahtarı kullanmak neden uygun değildir?",
  "Doğrudan izleme dağıtımdan daha güvenilir olduğu için",
  ["Amortisman hiçbir koşulda üretim maliyetine alınamayacağı ve dönem gideri sayıldığı için",
   "Alan anahtarı yalnız direkt işçilik giderlerinin mamullere yüklenmesinde kullanılabildiği için",
   "Makine amortismanının satış fiyatına göre dağıtılması mevzuatla zorunlu tutulduğu için",
   "Doğrudan izlenen her maliyetin yardımcı gider yerine aktarılması gerektiği için"],
  "Doğrudan izlenebilen gideri dolaylı anahtarla yeniden dağıtmak maliyet bilgisini bozabilir. Makine amortismanı ilgili bölüme doğrudan yüklenmelidir.",
  "TMS 2 par. 12 - sistematik dağıtım; 1 Sıra No.lu MSUGT - gider yerleri")

q("Bakım atölyesine ait yedek parça tüketiminin hangi üretim bölümüne hizmet verileceği henüz belli değilse birinci dağıtımda nerede toplanması uygundur?",
  "Bakım yardımcı gider yerinde",
  ["Hizmet henüz verilmediği için doğrudan satış ve pazarlama giderleri hesabında toplanması",
   "Tüm üretim bölümlerine gelecekteki satış tutarlarına göre peşinen eşit dağıtılması",
   "Yedek parça olduğu için mamullere direkt ilk madde maliyeti olarak hemen yüklenmesi",
   "Herhangi bir gider yerine kaydedilmeden yalnız stok çıkışı olarak maliyet dışında bırakılması"],
  "Bakım atölyesinin kendi tüketimi önce bakım yardımcı gider yerinde toplanır. Atölyenin üretim gider yerlerine sunduğu hizmetler belirlendiğinde ikinci dağıtımla aktarılır.",
  "1 Sıra No.lu MSUGT - yardımcı üretim ve hizmet gider yerleri; 730 hesabı")

q("Birinci dağıtımla ilgili aşağıdaki uygulamalardan hangileri doğrudur?\n\nI. Ortak bina giderinin alanla dağıtılması\n\nII. Ölçülen enerjinin sayaç tüketimiyle dağıtılması\n\nIII. Yalnız bir gider yerinde doğan giderin o yere doğrudan yüklenmesi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Alan ortak bina kullanımını, sayaç tüketimi enerji kullanımını temsil eder. Yalnız bir gider yerinde doğan gider ise dağıtım anahtarı olmadan doğrudan yüklenir; üç uygulama da uygundur.",
  "TMS 2 par. 12 - sistematik dağıtım; 1 Sıra No.lu MSUGT - gider yerleri", "hard")

q("Birinci dağıtım tablosunda gider türleri gider yerlerine paylaştırıldıktan sonra kontrol toplamı bakımından hangi eşitlik sağlanmalıdır?",
  "Dağıtılan giderler toplamı başlangıç giderleri toplamına eşit olmalıdır",
  ["Esas üretim gider yerleri toplamı her durumda başlangıç giderlerinin yarısına eşit olmalıdır",
   "Yardımcı gider yerlerinin bakiyesi birinci dağıtım sonunda mutlaka sıfır olmalıdır",
   "Her gider yerinin aldığı pay diğer tüm gider yerlerinin payına eşit olmak zorundadır",
   "Dağıtım sonucunda toplam gider, kullanılan anahtar sayısı kadar artmış olmalıdır"],
  "Dağıtım gider yaratmaz veya yok etmez; yalnız mevcut giderleri yerler arasında paylaştırır. Bu nedenle satır ve sütun toplamları başlangıç giderleriyle uzlaşmalıdır.",
  "1 Sıra No.lu MSUGT - maliyet hesaplarında tutarlılık ve gider yerleri")

q("Ortak giderin dağıtım anahtarı toplamında bir gider yerine ait veri eksikse güvenilir sonuç için öncelikli işlem ne olmalıdır?",
  "Eksik veri doğrulanıp dağıtımdan önce tamamlanmalıdır",
  ["Eksik gider yerine otomatik olarak sıfır pay verilip kalan tutar diğer yerlere dağıtılmalıdır",
   "Eksik değer bütün gider yerlerinin ortalaması alınarak gerekçe yazılmadan doldurulmalıdır",
   "Ortak giderin tamamı en yüksek anahtar değerine sahip gider yerine yüklenmelidir",
   "Dağıtım anahtarı verisi bulunmadığı için gider kayıtlardan tamamen çıkarılmalıdır"],
  "Anahtar toplamı eksikse paylar güvenilir değildir. Veri doğrulanmalı; zorunlu tahmin kullanılırsa yöntem ve gerekçe tutarlı biçimde belgelenmelidir.",
  "TMS 2 par. 12 - sistematik dağıtım ve güvenilir maliyet ölçümü")

q("Fabrika su giderinin bir kısmı proses tüketimine, bir kısmı sosyal alan kullanımına ait ve ayrı ölçülebiliyorsa en uygun yaklaşım nedir?",
  "Alt havuzlara ayırıp her kısmı kendi tüketim ölçüsüyle dağıtmak",
  ["Giderin tamamını yalnız çalışan sayısına göre bütün gider yerlerine dağıtmak",
   "Giderin tamamını yalnız üretilen mamul adedine göre esas üretim yerlerine yüklemek",
   "Su giderini üretimle ilişkisiz kabul ederek doğrudan genel yönetim giderine aktarmak",
   "Ölçüm verilerini kullanmadan bütün gider yerlerine eşit tutarda paylaştırmak"],
  "Proses ve sosyal kullanım farklı maliyet etkenlerine sahiptir. Ayrı ölçüm mevcutsa homojen alt havuzlar ve uygun anahtarlar daha doğru dağıtım sağlar.",
  "TMS 2 par. 12 - dolaylı üretim maliyetlerinin sistematik dağıtımı", "hard")

q("Kullanılmayan kapalı bir fabrika alanının giderini çalışan bölüm alanlarına dağıtmak hangi riski doğurur?",
  "Faaliyetteki bölümlerin kaynak tüketimini olduğundan yüksek gösterme riskini",
  ["Dağıtılan toplam giderin matematiksel olarak başlangıç giderinden düşük çıkmasını zorunlu kılar",
   "Bütün sabit genel üretim giderlerinin değişken maliyete dönüşmesine ve toplamın sıfırlanmasına yol açar",
   "Direkt malzeme ve direkt işçilik giderlerinin muhasebe kayıtlarından otomatik olarak silinmesini sağlar",
   "Yardımcı gider yerlerinin birbirine sunduğu hizmetlerin tam olarak dikkate alınmasını garanti eder"],
  "Atıl alana ait giderin çalışan bölümlere yüklenmesi, bu bölümlerin tüketmediği kapasite maliyetini üstlenmesine yol açabilir. Normal kapasite ve atıl kapasite ayrımı ayrıca değerlendirilmelidir.",
  "TMS 2 par. 13 - atıl kapasite ve dağıtılmayan genel üretim giderleri", "hard")

q("Bir gider yerine birinci dağıtımda önce doğrudan giderler, sonra ortak gider payları yüklendiğinde bölüm toplamı nasıl bulunur?",
  "Doğrudan giderler ile ortak gider paylarının toplamı olarak",
  ["Yalnız ortak gider payları dikkate alınıp doğrudan giderler toplam dışında bırakılarak",
   "Yalnız doğrudan giderler dikkate alınıp ortak giderlerin tamamı dönem gideri yapılarak",
   "Doğrudan giderlerden ortak gider payları çıkarılıp kalan tutar bölüm maliyeti sayılarak",
   "İki tutardan küçük olan seçilip diğer tutar yardımcı gider yerine aktarılarak"],
  "Birinci dağıtım sonundaki gider yeri toplamı, o yere doğrudan yüklenen giderlerle uygun anahtarlardan aldığı ortak gider paylarının toplamıdır.",
  "1 Sıra No.lu MSUGT - 730 hesabının gider yerleri itibarıyla izlenmesi")

q("Fabrika temizliği dışarıdan alınmış ve sözleşme her bölümün temizlenen metrekaresini ayrı gösteriyorsa hangi dağıtım yaklaşımı uygundur?",
  "Temizlenen alan ölçülerine göre gider yerlerine yüklemek",
  ["Temizlik giderini üretilen mamullerin satış fiyatlarına göre mamullere doğrudan paylaştırmak",
   "Temizlik üretimle ilgili olsa da tamamını merkez yönetim giderine aktarıp stoklardan çıkarmak",
   "Sözleşmedeki bölüm verilerini kullanmadan bütün gider yerlerine eşit tutar vermek",
   "Hizmet dışarıdan alındığı için gideri finansman maliyeti olarak faizlerle birlikte raporlamak"],
  "Sözleşmedeki temizlenen alan, gider yerlerinin hizmetten yararlanmasını ölçer. Gider bu veriye göre sistematik olarak gider yerlerine yüklenebilir.",
  "TMS 2 par. 12 - sistematik dağıtım")


# ── B. İkinci dağıtım: yardımcı gider yerleri (20) ────────────────────────
q("Bakım ve Enerji yardımcı gider yerleri birbirlerine hizmet verdiği hâlde doğrudan dağıtım yöntemi uygulanırsa bu karşılıklı hizmetler nasıl ele alınır?",
  "Yardımcı gider yerleri arasındaki hizmetler dikkate alınmaz",
  ["Karşılıklı hizmetler eşzamanlı denklemlerle tam olarak hesaplanıp üretim yerlerine aktarılır",
   "Yalnız maliyeti küçük olan yardımcı gider yerinin diğerine verdiği hizmet dikkate alınır",
   "Her yardımcı gider yeri diğerine verdiği hizmet kadar kendi giderini azaltarak bakiyede bırakır",
   "Karşılıklı hizmetler doğrudan mamullere yüklenir ve esas üretim gider yerleri atlanır"],
  "Doğrudan yöntemde yardımcı gider yerlerinin birbirlerine sunduğu hizmetler ihmal edilir; yardımcı giderler yalnız esas üretim gider yerlerine dağıtılır.",
  "1 Sıra No.lu MSUGT - yardımcı gider yerlerinin ikinci dağıtımı", "easy")

q("İkinci dağıtım yöntemlerine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Doğrudan yöntem yardımcı yerler arası hizmeti ihmal eder\n\nII. Kademeli yöntem yardımcı yerler arası hizmeti seçilen sıra ölçüsünde kısmen dikkate alır\n\nIII. Kademeli yöntem karşılıklı hizmetleri eşzamanlı denklemlerle tam olarak çözer",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Doğrudan yöntem karşılıklı hizmeti dışlar; kademeli yöntem seçilen sıra içinde tek yönlü dikkate alır. Eşzamanlı denklemlerle tam çözüm karşılıklı dağıtım yöntemine aittir.",
  "1 Sıra No.lu MSUGT - yardımcı gider yerlerinin dağıtım yöntemleri")

bakim_maliyeti, bakim_a, bakim_b = 180_000, 720, 480
bakim_toplam = bakim_a + bakim_b
bakim_a_pay = bakim_maliyeti * bakim_a / bakim_toplam
bakim_b_pay = bakim_maliyeti * bakim_b / bakim_toplam
assert (bakim_a_pay, bakim_b_pay) == (108_000, 72_000)
q(f"Doğrudan yöntemde Bakım yardımcı gider yerinin {tr(bakim_maliyeti)} TL maliyeti yalnız A ve B esas üretim yerlerine dağıtılacaktır. A {tr(bakim_a)}, B {tr(bakim_b)} bakım saati kullanmıştır. A ve B'nin payları sırasıyla kaç TL'dir?",
  f"{tr(bakim_a_pay)} TL ve {tr(bakim_b_pay)} TL",
  [f"{tr(bakim_b_pay)} TL ve {tr(bakim_a_pay)} TL",
   f"{tr(bakim_maliyeti/2)} TL ve {tr(bakim_maliyeti/2)} TL",
   f"{tr(bakim_maliyeti)} TL ve 0 TL",
   f"{tr(bakim_a)} TL ve {tr(bakim_b)} TL"],
  f"Toplam bakım saati {tr(bakim_toplam)}'dir. A payı {tr(bakim_maliyeti)} × {tr(bakim_a)} / {tr(bakim_toplam)} = {tr(bakim_a_pay)} TL; B payı {tr(bakim_b_pay)} TL'dir.",
  "TMS 2 par. 12 - dolaylı üretim maliyetlerinin sistematik dağıtımı")

bakim3, yemek3 = 160_000, 120_000
bakim_a_oran, yemek_a_oran = 0.60, 0.45
a_ikincil = bakim3 * bakim_a_oran + yemek3 * yemek_a_oran
assert a_ikincil == 150_000
q(f"Doğrudan yöntemde A esas üretim yeri, {tr(bakim3)} TL'lik Bakım maliyetinin %{int(bakim_a_oran*100)}'ını ve {tr(yemek3)} TL'lik Yemekhane maliyetinin %{int(yemek_a_oran*100)}'ini almaktadır. A'ya ikinci dağıtımla gelen toplam tutar kaç TL'dir?",
  f"{tr(a_ikincil)} TL",
  [f"{tr((bakim3+yemek3)*bakim_a_oran)} TL",
   f"{tr((bakim3+yemek3)*yemek_a_oran)} TL",
   f"{tr(bakim3*bakim_a_oran)} TL",
   f"{tr(yemek3*yemek_a_oran)} TL"],
  f"Bakım payı {tr(bakim3)} × %{int(bakim_a_oran*100)} = {tr(bakim3*bakim_a_oran)} TL; yemekhane payı {tr(yemek3)} × %{int(yemek_a_oran*100)} = {tr(yemek3*yemek_a_oran)} TL'dir. Toplam {tr(a_ikincil)} TL olur.",
  "1 Sıra No.lu MSUGT - yardımcı gider yerlerinin esas üretim yerlerine dağıtımı", "hard")

q("Kademeli dağıtımda yardımcı gider yerlerinin sırası belirlenirken en çok sayıda yardımcı yere hizmet veren bölümün önce kapatılması hangi amaca hizmet eder?",
  "Karşılıklı hizmetlerin daha büyük kısmını tek yönlü dikkate almaya",
  ["Yardımcı gider yerleri arasındaki bütün hizmetleri eşzamanlı denklemlerle eksiksiz çözmeye",
   "Esas üretim gider yerlerinin maliyetlerini yardımcı gider yerlerine geri dağıtmaya",
   "Birinci dağıtımda ortak giderlerin gider yerlerine verilmesini tamamen ortadan kaldırmaya",
   "Dağıtım sonunda toplam maliyeti başlangıç tutarından daha yüksek göstermeye"],
  "Kademeli yöntemde sıra sonucu etkiler. Diğer yardımcı yerlere daha fazla hizmet sunan yerin önce dağıtılması, karşılıklı hizmetin daha büyük bölümünü dikkate alabilir.",
  "1 Sıra No.lu MSUGT - kademeli ikinci dağıtım yöntemi")

enerji_kendi = 120_000
enerji_bakim, enerji_a, enerji_b = 0.20, 0.50, 0.30
bakim_kendi = 96_000
bakim_enerji_payi = enerji_kendi * enerji_bakim
bakim_dagitilacak = bakim_kendi + bakim_enerji_payi
bakim_a_oran2, bakim_b_oran2 = 0.75, 0.25
a_kademeli = enerji_kendi * enerji_a + bakim_dagitilacak * bakim_a_oran2
b_kademeli = enerji_kendi * enerji_b + bakim_dagitilacak * bakim_b_oran2
assert (bakim_enerji_payi, bakim_dagitilacak, a_kademeli, b_kademeli) == (24_000, 120_000, 150_000, 66_000)
q(f"Kademeli yöntemde önce Enerji dağıtılacaktır. Enerjinin {tr(enerji_kendi)} TL maliyetinin %{int(enerji_bakim*100)}'si Bakıma, %{int(enerji_a*100)}'si A'ya, kalanı B'ye verilir. Bakımın kendi {tr(bakim_kendi)} TL'si ve Enerjiden aldığı pay daha sonra A'ya %75, B'ye %25 dağıtılır. A'nın toplam payı kaç TL'dir?",
  f"{tr(a_kademeli)} TL",
  [f"{tr(b_kademeli)} TL",
   f"{tr(enerji_kendi*enerji_a)} TL",
   f"{tr(bakim_dagitilacak*bakim_a_oran2)} TL",
   f"{tr(enerji_kendi+bakim_kendi)} TL"],
  f"Enerjiden A'ya {tr(enerji_kendi*enerji_a)} TL, Bakıma {tr(bakim_enerji_payi)} TL gider. Bakım toplamı {tr(bakim_dagitilacak)} TL olur; A bunun {tr(bakim_dagitilacak*bakim_a_oran2)} TL'sini alır. A toplamı {tr(a_kademeli)} TL'dir.",
  "1 Sıra No.lu MSUGT - kademeli ikinci dağıtım yöntemi", "hard")

q(f"Önce Enerji sonra Bakım sırasıyla yapılan kademeli dağıtımda A'ya {tr(a_kademeli)} TL, B'ye {tr(b_kademeli)} TL aktarılmıştır. Kontrol toplamı bakımından hangi sonuç doğrudur?",
  f"A ve B toplamı {tr(enerji_kendi+bakim_kendi)} TL'dir",
  [f"A ve B toplamı yalnız Enerjinin {tr(enerji_kendi)} TL maliyetine eşittir",
   f"A ve B toplamı yalnız Bakımın {tr(bakim_kendi)} TL kendi maliyetine eşittir",
   f"A ve B toplamı {tr(enerji_kendi+bakim_kendi+bakim_enerji_payi)} TL olmalıdır",
   f"A ve B toplamı dağıtım sırası nedeniyle başlangıç maliyetlerinden düşük olmalıdır"],
  f"İç hizmet payı yeni maliyet yaratmaz. Esas üretim yerlerine aktarılan {tr(a_kademeli)} + {tr(b_kademeli)} = {tr(enerji_kendi+bakim_kendi)} TL, iki yardımcı yerin başlangıç maliyetleri toplamına eşittir.",
  "1 Sıra No.lu MSUGT - ikinci dağıtım kontrol toplamı")

q("Kademeli yöntemde dağıtım sırası Enerji-Bakım yerine Bakım-Enerji olarak değiştirilirse sonuçların değişebilmesinin nedeni nedir?",
  "Kapatılan yardımcı yerin sonraki yerlerden yeniden pay almamasıdır",
  ["Dağıtım sırası değişince toplam yardımcı gider maliyetinin matematiksel olarak artmasıdır",
   "Esas üretim yerlerinin kendi giderlerinin yardımcı gider yerlerine geri aktarılmasıdır",
   "Her sırada karşılıklı hizmetlerin eşzamanlı denklemlerle tam olarak çözülmesidir",
   "Sıra değişikliğinin yalnız direkt ilk madde maliyetini değiştirmesi ve GÜG'ü etkilememesidir"],
  "Kademeli yöntemde dağıtımı tamamlanıp kapatılan yardımcı gider yeri, daha sonra dağıtılan yardımcı yerden geri pay almaz. Bu tek yönlülük sıra etkisi yaratır.",
  "1 Sıra No.lu MSUGT - kademeli ikinci dağıtım yöntemi")

q("Kademeli dağıtım yöntemine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dağıtımı tamamlanan yardımcı gider yeri yeniden pay almaz\n\nII. Seçilen dağıtım sırası esas üretim yerlerinin alacağı payları etkileyebilir\n\nIII. Yöntem karşılıklı hizmetleri eşzamanlı denklemlerle tamamen dikkate alır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kademeli yöntemde kapatılan yer geri pay almaz ve sıra sonuçları etkileyebilir. Karşılıklı hizmetlerin tam ve eşzamanlı çözümü matematiksel yönteme aittir.",
  "1 Sıra No.lu MSUGT - kademeli ikinci dağıtım yöntemi", "hard")

# Karşılıklı hizmet denklemleri: M = 100.000 + %20 E; E = 76.000 + %20 M.
m_kendi, e_kendi, hizmet_orani = 100_000, 76_000, 0.20
m_toplam, e_toplam = 120_000, 100_000
assert m_toplam == m_kendi + hizmet_orani * e_toplam
assert e_toplam == e_kendi + hizmet_orani * m_toplam
q(f"Karşılıklı yöntemde Bakım (M) ve Enerji (E) toplam maliyetleri M = {tr(m_kendi)} + %20E ve E = {tr(e_kendi)} + %20M denklemleriyle gösterilmektedir. Denklem sistemi çözüldüğünde M'nin toplam maliyeti kaç TL'dir?",
  f"{tr(m_toplam)} TL",
  [f"{tr(m_kendi)} TL",
   f"{tr(m_toplam+e_toplam)} TL",
   f"{tr(m_kendi+e_kendi)} TL",
   f"{tr(m_kendi+hizmet_orani*e_kendi)} TL"],
  f"Eşzamanlı çözümde M = {tr(m_kendi)} + %20 × {tr(e_toplam)} = {tr(m_toplam)} TL; E = {tr(e_kendi)} + %20 × {tr(m_toplam)} = {tr(e_toplam)} TL olur.",
  "1 Sıra No.lu MSUGT - matematiksel (karşılıklı) ikinci dağıtım yöntemi", "hard")

q(f"Bakım ve Enerji denklemleri M = {tr(m_kendi)} + %20E ve E = {tr(e_kendi)} + %20M'dir. M toplamı {tr(m_toplam)} TL bulunduğuna göre E'nin toplam maliyeti kaç TL'dir?",
  f"{tr(e_toplam)} TL",
  [f"{tr(e_kendi)} TL",
   f"{tr(m_toplam)} TL",
   f"{tr(e_kendi+hizmet_orani*e_kendi)} TL",
   f"{tr(m_kendi+e_kendi)} TL"],
  f"Enerji toplamı E = {tr(e_kendi)} + %20 × {tr(m_toplam)} = {tr(e_kendi)} + {tr(hizmet_orani*m_toplam)} = {tr(e_toplam)} TL'dir.",
  "1 Sıra No.lu MSUGT - matematiksel (karşılıklı) ikinci dağıtım yöntemi", "hard")

m_a, m_b = m_toplam * 0.50, m_toplam * 0.30
e_a, e_b = e_toplam * 0.40, e_toplam * 0.40
a_karsilikli, b_karsilikli = m_a + e_a, m_b + e_b
assert (m_a, m_b, e_a, e_b, a_karsilikli, b_karsilikli) == (60_000, 36_000, 40_000, 40_000, 100_000, 76_000)
q(f"Karşılıklı çözüm sonunda Bakım {tr(m_toplam)} TL, Enerji {tr(e_toplam)} TL'dir. Bakım hizmetinin %50'si A'ya, %30'u B'ye; Enerjinin %40'ı A'ya, %40'ı B'ye sunulmuştur. A esas üretim yerine iki yardımcı yerden toplam kaç TL aktarılır?",
  f"{tr(a_karsilikli)} TL",
  [f"{tr(b_karsilikli)} TL",
   f"{tr(m_a)} TL",
   f"{tr(e_a)} TL",
   f"{tr(m_toplam+e_toplam)} TL"],
  f"A, Bakımdan {tr(m_toplam)} × %50 = {tr(m_a)} TL; Enerjiden {tr(e_toplam)} × %40 = {tr(e_a)} TL alır. Toplam {tr(a_karsilikli)} TL'dir.",
  "1 Sıra No.lu MSUGT - karşılıklı hizmetlerin esas üretim yerlerine dağıtımı", "hard")

q("Yardımcı gider yerleri birbirlerine önemli ölçüde hizmet sunuyorsa karşılıklı yöntemin doğrudan yönteme göre temel üstünlüğü nedir?",
  "Yardımcı yerler arası hizmetleri tam olarak maliyetlere katması",
  ["Esas üretim gider yerlerinin kendi maliyetlerini yardımcı gider yerlerine geri dağıtması",
   "Dağıtım anahtarı kullanmadan bütün maliyetleri mamullere eşit olarak yüklemesi",
   "Toplam gideri karşılıklı hizmet tutarı kadar artırarak daha yüksek maliyet göstermesi",
   "Birinci dağıtımın yapılmasını gereksiz kılarak tüm ortak giderleri kayıtlardan çıkarması"],
  "Karşılıklı yöntem, yardımcı gider yerlerinin birbirlerine sunduğu hizmetleri eşzamanlı denklemlerle tam olarak dikkate alır. Bu nedenle önemli karşılıklı hizmetlerde daha hassastır.",
  "1 Sıra No.lu MSUGT - matematiksel ikinci dağıtım yöntemi")

q("İki yardımcı gider yeri birbirine hiç hizmet sunmuyorsa doğrudan ve karşılıklı yöntem sonuçlarının aynı olmasının nedeni nedir?",
  "Çözülecek karşılıklı hizmet bulunmamasıdır",
  ["Karşılıklı yöntemin her durumda doğrudan yöntemin adlarını ve oranlarını aynen kullanmasıdır",
   "Esas üretim yerlerinin giderlerinin yardımcı gider yerlerine geri aktarılmasıdır",
   "İkinci dağıtımda bütün giderlerin tutarına bakılmadan eşit paylaştırılmasıdır",
   "Yardımcı gider yerlerinin maliyetlerinin stok maliyetinden tamamen çıkarılmasıdır"],
  "Yardımcı yerler arasında hizmet yoksa matematiksel denklemlerde karşılıklı pay oluşmaz. Her iki yöntem de yalnız esas üretim yerlerine aynı hizmet oranlarıyla dağıtım yapar.",
  "1 Sıra No.lu MSUGT - yardımcı gider yerlerinin ikinci dağıtımı")

q("İkinci dağıtım tamamlandıktan sonra yardımcı gider yerlerinin maliyet bakiyelerinin sıfır olması neyi gösterir?",
  "Maliyetlerinin hizmet alan esas üretim yerlerine aktarıldığını",
  ["Yardımcı gider yerlerinde dönem boyunca hiçbir maliyet oluşmadığını ve kayıt yapılmadığını",
   "Yardımcı gider maliyetlerinin tamamının genel yönetim gideri olarak iptal edildiğini",
   "Esas üretim gider yerlerinin maliyetlerinin yardımcı yerlere geri dağıtıldığını",
   "Dağıtılan tutarların mamul satış fiyatlarından indirilerek gelir kaydedildiğini"],
  "İkinci dağıtım yardımcı gider yeri maliyetlerini hizmet alan esas üretim gider yerlerine taşır. Dağıtım tamamlandığında yardımcı yer bakiyeleri sıfırlanır.",
  "1 Sıra No.lu MSUGT - yardımcı gider yerlerinin ikinci dağıtımı")

q("Bakım yardımcı gider yerinin maliyeti esas üretim yerlerine aktarıldıktan sonra mamullere hangi yolla ulaşır?",
  "Esas üretim yerlerinin üçüncü dağıtımı aracılığıyla",
  ["Bakım maliyeti ikinci dağıtım sonunda gider yeri bakiyesinde bırakılıp mamullere hiç yüklenmeyerek",
   "Bakım maliyeti doğrudan satış hasılatından indirilip üretim maliyetleriyle ilişkilendirilmeyerek",
   "Bakım gideri mamullere direkt ilk madde olarak ürün reçetesi üzerinden yüklenerek",
   "Bakım maliyeti yalnız merkez yönetim giderine aktarılıp dönem sonucunda gösterilerek"],
  "Bakım maliyeti ikinci dağıtımla esas üretim yerlerine gelir. Esas üretim yerlerinde biriken toplam GÜG, üçüncü dağıtımla mamullerin kullandığı faaliyet ölçülerine göre yüklenir.",
  "TMS 2 par. 12 - dolaylı üretim maliyetlerinin mamullere sistematik dağıtımı")

q("Karşılıklı dağıtım yöntemine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Her yardımcı yerin toplam maliyeti kendi maliyeti ile diğerlerinden aldığı hizmeti içerir\n\nII. Yardımcı yer toplamları eşzamanlı denklemlerle çözülebilir\n\nIII. Yardımcı yerlerin birbirine sunduğu hizmetler hesap dışında bırakılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karşılıklı yöntemde toplam maliyet, kendi maliyeti ile diğer yardımcı yerlerden alınan hizmetleri içerir ve eşzamanlı denklemlerle çözülür. Hizmetlerin dışlanması doğrudan yönteme aittir.",
  "1 Sıra No.lu MSUGT - matematiksel ikinci dağıtım yöntemi", "hard")

q("İkinci dağıtımın kontrolünde esas üretim yerlerine aktarılan toplam ile yardımcı gider yerlerinin dağıtım öncesi toplamının eşit olması hangi ilkeyi doğrular?",
  "Dağıtımın toplam maliyeti değiştirmediğini",
  ["Dağıtımın her yardımcı hizmeti yeni bir gider olarak yeniden oluşturduğunu",
   "Esas üretim yerlerinin giderlerinin ikinci dağıtımda mutlaka azaldığını",
   "Yardımcı giderlerin stok maliyetinden çıkarılarak dönem gideri yapıldığını",
   "Dağıtım yönteminin gider toplamını hizmet sayısı kadar çoğalttığını"],
  "İç hizmetler maliyetin kaynağını ve yerini değiştirir, yeni toplam maliyet yaratmaz. Esas yerlere aktarılan toplam, yardımcı yerlerin başlangıç toplamıyla uzlaşmalıdır.",
  "1 Sıra No.lu MSUGT - ikinci dağıtım kontrol toplamı")

q("Yemekhane, bakım ve enerji yardımcı gider yerleri için sırasıyla hangi hizmet ölçüleri daha güçlü neden-sonuç ilişkisi kurar?",
  "Öğün sayısı, bakım saati ve ölçülen kilovatsaat",
  ["Makine değeri, mamul satış fiyatı ve ortakların sermaye payı ölçülerinin birlikte kullanılması",
   "Bölüm yöneticilerinin kıdemi, çalışanların yaşı ve dönem kârı ölçülerinin kullanılması",
   "Tüm yardımcı hizmetlerin yalnız kaplanan alana göre ve aynı tek anahtarla dağıtılması",
   "Hiçbir hizmet ölçülmeden her yardımcı giderin esas üretim yerlerine eşit bölünmesi"],
  "Öğün sayısı yemekhane kullanımını, bakım saati bakım hizmetini, kWh ise enerji tüketimini doğrudan temsil eder. Anahtar hizmetten yararlanmayı yansıtmalıdır.",
  "TMS 2 par. 12 - sistematik dağıtım ve uygun faaliyet ölçüsü")

ilk_a, ilk_b = 420_000, 310_000
ikinci_a, ikinci_b = 150_000, 76_000
son_a, son_b = ilk_a + ikinci_a, ilk_b + ikinci_b
assert (son_a, son_b) == (570_000, 386_000)
q(f"Birinci dağıtım sonunda A esas üretim yerinde {tr(ilk_a)} TL, B'de {tr(ilk_b)} TL GÜG vardır. İkinci dağıtım A'ya {tr(ikinci_a)} TL, B'ye {tr(ikinci_b)} TL yardımcı gider aktarmıştır. İkinci dağıtım sonundaki A ve B toplamları sırasıyla kaç TL'dir?",
  f"{tr(son_a)} TL ve {tr(son_b)} TL",
  [f"{tr(ilk_a)} TL ve {tr(ilk_b)} TL",
   f"{tr(ikinci_a)} TL ve {tr(ikinci_b)} TL",
   f"{tr(ilk_a+ikinci_b)} TL ve {tr(ilk_b+ikinci_a)} TL",
   f"{tr(son_a+son_b)} TL ve 0 TL"],
  f"A toplamı {tr(ilk_a)} + {tr(ikinci_a)} = {tr(son_a)} TL; B toplamı {tr(ilk_b)} + {tr(ikinci_b)} = {tr(son_b)} TL'dir.",
  "1 Sıra No.lu MSUGT - esas üretim gider yerlerinin ikinci dağıtım sonrası toplamı")


# ── C. Üçüncü dağıtım ve mamullere yükleme (20) ──────────────────────────
q("İkinci dağıtım sonrası bir esas üretim gider yerinde biriken genel üretim giderinin mamullere yüklenmesinde oran nasıl oluşturulur?",
  "Gider yeri toplamı uygun faaliyet ölçüsü toplamına bölünür",
  ["Gider yeri toplamı mamullerin satış fiyatları toplamıyla çarpılarak doğrudan bulunur",
   "Yalnız direkt ilk madde toplamı genel üretim giderinden çıkarılarak oran elde edilir",
   "Gider yeri toplamı yardımcı gider yerlerinin sayısına bölünüp her mamule eşit verilir",
   "Üretim miktarı dikkate alınmadan gider yeri toplamının tamamı ilk üretilen mamule yüklenir"],
  "Üçüncü dağıtım oranı, esas üretim gider yerindeki toplam GÜG'ün o gider için seçilen toplam faaliyet ölçüsüne bölünmesiyle hesaplanır.",
  "TMS 2 par. 12 - genel üretim giderlerinin mamullere sistematik dağıtımı", "easy")

q("Kesim bölümü makine yoğun, Montaj bölümü emek yoğunsa bölüm bazında hangi iki anahtarın birlikte kullanılması daha uygundur?",
  "Kesimde makine saati, Montajda direkt işçilik saati",
  ["Her iki bölümde yalnız mamullerin satış fiyatı ve brüt kâr oranlarının birlikte kullanılması",
   "Kesimde çalışan sayısı, Montajda kullanılan fabrika alanı dışında hiçbir ölçü kullanılmaması",
   "Her iki bölümde de faaliyet yapısına bakılmadan yalnız direkt malzeme tutarının kullanılması",
   "Kesimde ve Montajda giderlerin hiçbir anahtar olmadan mamullere eşit dağıtılması"],
  "Anahtar bölümün kaynak tüketim yapısını yansıtmalıdır. Makine yoğun Kesimde makine saati, emek yoğun Montajda direkt işçilik saati uygun olabilir.",
  "TMS 2 par. 12 - sistematik dağıtım ve neden-sonuç ilişkisi")

q("Fabrika çapında tek yükleme oranı, otomasyon düzeyleri çok farklı iki üretim bölümünde hangi maliyetleme sorununa yol açabilir?",
  "Mamullerin bölüm kaynak tüketimini çapraz sübvanse etmesine",
  ["Dağıtılan genel üretim giderleri toplamının başlangıç giderinden matematiksel olarak farklı çıkmasına",
   "Direkt ilk madde ve direkt işçilik giderlerinin muhasebe kayıtlarından tamamen silinmesine",
   "Yardımcı gider yerlerinin karşılıklı hizmetlerinin eşzamanlı denklemlerle çözülmesine",
   "Bütün mamullerin üretim miktarları farklı olsa bile birim maliyetlerinin zorunlu olarak eşit olmasına"],
  "Tek oran, farklı maliyet etkenlerine sahip bölümlerde bazı mamullere fazla, bazılarına az GÜG yükleyebilir. Bölüm oranları kaynak tüketimini daha doğru yansıtır.",
  "TMS 2 par. 12 - sabit ve değişken genel üretim giderlerinin sistematik dağıtımı", "hard")

q("Üçüncü dağıtıma ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Esas üretim gider yeri toplamları mamullere yüklenir\n\nII. Her mamul, gider yerindeki faaliyet kullanımına göre pay alır\n\nIII. Mamullere yüklenen toplamlar esas üretim gider yeri toplamlarıyla uzlaştırılır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üçüncü dağıtım esas üretim gider yeri maliyetlerini mamullerin kullandığı faaliyet ölçüsüne göre yükler. Dağıtılan mamul payları gider yeri toplamıyla uzlaşmalıdır.",
  "TMS 2 par. 12 - genel üretim giderlerinin mamullere sistematik dağıtımı", "hard")

kesim_gug, kesim_saat = 528_000, 24_000
montaj_gug, montaj_saat = 378_000, 18_000
kesim_oran = kesim_gug / kesim_saat
montaj_oran = montaj_gug / montaj_saat
assert (kesim_oran, montaj_oran) == (22, 21)
q(f"İkinci dağıtım sonrası Kesim gider yerinde {tr(kesim_gug)} TL ve {tr(kesim_saat)} makine saati; Montajda {tr(montaj_gug)} TL ve {tr(montaj_saat)} direkt işçilik saati vardır. Bölüm yükleme oranları sırasıyla kaç TL'dir?",
  f"{tr(kesim_oran)} TL/makine saati ve {tr(montaj_oran)} TL/işçilik saati",
  [f"{tr(montaj_oran)} TL/makine saati ve {tr(kesim_oran)} TL/işçilik saati",
   f"{tr((kesim_gug+montaj_gug)/(kesim_saat+montaj_saat))} TL ve {tr(kesim_oran)} TL",
   f"{tr(kesim_gug/kesim_saat+montaj_gug/montaj_saat)} TL ve 0 TL",
   f"{tr(kesim_saat)} TL ve {tr(montaj_saat)} TL"],
  f"Kesim oranı {tr(kesim_gug)} / {tr(kesim_saat)} = {tr(kesim_oran)} TL/makine saati; Montaj oranı {tr(montaj_gug)} / {tr(montaj_saat)} = {tr(montaj_oran)} TL/işçilik saatidir.",
  "TMS 2 par. 12 - bölüm bazında sistematik genel üretim gideri dağıtımı")

x_makine, x_iscilik = 4, 3
x_birim_gug = x_makine * kesim_oran + x_iscilik * montaj_oran
assert x_birim_gug == 151
q(f"X mamulünün bir birimi Kesimde {tr(x_makine)} makine saati, Montajda {tr(x_iscilik)} direkt işçilik saati kullanmaktadır. Kesim oranı {tr(kesim_oran)} TL/makine saati, Montaj oranı {tr(montaj_oran)} TL/işçilik saati ise X'in birim GÜG payı kaç TL'dir?",
  f"{tr(x_birim_gug)} TL",
  [f"{tr(x_makine*kesim_oran)} TL",
   f"{tr(x_iscilik*montaj_oran)} TL",
   f"{tr((x_makine+x_iscilik)*(kesim_oran+montaj_oran))} TL",
   f"{tr(x_makine+x_iscilik+kesim_oran+montaj_oran)} TL"],
  f"Kesim payı {tr(x_makine)} × {tr(kesim_oran)} = {tr(x_makine*kesim_oran)} TL; Montaj payı {tr(x_iscilik)} × {tr(montaj_oran)} = {tr(x_iscilik*montaj_oran)} TL'dir. Toplam {tr(x_birim_gug)} TL olur.",
  "TMS 2 par. 12 - mamul faaliyet kullanımına göre GÜG yüklemesi")

x_adet = 1_600
x_parti_gug = x_adet * x_birim_gug
assert x_parti_gug == 241_600
q(f"Bir birimi {tr(x_birim_gug)} TL genel üretim gideri payı alan X mamulünden {tr(x_adet)} adet üretilmiştir. X üretim partisinin toplam GÜG payı kaç TL'dir?",
  f"{tr(x_parti_gug)} TL",
  [f"{tr((x_adet+400)*x_birim_gug)} TL",
   f"{tr((x_adet-400)*x_birim_gug)} TL",
   f"{tr(x_adet+x_birim_gug)} TL",
   f"{tr(x_birim_gug)} TL"],
  f"Parti GÜG payı = Birim pay × Üretim miktarı = {tr(x_birim_gug)} × {tr(x_adet)} = {tr(x_parti_gug)} TL'dir.",
  "TMS 2 par. 12 - genel üretim giderlerinin mamullere dağıtımı")

q("Otomatik makinelerde uzun süre işlem gören, ancak az direkt işçilik kullanan bir mamule yalnız direkt işçilik saatiyle fabrika çapında GÜG yüklenirse hangi hata beklenir?",
  "Makine kaynaklarını yoğun kullanan mamule eksik maliyet yüklenmesi",
  ["Mamulün direkt ilk madde maliyetinin otomatik olarak iki kez muhasebeleştirilmesi",
   "Dağıtılan toplam genel üretim giderinin her durumda başlangıç toplamından fazla çıkması",
   "Yardımcı gider yerlerinin birbirlerine sunduğu hizmetlerin tam olarak dikkate alınması",
   "Mamulün az işçilik kullandığı için sabit giderlerin tamamını tek başına üstlenmesi"],
  "Direkt işçilik saati makine tüketimini yansıtmıyorsa otomasyon yoğun mamul az pay alabilir. Makine saati veya bölüm bazlı oran, kaynak kullanımını daha iyi temsil eder.",
  "TMS 2 par. 12 - sistematik dağıtım ve uygun maliyet etkeni", "hard")

q("Bir üretim bölümünde kalite kontrol sayısı GÜG oluşumunu güçlü biçimde açıklıyor ve güvenilir ölçülüyorsa üçüncü dağıtımda kullanılmasının gerekçesi nedir?",
  "Mamulun bölüm kaynağından yararlanmasını temsil etmesi",
  ["Kalite kontrol sayısının tüm işletmeler için mevzuatla zorunlu tek dağıtım anahtarı olması",
   "Bu anahtar kullanıldığında genel üretim giderlerinin direkt malzemeye dönüşmesi",
   "Mamul satış fiyatlarını yükselterek dağıtılacak gider toplamını azaltması",
   "Yardımcı gider yerlerinin bakiyelerini birinci dağıtım öncesinde sıfırlaması"],
  "Güvenilir biçimde ölçülen kalite kontrol sayısı, bölüm maliyetleriyle neden-sonuç ilişkisi kuruyorsa mamullerin kaynak tüketimini temsil eden faaliyet ölçüsü olabilir.",
  "TMS 2 par. 12 - sistematik genel üretim gideri dağıtımı")

a_mh, a_lh, a_adet = 6, 2, 900
a_birim_gug = a_mh * kesim_oran + a_lh * montaj_oran
a_toplam_gug = a_birim_gug * a_adet
assert (a_birim_gug, a_toplam_gug) == (174, 156_600)
q(f"A mamulünün birimi Kesimde {tr(a_mh)} makine saati, Montajda {tr(a_lh)} işçilik saati kullanmaktadır. Bölüm oranları sırasıyla {tr(kesim_oran)} ve {tr(montaj_oran)} TL'dir. {tr(a_adet)} birim A mamulüne toplam kaç TL GÜG yüklenir?",
  f"{tr(a_toplam_gug)} TL",
  [f"{tr(a_birim_gug)} TL",
   f"{tr(a_mh*kesim_oran*a_adet)} TL",
   f"{tr(a_lh*montaj_oran*a_adet)} TL",
   f"{tr((a_mh+a_lh)*(kesim_oran+montaj_oran)*a_adet)} TL"],
  f"Birim GÜG = {tr(a_mh)} × {tr(kesim_oran)} + {tr(a_lh)} × {tr(montaj_oran)} = {tr(a_birim_gug)} TL'dir. {tr(a_adet)} birim için {tr(a_birim_gug)} × {tr(a_adet)} = {tr(a_toplam_gug)} TL yüklenir.",
  "TMS 2 par. 12 - bölüm oranlarıyla mamule GÜG yüklenmesi", "hard")

b_mh, b_lh, b_adet = 2, 5, 1_200
b_birim_gug = b_mh * kesim_oran + b_lh * montaj_oran
b_toplam_gug = b_birim_gug * b_adet
assert (b_birim_gug, b_toplam_gug) == (149, 178_800)
q(f"B mamulünün birimi Kesimde {tr(b_mh)} makine saati, Montajda {tr(b_lh)} işçilik saati kullanmaktadır. Bölüm oranları sırasıyla {tr(kesim_oran)} ve {tr(montaj_oran)} TL'dir. {tr(b_adet)} birim B mamulüne toplam kaç TL GÜG yüklenir?",
  f"{tr(b_toplam_gug)} TL",
  [f"{tr(b_birim_gug)} TL",
   f"{tr(b_mh*kesim_oran*b_adet)} TL",
   f"{tr(b_lh*montaj_oran*b_adet)} TL",
   f"{tr((b_mh+b_lh)*(kesim_oran+montaj_oran)*b_adet)} TL"],
  f"Birim GÜG = {tr(b_mh)} × {tr(kesim_oran)} + {tr(b_lh)} × {tr(montaj_oran)} = {tr(b_birim_gug)} TL'dir. {tr(b_adet)} birim için toplam {tr(b_toplam_gug)} TL yüklenir.",
  "TMS 2 par. 12 - bölüm oranlarıyla mamule GÜG yüklenmesi", "hard")

q("Üçüncü dağıtıma ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Esas üretim gider yeri toplamı dağıtımın maliyet havuzudur\n\nII. Mamulün faaliyet kullanımı yüklenen tutarı etkiler\n\nIII. Yardımcı gider yeri bakiyesi mamule ulaşmadan yardımcı yerde bırakılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Esas üretim gider yeri toplamı mamullere dağıtılacak havuzdur ve her mamul kullandığı faaliyet ölçüsüne göre pay alır. Yardımcı giderler ikinci dağıtımla esas yerlere aktarılmış olmalıdır.",
  "TMS 2 par. 12 - dolaylı üretim maliyetlerinin mamullere dağıtımı")

havuz, x_pay, y_pay = 420_000, 176_400, 243_600
assert x_pay + y_pay == havuz
q(f"Bir esas üretim gider yerinin {tr(havuz)} TL GÜG'ünden X mamulüne {tr(x_pay)} TL, Y mamulüne {tr(y_pay)} TL yüklenmiştir. Kontrol toplamı bakımından hangi sonuç doğrudur?",
  "Gider yerinin tamamı mamullere dağıtılmıştır",
  ["Gider yerinde dağıtılmamış 67.200 TL bakiye kaldığı için yükleme tamamlanmamıştır",
   "Mamullere gider yeri toplamından 67.200 TL fazla yükleme yapıldığı için kayıt ters çevrilmelidir",
   "Yalnız X mamulünün payı gider yeri toplamına eşit olduğundan Y payı iptal edilmelidir",
   "Yüklenen tutarlar gider yeri toplamıyla karşılaştırılamaz; kontrol toplamı kurulamaz"],
  f"Mamul payları {tr(x_pay)} + {tr(y_pay)} = {tr(havuz)} TL'dir. Bu tutar gider yeri toplamına eşit olduğundan havuz tamamen dağıtılmıştır.",
  "1 Sıra No.lu MSUGT - 730 ve 731 hesaplarının uzlaştırılması")

q("İkinci dağıtım yapılmadan esas üretim gider yeri oranı hesaplanırsa hangi maliyet eksikliği ortaya çıkar?",
  "Yardımcı hizmetlerden alınan maliyetler oran dışında kalır",
  ["Direkt ilk madde ve direkt işçilik giderleri mamullere iki kez yüklenmiş olur",
   "Birinci dağıtımda tüm ortak giderler otomatik olarak genel yönetim giderine dönüşür",
   "Esas üretim gider yerlerinin kendi giderleri yardımcı yerlere geri aktarılmış olur",
   "Dağıtılan toplam gider her durumda yardımcı gider toplamı kadar fazla çıkar"],
  "Esas üretim gider yeri üçüncü dağıtımdan önce yardımcı yerlerden aldığı payları da içermelidir. İkinci dağıtım atlanırsa mamuller yardımcı hizmet maliyetlerini eksik taşır.",
  "TMS 2 par. 12 - tüm dönüştürme maliyetlerinin sistematik dağıtımı", "hard")

q("Seçilen dağıtım anahtarında bir mamul için sıfır kullanım görünmesine rağmen mamulün bölümden fiilen yararlandığı biliniyorsa ne yapılmalıdır?",
  "Ölçüm verisi ve anahtar uygunluğu yeniden incelenmelidir",
  ["Mamulün bölüm kullanımına bakılmadan sıfır maliyet sonucu kesin kabul edilmelidir",
   "Gider yerinin tamamı veri hatası araştırılmadan bu mamule doğrudan yüklenmelidir",
   "Dağıtım anahtarı yerine mamulün satış fiyatı otomatik ve gerekçesiz kullanılmalıdır",
   "Bölüm gideri kayıtlardan çıkarılıp hiçbir mamule yüklenmeden iptal edilmelidir"],
  "Fiilî yararlanma varken sıfır kullanım, eksik faaliyet kaydı veya uygunsuz anahtar göstergesi olabilir. Veri doğrulanmadan maliyet sonucu kabul edilmemelidir.",
  "TMS 2 par. 12 - sistematik ve güvenilir dağıtım")

q("Bir maliyet mamule ekonomik biçimde doğrudan izlenebiliyorsa onu üçüncü dağıtım havuzuna almak neden sakıncalıdır?",
  "Doğrudan ilişkiyi gizleyip maliyeti başka mamullere kaydırabilir",
  ["Doğrudan maliyetlerin hiçbir zaman stok maliyetine alınamayacağı ve gider yazılması gerektiği için",
   "Üçüncü dağıtım yalnız satış ve genel yönetim giderleri için kullanılabildiği için",
   "Doğrudan izlenen maliyetin tutarı dağıtım havuzuna girince matematiksel olarak sıfırlandığı için",
   "Dağıtım havuzları yalnız finansman giderlerini mamullere yüklemek amacıyla kurulduğu için"],
  "Ekonomik biçimde doğrudan izlenebilen maliyet ilgili mamule doğrudan yüklenmelidir. Havuzda dağıtmak, maliyetin bir kısmını ilgisiz mamullere aktarabilir.",
  "TMS 2 par. 12 - doğrudan ve dolaylı dönüştürme maliyetleri")

birim_dm, birim_dl, birim_gug = 460, 280, 174
birim_uretim = birim_dm + birim_dl + birim_gug
assert birim_uretim == 914
q(f"Bir mamulün birim direkt malzemesi {tr(birim_dm)} TL, direkt işçiliği {tr(birim_dl)} TL ve bölüm oranlarıyla yüklenen GÜG'ü {tr(birim_gug)} TL'dir. Birim üretim maliyeti kaç TL'dir?",
  f"{tr(birim_uretim)} TL",
  [f"{tr(birim_dm+birim_dl)} TL",
   f"{tr(birim_dl+birim_gug)} TL",
   f"{tr(birim_dm+birim_gug)} TL",
   f"{tr(birim_gug)} TL"],
  f"Birim üretim maliyeti = Direkt malzeme + Direkt işçilik + Yüklenen GÜG = {tr(birim_dm)} + {tr(birim_dl)} + {tr(birim_gug)} = {tr(birim_uretim)} TL'dir.",
  "TMS 2 par. 10 ve 12 - stokların satın alma ve dönüştürme maliyetleri")

q("Bölüm oranları ile fabrika çapında tek oran karşılaştırmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bölümlerin kaynak yapıları farklıysa bölüm oranları çarpıklığı azaltabilir\n\nII. Bölümlerin maliyet etkenleri ve kullanım oranları aynıysa iki yaklaşım benzer sonuç verebilir\n\nIII. Fabrika çapında tek oran her koşulda bölüm oranlarından daha doğru sonuç verir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kaynak yapıları farklıysa bölüm oranları daha hassas olabilir; yapılar ve kullanım oranları aynıysa sonuçlar yakınlaşabilir. Tek oranın her koşulda üstün olduğu söylenemez.",
  "TMS 2 par. 12 - sistematik genel üretim gideri dağıtımı", "hard")

ayar_havuzu, toplam_ayar, p_ayar = 315_000, 175, 24
ayar_orani = ayar_havuzu / toplam_ayar
p_ayar_payi = ayar_orani * p_ayar
assert (ayar_orani, p_ayar_payi) == (1_800, 43_200)
q(f"Bir üretim bölümündeki {tr(ayar_havuzu)} TL makine ayar maliyeti, dönemdeki {tr(toplam_ayar)} ayar sayısına göre mamullere dağıtılacaktır. P mamulü {tr(p_ayar)} ayar gerektirdiğine göre P'ye yüklenecek ayar maliyeti kaç TL'dir?",
  f"{tr(p_ayar_payi)} TL",
  [f"{tr(ayar_orani)} TL",
   f"{tr(ayar_havuzu*p_ayar/(toplam_ayar+p_ayar))} TL",
   f"{tr(ayar_havuzu-p_ayar_payi)} TL",
   f"{tr(toplam_ayar*p_ayar)} TL"],
  f"Ayar başına maliyet {tr(ayar_havuzu)} / {tr(toplam_ayar)} = {tr(ayar_orani)} TL'dir. P'nin payı {tr(p_ayar)} × {tr(ayar_orani)} = {tr(p_ayar_payi)} TL olur.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik faaliyet ölçüsüyle dağıtımı", "hard")

e1_havuz, e2_havuz = 600_000, 420_000
e1_toplam_mh, e2_toplam_lh = 30_000, 21_000
e1_oran, e2_oran = e1_havuz / e1_toplam_mh, e2_havuz / e2_toplam_lh
x_e1_mh, x_e2_lh, x_miktar = 7_200, 5_250, 1_500
x_e1_pay, x_e2_pay = x_e1_mh * e1_oran, x_e2_lh * e2_oran
x_toplam_pay, x_birim_pay = x_e1_pay + x_e2_pay, (x_e1_pay + x_e2_pay) / x_miktar
assert (e1_oran, e2_oran, x_e1_pay, x_e2_pay, x_toplam_pay, x_birim_pay) == (20, 20, 144_000, 105_000, 249_000, 166)
q(f"İkinci dağıtım sonrası E1'de {tr(e1_havuz)} TL/{tr(e1_toplam_mh)} makine saati, E2'de {tr(e2_havuz)} TL/{tr(e2_toplam_lh)} işçilik saati vardır. X partisi E1'de {tr(x_e1_mh)} makine, E2'de {tr(x_e2_lh)} işçilik saati kullanmış ve {tr(x_miktar)} birim üretilmiştir. X'in toplam ve birim GÜG payı nedir?",
  f"{tr(x_toplam_pay)} TL toplam ve {tr(x_birim_pay)} TL/birim",
  [f"{tr(x_e1_pay)} TL toplam ve {tr(x_e1_pay/x_miktar)} TL/birim",
   f"{tr(x_e2_pay)} TL toplam ve {tr(x_e2_pay/x_miktar)} TL/birim",
   f"{tr(e1_havuz+e2_havuz)} TL toplam ve {tr((e1_havuz+e2_havuz)/x_miktar)} TL/birim",
   f"{tr(x_e1_mh+x_e2_lh)} TL toplam ve {tr(x_miktar)} TL/birim"],
  f"Her iki bölüm oranı {tr(e1_oran)} TL'dir. E1 payı {tr(x_e1_mh)} × {tr(e1_oran)} = {tr(x_e1_pay)} TL; E2 payı {tr(x_e2_lh)} × {tr(e2_oran)} = {tr(x_e2_pay)} TL'dir. Toplam {tr(x_toplam_pay)} TL, birim pay {tr(x_birim_pay)} TL olur.",
  "TMS 2 par. 12 - bölüm faaliyetleri üzerinden mamule GÜG dağıtımı", "hard")


print("TOPLAM:", len(Q))


# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base


if __name__ == "__main__":
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    letters = gen_letters(len(Q), SEED)
    out = []
    for i, it in enumerate(Q):
        ans = letters[i]
        ch = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            ch[k] = d
        assert len(set(ch.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "lessonId": L, "topicId": T,
            "question": it["stem"], "choices": ch, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", LBL],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-16T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "2026-07-16",
            "sourceUpdatedAt": "2026-07-16T00:00:00Z", "isPremium": False, "isActive": True,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = sum(1 for x in out if len(MARK.findall(x["question"])) >= 2)
    print(f"yazıldı: {len(out)} soru | öncüllü {onc} | harf {''.join(x['correctAnswer'] for x in out)[:40]}…")
