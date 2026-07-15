# -*- coding: utf-8 -*-
"""Yeterlilik — Hukuk Test 2 + Test 3 (2×20 = 40 soru).
Ticaret + Borçlar + İş/SGK. Doğru şık KISA, çeldiriciler UZUN.
Yıla bağlı tutar YOK (asgari ücret vb.); kanunda sabit yapısal sayı serbest.
explanation'da harf atıfı YOK (permütasyondan etkilenmesin)."""
import json, random

Q = []
def q(lesson, topic, label, stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    Q.append(dict(lesson=lesson, topic=topic, label=label, stem=stem, correct=correct,
                  distractors=distractors, why=why, ref=ref, difficulty=difficulty))

T, B, I = "ticaret_hukuku", "borclar_hukuku", "is_ve_sosyal_guvenlik_hukuku"

# ══ TİCARET HUKUKU (13) ═══════════════════════════════════════════════════
q(T, "ticari_isletme", "Ticari İşletme",
  "Türk Ticaret Kanunu'na göre ticari işletmenin tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Esnaf faaliyeti sınırını aşan düzeyde gelir sağlamayı hedefleyen, sürekli ve bağımsız biçimde yürütülen faaliyettir",
  ["Yalnızca bir defaya mahsus yapılan ve süreklilik taşımayan her türlü kazanç sağlama girişimidir",
   "Kâr amacı gütmeksizin üyelerinin ortak gereksinimlerini karşılamak üzere kurulan bir örgütlenmedir",
   "Bir başka işletmeye bağlı olarak ve onun talimatıyla yürütülen her türlü yardımcı faaliyettir",
   "Yalnızca sermaye şirketleri tarafından işletilebilen ve gerçek kişilere kapalı olan bir yapıdır"],
  "TTK m.11: ticari işletme, esnaf faaliyeti sınırını aşan düzeyde gelir sağlamayı hedef tutan, sürekli ve bağımsız biçimde yürütülen faaliyetlerin bütünüdür.",
  "6102 sayılı TTK m.11", "easy")

q(T, "ticari_isletme", "Ticari İşletme",
  "Ticari işletmenin devri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, içindeki malvarlığı unsurlarıyla birlikte bir bütün olarak ve tek bir sözleşmeyle devredilebilir",
  ["İşletmenin devri için her bir malvarlığı unsurunun ayrı ayrı ve kendi usulüne göre devredilmesi zorunludur",
   "Ticari işletme hiçbir biçimde devredilemez; yalnızca tasfiye edilerek sona erdirilebilir",
   "İşletmenin devri yalnızca mahkeme kararıyla ve alacaklıların oybirliğiyle gerçekleşebilir",
   "İşletme devrinde borçlar hiçbir hâlde devralana geçmez; tümü devredende kalmaya devam eder"],
  "TTK m.11/3: ticari işletme, içerdiği malvarlığı unsurlarının devri için zorunlu tasarruf işlemlerinin ayrı ayrı yapılmasına gerek olmaksızın bir bütün hâlinde devredilebilir.",
  "6102 sayılı TTK m.11/3")

q(T, "ticari_isletme", "Ticari İşletme",
  "Ticari işletmede merkez ve şube ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Şube, merkeze bağlı olmakla birlikte dış ilişkide bağımsız işlem yapabilen ve ayrıca tescil edilen birimdir",
  ["Şube merkezden tümüyle bağımsız ayrı bir tüzel kişilik olup kendi adına malvarlığına sahiptir",
   "Şube hiçbir biçimde ticaret siciline tescil edilmez; yalnızca merkez tescile tabi tutulur",
   "Bir ticari işletmenin birden fazla şubesi bulunması kanunen yasaklanmış bir durumdur",
   "Şube ile merkez arasında hukuki bakımdan hiçbir bağ bulunmaz; ikisi ayrı işletmelerdir"],
  "Şube, merkeze bağlı olmakla birlikte dış ilişkilerde bağımsız işlem yapabilen ve bulunduğu yer ticaret siciline tescil edilen birimdir; ayrı tüzel kişiliği yoktur.",
  "6102 sayılı TTK m.40 vd. - şube")

q(T, "tacir_yukumluluklari", "Tacirin Yükümlülükleri",
  "Gerçek kişilerde tacir sıfatının kazanılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir ticari işletmeyi kısmen de olsa kendi adına işleten kişi tacirdir",
  ["Tacir sıfatı yalnızca ticaret siciline tescil işlemi tamamlandıktan sonra ve tescille kazanılabilir",
   "Bir ticari işletmeyi başkası adına ve onun hesabına işleten kişi de doğrudan tacir sayılır",
   "Tacir sıfatı yalnızca vergi dairesine mükellefiyet kaydı yaptırılmasıyla kendiliğinden doğar",
   "Gerçek kişiler hiçbir hâlde tacir olamaz; tacir sıfatı yalnızca tüzel kişilere tanınmıştır"],
  "TTK m.12: bir ticari işletmeyi kısmen de olsa kendi adına işleten kişi tacirdir. Tescil kurucu değil açıklayıcıdır.",
  "6102 sayılı TTK m.12")

q(T, "tacir_yukumluluklari", "Tacirin Yükümlülükleri",
  "Tacirin 'basiretli bir iş adamı gibi hareket etme' yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Tacir, ticari faaliyetinde ortalama bir kişiden daha yüksek bir özen ölçüsüne uymakla yükümlüdür",
  ["Tacirden beklenen özen, ticari hayatla ilgisi bulunmayan sıradan bir kişiden beklenenle tümüyle aynıdır",
   "Tacir, ticari işlerinde her türlü özen yükümlülüğünden kanunen açıkça muaf tutulmuş durumdadır",
   "Basiretli iş adamı ölçüsü yalnızca sermaye şirketlerini bağlar; gerçek kişi tacirleri kapsamaz",
   "Bu yükümlülük yalnızca tacirin zarar etmesi hâlinde ve geriye dönük olarak uygulama alanı bulur"],
  "TTK m.18/2: her tacirin, ticaretine ait bütün faaliyetlerinde basiretli bir iş adamı gibi hareket etmesi gerekir; bu, ortalama kişiden daha ağır bir özen ölçüsüdür.",
  "6102 sayılı TTK m.18/2")

q(T, "tacir_yukumluluklari", "Tacirin Yükümlülükleri",
  "Ticaret unvanı bakımından aşağıdakilerden hangisi doğrudur?",
  "Her tacir, ticari işletmesine ilişkin işlemleri ticaret unvanıyla yapmak ve unvanını tescil ettirmekle yükümlüdür",
  ["Tacirin ticaret unvanı seçmesi ve kullanması tümüyle isteğe bağlı olup hiçbir yükümlülük doğurmaz",
   "Ticaret unvanı yalnızca sözlü olarak kullanılabilir; sicile tescil edilmesi kanunen yasaklanmıştır",
   "Ticaret unvanı yalnızca anonim şirketlere tanınmış olup diğer tacirler unvan kullanamaz",
   "Tacir her işlemi için farklı bir ticaret unvanı seçmek ve her defasında yeniden tescil ettirmek zorundadır"],
  "TTK m.18, 39: her tacir ticari işletmesine ilişkin işlemleri ticaret unvanıyla yapar ve unvanını ticaret siciline tescil ettirir.",
  "6102 sayılı TTK m.18, 39")

q(T, "tacir_yukumluluklari", "Tacirin Yükümlülükleri",
  "Aşağıdakilerden hangileri tacir olmanın sonuçlarındandır?\n\nI. Ticaret unvanı seçmek ve tescil ettirmek\n\nII. Basiretli bir iş adamı gibi hareket etmek\n\nIII. Ticari işlerinde her türlü özen yükümlülüğünden muaf olmak",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tacir; ticaret unvanı seçip tescil ettirmek (I) ve basiretli iş adamı gibi hareket etmekle (II) yükümlüdür. Özen yükümlülüğünden muafiyet (III) yoktur; aksine tacirden daha ağır özen beklenir. Doğru: I ve II.",
  "6102 sayılı TTK m.18")

q(T, "ticaret_sirketleri", "Ticaret Şirketleri",
  "Aşağıdakilerden hangileri Türk Ticaret Kanunu'na göre sermaye şirketlerindendir?\n\nI. Anonim şirket\n\nII. Limited şirket\n\nIII. Kollektif şirket",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TTK m.124: anonim (I) ve limited (II) şirketler sermaye şirketidir. Kollektif şirket (III) ise bir şahıs şirketi olduğundan sermaye şirketleri arasında yer almaz.",
  "6102 sayılı TTK m.124")

q(T, "ticaret_sirketleri", "Ticaret Şirketleri",
  "Sermaye şirketleri ile şahıs şirketleri arasındaki temel ayrım bakımından aşağıdakilerden hangisi doğrudur?",
  "Sermaye şirketlerinde ortakların sorumluluğu taahhüt ettikleri sermayeyle sınırlıyken, şahıs şirketlerinde ortaklar şirket borcundan şahsen sorumlu olabilir",
  ["Sermaye şirketlerinde ortaklar sınırsız, şahıs şirketlerinde ise sınırlı sorumlu olup bu yönüyle taban tabana zıttırlar",
   "Sermaye şirketlerinde ortakların kişiliği, şahıs şirketlerinde ise konulan sermaye ön planda tutulmaktadır",
   "İki şirket grubu arasında sorumluluk ve yapı bakımından kanunen hiçbir fark öngörülmemiştir",
   "Şahıs şirketlerinde paylar serbestçe devredilirken sermaye şirketlerinde devir kesin olarak yasaktır"],
  "Sermaye şirketlerinde (AŞ, limited, sermayesi paylara bölünmüş komandit) sorumluluk taahhüt edilen sermayeyle sınırlıdır; şahıs şirketlerinde (kollektif, adi komandit) ortakların kişiliği öndedir ve şahsi sorumluluk doğabilir.",
  "6102 sayılı TTK m.124")

q(T, "ticaret_sirketleri", "Ticaret Şirketleri",
  "Kollektif şirkette ortakların sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Ortaklar sınırsız ve müteselsilen sorumludur; ancak şahsi malvarlığına başvuru ikinci derecededir",
  ["Ortakların sorumluluğu koydukları sermaye tutarıyla sınırlı olup şahsi malvarlıkları hiçbir hâlde takip edilemez",
   "Alacaklılar hiçbir sıra gözetmeden, şirkete hiç başvurmadan doğrudan ortakların malvarlığına gidebilir",
   "Kollektif şirkette yalnızca yönetici ortak sorumludur; yönetime katılmayan ortakların sorumluluğu yoktur",
   "Ortaklar yalnızca kendi paylarına düşen bölünmüş kısımdan sorumlu olup müteselsil sorumluluk söz konusu değildir"],
  "TTK m.236-237: kollektif şirkette ortaklar şirket borçlarından sınırsız ve müteselsilen sorumludur; ancak alacaklılar şahsi malvarlığına ancak alacaklarını şirketten tamamen alamazlarsa başvurabilir (ikinci derece sorumluluk).",
  "6102 sayılı TTK m.236-237")

q(T, "ticaret_sirketleri", "Ticaret Şirketleri",
  "Anonim şirkette pay sahibinin 'tek borç ilkesi' bakımından aşağıdakilerden hangisi doğrudur?",
  "Pay sahibinin şirkete karşı tek borcu taahhüt ettiği sermaye payını ödemektir",
  ["Pay sahibi, sermaye borcunun yanında şirketin tüm borçlarından da şahsen ve sınırsız sorumlu tutulur",
   "Pay sahibine esas sözleşmeyle sermaye dışında her türlü ek edim ve borç sınırsızca yüklenebilmektedir",
   "Pay sahibinin şirkete karşı hiçbir borcu bulunmaz; sermaye taahhüdünde bulunması dahi gerekmez",
   "Pay sahibi her yıl taahhüt ettiği sermaye payının iki katını şirkete ödemekle yükümlü kılınmıştır"],
  "TTK m.480: pay sahibinin tek borcu taahhüt ettiği sermaye payını ödemektir; esas sözleşmeyle bunun dışında borç yüklenemez.",
  "6102 sayılı TTK m.480")

q(T, "ticari_defterler", "Ticari Defterler",
  "Ticari defter tutma yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Her tacir, ticari defterleri tutmak ve işletmesinin durumunu bu defterlerden açıkça görülebilecek şekilde ortaya koymakla yükümlüdür",
  ["Ticari defter tutmak yalnızca sermaye şirketlerinin yükümlülüğü olup gerçek kişi tacirleri bağlamaz",
   "Ticari defterlerin tutulması tümüyle tacirin takdirine bırakılmış olup hiçbir kanuni zorunluluk taşımaz",
   "Ticari defterler yalnızca vergi incelemesi başladığında ve geriye dönük olarak düzenlenmek zorundadır",
   "Ticari defterleri tacir değil, yalnızca bağlı bulunduğu ticaret odası tutmak ve saklamakla görevlidir"],
  "TTK m.64: her tacir ticari defterleri tutmak ve işletmesinin iktisadi ve mali durumunu bu defterlerden açıkça görülebilecek biçimde ortaya koymakla yükümlüdür.",
  "6102 sayılı TTK m.64")

q(T, "ticari_defterler", "Ticari Defterler",
  "Ticari defter ve belgelerin saklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Defterler ve saklanması zorunlu belgeler, son kayıt tarihinden itibaren kanunda öngörülen süre (on yıl) boyunca saklanır",
  ["Ticari defterlerin saklanmasına ilişkin hiçbir süre öngörülmemiş olup tacir dilediği zaman imha edebilir",
   "Defterler yalnızca ilgili hesap dönemi kapandığı ana kadar saklanır; sonrasında saklama yükümlülüğü düşer",
   "Ticari defterleri tacir değil, yalnızca ticaret sicili müdürlüğü arşivinde saklamakla görevlendirilmiştir",
   "Saklama süresi her tacir için ayrı ayrı ve bağlı bulunduğu odanın takdirine göre belirlenmektedir"],
  "TTK m.82: ticari defterler ve saklanması zorunlu belgeler, son kayıt tarihinden itibaren on yıl süreyle saklanır.",
  "6102 sayılı TTK m.82")

# ══ BORÇLAR HUKUKU (13) ═══════════════════════════════════════════════════
q(B, "borc_iliskisi", "Borç İlişkisi",
  "Borç ilişkisinin kaynakları bakımından aşağıdakilerden hangisi doğrudur?",
  "Borç ilişkisi sözleşmeden, haksız fiilden veya sebepsiz zenginleşmeden doğabilir",
  ["Borç ilişkisi yalnızca taraflar arasında yazılı bir sözleşme yapılmasıyla ve başka hiçbir yolla doğmaz",
   "Borç ilişkisinin tek kaynağı kanun olup tarafların iradesiyle borç ilişkisi kurulması mümkün değildir",
   "Borç ilişkisi yalnızca bir mahkeme kararıyla doğar; taraflar kendiliğinden borç altına giremez",
   "Haksız fiil ve sebepsiz zenginleşme borç doğurmaz; bunlar yalnızca cezai sonuç doğuran olgulardır"],
  "TBK sistematiğinde borç ilişkisinin kaynakları sözleşme, haksız fiil ve sebepsiz zenginleşmedir.",
  "6098 sayılı TBK m.1 vd.", "easy")

q(B, "borc_iliskisi", "Borç İlişkisi",
  "Borç ilişkisinde 'edim' kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Edim; verme, yapma veya yapmama biçiminde ortaya çıkabilir",
  ["Edim yalnızca bir miktar paranın ödenmesi biçiminde olabilir; başka türlü edim kanunen tanınmaz",
   "Edim yalnızca bir şeyin teslim edilmesi olarak anlaşılır; hizmet görme edim sayılmamaktadır",
   "Bir şeyi yapmaktan kaçınma taahhüdü hiçbir hâlde edim olarak kabul edilmez ve borç doğurmaz",
   "Edimin konusu her hâlde bir taşınmaz olmak zorunda olup taşınır mallar edim konusu yapılamaz"],
  "Edim, borçlunun yerine getirmekle yükümlü olduğu davranıştır ve verme, yapma ya da yapmama (kaçınma) biçiminde olabilir.",
  "6098 sayılı TBK - edim")

q(B, "borc_iliskisi", "Borç İlişkisi",
  "Aşağıdakilerden hangileri borç ilişkisinin kaynaklarındandır?\n\nI. Sözleşme\n\nII. Haksız fiil\n\nIII. Sebepsiz zenginleşme",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TBK sistematiğinde sözleşme (I), haksız fiil (II) ve sebepsiz zenginleşme (III) borç ilişkisinin kaynaklarıdır. Üçü de doğrudur.",
  "6098 sayılı TBK m.1, 49, 77")

q(B, "sozlesmenin_kurulmasi", "Sözleşmenin Kurulması",
  "Sözleşmenin kurulması bakımından aşağıdakilerden hangisi doğrudur?",
  "Sözleşme, tarafların karşılıklı ve birbirine uygun irade açıklamalarıyla kurulur",
  ["Sözleşmenin kurulması için her hâlde yazılı şekil ve noter onayı aranır; sözlü sözleşme geçersizdir",
   "Sözleşme yalnızca taraflardan birinin tek taraflı irade açıklamasıyla ve diğerinin katılımı olmadan kurulur",
   "Sözleşmenin kurulabilmesi için tarafların iradelerinin birbirinden farklı olması gerekli görülmektedir",
   "Sözleşme ancak ticaret siciline tescil edildikten sonra taraflar arasında hüküm ifade etmeye başlar"],
  "TBK m.1: sözleşme, tarafların iradelerini karşılıklı ve birbirine uygun olarak açıklamalarıyla kurulur; açıklama açık veya örtülü olabilir.",
  "6098 sayılı TBK m.1", "easy")

q(B, "sozlesmenin_kurulmasi", "Sözleşmenin Kurulması",
  "Sözleşmelerde şekil serbestisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Sözleşmeler kural olarak hiçbir şekle bağlı değildir; kanunda şekil öngörülen hâller istisnadır",
  ["Bütün sözleşmelerin geçerliliği için istisnasız biçimde yazılı şekil ve resmî onay şartı aranmaktadır",
   "Sözleşmelerde şekil tümüyle serbesttir; kanun hiçbir sözleşme için şekil şartı öngörmemiş durumdadır",
   "Şekil şartı yalnızca tacirler arasındaki sözleşmelerde aranır; diğer kişiler bundan tümüyle muaftır",
   "Kanunda öngörülen şekle uyulmaması sözleşmeyi etkilemez; sözleşme her hâlde geçerli kalmaya devam eder"],
  "TBK m.12: sözleşmelerin geçerliliği kural olarak hiçbir şekle bağlı değildir; kanunda şekil öngörülmüşse bu şekil geçerlilik şartıdır.",
  "6098 sayılı TBK m.12")

q(B, "sozlesmenin_kurulmasi", "Sözleşmenin Kurulması",
  "İrade sakatlığı hâllerinden 'hata' bakımından aşağıdakilerden hangisi doğrudur?",
  "Esaslı hataya düşen taraf sözleşmeyle bağlı olmaz; hatanın esaslı sayıldığı hâller kanunda gösterilmiştir",
  ["Her türlü hata, önemli olup olmadığına bakılmaksızın sözleşmeyi kendiliğinden kesin hükümsüz kılmaktadır",
   "Hataya düşen taraf hiçbir hâlde sözleşmeden kurtulamaz; sözleşmeyle aynen bağlı kalmaya devam eder",
   "Hata yalnızca karşı tarafın kastı bulunduğu hâllerde ileri sürülebilir; kendiliğinden hiçbir sonuç doğurmaz",
   "Hata hâlinde sözleşme ancak mahkemenin resen tespitiyle ve tarafların talebi aranmaksızın ortadan kalkar"],
  "TBK m.30-31: sözleşme kurulurken esaslı hataya düşen taraf sözleşmeyle bağlı olmaz; esaslı hata hâlleri kanunda sayılmıştır.",
  "6098 sayılı TBK m.30-31")

q(B, "sozlesmenin_kurulmasi", "Sözleşmenin Kurulması",
  "Temsil bakımından aşağıdakilerden hangisi doğrudur?",
  "Yetkili temsilcinin temsil olunan adına yaptığı işlemin hukuki sonuçları doğrudan temsil olunana ait olur",
  ["Temsilcinin yaptığı işlemin sonuçları her hâlde temsilcinin şahsında doğar; temsil olunanı hiç bağlamaz",
   "Temsil ilişkisi ancak noterde düzenlenen resmî bir vekâletnameyle kurulabilir; başka yolla doğmaz",
   "Yetkisiz temsilcinin yaptığı işlem, temsil olunanın onayı aranmaksızın kendiliğinden onu bağlar",
   "Temsil yalnızca ticaret şirketlerinde mümkündür; gerçek kişiler arasında temsil ilişkisi kurulamaz"],
  "TBK m.40: yetkili temsilcinin temsil olunan adına ve hesabına yaptığı işlemin sonuçları doğrudan temsil olunana ait olur.",
  "6098 sayılı TBK m.40")

q(B, "borcun_ifasi", "Borcun İfası",
  "Borçlunun temerrüdü bakımından aşağıdakilerden hangisi doğrudur?",
  "Muaccel borcun borçlusu, alacaklının ihtarıyla temerrüde düşer; belirli vade kararlaştırılmışsa ihtara gerek kalmaz",
  ["Borçlu, borç muaccel olur olmaz ve hiçbir koşula bağlı olmaksızın kendiliğinden temerrüde düşmüş sayılır",
   "Borçlunun temerrüde düşmesi için her hâlde mahkemeden bir tespit kararı alınması zorunlu tutulmuştur",
   "Borçlu hiçbir hâlde temerrüde düşmez; temerrüt yalnızca alacaklı bakımından söz konusu olabilen bir kurumdur",
   "Temerrüt için borcun muaccel olması aranmaz; müeccel borçta da borçlu ihtarla temerrüde düşürülebilir"],
  "TBK m.117: muaccel bir borcun borçlusu alacaklının ihtarıyla temerrüde düşer; ifa günü birlikte belirlenmişse veya tek taraflı belirleme hakkı tanınmışsa ihtara gerek olmaksızın temerrüt doğar.",
  "6098 sayılı TBK m.117")

q(B, "borcun_ifasi", "Borcun İfası",
  "Borcun ifa yeri bakımından aşağıdakilerden hangisi doğrudur?",
  "İfa yeri öncelikle tarafların açık veya örtülü iradesine göre belirlenir; aksi hâlde kanuni kurallar uygulanır",
  ["İfa yeri her hâlde ve istisnasız olarak alacaklının yerleşim yeri olarak kanunda kesin biçimde belirlenmiştir",
   "İfa yerini yalnızca mahkeme belirleyebilir; tarafların bu konuda anlaşma yapma yetkisi bulunmamaktadır",
   "İfa yeri kavramı borçlar hukukunda düzenlenmemiş olup uygulamada hiçbir sonuç doğurmayan bir kavramdır",
   "İfa yeri her hâlde borçlunun seçtiği yerdir; alacaklının bu konuda söz söyleme hakkı bulunmamaktadır"],
  "TBK m.89: ifa yeri tarafların açık veya örtülü iradesine göre belirlenir; belirlenmemişse para borçları alacaklının, parça borçları sözleşme kurulduğu sırada şeyin bulunduğu yerde ifa edilir.",
  "6098 sayılı TBK m.89")

q(B, "borcun_ifasi", "Borcun İfası",
  "Borcu sona erdiren sebepler bakımından aşağıdakilerden hangisi doğrudur?",
  "İfa, ibra, yenileme, birleşme, imkânsızlık ve takas borcu sona erdiren sebeplerdendir",
  ["Borç yalnızca ifa ile sona erer; bunun dışında borcu sona erdiren başka bir sebep kanunen tanınmaz",
   "Borç hiçbir sebeple sona ermez; borçlu ölse dahi borç sonsuza kadar varlığını sürdürmeye devam eder",
   "Borcu sona erdiren tek sebep zamanaşımı olup zamanaşımı dolmadıkça borç hiçbir biçimde son bulmaz",
   "Alacaklının borçluyu ibra etmesi borcu sona erdirmez; ibra yalnızca ahlaki bir beyan niteliği taşır"],
  "TBK m.131 vd.: ifa dışında ibra, yenileme, birleşme, kusursuz imkânsızlık, takas ve zamanaşımı gibi sebepler borç ilişkisini sona erdirir veya alacağı zayıflatır.",
  "6098 sayılı TBK m.131 vd.")

q(B, "haksiz_fiil", "Haksız Fiil",
  "Kusura dayanan haksız fiil sorumluluğunun unsurları bakımından aşağıdakilerden hangisi doğrudur?",
  "Hukuka aykırı fiil, kusur, zarar ve fiille zarar arasında uygun illiyet bağı bulunmalıdır",
  ["Yalnızca zararın doğmuş olması yeterlidir; hukuka aykırılık, kusur veya illiyet bağı hiç aranmamaktadır",
   "Kusur aranmaz; her türlü fiilden doğan zarardan fail her hâlde ve kusursuz olarak sorumlu tutulur",
   "İlliyet bağı aranmaz; fiille hiçbir bağlantısı bulunmayan zararlardan dahi fail sorumlu olmaktadır",
   "Hukuka aykırılık aranmaz; hukuka uygun davranıştan doğan zararlar da haksız fiil sorumluluğu doğurur"],
  "TBK m.49: kusurlu ve hukuka aykırı bir fiille başkasına zarar veren bu zararı gidermekle yükümlüdür; sorumluluk için hukuka aykırı fiil, kusur, zarar ve uygun illiyet bağı gerekir.",
  "6098 sayılı TBK m.49")

q(B, "haksiz_fiil", "Haksız Fiil",
  "Kusursuz sorumluluk hâlleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanunda öngörülen bazı hâllerde fail, kusuru bulunmasa dahi doğan zarardan sorumlu tutulur",
  ["Sorumluluk her hâlde kusura dayanır; kanun hiçbir durumda kusursuz sorumluluk öngörmemektedir",
   "Kusursuz sorumluluk yalnızca kamu kurumları bakımından geçerli olup özel kişileri hiç ilgilendirmez",
   "Kusursuz sorumlulukta zarar görenin zararı ispat etmesi dahi aranmaz; zarar varsayılmış kabul edilir",
   "Kusursuz sorumluluk hâlinde illiyet bağı aranmaz; her türlü zarardan sorumluluk kendiliğinden doğar"],
  "TBK m.65-71: hakkaniyet, özen (adam çalıştıran, hayvan bulunduran, yapı maliki) ve tehlike sorumluluğu gibi hâllerde kusur aranmaksızın sorumluluk doğar.",
  "6098 sayılı TBK m.65-71")

q(B, "haksiz_fiil", "Haksız Fiil",
  "Aşağıdakilerden hangileri kusura dayanan haksız fiil sorumluluğunun unsurlarındandır?\n\nI. Hukuka aykırı fiil\n\nII. Zarar\n\nIII. Fail ile zarar gören arasında önceden bir sözleşme bulunması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Hukuka aykırı fiil (I) ve zarar (II) haksız fiilin unsurlarındandır; haksız fiil sorumluluğu için taraflar arasında önceden sözleşme bulunması (III) gerekmez, aksine haksız fiil sözleşme dışı sorumluluktur. Doğru: I ve II.",
  "6098 sayılı TBK m.49")

# ══ İŞ VE SOSYAL GÜVENLİK HUKUKU (14) ═════════════════════════════════════
q(I, "is_sozlesmesi", "İş Sözleşmesi",
  "İş sözleşmesinin tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşçinin bağımlı olarak iş görmeyi, işverenin de ücret ödemeyi üstlendiği sözleşmedir",
  ["İşçinin hiçbir bağımlılık ilişkisi olmaksızın ve tümüyle bağımsız biçimde iş görmeyi üstlendiği sözleşmedir",
   "Tarafların karşılıklı olarak bir mal teslim etmeyi üstlendikleri ve ücret öğesi bulunmayan bir sözleşmedir",
   "İşverenin işçiye ücret ödemeksizin yalnızca eğitim vermeyi taahhüt ettiği karşılıksız bir anlaşmadır",
   "Yalnızca kamu kurumlarıyla memurlar arasında kurulabilen ve özel sektörde uygulanmayan bir sözleşmedir"],
  "İş Kanunu m.8: iş sözleşmesi, işçinin bağımlı olarak iş görmeyi, işverenin de ücret ödemeyi üstlenmesinden oluşan sözleşmedir. Bağımlılık iş sözleşmesinin ayırt edici unsurudur.",
  "4857 sayılı İş Kanunu m.8", "easy")

q(I, "is_sozlesmesi", "İş Sözleşmesi",
  "Belirli ve belirsiz süreli iş sözleşmesi ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Belirli süreli iş sözleşmesi ancak objektif koşulların varlığı hâlinde yapılabilir; esaslı neden olmadıkça zincirleme yapılamaz",
  ["Belirli süreli iş sözleşmesi hiçbir koşul aranmaksızın ve sınırsız sayıda zincirleme olarak yenilenebilir",
   "İş sözleşmesi her hâlde belirli süreli yapılmak zorundadır; belirsiz süreli sözleşme kanunen tanınmaz",
   "Belirli süreli iş sözleşmesi kanunda hiç düzenlenmemiş olup uygulamada geçersiz kabul edilmektedir",
   "Belirli ve belirsiz süreli sözleşmeler arasında hukuki sonuç bakımından hiçbir fark bulunmamaktadır"],
  "İş Kanunu m.11: belirli süreli iş sözleşmesi, işin süresi veya belirli bir işin tamamlanması gibi objektif koşullara bağlı olarak yapılabilir; esaslı neden olmadıkça zincirleme yapılamaz, aksi hâlde baştan itibaren belirsiz süreli sayılır.",
  "4857 sayılı İş Kanunu m.11")

q(I, "is_sozlesmesi", "İş Sözleşmesi",
  "İş sözleşmesinde deneme süresi bakımından aşağıdakilerden hangisi doğrudur?",
  "Deneme süresi en çok iki ay olarak kararlaştırılabilir; toplu iş sözleşmesiyle dört aya kadar uzatılabilir",
  ["Deneme süresi taraflarca sınırsız biçimde ve diledikleri kadar uzun olarak kararlaştırılabilmektedir",
   "İş sözleşmesinde deneme süresi kararlaştırılması kanunen tümüyle yasaklanmış bir uygulamadır",
   "Deneme süresi içinde taraflar sözleşmeyi hiçbir hâlde feshedemez; süre dolmadan fesih mümkün değildir",
   "Deneme süresi yalnızca işvereni bağlar; işçi bu süre içinde sözleşmeyi feshetme hakkına sahip değildir"],
  "İş Kanunu m.15: deneme süresi en çok iki ay olabilir; toplu iş sözleşmeleriyle dört aya kadar uzatılabilir. Bu süre içinde taraflar bildirim süresine gerek olmaksızın ve tazminatsız feshedebilir.",
  "4857 sayılı İş Kanunu m.15")

q(I, "esit_davranma", "Eşit Davranma İlkesi",
  "İşverenin eşit davranma borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "İşveren, esaslı bir neden olmadıkça işçiler arasında ayrım yapamaz",
  ["İşveren işçiler arasında dilediği gibi ayrım yapabilir; eşit davranma yönünde hiçbir yükümlülüğü yoktur",
   "Eşit davranma borcu yalnızca kamu işverenlerini bağlar; özel sektör işverenleri bundan tümüyle muaftır",
   "İşveren esaslı neden bulunsa dahi hiçbir biçimde işçiler arasında farklı uygulama yapamamaktadır",
   "Eşit davranma ilkesi yalnızca ücret konusunda geçerli olup çalışma koşullarını hiç kapsamamaktadır"],
  "İş Kanunu m.5: işveren, esaslı sebepler olmadıkça tam süreli-kısmi süreli veya belirli-belirsiz süreli çalışan işçiler arasında farklı işlem yapamaz; dil, ırk, cinsiyet gibi sebeplere dayalı ayrım yasaktır.",
  "4857 sayılı İş Kanunu m.5", "easy")

q(I, "esit_davranma", "Eşit Davranma İlkesi",
  "Eşit davranma ilkesine aykırılığın yaptırımı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşçi, ayrımcılık tazminatı ile yoksun bırakıldığı haklarını talep edebilir",
  ["Eşit davranma ilkesine aykırılığın hiçbir hukuki yaptırımı bulunmamakta olup yalnızca ahlaki bir sorun sayılır",
   "İlkeye aykırılık hâlinde iş sözleşmesi kendiliğinden ve geriye etkili biçimde tümüyle geçersiz hâle gelir",
   "İşçi yalnızca işten ayrılabilir; ayrımcılık nedeniyle herhangi bir tazminat talep etme hakkı bulunmaz",
   "Yaptırım yalnızca idari para cezası olup işçinin kişisel bir talep hakkı doğmamaktadır"],
  "İş Kanunu m.5: eşit davranma ilkesine aykırı davranıldığında işçi, dört aya kadar ücreti tutarındaki ayrımcılık tazminatı ile yoksun bırakıldığı hakları talep edebilir.",
  "4857 sayılı İş Kanunu m.5")

q(I, "calisma_sureleri", "Çalışma Süreleri",
  "İş Kanunu'na göre haftalık çalışma süresi bakımından aşağıdakilerden hangisi doğrudur?",
  "Genel bakımdan çalışma süresi haftada en çok kırk beş saattir; aksi kararlaştırılmadıkça günlere eşit bölünür",
  ["Haftalık çalışma süresi kanunda hiç düzenlenmemiş olup tümüyle tarafların anlaşmasına bırakılmıştır",
   "Haftalık çalışma süresi genel bakımdan en çok altmış saat olarak kanunda açıkça belirlenmiş durumdadır",
   "Çalışma süresi her hâlde günde sekiz saat olmak zorunda olup hiçbir biçimde farklı dağıtılamaz",
   "Haftalık çalışma süresi yalnızca kamu işyerlerinde geçerli olup özel sektörü hiç bağlamamaktadır"],
  "İş Kanunu m.63: genel bakımdan çalışma süresi haftada en çok kırk beş saattir; aksi kararlaştırılmamışsa bu süre işyerinde haftanın çalışılan günlerine eşit ölçüde bölünerek uygulanır.",
  "4857 sayılı İş Kanunu m.63")

q(I, "calisma_sureleri", "Çalışma Süreleri",
  "Fazla çalışma bakımından aşağıdakilerden hangisi doğrudur?",
  "Haftalık kırk beş saati aşan çalışmalar fazla çalışmadır; yılda toplam iki yüz yetmiş saati aşamaz",
  ["Fazla çalışma için kanunda hiçbir üst sınır öngörülmemiş olup işveren sınırsız fazla çalışma yaptırabilir",
   "Fazla çalışma kanunen tümüyle yasak olup hiçbir koşulda ve hiçbir işyerinde yaptırılamamaktadır",
   "Fazla çalışma karşılığında işçiye herhangi bir zamlı ücret veya serbest zaman hakkı doğmamaktadır",
   "Fazla çalışma yalnızca işçinin talebiyle yapılır; işverenin bu konuda hiçbir inisiyatifi bulunmaz"],
  "İş Kanunu m.41: haftalık kırk beş saati aşan çalışmalar fazla çalışmadır; her bir saat fazla çalışma için normal saat ücretinin yüzde elli fazlası ödenir ve fazla çalışma yılda iki yüz yetmiş saatten fazla olamaz.",
  "4857 sayılı İş Kanunu m.41")

q(I, "calisma_sureleri", "Çalışma Süreleri",
  "İş Kanunu'na göre çalışma sürelerine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel bakımdan haftalık çalışma süresi en çok kırk beş saattir\n\nII. Denkleştirmede günlük çalışma on bir saati geçemez\n\nIII. Denkleştirme işverenin tek taraflı kararıyla uygulanır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Haftalık süre en çok kırk beş saattir (I) ve denkleştirmede günlük çalışma on bir saati aşamaz (II). Ancak denkleştirme tarafların anlaşmasına bağlıdır, işverenin tek taraflı kararıyla uygulanamaz; bu nedenle III yanlıştır.",
  "4857 sayılı İş Kanunu m.63")

q(I, "yillik_izin", "Yıllık Ücretli İzin",
  "Yıllık ücretli izne hak kazanma bakımından aşağıdakilerden hangisi doğrudur?",
  "İşyerinde işe başladığı günden itibaren, deneme süresi de içinde olmak üzere en az bir yıl çalışmış olmak gerekir",
  ["Yıllık ücretli izne hak kazanmak için hiçbir kıdem koşulu aranmaz; işçi ilk günden izin talep edebilir",
   "Yıllık izne hak kazanmak için işyerinde en az on yıl kesintisiz çalışmış olma koşulu aranmaktadır",
   "Yıllık ücretli izin yalnızca işverenin takdirine bağlı bir lütuf olup işçinin talep hakkı bulunmaz",
   "Deneme süresinde geçen süre kıdemden sayılmaz; bir yıllık süre deneme bittikten sonra işlemeye başlar"],
  "İş Kanunu m.53: işyerinde işe başladığı günden itibaren, deneme süresi de içinde olmak üzere en az bir yıl çalışmış olan işçilere yıllık ücretli izin verilir.",
  "4857 sayılı İş Kanunu m.53")

q(I, "yillik_izin", "Yıllık Ücretli İzin",
  "Yıllık ücretli izin süreleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İzin süresi hizmet süresine göre kademelendirilmiştir ve kanunda öngörülen asgari sürelerin altına inilemez",
  ["Yıllık izin süresi her işçi için kıdemine bakılmaksızın tümüyle aynı ve sabit olarak belirlenmiştir",
   "İzin süreleri tümüyle işverenin takdirinde olup kanunda herhangi bir asgari süre öngörülmemiştir",
   "Sözleşmeyle kanuni izin sürelerinin altına inilebilir; kanuni süreler yalnızca tavsiye niteliğindedir",
   "Yıllık izin süresi yalnızca toplu iş sözleşmesi bulunan işyerlerinde uygulanır; diğerlerinde izin yoktur"],
  "İş Kanunu m.53: yıllık izin süreleri hizmet süresine göre kademelendirilmiştir (bir-beş yıl arası on dört, beş-on beş yıl arası yirmi, on beş yıl ve fazlası yirmi altı günden az olamaz); bu süreler sözleşmelerle artırılabilir ancak azaltılamaz.",
  "4857 sayılı İş Kanunu m.53")

q(I, "yillik_izin", "Yıllık Ücretli İzin",
  "Yıllık ücretli iznin kullanılması bakımından aşağıdakilerden hangisi doğrudur?",
  "İzin kural olarak bölünemez; ancak tarafların anlaşmasıyla bir bölümü en az on gün olmak üzere bölümler hâlinde kullanılabilir",
  ["Yıllık izin her hâlde ve istisnasız olarak tek seferde ve kesintisiz biçimde kullanılmak zorundadır",
   "Yıllık izin işveren tarafından dilediği kadar küçük parçalara bölünerek sınırsızca kullandırılabilir",
   "Yıllık izin hiçbir hâlde kullanılamaz; yalnızca ücrete çevrilerek işçiye ödenmesi mümkün olabilir",
   "İşçi çalışırken yıllık izin ücretini nakden talep edebilir ve izin kullanmaktan tümüyle vazgeçebilir"],
  "İş Kanunu m.56: yıllık ücretli izin işveren tarafından bölünemez; ancak tarafların anlaşmasıyla bir bölümü on günden aşağı olmamak üzere bölümler hâlinde kullanılabilir. İş sözleşmesi devam ederken izin ücrete çevrilemez.",
  "4857 sayılı İş Kanunu m.56")

q(I, "sosyal_guvenlik", "Sosyal Güvenlik",
  "5510 sayılı Kanun'un 4/1-(a) bendi kapsamındaki sigortalılık bakımından aşağıdakilerden hangisi doğrudur?",
  "Hizmet akdiyle bir veya birden fazla işveren tarafından çalıştırılanlar bu kapsamda sigortalı sayılır",
  ["Bu kapsamda yalnızca kendi nam ve hesabına bağımsız çalışanlar sigortalı olarak kabul edilmektedir",
   "Bu bent yalnızca kamu idarelerinde memur statüsünde görev yapanları kapsamına almış durumdadır",
   "Hizmet akdiyle çalışanlar hiçbir sigortalılık kapsamına girmez; yalnızca isteğe bağlı sigorta yaptırabilir",
   "Bu kapsamda sigortalılık yalnızca işçinin kendi talebiyle ve isteğe bağlı olarak başlatılabilmektedir"],
  "5510 sayılı Kanun m.4/1-(a): hizmet akdi ile bir veya birden fazla işveren tarafından çalıştırılanlar bu bent kapsamında sigortalı sayılır.",
  "5510 sayılı Kanun m.4/1-(a)")

q(I, "sosyal_guvenlik", "Sosyal Güvenlik",
  "Sigortalı işe giriş bildirgesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşveren, çalıştıracağı sigortalıyı kanunda öngörülen süre içinde ve kural olarak çalışmaya başlamadan önce Kuruma bildirmekle yükümlüdür",
  ["İşe giriş bildirgesinin verilmesi tümüyle isteğe bağlı olup hiçbir kanuni süre veya yükümlülük öngörülmemiştir",
   "Bildirge yükümlülüğü işverene değil, doğrudan sigortalının kendisine ait olan bir yükümlülüktür",
   "İşe giriş bildirgesi ancak sigortalının işten ayrılmasından sonra geriye dönük olarak verilebilmektedir",
   "Bildirge yalnızca kamu işyerleri için zorunlu olup özel sektör işverenleri bu yükümlülükten muaftır"],
  "5510 sayılı Kanun m.8: işveren, 4/1-(a) kapsamında sigortalı sayılanları kanunda öngörülen süreler içinde ve kural olarak çalışmaya başlatılmadan önce sigortalı işe giriş bildirgesiyle Kuruma bildirmekle yükümlüdür.",
  "5510 sayılı Kanun m.8")

q(I, "sosyal_guvenlik", "Sosyal Güvenlik",
  "Aşağıdakilerden hangileri işverenin sosyal güvenlik mevzuatından doğan yükümlülüklerindendir?\n\nI. Sigortalıyı işe giriş bildirgesiyle Kuruma bildirmek\n\nII. Prim belgelerini süresinde vermek ve primleri ödemek\n\nIII. Sigortalının primlerini bizzat sigortalının Kuruma yatırması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "İşveren sigortalıyı işe giriş bildirgesiyle bildirmek (I) ve prim belgelerini süresinde verip primleri ödemekle (II) yükümlüdür. Primleri Kuruma yatırma yükümlülüğü sigortalıya değil işverene aittir; bu nedenle III yanlıştır.",
  "5510 sayılı Kanun m.8, 86")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    """n soru için dengeli + örüntüsüz harf dizisi (n, 5'in katı olmak zorunda değil)."""
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base

def emit(items, prefix, seed):
    letters = gen_letters(len(items), seed)
    out = []
    for i, it in enumerate(items):
        ans = letters[i]
        choices = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            choices[k] = d
        out.append({
            "id": f"{prefix}-{i+1:04d}",
            "lessonId": it["lesson"], "topicId": it["topic"],
            "question": it["stem"], "choices": choices, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", it["label"]],
            "difficulty": it["difficulty"],
            "updatedAt": "2026-07-15T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu",
            "legislationVersion": "2026-07-15",
            "sourceUpdatedAt": "2026-07-15T00:00:00Z",
            "isPremium": False, "isActive": True,
        })
    return out

if __name__ == "__main__":
    assert len(Q) == 40, f"40 olmalı, şu an {len(Q)}"
    # Her testte üç ders de, öncüllüler de dengeli temsil edilsin.
    # Öncüllü ve normal soruları AYRI AYRI dönüşümlü dağıt (yoksa öncüllüler
    # tek dosyada yığılıyor — i%2 bölmesi bunu yapmıştı).
    import re as _re
    MARK = _re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in Q if len(MARK.findall(x["stem"])) >= 2]
    duz = [x for x in Q if len(MARK.findall(x["stem"])) < 2]
    t2 = [x for i, x in enumerate(duz) if i % 2 == 0] + [x for i, x in enumerate(onc) if i % 2 == 0]
    t3 = [x for i, x in enumerate(duz) if i % 2 == 1] + [x for i, x in enumerate(onc) if i % 2 == 1]
    print(f"öncüllü toplam {len(onc)} → t2:{sum(1 for x in t2 if x in onc)} t3:{sum(1 for x in t3 if x in onc)}")
    APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik"
    for items, name, prefix, seed in ((t2, "questions_hukuk_test2_2026.json", "hukuk-t2", 20260801),
                                      (t3, "questions_hukuk_test3_2026.json", "hukuk-t3", 20260802)):
        data = emit(items, prefix, seed)
        json.dump(data, open(f"{APP}/{name}", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        seq = "".join(x["correctAnswer"] for x in data)
        print(f"{name}: {len(data)} soru | harf {seq}")
