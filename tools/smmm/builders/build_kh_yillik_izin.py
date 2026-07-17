#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM İş Hukuku — Yıllık İzin konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde Çalışma ve Sosyal Güvenlik Bakanlığından alınan
güncel 4857 sayılı İş Kanunu m.53–60 ile Yıllık Ücretli İzin Yönetmeliğidir.
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
        "İşçi, deneme süresinin ardından aynı işyerinde çalışmaya devam etmiş ve işe girişinden itibaren toplam bir yılı doldurmuştur. İşveren deneme süresini hesaba katmamaktadır. Hangisi doğrudur?",
        "Yıllık ücretli izne hak kazanmak için gereken asgari çalışma süresi ve deneme süresinin etkisi nedir?",
        "Bir yıllık hesaba deneme süresi dâhildir ve haktan vazgeçilemez",
        ["Deneme süresi hiçbir zaman hesaba katılmaz", "Hak ancak beşinci yılın sonunda doğar", "Bir yıllık süre dolsa da izin yalnız işveren uygun görüp yazılı onay verirse kullanılabilir", "İşçi önceden imzaladığı belgeyle yıllık izin hakkından bütünüyle vazgeçebilir"],
        "İş Kanunu m.53, işe başlanılan günden itibaren deneme süresi de içinde olmak üzere en az bir yıl çalışan işçiye yıllık ücretli izin verir ve haktan vazgeçilemeyeceğini belirtir.",
        "Bir yıllık kıdem hesabının başlangıcı fiilî işe giriş tarihidir; deneme kaydı bu süreyi ertelemez.",
        "4857 sayılı İş Kanunu m.53", "easy",
    ),
    r(
        "İşçi, niteliği gereği her yıl yalnız dört ay süren kampanya işinde çalışmaktadır. İşyerindeki işi kampanya dönemiyle sınırlıdır. Genel yıllık izin hükümlerinden yararlanmak istemektedir. Sonuç nedir?",
        "Bir yıldan az süren mevsimlik veya kampanya işlerinde yıllık ücretli izin rejimi nasıl uygulanır?",
        "Niteliği gereği bir yıldan kısa mevsimlik veya kampanya işinde bu hükümler uygulanmaz",
        ["Her kampanya işçisi ilk iş gününde yirmi altı gün izin kazanır", "Mevsimlik işte yıllık izin daima iki kat uygulanır", "İşin niteliği ve çalışma biçimi önem taşımaksızın bütün kısa işler aynı hakka tabidir", "Kampanya işinde bir ay çalışan herkes için en az yirmi günlük yıllık izin zorunludur"],
        "İş Kanunu m.53, niteliklerinden ötürü bir yıldan az süren mevsimlik veya kampanya işlerinde çalışanları genel yıllık izin hükümlerinin dışında bırakır.",
        "Mevsimlik işyerinde devamlı çalışanlar bakımından Yönetmelik m.12 genel hükümlerin uygulanacağını ayrıca kabul eder.",
        "4857 sayılı İş Kanunu m.53; Yıllık Ücretli İzin Yönetmeliği m.12", "medium",
    ),
    r(
        "Otuz yaşındaki işçinin aynı işverendeki hizmeti altı yıldır. Bireysel veya toplu sözleşmede daha uzun izin öngörülmemiştir. Kanuni asgari izin süresi nedir?",
        "İş Kanunundaki hizmet süresi basamaklarına göre yıllık ücretli izinlerin asgari süreleri nelerdir?",
        "Bir-beş yıl için on dört, beş yıldan fazla-on beş yıldan az için yirmi, en az on beş yıl için yirmi altı gündür",
        ["Bütün hizmet sürelerinde yalnız yedi gündür ve kıdemin hiçbir etkisi bulunmaz", "Altı yıllık işçinin izni yalnız on dört saatle sınırlıdır", "Bir-beş yıl için yirmi altı, daha uzun hizmette on dört gündür", "Hizmet süresine bakılmaksızın izin süresinin tamamını her yıl işveren tek taraflı belirler"],
        "İş Kanunu m.53; bir yıldan beş yıla kadar, beş yıl dâhil, on dört; beş yıldan fazla on beş yıldan az yirmi; on beş yıl dâhil ve üzeri yirmi altı günlük alt sınır koyar.",
        "Altı yıllık hizmet ikinci basamaktadır ve kanuni asgari süre yirmi gündür; sözleşmeyle artırma mümkündür.",
        "4857 sayılı İş Kanunu m.53", "easy",
    ),
    r(
        "On sekiz yaşındaki işçinin aynı işverendeki hizmeti iki yıldır. İşveren, genel kıdem basamağına göre on dört gün izin vermek istemektedir. Uygulama uygun mudur?",
        "On sekiz ve daha küçük yaştaki işçiler ile elli ve daha yukarı yaştaki işçiler için asgari yıllık izin kaç gündür?",
        "Bu yaş gruplarında yıllık izin yirmi günden az olamaz",
        ["Bu işçiler yıllık izin kullanamaz", "Asgari süre yalnız beş gündür", "Yaş koruması sadece on sekiz yaşından küçükleri kapsar", "Elli yaşındaki işçinin izin süresi kıdemi ne olursa olsun on dört saattir"],
        "İş Kanunu m.53, on sekiz ve daha küçük yaştakilerle elli ve daha yukarı yaştakilerin yıllık iznini en az yirmi gün olarak belirler.",
        "İki yıllık kıdemin genel alt sınırı on dört gün olsa da yaşa ilişkin özel koruma nedeniyle en az yirmi gün verilmelidir.",
        "4857 sayılı İş Kanunu m.53", "easy",
    ),
    r(
        "Yer altı maden işçisinin kıdemine göre genel izin alt sınırı yirmi gündür. İşveren herhangi bir artırım yapmadan yirmi gün kullandırmıştır. Sonuç nedir?",
        "Yer altı işlerinde çalışan işçilerin yıllık izin süresi nasıl belirlenir?",
        "Kıdeme göre bulunan kanuni süre dört gün artırılarak uygulanır",
        ["Yer altı çalışanına yıllık izin verilmez", "Süre dört gün azaltılır", "Artırım yalnız yer üstü büro çalışanına uygulanır ve maden işçisini kapsamaz", "Yer altında geçen her yıl için izin süresi sınırsız olarak iki katına çıkar"],
        "İş Kanunu m.53, yer altı işlerinde çalışanların kıdeme göre bulunan yıllık izin sürelerini dörder gün artırır.",
        "Genel alt sınırı yirmi gün olan yer altı işçisinin kanuni asgari izni yirmi dört gündür.",
        "4857 sayılı İş Kanunu m.53", "medium",
    ),
    r(
        "İşçi aynı işverenin iki farklı işyerinde üçer yıl çalışmıştır. İşveren her işyerindeki süreyi ayrı değerlendirip toplam kıdemi üç yıl saymaktadır. Hangisi doğrudur?",
        "Aynı işverenin bir veya çeşitli işyerlerinde geçen süreler yıllık izin bakımından nasıl değerlendirilir?",
        "Aynı işverene ait işyerlerindeki süreler birleştirilir",
        ["Her işyeri değişiminde kıdem sıfırlanır", "Yalnız son altı ay dikkate alınır", "Birleştirme sadece aynı ilde ve aynı binadaki işyerleri arasında yapılabilir", "İşçinin önceki işyerindeki bütün çalışmaları yıllık izinden düşülerek ceza süresine çevrilir"],
        "İş Kanunu m.54, aynı işverenin bir veya çeşitli işyerlerinde geçen süreleri yıllık izin kıdeminde birleştirir.",
        "İşyerlerinin farklı olması aynı işveren bağını ortadan kaldırmaz; örnekte izin kıdemi toplam altı yıldır.",
        "4857 sayılı İş Kanunu m.54", "medium",
    ),
    r(
        "İşçinin bir yıllık hizmet döneminde, Kanunun çalışılmış gibi saymadığı yirmi günlük devamsızlığı vardır. İzin hakkının doğacağı tarih nasıl belirlenir?",
        "Çalışılmış gibi sayılan hâller dışındaki kesintiler bir yıllık izin kazanma süresini nasıl etkiler?",
        "Kesinti kadar süre eklenir ve hak kazanma tarihi ileri taşınır",
        ["Her devamsızlık izin hakkını sonsuza kadar kaldırır", "Kesinti hiçbir koşulda hesaba etki etmez ve hak ilk işe giriş yıl dönümünde doğar", "İşçi kesinti kadar yıllık izin kazanır", "Yirmi günlük boşluk nedeniyle kıdem otomatik olarak beş yıl artırılır"],
        "İş Kanunu m.54, m.55 dışında kalan devam kesintilerini karşılayacak süreyi hizmet süresine ekleyerek bir yıllık dönemin bitişini ileri taşır.",
        "Kesinti hak kaybına değil, hak kazanma tarihinin kesinti kadar ötelenmesine yol açar.",
        "4857 sayılı İş Kanunu m.54-55", "hard",
    ),
    r(
        "İşçi hastalık nedeniyle işe gidememiştir. Devamsızlığın yıllık izin kıdeminden sayılıp sayılmayacağı tartışılmaktadır. Temel kural nedir?",
        "Kaza veya hastalık nedeniyle işe gidilemeyen günlerin yıllık izin hesabındaki sınırı nedir?",
        "Sağlık nedeniyle fesihteki kanuni bekleme süresini aşmayan kısım sayılır",
        ["Hastalık günlerinin hiçbiri sayılmaz", "Her hastalık günü kıdemi iki yıl artırır", "Süre sınırsız olarak çalışılmış sayılır", "Yalnız işverenin özel sigorta yaptırdığı hastalıklar yıllık izin hesabına katılır"],
        "İş Kanunu m.55/a, kaza veya hastalık günlerini m.25/I-b'deki sürenin fazlası hariç çalışılmış gibi sayar.",
        "Sağlık devamsızlığında kanuni sınırın içindeki bölüm izin kıdemini kesmez; fazlası genel hesapta uzamaya yol açabilir.",
        "4857 sayılı İş Kanunu m.55/a", "hard",
    ),
    r(
        "Kadın işçi, İş Kanunundaki analık izni süresinde çalışmamıştır. İşveren bu dönemi yıllık izin kıdeminden düşmek istemektedir. Hangisi doğrudur?",
        "Kanuni doğum öncesi ve sonrası çalıştırılmama süreleri yıllık izin bakımından nasıl değerlendirilir?",
        "Kanuni analık izni günleri çalışılmış gibi sayılır",
        ["Analık izninin tamamı her hizmet yılında kıdemden düşülerek hesaplama yapılır", "Yalnız doğum günü hesaba katılır", "Bu süreler sadece erkek işçinin kıdemine eklenir", "Doğum öncesi ve sonrası sürelerin sayılması için işçinin yıllık izninden vazgeçmesi gerekir"],
        "İş Kanunu m.55/b, m.74 gereğince doğumdan önce ve sonra çalıştırılmayan günleri yıllık izin hesabında çalışılmış gibi sayar.",
        "Kanuni analık izni işçinin izin kıdemini kesmez; farklı ücretsiz izinlerin etkisi kendi düzenlemelerine göre değerlendirilir.",
        "4857 sayılı İş Kanunu m.55/b", "easy",
    ),
    r(
        "İşçi muvazzaf askerlik dışında kanuni bir ödev nedeniyle bir takvim yılında yüz yirmi gün işe gelememiştir. Bu sürenin ne kadarı yıllık izin hesabında çalışılmış sayılır?",
        "Muvazzaf askerlik dışındaki manevra veya kanuni ödev nedeniyle işe gidilemeyen sürenin yıllık sınırı nedir?",
        "Yılda en çok doksan günü çalışılmış gibi sayılır",
        ["Hiçbir günü sayılmaz", "Yüz yirmi günün tamamı hiçbir yıllık sınır olmaksızın çalışılmış sayılır", "Yalnız bir saat sayılır", "İşçi kanuni ödevde bulunduğu her gün için iki günlük yıllık izin kaybeder"],
        "İş Kanunu m.55/c, muvazzaf askerlik dışındaki manevra veya kanuni ödev nedeniyle işe gidilemeyen sürenin yılda doksan güne kadar olan bölümünü çalışılmış sayar.",
        "Örnekte yüz yirmi günün doksan günü bu bent kapsamında izin kıdemine katılır.",
        "4857 sayılı İş Kanunu m.55/c", "medium",
    ),
    r(
        "Zorlayıcı nedenle işyerindeki çalışma aralıksız üç hafta durmuş, ardından işçi yeniden işe başlamıştır. Çalışılmayan sürenin yıllık izin hesabındaki durumu nedir?",
        "Zorlayıcı nedenle işin bir haftadan çok tatil edilmesinde çalışılmış sayılan süre kaç gündür ve hangi koşula bağlıdır?",
        "İşçinin yeniden başlaması koşuluyla çalışmadığı sürenin on beş günü sayılır",
        ["Üç haftanın tamamı işçinin yeniden başlayıp başlamadığına bakılmaksızın çalışılmış sayılır", "Zorlayıcı nedenle geçen hiçbir gün sayılmaz", "Yalnız ilk bir saat sayılır", "On beş günün sayılması için işçinin iş sözleşmesini derhâl feshetmesi zorunludur"],
        "İş Kanunu m.55/d, zorlayıcı sebeple işin aralıksız bir haftadan çok tatilinde, yeniden işe başlama koşuluyla çalışılmayan zamanın on beş gününü sayar.",
        "Kural bütün durma süresini değil on beş günlük bölümü ve işe dönüş koşulunu kapsar.",
        "4857 sayılı İş Kanunu m.55/d", "hard",
    ),
    r(
        "İşveren, yıl içinde verdiği ücretli mazeret izinlerini yıllık izin kıdeminden düşmüş; hafta tatillerini de çalışılmamış gün saymıştır. Uygulama doğru mudur?",
        "Hafta tatili, genel tatil, işverenin verdiği diğer izinler ve önceki yıllık izin süresi kıdem hesabında nasıl değerlendirilir?",
        "Bu süreler yıllık izin hesabında çalışılmış gibi sayılır",
        ["Bütün bu süreler kıdemi keser", "Sadece işverenin takvim yılı başında belirlediği tek bir tatil günü çalışılmış sayılır", "Hafta tatili her ay izin hakkını sıfırlar", "Önceki yıllık izin kullanımı sonraki yıllarda izin kazanılmasını kesin olarak önler"],
        "İş Kanunu m.55; hafta tatili ve genel tatilleri, işverenin verdiği diğer izinleri, kısa çalışma sürelerini ve yıllık izin süresini çalışılmış gibi sayar.",
        "Kanuni dinlenme ve işverence tanınan izinler, sayılan kapsamda yeni yıllık izin kıdemini kesmez.",
        "4857 sayılı İş Kanunu m.55/f, j-k", "medium",
    ),
    r(
        "İşveren yirmi günlük yıllık izni işçinin onayı olmadan beşer günlük dört parçaya bölmüştür. Taraflar arasında başka anlaşma yoktur. Hangisi doğrudur?",
        "Yıllık ücretli izin hangi koşulla bölümler hâlinde kullandırılabilir?",
        "Tarafların anlaşması gerekir ve bölümlerden biri on günden az olamaz",
        ["İşveren dilediği gibi birer saatlik parçalara bölebilir", "Taraflar anlaşsa bile yıllık izin hiçbir koşulda bölünemez ve tek parça kullandırılır", "Bütün parçaların tam on gün olması zorunludur", "Bölme için işçinin onayı yerine yalnız müşterinin yazılı talebi yeterlidir"],
        "İş Kanunu m.56, yıllık iznin kural olarak sürekli verilmesini; tarafların anlaşması hâlinde bir bölümü en az on gün olmak üzere bölünebilmesini düzenler.",
        "Tek taraflı parçalama mümkün değildir. Bütün parçaların değil, en az bir bölümün on gün veya daha uzun olması gerekir.",
        "4857 sayılı İş Kanunu m.56", "medium",
    ),
    r(
        "İşveren, işçinin yıl içinde kullandığı hastalık iznini daha sonra yıllık izninden düşmüştür. Bu mahsup hukuka uygun mudur?",
        "Yıl içinde verilen diğer ücretli, ücretsiz, dinlenme veya hastalık izinleri yıllık izne mahsup edilebilir mi?",
        "Bu izinler yıllık ücretli izne mahsup edilemez",
        ["Tamamı yıllık izinden zorunlu olarak düşülür", "Sadece hastalık izninin iki katı düşülür", "Mahsup için işverenin sözlü açıklaması her durumda yeterlidir", "İşçinin hastalanması kazanılmış bütün yıllık izinlerini kendiliğinden ortadan kaldırır"],
        "İş Kanunu m.56, yıl içinde verilen diğer ücretli ve ücretsiz izinlerle dinlenme ve hastalık izinlerinin yıllık izne mahsup edilmesini yasaklar.",
        "Farklı amaçlı izin türleri yıllık dinlenme hakkının yerine geçirilemez.",
        "4857 sayılı İş Kanunu m.56", "easy",
    ),
    r(
        "İşçinin yıllık izin dönemine bir ulusal bayram günü ile bir hafta tatili günü rastlamıştır. İşveren bu iki günü yıllık izin süresinden saymıştır. Sonuç nedir?",
        "Yıllık izin günlerine rastlayan ulusal bayram, hafta tatili ve genel tatil günleri nasıl hesaplanır?",
        "Bu günler yıllık ücretli izin süresinden sayılmaz",
        ["Her biri yıllık izinden iki gün düşürür", "Yalnız hafta tatili izin süresinden sayılır ve ulusal bayram her durumda ayrıca eklenir", "Tatil günleri yıllık izin hakkını sona erdirir", "Ulusal bayram yalnız işçinin kıdemi on beş yılı aşarsa izin süresinden sayılmaz"],
        "İş Kanunu m.56, yıllık izin süresine rastlayan ulusal bayram, hafta tatili ve genel tatil günlerini izin günlerinden saymaz.",
        "İzin bitiş tarihi bu tatil günleri dışarıda bırakılarak belirlenir; ücret hakları ayrıca korunur.",
        "4857 sayılı İş Kanunu m.56", "easy",
    ),
    r(
        "İşçi yıllık iznini işyerinin bulunduğu şehirden başka yerde geçireceğini belgeleyerek yol izni istemiştir. İşveren talebi reddetmiştir. Hangisi doğrudur?",
        "Yıllık izni başka yerde geçirecek işçiye verilecek ücretsiz yol izninin koşulu ve üst sınırı nedir?",
        "İstem ve belgeyle toplam dört güne kadar ücretsiz yol izni verilir",
        ["Yol izni hiçbir durumda verilmez", "İşveren her işçiye ücretli otuz gün yol izni vermek zorundadır", "Belgeleme olmadan sınırsız ücretli izin ve ulaşım ödemesi doğar", "Dört günlük yol izni yalnız işveren de aynı yere tatile giderse kullanılabilir"],
        "İş Kanunu m.56, izni işyerinin kurulu olduğu yerden başka yerde geçirecek işçiye istem ve belgeleme koşuluyla toplam dört güne kadar ücretsiz yol izni verilmesini zorunlu kılar.",
        "Yol izni yıllık izin süresinden ayrı, ücretsiz ve gidiş-dönüş ihtiyacını karşılayan en çok dört günlük bir haktır.",
        "4857 sayılı İş Kanunu m.56", "medium",
    ),
    r(
        "Alt işveren değişmiş ancak işçi aynı işyerinde kesintisiz çalışmayı sürdürmüştür. Yeni alt işveren yıllık izin kıdemini sıfırdan başlatmıştır. Hangisi doğrudur?",
        "Alt işvereni değiştiği hâlde aynı işyerinde çalışan işçinin yıllık izin süresi nasıl hesaplanır?",
        "Aynı işyerindeki süreler birleştirilir; asıl işveren izin kullanımını gözetir",
        ["Her alt işveren değişiminde aynı işyerinde geçen yıllık izin kıdeminin tamamı sıfırlanır", "Yalnız asıl işverenin büro çalışanlarının süresi birleşir", "İzin kayıt belgesi tutulması kanunen yasaktır", "Alt işveren değişikliği işçinin geçmiş izin kıdemini işverene aktarılabilen bir borca dönüştürür"],
        "İş Kanunu m.56, aynı işyerinde devam eden alt işveren işçisinin sürelerini birleştirir; asıl işveren izin kullanımını kontrol edip sağlamakla, alt işveren kayıt örneğini vermekle yükümlüdür.",
        "İşveren değişiminin görünümü, işçinin aynı işyerindeki hizmet süresini yıllık izin bakımından ortadan kaldırmaz.",
        "4857 sayılı İş Kanunu m.56", "hard",
    ),
    r(
        "İşçi yıllık iznini kullanmak istediği tarihten bir hafta önce sözlü bildirim yapmıştır. Yönetmelikteki başvuru usulü bakımından hangisi doğrudur?",
        "İşçi yıllık izin isteğini ne zaman ve hangi biçimde bildirmelidir?",
        "Kullanmak istediği tarihten en az bir ay önce yazılı olarak bildirmelidir",
        ["İzne başladıktan sonra sözlü bildirim yeterlidir", "Yıllık izin talebi kullanımdan en az beş yıl önce noter aracılığıyla işverene gönderilmelidir", "İşçi hiçbir bildirimde bulunamaz", "Yalnız çalışma arkadaşına gönderilen isimsiz mesaj yazılı başvuru yerine geçer"],
        "Yıllık Ücretli İzin Yönetmeliği m.7, işçinin izin isteğini kullanmak istediği tarihten en az bir ay önce yazılı bildirmesini öngörür.",
        "İzin isteminde kimlik bilgileri, istenen tarih aralığı ve ücretsiz yol izni talebi de belirtilir.",
        "Yıllık Ücretli İzin Yönetmeliği m.7-8", "easy",
    ),
    r(
        "Aynı tarihte iki işçi yıllık izin istemiştir. İzin kurulu yalnız işçilerin istedikleri tarihle mutlak biçimde bağlı olduğunu düşünmektedir. Hangisi doğrudur?",
        "İzin zamanı belirlenirken işçinin talebi, iş durumu ve çakışan isteklerde öncelik nasıl değerlendirilir?",
        "Kurul taleple bağlı değildir; iş durumu, kıdem ve önceki izin tarihi gözetilir",
        ["İlk ulaşan talep, iş durumu ve diğer işçilerin kıdemi incelenmeden her durumda kabul edilir", "İzin zamanını yalnız müşteriler kura ile belirler", "Kıdem ve iş durumu hiçbir zaman değerlendirilemez", "Aynı tarihteki bütün talepler işçilerin yıllık izin hakkını kalıcı olarak sona erdirir"],
        "Yönetmelik m.8, kurul veya işvereni istenen tarihle bağlı tutmaz; çizelgede işçinin talebi ve iş durumu, çakışmada kıdem ve önceki yıl izin tarihi dikkate alınır.",
        "İşçinin tarih talebi önemlidir fakat iş organizasyonu ve adil sıra ölçütleriyle birlikte değerlendirilir.",
        "Yıllık Ücretli İzin Yönetmeliği m.8", "medium",
    ),
    r(
        "İşveren bütün işçileri kapsayan toplu yıllık izni şubat ayında başlatmak istemektedir. Yönetmelikteki dönem bakımından hangisi doğrudur?",
        "Toplu izin uygulaması hangi aylar arasında yapılabilir ve henüz izin hakkı kazanmayanlar kapsama alınabilir mi?",
        "Nisan başı-ekim sonu uygulanabilir; hak kazanmayanlar da kapsanabilir",
        ["Toplu izin yalnız ocak ayının ilk günü uygulanır", "Henüz hak kazanmayan işçilerin toplu izin çizelgesine alınması her durumda kesinlikle yasaktır", "Toplu izin bütün yıl işyerini kapatmayı zorunlu kılar", "İşveren toplu izni sadece işçilerin kıdemini sıfırlamak amacıyla on yılda bir kullanabilir"],
        "Yönetmelik m.10, toplu izni nisan başı-ekim sonu arasında öngörür ve henüz yıllık izin hakkı kazanmayanların da kapsanmasına izin verir.",
        "İşyeri güvenliği ve zorunlu bakım işleri için yeterli sayıda işçi toplu izin dışında tutulabilir; izinleri önce veya sonra verilir.",
        "Yıllık Ücretli İzin Yönetmeliği m.10-11", "medium",
    ),
    r(
        "Kısmi süreli çalışan işçiye, haftada yalnız üç gün çalıştığı gerekçesiyle yıllık izin verilmeyeceği bildirilmiştir. Hangisi doğrudur?",
        "Kısmi süreli veya çağrı üzerine çalışanların yıllık ücretli izin hakkı nasıl uygulanır?",
        "Tam süreli çalışanlar gibi yararlanırlar ve farklı işleme tabi tutulamazlar",
        ["Yıllık izin hakları yoktur", "İzinleri daima ücretsiz ve bir saatle sınırlıdır", "Yalnız çağrı üzerine çalışan işveren yıllık izin kullanabilir", "Kısmi süreli işçi izin hakkı için tam süreli işçinin iki katı kıdem tamamlamalıdır"],
        "Yönetmelik m.13, kısmi süreli ve çağrı üzerine çalışanların yıllık izinden tam süreli çalışanlar gibi yararlanacağını ve farklı işleme tabi tutulamayacağını düzenler.",
        "Bu işçiler izinlerini, sözleşmeleri sürerken izin dönemine rastlayan kısmi çalışma günlerinde çalışmayarak kullanır.",
        "Yıllık Ücretli İzin Yönetmeliği m.13", "easy",
    ),
    r(
        "İşyerinde yüz yirmi işçi bulunmaktadır. İşveren izin kurulunu yalnız iki işveren temsilcisinden oluşturmuştur. Kuruluş uygun mudur?",
        "İzin kurulu hangi büyüklükteki işyerinde ve hangi temsil yapısıyla kurulur?",
        "Yüzden fazla işçide bir işveren ve iki işçi temsilcili üç kişilik kurul kurulur",
        ["Her işyerinde yalnız işveren üyelerinden oluşur", "Kurul için en az bin işçi gerekir", "Yüzden fazla işçi varsa kurul kurulması yasaktır", "Üç kişilik kurulun tamamı işyeri dışındaki müşteriler tarafından seçilmek zorundadır"],
        "Yönetmelik m.15, yüzden fazla işçi bulunan işyerinde işvereni temsilen bir ve işçileri temsilen iki kişiden oluşan izin kurulu öngörür.",
        "Yüzden az işçili işyerinde görevler işveren veya görevlendireceği kişi ile işçilerin seçeceği temsilci tarafından yürütülür.",
        "Yıllık Ücretli İzin Yönetmeliği m.15 ve 18", "medium",
    ),
    r(
        "İşveren, yıllık izne çıkacak işçinin izin dönemine ilişkin ücretini izin dönüşünde ödeyeceğini bildirmiştir. Uygulama doğru mudur?",
        "Yıllık izin ücreti ne zaman ödenmeli veya avans olarak verilmelidir?",
        "İşçi izne başlamadan önce peşin ödenmeli veya avans olarak verilmelidir",
        ["İzin bitiminden on yıl sonra ödenir", "İzin ücreti hiçbir zaman ödenmez", "Yalnız işçi izin sırasında çalışırsa ödenir", "İşveren ödemeyi izin dönüşüne kadar erteleyebilir ve hiçbir avans vermeyebilir"],
        "İş Kanunu m.57, izin dönemine ilişkin ücretin izne başlamadan önce peşin ödenmesini veya avans olarak verilmesini zorunlu kılar.",
        "İzin ücretinin önceden verilmesi, ücretli dinlenme hakkının fiilen kullanılabilmesini sağlar.",
        "4857 sayılı İş Kanunu m.57", "easy",
    ),
    r(
        "Akortla çalışan işçinin izin ücreti hesaplanacaktır. Ücreti son bir yılda değişkenlik göstermiştir ve son yıl içinde zam yapılmamıştır. Hangi yöntem uygulanır?",
        "Akort, komisyon, kâra katılma veya yüzde usulü gibi değişken ücretlerde izin ücreti nasıl hesaplanır?",
        "Son bir yılda kazanılan ücret fiilen çalışılan günlere bölünerek ortalama bulunur",
        ["Yalnız en düşük günlük ücret esas alınır", "İzin ücreti sıfır kabul edilir", "İşçinin bütün kariyer ücretleri takvim günlerine bölünür", "Değişken ücretli işçiye izin yerine yalnız ücretsiz dinlenme verilmesi zorunludur"],
        "İş Kanunu m.57, belirli olmayan süre ve tutar üzerinden ücret alan işçinin izin ücretini son bir yıllık kazancın fiilen çalışılan günlere bölünmesiyle bulunan ortalamaya bağlar.",
        "Son bir yıl içinde zam varsa özel dönem hesabı uygulanır; fazla çalışma, prim ve sosyal yardımlar Yönetmelik m.21 uyarınca izin ücretine katılmaz.",
        "4857 sayılı İş Kanunu m.57; Yıllık Ücretli İzin Yönetmeliği m.21", "hard",
    ),
    r(
        "Yıllık iznini kullanan işçinin bu süre içinde başka bir işverene ücret karşılığı çalıştığı belirlenmiştir. İlk işveren ödediği izin ücretini geri istemektedir. Sonuç nedir?",
        "Yıllık izin sırasında ücret karşılığı başka işte çalışmanın izin ücretine etkisi nedir?",
        "İzin süresinde ödenen ücret işveren tarafından geri alınabilir",
        ["İşçi ayrıca ikinci bir yıllık izin kazanır", "İzin ücreti hiçbir koşulda geri istenemez", "İlk işveren işçiye zorunlu olarak iki kat ücret öder", "Başka işte çalışma izin süresini kendiliğinden ücretsiz kıdem dönemine dönüştürür"],
        "İş Kanunu m.58, yıllık izindeki işçinin izin süresinde ücret karşılığı çalıştığının anlaşılması hâlinde ödenen izin ücretinin geri alınabilmesini düzenler.",
        "Yıllık izin dinlenme amacı taşır; ücret karşılığı çalışma bu amaca aykırı özel sonucu doğurur.",
        "4857 sayılı İş Kanunu m.58", "medium",
    ),
    r(
        "İş sözleşmesi işçinin istifasıyla sona ermiş ve kullanmadığı on günlük yıllık izni kalmıştır. İşveren yalnız kendisi feshederse ödeme yapacağını savunmaktadır. Hangisi doğrudur?",
        "İş sözleşmesi sona erdiğinde kullanılmayan yıllık izin ücretinin koşulu ve ücret ölçüsü nedir?",
        "Sona erme nedeninden bağımsız olarak kullanılmayan izin son ücret üzerinden ödenir",
        ["İstifada kullanılmayan izin daima yanar", "Ödeme yalnız işçinin ilk işe giriş ücretinden yapılır", "Kullanılmayan izin ücretinin hak sahiplerine ödenmesi yasaktır", "Sözleşme sona erse de izin ücreti ancak işçinin yeniden aynı işverende çalışması hâlinde doğar"],
        "İş Kanunu m.59, sözleşmenin herhangi bir nedenle sona ermesinde kullanılmayan izin ücretini sona erme tarihindeki ücret üzerinden işçiye veya hak sahiplerine ödetir.",
        "Zamanaşımı sona erme tarihinden başlar; işverence fesihte bildirim süresi ve yeni iş arama izni yıllık izinle iç içe geçirilemez.",
        "4857 sayılı İş Kanunu m.59", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Yıllık izne hak kazanmayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Deneme süresi bir yıllık hesapta dikkate alınır.\n\nII. En az bir yıllık çalışma gerekir.\n\nIII. Yıllık izin hakkından vazgeçilemez.",
        "correct": "I, II ve III", "why": "İş Kanunu m.53 uyarınca üç ifade de yıllık izin hakkının temel özellikleridir.",
        "ref": "4857 sayılı İş Kanunu m.53", "difficulty": "easy",
    },
    {
        "stem": "Yıllık izin süreleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bir yıldan beş yıla kadar hizmette alt sınır on dört gündür.\n\nII. On beş yıl ve üzeri hizmette alt sınır yirmi altı gündür.\n\nIII. Yer altı işlerinde süreler dört gün artırılır.",
        "correct": "I, II ve III", "why": "İş Kanunu m.53'teki kıdem basamakları ve yer altı artırımı üç ifadeyi de doğrular.",
        "ref": "4857 sayılı İş Kanunu m.53", "difficulty": "medium",
    },
    {
        "stem": "Yıllık izin kıdeminin hesabıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aynı işverenin farklı işyerlerindeki süreler birleştirilir.\n\nII. Kanuni analık izni günleri çalışılmış gibi sayılır.\n\nIII. Her işyeri değişikliğinde aynı işveren yanındaki kıdem sıfırlanır.",
        "correct": "I ve II", "why": "İş Kanunu m.54-55 nedeniyle I ve II uygulanır. Aynı işverenin işyerleri arasındaki geçiş kıdemi sıfırlamaz.",
        "ref": "4857 sayılı İş Kanunu m.54-55", "difficulty": "medium",
    },
    {
        "stem": "Yıllık iznin kullanılmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tarafların anlaşmasıyla bölünebilir.\n\nII. Bölümlerden biri on günden az olamaz.\n\nIII. Hastalık izni yıllık izne mahsup edilir.",
        "correct": "I ve II", "why": "İş Kanunu m.56 uyarınca I ve II uygulanır. Hastalık izninin yıllık izne mahsup edilmesine izin verilmez.",
        "ref": "4857 sayılı İş Kanunu m.56", "difficulty": "medium",
    },
    {
        "stem": "Yıllık izin günlerinin hesabıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İzin dönemine rastlayan hafta tatili izin süresinden sayılmaz.\n\nII. Genel tatil günleri izin süresinden sayılmaz.\n\nIII. Belgelense bile şehir dışında geçirilecek izin için ücretsiz yol izni verilemez.",
        "correct": "I ve II", "why": "İş Kanunu m.56 uyarınca I ve II uygulanır. İstem ve belgeleme varsa toplam dört güne kadar ücretsiz yol izni verilmesi gerektiği için III uygulanmaz.",
        "ref": "4857 sayılı İş Kanunu m.56", "difficulty": "hard",
    },
    {
        "stem": "İzin başvurusu ve çizelgesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İstek en az bir ay önce yazılı bildirilir.\n\nII. İzin kurulu işçinin istediği tarihle her durumda bağlıdır.\n\nIII. Çakışan taleplerde kıdem ve önceki yıl izin tarihi dikkate alınır.",
        "correct": "I ve III", "why": "Yönetmelik m.7-8 nedeniyle I ve III uygulanır. Kurul, istenen tarihle mutlak biçimde bağlı değildir.",
        "ref": "Yıllık Ücretli İzin Yönetmeliği m.7-8", "difficulty": "medium",
    },
    {
        "stem": "Yıllık izin ücretiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İzne başlamadan önce peşin ödenir veya avans verilir.\n\nII. Değişken ücrette kural olarak son bir yıllık kazanç ve fiilî çalışma günleri esas alınır.\n\nIII. İzin dönemine rastlayan hafta tatili ücretleri ayrıca ödenmez.",
        "correct": "I ve II", "why": "İş Kanunu m.57 nedeniyle I ve II uygulanır. İzin dönemine rastlayan hafta tatili ve genel tatil ücretleri ayrıca ödenir.",
        "ref": "4857 sayılı İş Kanunu m.57", "difficulty": "hard",
    },
    {
        "stem": "İş sözleşmesinin sona ermesi ve yıllık izinle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kullanılmayan izin ücreti sona erme tarihindeki ücret üzerinden hesaplanır.\n\nII. Ödeme yalnız işveren feshi hâlinde yapılır.\n\nIII. İşverence fesihte bildirim süresi yıllık izinle iç içe geçirilebilir.",
        "correct": "Yalnız I", "why": "İş Kanunu m.59 uyarınca I uygulanır. Ödeme sona erme nedeninden bağımsızdır; işverence fesihte bildirim ve yeni iş arama süreleri yıllık izinle iç içe geçirilemez.",
        "ref": "4857 sayılı İş Kanunu m.59", "difficulty": "medium",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="is_hukuku", topic_id="yillik_izin",
        label="Yıllık İzin", slug="yillik_izin",
        prefix="kh-yillik-izin", seed=20260731,
        legislation_version="4857 sayılı İş Kanunu m.53–60 ve Yıllık Ücretli İzin Yönetmeliği — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
