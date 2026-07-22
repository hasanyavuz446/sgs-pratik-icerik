# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 37 Karşılıklar, Koşullu Borçlar ve
Koşullu Varlıklar — 60 soru. Kaynak: KGK TMS 37.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-10 soru, "hepsi" ~2 (%20-25)."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_37_karsiliklar"
PREFIX, SEED = "std-tms37-gen", 20261012
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_37_karsiliklar.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Karşılık: tanım ve muhasebeleştirme ölçütleri (16) ──────────────────
q("TMS 37'ye göre karşılık bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçekleşme zamanı veya tutarı belirsiz olan yükümlülüktür",
  ["Gerçekleşme zamanı ve tutarı kesin olarak bilinen yükümlülükleri ifade eden bir kavramdır",
   "İşletmenin gelecekte elde etmeyi beklediği ekonomik yararları ifade eden bir kavram niteliğindedir",
   "İşletmenin ortaklarına dağıtmayı planladığı kâr payını ifade eden bir kavramı karşılamaktadır",
   "Karşılık kavramı TMS 37'de tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 37: karşılık, gerçekleşme zamanı veya tutarı belirsiz olan yükümlülüktür. Bu yönüyle ticari borç ve tahakkuklardan ayrılır.",
  "TMS 37 - karşılık tanımı")

q("Karşılık ile ticari borç ve tahakkuklar arasındaki fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Karşılıkta gerçekleşme zamanı veya tutarı belirsizdir; ticari borç ve tahakkuklarda belirsizlik çok daha azdır",
  ["Karşılık ile ticari borç arasında hiçbir fark bulunmayıp ikisi aynı anlama gelmektedir",
   "Karşılıkta tutar kesindir; ticari borçlarda ise tutar her hâlde belirsiz kalmak zorundadır",
   "Karşılıklar yalnızca büyük işletmelerde, ticari borçlar ise küçük işletmelerde kullanılmaktadır",
   "Bu ayrım TMS 37'de düzenlenmemiş bir husus niteliğinde olup uygulamada yapılmamaktadır"],
  "TMS 37: karşılıklar, gelecekte yapılacak harcamanın zamanı veya tutarı konusunda belirsizlik bulunması nedeniyle ticari borçlar ve tahakkuklar gibi diğer borçlardan ayrılır.",
  "TMS 37 - karşılık ve ticari borç farkı")

q("Karşılık ayrılabilmesinin koşulları bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmiş olaydan doğan mevcut bir yükümlülük, kaynak çıkışı olasılığı ve güvenilir tahmin birlikte aranır",
  ["Yalnızca yönetimin karşılık ayırmaya karar vermiş olması yeterli olup başka koşul aranmaz",
   "Yalnızca gelecekte bir harcama yapılacağının öngörülmesi yeterli olup diğer koşullar aranmaz",
   "Koşullardan herhangi birinin sağlanması yeterli olup üçünün birlikte bulunması gerekmemektedir",
   "Karşılık ayırma koşulları TMS 37'de düzenlenmemiş olup işletmenin takdirine bırakılmıştır"],
  "TMS 37: karşılık ancak (a) geçmiş bir olaydan kaynaklanan mevcut bir yükümlülüğün bulunması, (b) yükümlülüğün yerine getirilmesi için ekonomik fayda içeren kaynakların işletmeden çıkma ihtimalinin muhtemel olması ve (c) yükümlülük tutarının güvenilir biçimde tahmin edilebilmesi durumunda muhasebeleştirilir. Üç koşul BİRLİKTE aranır.",
  "TMS 37 - karşılık ayırma koşulları")

q("Karşılık ayırmada 'muhtemel' ölçütü bakımından aşağıdakilerden hangisi doğrudur?",
  "Kaynak çıkışı olasılığının gerçekleşmeme olasılığından yüksek olması aranır",
  ["Kaynak çıkışının kesin olarak gerçekleşeceğinin bilinmesi gerekir; olasılık yeterli değildir",
   "Kaynak çıkışı olasılığının uzak ihtimal olması yeterli olup başka bir ölçüt aranmamaktadır",
   "Kaynak çıkışı olasılığı hiç dikkate alınmaz; her yükümlülük için karşılık ayrılmak zorundadır",
   "'Muhtemel' ölçütü TMS 37'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 37: bir yükümlülüğün yerine getirilmesi için ekonomik fayda içeren kaynakların çıkma ihtimalinin, çıkmama ihtimalinden yüksek olması durumunda kaynak çıkışı muhtemel kabul edilir.",
  "TMS 37 - muhtemel ölçütü")

q("Mevcut yükümlülük bakımından aşağıdakilerden hangisi doğrudur?",
  "Yasal yükümlülük veya zımni kabulden doğan yükümlülük biçiminde olabilir",
  ["Yalnızca sözleşme veya kanundan doğan yasal yükümlülükleri kapsayan bir kavramı ifade eder",
   "Yalnızca işletmenin gelecekte üstlenmeyi planladığı taahhütleri ifade eden bir kavramdır",
   "Yalnızca mahkeme kararıyla kesinleşmiş yükümlülükleri kapsayan dar bir kavram niteliğindedir",
   "Mevcut yükümlülük kavramı TMS 37'de tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TMS 37: yükümlülük, yasal yükümlülük (sözleşme, mevzuat veya diğer yasal düzenlemelerden doğan) ya da zımni kabulden doğan yükümlülük olabilir.",
  "TMS 37 - mevcut yükümlülük")

q("Zımni kabulden doğan yükümlülük bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin geçmiş uygulamaları veya açıklanmış politikalarıyla sorumluluk üstleneceğine dair geçerli beklenti yaratmasıyla doğar",
  ["Yalnızca yazılı bir sözleşmenin imzalanmış olmasıyla doğan yükümlülükleri ifade etmektedir",
   "Yalnızca mahkeme kararıyla kesinleşmiş olan yükümlülükleri ifade eden bir kavram niteliğindedir",
   "Yalnızca vergi mevzuatından doğan yükümlülükleri ifade eden dar kapsamlı bir kavramdır",
   "Zımni kabulden doğan yükümlülük TMS 37'de tanımlanmamış bir husus niteliğinde bulunur"],
  "TMS 37: zımni kabulden doğan yükümlülük, işletmenin geçmiş uygulamaları, yayımlanmış politikaları veya yeterince belirli güncel açıklamalarıyla sorumlulukları üstleneceğini diğer şahıslara taahhüt etmesi ve bunun sonucunda ilgili taraflar nezdinde geçerli bir beklenti yaratmasıyla doğar.",
  "TMS 37 - zımni kabulden doğan yükümlülük")

q("Karşılık ayırmada geçmiş olay (yükümlülük doğuran olay) bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin yükümlülüğü yerine getirmekten başka gerçekçi bir alternatifinin bulunmadığı olaydır",
  ["İşletmenin gelecekte gerçekleşmesini beklediği herhangi bir olayı ifade eden bir kavramdır",
   "İşletmenin yönetim kurulunun karar aldığı her olayı ifade eden geniş kapsamlı bir kavramdır",
   "Yalnızca nakit çıkışının fiilen gerçekleştiği olayları ifade eden dar bir kavram niteliğindedir",
   "Yükümlülük doğuran olay TMS 37'de tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TMS 37: yükümlülük doğuran olay, yasal veya zımni kabulden doğan bir yükümlülük yaratan ve sonucunda işletmenin bu yükümlülüğü yerine getirmekten başka gerçekçi bir alternatifinin bulunmadığı geçmişteki bir olaydır.",
  "TMS 37 - yükümlülük doğuran olay")

q("İşletmenin gelecekteki faaliyetlerinden doğacak maliyetler bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekte faaliyeti sürdürmekten kaçınarak önlenebilen maliyetler için karşılık ayrılmaz",
  ["Gelecekteki tüm maliyetler için her hâlde karşılık ayrılmak zorunda tutulmuş bulunmaktadır",
   "Gelecekteki maliyetler her hâlde varlık olarak aktifleştirilmek zorunda olan kalemleri ifade eder",
   "Gelecekteki maliyetler hiçbir hâlde finansal tablolara yansıtılamayan kalemleri ifade etmektedir",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: yalnızca işletmenin gelecekteki faaliyetlerinden bağımsız olarak mevcut olan yükümlülükler için karşılık ayrılır. İşletme gelecekteki faaliyetini sürdürmekten kaçınarak gelecekteki harcamalardan kaçınabiliyorsa mevcut bir yükümlülüğü yoktur; karşılık ayrılmaz.",
  "TMS 37 - gelecekteki faaliyet maliyetleri")

q("İşletmenin gelecekteki faaliyet zararları bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki faaliyet zararları için karşılık ayrılmaz",
  ["Gelecekteki faaliyet zararları için her hâlde karşılık ayrılmak zorunda tutulmaktadır",
   "Gelecekteki faaliyet zararları her hâlde varlık olarak aktifleştirilmek zorunda kalınmaktadır",
   "Gelecekteki faaliyet zararları yalnızca büyük işletmelerce karşılık ayrılarak izlenmektedir",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: gelecekteki faaliyet zararları için karşılık ayrılmaz; bunlar mevcut bir yükümlülük değildir. Ancak gelecekteki faaliyet zararı beklentisi, faaliyete ilişkin bazı varlıkların değer düşüklüğüne uğramış olabileceğinin göstergesidir (TMS 36).",
  "TMS 37 - gelecekteki faaliyet zararları")

q("Ekonomik açıdan dezavantajlı (zarara yol açacak) sözleşmeler bakımından aşağıdakilerden hangisi doğrudur?",
  "Sözleşmeden doğan mevcut yükümlülük karşılık olarak muhasebeleştirilir ve ölçülür",
  ["Bu sözleşmeler için hiçbir hâlde karşılık ayrılmaz; yalnızca dipnotta açıklanmaktadır",
   "Bu sözleşmeler her hâlde varlık olarak aktifleştirilmek zorunda tutulan kalemleri ifade eder",
   "Bu sözleşmeler her hâlde derhâl feshedilmek zorunda olup kayda alınmamaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: işletmenin ekonomik açıdan dezavantajlı bir sözleşmesinin bulunması durumunda, mevcut yükümlülük karşılık olarak muhasebeleştirilir ve ölçülür. Bu, gelecekteki faaliyet zararı kuralının bir istisnasıdır.",
  "TMS 37 - dezavantajlı sözleşmeler")

q("Yeniden yapılandırma karşılığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Ayrıntılı resmî plan bulunması ve etkilenenlerde geçerli beklenti yaratılması hâlinde zımni yükümlülük doğar",
  ["Yönetim kurulunun karar almış olması her hâlde tek başına karşılık ayrılması için yeterlidir",
   "Yeniden yapılandırma için hiçbir hâlde karşılık ayrılamaz; yalnızca dipnotta açıklanmaktadır",
   "Yeniden yapılandırma maliyetleri her hâlde varlık olarak aktifleştirilmek zorunda kalınmaktadır",
   "Yeniden yapılandırma karşılıkları TMS 37'de düzenlenmemiş bir husus niteliğinde bulunur"],
  "TMS 37: yeniden yapılandırmaya ilişkin zımni kabulden doğan yükümlülük, ancak işletmenin (a) yeniden yapılandırmaya ilişkin ayrıntılı ve resmî bir planının bulunması ve (b) planı uygulamaya başlayarak veya ana özelliklerini duyurarak etkilenecek olanlarda geçerli bir beklenti yaratması durumunda ortaya çıkar.",
  "TMS 37 - yeniden yapılandırma")

q("Yeniden yapılandırma karşılığına dâhil edilecek maliyetler bakımından aşağıdakilerden hangisi doğrudur?",
  "Yalnızca yeniden yapılandırmadan kaynaklanan zorunlu ve süregelen faaliyetlerle ilgisi olmayan doğrudan harcamalar dâhildir",
  ["Yeniden yapılandırmayla ilgili tüm harcamalar hiçbir ayrım yapılmaksızın dâhil edilmektedir",
   "Personelin yeniden eğitimi ve yer değiştirme maliyetleri de her hâlde dâhil edilmek zorundadır",
   "Yeni sistemlere ve dağıtım ağlarına yapılacak yatırımlar da her hâlde dâhil edilmektedir",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: yeniden yapılandırma karşılığı yalnızca yeniden yapılandırma sonucu katlanılan ve (a) yeniden yapılandırmadan kaynaklanan zorunlu harcamalarla (b) işletmenin süregelen faaliyetleri ile ilgili olmayan harcamaları içerir. Kalan personelin yeniden eğitimi/yer değiştirmesi, pazarlama, yeni sistem yatırımları DÂHİL EDİLMEZ.",
  "TMS 37 - yeniden yapılandırma maliyetleri")

q("Bir işletme, gelecek yıl önemli bir faaliyet zararı bekleyeceğini öngörmektedir. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki faaliyet zararı için karşılık ayrılmaz; ancak varlıklarda değer düşüklüğü göstergesi olabilir",
  ["Beklenen zarar tutarında her hâlde karşılık ayrılmak zorunda tutulan bir durumu ifade eder",
   "Beklenen zarar her hâlde varlık olarak aktifleştirilmek zorunda olan bir kalemi ifade etmektedir",
   "Beklenen zarar her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemdir",
   "Beklenen zarar hiçbir yerde belirtilmez; ne tabloda ne dipnotta yer almak zorunda kalınır"],
  "TMS 37: gelecekteki faaliyet zararları için karşılık ayrılmaz; mevcut bir yükümlülük yoktur. Ancak gelecekteki faaliyet zararı beklentisi, ilgili varlıkların değer düşüklüğüne uğramış olabileceğinin bir göstergesidir; TMS 36 uyarınca test yapılır.",
  "TMS 37 - gelecekteki faaliyet zararı (senaryo)")

q("Aşağıdakilerden hangileri TMS 37'ye göre karşılık ayırma koşullarındandır?\n\nI. Geçmiş bir olaydan kaynaklanan mevcut bir yükümlülüğün bulunması\n\nII. Kaynak çıkışı ihtimalinin muhtemel olması\n\nIII. Yükümlülük tutarının güvenilir biçimde tahmin edilebilmesi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 37 üç koşulu da BİRLİKTE arar: geçmiş olaydan doğan mevcut yükümlülük (I), kaynak çıkışının muhtemel olması (II) ve tutarın güvenilir tahmin edilebilmesi (III). Biri eksikse karşılık ayrılmaz.",
  "TMS 37 - karşılık koşulları")

q("Aşağıdaki ifadelerden hangileri TMS 37 bakımından doğrudur?\n\nI. Gelecekteki faaliyet zararları için karşılık ayrılmaz\n\nII. Dezavantajlı sözleşmeler için hiçbir durumda karşılık ayrılmaz\n\nIII. İşletmenin gelecekteki faaliyetlerinden doğacak ve kaçınılabilen maliyetler için karşılık ayrılır",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Gelecekteki faaliyet zararları için karşılık ayrılmaz (I). Dezavantajlı sözleşmeden doğan mevcut yükümlülük karşılık olarak muhasebeleştirildiğinden II; kaçınılabilen gelecekteki maliyetler mevcut yükümlülük yaratmadığından III yanlıştır. Yalnız I doğrudur.",
  "TMS 37 - karşılık ayrılmayan hâller")

q("Bir işletmenin yönetim kurulu bir fabrikayı kapatmaya karar vermiş ancak kararı henüz kimseye duyurmamış ve uygulamaya başlamamıştır. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Etkilenenlerde geçerli beklenti yaratılmadığından henüz zımni yükümlülük doğmamıştır; karşılık ayrılmaz",
  ["Yönetim kurulu kararı tek başına yeterlidir; derhâl karşılık ayrılmak zorunda tutulmaktadır",
   "Kapatma maliyetleri her hâlde varlık olarak aktifleştirilmek zorunda olan kalemleri ifade eder",
   "Bu durumda işletme her hâlde koşullu varlık muhasebeleştirmek zorunda bulunmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: yeniden yapılandırmaya ilişkin zımni yükümlülük, ayrıntılı resmî planın bulunması VE planın uygulanmaya başlanması ya da ana özelliklerinin duyurulmasıyla etkilenenlerde geçerli beklenti yaratılması hâlinde doğar. Yalnızca yönetim kararı yeterli değildir.",
  "TMS 37 - yeniden yapılandırma (senaryo)")

# ── B. Koşullu borç ve koşullu varlık (14) ─────────────────────────────────
q("TMS 37'ye göre koşullu borç bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçekleşmesi bir veya daha fazla belirsiz olayın oluşumuna bağlı olan olası yükümlülüktür",
  ["Gerçekleşme zamanı ve tutarı kesin olarak bilinen yükümlülükleri ifade eden bir kavramdır",
   "İşletmenin gelecekte elde etmesi muhtemel olan ekonomik yararları ifade eden bir kavramdır",
   "İşletmenin bilançosunda borç olarak gösterilmek zorunda olan kalemleri ifade etmektedir",
   "Koşullu borç kavramı TMS 37'de tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 37: koşullu borç, (a) geçmiş olaylardan kaynaklanan ve işletmenin tam olarak kontrolünde bulunmayan bir veya daha fazla kesin olmayan olayın gerçekleşip gerçekleşmemesiyle varlığı teyit edilecek olası yükümlülüktür ya da (b) geçmiş olaydan kaynaklanan ancak muhasebeleştirilemeyen mevcut yükümlülüktür.",
  "TMS 37 - koşullu borç tanımı")

q("Koşullu borçların muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Koşullu borçlar finansal tablolara yansıtılmaz; dipnotlarda açıklanır",
  ["Koşullu borçlar her hâlde bilançoda borç olarak muhasebeleştirilmek zorunda tutulmaktadır",
   "Koşullu borçlar hiçbir yerde belirtilmez; ne tabloda ne dipnotta yer almak zorunda kalınır",
   "Koşullu borçlar her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemleri ifade eder",
   "Koşullu borçların ele alınışı TMS 37'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 37: işletme koşullu borçlarını finansal tablolarına yansıtmaz; kaynak çıkışı ihtimali uzak değilse koşullu borcunu dipnotlarında açıklar.",
  "TMS 37 - koşullu borcun muhasebeleştirilmemesi")

q("Koşullu borcun açıklanmayacağı hâl bakımından aşağıdakilerden hangisi doğrudur?",
  "Kaynak çıkışı ihtimali uzaksa açıklama yapılmaz",
  ["Koşullu borçlar her hâlde ve istisnasız açıklanmak zorunda tutulan kalemleri ifade etmektedir",
   "Koşullu borçlar hiçbir hâlde açıklanmaz; dipnotlarda hiç yer almamak zorunda kalınmaktadır",
   "Koşullu borçlar yalnızca gerçekleşmeleri kesinleştiğinde açıklanmak zorunda bulunmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: kaynak çıkışı ihtimalinin UZAK olması durumunda koşullu borç açıklanmaz. Uzak değilse dipnotlarda açıklanır; hiçbir hâlde bilançoya alınmaz.",
  "TMS 37 - uzak ihtimal")

q("TMS 37'ye göre koşullu varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmiş olaylardan kaynaklanan ve varlığı belirsiz olayların gerçekleşmesiyle teyit edilecek olası varlıktır",
  ["Gerçekleşme zamanı ve tutarı kesin olarak bilinen varlıkları ifade eden bir kavram niteliğindedir",
   "İşletmenin gelecekte katlanması muhtemel olan yükümlülükleri ifade eden bir kavramı karşılar",
   "İşletmenin bilançosunda varlık olarak gösterilmek zorunda olan kalemleri ifade etmektedir",
   "Koşullu varlık kavramı TMS 37'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 37: koşullu varlık, geçmiş olaylardan kaynaklanan ve işletmenin tam anlamıyla kontrolünde bulunmayan bir veya daha fazla kesin mahiyette olmayan olayın ileride gerçekleşip gerçekleşmemesi ile mevcudiyeti teyit edilecek olan varlıktır.",
  "TMS 37 - koşullu varlık tanımı")

q("Koşullu varlıkların muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Koşullu varlıklar finansal tablolara yansıtılmaz; gelir girişi muhtemelse açıklanır",
  ["Koşullu varlıklar her hâlde bilançoda varlık olarak muhasebeleştirilmek zorunda tutulur",
   "Koşullu varlıklar hiçbir yerde belirtilmez; ne tabloda ne dipnotta yer almak zorunda kalınır",
   "Koşullu varlıklar her hâlde doğrudan özkaynağa kaydedilmek zorunda olan kalemleri ifade eder",
   "Koşullu varlıkların ele alınışı TMS 37'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 37: koşullu varlıklar finansal tablolara yansıtılmaz; çünkü bu durum hiçbir zaman elde edilemeyecek bir gelirin muhasebeleştirilmesi sonucunu doğurabilir. Ekonomik fayda girişi muhtemel ise koşullu varlık dipnotlarda açıklanır.",
  "TMS 37 - koşullu varlığın muhasebeleştirilmemesi")

q("Koşullu varlığın gerçekleşmesinin KESİN hâle gelmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelir elde edilmesinin kesin olması hâlinde ilgili varlık artık koşullu değildir; muhasebeleştirilir",
  ["Gelir kesinleşse dahi koşullu varlık hiçbir hâlde muhasebeleştirilememek zorunda kalınmaktadır",
   "Gelir kesinleştiğinde varlık her hâlde yalnızca dipnotta açıklanmak zorunda bulunmaktadır",
   "Gelir kesinleştiğinde varlık her hâlde doğrudan özkaynağa kaydedilmek zorunda tutulmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: gelirin elde edilmesinin neredeyse kesin hâle gelmesi durumunda ilgili varlık koşullu varlık olmaktan çıkar ve muhasebeleştirilmesi uygun olur.",
  "TMS 37 - koşullu varlığın kesinleşmesi")

q("Karşılık ile koşullu borç arasındaki temel ayrım bakımından aşağıdakilerden hangisi doğrudur?",
  "Karşılıkta mevcut yükümlülük vardır ve kaynak çıkışı muhtemeldir; koşullu borçta bu koşullar sağlanmaz",
  ["Karşılık ile koşullu borç arasında hiçbir fark bulunmayıp ikisi aynı anlama gelmektedir",
   "Karşılık dipnotta açıklanır; koşullu borç ise her hâlde bilançoya alınmak zorunda kalınmaktadır",
   "Karşılık yalnızca büyük işletmelerde, koşullu borç ise yalnızca küçük işletmelerde kullanılır",
   "Bu ayrım TMS 37'de düzenlenmemiş bir husus niteliğinde olup uygulamada yapılmamaktadır"],
  "TMS 37: karşılıklar, mevcut yükümlülük olmaları ve yerine getirilmeleri için kaynak çıkışının muhtemel olması nedeniyle muhasebeleştirilir. Koşullu borçlarda ise ya yükümlülük olası (mevcut değil) ya da mevcut olmakla birlikte kaynak çıkışı muhtemel değil veya tutar güvenilir ölçülemiyordur.",
  "TMS 37 - karşılık ve koşullu borç ayrımı")

q("Mevcut bir yükümlülük bulunmakla birlikte tutarın güvenilir biçimde tahmin edilemediği hâl bakımından aşağıdakilerden hangisi doğrudur?",
  "Karşılık ayrılmaz; koşullu borç olarak açıklanır",
  ["Tahmini bir tutarla her hâlde karşılık ayrılmak zorunda tutulan bir durumu ifade etmektedir",
   "Yükümlülük hiçbir yerde belirtilmez; ne tabloda ne dipnotta yer almak zorunda kalınmaktadır",
   "Yükümlülük her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade eder",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: son derece ender durumlarda tutarın güvenilir biçimde ölçülemediği bir yükümlülük olabilir. Bu mevcut yükümlülük karşılık olarak muhasebeleştirilmez; koşullu borç olarak açıklanır.",
  "TMS 37 - güvenilir ölçülemeyen yükümlülük")

q("Müşterek ve müteselsil sorumluluk doğuran yükümlülükler bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer taraflarca karşılanması beklenen kısım koşullu borç olarak ele alınır",
  ["Yükümlülüğün tamamı her hâlde işletmece karşılık olarak muhasebeleştirilmek zorundadır",
   "Yükümlülüğün hiçbir kısmı muhasebeleştirilmez; tamamı diğer taraflara ait sayılmaktadır",
   "Müşterek sorumluluk doğuran yükümlülükler hiçbir yerde belirtilmek zorunda bulunmamaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: müştereken ve müteselsilen sorumlu olunan bir yükümlülükte, borcun diğer taraflarca karşılanması beklenen kısmı koşullu borç olarak dikkate alınır. İşletme yalnızca kaynak çıkışının muhtemel olduğu kısım için karşılık ayırır.",
  "TMS 37 - müteselsil sorumluluk")

q("Koşullu borçların sürekli değerlendirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Sürekli değerlendirilir; kaynak çıkışı muhtemel hâle gelirse karşılık muhasebeleştirilir",
  ["Koşullu borçlar bir kez değerlendirildikten sonra hiçbir hâlde yeniden ele alınmamaktadır",
   "Koşullu borçlar hiçbir hâlde karşılığa dönüşemez; süresiz olarak dipnotta kalmak zorundadır",
   "Koşullu borçlar yalnızca vergi idaresi talep ettiğinde yeniden değerlendirilmek zorundadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: koşullu borçlar, ekonomik fayda içeren kaynakların işletmeden çıkma ihtimalinin oluşup oluşmadığını belirlemek amacıyla sürekli olarak değerlendirilir. Daha önce koşullu borç olarak açıklanan bir kalem için kaynak çıkışı muhtemel hâle gelirse karşılık muhasebeleştirilir.",
  "TMS 37 - koşullu borcun karşılığa dönüşmesi")

q("Bir işletme aleyhine dava açılmış olup hukuk müşavirine göre davayı kaybetme ihtimali kazanma ihtimalinden yüksektir ve tazminat tutarı güvenilir biçimde tahmin edilebilmektedir. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Üç koşul da sağlandığından karşılık muhasebeleştirilir",
  ["Dava sonuçlanmadığından hiçbir hâlde karşılık ayrılamaz; yalnızca dipnotta açıklanmaktadır",
   "Dava her hâlde koşullu varlık olarak muhasebeleştirilmek zorunda olan bir durumu ifade eder",
   "Tazminat tutarı her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulmaktadır",
   "Bu durumda işletme hiçbir kayıt yapmaz ve dipnotta da açıklama yapmak zorunda kalmaz"],
  "TMS 37: geçmiş olaydan (dava konusu olay) doğan mevcut yükümlülük var, kaybetme ihtimali kazanma ihtimalinden yüksek olduğundan kaynak çıkışı MUHTEMEL ve tutar güvenilir tahmin edilebiliyor. Üç koşul da sağlandığından karşılık muhasebeleştirilir.",
  "TMS 37 - dava karşılığı (senaryo)")

q("Bir işletme aleyhine dava açılmış olup hukuk müşavirine göre davayı kazanma ihtimali kaybetme ihtimalinden yüksektir. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Kaynak çıkışı muhtemel olmadığından karşılık ayrılmaz; ihtimal uzak değilse koşullu borç açıklanır",
  ["Dava açılmış olduğundan her hâlde karşılık ayrılmak zorunda tutulan bir durumu ifade etmektedir",
   "Dava her hâlde koşullu varlık olarak muhasebeleştirilmek zorunda bulunan bir durumu karşılar",
   "Bu durumda işletme hiçbir kayıt ve açıklama yapmak zorunda bulunmamak durumundadır",
   "Bu durumda işletme her hâlde tazminat tutarını gelir olarak kaydetmek zorunda kalmaktadır"],
  "TMS 37: kaynak çıkışı ihtimali çıkmama ihtimalinden yüksek değilse 'muhtemel' ölçütü sağlanmaz; karşılık ayrılmaz. Kaynak çıkışı ihtimali UZAK değilse koşullu borç olarak dipnotlarda açıklanır.",
  "TMS 37 - dava (senaryo)")

q("Bir işletme başka bir işletmeye karşı açtığı davayı kazanacağı konusunda güçlü beklenti içindedir ancak dava henüz sonuçlanmamıştır. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Koşullu varlıktır; muhasebeleştirilmez, girişi muhtemelse dipnotta açıklanır",
  ["Beklenen tazminat her hâlde varlık ve gelir olarak muhasebeleştirilmek zorunda tutulmaktadır",
   "Beklenen tazminat her hâlde karşılık olarak muhasebeleştirilmek zorunda olan bir kalemdir",
   "Beklenen tazminat hiçbir yerde belirtilmez; ne tabloda ne dipnotta yer almak zorunda kalınır",
   "Beklenen tazminat her hâlde doğrudan özkaynağa kaydedilmek zorunda bulunmaktadır"],
  "TMS 37: koşullu varlıklar finansal tablolara yansıtılmaz; hiçbir zaman elde edilemeyecek bir gelirin muhasebeleştirilmesine yol açabilir. Ekonomik fayda girişi muhtemelse dipnotlarda açıklanır. Elde edilmesi neredeyse kesinleşirse artık koşullu değildir ve muhasebeleştirilir.",
  "TMS 37 - koşullu varlık (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 37 bakımından doğrudur?\n\nI. Koşullu borçlar finansal tablolara yansıtılmaz\n\nII. Koşullu varlıklar finansal tablolara yansıtılmaz\n\nIII. Kaynak çıkışı ihtimali uzaksa koşullu borç açıklanmaz",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üçü de doğrudur: koşullu borçlar tablolara yansıtılmaz (I), koşullu varlıklar da yansıtılmaz (II) ve kaynak çıkışı ihtimali UZAK olduğunda koşullu borç açıklanmaz bile (III).",
  "TMS 37 - koşullu borç ve varlık")

# ── C. Ölçüm (16) ──────────────────────────────────────────────────────────
q("Karşılıkların ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Mevcut yükümlülüğün yerine getirilmesi için gereken harcamalara ilişkin en gerçekçi tahmindir",
  ["Yükümlülüğün olası en yüksek tutarı her hâlde esas alınmak zorunda tutulan bir ölçüdür",
   "Yükümlülüğün olası en düşük tutarı her hâlde esas alınmak zorunda olan bir ölçüyü ifade eder",
   "Karşılıklar her hâlde nominal bir tutarla ölçülmek zorunda olan kalemleri ifade etmektedir",
   "Karşılıkların ölçümü TMS 37'de düzenlenmemiş olup işletmenin takdirine bırakılmış bulunur"],
  "TMS 37: karşılık olarak muhasebeleştirilen tutar, mevcut yükümlülüğün raporlama dönemi sonu itibarıyla yerine getirilmesi için gereken harcamalara ilişkin EN GERÇEKÇİ tahmin olmalıdır.",
  "TMS 37 - en gerçekçi tahmin")

q("Karşılık ölçümünde 'en gerçekçi tahmin' bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin yükümlülüğü yerine getirmek veya üçüncü tarafa devretmek için makul biçimde ödeyeceği tutardır",
  ["İşletmenin ödemek istediği en düşük tutarı ifade eden bir ölçüyü karşılamak zorundadır",
   "İşletmenin karşılaşabileceği en yüksek zararı ifade eden bir ölçüyü karşılamak zorunda kalır",
   "Yalnızca bağımsız denetçinin belirlediği tutarı ifade eden bir ölçüyü karşılamak zorundadır",
   "Bu kavram TMS 37'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 37: en gerçekçi tahmin, işletmenin raporlama dönemi sonunda mevcut yükümlülüğü yerine getirmek veya aynı tarihte üçüncü bir tarafa devretmek için makul biçimde ödeyeceği tutardır.",
  "TMS 37 - en gerçekçi tahminin anlamı")

q("Çok sayıda benzer kalemden oluşan karşılıkların ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Beklenen değer yöntemiyle, tüm olası sonuçlar olasılıklarıyla ağırlıklandırılarak ölçülür",
  ["Her hâlde en yüksek olasılıklı tek bir sonucun tutarı esas alınmak zorunda tutulmaktadır",
   "Her hâlde en yüksek tutarlı sonucun tutarı esas alınmak zorunda olan bir yöntemi ifade eder",
   "Bu tür karşılıklar hiçbir hâlde ölçülemez; yalnızca dipnotta açıklanmak zorunda kalınmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: ölçülen yükümlülük çok sayıda kalemden oluşuyorsa, yükümlülük tüm olası sonuçların ilgili olasılıklarla ağırlıklandırılması suretiyle tahmin edilir. Bu istatistiksel tahmin yöntemine 'beklenen değer' denir (garanti karşılıkları gibi).",
  "TMS 37 - beklenen değer yöntemi")

q("Tek bir yükümlülüğün ölçülmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "En muhtemel sonuç en gerçekçi tahmini oluşturabilir; diğer olası sonuçlar da dikkate alınır",
  ["Her hâlde tüm olası sonuçların basit ortalaması alınmak zorunda olan bir yöntemi ifade eder",
   "Her hâlde en yüksek tutarlı sonuç esas alınmak zorunda tutulan bir yöntemi karşılamaktadır",
   "Tek yükümlülükler hiçbir hâlde ölçülemez; yalnızca dipnotta açıklanmak zorunda kalınmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: tek bir yükümlülüğün ölçülmesinde, en muhtemel sonuç borcun en gerçekçi tahmini olabilir. Ancak bu durumda dahi işletme diğer olası sonuçları dikkate alır; diğer olası sonuçlar çoğunlukla en muhtemel sonuçtan yüksek veya düşükse en gerçekçi tahmin daha yüksek ya da düşük bir tutar olabilir.",
  "TMS 37 - tek yükümlülüğün ölçümü")

q("Karşılık ölçümünde riskler ve belirsizlikler bakımından aşağıdakilerden hangisi doğrudur?",
  "Dikkate alınır; ancak belirsizlik, aşırı karşılık ayrılmasını haklı çıkarmaz",
  ["Riskler hiçbir hâlde dikkate alınmaz; karşılık her hâlde nominal tutarla ölçülmek zorundadır",
   "Belirsizlik hâlinde her hâlde mümkün olan en yüksek tutarda karşılık ayrılmak zorunda kalınır",
   "Belirsizlik hâlinde hiçbir hâlde karşılık ayrılamaz; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: en gerçekçi tahmine ulaşmak için mevcut durumu çevreleyen kaçınılmaz risk ve belirsizlikler dikkate alınır. Ancak belirsizlik, aşırı karşılık ayrılmasını veya borçların kasten yüksek gösterilmesini haklı çıkarmaz.",
  "TMS 37 - risk ve belirsizlikler")

q("Karşılıkların bugünkü değere indirgenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Paranın zaman değerinin etkisi önemliyse karşılık, yükümlülüğün bugünkü değeriyle ölçülür",
  ["Karşılıklar hiçbir hâlde iskonto edilemez; her zaman nominal tutarla ölçülmek zorundadır",
   "Karşılıklar her hâlde ve istisnasız iskonto edilmek zorunda olan kalemleri ifade etmektedir",
   "İskonto oranı her hâlde merkez bankasının politika faizi olmak zorunda bulunmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: paranın zaman değerinin etkisinin önemli olması durumunda karşılık, yükümlülüğün yerine getirilmesi için gerekli olması beklenen harcamaların bugünkü değeri ile ölçülür. İskonto oranı, paranın zaman değerine ve yükümlülüğe özgü risklere ilişkin cari piyasa değerlendirmelerini yansıtan vergi öncesi orandır.",
  "TMS 37 - bugünkü değere indirgeme")

q("Karşılık ölçümünde gelecekteki olaylar bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeterli tarafsız kanıt varsa yükümlülüğü etkileyebilecek gelecekteki olaylar dikkate alınır",
  ["Gelecekteki olaylar hiçbir hâlde dikkate alınmaz; yalnızca mevcut durum esas alınmaktadır",
   "Tüm gelecekteki olaylar hiçbir kanıt aranmaksızın her hâlde dikkate alınmak zorundadır",
   "Gelecekteki olaylar yalnızca vergi idaresi talep ettiğinde dikkate alınmak zorunda kalınır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: yükümlülüğün yerine getirilmesi için gerekli olan tutarı etkileyebilecek gelecekteki olaylar, gerçekleşecekleri yönünde yeterli tarafsız kanıtın bulunması durumunda karşılık tutarına yansıtılır (teknolojik gelişmeler gibi).",
  "TMS 37 - gelecekteki olaylar")

q("Karşılık ölçümünde varlıkların elden çıkarılmasından beklenen kazançlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Beklenen elden çıkarma kazançları karşılığın ölçümünde dikkate alınmaz",
  ["Beklenen kazançlar her hâlde karşılıktan indirilmek zorunda olan bir kalemi ifade etmektedir",
   "Beklenen kazançlar her hâlde karşılığa eklenmek zorunda olan bir kalemi ifade etmektedir",
   "Beklenen kazançlar her hâlde doğrudan özkaynağa kaydedilmek zorunda tutulmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: varlıkların beklenen elden çıkarılmalarından doğacak kazançlar, karşılığın ölçülmesinde dikkate alınmaz. Bu kazançlar, ilgili varlığa ilişkin Standart uyarınca ayrıca muhasebeleştirilir.",
  "TMS 37 - elden çıkarma kazançları")

q("Karşılığın yerine getirilmesi için gereken tutarın üçüncü taraflarca tazmin edilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Tazminin elde edileceği neredeyse kesinse ayrı bir varlık olarak muhasebeleştirilir; karşılıktan netleştirilmez",
  ["Tazmin her hâlde karşılıktan doğrudan indirilerek net biçimde gösterilmek zorunda kalınır",
   "Tazmin hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorunda bulunmaktadır",
   "Tazmin her hâlde ve hiçbir koşul aranmaksızın varlık olarak muhasebeleştirilmek zorundadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: karşılığın yerine getirilmesi için gereken harcamaların bir kısmının veya tamamının başka bir tarafça tazmin edilmesi bekleniyorsa, tazminat ancak işletmenin yükümlülüğü yerine getirmesi durumunda tazminatın elde edileceği KESİNE YAKIN ise muhasebeleştirilir. Tazminat AYRI bir varlık olarak ele alınır ve karşılık tutarını aşamaz.",
  "TMS 37 - tazminatlar")

q("Tazminatın kâr veya zarar tablosunda sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Karşılığa ilişkin gider, tazminat tutarı düşülerek net olarak sunulabilir",
  ["Tazminat hiçbir hâlde kâr veya zarar tablosunda gösterilemez; yalnızca dipnotta açıklanır",
   "Tazminat her hâlde ayrı bir gelir kalemi olarak sunulmak zorunda olup netleştirilememektedir",
   "Tazminat her hâlde doğrudan özkaynağa kaydedilmek zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: kâr veya zarar tablosunda karşılığa ilişkin gider, tazminat tutarı düşüldükten sonra net olarak sunulabilir. Ancak FİNANSAL DURUM TABLOSUNDA tazminata ilişkin varlık ile karşılık netleştirilemez.",
  "TMS 37 - tazminatın sunumu")

q("Karşılıkların gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Her raporlama dönemi sonunda gözden geçirilir ve en gerçekçi tahmini yansıtacak biçimde düzeltilir",
  ["Karşılıklar bir kez ayrıldıktan sonra hiçbir hâlde gözden geçirilmemek zorunda kalınmaktadır",
   "Karşılıklar yalnızca vergi idaresi talep ettiğinde gözden geçirilmek zorunda bulunmaktadır",
   "Karşılıklar yalnızca işletme zarar ettiğinde gözden geçirilmek zorunda olan kalemleri ifade eder",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: karşılıklar her raporlama dönemi sonunda gözden geçirilir ve en gerçekçi tahmini yansıtacak biçimde düzeltilir. Yükümlülüğün yerine getirilmesi için ekonomik fayda içeren kaynakların işletmeden çıkma ihtimali ortadan kalkarsa karşılık iptal edilir.",
  "TMS 37 - gözden geçirme")

q("Karşılığın kullanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Karşılık yalnızca ayrıldığı harcamalar için kullanılır",
  ["Karşılık işletmenin dilediği her türlü harcama için serbestçe kullanılabilmektedir",
   "Karşılık hiçbir hâlde kullanılamaz; süresiz olarak bilançoda tutulmak zorunda kalınmaktadır",
   "Karşılık yalnızca ortaklara kâr payı dağıtımında kullanılabilen bir kaynağı ifade etmektedir",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: karşılık, yalnızca ilk muhasebeleştirilmesi sırasında dikkate alınan harcamalar için kullanılır. Başka bir amaç için ayrılmış karşılığa harcama yansıtılması, iki farklı olayın etkisini gizleyeceğinden uygun değildir.",
  "TMS 37 - karşılığın kullanımı")

ad, olasilik_ad = 500_000, 60
q(f"Bir işletme aleyhine açılan davada tazminat tutarı {tr(ad)} TL olup hukuk müşaviri davanın kaybedilme olasılığını %{olasilik_ad} olarak değerlendirmektedir. Tutar güvenilir biçimde tahmin edilebilmektedir. TMS 37 bakımından muhasebeleştirilecek karşılık tutarı kaç TL'dir?",
  f"{tr(ad)} TL",
  [f"{tr(ad * olasilik_ad / 100)} TL", f"{tr(ad / 2)} TL", f"{tr(ad * 2)} TL", "0 TL"],
  f"Kaybetme olasılığı (%{olasilik_ad}) kazanma olasılığından yüksek olduğundan kaynak çıkışı MUHTEMELDİR ve üç koşul da sağlanır. Tek bir yükümlülükte en muhtemel sonuç en gerçekçi tahmini oluşturur: {tr(ad)} TL. Olasılıkla ağırlıklandırma (beklenen değer) çok sayıda benzer kalemde kullanılır; tek davada değil.",
  "TMS 37 - tek yükümlülükte ölçüm")

sat, kucuk_o, kucuk_m, buyuk_o, buyuk_m = 1_000_000, 75, 0, 20, 60_000
agir_o, agir_m = 5, 400_000
bek = (kucuk_o * kucuk_m + buyuk_o * buyuk_m + agir_o * agir_m) / 100
q(f"Bir işletme sattığı ürünlere garanti vermektedir. Geçmiş deneyime göre satılan ürünlerin %{kucuk_o}'inde hiç kusur çıkmamakta, %{buyuk_o}'sinde küçük kusur çıkmakta ve %{agir_o}'inde büyük kusur çıkmaktadır. Tüm ürünlerde küçük kusur çıksaydı onarım maliyeti {tr(buyuk_m)} TL, tüm ürünlerde büyük kusur çıksaydı {tr(agir_m)} TL olacaktı. Beklenen değer yöntemine göre garanti karşılığı kaç TL'dir?",
  f"{tr(bek)} TL",
  [f"{tr(buyuk_m + agir_m)} TL", f"{tr(agir_m)} TL", f"{tr((buyuk_m + agir_m) / 2)} TL", f"{tr(buyuk_m)} TL"],
  f"Çok sayıda benzer kalemde karşılık, tüm olası sonuçların olasılıklarıyla ağırlıklandırılmasıyla (beklenen değer) ölçülür: (%{kucuk_o} × 0) + (%{buyuk_o} × {tr(buyuk_m)}) + (%{agir_o} × {tr(agir_m)}) = 0 + {tr(buyuk_o * buyuk_m / 100)} + {tr(agir_o * agir_m / 100)} = {tr(bek)} TL.",
  "TMS 37 - garanti karşılığı (beklenen değer)")

kars_ilk, tazmin = 300_000, 120_000
net_gider37 = kars_ilk - tazmin
q(f"Bir işletme {tr(kars_ilk)} TL karşılık ayırmıştır. Bu tutarın {tr(tazmin)} TL'lik kısmının sigorta şirketinden tahsil edileceği kesine yakındır. TMS 37 bakımından kâr veya zarar tablosunda net olarak sunulabilecek gider tutarı kaç TL'dir?",
  f"{tr(net_gider37)} TL",
  [f"{tr(kars_ilk)} TL", f"{tr(kars_ilk + tazmin)} TL", f"{tr(tazmin)} TL", "0 TL"],
  f"TMS 37: tazminat, elde edileceği kesine yakınsa AYRI bir varlık olarak muhasebeleştirilir ve karşılığı aşamaz. Kâr veya zarar tablosunda karşılığa ilişkin gider, tazminat düşülerek net sunulabilir: {tr(kars_ilk)} − {tr(tazmin)} = {tr(net_gider37)} TL. Ancak FİNANSAL DURUM TABLOSUNDA varlık ile karşılık netleştirilemez.",
  "TMS 37 - tazminatta netleştirme")

q("Aşağıdaki ifadelerden hangileri karşılıkların ölçümü bakımından doğrudur?\n\nI. Karşılık en gerçekçi tahminle ölçülür\n\nII. Paranın zaman değeri önemliyse bugünkü değer kullanılır\n\nIII. Varlıkların elden çıkarılmasından beklenen kazançlar karşılıktan düşülür",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karşılık en gerçekçi tahminle ölçülür (I) ve paranın zaman değeri önemliyse bugünkü değer kullanılır (II). Ancak varlıkların beklenen elden çıkarılmasından doğacak kazançlar karşılığın ölçümünde DİKKATE ALINMAZ; bu nedenle III yanlıştır.",
  "TMS 37 - ölçüm")

# ── D. Açıklamalar ve karma (14) ───────────────────────────────────────────
q("Karşılıklara ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Her karşılık sınıfı için dönem başı ve sonu defter değeri mutabakatı ile yükümlülüğün niteliği açıklanır",
  ["Karşılıklar hakkında hiçbir açıklama yapılmaz; yalnızca tutar bilançoda gösterilmektedir",
   "Yalnızca karşılıkların toplam tutarı açıklanır; sınıf bazında hiçbir bilgi verilmemektedir",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca dava karşılığı bulunan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 37: işletme her karşılık sınıfı için dönem başı ve sonundaki defter değeri, dönem içinde ayrılan ilave karşılıklar, kullanılan tutarlar, iptal edilen tutarlar ve iskonto nedeniyle dönem içindeki artışı açıklar. Ayrıca yükümlülüğün niteliği ve beklenen ödeme zamanlaması belirtilir.",
  "TMS 37 - karşılık açıklamaları")

q("Koşullu borçlara ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kaynak çıkışı ihtimali uzak değilse niteliği ve mümkünse finansal etkisinin tahmini açıklanır",
  ["Koşullu borçlar hakkında hiçbir açıklama yapılmasına gerek bulunmamak durumundadır",
   "Koşullu borçlar her hâlde ve istisnasız bilançoda gösterilmek zorunda tutulmaktadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: kaynak çıkışı ihtimali uzak olmadıkça, işletme her bir koşullu borç sınıfı için koşullu borcun niteliğinin kısa açıklamasını ve mümkün olduğu durumlarda finansal etkisinin tahminini, belirsizliklere ilişkin göstergeleri ve tazminat olasılığını açıklar.",
  "TMS 37 - koşullu borç açıklamaları")

q("Açıklamaların işletmeye ciddi zarar vermesi hâli bakımından aşağıdakilerden hangisi doğrudur?",
  "Son derece ender durumlarda açıklama yapılmayabilir; ancak uyuşmazlığın genel niteliği ve açıklanmama nedeni belirtilir",
  ["Açıklamalar her hâlde ve istisnasız tam olarak yapılmak zorunda olup hiçbir istisna yoktur",
   "İşletme dilediği zaman ve gerekçesiz olarak açıklama yapmaktan kaçınabilmek durumundadır",
   "Açıklama yapılmaması hâlinde hiçbir bilgi verilmez; sessiz kalınmak zorunda bulunmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: son derece ender durumlarda, gerekli açıklamaların bir kısmının veya tamamının yapılmasının işletmenin durumuna ciddi zarar vermesi beklenebilir (karşı tarafla uyuşmazlıkta). Bu durumda açıklama yapılmaz; ancak uyuşmazlığın genel niteliği, bilginin açıklanmadığı ve açıklanmama nedeni belirtilir.",
  "TMS 37 - ciddi zarar hâli")

q("Bir işletme, ürünlerine iki yıl garanti vermektedir ve geçmiş deneyimine göre garanti talebi gelmesi muhtemeldir. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Satış anında yükümlülük doğar; beklenen değer yöntemiyle garanti karşılığı ayrılır",
  ["Garanti talebi fiilen gelene kadar hiçbir hâlde karşılık ayrılamaz; yalnızca dipnotta açıklanır",
   "Garanti maliyetleri her hâlde varlık olarak aktifleştirilmek zorunda olan kalemleri ifade eder",
   "Garanti her hâlde koşullu varlık olarak muhasebeleştirilmek zorunda bulunan bir durumdur",
   "Garanti maliyetleri her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulmaktadır"],
  "TMS 37: yükümlülük doğuran olay garanti kapsamındaki ürünlerin SATIŞIDIR; satış anında yasal yükümlülük doğar. Bir bütün olarak garantiler dikkate alındığında kaynak çıkışı muhtemeldir. Çok sayıda benzer kalem olduğundan karşılık beklenen değer yöntemiyle ölçülür.",
  "TMS 37 - garanti karşılığı (senaryo)")

q("Bir işletme, çevre mevzuatı gereği kirlettiği araziyi temizlemekle yükümlüdür ve mevzuat yürürlüktedir. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Kirletme olayı yükümlülük doğuran olaydır; temizleme maliyeti için karşılık ayrılır",
  ["Temizleme fiilen yapılana kadar hiçbir hâlde karşılık ayrılamaz; dipnotta açıklanmaktadır",
   "Temizleme maliyetleri her hâlde varlık olarak aktifleştirilmek zorunda olan kalemlerdir",
   "Temizleme yükümlülüğü her hâlde koşullu varlık olarak muhasebeleştirilmek zorundadır",
   "Temizleme maliyetleri her hâlde doğrudan özkaynaklardan indirilmek zorunda kalınmaktadır"],
  "TMS 37: yürürlükteki çevre mevzuatı uyarınca kirletme olayı, temizleme yükümlülüğü doğuran geçmiş bir olaydır. Mevcut yasal yükümlülük vardır, kaynak çıkışı muhtemeldir ve tutar güvenilir tahmin edilebiliyorsa karşılık ayrılır.",
  "TMS 37 - çevre temizleme karşılığı (senaryo)")

q("Bir işletme, henüz yürürlüğe girmemiş ancak yürürlüğe girmesi neredeyse kesin olan bir çevre mevzuatı nedeniyle gelecekte temizleme yapmak zorunda kalacaktır. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "Yasanın yürürlüğe gireceği neredeyse kesinse yükümlülük doğmuş sayılır",
  ["Yasa yürürlüğe girene kadar hiçbir hâlde yükümlülük doğamaz; karşılık ayrılamamaktadır",
   "Yasa taslak hâlindeyken dahi her hâlde ve koşulsuz olarak karşılık ayrılmak zorundadır",
   "Bu durumda işletme her hâlde koşullu varlık muhasebeleştirmek zorunda bulunmaktadır",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 37: yeni bir yasanın gerektireceği önlemlerin ayrıntıları ancak yasa tasarısının kesinleşmesiyle netleşir. Yasanın yürürlüğe gireceği hususunda neredeyse kesinlik varsa, yasadan doğan yükümlülük mevcut yükümlülük olarak dikkate alınır.",
  "TMS 37 - yasa tasarısı (senaryo)")

q("Aşağıdakilerden hangisi TMS 37'ye göre karşılık ayrılmasını gerektiren bir durumdur?",
  "Yürürlükteki mevzuat gereği kirletilen arazinin temizlenmesi yükümlülüğü",
  ["İşletmenin gelecek yıl için öngördüğü faaliyet zararı niteliğindeki beklentilerin tamamı",
   "İşletmenin gelecekte yapmayı planladığı personel eğitimi harcaması niteliğindeki tutarlar",
   "İşletmenin gelecek yıl satın almayı planladığı makine bedeli niteliğindeki taahhüt tutarları",
   "İşletmenin gelecekte yapmayı planladığı bakım harcaması niteliğindeki maliyet tutarlarının tümü"],
  "TMS 37: kirletme olayı yürürlükteki mevzuat karşısında mevcut bir yükümlülük doğurur; karşılık ayrılır. Diğer şıklardaki gelecekteki faaliyet zararı, eğitim, makine alımı ve bakım harcamaları ise işletmenin gelecekteki faaliyetlerinden kaçınarak önleyebileceği maliyetlerdir; mevcut yükümlülük yoktur, karşılık ayrılmaz.",
  "TMS 37 - karşılık gerektiren durum")

q("Aşağıdaki ifadelerden hangileri TMS 37 bakımından doğrudur?\n\nI. Tazminat, elde edileceği kesine yakınsa ayrı bir varlık olarak muhasebeleştirilir\n\nII. Tazminata ilişkin varlık ile karşılık finansal durum tablosunda netleştirilemez\n\nIII. Tazminat, ilgili karşılık tutarını aşabilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tazminat kesine yakınsa ayrı varlık olarak muhasebeleştirilir (I) ve finansal durum tablosunda karşılıkla netleştirilemez (II). Ancak muhasebeleştirilen tazminat tutarı ilgili KARŞILIĞI AŞAMAZ; bu nedenle III yanlıştır.",
  "TMS 37 - tazminatlar")

q("Aşağıdaki ifadelerden hangileri TMS 37 bakımından doğrudur?\n\nI. Karşılıklar her raporlama dönemi sonunda gözden geçirilir\n\nII. Karşılık yalnızca ayrıldığı harcamalar için kullanılır\n\nIII. Bir kez ayrılan karşılık hiçbir hâlde iptal edilemez",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karşılıklar her dönem sonunda gözden geçirilip en gerçekçi tahmine göre düzeltilir (I) ve yalnızca ayrıldığı harcamalar için kullanılır (II). Kaynak çıkışı ihtimali ortadan kalkarsa karşılık İPTAL EDİLİR; bu nedenle III yanlıştır.",
  "TMS 37 - karşılıkların izlenmesi")

q("Aşağıdaki ifadelerden hangileri karşılık ve koşullu kavramlar bakımından doğrudur?\n\nI. Karşılık bilançoya alınır\n\nII. Koşullu borç bilançoya alınmaz, açıklanır\n\nIII. Koşullu varlık bilançoya alınır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karşılık bilançoya alınır (I) ve koşullu borç alınmaz, uzak ihtimal değilse açıklanır (II). Koşullu VARLIK ise bilançoya ALINMAZ; girişi muhtemelse yalnızca dipnotta açıklanır. Bu nedenle III yanlıştır.",
  "TMS 37 - üçlü ayrım")

q("Karşılıkların finansal tablolardaki sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilançoda borç olarak sunulur; karşılık gideri kâr veya zararda muhasebeleştirilir",
  ["Karşılıklar her hâlde özkaynak kalemi olarak sunulmak zorunda olan tutarları ifade eder",
   "Karşılıklar her hâlde varlık olarak sunulmak zorunda olan tutarları ifade etmektedir",
   "Karşılıklar hiçbir hâlde bilançoda sunulmaz; yalnızca dipnotta açıklanmak zorunda kalınır",
   "Karşılıkların sunumu TMS 37'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 37: karşılık bir yükümlülüktür; bilançoda borç olarak sunulur. Karşılık ayrılmasına ilişkin gider kâr veya zararda muhasebeleştirilir. Koşullu borç ve koşullu varlıklardan farkı budur.",
  "TMS 37 - karşılıkların sunumu")

q("Bir işletmenin kâr payı dağıtımına ilişkin olarak henüz genel kurulda karar alınmamış olması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Mevcut bir yükümlülük doğmadığından karşılık ayrılmaz",
  ["Beklenen kâr payı tutarında her hâlde karşılık ayrılmak zorunda tutulan bir durumu ifade eder",
   "Beklenen kâr payı her hâlde koşullu varlık olarak muhasebeleştirilmek zorunda kalınmaktadır",
   "Beklenen kâr payı her hâlde varlık olarak aktifleştirilmek zorunda olan bir kalemi ifade eder",
   "Bu husus TMS 37'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 37: karşılık ancak geçmiş bir olaydan doğan MEVCUT yükümlülük varsa ayrılır. Kâr payı dağıtımına ilişkin yetkili organ kararı alınmadıkça işletmenin mevcut bir yükümlülüğü yoktur; karşılık ayrılmaz.",
  "TMS 37 - kâr payı (senaryo)")

q("Bir işletme, gelecek yıl makinelerine yapacağı büyük bakım için şimdiden karşılık ayırmak istemektedir. TMS 37 bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme bakımdan kaçınabileceğinden mevcut bir yükümlülük yoktur; karşılık ayrılmaz",
  ["Bakım maliyeti tahmin edilebildiğinden her hâlde karşılık ayrılmak zorunda tutulmaktadır",
   "Bakım maliyeti her hâlde koşullu borç olarak dipnotlarda açıklanmak zorunda bulunmaktadır",
   "Bakım maliyeti her hâlde derhâl gider yazılmak zorunda olan bir kalemi ifade etmektedir",
   "Bakım maliyeti her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulan bir tutardır"],
  "TMS 37: gelecekteki bakım harcamaları için karşılık ayrılmaz. İşletme, örneğin varlığı satarak gelecekteki harcamadan kaçınabileceğinden mevcut bir yükümlülüğü yoktur. Bakım maliyeti oluştuğunda gider yazılır veya ölçütleri karşılıyorsa TMS 16 uyarınca aktifleştirilir.",
  "TMS 37 - gelecekteki bakım (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 37 bakımından doğrudur?\n\nI. Yeniden yapılandırmada yalnızca yönetim kararı karşılık için yeterli değildir\n\nII. Yeniden yapılandırma karşılığına kalan personelin yeniden eğitimi dâhil edilmez\n\nIII. Yeniden yapılandırma karşılığına yeni sistemlere yapılacak yatırımlar dâhil edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Yalnızca yönetim kararı yeterli değildir; plan uygulanmaya başlanmalı veya duyurulmalıdır (I) ve kalan personelin yeniden eğitimi karşılığa dâhil edilmez (II). Yeni sistemlere ve dağıtım ağlarına yapılacak yatırımlar da süregelen faaliyetlerle ilgili olduğundan DÂHİL EDİLMEZ; bu nedenle III yanlıştır.",
  "TMS 37 - yeniden yapılandırma")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 37; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
