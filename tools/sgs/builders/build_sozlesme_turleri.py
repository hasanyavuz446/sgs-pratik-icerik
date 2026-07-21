# -*- coding: utf-8 -*-
"""SGS — Borçlar Hukuku / Sözleşme Türleri (TBK isimli sözleşmeler) — 60 soru.

Baba isteği (2026-07-18): "Borçlar hukuku sözleşme türleri".
Kaynak: 6098 sayılı TBK özel hükümler. SGS seviyesi: tanım, tarafların borçları,
sona erme, temel ayrımlar. ÖZGÜN — kitap/TESMER metni kopyalanmaz.

★ Şık örüntüsü temiz yazılır (bu oturumun dersi): doğru şık çeldiricilerle AYNI
register/boyda, kısa ve iddialı; dolgu ("…zorunda bulunmaktadır") YOK; doğru şık
sistematik olarak en uzun/en kısa değil; harf gen_letters ile dengeli.
"""
import json
import random
import re

DERS, KONU = "borclar_hukuku", "sozlesme_turleri"
PREFIX, SEED = "sozturu-gen", 20260718
OUT_APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/borclar_hukuku/sozlesme_turleri.json"
OUT_CONTENT = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/borclar_hukuku/sozlesme_turleri.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

# ── A. Genel tasnif ve kavramlar (10) ───────────────────────────────────────
q("Kanunda düzenlenip ad verilmiş sözleşmeler bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanunda ayrı bir ad altında düzenlenen bu sözleşmelere isimli (tipik) sözleşme denir",
  ["Kanunda ad verilmiş sözleşmelere isimsiz sözleşme denir ve bunlara genel hükümler uygulanmaz",
   "İsimli sözleşmelerin geçerliliği her hâlde resmî şekilde yapılmalarına bağlıdır",
   "Bir sözleşmenin isimli sayılması için mutlaka iki tarafa da borç yüklemesi gerekir",
   "İsimli sözleşmeler yalnızca tacirler arasında kurulabilen sözleşmelerdir"],
  "TBK özel hükümlerinde ad altında düzenlenen sözleşmeler isimli (tipik) sözleşmelerdir; satış, kira, vekâlet gibi.",
  "TBK - isimli sözleşme"),

q("Tam iki tarafa borç yükleyen sözleşme bakımından aşağıdakilerden hangisi doğrudur?",
  "Her iki tarafın da karşılıklı ve birbirine bağlı biçimde asli edim borcu altına girdiği sözleşmedir",
  ["Yalnızca taraflardan birinin borç altına girdiği, diğerinin hiçbir edim yükümü bulunmadığı sözleşmedir",
   "Tarafların borçlarının birbirinden tamamen bağımsız olduğu ve karşılıklılık taşımayan sözleşmedir",
   "Her iki tarafın da aynı yönde edim taahhüt ettiği ve karşı edim bulunmayan sözleşmedir",
   "Ancak bir tarafın ölümüyle sona erebilen ve devredilemeyen kişisel sözleşmedir"],
  "Satış, kira gibi sözleşmelerde iki taraf da karşılıklı asli edim borcu altına girer; buna tam iki tarafa borç yükleyen sözleşme denir.",
  "TBK - iki tarafa borç yükleyen sözleşme"),

q("İvazsız (karşılıksız) sözleşme bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir tarafın karşılık beklemeksizin diğerine bir kazandırmada bulunduğu sözleşmedir",
  ["Her iki tarafın da birbirine eşdeğer edimler taahhüt ettiği sözleşmedir",
   "Bir tarafın edimine karşılık diğer tarafın para ödemeyi üstlendiği sözleşmedir",
   "Yalnızca ticari işletmeler arasında bedelsiz yapılabilen sözleşmedir",
   "Karşılık içermediği için hukuken hiçbir sonuç doğurmayan sözleşmedir"],
  "Bağışlama, kullanım ödüncü gibi bir tarafın karşılık beklemeden kazandırmada bulunduğu sözleşmeler ivazsızdır.",
  "TBK - ivazsız sözleşme"),

q("Rızai (yalnız anlaşmayla kurulan) sözleşme bakımından aşağıdakilerden hangisi doğrudur?",
  "Tarafların karşılıklı ve birbirine uygun irade açıklamalarıyla kurulan sözleşmedir",
  ["Kurulması için anlaşmanın yanında malın teslimini de zorunlu kılan sözleşmedir",
   "Yalnızca resmî memur önünde yapıldığında kurulmuş sayılan sözleşmedir",
   "Tarafların iradesine bakılmaksızın kanun gereği kendiliğinden kurulan sözleşmedir",
   "Kurulması tek taraflı bir irade açıklamasına bağlı olan sözleşmedir"],
  "Satış, kira gibi sözleşmeler yalnız tarafların uygun iradeleriyle kurulur; bunlara rızai sözleşme denir.",
  "TBK m.1 - sözleşmenin kurulması"),

q("Sürekli edimli sözleşme bakımından aşağıdakilerden hangisi doğrudur?",
  "Edimin belirli bir zaman dilimine yayıldığı ve bu süre boyunca yerine getirildiği sözleşmedir",
  ["Edimin tek bir anda, bir defada yerine getirilerek tükendiği sözleşmedir",
   "Hiçbir edim içermeyen, yalnızca bir hakkı sona erdiren sözleşmedir",
   "Yalnızca peşin bedel karşılığında kurulabilen sözleşmedir",
   "Edimi hiçbir koşulda bölünemeyen ve devredilemeyen sözleşmedir"],
  "Kira, hizmet gibi edimin zamana yayıldığı sözleşmeler sürekli edimlidir; sona ermeleri kural olarak ileriye etkilidir.",
  "TBK - sürekli edimli sözleşme"),

q("Satış sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Satıcının malın zilyetlik ve mülkiyetini geçirme, alıcının bedeli ödeme borcu altına girdiği sözleşmedir",
  ["Satıcının yalnızca malı kullandırma, alıcının kira ödeme borcu altına girdiği sözleşmedir",
   "Malın mülkiyeti geçirilmeksizin yalnızca kullanımının bırakıldığı sözleşmedir",
   "Karşılıksız olarak bir malın mülkiyetinin devredildiği sözleşmedir",
   "Bir işin görülmesi karşılığında ücret ödenmesini konu alan sözleşmedir"],
  "TBK m.207: satış, satıcının malın mülkiyet ve zilyetliğini geçirme, alıcının ise bedeli ödeme borcunu doğuran sözleşmedir.",
  "TBK m.207 - satış sözleşmesi"),

q("Kira sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya verenin bir şeyin kullanılmasını bırakmayı, kiracının kira bedeli ödemeyi üstlendiği sözleşmedir",
  ["Kiraya verenin malın mülkiyetini kiracıya devretmeyi üstlendiği sözleşmedir",
   "Kiracının hiçbir bedel ödemeksizin malı kullanmasına izin verilen sözleşmedir",
   "Bir eserin meydana getirilmesi karşılığında bedel ödenen sözleşmedir",
   "Bir malın tüketilmek üzere karşılıksız verildiği sözleşmedir"],
  "TBK m.299: kirada kiraya veren bir şeyin kullanılmasını bırakır, kiracı da kira bedeli ödemeyi üstlenir; mülkiyet geçmez.",
  "TBK m.299 - kira sözleşmesi"),

q("Sözleşme özgürlüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Taraflar kanunda düzenlenmeyen türde bir sözleşmeyi de hukuka ve ahlaka aykırı olmamak kaydıyla yapabilir",
  ["Taraflar yalnızca kanunda ad verilmiş sözleşme tiplerinden birini seçmek zorundadır",
   "Sözleşmenin içeriği her hâlde kamu makamının önceden onayına bağlıdır",
   "Sözleşme özgürlüğü yalnızca kamu tüzel kişilerine tanınmış bir yetkidir",
   "Taraflar kanunun emredici hükümlerine aykırı sözleşmeleri de serbestçe yapabilir"],
  "Sözleşme özgürlüğü; taraflara tip serbestisi tanır, ancak emredici hükümlere, ahlaka ve kamu düzenine aykırılık sınırdır.",
  "TBK m.26-27 - sözleşme özgürlüğü ve sınırları"),


q("Bir sözleşmenin ivazlı mı ivazsız mı olduğunun belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir tarafın kazandırması karşılığında diğer taraftan bir karşı edim alıp almadığına bakılır",
  ["Sözleşmenin yazılı olup olmadığına bakılarak belirlenir",
   "Tarafların tacir sıfatını taşıyıp taşımadığına bakılarak belirlenir",
   "Sözleşmenin süreli mi süresiz mi olduğuna bakılarak belirlenir",
   "Sözleşmenin resmî şekle tabi olup olmadığına bakılarak belirlenir"],
  "İvazlılık ölçütü karşı edimdir: bir kazandırmaya karşılık edim varsa ivazlı (satış), yoksa ivazsızdır (bağışlama).",
  "TBK - ivazlı/ivazsız ayrımı"),

# ── B. Satış sözleşmesi (10) ─────────────────────────────────────────────────
q("Satışta yarar ve hasarın geçmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Taşınır satışında yarar ve hasar, kural olarak zilyetliğin devriyle (teslimle) alıcıya geçer",
  ["Yarar ve hasar, sözleşmenin kurulduğu anda kendiliğinden alıcıya geçer",
   "Yarar ve hasar, bedelin tamamı ödenmedikçe hiçbir hâlde alıcıya geçmez",
   "Yarar ve hasar, malın satıcıda kaldığı sürece dahi her hâlde alıcıya aittir",
   "Yarar ve hasar yalnızca tapuda tescil ile taşınırlarda da alıcıya geçer"],
  "TBK m.208: taşınır satışında yarar ve hasar, kural olarak zilyetliğin devriyle alıcıya geçer (eski sistemdeki sözleşme anı kuralı terk edilmiştir).",
  "TBK m.208 - yarar ve hasarın geçmesi"),

q("Satıcının ayıba karşı tekeffül (ayıptan sorumluluk) borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Satıcı, satılanın kendisine yüklenen nitelikleri taşımamasından veya değerini azaltan ayıplardan sorumludur",
  ["Satıcı yalnızca satılanın hiç teslim edilememesinden sorumlu olup ayıplardan sorumlu değildir",
   "Satıcının ayıptan sorumluluğu her durumda tarafların ayrıca kararlaştırmasına bağlıdır",
   "Ayıba karşı tekeffül yalnızca taşınmaz satışlarında söz konusu olabilir",
   "Satıcı, alıcının satış sırasında bildiği ayıplardan da her hâlde sorumludur"],
  "TBK m.219: satıcı, satılanın bildirdiği nitelikleri taşımamasından ve değerini/yararını ortadan kaldıran ya da azaltan ayıplardan sorumludur.",
  "TBK m.219 - ayıptan sorumluluk"),

q("Alıcının satılanı gözden geçirme ve ayıbı bildirme yükümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Alıcı, işlerin olağan akışına göre imkân bulur bulmaz satılanı gözden geçirip ayıpları satıcıya bildirmelidir",
  ["Alıcının satılanı gözden geçirme veya ayıbı bildirme gibi bir yükümü hiçbir hâlde bulunmaz",
   "Ayıp bildirimi yalnızca satıştan bir yıl sonra yapılabilir; daha önce yapılan bildirim geçersizdir",
   "Alıcı ayıbı bildirmese dahi satıcının sorumluluğu her hâlde aynen devam eder",
   "Ayıp bildirimi yalnızca noter aracılığıyla yapıldığında sonuç doğurur"],
  "TBK m.223: alıcı, teslim aldığı satılanı imkân bulunca gözden geçirmek ve ayıbı uygun süre içinde satıcıya bildirmekle yükümlüdür; aksi hâlde satılanı kabul etmiş sayılır.",
  "TBK m.223 - gözden geçirme ve bildirim"),

q("Satılanın zapt edilmesi (zapttan sorumluluk) bakımından aşağıdakilerden hangisi doğrudur?",
  "Satıcı, üçüncü kişinin sözleşme öncesine dayanan üstün hakkı nedeniyle satılanın alıcıdan alınmasından sorumludur",
  ["Satıcı, satıştan sonra doğan haklara dayanan zapttan da her hâlde sorumludur",
   "Zapttan sorumluluk yalnızca satıcının kötü niyetli olduğu hâllerde doğar",
   "Satıcının zapttan sorumluluğu yalnızca taşınır mallarda söz konusu olabilir",
   "Zapt hâlinde alıcı hiçbir talepte bulunamaz; satış aynen geçerli kalır"],
  "TBK m.214 vd.: satıcı, üçüncü kişinin satıştan önceki bir sebebe dayanan hakkı yüzünden satılanın alıcının elinden alınmasından (zapttan) sorumludur.",
  "TBK m.214 - zapttan sorumluluk"),

q("Satıcının asli borçları bakımından aşağıdakilerden hangisi doğrudur?",
  "Satıcı, satılanı ayıptan ari olarak teslim etmek ve mülkiyeti alıcıya geçirmekle yükümlüdür",
  ["Satıcı yalnızca bedeli tahsil etmekle yükümlü olup malı teslim borcu yoktur",
   "Satıcı malı teslim etse de mülkiyeti kendi üzerinde tutmakla yükümlüdür",
   "Satıcının tek borcu, alıcının bulunduğu yere kadar malı taşımaktır",
   "Satıcı malı ancak alıcı bedelin iki katını depozito olarak yatırınca teslim eder"],
  "TBK m.207/m.211: satıcının asli borçları satılanı teslim ve mülkiyeti geçirmedir; teslim ayıptan ari olmalıdır.",
  "TBK m.211 - satıcının borçları"),

q("Alıcının borçları bakımından aşağıdakilerden hangisi doğrudur?",
  "Alıcı, kararlaştırılan bedeli ödemek ve satılanı teslim almakla yükümlüdür",
  ["Alıcının tek borcu, satılanı kusursuz biçimde muhafaza etmektir; bedel ödeme borcu yoktur",
   "Alıcı, bedeli yalnızca satıcının onayıyla ödeyebilir; kendiliğinden ödeyemez",
   "Alıcı satılanı teslim almak zorunda değildir; teslim almaması hiçbir sonuç doğurmaz",
   "Alıcının bedel ödeme borcu yalnızca taşınmaz satışlarında doğar"],
  "TBK m.232: alıcı, sözleşmede kararlaştırılan bedeli ödemek ve satılanı teslim almakla yükümlüdür.",
  "TBK m.232 - alıcının borçları"),



q("Taksitle satış sözleşmesinin şekli bakımından aşağıdakilerden hangisi doğrudur?",
  "Taksitle satış sözleşmesi, geçerliliği kanunda öngörülen şekil koşullarına bağlı tutulan bir satış türüdür",
  ["Taksitle satış hiçbir şekil koşuluna tabi olmayıp yalnızca sözlü anlaşmayla geçerli olur",
   "Taksitle satış yalnızca taşınmazlarda yapılabilen bir satış türüdür",
   "Taksitle satışta mülkiyet her hâlde son taksitin ödenmesiyle satıcıya geçer",
   "Taksitle satışta alıcının cayma hakkı hiçbir koşulda bulunmaz"],
  "TBK m.253 vd.: taksitle satış, tüketiciyi koruyan şekil ve içerik koşullarına bağlanmıştır; yazılılık ve zorunlu kayıtlar aranır.",
  "TBK m.253 - taksitle satışın şekli"),

q("Satışta bedelin belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bedel, sözleşmede açıkça belirlenebileceği gibi belirlenmesini sağlayacak esaslar da gösterilerek kararlaştırılabilir",
  ["Bedelin sözleşmede rakamla belirtilmemesi hâlinde satış her durumda geçersizdir",
   "Bedel yalnızca satıcının satıştan sonra tek taraflı takdiriyle belirlenebilir",
   "Satış bedeli hiçbir hâlde piyasa rayicine göre belirlenemez",
   "Bedel yalnızca yabancı para cinsinden kararlaştırıldığında geçerli olur"],
  "TBK m.233: bedel, sözleşmede belirlenmemiş ama belirlenebilir kılınmışsa satış geçerlidir; koşullara göre rayiç bedel esas alınabilir.",
  "TBK m.233 - bedelin belirlenmesi"),

# ── C. Bağışlama (6) ─────────────────────────────────────────────────────────
q("Bağışlama sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bağışlayanın sağlararası bir işlemle malvarlığından bağışlanana karşılıksız kazandırma yaptığı sözleşmedir",
  ["Bağışlananın, aldığı mal karşılığında bağışlayana bedel ödediği sözleşmedir",
   "Bağışlayanın malının kullanımını geçici olarak bıraktığı sözleşmedir",
   "Yalnızca ölüme bağlı olarak sonuç doğuran ve mirasa ilişkin bir işlemdir",
   "İki tarafın da birbirine eşdeğer edim taahhüt ettiği sözleşmedir"],
  "TBK m.285: bağışlama, bağışlayanın sağlararası sonuç doğurmak üzere malvarlığından bağışlanana karşılıksız kazandırma yapmasıdır.",
  "TBK m.285 - bağışlama"),

q("Bağışlama sözünün (bağışlama taahhüdünün) şekli bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir şeyi bağışlama sözü vermenin geçerliliği yazılı şekilde yapılmasına bağlıdır",
  ["Bağışlama sözü verme hiçbir şekil koşuluna tabi olmayıp sözlü de geçerlidir",
   "Bağışlama sözü yalnızca resmî senetle verildiğinde geçerlilik kazanır",
   "Elden bağışlamada dahi ayrıca yazılı bir taahhütname düzenlenmesi şarttır",
   "Bağışlama sözünün geçerliliği bağışlananın da yazılı kabulüne bağlıdır"],
  "TBK m.288: bağışlama sözü vermenin (taahhüdünün) geçerliliği yazılı şekle bağlıdır; taşınmaz bağışı sözü ise resmî şekle tabidir.",
  "TBK m.288 - bağışlama sözünün şekli"),

q("Elden bağışlama bakımından aşağıdakilerden hangisi doğrudur?",
  "Bağışlayanın bir taşınırı bağışlanana teslim etmesiyle kurulan ve şekle bağlı olmayan bağışlamadır",
  ["Elden bağışlama yalnızca resmî senetle yapıldığında geçerli olur",
   "Elden bağışlama yalnızca taşınmazların devrinde söz konusu olabilir",
   "Elden bağışlamada teslim aranmaz; yalnızca sözlü anlaşma yeterlidir",
   "Elden bağışlama her hâlde bağışlayanın mirasçılarının onayına bağlıdır"],
  "TBK m.289: elden bağışlama, taşınırın zilyetliğinin bağışlanana geçirilmesiyle kurulur ve herhangi bir şekle bağlı değildir.",
  "TBK m.289 - elden bağışlama"),

q("Bağışlamadan dönme bakımından aşağıdakilerden hangisi doğrudur?",
  "Bağışlanan, bağışlayana veya yakınlarına karşı ağır bir suç işlerse bağışlayan bağışlamadan dönebilir",
  ["Bağışlayan hiçbir sebep göstermeksizin her zaman bağışlamadan dönebilir",
   "Bağışlamadan dönme yalnızca bağışlananın ölümü hâlinde mümkündür",
   "Yerine getirilmiş bir bağışlamadan hiçbir koşulda dönülemez",
   "Bağışlamadan dönme kararı yalnızca bağışlananın onayıyla sonuç doğurur"],
  "TBK m.295: bağışlanan, bağışlayana veya yakınlarına karşı ağır suç işlemek gibi hâllerde bağışlayan yerine getirilmiş bağışlamayı geri isteyebilir.",
  "TBK m.295 - bağışlamadan dönme"),


q("Bağışlayanın sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Bağışlama ivazsız olduğundan bağışlayan yalnızca ağır kusurundan sorumlu tutulur",
  ["Bağışlayan, satıcı gibi ayıba ve zapta karşı tam olarak sorumludur",
   "Bağışlayan bağışladığı malın her türlü ayıbından kusursuz olarak sorumludur",
   "Bağışlayanın hiçbir hâlde herhangi bir sorumluluğu doğmaz",
   "Bağışlayanın sorumluluğu bağışlananın tacir olup olmamasına göre belirlenir"],
  "TBK m.294: bağışlama karşılıksız olduğundan, bağışlayan bağışlanana verdiği zararlardan ancak ağır kusuru hâlinde sorumlu olur.",
  "TBK m.294 - bağışlayanın sorumluluğu"),

# ── D. Kira (8) ──────────────────────────────────────────────────────────────
q("Konut ve çatılı işyeri kiralarında sözleşmenin kiracı tarafından sona erdirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiracı, belirli süreli sözleşmede sürenin bitiminden en az on beş gün önce bildirimde bulunarak sözleşmeyi sona erdirebilir",
  ["Kiracı belirli süreli sözleşmeyi hiçbir hâlde süresinden önce veya bitiminde sona erdiremez",
   "Kiracının sözleşmeyi sona erdirmesi yalnızca kiraya verenin yazılı onayıyla mümkündür",
   "Kiracı, bildirimde bulunmasa dahi sözleşme her hâlde süre bitiminde kendiliğinden sona erer",
   "Kiracının bildirim yoluyla sona erdirme hakkı yalnızca on yıl geçtikten sonra doğar"],
  "TBK m.347: konut/çatılı işyerinde kiracı, belirli sürenin bitiminden en az on beş gün önce bildirimle sözleşmeyi sona erdirebilir; bildirmezse sözleşme bir yıl uzar.",
  "TBK m.347 - kiracının bildirimle sona erdirmesi"),

q("Konut ve çatılı işyeri kiralarında kiraya verenin sözleşmeyi sona erdirmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya veren, sözleşmeyi ancak kanunda sayılan belirli sebeplerle ve genellikle dava yoluyla sona erdirebilir",
  ["Kiraya veren, hiçbir sebep göstermeksizin süre bitiminde bildirimle sözleşmeyi sona erdirebilir",
   "Kiraya veren sözleşmeyi hiçbir koşulda ve hiçbir sebeple sona erdiremez",
   "Kiraya verenin sona erdirme hakkı yalnızca kira bedelinin hiç ödenmemesiyle sınırlıdır",
   "Kiraya veren, kiracının onayı olmadan sözleşmeyi tek bir bildirimle her zaman feshedebilir"],
  "TBK m.350 vd.: kiraya veren konut/çatılı işyeri kirasını ancak gereksinim, yeniden inşa, tahliye taahhüdü, temerrüt gibi sayılı sebeplerle sona erdirebilir.",
  "TBK m.350 - kiraya verenin sona erdirme sebepleri"),

q("Kira bedelinin ödenmemesi (kiracının temerrüdü) bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya veren, kiracıya bedeli ödemesi için süre verip bu sürede ödenmezse sözleşmeyi feshedebilir",
  ["Kira bedeli hiç ödenmese dahi kiraya veren sözleşmeyi hiçbir hâlde feshedemez",
   "Kiraya veren, süre vermeksizin ilk gecikmede sözleşmeyi kendiliğinden sona erdirmiş sayılır",
   "Temerrüt hâlinde kiraya verenin tek yaptırımı, gecikme faizi istemekten ibarettir",
   "Kiracının temerrüdü yalnızca işyeri kiralarında fesih sebebi oluşturur"],
  "TBK m.315: kira bedelini ödemede temerrüde düşen kiracıya kiraya veren yazılı süre verir; bu sürede ödenmezse sözleşmeyi feshedebilir.",
  "TBK m.315 - kiracının temerrüdü"),

q("Kiralananın kiracı tarafından üçüncü kişiye kullandırılması (alt kira) bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiracı, kiraya verene zarar verecek bir değişikliğe yol açmamak kaydıyla kiralananı kısmen veya tamamen başkasına kiralayabilir",
  ["Kiracı hiçbir koşulda kiralananı üçüncü bir kişiye kullandıramaz",
   "Alt kira için kiraya verenin onayı hiçbir hâlde gerekmez ve zarar koşulu aranmaz",
   "Alt kirada asıl kiracının kiraya verene karşı sorumluluğu tamamen sona erer",
   "Konut kiralarında alt kira serbest, işyeri kiralarında ise kesinlikle yasaktır"],
  "TBK m.322: kiracı, kiraya verene zarar verecek değişikliğe yol açmamak koşuluyla kiralananı alt kiraya verebilir; konutta yazılı izin aranabilir, kiracının sorumluluğu sürer.",
  "TBK m.322 - alt kira ve kullanım hakkının devri"),

q("Kiraya verenin ayıptan sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiraya veren, kiralananı kullanıma elverişli durumda teslim etmek ve bu durumda bulundurmakla yükümlüdür",
  ["Kiraya verenin kiralananı elverişli durumda bulundurma gibi bir borcu yoktur",
   "Kiralananın kullanıma elverişliliğini sağlamak yalnızca kiracının yükümüdür",
   "Kiraya veren, kiralanandaki hiçbir ayıptan sorumlu tutulamaz",
   "Kiraya verenin sorumluluğu yalnızca sözleşmede açıkça yazılıysa doğar"],
  "TBK m.301: kiraya veren, kiralananı kararlaştırılan tarihte, kullanıma elverişli durumda teslim etmek ve sözleşme süresince bu durumda bulundurmakla yükümlüdür.",
  "TBK m.301 - kiraya verenin teslim ve bulundurma borcu"),

q("Kiralananın el değiştirmesi (satılması) bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiralanan sözleşme süresince el değiştirirse, yeni malik kira sözleşmesinin tarafı hâline gelir",
  ["Kiralanan satılırsa kira sözleşmesi kendiliğinden ve her hâlde sona erer",
   "Yeni malik, mevcut kira sözleşmesiyle hiçbir hâlde bağlı olmaz",
   "Kira sözleşmesi ancak kiracı yeni malikle yeniden sözleşme yaparsa devam eder",
   "El değiştirme hâlinde kiracı derhâl tahliye etmek zorundadır"],
  "TBK m.310: kiralanan el değiştirirse yeni malik kira sözleşmesinin tarafı olur (satış kirayı bozmaz ilkesi); belirli koşullarda gereksinim nedeniyle sona erdirme saklıdır.",
  "TBK m.310 - kiralananın el değiştirmesi"),

q("Kiracının özenle kullanma ve komşulara saygı borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kiracı, kiralananı sözleşmeye uygun ve özenle kullanmak, komşulara gerekli saygıyı göstermekle yükümlüdür",
  ["Kiracının kiralananı nasıl kullanacağı konusunda hiçbir yükümü bulunmaz",
   "Kiracı kiralananı dilediği gibi tahrip edebilir; bundan hiçbir sorumluluğu doğmaz",
   "Kiracının özen borcu yalnızca işyeri kiralarında geçerlidir",
   "Kiracının komşularla ilişkisi kira sözleşmesini hiçbir biçimde ilgilendirmez"],
  "TBK m.316: kiracı kiralananı özenle kullanmak ve komşulara saygı göstermekle yükümlüdür; aykırılık sürerse sözleşme feshedilebilir.",
  "TBK m.316 - kiracının özen ve saygı borcu"),

q("Kira sözleşmesinin niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Kira, kullanımın devrini konu alan, sürekli edimli ve tam iki tarafa borç yükleyen bir sözleşmedir",
  ["Kira, mülkiyetin devrini konu alan ani edimli bir sözleşmedir",
   "Kira, yalnızca bir tarafa borç yükleyen ivazsız bir sözleşmedir",
   "Kira, bir eserin meydana getirilmesini konu alan bir sözleşmedir",
   "Kira, malın karşılıksız kullandırılmasını konu alan bir sözleşmedir"],
  "Kira; kullanımı devreden, süreye yayılan (sürekli edimli) ve iki tarafa da karşılıklı borç yükleyen ivazlı bir sözleşmedir.",
  "TBK m.299 - kiranın niteliği"),

# ── E. Ödünç sözleşmeleri (5) ────────────────────────────────────────────────
q("Kullanım ödüncü (ariyet) sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Ödünç verenin bir şeyin karşılıksız kullanılmasını ödünç alana bıraktığı, alanın aynı şeyi geri verdiği sözleşmedir",
  ["Ödünç alanın, aldığı şeyin bedelini ödünç verene ödediği sözleşmedir",
   "Ödünç alanın, aldığı şeyi tüketip aynı nitelikte başka bir şey iade ettiği sözleşmedir",
   "Ödünç verenin, verdiği şeyin mülkiyetini ödünç alana geçirdiği sözleşmedir",
   "Yalnızca para verilmesi hâlinde kurulabilen bir sözleşmedir"],
  "TBK m.379: kullanım ödüncünde ödünç veren bir şeyin karşılıksız kullanımını bırakır; ödünç alan o şeyin aynısını geri verir, mülkiyet geçmez.",
  "TBK m.379 - kullanım ödüncü"),

q("Tüketim ödüncü (karz/ödünç) sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Ödünç verenin bir miktar parayı veya tüketilebilir şeyi mülkiyetine geçirmek üzere verdiği, alanın aynı nitelik ve miktarda geri verdiği sözleşmedir",
  ["Ödünç alanın, aldığı şeyin aynısını (aynen o parçayı) geri vermekle yükümlü olduğu sözleşmedir",
   "Ödünç alana yalnızca kullanım hakkının tanındığı, mülkiyetin geçmediği sözleşmedir",
   "Bir işin görülmesi karşılığında ücret ödenmesini konu alan sözleşmedir",
   "Yalnızca bankaların taraf olabildiği ve faizsiz yapılamayan sözleşmedir"],
  "TBK m.386: tüketim ödüncünde verilen para veya tüketilebilir şeyin mülkiyeti ödünç alana geçer; alan aynı nitelik ve miktarda geri verir.",
  "TBK m.386 - tüketim ödüncü"),

q("Tüketim ödüncünde faiz bakımından aşağıdakilerden hangisi doğrudur?",
  "Ticari olmayan tüketim ödüncünde faiz, ancak kararlaştırılmışsa istenebilir",
  ["Tüketim ödüncünde faiz her hâlde kendiliğinden işler ve kararlaştırılması gerekmez",
   "Tüketim ödüncünde faiz kararlaştırılsa dahi hiçbir hâlde istenemez",
   "Faiz yalnızca kullanım ödüncünde söz konusu olabilir",
   "Tüketim ödüncünde faiz yalnızca ödünç alanın talebiyle işler"],
  "TBK m.387: adi (ticari olmayan) tüketim ödüncünde faiz ancak kararlaştırılmışsa istenebilir; ticari ödünçte ise kararlaştırılmasa da faiz istenebilir.",
  "TBK m.387 - ödünçte faiz"),


q("Kullanım ödüncü ile tüketim ödüncü arasındaki temel fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanım ödüncünde şeyin aynısı iade edilir ve mülkiyet geçmez; tüketim ödüncünde mülkiyet geçer ve aynı nitelikte iade edilir",
  ["İki sözleşmede de mülkiyet geçer ve aynı parça iade edilir",
   "İki sözleşmede de mülkiyet geçmez ve şeyin aynısı iade edilir",
   "Kullanım ödüncünde mülkiyet geçer, tüketim ödüncünde geçmez",
   "İki sözleşme arasında mülkiyet bakımından hiçbir fark bulunmaz"],
  "Temel fark mülkiyettedir: kullanım ödüncünde (ariyet) aynı şey iade edilir, mülkiyet geçmez; tüketim ödüncünde (karz) mülkiyet geçer, misli iade edilir.",
  "TBK m.379/m.386 - ödünç türleri farkı"),

# ── F. Hizmet sözleşmesi (5) ─────────────────────────────────────────────────
q("Hizmet sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşçinin belirli veya belirsiz süreyle bağımlı olarak iş görmeyi, işverenin ücret ödemeyi üstlendiği sözleşmedir",
  ["İşçinin bir eseri meydana getirmeyi, işverenin bedel ödemeyi üstlendiği sözleşmedir",
   "İşçinin işvereni temsilen üçüncü kişilerle sözleşme yapmayı üstlendiği sözleşmedir",
   "İşçinin bir malın mülkiyetini işverene devretmeyi üstlendiği sözleşmedir",
   "İşçinin karşılıksız olarak iş görmeyi üstlendiği ivazsız bir sözleşmedir"],
  "TBK m.393: hizmet sözleşmesinde işçi bağımlı olarak iş görmeyi, işveren ise ücret ödemeyi üstlenir; sonuç değil, iş görme edimi asıldır.",
  "TBK m.393 - hizmet sözleşmesi"),

q("Hizmet sözleşmesinin şekli bakımından aşağıdakilerden hangisi doğrudur?",
  "Hizmet sözleşmesi, kanunda aksi öngörülmedikçe herhangi bir şekle bağlı değildir",
  ["Hizmet sözleşmesinin geçerliliği her hâlde resmî senede bağlıdır",
   "Hizmet sözleşmesi yalnızca noter huzurunda yapıldığında geçerli olur",
   "Hizmet sözleşmesi ancak yazılı yapıldığında hüküm doğurur",
   "Hizmet sözleşmesi yalnızca işçi ve işverenin tacir olması hâlinde geçerlidir"],
  "TBK m.394: hizmet sözleşmesi kural olarak şekle bağlı değildir; kanunda öngörülen özel hâller (örneğin belirli süreli iş) dışında sözlü de kurulabilir.",
  "TBK m.394 - hizmet sözleşmesinin şekli"),

q("Hizmet ile eser sözleşmesi arasındaki temel fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Hizmet sözleşmesinde bağımlı iş görme edimi, eser sözleşmesinde ise belirli bir sonucun (eserin) meydana getirilmesi esastır",
  ["Her iki sözleşmede de yalnızca belirli bir sonucun meydana getirilmesi esastır",
   "Her iki sözleşmede de yüklenici işverene tam bağımlı olarak çalışır",
   "Hizmet sözleşmesinde sonuç, eser sözleşmesinde bağımlı iş görme esastır",
   "İki sözleşme arasında edimin niteliği bakımından hiçbir fark yoktur"],
  "Ayrım edimin niteliğindedir: hizmette bağımlı iş görme (emek) edimi, eserde ise bağımsız yüklenicinin bir sonuç/eser meydana getirmesi asıldır.",
  "TBK m.393/m.470 - hizmet ve eser farkı"),

q("İşverenin işçiyi gözetme borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "İşveren, işçinin kişiliğini korumak ve iş sağlığı ile güvenliği önlemlerini almakla yükümlüdür",
  ["İşverenin işçinin sağlığını veya güvenliğini gözetme gibi bir yükümü bulunmaz",
   "İşçinin korunması yalnızca işçinin kendi sorumluluğundadır",
   "İşverenin gözetme borcu yalnızca sözleşmede açıkça yazılmışsa doğar",
   "İşverenin gözetme borcu yalnızca kamu işyerlerinde geçerlidir"],
  "TBK m.417: işveren, işçinin kişiliğini korumak, iş sağlığı ve güvenliği için gerekli önlemleri almakla yükümlüdür.",
  "TBK m.417 - işverenin gözetme borcu"),

q("İşçinin sadakat ve özen borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "İşçi, işini özenle yapmak ve işverenin haklı menfaatini korumak (sadakat) yükümü altındadır",
  ["İşçinin işini özenle yapma veya işvereni gözetme gibi bir yükümü yoktur",
   "İşçinin sadakat borcu yalnızca sözleşme bittikten sonra doğar",
   "İşçi, işverenin menfaatine aykırı davranışlarından hiçbir hâlde sorumlu tutulamaz",
   "İşçinin özen borcu yalnızca yazılı sözleşmelerde geçerlidir"],
  "TBK m.396: işçi, işini özenle yapmak ve işverenin haklı menfaatlerini korumakla (sadakat borcu) yükümlüdür.",
  "TBK m.396 - işçinin özen ve sadakat borcu"),

# ── G. Eser sözleşmesi (6) ───────────────────────────────────────────────────
q("Eser sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yüklenicinin bir eser meydana getirmeyi, iş sahibinin de bedel ödemeyi üstlendiği sözleşmedir",
  ["Yüklenicinin işverene bağımlı olarak iş görmeyi üstlendiği sözleşmedir",
   "Yüklenicinin bir malın mülkiyetini iş sahibine devretmeyi üstlendiği sözleşmedir",
   "İş sahibinin bir malı yükleniciye karşılıksız kullandırdığı sözleşmedir",
   "Yüklenicinin iş sahibini temsilen işlem yapmayı üstlendiği sözleşmedir"],
  "TBK m.470: eser sözleşmesinde yüklenici bir eser meydana getirmeyi, iş sahibi de bunun karşılığında bedel ödemeyi üstlenir; sonuç (eser) esastır.",
  "TBK m.470 - eser sözleşmesi"),

q("Yüklenicinin eseri bizzat yapma borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Yüklenici, eseri kural olarak kendisi yapmak veya kendi yönetimi altında yaptırmakla yükümlüdür",
  ["Yüklenici eseri her hâlde bir başkasına devretmek zorundadır",
   "Yüklenicinin eseri kimin yapacağı hiçbir biçimde önem taşımaz",
   "Yüklenici, iş sahibinin onayı olmadan eseri hiçbir yardımcıya yaptıramaz",
   "Eserin kim tarafından yapılacağı yalnızca iş sahibinin takdirindedir"],
  "TBK m.471: yüklenici eseri bizzat yapmak veya kendi yönetimi altında yaptırmakla yükümlüdür; yüklenicinin kişisel özellikleri önem taşımıyorsa başkasına da yaptırabilir.",
  "TBK m.471 - eseri bizzat yapma"),

q("Eserin ayıplı olması hâlinde iş sahibinin hakları bakımından aşağıdakilerden hangisi doğrudur?",
  "İş sahibi ayıp ağırsa eseri reddedebilir, ayıbın giderilmesini veya bedelden indirim isteyebilir",
  ["Eser ayıplı olsa dahi iş sahibi hiçbir talepte bulunamaz",
   "İş sahibinin tek hakkı, eseri her hâlde aynen kabul etmektir",
   "İş sahibi yalnızca yükleniciyi değiştirmeyi isteyebilir; başka hakkı yoktur",
   "Ayıp hâlinde iş sahibi yalnızca cezai şart isteyebilir"],
  "TBK m.475: eser ayıplıysa iş sahibi, ayıp eseri kullanılamaz kılıyorsa reddedebilir; ayrıca ayıbın giderilmesini, bedelden indirim veya onarım giderini isteyebilir.",
  "TBK m.475 - eserdeki ayıp"),

q("Götürü bedelle yapılan eser sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bedel götürü kararlaştırılmışsa yüklenici, eseri kural olarak bu bedelle tamamlamakla yükümlüdür",
  ["Götürü bedelde yüklenici, harcadığı emeğe göre bedeli her zaman artırabilir",
   "Götürü bedel kararlaştırılması eser sözleşmesini geçersiz kılar",
   "Götürü bedelde iş sahibi, iş bitmeden istediği zaman bedeli düşürebilir",
   "Götürü bedel yalnızca taşınmaz yapımında kararlaştırılabilir"],
  "TBK m.480: götürü bedelde yüklenici eseri kararlaştırılan bedelle yapmakla yükümlüdür; öngörülemeyen olağanüstü durumlar dışında bedel artırılmaz.",
  "TBK m.480 - götürü bedel"),

q("Eser sözleşmesinde bedelin muacceliyeti (istenebilir hâle gelmesi) bakımından aşağıdakilerden hangisi doğrudur?",
  "Aksi kararlaştırılmadıkça bedel, eserin teslimi anında muaccel olur",
  ["Bedel her hâlde sözleşmenin kurulduğu anda peşin olarak muaccel olur",
   "Bedel yalnızca iş sahibinin dilediği zaman ödeme yapmasıyla muaccel olur",
   "Eser teslim edilse dahi bedel hiçbir zaman istenemez hâle gelmez",
   "Bedelin muacceliyeti yalnızca yüklenicinin tacir olmasına bağlıdır"],
  "TBK m.479: aksi kararlaştırılmadıkça yüklenicinin bedele hak kazanması ve bedelin muaccel olması eserin teslimi anındadır.",
  "TBK m.479 - bedelin muacceliyeti"),

q("İş sahibinin sözleşmeyi eser tamamlanmadan feshetmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İş sahibi, eser tamamlanmadan yüklenicinin bütün zararını gidererek sözleşmeyi feshedebilir",
  ["İş sahibi eser tamamlanmadan sözleşmeyi hiçbir hâlde feshedemez",
   "İş sahibi fesihte hiçbir tazminat ödemeksizin sözleşmeden dönebilir",
   "Fesih yalnızca yüklenicinin kusuruyla mümkündür",
   "Fesih hakkı yalnızca yükleniciye tanınmıştır; iş sahibinin böyle bir hakkı yoktur"],
  "TBK m.484: iş sahibi, eser tamamlanmadan yüklenicinin tüm zararını ödemek koşuluyla sözleşmeyi tek taraflı feshedebilir.",
  "TBK m.484 - iş sahibinin fesih hakkı"),

# ── H. Vekâlet (6) ───────────────────────────────────────────────────────────
q("Vekâlet sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Vekilin, vekâlet verenin bir işini görmeyi veya işlemini yapmayı üstlendiği sözleşmedir",
  ["Vekilin, vekâlet verene bir malın mülkiyetini devretmeyi üstlendiği sözleşmedir",
   "Vekilin, belirli bir eseri meydana getirmeyi üstlendiği sözleşmedir",
   "Vekilin, vekâlet verene bağımlı işçi olarak çalışmayı üstlendiği sözleşmedir",
   "Vekâlet verenin, vekile bir şeyi karşılıksız kullandırdığı sözleşmedir"],
  "TBK m.502: vekâlette vekil, vekâlet verenin bir işini görmeyi veya işlemini yapmayı üstlenir; belirli bir sonucu garanti etmez, iş görme edimi asıldır.",
  "TBK m.502 - vekâlet sözleşmesi"),

q("Vekâletin tek taraflı sona erdirilmesi (azil ve istifa) bakımından aşağıdakilerden hangisi doğrudur?",
  "Vekâlet veren azledebilir, vekil istifa edebilir; bu hak her zaman kullanılabilir",
  ["Vekâlet hiçbir tarafça tek taraflı olarak sona erdirilemez",
   "Yalnızca vekâlet veren azledebilir; vekilin istifa hakkı hiç yoktur",
   "Azil ve istifa yalnızca sözleşmede açıkça kararlaştırılmışsa mümkündür",
   "Vekâlet ancak mahkeme kararıyla sona erdirilebilir"],
  "TBK m.512: vekâlet veren her zaman azledebilir, vekil de her zaman istifa edebilir; uygun olmayan zamanda sona erdiren diğer tarafın zararını giderir.",
  "TBK m.512 - azil ve istifa"),

q("Vekilin talimata uyma borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Vekil, vekâlet verenin açık talimatına uymakla yükümlüdür; ancak zorunlu ve haberleşme imkânsızsa menfaate uygun davranabilir",
  ["Vekil, vekâlet verenin talimatlarını hiçbir hâlde dikkate almak zorunda değildir",
   "Vekil, her koşulda ve istisnasız kendi bildiği gibi hareket edebilir",
   "Vekil, vekâlet verenin talimatına aykırı davranmaktan hiçbir hâlde sorumlu olmaz",
   "Talimata uyma borcu yalnızca ücretli vekâlette söz konusudur"],
  "TBK m.505: vekil talimata uymakla yükümlüdür; haberleşme imkânsız ve gecikmede sakınca varsa, verenin menfaatine en uygun biçimde hareket edebilir.",
  "TBK m.505 - talimata uyma"),

q("Vekilin özenle ifa borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Vekil, üstlendiği işi vekâlet verenin haklı menfaatini gözeterek sadakat ve özenle yürütmekle yükümlüdür",
  ["Vekilin işi yürütürken özen veya sadakat gösterme yükümü yoktur",
   "Vekil, vekâlet verenin menfaatine aykırı davranmakta tamamen serbesttir",
   "Vekilin özen borcu yalnızca sözleşmede kararlaştırılmışsa doğar",
   "Vekilin özen ölçüsü yalnızca kendi işlerine gösterdiği özenle sınırlıdır"],
  "TBK m.506: vekil, vekâlet verenin menfaatlerini sadakat ve özenle gözeterek işi yürütür; özen ölçüsü benzer alandaki basiretli bir vekilinkidir.",
  "TBK m.506 - özen ve sadakat"),

q("Vekilin hesap verme borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Vekil, vekâlet verenin istemi üzerine yaptığı işlerin hesabını vermek ve edindiklerini ona teslim etmekle yükümlüdür",
  ["Vekilin vekâlet verene hesap verme veya edindiklerini teslim etme yükümü yoktur",
   "Vekil, iş görürken edindiği şeyleri kendi mülkiyetinde tutmakta serbesttir",
   "Hesap verme borcu yalnızca vekâlet sona erdikten on yıl sonra doğar",
   "Vekil hesap verse dahi edindiklerini teslim etmek zorunda değildir"],
  "TBK m.508: vekil, istem üzerine her zaman yaptığı işin hesabını vermek ve vekâlet dolayısıyla aldığı her şeyi vekâlet verene teslim etmekle yükümlüdür.",
  "TBK m.508 - hesap verme"),

q("Vekâletin ölümle sona ermesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Vekâlet, aksi kararlaştırılmadıkça taraflardan birinin ölümü, ehliyetini yitirmesi veya iflasıyla sona erer",
  ["Vekâlet, taraflardan birinin ölümüyle hiçbir hâlde sona ermez",
   "Vekâlet yalnızca mahkeme kararıyla sona erdirilebilir",
   "Vekâlet, yalnızca vekilin ölümüyle sona erer; verenin ölümü etkilemez",
   "Vekâletin sona ermesi tarafların iradesine bırakılmamıştır"],
  "TBK m.513: sözleşmeden veya işin niteliğinden aksi anlaşılmadıkça vekâlet, taraflardan birinin ölümü, ehliyetsizliği ya da iflasıyla sona erer.",
  "TBK m.513 - vekâletin sona ermesi"),

# ── I. Kefalet (5) ───────────────────────────────────────────────────────────
q("Kefalet sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kefilin, borçlunun borcunu ifa etmemesi hâlinde alacaklıya karşı sorumlu olmayı üstlendiği sözleşmedir",
  ["Kefilin, borçlunun borcunu bizzat üstlenip asıl borçlu hâline geldiği sözleşmedir",
   "Alacaklının, kefile bir malın mülkiyetini devrettiği sözleşmedir",
   "Kefilin, borçluya karşılıksız bir kazandırma yaptığı sözleşmedir",
   "Kefilin, alacaklıya bağımlı işçi olarak çalışmayı üstlendiği sözleşmedir"],
  "TBK m.581: kefalette kefil, borçlunun borcunu ifa etmemesinin sonuçlarından kişisel olarak sorumlu olmayı alacaklıya karşı üstlenir; borç fer'i (bağlı) niteliktedir.",
  "TBK m.581 - kefalet sözleşmesi"),

q("Kefalet sözleşmesinin şekli bakımından aşağıdakilerden hangisi doğrudur?",
  "Kefalet yazılı yapılmalı ve kefilin sorumlu olacağı azami miktar ile kefalet tarihi kefilin el yazısıyla belirtilmelidir",
  ["Kefalet hiçbir şekil koşuluna tabi olmayıp sözlü olarak da geçerlidir",
   "Kefalet için yalnızca alacaklının imzası yeterli olup kefilin imzası aranmaz",
   "Kefalette azami miktarın belirtilmesi gerekmez; sınırsız kefalet esastır",
   "Kefaletin geçerliliği yalnızca borçlunun onayına bağlıdır"],
  "TBK m.583: kefalet, yazılı şekilde yapılmadıkça ve kefilin sorumlu olduğu azami miktar ile kefalet tarihi el yazısıyla belirtilmedikçe geçerli olmaz.",
  "TBK m.583 - kefaletin şekli"),

q("Adi kefalet bakımından aşağıdakilerden hangisi doğrudur?",
  "Alacaklı, adi kefilin sorumluluğuna gitmeden önce kural olarak asıl borçluya başvurmak (tartışma def'i) zorundadır",
  ["Adi kefalette alacaklı, borçluya hiç başvurmadan doğrudan kefile gidebilir",
   "Adi kefalette kefil, asıl borçludan önce ve onun yerine sorumlu olur",
   "Adi kefalette kefilin hiçbir def'i ileri sürme hakkı yoktur",
   "Adi kefalet yalnızca ticari borçlarda söz konusu olabilir"],
  "TBK m.585: adi kefalette alacaklı, borçluya başvurup semeresiz kalmadıkça (tartışma def'i) kefile başvuramaz; bu, adi kefaleti müteselsil kefaletten ayırır.",
  "TBK m.585 - adi kefalette tartışma def'i"),

q("Müteselsil kefalet bakımından aşağıdakilerden hangisi doğrudur?",
  "Kefil müteselsil kefil sıfatıyla yükümlenmişse alacaklı, borçluya başvurmadan doğrudan kefile başvurabilir",
  ["Müteselsil kefalette alacaklı her hâlde önce borçluya başvurmak zorundadır",
   "Müteselsil kefalet, kefili asıl borçtan tamamen bağımsız kılar",
   "Müteselsil kefalette kefilin sorumluluğu asıl borçtan daha geniş olamayacağı gibi ondan da bağımsızdır",
   "Müteselsil kefalet yalnızca tüketici işlemlerinde geçerlidir"],
  "TBK m.586: müteselsil kefil, borçlu borcunu ödemediğinde alacaklı tarafından -önce borçluya gitme zorunluğu olmaksızın- doğrudan takip edilebilir.",
  "TBK m.586 - müteselsil kefalet"),

q("Kefaletin fer'iliği (bağlılığı) bakımından aşağıdakilerden hangisi doğrudur?",
  "Kefalet asıl borca bağlı fer'i bir borç olduğundan, asıl borç geçerli değilse kefalet de kural olarak geçersizdir",
  ["Kefalet, asıl borçtan tamamen bağımsız ve asli bir borç niteliğindedir",
   "Asıl borç sona erse dahi kefalet her hâlde ayakta kalmaya devam eder",
   "Kefalet, asıl borçtan daha ağır ve geniş kapsamlı olmak zorundadır",
   "Kefaletin geçerliliği asıl borcun geçerliliğinden hiçbir biçimde etkilenmez"],
  "TBK m.582: kefalet, mevcut ve geçerli bir asıl borca bağlıdır; fer'ilik gereği asıl borç geçersizse veya sona ererse kefalet de kural olarak etkilenir.",
  "TBK m.582 - kefaletin fer'iliği"),

# ── J. Diğer sözleşmeler (4) ─────────────────────────────────────────────────
q("Simsarlık (tellallık) sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Simsarın, taraflar arasında bir sözleşme kurulması imkânını hazırlamayı veya aracılık etmeyi üstlendiği sözleşmedir",
  ["Simsarın, iş sahibi adına ve hesabına doğrudan sözleşme yapmayı üstlendiği sözleşmedir",
   "Simsarın, bir eseri meydana getirmeyi üstlendiği sözleşmedir",
   "Simsarın, bir malın mülkiyetini devretmeyi üstlendiği sözleşmedir",
   "Simsarın, iş sahibine bağımlı işçi olarak çalışmayı üstlendiği sözleşmedir"],
  "TBK m.520: simsarlıkta simsar, sözleşme kurulması fırsatını göstermeyi veya kurulmasına aracılık etmeyi üstlenir; kural olarak sözleşme kurulursa ücrete hak kazanır.",
  "TBK m.520 - simsarlık"),

q("Vekâletsiz iş görme bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir kimsenin, vekâleti olmaksızın başkasının işini onun menfaatine ve varsayılan iradesine uygun görmesidir",
  ["Bir kimsenin, ancak yazılı vekâletle başkasının işini görmesidir",
   "İş sahibinin, kendi işini bizzat görmesini ifade eden bir kavramdır",
   "Yalnızca ücret karşılığında başkasının işinin görülmesidir",
   "Yalnızca kamu görevlilerinin yürüttüğü işleri kapsayan bir kurumdur"],
  "TBK m.526: vekâletsiz iş gören, iş sahibinin menfaat ve varsayılan iradesine uygun hareket etmelidir; aksi hâlde doğan zarardan sorumlu olur.",
  "TBK m.526 - vekâletsiz iş görme"),

q("Saklama (vedia) sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Saklayanın, kendisine bırakılan taşınırı güvenli biçimde koruyup geri vermeyi üstlendiği sözleşmedir",
  ["Saklayanın, kendisine bırakılan malın mülkiyetini kazandığı sözleşmedir",
   "Saklayanın, malı serbestçe kullanıp tüketebildiği sözleşmedir",
   "Bırakan kişinin, mala karşılık bedel aldığı bir satış sözleşmesidir",
   "Saklayanın malı hiçbir zaman geri vermek zorunda olmadığı sözleşmedir"],
  "TBK m.561: saklama sözleşmesinde saklayan, kendisine bırakılan taşınırı güvenli bir yerde korumayı ve istenince geri vermeyi üstlenir.",
  "TBK m.561 - saklama sözleşmesi"),

q("Ömür boyu gelir ve bakma sözleşmeleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir kimsenin, karşı tarafa hayatı boyunca bakıp gözetme ya da belirli gelir sağlama borcu altına girdiği sözleşmelerdir",
  ["Yalnızca bir malın mülkiyetinin peşin bedelle devrini konu alan sözleşmelerdir",
   "Karşılıksız olarak yalnızca bir defalık bir edim taahhüdünü içeren sözleşmelerdir",
   "Yalnızca ticari işletmeler arasında yapılabilen sözleşmelerdir",
   "Bir eserin meydana getirilmesini konu alan sözleşmelerdir"],
  "TBK m.607 vd. (ömür boyu gelir) ve m.611 vd. (ölünceye kadar bakma): bir taraf diğerine ömür boyu gelir sağlar ya da onu bakıp gözetmeyi üstlenir.",
  "TBK m.607/m.611 - ömür boyu gelir ve bakma"),


def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i - 1] == base[i - 2]) for i in range(2, len(base))):
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
                       "styleRef": "SGS Borçlar Hukuku (isimli sözleşmeler; sınav stiline kalibre)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    for path in (OUT_APP, OUT_CONTENT):
        json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yazıldı {len(out)} soru → iki repo | harf {''.join(x['answer'] for x in out)}")
