# -*- coding: utf-8 -*-
"""Vergi · VUK · Mükellef Ödevleri ve Değerleme — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında bu konu; iktisadi kıymetlerin değerleme ölçüleri (hisse senedi, kasa, mamul,
kıymeti düşen mal, sipariş avansı) ve emsal bedelinin belirlenme sırası üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 213 sayılı VUK md. 153-168, 177, 182, 220-221, 229-232,
242, 253-256, 258-285, 313-324, 328 ve mük. 315. Yeniden değerlenen hadler kökte verilir; hesaplar vergi_ortak.py ile.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_mukellef_odevleri_2026.json", lesson="vergi_usul_kanunu", topic="mukellef_odevleri",
          konu_adi="Mükellef Ödevleri ve Değerleme", seed=2026092908,
          surum="213 sayılı VUK güncel metni; hadler kökte; 29.09.2026 kontrolü")

V = "213 sayılı Vergi Usul Kanunu’na göre"
V26 = "213 sayılı Vergi Usul Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

a1 = 500_000 * 0.20
P.sayisal("VUK md. 313, 315",
    "(ABC) A.Ş., Ocak 2026’da 500.000 ₺’ye bir üretim makinesi satın alarak aynı ay aktifleştirmiştir. Makinenin Bakanlıkça "
    "ilan edilen faydalı ömrü 5 yıldır; şirket normal amortisman yöntemini seçmiş, gün esasını tercih etmemiştir."
    f"\n\n{V26}, (ABC) A.Ş.’nin 2026 yılı için ayırabileceği amortisman tutarı kaç ₺’dir?",
    tl(a1), secenekler(a1, 500_000 * 0.40, 500_000 * 0.10, 500_000, 500_000 * 0.25),
    "Md. 315'e göre amortisman Bakanlıkça ilan edilen oranlar üzerinden ayrılır; 5 yıllık faydalı ömür için oran %20'dir: "
    "500.000 × %20 = 100.000 ₺. Makine binek otomobil olmadığından kıst amortisman uygulanmaz.", zorluk="easy")

P.q("VUK md. 279, 284",
    "(ZAB) A.Ş.’nin mali müşaviri 31 Aralık 2025 tarihli bilançoyu vergi kanunlarına göre değerlemektedir."
    f"\n\n{V}, aşağıdaki iktisadi kıymet ve değerleme ölçüsü eşleştirmelerinden hangisi yanlıştır?",
    "Hisse senedi – borsa rayici",
    ["Kasa mevcudu (₺) – itibari değer",
     "Mamuller – maliyet bedeli",
     "Kıymeti düşen mallar – emsal bedeli",
     "Alınan sipariş avansları (₺) – mukayyet değer"],
    "Md. 279'a göre hisse senetleri alış bedeliyle değerlenir; bunlar dışındaki menkul kıymetler borsa rayici ile değerlenir. "
    "Kasa itibari değerle (md. 284), mamuller maliyet bedeliyle (md. 275), kıymeti düşen mallar emsal bedeliyle (md. 278), "
    "borçlar mukayyet değerle (md. 285) değerlenir.", zorluk="hard")

P.q("VUK md. 267",
    "(CDE) A.Ş.’nin elindeki bir malın gerçek bedeli bilinmediğinden emsal bedelinin tespiti gerekmektedir."
    f"\n\n{V}, emsal bedelin belirlenmesinde aşağıdakilerden hangisi kullanılmaz?",
    "Karşılaştırılabilir fiyat yöntemi",
    ["Ortalama fiyat esası", "Maliyet bedeli esası", "Takdir esası",
     "Kaza mercilerinin resen biçtikleri değerler"],
    "Md. 267'ye göre emsal bedel sırasıyla ortalama fiyat esası, maliyet bedeli esası ve takdir esasına göre belirlenir; kaza "
    "mercilerinin resen biçtikleri değerler de emsal bedeli sayılır. Karşılaştırılabilir fiyat yöntemi KVK md. 13'teki "
    "transfer fiyatlandırması yöntemidir.")

a2 = (500_000 - 500_000 * 0.40) * 0.40
P.sayisal("VUK mük. 315",
    "Bilanço esasına göre defter tutan (DEF) A.Ş., 2025 yılında 500.000 ₺’ye aldığı ve faydalı ömrü 5 yıl olan makineyi "
    "azalan bakiyeler usulüyle amortismana tabi tutmaktadır. Enflasyon düzeltmesi yapılmayacaktır."
    f"\n\n{V26}, (DEF) A.Ş.’nin bu makine için 2026 yılında ayıracağı amortisman kaç ₺’dir?",
    tl(a2), secenekler(a2, 500_000 * 0.40, 500_000 * 0.20, (500_000 - 100_000) * 0.20, (500_000 - 200_000) * 0.20),
    "Mük. 315'e göre azalan bakiyeler usulünde oran, %50'yi geçmemek üzere normal oranın iki katıdır (%20 × 2 = %40) ve "
    "her yıl önceki amortismanlar düşülmüş değer üzerinden hesaplanır: 2025'te 200.000 ₺; 2026'da (500.000 − 200.000) × "
    "%40 = 120.000 ₺.", zorluk="hard")

P.q("VUK md. 275",
    f"{V}, imal edilen emtianın maliyet bedeline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Genel idare giderleri payının maliyete katılması zorunludur.",
    ["İlk madde ve malzeme bedeli maliyet unsurudur.",
     "Mamule isabet eden işçilik maliyet unsurudur.",
     "Genel imal giderlerinden mamule düşen pay maliyet unsurudur.",
     "Ambalajlı satılması zaruri mamullerde ambalaj bedeli maliyet unsurudur."],
    "Md. 275'e göre genel idare giderlerinden mamule düşen hissenin maliyete katılması ihtiyaridir; ilk madde, işçilik, "
    "genel imal giderleri payı ve zaruri ambalaj bedeli maliyetin unsurudur.", zorluk="hard")

P.q("VUK md. 278",
    "(DEF) A.Ş.’nin deposunda su basması sonucu önemli ölçüde değer kaybına uğrayan kumaşlar ile üretimden kalan ve maliyeti "
    f"hesaplanması mutat olmayan kırpıntılar bulunmaktadır.\n\n{V}, bu kıymetler hangi ölçüyle değerlenir?",
    "Emsal bedeli",
    ["Maliyet bedeli", "Mukayyet değer", "Borsa rayici", "İtibari değer"],
    "Md. 278'e göre yangın, deprem ve su basması gibi afetler yüzünden veya bozulma, çürüme gibi nedenlerle değeri önemli "
    "ölçüde azalan emtia ile maliyeti hesaplanması mutat olmayan hurda ve döküntüler emsal bedeliyle değerlenir.")

a3 = 900_000 * 0.50
P.sayisal("VUK mük. 315",
    "Bilanço esasına göre defter tutan (GHI) Ltd. Şti., Ocak 2026’da faydalı ömrü 3 yıl olan bir cihazı 900.000 ₺’ye satın "
    f"almış ve azalan bakiyeler usulünü seçmiştir.\n\n{V26}, şirketin 2026 yılında ayırabileceği amortisman kaç ₺’dir?",
    tl(a3), secenekler(a3, 900_000 * 2 / 3, 900_000 / 3, 900_000 * 0.40, 900_000),
    "Normal oran 1/3 ≈ %33,33; iki katı %66,67 olsa da mük. 315'e göre azalan bakiyeler oranı %50'yi geçemez: 900.000 × %50 "
    "= 450.000 ₺.", zorluk="hard")

P.q("VUK md. 281, 285",
    f"{V}, alacak ve borçların değerlemesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Alacak senetlerini reeskonta tabi tutan, borç senetlerini tabi tutmayabilir.",
    ["Alacaklar mukayyet değerleriyle değerlenir.",
     "Borçlar mukayyet değerleriyle değerlenir.",
     "Vadesi gelmemiş senede bağlı alacaklar değerleme günü kıymetine irca olunabilir.",
     "Mevduat sözleşmesine dayanan alacaklar değerleme gününe kadar faiziyle dikkate alınır."],
    "Md. 285'e göre alacak senetlerini değerleme gününün kıymetine irca eden mükellefler borç senetlerini de aynı şekilde "
    "işleme tabi tutmak zorundadır. Alacak ve borçlar mukayyet değerle değerlenir.", zorluk="hard")

P.q("VUK md. 283",
    "(GHI) A.Ş., Aralık 2025’te 2026 yılının tamamına ait işyeri sigortası primini peşin ödemiştir."
    f"\n\n{V}, bu peşin ödenen gider 31 Aralık 2025 itibarıyla nasıl değerlenir?",
    "Mukayyet değer üzerinden aktifleştirilir.",
    ["Ödeme 2025’te yapıldığından tamamı 2025 yılı gideri yazılır.",
     "Emsal bedeliyle değerlenir.",
     "Borsa rayiciyle değerlenir.",
     "Tasarruf değeriyle pasifleştirilir."],
    "Md. 283'e göre gelecek hesap dönemine ait olarak peşin ödenen giderler ile cari döneme ait olup henüz tahsil edilmemiş "
    "hasılat, mukayyet değerleri üzerinden aktifleştirilmek suretiyle değerlenir.")

a4 = 1_200_000 / 5 * 4 / 12
P.sayisal("VUK md. 320",
    "Tekstil ticareti yapan (JKL) A.Ş., 12 Eylül 2026’da 1.200.000 ₺’ye bir binek otomobil satın alıp aktifleştirmiştir; "
    "faydalı ömrü 5 yıldır ve şirket normal amortisman usulünü uygulamaktadır. Şirketin faaliyeti araç kiralama değildir."
    f"\n\n{V26}, bu otomobil için 2026 yılında ayrılabilecek amortisman kaç ₺’dir?",
    tl(a4), secenekler(a4, 240_000, 1_200_000 / 5 * 3 / 12, 1_200_000 / 5 * 9 / 12, 0),
    "Md. 320'ye göre binek otomobillerin aktife girdiği dönemde ay kesri tam ay sayılarak kalan ay süresi kadar amortisman "
    "ayrılır: Eylül-Aralık 4 ay; 240.000 × 4/12 = 80.000 ₺. Ayrılmayan kısım itfa süresinin son yılında yok edilir.",
    zorluk="hard")

P.q("VUK md. 322",
    f"{V}, değersiz alacaklara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kazai hükme veya kanaat verici vesikaya göre tahsil imkânı kalmayan alacaklardır.",
    ["Dava veya icra safhasındaki tüm alacaklar değersiz alacaktır.",
     "Değersiz alacaklar sadece bilanço esasında zarar yazılabilir.",
     "Değersiz alacaklar emsal bedeliyle değerlenir.",
     "Değersiz alacaklar için zarar yazılmadan önce şüpheli alacak karşılığı ayrılması şarttır."],
    "Md. 322'ye göre kazai bir hükme veya kanaat verici bir vesikaya göre tahsiline imkân kalmayan alacaklar değersiz "
    "alacaktır; bu mahiyete girdikleri tarihte mukayyet değerleriyle zarara geçirilir, işletme hesabında gider yazılır.")

P.q("VUK md. 323",
    f"{V}, şüpheli alacak karşılığına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Karşılık ayrılabilmesi için alacağın ticari faaliyetle ilgili olması gerekmez.",
    ["Dava veya icra safhasındaki alacaklar şüpheli alacak sayılır.",
     "Karşılığın hangi alacaklara ait olduğu karşılık hesabında gösterilir.",
     "Teminatlı alacaklarda karşılık teminattan geri kalan miktara inhisar eder.",
     "Şüpheli alacakların sonradan tahsil edilen kısmı tahsil dönemi kâr-zarar hesabına alınır."],
    "Md. 323'e göre şüpheli alacak karşılığı, ticari ve zirai kazancın elde edilmesi ve idamesiyle ilgili alacaklar için "
    "ayrılabilir. Diğer ifadeler maddeye uygundur.")

dg = 10_000 + 8_000
P.sayisal("VUK md. 313",
    "(MNO) A.Ş. 2026 yılında şu demirbaşları almıştır: tek başına kullanılan bir yazıcı 10.000 ₺; bir dosya dolabı "
    "8.000 ₺; bir fotokopi makinesi 15.000 ₺; bir toplantı odası için birbirinin tamamlayıcısı olan 4 adet sandalye ve "
    "masadan oluşan, bütünlük arz eden takım toplam 20.000 ₺ (her parça 5.000 ₺). (Kanunda belirtilen had 12.000 ₺ olarak "
    f"alınacaktır.)\n\n{V26}, bu alımlardan amortismana tabi tutulmaksızın doğrudan gider yazılabilecek toplam tutar kaç "
    "₺’dir?",
    tl(dg), secenekler(dg, 10_000 + 8_000 + 20_000, 53_000, 10_000, 8_000 + 20_000),
    "Md. 313'e göre değeri Kanundaki haddi aşmayan alet, edevat, mefruşat ve demirbaşlar doğrudan gider yazılabilir; iktisadi "
    "ve teknik bakımdan bütünlük arz edenlerde had topluca dikkate alınır. Takım 20.000 ₺ ile haddi aştığından, fotokopi "
    "makinesi de 15.000 ₺ olduğundan amortismana tabidir: 10.000 + 8.000 = 18.000 ₺.", zorluk="hard")

P.q("VUK mük. 315",
    f"{V26}, azalan bakiyeler usulüyle amortismana ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşletme hesabına göre defter tutan mükellefler de bu usulü seçebilir.",
    ["Bu usul bilanço esasına göre defter tutanlar tarafından seçilebilir.",
     "Amortisman oranı normal oranın iki katıdır.",
     "Uygulanacak oran %50’yi geçemez.",
     "Amortisman, önceki amortismanlar düşülerek kalan değer üzerinden hesaplanır."],
    "Mük. 315'e göre azalan bakiyeler usulünü bilanço esasına göre defter tutan mükellefler seçebilir; oran %50'yi geçmemek "
    "üzere normal oranın iki katıdır ve her yıl kalan değer üzerinden hesaplanır.")

P.q("VUK md. 313",
    f"{V}, aşağıdakilerden hangisi amortisman konusu değildir?",
    "Stokta bekletilen satılık bilgisayarlar",
    ["İşletmede bir yıldan fazla kullanılan makineler",
     "İşletmede kullanılan binalar",
     "İşletmede kullanılan demirbaşlar",
     "İşletmede kullanılan sinema filmleri"],
    "Md. 313'e göre işletmede bir yıldan fazla kullanılan ve yıpranmaya maruz gayrimenkuller, alet, edevat, mefruşat, "
    "demirbaş ve sinema filmleri amortisman konusudur. Satılmak üzere elde tutulan emtia amortismana tabi değildir.",
    zorluk="easy")

sk = 250_000 - (400_000 - 240_000)
P.sayisal("VUK md. 328",
    "(PRS) Ltd. Şti., 400.000 ₺ maliyetli ve 240.000 ₺ birikmiş amortismanı bulunan bir makineyi 2026 yılında 250.000 ₺’ye "
    f"satmıştır. Şirket yenileme fonu ayırmamaktadır.\n\n{V}, bu satıştan doğan ve kâr-zarar hesabına geçirilecek kâr "
    "kaç ₺’dir?",
    tl(sk), secenekler(sk, 250_000, 150_000, 10_000, 250_000 - 240_000 + 40_000),
    "Md. 328'e göre amortismana tabi kıymetlerin satışında alınan bedel ile kayıtlı değeri (maliyet − ayrılmış amortisman) "
    "arasındaki fark kâr-zarar hesabına geçirilir: 250.000 − (400.000 − 240.000) = 90.000 ₺.")

P.q("VUK md. 328",
    "(JKL) A.Ş., yangın sonucu kullanılamaz hâle gelen bir makinesi için sigorta tazminatı almış ve aynı niteliğe sahip yeni "
    f"bir makine almaya karar vermiştir.\n\n{V}, bu durumda oluşan kâra ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kâr yenileme fonuna alınabilir.",
    ["Kâr aynı yıl vergilendirilir.",
     "Kâr iştirak kazancı sayılarak istisna edilir.",
     "Kâr yeni makinenin maliyet bedeline eklenir.",
     "Kâr sermayeye eklenmedikçe hesaplanmaz."],
    "Md. 328'e göre bilanço esasına göre defter tutan mükellefler, satılan veya zayi olan kıymetin yenilenmesi zorunlu ya da "
    "kararlaştırılmışsa oluşan kârı pasifte özel fon hesabına alabilir ve yeni kıymetin amortismanlarına mahsup edebilir.",
    zorluk="hard")

P.q("VUK md. 153",
    f"{V}, aşağıdakilerden hangisi işe başlamayı vergi dairesine bildirmekle yükümlü değildir?",
    "Sadece mevduat faizi elde eden kişi",
    ["Vergiye tabi ticaret ve sanat erbabı",
     "Serbest meslek erbabı",
     "Kurumlar vergisi mükellefleri",
     "Kollektif şirket ortakları"],
    "Md. 153'e göre vergiye tabi ticaret ve sanat erbabı, serbest meslek erbabı, kurumlar vergisi mükellefleri ile kollektif ve "
    "adi şirket ortakları ve komandite ortaklar işe başlamayı bildirmeye mecburdur.", zorluk="easy")

mb = 1_000_000 + 20_000 + 30_000 + 10_000
P.sayisal("VUK md. 262",
    "(TUV) A.Ş., 2026 yılında bir makineyi 1.000.000 ₺’ye kredi kullanarak satın almıştır. Makinenin fabrikaya nakli için "
    "20.000 ₺ nakliye gideri ödenmiştir. Makine aktife girinceye kadar krediye 30.000 ₺ faiz tahakkuk etmiş, aktife girdikten "
    f"sonra aynı hesap dönemi sonuna kadar 10.000 ₺ daha faiz oluşmuştur.\n\n{V}, makinenin maliyet bedeli kaç ₺’dir?",
    tl(mb), secenekler(mb, 1_000_000, 1_020_000, 1_050_000, 1_030_000),
    "Md. 262'ye göre maliyet bedeli; iktisap bedeli ile nakliye gibi doğrudan giderleri ve emtia dışındaki kıymetlerde "
    "finansman kredisine ait faizlerin kıymetin envantere alındığı hesap döneminin sonuna kadar olan kısmını içerir: "
    "1.000.000 + 20.000 + 30.000 + 10.000 = 1.060.000 ₺. Sonraki dönem faizlerini maliyete katmak ihtiyaridir.",
    zorluk="hard")

P.q("VUK md. 153, 168",
    "(MNO) A.Ş. kuruluş için ticaret siciline başvurmuş ve tescil edilmiştir. Şirket ortakları, ayrıca vergi dairesine işe "
    f"başlama bildirimi vermeleri gerekip gerekmediğini sormaktadır.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "İşe başlama bildirimi yapılmış sayılır.",
    ["Şirket ayrıca vergi dairesine bildirimde bulunmakle yükümlüdür.",
     "Bildirim şirket müdürünce otuz gün içinde yapılmalıdır.",
     "Kurumlar vergisi mükellefleri işe başlamayı bildirmez.",
     "Bildirim sadece ilk kâr elde edildiğinde yapılır."],
    "Md. 153 ve 168'e göre ticaret sicili memurlukları, tescil için başvuran kurumlar vergisi mükelleflerinin evraklarının "
    "suretini vergi dairesine iletir ve bu mükelleflerin işe başlamayı bildirme yükümlülüğü yerine getirilmiş sayılır.",
    zorluk="hard")

P.q("VUK md. 177",
    f"{V}, aşağıdakilerden hangisi alım-satım hacmine bakılmaksızın birinci sınıf tüccar sayılır?",
    "Her türlü ticaret şirketi",
    ["Yıllık satışı Kanundaki haddin altında kalan ferdi tüccar",
     "Kazancı basit usulde tespit edilen esnaf",
     "Serbest meslek erbabı",
     "Gerçek usulde vergilendirilmeyen çiftçi"],
    "Md. 177/4'e göre her türlü ticaret şirketleri, hasılat hadlerine bakılmaksızın birinci sınıf tüccardır; adi şirketler "
    "iştigal konusuna göre hadlere tabidir.", zorluk="easy")

yp = 10_000 * 35
P.sayisal("VUK md. 280",
    "(VYZ) A.Ş.’nin kasasında 31 Aralık 2025 tarihinde 10.000 ABD doları bulunmaktadır. Bu dövizler 30 ₺’lik kurdan alınmış "
    f"olup değerleme günündeki borsa rayici 35 ₺’dir.\n\n{V}, bu dövizlerin değerleme günündeki değeri kaç ₺’dir?",
    tl(yp), secenekler(yp, 300_000, 50_000, 325_000, 650_000),
    "Md. 280 ve 284'e göre yabancı paralar borsa rayici ile değerlenir: 10.000 × 35 = 350.000 ₺. Aradaki 50.000 ₺ kur "
    "farkı gelir olarak dikkate alınır.")

P.q("VUK md. 182",
    f"{V}, aşağıdakilerden hangisi bilanço esasına göre tutulan defterlerden biridir?",
    "Envanter defteri",
    ["İşletme defteri", "Serbest meslek kazanç defteri", "Çiftçi işletme defteri", "Hasılat defteri"],
    "Md. 182'ye göre bilanço esasında yevmiye defteri, defterikebir ve envanter defteri tutulur. İşletme defteri ikinci sınıf "
    "tüccarların, serbest meslek kazanç defteri serbest meslek erbabının, çiftçi işletme defteri çiftçilerin defteridir.", zorluk="easy")

P.q("VUK md. 220-221",
    "Öteden beri faaliyetini sürdüren (OPR) A.Ş., 2027 yılında kullanacağı yevmiye ve envanter defterlerini tasdik "
    f"ettirecektir. Şirket kâğıt defter kullanmaktadır.\n\n{V}, bu defterler en geç ne zaman tasdik ettirilmelidir?",
    "2026 yılının Aralık ayında",
    ["2027 yılının Ocak ayında", "2027 yılının Mart ayında", "2026 yılının Ekim ayında",
     "Defterler kullanılmaya başlandıktan sonra"],
    "Md. 221/1'e göre öteden beri işe devam edenler defterlerini, defterin kullanılacağı yıldan önce gelen son ayda tasdik "
    "ettirmeye mecburdur: 2027 defterleri için Aralık 2026.")

sa = 200_000 - 50_000
P.sayisal("VUK md. 323",
    "(ZAB) Ltd. Şti.’nin ticari faaliyetiyle ilgili 200.000 ₺ tutarındaki alacağı için borçlu aleyhine dava açılmıştır. "
    f"Alacak için borçludan 50.000 ₺ teminat alınmıştır.\n\n{V}, şirketin bu alacak için ayırabileceği şüpheli alacak "
    "karşılığı en fazla kaç ₺’dir?",
    tl(sa), secenekler(sa, 200_000, 50_000, 100_000, 0),
    "Md. 323'e göre dava veya icra safhasındaki alacaklar şüpheli alacaktır ve tasarruf değerine göre karşılık ayrılabilir; "
    "teminatlı alacaklarda karşılık teminattan geri kalan miktara inhisar eder: 200.000 − 50.000 = 150.000 ₺.")

P.q("VUK md. 221",
    f"{V}, defterlerin tasdik zamanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yeniden işe başlayanlar defterlerini işe başladıktan sonraki ilk ay içinde tasdik ettirir.",
    ["Öteden beri işe devam edenler, defterin kullanılacağı yıldan önceki son ayda tasdik ettirir.",
     "Sınıf değiştirenler, sınıf değiştirme tarihinden önce tasdik ettirir.",
     "Vergi muafiyeti kalkanlar, muaflıktan çıkma tarihinden itibaren on gün içinde tasdik ettirir.",
     "Yıl içinde defteri dolanlar, yeni defteri kullanmaya başlamadan önce tasdik ettirir."],
    "Md. 221/3'e göre yeniden işe başlayanlar, sınıf değiştirenler ve yeni bir mükellefiyete girenler defterlerini işe "
    "başlama, sınıf değiştirme veya yeni mükellefiyete girme tarihinden önce tasdik ettirmelidir.", zorluk="hard")

P.q("VUK md. 229, 232",
    f"{V}, fatura verme ve alma mecburiyetine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Birinci ve ikinci sınıf tüccarlar birbirine fatura vermekle yükümlüdür.",
    ["Serbest meslek erbabı tüccardan fatura istemekle yükümlü değildir.",
     "Vergiden muaf esnafa satış yapan tüccar fatura vermez.",
     "Nihai tüketiciye yapılan satışlarda tutara bakılmaksızın fatura verilmez.",
     "Fatura sadece bedelin tahsil edildiği tarihte düzenlenir."],
    "Md. 232'ye göre birinci ve ikinci sınıf tüccarlar; tüccarlara, serbest meslek erbabına, basit usul mükelleflerine, "
    "defter tutan çiftçilere ve muaf esnafa sattıkları mal ve yaptıkları işler için fatura vermek ve bunlardan fatura "
    "istemek ve almakla yükümlüdür; diğer alıcılara haddi aşan satışlarda veya istek hâlinde fatura verilir.")

sa2 = 20_000
P.sayisal("VUK md. 323",
    "(CDE) A.Ş.’nin ticari faaliyetle ilgili iki alacağı vardır: protesto edilmesine rağmen ödenmeyen 20.000 ₺ ile yazıyla "
    "defalarca istenmesine rağmen ödenmeyen, dava veya icra takibine konu edilmemiş 40.000 ₺. (Kanunda belirtilen had "
    f"25.000 ₺ olarak alınacaktır.)\n\n{V26}, şirketin bu alacaklar için ayırabileceği şüpheli alacak karşılığı toplamı kaç "
    "₺’dir?",
    tl(sa2), secenekler(sa2, 60_000, 40_000, 25_000, 45_000),
    "Md. 323'e göre protestoya veya yazıyla birden fazla istenmesine rağmen ödenmeyen alacaklar, Kanundaki haddi aşmıyorsa "
    "dava ve icra aranmaksızın şüpheli alacak sayılır. 20.000 ₺ haddin altındadır; 40.000 ₺ haddi aştığından ancak dava veya "
    "icra safhasına geçerse karşılık ayrılabilir.", zorluk="hard")

P.q("VUK md. 232",
    "Nihai tüketici Bayan (N), bir mağazadan 9.000 ₺’lik ürün satın almış ve fatura istemiştir. (Kanunda belirtilen had "
    f"12.000 ₺ olarak alınacaktır.)\n\n{V26}, mağazanın fatura verme yükümlülüğüne ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "İstendiği için fatura verilmelidir.",
    ["Tutar haddin altında kaldığından fatura verilmez.",
     "Fatura yerine sadece sevk irsaliyesi düzenlenir.",
     "Nihai tüketiciye tutarına bakılmaksızın fatura düzenlenmez.",
     "Fatura ancak bedel havale ile ödenmişse verilir."],
    "Md. 232/2'ye göre tüccardan mal alanların satın aldıkları malın bedelinin Kanundaki haddi geçmesi veya haddin altında "
    "olsa dahi istemeleri hâlinde satıcının fatura vermesi mecburidir.")

P.q("VUK md. 253-256",
    f"{V}, defter ve belgelerin muhafaza ve ibrazına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Defter tutma mecburiyeti olmayanların aldıkları faturaları saklama zorunluluğu yoktur.",
    ["Defter tutanlar defter ve belgeleri ilgili yılı takip eden yıldan başlayarak beş yıl saklar.",
     "Muhafaza süresi içinde defter ve belgeler yetkililerin talebinde ibraz edilmelidir.",
     "Elektronik ortamdaki kayıtlara erişim için gerekli şifreler de ibraz edilmelidir.",
     "Defter tutma mecburiyeti olmayanlar almaya mecbur oldukları faturaları beş yıl saklar."],
    "Md. 254'e göre defter tutma mecburiyeti olmayanlar da md. 232, 234 ve 235 gereğince almaya mecbur oldukları fatura, "
    "gider pusulası ve müstahsil makbuzlarını tanzim tarihlerini takip eden yıldan başlayarak beş yıl saklamak zorundadır.")

P.sayisal("VUK md. 324",
    "(FGH) A.Ş., 2025 yılında konkordato yoluyla alacaklılarının vazgeçtiği 300.000 ₺ tutarındaki borcunu özel bir karşılık "
    f"hesabına almıştır.\n\n{V}, bu tutar en geç hangi yılın sonuna kadar zararla itfa edilmezse kâr hesabına nakledilir?",
    "2028", ["2026", "2027", "2030", "2035"],
    "Md. 324'e göre konkordato veya sulh yoluyla alınmasından vazgeçilen alacaklar borçlunun defterlerinde özel karşılık "
    "hesabına alınır; alacaktan vazgeçildiği yılın sonundan başlayarak üç yıl içinde zararla itfa edilmezse kâr hesabına "
    "nakledilir: 2025 sonundan itibaren üç yıl, 2028 sonu.", zorluk="hard")

P.q("VUK md. 242",
    f"{V}, tüccarların dosyada muhafaza etmesi gereken vesikalar arasında aşağıdakilerden hangisi yer almaz?",
    "Özel mektuplar",
    ["Mukavelename ve taahhütnameler", "Kefaletnameler", "Mahkeme ilamları", "Vergi makbuzları ve ihbarnameler"],
    "Md. 242'ye göre tüccarlar, bir hüküm ifade eden veya bir hakkın ispatına delil olarak kullanılabilen mukavelename, "
    "taahhütname, kefaletname, mahkeme ilamları gibi hukuki vesikalar ile ihbarname, karar örnekleri ve vergi makbuzlarını "
    "dosyada muhafaza etmeye mecburdur.", zorluk="easy")

P.q("VUK md. 258-259",
    f"{V}, değerlemeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "İktisadi kıymetlerin vergi matrahı için takdir ve tespitidir.",
    ["Değerleme sadece yıl sonu stoklarına uygulanır.",
     "Değerlemede mükellefin seçtiği herhangi bir gün esas alınır.",
     "Değerleme sadece ticari kazançta yapılır.",
     "Değerlemede Türkiye Finansal Raporlama Standartları esas alınır."],
    "Md. 258'e göre değerleme, vergi matrahlarının hesaplanmasıyla ilgili iktisadi kıymetlerin takdir ve tespitidir; md. "
    "259'a göre kıymetlerin vergi kanunlarında gösterilen gün ve zamanlarda haiz oldukları değer esas tutulur.")

kt = 1_000_000 * 0.05 + 1_000_000
P.sayisal("VUK md. 267",
    "(IJK) A.Ş.’nin elindeki bir malın gerçek bedeli bilinmemektedir. Aynı cins maldan son üç ayda satış yapılmamıştır. "
    f"Malın maliyet bedeli 1.000.000 ₺ olup mal toptan satılacaktır.\n\n{V}, maliyet bedeli esasına göre bu malın emsal "
    "bedeli kaç ₺’dir?",
    tl(kt), secenekler(kt, 1_000_000, 1_100_000, 1_150_000, 1_025_000),
    "Md. 267'ye göre ortalama fiyat esası uygulanamadığında ikinci sırada maliyet bedeli esası uygulanır; maliyet bedeline "
    "toptan satışlar için %5, perakende satışlar için %10 eklenir: 1.000.000 × 1,05 = 1.050.000 ₺.")

P.q("VUK md. 263",
    f"{V}, borsa rayicine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Son muamele günündeki ortalama borsa değeridir.",
    ["Değerleme günündeki en yüksek borsa fiyatıdır.",
     "Yıl içindeki tüm işlemlerin ağırlıklı ortalamasıdır.",
     "Mükellefin kendi alış fiyatlarının ortalamasıdır.",
     "Merkez Bankasınca ilan edilen alış kurudur."],
    "Md. 263'e göre borsa rayici, borsalara kayıtlı iktisadi kıymetlerin değerlemeden önceki son muamele gününde borsadaki "
    "muamelelerinin ortalama değeridir; bariz kararsızlıklarda Bakanlık 30 günlük ortalamayı esas aldırabilir.")

P.oncul("VUK md. 279-285",
    f"{V} aşağıdaki iktisadi kıymet ve değerleme ölçüsü eşleştirmeleri değerlendirilmektedir:",
    ["Tahvil – borsa rayici", "Hisse senedi – alış bedeli", "Yabancı para – mukayyet değer",
     "Peşin ödenmiş gider – maliyet bedeli"],
    "Yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I ve II",
    ["I ve II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"],
    "Md. 279'a göre hisse senetleri dışındaki menkul kıymetler (tahvil) borsa rayici ile (I), hisse senetleri alış bedeliyle "
    "(II) değerlenir. Yabancı paralar borsa rayiciyle (md. 280), peşin ödenmiş giderler mukayyet değerle (md. 283) "
    "değerlenir.", zorluk="hard")

bk = 300_000 * 5 + 1_200_000
P.sayisal("VUK md. 177",
    "Bay (K), hem mal alım satımı yapmakta hem de onarım hizmeti vermektedir. 2025 yılında yıllık satış tutarı 1.200.000 ₺, "
    "onarım hizmetinden elde ettiği gayrisafi iş hasılatı 300.000 ₺’dir. (Karma faaliyetlerde uygulanacak had 2.500.000 ₺ "
    f"olarak alınacaktır.)\n\n{V26}, Bay (K)’nın sınıfının belirlenmesinde dikkate alınacak karma hesap tutarı kaç ₺’dir?",
    tl(bk), secenekler(bk, 1_500_000, 1_200_000 + 300_000 * 2, 1_200_000 * 5 + 300_000, 2_500_000),
    "Md. 177/3'e göre işlerin birlikte yapılması hâlinde iş hasılatının beş katı ile yıllık satış tutarının toplamı dikkate "
    "alınır: 300.000 × 5 + 1.200.000 = 2.700.000 ₺. Tutar haddi aştığından Bay (K) birinci sınıf tüccardır.", zorluk="hard")

P.q("VUK md. 320",
    f"{V26}, amortisman süresine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Amortisman süresi, kıymetin satın alındığı sözleşme tarihinden başlar.",
    ["Amortisman süresi kıymetlerin aktife girdiği yıldan başlar.",
     "Dileyen mükellefler kullanıma hazır olma tarihinden itibaren gün esasına göre amortisman ayırabilir.",
     "Binek otomobillerde aktife girilen dönemde kalan ay süresi kadar amortisman ayrılır.",
     "Mükellef belirleyeceği süre ilan edilen faydalı ömürden kısa olamaz."],
    "Md. 320'ye göre amortisman süresi kıymetlerin aktife girdiği yıldan başlar; gün esası ve binek otomobillerde kıst "
    "amortisman hükümleri ile faydalı ömürden kısa olmamak kaydıyla süre belirleme serbestisi vardır.")

P.q("VUK md. 262",
    f"{V26}, aşağıdakilerden hangisi bir iktisadi kıymetin maliyet bedeline dahil edilmez?",
    "Kıymetin kullanımı sırasında yapılan olağan bakım gideri",
    ["İktisapla doğrudan ilgili gümrük vergisi",
     "İktisapla doğrudan ilgili nakliye ve montaj gideri",
     "İktisapla doğrudan ilgili tapu harcı ve noter gideri",
     "İktisapla doğrudan ilgili değer tespiti ve danışmanlık gideri"],
    "Md. 262'ye 7338 sayılı Kanunla eklenen fıkraya göre gümrük vergisi, nakliye, montaj, resim, harç, noter, tapu, değer "
    "tespiti ve danışmanlık giderleri maliyete dahildir. Değeri artırmayan olağan bakım giderleri maliyet unsuru değil, "
    "dönem gideridir.", zorluk="hard")

P.sayisal("VUK md. 253",
    "(LMN) A.Ş.’nin 2025 hesap dönemine ait yevmiye defteri ve faturalarını ne zamana kadar saklaması gerektiği "
    f"sorulmaktadır.\n\n{V}, bu defter ve belgeler en az hangi yılın sonuna kadar muhafaza edilmelidir?",
    "2030", ["2026", "2028", "2031", "2035"],
    "Md. 253'e göre defter tutmak mecburiyetinde olanlar defter ve belgeleri, ilgili bulundukları yılı takip eden takvim "
    "yılından başlayarak beş yıl süreyle muhafaza etmeye mecburdur: 2026-2030.")

P.q("VUK md. 274",
    f"{V}, emtianın değerlemesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Emtia maliyet bedeliyle değerlenir.",
    ["Emtia kural olarak borsa rayiciyle değerlenir.",
     "Emtia mukayyet değerle değerlenir.",
     "Emtia sadece emsal bedeliyle değerlenir.",
     "Emtia itibari değerle değerlenir."],
    "Md. 274'e göre emtia maliyet bedeliyle değerlenir; satış bedelleri maliyete göre %10 veya daha fazla düşükse emsal "
    "bedeli ölçüsü uygulanabilir.", zorluk="easy")

P.q("VUK md. 177",
    f"{V}, birinci sınıf tüccarlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Adi şirketler iştigal konusuna bakılmaksızın birinci sınıf tüccar sayılır.",
    ["Her türlü ticaret şirketi birinci sınıf tüccardır.",
     "Kurumlar vergisine tabi diğer tüzel kişiler kural olarak birinci sınıftır.",
     "Alım-satım işlerinde alım veya satım tutarı haddi aşanlar birinci sınıftır.",
     "Karma faaliyetlerde iş hasılatının beş katı ile satış tutarı toplamı dikkate alınır."],
    "Md. 177/4'e göre her türlü ticaret şirketleri birinci sınıftır; ancak adi şirketler iştigal konularının hangi bende "
    "girdiğine göre o bent hükmüne (hadlere) tabidir.", zorluk="hard")

P.sayisal("VUK md. 168",
    "Serbest muhasebeci mali müşavir Bayan (L), 3 Mart 2026’da kendi bürosunu açarak serbest meslek faaliyetine başlamıştır."
    f"\n\n{V}, Bayan (L) işe başlamayı işe başlama tarihinden itibaren en geç kaç gün içinde vergi dairesine bildirmelidir?",
    "10", ["7", "15", "20", "30"],
    "Md. 168'e göre gerçek kişilerde işe başlama bildirimleri, işe başlama tarihinden itibaren on gün içinde yapılır.",
    zorluk="easy")

P.q("VUK md. 219",
    "(MNO) A.Ş., muhasebe fişlerine dayanarak kayıt yapan ve işlemleri önce fişlere işleyen bir kuruluştur. Bir alış "
    f"faturası 2 Mart 2026’da fişe işlenmiştir.\n\n{V}, bu işlemin yevmiye defterine intikaline ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "İşlem esas deftere en geç 45 gün içinde intikal ettirilmelidir.",
    ["İşlem aynı gün yevmiye defterine kaydedilmelidir.",
     "İşlem yıl sonuna kadar deftere kaydedilebilir.",
     "Fişe işleme deftere kayıt hükmünde değildir.",
     "İşlem en geç 90 gün içinde kaydedilmelidir."],
    "Md. 219/b'ye göre kayıtları mazbut vesikalara dayanan müesseselerde muamelelerin bunlara işlenmesi deftere işlenmesi "
    "hükmündedir; ancak kayıtların esas defterlere 45 günden geç intikal ettirilmesi caiz değildir. Genel kuralda gecikme "
    "on günü geçemez.", zorluk="hard")

P.q("VUK md. 219",
    f"{V}, muamelelerin defterlere kaydına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Serbest meslek kazanç defterine kayıtlar ay sonunda toplu olarak yapılabilir.",
    ["Kayıtların on günden fazla geciktirilmesi caiz değildir.",
     "Muhasebe fişine işlenen kayıtlar deftere işlenmiş sayılır.",
     "Fişlerdeki kayıtlar esas defterlere 45 günden geç intikal ettirilemez.",
     "Günlük kasa ve perakende satış defterlerine kayıtlar günü gününe yapılır."],
    "Md. 219/c'ye göre günlük kasa, perakende satış ve hasılat defterleri ile serbest meslek kazanç defterine muameleler günü "
    "gününe kaydedilir.")

P.sayisal("VUK md. 168",
    "(OPR) A.Ş. 2026 yılında işyeri adresini değiştirmiştir.\n\n"
    f"{V}, bu değişiklik, olayın vukuu tarihinden itibaren en geç kaç ay içinde vergi dairesine bildirilmelidir?",
    "1", ["2", "3", "6", "12"],
    "Md. 168'e göre şirketlerin işe başlama bildirimleri dışındaki bildirimler ile işi bırakma ve değişiklik bildirimleri, "
    "olayın vukuu tarihinden itibaren bir ay içinde mükellef tarafından yapılır.")

P.q("VUK md. 234",
    "İkinci sınıf tüccar Bay (N), vergiden muaf esnaf olan gezici bir ayakkabı tamircisine işyerindeki ayakkabıları "
    f"tamir ettirmiştir.\n\n{V}, Bay (N)’nin bu işlem için düzenlemesi gereken belge aşağıdakilerden hangisidir?",
    "Gider pusulası",
    ["Müstahsil makbuzu", "Serbest meslek makbuzu", "Perakende satış fişi", "Sevk irsaliyesi"],
    "Md. 234'e göre tüccarlar, belge düzenleme zorunluluğu bulunmayanlara yaptırdıkları işler için işi yapana imza ettirecekleri "
    "gider pusulası düzenler; vergiden muaf esnaf için düzenlenen gider pusulası fatura hükmündedir.", zorluk="easy")

P.sayisal("VUK md. 231",
    "(PRS) Ltd. Şti. 2 Mart 2026’da müşterisine mal teslim etmiştir; müşteri e-fatura kullanıcısı değildir ve özel süre "
    f"belirlenmemiştir.\n\n{V}, fatura malın teslim tarihinden itibaren en geç kaç gün içinde düzenlenmelidir?",
    "7", ["3", "5", "10", "15"],
    "Md. 231/5'e göre fatura, malın teslimi veya hizmetin yapıldığı tarihten itibaren azami yedi gün içinde düzenlenir; "
    "Bakanlık bu süreyi kısaltmaya yetkilidir.", zorluk="easy")

P.q("VUK md. 235",
    "Birinci sınıf tüccar (OPR) A.Ş., gerçek usulde vergiye tabi olmayan bir çiftçiden buğday satın almıştır."
    f"\n\n{V}, bu alışa ilişkin aşağıdakilerden hangisi doğrudur?",
    "İki nüsha müstahsil makbuzu düzenlenir.",
    ["Çiftçi alıcıya fatura düzenlemekle yükümlüdür.",
     "Alış için gider pusulası düzenlenir.",
     "Alış için herhangi bir belge düzenlenmesi gerekmez.",
     "Müstahsil makbuzu çiftçi tarafından düzenlenir."],
    "Md. 235'e göre tüccarlar, gerçek usulde vergiye tabi olmayan çiftçilerden satın aldıkları malların bedelini ödedikleri "
    "sırada iki nüsha müstahsil makbuzu düzenler, birini satıcı çiftçiye verir; alıcıda kalan nüsha fatura yerine geçer.")

P.sayisal("VUK md. 320",
    "(TUV) A.Ş., Bakanlıkça faydalı ömrü 30 yıl olarak ilan edilen bir bina için amortisman süresini kendisi belirlemek "
    f"istemektedir.\n\n{V26}, şirketin belirleyebileceği amortisman süresi en fazla kaç yıl olabilir?",
    "50", ["30", "45", "60", "75"],
    "Md. 320'ye göre mükellefler amortisman süresini ilan edilen faydalı ömürden kısa olmamak üzere belirleyebilir; ancak "
    "süre ilan edilen sürenin iki katını ve elli yılı aşamaz: iki katı 60 yıl olsa da üst sınır 50 yıldır.", zorluk="hard")

P.q("VUK md. 230",
    f"{V}, aşağıdakilerden hangisi faturada bulunması gereken asgari bilgiler arasında yer almaz?",
    "Satıcının yıllık satış hasılatı",
    ["Faturanın düzenlenme tarihi, seri ve sıra numarası",
     "Faturayı düzenleyenin adı, adresi, vergi dairesi ve hesap numarası",
     "Malın veya işin nev’i, miktarı, fiyatı ve tutarı",
     "Satılan malların teslim tarihi ve irsaliye numarası"],
    "Md. 230'a göre faturada düzenlenme tarihi, seri ve sıra numarası; düzenleyenin ve müşterinin kimlik ve vergi bilgileri; "
    "malın veya işin nev'i, miktarı, fiyatı ve tutarı ile teslim tarihi ve irsaliye numarası bulunur.", zorluk="easy")

P.sayisal("VUK md. 274",
    "(VYZ) A.Ş.’nin stoklarındaki bir emtianın maliyet bedeli 100.000 ₺’dir. Değerleme günündeki satış bedelleri maliyete "
    f"göre düşüktür.\n\n{V}, emsal bedeli ölçüsünün uygulanabilmesi için satış bedelinin maliyet bedeline göre en az yüzde "
    "kaç düşük olması gerekir?",
    "10", ["5", "15", "20", "25"],
    "Md. 274'e göre emtianın değerleme günündeki satış bedelleri maliyet bedeline göre %10 ve daha fazla düşüklük gösterirse "
    "mükellef, md. 267'nin ikinci sırasındaki usul hariç emsal bedeli ölçüsünü uygulayabilir.")

P.q("VUK md. 160",
    "Bir vergi müfettişi, (PRS) Ltd. Şti.’nin başkaca bir faaliyeti olmadığı hâlde münhasıran sahte belge düzenlemek "
    f"amacıyla mükellefiyet tesis ettirdiğini raporla tespit etmiştir.\n\n{V}, bu durumda aşağıdakilerden hangisi doğrudur?",
    "Mükellef işi bırakmış sayılır ve mükellefiyet kaydı terkin edilir.",
    ["Mükellefiyet kaydı ancak mükellefin talebiyle silinebilir.",
     "Mükellef işi bırakmış sayılmaz; sadece ceza kesilir.",
     "Mükellefiyet kaydı beş yıl süreyle askıya alınır.",
     "Mükellefin beyanname verdiği dönemlerde kayıt terkin edilemez."],
    "Md. 160'a göre münhasıran sahte belge düzenlemek amacıyla mükellefiyet tesis ettirildiğinin inceleme raporuyla tespiti ve "
    "kaydın devamına gerek görülmediğinin belirtilmesi hâlinde mükellef, beyanname verse dahi işi bırakmış addolunur ve "
    "kaydı terkin edilir.", zorluk="hard")

ge = 730_000 * 61 / (5 * 365)
P.sayisal("VUK md. 320",
    "(ABC) A.Ş., 730.000 ₺’ye aldığı ve faydalı ömrü 5 yıl olan bir makineyi 1 Kasım 2026’da kullanıma hazır hâle getirmiş ve "
    "gün esasına göre amortisman ayırmayı tercih etmiştir. Makine yıl sonuna kadar aktifte kalmıştır."
    f"\n\n{V26}, (ABC) A.Ş.’nin 2026 yılında bu makine için ayıracağı amortisman kaç ₺’dir?",
    tl(ge), secenekler(ge, 730_000 / 5, 730_000 / 5 * 2 / 12, 730_000 / 5 * 60 / 365, 730_000 * 61 / 365),
    "Md. 320'ye göre gün esasında süre, faydalı ömür × 365 gün olarak hesaplanır (1.825 gün) ve kıymetin aktifte kaldığı gün "
    "kadar amortisman ayrılır: 1 Kasım-31 Aralık 61 gün; 730.000 × 61 / 1.825 = 24.400 ₺.", zorluk="hard")

P.q("VUK md. 176",
    f"{V}, tüccarların defter tutma bakımından sınıflandırılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Birinci sınıf bilanço, ikinci sınıf işletme hesabı esasına göre defter tutar.",
    ["Birinci sınıf işletme hesabı, ikinci sınıf bilanço esasına göre defter tutar.",
     "Tüm tüccarlar bilanço esasına göre defter tutar.",
     "Tüccarlar üç sınıfa ayrılır.",
     "İkinci sınıf tüccarlar defter tutmaz."],
    "Md. 176'ya göre tüccarlar defter tutma bakımından iki sınıfa ayrılır: birinci sınıf tüccarlar bilanço esasına, ikinci "
    "sınıf tüccarlar işletme hesabı esasına göre defter tutar.", zorluk="easy")

st = 60_000
P.sayisal("VUK md. 323",
    "(DEF) Ltd. Şti., 2025 yılında dava safhasındaki bir alacağı için 150.000 ₺ şüpheli alacak karşılığı ayırmıştır. 2026 "
    f"yılında bu alacağın 60.000 ₺’si tahsil edilmiştir.\n\n{V}, 2026 yılında kâr-zarar hesabına intikal ettirilecek tutar "
    "kaç ₺’dir?",
    tl(st), secenekler(st, 150_000, 90_000, 0, 210_000),
    "Md. 323'e göre şüpheli alacakların sonradan tahsil edilen miktarları tahsil edildikleri dönemde kâr-zarar hesabına "
    "intikal ettirilir: 60.000 ₺.", zorluk="easy")

P.q("VUK md. 234",
    f"{V}, gider pusulasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Vergi dışı çiftçiden alımda da gider pusulası düzenlenir.",
    ["Belge düzenleme zorunluluğu olmayanlara yaptırılan işler için düzenlenir.",
     "Vergiden muaf esnaf için düzenlenen gider pusulası fatura hükmündedir.",
     "İki nüsha düzenlenir ve biri işi yapana verilir.",
     "Seri ve sıra numarası dahilinde teselsül ettirilir."],
    "Md. 234'e göre gider pusulası belge düzenleme zorunluluğu bulunmayanlardan yapılan alış ve yaptırılan işler için "
    "düzenlenir; gerçek usulde vergilendirilmeyen çiftçilerden alınan mallar hariçtir, bunlar için md. 235'e göre müstahsil "
    "makbuzu düzenlenir.", zorluk="hard")

kf = 20_000 * (36 - 32)
P.sayisal("VUK md. 280, 285",
    "(GHI) A.Ş., yurt dışındaki tedarikçisine 20.000 avro borçludur. Borç, avro kuru 32 ₺ iken kayda alınmıştır. Değerleme "
    f"gününde avronun borsa rayici 36 ₺’dir.\n\n{V}, değerleme sonucunda dikkate alınacak kur farkı gideri kaç ₺’dir?",
    tl(kf), secenekler(kf, 20_000 * 36, 20_000 * 32, 20_000 * 2, 20_000 * 68),
    "Md. 280'e göre yabancı paralarla olan borçlar da borsa rayici ile değerlenir: 20.000 × 36 = 720.000 ₺; kayıtlı değer "
    "640.000 ₺ olduğundan 80.000 ₺ kur farkı gideri doğar.")

P.q("VUK md. 230",
    "(TUV) A.Ş., sattığı malları kendi aracıyla alıcının deposuna taşımaktadır. Malların bir kısmını da satılmak üzere "
    f"komisyoncusuna göndermektedir.\n\n{V}, sevk irsaliyesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her iki durumda da irsaliyeyi satıcı düzenler.",
    ["Alıcıya taşımada sevk irsaliyesini alıcı düzenler.",
     "Komisyoncuya gönderimde sevk irsaliyesi gerekmez.",
     "Sevk irsaliyesi sadece ihracatta düzenlenir.",
     "Fatura düzenlendiğinde sevk irsaliyesi ayrıca aranmaz."],
    "Md. 230/5'e göre malın alıcıya teslim edilmek üzere satıcı tarafından taşındığı hâllerde satıcının sevk irsaliyesi "
    "düzenlemesi ve taşıtta bulundurması şarttır; malın komisyoncu veya aracıya gönderilmesinde de gönderen sevk irsaliyesi "
    "düzenler.")

of = 50_000 / 100 * 20
P.sayisal("VUK md. 267",
    "(JKL) A.Ş., gerçek bedeli bilinmeyen 20 adet ürünün emsal bedelini belirleyecektir. Değerlemenin yapıldığı ayda aynı "
    "cins üründen 100 adet toplam 50.000 ₺’ye satılmıştır. Bu satış miktarı emsal bedeli belirlenecek miktara göre "
    f"yeterlidir.\n\n{V}, 20 adet ürünün ortalama fiyat esasına göre emsal bedeli kaç ₺’dir?",
    tl(of), secenekler(of, 50_000, 10_500, 12_500, 2_500),
    "Md. 267'ye göre birinci sırada ortalama fiyat esası uygulanır; aylık satış miktarının emsal bedeli belirlenecek miktara "
    "göre %25'ten az olmaması gerekir. Ortalama satış fiyatı 50.000 / 100 = 500 ₺; 20 × 500 = 10.000 ₺.")

if __name__ == "__main__":
    sys.exit(P.yaz())
