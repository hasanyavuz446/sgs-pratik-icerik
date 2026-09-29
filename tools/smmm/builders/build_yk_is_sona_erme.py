# -*- coding: utf-8 -*-
"""Hukuk · İş Hukuku · İş Sözleşmesinin Sona Ermesi — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında sona erme soruları bildirim süresi, toplu işçi çıkarma bildirimi, yeni iş arama
izni gibi süre ve sayı soran kısa köklerle; işe iade ve haklı fesih ise "hangisi yanlıştır" kalıbıyla gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 4857 sayılı İş Kanunu md. 17-21, 24-27, 29 (7036 sayılı
Kanunla değişik arabuluculuk hükümleri dahil).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_is_sozlesmesinin_sona_ermesi_yeterlilik_2026.json", lesson="is_hukuku",
          topic="is_sozlesmesinin_sona_ermesi_yeterlilik", konu_adi="İş Sözleşmesinin Sona Ermesi", seed=2026093004,
          surum="4857 sayılı İş Kanunu güncel metni (7036 s. Kanun değişikliği dahil); 29.09.2026 kontrolü")

K = "4857 sayılı İş Kanunu’na göre"
K26 = "4857 sayılı İş Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İK md. 17",
    "İşyerinde dört aydır belirsiz süreli iş sözleşmesiyle çalışan işçinin sözleşmesi bildirimli olarak feshedilecektir."
    f"\n\n{K}, sözleşme bildirimin karşı tarafa yapılmasından kaç hafta sonra feshedilmiş sayılır?",
    "2", ["1", "4", "6", "8"],
    "Md. 17'ye göre işi altı aydan az sürmüş işçi için sözleşme, bildirimin diğer tarafa yapılmasından başlayarak iki hafta "
    "sonra feshedilmiş sayılır.", zorluk="easy")

P.q("İK md. 17",
    f"{K}, belirsiz süreli iş sözleşmesinin bildirimli feshine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bildirim süreleri sözleşmeyle kısaltılabilir.",
    ["Bildirim süreleri asgari sürelerdir.",
     "İşveren bildirim ücretini peşin ödeyerek feshedebilir.",
     "Bildirime uymayan taraf tazminat öder.",
     "Tazminatta ücret ekleri de dikkate alınır."],
    "Md. 17'ye göre bildirim süreleri asgari olup sözleşmelerle artırılabilir; kısaltılamaz.", zorluk="easy")

P.q("İK md. 17",
    f"{K}, bildirim süresine ait ücretin peşin ödenerek sözleşmenin feshedilmesi hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "İş güvencesi hükümlerini engellemez.",
    ["Feshi tek başına geçerli kılar.",
     "İşçinin işe iade hakkını ortadan kaldırır.",
     "Sadece işçi tarafından yapılabilir.",
     "Bildirim tazminatını ikiye katlar."],
    "Md. 17'ye göre işverenin bildirim şartına uymaması veya bildirim ücretini peşin ödeyerek feshetmesi md. 18-21'deki iş "
    "güvencesi hükümlerinin uygulanmasına engel olmaz.")

P.sayisal("İK md. 17",
    "İşyerinde iki yıldır belirsiz süreli iş sözleşmesiyle çalışan işçinin sözleşmesi işverence bildirimli olarak "
    f"feshedilecektir.\n\n{K}, işverenin uyması gereken asgari bildirim süresi kaç haftadır?",
    "6", ["2", "4", "8", "10"],
    "Md. 17'ye göre işi bir buçuk yıldan üç yıla kadar sürmüş işçi için bildirim süresi altı haftadır.")

P.q("İK md. 18",
    f"{K}, aşağıdakilerden hangisi fesih için geçerli bir sebep oluşturabilir?",
    "Yeterliliğe dayalı sebepler",
    ["Sendika üyeliği",
     "İşveren aleyhine idari makama başvurmak",
     "Hamilelik ve doğum",
     "Analık izni süresinde işe gelmemek"],
    "Md. 18'e göre işçinin yeterliliğinden veya davranışlarından ya da işletmenin gereklerinden kaynaklanan sebepler geçerli "
    "sebeptir; sendika üyeliği, idari başvuru, hamilelik ve analık izni devamsızlığı geçerli sebep oluşturmaz.", zorluk="easy")

P.oncul("İK md. 18",
    f"{K} aşağıdaki hususlar değerlendirilmektedir:",
    ["İşyeri sendika temsilciliği yapmak",
     "İşin gereklerinden kaynaklanan küçülme",
     "Medeni hâl ve aile yükümlülükleri",
     "Hastalık nedeniyle bekleme süresinde geçici devamsızlık"],
    "Yukarıdakilerden hangileri fesih için geçerli sebep oluşturmaz?",
    "I, III ve IV",
    ["I ve II", "II ve III", "I ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 18'e göre sendika temsilciliği (I), medeni hâl ve aile yükümlülükleri (III) ve bekleme süresindeki hastalık "
    "devamsızlığı (IV) geçerli sebep oluşturmaz; işin gereklerinden kaynaklanan küçülme (II) geçerli sebep olabilir.",
    zorluk="hard")

P.sayisal("İK md. 17",
    f"{K}, işi üç yıldan fazla sürmüş işçi için belirsiz süreli iş sözleşmesinin feshinde asgari bildirim süresi kaç "
    "haftadır?",
    "8", ["4", "6", "10", "12"],
    "Md. 17'ye göre işi üç yıldan fazla sürmüş işçi için sözleşme, bildirim yapılmasından başlayarak sekiz hafta sonra "
    "feshedilmiş sayılır; bu süreler asgari olup sözleşmelerle artırılabilir.", zorluk="easy")

P.q("İK md. 18",
    f"{K}, iş güvencesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kıdemde sadece son işyeri esas alınır.",
    ["Yer altı işçilerinde kıdem şartı aranmaz.",
     "Aynı işkolundaki işyerlerinin işçi sayısı birleştirilir.",
     "Belirsiz süreli sözleşmeler için uygulanır.",
     "İşletmenin bütününü yöneten işveren vekiline uygulanmaz."],
    "Md. 18'e göre işçinin altı aylık kıdemi aynı işverenin bir veya değişik işyerlerinde geçen süreler birleştirilerek hesap "
    "edilir.")

P.q("İK md. 18",
    f"{K}, aşağıdakilerden hangisi iş güvencesi hükümlerinden yararlanamaz?",
    "İşe alma-çıkarma yetkili işyeri yöneticisi",
    ["Otuz işçili işyerinde yedi aylık kıdemli işçi",
     "Yer altında iki aydır çalışan maden işçisi",
     "Sendika temsilcisi olan belirsiz süreli işçi",
     "Hamile olan belirsiz süreli kadın işçi"],
    "Md. 18'e göre işyerinin bütününü sevk ve idare eden ve işçiyi işe alma ve işten çıkarma yetkisi bulunan işveren "
    "vekilleri hakkında md. 18, 19 ve 21 uygulanmaz.", zorluk="hard")

it = 1_000 * 7 * 8
P.sayisal("İK md. 17",
    "İşveren, beş yıldır çalışan işçinin belirsiz süreli iş sözleşmesini bildirim süresine uymadan feshetmiştir. İşçinin "
    f"ücret ve para ile ölçülebilen menfaatleri dahil günlük ücreti 1.000 ₺’dir.\n\n{K}, işverenin ödemesi gereken "
    "bildirim tazminatı kaç ₺’dir?",
    tl(it), secenekler(it, 42_000, 28_000, 60_000, 30_000),
    "Md. 17'ye göre üç yıldan fazla kıdemli işçi için bildirim süresi sekiz haftadır; bildirime uymayan taraf bu süreye ilişkin "
    "ücret tutarında tazminat öder: 8 × 7 × 1.000 = 56.000 ₺.", zorluk="hard")

P.q("İK md. 19",
    f"{K}, işverenin fesih usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fesih bildirimi sözlü olarak da yapılabilir.",
    ["Fesih sebebi açık ve kesin belirtilmelidir.",
     "Davranışa dayalı fesihte savunma alınmalıdır.",
     "Verime dayalı fesihte savunma alınmalıdır.",
     "Md. 25/II’ye dayalı fesih hakkı saklıdır."],
    "Md. 19'a göre işveren fesih bildirimini yazılı yapmak ve fesih sebebini açık ve kesin belirtmek zorundadır; davranış veya "
    "verime dayalı fesihten önce işçinin savunması alınır.", zorluk="easy")

P.q("İK md. 20",
    f"{K}, işe iade davasında feshin geçerli bir sebebe dayandığını ispat yükü kime aittir?",
    "İşverene",
    ["İşçiye", "Arabulucuya", "Mahkemeye", "Sendikaya"],
    "Md. 20'ye göre feshin geçerli bir sebebe dayandığını ispat yükümlülüğü işverene aittir; işçi feshin başka bir sebebe "
    "dayandığını iddia ederse bunu ispatla yükümlüdür.", zorluk="easy")

P.sayisal("İK md. 17",
    "Yirmi işçi çalıştıran bir işyerinde iki yıllık kıdemi olan işçinin sözleşmesi, fesih hakkı kötüye kullanılarak ve "
    f"bildirim süresine uyularak feshedilmiştir.\n\n{K}, işçiye kaç haftalık ücret tutarında kötüniyet tazminatı "
    "ödenir?",
    "18", ["6", "12", "24", "32"],
    "Md. 17'ye göre iş güvencesi kapsamı dışında kalan işçinin sözleşmesi fesih hakkı kötüye kullanılarak feshedilirse "
    "bildirim süresinin üç katı tutarında tazminat ödenir: 6 hafta × 3 = 18 haftalık ücret.", zorluk="hard")

P.q("İK md. 20",
    f"{K}, işe iade uyuşmazlığına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Doğrudan açılan dava esastan incelenir.",
    ["Taraflar anlaşırsa özel hakeme gidilebilir.",
     "Dava ivedilikle sonuçlandırılır.",
     "Bölge adliye mahkemesi kararı kesindir.",
     "Usulden ret kararı resen tebliğ edilir."],
    "Md. 20'ye göre arabulucuya başvurmaksızın doğrudan açılan dava usulden reddedilir; kesinleşen ret kararının resen "
    "tebliğinden itibaren iki hafta içinde arabulucuya başvurulabilir.")

P.q("İK md. 20",
    "İşçi, arabulucuya başvurmadan doğrudan işe iade davası açmış ve dava usulden reddedilmiştir; ret kararı kesinleşerek "
    f"resen tebliğ edilmiştir.\n\n{K}, işçi bu durumda ne yapabilir?",
    "İki hafta içinde arabulucuya başvurabilir.",
    ["Bir yıl içinde yeniden dava açabilir.",
     "Arabulucuya başvurma hakkı düşmüştür.",
     "Sadece Yargıtay'a başvurabilir.",
     "Otuz gün içinde doğrudan yeniden dava açabilir."],
    "Md. 20'ye göre arabulucuya başvurmaksızın açılan davanın usulden reddi hâlinde, kesinleşen ret kararının resen "
    "tebliğinden itibaren iki hafta içinde arabulucuya başvurulabilir.", zorluk="hard")

P.sayisal("İK md. 18",
    f"{K}, iş güvencesi hükümlerinin uygulanması için işyerinde en az kaç işçi çalışıyor olmalıdır?",
    "30", ["10", "20", "50", "100"],
    "Md. 18'e göre otuz veya daha fazla işçi çalıştıran işyerlerinde en az altı aylık kıdemi olan işçinin belirsiz süreli "
    "sözleşmesini fesheden işveren geçerli bir sebebe dayanmak zorundadır.", zorluk="easy")

P.q("İK md. 21",
    f"{K}, geçersiz feshin sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu hükümler sözleşmeyle işçi aleyhine değiştirilebilir.",
    ["İşe başlatılan işçiye ödenen kıdem tazminatı mahsup edilir.",
     "Tazminat, dava tarihindeki ücret esas alınarak belirlenir.",
     "Mahkeme işe başlatmama tazminatını da belirler.",
     "Bildirim ücreti ödenmemişse ayrıca ödenir."],
    "Md. 21'e göre maddenin birinci, ikinci ve üçüncü fıkra hükümleri sözleşmelerle hiçbir suretle değiştirilemez; aksi yöndeki "
    "sözleşme hükümleri geçersizdir.")

P.q("İK md. 21",
    "İşe iade kararı kesinleşmiş ve işçiye tebliğ edilmiştir. İşçi on iş günü içinde işverene başvurmamıştır."
    f"\n\n{K}, bu durumun sonucu aşağıdakilerden hangisidir?",
    "Fesih geçerli sayılır.",
    ["İşveren işe başlatmama tazminatını öder.",
     "Süre, işçinin talebiyle bir ay uzar.",
     "İşçi dört aylık boşta geçen süre ücretini kaybetmez.",
     "Karar hükümsüz olur ve yeniden dava açılır."],
    "Md. 21'e göre işçi süresinde başvurmazsa işverence yapılan fesih geçerli bir fesih sayılır ve işveren sadece bunun hukuki "
    "sonuçlarıyla sorumlu olur.", zorluk="hard")

P.sayisal("İK md. 18",
    f"{K}, yer altı işlerinde çalışmayan işçinin iş güvencesinden yararlanabilmesi için en az kaç aylık kıdemi "
    "olmalıdır?",
    "6", ["1", "3", "4", "12"],
    "Md. 18'e göre iş güvencesi için işçinin en az altı aylık kıdemi olmalıdır; yer altı işlerinde çalışan işçilerde kıdem şartı "
    "aranmaz.")

P.q("İK md. 21",
    f"{K}, işe başlatma konusunda arabuluculuk faaliyetinde anlaşan tarafların belirlemesi zorunlu hususlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Kıdem tazminatının faiz oranı",
    ["İşe başlatma tarihi",
     "Boşta geçen süre ücretinin miktarı",
     "İşe başlatmama tazminatının miktarı",
     "Diğer hakların parasal miktarı"],
    "Md. 21'e göre arabuluculukta işe başlatma konusunda anlaşan taraflar işe başlatma tarihini, boşta geçen süre ücret ve "
    "diğer haklarının miktarını ve işe başlatmama tazminatının miktarını belirlemek zorundadır.", zorluk="hard")

P.q("İK md. 24",
    f"{K}, aşağıdakilerden hangisi işçiye iş sözleşmesini haklı nedenle derhal fesih hakkı vermez?",
    "İşverenin işyerini başka bir ile taşıma kararı",
    ["Ücretin sözleşmeye uygun ödenmemesi",
     "İşverenin işçiye cinsel tacizde bulunması",
     "İşin işçinin sağlığı için tehlikeli olması",
     "İşyerinde işin bir haftadan fazla durması"],
    "Md. 24'e göre sağlık sebepleri, ahlak ve iyiniyet kurallarına uymayan hâller (ücretin ödenmemesi, taciz vb.) ve bir "
    "haftadan fazla işi durduran zorlayıcı sebepler işçiye derhal fesih hakkı verir; işyerinin taşınması bu hâllerden "
    "değildir.")

P.sayisal("İK md. 20",
    "İşçi, fesih bildiriminde gösterilen sebebin geçerli olmadığını ileri sürerek işe iade talep etmek istemektedir."
    f"\n\n{K}, işçi fesih bildiriminin tebliğinden itibaren en geç kaç ay içinde arabulucuya başvurmalıdır?",
    "1", ["2", "3", "4", "6"],
    "Md. 20'ye göre işçi fesih bildiriminin tebliği tarihinden itibaren bir ay içinde işe iade talebiyle arabulucuya başvurmak "
    "zorundadır.")

P.q("İK md. 24",
    f"{K}, işçinin haklı nedenle derhal fesih hakkına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu hak sadece belirsiz süreli sözleşmelerde kullanılabilir.",
    ["Başka işçinin tacizine önlem alınmaması bir nedendir.",
     "Parça başı işte az iş verilip fark ödenmemesi bir nedendir.",
     "İşverenin işçiyi yanıltması bir nedendir.",
     "İşverenin aile üyelerine sataşması bir nedendir."],
    "Md. 24'e göre süresi belirli olsun veya olmasın işçi, sayılan hâllerde sözleşmeyi sürenin bitiminden önce veya bildirim "
    "süresini beklemeksizin feshedebilir.")

P.q("İK md. 25",
    f"{K}, aşağıdakilerden hangisi işverene ahlak ve iyiniyet kurallarına uymayan hâl nedeniyle derhal fesih hakkı "
    "vermez?",
    "İşçinin bir kez beş dakika geç kalması",
    ["İşçinin işverenin başka işçisini taciz etmesi",
     "İşyerine sarhoş gelmesi",
     "Meslek sırlarını ortaya atması",
     "Görevini yapmamakta ısrar etmesi"],
    "Md. 25/II'ye göre taciz, işyerine sarhoş gelme, meslek sırlarını açıklama ve hatırlatılan görevi yapmamakta ısrar derhal "
    "fesih sebebidir; tek seferlik kısa gecikme bu hâllerden değildir.", zorluk="easy")

P.sayisal("İK md. 20",
    "İşe iade talebiyle yürütülen arabuluculuk faaliyeti sonunda anlaşmaya varılamamış ve son tutanak düzenlenmiştir."
    f"\n\n{K}, son tutanağın düzenlendiği tarihten itibaren kaç hafta içinde iş mahkemesinde dava açılabilir?",
    "2", ["1", "3", "4", "6"],
    "Md. 20'ye göre arabuluculuk faaliyeti sonunda anlaşmaya varılamazsa son tutanağın düzenlendiği tarihten itibaren iki "
    "hafta içinde iş mahkemesinde dava açılabilir; taraflar anlaşırsa özel hakeme de gidilebilir.")

P.q("İK md. 25",
    f"{K}, işverenin haklı nedenle derhal fesih hakkına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşyerinde hapis gerektiren her suç derhal fesih sebebidir.",
    ["Gözaltı devamsızlığı bildirim süresini aşarsa fesih hakkı doğar.",
     "Makineleri otuz günlük ücretle ödenemeyecek zarara uğratmak nedendir.",
     "İşçinin işvereni yanıltması bir nedendir.",
     "İşçi feshe karşı yargı yoluna başvurabilir."],
    "Md. 25/II-f'ye göre işçinin işyerinde yedi günden fazla hapisle cezalandırılan ve cezası ertelenmeyen bir suç işlemesi "
    "derhal fesih sebebidir; her suç bu niteliği taşımaz.", zorluk="hard")

P.q("İK md. 25",
    "İşçi Bay (A), işyeri dışında işlediği iddia edilen bir suç nedeniyle tutuklanmış ve işe gelememektedir."
    f"\n\n{K}, işverenin bu nedenle derhal fesih hakkı ne zaman doğar?",
    "Devamsızlık bildirim süresini aşınca",
    ["Tutuklandığı gün",
     "Kesin mahkûmiyet hükmüyle",
     "Devamsızlık üç iş gününü aşınca",
     "Tutukluluk bir yılı aşınca"],
    "Md. 25/IV'e göre işçinin gözaltına alınması veya tutuklanması hâlinde devamsızlığın md. 17'deki bildirim süresini aşması "
    "işverene derhal fesih hakkı verir.")

P.sayisal("İK md. 21",
    f"{K}, feshin geçersizliğine karar verilmesi hâlinde işveren, işçiyi başvurusu üzerine en geç kaç ay içinde işe "
    "başlatmalıdır?",
    "1", ["2", "3", "4", "6"],
    "Md. 21'e göre işveren işçiyi başvurusu üzerine bir ay içinde işe başlatmazsa işçiye işe başlatmama tazminatı öder.")

P.q("İK md. 25",
    f"{K}, işçinin kendi kastından doğan hastalığı nedeniyle işverenin derhal fesih hakkına ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Ardı ardına üç iş günü aşılmalıdır.",
    ["Devamsızlık bir haftayı aşmalıdır.",
     "Sağlık kurulu raporu şarttır.",
     "Devamsızlık süresine bakılmaz.",
     "Bildirim süresinin iki katı beklenir."],
    "Md. 25/I-a'ya göre işçinin kendi kastından veya düzensiz yaşayışından doğan hastalık nedeniyle devamsızlığın ardı ardına "
    "üç iş günü veya bir ayda beş iş gününden fazla sürmesi işverene derhal fesih hakkı verir.", zorluk="hard")

P.q("İK md. 26",
    f"{K}, ahlak ve iyiniyet kurallarına dayanan derhal fesih hakkının kullanım süresine ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Maddi çıkarda altı iş günü uygulanmaz.",
    ["Süre öğrenme gününden başlar.",
     "Fiilden itibaren bir yıl geçince hak kullanılamaz.",
     "Maddi çıkar hâlinde bir yıllık süre uygulanmaz.",
     "Süresinde feshedenin tazminat hakları saklıdır."],
    "Md. 26'ya göre işçinin olayda maddi çıkar sağlaması hâlinde uygulanmayan süre bir yıllık süredir; altı iş günlük süre "
    "işlemeye devam eder.", zorluk="hard")

P.sayisal("İK md. 21",
    f"{K}, feshin geçersizliğine karar verilen işçi işe başlatılmazsa ödenecek tazminat en çok kaç aylık ücreti "
    "tutarındadır?",
    "8", ["4", "6", "10", "12"],
    "Md. 21'e göre işçiyi bir ay içinde işe başlatmayan işveren en az dört, en çok sekiz aylık ücreti tutarında tazminat "
    "ödemekle yükümlüdür.")

P.q("İK md. 27",
    f"{K}, yeni iş arama iznine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İzin süresi için ücretten kesinti yapılabilir.",
    ["İzin iş saatleri içinde verilir.",
     "İşçi isterse izin saatlerini toplu kullanabilir.",
     "Toplu izin işten ayrılmadan önceki günlere denk getirilir.",
     "Eksik kullandırılan iznin ücreti ödenir."],
    "Md. 27'ye göre işveren iş arama iznini iş saatleri içinde ve ücret kesintisi yapmadan vermeye mecburdur.", zorluk="easy")

P.q("İK md. 29",
    f"{K}, toplu işçi çıkarmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Fesih bildirimleri tebliğ günü hüküm doğurur.",
    ["Bildirim sendika temsilcilerine de yapılır.",
     "Bildirimde etkilenecek işçi sayısı gösterilir.",
     "Görüşmeler sonunda bir belge düzenlenir.",
     "Mevsim işlerinde bu hükümler uygulanmaz."],
    "Md. 29'a göre fesih bildirimleri işverenin toplu işçi çıkarma isteğini bölge müdürlüğüne bildirmesinden otuz gün sonra "
    "hüküm doğurur.")

P.sayisal("İK md. 21",
    f"{K}, feshin geçersizliği kararı kesinleşinceye kadar çalıştırılmadığı süre için işçiye en çok kaç aya kadar doğmuş "
    "ücret ve diğer hakları ödenir?",
    "4", ["2", "3", "6", "8"],
    "Md. 21'e göre kararın kesinleşmesine kadar çalıştırılmadığı süre için işçiye en çok dört aya kadar doğmuş bulunan ücret "
    "ve diğer hakları ödenir.", zorluk="hard")

P.q("İK md. 29",
    f"{K}, işyerinin bütünüyle kapatılarak faaliyete kesin ve devamlı olarak son verilmesi hâlinde işverenin "
    "yükümlülüğü aşağıdakilerden hangisidir?",
    "Durumu otuz gün önceden bildirmek ve ilan etmek",
    ["Sendikayla görüşme yapıp belge düzenlemek",
     "Bakanlıktan kapatma izni almak",
     "İşçilerin tamamına sekiz aylık tazminat ödemek",
     "Kapanıştan sonra altı ay içinde bildirimde bulunmak"],
    "Md. 29'a göre işyerinin bütünüyle kapatılması hâlinde işveren sadece durumu en az otuz gün önceden bölge müdürlüğüne ve "
    "Türkiye İş Kurumuna bildirmek ve işyerinde ilan etmekle yükümlüdür.")

P.q("İK md. 29",
    "Bir işveren toplu işçi çıkarmayı tamamlamış, dört ay sonra aynı nitelikteki iş için yeniden işçi almak istemiştir."
    f"\n\n{K}, işveren bu durumda ne yapmalıdır?",
    "Uygun eski işçileri tercihen çağırmalıdır.",
    ["Sadece yeni işçi almalıdır.",
     "Bakanlıktan izin almalıdır.",
     "Eski işçilere kıdem tazminatını iade ettirmelidir.",
     "Altı ay dolmadan işçi alamaz."],
    "Md. 29'a göre işveren toplu işçi çıkarmanın kesinleşmesinden itibaren altı ay içinde aynı nitelikteki iş için yeniden "
    "işçi almak isterse nitelikleri uygun olanları tercihen işe çağırır.")

P.sayisal("İK md. 21",
    f"{K}, işe iade kararı kesinleşen işçi, kararın tebliğinden itibaren kaç iş günü içinde işe başlamak için işverene "
    "başvurmalıdır?",
    "10", ["3", "6", "15", "30"],
    "Md. 21'e göre işçi kesinleşen kararın tebliğinden itibaren on iş günü içinde işverene başvurmak zorundadır; başvurmazsa "
    "fesih geçerli sayılır.")

P.q("İK md. 29",
    f"{K}, toplu işçi çıkarma bildiriminin yapılacağı merciler arasında aşağıdakilerden hangisi yer alır?",
    "Türkiye İş Kurumu",
    ["Ticaret sicili müdürlüğü", "Vergi dairesi", "Sosyal Güvenlik Kurumu", "İşyerinin bağlı olduğu belediye"],
    "Md. 29'a göre toplu işçi çıkarma bildirimi işyeri sendika temsilcilerine, ilgili bölge müdürlüğüne ve Türkiye İş Kurumuna "
    "yapılır.", zorluk="easy")

P.q("İK md. 17",
    f"{K}, iş güvencesi kapsamı dışında kalan işçinin sözleşmesinin fesih hakkı kötüye kullanılarak feshedilmesi "
    "hâlinde aşağıdakilerden hangisi doğrudur?",
    "Bildirim süresinin üç katı tazminat ödenir.",
    ["İşçi işe iade davası açabilir.",
     "Bildirim süresi kadar tazminat ödenir.",
     "Sekiz aylık ücret tutarında tazminat ödenir.",
     "Sadece manevi tazminat istenebilir."],
    "Md. 17'ye göre iş güvencesi dışındaki işçinin sözleşmesi fesih hakkı kötüye kullanılarak sona erdirilirse bildirim "
    "süresinin üç katı tutarında tazminat ödenir; bildirime de uyulmamışsa ayrıca bildirim tazminatı gerekir.")

P.sayisal("İK md. 26",
    "İşveren, işçinin hırsızlık yaptığını öğrenmiş; olayda işçinin maddi çıkar sağlamadığı anlaşılmıştır."
    f"\n\n{K}, işveren derhal fesih hakkını öğrenmeden itibaren kaç iş günü içinde kullanmalıdır?",
    "6", ["3", "10", "15", "30"],
    "Md. 26'ya göre ahlak ve iyiniyet kurallarına uymayan hâllere dayanan fesih yetkisi, öğrenmeden itibaren altı iş günü "
    "geçtikten ve her hâlde fiilden itibaren bir yıl sonra kullanılamaz; işçi maddi çıkar sağlamışsa bir yıllık süre "
    "uygulanmaz.")

P.q("İK md. 18",
    "Bir işverenin aynı işkolunda iki işyeri vardır: birinde 18, diğerinde 15 işçi çalışmaktadır. Yedi aylık kıdemli ve "
    f"belirsiz süreli işçinin sözleşmesi feshedilecektir.\n\n{K}, iş güvencesi hükümlerinin uygulanması bakımından "
    "aşağıdakilerden hangisi doğrudur?",
    "Toplam 33 işçi esas alınır; iş güvencesi uygulanır.",
    ["Sadece işçinin işyerindeki sayı esas alınır.",
     "İşyerleri ayrı olduğundan iş güvencesi uygulanmaz.",
     "Otuzun altındaki işyerinde güvence aranmaz.",
     "İşçi sayısı ortalaması alınır ve güvence uygulanmaz."],
    "Md. 18'e göre işverenin aynı işkolunda birden fazla işyeri varsa işçi sayısı bu işyerlerindeki toplam işçi sayısına göre "
    "belirlenir: 18 + 15 = 33 ≥ 30.", zorluk="hard")

P.q("İK md. 20",
    f"{K}, işe iade uyuşmazlığında özel hakeme gidilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Taraflar anlaşırsa gidilebilir.",
    ["İşverenin tek taraflı talebiyle gidilir.",
     "Arabuluculuktan önce gidilmesi şarttır.",
     "Sadece kamu işyerlerinde mümkündür.",
     "Özel hakem kararı istinafa tabidir."],
    "Md. 20'ye göre arabuluculukta anlaşma sağlanamazsa taraflar anlaşarak uyuşmazlığı aynı sürede iş mahkemesi yerine özel "
    "hakeme götürebilir.")

P.sayisal("İK md. 27",
    f"{K}, bildirim süresi içinde işçiye verilecek yeni iş arama izni günde en az kaç saattir?",
    "2", ["1", "3", "4", "5"],
    "Md. 27'ye göre bildirim süreleri içinde işveren işçiye iş saatleri içinde ve ücret kesintisi yapmadan yeni iş arama izni "
    "vermeye mecburdur; bu süre günde iki saatten az olamaz.", zorluk="easy")

P.q("İK md. 25",
    f"{K}, aşağıdakilerden hangisi işverene zorlayıcı sebeple derhal fesih hakkı verir?",
    "Bir haftadan uzun süren zorlayıcı sebep",
    ["İşyerinde bir günlük elektrik kesintisi",
     "İşçinin iki gün süren hafif hastalığı",
     "İşçinin yıllık izne çıkması",
     "İşverenin ekonomik durumunun bozulması"],
    "Md. 25/III'e göre işçiyi işyerinde bir haftadan fazla süreyle çalışmaktan alıkoyan zorlayıcı bir sebebin ortaya çıkması "
    "işverene derhal fesih hakkı verir.")

P.q("İK md. 24",
    f"{K}, aşağıdakilerden hangisi işçiye sağlık sebebiyle derhal fesih hakkı verir?",
    "Görüştüğü işçinin bulaşıcı hastalığı",
    ["İşverenin ücret artışı yapmaması",
     "İşçinin kendi isteğiyle hastane değiştirmesi",
     "İşyerinde yeni bir vardiya düzeni kurulması",
     "İşçinin başka ile taşınmak istemesi"],
    "Md. 24/I-b'ye göre işçinin sürekli olarak yakından ve doğrudan görüştüğü işveren veya başka bir işçinin bulaşıcı ya da "
    "işçinin işiyle bağdaşmayan bir hastalığa tutulması işçiye derhal fesih hakkı verir.")

ia = 400 * 2 * 2
P.sayisal("İK md. 27",
    "Saat ücreti 400 ₺ olan işçi, kendisine verilmesi gereken iki saatlik iş arama izni sırasında işveren tarafından "
    f"çalıştırılmıştır.\n\n{K}, işveren bu iki saat için izin ücretine ek olarak kaç ₺ ödemelidir?",
    tl(ia), secenekler(ia, 800, 1_200, 2_400, 400),
    "Md. 27'ye göre işveren iş arama izni esnasında işçiyi çalıştırırsa, izin ücretine ilaveten çalıştırdığı sürenin ücretini "
    "yüzde yüz zamlı öder: 400 × 2 × 2 = 1.600 ₺.", zorluk="hard")

P.q("İK md. 19",
    "İşveren, işçinin verimsizliği gerekçesiyle belirsiz süreli iş sözleşmesini feshetmek istemektedir; işçinin iş "
    f"güvencesi vardır.\n\n{K}, fesihten önce aşağıdakilerden hangisi yapılmalıdır?",
    "İşçinin iddialara karşı savunması alınmalıdır.",
    ["Bölge müdürlüğünden izin alınmalıdır.",
     "Sendikanın görüşü alınmalıdır.",
     "İşçiye iki aylık ücret peşin ödenmelidir.",
     "Noter aracılığıyla ihtar çekilmelidir."],
    "Md. 19'a göre hakkındaki iddialara karşı savunması alınmadan bir işçinin belirsiz süreli sözleşmesi davranışı veya verimi "
    "ile ilgili nedenlerle feshedilemez.")

P.sayisal("İK md. 29",
    "Bir işyerinde 250 işçi çalışmaktadır ve işveren ekonomik nedenlerle işçi çıkarmayı planlamaktadır."
    f"\n\n{K}, bir aylık süre içinde en az kaç işçinin işine son verilmesi toplu işçi çıkarma sayılır?",
    "25", ["10", "20", "30", "50"],
    "Md. 29'a göre 101 ile 300 işçi çalışan işyerlerinde en az yüzde on oranında işçinin bir aylık süre içinde işine son "
    "verilmesi toplu işçi çıkarmadır: 250 × %10 = 25.", zorluk="hard")

P.q("İK md. 21",
    "İşe iade davasını kazanan ve süresinde başvuran işçi işveren tarafından işe başlatılmıştır; işçiye fesih sırasında "
    f"kıdem tazminatı ödenmişti.\n\n{K}, ödenmiş kıdem tazminatı hakkında aşağıdakilerden hangisi doğrudur?",
    "Boşta geçen süre ödemesinden mahsup edilir.",
    ["İşçide kalır, mahsup edilmez.",
     "İşçi tarafından faiziyle iade edilir.",
     "Sonraki yılların ücretinden kesilir.",
     "İşe başlatmama tazminatına eklenir."],
    "Md. 21'e göre işçi işe başlatılırsa peşin ödenen bildirim ücreti ile kıdem tazminatı, bu madde uyarınca yapılacak "
    "ödemeden mahsup edilir.", zorluk="hard")

P.sayisal("İK md. 29",
    f"{K}, toplu işçi çıkarmak isteyen işveren bu isteğini ilgili mercilere en az kaç gün önceden yazıyla bildirmelidir?",
    "30", ["7", "15", "45", "60"],
    "Md. 29'a göre işveren toplu işçi çıkarmak istediğinde bunu en az otuz gün önceden yazıyla işyeri sendika temsilcilerine, "
    "bölge müdürlüğüne ve Türkiye İş Kurumuna bildirir.", zorluk="easy")

P.q("İK md. 26",
    f"{K}, işverenin haklı nedenle derhal fesih hakkını kullanma süresini aşması hâlinde aşağıdakilerden hangisi "
    "doğrudur?",
    "Aynı olaya dayanarak fesih yapılamaz.",
    ["Fesih yine de geçerli bir derhal fesih sayılır.",
     "Süre, işçinin onayıyla yeniden başlar.",
     "İşveren bir yıl içinde istediği anda feshedebilir.",
     "Süre aşımı işçiye tazminat ödeme borcu doğurur."],
    "Md. 26'ya göre ahlak ve iyiniyet kurallarına uymayan hâllere dayanan fesih yetkisi, öğrenmeden itibaren altı iş günü "
    "geçtikten sonra kullanılamaz.")

P.sayisal("İK md. 25",
    "İşçi, izin almaksızın ve haklı bir sebebe dayanmaksızın işe devam etmemektedir."
    f"\n\n{K}, işverene derhal fesih hakkı veren devamsızlık, ardı ardına en az kaç iş günüdür?",
    "2", ["1", "3", "4", "5"],
    "Md. 25/II-g'ye göre işçinin izinsiz ve haklı sebebe dayanmaksızın ardı ardına iki iş günü, bir ayda iki defa tatil "
    "gününden sonraki iş günü veya bir ayda üç iş günü devamsızlığı işverene derhal fesih hakkı verir.")

P.q("İK md. 25",
    f"{K}, aşağıdakilerden hangisi işverene derhal fesih hakkı veren devamsızlık hâllerinden biri değildir?",
    "Bir ayda iki iş günü devamsızlık",
    ["Ardı ardına iki iş günü devamsızlık",
     "Bir ayda üç iş günü devamsızlık",
     "Ayda iki kez tatil sonrası iş günü devamsızlık",
     "Kasıtlı hastalıkta ardı ardına dört iş günü devamsızlık"],
    "Md. 25'e göre izinsiz ve haklı sebebe dayanmayan ardı ardına iki iş günü, ayda iki kez tatil sonrası iş günü veya ayda "
    "üç iş günü devamsızlık ile kasıttan doğan hastalıkta üç iş gününü aşan devamsızlık derhal fesih sebebidir.",
    zorluk="hard")

P.sayisal("İK md. 25",
    "İki yıllık kıdemi olan işçi, kendi kusurundan kaynaklanmayan bir hastalık nedeniyle işe gelememektedir."
    f"\n\n{K}, işverenin bildirimsiz fesih hakkı devamsızlığın kaç haftayı aşmasından sonra doğar?",
    "12", ["6", "8", "10", "14"],
    "Md. 25/I-b'ye göre bu hâllerde işverenin bildirimsiz fesih hakkı, md. 17'deki bildirim süresinin altı hafta aşılmasından "
    "sonra doğar: iki yıllık kıdemde 6 + 6 = 12 hafta.", zorluk="hard")

P.q("İK md. 17",
    f"{K}, bildirim sürelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üç yıldan fazla kıdemde süre on haftadır.",
    ["Altı aydan az kıdemde süre iki haftadır.",
     "Bir buçuk yıla kadar kıdemde süre dört haftadır.",
     "Üç yıla kadar kıdemde süre altı haftadır.",
     "Süreler sözleşmeyle artırılabilir."],
    "Md. 17'ye göre işi üç yıldan fazla sürmüş işçi için bildirim süresi sekiz haftadır.", zorluk="easy")

P.sayisal("İK md. 24",
    "İşçinin çalıştığı işyerinde deprem nedeniyle iş durmuştur."
    f"\n\n{K}, işçiye zorlayıcı sebeple derhal fesih hakkı doğması için işin kaç günden fazla durmasını gerektirecek "
    "bir sebep bulunmalıdır?",
    "7", ["3", "5", "10", "15"],
    "Md. 24/III'e göre işçinin çalıştığı işyerinde bir haftadan fazla süreyle işin durmasını gerektirecek zorlayıcı sebepler "
    "ortaya çıkarsa işçi sözleşmeyi derhal feshedebilir.")

P.q("İK md. 18",
    f"{K}, aşağıdakilerden hangisi iş güvencesi hükümlerinden yararlanmanın koşullarından biri değildir?",
    "Sözleşmenin yazılı yapılmış olması",
    ["İşyerinde en az otuz işçi çalışması",
     "İşçinin en az altı aylık kıdemi",
     "Sözleşmenin belirsiz süreli olması",
     "İşçinin üst düzey yönetici olmaması"],
    "Md. 18'e göre iş güvencesi için otuz veya daha fazla işçi, en az altı aylık kıdem, belirsiz süreli sözleşme ve işçinin "
    "işletmeyi yöneten işveren vekili olmaması aranır; yazılı sözleşme koşul değildir.")

P.sayisal("İK md. 26",
    f"{K}, işçi maddi çıkar sağlamadıkça, ahlak ve iyiniyet kurallarına uymayan hâllere dayanan derhal fesih yetkisi "
    "fiilin gerçekleşmesinden itibaren kaç yıl sonra kullanılamaz?",
    "1", ["2", "3", "5", "10"],
    "Md. 26'ya göre bu fesih yetkisi öğrenmeden itibaren altı iş günü geçtikten ve her hâlde fiilin gerçekleşmesinden "
    "itibaren bir yıl sonra kullanılamaz.")

P.q("İK md. 21",
    f"{K}, işe başlatmama tazminatına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tazminat en az iki aylık ücrettir.",
    ["Tazminat en çok sekiz aylık ücrettir.",
     "Miktarı mahkeme veya özel hakem belirler.",
     "Dava tarihindeki ücret esas alınır.",
     "İşçinin başvurusu üzerine işe başlatılmaması gerekir."],
    "Md. 21'e göre işe başlatmama tazminatı en az dört, en çok sekiz aylık ücret tutarındadır.")

P.sayisal("İK md. 29",
    "Bir işyerinde 80 işçi çalışmaktadır."
    f"\n\n{K}, bir aylık süre içinde en az kaç işçinin işine son verilmesi toplu işçi çıkarma sayılır?",
    "10", ["5", "8", "20", "30"],
    "Md. 29'a göre 20 ile 100 işçi çalışan işyerlerinde en az on işçinin bir aylık süre içinde işine son verilmesi toplu "
    "işçi çıkarma sayılır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
