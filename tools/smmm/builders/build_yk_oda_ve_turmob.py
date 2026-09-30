# -*- coding: utf-8 -*-
"""Meslek Hukuku · Odalar ve TÜRMOB — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, TÜRMOB 2026 derlemesi):
  · 3568 sayılı Kanun m. 14-42 (27.03.2025-7546 değişiklikleri işlenmiş)
  · Serbest Muhasebeci Mali Müşavirler Odaları Yönetmeliği (14.01.2026-33137 işlenmiş)
  · TÜRMOB Yönetmeliği (14.01.2026-33137 işlenmiş)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_oda_ve_turmob_2026.json", lesson="meslek_hukuku", topic="oda_ve_turmob",
          konu_adi="Odalar ve TÜRMOB", seed=2026092804,
          surum="3568 s. Kanun (27.03.2025-7546 işlenmiş), SMMM Odaları Yön. ve TÜRMOB Yön. (14.01.2026-33137 işlenmiş), 28.09.2026 kontrolü")

K = "3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu’na göre"
OY = "Serbest Muhasebeci Mali Müşavirler Odaları Yönetmeliği’ne göre"
TY = "Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği Yönetmeliği’ne göre"

# ================================================================ odalar: nitelik ve kuruluş
P.q("3568 s. Kanun m. 14",
    f"{K}, meslek odalarının hukuki niteliğine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Tüzel kişiliğe sahip, kamu kurumu niteliğinde meslek kuruluşlarıdır.",
    ["Tüzel kişiliği bulunmayan, Birliğe bağlı taşra birimleridir.",
     "Dernekler mevzuatına tabi, özel hukuk tüzel kişileridir.",
     "Hazine ve Maliye Bakanlığına bağlı katma bütçeli kuruluşlardır.",
     "Ticaret sicilinde tescil edilen, kâr amacı gütmeyen şirketlerdir."],
    "Kanun m. 14'e göre SMMM ve YMM odaları ayrı ayrı kurulur ve tüzel kişiliğe sahip, kamu kurumu niteliğinde meslek "
    "kuruluşlarıdır; kuruluş amaçları dışında faaliyette bulunamazlar.",
    zorluk="easy")

P.sayisal("3568 s. Kanun m. 15/1; SMMM Odaları Yön. m. 5",
    f"{K}, bölgesi içinde kendi mesleği konusunda en az kaç meslek mensubu bulunan il merkezlerinde bir oda kurulur?",
    "250", ["100", "125", "150", "200"],
    "Kanun m. 15'e göre bölgesi içinde en az 250 meslek mensubu bulunan il merkezlerinde ve 250 meslek mensubu bulunan "
    "ilçelerde (büyükşehir belediyesi sınırları içindeki ilçeler hariç) oda kurulur; ilçelerde ayrıca en az 100 meslek "
    "mensubunun yazılı başvurusu aranır.")

P.sayisal("3568 s. Kanun m. 15/1",
    f"{K}, bölgesinde 250 meslek mensubu bulunan ve büyükşehir belediyesi sınırları dışında kalan bir ilçede oda "
    "kurulabilmesi için o ilçedeki en az kaç meslek mensubunun yazılı başvurusu aranır?",
    "100", ["50", "75", "125", "150"],
    "Kanun m. 15'e göre ilçelerde oda kurulabilmesi için o ilçedeki en az 100 meslek mensubunun yazılı başvurusu aranır.")

P.q("3568 s. Kanun m. 15",
    f"{K}, odaların kuruluşu ve faaliyetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Odalar, kuruluş kararının oda genel kurulunda alınmasıyla tüzel kişilik kazanır.",
    ["Oda kurulamayan yerlerin en yakın odaya bağlanmasına veya bölge odası kurulmasına Birlikçe karar verilir.",
     "Odalar, kuruluşlarını Birlik Yönetim Kurulu aracılığıyla Bakanlığa bildirmekle tüzel kişilik kazanır.",
     "Odalara üye olmayan meslek mensupları mesleki faaliyette bulunamaz.",
     "Büyükşehir belediyesi sınırları içindeki ilçelerde ilçe odası kurulamaz."],
    "Kanun m. 15'e göre odalar kuruluşlarını Birlik Yönetim Kurulu aracılığıyla Hazine ve Maliye Bakanlığına bildirmekle "
    "tüzel kişilik kazanır. Bölge odası kararı Birliğe aittir ve Bakanlığa bildirilir.")

P.q("3568 s. Kanun m. 15/5-6",
    f"{K}, amaçları dışında faaliyet gösteren bir odanın sorumlu organlarının görevlerine son verilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bakanlık veya başsavcılık istemiyle asliye hukuk mahkemesi karar verir.",
    ["Birlik Yönetim Kurulunun kararıyla görevlerine son verilir ve yerlerine Birlikçe atama yapılır.",
     "Oda genel kurulunun olağanüstü toplantısında üye tam sayısının üçte ikisiyle karar verilir.",
     "Vali tarafından görevden alınır ve karar 48 saat içinde idare mahkemesinin onayına sunulur.",
     "Birlik Disiplin Kurulunca yapılan soruşturma sonunda meslekten çıkarma cezası verilir."],
    "Kanun m. 15'e göre amaç dışı faaliyette bulunan odaların sorumlu organlarının görevine son verilmesine Bakanlığın "
    "veya Cumhuriyet başsavcılığının istemi üzerine asliye hukuk mahkemesince basit usulle karar verilir ve dava en geç "
    "üç ay içinde sonuçlandırılır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 15 son fıkralar",
    f"{K}, gecikmede sakınca bulunan hallerde odaların vali tarafından faaliyetten men edilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Karar 24 saat içinde hâkimin onayına sunulur; hâkim 48 saat içinde açıklamazsa karar yürürlükten kalkar.",
    ["Karar 48 saat içinde hâkimin onayına sunulur; hâkim 72 saat içinde açıklamazsa karar kesinleşir.",
     "Karar 24 saat içinde Bakanlığın onayına sunulur; Bakanlık 7 gün içinde açıklamazsa karar kesinleşir.",
     "Karar 3 gün içinde hâkimin onayına sunulur; hâkim 5 gün içinde açıklamazsa karar yürürlükten kalkar.",
     "Karar oda genel kurulunu da kapsar ve genel kurul toplantıları da durdurulur."],
    "Kanun m. 15'e göre milli güvenlik, kamu düzeni veya suçun önlenmesi gibi hallerde vali odayı faaliyetten men "
    "edebilir; karar 24 saat içinde hâkimin onayına sunulur, hâkim 48 saat içinde açıklamazsa karar kendiliğinden "
    "yürürlükten kalkar. Göreve son verme hükümleri oda genel kurulu hakkında uygulanmaz.",
    zorluk="hard")

# ================================================================ oda gelirleri ve organları
P.q("3568 s. Kanun m. 16",
    f"Aşağıdakilerden hangisi {K.replace('’na göre', '’na göre,')} odaların gelirlerinden biri değildir?",
    "Ruhsatname ücretleri",
    ["Yıllık üye aidatları", "Odaya giriş ücretleri", "Yardım ve bağışlar", "Mesleki eğitime yönelik kurs ve staj ücretleri"],
    "Kanun m. 16'ya göre oda gelirleri giriş ücreti, yıllık aidat, yardım ve bağışlar ile mesleki eğitime yönelik kurs "
    "ve staj ücretleri ve diğer gelirlerdir. Ruhsatname ücretleri m. 30'a göre Birliğin geliridir.",
    zorluk="easy")

P.q("3568 s. Kanun m. 16/2; SMMM Odaları Yön. m. 16",
    f"{K}, kamu kurum ve kuruluşlarında çalışan veya mesleği fiilen icra etmeyen meslek mensupları odaya giriş ücreti ve yıllık aidatlarını nasıl öderler?",
    "Yüzde elli indirimli öderler.",
    ["Yüzde yirmi beş indirimli öderler.",
     "Yüzde yetmiş beş indirimli öderler.",
     "Giriş ücretini tam, aidatı yarı öderler.",
     "Aidattan muaf tutulur, giriş ücretini öderler."],
    "Kanun m. 16/2 ve Odalar Yönetmeliği m. 16'ya göre kamu kurum ve kuruluşlarında çalışanlar ile mesleği fiilen icra "
    "etmeyenler odaya giriş ücreti ve yıllık üye aidatlarını yüzde elli indirimli olarak öder.")

P.q("SMMM Odaları Yön. m. 16",
    "(Z) Serbest Muhasebeci Mali Müşavirler Odası, yeni dönem bütçesinde kayıt ücreti, aidat ve diğer gelir kalemlerini "
    f"planlamaktadır. {OY}, odanın gelirleriyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kayıt ücreti, her üyeden oda yönetim kurulunun her yıl belirlediği tutarda iki yılda bir alınır.",
    ["Maktu yıllık aidat, memur maaşı taban aylığı katsayısının en az 200, en fazla 400 ile çarpımıdır.",
     "Oda aracılığıyla üyelere sağlanan tahkim ve bilirkişilik işlerinden alınan ücretlerin %4'ü oda gelirlerindendir.",
     "Kayıt ücreti, çalışanlar listesine kaydedilecek ortaklık büroları ve şirketlerden de alınır.",
     "Mesleki kimlik belgesi bedeli taban aylık katsayısının 200 ile çarpımıyla bulunur."],
    "Odalar Yönetmeliği m. 16/a'ya göre kayıt ücreti kayıt anında bir kez alınır ve taban aylık katsayısının 300 ile "
    "çarpımıyla bulunur. Aidat, tahkim-bilirkişilik payı ve kimlik belgesi bedeli aynı maddede düzenlenmiştir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 17",
    f"Aşağıdakilerden hangisi {K.replace('’na göre', '’na göre,')} odaların organlarından biri değildir?",
    "Danışma Kurulu",
    ["Yönetim Kurulu", "Genel Kurul", "Disiplin Kurulu", "Denetleme Kurulu"],
    "Kanun m. 17'ye göre odanın organları genel kurul, yönetim kurulu, disiplin kurulu ve denetleme kuruludur. Danışma "
    "kurulu Kanunda oda organı olarak sayılmamıştır.",
    zorluk="easy")

P.q("3568 s. Kanun m. 19",
    f"{K}, bir serbest muhasebeci mali müşavir odasına yazılacak adayların giriş ücretlerini ve odaya yazılı üyelerin yıllık aidatlarını tespit etmek aşağıdakilerden hangisinin görevidir?",
    "Oda Genel Kurulu",
    ["Oda Yönetim Kurulu", "Oda Denetleme Kurulu", "Birlik Yönetim Kurulu", "Oda Disiplin Kurulu"],
    "Kanun m. 19/h'ye göre giriş ücretlerini ve yıllık aidatları tespit etmek ve ödeme tarihlerini belirlemek oda genel "
    "kurulunun görevidir. Yönetim kurulu tarifeyi hazırlayıp genel kurula sunar (Odalar Yön. m. 12/j).")

P.q("3568 s. Kanun m. 19",
    f"{K}, aşağıdakilerden hangisi oda genel kurulunun görevleri arasında yer almaz?",
    "Uyulması mecburi mesleki kararları almak",
    ["Yönetim, disiplin ve denetleme kurulu üyeleri ile Birlik temsilcilerini seçmek",
     "Taşınmaz alım ve satımında yönetim kuruluna yetki vermek",
     "Bütçeyi ve kesin hesapları tasdik etmek",
     "Yönetim kurulunu ibra etmek"],
    "Uyulması mecburi mesleki kararları almak Kanun m. 33/f'ye göre Birlik Genel Kurulunun görevidir; oda genel kurulu "
    "bu konuda yalnızca Birliğe teklifte bulunur (m. 19/e). Diğerleri m. 19'da sayılan oda genel kurulu görevleridir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 20/1; SMMM Odaları Yön. m. 9",
    "(Y) Serbest Muhasebeci Mali Müşavirler Odası, son seçimli olağan genel kurulunu yapmış ve yeni kurullar göreve "
    f"başlamıştır. {OY}, Oda Genel Kurulu olağan olarak ne zaman toplanır?",
    "Üç yılda bir mayıs ayı içinde",
    ["İki yılda bir mayıs ayı içinde", "İki yılda bir eylül ayı içinde",
     "Üç yılda bir nisan ayı içinde", "Üç yılda bir eylül ayı içinde"],
    "Kanun m. 20 ve Odalar Yönetmeliği m. 9'a göre oda genel kurulu üç yılda bir mayıs ayı içinde başkanın daveti üzerine "
    "toplanır. Birlik Genel Kurulu ise üç yılda bir eylül ayında toplanır (Kanun m. 34).",
    zorluk="easy")

P.q("3568 s. Kanun m. 20 (27.03.2025-7546 değişikliği)",
    f"{K}, oda genel kurul toplantısına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Toplantı, ilk toplantı tarihinden en az 20 gün önce tirajı yüz binin üzerindeki bir gazetede ilan edilir.",
    ["Yönetim kurulu başkanı, üyelerin beşte birinin yazılı talebiyle en geç 15 gün içinde genel kurulu toplar.",
     "Toplantı ilanı, ilk toplantıdan en az 10 gün önce odanın resmi internet sitesinde yayımlanır.",
     "Genel kurul üye tam sayısının salt çoğunluğuyla toplanır, ikinci toplantıda çoğunluk aranmaz.",
     "İkinci toplantıya katılan üye sayısı kurulların asıl üyeleri toplamının iki katından az olamaz."],
    "7546 sayılı Kanunla değişen m. 20'ye göre oda genel kurulu ilanı ilk toplantıdan en az 10 gün önce odanın resmi "
    "internet sitesinde yapılır. 20 günlük gazete ilanı Birlik Genel Kurulu için öngörülmüştür (m. 34).",
    zorluk="hard")

P.sayisal("3568 s. Kanun m. 21; SMMM Odaları Yön. m. 10",
    f"{OY}, üye sayısı beş bini aşan odalarda Oda Yönetim Kurulu kaç asıl üyeden oluşur?",
    "9", ["3", "5", "7", "11"],
    "Kanun m. 21 ve Odalar Yönetmeliği m. 10'a göre yönetim kurulu, üye sayısı binin altındaki odalarda beş asıl beş "
    "yedek, bin ilâ beş bin arasında yedi asıl yedi yedek, beş bini aşanlarda dokuz asıl dokuz yedek üyeden oluşur.")

P.q("3568 s. Kanun m. 22; SMMM Odaları Yön. m. 11",
    f"{K}, oda yönetim kurulu üyeliğine seçilme yeterliğine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üye sayısı yüzden az olan odalarda en az beş yıllık kıdem şartı aranır.",
    ["Üyeler, kayıtlı olduğu odada en az üç yıl kıdemli olanlar arasından seçilir.",
     "Serbest veya bir işyerine bağlı olarak fiilen mesleki faaliyette bulunmak gerekir.",
     "Üst üste iki dönem başkanlık yapan, iki seçim dönemi geçmeden yönetime seçilemez.",
     "Seçilme yeterliğini kaybeden yönetim kurulu üyesinin görevi sona erer."],
    "Kanun m. 22'ye göre yönetim kurulu üyeleri odada en az üç yıl kıdemli ve fiilen mesleki faaliyette bulunanlar "
    "arasından seçilir; üye sayısı yüzden az olan odalarda üç yıllık süre şartı aranmaz.")

P.q("3568 s. Kanun m. 24; SMMM Odaları Yön. m. 14",
    "Oda yönetim kurulu üyesi (A), ardı ardına üç olağan toplantıya özürsüz olarak katılmamış ve yönetim kurulu kararıyla "
    f"istifa etmiş sayılmıştır. {K}, (A)'nın bu karara karşı başvurabileceği yol aşağıdakilerden hangisidir?",
    "Tebliğden itibaren on beş gün içinde TÜRMOB’a (Birliğe) itiraz",
    ["Tebliğden itibaren otuz gün içinde oda genel kuruluna itiraz",
     "Tebliğden itibaren on beş gün içinde oda disiplin kuruluna itiraz",
     "Tebliğden itibaren altmış gün içinde idare mahkemesine dava",
     "Karar tarihinden itibaren yedi gün içinde denetleme kuruluna itiraz"],
    "Kanun m. 24'e göre ardı ardına üç olağan toplantıya özürsüz katılmayan üye yönetim kurulu kararıyla istifa etmiş "
    "sayılır; bu karara karşı tebliğden itibaren on beş gün içinde Birliğe itiraz edilebilir.")

P.q("3568 s. Kanun m. 24; SMMM Odaları Yön. m. 14",
    f"{OY}, oda yönetim kurulunun toplantı ve karar usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetim kurulu toplantıları açıktır ve odaya kayıtlı her üye izleyici olarak katılabilir.",
    ["Yönetim kurulu salt çoğunlukla toplanır ve üye tam sayısının salt çoğunluğuyla karar verir.",
     "Oylarda eşitlik hâlinde başkanın bulunduğu taraf üstün tutulur.",
     "Üyeler, üçüncü dereceye kadar kan hısımlarıyla ilgili işlerin görüşülmesine katılamaz.",
     "Karara muhalif üyeler gerekçeli olmak koşuluyla muhalefet şerhi verebilir."],
    "Odalar Yönetmeliği m. 14'e göre yönetim kurulu toplantıları gizlidir; istisnai ve zorunlu haller dışında görevliler "
    "dışında kimse toplantıya alınmaz. Diğer ifadeler Kanun m. 24 ve Yönetmelik m. 14'te yer alır.")

P.q("3568 s. Kanun m. 25",
    f"{K}, oda disiplin kuruluna ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Üye sayısı 50'den fazla olan odalarda beş asıl ve üç yedek üyeden oluşur.",
    ["Üye sayısı 50'den fazla olan odalarda yedi asıl ve beş yedek üyeden oluşur.",
     "Oda büyüklüğünden bağımsız olarak üç asıl ve üç yedek üyeden oluşur.",
     "Üye sayısı 100'den fazla olan odalarda beş asıl ve beş yedek üyeden oluşur.",
     "Üye sayısı 50'ye kadar olan odalarda beş asıl ve bir yedek üyeden oluşur."],
    "Kanun m. 25'e göre oda disiplin kurulu, üye sayısı 50'ye kadar olan odalarda üç, 50'den fazla olan odalarda beş "
    "üyeden oluşur; üç üyeli kurullarda bir, beş üyeli kurullarda üç yedek üye seçilir.")

P.q("3568 s. Kanun m. 25-27",
    "Birlik kararıyla kurulan ve üye sayısı 60 olan bir bölge odasının olağan genel kurulunda disiplin ve denetleme "
    f"kurullarının seçimi yapılacaktır. {K}, oda kurullarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Oda denetleme kurulu beş asıl ve beş yedek üyeden oluşur.",
    ["Disiplin kurulu en az üç kişinin hazır bulunmasıyla toplanır.",
     "Disiplin kurulunda başkan yokken meslekte en kıdemli üye başkanlık eder.",
     "Denetleme kurulu odanın işlem ve hesaplarını denetleyip genel kurula rapor verir.",
     "Disiplin kurulu kararlarına tebliğden itibaren otuz gün içinde Birlik Disiplin Kuruluna itiraz edilir."],
    "Kanun m. 27'ye göre oda denetleme kurulu üç yıl için seçilen üç üye ile bir yedek üyeden oluşur. Disiplin kuruluna "
    "ilişkin diğer ifadeler m. 25'te, denetleme kurulunun görevi m. 27'dedir.")

P.q("SMMM Odaları Yön. m. 15",
    "Oda yönetim kurulu, genel kurulun onayına sunacağı gelecek yılın tahmini gelir ve gider bütçesini hazırlamaya "
    f"başlamıştır. {OY}, oda bütçesine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Nisanda hazırlanır, kabul edilince izleyen yılın ocak ayında yürürlüğe girer.",
    ["Bütçe yönetim kurulunca mart ayında hazırlanır ve kabul edildiği mayıs ayında yürürlüğe girer.",
     "Bütçe denetleme kurulunca hazırlanır ve Birlik Yönetim Kurulunun onayıyla yürürlüğe girer.",
     "Bütçe genel kurulca kabul edilmezse önceki yıl bütçesi aynen ve süresiz olarak uygulanır.",
     "Bütçede yedek ödenek ayrılmaz; kullanılmayan ödenekler yıl sonunda iptal edilir."],
    "Odalar Yönetmeliği m. 15'e göre bütçe yönetim kurulunca nisan ayında hazırlanıp genel kurula sunulur ve izleyen yılın "
    "ocak ayının birinci gününden itibaren uygulanır; bütçenin yüzde onu yedek ödenektir. Bütçe yürürlüğe konulamazsa "
    "önceki yıl bütçesinin 1/12'si esas alınarak geçici bütçelerle işlem yapılır.",
    zorluk="hard")

# ================================================================ Birlik
P.q("3568 s. Kanun m. 28",
    f"{K}, Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Birliğin merkezi İstanbul'dadır.",
    ["Birlik, tüzel kişiliğe sahip kamu kurumu niteliğinde meslek kuruluşudur.",
     "Birlik, kuruluş amaçları dışında faaliyette bulunamaz.",
     "Birliğin kısa adı TÜRMOB'dur.",
     "Bütün SMMM ve YMM odaları Birliğe katılır."],
    "Kanun m. 28'e göre Birlik tüzel kişiliğe sahip kamu kurumu niteliğinde meslek kuruluşudur ve merkezi Ankara'dadır; "
    "Bakanlığın bağlı kuruluşu değildir. Kısa ad TÜRMOB'dur (m. 1).")

P.q("3568 s. Kanun m. 30; TÜRMOB Yön. m. 8",
    f"{TY}, aşağıdakilerden hangisi TÜRMOB’un gelirlerinden biri değildir?",
    "Odaların net gelirlerinin %10'u oranındaki paylar",
    ["Birliğe ait mal gelirleri",
     "Kurs ve eğitim gelirleri",
     "Yeminli mali müşavirlik mühür ücretleri",
     "Ruhsatname ücretleri"],
    "TÜRMOB Yönetmeliği m. 8'e göre Birlik gelirleri; odaların brüt gelirlerinin %10'unu geçmemek üzere alınacak paylar, "
    "mal gelirleri, ruhsatname ücretleri, YMM mühür ücretleri, bağış ve yardımlar, kurs ve eğitim gelirleri ile diğer "
    "gelirlerdir. Pay, 2015 değişikliğiyle net değil brüt gelir üzerinden hesaplanır.",
    zorluk="hard")

P.q("TÜRMOB Yön. m. 9",
    f"{TY}, odaların Birlik payını ödeme süresine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her oda üç ayda tahsil ettiği brüt gelirden Birlik payını izleyen ayın 15'ine kadar öder.",
    ["Her oda bir yıl içinde tahsil ettiği net gelirlerinden Birlik payını izleyen yılın ocak ayı sonuna kadar öder.",
     "Her oda aylık tahsil ettiği net gelirlerinden Birlik payını izleyen ayın son iş gününe kadar öder.",
     "Her oda altı ayda bir tahsil ettiği brüt gelirlerinden Birlik payını izleyen ayın 30'una kadar öder.",
     "Her oda genel kurul yılında toplam brüt gelirinin %10'unu genel kurul tarihinden önce öder."],
    "TÜRMOB Yönetmeliği m. 9'a göre her oda üç ay içinde tahsil ettiği brüt gelirlerinden Birliğin payına isabet eden "
    "tutarı izleyen ayın 15'inci günü akşamına kadar Birliğe öder; mühür ve ruhsatname ücretleri belgeler verilmeden "
    "önce tahsil edilir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 31; TÜRMOB Yön. m. 10",
    f"{TY}, aşağıdakilerden hangisi Birliğin organlarından biri değildir?",
    "Haksız Rekabet Kurulu",
    ["Denetleme Kurulu", "Disiplin Kurulu", "Genel Kurul", "Yönetim Kurulu"],
    "Kanun m. 31 ve TÜRMOB Yönetmeliği m. 10'a göre Birliğin organları genel kurul, yönetim kurulu, disiplin kurulu ve "
    "denetleme kuruludur. Haksız rekabetle mücadele kurulu Birlik Yönetim Kuruluna bağlı bir çalışma kuruludur.",
    zorluk="easy")

P.q("3568 s. Kanun m. 32; TÜRMOB Yön. m. 11",
    f"{K}, Birlik Genel Kuruluna odalarca seçilecek temsilci sayısına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sabit üç temsilciye ek olarak üyelerinin yetmiş beşte biri kadar temsilci seçilir.",
    ["Her oda, üye sayısından bağımsız beş temsilciye ek olarak üyelerinin yüzde biri oranında temsilci seçer.",
     "Her oda, üyelerinin elliye biri oranında temsilci seçer; en az bir temsilci güvence altındadır.",
     "Her oda, üye sayısından bağımsız olarak eşit sayıda, yedi asıl ve yedi yedek temsilci seçer.",
     "Her oda, üyelerinin yetmiş beşte biri oranında seçer; yarımdan az kesirler tama tamamlanır."],
    "Kanun m. 32'ye göre her oda, üye sayısına bağlı olmaksızın seçeceği üç temsilciye ilave olarak üyelerinin yetmiş "
    "beşte biri oranında temsilci ve aynı sayıda yedek temsilci seçer; oranın yarısından az olanlar dikkate alınmaz, "
    "fazla olanlar tama tamamlanır. Temsilciler üç yıl için seçilir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 33; TÜRMOB Yön. m. 12",
    f"{TY}, aşağıdakilerden hangisi TÜRMOB Genel Kurulu’nun görevlerinden biridir?",
    "Uyulması mecburi mesleki kararlar almak",
    ["Birlik bütçesini hazırlamak",
     "Mesleki standartları geliştirmek",
     "Mesleki çalışma komiteleri kurmak",
     "Mesleki ruhsatları ve YMM mührünü vermek"],
    "Kanun m. 33/f ve TÜRMOB Yönetmeliği m. 12/f'ye göre uyulması mecburi mesleki kararları almak genel kurulun görevidir. "
    "Bütçeyi yapmak, standartları geliştirmek, komite kurmak ve ruhsat ile mühür vermek yönetim kurulunun görevleridir "
    "(TÜRMOB Yön. m. 23).")

P.q("3568 s. Kanun m. 34 (27.03.2025-7546 değişikliği); TÜRMOB Yön. m. 13-14",
    f"{K}, Birlik Genel Kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Genel kurul üç yılda bir mayıs ayında Birlik Yönetim Kurulu Başkanının daveti üzerine toplanır.",
    ["Toplantı ilanı ilk toplantıdan en az yirmi gün önce tirajı yüz binin üzerindeki bir gazetede yapılır.",
     "Temsilcilerin beşte birinin yazılı talebiyle olağanüstü toplantıya çağrılması mecburidir.",
     "Temsilcilerin beşte ikisinin imzasıyla teklif edilen konular gündeme ilave edilir.",
     "Genel kurul toplantılarında hazır bulunanların salt çoğunluğuyla karar verilir."],
    "Kanun m. 34'e göre Birlik Genel Kurulu üç yılda bir eylül ayında toplanır; mayıs ayı oda genel kurulları içindir "
    "(m. 20). İlan, olağanüstü toplantı ve gündem kuralları aynı maddededir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 35",
    f"{K}, Birlik Yönetim Kurulu kaç üyeden oluşur?",
    "9 asıl, 9 yedek",
    ["9 asıl, 7 yedek", "7 asıl, 7 yedek", "7 asıl, 5 yedek", "5 asıl, 5 yedek"],
    "Kanun m. 35'e göre Birlik Yönetim Kurulu, üç yıl için seçilen dokuz asıl ve dokuz yedek üyeden oluşur; üyelerden "
    "beşinin yeminli mali müşavir olması zorunludur.",
    zorluk="easy")

P.q("3568 s. Kanun m. 35; TÜRMOB Yön. m. 21-22",
    f"{K}, Birlik Yönetim Kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Başkan, en az on yıl SMMM'lik yapmış üyeler arasından seçilir.",
    ["Yönetim kurulu üyelerinden beşinin yeminli mali müşavir olması zorunludur.",
     "Üyeler kayıtlı olduğu odada en az üç yıl kıdemli genel kurul üyeleri arasından seçilir.",
     "Birliğin hukuki temsilcisi yönetim kurulu başkanıdır.",
     "Yönetim kurulu başkan ve üyeleri genel kurulda oy kullanma hakkına sahiptir."],
    "Kanun m. 35'e göre Birlik Yönetim Kurulu Başkanı en az beş yıl süreyle yeminli mali müşavirlik yapmış olanlar "
    "arasından seçilir. Beş YMM üye, üç yıl kıdem, hukuki temsil ve oy hakkı aynı maddededir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 36; TÜRMOB Yön. m. 23",
    f"{K}, aşağıdakilerden hangisi Birlik Yönetim Kurulunun görevleri arasında yer almaz?",
    "Oda disiplin kurulu kararlarına karşı yapılan itirazları incelemek",
    ["Odalarca önerilen giriş ücreti ve aidatları Bakanlığın tasdikine sunmak",
     "Odaların görüşünü alarak hazırlanan asgari ücret tarifelerini Bakanlığa sunmak",
     "Kanun uyarınca yapılması gereken sınavları yapmak",
     "Mesleki ruhsatları vermek"],
    "Oda disiplin kurulu kararlarına karşı itirazları incelemek Kanun m. 38'e göre Birlik Disiplin Kurulunun görevidir. "
    "Diğer seçenekler m. 36'da Birlik Yönetim Kurulunun görevleri olarak sayılmıştır.")

P.q("3568 s. Kanun m. 38; TÜRMOB Yön. m. 34",
    f"{K}, Birlik Disiplin Kuruluna ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Beş asıl ve beş yedek üyeden oluşur; asıl üyelerin üçünün yeminli mali müşavir olması mecburidir.",
    ["Yedi asıl ve yedi yedek üyeden oluşur; asıl üyelerin dördünün yeminli mali müşavir olması mecburidir.",
     "Üç asıl ve üç yedek üyeden oluşur; başkanın yeminli mali müşavir olması mecburidir.",
     "Beş asıl ve üç yedek üyeden oluşur; yeminli mali müşavir üye bulundurma zorunluluğu yoktur.",
     "Dokuz asıl ve dokuz yedek üyeden oluşur; üyelerin beşinin YMM olması mecburidir."],
    "Kanun m. 38'e göre Birlik Disiplin Kurulu üç yıl için seçilen beş asıl ve beş yedek üyeden oluşur; asıl üyelerin "
    "üçünün YMM olması mecburidir, genel kurulda bu sayıda YMM yoksa bulunanlarla yetinilir.")

P.q("3568 s. Kanun m. 39; TÜRMOB Yön. m. 38-39",
    f"{TY}, Birlik Denetleme Kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetleme kurulu üyeleri Birlik Yönetim Kurulu toplantılarına katılıp oy kullanabilir.",
    ["Üç yıl için seçilen üç asıl ve üç yedek üyeden oluşur.",
     "Üyelerinden en az birinin yeminli mali müşavir olması zorunludur.",
     "Kurula seçilen yeminli mali müşavir, kurulun başkanıdır.",
     "Birliğin işlem ve hesaplarını denetler ve genel kurula rapor verir."],
    "Kanun m. 39 ve TÜRMOB Yönetmeliği m. 39'a göre denetleme kurulu üyeleri yönetim kurulu toplantılarına katılabilir, "
    "ancak oy kullanamaz. Diğer ifadeler m. 38-40'ta yer alır.")

# ================================================================ seçimler, denetim
P.q("3568 s. Kanun m. 40",
    f"{K}, oda ve Birlik organlarının seçimlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Seçimler açık oyla ve Birlik Yönetim Kurulunun gözetimi altında yapılır.",
    ["Seçim yapılacak toplantıdan en az 15 gün önce üye listesi ilçe seçim kurulu başkanına verilir.",
     "Seçimler pazar günü saat dokuz ile on yedi arasında yapılacak şekilde düzenlenir.",
     "Dört yüz kişiden fazla üye bulunması hâlinde her dört yüz kişi için bir oy sandığı bulunur.",
     "Üyeler oda veya Birlik yönetim, denetleme ve disiplin kurullarından birinde görev alabilir."],
    "Kanun m. 40'a göre oda ve Birlik organ seçimleri gizli oyla ve yargı gözetimi altında yapılır. On beş günlük süre, "
    "pazar günü 9-17 saatleri, 400 kişilik sandık kuralı ve tek kurulda görev alma aynı maddededir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 40",
    f"{K}, seçim sonuçlarına yapılacak itirazlar ve seçimin iptaline ilişkin aşağıdakilerden hangisi doğrudur?",
    "İtiraz iki gün içinde yapılır; hâkim aynı gün inceleyip karara bağlar.",
    ["İtirazlar sonuçların ilanından itibaren yedi gün içinde yapılır; hâkim on gün içinde karar verir.",
     "İtirazlar on beş gün içinde Birlik Yönetim Kuruluna yapılır ve kurulun kararı kesindir.",
     "İtirazlar üç gün içinde ilçe seçim kuruluna yapılır ve kararı idare mahkemesine taşınabilir.",
     "İtirazlar otuz gün içinde oda genel kuruluna yapılır ve genel kurulun kararıyla sonuç kesinleşir."],
    "Kanun m. 40'a göre seçim işlemleri ve tutanakların düzenlenmesinden itibaren iki gün içinde yapılan itirazlar hâkim "
    "tarafından aynı gün incelenip kesin olarak karara bağlanır; hâkim seçimi iptal ederse bir aydan az, iki aydan fazla "
    "olmamak üzere yenileme gününü belirler.",
    zorluk="hard")

P.q("3568 s. Kanun m. 41",
    f"{K}, oda ve Birlik organlarının denetimine ve raporlama yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Faaliyet raporu ve mali tablolar izleyen yılın ocak sonuna kadar internette yayımlanır.",
    ["Odalar ve Birlik faaliyet raporlarını her yıl mart ayı sonuna kadar Resmî Gazete'de yayımlatır.",
     "Oda ve Birlik organlarını Sayıştay denetler; Bakanlığın denetim yetkisi bulunmaz.",
     "Odalar üyelerine ilişkin bilgileri beş yılda bir Hazine ve Maliye Bakanlığına bildirir.",
     "Odaların mali işlemlerini Birlik Denetleme Kurulu denetler ve sonucu Bakanlığa bildirir."],
    "Kanun m. 41'e göre Hazine ve Maliye Bakanlığı oda ve Birlik organlarını denetlemeye yetkilidir; odalar her yıl sonu "
    "itibarıyla üye bilgilerini ocak ayı sonuna kadar bildirir; odalar ve Birlik faaliyet raporu ve mali tablolarını "
    "izleyen yılın ocak ayı sonuna kadar internet sitelerinde yıl sonuna kadar kalmak üzere yayımlar.",
    zorluk="hard")

P.q("3568 s. Kanun m. 42; SMMM Odaları Yön. m. 23",
    f"{K}, odaları veya Birliği temsil etmek üzere milletlerarası toplantı ve kongrelere katılmak aşağıdakilerden hangisinin iznine tabidir?",
    "Hazine ve Maliye Bakanlığının",
    ["Dışişleri Bakanlığının", "Birlik Genel Kurulunun", "Oda Genel Kurulunun", "Cumhurbaşkanlığının"],
    "Kanun m. 42'ye göre odaları veya Birliği temsil etmek üzere milletlerarası toplantı ve kongrelere katılmak Maliye "
    "(bugün Hazine ve Maliye) Bakanlığının iznine tabidir.")

P.oncul("3568 s. Kanun m. 30; TÜRMOB Yön. m. 8 ve 12",
    "Birliğin gelirlerine ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Ruhsatname ücretleri Birliğin gelirlerindendir.",
     "Yeminli mali müşavirlik mühür ücretleri odaların gelirlerindendir.",
     "Odalardan alınacak pay miktarı ile ruhsat ve mühür ücretlerini Birlik Genel Kurulu tespit eder.",
     "Odalardan alınacak pay, odaların net gelirinin %20'sini geçemez."],
    f"{TY}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve III",
    ["Yalnız I", "I ve III", "II ve III", "II ve IV", "I, III ve IV"],
    "TÜRMOB Yönetmeliği m. 8'e göre ruhsatname ve YMM mühür ücretleri Birliğin gelirleridir; odalardan alınacak pay brüt "
    "gelirlerin %10'unu geçemez. M. 12/d'ye göre pay miktarı, ruhsat ve mühür ücretleri Birlik Genel Kurulunca tespit "
    "edilir.",
    zorluk="hard")

P.oncul("3568 s. Kanun m. 21, 25, 27, 35, 38, 39",
    "Oda ve Birlik kurullarının yapısına ilişkin aşağıdaki ifadeler verilmiştir:",
    ["Üye sayısı binin altındaki odalarda yönetim kurulu beş asıl ve beş yedek üyeden oluşur.",
     "Oda denetleme kurulu üç üye ve bir yedek üyeden oluşur.",
     "Birlik Denetleme Kurulu beş asıl ve beş yedek üyeden oluşur.",
     "Birlik Disiplin Kurulu dokuz asıl ve dokuz yedek üyeden oluşur."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve II",
    ["Yalnız I", "I ve II", "I ve IV", "II ve III", "I, II ve III"],
    "Kanun m. 21'e göre binin altındaki odalarda yönetim kurulu beş asıl beş yedek; m. 27'ye göre oda denetleme kurulu "
    "üç asıl bir yedek üyedir. Birlik Denetleme Kurulu üç asıl üç yedek (m. 39), Birlik Disiplin Kurulu beş asıl beş "
    "yedek (m. 38) üyeden oluşur.",
    zorluk="hard")

P.q("3568 s. Kanun m. 20",
    f"{K}, oda genel kurulunda başkanlık divanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Oda yönetim kurulu başkanı, yönetim ve denetleme kurulu üyeleri başkanlık divanına seçilemez.",
    ["Başkanlık divanına oda yönetim kurulu başkanı doğal başkan olarak katılır.",
     "Başkanlık divanı bir başkan ve bir kâtipten oluşur, seçim gizli oyla yapılır.",
     "Başkanlık divanı oda denetleme kurulu üyeleri arasından ad çekme yoluyla belirlenir.",
     "Başkanlık divanını oda yönetim kurulu toplantıdan önce kendi kararıyla belirler."],
    "Kanun m. 20'ye göre genel kurulda ilk iş olarak bir başkan, bir başkanvekili ve iki kâtip üyeden oluşan başkanlık "
    "divanı seçilir; seçim aksine karar yoksa işari oyla yapılır. Oda yönetim kurulu başkanı, yönetim ve denetleme "
    "kurulu üyeleri divana seçilemez.")

P.q("3568 s. Kanun m. 21",
    f"{K}, oda yönetim kurulunun toplu olarak görevden ayrılması ve yedeklerin de kalmaması hâlinde ne yapılır?",
    "Genel kurul olağanüstü toplanır ve kalan süre için seçim yapılır.",
    ["Birlik Yönetim Kurulu, yeni seçime kadar odayı yönetmek üzere geçici bir kurul atar.",
     "Oda denetleme kurulu, bir sonraki olağan genel kurula kadar yönetim kurulunun görevlerini üstlenir.",
     "Oda, en yakın odaya bağlanır ve olağan genel kurul toplantısına kadar faaliyetleri durdurulur.",
     "Hazine ve Maliye Bakanlığı odanın yönetimi için bir kayyum atar ve kayyum seçim yapar."],
    "Kanun m. 21'e göre yönetim kurulunun toplu olarak ayrılması veya asıl üye sayısının yarıdan aşağıya düşmesi ve "
    "yedeklerin de kalmaması hâlinde oda genel kurulu, oda denetçileri veya Bakan tarafından olağanüstü toplantıya "
    "çağrılır ve düşen kurulların süresini tamamlamak üzere seçim yapılır.")

P.q("3568 s. Kanun m. 23; SMMM Odaları Yön. m. 12",
    "Yeni seçilen oda yönetim kurulu, ilk toplantısında görev dağılımını yapmış ve dönem çalışma programını "
    f"hazırlamaktadır. {OY}, aşağıdakilerden hangisi oda yönetim kurulunun görevleri arasında yer almaz?",
    "Odanın yıllık üye aidatını tespit etmek",
    ["Odanın bütçe teklifini düzenleyip genel kurulun onayına sunmak",
     "Hakem ve bilirkişi listelerini hazırlamak",
     "Oda iç yönetmeliklerini hazırlayıp genel kurulun onayına sunmak",
     "Asgari ücret tarifesi önerisini her yıl Birliğe göndermek"],
    "Odalar Yönetmeliği m. 12'ye göre yönetim kurulu kayıt ücreti ve aidat tarifesini hazırlayarak genel kurula sunar ve "
    "Birliğe gönderir; aidatı kesin olarak tespit etmek Kanun m. 19/h'ye göre genel kurulun görevidir.")

P.q("SMMM Odaları Yön. m. 17 ve 18",
    "(X) Serbest Muhasebeci Mali Müşavirler Odasının denetleme kurulu, genel kurula sunacağı raporda odanın harcama ve "
    f"huzur hakkı uygulamalarını incelemektedir. {OY}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Harcamalar başkan veya başkan yardımcısı ile sekreterin müşterek imzasıyla yapılır.",
    ["Oda harcamaları, tutarı ne olursa olsun, yönetim kurulu başkanının tek imzasıyla yapılır.",
     "Oda kurulu üyelerine huzur hakkı verilmez; toplantılar gönüllülük esasına dayanır.",
     "Huzur hakkı miktarı Birlik Yönetim Kurulu tarafından bütün odalar için tek olarak belirlenir.",
     "Harcamalar denetleme kurulu başkanının önceden onay vermesiyle yapılabilir."],
    "Odalar Yönetmeliği m. 17'ye göre harcamalar yönetim kurulu başkanı veya başkan yardımcısı ile oda sekreterinin "
    "(sekreter yoksa muhasip üyenin) müşterek imzasıyla yapılır; m. 18'e göre kurul üyelerine huzur hakkı verilir ve "
    "miktarı bütçede oda genel kurulunca tespit edilir.")

P.sayisal("3568 s. Kanun m. 20/3; SMMM Odaları Yön. m. 9",
    f"{K}, oda yönetim kurulu başkanı, odaya kayıtlı üyelerin beşte birinin görüşme konularını belirten yazılı talebi üzerine genel kurulu en geç kaç gün içinde toplantıya çağırmak zorundadır?",
    "15", ["7", "10", "20", "30"],
    "Kanun m. 20 ve Odalar Yönetmeliği m. 9'a göre oda yönetim kurulu başkanı, üyelerin beşte birinin yazılı talebiyle "
    "en geç 15 gün içinde genel kurulu toplantıya çağırmak zorundadır.")

P.sayisal("3568 s. Kanun m. 34/3 (27.03.2025-7546 değişikliği)",
    f"{K}, Birlik Genel Kurul toplantısı ilk toplantı tarihinden en az kaç gün önce tirajı yüz binin üzerinde olan bir gazetede ilan edilir?",
    "20", ["7", "10", "15", "30"],
    "7546 sayılı Kanunla değişen m. 34'e göre Birlik Genel Kurul toplantısı ilk toplantı tarihinden en az yirmi gün önce "
    "tirajı yüz binin üzerindeki bir gazetede ilan edilir ve toplantı tarihine kadar Birliğin resmi internet sitesinde "
    "duyurulur.")

P.sayisal("3568 s. Kanun m. 40",
    f"{K}, oda ve Birlik seçimlerinde her kaç kişi için bir oy sandığı bulunur?",
    "400", ["100", "200", "250", "500"],
    "Kanun m. 40'a göre dört yüz kişiden fazla üye bulunması hâlinde her dört yüz kişi için bir oy sandığı bulunur ve her "
    "sandık için ayrı bir kurul oluşturulur.")

P.q("3568 s. Kanun m. 29; TÜRMOB Yön. m. 7",
    f"{TY}, aşağıdakilerden hangisi Birliğin görevleri arasında yer almaz?",
    "Meslek mensuplarının vergi beyannamelerini re'sen denetlemek",
    ["Odalar arasındaki mesleki anlaşmazlıkları çözümlemek",
     "Kanuna göre çıkarılacak yönetmelikleri hazırlamak",
     "Uluslararası standartlarla uyumlu mesleki etik ve denetim standartları oluşturmak",
     "Meslek mensuplarının sürekli eğitimini sağlamak"],
    "Kanun m. 29 ve TÜRMOB Yönetmeliği m. 7 Birliğin görevlerini sayar; odalar arası anlaşmazlıkları kesin çözmek, "
    "yönetmelik hazırlamak, standart oluşturmak ve sürekli eğitim bunlardandır. Beyannameleri re'sen denetlemek "
    "Birliğin görevi değildir.")

P.q("TÜRMOB Yön. m. 30-31",
    f"{TY}, Birlik Yönetim Kurulunun toplantılarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetim kurulu en az yedi üyenin katılmasıyla toplanır.",
    ["Olağan toplantılar, aksine karar alınmadıkça ayda bir gün yapılır.",
     "Oylarda eşitlik hâlinde başkanın bulunduğu taraf üstün tutulur.",
     "Ardı ardına üç olağan toplantıya katılmayan üye istifa etmiş sayılır.",
     "Yönetim kurulu toplantıları gizlidir."],
    "TÜRMOB Yönetmeliği m. 30'a göre yönetim kurulu en az beş üyenin katılmasıyla toplanır ve katılanların salt "
    "çoğunluğuyla karar verir. Aylık toplantı ve devamsızlık m. 31'de, gizlilik m. 32'de düzenlenmiştir.",
    zorluk="hard")

P.q("TÜRMOB Yön. m. 11",
    f"{TY}, serbest muhasebeci mali müşavir odalarının Birlik Genel Kurulu delegelerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Delegelerin en az yarısının serbest muhasebeci mali müşavir olması zorunludur.",
    ["Delegelerin tamamının yeminli mali müşavir olması zorunludur.",
     "Delegelerin en az üçte ikisinin oda yönetim kurulu üyesi olması zorunludur.",
     "Delegeler, oda genel kurulunca bir yıl için seçilir ve yeniden seçilemez.",
     "Delegelerin en az yarısının beş yıl kıdemli olması zorunludur."],
    "TÜRMOB Yönetmeliği m. 11'e göre SMMM odalarının delegelerinin en az yarısının serbest muhasebeci mali müşavir olması "
    "zorunludur; delegeler olağan genel kurulda üç yıl için seçilir ve yeniden seçilebilir.")

P.q("3568 s. Kanun m. 37 ve 38/4",
    "Birlik Disiplin Kurulu, bir oda disiplin kurulunun verdiği kınama cezasına karşı meslek mensubunun yaptığı itirazı "
    f"reddetmiştir. {K}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Birlik Disiplin Kurulunun itirazların reddine ait kararları Bakanlığın tasdiki ile kesinleşir.",
    ["Birlik Disiplin Kurulunun kararları Birlik Genel Kurulunun onayıyla kesinleşir.",
     "Birlik Yönetim Kurulu, üye tam sayısının üçte ikisinin katılmasıyla toplanır.",
     "Birlik Disiplin Kurulu, katılanların oybirliğiyle karar verir.",
     "Birlik Yönetim Kurulu üyeleri kendileriyle ilgili işlerin görüşülmesine katılabilir."],
    "Kanun m. 38'e göre Birlik Disiplin Kurulunun itirazların reddine ait kararları Bakanlığın tasdikiyle kesinleşir; "
    "kurul üye tam sayısının salt çoğunluğuyla toplanıp karar verir. M. 37'ye göre yönetim kurulu salt çoğunlukla "
    "toplanır ve üyeler ilgili oldukları işlerin görüşülmesine katılamaz.")

P.q("3568 s. Kanun m. 15/2",
    f"{K}, yeterli sayıda meslek mensubu bulunmayan ve oda kurulamayan yerlerle ilgili aşağıdakilerden hangisi doğrudur?",
    "En yakın odaya bağlanmasına veya bölge odası kurulmasına Birlik karar verir.",
    ["O yerdeki meslek mensupları dernek kurarak oda görevlerini yürütür.",
     "Vali, meslek mensuplarını il merkezindeki odaya bağlar.",
     "Meslek mensupları doğrudan TÜRMOB'a üye olur ve aidatlarını Birliğe öder.",
     "Oda kurulana kadar meslek mensupları mesleki faaliyette bulunamaz."],
    "Kanun m. 15/2'ye göre yeterli sayıda meslek mensubu bulunmayan yerlerin en yakın odaya bağlanmasına veya bölge "
    "odaları kurulmasına Birlikçe karar verilir ve bu karar Bakanlığa bildirilir.")

P.oncul("3568 s. Kanun m. 19 ve 33",
    "Aşağıdaki görevler verilmiştir:",
    ["Birlik temsilcilerini seçmek",
     "Uyulması mecburi mesleki kararları almak",
     "Yönetim kurulunun çalışma raporunu incelemek ve kabul etmek",
     "Odalardan alınacak pay miktarını tespit etmek"],
    f"{K}, yukarıdaki görevlerden hangileri oda genel kuruluna aittir?",
    "I ve III",
    ["Yalnız I", "I ve III", "II ve III", "II ve IV", "I, III ve IV"],
    "Kanun m. 19'a göre Birlik temsilcilerini seçmek ve yönetim kurulunun çalışma raporunu incelemek oda genel kurulunun "
    "görevidir. Mecburi mesleki kararları almak ve odalardan alınacak payı tespit etmek m. 33'e göre Birlik Genel "
    "Kurulunun görevidir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 22 ve 35",
    "Bir odada üst üste iki seçim döneminde iki defa yönetim kurulu başkanlığına seçilen (B), bir sonraki seçimde "
    f"yönetim kurulu üyeliğine aday olmak istemektedir. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Aradan iki seçim dönemi geçmedikçe yönetim kurulu üyeliğine seçilemez.",
    ["Başkan olarak değil, üye olarak hemen bir sonraki seçimde aday olabilir.",
     "Aradan bir seçim dönemi geçtikten sonra yeniden başkan seçilebilir.",
     "Oda genel kurulu izin verirse hemen bir sonraki seçimde aday olabilir.",
     "Ancak Birlik Yönetim Kurulu üyeliğine aday olabilir; oda yönetimine giremez."],
    "Kanun m. 22'ye göre odalarda üst üste iki seçim döneminde iki defa yönetim kurulu başkanlığına seçilmiş olanlar, "
    "aradan iki seçim dönemi geçmedikçe yönetim kurulu üyeliğine seçilemez. Aynı kural m. 35'te Birlik Yönetim Kurulu "
    "için de öngörülmüştür.")

P.q("3568 s. Kanun m. 25/2 ve 27",
    f"{K}, oda disiplin kurulu ve denetleme kurulu üyeliğine seçilmeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "En az üç yıl kıdem aranır; üyesi yüzden az odalarda bu şart aranmaz.",
    ["Kayıtlı olunan odada en az beş yıl kıdem aranır; bu şart istisnasız bütün odalar için geçerlidir.",
     "Kıdem aranmaz; ancak adayların yeminli mali müşavir olması zorunludur.",
     "Kayıtlı olunan odada en az on yıl kıdem ve fiilen mesleki faaliyet şartı aranır.",
     "Kayıtlı olunan odada en az iki yıl kıdem aranır; üye sayısı elliden az odalarda şart aranmaz."],
    "Kanun m. 25 ve 27'ye göre disiplin ve denetleme kurulu üyeleri, kayıtlı oldukları odada en az üç yıl kıdemli olup "
    "fiilen mesleki faaliyette bulunanlar arasından üç yıl için seçilir; üye sayısı yüzden az olan odalarda üç yıllık "
    "süre şartı aranmaz.")

P.q("3568 s. Kanun m. 32",
    f"{K}, Birlik Genel Kurulu temsilcilerinin seçimine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Temsilciler olağan oda genel kurulunda üç yıl için seçilir, yeniden seçilebilir.",
    ["Temsilciler Birlik Yönetim Kurulunca odaların önerisi üzerine iki yıl için atanır.",
     "Temsilciler oda yönetim kurulunca kendi üyeleri arasından bir yıl için seçilir.",
     "Temsilciler her yıl yapılan olağanüstü genel kurulda dört yıl için seçilir.",
     "Temsilciler oda disiplin kurulu üyeleri arasından ad çekme yoluyla belirlenir."],
    "Kanun m. 32'ye göre temsilciler her odanın olağan genel kurul toplantısında üç yıl için seçilir; yeniden seçilmek "
    "mümkündür.")

P.q("SMMM Odaları Yön. m. 14",
    f"{OY}, oda yönetim kurulu başkan ve üyelerinin görüşmelere katılma yasağı aşağıdaki kişilerden hangisini kapsamaz?",
    "Dördüncü derece kan hısımlarıyla ilgili işler",
    ["Kendileriyle ilgili işler",
     "Eşleriyle ilgili işler",
     "Üçüncü dereceye kadar kan hısımlarıyla ilgili işler",
     "İkinci dereceye kadar kayın hısımlarıyla ilgili işler"],
    "Odalar Yönetmeliği m. 14'e göre yönetim kurulu başkan ve üyeleri, üçüncü dereceye kadar kan ve ikinci dereceye kadar "
    "kayın hısımları, eşleri ve kendileri ile ilgili işlerin görüşülmesine ve soruşturmasına katılamaz. Dördüncü derece "
    "kan hısımlığı bu yasağın dışındadır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 34/2",
    f"{K}, Birlik Genel Kurulunun olağanüstü toplantıya çağrılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Temsilcilerin beşte birinin yazılı talebiyle toplantıya çağrılması mecburidir.",
    ["Olağanüstü toplantı ancak Hazine ve Maliye Bakanlığının istemiyle yapılabilir.",
     "Mevcut temsilcilerin üçte ikisinin yazılı talebiyle olağanüstü toplantı yapılabilir.",
     "Olağanüstü toplantı ancak odaların yarısının yönetim kurulu kararıyla istenebilir.",
     "Birlik Genel Kurulu olağanüstü toplanamaz; ihtiyaç olağan toplantıda görüşülür."],
    "Kanun m. 34/2'ye göre Birlik Yönetim Kurulu Başkanı, yönetim veya denetleme kurulunun gerekli gördüğü hallerde "
    "genel kurulu olağanüstü toplantıya çağırabilir; ayrıca mevcut temsilcilerin beşte birinin yazılı talebiyle "
    "çağrılması mecburidir.")

P.q("3568 s. Kanun m. 34/6; TÜRMOB Yön. m. 17",
    f"{TY}, Birlik Genel Kurulunda önceden bildirilen gündem dışında yeni konuların görüşülmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Genel kurul üyelerinin beşte ikisinin imzasıyla teklif edilen konular gündeme ilave edilir.",
    ["Toplantıda hazır bulunanların salt çoğunluğunun sözlü talebiyle her konu gündeme alınır.",
     "Gündem dışı konular ancak Birlik Yönetim Kurulunun önceden onayıyla görüşülebilir.",
     "Genel kurul üyelerinin üçte birinin imzasıyla teklif edilen konular gündeme ilave edilir.",
     "Gündeme madde eklenemez; yeni konular bir sonraki olağan genel kurul toplantısında görüşülür."],
    "Kanun m. 34 ve TÜRMOB Yönetmeliği m. 17'ye göre genel kurul üyelerinin beşte ikisinin imzasıyla teklif edilen "
    "konular gündeme ilave edilir; toplantıda hazır bulunanların beşte birinin imzasıyla da gündeme yeni madde ilavesi "
    "teklif edilebilir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 40",
    f"{K}, seçimlerde oyların kullanılmasına ve tahsise ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üye listesinde adı bulunmayan meslek mensubu, oda kimliğini göstererek oy kullanabilir.",
    ["Oy verme işlemi gizli oy açık tasnif esasına göre yapılır.",
     "Üyeler bağımsız aday olabileceği gibi grup listelerinden de aday olabilir.",
     "Mühürsüz oy pusulası ve zarfla kullanılan oylar geçersiz sayılır.",
     "Son kalan üyelik için oylar eşitse tahsis ad çekme yoluyla yapılır."],
    "Kanun m. 40'a göre üye listesinde adı yazılı bulunmayan meslek mensubu oy kullanamaz. Gizli oy açık tasnif, bağımsız "
    "ve grup adaylığı, mühürsüz pusulanın geçersizliği ve eşitlikte ad çekme aynı maddededir.")

P.q("3568 s. Kanun m. 15/4",
    "Serbest muhasebeci mali müşavir ruhsatı alan (C), hiçbir odaya kaydolmadan bir müşterinin defterlerini tutmaya "
    f"başlamıştır. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Odaya üye olmayan meslek mensubu mesleki faaliyette bulunamaz; kayıt şarttır.",
    ["Ruhsat sahibi olduğu için odaya kaydı, ilk genel kurula kadar ertelenebilir.",
     "Odaya kayıt ihtiyari olup oda hizmetlerinden yararlanmak için gereklidir.",
     "Odaya kaydolmadan bir yıl süreyle deneme amaçlı faaliyette bulunabilir.",
     "Kayıt yükümlülüğü ortaklık bürosu veya şirket kuranlar için öngörülmüştür."],
    "Kanun m. 15'e göre odalara üye olmayan meslek mensupları mesleki faaliyette bulunamaz; Odalar Yönetmeliği m. 34 de "
    "ruhsat alan her meslek mensubunun odaya kaydolmak zorunda olduğunu hükme bağlar.")

if __name__ == "__main__":
    sys.exit(P.yaz())
