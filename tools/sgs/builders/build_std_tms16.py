# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 16 Maddi Duran Varlıklar — 60 soru.
Kaynak: KGK TMS 16. Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
NOT: yıla bağlı oran/tutar (KDV, amortisman oranı listesi) SORULMAZ; oranlar
soru kökünde verilir ya da yapısal kurallar sorulur."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_16_mdv"
PREFIX, SEED = "std-tms16-gen", 20260618
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_16_mdv.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanım ve muhasebeleştirme (12) ──────────────────────────────────────
q("TMS 16'ya göre maddi duran varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretimde, arzda, kiraya vermede veya idari amaçla kullanılmak üzere elde tutulan ve bir dönemden fazla kullanımı öngörülen fiziki kalemlerdir",
  ["İşletmenin bir yıl içinde paraya çevirmeyi planladığı ve satış amacıyla elde tuttuğu varlıklardır",
   "İşletmenin fiziki niteliği bulunmayan ve haklardan oluşan varlıklarını ifade eden bir kalemdir",
   "İşletmenin değer artışı veya kira geliri elde etmek amacıyla elde tuttuğu gayrimenkulleri kapsar",
   "Maddi duran varlık kavramı TMS 16'da tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 16: maddi duran varlıklar, mal veya hizmet üretimi ya da arzında kullanılmak, başkalarına kiraya verilmek veya idari amaçlarla kullanılmak üzere elde tutulan ve bir dönemden fazla kullanımı öngörülen fiziki kalemlerdir.",
  "TMS 16 - MDV tanımı")

q("Maddi duran varlığın muhasebeleştirilme ölçütleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki ekonomik yararların işletmeye akışının muhtemel olması ve maliyetin güvenilir ölçülebilmesi gerekir",
  ["Yalnızca varlığın fiziki olarak teslim alınmış olması yeterli olup başka bir koşul aranmamaktadır",
   "Yalnızca varlığın hukuken mülkiyetinin devralınmış olması yeterli olup başka koşul aranmaz",
   "Yalnızca varlığın bedelinin tamamının nakit olarak ödenmiş olması koşulu aranmak zorundadır",
   "Muhasebeleştirme ölçütü bulunmayıp işletme dilediği kalemi serbestçe aktifleştirebilmektedir"],
  "TMS 16: bir maddi duran varlık kalemi, (a) bu kalemle ilgili gelecekteki ekonomik yararların işletmeye akışının muhtemel olması ve (b) kalemin maliyetinin güvenilir biçimde ölçülebilmesi durumunda varlık olarak muhasebeleştirilir.",
  "TMS 16 - muhasebeleştirme ölçütleri")

q("Maddi duran varlığın ilk muhasebeleştirilmesindeki ölçüm bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet bedeliyle ölçülür",
  ["Gerçeğe uygun değeriyle ölçülür; maliyet bedeli hiçbir hâlde dikkate alınmamaktadır",
   "Net gerçekleşebilir değeriyle ölçülür; bu değer maliyetten her hâlde düşük olmaktadır",
   "Kullanım değeriyle ölçülür; bu değer işletmenin beklediği nakit akışlarına dayanmaktadır",
   "İlk ölçüm için belirlenmiş bir esas bulunmayıp işletme dilediği değeri kullanabilmektedir"],
  "TMS 16: varlık olarak muhasebeleştirilme koşullarını sağlayan bir maddi duran varlık kalemi, ilk muhasebeleştirilmesinde maliyet bedeli ile ölçülür.",
  "TMS 16 - ilk ölçüm")

q("Maddi duran varlığın maliyetine giren unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Satın alma fiyatı, varlığı yerine ve çalışır duruma getirmenin doğrudan maliyetleri ile sökme ve restorasyon yükümlülüğü maliyeti dâhildir",
  ["Yalnızca satın alma fiyatı maliyete dâhil edilir; diğer tüm harcamalar gider yazılmaktadır",
   "Yalnızca nakit olarak ödenen tutarlar maliyete dâhil edilir; diğerleri dikkate alınmamaktadır",
   "İşletmenin tüm genel yönetim giderleri de maliyete dâhil edilmek zorunda tutulmuş bulunmaktadır",
   "Maliyet unsurları TMS 16'da düzenlenmemiş olup işletmenin takdirine bırakılmış bir husustur"],
  "TMS 16: maliyet unsurları (a) indirimler düşüldükten sonra alış fiyatı ve iade edilmeyen alış vergileri, (b) varlığı yerine ve yönetimin amaçladığı biçimde çalışır duruma getirmeye ilişkin doğrudan ilişkilendirilebilir maliyetler ve (c) sökme, kaldırma ve restorasyon yükümlülüğünün tahmini maliyetidir.",
  "TMS 16 - maliyet unsurları")

q("Aşağıdakilerden hangisi maddi duran varlığın maliyetine doğrudan ilişkilendirilebilir maliyet olarak DÂHİL EDİLİR?",
  "Montaj ve kurulum maliyetleri",
  ["Yeni bir tesisin açılışına ilişkin olarak yapılan tanıtım ve organizasyon maliyetleri niteliğinde harcamalar",
   "Yeni bir ürünün tanıtılmasına ilişkin olarak katlanılan reklam ve promosyon maliyeti niteliğindeki tutarlar",
   "Yeni bir yerde yeni bir müşteri kitlesiyle iş yapmaya ilişkin personel eğitimi niteliğindeki maliyetler",
   "İşletmenin genel yönetim giderleri ile idari nitelikteki diğer genel gider niteliğindeki harcamalar"],
  "TMS 16: montaj ve kurulum maliyetleri, varlığı yönetimin amaçladığı biçimde çalışır duruma getirmeye ilişkin doğrudan ilişkilendirilebilir maliyettir. Açılış, tanıtım/reklam, yeni müşteri kitlesiyle iş yapma (eğitim dâhil) ve genel yönetim giderleri maliyete DÂHİL EDİLMEZ.",
  "TMS 16 - doğrudan maliyetler")

q("Aşağıdakilerden hangisi maddi duran varlığın maliyetine DÂHİL EDİLMEZ?",
  "Yeni ürünün tanıtımına ilişkin reklam maliyetleri",
  ["Varlığın çalışır duruma getirilmesi için katlanılan montaj ve kurulum niteliğindeki maliyet tutarları",
   "Varlığın işletmeye taşınmasına ilişkin olarak katlanılan nakliye ve sigorta niteliğindeki maliyetler",
   "Varlığın gerektiği gibi çalışıp çalışmadığının sınanmasına ilişkin test niteliğindeki maliyet tutarları",
   "Varlığın kurulumunda görev alan çalışanlara sağlanan faydalardan doğan maliyet niteliğindeki tutarlar"],
  "TMS 16: yeni bir ürün veya hizmetin tanıtılmasına ilişkin maliyetler (reklam ve promosyon faaliyetleri dâhil) maddi duran varlığın maliyetine dâhil edilmez; gider olarak muhasebeleştirilir.",
  "TMS 16 - maliyete girmeyen unsurlar")

q("Maliyete eklemenin durdurulması bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık yönetimin amaçladığı biçimde çalışabilmesi için gerekli yer ve duruma getirildiğinde maliyete ekleme durur",
  ["Varlık fiilen kullanılmaya başlandığında durur; kullanılmadıkça maliyete ekleme sürmektedir",
   "Varlığın bedelinin tamamı ödendiğinde durur; ödeme tamamlanmadıkça ekleme devam etmektedir",
   "Varlığın faydalı ömrü sona erdiğinde durur; o tarihe kadar tüm harcamalar maliyete eklenir",
   "Maliyete eklemenin durdurulması TMS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TMS 16: bir maddi duran varlık kaleminin defter değerine yapılan ilaveler, varlık yönetimin amaçladığı biçimde çalışabilmesi için gerekli duruma ve yere getirildiğinde durdurulur.",
  "TMS 16 - maliyete eklemenin durması")

q("Maddi duran varlığın vadeli olarak satın alınması bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet, peşin fiyat eşdeğeridir; aradaki fark aktifleştirilmedikçe faiz gideri olarak kaydedilir",
  ["Maliyet, ödenecek toplam vadeli tutardır; faiz unsuru her hâlde maliyete dâhil edilmektedir",
   "Maliyet, ödenen peşinat tutarıdır; kalan taksitler hiçbir biçimde dikkate alınmamaktadır",
   "Vadeli alınan varlıklar hiçbir hâlde aktifleştirilemez; doğrudan gider yazılmak zorundadır",
   "Vadeli alımda maliyetin nasıl belirleneceği TMS 16'da düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 16: bir maddi duran varlığın maliyeti, muhasebeleştirme tarihindeki peşin fiyat eşdeğeridir. Ödemenin normal kredi vadelerinin ötesine ertelenmesi hâlinde, peşin fiyat eşdeğeri ile toplam ödeme arasındaki fark, TMS 23 uyarınca aktifleştirilmediği sürece kredi vadesi boyunca faiz gideri olarak kaydedilir.",
  "TMS 16 - vadeli alım")

q("Maddi duran varlığın takas yoluyla edinilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlem ticari nitelik taşıyorsa ve gerçeğe uygun değer güvenilir ölçülebiliyorsa maliyet gerçeğe uygun değerdir",
  ["Takasla edinilen varlık her hâlde ve istisnasız verilen varlığın defter değeriyle ölçülmektedir",
   "Takasla edinilen varlık hiçbir hâlde aktifleştirilemez; doğrudan gider yazılmak zorunda tutulur",
   "Takasla edinilen varlık her hâlde sıfır değerle kaydedilir; takasta bedel ödenmemiş olmaktadır",
   "Takas işlemleri TMS 16 kapsamı dışında olup bu konuda hiçbir düzenleme bulunmamaktadır"],
  "TMS 16: takas yoluyla edinilen varlığın maliyeti gerçeğe uygun değerle ölçülür. Ancak takas işlemi ticari nitelikte değilse ya da alınan veya verilen varlığın gerçeğe uygun değeri güvenilir biçimde ölçülemiyorsa, maliyet verilen varlığın defter değeridir.",
  "TMS 16 - takas")

q("Sökme ve restorasyon yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın sökülmesi, kaldırılması ve yerin restorasyonuna ilişkin yükümlülüğün tahmini maliyeti varlığın maliyetine dâhil edilir",
  ["Sökme ve restorasyon maliyetleri hiçbir hâlde varlığın maliyetine dâhil edilememektedir",
   "Sökme ve restorasyon maliyetleri yalnızca fiilen ödendiği dönemde gider yazılmak zorundadır",
   "Sökme ve restorasyon maliyetleri yalnızca dipnotta açıklanır; hiçbir tutar kaydedilmemektedir",
   "Sökme yükümlülüğü yalnızca varlık satıldığında dikkate alınır; edinimde hiç hesaba katılmaz"],
  "TMS 16: maddi duran varlığın sökülmesi, taşınması veya yerleştirildiği alanın restorasyonuna ilişkin tahmini maliyeti, işletmenin o kalemi edindiğinde katlandığı yükümlülük ölçüsünde maliyete dâhil edilir.",
  "TMS 16 - sökme ve restorasyon")

q("Aşağıdakilerden hangileri TMS 16'ya göre maddi duran varlığın maliyetine DÂHİL EDİLİR?\n\nI. Nakliye ve taşıma maliyetleri\n\nII. Genel yönetim giderleri\n\nIII. Yeni tesisin açılış maliyetleri",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Nakliye ve taşıma maliyetleri (I), varlığı yerine ve çalışır duruma getirmenin doğrudan maliyetlerindendir. Genel yönetim giderleri (II) ile yeni tesisin açılış maliyetleri (III) maliyete dâhil edilmez. Yalnız I doğrudur.",
  "TMS 16 - maliyet unsurları")

q("Aşağıdakilerden hangileri TMS 16'ya göre maddi duran varlığın maliyetine DÂHİL EDİLMEZ?\n\nI. Yeni ürünün reklam ve promosyon maliyetleri\n\nII. Personelin yeni müşteri kitlesiyle iş yapmaya yönelik eğitim maliyetleri\n\nIII. Genel yönetim giderleri",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 16 üçünü de maliyete dâhil edilmeyen unsurlar arasında sayar: tanıtım/reklam maliyetleri (I), yeni yerde yeni müşteri kitlesiyle iş yapma maliyetleri (personel eğitimi dâhil) (II) ve yönetim ile diğer genel giderler (III).",
  "TMS 16 - maliyete girmeyen unsurlar")

# ── B. Maliyet hesabı ve sonraki harcamalar (10) ───────────────────────────
liste, isk, nak, mon, tst, egt, rek = 500_000, 50_000, 20_000, 30_000, 15_000, 10_000, 25_000
mal1 = liste - isk + nak + mon + tst
q(f"Bir işletme makineyi {tr(liste)} TL liste fiyatıyla almış, {tr(isk)} TL ticari iskonto elde etmiştir. Ayrıca {tr(nak)} TL nakliye, {tr(mon)} TL montaj, {tr(tst)} TL test, {tr(egt)} TL personel eğitimi ve {tr(rek)} TL yeni ürün reklamı harcaması yapılmıştır. Makinenin TMS 16'ya göre maliyeti kaç TL'dir?",
  f"{tr(mal1)} TL",
  [f"{tr(mal1 + egt + rek)} TL", f"{tr(mal1 + egt)} TL", f"{tr(liste + nak + mon + tst)} TL", f"{tr(liste - isk)} TL"],
  f"Maliyet = (Liste − İskonto) + Nakliye + Montaj + Test = ({tr(liste)} − {tr(isk)}) + {tr(nak)} + {tr(mon)} + {tr(tst)} = {tr(mal1)} TL. Personel eğitimi ({tr(egt)} TL) ve yeni ürün reklamı ({tr(rek)} TL) TMS 16 uyarınca maliyete dâhil edilmez; gider yazılır.",
  "TMS 16 - maliyet hesabı")

satin, sok = 800_000, 60_000
mal2 = satin + sok
q(f"Bir işletme {tr(satin)} TL'ye tesis satın almıştır. Sözleşme gereği kullanım sonunda tesisin sökülmesi ve alanın eski hâline getirilmesi yükümlülüğünün bugünkü değeri {tr(sok)} TL olarak tahmin edilmiştir. Tesisin TMS 16'ya göre maliyeti kaç TL'dir?",
  f"{tr(mal2)} TL",
  [f"{tr(satin)} TL", f"{tr(satin - sok)} TL", f"{tr(sok)} TL", f"{tr(satin + sok * 2)} TL"],
  f"TMS 16 uyarınca sökme, kaldırma ve restorasyon yükümlülüğünün tahmini maliyeti varlığın maliyetine dâhil edilir: {tr(satin)} + {tr(sok)} = {tr(mal2)} TL.",
  "TMS 16 - sökme maliyeti hesabı")

q("Maddi duran varlığa ilişkin sonraki harcamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Muhasebeleştirme ölçütlerini karşılayan harcamalar defter değerine eklenir; günlük bakım giderleri kâr veya zarara yazılır",
  ["Tüm sonraki harcamalar her hâlde varlığın defter değerine eklenmek zorunda tutulmaktadır",
   "Tüm sonraki harcamalar her hâlde doğrudan gider yazılır; hiçbiri aktifleştirilememektedir",
   "Sonraki harcamalar hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmakla yetinilir",
   "Sonraki harcamaların ele alınışı TMS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TMS 16: günlük bakım maliyetleri (işçilik, sarf malzemesi, küçük parça) oluştuğunda kâr veya zarara yansıtılır. Muhasebeleştirme ölçütlerini karşılayan sonraki harcamalar ise defter değerine eklenir.",
  "TMS 16 - sonraki harcamalar")

q("Bir işletme, makinesine düzenli günlük bakım yaptırmış ve bakım bedelini ödemiştir. TMS 16 bakımından aşağıdakilerden hangisi doğrudur?",
  "Günlük bakım maliyeti oluştuğunda kâr veya zarara yansıtılır",
  ["Günlük bakım maliyeti her hâlde makinenin maliyetine eklenerek aktifleştirilmek zorundadır",
   "Günlük bakım maliyeti gelecek dönemlere yayılarak itfa edilmek zorunda olan bir kalemdir",
   "Günlük bakım maliyeti hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmaktadır",
   "Günlük bakım maliyeti doğrudan özkaynaklardan indirilmek zorunda tutulan bir harcamadır"],
  "TMS 16: bir maddi duran varlığın günlük bakımına ilişkin maliyetler (genellikle işçilik ve sarf malzemeleri) defter değerinde muhasebeleştirilmez; oluştuklarında kâr veya zarara yansıtılır.",
  "TMS 16 - günlük bakım (senaryo)")

q("Düzenli aralıklarla yapılan büyük çaplı denetim (muayene) maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Ölçütler sağlanıyorsa defter değerine eklenir; önceki denetimin kalan defter değeri bilanço dışı bırakılır",
  ["Büyük çaplı denetim maliyetleri her hâlde doğrudan gider yazılmak zorunda tutulmaktadır",
   "Büyük çaplı denetim maliyetleri hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanır",
   "Büyük çaplı denetim maliyetleri her hâlde özkaynaklardan indirilmek zorunda bulunmaktadır",
   "Büyük çaplı denetim maliyetlerinin ele alınışı TMS 16'da hiçbir biçimde düzenlenmemiştir"],
  "TMS 16: varlığın devamlı çalışması için düzenli aralıklarla yapılan büyük çaplı denetimlerin maliyeti, muhasebeleştirme ölçütlerinin sağlanması hâlinde defter değerine eklenir. Önceki denetime ilişkin kalan defter değeri finansal durum tablosu dışı bırakılır.",
  "TMS 16 - büyük çaplı denetim")

q("Belirli aralıklarla yenilenmesi gereken parçalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeni parçanın maliyeti ölçütleri sağlıyorsa defter değerine eklenir; değiştirilen parçanın defter değeri bilanço dışı bırakılır",
  ["Yeni parçanın maliyeti her hâlde doğrudan gider yazılır; aktifleştirilmesi mümkün olmamaktadır",
   "Yeni parça eklenirken eski parçanın defter değeri hiçbir hâlde bilanço dışı bırakılmamaktadır",
   "Parça değişimleri hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Parça değişimi her hâlde önceki dönem hatası olarak geriye dönük düzeltilmek zorunda kalınır"],
  "TMS 16: bazı parçaların belirli aralıklarla yenilenmesi gerekebilir. Yeni parçanın maliyeti, muhasebeleştirme ölçütlerini karşılıyorsa varlığın defter değerine eklenir; değiştirilen parçanın defter değeri finansal durum tablosu dışı bırakılır.",
  "TMS 16 - parça değişimi")

q("Maddi duran varlığın parçalara ayrılarak amortismana tabi tutulması bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyeti toplam maliyete göre önemli olan her parça ayrı ayrı amortismana tabi tutulur",
  ["Varlık her hâlde tek bir bütün olarak amortismana tabi tutulur; parçalara ayrılamamaktadır",
   "Yalnızca en ucuz parça ayrı amortismana tabi tutulur; diğerleri bütün hâlinde ele alınmaktadır",
   "Parçalara ayırma yalnızca vergi idaresi talep ettiğinde ve onun belirlediği biçimde yapılır",
   "Parçalara ayırma TMS 16'da düzenlenmemiş olup uygulamada hiç yapılmayan bir işlemdir"],
  "TMS 16: bir maddi duran varlık kaleminin toplam maliyetine göre önemli maliyet teşkil eden her bir parçası ayrı ayrı amortismana tabi tutulur (uçağın gövdesi ve motorları gibi).",
  "TMS 16 - parça bazlı amortisman")

q("Yedek parça ve donanım malzemeleri bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 16'daki tanımı karşılıyorlarsa maddi duran varlık, karşılamıyorlarsa stok olarak muhasebeleştirilirler",
  ["Yedek parçalar her hâlde ve istisnasız stok olarak muhasebeleştirilmek zorunda tutulmaktadır",
   "Yedek parçalar her hâlde maddi duran varlık olarak muhasebeleştirilmek zorunda bulunmaktadır",
   "Yedek parçalar hiçbir biçimde aktifleştirilemez; her hâlde doğrudan gider yazılmaktadır",
   "Yedek parçaların sınıflandırılması TMS 16'da düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 16: yedek parçalar ve donanım malzemeleri, maddi duran varlık tanımını karşılamaları durumunda TMS 16 uyarınca muhasebeleştirilir; aksi hâlde stok olarak sınıflandırılır.",
  "TMS 16 - yedek parçalar")

q("Emniyet veya çevre ile ilgili nedenlerle edinilen maddi duran varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Doğrudan ekonomik yarar sağlamasalar da diğer varlıklardan yarar elde edilmesi için gerekli olduklarından aktifleştirilirler",
  ["Doğrudan ekonomik yarar sağlamadıklarından her hâlde gider yazılmak zorunda tutulmuşlardır",
   "Bu varlıklar hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Bu varlıklar her hâlde özkaynaklardan indirilmek zorunda olan bir harcama niteliğindedir",
   "Bu varlıkların ele alınışı TMS 16'da düzenlenmemiş olup uygulamada dikkate alınmamaktadır"],
  "TMS 16: emniyet veya çevre ile ilgili nedenlerle edinilen maddi duran varlıklar doğrudan gelecekteki ekonomik yararı artırmasa da, işletmenin diğer varlıklarından gelecekte ekonomik yarar elde etmesi için gerekli olabilir; bu durumda varlık olarak muhasebeleştirilir.",
  "TMS 16 - emniyet ve çevre varlıkları")

q("Aşağıdaki ifadelerden hangileri TMS 16 bakımından doğrudur?\n\nI. Günlük bakım maliyetleri kâr veya zarara yansıtılır\n\nII. Değiştirilen parçanın defter değeri bilanço dışı bırakılır\n\nIII. Büyük çaplı denetim maliyetleri her hâlde doğrudan gider yazılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Günlük bakım gider yazılır (I) ve değiştirilen parçanın defter değeri bilanço dışı bırakılır (II). Büyük çaplı denetim maliyetleri ise muhasebeleştirme ölçütleri sağlanıyorsa defter değerine EKLENİR; her hâlde gider yazılmaz. Bu nedenle III yanlıştır.",
  "TMS 16 - sonraki harcamalar")

# ── C. Amortisman (18) ─────────────────────────────────────────────────────
q("TMS 16'ya göre amortisman bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir varlığın amortismana tabi tutarının faydalı ömrü boyunca sistematik olarak dağıtılmasıdır",
  ["Bir varlığın piyasa değerindeki azalışın ölçülerek kayda alınmasını ifade eden bir işlemdir",
   "Bir varlığın satılması hâlinde elde edilecek tutarın önceden hesaplanmasını ifade etmektedir",
   "Bir varlık için ayrılan ve gelecekte yenileme amacıyla kullanılacak nakit fonu ifade eder",
   "Amortisman kavramı TMS 16'da tanımlanmamış olup yalnızca vergi mevzuatında yer almaktadır"],
  "TMS 16: amortisman, bir varlığın amortismana tabi tutarının, faydalı ömrü boyunca sistematik olarak dağıtılmasıdır. Değer azalışının ölçülmesi değil, maliyetin dönemlere dağıtılmasıdır.",
  "TMS 16 - amortisman tanımı")

q("Amortismana tabi tutar bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın maliyetinden kalıntı değerinin düşülmesiyle bulunan tutardır",
  ["Varlığın maliyetinin tamamıdır; kalıntı değer hiçbir hâlde dikkate alınmamaktadır",
   "Varlığın gerçeğe uygun değerinden satış maliyetlerinin düşülmesiyle bulunan tutarı ifade eder",
   "Varlığın net defter değerine birikmiş amortismanın eklenmesiyle bulunan tutarı ifade etmektedir",
   "Amortismana tabi tutar kavramı TMS 16'da tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 16: amortismana tabi tutar, bir varlığın maliyetinden veya maliyet yerine geçen diğer tutardan kalıntı değerin düşülmesiyle bulunan tutardır.",
  "TMS 16 - amortismana tabi tutar")

q("Amortismana başlanacak tarih bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık kullanıma hazır olduğunda, yani yönetimin amaçladığı biçimde çalışabileceği yer ve duruma getirildiğinde başlar",
  ["Varlığın bedelinin tamamı ödendiğinde başlar; ödeme tamamlanmadıkça amortisman ayrılmamaktadır",
   "Varlık fiilen üretimde kullanılmaya başlandığında başlar; hazır olması yeterli sayılmamaktadır",
   "Varlığın hukuken mülkiyeti devralındığında başlar; fiziki teslim hiç dikkate alınmamaktadır",
   "Amortismana başlama tarihi TMS 16'da düzenlenmemiş olup işletmenin takdirine bırakılmıştır"],
  "TMS 16: bir varlığın amortismanı, varlık kullanılabilir olduğunda, yani yönetimin amaçladığı biçimde çalışabilmesi için gereken yer ve duruma getirildiğinde başlar.",
  "TMS 16 - amortismana başlama")

q("Boş duran ve kullanılmayan bir maddi duran varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık tümüyle itfa edilmedikçe veya satış amaçlı elde tutulan olarak sınıflandırılmadıkça amortisman durmaz",
  ["Varlık kullanılmadığı sürece amortisman ayrılması her hâlde durdurulmak zorunda tutulmaktadır",
   "Varlık boş durduğunda amortisman iki katına çıkarılarak hesaplanmak zorunda bulunmaktadır",
   "Boş duran varlıklar bilanço dışı bırakılmak zorunda olup amortisman söz konusu olmamaktadır",
   "Boş duran varlıkların amortismanı TMS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TMS 16: varlık kullanılmadığında veya elden çıkarılana kadar atıl tutulduğunda amortisman ayrılması durmaz. Amortisman ancak varlık tümüyle itfa edildiğinde ya da satış amaçlı elde tutulan olarak sınıflandırıldığında (veya bilanço dışı bırakıldığında) durur.",
  "TMS 16 - amortismanın durmaması")

q("Amortisman yöntemleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Doğrusal, azalan bakiyeler ve üretim miktarı yöntemleri kullanılabilir",
  ["Yalnızca doğrusal amortisman yöntemi kullanılabilir; diğer yöntemler kabul edilmemektedir",
   "Yalnızca azalan bakiyeler yöntemi kullanılabilir; doğrusal yöntem kesin olarak yasaklanmıştır",
   "Amortisman yöntemi her hâlde vergi mevzuatına göre seçilir; TMS 16'nın hükmü bulunmamaktadır",
   "Amortisman yöntemleri TMS 16'da düzenlenmemiş olup işletme her dönem yöntem değiştirmek zorundadır"],
  "TMS 16: varlığın amortismana tabi tutarının faydalı ömrü boyunca dağıtılmasında çeşitli yöntemler kullanılabilir: doğrusal amortisman, azalan bakiyeler ve üretim miktarı yöntemleri.",
  "TMS 16 - amortisman yöntemleri")

q("Hasılata dayalı amortisman yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın kullanımını içeren bir faaliyetten elde edilen hasılata dayalı yöntem uygun değildir",
  ["Hasılata dayalı yöntem her hâlde ve tercihen kullanılması gereken bir yöntemi ifade etmektedir",
   "Hasılata dayalı yöntem yalnızca büyük işletmelerce kullanılabilen bir yöntemi ifade eder",
   "Hasılata dayalı yöntem TMS 16'da doğrusal yöntemle eşdeğer kabul edilen bir yöntem niteliğindedir",
   "Hasılata dayalı yöntem TMS 16'da hiçbir biçimde ele alınmamış olup serbest bırakılmıştır"],
  "TMS 16: bir varlığın kullanımını içeren bir faaliyetten elde edilen hasılata dayalı amortisman yöntemi uygun değildir. Hasılat, varlığın ekonomik yararlarının tüketimi dışındaki etkenleri (fiyat değişimi, satış hacmi) de yansıtır.",
  "TMS 16 - hasılata dayalı yöntem")

q("Amortisman yönteminin gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "En az her hesap dönemi sonunda gözden geçirilir; beklenen tüketim biçimi değişmişse yöntem değiştirilir",
  ["Amortisman yöntemi bir kez seçildikten sonra hiçbir hâlde değiştirilememektedir",
   "Amortisman yöntemi her hesap döneminde zorunlu olarak değiştirilmek zorunda tutulmaktadır",
   "Amortisman yöntemi yalnızca vergi idaresi talep ettiğinde gözden geçirilmek zorundadır",
   "Amortisman yönteminin gözden geçirilmesi TMS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TMS 16: varlığa uygulanan amortisman yöntemi en azından her hesap dönemi sonunda gözden geçirilir. Beklenen tüketim biçiminde önemli bir değişiklik olmuşsa yöntem değiştirilir ve bu değişiklik muhasebe tahmini değişikliği olarak ele alınır.",
  "TMS 16 - yöntemin gözden geçirilmesi")

q("Faydalı ömür ve kalıntı değerin gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "En az her hesap dönemi sonunda gözden geçirilir; değişiklik tahmin değişikliği olarak ele alınır",
  ["Faydalı ömür ve kalıntı değer bir kez belirlendikten sonra hiçbir hâlde değiştirilememektedir",
   "Faydalı ömür ve kalıntı değer değişikliği muhasebe politikası değişikliği olarak ele alınmaktadır",
   "Faydalı ömür ve kalıntı değer değişikliği önceki dönem hatası sayılıp geriye dönük düzeltilir",
   "Faydalı ömür ve kalıntı değerin gözden geçirilmesi TMS 16'da düzenlenmemiş bir husustur"],
  "TMS 16: bir varlığın kalıntı değeri ve faydalı ömrü en az her hesap dönemi sonunda gözden geçirilir. Beklentilerin önceki tahminlerden farklı olması hâlinde değişiklik, TMS 8 uyarınca muhasebe tahminindeki değişiklik olarak muhasebeleştirilir.",
  "TMS 16 - faydalı ömür ve kalıntı değer")

q("Kalıntı değerin amortismanla ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kalıntı değer varlığın defter değerine eşit veya ondan büyükse amortisman gideri sıfır olur",
  ["Kalıntı değer ne olursa olsun amortisman her hâlde ayrılmaya devam edilmek zorundadır",
   "Kalıntı değer arttıkça amortisman gideri de artar; ikisi doğru orantılı biçimde hareket eder",
   "Kalıntı değer amortisman hesabında hiçbir biçimde dikkate alınmayan bir unsuru ifade eder",
   "Kalıntı değerin amortismanla ilişkisi TMS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TMS 16: bir varlığın kalıntı değeri, varlığın defter değerine eşit veya daha fazla bir tutara yükselirse, varlığın amortisman gideri, kalıntı değeri sonradan varlığın defter değerinin altına düşene kadar sıfıra eşit olur.",
  "TMS 16 - kalıntı değer ve amortisman")

q("Arazi ve binaların amortismanı bakımından aşağıdakilerden hangisi doğrudur?",
  "Arazi sınırsız ömürlü olduğundan kural olarak amortismana tabi değildir; binalar ise amortismana tabidir",
  ["Arazi ve binaların ikisi de amortismana tabi olup aynı faydalı ömür üzerinden itfa edilmektedir",
   "Arazi ve binaların ikisi de amortismana tabi olmayıp hiçbir hâlde itfa edilmemektedirler",
   "Arazi amortismana tabidir; binalar ise sınırsız ömürlü sayıldığından amortismana tabi değildir",
   "Arazi ve binaların amortismanı TMS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TMS 16: arazi ve binalar birlikte alınsa dahi ayrılabilir varlıklardır ve ayrı muhasebeleştirilir. Arazi sınırsız ömre sahip olduğundan amortismana tabi tutulmaz (taş ocağı gibi istisnalar hariç); binaların ise sınırlı ömrü olduğundan amortismana tabidir.",
  "TMS 16 - arazi ve bina")

m3, kal3, om3 = 620_000, 20_000, 8
a3 = (m3 - kal3) / om3
q(f"Maliyeti {tr(m3)} TL, kalıntı değeri {tr(kal3)} TL ve faydalı ömrü {om3} yıl olan bir makine doğrusal yöntemle amortismana tabidir. Yıllık amortisman gideri kaç TL'dir?",
  f"{tr(a3)} TL",
  [f"{tr(m3 / om3)} TL", f"{tr((m3 + kal3) / om3)} TL", f"{tr(m3 - kal3)} TL", f"{tr(kal3 / om3)} TL"],
  f"Doğrusal yöntemde yıllık amortisman = Amortismana tabi tutar ÷ Faydalı ömür. Amortismana tabi tutar = Maliyet − Kalıntı değer = {tr(m3)} − {tr(kal3)} = {tr(m3 - kal3)} TL. Yıllık amortisman = {tr(m3 - kal3)} ÷ {om3} = {tr(a3)} TL.",
  "TMS 16 - doğrusal amortisman")

m4, kal4, top_uretim, don_uretim = 900_000, 100_000, 400_000, 60_000
birim = (m4 - kal4) / top_uretim
a4 = birim * don_uretim
pay = don_uretim / top_uretim
q(f"Maliyeti {tr(m4)} TL, kalıntı değeri {tr(kal4)} TL olan bir makinenin toplam üretim kapasitesi {tr(top_uretim)} birim olarak tahmin edilmiştir. Dönemde {tr(don_uretim)} birim üretilmişse üretim miktarı yöntemine göre dönemin amortisman gideri kaç TL'dir?",
  f"{tr(a4)} TL",
  [f"{tr(m4 * pay)} TL",                      # kalıntı değer düşülmedi
   f"{tr((m4 + kal4) * pay)} TL",             # kalıntı değer düşülecekken eklendi
   f"{tr((m4 - 2 * kal4) * pay)} TL",         # kalıntı değer iki kez düşüldü
   f"{tr(m4 - kal4)} TL"],                    # amortismana tabi tutarın tamamı
  f"Üretim miktarı yönteminde birim başına amortisman = Amortismana tabi tutar ÷ Toplam tahmini üretim = ({tr(m4)} − {tr(kal4)}) ÷ {tr(top_uretim)} = {tr(birim)} TL/birim. Dönem amortismanı = {tr(birim)} × {tr(don_uretim)} = {tr(a4)} TL.",
  "TMS 16 - üretim miktarı yöntemi")

m5, oran = 500_000, 40
a5_1 = m5 * oran / 100
a5_2 = (m5 - a5_1) * oran / 100
q(f"Maliyeti {tr(m5)} TL olan bir makine, azalan bakiyeler yöntemiyle %{oran} oranında amortismana tabi tutulmaktadır. Kalıntı değer dikkate alınmadığında ikinci yılın amortisman gideri kaç TL'dir?",
  f"{tr(a5_2)} TL",
  [f"{tr(a5_1)} TL", f"{tr(m5 * oran / 100 * 2)} TL", f"{tr(m5 / 2 * oran / 100)} TL", f"{tr(m5 - a5_1)} TL"],
  f"Azalan bakiyeler yönteminde oran, her yıl kalan net defter değerine uygulanır. 1. yıl = {tr(m5)} × %{oran} = {tr(a5_1)} TL. Kalan net defter değeri = {tr(m5)} − {tr(a5_1)} = {tr(m5 - a5_1)} TL. 2. yıl = {tr(m5 - a5_1)} × %{oran} = {tr(a5_2)} TL.",
  "TMS 16 - azalan bakiyeler yöntemi")

q("Amortisman giderinin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Başka bir varlığın defter değerine dâhil edilmediği sürece kâr veya zarara yansıtılır",
  ["Amortisman gideri her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulmaktadır",
   "Amortisman gideri her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda bulunur",
   "Amortisman gideri hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmakla yetinilir",
   "Amortisman giderinin nereye yansıtılacağı TMS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TMS 16: her döneme ilişkin amortisman gideri, başka bir varlığın defter değerine dâhil edilmediği sürece kâr veya zararda muhasebeleştirilir. Örneğin üretimde kullanılan makinenin amortismanı stok maliyetine dâhil edilir.",
  "TMS 16 - amortismanın muhasebeleştirilmesi")

q("Bir işletme, üretimde kullandığı makinenin amortismanını hesaplamıştır. TMS 16 bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretimde kullanılan makinenin amortismanı stokların maliyetine dâhil edilir",
  ["Üretimde kullanılan makinenin amortismanı her hâlde doğrudan dönem gideri yazılmak zorundadır",
   "Üretimde kullanılan makinenin amortismanı doğrudan özkaynaklardan indirilmek zorunda kalınır",
   "Üretimde kullanılan makine için hiçbir hâlde amortisman ayrılmaz; üretim varlığı istisnadır",
   "Üretimde kullanılan makinenin amortismanı yalnızca dipnotta açıklanan bir husus niteliğindedir"],
  "TMS 16: amortisman gideri, başka bir varlığın defter değerine dâhil edilmediği sürece kâr veya zararda muhasebeleştirilir. Üretimde kullanılan maddi duran varlığın amortismanı, TMS 2 uyarınca stokların maliyetine dâhil edilir.",
  "TMS 16 - amortismanın stok maliyetine dâhili (senaryo)")

q("Aşağıdakilerden hangileri TMS 16'ya göre amortisman yöntemi olarak kullanılabilir?\n\nI. Doğrusal amortisman yöntemi\n\nII. Azalan bakiyeler yöntemi\n\nIII. Üretim miktarı yöntemi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 16 üç yöntemi de sayar: doğrusal amortisman (I), azalan bakiyeler (II) ve üretim miktarı (III). Yalnızca hasılata dayalı yöntem uygun değildir.",
  "TMS 16 - amortisman yöntemleri")

q("Aşağıdaki ifadelerden hangileri TMS 16 bakımından doğrudur?\n\nI. Amortisman varlık kullanıma hazır olduğunda başlar\n\nII. Varlık boş durduğunda amortisman ayrılması durur\n\nIII. Hasılata dayalı amortisman yöntemi uygun değildir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Amortisman varlık kullanılabilir olduğunda başlar (I) ve hasılata dayalı yöntem uygun değildir (III). Varlığın boş durması ise amortismanı DURDURMAZ; amortisman ancak varlık tümüyle itfa edildiğinde veya satış amaçlı sınıflandırıldığında durur. Bu nedenle II yanlıştır.",
  "TMS 16 - amortisman")

q("Aşağıdaki ifadelerden hangileri TMS 16 bakımından doğrudur?\n\nI. Faydalı ömür en az her dönem sonunda gözden geçirilir\n\nII. Kalıntı değer bir kez belirlendikten sonra değiştirilemez\n\nIII. Arazi kural olarak amortismana tabi değildir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Faydalı ömür en az her hesap dönemi sonunda gözden geçirilir (I) ve arazi sınırsız ömürlü olduğundan kural olarak amortismana tabi değildir (III). Kalıntı değer de tıpkı faydalı ömür gibi en az her dönem sonunda gözden geçirilir ve değişebilir; bu nedenle II yanlıştır.",
  "TMS 16 - amortisman")

# ── D. Sonraki ölçüm, yeniden değerleme, bilanço dışı bırakma (20) ─────────
q("Maddi duran varlığın sonraki ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme maliyet modelini veya yeniden değerleme modelini muhasebe politikası olarak seçer",
  ["Yalnızca maliyet modeli kullanılabilir; yeniden değerleme modeli kabul edilmemiş bulunmaktadır",
   "Yalnızca yeniden değerleme modeli kullanılabilir; maliyet modeli kesin olarak yasaklanmıştır",
   "İki model de aynı anda ve birlikte kullanılmak zorunda olup tek model yeterli görülmemektedir",
   "Sonraki ölçüm esası TMS 16'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmıştır"],
  "TMS 16: işletme muhasebe politikası olarak maliyet modelini veya yeniden değerleme modelini seçer ve bu politikayı ilgili maddi duran varlık sınıfının tamamına uygular.",
  "TMS 16 - sonraki ölçüm modelleri")

q("Seçilen ölçüm modelinin uygulanma kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Seçilen model, ilgili maddi duran varlık sınıfının tamamına uygulanır",
  ["Seçilen model yalnızca işletmenin seçtiği tek bir varlığa uygulanır; sınıfın geneli etkilenmez",
   "Seçilen model işletmedeki tüm varlık sınıflarına aynı anda uygulanmak zorunda tutulmaktadır",
   "Seçilen model her varlık için ayrı ayrı ve serbestçe belirlenebilen bir tercihi ifade eder",
   "Modelin kapsamı TMS 16'da düzenlenmemiş olup işletmenin takdirine bırakılmış bulunmaktadır"],
  "TMS 16: işletme seçtiği muhasebe politikasını (maliyet modeli veya yeniden değerleme modeli) ilgili maddi duran varlık sınıfının tamamına uygular. Aynı sınıftaki varlıkların seçmeli olarak yeniden değerlenmesi önlenmiş olur.",
  "TMS 16 - sınıf bazında uygulama")

q("Maliyet modeli bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık, maliyetinden birikmiş amortisman ve birikmiş değer düşüklüğü zararları indirilerek gösterilir",
  ["Varlık her hâlde gerçeğe uygun değeriyle gösterilir; birikmiş amortisman dikkate alınmamaktadır",
   "Varlık her hâlde ilk maliyetiyle gösterilir; birikmiş amortisman hiçbir hâlde indirilmemektedir",
   "Varlık net gerçekleşebilir değeriyle gösterilir; maliyet bilgisi hiç dikkate alınmamaktadır",
   "Maliyet modeli TMS 16'da tanımlanmamış olup uygulamada kullanılmayan bir modeli ifade eder"],
  "TMS 16: maliyet modelinde bir maddi duran varlık kalemi, varlık olarak muhasebeleştirildikten sonra maliyetinden birikmiş amortisman ve birikmiş değer düşüklüğü zararları indirildikten sonraki değeriyle gösterilir.",
  "TMS 16 - maliyet modeli")

q("Yeniden değerleme modeli bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değeri güvenilir ölçülebilen varlık, yeniden değerlenmiş tutarıyla gösterilir",
  ["Gerçeğe uygun değer ölçülemese dahi varlık her hâlde yeniden değerlenmek zorunda tutulmuştur",
   "Yeniden değerleme modeli yalnızca değeri düşen varlıklara uygulanabilen bir modeli ifade eder",
   "Yeniden değerleme modelinde varlık her hâlde ilk maliyetiyle gösterilmek zorunda kalınmaktadır",
   "Yeniden değerleme modeli TMS 16'da düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "TMS 16: gerçeğe uygun değeri güvenilir olarak ölçülebilen bir maddi duran varlık kalemi, yeniden değerlenmiş tutarı üzerinden gösterilir. Bu tutar, yeniden değerleme tarihindeki gerçeğe uygun değerinden sonraki birikmiş amortisman ve birikmiş değer düşüklüğü zararlarının indirilmesi suretiyle bulunur.",
  "TMS 16 - yeniden değerleme modeli")

q("Yeniden değerlemenin sıklığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Defter değeri gerçeğe uygun değerden önemli ölçüde farklılaşmayacak biçimde düzenli aralıklarla yapılır",
  ["Yeniden değerleme her hâlde ve istisnasız her ay yapılmak zorunda tutulan bir işlemdir",
   "Yeniden değerleme yalnızca bir kez yapılır; sonrasında hiçbir hâlde tekrarlanmamaktadır",
   "Yeniden değerleme yalnızca vergi idaresi talep ettiğinde ve onun belirlediği sıklıkta yapılır",
   "Yeniden değerlemenin sıklığı TMS 16'da düzenlenmemiş olup tümüyle serbest bırakılmıştır"],
  "TMS 16: yeniden değerlemeler, defter değerinin raporlama dönemi sonundaki gerçeğe uygun değerden önemli ölçüde farklı olmamasını sağlayacak düzenli aralıklarla yapılmalıdır. Sıklık, gerçeğe uygun değerdeki değişkenliğe bağlıdır.",
  "TMS 16 - yeniden değerleme sıklığı")

q("Yeniden değerleme sonucu defter değerinin ARTMASI bakımından aşağıdakilerden hangisi doğrudur?",
  "Artış diğer kapsamlı gelirde muhasebeleştirilir ve özkaynakta değer artışı olarak birikir",
  ["Artış her hâlde ve istisnasız doğrudan dönem kâr veya zararına yansıtılmak zorunda tutulur",
   "Artış hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Artış her hâlde ertelenmiş gelir olarak yabancı kaynaklarda gösterilmek zorunda bulunmaktadır",
   "Artış varlığın maliyetinden indirilerek net biçimde gösterilmek zorunda olan bir kalemdir"],
  "TMS 16: bir maddi duran varlığın defter değeri yeniden değerleme sonucunda artmışsa, bu artış diğer kapsamlı gelirde muhasebeleştirilir ve özkaynakta yeniden değerleme değer artışı adı altında toplanır.",
  "TMS 16 - yeniden değerleme artışı")

q("Daha önce kâr veya zarara yazılmış bir azalışı tersine çeviren yeniden değerleme artışı bakımından aşağıdakilerden hangisi doğrudur?",
  "Artış, daha önce kâr veya zarara yazılan azalışı tersine çevirdiği ölçüde kâr veya zarara yansıtılır",
  ["Artış her hâlde ve istisnasız tamamıyla diğer kapsamlı gelirde muhasebeleştirilmek zorundadır",
   "Artış her hâlde tamamıyla özkaynakta değer artışı olarak toplanmak zorunda tutulmaktadır",
   "Artış hiçbir biçimde kayda alınmaz; daha önce yazılan azalış geri alınamayan bir kalemdir",
   "Bu durumda artışın nereye yansıtılacağı TMS 16'da düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 16: yeniden değerleme artışı, aynı varlığın daha önce kâr veya zarar ile ilişkilendirilmiş bulunan yeniden değerleme azalışını tersine çevirdiği ölçüde kâr veya zararda muhasebeleştirilir.",
  "TMS 16 - artışın kâr/zarara yansıması")

q("Yeniden değerleme sonucu defter değerinin AZALMASI bakımından aşağıdakilerden hangisi doğrudur?",
  "Azalış kâr veya zarara yansıtılır; ancak o varlığa ilişkin değer artışı varsa o ölçüde diğer kapsamlı gelirde azaltılır",
  ["Azalış her hâlde ve istisnasız tamamıyla diğer kapsamlı gelirde muhasebeleştirilmek zorundadır",
   "Azalış hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Azalış her hâlde tamamıyla dönem kâr veya zararına yazılır; özkaynak hiçbir hâlde etkilenmez",
   "Azalış varlığın maliyetine eklenerek aktifleştirilmek zorunda olan bir kalemi ifade etmektedir"],
  "TMS 16: yeniden değerleme sonucu defter değeri azalmışsa azalış kâr veya zararda muhasebeleştirilir. Ancak azalış, o varlıkla ilgili yeniden değerleme değer artışındaki her tür alacak bakiyesi ölçüsünde diğer kapsamlı gelirde muhasebeleştirilir.",
  "TMS 16 - yeniden değerleme azalışı")

ndd5, gud5 = 300_000, 380_000
art5 = gud5 - ndd5
q(f"Bir binanın yeniden değerleme öncesi net defter değeri {tr(ndd5)} TL, yeniden değerleme tarihindeki gerçeğe uygun değeri {tr(gud5)} TL'dir. Binaya ilişkin daha önce kâr veya zarara yazılmış bir azalış bulunmamaktadır. Bu yeniden değerlemenin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  f"{tr(art5)} TL diğer kapsamlı gelirde muhasebeleştirilir",
  [f"{tr(art5)} TL doğrudan dönem kâr veya zararına gelir olarak yazılmak zorunda bulunmaktadır",
   f"{tr(gud5)} TL diğer kapsamlı gelirde muhasebeleştirilir; artış tutarı değil yeni değer kaydedilir",
   f"{tr(art5)} TL ertelenmiş gelir olarak yabancı kaynaklarda gösterilmek zorunda tutulmaktadır",
   "Hiçbir kayıt yapılmaz; yeniden değerleme farkı yalnızca dipnotlarda açıklanmakla yetinilir"],
  f"Yeniden değerleme artışı = {tr(gud5)} − {tr(ndd5)} = {tr(art5)} TL. Daha önce kâr veya zarara yazılmış bir azalış bulunmadığından artışın tamamı diğer kapsamlı gelirde muhasebeleştirilir ve özkaynakta yeniden değerleme değer artışı olarak birikir.",
  "TMS 16 - yeniden değerleme artışı hesabı")

q("Yeniden değerleme değer artışının özkaynak içindeki aktarımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık bilanço dışı bırakıldığında doğrudan geçmiş yıllar kârlarına aktarılabilir",
  ["Değer artışı her hâlde dönem kâr veya zararına aktarılmak zorunda olan bir kalemi ifade eder",
   "Değer artışı hiçbir hâlde ve hiçbir biçimde başka bir özkaynak kalemine aktarılamamaktadır",
   "Değer artışı her hâlde ortaklara kâr payı olarak dağıtılmak zorunda tutulan bir tutardır",
   "Değer artışının aktarımı TMS 16'da düzenlenmemiş olup serbest bırakılmış bir husus niteliğindedir"],
  "TMS 16: özkaynakta yer alan yeniden değerleme değer artışı, varlığın finansal durum tablosu dışı bırakılması sırasında doğrudan geçmiş yıllar kârlarına aktarılabilir. Bu aktarım kâr veya zarar üzerinden YAPILMAZ.",
  "TMS 16 - değer artışının aktarımı")

q("Maddi duran varlığın finansal durum tablosu dışı bırakılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Elden çıkarıldığında veya kullanımından ya da elden çıkarılmasından gelecekte ekonomik yarar beklenmediğinde bilanço dışı bırakılır",
  ["Varlık yalnızca fiziken yok olduğunda bilanço dışı bırakılabilen bir kalemi ifade etmektedir",
   "Varlık hiçbir hâlde bilanço dışı bırakılamaz; faydalı ömür sonunda dahi kayıtlarda kalmaktadır",
   "Varlık yalnızca vergi idaresi izin verdiğinde bilanço dışı bırakılabilen bir kalem niteliğindedir",
   "Bilanço dışı bırakma koşulları TMS 16'da düzenlenmemiş olup serbest bırakılmış bulunmaktadır"],
  "TMS 16: bir maddi duran varlık kaleminin defter değeri, (a) elden çıkarıldığında veya (b) kullanımından ya da elden çıkarılmasından gelecekte ekonomik yarar beklenmediğinde finansal durum tablosu dışı bırakılır.",
  "TMS 16 - bilanço dışı bırakma")

q("Maddi duran varlığın bilanço dışı bırakılmasından doğan kazanç veya kayıp bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr veya zarara dâhil edilir; ancak kazanç hasılat olarak sınıflandırılmaz",
  ["Kazanç her hâlde hasılat olarak sınıflandırılıp gelir tablosunun en üstünde gösterilmektedir",
   "Kazanç veya kayıp her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulmuştur",
   "Kazanç veya kayıp hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Kazanç veya kayıp doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade eder"],
  "TMS 16: bir maddi duran varlık kaleminin bilanço dışı bırakılmasından doğan kazanç veya kayıp, kâr veya zarara dâhil edilir. Ancak kazançlar HASILAT olarak sınıflandırılmaz.",
  "TMS 16 - bilanço dışı bırakma kazancı")

m6, bir6, satis6 = 400_000, 250_000, 180_000
ndd6 = m6 - bir6
kar6 = satis6 - ndd6
q(f"Maliyeti {tr(m6)} TL ve birikmiş amortismanı {tr(bir6)} TL olan bir makine {tr(satis6)} TL'ye satılmıştır. Bu satıştan doğan kazanç veya kayıp kaç TL'dir?",
  f"{tr(kar6)} TL kazanç",
  [f"{tr(satis6)} TL kazanç; satış bedelinin tamamı kazanç olarak kâr veya zarara yansıtılmaktadır",
   f"{tr(m6 - satis6)} TL kayıp; maliyet ile satış bedeli arasındaki fark kayıp olarak kaydedilir",
   f"{tr(kar6)} TL kayıp; net defter değeri satış bedelinden yüksek olduğundan kayıp doğmaktadır",
   f"{tr(bir6 - satis6) if bir6 > satis6 else tr(satis6 - bir6)} TL kazanç; birikmiş amortisman ile satış bedeli karşılaştırılmaktadır"],
  f"Net defter değeri = Maliyet − Birikmiş amortisman = {tr(m6)} − {tr(bir6)} = {tr(ndd6)} TL. Kazanç = Satış bedeli − Net defter değeri = {tr(satis6)} − {tr(ndd6)} = {tr(kar6)} TL kazanç. Bu kazanç kâr veya zarara dâhil edilir; hasılat olarak sınıflandırılmaz.",
  "TMS 16 - satış kazancı hesabı")

m7, bir7, satis7 = 700_000, 400_000, 260_000
ndd7 = m7 - bir7
zar7 = ndd7 - satis7
q(f"Maliyeti {tr(m7)} TL ve birikmiş amortismanı {tr(bir7)} TL olan bir taşıt {tr(satis7)} TL'ye satılmıştır. Bu satıştan doğan kazanç veya kayıp kaç TL'dir?",
  f"{tr(zar7)} TL kayıp",
  [f"{tr(zar7)} TL kazanç; satış bedeli net defter değerinin üzerinde kaldığından kazanç doğmaktadır",
   f"{tr(m7 - satis7)} TL kayıp; maliyet ile satış bedeli arasındaki fark kayıp olarak kaydedilmektedir",
   f"{tr(satis7)} TL kayıp; satış bedelinin tamamı kayıp olarak kâr veya zarara yansıtılmaktadır",
   f"{tr(bir7 - satis7)} TL kayıp; birikmiş amortisman ile satış bedeli karşılaştırılarak bulunmaktadır"],
  f"Net defter değeri = {tr(m7)} − {tr(bir7)} = {tr(ndd7)} TL. Satış bedeli {tr(satis7)} TL, net defter değerinin altında olduğundan kayıp doğar: {tr(ndd7)} − {tr(satis7)} = {tr(zar7)} TL kayıp. Kâr veya zarara dâhil edilir.",
  "TMS 16 - satış kaybı hesabı")

q("Yeniden değerleme modeli uygulanan bir varlık sınıfının tamamının yeniden değerlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Aynı sınıftaki tüm varlıklar eşzamanlı olarak yeniden değerlenir",
  ["Sınıftaki varlıklardan yalnızca değeri artanlar seçilerek yeniden değerlenebilmektedir",
   "Sınıftaki varlıklardan yalnızca değeri azalanlar seçilerek yeniden değerlenmek zorundadır",
   "Sınıftaki her varlık farklı tarihlerde ve işletmenin dilediği sırayla yeniden değerlenebilir",
   "Sınıf kavramı TMS 16'da düzenlenmemiş olup yeniden değerlemede dikkate alınmamaktadır"],
  "TMS 16: bir maddi duran varlık yeniden değerlendiğinde, ait olduğu sınıfın tamamı yeniden değerlenir. Bir sınıfın içindeki varlıklar, seçmeli yeniden değerlemeyi ve farklı tarihlerdeki maliyet-değer karışımını önlemek için eşzamanlı olarak yeniden değerlenir.",
  "TMS 16 - sınıfın eşzamanlı değerlemesi")

q("TMS 16'ya göre maddi duran varlık sınıfı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin faaliyetlerinde benzer nitelikte ve kullanıma sahip varlıkların gruplandırılmasıdır",
  ["İşletmenin en pahalı varlıklarının bir araya getirilmesiyle oluşturulan bir grubu ifade eder",
   "İşletmenin aynı yılda satın aldığı varlıkların bir araya getirilmesini ifade eden bir kavramdır",
   "İşletmenin aynı tedarikçiden aldığı varlıkların gruplandırılmasını ifade eden bir kavramdır",
   "Varlık sınıfı kavramı TMS 16'da tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 16: bir maddi duran varlık sınıfı, bir işletmenin faaliyetlerinde benzer nitelik ve kullanıma sahip varlıkların gruplandırılmasıdır (arazi, binalar, makineler, taşıtlar, demirbaşlar gibi).",
  "TMS 16 - varlık sınıfı")

q("Maddi duran varlıklarda değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Değer düşüklüğünün belirlenmesinde TMS 36 uygulanır",
  ["Değer düşüklüğü TMS 16'da ayrıntılı düzenlenmiş olup başka bir standarda başvurulmamaktadır",
   "Maddi duran varlıklarda hiçbir hâlde değer düşüklüğü söz konusu olmayan bir durum bulunmaktadır",
   "Değer düşüklüğü yalnızca stoklar için söz konusu olup duran varlıklara hiç uygulanmamaktadır",
   "Değer düşüklüğü yalnızca vergi mevzuatına göre belirlenir; hiçbir standart hükmü bulunmamaktadır"],
  "TMS 16: bir maddi duran varlık kaleminin değer düşüklüğüne uğrayıp uğramadığının belirlenmesinde işletme TMS 36 Varlıklarda Değer Düşüklüğü Standardını uygular.",
  "TMS 16 - değer düşüklüğü")

q("Aşağıdaki ifadelerden hangileri yeniden değerleme bakımından doğrudur?\n\nI. Yeniden değerleme artışı kural olarak diğer kapsamlı gelirde muhasebeleştirilir\n\nII. Yeniden değerleme artışı her hâlde dönem kâr veya zararına yazılır\n\nIII. Seçilen model varlık sınıfının tamamına uygulanır",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Yeniden değerleme artışı kural olarak diğer kapsamlı gelirde muhasebeleştirilir (I) ve seçilen ölçüm modeli varlık sınıfının tamamına uygulanır (III). Artış yalnızca daha önce kâr veya zarara yazılmış bir azalışı tersine çevirdiği ölçüde kâr veya zarara yansır; 'her hâlde' kâr veya zarara yazılmaz. Bu nedenle II yanlıştır.",
  "TMS 16 - yeniden değerleme")

q("Aşağıdaki ifadelerden hangileri TMS 16 bakımından doğrudur?\n\nI. Bilanço dışı bırakmadan doğan kazanç hasılat olarak sınıflandırılmaz\n\nII. Bilanço dışı bırakmadan doğan kayıp diğer kapsamlı gelirde muhasebeleştirilir\n\nIII. Değer düşüklüğünde TMS 36 uygulanır",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Bilanço dışı bırakma kazancı kâr veya zarara dâhil edilir ancak hasılat sayılmaz (I) ve değer düşüklüğünde TMS 36 uygulanır (III). Bilanço dışı bırakmadan doğan kazanç ya da kayıp KÂR VEYA ZARARA dâhil edilir, diğer kapsamlı gelire değil; bu nedenle II yanlıştır.",
  "TMS 16 - genel")

q("Maddi duran varlıklara ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Her varlık sınıfı için ölçüm esasları, amortisman yöntemleri, faydalı ömürler ve defter değeri hareketleri açıklanır",
  ["Maddi duran varlıklar hakkında hiçbir açıklama yapılmaz; yalnızca tutar bilançoda gösterilmektedir",
   "Yalnızca varlıkların toplam tutarı açıklanır; sınıf bazında hiçbir bilgi verilmemektedir",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmamaktadır",
   "Açıklama yalnızca yeniden değerleme modeli uygulayan işletmeler için zorunlu tutulmuştur"],
  "TMS 16: finansal tablolarda her bir maddi duran varlık sınıfı için brüt defter değerinin belirlenmesinde kullanılan ölçüm esasları, kullanılan amortisman yöntemleri, faydalı ömürler veya amortisman oranları ile dönem başı ve sonu defter değeri mutabakatı açıklanır.",
  "TMS 16 - açıklamalar")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 16; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} | harf {''.join(x['answer'] for x in out)[:40]}…")
