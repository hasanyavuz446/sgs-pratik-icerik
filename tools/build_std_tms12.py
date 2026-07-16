# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 12 Gelir Vergileri — 60 soru.
Kaynak: KGK TMS 12. Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-10 soru, "hepsi" ~2 (%20-25).
⚠ YILA BAĞLI ORAN YOK: vergi oranı her hesap sorusunun KÖKÜNDE verilir; hiçbir
soruda "kurumlar vergisi oranı kaçtır" ya da güncel oranın bilinmesi sorulmaz."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_12_gelir_vergileri"
PREFIX, SEED = "std-tms12-gen", 20260906
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_12_gelir_vergileri.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Temel kavramlar (16) ────────────────────────────────────────────────
q("TMS 12'nin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelir vergilerinin muhasebeleştirilmesini düzenlemek ve cari ile gelecekteki vergisel sonuçları göstermektir",
  ["İşletmenin ödeyeceği vergi tutarını en aza indirecek yöntemleri belirlemeyi amaçlamaktadır",
   "Vergi mevzuatındaki oran ve istisnaları belirleyen bir düzenleme niteliğinde bulunmaktadır",
   "İşletmenin vergi beyannamesinin nasıl doldurulacağını gösteren bir rehber niteliğindedir",
   "TMS 12'nin belirlenmiş bir amacı bulunmayıp yalnızca biçimsel bir düzenleme niteliğindedir"],
  "TMS 12: bu Standardın amacı gelir vergilerinin muhasebeleştirilmesini düzenlemektir. Temel konu, cari dönem ve gelecek dönemlerdeki vergisel sonuçların nasıl muhasebeleştirileceğidir.",
  "TMS 12 - amaç")

q("TMS 12'ye göre muhasebe kârı bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi gideri düşülmeden önceki dönem kârı veya zararıdır",
  ["Vergi mevzuatına göre hesaplanan ve üzerinden vergi ödenen tutarı ifade eden bir kavramdır",
   "Vergi gideri düşüldükten sonra kalan net dönem kârını ifade eden bir kavram niteliğindedir",
   "İşletmenin ortaklara dağıttığı kâr payı tutarını ifade eden bir kavramı karşılamaktadır",
   "Muhasebe kârı TMS 12'de tanımlanmamış olup uygulamada kullanılmayan bir kavramı ifade eder"],
  "TMS 12: muhasebe kârı, vergi gideri düşülmeden önceki dönem kârı veya zararıdır.",
  "TMS 12 - muhasebe kârı")

q("TMS 12'ye göre vergiye tabi kâr (mali kâr) bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi otoritelerince konulan kurallara göre belirlenen ve üzerinden vergi ödenen dönem kârıdır",
  ["Vergi gideri düşülmeden önceki muhasebe kârını ifade eden bir kavramı karşılamak durumundadır",
   "Vergi gideri düşüldükten sonra kalan net dönem kârını ifade eden bir kavram niteliğindedir",
   "İşletmenin gelecekte elde etmeyi beklediği kârı ifade eden bir kavramı karşılamaktadır",
   "Vergiye tabi kâr TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 12: vergiye tabi kâr (mali zarar), vergi otoriteleri tarafından konulan hükümlere göre bir hesap dönemi için tespit edilen ve üzerinden vergi ödenen (vergi geri kazanılan) kârdır (zarardır).",
  "TMS 12 - vergiye tabi kâr")

q("Muhasebe kârı ile vergiye tabi kâr arasındaki ilişki bakımından aşağıdakilerden hangisi doğrudur?",
  "İkisi farklı kurallara göre belirlendiğinden birbirinden farklı olabilir",
  ["İkisi her hâlde ve istisnasız birbirine eşit olmak zorunda bulunan tutarları ifade etmektedir",
   "Muhasebe kârı her hâlde vergiye tabi kârdan yüksek olmak zorunda tutulan bir tutarı karşılar",
   "Muhasebe kârı her hâlde vergiye tabi kârdan düşük olmak zorunda olan bir tutarı ifade eder",
   "Bu ilişki TMS 12'de düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 12: muhasebe kârı TFRS'lere, vergiye tabi kâr ise vergi mevzuatına göre belirlenir. Farklı kurallar uygulandığından ikisi birbirinden farklı olabilir; bu farklar geçici veya sürekli nitelikte olabilir.",
  "TMS 12 - iki kâr arasındaki fark")

q("TMS 12'ye göre dönem vergi gideri bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem kârı veya zararının belirlenmesinde dikkate alınan cari vergi ile ertelenmiş vergi toplamıdır",
  ["Yalnızca vergi dairesine fiilen ödenen tutarı ifade eden dar kapsamlı bir kavram niteliğindedir",
   "Yalnızca ertelenmiş vergiyi ifade eden ve cari vergiyi kapsamayan bir kavramı karşılamaktadır",
   "Yalnızca vergi beyannamesinde gösterilen tutarı ifade eden bir kavramı karşılamak durumundadır",
   "Vergi gideri TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 12: vergi gideri (geliri), dönem kârı veya zararının belirlenmesinde dikkate alınan toplam cari vergi ve ertelenmiş vergi tutarıdır. Muhasebe, yalnızca ödenen vergiyi değil ertelenmiş etkiyi de gösterir.",
  "TMS 12 - vergi gideri")

q("TMS 12'ye göre cari vergi bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönemin vergiye tabi kârı üzerinden ödenecek veya geri kazanılacak gelir vergisi tutarıdır",
  ["Gelecek dönemlerde ödenecek olan vergileri ifade eden bir kavramı karşılamak durumundadır",
   "Geçici farklardan kaynaklanan ve ileride doğacak vergileri ifade eden bir kavram niteliğindedir",
   "İşletmenin geçmiş yıllarda ödediği tüm vergilerin toplamını ifade eden bir kavramı karşılar",
   "Cari vergi TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 12: dönem vergisi (cari vergi), bir hesap dönemindeki vergiye tabi kâr (mali zarar) üzerinden ödenecek (geri kazanılacak) gelir vergisi tutarıdır.",
  "TMS 12 - cari vergi")

q("Cari dönem ve önceki dönemlere ilişkin ödenmemiş vergi bakımından aşağıdakilerden hangisi doğrudur?",
  "Borç olarak muhasebeleştirilir; ödenen tutar borcu aşıyorsa aşan kısım varlık olarak kaydedilir",
  ["Ödenmemiş vergi hiçbir hâlde borç olarak muhasebeleştirilemez; yalnızca dipnotta açıklanır",
   "Fazla ödenen vergi hiçbir hâlde varlık olarak muhasebeleştirilemez; gider yazılmak zorundadır",
   "Vergi borçları her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemleri ifade eder",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: cari dönem ve önceki dönemlere ilişkin ödenmemiş vergiler borç olarak muhasebeleştirilir. Halihazırda ödenen tutar ilgili dönemlere ilişkin ödenmesi gereken tutarı aşarsa, aşan kısım varlık olarak muhasebeleştirilir.",
  "TMS 12 - cari vergi borcu ve varlığı")

q("TMS 12'ye göre vergiye esas değer bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir varlık veya borcun vergisel açıdan taşıdığı tutardır",
  ["Bir varlığın veya borcun finansal tablolardaki defter değerini ifade eden bir kavramdır",
   "Bir varlığın piyasada satılması hâlinde elde edilecek tutarı ifade eden bir kavram niteliğindedir",
   "Bir varlığın ilk edinildiği tarihteki maliyet bedelini ifade eden bir kavramı karşılamaktadır",
   "Vergiye esas değer TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 12: bir varlık veya borcun vergiye esas değeri, vergisel açıdan bunlara atfedilen tutardır. Geçici farklar, defter değeri ile vergiye esas değer karşılaştırılarak bulunur.",
  "TMS 12 - vergiye esas değer")

q("TMS 12'ye göre geçici farklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir varlık veya borcun defter değeri ile vergiye esas değeri arasındaki farklardır",
  ["Muhasebe kârı ile vergiye tabi kâr arasındaki ve hiçbir zaman ortadan kalkmayan farklardır",
   "İşletmenin geçmiş yıllarda ödediği vergiler ile ödenmesi gereken vergiler arasındaki farklardır",
   "İşletmenin farklı dönemlerde uyguladığı vergi oranları arasındaki farkları ifade etmektedir",
   "Geçici farklar TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 12: geçici farklar, bir varlık veya borcun finansal durum tablosundaki defter değeri ile bunların vergiye esas değerleri arasındaki farklardır. Zamanla ortadan kalkarlar; sürekli farklardan bu yönüyle ayrılırlar.",
  "TMS 12 - geçici farklar")

q("Vergiye tabi geçici farklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecek dönemlerde vergiye tabi tutar doğuran farklardır; ertelenmiş vergi BORCU yaratır",
  ["Gelecek dönemlerde indirilebilir tutar doğuran farklardır; ertelenmiş vergi VARLIĞI yaratır",
   "Hiçbir zaman ortadan kalkmayan ve vergisel sonuç doğurmayan farkları ifade etmektedir",
   "Yalnızca cari dönemi etkileyen ve gelecek dönemlere sarkmayan farkları ifade eden kavramdır",
   "Bu kavram TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 12: vergiye tabi geçici farklar, gelecek dönemlerde varlığın defter değeri geri kazanıldığında veya borcun defter değeri ödendiğinde vergiye tabi tutar oluşmasına neden olan geçici farklardır. Bunlar ertelenmiş vergi BORCU doğurur.",
  "TMS 12 - vergiye tabi geçici farklar")

q("İndirilebilir geçici farklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecek dönemlerde indirilebilir tutar doğuran farklardır; ertelenmiş vergi VARLIĞI yaratır",
  ["Gelecek dönemlerde vergiye tabi tutar doğuran farklardır; ertelenmiş vergi BORCU yaratır",
   "Hiçbir zaman ortadan kalkmayan ve vergisel sonuç doğurmayan farkları ifade etmek durumundadır",
   "Yalnızca cari dönemi etkileyen ve gelecek dönemlere sarkmayan farkları ifade eden kavramdır",
   "Bu kavram TMS 12'de tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 12: indirilebilir geçici farklar, gelecek dönemlerde varlığın defter değeri geri kazanıldığında veya borcun defter değeri ödendiğinde vergiye tabi kârın tespitinde indirilebilir tutar oluşmasına neden olan geçici farklardır. Bunlar ertelenmiş vergi VARLIĞI doğurur.",
  "TMS 12 - indirilebilir geçici farklar")

q("Ertelenmiş vergi borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiye tabi geçici farklar üzerinden gelecek dönemlerde ödenecek gelir vergisi tutarıdır",
  ["İndirilebilir geçici farklar üzerinden gelecekte geri kazanılacak vergi tutarını ifade eder",
   "Cari dönemde vergi dairesine fiilen ödenmesi gereken vergi tutarını ifade eden bir kavramdır",
   "İşletmenin geçmiş yıllarda fazla ödediği vergilerin toplamını ifade eden bir kavram niteliğindedir",
   "Ertelenmiş vergi borcu TMS 12'de tanımlanmamış bir husus niteliğinde bulunmak durumundadır"],
  "TMS 12: ertelenmiş vergi borçları, vergiye tabi geçici farklar üzerinden gelecek dönemlerde ödenecek gelir vergisi tutarlarıdır.",
  "TMS 12 - ertelenmiş vergi borcu")

q("Ertelenmiş vergi varlığı bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirilebilir geçici farklar, devreden mali zararlar ve vergi avantajları üzerinden geri kazanılacak vergi tutarlarıdır",
  ["Vergiye tabi geçici farklar üzerinden gelecekte ödenecek vergi tutarlarını ifade etmektedir",
   "Cari dönemde vergi dairesine fiilen ödenmesi gereken vergi tutarını ifade eden bir kavramdır",
   "İşletmenin gelecekte elde etmeyi beklediği kâr tutarını ifade eden bir kavramı karşılamaktadır",
   "Ertelenmiş vergi varlığı TMS 12'de tanımlanmamış bir husus niteliğinde bulunmak durumundadır"],
  "TMS 12: ertelenmiş vergi varlıkları, (a) indirilebilir geçici farklar, (b) gelecek dönemlere devreden kullanılmamış mali zararlar ve (c) gelecek dönemlere devreden kullanılmamış vergi avantajları nedeniyle gelecek dönemlerde geri kazanılacak gelir vergisi tutarlarıdır.",
  "TMS 12 - ertelenmiş vergi varlığı")

q("Aşağıdakilerden hangileri ertelenmiş vergi VARLIĞI doğurur?\n\nI. İndirilebilir geçici farklar\n\nII. Gelecek dönemlere devreden kullanılmamış mali zararlar\n\nIII. Gelecek dönemlere devreden kullanılmamış vergi avantajları",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 12 üçünü de ertelenmiş vergi varlığı kaynağı olarak sayar: indirilebilir geçici farklar (I), devreden kullanılmamış mali zararlar (II) ve devreden kullanılmamış vergi avantajları (III).",
  "TMS 12 - ertelenmiş vergi varlığı kaynakları")

q("Aşağıdaki ifadelerden hangileri TMS 12 bakımından doğrudur?\n\nI. Geçici fark, defter değeri ile vergiye esas değer arasındaki farktır\n\nII. Vergiye tabi geçici fark ertelenmiş vergi borcu doğurur\n\nIII. İndirilebilir geçici fark ertelenmiş vergi borcu doğurur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Geçici fark defter değeri ile vergiye esas değer arasındaki farktır (I) ve vergiye tabi geçici fark ertelenmiş vergi BORCU doğurur (II). İndirilebilir geçici fark ise ertelenmiş vergi VARLIĞI doğurur; bu nedenle III yanlıştır.",
  "TMS 12 - geçici farklar")

q("Bir varlığın defter değerinin vergiye esas değerinden YÜKSEK olması bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilir",
  ["İndirilebilir geçici fark doğar; ertelenmiş vergi varlığı muhasebeleştirilmek zorundadır",
   "Hiçbir geçici fark doğmaz; iki değer arasındaki fark dikkate alınmamak zorunda kalınmaktadır",
   "Sürekli fark doğar; hiçbir hâlde ertelenmiş vergi muhasebeleştirilmemek durumundadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: bir VARLIĞIN defter değeri vergiye esas değerinden yüksekse, gelecekte geri kazanılacak ekonomik yarar vergisel olarak indirilebilecek tutarı aşar. Bu bir VERGİYE TABİ geçici farktır ve ertelenmiş vergi borcu doğurur.",
  "TMS 12 - varlıkta fark yönü")

# ── B. Muhasebeleştirme ve ölçüm (16) ──────────────────────────────────────
q("Ertelenmiş vergi borçlarının muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Standartta sayılan istisnalar dışında tüm vergiye tabi geçici farklar için muhasebeleştirilir",
  ["Hiçbir hâlde muhasebeleştirilmez; yalnızca dipnotlarda açıklanmakla yetinilmek zorundadır",
   "Yalnızca işletmenin muhasebeleştirmeyi tercih ettiği farklar için kaydedilmek zorunda kalınır",
   "Yalnızca vergi idaresi talep ettiğinde muhasebeleştirilmek zorunda olan kalemleri ifade eder",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi borcu, şerefiyenin ilk muhasebeleştirilmesinden ve belirli ilk muhasebeleştirme istisnalarından kaynaklananlar dışında, tüm vergiye tabi geçici farklar için muhasebeleştirilir.",
  "TMS 12 - ertelenmiş vergi borcunun kaydı")

q("Ertelenmiş vergi varlıklarının muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirilebilir geçici farkın kullanılmasına yetecek vergiye tabi kâr elde edilmesi muhtemel olduğu ölçüde muhasebeleştirilir",
  ["Vergiye tabi kâr beklentisine bakılmaksızın her hâlde tamamı muhasebeleştirilmek zorundadır",
   "Hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotlarda açıklanmakla yetinilmek zorunda kalınır",
   "Yalnızca vergi idaresi izin verdiğinde muhasebeleştirilebilen bir kalemi ifade etmek durumundadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlığı, indirilebilir geçici farkın kullanılmasına yeterli olacak tutarda vergiye tabi kâr elde edileceğinin MUHTEMEL olması ölçüsünde muhasebeleştirilir. Bu koşul, ertelenmiş vergi borcunda aranmaz — ihtiyatlılık gereği asimetriktir.",
  "TMS 12 - ertelenmiş vergi varlığının kaydı")

q("Kullanılmamış mali zararlar için ertelenmiş vergi varlığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Mahsup edilebilecek vergiye tabi kâr elde edilmesi muhtemel olduğu ölçüde muhasebeleştirilir",
  ["Mali zararlar için hiçbir hâlde ertelenmiş vergi varlığı muhasebeleştirilememek zorundadır",
   "Mali zararlar için her hâlde ve koşulsuz olarak ertelenmiş vergi varlığı kaydedilmek zorundadır",
   "Mali zararlar her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemleri ifade eder",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: kullanılmamış mali zararların ve vergi avantajlarının mahsup edilebileceği vergiye tabi kâr elde edilmesinin muhtemel olması ölçüsünde ertelenmiş vergi varlığı muhasebeleştirilir. Geçmişteki zarar geçmişi, muhtemelliğin değerlendirilmesinde güçlü bir kanıttır.",
  "TMS 12 - mali zararlar")

q("Ertelenmiş vergi varlık ve borçlarının ölçümünde kullanılacak oran bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın gerçekleşeceği veya borcun ödeneceği dönemde geçerli olması beklenen vergi oranıdır",
  ["Her hâlde cari dönemde geçerli olan vergi oranı kullanılmak zorunda tutulan bir orandır",
   "Her hâlde geçmiş dönemlerde uygulanmış olan ortalama vergi oranı kullanılmak zorundadır",
   "Her hâlde işletmenin seçtiği herhangi bir oran serbestçe kullanılabilmek zorunda kalınır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlık ve borçları, varlığın gerçekleşeceği veya borcun ödeneceği dönemde uygulanması beklenen vergi oranları üzerinden, raporlama dönemi sonu itibarıyla yasalaşmış veya yasalaşması kesine yakın oranlar kullanılarak ölçülür.",
  "TMS 12 - ertelenmiş verginin ölçüm oranı")

q("Ertelenmiş vergi varlık ve borçlarının iskonto edilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İskonto edilmez",
  ["Her hâlde ve istisnasız iskonto edilmek zorunda olan kalemleri ifade etmek durumundadır",
   "Yalnızca vadesi bir yılı aşanlar iskonto edilmek zorunda olup diğerleri nominal kalmaktadır",
   "İskonto edilip edilmeyeceği işletmenin serbest takdirine bırakılmış bir husus niteliğindedir",
   "Bu husus TMS 12'de düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlıkları ve borçları İSKONTO EDİLMEZ. Geçici farkların çözülme zamanlamasının güvenilir biçimde belirlenmesi çoğu durumda karmaşık olacağından iskonto zorunlu tutulmamış, isteğe bağlı iskonto da yasaklanmıştır.",
  "TMS 12 - iskonto yasağı")

q("Ertelenmiş vergi varlığının defter değerinin gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Her raporlama dönemi sonunda gözden geçirilir; yeterli vergiye tabi kâr muhtemel değilse azaltılır",
  ["Bir kez muhasebeleştirildikten sonra hiçbir hâlde gözden geçirilmemek zorunda kalınmaktadır",
   "Yalnızca vergi idaresi talep ettiğinde gözden geçirilmek zorunda olan bir kalemi ifade eder",
   "Her hâlde her dönem artırılmak zorunda olup hiçbir hâlde azaltılamayan bir kalemi karşılar",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlığının defter değeri her raporlama dönemi sonunda gözden geçirilir. Ertelenmiş vergi varlığının bir kısmının veya tamamının yararlanılmasına yetecek vergiye tabi kâr elde edilmesi artık muhtemel değilse defter değeri azaltılır. Sonradan muhtemel hâle gelirse azaltma iptal edilir.",
  "TMS 12 - EVV'nin gözden geçirilmesi")

q("Cari ve ertelenmiş verginin muhasebeleştirileceği yer bakımından aşağıdakilerden hangisi doğrudur?",
  "İlgili işlem kâr veya zararda muhasebeleştiriliyorsa vergi de kâr veya zararda muhasebeleştirilir",
  ["Vergi her hâlde ve istisnasız kâr veya zararda muhasebeleştirilmek zorunda tutulmaktadır",
   "Vergi her hâlde ve istisnasız diğer kapsamlı gelirde muhasebeleştirilmek zorunda kalınır",
   "Vergi her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: cari ve ertelenmiş vergi, verginin ilgili olduğu işlem veya olayın muhasebeleştirildiği yerle aynı yerde muhasebeleştirilir. İşlem kâr veya zararda ise vergi de kâr veya zararda; diğer kapsamlı gelirde ise vergi de orada muhasebeleştirilir.",
  "TMS 12 - verginin muhasebeleştirileceği yer")

q("Diğer kapsamlı gelirde muhasebeleştirilen bir işleme ilişkin vergi bakımından aşağıdakilerden hangisi doğrudur?",
  "İlgili vergi de diğer kapsamlı gelirde muhasebeleştirilir",
  ["İlgili vergi her hâlde kâr veya zararda muhasebeleştirilmek zorunda tutulan bir kalemdir",
   "İlgili vergi hiçbir hâlde muhasebeleştirilmez; yalnızca dipnotta açıklanmak zorunda kalınır",
   "İlgili vergi her hâlde varlığın maliyetine eklenmek zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: kâr veya zarar dışında muhasebeleştirilen işlem ve olaylara ilişkin cari ve ertelenmiş vergi, kâr veya zarar dışında muhasebeleştirilir. Diğer kapsamlı gelirde muhasebeleştirilen bir kaleme (TMS 16 yeniden değerleme artışı gibi) ilişkin vergi de diğer kapsamlı gelirde muhasebeleştirilir.",
  "TMS 12 - DKG'deki işlemin vergisi")

q("Ertelenmiş vergi varlık ve borçlarının finansal durum tablosunda sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönen varlık veya kısa vadeli borç olarak sınıflandırılmaz",
  ["Her hâlde dönen varlık veya kısa vadeli borç olarak sınıflandırılmak zorunda tutulmaktadır",
   "Her hâlde vadesine göre dönen ve duran olarak ikiye ayrılmak zorunda olan kalemleri ifade eder",
   "Hiçbir hâlde finansal durum tablosunda gösterilmez; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: işletme finansal durum tablosunda dönen/duran varlık ve kısa/uzun vadeli borç ayrımı yapıyorsa, ertelenmiş vergi varlıklarını (borçlarını) dönen varlık (kısa vadeli borç) olarak sınıflandırmaz.",
  "TMS 12 - ertelenmiş verginin sınıflandırılması")

q("Ertelenmiş vergi varlık ve borçlarının netleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yasal mahsup hakkı varsa ve aynı vergi idaresi ile aynı vergi mükellefine ilişkinse netleştirilir",
  ["Her hâlde ve koşulsuz olarak netleştirilmek zorunda olan kalemleri ifade etmek durumundadır",
   "Hiçbir hâlde netleştirilemez; her zaman brüt olarak gösterilmek zorunda kalınmaktadır",
   "Netleştirme yalnızca vergi idaresi izin verdiğinde yapılabilmek zorunda bulunmaktadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlıkları ve borçları ancak (a) işletmenin cari vergi varlıklarını cari vergi borçlarına mahsup etmek için yasal olarak uygulanabilir bir hakkı varsa ve (b) bunlar aynı vergi idaresince aynı vergi mükellefinden alınan gelir vergileriyle ilgiliyse netleştirilir.",
  "TMS 12 - netleştirme")

mk, gecici, oran12 = 1_000_000, 200_000, 25
ertelenmis = gecici * oran12 / 100
q(f"Bir işletmenin bir varlığının defter değeri, vergiye esas değerinden {tr(gecici)} TL yüksektir. İlgili dönemde uygulanması beklenen vergi oranı %{oran12}'tir. TMS 12'ye göre muhasebeleştirilecek ertelenmiş vergi tutarı ve niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  f"{tr(ertelenmis)} TL ertelenmiş vergi borcu",
  [f"{tr(ertelenmis)} TL ertelenmiş vergi varlığı olarak muhasebeleştirilmek zorunda bulunmaktadır",
   f"{tr(gecici)} TL ertelenmiş vergi borcu olarak kaydedilir; oran uygulanmadan farkın tamamı yazılır",
   f"{tr(gecici)} TL ertelenmiş vergi varlığı olarak kaydedilir; oran hiç dikkate alınmamaktadır",
   "Hiçbir kayıt yapılmaz; defter değeri ile vergiye esas değer farkı dikkate alınmamak durumundadır"],
  f"Varlığın defter değeri vergiye esas değerinden YÜKSEK olduğundan VERGİYE TABİ geçici fark doğar → ertelenmiş vergi BORCU. Tutar = Geçici fark × Oran = {tr(gecici)} × %{oran12} = {tr(ertelenmis)} TL.",
  "TMS 12 - ertelenmiş vergi borcu hesabı")

gecici2, oran2 = 160_000, 25
ev2 = gecici2 * oran2 / 100
q(f"Bir işletmenin bir borcunun defter değeri {tr(gecici2)} TL olup vergiye esas değeri sıfırdır (gider ancak fiilen ödendiğinde vergi matrahından indirilebilmektedir). İlgili dönemde uygulanması beklenen vergi oranı %{oran2}'tir. Muhasebeleştirilecek ertelenmiş vergi tutarı ve niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  f"{tr(ev2)} TL ertelenmiş vergi varlığı",
  [f"{tr(ev2)} TL ertelenmiş vergi borcu olarak muhasebeleştirilmek zorunda olan bir kalemdir",
   f"{tr(gecici2)} TL ertelenmiş vergi varlığı olarak kaydedilir; oran uygulanmadan fark yazılır",
   f"{tr(gecici2)} TL ertelenmiş vergi borcu olarak kaydedilir; oran hiç dikkate alınmamaktadır",
   "Hiçbir kayıt yapılmaz; borcun vergiye esas değeri sıfır olduğundan fark doğmamak durumundadır"],
  f"Bir BORCUN defter değeri ({tr(gecici2)} TL) vergiye esas değerinden (0) yüksekse, gelecekte ödendiğinde vergi matrahından indirilecektir → İNDİRİLEBİLİR geçici fark → ertelenmiş vergi VARLIĞI. Tutar = {tr(gecici2)} × %{oran2} = {tr(ev2)} TL (yeterli vergiye tabi kâr muhtemelse).",
  "TMS 12 - ertelenmiş vergi varlığı hesabı")

zarar12, oran3 = 400_000, 25
ev3 = zarar12 * oran3 / 100
q(f"Bir işletmenin gelecek dönemlere devreden {tr(zarar12)} TL kullanılmamış mali zararı bulunmakta ve bu zararın mahsup edilebileceği vergiye tabi kâr elde edilmesi muhtemeldir. Uygulanması beklenen vergi oranı %{oran3}'tir. Muhasebeleştirilecek ertelenmiş vergi varlığı kaç TL'dir?",
  f"{tr(ev3)} TL",
  [f"{tr(zarar12)} TL", f"{tr(zarar12 * 2)} TL", f"{tr(zarar12 / 2)} TL", "0 TL"],
  f"Devreden mali zarar, gelecekte vergi matrahından indirileceğinden ertelenmiş vergi VARLIĞI doğurur. Tutar = Mali zarar × Oran = {tr(zarar12)} × %{oran3} = {tr(ev3)} TL. Muhasebeleştirme, mahsup edilecek vergiye tabi kâr elde edilmesinin MUHTEMEL olması koşuluna bağlıdır.",
  "TMS 12 - mali zararda EVV hesabı")

mali_kar, oran4 = 800_000, 25
cari_v = mali_kar * oran4 / 100
q(f"Bir işletmenin dönem vergiye tabi kârı (mali kârı) {tr(mali_kar)} TL, cari dönemde geçerli vergi oranı %{oran4}'tir. Dönemin cari vergi tutarı kaç TL'dir?",
  f"{tr(cari_v)} TL",
  [f"{tr(mali_kar)} TL", f"{tr(mali_kar * 2)} TL", f"{tr(mali_kar / 2)} TL", "0 TL"],
  f"Cari vergi = Vergiye tabi kâr × Vergi oranı = {tr(mali_kar)} × %{oran4} = {tr(cari_v)} TL. Cari vergi, dönem vergiye tabi kârı üzerinden ödenecek gelir vergisi tutarıdır.",
  "TMS 12 - cari vergi hesabı")

q("Aşağıdaki ifadelerden hangileri ertelenmiş verginin ölçümü bakımından doğrudur?\n\nI. Gerçekleşeceği dönemde beklenen vergi oranı kullanılır\n\nII. Ertelenmiş vergi varlık ve borçları iskonto edilmez\n\nIII. Ertelenmiş vergi varlıkları dönen varlık olarak sınıflandırılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Gerçekleşeceği dönemde beklenen (yasalaşmış veya yasalaşması kesine yakın) oran kullanılır (I) ve ertelenmiş vergi iskonto EDİLMEZ (II). Ertelenmiş vergi varlıkları dönen varlık olarak SINIFLANDIRILMAZ; bu nedenle III yanlıştır.",
  "TMS 12 - ölçüm")

q("Aşağıdaki ifadelerden hangileri TMS 12 bakımından doğrudur?\n\nI. Ertelenmiş vergi varlığı, yeterli vergiye tabi kâr muhtemelse muhasebeleştirilir\n\nII. Ertelenmiş vergi varlığının defter değeri her dönem sonunda gözden geçirilir\n\nIII. Ertelenmiş vergi borcu da yalnızca vergiye tabi kâr muhtemelse muhasebeleştirilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Ertelenmiş vergi VARLIĞI yeterli vergiye tabi kâr muhtemelse muhasebeleştirilir (I) ve her dönem sonunda gözden geçirilir (II). Ertelenmiş vergi BORCUNDA ise böyle bir muhtemellik koşulu ARANMAZ; istisnalar dışında tüm vergiye tabi geçici farklar için kaydedilir. Bu asimetri ihtiyatlılık gereğidir; III yanlıştır.",
  "TMS 12 - muhasebeleştirme")

# ── C. Uygulama ve özel konular (14) ───────────────────────────────────────
q("Bir makinenin muhasebe amortismanının vergi amortismanından DÜŞÜK olması bakımından aşağıdakilerden hangisi doğrudur?",
  "Defter değeri vergiye esas değerden yüksek olur; vergiye tabi geçici fark ve ertelenmiş vergi borcu doğar",
  ["Defter değeri vergiye esas değerden düşük olur; ertelenmiş vergi varlığı doğmak zorundadır",
   "Hiçbir geçici fark doğmaz; amortisman farkları dikkate alınmamak zorunda kalınmaktadır",
   "Sürekli fark doğar; hiçbir hâlde ertelenmiş vergi muhasebeleştirilmemek zorunda tutulur",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "Vergi amortismanı daha hızlıysa vergiye esas değer daha hızlı azalır; varlığın defter değeri vergiye esas değerinden YÜKSEK kalır. Bu vergiye tabi geçici farktır ve ertelenmiş vergi BORCU doğurur. Fark ilerleyen yıllarda ters döner.",
  "TMS 12 - amortisman farkı (senaryo)")

q("Vergi matrahından ancak fiilen ödendiğinde indirilebilen bir gider karşılığı bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirilebilir geçici fark doğar; ertelenmiş vergi varlığı muhasebeleştirilir",
  ["Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilmek zorunda kalınır",
   "Hiçbir geçici fark doğmaz; karşılıklar vergisel açıdan dikkate alınmamak zorunda tutulur",
   "Sürekli fark doğar; hiçbir hâlde ertelenmiş vergi muhasebeleştirilmemek zorunda bulunmaktadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "Karşılık muhasebede gider yazılmış ancak vergisel olarak henüz indirilmemiştir; borcun defter değeri vergiye esas değerinden (sıfır) yüksektir. Gelecekte ödendiğinde matrahtan indirilecektir → İNDİRİLEBİLİR geçici fark → ertelenmiş vergi VARLIĞI (yeterli vergiye tabi kâr muhtemelse).",
  "TMS 12 - karşılıkta geçici fark (senaryo)")

q("Vergi mevzuatınca hiçbir zaman indirilemeyecek bir gider (kanunen kabul edilmeyen gider) bakımından aşağıdakilerden hangisi doğrudur?",
  "Sürekli fark doğar; ertelenmiş vergi muhasebeleştirilmez",
  ["İndirilebilir geçici fark doğar; ertelenmiş vergi varlığı muhasebeleştirilmek zorundadır",
   "Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilmek zorunda kalınır",
   "Bu gider hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorunda bulunur",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "Hiçbir zaman vergi matrahından indirilemeyecek giderler SÜREKLİ fark doğurur; ilerleyen dönemlerde ters dönmezler. TMS 12 yalnızca GEÇİCİ farklar üzerinden ertelenmiş vergi muhasebeleştirilmesini öngörür; sürekli farklar için ertelenmiş vergi kaydedilmez.",
  "TMS 12 - sürekli fark")

q("Şerefiyenin ilk muhasebeleştirilmesinden doğan vergiye tabi geçici fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Ertelenmiş vergi borcu muhasebeleştirilmez",
  ["Her hâlde ertelenmiş vergi borcu muhasebeleştirilmek zorunda olan bir durumu ifade etmektedir",
   "Her hâlde ertelenmiş vergi varlığı muhasebeleştirilmek zorunda tutulan bir durumu karşılar",
   "Şerefiye hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorunda kalınır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: şerefiyenin ilk muhasebeleştirilmesinden kaynaklanan vergiye tabi geçici fark için ertelenmiş vergi borcu muhasebeleştirilmez. Şerefiye artık değer olarak ölçüldüğünden ertelenmiş vergi borcu kaydedilmesi şerefiyeyi artırır ve döngüsel bir sonuç doğururdu.",
  "TMS 12 - şerefiye istisnası")

q("İlk muhasebeleştirme istisnası bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme birleşmesi olmayan ve ne muhasebe ne vergiye tabi kârı etkilemeyen bir işlemde ertelenmiş vergi kaydedilmez",
  ["Her işlemde ertelenmiş vergi muhasebeleştirilmek zorunda olup hiçbir istisna bulunmamaktadır",
   "İlk muhasebeleştirmede hiçbir hâlde ertelenmiş vergi muhasebeleştirilememek zorunda kalınır",
   "İstisna yalnızca vergi idaresi izin verdiğinde uygulanabilmek zorunda olan bir kuralı ifade eder",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: bir varlık veya borcun, işletme birleşmesi işlemi olmayan ve gerçekleştiği tarihte ne muhasebe kârını ne de vergiye tabi kârı etkilemeyen bir işlemdeki ilk muhasebeleştirilmesinden kaynaklanan geçici farklar için ertelenmiş vergi muhasebeleştirilmez.",
  "TMS 12 - ilk muhasebeleştirme istisnası")

q("Yeniden değerlenen bir maddi duran varlığa ilişkin ertelenmiş vergi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeniden değerleme diğer kapsamlı gelirde muhasebeleştirildiğinden ilgili ertelenmiş vergi de orada muhasebeleştirilir",
  ["İlgili ertelenmiş vergi her hâlde kâr veya zararda muhasebeleştirilmek zorunda tutulmaktadır",
   "Yeniden değerlemede hiçbir hâlde ertelenmiş vergi doğmaz; vergisel etki bulunmamak zorundadır",
   "İlgili ertelenmiş vergi her hâlde varlığın maliyetine eklenmek zorunda olan bir kalemdir",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: vergi, ilgili olduğu işlemin muhasebeleştirildiği yerde muhasebeleştirilir. Yeniden değerleme artışı diğer kapsamlı gelirde muhasebeleştirildiğinden, artıştan doğan vergiye tabi geçici farkın ertelenmiş vergisi de DİĞER KAPSAMLI GELİRDE muhasebeleştirilir.",
  "TMS 12 - yeniden değerlemenin vergisi")

q("Bir işletmenin ertelenmiş vergi varlığı bulunmakta ancak gelecekte yeterli vergiye tabi kâr elde etmesi artık muhtemel görünmemektedir. TMS 12 bakımından aşağıdakilerden hangisi doğrudur?",
  "Ertelenmiş vergi varlığının defter değeri azaltılır",
  ["Ertelenmiş vergi varlığı her hâlde defter değeriyle korunmak zorunda olan bir kalemi ifade eder",
   "Ertelenmiş vergi varlığı her hâlde artırılmak zorunda olup azaltılamayan bir kalemi karşılar",
   "Ertelenmiş vergi varlığı her hâlde ertelenmiş vergi borcuna dönüştürülmek zorunda kalınır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlığının bir kısmının veya tamamının yararlanılmasına yetecek vergiye tabi kâr elde edilmesi artık muhtemel değilse, ertelenmiş vergi varlığının defter değeri azaltılır. Sonradan tekrar muhtemel hâle gelirse bu azaltma iptal edilir.",
  "TMS 12 - EVV'nin azaltılması (senaryo)")

q("Bağlı ortaklık, şube, iştirak ve iş ortaklıklarındaki yatırımlara ilişkin geçici farklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Ana ortaklık farkın ters dönme zamanını kontrol edebiliyorsa ve yakın gelecekte dönmesi muhtemel değilse borç kaydedilmez",
  ["Bu farklar için her hâlde ve koşulsuz olarak ertelenmiş vergi borcu kaydedilmek zorundadır",
   "Bu farklar için hiçbir hâlde ertelenmiş vergi muhasebeleştirilememek zorunda bulunmaktadır",
   "Bu farklar her hâlde sürekli fark sayılıp hiçbir vergisel etki doğurmamak zorunda kalınır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: bağlı ortaklık, şube, iştirak ve iş ortaklıklarındaki yatırımlarla ilgili tüm vergiye tabi geçici farklar için ertelenmiş vergi borcu muhasebeleştirilir. Ancak (a) ana ortaklık farkın ters dönme zamanını kontrol edebiliyorsa ve (b) farkın öngörülebilir gelecekte ters dönmesi muhtemel değilse muhasebeleştirilmez.",
  "TMS 12 - iştiraklerdeki yatırımlar")

q("Vergi giderine ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi giderinin ana bileşenleri ile muhasebe kârı ve vergi gideri arasındaki ilişkinin mutabakatı açıklanır",
  ["Vergi gideri hakkında hiçbir açıklama yapılmaz; yalnızca tutar tabloda gösterilmek zorundadır",
   "Yalnızca ödenen vergi tutarı açıklanır; ertelenmiş vergi hiçbir hâlde açıklanmamak durumundadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca zarar eden işletmeler için zorunlu tutulmuş bir husus niteliğinde bulunur"],
  "TMS 12: vergi gideri (geliri) ile ilgili ana unsurlar ayrı ayrı açıklanır. Ayrıca muhasebe kârı ile vergi gideri arasındaki ilişkiye dair sayısal mutabakat ve her bir geçici fark türü için ertelenmiş vergi tutarları açıklanır.",
  "TMS 12 - açıklamalar")

mk2, kkeg, oran5 = 1_000_000, 100_000, 25
mali2 = mk2 + kkeg
cari2 = mali2 * oran5 / 100
q(f"Bir işletmenin muhasebe kârı {tr(mk2)} TL'dir. Dönemde {tr(kkeg)} TL kanunen kabul edilmeyen gider bulunmakta, başka bir fark yoktur. Vergi oranı %{oran5} ise dönemin cari vergi tutarı kaç TL'dir?",
  f"{tr(cari2)} TL",
  [f"{tr(mk2 * oran5 / 100)} TL", f"{tr((mk2 - kkeg) * oran5 / 100)} TL", f"{tr(mali2)} TL", f"{tr(kkeg * oran5 / 100)} TL"],
  f"Kanunen kabul edilmeyen gider matraha eklenir: Vergiye tabi kâr = {tr(mk2)} + {tr(kkeg)} = {tr(mali2)} TL. Cari vergi = {tr(mali2)} × %{oran5} = {tr(cari2)} TL. Bu bir SÜREKLİ farktır; ertelenmiş vergi doğurmaz.",
  "TMS 12 - sürekli fark ve cari vergi hesabı")

dd12, ved12, oran6 = 500_000, 380_000, 25
fark12 = dd12 - ved12
evb12 = fark12 * oran6 / 100
q(f"Bir makinenin defter değeri {tr(dd12)} TL, vergiye esas değeri {tr(ved12)} TL'dir. Uygulanması beklenen vergi oranı %{oran6}'tir. Muhasebeleştirilecek ertelenmiş vergi borcu kaç TL'dir?",
  f"{tr(evb12)} TL",
  [f"{tr(fark12)} TL", f"{tr(dd12 * oran6 / 100)} TL", f"{tr(ved12 * oran6 / 100)} TL", "0 TL"],
  f"Geçici fark = Defter değeri − Vergiye esas değer = {tr(dd12)} − {tr(ved12)} = {tr(fark12)} TL. Varlığın defter değeri yüksek olduğundan VERGİYE TABİ geçici farktır. Ertelenmiş vergi borcu = {tr(fark12)} × %{oran6} = {tr(evb12)} TL.",
  "TMS 12 - EVB hesabı")

cari3, ert_artis, oran7 = 200_000, 30_000, 25
top_gider = cari3 + ert_artis
q(f"Bir işletmenin dönem cari vergisi {tr(cari3)} TL, ertelenmiş vergi borcundaki artış {tr(ert_artis)} TL'dir. Başka bir ertelenmiş vergi hareketi yoktur. Kâr veya zarar tablosunda gösterilecek toplam vergi gideri kaç TL'dir?",
  f"{tr(top_gider)} TL",
  [f"{tr(cari3)} TL", f"{tr(cari3 - ert_artis)} TL", f"{tr(ert_artis)} TL", "0 TL"],
  f"TMS 12: vergi gideri = Cari vergi + Ertelenmiş vergi = {tr(cari3)} + {tr(ert_artis)} = {tr(top_gider)} TL. Ertelenmiş vergi borcundaki artış vergi giderini artırır; yalnızca ödenen vergi gösterilmez.",
  "TMS 12 - toplam vergi gideri hesabı")

q("Aşağıdakilerden hangisi TMS 12'ye göre ertelenmiş vergi DOĞURMAZ?",
  "Kanunen kabul edilmeyen giderler",
  ["Muhasebe amortismanı ile vergi amortismanı arasındaki fark niteliğindeki geçici farkların tümü",
   "Ancak fiilen ödendiğinde indirilebilen gider karşılıkları niteliğindeki geçici farkların tamamı",
   "Gelecek dönemlere devreden kullanılmamış mali zararlar niteliğindeki kalemlerin tamamı",
   "Şüpheli alacak karşılığının vergisel olarak henüz indirilmemiş olması niteliğindeki farklar"],
  "Kanunen kabul edilmeyen giderler SÜREKLİ fark doğurur; hiçbir zaman ters dönmediğinden ertelenmiş vergi doğurmaz. Diğer şıkların tamamı geçici fark veya devreden zarar niteliğinde olup ertelenmiş vergi doğurur.",
  "TMS 12 - ertelenmiş vergi doğurmayan")

q("Aşağıdaki ifadelerden hangileri TMS 12 bakımından doğrudur?\n\nI. Sürekli farklar için ertelenmiş vergi muhasebeleştirilmez\n\nII. Şerefiyenin ilk muhasebeleştirilmesinden doğan fark için ertelenmiş vergi borcu kaydedilmez\n\nIII. Diğer kapsamlı gelirdeki bir kaleme ilişkin vergi kâr veya zararda muhasebeleştirilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sürekli farklar için ertelenmiş vergi kaydedilmez (I) ve şerefiyenin ilk muhasebeleştirilmesinden doğan fark için ertelenmiş vergi borcu kaydedilmez (II). Diğer kapsamlı gelirde muhasebeleştirilen bir kaleme ilişkin vergi de DİĞER KAPSAMLI GELİRDE muhasebeleştirilir; bu nedenle III yanlıştır.",
  "TMS 12 - istisnalar ve sunum")

# ── D. Ek konular: oran değişimi, mahsup, sunum, karma (14) ────────────────
q("Vergi oranının değişmesinin mevcut ertelenmiş vergi bakiyelerine etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bakiyeler yeni oranla yeniden ölçülür; fark kural olarak kâr veya zarara yansıtılır",
  ["Mevcut bakiyeler her hâlde eski oranla korunmak zorunda olup yeniden ölçülmemektedir",
   "Oran değişikliği her hâlde önceki dönem hatası sayılıp geriye dönük düzeltilmek zorundadır",
   "Oran değişikliğinin etkisi her hâlde doğrudan özkaynaklardan indirilmek zorunda kalınır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlık ve borçları, raporlama dönemi sonu itibarıyla yasalaşmış veya yasalaşması kesine yakın oranlarla ölçülür. Oran değişirse bakiyeler yeniden ölçülür. Doğan fark, ilgili kalem başlangıçta kâr veya zararda muhasebeleştirildiyse kâr veya zarara yansıtılır.",
  "TMS 12 - oran değişiminin etkisi")

evb_eski, oran_eski, oran_yeni = 400_000, 25, 20
evb_yeni = evb_eski / oran_eski * oran_yeni
fark_oran = evb_eski - evb_yeni
q(f"Bir işletmenin %{oran_eski} oranıyla ölçülmüş {tr(evb_eski)} TL ertelenmiş vergi borcu bulunmaktadır. İlgili geçici farkın ters döneceği dönemde uygulanacak oran %{oran_yeni} olarak yasalaşmıştır. Yeniden ölçüm sonrası ertelenmiş vergi borcu kaç TL'dir?",
  f"{tr(evb_yeni)} TL",
  [f"{tr(evb_eski)} TL",                                   # yeniden ölçüm yapılmadı
   f"{tr(fark_oran)} TL",                                  # yalnızca azalış tutarı yazıldı
   f"{tr(evb_eski / oran_yeni * oran_eski)} TL",           # oran oranı ters çevrildi
   "0 TL"],                                                # borç tümüyle silindi sanıldı
  f"Geçici fark = {tr(evb_eski)} ÷ %{oran_eski} = {tr(evb_eski / oran_eski * 100)} TL. Yeni oranla ertelenmiş vergi borcu = {tr(evb_eski / oran_eski * 100)} × %{oran_yeni} = {tr(evb_yeni)} TL. Azalan {tr(fark_oran)} TL kural olarak kâr veya zarara (vergi geliri olarak) yansıtılır.",
  "TMS 12 - oran değişiminde yeniden ölçüm")

q("Cari vergi varlık ve borçlarının netleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yasal mahsup hakkı varsa ve net esasa göre ödeme niyeti bulunuyorsa netleştirilir",
  ["Her hâlde ve koşulsuz olarak netleştirilmek zorunda olan kalemleri ifade etmek durumundadır",
   "Hiçbir hâlde netleştirilemez; her zaman brüt olarak gösterilmek zorunda kalınmaktadır",
   "Netleştirme yalnızca vergi idaresi izin verdiğinde yapılabilmek zorunda bulunmaktadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 12: işletme cari vergi varlıkları ile borçlarını ancak (a) muhasebeleştirilen tutarları netleştirmek için yasal olarak uygulanabilir bir hakkı varsa ve (b) net esasa göre ödemek veya varlığı elde edip borcu ödemeyi aynı anda gerçekleştirmek niyetinde ise netleştirir.",
  "TMS 12 - cari verginin netleştirilmesi")

q("Vergi gideri ile muhasebe kârı arasındaki mutabakatın açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi gideri ile muhasebe kârı arasındaki ilişkinin sayısal mutabakatı açıklanır",
  ["Böyle bir mutabakatın açıklanmasına hiçbir hâlde gerek bulunmamak durumunda kalınmaktadır",
   "Yalnızca vergi idaresine sunulur; finansal tablo kullanıcılarına açıklanmamak zorundadır",
   "Mutabakat yalnızca zarar eden işletmeler için zorunlu tutulmuş bir husus niteliğindedir",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 12: işletme, vergi gideri (geliri) ile muhasebe kârı arasındaki ilişkiye dair açıklamayı, (a) vergi gideri ile muhasebe kârının uygulanabilir vergi oranıyla çarpımı arasındaki sayısal mutabakat veya (b) ortalama etkin vergi oranının sayısal mutabakatı biçiminde sunar.",
  "TMS 12 - mutabakat açıklaması")

q("Ertelenmiş verginin ölçümünde varlığın geri kazanılma biçimi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin defter değerini geri kazanmayı beklediği biçimin vergisel sonuçları esas alınır",
  ["Geri kazanma biçimi hiçbir hâlde dikkate alınmaz; her hâlde tek bir oran kullanılmaktadır",
   "Her hâlde varlığın satılacağı varsayılır; kullanım yoluyla geri kazanım dikkate alınmaz",
   "Her hâlde varlığın kullanılacağı varsayılır; satış yoluyla geri kazanım dikkate alınmaz",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: ertelenmiş vergi varlık ve borçlarının ölçümü, işletmenin raporlama dönemi sonu itibarıyla varlıklarının defter değerini geri kazanmayı veya borçlarının defter değerini ödemeyi beklediği biçimin vergisel sonuçlarını yansıtır. Kullanım ve satış farklı oranlara tabi olabilir.",
  "TMS 12 - geri kazanma biçimi")

q("İşletme birleşmesinde edinilen varlık ve borçlara ilişkin geçici farklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değer ile vergiye esas değer farkından ertelenmiş vergi doğar; şerefiyeyi etkiler",
  ["İşletme birleşmelerinde hiçbir hâlde ertelenmiş vergi doğmamak zorunda bulunmaktadır",
   "İşletme birleşmelerindeki farklar her hâlde sürekli fark sayılmak zorunda tutulmaktadır",
   "İşletme birleşmelerinde ertelenmiş vergi her hâlde doğrudan özkaynağa kaydedilmek zorundadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: bir işletme birleşmesinde edinilen tanımlanabilir varlıklar ve üstlenilen borçlar gerçeğe uygun değerleriyle muhasebeleştirilir; vergiye esas değerleri değişmeyebilir. Doğan geçici farklar için ertelenmiş vergi muhasebeleştirilir ve bu, şerefiye tutarını etkiler.",
  "TMS 12 - işletme birleşmesi")

q("Bir işletmenin geçmişte sürekli zarar etmiş olması ve devreden mali zararının bulunması bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmişteki zarar geçmişi, yeterli vergiye tabi kâr beklentisinin muhtemel olmadığına dair güçlü kanıttır",
  ["Geçmiş zararlar hiçbir hâlde dikkate alınmaz; ertelenmiş vergi varlığı her hâlde kaydedilir",
   "Geçmiş zararlar her hâlde ertelenmiş vergi borcu doğurmak zorunda olan kalemleri ifade eder",
   "Geçmiş zararlar hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorundadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: kullanılmamış mali zararların varlığı, gelecekte vergiye tabi kâr elde edilemeyebileceğine dair güçlü bir kanıttır. İşletmenin yakın geçmişte zarar geçmişi varsa, ertelenmiş vergi varlığı ancak yeterli vergiye tabi geçici fark bulunması veya ikna edici başka kanıt olması ölçüsünde muhasebeleştirilir.",
  "TMS 12 - zarar geçmişi (senaryo)")

q("Ertelenmiş vergi varlığı için değerlendirilecek vergiye tabi kâr kaynakları bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeterli vergiye tabi geçici farkların bulunması veya gelecekte vergiye tabi kâr elde edilmesi değerlendirilir",
  ["Yalnızca geçmiş dönemlerde elde edilmiş kârlar dikkate alınmak zorunda olan bir husustur",
   "Hiçbir kaynak değerlendirilmez; ertelenmiş vergi varlığı her hâlde kaydedilmek zorundadır",
   "Yalnızca vergi idaresinin görüşü dikkate alınmak zorunda olan bir husus niteliğindedir",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 12: indirilebilir geçici farkın kullanılabilmesi için, aynı vergi idaresi ve aynı mükellefe ilişkin yeterli VERGİYE TABİ GEÇİCİ FARK bulunması ya da gelecekte yeterli vergiye tabi kâr elde edilmesinin muhtemel olması değerlendirilir. Vergi planlama fırsatları da dikkate alınabilir.",
  "TMS 12 - vergiye tabi kâr kaynakları")

evv13, evb13 = 90_000, 140_000
net13 = evb13 - evv13
q(f"Aynı vergi idaresine ve aynı mükellefe ilişkin olup yasal mahsup hakkı bulunan bir işletmenin ertelenmiş vergi varlığı {tr(evv13)} TL, ertelenmiş vergi borcu {tr(evb13)} TL'dir. Finansal durum tablosunda gösterilecek net tutar ve niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  f"{tr(net13)} TL net ertelenmiş vergi borcu",
  [f"{tr(net13)} TL net ertelenmiş vergi varlığı olarak gösterilmek zorunda olan bir tutarı ifade eder",
   f"{tr(evv13 + evb13)} TL net ertelenmiş vergi borcu olarak gösterilir; iki tutar toplanmak zorundadır",
   f"{tr(evv13)} TL varlık ve {tr(evb13)} TL borç ayrı ayrı gösterilir; netleştirme hiçbir hâlde yapılamaz",
   "Hiçbir tutar gösterilmez; ertelenmiş vergiler yalnızca dipnotlarda açıklanmak zorunda kalınmaktadır"],
  f"TMS 12: yasal mahsup hakkı varsa ve aynı vergi idaresi/aynı mükellefe ilişkinse ertelenmiş vergi varlık ve borçları netleştirilir: {tr(evb13)} − {tr(evv13)} = {tr(net13)} TL. Borç varlıktan büyük olduğundan net ertelenmiş vergi BORCU gösterilir.",
  "TMS 12 - netleştirme hesabı")

q("Bir işletmenin şüpheli alacak karşılığı muhasebede gider yazılmış ancak vergisel olarak henüz indirilememiştir. TMS 12 bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirilebilir geçici fark doğar; koşullar sağlanıyorsa ertelenmiş vergi varlığı kaydedilir",
  ["Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu kaydedilmek zorunda tutulmaktadır",
   "Sürekli fark doğar; hiçbir hâlde ertelenmiş vergi muhasebeleştirilmemek zorunda kalınır",
   "Hiçbir fark doğmaz; karşılıklar vergisel açıdan hiç dikkate alınmamak zorunda bulunmaktadır",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "Karşılık nedeniyle alacağın defter değeri vergiye esas değerinden DÜŞÜKTÜR. Bir varlığın defter değeri vergiye esas değerinden düşükse İNDİRİLEBİLİR geçici fark doğar; gelecekte vergisel indirim sağlanacağından ertelenmiş vergi VARLIĞI kaydedilir (yeterli vergiye tabi kâr muhtemelse).",
  "TMS 12 - şüpheli alacak (senaryo)")

q("Bir varlığın defter değerinin vergiye esas değerinden DÜŞÜK olması bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirilebilir geçici fark doğar; ertelenmiş vergi varlığı muhasebeleştirilir",
  ["Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilmek zorunda kalınır",
   "Hiçbir geçici fark doğmaz; iki değer arasındaki fark dikkate alınmamak zorunda tutulmaktadır",
   "Sürekli fark doğar; hiçbir hâlde ertelenmiş vergi muhasebeleştirilmemek zorunda bulunur",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "Bir VARLIĞIN defter değeri vergiye esas değerinden düşükse, gelecekte vergisel olarak indirilebilecek tutar defter değerini aşar. Bu bir İNDİRİLEBİLİR geçici farktır ve ertelenmiş vergi VARLIĞI doğurur (yeterli vergiye tabi kâr muhtemelse).",
  "TMS 12 - varlıkta ters fark yönü")

q("Bir borcun defter değerinin vergiye esas değerinden YÜKSEK olması bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirilebilir geçici fark doğar; ertelenmiş vergi varlığı muhasebeleştirilir",
  ["Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilmek zorunda kalınır",
   "Hiçbir geçici fark doğmaz; borçlarda geçici fark söz konusu olmamak zorunda bulunmaktadır",
   "Sürekli fark doğar; hiçbir hâlde ertelenmiş vergi muhasebeleştirilmemek zorunda tutulur",
   "Bu husus TMS 12'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "BORÇLARDA yön varlıkların TERSİDİR: bir borcun defter değeri vergiye esas değerinden yüksekse, aradaki tutar gelecekte ödendiğinde vergi matrahından indirilecektir → İNDİRİLEBİLİR geçici fark → ertelenmiş vergi VARLIĞI.",
  "TMS 12 - borçta fark yönü")

q("Aşağıdakilerden hangileri TMS 12'ye göre ertelenmiş vergi BORCU doğurur?\n\nI. Varlığın defter değerinin vergiye esas değerinden yüksek olması\n\nII. Vergi amortismanının muhasebe amortismanından hızlı olması\n\nIII. Ancak ödendiğinde indirilebilen gider karşılığı ayrılması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Varlığın defter değerinin vergiye esas değerinden yüksek olması (I) ve vergi amortismanının daha hızlı olması (II — aynı sonucu doğurur) vergiye tabi geçici fark yaratır → ertelenmiş vergi BORCU. Ancak ödendiğinde indirilebilen karşılık (III) ise indirilebilir geçici fark yaratır → ertelenmiş vergi VARLIĞI; bu nedenle yanlıştır.",
  "TMS 12 - EVB doğuran hâller")

q("Aşağıdaki ifadelerden hangileri TMS 12 bakımından doğrudur?\n\nI. Vergi oranı değişirse mevcut ertelenmiş vergi bakiyeleri yeniden ölçülür\n\nII. Ertelenmiş vergi, varlığın geri kazanılma biçiminin vergisel sonuçlarını yansıtır\n\nIII. Vergi oranı değişikliği önceki dönem hatası sayılıp geriye dönük düzeltilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Oran değişirse bakiyeler yeniden ölçülür (I) ve ertelenmiş vergi, geri kazanma biçiminin vergisel sonuçlarını yansıtır (II). Oran değişikliği önceki dönem hatası DEĞİLDİR ve geriye dönük düzeltilmez; etkisi cari dönemde muhasebeleştirilir. Bu nedenle III yanlıştır.",
  "TMS 12 - oran ve ölçüm")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 12; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
