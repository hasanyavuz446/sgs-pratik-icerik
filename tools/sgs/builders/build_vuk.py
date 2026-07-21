# -*- coding: utf-8 -*-
"""SGS — Vergi Hukuku / Vergi Usul Kanunu (VUK) — 60 soru.

Baba isteği (2026-07-18): "Vergi hukuku VUK".
Kaynak: 213 sayılı VUK. SGS seviyesi: mükellefiyet, süreler, tarh türleri, vergi
alacağının sona ermesi, değerleme, amortisman, defter-belge, denetim, ceza.
ÖZGÜN — kitap/TESMER metni kopyalanmaz.

★ Şık örüntüsü BAŞTAN temiz (Konu 1'in dersi): doğru şık çeldiricilerle AYNI
register/boyda tek cümle; dolgu ("…zorunda bulunmaktadır") YOK; doğru sistematik
en uzun/en kısa DEĞİL; harf gen_letters ile dengeli. __main__ kör-öğrenciyi
ölçüp ≤%30 değilse HATA verir.

⚠ YILA-BAĞLI oran/tutar SORULMAZ (fatura haddi, doğrudan gider sınırı, amortisman
tutarı, ceza tutarları yıldan yıla değişir → güncellik=0). Yalnız kanunda SABİT
yapısal içerik: tarh türü, süre (7 gün fatura, 5 yıl zamanaşımı/saklama, 15 gün
pişmanlık, 30 gün uzlaşma), değerleme ölçüsü tanımı, belge/defter türü, ceza türü,
amortismanda "azalan bakiyede oran normalin 2 katı, %50 tavan" (kanunda sabit).
"""
import json
import random

DERS, KONU = "vergi_hukuku", "vergi_usul_kanunu"
PREFIX, SEED = "vuk-gen", 20260719
OUT_APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/vergi_hukuku/vergi_usul_kanunu.json"
OUT_CONTENT = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/vergi_usul_kanunu.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

# ── A. Mükellef, sorumlu, vergiyi doğuran olay, ehliyet (8) ───────────────────
q("Vergi mükellefi bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi kanunlarına göre kendisine vergi borcu düşen gerçek veya tüzel kişidir",
  ["Vergiyi kendi malvarlığından değil, başkası adına kesip yatıran aracı kişidir",
   "Yalnızca ticari kazanç elde eden ve tacir sıfatı taşıyan gerçek kişilerdir",
   "Verginin tarhından tahsiline kadar tüm işlemleri yürüten vergi dairesidir",
   "Vergi borcundan hiçbir biçimde sorumlu tutulamayan üçüncü kişilerdir"],
  "VUK m.8: mükellef, vergi kanunlarına göre kendisine vergi borcu düşen gerçek veya tüzel kişidir.",
  "VUK m.8 - mükellef"),

q("Vergi sorumlusu bakımından aşağıdakilerden hangisi doğrudur?",
  "Verginin ödenmesi bakımından alacaklı vergi dairesine karşı muhatap olan kişidir",
  ["Kendi kazancı üzerinden doğan vergiyi bizzat beyan edip ödeyen asıl borçludur",
   "Vergi borcu hiçbir koşulda kendisine yöneltilemeyen tamamen bağımsız kişidir",
   "Yalnızca vergi incelemesi sırasında geçici olarak belirlenen kişidir",
   "Vergi affı çıkması hâlinde borçtan kendiliğinden kurtulan tek kişidir"],
  "VUK m.8: vergi sorumlusu, verginin ödenmesi bakımından vergi dairesine muhatap olan kişidir (örn. işverenin ücretten kestiği stopaj).",
  "VUK m.8 - vergi sorumlusu"),

q("Vergiyi doğuran olay bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi alacağı, kanunun vergiyi bağladığı olayın gerçekleşmesiyle doğar",
  ["Vergi alacağı, ancak verginin fiilen tahsil edilmesiyle doğmuş sayılır",
   "Vergi alacağı, mükellefin beyanname vermesinden bağımsız olarak hiç doğmaz",
   "Vergi alacağı, yalnızca vergi dairesinin takdir kararıyla doğabilir",
   "Vergi alacağı, mükellefin işe başlama bildiriminin onaylanmasıyla doğar"],
  "VUK m.19: vergi alacağı, vergi kanunlarının vergiyi bağladığı olayın vukuu veya hukuki durumun tekemmülü ile doğar.",
  "VUK m.19 - vergiyi doğuran olay"),

q("Vergi ehliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Mükellefiyet için kanuni ehliyet şart değildir; küçük ve kısıtlı da mükellef olabilir",
  ["Mükellef olabilmek için her hâlde medeni hakları kullanma ehliyeti aranır",
   "Küçükler ve kısıtlılar hiçbir vergi ödevinin muhatabı olamayan kişilerdir",
   "Vergi ehliyeti yalnızca on sekiz yaşını dolduran gerçek kişilerde bulunur",
   "Tüzel kişiler ehliyet taşımadığından mükellefiyetleri kanunen mümkün değildir"],
  "VUK m.9: mükellefiyet için kanuni ehliyet şart değildir; küçük veya kısıtlı da vergiyi doğuran olayla mükellef olur, ödevleri kanuni temsilcilerce yerine getirilir.",
  "VUK m.9 - vergi ehliyeti"),

q("Kanuni temsilcinin ödevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Küçük, kısıtlı ve tüzel kişilerin vergi ödevleri kanuni temsilcilerince yerine getirilir",
  ["Kanuni temsilci, temsil ettiği kişinin hiçbir vergi ödevinden sorumlu tutulamaz",
   "Tüzel kişilerin ödevleri ortaklarca değil, yalnızca vergi dairesince yerine getirilir",
   "Kanuni temsilci ancak mahkeme kararıyla her olayda ayrıca görevlendirilir",
   "Temsilcinin ödevi yalnızca beyanname imzalamakla sınırlı olan biçimsel bir görevdir"],
  "VUK m.10: tüzel kişilerle küçük ve kısıtlıların ödevleri kanuni temsilcileri; tüzel kişiliği olmayan teşekküllerde ise idare edenler tarafından yerine getirilir.",
  "VUK m.10 - kanuni temsilci"),

q("Müteselsil sorumluluk kapsamında mal alım-satımında aşağıdakilerden hangisi doğrudur?",
  "Alım-satıma taraf olanlar, vergi kesenin ödemesi gereken vergiden zincirleme sorumlu olabilir",
  ["Alım-satıma taraf olanların birbirinin vergisinden sorumluluğu hiçbir hâlde doğmaz",
   "Müteselsil sorumluluk yalnızca aynı aileden olan mükellefler arasında geçerlidir",
   "Zincirleme sorumluluk yalnızca ithalat işlemlerinde ve gümrükte söz konusu olur",
   "Bu sorumluluk yalnızca vergi dairesinin yazılı onayı alındığında ortaya çıkar"],
  "VUK m.11: mal alım-satımı ve hizmet ifası dolayısıyla vergi kesenler ile taraf olanlar, kesilen verginin ödenmesinden müteselsilen sorumlu tutulabilir.",
  "VUK m.11 - müteselsil sorumluluk"),

q("İşe başlamayı bildirme ödevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiye tabi ticaret ve sanatla uğraşanlar işe başlamayı vergi dairesine bildirmekle yükümlüdür",
  ["İşe başlama yalnızca ilk yılın sonunda topluca bildirilebilen bir ödevdir",
   "İşe başlamayı bildirme ödevi yalnızca sermaye şirketlerine özgü bir yükümlülüktür",
   "Serbest meslek erbabı işe başlamayı hiçbir biçimde bildirmek durumunda değildir",
   "İşe başlama bildirimi yalnızca ticaret siciline yapılır, vergi dairesi ilgilenmez"],
  "VUK m.153: vergiye tabi ticaret ve sanat erbabı, serbest meslek erbabı ve kurumlar işe başlamayı vergi dairesine bildirmek zorundadır.",
  "VUK m.153 - işe başlamayı bildirme"),


# ── B. Süreler, mücbir sebep, zor durum, tebliğ (8) ──────────────────────────
q("Kanuni sürelerin niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanunla belirlenen süreler kural olarak kesin olup idarece uzatılıp kısaltılamaz",
  ["Kanuni süreler her mükellef için vergi dairesince serbestçe belirlenebilir",
   "Kanuni süreler yalnızca mükellef talep ederse işlemeye başlayan sürelerdir",
   "Kanunla konulan süreler idarece dilendiği zaman geriye yürütülerek değiştirilir",
   "Kanuni süreler yalnızca resmî tatil günlerinde işleyen özel sürelerdir"],
  "VUK m.14: süreler kanunla belirlenir; kanunda açıkça yazılı olmayan hâllerde 15 günden aşağı olmamak üzere ilgili idare belli eder.",
  "VUK m.14 - kanuni süreler"),

q("Mücbir sebep bakımından aşağıdakilerden hangisi doğrudur?",
  "Mücbir sebebin devam ettiği sürece kanuni süreler işlemez, durur",
  ["Mücbir sebep süreleri hiçbir biçimde etkilemez; süreler aynen işlemeye devam eder",
   "Mücbir sebep yalnızca vergi borcunu tümüyle ortadan kaldıran bir sona erme sebebidir",
   "Mücbir sebep hâlinde süreler durmaz, aksine yarı yarıya kısalarak işler",
   "Mücbir sebep yalnızca doğal afetleri kapsar; ağır hastalık buna dâhil değildir"],
  "VUK m.15: mücbir sebeplerden biri bulunursa, bu sebep ortadan kalkıncaya kadar süreler işlemez; tarh zamanaşımı da işlemeyen süre kadar uzar.",
  "VUK m.15 - mücbir sebep"),

q("Zor durum nedeniyle süre verilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Zor durumda olanlara, ödevin yerine getirileceği sürenin bir katını geçmemek üzere ek süre verilebilir",
  ["Zor durumda olanlara hiçbir koşulda ek süre verilmesi mümkün değildir",
   "Zor durum ek süresi her hâlde asıl sürenin en az beş katı olarak belirlenir",
   "Ek süre yalnızca vergi mahkemesinin vereceği kararla tanınabilen bir haktır",
   "Zor durum süresi yalnızca mücbir sebep hâllerinde kendiliğinden başlar"],
  "VUK m.17: zor durumda bulunmaları nedeniyle ödevleri süresinde yerine getiremeyeceklere, kanuni sürenin bir katını geçmemek üzere idarece uygun süre verilebilir.",
  "VUK m.17 - zor durum"),

q("Tebliğin muhatabı bakımından aşağıdakilerden hangisi doğrudur?",
  "Tebliğ, mükellefe, kanuni temsilcisine, umumi vekiline veya vergi sorumlusuna yapılır",
  ["Tebliğ yalnızca mükellefin bizzat kendisine yapılabilir; temsilciye yapılamaz",
   "Tebliğ, muhatabın komşusuna yapıldığında hiçbir hâlde geçerli sayılmaz",
   "Tebliğ yalnızca vergi dairesi binasında elden teslimle yapılabilir",
   "Tüzel kişilere tebliğ, herhangi bir çalışana değil yalnızca kurucu ortağa yapılır"],
  "VUK m.94: tebliğ; mükelleflere, kanuni temsilcilerine, umumi vekillerine veya vergi sorumlularına yapılır.",
  "VUK m.94 - tebliğin muhatabı"),

q("Tebliğ usulleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Tebliğ; posta, memur eliyle, ilan veya elektronik ortam yoluyla yapılabilir",
  ["Tebliğ yalnızca iadeli taahhütlü posta yoluyla yapılabilen tek usule bağlıdır",
   "Elektronik tebliğ hukuken geçersiz olup yalnızca kâğıt tebligat sonuç doğurur",
   "İlan yoluyla tebliğ VUK'ta yer almayan ve uygulanmayan bir yöntemdir",
   "Memur eliyle tebliğ yalnızca ceza ihbarnameleri için istisnaen kullanılır"],
  "VUK m.93 vd.: tebliğ posta ile, memur eliyle, ilan yoluyla ve elektronik ortamda yapılabilir.",
  "VUK m.93 - tebliğ usulleri"),

q("Elektronik tebligat bakımından aşağıdakilerden hangisi doğrudur?",
  "Elektronik ortamda yapılan tebliğ, muhatabın adresine ulaştığı tarihi izleyen beşinci günün sonunda yapılmış sayılır",
  ["Elektronik tebligat, gönderildiği an muhatap görmese de derhâl yapılmış sayılır",
   "Elektronik tebligat yalnızca mükellef onay verdiği her seferde geçerli olur",
   "Elektronik tebligatın hukuki sonucu ancak kâğıt nüsha da gönderilirse doğar",
   "Elektronik tebligat yalnızca kamu kurumlarına yapılabilen bir yöntemdir"],
  "VUK m.107/A: elektronik imzalı tebliğ evrakı, muhatabın elektronik adresine ulaştığı tarihi izleyen beşinci günün sonunda tebliğ edilmiş sayılır.",
  "VUK m.107/A - elektronik tebligat"),

q("Tebliğ yerine geçen işlemler bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilinen adreste bulunamama veya adres yanlışlığında ilan yoluyla tebliğ yapılabilir",
  ["Adres bulunamadığında tebliğ ödevi tamamen ortadan kalkar ve vergi silinir",
   "İlan yoluyla tebliğ yalnızca mükellef yabancı uyruklu ise uygulanabilir",
   "Adres yanlışsa tebliğ yapılmış sayılır ve ayrıca ilana gerek görülmez",
   "İlan tebliği yalnızca gazete yerine vergi dairesi kapısına asmakla yapılır"],
  "VUK m.103: muhatabın bilinen adresi yoksa, adreste bulunamazsa veya tebliğ yapılamazsa ilan yoluyla tebliğ edilir.",
  "VUK m.103 - ilan yoluyla tebliğ"),

q("Sürelerin hesaplanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Süre gün olarak belliyse başladığı gün sayılmaz, son günün tatile gelmesi hâlinde süre izleyen iş günü biter",
  ["Süreler her hâlde başladığı gün dâhil edilerek ve tatiller de sayılarak hesaplanır",
   "Sürenin son günü tatile gelirse süre o gün sona erer ve uzamaz",
   "Ay olarak belirlenen süreler her zaman otuz gün kabul edilerek hesaplanır",
   "Süre hesabında yalnızca vergi dairesinin çalıştığı günler tek tek toplanır"],
  "VUK m.18: süre gün ise başladığı gün hesaba katılmaz, son gün akşamı biter; son gün resmî tatilse tatili izleyen ilk iş günü mesai saati sonunda biter.",
  "VUK m.18 - sürelerin hesabı"),

# ── C. Tarh türleri, tahakkuk, düzeltme (8) ──────────────────────────────────
q("Verginin tarhı bakımından aşağıdakilerden hangisi doğrudur?",
  "Tarh, vergi alacağının kanundaki matrah ve oranlar üzerinden hesaplanarak miktarının belirlenmesidir",
  ["Tarh, hesaplanan verginin mükelleften fiilen tahsil edilmesi işlemidir",
   "Tarh, verginin ödenmesi gereken safhaya gelmesini ifade eden tahakkuktur",
   "Tarh, mükellefin beyannamesini vergi dairesine teslim etmesi işlemidir",
   "Tarh, kesinleşen vergiye karşı dava açılması sürecinin adıdır"],
  "VUK m.20: verginin tarhı, vergi alacağının kanunda gösterilen matrah ve nispetler üzerinden vergi dairesince hesaplanarak miktarının belirlenmesidir.",
  "VUK m.20 - tarh"),

q("Beyana dayanan tarh bakımından aşağıdakilerden hangisi doğrudur?",
  "Mükellefin veya sorumlunun beyan ettiği matrah üzerinden yapılan tarhtır",
  ["Mükellefin hiç beyanı olmadan idarenin resen takdiriyle yapılan tarhtır",
   "Vergi incelemesi sonucu bulunan farklar üzerinden yapılan ek tarhtır",
   "Yalnızca vergi dairesinin kendi kayıtlarından hareketle yaptığı tarhtır",
   "Takdir komisyonu kararına dayanılarak belirlenen matrah üzerinden tarhtır"],
  "Beyana dayanan tarhta matrah mükellefin/sorumlunun beyanına göre belirlenir; verginin normal ve asıl tarh usulüdür.",
  "VUK - beyana dayanan tarh"),

q("İkmalen vergi tarhı bakımından aşağıdakilerden hangisi doğrudur?",
  "Defter, kayıt ve belgelere veya kanuni ölçülere dayanılarak saptanan matrah farkı üzerinden yapılan tarhtır",
  ["Hiçbir defter ve belge bulunmadan tümüyle takdirle yapılan re'sen tarhtır",
   "Mükellefin ilk beyanı üzerinden hiç fark aranmadan yapılan olağan tarhtır",
   "Yalnızca mükellefin talebi üzerine matrahı düşürmek için yapılan tarhtır",
   "Vergi dairesinin maddi hatasını düzeltmek amacıyla yapılan düzeltme tarhıdır"],
  "VUK m.29: ikmalen tarh, bir vergi tarh edildikten sonra defter, kayıt ve belgelere veya kanuni ölçülere göre saptanan matrah farkı üzerinden yapılır.",
  "VUK m.29 - ikmalen tarh"),

q("Re'sen vergi tarhı bakımından aşağıdakilerden hangisi doğrudur?",
  "Matrahın defter-belge veya kanuni ölçülerle saptanamaması hâlinde takdir yoluyla yapılan tarhtır",
  ["Mükellefin eksiksiz beyanı üzerinden hiç takdire gerek olmadan yapılan tarhtır",
   "Yalnızca vergi dairesinin hesap hatasını gidermek için yaptığı düzeltmedir",
   "Defterler tam ve düzenli olduğunda tercihen başvurulan olağan tarh yöntemidir",
   "Mükellefin başvurusu üzerine matrahı artırmak için isteğe bağlı yapılan tarhtır"],
  "VUK m.30: re'sen tarh, matrahın defter, kayıt ve belgelere veya kanuni ölçülere göre tespitine imkân bulunmayan hâllerde takdir olunan matrah üzerinden yapılır.",
  "VUK m.30 - re'sen tarh"),

q("Verginin tahakkuku bakımından aşağıdakilerden hangisi doğrudur?",
  "Tahakkuk, tarh ve tebliğ edilen verginin ödenmesi gereken safhaya gelmesidir",
  ["Tahakkuk, verginin mükellef tarafından fiilen ödenmesi işlemidir",
   "Tahakkuk, vergi alacağının matrah üzerinden ilk kez hesaplanmasıdır",
   "Tahakkuk, mükellefe vergi ihbarnamesinin posta ile gönderilmesidir",
   "Tahakkuk, kesinleşen vergiye karşı uzlaşma talebinde bulunulmasıdır"],
  "VUK m.22: verginin tahakkuku, tarh ve tebliğ edilen verginin ödenmesi gereken bir safhaya gelmesidir.",
  "VUK m.22 - tahakkuk"),


q("Vergi hatalarında düzeltme bakımından aşağıdakilerden hangisi doğrudur?",
  "Hesap hataları ve vergilendirme hataları, dava açma yerine düzeltme yoluyla da giderilebilir",
  ["Vergi hataları yalnızca vergi mahkemesinde dava açılarak giderilebilir",
   "Düzeltme yalnızca mükellef lehine hataları kapsar, aleyhe hatalar düzeltilemez",
   "Bir hata düzeltildikten sonra hiçbir hâlde şikâyet yoluna başvurulamaz",
   "Düzeltme yalnızca hukuki uyuşmazlıklarda başvurulan bir yargı yoludur"],
  "VUK m.116-126: açık vergi hataları (hesap ve vergilendirme hataları) düzeltme yoluyla giderilebilir; reddedilirse şikâyet yoluyla Bakanlığa gidilir.",
  "VUK m.116 - vergi hatası ve düzeltme"),

q("Hesap hatası ile vergilendirme hatası ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Matrah, miktar ve mükerrer hatalar hesap hatası; mükellefin şahsında veya mevzuunda yanılma vergilendirme hatasıdır",
  ["Her türlü hata, ayrım yapılmaksızın tek bir hesap hatası kategorisinde toplanır",
   "Vergilendirme hataları yalnızca verginin oranında yapılan aritmetik yanlışlıklardır",
   "Hesap hataları yalnızca mükellefin kimliğinin yanlış yazılmasını ifade eder",
   "İki hata türü arasında hukuki sonuç bakımından hiçbir fark bulunmaz"],
  "VUK m.117-118: hesap hataları matrah/vergi miktarında ve mükerrer vergilendirmede; vergilendirme hataları mükellefin şahsında, mükellefiyette, mevzuda ve dönemde olur.",
  "VUK m.117 - hata türleri"),

# ── D. Vergi alacağını sona erdiren haller (8) ───────────────────────────────
q("Vergi borcunu sona erdiren haller bakımından aşağıdakilerden hangisi doğrudur?",
  "Ödeme, zamanaşımı, terkin ve hata düzeltmesi vergi borcunu sona erdiren hâllerdendir",
  ["Vergi borcu yalnızca ödeme ile sona erer; başka hiçbir sebep borcu kaldırmaz",
   "Zamanaşımı vergi borcunu değil yalnızca cezayı sona erdiren tek yoldur",
   "Vergi borcu her hâlde kuşaktan kuşağa geçerek hiçbir zaman sona ermez",
   "Terkin yalnızca cezaların silinmesi anlamına gelir, vergi aslını etkilemez"],
  "Vergi borcunu sona erdiren başlıca hâller: ödeme, zamanaşımı, terkin, tahakkuktan vazgeçme, hata düzeltme, uzlaşma ve aftır.",
  "VUK - vergi borcunu sona erdiren haller"),

q("Tarh (tahakkuk) zamanaşımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergiyi doğuran olayı izleyen yılın başından başlayarak beş yıl içinde tarh edilmeyen vergi zamanaşımına uğrar",
  ["Zamanaşımı süresi her vergi türü için mükellefin talebine göre belirlenir",
   "Vergiyi doğuran olayın olduğu gün başlayıp iki yılda dolan bir süredir",
   "Tarh zamanaşımı yalnızca mükellef dilekçe verdiğinde işlemeye başlar",
   "Zamanaşımı dolsa dahi vergi süresiz olarak tarh edilebilir, süre bağlayıcı değildir"],
  "VUK m.114: vergi alacağının doğduğu takvim yılını takip eden yılın başından başlayarak beş yıl içinde tarh ve tebliğ edilmeyen vergiler zamanaşımına uğrar.",
  "VUK m.114 - tarh zamanaşımı"),


q("Terkin bakımından aşağıdakilerden hangisi doğrudur?",
  "Doğal afetler nedeniyle varlıklarının önemli bölümünü yitirenlerin vergi ve cezaları kısmen veya tamamen terkin edilebilir",
  ["Terkin, her mükellefin talep ettiğinde vergisini silen olağan bir haktır",
   "Terkin yalnızca verginin tahsilinden sonra fazla ödemeyi iade etmektir",
   "Terkin, vergi borcunun taksitlendirilerek ertelenmesi işlemidir",
   "Terkin yalnızca ticari kazanç mükelleflerine tanınan bir vergi indirimidir"],
  "VUK m.115: yangın, yer sarsıntısı, sel gibi afetlerle varlıklarının en az üçte birini yitirenlerin ilgili vergi ve cezaları zararla orantılı olarak terkin edilebilir.",
  "VUK m.115 - terkin"),

q("Uzlaşma bakımından aşağıdakilerden hangisi doğrudur?",
  "Tarhiyat öncesi veya sonrası uzlaşmada vergi ve ceza üzerinde idareyle anlaşma sağlanabilir",
  ["Uzlaşma yalnızca mahkeme kararıyla kesinleşmiş borçlar için istenebilir",
   "Uzlaşmada yalnızca verginin aslı görüşülür, cezalar hiçbir hâlde kapsama girmez",
   "Uzlaşma sağlanan vergi için mükellef ayrıca dava açma hakkını korur",
   "Uzlaşma yalnızca vergi dairesinin tek taraflı olarak vergiyi silmesidir"],
  "VUK Ek m.1 vd.: mükellef, ikmalen/re'sen/idarece tarh edilen vergi ve cezalarda tarhiyat öncesi veya sonrası uzlaşma talep edebilir; uzlaşılan konuda dava açılamaz.",
  "VUK Ek m.1 - uzlaşma"),

q("Uzlaşma talebi süresi bakımından aşağıdakilerden hangisi doğrudur?",
  "Tarhiyat sonrası uzlaşma, vergi/ceza ihbarnamesinin tebliğinden itibaren otuz gün içinde istenir",
  ["Uzlaşma talebi için kanunda herhangi bir süre öngörülmemiştir",
   "Uzlaşma yalnızca ihbarnamenin tebliğinden bir yıl sonra istenebilir",
   "Uzlaşma talebi ancak verginin ödenmesinden sonra ileri sürülebilir",
   "Uzlaşma talebi için tanınan süre her mükellef için ayrı ayrı belirlenir"],
  "VUK Ek m.1: tarhiyat sonrası uzlaşma, vergi/ceza ihbarnamesinin tebliğ tarihinden itibaren 30 gün içinde talep edilir.",
  "VUK Ek m.1 - uzlaşma süresi"),

q("Pişmanlık ve ıslah bakımından aşağıdakilerden hangisi doğrudur?",
  "Kendiliğinden durumu bildiren mükellef, on beş gün içinde beyanname verip vergiyi öderse vergi ziyaı cezası kesilmez",
  ["Pişmanlık her hâlde verginin aslını da tamamen ortadan kaldıran bir aftır",
   "Pişmanlık yalnızca inceleme başladıktan sonra başvurulabilen bir yoldur",
   "Pişmanlıkta bildirimden sonra beyanname vermeye hiç gerek duyulmaz",
   "Pişmanlık yalnızca usulsüzlük cezalarını kaldıran, vergiyi etkilemeyen kurumdur"],
  "VUK m.371: kanuna aykırılığı kendiliğinden haber veren mükellef, haber verme dilekçesinden itibaren 15 gün içinde beyannameyi verip vergi ve gecikme zammını öderse vergi ziyaı cezası kesilmez.",
  "VUK m.371 - pişmanlık ve ıslah"),

q("Vergi cezalarında indirim bakımından aşağıdakilerden hangisi doğrudur?",
  "İhbarnamenin tebliğinden itibaren süresinde başvurup ödeyen mükellefin kesilen cezasında kanuni oranda indirim yapılır",
  ["Vergi cezalarında hiçbir koşulda indirim uygulanması mümkün değildir",
   "İndirim yalnızca dava açıp kazanılması hâlinde geriye dönük uygulanır",
   "Cezada indirim yalnızca verginin aslından tamamen vazgeçilmesiyle olur",
   "İndirimden yararlanmak için cezanın önce iki katına çıkarılması gerekir"],
  "VUK m.376: mükellef, ihbarnamenin tebliğinden itibaren süresinde başvurup vadesinde öderse, kesilen cezalarda kanunda belirlenen oranda indirim uygulanır.",
  "VUK m.376 - cezalarda indirim"),

# ── E. Değerleme ölçüleri + amortisman (8) ───────────────────────────────────
q("Değerleme bakımından aşağıdakilerden hangisi doğrudur?",
  "Değerleme, vergi matrahının hesaplanmasıyla ilgili iktisadi kıymetlerin takdir ve tespitidir",
  ["Değerleme, yalnızca satılan malın peşin fiyatının belirlenmesi işlemidir",
   "Değerleme, iktisadi kıymetlerin yalnızca defterde gösterilen adının yazılmasıdır",
   "Değerleme, verginin mükelleften tahsil edilme yönteminin seçilmesidir",
   "Değerleme, yalnızca dönem sonunda kasadaki nakdin sayılması işlemidir"],
  "VUK m.258: değerleme, vergi matrahlarının hesaplanmasıyla ilgili iktisadi kıymetlerin takdir ve tespitidir.",
  "VUK m.258 - değerleme"),

q("Maliyet bedeli ölçüsü bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet bedeli, bir kıymetin edinilmesi veya değerinin artırılması için yapılan ödemelerle ilgili giderlerin toplamıdır",
  ["Maliyet bedeli, kıymetin ileride satılacağı tahmin edilen satış fiyatıdır",
   "Maliyet bedeli, kıymetin borsada o günkü işlem gördüğü ortalama değerdir",
   "Maliyet bedeli, kıymetin vergi dairesince belirlenen resmî vergi değeridir",
   "Maliyet bedeli, senedin üzerinde yazılı olan nominal (itibari) değeridir"],
  "VUK m.262: maliyet bedeli, iktisadi bir kıymetin iktisap edilmesi veyahut değerinin artırılması dolayısıyla yapılan ödemelerle bunlara ilişkin giderlerin toplamıdır.",
  "VUK m.262 - maliyet bedeli"),

q("Mukayyet (kayıtlı) değer bakımından aşağıdakilerden hangisi doğrudur?",
  "Mukayyet değer, bir kıymetin muhasebe kayıtlarında gösterilen hesap değeridir",
  ["Mukayyet değer, kıymetin serbest piyasada oluşan güncel alım fiyatıdır",
   "Mukayyet değer, senedin ihraç anındaki üzerinde yazılı itibari değeridir",
   "Mukayyet değer, taşınmazın emlak vergisine esas olan vergi değeridir",
   "Mukayyet değer, malın maliyetine kâr eklenmiş satış değeridir"],
  "VUK m.265: mukayyet değer, bir iktisadi kıymetin muhasebe kayıtlarında gösterilen hesap değeridir.",
  "VUK m.265 - mukayyet değer"),

q("İtibari (nominal) değer bakımından aşağıdakilerden hangisi doğrudur?",
  "İtibari değer, her nevi senetle hisse senedi ve tahvillerin üzerinde yazılı olan değerdir",
  ["İtibari değer, senedin piyasada o gün alınıp satıldığı borsa rayicidir",
   "İtibari değer, senedin muhasebe defterinde kayıtlı bulunan hesap değeridir",
   "İtibari değer, kıymetin elde edilmesi için katlanılan maliyet bedelidir",
   "İtibari değer, taşınmazlar için takdir edilen emlak vergi değeridir"],
  "VUK m.266: itibari değer, her nevi senetlerle hisse senedi ve tahvillerin üzerinde yazılı olan değerlerdir.",
  "VUK m.266 - itibari değer"),

q("Emsal bedel bakımından aşağıdakilerden hangisi doğrudur?",
  "Emsal bedel, gerçek bedeli belli olmayan veya bilinmeyen bir malın değerleme günündeki satılabilir değeridir",
  ["Emsal bedel, malın her hâlde maliyetine eşit kabul edilen sabit değeridir",
   "Emsal bedel, yalnızca senetli alacaklar için hesaplanan tasarruf değeridir",
   "Emsal bedel, malın defterde gösterilen kayıtlı (mukayyet) değeridir",
   "Emsal bedel, kıymetin üzerinde yazılı olan itibari değerinden ibarettir"],
  "VUK m.267: emsal bedeli, gerçek bedeli olmayan veya bilinmeyen ya da doğru saptanamayan bir malın değerleme günündeki satılabilir değeridir; ortalama fiyat, maliyet bedeli ve takdir esasıyla sırasıyla belirlenir.",
  "VUK m.267 - emsal bedel"),

q("Amortisman bakımından aşağıdakilerden hangisi doğrudur?",
  "Amortisman, işletmede bir yıldan fazla kullanılan ve yıpranan duran varlıkların değerinin yıllara bölünerek gider yazılmasıdır",
  ["Amortisman, stokların dönem sonunda toplu olarak gider yazılması işlemidir",
   "Amortisman, alacakların tahsil edilemeyen kısmının doğrudan silinmesidir",
   "Amortisman, kasadaki nakdin enflasyona göre yeniden değerlenmesidir",
   "Amortisman, bir yıldan kısa sürede tükenen giderlerin peşin ödenmesidir"],
  "VUK m.313: işletmede bir yıldan fazla kullanılan ve yıpranmaya tabi gayrimenkul benzeri kıymetler için amortisman ayrılarak değer yıllara yayılır.",
  "VUK m.313 - amortisman"),

q("Azalan bakiyeler yöntemiyle amortisman bakımından aşağıdakilerden hangisi doğrudur?",
  "Azalan bakiyede uygulanacak oran normal amortisman oranının iki katıdır ve bu oran yüzde elliyi geçemez",
  ["Azalan bakiye yönteminde oran her yıl mükellefçe serbestçe yeniden belirlenir",
   "Azalan bakiye yöntemi yalnızca binek otomobiller için zorunlu olan usuldür",
   "Azalan bakiyede her yıl sabit ve eşit tutarda amortisman gideri yazılır",
   "Azalan bakiye oranı normal oranın yarısı kadar olup asla artırılamaz"],
  "VUK mük. m.315: azalan bakiyeler usulünde uygulanacak amortisman oranı normal amortisman oranının iki katıdır; ancak bu oran %50'yi geçemez.",
  "VUK mük.315 - azalan bakiye amortismanı"),


# ── F. Şüpheli/değersiz/vazgeçilen alacak + reeskont (6) ──────────────────────
q("Şüpheli alacak karşılığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Dava veya icra safhasındaki alacaklar için şüpheli alacak karşılığı ayrılarak gider yazılabilir",
  ["Her tahsil edilememiş alacak için doğrudan ve koşulsuz karşılık ayrılabilir",
   "Şüpheli alacak karşılığı yalnızca kamu kurumlarından olan alacaklarda ayrılır",
   "Şüpheli alacak karşılığı ancak alacak tamamen değersiz hâle geldiğinde ayrılır",
   "Karşılık ayrılması için alacağın senede bağlanmış olması her hâlde şarttır"],
  "VUK m.323: dava veya icra safhasındaki alacaklarla, protesto edilmiş ya da yazı ile bir defadan fazla istenmiş küçük alacaklar için şüpheli alacak karşılığı ayrılabilir.",
  "VUK m.323 - şüpheli alacak"),

q("Değersiz alacak bakımından aşağıdakilerden hangisi doğrudur?",
  "Kazai bir hükme veya kanaat verici bir vesikaya göre tahsiline artık imkân kalmayan alacaktır",
  ["Yalnızca vadesi henüz gelmemiş ve tahsili beklenen alacaklar değersiz sayılır",
   "Dava veya icra safhasında bulunan, tahsili şüpheli hâldeki alacaktır",
   "Senede bağlanmış olup vadesi ileri bir tarihte dolacak olan alacaktır",
   "Borçlusu tarafından her an ödenebilecek durumdaki sağlam alacaktır"],
  "VUK m.322: kazai bir hükme veya kanaat verici bir vesikaya göre tahsiline artık imkân kalmayan alacaklar değersiz alacaktır ve kayıtlı değeriyle zarara geçirilir.",
  "VUK m.322 - değersiz alacak"),

q("Vazgeçilen alacak bakımından aşağıdakilerden hangisi doğrudur?",
  "Konkordato veya sulh yoluyla alınmasından vazgeçilen ve borçlu için kazanç sayılan alacaktır",
  ["Borçlunun hiç haberi olmadan alacaklının tek taraflı sildiği her alacaktır",
   "Tahsili imkânsız olduğu mahkeme kararıyla saptanan değersiz alacaktır",
   "Dava safhasında bulunan ve karşılık ayrılabilen şüpheli alacaktır",
   "Vadesi gelmediği için henüz istenememiş olan olağan ticari alacaktır"],
  "VUK m.324: konkordato veya sulh yoluyla alınmasından vazgeçilen alacaklar, borçlunun defterlerinde özel bir karşılık hesabına alınır ve üç yıl içinde zararla itfa edilmezse kâr sayılır.",
  "VUK m.324 - vazgeçilen alacak"),


q("Reeskont (senetlerin değerlemesi) bakımından aşağıdakilerden hangisi doğrudur?",
  "Vadesi gelmemiş senede bağlı alacak ve borçlar, değerleme gününde tasarruf değerine indirgenebilir",
  ["Reeskont yalnızca kasadaki nakit mevcudu için yapılan bir değerlemedir",
   "Senede bağlı olmayan açık hesap alacakları da her hâlde reeskonta tabidir",
   "Reeskont, vadesi geçmiş ve tahsil edilemeyen alacakların silinmesidir",
   "Reeskont, duran varlıkların yıpranma payının hesaplanması işlemidir"],
  "VUK m.281/285: vadesi gelmemiş senede bağlı alacaklar ve borçlar, değerleme gününde tasarruf (peşin) değerine indirgenebilir; alacak senetlerini reeskonta tabi tutan borç senetlerini de tutar.",
  "VUK m.281 - reeskont"),


# ── G. Defterler, tasdik, saklama (5) ────────────────────────────────────────
q("Bilanço esasında tutulacak defterler bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilanço esasında yevmiye defteri, defterikebir ve envanter defteri tutulur",
  ["Bilanço esasında yalnızca tek bir işletme hesabı defteri tutulması yeterlidir",
   "Bilanço esasında defter tutmak isteğe bağlı olup hiçbir defter zorunlu değildir",
   "Bilanço esasında yalnızca serbest meslek kazanç defteri tutulur",
   "Bilanço esasında yalnızca alınan ve verilen faturaların dosyalanması yeterlidir"],
  "VUK m.182: bilanço esasında yevmiye defteri, defterikebir ve envanter defteri tutulur.",
  "VUK m.182 - bilanço esası defterleri"),

q("İşletme hesabı esası bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme hesabı esasında bir tarafı gider, diğer tarafı hasılat gösteren işletme hesabı defteri tutulur",
  ["İşletme hesabı esasında yevmiye, kebir ve envanter defteri birlikte tutulur",
   "İşletme hesabı esası yalnızca büyük sermaye şirketlerine tanınan bir usuldür",
   "İşletme hesabı esasında hiçbir defter tutulmaz, yalnızca beyanname verilir",
   "İşletme hesabı esası yalnızca serbest meslek erbabının kullandığı yöntemdir"],
  "VUK m.193-194: işletme hesabı esasında, bir tarafına giderler diğer tarafına hasılat kaydedilen işletme hesabı defteri tutulur.",
  "VUK m.193 - işletme hesabı esası"),

q("Defterlerin tasdiki (tasdik zamanı) bakımından aşağıdakilerden hangisi doğrudur?",
  "Öteden beri işe devam edenler, defterlerini kullanılacağı yıldan önce gelen son ayda tasdik ettirir",
  ["Defterler yalnızca yıl bittikten sonra, izleyen yılın herhangi bir ayında tasdik edilir",
   "Defter tasdiki tümüyle isteğe bağlı olup hiçbir zaman zorunlu değildir",
   "Yeni işe başlayanlar defterlerini ilk yılın sonunda tasdik ettirebilir",
   "Tasdik yalnızca defter dolduğunda ve yeni defter alındığında yapılır"],
  "VUK m.221: öteden beri işe devam edenler, defterin kullanılacağı yıldan önce gelen son ayda (normal hesap döneminde Aralık) tasdik ettirir; yeni işe başlayanlar işe başlamadan önce tasdik ettirir.",
  "VUK m.221 - tasdik zamanı"),

q("Defter ve belgeleri muhafaza süresi bakımından aşağıdakilerden hangisi doğrudur?",
  "Defter ve belgeler, ilgili bulundukları yılı izleyen yıldan başlayarak beş yıl süreyle saklanır",
  ["Defter ve belgeler beyanname verildiği anda imha edilebilir, saklama gerekmez",
   "Defter ve belgeler yalnızca inceleme başladığında bir aylığına saklanır",
   "Defter ve belgelerin saklama süresi mükellefin isteğine göre belirlenir",
   "Defter ve belgeler yalnızca cari yıl boyunca saklanır, yıl bitince atılabilir"],
  "VUK m.253: defter tutmak zorunda olanlar, defter ve belgelerini ilgili bulundukları yılı takip eden takvim yılından başlayarak beş yıl süreyle muhafaza eder.",
  "VUK m.253 - muhafaza süresi"),

q("Defter ve belgeleri ibraz ödevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Muhafaza edilen defter ve belgeler, yetkililerce istendiğinde inceleme için ibraz edilmek zorundadır",
  ["Muhafaza edilen defterler hiçbir hâlde vergi incelemesine ibraz edilemez",
   "İbraz ödevi yalnızca mükellefin kendi isteğiyle sunduğu belgeler için doğar",
   "Defterler yalnızca mahkeme kararı olmadıkça hiçbir memura gösterilemez",
   "İbraz ödevi yalnızca elektronik defter tutan mükellefler için geçerlidir"],
  "VUK m.256: saklanması zorunlu her türlü defter, belge ve karneleri, muhafaza süresi içinde yetkili makam ve memurların talebi üzerine ibraz ve inceleme için arz etmek zorunludur.",
  "VUK m.256 - ibraz ödevi"),

# ── H. Belgeler (5) ──────────────────────────────────────────────────────────
q("Fatura bakımından aşağıdakilerden hangisi doğrudur?",
  "Fatura, satılan mal veya yapılan iş karşılığında müşterinin borçlandığı tutarı gösteren ticari belgedir",
  ["Fatura, işletmenin dönem sonunda düzenlediği mali durum tablosudur",
   "Fatura, yalnızca malın taşınması sırasında araçta bulundurulan sevk belgesidir",
   "Fatura, serbest meslek erbabının tahsilatı için düzenlediği makbuzdur",
   "Fatura, çiftçiden alınan ürün karşılığı düzenlenen müstahsil belgesidir"],
  "VUK m.229: fatura, satılan emtia veya yapılan iş karşılığında müşterinin borçlandığı meblağı göstermek üzere emtiayı satan veya işi yapan tarafından düzenlenen ticari vesikadır.",
  "VUK m.229 - fatura"),

q("Fatura düzenleme süresi bakımından aşağıdakilerden hangisi doğrudur?",
  "Fatura, malın teslimi veya hizmetin yapıldığı tarihten itibaren yedi gün içinde düzenlenir",
  ["Fatura, malın tesliminden itibaren en geç bir yıl içinde düzenlenebilir",
   "Fatura yalnızca müşteri talep ettiğinde ve istediği tarihte düzenlenir",
   "Fatura, bedelin tamamen tahsil edildiği ay sonunda topluca düzenlenir",
   "Fatura için kanunda herhangi bir düzenleme süresi öngörülmemiştir"],
  "VUK m.231: fatura, malın teslimi veya hizmetin yapıldığı tarihten itibaren azami yedi gün içinde düzenlenir; bu süre içinde düzenlenmeyen fatura hiç düzenlenmemiş sayılır.",
  "VUK m.231 - fatura düzenleme süresi"),

q("Sevk irsaliyesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Sevk irsaliyesi, taşınan malın kim tarafından kime gönderildiğini gösteren ve taşıma sırasında bulundurulan belgedir",
  ["Sevk irsaliyesi, satış bedelinin tahsil edildiğini gösteren ödeme makbuzudur",
   "Sevk irsaliyesi, işletmenin dönem sonu stok sayım listesidir",
   "Sevk irsaliyesi, serbest meslek kazancı için düzenlenen tahsilat belgesidir",
   "Sevk irsaliyesi, çiftçiden yapılan alımlarda düzenlenen müstahsil makbuzudur"],
  "VUK m.230: malın bir yerden başka yere taşınmasında sevk irsaliyesi düzenlenir ve taşıma sırasında araçta bulundurulur.",
  "VUK m.230 - sevk irsaliyesi"),

q("Müstahsil makbuzu bakımından aşağıdakilerden hangisi doğrudur?",
  "Defter tutan çiftçi olmayanlardan alınan ürün karşılığında düzenlenen ve fatura yerine geçen belgedir",
  ["Serbest meslek erbabının müşterisinden tahsilat için düzenlediği makbuzdur",
   "Malın taşınması sırasında araçta bulundurulan sevk belgesidir",
   "Tacirler arasındaki mal satışında düzenlenen olağan ticari faturadır",
   "İşletmenin çalışanına ödediği ücreti gösteren bordro belgesidir"],
  "VUK m.235: defter tutan çiftçi sıfatı taşımayanlardan satın alınan ürünler için müstahsil makbuzu düzenlenir; bu makbuz fatura yerine geçer.",
  "VUK m.235 - müstahsil makbuzu"),

q("Serbest meslek makbuzu bakımından aşağıdakilerden hangisi doğrudur?",
  "Serbest meslek erbabının, mesleki faaliyetine ilişkin tahsilatları için düzenlediği belgedir",
  ["Serbest meslek makbuzu, satılan ticari mal için düzenlenen faturadır",
   "Serbest meslek makbuzu, malın sevkinde araçta bulundurulan irsaliyedir",
   "Serbest meslek makbuzu, çiftçiden alınan ürün için düzenlenen belgedir",
   "Serbest meslek makbuzu, işletmenin dönem sonu bilançosudur"],
  "VUK m.236: serbest meslek erbabı, mesleki faaliyetlerine ilişkin her türlü tahsilatı için serbest meslek makbuzu düzenlemek ve müşteriye vermek zorundadır.",
  "VUK m.236 - serbest meslek makbuzu"),

# ── I. Yoklama, inceleme, arama, bilgi toplama (4) ───────────────────────────
q("Yoklama bakımından aşağıdakilerden hangisi doğrudur?",
  "Yoklama, mükellefiyete ilişkin maddi olayları ve kayıtları araştırıp mevcut durumu saptamayı amaçlar",
  ["Yoklama, mükellefin defterlerinin ayrıntılı olarak hesaplanıp incelenmesidir",
   "Yoklama, yalnızca mahkeme kararıyla mükellefin iş yerinde arama yapılmasıdır",
   "Yoklama, kesinleşen vergi borcunun cebren tahsil edilmesi işlemidir",
   "Yoklama, mükellefin beyannamesinin vergi dairesine kabul edilmesidir"],
  "VUK m.127: yoklamadan maksat, mükellefleri ve mükellefiyetle ilgili maddi olayları, kayıtları ve mevzuları araştırmak ve tespit etmektir.",
  "VUK m.127 - yoklama"),

q("Vergi incelemesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İncelemeden maksat, ödenmesi gereken vergilerin doğruluğunu araştırıp saptamak ve sağlamaktır",
  ["İnceleme, yalnızca mükellefin iş yerinin dışarıdan gözlemlenmesidir",
   "İnceleme, vergi dairesinin mükellefe beyanname formu göndermesidir",
   "İnceleme, yalnızca kesinleşmiş cezanın mükelleften tahsil edilmesidir",
   "İnceleme, mükellefin kendi beyanını sonradan değiştirmesi işlemidir"],
  "VUK m.134: vergi incelemesinden maksat, ödenmesi gereken vergilerin doğruluğunu araştırmak, tespit etmek ve sağlamaktır.",
  "VUK m.134 - vergi incelemesi"),

q("Vergi incelemesine yetkili olanlar bakımından aşağıdakilerden hangisi doğrudur?",
  "İnceleme; vergi müfettişleri, yardımcıları ile vergi dairesi müdürü gibi yetkililerce yapılır",
  ["Vergi incelemesi yalnızca mükellefin kendi mali müşaviri tarafından yapılır",
   "Vergi incelemesini yalnızca vergi mahkemesi hâkimleri yürütebilir",
   "İncelemeyi yapmaya yalnızca Cumhurbaşkanlığınca atanan bir kurul yetkilidir",
   "Vergi incelemesi herhangi bir memur ayrımı olmaksızın tüm kamu görevlilerince yapılır"],
  "VUK m.135: vergi incelemesi; vergi müfettişleri, vergi müfettiş yardımcıları, ilin en büyük mal memuru, vergi dairesi müdürleri ile yetkili olanlar tarafından yapılır.",
  "VUK m.135 - incelemeye yetkililer"),

q("Bilgi verme ödevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kamu idareleri ile gerçek ve tüzel kişiler, istenen bilgileri vermek zorundadır",
  ["Bilgi verme ödevi yalnızca mükellefin kendisiyle sınırlı olup üçüncü kişileri bağlamaz",
   "İstenen bilgileri vermek her hâlde tümüyle ilgilinin isteğine bırakılmıştır",
   "Bilgi verme ödevi yalnızca bankalar için geçerli olup diğerlerini kapsamaz",
   "Bilgi ancak mahkeme kararı bulunması hâlinde ve yalnızca yazılı istenebilir"],
  "VUK m.148: kamu idare ve müesseseleri ile gerçek ve tüzel kişiler, vergi incelemesi yapmaya yetkili olanların isteyeceği bilgileri vermek zorundadır.",
  "VUK m.148 - bilgi verme"),

# ── J. Vergi suç ve cezaları (6) ─────────────────────────────────────────────
q("Vergi ziyaı bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi ziyaı, verginin zamanında tahakkuk ettirilmemesi veya eksik tahakkuku nedeniyle ziyaa uğratılmasıdır",
  ["Vergi ziyaı, mükellefin vergisini süresinden önce fazladan ödemesidir",
   "Vergi ziyaı, yalnızca defterlerin geç tasdik ettirilmesi durumudur",
   "Vergi ziyaı, vergi dairesinin mükellefe fazla iade yapmasıdır",
   "Vergi ziyaı, beyannamenin hiç verilmemiş ama verginin ödenmiş olmasıdır"],
  "VUK m.341: vergi ziyaı, mükellefin veya sorumlunun ödevlerini zamanında yerine getirmemesi yüzünden verginin zamanında tahakkuk ettirilmemesi veya eksik tahakkuk ettirilmesidir.",
  "VUK m.341 - vergi ziyaı"),

q("Vergi ziyaı cezası bakımından aşağıdakilerden hangisi doğrudur?",
  "Vergi ziyaına sebebiyet verilmesi hâlinde ziyaa uğratılan vergi üzerinden ziyaı cezası kesilir",
  ["Vergi ziyaı cezası, verginin aslından bağımsız maktu ve sabit bir tutardır",
   "Vergi ziyaı cezası yalnızca usulsüzlük fiilleri için kesilen bir cezadır",
   "Vergi ziyaı cezası, yalnızca hapis cezasından ibaret olan bir yaptırımdır",
   "Vergi ziyaı cezası, verginin ödenmesiyle kendiliğinden ikiye katlanır"],
  "VUK m.344: vergi ziyaına sebebiyet verildiğinde, ziyaa uğratılan verginin bir katı tutarında vergi ziyaı cezası kesilir (kaçakçılık fiilleriyle olursa üç kat).",
  "VUK m.344 - vergi ziyaı cezası"),

q("Usulsüzlük cezası bakımından aşağıdakilerden hangisi doğrudur?",
  "Usulsüzlük, vergi kanunlarının şekle ve usule ilişkin hükümlerine uyulmamasıdır",
  ["Usulsüzlük, yalnızca verginin hiç ödenmemesi durumunu ifade eder",
   "Usulsüzlük, mükellefin fazladan vergi ödemesi hâlinde kesilen cezadır",
   "Usulsüzlük, yalnızca sahte belge düzenleme fiilinden ibarettir",
   "Usulsüzlük, verginin zamanında ve doğru tahakkukunu ifade eden olumlu durumdur"],
  "VUK m.351: usulsüzlük, vergi kanunlarının şekle ve usule ilişkin hükümlerine riayet edilmemesidir; birinci ve ikinci derece usulsüzlük olarak ayrılır.",
  "VUK m.351 - usulsüzlük"),

q("Özel usulsüzlük cezası bakımından aşağıdakilerden hangisi doğrudur?",
  "Fatura, fiş gibi belgelerin verilmemesi veya alınmaması hâllerinde özel usulsüzlük cezası kesilir",
  ["Özel usulsüzlük cezası yalnızca verginin geç ödenmesi hâlinde kesilir",
   "Özel usulsüzlük cezası, mükellefin fazla beyanı hâlinde uygulanır",
   "Özel usulsüzlük cezası, yalnızca ilk derece usulsüzlükle aynı fiili cezalandırır",
   "Özel usulsüzlük cezası yalnızca kamu kurumlarına uygulanabilen bir yaptırımdır"],
  "VUK m.353: fatura, gider pusulası, müstahsil makbuzu gibi belgelerin verilmemesi, alınmaması veya gerçeğe aykırı düzenlenmesi hâllerinde özel usulsüzlük cezası kesilir.",
  "VUK m.353 - özel usulsüzlük"),

q("Kaçakçılık suçu (VUK 359) bakımından aşağıdakilerden hangisi doğrudur?",
  "Defterleri gizleme, sahte belge düzenleme veya kullanma gibi fiiller kaçakçılık suçunu oluşturur ve hapis cezası gerektirir",
  ["Kaçakçılık suçu yalnızca para cezasıyla karşılanan basit bir usulsüzlüktür",
   "Kaçakçılık, mükellefin vergisini süresinde ödememesi hâlinden ibarettir",
   "Kaçakçılık suçu yalnızca defterin geç tasdik ettirilmesiyle oluşur",
   "Kaçakçılık, yalnızca vergi ziyaı doğduğunda kesilen idari bir cezadır"],
  "VUK m.359: defter ve belgeleri gizlemek, muhteviyatı itibariyle yanıltıcı belge düzenlemek/kullanmak, sahte belge düzenlemek/kullanmak gibi fiiller kaçakçılık suçudur ve hapis cezası öngörülür.",
  "VUK m.359 - kaçakçılık suçu"),

q("Cezalarda tekerrür bakımından aşağıdakilerden hangisi doğrudur?",
  "Cezası kesinleşen mükellefin izleyen belli süre içinde yeniden ceza kesilmesini gerektiren fiil işlemesi cezayı artırır",
  ["Tekerrür, aynı fiilin tek seferde birden çok mükellef tarafından işlenmesidir",
   "Tekerrür, kesinleşmiş cezanın mükellef lehine indirilmesini sağlayan kurumdur",
   "Tekerrür, ilk kez ceza kesilen mükellefe uygulanan bir başlangıç hükmüdür",
   "Tekerrür, verginin süresinde ödenmesi hâlinde uygulanan bir ödüldür"],
  "VUK m.339: vergi ziyaı veya usulsüzlükten ceza kesilip kesinleşenlere, kesinleşme tarihini izleyen belli süre içinde tekrar ceza kesilmesi hâlinde ceza artırımlı uygulanır.",
  "VUK m.339 - tekerrür"),


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
                       "styleRef": "SGS Vergi Hukuku / VUK (sınav stiline kalibre)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })

    # ── self-check: şık örüntüsü baştan temiz mi? ──────────────────────────
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from audit import kor_ogrenci  # tools/sgs/audit.py
    puan, strateji = kor_ogrenci(out)
    from collections import Counter
    rank = Counter()
    for q0 in out:
        lens = sorted((len(v), k) for k, v in q0["options"].items())
        rank[[k for _, k in lens].index(q0["answer"]) + 1] += 1
    print(f"kör: {puan}% ← {strateji} | boy-sırası {dict((r, rank[r]) for r in range(1,6))}")
    if puan > 30:
        print(f"  ⚠ base %{puan} — fix_vuk_boy.py ile dengelenecek (build→fix→audit)")

    for path in (OUT_APP, OUT_CONTENT):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yazıldı {len(out)} soru → iki repo | harf {''.join(x['answer'] for x in out)}")
