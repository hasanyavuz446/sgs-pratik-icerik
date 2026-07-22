# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 20 Devlet Teşvikleri — 60 soru.
Kaynak: KGK TMS 20 (Devlet Teşviklerinin Muhasebeleştirilmesi ve Devlet
Yardımlarının Açıklanması). Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-9 soru, "hepsi" ~2 (%22-25)."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_20_devlet_tesvik"
PREFIX, SEED = "std-tms20-gen", 20260419
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_20_devlet_tesvik.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanımlar ve kapsam (14) ─────────────────────────────────────────────
q("TMS 20'ye göre devlet teşvikleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirli koşulların yerine getirilmesi karşılığında işletmeye kaynak aktarımı biçimindeki devlet yardımlarıdır",
  ["Devletin işletmelere karşılıksız ve hiçbir koşul aranmaksızın yaptığı bağışları ifade etmektedir",
   "İşletmelerin devlete ödediği vergi ve benzeri mali yükümlülükleri ifade eden bir kavramdır",
   "Devletin işletmelerden satın aldığı mal ve hizmetlerin bedelini ifade eden bir kavram niteliğindedir",
   "Devlet teşviki kavramı TMS 20'de tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 20: devlet teşvikleri, işletmenin faaliyet konuları ile ilgili belirli koşulların geçmişte veya gelecekte yerine getirilmesi karşılığında işletmeye kaynak aktarımı biçimindeki devlet yardımlarıdır.",
  "TMS 20 - devlet teşviki tanımı")

q("TMS 20'ye göre devlet yardımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirli koşulları sağlayan işletmelere ekonomik fayda sağlamak üzere devlet tarafından yapılan eylemlerdir",
  ["Yalnızca nakit olarak yapılan ödemeleri ifade eden dar kapsamlı bir kavramı karşılamaktadır",
   "Yalnızca vergi indirimlerini ifade eden ve başka hiçbir unsuru kapsamayan bir kavramdır",
   "İşletmelerin devlete yaptığı bağış ve yardımları ifade eden bir kavram niteliğinde bulunur",
   "Devlet yardımı kavramı TMS 20'de tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TMS 20: devlet yardımı, belirli kriterleri karşılayan bir işletme veya işletme grubuna ekonomik fayda sağlamak üzere devlet tarafından yapılan eylemlerdir. Devlet teşvikleri, devlet yardımlarının bir alt kümesidir.",
  "TMS 20 - devlet yardımı tanımı")

q("TMS 20'de 'devlet' kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Devleti, devlet organlarını ve yerel, ulusal ya da uluslararası benzer kuruluşları ifade eder",
  ["Yalnızca merkezi hükûmeti ifade eder; yerel yönetimler hiçbir hâlde kapsama girmemektedir",
   "Yalnızca yerel yönetimleri ifade eder; merkezi hükûmet kapsam dışında bırakılmaktadır",
   "Yalnızca uluslararası kuruluşları ifade eder; ulusal organlar kapsama alınmamaktadır",
   "'Devlet' kavramı TMS 20'de tanımlanmamış olup uygulamada dikkate alınmayan bir husustur"],
  "TMS 20: 'devlet' terimi; devleti, devlet organlarını ve yerel, ulusal veya uluslararası olmasına bakılmaksızın benzer kuruluşları ifade eder.",
  "TMS 20 - devlet kavramı")

q("Varlıklara ilişkin devlet teşvikleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin duran varlık satın alması, inşa etmesi veya edinmesi asli koşulu bulunan teşviklerdir",
  ["İşletmenin personel istihdam etmesi koşuluna bağlanan teşvikleri ifade eden bir türü karşılar",
   "İşletmenin belirli tutarda hasılat elde etmesi koşuluna bağlanan teşvikleri ifade etmektedir",
   "Hiçbir koşula bağlı olmayan ve karşılıksız verilen teşvikleri ifade eden bir türü karşılar",
   "Varlıklara ilişkin teşvikler TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 20: varlıklara ilişkin devlet teşvikleri, asli koşulu teşvike hak kazanan işletmenin duran varlık satın alması, inşa etmesi veya edinmesi olan teşviklerdir.",
  "TMS 20 - varlıklara ilişkin teşvikler")

q("Gelire ilişkin devlet teşvikleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlıklara ilişkin teşvikler dışında kalan devlet teşvikleridir",
  ["İşletmenin duran varlık edinmesi koşuluna bağlanan teşvikleri ifade eden bir türü karşılar",
   "Yalnızca işletmenin hasılatına doğrudan eklenen teşvikleri ifade eden dar bir kavramdır",
   "Hiçbir koşula bağlı olmayan ve karşılıksız verilen teşvikleri ifade eden bir türü karşılar",
   "Gelire ilişkin teşvikler TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 20: gelire ilişkin devlet teşvikleri, varlıklara ilişkin devlet teşvikleri dışında kalan devlet teşvikleridir. Tanım artık (kalıntı) yöntemle yapılmıştır.",
  "TMS 20 - gelire ilişkin teşvikler")

q("Devlet teşviklerinin muhasebeleştirilme koşulları bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin teşvik koşullarını yerine getireceğine ve teşvikin elde edileceğine dair makul güvence bulunmalıdır",
  ["Teşvikin yalnızca ilan edilmiş olması yeterli olup başka hiçbir koşul aranmamaktadır",
   "Teşvikin yalnızca nakden tahsil edilmiş olması gerekir; makul güvence yeterli sayılmamaktadır",
   "Teşvikler hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Muhasebeleştirme koşulları TMS 20'de düzenlenmemiş olup serbest bırakılmış bir husustur"],
  "TMS 20: devlet teşvikleri, (a) işletmenin teşvikin öngördüğü koşulları yerine getireceğine ve (b) teşvikin elde edileceğine dair makul bir güvence oluşmadan muhasebeleştirilmez.",
  "TMS 20 - muhasebeleştirme koşulları")

q("Devlet teşvikinin tahsil edilmiş olması bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvikin tahsil edilmiş olması, koşulların yerine getirileceğine dair kesin kanıt oluşturmaz",
  ["Teşvikin tahsil edilmesi hâlinde koşulların yerine getirildiği her hâlde kesinleşmiş sayılır",
   "Teşvik tahsil edilmedikçe hiçbir hâlde muhasebeleştirilemez; makul güvence yeterli değildir",
   "Teşvikin tahsil edilmesi hâlinde tutarın tamamı her hâlde derhâl gelir yazılmak zorundadır",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 20: bir teşvikin elde edilmiş olması, teşvike bağlı koşulların yerine getirildiği veya getirileceği hususunda kesin bir kanıt oluşturmaz. Teşvikin tahsil şekli, uygulanacak muhasebe yöntemini etkilemez.",
  "TMS 20 - tahsilin anlamı")

q("Parasal olmayan devlet teşvikleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvik ve varlık gerçeğe uygun değeriyle muhasebeleştirilebilir; nominal tutarla kaydedilmesi de mümkündür",
  ["Parasal olmayan teşvikler hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmaktadır",
   "Parasal olmayan teşvikler her hâlde piyasa değerinin iki katı üzerinden kaydedilmek zorundadır",
   "Parasal olmayan teşvikler her hâlde sıfır değerle kaydedilir; bedelsiz edinim söz konusudur",
   "Parasal olmayan teşviklerin ele alınışı TMS 20'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 20: arazi veya diğer kaynaklar gibi parasal olmayan devlet teşviklerinde, teşvik ve varlığın gerçeğe uygun değeri belirlenip her ikisinin de bu değerle muhasebeleştirilmesi olağan bir uygulamadır. Alternatif olarak varlık ve teşvik nominal tutar üzerinden kaydedilebilir.",
  "TMS 20 - parasal olmayan teşvikler")

q("Aşağıdakilerden hangisi TMS 20'nin kapsamı DIŞINDADIR?",
  "Vergiye esas kârın belirlenmesinde sağlanan devlet yardımları",
  ["İşletmenin duran varlık edinmesi koşuluna bağlanan ve nakden ödenen teşvik niteliğindeki tutarlar",
   "İşletmeye bedelsiz olarak arazi devredilmesi biçimindeki parasal olmayan teşvik niteliğinde yardımlar",
   "İşletmenin belirli bir bölgede personel istihdam etmesi koşuluna bağlanan teşvik niteliğinde tutarlar",
   "Geçmişte katlanılan giderleri karşılamak amacıyla işletmeye ödenen teşvik niteliğindeki tutarların tümü"],
  "TMS 20: bu Standart, vergilendirilebilir kârın belirlenmesinde sağlanan yardımlar ile vergi yükümlülüğü esas alınarak belirlenen yardımları (vergi tatilleri, yatırım indirimleri, hızlandırılmış amortisman, indirimli vergi oranları gibi) KAPSAMAZ. Bunlar TMS 12 kapsamındadır.",
  "TMS 20 - kapsam dışı")

q("Devlet teşviklerinin muhasebeleştirilmesindeki temel yaklaşım bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelir yaklaşımı benimsenmiştir; teşvikler ilgili maliyetlerle eşleştirilerek kâr veya zararda muhasebeleştirilir",
  ["Sermaye yaklaşımı benimsenmiştir; teşvikler her hâlde doğrudan özkaynağa kaydedilmek zorundadır",
   "Teşvikler hiçbir hâlde kâr veya zarara yansıtılamaz; tümü yabancı kaynakta bırakılmaktadır",
   "Teşvikler her hâlde tahsil edildikleri dönemde tümüyle gelir yazılmak zorunda tutulmaktadır",
   "Temel yaklaşım TMS 20'de belirlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 20: devlet teşvikleri, karşılanması amaçlanan maliyetlerle ilişkilendirilen dönemler boyunca sistematik biçimde kâr veya zarara yansıtılır (gelir yaklaşımı). Teşvikler doğrudan özkaynağa kaydedilmez.",
  "TMS 20 - gelir yaklaşımı")

q("Devlet teşviklerinin doğrudan özkaynağa kaydedilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvikler doğrudan özkaynağa kaydedilmez; kâr veya zararda muhasebeleştirilir",
  ["Teşvikler her hâlde ve istisnasız doğrudan özkaynağa kaydedilmek zorunda tutulmaktadır",
   "Teşviklerin özkaynağa kaydedilip kaydedilmeyeceği işletmenin serbest takdirine bırakılmıştır",
   "Teşvikler yalnızca büyük işletmelerce özkaynağa kaydedilir; küçükler gelir yazmak zorundadır",
   "Bu husus TMS 20'de düzenlenmemiş bir konu niteliğinde olup uygulamada belirsiz kalmaktadır"],
  "TMS 20: gelir yaklaşımı benimsenmiştir. Devlet teşvikleri, işletmenin ortakları dışındaki bir kaynaktan elde edildiğinden özkaynağa doğrudan kaydedilmez; teşvikin karşılamayı amaçladığı maliyetlerle eşleştirilerek kâr veya zararda muhasebeleştirilir.",
  "TMS 20 - özkaynağa kaydedilmeme")

q("Devlet teşviklerinin kâr veya zarara yansıtılma dönemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Karşılanması amaçlanan maliyetlerin gider olarak muhasebeleştirildiği dönemler boyunca yansıtılır",
  ["Her hâlde teşvikin tahsil edildiği dönemde tümüyle gelir yazılmak zorunda tutulmaktadır",
   "Her hâlde teşvikin ilan edildiği dönemde tümüyle gelir yazılmak zorunda bulunmaktadır",
   "Her hâlde işletmenin faaliyetinin son yılında tümüyle gelir yazılmak zorunda kalınmaktadır",
   "Teşviklerin yansıtılma dönemi TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 20: devlet teşvikleri, teşviklerle karşılanması amaçlanan maliyetlerin gider olarak muhasebeleştirildiği dönemler boyunca sistematik biçimde kâr veya zarara yansıtılır. Tahsil esasına göre gelir yazma, tahakkuk esasıyla bağdaşmaz.",
  "TMS 20 - eşleştirme")

q("Aşağıdakilerden hangileri TMS 20'ye göre devlet teşvikinin muhasebeleştirilmesi için aranır?\n\nI. İşletmenin teşvik koşullarını yerine getireceğine dair makul güvence\n\nII. Teşvikin nakden tahsil edilmiş olması\n\nIII. Teşvik tutarının peşinen özkaynağa kaydedilmiş olması",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Koşulların yerine getirileceğine dair makul güvence aranır (I). Fiilî tahsil muhasebeleştirme koşulu değildir (II) ve teşvik tutarı peşinen özkaynağa kaydedilmez (III). Yalnız I doğrudur.",
  "TMS 20 - muhasebeleştirme koşulları")

q("Aşağıdaki ifadelerden hangileri TMS 20 bakımından doğrudur?\n\nI. Teşviklerde gelir yaklaşımı benimsenmiştir\n\nII. Teşvikler doğrudan özkaynağa kaydedilmez\n\nIII. Vergi tatilleri ve yatırım indirimleri TMS 20 kapsamındadır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 20 gelir yaklaşımını benimser (I) ve teşvikler doğrudan özkaynağa kaydedilmez (II). Vergilendirilebilir kârın belirlenmesinde sağlanan yardımlar (vergi tatilleri, yatırım indirimleri, hızlandırılmış amortisman) ise TMS 20 kapsamı DIŞINDADIR; bu nedenle III yanlıştır.",
  "TMS 20 - kapsam ve yaklaşım")

# ── B. Varlıklara ilişkin teşviklerin sunumu (14) ──────────────────────────
q("Varlıklara ilişkin devlet teşviklerinin finansal durum tablosunda sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Ertelenmiş gelir olarak sunulabilir veya varlığın defter değerinden indirilebilir",
  ["Yalnızca ertelenmiş gelir olarak sunulabilir; varlıktan indirim yöntemi kabul edilmemektedir",
   "Yalnızca varlığın defter değerinden indirilebilir; ertelenmiş gelir yöntemi yasaklanmıştır",
   "Her hâlde doğrudan özkaynakta gösterilmek zorunda olan bir kalemi ifade etmektedir",
   "Varlıklara ilişkin teşviklerin sunumu TMS 20'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 20: parasal olmayanlar dâhil varlıklara ilişkin devlet teşvikleri, finansal durum tablosunda ya ertelenmiş gelir olarak ya da varlığın defter değerinden indirilerek gösterilir. İki yöntem de kabul edilir.",
  "TMS 20 - varlık teşviklerinde iki yöntem")

q("Varlıklara ilişkin teşvikin ertelenmiş gelir yöntemiyle sunulması bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvik, varlığın faydalı ömrü boyunca sistematik biçimde kâr veya zarara yansıtılır",
  ["Teşvik tahsil edildiği dönemde tümüyle gelir yazılmak zorunda olup yayılmamaktadır",
   "Teşvik hiçbir hâlde kâr veya zarara yansıtılmaz; süresiz olarak yabancı kaynakta kalmaktadır",
   "Teşvik her hâlde doğrudan özkaynağa aktarılmak zorunda olan bir kalemi ifade etmektedir",
   "Bu yöntemin işleyişi TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 20: ertelenmiş gelir yönteminde teşvik, amortismana tabi varlığın faydalı ömrü boyunca sistematik ve makul bir biçimde kâr veya zarara yansıtılır.",
  "TMS 20 - ertelenmiş gelir yöntemi")

q("Varlıklara ilişkin teşvikin varlığın defter değerinden indirilmesi yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvik, varlığın faydalı ömrü boyunca azaltılmış amortisman gideri yoluyla kâr veya zarara yansır",
  ["Teşvik bu yöntemde hiçbir hâlde kâr veya zarara yansımaz; kalıcı olarak varlıktan düşülür",
   "Teşvik bu yöntemde tahsil edildiği dönemde tümüyle gelir yazılmak zorunda tutulmaktadır",
   "Teşvik bu yöntemde her hâlde doğrudan özkaynağa aktarılmak zorunda bulunmaktadır",
   "Bu yöntemin işleyişi TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 20: teşvikin varlığın defter değerinden indirildiği yöntemde teşvik, amortismana tabi varlığın ömrü boyunca AZALTILMIŞ amortisman gideri yoluyla kâr veya zarara yansıtılmış olur. İki yöntem de aynı net etkiyi doğurur.",
  "TMS 20 - defter değerinden indirim yöntemi")

q("Varlıklara ilişkin teşviklerde iki sunum yönteminin kâr üzerindeki etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "İki yöntem de dönem kârı üzerinde aynı net etkiyi doğurur; yalnızca sunum farklıdır",
  ["Ertelenmiş gelir yöntemi her hâlde daha yüksek dönem kârı doğuran bir yöntemi ifade eder",
   "Defter değerinden indirim yöntemi her hâlde daha yüksek dönem kârı doğurmaktadır",
   "İki yöntem arasında hiçbir ilişki bulunmayıp sonuçları tümüyle bağımsız kalmaktadır",
   "Yöntemlerin kâr etkisi TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "İki yöntem de aynı net kâr etkisini doğurur. Ertelenmiş gelirde tam amortisman gideri + teşvik geliri; defter değerinden indirimde ise azaltılmış amortisman gideri kaydedilir. Net etki eşittir; fark yalnızca kalemlerin brüt/net sunumundadır.",
  "TMS 20 - yöntemlerin eşdeğerliği")

tes, mal20, om20 = 300_000, 900_000, 10
yil_tes = tes / om20
q(f"Bir işletme, {tr(mal20)} TL maliyetli ve {om20} yıl faydalı ömürlü bir makine için {tr(tes)} TL devlet teşviki almıştır. Teşvik ertelenmiş gelir olarak sunulmaktadır. Kalıntı değer sıfır olduğunda ilk yıl kâr veya zarara yansıtılacak teşvik geliri kaç TL'dir?",
  f"{tr(yil_tes)} TL",
  [f"{tr(tes)} TL", f"{tr(mal20 / om20)} TL", f"{tr((mal20 - tes) / om20)} TL", f"{tr(tes / 2)} TL"],
  f"Ertelenmiş gelir yönteminde teşvik, varlığın faydalı ömrü boyunca sistematik olarak gelir yazılır: {tr(tes)} ÷ {om20} = {tr(yil_tes)} TL. Teşvik tahsil edildiği dönemde tümüyle gelir yazılmaz.",
  "TMS 20 - ertelenmiş gelir hesabı")

net_mal = mal20 - tes
yil_amort_net = net_mal / om20
q(f"Bir işletme, {tr(mal20)} TL maliyetli ve {om20} yıl faydalı ömürlü bir makine için {tr(tes)} TL devlet teşviki almıştır. Teşvik varlığın defter değerinden indirilerek sunulmaktadır. Kalıntı değer sıfır olduğunda yıllık amortisman gideri kaç TL'dir?",
  f"{tr(yil_amort_net)} TL",
  [f"{tr(mal20 / om20)} TL", f"{tr((mal20 + tes) / om20)} TL", f"{tr(tes / om20)} TL", f"{tr(net_mal)} TL"],
  f"Teşvik defter değerinden indirildiğinde varlığın kayıtlı değeri = {tr(mal20)} − {tr(tes)} = {tr(net_mal)} TL olur. Yıllık amortisman = {tr(net_mal)} ÷ {om20} = {tr(yil_amort_net)} TL. Teşvik böylece azaltılmış amortisman yoluyla kâra yansır.",
  "TMS 20 - defter değerinden indirim hesabı")

q("Varlıklara ilişkin teşviklerin nakit akış tablosunda sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın alımı ve teşvik brüt olarak gösterilir; sunum yöntemine bakılmaksızın bu gösterim değişmez",
  ["Teşvik hiçbir hâlde nakit akış tablosunda gösterilmez; yalnızca dipnotta açıklanmaktadır",
   "Varlık alımı ile teşvik her hâlde netleştirilerek tek bir tutar hâlinde gösterilmek zorundadır",
   "Teşvik her hâlde işletme faaliyetlerinden nakit girişi olarak sunulmak zorunda tutulmuştur",
   "Teşviklerin nakit akış tablosundaki sunumu TMS 20'de düzenlenmemiş bir husustur"],
  "TMS 20: bir varlığın alımı ve buna ilişkin teşvik, nakit akış tablosunun sunumunda önemli hareketler olarak değerlendirilir. Bu nedenle teşvikin varlıktan indirilip indirilmediğine bakılmaksızın bu hareketler ayrı kalemler hâlinde (brüt) gösterilir.",
  "TMS 20 - nakit akış tablosunda sunum")

q("Bir işletmeye bedelsiz olarak arazi devredilmiş; karşılığında o bölgede fabrika kurup beş yıl faaliyet göstermesi şartı konulmuştur. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Parasal olmayan bir teşviktir; arazi ve teşvik gerçeğe uygun değeriyle veya nominal tutarla kaydedilebilir",
  ["Arazi bedelsiz olduğundan hiçbir hâlde aktifleştirilemez; yalnızca dipnotta açıklanmaktadır",
   "Arazi her hâlde piyasa değerinin iki katı üzerinden aktifleştirilmek zorunda tutulmaktadır",
   "Arazinin gerçeğe uygun değeri her hâlde derhâl ve tümüyle gelir yazılmak zorunda kalınır",
   "Bedelsiz devredilen araziler TMS 20 kapsamı dışında olup hiçbir standartta düzenlenmemiştir"],
  "TMS 20: arazi gibi parasal olmayan teşviklerde, varlığın ve teşvikin gerçeğe uygun değeriyle muhasebeleştirilmesi olağan uygulamadır; alternatif olarak ikisi de nominal tutarla kaydedilebilir. Koşullu olduğundan gerçeğe uygun değerin tamamı derhâl gelir yazılmaz.",
  "TMS 20 - parasal olmayan teşvik (senaryo)")

q("Aşağıdakilerden hangileri varlıklara ilişkin devlet teşviklerinin sunum yöntemidir?\n\nI. Ertelenmiş gelir olarak sunulması\n\nII. Varlığın defter değerinden indirilmesi\n\nIII. Doğrudan özkaynağa kaydedilmesi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 20 iki sunum yöntemine izin verir: ertelenmiş gelir (I) ve varlığın defter değerinden indirim (II). Doğrudan özkaynağa kaydetme (III) ise gelir yaklaşımı benimsendiğinden KABUL EDİLMEZ.",
  "TMS 20 - varlık teşviklerinde sunum")

q("Amortismana tabi OLMAYAN bir varlığa ilişkin ve belirli yükümlülükler getiren teşvik bakımından aşağıdakilerden hangisi doğrudur?",
  "Yükümlülüklerin karşılanması için gereken maliyetlerin yüklenildiği dönemler boyunca kâr veya zarara yansıtılır",
  ["Teşvik her hâlde tahsil edildiği dönemde tümüyle gelir yazılmak zorunda tutulmaktadır",
   "Teşvik hiçbir hâlde kâr veya zarara yansıtılamaz; süresiz olarak yabancı kaynakta kalmaktadır",
   "Teşvik her hâlde doğrudan özkaynağa aktarılmak zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 20: amortismana tabi olmayan varlıklara ilişkin teşvikler belirli yükümlülüklerin yerine getirilmesini gerektirebilir. Bu durumda teşvik, söz konusu yükümlülüklerin karşılanması için gereken maliyetlerin yüklenildiği dönemler boyunca kâr veya zarara yansıtılır (arazi karşılığı bina inşa şartı gibi).",
  "TMS 20 - amortismana tabi olmayan varlık")

q("Devlet teşvikinin bir dizi koşulun karşılanmasını gerektiren bir paketin parçası olması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Teşvikin kâr veya zarara yansıtılacağı dönemler dikkatlice belirlenir; teşvik unsurlara ayrıştırılabilir",
  ["Teşvik her hâlde tek bir kalem sayılır ve hiçbir hâlde unsurlara ayrıştırılamamaktadır",
   "Teşvik her hâlde tahsil edildiği dönemde tümüyle gelir yazılmak zorunda tutulmaktadır",
   "Bu tür paketler TMS 20 kapsamı dışında olup hiçbir biçimde muhasebeleştirilmemektedir",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 20: teşvik, bir dizi koşulun yerine getirilmesini gerektiren bir mali yardım paketinin parçası olabilir. Bu durumda teşvikin kâr veya zarara yansıtılacağı dönemlerin belirlenmesinde dikkatli olunması ve teşvikin farklı esaslara göre yansıtılacak unsurlara ayrıştırılması uygun olabilir.",
  "TMS 20 - teşvik paketleri")

q("Bir işletme, satın aldığı makine için aldığı devlet teşvikini makinenin maliyetinden indirmiştir. Makinenin amortismanı ve teşvikin kâra yansıması bakımından aşağıdakilerden hangisi doğrudur?",
  "Amortisman indirilmiş tutar üzerinden hesaplanır; teşvik azaltılmış amortisman yoluyla kâra yansır",
  ["Amortisman brüt maliyet üzerinden hesaplanır; teşvik ayrıca gelir olarak da yazılmak zorundadır",
   "Makine için hiçbir hâlde amortisman ayrılmaz; teşvik alınması amortismanı ortadan kaldırmaktadır",
   "Teşvik bu yöntemde hiçbir hâlde kâr veya zarara yansımaz; kalıcı olarak varlıktan düşülür",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 20: teşvik varlığın defter değerinden indirildiğinde amortisman, indirilmiş (net) tutar üzerinden hesaplanır. Böylece teşvik, varlığın ömrü boyunca AZALTILMIŞ amortisman gideri yoluyla kâr veya zarara yansımış olur. Ayrıca gelir yazılmaz; çift sayım olurdu.",
  "TMS 20 - defter değerinden indirim (senaryo)")

q("Aşağıdaki ifadelerden hangileri varlıklara ilişkin teşvikler bakımından doğrudur?\n\nI. Ertelenmiş gelir yönteminde teşvik faydalı ömür boyunca gelir yazılır\n\nII. İndirim yönteminde teşvik azaltılmış amortisman yoluyla kâra yansır\n\nIII. İki yöntem dönem kârı üzerinde farklı net etki doğurur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Ertelenmiş gelir yönteminde teşvik faydalı ömür boyunca gelir yazılır (I) ve indirim yönteminde azaltılmış amortisman yoluyla kâra yansır (II). İki yöntem dönem kârı üzerinde AYNI net etkiyi doğurur; yalnızca sunum farklıdır. Bu nedenle III yanlıştır.",
  "TMS 20 - sunum yöntemleri")

q("Aşağıdaki ifadelerden hangileri TMS 20 bakımından doğrudur?\n\nI. Varlık alımı ve teşvik nakit akış tablosunda brüt gösterilir\n\nII. Parasal olmayan teşvik nominal tutarla kaydedilebilir\n\nIII. Teşvikin tahsil şekli uygulanacak muhasebe yöntemini belirler",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Varlık alımı ve teşvik nakit akış tablosunda brüt gösterilir (I) ve parasal olmayan teşvik nominal tutarla kaydedilebilir (II). Ancak teşvikin TAHSİL ŞEKLİ uygulanacak muhasebe yöntemini ETKİLEMEZ; bu nedenle III yanlıştır.",
  "TMS 20 - genel")

# ── C. Gelire ilişkin teşvikler ve geri ödeme (16) ─────────────────────────
q("Gelire ilişkin devlet teşviklerinin sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr veya zarar tablosunda ayrı bir gelir kalemi olarak veya ilgili giderden indirilerek sunulabilir",
  ["Yalnızca ayrı bir gelir kalemi olarak sunulabilir; giderden indirim yöntemi kabul edilmemektedir",
   "Yalnızca ilgili giderden indirilerek sunulabilir; ayrı gelir kalemi gösterimi yasaklanmıştır",
   "Her hâlde doğrudan özkaynakta gösterilmek zorunda olan bir kalemi ifade etmektedir",
   "Gelire ilişkin teşviklerin sunumu TMS 20'de düzenlenmemiş bir husus niteliğinde bulunur"],
  "TMS 20: gelire ilişkin teşvikler, kâr veya zararın bir parçası olarak ya 'diğer gelirler' gibi genel bir başlık altında ayrıca ya da ilgili giderden indirilmek suretiyle raporlanır. İki yöntem de kabul edilir.",
  "TMS 20 - gelir teşviklerinde iki yöntem")

q("Geçmişte oluşan gider veya zararları karşılamak amacıyla verilen teşvikler bakımından aşağıdakilerden hangisi doğrudur?",
  "Elde edilebilir hâle geldiği dönemde kâr veya zarara yansıtılır",
  ["Geçmiş dönemlere dağıtılarak geriye dönük olarak muhasebeleştirilmek zorunda tutulmaktadır",
   "Gelecek dönemlere yayılarak sistematik biçimde gelir yazılmak zorunda bulunmaktadır",
   "Hiçbir hâlde kâr veya zarara yansıtılamaz; süresiz olarak yabancı kaynakta kalmaktadır",
   "Bu tür teşvikler TMS 20 kapsamı dışında olup hiçbir biçimde muhasebeleştirilmemektedir"],
  "TMS 20: işletmeye acil finansman desteği sağlamak veya işletmenin geçmişte oluşan gider ya da zararlarını karşılamak amacıyla verilen ve gelecekle ilgili herhangi bir maliyetle ilişkisi bulunmayan devlet teşvikleri, elde edilebilir hâle geldiği dönemde kâr veya zarara yansıtılır.",
  "TMS 20 - geçmiş giderleri karşılayan teşvikler")

q("Devlet teşvikinin geri ödenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Geri ödenebilir hâle gelen teşvik, bir muhasebe tahminindeki değişiklik olarak muhasebeleştirilir",
  ["Geri ödeme her hâlde önceki dönem hatası sayılıp geriye dönük düzeltilmek zorunda kalınır",
   "Geri ödeme her hâlde muhasebe politikası değişikliği sayılıp geriye dönük uygulanmaktadır",
   "Geri ödeme hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Teşviklerin geri ödenmesi TMS 20'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 20: geri ödenmesi gereken hâle gelen devlet teşviki, TMS 8 uyarınca bir muhasebe tahminindeki değişiklik olarak muhasebeleştirilir. Geçmiş dönemler yeniden düzenlenmez.",
  "TMS 20 - geri ödeme")

q("Gelire ilişkin bir teşvikin geri ödenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Önce varsa teşvikle ilgili itfa edilmemiş ertelenmiş gelirden düşülür; aşan kısım gider yazılır",
  ["Geri ödenen tutarın tamamı her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulur",
   "Geri ödenen tutar hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Geri ödenen tutar her hâlde varlığın defter değerine eklenmek zorunda bulunmaktadır",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 20: gelire ilişkin bir teşvikin geri ödenmesi durumunda, geri ödeme öncelikle teşvike ilişkin itfa edilmemiş ertelenmiş gelir tutarından mahsup edilir. Geri ödemenin bu tutarı aşması veya ertelenmiş gelir bulunmaması hâlinde geri ödeme derhâl kâr veya zararda muhasebeleştirilir.",
  "TMS 20 - gelir teşvikinin geri ödenmesi")

q("Varlıklara ilişkin bir teşvikin geri ödenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın defter değeri artırılır veya ertelenmiş gelir azaltılır; ek birikmiş amortisman derhâl gider yazılır",
  ["Geri ödenen tutarın tamamı her hâlde doğrudan özkaynaklardan indirilmek zorunda kalınır",
   "Geri ödenen tutar hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Geri ödeme hâlinde varlık her hâlde bilanço dışı bırakılmak zorunda tutulmaktadır",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 20: varlığa ilişkin bir teşvikin geri ödenmesi durumunda, geri ödenen tutar kadar varlığın defter değeri artırılır veya ertelenmiş gelir azaltılır. Teşvik olmasaydı bugüne kadar kaydedilmiş olması gereken birikmiş ek amortisman, derhâl kâr veya zararda muhasebeleştirilir.",
  "TMS 20 - varlık teşvikinin geri ödenmesi")

q("Varlığa ilişkin bir teşvikin geri ödenmesi hâlinde değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Artan defter değerinin değer düşüklüğüne uğramış olabileceği dikkate alınmalıdır",
  ["Geri ödeme hâlinde hiçbir hâlde değer düşüklüğü söz konusu olmamak zorunda bulunmaktadır",
   "Geri ödeme hâlinde varlık her hâlde gerçeğe uygun değeriyle yeniden ölçülmek zorundadır",
   "Geri ödeme hâlinde varlık her hâlde bilanço dışı bırakılmak zorunda tutulmaktadır",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 20: varlığa ilişkin teşvikin geri ödenmesi hâlinde, artan defter değerinin değer düşüklüğüne uğramış olabileceği hususu dikkate alınır. Yeni defter değeri geri kazanılabilir tutarı aşabilir.",
  "TMS 20 - geri ödemede değer düşüklüğü")

gelir_tes, gider20 = 80_000, 200_000
net_gider = gider20 - gelir_tes
q(f"Bir işletme, personel eğitimi için katlandığı {tr(gider20)} TL gideri karşılamak üzere {tr(gelir_tes)} TL devlet teşviki almıştır. Teşvik ilgili giderden indirilerek sunulmaktadır. Kâr veya zarar tablosunda gösterilecek net eğitim gideri kaç TL'dir?",
  f"{tr(net_gider)} TL",
  [f"{tr(gider20)} TL", f"{tr(gider20 + gelir_tes)} TL", f"{tr(gelir_tes)} TL", f"{tr(gider20 - gelir_tes * 2)} TL"],
  f"Gelire ilişkin teşvik, ilgili giderden indirilerek sunulabilir: {tr(gider20)} − {tr(gelir_tes)} = {tr(net_gider)} TL net gider. Alternatif yöntemde {tr(gider20)} TL gider ve {tr(gelir_tes)} TL gelir ayrı gösterilir; net kâr etkisi aynıdır.",
  "TMS 20 - gelir teşvikinde netleştirme")

tes_gp, itfa_edilmemis, geri = 150_000, 90_000, 120_000
gider_yaz = geri - itfa_edilmemis
q(f"Bir işletmenin aldığı {tr(tes_gp)} TL gelire ilişkin teşvike ait itfa edilmemiş ertelenmiş gelir bakiyesi {tr(itfa_edilmemis)} TL'dir. İşletme koşulları ihlal ettiğinden teşvikin {tr(geri)} TL'lik kısmını geri ödemek zorunda kalmıştır. Derhâl gider yazılacak tutar kaç TL'dir?",
  f"{tr(gider_yaz)} TL",
  [f"{tr(geri)} TL", f"{tr(itfa_edilmemis)} TL", f"{tr(tes_gp)} TL", "0 TL"],
  f"TMS 20: geri ödeme öncelikle itfa edilmemiş ertelenmiş gelirden mahsup edilir: {tr(geri)} − {tr(itfa_edilmemis)} = {tr(gider_yaz)} TL. Ertelenmiş geliri aşan bu kısım derhâl kâr veya zararda gider olarak muhasebeleştirilir.",
  "TMS 20 - geri ödeme hesabı")

q("Devlet yardımlarının açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulanan muhasebe politikası, teşviklerin niteliği ve kapsamı ile yararlanılmamış koşullar açıklanır",
  ["Devlet yardımları hakkında hiçbir açıklama yapılmaz; yalnızca tutarlar tabloda gösterilmektedir",
   "Yalnızca alınan teşvikin tutarı açıklanır; niteliği ve koşulları hiçbir hâlde belirtilmemektedir",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca teşvikten yararlanamayan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 20: işletme, devlet teşviklerine uygulanan muhasebe politikası ve sunum yöntemlerini, finansal tablolara yansıtılan devlet teşviklerinin niteliğini ve kapsamını, işletmenin doğrudan yararlandığı diğer devlet yardımlarına ilişkin göstergeleri ve yararlanılmamış koşullar ile devlet yardımlarına ilişkin diğer koşullu borçları açıklar.",
  "TMS 20 - açıklamalar")

q("Ekonomik faydası ölçülemeyen devlet yardımları bakımından aşağıdakilerden hangisi doğrudur?",
  "Makul biçimde değer biçilemeyen yardımlar finansal tablolara yansıtılmaz; açıklama yapılır",
  ["Bu yardımlar her hâlde tahmini bir tutarla finansal tablolara yansıtılmak zorunda tutulur",
   "Bu yardımlar hiçbir yerde belirtilmez; ne tabloda ne dipnotta yer almak zorunda bulunur",
   "Bu yardımlar her hâlde doğrudan özkaynağa kaydedilmek zorunda olan kalemleri ifade eder",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 20: bazı devlet yardımlarına makul biçimde değer biçilemez (ücretsiz teknik veya pazarlama önerileri, garanti sağlanması gibi). Bu yardımlar finansal tablolara yansıtılmaz; ancak açıklama yapılır.",
  "TMS 20 - ölçülemeyen yardımlar")

q("Devletin işletmenin müşterisi olarak yaptığı işlemler bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin hasılatının bir kısmını oluşturan bu işlemler devlet yardımı sayılmaz",
  ["Devletle yapılan tüm işlemler her hâlde devlet yardımı sayılmak zorunda tutulmaktadır",
   "Devletle yapılan işlemler hiçbir hâlde hasılat olarak muhasebeleştirilememektedir",
   "Devletle yapılan işlemler her hâlde doğrudan özkaynağa kaydedilmek zorunda kalınmaktadır",
   "Bu husus TMS 20'de düzenlenmemiş olup uygulamada dikkate alınmayan bir konu niteliğindedir"],
  "TMS 20: işletmenin faaliyetlerinin bir bölümünü oluşturan ve devletle yapılan işlemler, devlet yardımlarından ayırt edilemeyeceğinden bu Standart kapsamında değerlendirilmez. İşletmenin hasılatının bir kısmını oluşturan bu işlemler devlet yardımı sayılmaz.",
  "TMS 20 - devletle ticari işlemler")

q("Piyasa faizinin altında faiz oranıyla alınan devlet kredisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Faiz avantajı devlet teşviki olarak ele alınır; teşvik, kredinin defter değeri ile elde edilen tutar arasındaki fark kadardır",
  ["Faiz avantajı hiçbir hâlde devlet teşviki sayılmaz; kredi normal borç olarak muhasebeleştirilir",
   "Kredinin anaparasının tamamı her hâlde devlet teşviki sayılıp gelir yazılmak zorundadır",
   "Bu tür krediler hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 20: piyasa faiz oranından düşük faizli devlet kredisinden sağlanan fayda devlet teşviki olarak değerlendirilir. Kredi TFRS 9 uyarınca muhasebeleştirilip ölçülür; düşük faiz oranından sağlanan fayda, kredinin ilk defter değeri ile elde edilen tutar arasındaki fark olarak ölçülür.",
  "TMS 20 - düşük faizli devlet kredisi")

q("Bir işletme, ihracat gelirlerini artırdığı için devletten geçmiş dönem giderlerini karşılamak üzere destek almıştır ve desteğin gelecekle ilgili hiçbir maliyetle ilişkisi yoktur. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Destek, elde edilebilir hâle geldiği dönemde kâr veya zarara yansıtılır",
  ["Destek gelecek dönemlere yayılarak sistematik biçimde gelir yazılmak zorunda tutulmaktadır",
   "Destek geçmiş dönemlere dağıtılarak geriye dönük olarak muhasebeleştirilmek zorundadır",
   "Destek her hâlde doğrudan özkaynağa kaydedilmek zorunda olan bir kalemi ifade etmektedir",
   "Destek hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilmektedir"],
  "TMS 20: geçmişte oluşan gider veya zararları karşılamak amacıyla verilen ve gelecekle ilgili herhangi bir maliyetle ilişkisi bulunmayan teşvikler, elde edilebilir hâle geldiği dönemde kâr veya zarara yansıtılır. Yayma yapılmaz; karşılanacak gelecek maliyeti yoktur.",
  "TMS 20 - geçmiş gideri karşılayan teşvik (senaryo)")

q("Aşağıdakilerden hangileri gelire ilişkin devlet teşviklerinin sunum yöntemidir?\n\nI. Ayrı bir gelir kalemi olarak sunulması\n\nII. İlgili giderden indirilerek sunulması\n\nIII. Doğrudan geçmiş yıllar kârlarına aktarılması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 20 gelire ilişkin teşviklerde iki sunum yöntemine izin verir: ayrı gelir kalemi (I) veya ilgili giderden indirim (II). Doğrudan geçmiş yıllar kârlarına aktarma (III) ise gelir yaklaşımıyla bağdaşmaz; kabul edilmez.",
  "TMS 20 - gelir teşviklerinde sunum")

q("Aşağıdakilerden hangileri TMS 20'ye göre açıklanır?\n\nI. Devlet teşviklerine uygulanan muhasebe politikası ve sunum yöntemleri\n\nII. Finansal tablolara yansıtılan teşviklerin niteliği ve kapsamı\n\nIII. Yararlanılmamış koşullar ve devlet yardımlarına ilişkin diğer koşullu borçlar",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 20 üçünü de açıklama konusu sayar: uygulanan muhasebe politikası ve sunum yöntemleri (I), tablolara yansıtılan teşviklerin niteliği ve kapsamı (II) ile yararlanılmamış koşullar ve diğer koşullu borçlar (III).",
  "TMS 20 - açıklamalar")

q("Aşağıdaki ifadelerden hangileri teşviklerin geri ödenmesi bakımından doğrudur?\n\nI. Geri ödeme bir muhasebe tahmini değişikliği olarak ele alınır\n\nII. Gelir teşvikinde önce itfa edilmemiş ertelenmiş gelirden mahsup edilir\n\nIII. Geri ödeme önceki dönem hatası sayılıp geriye dönük düzeltilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Geri ödeme TMS 8 uyarınca muhasebe tahmini değişikliğidir (I) ve gelire ilişkin teşvikte önce itfa edilmemiş ertelenmiş gelirden mahsup edilir (II). Önceki dönem hatası SAYILMAZ ve geriye dönük düzeltilmez; bu nedenle III yanlıştır.",
  "TMS 20 - geri ödeme")

# ── D. Uygulama ve karma (16) ──────────────────────────────────────────────
q("Bir işletme, devlet teşvikini tahsil ettiği yıl tümüyle gelir yazmıştır; oysa teşvik beş yıllık bir yatırımın maliyetini karşılamaktadır. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulama yanlıştır; teşvik ilgili maliyetlerin gider yazıldığı dönemler boyunca yansıtılmalıdır",
  ["Uygulama doğrudur; teşvikler her hâlde tahsil edildikleri dönemde gelir yazılmak zorundadır",
   "Uygulama doğrudur; teşviklerin ne zaman gelir yazılacağı işletmenin serbest takdirindedir",
   "Uygulama yanlıştır; teşvik her hâlde doğrudan özkaynağa kaydedilmek zorunda bulunmaktadır",
   "Uygulama yanlıştır; teşvik hiçbir hâlde kâr veya zarara yansıtılamayan bir kalemi ifade eder"],
  "TMS 20: teşviklerin tahsil esasına göre gelir yazılması, tahakkuk esası varsayımıyla bağdaşmaz. Teşvik, karşılanması amaçlanan maliyetlerin gider olarak muhasebeleştirildiği dönemler boyunca sistematik biçimde kâr veya zarara yansıtılmalıdır.",
  "TMS 20 - tahsil esasının reddi (senaryo)")

q("Devlet teşviklerinin muhasebeleştirilmesinde tahakkuk esası bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşviklerin tahsil esasına göre gelir yazılması tahakkuk esasıyla bağdaşmaz",
  ["Teşvikler için tahakkuk esası uygulanmaz; tahsil esası her hâlde geçerli olmak zorundadır",
   "Teşvikler için hiçbir muhasebe esası uygulanmaz; kayıt zamanı serbestçe belirlenmektedir",
   "Teşvikler yalnızca nakit esasına göre muhasebeleştirilir; tahakkuk hiç dikkate alınmaz",
   "Bu husus TMS 20'de düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 20: teşviklerin tahsil esasına göre kâr veya zarara yansıtılması tahakkuk esası varsayımıyla bağdaşmaz. Böyle bir uygulama, ancak teşvikin tahsil edildiği dönemden başka bir döneme dağıtılmasına ilişkin bir esas bulunmadığında kabul edilebilir.",
  "TMS 20 - tahakkuk esası")

q("Bir işletme, aldığı devlet teşvikini doğrudan özkaynak kalemi olarak kaydetmiştir. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulama yanlıştır; gelir yaklaşımı gereği teşvik kâr veya zararda muhasebeleştirilmelidir",
  ["Uygulama doğrudur; teşvikler her hâlde doğrudan özkaynağa kaydedilmek zorunda tutulmaktadır",
   "Uygulama doğrudur; teşvikin nereye kaydedileceği işletmenin serbest takdirine bırakılmıştır",
   "Uygulama yanlıştır; teşvik her hâlde varlığın defter değerine eklenmek zorunda bulunmaktadır",
   "Uygulama yanlıştır; teşvik hiçbir hâlde muhasebeleştirilemeyen bir kalemi ifade etmektedir"],
  "TMS 20 gelir yaklaşımını benimser: devlet teşvikleri ortaklar dışındaki bir kaynaktan elde edildiğinden doğrudan özkaynağa kaydedilmez. Teşvik, karşılamayı amaçladığı maliyetlerle eşleştirilerek kâr veya zararda muhasebeleştirilir.",
  "TMS 20 - özkaynağa kaydetme yanlışı (senaryo)")

q("Devlet teşviki ile ilgili koşulların yerine getirilmemesi riski bakımından aşağıdakilerden hangisi doğrudur?",
  "Koşullu borç doğuruyorsa TMS 37 uyarınca ele alınır ve açıklanır",
  ["Bu risk hiçbir hâlde dikkate alınmaz; teşvik koşulsuz kabul edilmek zorunda bulunmaktadır",
   "Bu risk her hâlde teşvikin tümüyle iptal edilmesini gerektiren bir durumu ifade etmektedir",
   "Bu risk yalnızca vergi idaresini ilgilendirir; finansal tablolara hiç yansıtılmamaktadır",
   "Bu husus hiçbir standartta düzenlenmemiş olup uygulamada dikkate alınmayan bir konudur"],
  "TMS 20: teşvike bağlı koşulların yerine getirilmemesi hâlinde ortaya çıkabilecek koşullu borçlar veya koşullu varlıklar TMS 37 uyarınca ele alınır. Ayrıca yararlanılmamış koşullar ve devlet yardımlarına ilişkin diğer koşullu borçlar açıklanır.",
  "TMS 20 - koşullu borçlar")

q("Devlet teşviklerinin diğer standartlarla ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düşük faizli devlet kredisi TFRS 9, vergiye dayalı yardımlar ise TMS 12 kapsamındadır",
  ["Devlet teşvikleriyle ilgili her husus yalnızca TMS 20'de düzenlenmiş olup başka standart yoktur",
   "Devlet teşvikleri hiçbir standartta düzenlenmemiş olup uygulamada serbest bırakılmıştır",
   "Devlet teşvikleri yalnızca TMS 12 kapsamında olup TMS 20'nin hiçbir hükmü uygulanmamaktadır",
   "Devlet teşvikleri yalnızca TFRS 9 kapsamında olup TMS 20 yürürlükten kaldırılmış bulunmaktadır"],
  "TMS 20: piyasa faizinin altındaki devlet kredileri TFRS 9 uyarınca muhasebeleştirilip ölçülür; sağlanan fayda TMS 20 uyarınca teşvik olarak ele alınır. Vergilendirilebilir kârın belirlenmesinde sağlanan yardımlar ise TMS 20 kapsamı dışında olup TMS 12 kapsamındadır.",
  "TMS 20 - diğer standartlarla ilişki")

mal_t, tes_t, om_t, gecen_t = 1_000_000, 400_000, 8, 2
net_t = mal_t - tes_t
birik_net = net_t / om_t * gecen_t
q(f"Bir işletme {tr(mal_t)} TL maliyetli, {om_t} yıl faydalı ömürlü bir makine için {tr(tes_t)} TL teşvik almış ve teşviki varlığın defter değerinden indirmiştir. Kalıntı değer sıfırdır. {gecen_t} yıl sonundaki birikmiş amortisman kaç TL'dir?",
  f"{tr(birik_net)} TL",
  [f"{tr(mal_t / om_t * gecen_t)} TL", f"{tr(tes_t / om_t * gecen_t)} TL", f"{tr(net_t)} TL", f"{tr((mal_t + tes_t) / om_t * gecen_t)} TL"],
  f"Teşvik defter değerinden indirildiğinden amortisman net tutar üzerinden hesaplanır. Net maliyet = {tr(mal_t)} − {tr(tes_t)} = {tr(net_t)} TL. Yıllık amortisman = {tr(net_t)} ÷ {om_t} = {tr(net_t / om_t)} TL. {gecen_t} yıl sonunda birikmiş = {tr(net_t / om_t)} × {gecen_t} = {tr(birik_net)} TL.",
  "TMS 20 - net maliyet üzerinden amortisman")

q("Bir işletme, henüz koşullarını yerine getirmediği ancak yerine getireceğine dair makul güvence bulunan bir teşviki muhasebeleştirmek istemektedir. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvikin elde edileceğine dair de makul güvence varsa muhasebeleştirilebilir",
  ["Koşullar fiilen yerine getirilmedikçe teşvik hiçbir hâlde muhasebeleştirilememektedir",
   "Teşvik nakden tahsil edilmedikçe hiçbir hâlde muhasebeleştirilemez; güvence yeterli değildir",
   "Teşvik her hâlde derhâl ve tümüyle gelir yazılmak zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 20: devlet teşvikleri, (a) işletmenin teşvikin öngördüğü koşulları yerine getireceğine ve (b) teşvikin elde edileceğine dair makul güvence oluştuğunda muhasebeleştirilir. Koşulların fiilen tamamlanmış olması veya nakden tahsil şart değildir; iki makul güvence yeterlidir.",
  "TMS 20 - makul güvence (senaryo)")

q("Devlet teşviklerinin işletme için önemi ve raporlanma amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Teşvikin niteliği, kapsamı ve süresi kullanıcıların finansal tabloları karşılaştırmasına yardımcı olur",
  ["Teşviklerin raporlanmasının kullanıcılar açısından hiçbir bilgi değeri bulunmamaktadır",
   "Teşvikler yalnızca vergi matrahını ilgilendirir; finansal tablo kullanıcılarını hiç ilgilendirmez",
   "Teşvikler yalnızca işletmenin ortaklarını ilgilendirir; diğer kullanıcılara açıklanmamaktadır",
   "Bu husus TMS 20'de hiçbir biçimde ele alınmamış olup uygulamada dikkate alınmamaktadır"],
  "TMS 20: devlet yardımlarının raporlanması, işletmenin faaliyet sonuçlarının önceki dönemlerle ve diğer işletmelerin finansal tablolarıyla karşılaştırılmasına imkân verdiğinden önemlidir. Teşvikin niteliği, kapsamı ve süresi açıklanır.",
  "TMS 20 - raporlamanın amacı")

q("Aşağıdakilerden hangisi TMS 20'ye göre bir devlet teşviki örneğidir?",
  "Bir bölgede fabrika kurma koşuluyla verilen nakit destek",
  ["İşletmenin ödeyeceği kurumlar vergisinin oranında yapılan indirim niteliğindeki uygulamalar",
   "İşletmeye tanınan yatırım indirimi niteliğindeki vergi avantajını ifade eden uygulamaların tümü",
   "İşletmeye tanınan hızlandırılmış amortisman imkânı niteliğindeki vergisel kolaylıkların tümü",
   "Belirli bir süre için işletmeye tanınan vergi tatili niteliğindeki uygulamaların tamamı"],
  "TMS 20: belirli koşulların yerine getirilmesi karşılığında kaynak aktarımı biçimindeki yardımlar devlet teşvikidir. Diğer şıklardaki vergi oranı indirimi, yatırım indirimi, hızlandırılmış amortisman ve vergi tatili ise vergilendirilebilir kârın belirlenmesine ilişkin olduğundan TMS 20 kapsamı DIŞINDADIR.",
  "TMS 20 - teşvik örneği")

q("Devlet teşvikinin muhasebeleştirilmesinde teşvikin tahsil şekli bakımından aşağıdakilerden hangisi doğrudur?",
  "Tahsil şekli uygulanacak muhasebe yöntemini etkilemez",
  ["Nakden tahsil edilen teşvikler için farklı, ayni teşvikler için farklı yöntem uygulanmaktadır",
   "Tahsil şekli muhasebe yöntemini her hâlde belirleyen temel unsuru oluşturmak zorundadır",
   "Yalnızca nakden tahsil edilen teşvikler muhasebeleştirilir; diğerleri kayda alınmamaktadır",
   "Bu husus TMS 20'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 20: teşvikin tahsil şekli, teşvike ilişkin olarak uygulanacak muhasebe yöntemini etkilemez. Bu nedenle teşvik ister nakit olarak isterse devlete olan bir borcun azaltılması biçiminde elde edilsin aynı biçimde muhasebeleştirilir.",
  "TMS 20 - tahsil şeklinin etkisizliği")

q("Bir işletme, devlete olan bir borcunun silinmesi biçiminde devlet desteği almıştır. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Tahsil şekli yöntemi etkilemez; destek nakit alınmış gibi aynı esaslara göre muhasebeleştirilir",
  ["Nakit alınmadığından destek hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanır",
   "Borcun silinmesi her hâlde doğrudan özkaynağa kaydedilmek zorunda olan bir işlemi ifade eder",
   "Borcun silinmesi her hâlde önceki dönem hatası sayılıp geriye dönük düzeltilmek zorundadır",
   "Borç silinmesi biçimindeki destekler TMS 20 kapsamı dışında olup düzenlenmemiş bulunmaktadır"],
  "TMS 20: teşvikin tahsil şekli uygulanacak muhasebe yöntemini etkilemez. Teşvik ister nakit olarak isterse devlete olan bir borcun azaltılması biçiminde elde edilsin, aynı esaslara göre muhasebeleştirilir.",
  "TMS 20 - borç silinmesi (senaryo)")

q("Bir işletme, teşvik koşullarını ihlal ettiği için varlığa ilişkin teşvikin tamamını geri ödemek zorunda kalmıştır. TMS 20 bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın defter değeri artırılır; teşvik olmasaydı kaydedilecek birikmiş ek amortisman derhâl gider yazılır",
  ["Geri ödenen tutarın tamamı derhâl gider yazılır; varlığın defter değerine hiç dokunulmamaktadır",
   "Geri ödenen tutarın tamamı doğrudan özkaynaklardan indirilmek zorunda tutulan bir kalemdir",
   "Varlık her hâlde bilanço dışı bırakılmak zorunda olup amortisman söz konusu olmamaktadır",
   "Geri ödeme geriye dönük düzeltme gerektirir; geçmiş dönem tabloları yeniden düzenlenmektedir"],
  "TMS 20: varlığa ilişkin teşvikin geri ödenmesinde geri ödenen tutar kadar varlığın defter değeri artırılır (veya ertelenmiş gelir azaltılır). Teşvik alınmamış olsaydı bugüne kadar kaydedilmiş olması gereken birikmiş ek amortisman derhâl kâr veya zararda muhasebeleştirilir. Geriye dönük düzeltme yapılmaz.",
  "TMS 20 - varlık teşvikinin geri ödenmesi (senaryo)")

q("Aşağıdakilerden hangileri TMS 20 kapsamı DIŞINDADIR?\n\nI. Vergi tatilleri\n\nII. Yatırım indirimi\n\nIII. Hızlandırılmış amortisman imkânı",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 20, vergilendirilebilir kârın belirlenmesinde sağlanan veya vergi yükümlülüğü esas alınarak belirlenen yardımları kapsamaz. Vergi tatilleri (I), yatırım indirimi (II) ve hızlandırılmış amortisman (III) üçü de bu nedenle kapsam dışıdır; TMS 12 ilgilidir.",
  "TMS 20 - kapsam dışı")

q("Aşağıdaki ifadelerden hangileri TMS 20 bakımından doğrudur?\n\nI. Düşük faizli devlet kredisinden sağlanan fayda teşvik sayılır\n\nII. Değer biçilemeyen devlet yardımları tablolara yansıtılmaz ama açıklanır\n\nIII. Devletin işletmenin müşterisi olduğu işlemler devlet yardımı sayılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Piyasa faizinin altındaki krediden sağlanan fayda teşviktir (I) ve makul biçimde değer biçilemeyen yardımlar tablolara yansıtılmaz ancak açıklanır (II). İşletmenin hasılatının bir kısmını oluşturan, devletin müşteri olarak taraf olduğu işlemler ise devlet yardımı SAYILMAZ; bu nedenle III yanlıştır.",
  "TMS 20 - genel")

q("Aşağıdaki ifadelerden hangileri TMS 20 bakımından doğrudur?\n\nI. Teşvikler karşıladıkları maliyetlerle eşleştirilerek kâra yansıtılır\n\nII. Geçmiş giderleri karşılayan teşvik elde edilebilir olduğu dönemde kâra yansıtılır\n\nIII. Teşviklerin tahsil esasına göre gelir yazılması tahakkuk esasıyla bağdaşır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Teşvikler karşıladıkları maliyetlerle eşleştirilir (I) ve geçmiş giderleri karşılayan, gelecek maliyetle ilişkisi olmayan teşvik elde edilebilir olduğu dönemde kâra yansıtılır (II). Tahsil esasına göre gelir yazma ise tahakkuk esasıyla BAĞDAŞMAZ; bu nedenle III yanlıştır.",
  "TMS 20 - eşleştirme")

q("Devlet teşviklerinin sunumunda işletmenin seçim yapması bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme kabul edilen yöntemlerden birini seçip tutarlı biçimde uygular ve seçtiği yöntemi açıklar",
  ["İşletme her dönem farklı yöntem uygulamak zorunda olup tutarlılık aranmamaktadır",
   "İşletmenin hiçbir seçim hakkı bulunmayıp yöntem her hâlde vergi idaresince belirlenmektedir",
   "İşletme yöntem seçer ancak seçtiği yöntemi hiçbir hâlde açıklamak zorunda bulunmamaktadır",
   "Yöntem seçimi TMS 20'de düzenlenmemiş olup uygulamada dikkate alınmayan bir husustur"],
  "TMS 20 hem varlıklara hem gelire ilişkin teşviklerde ikişer sunum yöntemine izin verir. İşletme seçtiği yöntemi tutarlı biçimde uygular ve devlet teşviklerine uygulanan muhasebe politikası ile sunum yöntemlerini dipnotlarda açıklar.",
  "TMS 20 - yöntem seçimi ve tutarlılık")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 20; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
