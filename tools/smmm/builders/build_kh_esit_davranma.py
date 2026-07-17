#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM İş Hukuku — Eşit Davranma İlkesi konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde Çalışma ve Sosyal Güvenlik Bakanlığından alınan
güncel 4857 sayılı İş Kanunu m.5 ile 6701 sayılı Kanun m.2–7 ve m.21'dir.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors,
        "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r(
        "İşveren, aynı nitelikteki işçilere yalnız dilleri ve siyasi görüşleri nedeniyle farklı sosyal haklar uygulamıştır. İş Kanunu bakımından hangisi doğrudur?",
        "İş ilişkisinde ayrım yasağı kapsamında açıkça sayılan temellerden bazıları hangileridir?",
        "Dil ve siyasi görüşe dayalı ayrım iş ilişkisinde yasaktır",
        ["İşveren dilediği temelde ayrım yapabilir", "Dil yalnız ücret dışında ayrım nedeni olabilir", "Siyasi görüş çalışma koşullarında her zaman haklı farklılık nedenidir", "Ayrım yasağı yalnız iş sözleşmesi sona erdikten sonraki dönemde uygulanır"],
        "İş Kanunu m.5; dil, ırk, renk, cinsiyet, engellilik, siyasi düşünce, felsefi inanç, din, mezhep ve benzeri sebeplere dayalı ayrımı yasaklar.",
        "Yasak sayılan kelimelerle sınırlı kapalı bir liste değildir; benzeri kişisel temellere dayalı farklı muamele de denetlenir.",
        "4857 sayılı İş Kanunu m.5", "easy",
    ),
    r(
        "Kısmi süreli işçi, salt kısmi süreli olduğu gerekçesiyle aynı işi yapan tam süreli emsalinden farklı işleme tabi tutulmuştur. Esaslı sebep yoktur. Sonuç nedir?",
        "Kısmi ve tam süreli çalışanlar arasında farklı işlem hangi durumda yapılabilir?",
        "Esaslı sebep yoksa salt kısmi çalışma farklı işlemi haklı kılmaz",
        ["Kısmi işçi eşit işlem korumasından yararlanmaz", "Her kısmi çalışma ücret hakkını sona erdirir", "Farklılık için yalnız işverenin sözlü tercihi yeterlidir", "Tam süreli işçi karşısında kısmi işçiye daima daha ağır koşullar uygulanmalıdır"],
        "İş Kanunu m.5, esaslı sebepler olmadıkça tam süreli çalışan karşısında kısmi süreli çalışana farklı işlem yapılmasını yasaklar.",
        "Farklı çalışma süresi bölünebilir menfaatlerde orantı yaratabilir; fakat salt sözleşme türü keyfî eşitsizliği meşrulaştırmaz.",
        "4857 sayılı İş Kanunu m.5", "medium",
    ),
    r(
        "Belirli süreli çalışan, yalnız sözleşmesinin süreli olması nedeniyle emsal belirsiz süreli işçiden daha düşük yan hak almıştır. Haklı sebep gösterilmemiştir. Hangisi doğrudur?",
        "Belirli ve belirsiz süreli çalışanlar arasında farklı işlem yapılmasının sınırı nedir?",
        "Esaslı sebep yoksa salt belirli süreli olma farklılığı haklı göstermez",
        ["Belirli süreli işçinin hiçbir yan hakkı bulunmaz ve bu işçi emsal belirsiz süreli çalışanla hiçbir koşulda karşılaştırılamaz", "Süreli sözleşme her ayrımı kendiliğinden geçerli kılar", "İşveren gerekçe göstermeden tüm hakları kaldırabilir", "Belirsiz süreli emsal yalnız başka ülkede çalışan yönetici olabilir"],
        "İş Kanunu m.5, esaslı sebep olmadıkça belirsiz süreli çalışan karşısında belirli süreli çalışana farklı işlem yapılmasını yasaklar.",
        "Sözleşmenin süreli niteliği tek başına ayrım gerekçesi değildir. İşin veya menfaatin niteliğine dayanan nesnel neden ayrıca gösterilmelidir.",
        "4857 sayılı İş Kanunu m.5", "medium",
    ),
    r(
        "İşveren, iş başvurusunu adayın hamile olması nedeniyle reddetmiş; işin niteliği bu ayrımı zorunlu kılmamaktadır. İş Kanunu bakımından değerlendirme nedir?",
        "Cinsiyet veya gebeliğe dayalı farklı işlem iş ilişkisinin hangi aşamalarında yasaktır?",
        "Sözleşmenin yapılması, uygulanması ve sona ermesi dâhil bütün aşamalarda yasaktır",
        ["Gebelik işe alımda daima ret nedenidir", "Yasak yalnız iş sözleşmesinin imzalandığı günü kapsar", "Cinsiyet sözleşmenin sona ermesinde sınırsız ayrım nedeni olabilir", "Biyolojik veya işin niteliğiyle ilgili zorunluluk bulunmadan da farklı işlem yapılabilir"],
        "İş Kanunu m.5, biyolojik veya işin niteliğine ilişkin zorunlu neden yoksa cinsiyet ya da gebelik temelinde sözleşmenin yapılması, şartları, uygulanması ve sona ermesinde farklı işlemi yasaklar.",
        "Koruma işe başvuru anından iş ilişkisinin sona ermesine kadar uzanır. İstisna, gerçek ve zorunlu iş niteliğine dayanmalıdır.",
        "4857 sayılı İş Kanunu m.5", "medium",
    ),
    r(
        "Aynı veya eşit değerde işi yapan iki çalışandan kadına yalnız cinsiyeti nedeniyle daha düşük temel ücret belirlenmiştir. Hangisi doğrudur?",
        "Aynı veya eşit değerde iş için ücretin cinsiyete göre belirlenmesine ilişkin kural nedir?",
        "Cinsiyet nedeniyle daha düşük ücret kararlaştırılamaz",
        ["Ücret ayrımı tamamen serbesttir", "Kadın işçiye daima daha düşük ücret verilmelidir", "Eşit ücret ilkesi yalnız ikramiye dışındaki ayni yardımlara uygulanır", "Aynı değerde iş bulunması cinsiyet temelli ücret farkını kendiliğinden haklı kılar"],
        "İş Kanunu m.5, aynı veya eşit değerde bir iş için cinsiyet nedeniyle daha düşük ücret kararlaştırılmasını açıkça yasaklar.",
        "Karşılaştırma yalnız aynı görev unvanına değil, eşit değerde işe de uzanır. Ücret farkının cinsiyet dışı nesnel gerekçesi ayrıca incelenebilir.",
        "4857 sayılı İş Kanunu m.5", "easy",
    ),
    r(
        "İşveren, kadın işçiye özel koruyucu hükümlerin uygulanmasını gerekçe gösterip onun ücretini azaltmıştır. Bu gerekçe geçerli midir?",
        "Cinsiyete bağlı özel koruyucu hükümlerin uygulanması ücret bakımından ne sonuç doğurur?",
        "Özel koruma daha düşük ücret uygulanmasını haklı kılmaz",
        ["Koruyucu hüküm ücreti kaldırır", "Her özel koruma ücretin yarıya indirilmesini gerektirir", "Koruyucu hüküm yalnız işverenin ücret borcunu ertelemek için uygulanır", "Özel korumadan yararlanan işçi eşit ücret güvencesini tamamen kaybeder"],
        "İş Kanunu m.5, işçinin cinsiyeti nedeniyle özel koruyucu hükümlerin uygulanmasının daha düşük ücreti haklı kılmayacağını düzenler.",
        "Koruma önlemleri eşitliğe aykırı ücret indiriminin aracı yapılamaz. Korunma ve eşit ücret güvenceleri birlikte uygulanır.",
        "4857 sayılı İş Kanunu m.5", "easy",
    ),
    r(
        "İşveren eşit davranma borcunu ihlal etmiş ve işçiyi bazı ücret haklarından yoksun bırakmıştır. İşçi hangi talepleri birlikte ileri sürebilir?",
        "İş Kanunu m.5'e aykırılıkta işçinin isteyebileceği ayrımcılık tazminatının üst sınırı ve ek talebi nedir?",
        "Dört aya kadar ücreti tutarında uygun tazminat ile yoksun bırakıldığı hakları isteyebilir",
        ["İşçi yalnız özür talep edebilir", "Tazminat her durumda tam on iki aylık ücrettir ve işçi yoksun bırakıldığı hiçbir ücret veya yan hakkı ayrıca isteyemez", "Yoksun kalınan haklar tazminat istenince kesin olarak düşer", "İhlal işçiyi işverene dört aylık ücret ödemekle yükümlü kılar"],
        "İş Kanunu m.5, ihlalde işçiye dört aya kadar ücreti tutarında uygun tazminatın yanında yoksun bırakıldığı hakları isteme yetkisi verir.",
        "Tazminat sabit dört ay değildir; üst sınır dört aydır. Ücret ve yan hak kayıpları uygun tazminattan ayrı olarak talep edilebilir.",
        "4857 sayılı İş Kanunu m.5", "hard",
    ),
    r(
        "İşçi, cinsiyet ayrımı yapıldığı ihtimalini güçlü biçimde gösteren yazışmaları sunmuştur. Bundan sonra ispat yükü nasıl dağılır?",
        "İşçi ayrım ihlali ihtimalini güçlü biçimde gösteren bir durum ortaya koyarsa işveren neyi ispatlamalıdır?",
        "İşveren eşit davranma borcunu ihlal etmediğini ispatlamalıdır",
        ["İspat yükü hiçbir zaman değişmez", "İşçi artık işverenin bütün başka borçlarını ispatlar", "İşveren yalnız işçinin kıdemini inkâr ederek ispat yükünü yerine getirir", "Güçlü emare bulunsa bile işveren ayrım yapmadığını açıklamak zorunda değildir"],
        "İş Kanunu m.5'te genel olarak işçi ihlali ispatlar; güçlü ihtimali gösteren durum ortaya konduğunda işveren ihlal bulunmadığını ispatlar.",
        "Bu düzenleme ispat güçlüğünü dengeler. Soyut iddia yeterli değildir; işçi önce ihlal ihtimalini güçlü kılan olguyu göstermelidir.",
        "4857 sayılı İş Kanunu m.5", "hard",
    ),
    r(
        "İşveren, adayın etnik kökenini açıkça gerekçe göstererek başvurusunu karşılaştırılabilir adaylardan daha olumsuz değerlendirmiştir. Bu ayrım türü nedir?",
        "6701 sayılı Kanuna göre doğrudan ayrımcılığın ayırt edici unsuru nedir?",
        "Sayılan temele dayalı açık farklı muameleyle eşit yararlanmanın engellenmesidir",
        ["Her farklılık doğrudan ayrımdır", "Görünüşte tarafsız kuralın dolaylı etkisidir", "Yalnız birden çok ayrım temelinin aynı anda bulunması ve uygulamanın herkese özdeş sonuç vermesidir", "Kişinin ayrım temelini taşımadığı hâlde taşıdığı sanılarak muamele görmesidir"],
        "6701 sayılı Kanun m.2, karşılaştırılabilir durumdakilere göre eşit yararlanmayı sayılan temelde engelleyen veya zorlaştıran farklı muameleyi doğrudan ayrımcılık sayar.",
        "Açıkça ayrım temeline dayanan farklı muamele doğrudandır. Görünüşte tarafsız uygulamanın haklılaştırılamayan etkisi ise dolaylı ayrımcılıktır.",
        "6701 sayılı Kanun m.2", "medium",
    ),
    r(
        "İşyerinde herkese uygulanan görünüşte tarafsız bir kural, engelli çalışanları nesnel olarak haklılaştırılamayan dezavantajlı konuma sokmuştur. Ayrım türü nedir?",
        "Dolaylı ayrımcılığın doğrudan ayrımcılıktan temel farkı nedir?",
        "Görünüşte tarafsız uygulama belirli temelle bağlantılı haklılaştırılamayan dezavantaj doğurur",
        ["Dolaylı ayrım yalnız açık hakaretle oluşur", "Tarafsız görünen ve belirli bir grubu nesnel gerekçe olmadan ağır biçimde dezavantajlı kılan kurallar hiçbir zaman ayrımcılık oluşturmaz", "Dolaylı ayrım için herkesin tamamen aynı sonucu yaşaması zorunludur", "Bu tür ayrım yalnız iş sözleşmesinden bağımsız taşınmaz satışlarında mümkündür"],
        "6701 sayılı Kanun m.2, görünüşte ayrımcı olmayan uygulamanın sayılan temelle bağlantılı ve nesnel olarak haklılaştırılamayan dezavantaj yaratmasını dolaylı ayrımcılık sayar.",
        "Kuralın sözcükleri tarafsız olsa da etkisi değerlendirilir. Nesnel ve orantılı haklılaştırma bulunmuyorsa dolaylı ayrım doğabilir.",
        "6701 sayılı Kanun m.2", "hard",
    ),
    r(
        "Çalışanlar, dinleri nedeniyle ayrı bir alanda tutulmuş ve ortak eğitimlere alınmamıştır. Bu eylem 6701 sayılı Kanundaki hangi ayrım türüne örnektir?",
        "Kişilerin sayılan ayrım temeli nedeniyle eylem veya eylemsizlik sonucu diğerlerinden ayrı tutulmasına ne denir?",
        "Ayrı tutma",
        ["Makul düzenleme", "Olumlu tedbir", "Mesleki gereklilik", "İdari sürece katılım"],
        "6701 sayılı Kanun m.2, kişilerin sayılan temeller nedeniyle bir eylem veya eylemsizlik sonucu diğerlerinden ayrı tutulmasını 'ayrı tutma' olarak tanımlar.",
        "Fiziksel ayrıştırma yanında faaliyete erişimin engellenmesi de somut koşullara göre ayrı tutma oluşturabilir.",
        "6701 sayılı Kanun m.2 ve 4", "easy",
    ),
    r(
        "Şirket yöneticisi, insan kaynakları görevlisine belirli mezhepten adayları elemesi yönünde talimat vermiş ve görevli bu talimatı uygulamıştır. Hangisi doğrudur?",
        "Ayrımcılık yapılmasına yönelik talimatın verilmesi ve uygulanması nasıl değerlendirilir?",
        "Talimat verme ve talimatı uygulama ayrı ayrı ayrımcılık türleri arasındadır",
        ["Yalnız yazılı talimat ayrım sayılır", "Talimat uygulanırsa veren tamamen sorumsuz olur", "Ayrımcılık talimatı iş ilişkisinde kanunen zorunludur", "Talimatı uygulayan kişi ayrım yasağının kapsamı dışında kalır ve hiçbir sonuç doğmaz"],
        "6701 sayılı Kanun m.4, ayrımcılık talimatı verme ve bu talimatları uygulamayı ayrımcılık türleri arasında sayar.",
        "Ayrımcı kararın hiyerarşik talimat biçiminde kurulması yasağı ortadan kaldırmaz. Hem talimat hem uygulama denetlenir.",
        "6701 sayılı Kanun m.2 ve 4", "medium",
    ),
    r(
        "Bir çalışana hem yaşı hem engelliliğiyle bağlantılı tek bir ayrımcı uygulama yapılmıştır. Bu durum hangi kavramla ifade edilir?",
        "Ayrımcı uygulamanın birden fazla ayrımcılık temeliyle ilişkili olmasına ne denir?",
        "Çoklu ayrımcılık",
        ["Tekli ücret hesabı", "Makul düzenleme", "Doğrudan cinsiyet ayrımı", "Orantılı olumlu tedbir"],
        "6701 sayılı Kanun m.2, ayrımcı uygulamanın birden fazla ayrımcılık temeliyle ilişkili olmasını çoklu ayrımcılık olarak tanımlar.",
        "Temellerin kesişmesi ayrımın etkisini ağırlaştırabilir. Değerlendirme her bir temeli ve birlikte yarattıkları sonucu kapsar.",
        "6701 sayılı Kanun m.2 ve 4", "easy",
    ),
    r(
        "Yönetici, çalışanın etnik kökenine dayanarak onu işinden soğutmak ve dışlamak amacıyla kasıtlı eylemleri sürekli tekrarlamıştır. Kavram hangisidir?",
        "6701 sayılı Kanuna göre işyerinde yıldırma hangi amaç ve temele dayanan eylemleri ifade eder?",
        "Sayılan temele dayanıp kişiyi işinden soğutma, dışlama veya bıktırma amaçlı kasıtlı eylemler",
        ["Her iş eleştirisi yıldırmadır", "Yıldırma yalnız işyeri dışında meydana gelebilir", "İşyerinde yıldırma için hiçbir ayrım temeli, dışlama amacı veya kasıt aranmaz ve tek bir nesnel uyarı yeterlidir", "İşçinin performansına ilişkin nesnel ve ölçülü her geri bildirim yıldırma kabul edilir"],
        "6701 sayılı Kanun m.2, sayılan ayrım temellerine dayanarak kişiyi işinden soğutma, dışlama veya bıktırma amacıyla kasıtlı eylemleri işyerinde yıldırma sayar.",
        "Her çatışma bu özel tanıma girmez. Ayrım temeli, kasıt ve işten soğutma-dışlama-bıktırma amacı birlikte değerlendirilir.",
        "6701 sayılı Kanun m.2 ve 4", "hard",
    ),
    r(
        "Engelli çalışan görevini yerine getirebilmek için mali imkânlara göre ölçülü ve gerekli bir erişim düzenlemesi istemiş; işveren gerekçesiz reddetmiştir. Hangisi doğrudur?",
        "Makul düzenlemenin temel ölçütleri nelerdir?",
        "Belirli ihtiyaç için mali imkânlarla orantılı, ölçülü, gerekli ve uygun değişiklik yapılmalıdır",
        ["Her düzenleme maliyetten bağımsız sınırsız olmalıdır", "Makul düzenleme yalnız engelli olmayanlara sağlanır", "İşveren bütün talepleri hiçbir değerlendirme yapmadan reddedebilir", "Makul düzenleme yapmama, engellinin eşit yararlanmasını tümüyle engellese bile 6701 sayılı Kanunda ayrımcılık türü kabul edilmez"],
        "6701 sayılı Kanun m.2 makul düzenlemeyi engellinin eşit yararlanması için belirli durumda gereken, mali imkânlar nispetinde ölçülü, gerekli ve uygun tedbir olarak tanımlar.",
        "Kanun m.4 makul düzenleme yapmamayı ayrımcılık türü sayar. Talebin somut ihtiyaç, uygunluk, ölçülülük ve mali imkân yönleri birlikte incelenir.",
        "6701 sayılı Kanun m.2 ve 4", "hard",
    ),
    r(
        "İşveren vekili çalışanın dini nedeniyle insan onurunu çiğneyen, aşağılayıcı ve yıldırıcı sözler söylemiştir. 6701 sayılı Kanundaki kavram hangisidir?",
        "Taciz kavramı ayrım temeline dayanan hangi tür davranışları kapsar?",
        "İnsan onurunu çiğneme amacı taşıyan veya bu sonucu doğuran yıldırıcı ve aşağılayıcı davranışları",
        ["Her nezaket dışı söz hukuken tacizdir", "Taciz yalnız fiziksel zarar doğurursa mümkündür", "Psikolojik ve cinsel davranışlar taciz tanımının dışında kalır", "Ayrım temeline dayalı, insan onurunu çiğneyen ve aşağılayıcı davranış yalnız çalışma bittikten yıllar sonra taciz sayılır"],
        "6701 sayılı Kanun m.2, psikolojik ve cinsel türler dâhil sayılan temele dayalı; insan onurunu çiğneme amaçlı veya sonuçlu yıldırıcı, onur kırıcı, aşağılayıcı ya da utandırıcı davranışı taciz sayar.",
        "Amaç yanında sonuç da yeterli olabilir. Davranışın ayrım temeliyle bağlantısı ve insan onuruna etkisi incelenir.",
        "6701 sayılı Kanun m.2 ve 4", "medium",
    ),
    r(
        "Aday gerçekte belirli bir dine mensup değildir; ancak işveren onu o dine mensup sanarak işe almamıştır. Bu ayrım türü nedir?",
        "Kişi bir ayrım temelini gerçekte taşımadığı hâlde taşıdığı sanılarak ayrımcı muamele görürse hangi kavram uygulanır?",
        "Varsayılan temele dayalı ayrımcılık",
        ["Kişi temeli taşımıyorsa ayrım oluşmaz", "Yalnız çoklu ayrımcılık", "Makul mesleki gereklilik nedeniyle farklı işlem", "Eşitsizlikleri ortadan kaldırmaya yönelik ölçülü olumlu tedbir"],
        "6701 sayılı Kanun m.2, kişinin gerçekte ilgisi olmadığı bir ayrım temelini taşıdığı sanılarak ayrımcı muamele görmesini varsayılan temele dayalı ayrımcılık sayar.",
        "Koruma algıya dayalı ayrımı da kapsar. Zarar görenin o özelliği gerçekten taşıması şart değildir.",
        "6701 sayılı Kanun m.2 ve 4", "medium",
    ),
    r(
        "İşveren adayları medeni hâlleri ve sağlık durumları nedeniyle herhangi bir mesleki gereklilik olmadan elemiştir. 6701 sayılı Kanun bakımından hangisi doğrudur?",
        "6701 sayılı Kanunun ayrım yasağı temelleri arasında aşağıdakilerden hangileri yer alır?",
        "Medeni hâl ve sağlık durumu ayrım yasağı temelleri arasındadır",
        ["Yalnız göz rengi sayılmıştır", "Medeni hâl hiçbir zaman korunan temel değildir", "Sağlık durumu yalnız kamu çalışanlarında korunur", "Kanun sadece cinsiyet ve ırk temellerini sınırlı olarak kabul eder"],
        "6701 sayılı Kanun m.3; cinsiyet, ırk, renk, dil, din, inanç, mezhep, görüş, etnik köken, servet, doğum, medeni hâl, sağlık, engellilik ve yaş temellerini sayar.",
        "İstihdam kararlarında kişisel temel ile mesleki gereklilik arasındaki bağ incelenir. Keyfî sağlık veya medeni hâl ayrımı yasaktır.",
        "6701 sayılı Kanun m.3", "easy",
    ),
    r(
        "Kamu kurumu kendi görev alanında ayrımcılık ihlali tespit etmiştir. İhlal sona erse bile sonuçların giderilmesi ve tekrarın önlenmesi için ne yapmalıdır?",
        "Görevli kamu kurumlarının ayrımcılık yasağı ihlalindeki tedbir yükümlülüğü hangi amaçları kapsar?",
        "İhlali sona erdirme, sonuçları giderme, tekrarı önleme ve takibi sağlama tedbirlerini",
        ["Kurum yalnız ihlali kayda geçirir", "Sonuçların giderilmesi görev alanının dışındadır", "İhlal tekrarı için hiçbir önleyici tedbir alınamaz", "Kamu kurumu yalnız özel kişinin izniyle inceleme yapabilir; giderim ve önleme tedbiri alamaz"],
        "6701 sayılı Kanun m.3, görevli kamu kurumlarına ihlali sona erdirme, sonuçlarını giderme, tekrarını önleme ve adli-idari takibi sağlama tedbirleri alma görevi verir.",
        "Yükümlülük yalnız ihlalin durdurulmasıyla bitmez; giderim, önleme ve takip boyutları da vardır.",
        "6701 sayılı Kanun m.3", "medium",
    ),
    r(
        "Özel şirket, yetki alanındaki işe alım sürecinde ayrımcılık riskini bildiği hâlde hiçbir önleyici veya giderici tedbir almamıştır. Kanuni yükümlülüğü nedir?",
        "Ayrımcılık yasağından sorumlu gerçek ve özel hukuk tüzel kişileri kendi yetki alanlarında ne yapmalıdır?",
        "Ayrımcılığı tespit etme, ortadan kaldırma ve eşitliği sağlama tedbirlerini almalıdır",
        ["Özel kişiler eşitlik tedbiri alamaz", "Yalnız kesin mahkeme kararından sonra ilan vermekle yetinir", "Yetki alanındaki ayrımı görmezden gelmek kanuni yükümlülüktür", "Tedbir yükümlülüğü yalnız kamu kurumlarına ait olup işverenleri hiçbir zaman kapsamaz"],
        "6701 sayılı Kanun m.3, sorumlu gerçek ve özel hukuk tüzel kişilerine yetki alanlarında ayrımcılığın tespiti, kaldırılması ve eşitliğin sağlanması için tedbir yükler.",
        "İşveren ayrımcılık gerçekleşmeden önce önleyici, gerçekleştiğinde giderici kurumsal mekanizmalar kurmalıdır.",
        "6701 sayılı Kanun m.3", "medium",
    ),
    r(
        "Çalışan, ayrımcılık şikâyeti sürecine tanık olarak katıldığı için daha kötü vardiyaya verilmiştir. Bu olumsuz muamele nasıl değerlendirilir?",
        "Eşitlik sürecini başlatan veya sürece katılan kişinin bu nedenle olumsuz muamele görmesi hangi sonucu doğurur?",
        "Misilleme niteliğindeki olumsuz muamele de ayrımcılık oluşturur",
        ["Şikâyete katılan kişi korunmaz", "Olumsuz muamele yalnız ücret artışıysa ayrım sayılır", "İşveren sürece katılan herkese dilediği yaptırımı uygulayabilir", "Temsilciler ve tanıklar eşit muamele sürecinin sağladığı korumanın tamamen dışındadır"],
        "6701 sayılı Kanun m.4, eşitlik veya ayrımcılığı önleme için idari-adli süreci başlatan ya da katılanlar ile temsilcilerine bu nedenle yapılan olumsuz muameleyi ayrımcılık sayar.",
        "Misilleme yasağı şikâyet ve tanıklık mekanizmalarının etkili kullanılmasını güvence altına alır.",
        "6701 sayılı Kanun m.4", "medium",
    ),
    r(
        "İşveren ayrım yasağının yalnız işe başladıktan sonraki ücret döneminde geçerli olduğunu savunmaktadır. Oysa aday daha bilgi alma aşamasındadır. Hangisi doğrudur?",
        "6701 sayılı Kanunda istihdam ayrımcılığı yasağı işle ilgili hangi süreçleri kapsar?",
        "Bilgilenme, başvuru, seçim, işe alım, çalışma ve sona erme süreçlerinin tümünü kapsar",
        ["Yasak yalnız ilk ücret gününü kapsar", "İş başvurusundan önce bilgi isteyen kişi korunmaz", "Çalışmanın sona ermesi ayrım yasağının dışındadır", "Koruma yalnız kadrolu kamu çalışanlarına uygulanır; adaylar ve özel sektör kapsam dışıdır"],
        "6701 sayılı Kanun m.6, çalışanları, başvuranları, iş deneyimi edinmek veya bilgi almak isteyenleri; bilgilenmeden sona ermeye kadar işle ilgili tüm süreçlerde korur.",
        "Koruma yalnız kurulmuş iş sözleşmesine bağlı değildir. Aday, stajyer ve bilgi talep eden kişi de kapsamda olabilir.",
        "6701 sayılı Kanun m.6", "easy",
    ),
    r(
        "İş ilanı yaş temelinde ayrımcı koşul içeriyor; hizmetin zorunluluklarıyla bağlantılı, gerekli ve orantılı bir neden yoktur. İlan ayrım yasağı kapsamında mıdır?",
        "İstihdam ayrımcılığı yasağının iş ilanı dışında kapsadığı mesleki alanlara örnek hangisidir?",
        "İş ilanı, mesleki eğitim, yükselme, hizmet içi eğitim ve sosyal menfaatleri kapsar",
        ["İş ilanları kapsam dışıdır", "Yalnız işyerinin fiziksel adresi değerlendirilir", "Meslekte yükselme ve eğitimde ayrımcılık serbesttir", "Sosyal menfaatler ancak işveren isterse ayrım yasağına tabi olabilir ve denetlenemez"],
        "6701 sayılı Kanun m.6, iş ilanı, çalışma şartları, mesleki rehberlik ve eğitim, yükselme, hizmet içi eğitim ve sosyal menfaatleri açıkça kapsar.",
        "İşe erişim kadar kariyer gelişimi ve iş ilişkisindeki sosyal menfaatlere erişim de eşitlik denetimine tabidir.",
        "6701 sayılı Kanun m.6", "medium",
    ),
    r(
        "İşveren, adayın başvurusunu yalnız annelik ve çocuk bakımı gerekçesiyle reddetmiştir. İşin zorunlu niteliğine dayanan başka neden yoktur. Hangisi doğrudur?",
        "İstihdam başvurusunun hangi ailevi nedenlerle reddedilmesi 6701 sayılı Kanunda açıkça yasaklanmıştır?",
        "Gebelik, annelik ve çocuk bakımı gerekçeleriyle başvuru reddedilemez",
        ["Annelik her işte zorunlu ret nedenidir", "Çocuk bakımı yalnız ücret indirimi için kullanılabilir", "Gebelik temelli ret sadece özel işverenlerde serbesttir", "Başvuru aşaması istihdam ayrımcılığı yasağının hiçbir zaman kapsamına girmez"],
        "6701 sayılı Kanun m.6, işveren veya yetkilendirdiği kişinin başvuruyu gebelik, annelik ve çocuk bakımı gerekçeleriyle reddedemeyeceğini düzenler.",
        "Yasak işe alınmadan önce de geçerlidir. İşin gerçek ve zorunlu niteliğiyle bağlantısız ailevi varsayımlar ret nedeni yapılamaz.",
        "6701 sayılı Kanun m.6", "easy",
    ),
    r(
        "Bir sinema rolünde canlandırılacak tarihî kişinin cinsiyetinin rolün zorunlu niteliğiyle bağlantılı olduğu ve koşulun amaca uygun-orantılı kaldığı kabul edilmiştir. Farklı muamele mümkün müdür?",
        "Zorunlu mesleki gerekliliğe dayanan farklı muamelenin ayrım sayılmaması için hangi ölçütler aranır?",
        "Mesleki gereklilik bulunmalı ve farklı muamele amaca uygun ve orantılı olmalıdır",
        ["Her işveren tercihi mesleki gerekliliktir", "Farklı muamelenin amaçla bağlantısı aranmaz", "Orantılılık yalnız ücret ödenmediğinde değerlendirilir", "Zorunlu gereklilik bulunmasa bile cinsiyet ve yaş sınırsız ret nedeni yapılabilir"],
        "6701 sayılı Kanun m.7, zorunlu mesleki gereklilik varsa amaca uygun ve orantılı farklı muameleye istisna tanır; belirli cinsiyetin zorunlu olduğu durumları da sayar.",
        "İstisna dar yorumlanır. İşverenin kolaylığı değil işin gerçek gereği, meşru amaç ve orantılılık kanıtlanmalıdır.",
        "6701 sayılı Kanun m.7", "hard",
    ),
    r(
        "TİHEK'e yapılan yalnız ayrımcılık yasağı ihlali başvurusunda kişi, iddiasını destekleyen kuvvetli emare ve karine oluşturan olguları ortaya koymuştur. Sonraki ispat yükü kimdedir?",
        "6701 sayılı Kanun m.21'e göre başvuran kuvvetli emareleri gösterdiğinde karşı taraf neyi ispatlamalıdır?",
        "Karşı taraf ayrımcılık yasağı ve eşit muamele ilkesini ihlal etmediğini ispatlamalıdır",
        ["Karşı taraf hiçbir açıklama yapmaz", "Başvuran artık ilgisiz bütün işlemleri ispatlar", "Kuvvetli emare ispat yükünü tamamen ortadan kaldırır ve ihlali otomatik kesinleştirir", "İspat yükü yalnız başvuruyla ilgisi bulunmayan üçüncü kişiye ve kuruma geçer; işveren ihlal etmediğini hiçbir koşulda açıklamaz"],
        "6701 sayılı Kanun m.21, münhasıran ayrım başvurusunda kuvvetli emare veya karine olguları gösterilince karşı tarafa ihlal etmediğini ispat yükü verir.",
        "Başvuranın ilk gösterim yükü vardır; soyut iddia yeterli değildir. Kuvvetli emareden sonra açıklama ve karşı ispat yükü yer değiştirir.",
        "6701 sayılı Kanun m.21", "hard",
    ),
]


PREMISES = [
    {
        "stem": "İş Kanunundaki eşit davranma ilkesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dil ve siyasi düşünceye dayalı ayrım yasaktır.\n\nII. Esaslı sebep olmadan kısmi çalışana farklı işlem yapılamaz.\n\nIII. Belirli süreli olma her farklı işlemi tek başına haklı kılar.",
        "correct": "I ve II", "why": "İş Kanunu m.5 nedeniyle I ve II doğrudur. Salt belirli süreli olma farklı işlem için yeterli olmadığından III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.5", "difficulty": "medium",
    },
    {
        "stem": "Cinsiyet eşitliğiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aynı değerde iş için cinsiyet nedeniyle düşük ücret belirlenemez.\n\nII. Özel koruyucu hüküm daha düşük ücreti haklı kılmaz.\n\nIII. Gebelik temelli farklılık ancak biyolojik veya iş niteliği zorunlu kılıyorsa değerlendirilebilir.",
        "correct": "I, II ve III", "why": "İş Kanunu m.5 uyarınca üç ifade de doğrudur.",
        "ref": "4857 sayılı İş Kanunu m.5", "difficulty": "medium",
    },
    {
        "stem": "Ayrımcılık tazminatıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üst sınır dört aya kadar ücrettir.\n\nII. İşçi yoksun bırakıldığı hakları ayrıca isteyebilir.\n\nIII. Tazminat her ihlalde zorunlu olarak tam dört aylık ücret olur.",
        "correct": "I ve II", "why": "İş Kanunu m.5 nedeniyle I ve II doğrudur. Dört ay üst sınır olup sabit tutar olmadığından III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.5", "difficulty": "hard",
    },
    {
        "stem": "6701 sayılı Kanundaki ayrım türleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Doğrudan ayrımcılık açık farklı muameleyi kapsayabilir.\n\nII. Görünüşte tarafsız kural dolaylı ayrım yaratamaz.\n\nIII. Varsayılan temele dayalı ayrımda kişi özelliği gerçekte taşımayabilir.",
        "correct": "I ve III", "why": "6701 sayılı Kanun m.2 nedeniyle I ve III doğrudur. Görünüşte tarafsız uygulama haklılaştırılamayan dezavantaj yaratırsa dolaylı ayrım olabileceğinden II yanlıştır.",
        "ref": "6701 sayılı Kanun m.2", "difficulty": "medium",
    },
    {
        "stem": "Ayrımcılıkla mücadele araçlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Makul düzenleme yapmama ayrım türüdür.\n\nII. Ayrımcılık talimatını uygulama kanunun kapsamı dışındadır.\n\nIII. Ayrım şikâyetine katılana misilleme ayrımcılık oluşturabilir.",
        "correct": "I ve III", "why": "6701 sayılı Kanun m.4 nedeniyle I ve III doğrudur. Ayrımcılık talimatını uygulama da ayrım türü olduğundan II yanlıştır.",
        "ref": "6701 sayılı Kanun m.4", "difficulty": "medium",
    },
    {
        "stem": "İstihdamda ayrım yasağıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İş ilanı ve işe alım süreci kapsamdadır.\n\nII. Meslekte yükselme ve hizmet içi eğitim kapsamdadır.\n\nIII. Gebelik ve annelik nedeniyle başvuru reddedilemez.",
        "correct": "I, II ve III", "why": "6701 sayılı Kanun m.6 uyarınca üç ifade de doğrudur.",
        "ref": "6701 sayılı Kanun m.6", "difficulty": "medium",
    },
    {
        "stem": "Ayrım yasağının istisnalarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Zorunlu mesleki gereklilik amaca uygun ve orantılı farklılık sağlayabilir.\n\nII. Her işveren tercihi zorunlu mesleki gereklilik sayılır.\n\nIII. Eşitsizlikleri gidermeye yönelik gerekli ve orantılı tedbir ayrım iddiasına konu olmayabilir.",
        "correct": "I ve III", "why": "6701 sayılı Kanun m.7 nedeniyle I ve III doğrudur. İşverenin öznel tercihi tek başına mesleki gereklilik olmadığından II yanlıştır.",
        "ref": "6701 sayılı Kanun m.7", "difficulty": "hard",
    },
    {
        "stem": "İspat yüküyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşçi güçlü ihlal ihtimalini gösterirse işveren ihlal olmadığını ispatlar.\n\nII. TİHEK başvurusunda kuvvetli emare sonrası karşı ispat yükü doğabilir.\n\nIII. Soyut iddia her iki kanunda da ihlali otomatik kesinleştirir.",
        "correct": "I ve II", "why": "İş Kanunu m.5 ile 6701 sayılı Kanun m.21 nedeniyle I ve II doğrudur. Her iki düzende de önce güçlü olgu veya emare gerektiğinden III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.5; 6701 sayılı Kanun m.21", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="is_hukuku", topic_id="esit_davranma",
        label="Eşit Davranma İlkesi", slug="esit_davranma",
        prefix="kh-esit", seed=20260729,
        legislation_version="4857 sayılı İş Kanunu m.5 ve 6701 sayılı Kanun m.2–7, 21 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
