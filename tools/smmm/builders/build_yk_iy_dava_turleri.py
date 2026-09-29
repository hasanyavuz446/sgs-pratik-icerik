# -*- coding: utf-8 -*-
"""Hukuk · İdari Yargılama Hukuku · İdari Dava Türleri, Yürütmenin Durdurulması ve Kararların Sonuçları — 60 soru.

Gerçek 2026/1-2026/2 kitapçıklarında İYUK soruları iptal ve tam yargı davası ayrımı, idari makamların sükûtu, özel
yargılama usulleri (ivedi yargılama, merkezî sınavlar) ve kararların uygulanması gibi konuları "2577 sayılı … Kanunu’na
göre …" kalıbıyla sormuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 2577 sayılı İYUK md. 2, 10-13, 18, 20/A-20/C, 21, 27-30.
7331 sayılı Kanunla (2021) md. 10, 11 ve 13'teki cevap süresi altmış günden otuz güne indirilmiştir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_idari_dava_turleri_2026.json", lesson="idari_yargilama_hukuku",
          topic="idari_dava_turleri", konu_adi="İdari Dava Türleri", seed=2026093008,
          surum="2577 sayılı İYUK güncel metni (7331 s. Kanun değişikliği dahil); 29.09.2026 kontrolü")

K = "2577 sayılı İdari Yargılama Usulü Kanunu’na göre"
K26 = "2577 sayılı İdari Yargılama Usulü Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İYUK md. 10",
    "Bay (A), belediyeden işyeri açma izni verilmesini istemiş; belediye başvuruya cevap vermemiştir."
    f"\n\n{K26}, başvurudan itibaren kaç gün içinde cevap verilmezse istek reddedilmiş sayılır?",
    "30", ["15", "45", "60", "90"],
    "Md. 10'a göre (7331 sayılı Kanunla 2021'de altmıştan otuza indirildi) idareye yapılan başvuruya otuz gün içinde cevap "
    "verilmezse istek reddedilmiş sayılır.", zorluk="hard")

P.q("İYUK md. 2",
    f"{K}, aşağıdakilerden hangisi idari dava türlerinden biri değildir?",
    "Tespit davası",
    ["İptal davası", "Tam yargı davası", "İdari sözleşme davası", "Kamu hizmeti sözleşmesi davası"],
    "Md. 2/1'e göre idari dava türleri iptal davaları, tam yargı davaları ve kamu hizmetinin yürütülmesi için yapılan idari "
    "sözleşmelerden doğan uyuşmazlıklara ilişkin davalardır.", zorluk="easy")

P.q("İYUK md. 2",
    f"{K}, iptal davasının açılabileceği hukuka aykırılık yönleri arasında aşağıdakilerden hangisi yer almaz?",
    "Yerindelik",
    ["Yetki", "Şekil", "Sebep", "Maksat"],
    "Md. 2/1-a'ya göre iptal davaları idari işlemlerin yetki, şekil, sebep, konu ve maksat yönlerinden biri ile hukuka aykırı "
    "olmaları nedeniyle açılır; yerindelik denetimi yapılamaz.", zorluk="easy")

P.sayisal("İYUK md. 10",
    "İdare, otuz günlük süre içinde başvuruya kesin olmayan bir cevap vermiş; ilgili kesin cevabı beklemeyi tercih "
    f"etmiştir.\n\n{K26}, bu bekleme süresi başvuru tarihinden itibaren en çok kaç ay olabilir?",
    "4", ["2", "3", "6", "12"],
    "Md. 10'a göre ilgili kesin olmayan cevabı ret sayarak dava açabileceği gibi kesin cevabı da bekleyebilir; bu takdirde "
    "dava açma süresi işlemez, ancak bekleme süresi başvuru tarihinden itibaren dört ayı geçemez.", zorluk="hard")

P.q("İYUK md. 2",
    f"{K}, iptal davası açabilmek için davacıda aranan koşul aşağıdakilerden hangisidir?",
    "Menfaatinin ihlal edilmiş olması",
    ["Kişisel hakkının doğrudan ihlali",
     "Zarara uğramış olması",
     "İdareyle sözleşme yapmış olması",
     "Kamu görevlisi olması"],
    "Md. 2/1-a'ya göre iptal davası menfaatleri ihlal edilenler tarafından açılır; tam yargı davası ise kişisel hakları "
    "doğrudan muhtel olanlar tarafından açılır.")

P.q("İYUK md. 2",
    f"{K}, tam yargı davasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kişisel hakkı doğrudan ihlal edilen açar.",
    ["Menfaati ihlal edilen herkes açabilir.",
     "Sadece düzenleyici işlemlere karşı açılır.",
     "Sadece idari sözleşmelerden doğar.",
     "İdari eylemlere karşı açılamaz."],
    "Md. 2/1-b'ye göre tam yargı davaları idari eylem ve işlemlerden dolayı kişisel hakları doğrudan muhtel olanlar "
    "tarafından açılır.")

P.sayisal("İYUK md. 13",
    f"{K}, idari eylemden hakları ihlal edilenler, eylemi öğrendikleri tarihten itibaren en geç kaç yıl içinde ilgili "
    "idareye başvurmalıdır?",
    "1", ["2", "3", "5", "10"],
    "Md. 13'e göre idari eylemlerden hakları ihlal edilenler eylemi öğrendikleri tarihten itibaren bir yıl ve her hâlde eylem "
    "tarihinden itibaren beş yıl içinde ilgili idareye başvurmalıdır.")

P.q("İYUK md. 2",
    f"{K}, idari sözleşmelerden doğan davalara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tahkimli imtiyaz sözleşmeleri de kapsamdadır.",
    ["Kamu hizmetinin yürütülmesi için yapılır.",
     "Uyuşmazlık sözleşmenin tarafları arasındadır.",
     "Her türlü idari sözleşmeyi kapsar.",
     "Tahkim öngörülenler kapsam dışıdır."],
    "Md. 2/1-c'ye göre tahkim yolu öngörülen imtiyaz şartlaşma ve sözleşmelerinden doğan uyuşmazlıklar hariç, kamu hizmeti "
    "için yapılan idari sözleşmelerden doğan uyuşmazlıklar idari dava konusudur.", zorluk="hard")

P.q("İYUK md. 10",
    f"{K26}, idari makamların sükûtuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Cevap verilmezse istek kabul edilmiş sayılır.",
    ["İlgililer işlem yapılması için idareye başvurabilir.",
     "Kesin olmayan cevap ret sayılarak dava açılabilir.",
     "Kesin cevap beklenirse dava süresi işlemez.",
     "Bekleme süresi başvurudan itibaren dört ayı geçemez."],
    "Md. 10'a göre otuz gün içinde cevap verilmezse istek reddedilmiş sayılır; ilgililer bu sürenin bittiği tarihten itibaren "
    "dava açma süresi içinde dava açabilir.")

P.sayisal("İYUK md. 13",
    f"{K}, idari eylemden doğan zarar için idareye başvuru, her hâlde eylem tarihinden itibaren kaç yıl içinde "
    "yapılmalıdır?",
    "5", ["1", "2", "3", "10"],
    "Md. 13'e göre başvuru, öğrenmeden itibaren bir yıl ve her hâlde eylem tarihinden itibaren beş yıl içinde yapılır.")

P.q("İYUK md. 10",
    "İlgili, idarenin zımni ret sayılan sessizliğine karşı süresinde dava açmamıştır; idare otuz günlük sürenin bitmesinden "
    f"sonra başvuruyu açıkça reddetmiştir.\n\n{K26}, ilgili bu durumda ne yapabilir?",
    "60 gün içinde dava açabilir.",
    ["Dava hakkı tamamen düşmüştür.",
     "Sadece idareye yeniden başvurabilir.",
     "Otuz gün içinde üst makama başvurmalıdır.",
     "Bir yıl içinde dava açabilir."],
    "Md. 10'a göre dava açılmaması veya davanın süreden reddi hâllerinde, otuz günlük sürenin bitmesinden sonra idarece cevap "
    "verilirse cevabın tebliğinden itibaren altmış gün içinde dava açılabilir.", zorluk="hard")

P.q("İYUK md. 11",
    f"{K}, dava açılmadan önce üst makama başvurmaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Başlamış dava süresini durdurur.",
    ["Dava açma süresini keser ve yeniden başlatır.",
     "Dava açma süresine bir etkisi olmaz.",
     "Sadece vergi davalarında mümkündür.",
     "Dava açıldıktan sonra da yapılabilir."],
    "Md. 11'e göre idari işlemin kaldırılması, geri alınması, değiştirilmesi veya yeni işlem yapılması üst makamdan istenebilir; "
    "bu başvuru işlemeye başlamış olan dava açma süresini durdurur.")

P.sayisal("İYUK md. 27",
    "İdare mahkemesi, bir idari işlem hakkında yürütmenin durdurulmasına karar vermiştir."
    f"\n\n{K}, bu karara karşı kararın tebliğini izleyen günden itibaren kaç gün içinde bir defaya mahsus itiraz edilebilir?",
    "7", ["3", "10", "15", "30"],
    "Md. 27/7'ye göre yürütmenin durdurulması istemleri hakkındaki kararlara tebliği izleyen günden itibaren yedi gün içinde "
    "bir defaya mahsus itiraz edilebilir; itiraz mercii dosyanın gelişinden itibaren yedi gün içinde karar verir.")

P.q("İYUK md. 11",
    "İlgili, dava açma süresinin 20. gününde üst makama başvurmuş, başvurusu reddedilmiştir."
    f"\n\n{K}, dava açma süresinin hesabına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Süre yeniden işler; geçen 20 gün hesaba katılır.",
    ["Süre baştan başlar; geçen günler dikkate alınmaz.",
     "Dava açma süresi sona ermiştir.",
     "Süre otuz gün uzamış sayılır.",
     "İlgili sadece tazminat davası açabilir."],
    "Md. 11/3'e göre isteğin reddedilmesi veya reddedilmiş sayılması hâlinde dava açma süresi yeniden işlemeye başlar ve "
    "başvurma tarihine kadar geçmiş süre de hesaba katılır.", zorluk="hard")

P.q("İYUK md. 11",
    f"{K}, üst makama başvuru yoluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üst makam yoksa başvurulamaz.",
    ["Başvuru dava açma süresi içinde yapılır.",
     "İşlemin geri alınması istenebilir.",
     "Yeni bir işlem yapılması istenebilir.",
     "Cevap verilmezse istek reddedilmiş sayılır."],
    "Md. 11/1'e göre işlemin kaldırılması veya değiştirilmesi üst makamdan, üst makam yoksa işlemi yapmış olan makamdan "
    "istenebilir.")

P.sayisal("İYUK md. 27",
    f"{K}, yürütmenin durdurulmasına dair verilen kararlar kaç gün içinde yazılır ve imzalanır?",
    "15", ["3", "7", "10", "30"],
    "Md. 27/9'a göre yürütmenin durdurulmasına dair kararlar on beş gün içinde yazılır ve imzalanır.")

P.q("İYUK md. 12",
    f"{K}, iptal ve tam yargı davalarının açılma biçimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İptal ve tam yargı davaları birlikte açılamaz.",
    ["Doğrudan tam yargı davası açılabilir.",
     "Önce iptal, sonra tam yargı davası açılabilir.",
     "İptal kararının tebliğinden sonra tam yargı açılabilir.",
     "İşlemin icrasından doğan zarar için dava açılabilir."],
    "Md. 12'ye göre ilgililer doğrudan tam yargı davası veya iptal ve tam yargı davalarını birlikte açabilecekleri gibi önce "
    "iptal davası açıp kararın tebliğinden sonra tam yargı davası da açabilir.")

P.q("İYUK md. 12",
    "Bay (B), kendisini göreve iade etmeyen işleme karşı açtığı iptal davasını kazanmış ve karar kendisine tebliğ "
    f"edilmiştir.\n\n{K}, Bay (B)’nin uğradığı zarar için tam yargı davasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tebliğden itibaren dava süresinde açabilir.",
    ["İptal davası açtığı için tazminat isteyemez.",
     "Tam yargı davasını ancak adli yargıda açabilir.",
     "İşlem tarihinden itibaren beş yıl içinde açabilir.",
     "Önce Anayasa Mahkemesine başvurmalıdır."],
    "Md. 12'ye göre önce iptal davası açılmışsa, bu husustaki kararın veya kanun yolu kararının tebliğinden itibaren dava "
    "süresi içinde tam yargı davası açılabilir.")

P.sayisal("İYUK md. 28",
    f"{K}, idarenin mahkeme kararının gereğini yerine getirme süresi kararın idareye tebliğinden başlayarak hiçbir "
    "şekilde kaç günü geçemez?",
    "30", ["7", "15", "45", "60"],
    "Md. 28/1'e göre idare esasa ve yürütmenin durdurulmasına ilişkin kararların gereğine göre gecikmeksizin işlem tesis "
    "etmeye veya eylemde bulunmaya mecburdur; bu süre kararın tebliğinden başlayarak otuz günü geçemez.")

P.q("İYUK md. 13",
    f"{K26}, idari eylemden doğan zararlar için dava açılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Doğrudan dava açılır.",
    ["Önce ilgili idareye başvurmak gerekir.",
     "Ret cevabının tebliğinden sonra dava açılabilir.",
     "Otuz gün cevap verilmezse dava açılabilir.",
     "Adli yargıda görevsizlikte başvuru şartı aranmaz."],
    "Md. 13'e göre idari eylemlerden hakları ihlal edilenlerin dava açmadan önce ilgili idareye başvurarak haklarının yerine "
    "getirilmesini istemeleri gerekir.")

P.q("İYUK md. 13",
    "Bir kişinin idari eylem nedeniyle adli yargıda açtığı tazminat davası görev yönünden reddedilmiştir."
    f"\n\n{K}, bu kişinin idari yargıda açacağı dava hakkında aşağıdakilerden hangisi doğrudur?",
    "İdareye ön başvuru şartı aranmaz.",
    ["Önce yeniden idareye başvurması gerekir.",
     "Dava açma hakkı düşmüştür.",
     "Sadece iptal davası açabilir.",
     "Davayı ancak Danıştayda açabilir."],
    "Md. 13/2'ye göre görevli olmayan adli yargı mercilerine açılan tam yargı davasının görev yönünden reddi hâlinde, sonradan "
    "idari yargıda açılacak davalarda idareye başvurma şartı aranmaz.", zorluk="hard")

P.sayisal("İYUK md. 20/A",
    f"{K}, ivedi yargılama usulüne tabi davalarda dava açma süresi kaç gündür?",
    "30", ["7", "10", "15", "60"],
    "Md. 20/A'ya göre ivedi yargılama usulünde dava açma süresi otuz gündür; md. 11 uygulanmaz ve nihai kararlara karşı on "
    "beş gün içinde temyize başvurulabilir.")

P.q("İYUK md. 27",
    f"{K}, yürütmenin durdurulması kararı verilebilmesi için aranan koşullar aşağıdakilerden hangisinde doğru verilmiştir?",
    "Telafisi güç zarar ve açık aykırılık",
    ["Sadece telafisi güç veya imkânsız zararın doğması",
     "Sadece açık hukuka aykırılık",
     "Davacının talebi yeterlidir",
     "İdarenin onayı ve teminat"],
    "Md. 27/2'ye göre yürütmenin durdurulması için idari işlemin uygulanması hâlinde telafisi güç veya imkânsız zararların "
    "doğması ve işlemin açıkça hukuka aykırı olması şartları birlikte gerçekleşmelidir.")

P.q("İYUK md. 27",
    f"{K}, yürütmenin durdurulmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dava açılması işlemin yürütülmesini durdurur.",
    ["Kararlar kural olarak teminat karşılığında verilir.",
     "İdareden teminat alınmaz.",
     "Aynı sebeple ikinci kez istemde bulunulamaz.",
     "YD kararı verilen dosyalar öncelikle incelenir."],
    "Md. 27/1'e göre Danıştayda veya idari mahkemelerde dava açılması dava edilen idari işlemin yürütülmesini durdurmaz.",
    zorluk="easy")

P.sayisal("İYUK md. 20/A",
    f"{K}, ivedi yargılama usulüne tabi davalar dosyanın tekemmülünden itibaren en geç kaç ay içinde karara bağlanır?",
    "1", ["2", "3", "4", "6"],
    "Md. 20/A'ya göre ivedi yargılama usulüne tabi davalar dosyanın tekemmülünden itibaren en geç bir ay içinde karara "
    "bağlanır; temyiz istemi en geç iki ay içinde karara bağlanır.", zorluk="hard")

P.q("İYUK md. 27",
    f"{K}, vergi mahkemesinde açılan davaların tahsil işlemlerine etkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Dava konusu kısmın tahsili durur.",
    ["Tahsil işlemleri kural olarak durmaz.",
     "Verginin tamamının tahsili durur.",
     "Tahsil ancak teminatla durur.",
     "Ödeme emrine karşı davada tahsil durur."],
    "Md. 27/4'e göre vergi uyuşmazlıklarından doğan davaların açılması, tarh edilen vergi, resim ve harçlar ile zam ve "
    "cezalarının dava konusu edilen bölümünün tahsil işlemlerini durdurur.", zorluk="hard")

P.q("İYUK md. 27",
    f"{K}, aşağıdakilerden hangisi uygulanmakla etkisi tükenecek idari işlemlerden sayılmaz?",
    "Kamu görevlisinin naklen ataması",
    ["Bir mitingin yasaklanması",
     "Bir binanın yıkılması",
     "Bir sınavın ertelenmesi",
     "Bir etkinlik izninin iptali"],
    "Md. 27/2'ye göre kamu görevlileri hakkındaki atama, naklen atama, görev ve unvan değişikliği ile görevlendirme işlemleri "
    "uygulanmakla etkisi tükenecek işlemlerden sayılmaz.", zorluk="hard")

P.sayisal("İYUK md. 20/B",
    "ÖSYM tarafından yapılan merkezî bir sınavın sonucuna karşı dava açılacaktır."
    f"\n\n{K}, bu davada dava açma süresi kaç gündür?",
    "10", ["5", "15", "30", "60"],
    "Md. 20/B'ye göre MEB ve ÖSYM tarafından yapılan merkezî ve ortak sınavlar ile sonuçlarına ilişkin davalarda dava açma "
    "süresi on gündür.", zorluk="hard")

P.q("İYUK md. 27",
    f"{K}, uygulanmakla etkisi tükenecek idari işlemlerde yürütmenin durdurulmasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Savunma alınmadan da durdurulabilir.",
    ["Ancak kesin hükümle durdurulabilir.",
     "Böyle bir işlem durdurulamaz.",
     "Sadece Danıştay dava daireleri durdurabilir.",
     "Teminat alınması yasaktır."],
    "Md. 27/2'ye göre uygulanmakla etkisi tükenecek idari işlemlerin yürütülmesi, savunma alındıktan sonra yeniden karar "
    "verilmek üzere idarenin savunması alınmaksızın da durdurulabilir.")

P.q("İYUK md. 27",
    f"{K}, idare mahkemesinin yürütmenin durdurulmasına ilişkin kararına itiraz mercii aşağıdakilerden hangisidir?",
    "Bölge idare mahkemesi",
    ["Danıştay İdari Dava Daireleri Kurulu", "Anayasa Mahkemesi", "Aynı mahkemenin başkanı",
     "Uyuşmazlık Mahkemesi"],
    "Md. 27/7'ye göre idare ve vergi mahkemeleri ile tek hâkim tarafından verilen YD kararlarına karşı bölge idare mahkemesine, "
    "Danıştay dava dairelerinin kararlarına karşı ilgili Kurula itiraz edilir.")

P.sayisal("İYUK md. 20/B",
    f"{K}, merkezî sınavlara ilişkin davalarda davalı idarenin savunma süresi dava dilekçesinin tebliğinden itibaren kaç "
    "gündür?",
    "3", ["5", "7", "10", "15"],
    "Md. 20/B'ye göre savunma süresi dava dilekçesinin tebliğinden itibaren üç gün olup bir defaya mahsus en fazla üç gün "
    "uzatılabilir; davalar tekemmülden itibaren on beş gün içinde karara bağlanır.", zorluk="hard")

P.q("İYUK md. 27",
    f"{K}, yürütmenin durdurulması kararına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Karar gerekçeli olarak verilir.",
    ["Kararda gerekçe gösterilmez.",
     "Sadece Anayasa Mahkemesine başvuru gerekçesiyle verilebilir.",
     "İtiraz üzerine verilen karar temyiz edilir.",
     "Karar ancak duruşmadan sonra verilir."],
    "Md. 27/2'ye göre YD kararlarında işlemin hangi gerekçelerle açıkça hukuka aykırı olduğu ve doğacak zararların neler olduğu "
    "belirtilir; sadece AYM'ye başvurulduğu gerekçesiyle YD kararı verilemez.")

P.q("İYUK md. 28",
    f"{K}, mahkeme kararlarının sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kararı uygulamayan memura doğrudan tazminat davası açılır.",
    ["İdare kararın gereğini gecikmeksizin yerine getirir.",
     "Karar uygulanmazsa idare aleyhine tazminat davası açılabilir.",
     "Hükmedilen para davacının banka hesabına yatırılır.",
     "Tazminat davalarında idare faiz öder."],
    "Md. 28/4'e göre mahkeme kararlarının süresi içinde kamu görevlilerince yerine getirilmemesi hâlinde tazminat davası ancak "
    "ilgili idare aleyhine açılabilir.")

P.sayisal("İYUK md. 27",
    f"{K}, yürütmenin durdurulması kararına yapılan itiraz üzerine itiraz mercii dosyanın kendisine gelişinden itibaren "
    "kaç gün içinde karar vermek zorundadır?",
    "7", ["3", "10", "15", "30"],
    "Md. 27/7'ye göre itiraz edilen merciler dosyanın kendisine gelişinden itibaren yedi gün içinde karar vermek zorundadır; "
    "itiraz üzerine verilen kararlar kesindir.", zorluk="hard")

P.q("İYUK md. 28",
    f"{K}, tazminat ve vergi davalarında idarece ödenecek faize ilişkin aşağıdakilerden hangisi doğrudur?",
    "6183 md. 48 tecil faizi uygulanır.",
    ["Kanuni faiz oranı uygulanır.",
     "Ticari avans faizi oranı uygulanır.",
     "Faiz ödenmez.",
     "Mevduat faizi oranı uygulanır."],
    "Md. 28/6'ya göre tazminat ve vergi davalarında idarece kararın tebliği ile ödeme tarihi arasındaki süre için 6183 sayılı "
    "Kanunun 48. maddesine göre belirlenen tecil faizi oranında faiz ödenir.", zorluk="hard")

P.q("İYUK md. 20/A",
    f"{K}, aşağıdakilerden hangisi ivedi yargılama usulüne tabi uyuşmazlıklardan biri değildir?",
    "İhaleden yasaklama kararları",
    ["Acele kamulaştırma işlemleri",
     "Özelleştirme Yüksek Kurulu kararları",
     "Turizmi Teşvik Kanunu uyarınca kiralama işlemleri",
     "ÇED sonucu alınan kararlar"],
    "Md. 20/A'ya göre ihaleden yasaklama kararları hariç ihale işlemleri, acele kamulaştırma, ÖYK kararları, turizm satış ve "
    "kiralamaları ve idari yaptırımlar hariç ÇED kararları ivedi yargılamaya tabidir.", zorluk="hard")

P.sayisal("İYUK md. 20/B",
    f"{K}, merkezî ve ortak sınavlara ilişkin davalarda verilen nihai kararlara karşı tebliğden itibaren kaç gün içinde "
    "temyiz yoluna başvurulabilir?",
    "5", ["3", "7", "10", "15"],
    "Md. 20/B'ye göre merkezî sınav davalarında nihai kararlara karşı tebliğden itibaren beş gün içinde temyize başvurulabilir; "
    "temyiz dilekçelerine cevap süresi de beş gündür.", zorluk="hard")

P.q("İYUK md. 20/A",
    f"{K}, ivedi yargılama usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu davalarda istinafa gidilebilir.",
    ["Md. 11 hükümleri uygulanmaz.",
     "YD kararlarına itiraz edilemez.",
     "Temyiz süresi on beş gündür.",
     "Temyiz üzerine verilen kararlar kesindir."],
    "Md. 45/8'e göre ivedi yargılama usulüne tabi davalarda istinaf yoluna başvurulamaz; nihai kararlara karşı doğrudan temyiz "
    "yoluna gidilir.", zorluk="hard")

P.q("İYUK md. 20/B",
    f"{K}, merkezî sınavlarla ilgili davalarda verilen yürütmenin durdurulması ve iptal kararları nasıl uygulanır?",
    "Sınava katılanların lehine",
    ["Sadece davacı hakkında",
     "Sadece sonraki sınavlarda",
     "Sınavın tamamen iptali şeklinde",
     "İdarenin takdirine göre"],
    "Md. 20/B'ye göre MEB ve ÖSYM'nin merkezî ve ortak sınavlarıyla ilgili davalarda verilen YD ve iptal kararları, sınava "
    "katılan kişilerin lehine sonuç doğuracak şekilde uygulanır.")

P.sayisal("İYUK md. 20/A",
    f"{K}, ivedi yargılama usulünde davalı idarenin savunma süresi dava dilekçesinin tebliğinden itibaren kaç gündür?",
    "15", ["3", "7", "10", "30"],
    "Md. 20/A'ya göre ivedi yargılamada savunma süresi dava dilekçesinin tebliğinden itibaren on beş gündür ve bir defaya "
    "mahsus en fazla on beş gün uzatılabilir.")

P.q("İYUK md. 20/B",
    f"{K}, merkezî sınavlara ilişkin davaların yargılama usulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Üst makama başvuru süreyi durdurur.",
    ["İlk inceleme yedi gün içinde yapılır.",
     "YD kararlarına itiraz edilemez.",
     "Temyiz süresi beş gündür.",
     "Temyiz dilekçesine cevap süresi beş gündür."],
    "Md. 20/B'ye göre bu davalarda md. 11 hükümleri uygulanmaz; üst makama başvuru dava açma süresini durdurmaz.",
    zorluk="hard")

P.q("İYUK md. 20/C",
    f"{K}, askerî hizmete ilişkin idari uyuşmazlıklarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Savaş hâlinde de yürütmenin durdurulması kararı verilebilir.",
    ["Dilekçede sicil, sınıf ve rütbe de gösterilir.",
     "Dilekçe en yakın amire de verilebilir.",
     "YAŞ terfi işlemlerine karşı yargı yolu kapalıdır.",
     "Görev yerinin bağlı olduğu BİM’deki idare mahkemesi yetkilidir."],
    "Md. 20/C'ye göre savaş hâlinde yürütmenin durdurulmasına karar verilemez.", zorluk="hard")

P.sayisal("İYUK md. 20/B",
    f"{K}, merkezî sınavlara ilişkin davalar dosyanın tekemmülünden itibaren en geç kaç gün içinde karara bağlanır?",
    "15", ["5", "7", "10", "30"],
    "Md. 20/B'ye göre merkezî sınav davaları dosyanın tekemmülünden itibaren en geç on beş gün içinde karara bağlanır.")

P.q("İYUK md. 18",
    f"{K}, duruşmalara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Taraflardan hiçbiri gelmezse dava reddedilir.",
    ["Duruşmalar kural olarak açık yapılır.",
     "Genel ahlak gerektirirse duruşma gizli yapılabilir.",
     "Taraflara ikişer defa söz verilir.",
     "Danıştay duruşmalarında savcının bulunması şarttır."],
    "Md. 18'e göre taraflardan hiçbiri gelmezse duruşma açılmaz ve inceleme evrak üzerinde yapılır; dava bu nedenle reddedilmez.")

P.q("İYUK md. 21",
    f"{K}, dilekçe ve savunmalarla birlikte verilmeyen belgelere ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zamanında sunulamamışsa kabul edilir.",
    ["Kural olarak kabul edilmez.",
     "Sadece temyizde sunulabilir.",
     "Karşı tarafa tebliğ edilmeden kabul edilir.",
     "Ancak noter onaylıysa kabul edilir."],
    "Md. 21'e göre dilekçe ve savunmalarla verilmeyen belgeler, vaktinde ibraz edilmelerine imkân bulunmadığına mahkemece "
    "kanaat getirilirse kabul edilir ve diğer tarafa tebliğ edilir.")

P.sayisal("İYUK md. 13",
    "İdari bir eylem nedeniyle zarara uğrayan kişi, süresi içinde ilgili idareye başvurmuş; idare cevap vermemiştir."
    f"\n\n{K26}, başvurudan itibaren kaç günlük sürenin bitiminden sonra dava süresi içinde dava açılabilir?",
    "30", ["15", "45", "60", "90"],
    "Md. 13'e göre (7331 sayılı Kanunla değişik) istek hakkında otuz gün içinde cevap verilmezse bu sürenin bittiği tarihten "
    "itibaren dava süresi içinde dava açılabilir.", zorluk="hard")

P.q("İYUK md. 29",
    f"{K}, kararın açıklanması veya aykırılığın giderilmesi istemine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Karar yerine getirilinceye kadar istenebilir.",
    ["Karar tarihinden itibaren yedi gün içinde istenir.",
     "Sadece davacı tarafından istenebilir.",
     "Dilekçe tek nüsha verilir.",
     "İstemi Danıştay inceler."],
    "Md. 29'a göre yeterince açık olmayan veya aykırı hüküm fıkraları taşıyan kararların açıklanması veya aykırılığın "
    "giderilmesi taraflardan her biri tarafından kararın yerine getirilmesine kadar istenebilir.")

P.q("İYUK md. 30",
    f"{K}, aşağıdakilerden hangisinin düzeltilmesi md. 30 kapsamında istenemez?",
    "Kararın hukuki gerekçesi",
    ["Tarafların adı ve soyadı",
     "Tarafların sıfatı",
     "İddiaların sonucuna ilişkin yanlışlık",
     "Hüküm fıkrasındaki hesap yanlışlığı"],
    "Md. 30'a göre iki tarafın adı, soyadı ve sıfatı ile iddiaları sonucuna ilişkin yanlışlıklar ve hüküm fıkrasındaki hesap "
    "yanlışlıklarının düzeltilmesi istenebilir; kararın gerekçesi bu yolla değiştirilemez.")

P.oncul("İYUK md. 20/A",
    f"{K} aşağıdaki uyuşmazlıklar değerlendirilmektedir:",
    ["Acele kamulaştırma işlemi",
     "Kamu görevlisinin disiplin cezası",
     "İhale işlemi",
     "Vergi ziyaı cezası"],
    "Yukarıdakilerden hangileri ivedi yargılama usulüne tabidir?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 20/A'ya göre acele kamulaştırma (I) ve ihaleden yasaklama hariç ihale işlemleri (III) ivedi yargılamaya tabidir; "
    "disiplin cezası (II) ve vergi ziyaı cezası (IV) bu kapsamda değildir.")

P.q("İYUK md. 2",
    "Bir yüklenici, belediyeyle yaptığı ve kamu hizmetinin yürütülmesine ilişkin idari sözleşmeden doğan alacağı için dava "
    f"açacaktır; sözleşmede tahkim öngörülmemiştir.\n\n{K}, bu dava hakkında aşağıdakilerden hangisi doğrudur?",
    "İdari sözleşmeden doğan idari davadır.",
    ["Adli yargıda görülen alacak davasıdır.",
     "İptal davası olarak açılmalıdır.",
     "Ticaret mahkemesinde açılmalıdır.",
     "Uyuşmazlık Mahkemesinde görülür."],
    "Md. 2/1-c'ye göre tahkim yolu öngörülen imtiyaz sözleşmeleri hariç, kamu hizmetinin yürütülmesi için yapılan idari "
    "sözleşmelerden doğan uyuşmazlıklar idari davadır.")

P.q("İYUK md. 28",
    f"{K}, vergi uyuşmazlığına ilişkin mahkeme kararının idareye tebliğinden sonra aşağıdakilerden hangisi yapılır?",
    "Hesaplanan miktar mükellefe bildirilir.",
    ["Mükellef yeniden dava açar.",
     "Karar Maliye Bakanlığınca onaylanır.",
     "Vergi o yıl tahsil edilmez.",
     "Karar Resmî Gazete'de ilan edilir."],
    "Md. 28/5'e göre vergi uyuşmazlıklarına ilişkin mahkeme kararlarının idareye tebliğinden sonra bu kararlara göre tespit "
    "edilecek vergi ve cezaların miktarı ilgili idarece mükellefe bildirilir.")

P.q("İYUK md. 27",
    f"{K}, yürütmenin durdurulmasında teminata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Adli yardımdan yararlananlardan da teminat alınır.",
    ["Kararlar kural olarak teminat karşılığında verilir.",
     "Durumun gereğine göre teminat aranmayabilir.",
     "İdareden teminat alınmaz.",
     "Teminat uyuşmazlığını kararı veren merci çözer."],
    "Md. 27/6'ya göre YD kararları teminat karşılığında verilir, ancak durumun gereklerine göre teminat aranmayabilir; "
    "idareden ve adli yardımdan faydalananlardan teminat alınmaz.")

P.q("İYUK md. 28",
    f"{K}, idare mahkeme kararına göre işlem tesis etmezse ilgili aşağıdaki davalardan hangisini açabilir?",
    "Maddi ve manevi tazminat davası",
    ["Menfi tespit davası", "İstirdat davası", "Kamulaştırmasız el atma davası", "Ceza davası"],
    "Md. 28/3'e göre mahkeme kararlarına göre işlem tesis edilmeyen veya eylemde bulunulmayan hâllerde idare aleyhine maddi ve "
    "manevi tazminat davası açılabilir.")

P.q("İYUK md. 28",
    "Terör örgütüyle iltisak gerekçesiyle kamu görevinden çıkarılan Milli Savunma Bakanlığı personeli açtığı davayı ilk "
    f"derecede kazanmış, karar göreve iade sonucunu doğurmaktadır.\n\n{K26}, bu karar ne zaman yerine getirilir?",
    "Nihai kararın kesinleşmesinden sonra",
    ["Kararın idareye tebliğinden itibaren otuz gün içinde",
     "Yürütmenin durdurulması kararıyla derhal",
     "İlk derece kararının verildiği gün",
     "İdarenin takdir edeceği bir tarihte"],
    "Md. 28/1'e 7588 sayılı Kanunla 2026'da eklenen cümleye göre bu personel hakkında göreve iade sonucunu doğuran mahkeme "
    "kararları uyarınca tesis edilecek işlemler nihai kararların kesinleşmesinden sonra yerine getirilir.", zorluk="hard")

P.q("İYUK md. 18",
    f"{K}, Danıştayda görülen davaların duruşmalarında taraflar dinlendikten sonra aşağıdakilerden hangisi yapılır?",
    "Savcı yazılı düşüncesini açıklar.",
    ["Tetkik hâkimi raporunu okur.",
     "Tanıklar dinlenir.",
     "Bilirkişi rapor sunar.",
     "Karar derhal açıklanır ve tefhim edilir."],
    "Md. 18/4'e göre Danıştaydaki duruşmalarda savcının bulunması şarttır; taraflar dinlendikten sonra savcı yazılı düşüncesini "
    "açıklar, ardından taraflara son sözleri sorulur.")

P.q("İYUK md. 22",
    f"{K}, davaların karara bağlanmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Usulde azınlık kalan esasta oy kullanmaz.",
    ["Meseleler sırasıyla oya konulur.",
     "Azınlık görüşleri kararın altına yazılır.",
     "Konular aydınlanınca karar verilir.",
     "Görüşmeler için tutanak düzenlenir."],
    "Md. 22'ye göre md. 15'teki sebepler veya usul meselelerinde azınlıkta kalanlar işin esası hakkında da oylarını kullanır.")

P.q("İYUK md. 27",
    f"{K}, aşağıdaki hâllerden hangisinde vergi davasının açılması tahsil işlemini durdurmaz?",
    "İhtirazi kayıtlı beyana dayalı tahsilat",
    ["Tarhiyatın dava konusu edilen kısmı",
     "Dava konusu vergi ziyaı cezası",
     "Dava konusu tarh edilen harç",
     "Dava konusu tarh edilen resim ve zamları"],
    "Md. 27/4'e göre ihtirazi kayıtla verilen beyannameler üzerine yapılan işlemlerle tahsilat işlemlerinden dolayı açılan "
    "davalar tahsil işlemini durdurmaz; bunlar hakkında yürütmenin durdurulması istenebilir.", zorluk="hard")

P.q("İYUK md. 20/C",
    f"{K}, olağanüstü hâl tedbirlerinin uygulanmasında görevlendirilen askerî personelin naklen atanmasına ilişkin iptal "
    "davalarında aşağıdakilerden hangisi doğrudur?",
    "YD kararı verilemez.",
    ["YD ancak teminatla verilir.",
     "Dava açma süresi on gündür.",
     "Dava doğrudan Danıştayda açılır.",
     "YD kararı savunma alınmadan verilir."],
    "Md. 20/C/5'e göre olağanüstü hâller sebebiyle alınan tedbirlerin uygulanmasında görevlendirilenlerin naklen atanmalarına "
    "ilişkin iptal davalarında yürütmenin durdurulmasına karar verilemez.", zorluk="hard")

P.q("İYUK md. 2",
    f"{K}, aşağıdakilerden hangisi tam yargı davasının konusu olabilir?",
    "Eylemden doğan zararın tazmini",
    ["İşlemin yerindeliğinin denetimi",
     "Kanunun Anayasaya aykırılığı",
     "Yasama işleminin iptali",
     "Yargı kararının iptali"],
    "Md. 2/1-b'ye göre tam yargı davaları idari eylem ve işlemlerden dolayı kişisel hakları doğrudan muhtel olanların açtığı "
    "davalardır; eylemden doğan zararın tazmini bu davanın konusudur.", zorluk="easy")

P.q("İYUK md. 27",
    f"{K}, dava dilekçesi ve eklerinden yürütmenin durdurulması isteminin yerinde olmadığı anlaşılırsa aşağıdakilerden "
    "hangisi doğrudur?",
    "İstem savunmasız reddedilebilir.",
    ["Önce idarenin savunması alınmalıdır.",
     "İstem Danıştaya gönderilir.",
     "İstem ancak duruşmada reddedilir.",
     "İstem hakkında karar verilemez."],
    "Md. 27/3'e göre dava dilekçesi ve eklerinden YD isteminin yerinde olmadığı anlaşılırsa davalı idarenin savunması "
    "alınmaksızın istem reddedilebilir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
