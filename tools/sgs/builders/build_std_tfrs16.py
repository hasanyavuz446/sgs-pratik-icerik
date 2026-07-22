# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TFRS 16 Kiralamalar — 60 soru.
Kaynak: KGK TFRS 16. Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-9 soru, "hepsi" ~2 (%22-25).
NOT: faiz/iskonto oranları SÖZLEŞME oranıdır ve soru kökünde verilir → yıla bağlı değil."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tfrs_16_kiralamalar"
PREFIX, SEED = "std-tfrs16-gen", 20260805
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tfrs_16_kiralamalar.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanım ve kapsam (14) ────────────────────────────────────────────────
q("TFRS 16'ya göre kiralama bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir varlığın kullanım hakkını belirli bir süre için bedel karşılığında devreden sözleşmedir",
  ["Bir varlığın mülkiyetinin bedel karşılığında kesin olarak devredilmesini ifade eden sözleşmedir",
   "Bir işletmenin başka bir işletmenin paylarını satın almasını ifade eden bir sözleşme türüdür",
   "Bir varlığın bakım ve onarımının üstlenilmesini ifade eden bir hizmet sözleşmesi niteliğindedir",
   "Kiralama kavramı TFRS 16'da tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TFRS 16: kiralama, bir varlığın (dayanak varlık) kullanım hakkını bir bedel karşılığında belirli bir süre için devreden sözleşme ya da sözleşmenin bir parçasıdır.",
  "TFRS 16 - kiralama tanımı")

q("Bir sözleşmenin kiralama niteliği taşıması bakımından aşağıdakilerden hangisi doğrudur?",
  "Tanımlanmış bir varlığın kullanımını kontrol etme hakkının bedel karşılığında devredilmesi gerekir",
  ["Yalnızca sözleşmede 'kiralama' ifadesinin geçmesi yeterli olup başka bir koşul aranmamaktadır",
   "Yalnızca varlığın mülkiyetinin devredilmiş olması gerekir; kullanım hakkı yeterli sayılmaz",
   "Yalnızca sözleşmenin bir yıldan uzun süreli olması yeterli olup başka koşul aranmamaktadır",
   "Kiralama niteliğinin belirlenmesi TFRS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TFRS 16: bir sözleşme, tanımlanmış bir varlığın kullanımını kontrol etme hakkını belirli bir süre için bedel karşılığında devrediyorsa kiralamadır ya da kiralama içerir.",
  "TFRS 16 - kiralama tanımının unsurları")

q("Tanımlanmış varlığın kullanımını kontrol etme hakkı bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanımdan sağlanacak ekonomik yararların tamamına yakınını elde etme ve kullanımı yönetme hakkı bulunmalıdır",
  ["Yalnızca varlığın fiziken teslim alınmış olması yeterli olup başka bir koşul aranmamaktadır",
   "Yalnızca kira bedelinin peşin olarak ödenmiş olması yeterli olup başka koşul aranmamaktadır",
   "Yalnızca varlığın hukuki mülkiyetinin devralınmış olması gerekir; kullanım hakkı yetmemektedir",
   "Kontrol etme hakkı TFRS 16'da tanımlanmamış olup uygulamada dikkate alınmayan bir husustur"],
  "TFRS 16: müşteri, kullanım süresi boyunca (a) tanımlanmış varlığın kullanımından sağlanacak ekonomik yararların tamamına yakınını elde etme hakkına ve (b) tanımlanmış varlığın kullanımını yönetme hakkına sahipse varlığın kullanımını kontrol ediyordur.",
  "TFRS 16 - kontrol etme hakkı")

q("Tanımlanmış varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık genellikle sözleşmede açıkça belirtilir; tedarikçi ikame etme hakkına sahipse varlık tanımlanmış değildir",
  ["Varlığın sözleşmede belirtilmesi hiçbir hâlde gerekmez; her varlık tanımlanmış sayılmaktadır",
   "Tedarikçinin ikame hakkı bulunsa dahi varlık her hâlde tanımlanmış sayılmak zorunda kalınır",
   "Yalnızca gayrimenkuller tanımlanmış varlık sayılır; taşınırlar hiçbir hâlde kapsama girmez",
   "Tanımlanmış varlık kavramı TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: varlık genellikle sözleşmede açıkça belirtilerek tanımlanır. Ancak tedarikçinin kullanım süresi boyunca varlığı ikame etmeye ilişkin esasa ilişkin bir hakkı varsa varlık tanımlanmış değildir.",
  "TFRS 16 - tanımlanmış varlık")

q("TFRS 16'nın kiracı muhasebesindeki temel yaklaşımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiracı tüm kiralamalar için tek bir model uygular; finansal ve faaliyet kiralaması ayrımı kaldırılmıştır",
  ["Kiracı finansal ve faaliyet kiralaması ayrımını her hâlde sürdürmek zorunda tutulmaktadır",
   "Kiracı tüm kiralamaları her hâlde faaliyet kiralaması olarak muhasebeleştirmek zorundadır",
   "Kiracı hiçbir kiralamayı finansal tablolarına yansıtmaz; tümü dipnotta açıklanmaktadır",
   "Kiracı muhasebesi TFRS 16'da düzenlenmemiş olup serbest bırakılmış bir husus niteliğindedir"],
  "TFRS 16: kiracı açısından finansal kiralama ile faaliyet kiralaması ayrımı KALDIRILMIŞTIR. Kiracı, kısa vadeli ve düşük değerli varlık muafiyetleri dışındaki tüm kiralamalar için kullanım hakkı varlığı ve kira yükümlülüğü muhasebeleştirir.",
  "TFRS 16 - kiracıda tek model")

q("Kiraya veren muhasebesindeki sınıflandırma bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya veren, kiralamalarını finansal kiralama veya faaliyet kiralaması olarak sınıflandırmayı sürdürür",
  ["Kiraya veren için de finansal ve faaliyet kiralaması ayrımı tümüyle kaldırılmış bulunmaktadır",
   "Kiraya veren tüm kiralamaları her hâlde finansal kiralama olarak sınıflandırmak zorundadır",
   "Kiraya veren hiçbir kiralamayı finansal tablolarına yansıtmaz; tümü dipnotta açıklanmaktadır",
   "Kiraya veren muhasebesi TFRS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TFRS 16: kiraya veren, kiralamalarının her birini faaliyet kiralaması veya finansal kiralama olarak sınıflandırır. Kiracıdaki ayrım kaldırılmış olsa da KİRAYA VERENDE ayrım DEVAM ETMEKTEDİR. Bu, Standardın en çok karıştırılan noktasıdır.",
  "TFRS 16 - kiraya verende ayrım sürer")

q("Kiracının uygulayabileceği muafiyetler bakımından aşağıdakilerden hangisi doğrudur?",
  "Kısa vadeli kiralamalar ile dayanak varlığın düşük değerli olduğu kiralamalarda muafiyet uygulanabilir",
  ["Kiracı için hiçbir muafiyet öngörülmemiş olup tüm kiralamalar bilançoya alınmak zorundadır",
   "Kiracı dilediği kiralamayı muafiyet kapsamına alabilir; hiçbir ölçüt aranmamaktadır",
   "Muafiyet yalnızca gayrimenkul kiralamaları için uygulanabilen bir kolaylığı ifade etmektedir",
   "Muafiyetler TFRS 16'da düzenlenmemiş olup uygulamada hiç kullanılmayan bir husustur"],
  "TFRS 16: kiracı, (a) kısa vadeli kiralamalara ve (b) dayanak varlığın düşük değerli olduğu kiralamalara Standardın muhasebeleştirme hükümlerini uygulamamayı seçebilir.",
  "TFRS 16 - muafiyetler")

q("Kısa vadeli kiralama bakımından aşağıdakilerden hangisi doğrudur?",
  "Başlangıç tarihinde kiralama süresi on iki ay veya daha kısa olan ve satın alma opsiyonu içermeyen kiralamadır",
  ["Başlangıç tarihinde kiralama süresi yirmi dört ay veya daha kısa olan her türlü kiralamayı ifade eder",
   "Satın alma opsiyonu içerse dahi süresi kısa olan her kiralama bu kapsamda değerlendirilmektedir",
   "Kira bedeli düşük olan her kiralama süresine bakılmaksızın kısa vadeli sayılmak zorundadır",
   "Kısa vadeli kiralama kavramı TFRS 16'da tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: kısa vadeli kiralama, başlangıç tarihinde kiralama süresi 12 ay veya daha az olan kiralamadır. Satın alma opsiyonu içeren bir kiralama kısa vadeli kiralama DEĞİLDİR.",
  "TFRS 16 - kısa vadeli kiralama")

q("Muafiyet uygulanan kiralamalarda kira ödemeleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Kira ödemeleri kiralama süresi boyunca doğrusal olarak gider muhasebeleştirilir",
  ["Kira ödemeleri her hâlde kullanım hakkı varlığı olarak aktifleştirilmek zorunda tutulmaktadır",
   "Kira ödemeleri her hâlde tek seferde ve peşin olarak gider yazılmak zorunda bulunmaktadır",
   "Kira ödemeleri hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Kira ödemeleri her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemlerdir"],
  "TFRS 16: muafiyet seçilen kiralamalarda kiracı, kiralamaya ilişkin kira ödemelerini kiralama süresi boyunca doğrusal olarak veya başka bir sistematik esasa göre gider olarak muhasebeleştirir.",
  "TFRS 16 - muafiyette gider yazma")

q("Düşük değerli varlık muafiyetinin uygulanma düzeyi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiralama bazında uygulanabilir; dayanak varlığın yeniyken değerine göre değerlendirilir",
  ["Yalnızca işletmenin tamamı için topluca uygulanabilen bir muafiyeti ifade etmektedir",
   "Yalnızca varlığın kiralama tarihindeki kullanılmış hâlinin değerine göre değerlendirilmektedir",
   "Düşük değer ölçütü her hâlde kiracının toplam varlıklarına oranlanarak belirlenmek zorundadır",
   "Bu muafiyetin uygulanma düzeyi TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: düşük değerli varlık kiralamalarına ilişkin muafiyet kiralama bazında uygulanabilir. Bir dayanak varlığın düşük değerli olup olmadığı, varlığın YENİ hâlindeki değerine göre ve kiracının büyüklüğünden bağımsız olarak mutlak biçimde değerlendirilir.",
  "TFRS 16 - düşük değerli varlık")

q("Kısa vadeli kiralama muafiyetinin uygulanma düzeyi bakımından aşağıdakilerden hangisi doğrudur?",
  "Dayanak varlık sınıfı bazında yapılan bir tercihtir",
  ["Her kiralama için ayrı ayrı ve serbestçe yapılabilen bir tercihi ifade etmektedir",
   "İşletmenin tüm kiralamaları için topluca yapılmak zorunda olan bir tercihi ifade eder",
   "Yalnızca kiraya verenin onay vermesi hâlinde yapılabilen bir tercih niteliğinde bulunur",
   "Bu tercihin düzeyi TFRS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TFRS 16: kısa vadeli kiralamalara ilişkin tercih, kullanım hakkının ilgili olduğu dayanak varlık sınıfı bazında yapılır. Düşük değerli varlık muafiyeti ise kiralama bazında uygulanabilir.",
  "TFRS 16 - muafiyet tercihinin düzeyi")

q("Bir işletme, ofisinde kullanmak üzere bir dizüstü bilgisayarı iki yıllığına kiralamıştır. TFRS 16 bakımından aşağıdakilerden hangisi doğrudur?",
  "Dayanak varlık düşük değerliyse muafiyet uygulanıp kira ödemeleri doğrusal gider yazılabilir",
  ["Süre on iki ayı aştığından her hâlde kullanım hakkı varlığı muhasebeleştirilmek zorundadır",
   "Bilgisayar kiralamaları TFRS 16 kapsamı dışında olup hiçbir hâlde kayda alınmamaktadır",
   "Kira ödemeleri her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulan kalemlerdir",
   "Kiralama her hâlde finansal kiralama sayılır ve dayanak varlık aktifleştirilmek zorundadır"],
  "TFRS 16: kiralama süresi 12 ayı aştığından kısa vadeli kiralama muafiyeti uygulanamaz. Ancak dizüstü bilgisayar gibi dayanak varlığın düşük değerli olduğu kiralamalarda ayrı bir muafiyet vardır; kiracı bunu seçerse kira ödemelerini doğrusal olarak gider yazar.",
  "TFRS 16 - düşük değerli varlık (senaryo)")

q("Aşağıdakilerden hangileri TFRS 16'ya göre kiracının muafiyet uygulayabileceği kiralamalardandır?\n\nI. Kısa vadeli kiralamalar\n\nII. Dayanak varlığın yüksek değerli olduğu kiralamalar\n\nIII. Kiracının kârsız olduğu dönemdeki kiralamalar",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Kısa vadeli kiralamalarda muafiyet uygulanabilir (I). İkinci muafiyet yüksek değil, düşük değerli dayanak varlıklar içindir; bu nedenle II yanlıştır. Kiracının kârlılık durumu da muafiyet ölçütü değildir (III). Yalnız I doğrudur.",
  "TFRS 16 - muafiyetler")

q("Aşağıdaki ifadelerden hangileri TFRS 16 bakımından doğrudur?\n\nI. Kiracıda finansal-faaliyet kiralaması ayrımı kaldırılmıştır\n\nII. Kiraya verende bu ayrım sürmektedir\n\nIII. Kiraya veren de tüm kiralamalar için tek model uygular",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kiracıda ayrım kaldırılmış (I), kiraya verende ise sürmektedir (II). Kiraya veren tek model UYGULAMAZ; kiralamalarını finansal veya faaliyet kiralaması olarak sınıflandırmaya devam eder. Bu nedenle III yanlıştır.",
  "TFRS 16 - kiracı-kiraya veren ayrımı")

# ── B. Kiracı: ilk ölçüm (16) ──────────────────────────────────────────────
q("Kiracının başlangıç tarihinde yapacağı muhasebeleştirme bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir kullanım hakkı varlığı ve bir kira yükümlülüğü muhasebeleştirir",
  ["Yalnızca kira gideri muhasebeleştirir; bilançoda hiçbir kalem oluşturulmamaktadır",
   "Dayanak varlığın kendisini maddi duran varlık olarak aktifleştirmek zorunda tutulmaktadır",
   "Yalnızca dipnotlarda açıklama yapar; finansal tablolara hiçbir tutar yansıtılmamaktadır",
   "Yalnızca bir yükümlülük muhasebeleştirir; varlık tarafında hiçbir kayıt yapılmamaktadır"],
  "TFRS 16: kiracı, başlangıç tarihinde bir kullanım hakkı varlığı ve bir kira yükümlülüğü muhasebeleştirir. Kiracı dayanak varlığın kendisini değil, onu kullanma HAKKINI aktifleştirir.",
  "TFRS 16 - kiracının ilk muhasebeleştirmesi")

q("Kira yükümlülüğünün ilk ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Başlangıç tarihinde ödenmemiş kira ödemelerinin bugünkü değeriyle ölçülür",
  ["Ödenecek toplam kira tutarının iskonto edilmemiş nominal toplamıyla ölçülmek zorundadır",
   "Dayanak varlığın gerçeğe uygun değeriyle ölçülür; kira ödemeleri dikkate alınmamaktadır",
   "Yalnızca ilk yılın kira ödemesi tutarıyla ölçülür; sonraki yıllar hiç dikkate alınmaz",
   "Kira yükümlülüğünün ilk ölçümü TFRS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TFRS 16: kiracı başlangıç tarihinde kira yükümlülüğünü, o tarihte ödenmemiş olan kira ödemelerinin bugünkü değeri üzerinden ölçer.",
  "TFRS 16 - kira yükümlülüğü ilk ölçümü")

q("Kira ödemelerinin iskonto edilmesinde kullanılacak oran bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiralamadaki zımni faiz oranı kolayca belirlenebiliyorsa o, aksi hâlde kiracının alternatif borçlanma faiz oranı kullanılır",
  ["Her hâlde ve istisnasız kiracının alternatif borçlanma faiz oranı kullanılmak zorunda kalınır",
   "Her hâlde merkez bankasının ilan ettiği politika faizi kullanılmak zorunda tutulmaktadır",
   "İskonto oranı kullanılmaz; kira ödemeleri nominal tutarlarıyla toplanmak zorunda bulunur",
   "İskonto oranının belirlenmesi TFRS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TFRS 16: kira ödemeleri, kiralamadaki zımni faiz oranı kolaylıkla belirlenebiliyorsa bu oran kullanılarak iskonto edilir. Bu oran kolaylıkla belirlenemiyorsa kiracı, kendi alternatif borçlanma faiz oranını kullanır.",
  "TFRS 16 - iskonto oranı")

q("Kullanım hakkı varlığının ilk ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet bedeliyle ölçülür",
  ["Gerçeğe uygun değeriyle ölçülür; maliyet bedeli hiçbir hâlde dikkate alınmamaktadır",
   "Net gerçekleşebilir değeriyle ölçülür; bu değer maliyetten her hâlde düşük olmaktadır",
   "Dayanak varlığın defter değeriyle ölçülür; kiraya verenin kayıtları esas alınmaktadır",
   "Kullanım hakkı varlığının ilk ölçümü TFRS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TFRS 16: kiracı, başlangıç tarihinde kullanım hakkı varlığını maliyet bedeli üzerinden ölçer.",
  "TFRS 16 - kullanım hakkı varlığı ilk ölçümü")

q("Kullanım hakkı varlığının maliyetine giren unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kira yükümlülüğü, peşin ödemeler, doğrudan maliyetler ve restorasyon tahmini girer; teşvikler düşülür",
  ["Yalnızca kira yükümlülüğünün ilk ölçüm tutarı maliyete girer; diğer unsurlar gider yazılır",
   "Yalnızca peşin ödenen kira tutarı maliyete girer; kira yükümlülüğü dikkate alınmamaktadır",
   "İşletmenin tüm genel yönetim giderleri de maliyete dâhil edilmek zorunda tutulmaktadır",
   "Kullanım hakkı varlığının maliyet unsurları TFRS 16'da düzenlenmemiş bir husustur"],
  "TFRS 16: kullanım hakkı varlığının maliyeti; (a) kira yükümlülüğünün ilk ölçüm tutarını, (b) başlangıç tarihinde veya öncesinde yapılan kira ödemelerinden alınan kiralama teşvikleri düşülmüş hâlini, (c) kiracı tarafından katlanılan başlangıçtaki doğrudan maliyetleri ve (d) sökme, kaldırma ve restorasyon maliyeti tahminini içerir.",
  "TFRS 16 - kullanım hakkı varlığı maliyeti")

yuk, pesin, dogrudan, tesvik = 500_000, 40_000, 25_000, 15_000
khv = yuk + pesin + dogrudan - tesvik
q(f"Bir kiracının başlangıç tarihinde ölçtüğü kira yükümlülüğü {tr(yuk)} TL'dir. Kiracı başlangıçta {tr(pesin)} TL peşin kira ödemiş, {tr(dogrudan)} TL başlangıçtaki doğrudan maliyete katlanmış ve kiraya verenden {tr(tesvik)} TL kiralama teşviki almıştır. Kullanım hakkı varlığının maliyeti kaç TL'dir?",
  f"{tr(khv)} TL",
  [f"{tr(yuk + pesin + dogrudan + tesvik)} TL",   # teşvik düşülecekken eklendi
   f"{tr(yuk + pesin + dogrudan)} TL",            # teşvik hiç düşülmedi
   f"{tr(yuk)} TL",                               # yalnızca kira yükümlülüğü alındı
   f"{tr(yuk - pesin - dogrudan + tesvik)} TL"],  # işaretler tümüyle ters
  f"Kullanım hakkı varlığı = Kira yükümlülüğü + Peşin ödemeler + Başlangıçtaki doğrudan maliyetler − Alınan kiralama teşvikleri = {tr(yuk)} + {tr(pesin)} + {tr(dogrudan)} − {tr(tesvik)} = {tr(khv)} TL.",
  "TFRS 16 - kullanım hakkı varlığı maliyeti hesabı")

taksit, faktor = 100_000, 2.4869
pv = round(taksit * faktor)
q(f"Bir işletme bir depoyu 3 yıllığına kiralamıştır. Her yıl sonunda {tr(taksit)} TL kira ödenecektir. Sözleşmedeki zımni faiz oranına göre 3 yıllık eşit taksitli ödemelerin bugünkü değer faktörü 2,4869'dur. Kira yükümlülüğünün ilk ölçüm tutarı kaç TL'dir?",
  f"{tr(pv)} TL",
  [f"{tr(taksit * 3)} TL", f"{tr(taksit)} TL", f"{tr(round(taksit * 3 * faktor))} TL", f"{tr(round(taksit / faktor))} TL"],
  f"Kira yükümlülüğü, ödenmemiş kira ödemelerinin BUGÜNKÜ DEĞERİDİR; nominal toplam değildir. Bugünkü değer = Yıllık taksit × Bugünkü değer faktörü = {tr(taksit)} × 2,4869 = {tr(pv)} TL. Nominal toplam olan {tr(taksit * 3)} TL yükümlülük tutarı değildir.",
  "TFRS 16 - kira yükümlülüğü bugünkü değeri")

q("Başlangıçtaki doğrudan maliyetler bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiracı tarafından katlanılan bu maliyetler kullanım hakkı varlığının maliyetine dâhil edilir",
  ["Bu maliyetler her hâlde ve istisnasız doğrudan dönem gideri yazılmak zorunda tutulmaktadır",
   "Bu maliyetler her hâlde kira yükümlülüğüne eklenmek zorunda olan bir kalemi ifade etmektedir",
   "Bu maliyetler hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Başlangıçtaki doğrudan maliyetler TFRS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TFRS 16: kiracı tarafından katlanılan başlangıçtaki doğrudan maliyetler, kullanım hakkı varlığının maliyetine dâhil edilir.",
  "TFRS 16 - başlangıçtaki doğrudan maliyetler")

q("Kira ödemelerinin kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Sabit ödemeler, endekse bağlı değişken ödemeler, kalıntı değer taahhütleri ve makul ölçüde kesin opsiyon bedelleri dâhildir",
  ["Yalnızca sabit kira ödemeleri dâhildir; diğer hiçbir unsur hesaba katılmamaktadır",
   "Yalnızca değişken kira ödemeleri dâhildir; sabit ödemeler hiç dikkate alınmamaktadır",
   "İşletmenin tüm işletme giderleri de kira ödemesi sayılarak hesaba katılmak zorundadır",
   "Kira ödemelerinin kapsamı TFRS 16'da düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TFRS 16: kira ödemeleri; sabit ödemeleri (alınacak teşvikler düşülmüş), bir endeks veya orana bağlı değişken kira ödemelerini, kalıntı değer taahhütleri kapsamında ödenmesi beklenen tutarları, kullanılacağı makul ölçüde kesin olan satın alma opsiyonunun kullanım fiyatını ve sonlandırma cezalarını içerir.",
  "TFRS 16 - kira ödemelerinin kapsamı")

q("Endekse veya orana bağlı OLMAYAN değişken kira ödemeleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Kira yükümlülüğünün ölçümüne dâhil edilmez; gerçekleştiği dönemde gider yazılır",
  ["Her hâlde kira yükümlülüğünün ölçümüne dâhil edilmek zorunda olan bir kalemi ifade eder",
   "Her hâlde kullanım hakkı varlığının maliyetine eklenmek zorunda tutulan bir kalemdir",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Bu ödemelerin ele alınışı TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: bir endekse veya orana bağlı olmayan değişken kira ödemeleri (satış hasılatına bağlı ödemeler gibi) kira yükümlülüğünün ölçümüne dâhil edilmez; bunları tetikleyen olayın gerçekleştiği dönemde kâr veya zararda muhasebeleştirilir.",
  "TFRS 16 - değişken kira ödemeleri")

q("Kiralama süresinin belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İptal edilemeyen süreye, kullanılacağı makul ölçüde kesin olan uzatma opsiyonu dönemleri eklenir",
  ["Yalnızca iptal edilemeyen süre dikkate alınır; uzatma opsiyonları hiçbir hâlde eklenmez",
   "Tüm uzatma opsiyonları her hâlde ve koşulsuz olarak kiralama süresine eklenmek zorundadır",
   "Kiralama süresi her hâlde on iki ay olarak kabul edilmek zorunda tutulan bir kavramdır",
   "Kiralama süresinin belirlenmesi TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunur"],
  "TFRS 16: kiralama süresi, kiralamanın iptal edilemeyen süresi ile (a) kiracının kullanacağından makul ölçüde emin olduğu uzatma opsiyonuna ilişkin dönemleri ve (b) kullanmayacağından makul ölçüde emin olduğu sonlandırma opsiyonuna ilişkin dönemleri kapsar.",
  "TFRS 16 - kiralama süresi")

q("Kiralama ve kiralama niteliği taşımayan bileşenlerin ayrıştırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak ayrıştırılır; ancak kiracı ayrıştırmama kolaylığını dayanak varlık sınıfı bazında seçebilir",
  ["Bileşenler hiçbir hâlde ayrıştırılamaz; sözleşme her zaman bütün olarak ele alınmaktadır",
   "Bileşenler her hâlde ayrıştırılmak zorunda olup hiçbir kolaylık öngörülmemiş bulunmaktadır",
   "Ayrıştırma yalnızca kiraya verenin onay vermesi hâlinde yapılabilen bir işlemi ifade eder",
   "Bileşenlerin ayrıştırılması TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: kiralama içeren bir sözleşmede kiracı, her bir kiralama bileşenini kiralama niteliği taşımayan bileşenlerden (bakım hizmeti gibi) ayrı olarak muhasebeleştirir. Ancak kiracı, dayanak varlık sınıfı bazında bunları ayrıştırmama ve tek bir kiralama bileşeni olarak muhasebeleştirme kolaylığını seçebilir.",
  "TFRS 16 - bileşenlerin ayrıştırılması")

q("Bir işletme, mağazasını on yıllığına kiralamış olup kira bedeli sabittir. TFRS 16 bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiracı kullanım hakkı varlığı ve kira yükümlülüğü muhasebeleştirir",
  ["Kiracı yalnızca kira gideri yazar; bilançoda hiçbir kalem oluşturulmamak zorundadır",
   "Kiracı mağazanın kendisini maddi duran varlık olarak aktifleştirmek zorunda tutulmaktadır",
   "Kiracı bu kiralamayı yalnızca dipnotlarda açıklar; tablolara hiçbir tutar yansıtılmaz",
   "Kiracı bu kiralamayı faaliyet kiralaması sayarak bilanço dışında bırakmak zorundadır"],
  "TFRS 16: kiralama süresi 12 ayı aştığından ve gayrimenkul düşük değerli sayılmadığından muafiyet uygulanamaz. Kiracı, kullanım hakkı varlığı ve kira yükümlülüğü muhasebeleştirir. Eski standarttaki 'faaliyet kiralaması bilanço dışıdır' yaklaşımı KALDIRILMIŞTIR.",
  "TFRS 16 - kiracı muhasebesi (senaryo)")

q("Aşağıdakilerden hangileri kullanım hakkı varlığının maliyetine DÂHİL EDİLİR?\n\nI. Kira yükümlülüğünün ilk ölçüm tutarı\n\nII. Başlangıçtaki doğrudan maliyetler\n\nIII. Sökme ve restorasyon maliyeti tahmini",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TFRS 16 üçünü de kullanım hakkı varlığının maliyetine dâhil eder: kira yükümlülüğünün ilk ölçüm tutarı (I), kiracının katlandığı başlangıçtaki doğrudan maliyetler (II) ve sökme/kaldırma/restorasyon maliyeti tahmini (III). Alınan kiralama teşvikleri ise düşülür.",
  "TFRS 16 - kullanım hakkı varlığı maliyeti")

q("Aşağıdaki ifadelerden hangileri kira yükümlülüğü bakımından doğrudur?\n\nI. Ödenmemiş kira ödemelerinin bugünkü değeriyle ölçülür\n\nII. Zımni faiz oranı belirlenemiyorsa alternatif borçlanma faiz oranı kullanılır\n\nIII. Endekse bağlı olmayan değişken ödemeler yükümlülüğe dâhil edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kira yükümlülüğü bugünkü değerle ölçülür (I) ve zımni oran kolayca belirlenemiyorsa kiracının alternatif borçlanma faiz oranı kullanılır (II). Endekse veya orana bağlı OLMAYAN değişken ödemeler ise yükümlülüğe DÂHİL EDİLMEZ; gerçekleştiğinde gider yazılır. Bu nedenle III yanlıştır.",
  "TFRS 16 - kira yükümlülüğü")

# ── C. Kiracı: sonraki ölçüm (14) ──────────────────────────────────────────
q("Kullanım hakkı varlığının sonraki ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak maliyet modeliyle; birikmiş amortisman ve birikmiş değer düşüklüğü indirilerek ölçülür",
  ["Her hâlde gerçeğe uygun değeriyle ölçülür; amortisman hiçbir hâlde ayrılmamaktadır",
   "Her hâlde ilk maliyetiyle gösterilir; birikmiş amortisman hiçbir hâlde indirilmemektedir",
   "Her hâlde net gerçekleşebilir değeriyle ölçülür; maliyet bilgisi hiç dikkate alınmaz",
   "Kullanım hakkı varlığının sonraki ölçümü TFRS 16'da düzenlenmemiş bir husustur"],
  "TFRS 16: kiracı, kullanım hakkı varlığını başlangıç tarihinden sonra maliyet yöntemini uygulayarak ölçer; maliyetinden birikmiş amortisman ve birikmiş değer düşüklüğü zararları indirilir ve kira yükümlülüğünün yeniden ölçümüne göre düzeltilir.",
  "TFRS 16 - kullanım hakkı varlığının sonraki ölçümü")

q("Kullanım hakkı varlığının amortisman süresi bakımından aşağıdakilerden hangisi doğrudur?",
  "Mülkiyet devri veya opsiyon varsa faydalı ömür; aksi hâlde kiralama süresi ile ömürden kısa olanı",
  ["Her hâlde dayanak varlığın faydalı ömrü esas alınır; kiralama süresi hiç dikkate alınmaz",
   "Her hâlde kiralama süresi esas alınır; dayanak varlığın faydalı ömrü hiç dikkate alınmaz",
   "Her hâlde kiralama süresi ile faydalı ömürden UZUN olanı esas alınmak zorunda kalınır",
   "Amortisman süresi TFRS 16'da düzenlenmemiş olup işletmenin takdirine bırakılmıştır"],
  "TFRS 16: kiralama kiracıya mülkiyeti devrediyorsa veya kiracının satın alma opsiyonunu kullanacağı makul ölçüde kesinse, kiracı kullanım hakkı varlığını dayanak varlığın faydalı ömrü boyunca amortismana tabi tutar. Aksi hâlde, kiralama süresinin sonu ile faydalı ömrün sonundan ERKEN olanına kadar amortismana tabi tutar.",
  "TFRS 16 - amortisman süresi")

khv2, kira_sure, fay_omur = 550_000, 5, 8
amort2 = khv2 / kira_sure
q(f"Bir kiracının kullanım hakkı varlığının maliyeti {tr(khv2)} TL'dir. Kiralama süresi {kira_sure} yıl, dayanak varlığın faydalı ömrü {fay_omur} yıldır. Kiralama mülkiyeti devretmemekte ve satın alma opsiyonu bulunmamaktadır. Yıllık amortisman gideri kaç TL'dir?",
  f"{tr(amort2)} TL",
  [f"{tr(khv2 / fay_omur)} TL", f"{tr(khv2 / (kira_sure + fay_omur))} TL", f"{tr(khv2)} TL", f"{tr(khv2 / 2 / kira_sure)} TL"],
  f"Mülkiyet devri ve satın alma opsiyonu bulunmadığından amortisman süresi, kiralama süresi ({kira_sure} yıl) ile faydalı ömürden ({fay_omur} yıl) KISA olanıdır: {kira_sure} yıl. Yıllık amortisman = {tr(khv2)} ÷ {kira_sure} = {tr(amort2)} TL.",
  "TFRS 16 - amortisman süresi hesabı")

q("Kira yükümlülüğünün sonraki ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Defter değeri faiz tutarı kadar artırılır, yapılan kira ödemeleri kadar azaltılır",
  ["Defter değeri her hâlde sabit kalır; hiçbir faiz veya ödeme etkisi yansıtılmamaktadır",
   "Defter değeri yalnızca ödemeler kadar azaltılır; faiz tutarı hiç dikkate alınmamaktadır",
   "Defter değeri her hâlde gerçeğe uygun değeriyle yeniden ölçülmek zorunda tutulmaktadır",
   "Kira yükümlülüğünün sonraki ölçümü TFRS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TFRS 16: kiracı, başlangıç tarihinden sonra kira yükümlülüğünü (a) defter değerini kira yükümlülüğündeki faizi yansıtacak biçimde artırarak, (b) yapılan kira ödemelerini yansıtacak biçimde azaltarak ve (c) yeniden değerlendirmeleri yansıtacak biçimde yeniden ölçerek ölçer.",
  "TFRS 16 - kira yükümlülüğünün sonraki ölçümü")

yuk3, oran3, odeme3 = 600_000, 8, 150_000
faiz3 = yuk3 * oran3 / 100
anapara3 = odeme3 - faiz3
kalan3 = yuk3 - anapara3
q(f"Bir kiracının dönem başı kira yükümlülüğü {tr(yuk3)} TL, sözleşmedeki faiz oranı yıllık %{oran3}'dir. Dönem sonunda {tr(odeme3)} TL kira ödemesi yapılmıştır. Bu ödemenin anapara kısmı kaç TL'dir?",
  f"{tr(anapara3)} TL",
  [f"{tr(odeme3)} TL", f"{tr(faiz3)} TL", f"{tr(odeme3 + faiz3)} TL", f"{tr(kalan3)} TL"],
  f"Etkin faiz yönteminde önce faiz hesaplanır: {tr(yuk3)} × %{oran3} = {tr(faiz3)} TL. Ödemenin faizi aşan kısmı anaparayı azaltır: {tr(odeme3)} − {tr(faiz3)} = {tr(anapara3)} TL. Dönem sonu yükümlülük = {tr(yuk3)} − {tr(anapara3)} = {tr(kalan3)} TL.",
  "TFRS 16 - faiz ve anapara ayrımı")

q("Kiracının kâr veya zararına yansıyan tutarlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanım hakkı varlığının amortismanı ile kira yükümlülüğüne ilişkin faiz gideri ayrı ayrı yansıtılır",
  ["Yalnızca tek bir kira gideri yansıtılır; amortisman ve faiz ayrımı yapılmamaktadır",
   "Yalnızca amortisman gideri yansıtılır; faiz gideri hiçbir hâlde kaydedilmemektedir",
   "Yalnızca faiz gideri yansıtılır; amortisman hiçbir hâlde ayrılmamak zorunda kalınmaktadır",
   "Kiracının kâr veya zararına hiçbir tutar yansımaz; tümü özkaynakta gösterilmektedir"],
  "TFRS 16: kiracı, kullanım hakkı varlığının amortisman giderini ve kira yükümlülüğüne ilişkin faiz giderini AYRI olarak sunar. Faiz gideri, kira yükümlülüğünün her dönemdeki kalanına sabit bir dönemsel faiz oranı uygulanarak bulunur.",
  "TFRS 16 - amortisman ve faizin ayrı sunumu")

q("Kiracının kiralama giderlerinin dönemler arası dağılımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Faiz gideri yükümlülük azaldıkça düştüğünden toplam gider ilk yıllarda daha yüksektir",
  ["Toplam gider her hâlde tüm dönemlerde eşit tutarda gerçekleşmek zorunda bulunmaktadır",
   "Toplam gider ilk yıllarda daha düşük olup sonraki yıllarda kademeli olarak artmaktadır",
   "Toplam gider yalnızca son yılda muhasebeleştirilir; önceki yıllarda gider yazılmamaktadır",
   "Giderlerin dönemsel dağılımı TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: amortisman genellikle doğrusaldır ancak faiz gideri yükümlülük bakiyesi azaldıkça düşer. Bu nedenle amortisman ve faizin toplamı, kiralamanın ilk yıllarında daha yüksek, sonraki yıllarında daha düşük olur (azalan gider profili).",
  "TFRS 16 - gider profili")

q("Kira yükümlülüğünün yeniden değerlendirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiralama süresi veya ödemelerde değişiklik olursa yeniden ölçülür; düzeltme kullanım hakkı varlığına yapılır",
  ["Kira yükümlülüğü hiçbir hâlde yeniden ölçülemez; ilk ölçüm tutarı süre boyunca korunur",
   "Yeniden ölçüm farkı her hâlde doğrudan dönem kâr veya zararına yansıtılmak zorundadır",
   "Yeniden ölçüm farkı her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulmaktadır",
   "Kira yükümlülüğünün yeniden değerlendirilmesi TFRS 16'da düzenlenmemiş bir husustur"],
  "TFRS 16: kiralama süresinde veya satın alma opsiyonu değerlendirmesinde değişiklik olması ya da kira ödemelerinin değişmesi hâlinde kiracı kira yükümlülüğünü yeniden ölçer. Yeniden ölçüm tutarı, kullanım hakkı varlığına düzeltme olarak yansıtılır. Kullanım hakkı varlığı sıfıra inmişse kalan tutar kâr veya zarara yansıtılır.",
  "TFRS 16 - yeniden değerlendirme")

q("Kullanım hakkı varlığında değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Değer düşüklüğünün belirlenmesinde TMS 36 uygulanır",
  ["Kullanım hakkı varlıklarında hiçbir hâlde değer düşüklüğü söz konusu olmamaktadır",
   "Değer düşüklüğü TFRS 16'da ayrıntılı düzenlenmiş olup başka standarda başvurulmamaktadır",
   "Değer düşüklüğü yalnızca stoklar için söz konusu olup kullanım hakkına uygulanmamaktadır",
   "Değer düşüklüğü yalnızca vergi mevzuatına göre belirlenir; standart hükmü bulunmamaktadır"],
  "TFRS 16: kiracı, kullanım hakkı varlığının değer düşüklüğüne uğrayıp uğramadığını belirlemek ve belirlenen değer düşüklüğü zararını muhasebeleştirmek için TMS 36 Varlıklarda Değer Düşüklüğü Standardını uygular.",
  "TFRS 16 - değer düşüklüğü")

q("Kullanım hakkı varlığının finansal durum tablosunda sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer varlıklardan ayrı olarak sunulur veya hangi kalemde yer aldığı dipnotta açıklanır",
  ["Her hâlde stoklar içinde sunulmak zorunda olup ayrı gösterilmesi mümkün olmamaktadır",
   "Hiçbir biçimde finansal durum tablosunda sunulmaz; yalnızca dipnotta açıklanmaktadır",
   "Her hâlde nakit ve nakit benzerleri içinde sunulmak zorunda tutulan bir kalemi ifade eder",
   "Kullanım hakkı varlığının sunumu TFRS 16'da düzenlenmemiş bir husus niteliğindedir"],
  "TFRS 16: kiracı, kullanım hakkı varlıklarını diğer varlıklardan ayrı olarak finansal durum tablosunda sunar veya dipnotlarda hangi kalemde yer aldığını açıklar.",
  "TFRS 16 - sunum")

q("Kiralamalara ilişkin nakit akışlarının sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kira yükümlülüğünün anapara kısmı finansman faaliyeti olarak sunulur",
  ["Kira ödemelerinin tamamı her hâlde işletme faaliyeti olarak sunulmak zorunda tutulmaktadır",
   "Kira ödemelerinin tamamı her hâlde yatırım faaliyeti olarak sunulmak zorunda bulunmaktadır",
   "Kira ödemeleri nakit akış tablosunda hiçbir biçimde gösterilmez; dipnotta açıklanmaktadır",
   "Kiralamalara ilişkin nakit akışlarının sunumu TFRS 16'da düzenlenmemiş bir husustur"],
  "TFRS 16: kiracı, kira yükümlülüğünün anapara kısmına ilişkin nakit ödemeleri finansman faaliyeti olarak; kısa vadeli, düşük değerli varlık ve değişken kira ödemelerini ise işletme faaliyeti içinde sınıflandırır.",
  "TFRS 16 - nakit akış sunumu")

q("Bir kiracının kullanım hakkı varlığı ve kira yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "İkisinin defter değeri zamanla farklılaşır; amortisman ve faiz farklı hızda işler",
  ["İkisinin defter değeri her hâlde ve her dönemde birbirine eşit kalmak zorunda bulunmaktadır",
   "Kullanım hakkı varlığı hiç amortismana tabi tutulmaz; yükümlülükle eşit tutulmak zorundadır",
   "Kira yükümlülüğü hiçbir hâlde azalmaz; ilk ölçüm tutarı süre boyunca sabit kalmaktadır",
   "İkisi arasındaki ilişki TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "Kullanım hakkı varlığı genellikle doğrusal amortismana tabidir; kira yükümlülüğü ise etkin faiz yöntemiyle azalır. Farklı hızda ilerlediklerinden başlangıçta eşit (ya da yakın) olsalar bile defter değerleri zamanla birbirinden ayrışır.",
  "TFRS 16 - varlık ve yükümlülüğün ayrışması")

q("Aşağıdaki ifadelerden hangileri kiracının sonraki ölçümü bakımından doğrudur?\n\nI. Kullanım hakkı varlığı amortismana tabi tutulur\n\nII. Kira yükümlülüğüne faiz işletilir\n\nIII. Amortisman ve faiz tek bir kira gideri olarak birlikte sunulur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kullanım hakkı varlığı amortismana tabi tutulur (I) ve kira yükümlülüğüne faiz işletilir (II). Ancak kiracı amortisman gideri ile faiz giderini AYRI olarak sunar; tek bir kira gideri olarak birleştirmez. Bu nedenle III yanlıştır.",
  "TFRS 16 - sonraki ölçüm")

q("Aşağıdaki ifadelerden hangileri TFRS 16 bakımından doğrudur?\n\nI. Mülkiyet devri varsa amortisman süresi dayanak varlığın faydalı ömrüdür\n\nII. Mülkiyet devri yoksa kiralama süresi ile faydalı ömürden UZUN olanı esas alınır\n\nIII. Kullanım hakkı varlığında değer düşüklüğü için TMS 36 uygulanır",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Mülkiyet devri veya kullanılacağı makul ölçüde kesin satın alma opsiyonu varsa dayanak varlığın faydalı ömrü esas alınır (I) ve değer düşüklüğünde TMS 36 uygulanır (III). Mülkiyet devri yoksa kiralama süresi ile faydalı ömürden KISA olanı esas alınır, uzun olanı değil; bu nedenle II yanlıştır.",
  "TFRS 16 - sonraki ölçüm")

# ── D. Kiraya veren ve satış-geri kiralama (16) ────────────────────────────
q("Kiraya verenin kiralama sınıflandırması bakımından aşağıdakilerden hangisi doğrudur?",
  "Mülkiyetten kaynaklanan risk ve getirilerin tamamına yakını devrediliyorsa finansal kiralamadır",
  ["Sözleşmede 'finansal kiralama' ifadesinin geçmesi hâlinde finansal kiralama sayılmak zorundadır",
   "Kiralama süresi bir yılı aşan her sözleşme her hâlde finansal kiralama sayılmak zorundadır",
   "Kira bedeli yüksek olan her sözleşme her hâlde finansal kiralama olarak sınıflandırılmaktadır",
   "Kiraya verenin sınıflandırması TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: bir kiralama, dayanak varlığın mülkiyetinden kaynaklanan tüm risk ve getirilerin önemli ölçüde devredilmesi durumunda finansal kiralama olarak sınıflandırılır. Devredilmiyorsa faaliyet kiralamasıdır. Sınıflandırma sözleşmenin özüne bakılarak yapılır.",
  "TFRS 16 - kiraya verenin sınıflandırması")

q("Aşağıdakilerden hangisi kiraya veren açısından finansal kiralama göstergesidir?",
  "Kiralama süresi sonunda mülkiyetin kiracıya devredilmesi",
  ["Kiralama süresinin dayanak varlığın ekonomik ömrünün küçük bir bölümünü kapsaması durumu",
   "Kira ödemelerinin bugünkü değerinin varlığın gerçeğe uygun değerinin çok altında kalması",
   "Dayanak varlığın kiralama sonunda kiraya verene iade edilip başkasına kiralanabilmesi durumu",
   "Dayanak varlığın genel nitelikli olması ve başka kullanıcılarca da kullanılabilir olması durumu"],
  "TFRS 16: finansal kiralama göstergeleri arasında kiralama süresi sonunda mülkiyetin kiracıya geçmesi, cazip fiyatlı satın alma opsiyonu, sürenin ekonomik ömrün büyük bölümünü kapsaması, kira ödemelerinin bugünkü değerinin gerçeğe uygun değerin tamamına yakınına eşit olması ve varlığın özel nitelikli olması sayılır.",
  "TFRS 16 - finansal kiralama göstergeleri")

q("Kiraya verenin finansal kiralamada yapacağı muhasebeleştirme bakımından aşağıdakilerden hangisi doğrudur?",
  "Dayanak varlığı bilanço dışı bırakıp kiralamadaki net yatırımı tutarında alacak muhasebeleştirir",
  ["Dayanak varlığı bilançosunda tutmaya devam eder ve amortismana tabi tutmak zorunda kalınır",
   "Hiçbir kayıt yapmaz; finansal kiralama yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Aldığı kira bedellerini her hâlde doğrusal olarak gelir yazmak zorunda tutulmaktadır",
   "Dayanak varlığı gerçeğe uygun değeriyle yeniden ölçüp bilançosunda tutmak zorundadır"],
  "TFRS 16: kiraya veren, finansal kiralama kapsamındaki varlıkları finansal durum tablosunda muhasebeleştirir ve bunları kiralamadaki net yatırıma eşit bir tutarda alacak olarak sunar. Dayanak varlık bilanço dışı bırakılır.",
  "TFRS 16 - kiraya veren finansal kiralama")

q("Kiraya verenin faaliyet kiralamasında yapacağı muhasebeleştirme bakımından aşağıdakilerden hangisi doğrudur?",
  "Dayanak varlığı bilançosunda tutmaya devam eder ve kira gelirini doğrusal olarak gelir yazar",
  ["Dayanak varlığı bilanço dışı bırakıp alacak muhasebeleştirmek zorunda tutulmaktadır",
   "Hiçbir kayıt yapmaz; faaliyet kiralaması yalnızca dipnotlarda açıklanmakla yetinilir",
   "Kira gelirinin tamamını sözleşme başlangıcında peşin olarak gelir yazmak zorunda kalır",
   "Dayanak varlık için hiçbir hâlde amortisman ayrılmaz; varlık itfa edilmeden bırakılmaktadır"],
  "TFRS 16: kiraya veren, faaliyet kiralamalarına ilişkin kira ödemelerini doğrusal yöntemle veya başka bir sistematik esasa göre gelir olarak muhasebeleştirir. Dayanak varlık bilançoda kalır ve amortismana tabi tutulur.",
  "TFRS 16 - kiraya veren faaliyet kiralaması")

q("Kiraya verenin faaliyet kiralamasındaki dayanak varlığın amortismanı bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya veren, benzer varlıklara ilişkin olağan amortisman politikasını uygular",
  ["Faaliyet kiralamasındaki varlıklar için hiçbir hâlde amortisman ayrılmamak zorunda kalınır",
   "Amortisman kiracı tarafından ayrılır; kiraya veren hiçbir hâlde amortisman kaydetmemektedir",
   "Amortisman her hâlde kiralama süresi üzerinden ayrılmak zorunda olup faydalı ömür dikkate alınmaz",
   "Bu husus TFRS 16'da düzenlenmemiş olup kiraya verenin serbest takdirine bırakılmıştır"],
  "TFRS 16: kiraya veren, faaliyet kiralamasına konu amortismana tabi dayanak varlıkların amortisman politikasını, benzer varlıklara ilişkin olağan amortisman politikasıyla tutarlı biçimde belirler.",
  "TFRS 16 - faaliyet kiralamasında amortisman")

q("Satış ve geri kiralama işlemlerinde devrin satış sayılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Devrin satış olup olmadığı TFRS 15'teki hükümlere göre belirlenir",
  ["Devir her hâlde satış sayılır; TFRS 15'teki ölçütlere başvurulmasına gerek bulunmamaktadır",
   "Devir hiçbir hâlde satış sayılmaz; işlem her zaman finansman işlemi olarak ele alınmaktadır",
   "Devrin satış sayılıp sayılmadığı işletmenin serbest takdirine bırakılmış bir husustur",
   "Satış ve geri kiralama işlemleri TFRS 16 kapsamı dışında olup düzenlenmemiş bulunmaktadır"],
  "TFRS 16: işletme, varlık devrinin satış olarak muhasebeleştirilip muhasebeleştirilmeyeceğini belirlemek için TFRS 15'teki (bir edim yükümlülüğünün ne zaman yerine getirildiğine ilişkin) hükümleri uygular.",
  "TFRS 16 - satış ve geri kiralamada satış ölçütü")

q("Devrin satış olarak muhasebeleştirildiği satış ve geri kiralama işlemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Satıcı-kiracı, elde tuttuğu kullanım hakkıyla ilgili kazancı değil, yalnızca devredilen haklara ilişkin kazancı muhasebeleştirir",
  ["Satıcı-kiracı satıştan doğan kazancın tamamını her hâlde derhâl kâr veya zarara yansıtır",
   "Satıcı-kiracı satıştan doğan kazancı hiçbir hâlde muhasebeleştiremez; kazanç yok sayılmaktadır",
   "Satıcı-kiracı satıştan doğan kazancın tamamını her hâlde doğrudan özkaynaklara aktarmaktadır",
   "Bu husus TFRS 16'da düzenlenmemiş olup satıcı-kiracının serbest takdirine bırakılmıştır"],
  "TFRS 16: devir satış olarak muhasebeleştiriliyorsa satıcı-kiracı, kullanım hakkı varlığını dayanak varlığın önceki defter değerinin elde tutulan kullanım hakkıyla ilgili kısmı üzerinden ölçer. Bu nedenle yalnızca alıcı-kiraya verene devredilen haklara ilişkin kazanç veya kayıp tutarını muhasebeleştirir.",
  "TFRS 16 - satış ve geri kiralamada kazanç")

q("Devrin satış olarak muhasebeleştirilmediği satış ve geri kiralama işlemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Satıcı-kiracı varlığı bilançosunda tutmaya devam eder ve devir bedeli kadar finansal borç muhasebeleştirir",
  ["Satıcı-kiracı varlığı her hâlde bilanço dışı bırakmak zorunda olup borç kaydetmemektedir",
   "Satıcı-kiracı satıştan doğan kazancın tamamını her hâlde derhâl kâr veya zarara yansıtır",
   "Satıcı-kiracı hiçbir kayıt yapmaz; işlem yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Bu husus TFRS 16'da düzenlenmemiş olup satıcı-kiracının takdirine bırakılmış bulunmaktadır"],
  "TFRS 16: varlık devri satış olarak muhasebeleştirilmiyorsa satıcı-kiracı devredilen varlığı muhasebeleştirmeye devam eder ve devirden elde edilen tutara eşit bir finansal borç muhasebeleştirir. Bu bir finansman işlemidir.",
  "TFRS 16 - satış sayılmayan geri kiralama")

q("Kiraya verenin faaliyet kiralamasında katlandığı başlangıçtaki doğrudan maliyetler bakımından aşağıdakilerden hangisi doğrudur?",
  "Dayanak varlığın defter değerine eklenir ve kira geliriyle aynı esasa göre gider yazılır",
  ["Bu maliyetler her hâlde ve derhâl tek seferde gider yazılmak zorunda tutulmaktadır",
   "Bu maliyetler her hâlde kiracı tarafından karşılanmak zorunda olup kiraya vereni ilgilendirmez",
   "Bu maliyetler hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Bu husus TFRS 16'da düzenlenmemiş olup kiraya verenin takdirine bırakılmış bulunmaktadır"],
  "TFRS 16: kiraya veren, faaliyet kiralamasının müzakere edilmesi ve düzenlenmesinde katlandığı başlangıçtaki doğrudan maliyetleri dayanak varlığın defter değerine ekler ve bu maliyetleri kira geliri ile aynı esasa göre kiralama süresi boyunca gider olarak muhasebeleştirir.",
  "TFRS 16 - kiraya verende doğrudan maliyetler")

q("Bir işletme, sahibi olduğu binayı bir bankaya satıp aynı binayı uzun süreli olarak geri kiralamıştır ve devir TFRS 15 uyarınca satış sayılmıştır. TFRS 16 bakımından aşağıdakilerden hangisi doğrudur?",
  "Elde tutulan kullanım hakkına düşen kazanç muhasebeleştirilmez; yalnızca devredilen haklara ilişkin kazanç kaydedilir",
  ["Satıştan doğan kazancın tamamı derhâl kâr veya zarara yansıtılmak zorunda tutulmaktadır",
   "Satıştan doğan kazanç hiçbir hâlde muhasebeleştirilemez; kazanç tümüyle yok sayılmaktadır",
   "Bina her hâlde bilançoda tutulmaya devam edilir; satış hiçbir biçimde kayda alınmamaktadır",
   "Satıştan doğan kazancın tamamı her hâlde doğrudan özkaynaklara aktarılmak zorunda kalınır"],
  "TFRS 16: satış sayılan geri kiralamada satıcı-kiracı kullanım hakkı varlığını, dayanak varlığın önceki defter değerinin ELDE TUTULAN kullanım hakkına ilişkin kısmı üzerinden ölçer. Bu nedenle kazancın yalnızca alıcı-kiraya verene DEVREDİLEN haklara düşen kısmı muhasebeleştirilir.",
  "TFRS 16 - satış ve geri kiralama (senaryo)")

q("Aşağıdakilerden hangileri kiraya veren açısından finansal kiralama göstergesidir?\n\nI. Kiralama süresi sonunda mülkiyetin kiracıya devredilmesi\n\nII. Kiralama süresinin dayanak varlığın ekonomik ömrünün büyük bölümünü kapsaması\n\nIII. Dayanak varlığın yalnızca kiracı tarafından kullanılabilecek özel nitelikte olması",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TFRS 16 üçünü de finansal kiralama göstergesi olarak sayar: sürenin sonunda mülkiyetin devri (I), kiralama süresinin ekonomik ömrün büyük bölümünü kapsaması (II) ve dayanak varlığın büyük değişiklikler olmadan yalnızca kiracı tarafından kullanılabilecek özel nitelikte olması (III).",
  "TFRS 16 - finansal kiralama göstergeleri")

q("Aşağıdaki ifadelerden hangileri kiraya veren muhasebesi bakımından doğrudur?\n\nI. Finansal kiralamada net kiralama yatırımı tutarında alacak muhasebeleştirilir\n\nII. Faaliyet kiralamasında kira geliri doğrusal olarak yazılır\n\nIII. Faaliyet kiralamasında dayanak varlık bilanço dışı bırakılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Finansal kiralamada net kiralama yatırımı tutarında alacak kaydedilir (I) ve faaliyet kiralamasında kira geliri doğrusal olarak yazılır (II). Faaliyet kiralamasında dayanak varlık kiraya verenin bilançosunda KALIR ve amortismana tabi tutulur; bu nedenle III yanlıştır.",
  "TFRS 16 - kiraya veren muhasebesi")

q("Kiracının yapacağı açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Amortisman, faiz gideri, muafiyet kapsamındaki kiralama giderleri ve toplam nakit çıkışı açıklanır",
  ["Kiralamalar hakkında hiçbir açıklama yapılmaz; yalnızca tutarlar bilançoda gösterilmektedir",
   "Yalnızca toplam kira gideri açıklanır; hiçbir ayrıntılı bilgi verilmesine gerek bulunmamaktadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca finansal kiralama yapan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TFRS 16: kiracı, kullanım hakkı varlıklarına ilişkin amortisman giderini (dayanak varlık sınıfı bazında), kira yükümlülüklerine ilişkin faiz giderini, kısa vadeli ve düşük değerli varlık kiralamalarına ilişkin giderleri, değişken kira ödemelerine ilişkin giderleri ve kiralamalara ilişkin toplam nakit çıkışını açıklar.",
  "TFRS 16 - kiracı açıklamaları")

q("Kiralama değişikliği (kiralamada yapılan bir değişiklik) bakımından aşağıdakilerden hangisi doğrudur?",
  "Kapsam genişliyor ve bedel tek başına fiyatla orantılı artıyorsa değişiklik ayrı bir kiralama olarak muhasebeleştirilir",
  ["Her kiralama değişikliği her hâlde ayrı bir kiralama olarak muhasebeleştirilmek zorundadır",
   "Kiralama değişiklikleri hiçbir hâlde muhasebeleştirilmez; mevcut kayıtlar aynen sürdürülür",
   "Her kiralama değişikliği her hâlde önceki dönem hatası sayılıp geriye dönük düzeltilmektedir",
   "Kiralama değişiklikleri TFRS 16'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 16: kiracı, (a) değişiklik bir veya daha fazla dayanak varlığın kullanım hakkını ekleyerek kiralamanın kapsamını genişletiyorsa ve (b) kiralama bedeli, kapsam artışının tek başına fiyatına karşılık gelen tutarda artıyorsa, kiralama değişikliğini AYRI bir kiralama olarak muhasebeleştirir.",
  "TFRS 16 - kiralama değişikliği")

q("Bir kiracı, kiraladığı mağazanın kirası olarak aylık sabit tutar yerine yalnızca aylık satış hasılatının belirli bir yüzdesini ödemektedir. TFRS 16 bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu ödemeler endekse veya orana bağlı olmadığından yükümlülüğe dâhil edilmez; gerçekleştiğinde gider yazılır",
  ["Bu ödemeler her hâlde kira yükümlülüğünün ölçümüne dâhil edilmek zorunda tutulmaktadır",
   "Bu ödemeler her hâlde kullanım hakkı varlığının maliyetine eklenmek zorunda bulunmaktadır",
   "Bu ödemeler hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Bu ödemeler her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemleri ifade eder"],
  "TFRS 16: satış hasılatına bağlı kira ödemeleri, bir endekse veya orana bağlı OLMAYAN değişken kira ödemesidir. Kira yükümlülüğünün ölçümüne dâhil edilmez; bunları tetikleyen olayın gerçekleştiği dönemde kâr veya zararda muhasebeleştirilir.",
  "TFRS 16 - hasılata bağlı kira (senaryo)")

q("Bir işletme bir depoyu 4 yıllığına kiralamış; sözleşmede 3 yıl daha uzatma opsiyonu bulunmakta ve işletme bu opsiyonu kullanacağından makul ölçüde emin bulunmaktadır. TFRS 16 bakımından kiralama süresi kaç yıldır?",
  "7 yıl",
  ["4 yıl; yalnızca iptal edilemeyen süre dikkate alınır, uzatma opsiyonları hiç eklenmemektedir",
   "3 yıl; yalnızca uzatma opsiyonuna ilişkin dönem kiralama süresi olarak kabul edilmektedir",
   "1 yıl; kiralama süresi her hâlde on iki ay olarak kabul edilmek zorunda tutulmaktadır",
   "4 yıl; uzatma opsiyonu ancak fiilen kullanıldığı tarihte süreye eklenebilmektedir"],
  "TFRS 16: kiralama süresi, iptal edilemeyen süre (4 yıl) ile kiracının kullanacağından makul ölçüde emin olduğu uzatma opsiyonuna ilişkin dönemlerin (3 yıl) toplamıdır: 4 + 3 = 7 yıl. Opsiyonun fiilen kullanılmasını beklemeye gerek yoktur; değerlendirme başlangıç tarihinde yapılır.",
  "TFRS 16 - kiralama süresi (senaryo)")

q("TFRS 16'nın getirdiği temel değişikliğin finansal tablolara etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Eskiden bilanço dışı kalan faaliyet kiralamaları kiracının bilançosuna girdiğinden varlık ve yükümlülükler artar",
  ["Kiracının varlık ve yükümlülüklerinde hiçbir değişiklik meydana gelmemektedir",
   "Kiracının varlık ve yükümlülükleri azalır; kiralamalar bilanço dışına çıkarılmaktadır",
   "Yalnızca kiraya verenin bilançosu etkilenir; kiracının tabloları hiç değişmemektedir",
   "Bu etki TFRS 16'da hiçbir biçimde ele alınmamış olup uygulamada ortaya çıkmamaktadır"],
  "TFRS 16 ile kiracıdaki finansal-faaliyet kiralaması ayrımı kaldırılmıştır. Eskiden bilanço dışında kalıp yalnızca gider yazılan faaliyet kiralamaları artık kullanım hakkı varlığı ve kira yükümlülüğü olarak bilançoya girer; bu da kiracının varlık ve yükümlülük toplamlarını artırır.",
  "TFRS 16 - bilançoya etkisi")

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
                       "styleRef": "SGS Muhasebe Standartları (TFRS 16; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
