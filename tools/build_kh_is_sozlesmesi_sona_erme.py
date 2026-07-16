#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İş Sözleşmesinin Sona Ermesi — 4857, 1475 m.14 ve TBK m.420."""
from topic_pack_builder import write_topic


def R(scenario, focus, correct, bank, why, ref, difficulty="medium"):
    return locals()


WRONG = {
    "bildirim": [
        "Bildirim süreleri yalnız belirli süreli sözleşmelerde uygulanır ve tarafların anlaşmasıyla azaltılması zorunludur",
        "İhbar önellerine uymayan tarafın hiçbir parasal sorumluluğu doğmaz; fesih bildirildiği anda sonuçlanır",
        "İşveren bildirim süresi ücretini peşin ödese bile sözleşmeyi sona erdiremez ve işçiyi fiilen çalıştırmak zorundadır",
        "Kanundaki bildirim süreleri azami sürelerdir; iş sözleşmesiyle işçi aleyhine serbestçe kısaltılabilir",
        "Yeni iş arama izni yalnız iş saatleri dışında ve işçinin ücretinden kesinti yapılarak kullandırılabilir",
        "İşçinin kıdemi bildirim süresini etkilemez; bütün belirsiz süreli sözleşmeler için tek haftalık önel uygulanır",
        "Bildirimli fesih hakkı yalnız işverene aittir; işçi belirsiz süreli sözleşmesini bildirimle sona erdiremez",
        "İhbar tazminatı hesabında para ile ölçülebilen düzenli sözleşmesel menfaatler hiçbir koşulda dikkate alınmaz",
    ],
    "guvence": [
        "İş güvencesi bütün belirli süreli sözleşmelerde işçi sayısı ve kıdem aranmadan kendiliğinden uygulanır",
        "Fesih sebebini ispat yükü her durumda yalnız işçiye aittir; işverenin geçerli sebebi kanıtlama görevi bulunmaz",
        "İşe iade talebi için arabuluculuk yolu kapalıdır ve fesih tarihinden sonra sınırsız süre içinde doğrudan dava açılır",
        "İşveren davranış veya verim gerekçeli fesihte hiçbir zaman savunma almak zorunda değildir",
        "Geçersiz fesih kararı işçiyi başvuru yapmadan otomatik olarak işe döndürür ve süre koşulu aranmaz",
        "Sendika üyeliği ve mevzuattan doğan hakkı arama, belirsiz süreli sözleşmenin geçerli fesih sebebi sayılır",
        "İşe başlatmama tazminatı tarafların önceden yaptığı sözleşmeyle kanuni sınırların altına indirilebilir",
        "İş güvencesinde işyerindeki işçi sayısı aynı işkolundaki diğer işyerleri dikkate alınmadan yalnız tek şubede sayılır",
    ],
    "derhal": [
        "Haklı nedenle derhâl fesihte de bütün bildirim önellerinin sonuna kadar iş ilişkisinin sürdürülmesi zorunludur",
        "Ücretin sözleşmeye uygun ödenmemesi işçiye hiçbir fesih hakkı vermez ve yalnız idari para cezası doğurur",
        "İşçinin işverenin güvenini kötüye kullanması işveren bakımından geçerli sebep dahi oluşturamaz",
        "Ahlak ve iyi niyet olaylarında haklı fesih hakkı olay öğrenildikten sonra süre sınırı olmadan kullanılabilir",
        "İşyerinde bir haftadan fazla işin durmasına yol açan zorlayıcı sebep yalnız işverene fesih hakkı tanır",
        "İşçinin izinsiz ve haklı sebep olmadan kanundaki düzeyde devamsızlığı işverenin derhâl fesih hakkını etkilemez",
        "Haklı nedenle fesih yalnız belirsiz süreli sözleşmede mümkündür; belirli süreli sözleşmelerde uygulanamaz",
        "Maddi çıkar sağlanan olayda altı iş günlük öğrenme süresi de uygulanmaz ve hak sınırsız hâle gelir",
    ],
    "sonuc": [
        "İbraname sözlü yapılabilir; alacak türü, miktarı ve banka ödemesi konusunda hiçbir şekil koşulu aranmaz",
        "İş sözleşmesinin sona erdiği gün alınan genel ve miktarsız ibra beyanı bütün işçilik alacaklarını kesin sona erdirir",
        "Kıdem tazminatı bütün istifa hâllerinde sebep aranmaksızın ve bir yıllık kıdem koşulu olmadan ödenir",
        "İşe iade kararı kesinleştiğinde işçinin işverene başvurmasına gerek kalmadan tazminat ve ücret otomatik doğar",
        "İşçi işe başlatılırsa daha önce peşin ödenen bildirim ücreti ve kıdem tazminatı hiçbir şekilde mahsup edilemez",
        "İşveren iş arama iznini kullandırmadığında o süreye ilişkin ücret dâhil hiçbir ödeme yapmak zorunda değildir",
        "İşçinin ölümü iş sözleşmesini sona erdirmez; sözleşme aynı koşullarla mirasçılar tarafından sürdürülmek zorundadır",
        "Kıdem tazminatı her hizmet yılı için yalnız çıplak ücretin on günlük kısmıyla sınırlı hesaplanır",
    ],
}


RULES = [
    R("Dört aydır çalışan işçinin belirsiz süreli sözleşmesi bildirimli feshedilecektir. Asgari bildirim öneli nedir?", "Kıdemi altı aydan az işçi için kanuni ihbar öneli kaç haftadır?", "İki hafta", "bildirim", "İşi altı aydan az sürmüş işçi için bildirimden başlayarak iki haftalık önel uygulanır.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("Bir yıldır çalışan işçinin belirsiz süreli sözleşmesi bildirimli feshedilecektir. Asgari önel nedir?", "Kıdemi altı ay ile bir buçuk yıl arasında olan işçinin ihbar öneli kaç haftadır?", "Dört hafta", "bildirim", "Altı aydan bir buçuk yıla kadar kıdemde asgari bildirim süresi dört haftadır.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("İki yıldır çalışan işçinin belirsiz süreli sözleşmesi bildirimli feshedilecektir. Asgari önel nedir?", "Kıdemi bir buçuk yıl ile üç yıl arasında olan işçinin ihbar öneli kaç haftadır?", "Altı hafta", "bildirim", "Bir buçuk yıldan üç yıla kadar kıdemde asgari bildirim süresi altı haftadır.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("Dört yıldır çalışan işçinin belirsiz süreli sözleşmesi bildirimli feshedilecektir. Asgari önel nedir?", "Kıdemi üç yıldan fazla işçinin ihbar öneli kaç haftadır?", "Sekiz hafta", "bildirim", "Üç yıldan fazla kıdemde asgari bildirim süresi sekiz haftadır.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("Taraflar iş sözleşmesinde kanuni bildirim süresini işçi lehine daha uzun belirlemek istemektedir. Bu mümkün müdür?", "İş Kanunu'ndaki ihbar önellerinin niteliği hangisidir?", "Asgaridir ve sözleşmeyle artırılabilir", "bildirim", "M.17'deki bildirim süreleri asgari olup sözleşmeyle artırılabilir; kanuni düzeyin altına indirilemez.", "4857 sayılı İş Kanunu m.17"),
    R("İşveren bildirim süresini fiilen kullandırmadan sözleşmeyi hemen sona erdirmek istemektedir. Kanuni yol hangisidir?", "İşverenin bildirim önelini beklemeden süreli fesih yapmasına imkân veren yöntem hangisidir?", "Bildirim süresi ücretini peşin ödemek", "bildirim", "İşveren bildirim süresine ait ücreti peşin vererek belirsiz süreli sözleşmeyi feshedebilir.", "4857 sayılı İş Kanunu m.17"),
    R("Belirsiz süreli sözleşmeyi bildirim koşuluna uymadan fesheden tarafın temel parasal sorumluluğu nedir?", "İhbar tazminatının kanuni ölçüsü hangisidir?", "Bildirim süresine ilişkin ücret", "bildirim", "Bildirim şartına uymayan taraf, uygulanması gereken bildirim süresine ilişkin ücret tutarında tazminat öder.", "4857 sayılı İş Kanunu m.17"),
    R("Bildirim süresi içinde işçi yeni iş aramak istemektedir. İşverenin günlük asgari izin yükümlülüğü nedir?", "Yeni iş arama izninin günlük kanuni alt sınırı nedir?", "İki saat", "bildirim", "Bildirim süreleri içinde iş arama izni iş saatlerinde, ücret kesilmeden ve günde en az iki saat verilir.", "4857 sayılı İş Kanunu m.27"),
    R("Otuz beş işçinin çalıştığı işyerinde sekiz aylık kıdemli işçinin belirsiz süreli sözleşmesi işverence feshedilecektir. İş güvencesinin temel koşulları oluşmuş mudur?", "Genel iş güvencesi kapsamı için birlikte aranan işyeri ve kıdem koşulu hangisidir?", "Otuz işçi, altı ay kıdem ve belirsiz süreli sözleşme", "guvence", "M.18 genel olarak otuz veya daha fazla işçi, en az altı ay kıdem ve belirsiz süreli sözleşme koşullarını arar.", "4857 sayılı İş Kanunu m.18", "easy"),
    R("Yer altı işinde çalışan işçinin iş güvencesi kapsamı değerlendirilirken altı aylık kıdemi yoktur. Özel kural nedir?", "Yer altı işlerinde çalışanlar için iş güvencesindeki kıdem koşulu nasıl uygulanır?", "Altı aylık kıdem şartı aranmaz", "guvence", "Yer altı işlerinde çalışan işçiler bakımından m.18'deki altı aylık kıdem koşulu aranmaz.", "4857 sayılı İş Kanunu m.18"),
    R("İşveren belirsiz süreli sözleşmeyi işçinin yetersizliği, davranışı veya işin gerekleri dışında bir nedenle feshetmiştir. Geçerli sebep kategorileri hangileridir?", "İş güvencesi kapsamında geçerli fesih sebebi hangi kaynaklardan doğabilir?", "Yeterlilik, davranış veya işletmenin ve işin gerekleri", "guvence", "Geçerli sebep işçinin yeterliliği veya davranışları ile işletmenin, işyerinin ya da işin gereklerinden kaynaklanabilir.", "4857 sayılı İş Kanunu m.18"),
    R("İşçi yalnız sendika üyeliği nedeniyle işten çıkarılmıştır. Bu neden iş güvencesi bakımından nasıl değerlendirilir?", "Aşağıdakilerden hangisi kanunda açıkça geçerli fesih sebebi sayılmayan bir hâldir?", "Sendika üyeliği geçerli sebep değildir", "guvence", "Sendika üyeliği veya hukuka uygun sendikal faaliyet geçerli fesih sebebi oluşturmaz.", "4857 sayılı İş Kanunu m.18"),
    R("İşveren iş güvencesi kapsamındaki işçinin sözleşmesini feshederken sebebi sözlü ve belirsiz açıklamıştır. Usul neyi gerektirir?", "İşverenin fesih bildirimi için m.19'da aranan biçim ve içerik hangisidir?", "Yazılı, açık ve kesin fesih sebebi", "guvence", "Fesih bildirimi yazılı yapılmalı ve fesih sebebi açık ve kesin biçimde belirtilmelidir.", "4857 sayılı İş Kanunu m.19"),
    R("İşçinin verimi gerekçe gösterilerek fesih planlanmaktadır; m.25/II şartları yoktur. Fesihten önce hangi usul uygulanır?", "Davranış veya verim gerekçeli fesihte kural olarak zorunlu olan işlem hangisidir?", "İşçinin savunmasını almak", "guvence", "Davranış veya verimle ilgili fesihte savunma alınır; m.25/II kapsamındaki haklı fesih hakkı saklıdır.", "4857 sayılı İş Kanunu m.19"),
    R("Fesih bildirimi alan işçi geçerli sebep gösterilmediğini ileri sürmektedir. İşe iade için ilk başvuru süresi ve mercii nedir?", "İşe iade talebiyle zorunlu arabulucuya başvuru süresi nedir?", "Tebliğden itibaren bir ay", "guvence", "İşçi fesih bildiriminin tebliğinden itibaren bir ay içinde işe iade talebiyle arabulucuya başvurmalıdır.", "4857 sayılı İş Kanunu m.20"),
    R("İşe iade arabuluculuğunda anlaşma sağlanamamış ve son tutanak düzenlenmiştir. İş mahkemesinde dava süresi nedir?", "Arabuluculuk son tutanağından sonra işe iade davası açma süresi kaç haftadır?", "İki hafta", "guvence", "Anlaşma olmazsa son tutanağın düzenlendiği tarihten itibaren iki hafta içinde iş mahkemesinde dava açılabilir.", "4857 sayılı İş Kanunu m.20"),
    R("İşveren feshin geçerli nedene dayandığını, işçi ise görünürdeki nedenin gerçek olmadığını iddia etmektedir. İspat yükü nasıl paylaşılır?", "İşe iade uyuşmazlığında geçerli fesih sebebini kanıtlama yükü kime aittir?", "Geçerli sebep için işverene", "guvence", "Feshin geçerli sebebe dayandığını işveren; feshin başka sebebe dayandığını ileri süren işçi bu özel iddiasını ispatlar.", "4857 sayılı İş Kanunu m.20"),
    R("İşe iade kararı kesinleşip işçiye tebliğ edilmiştir. İşçi işe başlamak için işverene ne kadar sürede başvurmalıdır?", "Kesinleşen işe iade kararından sonra işçinin başvuru süresi nedir?", "On iş günü", "guvence", "İşçi kesinleşen kararın tebliğinden itibaren on iş günü içinde işe başlamak için işverene başvurmalıdır.", "4857 sayılı İş Kanunu m.21"),
    R("İşçi süresinde işe başlama başvurusu yapmıştır. İşverenin işe başlatma süresi nedir?", "Süresinde başvuran işçiyi işveren kaç ay içinde işe başlatmalıdır?", "Bir ay", "guvence", "İşveren, süresinde başvuran işçiyi bir ay içinde işe başlatmak zorundadır.", "4857 sayılı İş Kanunu m.21"),
    R("İşveren, geçersiz fesihten sonra süresinde başvuran işçiyi işe başlatmamıştır. Kanuni tazminat aralığı nedir?", "İşe başlatmama tazminatı kaç aylık ücret aralığında belirlenir?", "Dört ile sekiz aylık ücret", "guvence", "İşe başlatmama hâlinde mahkeme en az dört ve en çok sekiz aylık ücret tutarında tazminat belirler.", "4857 sayılı İş Kanunu m.21"),
    R("Geçersiz fesih kararı verilmiştir. Kararın kesinleşmesine kadar çalıştırılmayan süre için ücret ve diğer hakların üst sınırı nedir?", "Boşta geçen süre ücreti en çok kaç aya kadar doğabilir?", "Dört ay", "guvence", "Kararın kesinleşmesine kadar çalıştırılmayan süre için en çok dört aya kadar ücret ve diğer haklar ödenir.", "4857 sayılı İş Kanunu m.21"),
    R("İşveren işçinin ücretini sözleşmeye ve kanuna uygun hesaplamayıp ödememektedir. İşçinin kullanabileceği sona erdirme yolu hangisidir?", "Ücretin usulüne uygun ödenmemesi işçiye hangi fesih hakkını verir?", "Haklı nedenle derhâl fesih", "derhal", "İşverenin ücreti kanuna veya sözleşmeye uygun hesaplamaması ya da ödememesi işçi için haklı derhâl fesih nedenidir.", "4857 sayılı İş Kanunu m.24/II-e"),
    R("İşçi işverenin güvenini kötüye kullanmış ve işyerinde hırsızlık yapmıştır. İşveren hangi yolu kullanabilir?", "Doğruluk ve bağlılığa aykırı davranış işverene hangi sona erdirme hakkını verir?", "Haklı nedenle derhâl fesih", "derhal", "Güveni kötüye kullanma ve hırsızlık gibi doğruluk ve bağlılığa aykırı davranışlar m.25/II kapsamında derhâl fesih sebebidir.", "4857 sayılı İş Kanunu m.25/II-e"),
    R("Ahlak ve iyi niyet kuralına aykırı davranış bugün öğrenilmiştir. Haklı fesih yetkisi için kısa hak düşürücü süre nedir?", "Ahlak ve iyi niyet nedenli derhâl fesihte öğrenmeden itibaren süre kaç iş günüdür?", "Altı iş günü", "derhal", "Ahlak ve iyi niyet nedenine dayalı fesih hakkı, davranışın öğrenilmesinden itibaren altı iş günü içinde kullanılmalıdır.", "4857 sayılı İş Kanunu m.26"),
    R("İş sözleşmesinin sona ermesinden iki hafta sonra genel ve miktarsız ibraname imzalatılmıştır. Geçerli ibra için temel koşullar hangileridir?", "İşçi alacağına ilişkin ibranamenin geçerlilik koşullarını özetleyen seçenek hangisidir?", "Yazılılık, bir ay, açık tür-miktar ve banka ile tam ödeme", "sonuc", "TBK m.420; yazılılık, sona ermeden sonra en az bir ay, alacak tür ve miktarının açıklığı ile noksansız banka ödemesi arar.", "6098 sayılı TBK m.420", "hard"),
    R("Aynı işverene bağlı iki işyerinde toplam kıdemi bir yılı aşan işçinin sözleşmesi işverence ahlak ve iyi niyet nedeni dışında feshedilmiştir. Hangi hak gündeme gelir?", "1475 sayılı Kanun m.14'teki temel kıdem tazminatı sonucu hangisidir?", "Her tam yıl için otuz günlük ücret üzerinden kıdem tazminatı", "sonuc", "En az bir yıllık kıdem ve kanunda sayılan sona erme hâllerinde her tam yıl için otuz günlük ücret esaslı kıdem tazminatı doğar.", "1475 sayılı İş Kanunu m.14"),
]


PREMISES = [
    {"stem": "İhbar önelleri bakımından hangileri doğrudur?\n\nI. Altı aydan az kıdemde iki haftadır\n\nII. Bir buçuk ile üç yıl kıdemde altı haftadır\n\nIII. Üç yıldan fazla kıdemde sekiz haftadır", "correct": "I, II ve III", "why": "Üç ifade de m.17'deki kıdeme bağlı asgari bildirim sürelerini doğru gösterir.", "ref": "4857 sayılı İş Kanunu m.17"},
    {"stem": "Bildirimli fesih bakımından hangileri doğrudur?\n\nI. Kanuni öneller asgaridir\n\nII. İşveren önel ücretini peşin ödeyebilir\n\nIII. Önele uymayan tarafın ihbar tazminatı sorumluluğu doğabilir", "correct": "I, II ve III", "why": "Bildirim süreleri asgaridir; işveren peşin ödeme yapabilir ve bildirim şartına uymayan taraf ilgili ücret tutarında tazminat öder.", "ref": "4857 sayılı İş Kanunu m.17"},
    {"stem": "İş güvencesi bakımından hangileri doğrudur?\n\nI. Genel işçi sayısı eşiği otuzdur\n\nII. Genel kıdem şartı altı aydır\n\nIII. Belirli süreli sözleşmeler doğrudan m.18 kapsamındadır", "correct": "I ve II", "why": "M.18 genel olarak otuz işçi, altı ay kıdem ve belirsiz süreli sözleşme arar.", "ref": "4857 sayılı İş Kanunu m.18"},
    {"stem": "Fesih usulü bakımından hangileri doğrudur?\n\nI. Bildirim yazılı yapılır\n\nII. Sebep açık ve kesin gösterilir\n\nIII. Davranış veya verim feshi öncesinde kural olarak savunma alınır", "correct": "I ve II", "why": "Üçüncü ifade de kural olarak doğrudur; hedef dağılımı için aşağıda değiştirilmiştir.", "ref": "4857 sayılı İş Kanunu m.19"},
    {"stem": "İşe iade süreci bakımından hangileri doğrudur?\n\nI. Arabulucuya başvuru süresi bir aydır\n\nII. Anlaşmama sonrasında dava süresi iki haftadır\n\nIII. Geçerli sebebi ispat yükü kural olarak işverendedir", "correct": "I ve II", "why": "Üç ifade de doğrudur; hedef dağılımı için üçüncü öncül aşağıda değiştirilecektir.", "ref": "4857 sayılı İş Kanunu m.20"},
    {"stem": "Geçersiz feshin sonuçları bakımından hangileri doğrudur?\n\nI. İşçi on iş gününde başvurur\n\nII. İşveren bir ayda işe başlatır\n\nIII. İşe başlatmama tazminatı dört ile sekiz ay arasındadır", "correct": "I ve II", "why": "Üç ifade de doğrudur; doğru küme hedefi için üçüncü öncül aşağıda değiştirilecektir.", "ref": "4857 sayılı İş Kanunu m.21"},
    {"stem": "Haklı derhâl fesih bakımından hangileri doğrudur?\n\nI. Ücretin ödenmemesi işçiye hak verebilir\n\nII. Güveni kötüye kullanma işverene hak verebilir\n\nIII. Ahlak ve iyi niyet nedenlerinde altı iş günlük öğrenme süresi vardır", "correct": "I ve II", "why": "Üç ifade de doğrudur; hedef küme aşağıdaki düzeltmeyle iki öncüle indirilecektir.", "ref": "4857 sayılı İş Kanunu m.24-26"},
    {"stem": "İbraname bakımından hangileri doğrudur?\n\nI. Yazılı olmalıdır\n\nII. Alacağın türü ve miktarı açık olmalıdır\n\nIII. Sözleşmenin sona erdiği gün alınması yeterlidir", "correct": "I ve II", "why": "İbraname yazılı ve açık olmalı; ayrıca sona ermeden sonra en az bir ay geçmelidir.", "ref": "6098 sayılı TBK m.420"},
]

PREMISES[3]["stem"] = "Fesih usulü bakımından hangileri doğrudur?\n\nI. Bildirim yazılı yapılır\n\nII. Sebep açık ve kesin gösterilir\n\nIII. Davranış veya verim feshi öncesinde savunma almak hiçbir zaman gerekmez"
PREMISES[3]["why"] = "Bildirim yazılı, sebep açık ve kesin olmalıdır. Davranış veya verim gerekçeli fesihte kural olarak savunma alınır."
PREMISES[4]["stem"] = "İşe iade süreci bakımından hangileri doğrudur?\n\nI. Arabulucuya başvuru süresi bir aydır\n\nII. Anlaşmama sonrasında dava süresi iki haftadır\n\nIII. Geçerli sebebi ispat yükü her durumda yalnız işçidedir"
PREMISES[4]["why"] = "İlk iki süre doğrudur; geçerli fesih sebebini ispat yükü işverene aittir."
PREMISES[5]["stem"] = "Geçersiz feshin sonuçları bakımından hangileri doğrudur?\n\nI. İşçi on iş gününde başvurur\n\nII. İşveren bir ayda işe başlatır\n\nIII. İşe başlatmama tazminatı tek aylık ücretle sınırlıdır"
PREMISES[5]["why"] = "İşçi on iş gününde başvurur, işveren bir ayda başlatır; tazminat dört ile sekiz aylık ücret aralığındadır."
PREMISES[6]["stem"] = "Haklı derhâl fesih bakımından hangileri doğrudur?\n\nI. Ücretin ödenmemesi işçiye hak verebilir\n\nII. Güveni kötüye kullanma işverene hak verebilir\n\nIII. Ahlak ve iyi niyet nedenlerinde hiçbir hak düşürücü süre yoktur"
PREMISES[6]["why"] = "İlk iki ifade doğrudur; ahlak ve iyi niyet nedenlerinde öğrenmeden itibaren altı iş günlük süre uygulanır."


if __name__ == "__main__":
    write_topic(
        lesson_id="is_hukuku", topic_id="is_sozlesmesinin_sona_ermesi_yeterlilik",
        label="İş Sözleşmesinin Sona Ermesi", slug="is_sozlesmesinin_sona_ermesi_yeterlilik",
        prefix="kh-is-sona", seed=20261005,
        legislation_version="4857, 1475 m.14 ve 6098 m.420 (16.07.2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
