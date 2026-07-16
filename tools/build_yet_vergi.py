# -*- coding: utf-8 -*-
"""Yeterlilik — Vergi Mevzuatı ve Uygulaması Test 2 + Test 3 (2×20 = 40 soru).
6 alt ders: VUK · Vergi Hukuku · Türk Vergi Sistemi · GV · KV · KDV.
⚠️ YILA BAĞLI ORAN/HAD/TARİFE/TUTAR YOK — yalnız kanunda sabit yapısal-kavramsal
(mükellef, vergiyi doğuran olay, istisna TÜRÜ, beyan usulü, süre yapısı).
Doğru şık KISA, çeldiriciler UZUN. explanation'da harf atıfı YOK."""
import json, random, re

Q = []
def q(lesson, topic, label, stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(lesson=lesson, topic=topic, label=label, stem=stem, correct=correct,
                  distractors=distractors, why=why, ref=ref, difficulty=difficulty))

VUK, VH, TVS = "vergi_usul_kanunu", "vergi_hukuku", "turk_vergi_sistemi"
GV, KV, KDV = "gelir_vergisi", "kurumlar_vergisi", "katma_deger_vergisi"

# ══ VERGİ USUL KANUNU (8) ═════════════════════════════════════════════════
q(VUK, "vergilendirme_sureci", "Vergilendirme Süreci",
  "Vergiyi doğuran olay bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi kanunlarının vergiyi bağladıkları olayın vuku bulması veya hukuki durumun tamamlanmasıyla doğar",
  ["Vergiyi doğuran olay, ancak verginin mükellef tarafından fiilen ödenmesiyle ortaya çıkmış sayılır",
   "Vergiyi doğuran olay, verginin idare tarafından tarh edilip mükellefe tebliğ edilmesiyle gerçekleşir",
   "Vergiyi doğuran olay, mükellefin vergi dairesine kayıt yaptırıp mükellefiyet tesis ettirmesiyle doğar",
   "Vergiyi doğuran olay, takvim yılının sona ermesiyle ve başka hiçbir koşula bağlı olmadan doğar"],
  "VUK m.19: vergi alacağı, vergi kanunlarının vergiyi bağladıkları olayın vuku bulması veya hukuki durumun tekemmülü ile doğar. Tarh, tebliğ ve tahsil sonraki aşamalardır.",
  "213 sayılı VUK m.19", "easy")

q(VUK, "vergilendirme_sureci", "Vergilendirme Süreci",
  "Verginin tarhı bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi alacağının kanunda gösterilen matrah ve oranlar üzerinden idarece hesaplanarak miktarının belirlenmesidir",
  ["Verginin mükellef tarafından vergi dairesi veznesine fiilen ödenmesi işlemini ifade etmektedir",
   "Vergilendirmeyi ilgilendiren belgelerin mükellefe yazılı olarak bildirilmesi işlemini ifade eder",
   "Mükellefin defter ve belgelerinin idare tarafından incelenmesi sürecini ifade eden bir aşamadır",
   "Verginin mükellef tarafından beyanname ile idareye bildirilmesi işlemini ifade eden bir aşamadır"],
  "VUK m.20: verginin tarhı, vergi alacağının kanunda gösterilen matrah ve nispetler üzerinden vergi dairesince hesaplanarak miktarının tespit edilmesidir.",
  "213 sayılı VUK m.20")

q(VUK, "vergilendirme_sureci", "Vergilendirme Süreci",
  "Tebliğ bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergilendirmeyi ilgilendiren ve hüküm ifade eden belgelerin yetkili makamlarca ilgiliye yazı ile bildirilmesidir",
  ["Vergi alacağının matrah üzerinden hesaplanarak miktarının idarece belirlenmesi işlemini ifade eder",
   "Verginin mükellef tarafından vergi dairesine ödenerek vergi borcunun sona erdirilmesi işlemidir",
   "Vergiyi doğuran olayın gerçekleşmesiyle vergi alacağının kendiliğinden doğması aşamasını ifade eder",
   "Mükellefin vergiye ilişkin defter ve belgelerini kanuni süre boyunca saklaması yükümlülüğüdür"],
  "VUK m.21: tebliğ, vergilendirmeyi ilgilendiren ve hüküm ifade eden hususların yetkili makamlarca mükellefe veya ceza sorumlusuna yazı ile bildirilmesidir.",
  "213 sayılı VUK m.21")

q(VUK, "vergilendirme_sureci", "Vergilendirme Süreci",
  "Aşağıdakilerden hangileri vergilendirme sürecinin aşamalarındandır?\n\nI. Tarh\n\nII. Tebliğ\n\nIII. Tahakkuk ve tahsil",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Vergilendirme süreci; tarh (I), tebliğ (II), tahakkuk ve tahsil (III) aşamalarından oluşur. Vergiyi doğuran olayın ardından bu dört işlem sırayla gerçekleşir. Üçü de sürecin aşamasıdır.",
  "213 sayılı VUK m.20-23")

q(VUK, "mukellef_odevleri", "Mükellef Ödevleri",
  "Vergi mükellefi ile vergi sorumlusu ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Mükellef vergi borcunu kendi malından ödeyen; sorumlu ise ödeme bakımından idareye muhatap olan kişidir",
  ["Mükellef ile vergi sorumlusu her hâlde aynı kişidir; aralarında hiçbir hukuki fark bulunmamaktadır",
   "Mükellef verginin ödenmesinden idareye karşı muhatap; sorumlu ise vergiyi kendi malından ödeyen kişidir",
   "Vergi sorumlusu diye bir kavram VUK'ta düzenlenmemiş olup yalnızca mükellef kavramı bulunmaktadır",
   "Mükellef yalnızca tüzel kişi, vergi sorumlusu ise yalnızca gerçek kişi olabilen bir sıfattır"],
  "VUK m.8: mükellef, vergi kanunlarına göre kendisine vergi borcu düşen gerçek/tüzel kişidir; vergi sorumlusu ise verginin ödenmesi bakımından alacaklı vergi dairesine karşı muhatap olan kişidir (örneğin stopajda işveren).",
  "213 sayılı VUK m.8")

q(VUK, "mukellef_odevleri", "Mükellef Ödevleri",
  "Mükellefin ödevleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Bildirimde bulunma, defter tutma, belge düzenleme ve muhafaza-ibraz ödevleri mükellefin şekli ödevlerindendir",
  ["Mükellefin tek ödevi vergiyi ödemek olup defter tutma ve belge düzenlemeyle ilgili bir yükümlülüğü yoktur",
   "Defter tutma ve belge düzenleme yalnızca vergi idaresinin ödevi olup mükellefi hiç ilgilendirmemektedir",
   "Mükellefin muhafaza ve ibraz ödevi yoktur; belgeler düzenlendiği anda idareye teslim edilmektedir",
   "Bildirimde bulunma ödevi yalnızca işe başlarken doğar; adres veya işi bırakma bildirimi gerekmemektedir"],
  "VUK: mükellefin maddi ödevi (vergiyi ödeme) yanında şekli ödevleri de vardır: bildirimler (işe başlama, değişiklik, işi bırakma), defter tutma, belge düzenleme-alma ve defter-belgeleri muhafaza ile ibraz.",
  "213 sayılı VUK m.153 vd.")

q(VUK, "vergi_cezalari", "Vergi Cezaları",
  "Vergi ziyaı bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergilendirme ödevlerinin zamanında yerine getirilmemesi yüzünden verginin zamanında veya tam tahakkuk ettirilememesidir",
  ["Mükellefin vergisini zamanında ve tam olarak ödemesine rağmen idarece ceza kesilmesi durumunu ifade eder",
   "Vergi idaresinin bir hesaplama hatası yapması sonucu mükellef aleyhine fazla vergi tahakkuk ettirmesidir",
   "Mükellefin vergiye ilişkin bir uyuşmazlığı yargıya taşıması hâlinde doğan yargılama giderini ifade eder",
   "Verginin kanuni süresinden önce ve fazla ödenmesi sonucu hazine lehine oluşan bir vergi fazlalığıdır"],
  "VUK m.341: vergi ziyaı, mükellefin veya sorumlunun vergilendirme ödevlerini zamanında yerine getirmemesi ya da eksik yerine getirmesi yüzünden verginin zamanında tahakkuk ettirilmemesi veya eksik tahakkuk ettirilmesidir.",
  "213 sayılı VUK m.341")

q(VUK, "vergi_cezalari", "Vergi Cezaları",
  "Vergi cezalarının türleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi ziyaı cezası ile usulsüzlük cezaları idari; kaçakçılık suçlarına ilişkin cezalar ise adli niteliktedir",
  ["Bütün vergi cezaları adli nitelikte olup yalnızca ceza mahkemeleri tarafından hükmedilebilmektedir",
   "Bütün vergi cezaları idari nitelikte olup hiçbiri için ceza mahkemesine başvurulması söz konusu değildir",
   "Vergi cezaları yalnızca para cezasından ibaret olup hapis cezası hiçbir hâlde söz konusu olamamaktadır",
   "Usulsüzlük cezaları adli, kaçakçılık cezaları ise idari nitelikte olup bu yönüyle birbirinin tersidir"],
  "VUK: vergi ziyaı cezası ve usulsüzlük cezaları (genel/özel) idari para cezası niteliğindedir; kaçakçılık suçları (VUK m.359) ise adli nitelikte olup hapis cezası gerektirir ve ceza mahkemesinde yargılanır.",
  "213 sayılı VUK m.344, 351, 359")

q(VUK, "mukellef_odevleri", "Mükellef Ödevleri",
  "Defter ve belgelerin muhafaza ve ibraz ödevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Mükellef, tuttuğu defter ve düzenlediği belgeleri kanunda öngörülen süre boyunca saklamak ve yetkili makamlara ibraz etmekle yükümlüdür",
  ["Mükellefin defter ve belgeleri saklama yükümlülüğü bulunmayıp bunları dilediği zaman imha edebilmektedir",
   "Defter ve belgeler yalnızca ilgili hesap dönemi kapanana kadar saklanır; sonrasında ibraz yükümlülüğü düşer",
   "Defter ve belgeleri saklama ödevi mükellefe değil, doğrudan vergi dairesine ait olan bir yükümlülüktür",
   "Mükellef defterlerini saklamakla yükümlüyse de bunları hiçbir hâlde idareye ibraz etmek zorunda değildir"],
  "VUK m.253-256: mükellefler tuttukları defterleri ve aldıkları-düzenledikleri belgeleri kanunda öngörülen süre boyunca muhafaza etmek ve yetkili makam ve memurların talebi üzerine ibraz etmekle yükümlüdür.",
  "213 sayılı VUK m.253-256")

# ══ VERGİ HUKUKU (7) ══════════════════════════════════════════════════════
q(VH, "vergi_hukuku_ilkeleri", "Vergi Hukuku İlkeleri",
  "Verginin kanuniliği ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi, resim, harç ve benzeri mali yükümlülükler kanunla konulur, değiştirilir veya kaldırılır",
  ["Vergiler idarenin çıkardığı yönetmelik ve tebliğlerle serbestçe konulabilir; kanun şartı aranmamaktadır",
   "Vergiler yalnızca Cumhurbaşkanlığı kararnamesiyle konulur; yasama organının bu konuda yetkisi yoktur",
   "Vergiler yerel yönetimlerin meclis kararıyla ve kanuni dayanak aranmaksızın serbestçe konulabilmektedir",
   "Vergilerin konulması tümüyle vergi idaresinin takdirinde olup herhangi bir hukuki sınıra tabi değildir"],
  "Anayasa m.73: vergi, resim, harç ve benzeri mali yükümlülükler kanunla konulur, değiştirilir veya kaldırılır. Bu, verginin kanuniliği (yasallığı) ilkesidir.",
  "Anayasa m.73 - verginin kanuniliği", "easy")

q(VH, "vergi_hukuku_ilkeleri", "Vergi Hukuku İlkeleri",
  "Vergide eşitlik ve mali güce göre vergilendirme ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Herkes kamu giderlerini karşılamak üzere mali gücüne göre vergi ödemekle yükümlüdür",
  ["Herkes mali gücüne bakılmaksızın eşit ve aynı tutarda vergi ödemekle yükümlü tutulmaktadır",
   "Vergi yalnızca yüksek gelir gruplarından alınır; düşük gelirliler vergi ödemekten tümüyle muaftır",
   "Vergilendirmede mali güç ilkesi yalnızca gelir vergisinde geçerli olup diğer vergilerde aranmamaktadır",
   "Mali güce göre vergilendirme yalnızca bir öneri olup Anayasada düzenlenmemiş bir kavramdır"],
  "Anayasa m.73: herkes, kamu giderlerini karşılamak üzere mali gücüne göre vergi ödemekle yükümlüdür. Vergi yükünün adaletli ve dengeli dağılımı maliye politikasının sosyal amacıdır.",
  "Anayasa m.73 - mali güce göre vergilendirme")

q(VH, "vergi_hukuku_ilkeleri", "Vergi Hukuku İlkeleri",
  "Vergi kanunlarının yorumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi kanunları lafzı ve ruhu ile hüküm ifade eder; lafzın açık olmadığı hâllerde konuluş amacı dikkate alınır",
  ["Vergi kanunları yalnızca lafzıyla uygulanır; hiçbir hâlde amaca veya ruha başvurulamamaktadır",
   "Vergi kanunları kıyas yoluyla genişletilerek uygulanır; benzer olaylara aynı hüküm uygulanabilmektedir",
   "Vergi kanunlarının yorumu tümüyle mükellefin lehine yapılır; şüphe her hâlde mükellef lehine çözülür",
   "Vergi kanunlarını yorumlama yetkisi yalnızca vergi idaresine ait olup yargı bu konuda yetkisizdir"],
  "VUK m.3: vergi kanunları lafzı ve ruhu ile hüküm ifade eder. Lafzın açık olmadığı hâllerde hükümler, konuluşundaki amaç, hükümlerin kanun yapısındaki yeri ve diğer maddelerle bağlantısı göz önünde tutularak uygulanır. Vergi hukukunda kıyas yasaktır.",
  "213 sayılı VUK m.3")

q(VH, "vergi_hukuku_ilkeleri", "Vergi Hukuku İlkeleri",
  "Vergi hukukunda ispat ve delil bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergilendirmede vergiyi doğuran olay ve buna ilişkin işlemlerin gerçek mahiyeti esastır",
  ["Vergilendirmede işlemlerin yalnızca biçimsel görünümü esas alınır; gerçek mahiyet hiç araştırılmaz",
   "Vergiyi doğuran olayın gerçek mahiyeti yalnızca mükellefin beyanıyla belirlenir; başka delil aranmaz",
   "Vergi hukukunda ispat kavramı yoktur; idarenin takdiri her hâlde kesin ve tartışmasız kabul edilir",
   "Vergilendirmede yalnızca yemin delil olarak kabul edilir; belge ve kayıtlar delil sayılmamaktadır"],
  "VUK m.3: vergilendirmede vergiyi doğuran olay ve bu olaya ilişkin muamelelerin gerçek mahiyeti esastır. İktisadi, ticari ve teknik icaplara uymayan veya olayın özelliğine göre olağandışı görülen durumları iddia eden taraf ispatla yükümlüdür.",
  "213 sayılı VUK m.3 - ispat")

q(VH, "vergi_uyusmazliklari", "Vergi Uyuşmazlıkları",
  "Aşağıdakilerden hangileri vergi uyuşmazlıklarının idari çözüm yollarındandır?\n\nI. Uzlaşma\n\nII. Cezalarda indirim\n\nIII. Vergi mahkemesinde dava açma",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Uzlaşma (I) ve cezalarda indirim (II) idari çözüm yollarıdır. Vergi mahkemesinde dava açmak (III) ise idari değil yargısal çözüm yoludur; bu nedenle idari çözüm yolları arasında sayılmaz. Doğru: I ve II.",
  "213 sayılı VUK - uyuşmazlık çözümü")

q(VH, "vergi_uyusmazliklari", "Vergi Uyuşmazlıkları",
  "Vergi hatası bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiye ilişkin hesaplarda veya vergilendirmede yapılan hatalar yüzünden haksız yere fazla veya eksik vergi istenmesi ya da alınmasıdır",
  ["Vergi hatası yalnızca mükellefin beyanındaki hataları kapsar; idarenin yaptığı hatalar bu kapsama girmez",
   "Vergi hatası ancak dava açılarak düzeltilebilir; idareye başvuruyla düzeltme hiçbir hâlde mümkün değildir",
   "Vergi hatası kavramı yalnızca hukuki uyuşmazlıkları ifade eder; hesap hataları bu kapsamda değildir",
   "Vergi hatası yalnızca mükellef lehine düzeltilir; idare lehine olan hatalar düzeltilememektedir"],
  "VUK m.116-118: vergi hatası, vergiye müteallik hesaplarda (hesap hataları) veya vergilendirmede (vergilendirme hataları) yapılan hatalar yüzünden haksız yere fazla veya eksik vergi istenmesi veya alınmasıdır; düzeltme yoluyla giderilir.",
  "213 sayılı VUK m.116-118")

# ══ TÜRK VERGİ SİSTEMİ (5) ════════════════════════════════════════════════
q(TVS, "vergi_sistemi_yapisi", "Vergi Sistemi Yapısı",
  "Türk vergi sisteminde vergilerin sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiler gelir, harcama ve servet üzerinden alınan vergiler olarak sınıflandırılır",
  ["Türk vergi sisteminde yalnızca gelir üzerinden vergi alınır; harcama ve servet vergisi bulunmamaktadır",
   "Vergiler yalnızca dolaylı vergilerden oluşur; dolaysız vergi diye bir kategori bulunmamaktadır",
   "Vergilerin konusu kanunda belirlenmemiş olup idare dilediği konudan vergi alabilmektedir",
   "Türk vergi sisteminde tüm vergiler tek bir kanunda toplanmış olup ayrı vergi kanunları yoktur"],
  "Türk vergi sistemi konularına göre üç grupta toplanır: gelir üzerinden alınanlar (gelir ve kurumlar vergisi), harcama üzerinden alınanlar (KDV, ÖTV, damga vergisi) ve servet üzerinden alınanlar (emlak, MTV, veraset ve intikal vergisi).",
  "Türk Vergi Sistemi - sınıflandırma", "easy")

q(TVS, "vergi_sistemi_yapisi", "Vergi Sistemi Yapısı",
  "Dolaysız ve dolaylı vergi ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Dolaysız vergilerde vergiyi ödeyen ile yüklenen kural olarak aynı kişiyken, dolaylı vergilerde farklı kişilerdir",
  ["Dolaysız vergilerde vergiyi ödeyen ile yüklenen farklı kişiler; dolaylı vergilerde ise aynı kişidir",
   "Dolaysız ve dolaylı vergiler arasında yansıma bakımından hiçbir fark bulunmamaktadır",
   "Dolaysız vergiler yalnızca tüzel kişilerden, dolaylı vergiler ise yalnızca gerçek kişilerden alınır",
   "Dolaylı vergiler kişinin gelirine ve servetine, dolaysız vergiler ise harcamalarına göre alınır"],
  "Dolaysız vergilerde (gelir, kurumlar vergisi) verginin mükellefi ile yüklenicisi kural olarak aynıdır ve yansıtılması güçtür; dolaylı vergilerde (KDV, ÖTV) vergi mal/hizmet fiyatına eklenerek nihai tüketiciye yansıtılır.",
  "Türk Vergi Sistemi - dolaysız/dolaylı")

q(TVS, "vergi_sistemi_yapisi", "Vergi Sistemi Yapısı",
  "Aşağıdakilerden hangileri harcama üzerinden alınan vergilerdendir?\n\nI. Katma değer vergisi\n\nII. Özel tüketim vergisi\n\nIII. Emlak vergisi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "KDV (I) ve ÖTV (II) harcama üzerinden alınan (dolaylı) vergilerdir. Emlak vergisi (III) ise servet üzerinden alınan bir vergidir; bu nedenle harcama vergisi değildir. Doğru: I ve II.",
  "Türk Vergi Sistemi - vergi türleri")

q(TVS, "vergi_sistemi_yapisi", "Vergi Sistemi Yapısı",
  "Servet üzerinden alınan vergiler bakımından aşağıdakilerden hangisi doğrudur?",
  "Emlak vergisi, motorlu taşıtlar vergisi ile veraset ve intikal vergisi servet üzerinden alınan vergilerdendir",
  ["Servet üzerinden alınan tek vergi gelir vergisi olup başka bir servet vergisi bulunmamaktadır",
   "Motorlu taşıtlar vergisi harcama üzerinden alınan bir vergi olup servet vergisi kapsamında değildir",
   "Servet üzerinden vergi alınması Anayasaya aykırı olduğundan Türk vergi sisteminde yer almamaktadır",
   "Veraset ve intikal vergisi gelir üzerinden alınan bir vergi olup servet vergisi sayılmamaktadır"],
  "Servet üzerinden alınan vergiler; emlak vergisi, motorlu taşıtlar vergisi ile veraset ve intikal vergisidir. Bunlar kişilerin sahip olduğu servet unsurları veya servet transferi üzerinden alınır.",
  "Türk Vergi Sistemi - servet vergileri")

q(TVS, "vergi_sistemi_yapisi", "Vergi Sistemi Yapısı",
  "Verginin konusu ve matrahı kavramları bakımından aşağıdakilerden hangisi doğrudur?",
  "Verginin konusu üzerine vergi konulan iktisadi unsur; matrah ise verginin hesaplanmasına esas alınan değer veya miktardır",
  ["Verginin konusu ile matrahı her hâlde aynı kavram olup aralarında hiçbir fark bulunmamaktadır",
   "Matrah üzerine vergi konulan iktisadi unsur; konu ise verginin hesaplandığı değer veya miktardır",
   "Verginin konusu ve matrahı kanunda düzenlenmemiş olup idarenin serbestçe belirlediği kavramlardır",
   "Matrah yalnızca gelir vergisinde bulunur; diğer vergilerde matrah kavramı söz konusu değildir"],
  "Verginin konusu, üzerine vergi konulan ve verginin kaynağını oluşturan iktisadi unsurdur (gelir, harcama, servet). Matrah ise verginin hesaplanmasına esas alınan ve tarifenin uygulandığı değer ya da miktardır.",
  "Türk Vergi Sistemi - konu ve matrah")

# ══ GELİR VERGİSİ (7) ═════════════════════════════════════════════════════
q(GV, "gelir_unsurlari", "Gelir Unsurları",
  "Gelir vergisinde gelirin unsurları bakımından aşağıdakilerden hangisi doğrudur?",
  "Ticari, zirai ve serbest meslek kazançları ile ücretler, gayrimenkul ve menkul sermaye iratları ve diğer kazanç ve iratlar gelirin unsurlarıdır",
  ["Gelir vergisinde yalnızca ücretler vergilendirilir; diğer kazanç türleri gelir sayılmamaktadır",
   "Gelirin unsurları kanunda sayılmamış olup idare her türlü kazancı takdiren gelir sayabilmektedir",
   "Gelir vergisinde yalnızca ticari kazanç vergilendirilir; serbest meslek kazancı kapsam dışındadır",
   "Menkul ve gayrimenkul sermaye iratları gelir sayılmaz; yalnızca emekle elde edilen kazançlar gelirdir"],
  "GVK m.2: gelire giren kazanç ve iratlar yedi bentte sayılmıştır: ticari kazançlar, zirai kazançlar, ücretler, serbest meslek kazançları, gayrimenkul sermaye iratları, menkul sermaye iratları, diğer kazanç ve iratlar.",
  "193 sayılı GVK m.2", "easy")

q(GV, "gelir_unsurlari", "Gelir Unsurları",
  "Gelir vergisinde tam ve dar mükellefiyet ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Tam mükellefler yurt içi ve dışı tüm kazançları, dar mükellefler yalnızca Türkiye'deki kazançları üzerinden vergilendirilir",
  ["Tam mükellefler yalnızca Türkiye'deki, dar mükellefler ise dünya genelindeki kazançları üzerinden vergilendirilir",
   "Tam ve dar mükellefiyet arasında vergilendirilecek kazançlar bakımından hiçbir fark bulunmamaktadır",
   "Tam mükellefiyet yalnızca kurumlara, dar mükellefiyet yalnızca gerçek kişilere uygulanabilmektedir",
   "Dar mükellefler hiçbir kazançları üzerinden vergilendirilmez; yalnızca tam mükellefler vergi öder"],
  "GVK m.3-6: Türkiye'de yerleşmiş olan gerçek kişiler (tam mükellef) Türkiye içinde ve dışında elde ettikleri kazançların tamamı üzerinden; Türkiye'de yerleşmemiş olanlar (dar mükellef) yalnızca Türkiye'de elde ettikleri kazançlar üzerinden vergilendirilir.",
  "193 sayılı GVK m.3-6")

q(GV, "gelir_unsurlari", "Gelir Unsurları",
  "Ticari kazançta gerçek usul ve basit usul ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçek usulde kazanç defter kayıtlarına göre; basit usulde ise kanuni koşulları taşıyanlarda daha yalın esaslarla tespit edilir",
  ["Gerçek usul ve basit usul arasında kazancın tespiti bakımından hiçbir fark bulunmamaktadır",
   "Basit usulde kazanç defter kayıtlarına göre, gerçek usulde ise yalın esaslara göre tespit edilir",
   "Ticari kazanç yalnızca basit usulde tespit edilir; gerçek usul diye bir yöntem bulunmamaktadır",
   "Basit usule tabi olmak her mükellefin serbest tercihi olup kanuni koşul aranmamaktadır"],
  "GVK: ticari kazanç gerçek usulde (bilanço veya işletme hesabı esası) defter kayıtlarına dayalı tespit edilir. Kanuni şartları taşıyan küçük esnaf ise basit usulde vergilendirilir; basit usule tabi olmak kanunda sayılan koşullara bağlıdır.",
  "193 sayılı GVK - ticari kazanç usulleri")

q(GV, "beyan_ve_tespit", "Beyan ve Tespit",
  "Gelir vergisinde beyan esası bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelir vergisi kural olarak mükellefin beyanı üzerine tarh olunur; gelir, yıllık beyanname ile beyan edilir",
  ["Gelir vergisi hiçbir hâlde beyanname gerektirmez; vergi tümüyle idarece resen tarh edilmektedir",
   "Gelir vergisinde beyan esası bulunmaz; vergi yalnızca kaynakta kesinti yoluyla tahsil edilmektedir",
   "Yıllık beyanname yalnızca kurumlar vergisi mükelleflerince verilir; gerçek kişiler beyanname vermez",
   "Beyan esası yalnızca dar mükellefler için geçerli olup tam mükellefler beyanname vermemektedir"],
  "GVK: gelir vergisi kural olarak mükellefin (veya sorumlunun) beyanı üzerine tarh olunur; mükellef bir takvim yılı içinde elde ettiği gelir unsurlarını kural olarak yıllık beyanname ile toplar ve beyan eder. Bazı gelirlerde kaynakta kesinti (stopaj) da uygulanır.",
  "193 sayılı GVK - beyan esası")

q(GV, "beyan_ve_tespit", "Beyan ve Tespit",
  "Gelir vergisinde tevkifat (stopaj) bakımından aşağıdakilerden hangisi doğrudur?",
  "Bazı gelirlerde vergi, geliri sağlayan tarafından ödeme sırasında kesilerek vergi dairesine yatırılır",
  ["Tevkifat, mükellefin gelirini beyan ettikten sonra vergiyi tek seferde ödemesini ifade eden bir usuldür",
   "Tevkifat yalnızca kurumlar vergisinde uygulanan bir usul olup gelir vergisiyle ilgisi bulunmamaktadır",
   "Tevkifat, verginin idare tarafından resen hesaplanıp mükelleften talep edilmesini ifade etmektedir",
   "Tevkifat, mükellefin vergisini kanuni süreden önce ödemesi hâlinde idarece yapılan bir iade işlemidir"],
  "GVK m.94: kanunda sayılan ödemeleri (ücret, kira, serbest meslek ödemesi, kâr payı vb.) yapanlar, ödeme sırasında gelir vergisi tevkifatı (stopaj) yaparak keserler ve vergi dairesine yatırır. Bu, verginin kaynakta kesilmesidir.",
  "193 sayılı GVK m.94")

q(GV, "beyan_ve_tespit", "Beyan ve Tespit",
  "Aşağıdakilerden hangileri gelir vergisinin konusuna giren kazanç ve iratlardandır?\n\nI. Serbest meslek kazancı\n\nII. Gayrimenkul sermaye iradı\n\nIII. Kurum kazancı",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Serbest meslek kazancı (I) ve gayrimenkul sermaye iradı (II) GVK m.2'de sayılan gelir unsurlarındandır. Kurum kazancı (III) ise gelir vergisinin değil, kurumlar vergisinin konusudur. Doğru: I ve II.",
  "193 sayılı GVK m.2")

# ══ KURUMLAR VERGİSİ (6) ══════════════════════════════════════════════════
q(KV, "kurumlar_mukellefiyeti", "Kurumlar Mükellefiyeti",
  "Kurumlar vergisinin mükellefleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Sermaye şirketleri, kooperatifler, iktisadi kamu kuruluşları ve dernek-vakıf iktisadi işletmeleri kurumlar vergisi mükellefidir",
  ["Kurumlar vergisinin mükellefi yalnızca gerçek kişiler olup tüzel kişiler bu verginin konusuna girmez",
   "Kurumlar vergisi yalnızca anonim şirketlerden alınır; limited şirket ve kooperatifler kapsam dışıdır",
   "Dernek ve vakıflar her hâlde kurumlar vergisi mükellefidir; iktisadi işletme koşulu aranmamaktadır",
   "Kurumlar vergisinin mükellefleri kanunda sayılmamış olup idare dilediği kuruluşu mükellef sayabilir"],
  "KVK m.1: sermaye şirketleri, kooperatifler, iktisadi kamu kuruluşları, dernek veya vakıflara ait iktisadi işletmeler ve iş ortaklıkları kurumlar vergisi mükellefidir. Kurum kazancı gelir vergisi konusuna giren gelir unsurlarından oluşur.",
  "5520 sayılı KVK m.1", "easy")

q(KV, "kurumlar_mukellefiyeti", "Kurumlar Mükellefiyeti",
  "Kurumlar vergisinde tam ve dar mükellefiyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanuni veya iş merkezi Türkiye'de bulunan kurumlar tam mükellef olup dünya genelindeki kazançları üzerinden vergilendirilir",
  ["Kanuni merkezi Türkiye'de olan kurumlar dar mükellef sayılır ve yalnızca yurt dışı kazançları vergilendirilir",
   "Kurumlar vergisinde tam ve dar mükellefiyet ayrımı bulunmayıp tüm kurumlar aynı esasa tabidir",
   "Tam mükellef kurumlar yalnızca Türkiye'deki kazançları üzerinden vergilendirilir; yurt dışı kazanç hariçtir",
   "Dar mükellef kurumlar Türkiye içi ve dışı tüm kazançları üzerinden tam mükellef gibi vergilendirilir"],
  "KVK m.3: kanuni merkezi veya iş merkezi Türkiye'de bulunan kurumlar tam mükelleftir ve gerek Türkiye içinde gerek dışında elde ettikleri kazançların tamamı üzerinden vergilendirilir. Her ikisi de Türkiye'de bulunmayanlar dar mükellef olup yalnızca Türkiye'deki kazançları vergilendirilir.",
  "5520 sayılı KVK m.3")

q(KV, "kurum_kazanci", "Kurum Kazancı",
  "Kurum kazancının niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Kurum kazancı, gelir vergisinin konusuna giren gelir unsurlarından oluşur ve bir bütün olarak vergilendirilir",
  ["Kurum kazancı yalnızca ticari kazançtan oluşur; kurumun diğer gelir unsurları kazanca dâhil edilmez",
   "Kurum kazancı her gelir unsuru için ayrı ayrı ve farklı oranlarla vergilendirilen bir kazanç türüdür",
   "Kurum kazancının nasıl belirleneceği kanunda düzenlenmemiş olup idarenin takdirine bırakılmıştır",
   "Kurum kazancı yalnızca kurumun dağıttığı kâr payından ibaret olup dağıtılmayan kazanç vergilendirilmez"],
  "KVK m.6: kurumlar vergisi, mükelleflerin bir hesap dönemi içinde elde ettikleri safi kurum kazancı üzerinden hesaplanır. Kurum kazancı, gelir vergisinin konusuna giren gelir unsurlarından oluşur ve bir bütün olarak kurum kazancı kabul edilir.",
  "5520 sayılı KVK m.6")

q(KV, "kurum_kazanci", "Kurum Kazancı",
  "Kurumlar vergisinde safi kurum kazancının tespiti bakımından aşağıdakilerden hangisi doğrudur?",
  "Safi kurum kazancı ticari kazanç gibi tespit edilir; kanunen kabul edilmeyen giderler indirilemez, matraha eklenir",
  ["Safi kurum kazancı, hiçbir gider indirilmeksizin brüt hasılatın tamamı üzerinden hesaplanmaktadır",
   "Safi kurum kazancının tespitinde kanunen kabul edilmeyen giderler de serbestçe indirilebilmektedir",
   "Safi kurum kazancı yalnızca kurumun kasasındaki nakit mevcuduna göre belirlenen bir tutardır",
   "Safi kurum kazancının tespitinde hiçbir gider indirimi kabul edilmez; tüm giderler kâra eklenir"],
  "KVK m.6: safi kurum kazancının tespitinde GVK'nın ticari kazanç hükümleri uygulanır. Hasılattan indirilecek giderler ile kanunen kabul edilmeyen giderler (KKEG) ayrımı yapılır; KKEG matraha eklenir, indirilemez.",
  "5520 sayılı KVK m.6, 11")

q(KV, "kurum_kazanci", "Kurum Kazancı",
  "İştirak kazançları istisnası bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir kurumun tam mükellef başka bir kurumun sermayesine katılımından elde ettiği kazançlar kural olarak kurumlar vergisinden istisnadır",
  ["İştirak kazançları her hâlde kurumlar vergisine tabi olup hiçbir istisna öngörülmemiştir",
   "İştirak kazançları istisnası yalnızca gerçek kişilere uygulanır; kurumlar bu istisnadan yararlanamaz",
   "İştirak kazançları istisnasının amacı kâr payının yalnızca dağıtan kurumda vergilendirilmesini engellemektir",
   "İştirak kazançları istisnası yalnızca dar mükellef kurumlara ve yurt dışı iştiraklere uygulanmaktadır"],
  "KVK m.5: tam mükellef bir kurumun, tam mükellef başka bir kurumun sermayesine iştirakinden elde ettiği kazançlar kurumlar vergisinden istisnadır. Amaç, aynı kazancın hem iştirak edilen hem iştirak eden kurumda mükerrer vergilendirilmesini önlemektir.",
  "5520 sayılı KVK m.5 - iştirak kazançları istisnası")

q(KV, "kurum_kazanci", "Kurum Kazancı",
  "Kurumlar vergisinde beyan ve hesap dönemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kurumlar vergisi, mükellefin beyanı üzerine tarh olunur ve kural olarak hesap dönemi takvim yılıdır",
  ["Kurumlar vergisi beyanname gerektirmez; vergi her hâlde idarece resen tarh edilerek mükelleften istenir",
   "Kurumlar vergisinde hesap dönemi diye bir kavram bulunmayıp vergi her ay ayrı ayrı beyan edilmektedir",
   "Kurumlar vergisi yalnızca kurumun kâr dağıtması hâlinde doğar; dağıtılmayan kazanç hiç beyan edilmez",
   "Kurumlar vergisi beyannamesini kurum değil, doğrudan ortakları kendi adlarına ayrı ayrı vermektedir"],
  "KVK m.14, 16: kurumlar vergisi mükellefin beyanı üzerine tarh olunur; beyan, ilgili hesap dönemi sonuçlarını içerir. Hesap dönemi kural olarak takvim yılıdır; özel hesap dönemi tayin edilenlerde bu dönem esas alınır.",
  "5520 sayılı KVK m.14, 16")

q(KV, "kurumlar_mukellefiyeti", "Kurumlar Mükellefiyeti",
  "Aşağıdakilerden hangileri kurumlar vergisi mükellefidir?\n\nI. Sermaye şirketleri\n\nII. Kooperatifler\n\nIII. Adi ortaklıklar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sermaye şirketleri (I) ve kooperatifler (II) KVK m.1'de sayılan kurumlar vergisi mükellefidir. Adi ortaklık (III) ise tüzel kişiliği bulunmadığından ayrı bir kurumlar vergisi mükellefi değildir; kazancı ortaklarına pay edilerek vergilendirilir. Doğru: I ve II.",
  "5520 sayılı KVK m.1")

# ══ KATMA DEĞER VERGİSİ (7) ═══════════════════════════════════════════════
q(KDV, "kdv_mekanizmasi", "KDV Mekanizması",
  "Katma değer vergisinin konusu bakımından aşağıdakilerden hangisi doğrudur?",
  "Türkiye'de yapılan ticari, sınai, zirai faaliyet ve serbest meslek faaliyeti çerçevesindeki teslim ve hizmetler ile ithalat KDV'nin konusuna girer",
  ["KDV yalnızca ithalattan alınır; yurt içinde yapılan teslim ve hizmetler verginin konusuna girmemektedir",
   "KDV yalnızca nihai tüketicinin doğrudan devlete ödediği ve işletmeleri hiç ilgilendirmeyen bir vergidir",
   "KDV'nin konusu kanunda belirlenmemiş olup idare her türlü işlemi vergiye tabi tutabilmektedir",
   "KDV yalnızca gerçek kişilerin yaptığı teslimlere uygulanır; şirketlerin teslimleri kapsam dışıdır"],
  "KDVK m.1: Türkiye'de yapılan ticari, sınai, zirai faaliyet ve serbest meslek faaliyeti çerçevesindeki teslim ve hizmetler, her türlü mal ve hizmet ithalatı ile diğer faaliyetlerden doğan teslim ve hizmetler KDV'nin konusunu oluşturur.",
  "3065 sayılı KDVK m.1", "easy")

q(KDV, "kdv_mekanizmasi", "KDV Mekanizması",
  "Katma değer vergisinde vergiyi doğuran olay bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak malın teslimi veya hizmetin yapılması anında vergiyi doğuran olay gerçekleşir",
  ["Vergiyi doğuran olay, her hâlde bedelin nakden tahsil edildiği anda ve yalnızca o anda gerçekleşir",
   "Vergiyi doğuran olay, malın üretildiği anda gerçekleşir; teslim edilip edilmemesi önem taşımaz",
   "KDV'de vergiyi doğuran olay diye bir kavram bulunmayıp vergi yıl sonunda toplu olarak doğar",
   "Vergiyi doğuran olay, yalnızca faturanın düzenlendiği anda gerçekleşir; teslim dikkate alınmaz"],
  "KDVK m.10: vergiyi doğuran olay, kural olarak malın teslimi veya hizmetin ifası anında meydana gelir. Fatura önce düzenlenirse fatura tutarıyla sınırlı olarak, kısım kısım teslimde her kısmın tesliminde vergiyi doğuran olay gerçekleşir.",
  "3065 sayılı KDVK m.10")

q(KDV, "kdv_mekanizmasi", "KDV Mekanizması",
  "KDV'nin yansıtılması bakımından aşağıdakilerden hangisi doğrudur?",
  "KDV, her aşamada eklenen değer üzerinden alınır ve indirim mekanizmasıyla nihayetinde nihai tüketici üzerinde kalır",
  ["KDV her aşamada mükellefin üzerinde kalır; nihai tüketiciye hiçbir biçimde yansıtılamamaktadır",
   "KDV yalnızca üretim aşamasında bir kez alınır; sonraki aşamalarda tekrar KDV hesaplanmamaktadır",
   "KDV'de indirim mekanizması bulunmadığından vergi her aşamada mükerrer olarak birikmektedir",
   "KDV yalnızca ilk satıcının ödediği bir vergi olup zincirdeki diğer satıcıları hiç ilgilendirmez"],
  "KDV, üretim-dağıtım zincirinin her aşamasında yaratılan katma değer üzerinden alınır. Mükellef hesapladığı KDV'den yüklendiği KDV'yi indirir; vergi indirim mekanizmasıyla aşama aşama devrederek nihai tüketici üzerinde kalır.",
  "3065 sayılı KDVK - yansıma")

q(KDV, "kdv_teslim_ve_indirim", "KDV Teslim ve İndirim",
  "KDV'de indirim mekanizması bakımından aşağıdakilerden hangisi doğrudur?",
  "Mükellef, teslim ve hizmetleri üzerinden hesapladığı KDV'den, kendisine yapılan teslim ve hizmetler nedeniyle yüklendiği KDV'yi indirir",
  ["Mükellef yüklendiği KDV'yi hiçbir hâlde indiremez; hesapladığı KDV'nin tamamını vergi dairesine öder",
   "Mükellef yalnızca nakden tahsil ettiği KDV'yi indirebilir; henüz tahsil edilmemiş KDV indirilemez",
   "İndirim mekanizması yalnızca ihracatçılara tanınmış olup yurt içi mükelleflerini kapsamamaktadır",
   "Mükellef hesapladığı KDV yerine yüklendiği KDV'yi vergi dairesine öder; ikisi yer değiştirir"],
  "KDVK m.29: mükellefler, yaptıkları teslim ve hizmetler üzerinden hesapladıkları KDV'den, kendilerine yapılan teslim ve hizmetler dolayısıyla yüklendikleri (fatura vb. belgelerde gösterilen) KDV'yi indirebilir.",
  "3065 sayılı KDVK m.29")

q(KDV, "kdv_teslim_ve_indirim", "KDV Teslim ve İndirim",
  "Sonraki döneme devreden KDV bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir vergilendirme döneminde indirilecek KDV, hesaplanan KDV'den fazlaysa aradaki fark sonraki döneme devredilir",
  ["İndirilecek KDV hesaplanan KDV'den fazlaysa aradaki fark mükellefe her hâlde derhâl nakden iade edilir",
   "İndirilecek KDV hesaplanan KDV'den fazla olsa dahi fark dikkate alınmaz ve mükellef lehine hiçbir sonuç doğmaz",
   "İndirilecek KDV ile hesaplanan KDV arasındaki fark her hâlde ceza olarak mükelleften ayrıca tahsil edilir",
   "Devreden KDV yalnızca yıl sonunda bir kez hesaplanır; aylık dönemlerde devir söz konusu değildir"],
  "KDVK m.29: bir vergilendirme döneminde indirilecek KDV toplamı, hesaplanan KDV'den fazla olduğu takdirde aradaki fark sonraki döneme devrolunur; kural olarak iade edilmez (iade yalnızca kanunda öngörülen istisna/özel hâllerde mümkündür).",
  "3065 sayılı KDVK m.29 - devreden KDV")

q(KDV, "kdv_teslim_ve_indirim", "KDV Teslim ve İndirim",
  "İndirilemeyecek KDV bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiye tabi olmayan veya istisna edilmiş işlemlerle ilgili yüklenilen KDV ile kanunda sayılan bazı giderlere ait KDV indirilemez",
  ["Mükellefin yüklendiği her türlü KDV hiçbir sınır olmaksızın ve her hâlde indirilebilmektedir",
   "İndirilemeyecek KDV diye bir kavram bulunmayıp tüm yüklenilen KDV her koşulda indirim konusu yapılır",
   "Yalnızca ihraç edilen mallara ait KDV indirilemez; yurt içi teslimlerin KDV'si her hâlde indirilir",
   "İndirilemeyecek KDV yalnızca ithalatta söz konusu olup yurt içi alımlarda böyle bir sınır yoktur"],
  "KDVK m.30: vergiye tabi olmayan veya vergiden istisna edilmiş işlemlerle ilgili yüklenilen KDV, kanunen kabul edilmeyen giderlere ilişkin KDV ve kanunda sayılan diğer hâllerdeki KDV indirim konusu yapılamaz.",
  "3065 sayılı KDVK m.30")

q(KDV, "kdv_mekanizmasi", "KDV Mekanizması",
  "Aşağıdaki ifadelerden hangileri katma değer vergisi bakımından doğrudur?\n\nI. KDV harcama üzerinden alınan dolaylı bir vergidir\n\nII. Mükellef hesapladığı KDV'den yüklendiği KDV'yi indirir\n\nIII. KDV yükü nihai tüketici yerine ilk üretici üzerinde kalır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "KDV harcama üzerinden alınan dolaylı bir vergidir (I) ve mükellef hesapladığı KDV'den yüklendiğini indirir (II). İndirim mekanizması sayesinde vergi yükü ilk üretici üzerinde değil nihai tüketici üzerinde kalır; bu nedenle III yanlıştır. Doğru: I ve II.",
  "3065 sayılı KDVK m.1, 29")

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
            "id": f"{prefix}-{i+1:04d}", "lessonId": it["lesson"], "topicId": it["topic"],
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
    for items, name, prefix, seed in ((t2, "questions_vergi_test2_2026.json", "vergi-t2", 20260809),
                                      (t3, "questions_vergi_test3_2026.json", "vergi-t3", 20260810)):
        data = emit(items, prefix, seed)
        json.dump(data, open(f"{APP}/{name}", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{name}: {len(data)} soru | harf {''.join(x['correctAnswer'] for x in data)}")
