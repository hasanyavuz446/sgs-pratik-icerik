#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Sermaye Piyasası Mevzuatı — Kolektif Yatırım Kuruluşları, 3×20.

Dayanaklar, 17.07.2026 tarihinde 6362 sayılı Kanunun güncel metni, SPK'nın
güncel III-52.1 sayılı Tebliği ve Kurulun yatırım fonları ile portföy saklama
tanıtım rehberleri üzerinden doğrulanmıştır.
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
        "Tasarruf sahiplerinin birikimleri profesyonel biçimde ortak bir portföyde yönetilecektir. Yapı ayrı bir anonim ortaklık kurulmadan, portföy yönetim şirketinin içtüzüğüyle oluşturulmuştur. Bu yapı hangisidir?",
        "Kolektif yatırım kuruluşlarında yatırım fonu ile yatırım ortaklığının hukuki yapı farkı nedir?",
        "Yatırım fonudur; ayrı tüzel kişiliği bulunmayan malvarlığıdır",
        ["Yatırım ortaklığıdır; mutlaka anonim ortaklık tüzel kişiliği vardır", "Mevduat bankasıdır; tasarrufları kredi olarak toplar", "Borsadır; alım satım emirlerini eşleştirmek için kurulur", "Portföy saklayıcısıdır; yatırım kararlarını kendisi verir"],
        "SPK'nın tanıtım rehberine göre kolektif yatırım kuruluşu ayrı bir tüzel kişilik olarak kurulursa yatırım ortaklığı, başka bir tüzel kişi tarafından içtüzük çerçevesinde oluşturulursa yatırım fonudur.",
        "Yatırım ortaklığı anonim ortaklık, yatırım fonu ise portföy yönetim şirketince içtüzükle kurulan tüzel kişiliği bulunmayan malvarlığıdır.",
        "6362 sayılı Kanun m.48 ve m.52; SPK Yatırım Fonları Tanıtım Rehberi", "easy",
    ),
    r(
        "Bir şirket, paylarını ihraç ederek sermaye piyasası araçları ve gayrimenkullerden oluşan portföyü işletmek amacıyla anonim ortaklık şeklinde kurulmuştur. Hukuki niteliği nedir?",
        "6362 sayılı Kanuna göre yatırım ortaklığının amaç ve şirket biçimi nedir?",
        "Pay ihraç eden anonim yatırım ortaklığıdır",
        ["Tasarruf mevduatı kabul eden bir kredi kuruluşudur", "Tüzel kişiliği olmayan yatırım fonudur", "Yalnız saklama hizmeti veren merkezi kuruluşudur", "Borsa işlemlerini denetleyen kamu kurumudur"],
        "Kanun m.48, yatırım ortaklığını belirlenen varlık ve haklardan oluşan portföyleri işletmek amacıyla paylarını ihraç etmek üzere kurulan sabit veya değişken sermayeli anonim ortaklık olarak tanımlar.",
        "Yatırım ortaklığının ayırt edici unsurları anonim ortaklık biçimi, pay ihracı ve portföy işletme amacıdır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.48/1", "easy",
    ),
    r(
        "Kuruldan yatırım ortaklığı kuruluş izni isteyen anonim şirketin pay bedelleri kuruluşta kısmen ödenmiş, unvanında da 'Yatırım Ortaklığı' ibaresine yer verilmemiştir. İzin şartları sağlanmış mıdır?",
        "Yatırım ortaklığının kuruluşunda pay bedeli, unvan ve saklama bakımından hangi koşullar aranır?",
        "Hayır; paylar tam nakden ödenmeli ve gerekli ibare bulunmalıdır",
        ["Evet; pay bedellerinin hiç ödenmemesi kuruluş için yeterlidir", "Evet; unvanda faaliyet türünü belirten ibare kullanılması yasaktır", "Hayır; fakat portföy saklama kuruluşu belirlemek mümkün değildir", "Evet; yatırım politikası mevzuata aykırı olsa da izin verilir"],
        "Kanun m.49; payların nakit karşılığı çıkarılıp tam ve nakden ödenmesini, unvanda 'Yatırım Ortaklığı' ibaresini, uygun esas sözleşme ve yatırım politikasını ve yetkili saklayıcının belirlenmesini şart koşar.",
        "Kayıtlı sermayeli anonim ortaklık biçimi, Kurulca belirlenen başlangıç sermayesi ve portföy saklayıcısı da kuruluş koşulları arasındadır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.49/1", "medium",
    ),
    r(
        "Değişken sermayeli yatırım ortaklığının varlıkları 72 milyon TL, borçları 12 milyon TL'dir. Ortaklığın sermayesi hangi tutara eşit olmalıdır?",
        "Değişken sermayeli yatırım ortaklığında net aktif değer ve sermaye ilişkisi nasıldır?",
        "60 milyon TL net aktif değere eşit olmalıdır",
        ["72 milyon TL brüt varlık toplamına eşit olmalıdır", "12 milyon TL borç toplamına eşit olmalıdır", "84 milyon TL varlık ve borç toplamına eşit olmalıdır", "Sermaye net aktif değerden tamamen bağımsız belirlenir"],
        "Kanun m.50/1'e göre net aktif değer, varlıklar toplamından borçlar toplamının çıkarılmasıyla bulunur: 72 − 12 = 60 milyon TL. Değişken sermayeli ortaklığın sermayesi bu değere eşittir.",
        "Bu ortaklık türünde sermaye sabit bir nominal tutar değil, her zaman net aktif değere eşit olacak şekilde değişen büyüklüktür.",
        "6362 sayılı Sermaye Piyasası Kanunu m.50/1", "medium",
    ),
    r(
        "Değişken sermayeli yatırım ortaklığı, yatırımcı paylarına nominal değer ve genel kurulda yönetim hakkı tanımak istemektedir. Bu tasarım uygun mudur?",
        "Değişken sermayeli yatırım ortaklığında pay türleri ve yatırımcı paylarının hakları nasıldır?",
        "Hayır; itibari değer ve yönetim hakkı yoktur",
        ["Evet; bütün paylar nominal değer ve yönetim hakkı taşımak zorundadır", "Hayır; fakat ortaklıkta yalnız borçlanma aracı bulunabilir", "Evet; yatırımcı payları mutlaka kurucu payına dönüşür", "Hayır; değişken sermayeli ortaklık hiçbir pay ihraç edemez"],
        "Kanun m.50/2, payları kurucu ve yatırımcı payları olarak ayırır, payların itibari değerinin olmadığını ve yatırımcı paylarının yönetimsel hak vermediğini düzenler.",
        "Kurucu payları nama yazılıdır ve kuruluş sermayesini temsil eder; yatırımcı payları ise portföye katılım sağlasa da yönetimsel hak doğurmaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.50/2", "medium",
    ),
    r(
        "Yatırımcı, değişken sermayeli yatırım ortaklığındaki yatırımcı paylarının itfasını talep etmiş; ortaklık hiçbir gerekçe göstermeden talebi reddetmiştir. Genel kural nedir?",
        "Değişken sermayeli yatırım ortaklığının yatırımcı paylarını itfa yükümlülüğü nasıl işler?",
        "Talep üzerine itfa ve bedel iadesi gerekir",
        ["Paylar hiçbir zaman itfa edilemez ve bedel geri ödenmez", "İtfa yalnız bütün pay sahiplerinin oybirliğiyle yapılabilir", "Yatırımcı payı yalnız kurucu payına çevrilerek sona erer", "Ortaklık pay bedelini yalnız on yıl sonra bağış olarak öder"],
        "Kanun m.50/3, değişken sermayeli yatırım ortaklığının pay sahibinin talebi üzerine payı itfa etmesini ve sermayede buna karşılık gelen bedeli geri ödemesini öngörür.",
        "İtfa usul ve esasları ortaklığın esas sözleşmesinde gösterilir; açık uçlu yapı yatırımcı payının ortaklığa iadesine dayanır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.50/3", "medium",
    ),
    r(
        "Portföy yönetim şirketi, tasarruf sahiplerinden katılma payı karşılığı topladığı varlıklarla onların hesabına portföy işletmek üzere içtüzük düzenlemiştir. Oluşan malvarlığının niteliği nedir?",
        "Yatırım fonunu oluşturan unsurlar hangi şekilde bir araya gelir?",
        "Tüzel kişiliği olmayan yatırım fonudur",
        ["Ortaklarına oy hakkı veren sabit sermayeli anonim şirkettir", "Yalnız bankaların kurabildiği mevduat hesabıdır", "Kurucunun borçlarına karşılık gösterilen kişisel malvarlığıdır", "Sermaye piyasası aracı ihraç edemeyen ticari işletmedir"],
        "Kanun m.52; yatırım fonunu katılma payı karşılığında toplanan para veya diğer varlıklarla, tasarruf sahipleri hesabına, inançlı mülkiyet esasına göre portföy işletmek için içtüzükle kurulan tüzel kişiliksiz malvarlığı olarak tanımlar.",
        "Yatırım fonu anonim ortaklık değildir; kurucunun kendi hesabına değil katılma payı sahipleri hesabına işletilen ayrı bir malvarlığıdır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.52/1; III-52.1 m.3/1-t", "easy",
    ),
    r(
        "Portföy yönetim şirketi yatırım fonu kurmak istemekte, ancak portföy saklayıcısıyla anlaşmadan ve içtüzüğü Kurula sunmadan faaliyete başlamayı planlamaktadır. Mümkün müdür?",
        "Yatırım fonunun kuruluş izni için saklama ve içtüzük bakımından hangi koşullar gerekir?",
        "Hayır; yetkili saklayıcıyla anlaşma ve Kurul onaylı içtüzük gerekir",
        ["Evet; saklama hizmeti ve içtüzük yatırım fonunda aranmaz", "Hayır; fakat fon içtüzüğünü yalnız yatırımcılar onaylar", "Evet; kurucu kendi borçları için fon varlığını teminat gösterirse kurulur", "Hayır; yatırım fonu sadece borsa tarafından kurulabilir"],
        "Kanun m.52/2, fon kuruluşu için Kurulca yetkilendirilmiş saklama kuruluşuyla anlaşmayı ve fon içtüzüğünün Kurulca onaylanmasını arar.",
        "Kuruluş izni, portföyün kim tarafından saklanacağı ve katılma ilişkisinin hangi içtüzük hükümlerine göre yürütüleceği belirlenmeden verilemez.",
        "6362 sayılı Sermaye Piyasası Kanunu m.52/2", "easy",
    ),
    r(
        "Fon yöneticisi, fon varlıkları üzerinde kurucunun kendi hesabına tasarruf ettiğini savunmaktadır. Doğru yetki kullanımı hangisidir?",
        "Fon yönetim şirketi yatırım fonunu hangi amaçla temsil ve yönetir?",
        "Kendi adına ve fon hesabına tasarruf eder",
        ["Hem kendi adına hem kendi hesabına sınırsız tasarruf eder", "Yalnız portföy saklayıcısının hesabına yatırım yapar", "Fon varlıklarını kurucunun üçüncü kişi borçlarına ayırır", "Katılma payı sahiplerinin haklarını gözetmeden işlem yapar"],
        "Kanun m.52/3, fon yönetim şirketinin fonu katılma payı sahiplerinin haklarını koruyarak temsil ve yönetmesini; varlıklar üzerinde kendi adına fakat fon hesabına tasarruf etmesini düzenler.",
        "İnançlı mülkiyet yapısında hukuki işlem kurucunun kendi adına yapılabilir, ancak ekonomik sonuç fon hesabına ve katılımcı yararına doğar.",
        "6362 sayılı Sermaye Piyasası Kanunu m.52/3", "medium",
    ),
    r(
        "Kurucunun alacaklısı, portföy yönetim şirketinin borcu için yatırım fonunun malvarlığını haczettirmek istemektedir. Bu talep fon varlıklarının ayrılığıyla bağdaşır mı?",
        "Fon malvarlığının kurucu ve portföy saklayıcısı karşısındaki hukuki konumu nedir?",
        "Hayır; fon malvarlığı ayrıdır ve haczedilemez",
        ["Evet; fon varlığı kurucunun bütün borçlarına karşılık oluşturur", "Evet; saklayıcının iflasında doğrudan iflas masasına girer", "Hayır; fakat fon varlığı yalnız çalışanlara ait kişisel maldır", "Evet; ihtiyati tedbir ve rehin hiçbir sınıra tabi değildir"],
        "Kanun m.53, fon malvarlığını fon yönetim şirketi ve saklayıcının malvarlığından ayırır; kamu alacakları dahil haciz, ihtiyati tedbir ve iflas masasına dahil edilme yasağı getirir.",
        "Fon varlığı yatırımcılar için ayrılmıştır. Fon hesabına ve içtüzükte hükme dayanan belirli işlemler dışındaki teminat ve rehin de yasaktır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.53/1-2", "medium",
    ),
    r(
        "Fonun tasfiyesinde kalan malvarlığının bir bölümü kurucunun ortaklarına dağıtılmak istenmektedir. Kanuna uygun dağıtım nasıl yapılır?",
        "Fon malvarlığının tasfiyesi ve kurucu borçlarıyla mahsup bakımından hangi koruma uygulanır?",
        "Tasfiye bakiyesi yalnız katılma payı sahiplerine ödenir",
        ["Tasfiye bakiyesi yalnız kurucunun alacaklılarına ödenir", "Fon alacağı kurucunun borcuyla zorunlu olarak mahsup edilir", "Saklayıcı bütün fon varlığını kendi sermayesine ekler", "Tasfiye sonunda hiçbir katılma payı sahibine ödeme yapılamaz"],
        "Kanun m.53/3-4, tasfiyede yalnız katılma payı sahiplerine ödeme yapılmasını ve fon yönetim şirketinin üçüncü kişi borçlarıyla fonun aynı kişilerden alacaklarının mahsup edilememesini düzenler.",
        "Fon malvarlığının ayrılığı tasfiye aşamasında da sürer; kurucunun veya saklayıcının ekonomik menfaati için dağıtılamaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.53/3-4", "medium",
    ),
    r(
        "Bir limited şirket, ana faaliyet konusu olarak yatırım fonu kurup yönetmek üzere 'fon yönetim şirketi' izni talep etmiştir. Şirket türü bakımından talep uygun mudur?",
        "Fon yönetim şirketinin hukuki şekli, ana faaliyeti ve izin şartı nedir?",
        "Hayır; anonim ortaklık olmalı ve Kuruldan izin almalıdır",
        ["Evet; her limited şirket izinsiz biçimde fon yönetebilir", "Hayır; fon yönetim şirketi yalnız gerçek kişi olabilir", "Evet; ana faaliyeti mevduat kabul etmek olmak zorundadır", "Hayır; fon yönetimi sadece portföy saklayıcısına bırakılmıştır"],
        "Kanun m.55, fon yönetim şirketini ana faaliyet konusu yatırım fonlarının kurulması ve yönetimi olan anonim ortaklık olarak düzenler; kuruluş ve faaliyet için Kurul izni gerekir.",
        "Fon yönetim şirketi herhangi bir ticaret şirketi değildir; şirket türü, ana faaliyet ve düzenleyici izin birlikte aranır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.55/1", "easy",
    ),
    r(
        "Portföy saklayıcısı, fonun katılma payı ihracının içtüzüğe uygunluğunu kontrol etmenin görevi dışında olduğunu savunmaktadır. Bu görüş doğru mudur?",
        "Portföy saklama hizmeti yalnız varlıkları fiziken tutmaktan mı ibarettir?",
        "Hayır; saklama yanında mevzuata uygunluk kontrolü de yapar",
        ["Evet; saklayıcı hiçbir mevzuat uygunluğu kontrolü yapmaz", "Evet; saklayıcı yalnız yatırım tavsiyesi vermekle görevlidir", "Hayır; fakat bütün yatırım kararlarını saklayıcı tek başına alır", "Evet; fon gelirlerinin kullanımını izlemek kesinlikle yasaktır"],
        "Kanun m.56; saklama hizmetine ihraç ve itfanın, birim pay değerinin, talimatların, edimlerin, gelir kullanımının ve portföy işlemlerinin mevzuat ve fon belgelerine uygunluğunun sağlanmasını dahil eder.",
        "Portföy saklama, varlığı koruma yanında fon yönetiminin belirli işlemlerine ilişkin bağımsız uygunluk kontrollerini de içerir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.56/1", "medium",
    ),
    r(
        "Portföy saklayıcısı yükümlülüklerini gereği gibi yerine getirmeyerek katılma payı sahiplerini zarara uğratmış, ancak sorumluluğunun bulunmadığını ileri sürmüştür. Sonuç nedir?",
        "Portföy saklayıcısının zarardan sorumluluğu ve fon yönetim şirketiyle kurumsal ilişkisi nasıldır?",
        "Zarardan sorumludur; fon yönetim şirketiyle aynı tüzel kişi olamaz",
        ["Sorumlu değildir; bütün zararlar yalnız yatırımcıya aittir", "Aynı tüzel kişi olmalı ve bağımsız davranmamalıdır", "Yalnız kâr kaybında sorumlu olur, varlık kaybında olmaz", "Sorumluluk doğması için saklayıcının yatırım ortaklığı kurması gerekir"],
        "Kanun m.56/2 ve 6, saklayıcıyı gereği gibi ifa etmemesinden doğan zarardan sorumlu tutar; saklayıcı ve fon yönetim şirketi aynı tüzel kişi olamaz ve bağımsız hareket eder.",
        "Görev ayrılığı yatırımcı varlıklarının yönetimden bağımsız kontrolünü sağlar; tüzel kişilerin ayrılığı sorumluluğu ortadan kaldırmaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.56/2 ve 6", "hard",
    ),
    r(
        "Tek bir içtüzük altında üç ayrı fonun katılma payı ihraç edilmektedir. Her fonun varlık ve yükümlülükleri ayrı izlenmektedir. Üst yapı hangisidir?",
        "Şemsiye fonun bağlı fonlarla ilişkisi ve malvarlığı ayrılığı nasıldır?",
        "Şemsiye fondur; her bağlı fonun varlık ve yükümlülükleri ayrıdır",
        ["Yatırım ortaklığıdır; bütün fonların borçları zorunlu olarak birleşir", "Mevduat hesabıdır; her yatırımcı aynı alacaklıdır", "Portföy saklama şirketidir; bütün fonları kendi hesabına işletir", "Borsadır; bağlı fonların paylarını kendisi ihraç eder"],
        "III-52.1 m.4, şemsiye fonu tek içtüzük kapsamında ihraç edilen tüm fonları kapsayan yatırım fonu olarak tanımlar ve her bağlı fonun varlık ve yükümlülüklerini ayırır.",
        "Ortak içtüzük hukuki çatı sağlar; fakat bağlı fonların portföyleri, borçları ve mevzuat sınırları kural olarak ayrı değerlendirilir.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.4", "easy",
    ),
    r(
        "Şemsiye fon içtüzüğü, yalnız kurucunun tek taraflı iç yönetmeliği olarak hazırlanmış ve katılma payı sahipleriyle hukuki ilişki kurmadığı belirtilmiştir. Bu nitelendirme doğru mudur?",
        "Şemsiye fon içtüzüğünün tarafları ve hukuki niteliği nedir?",
        "Hayır; taraflar arasındaki iltihaki sözleşme niteliğindedir",
        ["Evet; yalnız çalışanların görev dağılımını gösteren iç yazıdır", "Evet; katılma payı sahipleriyle hiçbir bağlantısı bulunmaz", "Hayır; fakat içtüzük yalnız borsa emirlerinin eşleşmesini düzenler", "Evet; içtüzük fon varlığının kurucuya devrini sağlar"],
        "III-52.1 m.8, içtüzüğü katılma payı sahipleri ile kurucu, saklayıcı ve varsa yönetici arasında yönetim, saklama ve inançlı mülkiyet esaslarını içeren iltihaki sözleşme olarak düzenler.",
        "İçtüzük, yatırımcının önceden belirlenmiş fon koşullarına katılma payı edinerek dahil olduğu temel fon sözleşmesidir.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.8", "medium",
    ),
    r(
        "Kurucu, fonun portföy yönetimi hizmetini dışarıdan alınca fon faaliyetlerinin mevzuata uygunluğundan artık sorumlu olmadığını ileri sürmektedir. Bu görüş doğru mudur?",
        "Fon faaliyetlerinde dışarıdan hizmet alınması kurucunun sorumluluğunu nasıl etkiler?",
        "Hayır; dışarıdan hizmet kurucunun sorumluluğunu kaldırmaz",
        ["Evet; bütün sorumluluk hizmet sağlayıcıya kesin olarak geçer", "Evet; kurucu fonu temsil etme görevini de tamamen kaybeder", "Hayır; fakat kurucu yalnız kendi ortaklarının hakkını korur", "Evet; hizmet alınca içtüzük ve izahname uygulanmaz"],
        "III-52.1 m.9, kurucuyu katılımcı haklarının korunması, temsil, yönetim ve fon faaliyetlerinin içtüzük ile izahnameye uygunluğundan sorumlu tutar; dışarıdan hizmet bu sorumluluğu kaldırmaz.",
        "Portföy yöneticiliği dahil hizmetlerin devri görev dağılımını değiştirir, kurucunun yatırımcıya ve mevzuata karşı nihai sorumluluğunu ortadan kaldırmaz.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.9", "medium",
    ),
    r(
        "Bir portföy yönetim şirketi yatırım fonunu herhangi bir üst yapı olmadan tekil fon biçiminde kurmak istemektedir. 17.07.2026 itibarıyla genel kuruluş modeli nedir?",
        "17.07.2026 itibarıyla yatırım fonlarının kuruluşunda şemsiye fon bakımından hangi esas uygulanır?",
        "Yatırım fonlarının şemsiye fon biçiminde kurulması gerekir",
        ["Her fonun anonim ortaklık olarak kurulması zorunludur", "Şemsiye fon kurulması bütün yatırım fonları için yasaktır", "Fon yalnız portföy saklayıcısının şubesi olarak kurulabilir", "Yatırım fonu hiçbir içtüzük veya izin olmadan oluşur"],
        "III-52.1 m.10/1, yatırım fonlarının şemsiye fon şeklinde kurulmasını zorunlu tutar; şemsiye fona bağlı her fon için ayrı izahname ve yatırımcı bilgi formu düzenlenir.",
        "Şemsiye fon tek içtüzük çatısıdır. Katılma payı ihracı yapılan bağlı fonlar ise kendi portföy, izahname ve yatırımcı bilgi formuna sahiptir.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.4 ve m.10", "easy",
    ),
    r(
        "Fon katılma payları yalnız kurucunun personeline kapalı biçimde verilecek, izahname hazırlanmadan satış yapılacaktır. 17.07.2026 itibarıyla uygun ihraç yolu hangisidir?",
        "17.07.2026 itibarıyla fon katılma paylarının satış biçimleri ve temel belgeleri nelerdir?",
        "Halka arz, tahsisli veya nitelikli satış; izahname ve bilgi formu gerekir",
        ["Katılma payları belgesiz ve hiçbir yatırımcı sınırlaması olmadan dağıtılır", "Yalnız borsaya bağış yoluyla pay ihracı yapılabilir", "Her satışta ortaklık genel kurulu pay senedi bastırır", "Katılma payı yalnız kredi sözleşmesiyle ve gizlice satılır"],
        "III-52.1 m.11, katılma paylarının halka arz edilmesini veya belirli kişi ya da kuruluşlara tahsisli ya da nitelikli yatırımcılara satılmasını; her fon için izahname ve yatırımcı bilgi formu düzenlenmesini öngörür.",
        "Katılma payı ihracı düzenlenmiş satış kanallarından biriyle yapılır. Kurulca onaylı fon izahnamesi kural olarak ihracın ön koşuludur.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.11/1-3", "medium",
    ),
    r(
        "Kurul fon izahnamesini onaylamış, kurucu bunu 'SPK fonun getirisini garanti etti' şeklinde tanıtmıştır. Bu yorum uygun mudur?",
        "Fon izahnamesinin Kurulca onaylanması hangi iki anlama gelmez?",
        "Tekeffül veya yatırım tavsiyesi değildir",
        ["Onay her yatırımcıya sabit getiri garantisi verir", "Onay fondaki bütün riskleri Kurula devreder", "Onay kurucunun doğru bilgi sorumluluğunu sona erdirir", "Onay fon varlığını devlet borcuna dönüştürür"],
        "III-52.1 m.11/5, izahname onayının bilgilerin doğruluğunun Kurulca tekeffülü veya katılma payına ilişkin yatırım tavsiyesi sayılamayacağını açıkça düzenler.",
        "Kurul onayı kamuyu aydınlatma belgesinin mevzuat standardına ilişkindir; ekonomik başarı ve getiri garantisi değildir.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.11/4-5", "easy",
    ),
    r(
        "Yatırımcı bilgi formunda fonun stratejisi, riskleri, giderleri ve alım satım esasları yerine yalnız reklam sloganı kullanılmıştır. Formun işlevi bakımından eksiklik var mıdır?",
        "Yatırımcı bilgi formunun temel amacı ve içeriği nedir?",
        "Evet; strateji ve riskleri özetleyip bilinçli kararı destekler",
        ["Hayır; formun tek amacı fonun reklamını yapmaktır", "Evet; fakat risk ve gider bilgisinin formda bulunması yasaktır", "Hayır; form yalnız kurucunun personel listesini içerir", "Evet; form yatırımcıdan bütün diğer belgeleri gizlemek için hazırlanır"],
        "III-52.1 m.12; form fonun yapısı, yatırım stratejisi, risk-getiri profili, giderleri ve alım satım esasları gibi temel bilgileri anlaşılır biçimde sunar.",
        "Kurucu formun içtüzük ve izahnameyle tutarlılığından, doğruluğundan ve güncelliğinden sorumludur; form yatırım kararını bilinçli kılmaya hizmet eder.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.12", "medium",
    ),
    r(
        "17.07.2026 tarihinde yatırımcı bilgi formu altı sayfa ve küçük puntolu teknik metin olarak hazırlanmıştır. Genel biçim kuralına uygun mudur?",
        "17.07.2026 itibarıyla yatırımcı bilgi formunun uzunluk ve anlatım standardı nedir?",
        "Hayır; kısa, öz, anlaşılır, en çok iki sayfa ve 12 punto olmalıdır",
        ["Evet; form en az yüz sayfa ve altı punto olmak zorundadır", "Hayır; fakat form yalnız sözlü olarak yatırımcıya aktarılır", "Evet; uzunluk ve yazı boyutu için hiçbir standart yoktur", "Hayır; yatırımcı bilgi formunun hazırlanması bütün fonlarda yasaktır"],
        "III-52.1 m.12/4, yatırımcı bilgi formunun kısa, öz ve anlaşılır biçimde en çok iki sayfa ve 12 punto hazırlanmasını gerektirir.",
        "Biçim kuralı, temel risk ve maliyet bilgisinin yatırımcı tarafından hızlıca okunup karşılaştırılabilmesini destekler.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.12/4", "easy",
    ),
    r(
        "Bir fonun toplam değeri 18 milyon TL, dolaşımdaki katılma payı sayısı 6 milyondur. Katılma paylarının itibari değeri olmadığına göre birim pay değeri kaç TL'dir?",
        "Fon birim pay değeri nasıl hesaplanır ve hangi işleme esas olur?",
        "3 TL'dir; fon toplam değeri pay sayısına bölünür",
        ["108 TL'dir; toplam değer pay sayısıyla çarpılır", "12 TL'dir; pay sayısı toplam değerden çıkarılır", "24 TL'dir; toplam değer ile pay sayısı toplanır", "Birim pay değeri hiçbir hesaplama yapılmadan kurucu tarafından seçilir"],
        "III-52.1 m.14'e göre birim pay değeri fon toplam değerinin katılma payı sayısına bölünmesiyle bulunur: 18 milyon / 6 milyon = 3 TL.",
        "Birim pay değeri katılma payı alım satımına esas fiyattır; katılma paylarının itibari değeri bulunmaz ve fiyatın günlük hesaplanması kuraldır.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.14/1-4", "medium",
    ),
    r(
        "Yatırımcı fondan çıkmak için katılma payını üçüncü bir kişinin borcuna mahsup etmek yerine bilgilendirme dokümanındaki esaslarla fona iade etmiştir. İşlem nasıl nitelendirilir?",
        "Katılma payının alımı ve satımı fonla yatırımcı arasında nasıl gerçekleşir?",
        "Payın fona iadesiyle paraya çevrilmesi katılma payı satımıdır",
        ["İade işlemi kurucunun anonim ortaklık genel kurulunda oy kullanımıdır", "Katılma payı hiçbir zaman fona iade edilemez", "Satım yalnız fiziki senedin noterde devriyle mümkündür", "Fon çıkışı yatırımcının portföydeki belirli varlığı doğrudan almasıdır"],
        "III-52.1 m.15, katılma payı alımını birim pay değerinin tam ve nakden ödenmesine; satımı ise payın bilgilendirme dokümanındaki esaslarla fona iade edilerek paraya çevrilmesine bağlar.",
        "Katılma paylarının günlük alım satımı esastır; fonun türü ve niteliğine göre Kurul istisna getirebilir.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.15/1-2", "medium",
    ),
    r(
        "17.07.2026 tarihinde portföyünün devamlı olarak %85'ini yerli ve yabancı paylara yatıran şemsiye fonun türü hangisidir?",
        "17.07.2026 itibarıyla borçlanma aracı, pay, kıymetli maden veya fon paylarına en az %80 yatırım yapan şemsiye fonlar nasıl adlandırılır?",
        "Hisse senedi şemsiye fonudur",
        ["Borçlanma araçları şemsiye fonudur", "Kıymetli madenler şemsiye fonudur", "Fon sepeti şemsiye fonudur", "Para piyasası şemsiye fonudur"],
        "III-52.1 m.6; toplam değerin en az %80'ini devamlı olarak paylara yatıran fon hisse senedi, borçlanma araçlarına yatıran borçlanma araçları, kıymetli madenlere yatıran kıymetli madenler şemsiye fonudur.",
        "Fon sepeti şemsiye fonu ise portföyünü diğer fonların ve borsa yatırım fonlarının katılma paylarından oluşturur.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.6/1-a", "easy",
    ),
    r(
        "Bir fon yalnız nitelikli yatırımcılara satılmak üzere kurulmuş ve KAP sayfasında açıklanan strateji ile limitler çerçevesinde yönetilmektedir. 17.07.2026 itibarıyla türü nedir?",
        "17.07.2026 itibarıyla serbest şemsiye fonun satış ve portföy rejimi hangi özelliği taşır?",
        "Yalnız nitelikli yatırımcıya satılan serbest fondur",
        ["Para piyasası fonudur; payları yalnız çocuklara satılır", "Garantili fondur; her durumda devlet garantisi taşır", "Katılım fonudur; yalnız faizli araçlardan oluşur", "Fon sepetidir; yalnız kendi paylarına yatırım yapar"],
        "III-52.1 m.6/1-d ve m.25, serbest fonları yalnız nitelikli yatırımcılara satılan ve genel portföy sınırlamaları yerine KAP'taki yatırım stratejisi ile limitleri çerçevesinde yönetilen fonlar olarak düzenler.",
        "Serbest fon sınırsız veya denetimsiz değildir; yatırımcı niteliği, KAP açıklamaları, risk limitleri ve uzman personel koşulları devam eder.",
        "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.6/1-d ve m.25", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Kolektif yatırım kuruluşlarının hukuki yapısı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatırım ortaklığı anonim ortaklıktır\n\nII. Yatırım fonunun ayrı tüzel kişiliği vardır\n\nIII. Yatırım fonu içtüzükle kurulan malvarlığıdır",
        "correct": "I ve III",
        "why": "Yatırım ortaklığı anonim ortaklık, yatırım fonu ise içtüzükle kurulan tüzel kişiliksiz malvarlığıdır. Fonun ayrı tüzel kişiliği bulunmadığından II doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.48 ve m.52", "difficulty": "easy",
    },
    {
        "stem": "Değişken sermayeli yatırım ortaklıkları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sermaye net aktif değere eşittir\n\nII. Payların itibari değeri bulunmaz\n\nIII. Yatırımcı payları yönetimsel hak vermez",
        "correct": "I, II ve III",
        "why": "Değişken sermayeli ortaklıkta sermaye net aktif değere eşittir, paylar nominal değer taşımaz ve yatırımcı payları yönetim hakkı vermez.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.50/1-2", "difficulty": "medium",
    },
    {
        "stem": "Fon malvarlığının korunması bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fon varlığı kurucunun varlığından ayrıdır\n\nII. Fon varlığı kurucunun kamu borcu için haczedilebilir\n\nIII. Tasfiyede yalnız katılma payı sahiplerine ödeme yapılır",
        "correct": "I ve III",
        "why": "Fon malvarlığı kurucudan ayrıdır ve tasfiye bakiyesi katılımcılara aittir. Kamu alacağı için de haczedilemediğinden II doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.53", "difficulty": "medium",
    },
    {
        "stem": "Fon yönetim şirketi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Anonim ortaklık şeklinde kurulur\n\nII. Kuruluş ve faaliyet için Kurul izni gerekir\n\nIII. Yalnız kendi ortaklarının çıkarını gözetir",
        "correct": "I ve II",
        "why": "Fon yönetim şirketi anonim ortaklıktır ve Kurul iznine tabidir. Fonların, yatırımcıların, müşterilerin çıkarı ile piyasa bütünlüğünü gözettiğinden III doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.55", "difficulty": "easy",
    },
    {
        "stem": "Portföy saklama hizmeti bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Katılma payı ihracı ve itfasının uygunluğu gözetilir\n\nII. Birim pay değerinin esaslara uygun hesaplanması gözetilir\n\nIII. Saklayıcı ile fon yönetim şirketi aynı tüzel kişi olabilir",
        "correct": "I ve II",
        "why": "Saklayıcı ihraç-itfa ve birim pay değerinin uygunluğunu gözetir. Saklayıcı ile fon yönetim şirketi aynı tüzel kişi olamayacağı için III doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.56", "difficulty": "medium",
    },
    {
        "stem": "Şemsiye fon yapısı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bağlı fonlar tek içtüzük çatısı altındadır\n\nII. Her bağlı fonun varlık ve yükümlülükleri ayrıdır\n\nIII. Her katılma payı ihracı için ayrı izahname ve yatırımcı bilgi formu düzenlenir",
        "correct": "I, II ve III",
        "why": "Şemsiye fon tek içtüzük çatısı sağlar; bağlı fonların malvarlıkları ayrıdır ve her katılma payı ihracı ayrı izahname ile yatırımcı bilgi formuna dayanır.",
        "ref": "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.4", "difficulty": "easy",
    },
    {
        "stem": "Fon bilgilendirme belgeleri bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatırımcı bilgi formu fonun strateji ve riskini özetler\n\nII. Kurul onayı fon getirisini garanti eder\n\nIII. Formun içtüzük ve izahnameyle tutarlılığından kurucu sorumludur",
        "correct": "I ve III",
        "why": "Yatırımcı bilgi formu strateji ve riskleri özetler ve tutarlılık sorumluluğu kurucudadır. Kurul onayı getiri garantisi oluşturmadığından II doğru değildir.",
        "ref": "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.11-12", "difficulty": "medium",
    },
    {
        "stem": "Fon katılma payları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Katılma paylarının itibari değeri vardır\n\nII. Birim pay değeri fon toplam değerinin pay sayısına bölünmesiyle bulunur\n\nIII. Pay satımı, payın fona iade edilerek paraya çevrilmesidir",
        "correct": "II ve III",
        "why": "Birim pay değeri toplam değerin pay sayısına bölünmesiyle hesaplanır ve yatırımcı payını fona iade ederek çıkar. Katılma payının itibari değeri bulunmadığından I doğru değildir.",
        "ref": "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m.14-15", "difficulty": "medium",
    },
]


if __name__ == "__main__":
    write_topic(
        lesson_id="sermaye_piyasasi_ve_finans",
        topic_id="kolektif_yatirim",
        label="Kolektif Yatırım Kuruluşları",
        slug="kolektif_yatirim",
        prefix="topic-kyk",
        seed=2026071738,
        legislation_version=(
            "6362 sayılı Sermaye Piyasası Kanunu m.48-56; Yatırım Fonlarına "
            "İlişkin Esaslar Tebliği III-52.1; SPK yatırım fonları ve portföy "
            "saklama tanıtım rehberleri (17.07.2026 kontrolü)"
        ),
        rules=RULES,
        premises=PREMISES,
        wrong_banks={},
    )
