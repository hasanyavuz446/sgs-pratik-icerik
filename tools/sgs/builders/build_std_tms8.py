# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 8 Muhasebe Politikaları, Tahminlerdeki
Değişiklikler ve Hatalar — 60 soru. Kaynak: KGK TMS 8.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_8_politikalar"
PREFIX, SEED = "std-tms8-gen", 20261104
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_8_politikalar.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Muhasebe politikaları (14) ──────────────────────────────────────────
q("TMS 8'e göre muhasebe politikaları bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tabloların hazırlanmasında ve sunulmasında uygulanan belirli ilkeler, esaslar, gelenekler, kurallar ve uygulamalardır",
  ["İşletmenin vergi matrahını hesaplarken uyduğu vergi mevzuatı hükümlerini ifade eden kurallardır",
   "İşletme yönetiminin gelecek dönemlere ilişkin belirlediği satış ve kâr hedeflerini ifade etmektedir",
   "İşletmenin çalışanlarına uyguladığı ücret ve prim esaslarını düzenleyen iç yönergeleri ifade eder",
   "Bağımsız denetçinin denetim sırasında uyguladığı denetim tekniklerini gösteren esasları kapsar"],
  "TMS 8: muhasebe politikaları, finansal tabloların hazırlanmasında ve sunulmasında işletme tarafından uygulanan belirli ilkeler, esaslar, gelenekler, kurallar ve uygulamalardır.",
  "TMS 8 - muhasebe politikası tanımı")

q("Bir işlem için uygulanacak muhasebe politikasının belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlemle ilgili bir TFRS varsa politika o TFRS uygulanarak belirlenir",
  ["İşletme yönetimi ilgili TFRS bulunsa dahi dilediği politikayı serbestçe seçip uygulayabilmektedir",
   "Politika her hâlde vergi mevzuatına göre belirlenir; TFRS hükümleri dikkate alınmamaktadır",
   "Politika belirlenmesi TMS 8'de düzenlenmemiş olup tümüyle işletmenin takdirine bırakılmıştır",
   "Politika her hâlde bağımsız denetçi tarafından belirlenir; işletmenin bu konuda yetkisi yoktur"],
  "TMS 8: bir işleme, olaya veya duruma özel olarak uygulanan bir TFRS bulunması durumunda, ilgili kaleme uygulanacak muhasebe politikası veya politikaları söz konusu TFRS uygulanarak belirlenir.",
  "TMS 8 - politika seçimi")

q("İşleme özel bir TFRS bulunmaması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Yönetim, ilgili ve güvenilir bilgi sağlayan bir politika geliştirmek için kendi muhakemesini kullanır",
  ["İşletme bu durumda finansal tablo düzenlemekten tümüyle muaf tutulmuş bulunmaktadır",
   "İşletme bu durumda ilgili kalemi finansal tablolara hiç yansıtmadan dipnotta açıklamaktadır",
   "İşletme bu durumda her hâlde vergi mevzuatındaki hükmü aynen uygulamak zorunda tutulmuştur",
   "İşletme bu durumda politika geliştiremez; ilgili işlemi hiçbir biçimde kaydedememektedir"],
  "TMS 8: bir işleme özel olarak uygulanabilecek bir TFRS yoksa yönetim, ilgili ve güvenilir bilgi sağlayan bir muhasebe politikası geliştirmek ve uygulamakta muhakemesini kullanır.",
  "TMS 8 - muhakeme kullanımı")

q("Politika geliştirirken yönetimin başvuracağı kaynakların sırası bakımından aşağıdakilerden hangisi doğrudur?",
  "Önce benzer konulardaki TFRS hükümlerine, sonra Kavramsal Çerçevedeki tanım ve ölçütlere başvurulur",
  ["Önce sektör uygulamalarına, sonra vergi mevzuatına başvurulur; TFRS hükümleri hiç dikkate alınmaz",
   "Önce Kavramsal Çerçeveye, sonra vergi mevzuatına başvurulur; benzer TFRS hükümleri göz ardı edilir",
   "Kaynaklar arasında hiçbir sıra bulunmayıp yönetim dilediği kaynağı serbestçe seçebilmektedir",
   "Yalnızca uluslararası muhasebe literatürüne başvurulur; TFRS hükümleri kaynak sayılmamaktadır"],
  "TMS 8: yönetim muhakemesini kullanırken sırasıyla, benzer ve ilgili konuları ele alan TFRS hükümlerini ve Kavramsal Çerçevedeki varlık, yabancı kaynak, gelir ve gider tanım, muhasebeleştirme kriterleri ile ölçüm kavramlarını dikkate alır.",
  "TMS 8 - kaynak hiyerarşisi")

q("Politika geliştirirken başvurulabilecek diğer kaynaklar bakımından aşağıdakilerden hangisi doğrudur?",
  "TFRS ile çelişmemek koşuluyla benzer çerçeve kullanan standart belirleyicilerin kararlarına ve sektör uygulamalarına başvurulabilir",
  ["Başka hiçbir kaynağa başvurulamaz; yalnızca TFRS metinleri kaynak olarak kullanılabilmektedir",
   "TFRS ile çelişse dahi her türlü sektör uygulaması doğrudan kaynak olarak benimsenebilmektedir",
   "Yalnızca vergi mevzuatı kaynak olarak kullanılabilir; diğer kaynaklara başvurulması yasaktır",
   "Yalnızca bağımsız denetçinin görüşü kaynak sayılır; literatür ve sektör uygulaması dikkate alınmaz"],
  "TMS 8: yönetim, TFRS ile çelişmemesi kaydıyla, benzer kavramsal çerçeve kullanan diğer standart belirleyici kuruluşların en son kararlarını, diğer muhasebe literatürünü ve sektör uygulamalarını da dikkate alabilir.",
  "TMS 8 - diğer kaynaklar")

q("Muhasebe politikalarının tutarlılığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Benzer işlem ve olaylar için politikalar tutarlı biçimde seçilir ve uygulanır",
  ["Her dönem farklı politika uygulanmak zorunda olup tutarlılık aranmayan bir husustur",
   "Benzer işlemler için her biri farklı politikayla muhasebeleştirilmek zorunda tutulmuştur",
   "Tutarlılık yalnızca vergi idaresi talep ettiğinde ve onun belirlediği ölçüde aranmaktadır",
   "Tutarlılık kavramı TMS 8'de düzenlenmemiş olup uygulamada dikkate alınmamaktadır"],
  "TMS 8: bir TFRS özellikle bir sınıflandırma gerektirmedikçe veya buna izin vermedikçe, işletme benzer işlem, diğer olay ve koşullar için muhasebe politikalarını tutarlı biçimde seçer ve uygular.",
  "TMS 8 - tutarlılık")

q("Bir TFRS'nin kalemlerin sınıflandırılmasına izin vermesi hâlinde aşağıdakilerden hangisi doğrudur?",
  "Her sınıf için uygun bir politika seçilir ve tutarlı biçimde uygulanır",
  ["Tüm sınıflar için tek bir politika seçilmek zorunda olup sınıf ayrımı yapılamamaktadır",
   "Her sınıf için her dönem farklı politika uygulanmak zorunda olup tutarlılık aranmamaktadır",
   "Sınıflandırmaya izin verilse dahi işletme hiçbir hâlde farklı politika uygulayamamaktadır",
   "Sınıflandırma hâlinde politika seçimi bağımsız denetçi tarafından yapılmak zorundadır"],
  "TMS 8: bir TFRS kalemlerin farklı politikaların uygulanmasının uygun olabileceği sınıflara ayrılmasını gerektiriyor veya buna izin veriyorsa, her sınıf için uygun bir politika seçilir ve tutarlı olarak uygulanır.",
  "TMS 8 - sınıf bazında politika")

q("Muhasebe politikalarının önemlilik ile ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "TFRS'lerdeki politikaların, etkisi önemsizse uygulanması gerekmez; ancak önemsiz sapmalar kasıtlı yapılamaz",
  ["TFRS'lerdeki tüm politikalar etkisi ne olursa olsun her hâlde uygulanmak zorunda tutulmuştur",
   "Önemlilik kavramı muhasebe politikalarıyla hiçbir biçimde ilişkilendirilemeyen bir kavramdır",
   "Önemsiz sapmalar kasıtlı olarak yapılabilir; TMS 8 bu konuda hiçbir sınırlama getirmemektedir",
   "Politikaların uygulanması yalnızca büyük işletmeler için zorunlu olup küçükler muaf tutulur"],
  "TMS 8: TFRS'lerde belirtilen muhasebe politikalarının etkilerinin önemsiz olması durumunda bunların uygulanmasına gerek yoktur. Ancak belirli bir sunumu sağlamak amacıyla önemsiz sapmalar yapılması veya bunların düzeltilmemesi uygun değildir.",
  "TMS 8 - önemlilik")

q("Muhasebe politikalarının açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, finansal tabloları anlamak için gerekli olan önemli muhasebe politikalarını dipnotlarda açıklar",
  ["Muhasebe politikaları hiçbir biçimde açıklanmaz; yalnızca işletme içinde saklı tutulmaktadır",
   "Muhasebe politikaları yalnızca vergi beyannamesinde belirtilir; dipnotlarda hiç yer almamaktadır",
   "Muhasebe politikaları yalnızca bağımsız denetçiye bildirilir; kullanıcılara açıklanmamaktadır",
   "Muhasebe politikalarının açıklanması yalnızca zarar eden işletmeler için zorunlu tutulmuştur"],
  "Muhasebe politikaları, finansal tabloların anlaşılması bakımından kullanıcılara yardımcı olacak biçimde dipnotlarda açıklanır. Bu, politika seçimi ve değişikliklerinin şeffaflığını sağlar.",
  "TMS 8 - politika açıklaması")

q("Bir işletme, stok maliyetlerini bugüne kadar ağırlıklı ortalama maliyet yöntemiyle ölçmüştür. TMS 8 bakımından aşağıdakilerden hangisi doğrudur?",
  "Seçilen bu ölçüm yöntemi bir muhasebe politikasıdır",
  ["Seçilen bu ölçüm yöntemi bir muhasebe tahmini olup ileriye dönük olarak değiştirilebilmektedir",
   "Seçilen bu ölçüm yöntemi önceki dönem hatası niteliğinde olup düzeltilmesi gerekmektedir",
   "Stok ölçüm yöntemi TMS 8 kapsamında hiçbir biçimde değerlendirilemeyen bir husus niteliğindedir",
   "Stok ölçüm yöntemi yalnızca vergi mevzuatına göre belirlenir; muhasebe politikası sayılmamaktadır"],
  "Stok maliyetinin belirlenmesinde kullanılan yöntem (FIFO veya ağırlıklı ortalama), finansal tabloların hazırlanmasında uygulanan bir ilke olduğundan muhasebe politikasıdır; tahmin değildir.",
  "TMS 8 - politika örneği (senaryo)")

q("Bir işletme, maddi duran varlıklarını maliyet modeli yerine yeniden değerleme modeliyle ölçmeye başlamıştır. TMS 8 bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu bir politika değişikliğidir; ancak ilk kez uygulanması TMS 16 uyarınca ele alınır",
  ["Bu bir muhasebe tahmini değişikliği olup ileriye dönük olarak uygulanmak zorunda tutulmuştur",
   "Bu bir önceki dönem hatası olup geriye dönük yeniden düzenleme yapılmasını gerektirmektedir",
   "Bu değişiklik hiçbir standart kapsamında değerlendirilmez; kayda alınmasına gerek yoktur",
   "Bu değişiklik yalnızca vergi mevzuatı açısından sonuç doğurur; finansal tabloları etkilemez"],
  "TMS 8: yeniden değerleme modelinin ilk kez uygulanması bir muhasebe politikası değişikliğidir; ancak TMS 8'in politika değişikliği hükümlerine göre değil, TMS 16 (veya TMS 38) uyarınca yeniden değerleme olarak ele alınır.",
  "TMS 8 - yeniden değerlemenin ilk uygulanması")

q("Aşağıdakilerden hangileri TMS 8'e göre muhasebe politikası sayılır?\n\nI. Stok maliyetinin ölçümünde kullanılan yöntem\n\nII. Maddi duran varlığın yararlı ömrünün belirlenmesi\n\nIII. Şüpheli alacak karşılığı oranının belirlenmesi",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Stok maliyetinin ölçümünde kullanılan yöntem (I) muhasebe politikasıdır. Maddi duran varlığın yararlı ömrü (II) ile şüpheli alacak karşılığı oranı (III) ölçüm belirsizliğine dayanan muhasebe tahminleridir. Yalnız I doğrudur.",
  "TMS 8 - politika-tahmin ayrımı")

q("Aşağıdaki ifadelerden hangileri muhasebe politikaları bakımından doğrudur?\n\nI. İşleme özel bir TFRS varsa politika o TFRS uygulanarak belirlenir\n\nII. Benzer işlemler için politikalar tutarlı uygulanır\n\nIII. TFRS yoksa yönetim muhakemesini kullanarak politika geliştirir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 8'e göre üçü de doğrudur: işleme özel TFRS varsa o uygulanır (I), benzer işlemlerde tutarlılık esastır (II) ve TFRS yoksa yönetim ilgili ve güvenilir bilgi sağlayan bir politika geliştirmek için muhakemesini kullanır (III).",
  "TMS 8 - politikalar")

q("Muhasebe politikalarının amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablo bilgisinin ihtiyaca uygun ve güvenilir olmasını sağlayarak karşılaştırılabilirliği artırmaktır",
  ["Yalnızca işletmenin ödeyeceği vergiyi en aza indirecek bir sonuç elde etmeyi amaçlamaktadır",
   "Yalnızca işletmenin dönem kârını mümkün olduğunca yüksek göstermeyi amaçlayan bir araçtır",
   "Yalnızca bağımsız denetçinin işini kolaylaştırmayı amaçlayan biçimsel bir düzenlemedir",
   "Muhasebe politikalarının belirlenmiş bir amacı bulunmayıp yalnızca geleneksel bir uygulamadır"],
  "Muhasebe politikalarının tutarlı seçimi ve uygulanması, bilginin ihtiyaca uygunluğunu ve güvenilirliğini sağlar; dönemler ve işletmeler arası karşılaştırılabilirliği artırır.",
  "TMS 8 - amaç")

# ── B. Politika değişikliği (14) ───────────────────────────────────────────
q("Muhasebe politikasında değişiklik yapılabilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişiklik ancak bir TFRS tarafından gerekli kılınıyorsa veya daha güvenilir ve uygun bilgi sağlıyorsa yapılır",
  ["İşletme muhasebe politikasını dilediği zaman gerekçe göstermeksizin serbestçe değiştirebilmektedir",
   "Muhasebe politikası hiçbir hâlde ve hiçbir gerekçeyle değiştirilemeyen bir unsur niteliğindedir",
   "Muhasebe politikası yalnızca vergi idaresi izin verdiğinde ve onun belirlediği ölçüde değiştirilir",
   "Muhasebe politikası yalnızca işletme zarar ettiğinde değiştirilebilen bir unsuru ifade etmektedir"],
  "TMS 8: işletme muhasebe politikasını ancak (a) bir TFRS tarafından gerekli kılınıyorsa veya (b) işlemlerin finansal tablolar üzerindeki etkileri hakkında daha güvenilir ve daha uygun bilgi sağlıyorsa değiştirir.",
  "TMS 8 - değişiklik koşulları")

q("Muhasebe politikası değişikliğinin uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak geriye dönük uygulanır",
  ["Kural olarak ileriye dönük uygulanır; geçmiş dönemler hiçbir hâlde düzeltilmemektedir",
   "Yalnızca cari dönem kâr veya zararına yansıtılır; karşılaştırmalı bilgiler değiştirilmez",
   "Politika değişikliği hiçbir biçimde finansal tablolara yansıtılmaz; yalnızca dipnotta belirtilir",
   "Politika değişikliği yalnızca gelecek dönemlerde uygulanır; cari dönem de etkilenmemektedir"],
  "TMS 8: bir muhasebe politikası değişikliği, geçiş hükümleri bulunmadıkça geriye dönük olarak uygulanır. Böylece karşılaştırılabilirlik korunur.",
  "TMS 8 - geriye dönük uygulama")

q("Geriye dönük uygulama bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeni politika, sanki hep uygulanıyormuş gibi geçmiş işlemlere de uygulanır",
  ["Yeni politika yalnızca değişiklik tarihinden sonraki işlemlere uygulanan bir yöntemi ifade eder",
   "Yeni politika yalnızca gelecek dönemlerde uygulanır; cari dönem işlemleri etkilenmemektedir",
   "Geriye dönük uygulama yalnızca karşılaştırmalı bilgilerin dipnotta açıklanmasını ifade etmektedir",
   "Geriye dönük uygulama kavramı TMS 8'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 8: geriye dönük uygulama, yeni muhasebe politikasının işlem, olay ve koşullara sanki bu politika hep kullanımdaymış gibi uygulanmasıdır.",
  "TMS 8 - geriye dönük uygulama tanımı")

q("Politika değişikliğinde en erken dönem bakımından aşağıdakilerden hangisi doğrudur?",
  "Sunulan en erken dönemin açılış özkaynak kalemleri düzeltilir ve karşılaştırmalı tutarlar yeniden düzenlenir",
  ["Yalnızca cari dönem tutarları düzeltilir; açılış özkaynağına hiçbir biçimde dokunulmamaktadır",
   "Yalnızca gelecek dönem tutarları düzeltilir; geçmiş ve cari dönem etkilenmeden bırakılmaktadır",
   "Hiçbir düzeltme yapılmaz; değişiklik yalnızca dipnotlarda açıklanmakla yetinilen bir husustur",
   "Yalnızca vergi beyannamesindeki tutarlar düzeltilir; finansal tablolar değiştirilmemektedir"],
  "TMS 8: politika değişikliği geriye dönük uygulanırken, sunulan en erken dönemin etkilenen her bir özkaynak kaleminin açılış tutarı ile diğer karşılaştırmalı tutarlar, yeni politika hep uygulanıyormuş gibi düzeltilir.",
  "TMS 8 - açılış özkaynak düzeltmesi")

q("Geçiş hükmü bulunan bir TFRS'nin ilk kez uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "İlgili TFRS'deki özel geçiş hükümlerine uyulur",
  ["Geçiş hükmü bulunsa dahi her hâlde TMS 8'in genel geriye dönük kuralı uygulanmak zorundadır",
   "Geçiş hükmü bulunsa dahi her hâlde ileriye dönük uygulama yapılmak zorunda tutulmuştur",
   "Geçiş hükümleri bağlayıcı olmayıp işletme dilediği yöntemi serbestçe seçebilmektedir",
   "Geçiş hükümleri yalnızca büyük işletmeler için bağlayıcı olup küçükler bunlardan muaftır"],
  "TMS 8: bir TFRS'nin ilk kez uygulanmasından kaynaklanan politika değişikliği, varsa söz konusu TFRS'nin özel geçiş hükümlerine göre muhasebeleştirilir.",
  "TMS 8 - geçiş hükümleri")

q("Geçiş hükmü bulunmayan bir TFRS'nin ilk kez uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişiklik geriye dönük olarak uygulanır",
  ["Değişiklik ileriye dönük uygulanır; geçmiş dönemler hiçbir hâlde düzeltilmemektedir",
   "Değişiklik hiçbir biçimde uygulanmaz; ilgili TFRS işletme için bağlayıcı olmaktan çıkmaktadır",
   "Değişiklik yalnızca dipnotlarda açıklanır; finansal tablo tutarlarına hiç yansıtılmamaktadır",
   "Değişikliğin uygulanma biçimi işletmenin serbest takdirine bırakılmış bir husus niteliğindedir"],
  "TMS 8: bir TFRS'nin ilk kez uygulanmasından kaynaklanan politika değişikliğinde özel geçiş hükmü yoksa değişiklik geriye dönük olarak uygulanır.",
  "TMS 8 - geçiş hükmü yokluğu")

q("Aşağıdakilerden hangisi TMS 8'e göre muhasebe politikası değişikliği DEĞİLDİR?",
  "Özü itibarıyla daha önceki işlemlerden farklı olan yeni bir işlem için yeni politika uygulanması",
  ["Stok maliyetinin ölçümünde kullanılan yöntemin ağırlıklı ortalamadan FIFO'ya çevrilmesi işlemi",
   "Bir TFRS'nin gerekli kılması nedeniyle uygulanan ölçüm esasının değiştirilmesi niteliğindeki işlem",
   "Daha güvenilir ve uygun bilgi sağlaması nedeniyle sunum esasının değiştirilmesi niteliğinde işlem",
   "Maddi duran varlıklarda maliyet modelinden yeniden değerleme modeline geçilmesi niteliğinde işlem"],
  "TMS 8: özü itibarıyla önceki işlem ve olaylardan farklı olan işlemler için yeni bir politika uygulanması ile daha önce gerçekleşmemiş veya önemsiz olan işlemler için yeni politika uygulanması, muhasebe politikası değişikliği DEĞİLDİR.",
  "TMS 8 - değişiklik sayılmayan hâller")

q("Daha önce hiç gerçekleşmemiş bir işlem türü için ilk kez politika belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu bir muhasebe politikası değişikliği sayılmaz",
  ["Bu bir muhasebe politikası değişikliği olup geriye dönük uygulanmak zorunda tutulmaktadır",
   "Bu bir önceki dönem hatası olup geriye dönük yeniden düzenleme yapılmasını gerektirmektedir",
   "Bu bir muhasebe tahmini değişikliği olup ileriye dönük uygulanmak zorunda bulunmaktadır",
   "Bu durumda işletme söz konusu işlemi hiçbir biçimde muhasebeleştirememektedir"],
  "TMS 8: daha önce gerçekleşmemiş veya önemsiz olan işlem, olay ve koşullar için yeni bir muhasebe politikası uygulanması, muhasebe politikası değişikliği değildir.",
  "TMS 8 - değişiklik sayılmayan hâller")

q("Politika değişikliğinin geriye dönük uygulanmasının uygulanabilir olmaması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Uygulamanın mümkün olduğu en erken dönemin başından itibaren ileriye dönük uygulanır",
  ["Değişiklik hiçbir biçimde uygulanmaz; işletme eski politikayı sürdürmek zorunda tutulmaktadır",
   "Değişiklik her hâlde geriye dönük uygulanmak zorunda olup hiçbir istisna kabul edilmemektedir",
   "Değişiklik yalnızca dipnotlarda açıklanır; finansal tablo tutarlarına hiç yansıtılmamaktadır",
   "Bu durumda işletme finansal tablo düzenlemekten tümüyle muaf tutulmuş bulunmaktadır"],
  "TMS 8: geriye dönük uygulamanın belirli bir döneme ilişkin etkilerinin belirlenmesi uygulanabilir değilse, yeni politika uygulamanın mümkün olduğu en erken dönemin başından itibaren uygulanır.",
  "TMS 8 - uygulanabilir olmama")

q("TMS 8'e göre 'uygulanabilir olmama' bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin her türlü makul çabayı göstermesine rağmen bir hükmü uygulayamaması hâlini ifade eder",
  ["İşletmenin uygulamayı maliyetli bulup tercih etmemesi hâlini ifade eden bir kavram niteliğindedir",
   "İşletmenin uygulamayı unutması veya ihmal etmesi hâlini ifade eden bir kavramı karşılamaktadır",
   "İşletmenin vergi avantajı sağlamak amacıyla uygulamadan kaçınması hâlini ifade eden kavramdır",
   "Uygulanabilir olmama kavramı TMS 8'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 8: bir hükmün uygulanması, işletmenin her türlü makul çabayı göstermesine rağmen söz konusu hükmü uygulayamaması durumunda uygulanabilir değildir. Sadece maliyetli veya zahmetli olması yeterli değildir.",
  "TMS 8 - uygulanabilir olmama tanımı")

q("Yayımlanmış ancak henüz yürürlüğe girmemiş bir TFRS bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulanmamışsa bu durum ile muhtemel etkilerine ilişkin bilinen veya makul ölçüde tahmin edilebilir bilgiler açıklanır",
  ["Yürürlüğe girmemiş bir TFRS hakkında hiçbir açıklama yapılmasına gerek bulunmamaktadır",
   "Yürürlüğe girmemiş bir TFRS her hâlde ve derhâl uygulanmak zorunda tutulan bir düzenlemedir",
   "Yürürlüğe girmemiş bir TFRS hiçbir hâlde erken uygulanamaz; bu kesin olarak yasaklanmıştır",
   "Yürürlüğe girmemiş TFRS'ler yalnızca vergi idaresine bildirilir; dipnotlarda yer almamaktadır"],
  "TMS 8: işletme, yayımlanmış ancak henüz yürürlüğe girmemiş bir TFRS'yi uygulamamışsa bu durumu ve söz konusu TFRS'nin uygulanmasının muhtemel etkilerinin değerlendirilmesine ilişkin bilinen veya makul ölçüde tahmin edilebilir bilgileri açıklar.",
  "TMS 8 - yürürlüğe girmemiş TFRS")

q("Politika değişikliğinde yapılacak açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişikliğin niteliği, nedeni ve etkilenen kalemlerdeki düzeltme tutarları açıklanır",
  ["Politika değişikliği hakkında hiçbir açıklama yapılmaz; yalnızca tutarlar sessizce düzeltilir",
   "Yalnızca değişikliğin yapıldığı belirtilir; nedeni ve tutarsal etkisi hiçbir hâlde açıklanmaz",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca değişiklik işletmenin kârını artırdığında zorunlu olup azalttığında aranmaz"],
  "TMS 8: politika değişikliğinde değişikliğin niteliği, yeni politikaya geçiş nedeni, cari ve önceki dönemlerde etkilenen kalemlere ilişkin düzeltme tutarları ile mümkünse önceki dönemlere ilişkin düzeltme tutarı açıklanır.",
  "TMS 8 - politika değişikliği açıklamaları")

q("Aşağıdakilerden hangileri TMS 8'e göre muhasebe politikası değişikliğinin koşullarındandır?\n\nI. Bir TFRS tarafından gerekli kılınması\n\nII. Daha güvenilir ve uygun bilgi sağlaması\n\nIII. İşletmenin vergi yükünü azaltması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 8 politika değişikliğini iki hâlle sınırlar: bir TFRS'nin gerekli kılması (I) veya daha güvenilir ve uygun bilgi sağlanması (II). Vergi yükünün azaltılması (III) TMS 8'de bir değişiklik gerekçesi değildir.",
  "TMS 8 - değişiklik koşulları")

q("Aşağıdaki ifadelerden hangileri politika değişikliği bakımından doğrudur?\n\nI. Kural olarak geriye dönük uygulanır\n\nII. Geçiş hükmü varsa ona uyulur\n\nIII. Özü farklı yeni bir işlem için politika belirlenmesi de politika değişikliğidir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Politika değişikliği kural olarak geriye dönük uygulanır (I) ve geçiş hükmü varsa ona uyulur (II). Özü itibarıyla farklı yeni bir işlem için politika belirlenmesi (III) ise TMS 8'e göre politika değişikliği SAYILMAZ.",
  "TMS 8 - politika değişikliği")

# ── C. Muhasebe tahminleri (16) ────────────────────────────────────────────
q("TMS 8'e göre muhasebe tahminleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Ölçüm belirsizliğine tabi olan, finansal tablolardaki parasal tutarlardır",
  ["Finansal tabloların hazırlanmasında uygulanan ilke, esas, gelenek ve kuralları ifade etmektedir",
   "İşletme yönetiminin gelecek dönemlere ilişkin belirlediği bütçe ve hedefleri ifade eden tutarlardır",
   "Önceki dönem finansal tablolarında yapılmış olan ihmal ve yanlış beyanları ifade eden kavramdır",
   "Muhasebe tahmini kavramı TMS 8'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 8: muhasebe tahminleri, ölçüm belirsizliğine tabi olan, finansal tablolardaki parasal tutarlardır. Politikalar ise uygulanan ilke ve esaslardır.",
  "TMS 8 - muhasebe tahmini tanımı")

q("Muhasebe tahminindeki değişikliğin uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "İleriye dönük olarak uygulanır",
  ["Geriye dönük olarak uygulanır; geçmiş dönem karşılaştırmalı tutarları yeniden düzenlenmektedir",
   "En erken dönemin açılış özkaynağı düzeltilerek geriye dönük biçimde uygulanmak zorundadır",
   "Hiçbir biçimde finansal tablolara yansıtılmaz; yalnızca dipnotlarda açıklanan bir husustur",
   "Yalnızca gelecek dönemlerde uygulanır; değişikliğin yapıldığı cari dönem hiç etkilenmemektedir"],
  "TMS 8: muhasebe tahminindeki değişikliğin etkisi ileriye dönük olarak, değişikliğin yapıldığı cari dönemde ve etkiliyorsa gelecek dönemlerde kâr veya zarara dâhil edilerek muhasebeleştirilir.",
  "TMS 8 - ileriye dönük uygulama")

q("Muhasebe tahminindeki değişikliğin niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeni bilgi veya gelişmelerden kaynaklanır; hata düzeltmesi niteliğinde değildir",
  ["Her hâlde önceki dönem hatası niteliğinde olup geriye dönük düzeltilmesi gerekmektedir",
   "Her hâlde bir muhasebe politikası değişikliği niteliğinde olup geriye dönük uygulanmaktadır",
   "İşletmenin kasıtlı olarak yaptığı bir yanlış beyan niteliğinde sayılan bir işlemi ifade eder",
   "Muhasebe tahmini değişikliği hiçbir hâlde finansal tablolara yansıtılamayan bir husustur"],
  "TMS 8: muhasebe tahminindeki değişiklikler yeni bilgi veya gelişmelerden kaynaklanır ve bu nedenle hataların düzeltilmesi anlamına gelmez.",
  "TMS 8 - tahmin değişikliğinin niteliği")

q("Bir değişikliğin politika mı yoksa tahmin değişikliği mi olduğunun ayırt edilemediği hâllerde aşağıdakilerden hangisi doğrudur?",
  "Değişiklik, muhasebe tahminindeki değişiklik olarak kabul edilir",
  ["Değişiklik her hâlde muhasebe politikası değişikliği olarak kabul edilmek zorunda tutulmuştur",
   "Değişiklik her hâlde önceki dönem hatası olarak kabul edilip geriye dönük düzeltilmektedir",
   "Değişiklik hiçbir biçimde finansal tablolara yansıtılmaz; kayda alınmasına gerek bulunmaz",
   "Bu durumda işletme değişikliği uygulamaktan tümüyle vazgeçmek zorunda bırakılmaktadır"],
  "TMS 8: bir muhasebe politikası değişikliği ile bir muhasebe tahmini değişikliğinin birbirinden ayırt edilmesinin zor olduğu durumlarda, söz konusu değişiklik muhasebe tahminindeki değişiklik olarak dikkate alınır.",
  "TMS 8 - ayırt edilemeyen değişiklik")

q("Maddi duran varlığın faydalı ömrünün yeniden gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu bir muhasebe tahmini değişikliğidir; ileriye dönük uygulanır",
  ["Bu bir muhasebe politikası değişikliği olup geriye dönük uygulanmak zorunda tutulmaktadır",
   "Bu bir önceki dönem hatası olup geriye dönük yeniden düzenleme yapılmasını gerektirmektedir",
   "Faydalı ömür hiçbir hâlde değiştirilemez; ilk belirlenen ömür üzerinden devam edilmektedir",
   "Faydalı ömür değişikliği hiçbir biçimde finansal tablolara yansıtılmayan bir husus niteliğindedir"],
  "Faydalı ömür ölçüm belirsizliğine tabi bir tahmindir; gözden geçirme sonucu değişmesi muhasebe tahmini değişikliğidir ve ileriye dönük uygulanır. Geçmiş amortismanlar düzeltilmez.",
  "TMS 8 - faydalı ömür")

q("Amortisman yönteminin değiştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu bir muhasebe tahmini değişikliği olarak ele alınır ve ileriye dönük uygulanır",
  ["Bu bir muhasebe politikası değişikliği olup her hâlde geriye dönük uygulanmak zorundadır",
   "Bu bir önceki dönem hatası niteliğinde olup yeniden düzenleme yapılmasını gerektirmektedir",
   "Amortisman yöntemi hiçbir hâlde değiştirilemez; ilk seçilen yöntem zorunlu olarak sürdürülür",
   "Amortisman yöntemi değişikliği yalnızca vergi idaresinin izniyle yapılabilen bir işlemdir"],
  "Amortisman yöntemi, varlığın gelecekteki ekonomik faydalarının tüketim biçimine ilişkin bir tahmini yansıtır; değiştirilmesi TMS 16 uyarınca muhasebe tahmini değişikliği olarak ele alınır ve ileriye dönük uygulanır.",
  "TMS 8 - amortisman yöntemi")

q("Şüpheli alacak karşılığı tutarının gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu bir muhasebe tahmini değişikliğidir; cari dönem kâr veya zararına yansıtılır",
  ["Bu bir muhasebe politikası değişikliği olup geriye dönük uygulanmak zorunda tutulmaktadır",
   "Bu bir önceki dönem hatası olup geçmiş dönem tabloları yeniden düzenlenmek zorundadır",
   "Şüpheli alacak karşılığı bir kez belirlendikten sonra hiçbir hâlde değiştirilememektedir",
   "Şüpheli alacak karşılığı değişikliği hiçbir biçimde kâr veya zarara yansıtılmayan bir husustur"],
  "Şüpheli alacak karşılığı ölçüm belirsizliğine tabi bir tahmindir; yeni bilgiyle gözden geçirilmesi tahmin değişikliğidir ve ileriye dönük olarak cari dönem kâr/zararına yansıtılır.",
  "TMS 8 - şüpheli alacak tahmini")

q("Muhasebe tahmini geliştirilirken kullanılan girdiler bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, ölçüm tekniklerini ve girdileri seçerek makul tahminler geliştirmek için muhakemesini kullanır",
  ["Tahminler her hâlde vergi mevzuatındaki oranlar kullanılarak belirlenmek zorunda tutulmuştur",
   "Tahminler yalnızca bağımsız denetçi tarafından belirlenir; işletmenin bu konuda yetkisi yoktur",
   "Tahminler için hiçbir girdi kullanılmaz; tutarlar rastgele biçimde belirlenebilmektedir",
   "Tahmin geliştirilmesi TMS 8'de düzenlenmemiş olup uygulamada hiç yapılmayan bir işlemdir"],
  "TMS 8: muhasebe tahmini geliştirilirken işletme ölçüm tekniklerini ve girdileri kullanır. Bu seçimler, güvenilir bilgiye dayalı makul tahminler geliştirmek için yönetimin muhakemesini gerektirir.",
  "TMS 8 - tahmin girdileri")

q("Muhasebe tahminindeki değişikliğin gelecek dönemleri de etkilemesi hâlinde aşağıdakilerden hangisi doğrudur?",
  "Değişikliğin etkisi hem cari dönemde hem de etkilediği gelecek dönemlerde muhasebeleştirilir",
  ["Değişikliğin etkisi yalnızca cari dönemde muhasebeleştirilir; gelecek dönemler hiç etkilenmez",
   "Değişikliğin etkisi yalnızca gelecek dönemlerde muhasebeleştirilir; cari dönem etkilenmemektedir",
   "Değişikliğin etkisi geçmiş dönemlere dağıtılarak geriye dönük biçimde muhasebeleştirilmektedir",
   "Değişikliğin etkisi hiçbir döneme yansıtılmaz; yalnızca dipnotlarda açıklanmakla yetinilir"],
  "TMS 8: tahmin değişikliğinin etkisi, değişikliğin yalnızca cari dönemi etkilemesi hâlinde cari dönemde; cari dönem ve gelecek dönemleri etkilemesi hâlinde ise her iki dönemde de kâr veya zarara dâhil edilerek muhasebeleştirilir.",
  "TMS 8 - tahmin etkisinin dağılımı")

q("Muhasebe tahmini değişikliğinin açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişikliğin niteliği ile cari dönemdeki ve varsa gelecek dönemlerdeki etkisinin tutarı açıklanır",
  ["Tahmin değişikliği hakkında hiçbir açıklama yapılmaz; tutarlar sessizce güncellenmektedir",
   "Yalnızca değişikliğin yapıldığı belirtilir; niteliği ve tutarsal etkisi hiçbir hâlde açıklanmaz",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmamaktadır",
   "Açıklama yalnızca değişiklik işletmenin kârını azalttığında zorunlu olup artırdığında aranmaz"],
  "TMS 8: işletme, muhasebe tahminindeki değişikliğin niteliğini ve cari dönemde etkisi olan ya da gelecek dönemlerde etkisi olması beklenen tutarı açıklar.",
  "TMS 8 - tahmin değişikliği açıklaması")

mal, omur, gecen, yeni_kalan = 500_000, 10, 4, 4
yillik_eski = mal / omur
birikmis = yillik_eski * gecen
ndd = mal - birikmis
yeni_yillik = ndd / yeni_kalan
q(f"Maliyeti {tr(mal)} TL olan bir makine, kalıntı değeri sıfır kabul edilerek {omur} yıl faydalı ömürle doğrusal amortismana tabi tutulmuştur. {gecen}. yılın sonunda kalan faydalı ömür {yeni_kalan} yıl olarak yeniden tahmin edilmiştir. Buna göre izleyen yılın amortisman gideri kaç TL'dir?",
  f"{tr(yeni_yillik)} TL",
  [f"{tr(yillik_eski)} TL", f"{tr(mal / yeni_kalan)} TL", f"{tr(ndd / omur)} TL",
   f"{tr(mal / (gecen + yeni_kalan))} TL"],   # geriye dönük sanıp toplam 8 yıla bölme hatası
  f"Faydalı ömür değişikliği bir tahmin değişikliğidir; ileriye dönük uygulanır, geçmiş amortismanlar düzeltilmez. Birikmiş amortisman = {tr(mal)} × {gecen}/{omur} = {tr(birikmis)} TL. Net defter değeri = {tr(mal)} − {tr(birikmis)} = {tr(ndd)} TL. Yeni yıllık amortisman = {tr(ndd)} ÷ {yeni_kalan} = {tr(yeni_yillik)} TL.",
  "TMS 8 - faydalı ömür değişikliği")

m2, kal2, om2, gec2, yeni_kal2, yeni_om2 = 800_000, 50_000, 10, 3, 80_000, 5
yil2 = (m2 - kal2) / om2
bir2 = yil2 * gec2
ndd2 = m2 - bir2
yeni2 = (ndd2 - yeni_kal2) / yeni_om2
q(f"Maliyeti {tr(m2)} TL, kalıntı değeri {tr(kal2)} TL ve faydalı ömrü {om2} yıl olan bir makine doğrusal amortismana tabidir. {gec2}. yılın sonunda kalıntı değer {tr(yeni_kal2)} TL'ye, kalan faydalı ömür {yeni_om2} yıla revize edilmiştir. İzleyen yılın amortisman gideri kaç TL'dir?",
  f"{tr(yeni2)} TL",
  [f"{tr(yil2)} TL", f"{tr(ndd2 / yeni_om2)} TL", f"{tr((m2 - yeni_kal2) / yeni_om2)} TL", f"{tr((ndd2 - kal2) / yeni_om2)} TL"],
  f"Tahmin değişikliği ileriye dönük uygulanır. Eski yıllık amortisman = ({tr(m2)} − {tr(kal2)}) ÷ {om2} = {tr(yil2)} TL. Birikmiş = {tr(yil2)} × {gec2} = {tr(bir2)} TL. Net defter değeri = {tr(m2)} − {tr(bir2)} = {tr(ndd2)} TL. Yeni yıllık = ({tr(ndd2)} − {tr(yeni_kal2)}) ÷ {yeni_om2} = {tr(yeni2)} TL.",
  "TMS 8 - kalıntı değer ve ömür değişikliği")

q("Bir işletme, bir makinenin faydalı ömrünü 10 yıldan 6 yıla indirmiştir. TMS 8 bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmiş dönem amortismanları düzeltilmez; kalan defter değeri kalan ömre dağıtılır",
  ["Geçmiş dönem amortismanları yeniden hesaplanarak karşılaştırmalı tutarlar düzeltilmek zorundadır",
   "En erken dönemin açılış özkaynağı düzeltilerek değişiklik geriye dönük biçimde uygulanmaktadır",
   "Değişiklik önceki dönem hatası sayılır ve geçmiş finansal tablolar yeniden düzenlenmektedir",
   "Değişiklik hiçbir biçimde muhasebeleştirilmez; yalnızca dipnotlarda açıklanmakla yetinilmektedir"],
  "TMS 8: faydalı ömür değişikliği muhasebe tahmini değişikliğidir ve ileriye dönük uygulanır. Geçmiş dönem amortismanları düzeltilmez; varlığın kalan net defter değeri (varsa kalıntı değer düşülerek) kalan faydalı ömre dağıtılır.",
  "TMS 8 - ileriye dönük uygulama (senaryo)")

q("Aşağıdakilerden hangileri TMS 8'e göre muhasebe tahmini sayılır?\n\nI. Şüpheli alacak karşılığı\n\nII. Maddi duran varlığın faydalı ömrü\n\nIII. Garanti karşılığı",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üçü de ölçüm belirsizliğine tabi parasal tutarlardır: şüpheli alacak karşılığı (I), faydalı ömür (II) ve garanti karşılığı (III) muhasebe tahminidir. Değişmeleri ileriye dönük uygulanır.",
  "TMS 8 - tahmin örnekleri")

q("Aşağıdaki ifadelerden hangileri muhasebe tahminleri bakımından doğrudur?\n\nI. Tahmin değişikliği ileriye dönük uygulanır\n\nII. Tahmin değişikliği hata düzeltmesi değildir\n\nIII. Politika mı tahmin mi ayırt edilemiyorsa politika değişikliği sayılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tahmin değişikliği ileriye dönük uygulanır (I) ve yeni bilgiden kaynaklandığından hata düzeltmesi değildir (II). Ayırt edilemeyen değişiklik ise TAHMİN değişikliği sayılır, politika değil; bu nedenle III yanlıştır.",
  "TMS 8 - tahminler")

q("Muhasebe politikası ile muhasebe tahmini arasındaki fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Politika uygulanan ilke ve esası, tahmin ise ölçüm belirsizliğine tabi parasal tutarı ifade eder",
  ["Politika ve tahmin aynı anlama gelen kavramlar olup aralarında hiçbir fark bulunmamaktadır",
   "Politika ölçüm belirsizliğine tabi tutarı, tahmin ise uygulanan ilke ve esasları ifade etmektedir",
   "İkisi de geriye dönük uygulanan değişiklikler olup aralarındaki ayrımın hiçbir sonucu yoktur",
   "İkisi de ileriye dönük uygulanan değişiklikler olup ayrım yalnızca biçimsel nitelik taşımaktadır"],
  "TMS 8: muhasebe politikası uygulanan ilke, esas ve kuralları; muhasebe tahmini ise ölçüm belirsizliğine tabi parasal tutarları ifade eder. Ayrım önemlidir: politika değişikliği geriye dönük, tahmin değişikliği ileriye dönük uygulanır.",
  "TMS 8 - politika-tahmin farkı")

# ── D. Hatalar (16) ────────────────────────────────────────────────────────
q("TMS 8'e göre önceki dönem hataları bakımından aşağıdakilerden hangisi doğrudur?",
  "Güvenilir bilginin kullanılmaması veya yanlış kullanılması sonucu ortaya çıkan ihmal ve yanlış beyanlardır",
  ["Yeni bilgi ve gelişmelerden kaynaklanan ve ileriye dönük uygulanan değişiklikleri ifade eder",
   "İşletmenin uyguladığı ilke, esas ve kuralların bütününü ifade eden bir kavram niteliğindedir",
   "İşletmenin gelecek dönemlere ilişkin belirlediği bütçe sapmalarını ifade eden bir kavramdır",
   "Önceki dönem hatası kavramı TMS 8'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 8: önceki dönem hataları, güvenilir bilginin kullanılmaması veya yanlış kullanılması sonucu, işletmenin bir veya daha fazla önceki dönemine ait finansal tablolarındaki ihmaller ve yanlış beyanlardır.",
  "TMS 8 - önceki dönem hatası tanımı")

q("Önceki dönem hatasının düzeltilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Geriye dönük yeniden düzenleme yoluyla düzeltilir",
  ["İleriye dönük olarak düzeltilir; geçmiş dönem karşılaştırmalı tutarlarına hiç dokunulmamaktadır",
   "Yalnızca cari dönem kâr veya zararına dâhil edilerek düzeltilen bir husus niteliğindedir",
   "Hiçbir biçimde düzeltilmez; hatalı tutarlar olduğu gibi bırakılıp dipnotta açıklanmaktadır",
   "Yalnızca gelecek dönemlerde düzeltilir; cari dönem ve geçmiş dönemler etkilenmemektedir"],
  "TMS 8: işletme, önemli bir önceki dönem hatasını, tespit edildiği dönemden sonraki ilk finansal tablolarında geriye dönük olarak düzeltir.",
  "TMS 8 - geriye dönük yeniden düzenleme")

q("Önceki dönem hatasının cari dönem kâr veya zararı ile ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Hata düzeltmesi cari dönem kâr veya zararına dâhil edilmez",
  ["Hata düzeltmesi her hâlde cari dönem kâr veya zararına dâhil edilmek zorunda tutulmaktadır",
   "Hata düzeltmesi gelecek dönemlerin kâr veya zararına dağıtılarak muhasebeleştirilmektedir",
   "Hata düzeltmesi yalnızca vergi matrahını etkiler; finansal tablo kârını hiç etkilememektedir",
   "Hata düzeltmesinin kâr veya zararla ilişkisi TMS 8'de düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 8: önceki dönem hatalarının düzeltilmesi, hatanın keşfedildiği dönemin kâr veya zararının dışında tutulur; geriye dönük yeniden düzenleme yapılır. Aksi hâlde cari dönem kârı hatalı olurdu.",
  "TMS 8 - hata ve cari dönem kârı")

q("Hatanın geriye dönük düzeltilmesinde izlenecek yol bakımından aşağıdakilerden hangisi doğrudur?",
  "Hatanın oluştuğu önceki dönemin karşılaştırmalı tutarları yeniden düzenlenir",
  ["Yalnızca cari dönem tutarları düzeltilir; karşılaştırmalı bilgilere hiç dokunulmamaktadır",
   "Yalnızca gelecek dönem tutarları düzeltilir; geçmiş ve cari dönem etkilenmeden bırakılmaktadır",
   "Yalnızca vergi beyannamesindeki tutarlar düzeltilir; finansal tablolar değiştirilmemektedir",
   "Hiçbir tutar düzeltilmez; hata yalnızca dipnotlarda açıklanmakla yetinilen bir husustur"],
  "TMS 8: hata, oluştuğu önceki dönem sunuluyorsa o dönemin karşılaştırmalı tutarları yeniden düzenlenerek; hata sunulan en erken dönemden önce oluşmuşsa en erken dönemin açılış varlık, yabancı kaynak ve özkaynak tutarları yeniden düzenlenerek düzeltilir.",
  "TMS 8 - hatanın düzeltilme yolu")

q("Hata sunulan en erken dönemden önce oluşmuşsa aşağıdakilerden hangisi doğrudur?",
  "Sunulan en erken dönemin açılış varlık, yabancı kaynak ve özkaynak tutarları yeniden düzenlenir",
  ["Bu durumda hiçbir düzeltme yapılmaz; hata dikkate alınmadan bırakılan bir husus niteliğindedir",
   "Bu durumda yalnızca cari dönem kâr veya zararı düzeltilir; açılış tutarlarına dokunulmamaktadır",
   "Bu durumda hata ileriye dönük olarak düzeltilir; geçmiş tutarlara hiç dokunulmamaktadır",
   "Bu durumda işletme finansal tablo düzenlemekten tümüyle muaf tutulmuş bulunmaktadır"],
  "TMS 8: hata sunulan en erken dönemden önce oluşmuşsa, sunulan en erken döneme ait varlık, yabancı kaynak ve özkaynakların açılış tutarları yeniden düzenlenir.",
  "TMS 8 - en erken dönem açılış düzeltmesi")

q("Önemli hata içeren veya kasıtlı önemsiz hata içeren finansal tablolar bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu tablolar TFRS'lere uygun sayılmaz",
  ["Bu tablolar hata içerse dahi her hâlde TFRS'lere uygun kabul edilmek zorunda tutulmaktadır",
   "Bu tablolar yalnızca vergi açısından sorun doğurur; TFRS'ye uygunluğu hiç etkilenmemektedir",
   "Bu tabloların TFRS'ye uygunluğu bağımsız denetçinin takdirine bırakılmış bir husustur",
   "Hataların TFRS uygunluğuna etkisi TMS 8'de düzenlenmemiş olup serbest bırakılmış bulunmaktadır"],
  "TMS 8: önemli hatalar içeren veya belirli bir sunumu sağlamak amacıyla kasıtlı olarak yapılan önemsiz hatalar içeren finansal tablolar TFRS'lere uygun değildir.",
  "TMS 8 - hata ve TFRS uygunluğu")

q("Hataların kaynağı bakımından aşağıdakilerden hangisi doğrudur?",
  "Hatalar; matematiksel yanlışlıklar, politikaların yanlış uygulanması, bilgilerin yanlış yorumlanması ve dikkatsizlikten kaynaklanabilir",
  ["Hatalar yalnızca matematiksel yanlışlıklardan kaynaklanabilen bir kavramı ifade etmektedir",
   "Hatalar yalnızca kasıtlı işlemlerden kaynaklanır; dikkatsizlik hiçbir hâlde hata sayılmamaktadır",
   "Hatalar yalnızca bağımsız denetçinin yaptığı yanlışlıklardan kaynaklanabilen bir kavramdır",
   "Hataların kaynağı TMS 8'de düzenlenmemiş olup uygulamada dikkate alınmayan bir husustur"],
  "TMS 8: hatalar; matematiksel hataların, muhasebe politikalarının uygulanmasındaki hataların, bilgilerin gözden kaçırılmasının veya yanlış yorumlanmasının ve dikkatsizliğin sonucunda ortaya çıkabilir.",
  "TMS 8 - hata kaynakları")

q("Hatanın geriye dönük düzeltilmesinin uygulanabilir olmaması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Düzeltmenin uygulanabilir olduğu en erken dönemden itibaren ileriye dönük olarak düzeltilir",
  ["Hata hiçbir biçimde düzeltilmez; hatalı tutarlar olduğu gibi bırakılmak zorunda kalınmaktadır",
   "Hata her hâlde geriye dönük düzeltilmek zorunda olup hiçbir istisna kabul edilmemektedir",
   "Hata yalnızca cari dönem kâr veya zararına dâhil edilerek düzeltilmek zorunda tutulmuştur",
   "Bu durumda işletme finansal tablo düzenlemekten tümüyle muaf tutulmuş bulunmaktadır"],
  "TMS 8: hatanın tüm dönemlere ilişkin etkilerinin belirlenmesi uygulanabilir değilse, işletme uygulamanın mümkün olduğu en erken dönemden itibaren karşılaştırmalı bilgileri ileriye dönük olarak yeniden düzenler.",
  "TMS 8 - hatada uygulanabilir olmama")

q("Bir işletme, geçen yılın kapanış stokunu 40.000 TL fazla saydığını bu yıl fark etmiştir. TMS 8 bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu bir önceki dönem hatasıdır; geriye dönük yeniden düzenleme yapılır",
  ["Bu bir muhasebe tahmini değişikliği olup ileriye dönük olarak uygulanmak zorunda tutulmuştur",
   "Bu bir muhasebe politikası değişikliği olup geçiş hükümlerine göre ele alınmak zorundadır",
   "Bu fark cari dönem kâr veya zararına dâhil edilerek düzeltilmek zorunda olan bir kalemdir",
   "Bu fark hiçbir biçimde düzeltilmez; yalnızca dipnotlarda açıklanmakla yetinilen bir husustur"],
  "Kapanış stokunun fazla sayılması, güvenilir bilginin yanlış kullanılmasından kaynaklanan bir önceki dönem hatasıdır. Geriye dönük yeniden düzenleme yapılır; cari dönem kâr veya zararına dâhil edilmez.",
  "TMS 8 - hata (senaryo)")

hata_stok = 40_000
q(f"Bir işletme, 2025 kapanış stokunu {tr(hata_stok)} TL fazla saydığını 2026'da tespit etmiştir. Vergi etkisi ihmal edildiğinde bu hatanın 2025 dönem kârına etkisi nedir?",
  f"{tr(hata_stok)} TL fazla gösterilmiştir",
  [f"{tr(hata_stok)} TL eksik gösterilmiştir; kapanış stokundaki fazlalık kârı azaltan bir etki doğurur",
   f"{tr(hata_stok * 2)} TL fazla gösterilmiştir; hatanın etkisi iki katı olarak kâra yansımaktadır",
   "Hiç etkilenmemiştir; kapanış stokundaki yanlışlık dönem kârını hiçbir biçimde etkilememektedir",
   f"{tr(hata_stok)} TL fazla gösterilmiştir; ancak bu etki yalnızca 2026 kârında ortaya çıkmaktadır"],
  f"Satılan malın maliyeti = Dönem başı stok + Alışlar − Dönem sonu stok. Kapanış stoku {tr(hata_stok)} TL fazla sayılırsa SMM {tr(hata_stok)} TL EKSİK hesaplanır; gider eksildiği için 2025 kârı {tr(hata_stok)} TL FAZLA gösterilmiş olur.",
  "TMS 8 - hatanın kâra etkisi")

duz = 40_000
q(f"Önceki dönem kârını {tr(duz)} TL fazla gösteren bir hata cari dönemde tespit edilmiştir. Vergi etkisi ihmal edildiğinde bu hatanın düzeltilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  f"Cari dönem açılış geçmiş yıllar kârı {tr(duz)} TL azaltılır",
  [f"Cari dönem açılış geçmiş yıllar kârı {tr(duz)} TL artırılır; hata özkaynağı yükselten bir etki doğurur",
   f"Cari dönem kâr veya zararına {tr(duz)} TL gider yazılır; düzeltme cari dönem sonucunu etkilemektedir",
   f"Gelecek dönemlere {tr(duz)} TL yayılarak düzeltilir; hata ileriye dönük olarak giderilmektedir",
   "Hiçbir düzeltme yapılmaz; hata yalnızca dipnotlarda açıklanmakla yetinilen bir husus niteliğindedir"],
  f"Hata düzeltmesi geriye dönüktür ve cari dönem kâr veya zararına dâhil edilmez. Önceki dönem kârı {tr(duz)} TL fazla gösterildiğinden, açılış geçmiş yıllar kârı {tr(duz)} TL azaltılarak düzeltme özkaynakta yapılır.",
  "TMS 8 - hata düzeltme kaydı")

q("Önceki dönem hatasının açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Hatanın niteliği ile sunulan her önceki döneme ilişkin düzeltme tutarları açıklanır",
  ["Hata hakkında hiçbir açıklama yapılmaz; tutarlar sessizce düzeltilmekle yetinilmektedir",
   "Yalnızca hatanın varlığı belirtilir; niteliği ve tutarsal etkisi hiçbir hâlde açıklanmamaktadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca hata işletmenin kârını azalttığında zorunlu olup artırdığında aranmamaktadır"],
  "TMS 8: işletme önceki dönem hatasının niteliğini, sunulan her bir önceki döneme ilişkin etkilenen kalemlerdeki düzeltme tutarlarını ve mümkünse sunulan en erken dönemin başındaki düzeltme tutarını açıklar.",
  "TMS 8 - hata açıklaması")

q("Bir işletme, geçen yıl bir bakım giderini sehven maddi duran varlık maliyetine eklediğini fark etmiştir. TMS 8 bakımından aşağıdakilerden hangisi doğrudur?",
  "Muhasebe politikasının yanlış uygulanmasından doğan bu durum bir önceki dönem hatasıdır",
  ["Bu bir muhasebe tahmini değişikliği olup ileriye dönük olarak uygulanmak zorunda tutulmuştur",
   "Bu bir muhasebe politikası değişikliği olup geçiş hükümlerine göre ele alınmak zorundadır",
   "Bu durum hiçbir biçimde düzeltilmez; yapılan kayıt olduğu gibi bırakılmak zorunda kalınmaktadır",
   "Bu durum yalnızca vergi mevzuatı açısından sonuç doğurur; finansal tabloları etkilememektedir"],
  "TMS 8: hatalar, muhasebe politikalarının uygulanmasındaki yanlışlıklardan da kaynaklanabilir. Gider yazılması gereken bakım harcamasının aktifleştirilmesi bir önceki dönem hatasıdır; geriye dönük düzeltilir.",
  "TMS 8 - hata (senaryo)")

q("Aşağıdakilerden hangileri TMS 8'e göre geriye dönük olarak uygulanır?\n\nI. Muhasebe politikası değişikliği\n\nII. Önceki dönem hatasının düzeltilmesi\n\nIII. Muhasebe tahmini değişikliği",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Politika değişikliği (I) ve hata düzeltmesi (II) geriye dönük uygulanır. Tahmin değişikliği (III) ise İLERİYE dönük uygulanır; bu nedenle yanlıştır. TMS 8'in en kritik ayrımı budur.",
  "TMS 8 - geriye/ileriye dönük ayrımı")

q("Aşağıdaki ifadelerden hangileri önceki dönem hataları bakımından doğrudur?\n\nI. Hata düzeltmesi cari dönem kâr veya zararına dâhil edilmez\n\nII. Önemli hata içeren tablolar TFRS'lere uygun sayılmaz\n\nIII. Hata düzeltmesi ile tahmin değişikliği aynı anlama gelir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Hata düzeltmesi cari dönem kâr/zararının dışında tutulur (I) ve önemli hata içeren tablolar TFRS'ye uygun değildir (II). Tahmin değişikliği ise yeni bilgiden kaynaklanır ve hata düzeltmesi DEĞİLDİR; bu nedenle III yanlıştır.",
  "TMS 8 - hatalar")

q("Aşağıdaki eşleştirmelerden hangisi TMS 8 bakımından doğrudur?",
  "Politika değişikliği geriye dönük, tahmin değişikliği ileriye dönük uygulanır",
  ["Politika değişikliği ileriye dönük, tahmin değişikliği geriye dönük olarak uygulanmak zorundadır",
   "Politika değişikliği ve tahmin değişikliğinin ikisi de ileriye dönük biçimde uygulanmaktadır",
   "Politika değişikliği ve hata düzeltmesinin ikisi de ileriye dönük olarak uygulanmak zorundadır",
   "Tahmin değişikliği ve hata düzeltmesinin ikisi de geriye dönük biçimde uygulanmak zorundadır"],
  "TMS 8'in temel ayrımı: muhasebe politikası değişikliği ve önceki dönem hatası GERİYE dönük; muhasebe tahmini değişikliği İLERİYE dönük uygulanır.",
  "TMS 8 - temel ayrım")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 8; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} | harf {''.join(x['answer'] for x in out)[:40]}…")
