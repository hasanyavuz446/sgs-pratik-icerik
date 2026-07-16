# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 2 Stoklar — 60 soru.
⚠️ Babanın listesinde "TMS 3" yazıyordu; KGK 2026 seti (Kırmızı Kitap) kapağı
   "TMS 2 STOKLAR" — doğrulandı, numara düzeltildi.
Aritmetik python'da hesaplanır. Doğru şık KISA, çeldiriciler UZUN."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_2_stoklar"
PREFIX, SEED = "std-tms2-gen", 20260922
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_2_stoklar.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Amaç, kapsam, tanım (10) ────────────────────────────────────────────
q("TMS 2'nin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Stoklarla ilgili muhasebe uygulamalarını, özellikle varlık olarak izlenecek maliyetin belirlenmesini düzenlemektir",
  ["İşletmenin stoklarını kaç adet tutması gerektiğini belirleyen bir stok yönetimi standardıdır",
   "Stokların satış fiyatının nasıl belirleneceğini gösteren bir fiyatlandırma standardı niteliğindedir",
   "Yalnızca stok sayımının nasıl yapılacağını düzenleyen bir denetim standardı olarak yayımlanmıştır",
   "Stokların vergi matrahındaki değerini belirleyen bir vergi mevzuatı düzenlemesi niteliğindedir"],
  "TMS 2: bu Standardın amacı stoklarla ilgili muhasebe işlemlerini düzenlemektir. Temel konu, varlık olarak muhasebeleştirilecek ve ilgili hasılat muhasebeleştirilinceye kadar taşınacak maliyetin belirlenmesidir.",
  "TMS 2 - amaç")

q("TMS 2'ye göre stok tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Olağan iş akışı içinde satılmak üzere elde tutulan, üretim sürecindeki ya da üretimde kullanılacak varlıklardır",
  ["İşletmenin uzun vadeli kullanım amacıyla elde tuttuğu makine ve teçhizatı ifade eden varlıklardır",
   "İşletmenin değer artışı beklentisiyle yatırım amaçlı elde tuttuğu gayrimenkulleri kapsamaktadır",
   "İşletmenin üçüncü kişilerden olan alacaklarını gösteren ve nakde çevrilecek varlıkları ifade eder",
   "İşletmenin ortaklarına dağıtmayı planladığı kâr payını gösteren bir özkaynak kalemi niteliğindedir"],
  "TMS 2: stoklar; olağan iş akışı içinde satılmak için elde tutulan, satılmak üzere üretilmekte olan ya da üretim sürecinde veya hizmet sunumunda kullanılacak ilk madde ve malzeme şeklindeki varlıklardır.",
  "TMS 2 - stok tanımı")

q("TMS 2'ye göre stokların ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Stoklar, maliyet ile net gerçekleşebilir değerden düşük olanıyla ölçülür",
  ["Stoklar her hâlde maliyet değeriyle ölçülür; net gerçekleşebilir değer hiç dikkate alınmaz",
   "Stoklar her hâlde net gerçekleşebilir değerle ölçülür; maliyet değeri hiç kullanılmamaktadır",
   "Stoklar maliyet ile net gerçekleşebilir değerden yüksek olanıyla ölçülmek zorunda tutulmuştur",
   "Stokların ölçüm esası standartta belirlenmemiş olup her işletme serbestçe seçebilmektedir"],
  "TMS 2: stoklar, maliyet ve net gerçekleşebilir değerden düşük olanı ile ölçülür. Bu, varlığın satışından elde edilecek tutarın üzerinde bir değerle taşınmamasını sağlar.",
  "TMS 2 - ölçüm ilkesi")

q("Net gerçekleşebilir değer bakımından aşağıdakilerden hangisi doğrudur?",
  "Olağan iş akışı içindeki tahmini satış fiyatından tamamlanma ve satış maliyetleri düşülerek bulunur",
  ["Piyasa katılımcıları arasındaki olağan işlemde oluşacak fiyatı gösteren piyasa temelli bir ölçümdür",
   "Stokun edinilmesi sırasında fiilen katlanılan tarihi maliyeti gösteren bir tutarı ifade etmektedir",
   "Stokun benzerinin bugün edinilmesi için ödenecek bedeli gösteren bir cari maliyet ölçümüdür",
   "Net gerçekleşebilir değer, stokun defter değerinin iki katı olarak hesaplanan bir üst sınırdır"],
  "TMS 2: net gerçekleşebilir değer, işin normal akışı içinde tahmini satış fiyatından, tahmini tamamlanma maliyeti ve satışı gerçekleştirmek için gerekli tahmini maliyetlerin düşülmesiyle bulunan tutardır. İşletmeye özgüdür.",
  "TMS 2 - net gerçekleşebilir değer")

q("Net gerçekleşebilir değer ile gerçeğe uygun değer farkı bakımından aşağıdakilerden hangisi doğrudur?",
  "Net gerçekleşebilir değer işletmeye özgüdür; gerçeğe uygun değer ise piyasa bakışını yansıtır",
  ["Net gerçekleşebilir değer piyasa bakışını, gerçeğe uygun değer ise işletmeye özgü tutarı yansıtır",
   "İkisi arasında hiçbir fark bulunmayıp aynı tutarı ifade eden eş anlamlı kavramlar niteliğindedir",
   "Net gerçekleşebilir değer geçmiş maliyeti, gerçeğe uygun değer ise gelecekteki maliyeti gösterir",
   "İki kavram da yalnızca maddi duran varlıklarda kullanılır; stoklarda hiç uygulanmamaktadır"],
  "TMS 2: net gerçekleşebilir değer işletmeye özgü bir tutardır; gerçeğe uygun değer ise piyasa katılımcılarının bakış açısını yansıtır. Bir stokun net gerçekleşebilir değeri, gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarına eşit olmayabilir.",
  "TMS 2 - NGD/GUD farkı")

q("Hizmet sunan işletmelerde stok bakımından aşağıdakilerden hangisi doğrudur?",
  "Hizmet sunan işletmelerde stoklar, hasılatı henüz muhasebeleştirilmemiş hizmetin maliyetlerinden oluşur",
  ["Hizmet sunan işletmelerde hiçbir hâlde stok kavramı bulunmaz ve stok kaydı yapılamamaktadır",
   "Hizmet işletmelerinde stok, satış personeline ödenen prim ve komisyonlardan oluşmaktadır",
   "Hizmet işletmelerinde stok, genel yönetim giderlerinin tamamını kapsayan bir kalem niteliğindedir",
   "Hizmet işletmelerinde stok, işletmenin sahip olduğu tüm nakit ve alacakları ifade etmektedir"],
  "TMS 2: hizmet sunan işletmelerde stoklar, hasılatı henüz muhasebeleştirilmemiş hizmetin maliyetlerinden oluşur. Bu maliyetler esas olarak hizmeti sunan personelin ücretleri ve diğer doğrudan maliyetlerdir.",
  "TMS 2 - hizmet işletmelerinde stok")

q("TMS 2'nin kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Tüm stoklara uygulanır; ancak inşaat sözleşmeleri ve finansal araçlar gibi bazı kalemler kapsam dışıdır",
  ["TMS 2 istisnasız tüm varlıklara uygulanır; hiçbir kapsam dışı kalem öngörülmemiş bulunmaktadır",
   "TMS 2 yalnızca ticari mallara uygulanır; mamul ve yarı mamuller kapsam dışında bırakılmıştır",
   "TMS 2 yalnızca üretim işletmelerinde uygulanır; ticaret işletmelerini hiç kapsamamaktadır",
   "TMS 2 yalnızca ithal edilen stoklara uygulanır; yurt içinden alınan stoklar kapsam dışıdır"],
  "TMS 2 stoklara ilişkin genel standarttır; ancak inşaat sözleşmelerinden kaynaklanan işler, finansal araçlar ile tarımsal faaliyete ilişkin canlı varlıklar ve hasat zamanındaki tarımsal ürünler bu Standardın kapsamı dışındadır.",
  "TMS 2 - kapsam")

q("Aşağıdakilerden hangileri TMS 2'ye göre stok sayılır?\n\nI. Olağan iş akışında satılmak üzere elde tutulan ticari mallar\n\nII. Üretim sürecindeki yarı mamuller\n\nIII. Üretimde kullanılacak ilk madde ve malzeme",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 2: stoklar; satılmak üzere elde tutulanlar (I), satılmak üzere üretilmekte olanlar (II) ve üretim/hizmet sürecinde kullanılacak ilk madde ve malzemeler (III) olarak üç grupta tanımlanır. Üçü de stoktur.",
  "TMS 2 - stok tanımı")

q("Aşağıdaki ifadelerden hangileri TMS 2 bakımından doğrudur?\n\nI. Stoklar maliyet ile NGD'den düşük olanıyla ölçülür\n\nII. NGD işletmeye özgü bir tutardır\n\nIII. Yatırım amaçlı gayrimenkuller stok sayılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Stoklar maliyet ile NGD'den düşük olanıyla ölçülür (I) ve NGD işletmeye özgüdür (II). Yatırım amaçlı gayrimenkuller ise TMS 40 kapsamındadır, stok değildir; bu nedenle III yanlıştır.",
  "TMS 2 - ölçüm ve kapsam")

sf, tam, sat = 80_000, 6_000, 4_000
q(f"Bir stokun tahmini satış fiyatı {tr(sf)} TL, tamamlanma maliyeti {tr(tam)} TL ve satış maliyetleri {tr(sat)} TL'dir. Net gerçekleşebilir değer kaç TL'dir?",
  f"{tr(sf-tam-sat)} TL",
  [f"{tr(sf-tam)} TL", f"{tr(sf+tam+sat)} TL", f"{tr(sf-sat)} TL", f"{tr(sf)} TL"],
  f"Net gerçekleşebilir değer = Tahmini satış fiyatı − Tamamlanma maliyeti − Satış maliyetleri = {tr(sf)} − {tr(tam)} − {tr(sat)} = {tr(sf-tam-sat)} TL.",
  "TMS 2 - net gerçekleşebilir değer")

# ── B. Stok maliyeti (16) ──────────────────────────────────────────────────
q("TMS 2'ye göre stok maliyetinin unsurları bakımından aşağıdakilerden hangisi doğrudur?",
  "Satın alma maliyetleri, dönüştürme maliyetleri ve stokları mevcut konum ve duruma getiren diğer maliyetlerden oluşur",
  ["Yalnızca satın alma bedelinden oluşur; taşıma ve dönüştürme maliyetleri hiç dâhil edilmez",
   "Yalnızca dönüştürme maliyetlerinden oluşur; satın alma maliyetleri kapsam dışında bırakılmıştır",
   "Stok maliyetinin unsurları standartta belirlenmemiş olup her işletme serbestçe belirlemektedir",
   "Stok maliyeti yalnızca satış fiyatının belirli bir yüzdesi olarak hesaplanan bir tutardır"],
  "TMS 2: stok maliyeti; tüm satın alma maliyetlerini, dönüştürme maliyetlerini ve stokların mevcut konum ve duruma getirilmesi için katlanılan diğer maliyetleri içerir.",
  "TMS 2 - maliyet unsurları")

q("Satın alma maliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Satın alma fiyatı, iade alınamayan vergiler ile taşıma ve yükleme-boşaltma maliyetlerini içerir; ticari iskontolar düşülür",
  ["Yalnızca satın alma fiyatından oluşur; taşıma ve vergi gibi hiçbir ek maliyet eklenmemektedir",
   "Ticari iskontolar satın alma maliyetine eklenerek maliyet artırılmak zorunda tutulmaktadır",
   "Sonradan iade alınabilecek vergiler de satın alma maliyetine dâhil edilerek stokta izlenmektedir",
   "Satın alma maliyeti yalnızca ithal edilen stoklar için hesaplanır; yurt içi alımlarda hesaplanmaz"],
  "TMS 2: satın alma maliyeti; satın alma fiyatı, ithalat vergileri ve diğer vergiler (işletmece vergi idaresinden iade alınabilecekler hariç), nakliye, yükleme-boşaltma ve doğrudan ilişkilendirilebilen diğer maliyetleri içerir. Ticari iskontolar ve benzeri indirimler düşülür.",
  "TMS 2 - satın alma maliyeti")

q("Dönüştürme maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretimle doğrudan ilişkili işçilik ile sistematik olarak dağıtılan sabit ve değişken genel üretim giderlerini içerir",
  ["Yalnızca direkt işçilik maliyetlerinden oluşur; genel üretim giderleri hiç dâhil edilmemektedir",
   "Yalnızca genel üretim giderlerinden oluşur; direkt işçilik kapsam dışında bırakılmış durumdadır",
   "Pazarlama ve genel yönetim giderlerini de içeren geniş kapsamlı bir maliyet grubunu ifade eder",
   "Dönüştürme maliyeti kavramı TMS 2'de yer almayan ve uygulanmayan bir kavram niteliğindedir"],
  "TMS 2: dönüştürme maliyetleri, direkt işçilik gibi üretimle doğrudan ilişkili maliyetleri ve ilk madde ve malzemenin mamule dönüştürülmesinde katlanılan sabit ve değişken genel üretim giderlerinin sistematik dağıtımını içerir.",
  "TMS 2 - dönüştürme maliyetleri")

q("Sabit genel üretim giderlerinin dağıtımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Sabit genel üretim giderleri normal kapasite esas alınarak dönüştürme maliyetine dağıtılır",
  ["Sabit genel üretim giderleri her hâlde fiili üretim miktarına göre dağıtılmak zorunda tutulmuştur",
   "Sabit genel üretim giderleri hiçbir hâlde stok maliyetine dağıtılmaz; tümü dönem gideri yazılır",
   "Sabit genel üretim giderleri her hâlde teorik azami kapasiteye göre dağıtılmak zorundadır",
   "Sabit genel üretim giderlerinin dağıtımı standartta düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 2: sabit genel üretim giderlerinin dönüştürme maliyetlerine dağıtımı, üretim tesislerinin normal kapasitesi esas alınarak yapılır. Normal kapasite, olağan koşullarda birkaç dönem beklenen ortalama üretimdir.",
  "TMS 2 - sabit GÜG dağıtımı")

q("Düşük üretim veya atıl kapasite hâlinde sabit genel üretim giderleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Dağıtılmayan sabit genel üretim giderleri stok maliyetine eklenmez; oluştuğu dönemde gider yazılır",
  ["Dağıtılmayan sabit giderler her hâlde stok maliyetine eklenerek mamullere yüklenmek zorundadır",
   "Dağıtılmayan sabit giderler gelecek dönemin stok maliyetine aktarılarak orada izlenmektedir",
   "Düşük üretim hâlinde her birime yüklenen sabit gider payı artırılarak toplam dağıtılmaktadır",
   "Düşük üretim hâlinde sabit giderlerin tamamı özkaynaklardan doğrudan indirilmek zorundadır"],
  "TMS 2: her bir üretim birimine dağıtılan sabit genel üretim gideri tutarı, düşük kapasite kullanımı ya da atıl kapasite nedeniyle artırılmaz. Dağıtılmayan genel üretim giderleri, gerçekleştiği dönemde gider olarak muhasebeleştirilir.",
  "TMS 2 - düşük üretim")

q("Anormal derecede yüksek üretim hâlinde sabit genel üretim giderleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Her bir birime dağıtılan sabit gider payı azaltılır; böylece stoklar maliyetin üzerinde ölçülmez",
  ["Her bir birime dağıtılan sabit gider payı artırılarak stok maliyeti yükseltilmek zorundadır",
   "Yüksek üretim hâlinde sabit giderlerin tamamı dönem gideri olarak yazılmak zorunda tutulmuştur",
   "Yüksek üretim hâlinde sabit gider dağıtımı hiç yapılmaz; stoklar yalnızca DİMM ile ölçülür",
   "Anormal yüksek üretim standartta düzenlenmemiş olup normal üretimle aynı işlem görmektedir"],
  "TMS 2: anormal derecede yüksek üretim olması durumunda, her bir üretim birimine dağıtılan sabit genel üretim maliyeti tutarı azaltılır; böylece stoklar maliyetin üzerinde bir değerle ölçülmemiş olur.",
  "TMS 2 - anormal yüksek üretim")

q("Değişken genel üretim giderlerinin dağıtımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişken genel üretim giderleri, üretim tesislerinin fiili kullanımı esas alınarak dağıtılır",
  ["Değişken genel üretim giderleri her hâlde normal kapasite esas alınarak dağıtılmak zorundadır",
   "Değişken genel üretim giderleri hiçbir hâlde stok maliyetine dağıtılmaz; dönem gideri yazılır",
   "Değişken genel üretim giderleri teorik azami kapasiteye göre dağıtılmak zorunda tutulmuştur",
   "Değişken genel üretim giderlerinin dağıtımında hiçbir ölçüt bulunmayıp rastgele yapılmaktadır"],
  "TMS 2: değişken genel üretim giderleri, üretim tesislerinin fiili kullanımı esas alınarak her bir üretim birimine dağıtılır. Sabit giderlerde ise normal kapasite esas alınır.",
  "TMS 2 - değişken GÜG dağıtımı")

q("TMS 2'ye göre stok maliyetine alınmayan giderler bakımından aşağıdakilerden hangisi doğrudur?",
  "Normalin üstündeki fire, depolama (üretim aşaması gerektirmedikçe), genel yönetim ve satış giderleri stok maliyetine alınmaz",
  ["Tüm giderler her hâlde stok maliyetine eklenir; hiçbir gider kapsam dışında bırakılmamaktadır",
   "Yalnızca satış giderleri stok maliyetine alınmaz; diğer tüm giderler stokta izlenmektedir",
   "Normalin üstündeki fire de stok maliyetine eklenerek mamullere yüklenmek zorunda tutulmuştur",
   "Stok maliyetine alınmayan gider kavramı TMS 2'de düzenlenmemiş olup uygulanmamaktadır"],
  "TMS 2 par. 16: normalin üstündeki fire ve kayıplar, sonraki üretim aşaması için zorunlu olmayan depolama giderleri, stokun mevcut konum ve duruma getirilmesine katkısı olmayan genel yönetim giderleri ile satış giderleri stok maliyetine alınmaz; oluştukları dönemde gider yazılır.",
  "TMS 2 - maliyete alınmayan giderler")

q("Vadeli alım koşullarındaki finansman unsuru bakımından aşağıdakilerden hangisi doğrudur?",
  "Peşin alım fiyatı ile ödenen tutar arasındaki fark finansman gideri olarak finansman süresince muhasebeleştirilir",
  ["Vadeli alımdaki tüm tutar her hâlde stok maliyetine eklenerek stokta izlenmek zorundadır",
   "Vadeli alımlarda finansman unsuru hiç dikkate alınmaz; peşin fiyat ile vadeli fiyat aynı sayılır",
   "Vadeli alımdaki finansman unsuru doğrudan özkaynaklardan indirilmek zorunda tutulmaktadır",
   "Vadeli alım koşulları TMS 2'de düzenlenmemiş olup uygulamada hiç dikkate alınmamaktadır"],
  "TMS 2: bir işletme stokları vadeli ödeme koşuluyla almış olabilir. Anlaşma fiilen bir finansman unsuru içerdiğinde (peşin alım fiyatı ile ödenen tutar arasındaki fark gibi), bu unsur finansman süresi boyunca faiz gideri olarak muhasebeleştirilir.",
  "TMS 2 - finansman unsuru")

lf, isk, tas, ver = 320_000, 20_000, 18_000, 12_000
q(f"Ana malzemenin liste fiyatı {tr(lf)} TL, ticari iskonto {tr(isk)} TL, taşıma gideri {tr(tas)} TL ve iade alınamayan vergi {tr(ver)} TL'dir. TMS 2'ye göre satın alma maliyeti kaç TL'dir?",
  f"{tr(lf-isk+tas+ver)} TL",
  [f"{tr(lf+isk+tas+ver)} TL", f"{tr(lf-isk)} TL", f"{tr(lf-isk-tas-ver)} TL", f"{tr(lf)} TL"],
  f"Satın alma maliyeti = Liste fiyatı − Ticari iskonto + Taşıma + İade alınamayan vergi = {tr(lf)} − {tr(isk)} + {tr(tas)} + {tr(ver)} = {tr(lf-isk+tas+ver)} TL.",
  "TMS 2 - satın alma maliyeti")

lf2, iade_alinabilir = 250_000, 45_000
q(f"Bir stokun satın alma fiyatı {tr(lf2)} TL olup ayrıca sonradan vergi idaresinden iade alınabilecek {tr(iade_alinabilir)} TL vergi ödenmiştir. Başka maliyet yoksa stokun satın alma maliyeti kaç TL'dir?",
  f"{tr(lf2)} TL",
  [f"{tr(lf2+iade_alinabilir)} TL", f"{tr(lf2-iade_alinabilir)} TL", f"{tr(iade_alinabilir)} TL", f"{tr(lf2+iade_alinabilir*2)} TL"],
  f"TMS 2: sonradan iade alınabilecek vergiler satın alma maliyetine dâhil edilmez. Bu nedenle maliyet yalnızca satın alma fiyatı olan {tr(lf2)} TL'dir; {tr(iade_alinabilir)} TL vergi indirim konusu yapılır.",
  "TMS 2 - iade alınabilen vergi")

sgug, nk, fiili = 420_000, 14_000, 11_000
yuk = sgug / nk * fiili
q(f"Sabit genel üretim gideri {tr(sgug)} TL, normal kapasite {tr(nk)} birim ve fiili üretim {tr(fiili)} birimdir. TMS 2'ye göre stok maliyetine yüklenecek sabit genel üretim gideri kaç TL'dir?",
  f"{tr(int(yuk))} TL",
  [f"{tr(sgug)} TL", f"{tr(int(sgug-yuk))} TL", f"{tr(int(sgug/fiili*nk))} TL", f"{tr(int(sgug/nk))} TL"],
  f"Birim sabit GÜG = {tr(sgug)} / {tr(nk)} = {tr(int(sgug/nk))} TL. Fiili üretime yüklenen = {tr(int(sgug/nk))} × {tr(fiili)} = {tr(int(yuk))} TL. Dağıtılmayan {tr(int(sgug-yuk))} TL dönem gideri yazılır.",
  "TMS 2 - normal kapasite")

toplam_mlz, endirekt, anormal_fire = 285_000, 15_000, 10_000
q(f"Üretime verilen toplam malzeme {tr(toplam_mlz)} TL'dir. Bunun {tr(endirekt)} TL'si endirekt malzeme, {tr(anormal_fire)} TL'si normalin üstündeki firedir. TMS 2'ye göre stok maliyetine alınacak direkt malzeme kaç TL'dir?",
  f"{tr(toplam_mlz-endirekt-anormal_fire)} TL",
  [f"{tr(toplam_mlz-endirekt)} TL", f"{tr(toplam_mlz-anormal_fire)} TL", f"{tr(toplam_mlz)} TL", f"{tr(endirekt+anormal_fire)} TL"],
  f"Endirekt malzeme GÜG içinde izlenir; normalin üstündeki fire ise TMS 2 par. 16 uyarınca stok maliyetine alınmaz, dönem gideri yazılır. Direkt malzeme = {tr(toplam_mlz)} − {tr(endirekt)} − {tr(anormal_fire)} = {tr(toplam_mlz-endirekt-anormal_fire)} TL.",
  "TMS 2 - maliyete alınmayan giderler")

q("Bir işletme, ürettiği malları depoda beklettiği için katlandığı ve sonraki üretim aşaması için zorunlu olmayan depolama giderini stok maliyetine eklemek istemektedir. TMS 2 bakımından aşağıdakilerden hangisi doğrudur?",
  "Sonraki üretim aşaması için zorunlu olmayan depolama gideri stok maliyetine alınmaz; dönem gideri yazılır",
  ["Tüm depolama giderleri her hâlde stok maliyetine eklenerek stokta izlenmek zorunda tutulmuştur",
   "Depolama gideri her hâlde satış gideri olarak sınıflandırılır ve pazarlama bölümüne yüklenir",
   "Depolama gideri doğrudan özkaynaklardan indirilir; kâr veya zarara hiç yansıtılmamaktadır",
   "Depolama giderleri TMS 2'de düzenlenmemiş olup işletmenin serbest tercihine bırakılmıştır"],
  "TMS 2 par. 16(b): bir sonraki üretim aşaması için zorunlu olanlar dışındaki depolama giderleri stok maliyetine dâhil edilmez ve oluştuğu dönemde gider olarak muhasebeleştirilir.",
  "TMS 2 - depolama gideri (senaryo)")

q("Aşağıdakilerden hangileri TMS 2'ye göre stok maliyetine dâhil edilir?\n\nI. Satın alma fiyatı\n\nII. Edinimle doğrudan ilişkili taşıma gideri\n\nIII. Satış ve pazarlama giderleri",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Satın alma fiyatı (I) ve edinimle doğrudan ilişkili taşıma gideri (II) stok maliyetine girer. Satış ve pazarlama giderleri (III) ise TMS 2 par. 16 uyarınca stok maliyetine alınmaz; bu nedenle yanlıştır.",
  "TMS 2 - maliyet unsurları")

q("Aşağıdaki ifadelerden hangileri TMS 2 bakımından doğrudur?\n\nI. Sabit GÜG normal kapasiteye göre dağıtılır\n\nII. Değişken GÜG fiili kullanıma göre dağıtılır\n\nIII. Normalin üstündeki fire stok maliyetine eklenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sabit GÜG normal kapasiteye (I), değişken GÜG fiili kullanıma (II) göre dağıtılır. Normalin üstündeki fire ise stok maliyetine alınmaz, dönem gideri yazılır; bu nedenle III yanlıştır.",
  "TMS 2 - GÜG dağıtımı")

# ── C. Maliyet hesaplama yöntemleri (14) ───────────────────────────────────
q("TMS 2'ye göre kabul edilen maliyet hesaplama yöntemleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Normal şartlarda birbirinin yerine geçebilen stoklarda ilk giren ilk çıkar ya da ağırlıklı ortalama maliyet yöntemi kullanılır",
  ["Yalnızca son giren ilk çıkar yöntemi kullanılabilir; diğer yöntemler kesin olarak yasaklanmıştır",
   "İşletme dilediği yöntemi hiçbir ölçüt aranmaksızın ve her yıl değiştirerek kullanabilmektedir",
   "TMS 2 hiçbir maliyet hesaplama yöntemi öngörmez; konu tümüyle vergi mevzuatına bırakılmıştır",
   "Tüm stoklarda her hâlde özel maliyet yöntemi kullanılmak zorunda olup başka yöntem kabul edilmez"],
  "TMS 2: normal şartlarda birbirleriyle ikame edilebilen stok kalemlerinin maliyeti, ilk giren ilk çıkar (FIFO) veya ağırlıklı ortalama maliyet formülü kullanılarak belirlenir. LIFO (son giren ilk çıkar) TMS 2'de kabul edilmez.",
  "TMS 2 - maliyet yöntemleri")

q("Son giren ilk çıkar (LIFO) yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 2 kapsamında LIFO yönteminin kullanılmasına izin verilmez",
  ["LIFO, TMS 2'de kabul edilen üç yöntemden biri olup serbestçe kullanılabilmektedir",
   "LIFO yalnızca üretim işletmelerinde kullanılabilir; ticaret işletmelerinde yasaklanmıştır",
   "LIFO her hâlde kullanılmak zorunda olan tek yöntem olup FIFO kabul edilmemektedir",
   "LIFO yalnızca enflasyon dönemlerinde kullanılabilen özel bir yöntem olarak düzenlenmiştir"],
  "TMS 2, stok maliyetinin belirlenmesinde ilk giren ilk çıkar (FIFO) ve ağırlıklı ortalama maliyet formüllerine izin verir; son giren ilk çıkar (LIFO) yöntemi kabul edilmez.",
  "TMS 2 - LIFO yasağı")

q("Normal şartlarda ikame edilemeyen stoklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Özel projeler için ayrılan ve normalde ikame edilemeyen stokların maliyeti, her bir varlık için ayrı ayrı belirlenir",
  ["Bu tür stoklarda da her hâlde ağırlıklı ortalama yöntemi kullanılmak zorunda tutulmaktadır",
   "Bu tür stoklarda hiçbir maliyet belirlenmez; doğrudan net gerçekleşebilir değerle ölçülür",
   "İkame edilemeyen stok kavramı TMS 2'de yer almayan ve uygulanmayan bir kavram niteliğindedir",
   "Bu tür stokların maliyeti yalnızca satış fiyatının yarısı olarak belirlenmek zorundadır"],
  "TMS 2: normal şartlarda ikame edilemeyen stok kalemleri ile özel projeler için üretilen ve ayrılan mal veya hizmetlerin maliyeti, her bir varlığa ilişkin özel maliyetlerin belirlenmesi (özel tanımlama) yoluyla bulunur.",
  "TMS 2 - özel tanımlama")

q("İlk giren ilk çıkar (FIFO) yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "İlk alınan stokların ilk satıldığı varsayılır; dönem sonu stok en son alınanlardan oluşur",
  ["Son alınan stokların ilk satıldığı varsayılır; dönem sonu stok en eski alımlardan oluşmaktadır",
   "Tüm alımların ortalaması alınarak birim maliyet bulunur; alım sırası hiç dikkate alınmaz",
   "Her bir stok kaleminin maliyeti ayrı ayrı belirlenir; hiçbir akış varsayımı kullanılmamaktadır",
   "FIFO yönteminde stoklar her hâlde satış fiyatı üzerinden değerlenmek zorunda tutulmuştur"],
  "FIFO yönteminde ilk alınan (veya üretilen) stokların ilk satıldığı varsayılır; dolayısıyla dönem sonunda kalan stoklar en son alınan veya üretilenlerden oluşur.",
  "TMS 2 - FIFO")

q("Ağırlıklı ortalama maliyet yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem başı stok ile dönem içi alımların ağırlıklı ortalaması alınarak birim maliyet belirlenir",
  ["İlk alınan stokların ilk satıldığı varsayılarak birim maliyet belirlenen bir yöntemdir",
   "Son alınan stokların ilk satıldığı varsayımına dayanan ve TMS 2'de kabul edilen bir yöntemdir",
   "Her bir stok kaleminin maliyetinin ayrı ayrı izlendiği özel tanımlama yöntemini ifade etmektedir",
   "Ağırlıklı ortalama yöntemi TMS 2'de kabul edilmeyen ve kullanılması yasak bir yöntemdir"],
  "TMS 2: ağırlıklı ortalama maliyet yönteminde her bir kalemin maliyeti, dönem başındaki benzer kalemlerin ağırlıklı ortalama maliyeti ile dönem içinde alınan veya üretilenlerin ağırlıklı ortalama maliyetinden bulunur.",
  "TMS 2 - ağırlıklı ortalama")

q("Maliyet hesaplama yönteminin tutarlı uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, benzer özellik ve kullanıma sahip tüm stoklar için aynı maliyet hesaplama yöntemini kullanır",
  ["İşletme her stok kalemi için farklı bir yöntem seçmek zorunda olup tutarlılık aranmamaktadır",
   "İşletme yöntemini her yıl değiştirmek zorunda olup aynı yöntemi iki yıl kullanamamaktadır",
   "Yöntem seçimi tümüyle serbest olup benzer stoklarda farklı yöntemler kullanılabilmektedir",
   "Yöntemin tutarlı uygulanması TMS 2'de düzenlenmemiş olup uygulamada aranmamaktadır"],
  "TMS 2: işletme, benzer özellik ve kullanıma sahip tüm stoklar için aynı maliyet hesaplama yöntemini kullanır. Farklı özellik veya kullanımdaki stoklar için farklı yöntemler uygun olabilir.",
  "TMS 2 - yöntem tutarlılığı")

b_adet, b_fiyat, a_adet, a_fiyat, satilan = 80, 10, 60, 15, 100
fifo_smm = b_adet * b_fiyat + (satilan - b_adet) * a_fiyat
q(f"Dönem başı stok {tr(b_adet)} birim × {tr(b_fiyat)} TL, dönem içi alış {tr(a_adet)} birim × {tr(a_fiyat)} TL'dir. FIFO yöntemine göre {tr(satilan)} birim satılırsa satılan stokun maliyeti kaç TL'dir?",
  f"{tr(fifo_smm)} TL",
  [f"{tr(satilan*a_fiyat)} TL", f"{tr(satilan*b_fiyat)} TL",
   f"{tr(int(satilan*((b_adet*b_fiyat+a_adet*a_fiyat)/(b_adet+a_adet))))} TL",
   f"{tr(a_adet*a_fiyat+(satilan-a_adet)*b_fiyat)} TL"],
  f"FIFO'da önce en eski stok çıkar: {tr(b_adet)} × {tr(b_fiyat)} = {tr(b_adet*b_fiyat)} TL, kalan {tr(satilan-b_adet)} birim yeni alıştan: {tr(satilan-b_adet)} × {tr(a_fiyat)} = {tr((satilan-b_adet)*a_fiyat)} TL. Toplam {tr(fifo_smm)} TL.",
  "TMS 2 - FIFO")

c_b, c_bf, c_a, c_af = 100, 20, 100, 30
ort = (c_b*c_bf + c_a*c_af) / (c_b + c_a)
q(f"Dönem başı {tr(c_b)} birim stok {tr(c_bf)} TL'den, dönem içi {tr(c_a)} birim {tr(c_af)} TL'den alınmıştır. Ağırlıklı ortalama birim maliyet kaç TL'dir?",
  f"{tr(int(ort))} TL",
  [f"{tr(c_af)} TL", f"{tr(c_bf)} TL", f"{tr(int((c_bf+c_af)/2)+3)} TL", f"{tr(c_b*c_bf+c_a*c_af)} TL"],
  f"Toplam maliyet = {tr(c_b)}×{tr(c_bf)} + {tr(c_a)}×{tr(c_af)} = {tr(c_b*c_bf+c_a*c_af)} TL; toplam miktar {tr(c_b+c_a)} birim. Ağırlıklı ortalama = {tr(c_b*c_bf+c_a*c_af)} / {tr(c_b+c_a)} = {tr(int(ort))} TL.",
  "TMS 2 - ağırlıklı ortalama")

d_b, d_bf, d_a, d_af, kalan = 50, 12, 50, 18, 40
ort2 = (d_b*d_bf + d_a*d_af) / (d_b + d_a)
q(f"Dönem başı {tr(d_b)} birim {tr(d_bf)} TL'den, dönem içi {tr(d_a)} birim {tr(d_af)} TL'dendir. Ağırlıklı ortalamaya göre dönem sonu {tr(kalan)} birim stokun maliyeti kaç TL'dir?",
  f"{tr(int(kalan*ort2))} TL",
  [f"{tr(kalan*d_bf)} TL", f"{tr(kalan*d_af)} TL", f"{tr(int(ort2))} TL", f"{tr(d_b*d_bf+d_a*d_af)} TL"],
  f"Ağırlıklı ortalama birim maliyet = ({tr(d_b)}×{tr(d_bf)} + {tr(d_a)}×{tr(d_af)}) / {tr(d_b+d_a)} = {tr(int(ort2))} TL. Dönem sonu stok = {tr(kalan)} × {tr(int(ort2))} = {tr(int(kalan*ort2))} TL.",
  "TMS 2 - ağırlıklı ortalama")

q("Perakende yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Benzer kâr marjına sahip çok sayıda kalemin hızla değiştiği perakende sektöründe, satış değerinden uygun brüt marj indirilerek maliyet bulunur",
  ["Perakende yöntemi TMS 2'de kabul edilmeyen ve kullanılması yasaklanmış bir yöntem niteliğindedir",
   "Perakende yöntemi yalnızca üretim işletmelerinde kullanılabilen özel bir maliyet yöntemidir",
   "Perakende yönteminde stoklar her hâlde satış fiyatıyla ölçülür; hiçbir indirim yapılmamaktadır",
   "Perakende yöntemi yalnızca tek bir stok kalemi bulunan işletmelerde uygulanabilmektedir"],
  "TMS 2: perakende yöntemi, benzer kâr marjına sahip, hızla değişen çok sayıda kalemden oluşan ve başka maliyet yöntemi uygulaması mümkün olmayan perakende sektöründe kullanılır; stok maliyeti, satış değerinden uygun bir brüt kâr marjı indirilerek bulunur.",
  "TMS 2 - perakende yöntemi")

q("Standart maliyet yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Sonuçları maliyete yakınsa maliyetin ölçümünde kolaylık amacıyla kullanılabilir; standartlar düzenli gözden geçirilir",
  ["Standart maliyet yöntemi TMS 2'de hiçbir hâlde kabul edilmeyen ve yasaklanan bir yöntemdir",
   "Standart maliyet yöntemi kullanılırken standartlar hiçbir zaman gözden geçirilmez ve sabit kalır",
   "Standart maliyet yöntemi, sonuçları gerçek maliyetten çok farklı olsa dahi serbestçe kullanılır",
   "Standart maliyet yöntemi yalnızca hizmet işletmelerinde kullanılabilen bir uygulamadır"],
  "TMS 2: standart maliyet yöntemi ve perakende yöntemi gibi maliyet ölçüm teknikleri, sonuçları maliyete yaklaşık olduğu takdirde kullanılabilir. Standart maliyetler düzenli olarak gözden geçirilir ve gerekiyorsa cari koşullara göre revize edilir.",
  "TMS 2 - standart maliyet")

q("Aşağıdakilerden hangileri TMS 2'ye göre kabul edilen maliyet hesaplama yöntemleridir?\n\nI. İlk giren ilk çıkar (FIFO)\n\nII. Ağırlıklı ortalama maliyet\n\nIII. Son giren ilk çıkar (LIFO)",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 2 ikame edilebilen stoklarda FIFO (I) ve ağırlıklı ortalama (II) yöntemlerine izin verir. LIFO (III) ise TMS 2 kapsamında kabul edilmez; bu nedenle yanlıştır.",
  "TMS 2 - maliyet yöntemleri")

q("Aşağıdaki ifadelerden hangileri TMS 2 bakımından doğrudur?\n\nI. İkame edilemeyen stoklarda özel tanımlama kullanılır\n\nII. Benzer stoklarda aynı yöntem tutarlı uygulanır\n\nIII. Standart maliyet, sonuçları maliyetten çok farklı olsa da kullanılabilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "İkame edilemeyen stoklarda özel tanımlama kullanılır (I) ve benzer stoklarda yöntem tutarlı uygulanır (II). Standart maliyet ise ancak sonuçları maliyete yaklaşıksa kullanılabilir; bu nedenle III yanlıştır.",
  "TMS 2 - yöntemler")

q("Bir işletme, aynı özellikteki ticari mallarının bir kısmında FIFO, bir kısmında ağırlıklı ortalama yöntemi kullanmak istemektedir. TMS 2 bakımından aşağıdakilerden hangisi doğrudur?",
  "Benzer özellik ve kullanımdaki stoklarda aynı yöntem kullanılmalıdır; iki farklı yöntem uygulanamaz",
  ["İşletme aynı stok grubunda dilediği kadar farklı yöntemi serbestçe kullanabilmektedir",
   "İşletme her hâlde tüm stoklarında tek bir yöntem kullanmak zorunda olup istisnası yoktur",
   "İşletme yöntem seçimini her ay değiştirmek zorunda olup tutarlılık aranmamaktadır",
   "Farklı yöntem kullanılması hâlinde finansal tablolar kendiliğinden geçersiz sayılmaktadır"],
  "TMS 2: işletme, benzer özellik ve kullanıma sahip tüm stoklar için aynı maliyet hesaplama yöntemini kullanır. Ancak farklı özellik veya kullanımdaki stok grupları için farklı yöntemler uygulanabilir.",
  "TMS 2 - yöntem tutarlılığı (senaryo)")

# ── D. Değer düşüklüğü ve gider yazma (12) ─────────────────────────────────
q("Stokların net gerçekleşebilir değere indirgenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet net gerçekleşebilir değerin üzerindeyse stok net gerçekleşebilir değere indirgenir; fark gider yazılır",
  ["Maliyet net gerçekleşebilir değerin üzerinde olsa dahi stok her hâlde maliyetle taşınmaya devam eder",
   "Net gerçekleşebilir değer maliyetin üzerindeyse stok net gerçekleşebilir değere yükseltilmek zorundadır",
   "İndirgeme farkı doğrudan özkaynaklardan indirilir; kâr veya zarara hiç yansıtılmamaktadır",
   "Değer düşüklüğü kavramı TMS 2'de yer almayan ve uygulanmayan bir kavram niteliğindedir"],
  "TMS 2: stokların maliyeti net gerçekleşebilir değerinin üzerindeyse (zarar görmüş, kısmen kullanılamaz hâle gelmiş, satış fiyatı düşmüşse) stoklar net gerçekleşebilir değere indirgenir ve indirgeme tutarı gider olarak muhasebeleştirilir.",
  "TMS 2 - değer düşüklüğü")

q("Değer düşüklüğü değerlendirmesinin yapılma düzeyi bakımından aşağıdakilerden hangisi doğrudur?",
  "Net gerçekleşebilir değere indirgeme genellikle her bir stok kalemi bazında yapılır",
  ["İndirgeme her hâlde tüm stokların toplamı üzerinden ve tek seferde yapılmak zorunda tutulmuştur",
   "İndirgeme yalnızca işletmenin tüm varlıkları birlikte değerlendirilerek yapılabilmektedir",
   "İndirgeme yalnızca satış fiyatı en yüksek olan tek bir kalem için yapılır; diğerleri değerlendirilmez",
   "Değerlendirme düzeyi TMS 2'de düzenlenmemiş olup işletmenin serbest tercihine bırakılmıştır"],
  "TMS 2: stokların net gerçekleşebilir değere indirgenmesi genellikle her bir stok kalemi bazında yapılır. Bazı durumlarda benzer veya ilişkili kalemlerin gruplandırılması uygun olabilir; ancak stokların tamamı tek bir sınıf olarak değerlendirilemez.",
  "TMS 2 - değerlendirme düzeyi")

q("Üretimde kullanılacak ilk madde ve malzemenin değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Mamullerin maliyetin üzerinde satılması bekleniyorsa ilk madde ve malzeme değer düşüklüğüne uğratılmaz",
  ["İlk madde ve malzeme her hâlde ve koşulsuz olarak değer düşüklüğüne uğratılmak zorunda tutulmuştur",
   "İlk madde ve malzemede hiçbir hâlde değer düşüklüğü değerlendirmesi yapılmamaktadır",
   "İlk madde ve malzemenin değer düşüklüğü yalnızca mamul kârlı satılıyorsa hesaplanmaktadır",
   "İlk madde ve malzeme yalnızca satış fiyatının yarısı kadar değer düşüklüğüne uğratılır"],
  "TMS 2: üretimde kullanılmak üzere elde tutulan ilk madde ve malzeme, kullanılacağı mamullerin maliyetin üzerinde satılması bekleniyorsa maliyetin altında bir değere indirgenmez. Mamullerin maliyetin altında satılması bekleniyorsa indirgeme yapılır.",
  "TMS 2 - ilk madde ve malzemede değer düşüklüğü")

q("Değer düşüklüğünün iptali bakımından aşağıdakilerden hangisi doğrudur?",
  "Koşullar değişip değer artarsa önceki indirgeme iptal edilir; iptal, orijinal maliyeti aşamaz",
  ["Değer düşüklüğü hiçbir hâlde iptal edilemez; bir kez indirgenen stok o değerle taşınmaya devam eder",
   "İptal tutarı sınırsızdır; stok değer artışı kadar orijinal maliyetin üzerine çıkarılabilmektedir",
   "İptal yalnızca stok satıldığında yapılabilir; elde tutulan stokta iptal söz konusu değildir",
   "Değer düşüklüğü iptali doğrudan özkaynaklara kaydedilir; kâr veya zarara hiç yansıtılmaz"],
  "TMS 2: stokların net gerçekleşebilir değere indirgenmesine yol açan koşullar ortadan kalkarsa veya ekonomik koşullar nedeniyle net gerçekleşebilir değerde artış olursa, indirgeme tutarı iptal edilir. İptal, yeni defter değerinin maliyet ile revize edilmiş net gerçekleşebilir değerden düşük olanına eşit olmasıyla sınırlıdır.",
  "TMS 2 - değer düşüklüğü iptali")

q("Stokların gider olarak muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Stoklar satıldığında defter değeri, ilgili hasılatın muhasebeleştirildiği dönemde gider olarak kaydedilir",
  ["Stokların defter değeri her hâlde alındığı dönemde doğrudan gider olarak muhasebeleştirilmektedir",
   "Stokların defter değeri satılsa dahi hiçbir zaman gider yazılmaz; sürekli stokta taşınmaktadır",
   "Stokların defter değeri satış hasılatına eklenerek dönem kârını artıran bir unsur olarak izlenir",
   "Stokların gider yazılması yalnızca vergi idaresinin izniyle ve onun belirlediği zamanda yapılır"],
  "TMS 2: stoklar satıldığında bunların defter değeri, ilgili hasılatın muhasebeleştirildiği dönemde gider olarak muhasebeleştirilir (hasılatla eşleştirme).",
  "TMS 2 - gider olarak muhasebeleştirme")

mal, ngd = 70_000, 62_000
q(f"Bir stokun maliyeti {tr(mal)} TL, net gerçekleşebilir değeri {tr(ngd)} TL'dir. TMS 2'ye göre stok hangi tutarla ölçülür ve değer düşüklüğü kaç TL'dir?",
  f"{tr(ngd)} TL ile ölçülür; {tr(mal-ngd)} TL değer düşüklüğü yazılır",
  [f"{tr(mal)} TL ile ölçülür; değer düşüklüğü yazılmaz",
   f"{tr(mal+ngd)} TL ile ölçülür; değer düşüklüğü yazılmaz",
   f"{tr(ngd)} TL ile ölçülür; {tr(mal)} TL değer düşüklüğü yazılır",
   f"{tr(mal)} TL ile ölçülür; {tr(mal-ngd)} TL değer artışı yazılır"],
  f"Stoklar maliyet ile net gerçekleşebilir değerden düşük olanıyla ölçülür. NGD ({tr(ngd)}) maliyetin ({tr(mal)}) altında olduğundan stok {tr(ngd)} TL'ye indirgenir ve aradaki {tr(mal-ngd)} TL gider olarak muhasebeleştirilir.",
  "TMS 2 - değer düşüklüğü")

m2, sf2, tam2, sat2 = 36_000, 40_000, 2_000, 3_000
ngd2 = sf2 - tam2 - sat2
q(f"Maliyeti {tr(m2)} TL olan stokun tahmini satış fiyatı {tr(sf2)} TL, tamamlanma maliyeti {tr(tam2)} TL ve satış maliyeti {tr(sat2)} TL'dir. TMS 2'ye göre doğru sonuç hangisidir?",
  f"Stok {tr(ngd2)} TL'ye indirgenir ve {tr(m2-ngd2)} TL gider yazılır",
  [f"Stok {tr(m2)} TL'de kalır; değer düşüklüğü yoktur",
   f"Stok {tr(sf2)} TL'ye yükseltilir ve {tr(sf2-m2)} TL kâr yazılır",
   f"Stok {tr(tam2)} TL'ye indirgenir ve {tr(m2-tam2)} TL gider yazılır",
   f"Stok {tr(sf2-sat2)} TL'ye indirgenir ve fark gider yazılır"],
  f"NGD = {tr(sf2)} − {tr(tam2)} − {tr(sat2)} = {tr(ngd2)} TL. Maliyet {tr(m2)} TL bunun üzerinde olduğundan stok {tr(ngd2)} TL'ye indirgenir ve {tr(m2-ngd2)} TL gider olarak muhasebeleştirilir.",
  "TMS 2 - NGD ve değer düşüklüğü")

m3, onceki_ngd, yeni_ngd = 90_000, 72_000, 85_000
q(f"Maliyeti {tr(m3)} TL olan stok önceki dönemde {tr(onceki_ngd)} TL'ye indirgenmiştir. Cari dönemde net gerçekleşebilir değer {tr(yeni_ngd)} TL'ye yükselmiştir. Yeni defter değeri kaç TL olur?",
  f"{tr(yeni_ngd)} TL",
  [f"{tr(m3)} TL", f"{tr(onceki_ngd)} TL", f"{tr(m3+yeni_ngd-onceki_ngd)} TL", f"{tr(yeni_ngd-onceki_ngd)} TL"],
  f"Önceki indirgeme iptal edilir; ancak iptal, defter değerinin maliyet ile revize NGD'den düşük olanını aşmasına izin vermez. min({tr(m3)}, {tr(yeni_ngd)}) = {tr(yeni_ngd)} TL yeni defter değeridir.",
  "TMS 2 - değer düşüklüğü iptali")

m4, yeni_ngd4 = 90_000, 95_000
q(f"Maliyeti {tr(m4)} TL olan ve önceki dönemde değer düşüklüğü ayrılan stokun net gerçekleşebilir değeri cari dönemde {tr(yeni_ngd4)} TL'ye yükselmiştir. Yeni defter değeri kaç TL olur?",
  f"{tr(m4)} TL",
  [f"{tr(yeni_ngd4)} TL", f"{tr(m4+yeni_ngd4)} TL", f"{tr(yeni_ngd4-m4)} TL", f"{tr(int(m4/2))} TL"],
  f"İptal, defter değerinin orijinal maliyeti aşmasına izin vermez. NGD ({tr(yeni_ngd4)}) maliyetin ({tr(m4)}) üzerinde olduğundan defter değeri maliyetle sınırlı kalır: {tr(m4)} TL.",
  "TMS 2 - iptalin maliyet sınırı")

q("Bir işletmenin ilk madde ve malzemesinin piyasa fiyatı düşmüş; ancak bu malzemeyle üretilecek mamullerin maliyetin üzerinde satılması beklenmektedir. TMS 2 bakımından aşağıdakilerden hangisi doğrudur?",
  "İlk madde ve malzeme değer düşüklüğüne uğratılmaz; maliyetle taşınmaya devam eder",
  ["İlk madde ve malzeme her hâlde düşen piyasa fiyatına indirgenmek zorunda tutulmaktadır",
   "İlk madde ve malzeme doğrudan gider yazılarak stoklardan tümüyle çıkarılmak zorundadır",
   "Mamullerin kârlı satılacak olması ilk madde ve malzemenin değerlemesini hiç etkilememektedir",
   "İlk madde ve malzeme her hâlde satış fiyatı üzerinden yeniden ölçülmek zorunda kalmaktadır"],
  "TMS 2: ilk madde ve malzemenin fiyatı düşse dahi, kullanılacağı mamullerin maliyetin üzerinde satılması bekleniyorsa ilk madde ve malzeme maliyetin altına indirgenmez.",
  "TMS 2 - ilk madde değer düşüklüğü (senaryo)")

q("Aşağıdaki ifadelerden hangileri değer düşüklüğü bakımından doğrudur?\n\nI. İndirgeme genellikle kalem bazında yapılır\n\nII. Koşullar değişirse indirgeme iptal edilebilir\n\nIII. İptal, stokun orijinal maliyetini aşabilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "İndirgeme kalem bazında yapılır (I) ve koşullar değişirse iptal edilebilir (II). Ancak iptal, defter değerinin orijinal maliyeti aşmasına izin vermez; bu nedenle III yanlıştır.",
  "TMS 2 - değer düşüklüğü")

q("Aşağıdakilerden hangileri TMS 2'ye göre dipnotlarda açıklanır?\n\nI. Stokların ölçümünde kullanılan muhasebe politikaları\n\nII. Stokların toplam defter değeri ve uygun sınıflandırmalara göre dağılımı\n\nIII. Dönem içinde gider olarak muhasebeleştirilen stok tutarı",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 2: dipnotlarda; ölçümde kullanılan muhasebe politikaları ve maliyet yöntemi (I), toplam defter değeri ve sınıflandırmalara göre dağılım (II), dönemde gider yazılan stok tutarı (III), değer düşüklüğü ve iptal tutarları açıklanır. Üçü de doğrudur.",
  "TMS 2 - dipnot açıklamaları")

q("Stok maliyetine alınmayan giderlerin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu giderler oluştukları dönemde gider olarak muhasebeleştirilir",
  ["Bu giderler gelecek dönemin stok maliyetine aktarılarak orada izlenmek zorunda tutulmaktadır",
   "Bu giderler doğrudan özkaynaklardan indirilir; kâr veya zarara hiçbir biçimde yansıtılmaz",
   "Bu giderler satış hasılatına eklenerek dönem kârını artıran bir unsur olarak kaydedilmektedir",
   "Bu giderler hiçbir yerde muhasebeleştirilmez; yalnızca dipnotlarda açıklanmak zorundadır"],
  "TMS 2 par. 16: stok maliyetine alınmayan giderler (normalin üstündeki fire, zorunlu olmayan depolama, genel yönetim, satış giderleri) gerçekleştikleri dönemde gider olarak muhasebeleştirilir.",
  "TMS 2 - maliyete alınmayanların kaydı")

q("Bir işletmenin stoklarının bir kısmı zarar görmüş ve satılabilir değeri düşmüştür. TMS 2 bakımından aşağıdakilerden hangisi doğrudur?",
  "Zarar gören stoklar net gerçekleşebilir değere indirgenir ve aradaki fark gider yazılır",
  ["Zarar gören stoklar her hâlde maliyet değeriyle taşınmaya devam eder; indirgeme yapılmaz",
   "Zarar gören stoklar doğrudan stoklardan çıkarılır ve hiçbir tutar finansal tablolara alınmaz",
   "Zarar gören stoklar orijinal satış fiyatı üzerinden değerlenerek stokta gösterilmek zorundadır",
   "Zarar gören stokların değerlemesi yalnızca sigorta şirketinin belirlediği tutara göre yapılır"],
  "TMS 2: stoklar zarar görmüş, kısmen ya da tamamen kullanılamaz hâle gelmişse maliyetleri geri kazanılamayabilir. Bu durumda stoklar net gerçekleşebilir değere indirgenir ve indirgeme gider olarak muhasebeleştirilir.",
  "TMS 2 - değer düşüklüğü (senaryo)")

q("Net gerçekleşebilir değer tahmininde dikkate alınacak bilgiler bakımından aşağıdakilerden hangisi doğrudur?",
  "Tahmin, tahmin tarihinde mevcut en güvenilir kanıtlara dayanır; dönem sonundan sonraki olaylar da dikkate alınır",
  ["Tahmin yalnızca stokun alındığı tarihteki fiyata dayanır; sonraki bilgiler hiç dikkate alınmaz",
   "Tahmin tümüyle yönetimin keyfi kanaatine bırakılmış olup hiçbir kanıt aranmamaktadır",
   "Tahminde yalnızca vergi idaresinin belirlediği değerler kullanılabilir; başka kanıt geçersizdir",
   "Net gerçekleşebilir değer tahmini yapılmaz; stoklar her hâlde maliyetle taşınmak zorundadır"],
  "TMS 2: net gerçekleşebilir değer tahminleri, stokların gerçekleşmesi beklenen tutarı hakkında tahmin tarihinde mevcut en güvenilir kanıtlara dayanır. Raporlama dönemi sonundan sonraki olayların, dönem sonundaki koşulları teyit ettiği ölçüde dikkate alınır.",
  "TMS 2 - NGD tahmini")

q("Sözleşmeye bağlanmış satışlarda net gerçekleşebilir değer bakımından aşağıdakilerden hangisi doğrudur?",
  "Kesin satış sözleşmesine bağlı stoklarda net gerçekleşebilir değer sözleşme fiyatına göre belirlenir",
  ["Sözleşmeye bağlı stoklarda da her hâlde genel piyasa fiyatı esas alınmak zorunda tutulmuştur",
   "Sözleşmeye bağlı stoklarda net gerçekleşebilir değer hiç hesaplanmaz; maliyet esas alınır",
   "Sözleşme fiyatı yalnızca piyasa fiyatından yüksekse dikkate alınır; düşükse göz ardı edilir",
   "Sözleşmeye bağlı satışlar TMS 2'de düzenlenmemiş olup uygulamada dikkate alınmamaktadır"],
  "TMS 2: elde tutulan stoklar kesin satış sözleşmelerine konu ise net gerçekleşebilir değer sözleşme fiyatına göre belirlenir. Sözleşme miktarı elde tutulan stoktan azsa, fazla kısmın NGD'si genel satış fiyatlarına göre belirlenir.",
  "TMS 2 - sözleşmeli satış")

q("Stokların ölçümünde her dönem yapılacak değerlendirme bakımından aşağıdakilerden hangisi doğrudur?",
  "Net gerçekleşebilir değer her raporlama döneminde yeniden değerlendirilir",
  ["Net gerçekleşebilir değer yalnızca stokun alındığı dönemde bir kez değerlendirilir; sonra bakılmaz",
   "Net gerçekleşebilir değer beş yılda bir değerlendirilir; ara dönemlerde hiç incelenmemektedir",
   "Değerlendirme yalnızca işletme zarar ettiğinde yapılır; kâr hâlinde hiç değerlendirme yapılmaz",
   "Değerlendirme sıklığı standartta düzenlenmemiş olup işletmenin serbest tercihine bırakılmıştır"],
  "TMS 2: net gerçekleşebilir değer, her raporlama döneminde yeniden değerlendirilir. Daha önce indirgemeye neden olan koşullar ortadan kalkmışsa veya değer artmışsa indirgeme iptal edilir.",
  "TMS 2 - dönemsel değerlendirme")

q("Hizmet sunan işletmelerin stok maliyetine dâhil edilmeyen unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Satış ve genel yönetim personelinin ücretleri hizmet stokunun maliyetine dâhil edilmez",
  ["Tüm personel ücretleri her hâlde hizmet stokunun maliyetine dâhil edilmek zorunda tutulmuştur",
   "Hizmeti sunan personelin ücretleri hizmet stokunun maliyetine hiçbir hâlde dâhil edilmez",
   "Hizmet işletmelerinde maliyet kavramı bulunmadığından böyle bir ayrım söz konusu değildir",
   "Hizmet stokunun maliyeti yalnızca faturalanan satış tutarı üzerinden hesaplanmaktadır"],
  "TMS 2: hizmet sunan işletmenin stok maliyeti, hizmeti sunan personel ile diğer doğrudan personelin ücretleri ve ilgili genel giderlerden oluşur. Satış ve genel yönetim personelinin ücretleri ise stok maliyetine alınmaz; gerçekleştikleri dönemde gider yazılır.",
  "TMS 2 - hizmet stok maliyeti")

d_sf, d_isk_orani_yok = 120_000, 10_000
q(f"Liste fiyatı {tr(d_sf)} TL olan ticari mal için {tr(d_isk_orani_yok)} TL ticari iskonto uygulanmıştır. İade alınamayan vergi ve başka gider yoksa satın alma maliyeti kaç TL'dir?",
  f"{tr(d_sf-d_isk_orani_yok)} TL",
  [f"{tr(d_sf+d_isk_orani_yok)} TL", f"{tr(d_sf)} TL", f"{tr(d_isk_orani_yok)} TL", f"{tr(d_sf-d_isk_orani_yok*2)} TL"],
  f"TMS 2: ticari iskontolar ve benzeri indirimler satın alma maliyetinin belirlenmesinde düşülür. Maliyet = {tr(d_sf)} − {tr(d_isk_orani_yok)} = {tr(d_sf-d_isk_orani_yok)} TL.",
  "TMS 2 - ticari iskonto")

q("Aşağıdaki ifadelerden hangileri TMS 2 bakımından doğrudur?\n\nI. Hizmet işletmelerinde de stok kavramı vardır\n\nII. NGD her raporlama döneminde yeniden değerlendirilir\n\nIII. LIFO yöntemi TMS 2'de kabul edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Hizmet işletmelerinde stok kavramı vardır (I) ve NGD her dönem yeniden değerlendirilir (II). LIFO ise TMS 2'de kabul edilmez; bu nedenle III yanlıştır.",
  "TMS 2 - genel")

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
        opts = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            opts[k] = d
        assert len(set(opts.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "ders": DERS, "konu": KONU,
            "stem": it["stem"], "options": opts, "answer": ans,
            "solution": it["why"] + f" Doğru cevap {ans}.",
            "source": {"kind": "generated",
                       "styleRef": "SGS Muhasebe Standartları (TMS 2; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} | harf {''.join(x['answer'] for x in out)[:40]}…")
