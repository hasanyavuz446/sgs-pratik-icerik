#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Hukuk — Sözleşmenin Kurulması konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde mevzuat.gov.tr'den alınan güncel 6098 sayılı
TBK m.1–47 metnidir. Paket öneri-kabul, şekil, genel işlem koşulları, içerik,
irade bozuklukları ve temsili sınav ağırlığıyla birlikte ele alır.
"""
from topic_pack_builder import write_topic


def r(
    scenario, focus, correct, distractors, why, focus_why, ref,
    difficulty="medium", *, focus_correct=None, focus_distractors=None,
):
    item = {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors, "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref, "difficulty": difficulty,
    }
    if focus_correct is not None:
        item["focus_correct"] = focus_correct
    if focus_distractors is not None:
        item["focus_distractors"] = focus_distractors
    return item


RULES = [
    r(
        "A satma, B de aynı malı aynı koşullarla satın alma iradesini karşılıklı açıklamıştır. Açıklamalardan biri açık, diğeri davranışla yapılmıştır. Sözleşmenin kurulması bakımından hangisi doğrudur?",
        "Sözleşmenin kurulması için taraf iradelerinin taşıması gereken temel ilişki hangisidir?",
        "İradeler karşılıklı ve birbirine uygun açıklanmalı; açıklama açık veya örtülü olabilir",
        ["Taraf iradelerinin birbirine aykırı olması ve hiçbir şekilde açıklanmaması gerekir", "Sözleşme yalnız iki açıklamanın da noter huzurunda sözlü yapılmasıyla kurulur", "Taraflardan birinin içinden geçirdiği fakat açıklamadığı irade tek başına yeterlidir", "Örtülü irade açıklaması hiçbir sözleşmede hukuki sonuç doğuramaz ve hiçbir zaman kabul sayılamaz"],
        "TBK m.1, sözleşmeyi karşılıklı ve birbirine uygun irade açıklamalarına bağlar; açıklamanın açık veya örtülü olabileceğini kabul eder.",
        "Kurucu unsur iç irade değil, karşı tarafa yönelen uyumlu açıklamadır. Davranışın durumdan anlam çıkaracak açıklıkta olması hâlinde örtülü kabul de mümkündür.",
        "6098 sayılı TBK m.1", "easy",
    ),
    r(
        "Taraflar sözleşmenin esaslı noktalarında anlaşmış, teslim ambalajının rengi gibi ikinci derecedeki bir noktayı görüşmemiştir. Sözleşmenin kurulması bakımından hangisi doğrudur?",
        "Esaslı noktalarda anlaşan tarafların ikinci derecedeki noktaları açık bırakmasının sözleşmeye etkisi nedir?",
        "Esaslı noktalar üzerinde uyuşma varsa sözleşme kural olarak kurulmuş sayılır",
        ["İkinci derecedeki tek bir nokta açık kaldığında sözleşme kesin olarak kurulmamış sayılır", "Yan noktalar görüşülmediyse esaslı noktalardaki anlaşma kendiliğinden hükümsüz olur", "Sözleşme yalnız bütün ayrıntılar mahkemece önceden belirlenirse kurulabilir", "İkinci derecedeki noktalar tarafların iradesinden bağımsız olarak ceza koşuluna dönüşür"],
        "TBK m.2, esaslı noktalarda uyuşma varsa ikinci derecedeki noktalar görüşülmese bile sözleşmeyi kurulmuş sayar; uyuşmazlığı işin özelliğine göre hâkim çözebilir.",
        "Sözleşmenin çekirdeği esaslı noktalardır. Yan noktaların eksikliği kuruluşa engel olmaz; şekle ilişkin özel kurallar saklıdır.",
        "6098 sayılı TBK m.2", "medium",
    ),
    r(
        "Öneren, kabul için on günlük süre belirlemiştir. Süre bitmeden önerisini geri çektiğini bildirmiş, fakat geri alma kuralları da oluşmamıştır. Bağlılık bakımından hangisi doğrudur?",
        "Kabul için süre belirlenerek yapılan öneri önereni hangi ana kadar bağlar?",
        "Öneren belirlediği kabul süresinin sonuna kadar önerisiyle bağlıdır",
        ["Öneren süre belirlese bile öneriyi her an hiçbir koşul olmadan yok sayabilir", "Süreli öneri yalnız kabul süresi bittikten sonra bağlayıcılık kazanır", "Öneren yalnız karşı tarafın öneriyi reddetmesinden sonra kabul verebilir", "Kabul süresi belirlenmesi öneriyi bağlayıcı olmayan reklama dönüştürür"],
        "TBK m.3'e göre kabul süresi belirleyen öneren sürenin sonuna kadar önerisiyle bağlıdır; kabul bu sürede ulaşmazsa bağlılık sona erer.",
        "Süre, karşı tarafa güvenli bir kabul penceresi verir. Öneren geri alma için TBK m.10 koşulları yoksa bu pencere içinde tek taraflı olarak serbestleşemez.",
        "6098 sayılı TBK m.3", "easy",
    ),
    r(
        "A, yüz yüze görüşmede kabul süresi belirlemeden öneride bulunmuş; B görüşme sırasında hemen kabul etmemiştir. A'nın öneriyle bağlılığı bakımından hangisi doğrudur?",
        "Hazır olanlar arasında kabul süresi belirlenmeksizin yapılan önerinin bağlayıcılığı nasıl sona erer?",
        "Öneri hemen kabul edilmezse öneren kural olarak bağlılıktan kurtulur",
        ["Öneren kabul edilmeyen öneriyle ömür boyu ve değişmez biçimde bağlı kalır", "Hazır kişiye yapılan öneri ancak otuz gün sonra karşı tarafa ulaşmış sayılır", "Hemen kabul edilmeyen öneri kendiliğinden kurulmuş sözleşme sayılır", "Bağlılığın sona ermesi için karşı tarafın ticaret sicilinden izin alması gerekir"],
        "TBK m.4 hazır olan kişiye süresiz öneri hemen kabul edilmezse önereni bağlılıktan kurtarır. Doğrudan iletişim sırasında telefon ve bilgisayar önerileri de hazırlar arasıdır.",
        "Hazır olma fiziksel aynı mekânla sınırlı değildir; kesintisiz doğrudan iletişim yeterlidir. Süresiz öneride karar anı görüşmenin kendisidir.",
        "6098 sayılı TBK m.4", "medium",
    ),
    r(
        "A, kabul süresi belirlemeden mektupla hazır olmayan B'ye öneri göndermiştir. Yanıtın olağan sürede ulaşması beklenmektedir. A'nın bağlılığı nasıl belirlenir?",
        "Hazır olmayan kişiye süresiz yapılan öneri, önereni hangi ana kadar bağlar?",
        "Zamanında gönderilen yanıtın usulüne uygun olarak ulaşmasının beklenebileceği ana kadar",
        ["Öneri gönderildiği anda hiçbir kabul imkânı bırakmadan kesin olarak sona erer", "Öneren yalnız mektubun yazıldığı günün sonuna kadar ve teslimden bağımsız bağlıdır", "Öneri hazır olmayan kişiye yapılınca kendiliğinden kabul edilmiş sayılır", "Bağlılık ancak karşı tarafın ölümünden sonra ve mirasçı kararıyla başlar"],
        "TBK m.5, hazır olmayanlar arasındaki süresiz öneriyi zamanında ve usulüne uygun gönderilecek yanıtın ulaşmasının beklenebileceği ana kadar bağlayıcı tutar.",
        "Mesafe ilişkilerinde makul gönderme ve ulaşma süresi hesaba katılır. Geç ulaşan zamanında kabulü istemeyen öneren durumu hemen bildirmelidir.",
        "6098 sayılı TBK m.5", "medium",
    ),
    r(
        "Önerinin niteliği gereği açık kabul beklenmesi gerekmemekte, muhatap da öneriyi uygun sürede reddetmemektedir. Örtülü kabul bakımından hangisi doğrudur?",
        "Açık kabul beklenmesinin gerekmediği durumda öneri uygun sürede reddedilmezse hangi sonuç doğabilir?",
        "Öneri uygun sürede reddedilmezse sözleşme kurulmuş sayılabilir",
        ["Sessizlik her durumda ve bütün sözleşmelerde kesin ret anlamına gelir", "Açık kabul yoksa önerinin niteliğine bakılmaksızın sözleşme kurulamaz", "Muhatabın reddetmemesi önereni kendiliğinden borçsuz ve alacaklı yapar", "Örtülü kabul yalnız mahkeme kararı kesinleştikten sonra mümkün olur"],
        "TBK m.6, Kanun, işin özelliği veya durum gereği açık kabul beklenmiyorsa önerinin uygun sürede reddedilmemesine kuruluş sonucu bağlar.",
        "Sessizlik genel kabul kuralı değildir. Örtülü kabul için somut ilişkinin açık kabul beklentisini gereksiz kılması gerekir.",
        "6098 sayılı TBK m.6", "medium",
    ),
    r(
        "Bir işletme, tüketicinin sipariş etmediği ürünü gönderip iade etmeyen kişinin bedeli kabul ettiğini ileri sürmüştür. Ismarlanmayan şey bakımından hangisi doğrudur?",
        "Ismarlanmamış bir şeyin gönderilmesi ve alan kişinin yükümlülüğü hakkında temel kural nedir?",
        "Gönderim öneri sayılmaz; alan kişi şeyi geri göndermek veya saklamak zorunda değildir",
        ["Gönderim kesin öneridir ve alan kişi bedeli hemen ödemek zorundadır", "Alan kişi ürünü ömür boyu ücretsiz saklamak ve sigortalamakla yükümlüdür", "Siparişsiz ürün yalnız teslimle birlikte geçerli ceza sözleşmesi oluşturur", "Alan kişi ürünü mutlaka notere teslim etmedikçe hapis cezası borçlusu olur"],
        "TBK m.7, ısmarlanmayan şeyin gönderilmesini öneri saymaz; alan kişiye geri gönderme veya saklama borcu yüklemez.",
        "Gönderen kendi tek taraflı davranışıyla muhataba sözleşme ve masraf yükleyemez. Sessizlik burada kabul olarak nitelendirilmez.",
        "6098 sayılı TBK m.7", "easy",
    ),
    r(
        "Öneriyi geri alma açıklaması öneriyle aynı anda muhataba ulaşmıştır. Muhatap önce öneri metnini okumuştur. Geri almanın etkisi bakımından hangisi doğrudur?",
        "Önerinin geri alınmış sayılması için geri alma açıklamasının ulaşma veya öğrenilme zamanı nasıl olmalıdır?",
        "Geri alma öneriden önce veya aynı anda ulaşırsa öneri yapılmamış sayılır",
        ["Geri alma yalnız önerinin kabulünden bir yıl sonra ulaşırsa sonuç doğurur", "Geri alma zamanı önem taşımaz ve öneren her durumda ömür boyu bağlıdır", "Öneri muhataba ulaşmadan geri alınması kanunen kesin olarak yasaktır", "Geri alma sadece mahkemece öneri metni değiştirildikten sonra mümkündür"],
        "TBK m.10, geri alma öneriden önce veya aynı anda ulaşırsa ya da sonra ulaşsa bile öneriden önce öğrenilirse öneriyi yapılmamış sayar.",
        "Ulaşma ile fiilî öğrenme farklı olabilir. Kanun muhatabın güveni oluşmadan önceki geri almayı etkili kılar; aynı kural kabul için de geçerlidir.",
        "6098 sayılı TBK m.10", "medium",
    ),
    r(
        "Kanunda belirli şekle bağlanmamış bir sözleşme taraflarca sözlü kurulmuştur. Taraflar ayrıca şekil kararlaştırmamıştır. Geçerlilik bakımından hangisi doğrudur?",
        "Sözleşmelerin şekli konusunda TBK'nın kabul ettiği genel ilke hangisidir?",
        "Kanunda aksi yoksa sözleşmenin geçerliliği herhangi bir şekle bağlı değildir",
        ["Bütün sözleşmelerin geçerliliği mutlaka noterlikçe resmî senede bağlıdır", "Şekilsiz yapılan her sözleşme kendiliğinden haksız fiil sayılır", "Sözleşme yalnız beş tanık ve sicil müdürü önünde kurulabilir", "Tarafların sözlü anlaşması kanunda şekil yokken bile hiçbir sonuç doğuramaz"],
        "TBK m.12/1 sözleşmelerde şekil serbestisini genel kural kabul eder. Kanunda aksi öngörülmüşse kanuni şekil kural olarak geçerlilik şeklidir.",
        "Şekil zorunluluğu istisnadır. Kanun veya tarafların iradi şekil anlaşması bulunmadıkça sözlü, yazılı ya da davranışla kuruluş mümkündür.",
        "6098 sayılı TBK m.12/1", "easy",
    ),
    r(
        "Kanun sözleşmeyi yazılı geçerlilik şekline bağlamıştır. Metinde borç altına giren kişinin imzası bulunmamaktadır. Hangisi doğrudur?",
        "Yasal yazılı şeklin temel unsurlarından biri aşağıdakilerden hangisidir?",
        "Yazılı sözleşmede borç altına giren kişilerin imzası bulunmalıdır",
        ["Yazılı metinde borç altına girenlerin imzasının bulunması kesin olarak yasaktır", "Yazılı şekil yalnız sözleşmenin sözlü okunmasıyla ve imzasız tamamlanır", "İmza yerine her durumda açıklamasız boş sayfa kullanılması yeterlidir", "Borç altına girenin değil yalnız ilgisiz tanığın imzası zorunludur"],
        "TBK m.14/1, yazılı şekilde yapılması öngörülen sözleşmede borç altına girenlerin imzasını zorunlu tutar.",
        "İmza, yazılı metni borç altına girenin iradesine bağlar. Güvenli elektronik imza da el yazısı imzasının hukuki sonuçlarını doğurur.",
        "6098 sayılı TBK m.14-15", "easy",
    ),
    r(
        "Kanunda şekle tabi olmayan sözleşmenin noterlikçe yapılacağını taraflar kararlaştırmış, fakat daha sonra yalnız sözlü anlaşmıştır. İradi şeklin etkisi bakımından hangisi doğrudur?",
        "Tarafların kanunen şekilsiz sözleşme için belirli bir şekil kararlaştırmasının sonucu nedir?",
        "Kararlaştırılan şekle uyulmayan sözleşme kural olarak tarafları bağlamaz",
        ["İradi şekil kararı hiçbir durumda sonuç doğurmaz ve sözleşme daima bağlar", "Şekle uyulmaması yalnız sözleşme bedelini otomatik olarak iki katına çıkarır", "Tarafların belirlediği şekil sadece üçüncü kişileri bağlar, tarafları etkilemez", "İradi şekil yalnız sözleşme ifa edildikten sonra geçmişe etkili uygulanır"],
        "TBK m.17, Kanunda şekle bağlanmamış sözleşme için taraflar belirli şekil kararlaştırmışsa buna uyulmayan sözleşmenin tarafları bağlamayacağını düzenler.",
        "Taraflar şekil serbestisini kullanarak kendilerini şekle bağlayabilir. Yalnız 'yazılı' denmişse yasal yazılı şekil hükümleri uygulanır.",
        "6098 sayılı TBK m.17", "medium",
    ),
    r(
        "Taraflar sözleşmeye gerçekte istemedikleri bir ad vermiş, kullandıkları sözcüklerle gerçek ortak amaçlarını gizlemiştir. Yorumda hangi irade esas alınır?",
        "Sözleşmenin türü ve içeriği belirlenirken kullanılan yanlış veya gizleyici sözcükler karşısında hangi ölçüt uygulanır?",
        "Sözleşmenin tür ve içeriğinde tarafların gerçek ve ortak iradeleri esas alınır",
        ["Sözleşme başlığındaki ilk sözcük gerçek iradeden bağımsız olarak tek ölçüttür", "Tarafların ortak amacı hiçbir durumda araştırılamaz ve daima yok sayılır", "Yorum yalnız sözleşme dışındaki üçüncü kişinin kişisel isteğine göre yapılır", "Gerçek irade yerine her durumda ticaret sicilindeki işletme adı uygulanır"],
        "TBK m.19/1, sözleşmenin tür ve içeriğinde yanlışlıkla veya gerçek amacı gizlemek için kullanılan sözcüklere değil gerçek ve ortak iradeye üstünlük verir.",
        "Yorum görünüşteki etikete hapsolmaz. Tarafların birlikte gerçekleştirmek istediği hukuki ve ekonomik amaç belirlenir.",
        "6098 sayılı TBK m.19/1", "medium",
    ),
    r(
        "Banka, ileride çok sayıdaki benzer sözleşmede kullanmak üzere koşulları önceden ve tek başına hazırlayıp müşteriye sunmuştur. Bu hükümler nasıl nitelendirilir?",
        "Genel işlem koşulunun ayırt edici hazırlama ve kullanım özellikleri hangileridir?",
        "Düzenleyen tarafından çok sayıda benzer sözleşme için önceden tek yanlı hazırlanır",
        ["Hükümler yalnız tek olay için tarafların ayrıntılı pazarlığıyla birlikte hazırlanır", "Koşullar mahkemece sadece uyuşmazlıktan sonra ve bir sözleşme için yazılır", "Genel işlem koşulu yalnız sözlü ve iki tarafça aynı anda üretilen hükümlerdir", "Bir hükmün genel koşul olması için bütün sözleşme metinlerinin harfiyen özdeşliği gerekir"],
        "TBK m.20 genel işlem koşulunu, düzenleyenin çok sayıdaki benzer sözleşmede kullanmak amacıyla önceden ve tek başına hazırladığı hükümler olarak tanımlar.",
        "Metinlerin tümüyle özdeş olmaması veya 'tek tek tartışıldı' kaydı tek başına niteliği kaldırmaz. Hazırlama gücü ve çoklu kullanım amacı belirleyicidir.",
        "6098 sayılı TBK m.20", "easy",
    ),
    r(
        "Düzenleyen, karşı tarafın menfaatine aykırı genel işlem koşullarının varlığını açıkça bildirmemiş ve içeriğini öğrenme imkânı sağlamamıştır. Sonuç nedir?",
        "Karşı taraf aleyhine genel işlem koşulunun sözleşme kapsamına girmesi için gereken koşullar hangileridir?",
        "Açık bilgi, içeriği öğrenme imkânı ve karşı tarafın kabulü birlikte gerekir",
        ["Koşulun küçük yazılması ve karşı taraftan saklanması tek başına yeterlidir", "Düzenleyenin içinden koşulun geçerli olduğunu düşünmesi kapsam için yeterlidir", "Karşı tarafın koşulu öğrenmesi kesin olarak engellenmeli ve ret hakkı kaldırılmalıdır", "Koşul yalnız sözleşmeyle ilgisizse ve karşı taraf görmediyse geçerli olur"],
        "TBK m.21/1, karşı taraf aleyhine genel koşulun kapsama girmesini açık bilgilendirme, içeriği öğrenme imkânı ve kabul şartlarına bağlar; aksi hâlde yazılmamış sayar.",
        "Şeffaflık ve gerçek kabul birlikte aranır. Sözleşmenin niteliğine yabancı şaşırtıcı koşullar da ayrıca yazılmamış sayılır.",
        "6098 sayılı TBK m.21", "medium",
    ),
    r(
        "Genel işlem koşulu açık ve anlaşılır değildir; iki farklı anlama gelmektedir. Yorum bakımından hangisi doğrudur?",
        "Açık olmayan veya birden çok anlama gelen genel işlem koşulu kimin lehine yorumlanır?",
        "Belirsiz koşul düzenleyenin aleyhine ve karşı tarafın lehine yorumlanır",
        ["Belirsiz koşul daima düzenleyenin lehine ve karşı tarafın aleyhine yorumlanır", "Koşul yorumlanmadan yalnız düzenleyenin iç iradesine göre uygulanır", "Belirsizlik karşı tarafın bütün haklarını kendiliğinden sona erdirir", "Çok anlamlı hüküm yalnız sözleşmeyi yazan bilgisayar lehine yorumlanır"],
        "TBK m.23 belirsiz genel işlem koşulunu düzenleyenin aleyhine ve karşı tarafın lehine yorumlayan contra proferentem ilkesini benimser.",
        "Metni tek yanlı hazırlayan belirsizlik riskini taşır. Karşı tarafın anlamadığı metinden düzenleyen lehine sonuç çıkarılamaz.",
        "6098 sayılı TBK m.23", "easy",
    ),
    r(
        "Genel koşul, düzenleyene sözleşmeyi karşı taraf aleyhine tek yanlı değiştirme yetkisi vermektedir. Bu kaydın durumu nedir?",
        "Düzenleyene karşı taraf aleyhine tek yanlı değişiklik veya yeni düzenleme yetkisi veren genel işlem koşulu nasıl değerlendirilir?",
        "Tek yanlı değişiklik yetkisi veren kayıt yazılmamış sayılır",
        ["Kayıt her durumda geçerlidir ve düzenleyen bütün borçları sınırsız artırabilir", "Kayıt yalnız karşı tarafın haklarını kaldırdığı ölçüde zorunlu uygulanır", "Tek yanlı değişiklik kaydı sözleşmeyi kendiliğinden resmî senede dönüştürür", "Düzenleyenin her değişikliği mahkeme kararı olmadan kesin hüküm sayılır"],
        "TBK m.24, düzenleyene karşı taraf aleyhine genel koşulu tek yanlı değiştirme veya yeni düzenleme getirme yetkisi veren kayıtları yazılmamış sayar.",
        "Önceden hazırlanmış sözleşme, düzenleyene sonradan sınırsız içerik kurma gücü veremez. Ayrıca dürüstlüğe aykırı ağırlaştırıcı hükümler m.25 içerik denetimine tabidir.",
        "6098 sayılı TBK m.24-25", "medium",
    ),
    r(
        "Taraflar, konusu kanunun emredici hükmüne aykırı bir sözleşme kurmuştur. Sözleşme özgürlüğünün sınırı bakımından hangisi doğrudur?",
        "Emredici hükme, ahlaka, kamu düzenine, kişilik haklarına aykırı veya konusu imkânsız sözleşmenin yaptırımı nedir?",
        "Emredici hükme aykırı veya imkânsız konulu sözleşme kesin hükümsüzdür",
        ["Sözleşme her durumda geçerlidir ve aykırılık yalnız başlığını değiştirir", "Aykırılık sözleşmeyi kendiliğinden süresiz ve geri alınamaz öneriye dönüştürür", "Sözleşme yalnız borçlunun ölümüyle geçerli hâle gelir", "Emredici hükme aykırılık karşı tarafın kabulüyle daima giderilir"],
        "TBK m.26 sözleşme özgürlüğünü kanuni sınırlar içinde tanır; m.27 emredici hüküm, ahlak, kamu düzeni, kişilik hakkı aykırılığı veya imkânsız konuda kesin hükümsüzlük öngörür.",
        "Sözleşme özgürlüğü sınırsız değildir. Kesin hükümsüzlük başlangıçtan itibaren geçerlilik sonucunu engeller ve kural olarak herkesçe ileri sürülebilir.",
        "6098 sayılı TBK m.26-27", "easy",
    ),
    r(
        "Zor durumdaki kişinin bu hâlinden yararlanılarak karşılıklı edimler arasında açık oransızlık oluşturulmuştur. Zarar görenin seçimlik hakkı bakımından hangisi doğrudur?",
        "Aşırı yararlanmada zarar görenin TBK m.28 uyarınca kullanabileceği temel seçimlik yollar hangileridir?",
        "Bağlı olmadığını bildirip iade veya bağlı kalıp oransızlığın giderilmesini isteyebilir",
        ["Zarar gören yalnız sözleşmeyi iki kat bedelle ifa etmek zorundadır", "Açık oransızlık hiçbir durumda sözleşmeye etki etmez ve hak vermez", "Zarar gören sadece düzenleyenin şirket ortağı olmayı talep edebilir", "Aşırı yararlanma bütün edimleri karşı tarafa bağışlanmış sayar"],
        "TBK m.28 açık oransızlık ve sömürü koşulları oluştuğunda zarar görene sözleşmeyle bağlı olmadığını bildirip iade veya sözleşmeye bağlı kalıp oransızlığın giderilmesini isteme seçeneği verir.",
        "Gabin yalnız fiyat farkı değildir; zor durum, düşüncesizlik veya deneyimsizlikten yararlanma gerekir. Zarar gören sözleşmeyi koruyan ya da çözen yolu seçebilir.",
        "6098 sayılı TBK m.28", "hard",
    ),
    r(
        "Taraflar ileride resmî şekilde taşınmaz satış sözleşmesi kurmak üzere yalnız sözlü önsözleşme yapmıştır. Önsözleşmenin şekli bakımından hangisi doğrudur?",
        "Kanuni istisnalar dışında önsözleşmenin geçerliliği hangi sözleşmenin şekline bağlıdır?",
        "Önsözleşme ileride kurulacak asıl sözleşmenin şekline uygun yapılmalıdır",
        ["Önsözleşme her durumda asıl sözleşmeden bağımsız olarak yalnız sözlü yapılmalıdır", "Asıl sözleşmenin şekli önsözleşmeyi hiçbir şekilde etkilemez", "Önsözleşme ancak asıl sözleşme ifa edildikten sonra geriye etkili kurulabilir", "Önsözleşme yalnız tarafların şirket kurması hâlinde şekil kazanır"],
        "TBK m.29 önsözleşmeyi geçerli kabul eder; kanuni istisnalar dışında geçerliliğini ileride kurulacak asıl sözleşmenin şekline bağlar.",
        "Önsözleşme gelecekte sözleşme yapma borcu doğurur. Şekil, ileride kurulacak sözleşmenin geçerlilik düzenini dolanmak için kullanılamaz.",
        "6098 sayılı TBK m.29", "medium",
    ),
    r(
        "Taraf, sözleşme kurulurken sözleşmenin konusu hakkında esaslı yanılmaya düşmüştür. Bağlayıcılık bakımından hangisi doğrudur?",
        "Sözleşme kurulurken yapılan basit hesap yanlışlığının sonucu nedir?",
        "Esaslı yanılmaya düşen taraf, kurulan sözleşmeyle bağlı değildir",
        ["Her türlü esaslı yanılma sözleşmeyi yanılan yönünden kesin ve değişmez bağlar", "Yanılma yalnız karşı tarafın borcunu artırır ve yanılana hiçbir hak vermez", "Yanılan sözleşmeyi mutlaka ifa edip ayrıca iki kat tazminat öder", "Esaslı yanılma sadece sözleşmenin başlığını değiştirir, bağlayıcılığı etkilemez"],
        "TBK m.30 esaslı yanılmaya düşen tarafı sözleşmeyle bağlı tutmaz. Sözleşme türü, konu, kişi veya edim miktarındaki önemli açıklama yanılmaları m.31'de örneklenir.",
        "Basit hesap yanlışlığı sözleşmenin bağlayıcılığını ortadan kaldırmaz; hesap düzeltilerek sözleşme korunur.",
        "6098 sayılı TBK m.30-31", "medium",
        focus_correct="Basit hesap yanlışlığı sözleşmenin geçerliliğini etkilemez; yanlışlık düzeltilir",
        focus_distractors=[
            "Basit hesap yanlışlığı sözleşmeyi baştan itibaren kesin hükümsüz kılar",
            "Hesap yanlışlığı yalnız karşı taraf isterse sözleşmenin konusunu değiştirir",
            "Her hesap yanlışlığı yanılana sözleşmeyi süresiz olarak geri alma hakkı verir",
            "Hesap yanlışlığı hiçbir biçimde düzeltilmez ve yanlış sonuç tarafları değişmez biçimde bağlar",
        ],
    ),
    r(
        "Taraf yalnız kişisel saikinde yanılmıştır; bu saiki sözleşmenin temeli saydığı karşı tarafça bilinebilir değildir. Yanılmanın esaslılığı bakımından hangisi doğrudur?",
        "Saikte yanılmanın esaslı sayılması için yanılanın saiki sözleşmenin temeli sayması dışında hangi koşul aranır?",
        "Temel sayılan saik dürüstlüğe uygun olmalı ve karşı tarafça bilinebilir olmalıdır",
        ["Her kişisel saik yanılması başka koşul olmadan daima esaslı kabul edilir", "Saikin karşı tarafça bilinememesi esaslılığın zorunlu koşuludur", "Saikte yanılma yalnız sözleşme tamamen ifa edildikten sonra doğabilir", "Saik yalnız üçüncü kişinin gizli düşüncesine uygunsa esaslı sayılır"],
        "TBK m.32 saikte yanılmayı kural olarak esaslı saymaz; saikin sözleşme temeli olması, dürüstlüğe uygunluğu ve bunun karşı tarafça bilinebilirliği birlikte aranır.",
        "Sözleşme dışı her beklenti karşı tarafa yüklenemez. Saikin ortak işlem temelinde görünür ve dürüstçe önem taşıması gerekir.",
        "6098 sayılı TBK m.32", "hard",
    ),
    r(
        "A, B'nin aldatması sonucu sözleşme yapmıştır; aldatmanın yol açtığı yanılma esaslı nitelikte değildir. A'nın bağlılığı bakımından hangisi doğrudur?",
        "Karşı tarafın aldatması sonucu sözleşme yapan kişinin yanılmasının esaslı olması gerekir mi?",
        "Aldatma varsa yanılma esaslı olmasa da aldatılan sözleşmeyle bağlı değildir",
        ["Aldatılan yalnız yanılma esaslıysa ve sözleşme kesinlikle ifa edilmişse bağlı olmaz", "Aldatma sözleşmenin bağlayıcılığını hiçbir koşulda etkilemez", "Aldatılan her durumda aldatana yeni bir sözleşme önerisi yapmak zorundadır", "Aldatma yalnız ticaret siciline tescil edilirse hukuki sonuç doğurur"],
        "TBK m.36/1, taraflardan birinin diğerinin aldatmasıyla sözleşme yapması hâlinde yanılma esaslı olmasa bile sözleşmeyle bağlı olmadığını düzenler.",
        "Aldatma irade oluşumunu hileli biçimde bozar. Bu nedenle esaslı yanılmada aranan önem eşiği ayrıca aranmaz.",
        "6098 sayılı TBK m.36", "easy",
    ),
    r(
        "Kişi, kendisinin veya yakınının malvarlığına ağır ve yakın zarar tehlikesi doğduğuna haklı olarak inanarak sözleşme yapmıştır. Korkutma bakımından hangisi doğrudur?",
        "TBK m.38 anlamında korkutmanın oluşması için zarar tehlikesi hangi nitelikleri taşımalıdır?",
        "Tehlike kişilik hakkı veya malvarlığına yönelik ağır ve yakın olmalıdır",
        ["Tehlikenin uzak, önemsiz ve kişinin inanamayacağı nitelikte olması zorunludur", "Korkutma yalnız geçmişte sona ermiş küçük bir rahatsızlığa dayanabilir", "Zarar tehlikesinin kişiye veya yakınlarına yönelmesi kesin olarak yasaktır", "Korkutma yalnız sözleşme yapıldıktan on yıl sonra ortaya çıkan olaydır"],
        "TBK m.38, kişinin kendisi veya yakınının kişilik hakkı ya da malvarlığına yönelik ağır ve yakın zarar tehlikesine haklı olarak inanmasını korkutma sayar.",
        "Ölçüt somut kişinin durumu içinde haklı korkudur. Kanuni hakkı kullanma tehdidi de zor durumdan aşırı menfaat sağlama aracı yapılırsa korkutma olabilir.",
        "6098 sayılı TBK m.37-38", "medium",
    ),
    r(
        "Aldatılan taraf aldatmayı öğrendikten sonra bir yıl boyunca bağlı olmadığını bildirmemiş ve verdiğini geri istememiştir. Sonuç nedir?",
        "Yanılma veya aldatmanın öğrenilmesi ya da korkutma etkisinin kalkmasından başlayan onama süresi ne kadardır?",
        "Bir yıl içinde hak kullanılmazsa sözleşme onanmış sayılır",
        ["Hak hiçbir süreye bağlı değildir ve sözleşme yüz yıl askıda kalır", "Süre yalnız iki gündür ve sözleşmenin kurulduğu tarihten önce başlar", "Bir yıl sonunda sözleşme kendiliğinden ceza mahkûmiyetine dönüşür", "Süre beş yıldır ve yalnız borçlunun ölümünden sonra işlemeye başlar"],
        "TBK m.39, yanılma veya aldatmanın öğrenilmesinden ya da korkutmanın etkisinin kalkmasından itibaren bir yıl içinde bağlı olmama bildirimi veya geri istem olmazsa onama sonucu doğurur.",
        "Bir yıllık hak düşürücü süre, askıda kalan bağlayıcılık durumunu kesinleştirir. Aldatma veya korkutmadan doğan tazminat hakkı onamayla kendiliğinden ortadan kalkmaz.",
        "6098 sayılı TBK m.39", "medium",
    ),
    r(
        "Yetkili temsilci, temsil olunan adına ve hesabına sözleşme yapmış ve temsil sıfatını karşı tarafa bildirmiştir. İşlemin sonuçları kime aittir?",
        "Yetkili doğrudan temsilde temsilcinin yaptığı hukuki işlem kural olarak kimi bağlar?",
        "Yetkili temsil işleminin sonuçları doğrudan doğruya temsil olunanı bağlar",
        ["İşlemin bütün sonuçları yalnız karşı tarafla ilgisiz üçüncü kişiye ait olur", "Yetkili temsil hiçbir sonuç doğurmaz ve sözleşme kendiliğinden hükümsüzdür", "Temsilci her durumda işlemin tek tarafı olur ve temsil olunan hiç bağlanmaz", "İşlem yalnız temsilcinin ölümüyle temsil olunanı geçmişe etkili bağlar"],
        "TBK m.40, yetkili temsilcinin başkası adına ve hesabına yaptığı hukuki işlemin sonuçlarını doğrudan temsil olunana bağlar.",
        "Doğrudan temsil, hak ve borçların temsilci üzerinde durmadan temsil olunanda doğmasını sağlar. Temsil sıfatının açıklanması kuraldır.",
        "6098 sayılı TBK m.40", "easy",
    ),
    r(
        "Yetkisiz temsilci A adına B ile sözleşme yapmış; A işlemi henüz onamamıştır. İşlemin A'yı bağlaması bakımından hangisi doğrudur?",
        "Yetkisiz temsilcinin yaptığı hukuki işlemin temsil olunanı bağlaması hangi olaya bağlıdır?",
        "Yetkisiz temsil işlemi, temsil olunan işlemi onadığı takdirde kendisini bağlar",
        ["Yetkisiz temsil işlemi temsil olunanı bilgisi olmadan her durumda kesin bağlar", "Onama yalnız yetkisiz temsilcinin kendi kendine vereceği izinle gerçekleşir", "Temsil olunan işlemi reddetse bile bütün borçlar iki katıyla ona geçer", "Yetkisizlik işlemi karşı tarafın bütün sözleşmelerini kendiliğinden sona erdirir"],
        "TBK m.46'ya göre yetkisiz temsilcinin işlemi ancak temsil olunan onarsa onu bağlar. Karşı taraf uygun sürede onama açıklaması isteyebilir.",
        "Yetkisiz işlem onamaya kadar temsil olunan yönünden askıdadır. Sürede onama olmazsa karşı taraf da işlemle bağlı olmaktan kurtulur.",
        "6098 sayılı TBK m.46", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Öneri ve kabulle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Süreli öneri kabul süresinin sonuna kadar bağlar.\n\nII. Doğrudan telefon görüşmesindeki öneri hazırlar arası sayılır.\n\nIII. Ismarlanmayan şeyin gönderilmesi öneri sayılmaz.",
        "correct": "I, II ve III", "why": "TBK m.3 süreli öneriyi, m.4 telefon gibi doğrudan iletişimi ve m.7 ısmarlanmayan şeyi düzenler. Üç ifade de doğrudur.",
        "ref": "6098 sayılı TBK m.3, 4 ve 7", "difficulty": "medium",
    },
    {
        "stem": "Sözleşmenin şekliyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kanunda aksi yoksa şekil serbestisi vardır.\n\nII. Yasal yazılı şekilde borç altına girenlerin imzası aranır.\n\nIII. Güvenli elektronik imza el yazısı imzasının hukuki sonuçlarını doğurur.",
        "correct": "I, II ve III", "why": "TBK m.12 şekil serbestisini, m.14 imzayı ve m.15 güvenli elektronik imzanın el yazısı imzasıyla eş sonuçlarını düzenler.",
        "ref": "6098 sayılı TBK m.12, 14 ve 15", "difficulty": "medium",
    },
    {
        "stem": "Genel işlem koşullarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Çok sayıda benzer sözleşme için önceden hazırlanır.\n\nII. Öğrenme imkânı verilmeyen aleyhe koşul her durumda sözleşme kapsamına girer.\n\nIII. Belirsiz hüküm düzenleyenin aleyhine yorumlanır.",
        "correct": "I ve III", "why": "TBK m.20 nedeniyle I, m.23 nedeniyle III doğrudur. Öğrenme imkânı verilmeyen aleyhe koşul m.21 uyarınca yazılmamış sayılır; II yanlıştır.",
        "ref": "6098 sayılı TBK m.20, 21 ve 23", "difficulty": "medium",
    },
    {
        "stem": "İrade bozukluklarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Esaslı yanılan sözleşmeyle bağlı olmaz.\n\nII. Karşı tarafın aldatmasında yanılmanın esaslı olması gerekmez.\n\nIII. Korkutma yalnız üçüncü kişi tarafından yapılırsa sonuç doğurur.",
        "correct": "I ve II", "why": "TBK m.30 ve 36 nedeniyle I ve II doğrudur. Korkutma karşı taraf veya üçüncü kişi tarafından yapılabilir; III yanlıştır.",
        "ref": "6098 sayılı TBK m.30, 36 ve 37", "difficulty": "medium",
    },
    {
        "stem": "Temsille ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yetkili temsil işlemi doğrudan temsil olunanı bağlayabilir.\n\nII. Hukuki işlemden doğan temsil yetkisi kural olarak geri alınabilir.\n\nIII. Yetkisiz temsil işlemi onama olmadan temsil olunanı kesin bağlar.",
        "correct": "I ve II", "why": "TBK m.40 ve 42 nedeniyle I ve II doğrudur. Yetkisiz işlem m.46 gereği ancak onamayla temsil olunanı bağlar; III yanlıştır.",
        "ref": "6098 sayılı TBK m.40, 42 ve 46", "difficulty": "medium",
    },
    {
        "stem": "Sözleşmenin içeriğiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Taraflar içeriği kanuni sınırlar içinde özgürce belirler.\n\nII. Konusu imkânsız sözleşme her durumda geçerlidir.\n\nIII. Kısmi hükümsüzlük kural olarak kalan hükümleri etkilemez.",
        "correct": "I ve III", "why": "TBK m.26 nedeniyle I, m.27'deki kısmi hükümsüzlük kuralı nedeniyle III doğrudur. Konusu imkânsız sözleşme kesin hükümsüzdür; II yanlıştır.",
        "ref": "6098 sayılı TBK m.26-27", "difficulty": "medium",
    },
    {
        "stem": "Aşırı yararlanmayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Karşılıklı edimler arasında açık oransızlık aranır.\n\nII. Zor durum, düşüncesizlik veya deneyimsizlikten yararlanma gerekir.\n\nIII. Zarar görenin sözleşmeyle bağlı kalıp oransızlığı giderme seçeneği yoktur.",
        "correct": "I ve II", "why": "TBK m.28'in maddi ve öznel koşulları I ve II'dir. Zarar gören sözleşmeyi koruyup oransızlığın giderilmesini de seçebilir; III yanlıştır.",
        "ref": "6098 sayılı TBK m.28", "difficulty": "hard",
    },
    {
        "stem": "İrade bozukluğunun giderilmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bir yıllık süre her durumda sözleşmenin kurulmasından önce başlar.\n\nII. Korkutmada süre etkinin ortadan kalkmasıyla başlayabilir.\n\nIII. Sürede hak kullanılmazsa sözleşme onanmış sayılabilir.",
        "correct": "II ve III", "why": "TBK m.39'a göre korkutmada süre etkinin ortadan kalkmasıyla başlayabileceğinden II, süresinde hak kullanılmaması onama doğurabildiğinden III doğrudur. Süre sözleşmeden önce başlamaz; I yanlıştır.",
        "ref": "6098 sayılı TBK m.39", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="borclar_hukuku", topic_id="sozlesmenin_kurulmasi",
        label="Sözleşmenin Kurulması", slug="sozlesmenin_kurulmasi",
        prefix="kh-soz-kur", seed=20260725,
        legislation_version="6098 sayılı TBK m.1–47 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
