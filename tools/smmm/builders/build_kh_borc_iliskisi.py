#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Hukuk — Borç İlişkisi konu havuzu (3×20).

17.07.2026 tarihinde mevzuat.gov.tr'den alınan güncel 6098 sayılı TBK metni
esas alınmıştır. Sözleşmenin kurulması, ifa ve haksız fiil ayrı konu paketlerine
bırakılmış; bu paket sona erme, zamanaşımı, teselsül ve alacak/borç devrine
odaklanmıştır.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors, "focus_distractors": distractors[1:] + distractors[:1],
        "why": why, "focus_why": focus_why, "ref": ref, "difficulty": difficulty,
    }


RULES = [
    # 1
    r(
        "A, üçüncü kişi C'nin belirli işi yapacağını B'ye karşı üstlenmiştir. C işi yapmayınca B zarara uğramıştır. A'nın sorumluluğu bakımından hangisi doğrudur?",
        "Üçüncü kişinin fiilini başkasına karşı üstlenen kişi, üstlenilen fiil gerçekleşmezse hangi yükümlülük altına girer?",
        "Üstlenen, üçüncü kişinin fiilinin gerçekleşmemesinden doğan zararı gidermelidir",
        ["Üstlenen yalnız üçüncü kişiye sözlü uyarı yapmakla bütün sorumluluktan kurtulur", "Zarar gören hiçbir koşulda üstlenene başvuramaz ve yalnız üçüncü kişiyi izler", "Üçüncü kişinin fiili gerçekleşmese de üstlenen daima borçsuz kabul edilir", "Üstlenme, üçüncü kişiyi kendiliğinden sözleşmenin tek borçlusu hâline getirir"],
        "TBK m.128 uyarınca üçüncü kişinin fiilini üstlenen, fiilin gerçekleşmemesinden doğan zararı gidermekle yükümlüdür. Üçüncü kişi doğrudan bu sözle borçlu hâle gelmez.",
        "Bu kurum bir sonuç taahhüdüdür. Üstlenilen üçüncü kişi davranışı gerçekleşmezse zarar, fiili üstlenmiş olan kişiden istenebilir.",
        "6098 sayılı TBK m.128", "medium",
    ),
    # 2
    r(
        "A ile B arasındaki sözleşmede edimin üçüncü kişi C'ye ifa edilmesi kararlaştırılmıştır. Tarafların amacı C'ye doğrudan talep hakkı tanımaktadır. C bu hakkı kullanacağını B'ye bildirmiştir. Hangisi doğrudur?",
        "Tam üçüncü kişi yararına sözleşmede lehtar hakkını kullanacağını borçluya bildirdikten sonra vaat ettirenin yetkisi nasıl sınırlanır?",
        "Vaat ettiren artık borçluyu ibra edemez ve borcun kapsamını değiştiremez",
        ["Vaat ettiren bildirime rağmen borcu tek taraflı olarak her zaman ortadan kaldırabilir", "Lehtarın bildirimi borcu sona erdirir ve edimin ifasını kesin olarak yasaklar", "Borçlu bildirimle sözleşmenin bütün haklarını kendiliğinden devralmış olur", "Lehtar hakkını kullanınca vaat ettiren bütün şirket borçlarından sorumlu hâle gelir"],
        "TBK m.129/2'de üçüncü kişi doğrudan talep hakkını kullanacağını borçluya bildirdikten sonra vaat ettiren borçluyu ibra edemez, borcun nitelik ve kapsamını değiştiremez.",
        "Lehtarın hakkı kesinleştiğinde ilk sözleşme tarafı bu hakkı zayıflatamaz. Bildirim, üçüncü kişinin kazanımını vaat ettirenin sonraki tasarruflarına karşı korur.",
        "6098 sayılı TBK m.129/2", "hard",
    ),
    # 3
    r(
        "Asıl borç ifayla sona ermiş; sözleşmede işlemiş faiz ve ceza koşulunun ayrıca korunacağına ilişkin kayıt veya bildirim bulunmamaktadır. Bağlı hakların durumu nedir?",
        "Asıl borç ifa veya başka sebeple sona erdiğinde rehin, kefalet, faiz ve ceza koşulu gibi bağlı hakların temel akıbeti nedir?",
        "Asıl borca bağlı rehin, kefalet, faiz ve ceza koşulu da kural olarak sona erer",
        ["Bağlı hakların tamamı asıl borçtan bağımsız biçimde süresiz devam eder", "Asıl borç sona erince yalnız borçlunun adı değişir ve bütün güvenceler artar", "Rehin ve kefalet kendiliğinden yeni bir asıl borç oluşturur", "Faiz borcu asıl alacağın sona ermesiyle zorunlu olarak iki katına çıkar"],
        "TBK m.131 asıl borç sona erdiğinde rehin, kefalet, faiz ve ceza koşulu gibi bağlı hakları da kural olarak sona erdirir. İşlemiş faiz veya cezanın saklı tutulması istisna oluşturabilir.",
        "Fer'î haklar asıl borcu izler. Asıl borç ortadan kalkınca özel hüküm veya saklı tutma bulunmadıkça bağlı güvence ve yan borçların hukuki temeli de sona erer.",
        "6098 sayılı TBK m.131", "medium",
    ),
    # 4
    r(
        "Yazılı şekle tabi sözleşmeden doğan borcu taraflar sonradan ibra etmek istemektedir. İbra sözleşmesini sözlü kurmuşlardır. TBK m.132 bakımından hangisi doğrudur?",
        "Borcu doğuran işlem belirli şekle bağlı olsa bile ibra sözleşmesinin şekli hakkında temel kural hangisidir?",
        "Taraflar borcu şekle bağlı olmadan tamamen veya kısmen ibra edebilir",
        ["İbra her durumda borcu doğuran işlemin iki kat ağır şekline bağlıdır", "İbra yalnız mahkeme kararıyla ve borcun tamamı için yapılabilir", "Şekle tabi borç hiçbir anlaşmayla tamamen veya kısmen sona erdirilemez", "İbra sadece borçlunun tek taraflı iç iradesiyle ve alacaklı olmadan kurulur"],
        "TBK m.132, borcu doğuran işlem kanunen veya taraf iradesiyle şekle bağlı olsa bile borcun şekle bağlı olmayan ibra sözleşmesiyle tamamen veya kısmen kaldırılmasına izin verir.",
        "İbra, borcu doğuran işlemin şekline tabi değildir. Ancak tek taraflı vazgeçme değil, alacaklı ile borçlu arasında borcu kaldıran bir sözleşmedir.",
        "6098 sayılı TBK m.132", "medium",
    ),
    # 5
    r(
        "Mevcut borç için yeni bir senet düzenlenmiş ancak taraflar eski borcu sona erdirme iradesini açıkça ortaya koymamıştır. Yenileme bakımından hangisi doğrudur?",
        "Mevcut borcun yeni bir borçla sona erdirilerek yenilenmesi için gereken temel unsur nedir?",
        "Tarafların mevcut borcu sona erdirme yönündeki açık yenileme iradesi gerekir",
        ["Yeni bir senet düzenlenmesi tek başına ve her durumda eski borcu sona erdirir", "Borçlunun içinden yenilemeyi düşünmesi alacaklı bilmese de yeterlidir", "Yenileme yalnız ticaret sicili müdürünün tek taraflı kararıyla gerçekleşir", "Her kısmi ödeme eski borcu kendiliğinden yeni bir borca dönüştürür"],
        "TBK m.133'e göre yenileme ancak tarafların açık iradesiyle olur. Yeni senet, kambiyo taahhüdü veya kefalet senedi tek başına yenileme sayılmaz.",
        "Yenileme karine değildir. Eski borcun yerine yeni borcun geçirilmesi, tarafların bu sona erdirme sonucunu açıkça istemesine bağlıdır.",
        "6098 sayılı TBK m.133", "medium",
    ),
    # 6
    r(
        "Bir miras işlemi sonucunda aynı kişi hem belirli alacağın alacaklısı hem borçlusu hâline gelmiştir. Üçüncü kişilerin önceden mevcut hakları da yoktur. Borcun durumu nedir?",
        "Alacaklı ve borçlu sıfatlarının aynı kişide birleşmesi borç üzerinde hangi temel sonucu doğurur?",
        "Alacaklı ve borçlu sıfatları birleşince borç kural olarak sona erer",
        ["Sıfatların birleşmesi borcu zorunlu olarak iki kat artırır", "Birleşme yalnız alacaklının değişmesini sağlar ve borç aynen üçüncü kişiye geçer", "Aynı kişi kendisine karşı süresiz icra takibi yapmak zorunda kalır", "Birleşme borcu hiçbir şekilde etkilemez ve yeni kefalet doğurur"],
        "TBK m.135'e göre alacaklı ve borçlu sıfatlarının aynı kişide birleşmesi borcu sona erdirir; üçüncü kişilerin alacak üzerindeki önceden mevcut hakları saklıdır.",
        "Bir kişi aynı edimin hem talep edeni hem yükümlüsü olamaz. Bu sıfat birleşmesi borcu söndürür, fakat üçüncü kişilerin daha önce kazanılmış haklarını ortadan kaldırmaz.",
        "6098 sayılı TBK m.135", "easy",
    ),
    # 7
    r(
        "Borcun ifası, borçlunun sorumlu tutulamayacağı sonradan ortaya çıkan bir sebeple tamamen imkânsızlaşmıştır. Borçlunun bildirim yükümünü de ihlal etmediği varsayılırsa hangisi doğrudur?",
        "Borçlunun sorumlu olmadığı sebeple sonradan ortaya çıkan tam ifa imkânsızlığının borca temel etkisi nedir?",
        "Borçlunun sorumlu tutulamadığı imkânsızlıkta aynen ifa borcu sona erer",
        ["Borç imkânsızlığa rağmen her durumda aynen ifa edilmek üzere süresiz devam eder", "İmkânsızlık yalnız alacaklıyı borçlu hâline getirir ve eski borcu artırır", "Borçlu kusursuz olsa da mutlaka edimin iki katını aynen teslim etmelidir", "İmkânsızlık yalnız sözleşmenin adını değiştirir ve borca hiçbir etki yapmaz"],
        "TBK m.136/1, ifanın borçlunun sorumlu tutulamayacağı sebeple imkânsızlaşması hâlinde borcu sona erdirir. Bildirmeme ve zararı önlememe ayrı tazminat sonucu doğurabilir.",
        "Sonraki imkânsızlık borçluya yüklenemiyorsa aynen ifa borcu sürdürülemez. Karşılıklı sözleşmedeki iade sonuçları ayrıca sebepsiz zenginleşme hükümlerine bağlanır.",
        "6098 sayılı TBK m.136", "medium",
    ),
    # 8
    r(
        "Borcun yalnız bir bölümü borçlunun sorumlu tutulamayacağı sebeple imkânsızlaşmış; kalan bölüm bağımsız olarak ifa edilebilir durumdadır. Kural olarak sonuç nedir?",
        "Borçlunun sorumlu olmadığı kısmi ifa imkânsızlığında borcun hangi bölümü sona erer?",
        "Borçlu kural olarak yalnız imkânsızlaşan kısım yönünden borçtan kurtulur",
        ["Borcun tamamı her durumda sona erer ve kalan bölümün ifası yasaklanır", "Kısmi imkânsızlık borç miktarını kendiliğinden iki katına çıkarır", "İmkânsızlaşan bölüm aynen ifa edilmiş sayılır ve alacaklı borçlu olur", "Borcun hiçbir kısmı etkilenmez ve imkânsız bölüm süresiz bekletilir"],
        "TBK m.137 kısmi imkânsızlıkta borçluyu kural olarak yalnız imkânsızlaşan kısımdan kurtarır. Tarafların bu sözleşmeyi hiç yapmayacağı açıksa tamamı sona erebilir.",
        "Kısmi imkânsızlıkta bölünebilirlik esastır. Mümkün kalan bölüm korunur; fakat imkânsız kısmın sözleşme iradesi için belirleyici olduğu durumda tam sona erme gündeme gelir.",
        "6098 sayılı TBK m.137", "medium",
    ),
    # 9
    r(
        "Sözleşmeden sonra öngörülemez olağanüstü durum borçludan kaynaklanmadan ortaya çıkmış, dengeyi dürüstlük kuralına aykırı derecede bozmuş ve borç henüz ifa edilmemiştir. Borçlu öncelikle ne isteyebilir?",
        "Aşırı ifa güçlüğünün kanuni koşulları oluştuğunda borçlunun hâkimden öncelikle talep edebileceği yol hangisidir?",
        "Borçlu sözleşmenin yeni koşullara uyarlanmasını hâkimden isteyebilir",
        ["Borçlu hiçbir koşul aranmadan karşı tarafın bütün malvarlığını devralabilir", "Sözleşme kendiliğinden ceza sözleşmesine dönüşür ve borç iki katına çıkar", "Borçlu yalnız ticaret siciline bildirim yaparak bütün edimleri ifa etmiş sayılır", "Olağanüstü durum borçluya tek taraflı yeni bir alacaklı seçme hakkı verir"],
        "TBK m.138 koşulları oluştuğunda borçlu önce uyarlama, bu mümkün değilse dönme; sürekli edimli sözleşmede kural olarak fesih isteyebilir.",
        "Aşırı ifa güçlüğü borcu kendiliğinden silmez. Sözleşme dengesinin yargısal uyarlamayla kurulması öncelikli çözümdür.",
        "6098 sayılı TBK m.138", "hard",
    ),
    # 10
    r(
        "A ile B birbirine karşı muaccel para borçlarına sahiptir. Borçlar aynı türden ve karşılıklıdır. Takas koşulları bakımından hangisi doğrudur?",
        "İki kişinin alacaklarını takas edebilmesi için TBK m.139'da aranan temel koşul grubu hangisidir?",
        "Karşılıklı, özdeş türde ve muaccel borçlar takasa elverişlidir",
        ["Borçların farklı kişilere ait, vadesiz ve farklı türde olması zorunludur", "Takas için alacakların mutlaka aynı sözleşmeden doğması gerekir", "Takas yalnız iki borç da zamanaşımına uğradıktan sonra kendiliğinden olur", "Para borçları hiçbir durumda birbirleriyle takas edilemez"],
        "TBK m.139, iki kişinin karşılıklı para veya özdeş diğer edimleri birbirine borçlu ve her iki borcun muaccel olması hâlinde takasa izin verir.",
        "Takas aynı sözleşmeden doğmayı gerektirmez. Karşılıklılık, edimlerin özdeşliği ve muacceliyet temel koşullardır.",
        "6098 sayılı TBK m.139", "medium",
    ),
    # 11
    r(
        "Takas koşulları gerçekleşmiş olmasına rağmen borçlu alacaklıya takas iradesini bildirmemiştir. Borcun kendiliğinden sona erdiğini savunmaktadır. Hangisi doğrudur?",
        "Takasın gerçekleşmesi için borçlunun yerine getirmesi gereken işlem aşağıdakilerden hangisidir?",
        "Takasın sonuç doğurması için borçlu iradesini alacaklıya açıkça bildirmelidir",
        ["Borçlu hiçbir açıklama yapmadan takasın mahkemece resen uygulanmasını beklemelidir", "Takas için borçlunun yalnız kendi defterine gizli bir not yazması yeterlidir", "Borçlu takas yerine bütün alacağını üçüncü kişiye bağışlamak zorundadır", "Takas iradesi yalnız ticaret sicilinde şirket kuruluşu olarak tescil edilir"],
        "TBK m.143'e göre takas ancak borçlunun takas iradesini alacaklıya bildirmesiyle gerçekleşir; borçlar daha az olan tutar ölçüsünde sona erer.",
        "Koşulların varlığı takas yetkisi verir, fakat sona erme sonucu bildirimle doğar. Hâkim taraf iradesi olmadan takası kendiliğinden uygulamaz.",
        "6098 sayılı TBK m.143", "easy",
    ),
    # 12
    r(
        "Kanunda başka süre öngörülmeyen bir alacak için taraflar zamanaşımı süresini araştırmaktadır. Genel zamanaşımı süresi bakımından hangisi doğrudur?",
        "TBK'da aksine özel hüküm bulunmadığında alacaklara uygulanan genel zamanaşımı süresi kaç yıldır?",
        "Aksine hüküm yoksa alacak on yıllık zamanaşımına tabidir",
        ["Aksine hüküm yoksa bütün alacaklar yalnız bir aylık zamanaşımına tabidir", "Bütün alacaklar süre olmaksızın kendiliğinden doğduğu gün sona erer", "Genel zamanaşımı her durumda iki yıl olup değiştirilemez", "Zamanaşımı yalnız borçlunun ölümünden elli yıl sonra işlemeye başlar"],
        "TBK m.146, Kanunda aksine bir hüküm bulunmadıkça her alacağın on yıllık zamanaşımına tabi olduğunu düzenler.",
        "On yıl genel süredir. Kira bedeli ve bazı dönemsel edimler gibi özel beş yıllık veya başka kanuni süreler saklıdır.",
        "6098 sayılı TBK m.146", "easy",
    ),
    # 13
    r(
        "Taraflar sözleşmede TBK'nın bu ayırımında belirlenen zamanaşımı süresini yirmi yıla çıkaran hüküm koymuştur. Bu hüküm nasıl değerlendirilir?",
        "TBK'nın zamanaşımı ayırımında belirlenen sürelerin taraf sözleşmesiyle değiştirilmesi mümkün müdür?",
        "Kanunda belirlenen zamanaşımı süreleri sözleşmeyle değiştirilemez",
        ["Taraflar bütün zamanaşımı sürelerini diledikleri gibi artırıp azaltabilir", "Zamanaşımı süresi yalnız borçlunun tek taraflı bildirimiyle sonsuz yapılabilir", "Süre değişikliği için alacaklının haberi olmadan gizli kayıt yeterlidir", "Tarafların her anlaşması kanuni süreyi kendiliğinden iki güne indirir"],
        "TBK m.148, bu ayırımda belirlenen zamanaşımı sürelerinin sözleşmeyle değiştirilemeyeceğini açıkça düzenler.",
        "Zamanaşımı sürelerinin kesinliği, borçlunun korunması kadar hukuki güvenliğe hizmet eder. Taraf iradesi kanuni süre sistemini değiştiremez.",
        "6098 sayılı TBK m.148", "easy",
    ),
    # 14
    r(
        "Bir alacak bugün muaccel olmuş ve özel başlangıç kuralı bulunmamaktadır. Zamanaşımının başlangıcı bakımından hangisi doğrudur?",
        "Genel kurala göre zamanaşımı hangi olayla işlemeye başlar?",
        "Zamanaşımı kural olarak alacağın muaccel olduğu anda işlemeye başlar",
        ["Zamanaşımı sözleşme görüşmelerinin ilk gününde her durumda başlar", "Süre yalnız alacaklı borcu bağışladıktan sonra işlemeye başlar", "Zamanaşımı borçlu şirket kurduğunda ve borç doğmadan önce başlar", "Alacağın muacceliyeti zamanaşımının başlangıcını hiçbir şekilde etkilemez"],
        "TBK m.149'a göre zamanaşımı alacağın muaccel olmasıyla başlar. Muacceliyet bildirime bağlıysa süre bildirimin yapılabileceği günden işler.",
        "Alacak talep edilebilir hâle gelmeden alacaklının hareketsizliği kural olarak süreyi başlatmaz. Başlangıç ölçütü muacceliyettir.",
        "6098 sayılı TBK m.149", "easy",
    ),
    # 15
    r(
        "Borçlu zamanaşımı savunması ileri sürmemiştir. Hâkim dosyadan sürenin dolduğunu görerek bunu kendiliğinden uygulamak istemektedir. Hangisi doğrudur?",
        "Zamanaşımının yargılamada dikkate alınması bakımından hâkimin yetkisi nasıl sınırlandırılmıştır?",
        "Zamanaşımı ileri sürülmedikçe hâkim bunu kendiliğinden dikkate alamaz",
        ["Hâkim zamanaşımını taraf iradesine bakmadan her davada resen uygular", "Zamanaşımı savunmasını yalnız tanık ileri sürebilir ve taraflar söyleyemez", "Sürenin dolması davayı kendiliğinden ceza davasına dönüştürür", "Zamanaşımı yalnız ticaret sicili müdürünün yazılı emriyle uygulanır"],
        "TBK m.161 zamanaşımının def'i niteliğini yansıtır: borçlu ileri sürmedikçe hâkim bunu kendiliğinden göz önüne alamaz.",
        "Sürenin dolması borcu kendiliğinden yok etmez; borçluya ifadan kaçınma savunması verir. Bu savunmanın yargılamada ileri sürülmesi gerekir.",
        "6098 sayılı TBK m.161", "medium",
    ),
    # 16
    r(
        "Üç borçludan her biri alacaklıya borcun tamamından sorumlu olmayı kabul ettiğini bildirmiştir. Kanunda başka engel yoktur. Borçluluk türü bakımından hangisi doğrudur?",
        "Birden çok borçlu arasında müteselsil borçluluğun taraf iradesiyle doğması için ne gerekir?",
        "Her borçlu alacaklıya borcun tamamından sorumlu olmayı kabul etmelidir",
        ["Borçlulardan yalnız biri diğerlerinin haberi olmadan alacaklı sıfatını edinmelidir", "Her borçlu yalnız kendi payından sorumlu olduğunu gizlice düşünmelidir", "Müteselsil borçluluk yalnız bütün borçlular şirket kurarsa doğabilir", "Taraf iradesiyle teselsül hiçbir zaman kurulamaz; yalnız mahkeme kurabilir"],
        "TBK m.162, borçluların her birinin alacaklıya borcun tamamından sorumlu olmayı kabul ettiğini bildirmesiyle teselsülü kurar; bildirim yoksa kanuni hâl gerekir.",
        "Teselsül borçlu aleyhine ağır sonuç doğurduğundan varsayılmaz. Açık kabul veya Kanunun özel hükmü bulunmalıdır.",
        "6098 sayılı TBK m.162", "medium",
    ),
    # 17
    r(
        "Alacaklı, müteselsil borcun tamamını yalnız borçlulardan birinden istemiştir. Seçilen borçlu, diğerlerine de aynı anda başvurulmadığı için talebin geçersiz olduğunu savunmaktadır. Hangisi doğrudur?",
        "Müteselsil borçlulukta alacaklı borcun tamamı veya bir kısmı için borçlulara nasıl başvurabilir?",
        "Alacaklı dilerse borçluların tümüne, dilerse yalnız birine başvurabilir",
        ["Alacaklı borcu yalnız bütün borçlulara eşit parçalara bölerek isteyebilir", "Alacaklı hiçbir borçludan borcun tamamını isteyemez ve dava açamaz", "Alacaklı yalnız en az ödeme gücü bulunan borçluya başvurmak zorundadır", "Alacaklı önce bütün borçluların yazılı iznini almadan talepte bulunamaz"],
        "TBK m.163 alacaklıya borcun tamamını veya kısmını borçluların hepsinden ya da yalnız birinden isteme seçeneği verir; sorumluluk tam ödeme gerçekleşene kadar sürer.",
        "Dış ilişkide her müteselsil borçlu borcun tamamıyla karşı karşıyadır. Alacaklı takip sırasını ve kapsamını seçebilir.",
        "6098 sayılı TBK m.163", "easy",
    ),
    # 18
    r(
        "Müteselsil borçlulardan biri, diğer borçlunun alacaklıyla arasındaki yalnız ona özgü kişisel savunmayı ileri sürmek istemektedir. Hangisi doğrudur?",
        "Müteselsil borçlu alacaklıya karşı hangi savunmaları ileri sürebilir?",
        "Kendi kişisel savunmalarıyla borcun sebep veya konusundan doğan ortak savunmaları",
        ["Diğer borçlunun yalnız kişiliğine özgü bütün savunmaları sınırsız biçimde", "Borçla ilgisi bulunmayan üçüncü kişilerin her türlü kişisel itirazını", "Hiçbir def'i veya itirazı ileri süremez; savunma hakkı tamamen kaldırılmıştır", "Yalnız ticaret sicilinde ilan edilen vergi borçlarına ilişkin savunmaları"],
        "TBK m.164, borçluya alacaklıyla kendi kişisel ilişkisinden ve müteselsil borcun sebep veya konusundan doğan def'i ve itirazları tanır; başkasına özgü kişisel savunma kullanılamaz.",
        "Ortak savunmalar borcun temelini etkilediği için bütün borçlulara açıktır. Kişisel savunmalar ise yalnız ait olduğu borçlu tarafından kullanılabilir.",
        "6098 sayılı TBK m.164", "medium",
    ),
    # 19
    r(
        "Müteselsil borçlulardan biri, alacaklıyla yaptığı işlemle diğer borçluların sorumluluğunu ağırlaştırmıştır. Kanun veya sözleşmede buna izin veren hüküm yoktur. Hangisi doğrudur?",
        "Müteselsil borçlulardan birinin bireysel davranışının diğer borçlulara etkisi bakımından kural nedir?",
        "Bir borçlu kendi davranışıyla diğer borçluların durumunu ağırlaştıramaz",
        ["Bir borçlu diğerlerinin borcunu tek taraflı ve sınırsız biçimde artırabilir", "Bireysel davranış bütün borçluları kendiliğinden alacaklı hâline getirir", "Borçlulardan biri diğerlerinin bütün savunmalarından kesin olarak vazgeçebilir", "Her borçlu başka borçlular adına yeni ceza koşulu koymak zorundadır"],
        "TBK m.165, Kanun veya sözleşmede aksi yoksa müteselsil borçlulardan birinin kendi davranışıyla diğerlerinin durumunu ağırlaştıramayacağını düzenler.",
        "Teselsül ortak sorumluluk yaratır fakat borçlulara birbirlerinin hukuki durumunu tek taraflı ağırlaştırma temsil yetkisi vermez.",
        "6098 sayılı TBK m.165", "easy",
    ),
    # 20
    r(
        "Müteselsil borçlulardan biri borcun yarısını alacaklıya ifa etmiştir. Diğer borçluların dış ilişkideki borcu bakımından hangisi doğrudur?",
        "Müteselsil borçlulardan birinin ifa veya takasla borcu sona erdirmesi diğer borçluları nasıl etkiler?",
        "Diğer borçlular da sona eren miktar oranında borçtan kurtulur",
        ["Diğer borçluların borcu ifa edilen miktar kadar kendiliğinden artar", "İfa yalnız ödeyen borçluyu etkiler ve alacaklı aynı tutarı tekrar isteyebilir", "Diğer borçlular alacaklı sıfatını kazanıp ifa edenden ödeme ister", "Kısmi ifa bütün borcu geçersiz kılar ve önceki ödemeyi yok sayar"],
        "TBK m.166/1, borçlulardan birinin ifa veya takasla sona erdirdiği miktar oranında diğer müteselsil borçluları da borçtan kurtarır.",
        "Alacaklı aynı borç miktarını birden çok kez tahsil edemez. Dış borcun azalması bütün borçluların alacaklıya karşı kalan sorumluluğunu aynı ölçüde azaltır.",
        "6098 sayılı TBK m.166/1", "easy",
    ),
    # 21
    r(
        "Üç müteselsil borçlu arasında farklı paylaşım kararlaştırılmamıştır. Borcun tamamını ödeyen borçlu, diğerlerinden paylarını istemektedir. İç ilişki bakımından hangisi doğrudur?",
        "Müteselsil borçluların iç ilişkisinde aksi anlaşılmadıkça borç payları ve rücu hakkı nasıl belirlenir?",
        "Borçlular eşit paylıdır; fazla ödeyen diğerlerine payları oranında rücu eder",
        ["Borcun tamamı yalnız ilk ödeme yapan üzerinde kalır ve rücu kesin olarak yasaktır", "İç ilişkide bütün paylar alacaklı tarafından rastgele belirlenir", "Fazla ödeme yapan diğer borçluların tüm malvarlığını kendiliğinden edinir", "Paylaşım yalnız borçlular farklı şehirlerdeyse ve mahkemece yapılabilir"],
        "TBK m.167, aksi kararlaştırılmadıkça veya ilişkinin niteliğinden başka sonuç çıkmadıkça eşit iç pay kabul eder ve fazla ödeyene diğerlerine payları oranında rücu hakkı verir.",
        "Teselsül dış ilişkide tam sorumluluk, iç ilişkide ise nihai paylaşım doğurur. Borcu taşıması gereken payı aşan borçlu fazlayı geri ister.",
        "6098 sayılı TBK m.167", "medium",
    ),
    # 22
    r(
        "Müteselsil borçlu borcun tamamını ifa etmiş ve diğerlerine rücu hakkı kazanmıştır. Alacaklının güvencelerinden yararlanmak istemektedir. Hangisi doğrudur?",
        "Diğer müteselsil borçlulara rücu hakkına sahip borçlunun alacaklının haklarına halefiyeti hangi ölçüdedir?",
        "Rücu hakkı sahibi, ifa ettiği miktar oranında alacaklının haklarına halef olur",
        ["İfa eden hiçbir hakka halef olamaz ve bütün güvenceler kendiliğinden yok olur", "Halefiyet ödenen miktarla ilgisiz biçimde bütün üçüncü kişi haklarını kapsar", "Borçlu yalnız alacaklının kişisel aile haklarına halef olabilir", "Halefiyet için diğer borçluların borcu iki kat artırması zorunludur"],
        "TBK m.168, diğerlerine rücu hakkı bulunan borçluyu ifa ettiği miktar oranında alacaklının haklarına halef kılar.",
        "Halefiyet rücu alacağını güçlendiren kanuni geçiştir. Kapsam, borçlunun yaptığı ifa ve rücu edebileceği miktarla sınırlıdır.",
        "6098 sayılı TBK m.168", "medium",
    ),
    # 23
    r(
        "Müteselsil alacaklılardan biri icra veya mahkemeye henüz başvurmamıştır. Borçlu, alacaklılardan seçtiği birine borcun tamamını ifa etmiştir. Sonuç nedir?",
        "Müteselsil alacaklılıkta borçlunun alacaklılardan birine yaptığı tam ifa diğer alacaklıları nasıl etkiler?",
        "Borçlu bir alacaklıya ifayla bütün alacaklılara karşı borçtan kurtulur",
        ["Borçlu aynı borcu her alacaklıya ayrı ayrı yeniden ödemek zorundadır", "İfa borcu sona erdirmez ve borçluyu müteselsil alacaklı hâline getirir", "Ödeme yalnız seçilmeyen alacaklıların payını iki kat artırır", "Borçlu ifa ettikten sonra bütün alacaklıların kişisel borçlarını üstlenir"],
        "TBK m.169'da borçlu, takip bildirimi yokken dilediği müteselsil alacaklıya ifa edebilir ve birine yaptığı ifayla bütününe karşı borçtan kurtulur.",
        "Müteselsil alacaklılık borçluyu aynı edimi tekrar tekrar ifaya zorlamaz. Alacaklıların iç paylaşımı, borçlunun dış ilişkide kurtulmasından ayrıdır.",
        "6098 sayılı TBK m.169", "medium",
    ),
    # 24
    r(
        "Alacaklı, sözleşme ve işin niteliğinde engel bulunmayan alacağını üçüncü kişiye devretmek istemektedir. Borçlu buna rıza göstermemiştir. Devrin mümkünlüğü bakımından hangisi doğrudur?",
        "Alacağın iradi devrinde, Kanun, sözleşme veya işin niteliği engel olmadıkça borçlunun rızası aranır mı?",
        "Alacaklı borçlunun rızası olmadan alacağını üçüncü kişiye devredebilir",
        ["Alacağın devri için borçlunun noter huzurunda mutlaka taraf olması gerekir", "Borçlu rıza vermezse alacak hiçbir koşulda kanun veya kararla devredilemez", "Devir yalnız borç tamamen ödendikten ve alacak sona erdikten sonra yapılabilir", "Alacaklı devir yerine borçlunun bütün sözleşmelerini üstlenmek zorundadır"],
        "TBK m.183, Kanun, sözleşme veya işin niteliği engel olmadıkça alacağın borçlunun rızası aranmaksızın üçüncü kişiye devrini kabul eder.",
        "Alacağın devrinde alacaklı değişir, borçlunun edimi aynı kalır. Bu nedenle borçlu rızası kural olarak kurucu unsur değildir.",
        "6098 sayılı TBK m.183", "easy",
    ),
    # 25
    r(
        "Alacaklı ile devralan, alacağın devri konusunda yalnız sözlü anlaşmıştır. Kanuni veya yargısal devir söz konusu değildir. İradi devrin geçerliliği bakımından hangisi doğrudur?",
        "Alacağın iradi devrinin geçerliliği hangi şekil şartına bağlıdır?",
        "İradi alacak devrinin geçerliliği yazılı şekilde yapılmasına bağlıdır",
        ["Alacağın devri yalnız sözlü yapılabilir ve yazılı anlaşma geçersizdir", "Devir her durumda resmî senet ve mahkeme kararı gerektirir", "Alacak devri hiçbir şekle uyulsa dahi hukuken mümkün değildir", "Geçerlilik yalnız borçlunun ticaret siciline kaydolmasına bağlıdır"],
        "TBK m.184/1 alacağın iradi devrinin geçerliliğini yazılı şekle bağlar. Buna karşılık alacağı devretme sözü şekle bağlı değildir.",
        "Yazılı şekil geçerlilik koşuludur. Borçlu rızası aranmasa da devreden ve devralanın devir anlaşması yazıya dökülmelidir.",
        "6098 sayılı TBK m.184", "easy",
    ),
    # 26
    r(
        "Borçlu, alacağın devredildiğini öğrendiği anda eski alacaklıya karşı bir savunmaya sahiptir. Devralan bu savunmanın kendisine karşı kullanılamayacağını ileri sürmektedir. Hangisi doğrudur?",
        "Alacağın devrini öğrenen borçlunun eski alacaklıya karşı mevcut savunmaları devralana karşı ileri sürme durumu nedir?",
        "Borçlu, devir anında mevcut savunmalarını devralana karşı da ileri sürebilir",
        ["Devir borçlunun bütün savunmalarını kendiliğinden ve geriye etkili olarak yok eder", "Borçlu yalnız devralanın kişisel borçlarıyla ilgisiz savunmaları kullanabilir", "Devralan alacağı her türlü itirazdan arınmış biçimde ve daima iki kat kazanır", "Borçlunun savunma hakkı yalnız alacağı devredenin yazılı izniyle doğar"],
        "TBK m.188, borçlunun devri öğrendiği sırada devredene karşı sahip olduğu savunmaları devralana karşı da ileri sürebileceğini düzenler.",
        "Alacağın devri borçlunun hukuki durumunu ağırlaştırmamalıdır. Devralan, alacağı mevcut savunmalarla birlikte kazanır.",
        "6098 sayılı TBK m.188", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Borcun sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İbra borcu tamamen veya kısmen sona erdirebilir.\n\nII. Yenileme için tarafların açık iradesi gerekir.\n\nIII. Alacaklı ve borçlu sıfatlarının birleşmesi kural olarak borcu sona erdirir.",
        "correct": "I, II ve III", "why": "TBK m.132 ibra, m.133 yenileme ve m.135 birleşme yoluyla sona ermeyi düzenler. Üç ifade de doğrudur.",
        "ref": "6098 sayılı TBK m.132, 133 ve 135", "difficulty": "medium",
    },
    {
        "stem": "Zamanaşımıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel süre, aksine hüküm yoksa on yıldır.\n\nII. Süre kural olarak alacağın muacceliyetiyle başlar.\n\nIII. Hâkim zamanaşımını borçlu ileri sürmese de resen uygular.",
        "correct": "I ve II", "why": "TBK m.146 ve 149 gereği I ve II doğrudur. TBK m.161 hâkimin zamanaşımını kendiliğinden dikkate alamayacağını düzenlediğinden III yanlıştır.",
        "ref": "6098 sayılı TBK m.146, 149 ve 161", "difficulty": "medium",
    },
    {
        "stem": "Müteselsil borçlulukla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Alacaklı borcun tamamını yalnız bir borçludan isteyebilir.\n\nII. Bir borçlu ifa ettiği ölçüde diğerlerini de dış borçtan kurtarır.\n\nIII. Borçlulardan biri diğerlerinin durumunu tek taraflı ağırlaştırabilir.",
        "correct": "I ve II", "why": "TBK m.163 ve 166 nedeniyle I ve II doğrudur. TBK m.165 kural olarak bir borçlunun diğerlerinin durumunu ağırlaştıramayacağını söyler; III yanlıştır.",
        "ref": "6098 sayılı TBK m.163, 165 ve 166", "difficulty": "medium",
    },
    {
        "stem": "Alacağın devriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İradi devir kural olarak borçlu rızası olmadan yapılabilir.\n\nII. İradi devrin geçerliliği yazılı şekle bağlıdır.\n\nIII. Devir borçlunun mevcut savunmalarını daima ortadan kaldırır.",
        "correct": "I ve II", "why": "TBK m.183 ve 184 gereği I ve II doğrudur. TBK m.188 borçlunun mevcut savunmalarını devralana karşı korur; III yanlıştır.",
        "ref": "6098 sayılı TBK m.183, 184 ve 188", "difficulty": "medium",
    },
    {
        "stem": "Borcun üstlenilmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dış üstlenme sözleşmesi borcu üstlenen ile alacaklı arasında kurulur.\n\nII. Alacaklının kabulü yalnız açık olabilir, örtülü kabul geçersizdir.\n\nIII. Üstlenilen borca ilişkin savunmalar yeni borçluya geçer.",
        "correct": "I ve III", "why": "TBK m.196 dış üstlenmeyi üstlenen ile alacaklı arasında kurduğundan I, TBK m.199 borca ilişkin savunmaları yeni borçluya geçirdiğinden III doğrudur. Kabul örtülü de olabilir; II yanlıştır.",
        "ref": "6098 sayılı TBK m.196 ve 199", "difficulty": "hard",
    },
    {
        "stem": "Borca katılmayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Katılan ile alacaklı arasında sözleşme kurulur.\n\nII. Katılan mevcut borçlunun yanında yer alır.\n\nIII. Katılan ile borçlu alacaklıya karşı müteselsilen sorumlu olur.",
        "correct": "I, II ve III", "why": "TBK m.201 borca katılmayı, mevcut borca borçlunun yanında katılan ile alacaklı arasında kurulan ve müteselsil sorumluluk doğuran sözleşme olarak tanımlar.",
        "ref": "6098 sayılı TBK m.201", "difficulty": "medium",
    },
    {
        "stem": "Sözleşmenin devriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Devredenin taraf sıfatı ile bütün hak ve borçları devralana geçer.\n\nII. Sözleşmede kalan taraf anlaşmanın tarafıdır veya önceden izin ya da sonradan onay verir.\n\nIII. Devrin geçerliliği devredilen sözleşmenin şeklinden tamamen bağımsızdır.",
        "correct": "I ve II", "why": "TBK m.205 gereği I ve II doğrudur. Sözleşme devrinin geçerliliği devredilen sözleşmenin şekline bağlı olduğundan III yanlıştır.",
        "ref": "6098 sayılı TBK m.205", "difficulty": "hard",
    },
    {
        "stem": "Müteselsil alacaklılıkla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Borçlu hiçbir alacaklıya seçim yaparak ifada bulunamaz.\n\nII. Bir alacaklıya yapılan ifa bütün alacaklılara karşı borcu sona erdirebilir.\n\nIII. Fazla pay alan alacaklı fazlayı payını alamayan diğer alacaklılara ödemelidir.",
        "correct": "II ve III", "why": "TBK m.169'a göre borçlu, takip bildirimi yoksa dilediği alacaklıya ifa edebildiğinden I yanlıştır. Birine ifa borcu sona erdirebilir ve fazla pay alanın iç ilişkide iade yükümü vardır; II ve III doğrudur.",
        "ref": "6098 sayılı TBK m.169", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="borclar_hukuku", topic_id="borc_iliskisi",
        label="Borç İlişkisi", slug="borc_iliskisi", prefix="kh-borc-il",
        seed=20260724,
        legislation_version="6098 sayılı TBK — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
