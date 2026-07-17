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

# Doğru şıkkın uzunluğunun cevap anahtarına dönüşmemesi için her kazanım
# bankasında hem kısa hem uzun, konuya yakın yanlış önermeler tutulur.
WRONG["bildirim"].extend([
    "Önel her durumda bir haftadır",
    "Süreler yalnız iş günüyle hesaplanır",
    "Peşin ödeme feshi engeller",
    "Bildirimli fesih yalnız işverene aittir",
    "Belirli ve belirsiz süreli bütün sözleşmeler aynı bildirim önellerine tabidir; sözleşmenin süresi ve fesih türü önem taşımaz",
    "Kanuni bildirim süreleri azami niteliktedir ve taraflar bu süreleri işçi aleyhine diledikleri kadar kısaltabilir",
    "İşveren önel ücretini peşin ödediğinde iş güvencesine ilişkin geçerli sebep ve fesih usulü hükümleri artık uygulanmaz",
    "İhbar tazminatı hesabında işçiye düzenli sağlanan ve para ile ölçülebilen sözleşmesel veya kanuni menfaatler hiçbir zaman dikkate alınmaz",
])
WRONG["guvence"].extend([
    "İş güvencesinde kıdem aranmaz",
    "Fesih sebebi sözlü bırakılabilir",
    "İspat yükü daima işçidedir",
    "İşe iade başvurusu süresizdir",
    "İş güvencesi bütün belirli süreli sözleşmelere, işçi sayısı ve kıdem koşulu aranmaksızın kendiliğinden uygulanır",
    "İşveren davranış veya verim gerekçeli fesihte savunma almadan ve fesih sebebini yazılı açıklamadan sözleşmeyi sona erdirebilir",
    "İşe iade talebi arabulucuya götürülemez; işçi fesih bildiriminin ardından süre sınırlaması olmaksızın doğrudan dava açabilir",
    "Geçersiz fesih kararından sonra işçinin başvurusuna gerek yoktur; işe başlatma ve bütün parasal sonuçlar karar anında otomatik doğar",
])
WRONG["derhal"].extend([
    "Haklı fesihte önel beklenir",
    "Ücret ihlali fesih hakkı doğurmaz",
    "Devamsızlık hiçbir sonuç doğurmaz",
    "Haklı fesih yetkisi süresizdir",
    "Ahlak ve iyi niyet kurallarına aykırı davranışlarda öğrenme ve olay tarihine bağlı hiçbir hak düşürücü süre uygulanmaz",
    "Haklı nedenle derhâl fesih yalnız belirsiz süreli sözleşmelerde mümkündür; belirli süreli sözleşmelerde süre sonuna kadar beklenir",
    "İşçinin doğruluk ve bağlılığa aykırı davranışı ile işverenin ücreti ödememesi, taraflardan hiçbirine derhâl fesih hakkı vermez",
    "İşçinin olaydan maddi çıkar sağlaması hâlinde hem altı iş günlük öğrenme süresi hem de bir yıllık üst süre tamamen ortadan kalkar",
])
WRONG["sonuc"].extend([
    "İbra sözlü yapılabilir",
    "Kıdem için çalışma süresi aranmaz",
    "Kullanılmayan izin alacağı sona erer",
    "İbra ödemesinde banka aranmaz",
    "Sözleşmenin sona erdiği gün düzenlenen, alacak türü ve miktarı belirtilmeyen genel ibra beyanı bütün işçilik alacaklarını sona erdirir",
    "Kıdem tazminatı, sona erme sebebi ve bir yıllık kıdem koşulu aranmadan her ayrılan işçiye yalnız çıplak ücret üzerinden ödenir",
    "İş sözleşmesi sona erdiğinde kullanılmayan yıllık izinler ücret alacağına dönüşmez ve işçinin hak sahipleri de herhangi bir ödeme isteyemez",
    "İbra belgesinde yazılılık, bir aylık bekleme, alacak tür ve miktarının açıklığı ile noksansız banka ödemesi koşullarından hiçbiri aranmaz",
])


RULES = [
    R("Dört aydır çalışan işçinin belirsiz süreli sözleşmesi bildirimli feshedilecektir. Asgari bildirim öneli nedir?", "Kıdemi altı aydan az işçi için kanuni ihbar öneli kaç haftadır?", "İki hafta", "bildirim", "İşi altı aydan az sürmüş işçi için bildirimden başlayarak iki haftalık önel uygulanır.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("Bir yıldır çalışan işçiye bildirimli fesihte üç haftalık önel tanınmıştır. Kanuni alt sınır bakımından sonuç nedir?", "Kıdemi altı ay ile bir buçuk yıl arasında olan işçinin ihbar öneli kaç haftadır?", "Dört hafta", "bildirim", "Altı aydan bir buçuk yıla kadar kıdemde asgari bildirim süresi dört haftadır; üç haftalık önel yetersizdir.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("İki yıl kıdemli işçinin sözleşmesinde altı haftalık bildirim öneli uygulanmıştır. Kanuni alt sınır karşılanmış mıdır?", "Kıdemi bir buçuk yıl ile üç yıl arasında olan işçinin ihbar öneli kaç haftadır?", "Altı hafta", "bildirim", "Bir buçuk yıldan üç yıla kadar kıdemde asgari bildirim süresi altı haftadır; uygulanan önel alt sınırı karşılar.", "4857 sayılı İş Kanunu m.17", "easy"),
    R("Dört yıl kıdemli işçiye bildirimli fesihte altı haftalık önel verilmiştir. Kanuni alt sınır karşılanmış mıdır?", "Kıdemi üç yıldan fazla işçinin ihbar öneli kaç haftadır?", "Sekiz hafta", "bildirim", "Üç yıldan fazla kıdemde asgari bildirim süresi sekiz haftadır; altı haftalık önel yetersizdir.", "4857 sayılı İş Kanunu m.17", "easy"),
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
    F("Dört aylık kıdem için asgari bildirim süresi iki haftadır", "Belirli süreli iş sözleşmesi, aksi kararlaştırılmadıkça süresi dolduğunda nasıl sona erer?", "Fesih bildirimi gerekmeksizin sürenin bitiminde kendiliğinden sona erer", "Belirli süreli hizmet sözleşmesi, aksi kararlaştırılmadıkça bildirim aranmadan kararlaştırılan sürenin sonunda kendiliğinden sona erer.", "6098 sayılı TBK m.430", "easy"),
    F("Üç haftalık önel yetersizdir; asgari bildirim süresi dört haftadır", "İş güvencesi kapsamı dışındaki işçinin sözleşmesi fesih hakkı kötüye kullanılarak sona erdirilmiştir. Kötüniyet tazminatının kanuni ölçüsü nedir?", "Bildirim süresinin üç katı tutarında kötüniyet tazminatı ödenir", "M.17, iş güvencesi dışında kalan işçinin sözleşmesi fesih hakkı kötüye kullanılarak sona erdirildiğinde bildirim süresinin üç katı tutarında tazminat öngörür.", "4857 sayılı İş Kanunu m.17", "hard"),
    F("Evet; iki yıllık kıdem için altı haftalık kanuni önel karşılanmıştır", "Belirsiz süreli sözleşmede bildirim öneli hangi olayla işlemeye başlar?", "Fesih bildiriminin diğer tarafa yapılmasıyla işlemeye başlar", "Kanuni önel, fesih iradesini içeren bildirimin diğer tarafa yapılmasıyla işlemeye başlar.", "4857 sayılı İş Kanunu m.17"),
    F("Hayır; dört yıllık kıdem için asgari önel sekiz haftadır", "Yüz elli işçinin çalıştığı işyerinde bir ay içinde on beş işçinin sözleşmesi m.17 uyarınca sona erdirilecektir. Sayısal toplu çıkarma eşiği aşılmış mıdır?", "Evet; yüz bir ile üç yüz işçi arasındaki işyerinde yüzde onluk eşik sağlanmıştır", "M.29'a göre 101-300 işçinin bulunduğu işyerinde bir ay içinde en az yüzde on oranındaki m.17 feshi toplu işçi çıkarma sayılır.", "4857 sayılı İş Kanunu m.29", "hard"),
    F("Kanuni bildirim önelleri asgaridir ve sözleşmeyle artırılabilir", "Taraflar m.17'deki kanuni bildirim önelini işçi aleyhine kısaltabilir mi?", "Hayır; asgari öneller kısaltılamaz, yalnız artırılabilir", "M.17'deki öneller koruyucu asgari sürelerdir; sözleşme ile artırılabilir fakat kanuni düzeyin altına indirilemez.", "4857 sayılı İş Kanunu m.17"),
    F("İşveren bildirim süresine ait ücreti peşin vererek sözleşmeyi sona erdirebilir", "İşverenin bildirim ücretini peşin ödemesi iş güvencesi hükümlerini devre dışı bırakır mı?", "Hayır; peşin ödeme m.18-21 hükümlerinin uygulanmasını engellemez", "M.17, işverenin önel ücretini peşin ödemesinin iş güvencesi ve fesih denetimini ortadan kaldırmadığını açıkça düzenler.", "4857 sayılı İş Kanunu m.17", "hard"),
    F("Uyulmayan bildirim süresine ilişkin ücret tutarında ihbar tazminatı ödenir", "İhbar tazminatı hesabında çıplak ücrete ek olarak hangi menfaatler dikkate alınır?", "Para veya para ile ölçülebilen düzenli sözleşmesel ve kanuni menfaatler", "M.17, ihbar tazminatı ve peşin önel ücretinde temel ücrete ek olarak para ile ölçülebilen sözleşme ve kanun kaynaklı menfaatleri de hesaba katar.", "4857 sayılı İş Kanunu m.17", "hard"),
    F("İş arama izni iş saatlerinde, ücret kesilmeden ve günde en az iki saat verilir", "İşveren, işçiyi yeni iş arama izni sırasında çalıştırırsa hangi ek ödeme doğar?", "İzin ücretine ek olarak çalıştırılan sürenin ücreti yüzde yüz zamlı ödenir", "M.27 uyarınca işçi izin kullanmış gibi ücretini alır; çalıştırıldığı süre için ayrıca yüzde yüz zamlı ücret ödenir.", "4857 sayılı İş Kanunu m.27", "hard"),
    F("Otuz işçi, en az altı ay kıdem ve belirsiz süreli sözleşme koşulları oluşmuştur", "İşverenin aynı işkolunda birden fazla işyeri varsa otuz işçi eşiği nasıl hesaplanır?", "Aynı işkolundaki işyerlerinde çalışan toplam işçi sayısı esas alınır", "M.18, aynı işkolundaki birden çok işyerinde işçi sayısının bu işyerlerinin toplamına göre belirlenmesini emreder.", "4857 sayılı İş Kanunu m.18", "hard"),
    F("Yer altı işçisinde iş güvencesi için altı aylık kıdem koşulu aranmaz", "Yer altı işçileri m.18'deki bütün iş güvencesi koşullarından muaf mıdır?", "Hayır; özel istisna yalnız altı aylık kıdem koşuluna ilişkindir", "M.18 yer altı işçileri için yalnız kıdem şartını kaldırır; belirsiz süreli sözleşme ve işçi sayısı gibi diğer kapsam koşullarını kaldırmaz.", "4857 sayılı İş Kanunu m.18", "hard"),
    F("Geçerli sebep işçinin yeterliliği, davranışı veya işletmenin ve işin gereklerinden doğabilir", "Hastalık nedeniyle m.25/I-b'deki bekleme süresi içindeki geçici devamsızlık geçerli fesih sebebi sayılır mı?", "Hayır; kanuni bekleme süresindeki geçici devamsızlık geçerli sebep oluşturmaz", "M.18, hastalık veya kaza nedeniyle m.25/I-b'de öngörülen bekleme süresindeki geçici devamsızlığı geçerli sebep saymaz.", "4857 sayılı İş Kanunu m.18", "hard"),
    F("Sendika üyeliği veya hukuka uygun sendikal faaliyet geçerli fesih sebebi değildir", "İşçinin mevzuattan doğan hakkını aramak için idari ya da adli makama başvurması geçerli fesih sebebi midir?", "Hayır; hakkını aramak için makamlara başvurması geçerli sebep değildir", "M.18, işçinin mevzuat veya sözleşmeden doğan haklarını izlemek için yetkili makamlara başvurmasını geçerli fesih sebebi dışında tutar.", "4857 sayılı İş Kanunu m.18"),
    F("Fesih bildirimi yazılı yapılmalı; sebep açık ve kesin biçimde gösterilmelidir", "İş güvencesi kapsamındaki işçiye yalnız sözlü ve belirsiz bir fesih açıklaması yapılması m.19'a uygun mudur?", "Hayır; yazılı bildirim ile açık ve kesin sebep birlikte aranır", "M.19 fesih iradesinin yazılı bildirilmesini ve dayanılan sebebin açık, kesin şekilde belirtilmesini birlikte zorunlu kılar.", "4857 sayılı İş Kanunu m.19", "easy"),
    F("Davranış veya verim gerekçeli geçerli fesihten önce işçinin savunması alınmalıdır", "İşçinin davranışı m.25/II kapsamında haklı fesih oluşturuyorsa m.19'daki savunma kuralı bu hakkı kaldırır mı?", "Hayır; m.25/II koşullarına uygun haklı fesih hakkı saklıdır", "M.19 savunma kuralını getirirken işverenin m.25/II şartlarına uygun derhâl fesih yetkisini açıkça saklı tutar.", "4857 sayılı İş Kanunu m.19", "hard"),
    F("İşçi fesih bildiriminin tebliğinden itibaren bir ay içinde zorunlu arabulucuya başvurmalıdır", "İşçi arabulucuya gitmeden doğrudan işe iade davası açmış ve dava bu nedenle usulden reddedilmiştir. Yeni başvuru süresi nedir?", "Kesinleşen ret kararının resen tebliğinden itibaren iki hafta içinde arabulucuya başvurulur", "M.20, zorunlu arabuluculuk atlandığı için verilen ret kesinleşip tebliğ edilince işçiye iki haftalık telafi başvurusu tanır.", "4857 sayılı İş Kanunu m.20", "hard"),
    F("Anlaşmama son tutanağından itibaren iki hafta içinde iş mahkemesinde dava açılır", "İşe iade arabuluculuğunda anlaşma olmazsa taraflar iş mahkemesi yerine özel hakeme gidebilir mi?", "Evet; taraflar anlaşırlarsa iki haftalık sürede özel hakeme gidebilir", "M.20, arabuluculukta anlaşma olmazsa tarafların ortak iradesiyle uyuşmazlığın iki hafta içinde özel hakeme götürülmesine izin verir.", "4857 sayılı İş Kanunu m.20", "hard"),
    F("Feshin geçerli sebebe dayandığını kanıtlama yükü işverene aittir", "İşçi feshin işverenin açıkladığından başka bir sebebe dayandığını ileri sürerse bu iddiayı kim ispatlar?", "Açıkladığı farklı fesih sebebini ispat yükü işçiye aittir", "M.20 genel geçerli sebep ispatını işverene yükler; işçi görünürdeki sebepten farklı bir sebep ileri sürerse özel iddiasını kendisi ispatlar.", "4857 sayılı İş Kanunu m.20"),
    F("İşçi kesinleşen kararın tebliğinden itibaren on iş gününde işverene başvurmalıdır", "İşçi kesinleşen işe iade kararından sonra on iş gününde başvurmazsa fesih nasıl değerlendirilir?", "Fesih geçerli sayılır ve işveren yalnız bunun hukuki sonuçlarından sorumlu olur", "M.21, süresinde işe başlama başvurusu yapılmamasını feshin geçerli sayılması sonucuna bağlar.", "4857 sayılı İş Kanunu m.21", "hard"),
    F("İşveren süresinde başvuran işçiyi başvurudan itibaren bir ay içinde işe başlatmalıdır", "İşverenin bir aylık işe başlatma süresi hangi olaydan sonra işler?", "İşçinin kesinleşen karara dayanarak süresinde işe başlama başvurusu yapmasıyla", "İşverenin bir aylık yükümlülüğü, işçinin kesinleşen karar üzerine on iş günlük sürede işe başlamak için başvurmasıyla doğar.", "4857 sayılı İş Kanunu m.21"),
    F("İşe başlatmama tazminatı dört ile sekiz aylık ücret arasında belirlenir", "Feshin geçersizliğine karar veren mahkeme işe başlatmama tazminatını ayrıca belirler mi?", "Evet; işe başlatılmama hâlinde ödenecek tazminat karar içinde belirlenir", "M.21 mahkeme veya özel hakemin geçersizlik kararı verirken işe başlatmama ihtimalindeki tazminat miktarını da belirlemesini ister.", "4857 sayılı İş Kanunu m.21"),
    F("Boşta geçen süre için en çok dört aya kadar ücret ve diğer haklar ödenir", "Mahkeme boşta geçen süre ücreti ile işe başlatmama tazminatını hangi tarihteki ücreti esas alarak parasallaştırır?", "Dava tarihindeki ücret esas alınarak parasal miktar belirlenir", "M.21, işe başlatmama tazminatı ile boşta geçen süre ücret ve haklarının dava tarihindeki ücret üzerinden parasal belirlenmesini öngörür.", "4857 sayılı İş Kanunu m.21", "hard"),
    F("Ücretin kanuna veya sözleşmeye uygun ödenmemesi işçiye haklı derhâl fesih hakkı verir", "İşçi başka bir işçi veya üçüncü kişi tarafından cinsel tacize uğradığını işverene bildirmiş; gerekli önlem alınmamıştır. İşçi ne yapabilir?", "İşçi m.24/II uyarınca sözleşmesini haklı nedenle derhâl feshedebilir", "İşveren, bildirilen cinsel tacize karşı gerekli önlemleri almazsa m.24/II-d işçiye haklı derhâl fesih hakkı tanır.", "4857 sayılı İş Kanunu m.24/II-d", "hard"),
    F("Hırsızlık ve güveni kötüye kullanma işverene haklı nedenle derhâl fesih hakkı verir", "İşçinin izinsiz ve haklı sebep olmadan ardı ardına iki iş günü işe gelmemesi hangi sonucu doğurabilir?", "İşveren m.25/II-g uyarınca sözleşmeyi haklı nedenle derhâl feshedebilir", "M.25/II-g, haklı sebep ve izin olmadan ardı ardına iki iş günlük devamsızlığı işveren için derhâl fesih sebebi sayar.", "4857 sayılı İş Kanunu m.25/II-g", "hard"),
    F("Ahlak ve iyi niyet nedenli fesih hakkı öğrenmeden itibaren altı iş gününde kullanılmalıdır", "İşçinin olaydan maddi çıkar sağlaması m.26'daki sürelerden hangisini etkiler?", "Bir yıllık üst süre uygulanmaz; altı iş günlük öğrenme süresi devam eder", "M.26 maddi çıkar hâlinde yalnız fiilden itibaren bir yıllık üst süreyi kaldırır; öğrenmeden başlayan altı iş günlük süreyi kaldırmaz.", "4857 sayılı İş Kanunu m.26", "hard"),
    F("Geçerli ibra için yazılılık, en az bir ay, açık tür ve miktar ile noksansız banka ödemesi birlikte aranır", "Gerçek hak tutarını içermeyen ancak banka yoluyla kısmi ödeme gösteren belge hangi ölçüde hüküm doğurur?", "Yalnız içerdiği ödeme miktarıyla sınırlı olarak makbuz hükmündedir", "TBK m.420, gerçek tutarı içermeyen ödeme belgesini ibra saymaz; banka ödemesi koşuluyla yalnız yazılı miktar kadar makbuz etkisi tanır.", "6098 sayılı TBK m.420", "hard"),
    F("Kanuni sona erme hâlinde her tam yıl için otuz günlük ücret esaslı kıdem tazminatı doğar", "İş sözleşmesi herhangi bir nedenle sona erdiğinde kullanılmayan yıllık izinler ne olur?", "Kullanılmayan izinlerin ücreti sona erme tarihindeki ücret üzerinden işçiye veya hak sahiplerine ödenir", "İş Kanunu m.59, sona erme sebebinden bağımsız olarak hak kazanılmış kullanılmayan izinleri son ücret üzerinden para alacağına dönüştürür.", "4857 sayılı İş Kanunu m.59", "hard"),
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
    {"stem": "İhbar önelleri bakımından hangileri doğrudur?\n\nI. Altı aydan az kıdemde iki haftadır\n\nII. Bir buçuk ile üç yıl kıdemde altı haftadır\n\nIII. Üç yıldan fazla kıdemde sekiz haftadır", "correct": "I, II ve III", "why": "Üç ifade de m.17'deki kıdeme bağlı asgari bildirim sürelerini doğru gösterir.", "ref": "4857 sayılı İş Kanunu m.17"},
    {"stem": "Bildirimli fesih bakımından hangileri doğrudur?\n\nI. Kanuni öneller asgaridir\n\nII. İşveren önel ücretini peşin ödeyebilir\n\nIII. Önele uymayan tarafın ihbar tazminatı sorumluluğu doğabilir", "correct": "I, II ve III", "why": "Bildirim süreleri asgaridir; işveren peşin ödeme yapabilir ve bildirim şartına uymayan taraf ilgili ücret tutarında tazminat öder.", "ref": "4857 sayılı İş Kanunu m.17"},
    {"stem": "İş güvencesi bakımından hangileri doğrudur?\n\nI. Genel işçi sayısı eşiği otuzdur\n\nII. Belirli süreli sözleşmeler doğrudan m.18 kapsamındadır\n\nIII. Aynı işkolundaki birden çok işyerinin işçi sayısı birlikte değerlendirilir", "correct": "I ve III", "why": "M.18 otuz işçi ve belirsiz süreli sözleşme arar; aynı işkolundaki işyerlerinde toplam işçi sayısı esas alınır.", "ref": "4857 sayılı İş Kanunu m.18"},
    {"stem": "Fesih usulü bakımından hangileri doğrudur?\n\nI. Sözlü ve belirsiz bir bildirim yeterlidir\n\nII. Fesih bildirimi yazılı yapılır\n\nIII. Davranış veya verim feshi öncesinde kural olarak savunma alınır", "correct": "II ve III", "why": "M.19 yazılı ve açık fesih bildirimi arar; davranış veya verim gerekçeli fesihte kural olarak savunma alınır.", "ref": "4857 sayılı İş Kanunu m.19"},
    {"stem": "İşe iade süreci bakımından hangileri doğrudur?\n\nI. Arabulucuya başvuru süresi bir aydır\n\nII. Anlaşmama sonrasında dava süresi iki haftadır\n\nIII. Geçerli sebebi ispat yükü her durumda yalnız işçidedir", "correct": "I ve II", "why": "İlk iki süre doğrudur; geçerli fesih sebebini ispat yükü işverene aittir.", "ref": "4857 sayılı İş Kanunu m.20"},
    {"stem": "Geçersiz feshin sonuçları bakımından hangileri doğrudur?\n\nI. İşçi on iş gününde işverene başvurur\n\nII. İşverenin işe başlatma süresi iki aydır\n\nIII. İşe başlatmama tazminatı dört ile sekiz aylık ücret arasındadır", "correct": "I ve III", "why": "İşçi on iş gününde başvurur; işverenin süresi bir aydır ve işe başlatmama tazminatı dört ile sekiz aylık ücret aralığındadır.", "ref": "4857 sayılı İş Kanunu m.21"},
    {"stem": "Haklı derhâl fesih bakımından hangileri doğrudur?\n\nI. Ücretin ödenmemesi işçiye hiçbir fesih hakkı vermez\n\nII. Güveni kötüye kullanma işverene hak verebilir\n\nIII. Ahlak ve iyi niyet nedenlerinde altı iş günlük öğrenme süresi vardır", "correct": "II ve III", "why": "Ücretin ödenmemesi işçiye, güveni kötüye kullanma işverene haklı fesih hakkı verebilir; m.26'da altı iş günlük öğrenme süresi vardır.", "ref": "4857 sayılı İş Kanunu m.24-26"},
    {"stem": "İbraname bakımından hangileri doğrudur?\n\nI. Sözlü yapılması yeterlidir\n\nII. Yazılı olması ve alacak türü ile miktarını açıkça göstermesi gerekir\n\nIII. Sözleşmenin sona erdiği gün alınması yeterlidir", "correct": "Yalnız II", "why": "İbra yazılı ve açık olmalı; ayrıca sözleşmenin sona ermesinden başlayarak en az bir ay geçmeli ve noksansız ödeme banka aracılığıyla yapılmalıdır.", "ref": "6098 sayılı TBK m.420"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="is_hukuku", topic_id="is_sozlesmesinin_sona_ermesi_yeterlilik",
        label="İş Sözleşmesinin Sona Ermesi", slug="is_sozlesmesinin_sona_ermesi_yeterlilik",
        prefix="kh-is-sona", seed=20261005,
        legislation_version="4857, 1475 m.14 ve 6098 m.420 (17.07.2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
