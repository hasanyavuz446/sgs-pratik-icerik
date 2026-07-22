# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 36 Varlıklarda Değer Düşüklüğü — 60 soru.
Kaynak: KGK TMS 36. Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-10 soru, "hepsi" ~2 (%20-25)."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_36_deger_dusuklugu"
PREFIX, SEED = "std-tms36-gen", 20260713
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_36_deger_dusuklugu.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Temel kavramlar (14) ────────────────────────────────────────────────
q("TMS 36'nın amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlıkların geri kazanılabilir tutarından yüksek bir değerle izlenmemesini sağlamaktır",
  ["Varlıkların her hâlde gerçeğe uygun değerleriyle ölçülmesini sağlamayı amaçlamaktadır",
   "Varlıkların amortisman yöntemlerinin nasıl belirleneceğini düzenlemeyi amaçlamaktadır",
   "Varlıkların ilk muhasebeleştirilmesindeki maliyet unsurlarını belirlemeyi amaçlamaktadır",
   "TMS 36'nın belirlenmiş bir amacı bulunmayıp yalnızca biçimsel bir düzenleme niteliğindedir"],
  "TMS 36: bu Standardın amacı, işletmenin varlıklarının geri kazanılabilir tutarından daha yüksek bir değerden izlenmemesini sağlamak amacıyla uygulanması gereken işlemleri belirlemektir.",
  "TMS 36 - amaç")

q("Değer düşüklüğü zararı bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir varlığın defter değerinin geri kazanılabilir tutarını aşan kısmıdır",
  ["Bir varlığın maliyetinin birikmiş amortismanı aşan kısmını ifade eden bir kavramdır",
   "Bir varlığın gerçeğe uygun değerinin maliyetini aşan kısmını ifade eden bir kavramdır",
   "Bir varlığın satışından doğan zararı ifade eden ve elden çıkarmada ortaya çıkan kalemdir",
   "Değer düşüklüğü zararı TMS 36'da tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 36: değer düşüklüğü zararı, bir varlığın defter değerinin geri kazanılabilir tutarını aşan kısmıdır.",
  "TMS 36 - değer düşüklüğü zararı")

q("TMS 36'ya göre geri kazanılabilir tutar bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değerden satış maliyetleri düşülerek bulunan tutar ile kullanım değerinden YÜKSEK olanıdır",
  ["Gerçeğe uygun değer ile kullanım değerinden DÜŞÜK olanını ifade eden bir kavram niteliğindedir",
   "Her hâlde varlığın gerçeğe uygun değerini ifade eden ve kullanım değerini dikkate almayan ölçüdür",
   "Her hâlde varlığın kullanım değerini ifade eden ve gerçeğe uygun değeri dikkate almayan ölçüdür",
   "Geri kazanılabilir tutar TMS 36'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: geri kazanılabilir tutar, bir varlığın veya nakit yaratan birimin gerçeğe uygun değerinden satış maliyetleri düşülmek suretiyle hesaplanan değeri ile kullanım değerinden YÜKSEK olanıdır. Bu, Standardın en kritik tanımıdır.",
  "TMS 36 - geri kazanılabilir tutar")

q("TMS 36'ya göre kullanım değeri bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlıktan elde edilmesi beklenen gelecekteki nakit akışlarının bugünkü değeridir",
  ["Varlığın piyasada satılması hâlinde elde edilecek net tutarı ifade eden bir kavramdır",
   "Varlığın ilk edinildiği tarihteki maliyet bedelini ifade eden bir kavram niteliğindedir",
   "Varlığın birikmiş amortismanı düşülmüş defter değerini ifade eden bir kavramı karşılamaktadır",
   "Kullanım değeri TMS 36'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: kullanım değeri, bir varlık veya nakit yaratan birimden elde edilmesi beklenen gelecekteki nakit akışlarının bugünkü değeridir.",
  "TMS 36 - kullanım değeri")

q("Nakit yaratan birim bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer varlıklardan büyük ölçüde bağımsız nakit girişi sağlayan en küçük tanımlanabilir varlık grubudur",
  ["İşletmenin en büyük varlık grubunu ifade eden ve bölünemeyen bir bütünü karşılamaktadır",
   "İşletmenin nakit ve nakit benzeri varlıklarının toplamını ifade eden bir kavram niteliğindedir",
   "İşletmenin yalnızca nakit yaratan tek bir makinesini ifade eden dar kapsamlı bir kavramdır",
   "Nakit yaratan birim TMS 36'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: nakit yaratan birim, diğer varlıklardan veya varlık gruplarından sağlanan nakit girişlerinden büyük ölçüde bağımsız nakit girişi sağlayan en küçük tanımlanabilir varlık grubudur.",
  "TMS 36 - nakit yaratan birim")

q("Değer düşüklüğü belirtilerinin değerlendirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme her raporlama dönemi sonunda değer düşüklüğü belirtisi olup olmadığını değerlendirir",
  ["Değer düşüklüğü belirtileri yalnızca beş yılda bir değerlendirilmek zorunda tutulmaktadır",
   "Değer düşüklüğü belirtileri yalnızca vergi idaresi talep ettiğinde değerlendirilmektedir",
   "Değer düşüklüğü belirtileri yalnızca varlık satılırken değerlendirilmek zorunda kalınmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: işletme her raporlama döneminin sonunda bir varlığa ilişkin değer düşüklüğü belirtisi bulunup bulunmadığını değerlendirir. Böyle bir belirti varsa varlığın geri kazanılabilir tutarını tahmin eder.",
  "TMS 36 - belirtilerin değerlendirilmesi")

q("Belirtiden bağımsız olarak yıllık değer düşüklüğü testi gerektiren varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Sınırsız ömürlü maddi olmayan duran varlıklar, henüz kullanıma hazır olmayanlar ve şerefiye yıllık test edilir",
  ["Tüm maddi duran varlıklar her hâlde yıllık olarak test edilmek zorunda tutulmaktadır",
   "Hiçbir varlık belirti olmaksızın test edilmez; her hâlde belirti aranmak zorunda kalınmaktadır",
   "Yalnızca stoklar belirti aranmaksızın yıllık olarak test edilmek zorunda bulunmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 36: değer düşüklüğü belirtisi olsun olmasın, (a) sınırsız faydalı ömre sahip maddi olmayan duran varlıklar, (b) henüz kullanıma hazır olmayan maddi olmayan duran varlıklar ve (c) işletme birleşmesinde edinilen şerefiye yıllık olarak değer düşüklüğü testine tabi tutulur.",
  "TMS 36 - yıllık zorunlu test")

q("Aşağıdakilerden hangisi TMS 36'ya göre bir DIŞ değer düşüklüğü belirtisidir?",
  "Varlığın piyasa değerinde beklenenden çok daha fazla düşüş olması",
  ["Varlığın fiziksel olarak hasar gördüğünün işletme içi raporlamayla tespit edilmesi niteliğinde durum",
   "Varlığın ekonomik performansının beklenenden düşük olduğunun iç raporlamayla anlaşılması durumu",
   "Varlığın kullanım biçiminde işletme içinde önemli değişiklikler yapılmasına karar verilmesi durumu",
   "Varlığın atıl duruma düştüğünün işletmenin kendi iç raporlama sistemiyle belirlenmesi durumu"],
  "TMS 36: dış kaynaklı belirtiler arasında varlığın piyasa değerinin beklenenden fazla düşmesi, teknolojik/piyasa/ekonomik/hukuki çevrede olumsuz değişiklikler, piyasa faiz oranlarındaki artış ve net varlıkların piyasa değerini aşması sayılır. Diğer şıklardaki hasar, düşük performans, kullanım değişikliği ve atıl kalma İÇ kaynaklı belirtilerdir.",
  "TMS 36 - dış kaynaklı belirtiler")

q("Aşağıdakilerden hangisi TMS 36'ya göre bir İÇ değer düşüklüğü belirtisidir?",
  "Varlığın fiziksel olarak hasar görmüş olması",
  ["Varlığın piyasa değerinde beklenenden çok daha fazla düşüş yaşandığının gözlemlenmesi durumu",
   "İşletmenin faaliyet gösterdiği teknolojik ve ekonomik çevrede olumsuz değişiklikler olması durumu",
   "Piyasa faiz oranlarında artış olması ve bunun kullanım değeri hesabını etkilemesi niteliğinde durum",
   "İşletmenin net varlıklarının defter değerinin piyasa değerini aşması niteliğindeki durumların tümü"],
  "TMS 36: iç kaynaklı belirtiler arasında varlığın kullanım dışı kalması veya fiziksel hasar görmesi, kullanım biçiminde olumsuz değişiklikler ve ekonomik performansının beklenenden kötü olacağını gösteren iç raporlama kanıtları sayılır. Diğer şıklar DIŞ kaynaklı belirtilerdir.",
  "TMS 36 - iç kaynaklı belirtiler")

q("Geri kazanılabilir tutarın hesaplanmasında kolaylık bakımından aşağıdakilerden hangisi doğrudur?",
  "İki tutardan biri defter değerini aşıyorsa değer düşüklüğü yoktur; diğerinin hesaplanmasına gerek kalmaz",
  ["Her hâlde iki tutarın da ayrı ayrı hesaplanması zorunlu olup hiçbir kolaylık bulunmamaktadır",
   "Her hâlde yalnızca kullanım değerinin hesaplanması yeterli olup diğeri hiç dikkate alınmaz",
   "Her hâlde yalnızca gerçeğe uygun değerin hesaplanması yeterli olup kullanım değeri aranmaz",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: geri kazanılabilir tutar, gerçeğe uygun değerden satış maliyetleri düşülmüş tutar ile kullanım değerinden yüksek olanıdır. Bu tutarlardan HERHANGİ BİRİ varlığın defter değerini aşıyorsa varlık değer düşüklüğüne uğramamıştır ve diğer tutarın tahmin edilmesine gerek yoktur.",
  "TMS 36 - hesaplama kolaylığı")

q("Değer düşüklüğü zararının muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet modelinde derhâl kâr veya zarara yansıtılır",
  ["Her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade etmektedir",
   "Her hâlde gelecek dönemlere yayılarak sistematik biçimde gider yazılmak zorunda kalınır",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Değer düşüklüğü zararının muhasebeleştirilmesi TMS 36'da düzenlenmemiş bir husustur"],
  "TMS 36: değer düşüklüğü zararı, varlık yeniden değerlenmiş tutarı üzerinden gösterilmedikçe derhâl kâr veya zararda muhasebeleştirilir. Yeniden değerlenmiş varlıklarda ise değer artışı ölçüsünde diğer kapsamlı gelirde muhasebeleştirilir.",
  "TMS 36 - zararın muhasebeleştirilmesi")

q("Yeniden değerlenmiş bir varlıkta değer düşüklüğü zararı bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığa ilişkin değer artışı fonu ölçüsünde diğer kapsamlı gelirde muhasebeleştirilir",
  ["Her hâlde ve istisnasız tamamıyla kâr veya zarara yansıtılmak zorunda tutulmaktadır",
   "Her hâlde ve istisnasız tamamıyla diğer kapsamlı gelirde muhasebeleştirilmek zorundadır",
   "Yeniden değerlenmiş varlıklarda hiçbir hâlde değer düşüklüğü söz konusu olmamaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: yeniden değerlenmiş bir varlıktaki değer düşüklüğü zararı, o varlığa ilişkin yeniden değerleme değer artışı ölçüsünde diğer kapsamlı gelirde muhasebeleştirilir (yeniden değerleme azalışı gibi). Değer artışını aşan kısım kâr veya zarara yansıtılır.",
  "TMS 36 - yeniden değerlenmiş varlıkta zarar")

q("Aşağıdakilerden hangileri belirti aranmaksızın yıllık değer düşüklüğü testine tabidir?\n\nI. Sınırsız faydalı ömre sahip maddi olmayan duran varlıklar\n\nII. Henüz kullanıma hazır olmayan maddi olmayan duran varlıklar\n\nIII. İşletme birleşmesinde edinilen şerefiye",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 36 üçünü de belirtiden bağımsız olarak yıllık teste tabi tutar: sınırsız ömürlü maddi olmayan duran varlıklar (I), henüz kullanıma hazır olmayanlar (II) ve işletme birleşmesinde edinilen şerefiye (III).",
  "TMS 36 - yıllık zorunlu test")

q("Aşağıdaki ifadelerden hangileri TMS 36 bakımından doğrudur?\n\nI. Geri kazanılabilir tutar, GUD eksi satış maliyetleri ile kullanım değerinden yüksek olanıdır\n\nII. Değer düşüklüğü zararı geri kazanılabilir tutarın defter değerini aşan kısmıdır\n\nIII. Geri kazanılabilir tutar her hâlde kullanım değeridir",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Geri kazanılabilir tutar iki ölçüden yüksek olanıdır (I). Değer düşüklüğü zararı II'deki gibi tersine değil, defter değerinin geri kazanılabilir tutarı aşan kısmıdır. Tutar her durumda kullanım değerine eşit olmadığından III de yanlıştır. Yalnız I doğrudur.",
  "TMS 36 - temel kavramlar")

# ── B. Ölçüm ve hesaplama (16) ─────────────────────────────────────────────
ddg, ku, dd = 380_000, 420_000, 500_000
gkt = max(ddg, ku)
zarar = dd - gkt
q(f"Bir makinenin defter değeri {tr(dd)} TL'dir. Gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarı {tr(ddg)} TL, kullanım değeri {tr(ku)} TL'dir. TMS 36'ya göre muhasebeleştirilecek değer düşüklüğü zararı kaç TL'dir?",
  f"{tr(zarar)} TL",
  [f"{tr(dd - ddg)} TL", f"{tr(ku - ddg)} TL", f"{tr(dd)} TL", "0 TL"],
  f"Geri kazanılabilir tutar = max(GUD − satış maliyetleri; kullanım değeri) = max({tr(ddg)}; {tr(ku)}) = {tr(gkt)} TL. Değer düşüklüğü zararı = Defter değeri − Geri kazanılabilir tutar = {tr(dd)} − {tr(gkt)} = {tr(zarar)} TL. Düşük olan {tr(ddg)} TL değil, YÜKSEK olan alınır.",
  "TMS 36 - değer düşüklüğü hesabı")

ddg2, ku2, dd2 = 640_000, 600_000, 700_000
gkt2 = max(ddg2, ku2)
zarar2 = dd2 - gkt2
q(f"Bir binanın defter değeri {tr(dd2)} TL'dir. Gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarı {tr(ddg2)} TL, kullanım değeri {tr(ku2)} TL'dir. Muhasebeleştirilecek değer düşüklüğü zararı kaç TL'dir?",
  f"{tr(zarar2)} TL",
  [f"{tr(dd2 - ku2)} TL", f"{tr(ddg2 - ku2)} TL", f"{tr(dd2)} TL", "0 TL"],
  f"Geri kazanılabilir tutar = max({tr(ddg2)}; {tr(ku2)}) = {tr(gkt2)} TL. Zarar = {tr(dd2)} − {tr(gkt2)} = {tr(zarar2)} TL. Burada yüksek olan GUD eksi satış maliyetleridir; kullanım değeri değil.",
  "TMS 36 - değer düşüklüğü hesabı")

ddg3, ku3, dd3 = 520_000, 560_000, 480_000
q(f"Bir makinenin defter değeri {tr(dd3)} TL, gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarı {tr(ddg3)} TL ve kullanım değeri {tr(ku3)} TL'dir. TMS 36'ya göre aşağıdakilerden hangisi doğrudur?",
  "Değer düşüklüğü yoktur; geri kazanılabilir tutar defter değerini aşmaktadır",
  [f"{tr(dd3 - ddg3) if dd3 > ddg3 else tr(ddg3 - dd3)} TL değer düşüklüğü zararı muhasebeleştirilmek zorunda tutulmaktadır",
   f"{tr(ku3 - dd3)} TL değer artışı gelir olarak kâr veya zarara yansıtılmak zorunda kalınmaktadır",
   "Varlık her hâlde kullanım değeriyle yeniden ölçülmek zorunda olup fark gelir yazılmaktadır",
   "Varlık her hâlde bilanço dışı bırakılmak zorunda olup defter değeri sıfırlanmak durumundadır"],
  f"Geri kazanılabilir tutar = max({tr(ddg3)}; {tr(ku3)}) = {tr(max(ddg3, ku3))} TL. Bu tutar defter değeri {tr(dd3)} TL'yi aştığından değer düşüklüğü YOKTUR. TMS 36 yalnızca değer DÜŞÜKLÜĞÜ ile ilgilenir; defter değeri geri kazanılabilir tutara yükseltilmez, değer artışı kaydedilmez.",
  "TMS 36 - değer düşüklüğü olmayan hâl")

q("Kullanım değerinin hesaplanmasında dikkate alınacak unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki nakit akışları tahmini ve bunlara uygulanacak iskonto oranı dikkate alınır",
  ["Yalnızca varlığın piyasa fiyatı dikkate alınır; nakit akışları hiç hesaba katılmamaktadır",
   "Yalnızca varlığın ilk maliyeti dikkate alınır; gelecekteki akışlar hiç dikkate alınmaz",
   "Yalnızca varlığın birikmiş amortismanı dikkate alınır; başka bir unsur hesaba katılmaz",
   "Kullanım değerinin hesabı TMS 36'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 36: kullanım değerinin hesaplanmasında (a) varlıktan elde edilmesi beklenen gelecekteki nakit akışlarının tahmin edilmesi ve (b) bu akışlara paranın zaman değeri ile varlığa özgü riskleri yansıtan uygun iskonto oranının uygulanması unsurları yer alır.",
  "TMS 36 - kullanım değerinin unsurları")

q("Kullanım değeri hesabında kullanılacak iskonto oranı bakımından aşağıdakilerden hangisi doğrudur?",
  "Paranın zaman değeri ile varlığa özgü riskleri yansıtan vergi öncesi orandır",
  ["Her hâlde işletmenin ortalama borçlanma maliyetini yansıtan vergi sonrası oran kullanılmaktadır",
   "Her hâlde merkez bankasının ilan ettiği politika faizi oranı kullanılmak zorunda tutulmuştur",
   "İskonto oranı kullanılmaz; gelecekteki nakit akışları nominal tutarlarıyla toplanmaktadır",
   "İskonto oranının belirlenmesi TMS 36'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 36: iskonto oranı, paranın zaman değerine ve varlığa özgü risklere ilişkin cari piyasa değerlendirmelerini yansıtan VERGİ ÖNCESİ orandır. Nakit akışı tahminlerinde düzeltilmiş riskler, iskonto oranında tekrar dikkate alınmaz.",
  "TMS 36 - iskonto oranı")

q("Kullanım değeri hesabındaki nakit akışı tahminleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın mevcut durumuna dayanır; henüz taahhüt edilmemiş yeniden yapılandırma veya iyileştirme etkileri dâhil edilmez",
  ["Planlanan tüm iyileştirme ve yeniden yapılandırmaların etkileri her hâlde dâhil edilmektedir",
   "Yalnızca geçmiş dönemlerin fiilî nakit akışları dikkate alınır; gelecek tahmini yapılmaz",
   "Nakit akışı tahminleri her hâlde en iyimser senaryoya göre yapılmak zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: gelecekteki nakit akışı tahminleri varlığın mevcut durumuna dayandırılır. Bu tahminler, işletmenin henüz taahhüt etmediği bir yeniden yapılandırmadan veya varlığın performansının iyileştirilmesinden kaynaklanacak tahmini gelecekteki nakit giriş ya da çıkışlarını içermez.",
  "TMS 36 - nakit akışı tahminleri")

q("Kullanım değeri hesabında finansman faaliyetleri ve gelir vergisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansman faaliyetlerinden nakit akışları ile gelir vergisi tahsilat ve ödemeleri dâhil edilmez",
  ["Finansman nakit akışları ve gelir vergisi her hâlde hesaba dâhil edilmek zorunda tutulmaktadır",
   "Yalnızca finansman nakit akışları dâhil edilir; gelir vergisi hiçbir hâlde dâhil edilmemektedir",
   "Yalnızca gelir vergisi dâhil edilir; finansman nakit akışları hiçbir hâlde dâhil edilmemektedir",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: gelecekteki nakit akışı tahminleri, finansman faaliyetlerinden kaynaklanan nakit giriş ve çıkışları ile gelir vergisi tahsilat veya ödemelerini içermez. İskonto oranı vergi öncesi olduğundan vergi çift sayılmaz.",
  "TMS 36 - hesaba dâhil edilmeyen akışlar")

q("Değer düşüklüğü zararının muhasebeleştirilmesinden sonraki amortisman bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltilmiş defter değeri kalan faydalı ömre sistematik olarak dağıtılır",
  ["Amortisman her hâlde eski defter değeri üzerinden hesaplanmaya devam edilmek zorundadır",
   "Değer düşüklüğü sonrası hiçbir hâlde amortisman ayrılmaz; varlık itfa edilmeden bırakılır",
   "Amortisman her hâlde varlığın ilk maliyeti üzerinden hesaplanmak zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: bir değer düşüklüğü zararının muhasebeleştirilmesinden sonra, varlığın amortismanı, düzeltilmiş defter değerinden varsa kalıntı değeri düşülerek kalan faydalı ömrüne sistematik biçimde dağıtılacak biçimde gelecek dönemlerde düzeltilir.",
  "TMS 36 - sonraki amortisman")

dd4, gkt4, kalan_om = 900_000, 600_000, 6
yeni_amort = gkt4 / kalan_om
q(f"Bir makinenin defter değeri {tr(dd4)} TL iken geri kazanılabilir tutarı {tr(gkt4)} TL olarak belirlenmiş ve değer düşüklüğü muhasebeleştirilmiştir. Kalıntı değer sıfır ve kalan faydalı ömür {kalan_om} yıldır. Değer düşüklüğü sonrası yıllık amortisman gideri kaç TL'dir?",
  f"{tr(yeni_amort)} TL",
  [f"{tr(dd4 / kalan_om)} TL", f"{tr((dd4 - gkt4) / kalan_om)} TL", f"{tr(gkt4)} TL", f"{tr(dd4 - gkt4)} TL"],
  f"Değer düşüklüğü sonrası amortisman, DÜZELTİLMİŞ defter değeri üzerinden hesaplanır. Düzeltilmiş defter değeri = geri kazanılabilir tutar = {tr(gkt4)} TL. Yıllık amortisman = {tr(gkt4)} ÷ {kalan_om} = {tr(yeni_amort)} TL. Eski defter değeri {tr(dd4)} TL artık kullanılmaz.",
  "TMS 36 - değer düşüklüğü sonrası amortisman")

q("Bireysel bir varlık için geri kazanılabilir tutarın tahmin edilemediği hâl bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın ait olduğu nakit yaratan birimin geri kazanılabilir tutarı belirlenir",
  ["Bu durumda hiçbir hâlde değer düşüklüğü testi yapılamaz; varlık test dışı bırakılmaktadır",
   "Bu durumda varlık her hâlde bilanço dışı bırakılmak zorunda olup defter değeri sıfırlanır",
   "Bu durumda varlık her hâlde gerçeğe uygun değeriyle ölçülmek zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: bireysel bir varlığın geri kazanılabilir tutarının tahmin edilmesi mümkün değilse, işletme varlığın ait olduğu nakit yaratan birimin geri kazanılabilir tutarını belirler. Varlık, diğer varlıklardan büyük ölçüde bağımsız nakit girişi sağlamıyorsa bu duruma girilir.",
  "TMS 36 - nakit yaratan birime geçiş")

q("Nakit yaratan birimde değer düşüklüğü zararının dağıtımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Önce varsa birime dağıtılmış şerefiyeye, sonra diğer varlıklara defter değerleri oranında dağıtılır",
  ["Zarar her hâlde tüm varlıklara eşit tutarlarda paylaştırılmak zorunda tutulmaktadır",
   "Zarar her hâlde önce maddi duran varlıklara dağıtılır; şerefiye en sona bırakılmaktadır",
   "Zarar hiçbir varlığa dağıtılmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Zararın dağıtımı TMS 36'da düzenlenmemiş olup işletmenin takdirine bırakılmış bulunmaktadır"],
  "TMS 36: nakit yaratan birimin değer düşüklüğü zararı, (a) önce birime dağıtılmış olan şerefiyenin defter değerinin azaltılmasında, (b) sonra birimdeki diğer varlıklara defter değerleri oranında dağıtılarak kullanılır.",
  "TMS 36 - NYB'de zarar dağıtımı")

q("Nakit yaratan birimdeki bir varlığın defter değerinin indirilebileceği alt sınır bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın GUD eksi satış maliyetleri, kullanım değeri ve sıfırdan yüksek olanının altına indirilemez",
  ["Varlığın defter değeri her hâlde sıfıra kadar indirilebilmek zorunda tutulan bir tutarı ifade eder",
   "Varlığın defter değeri hiçbir hâlde indirilemez; zarar yalnızca şerefiyeden düşülmektedir",
   "Varlığın defter değeri her hâlde negatif değere kadar indirilebilmek zorunda bulunmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: zararın dağıtımında bir varlığın defter değeri, (a) gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarı, (b) kullanım değeri ve (c) sıfırdan YÜKSEK olanının altına indirilemez. Aksi hâlde dağıtılamayan tutar diğer varlıklara oranlanır.",
  "TMS 36 - dağıtımın alt sınırı")

nyb_ser, nyb_diger, nyb_gkt = 100_000, 500_000, 480_000
nyb_dd = nyb_ser + nyb_diger
nyb_zarar = nyb_dd - nyb_gkt
kalan_zarar = nyb_zarar - nyb_ser
q(f"Bir nakit yaratan birimin defter değeri {tr(nyb_dd)} TL olup bunun {tr(nyb_ser)} TL'si şerefiye, {tr(nyb_diger)} TL'si diğer varlıklardır. Birimin geri kazanılabilir tutarı {tr(nyb_gkt)} TL'dir. Şerefiyeye dağıtılacak değer düşüklüğü zararı kaç TL'dir?",
  f"{tr(nyb_ser)} TL",
  [f"{tr(nyb_zarar)} TL", f"{tr(kalan_zarar)} TL", f"{tr(nyb_zarar / 2)} TL", "0 TL"],
  f"Toplam zarar = {tr(nyb_dd)} − {tr(nyb_gkt)} = {tr(nyb_zarar)} TL. Zarar ÖNCE şerefiyeye dağıtılır; şerefiye {tr(nyb_ser)} TL olduğundan tamamı silinir. Kalan {tr(kalan_zarar)} TL diğer varlıklara defter değerleri oranında dağıtılır. Şerefiyeye düşen: {tr(nyb_ser)} TL.",
  "TMS 36 - şerefiyeye dağıtım hesabı")

q("Şerefiyenin değer düşüklüğü testi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme birleşmesinde edinilen şerefiye, yarar sağlaması beklenen nakit yaratan birimlere dağıtılır",
  ["Şerefiye hiçbir hâlde nakit yaratan birimlere dağıtılamaz; bireysel olarak test edilmektedir",
   "Şerefiye her hâlde işletmenin tüm birimlerine eşit tutarlarda dağıtılmak zorunda tutulur",
   "Şerefiye hiçbir hâlde değer düşüklüğü testine tabi tutulmaz; süresiz olarak korunmaktadır",
   "Şerefiyenin testi TMS 36'da düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: değer düşüklüğü testi amacıyla işletme birleşmesinde edinilen şerefiye, birleşmenin sinerjilerinden yararlanması beklenen edinen işletmenin her bir nakit yaratan birimine dağıtılır. Şerefiye tek başına nakit yaratmadığından bireysel test edilemez.",
  "TMS 36 - şerefiyenin dağıtımı")

q("Aşağıdaki ifadelerden hangileri değer düşüklüğü ölçümü bakımından doğrudur?\n\nI. Geri kazanılabilir tutar iki ölçüden yüksek olanıdır\n\nII. İki tutardan biri defter değerini aşarsa diğerini hesaplamaya gerek yoktur\n\nIII. Kullanım değeri hesabına gelir vergisi ödemeleri dâhil edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Geri kazanılabilir tutar iki ölçüden yüksek olanıdır (I) ve biri defter değerini aşarsa diğerini hesaplamaya gerek yoktur (II). Kullanım değeri hesabına gelir vergisi tahsilat ve ödemeleri DÂHİL EDİLMEZ; iskonto oranı vergi öncesidir. Bu nedenle III yanlıştır.",
  "TMS 36 - ölçüm")

q("Aşağıdaki ifadelerden hangileri nakit yaratan birim bakımından doğrudur?\n\nI. Zarar önce şerefiyeye dağıtılır\n\nII. Kalan zarar diğer varlıklara defter değerleri oranında dağıtılır\n\nIII. Bir varlığın defter değeri kullanım değerinin altına indirilebilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Zarar önce şerefiyeye (I), kalanı diğer varlıklara defter değerleri oranında (II) dağıtılır. Bir varlığın defter değeri GUD eksi satış maliyetleri, kullanım değeri ve sıfırdan yüksek olanının ALTINA İNDİRİLEMEZ; bu nedenle III yanlıştır.",
  "TMS 36 - NYB'de dağıtım")

# ── C. Değer düşüklüğünün iptali (16) ──────────────────────────────────────
q("Değer düşüklüğü zararının iptali bakımından aşağıdakilerden hangisi doğrudur?",
  "Geri kazanılabilir tutarın belirlenmesinde kullanılan tahminlerde değişiklik olmuşsa iptal edilir",
  ["Değer düşüklüğü zararı hiçbir hâlde iptal edilemez; kalıcı olarak kayıtlarda kalmaktadır",
   "Değer düşüklüğü zararı her hâlde ve koşulsuz olarak izleyen dönemde iptal edilmek zorundadır",
   "İptal yalnızca vergi idaresi izin verdiğinde yapılabilen bir işlemi ifade etmektedir",
   "Değer düşüklüğünün iptali TMS 36'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 36: işletme her raporlama dönemi sonunda, şerefiye dışındaki bir varlık için geçmiş dönemlerde muhasebeleştirilmiş değer düşüklüğü zararının artık mevcut olmayabileceğine veya azalmış olabileceğine ilişkin belirti olup olmadığını değerlendirir. Belirti varsa geri kazanılabilir tutar tahmin edilir.",
  "TMS 36 - iptalin koşulu")

q("Şerefiyeye ilişkin değer düşüklüğü zararının iptali bakımından aşağıdakilerden hangisi doğrudur?",
  "Şerefiyeye ilişkin değer düşüklüğü zararı izleyen dönemlerde iptal edilmez",
  ["Şerefiyedeki değer düşüklüğü zararı her hâlde ve koşulsuz olarak iptal edilmek zorundadır",
   "Şerefiyedeki değer düşüklüğü zararı yalnızca vergi idaresi izin verdiğinde iptal edilmektedir",
   "Şerefiyedeki değer düşüklüğü zararı diğer varlıklarla aynı esaslara göre iptal edilebilmektedir",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: ŞEREFİYEYE ilişkin olarak muhasebeleştirilmiş bir değer düşüklüğü zararı izleyen dönemlerde İPTAL EDİLMEZ. Sonraki artışlar, muhtemelen işletme içi yaratılan şerefiyenin artışıdır ve TMS 38 uyarınca muhasebeleştirilemez. Bu, iptal kuralının en önemli istisnasıdır.",
  "TMS 36 - şerefiyede iptal yasağı")

q("Değer düşüklüğü iptalinin üst sınırı bakımından aşağıdakilerden hangisi doğrudur?",
  "Değer düşüklüğü hiç muhasebeleştirilmemiş olsaydı bulunacak defter değeri aşılamaz",
  ["İptal sonrası defter değeri her hâlde varlığın ilk maliyetine yükseltilmek zorunda kalınır",
   "İptal sonrası defter değeri her hâlde geri kazanılabilir tutara yükseltilmek zorunda tutulur",
   "İptal için hiçbir üst sınır bulunmayıp defter değeri sınırsızca artırılabilmektedir",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: değer düşüklüğü zararının iptali nedeniyle artırılan defter değeri, geçmiş yıllarda hiç değer düşüklüğü zararı muhasebeleştirilmemiş olsaydı belirlenmiş olacak defter değerini (amortisman düşülmüş net tutarı) AŞAMAZ. Bu, iptalin tavanıdır.",
  "TMS 36 - iptalin üst sınırı")

q("Değer düşüklüğü iptalinin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet modelinde derhâl kâr veya zarara yansıtılır",
  ["Her hâlde doğrudan özkaynağa kaydedilmek zorunda olan bir kalemi ifade etmektedir",
   "Her hâlde gelecek dönemlere yayılarak sistematik biçimde gelir yazılmak zorunda kalınır",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "İptalin muhasebeleştirilmesi TMS 36'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 36: değer düşüklüğü zararının iptali, varlık yeniden değerlenmiş tutarı üzerinden gösterilmedikçe derhâl kâr veya zararda muhasebeleştirilir. Yeniden değerlenmiş varlıklarda ise iptal, yeniden değerleme artışı olarak diğer kapsamlı gelirde muhasebeleştirilir.",
  "TMS 36 - iptalin muhasebeleştirilmesi")

ilk_mal, ilk_om, gecen36 = 800_000, 8, 2
yil_ilk = ilk_mal / ilk_om
dd_zaman = ilk_mal - yil_ilk * gecen36
gkt_dus = 480_000
tavan_om_kalan = ilk_om - (gecen36 + 1)
tavan = ilk_mal - yil_ilk * (gecen36 + 1)
q(f"Maliyeti {tr(ilk_mal)} TL, faydalı ömrü {ilk_om} yıl olan bir makine doğrusal amortismana tabidir (kalıntı değer sıfır). {gecen36}. yıl sonunda değer düşüklüğü muhasebeleştirilmiştir. {gecen36+1}. yıl sonunda değer düşüklüğü ortadan kalkmışsa, iptal sonrası defter değeri EN FAZLA kaç TL olabilir?",
  f"{tr(tavan)} TL",
  [f"{tr(ilk_mal)} TL",                                  # hiç amortisman düşülmedi
   f"{tr(dd_zaman)} TL",                                 # 3. yılın amortismanı unutuldu
   f"{tr(gkt_dus)} TL",                                  # düşürülmüş defter değeri sanıldı
   f"{tr(ilk_mal - yil_ilk * (gecen36 + 2))} TL"],       # bir yıl fazla amortisman düşüldü
  f"İptal tavanı, değer düşüklüğü HİÇ muhasebeleştirilmemiş olsaydı bulunacak defter değeridir. Yıllık amortisman = {tr(ilk_mal)} ÷ {ilk_om} = {tr(yil_ilk)} TL. {gecen36+1}. yıl sonunda birikmiş = {tr(yil_ilk)} × {gecen36+1} = {tr(yil_ilk * (gecen36+1))} TL. Tavan = {tr(ilk_mal)} − {tr(yil_ilk * (gecen36+1))} = {tr(tavan)} TL.",
  "TMS 36 - iptal tavanı hesabı")

q("Değer düşüklüğü iptalinden sonraki amortisman bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltilmiş defter değeri kalan faydalı ömre sistematik olarak dağıtılır",
  ["Amortisman her hâlde iptal öncesi düşük defter değeri üzerinden hesaplanmaya devam edilir",
   "İptal sonrası hiçbir hâlde amortisman ayrılmaz; varlık itfa edilmeden bırakılmak zorundadır",
   "Amortisman her hâlde varlığın ilk maliyeti üzerinden hesaplanmak zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: bir değer düşüklüğü zararının iptalinin muhasebeleştirilmesinden sonra, varlığın amortismanı, düzeltilmiş defter değerinden varsa kalıntı değer düşülerek kalan faydalı ömrüne sistematik biçimde dağıtılacak biçimde gelecek dönemlerde düzeltilir.",
  "TMS 36 - iptal sonrası amortisman")

q("Nakit yaratan birimde değer düşüklüğü iptalinin dağıtımı bakımından aşağıdakilerden hangisi doğrudur?",
  "İptal, birimdeki varlıklara (şerefiye hariç) defter değerleri oranında dağıtılır",
  ["İptal her hâlde önce şerefiyeye dağıtılmak zorunda olup diğer varlıklar sonra gelmektedir",
   "İptal her hâlde tüm varlıklara eşit tutarlarda paylaştırılmak zorunda tutulmaktadır",
   "İptal hiçbir varlığa dağıtılmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: nakit yaratan birime ilişkin değer düşüklüğü zararının iptali, birimin şerefiye DIŞINDAKİ varlıklarına defter değerleri oranında dağıtılır. Şerefiyeye ilişkin değer düşüklüğü zararı iptal edilmediğinden şerefiye bu dağıtıma girmez.",
  "TMS 36 - NYB'de iptalin dağıtımı")

q("Değer düşüklüğü iptali belirtileri bakımından aşağıdakilerden hangisi doğrudur?",
  "Piyasa değerinde önemli artış ve olumlu çevresel değişiklikler gibi dış ve iç belirtiler değerlendirilir",
  ["İptal belirtisi diye bir kavram bulunmayıp iptal her hâlde koşulsuz olarak yapılmaktadır",
   "Yalnızca varlığın satılması hâlinde iptal belirtisi doğabilmek zorunda bulunmaktadır",
   "İptal belirtileri yalnızca vergi idaresi tarafından belirlenebilen bir husus niteliğindedir",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: iptal belirtileri, değer düşüklüğü belirtilerinin aynasıdır. Dış kaynaklı: varlığın piyasa değerinde önemli artış, teknolojik/piyasa/ekonomik/hukuki çevrede olumlu değişiklikler, piyasa faiz oranlarında düşüş. İç kaynaklı: varlığın kullanım biçiminde olumlu değişiklikler, ekonomik performansın beklenenden iyi olması.",
  "TMS 36 - iptal belirtileri")

q("Bir işletme, geçen yıl değer düşüklüğü muhasebeleştirdiği bir makinenin geri kazanılabilir tutarının bu yıl arttığını tespit etmiştir. TMS 36 bakımından aşağıdakilerden hangisi doğrudur?",
  "Tahminlerde değişiklik varsa iptal edilir; ancak hiç zarar yazılmasaydı bulunacak defter değeri aşılamaz",
  ["Değer düşüklüğü hiçbir hâlde iptal edilemez; zarar kalıcı olarak kayıtlarda kalmak zorundadır",
   "Defter değeri her hâlde geri kazanılabilir tutara yükseltilmek zorunda olup sınır aranmamaktadır",
   "Defter değeri her hâlde varlığın ilk maliyetine yükseltilmek zorunda tutulan bir işlemi ifade eder",
   "İptal her hâlde doğrudan özkaynağa kaydedilmek zorunda olan bir kalemi ifade etmektedir"],
  "TMS 36: şerefiye dışındaki varlıklarda, geri kazanılabilir tutarın belirlenmesinde kullanılan tahminlerde değişiklik olmuşsa değer düşüklüğü iptal edilir. Ancak artırılan defter değeri, hiç değer düşüklüğü muhasebeleştirilmemiş olsaydı (amortisman düşülmüş) bulunacak defter değerini aşamaz.",
  "TMS 36 - iptal (senaryo)")

q("Bir işletme, işletme birleşmesinde edindiği şerefiye için geçen yıl değer düşüklüğü muhasebeleştirmiştir. Bu yıl ilgili birimin performansı belirgin biçimde iyileşmiştir. TMS 36 bakımından aşağıdakilerden hangisi doğrudur?",
  "Şerefiyeye ilişkin değer düşüklüğü zararı iptal edilmez",
  ["Performans iyileştiğinden zarar her hâlde iptal edilmek zorunda olan bir durumu ifade eder",
   "Zarar iptal edilir ancak yalnızca şerefiyenin ilk maliyetine kadar yükseltilebilmektedir",
   "Zarar her hâlde doğrudan özkaynağa aktarılarak iptal edilmek zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: şerefiyeye ilişkin değer düşüklüğü zararı izleyen dönemlerde İPTAL EDİLMEZ. Sonradan ortaya çıkan artış muhtemelen işletme içinde yaratılan şerefiyenin artışıdır; TMS 38 işletme içi yaratılan şerefiyenin muhasebeleştirilmesini yasaklar.",
  "TMS 36 - şerefiyede iptal yasağı (senaryo)")

q("Aşağıdaki ifadelerden hangileri değer düşüklüğünün iptali bakımından doğrudur?\n\nI. Şerefiyeye ilişkin değer düşüklüğü zararı iptal edilmez\n\nII. İptal, hiç zarar yazılmasaydı bulunacak defter değerini aşamaz\n\nIII. İptal, maliyet modelinde derhâl kâr veya zarara yansıtılır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üçü de doğrudur: şerefiyedeki zarar iptal edilmez (I), iptal tavanı hiç zarar yazılmasaydı bulunacak defter değeridir (II) ve maliyet modelinde iptal derhâl kâr veya zarara yansıtılır (III).",
  "TMS 36 - iptal")

q("Aşağıdaki ifadelerden hangileri TMS 36 bakımından doğrudur?\n\nI. Değer düşüklüğü sonrası amortisman düzeltilmiş defter değeri üzerinden hesaplanır\n\nII. NYB'de iptal şerefiye dışındaki varlıklara dağıtılır\n\nIII. Değer düşüklüğü zararı hiçbir hâlde iptal edilemez",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Değer düşüklüğü sonrası amortisman düzeltilmiş defter değeri üzerinden hesaplanır (I) ve NYB'de iptal şerefiye dışındaki varlıklara dağıtılır (II). Şerefiye dışındaki varlıklarda değer düşüklüğü zararı İPTAL EDİLEBİLİR; yalnızca şerefiyede iptal yasaktır. Bu nedenle III yanlıştır.",
  "TMS 36 - iptal")

q("TMS 36'ya ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Her varlık sınıfı için muhasebeleştirilen değer düşüklüğü zararı ve iptalleri ile hangi kalemde yer aldığı açıklanır",
  ["Değer düşüklüğü hakkında hiçbir açıklama yapılmaz; yalnızca tutar bilançoda gösterilmektedir",
   "Yalnızca toplam değer düşüklüğü tutarı açıklanır; sınıf bazında hiçbir bilgi verilmemektedir",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca şerefiyesi bulunan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 36: işletme her varlık sınıfı için dönem içinde kâr veya zararda muhasebeleştirilen değer düşüklüğü zararı tutarını ve bu zararların yer aldığı kalemleri, iptal edilen değer düşüklüğü zararı tutarlarını ve diğer kapsamlı gelirde muhasebeleştirilenleri açıklar.",
  "TMS 36 - açıklamalar")

q("TMS 36'nın kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Stoklar, ertelenmiş vergi varlıkları ve TFRS 9 kapsamındaki finansal varlıklar kapsam dışıdır",
  ["TMS 36 istisnasız tüm varlıklara uygulanır; hiçbir varlık kapsam dışında bırakılmamaktadır",
   "TMS 36 yalnızca stoklara uygulanır; duran varlıklar kapsam dışında bırakılmış bulunmaktadır",
   "TMS 36 yalnızca finansal varlıklara uygulanır; diğer varlıklar kapsam dışı tutulmuştur",
   "TMS 36'nın kapsamı Standartta düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: bu Standart, başka Standartlarda değer düşüklüğü hükümleri bulunan varlıklara uygulanmaz. Stoklar (TMS 2), inşaat sözleşmelerinden alacaklar, ertelenmiş vergi varlıkları (TMS 12), çalışanlara sağlanan faydalardan doğan varlıklar, TFRS 9 kapsamındaki finansal varlıklar, TMS 40 uyarınca GUD ile ölçülen yatırım amaçlı gayrimenkuller kapsam dışıdır.",
  "TMS 36 - kapsam")

q("Bir işletmenin sınırsız ömürlü bir markası bulunmakta ancak değer düşüklüğü belirtisi görülmemektedir. TMS 36 bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirti olmasa da yıllık olarak değer düşüklüğü testine tabi tutulur",
  ["Belirti bulunmadığından hiçbir hâlde test yapılmasına gerek bulunmamak durumundadır",
   "Marka her hâlde itfa edilmek zorunda olup değer düşüklüğü testi uygulanmamaktadır",
   "Test yalnızca marka satılırken yapılmak zorunda olup elde tutulurken aranmamaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: sınırsız faydalı ömre sahip maddi olmayan duran varlıklar, değer düşüklüğü belirtisi olsun olmasın YILLIK olarak değer düşüklüğü testine tabi tutulur. Bu varlıklar itfa edilmediğinden yıllık test, defter değerinin kontrol edilmesini sağlar.",
  "TMS 36 - sınırsız ömürlü varlıkta yıllık test (senaryo)")

q("Aşağıdakilerden hangileri TMS 36 kapsamı DIŞINDADIR?\n\nI. Stoklar\n\nII. Ertelenmiş vergi varlıkları\n\nIII. Maddi duran varlıklar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Stoklar TMS 2'de (I) ve ertelenmiş vergi varlıkları TMS 12'de (II) kendi değer düşüklüğü hükümlerine sahip olduğundan TMS 36 kapsamı dışındadır. Maddi duran varlıklar (III) ise TMS 36 KAPSAMINDADIR; TMS 16 değer düşüklüğü için TMS 36'ya yollama yapar.",
  "TMS 36 - kapsam")

# ── D. Ek konular: GUD, ortak varlıklar, projeksiyon, test zamanı (14) ─────
q("Gerçeğe uygun değerden satış maliyetleri düşülmüş tutar bakımından aşağıdakilerden hangisi doğrudur?",
  "Piyasa katılımcıları arasındaki satış fiyatından elden çıkarma maliyetleri düşülerek bulunur",
  ["Varlıktan beklenen gelecekteki nakit akışlarının bugünkü değerini ifade eden bir ölçüdür",
   "Varlığın birikmiş amortismanı düşülmüş defter değerini ifade eden bir ölçüyü karşılamaktadır",
   "Varlığın ilk edinildiği tarihteki maliyet bedelini ifade eden bir ölçüyü karşılamak zorundadır",
   "Bu kavram TMS 36'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 36: gerçeğe uygun değer TFRS 13 uyarınca ölçülür; ölçüm tarihinde piyasa katılımcıları arasındaki olağan bir işlemde varlığın satışından elde edilecek fiyattır. Bundan elden çıkarma maliyetleri düşülerek ilgili tutara ulaşılır.",
  "TMS 36 - GUD eksi satış maliyetleri")

q("Satış (elden çıkarma) maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansman maliyetleri ve gelir vergisi gideri dışında, elden çıkarmaya doğrudan atfedilebilir maliyetlerdir",
  ["İşletmenin tüm genel yönetim giderlerini kapsayan geniş bir kavramı ifade etmek zorundadır",
   "Finansman maliyetleri ve gelir vergisi gideri de dâhil olmak üzere her türlü gideri kapsar",
   "Yalnızca varlığın taşınma maliyetini kapsayan ve başka hiçbir unsuru içermeyen bir kavramdır",
   "Satış maliyetleri TMS 36'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: elden çıkarma maliyetleri, finansman maliyetleri ve gelir vergisi gideri dışında, bir varlığın veya nakit yaratan birimin elden çıkarılmasıyla doğrudan ilişkilendirilebilen ek maliyetlerdir (hukuki masraflar, damga vergisi, taşıma maliyetleri gibi).",
  "TMS 36 - elden çıkarma maliyetleri")

q("Kullanım değeri hesabında nakit akışı projeksiyonlarının dönemi bakımından aşağıdakilerden hangisi doğrudur?",
  "En fazla beş yıllık bütçe veya tahminlere dayandırılır; daha uzun süre için gerekçe aranır",
  ["Projeksiyonlar her hâlde en az yirmi yıllık dönemi kapsamak zorunda tutulmaktadır",
   "Projeksiyonlar yalnızca bir yıllık dönemi kapsayabilir; daha uzun süre hiçbir hâlde kullanılamaz",
   "Projeksiyon dönemi için hiçbir sınır bulunmayıp işletme dilediği süreyi serbestçe seçebilmektedir",
   "Bu husus TMS 36'da düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 36: nakit akışı projeksiyonları, yönetim tarafından onaylanmış en fazla BEŞ YILLIK bütçe veya tahminlere dayandırılır. Yönetimin daha uzun bir dönem için güvenilir tahmin yapabildiğini gösterebilmesi ve geçmiş deneyimin bunu doğrulaması hâlinde daha uzun bir dönem kullanılabilir.",
  "TMS 36 - projeksiyon dönemi")

q("Beş yılı aşan dönemler için nakit akışı tahminleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Sabit veya azalan bir büyüme oranı kullanılarak tahmin edilir; artan oran gerekçelendirilmelidir",
  ["Her hâlde sürekli artan bir büyüme oranı kullanılmak zorunda tutulan bir yöntemi ifade eder",
   "Beş yılı aşan dönemler için hiçbir hâlde tahmin yapılamaz; hesap beş yılla sınırlı kalmaktadır",
   "Her hâlde işletmenin son yıldaki büyüme oranı sonsuza kadar aynen sürdürülmek zorundadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: en son bütçe/tahminlerin ötesindeki nakit akışları, sabit veya azalan bir büyüme oranı kullanılarak tahmin edilir. Bu oran, ürün/sektör/ülke için uzun dönemli ortalama büyüme oranını aşmamalıdır; artan oran kullanımı gerekçelendirilmelidir.",
  "TMS 36 - büyüme oranı varsayımı")

q("TMS 36'ya göre ortak varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Şerefiye dışındaki, birden fazla nakit yaratan birimin nakit akışına katkıda bulunan varlıklardır",
  ["İşletmenin ortaklarına ait olan ve işletmeye tahsis edilen varlıkları ifade eden bir kavramdır",
   "İşletmenin başka işletmelerle müştereken sahip olduğu varlıkları ifade eden bir kavramı karşılar",
   "İşletmenin yalnızca tek bir nakit yaratan birime hizmet eden varlıklarını ifade etmektedir",
   "Ortak varlık kavramı TMS 36'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 36: ortak varlıklar, şerefiye dışındaki, hem incelenen nakit yaratan birimin hem de diğer nakit yaratan birimlerin gelecekteki nakit akışlarına katkıda bulunan varlıklardır (genel merkez binası, bilgi işlem merkezi gibi).",
  "TMS 36 - ortak varlıklar")

q("Ortak varlıkların değer düşüklüğü testi bakımından aşağıdakilerden hangisi doğrudur?",
  "Makul ve tutarlı bir esasla nakit yaratan birimlere dağıtılır; dağıtılamıyorsa daha büyük birim grubu test edilir",
  ["Ortak varlıklar her hâlde bireysel olarak test edilir; birimlere hiç dağıtılmamaktadır",
   "Ortak varlıklar hiçbir hâlde değer düşüklüğü testine tabi tutulamayan kalemleri ifade eder",
   "Ortak varlıklar her hâlde tüm birimlere eşit tutarlarda dağıtılmak zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: ortak varlıklar büyük ölçüde bağımsız nakit girişi sağlamadığından bireysel geri kazanılabilir tutarları belirlenemez. Makul ve tutarlı bir esasla ilgili nakit yaratan birime dağıtılabiliyorsa birim o şekilde test edilir; dağıtılamıyorsa ortak varlığın dağıtılabildiği en küçük birim grubu test edilir.",
  "TMS 36 - ortak varlıkların testi")

q("Sınırsız ömürlü maddi olmayan duran varlığın yıllık testinin zamanlaması bakımından aşağıdakilerden hangisi doğrudur?",
  "Yıl içinde herhangi bir tarihte yapılabilir; ancak her yıl aynı tarihte yapılır",
  ["Her hâlde ve istisnasız raporlama dönemi sonunda yapılmak zorunda tutulan bir işlemdir",
   "Her yıl farklı bir tarihte yapılmak zorunda olup tutarlılık aranmayan bir husustur",
   "Yalnızca vergi idaresinin belirlediği tarihte yapılabilen bir işlemi ifade etmek durumundadır",
   "Testin zamanlaması TMS 36'da düzenlenmemiş bir husus niteliğinde bulunmak durumundadır"],
  "TMS 36: sınırsız faydalı ömre sahip bir maddi olmayan duran varlığın değer düşüklüğü testi yıllık dönem içinde herhangi bir zamanda yapılabilir; ancak her yıl AYNI zamanda yapılır. Farklı maddi olmayan duran varlıklar farklı zamanlarda test edilebilir.",
  "TMS 36 - testin zamanlaması")

q("Şerefiyenin dağıtıldığı nakit yaratan birimin büyüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Birim, işletmenin iç raporlamasında izlenen en küçük düzeyi aşamaz ve faaliyet bölümünden büyük olamaz",
  ["Şerefiye her hâlde işletmenin bütününe dağıtılmak zorunda olup birim ayrımı yapılmamaktadır",
   "Şerefiyenin dağıtılacağı birimin büyüklüğü için hiçbir sınır bulunmayıp serbestçe seçilir",
   "Şerefiye her hâlde en küçük tek bir varlığa dağıtılmak zorunda tutulan bir kalemi ifade eder",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: şerefiyenin dağıtıldığı her bir birim veya birim grubu, (a) işletme içi yönetim amaçlarıyla şerefiyenin izlendiği en küçük düzeyi temsil eder ve (b) TFRS 8 uyarınca belirlenen faaliyet bölümlerinden büyük olamaz.",
  "TMS 36 - şerefiyenin dağıtım düzeyi")

q("Şerefiye dağıtılmış bir nakit yaratan birimin testinin zamanlaması bakımından aşağıdakilerden hangisi doğrudur?",
  "Yıllık olarak ve değer düşüklüğü belirtisi bulunduğunda test edilir; yıllık test her yıl aynı zamanda yapılabilir",
  ["Yalnızca değer düşüklüğü belirtisi bulunduğunda test edilir; yıllık zorunluluk bulunmamaktadır",
   "Yalnızca beş yılda bir test edilmek zorunda olup yıllık test yapılmasına gerek kalmamaktadır",
   "Hiçbir hâlde test edilmez; şerefiye süresiz olarak defter değeriyle korunmak zorundadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 36: şerefiyenin dağıtıldığı bir nakit yaratan birim, yıllık olarak ve birimde değer düşüklüğü olabileceğine ilişkin belirti bulunduğunda test edilir. Yıllık test yıl içinde herhangi bir zamanda yapılabilir; ancak her yıl aynı zamanda yapılır.",
  "TMS 36 - şerefiye testinin zamanlaması")

q("Nakit yaratan birimlerin dönemler arası tutarlılığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Aynı varlık için nakit yaratan birimler dönemden döneme tutarlı biçimde belirlenir",
  ["Nakit yaratan birimler her dönem farklı belirlenmek zorunda olup tutarlılık aranmamaktadır",
   "Nakit yaratan birimler bir kez belirlendikten sonra hiçbir hâlde değiştirilememek durumundadır",
   "Nakit yaratan birimler yalnızca vergi idaresi tarafından belirlenebilen bir husus niteliğindedir",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: aynı varlık veya varlık türleri için nakit yaratan birimler, değişikliğin gerekçelendirilebildiği durumlar dışında dönemden döneme tutarlı biçimde belirlenir. Birimlerin belirlenmesinde değişiklik olmuşsa açıklama yapılır.",
  "TMS 36 - NYB'nin tutarlılığı")

q("Nakit yaratan birimin defter değerinin belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Geri kazanılabilir tutarın belirlenme biçimiyle tutarlı olacak biçimde belirlenir",
  ["Birimin defter değeri her hâlde işletmenin tüm varlıklarının toplamı olmak zorunda kalmaktadır",
   "Birimin defter değeri hiçbir hâlde belirlenemez; yalnızca bireysel varlıklar dikkate alınır",
   "Birimin defter değeri her hâlde gerçeğe uygun değeriyle ölçülmek zorunda tutulmaktadır",
   "Bu husus TMS 36'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 36: bir nakit yaratan birimin defter değeri, birimin geri kazanılabilir tutarının belirlenme biçimiyle tutarlı bir esasa göre belirlenir. Birime doğrudan atfedilebilen ve makul/tutarlı bir esasla dağıtılabilen varlıkları içerir; muhasebeleştirilmiş borçları kural olarak içermez.",
  "TMS 36 - NYB'nin defter değeri")

nakit_yil, iskonto, faktor36 = 100_000, 10, 2.4869
# Cevap, soru kökünde VERİLEN faktörle hesaplanmalı; tam iskonto (248.685) kökle çelişir.
pv3 = round(nakit_yil * faktor36)
q(f"Bir varlıktan gelecek 3 yıl boyunca her yıl sonunda {tr(nakit_yil)} TL net nakit girişi beklenmektedir. Varlığa özgü riskleri yansıtan vergi öncesi iskonto oranı yıllık %{iskonto}'dur. Varlığın kullanım değeri kaç TL'dir? (3 yıllık eşit taksitli bugünkü değer faktörü 2,4869)",
  f"{tr(pv3)} TL",
  [f"{tr(nakit_yil * 3)} TL", f"{tr(nakit_yil)} TL", f"{tr(round(nakit_yil * 3 * 1.1))} TL", f"{tr(round(nakit_yil / 1.1))} TL"],
  f"Kullanım değeri, beklenen gelecekteki nakit akışlarının BUGÜNKÜ değeridir: {tr(nakit_yil)} × 2,4869 = {tr(pv3)} TL. Nominal toplam olan {tr(nakit_yil * 3)} TL kullanım değeri değildir; paranın zaman değeri dikkate alınmalıdır.",
  "TMS 36 - kullanım değeri hesabı")

q("Bir işletmenin genel merkez binası birden fazla nakit yaratan birime hizmet etmektedir ve makul bir esasla birimlere dağıtılabilmektedir. TMS 36 bakımından aşağıdakilerden hangisi doğrudur?",
  "Ortak varlıktır; ilgili birimlere dağıtılarak birim düzeyinde test edilir",
  ["Genel merkez binası her hâlde bireysel olarak test edilmek zorunda tutulan bir varlığı ifade eder",
   "Genel merkez binası hiçbir hâlde değer düşüklüğü testine tabi tutulamayan bir varlık niteliğindedir",
   "Genel merkez binası her hâlde şerefiye olarak sınıflandırılmak zorunda bulunan bir kalemdir",
   "Genel merkez binası her hâlde bilanço dışı bırakılmak zorunda olan bir varlığı ifade etmektedir"],
  "TMS 36: genel merkez binası, birden fazla nakit yaratan birimin nakit akışına katkıda bulunan bir ORTAK VARLIKTIR. Kendi başına bağımsız nakit girişi sağlamadığından bireysel test edilemez; makul ve tutarlı bir esasla birimlere dağıtılarak birim düzeyinde test edilir.",
  "TMS 36 - ortak varlık (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 36 bakımından doğrudur?\n\nI. Nakit akışı projeksiyonları en fazla beş yıllık bütçelere dayandırılır\n\nII. Beş yılı aşan dönemlerde sabit veya azalan büyüme oranı kullanılır\n\nIII. Elden çıkarma maliyetlerine finansman maliyetleri de dâhildir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Projeksiyonlar en fazla beş yıllık bütçelere dayandırılır (I) ve beş yılı aşan dönemlerde sabit veya azalan büyüme oranı kullanılır (II). Elden çıkarma maliyetlerine finansman maliyetleri ve gelir vergisi gideri DÂHİL DEĞİLDİR; bu nedenle III yanlıştır.",
  "TMS 36 - kullanım değeri ve GUD")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 36; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
