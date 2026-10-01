#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkçe — Paragraf (yeni konu) — gerçek sınav profiline göre yazıldı.

YENİ KONU. 2021-2026'nın 16 kitapçığında Türkçe sorularının %38'i paragraf sorusu, havuzda karşılığı yoktu. 60 özgün paragraf: düşüncenin akışını bozan cümle, paragraf sıralama (ilk/üçüncü/dördüncü cümle), yer değiştirme, düşünceyi geliştirme yolları (tek ve ikili), anlatım biçimi, ana düşünce/vurgulanan düşünce, çıkarılabilir/söylenemez, paragraf tamamlama (baş, orta, son), nesnel/öznel yargı, paragraf içi noktalama ve kalın sözcüğün anlamı/türü. Numaralı şıklar (I-V, 'I ve II') gerçek sınavdaki gibi sıralı; harf doğru şıkkın sırasından gelir, kalan 45 soruda harf dengelenir. Serbest şıklarda doğru şık en uzun 6/45, en kısa 7/45.
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
