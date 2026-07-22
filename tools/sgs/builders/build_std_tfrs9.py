# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TFRS 9 Finansal Araçlar — 60 soru.
Kaynak: KGK TFRS 9 (+ TMS 32 tanımları). Aritmetik python'da hesaplanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-10 soru, "hepsi" ~2 (%20-25).
NOT: faiz oranları soru kökünde verilir (sözleşme oranı) → yıla bağlı değil."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tfrs_9_finansal_arac"
PREFIX, SEED = "std-tfrs9-gen", 20260311
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tfrs_9_finansal_arac.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanımlar ve kapsam (14) ─────────────────────────────────────────────
q("Finansal araç bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir işletmede finansal varlık, başka bir işletmede finansal borç veya özkaynak aracı doğuran sözleşmedir",
  ["Yalnızca nakit ve nakit benzeri varlıkları ifade eden dar kapsamlı bir kavram niteliğindedir",
   "Yalnızca borsada işlem gören hisse senetlerini ifade eden bir kavramı karşılamak durumundadır",
   "İşletmenin fiziksel varlıklarını ve stoklarını ifade eden bir kavramı karşılamak zorundadır",
   "Finansal araç kavramı hiçbir standartta tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 32: finansal araç, bir işletmenin finansal varlığı ile başka bir işletmenin finansal borcu veya özkaynağa dayalı finansal aracında artışa neden olan herhangi bir sözleşmedir. TFRS 9 bu araçların muhasebeleştirilmesini düzenler.",
  "TFRS 9 - finansal araç tanımı")

q("Aşağıdakilerden hangisi finansal varlık DEĞİLDİR?",
  "Stoklar",
  ["İşletmenin kasasında ve bankasındaki nakit niteliğindeki varlıkların tamamı",
   "Başka bir işletmeden nakit alınmasını sağlayan sözleşmeye bağlı hak niteliğindeki alacaklar",
   "Başka bir işletmenin özkaynağına dayalı finansal aracı niteliğindeki yatırımların tümü",
   "Başka bir işletmeyle finansal varlık takas etme hakkı doğuran sözleşme niteliğindeki haklar"],
  "TMS 32: finansal varlık; nakit, başka bir işletmenin özkaynağına dayalı finansal aracı, sözleşmeye bağlı nakit alma hakkı veya elverişli koşullarda finansal araç takas etme hakkı ile belirli sözleşmelerden oluşur. STOKLAR fiziki varlıktır; sözleşmeye bağlı nakit hakkı doğurmaz, finansal varlık değildir.",
  "TFRS 9 - finansal varlık olmayan")

q("Finansal borç bakımından aşağıdakilerden hangisi doğrudur?",
  "Başka bir işletmeye nakit veya finansal varlık verilmesine ilişkin sözleşmeye bağlı yükümlülüktür",
  ["İşletmenin ortaklara olan sermaye yükümlülüğünü ifade eden bir kavramı karşılamak zorundadır",
   "İşletmenin stok alımından doğan tüm yükümlülüklerini kapsayan bir kavramı ifade etmektedir",
   "İşletmenin vergi dairesine olan borçlarını ifade eden bir kavramı karşılamak durumundadır",
   "Finansal borç kavramı hiçbir standartta tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 32: finansal borç, başka bir işletmeye nakit veya başka bir finansal varlık verilmesine ilişkin sözleşmeye bağlı yükümlülük ya da işletmenin aleyhine olabilecek koşullarda finansal varlık veya borçların takas edilmesine ilişkin sözleşmeye bağlı yükümlülüktür.",
  "TFRS 9 - finansal borç")

q("Finansal varlığın ilk muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, sözleşme hükümlerine taraf olduğunda finansal varlığı veya borcu muhasebeleştirir",
  ["İşletme yalnızca nakit tahsil edildiğinde muhasebeleştirmek zorunda olan bir kalemi ifade eder",
   "İşletme yalnızca vade geldiğinde muhasebeleştirmek zorunda tutulan bir kalemi karşılamaktadır",
   "İşletme yalnızca vergi idaresi talep ettiğinde muhasebeleştirmek zorunda bulunmaktadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: işletme, finansal tablolarına yalnızca finansal aracın sözleşmeye bağlı hükümlerine taraf olduğunda bir finansal varlık veya finansal borç yansıtır.",
  "TFRS 9 - ilk muhasebeleştirme zamanı")

q("Finansal varlık ve borçların ilk ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değeriyle ölçülür; GUDFK dışındakilerde işlem maliyetleri eklenir veya düşülür",
  ["Her hâlde nominal değeriyle ölçülür; gerçeğe uygun değer hiç dikkate alınmamak zorundadır",
   "Her hâlde itfa edilmiş maliyetiyle ölçülür; işlem maliyetleri hiçbir hâlde dikkate alınmaz",
   "Her hâlde vade sonundaki tutarıyla ölçülür; bugünkü değer hiç dikkate alınmamaktadır",
   "İlk ölçüm esası TFRS 9'da düzenlenmemiş olup işletmenin takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: işletme, ilk muhasebeleştirmede finansal varlık veya borcu gerçeğe uygun değerinden ölçer. Gerçeğe uygun değer farkı kâr veya zarara yansıtılan (GUDFK) araçlar dışında, edinimle doğrudan ilişkilendirilebilen işlem maliyetleri de eklenir (borçlarda düşülür).",
  "TFRS 9 - ilk ölçüm")

q("Gerçeğe uygun değer farkı kâr veya zarara yansıtılan finansal varlıklarda işlem maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlem maliyetleri doğrudan kâr veya zarara yansıtılır; maliyete eklenmez",
  ["İşlem maliyetleri her hâlde varlığın maliyetine eklenmek zorunda olan kalemleri ifade eder",
   "İşlem maliyetleri her hâlde doğrudan özkaynaklara kaydedilmek zorunda tutulmaktadır",
   "İşlem maliyetleri hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmak zorundadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TFRS 9: gerçeğe uygun değer farkı kâr veya zarara yansıtılan finansal varlık veya borçlarda, işlem maliyetleri ilk ölçüme DÂHİL EDİLMEZ; doğrudan kâr veya zarara yansıtılır. Diğer sınıflarda ise maliyete eklenir.",
  "TFRS 9 - GUDFK'da işlem maliyetleri")

q("Finansal varlıkların sınıflandırılmasında esas alınan iki ölçüt bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin yönetim iş modeli ile finansal varlığın sözleşmeye bağlı nakit akışı özellikleridir",
  ["Yalnızca yönetimin varlığı elde tutma niyeti esas alınır; başka bir ölçüt aranmamaktadır",
   "Yalnızca varlığın vadesi esas alınır; kısa vadeliler ve uzun vadeliler ayrı sınıflandırılır",
   "Yalnızca varlığın borsada işlem görüp görmediği esas alınmak zorunda bulunmaktadır",
   "Sınıflandırma ölçütleri TFRS 9'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 9: finansal varlıklar, (a) işletmenin finansal varlıkların yönetimi için kullandığı iş modeli ve (b) finansal varlığın sözleşmeye bağlı nakit akışlarının özellikleri esas alınarak sınıflandırılır. Eski TMS 39'daki niyet temelli sınıflandırma terk edilmiştir.",
  "TFRS 9 - sınıflandırma ölçütleri")

q("TFRS 9'a göre finansal varlıkların ölçüm sınıfları bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfa edilmiş maliyet, GUDDKG ve GUDFK olmak üzere üç ölçüm sınıfı vardır",
  ["Yalnızca tek bir ölçüm sınıfı bulunmakta olup tüm finansal varlıklar aynı biçimde ölçülmektedir",
   "Yalnızca itfa edilmiş maliyet sınıfı bulunmakta olup gerçeğe uygun değer hiç kullanılmamaktadır",
   "Yalnızca gerçeğe uygun değer sınıfı bulunmakta olup itfa edilmiş maliyet hiç kullanılmamaktadır",
   "Ölçüm sınıfları TFRS 9'da düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TFRS 9: finansal varlıklar üç ölçüm sınıfına ayrılır: itfa edilmiş maliyet, gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılan (GUDDKG) ve gerçeğe uygun değer farkı kâr veya zarara yansıtılan (GUDFK).",
  "TFRS 9 - üç ölçüm sınıfı")

q("İtfa edilmiş maliyetle ölçülen finansal varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "İş modeli sözleşmeye bağlı nakit akışlarının tahsili ve nakit akışları yalnızca anapara ve faiz ödemelerini içeriyorsa bu sınıfa girer",
  ["Her finansal varlık istisnasız bu sınıfta ölçülmek zorunda olup başka sınıf bulunmamaktadır",
   "Yalnızca borsada işlem gören varlıklar bu sınıfta ölçülmek zorunda tutulan kalemleri ifade eder",
   "Yalnızca yönetimin öyle karar verdiği varlıklar bu sınıfta ölçülmek zorunda bulunmaktadır",
   "Bu sınıfın koşulları TFRS 9'da düzenlenmemiş bir husus niteliğinde bulunmak durumundadır"],
  "TFRS 9: finansal varlık, (a) sözleşmeye bağlı nakit akışlarının tahsil edilmesini amaçlayan bir iş modeli kapsamında elde tutuluyorsa ve (b) sözleşme şartları belirli tarihlerde SADECE anapara ve anapara bakiyesine ilişkin faiz ödemelerini içeren nakit akışlarına yol açıyorsa itfa edilmiş maliyetinden ölçülür.",
  "TFRS 9 - itfa edilmiş maliyet koşulları")

q("Gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılan finansal varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "İş modeli hem nakit akışı tahsilini hem satışı amaçlıyorsa ve nakit akışları anapara ile faizden oluşuyorsa bu sınıfa girer",
  ["Yalnızca satış amacıyla elde tutulan varlıklar bu sınıfta ölçülmek zorunda tutulmaktadır",
   "Yalnızca vadeye kadar elde tutulacak varlıklar bu sınıfta ölçülmek zorunda bulunmaktadır",
   "Yalnızca yönetimin öyle karar verdiği varlıklar bu sınıfta ölçülmek zorunda kalınmaktadır",
   "Bu sınıfın koşulları TFRS 9'da düzenlenmemiş bir husus niteliğinde bulunmak durumundadır"],
  "TFRS 9: finansal varlık, (a) hem sözleşmeye bağlı nakit akışlarının tahsilini hem finansal varlığın satılmasını amaçlayan bir iş modeli kapsamında elde tutuluyorsa ve (b) nakit akışları sadece anapara ve faiz ödemelerini içeriyorsa gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak ölçülür.",
  "TFRS 9 - GUDDKG koşulları")

q("Gerçeğe uygun değer farkı kâr veya zarara yansıtılan finansal varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfa edilmiş maliyet veya GUDDKG koşullarını sağlamayan finansal varlıklar bu sınıfta ölçülür",
  ["Yalnızca vadeye kadar elde tutulan varlıklar bu sınıfta ölçülmek zorunda tutulmaktadır",
   "Yalnızca alacaklar bu sınıfta ölçülmek zorunda olup diğer varlıklar kapsam dışı kalmaktadır",
   "Hiçbir varlık bu sınıfta ölçülemez; TFRS 9 bu sınıfı kabul etmemiş bulunmak durumundadır",
   "Bu sınıfın koşulları TFRS 9'da düzenlenmemiş bir husus niteliğinde bulunmak durumundadır"],
  "TFRS 9: itfa edilmiş maliyetten veya gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak ölçülmeyen finansal varlıklar, gerçeğe uygun değer farkı kâr veya zarara yansıtılarak ölçülür. Bu, artık (kalıntı) sınıftır.",
  "TFRS 9 - GUDFK sınıfı")

q("Aşağıdakilerden hangileri TFRS 9'a göre finansal varlıkların ölçüm sınıflarındandır?\n\nI. İtfa edilmiş maliyet\n\nII. Gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılan\n\nIII. Gerçeğe uygun değer farkı kâr veya zarara yansıtılan",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TFRS 9 üç ölçüm sınıfı öngörür: itfa edilmiş maliyet (I), gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılan (II) ve gerçeğe uygun değer farkı kâr veya zarara yansıtılan (III).",
  "TFRS 9 - ölçüm sınıfları")

q("Aşağıdaki ifadelerden hangileri finansal varlıkların sınıflandırılması bakımından doğrudur?\n\nI. İşletmenin iş modeli esas alınır\n\nII. İşletmenin faaliyet gösterdiği sektör tek başına esas alınır\n\nIII. Yönetimin varlığı elde tutma niyeti tek başına belirleyicidir",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "TFRS 9 sınıflandırmada işletmenin iş modelini esas alır (I). Faaliyet gösterilen sektör tek başına sınıflandırma ölçütü değildir (II); yönetimin varlığı elde tutma niyeti de tek başına belirleyici değildir (III). Yalnız I doğrudur.",
  "TFRS 9 - sınıflandırma")

q("Sadece anapara ve faiz ödemesi ölçütü bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akışlarının belirli tarihlerde yalnızca anapara ve anapara bakiyesine ilişkin faizden oluşması gerekir",
  ["Nakit akışlarının her hâlde işletmenin kârına bağlı olması gerekmek zorunda bulunmaktadır",
   "Nakit akışlarının her hâlde borsa endeksine bağlı olması gerekmek zorunda tutulmaktadır",
   "Nakit akışı özellikleri hiçbir hâlde dikkate alınmaz; yalnızca iş modeli esas alınmaktadır",
   "Bu ölçüt TFRS 9'da düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TFRS 9: sözleşme şartlarının belirli tarihlerde SADECE anapara ve anapara bakiyesine ilişkin faiz ödemelerini içeren nakit akışlarına yol açması gerekir. Faiz; paranın zaman değeri, kredi riski, diğer temel borç verme riskleri ve kâr marjını içerir. Kârı paylaşan araçlar bu ölçütü sağlamaz.",
  "TFRS 9 - SPPI ölçütü")

# ── B. Sonraki ölçüm ve özkaynak araçları (16) ─────────────────────────────
q("İtfa edilmiş maliyet yönteminde etkin faiz bakımından aşağıdakilerden hangisi doğrudur?",
  "Faiz geliri, etkin faiz oranı brüt defter değerine uygulanarak hesaplanır",
  ["Faiz geliri her hâlde nominal faiz oranı üzerinden hesaplanmak zorunda tutulmaktadır",
   "Faiz geliri her hâlde vade sonunda tek seferde muhasebeleştirilmek zorunda bulunmaktadır",
   "İtfa edilmiş maliyette hiçbir hâlde faiz geliri hesaplanmaz; yalnızca anapara izlenmektedir",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: faiz geliri, etkin faiz yöntemi kullanılarak hesaplanır. Kural olarak etkin faiz oranı finansal varlığın brüt defter değerine uygulanır. Etkin faiz oranı, beklenen ömür boyunca tahmini nakit akışlarını brüt defter değerine iskonto eden orandır.",
  "TFRS 9 - etkin faiz yöntemi")

q("Etkin faiz oranı bakımından aşağıdakilerden hangisi doğrudur?",
  "Beklenen ömür boyunca tahmini nakit akışlarını brüt defter değerine iskonto eden orandır",
  ["Sözleşmede yazılı olan nominal faiz oranını ifade eden bir kavramı karşılamak zorundadır",
   "Merkez bankasının ilan ettiği politika faizini ifade eden bir kavramı karşılamak durumundadır",
   "İşletmenin ortalama borçlanma maliyetini ifade eden bir kavramı karşılamak zorunda kalınır",
   "Etkin faiz oranı TFRS 9'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TFRS 9: etkin faiz oranı, finansal varlığın veya borcun beklenen ömrü boyunca tahmini gelecek nakit ödeme veya tahsilatlarını tam olarak finansal varlığın brüt defter değerine ya da finansal borcun itfa edilmiş maliyetine iskonto eden orandır.",
  "TFRS 9 - etkin faiz oranı")

q("GUDDKG olarak ölçülen bir borçlanma aracında değer değişimleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Değer değişimi diğer kapsamlı gelirde muhasebeleştirilir; faiz ve değer düşüklüğü kâr veya zarara yansıtılır",
  ["Tüm değişimler her hâlde kâr veya zarara yansıtılmak zorunda olan kalemleri ifade etmektedir",
   "Tüm değişimler her hâlde doğrudan özkaynaktan indirilmek zorunda tutulan kalemleri karşılar",
   "Hiçbir değişim kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilmek zorunda kalınır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: GUDDKG olarak ölçülen borçlanma araçlarında kazanç ve kayıplar diğer kapsamlı gelirde muhasebeleştirilir. Ancak etkin faiz yöntemiyle hesaplanan faiz geliri, değer düşüklüğü kazanç/kayıpları ve kur farkları kâr veya zararda muhasebeleştirilir.",
  "TFRS 9 - GUDDKG borçlanma aracı")

q("GUDDKG olarak ölçülen bir borçlanma aracının finansal tablo dışı bırakılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer kapsamlı gelirde biriken kazanç veya kayıp kâr veya zarara yeniden sınıflandırılır",
  ["Biriken tutar her hâlde özkaynakta kalmak zorunda olup hiçbir hâlde aktarılamamaktadır",
   "Biriken tutar her hâlde doğrudan geçmiş yıllar kârına aktarılmak zorunda tutulmaktadır",
   "Biriken tutar hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmak zorunda kalınır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TFRS 9: GUDDKG olarak ölçülen BORÇLANMA aracı finansal tablo dışı bırakıldığında, daha önce diğer kapsamlı gelirde muhasebeleştirilmiş olan toplam kazanç veya kayıp, özkaynaktan çıkarılıp kâr veya zarara yeniden sınıflandırılır.",
  "TFRS 9 - GUDDKG'de yeniden sınıflandırma")

q("Özkaynağa dayalı finansal araçlara yapılan yatırımlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak GUDFK ile ölçülür; ticari amaçla elde tutulmayanlar için geri dönülemez GUDDKG tercihi yapılabilir",
  ["Her hâlde itfa edilmiş maliyetle ölçülmek zorunda olan kalemleri ifade etmek durumundadır",
   "Her hâlde ve istisnasız GUDDKG ile ölçülmek zorunda tutulan kalemleri karşılamaktadır",
   "Her hâlde maliyet bedeliyle ölçülmek zorunda olup gerçeğe uygun değer hiç kullanılmaz",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TFRS 9: özkaynağa dayalı finansal araçlara yapılan yatırımlar kural olarak GUDFK ile ölçülür. Ancak ticari amaçla elde tutulmayan özkaynak araçları için, ilk muhasebeleştirmede gerçeğe uygun değer değişimlerini diğer kapsamlı gelirde sunma yönünde GERİ DÖNÜLEMEZ bir tercih yapılabilir.",
  "TFRS 9 - özkaynak araçları")

q("Özkaynak aracı için yapılan GUDDKG tercihinin niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "İlk muhasebeleştirmede yapılır ve geri dönülemez niteliktedir",
  ["Her dönem serbestçe değiştirilebilen ve geri alınabilen bir tercihi ifade etmek durumundadır",
   "Yalnızca vergi idaresi izin verdiğinde yapılabilen bir tercihi ifade etmek zorunda kalınmaktadır",
   "Varlığın satılmasına kadar istenildiği zaman yapılabilen bir tercihi karşılamak durumundadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: bu tercih İLK MUHASEBELEŞTİRMEDE, araç bazında yapılır ve GERİ DÖNÜLEMEZ. İşletme sonradan bu tercihten vazgeçemez.",
  "TFRS 9 - tercihin geri dönülemezliği")

q("GUDDKG tercihi yapılan özkaynak aracının satılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer kapsamlı gelirde biriken tutar kâr veya zarara yeniden sınıflandırılmaz; özkaynak içinde aktarılabilir",
  ["Biriken tutar her hâlde kâr veya zarara yeniden sınıflandırılmak zorunda tutulmaktadır",
   "Biriken tutar her hâlde derhâl gelir olarak kâr veya zarara yazılmak zorunda bulunmaktadır",
   "Biriken tutar her hâlde varlığın maliyetine eklenmek zorunda olan kalemleri ifade etmektedir",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: GUDDKG tercihi yapılan ÖZKAYNAK araçlarında, diğer kapsamlı gelirde muhasebeleştirilen tutarlar sonradan kâr veya zarara YENİDEN SINIFLANDIRILMAZ. İşletme özkaynak içinde birikmiş kazancı aktarabilir. Bu, borçlanma araçlarındaki GUDDKG'den temel farkıdır.",
  "TFRS 9 - özkaynak GUDDKG'de yeniden sınıflandırma yasağı")

q("GUDDKG tercihi yapılan özkaynak aracından elde edilen kâr payları bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırımın maliyetinin geri kazanımını temsil etmedikçe kâr veya zarara yansıtılır",
  ["Kâr payları her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulmaktadır",
   "Kâr payları her hâlde varlığın maliyetinden indirilmek zorunda olan kalemleri ifade eder",
   "Kâr payları hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmak zorunda kalınır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: GUDDKG olarak ölçülen özkaynak araçlarından elde edilen kâr payları, yatırımın maliyetinin bir kısmının geri kazanımını açıkça temsil etmedikçe kâr veya zararda muhasebeleştirilir. Değer değişimleri DKG'de kalsa da kâr payı kâr/zarara gider.",
  "TFRS 9 - özkaynak GUDDKG'de kâr payı")

q("Finansal borçların sonraki ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak itfa edilmiş maliyetle ölçülür; belirli borçlar GUDFK ile ölçülür",
  ["Tüm finansal borçlar her hâlde gerçeğe uygun değerle ölçülmek zorunda tutulmaktadır",
   "Tüm finansal borçlar her hâlde nominal değerleriyle ölçülmek zorunda bulunmaktadır",
   "Tüm finansal borçlar her hâlde diğer kapsamlı gelirle ilişkilendirilerek ölçülmektedir",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TFRS 9: işletme, tüm finansal borçları sonradan itfa edilmiş maliyetinden ölçer. Ancak GUDFK olarak ölçülen finansal borçlar, finansal varlığın devrine ilişkin borçlar, finansal garanti sözleşmeleri ve piyasa altı faizli kredi taahhütleri gibi istisnalar vardır.",
  "TFRS 9 - finansal borçların ölçümü")

q("GUDFK olarak tanımlanan bir finansal borçta kredi riskindeki değişimin etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin kendi kredi riskindeki değişimden kaynaklanan kısım kural olarak diğer kapsamlı gelirde sunulur",
  ["Değişimin tamamı her hâlde kâr veya zarara yansıtılmak zorunda olan bir kalemi ifade eder",
   "Değişimin tamamı her hâlde doğrudan özkaynaktan indirilmek zorunda tutulmaktadır",
   "Bu değişim hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmak zorunda kalınır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: GUDFK olarak tanımlanan bir finansal borçta, borcun gerçeğe uygun değerindeki değişimin işletmenin KENDİ KREDİ RİSKİNDEKİ değişikliklerden kaynaklanan kısmı diğer kapsamlı gelirde, kalan kısmı kâr veya zararda sunulur (muhasebe uyumsuzluğu yaratmadıkça).",
  "TFRS 9 - kendi kredi riski")

nom, oran9, yil9 = 1_000_000, 10, 1
faiz9 = nom * oran9 / 100
q(f"Bir işletme, nominal değeri {tr(nom)} TL olan bir tahvili başabaş (nominal değerinden) satın almıştır. Tahvilin yıllık faiz oranı %{oran9} olup yılda bir kez faiz ödemesi yapılmaktadır. Tahvil itfa edilmiş maliyetle ölçülmektedir. İlk yılın faiz geliri kaç TL'dir?",
  f"{tr(faiz9)} TL",
  [f"{tr(nom)} TL", f"{tr(faiz9 * 2)} TL", f"{tr(faiz9 / 2)} TL", "0 TL"],
  f"Tahvil başabaş alındığından etkin faiz oranı nominal faiz oranına eşittir (%{oran9}). Faiz geliri = Brüt defter değeri × Etkin faiz oranı = {tr(nom)} × %{oran9} = {tr(faiz9)} TL. Etkin faiz yöntemiyle kâr veya zarara yansıtılır.",
  "TFRS 9 - faiz geliri hesabı")

gud_a, gud_b = 500_000, 560_000
kazanc9 = gud_b - gud_a
q(f"GUDFK olarak ölçülen bir hisse senedi yatırımının dönem başı gerçeğe uygun değeri {tr(gud_a)} TL, dönem sonu gerçeğe uygun değeri {tr(gud_b)} TL'dir. TFRS 9'a göre bu değişimin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  f"{tr(kazanc9)} TL kazanç kâr veya zarara yansıtılır",
  [f"{tr(kazanc9)} TL kazanç diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulmaktadır",
   f"{tr(kazanc9)} TL kazanç doğrudan özkaynakta değer artışı olarak biriktirilmek zorundadır",
   f"{tr(gud_b)} TL kazanç olarak kaydedilir; artış tutarı değil yeni değerin tamamı yazılmaktadır",
   "Hiçbir kayıt yapılmaz; değer artışı yalnızca dipnotlarda açıklanmakla yetinilmek durumundadır"],
  f"Kazanç = {tr(gud_b)} − {tr(gud_a)} = {tr(kazanc9)} TL. GUDFK olarak ölçülen bir finansal varlığın gerçeğe uygun değerindeki değişim, oluştuğu dönemde KÂR VEYA ZARARA yansıtılır. GUDDKG tercihi yapılsaydı diğer kapsamlı gelire giderdi.",
  "TFRS 9 - GUDFK değer artışı hesabı")

gud_c, gud_d = 700_000, 640_000
kayip9 = gud_c - gud_d
q(f"İlk muhasebeleştirmede geri dönülemez GUDDKG tercihi yapılmış, ticari amaçla elde tutulmayan bir hisse senedi yatırımının gerçeğe uygun değeri {tr(gud_c)} TL'den {tr(gud_d)} TL'ye düşmüştür. TFRS 9'a göre aşağıdakilerden hangisi doğrudur?",
  f"{tr(kayip9)} TL kayıp diğer kapsamlı gelirde muhasebeleştirilir",
  [f"{tr(kayip9)} TL kayıp kâr veya zarara yansıtılmak zorunda olan bir kalemi ifade etmektedir",
   f"{tr(kayip9)} TL kayıp varlığın maliyetinden indirilmek zorunda tutulan bir kalemi karşılar",
   f"{tr(gud_d)} TL kayıp olarak kaydedilir; azalış tutarı değil yeni değerin tamamı yazılmaktadır",
   "Hiçbir kayıt yapılmaz; değer azalışı yalnızca dipnotlarda açıklanmakla yetinilmek durumundadır"],
  f"Kayıp = {tr(gud_c)} − {tr(gud_d)} = {tr(kayip9)} TL. Ticari amaçla elde tutulmayan özkaynak aracı için geri dönülemez GUDDKG tercihi yapıldığından değer değişimi DİĞER KAPSAMLI GELİRDE muhasebeleştirilir ve satışta kâr veya zarara yeniden sınıflandırılmaz.",
  "TFRS 9 - özkaynak GUDDKG hesabı")

q("Aşağıdaki ifadelerden hangileri GUDDKG ölçümü bakımından doğrudur?\n\nI. Borçlanma aracında biriken tutar satışta kâr veya zarara yeniden sınıflandırılır\n\nII. Özkaynak aracında biriken tutar satışta kâr veya zarara yeniden sınıflandırılmaz\n\nIII. Özkaynak aracı için yapılan GUDDKG tercihi her dönem değiştirilebilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Borçlanma aracında biriken tutar satışta kâr/zarara yeniden sınıflandırılır (I); özkaynak aracında ise sınıflandırılmaz (II) — bu ikisinin ayrımı Standardın en kritik noktalarındandır. Özkaynak aracı için yapılan tercih ise İLK muhasebeleştirmede yapılır ve GERİ DÖNÜLEMEZ; bu nedenle III yanlıştır.",
  "TFRS 9 - GUDDKG ayrımı")

q("Aşağıdaki ifadelerden hangileri TFRS 9 bakımından doğrudur?\n\nI. Finansal varlıklar ilk olarak gerçeğe uygun değerle ölçülür\n\nII. GUDFK araçlarda işlem maliyetleri kâr veya zarara yansıtılır\n\nIII. GUDFK araçlarda işlem maliyetleri maliyete eklenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Finansal varlıklar ilk olarak gerçeğe uygun değerle ölçülür (I) ve GUDFK araçlarda işlem maliyetleri doğrudan kâr veya zarara yansıtılır (II). Maliyete EKLENMEZ; bu nedenle III yanlıştır (III, II ile çelişir).",
  "TFRS 9 - ilk ölçüm")

# ── C. Değer düşüklüğü (beklenen kredi zararı) (16) ────────────────────────
q("TFRS 9'un değer düşüklüğü modeli bakımından aşağıdakilerden hangisi doğrudur?",
  "Beklenen kredi zararı modelidir; zararın gerçekleşmesi beklenmeden karşılık ayrılır",
  ["Gerçekleşmiş zarar modelidir; zarar fiilen doğana kadar hiçbir karşılık ayrılmamaktadır",
   "Hiçbir değer düşüklüğü modeli öngörülmemiş olup karşılık ayrılması yasaklanmış bulunmaktadır",
   "Yalnızca vergi mevzuatındaki şüpheli alacak hükümleri uygulanmak zorunda tutulmaktadır",
   "Değer düşüklüğü modeli TFRS 9'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 9: BEKLENEN kredi zararı modeli uygulanır. Zararın gerçekleşmesini beklemeye gerek yoktur; ileriye dönük bilgi kullanılarak beklenen kredi zararları için karşılık ayrılır. Eski TMS 39'daki 'gerçekleşmiş zarar' modeli terk edilmiştir.",
  "TFRS 9 - beklenen kredi zararı modeli")

q("Beklenen kredi zararı bakımından aşağıdakilerden hangisi doğrudur?",
  "Kredi zararlarının ilgili temerrüt olasılıklarıyla ağırlıklandırılmış tahminidir",
  ["Fiilen gerçekleşmiş ve tahsil edilemeyeceği kesinleşmiş alacakları ifade eden bir kavramdır",
   "İşletmenin geçmiş yıllarda tahsil edemediği alacakların toplamını ifade eden bir kavramdır",
   "Vergi mevzuatına göre şüpheli sayılan alacakları ifade eden bir kavramı karşılamaktadır",
   "Beklenen kredi zararı TFRS 9'da tanımlanmamış bir husus niteliğinde bulunmak durumundadır"],
  "TFRS 9: beklenen kredi zararları, kredi zararlarının ilgili temerrüt olasılıklarıyla ağırlıklandırılarak belirlenen tahminidir. Olasılık ağırlıklı, paranın zaman değerini yansıtan ve makul/desteklenebilir bilgiyi kullanan tarafsız bir tutar olarak ölçülür.",
  "TFRS 9 - beklenen kredi zararı tanımı")

q("Beklenen kredi zararı ölçümünde dikkate alınacak unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Olasılık ağırlıklı tarafsız tutar, paranın zaman değeri ve geleceğe yönelik makul bilgi dikkate alınır",
  ["Yalnızca geçmiş dönemlerin fiilî zarar verileri dikkate alınmak zorunda tutulmaktadır",
   "Yalnızca en kötü senaryo dikkate alınarak en yüksek karşılık ayrılmak zorunda kalınmaktadır",
   "Yalnızca en iyi senaryo dikkate alınarak en düşük karşılık ayrılmak zorunda bulunmaktadır",
   "Bu unsurlar TFRS 9'da düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TFRS 9: beklenen kredi zararları; (a) bir dizi olası sonucun değerlendirilmesiyle belirlenen tarafsız ve olasılıklara göre ağırlıklandırılmış tutarı, (b) paranın zaman değerini ve (c) geçmiş olaylar, mevcut şartlar ve gelecekteki ekonomik koşul tahminlerine ilişkin makul ve desteklenebilir bilgiyi yansıtacak biçimde ölçülür.",
  "TFRS 9 - BKZ ölçüm unsurları")

q("Genel değer düşüklüğü yaklaşımındaki üç aşama bakımından aşağıdakilerden hangisi doğrudur?",
  "Kredi riskinde önemli artış olmayanlarda 12 aylık, önemli artış olanlarda ömür boyu beklenen kredi zararı ayrılır",
  ["Tüm finansal varlıklar için her hâlde ömür boyu beklenen kredi zararı ayrılmak zorundadır",
   "Tüm finansal varlıklar için her hâlde 12 aylık beklenen kredi zararı ayrılmak zorunda kalınır",
   "Aşamalı bir yaklaşım bulunmayıp hiçbir hâlde karşılık ayrılmamak zorunda tutulmaktadır",
   "Bu yaklaşım TFRS 9'da düzenlenmemiş bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TFRS 9: ilk muhasebeleştirmeden bu yana kredi riskinde ÖNEMLİ artış olmamışsa 12 aylık beklenen kredi zararı tutarında karşılık ayrılır. Kredi riskinde önemli artış olmuşsa ÖMÜR BOYU beklenen kredi zararı tutarında karşılık ayrılır.",
  "TFRS 9 - aşamalı yaklaşım")

q("12 aylık beklenen kredi zararı bakımından aşağıdakilerden hangisi doğrudur?",
  "Raporlama tarihinden sonraki 12 ay içinde gerçekleşebilecek temerrütlerden kaynaklanan ömür boyu zararların bir kısmıdır",
  ["Yalnızca gelecek 12 ayda tahsil edilemeyecek anaparanın tamamını ifade eden bir kavramdır",
   "Aracın tüm ömrü boyunca beklenen kredi zararlarının tamamını ifade eden bir kavram niteliğindedir",
   "Yalnızca geçmiş 12 ayda gerçekleşmiş zararları ifade eden bir kavramı karşılamak zorundadır",
   "Bu kavram TFRS 9'da tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TFRS 9: 12 aylık beklenen kredi zararları, raporlama tarihinden sonraki 12 ay içinde finansal araca ilişkin gerçekleşmesi mümkün temerrüt olaylarından kaynaklanan ömür boyu beklenen kredi zararlarının bir kısmıdır. 'Gelecek 12 ayda beklenen nakit açığı' DEĞİLDİR.",
  "TFRS 9 - 12 aylık BKZ")

q("Kredi riskinde önemli artışın değerlendirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İlk muhasebeleştirmedeki temerrüt riski ile raporlama tarihindeki temerrüt riski karşılaştırılır",
  ["Yalnızca raporlama tarihindeki mutlak temerrüt riski dikkate alınmak zorunda tutulmaktadır",
   "Yalnızca alacağın tutarı dikkate alınır; temerrüt riski hiç değerlendirilmemek durumundadır",
   "Kredi riskindeki değişim hiçbir hâlde değerlendirilmez; her hâlde aynı karşılık ayrılmaktadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: işletme her raporlama tarihinde, finansal araca ilişkin kredi riskinin ilk muhasebeleştirmeden bu yana önemli ölçüde artıp artmadığını değerlendirir. Bu değerlendirmede raporlama tarihindeki temerrüt riski ile İLK MUHASEBELEŞTİRME tarihindeki temerrüt riski karşılaştırılır.",
  "TFRS 9 - kredi riskinde önemli artış")

q("Ticari alacaklara ilişkin değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Basitleştirilmiş yaklaşım uygulanır; her zaman ömür boyu beklenen kredi zararı tutarında karşılık ayrılır",
  ["Ticari alacaklar için her hâlde 12 aylık beklenen kredi zararı ayrılmak zorunda tutulmaktadır",
   "Ticari alacaklar için hiçbir hâlde karşılık ayrılmaz; yalnızca dipnotta açıklanmaktadır",
   "Ticari alacaklar TFRS 9 kapsamı dışında olup hiçbir değer düşüklüğü hükmüne tabi değildir",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: önemli bir finansman bileşeni içermeyen ticari alacaklar için işletme, zarar karşılığını HER ZAMAN ömür boyu beklenen kredi zararlarına eşit tutarda ölçer (basitleştirilmiş yaklaşım). Kredi riskindeki değişimin izlenmesine gerek yoktur.",
  "TFRS 9 - ticari alacaklarda basitleştirilmiş yaklaşım")

q("Değer düşüklüğü hükümlerinin uygulanacağı finansal varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfa edilmiş maliyetle ve GUDDKG ile ölçülen borçlanma araçlarına uygulanır; GUDFK araçlara uygulanmaz",
  ["Tüm finansal varlıklara istisnasız uygulanmak zorunda olan hükümleri ifade etmek durumundadır",
   "Yalnızca GUDFK ile ölçülen varlıklara uygulanmak zorunda olan hükümleri karşılamaktadır",
   "Hiçbir finansal varlığa uygulanmayan ve yalnızca biçimsel olan hükümleri ifade etmektedir",
   "Bu husus TFRS 9'da düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TFRS 9: değer düşüklüğü hükümleri itfa edilmiş maliyetle ölçülen finansal varlıklara, GUDDKG ile ölçülen borçlanma araçlarına, kira alacaklarına, sözleşme varlıklarına ve belirli kredi taahhütleri ile finansal garantilere uygulanır. GUDFK ile ölçülenlere UYGULANMAZ; değer değişimi zaten kâr/zarara yansır.",
  "TFRS 9 - değer düşüklüğünün kapsamı")

q("GUDDKG ile ölçülen bir borçlanma aracının değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Zarar karşılığı kâr veya zarara yansıtılır; varlığın defter değeri azaltılmaz",
  ["Zarar karşılığı diğer kapsamlı gelirde muhasebeleştirilmek zorunda olan bir kalemi ifade eder",
   "GUDDKG araçlarda hiçbir hâlde değer düşüklüğü söz konusu olmamak zorunda bulunmaktadır",
   "Zarar karşılığı doğrudan özkaynaktan indirilmek zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: GUDDKG ile ölçülen borçlanma araçlarında zarar karşılığı kâr veya zararda muhasebeleştirilir; ancak finansal durum tablosundaki defter değeri zaten gerçeğe uygun değer olduğundan varlığın defter değeri AZALTILMAZ. Karşılık diğer kapsamlı gelirde muhasebeleştirilir.",
  "TFRS 9 - GUDDKG'de değer düşüklüğü")

alacak9, oran_bkz = 2_000_000, 3
bkz9 = alacak9 * oran_bkz / 100
q(f"Bir işletmenin önemli finansman bileşeni içermeyen ticari alacakları {tr(alacak9)} TL'dir. Geçmiş deneyim ve ileriye dönük beklentilere göre ömür boyu beklenen kredi zararı oranı %{oran_bkz} olarak tahmin edilmiştir. TFRS 9'a göre ayrılacak zarar karşılığı kaç TL'dir?",
  f"{tr(bkz9)} TL",
  [f"{tr(alacak9)} TL", f"{tr(bkz9 * 2)} TL", f"{tr(bkz9 / 2)} TL", "0 TL"],
  f"Önemli finansman bileşeni içermeyen ticari alacaklarda basitleştirilmiş yaklaşım uygulanır: her zaman ÖMÜR BOYU beklenen kredi zararı kadar karşılık ayrılır. Karşılık = {tr(alacak9)} × %{oran_bkz} = {tr(bkz9)} TL. 12 aylık BKZ hesaplanmaz.",
  "TFRS 9 - ticari alacakta BKZ hesabı")

tut_a, tem_ol, kayip_or = 1_000_000, 2, 40
bkz_b = tut_a * tem_ol / 100 * kayip_or / 100
q(f"Bir kredinin tutarı {tr(tut_a)} TL'dir. Temerrüt olasılığı %{tem_ol}, temerrüt hâlinde kayıp oranı %{kayip_or} olarak tahmin edilmektedir. Paranın zaman değeri ihmal edildiğinde beklenen kredi zararı kaç TL'dir?",
  f"{tr(bkz_b)} TL",
  [f"{tr(tut_a * tem_ol / 100)} TL", f"{tr(tut_a * kayip_or / 100)} TL", f"{tr(tut_a)} TL", "0 TL"],
  f"Beklenen kredi zararı, kredi zararlarının temerrüt olasılıklarıyla ağırlıklandırılmasıdır: Tutar × Temerrüt olasılığı × Temerrüt hâlinde kayıp oranı = {tr(tut_a)} × %{tem_ol} × %{kayip_or} = {tr(bkz_b)} TL. Yalnızca temerrüt olasılığı ya da yalnızca kayıp oranı uygulanması eksik hesaptır.",
  "TFRS 9 - BKZ olasılık hesabı")

q("Kredi değer düşüklüğüne uğramış finansal varlıkta faiz geliri bakımından aşağıdakilerden hangisi doğrudur?",
  "Etkin faiz oranı, brüt defter değerine değil itfa edilmiş maliyete (net defter değerine) uygulanır",
  ["Etkin faiz oranı her hâlde brüt defter değerine uygulanmak zorunda tutulan bir yöntemdir",
   "Değer düşüklüğüne uğramış varlıklarda hiçbir hâlde faiz geliri hesaplanmamak zorundadır",
   "Faiz geliri her hâlde nominal faiz oranıyla hesaplanmak zorunda olan bir kalemi ifade eder",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: bir finansal varlık sonradan kredi değer düşüklüğüne uğramışsa, işletme izleyen raporlama dönemlerinde faiz gelirini, etkin faiz oranını varlığın İTFA EDİLMİŞ MALİYETİNE (zarar karşılığı düşülmüş net tutara) uygulayarak hesaplar; brüt defter değerine değil.",
  "TFRS 9 - değer düşüklüğünde faiz geliri")

q("Bir işletme müşterilerinden olan ticari alacakları için zarar karşılığı ayırmaktadır ancak henüz hiçbir alacak vadesini geçirmemiştir. TFRS 9 bakımından aşağıdakilerden hangisi doğrudur?",
  "Vade geçmemiş olsa da beklenen kredi zararı için karşılık ayrılır",
  ["Vade geçmedikçe hiçbir hâlde karşılık ayrılamaz; zararın gerçekleşmesi beklenmek zorundadır",
   "Karşılık yalnızca alacağın tahsil edilemeyeceği kesinleştiğinde ayrılmak zorunda kalınmaktadır",
   "Ticari alacaklar için hiçbir hâlde karşılık ayrılmaz; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9 BEKLENEN kredi zararı modelini benimser: zararın gerçekleşmesini veya vadenin geçmesini beklemeye gerek yoktur. Önemli finansman bileşeni içermeyen ticari alacaklarda ilk muhasebeleştirmeden itibaren ömür boyu beklenen kredi zararı kadar karşılık ayrılır.",
  "TFRS 9 - beklenen zarar (senaryo)")

q("Aşağıdaki ifadelerden hangileri TFRS 9 değer düşüklüğü bakımından doğrudur?\n\nI. Beklenen kredi zararı modeli uygulanır\n\nII. Ticari alacaklarda basitleştirilmiş yaklaşımla ömür boyu BKZ ayrılır\n\nIII. GUDFK ile ölçülen varlıklara da değer düşüklüğü hükümleri uygulanır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Beklenen kredi zararı modeli uygulanır (I) ve önemli finansman bileşeni içermeyen ticari alacaklarda her zaman ömür boyu BKZ ayrılır (II). GUDFK ile ölçülen varlıklara değer düşüklüğü hükümleri UYGULANMAZ; değer değişimi zaten kâr veya zarara yansır. Bu nedenle III yanlıştır.",
  "TFRS 9 - değer düşüklüğü")

q("Aşağıdaki ifadelerden hangileri TFRS 9 bakımından doğrudur?\n\nI. Kredi riskinde önemli artış yoksa 12 aylık BKZ ayrılır\n\nII. Kredi riskinde önemli artış varsa ömür boyu BKZ ayrılır\n\nIII. Kredi riskindeki artış, raporlama tarihindeki mutlak riske bakılarak belirlenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kredi riskinde önemli artış yoksa 12 aylık (I), varsa ömür boyu BKZ ayrılır (II). Artış, raporlama tarihindeki MUTLAK riske değil, raporlama tarihindeki risk ile İLK MUHASEBELEŞTİRMEDEKİ riskin KARŞILAŞTIRILMASINA bakılarak belirlenir. Bu nedenle III yanlıştır.",
  "TFRS 9 - aşamalı yaklaşım")

# ── D. Finansal tablo dışı bırakma, riskten korunma, karma (14) ────────────
q("Finansal varlığın finansal tablo dışı bırakılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akışlarına ilişkin sözleşmeye bağlı haklar sona erdiğinde veya varlık devredildiğinde bilanço dışı bırakılır",
  ["Yalnızca varlığın vadesi geldiğinde bilanço dışı bırakılabilen bir kalemi ifade etmektedir",
   "Hiçbir hâlde bilanço dışı bırakılamaz; süresiz olarak kayıtlarda kalmak zorunda kalınmaktadır",
   "Yalnızca vergi idaresi izin verdiğinde bilanço dışı bırakılabilen bir kalemi karşılamaktadır",
   "Bu husus TFRS 9'da düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TFRS 9: işletme, (a) finansal varlıktan kaynaklanan nakit akışlarına ilişkin sözleşmeye bağlı haklarının süresi dolduğunda veya (b) finansal varlığı devrettiğinde ve devir işlemi bilanço dışı bırakma koşullarını sağladığında finansal varlığı bilanço dışı bırakır.",
  "TFRS 9 - finansal varlıkta bilanço dışı bırakma")

q("Devredilen finansal varlıkta risk ve getirilerin durumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Risk ve getirilerin tamamına yakını devredilmişse bilanço dışı bırakılır; elde tutulmuşsa bırakılmaz",
  ["Devir işlemi yapılması her hâlde bilanço dışı bırakma için yeterli olmak zorunda bulunmaktadır",
   "Risk ve getiriler hiçbir hâlde dikkate alınmaz; yalnızca hukuki devir yeterli sayılmaktadır",
   "Devredilen varlıklar hiçbir hâlde bilanço dışı bırakılamaz; her zaman kayıtlarda kalmaktadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: işletme, finansal varlığın mülkiyetinden kaynaklanan risk ve getirilerin tamamına yakınını devretmişse varlığı bilanço dışı bırakır. Risk ve getirilerin tamamına yakınını elinde tutuyorsa varlığı bilanço dışı bırakmaz; hukuki devir tek başına yeterli değildir.",
  "TFRS 9 - risk ve getirilerin devri")

q("Finansal borcun finansal tablo dışı bırakılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Yalnızca yükümlülük ortadan kalktığında, iptal edildiğinde veya süresi dolduğunda bilanço dışı bırakılır",
  ["Borç her hâlde vadesinde bilanço dışı bırakılmak zorunda olup ödeme aranmamak durumundadır",
   "Borç hiçbir hâlde bilanço dışı bırakılamaz; süresiz olarak kayıtlarda kalmak zorunda kalınır",
   "Borç işletmenin dilediği zaman bilanço dışı bırakılabilen bir kalemi ifade etmek durumundadır",
   "Bu husus TFRS 9'da düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TFRS 9: işletme, finansal borcu (veya bir kısmını) yalnızca ortadan kalktığında (yani sözleşmede belirtilen yükümlülük yerine getirildiğinde, iptal edildiğinde veya süresi dolduğunda) finansal durum tablosu dışı bırakır.",
  "TFRS 9 - finansal borçta bilanço dışı bırakma")

q("Finansal varlıkların yeniden sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Yalnızca iş modeli değiştiğinde yapılır; bu durum çok nadirdir ve ileriye dönük uygulanır",
  ["İşletme her dönem serbestçe ve gerekçesiz olarak yeniden sınıflandırma yapabilmek zorundadır",
   "Yeniden sınıflandırma hiçbir hâlde yapılamaz; ilk sınıflandırma kalıcı olmak zorunda kalınır",
   "Yeniden sınıflandırma her hâlde geriye dönük olarak uygulanmak zorunda tutulmaktadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: işletme yalnızca finansal varlıkların yönetimine ilişkin İŞ MODELİNİ değiştirdiğinde etkilenen tüm finansal varlıkları yeniden sınıflandırır. Bu değişikliklerin çok nadir olması beklenir ve yeniden sınıflandırma İLERİYE dönük uygulanır. Finansal BORÇLAR yeniden sınıflandırılmaz.",
  "TFRS 9 - yeniden sınıflandırma")

q("Finansal borçların yeniden sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal borçlar yeniden sınıflandırılmaz",
  ["Finansal borçlar her dönem serbestçe yeniden sınıflandırılabilmek zorunda bulunmaktadır",
   "Finansal borçlar iş modeli değiştiğinde yeniden sınıflandırılmak zorunda tutulmaktadır",
   "Finansal borçlar her hâlde her raporlama döneminde yeniden sınıflandırılmak zorundadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TFRS 9: işletme hiçbir finansal borcu yeniden sınıflandırmaz. Yeniden sınıflandırma yalnızca finansal VARLIKLAR için ve yalnızca iş modeli değiştiğinde söz konusudur.",
  "TFRS 9 - borçlarda yeniden sınıflandırma yasağı")

q("Riskten korunma muhasebesinin uygulanması bakımından aşağıdakilerden hangisi doğrudur?",
  "İsteğe bağlıdır; koşullar sağlanırsa uygulanabilir",
  ["Her hâlde ve istisnasız zorunlu olup uygulanmaması mümkün olmamak durumundadır",
   "Hiçbir hâlde uygulanamaz; TFRS 9 riskten korunma muhasebesini kaldırmış bulunmaktadır",
   "Yalnızca vergi idaresi izin verdiğinde uygulanabilmek zorunda olan bir yöntemi ifade eder",
   "Bu husus TFRS 9'da düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TFRS 9: riskten korunma muhasebesinin uygulanması işletmenin tercihine bağlıdır (isteğe bağlı). Ancak uygulanabilmesi için uygunluk koşullarının (uygun korunma aracı ve konusu, resmî belgelendirme, ekonomik ilişki gibi) sağlanması gerekir.",
  "TFRS 9 - riskten korunma muhasebesi")

q("Riskten korunma muhasebesinin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr veya zararı etkileyen risk yönetimi faaliyetlerinin etkisini finansal tablolara yansıtmaktır",
  ["İşletmenin ödeyeceği vergiyi azaltmayı amaçlayan bir yöntem niteliğinde bulunmaktadır",
   "İşletmenin kârını olduğundan yüksek göstermeyi amaçlayan bir yöntemi ifade etmek durumundadır",
   "İşletmenin tüm risklerini ortadan kaldırmayı amaçlayan bir yöntemi karşılamak zorundadır",
   "Riskten korunma muhasebesinin belirlenmiş bir amacı bulunmamak durumunda kalınmaktadır"],
  "TFRS 9: riskten korunma muhasebesinin amacı, kâr veya zararı etkileyebilecek belirli riskleri yönetmek için finansal araçları kullanan işletmenin risk yönetimi faaliyetlerinin etkisini finansal tablolara yansıtmaktır.",
  "TFRS 9 - riskten korunmanın amacı")

q("Riskten korunma türleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değer riskinden korunma, nakit akış riskinden korunma ve yurtdışı işletmedeki net yatırım riskinden korunma vardır",
  ["Yalnızca tek bir riskten korunma türü bulunmakta olup ayrım yapılmamak zorunda kalınmaktadır",
   "Yalnızca nakit akış riskinden korunma bulunmakta olup diğer türler kabul edilmemektedir",
   "Yalnızca gerçeğe uygun değer riskinden korunma bulunmakta olup diğerleri yasaklanmıştır",
   "Riskten korunma türleri TFRS 9'da düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TFRS 9 üç riskten korunma ilişkisi türü öngörür: gerçeğe uygun değer riskinden korunma, nakit akış riskinden korunma ve yurtdışındaki işletmede bulunan net yatırım riskinden korunma.",
  "TFRS 9 - riskten korunma türleri")

q("TFRS 9'un TMS 39'a göre getirdiği temel değişiklikler bakımından aşağıdakilerden hangisi doğrudur?",
  "Sınıflandırma iş modeli temelli oldu ve gerçekleşmiş zarar yerine beklenen kredi zararı modeli geldi",
  ["Hiçbir değişiklik getirmemiş olup TMS 39'un aynen tekrarı niteliğinde bulunmak durumundadır",
   "Yalnızca finansal borçların ölçümünü değiştirmiş olup varlıklara hiç dokunmamış bulunmaktadır",
   "Yalnızca dipnot açıklamalarını değiştirmiş olup ölçüm esaslarına hiç dokunmamış bulunmaktadır",
   "TFRS 9 ile TMS 39 arasındaki ilişki hiçbir düzenlemede ele alınmamış bulunmak durumundadır"],
  "TFRS 9'un temel yenilikleri: (a) niyet temelli sınıflandırma yerine İŞ MODELİ + nakit akışı özellikleri temelli üç sınıf, (b) gerçekleşmiş zarar yerine BEKLENEN kredi zararı modeli ve (c) risk yönetimiyle daha uyumlu riskten korunma muhasebesi.",
  "TFRS 9 - TMS 39'dan farkı")

q("Bir işletme, sözleşmeye bağlı nakit akışlarını tahsil etmek amacıyla elde tuttuğu ve nakit akışları yalnızca anapara ile faizden oluşan bir tahvile sahiptir. TFRS 9 bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfa edilmiş maliyetle ölçülür",
  ["Her hâlde gerçeğe uygun değer farkı kâr veya zarara yansıtılarak ölçülmek zorunda kalınmaktadır",
   "Her hâlde gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak ölçülmek zorundadır",
   "Her hâlde maliyet bedeliyle ölçülmek zorunda olup hiçbir hâlde itfa uygulanmamaktadır",
   "Bu tahvil hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorunda kalınır"],
  "TFRS 9: iki koşul da sağlanmıştır — (a) iş modeli sözleşmeye bağlı nakit akışlarının tahsilini amaçlıyor ve (b) nakit akışları sadece anapara ve faiz ödemelerinden oluşuyor. Bu durumda finansal varlık İTFA EDİLMİŞ MALİYETİNDEN ölçülür.",
  "TFRS 9 - itfa edilmiş maliyet (senaryo)")

q("Bir işletme, kısa vadede satarak kâr elde etmek amacıyla hisse senedi almıştır. TFRS 9 bakımından aşağıdakilerden hangisi doğrudur?",
  "Ticari amaçla elde tutulduğundan GUDFK ile ölçülür; GUDDKG tercihi yapılamaz",
  ["Her hâlde itfa edilmiş maliyetle ölçülmek zorunda olan bir yatırımı ifade etmek durumundadır",
   "Her hâlde GUDDKG tercihi yapılarak ölçülmek zorunda olan bir yatırımı karşılamaktadır",
   "Her hâlde maliyet bedeliyle ölçülmek zorunda olup değer değişimi hiç kaydedilmemektedir",
   "Bu yatırım hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorunda kalınır"],
  "TFRS 9: özkaynak araçları kural olarak GUDFK ile ölçülür. Geri dönülemez GUDDKG tercihi yalnızca TİCARİ AMAÇLA ELDE TUTULMAYAN özkaynak araçları için yapılabilir. Kısa vadede satıp kâr elde etmek amacıyla alınan hisse senedi ticari amaçlıdır; tercih yapılamaz.",
  "TFRS 9 - ticari amaçlı özkaynak (senaryo)")

q("Aşağıdaki ifadelerden hangileri TFRS 9 bakımından doğrudur?\n\nI. Finansal varlıklar yalnızca iş modeli değiştiğinde yeniden sınıflandırılır\n\nII. Finansal borçlar yeniden sınıflandırılmaz\n\nIII. Yeniden sınıflandırma geriye dönük uygulanır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Finansal varlıklar yalnızca iş modeli değiştiğinde yeniden sınıflandırılır (I) ve finansal borçlar hiç yeniden sınıflandırılmaz (II). Yeniden sınıflandırma İLERİYE dönük uygulanır, geriye dönük değil; bu nedenle III yanlıştır.",
  "TFRS 9 - yeniden sınıflandırma")

q("Aşağıdakilerden hangileri TFRS 9'a göre finansal varlığın bilanço dışı bırakılma hâllerindendir?\n\nI. Nakit akışlarına ilişkin sözleşmeye bağlı hakların süresinin dolması\n\nII. Varlığın devredilmesi ve risk ile getirilerin tamamına yakınının devredilmesi\n\nIII. Varlığın hukuken devredilmesi ancak risk ve getirilerin tamamına yakınının elde tutulması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sözleşmeye bağlı hakların süresinin dolması (I) ve risk ile getirilerin tamamına yakınının devredildiği bir devir (II) bilanço dışı bırakmayı gerektirir. Risk ve getiriler ELDE TUTULUYORSA (III) hukuki devre rağmen varlık bilanço dışı BIRAKILMAZ; bu nedenle yanlıştır.",
  "TFRS 9 - bilanço dışı bırakma")

q("Bir işletme, alacaklarını bir faktoring şirketine devretmiş ancak tahsil edilememe riskini tümüyle üzerinde tutmayı sürdürmektedir. TFRS 9 bakımından aşağıdakilerden hangisi doğrudur?",
  "Risk ve getiriler elde tutulduğundan alacaklar bilanço dışı bırakılmaz",
  ["Hukuki devir yapıldığından alacaklar her hâlde bilanço dışı bırakılmak zorunda tutulmaktadır",
   "Alacaklar her hâlde gerçeğe uygun değerle yeniden ölçülmek zorunda olan kalemleri ifade eder",
   "Alacaklar her hâlde derhâl gider yazılmak zorunda olan bir kalemi karşılamak durumundadır",
   "Bu husus TFRS 9'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TFRS 9: bilanço dışı bırakmada belirleyici olan hukuki devir değil, mülkiyetten kaynaklanan RİSK VE GETİRİLERİN devredilip devredilmediğidir. İşletme tahsil edilememe riskini tümüyle üzerinde tutuyorsa risk ve getirilerin tamamına yakınını elinde tutuyor demektir; alacaklar bilanço dışı bırakılmaz ve alınan tutar finansal borç olarak kaydedilir.",
  "TFRS 9 - kabilirücu faktoring (senaryo)")

q("Bir işletme, tahvil portföyünü hem faiz tahsil etmek hem uygun fiyat oluştuğunda satmak amacıyla elde tutmakta olup nakit akışları yalnızca anapara ve faizden oluşmaktadır. TFRS 9 bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak ölçülür",
  ["Her hâlde itfa edilmiş maliyetle ölçülmek zorunda olan bir portföyü ifade etmek durumundadır",
   "Her hâlde gerçeğe uygun değer farkı kâr veya zarara yansıtılarak ölçülmek zorunda kalınmaktadır",
   "Her hâlde maliyet bedeliyle ölçülmek zorunda olup değer değişimi hiç kaydedilmemektedir",
   "Bu portföy hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotta açıklanmak zorunda kalınır"],
  "TFRS 9: iş modeli hem sözleşmeye bağlı nakit akışlarının tahsilini HEM satışı amaçlıyorsa ve nakit akışları yalnızca anapara ve faiz ödemelerinden oluşuyorsa, finansal varlık gerçeğe uygun değer farkı DİĞER KAPSAMLI GELİRE yansıtılarak ölçülür. Yalnız tahsil amaçlı olsaydı itfa edilmiş maliyet olurdu.",
  "TFRS 9 - GUDDKG iş modeli (senaryo)")

q("Finansal araçlara ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Açıklama hükümleri TFRS 7'de düzenlenmiştir",
  ["Açıklama hükümleri TFRS 9'da düzenlenmiş olup başka bir standarda başvurulmamaktadır",
   "Finansal araçlar hakkında hiçbir açıklama yapılmasına gerek bulunmamak durumundadır",
   "Açıklamalar yalnızca vergi idaresine yapılır; kullanıcılara bilgi verilmemek zorundadır",
   "Bu husus hiçbir standartta düzenlenmemiş olup uygulamada serbest bırakılmış bulunmaktadır"],
  "TFRS 9 muhasebeleştirme ve ölçümü düzenler; finansal araçlara ilişkin AÇIKLAMA hükümleri TFRS 7 Finansal Araçlar: Açıklamalar Standardında yer alır. Sunum hükümleri ise TMS 32'dedir.",
  "TFRS 9 - açıklamaların yeri")

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
                       "styleRef": "SGS Muhasebe Standartları (TFRS 9; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
