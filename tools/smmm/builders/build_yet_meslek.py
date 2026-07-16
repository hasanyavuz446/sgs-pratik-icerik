# -*- coding: utf-8 -*-
"""Yeterlilik — Meslek Hukuku Test 2 + Test 3 (2×20 = 40 soru).
3568 sayılı Kanun + TÜRMOB/TESMER + Etik. Doğru şık KISA, çeldiriciler UZUN.
⚠️ Ücret tarifesi TUTARI, staj süresi dışındaki yıla bağlı değerler YOK.
explanation'da harf atıfı YOK."""
import json, random, re

L = "meslek_hukuku"
Q = []
def q(topic, label, stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(topic=topic, label=label, stem=stem, correct=correct, distractors=distractors,
                  why=why, ref=ref, difficulty=difficulty))

# ══ MESLEK VE UNVANLAR (6) ════════════════════════════════════════════════
q("meslek_ve_unvanlar", "Meslek ve Unvanlar",
  "3568 sayılı Kanun'a göre meslek unvanları bakımından aşağıdakilerden hangisi doğrudur?",
  "Serbest Muhasebeci Mali Müşavir ve Yeminli Mali Müşavir olmak üzere iki meslek unvanı bulunur",
  ["Kanunda tek bir meslek unvanı öngörülmüş olup tüm meslek mensupları aynı unvanı taşımaktadır",
   "Meslek unvanları kanunda sayılmamış olup meslek mensupları diledikleri unvanı serbestçe kullanır",
   "Yeminli mali müşavirlik bir unvan değil, yalnızca serbest muhasebeci mali müşavirlerin bir göreviridir",
   "Meslek unvanları yalnızca TÜRMOB tarafından her yıl yeniden belirlenen değişken adlandırmalardır"],
  "3568 sayılı Kanun m.1-2: mesleğin konusu ve unvanları düzenlenmiştir; Serbest Muhasebeci Mali Müşavir (SMMM) ve Yeminli Mali Müşavir (YMM) olmak üzere iki meslek unvanı vardır.",
  "3568 sayılı Kanun m.1-2", "easy")

q("meslek_ve_unvanlar", "Meslek ve Unvanlar",
  "Serbest muhasebeci mali müşavirlerin yapabileceği işler bakımından aşağıdakilerden hangisi doğrudur?",
  "Muhasebe sistemi kurmak, defter tutmak, mali tablo düzenlemek ile denetim, danışmanlık ve bilirkişilik yapabilirler",
  ["Yalnızca defter tutabilirler; danışmanlık ve mali tablo düzenleme yetkileri bulunmamaktadır",
   "Yalnızca vergi beyannamesi imzalayabilirler; muhasebe sistemi kurma yetkileri kanunen yasaktır",
   "Meslek mensuplarının yapabileceği işler kanunda sayılmamış olup her mensup dilediği işi yapabilir",
   "Yalnızca tasdik (tam tasdik) işi yapabilirler; defter tutmaları kanunen kendilerine yasaklanmıştır"],
  "3568 sayılı Kanun m.2: SMMM'ler gerçek ve tüzel kişilere ait teşebbüs ve işletmelerin muhasebe sistemlerini kurmak, defterlerini tutmak, mali tablolarını düzenlemek ile bunlarla ilgili işlerde denetim, danışmanlık, bilirkişilik ve benzeri işleri yapabilir.",
  "3568 sayılı Kanun m.2")

q("meslek_ve_unvanlar", "Meslek ve Unvanlar",
  "Yeminli mali müşavirlerin tasdik yetkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Tasdik işi yalnızca yeminli mali müşavirlere aittir; YMM'ler defter tutamaz ve muhasebe bürosu açamaz",
  ["Tasdik işini hem YMM'ler hem SMMM'ler yapabilir; ikisi arasında bu bakımdan fark bulunmamaktadır",
   "YMM'ler tasdik yetkisinin yanında defter de tutabilir; muhasebe bürosu açmalarında engel yoktur",
   "Tasdik yetkisi yalnızca serbest muhasebeci mali müşavirlere ait olup YMM'ler tasdik yapamamaktadır",
   "Tasdik yetkisi kanunda düzenlenmemiş olup uygulamada her meslek mensubunca serbestçe kullanılır"],
  "3568 sayılı Kanun m.2, 12: tasdik işi YMM'lere aittir. YMM'ler muhasebe ile ilgili defter tutamaz, muhasebe bürosu açamaz ve bu bürolara ortak olamazlar; bu, tasdik işinin tarafsızlığını korumaya yöneliktir.",
  "3568 sayılı Kanun m.2, 12")

q("meslek_ve_unvanlar", "Meslek ve Unvanlar",
  "Meslek mensuplarının çalışma biçimi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensupları mesleklerini serbest olarak ya da bir işverene bağlı çalışarak icra edebilir; ancak ikisi birlikte yapılamaz",
  ["Meslek mensupları yalnızca bir işverene bağlı olarak çalışabilir; serbest çalışmaları yasaklanmıştır",
   "Meslek mensupları yalnızca serbest çalışabilir; hiçbir hâlde bağımlı olarak istihdam edilemezler",
   "Meslek mensupları serbest çalışmayı ve bağımlı çalışmayı aynı anda ve sınırsızca yürütebilmektedir",
   "Meslek mensuplarının çalışma biçimi kanunda düzenlenmemiş olup tümüyle serbest bırakılmıştır"],
  "3568 sayılı Kanun: meslek mensupları mesleği serbest olarak (kendi ad ve hesabına büro açarak) veya bir işverene bağlı olarak icra edebilir. Serbest meslek faaliyeti ile bağımlı çalışma birlikte yürütülemez.",
  "3568 sayılı Kanun - çalışma biçimi")

q("meslek_ve_unvanlar", "Meslek ve Unvanlar",
  "Meslek unvanlarının kullanılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanunda öngörülen şartları taşımayan ve ruhsat almayan kişiler meslek unvanlarını kullanamaz",
  ["Meslek unvanları serbestçe kullanılabilir; ruhsat almayan kişilerin de unvan kullanması mümkündür",
   "Meslek unvanını kullanmak için yalnızca ilgili odaya bir dilekçe vermek yeterli görülmektedir",
   "Meslek unvanı yalnızca meslek mensubunun kartvizitinde kullanılabilir; başka yerde kullanılamaz",
   "Unvan kullanımına ilişkin kanunda hiçbir kısıtlama bulunmayıp konu tümüyle serbest bırakılmıştır"],
  "3568 sayılı Kanun m.3: kanunun öngördüğü şartları taşımayan ve ruhsat almamış kişiler SMMM veya YMM unvanlarını ya da bu unvanları çağrıştıracak ibareleri kullanamaz; aksi hâlde kanuni yaptırım uygulanır.",
  "3568 sayılı Kanun m.3")

q("meslek_ve_unvanlar", "Meslek ve Unvanlar",
  "Aşağıdakilerden hangileri 3568 sayılı Kanun'a göre doğrudur?\n\nI. Meslek unvanları SMMM ve YMM'dir\n\nII. Tasdik işi YMM'lere aittir\n\nIII. YMM'ler muhasebe bürosu açıp defter tutabilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kanunda iki meslek unvanı vardır (I) ve tasdik işi YMM'lere aittir (II). Ancak YMM'ler muhasebe ile ilgili defter tutamaz ve muhasebe bürosu açamaz; bu nedenle III yanlıştır. Doğru: I ve II.",
  "3568 sayılı Kanun m.1-2, 12")

# ══ RUHSAT, SINAV VE STAJ (6) ═════════════════════════════════════════════
q("ruhsat_ve_staj", "Ruhsat, Sınav ve Staj",
  "Serbest muhasebeci mali müşavir olabilmenin genel şartları bakımından aşağıdakilerden hangisi doğrudur?",
  "Türk vatandaşı olmak, medeni hakları kullanma ehliyeti ve kanunda sayılan suçlardan hüküm giymemiş olmak aranır",
  ["Meslek mensubu olmak için hiçbir genel şart aranmaz; yalnızca sınavda başarılı olmak yeterlidir",
   "Genel şartlar arasında yalnızca belirli bir yaşın doldurulması bulunmakta olup başka koşul yoktur",
   "Genel şartlar her yıl TÜRMOB tarafından yeniden ve serbestçe belirlenen değişken ölçütlerdir",
   "Meslek mensubu olabilmek için yalnızca bir meslek mensubunun yanında çalışıyor olmak yeterlidir"],
  "3568 sayılı Kanun m.4: meslek mensubu olabilmenin genel şartları; Türk vatandaşı olmak, medeni hakları kullanma ehliyetine sahip bulunmak, kamu haklarından mahrum bulunmamak, kanunda sayılan suçlardan hüküm giymemiş olmak ve ceza/disiplin soruşturması sonucu memuriyetten çıkarılmamış olmaktır.",
  "3568 sayılı Kanun m.4")

q("ruhsat_ve_staj", "Ruhsat, Sınav ve Staj",
  "Serbest muhasebeci mali müşavirlik stajı bakımından aşağıdakilerden hangisi doğrudur?",
  "Staj süresi üç yıl olup staja başlayabilmek için staja giriş sınavında başarılı olmak gerekir",
  ["Staj süresi bir yıl olup staja başlamak için herhangi bir sınavda başarılı olmak gerekmemektedir",
   "Staj yapmaksızın doğrudan yeterlilik sınavına girilebilir; staj kanunen zorunlu tutulmamıştır",
   "Staj süresi kanunda belirlenmemiş olup her aday dilediği kadar staj yaparak sınava girebilir",
   "Staja giriş sınavı yalnızca yeminli mali müşavir adayları için öngörülmüş bir sınav türüdür"],
  "3568 sayılı Kanun m.5, 6: SMMM olabilmek için staja giriş sınavını kazanarak meslek mensubu yanında veya kanunda öngörülen yerlerde üç yıl staj yapmak ve SMMM sınavını başarmak gerekir.",
  "3568 sayılı Kanun m.5-6")

q("ruhsat_ve_staj", "Ruhsat, Sınav ve Staj",
  "Yeminli mali müşavir olabilmenin özel şartları bakımından aşağıdakilerden hangisi doğrudur?",
  "En az on yıl serbest muhasebeci mali müşavirlik yapmış olmak ve yeminli mali müşavirlik sınavını vermek gerekir",
  ["Yeminli mali müşavir olmak için serbest muhasebeci mali müşavirlik yapmış olmak şartı aranmamaktadır",
   "Yeminli mali müşavirlik sınavı bulunmayıp bu unvan yalnızca kıdeme göre kendiliğinden kazanılmaktadır",
   "Yeminli mali müşavir olmak için yalnızca bir yıl mesleki deneyim ve TÜRMOB onayı yeterli görülmektedir",
   "Yeminli mali müşavirlik doğrudan üniversite mezuniyetiyle ve staj yapılmaksızın kazanılabilen bir unvandır"],
  "3568 sayılı Kanun m.9: YMM olabilmek için en az on yıl SMMM'lik yapmış olmak, YMM sınavını vermek ve YMM ruhsatını almak gerekir. Kanunda öngörülen istisnai hâller saklıdır.",
  "3568 sayılı Kanun m.9")

q("ruhsat_ve_staj", "Ruhsat, Sınav ve Staj",
  "TESMER'in görevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Staj, sınav ve mesleki eğitim faaliyetlerini yürütmek üzere TÜRMOB bünyesinde kurulmuş bir merkezdir",
  ["Meslek mensuplarının disiplin soruşturmasını yürüten ve ceza veren bağımsız bir kuruldur",
   "Meslek mensuplarının ücret tarifesini belirleyip yürürlüğe koyan bir kamu kurumu niteliğindedir",
   "Bağımsız denetim kuruluşlarını yetkilendiren ve denetleyen bir kamu otoritesi olarak görev yapar",
   "Meslek mensuplarının vergi beyannamelerini inceleyen ve onaylayan bir idari birim olarak çalışır"],
  "TESMER (Temel Eğitim ve Staj Merkezi), TÜRMOB bünyesinde kurulmuş olup staj, sınav ve mesleki eğitim faaliyetlerini yürütür.",
  "3568 sayılı Kanun - TESMER")

q("ruhsat_ve_staj", "Ruhsat, Sınav ve Staj",
  "Ruhsat bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanuni şartları taşıyan ve sınavı başaranlara ilgili unvana ait ruhsat verilir; mesleki faaliyet ruhsatla icra edilir",
  ["Ruhsat kavramı kanunda düzenlenmemiş olup meslek sınavı kazanmak tek başına yeterli görülmektedir",
   "Ruhsat yalnızca yeminli mali müşavirlere verilir; serbest muhasebeci mali müşavirler ruhsatsız çalışır",
   "Ruhsat her yıl yenilenmek zorunda olup yenilenmediği takdirde kendiliğinden geçersiz hâle gelmektedir",
   "Ruhsat, meslek mensubunun bağlı olduğu işverence düzenlenip ilgili odaya bildirilen bir belgedir"],
  "3568 sayılı Kanun: kanuni şartları taşıyan ve ilgili sınavı başaranlara SMMM veya YMM ruhsatı verilir; mesleki faaliyet bu ruhsata ve odaya kayda dayalı olarak icra edilir.",
  "3568 sayılı Kanun - ruhsat")

q("ruhsat_ve_staj", "Ruhsat, Sınav ve Staj",
  "Aşağıdakilerden hangileri serbest muhasebeci mali müşavir olabilmek için gereklidir?\n\nI. Staja giriş sınavında başarılı olmak\n\nII. Üç yıl staj yapmak\n\nIII. On yıl yeminli mali müşavirlik yapmış olmak",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "SMMM olmak için staja giriş sınavı (I) ve üç yıllık staj (II) gereklidir. On yıl SMMM'lik yapmış olmak ise YMM olmanın şartıdır; üstelik ifade tersine kurulmuştur. Bu nedenle III yanlıştır. Doğru: I ve II.",
  "3568 sayılı Kanun m.4-6, 9")

# ══ MESLEKİ SORUMLULUK (6) ════════════════════════════════════════════════
q("mesleki_sorumluluk", "Mesleki Sorumluluklar",
  "Beyanname imzalayan meslek mensubunun sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Beyannamedeki bilgilerin defter kayıtlarına ve belgelere uygunluğundan; aykırılıktan doğan vergi ziyaından mükellefle birlikte sorumludur",
  ["Beyanname imzalayan meslek mensubunun hiçbir sorumluluğu doğmaz; sorumluluk tümüyle mükellefe aittir",
   "Meslek mensubu, mükellefin kendisinden gizlediği hususlardan dahi her hâlde ve sınırsız sorumludur",
   "Meslek mensubunun sorumluluğu yalnızca disiplin cezasıyla sınırlı olup mali sorumluluğu bulunmaz",
   "Beyanname imzalayan meslek mensubu, mükellefin tüm vergi borcunu kendi malvarlığından ödemekle yükümlüdür"],
  "VUK mükerrer m.227: beyannameyi imzalayan meslek mensupları, imzaladıkları beyannamelerde yer alan bilgilerin defter kayıtlarına ve bu kayıtların dayanağını oluşturan belgelere uygun olmamasından doğan vergi ziyaına bağlı amme alacaklarından mükellefle birlikte müştereken ve müteselsilen sorumludur.",
  "213 sayılı VUK mük. m.227")

q("mesleki_sorumluluk", "Mesleki Sorumluluklar",
  "Tasdik yapan yeminli mali müşavirin sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Tasdik ettiği belgelerin gerçeğe aykırı olmasından doğan vergi ziyaı ve cezalardan mükellefle birlikte sorumludur",
  ["Tasdik yapan YMM'nin hiçbir sorumluluğu bulunmayıp tasdik yalnızca biçimsel bir onay işlemidir",
   "YMM'nin sorumluluğu yalnızca tasdik ücretini iade etmekle sınırlı olup vergi sorumluluğu doğmaz",
   "Tasdik sorumluluğu yalnızca mükellefe ait olup YMM hiçbir hâlde sorumlu tutulamamaktadır",
   "YMM tasdik ettiği belgelerden yalnızca beş yıl sonra ve yalnızca disiplin yönünden sorumlu olur"],
  "3568 sayılı Kanun m.12: YMM'ler yaptıkları tasdikin doğruluğundan sorumludur; tasdik ettikleri belgelerin gerçeğe aykırı olması hâlinde ziyaa uğratılan vergilerden ve kesilecek cezalardan mükellefle birlikte müştereken ve müteselsilen sorumlu olurlar.",
  "3568 sayılı Kanun m.12")

q("mesleki_sorumluluk", "Mesleki Sorumluluklar",
  "Meslek mensubunun sorumluluk türleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubunun disiplin, hukuki (tazminat), mali ve cezai sorumluluğu birlikte söz konusu olabilir",
  ["Meslek mensubunun yalnızca disiplin sorumluluğu bulunur; hukuki ve cezai sorumluluk söz konusu değildir",
   "Meslek mensubunun tek sorumluluğu ücretini iade etmek olup başka bir yaptırıma tabi tutulamamaktadır",
   "Meslek mensubu yalnızca ceza mahkemesinde yargılanır; disiplin ve tazminat sorumluluğu bulunmaz",
   "Sorumluluk türleri kanunda düzenlenmemiş olup uygulamada odanın takdirine bırakılmış durumdadır"],
  "Meslek mensubunun; meslek kurallarına aykırılıktan disiplin, müşteriye verdiği zarardan hukuki (tazminat), vergi mevzuatından doğan mali (müşterek-müteselsil) ve suç oluşturan fiillerden cezai sorumluluğu birlikte doğabilir.",
  "3568 sayılı Kanun - sorumluluk türleri")

q("mesleki_sorumluluk", "Mesleki Sorumluluklar",
  "Meslek mensubunun sır saklama yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensupları ve yanlarında çalışanlar, işleri dolayısıyla öğrendikleri bilgileri kanunda öngörülen hâller dışında açıklayamaz",
  ["Meslek mensubu öğrendiği bilgileri hiçbir hâlde ve hiçbir mercie açıklayamaz; istisnası bulunmamaktadır",
   "Sır saklama yükümlülüğü yalnızca meslek mensubunu bağlar; yanında çalışanlar bu yükümlülüğün dışındadır",
   "Sır saklama yükümlülüğü müşteri ilişkisi sona erdiğinde kendiliğinden ortadan kalkmış olmaktadır",
   "Sır saklama yalnızca yazılı bilgileri kapsar; sözlü öğrenilen bilgiler bu kapsamda değerlendirilmez"],
  "3568 sayılı Kanun m.43: meslek mensupları ve yanlarında çalışanlar, işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler; adli ve idari her türlü işlemde tanıklıktan çekinebilirler. Kanunen açıkça bilgi verme yükümlülüğü bulunan hâller saklıdır.",
  "3568 sayılı Kanun m.43")

q("mesleki_sorumluluk", "Mesleki Sorumluluklar",
  "Meslek mensubuna getirilen yasaklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensupları ticari faaliyette bulunamaz ve mesleğin bağımsızlık ve tarafsızlığıyla bağdaşmayan işler yapamaz",
  ["Meslek mensupları her türlü ticari faaliyeti serbestçe yürütebilir; bu konuda hiçbir yasak bulunmamaktadır",
   "Meslek mensuplarına yalnızca reklam yasağı getirilmiş olup ticari faaliyet tümüyle serbest bırakılmıştır",
   "Ticaret yasağı yalnızca yeminli mali müşavirleri bağlar; serbest muhasebeci mali müşavirler serbesttir",
   "Meslek mensubuna hiçbir yasak getirilmemiş olup meslek kuralları yalnızca tavsiye niteliği taşımaktadır"],
  "3568 sayılı Kanun m.43-45: meslek mensupları mesleğin bağımsızlık ve tarafsızlığıyla bağdaşmayan işleri yapamaz; ticari faaliyette bulunamaz ve iş elde etmek için reklam sayılabilecek faaliyetlerde bulunamazlar.",
  "3568 sayılı Kanun m.43-45")

q("mesleki_sorumluluk", "Mesleki Sorumluluklar",
  "Aşağıdakilerden hangileri meslek mensubu için öngörülen yasak ve yükümlülüklerdendir?\n\nI. Sır saklama yükümlülüğü\n\nII. Reklam yasağı\n\nIII. Ticari faaliyette bulunma yasağı",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "3568 sayılı Kanun: sır saklama yükümlülüğü (I), iş elde etmek için reklam yasağı (II) ve mesleğin bağımsızlığıyla bağdaşmayan ticari faaliyet yasağı (III) meslek mensubunu bağlar. Üçü de doğrudur.",
  "3568 sayılı Kanun m.43-45")

# ══ ÇALIŞMA USUL VE ESASLARI (5) ══════════════════════════════════════════
q("calisma_usulleri", "Çalışma Usul ve Esasları",
  "Meslek mensubu ile müşteri arasındaki sözleşme bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu ile müşteri arasında yazılı sözleşme yapılması esastır",
  ["Meslek mensubu ile müşteri arasında sözleşme yapılması gerekmez; sözlü anlaşma her hâlde yeterlidir",
   "Sözleşme yalnızca yeminli mali müşavirlerle yapılır; serbest muhasebeci mali müşavirlerle yapılmaz",
   "Sözleşmenin geçerliliği için noterde resmî senet düzenlenmesi ve odaya tescili zorunlu tutulmuştur",
   "Sözleşmeyi meslek mensubu değil, doğrudan bağlı bulunduğu oda müşteriyle imzalamak zorundadır"],
  "3568 sayılı Kanun ve ilgili yönetmelik: meslek mensubu ile iş sahibi arasında yazılı sözleşme yapılması esastır; sözleşmede işin konusu, süresi ve ücreti gibi hususlar belirtilir.",
  "3568 sayılı Kanun - sözleşme")

q("calisma_usulleri", "Çalışma Usul ve Esasları",
  "Ücret tarifesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensuplarının uygulayacağı asgari ücret tarifesi TÜRMOB'ca hazırlanıp ilgili Bakanlığın onayıyla yürürlüğe girer",
  ["Meslek mensupları ücretlerini hiçbir sınır olmaksızın ve tarifeye bağlı kalmadan serbestçe belirler",
   "Ücret tarifesini her meslek mensubu kendisi belirleyip bağlı bulunduğu odaya bildirmekle yetinir",
   "Ücret tarifesi doğrudan Cumhurbaşkanı kararıyla belirlenir; TÜRMOB'un bu süreçte hiçbir rolü yoktur",
   "Ücret tarifesi diye bir kavram bulunmayıp meslek mensubu ücret talep etmeksizin hizmet vermektedir"],
  "3568 sayılı Kanun m.46: meslek mensuplarının uygulayacakları asgari ücret tarifesi TÜRMOB tarafından hazırlanır ve ilgili Bakanlığın onayıyla yürürlüğe girer. Tarifedeki tutarların altında ücret alınamaz.",
  "3568 sayılı Kanun m.46")

q("calisma_usulleri", "Çalışma Usul ve Esasları",
  "Meslek mensubunun işi bırakması bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu haklı sebep olmaksızın işi bırakarak müşteriyi zarara uğratamaz; işi bırakırken devir ve bilgilendirme yükümlülüğü vardır",
  ["Meslek mensubu dilediği zaman ve hiçbir bildirimde bulunmaksızın işi bırakabilir; sorumluluğu doğmaz",
   "Meslek mensubu işi hiçbir hâlde bırakamaz; sözleşme ömür boyu devam etmek zorunda tutulmaktadır",
   "İşi bırakma yalnızca müşterinin onayıyla mümkün olup meslek mensubunun kendi iradesi yeterli değildir",
   "İşi bırakan meslek mensubu belge ve bilgileri imha etmek zorunda olup devretmesi kanunen yasaktır"],
  "3568 sayılı Kanun ve meslek kuralları: meslek mensubu, haklı bir sebep olmaksızın işi yarıda bırakarak müşteriyi zarara uğratamaz; ilişkiyi sonlandırırken müşterinin mağdur olmaması için belge ve bilgilerin devrine özen gösterir.",
  "3568 sayılı Kanun - işi bırakma")

q("calisma_usulleri", "Çalışma Usul ve Esasları",
  "Meslek mensubunun büro açması bakımından aşağıdakilerden hangisi doğrudur?",
  "Serbest çalışan meslek mensubu, mesleki faaliyetini yürütmek üzere bağlı olduğu odaya kayıtlı bir iş yeri (büro) açmakla yükümlüdür",
  ["Serbest çalışan meslek mensubunun büro açması gerekmez; faaliyetini istediği yerden yürütebilir",
   "Büro açmak yalnızca yeminli mali müşavirler için zorunlu olup diğer meslek mensuplarını bağlamaz",
   "Meslek mensubu birden fazla ilde sınırsız sayıda büro açabilir; hiçbir kayıt veya bildirim aranmaz",
   "Büro açma yükümlülüğü kanunda düzenlenmemiş olup tümüyle meslek mensubunun takdirindedir"],
  "3568 sayılı Kanun ve ilgili yönetmelik: mesleği serbest olarak icra eden meslek mensupları, bağımsız büro açmak ve bu büroyu bağlı oldukları odaya bildirmekle yükümlüdür; büro standartlarına uyulması gerekir.",
  "3568 sayılı Kanun - büro açma")

q("calisma_usulleri", "Çalışma Usul ve Esasları",
  "Meslek mensubunun defter ve belgeleri saklaması bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu, kendisine teslim edilen ve düzenlediği belgeleri kanunda öngörülen süre boyunca saklamakla yükümlüdür",
  ["Meslek mensubunun belge saklama yükümlülüğü bulunmayıp belgeleri dilediği zaman imha edebilir",
   "Belge saklama yükümlülüğü yalnızca müşteriye ait olup meslek mensubunu hiç ilgilendirmemektedir",
   "Meslek mensubu belgeleri işi bitirdiği gün müşteriye iade eder; saklama süresi söz konusu değildir",
   "Belgeler yalnızca bağlı bulunulan oda arşivinde saklanır; meslek mensubunun bir görevi bulunmaz"],
  "Meslek mensubu, mesleki faaliyeti kapsamında kendisine teslim edilen ve düzenlediği defter/belgeleri mevzuatta öngörülen süre boyunca muhafaza etmek ve talep hâlinde ibraz etmekle yükümlüdür.",
  "3568 sayılı Kanun - muhafaza yükümlülüğü")

# ══ ODALAR VE TÜRMOB (5) ══════════════════════════════════════════════════
q("oda_ve_turmob", "Odalar ve TÜRMOB",
  "Meslek odalarının hukuki niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Odalar, tüzel kişiliğe sahip kamu kurumu niteliğinde meslek kuruluşlarıdır",
  ["Odalar, meslek mensuplarının ortaklığıyla kurulmuş ve kâr amacı güden özel hukuk şirketleridir",
   "Odalar, bir bakanlığa bağlı olarak çalışan ve tüzel kişiliği bulunmayan genel müdürlüklerdir",
   "Odalar, tüzel kişiliği bulunmayan ve yalnızca üyelerin gönüllü bir araya geldiği derneklerdir",
   "Odalar, ticaret siciline tescil edilen ve ticari faaliyet yürüten anonim şirket niteliğindedir"],
  "3568 sayılı Kanun m.14: odalar, tüzel kişiliğe sahip, kamu kurumu niteliğinde meslek kuruluşlarıdır. Anayasa m.135 kapsamındadırlar.",
  "3568 sayılı Kanun m.14", "easy")

q("oda_ve_turmob", "Odalar ve TÜRMOB",
  "TÜRMOB bakımından aşağıdakilerden hangisi doğrudur?",
  "Odaların üst kuruluşu olup tüzel kişiliğe sahip, kamu kurumu niteliğinde bir meslek kuruluşudur",
  ["TÜRMOB bir bakanlığın genel müdürlüğü olup ayrı bir tüzel kişiliği bulunmamaktadır",
   "TÜRMOB, meslek mensuplarının kurduğu ve kâr dağıtan bir kooperatif niteliğinde bulunmaktadır",
   "TÜRMOB odalardan bağımsız bir kuruluş olup odalarla arasında hiçbir hukuki bağ bulunmamaktadır",
   "TÜRMOB yalnızca bir danışma organı olup hiçbir düzenleyici veya idari yetkisi bulunmamaktadır"],
  "3568 sayılı Kanun m.29: TÜRMOB (Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği), odaların üst kuruluşu olup tüzel kişiliğe sahip, kamu kurumu niteliğinde bir meslek kuruluşudur.",
  "3568 sayılı Kanun m.29")

q("oda_ve_turmob", "Odalar ve TÜRMOB",
  "Odaya kayıt zorunluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensupları, mesleki faaliyette bulunabilmek için bölgesinde bulundukları odaya kaydolmak zorundadır",
  ["Odaya kayıt tümüyle isteğe bağlı olup kaydolmayan meslek mensubu da serbestçe faaliyet gösterebilir",
   "Odaya kayıt yalnızca yeminli mali müşavirler için zorunlu olup diğerleri bu yükümlülükten muaftır",
   "Meslek mensubu dilediği ildeki odaya kaydolabilir; bölge veya yerleşim yeri ölçütü aranmamaktadır",
   "Odaya kayıt yalnızca meslek mensubunun ilk beş yılında zorunlu olup sonrasında kayıt silinmektedir"],
  "3568 sayılı Kanun m.19: meslek mensupları, mesleki faaliyette bulunabilmek için bölgesi içinde bulundukları odaya kaydolmak zorundadır. Ruhsat ve odaya kayıt mesleğin icrasının ön koşuludur.",
  "3568 sayılı Kanun m.19")

q("oda_ve_turmob", "Odalar ve TÜRMOB",
  "Odaların organları bakımından aşağıdakilerden hangisi doğrudur?",
  "Genel kurul, yönetim kurulu, disiplin kurulu ve denetleme kurulu odanın organlarındandır",
  ["Odanın tek organı genel kurul olup yönetim ve disiplin kurulu diye organlar bulunmamaktadır",
   "Odanın organları bulunmayıp tüm kararlar doğrudan TÜRMOB tarafından alınıp uygulanmaktadır",
   "Oda organları her yıl ilgili Bakanlık tarafından atanmakta olup seçim yapılmamaktadır",
   "Odanın tek organı disiplin kurulu olup başka bir karar veya yürütme organı öngörülmemiştir"],
  "3568 sayılı Kanun m.15: odanın organları genel kurul, yönetim kurulu, disiplin kurulu ve denetleme kuruludur.",
  "3568 sayılı Kanun m.15")

q("oda_ve_turmob", "Odalar ve TÜRMOB",
  "Aşağıdakilerden hangileri doğrudur?\n\nI. Odalar kamu kurumu niteliğinde meslek kuruluşudur\n\nII. TÜRMOB odaların üst kuruluşudur\n\nIII. Meslek mensubunun odaya kaydı isteğe bağlıdır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Odalar kamu kurumu niteliğinde meslek kuruluşudur (I) ve TÜRMOB odaların üst kuruluşudur (II). Ancak mesleki faaliyette bulunmak için odaya kayıt zorunludur, isteğe bağlı değildir; bu nedenle III yanlıştır. Doğru: I ve II.",
  "3568 sayılı Kanun m.14, 19, 29")

# ══ MESLEKİ ETİK + DİSİPLİN (12) ══════════════════════════════════════════
q("mesleki_etik", "Mesleki Etik",
  "Mesleki etikte dürüstlük ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu tüm mesleki ve iş ilişkilerinde açık sözlü ve doğru olmalıdır",
  ["Meslek mensubu müşterisinin çıkarı gerektiriyorsa gerçeğe aykırı beyanda bulunabilmektedir",
   "Dürüstlük yalnızca meslek mensubunun kendi ortaklarına karşı geçerli olan sınırlı bir ilkedir",
   "Dürüstlük ilkesi yalnızca yazılı raporları kapsar; sözlü beyanlar bu ilkenin dışında tutulmuştur",
   "Dürüstlük etik kurallarda yer almayan ve yalnızca kişisel bir tercih olarak görülen bir davranıştır"],
  "Etik Kurallar: dürüstlük ilkesi, meslek mensubunun tüm mesleki ve iş ilişkilerinde açık sözlü ve doğru olmasını gerektirir; yanıltıcı olduğunu bildiği bilgileri içeren raporlarla ilişkilendirilmemelidir.",
  "Meslek Etiği - dürüstlük", "easy")

q("mesleki_etik", "Mesleki Etik",
  "Tarafsızlık (objektiflik) ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu; yanlılık, çıkar çatışması veya başkalarının etkisi altında kalarak mesleki muhakemesini bozmamalıdır",
  ["Meslek mensubu ücretini ödeyen müşterinin görüşünü her hâlde benimsemek ve savunmakla yükümlüdür",
   "Tarafsızlık yalnızca bağımsız denetim işlerinde aranır; diğer mesleki hizmetlerde geçerli değildir",
   "Tarafsızlık, meslek mensubunun hiçbir konuda görüş bildirmemesi ve tarafsız kalması anlamına gelir",
   "Tarafsızlık ilkesi yalnızca meslek mensubunun akrabalarıyla olan ilişkilerini kapsamına almaktadır"],
  "Etik Kurallar: tarafsızlık ilkesi, meslek mensubunun yanlılık, çıkar çatışması veya başkalarının nüfuzu altında kalarak mesleki veya iş kararlarını vermemesini gerektirir.",
  "Meslek Etiği - tarafsızlık")

q("mesleki_etik", "Mesleki Etik",
  "Mesleki yeterlik ve özen ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu bilgi ve becerisini gerekli düzeyde tutmalı ve hizmetleri geçerli standartlara uygun, özenle yürütmelidir",
  ["Meslek mensubu bir kez ruhsat aldıktan sonra bilgisini güncellemek zorunda değildir; eğitim gerekmez",
   "Mesleki özen yalnızca ücreti yüksek işlerde aranır; düşük ücretli işlerde özen yükümlülüğü doğmaz",
   "Mesleki yeterlik yalnızca sınav aşamasında aranan bir koşul olup meslek icrasında geçerliliği yoktur",
   "Meslek mensubu yeterli bilgisi olmayan bir işi de üstlenebilir; sorumluluk müşteriye ait olmaktadır"],
  "Etik Kurallar: mesleki yeterlik ve özen ilkesi, meslek mensubunun mesleki bilgi ve becerisini yeterli hizmet sağlayacak düzeyde tutmasını (sürekli eğitim) ve hizmetleri geçerli standartlara uygun biçimde özenle yürütmesini gerektirir.",
  "Meslek Etiği - mesleki yeterlik ve özen")

q("mesleki_etik", "Mesleki Etik",
  "Mesleki davranış ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu ilgili mevzuata uymalı ve mesleğin itibarını zedeleyecek davranışlardan kaçınmalıdır",
  ["Meslek mensubunun mesleki hayatı dışındaki davranışları mesleği hiçbir biçimde ilgilendirmemektedir",
   "Mesleki davranış ilkesi yalnızca meslek mensubunun bürosundaki davranışlarını kapsamına almaktadır",
   "Meslek mensubu mesleğin itibarını zedelese dahi mevzuata uyduğu sürece hiçbir yaptırımla karşılaşmaz",
   "Mesleki davranış ilkesi etik kurallarda yer almayıp yalnızca disiplin yönetmeliğinin konusudur"],
  "Etik Kurallar: mesleki davranış ilkesi, meslek mensubunun ilgili mevzuata uymasını ve mesleğin itibarını zedeleyecek her türlü davranıştan kaçınmasını gerektirir.",
  "Meslek Etiği - mesleki davranış")

q("mesleki_etik", "Mesleki Etik",
  "Çıkar çatışması bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu çıkar çatışması doğuran durumları belirlemeli, değerlendirmeli ve gerekirse işi kabul etmemelidir",
  ["Çıkar çatışması meslek mensubunu hiç ilgilendirmez; her işi koşulsuz kabul etmek zorundadır",
   "Çıkar çatışması yalnızca ücret yüksekse dikkate alınır; düşük ücretli işlerde göz ardı edilebilir",
   "Çıkar çatışması ancak müşteri şikâyet ederse değerlendirilir; meslek mensubunun bir görevi yoktur",
   "Çıkar çatışması hâlinde meslek mensubu her iki tarafı da temsil ederek uyuşmazlığı çözmelidir"],
  "Etik Kurallar: meslek mensubu, temel ilkelere uyumu tehdit eden çıkar çatışması yaratabilecek durumları belirler ve değerlendirir; koruyucu önlemlerle tehdit kabul edilebilir düzeye indirilemiyorsa işi reddeder veya ilişkiyi sonlandırır.",
  "Meslek Etiği - çıkar çatışması")

q("mesleki_etik", "Mesleki Etik",
  "Mesleki etik bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dürüstlük temel ilkelerdendir\n\nII. Tarafsızlık temel ilkelerdendir\n\nIII. Meslek mensubu ücretini ödeyen müşterinin görüşünü benimsemekle yükümlüdür",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Dürüstlük (I) ve tarafsızlık (II) mesleki etiğin temel ilkelerindendir. Müşterinin görüşünü benimseme yükümlülüğü (III) ise tam tersine tarafsızlık ilkesine aykırıdır; bu nedenle yanlıştır.",
  "Meslek Etiği - temel ilkeler")

q("disiplin", "Disiplin Hükümleri",
  "Disiplin cezalarının türleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Uyarma, kınama, geçici olarak mesleki faaliyetten alıkoyma, yeminli sıfatını kaldırma ve meslekten çıkarma disiplin cezalarıdır",
  ["Tek disiplin cezası meslekten çıkarma olup daha hafif bir yaptırım öngörülmemiş bulunmaktadır",
   "Disiplin cezaları yalnızca para cezasından ibaret olup meslekten çıkarma söz konusu değildir",
   "Disiplin cezaları kanunda sayılmamış olup odanın takdirine göre serbestçe belirlenebilmektedir",
   "Disiplin cezası yalnızca hapis cezası olup adli mercilerce hükmedilen bir yaptırım niteliğindedir"],
  "3568 sayılı Kanun m.48: disiplin cezaları uyarma, kınama, geçici olarak mesleki faaliyetten alıkoyma, yeminli sıfatını kaldırma ve meslekten çıkarmadır.",
  "3568 sayılı Kanun m.48")

q("disiplin", "Disiplin Hükümleri",
  "Disiplin cezası verme yetkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Disiplin cezaları, meslek mensubunun bağlı olduğu odanın disiplin kurulu tarafından verilir",
  ["Disiplin cezalarını doğrudan ceza mahkemeleri verir; odanın bu konuda hiçbir yetkisi bulunmamaktadır",
   "Disiplin cezalarını meslek mensubunun müşterisi belirler ve doğrudan uygular; oda araya girmez",
   "Disiplin cezası verme yetkisi yalnızca ilgili Bakanlığa ait olup meslek kuruluşları yetkisizdir",
   "Disiplin cezaları oda genel kurulunda tüm üyelerin oylamasıyla ve oy çokluğuyla verilmektedir"],
  "3568 sayılı Kanun m.15, 48: disiplin cezaları meslek mensubunun bağlı olduğu odanın disiplin kurulu tarafından verilir; TÜRMOB Disiplin Kurulu ise itirazları inceler.",
  "3568 sayılı Kanun m.48")

q("disiplin", "Disiplin Hükümleri",
  "Disiplin kararlarına itiraz bakımından aşağıdakilerden hangisi doğrudur?",
  "Oda disiplin kurulu kararlarına karşı TÜRMOB Disiplin Kuruluna itiraz edilebilir",
  ["Oda disiplin kurulu kararları kesin olup hiçbir mercie itiraz edilmesi mümkün değildir",
   "Disiplin kararlarına itiraz yalnızca kararı veren odanın kendisine yapılabilir; üst kurul yoktur",
   "Disiplin kararlarına itiraz yalnızca ilgili Bakanlığa yapılır; TÜRMOB'un bu konuda yetkisi yoktur",
   "Disiplin kararlarına itiraz doğrudan Yargıtaya yapılır; idari bir itiraz yolu öngörülmemiştir"],
  "3568 sayılı Kanun m.49-50: oda disiplin kurulu kararlarına karşı TÜRMOB Disiplin Kuruluna itiraz edilebilir; kesinleşen disiplin kararlarına karşı ayrıca yargı yolu açıktır.",
  "3568 sayılı Kanun m.49-50")

q("disiplin", "Disiplin Hükümleri",
  "Meslekten çıkarma cezası bakımından aşağıdakilerden hangisi doğrudur?",
  "En ağır disiplin cezası olup kanunda sayılan ağır fiillerde ve belirli koşulların gerçekleşmesi hâlinde verilir",
  ["En hafif disiplin cezası olup küçük şekil hatalarında dahi doğrudan uygulanabilmektedir",
   "Meslekten çıkarma cezası bulunmayıp en ağır ceza yalnızca kınamadan ibaret kalmaktadır",
   "Meslekten çıkarma cezası müşterinin talebi üzerine ve başka koşul aranmaksızın verilmektedir",
   "Meslekten çıkarma cezası her disiplin soruşturmasının kendiliğinden sonucu olarak ortaya çıkar"],
  "3568 sayılı Kanun m.48: meslekten çıkarma en ağır disiplin cezası olup kanunda sayılan ağır fiiller ile disiplin cezalarının tekerrürü gibi hâllerde verilir; meslek mensubunun ruhsatı iptal edilir.",
  "3568 sayılı Kanun m.48")

q("disiplin", "Disiplin Hükümleri",
  "Disiplin soruşturması ile ceza kovuşturması ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir fiil hem disiplin hem ceza sorumluluğu doğurabilir; disiplin soruşturması ceza kovuşturmasından bağımsız yürütülebilir",
  ["Bir fiil ya disiplin ya ceza sorumluluğu doğurur; ikisi hiçbir hâlde birlikte söz konusu olamaz",
   "Disiplin soruşturması ancak ceza davası kesinleştikten sonra başlatılabilir; öncesinde mümkün değildir",
   "Ceza kovuşturması başlatıldığında disiplin soruşturması kendiliğinden ve kesin olarak düşmektedir",
   "Disiplin ve ceza sorumluluğu aynı kurum tarafından ve tek bir kararla birlikte hükme bağlanmaktadır"],
  "Disiplin sorumluluğu ile cezai sorumluluk farklı hukuki temellere dayanır; aynı fiil hem meslek kurallarına aykırılık hem suç oluşturabilir. Disiplin soruşturması kural olarak ceza kovuşturmasından bağımsız yürütülür.",
  "3568 sayılı Kanun - disiplin/ceza ilişkisi")

q("disiplin", "Disiplin Hükümleri",
  "Aşağıdakilerden hangileri 3568 sayılı Kanun'a göre disiplin cezalarındandır?\n\nI. Uyarma\n\nII. Kınama\n\nIII. Geçici olarak mesleki faaliyetten alıkoyma",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "3568 sayılı Kanun m.48: disiplin cezaları uyarma (I), kınama (II), geçici olarak mesleki faaliyetten alıkoyma (III), yeminli sıfatını kaldırma ve meslekten çıkarmadır. Üçü de disiplin cezasıdır.",
  "3568 sayılı Kanun m.48")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
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
        ch = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            ch[k] = d
        assert len(set(ch.values())) == 5, f"{prefix}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{prefix}-{i+1:04d}", "lessonId": L, "topicId": it["topic"],
            "question": it["stem"], "choices": ch, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", it["label"]],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-16T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "2026-07-16",
            "sourceUpdatedAt": "2026-07-16T00:00:00Z", "isPremium": False, "isActive": True,
        })
    return out

if __name__ == "__main__":
    assert len(Q) == 40, f"40 olmalı, şu an {len(Q)}"
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in Q if len(MARK.findall(x["stem"])) >= 2]
    duz = [x for x in Q if len(MARK.findall(x["stem"])) < 2]
    t2 = [x for i, x in enumerate(duz) if i % 2 == 0] + [x for i, x in enumerate(onc) if i % 2 == 0]
    t3 = [x for i, x in enumerate(duz) if i % 2 == 1] + [x for i, x in enumerate(onc) if i % 2 == 1]
    print(f"öncüllü {len(onc)} → t2:{len([x for x in t2 if x in onc])} t3:{len([x for x in t3 if x in onc])}")
    APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik"
    for items, name, prefix, seed in ((t2, "questions_meslek_hukuku_test2_2026.json", "mh-t2", 20260811),
                                      (t3, "questions_meslek_hukuku_test3_2026.json", "mh-t3", 20260812)):
        data = emit(items, prefix, seed)
        json.dump(data, open(f"{APP}/{name}", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{name}: {len(data)} soru | harf {''.join(x['correctAnswer'] for x in data)}")
