# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 21 Kur Değişiminin Etkileri — 60 soru.
Kaynak: KGK TMS 21.

★ Gerçek sınav kalibrasyonu:
  · 2025 s.53 — "geçerli para biriminin tespitinde hangisini DİKKATE ALMAZ?"  (negatif kök)
  · 2024 s.50 — "hangisi geçerli para biriminin ..."                          (negatif kök)
  → Sınav bu standartta GEÇERLİ PARA BİRİMİ tespitine ve NEGATİF köke yükleniyor.

KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115).
⚠ NEGATİF kökte kural TERSİNE döner: doğru şık = YANLIŞ/kapsam dışı ifadedir;
  orada doğru şık uzun, çeldiriciler kısa olursa ipucu verir → negatif köklerde
  tüm şıklar birbirine yakın boyda yazıldı.
⚠ Kur SÖZLEŞMEYE/tarihe özgüdür ve soru kökünde verilir → yıla bağlı değil.
"""
import collections, json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_21_kur_degisimi"
PREFIX, SEED = "std-tms21-gen", 20260803
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_21_kur_degisimi.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Geçerli para birimi (sınavın favorisi) (16) ─────────────────────────
q("TMS 21'e göre geçerli para birimi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin faaliyet gösterdiği temel ekonomik çevrede geçerli olan para birimidir",
  ["İşletmenin finansal tablolarını sunmayı tercih ettiği para birimini ifade etmektedir",
   "İşletmenin kurulduğu ülkenin resmî para birimini ifade eden bir kavramı karşılamaktadır",
   "İşletmenin en çok işlem yaptığı bankanın kullandığı para birimini ifade etmek durumundadır",
   "Geçerli para birimi TMS 21'de tanımlanmamış olup uygulamada kullanılmayan bir kavramdır"],
  "TMS 21: geçerli para birimi, işletmenin faaliyet gösterdiği temel ekonomik çevrede geçerli olan para birimidir. Kurulduğu ülkenin para birimi ya da tabloların sunulduğu para birimi ile aynı olmak zorunda değildir.",
  "TMS 21 - geçerli para birimi")

q("TMS 21'e göre raporlama para birimi bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tabloların sunumunda kullanılan para birimidir; işletme bunu serbestçe seçebilir",
  ["İşletmenin faaliyet gösterdiği temel ekonomik çevrenin para birimini ifade etmektedir",
   "İşletmenin kurulduğu ülkenin resmî para birimi olmak zorunda olan bir kavramı karşılar",
   "Her hâlde geçerli para birimiyle aynı olmak zorunda olan bir kavramı ifade etmek durumundadır",
   "Raporlama para birimi TMS 21'de tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TMS 21: raporlama para birimi, finansal tabloların sunumunda kullanılan para birimidir. İşletme finansal tablolarını herhangi bir para biriminde (veya para birimlerinde) sunabilir; bu, geçerli para biriminden farklı olabilir.",
  "TMS 21 - raporlama para birimi")

q("TMS 21'e göre yabancı para bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin geçerli para birimi dışındaki para birimleridir",
  ["İşletmenin raporlama para birimi dışındaki tüm para birimlerini ifade etmek durumundadır",
   "Yalnızca konvertibl olan ve serbestçe alınıp satılabilen para birimlerini ifade etmektedir",
   "Yalnızca işletmenin kurulduğu ülke dışındaki devletlerin para birimlerini karşılamaktadır",
   "Yabancı para kavramı TMS 21'de tanımlanmamış bir husus niteliğinde bulunmak durumundadır"],
  "TMS 21: yabancı para, işletmenin geçerli para birimi dışındaki para birimleridir. Ölçüt raporlama para birimi değil, GEÇERLİ para birimidir.",
  "TMS 21 - yabancı para")

# ★ 2025 s.53 / 2024 s.50 kalıbı — NEGATİF kök, şıklar denk boyda
q("TMS 21'e göre bir işletme, geçerli para biriminin tespitinde aşağıdaki faktörlerden hangisini dikkate almaz?",
  "İşletmenin ortaklarının uyruğunu ve ikametgâhını",
  ["Mal ve hizmetlerin satış fiyatını en çok etkileyen para birimini",
   "İşçilik ve malzeme maliyetlerini en çok etkileyen para birimini",
   "Borçlanma ve özkaynak yoluyla sağlanan fonların para birimini",
   "Faaliyetlerden elde edilen tutarların biriktirildiği para birimini"],
  "TMS 21: geçerli para birimi belirlenirken birincil olarak satış fiyatını ve maliyetleri en çok etkileyen para birimi; ayrıca finansman fonlarının ve faaliyetlerden elde edilip biriktirilen tutarların para birimi dikkate alınır. Ortakların uyruğu veya ikametgâhı bu faktörler arasında YER ALMAZ.",
  "TMS 21 - geçerli para birimi faktörleri")

q("Geçerli para biriminin belirlenmesinde birincil göstergeler bakımından aşağıdakilerden hangisi doğrudur?",
  "Satış fiyatlarını ve mal/hizmet maliyetlerini en çok etkileyen para birimi birincil göstergedir",
  ["Finansman faaliyetlerinden sağlanan fonların para birimi birincil gösterge sayılmak zorundadır",
   "İşletmenin banka hesaplarının bulunduğu para birimi birincil gösterge sayılmak durumundadır",
   "İşletmenin ortaklarına kâr payı ödediği para birimi birincil gösterge olmak zorunda kalınır",
   "Birincil ve ikincil gösterge ayrımı TMS 21'de bulunmamakta olup hepsi eşit sayılmaktadır"],
  "TMS 21: geçerli para birimi belirlenirken öncelikle (a) mal ve hizmetlerin satış fiyatını en çok etkileyen ve (b) işçilik, malzeme ve diğer maliyetleri en çok etkileyen para birimi dikkate alınır. Finansman ve fon biriktirme para birimi ise kanıt sağlayan ikincil göstergelerdir.",
  "TMS 21 - birincil göstergeler")

q("Geçerli para biriminin açık olmadığı durumlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Yönetim, işlemlerin ekonomik etkilerini en iyi yansıtan para birimini muhakemeyle belirler",
  ["Bu durumda her hâlde işletmenin kurulduğu ülkenin para birimi kullanılmak zorunda kalınır",
   "Bu durumda her hâlde en çok işlem yapılan yabancı para birimi kullanılmak zorunda tutulur",
   "Bu durumda işletme finansal tablo düzenlemekten tümüyle muaf tutulmak zorunda bulunmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: göstergelerin karma sonuç vermesi ve geçerli para biriminin açıkça belli olmaması durumunda, yönetim işlem, olay ve koşulların ekonomik etkilerini en iyi biçimde yansıtan geçerli para birimini belirlemek için muhakemesini kullanır.",
  "TMS 21 - muhakeme")

q("Geçerli para biriminin değiştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yalnızca temel ekonomik çevrede değişiklik olursa değişir; değişiklik ileriye dönük uygulanır",
  ["İşletme her dönem geçerli para birimini serbestçe değiştirebilmek zorunda bulunmaktadır",
   "Geçerli para birimi hiçbir hâlde değiştirilemez; ilk belirlenen birim kalıcı olmaktadır",
   "Geçerli para birimi değişikliği her hâlde geriye dönük uygulanmak zorunda tutulmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 21: bir işletmenin geçerli para birimi, ancak temel ekonomik çevresinde değişiklik olması hâlinde değişir. Geçerli para birimindeki değişikliğe ilişkin tüm işlemler değişiklik tarihinden itibaren İLERİYE dönük olarak muhasebeleştirilir.",
  "TMS 21 - geçerli para birimi değişikliği")

q("TMS 21'e göre parasal kalemler bakımından aşağıdakilerden hangisi doğrudur?",
  "Elde tutulan para ile sabit veya belirlenebilir tutarda para olarak alınacak ya da ödenecek varlık ve borçlardır",
  ["İşletmenin fiziki niteliği bulunan tüm varlıklarını kapsayan bir kavramı ifade etmektedir",
   "İşletmenin yalnızca kasa ve banka mevcudunu kapsayan dar kapsamlı bir kavram niteliğindedir",
   "İşletmenin yabancı para cinsinden olan tüm kalemlerini kapsayan bir kavramı karşılamaktadır",
   "Parasal kalem kavramı TMS 21'de tanımlanmamış bir husus niteliğinde bulunmak durumundadır"],
  "TMS 21: parasal kalemlerin temel özelliği, sabit veya belirlenebilir tutarda bir para olarak alma hakkı veya ödeme yükümlülüğü içermesidir (nakit, alacaklar, borçlar, ödenecek nakdi temettü gibi).",
  "TMS 21 - parasal kalem")

q("Aşağıdakilerden hangisi TMS 21'e göre parasal kalem DEĞİLDİR?",
  "Peşin ödenmiş giderler",
  ["Sabit tutarda tahsil edilecek olan ticari alacaklar niteliğindeki varlık kalemlerinin tümü",
   "Belirlenebilir tutarda ödenecek olan ticari borçlar niteliğindeki kaynak kalemlerinin tamamı",
   "İşletmenin kasasında ve bankasında bulunan nakit niteliğindeki varlık kalemlerinin tümü",
   "Nakit olarak ödenmesi kararlaştırılmış ve tutarı belirli olan temettü borcu niteliğinde kalemler"],
  "TMS 21: parasal olmayan kalemlerin temel özelliği, sabit veya belirlenebilir tutarda para alma hakkı veya ödeme yükümlülüğü İÇERMEMESİDİR. Peşin ödenmiş giderler mal veya hizmet alma hakkı verir, para alma hakkı vermez; parasal olmayan kalemdir. Diğerleri parasaldır.",
  "TMS 21 - parasal olmayan kalem")

q("Aşağıdakilerden hangisi TMS 21'e göre parasal olmayan kalemdir?",
  "Şerefiye",
  ["Sabit tutarda tahsil edileceği belirlenmiş olan alacak senetleri niteliğindeki varlık kalemleri",
   "Vadesinde belirli tutarda ödenecek olan banka kredisi niteliğindeki kaynak kalemlerinin tümü",
   "Yabancı para cinsinden bankada tutulan vadesiz mevduat niteliğindeki varlık kalemlerinin tamamı",
   "Tutarı sözleşmeyle belirlenmiş ve nakden ödenecek olan kira borcu niteliğindeki kalemler"],
  "TMS 21: parasal olmayan kalem örnekleri arasında peşin ödenmiş giderler, şerefiye, maddi olmayan duran varlıklar, stoklar, maddi duran varlıklar ve parasal olmayan bir varlığın teslimiyle ödenecek karşılıklar sayılır.",
  "TMS 21 - parasal olmayan kalem örneği")

q("Aşağıdakilerden hangileri TMS 21'e göre parasal olmayan kalemdir?\n\nI. Stoklar\n\nII. Maddi duran varlıklar\n\nIII. Ticari alacaklar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "I ve III"],
  "Stoklar (I) ve maddi duran varlıklar (II) sabit tutarda para alma hakkı vermediğinden parasal olmayan kalemdir. Ticari alacaklar (III) ise belirlenebilir tutarda para alma hakkı verir; PARASAL kalemdir.",
  "TMS 21 - parasal / parasal olmayan ayrımı")

q("Aşağıdakilerden hangileri geçerli para biriminin belirlenmesinde dikkate alınır?\n\nI. Mal ve hizmet satış fiyatını en çok etkileyen para birimi\n\nII. İşçilik ve malzeme maliyetlerini en çok etkileyen para birimi\n\nIII. Finansman faaliyetlerinden sağlanan fonların para birimi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "I ve III"],
  "TMS 21 üçünü de dikkate alır: satış fiyatını (I) ve maliyetleri (II) en çok etkileyen para birimi birincil göstergedir; finansman fonlarının para birimi (III) ise kanıt sağlayan ikincil göstergedir.",
  "TMS 21 - geçerli para birimi göstergeleri")

q("Yurtdışındaki işletmenin geçerli para biriminin belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Faaliyetlerin raporlayan işletmenin uzantısı mı yoksa özerk mi olduğu dikkate alınır",
  ["Yurtdışındaki işletmenin geçerli para birimi her hâlde ana ortaklıkla aynı olmak zorundadır",
   "Yurtdışındaki işletmenin geçerli para birimi her hâlde bulunduğu ülkenin parası olmalıdır",
   "Yurtdışındaki işletmeler için geçerli para birimi kavramı hiç uygulanmamak durumundadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: yurtdışındaki işletmenin geçerli para birimi belirlenirken faaliyetlerinin raporlayan işletmenin bir uzantısı olarak mı yoksa önemli ölçüde özerklikle mi yürütüldüğü, işlemlerin raporlayan işletmeyle oranı, nakit akışlarının doğrudan etkileyip etkilemediği ve borç servisinin yeterliliği gibi ek göstergeler dikkate alınır.",
  "TMS 21 - yurtdışındaki işletme")

q("Bir işletmenin ürün fiyatları ve maliyetleri ağırlıklı olarak avro cinsinden belirlenmekte, ancak işletme finansal tablolarını Türk lirası olarak sunmaktadır. TMS 21 bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçerli para birimi avro, raporlama para birimi Türk lirasıdır",
  ["Hem geçerli hem raporlama para birimi her hâlde Türk lirası olmak zorunda bulunmaktadır",
   "Hem geçerli hem raporlama para birimi her hâlde avro olmak zorunda tutulan bir durumdur",
   "Geçerli para birimi Türk lirası, raporlama para birimi avro olmak zorunda kalınmaktadır",
   "Bu durumda işletme finansal tablo düzenlemekten tümüyle muaf tutulmak zorunda kalır"],
  "TMS 21: geçerli para birimi, satış fiyatlarını ve maliyetleri en çok etkileyen para birimidir — burada avro. Raporlama para birimi ise işletmenin tabloları sunmayı seçtiği birimdir ve serbestçe belirlenebilir — burada TL. İkisi farklı olabilir; bu durumda çevrim yapılır.",
  "TMS 21 - iki para birimi (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 21 bakımından doğrudur?\n\nI. Yabancı para, geçerli para birimi dışındaki para birimidir\n\nII. Geçerli para birimi her dönem serbestçe değiştirilebilir\n\nIII. Raporlama para birimi serbestçe seçilebilir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "II ve III"],
  "Yabancı para, geçerli para birimi dışındaki birimdir (I) ve raporlama para birimi serbestçe seçilebilir (III). Geçerli para birimi ise SERBESTÇE değiştirilemez; yalnızca temel ekonomik çevrede değişiklik olursa değişir. Bu nedenle II yanlıştır.",
  "TMS 21 - para birimleri")

q("Geçerli para birimi değişikliğinin uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişiklik tarihindeki kur kullanılarak tüm kalemler yeni para birimine çevrilir; ileriye dönük uygulanır",
  ["Değişiklik geriye dönük uygulanır ve karşılaştırmalı tutarlar yeniden düzenlenmek zorundadır",
   "Değişiklik hâlinde hiçbir çevrim yapılmaz; tutarlar eski para biriminde bırakılmak zorundadır",
   "Değişiklik hâlinde işletme her hâlde önceki dönem hatası düzeltmesi yapmak zorunda kalır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: geçerli para birimindeki değişikliğe ilişkin tüm işlemler ileriye dönük muhasebeleştirilir. İşletme tüm kalemleri değişiklik tarihindeki kuru kullanarak yeni geçerli para birimine çevirir; parasal olmayan kalemler için ortaya çıkan çevrilmiş tutarlar tarihi maliyet olarak kabul edilir.",
  "TMS 21 - değişikliğin uygulanması")

# ── B. İlk muhasebeleştirme ve dönem sonu ölçüm (16) ───────────────────────
q("Yabancı para işlemin ilk muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlem tarihindeki geçerli para birimi ile yabancı para arasındaki spot kur uygulanır",
  ["Her hâlde dönem sonundaki kapanış kuru uygulanmak zorunda olan bir ölçümü ifade etmektedir",
   "Her hâlde dönem başındaki açılış kuru uygulanmak zorunda tutulan bir ölçümü karşılamaktadır",
   "Her hâlde dönemin ortalama kuru uygulanmak zorunda olan bir ölçümü ifade etmek durumundadır",
   "İlk muhasebeleştirmedeki kur TMS 21'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 21: yabancı para işlem, ilk muhasebeleştirme sırasında, işlem tarihindeki geçerli para birimi ile yabancı para arasındaki spot kur uygulanmak suretiyle geçerli para biriminde kaydedilir.",
  "TMS 21 - ilk muhasebeleştirme")

q("İşlem tarihindeki kurun uygulanmasında kolaylık bakımından aşağıdakilerden hangisi doğrudur?",
  "Kurun önemli ölçüde dalgalanmadığı hâllerde dönemin ortalama kuru kullanılabilir",
  ["Her hâlde işlem tarihinin kesin kuru kullanılmak zorunda olup hiçbir kolaylık bulunmamaktadır",
   "Kur dalgalansa dahi her hâlde dönemin ortalama kuru kullanılmak zorunda tutulmaktadır",
   "Her hâlde dönem sonundaki kapanış kuru kullanılmak zorunda olan bir kolaylığı ifade eder",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: uygulama kolaylığı açısından işlem tarihindeki kura yaklaşan bir kur kullanılabilir (haftalık veya aylık ortalama kur gibi). Ancak kurlar önemli ölçüde dalgalanıyorsa, dönem için ortalama kur kullanılması UYGUN DEĞİLDİR.",
  "TMS 21 - ortalama kur kolaylığı")

q("Raporlama dönemi sonunda yabancı para PARASAL kalemler bakımından aşağıdakilerden hangisi doğrudur?",
  "Kapanış kuru kullanılarak çevrilir",
  ["İşlem tarihindeki tarihî kur kullanılarak çevrilmek zorunda olan bir ölçümü ifade etmektedir",
   "Hiçbir çevrim yapılmaz; ilk kayıt tutarında bırakılmak zorunda olan bir ölçümü karşılamaktadır",
   "Her hâlde dönemin ortalama kuru kullanılarak çevrilmek zorunda tutulan bir ölçümdür",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: her raporlama dönemi sonunda yabancı para birimindeki parasal kalemler kapanış kuru kullanılarak çevrilir.",
  "TMS 21 - parasal kalemlerin dönem sonu ölçümü")

q("Tarihî maliyetiyle ölçülen yabancı para PARASAL OLMAYAN kalemler bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlem tarihindeki kur kullanılarak çevrilir",
  ["Kapanış kuru kullanılarak çevrilmek zorunda olan bir ölçümü ifade etmek durumundadır",
   "Her hâlde dönemin ortalama kuru kullanılarak çevrilmek zorunda tutulan bir ölçümdür",
   "Her raporlama döneminde yeniden değerlenmek zorunda olan bir ölçümü karşılamaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 21: yabancı para birimi üzerinden tarihî maliyetle ölçülen parasal olmayan kalemler, işlem tarihindeki kur kullanılarak çevrilir. Kapanış kuruyla yeniden çevrilmez.",
  "TMS 21 - parasal olmayan kalem (tarihî maliyet)")

q("Gerçeğe uygun değeriyle ölçülen yabancı para PARASAL OLMAYAN kalemler bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değerin belirlendiği tarihteki kur kullanılarak çevrilir",
  ["İşlem tarihindeki tarihî kur kullanılarak çevrilmek zorunda olan bir ölçümü ifade etmektedir",
   "Her hâlde raporlama dönemi sonundaki kapanış kuru kullanılmak zorunda tutulan bir ölçümdür",
   "Her hâlde dönemin ortalama kuru kullanılarak çevrilmek zorunda olan bir ölçümü karşılar",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: yabancı para birimi üzerinden gerçeğe uygun değeriyle ölçülen parasal olmayan kalemler, gerçeğe uygun değerin belirlendiği tarihteki kurlar kullanılarak çevrilir.",
  "TMS 21 - parasal olmayan kalem (GUD)")

q("Parasal kalemlerin ödenmesinden veya çevrilmesinden doğan kur farkları bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak oluştukları dönemin kâr veya zararında muhasebeleştirilir",
  ["Her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda olan bir kalemi ifade eder",
   "Her hâlde doğrudan özkaynakta biriktirilmek zorunda olan bir kalemi karşılamak durumundadır",
   "Her hâlde ilgili varlığın maliyetine eklenmek zorunda tutulan bir kalemi ifade etmektedir",
   "Kur farkları hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmak zorunda kalınır"],
  "TMS 21: parasal kalemlerin ödenmesinden ya da dönem içinde veya önceki finansal tablolarda çevrilmesinden kaynaklanan kur farkları, oluştukları dönemde kâr veya zararda muhasebeleştirilir.",
  "TMS 21 - kur farkının yeri")

q("Parasal olmayan bir kalemin kazanç veya kaybı diğer kapsamlı gelirde muhasebeleştiriliyorsa kur farkı bakımından aşağıdakilerden hangisi doğrudur?",
  "İlgili kur farkı da diğer kapsamlı gelirde muhasebeleştirilir",
  ["İlgili kur farkı her hâlde kâr veya zararda muhasebeleştirilmek zorunda tutulmaktadır",
   "İlgili kur farkı her hâlde varlığın maliyetine eklenmek zorunda olan bir kalemi ifade eder",
   "İlgili kur farkı hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmak zorundadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: parasal olmayan bir kalemden kaynaklanan kazanç veya kayıp diğer kapsamlı gelirde muhasebeleştirildiğinde, bu kazanç veya kaybın kur farkına ilişkin kısmı da diğer kapsamlı gelirde muhasebeleştirilir. Kur farkı, ana kalemi izler.",
  "TMS 21 - kur farkı ana kalemi izler")

kur1, kur2, tutar = 30, 34, 10_000
fark = tutar * (kur2 - kur1)
q(f"Bir işletme, 1 Ekim'de {tr(tutar)} ABD doları tutarında ticari mal satmış ve alacağı henüz tahsil etmemiştir. İşlem tarihindeki kur {kur1} ₺, dönem sonu kapanış kuru {kur2} ₺'dir. TMS 21'e göre dönem sonunda muhasebeleştirilecek kur farkı kaç ₺'dir?",
  f"{tr(fark)} ₺ kur farkı geliri",
  [f"{tr(fark)} ₺ kur farkı gideri; alacak parasal kalem olduğundan kur artışı gider doğurmaktadır",
   f"{tr(tutar * kur2)} ₺ kur farkı geliri; alacağın çevrilmiş tutarının tamamı gelir yazılmaktadır",
   f"{tr(tutar * kur1)} ₺ kur farkı geliri; alacağın ilk kayıt tutarı gelir olarak yazılmaktadır",
   "Kur farkı doğmaz; ticari alacaklar dönem sonunda yeniden çevrilmemek zorunda kalmaktadır"],
  f"Ticari alacak PARASAL kalemdir; dönem sonunda kapanış kuruyla çevrilir. İlk kayıt = {tr(tutar)} × {kur1} = {tr(tutar*kur1)} ₺. Dönem sonu = {tr(tutar)} × {kur2} = {tr(tutar*kur2)} ₺. Kur yükseldiğinden ALACAK değer kazanmıştır: {tr(tutar*kur2)} − {tr(tutar*kur1)} = {tr(fark)} ₺ kur farkı GELİRİ; kâr veya zararda muhasebeleştirilir.",
  "TMS 21 - alacakta kur farkı hesabı")

kurA, kurB, borc = 30, 34, 20_000
fark2 = borc * (kurB - kurA)
q(f"Bir işletmenin {tr(borc)} ABD doları tutarında yabancı para satıcı borcu vardır. Borcun doğduğu tarihte kur {kurA} ₺, dönem sonu kapanış kuru {kurB} ₺'dir. TMS 21'e göre dönem sonunda muhasebeleştirilecek kur farkı kaç ₺'dir?",
  f"{tr(fark2)} ₺ kur farkı gideri",
  [f"{tr(fark2)} ₺ kur farkı geliri; borç parasal kalem olduğundan kur artışı gelir doğurmaktadır",
   f"{tr(borc * kurB)} ₺ kur farkı gideri; borcun çevrilmiş tutarının tamamı gider yazılmaktadır",
   f"{tr(borc * kurA)} ₺ kur farkı gideri; borcun ilk kayıt tutarı gider olarak yazılmaktadır",
   "Kur farkı doğmaz; satıcı borçları dönem sonunda yeniden çevrilmemek zorunda kalmaktadır"],
  f"Satıcı borcu PARASAL kalemdir; kapanış kuruyla çevrilir. İlk kayıt = {tr(borc)} × {kurA} = {tr(borc*kurA)} ₺. Dönem sonu = {tr(borc)} × {kurB} = {tr(borc*kurB)} ₺. Kur yükseldiğinden BORÇ ağırlaşmıştır: {tr(borc*kurB)} − {tr(borc*kurA)} = {tr(fark2)} ₺ kur farkı GİDERİ. Alacakta kur artışı gelir, borçta gider doğurur.",
  "TMS 21 - borçta kur farkı hesabı")

kurS, kurK, stok = 25, 31, 8_000
q(f"Bir işletme, 1 Kasım'da {tr(stok)} ABD doları ödeyerek ticari mal satın almıştır. İşlem tarihindeki kur {kurS} ₺, dönem sonu kapanış kuru {kurK} ₺'dir. Stok tarihî maliyetle ölçülmektedir. TMS 21'e göre stokun dönem sonu defter değeri kaç ₺'dir?",
  f"{tr(stok * kurS)} ₺",
  [f"{tr(stok * kurK)} ₺", f"{tr(stok * (kurK - kurS))} ₺", f"{tr(stok * (kurS + kurK) / 2)} ₺", f"{tr(stok)} ₺"],
  f"Stok PARASAL OLMAYAN kalemdir ve tarihî maliyetle ölçülmektedir; işlem tarihindeki kurla çevrilir ve dönem sonunda YENİDEN ÇEVRİLMEZ: {tr(stok)} × {kurS} = {tr(stok*kurS)} ₺. Kapanış kuru uygulansaydı {tr(stok*kurK)} ₺ bulunurdu ki bu yanlıştır — stokta kur farkı doğmaz.",
  "TMS 21 - parasal olmayan kalemde çevrim yok")

q("Bir işletme yabancı para cinsinden aldığı makineyi tarihî maliyetle izlemektedir. Dönem sonunda kur önemli ölçüde yükselmiştir. TMS 21 bakımından aşağıdakilerden hangisi doğrudur?",
  "Makine parasal olmayan kalem olduğundan yeniden çevrilmez; kur farkı doğmaz",
  ["Makine kapanış kuruyla yeniden çevrilir ve kur farkı gideri yazılmak zorunda tutulmaktadır",
   "Makine kapanış kuruyla çevrilir ve kur farkı maliyete eklenmek zorunda bulunmaktadır",
   "Makine için her hâlde kur farkı geliri muhasebeleştirilmek zorunda olan bir durumu ifade eder",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: tarihî maliyetle ölçülen parasal olmayan kalemler işlem tarihindeki kurla çevrilir ve dönem sonunda kapanış kuruyla yeniden çevrilmez. Maddi duran varlık parasal olmayan kalemdir; kur değişimi onun defter değerini etkilemez, kur farkı doğmaz.",
  "TMS 21 - MDV'de kur farkı yok (senaryo)")

q("Aşağıdaki ifadelerden hangileri dönem sonu çevrimi bakımından doğrudur?\n\nI. Tarihî maliyetli parasal olmayan kalemler kapanış kuruyla yeniden çevrilir\n\nII. Parasal kalemler kapanış kuruyla çevrilir\n\nIII. Gerçeğe uygun değerle ölçülen parasal olmayan kalemler, bu değerin belirlendiği tarihteki kurla çevrilir",
  "II ve III",
  ["I, II ve III", "Yalnız II", "I ve II", "I ve III"],
  "Parasal kalemler kapanış kuruyla (II), gerçeğe uygun değerle ölçülen parasal olmayan kalemler ise GUD'ün belirlendiği tarihteki kurla (III) çevrilir. Tarihî maliyetle ölçülen parasal olmayan kalemler İŞLEM TARİHİ kuruyla çevrilir ve kapanış kuruyla yeniden çevrilmez; bu nedenle I yanlıştır.",
  "TMS 21 - dönem sonu çevrimi")

q("Yurtdışındaki işletmedeki net yatırımın bir parçası olan parasal kalemin kur farkı bakımından aşağıdakilerden hangisi doğrudur?",
  "Konsolide finansal tablolarda diğer kapsamlı gelirde muhasebeleştirilir",
  ["Her hâlde kâr veya zararda muhasebeleştirilmek zorunda olan bir kalemi ifade etmektedir",
   "Her hâlde ilgili varlığın maliyetine eklenmek zorunda olan bir kalemi karşılamak durumundadır",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmak zorunda kalınmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: raporlayan işletmenin yurtdışındaki işletmede bulunan net yatırımının bir parçasını oluşturan parasal kalemden kaynaklanan kur farkları, bireysel tablolarda kâr veya zararda; ancak yurtdışındaki işletmeyi içeren konsolide finansal tablolarda diğer kapsamlı gelirde muhasebeleştirilir ve net yatırımın elden çıkarılmasına kadar özkaynakta biriktirilir.",
  "TMS 21 - net yatırımda kur farkı")

q("Yabancı para işlemlerin niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Yabancı para cinsinden alım-satım, borçlanma ve varlık edinimi yabancı para işlemidir",
  ["Yalnızca yabancı ülkelerdeki taraflarla yapılan işlemler yabancı para işlemi sayılmaktadır",
   "Yalnızca nakit hareketi içeren işlemler yabancı para işlemi sayılmak zorunda kalmaktadır",
   "Yalnızca bankalar aracılığıyla yapılan işlemler yabancı para işlemi sayılmak durumundadır",
   "Yabancı para işlem kavramı TMS 21'de tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TMS 21: yabancı para işlem, yabancı para cinsinden yapılan veya yabancı paranın ödenmesini gerektiren işlemdir; mal/hizmet alım-satımı, yabancı para borç alınıp verilmesi ve yabancı para cinsinden varlık edinimi/elden çıkarımı bunlara dâhildir. İşlemin karşı tarafının yurtdışında olması şart değildir.",
  "TMS 21 - yabancı para işlem")

# ── C. Sunum, çevrim ve açıklamalar (14) ───────────────────────────────────
q("Geçerli para biriminden farklı bir raporlama para birimine çevrimde varlık ve borçlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kapanış kuru kullanılarak çevrilir",
  ["İşlem tarihindeki tarihî kur kullanılarak çevrilmek zorunda olan bir işlemi ifade etmektedir",
   "Her hâlde dönemin ortalama kuru kullanılarak çevrilmek zorunda tutulan bir işlemi karşılar",
   "Hiçbir çevrim yapılmaz; tutarlar geçerli para biriminde bırakılmak zorunda kalınmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: geçerli para biriminden farklı bir raporlama para birimine çevrimde, her finansal durum tablosundaki varlık ve borçlar o tablonun tarihindeki kapanış kuru kullanılarak çevrilir.",
  "TMS 21 - raporlama para birimine çevrim (varlık/borç)")

q("Raporlama para birimine çevrimde gelir ve giderler bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlem tarihlerindeki kurlarla çevrilir; kur önemli dalgalanmıyorsa ortalama kur kullanılabilir",
  ["Her hâlde kapanış kuru kullanılarak çevrilmek zorunda olan bir işlemi ifade etmek durumundadır",
   "Her hâlde dönem başındaki açılış kuru kullanılarak çevrilmek zorunda tutulan bir işlemdir",
   "Hiçbir çevrim yapılmaz; gelir ve giderler geçerli para biriminde bırakılmak zorunda kalınır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: kâr veya zarar ile diğer kapsamlı gelir tablosundaki gelir ve giderler işlem tarihlerindeki kurlar kullanılarak çevrilir. Uygulama kolaylığı için kurlar önemli ölçüde dalgalanmıyorsa dönemin ortalama kuru kullanılabilir.",
  "TMS 21 - çevrimde gelir/gider")

q("Raporlama para birimine çevrimden doğan kur farkları bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer kapsamlı gelirde muhasebeleştirilir",
  ["Her hâlde kâr veya zararda muhasebeleştirilmek zorunda olan bir kalemi ifade etmek durumundadır",
   "Her hâlde varlıkların maliyetine eklenmek zorunda olan bir kalemi karşılamak zorunda kalınır",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmak zorunda bulunmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: geçerli para biriminden farklı bir raporlama para birimine çevrimde ortaya çıkan tüm kur farkları diğer kapsamlı gelirde muhasebeleştirilir. Bu, tek tek parasal kalemlerin kur farkından (kâr/zarara giden) farklıdır.",
  "TMS 21 - çevrim kur farkı")

q("Yurtdışındaki işletmenin elden çıkarılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Özkaynakta biriken kur farkları kâr veya zarara yeniden sınıflandırılır",
  ["Özkaynakta biriken kur farkları her hâlde özkaynakta kalmak zorunda olan tutarları ifade eder",
   "Özkaynakta biriken kur farkları her hâlde geçmiş yıllar kârına aktarılmak zorunda kalınır",
   "Özkaynakta biriken kur farkları her hâlde iptal edilmek zorunda olan tutarları karşılar",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: yurtdışındaki işletmenin elden çıkarılması durumunda, özkaynakta ayrı bir unsur olarak biriktirilmiş bulunan ve o işletmeye ilişkin kur farklarının toplam tutarı, elden çıkarma kazanç veya kaybının muhasebeleştirildiği anda kâr veya zarara yeniden sınıflandırılır.",
  "TMS 21 - elden çıkarmada yeniden sınıflandırma")

q("Yurtdışındaki işletmenin edinimiyle doğan şerefiye ve düzeltmeler bakımından aşağıdakilerden hangisi doğrudur?",
  "Yurtdışındaki işletmenin varlık ve borçları olarak ele alınır; kapanış kuruyla çevrilir",
  ["Raporlayan işletmenin varlıkları sayılır ve tarihî kurla çevrilmek zorunda tutulmaktadır",
   "Her hâlde işlem tarihindeki kurla çevrilir ve sonradan yeniden çevrilmemek zorunda kalınır",
   "Şerefiye hiçbir hâlde çevrime tabi tutulamayan bir kalemi ifade etmek zorunda bulunmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: yurtdışındaki bir işletmenin ediniminden doğan şerefiye ile varlık ve borçların defter değerlerine yapılan gerçeğe uygun değer düzeltmeleri, yurtdışındaki işletmenin varlık ve borçları olarak ele alınır; onun geçerli para biriminde ifade edilir ve kapanış kuruyla çevrilir.",
  "TMS 21 - şerefiyenin çevrimi")

q("TMS 21'e göre yapılacak açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr veya zarara yansıtılan kur farkı tutarı ile özkaynakta biriken net kur farkları açıklanır",
  ["Kur farkları hakkında hiçbir açıklama yapılmasına gerek bulunmamak zorunda kalınmaktadır",
   "Yalnızca kullanılan kurlar açıklanır; tutarlar hiçbir hâlde açıklanmamak zorunda bulunur",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca yurtdışında faaliyeti bulunan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 21: işletme, kâr veya zararda muhasebeleştirilen kur farklarının tutarını (TFRS 9 uyarınca GUD farkı kâr/zarara yansıtılan finansal araçlardan doğanlar hariç) ve diğer kapsamlı gelirde muhasebeleştirilip özkaynakta ayrı bir unsurda biriktirilen net kur farklarının dönem başı ve sonu mutabakatını açıklar.",
  "TMS 21 - açıklamalar")

q("Raporlama para biriminin geçerli para biriminden farklı olması hâlinde açıklama bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu durum, geçerli para birimi ve farklı bir raporlama para birimi kullanılmasının nedeniyle birlikte açıklanır",
  ["Bu durumun açıklanmasına hiçbir hâlde gerek bulunmamak zorunda olan bir husustur",
   "Yalnızca raporlama para birimi belirtilir; geçerli para birimi hiçbir hâlde açıklanmaz",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklanmamaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: raporlama para biriminin geçerli para biriminden farklı olması durumunda, geçerli para birimi belirtilerek bu durum açıklanır ve farklı bir raporlama para birimi kullanılmasının nedeni belirtilir.",
  "TMS 21 - farklı raporlama para birimi açıklaması")

q("Yüksek enflasyonlu ekonomideki yurtdışı işletmenin çevrimi bakımından aşağıdakilerden hangisi doğrudur?",
  "Önce TMS 29 uyarınca düzeltilir, sonra kapanış kuru kullanılarak çevrilir",
  ["Doğrudan tarihî kurlarla çevrilir; TMS 29 düzeltmesi hiçbir hâlde yapılmamak zorundadır",
   "Doğrudan ortalama kurla çevrilir; enflasyon düzeltmesi hiç dikkate alınmamak durumundadır",
   "Bu işletmelerin tabloları hiçbir hâlde çevrilemez; ayrı sunulmak zorunda kalınmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: geçerli para birimi yüksek enflasyonlu bir ekonominin para birimi olan işletmenin finansal tabloları, önce TMS 29 uyarınca yeniden düzenlenir; ardından tüm tutarlar (karşılaştırmalı dâhil) en son finansal durum tablosu tarihindeki kapanış kuru kullanılarak çevrilir.",
  "TMS 21 - yüksek enflasyonda çevrim")

q("Aşağıdakilerden hangisi TMS 21'e göre kur farkının kâr veya zarar DIŞINDA muhasebeleştirildiği bir durumdur?",
  "Yurtdışındaki işletmedeki net yatırımın parçası olan parasal kalemin konsolide tablolardaki kur farkı",
  ["Yabancı para ticari alacağın dönem sonunda kapanış kuruyla çevrilmesinden doğan kur farkı",
   "Yabancı para satıcı borcunun dönem sonunda kapanış kuruyla çevrilmesinden doğan kur farkı",
   "Yabancı para banka mevduatının dönem sonunda kapanış kuruyla çevrilmesinden doğan kur farkı",
   "Yabancı para kredinin vadesinde ödenmesi sırasında ortaya çıkan gerçekleşmiş kur farkı tutarı"],
  "TMS 21: parasal kalemlerden doğan kur farkları kural olarak kâr veya zarara yazılır. İstisna, yurtdışındaki işletmedeki net yatırımın parçası olan parasal kalemdir: konsolide tablolarda diğer kapsamlı gelirde muhasebeleştirilir. Diğer şıkların hepsi olağan parasal kalemdir; kâr/zarara gider.",
  "TMS 21 - kâr/zarar dışı istisna")

q("Aşağıdaki ifadelerden hangileri raporlama para birimine çevrim bakımından doğrudur?\n\nI. Varlık ve borçlar kapanış kuruyla çevrilir\n\nII. Gelir ve giderler işlem tarihi kurlarıyla çevrilir\n\nIII. Çevrimden doğan kur farkları kâr veya zarara yazılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "I ve III"],
  "Varlık ve borçlar kapanış kuruyla (I), gelir ve giderler işlem tarihi kurlarıyla (II) çevrilir. Çevrimden doğan kur farkları ise DİĞER KAPSAMLI GELİRDE muhasebeleştirilir, kâr veya zararda değil. Bu nedenle III yanlıştır.",
  "TMS 21 - çevrim")

q("Bir işletme, yabancı para cinsinden borcunu vadesinde ödemiştir ve ödeme tarihindeki kur, borcun doğduğu tarihteki kurdan yüksektir. TMS 21 bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçekleşen kur farkı gideri, ödemenin yapıldığı dönemin kâr veya zararına yansıtılır",
  ["Gerçekleşen kur farkı her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda kalınır",
   "Gerçekleşen kur farkı her hâlde ilgili varlığın maliyetine eklenmek zorunda tutulmaktadır",
   "Gerçekleşen kur farkı hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: parasal kalemlerin ÖDENMESİNDEN kaynaklanan kur farkları da oluştukları dönemde kâr veya zararda muhasebeleştirilir. Kur yükselmişse borcun ödenmesi daha fazla yerli para gerektirir; aradaki fark kur farkı giderdir.",
  "TMS 21 - ödemede kur farkı (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 21 bakımından doğrudur?\n\nI. Yurtdışı işletme elden çıkarılınca biriken kur farkları özkaynakta kalır\n\nII. Parasal kalemlerin kur farkı kural olarak kâr veya zarara yazılır\n\nIII. Parasal olmayan kalemin kazancı diğer kapsamlı gelirdeyse kur farkı da orada muhasebeleştirilir",
  "II ve III",
  ["I, II ve III", "Yalnız II", "I ve II", "I ve III"],
  "Parasal kalemlerin kur farkı kural olarak kâr/zarara yazılır (II) ve parasal olmayan kalemin kazancı diğer kapsamlı gelirdeyse kur farkı da orada muhasebeleştirilir (III). Yurtdışı işletme elden çıkarılınca özkaynakta biriken kur farkları KÂR VEYA ZARARA YENİDEN SINIFLANDIRILIR; özkaynakta kalmaz. Bu nedenle I yanlıştır.",
  "TMS 21 - kur farkının yeri")

q("TMS 21'in kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "TFRS 9 kapsamındaki türev işlem ve bakiyeler ile riskten korunma muhasebesi kapsam dışıdır",
  ["TMS 21 istisnasız tüm yabancı para işlemlere uygulanır; hiçbir kapsam dışı hâl bulunmamaktadır",
   "TMS 21 yalnızca yurtdışında faaliyeti olan işletmelere uygulanmak zorunda tutulmaktadır",
   "TMS 21 yalnızca nakit işlemlere uygulanır; alacak ve borçlar kapsam dışında bırakılmıştır",
   "TMS 21'in kapsamı Standartta düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 21: TFRS 9 kapsamındaki türev işlem ve bakiyelere (TFRS 9 kapsamı dışında kalan bazı türevler hariç) ve yabancı para kalemlerine ilişkin riskten korunma muhasebesine bu Standart uygulanmaz; TFRS 9 uygulanır.",
  "TMS 21 - kapsam")

q("Aşağıdakilerden hangisi TMS 21'e göre kapanış kuruyla çevrilmez?",
  "Tarihî maliyetiyle ölçülen yabancı para stoklar",
  ["Yabancı para cinsinden bulunan ve tahsil edilecek olan ticari alacaklar niteliğindeki varlıklar",
   "Yabancı para cinsinden ödenecek olan satıcı borçları niteliğindeki kaynak kalemlerinin tümü",
   "Yabancı para cinsinden bankada bulunan vadesiz mevduat niteliğindeki varlık kalemlerinin tamamı",
   "Yabancı para cinsinden alınmış ve vadesinde ödenecek olan banka kredisi niteliğinde borçlar"],
  "TMS 21: kapanış kuruyla çevrilenler PARASAL kalemlerdir (alacak, borç, nakit, kredi). Tarihî maliyetle ölçülen stoklar parasal olmayan kalemdir; işlem tarihindeki kurla çevrilir ve dönem sonunda yeniden çevrilmez.",
  "TMS 21 - kapanış kuru uygulanmayan kalem")

# ── D. Ek hesap ve uygulama (16) ───────────────────────────────────────────
kd1, kd2, mev = 32, 29, 15_000
kayip = mev * (kd1 - kd2)
q(f"Bir işletmenin yabancı para vadesiz mevduatı {tr(mev)} ABD dolarıdır. Önceki dönem sonu kuru {kd1} ₺, bu dönem sonu kapanış kuru {kd2} ₺'dir. TMS 21'e göre bu dönem muhasebeleştirilecek kur farkı kaç ₺'dir?",
  f"{tr(kayip)} ₺ kur farkı gideri",
  [f"{tr(kayip)} ₺ kur farkı geliri; mevduat parasal kalem olduğundan kur düşüşü gelir doğurur",
   f"{tr(mev * kd2)} ₺ kur farkı gideri; mevduatın çevrilmiş tutarının tamamı gider yazılmaktadır",
   f"{tr(mev * kd1)} ₺ kur farkı gideri; mevduatın önceki tutarı gider olarak yazılmak zorundadır",
   "Kur farkı doğmaz; vadesiz mevduat dönem sonunda yeniden çevrilmemek zorunda kalmaktadır"],
  f"Vadesiz mevduat PARASAL kalemdir; kapanış kuruyla çevrilir. Önceki tutar = {tr(mev)} × {kd1} = {tr(mev*kd1)} ₺. Bu dönem = {tr(mev)} × {kd2} = {tr(mev*kd2)} ₺. Kur DÜŞTÜĞÜNDEN varlık değer kaybetmiştir: {tr(mev*kd1)} − {tr(mev*kd2)} = {tr(kayip)} ₺ kur farkı GİDERİ. Varlıkta kur düşüşü gider, borçta gelir doğurur.",
  "TMS 21 - kur düşüşünde varlık")

kb1, kb2, kredi = 30, 27, 50_000
gelir_b = kredi * (kb1 - kb2)
q(f"Bir işletmenin {tr(kredi)} ABD doları tutarında banka kredisi borcu vardır. Önceki dönem sonu kuru {kb1} ₺, bu dönem sonu kapanış kuru {kb2} ₺'dir. TMS 21'e göre bu dönem muhasebeleştirilecek kur farkı kaç ₺'dir?",
  f"{tr(gelir_b)} ₺ kur farkı geliri",
  [f"{tr(gelir_b)} ₺ kur farkı gideri; borç parasal kalem olduğundan kur düşüşü gider doğurmaktadır",
   f"{tr(kredi * kb2)} ₺ kur farkı geliri; borcun çevrilmiş tutarının tamamı gelir yazılmak zorundadır",
   f"{tr(kredi * kb1)} ₺ kur farkı geliri; borcun önceki tutarı gelir olarak yazılmak zorundadır",
   "Kur farkı doğmaz; banka kredileri dönem sonunda yeniden çevrilmemek zorunda kalmaktadır"],
  f"Banka kredisi PARASAL borçtur. Önceki tutar = {tr(kredi)} × {kb1} = {tr(kredi*kb1)} ₺. Bu dönem = {tr(kredi)} × {kb2} = {tr(kredi*kb2)} ₺. Kur DÜŞTÜĞÜNDEN borç hafiflemiştir: {tr(kredi*kb1)} − {tr(kredi*kb2)} = {tr(gelir_b)} ₺ kur farkı GELİRİ. Borçta kur düşüşü gelir doğurur; varlıktakinin tersidir.",
  "TMS 21 - kur düşüşünde borç")

kg1, kg2, mdv = 28, 35, 40_000
q(f"Bir işletme, {tr(mdv)} ABD doları ödeyerek makine satın almıştır. İşlem tarihindeki kur {kg1} ₺, dönem sonu kapanış kuru {kg2} ₺'dir. Makine maliyet modeliyle izlenmektedir. TMS 21'e göre makinenin dönem sonu defter değeri (amortisman ihmal edilerek) kaç ₺'dir?",
  f"{tr(mdv * kg1)} ₺",
  [f"{tr(mdv * kg2)} ₺", f"{tr(mdv * (kg2 - kg1))} ₺", f"{tr(mdv * (kg1 + kg2) / 2)} ₺", f"{tr(mdv)} ₺"],
  f"Maddi duran varlık PARASAL OLMAYAN kalemdir ve maliyet modeliyle (tarihî maliyet) izlenmektedir; işlem tarihindeki kurla çevrilir ve dönem sonunda YENİDEN ÇEVRİLMEZ: {tr(mdv)} × {kg1} = {tr(mdv*kg1)} ₺. Kapanış kuru uygulanırsa {tr(mdv*kg2)} ₺ bulunur ki bu yanlıştır; makinede kur farkı doğmaz.",
  "TMS 21 - MDV'de tarihî kur")

q("Aynı yabancı para tutarında hem alacağı hem borcu bulunan bir işletmede kur yükselmiştir. TMS 21 bakımından aşağıdakilerden hangisi doğrudur?",
  "İkisi de parasal kalemdir; alacakta kur farkı geliri, borçta gideri doğar ve net etki sıfırlanır",
  ["İkisinde de kur farkı gideri doğar; parasal kalemler her hâlde gider doğurmak zorundadır",
   "İkisinde de kur farkı geliri doğar; parasal kalemler her hâlde gelir doğurmak zorunda kalır",
   "Hiçbirinde kur farkı doğmaz; alacak ve borç birbirini otomatik olarak mahsup etmektedir",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: alacak ve borcun ikisi de parasal kalemdir ve kapanış kuruyla çevrilir. Kur yükseldiğinde alacak değer kazanır (gelir), borç ağırlaşır (gider). Tutarlar eşitse kâr veya zarardaki net etki sıfırlanır; ancak iki kur farkı ayrı ayrı muhasebeleştirilir, kendiliğinden mahsup edilmez.",
  "TMS 21 - doğal denge (senaryo)")

q("Yabancı para cinsinden peşin ödenen sigorta primi bakımından aşağıdakilerden hangisi doğrudur?",
  "Parasal olmayan kalemdir; işlem tarihi kuruyla çevrilir ve kur farkı doğmaz",
  ["Parasal kalemdir; kapanış kuruyla çevrilir ve kur farkı doğmak zorunda bulunmaktadır",
   "Her hâlde kapanış kuruyla yeniden çevrilir ve kur farkı gideri yazılmak zorunda kalınır",
   "Hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotlarda açıklanmak zorunda tutulmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: peşin ödenmiş giderler parasal olmayan kalem örneği olarak sayılır — sabit tutarda para alma hakkı değil, gelecekte mal/hizmet alma hakkı verir. Tarihî maliyetle ölçüldüğünden işlem tarihi kuruyla çevrilir; dönem sonunda yeniden çevrilmez, kur farkı doğmaz.",
  "TMS 21 - peşin ödenmiş gider")

q("Yabancı para cinsinden alınan sipariş avansı (henüz mal teslim edilmemiş) bakımından aşağıdakilerden hangisi doğrudur?",
  "Mal teslimiyle kapanacağından parasal olmayan kalemdir; kapanış kuruyla çevrilmez",
  ["Parasal borçtur; kapanış kuruyla çevrilir ve kur farkı doğmak zorunda olan bir kalemdir",
   "Her hâlde kapanış kuruyla yeniden çevrilir ve kur farkı geliri yazılmak zorunda kalınır",
   "Hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotlarda açıklanmak zorunda bulunmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: parasal olmayan kalemin ölçütü, sabit veya belirlenebilir tutarda PARA alma hakkı ya da ödeme yükümlülüğü İÇERMEMESİDİR. Mal teslimiyle kapatılacak alınan avans, para ödeme değil mal teslim yükümlülüğü doğurur; parasal olmayan kalemdir ve yeniden çevrilmez.",
  "TMS 21 - alınan avans")

q("Aşağıdakilerden hangileri TMS 21'e göre parasal kalemdir?\n\nI. Yabancı para banka mevduatı\n\nII. Yabancı para peşin ödenmiş gider\n\nIII. Yabancı para ticari borç",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "II ve III"],
  "Banka mevduatı (I) ve ticari borç (III) sabit/belirlenebilir tutarda para alma hakkı ya da ödeme yükümlülüğü içerir; parasaldır. Peşin ödenmiş gider (II) ise para değil mal/hizmet alma hakkı verir; PARASAL OLMAYAN kalemdir.",
  "TMS 21 - parasal kalem ayrımı")

q("Aşağıdakilerden hangileri TMS 21'e göre kur farkının doğrudan kâr veya zarara yazıldığı hâllerdendir?\n\nI. Yabancı para alacağın kapanış kuruyla çevrilmesi\n\nII. Raporlama para birimine çevrimden doğan farklar\n\nIII. Yurtdışındaki işletmedeki net yatırımın parçası olan parasal kalemin konsolide tablolardaki farkı",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "I ve III"],
  "Olağan parasal kalemin çevrilmesinden doğan kur farkı kâr veya zarara yazılır (I). Raporlama para birimine çevrimden doğan farklar (II) ve yurtdışındaki işletmedeki net yatırımın parçası olan parasal kalemin konsolide tablolardaki farkı (III) ise DİĞER KAPSAMLI GELİRDE muhasebeleştirilir; ikisi de yanlıştır.",
  "TMS 21 - kur farkının yeri")

q("Bir işletmenin geçerli para birimi ile raporlama para birimi aynıdır. TMS 21 bakımından aşağıdakilerden hangisi doğrudur?",
  "Çevrim gerekmez; yalnız yabancı para işlemler için kur uygulanır",
  ["Her hâlde tüm kalemler için raporlama para birimine çevrim yapılmak zorunda tutulmaktadır",
   "Her hâlde diğer kapsamlı gelirde çevrim kur farkı doğmak zorunda olan bir durumu ifade eder",
   "Bu durumda işletme finansal tablo düzenlemekten tümüyle muaf tutulmak zorunda kalmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: raporlama para birimi geçerli para birimiyle aynıysa ayrıca bir çevrim süreci gerekmez. Standardın çevrim hükümleri, geçerli para biriminden FARKLI bir raporlama para birimi kullanıldığında veya yurtdışı işletme konsolide edildiğinde devreye girer. Yabancı para işlemler için kur elbette uygulanır.",
  "TMS 21 - aynı para birimi (senaryo)")

q("Yabancı para işlemin kaydedilmesinde kullanılacak kur bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlemin TMS'lere göre muhasebeleştirilme koşullarının sağlandığı tarihteki kur esas alınır",
  ["Her hâlde faturanın düzenlendiği tarihteki kur esas alınmak zorunda olan bir ölçümdür",
   "Her hâlde ödemenin yapıldığı tarihteki kur esas alınmak zorunda tutulan bir ölçümü karşılar",
   "Her hâlde sözleşmenin imzalandığı tarihteki kur esas alınmak zorunda bulunan bir ölçümdür",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: işlem tarihi, işlemin ilgili TMS'lere göre muhasebeleştirilme koşullarının ilk kez sağlandığı tarihtir. Kur bu tarihe göre belirlenir.",
  "TMS 21 - işlem tarihi")

kf1, kf2, ihr = 26, 33, 12_000
q(f"Bir ihracatçı işletme, 15 Kasım'da {tr(ihr)} ABD doları tutarında mal satmıştır. İşlem tarihindeki kur {kf1} ₺'dir. Alacak, kurun {kf2} ₺ olduğu 20 Aralık'ta tahsil edilmiştir. TMS 21'e göre bu işlemden doğan kur farkı kaç ₺'dir?",
  f"{tr(ihr * (kf2 - kf1))} ₺ kur farkı geliri",
  [f"{tr(ihr * (kf2 - kf1))} ₺ kur farkı gideri; tahsilat sırasında kur artışı gider doğurmaktadır",
   f"{tr(ihr * kf2)} ₺ kur farkı geliri; tahsil edilen tutarın tamamı kur farkı sayılmaktadır",
   f"{tr(ihr * kf1)} ₺ kur farkı geliri; satış tutarının tamamı kur farkı olarak yazılmaktadır",
   "Kur farkı doğmaz; alacak aynı dönem içinde tahsil edildiğinden fark oluşmamak zorundadır"],
  f"Alacak parasal kalemdir. Satışta kayıt = {tr(ihr)} × {kf1} = {tr(ihr*kf1)} ₺. Tahsilatta alınan = {tr(ihr)} × {kf2} = {tr(ihr*kf2)} ₺. Kur yükseldiğinden işletme daha fazla yerli para tahsil etmiştir: {tr(ihr*kf2)} − {tr(ihr*kf1)} = {tr(ihr*(kf2-kf1))} ₺ kur farkı GELİRİ. Ödemeden doğan kur farkı da kâr/zarara yazılır; aynı dönemde gerçekleşmiş olması sonucu değiştirmez.",
  "TMS 21 - gerçekleşmiş kur farkı hesabı")

q("Yabancı para cinsinden yeniden değerleme modeliyle ölçülen arsa bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değerin belirlendiği tarihteki kurla çevrilir; kur farkı yeniden değerleme farkını izler",
  ["Her hâlde işlem tarihindeki tarihî kurla çevrilmek zorunda olan bir ölçümü ifade etmektedir",
   "Her hâlde kapanış kuruyla çevrilir ve kur farkı kâr veya zarara yazılmak zorunda kalınır",
   "Arsa parasal kalem sayıldığından her hâlde kapanış kuruyla çevrilmek zorunda bulunmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: gerçeğe uygun değeriyle ölçülen parasal olmayan kalemler, gerçeğe uygun değerin belirlendiği tarihteki kurla çevrilir. Yeniden değerleme farkı diğer kapsamlı gelirde muhasebeleştirildiğinden, bu kazancın kur farkına ilişkin kısmı da diğer kapsamlı gelirde muhasebeleştirilir — kur farkı ana kalemi izler.",
  "TMS 21 - GUD ile ölçülen parasal olmayan (senaryo)")

q("Aşağıdaki ifadelerden hangileri geçerli para birimi bakımından doğrudur?\n\nI. Temel ekonomik çevrenin para birimidir\n\nII. Yalnızca temel ekonomik çevre değişirse değişir\n\nIII. İşletmenin kurulduğu ülkenin para birimi olmak zorundadır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "I ve III"],
  "Geçerli para birimi temel ekonomik çevrenin para birimidir (I) ve yalnızca o çevre değişirse değişir (II). İşletmenin kurulduğu ülkenin para birimi olmak ZORUNDA DEĞİLDİR; nitekim Türkiye'de kurulu bir işletmenin geçerli para birimi avro olabilir. Bu nedenle III yanlıştır.",
  "TMS 21 - geçerli para birimi")

q("Kur farkının ilgili varlığın maliyetine eklenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 21 kural olarak buna izin vermez; ancak TMS 23 kapsamında faiz düzeltmesi sayılan kısım aktifleştirilebilir",
  ["Kur farkları her hâlde ilgili varlığın maliyetine eklenmek zorunda tutulan kalemleri ifade eder",
   "Kur farkları hiçbir hâlde ve hiçbir koşulda varlık maliyetiyle ilişkilendirilememek durumundadır",
   "Kur farkları her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemleri karşılamaktadır",
   "Bu husus hiçbir standartta düzenlenmemiş olup uygulamada serbest bırakılmış bulunmaktadır"],
  "TMS 21: parasal kalemlerden doğan kur farkları kural olarak kâr veya zarara yazılır; varlık maliyetine eklenmez. Ancak TMS 23 uyarınca, yabancı para borçlanmalarında FAİZ MALİYETLERİNE İLİŞKİN DÜZELTME olarak dikkate alınan kur farkları borçlanma maliyeti sayılır ve özellikli varlıkta aktifleştirilebilir.",
  "TMS 21 - TMS 23 ile kesişim")

q("Aşağıdaki ifadelerden hangileri TMS 21 bakımından doğrudur?\n\nI. Kurlar önemli dalgalanıyorsa ortalama kur kullanılması uygun değildir\n\nII. Yüksek enflasyonlu ekonomide önce TMS 29 düzeltmesi yapılır\n\nIII. TFRS 9 kapsamındaki türev işlem ve bakiyeler TMS 21'in kapsamı dışındadır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "I ve III"],
  "Üçü de doğrudur: kurlar önemli ölçüde dalgalanıyorsa ortalama kur uygun değildir (I); yüksek enflasyonlu ekonomide önce TMS 29 düzeltmesi yapılıp sonra kapanış kuruyla çevrilir (II); TFRS 9 kapsamındaki türev işlem ve bakiyeler TMS 21'in kapsamı dışındadır ve TFRS 9'a tabidir (III).",
  "TMS 21 - kapsam ve uygulama")

q("Bir işletmenin yurtdışındaki bağlı ortaklığının geçerli para birimi ana ortaklıktan farklıdır. Konsolidasyonda TMS 21 bakımından aşağıdakilerden hangisi doğrudur?",
  "Bağlı ortaklığın tabloları raporlama para birimine çevrilir; çevrim farkları diğer kapsamlı gelirde birikir",
  ["Bağlı ortaklığın tabloları çevrilmeden doğrudan konsolide edilmek zorunda tutulmaktadır",
   "Çevrim farkları her hâlde kâr veya zararda muhasebeleştirilmek zorunda olan kalemleri ifade eder",
   "Bağlı ortaklık her hâlde ana ortaklığın geçerli para birimini benimsemek zorunda kalmaktadır",
   "Bu husus TMS 21'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 21: yurtdışındaki işletmenin sonuçları ve finansal durumu raporlama para birimine çevrilir — varlık/borçlar kapanış kuruyla, gelir/giderler işlem tarihi kurlarıyla. Ortaya çıkan tüm kur farkları diğer kapsamlı gelirde muhasebeleştirilir ve elden çıkarmaya kadar özkaynakta birikir.",
  "TMS 21 - konsolidasyonda çevrim (senaryo)")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 21; 2025/2024 kalıbına kalibre)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    dagilim = collections.Counter(x["options"][x["answer"]].strip() for x in onc)
    hepsi = dagilim["I, II ve III"]
    # ⚠ "hepsi" oranı tek başına yetmez: 10 öncüllünün 9'u "I ve II" ise bu da örüntüdür.
    en_cok = dagilim.most_common(1)[0] if dagilim else ("-", 0)
    neg = sum(1 for x in out if re.search(r"(değildir|çevrilmez|almaz)\s*\?", x["stem"], re.I))
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} | hepsi {hepsi} (%{hepsi*100//max(len(onc),1)}) "
          f"| en çok tekrar eden cevap: {en_cok[0]!r} ×{en_cok[1]} | negatif kök {neg}")
    print("   öncül cevap dağılımı:", dict(dagilim))
    assert en_cok[1] <= len(onc) * 0.4, f"öncüllerde örüntü: {en_cok}"
    assert 0.1 <= hepsi / max(len(onc), 1) <= 0.3, f"'hepsi' oranı {hepsi}/{len(onc)}"
    print("   harf:", "".join(x["answer"] for x in out))
