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


PREMISES = [
    {"stem": "Dava açma süreleri bakımından hangileri doğrudur?\n\nI. İdare mahkemesinde genel süre altmış gündür\n\nII. Vergi mahkemesinde genel süre otuz gündür\n\nIII. Özel kanun farklı süre öngörebilir", "correct": "I, II ve III", "why": "İYUK m.7'deki altmış ve otuz günlük süreler, özel kanunda ayrı süre gösterilmeyen hâllerde uygulanır.", "ref": "2577 sayılı İYUK m.7/1"},
    {"stem": "Süre hesabı bakımından hangileri doğrudur?\n\nI. Süre bildirimi izleyen gün başlar\n\nII. Tatil günleri süreye dâhildir\n\nIII. Son gün tatilse süre önceki gün sona erer", "correct": "I ve II", "why": "Süre izleyen gün başlar ve tatiller hesaba katılır; son gün tatilse izleyen çalışma gününe uzar.", "ref": "2577 sayılı İYUK m.8"},
    {"stem": "İYUK m.11 başvurusu bakımından hangileri doğrudur?\n\nI. Dava açma süresi içinde yapılır\n\nII. İşleyen dava süresini durdurur\n\nIII. Retten sonra başvurudan önce geçen süre hesaba katılmaz", "correct": "I ve II", "why": "Başvuru süresinde yapılır ve dava süresini durdurur; ret sonrası önce geçen süre hesaba katılır.", "ref": "2577 sayılı İYUK m.11"},
    {"stem": "Yürütmenin durdurulması bakımından hangileri doğrudur?\n\nI. Dava açılması kural olarak yürütmeyi durdurmaz\n\nII. Açık hukuka aykırılık ile telafisi güç zarar birlikte aranır\n\nIII. Kararda iki koşulun gerekçesi gösterilir", "correct": "I, II ve III", "why": "Üç ifade de yürütmenin durdurulmasına ilişkin genel sistemi doğru açıklar.", "ref": "2577 sayılı İYUK m.27"},
    {"stem": "Yürütmenin durdurulmasına itiraz bakımından hangileri doğrudur?\n\nI. Tebliği izleyen günden itibaren yedi günlük süre vardır\n\nII. İtiraz bir defaya mahsustur\n\nIII. İtiraz üzerine verilen karar yeniden aynı yolla sınırsız incelenir", "correct": "I ve II", "why": "İtiraz yedi gün içinde ve bir defa yapılabilir; itiraz üzerine verilen karar kesindir.", "ref": "2577 sayılı İYUK m.27/7"},
    {"stem": "Kanun yolları bakımından hangileri doğrudur?\n\nI. İstinafın genel süresi otuz gündür\n\nII. Temyizin genel süresi otuz gündür\n\nIII. Her istinaf kararı parasal sınıra bakılmaksızın temyize açıktır", "correct": "I ve II", "why": "İstinaf ve temyiz için genel süre otuz gündür; her bölge idare mahkemesi kararı temyize açık değildir.", "ref": "2577 sayılı İYUK m.45-46"},
    {"stem": "Temyiz incelemesi sonunda Danıştay hangilerini yapabilir?\n\nI. Hukuka uygun kararı onayabilir\n\nII. Etkili usul hatası varsa bozabilir\n\nIII. İdarenin yerine geçerek yeni idari işlem kurabilir", "correct": "I ve II", "why": "Danıştay hukuka uygun kararı onar, kanundaki bozma sebeplerinde bozar; idari işlem tesis etmez.", "ref": "2577 sayılı İYUK m.49"},
    {"stem": "Yargılamanın yenilenmesi bakımından hangileri doğrudur?\n\nI. Kanunda sayılan sebeplere dayanır\n\nII. Esas kararı vermiş mahkemece incelenir\n\nIII. Her memnuniyetsizlik tek başına yenileme sebebidir", "correct": "I ve II", "why": "Yargılamanın yenilenmesi olağanüstü ve sınırlı sebeplere bağlıdır; esas kararı veren mahkeme inceler.", "ref": "2577 sayılı İYUK m.53"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="idari_yargilama_hukuku", topic_id="idari_yargida_sureler_kanun_yollari",
        label="Süreler ve Kanun Yolları", slug="idari_yargida_sureler_kanun_yollari",
        prefix="kh-iy-sure", seed=20261003, legislation_version="2577 sayılı İYUK (16.07.2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
