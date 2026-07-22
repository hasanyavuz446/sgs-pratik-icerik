# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 40 Yatırım Amaçlı Gayrimenkuller — 60 soru.
Kaynak: KGK TMS 40. Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-10 soru, "hepsi" ~2 (%20-25)."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_40_yatirim_amacli"
PREFIX, SEED = "std-tms40-gen", 20260129
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_40_yatirim_amacli.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanım ve sınıflandırma (16) ─────────────────────────────────────────
q("TMS 40'a göre yatırım amaçlı gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "Kira geliri veya değer artış kazancı ya da her ikisini elde etmek amacıyla elde tutulan gayrimenkuldür",
  ["Mal ve hizmet üretiminde kullanılmak üzere elde tutulan gayrimenkulleri ifade etmektedir",
   "Normal iş akışı çerçevesinde satılmak üzere elde tutulan gayrimenkulleri ifade eden kavramdır",
   "İdari amaçlarla kullanılmak üzere elde tutulan gayrimenkulleri ifade eden bir kavram niteliğindedir",
   "Yatırım amaçlı gayrimenkul TMS 40'ta tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 40: yatırım amaçlı gayrimenkul, kira geliri veya değer artış kazancı ya da her ikisini birden elde etmek amacıyla elde tutulan gayrimenkuldür (arsa veya bina ya da binanın bir kısmı veya her ikisi).",
  "TMS 40 - tanım")

q("Yatırım amaçlı gayrimenkulün diğer gayrimenkullerden ayrılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretimde, hizmet arzında, idari amaçla kullanılmak veya normal iş akışında satılmak üzere elde tutulmaz",
  ["Yatırım amaçlı gayrimenkul üretimde kullanılan gayrimenkulleri de kapsayan geniş bir kavramdır",
   "Yatırım amaçlı gayrimenkul normal iş akışında satılan gayrimenkulleri de kapsamak zorundadır",
   "Yatırım amaçlı gayrimenkul ile diğer gayrimenkuller arasında hiçbir fark bulunmamaktadır",
   "Bu ayrım TMS 40'ta düzenlenmemiş bir husus niteliğinde olup uygulamada yapılmamaktadır"],
  "TMS 40: yatırım amaçlı gayrimenkul, (a) mal veya hizmet üretiminde ya da tedarikinde veya idari amaçla kullanılmak ya da (b) normal iş akışı çerçevesinde satılmak amacıyla elde tutulmaz. Bu iki dışlama, sınıflandırmanın kilididir.",
  "TMS 40 - kapsam dışı amaçlar")

q("Yatırım amaçlı gayrimenkulün nakit akışı bakımından ayırt edici özelliği bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin diğer varlıklarından büyük ölçüde bağımsız nakit akışı yaratır",
  ["İşletmenin diğer varlıklarıyla birlikte ve onlara bağımlı nakit akışı yaratmak zorundadır",
   "Hiçbir nakit akışı yaratmayan ve yalnızca değer saklayan bir varlığı ifade etmek durumundadır",
   "Yalnızca satıldığında nakit akışı yaratan ve elde tutulurken hiç getiri sağlamayan varlıktır",
   "Bu özellik TMS 40'ta düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 40: yatırım amaçlı gayrimenkul, işletmenin sahip olduğu diğer varlıklardan büyük ölçüde bağımsız nakit akışları yaratır. Bu özellik, onu sahibi tarafından kullanılan gayrimenkulden ayırır.",
  "TMS 40 - bağımsız nakit akışı")

q("Aşağıdakilerden hangisi TMS 40'a göre yatırım amaçlı gayrimenkuldür?",
  "Değer artışı amacıyla elde tutulan arsa",
  ["İşletmenin idari faaliyetlerinde kullanılmak üzere elde tutulan genel merkez binası niteliğindeki yapı",
   "Emlak işiyle uğraşan işletmenin normal iş akışında satmak üzere elde tuttuğu konut niteliğindeki yapı",
   "İşletmenin üretim faaliyetinde kullandığı ve makinelerin yerleştirildiği fabrika binası niteliğinde yapı",
   "Bir müteahhidin üçüncü kişiler adına inşa etmekte olduğu ve teslim edeceği bina niteliğindeki yapı"],
  "TMS 40: uzun vadede değer artış kazancı elde etmek amacıyla elde tutulan arsa yatırım amaçlı gayrimenkuldür. İdari bina ve fabrika sahibi tarafından kullanılandır (TMS 16); satılmak üzere tutulan konut stoktur (TMS 2); başkası adına inşa edilen ise TFRS 15 kapsamındadır.",
  "TMS 40 - yatırım amaçlı örnek")

q("Gelecekteki kullanımı henüz belirlenmemiş bir arsa bakımından aşağıdakilerden hangisi doğrudur?",
  "Değer artışı amacıyla elde tutulduğu kabul edilir; yatırım amaçlı gayrimenkuldür",
  ["Her hâlde stok olarak sınıflandırılmak zorunda olan bir varlığı ifade etmek durumundadır",
   "Her hâlde sahibi tarafından kullanılan gayrimenkul olarak sınıflandırılmak zorunda kalınır",
   "Kullanımı belirlenene kadar hiçbir hâlde muhasebeleştirilemeyen bir varlığı ifade etmektedir",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gelecekte nasıl kullanılacağına karar verilmemiş bir arsa, işletme arsayı sahibi tarafından kullanılan gayrimenkul olarak kullanmaya veya normal iş akışı çerçevesinde kısa vadede satmaya karar vermediğinden, değer artış kazancı elde etmek amacıyla elde tutuluyor kabul edilir.",
  "TMS 40 - kullanımı belirlenmemiş arsa")

q("Faaliyet kiralamasıyla kiraya verilen bir bina bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin sahip olduğu ve faaliyet kiralamasıyla kiraya verdiği bina yatırım amaçlı gayrimenkuldür",
  ["Kiraya verilen bina her hâlde stok olarak sınıflandırılmak zorunda tutulan bir varlığı ifade eder",
   "Kiraya verilen bina her hâlde sahibi tarafından kullanılan gayrimenkul olarak sınıflandırılır",
   "Kiraya verilen bina hiçbir hâlde aktifleştirilemez; yalnızca dipnotta açıklanmak zorundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: işletmenin sahip olduğu (veya kullanım hakkı varlığı olarak elde tuttuğu) ve bir veya daha fazla faaliyet kiralaması çerçevesinde kiralanan bina yatırım amaçlı gayrimenkuldür.",
  "TMS 40 - kiraya verilen bina")

q("Boş olan ancak kiraya verilmek üzere elde tutulan bir bina bakımından aşağıdakilerden hangisi doğrudur?",
  "Faaliyet kiralamasıyla kiraya verilmek üzere elde tutuluyorsa yatırım amaçlı gayrimenkuldür",
  ["Boş olduğundan hiçbir hâlde yatırım amaçlı sayılamaz; kiraya verilene kadar stok olmaktadır",
   "Boş binalar her hâlde sahibi tarafından kullanılan gayrimenkul olarak sınıflandırılmaktadır",
   "Boş binalar hiçbir hâlde aktifleştirilemez; yalnızca dipnotta açıklanmak zorunda kalınmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: bir veya daha fazla faaliyet kiralaması çerçevesinde kiralanmak üzere elde tutulan boş bina, yatırım amaçlı gayrimenkul örnekleri arasında sayılır. Boş olması sınıflandırmayı değiştirmez; belirleyici olan elde tutma AMACIDIR.",
  "TMS 40 - boş bina")

q("Aşağıdakilerden hangisi TMS 40'a göre yatırım amaçlı gayrimenkul DEĞİLDİR?",
  "Emlak işletmesinin normal iş akışında satmak üzere elde tuttuğu konut",
  ["Uzun vadede değer artış kazancı elde etmek amacıyla elde tutulan arsa niteliğindeki gayrimenkuller",
   "Gelecekteki kullanımı henüz belirlenmemiş olan ve elde tutulmakta olan arsa niteliğinde varlıklar",
   "Faaliyet kiralaması çerçevesinde kiraya verilen ve kira geliri sağlayan bina niteliğinde yapıların tümü",
   "Kiraya verilmek üzere elde tutulan ancak henüz kiracı bulunamamış boş bina niteliğindeki yapılar"],
  "TMS 40: normal iş akışı çerçevesinde satılmak amacıyla elde tutulan veya bu amaçla inşa/geliştirme aşamasında olan gayrimenkuller yatırım amaçlı DEĞİLDİR; TMS 2 Stoklar kapsamındadır. Diğer şıkların tamamı yatırım amaçlı gayrimenkul örnekleridir.",
  "TMS 40 - yatırım amaçlı olmayan")

q("Sahibi tarafından kullanılan gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 16 kapsamındadır; yatırım amaçlı gayrimenkul sayılmaz",
  ["Her hâlde TMS 40 kapsamında olup yatırım amaçlı gayrimenkul sayılmak zorunda kalınmaktadır",
   "Her hâlde TMS 2 kapsamında olup stok olarak sınıflandırılmak zorunda tutulmaktadır",
   "Hiçbir standart kapsamında değildir; muhasebeleştirilmesi serbest bırakılmış bulunmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 40: sahibi tarafından kullanılan gayrimenkul, mal veya hizmet üretiminde ya da tedarikinde veya idari amaçla kullanılmak üzere (sahibi veya kiracı tarafından) elde tutulan gayrimenkuldür ve TMS 16 kapsamındadır.",
  "TMS 40 - sahibi tarafından kullanılan")

q("Başka bir işletmeye finansal kiralamayla verilen gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya verenin yatırım amaçlı gayrimenkulü değildir; TFRS 16 uyarınca ele alınır",
  ["Her hâlde kiraya verenin yatırım amaçlı gayrimenkulü olarak sınıflandırılmak zorundadır",
   "Her hâlde kiraya verenin stoku olarak sınıflandırılmak zorunda tutulan bir varlığı ifade eder",
   "Hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotlarda açıklanmakla yetinilen bir varlıktır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: başka bir işletmeye finansal kiralama çerçevesinde kiralanan gayrimenkul, kiraya verenin yatırım amaçlı gayrimenkulleri arasında sayılmaz; TFRS 16 uyarınca net kiralama yatırımı olarak ele alınır. Faaliyet kiralamasıyla kiraya verilen ise yatırım amaçlıdır.",
  "TMS 40 - finansal kiralamayla verilen")

q("Bir gayrimenkulün bir kısmının kira, bir kısmının üretim amacıyla kullanılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kısımlar ayrı satılabiliyorsa ayrı muhasebeleştirilir; ayrılamıyorsa üretim kısmı önemsizse tamamı yatırım amaçlıdır",
  ["Gayrimenkulün tamamı her hâlde yatırım amaçlı gayrimenkul sayılmak zorunda tutulmaktadır",
   "Gayrimenkulün tamamı her hâlde sahibi tarafından kullanılan gayrimenkul sayılmak zorundadır",
   "Bu tür gayrimenkuller hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: kısımlar ayrı ayrı satılabiliyorsa (veya finansal kiralamayla ayrı kiralanabiliyorsa) ayrı muhasebeleştirilir. Ayrı satılamıyorsa, gayrimenkul ancak üretimde veya idari amaçla kullanılan kısım ÖNEMSİZ ise yatırım amaçlı gayrimenkuldür.",
  "TMS 40 - karma kullanım")

q("Yatırım amaçlı gayrimenkulle birlikte tamamlayıcı hizmet sunulması bakımından aşağıdakilerden hangisi doğrudur?",
  "Hizmetler bir bütün olarak önemsizse gayrimenkul yatırım amaçlıdır; önemliyse sahibi tarafından kullanılandır",
  ["Hizmet sunulması hâlinde gayrimenkul her hâlde yatırım amaçlı sayılmak zorunda tutulmaktadır",
   "Hizmet sunulması hâlinde gayrimenkul her hâlde stok olarak sınıflandırılmak zorunda kalınır",
   "Hizmet sunulan gayrimenkuller hiçbir hâlde muhasebeleştirilemeyen varlıkları ifade etmektedir",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: işletme, kullananlara tamamlayıcı nitelikte hizmetler sunabilir (güvenlik, bakım gibi). Bu hizmetler bir bütün olarak sözleşmenin önemsiz bir bölümünü oluşturuyorsa gayrimenkul yatırım amaçlıdır. Hizmetler önemliyse (otel işletmeciliği gibi) sahibi tarafından kullanılandır.",
  "TMS 40 - tamamlayıcı hizmetler")

q("Bir ana ortaklığın bağlı ortaklığına kiraya verdiği bina bakımından aşağıdakilerden hangisi doğrudur?",
  "Bireysel finansal tablolarda yatırım amaçlı, konsolide tablolarda ise sahibi tarafından kullanılandır",
  ["Hem bireysel hem konsolide tablolarda her hâlde yatırım amaçlı gayrimenkul sayılmak zorundadır",
   "Hem bireysel hem konsolide tablolarda her hâlde sahibi tarafından kullanılan sayılmak zorundadır",
   "Bu bina hiçbir tabloda muhasebeleştirilemez; yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: bir işletme, ana ortaklığına veya diğer bir bağlı ortaklığa gayrimenkul kiralayabilir. Bu gayrimenkul konsolide finansal tablolarda yatırım amaçlı sayılmaz; grup açısından sahibi tarafından kullanılandır. Ancak kiraya veren işletmenin BİREYSEL tablolarında yatırım amaçlıdır.",
  "TMS 40 - grup içi kiralama")

q("Aşağıdakilerden hangileri TMS 40'a göre yatırım amaçlı gayrimenkuldür?\n\nI. Değer artışı amacıyla elde tutulan arsa\n\nII. Gelecekteki kullanımı belirlenmemiş arsa\n\nIII. Faaliyet kiralamasıyla kiraya verilen bina",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 40 üçünü de yatırım amaçlı gayrimenkul örneği olarak sayar: değer artışı amacıyla tutulan arsa (I), kullanımı belirlenmemiş arsa (II — değer artışı amacıyla tutuluyor sayılır) ve faaliyet kiralamasıyla kiraya verilen bina (III).",
  "TMS 40 - yatırım amaçlı örnekler")

q("Aşağıdakilerden hangileri TMS 40'a göre yatırım amaçlı gayrimenkul DEĞİLDİR?\n\nI. Normal iş akışında satılmak üzere tutulan gayrimenkul\n\nII. Değer artışı amacıyla elde tutulan arsa\n\nIII. Kiraya verilmek üzere tutulan boş bina",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Normal iş akışında satılmak üzere tutulan gayrimenkul stoktur ve TMS 40 kapsamında değildir (I). Değer artışı amacıyla tutulan arsa (II) ile kiraya verilmek üzere tutulan boş bina (III) yatırım amaçlı gayrimenkuldür. Yalnız I doğrudur.",
  "TMS 40 - kapsam dışı")

q("Yatırım amaçlı gayrimenkulün muhasebeleştirilme ölçütleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki ekonomik yararların işletmeye girişinin muhtemel olması ve maliyetin güvenilir ölçülebilmesi gerekir",
  ["Yalnızca gayrimenkulün tapuda tescil edilmiş olması yeterli olup başka koşul aranmamaktadır",
   "Yalnızca gayrimenkulün bedelinin tamamının ödenmiş olması yeterli olup başka koşul aranmaz",
   "Yalnızca yönetimin varlık olarak kaydetmeye karar vermiş olması yeterli görülmek durumundadır",
   "Muhasebeleştirme ölçütleri TMS 40'ta düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 40: yatırım amaçlı gayrimenkul, ancak (a) gayrimenkulle ilgili gelecekteki ekonomik yararların işletmeye girişinin muhtemel olması ve (b) yatırım amaçlı gayrimenkulün maliyetinin güvenilir biçimde ölçülebilmesi durumunda varlık olarak muhasebeleştirilir.",
  "TMS 40 - muhasebeleştirme ölçütleri")

# ── B. İlk ölçüm ve sonraki ölçüm modelleri (16) ───────────────────────────
q("Yatırım amaçlı gayrimenkulün ilk ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet bedeliyle ölçülür; işlem maliyetleri de maliyete dâhil edilir",
  ["Her hâlde gerçeğe uygun değeriyle ölçülür; maliyet bedeli hiç dikkate alınmamaktadır",
   "Her hâlde net gerçekleşebilir değeriyle ölçülür; maliyet bilgisi hiç dikkate alınmamaktadır",
   "Her hâlde vergi değeriyle ölçülür; muhasebe standartları bu konuda hüküm içermemektedir",
   "İlk ölçüm esası TMS 40'ta düzenlenmemiş olup işletmenin takdirine bırakılmış bulunmaktadır"],
  "TMS 40: yatırım amaçlı gayrimenkul başlangıçta maliyeti ile ölçülür. İşlem maliyetleri de ilk ölçüme dâhil edilir.",
  "TMS 40 - ilk ölçüm")

q("Yatırım amaçlı gayrimenkulün maliyetine giren unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Satın alma fiyatı ile doğrudan ilişkilendirilebilir harcamalar (hukuki hizmet, emlak alım vergisi, işlem maliyetleri) dâhildir",
  ["Yalnızca satın alma fiyatı maliyete girer; diğer tüm harcamalar gider yazılmak zorundadır",
   "İşletmenin tüm genel yönetim giderleri de maliyete dâhil edilmek zorunda tutulmaktadır",
   "Gayrimenkulün açılışına ilişkin tanıtım maliyetleri de maliyete dâhil edilmek zorundadır",
   "Maliyet unsurları TMS 40'ta düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 40: satın alınan yatırım amaçlı gayrimenkulün maliyeti, satın alma fiyatı ve buna doğrudan ilişkilendirilebilen harcamalardan oluşur (hukuki hizmetlere ilişkin ödemeler, gayrimenkul alım vergisi ve diğer işlem maliyetleri).",
  "TMS 40 - maliyet unsurları")

q("Aşağıdakilerden hangisi yatırım amaçlı gayrimenkulün maliyetine DÂHİL EDİLMEZ?",
  "Gayrimenkulün açılışına ilişkin maliyetler",
  ["Gayrimenkulün satın alınmasına ilişkin olarak ödenen hukuki hizmet bedeli niteliğindeki tutarların tümü",
   "Gayrimenkulün ediniminde ödenen ve iade edilmeyen gayrimenkul alım vergisi niteliğindeki tutarlar",
   "Gayrimenkulün ediniminde katlanılan ve doğrudan ilişkilendirilebilen işlem maliyeti niteliğinde tutarlar",
   "Gayrimenkulün satın alma fiyatı olarak satıcıya ödenen ve sözleşmede belirlenen bedel niteliğinde tutar"],
  "TMS 40: yatırım amaçlı gayrimenkulün maliyetine (a) başlangıç maliyetleri (gayrimenkulün açılışına ilişkin maliyetler), (b) gayrimenkul planlanan doluluk düzeyine ulaşana kadar oluşan işletme zararları ve (c) inşaatta kullanılan malzeme/işçilikte oluşan normalin üstündeki kayıplar DÂHİL EDİLMEZ.",
  "TMS 40 - maliyete girmeyen unsurlar")

q("Yatırım amaçlı gayrimenkulün sonraki ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme gerçeğe uygun değer yöntemini veya maliyet yöntemini muhasebe politikası olarak seçer",
  ["Yalnızca maliyet yöntemi kullanılabilir; gerçeğe uygun değer yöntemi kabul edilmemektedir",
   "Yalnızca gerçeğe uygun değer yöntemi kullanılabilir; maliyet yöntemi kesin olarak yasaklanmıştır",
   "İki yöntem de aynı anda ve birlikte kullanılmak zorunda olup tek yöntem yeterli görülmemektedir",
   "Sonraki ölçüm esası TMS 40'ta düzenlenmemiş olup işletmenin takdirine bırakılmış bulunmaktadır"],
  "TMS 40: işletme, muhasebe politikası olarak gerçeğe uygun değer yöntemini veya maliyet yöntemini seçer ve bu politikayı tüm yatırım amaçlı gayrimenkullerine uygular.",
  "TMS 40 - iki yöntem")

q("Seçilen ölçüm yönteminin uygulanma kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Seçilen yöntem tüm yatırım amaçlı gayrimenkullere uygulanır",
  ["Seçilen yöntem yalnızca işletmenin seçtiği tek bir gayrimenkule uygulanmak zorunda kalınır",
   "Her gayrimenkul için ayrı ayrı ve serbestçe farklı yöntem seçilebilmek zorunda bulunmaktadır",
   "Seçilen yöntem işletmenin tüm maddi duran varlıklarına da uygulanmak zorunda tutulmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: işletme seçtiği yöntemi (gerçeğe uygun değer veya maliyet) TÜM yatırım amaçlı gayrimenkullerine uygular. TMS 16'daki sınıf bazında seçimden farklıdır.",
  "TMS 40 - yöntemin kapsamı")

q("Gerçeğe uygun değer yönteminde değer değişimleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değerdeki değişimden kaynaklanan kazanç veya kayıp oluştuğu dönemde kâr veya zarara yansıtılır",
  ["Değer değişimleri her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulmaktadır",
   "Değer değişimleri her hâlde doğrudan özkaynakta değer artışı olarak biriktirilmek zorundadır",
   "Değer değişimleri hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Değer değişimlerinin ele alınışı TMS 40'ta düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 40: yatırım amaçlı gayrimenkulün gerçeğe uygun değerindeki değişimden kaynaklanan kazanç veya kayıp, oluştuğu dönemde KÂR VEYA ZARARA dâhil edilir. Bu, TMS 16'daki yeniden değerleme modelinden (artış diğer kapsamlı gelire gider) temel farkıdır.",
  "TMS 40 - GUD değişimi kâr/zarara")

q("Gerçeğe uygun değer yönteminde amortisman bakımından aşağıdakilerden hangisi doğrudur?",
  "Gayrimenkul için amortisman ayrılmaz",
  ["Gayrimenkul için her hâlde amortisman ayrılmak zorunda olup faydalı ömre bölünmektedir",
   "Amortisman yalnızca binalar için ayrılır; arsalar için ayrıca itfa payı hesaplanmak zorundadır",
   "Amortisman her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade eder",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gerçeğe uygun değer yönteminde yatırım amaçlı gayrimenkul için amortisman ayrılmaz. Gayrimenkul her raporlama dönemi sonunda gerçeğe uygun değeriyle yeniden ölçülür; değer değişimi kâr veya zarara yansıtılır.",
  "TMS 40 - GUD yönteminde amortisman yok")

q("Maliyet yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Gayrimenkul TMS 16'daki maliyet modeline göre ölçülür; gerçeğe uygun değeri dipnotta açıklanır",
  ["Gayrimenkul her hâlde gerçeğe uygun değeriyle ölçülür; maliyet hiç dikkate alınmamaktadır",
   "Maliyet yönteminde gerçeğe uygun değer hiçbir hâlde açıklanmaz; dipnotta yer almamaktadır",
   "Maliyet yönteminde hiçbir hâlde amortisman ayrılmaz; gayrimenkul itfa edilmeden bırakılır",
   "Maliyet yöntemi TMS 40'ta düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 40: maliyet yöntemini seçen işletme, tüm yatırım amaçlı gayrimenkullerini TMS 16'daki maliyet modeline uygun olarak ölçer (maliyet − birikmiş amortisman − birikmiş değer düşüklüğü). Ancak yatırım amaçlı gayrimenkullerinin GERÇEĞE UYGUN DEĞERİNİ dipnotlarda AÇIKLAR.",
  "TMS 40 - maliyet yöntemi")

q("Gerçeğe uygun değer yönteminden maliyet yöntemine dönülmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişikliğin daha uygun bir sunum sağlaması pek olası değildir; bu nedenle geçiş beklenmez",
  ["İşletme her dönem serbestçe ve gerekçesiz olarak yöntem değiştirebilmek zorunda bulunmaktadır",
   "Yöntem değişikliği hiçbir hâlde ve hiçbir koşulda yapılamayan bir işlemi ifade etmek durumundadır",
   "Yöntem değişikliği yalnızca vergi idaresi izin verdiğinde yapılabilmek zorunda kalınmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: bir işletme, muhasebe politikasında yapılacak isteğe bağlı bir değişikliği ancak daha uygun bir sunum sağlıyorsa yapar. Gerçeğe uygun değer yönteminden maliyet yöntemine geçilmesinin daha uygun bir sunumla sonuçlanması ihtimali PEK OLASI DEĞİLDİR.",
  "TMS 40 - GUD'den maliyete dönüş")

q("Gerçeğe uygun değerin güvenilir biçimde ölçülememesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İstisnai hâllerde inşa hâlindekiler dışında gayrimenkul TMS 16 maliyet modeliyle ölçülür; kalıntı değer sıfır varsayılır",
  ["Gerçeğe uygun değer ölçülemese dahi her hâlde tahmini bir değerle ölçülmek zorunda kalınır",
   "Bu durumda gayrimenkul hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmaktadır",
   "Bu durumda gayrimenkul her hâlde bilanço dışı bırakılmak zorunda tutulan bir varlığı ifade eder",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: istisnai durumlarda, gerçeğe uygun değerin sürekli olarak güvenilir biçimde ölçülemeyeceğine dair açık kanıt bulunabilir. Bu durumda gayrimenkul, elden çıkarılana kadar TMS 16'daki maliyet modeli kullanılarak ölçülür ve kalıntı değerinin sıfır olduğu varsayılır.",
  "TMS 40 - GUD ölçülemezse")

gud1, gud2 = 1_000_000, 1_150_000
kazanc = gud2 - gud1
q(f"Gerçeğe uygun değer yöntemini uygulayan bir işletmenin yatırım amaçlı gayrimenkulünün dönem başı gerçeğe uygun değeri {tr(gud1)} TL, dönem sonu gerçeğe uygun değeri {tr(gud2)} TL'dir. TMS 40'a göre bu değişimin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  f"{tr(kazanc)} TL kazanç kâr veya zarara yansıtılır",
  [f"{tr(kazanc)} TL kazanç diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulan bir kalemdir",
   f"{tr(kazanc)} TL kazanç doğrudan özkaynakta değer artışı olarak biriktirilmek zorunda kalınır",
   f"{tr(gud2)} TL kazanç olarak kaydedilir; artış tutarı değil yeni değerin tamamı yazılmaktadır",
   "Hiçbir kayıt yapılmaz; değer artışı yalnızca dipnotlarda açıklanmakla yetinilmek durumundadır"],
  f"Kazanç = {tr(gud2)} − {tr(gud1)} = {tr(kazanc)} TL. TMS 40 gerçeğe uygun değer yönteminde değer değişiminden doğan kazanç veya kayıp, oluştuğu dönemde KÂR VEYA ZARARA dâhil edilir. TMS 16'daki yeniden değerlemeden farklı olarak diğer kapsamlı gelire gitmez.",
  "TMS 40 - GUD artışı hesabı")

gudA, gudB = 900_000, 820_000
kayip = gudA - gudB
q(f"Gerçeğe uygun değer yöntemini uygulayan bir işletmenin yatırım amaçlı gayrimenkulünün gerçeğe uygun değeri {tr(gudA)} TL'den {tr(gudB)} TL'ye düşmüştür. TMS 40'a göre aşağıdakilerden hangisi doğrudur?",
  f"{tr(kayip)} TL kayıp kâr veya zarara yansıtılır",
  [f"{tr(kayip)} TL kayıp diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulan bir kalemdir",
   f"{tr(kayip)} TL kayıp doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade eder",
   f"{tr(gudB)} TL kayıp olarak kaydedilir; azalış tutarı değil yeni değerin tamamı yazılmaktadır",
   "Hiçbir kayıt yapılmaz; değer azalışı yalnızca dipnotlarda açıklanmakla yetinilmektedir"],
  f"Kayıp = {tr(gudA)} − {tr(gudB)} = {tr(kayip)} TL. TMS 40 gerçeğe uygun değer yönteminde değer değişiminden doğan kazanç veya kayıp, oluştuğu dönemde kâr veya zarara dâhil edilir. Değer artışı fonu aranmaz; azalış doğrudan kâr veya zarara yazılır.",
  "TMS 40 - GUD azalışı hesabı")

mal40, om40 = 1_200_000, 25
amort40 = mal40 / om40
q(f"Maliyet yöntemini uygulayan bir işletmenin yatırım amaçlı binasının maliyeti {tr(mal40)} TL, faydalı ömrü {om40} yıl ve kalıntı değeri sıfırdır. Doğrusal yönteme göre yıllık amortisman gideri kaç TL'dir?",
  f"{tr(amort40)} TL",
  [f"{tr(mal40)} TL", f"{tr(mal40 / 10)} TL", f"{tr(mal40 / 50)} TL", "0 TL"],
  f"Maliyet yönteminde yatırım amaçlı gayrimenkul TMS 16 maliyet modeline göre ölçülür ve amortismana tabi tutulur: {tr(mal40)} ÷ {om40} = {tr(amort40)} TL. Amortismanın ayrılmadığı yöntem gerçeğe uygun değer yöntemidir.",
  "TMS 40 - maliyet yönteminde amortisman")

q("Bir işletme yatırım amaçlı gayrimenkulünü gerçeğe uygun değer yöntemiyle ölçmekte ve ayrıca amortisman da ayırmaktadır. TMS 40 bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulama yanlıştır; gerçeğe uygun değer yönteminde amortisman ayrılmaz",
  ["Uygulama doğrudur; gerçeğe uygun değer yönteminde de amortisman ayrılmak zorunda kalınmaktadır",
   "Uygulama doğrudur; amortisman ayrılıp ayrılmayacağı işletmenin serbest takdirine bırakılmıştır",
   "Uygulama yanlıştır; gerçeğe uygun değer yönteminde gayrimenkul hiç ölçülmemek zorundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gerçeğe uygun değer yönteminde yatırım amaçlı gayrimenkul için AMORTİSMAN AYRILMAZ. Gayrimenkul her dönem sonunda gerçeğe uygun değeriyle yeniden ölçülür; değer değişimi kâr veya zarara yansıtılır. Hem GUD ile ölçüp hem amortisman ayırmak çift sayım olurdu.",
  "TMS 40 - GUD ve amortisman (senaryo)")

q("Aşağıdaki ifadelerden hangileri gerçeğe uygun değer yöntemi bakımından doğrudur?\n\nI. Değer değişimi kâr veya zarara yansıtılır\n\nII. Amortisman ayrılmaz\n\nIII. Değer artışı diğer kapsamlı gelirde muhasebeleştirilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "GUD yönteminde değer değişimi kâr veya zarara yansıtılır (I) ve amortisman ayrılmaz (II). Değer artışı diğer kapsamlı gelire GİTMEZ; bu TMS 16'daki yeniden değerleme modelidir. Bu nedenle III yanlıştır — TMS 40 ile TMS 16'nın en çok karıştırılan farkıdır.",
  "TMS 40 - GUD yöntemi")

q("Aşağıdaki ifadelerden hangileri TMS 40 bakımından doğrudur?\n\nI. Seçilen ölçüm yöntemi tüm yatırım amaçlı gayrimenkullere uygulanır\n\nII. Maliyet yönteminde gerçeğe uygun değer dipnotta açıklanır\n\nIII. Maliyet yönteminde amortisman ayrılmaz",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Seçilen yöntem tüm yatırım amaçlı gayrimenkullere uygulanır (I) ve maliyet yönteminde GUD dipnotta açıklanır (II). Maliyet yönteminde TMS 16 maliyet modeli uygulandığından AMORTİSMAN AYRILIR; amortisman ayrılmayan yöntem GUD yöntemidir. Bu nedenle III yanlıştır.",
  "TMS 40 - ölçüm yöntemleri")

# ── C. Transferler (14) ────────────────────────────────────────────────────
q("Yatırım amaçlı gayrimenkullere veya bunlardan yapılacak transferler bakımından aşağıdakilerden hangisi doğrudur?",
  "Yalnızca kullanımda değişiklik olduğunda yapılır",
  ["Transferler işletmenin dilediği zaman ve gerekçesiz olarak yapılabilmek zorunda bulunmaktadır",
   "Transferler her hâlde her raporlama dönemi sonunda zorunlu olarak yapılmak durumundadır",
   "Transferler hiçbir hâlde yapılamaz; sınıflandırma ilk edinimde kalıcı olarak belirlenmektedir",
   "Transferlerin koşulları TMS 40'ta düzenlenmemiş bir husus niteliğinde bulunmak durumundadır"],
  "TMS 40: yatırım amaçlı gayrimenkullere veya bu gayrimenkullerden yapılan transferler, ancak ve ancak KULLANIMDA BİR DEĞİŞİKLİK olduğunda yapılır. Yönetimin niyetindeki değişiklik tek başına yeterli değildir.",
  "TMS 40 - transferin koşulu")

q("Sahibi tarafından kullanılmaya başlanan bir yatırım amaçlı gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 16 kapsamındaki sahibi tarafından kullanılan gayrimenkullere transfer edilir",
  ["Her hâlde yatırım amaçlı gayrimenkul olarak kalmaya devam etmek zorunda bulunmaktadır",
   "Her hâlde stok olarak sınıflandırılıp TMS 2 kapsamına alınmak zorunda tutulmaktadır",
   "Her hâlde bilanço dışı bırakılmak zorunda olup yeniden muhasebeleştirilememektedir",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: sahibi tarafından kullanımın başlaması veya sahibi tarafından kullanım amacıyla geliştirmeye başlanması hâlinde, yatırım amaçlı gayrimenkulden sahibi tarafından kullanılan gayrimenkule (TMS 16) transfer yapılır.",
  "TMS 40 - TMS 16'ya transfer")

q("Satış amacıyla geliştirilmeye başlanan bir yatırım amaçlı gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "Stoklara transfer edilir",
  ["Her hâlde yatırım amaçlı gayrimenkul olarak kalmaya devam etmek zorunda bulunmaktadır",
   "Her hâlde sahibi tarafından kullanılan gayrimenkul olarak sınıflandırılmak zorunda kalınır",
   "Her hâlde bilanço dışı bırakılmak zorunda olup yeniden muhasebeleştirilememektedir",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: satış amacıyla geliştirmeye başlanması durumunda yatırım amaçlı gayrimenkulden stoklara transfer yapılır.",
  "TMS 40 - stoklara transfer")

q("Sahibi tarafından kullanımına son verilen bir gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım amaçlı gayrimenkullere transfer edilir",
  ["Her hâlde stok olarak sınıflandırılıp TMS 2 kapsamına alınmak zorunda tutulmaktadır",
   "Her hâlde sahibi tarafından kullanılan gayrimenkul olarak kalmaya devam etmek zorundadır",
   "Her hâlde bilanço dışı bırakılmak zorunda olup yeniden muhasebeleştirilememek durumundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: sahibi tarafından kullanımın sona ermesi durumunda, sahibi tarafından kullanılan gayrimenkulden yatırım amaçlı gayrimenkullere transfer yapılır.",
  "TMS 40 - yatırım amaçlıya transfer")

q("Bir yatırım amaçlı gayrimenkulün satış amacıyla geliştirilmeden doğrudan satılmasına karar verilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Elden çıkarılana kadar yatırım amaçlı gayrimenkul olarak kalır; stoklara transfer edilmez",
  ["Her hâlde derhâl stoklara transfer edilmek zorunda olan bir gayrimenkulü ifade etmektedir",
   "Her hâlde sahibi tarafından kullanılan gayrimenkul olarak sınıflandırılmak zorunda kalınır",
   "Her hâlde derhâl bilanço dışı bırakılmak zorunda olup satış beklenmeden silinmektedir",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: işletme, bir yatırım amaçlı gayrimenkulü GELİŞTİRMEDEN elden çıkarmaya karar verirse, gayrimenkulü finansal durum tablosu dışı bırakılana kadar yatırım amaçlı gayrimenkul olarak sınıflandırmaya devam eder; stoklara transfer etmez.",
  "TMS 40 - geliştirmeden satış kararı")

q("Gerçeğe uygun değer yönteminde yatırım amaçlıdan sahibi tarafından kullanılana yapılan transfer bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanımdaki değişiklik tarihindeki gerçeğe uygun değer, sonraki muhasebeleştirmede tahmini maliyet olur",
  ["Transfer her hâlde gayrimenkulün ilk maliyet bedeli üzerinden yapılmak zorunda tutulmaktadır",
   "Transfer her hâlde gayrimenkulün defter değeri sıfırlanarak yapılmak zorunda bulunmaktadır",
   "Bu transfer hiçbir hâlde yapılamaz; gayrimenkul yatırım amaçlı kalmak zorunda kalmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: gerçeğe uygun değer yöntemi uygulanan bir yatırım amaçlı gayrimenkulden sahibi tarafından kullanılan gayrimenkule veya stoklara yapılan transferde, gayrimenkulün sonraki muhasebeleştirilmesindeki tahmini maliyeti, kullanımdaki değişikliğin gerçekleştiği tarihteki gerçeğe uygun değeridir.",
  "TMS 40 - transferde tahmini maliyet")

q("Sahibi tarafından kullanılan gayrimenkulden gerçeğe uygun değerle ölçülecek yatırım amaçlıya transfer bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişiklik tarihine kadar TMS 16 uygulanır; defter değeri ile GUD farkı yeniden değerleme gibi ele alınır",
  ["Fark her hâlde ve istisnasız doğrudan dönem kâr veya zararına yansıtılmak zorunda tutulur",
   "Bu transferde hiçbir fark doğmaz; gayrimenkul defter değeriyle aynen aktarılmak zorundadır",
   "Fark her hâlde gayrimenkulün maliyetine eklenerek aktifleştirilmek zorunda bulunmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: sahibi tarafından kullanılan gayrimenkulden gerçeğe uygun değerle gösterilecek yatırım amaçlı gayrimenkule yapılan transferde, kullanımdaki değişiklik tarihine kadar TMS 16 uygulanır. O tarihteki defter değeri ile gerçeğe uygun değer arasındaki fark, TMS 16 uyarınca YENİDEN DEĞERLEME gibi işlem görür (artış diğer kapsamlı gelire).",
  "TMS 40 - TMS 16'dan transfer")

q("Stoklardan gerçeğe uygun değerle ölçülecek yatırım amaçlı gayrimenkule transfer bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değer ile önceki defter değeri arasındaki fark kâr veya zarara yansıtılır",
  ["Fark her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda olan bir kalemi ifade eder",
   "Fark her hâlde doğrudan özkaynakta değer artışı olarak biriktirilmek zorunda tutulmaktadır",
   "Bu transferde hiçbir fark doğmaz; gayrimenkul defter değeriyle aynen aktarılmak zorundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: stoklardan gerçeğe uygun değerle gösterilecek yatırım amaçlı gayrimenkule yapılan transferde, gayrimenkulün transfer tarihindeki gerçeğe uygun değeri ile önceki defter değeri arasındaki fark KÂR VEYA ZARARA yansıtılır. TMS 16'dan yapılan transferden (DKG) farklıdır.",
  "TMS 40 - stoklardan transfer")

q("Maliyet yöntemi uygulanan işletmede yapılan transferler bakımından aşağıdakilerden hangisi doğrudur?",
  "Transferler gayrimenkulün defter değerini değiştirmez ve maliyetini etkilemez",
  ["Transferler her hâlde gayrimenkulün gerçeğe uygun değeriyle yapılmak zorunda tutulmaktadır",
   "Transferlerde her hâlde defter değeri ile gerçeğe uygun değer farkı kâr veya zarara yazılır",
   "Maliyet yönteminde hiçbir hâlde transfer yapılamaz; sınıflandırma kalıcı olmak zorundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: maliyet yöntemini uygulayan bir işletmenin yatırım amaçlı gayrimenkul, sahibi tarafından kullanılan gayrimenkul ve stoklar arasında yaptığı transferler, transfer edilen gayrimenkulün defter değerini değiştirmez ve ölçüm ya da açıklama amacıyla belirlenen maliyetini etkilemez.",
  "TMS 40 - maliyet yönteminde transfer")

tr_gud, tr_dd = 1_400_000, 1_100_000
tr_fark = tr_gud - tr_dd
q(f"Gerçeğe uygun değer yöntemini uygulayan bir işletme, sahibi tarafından kullandığı binayı kiraya vermeye başlamıştır. Binanın TMS 16'ya göre defter değeri {tr(tr_dd)} TL, transfer tarihindeki gerçeğe uygun değeri {tr(tr_gud)} TL'dir. TMS 40'a göre {tr(tr_fark)} TL'lik fark nasıl muhasebeleştirilir?",
  "Yeniden değerleme gibi ele alınır; diğer kapsamlı gelirde muhasebeleştirilir",
  ["Doğrudan dönem kâr veya zararına gelir olarak yansıtılmak zorunda olan bir farkı ifade eder",
   "Doğrudan binanın maliyetine eklenerek aktifleştirilmek zorunda olan bir farkı ifade etmektedir",
   "Ertelenmiş gelir olarak yabancı kaynaklarda gösterilmek zorunda tutulan bir farkı karşılar",
   "Hiçbir kayıt yapılmaz; fark yalnızca dipnotlarda açıklanmakla yetinilmek durumundadır"],
  f"Fark = {tr(tr_gud)} − {tr(tr_dd)} = {tr(tr_fark)} TL. TMS 40: sahibi tarafından kullanılandan (TMS 16) gerçeğe uygun değerle gösterilecek yatırım amaçlıya transferde, transfer tarihine kadar TMS 16 uygulanır ve fark TMS 16'daki YENİDEN DEĞERLEME gibi işlem görür; artış diğer kapsamlı gelirde muhasebeleştirilir.",
  "TMS 40 - TMS 16'dan transfer hesabı")

st_gud, st_dd = 950_000, 800_000
st_fark = st_gud - st_dd
q(f"Gerçeğe uygun değer yöntemini uygulayan bir emlak işletmesi, satmak üzere stoklarında tuttuğu konutu kiraya vermeye karar vermiştir. Konutun defter değeri {tr(st_dd)} TL, transfer tarihindeki gerçeğe uygun değeri {tr(st_gud)} TL'dir. TMS 40'a göre {tr(st_fark)} TL'lik fark nasıl muhasebeleştirilir?",
  "Kâr veya zarara yansıtılır",
  ["Diğer kapsamlı gelirde muhasebeleştirilerek özkaynakta biriktirilmek zorunda tutulmaktadır",
   "Doğrudan özkaynakta değer artışı olarak biriktirilmek zorunda olan bir farkı ifade etmektedir",
   "Ertelenmiş gelir olarak yabancı kaynaklarda gösterilmek zorunda olan bir farkı karşılamaktadır",
   "Hiçbir kayıt yapılmaz; fark yalnızca dipnotlarda açıklanmakla yetinilmek zorunda kalınmaktadır"],
  f"Fark = {tr(st_gud)} − {tr(st_dd)} = {tr(st_fark)} TL. TMS 40: STOKLARDAN gerçeğe uygun değerle gösterilecek yatırım amaçlı gayrimenkule yapılan transferde fark KÂR VEYA ZARARA yansıtılır. TMS 16'dan yapılan transferde ise fark yeniden değerleme gibi (diğer kapsamlı gelir) ele alınır; ikisi karıştırılmamalıdır.",
  "TMS 40 - stoklardan transfer hesabı")

q("Aşağıdakilerden hangileri TMS 40'a göre transfer gerektiren kullanım değişikliklerindendir?\n\nI. Sahibi tarafından kullanımın başlaması\n\nII. Satış amacıyla geliştirmeye başlanması\n\nIII. Sahibi tarafından kullanımın sona ermesi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 40 üçünü de transfer gerektiren kullanım değişikliği olarak sayar: sahibi tarafından kullanımın başlaması → TMS 16'ya (I), satış amacıyla geliştirmeye başlanması → stoklara (II) ve sahibi tarafından kullanımın sona ermesi → yatırım amaçlıya (III).",
  "TMS 40 - transfer hâlleri")

q("Aşağıdaki ifadelerden hangileri transferler bakımından doğrudur?\n\nI. Transferler yalnızca kullanımda değişiklik olduğunda yapılır\n\nII. Stoklardan yatırım amaçlıya transferde fark kâr veya zarara yansıtılır\n\nIII. TMS 16'dan yatırım amaçlıya transferde fark kâr veya zarara yansıtılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Transferler yalnızca kullanımda değişiklik olduğunda yapılır (I) ve stoklardan transferde fark kâr veya zarara yansıtılır (II). TMS 16'dan (sahibi tarafından kullanılandan) transferde ise fark YENİDEN DEĞERLEME gibi ele alınır; artış diğer kapsamlı gelire gider. Bu nedenle III yanlıştır.",
  "TMS 40 - transferler")

q("Bir işletmenin yönetimi, yatırım amaçlı bir binayı ileride kendi kullanımına almayı planlamakta ancak henüz kullanmaya başlamamıştır. TMS 40 bakımından aşağıdakilerden hangisi doğrudur?",
  "Fiilen kullanım başlamadığından transfer yapılmaz; bina yatırım amaçlı kalır",
  ["Yönetimin planı yeterlidir; derhâl TMS 16'ya transfer edilmek zorunda tutulan bir durumdur",
   "Bina her hâlde derhâl stoklara transfer edilmek zorunda olan bir varlığı ifade etmektedir",
   "Bina her hâlde derhâl bilanço dışı bırakılmak zorunda olan bir varlığı ifade etmek durumundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: transferler ancak ve ancak KULLANIMDA BİR DEĞİŞİKLİK olduğunda yapılır. Yönetimin niyeti veya planı tek başına kullanımda değişiklik sayılmaz; sahibi tarafından kullanımın fiilen başlaması (veya bu amaçla geliştirmeye başlanması) gerekir.",
  "TMS 40 - transferde niyet yetmez (senaryo)")

# ── D. Elden çıkarma, açıklamalar, karma (14) ──────────────────────────────
q("Yatırım amaçlı gayrimenkulün finansal durum tablosu dışı bırakılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Elden çıkarıldığında veya kullanımdan çekilip gelecekte ekonomik yarar beklenmediğinde bilanço dışı bırakılır",
  ["Yalnızca fiziken yok olduğunda bilanço dışı bırakılabilmek zorunda olan bir varlığı ifade eder",
   "Hiçbir hâlde bilanço dışı bırakılamaz; süresiz olarak kayıtlarda kalmak zorunda kalmaktadır",
   "Yalnızca vergi idaresi izin verdiğinde bilanço dışı bırakılabilmek zorunda bulunmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 40: yatırım amaçlı gayrimenkul, (a) elden çıkarıldığında veya (b) kullanımdan sürekli olarak çekildiğinde ve elden çıkarılmasından gelecekte hiçbir ekonomik yarar beklenmediğinde finansal durum tablosu dışı bırakılır.",
  "TMS 40 - bilanço dışı bırakma")

q("Yatırım amaçlı gayrimenkulün elden çıkarılmasından doğan kazanç veya kayıp bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr veya zarara yansıtılır; net elden çıkarma hasılatı ile defter değeri arasındaki farktır",
  ["Her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda olan bir kalemi ifade etmektedir",
   "Her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade etmek durumundadır",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: yatırım amaçlı gayrimenkulün kullanım dışı bırakılmasından veya elden çıkarılmasından kaynaklanan kazanç ya da kayıplar, elden çıkarmadan kaynaklanan net tahsilat ile varlığın defter değeri arasındaki fark olarak belirlenir ve kâr veya zararda muhasebeleştirilir.",
  "TMS 40 - elden çıkarma kazancı")

sat40_bedel, sat40_dd = 1_300_000, 1_150_000
sat40_kar = sat40_bedel - sat40_dd
q(f"Gerçeğe uygun değer yöntemini uygulayan bir işletme, defter değeri (son gerçeğe uygun değeri) {tr(sat40_dd)} TL olan yatırım amaçlı gayrimenkulünü {tr(sat40_bedel)} TL'ye satmıştır. Elden çıkarmadan doğan kazanç kaç TL'dir?",
  f"{tr(sat40_kar)} TL",
  [f"{tr(sat40_bedel)} TL", f"{tr(sat40_dd)} TL", f"{tr(sat40_bedel + sat40_dd)} TL", "0 TL"],
  f"Kazanç = Net elden çıkarma hasılatı − Defter değeri = {tr(sat40_bedel)} − {tr(sat40_dd)} = {tr(sat40_kar)} TL. Kâr veya zararda muhasebeleştirilir.",
  "TMS 40 - elden çıkarma kazancı hesabı")

q("Gerçeğe uygun değer yöntemini uygulayan işletmenin yapacağı açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem başı ve sonu defter değeri mutabakatı ile gerçeğe uygun değer değişiminden doğan net kazanç açıklanır",
  ["Yatırım amaçlı gayrimenkuller hakkında hiçbir açıklama yapılmasına gerek bulunmamaktadır",
   "Yalnızca toplam tutar açıklanır; hiçbir hareket veya değişim bilgisi verilmemek durumundadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca maliyet yöntemi uygulayan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 40: gerçeğe uygun değer yöntemini uygulayan işletme, dönem başındaki ve sonundaki defter değerleri arasında mutabakat sunar; ilaveleri, elden çıkarmaları, gerçeğe uygun değer düzeltmelerinden kaynaklanan net kazanç veya kayıpları ve transferleri gösterir.",
  "TMS 40 - GUD yönteminde açıklamalar")

q("Maliyet yöntemini uygulayan işletmenin gerçeğe uygun değer açıklaması bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım amaçlı gayrimenkullerin gerçeğe uygun değerini dipnotlarda açıklar",
  ["Maliyet yönteminde gerçeğe uygun değer hiçbir hâlde açıklanmak zorunda bulunmamaktadır",
   "Maliyet yönteminde yalnızca vergi değeri açıklanır; gerçeğe uygun değer belirtilmemektedir",
   "Maliyet yönteminde gerçeğe uygun değer her hâlde bilançoda gösterilmek zorunda tutulur",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 40: maliyet yöntemini uygulayan işletme, yatırım amaçlı gayrimenkullerinin GERÇEĞE UYGUN DEĞERİNİ dipnotlarda açıklar. Bu, iki yöntem arasında karşılaştırılabilirliği sağlar.",
  "TMS 40 - maliyet yönteminde GUD açıklaması")

q("Yatırım amaçlı gayrimenkullerin ölçümünde bağımsız değerleme uzmanı kullanılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanılması teşvik edilir ancak zorunlu değildir; kullanılıp kullanılmadığı açıklanır",
  ["Bağımsız değerleme uzmanı kullanılması her hâlde ve istisnasız zorunlu tutulmuş bulunmaktadır",
   "Bağımsız değerleme uzmanı kullanılması hiçbir hâlde kabul edilmeyen bir uygulamayı ifade eder",
   "Değerleme uzmanı kullanılsa dahi bu husus hiçbir hâlde açıklanmak zorunda bulunmamaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: işletmenin, ilgili yerdeki ve türdeki yatırım amaçlı gayrimenkuller konusunda güncel bilgisi bulunan, kabul görmüş ve mesleki açıdan yeterli bir değerleme uzmanının değerlemesine dayanması teşvik edilir; ancak zorunlu değildir. İşletme bu tür bir değerlemeye dayanıp dayanmadığını açıklar.",
  "TMS 40 - değerleme uzmanı")

q("Bir işletme yatırım amaçlı gayrimenkulünü gerçeğe uygun değer yöntemiyle ölçmekte ve değer artışını diğer kapsamlı gelire kaydetmektedir. TMS 40 bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulama yanlıştır; değer artışı kâr veya zarara yansıtılmalıdır",
  ["Uygulama doğrudur; TMS 40'ta değer artışı diğer kapsamlı gelire kaydedilmek zorundadır",
   "Uygulama doğrudur; artışın nereye kaydedileceği işletmenin serbest takdirine bırakılmıştır",
   "Uygulama yanlıştır; değer artışı her hâlde gayrimenkulün maliyetine eklenmek zorundadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gerçeğe uygun değer yönteminde değer değişiminden kaynaklanan kazanç veya kayıp, oluştuğu dönemde KÂR VEYA ZARARA dâhil edilir. Diğer kapsamlı gelire kaydetme TMS 16'daki yeniden değerleme modelidir; TMS 40'ta uygulanmaz.",
  "TMS 40 - GUD artışının yeri (senaryo)")

q("TMS 40 ile TMS 16'nın gerçeğe uygun değer yaklaşımları arasındaki fark bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 40'ta değer değişimi kâr veya zarara, TMS 16'da yeniden değerleme artışı diğer kapsamlı gelire gider",
  ["İki standartta da değer değişimi kâr veya zarara yansıtılır; aralarında hiçbir fark yoktur",
   "İki standartta da değer değişimi diğer kapsamlı gelire yansıtılır; aralarında hiçbir fark yoktur",
   "TMS 40'ta değer değişimi diğer kapsamlı gelire, TMS 16'da ise kâr veya zarara yansıtılmaktadır",
   "Bu fark hiçbir standartta düzenlenmemiş olup uygulamada dikkate alınmayan bir husustur"],
  "En kritik ayrım: TMS 40 gerçeğe uygun değer yönteminde değer değişimi (artış da azalış da) KÂR VEYA ZARARA yansıtılır ve amortisman ayrılmaz. TMS 16 yeniden değerleme modelinde ise artış diğer kapsamlı gelire gider, özkaynakta birikir ve varlık amortismana tabi tutulmaya devam eder.",
  "TMS 40 - TMS 16 ile fark")

q("Yatırım amaçlı gayrimenkullerin gerçeğe uygun değerinin ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değer TFRS 13'e göre ölçülür",
  ["Gerçeğe uygun değer her hâlde vergi değeri esas alınarak belirlenmek zorunda tutulmaktadır",
   "Gerçeğe uygun değer her hâlde gayrimenkulün ilk maliyeti esas alınarak belirlenmek zorundadır",
   "Gerçeğe uygun değerin nasıl ölçüleceği hiçbir standartta düzenlenmemiş bulunmaktadır",
   "Gerçeğe uygun değer her hâlde yönetimin serbest tahminine göre belirlenmek zorunda kalınır"],
  "TMS 40: yatırım amaçlı gayrimenkulün gerçeğe uygun değeri TFRS 13 Gerçeğe Uygun Değer Ölçümü uyarınca ölçülür.",
  "TMS 40 - GUD'ün ölçüm esası")

q("Yatırım amaçlı gayrimenkulle ilgili sonraki harcamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Muhasebeleştirme ölçütlerini karşılayan harcamalar defter değerine eklenir; günlük bakım gider yazılır",
  ["Tüm sonraki harcamalar her hâlde defter değerine eklenmek zorunda tutulan kalemleri ifade eder",
   "Tüm sonraki harcamalar her hâlde doğrudan gider yazılmak zorunda olup aktifleştirilemez",
   "Sonraki harcamalar hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gayrimenkulün günlük bakım maliyetleri defter değerine dâhil edilmez; oluştuklarında kâr veya zarara yansıtılır. Muhasebeleştirme ölçütlerini karşılayan sonraki harcamalar ise defter değerine eklenir.",
  "TMS 40 - sonraki harcamalar")

q("İnşa veya geliştirme aşamasındaki yatırım amaçlı gayrimenkul bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekte yatırım amaçlı kullanılmak üzere inşa edilen veya geliştirilen gayrimenkul TMS 40 kapsamındadır",
  ["İnşa aşamasındaki gayrimenkuller her hâlde TMS 16 kapsamında olup TMS 40 uygulanmamaktadır",
   "İnşa aşamasındaki gayrimenkuller her hâlde stok olarak sınıflandırılmak zorunda tutulmaktadır",
   "İnşa aşamasındaki gayrimenkuller hiçbir hâlde aktifleştirilemez; harcamalar gider yazılır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gelecekte yatırım amaçlı gayrimenkul olarak kullanılmak üzere inşa edilmekte veya geliştirilmekte olan gayrimenkul, yatırım amaçlı gayrimenkul örnekleri arasındadır ve TMS 40 kapsamındadır.",
  "TMS 40 - inşa hâlindeki gayrimenkul")

q("Aşağıdaki ifadelerden hangileri TMS 40 bakımından doğrudur?\n\nI. Elden çıkarma kazancı kâr veya zarara yansıtılır\n\nII. Maliyet yönteminde gerçeğe uygun değer dipnotta açıklanır\n\nIII. Yatırım amaçlı gayrimenkulün açılış maliyetleri varlığın maliyetine dâhil edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Elden çıkarma kazancı kâr veya zarara yansıtılır (I) ve maliyet yönteminde GUD dipnotta açıklanır (II). Gayrimenkulün AÇILIŞINA ilişkin başlangıç maliyetleri ise TMS 40 uyarınca maliyete DÂHİL EDİLMEZ; gider yazılır. Bu nedenle III yanlıştır.",
  "TMS 40 - genel")

q("Bir otel işletmesi, sahibi olduğu otel binasında konaklama hizmeti sunmaktadır. TMS 40 bakımından aşağıdakilerden hangisi doğrudur?",
  "Sunulan hizmetler önemli olduğundan bina sahibi tarafından kullanılandır; yatırım amaçlı değildir",
  ["Bina kira geliri sağladığından her hâlde yatırım amaçlı gayrimenkul sayılmak zorunda kalınır",
   "Bina her hâlde stok olarak sınıflandırılıp TMS 2 kapsamında ele alınmak zorunda tutulmaktadır",
   "Otel binaları hiçbir hâlde aktifleştirilemez; yalnızca dipnotlarda açıklanmak zorunda kalınır",
   "Bu husus TMS 40'ta düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 40: gayrimenkulü kullananlara sunulan tamamlayıcı hizmetler bir bütün olarak sözleşmenin ÖNEMLİ bir bölümünü oluşturuyorsa gayrimenkul sahibi tarafından kullanılandır. Otel işletmeciliğinde konuklara sunulan hizmetler önemli olduğundan otel binası yatırım amaçlı gayrimenkul değildir; TMS 16 kapsamındadır.",
  "TMS 40 - otel (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 40 bakımından doğrudur?\n\nI. Yatırım amaçlı gayrimenkul diğer varlıklardan büyük ölçüde bağımsız nakit akışı yaratır\n\nII. Ana ortaklığa kiraya verilen bina konsolide tablolarda yatırım amaçlıdır\n\nIII. Değerleme uzmanı kullanılması teşvik edilir ancak zorunlu değildir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Yatırım amaçlı gayrimenkul bağımsız nakit akışı yaratır (I) ve değerleme uzmanı kullanılması teşvik edilir ama zorunlu değildir (III). Grup içi kiralanan bina KONSOLİDE tablolarda yatırım amaçlı SAYILMAZ (grup açısından sahibi tarafından kullanılandır); yalnızca bireysel tablolarda yatırım amaçlıdır. Bu nedenle II yanlıştır.",
  "TMS 40 - genel")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 40; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
