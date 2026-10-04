#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkçe — Paragraf (yeni konu) — gerçek sınav profiline göre yazıldı.

YENİ KONU. 2021-2026'nın 16 kitapçığında Türkçe sorularının %38'i paragraf sorusu, havuzda karşılığı yoktu. 60 özgün paragraf: düşüncenin akışını bozan cümle, paragraf sıralama (ilk/üçüncü/dördüncü cümle), yer değiştirme, düşünceyi geliştirme yolları (tek ve ikili), anlatım biçimi, ana düşünce/vurgulanan düşünce, çıkarılabilir/söylenemez, paragraf tamamlama (baş, orta, son), nesnel/öznel yargı, paragraf içi noktalama ve kalın sözcüğün anlamı/türü. Numaralı şıklar (I-V, 'I ve II') gerçek sınavdaki gibi sıralı; harf doğru şıkkın sırasından gelir, kalan 45 soruda harf dengelenir. Serbest şıklarda doğru şık en uzun 6/45, en kısa 7/45.

2026-10-05: paket 100 soruya çıkarıldı (0061-0100; Türkçe içindeki paragraf payı %25 → %36, gerçek sınav %38). Yeni 40 soru aynı tip dağılımıyla yazıldı; serbest şıklı 28 soruda doğru şık en uzun 3, en kısa 3; gerçek kitapçıklarla ortak 6'lı sözcük dizisi yalnız standart soru kalıbında.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/turkce/paragraf.json"
STYLE_REF = 'SGS Türkçe paragraf (gerçek sınav 1-7 profili)'
ONEK = "turkce-paragraf-gen-"


def patch(stem, options, answer, solution, ref='Türkçe - paragraf'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        '(I) Kütüphaneler uzun süre, kitapların korunduğu sessiz mekânlar olarak görüldü. (II) Oysa bugün pek çok kütüphane; atölyeler, söyleşiler ve dijital hizmetlerle bir buluşma yerine dönüşmüş durumda. (III) Çocuklar için düzenlenen okuma saatleri, aileleri de bu mekânlara çekiyor. (IV) Matbaanın icadından önce kitaplar elle çoğaltıldığı için oldukça pahalıydı. (V) Böylece kütüphane, okuru beklemek yerine okura giden canlı bir kurum kimliği kazanıyor.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'D',
        'Parça, kütüphanelerin sessiz mekânlardan canlı buluşma yerlerine dönüşmesini anlatıyor. IV. cümle ise matbaa öncesinde kitapların pahalılığından söz ederek bu konunun dışına çıkıyor; akışı bozan cümle odur.',
    ),
    # düzey 3
    '0002': patch(
        'Muhasebe yazılımlarının yaygınlaşması, defter tutmayı eskisine göre çok daha hızlı hâle getirdi. Fişlerin elle deftere geçirildiği, toplamların defalarca kontrol edildiği günler artık geride kaldı. Ancak bu hız, meslek mensubunun sorumluluğunu azaltmadı; tersine, yanlış girilen bir verinin saniyeler içinde bütün raporlara yayılması, dikkatli olmanın önemini artırdı. Bugün iyi bir muhasebeci, kayıt yapmakla yetinmeyip rakamların arkasındaki işlemleri sorgulayan kişidir.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İyi bir muhasebeci rakamların dayandığı işlemleri de sorgular.',
            'B': 'Muhasebe yazılımları kayıt işlemlerini hızlandırmıştır.',
            'C': 'Hatalı bir veri kısa sürede birçok raporu etkileyebilir.',
            'D': 'Geçmişte toplamlar elle ve tekrar tekrar denetlenirdi.',
            'E': 'Yazılımlar, muhasebecinin sorumluluğunu önemli ölçüde hafifletmiştir.',
        },
        'E',
        'Parçada hızın meslek mensubunun sorumluluğunu azaltmadığı, tersine dikkatin önemini artırdığı açıkça belirtiliyor. Sorumluluğun hafiflediği yargısı bu nedenle söylenemez; diğer yargıların hepsi parçada yer alıyor.',
    ),
    # düzey 2
    '0003': patch(
        "Bir belediyenin kütüphane kayıtlarına göre geçen yıl kütüphaneden 48 bin kitap ödünç alındı. Ödünç alınan kitapların yüzde 40'ını çocuk kitapları oluşturdu. Kütüphanenin kayıtlı üye sayısı 15 bine ulaşırken üyelerin yaklaşık 6 bini 18 yaşın altındaydı. Bu rakamlar, ilçede okuma alışkanlığının en çok çocuklar arasında yaygınlaştığını gösteriyor.\n\nBu parçada düşünceyi geliştirmek için ağırlıklı olarak aşağıdakilerden hangisine başvurulmuştur?",
        {
            'A': 'Örneklendirme',
            'B': 'Sayısal verilerden yararlanma',
            'C': 'Tanımlama',
            'D': 'Tanık gösterme',
            'E': 'Benzetme',
        },
        'B',
        'Parçadaki yargı (okuma alışkanlığının çocuklar arasında yaygınlaştığı), ödünç alınan kitap sayısı, yüzdeler ve üye sayıları gibi sayısal verilerle desteklenmiştir.',
    ),
    # düzey 3
    '0004': patch(
        'Bir şehrin kimliği yalnızca anıtlarında, saraylarında ya da meydanlarında aranmamalıdır. Sabahları açılan fırının kokusu, mahalle kahvesinde süren sohbetler, pazar yerinde yükselen sesler de o kimliğin parçasıdır. Büyük yapıları korumaya gösterilen özenin bir benzeri bu gündelik hayata da gösterilmezse şehirler, zamanla birbirinin aynı olan sıradan yerlere dönüşür.\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Şehirler büyüdükçe yeni meydanlara ve anıtlara daha çok ihtiyaç duyar.',
            'B': 'Tarihî anıtlar, bir şehrin geçmişini geleceğe taşıyan en değerli varlıklarıdır.',
            'C': 'Mahalle kültürü büyük şehirlerde hızla zayıflamakta ve unutulmaktadır.',
            'D': 'Pazar yerleri, şehirlerin ekonomik hayatında hâlâ önemli bir yer tutmaktadır.',
            'E': 'Şehrin gündelik yaşamı da büyük yapılar kadar korunmalıdır.',
        },
        'E',
        'Yazar, şehrin kimliğinin anıtların yanında gündelik hayattan da oluştuğunu ve bu hayatın da büyük yapılar kadar korunması gerektiğini vurguluyor. Diğer seçenekler ya parçada yer almıyor ya da ayrıntıya odaklanıyor.',
    ),
    # düzey 2
    '0005': patch(
        'Ah, ne çok şey biriktirmişiz ( ) Eski fotoğraflar, okul karneleri, sararmış mektuplar ( ) Saymakla bitmez. Annem hepsini tek tek katlayıp kutulara yerleştirirken bir yandan da soruyordu ( ) “Bunları gerçekten saklamak istiyor musun ( )”\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(!) (...) (:) (?)',
            'B': '(.) (:) (;) (?)',
            'C': '(!) (...) (,) (?)',
            'D': '(!) (;) (:) (.)',
            'E': '(?) (...) (:) (?)',
        },
        'A',
        "'Ah' ünlemiyle başlayan duygu cümlesinin sonuna ünlem, sayılması tamamlanmamış sıralamanın sonuna ('Saymakla bitmez.') üç nokta, doğrudan aktarılacak sözden önce iki nokta, aktarılan soru cümlesinin sonuna soru işareti konur.",
    ),
    # düzey 3
    '0006': patch(
        'Çocukluğumuzda dinlediğimiz masallar, çoğu zaman basit bir iyilik-kötülük karşıtlığına dayanır. Ama bu basitlik aldatıcıdır; çünkü masal, çocuğun henüz adını koyamadığı korkularına bir biçim verir. Devin, kurdun ya da cadının yenildiği her hikâye, çocuğa kendi korkularının da üstesinden gelinebileceğini fısıldar. ----\n\nBu parçanın sonuna düşüncenin akışına göre aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Bu yüzden masallar, çocuğun iç dünyasını güçlendiren sessiz birer rehberdir.',
            'B': 'Masal anlatıcılığı eski çağlarda saygın bir meslek sayılırdı.',
            'C': 'Bugün çocuklar masal yerine daha çok çizgi film izlemektedir.',
            'D': 'Masallar ilk kez yazıya geçirildiğinde aslında çocuklar için değil, yetişkinler için derlenmişti.',
            'E': 'Devler ve cadılar, farklı kültürlerin masallarında birbirinden farklı adlarla anılır.',
        },
        'A',
        'Parça, masalların çocuğun korkularına biçim verip onları yenebileceğini hissettirdiğini anlatıyor. Bu düşünceyi bağlayan sonuç cümlesi, masalların çocuğun iç dünyasını güçlendirdiğini söyleyen seçenektir; diğerleri konuyu başka yöne çeker.',
    ),
    # düzey 2
    '0007': patch(
        'Köyün girişindeki çınar, gövdesini yılların ağırlığıyla hafifçe yana eğmişti. Geniş dallarının altında, yazın en sıcak günlerinde bile serin bir gölge dolaşırdı. Kabuğu yer yer soyulmuş, açılan yerlerde açık yeşil lekeler belirmişti. Rüzgâr estikçe yaprakları gümüşî bir parıltıyla dalgalanır, dibindeki çeşmenin şırıltısına karışırdı.\n\nBu parçanın anlatımında aşağıdakilerden hangisi ağır basmaktadır?',
        {
            'A': 'Açıklama',
            'B': 'Karşılaştırma',
            'C': 'Betimleme',
            'D': 'Tartışma',
            'E': 'Öyküleme',
        },
        'C',
        'Parçada bir olay anlatılmıyor; çınarın görünümü, gölgesi, kabuğu ve yaprakları renk, ses ve dokunma izlenimleriyle sözle resmediliyor. Bu, betimlemedir.',
    ),
    # düzey 3
    '0008': patch(
        'Yazmaya başladığım ilk yıllarda her cümlemin kusursuz olmasını isterdim. Bir paragrafı günlerce yeniden yazar, sonunda çoğu zaman hiçbirini beğenmeyip kâğıtları buruştururdum. Zamanla anladım ki kusursuzluk beklentisi beni yazmaktan alıkoyuyordu. Şimdi önce aklımdakini olduğu gibi döküyor, düzeltmeyi sonraya bırakıyorum.\n\nBu sözleri söyleyen bir yazar için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Mükemmeliyetçiliğin üretkenliğini engellediğini fark etmiştir.',
            'B': 'Yazdıklarını hiç düzeltmeden yayımlamayı tercih etmektedir.',
            'C': 'Uzun metinler yerine kısa öyküler yazmaya yönelmiştir.',
            'D': 'Yazmayı bir süre bırakıp başka bir işe yönelmiştir.',
            'E': 'Okurlarının eleştirileri yüzünden yazma biçimini değiştirmiştir.',
        },
        'A',
        "Yazar, kusursuzluk beklentisinin kendisini yazmaktan alıkoyduğunu anladığını söylüyor; yani mükemmeliyetçiliğin üretkenliğini engellediğini fark etmiştir. Düzeltmeyi bıraktığını değil sonraya ertelediğini belirttiği için 'hiç düzeltmeden' yargısı yanlıştır.",
    ),
    # düzey 3
    '0009': patch(
        "(I) Kapadokya'daki peri bacaları, volkanik tüflerin rüzgâr ve yağmurla aşınması sonucu oluşmuştur. (II) Bölgedeki yeraltı şehirlerinin bir kısmı birkaç kat derinliğe ulaşır. (III) Gün doğumunda gökyüzünü dolduran balonlar, bölgenin en büyüleyici manzarasını oluşturur. (IV) Bölgedeki pek çok kaya oyma kilise, duvar resimleriyle süslenmiştir. (V) Kapadokya'nın bir bölümü, UNESCO Dünya Mirası Listesi'nde yer almaktadır.\n\nBu parçadaki numaralanmış cümlelerden hangisinde öznel bir yargı vardır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'C',
        "III. cümledeki 'en büyüleyici manzara' değerlendirmesi kişiden kişiye değişebilen bir beğeniyi yansıtır; öznel yargıdır. Diğer cümleler doğruluğu araştırılarak kanıtlanabilecek bilgiler içerir.",
    ),
    # düzey 3
    '0010': patch(
        'Ekonomide “sürü davranışı” denen bir eğilimden söz edilir. Yatırımcılar, kendi değerlendirmelerine dayanmak yerine çoğunluğun ne yaptığına bakarak karar verir. Bir hisse senedine talep artmaya başladığında, nedenini araştırmadan alım yapanların sayısı da hızla çoğalır. Fiyatlar gerçek değerinden uzaklaştığında ise aynı kalabalık bu kez satmak için yarışır ve düşüş beklenenden sert olur.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Fiyatlar düştüğünde yatırımcılar genellikle alım yapmayı tercih eder.',
            'B': 'Sürü davranışı en çok deneyimli yatırımcılarda görülür.',
            'C': 'Sürü davranışı fiyat hareketlerini iki yönde de büyütebilir.',
            'D': 'Sürü davranışı ilk kez hisse senedi piyasalarında gözlemlenmiştir.',
            'E': 'Yatırımcıların çoğu kararlarını ayrıntılı analizlere dayandırır.',
        },
        'C',
        'Parça, kalabalığın yükselişte alım yaparak fiyatı gerçek değerinden uzaklaştırdığını, ardından satışa geçerek düşüşü sertleştirdiğini anlatıyor; buradan sürü davranışının fiyat hareketlerini iki yönde de büyüttüğü çıkarılır.',
    ),
    # düzey 3
    '0011': patch(
        '(I) Bu yüzden ilk başta yalnızca birkaç bilim insanının ilgisini çekmişti. (II) İnternet, ilk ortaya çıktığında üniversiteler arasında bilgi paylaşmak için geliştirilmiş bir ağdı. (III) Bugün ise milyarlarca insanın her gün kullandığı bir iletişim aracına dönüştü. (IV) Ağa bağlanan bilgisayarların sayısı arttıkça kullanım alanları da genişledi. (V) Kısa sürede e-posta, haber siteleri ve alışveriş platformları ortaya çıktı.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın ilk cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'B',
        "Doğru sıra II-I-IV-V-III'tür. Konuyu tanıtan ve başka bir cümleye bağlanmayan II. cümle paragrafın girişidir; I. cümledeki 'Bu yüzden' ifadesi öncesinde bir cümle bulunmasını gerektirir.",
    ),
    # düzey 3
    '0012': patch(
        'Enflasyon, mal ve hizmet fiyatlarının genel düzeyinde sürekli bir artış olmasıdır. Örneğin geçen yıl 100 liraya alınan bir alışveriş sepeti bugün 140 liraya alınabiliyorsa bu sepetin fiyatı yüzde 40 artmış demektir. Fiyatlar arttıkça aynı parayla daha az şey satın alınabilir; yani paranın satın alma gücü düşer.\n\nBu parçada düşünceyi geliştirme yollarından hangileri kullanılmıştır?',
        {
            'A': 'Karşılaştırma - Tanık gösterme',
            'B': 'Tanımlama - Benzetme',
            'C': 'Tanık gösterme - Benzetme',
            'D': 'Tanımlama - Örneklendirme',
            'E': 'Örneklendirme - Tanık gösterme',
        },
        'D',
        "İlk cümle enflasyonun ne olduğunu açıklayan bir tanımlamadır; ikinci cümle 'Örneğin' ile başlayan alışveriş sepeti örneğidir. Parçada bir alıntı (tanık gösterme) ya da benzetme bulunmadığından bunları içeren seçenekler yanlıştır.",
    ),
    # düzey 3
    '0013': patch(
        'Arıların önemi, çoğu zaman bal üretimiyle sınırlıymış gibi düşünülür. Oysa meyve ve sebzelerin önemli bir bölümü, verim için arılar başta olmak üzere tozlaştırıcı böceklere ihtiyaç duyar. Tarım ilaçlarının bilinçsiz kullanımı ve yaşam alanlarının daralması, son yıllarda arı kolonilerini zayıflatmaktadır. Bu durum arıcılarla birlikte sofrasına meyve ve sebze gelen herkesi ilgilendirir.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yaşam alanlarının daralması arıları olumsuz etkileyen etkenlerdendir.',
            'B': 'Arı kolonilerindeki zayıflama, arıcılar dışında kimseyi doğrudan ilgilendirmez.',
            'C': 'Arıların önemi çoğu zaman bal üretimiyle sınırlı görülür.',
            'D': 'Pek çok meyve ve sebzenin verimi tozlaştırıcı böceklere bağlıdır.',
            'E': 'Tarım ilaçlarının bilinçsiz kullanımı arı kolonilerine zarar vermektedir.',
        },
        'B',
        'Parçanın son cümlesi sorunun arıcılarla birlikte meyve ve sebze tüketen herkesi ilgilendirdiğini söylüyor; bu nedenle yalnız arıcıları ilgilendirdiği yargısı söylenemez.',
    ),
    # düzey 3
    '0014': patch(
        '(I) Düzenli uyku, öğrenmenin en çok göz ardı edilen destekçisidir. (II) Kahve, dünyada en çok tüketilen içeceklerden biridir. (III) Gün içinde edinilen bilgiler, uyku sırasında beyinde yeniden düzenlenip kalıcı belleğe aktarılır. (IV) Bu nedenle sınavdan önceki geceyi uykusuz geçiren öğrenci, çalıştığının önemli bir kısmını hatırlamakta zorlanabilir. (V) Kısacası iyi bir uyku, en az çalışmanın kendisi kadar başarıya katkı sağlar.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'B',
        'Parça, uykunun öğrenmeye katkısını anlatıyor. II. cümle kahvenin ne kadar tüketildiğinden söz ederek konunun dışına çıkıyor ve I. cümle ile III. cümle arasındaki bağı koparıyor.',
    ),
    # düzey 2
    '0015': patch(
        'Yazar, romanın ilk sayfalarında okuru **ağır** bir sessizliğin içine çeker. Kahraman, bir **kapı** aralığından kardeşinin evden ayrılışını izler. O an kalbi **taş** kesilmiş gibidir. Yıllar sonra aynı eve döndüğünde anılar içinde **dalga dalga** yükselir; değişenin ev değil, kendi **bakışı** olduğunu anlar.\n\nBu parçadaki kalın yazılmış sözcüklerden hangisi gerçek anlamıyla kullanılmıştır?',
        {
            'A': 'kapı',
            'B': 'ağır',
            'C': 'bakışı',
            'D': 'dalga dalga',
            'E': 'taş',
        },
        'A',
        "'Kapı aralığı' sözcüğün somut, ilk anlamıdır. 'Ağır sessizlik', 'taş kesilmek', anıların 'dalga dalga' yükselmesi ve 'bakış' (dünyaya bakış açısı) mecaz anlamlıdır.",
    ),
    # düzey 3
    '0016': patch(
        '(I) Sabah erkenden yola çıktık. (II) Molanın ardından yokuşu tırmanmaya başladık. (III) Öğle saatlerinde dağın eteğindeki bir çeşmede mola verdik. (IV) Tırmanış iki saat sürdü ve zirveye vardığımızda bütün vadi ayaklarımızın altındaydı. (V) Akşam olduğunda yorgun ama mutlu bir şekilde köye ulaştık.\n\nBu parçadaki numaralanmış cümlelerden hangi ikisinin yeri değiştirilirse düşüncenin akışı düzelir?',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'II ve IV',
            'D': 'III ve V',
            'E': 'IV ve V',
        },
        'B',
        "Molanın ardından tırmanıldığını söyleyen II. cümle, molanın verildiğini anlatan III. cümleden önce gelmiş. İkisinin yeri değişince sıra 'yola çıkış - mola - tırmanış - zirve - köye varış' biçiminde düzelir.",
    ),
    # düzey 3
    '0017': patch(
        'Bir dili gerçekten öğrenmek, sözcükleri ve dil bilgisi kurallarını ezberlemekle tamamlanmaz. O dili konuşan insanların nasıl şaka yaptığını, neye üzüldüğünü, hangi sözü ayıp saydığını da bilmek gerekir. Sözlükte karşılığı bulunan pek çok ifade, gündelik konuşmada bambaşka bir anlam kazanır. Bu yüzden dil, kendisini besleyen kültürden ayrı düşünülemez.\n\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
        {
            'A': 'Bir dili öğrenmek, o dilin kültürünü de tanımayı gerektirir.',
            'B': 'Sözlükler gündelik konuşmayı öğrenmek için yeterli kaynaklardır.',
            'C': 'Şakalar ve deyimler her dilde aynı biçimde anlaşılır.',
            'D': 'Yabancı dil öğrenmeye küçük yaşta başlamak gerekir.',
            'E': 'Dil bilgisi kuralları bir dili öğrenmenin en zor bölümüdür.',
        },
        'A',
        "Parça, sözcük ve kural bilgisinin yetmediğini, insanların gündelik yaşamını ve değerlerini bilmenin de gerektiğini anlatıp 'dil kültürden ayrı düşünülemez' yargısıyla bağlanıyor.",
    ),
    # düzey 3
    '0018': patch(
        'Çevrim içi alışveriş, tüketicilere zaman ve fiyat karşılaştırma kolaylığı sağlıyor. ---- Bu yüzden uzmanlar, alışveriş yapılan sitenin güvenilirliğini kontrol etmeyi ve kart bilgilerini güvenli ödeme sayfaları dışında hiçbir yere girmemeyi öneriyor.\n\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Mağazada alışverişi sevenlerin sayısı hâlâ azımsanmayacak kadar fazla.',
            'B': 'Çevrim içi alışverişte en çok giyim ürünleri tercih ediliyor.',
            'C': 'Kargo şirketlerinin sayısı da son yıllarda belirgin biçimde arttı ve teslim süreleri kısaldı.',
            'D': 'Pek çok kişi ürünleri mağazada görüp internetten satın alıyor.',
            'E': 'Ne var ki bu kolaylık, dolandırıcılık riskini de beraberinde getiriyor.',
        },
        'E',
        "Boşluktan sonraki 'Bu yüzden' ile başlayan cümle güvenlik önlemleri öneriyor; öncesinde bu önlemleri gerektiren bir tehlikeden söz edilmelidir. Bu bağı kuran, dolandırıcılık riskini anlatan cümledir.",
    ),
    # düzey 2
    '0019': patch(
        'Kırk yıllık ustaydı. Tezgâhının başına geçmeden önce aletlerini tek tek siler, sonra sırayla dizerdi. Çırakları bu işi gereksiz bir tören sanır, gülüşürlerdi. Bir gün içlerinden biri nedenini sorunca usta, “Aleti temiz olmayanın işi de temiz olmaz.” dedi. O günden sonra kimse gülmedi.\n\nBu parçada asıl vurgulanan düşünce aşağıdakilerden hangisidir?',
        {
            'A': 'Kırk yıllık deneyim her sorunu çözmeye yeter.',
            'B': 'Meslek sırları çıraklardan saklanmalıdır.',
            'C': 'Ustalar çıraklarına karşı sert davranmalıdır.',
            'D': 'İyi bir iş, hazırlığa ve özene verilen önemle başlar.',
            'E': 'Eski çalışma yöntemleri bugün geçerliliğini yitirmiştir.',
        },
        'D',
        'Ustanın sözü ve davranışı, işin niteliğinin aletlere ve hazırlığa gösterilen özenle başladığını anlatıyor; parçanın vurguladığı düşünce budur.',
    ),
    # düzey 2
    '0020': patch(
        'Kentte yaşayan bir çocuk, oyun alanını çoğunlukla apartmanın önündeki dar bir bahçeyle sınırlı bulur; oyuncakları satın alınmış, oyun saatleri bellidir. Köyde büyüyen bir çocuk ise derenin kıyısını, ağaçların arasını, tarlanın kenarını oyun alanı bilir; oyuncaklarını çoğu zaman kendisi yapar, akşam olunca eve döner.\n\nBu parçada düşünceyi geliştirmek için ağırlıklı olarak aşağıdakilerden hangisine başvurulmuştur?',
        {
            'A': 'Benzetme',
            'B': 'Karşılaştırma',
            'C': 'Tanık gösterme',
            'D': 'Sayısal verilerden yararlanma',
            'E': 'Tanımlama',
        },
        'B',
        'Parça, kentte ve köyde büyüyen çocukların oyun alanlarını, oyuncaklarını ve oyun saatlerini yan yana koyarak aralarındaki farkları gösteriyor; bu karşılaştırmadır.',
    ),
    # düzey 3
    '0021': patch(
        "(I) Şirketler artık finansal sonuçlarının yanında çevreye ve topluma etkileriyle de değerlendiriliyor. (II) Yatırımcılar, karbon salımını azaltmayan işletmeleri uzun vadede riskli görmeye başladı. (III) Muhasebenin kökleri, Mezopotamya'daki kil tabletlere kadar uzanır. (IV) Bu nedenle birçok şirket, sürdürülebilirlik raporlarını finansal tablolarıyla birlikte yayımlıyor. (V) Böylece paydaşlar, işletmenin geleceğe ne kadar hazırlıklı olduğunu daha iyi görebiliyor.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'C',
        "Parça, şirketlerin çevresel ve toplumsal etkileriyle değerlendirilmesini ve sürdürülebilirlik raporlamasını anlatıyor. III. cümle muhasebenin tarihine geçerek konunun dışına çıkıyor; IV. cümledeki 'Bu nedenle' de II. cümleye bağlanıyor.",
    ),
    # düzey 3
    '0022': patch(
        'Halk ozanları, şiirlerini çoğunlukla yazıya geçirmeden, saz eşliğinde söyleyerek yaşatmıştır. Bu şiirler kulaktan kulağa aktarıldıkça bazı sözcükleri değişmiş, bazen yeni dizeler eklenmiştir. Bu yüzden aynı türkünün farklı yörelerde birbirinden ayrı biçimleri bulunabilir. Derlemeciler bu farklılıkları birer kusur olarak değil, yaşayan bir geleneğin izleri olarak görür.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Derlemeciler, türküler arasındaki farklılıkları aktarım hatası sayar.',
            'B': 'Aynı türkü farklı yörelerde farklı biçimlerde söylenebilir.',
            'C': 'Halk şiirinin yaşamasında sözlü aktarım belirleyici olmuştur.',
            'D': 'Halk ozanları şiirlerini çoğu zaman saz eşliğinde söylemiştir.',
            'E': 'Aktarım sürecinde bazı türkülerin sözcükleri değişmiş, bazılarına yeni dizeler eklenmiştir.',
        },
        'A',
        'Son cümle derlemecilerin farklılıkları kusur değil, yaşayan geleneğin izi olarak gördüğünü söylüyor; bunları aktarım hatası saydıkları yargısı parçayla çelişir.',
    ),
    # düzey 2
    '0023': patch(
        'İyi bir çevirmen, metni bir dilden ötekine sözcük sözcük aktaran kişi değildir. Uzun yıllar çeviri yapmış bir dostumun deyişiyle “Çevirmen, yazarın o dilde doğsaydı nasıl yazacağını tahmin etmeye çalışan kişidir.” Bu tahmin, iki dili bilmenin ötesinde iki kültürü de derinden tanımayı gerektirir.\n\nBu parçada düşünceyi geliştirme yollarından hangisine başvurulmuştur?',
        {
            'A': 'Örneklendirme',
            'B': 'Sayısal verilerden yararlanma',
            'C': 'Benzetme',
            'D': 'Tanık gösterme',
            'E': 'Karşılaştırma',
        },
        'D',
        'Yazar, düşüncesini desteklemek için deneyimli bir çevirmenin sözünü tırnak içinde aktarıyor; bu, tanık göstermedir.',
    ),
    # düzey 3
    '0024': patch(
        'Tasarruf çoğu zaman harcamaları kısmak olarak anlaşılır. Oysa gelir düzeyi ne olursa olsun, bütçesini planlamayan biri ay sonunu getirmekte zorlanabilir. Küçük ama düzenli birikimler, beklenmedik bir masraf karşısında büyük bir borca girmeyi önler. Bu nedenle tasarrufu bir yoksunluk değil, geleceğe dönük bir güvence olarak görmek gerekir.\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Yüksek gelirli kişilerin tasarruf yapmasına gerek yoktur.',
            'B': 'Tasarruf, geleceğe dönük bir güvencedir.',
            'C': 'Bütçe planlaması karmaşık bir uzmanlık gerektirir.',
            'D': 'Harcamaları kısmak, birikim yapmanın en kısa yoludur.',
            'E': 'Beklenmedik masraflar ancak borçlanarak karşılanabilir.',
        },
        'B',
        'Yazar, tasarrufun yoksunluk olarak değil, beklenmedik durumlara karşı bir güvence olarak görülmesi gerektiğini vurguluyor. Diğer seçenekler ya parçayla çelişiyor ya da parçada yer almıyor.',
    ),
    # düzey 3
    '0025': patch(
        'Kurulun gündemindeki maddeler şunlardı ( ) bütçe, personel ve yeni şube ( ) Toplantıyı Dr ( ) Selim Kaya yönetti ( ) Toplantının sonunda bir üye, kararların ne zaman uygulanacağını sordu ( )\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(;) (.) (,) (.) (?)',
            'B': '(:) (.) (.) (.) (?)',
            'C': '(:) (...) (.) (.) (.)',
            'D': '(:) (.) (.) (.) (.)',
            'E': '(,) (.) (.) (,) (?)',
        },
        'D',
        "'Şunlardı' ile duyurulan sıralamadan önce iki nokta, cümle sonlarında nokta, 'Dr' kısaltmasından sonra nokta gelir. Son cümle soruyu dolaylı aktarır ('ne zaman uygulanacağını sordu'), soru cümlesi değildir; bu yüzden sonuna soru işareti değil nokta konur.",
    ),
    # düzey 3
    '0026': patch(
        '(I) Hamur mayalanınca şekil verilip fırına sürülür. (II) Önce un, su, tuz ve maya geniş bir kapta karıştırılır. (III) Fırından çıkan ekmek, kesilmeden önce bir süre dinlendirilir. (IV) Karışım, pürüzsüz bir hamur elde edilene kadar yoğrulur. (V) Yoğrulan hamurun üzeri örtülerek ılık bir yerde mayalanmaya bırakılır.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın dördüncü cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'A',
        "Ekmek yapımının sırası II (karıştırma) - IV (yoğurma) - V (mayalandırma) - I (şekil verip fırına sürme) - III (dinlendirme) biçimindedir. Dördüncü cümle I'dir.",
    ),
    # düzey 3
    '0027': patch(
        'Eleştiri, bir yapıtı küçümsemek için değil, onu daha iyi anlamak için yapılır. İyi bir eleştirmen, beğenmediği bir romanda bile yazarın neyi amaçladığını görmeye çalışır; yapıtı kendi zevkinin değil, kendi koşullarının içinde değerlendirir. Bu tutum, okura da yapıtın kusurlarını görürken değerini gözden kaçırmamayı öğretir.\n\nBu parçaya göre iyi bir eleştirmenle ilgili aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Yazarın amacını yapıtın değerinden daha önemli sayar.',
            'B': 'Okurun zevkine uygun yapıtları öne çıkarmaya özen gösterir.',
            'C': 'Beğenmediği yapıtlar hakkında yazmaktan kaçınır.',
            'D': 'Yapıtı değerlendirirken kişisel beğenisini ölçüt almaz.',
            'E': 'Yapıtların kusurlarından söz etmemeyi bir ilke olarak benimser.',
        },
        'D',
        "Parçada iyi eleştirmenin yapıtı 'kendi zevkinin değil, kendi koşullarının içinde' değerlendirdiği söyleniyor; yani kişisel beğenisini ölçüt almaz. Beğenmediği romanı da incelediği ve kusurları görmeyi öğrettiği için diğer yargılar parçayla çelişir.",
    ),
    # düzey 3
    '0028': patch(
        '(I) Kış aylarında evlerde tüketilen enerjinin büyük bölümü ısınmaya harcanır. (II) Pencere ve kapılardaki küçük aralıklar bile ısının önemli bir kısmının dışarı kaçmasına yol açar. (III) Bu nedenle yalıtım, hem faturaları düşürmenin hem de enerji tasarrufu sağlamanın etkili yollarından biridir. (IV) Yalıtımlı bir evde aynı sıcaklığa daha az yakıtla ulaşılır. (V) Kış turizmi, son yıllarda kayak merkezlerinin artmasıyla birlikte hızla gelişmektedir.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'E',
        'Parça, evlerde ısınma enerjisinin yalıtımla nasıl azaltılabileceğini anlatıyor. V. cümle kış turizmine geçerek konunun dışına çıkıyor.',
    ),
    # düzey 2
    '0029': patch(
        'Tren istasyona girdiğinde peronda kimse yoktu. Elindeki valizi yere bırakıp saatine baktı; beklediği kişi en az yarım saat gecikmişti. Bir süre bankta oturdu, sonra büfeye gidip bir çay aldı. Tam çayını bitirmişti ki arkasından tanıdık bir ses adını seslendi.\n\nBu parçanın anlatımında aşağıdakilerden hangisi ağır basmaktadır?',
        {
            'A': 'Açıklama',
            'B': 'Karşılaştırma',
            'C': 'Öyküleme',
            'D': 'Tartışma',
            'E': 'Betimleme',
        },
        'C',
        'Parçada bir kişinin başından geçenler zaman sırasıyla ve eylemlerle anlatılıyor (trenin gelişi, bekleme, çay alma, seslenilme); bu öykülemedir.',
    ),
    # düzey 3
    '0030': patch(
        'Gençliğimde her şeyi bilen biri olmak isterdim. Bir konuda soru sorulduğunda “Bilmiyorum.” demek bana yenilgi gibi gelirdi. Yaş ilerledikçe asıl bilgeliğin, bilmediğini kabul edebilmekte olduğunu gördüm. Bugün en çok güvendiğim insanlar, emin olmadıkları konuda susmayı bilenlerdir.\n\nBu parçanın yazarı için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Yaşlandıkça insanın merakının azaldığını düşünmektedir.',
            'B': 'Gençliğinde çevresindekilere sık sık danışmıştır.',
            'C': 'Zamanla bilmediğini kabul etmenin değerini anlamıştır.',
            'D': 'Bilgili görünmeyi bugün de önemli bulmaktadır.',
            'E': 'Emin olmadığı konularda da fikir bildirmeyi sürdürmektedir.',
        },
        'C',
        'Yazar, yaş ilerledikçe asıl bilgeliğin bilmediğini kabul etmek olduğunu gördüğünü söylüyor; bu, bilmediğini kabul etmenin değerini zamanla anladığını gösterir.',
    ),
    # düzey 3
    '0031': patch(
        '---- Örneğin bir işletme, satışlarının arttığını gösterse de alacaklarını tahsil edemiyorsa nakit sıkıntısına düşebilir. Kâğıt üzerinde kâr eden pek çok şirketin, ödemelerini yapamadığı için kapandığı görülmüştür. Bu yüzden yöneticiler kâr kadar nakit akışını da yakından izlemelidir.\n\nBu parçanın başına düşüncenin akışına göre aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Satışları artan işletmeler genellikle daha fazla vergi öder.',
            'B': 'Muhasebe kayıtlarının düzenli tutulması yasal bir zorunluluktur.',
            'C': 'Yöneticiler kârı artırmak için öncelikle maliyetleri düşürmelidir.',
            'D': 'Kârlı görünmek, bir işletmenin ayakta kalmasına tek başına yetmez.',
            'E': 'Alacakların tahsili, satış ekibinin en önemli görevleri arasındadır.',
        },
        'D',
        "'Örneğin' ile başlayan ikinci cümle, kâr eden ama nakit sıkıntısına düşen işletmeyi örnekliyor; örneklenen yargı, kârlı görünmenin ayakta kalmaya yetmediğidir. Paragrafın sonucu da (kâr kadar nakit akışı izlenmeli) bu girişe bağlanır.",
    ),
    # düzey 3
    '0032': patch(
        'Akıllı telefonlar, bilgiye ulaşmayı hiç olmadığı kadar kolaylaştırdı. Bir sorunun cevabını öğrenmek için artık kütüphaneye gitmek ya da birine danışmak gerekmiyor. Ancak bu kolaylığın bir bedeli var: Sürekli bildirim alan zihin, bir konuya uzun süre odaklanmakta zorlanıyor. Uzmanlar, gün içinde telefondan uzak kalınan zaman dilimleri belirlemenin dikkati güçlendirdiğini belirtiyor.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Bir sorunun cevabı artık başkasına danışmadan öğrenilebilmektedir.',
            'B': 'Sürekli gelen bildirimler, zihnin bir konuya uzun süre odaklanmasını güçleştirebilir.',
            'C': 'Telefondan uzak geçirilen süreler dikkati olumlu etkileyebilir.',
            'D': 'Akıllı telefonlar bilgiye ulaşmayı kolaylaştırmıştır.',
            'E': 'Uzmanlar, telefonun gün boyunca açık ve yakında tutulmasını önermektedir.',
        },
        'E',
        'Uzmanlar telefondan uzak kalınan zaman dilimleri belirlemeyi öneriyor; telefonun gün boyu açık ve yakında tutulmasını önerdikleri yargısı parçayla çelişir.',
    ),
    # düzey 3
    '0033': patch(
        "(I) Roman, 1950'li yıllarda bir sahil kasabasında geçiyor. (II) Bu, yazarın okunması en keyifli eseri. (III) Karakterler öyle canlı ki insan onları yıllardır tanıyormuş gibi hissediyor. (IV) Son bölüm bence biraz aceleyle yazılmış. (V) Yine de bu kitap, her okurun kitaplığında bulunmayı hak ediyor.\n\nBu parçadaki numaralanmış cümlelerden hangisinde nesnel bir yargı vardır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'A',
        'I. cümle romanın geçtiği zamanı ve yeri bildiriyor; doğruluğu kitaba bakılarak denetlenebilir, nesneldir. Diğer cümleler (en keyifli eser, canlı karakterler, aceleyle yazılmış son bölüm, kitaplıkta bulunmayı hak etmek) kişisel değerlendirmedir.',
    ),
    # düzey 2
    '0034': patch(
        'Bellek, her şeyi olduğu gibi saklayan bir arşivden çok, her açılışta yeniden düzenlenen bir çekmeceye benzer. Bir anıyı her hatırlayışımızda ona o günkü duygularımızdan bir şeyler ekleriz. Bu yüzden yıllar önce yaşadığımız bir olayı anlatırken aslında o olayın en son hatırladığımız biçimini anlatırız.\n\nBu parçada düşünceyi geliştirme yollarından hangisine başvurulmuştur?',
        {
            'A': 'Örneklendirme',
            'B': 'Sayısal verilerden yararlanma',
            'C': 'Tanımlama',
            'D': 'Tanık gösterme',
            'E': 'Benzetme',
        },
        'E',
        'Bellek, her açılışta yeniden düzenlenen bir çekmeceye benzetiliyor; düşünce bu benzetme üzerinden geliştiriliyor.',
    ),
    # düzey 2
    '0035': patch(
        'Sabahın **ilk** ışıklarıyla yola çıktık. Yol **uzun**du ama manzara her şeyi unutturuyordu. Köye **geç** vardık; ev sahibimiz bizi **sıcak** bir çorbayla karşıladı. **Bu** misafirperverliği hiç unutmadım.\n\nBu parçadaki kalın yazılmış sözcüklerden hangisi zarf (belirteç) olarak kullanılmıştır?',
        {
            'A': 'sıcak',
            'B': 'uzun',
            'C': 'Bu',
            'D': 'geç',
            'E': 'ilk',
        },
        'D',
        "'Geç vardık' sözünde 'geç', 'varmak' eyleminin zamanını bildirerek eylemi niteler; zarftır. 'İlk ışıklar', 'sıcak çorba', 'bu misafirperverlik' öbeklerinde sözcükler adları niteleyen sıfatlardır; 'uzundu' da adı niteleyen bir sıfatın ek-eylemle yüklem olmasıdır.",
    ),
    # düzey 3
    '0036': patch(
        'Bir toplumda güven duygusu zayıfladığında en basit işlemler bile pahalı hâle gelir. Taraflar birbirine güvenmediği için her anlaşmada daha fazla belge, daha fazla denetim ve daha fazla zaman gerekir. Güvenin yüksek olduğu toplumlarda ise bir el sıkışma, sayfalarca sözleşmenin yerini tutabilir. Bu yüzden güven, ekonomik hayatın görünmeyen ama en değerli sermayelerinden biridir.\n\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
        {
            'A': 'Ekonomik büyüme toplumdaki güven ortamını zayıflatır.',
            'B': 'Yazılı sözleşmeler ekonomik hayatta gereksizdir.',
            'C': 'Güven, ekonomik hayatın maliyetini düşürür.',
            'D': 'Denetim sayısı arttıkça toplumsal güven de artar.',
            'E': 'El sıkışarak yapılan anlaşmalar hukuken geçersizdir.',
        },
        'C',
        'Parça, güvensizliğin işlemleri pahalılaştırdığını, güvenin ise anlaşmaları kolaylaştırdığını anlatıp güveni ekonomik hayatın değerli bir sermayesi olarak niteliyor.',
    ),
    # düzey 3
    '0037': patch(
        'Çocuklara para yönetimini öğretmenin en etkili yolu, onlara küçük de olsa bir harçlık vermek ve bu parayı nasıl kullanacaklarına kendilerinin karar vermesine izin vermektir. Harçlığını ilk günden harcayan bir çocuk, hafta sonunda istediği şeyi alamadığında bekleme ve plan yapma gerektiğini kendisi keşfeder.\n\nBu paragraf aşağıdakilerden hangisiyle sürdürülebilir?',
        {
            'A': 'Çocuklar para birimlerini okulda matematik derslerinde öğrenir.',
            'B': 'Bu deneyim, ona öğütlerden daha kalıcı bir sorumluluk kazandırır.',
            'C': 'Bazı aileler ise harçlığı, çocuğun ev işlerine yardım etmesi karşılığında verir.',
            'D': 'Bankalar çocuklar için özel tasarruf hesapları açmaktadır.',
            'E': 'Harçlık miktarı ailenin gelir düzeyine göre belirlenmelidir.',
        },
        'B',
        'Paragraf, çocuğun harçlığını kendisi yöneterek deneyimle öğrenmesini anlatıyor. Bu deneyimin çocuğa kazandırdığı kalıcı sorumluluğu söyleyen cümle düşünceyi sürdürür; diğerleri konuyu başka yönlere çeker.',
    ),
    # düzey 3
    '0038': patch(
        '(I) Bu nedenle yeni gelen çalışanlar, ilk haftalarını çoğunlukla gözlem yaparak geçirir. (II) Ardından deneyimli bir çalışanın yanında küçük görevler üstlenmeye başlarlar. (III) Birkaç ay sonra ise kendi müşteri dosyalarını yönetebilecek duruma gelirler. (IV) Bu aşamalı süreç, hataların en aza indirilmesini sağlar. (V) Muhasebe bürolarında işler, yasal süreler nedeniyle yoğun ve hataya kapalıdır.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın ilk cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'E',
        "Doğru sıra V-I-II-III-IV'tür. Konuyu ve gerekçeyi ortaya koyan V. cümle girişte yer alır; I. cümledeki 'Bu nedenle' ifadesi, V. cümlede verilen yoğunluk ve hataya kapalılık durumuna bağlanır.",
    ),
    # düzey 3
    '0039': patch(
        'Bitkiler ışığa doğru yönelir; bu hareket, gövdenin gölgede kalan tarafındaki hücrelerin daha hızlı uzamasıyla gerçekleşir. Saksısını sık sık döndürdüğünüz bir bitkinin dik büyümesinin nedeni de budur. Saksı hiç döndürülmezse bitki, zamanla pencereye doğru belirgin biçimde eğilir.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Bitkinin eğilmesi, gövdedeki hücrelerin farklı hızlarda uzamasından kaynaklanır.',
            'B': 'Bitkiler karanlık ortamda büyümeyi tamamen durdurur.',
            'C': 'Bütün bitkiler ışığa aynı hızla yönelir.',
            'D': 'Saksının döndürülmesi bitkinin daha hızlı büyümesini sağlar.',
            'E': 'Işık alan taraftaki hücreler gölgedekilerden daha hızlı uzar.',
        },
        'A',
        'Parçaya göre gölgedeki taraf daha hızlı uzadığı için gövde ışığa doğru eğilir; yani eğilme hücrelerin farklı hızlarda uzamasından kaynaklanır. Işık alan tarafın daha hızlı uzadığı yargısı parçanın tersidir; saksı döndürmenin hızı değil dik büyümeyi sağladığı söylenmiştir.',
    ),
    # düzey 3
    '0040': patch(
        'Kitabın sonunda yazar şu soruyu soruyor ( ) “İnsan, kaybettiği şeyin değerini neden ancak kaybettikten sonra anlar ( )” Bu soru, bütün roman boyunca farklı biçimlerde karşımıza çıkıyor ( ) kimi zaman bir mektupta, kimi zaman bir rüyada ( )\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(:) (?) (:) (.)',
            'B': '(,) (?) (:) (...)',
            'C': '(;) (!) (,) (.)',
            'D': '(:) (.) (:) (.)',
            'E': '(:) (?) (;) (?)',
        },
        'A',
        "Aktarılacak sözden önce iki nokta, aktarılan soru cümlesinin sonunda soru işareti kullanılır. 'Karşımıza çıkıyor' sözünden sonra gelen açıklama ve örneklerden önce yine iki nokta konur; cümle nokta ile biter.",
    ),
    # düzey 3
    '0041': patch(
        "(I) Türk mutfağı, farklı coğrafyaların ürünlerini bir araya getiren zengin bir mirasa sahiptir. (II) Mutfak robotları, son yıllarda evlerde en çok satılan küçük ev aletleri arasına girdi. (III) Ege'nin zeytinyağlıları, Karadeniz'in balık yemekleri ve Güneydoğu'nun kebapları bu zenginliğin örnekleridir. (IV) Her bölgenin yemekleri, o bölgenin iklimini ve tarımını yansıtır. (V) Bu yüzden bir yemeğin tarifi, aynı zamanda bir coğrafyanın da öyküsüdür.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'B',
        "Parça, Türk mutfağının bölgesel zenginliğini ve yemeklerin coğrafyayı yansıtmasını anlatıyor. II. cümle mutfak robotlarının satışına geçerek konunun dışına çıkıyor; III. cümledeki 'bu zenginlik' de I. cümleye bağlanıyor.",
    ),
    # düzey 3
    '0042': patch(
        'Bağımsız denetim, işletmenin finansal tablolarının gerçeği doğru yansıtıp yansıtmadığına dair makul bir güvence sağlar. Denetçi bütün işlemleri tek tek incelemez; önemli hataların bulunabileceği alanları belirleyip bu alanlarda örnekleme yapar. Bu nedenle denetim raporu, tablolarda hiç hata olmadığının değil, önemli bir yanlışlık bulunmadığına ilişkin bir görüşün ifadesidir.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Denetçi görüşünü, bütün işlemleri tek tek inceleyerek oluşturur.',
            'B': 'Denetimden geçmiş tablolarda, önemlilik sınırının altında kalan hatalar bulunabilir.',
            'C': 'Denetim raporu, tablolar hakkında bir görüş bildirir.',
            'D': 'Denetçi riskli alanlarda örnekleme yöntemine başvurur.',
            'E': 'Bağımsız denetim makul düzeyde bir güvence sağlar.',
        },
        'A',
        'Parçada denetçinin bütün işlemleri tek tek incelemediği, örnekleme yaptığı açıkça belirtiliyor; bu nedenle görüşünü bütün işlemleri inceleyerek oluşturduğu söylenemez.',
    ),
    # düzey 2
    '0043': patch(
        'Gündelik hayatta kullandığımız pek çok buluş, aslında bir rastlantının ürünüdür. Örneğin radar üzerinde çalışan bir mühendis, cebindeki çikolatanın cihazın yanında eridiğini fark etmiş; bu gözlem mikrodalga fırının geliştirilmesine yol açmıştır. Laboratuvarda unutulan bir kültür kabında üreyen küf de penisilinin keşfedilmesini sağlamıştır.\n\nBu parçada düşünceyi geliştirmek için ağırlıklı olarak aşağıdakilerden hangisine başvurulmuştur?',
        {
            'A': 'Sayısal verilerden yararlanma',
            'B': 'Benzetme',
            'C': 'Tanık gösterme',
            'D': 'Tanımlama',
            'E': 'Örneklendirme',
        },
        'E',
        'Buluşların rastlantının ürünü olabileceği yargısı, mikrodalga fırın ve penisilin örnekleriyle somutlaştırılıyor; bu örneklendirmedir.',
    ),
    # düzey 3
    '0044': patch(
        'Eski eşyaları onarmak, bir zamanlar zorunluluktan yapılan bir işti. Yırtılan giysi yamanır, bozulan saat ustaya götürülür, kırılan sandalye yeniden tutkallanırdı. Bugün ise yenisini almak çoğu zaman onarmaktan daha ucuz görünüyor. Oysa her atılan eşya, onu üretmek için harcanan emeği, enerjiyi ve hammaddeyi de çöpe gönderiyor. Onarım kültürünü yeniden canlandırmak, bütçemizle birlikte doğayı da korumanın yollarından biri olabilir.\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Eski ustaların sayısı gün geçtikçe azalmaktadır.',
            'B': 'Üretimde harcanan enerji son yıllarda belirgin biçimde artmıştır.',
            'C': 'Yeni eşya almak çoğu zaman onarmaktan daha pahalıya gelir.',
            'D': 'Onarım kültürü hem bütçeyi hem doğayı korur.',
            'E': 'Giysilerin yamanması geçmişte bir moda olarak görülürdü.',
        },
        'D',
        'Yazar, atılan her eşyanın emek, enerji ve hammadde kaybı olduğunu belirtip onarım kültürünün yeniden canlanmasının hem bütçeyi hem doğayı koruyacağını vurguluyor.',
    ),
    # düzey 3
    '0045': patch(
        '(I) Önce işletmenin geçmiş yıllara ait satış verileri incelenir. (II) Bu verilerden yola çıkılarak gelecek yılın satış tahmini yapılır. (III) Hazırlanan bütçeler bir araya getirilerek ana bütçe oluşturulur. (IV) Satış tahminine göre üretim ve gider bütçeleri hazırlanır. (V) Son olarak ana bütçe, yönetim kurulunun onayına sunulur.\n\nBu parçadaki numaralanmış cümlelerden hangi ikisinin yeri değiştirilirse düşüncenin akışı düzelir?',
        {
            'A': 'I ve II',
            'B': 'II ve IV',
            'C': 'III ve IV',
            'D': 'III ve V',
            'E': 'IV ve V',
        },
        'C',
        "Ana bütçe, üretim ve gider bütçeleri hazırlandıktan sonra oluşturulabilir. III ve IV yer değiştirince sıra 'veriler - satış tahmini - üretim ve gider bütçeleri - ana bütçe - onay' biçiminde düzelir.",
    ),
    # düzey 3
    '0046': patch(
        'Göç eden kuşların binlerce kilometrelik yolculuklarında yönlerini nasıl buldukları uzun süre merak konusu oldu. Araştırmalar, bu kuşların güneşin konumundan, yıldızlardan ve yerin manyetik alanından yararlandığını gösteriyor. Bulutlu gecelerde yıldızları göremeyen kuşların manyetik alana daha çok güvendiği düşünülüyor.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Güneşin konumu kuşlar için yıldızlardan daha güvenilir bir ipucudur.',
            'B': 'Manyetik alan, kuşların gündüz yararlandığı başlıca ipucudur.',
            'C': 'Kuşlar bulutlu havalarda göç etmeyi bırakır.',
            'D': 'Kuşların yön bulma biçimi artık tartışılmamaktadır.',
            'E': 'Göçmen kuşlar yön bulmak için birden fazla ipucundan yararlanır.',
        },
        'E',
        'Parçada kuşların güneş, yıldızlar ve manyetik alan gibi birden çok ipucunu kullandığı belirtiliyor. Bulutlu gecelerde göç etmeyi bıraktıkları değil, manyetik alana daha çok güvendikleri söyleniyor.',
    ),
    # düzey 3
    '0047': patch(
        "(I) Kızılırmak, tamamı Türkiye sınırları içinde kalan en uzun akarsudur. (II) Irmak, Sivas'ın doğusundaki dağlardan doğup Karadeniz'e dökülür. (III) Üzerinde enerji üretimi ve sulama amaçlı birçok baraj bulunmaktadır. (IV) Kıyısındaki kasabalar, ülkenin en huzurlu yerleşimleri arasında sayılmalıdır. (V) Irmak, adını sularına renk veren kızıl topraktan alır.\n\nBu parçadaki numaralanmış cümlelerden hangisinde nesnel bir yargıya yer verilmemiştir?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'D',
        "IV. cümledeki 'en huzurlu yerleşimler arasında sayılmalıdır' değerlendirmesi kişisel bir görüştür ve kanıtlanamaz. Diğer cümleler ırmağın uzunluğu, kaynağı, barajları ve adının kökeni hakkında denetlenebilir bilgiler verir.",
    ),
    # düzey 3
    '0048': patch(
        'Bir yazarın üslubu, parmak izi gibi kendine özgüdür. ---- Kimi kısa ve keskin cümleleri sever, kimi uzun ve dolambaçlı anlatımları. Bu farklılık, aynı olayı anlatan iki yazarın metinlerini birbirinden kolayca ayırt etmemizi sağlar.\n\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Üslup, yazarın yaşadığı dönemin olaylarından etkilenmez.',
            'B': 'Yazarların cümle tercihleri farklıdır.',
            'C': 'Okurlar çoğunlukla kısa romanları daha çok sever.',
            'D': 'Eleştirmenler yazarları üsluplarına göre sınıflandırmaktan kaçınır.',
            'E': 'Bazı yazarlar yapıtlarını takma adla yayımlamayı seçer.',
        },
        'B',
        "Boşluktan sonra gelen 'Kimi kısa ve keskin cümleleri sever, kimi ...' cümlesi, yazarların cümle tercihlerinin farklılığını örnekliyor. Bu örneklere bağlanan genel yargı, yazarların cümle tercihlerinin farklı olduğudur.",
    ),
    # düzey 3
    '0049': patch(
        'Çocukken babam bana bisiklet sürmeyi öğretirken arkamdan tutuyormuş gibi yapardı. Bir gün arkama döndüğümde onun çoktan elini bıraktığını, metrelerce uzakta durduğunu gördüm. O ana kadar düşmemiştim; çünkü düşebileceğimi bilmiyordum. Bugün bile bir işe başlarken korktuğumda o anı hatırlarım.\n\nBu parçada anlatıcının vurguladığı düşünce aşağıdakilerden hangisidir?',
        {
            'A': 'Çocuklara bisiklet sürmeyi öğretmek, anne babadan büyük bir sabır ister.',
            'B': 'Babalar çocuklarını aşırı korumaktan kaçınmalıdır.',
            'C': 'Çocukluk anıları zamanla bulanıklaşıp önemini yitirir.',
            'D': 'İnsan, yapabileceklerini çoğu zaman kendine güvendiğinde fark eder.',
            'E': 'Düşme korkusu, öğrenmeyi çoğu durumda hızlandırır.',
        },
        'D',
        'Anlatıcı, düşebileceğini bilmediği için düşmediğini ve korktuğunda bu anıyı hatırladığını söylüyor; vurgulanan düşünce, insanın kendine güvendiğinde yapabileceklerini fark ettiğidir.',
    ),
    # düzey 3
    '0050': patch(
        '(I) Kooperatifler, üyelerinin ortak ekonomik ihtiyaçlarını karşılamak için kurulan örgütlerdir. (II) Üreticiler bir araya gelerek ürünlerini aracılara bağlı kalmadan daha iyi fiyata satabilir. (III) Kırsal kesimde internet erişimi, son yıllarda belirgin biçimde yaygınlaştı. (IV) Toplu alım yaparak girdi maliyetlerini de düşürebilirler. (V) Böylece küçük üreticiler, büyük işletmelerle rekabet edebilecek bir güce ulaşır.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'C',
        'Parça, kooperatiflerin küçük üreticilere sağladığı satış ve maliyet avantajlarını anlatıyor. III. cümle internet erişimine geçerek konunun dışına çıkıyor; IV. cümle de II. cümlenin devamıdır.',
    ),
    # düzey 3
    '0051': patch(
        'Ünlü ressamların atölyelerinde çalışan çıraklar, yıllarca boya hazırlar, tuvalleri gerer ve ustanın tablolarındaki arka planları boyarlardı. Ustanın imzasını taşıyan pek çok tablonun bazı bölümlerinin aslında çıraklar tarafından yapıldığı bugün biliniyor. O dönemde bu durum bir aldatmaca değil, olağan bir çalışma düzeni olarak görülüyordu.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Çıraklar ustanın tablolarının bazı bölümlerini boyardı.',
            'B': 'Çırakların işleri arasında boya hazırlamak da vardı.',
            'C': 'Ustanın imzasını taşıyan bazı tablolar, aslında atölyedeki ortak bir emeğin ürünüdür.',
            'D': 'Atölyedeki iş bölümü dönemin koşullarında olağan karşılanırdı.',
            'E': 'O dönemde çırakların tablolara katkısı ustaya karşı bir hile sayılırdı.',
        },
        'E',
        'Son cümle bu durumun o dönemde aldatmaca değil, olağan bir çalışma düzeni olarak görüldüğünü söylüyor; hile sayıldığı yargısı parçayla çelişir.',
    ),
    # düzey 3
    '0052': patch(
        'Yürüyüş, koşuya göre eklemleri daha az yorar; buna karşılık aynı sürede daha az enerji harcatır. Bir spor hekimi, “Düzenli yürüyüş, özellikle ileri yaştakiler için koşudan daha sürdürülebilir bir egzersizdir.” diyor. Kısacası hangisinin seçileceği, kişinin yaşına ve hedefine bağlıdır.\n\nBu parçada düşünceyi geliştirme yollarından hangileri kullanılmıştır?',
        {
            'A': 'Örneklendirme - Sayısal verilerden yararlanma',
            'B': 'Tanık gösterme - Benzetme',
            'C': 'Sayısal verilerden yararlanma - Karşılaştırma',
            'D': 'Karşılaştırma - Tanık gösterme',
            'E': 'Benzetme - Tanımlama',
        },
        'D',
        'Yürüyüş ve koşu, eklemlere etkisi ve harcanan enerji bakımından karşılaştırılıyor; ardından bir spor hekiminin sözü aktarılıyor (tanık gösterme). Parçada sayısal veri ve benzetme bulunmadığından bunları içeren seçenekler yanlıştır.',
    ),
    # düzey 3
    '0053': patch(
        '(I) Toplanan yapraklar önce gölgede soldurulur. (II) Çay hasadı, ilkbaharda filizlerin sürmesiyle başlar. (III) Ardından yapraklar kıvrılarak hücre özsuyunun dışarı çıkması sağlanır. (IV) Rengi koyulaşan yapraklar son olarak kurutulur. (V) Kıvrılan yapraklar nemli bir ortamda bekletilerek fermente edilir.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın üçüncü cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'C',
        "Siyah çay yapımının sırası II (hasat) - I (soldurma) - III (kıvırma) - V (fermantasyon) - IV (kurutma) biçimindedir. Üçüncü cümle III'tür.",
    ),
    # düzey 2
    '0054': patch(
        'Faiz, ödünç alınan bir paranın kullanılması karşılığında ödenen bedeldir. Borç alan kişi, anaparanın yanında belirli bir oran üzerinden hesaplanan bu bedeli de geri öder. Faiz oranı yükseldikçe borçlanmanın maliyeti artar; düştükçe azalır.\n\nBu parçanın anlatımında aşağıdakilerden hangisi ağır basmaktadır?',
        {
            'A': 'Tartışma',
            'B': 'Açıklama',
            'C': 'Öyküleme',
            'D': 'Söyleşi',
            'E': 'Betimleme',
        },
        'B',
        'Parça, faizin ne olduğunu ve oranın borçlanma maliyetine etkisini bilgi vermek amacıyla anlatıyor; bir görüşü savunmuyor, olay anlatmıyor, bir şeyi resmetmiyor. Bu, açıklayıcı anlatımdır.',
    ),
    # düzey 3
    '0055': patch(
        'Bir fotoğraf karesi, gerçeğin küçük bir parçasını gösterir. Fotoğrafçı neyi kadrajın içine alacağına, neyi dışarıda bırakacağına karar verirken aslında bize bir bakış açısı sunar. Aynı kalabalığı çeken iki fotoğrafçıdan biri öfkeli yüzleri, öteki gülümseyen çocukları öne çıkarabilir. Bu yüzden bir fotoğrafa bakarken gördüğümüz kadar göremediğimizi de düşünmeliyiz.\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Fotoğraf makineleri geliştikçe görüntü kalitesi artmaktadır.',
            'B': 'Fotoğraf, gerçeği çekenin gözüyle yansıtır.',
            'C': 'İyi bir fotoğrafçı kalabalıkları çekmekten kaçınmalıdır.',
            'D': 'Fotoğraflar resimden daha gerçekçi bir anlatım sunar.',
            'E': 'Gülümseyen insanların fotoğrafları daha çok ilgi görür.',
        },
        'B',
        'Parça, fotoğrafçının kadraj seçimiyle gerçeğin bir bölümünü ve bir bakış açısını sunduğunu anlatıyor; yani fotoğraf gerçeği çekenin gözüyle, onun seçimleriyle sınırlı olarak yansıtır.',
    ),
    # düzey 2
    '0056': patch(
        'Ankara ( ) İstanbul hattında yeni seferler başladı ( ) Biletler internetten, gişelerden ve mobil uygulamadan alınabiliyor ( ) Yetkililer, yoğunluk sürerse sefer sayısının artırılacağını açıkladı ( )\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(-) (.) (...) (!)',
            'B': '(-) (;) (.) (.)',
            'C': '(/) (.) (:) (.)',
            'D': '(,) (.) (.) (?)',
            'E': '(-) (.) (.) (.)',
        },
        'E',
        "İki yer adı arasında 'arasında, ile' anlamı veren kısa çizgi kullanılır (Ankara-İstanbul hattı). Diğer üç yer bitmiş bildirme cümlelerinin sonudur; nokta konur.",
    ),
    # düzey 3
    '0057': patch(
        "Ebru, kitreyle yoğunlaştırılmış su üzerine serpilen boyalarla yapılan geleneksel bir süsleme sanatıdır. Sanatçı, boyaları fırça ve bizle yönlendirerek desenler oluşturur; ardından üzerine kâğıt kapatarak deseni kâğıda aktarır. Her ebru tek bir baskıdan ibaret olduğu için iki eserin birbirinin aynısı olması mümkün değildir. Ebru sanatı, 2014 yılında UNESCO İnsanlığın Somut Olmayan Kültürel Mirası Temsilî Listesi'ne alınmıştır.\n\nBu parçada ebruyla ilgili aşağıdakilerden hangisine değinilmemiştir?",
        {
            'A': 'Desenin kâğıda nasıl aktarıldığına',
            'B': 'Eserlerin birbirinden farklı olmasının nedenine',
            'C': 'Uluslararası bir listeye alındığına',
            'D': 'Yapımında kullanılan araçlara',
            'E': 'İlk kez hangi dönemde ortaya çıktığına',
        },
        'E',
        'Parçada ebrunun yapımında kullanılan araçlardan (fırça, biz), desenin kâğıda aktarılmasından, her eserin tek baskı olmasından ve UNESCO listesine alınmasından söz ediliyor; ortaya çıktığı döneme ise değinilmiyor.',
    ),
    # düzey 2
    '0058': patch(
        'Fabrikanın **bacası** sabahtan beri tütüyordu. İşçiler **ağır** kasaları kamyona taşıyor, ustabaşı listeyi kontrol ediyordu. Öğle arasında herkes bahçedeki **uzun** masaya oturdu. Yemekte, emekliliği yaklaşan usta herkese **tatlı** bir veda konuşması yaptı. Konuşmanın sonunda masadaki **ekmekleri** paylaştılar.\n\nBu parçadaki kalın yazılmış sözcüklerden hangisi mecaz anlamıyla kullanılmıştır?',
        {
            'A': 'tatlı',
            'B': 'ekmekleri',
            'C': 'uzun',
            'D': 'bacası',
            'E': 'ağır',
        },
        'A',
        "'Tatlı bir konuşma' ifadesinde 'tatlı', tat bildiren gerçek anlamından uzaklaşarak 'hoş, içten' anlamında kullanılmıştır. Baca, ağır kasalar, uzun masa ve ekmek sözcükleri gerçek anlamlarıyla kullanılmıştır.",
    ),
    # düzey 3
    '0059': patch(
        'Her sabah işe gitmeden önce yarım saat yürürüm. Bu alışkanlığı yıllar önce doktorumun önerisiyle edindim; ilk haftalarda üşenip kaç kez vazgeçtiğimi hatırlamıyorum bile. Şimdi ise yürüyüş yapmadığım günlerde kendimi eksik hissediyorum. Bazen yürürken yazacağım yazıların taslağını kafamda kuruyor, eve döner dönmez not alıyorum.\n\nBu parçanın yazarıyla ilgili aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yürüyüş yapmadığı günlerde bir eksiklik duyar.',
            'B': 'Yürüyüşünü sabahları, işe gitmeden önce yapar.',
            'C': 'Yürüyüş alışkanlığını kimseden etkilenmeden, kendi isteğiyle edinmiştir.',
            'D': 'Yürüyüş sırasında yazılarıyla ilgili düşünür.',
            'E': 'Yürüyüşe başladığı ilk zamanlarda zorlanmıştır.',
        },
        'C',
        'Yazar bu alışkanlığı doktorunun önerisiyle edindiğini söylüyor; kimseden etkilenmeden edindiği yargısı parçayla çelişir.',
    ),
    # düzey 3
    '0060': patch(
        'Kayıt dışı ekonomi, devletin vergi gelirlerini azaltmakla kalmaz. Faturasız satış yapan bir işletme, vergisini düzenli ödeyen rakibine karşı haksız bir fiyat avantajı elde eder. Kayıt dışı çalıştırılan işçi ise sağlık güvencesinden ve emeklilik hakkından yoksun kalır. Bu nedenle kayıt dışılıkla mücadele, vergi gelirlerinin ötesinde adil rekabet ve sosyal güvenlik açısından da önem taşır.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Faturasız satış yapan işletmeler daha yüksek fiyatla satış yapar.',
            'B': 'Kayıt dışılıkla mücadele işçi ücretlerini düşürür.',
            'C': 'Kayıt dışı ekonomi, kurallara uyan işletmelerin rekabet gücünü zayıflatır.',
            'D': 'Kayıt dışı çalışan işçiler emeklilik hakkı kazanabilir.',
            'E': 'Kayıt dışı ekonominin zararı vergi gelirleriyle sınırlıdır.',
        },
        'C',
        'Parçada faturasız satış yapan işletmenin vergisini ödeyen rakibine karşı haksız fiyat avantajı kazandığı söyleniyor; buradan kurallara uyan işletmelerin rekabet gücünün zayıfladığı çıkarılır.',
    ),
    # düzey 3
    '0061': patch(
        '(I) Kent ağaçları, yaz aylarında caddelerin sıcaklığını birkaç derece düşürebilir. (II) Ağaç dikimi, Osmanlı döneminde vakıflar aracılığıyla da desteklenirdi. (III) Yaprakların gölgesi ve buharlaşma, asfaltın ısı biriktirmesini azaltır. (IV) Bu nedenle ağaçlıklı bir sokakta yürüyen biri, açıkta kalan bir meydana göre belirgin bir serinlik hisseder. (V) Belediyelerin yeşil alan planlarını iklime uyum açısından ele alması bu yüzden önemlidir.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'B',
        'Parça kent ağaçlarının serinletici etkisini anlatıyor. II. cümle ağaç dikiminin tarihteki desteklenme biçimine geçerek konunun dışına çıkıyor.',
    ),
    # düzey 3
    '0062': patch(
        '(I) Sesli kitaplar son yıllarda okuma alışkanlığına yeni bir boyut kazandırdı. (II) Trafikte geçen süreyi ya da ev işlerini bir romanı dinleyerek değerlendirmek mümkün hâle geldi. (III) Bazı okurlar, iyi bir seslendirmenin metni daha canlı kıldığını düşünüyor. (IV) Eleştirmenlerin bir kısmı ise dinlemenin, okurun metinle kurduğu yavaş ve derin ilişkiyi zayıflattığını savunuyor. (V) Kâğıt fiyatlarındaki artış, yayınevlerinin baskı sayılarını düşürmesine yol açtı.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'E',
        'Parça sesli kitapların okumaya getirdiği yenilikleri ve bunlara yöneltilen eleştirileri ele alıyor. V. cümle kâğıt fiyatlarından söz ederek konudan uzaklaşıyor.',
    ),
    # düzey 3
    '0063': patch(
        "(I) Arıcılık, Anadolu'da binlerce yıllık bir geçmişe sahiptir. (II) Kovanlar eskiden ağaç kütüklerinden ya da hasırdan yapılır, bal alınırken kovan çoğu zaman zarar görürdü. (III) Balın rengi ve tadı, arıların konduğu çiçeklere göre değişir. (IV) Çerçeveli modern kovanlar ise peteklerin kovana zarar vermeden alınmasını sağladı. (V) Bu yenilik, arıcılığı göçebe bir uğraştan planlı bir üretim dalına dönüştürdü.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'C',
        'Parça kovan yapımındaki değişimi ve bunun arıcılığa etkisini anlatıyor. III. cümle balın rengi ve tadından söz ederek bu akışı kesiyor.',
    ),
    # düzey 3
    '0064': patch(
        '(I) Bir dili öğrenmenin en etkili yollarından biri, o dili konuşan insanlarla düzenli iletişim kurmaktır. (II) Ders kitaplarındaki kalıplar, gündelik konuşmanın hızını ve esnekliğini çoğu zaman yansıtmaz. (III) Karşılıklı konuşma ise öğrenciyi beklenmedik sorulara anında yanıt vermeye zorlar. (IV) Türkçe, eklemeli bir dil olarak sözcük türetmede oldukça zengindir. (V) Bu zorlanma, zamanla kişinin dili düşünmeden kullanabilmesini sağlar.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'D',
        "Parça dil öğreniminde karşılıklı konuşmanın yararını anlatıyor. IV. cümle Türkçenin yapısına geçerek akışı bozuyor; V. cümledeki 'Bu zorlanma' da III. cümleye bağlanıyor.",
    ),
    # düzey 3
    '0065': patch(
        '(I) Bu nedenle sabah saatlerinde yapılan sulama hem tasarruf sağlar hem de bitkiyi korur. (II) Bahçe sulamasında en sık yapılan hata, suyu günün en sıcak saatlerinde vermektir. (III) Akşam sulaması ise yaprakların uzun süre ıslak kalmasına ve mantar hastalıklarına yol açabilir. (IV) Öğle güneşinde verilen suyun önemli bir kısmı köklere ulaşmadan buharlaşır. (V) Sabah serinliğinde verilen su ise toprağa yavaşça işler ve gün boyu bitkinin ihtiyacını karşılar.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın dördüncü cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'E',
        "Sıralama II-IV-III-V-I'dir: hata tanıtılır, öğle sulamasının sakıncası, akşam sulamasının sakıncası, sabah sulamasının yararı ve 'Bu nedenle' ile sonuç gelir. Dördüncü cümle V'tir.",
    ),
    # düzey 3
    '0066': patch(
        '(I) Ancak kısa sürede, telefonun iş görüşmelerini kolaylaştıran bir araç olduğu anlaşıldı. (II) Telefon ilk icat edildiğinde birçok kişi tarafından gereksiz bir oyuncak olarak görülmüştü. (III) Bugün ise cebimizdeki telefon, bankacılıktan sağlığa kadar pek çok işi yürüttüğümüz bir merkeze dönüştü. (IV) Yaygınlaştıkça evlerin de vazgeçilmez eşyası hâline geldi. (V) Bu dönüşüm, bir buluşun değerinin çoğu zaman ancak zamanla anlaşılabildiğini gösteriyor.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın ikinci cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'A',
        "Sıralama II-I-IV-III-V'tir: ilk algı, 'Ancak' ile gelen değişim, yaygınlaşma, bugünkü durum ve genel sonuç. İkinci cümle I'dir.",
    ),
    # düzey 3
    '0067': patch(
        '(I) Böylece okul bahçesi, ders saatleri dışında da mahalleye açık bir alana dönüştü. (II) Okulun boş duran bahçesi uzun süre yalnızca teneffüslerde kullanılıyordu. (III) Okul yönetimi, velilerle birlikte bahçeye bir sebze tarhı ve oturma alanı yapmaya karar verdi. (IV) Hafta sonları öğrencilerle birlikte gelen aileler, tarhların bakımını sırayla üstlendi. (V) Bu deneyim, küçük bir düzenlemenin bir mekânın işlevini nasıl değiştirebileceğini gösteriyor.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın üçüncü cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'D',
        "Sıralama II-III-IV-I-V'tir: eski durum, karar, uygulama, 'Böylece' ile ortaya çıkan sonuç ve genel yargı. Üçüncü cümle IV'tür.",
    ),
    # düzey 3
    '0068': patch(
        '(I) Oysa çoğu zaman bu yorgunluğun asıl nedeni beden değil, zihindir. (II) Uzun bir iş gününün sonunda kendimizi bitkin hissederiz. (III) Gün boyu verilen sayısız küçük karar, zihni fark ettirmeden tüketir. (IV) Bu yüzden akşamları kısa bir yürüyüş yapmak ya da sessiz bir ortamda oturmak, uzun bir uykudan daha dinlendirici olabilir. (V) Bunu çoğunlukla fiziksel bir yorgunluk sanırız.\n\nNumaralanmış cümlelerle anlamlı bir paragraf oluşturulursa paragrafın ilk cümlesi hangisi olur?',
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'B',
        "Sıralama II-V-I-III-IV'tür: durum, yaygın yorum, 'Oysa' ile düzeltme, gerekçe ve öneri. İlk cümle II'dir.",
    ),
    # düzey 3
    '0069': patch(
        "(I) Kahvenin Avrupa'ya yayılması 17. yüzyılda gerçekleşti. (II) Kahvehaneler kısa sürede tüccarların, yazarların ve öğrencilerin buluşma yeri oldu. (III) Venedik ve Londra'da ilk kahvehaneler açıldı. (IV) Bu mekânlarda gazeteler okunuyor, haberler tartışılıyor, ticari anlaşmalar yapılıyordu. (V) Bu yüzden bazı tarihçiler kahvehaneleri kamusal tartışmanın doğduğu yerler olarak görür.\n\nBu parçadaki numaralanmış cümlelerden hangi ikisinin yeri değiştirilirse düşüncenin akışı düzelir?",
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'III ve IV',
            'E': 'IV ve V',
        },
        'C',
        'Kahvehanelerin buluşma yeri olması, önce açılmalarından sonra gelmelidir. II ile III yer değiştirince sıra I-III-II-IV-V olur.',
    ),
    # düzey 3
    '0070': patch(
        '(I) Uyku boyunca vücut ısıları belirgin biçimde düşer. (II) Kış geldiğinde korunaklı bir yuvaya çekilirler. (III) Kış uykusuna yatan hayvanlar, sonbaharda yoğun biçimde beslenerek vücutlarında yağ depolar. (IV) Isının düşmesiyle kalp atışları ve solunum yavaşlar, enerji tüketimi en aza iner. (V) Bahar geldiğinde depoladıkları yağın büyük kısmını tüketmiş olarak uyanırlar.\n\nBu parçadaki numaralanmış cümlelerden hangi ikisinin yeri değiştirilirse düşüncenin akışı düzelir?',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II ve IV',
            'D': 'III ve V',
            'E': 'IV ve V',
        },
        'B',
        'Parça sonbaharda yağ depolamayla başlamalıdır. I ile III yer değiştirince sıra yağ depolama, yuvaya çekilme, ısının düşmesi, kalbin yavaşlaması ve baharda uyanma olur.',
    ),
    # düzey 2
    '0071': patch(
        'Biyoçeşitlilik, belirli bir bölgede yaşayan canlı türlerinin, bu türlerin genetik farklılıklarının ve oluşturdukları ekosistemlerin bütününü ifade eder. Kavram yalnızca tür sayısını değil, türlerin birbirleriyle ve çevreleriyle kurduğu ilişkileri de kapsar. Bu nedenle bir ormandaki ağaç türlerinin sayısı kadar, o ağaçlara bağlı yaşayan böceklerin ve mantarların çeşitliliği de biyoçeşitliliğin parçasıdır.\n\nBu parçada düşünceyi geliştirmek için ağırlıklı olarak aşağıdakilerden hangisine başvurulmuştur?',
        {
            'A': 'Tanımlama',
            'B': 'Karşılaştırma',
            'C': 'Tanık gösterme',
            'D': 'Sayısal verilerden yararlanma',
            'E': 'Benzetme',
        },
        'A',
        "Parça 'biyoçeşitlilik' kavramının ne olduğunu ve neleri kapsadığını açıklıyor; ağırlıklı yol tanımlamadır.",
    ),
    # düzey 2
    '0072': patch(
        'Usta bir öykücünün en önemli becerisi, söylemediklerini okura sezdirebilmesidir. Uzun yıllar öykü atölyeleri yöneten bir yazar, öğrencilerine sık sık "Öykünün gücü, yazmadığın cümlelerdedir." derdi. Gerçekten de iyi bir öykü bittiğinde okur, metinde açıkça yer almayan bir duyguyla baş başa kalır.\n\nBu parçada düşünceyi geliştirmek için ağırlıklı olarak aşağıdakilerden hangisine başvurulmuştur?',
        {
            'A': 'Tanımlama',
            'B': 'Karşılaştırma',
            'C': 'Sayısal verilerden yararlanma',
            'D': 'Örneklendirme',
            'E': 'Tanık gösterme',
        },
        'E',
        'Yazar, düşüncesini desteklemek için deneyimli bir öykü yazarının sözüne başvuruyor; bu tanık göstermedir.',
    ),
    # düzey 2
    '0073': patch(
        'Kâğıt kitap, okura sayfalar arasında rahatça gidip gelme ve kenarına not alma imkânı verir. Elektronik kitap ise yüzlerce eseri tek bir cihazda taşımayı ve yazı boyutunu dilediğince ayarlamayı mümkün kılar. Biri dokunma ve sahiplenme duygusuyla, öteki pratikliğiyle öne çıkar.\n\nBu parçada düşünceyi geliştirmek için ağırlıklı olarak aşağıdakilerden hangisine başvurulmuştur?',
        {
            'A': 'Karşılaştırma',
            'B': 'Tanımlama',
            'C': 'Tanık gösterme',
            'D': 'Sayısal verilerden yararlanma',
            'E': 'Benzetme',
        },
        'A',
        'Parça kâğıt kitapla elektronik kitabın özelliklerini karşılaştırıyor.',
    ),
    # düzey 3
    '0074': patch(
        'Ekonomide fırsat maliyeti, bir seçim yapılırken vazgeçilen en iyi alternatifin değeridir. Örneğin hafta sonunu sınava çalışarak geçiren bir öğrencinin fırsat maliyeti, o sürede yarı zamanlı bir işte kazanabileceği ücret ya da arkadaşlarıyla geçirebileceği zamandır. Kavram, her tercihin bir bedeli olduğunu hatırlatır.\n\nBu parçada düşünceyi geliştirme yollarından hangileri kullanılmıştır?',
        {
            'A': 'Karşılaştırma ve tanık gösterme',
            'B': 'Tanımlama ve örneklendirme',
            'C': 'Benzetme ve tanımlama',
            'D': 'Örneklendirme ve sayısal veriler',
            'E': 'Tanık gösterme ve benzetme',
        },
        'B',
        "İlk cümle fırsat maliyetini tanımlıyor, ikinci cümle 'Örneğin' ile bir örnek veriyor.",
    ),
    # düzey 3
    '0075': patch(
        "İlçede 2015 yılında kişi başına günlük su tüketimi 210 litreydi. Akıllı sayaçların kullanılmaya başlanmasından sonra bu rakam 2024'te 165 litreye geriledi. Aynı dönemde sayaç uygulanmayan komşu ilçede tüketim neredeyse değişmedi ve 205 litre dolayında kaldı. Bu tablo, ölçmenin tasarrufun ilk adımı olduğunu gösteriyor.\n\nBu parçada düşünceyi geliştirme yollarından hangileri kullanılmıştır?",
        {
            'A': 'Tanımlama ve tanık gösterme',
            'B': 'Benzetme ve örneklendirme',
            'C': 'Sayısal verilerden yararlanma ve tanık gösterme',
            'D': 'Tanımlama ve benzetme',
            'E': 'Sayısal verilerden yararlanma ve karşılaştırma',
        },
        'E',
        'Parça tüketim rakamlarını veriyor ve iki ilçeyi birbiriyle karşılaştırıyor.',
    ),
    # düzey 2
    '0076': patch(
        'Sabahın ilk ışıkları limana vurduğunda kayıklar, durgun suyun üstünde hafifçe sallanıyordu. Rıhtım boyunca dizilmiş ağların arasından tuz ve yosun kokusu yükseliyor, martılar balıkçıların başında halkalar çiziyordu. Uzakta, sisin içinden adanın gri silueti belli belirsiz seçiliyordu.\n\nBu parçanın anlatımında aşağıdakilerden hangisi ağır basmaktadır?',
        {
            'A': 'Öyküleme',
            'B': 'Açıklama',
            'C': 'Tartışma',
            'D': 'Betimleme',
            'E': 'Söyleşi',
        },
        'D',
        'Parça limanı renk, koku, ses ve görüntü ayrıntılarıyla göz önünde canlandırıyor; betimleme ağır basıyor.',
    ),
    # düzey 2
    '0077': patch(
        'Kapıyı açtığında karşısında yıllardır görmediği okul arkadaşını buldu. Bir an ne diyeceğini bilemedi, sonra kenara çekilip onu içeri buyur etti. Mutfakta çay demlenirken eski fotoğrafları çıkardılar ve saatlerce o günleri konuştular. Gece yarısına doğru arkadaşı kalkarken yeniden görüşmek için birbirlerine söz verdiler.\n\nBu parçanın anlatımında aşağıdakilerden hangisi ağır basmaktadır?',
        {
            'A': 'Betimleme',
            'B': 'Açıklama',
            'C': 'Öyküleme',
            'D': 'Tartışma',
            'E': 'Söyleşi',
        },
        'C',
        'Parça zaman sırasına göre birbirini izleyen olayları anlatıyor; öyküleme ağır basıyor.',
    ),
    # düzey 3
    '0078': patch(
        'Bir kenti tanımak için müzelerini gezmek yetmez. Asıl kent; pazar yerlerinde, mahalle kahvelerinde, akşamüstü dolan otobüslerde yaşar. Rehber kitaplar size kentin yıllar önce nasıl olduğunu anlatır, ama bugün nasıl soluk aldığını ancak sokaklarında dolaşırsanız öğrenebilirsiniz.\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Kent, gündelik hayatında tanınır.',
            'B': 'Müzeler, kentlerin en ilgi çekici yerleridir.',
            'C': 'Rehber kitaplar güncel bilgi vermediği için gezilerde kullanılmamalıdır.',
            'D': 'Kent yaşamı en çok toplu taşıma araçlarında hissedilir.',
            'E': 'Kentlerin tarihî dokusu korunmalıdır.',
        },
        'A',
        'Yazar, kentin gerçek yüzünün müzelerde değil gündelik hayatın aktığı yerlerde görüleceğini vurguluyor.',
    ),
    # düzey 3
    '0079': patch(
        'Usta bir çömlekçinin elinde çamur, birkaç dakikada zarif bir vazoya dönüşür. İzleyene bu iş kolay görünür. Oysa o birkaç dakikanın ardında, yüzlerce kez çöken çamurlar ve yılların sabrı vardır. Kolay görünen her ustalık, görünmeyen uzun bir emeğin ürünüdür.\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Çömlekçilik kısa sürede öğrenilebilecek bir zanaattir.',
            'B': 'Ustalık emekle kazanılır.',
            'C': 'İzleyiciler ustaların işini çoğu zaman küçümser.',
            'D': 'Çamurla çalışmak hem sabır hem de güçlü eller gerektiren zorlu bir iştir.',
            'E': 'El sanatları günümüzde eskisi kadar ilgi görmemektedir.',
        },
        'B',
        'Son cümle ana düşünceyi açıkça veriyor: kolay görünen ustalık uzun bir emeğe dayanır.',
    ),
    # düzey 3
    '0080': patch(
        'Bir yapıtı eleştirirken amaç onu küçümsemek değil, okura yapıtın güçlü ve zayıf yanlarını gösterebilmektir. İyi bir eleştirmen kişisel beğenisini gerekçeleriyle ortaya koyar ve okuru kendi yargısına ulaşması için donatır. Gerekçesiz övgü de gerekçesiz yergi de okura bir şey kazandırmaz.\n\nBu parçada asıl vurgulanan düşünce aşağıdakilerden hangisidir?',
        {
            'A': 'Eleştiri, gerekçelere dayanarak okuru aydınlatmalıdır.',
            'B': 'Eleştirmenler yapıtların zayıf yanlarını öne çıkarmalıdır.',
            'C': 'Okurlar eleştirmenlerin beğenilerini benimsemelidir.',
            'D': 'Övgü, yergiden daha yararlı bir eleştiri biçimidir.',
            'E': 'Eleştirmen kişisel beğenisini yazısına yansıtmamalıdır.',
        },
        'A',
        'Parça eleştirinin değerini gerekçeye ve okura kazandırdığına bağlıyor; gerekçesiz övgü ve yergi reddediliyor.',
    ),
    # düzey 3
    '0081': patch(
        'Bildirim seslerinin gün boyu bölük pörçük ettiği bir zihin, derin düşünmeye zor geçer. Bir metni okurken ya da bir sorunu çözerken her kesinti, yeniden odaklanmak için ek bir çaba ister. Bu yüzden telefonu belirli saatlerde sessize almak, verimliliği artırmanın en ucuz yollarından biridir.\n\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
        {
            'A': 'Telefonlar insan zihnine kalıcı zarar verir.',
            'B': 'Okuma alışkanlığı teknolojiyle birlikte azalmaktadır.',
            'C': 'Sorun çözme becerisi, düzenli çalışmayla gelişir.',
            'D': 'Bildirim sesleri, kişinin uyku düzenini olumsuz etkileyebilir.',
            'E': 'Kesintileri azaltmak, odaklanmayı ve verimi artırır.',
        },
        'E',
        'Parça kesintilerin odaklanmayı zorlaştırdığını ve telefonu sessize almanın verimi artırdığını savunuyor.',
    ),
    # düzey 3
    '0082': patch(
        'Lale, Osmanlı kültüründe bir çiçekten öte, zevk ve inceliğin simgesiydi. 18. yüzyılın başlarında lale soğanları yüksek fiyatlarla alınıp satılır, bahçelerde lale şenlikleri düzenlenirdi. Çinilerden kumaşlara kadar pek çok süsleme sanatında da lale motifi sıkça kullanıldı.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Lale soğanları yüksek fiyatlarla alınıp satılmıştır.',
            'B': 'Bahçelerde lale şenlikleri düzenlendiği olmuştur.',
            'C': 'Lale motifi süslemede pek kullanılmamıştır.',
            'D': 'Lale, Osmanlı kültüründe incelik simgesi sayılmıştır.',
            'E': 'Lale motifine çinilerde de rastlanır.',
        },
        'C',
        'Parçada lale motifinin çinilerden kumaşlara kadar pek çok süsleme sanatında sıkça kullanıldığı belirtiliyor; tersi söylenemez.',
    ),
    # düzey 3
    '0083': patch(
        'Maraton koşucuları yarıştan önceki günlerde karbonhidrat ağırlıklı beslenir. Bunun amacı, kaslarda enerji kaynağı olarak kullanılan glikojen depolarını doldurmaktır. Yarışın son kilometrelerinde bu depolar tükendiğinde koşucu ani bir halsizlik yaşar; sporcular bu duruma "duvara çarpmak" der.\n\nBu parçaya göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Glikojen kaslarda enerji kaynağı olarak kullanılır.',
            'B': 'Depoların tükenmesi ani bir halsizliğe yol açabilir.',
            'C': 'Sporcular bu halsizliği adlandırmak için özel bir deyim kullanır.',
            'D': 'Koşucular yarıştan önce karbonhidratı azaltır.',
            'E': 'Beslenme, yarış performansını etkileyebilir.',
        },
        'D',
        'Parçaya göre koşucular yarış öncesinde karbonhidrat ağırlıklı beslenir; tüketimi azalttıkları söylenemez.',
    ),
    # düzey 3
    '0084': patch(
        "Çay, Türkiye'ye 20. yüzyılın başlarında Doğu Karadeniz'deki deneme üretimleriyle girdi. Bölgenin bol yağışlı iklimi ve asitli toprağı çay tarımına çok elverişliydi. Kısa sürede yaygınlaşan çay, bugün gündelik hayatın vazgeçilmez içeceği; misafir ağırlamanın ve sohbetin simgesi.\n\nBu parçada çayla ilgili aşağıdakilerden hangisine değinilmemiştir?",
        {
            'A': "Türkiye'ye geliş dönemine",
            'B': 'Yetiştiği bölgeye',
            'C': 'İhracattaki payına',
            'D': 'Yetişmesi için uygun iklim ve toprak koşullarına',
            'E': 'Toplumsal hayattaki yerine',
        },
        'C',
        'Parçada çayın geliş dönemi, bölgesi, iklim ve toprak koşulları ile sosyal hayattaki yeri anlatılıyor; ihracattan söz edilmiyor.',
    ),
    # düzey 3
    '0085': patch(
        '"Yazmaya başladığımda bir planım olmaz. Karakterlerimi bir yere bırakır, ne yapacaklarını izlerim. Kimi zaman beni şaşırtırlar; sonunu bildiğim bir hikâyeyi yazmak bana sıkıcı gelir."\n\nBu sözleri söyleyen bir yazar için aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Öykülerinin sonunu baştan kurgulayarak yazar.',
            'B': 'Yazarken karakterlerine hareket alanı tanır.',
            'C': 'Yazma sürecinde kendisi de şaşırtıcı gelişmelerle karşılaşır.',
            'D': 'Önceden belirlenmiş bir plana bağlı kalmaz.',
            'E': 'Sonu belli bir hikâyeyi yazmaktan pek hoşlanmaz.',
        },
        'A',
        'Yazar, sonunu bildiği hikâyeyi yazmanın kendisine sıkıcı geldiğini söylüyor; sonu baştan kurguladığı söylenemez.',
    ),
    # düzey 3
    '0086': patch(
        'Göç eden kuşlar yön bulmak için güneşin konumundan, yıldızlardan ve yerin manyetik alanından yararlanır. Araştırmacılar, bulutlu gecelerde bile yolunu şaşırmayan kuşların manyetik alanı algılayabildiğini gözlemlemiştir. Ancak şiddetli fırtınalar ve kentlerin yoğun ışıkları kuşların rotasından sapmasına yol açabilmektedir.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Kuşlar göçlerini gündüz saatleriyle sınırlar.',
            'B': 'Kent ışıkları kuşların yön bulmasını kolaylaştırır.',
            'C': 'Fırtınalar kuşları göç etmekten vazgeçirir.',
            'D': 'Kuşlar yön bulurken birden çok ipucu kullanır.',
            'E': 'Bulutlu havalarda kuşlar göç etmez.',
        },
        'D',
        'Parçada güneş, yıldızlar ve manyetik alan olmak üzere birden çok ipucu sayılıyor. Diğer seçenekler parçayla çelişiyor ya da parçada dayanağı yok.',
    ),
    # düzey 3
    '0087': patch(
        'Fiyatı düşen bir ürüne olan talebin artması beklenir. Ancak bazı lüks ürünlerde durum farklıdır: Fiyat düştüğünde ürün ayrıcalıklı olma niteliğini yitirdiği için bazı tüketiciler ondan uzaklaşır. Bu ürünlerde yüksek fiyat, tüketiciye bir statü göstergesi olarak çekici gelir.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Lüks ürünlerin fiyatı düşürülmez.',
            'B': 'Bazı ürünlerde fiyat, ürünün anlamının bir parçasıdır.',
            'C': 'Fiyat düşüşü her ürünün talebini artırır.',
            'D': 'Tüketiciler ucuz ürünleri tercih etmez.',
            'E': 'Statü göstergesi olan ürünlerin kalitesi daha yüksektir.',
        },
        'B',
        'Lüks ürünlerde yüksek fiyatın bir statü göstergesi olarak çekici gelmesi, fiyatın ürünün anlamının parçası olduğunu gösteriyor.',
    ),
    # düzey 3
    '0088': patch(
        'Antik çağda yazı, kil tabletlere sivri uçlu çubuklarla bastırılarak yazılırdı. Tabletler fırınlandığında binlerce yıl dayanabiliyordu. Bu sayede bugün o dönemin ticari anlaşmalarını, vergi kayıtlarını ve hatta öğrencilerin yazı alıştırmalarını okuyabiliyoruz.\n\nBu parçadan aşağıdakilerin hangisi çıkarılabilir?',
        {
            'A': 'Antik çağda yazı bilenlerin sayısı çok fazlaydı.',
            'B': 'Kil tabletler devlet kayıtlarıyla sınırlı kalmıştır.',
            'C': 'Fırınlanmayan tabletler daha uzun dayanmıştır.',
            'D': 'Antik çağda vergi toplanmamıştır.',
            'E': 'Yazı malzemesi, kayıtların korunmasını etkilemiştir.',
        },
        'E',
        'Fırınlanan kil tabletlerin binlerce yıl dayanması sayesinde kayıtların bugün okunabildiği belirtiliyor.',
    ),
    # düzey 3
    '0089': patch(
        'Bir ülkenin yollarına, köprülerine ve limanlarına yapılan yatırımlar ilk bakışta yalnızca ulaşımı kolaylaştırır gibi görünür. Oysa iyi bir yol, köydeki üreticinin ürününü kente daha ucuza ulaştırmasını, bir fabrikanın hammaddeye daha hızlı erişmesini sağlar. ----\n\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Köprü yapımında kullanılan malzemeler her geçen yıl pahalanmaktadır.',
            'B': 'Kentlerde trafik sıkışıklığı giderek artmaktadır.',
            'C': 'Bu yüzden altyapı yatırımları, ekonominin bütününe yayılan bir etki yaratır.',
            'D': 'Limanlar deniz ticaretinin en eski yapılarındandır.',
            'E': 'Köylerde üretim yapan kişi sayısı azalmaktadır.',
        },
        'C',
        'Parça yol yatırımlarının etkisinin ulaşımla sınırlı kalmadığını anlatıyor; sona bu düşünceyi bağlayan sonuç cümlesi gelmelidir.',
    ),
    # düzey 3
    '0090': patch(
        '---- Kimimiz sabah erken saatlerde daha dinç ve yaratıcıyken kimimiz ancak akşam saatlerinde odaklanabiliriz. Bu farkı bilmek, zor işleri zihnin en açık olduğu saatlere bırakarak gün boyu daha verimli olmamızı sağlar.\n\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Erken kalkmak başarının ilk koşuludur.',
            'B': 'Herkesin en verimli olduğu saatler aynı değildir.',
            'C': 'Akşam saatlerinde yapılan işler genellikle hatalı olur.',
            'D': 'Düzenli uyku, sağlıklı yaşamın temelidir.',
            'E': 'Zor işleri ertelemek verimliliği düşürür.',
        },
        'B',
        'Sonraki cümleler kişiden kişiye değişen verimli saatleri anlatıyor; parçaya bu genel yargıyla başlanmalıdır.',
    ),
    # düzey 3
    '0091': patch(
        'Bir sözlük, sözcüklerin anlamlarını sıralayan bir kitaptan ibaret değildir. ---- Örneğin bir sözcüğün eski baskılarda yer alıp yenilerinde çıkarılması, o sözcüğün gündelik hayattan nasıl çekildiğini gösterir.\n\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
        {
            'A': 'Sözlükler genellikle alfabetik sıraya göre düzenlenir.',
            'B': 'İyi bir sözlük okullarda ders aracı olarak kullanılmalıdır.',
            'C': 'Sözcüklerin kökenini araştırmak uzmanlık gerektiren bir çalışmadır.',
            'D': 'Her yeni baskısı, dilin zaman içindeki değişimine de tanıklık eder.',
            'E': 'Elektronik sözlükler basılı sözlüklerin yerini almıştır.',
        },
        'D',
        "Boşluktan sonraki 'Örneğin' cümlesi sözlük baskılarındaki değişimin dilin değişimini gösterdiğini örnekliyor; boşluğa bu yargı gelmelidir.",
    ),
    # düzey 3
    '0092': patch(
        'Bir kentin hafızası binalarında saklıdır. Yıkılan her eski yapıyla birlikte, o yapının çevresinde örülmüş anılar, alışkanlıklar ve ilişkiler de kaybolur.\n\nBu paragraf aşağıdakilerden hangisiyle sürdürülebilir?',
        {
            'A': 'Yeni binaların depreme dayanıklı olması büyük önem taşır.',
            'B': 'Kentlerde yeşil alanların payı giderek azalmaktadır.',
            'C': 'Mimarlık fakülteleri her yıl çok sayıda öğrenci mezun etmektedir.',
            'D': 'Eski binaların bakımı yüksek maliyetlidir.',
            'E': 'Bu nedenle eski yapıları korumak, kentin belleğini korumaktır.',
        },
        'E',
        'Parça eski yapılarla birlikte anıların da kaybolduğunu söylüyor; bu düşünceyi koruma sonucuna bağlayan cümle akışa uygundur.',
    ),
    # düzey 3
    '0093': patch(
        '"Bir şiiri yazdıktan sonra çekmeceye koyar, aylar sonra yeniden okurum. O zaman artık şiirin yazarı değil, okuru olurum; fazla sözcükleri ancak o gözle görebilirim."\n\nBu sözleri söyleyen şair için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Şiirlerini zaman geçtikten sonra eleştirel bir gözle düzeltir.',
            'B': 'Şiirlerini yazdığı gün yayımlamayı tercih eder.',
            'C': 'Okurların eleştirilerini önemsemez.',
            'D': 'Uzun şiirleri kısa şiirlere yeğler.',
            'E': 'Şiirlerinde sözcük seçimine özen göstermez.',
        },
        'A',
        'Şair, şiirini aylar sonra bir okur gözüyle okuyup fazla sözcükleri ayıkladığını söylüyor.',
    ),
    # düzey 3
    '0094': patch(
        '"Çocuklar için yazmak, büyükler için yazmaktan daha zordur. Çocuk okur sıkıldığında kitabı bırakır; nezaketen sayfa çevirmez."\n\nBu sözleri söyleyen yazar için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Büyükler için yazmayı daha zor bulur.',
            'B': 'Çocukların kitap okumadığını düşünür.',
            'C': 'İlgiyi canlı tutmayı önemser.',
            'D': 'Çocuk kitaplarının kısa olması gerektiğini savunur.',
            'E': 'Yetişkin okurların sabırsız olduğunu düşünür.',
        },
        'C',
        'Yazar, sıkılan çocuk okurun kitabı bıraktığını söyleyerek ilgiyi canlı tutmanın önemine dikkat çekiyor.',
    ),
    # düzey 3
    '0095': patch(
        "(I) Kapadokya'daki peri bacaları, volkanik tüflerin rüzgâr ve yağmurla aşınmasıyla oluşmuştur. (II) Bölgede kayalara oyulmuş çok sayıda kilise ve yerleşim yeri bulunur. (III) Gün doğumunda gökyüzünü dolduran balonlar, insanın içini ısıtan eşsiz bir manzara oluşturur. (IV) Göreme ve çevresi, 1985 yılında UNESCO Dünya Mirası Listesi'ne alınmıştır. (V) Yaz aylarında bölgeyi ziyaret eden turist sayısı artar.\n\nBu parçadaki numaralanmış cümlelerden hangisinde öznel bir yargı vardır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'C',
        "'İnsanın içini ısıtan eşsiz bir manzara' ifadesi kişisel duygu ve değerlendirme içerir; III. cümle özneldir. Diğerleri doğrulanabilir bilgilerdir.",
    ),
    # düzey 3
    '0096': patch(
        "(I) Bu roman, son yılların en sürükleyici eserlerinden biri. (II) Yazarın akıcı dili, okuru ilk sayfadan yakalıyor. (III) Karakterlerin iç dünyaları o kadar ustaca işlenmiş ki her biri gerçek bir insan gibi. (IV) Roman, 1950'li yıllarda bir Ege kasabasında geçiyor. (V) Bence kitabın sonu, okurların çoğunu derinden etkileyecek.\n\nBu parçadaki numaralanmış cümlelerden hangisinde nesnel bir yargı vardır?",
        {
            'A': 'I',
            'B': 'II',
            'C': 'III',
            'D': 'IV',
            'E': 'V',
        },
        'D',
        'Romanın geçtiği zaman ve yer doğrulanabilir bir bilgidir; IV. cümle nesneldir. Diğer cümleler kişisel beğeni ve tahmin içerir.',
    ),
    # düzey 2
    '0097': patch(
        'Dedem, bahçedeki **yaşlı** cevizin altında oturmayı severdi. **Akşamları** oraya bir sandalye taşır, **uzun uzun** gökyüzünü seyrederdi. Bazen **bize** eski günlerden hikâyeler anlatır, sesi **yavaş yavaş** kısılırdı.\n\nBu parçadaki kalın yazılmış sözcüklerden hangisi sıfat olarak kullanılmıştır?',
        {
            'A': 'Akşamları',
            'B': 'uzun uzun',
            'C': 'bize',
            'D': 'yavaş yavaş',
            'E': 'yaşlı',
        },
        'E',
        "'yaşlı' sözcüğü 'ceviz' adını nitelediği için sıfattır. 'Akşamları', 'uzun uzun' ve 'yavaş yavaş' eylemi niteleyen zarflar, 'bize' ise zamirdir.",
    ),
    # düzey 2
    '0098': patch(
        'Kardeşim yeni işine **sıcak** bir sabah başladı. İlk gün **ağır** dosyaları arşive taşıdı. Öğle yemeğini iş yerinin **geniş** bahçesinde yedi. Başta çekingen davransa da akşama doğru iş arkadaşlarıyla arasındaki **buzlar** eridi. Eve **yorgun** ama mutlu döndü.\n\nBu parçadaki kalın yazılmış sözcüklerden hangisi mecaz anlamıyla kullanılmıştır?',
        {
            'A': 'sıcak',
            'B': 'ağır',
            'C': 'geniş',
            'D': 'buzlar',
            'E': 'yorgun',
        },
        'D',
        "'buzların erimesi' kişiler arasındaki soğukluğun ve çekingenliğin ortadan kalkması anlamında mecazdır; diğer sözcükler gerçek anlamlarıyla kullanılmıştır.",
    ),
    # düzey 2
    '0099': patch(
        'Pazardan şunları aldık ( ) domates, biber, salatalık ve biraz peynir ( ) Eve dönerken annem sordu ( ) "Ekmek almayı unutmadınız, değil mi ( )"\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(:) (.) (:) (?)',
            'B': '(;) (.) (,) (?)',
            'C': '(:) (,) (:) (.)',
            'D': '(,) (.) (:) (!)',
            'E': '(:) (...) (;) (?)',
        },
        'A',
        'Açıklama ve sıralama öncesinde iki nokta, cümle sonunda nokta, alıntı öncesinde iki nokta, soru cümlesinin sonunda soru işareti kullanılır.',
    ),
    # düzey 2
    '0100': patch(
        "Toplantı saat 14 ( ) 30'da başladı ( ) Dr ( ) Ayşe Demir sunumunda üç konuya değindi ( ) maliyet, kalite ve teslim süresi ( )\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?",
        {
            'A': '(:) (.) (.) (:) (.)',
            'B': '(.) (.) (.) (:) (.)',
            'C': '(.) (,) (.) (;) (.)',
            'D': '(.) (.) (,) (:) (...)',
            'E': '(,) (.) (.) (:) (.)',
        },
        'B',
        "Saat ile dakika arasına nokta, cümle sonuna nokta, kısaltma olan 'Dr'den sonra nokta, açıklama yapılacak sıralamadan önce iki nokta ve cümle sonuna nokta konur.",
    ),
}

PATCHES = {ONEK + k: v for k, v in _PATCHES.items()}


def apply_or_check(path, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    fark = []
    for qid, alanlar in PATCHES.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadi: {path}::{qid}")
        for alan, beklenen in alanlar.items():
            if q.get(alan) != beklenen:
                fark.append(f"{path}::{qid}.{alan}")
                if write:
                    q[alan] = beklenen
        if write:
            if len(set(q["options"].values())) != 5:
                raise SystemExit(f"Secenek cakismasi: {path}::{qid}")
            if q["answer"] not in q["options"]:
                raise SystemExit(f"Cevap secenekte yok: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return fark


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    fark = []
    for path in (ROOT / RELATIVE_PATH, APP_ROOT / RELATIVE_PATH):
        fark.extend(apply_or_check(path, args.write))
    if args.check and fark:
        print("Eslesmeyen alanlar:")
        for f in fark[:20]:
            print(f"- {f}")
        return 1
    print(f"1 paket / {len(PATCHES)} soru ('Türkçe — Paragraf (yeni konu)') iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
