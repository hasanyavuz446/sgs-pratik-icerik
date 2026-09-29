# -*- coding: utf-8 -*-
"""Hukuk · Sosyal Güvenlik Mevzuatı · Primler ve Sigorta Kolları — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında 5510 sayılı Kanunun sigorta kolları ve prim hükümleri "kısa ve uzun vadeli
sigorta kollarından biri değildir", "… sigortasından sağlanan haklardan biri değildir" ve süre-oran soran kalıplarla
gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 5510 sayılı Kanun md. 15-19, 21, 25-26, 28, 32, 37, 80-82,
86, 88-89. 7566 sayılı Kanunla (4.12.2025) malullük, yaşlılık ve ölüm primi %21'e (işveren %12) çıkarılmış; 7577 sayılı
Kanunla (2.4.2026) prime esas kazanç istisnaları yeniden düzenlenmiş; 7578 sayılı Kanunla (22.4.2026) analık süreleri
değişmiştir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_primler_ve_sigorta_kollari_2026.json", lesson="sosyal_guvenlik_mevzuati",
          topic="primler_ve_sigorta_kollari", konu_adi="Primler ve Sigorta Kolları", seed=2026093006,
          surum="5510 sayılı Kanun güncel metni (7566, 7577, 7578 s. Kanun değişiklikleri dahil); 29.09.2026 kontrolü")

K = "5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu’na göre"
K26 = ("5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu’nun 2026 yılında yürürlükte olan hükümlerine "
       "göre")

P.sayisal("SGK md. 81",
    f"{K26}, malullük, yaşlılık ve ölüm sigortaları prim oranı sigortalının prime esas kazancının yüzde kaçıdır?",
    "21", ["9", "12", "20", "22"],
    "Md. 81/a'ya göre (7566 sayılı Kanunla değişik) malullük, yaşlılık ve ölüm sigortaları prim oranı prime esas kazancın "
    "%21'idir; bunun %9'u sigortalı, %12'si işveren hissesidir.", zorluk="hard")

P.q("SGK md. 3",
    f"{K}, aşağıdakilerden hangisi kısa vadeli sigorta kollarından biri değildir?",
    "Yaşlılık sigortası",
    ["İş kazası sigortası", "Meslek hastalığı sigortası", "Hastalık sigortası", "Analık sigortası"],
    "Md. 3'e göre kısa vadeli sigorta kolları iş kazası ve meslek hastalığı, hastalık ve analık sigortasıdır; yaşlılık "
    "sigortası uzun vadelidir.", zorluk="easy")

P.q("SGK md. 3",
    f"{K}, aşağıdakilerden hangisi uzun vadeli sigorta kollarından biridir?",
    "Ölüm sigortası",
    ["Analık sigortası", "Hastalık sigortası", "İş kazası sigortası", "Genel sağlık sigortası"],
    "Md. 3'e göre uzun vadeli sigorta kolları malullük, yaşlılık ve ölüm sigortasıdır.", zorluk="easy")

P.sayisal("SGK md. 81",
    f"{K26}, malullük, yaşlılık ve ölüm sigortaları priminin işveren hissesi prime esas kazancın yüzde kaçıdır?",
    "12", ["5", "7", "9", "11"],
    "Md. 81/a'ya göre 2025 değişikliğiyle işveren hissesi %11'den %12'ye çıkarılmıştır; sigortalı hissesi %9'dur.",
    zorluk="hard")

P.q("SGK md. 16",
    f"{K}, aşağıdakilerden hangisi iş kazası ve meslek hastalığı sigortasından sağlanan haklardan biri değildir?",
    "Emzirme ödeneği",
    ["Geçici iş göremezlik ödeneği", "Sürekli iş göremezlik geliri", "Hak sahiplerine gelir", "Cenaze ödeneği"],
    "Md. 16'ya göre iş kazası ve meslek hastalığı sigortasından geçici iş göremezlik ödeneği, sürekli iş göremezlik geliri, "
    "hak sahiplerine gelir, kız çocuklarına evlenme ödeneği ve cenaze ödeneği sağlanır; emzirme ödeneği analık sigortasından "
    "verilir.")

P.q("SGK md. 16",
    f"{K}, emzirme ödeneğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ödenek, çocuğun yaşaması şartı aranmadan verilir.",
    ["Analık sigortasından sağlanan bir haktır.",
     "Sigortalı olmayan eşi doğuran erkeğe de verilir.",
     "4/a’da doğumdan önceki yılda 120 gün prim aranır.",
     "Tutarı Kurum tarifesiyle belirlenir."],
    "Md. 16'ya göre emzirme ödeneği her çocuk için yaşaması şartıyla, Kurum Yönetim Kurulunca belirlenen tarife üzerinden "
    "verilir.")

P.sayisal("SGK md. 81",
    f"{K26}, genel sağlık sigortası primi kısa ve uzun vadeli sigorta kollarına tabi olanlar için prime esas kazancın "
    "yüzde kaçıdır?",
    "12,5", ["5", "7,5", "12", "15"],
    "Md. 81/f'ye göre genel sağlık sigortası primi kısa ve uzun vadeli sigorta kollarına tabi olanlar için prime esas kazancın "
    "%12,5'idir; %5'i sigortalı, %7,5'i işveren hissesidir.")

P.q("SGK md. 15",
    f"{K26}, analık hâlinin kapsamına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Doğumdan sonraki ilk on altı haftaya kadar",
    ["Sadece doğum günüyle sınırlıdır.",
     "Doğumdan sonraki ilk sekiz haftayla sınırlıdır.",
     "Sigortalı olmayan eşi kapsamaz.",
     "Doğumdan önceki bir yıllık süreyi de kapsar."],
    "Md. 15'e göre (7578 sayılı Kanunla 2026'da değişik) gebeliğin başladığı tarihten itibaren doğumdan sonraki ilk on altı "
    "haftalık süreye kadar olan gebelik ve analıkla ilgili rahatsızlık ve engellilik hâlleri analık hâlidir.", zorluk="hard")

P.q("SGK md. 18",
    f"{K}, geçici iş göremezlik ödeneğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birden çok hâlde ödenekler toplanır.",
    ["Yatarak tedavide günlük kazancın yarısıdır.",
     "Ayaktan tedavide günlük kazancın üçte ikisidir.",
     "İş kazasında ilk günden itibaren verilir.",
     "İşverence ödenip sonra Kurumla mahsuplaşılabilir."],
    "Md. 18'e göre bir sigortalıda iş kazası, meslek hastalığı, hastalık ve analık hâllerinden birkaçı birleşirse geçici iş "
    "göremezlik ödeneklerinden en yükseği verilir.")

pr = 50_000 * 0.0225
P.sayisal("SGK md. 81",
    "4/a kapsamındaki bir sigortalının 2026 yılı Mart ayına ait prime esas kazancı 50.000 ₺’dir; kısa vadeli sigorta kolları "
    f"prim oranında Cumhurbaşkanınca değişiklik yapılmamıştır.\n\n{K26}, bu ay için ödenecek kısa vadeli sigorta kolları "
    "primi kaç ₺’dir?",
    tl(pr), secenekler(pr, 1_000, 1_250, 562.5, 4_500),
    "Md. 81/c'ye göre kısa vadeli sigorta kolları prim oranı prime esas kazancın %2,25'idir ve tamamını işveren öder: "
    "50.000 × %2,25 = 1.125 ₺.", zorluk="hard")

P.q("SGK md. 18",
    f"{K}, 4/b kapsamındaki sigortalılara geçici iş göremezlik ödeneği ödenmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Prim borçlarının ödenmiş olması şarttır.",
    ["Prim borcu olsa da ödenek verilir.",
     "Ayaktan tedavide de her gün için ödenir.",
     "Hastalık hâlinde ilk günden ödenir.",
     "4/b sigortalısına ödenek verilmez."],
    "Md. 18'e göre 4/b sigortalılarına iş kazası, meslek hastalığı veya analık hâlinde ödenek, genel sağlık sigortası dahil "
    "prim borçlarının ödenmiş olması şartıyla yatarak tedavi süresince veya sonrasındaki istirahat süresinde ödenir.",
    zorluk="hard")

P.q("SGK md. 21",
    f"{K}, iş kazasının işverenin kastı veya iş güvenliği mevzuatına aykırı hareketi sonucu meydana gelmesi hâlinde "
    "aşağıdakilerden hangisi doğrudur?",
    "Ödemeler işverene ödettirilir.",
    ["Sigortalıya herhangi bir ödeme yapılmaz.",
     "Ödemelerin tamamı sigortalıdan geri alınır.",
     "İşverenin kusuru dikkate alınmaz.",
     "Ödemeler Hazine tarafından karşılanır."],
    "Md. 21'e göre iş kazası ve meslek hastalığı işverenin kastı veya iş sağlığı ve güvenliği mevzuatına aykırı hareketi sonucu "
    "meydana gelmişse Kurumca yapılan ödemeler ve bağlanan gelirin ilk peşin sermaye değeri işverene ödettirilir.")

sg = 40_000 * 0.09
P.sayisal("SGK md. 81",
    "4/a kapsamındaki bir sigortalının 2026 yılı Nisan ayına ait prime esas kazancı 40.000 ₺’dir."
    f"\n\n{K26}, bu kazanç üzerinden hesaplanacak malullük, yaşlılık ve ölüm sigortaları priminin sigortalı hissesi kaç "
    "₺’dir?",
    tl(sg), secenekler(sg, 4_800, 8_400, 2_000, 4_400),
    "Md. 81/a'ya göre malullük, yaşlılık ve ölüm sigortaları priminin %9'u sigortalı hissesidir: 40.000 × %9 = 3.600 ₺.",
    zorluk="hard")

P.q("SGK md. 21",
    "İşveren, sigortalının geçirdiği iş kazasını üç iş günlük süre içinde Kuruma bildirmemiş, iki hafta sonra bildirmiştir."
    f"\n\n{K}, bildirim tarihine kadar geçen süre için sigortalıya ödenecek geçici iş göremezlik ödeneği hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Kurumca işverenden tahsil edilir.",
    ["Sigortalıya o süre için ödenmez.",
     "Sigortalının ücretinden kesilir.",
     "Yarısı işverenden tahsil edilir.",
     "İşverene idari para cezası olarak yazılır."],
    "Md. 21'e göre iş kazası süresinde Kuruma bildirilmezse bildirim tarihine kadar geçen süre için sigortalıya ödenecek geçici "
    "iş göremezlik ödeneği Kurumca işverenden tahsil edilir.", zorluk="hard")

P.q("SGK md. 21",
    f"{K}, iş kazasının üçüncü bir kişinin kusuru nedeniyle meydana gelmesi hâlinde Kurumun rücu hakkına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Ödemelerin yarısı üçüncü kişiye ödettirilir.",
    ["Ödemelerin tamamı sigortalıya ödettirilir.",
     "Kurum üçüncü kişiye rücu edemez.",
     "Ödemelerin dörtte biri işverene ödettirilir.",
     "Ödemelerin tamamı işverene ödettirilir."],
    "Md. 21'e göre iş kazası, meslek hastalığı ve hastalık üçüncü bir kişinin kusuru nedeniyle meydana gelmişse Kurumca yapılan "
    "ödemeler ve bağlanan gelirin ilk peşin sermaye değerinin yarısı zarara sebep olan üçüncü kişilere ödettirilir.",
    zorluk="hard")

P.sayisal("SGK md. 81",
    f"{K26}, 3308 sayılı Kanuna tabi aday çırak ve çıraklar için prim oranı prime esas kazançlarının yüzde kaçıdır?",
    "6", ["1", "2", "5", "12,5"],
    "Md. 81/d'ye göre md. 5/b kapsamındakiler için prim oranı prime esas kazancın %6'sıdır; bunun %1'i kısa vadeli sigorta "
    "kolları, %5'i genel sağlık sigortası primidir.", zorluk="hard")

P.q("SGK md. 25",
    f"{K26}, malullüğe ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşe girişten önceki malullükle de malullük aylığı alınır.",
    ["Malullüğü Kurum Sağlık Kurulu tespit eder.",
     "4/a ve 4/b’de çalışma gücünün %60 kaybı aranır.",
     "Talep sigortalı veya işveren tarafından yapılabilir.",
     "Askerlikte oluşan ve işe engel olmayan malullükte uygulanmaz."],
    "Md. 25'e göre sigortalı olarak ilk defa çalışmaya başlamadan önce çalışma gücünün %60'ını kaybettiği tespit edilen "
    "sigortalı, bu hastalık veya engellilik sebebiyle malullük aylığından yararlanamaz.")

P.q("SGK md. 26",
    f"{K}, malullük aylığı bağlanmasının şartları arasında aşağıdakilerden hangisi yer almaz?",
    "Sigortalının 50 yaşını doldurmuş olması",
    ["Sigortalının malul sayılması",
     "En az 1800 gün prim bildirilmiş olması",
     "Kurumdan yazılı istekte bulunulması",
     "4/b’lilerde prim borcunun bulunmaması"],
    "Md. 26'ya göre malullük aylığı için malul sayılma, en az on yıl sigortalılık ve 1800 gün prim, işten ayrılma ile yazılı "
    "istek ve 4/b sigortalıları için prim borcunun bulunmaması gerekir; yaş şartı yoktur.")

P.sayisal("SGK md. 82",
    f"{K26}, prime esas günlük kazancın üst sınırı, 16 yaşından büyük sigortalıların günlük kazanç alt sınırının kaç "
    "katıdır?",
    "9", ["3", "5", "6,5", "7,5"],
    "Md. 82'ye göre prime esas günlük kazancın üst sınırı 16 yaşından büyük sigortalıların günlük kazanç alt sınırının 9 "
    "katıdır; sosyal güvenlik sözleşmesi olmayan ülkelere götürülen Türk işçileri için 3 katıdır.")

P.q("SGK md. 28",
    f"{K}, yaşlılık sigortasından sigortalıya sağlanan haklar aşağıdakilerden hangisinde birlikte verilmiştir?",
    "Yaşlılık aylığı ve toptan ödeme",
    ["Yaşlılık aylığı ve emzirme ödeneği",
     "Toptan ödeme ve cenaze ödeneği",
     "Geçici iş göremezlik ödeneği ve aylık",
     "Evlenme ödeneği ve yaşlılık aylığı"],
    "Md. 28'e göre yaşlılık sigortasından sağlanan haklar yaşlılık aylığı bağlanması ve toptan ödeme yapılmasıdır.")

P.q("SGK md. 28",
    f"{K}, ilk defa bu Kanuna göre sigortalı sayılanlarda yaşlılık aylığı için temel yaş şartı aşağıdakilerden "
    "hangisidir?",
    "Kadın 58, erkek 60",
    ["Kadın 55, erkek 58", "Kadın 60, erkek 62", "Kadın 50, erkek 55", "Kadın ve erkek 65"],
    "Md. 28'e göre ilk defa bu Kanuna tabi olanlara kadın ise 58, erkek ise 60 yaşını doldurmaları ve prim gün şartını "
    "sağlamaları hâlinde yaşlılık aylığı bağlanır; yaş şartı 2036'dan itibaren kademeli olarak artar.")

P.sayisal("SGK md. 18",
    f"{K}, hastalık sebebiyle iş göremezliğe uğrayan 4/a sigortalısına geçici iş göremezlik ödeneği, iş göremezliğin "
    "kaçıncı gününden başlamak üzere verilir?",
    "3", ["1", "2", "4", "5"],
    "Md. 18/b'ye göre hastalık hâlinde, iş göremezliğin başladığı tarihten önceki bir yıl içinde en az doksan gün kısa vadeli "
    "sigorta primi bildirilmişse, geçici iş göremezliğin üçüncü gününden başlamak üzere her gün için ödenek verilir.")

P.q("SGK md. 32",
    f"{K}, aşağıdakilerden hangisi ölüm sigortasından sağlanan haklardan biri değildir?",
    "Sürekli iş göremezlik geliri",
    ["Ölüm aylığı", "Ölüm toptan ödemesi", "Kız çocuklarına evlenme ödeneği", "Cenaze ödeneği"],
    "Md. 32'ye göre ölüm sigortasından ölüm aylığı, ölüm toptan ödemesi, kız çocuklarına evlenme ödeneği ve cenaze ödeneği "
    "sağlanır; sürekli iş göremezlik geliri iş kazası sigortasından verilir.", zorluk="easy")

P.q("SGK md. 37",
    f"{K}, aylığı evlenmesi nedeniyle kesilen kız çocuğuna verilecek evlenme ödeneği hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "İki yıllık tutar bir defada ödenir.",
    ["Bir yıllık aylık tutarı taksitle ödenir.",
     "Üç yıllık aylık tutarı ödenir.",
     "Ödenek her evlilikte yeniden ödenir.",
     "Sadece sigortalı olmayanlara ödenir."],
    "Md. 37'ye göre evlenmeleri nedeniyle gelir veya aylığı kesilen kız çocuklarına talepleri hâlinde almakta oldukları aylık "
    "veya gelirin iki yıllık tutarı bir defaya mahsus evlenme ödeneği olarak peşin ödenir.")

P.sayisal("SGK md. 18",
    f"{K}, hastalık hâlinde geçici iş göremezlik ödeneği için iş göremezlikten önceki bir yıl içinde en az kaç gün kısa "
    "vadeli sigorta primi bildirilmiş olmalıdır?",
    "90", ["30", "60", "120", "180"],
    "Md. 18/b'ye göre hastalık hâlinde ödenek için iş göremezliğin başladığı tarihten önceki bir yıl içinde en az doksan gün "
    "kısa vadeli sigorta primi bildirilmiş olmalıdır.")

P.q("SGK md. 80",
    f"{K26}, aşağıdakilerden hangisi 4/a sigortalısının prime esas kazancına dahil edilir?",
    "Hak edilen ücretler",
    ["Ayni yardımlar", "Kıdem tazminatı", "Görev yollukları", "Keşif ücreti"],
    "Md. 80/a'ya göre hak edilen ücretler ile prim, ikramiye ve benzeri ödemeler prime esas kazanca dahildir; ayni yardımlar, "
    "kıdem ve ihbar tazminatı, görev yollukları ve keşif ücreti prime esas kazanca tabi tutulmaz.", zorluk="easy")

P.q("SGK md. 80",
    f"{K26}, prime esas kazanca tabi tutulmayan ödemelere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İhbar tazminatı prime esas kazanca dahildir.",
    ["Doğum ve evlenme yardımları prime tabi değildir.",
     "Seyyar görev tazminatı prime tabi değildir.",
     "Kasa tazminatı prime tabi değildir.",
     "Ayni yardım yerine nakit ödeme prime tabidir."],
    "Md. 80/b'ye göre kıdem, ihbar, seyyar görev ve kasa tazminatları ile ölüm, doğum ve evlenme yardımları prime esas kazanca "
    "tabi tutulmaz; ayni yardım yerine yapılan nakdi ödemeler ise prime tabidir.")

P.sayisal("SGK md. 18",
    f"{K26}, sigortalı kadının analığı hâlinde tekil gebelikte doğumdan sonra kaç haftalık sürede çalışmadığı her gün "
    "için geçici iş göremezlik ödeneği verilir?",
    "16", ["6", "8", "10", "12"],
    "Md. 18/c'ye göre (7578 sayılı Kanunla 2026'da değişik) doğumdan önceki bir yıl içinde en az doksan gün prim bildirilmişse "
    "doğumdan önceki sekiz ve sonraki on altı haftalık sürede çalışılmayan her gün için ödenek verilir.", zorluk="hard")

P.q("SGK md. 80",
    f"{K}, ücretler ile ücret dışındaki ödemelerin prime esas kazanca mal edilmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Ücretler hak edildikleri aya mal edilir.",
    ["Ücretler ödendikleri aya mal edilir.",
     "İkramiyeler hak edildiği yıla yayılır.",
     "Tüm ödemeler yıl sonunda birlikte bildirilir.",
     "Ücret dışı ödemeler prime tabi değildir."],
    "Md. 80/d'ye göre ücretler hak edildikleri aya mal edilerek prime tabi tutulur; diğer ödemeler ise öncelikle ödendiği ayın "
    "kazancına dahil edilir.")

P.q("SGK md. 80",
    f"{K}, komisyon ücreti ve kâra katılma gibi belirsiz tutar üzerinden ücret alan sigortalının günlük kazancı nasıl "
    "belirlenir?",
    "Md. 82’deki alt sınır esas alınır.",
    ["Son üç ayın ortalaması esas alınır.",
     "Md. 82’deki üst sınır esas alınır.",
     "İşverenin beyanı esas alınır.",
     "Yıllık kazanç 360’a bölünür."],
    "Md. 80/e'ye göre belirsiz zaman ve tutar üzerinden ücret alan sigortalıların prim ve ödeneklerine esas günlük kazançları "
    "md. 82'ye göre belirlenen alt sınırdır.")

gi = 1_500 * 2 / 3 * 10
P.sayisal("SGK md. 18",
    "İş kazası geçiren sigortalı, ayaktan tedavi gördüğü 10 gün için istirahat raporu almıştır. Md. 17’ye göre hesaplanan "
    f"günlük kazancı 1.500 ₺’dir.\n\n{K}, bu süre için ödenecek geçici iş göremezlik ödeneği kaç ₺’dir?",
    tl(gi), secenekler(gi, 7_500, 15_000, 8_000, 12_000),
    "Md. 18'e göre iş kazasında her gün için ödenek verilir; ödenek yatarak tedavide günlük kazancın yarısı, ayaktan tedavide "
    "üçte ikisidir: 1.500 × 2/3 × 10 = 10.000 ₺.", zorluk="hard")

P.q("SGK md. 81",
    f"{K26}, kısa vadeli sigorta kolları primine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Primin yarısını sigortalı öder.",
    ["Oran prime esas kazancın %2,25’idir.",
     "Primin tamamını işveren öder.",
     "Cumhurbaşkanı oranı %1,5’e kadar indirebilir.",
     "Cumhurbaşkanı oranı %2,5’e kadar artırabilir."],
    "Md. 81/c'ye göre kısa vadeli sigorta kolları prim oranı %2,25'tir ve primin tamamını işveren öder; Cumhurbaşkanı oranı "
    "%1,5'e kadar indirmeye veya %2,5'e kadar artırmaya yetkilidir.", zorluk="hard")

P.q("SGK md. 81",
    f"{K26}, genel sağlık sigortası priminin hisselere dağılımı aşağıdakilerden hangisinde doğru verilmiştir?",
    "Sigortalı %5, işveren %7,5",
    ["Sigortalı %7,5, işveren %5", "Sigortalı %6, işveren %6,5", "Sigortalı %9, işveren %12",
     "Sigortalı %2,5, işveren %10"],
    "Md. 81/f'ye göre genel sağlık sigortası primi %12,5'tir; bunun %5'i sigortalı, %7,5'i işveren hissesidir.", zorluk="hard")

P.sayisal("SGK md. 19",
    f"{K}, iş kazası veya meslek hastalığı sonucu meslekte kazanma gücü en az yüzde kaç azalan sigortalı sürekli iş "
    "göremezlik gelirine hak kazanır?",
    "10", ["5", "15", "25", "60"],
    "Md. 19'a göre Kurum Sağlık Kurulunca meslekte kazanma gücü en az %10 oranında azaldığı tespit edilen sigortalı sürekli "
    "iş göremezlik gelirine hak kazanır.")

P.q("SGK md. 81",
    f"{K26}, 4/b kapsamındaki sigortalıların primlerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Üç oranın toplamı üzerinden öderler.",
    ["Sadece genel sağlık sigortası primi öderler.",
     "Sadece uzun vadeli sigorta primi öderler.",
     "Primlerini işveren hissesi olmadan %9 üzerinden öderler.",
     "Prim ödeme yükümlülükleri bulunmaz."],
    "Md. 81/g'ye göre 4/b sigortalıları (a), (c) ve (f) bentlerindeki prim oranlarının toplamı üzerinden, yani malullük-yaşlılık-"
    "ölüm, kısa vadeli ve genel sağlık sigortası oranları üzerinden primlerini öder.", zorluk="hard")

P.sayisal("SGK md. 19",
    f"{K}, sürekli tam iş göremezlik hâlinde sigortalıya aylık kazancının yüzde kaçı oranında gelir bağlanır?",
    "70", ["50", "60", "80", "100"],
    "Md. 19'a göre sürekli tam iş göremezlikte sigortalıya md. 17'ye göre hesaplanan aylık kazancının %70'i oranında gelir "
    "bağlanır; kısmi iş göremezlikte bu tutarın iş göremezlik derecesi oranındaki kısmı ödenir.")

P.q("SGK md. 82",
    f"{K}, günlük kazancı alt sınırın altında olan sigortalıya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Aradaki farka ait primleri işveren öder.",
    ["Prim, gerçek kazancı üzerinden alınır.",
     "Farkı sigortalı kendisi öder.",
     "Farka ait primleri Hazine öder.",
     "Bu sigortalıdan prim alınmaz."],
    "Md. 82'ye göre günlük kazancı alt sınırın altında olanların kazançları alt sınır üzerinden hesaplanır; aradaki farka ait "
    "primlerin tümünü işveren öder.")

P.sayisal("SGK md. 25",
    f"{K}, 4/a ve 4/b kapsamındaki sigortalının malul sayılması için çalışma gücünün en az yüzde kaçını kaybettiğinin "
    "tespiti gerekir?",
    "60", ["10", "40", "50", "70"],
    "Md. 25'e göre 4/a ve 4/b sigortalıları için çalışma gücünün veya iş kazası ya da meslek hastalığı sonucu meslekte "
    "kazanma gücünün en az %60'ını kaybettiği Kurum Sağlık Kurulunca tespit edilen sigortalı malul sayılır.", zorluk="easy")

P.q("SGK md. 82",
    f"{K}, aynı sigortalılık hâline tabi birden fazla işte çalışma nedeniyle üst sınırı aşan primler hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Talep üzerine sigortalıya iade edilir.",
    ["Kurum tarafından gelir kaydedilir.",
     "İşverene faiziyle iade edilir.",
     "Sonraki yılların primlerine mahsup edilemez.",
     "Sigortalının hizmet süresine eklenir."],
    "Md. 82'ye göre birden fazla işte çalışma nedeniyle ödenen primler üst sınıra göre hesaplanacak miktarı aşarsa, aşan kısım "
    "sigortalının talebi üzerine talep tarihini takip eden ay içinde hissesi oranında sigortalıya geri ödenir.",
    zorluk="hard")

P.sayisal("SGK md. 26",
    f"{K}, malullük aylığı bağlanabilmesi için sigortalının en az kaç yıldan beri sigortalı olması gerekir?",
    "10", ["5", "7", "15", "25"],
    "Md. 26'ya göre malullük aylığı için en az on yıldan beri sigortalı olup toplam 1800 gün prim bildirilmiş olması gerekir; "
    "başkasının sürekli bakımına muhtaç malullerde sigortalılık süresi aranmaz.")

P.q("SGK md. 88",
    f"{K}, 4/a sigortalılarının primlerinin ödenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sigortalı hissesini sigortalı kendisi öder.",
    ["İşveren sigortalı hissesini ücretten keser.",
     "İşveren kendi hissesini ekleyerek öder.",
     "Hak edilip ödenmeyen ücretin primi de ödenir.",
     "Ödeme Kurumca belirlenen günün sonuna kadar yapılır."],
    "Md. 88'e göre işveren, sigortalı hissesi prim tutarlarını ücretlerinden keserek ve kendi hissesini ekleyerek en geç Kurumca "
    "belirlenecek günün sonuna kadar Kuruma öder; hak edilip ödenmeyen ücretlerin primleri de aynı şekilde ödenir.")

P.sayisal("SGK md. 26",
    f"{K}, malullük aylığı bağlanabilmesi için en az kaç gün malullük, yaşlılık ve ölüm sigortaları primi bildirilmiş "
    "olmalıdır?",
    "1800", ["900", "3600", "5400", "7200"],
    "Md. 26'ya göre malullük aylığı için toplam 1800 gün malullük, yaşlılık ve ölüm sigortaları primi bildirilmiş olmalıdır.")

P.q("SGK md. 89",
    f"{K}, işyerinin devri hâlinde eski işverenin Kuruma olan prim borçlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yeni işveren de müteselsilen sorumludur.",
    ["Sadece eski işveren sorumludur.",
     "Borç devirle birlikte sona erer.",
     "Aksine sözleşme Kuruma karşı geçerlidir.",
     "Yeni işveren borcun yarısından sorumludur."],
    "Md. 89'a göre işyeri aktif veya pasifiyle birlikte devralınır, intikal eder, katılır veya birleşirse eski işverenin prim "
    "borçlarından yeni işveren de müştereken ve müteselsilen sorumludur; aykırı sözleşme hükümleri Kuruma karşı geçersizdir.")

P.sayisal("SGK md. 28",
    f"{K}, ilk defa bu Kanuna göre sigortalı sayılan 4/a sigortalısı için yaşlılık aylığında aranan prim gün sayısı "
    "kaçtır?",
    "7200", ["3600", "5400", "5975", "9000"],
    "Md. 28'e göre ilk defa bu Kanuna tabi olanlarda yaşlılık aylığı için 9000 gün aranır; 4/a sigortalıları için bu şart "
    "7200 gün olarak uygulanır.", zorluk="hard")

P.q("SGK md. 89",
    f"{K26}, gecikme cezası ve gecikme zammına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dava açılmışsa gecikme zammı tahsil edilmez.",
    ["Gecikme cezası ilk üç ay için uygulanır.",
     "Ödeme yapılan ay için zam günlük hesaplanır.",
     "Cumhurbaşkanı ceza oranını değiştirebilir.",
     "Gecikme zammı borç ödeninceye kadar işler."],
    "Md. 89'a göre dava ve icra takibi açılmış olsa bile prim ve diğer Kurum alacaklarının ödenmemiş kısmı için gecikme cezası "
    "ve gecikme zammı tahsil edilir.")

P.sayisal("SGK md. 28",
    f"{K}, ilk defa bu Kanuna göre sigortalı sayılanlar, yaş hadlerine üç yıl eklenmek şartıyla en az kaç gün prim "
    "bildirimiyle yaşlılık aylığından yararlanabilir?",
    "5400", ["1800", "3600", "3960", "7200"],
    "Md. 28'e göre sigortalılar yaş hadlerine 65 yaşını geçmemek üzere üç yıl eklenmek ve en az 5400 gün prim bildirilmiş "
    "olmak şartıyla da yaşlılık aylığından yararlanabilir.", zorluk="hard")

P.q("SGK md. 86",
    f"{K}, sigortalıların ay içinde otuz günden az çalışmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eksik gün nedenini sigortalı beyan eder.",
    ["Eksik gün sayısı işverence beyan edilir.",
     "Eksik gün belgelerinin şeklini Kurum belirler.",
     "Belgeler verilmezse beyan re’sen düzenlenir.",
     "Beyan muhtasar ve prim hizmet beyannamesiyle yapılabilir."],
    "Md. 86'ya göre ay içinde bazı günlerde çalıştırılmayan ve ücret ödenmeyen sigortalıların eksik gün nedeni ve sayısı "
    "işverence ilgili aya ait belgede veya muhtasar ve prim hizmet beyannamesinde beyan edilir.")

P.sayisal("SGK md. 32",
    f"{K}, 4/a sigortalısının hak sahiplerine ölüm aylığı bağlanabilmesi için, en az beş yıldan beri sigortalı olan "
    "sigortalı adına toplam en az kaç gün prim bildirilmiş olmalıdır?",
    "900", ["360", "720", "1080", "1800"],
    "Md. 32'ye göre ölüm aylığı için en az 1800 gün prim ya da 4/a sigortalıları için en az beş yıldan beri sigortalı olup "
    "toplam 900 gün prim bildirilmiş olması gerekir.", zorluk="hard")

P.q("SGK md. 17",
    f"{K26}, geçici iş göremezlik ödeneğinin hesabına esas günlük kazanç nasıl hesaplanır?",
    "On iki aylık kazanç gün sayısına bölünür.",
    ["Son ayın ücreti otuza bölünür.",
     "Asgari ücret günlük tutarı esas alınır.",
     "Son üç ayın brüt ücreti doksana bölünür.",
     "İşverenin beyan ettiği günlük ücret esas alınır."],
    "Md. 17'ye göre (7537 sayılı Kanunla değişik) ödeneklere esas günlük kazanç, iş kazası veya doğum tarihinden ya da iş "
    "göremezliğin başladığı tarihten önceki on iki aydaki prime esas kazançlar toplamının prim ödeme gün sayısına bölünmesiyle "
    "hesaplanır.", zorluk="hard")

P.sayisal("SGK md. 89",
    f"{K26}, Kurumun süresinde ödenmeyen prim alacaklarına ilk üç aylık sürede her ay için yüzde kaç gecikme cezası "
    "uygulanır?",
    "3", ["1", "2", "5", "10"],
    "Md. 89'a göre süresinde ödenmeyen prim ve diğer alacaklara ilk üç aylık sürede her ay için %3 gecikme cezası uygulanır; "
    "ayrıca gecikme zammı hesaplanır.")

P.oncul("SGK md. 16",
    f"{K} aşağıdaki haklar değerlendirilmektedir:",
    ["Günlük geçici iş göremezlik ödeneği",
     "Emzirme ödeneği",
     "Sürekli iş göremezlik geliri",
     "Malullük aylığı"],
    "Yukarıdakilerden hangileri hastalık ve analık sigortasından sağlanır?",
    "I ve II",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, II ve III"],
    "Md. 16'ya göre hastalık ve analık sigortasından geçici iş göremezlik ödeneği (I) ve analık sigortasından emzirme ödeneği "
    "(II) sağlanır; sürekli iş göremezlik geliri (III) iş kazası sigortasından, malullük aylığı (IV) malullük sigortasından "
    "verilir.", zorluk="hard")

P.sayisal("SGK md. 86",
    f"{K}, işveren işyeri defter, kayıt ve belgelerini ilgili olduğu yılı takip eden yıl başından başlamak üzere kaç yıl "
    "süreyle saklamak zorundadır?",
    "10", ["3", "5", "15", "30"],
    "Md. 86'ya göre işveren ve işyeri sahipleri defter, kayıt ve belgeleri on yıl, kamu idareleri otuz yıl saklamak ve "
    "istenmesi hâlinde on beş gün içinde ibraz etmek zorundadır.")

P.q("SGK md. 19",
    f"{K26}, sürekli iş göremezlik gelirine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kısmi iş göremezlikte tam gelir ödenir.",
    ["Kazanma gücü kaybını Kurum Sağlık Kurulu tespit eder.",
     "Gelir, kazanma gücü kaybı oranına göre hesaplanır.",
     "Tam iş göremezlikte aylık kazancın %70’i bağlanır.",
     "Yeniden tedavide kayıp oranı yeniden tespit edilir."],
    "Md. 19'a göre sürekli kısmi iş göremezlikte gelir tam iş göremezlik geliri gibi hesaplanır ve bunun iş göremezlik "
    "derecesi oranındaki tutarı ödenir.")

P.sayisal("SGK md. 89",
    f"{K}, yanlış veya yersiz alındığı tespit edilen primler, alındıkları tarihten en çok kaç yıl geçmemişse kanuni "
    "faiziyle geri verilir?",
    "10", ["2", "3", "5", "15"],
    "Md. 89'a göre yanlış veya yersiz alınan primler alındıkları tarihten on yıl geçmemişse hisseleri oranında kanuni faizi "
    "ile birlikte geri verilir.")

P.q("SGK md. 28",
    f"{K}, sigortalı olmadan önce malul sayılmayı gerektirecek hastalığı bulunan ve bu nedenle malullük aylığı "
    "alamayanlara yaşlılık aylığı bağlanması için aşağıdaki şartlardan hangisi aranır?",
    "En az 15 yıl sigortalılık ve 3960 gün prim",
    ["En az 10 yıl sigortalılık ve 1800 gün prim",
     "En az 25 yıl sigortalılık ve 5400 gün prim",
     "En az 20 yıl sigortalılık ve 7200 gün prim",
     "Sigortalılık süresi aranmaksızın 900 gün prim"],
    "Md. 28'e göre işe girişten önce malul sayılmayı gerektirecek hastalığı veya engelliliği bulunanlara en az on beş yıldan "
    "beri sigortalı olmak ve en az 3960 gün prim bildirilmiş olmak şartıyla yaşlılık aylığı bağlanır.", zorluk="hard")

P.sayisal("SGK md. 86",
    f"{K}, işveren, Kurumun denetim memurlarınca istenmesi hâlinde işyeri defter ve belgelerini kaç gün içinde ibraz "
    "etmek zorundadır?",
    "15", ["5", "7", "10", "30"],
    "Md. 86'ya göre işveren defter, kayıt ve belgeleri saklamak ve Kurumun denetim memurlarınca istenmesi hâlinde on beş gün "
    "içinde ibraz etmek zorundadır.")

P.q("SGK md. 18",
    f"{K}, hastalık nedeniyle geçici iş göremezlik ödeneği alabilmek için aşağıdakilerden hangisi aranmaz?",
    "En az beş yıllık sigortalılık süresi",
    ["Kurumca yetkili hekimden istirahat raporu",
     "Önceki bir yıl içinde doksan gün prim",
     "Hastalık sigortasına tabi olma",
     "İş göremezliğin üçüncü güne ulaşması"],
    "Md. 18/b'ye göre hastalık hâlinde ödenek için istirahat raporu, hastalık sigortasına tabi olma ve önceki bir yıl içinde "
    "doksan gün prim bildirimi aranır; ödenek üçüncü günden başlar, beş yıllık sigortalılık şartı yoktur.")

P.sayisal("SGK md. 86",
    f"{K}, kamu idareleri işyeri defter, kayıt ve belgelerini kaç yıl süreyle saklamak zorundadır?",
    "30", ["5", "10", "15", "20"],
    "Md. 86'ya göre işverenler on yıl, kamu idareleri otuz yıl, tasfiye ve iflas idaresi memurları görevleri süresince "
    "belgeleri saklar.", zorluk="hard")

P.q("SGK md. 28",
    f"{K}, ilk defa bu Kanuna göre sigortalı sayılanların yaşlılık aylığı yaş hadlerine ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Yaş hadleri 2030’dan itibaren artar.",
    ["Temel yaş kadında 58, erkekte 60’tır.",
     "2048’den itibaren yaş şartı 65’tir.",
     "Prim gün şartının dolduğu tarihteki had esas alınır.",
     "Üç yıl ekleme 65 yaşını geçemez."],
    "Md. 28'e göre yaş şartı 1/1/2036'dan itibaren kademeli olarak artar ve 1/1/2048'den itibaren kadın ve erkek için 65 olur; "
    "prim gün şartının doldurulduğu tarihteki yaş hadleri esas alınır.", zorluk="hard")

P.sayisal("SGK md. 16",
    f"{K}, 4/a sigortalısı kadına emzirme ödeneği verilebilmesi için doğumdan önceki bir yıl içinde en az kaç gün kısa "
    "vadeli sigorta kolları primi bildirilmiş olmalıdır?",
    "120", ["60", "90", "180", "360"],
    "Md. 16'ya göre emzirme ödeneği için 4/a sigortalıları adına doğumdan önceki bir yıl içinde en az 120 gün kısa vadeli "
    "sigorta kolları primi bildirilmiş olmalıdır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
