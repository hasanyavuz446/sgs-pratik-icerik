# -*- coding: utf-8 -*-
"""Hukuk · İdari Yargılama Hukuku · Süreler ve Kanun Yolları — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında İYUK soruları dava açma süresi, sürelerin başlangıcı, istinaf ve temyiz gibi
konuları "2577 sayılı İdari Yargılama Usulü Kanunu’na göre …" kalıbıyla sormuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 2577 sayılı İYUK md. 7-8, 16-17, 45-53 (7524 sayılı Kanunla
2024'te ve 7589 sayılı Kanunla 2026'da değişik istinaf-temyiz hükümleri dahil). Yıllık yeniden değerlemeye tabi parasal
sınırlar soru konusu yapılmamıştır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_idari_yargida_sureler_kanun_yollari_2026.json", lesson="idari_yargilama_hukuku",
          topic="idari_yargida_sureler_kanun_yollari", konu_adi="İdari Yargıda Süreler ve Kanun Yolları",
          seed=2026093009, surum="2577 sayılı İYUK güncel metni (7524 ve 7589 s. Kanun değişiklikleri dahil); "
          "29.09.2026 kontrolü")

K = "2577 sayılı İdari Yargılama Usulü Kanunu’na göre"
K26 = "2577 sayılı İdari Yargılama Usulü Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İYUK md. 7",
    f"{K}, özel kanunlarında ayrı süre gösterilmeyen hâllerde idare mahkemelerinde dava açma süresi kaç gündür?",
    "60", ["15", "30", "45", "90"],
    "Md. 7/1'e göre dava açma süresi özel kanunlarda ayrı süre gösterilmeyen hâllerde Danıştayda ve idare mahkemelerinde "
    "altmış, vergi mahkemelerinde otuz gündür.", zorluk="easy")

P.q("İYUK md. 7",
    f"{K}, tahakkuku tahsile bağlı vergilerde dava açma süresi hangi tarihi izleyen günden başlar?",
    "Tahsilatın yapıldığı tarih",
    ["Beyannamenin verildiği tarih", "Vergi dönemi sonu", "Takvim yılı sonu", "Tahakkuk fişinin düzenlendiği tarih"],
    "Md. 7/2-b'ye göre tahakkuku tahsile bağlı vergilerde süre tahsilatın, tebliğ yapılan hâllerde tebliğin, tevkif yoluyla "
    "alınan vergilerde ödemenin, tescile bağlı vergilerde tescilin yapıldığı tarihi izleyen günden başlar.")

P.q("İYUK md. 7",
    f"{K}, vergi, resim ve harçlardan doğan uyuşmazlıklarda dava süresinin hangi tarihten başladığına ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tevkifatta süre yıl sonunda başlar.",
    ["Tebliğ yapılan hâllerde tebliği izleyen günden başlar.",
     "Tescile bağlı vergilerde tescili izleyen günden başlar.",
     "Tahakkuku tahsile bağlı vergilerde tahsilattan başlar.",
     "İdarenin açacağı davada karar idareye gelince başlar."],
    "Md. 7/2-b'ye göre tevkif yoluyla alınan vergilerde süre istihkak sahiplerine ödemenin yapıldığı tarihi izleyen günden "
    "başlar.", zorluk="hard")

P.sayisal("İYUK md. 7",
    "Mükellefe vergi/ceza ihbarnamesi tebliğ edilmiştir; özel kanunda farklı bir süre öngörülmemiştir."
    f"\n\n{K}, mükellef tebliğden itibaren kaç gün içinde vergi mahkemesinde dava açabilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 7/1'e göre vergi mahkemelerinde dava açma süresi otuz gündür; süre tebliği izleyen günden başlar.", zorluk="easy")

P.q("İYUK md. 7",
    f"{K}, idari uyuşmazlıklarda dava açma süresi hangi tarihi izleyen günden başlar?",
    "Yazılı bildirimin yapıldığı tarih",
    ["İşlemin imzalandığı tarih", "İşlemin arşive kaldırıldığı tarih", "İşlemin Resmî Gazete’de ilanı",
     "İlgilinin sözlü olarak öğrendiği tarih"],
    "Md. 7/2-a'ya göre idari uyuşmazlıklarda dava açma süresi yazılı bildirimin yapıldığı tarihi izleyen günden başlar.",
    zorluk="easy")

P.q("İYUK md. 7",
    f"{K}, ilanı gereken düzenleyici işlemlere karşı dava açılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Düzenleyici işlem iptal edilmedikçe uygulama işlemi iptal edilemez.",
    ["Dava süresi ilan tarihini izleyen günden başlar.",
     "Uygulama üzerine düzenleyici işleme de dava açılabilir.",
     "Düzenleyici işlem ve uygulama işlemi birlikte dava konusu olabilir.",
     "Uygulama işlemine ayrıca dava açılabilir."],
    "Md. 7/4'e göre ilgililer uygulama üzerine düzenleyici işlem veya uygulama işlemi yahut her ikisi aleyhine dava açabilir; "
    "düzenleyici işlemin iptal edilmemiş olması ona dayalı işlemin iptaline engel olmaz.", zorluk="hard")

P.sayisal("İYUK md. 7",
    "Adresi belli olmayan bir kişiye özel kanunundaki hükümlere göre ilan yoluyla bildirim yapılmıştır; özel kanunda aksine "
    f"hüküm yoktur.\n\n{K}, dava açma süresi son ilan tarihini izleyen günden itibaren kaç gün sonra işlemeye başlar?",
    "15", ["3", "7", "10", "30"],
    "Md. 7/3'e göre ilan yoluyla bildirim yapılan hâllerde süre, son ilan tarihini izleyen günden itibaren on beş gün sonra "
    "işlemeye başlar.", zorluk="hard")

P.q("İYUK md. 8",
    f"{K}, sürelere ilişkin genel esaslara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tatil günleri sürelere dahil edilmez.",
    ["Süreler tebliği izleyen günden işlemeye başlar.",
     "Süreler ilanı izleyen günden işlemeye başlar.",
     "Son gün tatile rastlarsa süre izleyen iş gününe uzar.",
     "Adli tatile rastlayan süre yedi gün uzamış sayılır."],
    "Md. 8/2'ye göre tatil günleri sürelere dahildir; ancak sürenin son günü tatile rastlarsa süre tatili izleyen çalışma "
    "gününün bitimine kadar uzar.", zorluk="easy")

P.q("İYUK md. 8",
    "Dava açma süresinin son günü pazar gününe rastlamaktadır; ertesi gün resmî tatil değildir."
    f"\n\n{K}, dava en geç ne zamana kadar açılabilir?",
    "Pazartesi mesai bitimine kadar",
    ["Cumartesi mesai bitimine kadar", "Pazar gece yarısına kadar", "Salı mesai bitimine kadar",
     "Takip eden haftanın cumasına kadar"],
    "Md. 8/2'ye göre sürenin son günü tatil gününe rastlarsa süre tatil gününü izleyen çalışma gününün bitimine kadar uzar.")

P.sayisal("İYUK md. 8",
    f"{K}, Kanunda yazılı sürelerin bitmesi çalışmaya ara verme zamanına rastlarsa bu süreler, ara vermenin sona erdiği "
    "günü izleyen tarihten itibaren kaç gün uzamış sayılır?",
    "7", ["3", "5", "10", "15"],
    "Md. 8/3'e göre sürelerin bitmesi çalışmaya ara verme zamanına rastlarsa süreler ara vermenin sona erdiği günü izleyen "
    "tarihten itibaren yedi gün uzamış sayılır.")

P.q("İYUK md. 16",
    f"{K}, dilekçe ve savunmaların karşılıklı verilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Davacı, davalının ikinci savunmasına kural olarak cevap verir.",
    ["Dava dilekçesi davalıya tebliğ olunur.",
     "Davalının savunması davacıya tebliğ olunur.",
     "Davacının ikinci dilekçesi davalıya tebliğ edilir.",
     "Süre geçtikten sonraki savunmaya dayanılamaz."],
    "Md. 16/2'ye göre davalının ikinci savunması davacıya tebliğ edilir, buna karşı davacı cevap veremez; ancak cevabı "
    "gerektiren hususlar varsa mahkeme süre verir.")

P.q("İYUK md. 16",
    f"{K}, tam yargı davalarında dava dilekçesindeki miktarın artırılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Harç ödenerek bir kez artırılabilir.",
    ["Dava açıldıktan sonra artırılamaz.",
     "Sadece istinaf aşamasında artırılabilir.",
     "Harç ödenmeden sınırsız artırılabilir.",
     "Ancak davalı idarenin rızasıyla artırılabilir."],
    "Md. 16/4'e göre tam yargı davalarında dilekçedeki miktar, nihai karar verilinceye kadar harcı ödenmek suretiyle bir "
    "defaya mahsus artırılabilir ve artırma dilekçesi otuz gün içinde cevap verilmek üzere karşı tarafa tebliğ edilir.",
    zorluk="hard")

P.sayisal("İYUK md. 16",
    f"{K}, taraflar yapılan tebliğlere karşı tebliğ tarihinden itibaren kaç gün içinde cevap verebilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 16/3'e göre taraflar tebliğ tarihinden itibaren otuz gün içinde cevap verebilir.", zorluk="easy")

P.q("İYUK md. 17",
    f"{K}, temyiz ve istinaf aşamasında duruşma yapılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Taraf istemi ve merci kararına bağlıdır.",
    ["Her dosyada zorunludur.",
     "Sadece idarenin istemiyle yapılır.",
     "Bu aşamada yapılamaz.",
     "Tarafların istemi tek başına yeterlidir."],
    "Md. 17/2'ye göre temyiz ve istinaflarda duruşma yapılması tarafların istemine ve Danıştay veya ilgili bölge idare "
    "mahkemesi kararına bağlıdır.")

P.q("İYUK md. 17",
    f"{K}, duruşmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mahkeme resen duruşmaya karar veremez.",
    ["Duruşma talebi dava dilekçesiyle yapılabilir.",
     "Duruşma talebi savunmada da yapılabilir.",
     "İptal davalarında taraf isteğiyle duruşma yapılır.",
     "Davetiyeler en az otuz gün önce gönderilir."],
    "Md. 17/4'e göre Danıştay, mahkeme ve hâkim, birinci ve ikinci fıkralardaki kayıtlara bağlı olmaksızın kendiliğinden "
    "duruşma yapılmasına karar verebilir.")

P.sayisal("İYUK md. 16",
    "Davalı idare, haklı bir sebebe dayanarak savunma süresinin uzatılmasını süresi içinde istemiştir."
    f"\n\n{K}, mahkeme bu süreyi bir defaya mahsus olmak üzere en çok kaç gün uzatabilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 16/3'e göre cevap süresi haklı sebeplerle taraflardan birinin isteği üzerine otuz günü geçmemek ve bir defaya "
    "mahsus olmak üzere uzatılabilir; süre geçtikten sonraki uzatma talepleri kabul edilmez.")

P.q("İYUK md. 45",
    f"{K}, idare ve vergi mahkemesi kararlarına karşı istinaf başvurusu hangi mercie yapılır?",
    "Bölge idare mahkemesine",
    ["Danıştay İdari Dava Daireleri Kuruluna", "Kararı veren mahkemenin başkanına", "Anayasa Mahkemesine",
     "Uyuşmazlık Mahkemesine"],
    "Md. 45/1'e göre istinaf, mahkemenin bulunduğu yargı çevresindeki bölge idare mahkemesine yapılır.", zorluk="easy")

P.q("İYUK md. 45",
    f"{K26}, bölge idare mahkemesinin istinaf incelemesi sonucunda istinaf başvurusunun reddine karar verdiği hâller "
    "arasında aşağıdakilerden hangisi yer almaz?",
    "Kararın hukuka aykırı bulunması",
    ["Kararın hukuka uygun bulunması",
     "Sonuç doğru, gerekçe eksik bulunması",
     "Maddi yanlışlığın düzeltilebilir olması",
     "Gerekçenin değiştirilmesiyle kararın doğru olması"],
    "Md. 45/3'e göre (7589 sayılı Kanunla 2026'da değişik) karar hukuka uygunsa, sonucu doğru olup gerekçesi değiştirilerek "
    "ya da maddi yanlışlık düzeltilerek istinaf başvurusu reddedilir; hukuka aykırılık hâlinde ise karar kaldırılır.",
    zorluk="hard")

P.sayisal("İYUK md. 45",
    f"{K}, idare ve vergi mahkemelerinin kararlarına karşı kararın tebliğinden itibaren kaç gün içinde istinaf yoluna "
    "başvurulabilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 45/1'e göre idare ve vergi mahkemelerinin kararlarına karşı kararın tebliğinden itibaren otuz gün içinde bölge idare "
    "mahkemesine istinaf yoluna başvurulabilir.", zorluk="easy")

P.q("İYUK md. 45",
    f"{K}, bölge idare mahkemesinin ilk derece kararını hukuka uygun bulmaması hâlinde kural olarak aşağıdakilerden "
    "hangisi yapılır?",
    "Karar kaldırılıp esastan yeniden karar verilir.",
    ["Dosya doğrudan ilk derece mahkemesine gönderilir.",
     "Karar bozularak Danıştaya gönderilir.",
     "Dava açılmamış sayılır.",
     "İstinaf başvurusu reddedilir."],
    "Md. 45/4'e göre bölge idare mahkemesi kararı hukuka uygun bulmazsa istinaf başvurusunu kabul ederek ilk derece kararını "
    "kaldırır ve işin esası hakkında yeniden karar verir.")

P.q("İYUK md. 45",
    f"{K26}, aşağıdaki hâllerden hangisinde bölge idare mahkemesi ilk derece kararını kaldırarak dosyayı kararı veren "
    "mahkemeye göndermez?",
    "Kararın gerekçesinin yetersiz görülmesi",
    ["Davaya görevsiz mahkemece bakılmış olması",
     "Reddedilmiş hâkimin davaya bakmış olması",
     "Dosyanın yanlış hasımla tekemmül ettirilmesi",
     "Talep hakkında karar verilmemiş olması"],
    "Md. 45/5'e göre görev-yetki, reddedilmiş hâkim, dilekçe reddi, yanlış hasım, eksik hüküm gibi hâllerde dosya geri "
    "gönderilir; gerekçenin eksikliği ise gerekçe değiştirilerek istinafın reddini gerektirir.", zorluk="hard")

P.sayisal("İYUK md. 46",
    f"{K}, temyize açık kararlar kararın tebliğinden itibaren kaç gün içinde Danıştayda temyiz edilebilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 46/1'e göre Danıştay dava dairelerinin nihai kararları ile bölge idare mahkemelerinin sayılan davalardaki kararları "
    "tebliğden itibaren otuz gün içinde temyiz edilebilir.")

P.q("İYUK md. 45",
    f"{K}, istinafa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kararı veren hâkim istinaf incelemesinde görev alabilir.",
    ["İstinaf temyizin şekil ve usullerine tabidir.",
     "Dilekçedeki hitaba bakılmaksızın dosya BİM’e gönderilir.",
     "Temyize açık olmayan BİM kararları kesindir.",
     "İvedi yargılama davalarında istinafa başvurulamaz."],
    "Md. 45/7'ye göre istinafa konu kararı veren veya karara katılan hâkim aynı davanın istinaf incelemesinde bulunamaz.")

P.q("İYUK md. 46",
    f"{K}, aşağıdaki davalardan hangisinde bölge idare mahkemesi kararına karşı temyiz yoluna başvurulamaz?",
    "Uyarma cezasına karşı dava",
    ["Düzenleyici işleme karşı iptal davası",
     "Meslekten çıkarma işlemine karşı dava",
     "İmar planına karşı dava",
     "Maden mevzuatına ilişkin dava"],
    "Md. 46/1'e göre düzenleyici işlemler, meslekten veya kamu görevinden çıkarma, imar planları ve maden-orman mevzuatına "
    "ilişkin davalarda BİM kararları temyize açıktır; uyarma cezası bu hâllerden değildir.")

P.sayisal("İYUK md. 48",
    "Temyiz dilekçesi md. 3’teki esaslara göre düzenlenmemiştir ve eksiklerin tamamlanması temyiz edene tebliğ edilmiştir."
    f"\n\n{K}, eksiklikler kaç gün içinde tamamlanmalıdır?",
    "15", ["3", "7", "10", "30"],
    "Md. 48/2'ye göre eksikliklerin on beş gün içinde tamamlatılması ilgiliye tebliğ olunur; tamamlanmazsa temyiz isteminde "
    "bulunulmamış sayılmasına karar verilir.")

P.oncul("İYUK md. 46",
    f"{K} bölge idare mahkemesinin aşağıdaki davalarda verdiği kararlar değerlendirilmektedir:",
    ["Öğrencilik statüsünden çıkarma işlemine karşı iptal davası",
     "Kamu görevlisinin yıllık izin talebinin reddine karşı dava",
     "Kültür Varlıklarını Koruma Yüksek Kurulunun itiraz kararına karşı dava",
     "Ülke çapında yapılan meslek sınavına ilişkin dava"],
    "Bu kararlardan hangileri Danıştayda temyiz edilebilir?",
    "I, III ve IV",
    ["I ve II", "II ve III", "III ve IV", "I, III ve IV", "I, II, III ve IV"],
    "Md. 46/1'e göre öğrencilik statüsünden çıkarma (I), Kültür Varlıklarını Koruma Yüksek Kurulu itiraz kararları (III) ve "
    "ülke çapındaki sınavlar (IV) temyize açıktır; yıllık izin talebinin reddi (II) sayılmamıştır.", zorluk="hard")

P.q("İYUK md. 46",
    f"{K}, aşağıdakilerden hangisi temyize açık davalar arasında sayılmıştır?",
    "Müşterek kararnameyle yapılan atamalar",
    ["Şube müdürünün naklen ataması",
     "Memurun aylıksız izin talebinin reddi",
     "Öğrenciye verilen kınama cezası",
     "Belediye zabıtasının park cezası"],
    "Md. 46/1-f'ye göre müşterek kararnameyle yapılan atama ve görevden alma işlemleri ile daire başkanı ve üstü görevlilerin "
    "atama işlemlerine karşı açılan davalarda BİM kararları temyiz edilebilir.")

P.sayisal("İYUK md. 48",
    "Temyiz dilekçesi verilirken gerekli harç ve giderlerin tamamı ödenmemiştir."
    f"\n\n{K}, eksik harç ve giderlerin tamamlanması için temyiz edene kaç günlük süre verilir?",
    "7", ["3", "10", "15", "30"],
    "Md. 48/6'ya göre harç ve giderlerin yedi günlük süre içinde tamamlanması, aksi hâlde temyizden vazgeçilmiş sayılacağı "
    "temyiz edene yazılı olarak bildirilir.", zorluk="hard")

P.q("İYUK md. 48",
    f"{K}, temyiz dilekçesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dilekçe Adalet Bakanlığına hitaben yazılır.",
    ["Dilekçe md. 3 esaslarına göre düzenlenir.",
     "Dilekçe kararı veren mercie de verilebilir.",
     "Dilekçe karşı tarafa tebliğ edilir.",
     "Cevap veren taraf da temyiz isteyebilir."],
    "Md. 48/1'e göre temyiz istemleri Danıştay Başkanlığına hitaben yazılmış dilekçelerle yapılır.", zorluk="easy")

P.q("İYUK md. 48",
    "Kararı süresinde temyiz etmeyen davalı idare, davacının temyiz dilekçesine süresi içinde cevap vermektedir."
    f"\n\n{K}, davalı idarenin bu aşamadaki temyiz hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Cevap dilekçesinde temyiz isteyebilir.",
    ["Süresi geçtiği için temyiz edemez.",
     "Ancak ayrı ve harçsız dilekçeyle temyiz edebilir.",
     "Sadece kanun yararına temyize gidebilir.",
     "Davacının rızasıyla temyiz edebilir."],
    "Md. 48/3'e göre cevap veren, kararı süresinde temyiz etmemiş olsa bile cevap dilekçesinde temyiz isteminde "
    "bulunabilir; bu dilekçe temyiz dilekçesi yerine geçer.", zorluk="hard")

P.sayisal("İYUK md. 48",
    f"{K}, temyiz dilekçesinin tebliğ edildiği karşı taraf, tebliğ tarihini izleyen kaç gün içinde cevap verebilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 48/3'e göre karşı taraf temyiz dilekçesinin tebliğ tarihini izleyen otuz gün içinde cevap verebilir.")

P.q("İYUK md. 48",
    f"{K}, temyizin kanuni süre geçtikten sonra yapılması hâlinde temyiz isteminin reddine hangi merci karar verir?",
    "Kararı veren merci",
    ["Danıştay Başsavcılığı", "Anayasa Mahkemesi", "Adalet Bakanlığı", "Uyuşmazlık Mahkemesi"],
    "Md. 48/6'ya göre temyizin kanuni süre geçtikten sonra yapılması veya kesin bir karar hakkında olması hâlinde kararı veren "
    "merci temyiz isteminin reddine karar verir.")

P.q("İYUK md. 49",
    f"{K}, temyiz incelemesi sonunda Danıştayın kararı bozma sebepleri arasında aşağıdakilerden hangisi yer almaz?",
    "Kararın oyçokluğuyla verilmiş olması",
    ["Görev ve yetki dışında bir işe bakılmış olması",
     "Hukuka aykırı karar verilmesi",
     "Usul hükümlerinde kararı etkileyecek hata olması",
     "Usul hükümlerinde kararı etkileyecek eksiklik olması"],
    "Md. 49/2'ye göre Danıştay görev ve yetki dışında bir işe bakılması, hukuka aykırı karar ve kararı etkileyebilecek usul "
    "hatası veya eksikliği sebepleriyle kararı bozar; oyçokluğu bozma sebebi değildir.", zorluk="easy")

P.sayisal("İYUK md. 48",
    "Kararı veren merci, temyizin kanuni süre geçtikten sonra yapıldığı gerekçesiyle temyiz isteminin reddine karar vermiştir."
    f"\n\n{K}, bu karara karşı tebliğ tarihini izleyen kaç gün içinde temyiz yoluna başvurulabilir?",
    "7", ["3", "10", "15", "30"],
    "Md. 48/6'ya göre kararı veren merciin süre aşımı, kesin karar ve temyiz edilmemiş sayılma kararlarına karşı tebliğ "
    "tarihini izleyen günden itibaren yedi gün içinde temyiz yoluna başvurulabilir.", zorluk="hard")

P.q("İYUK md. 49",
    f"{K}, temyiz incelemesinde Danıştayın verebileceği kararlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gerekçesi eksik olan kararı doğrudan bozar.",
    ["Hukuka uygun kararı onar.",
     "Sonucu doğru kararı gerekçesini değiştirerek onar.",
     "Maddi hatayı düzelterek onayabilir.",
     "Kısmen onama ve kısmen bozma kararı verebilir."],
    "Md. 49/1'e göre kararın sonucu hukuka uygun olmakla birlikte gerekçesi doğru veya yeterli değilse Danıştay kararı "
    "gerekçesini değiştirerek onar.")

P.q("İYUK md. 50",
    f"{K}, Danıştayın bozma kararı üzerine bölge idare mahkemesinin yapabileceklerine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Uyabilir veya ısrar edebilir.",
    ["Bozmaya uymakla yükümlüdür.",
     "Dosyayı Anayasa Mahkemesine göndermelidir.",
     "Davayı düşürmekle yükümlüdür.",
     "Sadece yeni bilirkişi incelemesi yapabilir."],
    "Md. 50/3'e göre bölge idare mahkemesi Danıştayca verilen bozma kararına uyabileceği gibi kararında ısrar da edebilir.")

P.sayisal("İYUK md. 53",
    f"{K}, yargılamanın yenilenmesi, (h) ve (ı) bentleri dışındaki sebepler için kaç gün içinde istenebilir?",
    "60", ["15", "30", "90", "120"],
    "Md. 53/3'e göre yargılamanın yenilenmesi süresi (h) bendi için on yıl, (ı) bendi için AİHM kararının kesinleşmesinden "
    "itibaren bir yıl, diğer sebepler için altmış gündür.")

P.q("İYUK md. 50",
    "Bölge idare mahkemesi Danıştayın bozma kararına uymayarak ısrar kararı vermiş, bu karar temyiz edilmiştir."
    f"\n\n{K}, ısrar kararının temyizini kim inceler?",
    "Danıştay İdari veya Vergi Dava Daireleri Kurulu",
    ["Bozma kararı veren Danıştay dairesi", "Aynı bölge idare mahkemesi", "Anayasa Mahkemesi",
     "Danıştay Başkanlar Kurulu"],
    "Md. 50/5'e göre ısrar kararının temyizi hâlinde talep, konusuna göre Danıştay İdari veya Vergi Dava Daireleri Kurulunca "
    "incelenir; Kurul kararlarına uyulması zorunludur.")

P.q("İYUK md. 50",
    f"{K}, temyiz üzerine verilen kararlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kurulların kararlarına uyulması isteğe bağlıdır.",
    ["Bozmaya uyulursa temyiz incelemesi bozmaya uygunlukla sınırlıdır.",
     "Bozma üzerine ilgili merci dosyayı öncelikle inceler.",
     "Onama kararları ilk derece mahkemesine gönderilir.",
     "Onama kararları yedi gün içinde tebliğe çıkarılır."],
    "Md. 50/5'e göre Danıştay İdari ve Vergi Dava Daireleri Kurulları kararlarına uyulması zorunludur.")

P.sayisal("İYUK md. 53",
    f"{K}, aynı taraflar, konu ve sebeple verilmiş önceki ilama aykırı karar verilmesine dayanan yargılamanın yenilenmesi "
    "istemi kaç yıl içinde yapılabilir?",
    "10", ["1", "2", "5", "20"],
    "Md. 53/3'e göre (1) numaralı fıkranın (h) bendinde yazılı sebep için yargılamanın yenilenmesi süresi on yıldır.",
    zorluk="hard")

P.q("İYUK md. 51",
    f"{K}, kanun yararına temyize ilişkin aşağıdakilerden hangisi doğrudur?",
    "Başsavcı tarafından başvurulur.",
    ["Taraflar tarafından başvurulur.",
     "Bozma kararı önceki kararın sonuçlarını kaldırır.",
     "Sadece istinaftan geçmiş kararlar için kullanılır.",
     "Bozma kararı gizli tutulur."],
    "Md. 51'e göre kesin veya kanun yoluna gidilmeden kesinleşmiş hukuka aykırı kararlar ilgili bakanlıkların lüzumu üzerine "
    "veya kendiliğinden Başsavcı tarafından kanun yararına temyiz olunabilir.")

P.q("İYUK md. 51",
    f"{K}, kanun yararına bozma kararının sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kesinleşmiş kararın hukuki sonuçlarını kaldırır.",
    ["Bozma kararının örneği ilgili bakanlığa gönderilir.",
     "Bozma kararı Resmî Gazete’de yayımlanır.",
     "Başvuru bakanlığın lüzumu üzerine yapılabilir.",
     "Başsavcı resen de başvurabilir."],
    "Md. 51/2'ye göre kanun yararına bozma kararı, daha önce kesinleşmiş olan merci kararının hukuki sonuçlarını kaldırmaz.",
    zorluk="hard")

P.sayisal("İYUK md. 53",
    f"{K}, AİHM’in kesinleşmiş ihlal kararına dayanan yargılamanın yenilenmesi istemi, kararın kesinleştiği tarihten "
    "itibaren kaç yıl içinde yapılabilir?",
    "1", ["2", "3", "5", "10"],
    "Md. 53/3'e göre (ı) bendindeki sebep için süre AİHM kararının kesinleştiği tarihten itibaren bir yıldır.", zorluk="hard")

P.q("İYUK md. 52",
    f"{K}, temyiz veya istinafa başvurulmasının kararın yürütülmesine etkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kararın yürütülmesini durdurmaz.",
    ["Kararın yürütülmesini doğrudan durdurur.",
     "Sadece iptal kararlarının yürütülmesini durdurur.",
     "İdare aleyhine kararların yürütülmesini durdurur.",
     "Vergi davalarında kararın yürütülmesini durdurur."],
    "Md. 52/1'e göre temyiz veya istinaf yoluna başvurulmuş olması hâkim, mahkeme veya Danıştay kararlarının yürütülmesini "
    "durdurmaz; teminat karşılığında yürütmenin durdurulmasına karar verilebilir.")

P.q("İYUK md. 52",
    f"{K}, temyiz ve istinaf aşamasında yürütmenin durdurulmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bu aşamadaki YD kararlarına itiraz edilir.",
    ["İptal davalarında teminat istenmeyebilir.",
     "İdareden teminat alınmaz.",
     "Kararın bozulması yürütmeyi durdurur.",
     "Adli yardımdan yararlananlardan teminat alınmaz."],
    "Md. 52/4'e göre temyiz ve istinaf incelemesi sırasında yürütmenin durdurulması istemleri hakkında verilen kararlar "
    "kesindir.", zorluk="hard")

P.sayisal("İYUK md. 46",
    f"{K}, belli bir ticari faaliyetin icrasını en az kaç gün süreyle engelleyen işlemlere karşı açılan iptal davalarında "
    "bölge idare mahkemesi kararları temyize açıktır?",
    "30", ["7", "15", "60", "90"],
    "Md. 46/1-e'ye göre belli bir ticari faaliyetin icrasını süresiz veya otuz gün yahut daha uzun süreyle engelleyen "
    "işlemlere karşı açılan iptal davalarında verilen kararlar temyiz edilebilir.", zorluk="hard")

P.q("İYUK md. 52",
    "İlk derece mahkemesi davayı reddetmiş, davacı istinaf yoluna başvurarak dava konusu işlem hakkında yürütmenin "
    f"durdurulmasını istemiştir.\n\n{K}, bu istemin kabulü aşağıdakilerden hangisine bağlıdır?",
    "Md. 27’deki koşulların varlığına",
    ["Davacının teminat yatırmasına",
     "İdarenin rızasına",
     "Duruşma yapılmasına",
     "Karar düzeltme yoluna gidilmesine"],
    "Md. 52/1'e göre davanın reddine ilişkin kararlara karşı kanun yoluna başvurulması hâlinde dava konusu işlem hakkında "
    "yürütmenin durdurulması, md. 27'deki koşulların varlığına bağlıdır.", zorluk="hard")

P.q("İYUK md. 53",
    f"{K}, aşağıdakilerden hangisi yargılamanın yenilenmesi sebeplerinden biri değildir?",
    "Karardan sonra içtihadın değişmesi",
    ["Karara esas belgenin sahteliğine hükmedilmesi",
     "Bilirkişinin kasten gerçeğe aykırı beyanı",
     "Lehine karar verilenin hile kullanması",
     "Çekinmesi gereken hâkimin karara katılması"],
    "Md. 53/1'e göre sahte belge, bilirkişinin kasıtlı gerçeğe aykırı beyanı, hile, çekinmesi gereken hâkimin katılması gibi "
    "hâller yenileme sebebidir; içtihat değişikliği sayılmamıştır.")

P.sayisal("İYUK md. 45",
    f"{K}, bölge idare mahkemelerinin temyize açık olmayan kararları dosyayla birlikte ilk derece mahkemesine gönderilir; "
    "bu kararlar ilk derece mahkemesince kaç gün içinde tebliğe çıkarılır?",
    "7", ["3", "10", "15", "30"],
    "Md. 45/6'ya göre temyize açık olmayan BİM kararları kesindir; dosyayla birlikte kararı veren ilk derece mahkemesine "
    "gönderilir ve bu mahkemece yedi gün içinde tebliğe çıkarılır.", zorluk="hard")

P.q("İYUK md. 53",
    f"{K}, yargılamanın yenilenmesi istemi hakkında hangi merci karar verir?",
    "Esas kararı vermiş olan mahkeme",
    ["Danıştay Başkanlar Kurulu", "Anayasa Mahkemesi", "Bölge adliye mahkemesi", "Adalet Bakanlığı"],
    "Md. 53/2'ye göre yargılamanın yenilenmesi istekleri esas kararı vermiş olan mahkemece karara bağlanır.")

P.q("İYUK md. 53",
    f"{K}, yargılamanın yenilenmesi sürelerinin başlangıcına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sebebin istemde bulunan yönünden gerçekleştiği tarihi izler.",
    ["Kararın verildiği tarihte başlar.",
     "Davanın açıldığı tarihte başlar.",
     "Kararın kesinleşmesinden bir yıl sonra başlar.",
     "Takvim yılı başında başlar."],
    "Md. 53/3'e göre süreler dayanılan sebebin istemde bulunan yönünden gerçekleştiği tarihi izleyen günden başlatılarak "
    "hesaplanır.")

P.q("İYUK md. 45",
    f"{K26}, bölge idare mahkemesinin md. 48/7 uyarınca verdiği kararlara karşı kanun yoluna ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Yedi gün içinde temyize gidilir.",
    ["Bu kararlar kesin olup kanun yolu kapalıdır.",
     "Otuz gün içinde istinafa başvurulur.",
     "Altmış gün içinde temyiz edilir.",
     "On beş gün içinde itiraz edilir."],
    "Md. 45/2'ye 7524 sayılı Kanunla 2024'te eklenen cümleye göre bölge idare mahkemesinin md. 48/7 uyarınca verdiği kararlara "
    "karşı tebliğ tarihini izleyen günden itibaren yedi gün içinde temyiz yoluna başvurulabilir.", zorluk="hard")

P.q("İYUK md. 49",
    f"{K}, temyiz incelemesinde görev alamayacak hâkime ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kararı veren veya karara katılan hâkim",
    ["Aynı ilde görev yapan her hâkim",
     "Davacıyla aynı meslekten olan hâkim",
     "Daha önce aynı idareye karşı dava bakmış hâkim",
     "Danıştayda beş yıldan az görev yapmış hâkim"],
    "Md. 49/5'e göre temyize konu edilen kararı veren ya da karara katılan hâkim aynı davanın temyiz incelemesinde görev "
    "alamaz.")

P.q("İYUK md. 45",
    f"{K26}, bölge idare mahkemesinin istinaf üzerine kararı kaldırıp dosyayı geri göndermesi yerine eksikliği kendisi "
    "gidererek karar verebileceği hâl aşağıdakilerden hangisidir?",
    "Gerekli keşfin yapılmamış olması",
    ["Davaya görevsiz mahkemece bakılması",
     "Dilekçe reddi gerekirken esasa girilmesi",
     "Dosyanın yanlış hasımla tekemmül ettirilmesi",
     "Reddedilmiş hâkimin davaya bakması"],
    "Md. 45/5'e göre keşif veya bilirkişi incelemesi ya da duruşma yapılması gerektiği hâlde yapılmadan karar verilmesi "
    "hâllerinde bölge idare mahkemesi bu eksikliği kendisi gidererek karar verebilir.", zorluk="hard")

P.q("İYUK md. 7",
    f"{K}, idarenin dava açması gereken konularda dava açma süresi hangi tarihi izleyen günden başlar?",
    "Kararın idareye geldiği tarih",
    ["İdarenin dava açmaya karar verdiği tarih",
     "Mükellefin ödeme yaptığı tarih",
     "Takvim yılının sona erdiği tarih",
     "Uyuşmazlık konusu işlemin yapıldığı tarih"],
    "Md. 7/2-b'ye göre idarenin dava açması gereken konularda süre ilgili merci veya komisyon kararının idareye geldiği tarihi "
    "izleyen günden başlar.", zorluk="hard")

P.q("İYUK md. 45",
    f"{K26}, aşağıdaki ilk derece kararlarından hangisine karşı istinaf yoluna başvurulamaz?",
    "Sınırı aşmayan vergi davası kararı",
    ["Düzenleyici işlem iptal kararı",
     "Meslekten çıkarma işlemine ilişkin karar",
     "İmar planına ilişkin karar",
     "Sınırı aşan tam yargı davası kararı"],
    "Md. 45/1'e göre konusu Kanundaki parasal sınırı geçmeyen vergi davaları, tam yargı davaları ve idari işlemlere karşı "
    "açılan iptal davaları hakkındaki kararlar kesindir; sınır her yıl yeniden değerleme oranında güncellenir.",
    zorluk="hard")

P.q("İYUK md. 8",
    f"{K}, süreler hangi günden itibaren işlemeye başlar?",
    "Tebliğ, yayın veya ilanı izleyen gün",
    ["Tebliğin yapıldığı gün",
     "Tebliğden sonraki ikinci gün",
     "İşlemin imzalandığı gün",
     "Tebliğden sonraki ilk iş gününün mesai bitiminden sonra"],
    "Md. 8/1'e göre süreler tebliğ, yayın veya ilan tarihini izleyen günden itibaren işlemeye başlar.", zorluk="easy")

P.q("İYUK md. 49",
    f"{K}, temyiz incelemesinde kararın kısmen onanıp kısmen bozulması hâlinde aşağıdakilerden hangisi doğrudur?",
    "Kesinleşen kısım kararda belirtilir.",
    ["Kararın tamamı bozulmuş sayılır.",
     "Onanan kısım da yeniden incelenir.",
     "Kesinleşme ancak ısrar kararıyla olur.",
     "Dosya Anayasa Mahkemesine gönderilir."],
    "Md. 49/3'e göre kararların kısmen onanması ve kısmen bozulması hâllerinde kesinleşen kısım Danıştay kararında "
    "belirtilir.")

P.q("İYUK md. 53",
    f"{K}, aşağıdakilerden hangisi yargılamanın yenilenmesi sebeplerinden biridir?",
    "AİHM’de dostane çözümle düşme kararı",
    ["Kararın oyçokluğuyla verilmesi",
     "Davacının yeni avukat tutması",
     "Mahkemenin yoğun iş yükü",
     "Aynı konuda başka mahkemede farklı içtihat bulunması"],
    "Md. 53/1-ı'ya göre hüküm aleyhine AİHM'e yapılan başvuru hakkında dostane çözüm veya tek taraflı deklarasyon sonucunda "
    "düşme kararı verilmesi yargılamanın yenilenmesi sebebidir.", zorluk="hard")

P.q("İYUK md. 48",
    f"{K}, kararı veren merci temyiz dosyasını Danıştaya ne zaman gönderir?",
    "Cevap verildikten veya süre geçtikten sonra",
    ["Temyiz dilekçesinin verildiği gün",
     "Karar kesinleştikten sonra",
     "Danıştay talep ettiğinde",
     "YD kararından sonra ve cevap beklenmeden hemen"],
    "Md. 48/4'e göre kararı veren Danıştay veya bölge idare mahkemesi, cevap dilekçesi verildikten veya cevap süresi geçtikten "
    "sonra dosyayı dizi listesine bağlı olarak Danıştaya veya Kurula gönderir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
