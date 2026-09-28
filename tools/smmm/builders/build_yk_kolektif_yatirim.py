# -*- coding: utf-8 -*-
"""SPK Mevzuatı · Kolektif Yatırım Kuruluşları — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · 6362 s. Sermaye Piyasası Kanunu m. 48-56, 130/3
  · Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1), 2024 değişiklikleri işlenmiş
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_kolektif_yatirim_2026.json", lesson="sermaye_piyasasi_ve_finans", topic="kolektif_yatirim",
          konu_adi="Kolektif Yatırım Kuruluşları", seed=2026092823,
          surum="6362 s. Sermaye Piyasası Kanunu; Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1, 2024); 28.09.2026 kontrolü")

K = "6362 sayılı Sermaye Piyasası Kanunu’na göre"
T = "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1)’ne göre"

# ================================================================ yatırım ortaklıkları (m. 48-49)
P.q("6362 s. SPKn m. 48-49",
    f"{K}, yatırım ortaklıklarının kuruluşuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırım ortaklıkları esas sermayeli anonim ortaklık şeklinde kurulur.",
    ["Başlangıç sermayeleri Kurulca belirlenen miktardan az olamaz.",
     "Ticaret unvanlarında “Yatırım Ortaklığı” ibaresinin bulunması gerekir.",
     "Pay bedellerinin kuruluş sırasında tam ve nakden ödenmesi gerekir.",
     "Portföy saklama hizmetini yürütecek yetkili bir kuruluşun belirlenmiş olması gerekir."],
    "Kanun m. 49/1'e göre yatırım ortaklıklarına kuruluş izni verilebilmesi için kayıtlı sermayeli anonim ortaklık şeklinde "
    "kurulmaları, başlangıç sermayesinin Kurulca belirlenen miktardan az olmaması, payların nakit karşılığı çıkarılıp bedellerin "
    "tam ve nakden ödenmesi, unvanda “Yatırım Ortaklığı” ibaresi ve portföy saklayıcısının belirlenmiş olması gerekir.",
    zorluk="easy")

P.q("6362 s. SPKn m. 49/4",
    "Bir menkul kıymet yatırım ortaklığı, portföyünün yönetimini bir portföy yönetim şirketinden hizmet alarak yürütmek "
    f"istemektedir. {K}, bunun için aşağıdakilerden hangisi gereklidir?",
    "Esas sözleşmede hüküm bulunması ve Kurulun onayının alınması",
    ["Esas sözleşmede hüküm bulunması, Kurul onayı aranmaz",
     "Genel kurul kararı alınması, Kurul onayı aranmaz",
     "Yönetim kurulu kararı alınması ve KAP’ta açıklanması",
     "Hizmet alınacak şirketin yatırım ortaklığına ortak olması"],
    "Kanun m. 49/4'e göre yatırım ortaklıkları, esas sözleşmelerinde hüküm bulunmak kaydıyla ve Kurulun onayını almak "
    "şartıyla bir portföy yönetim şirketinden hizmet alabilir; iki şart birlikte aranır.")

P.q("6362 s. SPKn m. 49/5-6",
    "Kurulmakta olan bir gayrimenkul yatırım ortaklığının kurucuları, sermaye taahhütlerinin bir kısmını sahip oldukları bir "
    f"alışveriş merkezini ortaklığa devrederek karşılamak istemektedir. {K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurulca portföye alınması uygun görülen varlıklar ayni sermaye olarak konulabilir.",
    ["Yatırım ortaklıklarında pay bedelleri nakden ödenmek zorunluluğundadır; ayni sermaye konulamaz.",
     "Ayni sermaye ancak sermaye artırımlarında konulabilir, kuruluşta konulamaz.",
     "Ayni sermaye konulabilmesi için genel kurulda oybirliği aranır.",
     "Ayni sermaye olarak konulan varlığın değerini kurucular belirler."],
    "Kanun m. 49/5'e göre gayrimenkul yatırım ortaklıklarının kuruluşlarında ve sermaye artırımlarında Kurulca portföye "
    "alınması uygun görülen varlıklar ayni sermaye olarak konulabilir; bu varlıkların değerleme esaslarını Kurul belirler. "
    "Genel kural olan nakdi ödeme şartının istisnasıdır.")

P.oncul("6362 s. SPKn m. 48-49",
    "Yatırım ortaklıklarına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Esas sözleşme değişikliklerinde Kurulun uygun görüşünün alınması zorunludur.",
     "Kuruluşa ilişkin şartlar, bir anonim ortaklığın yatırım ortaklığına dönüşümünde de aranır.",
     "Yatırım ortaklıklarının kurucularına aracı kurum kurucularına ilişkin şartlar kıyasen uygulanır.",
     "Menkul kıymet yatırım ortaklıkları kuruluşta ayni sermaye kabul edebilir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve III", ["I ve II", "II ve III", "III ve IV", "I, II ve III", "I, III ve IV"],
    "Kanun m. 48/3 esas sözleşme değişikliklerinde Kurul uygun görüşünü, m. 49/3 kuruluş şartlarının dönüşümde de "
    "aranmasını, m. 49/2 kuruculara m. 44'ün kıyasen uygulanmasını öngörür. Ayni sermaye istisnası m. 49/5'e göre yalnız "
    "gayrimenkul yatırım ortaklıklarına tanınmıştır.")

# ================================================================ değişken sermayeli yatırım ortaklığı (m. 50-51)
P.sayisal("6362 s. SPKn m. 50/1",
    "Bir değişken sermayeli yatırım ortaklığının değerleme günündeki varlıklarının toplamı 500 milyon TL, borçlarının "
    f"toplamı 120 milyon TL’dir. {K}, bu ortaklığın o gün itibarıyla sermayesi kaç milyon TL’dir?",
    "380", ["120", "440", "500", "620"],
    "Kanun m. 50/1'e göre değişken sermayeli yatırım ortaklıklarının sermayesi her zaman net aktif değerine eşittir; net aktif "
    "değer varlıklar toplamından borçlar toplamının düşülmesiyle bulunur: 500 − 120 = 380 milyon TL.")

P.q("6362 s. SPKn m. 50/2",
    f"{K}, değişken sermayeli yatırım ortaklıklarının paylarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırımcı payları sahibine oy hakkı dahil idari haklar verir.",
    ["Kurucu paylarının nama yazılı olması zorunludur.",
     "Değişken sermayeli yatırım ortaklıklarının paylarının itibari değeri bulunmaz.",
     "Kurucu payları kuruluştan sonra Kurul izni ve genel kurul kararıyla ihraç edilebilir.",
     "Kurul onayı alınmadan yapılan kurucu pay devirleri pay defterine kaydolunmaz."],
    "Kanun m. 50/2'ye göre DSYO payları yatırımcı payları ile nama yazılı kurucu paylarından oluşur ve itibari değerleri "
    "yoktur. Kurucu payları kuruluştan sonra da Kurul izni ve genel kurul kararıyla ihraç edilebilir; izinsiz devirler pay "
    "defterine kaydolunmaz. Yatırımcı payları sahibine idari haklar vermez.")

P.sayisal("6362 s. SPKn m. 50/4",
    "Bir değişken sermayeli yatırım ortaklığında kurucu paylarının değeri Kurulca belirlenen tutarın altına düşmüş ve yönetim "
    f"kurulu durumu Kurula bildirmiştir. {K}, genel kurul bildirimi takiben en geç kaç gün içinde toplanır?",
    "30", ["7", "15", "45", "60"],
    "Kanun m. 50/4'e göre kurucu paylarının değerinin belirlenen tutarın altına düşmesi veya mali durumun zayıflaması hâlinde "
    "yönetim kurulu bunu Kurula bildirir, genel kurulu derhâl toplantıya çağırır ve genel kurul en geç otuz gün içinde "
    "toplanır; durum giderilemezse Kurul tasfiye dahil her türlü tedbiri alır.")

P.q("6362 s. SPKn m. 50/3",
    "Değişken sermayeli bir yatırım ortaklığının yatırımcı payı sahibi, paylarını ortaklığa geri vermek istemektedir. "
    f"{K}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ortaklık, talep üzerine payları itfa edip bedelini geri ödemekle yükümlüdür.",
    ["Ortaklık, payları ancak genel kurul kararıyla ve sermaye azaltımı yoluyla geri alabilir.",
     "Pay sahibi paylarını ancak borsada satarak ortaklıktan çıkabilir.",
     "Ortaklık, kendi paylarını ancak TTK’nın kendi payını iktisap hükümleri çerçevesinde alabilir.",
     "Geri ödeme, ancak kurucu paylarının değeri artırıldıktan sonra yapılabilir."],
    "Kanun m. 50/3'e göre değişken sermayeli yatırım ortaklıkları pay ihraç eder ve ihraç olunan payları itfa eder; pay "
    "sahibinin talebi üzerine payları itfa etmek ve sermayede buna karşılık gelen bedeli geri ödemekle yükümlüdür. İtfa "
    "usulü esas sözleşmede gösterilir; m. 51 TTK'nın kendi payını iktisap hükümlerini uygulamaz.")

P.q("6362 s. SPKn m. 51",
    f"{K}, aşağıdakilerden hangisi değişken sermayeli yatırım ortaklıklarında uygulanmayacak 6102 sayılı Türk Ticaret "
    "Kanunu hükümleri arasında sayılmamıştır?",
    "Yönetim kurulu üyelerinin sorumluluğuna ilişkin hükümler",
    ["Asgari sermaye miktarına ilişkin hükümler",
     "Nominal değere ilişkin hükümler",
     "Yedek akçelere ilişkin hükümler",
     "Kâr-zarar hesabı ve kârın dağıtımına ilişkin hükümler"],
    "Kanun m. 51'e göre DSYO'larda TTK'nın esas sermaye, asgari sermaye, esas sözleşmenin asgari içeriği, ayni sermaye, "
    "nominal değer, kendi paylarını iktisap, sermaye artırım ve azaltımı, pay taahhüdü ve ödenmesi, pay devri "
    "kısıtlamaları, kâr-zarar ve kâr dağıtımı, yedek akçeler ve tasfiye hükümleri uygulanmaz. Yönetim kurulu sorumluluğu "
    "bu listede yoktur.", zorluk="hard")

# ================================================================ yatırım fonu (m. 52-54)
P.q("6362 s. SPKn m. 52/1",
    f"{K}, yatırım fonlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırım fonları, kurucu yatırımcıların genel kurul kararıyla kurulur.",
    ["Yatırım fonları portföy yönetim şirketleri tarafından iç tüzük ile kurulur.",
     "Yatırım fonları tüzel kişiliği bulunmayan mal varlıklarıdır.",
     "Fon portföyü inançlı mülkiyet esaslarına göre işletilir.",
     "Fon, tasarruf sahiplerinden katılma payı karşılığında toplanan varlıklarla oluşturulur."],
    "Kanun m. 52/1'e göre yatırım fonu, tasarruf sahiplerinden katılma payı karşılığı toplanan para veya varlıklarla, "
    "tasarruf sahipleri hesabına inançlı mülkiyet esaslarına göre portföy işletmek amacıyla portföy yönetim şirketleri "
    "tarafından fon iç tüzüğü ile kurulan ve tüzel kişiliği bulunmayan mal varlığıdır; genel kurulu yoktur.")

P.sayisal("6362 s. SPKn m. 52/2",
    "Bir portföy yönetim şirketi, gerekli belgeleri eksiksiz sunarak yeni bir yatırım fonu kurmak için Kurula başvurmuştur. "
    f"{K}, bu başvuru belgelerin sunulmasından itibaren en geç kaç ay içinde karara bağlanır?",
    "2", ["1", "3", "6", "12"],
    "Kanun m. 52/2'ye göre yatırım fonlarının kuruluş izni için kurucunun yetkili bir portföy saklayıcısıyla anlaşmış olması "
    "ve iç tüzüğün Kurulca onaylanması gerekir; başvurular gerekli belgelerin eksiksiz sunulmasından itibaren iki ay içinde "
    "karara bağlanır. Portföy yönetim şirketi kuruluş başvuruları için bu süre altı aydır.")

P.q("6362 s. SPKn m. 52/5",
    "Bir yatırım fonu portföyüne bir iş merkezi almıştır. "
    f"{K}, bu taşınmazın tapu kütüğüne tesciline ilişkin aşağıdakilerden hangisi doğrudur?",
    "Taşınmaz fon adına tescil edilir.",
    ["Taşınmaz portföy yönetim şirketi adına tescil edilir.",
     "Taşınmaz portföy saklayıcısı adına tescil edilir.",
     "Taşınmaz katılma payı sahipleri adına paylı mülkiyet olarak tescil edilir.",
     "Taşınmaz, Kurul adına emaneten tescil edilir."],
    "Kanun m. 52/5'e (7222 s. Kanunla 2020) göre fon; tapu ve diğer resmî sicil işlemleri ile ortağı olacağı şirketlerin "
    "ticaret sicili işlemleriyle sınırlı olarak tüzel kişiliği haiz addolunur ve portföydeki taşınmazlar tapu kütüğüne fon "
    "adına tescil edilir.", zorluk="easy")

P.q("6362 s. SPKn m. 52/5",
    "Portföyünde taşınmaz bulunan bir yatırım fonu adına tapuda satış işlemi yapılacaktır. "
    f"{K}, bu işlem kimlerin imzasıyla gerçekleştirilir?",
    "Şirket ile saklayıcıyı temsil eden birer yetkilinin müşterek imzasıyla",
    ["Portföy yönetim şirketinin yetkilisinin tek başına imzasıyla",
     "Portföy saklayıcısının yetkilisinin tek başına imzasıyla",
     "Portföy yönetim şirketi yetkilisi ile Kurul temsilcisinin müşterek imzasıyla",
     "Katılma payı sahiplerinin çoğunluğunu temsil eden kişinin imzasıyla"],
    "Kanun m. 52/5'e göre tapuda, ticaret sicilinde ve diğer resmî sicillerde fon adına yapılacak işlemler portföy yönetim "
    "şirketi ile portföy saklama hizmetini yürüten kuruluşu temsil eden birer yetkilinin müşterek imzalarıyla gerçekleştirilir.")

P.q("6362 s. SPKn m. 52/4",
    f"{K}, portföy yönetim şirketi ile katılma payı sahipleri arasındaki ilişkilerde Kanunda, ilgili mevzuatta ve fon iç "
    "tüzüğünde hüküm bulunmayan hâllerde aşağıdakilerden hangisi kıyasen uygulanır?",
    "Türk Borçlar Kanunu’nun vekâlet sözleşmesine ilişkin hükümleri",
    ["Türk Borçlar Kanunu’nun adi ortaklığa ilişkin hükümleri",
     "Türk Ticaret Kanunu’nun anonim şirketlere ilişkin hükümleri",
     "Türk Medeni Kanunu’nun vakıflara ilişkin hükümleri",
     "Türk Borçlar Kanunu’nun eser sözleşmesine ilişkin hükümleri"],
    "Kanun m. 52/4'e göre bu ilişkilerde hüküm bulunmayan hâllerde 6098 sayılı TBK'nın 502 ila 514 üncü maddeleri, yani "
    "vekâlet sözleşmesine ilişkin hükümler kıyasen uygulanır.")

P.q("6362 s. SPKn m. 53",
    f"{K}, yatırım fonunun mal varlığının ayrılığına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Portföy yönetim şirketinin iflası hâlinde fon mal varlığı iflas masasına dâhil edilir.",
    ["Fon mal varlığı, portföy yönetim şirketinin ve saklayıcının mal varlığından ayrıdır.",
     "Fon mal varlığı, kamu alacaklarının tahsili amacıyla da haczedilemez.",
     "Fon mal varlığının tasfiyesinde ödeme katılma payı sahiplerine yapılır.",
     "Şirketin üçüncü kişilere borçları, fonun aynı kişilerden alacaklarıyla mahsup edilemez."],
    "Kanun m. 53'e göre fonun mal varlığı portföy yönetim şirketi ve saklayıcının mal varlığından ayrıdır; kamu alacakları "
    "dahil haczedilemez, ihtiyati tedbir konulamaz ve iflas masasına dâhil edilemez. Tasfiyede yalnız katılma payı sahiplerine "
    "ödeme yapılır; mahsup yasağı vardır.")

P.q("6362 s. SPKn m. 53/2",
    "Bir yatırım fonu, iç tüzüğünde hüküm bulunmak kaydıyla, fon hesabına bir türev araç işleminde bulunmuştur. "
    f"{K}, fon mal varlığının bu işlem için teminat gösterilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Fon hesabına olması ve iç tüzükte hüküm bulunması şartıyla teminat gösterilebilir.",
    ["Fon mal varlığı hangi amaçla olursa olsun teminat gösterilemez.",
     "Teminat gösterilebilmesi için katılma payı sahiplerinin onayı gerekir.",
     "Teminat gösterilebilmesi için portföy yönetim şirketinin de müteselsil kefil olması gerekir.",
     "Teminat ancak portföy yönetim şirketinin kendi borçları için gösterilebilir."],
    "Kanun m. 53/2'ye göre fon mal varlığı, fon hesabına olması ve fon iç tüzüğünde hüküm bulunması şartıyla kredi almak, "
    "türev araç işlemleri, açığa satış işlemleri veya fon adına taraf olunan benzer işlemler haricinde teminat gösterilemez "
    "ve rehnedilemez.")

# ================================================================ portföy yönetim şirketi ve saklama (m. 55-56, 130/3)
P.q("6362 s. SPKn m. 55",
    f"{K}, portföy yönetim şirketlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Portföy yönetim şirketleri limited şirket olarak da kurulabilir.",
    ["Ana faaliyet konusu yatırım fonlarının kurulması ve yönetimidir.",
     "Kurulması ve faaliyete geçmesi Kurulun iznine tabidir.",
     "Faaliyetleri nedeniyle yatırdığı teminatlar kamu alacakları için de haczedilemez.",
     "Esas sözleşme değişikliklerinde Kurulun uygun görüşünün alınması zorunludur."],
    "Kanun m. 55'e göre portföy yönetim şirketi, ana faaliyet konusu yatırım fonlarının kurulması ve yönetimi olan anonim "
    "ortaklıktır; kuruluşu ve faaliyete geçmesi Kurul iznine tabidir. Yatırdığı teminatlar haczedilemez; dönüşüm ve esas "
    "sözleşme değişikliklerinde Kurulun uygun görüşü zorunludur.", zorluk="easy")

P.sayisal("6362 s. SPKn m. 55/1",
    f"{K}, portföy yönetim şirketlerinin kuruluş başvuruları, gerekli belgelerin Kurula eksiksiz sunulmasından itibaren kaç ay "
    "içinde karara bağlanır?",
    "6", ["1", "2", "3", "12"],
    "Kanun m. 55/1'e göre portföy yönetim şirketlerinin kuruluş başvuruları gerekli belgelerin eksiksiz sunulmasından itibaren "
    "altı ay içinde Kurul tarafından karara bağlanır ve ilgililere bildirilir. Yatırım fonu kuruluşunda süre iki aydır.")

P.oncul("6362 s. SPKn m. 56/1",
    "Bir yatırım fonuna ilişkin aşağıdaki işlemler verilmiştir:",
    ["Fon portföyüne hangi payların alınacağına ilişkin yatırım kararını vermek",
     "Katılma paylarının ihraç ve itfa işlemlerinin mevzuata ve iç tüzüğe uygunluğunu sağlamak",
     "Birim katılma payı değerinin değerleme esaslarına göre hesaplanmasını sağlamak",
     "Fon gelirlerinin mevzuata ve iç tüzüğe uygun kullanılmasını sağlamak"],
    f"{K}, yukarıdakilerden hangileri portföy saklama hizmetinin kapsamında yer alır?",
    "II, III ve IV", ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 56/1'e göre portföy saklama hizmeti ihraç ve itfa işlemlerinin uygunluğunu, birim pay değerinin doğru "
    "hesaplanmasını, talimatların yerine getirilmesini, bedellerin aktarılmasını, gelirlerin uygun kullanılmasını ve varlık "
    "alım satımlarının uygunluğunu sağlamayı içerir. Yatırım kararı vermek portföy yöneticisinin işidir.")

P.q("6362 s. SPKn m. 56/6",
    "Bir portföy yönetim şirketi, kurucusu olduğu yatırım fonlarının portföy saklama hizmetini de kendi bünyesinde yürütmeyi "
    f"planlamaktadır. {K}, bu plana ilişkin aşağıdakilerden hangisi doğrudur?",
    "Saklayıcı ile şirket aynı tüzel kişi olamayacağından plan uygulanamaz.",
    ["Kurulun onayıyla saklama hizmeti şirket bünyesinde yürütülebilir.",
     "Fon iç tüzüğünde hüküm bulunmak kaydıyla şirket saklama hizmetini de yürütebilir.",
     "Şirket, fon toplam değeri Kurulca belirlenen tutarı aşmadıkça saklamayı yürütebilir.",
     "Saklama hizmeti şirket bünyesinde yürütülür, ancak MKK’ya bildirim yapılır."],
    "Kanun m. 56/6'ya göre portföy saklama hizmetini yürüten kuruluş ile portföy yönetim şirketi aynı tüzel kişi olamaz; ikisi "
    "birbirinden bağımsız ve sadece katılma payı sahiplerinin menfaatleri doğrultusunda hareket eder.")

P.q("6362 s. SPKn m. 56/7",
    f"{K}, portföy saklayıcısı ile portföy yönetim şirketi arasındaki bağımsızlığa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Portföy yönetim şirketinin ortakları saklayıcı kuruluşta yönetici olarak görev alabilir.",
    ["Saklayıcı kuruluşun yöneticileri portföy yönetim şirketinde ortak olamaz.",
     "Fon portföyüne aracılık eden yatırım kuruluşunun yöneticileri portföy yönetim şirketinde yönetici olamaz.",
     "Portföy yönetim şirketini temsil ve ilzama yetkili kişiler saklayıcıda temsilci olamaz.",
     "Saklayıcı ve portföy yönetim şirketi sadece katılma payı sahiplerinin menfaatleri doğrultusunda hareket eder."],
    "Kanun m. 56/7'ye göre saklayıcı ve fona aracılık eden yatırım kuruluşunun yöneticileri ve temsilcileri portföy yönetim "
    "şirketinde ortak, yönetici veya temsilci olamaz; portföy yönetim şirketinin ortakları, yöneticileri ve temsilcileri de "
    "saklayıcıda yönetici ya da temsilci olamaz.", zorluk="hard")

P.q("6362 s. SPKn m. 56/4",
    "Bir fonun portföy saklayıcısı, saklamasındaki yabancı payları yurt dışındaki başka bir saklama kuruluşu nezdinde "
    f"saklatmaktadır. {K}, bu durumda sorumluluğa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Saklama hizmeti veren tüm kuruluşlar müteselsilen sorumludur.",
    ["Sorumluluk alt saklayıcıya geçer, ilk saklayıcı sorumluluktan kurtulur.",
     "Her kuruluş sadece kendi sakladığı varlıklar için kusursuz sorumludur.",
     "Sorumluluk portföy yönetim şirketine geçer.",
     "Alt saklama Kurul iznine bağlı olduğundan sorumluluk Kurula aittir."],
    "Kanun m. 56/4'e göre portföy saklayıcısı saklamasındaki varlıkların tümünü veya bir kısmını başka portföy saklama "
    "kuruluşları nezdinde saklayabilir; bu hâlde portföy saklama hizmetini veren tüm kuruluşlar müteselsilen sorumludur.")

P.q("6362 s. SPKn m. 56/2-3",
    f"{K}, portföy saklama hizmetinden doğan sorumluluğa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırım ortaklıklarında saklayıcı, verdiği zararlardan doğrudan pay sahiplerine karşı sorumludur.",
    ["Yatırım fonlarında saklayıcı, portföy yönetim şirketi ve katılma payı sahiplerine verdiği zarardan sorumludur.",
     "Portföy yönetim şirketi, Kanun ihlali nedeniyle doğan zararın saklayıcıdan giderilmesini talep etmekle yükümlüdür.",
     "Saklayıcı da portföy yönetim şirketinden doğan zararların giderilmesini talep etmekle yükümlüdür.",
     "Pay veya katılma payı sahiplerinin dava açma hakkı saklıdır."],
    "Kanun m. 56/2'ye göre saklayıcı, yükümlülüklerini yerine getirmemesi nedeniyle yatırım fonlarında portföy yönetim şirketi "
    "ve katılma payı sahiplerine, yatırım ortaklıklarında ise ortaklığa verdiği zararlardan sorumludur. m. 56/3 karşılıklı "
    "talep yükümlülüğü getirir ve pay sahiplerinin dava hakkını saklı tutar.", zorluk="hard")

P.sayisal("6362 s. SPKn m. 130/3",
    "Bir yatırım fonunun üçer aylık dönemin son iş günündeki net varlık değeri 800 milyon TL’dir. "
    f"{K} öngörülen oranın uygulandığı varsayımıyla, bu dönem için Kurul hesabına yatırılacak ücret kaç TL’dir?",
    "40.000", ["4.000", "24.000", "80.000", "400.000"],
    "Kanun m. 130/3'e göre yatırım fonları ve DSYO'lar üçer aylık dönemlerin son iş gününde net varlık değerlerinin yüz binde "
    "beşi tutarındaki ücreti izleyen on iş günü içinde Kurul hesabına yatırır: 800.000.000 × 5 / 100.000 = 40.000 TL. Kurul "
    "bu oranı aşmamak kaydıyla farklı oran belirleyebilir.", zorluk="hard")

# ================================================================ Tebliğ: şemsiye fon ve fon türleri (m. 4-7, 10)
P.q("III-52.1 m. 6/1-a",
    "Bir fonun iç tüzük ve izahnamesine göre fon toplam değerinin en az %80’i devamlı olarak Borsa İstanbul’da işlem gören "
    f"ihraççı paylarına yatırılmaktadır. {T}, bu fonun bağlı olacağı şemsiye fon türü aşağıdakilerden hangisidir?",
    "Hisse senedi şemsiye fonu",
    ["Değişken şemsiye fon", "Katılım şemsiye fonu", "Fon sepeti şemsiye fonu", "Serbest şemsiye fon"],
    "Tebliğ m. 6/1-a'ya göre fon toplam değerinin en az %80'i devamlı olarak yerli ve/veya yabancı ihraççıların paylarına "
    "yatırılan fonlar hisse senedi şemsiye fonuna bağlıdır. Bu oranın BİAŞ'ta işlem gören paylardan oluşması fonu ayrıca "
    "“hisse senedi yoğun fon” yapar.", zorluk="easy")

P.sayisal("III-52.1 m. 6/1-b",
    f"{T}, para piyasası şemsiye fonuna bağlı bir fonun günlük olarak hesaplanan portföy ağırlıklı ortalama vadesi en fazla "
    "kaç gün olabilir?",
    "45", ["30", "60", "90", "184"],
    "Tebliğ m. 6/1-b'ye göre para piyasası fonlarının portföyü devamlı olarak vadesine en fazla 184 gün kalmış likiditesi "
    "yüksek araçlardan oluşur ve günlük hesaplanan ağırlıklı ortalama vadesi en fazla 45 gündür.")

P.q("III-52.1 m. 6/1-c, d",
    "Bir portföy yönetim şirketi, portföyünün tamamı devamlı olarak kira sertifikaları, katılma hesapları, ortaklık payları ve "
    f"altından oluşacak bir fon kurmak istemektedir. {T}, bu fon hangi şemsiye fon türüne bağlanır?",
    "Katılım şemsiye fonu",
    ["Kıymetli madenler şemsiye fonu", "Borçlanma araçları şemsiye fonu", "Değişken şemsiye fon", "Koruma amaçlı şemsiye fon"],
    "Tebliğ m. 6/1-c'ye göre portföyünün tamamı devamlı olarak kira sertifikaları, katılma hesapları, ortaklık payları, altın "
    "ve diğer kıymetli madenler ile faize dayalı olmayan araçlardan oluşan fonlar katılım şemsiye fonuna bağlıdır.")

P.q("III-52.1 m. 6/1-d, 25",
    "Bir fonun katılma payları yalnız nitelikli yatırımcılara satılmak üzere ihraç edilecektir. "
    f"{T}, bu fona ilişkin aşağıdakilerden hangisi doğrudur?",
    "Serbest şemsiye fona bağlanır, genel portföy sınırlamalarına tabi olmaz.",
    ["Değişken şemsiye fona bağlanır ve genel portföy sınırlamalarına tabidir.",
     "Serbest şemsiye fona bağlanır, ancak tek ihraççı sınırlaması %10 olarak uygulanır.",
     "Garantili şemsiye fona bağlanır ve vadesi en az altı ay olur.",
     "Fon sepeti şemsiye fonuna bağlanır ve diğer fonlara yatırım yapamaz."],
    "Tebliğ m. 6/1-d'ye göre katılma payları sadece nitelikli yatırımcılara satılmak üzere kurulan fonlar serbest şemsiye "
    "fona bağlıdır; m. 25'e göre serbest fonlar m. 17-24'teki portföy ve işlem sınırlamalarına tabi olmaksızın KAP'taki "
    "yatırım stratejileri ve limitleri dahilinde yatırım yapar.", zorluk="hard")

P.oncul("III-52.1 m. 6/1-e, 27",
    "Garantili ve koruma amaçlı fonlara ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Garantili fonlarda getiri, garantör tarafından verilen garantiye dayanılarak taahhüt edilir.",
     "Bu fonların vadeleri asgari üç ay olarak belirlenir.",
     "Koruma amaçlı fonlarda koruma, en iyi gayret esası çerçevesinde amaçlanır.",
     "Garanti ya da koruma tüm katılma payı sahipleri açısından aynı nitelikte olmalıdır."],
    f"{T}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV", ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Tebliğ m. 6/1-e'ye göre garantili fonlarda geri ödeme garantör garantisine dayanılarak taahhüt edilir, koruma amaçlı "
    "fonlarda en iyi gayret esasıyla amaçlanır. m. 27'ye göre bu fonların vadesi asgari altı aydır ve garanti ya da koruma "
    "tüm katılma payı sahipleri için aynı niteliktedir.")

P.q("III-52.1 m. 7",
    f"{T}, fon unvanlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yabancı araçlara %50 yatırım yapan fonun unvanında “Yabancı” ibaresi zorunludur.",
    ["Fonun unvanı yatırım stratejisine uygun olmalıdır.",
     "Endeks kapsamındaki varlıklardan oluşan fonların unvanında “Endeks” ibaresi yer alır.",
     "İştiraklerin araçlarından oluşan fonların unvanında “İştirak” ibaresi yer alır.",
     "Fonun diğer fonlardan üstün olduğunu ima eden ifadeler unvanda kullanılamaz."],
    "Tebliğ m. 7'ye göre unvan yatırım stratejisine uygun olmalı, yanıltıcı veya üstünlük ima eden ifadeler içermemelidir; "
    "endeks fonlarında “Endeks”, iştirak fonlarında “İştirak” ibaresi zorunludur. “Yabancı” ibaresi fon toplam değerinin en "
    "az %80'i oranında yabancı araçlara yatırım yapan fonlar için zorunludur.")

P.oncul("III-52.1 m. 4, 8, 10",
    "Şemsiye fon yapısına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Şemsiye fona bağlı fonların katılma payları, her fon için ayrı iç tüzüğe dayalı olarak ihraç edilir.",
     "Yatırım fonlarının şemsiye fon şeklinde kurulması zorunludur.",
     "Şemsiye fona bağlı her bir fonun varlık ve yükümlülükleri birbirinden ayrıdır.",
     "Şemsiye fon iç tüzüğü genel işlem şartlarını içeren iltihaki bir sözleşmedir."],
    f"{T}, yukarıdaki ifadelerden hangileri doğrudur?",
    "II, III ve IV", ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Tebliğ m. 10'a göre yatırım fonlarının şemsiye fon şeklinde kurulması zorunludur; m. 4/3'e göre bağlı fonların varlık ve "
    "yükümlülükleri birbirinden ayrıdır. m. 8'e göre iç tüzük iltihaki bir sözleşmedir ve bağlı fonların katılma payları tek "
    "şemsiye fon iç tüzüğüne dayalı olarak ihraç edilir; her fon için ayrı izahname ve yatırımcı bilgi formu düzenlenir.")

# ================================================================ Tebliğ: kuruluş, ihraç, bilgilendirme (m. 10-13)
P.q("III-52.1 m. 10/5",
    "Kurul, bir şemsiye fonun iç tüzüğünü onaylamış ve karar kurucuya tebliğ edilmiştir. "
    f"{T}, iç tüzüğün tescil ve ilanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Altı iş günü içinde ticaret siciline tescil ettirilir, TTSG ve KAP’ta ilan edilir.",
    ["Tebellüğü izleyen on iş günü içinde sadece KAP’ta ilan edilir, tescil edilmez.",
     "Tebellüğü izleyen otuz gün içinde Kurulun internet sitesinde ilan edilir.",
     "İç tüzük ilk fonun satışa başladığı gün ticaret siciline tescil ettirilir.",
     "İç tüzük ticaret siciline tescil edilmez; kurucunun ve KAP’ın internet sitesinde yayımlanması yeterlidir."],
    "Tebliğ m. 10/5'e göre Kurulca onaylanan iç tüzük, Kurul kararının tebellüğünü izleyen altı iş günü içinde kurucunun "
    "merkezinin bulunduğu yerin ticaret siciline tescil ettirilir ve TTSG ile KAP'ta ilan olunur.")

P.q("III-52.1 m. 11/2",
    "Bir şemsiye fonun iç tüzüğü ticaret siciline tescil edilmiş, ancak kurucu bağlı ilk fonun katılma payı ihracı için "
    f"Kurula başvurmamıştır. {T}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlk başvuru tescilden itibaren üç ay içinde yapılmazsa iç tüzük sicilden terkin ettirilir.",
    ["Kurucu, başvuru yapıncaya kadar süre sınırı olmaksızın iç tüzüğü tescilli tutabilir.",
     "İlk başvuru bir yıl içinde yapılmazsa şemsiye fon Kurul kararıyla tasfiye edilir.",
     "Başvuru süresi geçerse kurucuya idari para cezası verilir, iç tüzük geçerliliğini korur.",
     "İlk başvuru altı ay içinde yapılmazsa kurucunun faaliyet izni iptal edilir."],
    "Tebliğ m. 11/2'ye göre şemsiye fona bağlı ilk fonun katılma payı ihracı başvurusunun iç tüzüğün tescilinden itibaren en "
    "geç üç ay içinde yapılması zorunludur; yapılmazsa iç tüzük kurucu tarafından ticaret sicilinden terkin ettirilir ve "
    "belgeler altı iş günü içinde Kurula gönderilir.")

P.q("III-52.1 m. 11/4",
    f"{T}, fon izahnamesinin Kurulca onaylanması sürecine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İzahname, Kurula sunulan belgeler çerçevesinde otuz iş günü içinde incelenir.",
    ["Bilgilerin tutarlı, anlaşılabilir ve standarda göre eksiksiz olduğu tespit edilirse izahname onaylanır.",
     "Eksik belge varsa başvuru sahibi başvurudan itibaren on iş günü içinde bilgilendirilir.",
     "Eksikler tamamlanınca inceleme süresi belgelerin sunulduğu tarihten itibaren işlemeye başlar.",
     "Onaylanmayan başvurular gerekçesiyle başvuru sahibine bildirilir."],
    "Tebliğ m. 11/4'e göre izahname Kurula sunulan bilgi ve belgeler çerçevesinde 20 iş günü içinde incelenir; eksik veya ek "
    "belge gerekiyorsa başvuru sahibi 10 iş günü içinde bilgilendirilir ve 20 iş günlük süre eksiklerin sunulduğu tarihten "
    "itibaren işler. Onaylanmama gerekçeli bildirilir.")

P.q("III-52.1 m. 11/6-8",
    f"{T}, katılma paylarının satışa sunulmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Onaylı izahname ticaret siciline tescil edilir ve TTSG’de ilan edilir.",
    ["İzahname ve yatırımcı bilgi formu izin yazısının tebellüğünü izleyen on iş günü içinde KAP’ta yayımlanır.",
     "İzahnamenin nerede yayımlandığı hususu ticaret siciline tescil ettirilir.",
     "Katılma payları yatırımcı bilgi formunun KAP’ta yayımını takiben satışa sunulur.",
     "Toplanan para takip eden iş günü izahnamede belirlenen varlıklara yatırılır."],
    "Tebliğ m. 11/6'ya göre izahname ve yatırımcı bilgi formu tebellüğü izleyen 10 iş günü içinde KAP'ta ve kurucunun "
    "sitesinde yayımlanır; izahname ayrıca tescil ve ilan edilmez, yalnız nerede yayımlandığı tescil edilir. m. 11/7-8'e göre "
    "satış formun KAP'ta yayımını izler ve toplanan para takip eden iş günü yatırılır.", zorluk="hard")

P.q("III-52.1 m. 12-13",
    f"{T}, yatırımcı bilgi formuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yatırımcı bilgi formunda yapılacak her değişiklik Kurul onayına tabidir.",
    ["Form azami iki sayfa ve 12 punto olarak hazırlanır.",
     "Formda fonun toplam gider oranına yer verilir.",
     "Formun içeriğinin doğruluğundan ve güncelliğinden kurucu sorumludur.",
     "Formda fonun risk ve getiri profili yer alır."],
    "Tebliğ m. 12'ye göre form azami iki sayfa ve 12 punto hazırlanır; gider oranı ile risk ve getiri profilini içerir ve "
    "doğruluğundan kurucu sorumludur. m. 13/3'e göre formdaki değişiklikler Kurul onayına tabi değildir; altı iş günü önce "
    "Kurula bildirilir ve değişikliği takip eden iş günü KAP'ta ilan edilir.")

# ================================================================ Tebliğ: katılma payı değeri ve alım satımı (m. 14-15)
P.sayisal("III-52.1 m. 14/2",
    "Bir yatırım fonunun toplam değeri 24.000.000 TL, tedavüldeki katılma payı sayısı 8.000.000 adettir. "
    f"{T}, bu fonun birim pay değeri kaç TL’dir?",
    "3,00", ["0,33", "1,50", "3,33", "8,00"],
    "Tebliğ m. 14/2'ye göre fon birim pay değeri, fon toplam değerinin katılma paylarının sayısına bölünmesiyle bulunur: "
    "24.000.000 / 8.000.000 = 3,00 TL. Katılma paylarının itibari değeri yoktur ve birim pay değeri alım satıma esas fiyattır.",
    zorluk="easy")

P.q("III-52.1 m. 14/5",
    "Bir yatırımcı hisse senedi fonundan katılma payı almak için emir vermiştir. "
    f"{T}, bu emir hangi fiyat üzerinden yerine getirilir?",
    "Emrin verilmesini takip eden ilk hesaplamada bulunacak pay fiyatı",
    ["Emrin verildiği anda en son ilan edilmiş olan pay fiyatı",
     "Emrin verildiği günün açılış fiyatı ile kapanış fiyatının ortalaması",
     "Emrin verildiği haftanın ortalama birim pay değeri",
     "Kurucunun belirlediği sabit alım fiyatı"],
    "Tebliğ m. 14/5'e göre para piyasası ve kısa vadeli borçlanma araçları fonları dışındaki fonlarda alım satım emirleri, "
    "emrin verilmesini takip eden ilk hesaplamada bulunacak pay fiyatı üzerinden yerine getirilir. Para piyasası ve kısa "
    "vadeli borçlanma araçları fonlarında en son ilan edilen fiyat esas alınır.")

P.q("III-52.1 m. 14-15",
    f"{T}, katılma paylarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Katılma paylarının itibari değeri iç tüzükte belirlenir.",
    ["Fonların birim pay değerinin günlük olarak hesaplanması ve ilan edilmesi esastır.",
     "Katılma payı sahiplerine temettü dağıtılması mümkündür.",
     "Katılma payı alımında birim pay değerinin tam olarak nakden ödenmesi gerekir.",
     "İzahnamede hüküm bulunması ve borsanın uygun görmesiyle katılma payları borsada işlem görebilir."],
    "Tebliğ m. 14'e göre katılma paylarının itibari değeri yoktur; birim pay değeri günlük hesaplanıp ilan edilir ve temettü "
    "dağıtılabilir. m. 15'e göre alımda birim pay değeri tam ve nakden ödenir; izahnamede hüküm ve borsanın uygun görmesiyle "
    "paylar borsada işlem görebilir.")

P.q("III-52.1 m. 15/1",
    "Fon toplam değerinin %85’i oranında altına yatırım yapan bir fonun yatırımcısı, katılma payı alımında nakit yerine "
    f"fiziki altın teslim etmek istemektedir. {T}, bu talebe ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kurulun onayı alınmak kaydıyla katılma payı alım satımında altın kullanılabilir.",
    ["Katılma payı alımında nakit dışında bir değer kullanılması mümkün değildir.",
     "Kurucunun yönetim kurulu kararı ile altın kabul edilebilir, Kurul onayı aranmaz.",
     "Altın ancak fonun tasfiyesinde yatırımcıya iade edilebilir, alımda kullanılamaz.",
     "Altın, fon toplam değerinin en az yarısı altın olan her fonda kullanılabilir."],
    "Tebliğ m. 15/1'e göre katılma payı alımında birim pay değerinin tam olarak nakden ödenmesi esastır; ancak fon toplam "
    "değerinin en az %80'i oranında altına yatırım yapan fonlarda Kurulun onayı alınmak kaydıyla alım satımda altın da "
    "kullanılabilir.")

# ================================================================ Tebliğ: portföy sınırlamaları (m. 17-24)
P.sayisal("III-52.1 m. 17/1-a",
    "Toplam değeri 200 milyon TL olan bir borçlanma araçları fonu, özel sektör borçlanma araçlarına yatırım yapmaktadır. "
    f"{T}, bu fon ipotek ve varlık teminatlı olmayan araçlar için tek bir ihraççının araçlarına en fazla kaç milyon TL "
    "yatırabilir?",
    "20", ["10", "40", "50", "70"],
    "Tebliğ m. 17/1-a'ya göre fon toplam değerinin %10'undan fazlası bir ihraççının para ve sermaye piyasası araçlarına ve "
    "bunlara dayalı türev araçlara yatırılamaz: 200 × %10 = 20 milyon TL. İpotek ve varlık teminatlı menkul kıymetlerde oran %25'tir.")

P.q("III-52.1 m. 17/1-b",
    "Bir hisse senedi fonunun portföy dağılımı aşağıdaki seçeneklerde verilmiştir. "
    f"{T}, hangi portföy tek ihraççıya ilişkin sınırlamalara aykırıdır?",
    "Beş ihraççının her birine fon toplam değerinin %9’u yatırılmıştır.",
    ["Bir ihraççıya %10, üç ihraççının her birine %8 yatırılmıştır.",
     "Dört ihraççının her birine %9, kalan ihraççıların her birine %4 yatırılmıştır.",
     "On ihraççının her birine fon toplam değerinin %4’ü yatırılmıştır.",
     "İki ihraççının her birine %10, dört ihraççının her birine %5 yatırılmıştır."],
    "Tebliğ m. 17/1'e göre tek ihraççıya %10'dan fazla yatırılamaz ve %5'ten fazla yatırım yapılan ihraççıların toplamı %40'ı "
    "aşamaz. Beş ihraççıda %9 × 5 = %45 olduğundan sınır aşılır. %10 + 3 × %8 = %34, 4 × %9 = %36, 2 × %10 = %20 sınır "
    "içindedir; %5 tam oranı %5'ten fazla sayılmaz.", zorluk="hard")

P.q("III-52.1 m. 17/2",
    "Aynı kurucuya ait ve aynı yöneticinin yönettiği üç fon, Borsa İstanbul’da işlem gören bir ortaklığın paylarına yatırım "
    f"yapmaktadır. {T}, bu fonların söz konusu ortaklığın sermayesinde sahip olabileceği paylara ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Her fon tek başına %10’dan, fonlar toplu olarak %20’den fazlasına sahip olamaz.",
    ["Her fon tek başına %5’ten, fonlar toplu olarak %10’dan fazlasına sahip olamaz.",
     "Fonlar toplu olarak sermayenin %40’ını aşmadıkça sınırlama uygulanmaz.",
     "Her fon tek başına %20’den, fonlar toplu olarak %40’tan fazlasına sahip olamaz.",
     "Sınırlama oy haklarına değil sadece sermaye payına uygulanır."],
    "Tebliğ m. 17/2'ye göre fon tek başına hiçbir ihraççının sermayesinin veya tüm oy haklarının %10'undan fazlasına, aynı "
    "yöneticinin yönetimindeki tek bir kurucuya ait fonlar ise toplu olarak %20'sinden fazlasına sahip olamaz.", zorluk="hard")

P.oncul("III-52.1 m. 17/4-5, 18",
    "Toplam değeri 100 milyon TL olan bir borçlanma araçları fonunun portföyüne ilişkin aşağıdaki durumlar verilmiştir:",
    ["Tek bir bankadaki vadeli mevduata 5 milyon TL yatırılmıştır.",
     "Tek bir ihraççının varantlarına 4 milyon TL yatırılmıştır.",
     "Başka bir yatırım fonunun katılma paylarına 8 milyon TL yatırılmıştır.",
     "Farklı bankalardaki vadeli mevduatların toplamı 12 milyon TL’dir."],
    f"{T}, yukarıdakilerden hangileri portföy sınırlamalarına aykırıdır?",
    "I ve IV", ["Yalnız I", "I ve IV", "II ve III", "I, II ve IV", "II, III ve IV"],
    "Tebliğ m. 17/5'e göre mevduat ve katılma hesapları fon toplam değerinin en fazla %10'u, tek bankada %3'ü olabilir: 5 "
    "milyon (%5) ve 12 milyon (%12) aykırıdır. m. 17/4'e göre tek ihraççının varantları %5'i aşamaz (%4 uygun); m. 18'e göre "
    "tek bir fonun katılma paylarına %10'a kadar yatırım yapılabilir (%8 uygun).", zorluk="hard")

P.q("III-52.1 m. 17/5",
    f"{T}, katılım fonları dışındaki fonların mevduat ve katılma hesaplarına ilişkin sınırlamalarında aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Mevduat vadesi fonun vadesini aşmamak kaydıyla on iki aydan uzun olabilir.",
    ["Fon toplam değerinin en fazla %10’u mevduat ve katılma hesaplarında değerlendirilebilir.",
     "Tek bir bankada değerlendirilecek tutar fon toplam değerinin %3’ünü aşamaz.",
     "Katılım fonlarında bu oranlar sırasıyla %25 ve %10 olarak uygulanır.",
     "Mevduat sertifikaları da bu sınırlamanın hesabına dâhil edilir."],
    "Tebliğ m. 17/5'e göre fon toplam değerinin en fazla %10'u, 12 aydan uzun vadeli olmamak şartıyla mevduat, katılma "
    "hesabı ve mevduat sertifikalarında değerlendirilebilir; tek bankada %3'ü aşamaz. Katılım fonlarında oranlar %25 ve %10'dur.")

P.q("III-52.1 m. 20",
    "Bir borçlanma araçları fonunun portföyünün aylık ağırlıklı ortalama vadesi 400 gündür. "
    f"{T}, fon unvanında vade yapısına yer verilmek istenirse hangi ifade kullanılır?",
    "Orta vadeli",
    ["Kısa vadeli", "Uzun vadeli", "Değişken vadeli", "Vadesiz"],
    "Tebliğ m. 20/1'e göre aylık ağırlıklı ortalama vade 25-90 gün ise “kısa vadeli”, 91-730 gün ise “orta vadeli”, 730 "
    "günden fazla ise “uzun vadeli” ifadesi unvanda yer alır; 400 gün orta vadeli aralıktadır.", zorluk="easy")

P.q("III-52.1 m. 22",
    f"{T}, fon portföyündeki sermaye piyasası araçlarının ödünç verilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fonlar portföylerindeki araçların piyasa değerinin tamamını ödünç verebilir.",
    ["Ödünç verme, Kurul düzenlemeleri çerçevesinde yapılacak bir sözleşmeyle gerçekleştirilir.",
     "Ödünç verilen araçların en az %100’ü karşılığında teminat Takasbank’ta bloke edilir.",
     "Ödünç verme sözleşmesine fon lehine tek taraflı fesih hükmü konulması zorunludur.",
     "Kıymetli madenlerin ödünç verilmesinde sınır piyasa değerinin %75’idir."],
    "Tebliğ m. 22'ye göre fonlar herhangi bir anda portföylerindeki araçların piyasa değerinin en fazla %50'si tutarında "
    "ödünç verebilir; ödünç verilenlerin en az %100'ü karşılığında teminat Takasbank'ta bloke edilir, sözleşmede fon lehine "
    "tek taraflı fesih hükmü bulunur. Kıymetli madenlerde oran %75'tir.", zorluk="hard")

P.oncul("III-52.1 m. 21, 24",
    "Serbest fon olmayan bir değişken fonun işlemlerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Fon açığa satış ve kredili menkul kıymet işlemi yapamaz.",
     "Türev araçlar nedeniyle maruz kalınan açık pozisyon tutarı fon toplam değerini aşamaz.",
     "Borsa dışında taraf olunan ters repo sözleşmelerine fon toplam değerinin %25’ine kadar yatırım yapılabilir.",
     "Takasbank para piyasası ve organize para piyasası işlemleri fon toplam değerinin %20’sini aşamaz."],
    f"{T}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV", ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "I, III ve IV"],
    "Tebliğ m. 24/4'e göre fon açığa satış ve kredili işlem yapamaz; m. 24/1-b'ye göre türev araçlardan doğan açık pozisyon "
    "fon toplam değerini aşamaz; m. 24/3'e göre Takasbank ve organize para piyasası işlemleri %20 ile sınırlıdır. m. 21/2'ye "
    "göre borsa dışı ters repoya en fazla %10 yatırım yapılabilir.", zorluk="hard")

P.q("III-52.1 m. 23/2",
    f"Unvanında “Endeks” ibaresi bulunan bir fonun yöneticisi performansı izlemektedir. {T}, bu fona ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Endeks ile birim pay değeri arasındaki korelasyon en az %90 olmalıdır.",
    ["Fonun getirisi endeksin getirisini en az %10 aşmalıdır.",
     "Korelasyon katsayısı en az %50 olduğunda fon yükümlülüğünü yerine getirmiş olur.",
     "Endeks fonları endekste yer alan payların tamamını eşit ağırlıkla portföyde bulundurur.",
     "Endeks fonlarına tek ihraççı ve grup sınırlamaları endeks dışı paylar için de uygulanmaz."],
    "Tebliğ m. 23/2'ye göre endeks fonlarında yönetici fonu, getirisi baz alınan endeksin getirisinden önemli ölçüde "
    "sapmayacak şekilde yönetir ve endeks değeri ile birim pay değeri arasındaki korelasyon katsayısı en az %90 olmalıdır. "
    "m. 23/3'teki sınırlama istisnaları yalnız endekse dahil varlıklar içindir.")

P.q("III-52.1 m. 23/4",
    "Bir fon, yalnız enerji sektöründe faaliyet gösteren ihraççıların paylarına yatırım yapmak üzere kurulmuştur. "
    f"{T}, bu fona ilişkin tek ihraççı sınırlaması nasıl uygulanır?",
    "Sektördeki ihraççılar için tek ihraççı sınırı %20 olarak uygulanır.",
    ["Tek ihraççı sınırı sektör fonlarında da %10 olarak uygulanır.",
     "Sektör fonlarında tek ihraççı sınırı uygulanmaz.",
     "Tek ihraççı sınırı %35 olarak uygulanır.",
     "Tek ihraççı sınırı Kurul tarafından fon bazında ayrıca belirlenir."],
    "Tebliğ m. 23/4'e göre belirli bir sektördeki ihraççılara yatırım yapan fonlarda m. 17/1-a'daki %10'luk sınırlama o "
    "sektörde faaliyet gösteren ihraççılar için %20 olarak uygulanır; (b) ve (c) bentlerindeki sınırlamalar uygulanmaz.")

# ================================================================ Tebliğ: serbest fon, fon sepeti, garantili (m. 25-27)
P.q("III-52.1 m. 25",
    f"{T}, serbest fonlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Serbest fonlar Tebliğdeki tek ihraççı ve grup sınırlamalarına tabidir.",
    ["Serbest fonlar KAP sayfasında yer alan yatırım stratejileri ve limitleri dahilinde yatırım yapar.",
     "Portföye alınacak yabancı fonlar için ilgili otoriteden izin alınmış olması şartı aranır.",
     "Satış yapan kuruluşlar yatırımcıların nitelikli yatırımcı olduğuna dair belgeleri temin eder.",
     "Satışlar yeterli bilgi ve deneyime sahip satış personeli tarafından gerçekleştirilir."],
    "Tebliğ m. 25'e (2024) göre serbest fonlar m. 17-24'teki portföy ve işlem sınırlamalarına tabi olmaksızın KAP sayfasındaki "
    "strateji ve limitler dahilinde yatırım yapar; yabancı fon payları için izin şartı aranır ve satış yapan kuruluşlar "
    "nitelikli yatırımcı belgelerini temin eder.")

P.q("III-52.1 m. 26",
    f"{T}, fon sepeti fonlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fon sepeti fonları diğer fon sepeti fonlarının katılma paylarına yatırım yapabilir.",
    ["Tek bir fona ait katılma paylarının değeri fon sepeti fonu toplam değerinin %20’sini aşamaz.",
     "Portföye alınan katılma payı sayısı, yatırım yapılan fonun pay sayısının %25’ini aşamaz.",
     "Serbest fonlara ait katılma paylarının değeri fon toplam değerinin %10’unu geçemez.",
     "Yatırım yapılan fonların yönetim ücretleri toplam gider oranının hesabında dikkate alınır."],
    "Tebliğ m. 26'ya göre fon sepeti fonlarında tek fona yatırım %20'yi, yatırılan fonun pay sayısının %25'ini, serbest fon "
    "payları %10'u aşamaz ve ödenen ücretler toplam gider oranına dahil edilir. Fon sepeti fonları diğer fon sepeti fonlarına "
    "yatırım yapamaz.", zorluk="hard")

P.sayisal("III-52.1 m. 27/1",
    f"{T}, garantili ve koruma amaçlı şemsiye fonlara bağlı fonların vadesi asgari kaç ay olarak belirlenmelidir?",
    "6", ["1", "3", "12", "24"],
    "Tebliğ m. 27/1'e göre garantili ve koruma amaçlı şemsiye fona bağlı fonların vadelerinin asgari altı ay olarak "
    "belirlenmesi zorunludur; fonun vadesi içinde yönetim stratejisinde ve türünde değişiklik yapılamaz.")

# ================================================================ Tebliğ: yönetim, sona erme, devir, birleşme (m. 5, 28-30)
P.sayisal("III-52.1 m. 5/2",
    f"{T}, fon malvarlığını yönetecek portföy yöneticilerinin sermaye piyasası alanında en az kaç yıllık tecrübeye sahip "
    "olması gerekir?",
    "5", ["1", "2", "3", "10"],
    "Tebliğ m. 5/2'ye göre fon malvarlığı, fonun yatırım yapabileceği varlıklar konusunda yeterli bilgi ve sermaye piyasası "
    "alanında en az beş yıllık tecrübeye sahip portföy yöneticileri tarafından yatırımcı lehine yönetilir.", zorluk="easy")

P.q("III-52.1 m. 28",
    "Süresiz olarak kurulmuş bir yatırım fonunun kurucusu fonu sona erdirmek istemektedir. "
    f"{T}, bu sürece ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fesih ihbarından sonra da tasfiye başlayana kadar yeni katılma payı ihraç edilebilir.",
    ["Kurucu, Kurulun uygun görüşünü aldıktan sonra altı ay sonrası için feshi ihbar eder.",
     "Tasfiye bakiyesi katılma payı sahiplerine payları oranında dağıtılır.",
     "Tasfiye anından itibaren katılma payı ihraç edilemez ve geri alınamaz.",
     "Süre sonunda iade edilmemiş paylar satış talimatı beklenmeden satılarak yatırımcılar adına nemalandırılır."],
    "Tebliğ m. 28'e göre süresiz fon, kurucunun Kurulun uygun görüşünü aldıktan sonra altı ay sonrası için feshi ihbarıyla "
    "sona erer; fesih ihbarından sonra yeni katılma payı ihraç edilemez, tasfiye anından itibaren pay ihraç ve geri alımı "
    "durur. Tasfiye bakiyesi pay oranında dağıtılır; iade edilmemiş paylar satılarak nemalandırılır.")

P.q("III-52.1 m. 29",
    f"{T}, fonun ve şemsiye fonun devrine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Devir nedeniyle yapılan masraflar fon portföyünden karşılanır.",
    ["Kurucunun iflası hâlinde Kurul fonu başka bir portföy yönetim şirketine tasfiye amacıyla devreder.",
     "Saklayıcının mali durumu zayıflarsa kurucu fon varlığını Kurulca uygun görülen başka saklayıcıya devreder.",
     "İflas ve tasfiye dışında fonun başka kurucuya devri Kurulun uygun görüşüyle mümkündür.",
     "Kurucu değişikliğinden önceki yükümlülüklerden her iki kurucu müteselsilen sorumludur."],
    "Tebliğ m. 29'a göre kurucunun iflasında Kurul fonu başka bir portföy yönetim şirketine tasfiye amacıyla devreder; "
    "saklayıcının zayıflamasında kurucu varlıkları başka saklayıcıya devreder; diğer devirler Kurul uygun görüşüne bağlıdır. "
    "Masraflar fona yansıtılamaz ve önceki yükümlülüklerden her iki kurucu müteselsilen sorumludur.")

P.q("III-52.1 m. 30",
    "İki yatırım fonunun birleştirilmesi için Kurulun izni alınmış ve duyuru metni hazırlanmıştır. "
    f"{T}, bu birleşmeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yürürlük tarihi, duyurunun yayımından itibaren otuz günden az olamaz.",
    ["Birleşme, duyuru metninin KAP’ta yayımlandığı gün yürürlüğe girer.",
     "Değiştirme oranı, sona erecek fonun birim pay değeri devralan fonunkine bölünerek bulunur.",
     "Sona eren fonun varlıkları birleşme tarihinden sonra altı ay içinde devredilir.",
     "Duyuru metni Kurul izninden itibaren otuz iş günü içinde ilan edilir."],
    "Tebliğ m. 30'a göre birleşme ve dönüşüme ilişkin onaylı duyuru metni izin yazısını takip eden altı iş günü içinde "
    "KAP'ta ilan edilir ve yürürlük tarihi yayımdan itibaren 30 günden az olamaz. Değiştirme oranı, bünyesinde birleşilecek "
    "fonun birim pay değerinin sona erecek fonunkine bölünmesiyle bulunur; varlıklar birleşme tarihinde devredilir.",
    zorluk="hard")

P.q("III-52.1 m. 11/8",
    "Bir koruma amaçlı fonun katılma payları için talep toplanmış ve talep toplama süresi sona ermiştir. "
    f"{T}, toplanan paranın izahnamede belirlenen varlıklara yatırılma süresi aşağıdakilerden hangisidir?",
    "Talep toplamanın sona erdiği günden itibaren iki iş günü",
    ["Talep toplamanın sona erdiği günü takip eden iş günü",
     "Talep toplamanın sona erdiği günden itibaren beş iş günü",
     "Talep toplamanın sona erdiği günden itibaren on iş günü",
     "Fonun vadesinin başladığı ilk ayın sonuna kadar"],
    "Tebliğ m. 11/8'e göre katılma payları karşılığı toplanan para takip eden iş günü izahnamedeki varlıklara yatırılır; "
    "garantili ve koruma amaçlı fonlarda talep toplanması hâlinde bu süre iki iş günüdür ve talep toplamanın sona erdiği gün "
    "esas alınır.")

P.q("6362 s. SPKn m. 52/6",
    "Bir portföy yönetim şirketi, yabancı para ve sermaye piyasası araçlarına yatırım yapan bir fonun katılma paylarının "
    f"Türk lirası yerine ABD doları üzerinden alınıp satılmasını istemektedir. {K}, bu talebe ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Kurul, TCMB ve Hazinenin görüşünü alarak TCMB’nin kur ilan ettiği yabancı para üzerinden alım satıma izin verebilir.",
    ["Katılma paylarının alım satımı Türk lirası dışında bir para birimiyle yapılamaz.",
     "Kurucu, fon iç tüzüğünde hüküm bulunmak kaydıyla Kurul izni aranmaksızın döviz üzerinden işlem yapabilir.",
     "Döviz üzerinden alım satıma BDDK izin verir.",
     "Döviz üzerinden alım satım sadece nitelikli yatırımcılara yapılabilir."],
    "Kanun m. 52/6'ya göre Kurul, TCMB ve Hazine Müsteşarlığının (bugün Hazine ve Maliye Bakanlığı) görüşünü alarak fon "
    "katılma paylarının alım satımının TCMB tarafından günlük alım satım kurları ilan edilen yabancı para birimleri üzerinden "
    "yapılmasına izin verebilir; Tebliğ m. 15/8 bu imkânı Kurul onayına bağlar.", zorluk="hard")

P.q("III-52.1 m. 33",
    f"Bir fonun izahnamesinde azami yıllık fon toplam gider oranı belirlenmiştir. {T}, bu oranın aşılıp aşılmadığının "
    "kontrolüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "3, 6, 9 ve 12 aylık dönemlerin son iş günü itibarıyla kontrol edilir.",
    ["Her ayın son iş günü itibarıyla kontrol edilir.",
     "Sadece hesap dönemi sonunda bağımsız denetçi tarafından kontrol edilir.",
     "Her işlem günü sonunda portföy saklayıcısı tarafından kontrol edilir.",
     "Kurulun talep ettiği tarihlerde kontrol edilir; dönemsel kontrol yapılmaz."],
    "Tebliğ m. 33/1'e göre fondan karşılanan tüm giderlerin toplamı Ek-4'teki azami oranları aşamaz; 3, 6, 9 ve 12 aylık "
    "dönemlerin son iş günü itibarıyla oranın aşılıp aşılmadığı kontrol edilir ve aşım kurucu tarafından iade edilir. Sonuçlar "
    "dönem bitimini izleyen altı iş günü içinde KAP'ta ilan edilir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
