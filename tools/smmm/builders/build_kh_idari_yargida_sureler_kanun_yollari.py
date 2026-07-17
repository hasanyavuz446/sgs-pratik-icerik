#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İdari Yargıda Süreler ve Kanun Yolları — 60 özgün soru."""
from topic_pack_builder import write_topic


def R(scenario, focus, correct, bank, why, ref, difficulty="medium"):
    return locals()


WRONG = {
    "sure": [
        "Süre bildirimin yapıldığı gün başlar ve hafta sonları hesaba katılmadan yalnız iş günleri üzerinden yürür",
        "Özel kanunda farklı süre olsa bile bütün idari davalarda değişmez biçimde doksan günlük tek süre uygulanır",
        "Sürenin son günü tatile rastlarsa önceki çalışma gününde sona erer ve sonraki güne uzaması mümkün değildir",
        "Çalışmaya ara verme bütün idari dava sürelerini ara verme boyunca durdurur ve kalan süre sonradan aynen işletilir",
        "İdari makama yapılan her başvuru, kanuni süresi dışında yapılsa bile sona ermiş dava açma süresini yeniden başlatır",
        "Yazılı bildirim bulunması hâlinde süre bildirimi izleyen gün değil, işlemin idarece hazırlandığı tarihte başlar",
        "Görevsiz adli yargı yerine yapılan başvurunun tarihi hiçbir koşulda korunmaz ve dava daima süreden reddedilir",
        "Kanunda günle belirlenen sürelerin hesabında resmî tatiller tamamen dışarıda bırakılarak yalnız mesai günleri sayılır",
    ],
    "yd": [
        "İdari dava açılması bütün işlemlerin yürütmesini kendiliğinden durdurur ve ayrıca mahkeme kararı gerekmez",
        "Yürütmenin durdurulması için yalnız işlemin hukuka aykırı görünmesi yeterlidir; zarar koşulu hiçbir zaman aranmaz",
        "Mahkeme koşulları göstermeden tek cümlelik ara kararla yürütmeyi durdurabilir ve gerekçe yazmak zorunda değildir",
        "Yürütmenin durdurulması istemi yalnız dava açılmadan önce yapılabilir; dava dilekçesinde ileri sürülmesi yasaktır",
        "İtiraz üzerine verilen yürütmenin durdurulması kararı aynı merci önünde sınırsız sayıda yeniden incelenebilir",
        "Atama ve naklen atama işlemleri kanun gereği her zaman uygulanmakla etkisi tükenecek işlem kabul edilir",
        "Vergi davası açılması hiçbir durumda dava konusu tahsil işlemini etkilemez ve yürütmenin durdurulması da istenemez",
        "Aynı sebeplere dayanılarak yürütmenin durdurulması istemi reddedilse bile sınırsız kez tekrarlanabilir",
    ],
    "yol": [
        "İstinaf başvurusu doğrudan Danıştay Genel Kurulunca ilk derece incelemesi yapılarak kesin karara bağlanır",
        "Temyiz incelemesinde Danıştay idarenin takdir yetkisini kullanarak uyuşmazlığa konu yeni işlemi kendisi tesis eder",
        "Kanun yoluna başvurulması ilk derece kararının yürütülmesini her durumda kendiliğinden durdurur",
        "Bölge idare mahkemesi istinafta hukuka aykırı kararı saptasa bile yalnız dosyayı kapatabilir, esas hakkında karar veremez",
        "Kanun yararına bozma daha önce kesinleşmiş kararın taraflar arasındaki bütün hukuki sonuçlarını geriye etkili kaldırır",
        "İvedi yargılama usulündeki kararlar önce istinafa, ardından aynı dosya üzerinden yeniden ilk derece mahkemesine gider",
        "Temyiz yalnız tarafların sözlü beyanıyla yapılır; dilekçe ve kanuni başvuru süresi aranmaz",
        "Yargılamanın yenilenmesi kanunda sayılan sebeplere bağlı değildir ve kesinleşen her karar için süre sınırı olmadan istenebilir",
    ],
}

# Seçenek uzunluğunu cevap anahtarı hâline getirmeyen, konuya yakın çeldiriciler.
WRONG.update({
    "sure": [
        "Süre, işlemin idare içinde imzalandığı gün işlemeye başlar",
        "Bütün idari davalarda değişmez biçimde doksan günlük süre uygulanır",
        "Tatil günleri süre hesabına alınmaz; yalnız çalışma günleri sayılır",
        "Son gün tatile rastlarsa süre önceki çalışma gününde tamamlanır",
        "İdari başvuru, geçmiş dava süresini silerek baştan başlatır",
        "Çalışmaya ara verme bütün süreleri ara verme boyunca durdurur",
        "Görevsiz yargı yerine başvuru tarihi hiçbir durumda korunmaz",
        "Özel kanundaki süre yerine daima İYUK'taki genel süre uygulanır",
    ],
    "yd": [
        "Dava açılması işlemin yürütmesini her durumda kendiliğinden durdurur",
        "Yalnız hukuka aykırılık iddiası yürütmenin durdurulmasına yeterlidir",
        "Yürütmenin durdurulması kararı gerekçe gösterilmeden verilebilir",
        "İstem yalnız dava açılmadan önce ayrı bir başvuruyla ileri sürülebilir",
        "Aynı karara karşı sınırsız sayıda yürütmeyi durdurma itirazı yapılabilir",
        "Vergi davası dava konusu tahsil işlemini hiçbir durumda etkilemez",
        "Kanun yolu başvurusu ilk derece kararını otomatik olarak durdurur",
        "Mahkeme telafisi güç zararı somutlaştırmadan karar vermek zorundadır",
    ],
    "yol": [
        "İstinaf başvurusunu ilk derece mahkemesi esastan ve kesin inceler",
        "Bütün bölge idare mahkemesi kararları sınırsız biçimde temyize açıktır",
        "Kanun yoluna başvuru kararı kendiliğinden yürütülemez hâle getirir",
        "Danıştay temyizde idarenin yerine geçerek yeni idari işlem kurar",
        "Kanun yararına bozma kesin kararın taraflar arasındaki sonucunu kaldırır",
        "İvedi yargılama kararları önce istinaf, sonra temyiz incelemesine gider",
        "Temyiz için dilekçe ve kanuni başvuru süresi aranmaz",
        "Yargılamanın yenilenmesi her memnuniyetsizlik sebebiyle istenebilir",
    ],
})

# Doğru seçeneğin uzunluğunun cevap anahtarına dönüşmesini önlemek için her
# bankada kısa ve uzun, fakat konu bakımından makul yanlış önermeler bulunur.
WRONG["sure"].extend([
    "Süre daima tebliğ günü başlar",
    "Bütün süreler doksan gündür",
    "Tatil günleri hiç sayılmaz",
    "Her idari başvuru süreyi yeniler",
    "Özel kanundaki farklı süre dikkate alınmaz; bütün uyuşmazlıklarda yalnız İYUK'taki genel dava süresi uygulanır",
    "Çalışmaya ara verme, bitiş tarihine bakılmaksızın bütün kanuni ve idari başvuru sürelerini kendiliğinden durdurur",
    "İdarenin sonradan verdiği cevap, zımni ret üzerine tüketilmiş veya geçirilmiş dava süresini hiçbir koşulda etkilemez",
    "Görevsiz yargı yerine yapılan ilk başvurunun tarihi korunmaz; görevli idari yargıda her durumda yeni bir dava süresi başlar",
])
WRONG["yd"].extend([
    "Dava açılması yürütmeyi durdurur",
    "İtiraz için süre aranmaz",
    "Gerekçe gösterilmesi zorunlu değildir",
    "Her işlemde geçici durdurma verilir",
    "Yürütmenin durdurulması için açık hukuka aykırılığın varlığı yeterlidir; telafisi güç veya imkânsız zarar aranmaz",
    "Mahkeme, yürütmenin durdurulması kararında hukuka aykırılık ve zarar koşullarının somut gerekçelerini göstermek zorunda değildir",
    "Vergi mahkemesinde dava açılması, dava konusu edilen bölüm dâhil olmak üzere tahsil işlemlerinin hiçbirini kendiliğinden etkilemez",
    "Yürütmenin durdurulması kararına karşı aynı gerekçelerle ve herhangi bir sayısal sınırlama olmaksızın tekrar tekrar itiraz edilebilir",
])
WRONG["yol"].extend([
    "Her karar temyize açıktır",
    "İstinafı Danıştay inceler",
    "Kanun yolu kararı durdurur",
    "Yenileme sebebe bağlı değildir",
    "İstinaf veya temyiz başvurusu yapılınca ilk derece kararının yürütülmesi ayrıca bir karar aranmadan kendiliğinden durur",
    "Danıştay temyiz incelemesinde idarenin yerine geçerek uyuşmazlığı sona erdirecek yeni bir idari işlem tesis etmekle görevlidir",
    "Kanun yararına bozma, kesinleşen kararın taraflar arasında doğurduğu bütün hukuki sonuçları geçmişe etkili olarak ortadan kaldırır",
    "Yargılamanın yenilenmesi, kanunda sınırlı olarak sayılan sebepler aranmaksızın kesinleşmiş her karar için süresiz biçimde istenebilir",
])


RULES = [
    R("Özel kanunda ayrı süre bulunmayan bir idari işleme karşı idare mahkemesinde dava açılacaktır. Genel süre nedir?", "Danıştay ve idare mahkemelerinde genel dava açma süresi kaç gündür?", "Altmış gün", "sure", "Özel kanunda ayrı süre yoksa Danıştay ve idare mahkemelerinde dava açma süresi altmış gündür.", "2577 sayılı İYUK m.7/1", "easy"),
    R("Özel kanunda ayrı süre bulunmayan vergi tarhiyatına karşı vergi mahkemesinde dava açılacaktır. Genel süre nedir?", "Vergi mahkemelerinde genel dava açma süresi kaç gündür?", "Otuz gün", "sure", "Vergi mahkemelerinde özel kanunda ayrı süre yoksa genel dava açma süresi otuz gündür.", "2577 sayılı İYUK m.7/1", "easy"),
    R("İdari işlem 4 Ağustos günü usulüne uygun yazılı olarak bildirilmiştir. Dava süresi hangi gün işlemeye başlar?", "Yazılı bildirimde dava süresinin başlangıcına ilişkin genel kural hangisidir?", "Bildirimi izleyen gün", "sure", "İdari süreler tebliğ, yayın veya ilan tarihini izleyen günden itibaren işlemeye başlar.", "2577 sayılı İYUK m.7/2, m.8/1"),
    R("Adresi bilinmeyen kişiye özel kanuna uygun ilanla bildirim yapılmış ve özel kanunda aksi düzenlenmemiştir. Süre nasıl başlar?", "İlan yoluyla bildirimde son ilandan sonra uygulanan yapısal bekleme süresi nedir?", "Son ilanı izleyen günden on beş gün sonra", "sure", "Özel kanunda aksi yoksa ilanla bildirimde dava süresi son ilan tarihini izleyen günden on beş gün sonra işlemeye başlar.", "2577 sayılı İYUK m.7/3", "hard"),
    R("İlanı gereken düzenleyici işlem Resmî Gazete'de yayımlanmıştır. Dava süresi hangi tarihten başlar?", "İlanı gereken düzenleyici işlemlerde dava süresinin başlangıcı hangisidir?", "İlan tarihini izleyen gün", "sure", "Düzenleyici işlemlerde dava süresi ilan tarihini izleyen günden itibaren başlar.", "2577 sayılı İYUK m.7/4"),
    R("Dava açma süresinin ortasındaki resmî tatiller hesaplama bakımından nasıl değerlendirilir?", "İYUK'a göre tatil günlerinin sürelere etkisi hangisidir?", "Tatil günleri süreye dâhildir", "sure", "Tatil günleri süre hesabına dâhildir; yalnız son gün tatile rastlarsa uzama olur.", "2577 sayılı İYUK m.8/2", "easy"),
    R("Kanuni sürenin son günü pazar gününe rastlamıştır. Süre ne zaman sona erer?", "Sürenin son gününün tatil olması hâlindeki uzama kuralı hangisidir?", "İzleyen çalışma gününün sonunda", "sure", "Son gün tatilse süre tatili izleyen çalışma gününün bitimine kadar uzar.", "2577 sayılı İYUK m.8/2"),
    R("İYUK'ta yazılı bir sürenin bitişi mahkemelerin çalışmaya ara verme zamanına rastlamıştır. Kanuni sonuç nedir?", "Çalışmaya ara vermeye rastlayan İYUK süreleri ne kadar uzamış sayılır?", "Ara vermenin bitimini izleyen tarihten yedi gün", "sure", "İYUK'ta yazılı süre, çalışmaya ara vermenin sona erdiği günü izleyen tarihten itibaren yedi gün uzamış sayılır.", "2577 sayılı İYUK m.8/3", "hard"),
    R("Adli yargıdaki dava görev yönünden reddedilmiş ve karar kesinleşmiştir. İdari yargıda başvuru için tanınan yapısal süre nedir?", "Görevsiz adli yargı kararının kesinleşmesinden sonra idari dava açma süresi kaç gündür?", "Otuz gün", "sure", "Görevsizlik kararının kesinleşmesini izleyen günden itibaren otuz gün içinde görevli idari yargı yerinde dava açılabilir.", "2577 sayılı İYUK m.9"),
    R("Kişi, hakkında dava konusu olabilecek bir işlemin yapılması için idareye başvurmuş; idare cevap vermemiştir. İstek ne zaman reddedilmiş sayılır?", "İYUK m.10 başvurusunda zımni ret süresi kaç gündür?", "Otuz gün", "sure", "İYUK m.10'a göre otuz gün içinde cevap verilmezse istek reddedilmiş sayılır.", "2577 sayılı İYUK m.10/2"),
    R("İYUK m.10 başvurusuna otuz gün içinde kesin olmayan cevap verilmiştir. İlgili kesin cevabı beklemek isterse azami bekleme süresi nedir?", "Kesin olmayan cevaptan sonra kesin cevabı bekleme süresinin üst sınırı nedir?", "Başvuru tarihinden itibaren dört ay", "sure", "Kesin olmayan cevapta dava süresi işlemez; ancak bekleme başvuru tarihinden itibaren dört ayı geçemez.", "2577 sayılı İYUK m.10/2", "hard"),
    R("İYUK m.10 başvurusunda zımni ret sonrası dava açılmamış; idare daha sonra açık cevap vermiştir. Yeni dava imkânı nasıl doğar?", "Zımni retten sonra gelen geç cevaba karşı öngörülen dava süresi nedir?", "Cevabın tebliğinden itibaren altmış gün", "sure", "Zımni ret sonrasında yetkili makam cevap verirse, cevabın tebliğinden itibaren altmış gün içinde dava açılabilir.", "2577 sayılı İYUK m.10/2", "hard"),
    R("Kişi dava açmadan önce işlemin kaldırılmasını üst makamdan istemek istemektedir. Başvuru ne zaman yapılmalıdır?", "İYUK m.11 kapsamındaki idari başvurunun zaman koşulu hangisidir?", "Dava açma süresi içinde", "sure", "Üst makama veya üst makam yoksa işlemi yapan makama başvuru, dava açma süresi içinde yapılmalıdır.", "2577 sayılı İYUK m.11/1"),
    R("İYUK m.11 uyarınca süresinde üst makama başvurulmuştur. İşlemekte olan dava açma süresine etkisi nedir?", "Üst makama başvurunun dava açma süresine etkisi hangisidir?", "Dava açma süresini durdurur", "sure", "Süresinde yapılan m.11 başvurusu işlemeye başlamış dava açma süresini durdurur.", "2577 sayılı İYUK m.11/1", "easy"),
    R("Üst makam, işlemin kaldırılması başvurusuna cevap vermemiştir. Başvuru ne zaman reddedilmiş sayılır?", "İYUK m.11 başvurusundaki zımni ret süresi kaç gündür?", "Otuz gün", "sure", "Üst makam başvurusuna otuz gün içinde cevap verilmezse istek reddedilmiş sayılır.", "2577 sayılı İYUK m.11/2"),
    R("İYUK m.11 başvurusu reddedilmiş ve dava süresi yeniden işlemeye başlamıştır. Başvurudan önce geçen süreye ne olur?", "M.11 başvurusunun reddinden sonra kalan dava süresi nasıl hesaplanır?", "Başvurudan önce geçen süre hesaba katılır", "sure", "Ret veya zımni ret üzerine süre yeniden işler; başvuru tarihine kadar geçmiş olan süre de toplam hesaba dâhil edilir.", "2577 sayılı İYUK m.11/3", "hard"),
    R("Bir idari işleme karşı iptal davası açılmıştır. Yalnız dava açılması işlemin uygulanmasını durdurur mu?", "İdari dava açılmasının işlemin yürütmesine genel etkisi hangisidir?", "Yürütmeyi kendiliğinden durdurmaz", "yd", "İdari dava açılması, kanundaki özel hâller dışında işlemin yürütülmesini kendiliğinden durdurmaz.", "2577 sayılı İYUK m.27/1", "easy"),
    R("İşlem açıkça hukuka aykırıdır ancak uygulanması telafisi güç zarar doğurmayacaktır. Genel kurala göre yürütme durdurulabilir mi?", "Yürütmenin durdurulması için birlikte gerçekleşmesi gereken iki koşul hangisidir?", "Açık hukuka aykırılık ve telafisi güç zarar", "yd", "Genel yürütmenin durdurulması kararı için açık hukuka aykırılık ile telafisi güç veya imkânsız zarar koşulları birlikte gerekir.", "2577 sayılı İYUK m.27/2"),
    R("Mahkeme yürütmenin durdurulmasına karar verirken yalnız 'koşullar oluşmuştur' demiştir. Kararda ayrıca ne gösterilmelidir?", "Yürütmenin durdurulması kararının gerekçe içeriği için zorunlu olan nedir?", "Hukuka aykırılık ve telafisi güç zarar somutlaştırılmalıdır", "yd", "Kararda işlemin hangi gerekçelerle açıkça hukuka aykırı olduğu ve doğacak telafisi güç zararın ne olduğu belirtilmelidir.", "2577 sayılı İYUK m.27/2"),
    R("Uygulanmakla etkisi tükenecek işlem için acil yürütmenin durdurulması istenmiştir. Savunma alınmadan geçici karar mümkün müdür?", "Uygulanmakla etkisi tükenecek işlemde savunma alınmadan verilen kararın niteliği hangisidir?", "Savunmadan sonra yeniden karar verilmek üzere durdurulabilir", "yd", "Etkisi uygulanmakla tükenecek işlemin yürütmesi, savunma alındıktan sonra yeniden karar verilmek üzere savunma öncesinde durdurulabilir.", "2577 sayılı İYUK m.27/2", "hard"),
    R("Tarh edilen vergiye karşı vergi mahkemesinde dava açılmıştır. Dava konusu bölümün tahsil işlemi kural olarak ne olur?", "Vergi davasının dava konusu tahsil işlemine genel etkisi hangisidir?", "Tahsil işlemi durur", "yd", "Vergi mahkemesinde vergi uyuşmazlığından doğan davanın açılması, dava konusu edilen bölümün tahsil işlemini kural olarak durdurur.", "2577 sayılı İYUK m.27/4"),
    R("İdare mahkemesinin yürütmenin durdurulması kararına karşı başvuru yapılacaktır. Genel itiraz süresi ve sayısı nedir?", "Yürütmenin durdurulması kararına itirazın yapısal sınırı hangisidir?", "Yedi gün içinde bir defa", "yd", "Yürütmenin durdurulması kararına tebliği izleyen günden itibaren yedi gün içinde bir defaya mahsus itiraz edilebilir.", "2577 sayılı İYUK m.27/7"),
    R("İdare mahkemesi kararı olağan istinafa açıktır. Başvuru hangi süre içinde ve nereye yapılır?", "İstinaf başvurusunun genel süresi ve inceleme mercii hangisidir?", "Otuz gün içinde bölge idare mahkemesine", "yol", "İstinaf, kararın tebliğinden itibaren otuz gün içinde mahkemenin bulunduğu çevredeki bölge idare mahkemesine yapılır.", "2577 sayılı İYUK m.45/1", "easy"),
    R("Bölge idare mahkemesinin İYUK m.46'da sayılan temyize açık kararına başvurulacaktır. Genel süre ve merci hangisidir?", "İdari yargıda temyizin genel süresi ve inceleme mercii hangisidir?", "Otuz gün içinde Danıştaya", "yol", "İYUK m.46 kapsamındaki kararlar tebliğden itibaren otuz gün içinde Danıştayda temyiz edilebilir.", "2577 sayılı İYUK m.46"),
    R("İlk derece kararı hakkında istinaf başvurusu yapılmıştır. Başvuru tek başına kararın yürütülmesini durdurur mu?", "İstinaf veya temyiz başvurusunun kararın yürütmesine genel etkisi hangisidir?", "Kendiliğinden durdurmaz", "yol", "İstinaf veya temyiz yoluna başvurulması, mahkeme kararının yürütülmesini kendiliğinden durdurmaz; ayrıca karar gerekir.", "2577 sayılı İYUK m.52/1"),
    R("Kesinleşmiş bir karar kanun yararına temyiz sonucunda bozulmuştur. Bu bozmanın taraflar arasındaki önceki sonuca etkisi nedir?", "Kanun yararına bozmanın kesinleşmiş merci kararına etkisi hangisidir?", "Kesinleşmiş kararın hukuki sonuçlarını kaldırmaz", "yol", "Kanun yararına bozma, hukuka aykırılığı giderici içtihat işlevi görür; daha önce kesinleşen kararın taraflar bakımından sonuçlarını kaldırmaz.", "2577 sayılı İYUK m.51/2", "hard"),
]


def F(correct, focus, focus_correct, focus_why, focus_ref=None, focus_difficulty=None):
    item = {
        "correct": correct,
        "focus": focus,
        "focus_correct": focus_correct,
        "focus_why": focus_why,
    }
    if focus_ref:
        item["focus_ref"] = focus_ref
    if focus_difficulty:
        item["focus_difficulty"] = focus_difficulty
    return item


VARIANTS = [
    F("Genel dava açma süresi, yazılı bildirimi izleyen günden itibaren altmış gündür", "İdare mahkemesindeki altmış günlük genel sürenin uygulanmasını engelleyen durum hangisidir?", "Özel kanunda uyuşmazlık için ayrı bir dava açma süresinin gösterilmiş olması", "İYUK m.7/1'deki altmış gün, özel kanunda ayrı süre bulunmayan hâller içindir; özel süre genel süreden önce uygulanır.", "2577 sayılı İYUK m.7/1"),
    F("Vergi mahkemesinde genel dava açma süresi otuz gündür", "Vergi mahkemesindeki otuz günlük genel süre hangi kayıtla uygulanır?", "Uyuşmazlığa ilişkin özel kanunda farklı bir süre bulunmaması kaydıyla", "Vergi mahkemesindeki otuz günlük süre de tamamlayıcı genel süredir; özel kanundaki farklı süre saklıdır.", "2577 sayılı İYUK m.7/1"),
    F("Süre, yazılı bildirimin yapıldığı günü izleyen gün işlemeye başlar", "Yazılı bildirim günü süre hesabına dâhil edilir mi?", "Hayır; başlangıç bildirimi izleyen gündür", "İYUK m.8/1 uyarınca tebliğ, yayın veya ilan günü sayılmaz; süre bunları izleyen günden başlar.", "2577 sayılı İYUK m.8/1", "easy"),
    F("Süre, son ilan tarihini izleyen günden on beş gün sonra işlemeye başlar", "İlanla bildirimde on beş günlük bekleme kuralı hangi durumda uygulanmaz?", "Özel kanunun ilanla bildirim için farklı bir başlangıç öngörmesi hâlinde", "İYUK m.7/3 açıkça özel kanundaki aksi hükmü saklı tutar; on beş günlük yapı tamamlayıcı kuraldır.", "2577 sayılı İYUK m.7/3", "hard"),
    F("Dava süresi, düzenleyici işlemin ilan tarihini izleyen gün başlar", "Düzenleyici işlemin doğrudan dava süresi geçirilirse daha sonraki uygulama ne sağlar?", "Uygulama üzerine düzenleyici işlem veya uygulama işlemi süresinde dava edilebilir", "İYUK m.7/4, ilan süresi geçirilmiş düzenleyici işlemin uygulanması üzerine düzenleyici ve/veya uygulama işlemine dava açma olanağı tanır.", "2577 sayılı İYUK m.7/4"),
    F("Resmî tatil günleri kanuni sürenin hesabına dâhildir", "Tatil günlerinin süreye dâhil olması hangi istisnayla birlikte uygulanır?", "Sürenin son günü tatile rastlarsa bitiş izleyen çalışma gününe uzar", "Ara günlerdeki tatiller sayılır; yalnız son gün tatilse m.8/2 uyarınca izleyen çalışma günü sonuna uzama olur.", "2577 sayılı İYUK m.8/2"),
    F("Süre, tatili izleyen çalışma gününün bitiminde sona erer", "Son günün tatil olması süreyi tatilden önceki güne çeker mi?", "Hayır; süre tatili izleyen çalışma gününün sonuna kadar devam eder", "İYUK m.8/2 hak kaybını önlemek için son gün tatilse süreyi sonraki çalışma gününün bitimine uzatır.", "2577 sayılı İYUK m.8/2", "easy"),
    F("Süre, ara vermenin bitimini izleyen tarihten başlayarak yedi gün uzamış sayılır", "Çalışmaya ara verme kuralı bütün mevzuat sürelerini kendiliğinden uzatır mı?", "Hayır; İYUK'ta yazılı ve bitimi ara vermeye rastlayan süreler için uygulanır", "M.8/3 yalnız İYUK'ta yazılı sürenin bitişi çalışmaya ara vermeye rastladığında yedi günlük uzama getirir.", "2577 sayılı İYUK m.8/3", "hard"),
    F("Kesinleşmeyi izleyen günden itibaren otuz gün içinde idari yargıda dava açılabilir", "Görevsiz adli yargıya yapılan ilk başvurunun tarihi korunur mu?", "Evet; ilk başvuru tarihi idari yargıya başvuru tarihi sayılır", "İYUK m.9 hem kesinleşmeden sonra otuz günlük geçiş süresi verir hem de görevsiz yargı yerine başvuru tarihini korur.", "2577 sayılı İYUK m.9"),
    F("İdare otuz gün cevap vermezse istek reddedilmiş sayılır", "İYUK m.10'daki otuz günlük zımni ret süresi sonunda ne başlar?", "Görevli mahkemenin uyuşmazlık için öngörülen dava açma süresi", "Otuz günlük sessizlik zımni ret işlemini oluşturur; ardından uyuşmazlığa göre genel veya özel dava açma süresi işler.", "2577 sayılı İYUK m.10/2; 7331 sayılı Kanun m.1"),
    F("Kesin cevabı bekleme süresi başvuru tarihinden itibaren dört ayı geçemez", "Kesin olmayan cevap alan ilgili hangi iki yoldan birini seçebilir?", "Cevabı ret sayarak dava açabilir veya dört aylık üst sınıra kadar kesin cevabı bekleyebilir", "M.10/2 kesin olmayan cevapta seçim tanır; bekleme sırasında dava süresi işlemez, ancak toplam bekleme dört ayı aşamaz.", "2577 sayılı İYUK m.10/2", "hard"),
    F("Geç açık cevap, tebliğinden itibaren görevli mahkemenin dava süresini yeniden başlatır", "Zımni ret üzerine dava açılmaması geç açık cevabı yargı denetimi dışında bırakır mı?", "Hayır; geç cevabın tebliği yeni bir dava açma imkânı doğurur", "M.10/2, zımni retten sonra dava açılmamış veya dava süreden reddedilmişse sonradan verilen açık cevaba karşı yeni süre tanır.", "2577 sayılı İYUK m.10/2", "hard"),
    F("Başvuru, işlemekte olan dava açma süresi dolmadan yapılmalıdır", "İYUK m.11 başvurusunda idareden hangi işlemler istenebilir?", "İşlemin kaldırılması, geri alınması, değiştirilmesi veya yeni işlem yapılması", "M.11/1 üst makamdan, yoksa işlemi yapan makamdan dört seçimlik idari tasarruftan birinin istenmesine izin verir.", "2577 sayılı İYUK m.11/1"),
    F("Süresinde yapılan başvuru işlemekte olan dava açma süresini durdurur", "İYUK m.11 başvurusu geçmiş süreyi silip süreyi baştan başlatır mı?", "Hayır; başvuru yalnız kalan sürenin işlemesini durdurur", "M.11 başvurusu süreyi kesip sıfırlamaz; ret sonrasında başvurudan önce geçen günler hesaba katılarak kalan süre işler.", "2577 sayılı İYUK m.11/1-3"),
    F("Üst makam otuz gün cevap vermezse başvuru zımnen reddedilmiş sayılır", "İYUK m.11'deki zımni ret süresi hangi değişiklikle otuz güne indirilmiştir?", "7331 sayılı Kanunla altmış günden otuz güne indirilmiştir", "7331 sayılı Kanun m.2, m.11/2'deki eski altmış günlük cevap süresini otuz gün olarak değiştirmiştir.", "2577 sayılı İYUK m.11/2; 7331 sayılı Kanun m.2", "easy"),
    F("Retten sonra süre kaldığı yerden işler ve başvurudan önce geçen günler hesaba katılır", "M.11 başvurusundan önce dava süresinin yirmi günü geçmişse ret sonrası bu günler yok sayılır mı?", "Hayır; geçen yirmi gün toplam dava süresinden düşülür", "M.11/3 uyarınca başvurudan önce geçen süre korunur; ret veya zımni ret üzerine yalnız kalan bölüm işlemeye devam eder.", "2577 sayılı İYUK m.11/3", "hard"),
    F("Yalnız dava açılması işlemin yürütmesini kendiliğinden durdurmaz", "Dava açılmasının yürütmeyi durdurmaması kuralının açık kanuni istisnası hangisidir?", "Vergi mahkemesinde dava konusu edilen vergi bölümünün tahsil işleminin durması", "M.27/1 genel olarak otomatik durmayı reddeder; m.27/4 vergi davalarında dava konusu bölümün tahsilini kural olarak durdurur.", "2577 sayılı İYUK m.27/1, m.27/4"),
    F("Hayır; açık hukuka aykırılık ve telafisi güç zarar koşulları birlikte aranır", "Yürütmenin durdurulmasındaki iki koşul alternatif midir?", "Hayır; her iki koşulun somut olayda birlikte gerçekleşmesi gerekir", "M.27/2 kümülatif iki koşul öngörür; yalnız hukuka aykırılık veya yalnız zarar iddiası genel kuralda yeterli değildir.", "2577 sayılı İYUK m.27/2"),
    F("Kararda açık hukuka aykırılık ve telafisi güç zarar ayrı ayrı somutlaştırılmalıdır", "Yürütmenin durdurulması kararında kalıp bir gerekçe yeterli midir?", "Hayır; işlemin hukuka aykırılığı ve doğacak zarar somut gerekçelerle gösterilmelidir", "M.27/2, iki koşulun hangi gerekçelerle gerçekleştiğinin kararda belirtilmesini zorunlu kılar.", "2577 sayılı İYUK m.27/2"),
    F("Savunma alındıktan sonra yeniden karar verilmek üzere geçici olarak durdurulabilir", "Savunma alınmadan geçici durdurma hangi işlem grubunda mümkündür?", "Uygulanmakla etkisi tükenecek idari işlemlerde", "M.27/2, uygulanmakla etkisi tükenecek işlemlerde savunma beklenirken geri dönülmez sonuç doğmasını önleyen geçici mekanizma kurar.", "2577 sayılı İYUK m.27/2", "hard"),
    F("Dava konusu edilen vergi bölümünün tahsil işlemi kural olarak durur", "Vergi davasındaki otomatik durma dava konusu edilmeyen vergi bölümünü de kapsar mı?", "Hayır; etki yalnız dava konusu edilen bölümün tahsil işlemi üzerindedir", "İYUK m.27/4 otomatik durmayı vergi uyuşmazlığında dava konusu yapılan bölümle sınırlar.", "2577 sayılı İYUK m.27/4"),
    F("Karara karşı tebliği izleyen günden itibaren yedi gün içinde bir defa itiraz edilir", "Yürütmenin durdurulması itirazı üzerine verilen kararın niteliği nedir?", "İtiraz üzerine verilen karar kesindir", "M.27/7 itirazı bir defayla sınırlar ve itiraz merciinin kararını kesin sayar.", "2577 sayılı İYUK m.27/7"),
    F("Kararın tebliğinden itibaren otuz gün içinde bölge idare mahkemesine istinaf edilir", "İstinaf dilekçesi doğrudan inceleme merciine verilmek zorunda mıdır?", "Hayır; kanun yolu dilekçeleri kararı veren mahkemeye de verilebilir", "İstinafta inceleme BİM tarafından yapılır; başvuru usulünde m.48'in temyiz dilekçesine ilişkin hükümleri uygulanır.", "2577 sayılı İYUK m.45/1-2, m.48"),
    F("Temyize açık karar, tebliğden itibaren otuz gün içinde Danıştayda temyiz edilir", "Her bölge idare mahkemesi kararı temyiz edilebilir mi?", "Hayır; temyiz yolu İYUK m.46'da sayılan kararlarla sınırlıdır", "İstinaf genel, temyiz ise m.46'da sayılan uyuşmazlıklar bakımından açık kanun yoludur.", "2577 sayılı İYUK m.46", "medium"),
    F("İstinaf veya temyiz başvurusu kararın yürütülmesini kendiliğinden durdurmaz", "Kanun yolu aşamasında kararın yürütülmesi ayrıca durdurulabilir mi?", "Evet; kanundaki koşullarla yürütmenin durdurulmasına ayrıca karar verilebilir", "M.52/1 otomatik durmayı reddeder, fakat teminat ve m.27 koşulları çerçevesinde ayrıca durdurma kararı verilmesine izin verir.", "2577 sayılı İYUK m.52/1"),
    F("Kanun yararına bozma kesin kararın taraflar arasındaki hukuki sonuçlarını kaldırmaz", "Kanun yararına bozma kararının yayımlanmasının temel işlevi nedir?", "Benzer hukuka aykırılıkların tekrarlanmasını önleyecek içtihat yönlendirmesi sağlamak", "Kanun yararına temyiz, taraflar yönünden kesin sonucu değiştirmeden hukuka aykırılığı ortaya koyup kararın Resmî Gazete'de yayımlanmasını sağlar.", "2577 sayılı İYUK m.51", "hard"),
]

assert len(VARIANTS) == len(RULES) == 26
for rule, variant in zip(RULES, VARIANTS):
    rule.update(variant)


def length_balanced_distractors(correct, bank):
    """Doğru cevabın iki yanında ikişer uzunlukta çeldirici seçer."""
    shorter = sorted((x for x in bank if len(x) < len(correct)), key=len, reverse=True)
    longer = sorted((x for x in bank if len(x) > len(correct)), key=len)
    assert len(shorter) >= 2 and len(longer) >= 2, correct
    return shorter[:2] + longer[:2]


for rule in RULES:
    bank = WRONG[rule["bank"]]
    rule["scenario_distractors"] = length_balanced_distractors(rule["correct"], bank)
    rule["focus_distractors"] = length_balanced_distractors(rule["focus_correct"], bank)


PREMISES = [
    {"stem": "Dava açma süreleri bakımından hangileri doğrudur?\n\nI. İdare mahkemesinde genel süre altmış gündür\n\nII. Vergi mahkemesinde genel süre otuz gündür\n\nIII. Özel kanun farklı süre öngörebilir", "correct": "I, II ve III", "why": "İYUK m.7'deki altmış ve otuz günlük süreler, özel kanunda ayrı süre gösterilmeyen hâllerde uygulanır.", "ref": "2577 sayılı İYUK m.7/1"},
    {"stem": "Süre hesabı bakımından hangileri doğrudur?\n\nI. Süre bildirimi izleyen gün başlar\n\nII. Tatil günleri süre hesabının dışında tutulur\n\nIII. Son gün tatilse süre izleyen çalışma gününe uzar", "correct": "I ve III", "why": "Süre bildirimi izleyen gün başlar; tatiller hesaba katılır ve yalnız son gün tatilse süre izleyen çalışma gününe uzar.", "ref": "2577 sayılı İYUK m.8"},
    {"stem": "İYUK m.11 başvurusu bakımından hangileri doğrudur?\n\nI. Dava açma süresi içinde yapılır\n\nII. Dava açma süresini baştan başlatır\n\nIII. Retten sonra başvurudan önce geçen süre hesaba katılır", "correct": "I ve III", "why": "Başvuru dava açma süresi içinde yapılır ve süreyi yalnız durdurur; ret sonrası başvurudan önce geçen süre hesaba katılır.", "ref": "2577 sayılı İYUK m.11"},
    {"stem": "Yürütmenin durdurulması bakımından hangileri doğrudur?\n\nI. Dava açılması kural olarak yürütmeyi durdurmaz\n\nII. Açık hukuka aykırılık ile telafisi güç zarar birlikte aranır\n\nIII. Kararda iki koşulun gerekçesi gösterilir", "correct": "I, II ve III", "why": "Üç ifade de yürütmenin durdurulmasına ilişkin genel sistemi doğru açıklar.", "ref": "2577 sayılı İYUK m.27"},
    {"stem": "Yürütmenin durdurulmasına itiraz bakımından hangileri doğrudur?\n\nI. İtiraz üzerine verilen karar aynı yolla sınırsız incelenebilir\n\nII. Tebliği izleyen günden itibaren yedi günlük süre vardır\n\nIII. İtiraz bir defaya mahsustur", "correct": "II ve III", "why": "İtiraz yedi gün içinde ve bir defa yapılabilir; itiraz üzerine verilen karar kesindir.", "ref": "2577 sayılı İYUK m.27/7"},
    {"stem": "Kanun yolları bakımından hangileri doğrudur?\n\nI. İstinafın genel süresi otuz gündür\n\nII. Temyizin genel süresi otuz gündür\n\nIII. Her istinaf kararı parasal sınıra bakılmaksızın temyize açıktır", "correct": "I ve II", "why": "İstinaf ve temyiz için genel süre otuz gündür; her bölge idare mahkemesi kararı temyize açık değildir.", "ref": "2577 sayılı İYUK m.45-46"},
    {"stem": "Temyiz incelemesi sonunda Danıştay hangilerini yapabilir?\n\nI. Hukuka uygun kararı onayabilir\n\nII. İdarenin yerine geçerek yeni idari işlem kurabilir\n\nIII. Her usul eksikliğinde, sonuca etkisine bakmadan kararı bozmak zorundadır", "correct": "Yalnız I", "why": "Danıştay hukuka uygun kararı onayabilir; idari işlem tesis edemez ve ancak karara etkili usul ihlali bozma sebebi olabilir.", "ref": "2577 sayılı İYUK m.49"},
    {"stem": "Yargılamanın yenilenmesi bakımından hangileri doğrudur?\n\nI. Her memnuniyetsizlik tek başına yenileme sebebidir\n\nII. Kanunda sayılan sebeplere dayanır\n\nIII. Esas kararı vermiş mahkemece incelenir", "correct": "II ve III", "why": "Yargılamanın yenilenmesi olağanüstü ve sınırlı sebeplere bağlıdır; esas kararı veren mahkeme inceler.", "ref": "2577 sayılı İYUK m.53"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="idari_yargilama_hukuku", topic_id="idari_yargida_sureler_kanun_yollari",
        label="Süreler ve Kanun Yolları", slug="idari_yargida_sureler_kanun_yollari",
        prefix="kh-iy-sure", seed=20261003, legislation_version="2577 sayılı İYUK (17.07.2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
