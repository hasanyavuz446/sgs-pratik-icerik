#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM İş Hukuku — İş Sözleşmesi konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde Çalışma ve Sosyal Güvenlik Bakanlığından alınan
güncel 4857 sayılı İş Kanunu m.2 ve m.6–16 metnidir.
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
        "A gerçek kişi olarak B şirketine ait işyerinde bir iş sözleşmesine dayanıp bağımlı çalışmaktadır. Kanuni sıfatlar bakımından hangisi doğrudur?",
        "4857 sayılı Kanuna göre işçi ve işveren kavramlarını ayıran temel tanım hangisidir?",
        "İş sözleşmesiyle çalışan gerçek kişi işçi, işçi çalıştıran kişi veya kuruluş işverendir",
        ["İşçi yalnız tüzel kişi, işveren ise yalnız kamu kurumu olabilir", "İş ilişkisi işçinin işveren adına şirket kurmasıyla meydana gelir", "Ücret alan herkes, iş sözleşmesi ve bağımlılık unsuru aranmadan her koşulda işçi sayılır", "İşveren sıfatı yalnız işyerinin binasına malik olan gerçek kişiye aittir"],
        "İş Kanunu m.2, iş sözleşmesine dayanarak çalışan gerçek kişiyi işçi; işçi çalıştıran gerçek veya tüzel kişi yahut kişiliği olmayan kuruluşu işveren sayar.",
        "İşçi gerçek kişidir ve iş sözleşmesine dayanır. İşverenin tüzel kişi veya tüzel kişiliği bulunmayan kurum olması mümkündür.",
        "4857 sayılı İş Kanunu m.2", "easy",
    ),
    r(
        "İşveren adına hareket ederek işletmenin yönetiminde görev alan müdür, işçilere karşı bu sıfatla işlem yapmıştır. Bu işlemlerden doğrudan kim sorumludur?",
        "İşveren vekilinin bu sıfatla işçilere karşı yaptığı işlem ve yükümlülüklerden doğrudan sorumluluk kime aittir?",
        "İşveren vekilinin işlemlerinden doğrudan işveren sorumludur",
        ["İşçi bütün sonuçlardan işveren yerine tek başına sorumludur", "İşveren vekilinin işlemleri hiçbir kişiyi hukuken bağlamaz", "Sorumluluk yalnız işveren vekilinin ailesine geçer", "İşveren, vekilin yönetim işlemlerinden kanunen daima ayrıdır"],
        "İş Kanunu m.2, işveren vekilinin bu sıfatla işçilere karşı işlem ve yükümlülüklerinden doğrudan işvereni sorumlu tutar.",
        "İşveren için öngörülen yükümlülükler vekile de uygulanır; vekillik işçinin hak ve borçlarını ortadan kaldırmaz.",
        "4857 sayılı İş Kanunu m.2", "easy",
    ),
    r(
        "İşveren, asıl işinin bir bölümünü yalnız maliyeti azaltmak için, işletme ve iş gereği ile teknolojik uzmanlık koşulları bulunmadan başka işverene vermiştir. İlişki geçerli midir?",
        "Asıl işin bir bölümünün alt işverene verilebilmesi hangi temel koşula bağlıdır?",
        "İşletme ve işin gereği ile teknolojik nedenlerle uzmanlık gerektirmelidir",
        ["Asıl işin her bölümü hiçbir koşul aranmadan alt işverene verilebilir", "Uzmanlık yalnız alt işverenin daha az ücret ödemesiyle oluşur", "Asıl iş sadece işçilerin sözlü onayı alınırsa bölünebilir", "Alt işverenlik için asıl işverenin faaliyetini tamamen durdurması gerekir"],
        "İş Kanunu m.2, asıl işin bölümünün alt işverene verilmesini işletme ve işin gereği ile teknolojik nedenlerle uzmanlık koşuluna bağlar.",
        "Yardımcı işlerde alt işverenlik mümkündür. Asıl işin bölünmesinde ise kanundaki uzmanlık koşulları birlikte aranır.",
        "4857 sayılı İş Kanunu m.2", "hard",
    ),
    r(
        "Alt işveren işçisinin o işyeriyle ilgili ve iş sözleşmesinden doğan ücreti ödenmemiştir. Asıl işveren sorumluluğun yalnız alt işverene ait olduğunu savunmuştur. Hangisi doğrudur?",
        "Asıl işveren, alt işveren işçilerine karşı hangi yükümlülüklerden alt işverenle birlikte sorumludur?",
        "İşyeriyle ilgili kanun, iş ve toplu iş sözleşmesi yükümlülüklerinden birlikte sorumludur",
        ["Asıl işveren, işyeriyle ilgili ücret ve toplu iş sözleşmesi borçlarında dahi alt işveren işçisine karşı hiçbir durumda sorumlu olmaz", "Birlikte sorumluluk yalnız işçinin asıl işverene ortak olmasıyla doğar", "Alt işverenin ücret borcu kendiliğinden işçinin ailesine geçer", "Sorumluluk sadece işyeri dışındaki ilgisiz özel borçları kapsar"],
        "İş Kanunu m.2, asıl işvereni alt işveren işçilerine karşı kanundan, iş sözleşmesinden ve alt işverenin toplu iş sözleşmesinden doğan işyeri yükümlülüklerinde birlikte sorumlu tutar.",
        "Birlikte sorumluluk işçiye her iki işverene başvurma güvencesi sağlar. Yükümlülüğün ilgili işyeriyle bağlantılı olması gerekir.",
        "4857 sayılı İş Kanunu m.2", "medium",
    ),
    r(
        "Asıl işverenin işçisi hakları kısıtlanarak kâğıt üzerinde alt işveren işçisi yapılmış, çalışma aynı biçimde sürmüştür. Muvazaanın sonucu nedir?",
        "Muvazaalı asıl işveren-alt işveren ilişkisinde alt işveren işçileri hangi tarihten itibaren kimin işçisi sayılır?",
        "Başlangıçtan itibaren asıl işverenin işçisi sayılarak işlem görürler",
        ["İşçiler hiçbir işverene bağlı olmayan gönüllü çalışan sayılır", "Muvazaa yalnız işçinin ücretini kendiliğinden yarıya indirir", "İşçiler muvazaa tarihinden önceki bütün haklarını kaybeder", "Alt işverenlik muvazaalı olsa da ilişki daima geçerli kalır"],
        "İş Kanunu m.2, muvazaalı ilişkide alt işveren işçilerini başlangıçtan itibaren asıl işveren işçisi sayar.",
        "Asıl işveren işçisinin hakları kısıtlanarak alt işverene geçirilmesi korunmaz. Kanun görünüşü değil gerçek iş ilişkisini esas alır.",
        "4857 sayılı İş Kanunu m.2", "medium",
    ),
    r(
        "İşyeri hukuki işlemle başka işverene devredilmiştir. Devir tarihinde mevcut iş sözleşmelerinin sona erdiği ileri sürülmektedir. Kanuni sonuç nedir?",
        "İşyeri veya bölümünün hukuki işlemle devrinde mevcut iş sözleşmeleri ne olur?",
        "Mevcut iş sözleşmeleri bütün hak ve borçlarıyla devralana geçer",
        ["Bütün sözleşmeler devir anında tazminatsız sona erer", "Sözleşmeler yalnız işçiler yeniden sınava girerse devam eder", "Devir işçilerin kıdemini her durumda sıfırlar", "Haklar tamamen devredende kalır, bütün borçlar işçiye geçer ve devralan hiçbir yükümlülük üstlenmez"],
        "İş Kanunu m.6 uyarınca devir tarihinde mevcut iş sözleşmeleri bütün hak ve borçlarıyla devralana geçer.",
        "Devralan, hizmet süresine bağlı haklarda işçinin devreden yanında işe başladığı tarihi esas alır.",
        "4857 sayılı İş Kanunu m.6", "easy",
    ),
    r(
        "İşveren iş sözleşmesini yalnız işyerinin başka birine devredilmiş olmasına dayanarak feshetmiştir. Başka ekonomik veya organizasyonel neden yoktur. Hangisi doğrudur?",
        "İşyeri devri tek başına işçi veya işveren yönünden fesih sebebi oluşturur mu?",
        "Sırf devir fesih için geçerli veya haklı sebep oluşturmaz",
        ["Devir bütün iş sözleşmelerini zorunlu olarak aynı gün sona erdirir", "İşçi devri öğrenince bütün haklarını kaybetmiş sayılır", "Devralan her işçiyi hiçbir gerekçe olmadan tazminatsız çıkarabilir", "Devir yalnız ücretin ödenmemesi şartıyla fesih sebebi sayılmaz"],
        "İş Kanunu m.6, sırf işyeri devrini işveren için fesih ve işçi için haklı fesih sebebi saymaz.",
        "Ekonomik, teknolojik ve organizasyonel nedenlere dayalı fesihler ile tarafların diğer haklı fesih hakları saklıdır.",
        "4857 sayılı İş Kanunu m.6", "medium",
    ),
    r(
        "İşçi özel istihdam bürosunun işçisi olarak başka işverenin yanında geçici görevlendirilmiştir. Bu ilişkide işveren sıfatı kimdedir?",
        "Özel istihdam bürosu aracılığıyla kurulan geçici iş ilişkisinde işçinin işvereni kimdir?",
        "Geçici işçinin işvereni özel istihdam bürosudur",
        ["Geçici işçinin hiçbir işvereni bulunmaz", "İşveren yalnız Türkiye İş Kurumudur", "İşçi geçici görevlendirmeyle kendi işvereni olur", "İşveren sıfatı her gün iki işveren arasında kura ile değişir"],
        "İş Kanunu m.7, özel istihdam bürosu aracılığındaki geçici iş ilişkisinde işverenin büro olduğunu açıkça düzenler.",
        "Geçici işçi çalıştıran işveren talimat ve iş sağlığı güvenliği gibi kanuni yükümlülükler taşır; bu durum büroyla kurulu iş sözleşmesini ortadan kaldırmaz.",
        "4857 sayılı İş Kanunu m.7", "medium",
    ),
    r(
        "A, B'nin iş organizasyonu içinde ona bağımlı iş görmeyi; B de bunun karşılığında ücret ödemeyi üstlenmiştir. Bu sözleşme nasıl tanımlanır?",
        "İş sözleşmesinin iki temel karşılıklı edimi hangileridir?",
        "İşçinin bağımlı iş görmesi ve işverenin ücret ödemesidir",
        ["İşçinin bağımsız şirket kurması ve işverenin ortak olmasıdır", "İşverenin ücretsiz çalışması ve işçinin kira ödemesidir", "Tarafların yalnız gelecekte görüşme sözü vermesidir", "İşçinin ücret ödeyip işverenin hiçbir edim üstlenmemesidir"],
        "İş Kanunu m.8 iş sözleşmesini işçinin bağımlı iş görme, işverenin ücret ödeme borçlarından oluşan sözleşme olarak tanımlar.",
        "Bağımlılık iş sözleşmesini eser veya vekâlet gibi ilişkilerden ayıran başlıca ölçüttür. Ücret karşı edimdir.",
        "4857 sayılı İş Kanunu m.8", "easy",
    ),
    r(
        "Taraflar on sekiz ay sürecek iş sözleşmesini yalnız sözlü kurmuştur. Yazılı şekil bakımından hangisi doğrudur?",
        "Süresi bir yıl veya daha fazla olan iş sözleşmesinin şekli nasıl olmalıdır?",
        "Bir yıl ve daha uzun iş sözleşmesi yazılı yapılmalıdır",
        ["Bütün iş sözleşmeleri yalnız noter senediyle kurulabilir", "Bir yılı aşan sözleşmeler mutlaka sözlü yapılmalıdır", "Yazılı şekil sadece bir günden kısa işlerde aranır", "İş sözleşmesinde hiçbir süre için yazılı şekil kullanılamaz"],
        "İş Kanunu m.8 genel şekil serbestisini kabul eder; ancak süresi bir yıl ve daha fazla iş sözleşmelerinde yazılı şekli zorunlu kılar.",
        "Yazılı belgeler damga vergisi ile her çeşit resim ve harçtan muaftır. Özel kanuni şekiller ayrıca saklıdır.",
        "4857 sayılı İş Kanunu m.8", "easy",
    ),
    r(
        "Yazılı sözleşme yapılmamış, iş ilişkisi devam etmektedir. İşveren çalışma koşulları ve ücret bilgilerini gösteren belgeyi vermemiştir. Genel süre nedir?",
        "Yazılı sözleşme bulunmadığında çalışma koşullarını gösteren belgenin işçiye verilme süresi kural olarak ne kadardır?",
        "İşveren belgeyi en geç iki ay içinde vermelidir",
        ["Belge yalnız işçi emekli olduktan sonra verilir", "İşverenin hiçbir yazılı bilgi verme yükümlülüğü yoktur", "Belge sözleşmenin kurulmasından önce on yıl içinde verilebilir", "Belge yalnız ücret ödenmediğinde mahkeme tarafından hazırlanır"],
        "İş Kanunu m.8, yazılı sözleşme yoksa genel ve özel koşulları içeren belgenin en geç iki ayda verilmesini öngörür.",
        "Bir ayı geçmeyen belirli süreli sözleşmede bu hüküm uygulanmaz. İlişki iki ay dolmadan biterse bilgi en geç sona erme tarihinde verilmelidir.",
        "4857 sayılı İş Kanunu m.8", "medium",
    ),
    r(
        "Taraflar kanuni sınırlara uyarak ihtiyaçlarına uygun kısmi ve belirli süreli bir iş sözleşmesi düzenlemiştir. Tür belirleme bakımından hangisi doğrudur?",
        "Tarafların iş sözleşmesinin türü ve çalışma biçimini belirleme serbestisinin sınırı nedir?",
        "Kanuni sınırlamalar içinde ihtiyaçlarına uygun sözleşme türü seçebilirler",
        ["Taraflar yalnız belirsiz ve tam süreli sözleşme yapabilir", "İş sözleşmesinin türü her durumda rastgele üçüncü kişi tarafından seçilir", "Kanuni sınırlamalar sözleşme türlerine hiçbir zaman uygulanmaz", "Deneme ve kısmi çalışma biçimleri kanunen bütünüyle yasaktır"],
        "İş Kanunu m.9 taraflara kanuni sınırlamalar saklı kalmak üzere ihtiyaçlarına uygun tür ve çalışma biçimi seçme serbestisi tanır.",
        "Belirli-belirsiz, tam-kısmi ve deneme süreli biçimler mümkündür. Serbesti, emredici koruma hükümlerini bertaraf edemez.",
        "4857 sayılı İş Kanunu m.9", "medium",
    ),
    r(
        "Niteliği gereği yirmi sekiz iş günü sürecek bir iş için sözleşme yapılmıştır. İş sürekli mi süreksiz mi sayılır?",
        "Niteliği bakımından en çok kaç iş günü süren işler süreksiz iş kabul edilir?",
        "En çok otuz iş günü süren işler süreksiz iş sayılır",
        ["Bir iş günü süren bütün işler sürekli iş sayılır", "Süreksiz iş için alt sınır üç yüz iş günüdür", "İşin niteliği değil yalnız işçinin yaşı belirleyicidir", "Otuz iş gününden uzun bütün işler de süreksizdir"],
        "İş Kanunu m.10 nitelik bakımından en çok otuz iş günü süren işi süreksiz, daha fazla devam edeni sürekli iş sayar.",
        "Ölçüt sözleşmede yazılan keyfî süre değil, işin niteliğine göre süresidir. Süreksiz işte bazı konular TBK hükümlerine tabidir.",
        "4857 sayılı İş Kanunu m.10", "easy",
    ),
    r(
        "İş ilişkisinin ne kadar süreceği kararlaştırılmamış, belirli süreyi haklı kılan objektif koşul da bulunmamaktadır. Sözleşmenin türü nedir?",
        "İş ilişkisinin bir süreye bağlı kurulmadığı durumda sözleşme kural olarak nasıl nitelendirilir?",
        "İş sözleşmesi belirsiz süreli sayılır",
        ["Sözleşme kendiliğinden bir günlük belirli süreli olur", "İş ilişkisi süre yazılmadığı için kesin olarak hükümsüzdür", "Sözleşme yalnız işverenin istediği gün geçmişe etkili doğar", "Süre belirtilmemesi sözleşmeyi ortaklık sözleşmesine çevirir"],
        "İş Kanunu m.11, iş ilişkisinin bir süreye bağlı kurulmadığı hâlde sözleşmeyi belirsiz süreli sayar.",
        "Belirli süreli sözleşme istisnai koşullara dayanır. Süre kaydı yoksa belirsiz süreli ilişki esastır.",
        "4857 sayılı İş Kanunu m.11", "easy",
    ),
    r(
        "İşveren kalıcı ve sürekli iş için objektif neden göstermeden art arda belirli süreli sözleşmeler yapmıştır. Zincirlemenin sonucu nedir?",
        "Belirli süreli iş sözleşmelerinin esaslı neden olmadan zincirleme yapılmasının sonucu nedir?",
        "Sözleşme başlangıçtan itibaren belirsiz süreli kabul edilir",
        ["Her yenileme işçinin kıdemini zorunlu olarak sıfırlar", "Zincirleme sözleşmeler hiçbir koşulda belirsiz süreliye dönüşmez", "Sözleşme yalnız son gün için geçerli bir eser sözleşmesi olur", "Esaslı neden yokluğu işçiyi işveren vekili hâline getirir"],
        "İş Kanunu m.11, esaslı neden olmaksızın zincirlenen belirli süreli sözleşmeyi başlangıçtan itibaren belirsiz süreli kabul eder.",
        "Esaslı nedene dayanan zincirleme sözleşmeler belirli süreli niteliğini korur. Kural kötüye kullanmayı önler.",
        "4857 sayılı İş Kanunu m.11", "medium",
    ),
    r(
        "Belirli süreli işçi, yalnız sözleşmesinin süreli olması gerekçesiyle aynı işi yapan belirsiz süreli işçiden daha düşük haklara tabi tutulmuştur. Haklı neden yoktur. Hangisi doğrudur?",
        "Belirli süreli işçiye emsal belirsiz süreli işçiden farklı işlem yapılabilmesinin temel koşulu nedir?",
        "Farklı işlemi haklı kılan objektif bir neden bulunmalıdır",
        ["Süreli sözleşme her türlü farklı işlemi tek başına haklı kılar", "Belirli süreli işçi hiçbir işçilik hakkından yararlanamaz", "Emsal işçi yalnız başka ülkedeki ilgisiz işyerinden seçilir", "Farklı işlem için işverenin açıklamasız tercihi yeterlidir"],
        "İş Kanunu m.12, haklı neden olmadıkça salt belirli süreli olma nedeniyle emsal işçiye göre farklı işlemi yasaklar.",
        "Bölünebilir parasal menfaatler çalışılan süreye orantılı verilir. Emsal öncelikle aynı işyerindeki aynı veya benzeri işte çalışan belirsiz süreli işçidir.",
        "4857 sayılı İş Kanunu m.12", "medium",
    ),
    r(
        "İşçinin haftalık süresi emsal tam süreli işçiye göre önemli ölçüde daha az kararlaştırılmıştır. Sözleşme hangi türdedir?",
        "Kısmi süreli iş sözleşmesinin ayırt edici çalışma süresi ölçütü nedir?",
        "Haftalık süre emsal tam süreli işçiden önemli ölçüde daha azdır",
        ["Haftalık süre emsal işçiden mutlaka daha uzun olmalıdır", "Kısmi süre yalnız işçinin ücretsiz çalışmasıyla oluşur", "Çalışma süresi tür ayrımında hiçbir rol oynamaz", "Kısmi sözleşmede işveren ücret ödememeyi üstlenir"],
        "İş Kanunu m.13, normal haftalık süresi emsal tam süreli işçiye göre önemli ölçüde az olan sözleşmeyi kısmi süreli sayar.",
        "Kısmi süreli çalışma tek başına daha düşük işlem sebebi değildir. Süre ve bölünebilir menfaatler orantı ilkesine tabidir.",
        "4857 sayılı İş Kanunu m.13", "easy",
    ),
    r(
        "Kısmi süreli işçinin ikramiye gibi bölünebilir parasal menfaati hesaplanmaktadır. Haklı bir ayrım nedeni bulunmamaktadır. Ödeme nasıl yapılır?",
        "Kısmi süreli işçinin ücret ve paraya ilişkin bölünebilir menfaatleri nasıl belirlenir?",
        "Emsal tam süreli işçiye göre çalıştığı süreyle orantılı ödenir",
        ["Kısmi işçiye hiçbir bölünebilir parasal menfaat ödenmez", "Menfaat her durumda emsal işçinin iki katı belirlenir", "Ödeme yalnız işverenin sonraki yıl yapacağı kuraya bağlıdır", "Kısmi çalışma işçinin temel ücret hakkını tamamen kaldırır"],
        "İş Kanunu m.13, kısmi süreli işçinin bölünebilir parasal menfaatlerini emsal tam süreliye göre çalışma süresi oranında ödetir.",
        "Orantı eşit davranma ilkesinin uygulamasıdır. Bölünemeyen haklar sırf kısmi çalışma nedeniyle dışlanamaz.",
        "4857 sayılı İş Kanunu m.13", "medium",
    ),
    r(
        "Kısmi süreli işçi, niteliğine uygun boş tam süreli pozisyona geçmek istediğini bildirmiştir. İşverenin genel yükümlülüğü nedir?",
        "Kısmi-tam süreli geçiş istekleri ve açık pozisyonlar bakımından işveren ne yapmalıdır?",
        "Geçiş isteklerini dikkate almalı ve boş yerleri zamanında duyurmalıdır",
        ["Bütün geçiş isteklerini incelemeden kesin olarak reddetmelidir", "Boş pozisyonları yalnız işyeri dışındaki kişilere gizlice bildirmelidir", "Kısmi işçiyi talebi nedeniyle tazminatsız işten çıkarmalıdır", "Tam süreli pozisyonları hiçbir çalışana duyurmaması zorunludur"],
        "İş Kanunu m.13 işverene niteliklere uygun geçiş isteklerini dikkate alma ve boş yerleri zamanında duyurma yükümlülüğü verir.",
        "Hüküm otomatik atama hakkı değil, gerçek değerlendirme ve bilgilendirme güvencesi sağlar.",
        "4857 sayılı İş Kanunu m.13", "medium",
    ),
    r(
        "Yazılı sözleşmede işçinin yalnız ihtiyaç doğduğunda çağrılarak çalışacağı kararlaştırılmıştır. Bu çalışma biçimi nasıl nitelendirilir?",
        "Çağrı üzerine çalışmaya dayalı iş ilişkisi hangi sözleşme türüdür?",
        "Çağrı üzerine çalışma, kısmi süreli bir iş sözleşmesidir",
        ["Çağrı üzerine çalışma zorunlu olarak ücretsiz stajdır", "Bu ilişki hiçbir iş sözleşmesi niteliği taşımaz", "Çağrı kaydı işçiyi işverenin ortağı hâline getirir", "Çağrılı çalışma yalnız belirsiz ücretli kira sözleşmesidir"],
        "İş Kanunu m.14, ihtiyaç hâlinde iş görmenin yazılı kararlaştırıldığı çağrı üzerine çalışmayı kısmi süreli iş sözleşmesi sayar.",
        "Çağrı üzerine çalışma yazılı kurulmalıdır. İşçi belirlenen çalışma süresinde çağrılsa da çağrılmasa da ücrete hak kazanır.",
        "4857 sayılı İş Kanunu m.14", "easy",
    ),
    r(
        "Çağrı üzerine sözleşmede hafta, ay veya yıl içinde çalışılacak süre hiç belirlenmemiştir. Kanuni varsayım nedir?",
        "Çağrı üzerine çalışmada taraflar süreyi belirlememişse haftalık çalışma süresi kaç saat sayılır?",
        "Haftalık çalışma süresi yirmi saat kararlaştırılmış sayılır",
        ["Haftalık süre sıfır saat sayılır ve ücret hakkı doğmaz", "Süre her hafta işverenin sınırsız tercihine bırakılır", "Haftalık süre otomatik olarak yüz saat kabul edilir", "Belirsizlik sözleşmeyi geçmişe etkili olarak hükümsüz kılar"],
        "İş Kanunu m.14, taraflar zaman dilimindeki süreyi belirlememişse haftalık yirmi saat kararlaştırılmış sayar.",
        "Varsayılan süre işçiye asgari ücret güvencesi sağlar. Belirlenen sürede çağrılmasa bile ücret hakkı vardır.",
        "4857 sayılı İş Kanunu m.14", "medium",
    ),
    r(
        "Aksi kararlaştırılmamış çağrı üzerine işte işveren çağrıyı bir gün önce yapmış, günlük süre de sözleşmede yazılmamıştır. Kanuna uygunluk nedir?",
        "Çağrı süresi ve kararlaştırılmamış günlük çalışma bakımından genel kanuni alt sınırlar nedir?",
        "Çağrı en az dört gün önce yapılmalı, her çağrıda en az dört saat çalıştırılmalıdır",
        ["Çağrı çalışma bittikten sonra yapılabilir ve süre bir dakika olabilir", "İşveren çağrıyı hiçbir zaman işçiye bildirmek zorunda değildir", "Günlük süre yazılmamışsa işçi her çağrıda aralıksız yirmi dört saat çalıştırılmak zorundadır", "Dört günlük çağrı kuralı yalnız işçi ücret istemezse uygulanır"],
        "İş Kanunu m.14 aksi yoksa çağrının en az dört gün önce yapılmasını; günlük süre yoksa her çağrıda en az dört saat üst üste çalıştırmayı öngörür.",
        "Ön bildirim işçinin zamanını planlamasını, asgari blok ise anlamsız derecede kısa çağrıları önlemeyi amaçlar.",
        "4857 sayılı İş Kanunu m.14", "medium",
    ),
    r(
        "İşçi işverenin organizasyonu içinde, teknolojik araçlarla evinden çalışacaktır. Taraflar ilişkiyi sözlü kurmuştur. Uzaktan çalışma bakımından hangisi doğrudur?",
        "Uzaktan çalışma ilişkisinin kurulması hangi şekle bağlıdır?",
        "Uzaktan çalışma iş sözleşmesi yazılı kurulmalıdır",
        ["Uzaktan çalışma yalnız sözlü ve tanıksız kurulabilir", "Evden çalışma hiçbir iş ilişkisi niteliği taşımaz", "Yazılı şekil sadece işçi işyerinde çalışırsa aranır", "Uzaktan çalışma işvereni ücret borcundan kurtarır"],
        "İş Kanunu m.14, işveren organizasyonu içinde evde veya teknolojik araçlarla işyeri dışında yapılan uzaktan çalışmayı yazılı iş ilişkisi olarak düzenler.",
        "Sözleşmede işin tanımı, biçimi, yeri, süresi, ücret, ekipman, iletişim ve çalışma koşulları yer alır.",
        "4857 sayılı İş Kanunu m.14", "easy",
    ),
    r(
        "Uzaktan çalışan, yalnız sözleşmesinin uzaktan çalışma niteliği gerekçe gösterilerek emsal işçiden daha kötü koşullara tabi tutulmuştur. Esaslı neden yoktur. Hangisi doğrudur?",
        "Uzaktan çalışanların emsal işçiye göre farklı işleme tabi tutulmasının sınırı nedir?",
        "Esaslı neden yoksa salt uzaktan çalışma nedeniyle farklı işlem yapılamaz",
        ["Uzaktan çalışan bütün işçilik haklarını otomatik olarak kaybeder", "Farklı işlem için yalnız işverenin sözlü tercihi yeterlidir", "Eşit işlem ilkesi hiçbir uzaktan çalışma ilişkisinde uygulanmaz", "Uzaktan çalışma iş sağlığı ve güvenliği yükümlülüklerini kaldırır"],
        "İş Kanunu m.14, esaslı neden olmadıkça salt uzaktan çalışma niteliği yüzünden emsal işçiden farklı işlemi yasaklar.",
        "İşveren işin niteliğine göre bilgilendirme, eğitim, sağlık gözetimi ve ekipman güvenliği önlemlerini de almakla yükümlüdür.",
        "4857 sayılı İş Kanunu m.14", "medium",
    ),
    r(
        "Bireysel iş sözleşmesine altı aylık deneme kaydı konulmuştur. Toplu iş sözleşmesinde süreyi uzatan hüküm yoktur. Geçerli azami süre nedir?",
        "Deneme süresi bireysel ve toplu iş sözleşmesiyle en çok ne kadar kararlaştırılabilir?",
        "Bireysel sözleşmede iki ay, toplu iş sözleşmesiyle dört aya kadar olabilir",
        ["Deneme süresi bireysel sözleşmede hiçbir üst sınıra bağlı olmadan tarafların istediği kadar uzun ve sınırsız belirlenebilir", "Toplu iş sözleşmesi deneme süresini hiçbir zaman değiştiremez", "Deneme kaydı her iş sözleşmesinde kanunen zorunludur", "Deneme süresi yalnız işçi ücret almazsa bir yıl olabilir"],
        "İş Kanunu m.15 deneme süresini en çok iki ay; toplu iş sözleşmesiyle uzatıldığında dört ay olarak sınırlar.",
        "Deneme kaydı zorunlu değildir. Konulmuşsa kanuni azami süreyi aşan kısmı korunmaz.",
        "4857 sayılı İş Kanunu m.15", "easy",
    ),
    r(
        "İşveren deneme süresi içinde sözleşmeyi bildirim süresi vermeden sona erdirmiştir. İşçi çalıştığı günlerin ücretini istemektedir. Sonuç nedir?",
        "Deneme süresinde fesih ve işçinin çalışılmış günlere ilişkin hakları nasıl düzenlenmiştir?",
        "Taraflar bildirimsiz ve tazminatsız feshedebilir; çalışılan günlerin hakları saklıdır",
        ["Deneme süresinde işçi, fiilen çalıştığı günler için ücret ve diğer haklarını hiçbir koşulda talep edemez", "Fesih için her durumda sekiz haftalık bildirim verilmesi gerekir", "Deneme süresinde yalnız işçi tazminat ödeyerek feshedebilir", "Çalışılmış günler iş sözleşmesi sona erince yok sayılır"],
        "İş Kanunu m.15 taraflara deneme süresinde bildirimsiz ve tazminatsız fesih yetkisi verir; çalışılan günlerin ücret ve diğer haklarını korur.",
        "Deneme, ücretsiz çalışma dönemi değildir. Fesih kolaylığı geçmiş çalışma karşılıklarını ortadan kaldırmaz.",
        "4857 sayılı İş Kanunu m.15", "medium",
    ),
]


PREMISES = [
    {
        "stem": "İş ilişkisinin temel kavramlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşçi, iş sözleşmesine dayanarak çalışan gerçek kişidir.\n\nII. İşveren vekilinin bu sıfatla yaptığı işlemlerden doğrudan işveren sorumludur.\n\nIII. İşveren vekilliği işçinin haklarını ortadan kaldırmaz.",
        "correct": "I, II ve III", "why": "İş Kanunu m.2 uyarınca üç ifade de doğrudur.",
        "ref": "4857 sayılı İş Kanunu m.2", "difficulty": "medium",
    },
    {
        "stem": "İş sözleşmesinin şekliyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kanunda aksi yoksa iş sözleşmesi özel şekle tabi değildir.\n\nII. Bir yıl ve daha uzun sözleşme yazılı yapılmalıdır.\n\nIII. Yazılı sözleşme yoksa işverenin kanuni bilgi belgesi verme yükümlülüğü olabilir.",
        "correct": "I, II ve III", "why": "İş Kanunu m.8 uyarınca üç ifade de doğrudur.",
        "ref": "4857 sayılı İş Kanunu m.8", "difficulty": "medium",
    },
    {
        "stem": "Belirli süreli iş sözleşmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Objektif koşula dayanabilir.\n\nII. Esaslı neden olmadan zincirlenirse başlangıçtan itibaren belirsiz sayılır.\n\nIII. Salt süreli olması her türlü farklı işlemi haklı kılar.",
        "correct": "I ve II", "why": "İş Kanunu m.11 nedeniyle I ve II doğrudur. Salt süreli olma farklı işlem için yeterli olmadığından III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.11-12", "difficulty": "medium",
    },
    {
        "stem": "Kısmi süreli çalışmayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Haftalık süre emsal tam süreliye göre önemli ölçüde daha azdır.\n\nII. Bölünebilir parasal menfaatler süreyle orantılı ödenir.\n\nIII. Kısmi işçinin tam süreliye geçiş isteği hiçbir zaman dikkate alınmaz.",
        "correct": "I ve II", "why": "İş Kanunu m.13 nedeniyle I ve II doğrudur. Geçiş istekleri dikkate alınacağından III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.13", "difficulty": "medium",
    },
    {
        "stem": "Çağrı üzerine çalışmayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yazılı ve kısmi süreli bir iş sözleşmesidir.\n\nII. Süre belirlenmemişse haftalık sıfır saat sayılır.\n\nIII. Süreye uygun çağrıda işçi iş görme edimini yerine getirir.",
        "correct": "I ve III", "why": "İş Kanunu m.14 nedeniyle I ve III doğrudur. Süre belirlenmemişse haftalık yirmi saat kabul edildiğinden II yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.14", "difficulty": "medium",
    },
    {
        "stem": "Uzaktan çalışmayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yazılı kurulur.\n\nII. İşverenin iş sağlığı ve güvenliği yükümlülükleri sona erer.\n\nIII. Esaslı neden yoksa emsal işçiden salt bu nedenle farklı işlem yapılamaz.",
        "correct": "I ve III", "why": "İş Kanunu m.14 nedeniyle I ve III doğrudur. İşverenin bilgilendirme, eğitim ve güvenlik yükümlülükleri sürdüğünden II yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.14", "difficulty": "medium",
    },
    {
        "stem": "Deneme süreli sözleşmeyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bireysel sözleşmeyle süre en çok dört aydır.\n\nII. Toplu iş sözleşmesiyle dört aya kadar uzatılabilir.\n\nIII. Çalışılan günlerin ücret ve hakları saklıdır.",
        "correct": "II ve III", "why": "İş Kanunu m.15 nedeniyle II ve III doğrudur. Bireysel sözleşmede üst sınır iki ay olduğundan I yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.15", "difficulty": "medium",
    },
    {
        "stem": "Takım sözleşmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Takım kılavuzu takımı temsilen işverenle sözleşme yapar.\n\nII. Takım sözleşmesi yazılı yapılır.\n\nIII. Kılavuz işçilerin ücretlerinden aracılık kesintisi yapabilir.",
        "correct": "I ve II", "why": "İş Kanunu m.16 nedeniyle I ve II doğrudur. Takım kılavuzu ücretlerden aracılık kesintisi yapamayacağından III yanlıştır.",
        "ref": "4857 sayılı İş Kanunu m.16", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="is_hukuku", topic_id="is_sozlesmesi",
        label="İş Sözleşmesi", slug="is_sozlesmesi",
        prefix="kh-is-soz", seed=20260728,
        legislation_version="4857 sayılı İş Kanunu m.2 ve 6–16 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
