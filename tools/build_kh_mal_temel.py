# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Maliyet Muhasebesi / Maliyet Temelleri (60 soru = 3×20).
Doğru şık KISA, çeldiriciler UZUN. explanation'da harf atıfı YOK.
Aritmetik python'da hesaplanır. Yıla bağlı oran/tutar YOK."""
import json, random, re

L, T, LBL = "maliyet_muhasebesi", "maliyet_temelleri", "Maliyet Temelleri"
PREFIX, SEED = "kh-mal-temel", 20260901
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik/questions_topic_maliyet_temelleri_2026.json"

Q = []
def q(stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why,
                  ref=ref, difficulty=difficulty))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Temel kavramlar (10) ────────────────────────────────────────────────
q("Maliyet kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirli bir amaca ulaşmak için katlanılan ve parayla ölçülebilen fedakârlıkların toplamıdır",
  ["İşletmenin bir dönemde elde ettiği ve parayla ölçülen tüm gelirlerinin toplamını ifade eder",
   "İşletmenin sahip olduğu varlıkların piyasadaki güncel satış değerlerinin toplamını gösterir",
   "İşletmenin ortaklarına dağıttığı kâr paylarının bir hesap dönemindeki toplam tutarıdır",
   "İşletmenin gelecekte elde etmeyi beklediği nakit girişlerinin bugünkü değerini ifade eder"],
  "Maliyet, belirli bir amaca ulaşmak (mal veya hizmet edinmek, üretmek) için katlanılan ve parayla ölçülebilen fedakârlıkların toplamıdır.",
  "Maliyet muhasebesi - maliyet kavramı", "easy")

q("Harcama ile maliyet arasındaki fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Harcama para veya borç doğuran ödeme; maliyet ise belirli bir amaç için katlanılan fedakârlıktır",
  ["Harcama ile maliyet aynı kavram olup aralarında hiçbir hukuki veya teknik fark bulunmamaktadır",
   "Harcama belirli bir amaç için katlanılan fedakârlık; maliyet ise yalnızca nakit çıkışını ifade eder",
   "Harcama yalnızca nakit ödemeleri kapsar; borçlanma yoluyla edinilen varlıklar harcama sayılmaz",
   "Harcama yalnızca üretim işletmelerinde, maliyet ise yalnızca ticaret işletmelerinde kullanılır"],
  "Harcama, para ödenmesi veya borç altına girilmesidir. Maliyet ise belirli bir amaca ulaşmak için katlanılan fedakârlıktır. Her harcama maliyet doğurmayabilir (örneğin borç ödemesi).",
  "Maliyet muhasebesi - harcama/maliyet")

q("Gider kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Hasılat elde etmek amacıyla tüketilen ve dönem sonucuna yansıtılan maliyet unsurudur",
  ["Henüz tüketilmemiş ve gelecekte fayda sağlayacak varlıkları ifade eden bir kavram niteliğindedir",
   "İşletmenin bir dönemde tahsil ettiği nakit tutarını gösteren ve sonuca yansımayan bir kalemdir",
   "İşletmenin ortaklarına dağıttığı kâr payını ifade eden ve sonuç hesaplarına girmeyen bir tutardır",
   "Yalnızca üretimle ilgili tüketimleri kapsar; pazarlama ve yönetim tüketimleri gider sayılmaz"],
  "Gider, hasılat elde etmek amacıyla tüketilen mal ve hizmetlerin parasal tutarıdır ve tüketildiği dönemin sonucuna yansıtılır. Tüketilmemiş maliyet ise varlık olarak kalır.",
  "Maliyet muhasebesi - gider kavramı")

q("Zarar kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Hasılat elde etme amacına hizmet etmeksizin ortaya çıkan ve fayda sağlamayan tükenmelerdir",
  ["Hasılat elde etmek amacıyla bilinçli olarak katlanılan ve fayda sağlayan tüketimleri ifade eder",
   "İşletmenin gelecekte fayda sağlayacağı için aktifleştirilen ve varlık olarak izlenen tutarlardır",
   "İşletmenin ürettiği mamullerin maliyetine eklenen ve stoklarda izlenen normal tüketimlerdir",
   "İşletmenin dönem içinde elde ettiği gelirin giderleri aşan kısmını gösteren olumlu farktır"],
  "Zarar, hasılat elde etme amacına hizmet etmeyen, karşılığında fayda sağlanmayan tükenmelerdir (yangın, hırsızlık gibi). Gider ise hasılat amacına yönelik bilinçli tüketimdir.",
  "Maliyet muhasebesi - zarar kavramı")

q("Maliyet muhasebesinin amaçları bakımından aşağıdakilerden hangisi doğrudur?",
  "Mamul maliyetini saptamak, maliyet kontrolüne yardımcı olmak ve yönetim kararlarına veri sağlamaktır",
  ["Yalnızca işletmenin vergi borcunu hesaplamak ve beyannameyi hazırlamaktan ibaret bir işlevi vardır",
   "Yalnızca ortaklara dağıtılacak kâr payını belirlemek amacıyla tutulan bir kayıt sisteminden ibarettir",
   "Yalnızca işletmenin nakit giriş ve çıkışlarını izlemek üzere kurulmuş bir takip sistemidir",
   "Yalnızca dış kullanıcılara finansal tablo sunmak amacıyla tutulur; yönetimi hiç ilgilendirmez"],
  "Maliyet muhasebesinin başlıca amaçları: mamul/hizmet maliyetini saptamak, maliyet kontrolüne yardımcı olmak, planlama ve yönetim kararlarına veri sağlamaktır.",
  "Maliyet muhasebesi - amaçlar", "easy")

q("Maliyet muhasebesi ile finansal muhasebe ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet muhasebesi ağırlıkla iç kullanıcılara, finansal muhasebe ise ağırlıkla dış kullanıcılara bilgi sunar",
  ["Maliyet muhasebesi dış kullanıcılara, finansal muhasebe ise yalnızca yöneticilere bilgi sunmaktadır",
   "İki muhasebe dalı arasında hiçbir fark bulunmayıp aynı amaca hizmet eden tek bir sistemdirler",
   "Maliyet muhasebesi yalnızca ticaret işletmelerinde, finansal muhasebe yalnızca üretimde uygulanır",
   "Maliyet muhasebesi kayıt tutmaz; yalnızca finansal muhasebenin ürettiği raporları yorumlamaktadır"],
  "Maliyet muhasebesi ağırlıklı olarak işletme içi kullanıcılara (yönetim) planlama, kontrol ve karar verme için bilgi üretir; finansal muhasebe ise dış kullanıcılara yönelik finansal tablo hazırlar. İkisi ortak veri tabanını kullanır.",
  "Maliyet muhasebesi - finansal muhasebeyle ilişki")

q("Maliyet nesnesi (maliyet objesi) kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyeti ayrı olarak ölçülmek istenen mamul, hizmet, bölüm veya faaliyettir",
  ["Yalnızca işletmenin ürettiği fiziki mamulleri ifade eden dar kapsamlı bir kavram niteliğindedir",
   "İşletmenin maliyetlerini kaydettiği defter ve belgelerin tümünü ifade eden teknik bir kavramdır",
   "Maliyet muhasebesinde kullanılan ve maliyetleri dağıtmaya yarayan ölçü birimini ifade etmektedir",
   "İşletmenin maliyetlerini onaylayan ve denetleyen birimi ifade eden örgütsel bir kavramdır"],
  "Maliyet nesnesi, maliyetinin ayrıca ölçülmesi istenen her türlü unsurdur: bir mamul, hizmet, sipariş, bölüm, faaliyet veya müşteri olabilir.",
  "Maliyet muhasebesi - maliyet nesnesi")

q("Maliyet ile stok ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretim maliyetleri mamul satılana kadar stokta izlenir; satıldığında satılan mamul maliyetine dönüşür",
  ["Üretim maliyetleri oluştukları anda doğrudan gider yazılır; stokta hiçbir biçimde izlenmez",
   "Üretim maliyetleri yalnızca mamul satıldığında kaydedilir; üretim sırasında kayıt yapılmaz",
   "Üretim maliyetleri her hâlde dönem gideri sayılır ve stok değerlemesinde hiç dikkate alınmaz",
   "Üretim maliyetleri satış hasılatına eklenir; stok hesaplarıyla arasında bir ilişki bulunmaz"],
  "Üretim maliyetleri ürün maliyeti niteliğindedir: mamul stoklarında izlenir ve ancak satıldığında satılan mamullerin maliyeti olarak dönem sonucuna yansır (maliyet akışı).",
  "Maliyet muhasebesi - maliyet/stok ilişkisi")

q("Aşağıdakilerden hangileri maliyet muhasebesinin amaçlarındandır?\n\nI. Mamul maliyetini saptamak\n\nII. Maliyet kontrolüne yardımcı olmak\n\nIII. Yönetim kararlarına veri sağlamak",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Maliyet muhasebesi; mamul maliyetini saptamak (I), maliyet kontrolüne yardımcı olmak (II) ve planlama ile yönetim kararlarına veri sağlamak (III) amaçlarına birlikte hizmet eder. Üçü de doğrudur.",
  "Maliyet muhasebesi - amaçlar")

q("Maliyet, gider ve zarar ayrımı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tüketilmemiş maliyet varlık olarak izlenir\n\nII. Tüketilen ve hasılata hizmet eden maliyet gider olur\n\nIII. Zarar, karşılığında fayda sağlanan bilinçli bir tüketimdir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tüketilmemiş maliyet varlıktır (I) ve hasılata hizmet eden tüketim giderdir (II). Zarar ise karşılığında fayda sağlanmayan tükenmedir; bu nedenle III yanlıştır.",
  "Maliyet muhasebesi - maliyet/gider/zarar")

# ── B. Maliyet sınıflandırmaları (14) ──────────────────────────────────────
q("Direkt (dolaysız) maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet nesnesiyle doğrudan ilişkilendirilebilen ve ekonomik biçimde izlenebilen maliyettir",
  ["Maliyet nesnesiyle ilişkisi kurulamayan ve ancak dağıtım anahtarıyla yüklenebilen maliyettir",
   "Üretim hacmi değiştikçe toplamı değişmeyen ve sabit kalan maliyet türünü ifade etmektedir",
   "Yalnızca üretim dışı faaliyetlerde ortaya çıkan ve mamule yüklenmeyen maliyetleri ifade eder",
   "Geçmişte katlanılmış olan ve gelecekteki kararları etkilemeyen maliyetleri ifade eden bir türdür"],
  "Direkt maliyet, belirli bir maliyet nesnesiyle doğrudan ilişkilendirilebilen ve ekonomik biçimde izlenebilen maliyettir (direkt ilk madde ve malzeme, direkt işçilik).",
  "Maliyet sınıflandırması - izlenebilirlik", "easy")

q("Endirekt (dolaylı) maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet nesnesiyle doğrudan ilişkilendirilemeyen ve dağıtım anahtarıyla yüklenen maliyettir",
  ["Maliyet nesnesiyle doğrudan ilişkilendirilebilen ve kolayca izlenebilen maliyet türünü ifade eder",
   "Üretim hacmi arttıkça birim başına toplamı da orantılı olarak artan maliyeti ifade etmektedir",
   "Yalnızca işletmenin ürettiği mamulün hammaddesini oluşturan tüketimleri kapsayan bir türdür",
   "Gelecekte hiçbir fayda sağlamayacak olan ve iptal edilen maliyetleri ifade eden bir kategoridir"],
  "Endirekt maliyet, maliyet nesnesiyle doğrudan ilişkilendirilemeyen veya ekonomik olarak izlenemeyen maliyettir; mamule dağıtım anahtarı yardımıyla yüklenir (genel üretim giderleri).",
  "Maliyet sınıflandırması - izlenebilirlik")

q("Sabit maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirli bir faaliyet aralığında toplamı değişmeyen; birim başına ise üretim arttıkça azalan maliyettir",
  ["Toplamı üretim hacmiyle orantılı artan; birim başına ise sabit kalan maliyet türünü ifade eder",
   "Hem toplamı hem birim başına tutarı üretim hacminden bağımsız olarak sabit kalan maliyettir",
   "Toplamı üretim arttıkça azalan ve birim başına tutarı da sürekli düşen bir maliyet türüdür",
   "Yalnızca üretim yapılmadığı dönemlerde ortaya çıkan ve üretim başlayınca sıfırlanan maliyettir"],
  "Sabit maliyet, ilgili faaliyet aralığında toplam olarak değişmez (kira, amortisman); üretim arttıkça aynı toplam daha fazla birime dağıldığından birim başına sabit maliyet azalır.",
  "Maliyet sınıflandırması - davranış")

q("Değişken maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Toplamı üretim hacmiyle orantılı olarak değişen; birim başına ise sabit kalan maliyettir",
  ["Toplamı üretim hacminden bağımsız olarak sabit kalan; birim başına ise azalan maliyet türüdür",
   "Hem toplamı hem birim başına tutarı üretim hacmiyle orantılı olarak artan bir maliyet türüdür",
   "Yalnızca üretim durduğunda ortaya çıkan ve üretim sırasında hiç oluşmayan maliyetleri ifade eder",
   "Üretim hacmi arttıkça toplamı azalan ve birim başına tutarı artan bir maliyet kategorisidir"],
  "Değişken maliyet, toplam olarak üretim hacmiyle orantılı değişir (direkt ilk madde); birim başına ise sabit kalır. Sabit maliyetin tam tersi davranış gösterir.",
  "Maliyet sınıflandırması - davranış")

q("Karma (yarı değişken) maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Hem sabit hem değişken unsur içeren; belirli bir taban tutarı olup faaliyetle birlikte artan maliyettir",
  ["Yalnızca sabit unsur içeren ve faaliyet hacminden hiç etkilenmeyen bir maliyet türünü ifade eder",
   "Yalnızca değişken unsur içeren ve faaliyet sıfırken tutarı da sıfır olan bir maliyet kategorisidir",
   "Faaliyet hacmi belirli aralıkları aştığında basamaklar hâlinde sıçrayan maliyeti ifade etmektedir",
   "Geçmiş kararlardan doğan ve artık değiştirilemeyen maliyetleri ifade eden özel bir türdür"],
  "Karma (yarı değişken) maliyet hem sabit hem değişken unsur içerir: sabit bir taban tutarı vardır ve faaliyet hacmiyle birlikte değişken kısmı artar (sabit ücretli + kullanıma bağlı elektrik faturası gibi).",
  "Maliyet sınıflandırması - karma maliyet")

q("Basamaklı (kademeli) maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirli faaliyet aralıklarında sabit kalan; aralık aşıldığında sıçrama yaparak yeni bir düzeyde sabitlenen maliyettir",
  ["Faaliyet hacmiyle tam orantılı olarak ve kesintisiz biçimde sürekli artan bir maliyet türüdür",
   "Faaliyet hacmi ne olursa olsun hiçbir zaman ve hiçbir düzeyde değişmeyen mutlak sabit maliyettir",
   "Faaliyet hacmi arttıkça toplamı azalan ve giderek sıfıra yaklaşan bir maliyet kategorisidir",
   "Yalnızca direkt ilk madde ve malzemede görülen ve başka hiçbir maliyette karşılaşılmayan bir türdür"],
  "Basamaklı maliyet, belirli bir faaliyet aralığında sabittir; aralık aşıldığında kademe hâlinde sıçrar ve yeni aralıkta yine sabitlenir (ek ustabaşı istihdamı gibi).",
  "Maliyet sınıflandırması - basamaklı maliyet")

q("İlgili faaliyet aralığı (geçerli hacim aralığı) bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet davranışına ilişkin varsayımların geçerli olduğu faaliyet hacmi aralığıdır",
  ["Maliyetlerin her hacim düzeyinde aynı biçimde davrandığını ifade eden sınırsız bir aralıktır",
   "İşletmenin ulaşabileceği azami teorik kapasiteyi ifade eden ve aşılamayan bir üst sınırdır",
   "Yalnızca değişken maliyetler için geçerli olup sabit maliyetleri hiç ilgilendirmeyen bir kavramdır",
   "İşletmenin kâr elde etmeye başladığı faaliyet hacmini gösteren başabaş noktasını ifade eder"],
  "İlgili faaliyet aralığı, maliyet davranışı varsayımlarının (sabitin sabit, değişkenin orantılı kalması) geçerli olduğu hacim aralığıdır; bu aralık dışında varsayımlar bozulur.",
  "Maliyet sınıflandırması - faaliyet aralığı")

q("Ürün maliyeti ile dönem gideri ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Ürün maliyetleri stokta izlenip satışta gidere dönüşür; dönem giderleri ise oluştuğu dönemde sonuca yansır",
  ["Ürün maliyetleri oluştuğu dönemde sonuca yansır; dönem giderleri ise stokta izlenerek ertelenir",
   "İkisi arasında hiçbir fark bulunmayıp tümü oluştukları dönemde doğrudan gider yazılmaktadır",
   "Ürün maliyetleri hiçbir zaman gidere dönüşmez; sürekli olarak stok hesabında bekletilmektedir",
   "Dönem giderleri mamul maliyetine eklenir; ürün maliyetleri ise doğrudan özkaynaklardan düşülür"],
  "Ürün maliyetleri (DİMM, DİG, GÜG) stoklarda izlenir ve mamul satıldığında SMM olarak sonuca yansır. Dönem giderleri (pazarlama, genel yönetim) ise oluştukları dönemde doğrudan gider yazılır.",
  "Maliyet sınıflandırması - ürün/dönem")

q("İşlevlerine göre maliyet sınıflandırması bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyetler üretim, araştırma-geliştirme, pazarlama-satış-dağıtım, genel yönetim ve finansman işlevlerine göre ayrılır",
  ["Maliyetler yalnızca üretim ve üretim dışı olmak üzere iki işleve ayrılır; başka ayrım yapılmaz",
   "İşlevsel sınıflandırma yalnızca ticaret işletmelerinde kullanılır; üretim işletmelerinde uygulanmaz",
   "İşlevlerine göre sınıflandırma tekdüzen hesap planında yer almayan ve uygulanmayan bir yöntemdir",
   "Maliyetler yalnızca sabit ve değişken olarak ayrılır; işlevsel bir sınıflandırma söz konusu değildir"],
  "İşlevlerine göre maliyetler; üretim, araştırma-geliştirme, pazarlama-satış-dağıtım, genel yönetim ve finansman giderleri olarak sınıflandırılır. TDHP'nin 7'li grubu bu ayrımı esas alır.",
  "Maliyet sınıflandırması - işlev")

q("Kontrol edilebilirlik bakımından maliyet sınıflandırması için aşağıdakilerden hangisi doğrudur?",
  "Bir maliyetin kontrol edilebilirliği, ilgili yöneticinin o maliyet üzerinde yetkisi bulunup bulunmadığına göre belirlenir",
  ["Tüm maliyetler her yönetici tarafından kontrol edilebilir; kontrol edilemeyen maliyet bulunmamaktadır",
   "Hiçbir maliyet kontrol edilemez; maliyetler işletme dışı etkenlerce belirlenen veri niteliğindedir",
   "Kontrol edilebilirlik yalnızca değişken maliyetler için söz konusudur; sabitler hiç kontrol edilemez",
   "Kontrol edilebilirlik maliyetin tutarına göre belirlenir; büyük tutarlar her hâlde kontrol edilemez"],
  "Bir maliyet, belirli bir yöneticinin yetki alanı içinde ve onun kararlarıyla önemli ölçüde etkilenebiliyorsa o yönetici için kontrol edilebilir maliyettir. Aynı maliyet farklı kademeler için farklı sınıflanabilir.",
  "Maliyet sınıflandırması - kontrol edilebilirlik")

q("Bir üretim işletmesinde fabrika binasının kirası ve mamulün hammaddesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Fabrika kirası sabit ve endirekt; hammadde ise değişken ve direkt maliyettir",
  ["Fabrika kirası değişken ve direkt; hammadde ise sabit ve endirekt maliyet olarak sınıflandırılır",
   "İkisi de sabit ve direkt maliyet olup üretim hacminden bağımsız biçimde davranış göstermektedir",
   "İkisi de değişken ve endirekt maliyet olup mamule ancak dağıtım anahtarıyla yüklenebilmektedir",
   "Fabrika kirası dönem gideri, hammadde ise finansman gideri olarak sonuç hesaplarına aktarılır"],
  "Fabrika kirası üretim hacminden etkilenmez (sabit) ve tek bir mamulle doğrudan ilişkilendirilemez (endirekt, GÜG). Hammadde ise üretimle orantılı artar (değişken) ve mamulle doğrudan ilişkilendirilir (direkt).",
  "Maliyet sınıflandırması - uygulama")

q("Aşağıdakilerden hangileri maliyetlerin DAVRANIŞLARINA göre sınıflandırılmasında yer alır?\n\nI. Sabit maliyet\n\nII. Değişken maliyet\n\nIII. Direkt maliyet",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Davranışlarına göre maliyetler sabit (I), değişken (II) ve karma olarak sınıflandırılır. Direkt maliyet (III) ise davranış değil, izlenebilirlik ölçütüne göre yapılan bir sınıflandırmadır; bu nedenle yanlıştır.",
  "Maliyet sınıflandırması - davranış")

q("Maliyet davranışı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sabit maliyetin birim başına tutarı üretim arttıkça azalır\n\nII. Değişken maliyetin birim başına tutarı sabittir\n\nIII. Sabit maliyetin toplamı üretim arttıkça orantılı artar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sabit maliyette toplam değişmez, birim azalır (I); değişken maliyette toplam orantılı artar, birim sabit kalır (II). Sabit maliyetin toplamının orantılı artması (III) değişken maliyetin davranışıdır; bu nedenle yanlıştır.",
  "Maliyet sınıflandırması - davranış")

q("Aşağıdakilerden hangileri ürün (stoklanabilir) maliyet unsurlarındandır?\n\nI. Direkt ilk madde ve malzeme\n\nII. Direkt işçilik\n\nIII. Pazarlama, satış ve dağıtım giderleri",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Ürün maliyeti DİMM (I), direkt işçilik (II) ve genel üretim giderlerinden oluşur. Pazarlama-satış-dağıtım giderleri (III) ise dönem gideridir, stok maliyetine girmez.",
  "Maliyet sınıflandırması - ürün maliyeti")

# ── C. Üretim maliyeti unsurları ve akış (14) ──────────────────────────────
q("Üretim maliyetinin unsurları bakımından aşağıdakilerden hangisi doğrudur?",
  "Direkt ilk madde ve malzeme, direkt işçilik ve genel üretim giderlerinden oluşur",
  ["Yalnızca direkt ilk madde ve malzeme ile direkt işçilikten oluşur; genel üretim giderleri dâhil değildir",
   "Direkt ilk madde, direkt işçilik ve pazarlama giderlerinden oluşan üç unsurlu bir yapıya sahiptir",
   "Yalnızca genel üretim giderlerinden oluşur; direkt maliyetler dönem gideri olarak kaydedilmektedir",
   "Üretim maliyetinin unsurları belirlenmemiş olup her işletme kendi unsurlarını serbestçe seçer"],
  "Üretim maliyeti üç unsurdan oluşur: direkt ilk madde ve malzeme (DİMM), direkt işçilik (DİG) ve genel üretim giderleri (GÜG).",
  "Üretim maliyeti - unsurlar", "easy")

q("Direkt ilk madde ve malzeme bakımından aşağıdakilerden hangisi doğrudur?",
  "Mamulün bünyesine giren ve mamulle doğrudan ilişkilendirilebilen ana madde tüketimidir",
  ["Mamulün bünyesine girmeyen ve üretimi destekleyen yardımcı malzeme tüketimlerini ifade eder",
   "Üretimde çalışan işçilere ödenen ücret ve benzeri ödemelerin toplamını gösteren bir unsurdur",
   "Fabrika binasının kirası, amortismanı ve sigorta gideri gibi genel nitelikli tüketimleri kapsar",
   "Mamulün satışı için katlanılan reklam ve dağıtım harcamalarını ifade eden bir maliyet türüdür"],
  "Direkt ilk madde ve malzeme, mamulün bünyesine giren ve mamulle doğrudan ilişkilendirilebilen ana madde tüketimidir. Bünyeye girmeyen veya izlenmesi ekonomik olmayan malzemeler endirekt sayılır.",
  "Üretim maliyeti - DİMM")

q("Endirekt malzeme bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretimde kullanılan ancak mamulle doğrudan ilişkilendirilmesi ekonomik olmayan malzeme tüketimidir",
  ["Mamulün bünyesine giren ve mamulle doğrudan ilişkilendirilebilen ana madde tüketimini ifade eder",
   "Üretimde çalışan ve doğrudan mamul üzerinde çalışan işçilerin ücretlerini kapsayan bir unsurdur",
   "İşletmenin pazarlama faaliyetlerinde kullandığı ve üretimle ilgisi bulunmayan malzemelerdir",
   "Endirekt malzeme diye bir kavram bulunmayıp tüm malzemeler direkt olarak sınıflandırılmaktadır"],
  "Endirekt malzeme, üretim sürecinde kullanılan ancak mamulle doğrudan ilişkilendirilmesi mümkün ya da ekonomik olmayan malzemedir (yağ, vida, temizlik malzemesi); genel üretim giderleri içinde izlenir.",
  "Üretim maliyeti - endirekt malzeme")

q("Direkt işçilik bakımından aşağıdakilerden hangisi doğrudur?",
  "Mamulün üretiminde doğrudan çalışan ve mamulle ilişkilendirilebilen işçilik maliyetidir",
  ["Üretim sürecini destekleyen ancak mamul üzerinde doğrudan çalışmayan personelin ücretini kapsar",
   "İşletmenin genel yönetim biriminde çalışan personelin ücret ve benzeri ödemelerini ifade eder",
   "Mamulün bünyesine giren ana madde tüketiminin parasal tutarını gösteren bir maliyet unsurudur",
   "Pazarlama bölümünde çalışan satış temsilcilerinin ücret ve primlerini kapsayan bir gider türüdür"],
  "Direkt işçilik, mamulün üretiminde fiilen ve doğrudan çalışan işçilerin, mamulle ilişkilendirilebilen işçilik maliyetidir. Ustabaşı, bakım personeli gibi destek işçilikleri endirekt sayılır.",
  "Üretim maliyeti - direkt işçilik")

q("Genel üretim giderleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Direkt ilk madde ve direkt işçilik dışında kalan tüm üretim maliyetlerini kapsayan endirekt unsurdur",
  ["Yalnızca mamulün bünyesine giren ana madde tüketimlerini kapsayan bir maliyet unsurunu ifade eder",
   "Yalnızca pazarlama, satış ve genel yönetim giderlerini kapsayan bir dönem gideri kategorisidir",
   "Mamulle doğrudan ilişkilendirilebilen ve dağıtım anahtarı gerektirmeyen maliyetleri ifade eder",
   "Genel üretim giderleri üretim maliyetine dâhil edilmez; doğrudan dönem gideri yazılmaktadır"],
  "Genel üretim giderleri, DİMM ve direkt işçilik dışında kalan tüm üretim maliyetleridir: endirekt malzeme, endirekt işçilik, fabrika amortismanı, kira, enerji vb. Endirekt olduklarından mamule dağıtım anahtarıyla yüklenir.",
  "Üretim maliyeti - GÜG")

dimm, dig, gug = 180_000, 120_000, 90_000
q(f"Bir üretim işletmesinde direkt ilk madde ve malzeme {tr(dimm)} TL, direkt işçilik {tr(dig)} TL ve genel üretim giderleri {tr(gug)} TL'dir. Toplam üretim maliyeti kaç TL'dir?",
  f"{tr(dimm+dig+gug)} TL",
  [f"{tr(dimm+dig)} TL", f"{tr(dig+gug)} TL", f"{tr(dimm+gug)} TL", f"{tr(dimm)} TL"],
  f"Üretim maliyeti = DİMM + Direkt İşçilik + GÜG = {tr(dimm)} + {tr(dig)} + {tr(gug)} = {tr(dimm+dig+gug)} TL.",
  "Üretim maliyeti - toplam")

q(f"Direkt ilk madde ve malzeme {tr(dimm)} TL, direkt işçilik {tr(dig)} TL olan bir işletmede birinci madde ve malzeme ile işçilikten oluşan temel (asal) maliyet kaç TL'dir?",
  f"{tr(dimm+dig)} TL",
  [f"{tr(dimm+dig+gug)} TL", f"{tr(dig+gug)} TL", f"{tr(dimm-dig)} TL", f"{tr(dimm)} TL"],
  f"Temel (asal/birincil) maliyet = DİMM + Direkt İşçilik = {tr(dimm)} + {tr(dig)} = {tr(dimm+dig)} TL. Genel üretim giderleri bu tanıma dâhil değildir.",
  "Üretim maliyeti - temel maliyet")

q(f"Direkt işçilik {tr(dig)} TL, genel üretim giderleri {tr(gug)} TL olan bir işletmede dönüşüm (şekillendirme) maliyeti kaç TL'dir?",
  f"{tr(dig+gug)} TL",
  [f"{tr(dimm+dig)} TL", f"{tr(dimm+dig+gug)} TL", f"{tr(gug-dig)} TL", f"{tr(gug)} TL"],
  f"Dönüşüm maliyeti = Direkt İşçilik + GÜG = {tr(dig)} + {tr(gug)} = {tr(dig+gug)} TL. Bu, ilk maddeyi mamule dönüştürmek için katlanılan maliyeti gösterir; DİMM dâhil değildir.",
  "Üretim maliyeti - dönüşüm maliyeti")

q("Temel (asal) maliyet ile dönüşüm maliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Temel maliyet DİMM ile direkt işçilikten; dönüşüm maliyeti ise direkt işçilik ile GÜG'den oluşur",
  ["Temel maliyet direkt işçilik ile GÜG'den; dönüşüm maliyeti ise DİMM ile direkt işçilikten oluşur",
   "İkisi de aynı unsurlardan oluşur; aralarında hesaplama bakımından hiçbir fark bulunmamaktadır",
   "Temel maliyet yalnızca GÜG'den; dönüşüm maliyeti ise yalnızca DİMM'den oluşan kavramlardır",
   "İkisi de pazarlama ve genel yönetim giderlerini içerir; üretim maliyetiyle ilgileri bulunmaz"],
  "Temel (asal) maliyet = DİMM + Direkt İşçilik. Dönüşüm maliyeti = Direkt İşçilik + GÜG. Direkt işçilik her iki tanımda da yer alır.",
  "Üretim maliyeti - temel/dönüşüm")

q("Üretim maliyetlerinin akışı bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyetler önce yarı mamul, tamamlanınca mamul stokunda izlenir; satıldığında satılan mamul maliyetine dönüşür",
  ["Maliyetler oluştukları anda doğrudan satılan mamul maliyetine aktarılır; stok hesabı kullanılmaz",
   "Maliyetler önce mamul, sonra yarı mamul stokunda izlenir; bu sıra kanunen zorunlu tutulmuştur",
   "Maliyetler yalnızca dönem sonunda ve tek seferde stok hesaplarına aktarılarak izlenmektedir",
   "Üretim maliyetleri stok hesaplarında hiç izlenmez; tümü doğrudan özkaynaklardan indirilmektedir"],
  "Maliyet akışı: üretime verilen maliyetler yarı mamul hesabında toplanır, üretim tamamlanınca mamul stokuna aktarılır, mamul satılınca satılan mamullerin maliyetine dönüşerek sonuca yansır.",
  "Üretim maliyeti - maliyet akışı")

ybs, uretim_mal, ysS = 40_000, 390_000, 55_000
q(f"Dönem başı yarı mamul stoku {tr(ybs)} TL, döneme ait toplam üretim maliyeti {tr(uretim_mal)} TL ve dönem sonu yarı mamul stoku {tr(ysS)} TL'dir. Üretilen mamul maliyeti kaç TL'dir?",
  f"{tr(ybs+uretim_mal-ysS)} TL",
  [f"{tr(ybs+uretim_mal+ysS)} TL", f"{tr(uretim_mal-ybs+ysS)} TL", f"{tr(uretim_mal)} TL", f"{tr(uretim_mal-ysS)} TL"],
  f"Üretilen mamul maliyeti = Dönem başı yarı mamul + Dönem üretim maliyeti − Dönem sonu yarı mamul = {tr(ybs)} + {tr(uretim_mal)} − {tr(ysS)} = {tr(ybs+uretim_mal-ysS)} TL.",
  "Üretim maliyeti - üretilen mamul maliyeti")

mbs, uretilen, msS = 60_000, 375_000, 80_000
q(f"Dönem başı mamul stoku {tr(mbs)} TL, üretilen mamul maliyeti {tr(uretilen)} TL ve dönem sonu mamul stoku {tr(msS)} TL'dir. Satılan mamullerin maliyeti kaç TL'dir?",
  f"{tr(mbs+uretilen-msS)} TL",
  [f"{tr(mbs+uretilen+msS)} TL", f"{tr(uretilen-mbs+msS)} TL", f"{tr(uretilen)} TL", f"{tr(uretilen-msS)} TL"],
  f"Satılan mamullerin maliyeti = Dönem başı mamul + Üretilen mamul maliyeti − Dönem sonu mamul = {tr(mbs)} + {tr(uretilen)} − {tr(msS)} = {tr(mbs+uretilen-msS)} TL.",
  "Üretim maliyeti - SMM")

q("Tekdüzen hesap planında maliyet hesapları bakımından aşağıdakilerden hangisi doğrudur?",
  "Giderlerin izlenmesinde 7/A (fonksiyon esaslı) veya 7/B (çeşit esaslı) seçeneklerinden biri kullanılır",
  ["Maliyet hesapları için tek bir seçenek öngörülmüş olup tüm işletmeler aynı düzeni kullanmak zorundadır",
   "Maliyet hesapları hesap planında yer almaz; işletmeler kendi hesap kodlarını serbestçe belirler",
   "7/A seçeneği yalnızca ticaret işletmelerince, 7/B ise yalnızca bankalarca kullanılabilmektedir",
   "7/A ve 7/B seçeneklerinin ikisi de aynı anda ve birlikte kullanılmak zorunda tutulmaktadır"],
  "TDHP'de gider hesapları için iki seçenek vardır: 7/A giderleri fonksiyon esasına göre (710 DİMM, 720 Direkt İşçilik, 730 GÜG…), 7/B ise çeşit esasına göre izler. İşletme kanuni ölçütlere göre birini uygular.",
  "TDHP - 7/A ve 7/B seçenekleri")

q("Aşağıdakilerden hangileri üretim maliyetinin unsurlarındandır?\n\nI. Direkt ilk madde ve malzeme\n\nII. Direkt işçilik\n\nIII. Genel üretim giderleri",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üretim maliyeti; DİMM (I), direkt işçilik (II) ve genel üretim giderlerinden (III) oluşur. Üçü de üretim maliyetinin unsurudur.",
  "Üretim maliyeti - unsurlar")

# ── D. Kapasite, karar maliyetleri, uygulama (12) ──────────────────────────
q("Kapasite kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin belirli bir dönemde üretebileceği azami mamul veya hizmet miktarını ifade eder",
  ["İşletmenin bir dönemde fiilen sattığı mamul miktarını gösteren ve üretimle ilgisi olmayan bir ölçüdür",
   "İşletmenin sahip olduğu toplam varlıkların parasal tutarını gösteren bir büyüklük ölçüsüdür",
   "İşletmenin kâr elde etmeye başladığı satış düzeyini ifade eden bir başabaş göstergesidir",
   "İşletmenin ortaklarından sağladığı toplam sermaye tutarını ifade eden bir finansman kavramıdır"],
  "Kapasite, işletmenin mevcut üretim faktörleriyle belirli bir dönemde gerçekleştirebileceği azami üretim miktarıdır. Teorik, pratik, normal ve fiili kapasite olarak ayrılır.",
  "Maliyet temelleri - kapasite")

q("Normal kapasite bakımından aşağıdakilerden hangisi doğrudur?",
  "Olağan koşullarda, birkaç dönemin ortalaması alınarak ulaşılması beklenen üretim düzeyidir",
  ["Hiçbir kesinti ve duruş olmaksızın ulaşılabilecek teorik azami üretim düzeyini ifade etmektedir",
   "İşletmenin cari dönemde fiilen gerçekleştirdiği üretim miktarını gösteren bir kapasite türüdür",
   "İşletmenin hiç üretim yapmadığı ve tüm makinelerin durduğu düzeyi ifade eden bir kavramdır",
   "İşletmenin gelecekte ulaşmayı hedeflediği ve hiçbir zaman gerçekleşmeyen ideal üretim düzeyidir"],
  "Normal kapasite, olağan koşullarda ve birkaç dönemin ortalaması dikkate alınarak ulaşılması beklenen üretim düzeyidir. Sabit GÜG'ün mamule yüklenmesinde ölçüt olarak kullanılır (TMS 2).",
  "Maliyet temelleri - normal kapasite")

q("Kapasite kullanımının stok maliyetine etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Sabit genel üretim giderleri normal kapasiteye göre yüklenir; düşük üretimde yüklenemeyen kısım dönem gideri yazılır",
  ["Sabit genel üretim giderlerinin tamamı her hâlde fiilen üretilen mamullere yüklenmek zorundadır",
   "Sabit genel üretim giderleri hiçbir hâlde mamule yüklenmez; tümü doğrudan dönem gideri yazılır",
   "Düşük kapasite kullanımında yüklenemeyen sabit giderler gelecek dönemin stoklarına aktarılır",
   "Kapasite kullanım düzeyinin stok maliyeti üzerinde herhangi bir etkisi bulunmamaktadır"],
  "TMS 2: sabit genel üretim giderleri normal kapasite esas alınarak dönüştürme maliyetine dağıtılır. Fiili üretim normalin altındaysa dağıtılamayan kısım stok maliyetine eklenmez, oluştuğu dönemde gider yazılır.",
  "TMS 2 - normal kapasite ve sabit GÜG")

sabit_gug, normal_kap, fiili = 200_000, 10_000, 8_000
yuklenen = sabit_gug / normal_kap * fiili
q(f"Sabit genel üretim gideri {tr(sabit_gug)} TL, normal kapasite {tr(normal_kap)} birim ve fiili üretim {tr(fiili)} birimdir. TMS 2'ye göre mamullere yüklenecek sabit genel üretim gideri kaç TL'dir?",
  f"{tr(int(yuklenen))} TL",
  [f"{tr(sabit_gug)} TL", f"{tr(int(sabit_gug/fiili*normal_kap))} TL", f"{tr(int(sabit_gug-yuklenen))} TL", f"{tr(int(sabit_gug/normal_kap))} TL"],
  f"Birim başına sabit GÜG = {tr(sabit_gug)} / {tr(normal_kap)} = {tr(int(sabit_gug/normal_kap))} TL. Fiili üretime yüklenecek tutar = {tr(int(sabit_gug/normal_kap))} × {tr(fiili)} = {tr(int(yuklenen))} TL. Kalan {tr(int(sabit_gug-yuklenen))} TL dönem gideri yazılır.",
  "TMS 2 - sabit GÜG yüklemesi")

q("Batmış (gömülü) maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmişte katlanılmış ve hiçbir kararla değiştirilemeyecek olan; bu nedenle karara ilgisiz maliyettir",
  ["Gelecekte ortaya çıkacak ve alınacak karara göre değişebilen; bu nedenle karara ilgili maliyettir",
   "Bir seçenek tercih edildiğinde vazgeçilen diğer seçeneğin sağlayacağı faydayı ifade etmektedir",
   "Üretim hacmiyle orantılı olarak değişen ve birim başına sabit kalan bir maliyet türünü ifade eder",
   "Mamulün bünyesine giren ve mamulle doğrudan ilişkilendirilebilen ana madde tüketimini gösterir"],
  "Batmış maliyet geçmişte katlanılmıştır ve hangi karar alınırsa alınsın değişmez; bu nedenle karar analizinde dikkate alınmaz (ilgisiz maliyet).",
  "Karar maliyetleri - batmış maliyet")

q("Fırsat maliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir seçenek tercih edildiğinde vazgeçilen en iyi diğer seçeneğin sağlayacağı faydadır",
  ["Geçmişte fiilen katlanılmış ve muhasebe kayıtlarında yer alan bir maliyet türünü ifade etmektedir",
   "İşletmenin ürettiği mamulün bünyesine giren ana madde tüketiminin parasal tutarını göstermektedir",
   "İşletmenin bankaya ödediği faiz giderlerinin toplamını ifade eden bir finansman maliyetidir",
   "Üretim hacmi arttıkça toplamı değişmeyen ve sabit kalan maliyetleri ifade eden bir kavramdır"],
  "Fırsat maliyeti, bir seçeneğin tercih edilmesi nedeniyle vazgeçilen en iyi alternatifin sağlayacağı faydadır. Muhasebe kayıtlarında yer almaz ancak karar analizinde dikkate alınır.",
  "Karar maliyetleri - fırsat maliyeti")

q("İlgili (geçerli) maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekte ortaya çıkacak ve seçenekler arasında farklılık gösteren maliyettir",
  ["Geçmişte katlanılmış ve seçenekler arasında hiç farklılık göstermeyen maliyeti ifade etmektedir",
   "Muhasebe kayıtlarında yer alan tüm maliyetleri kapsayan ve ayrım yapılmayan bir kategoridir",
   "Yalnızca sabit maliyetleri kapsayan ve değişken maliyetleri hiç dikkate almayan bir kavramdır",
   "Yalnızca üretim maliyetlerini kapsar; pazarlama ve yönetim maliyetleri hiç ilgili sayılmaz"],
  "Bir maliyetin karar açısından ilgili olabilmesi için iki koşul aranır: gelecekte ortaya çıkacak olması ve seçenekler arasında farklılık göstermesi. Batmış maliyetler ve seçenekler arasında değişmeyen maliyetler ilgisizdir.",
  "Karar maliyetleri - ilgili maliyet")

q("Bir işletme daha önce satın aldığı ve kullanılamayan bir makinenin maliyetini yeni yatırım kararında dikkate almak istemektedir. Bu durumda aşağıdakilerden hangisi doğrudur?",
  "Makinenin geçmişteki maliyeti batmış maliyettir; yeni karar hangi yönde alınırsa alınsın değişmeyeceğinden dikkate alınmaz",
  ["Makinenin geçmişteki maliyeti her hâlde yeni yatırım kararına dâhil edilmek zorunda tutulmaktadır",
   "Makinenin geçmişteki maliyeti fırsat maliyeti sayılır ve yeni seçeneğin maliyetine eklenmelidir",
   "Makinenin maliyeti değişken maliyet olduğundan yeni üretim hacmine göre yeniden hesaplanmalıdır",
   "Makinenin maliyeti gelecekte değişebileceğinden karar açısından ilgili maliyet kabul edilmelidir"],
  "Geçmişte katlanılmış ve geri alınamayacak olan makine maliyeti batmış maliyettir; hangi karar verilirse verilsin değişmez, bu nedenle karar analizine dâhil edilmez.",
  "Karar maliyetleri - batmış maliyet (senaryo)")

q("Bir işletme atıl duran bir üretim hattını kiraya verme fırsatından vazgeçerek kendi üretiminde kullanmaya karar vermiştir. Bu durumda aşağıdakilerden hangisi doğrudur?",
  "Vazgeçilen kira geliri, kendi üretim seçeneğinin fırsat maliyetini oluşturur",
  ["Vazgeçilen kira geliri hiçbir maliyet doğurmaz; yalnızca fiilen ödenen tutarlar maliyet sayılır",
   "Vazgeçilen kira geliri batmış maliyet sayılır ve karar analizinde dikkate alınmamalıdır",
   "Vazgeçilen kira geliri işletmenin hasılatına eklenir ve dönem kârını artıran bir unsur olur",
   "Vazgeçilen kira geliri direkt ilk madde maliyeti olarak mamulün bünyesine yüklenmelidir"],
  "Kendi üretimini seçerek vazgeçilen kira geliri, tercih edilmeyen en iyi alternatifin faydasıdır; bu nedenle seçilen seçeneğin fırsat maliyetidir ve karar analizinde dikkate alınır.",
  "Karar maliyetleri - fırsat maliyeti (senaryo)")

q("Bir işletmede aylık fabrika kirası her ay aynı tutardadır ve üretim miktarından etkilenmemektedir. Bu maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "İlgili faaliyet aralığında sabit maliyettir; üretim arttıkça birim başına düşen payı azalır",
  ["Değişken maliyettir; üretim arttıkça toplam tutarı da orantılı olarak artış göstermektedir",
   "Karma maliyettir; hem sabit hem değişken unsur içerdiğinden ikiye ayrılarak analiz edilir",
   "Batmış maliyettir; geçmişte katlanıldığı için gelecekteki kararlarda hiç dikkate alınmaz",
   "Direkt maliyettir; mamulle doğrudan ilişkilendirilebildiği için dağıtım anahtarı gerekmez"],
  "Üretim miktarından etkilenmeyen ve toplamı değişmeyen fabrika kirası sabit maliyettir. Toplam sabit kaldığından üretim arttıkça birim başına düşen sabit maliyet payı azalır.",
  "Maliyet davranışı - sabit maliyet (senaryo)")

q("Aşağıdakilerden hangileri karar analizinde ilgisiz (geçersiz) maliyet sayılır?\n\nI. Batmış maliyet\n\nII. Seçenekler arasında farklılık göstermeyen maliyet\n\nIII. Fırsat maliyeti",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Batmış maliyet (I) ve seçenekler arasında değişmeyen maliyet (II) karar açısından ilgisizdir. Fırsat maliyeti (III) ise seçenekler arasında farklılık doğurduğundan ilgili maliyettir; bu nedenle yanlıştır.",
  "Karar maliyetleri - ilgili/ilgisiz")

q("Maliyet kavramları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Batmış maliyet geçmişte katlanılmıştır ve değiştirilemez\n\nII. Fırsat maliyeti muhasebe kayıtlarında yer almaz\n\nIII. İlgili maliyet, seçenekler arasında farklılık göstermeyen maliyettir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Batmış maliyet geçmişte katlanılmış ve değiştirilemezdir (I); fırsat maliyeti kayıtlarda yer almaz ancak karar analizine girer (II). İlgili maliyet ise seçenekler arasında FARKLILIK GÖSTEREN maliyettir; III bunun tersini söylediğinden yanlıştır.",
  "Karar maliyetleri - kavramlar")

q("Endirekt işçilik bakımından aşağıdakilerden hangisi doğrudur?",
  "Üretimi destekleyen ancak mamul üzerinde doğrudan çalışmayan personelin işçilik maliyetidir",
  ["Mamulün üretiminde fiilen ve doğrudan çalışan işçilerin ücretlerini kapsayan bir maliyet unsurudur",
   "İşletmenin pazarlama bölümünde çalışan satış personelinin ücretlerini ifade eden bir gider türüdür",
   "Mamulün bünyesine giren ana madde tüketiminin parasal tutarını gösteren bir maliyet kalemidir",
   "Endirekt işçilik diye bir kavram bulunmayıp tüm işçilikler direkt olarak sınıflandırılmaktadır"],
  "Endirekt işçilik; ustabaşı, bakım-onarım personeli, depo görevlisi gibi üretimi destekleyen ancak mamulle doğrudan ilişkilendirilemeyen işçilik maliyetidir ve genel üretim giderleri içinde izlenir.",
  "Üretim maliyeti - endirekt işçilik")

q("Maliyet yeri (gider yeri) kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyetlerin toplandığı ve izlendiği örgütsel bölüm ya da faaliyet birimidir",
  ["Maliyeti ayrıca ölçülmek istenen mamul veya hizmeti ifade eden bir kavram niteliğindedir",
   "İşletmenin maliyet kayıtlarını sakladığı fiziki arşiv alanını ifade eden teknik bir terimdir",
   "Maliyetlerin mamullere yüklenmesinde kullanılan ölçü birimini ifade eden bir dağıtım aracıdır",
   "İşletmenin ürettiği mamullerin satıldığı coğrafi bölgeyi ifade eden pazarlama kavramıdır"],
  "Maliyet (gider) yeri, maliyetlerin oluştuğu ve toplandığı örgütsel birimdir (esas üretim yerleri, yardımcı üretim yerleri, hizmet yerleri). Maliyetler önce gider yerlerinde toplanır, sonra mamullere yüklenir.",
  "Maliyet muhasebesi - gider yeri")

q("Esas üretim gider yeri ile yardımcı üretim gider yeri ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Esas üretim yerlerinde mamul doğrudan işlem görür; yardımcı yerler ise esas yerlere hizmet sunar",
  ["Yardımcı üretim yerlerinde mamul doğrudan işlem görür; esas yerler ise onlara destek vermektedir",
   "İkisi arasında hiçbir fark bulunmayıp aynı işlevi gören ve eş anlamlı kullanılan kavramlardır",
   "Esas üretim yerleri yalnızca pazarlama, yardımcı üretim yerleri ise yalnızca yönetim birimleridir",
   "Yardımcı üretim yerlerinin maliyetleri hiçbir hâlde mamule yansıtılmaz; doğrudan gider yazılır"],
  "Esas üretim gider yerlerinde mamul fiilen işlem görür (kesim, montaj). Yardımcı üretim gider yerleri ise esas yerlere hizmet sunar (bakım-onarım, enerji); maliyetleri ikinci dağıtımla esas yerlere aktarılır.",
  "Maliyet muhasebesi - gider yeri türleri")

q("Maliyet taşıyıcısı (maliyet objesi) ile gider yeri ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyetler önce gider yerlerinde toplanır, ardından maliyet taşıyıcısı olan mamullere yüklenir",
  ["Maliyetler önce mamullere yüklenir, ardından gider yerlerine dağıtılarak ikinci kez izlenir",
   "Gider yeri ile maliyet taşıyıcısı aynı kavram olup ikisi arasında hiçbir fark bulunmamaktadır",
   "Maliyetler hiçbir yerde toplanmaz; her maliyet oluştuğu anda doğrudan dönem gideri yazılır",
   "Maliyet taşıyıcısı kavramı yalnızca ticaret işletmelerinde kullanılır; üretimde uygulanmaz"],
  "Maliyet akışında endirekt maliyetler önce gider yerlerinde toplanır (dağıtım), sonra uygun dağıtım anahtarlarıyla maliyet taşıyıcısına (mamul/sipariş) yüklenir.",
  "Maliyet muhasebesi - taşıyıcı/gider yeri")

q("Fiili maliyet ile tahmini (önceden belirlenmiş) maliyet ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Fiili maliyet gerçekleşen tutarlara; tahmini maliyet ise önceden belirlenen ölçütlere dayanır",
  ["Fiili maliyet önceden belirlenen ölçütlere; tahmini maliyet ise gerçekleşen tutarlara dayanmaktadır",
   "İkisi arasında hiçbir fark bulunmayıp aynı hesaplama yöntemini ifade eden eş anlamlı kavramlardır",
   "Fiili maliyet yalnızca ticaret, tahmini maliyet ise yalnızca hizmet işletmelerinde kullanılabilir",
   "Tahmini maliyet muhasebe kayıtlarında hiç kullanılmaz; yalnızca akademik bir kavram niteliğindedir"],
  "Fiili maliyet, gerçekleşmiş tutarlar üzerinden hesaplanır (dönem sonunda bilinir). Tahmini/standart maliyet ise önceden belirlenmiş ölçütlere dayanır ve kontrol ile hızlı bilgi sağlar.",
  "Maliyet muhasebesi - fiili/tahmini maliyet")

q("Ticaret işletmesi ile üretim işletmesinde maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Ticaret işletmesinde satılan ticari mal maliyeti; üretim işletmesinde ise üretim maliyeti hesaplanır",
  ["Ticaret işletmesinde de üretim maliyeti hesaplanır; iki işletme türü arasında hiçbir fark yoktur",
   "Üretim işletmesinde maliyet hesaplanmaz; yalnızca ticaret işletmeleri maliyet muhasebesi tutar",
   "Ticaret işletmesinde maliyet kavramı bulunmaz; yalnızca satış hasılatı kaydedilerek izlenmektedir",
   "İki işletme türünde de yalnızca direkt işçilik izlenir; malzeme ve genel giderler dikkate alınmaz"],
  "Ticaret işletmesi malı hazır alıp satar; maliyeti satın alma bedeli ve ek giderlerden oluşur (SMM). Üretim işletmesi ise mamulü kendisi üretir; DİMM + DİG + GÜG'den oluşan üretim maliyetini hesaplar.",
  "Maliyet muhasebesi - işletme türü")

q("Hizmet işletmelerinde maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Hizmet işletmelerinde de maliyet hesaplanır; ancak stoklanabilir mamul bulunmadığından maliyet ağırlıkla dönem sonucuna yansır",
  ["Hizmet işletmelerinde maliyet kavramı bulunmayıp yalnızca hasılat kaydedilerek izlenmektedir",
   "Hizmet işletmelerinde üretilen hizmetler her hâlde stokta izlenir ve satılana kadar bekletilir",
   "Hizmet işletmeleri yalnızca direkt malzeme maliyeti hesaplar; işçilik ve genel giderler dikkate alınmaz",
   "Hizmet işletmelerinde maliyet muhasebesi tutulması kanunen yasaklanmış bir uygulamadır"],
  "Hizmet işletmelerinde de maliyet hesaplanır (direkt işçilik ve genel giderler ağırlıklıdır). Ancak hizmet stoklanamadığından üretilen hizmetin maliyeti ağırlıkla oluştuğu dönemin sonucuna yansır.",
  "Maliyet muhasebesi - hizmet işletmeleri")

q("Maliyet muhasebesinde 7/A seçeneği bakımından aşağıdakilerden hangisi doğrudur?",
  "Giderler önce fonksiyonlarına göre izlenir; üretim giderleri 710, 720 ve 730 hesaplarında toplanır",
  ["Giderler yalnızca çeşit esasına göre izlenir; fonksiyonel bir ayrım hiçbir biçimde yapılmamaktadır",
   "7/A seçeneğinde gider hesabı kullanılmaz; tüm tüketimler doğrudan stok hesabına kaydedilmektedir",
   "7/A seçeneği yalnızca dönem sonunda tek bir kayıtla uygulanır; dönem içinde gider izlenmez",
   "7/A seçeneği yalnızca bankalar ve sigorta şirketleri tarafından kullanılabilen özel bir düzendir"],
  "TDHP 7/A seçeneğinde giderler fonksiyon esasına göre izlenir: 710 Direkt İlk Madde ve Malzeme Giderleri, 720 Direkt İşçilik Giderleri, 730 Genel Üretim Giderleri, 760 Pazarlama, 770 Genel Yönetim vb.",
  "TDHP - 7/A seçeneği")

q("Aşağıdakilerden hangileri genel üretim giderleri içinde yer alır?\n\nI. Endirekt malzeme\n\nII. Endirekt işçilik\n\nIII. Fabrika binasının amortismanı",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Genel üretim giderleri; endirekt malzeme (I), endirekt işçilik (II) ve fabrika amortismanı (III) gibi DİMM ve direkt işçilik dışındaki tüm üretim maliyetlerini kapsar. Üçü de GÜG'dür.",
  "Üretim maliyeti - GÜG kapsamı")

q("Gider yerleri bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Esas üretim yerlerinde mamul doğrudan işlem görür\n\nII. Yardımcı üretim yerleri esas yerlere hizmet sunar\n\nIII. Yardımcı üretim yerlerinin maliyetleri mamule hiçbir biçimde yansıtılmaz",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Esas üretim yerlerinde mamul işlem görür (I) ve yardımcı yerler esas yerlere hizmet sunar (II). Yardımcı yerlerin maliyetleri ikinci dağıtımla esas yerlere, oradan da mamule yansıtılır; bu nedenle III yanlıştır.",
  "Maliyet muhasebesi - gider yerleri")

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
        ch = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            ch[k] = d
        assert len(set(ch.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "lessonId": L, "topicId": T,
            "question": it["stem"], "choices": ch, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", LBL],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-16T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "2026-07-16",
            "sourceUpdatedAt": "2026-07-16T00:00:00Z", "isPremium": False, "isActive": True,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = sum(1 for x in out if len(MARK.findall(x["question"])) >= 2)
    print(f"yazıldı: {len(out)} soru | öncüllü {onc} | harf {''.join(x['correctAnswer'] for x in out)[:40]}…")
