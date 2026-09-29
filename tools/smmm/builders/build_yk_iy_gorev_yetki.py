# -*- coding: utf-8 -*-
"""Hukuk · İdari Yargılama Hukuku · Görev, Yetki ve İlk İnceleme — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında İYUK soruları "2577 sayılı İdari Yargılama Usulü Kanunu’na göre …" kalıbıyla; ilk
incelemede bakılacak hususlar, dilekçenin verileceği yerler ve yetkili mahkeme gibi kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 2577 sayılı İYUK md. 1-5, 9, 14-15, 24, 26, 32-44.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_idari_yargi_gorev_yetki_2026.json", lesson="idari_yargilama_hukuku",
          topic="idari_yargi_gorev_yetki", konu_adi="İdari Yargıda Görev ve Yetki", seed=2026093007,
          surum="2577 sayılı İYUK güncel metni; 29.09.2026 kontrolü")

K = "2577 sayılı İdari Yargılama Usulü Kanunu’na göre"
K26 = "2577 sayılı İdari Yargılama Usulü Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

P.sayisal("İYUK md. 9",
    "Bir idari işleme karşı adli yargıda açılan dava görev yönünden reddedilmiş ve karar kesinleşmiştir."
    f"\n\n{K}, kararın kesinleşmesini izleyen günden itibaren kaç gün içinde görevli idari yargı merciinde dava açılabilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 9'a göre adli yargıda açılan davanın görev yönünden reddi hâlinde kararın kesinleşmesini izleyen günden itibaren "
    "otuz gün içinde görevli mahkemede dava açılabilir; görevsiz yere başvurma tarihi idari yargıya başvurma tarihi sayılır.")

P.q("İYUK md. 14",
    f"{K}, aşağıdakilerden hangisi dilekçeler üzerine yapılacak ilk inceleme konularından biri değildir?",
    "Davanın esastan haklılığı",
    ["Görev ve yetki", "İdari merci tecavüzü", "Süre aşımı", "Husumet"],
    "Md. 14/3'e göre ilk incelemede görev ve yetki, idari merci tecavüzü, ehliyet, kesin ve yürütülmesi gereken işlem, süre "
    "aşımı, husumet ve md. 3 ile 5'e uygunluk incelenir; davanın esası ilk inceleme konusu değildir.", zorluk="easy")

P.q("İYUK md. 14",
    f"{K}, dava dilekçeleri ilk incelemede hangi sırayla incelenir?",
    "Kanunda sayılan sırayla",
    ["Husumetten başlanarak ters sırayla",
     "Süre aşımından başlanarak",
     "Mahkemenin kendi belirlediği sırayla",
     "Davacının talep ettiği sırayla"],
    "Md. 14/3'e göre dilekçeler görev ve yetki, idari merci tecavüzü, ehliyet, kesin ve yürütülmesi gereken işlem, süre aşımı, "
    "husumet ve md. 3-5'e uygunluk yönlerinden sırasıyla incelenir.")

P.sayisal("İYUK md. 6",
    f"{K}, asliye hukuk hâkimliğine verilen bir dava dilekçesi en geç kaç gün içinde ait olduğu mahkeme başkanlığına "
    "taahhütlü olarak gönderilir?",
    "3", ["1", "2", "5", "7"],
    "Md. 6'ya göre md. 4'te yazılı diğer yerlere verilen dilekçeler en geç üç gün içinde Danıştay veya ait olduğu mahkeme "
    "başkanlığına taahhütlü olarak gönderilir.", zorluk="hard")

P.oncul("İYUK md. 14",
    f"{K} aşağıdaki hususlar değerlendirilmektedir:",
    ["Ehliyet", "İdari işlemin yerindeliği", "Süre aşımı", "Tanıkların güvenilirliği"],
    "Yukarıdakilerden hangileri ilk inceleme konuları arasında yer alır?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 14/3'e göre ehliyet (I) ve süre aşımı (III) ilk inceleme konusudur; idari işlemin yerindeliği (II) idari yargının "
    "denetim alanı dışında kalır, tanıkların güvenilirliği (IV) ilk inceleme konusu değildir.")

P.q("İYUK md. 15",
    f"{K}, ilk incelemede adli yargının görevli olduğu bir konuda açıldığı anlaşılan dava hakkında hangi karar verilir?",
    "Davanın reddine",
    ["Dosyanın adli mahkemeye gönderilmesine",
     "Dilekçenin görevli idareye tevdiine",
     "Dilekçenin gerçek hasma tebliğine",
     "Dosyanın işlemden kaldırılmasına"],
    "Md. 15/1-a'ya göre adli yargının görevli olduğu konularda açılan davaların reddine karar verilir; idari yargının görevli "
    "olduğu konularda görevli veya yetkili olmayan mahkemeye açılan dava ise reddedilerek dosya görevli mahkemeye gönderilir.")

P.sayisal("İYUK md. 6",
    "Bir dava, harç ve posta ücreti hiç verilmeden açılmıştır."
    f"\n\n{K}, harcın ve posta ücretinin tamamlanması için ilgiliye kaç günlük süre tebliğ olunur?",
    "30", ["7", "10", "15", "60"],
    "Md. 6'ya göre harç veya posta ücreti verilmeden ya da eksik verilerek dava açılmışsa otuz gün içinde tamamlanması "
    "ilgiliye tebliğ olunur; tebligata rağmen yerine getirilmezse bildirim bir kez daha tekrarlanır.")

P.q("İYUK md. 15",
    f"{K}, idari yargının görev alanına giren ancak yetkisiz idare mahkemesine açılan dava hakkında ilk incelemede ne "
    "yapılır?",
    "Yetkiden ret ve dosyanın gönderilmesi",
    ["Esastan reddedilir.",
     "Dilekçe görevli idareye tevdi edilir.",
     "Dava açılmamış sayılır.",
     "Dosya Anayasa Mahkemesine gönderilir."],
    "Md. 15/1-a'ya göre idari yargının görevli olduğu konularda yetkili olmayan mahkemeye açılan dava yetki yönünden "
    "reddedilerek dosya yetkili mahkemeye gönderilir.")

P.q("İYUK md. 15",
    "Davacı, dava dilekçesinde davalı idareyi göstermemiştir."
    f"\n\n{K}, ilk incelemede bu durumda hangi karar verilir?",
    "Gerçek hasma tebliğine",
    ["Davanın husumetten reddine",
     "Davanın açılmamış sayılmasına",
     "Dilekçenin görevli idareye tevdiine",
     "Dosyanın Danıştaya gönderilmesine"],
    "Md. 15/1-c'ye göre davanın hasım gösterilmeden veya yanlış hasım gösterilerek açılması hâlinde dava dilekçesinin tespit "
    "edilecek gerçek hasma tebliğine karar verilir.")

P.sayisal("İYUK md. 14",
    f"{K}, ilk inceleme ve buna bağlı işlemler dilekçenin alındığı tarihten itibaren en "
    "geç kaç gün içinde sonuçlandırılır?",
    "15", ["3", "7", "30", "60"],
    "Md. 14'e göre ilk inceleme ile rapor ve tebligat işlemleri dilekçenin alındığı tarihten itibaren en geç on beş gün "
    "içinde sonuçlandırılır.", zorluk="hard")

P.q("İYUK md. 15",
    f"{K}, ilk incelemede idari merci tecavüzü tespit edilirse aşağıdaki kararlardan hangisi verilir?",
    "Görevli merciye tevdiine",
    ["Davanın esastan reddine",
     "Dilekçenin gerçek hasma tebliğine",
     "Dosyanın adli yargıya gönderilmesine",
     "Otuz gün içinde yeni dilekçe verilmesine"],
    "Md. 15/1-e'ye göre md. 14/3-b'deki idari merci tecavüzü hâlinde dilekçelerin görevli idare merciine tevdiine karar "
    "verilir; bu durumda mahkemeye başvurma tarihi merciye başvurma tarihi sayılır.", zorluk="hard")

P.q("İYUK md. 15",
    f"{K}, ilk inceleme üzerine verilen kararlardan hangisine karşı istinaf veya temyiz yoluna başvurulabilir?",
    "Süre aşımı nedeniyle davanın reddi",
    ["Gerçek hasma tebliğ kararı",
     "Yetki yönünden ret ve gönderme kararı",
     "Dilekçe ret kararı",
     "Görev yönünden ret ve gönderme kararı"],
    "Md. 15/4'e göre idari yargının görevli olduğu konularda görev ve yetki yönünden ret, gerçek hasma tebliğ ve dilekçe ret "
    "kararları dışındaki ilk inceleme kararlarına karşı istinaf veya temyiz yoluna başvurulabilir.", zorluk="hard")

P.sayisal("İYUK md. 15",
    "Dava dilekçesi, md. 3’te sayılan unsurları taşımadığı için ilk incelemede reddedilmiştir."
    f"\n\n{K}, davacı dilekçesini kaç gün içinde yeniden düzenleyerek verebilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 15/1-d'ye göre md. 3 ve 5'e uygun olmayan dilekçeler otuz gün içinde yeniden düzenlenmek veya noksanları "
    "tamamlanmak üzere reddedilir.")

P.q("İYUK md. 15",
    f"{K}, ilk incelemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Dilekçe reddinde yeni dilekçeye tekrar harç alınır.",
    ["Merciye tevdide mahkemeye başvuru tarihi esas alınır.",
     "Aynı yanlışlıkla yenilenen dilekçede dava reddedilir.",
     "Ehliyet yokluğunda davanın reddine karar verilir.",
     "Süre aşımında davanın reddine karar verilir."],
    "Md. 15/3'e göre dilekçelerin md. 3'e uygun olmamaları nedeniyle reddi hâlinde yeni dilekçeler için ayrıca harç alınmaz.")

P.q("İYUK md. 4",
    f"{K}, idare veya vergi mahkemesi bulunmayan bir yerde dava dilekçesi aşağıdakilerden hangisine verilebilir?",
    "Asliye hukuk hâkimliğine",
    ["Sulh ceza hâkimliğine", "Kaymakamlığa", "Noterliğe", "Belediye başkanlığına"],
    "Md. 4'e göre dilekçeler idare veya vergi mahkemesi bulunmayan yerlerde, büyükşehir belediyesi sınırları içinde kalıp "
    "kalmadığına bakılmaksızın asliye hukuk hâkimliklerine, yabancı ülkelerde Türk konsolosluklarına verilebilir.",
    zorluk="easy")

P.sayisal("İYUK md. 41",
    f"{K}, bağlantı iddiasının mahkemece kabul edilmemesine ilişkin ara karar tebliğ edilen taraflar, tebliğ tarihini "
    "izleyen kaç gün içinde bölge idare mahkemesine veya Danıştaya başvurabilir?",
    "15", ["7", "10", "30", "60"],
    "Md. 41'e göre bağlantı iddiaları mahkemelerce kabul edilmezse taraflar ara kararın tebliğini izleyen on beş gün içinde "
    "bölge idare mahkemesine veya Danıştaya başvurabilir.", zorluk="hard")

P.q("İYUK md. 4",
    f"{K}, yurt dışında bulunan bir davacı idari dava dilekçesini aşağıdakilerden hangisine verebilir?",
    "Türk konsolosluğuna",
    ["Bulunduğu ülkenin mahkemesine", "Yabancı ülkenin noterine", "Bulunduğu ülkenin belediyesine",
     "Uluslararası tahkim merkezine"],
    "Md. 4'e göre dilekçeler ve davalara ilişkin her türlü evrak yabancı memleketlerde Türk konsolosluklarına verilebilir.")

P.q("İYUK md. 3",
    f"{K}, dava dilekçesinde gösterilmesi gereken hususlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İptal davalarında uyuşmazlık miktarı gösterilir.",
    ["Tarafların ad, soyad ve adresleri gösterilir.",
     "Davanın konu ve sebepleri gösterilir.",
     "İşlemin yazılı bildirim tarihi gösterilir.",
     "Tam yargı davasında uyuşmazlık miktarı gösterilir."],
    "Md. 3/2'ye göre uyuşmazlık konusu miktar vergi ve benzeri mali yükümlere ilişkin davalarla tam yargı davalarında "
    "gösterilir; iptal davaları için böyle bir unsur öngörülmemiştir.")

P.sayisal("İYUK md. 26",
    "Davacının gösterdiği adrese tebligat yapılamadığı için dava dosyası işlemden kaldırılmıştır."
    f"\n\n{K}, yeni adres bildirilerek dosyanın işleme konulması en geç kaç yıl içinde istenmezse davanın açılmamış "
    "sayılmasına karar verilir?",
    "1", ["2", "3", "4", "5"],
    "Md. 26'ya göre adrese tebligat yapılamazsa dosya işlemden kaldırılır; işlemden kaldırıldığı tarihten başlayarak bir yıl "
    "içinde yeni adres bildirilmezse davanın açılmamış sayılmasına karar verilir.")

P.q("İYUK md. 3",
    f"{K}, idari davalar aşağıdakilerden hangisi ile açılır?",
    "İlgili başkanlığa hitaben yazılmış imzalı dilekçe",
    ["Sözlü başvuru ve tutanak", "İdareye verilen şikâyet yazısı", "Noter ihtarnamesi",
     "Kaymakamlığa yapılan sözlü itiraz"],
    "Md. 3/1'e göre idari davalar Danıştay, idare mahkemesi ve vergi mahkemesi başkanlıklarına hitaben yazılmış imzalı "
    "dilekçelerle açılır.", zorluk="easy")

P.q("İYUK md. 5",
    f"{K}, birden fazla idari işleme karşı tek dilekçeyle dava açılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İşlemler arasında bağlılık varsa mümkündür.",
    ["Koşulsuz olarak mümkündür.",
     "İşlemler aynı gün yapılmışsa mümkündür.",
     "Sadece vergi ve harç davalarında mümkündür, diğerlerinde değil.",
     "Mahkemenin izni varsa mümkündür."],
    "Md. 5/1'e göre her idari işlem aleyhine ayrı dava açılır; ancak aralarında maddi veya hukuki bağlılık ya da sebep-sonuç "
    "ilişkisi bulunan birden fazla işleme karşı bir dilekçeyle dava açılabilir.")

P.sayisal("İYUK md. 26",
    "Dava sürerken davacı ölmüş ve dosya işlemden kaldırılmıştır; dosyada verilmiş bir yürütmenin durdurulması kararı "
    f"vardır.\n\n{K}, kaç ay içinde yenileme dilekçesi verilmezse yürütmenin durdurulması kararı kendiliğinden hükümsüz kalır?",
    "4", ["1", "2", "3", "6"],
    "Md. 26'ya göre tarafın ölümü gibi sebeplerle dosya işlemden kaldırılmışsa, dört ay içinde yenileme dilekçesi verilmemesi "
    "hâlinde varsa yürütmenin durdurulması kararı kendiliğinden hükümsüz kalır.", zorluk="hard")

P.q("İYUK md. 5",
    f"{K}, birden fazla kişinin müşterek dilekçeyle dava açabilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İştirak ve sebep birliği gerekir.",
    ["Davacıların aynı ilde oturması yeterlidir.",
     "Davacıların akraba olması gerekir.",
     "Davacı sayısı üçü geçmemelidir.",
     "Müşterek dilekçeyle dava açılamaz."],
    "Md. 5/2'ye göre müşterek dilekçeyle dava açılabilmesi için davacıların hak veya menfaatlerinde iştirak bulunması ve "
    "davaya yol açan maddi olay veya hukuki sebeplerin aynı olması gerekir.")

P.q("İYUK md. 2",
    f"{K}, idari yargı yetkisinin sınırlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İdari mahkemeler yerindelik denetimi yapabilir.",
    ["Denetim hukuka uygunlukla sınırlıdır.",
     "Mahkemeler idari işlem yerine geçen karar veremez.",
     "Takdir yetkisini kaldıran karar verilemez.",
     "Yürütme görevini kısıtlayan karar verilemez."],
    "Md. 2/2'ye göre idari yargı yetkisi idari eylem ve işlemlerin hukuka uygunluğunun denetimi ile sınırlıdır; idari "
    "mahkemeler yerindelik denetimi yapamaz.", zorluk="easy")

P.sayisal("İYUK md. 6",
    "Dava açıldıktan sonra posta ücreti tebligatı engelleyecek şekilde azalmış, iki kez yapılan bildirime rağmen "
    f"tamamlanmadığı için dosya işlemden kaldırılmıştır.\n\n{K}, bu kararın tebliğinden itibaren kaç ay içinde dosyanın "
    "yeniden işleme konulması istenmezse davanın açılmamış sayılmasına karar verilir?",
    "3", ["1", "2", "4", "6"],
    "Md. 6/5'e göre posta ücreti tamamlanmazsa dosya işlemden kaldırılır; kararın tebliğinden başlayarak üç ay içinde noksan "
    "tamamlanarak yeniden işleme konulması istenmezse davanın açılmamış sayılmasına karar verilir.", zorluk="hard")

P.q("İYUK md. 1",
    f"{K}, idari yargı mercilerinde uygulanan yargılama usulü aşağıdakilerden hangisidir?",
    "Yazılı yargılama usulü",
    ["Sözlü yargılama usulü", "Basit yargılama usulü", "Seri muhakeme usulü", "Tahkim usulü"],
    "Md. 1/2'ye göre Danıştay, bölge idare mahkemeleri, idare ve vergi mahkemelerinde yazılı yargılama usulü uygulanır ve "
    "inceleme evrak üzerinde yapılır.", zorluk="easy")

P.q("İYUK md. 32",
    f"{K}, Kanunda veya özel kanunlarda yetkili mahkeme gösterilmemişse genel yetkili idare mahkemesi aşağıdakilerden "
    "hangisidir?",
    "İşlemi yapan merciin yeri mahkemesi",
    ["Davacının ikametgâhı mahkemesi",
     "Danıştayın belirlediği mahkeme",
     "İşlemin tebliğ edildiği yer mahkemesi",
     "Davacının seçeceği herhangi bir mahkeme"],
    "Md. 32'ye göre yetkili idare mahkemesi, dava konusu idari işlemi veya idari sözleşmeyi yapan idari merciin bulunduğu "
    "yerdeki idare mahkemesidir.", zorluk="easy")

P.sayisal("İYUK md. 16",
    f"{K}, Danıştayda ilk derece mahkemesi sıfatıyla görülen davalarda savcının esas hakkındaki düşüncesinin tebliğinden "
    "itibaren taraflar kaç gün içinde görüşlerini yazılı olarak bildirebilir?",
    "10", ["3", "7", "15", "30"],
    "Md. 16/6'ya göre Danıştayda ilk derece mahkemesi olarak görülen davalarda savcının yazılı düşüncesi taraflara tebliğ "
    "edilir; taraflar tebliğden itibaren on gün içinde görüşlerini yazılı bildirebilir.", zorluk="hard")

P.q("İYUK md. 32",
    f"{K}, idari yargıda yetki kuralının niteliğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yetki kamu düzenindendir.",
    ["Taraflar yetki sözleşmesi yapabilir.",
     "Yetki itirazı sadece davalı idarece ileri sürülebilir.",
     "Yetki ilk duruşmadan sonra incelenemez.",
     "Yetkisizlik kararına karşı itiraz edilemez."],
    "Md. 32/2'ye göre İYUK'un uygulanmasında yetki kamu düzenindendir; bu nedenle mahkemece kendiliğinden gözetilir.")

P.q("İYUK md. 33",
    f"{K}, kamu görevlilerinin atanması ve nakilleriyle ilgili davalarda yetkili mahkeme aşağıdakilerden hangisidir?",
    "Yeni veya eski görev yeri idare mahkemesi",
    ["Sadece Ankara idare mahkemesi",
     "Davacının doğum yeri idare mahkemesi",
     "İşlemi yapan bakanlığın bulunduğu yer mahkemesi",
     "Danıştay"],
    "Md. 33/1'e göre kamu görevlilerinin atanması ve nakilleriyle ilgili davalarda yetkili mahkeme, yeni veya eski görev yeri "
    "idare mahkemesidir.")

P.sayisal("İYUK md. 17",
    f"{K}, duruşma davetiyeleri duruşma gününden en az kaç gün önce taraflara gönderilir?",
    "30", ["7", "10", "15", "60"],
    "Md. 17/5'e göre duruşma davetiyeleri duruşma gününden en az otuz gün önce taraflara gönderilir.")

P.q("İYUK md. 33",
    "Konya’da görev yapan bir memur, emekliye sevk edilmesi işlemine karşı dava açacaktır; işlemi Ankara’daki genel müdürlük "
    f"yapmıştır.\n\n{K}, yetkili mahkeme aşağıdakilerden hangisidir?",
    "Konya İdare Mahkemesi",
    ["Ankara İdare Mahkemesi", "Danıştay", "Memurun doğum yeri idare mahkemesi", "Memurun seçeceği idare mahkemesi"],
    "Md. 33/2'ye göre kamu görevlilerinin görevlerine son verilmesi, emekli edilmeleri veya görevden uzaklaştırılmalarıyla "
    "ilgili davalarda yetkili mahkeme, kamu görevlisinin son görev yaptığı yer idare mahkemesidir.", zorluk="hard")

P.q("İYUK md. 33",
    f"{K}, görevle ilişiği kesmeyen disiplin cezalarına karşı açılan davalarda yetkili mahkeme aşağıdakilerden "
    "hangisidir?",
    "İlgilinin görevli bulunduğu yer mahkemesi",
    ["Cezayı veren merciin bulunduğu yer mahkemesi",
     "İlgilinin ikametgâhı mahkemesi",
     "Ankara idare mahkemesi",
     "İlgilinin ilk atandığı yer mahkemesi"],
    "Md. 33/3'e göre görevle ilişiğin kesilmesi sonucunu doğurmayan disiplin cezaları ile özlük ve parasal haklara ilişkin "
    "davalarda yetkili mahkeme ilgilinin görevli bulunduğu yer idare mahkemesidir.")

P.q("İYUK md. 34",
    "İstanbul’da bulunan bir bakanlık birimi, İzmir’deki bir taşınmazın kamulaştırılmasına karar vermiştir."
    f"\n\n{K}, bu işleme karşı açılacak davada yetkili mahkeme aşağıdakilerden hangisidir?",
    "İzmir İdare Mahkemesi",
    ["İstanbul İdare Mahkemesi", "Ankara İdare Mahkemesi", "Davacının ikametgâhı mahkemesi", "Danıştay"],
    "Md. 34/1'e göre imar, kamulaştırma, yıkım, işgal, tahsis, ruhsat ve iskân gibi taşınmaz mallarla ilgili davalarda yetkili "
    "mahkeme taşınmazın bulunduğu yer idare mahkemesidir.", zorluk="easy")

P.q("İYUK md. 34",
    f"{K}, köy ve belediyeler arasındaki sınır uyuşmazlıklarında yetkili mahkemeye ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Köy veya belediyenin bulunduğu yer",
    ["Davacının ikametgâhının bulunduğu yer",
     "İçişleri Bakanlığının bulunduğu yer",
     "Danıştay",
     "Valiliğin bulunduğu il merkezi"],
    "Md. 34/2'ye göre köy, belediye ve özel idareleri ilgilendiren davalarla sınır uyuşmazlıklarında yetkili mahkeme mülki "
    "idari birimin, köy, belediye veya mahallenin bulunduğu yahut yeni bağlandığı yer idare mahkemesidir.")

P.q("İYUK md. 35",
    f"{K}, taşınır mallara ilişkin davalarda yetkili mahkeme aşağıdakilerden hangisidir?",
    "Taşınır malın bulunduğu yer mahkemesi",
    ["Malın sahibinin ikametgâhı mahkemesi",
     "İşlemi yapan merciin bulunduğu yer mahkemesi",
     "Malın satın alındığı yer mahkemesi",
     "Ankara idare mahkemesi"],
    "Md. 35'e göre taşınır mallara ilişkin davalarda yetkili mahkeme taşınır malın bulunduğu yer idare mahkemesidir.")

P.q("İYUK md. 36",
    f"{K}, idari sözleşmeler dışındaki tam yargı davalarında yetkili mahkemenin belirlenmesine ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Davacının ikametgâhı kural olarak ilk sırada gelir.",
    ["İlk sırada zararı doğuran uyuşmazlıkta yetkili mahkeme gelir.",
     "Hizmetten doğan zararda hizmetin görüldüğü yer yetkilidir.",
     "Eylemden doğan zararda eylemin yapıldığı yer yetkilidir.",
     "Diğer hâllerde davacının ikametgâhı yetkilidir."],
    "Md. 36'ya göre yetkili mahkeme sırasıyla zararı doğuran uyuşmazlığı çözmeye yetkili mahkeme, hizmetin görüldüğü veya "
    "eylemin yapıldığı yer ve diğer hâllerde davacının ikametgâhı mahkemesidir.")

P.q("İYUK md. 36",
    "Belediyenin yürüttüğü yol yapım çalışması sırasında Bursa’daki aracına zarar gelen ve Ankara’da oturan davacı, zararın "
    f"tazmini için dava açacaktır.\n\n{K}, yetkili mahkeme aşağıdakilerden hangisidir?",
    "Bursa İdare Mahkemesi",
    ["Ankara İdare Mahkemesi", "Danıştay", "Davacının seçeceği mahkeme", "İstanbul İdare Mahkemesi"],
    "Md. 36/b'ye göre zarar bayındırlık ve ulaştırma gibi bir hizmetten veya idarenin eyleminden doğmuşsa hizmetin görüldüğü "
    "veya eylemin yapıldığı yer idare mahkemesi yetkilidir.", zorluk="hard")

P.q("İYUK md. 37",
    f"{K}, 6183 sayılı Kanunun uygulanmasından doğan vergi uyuşmazlıklarında yetkili vergi mahkemesi aşağıdakilerden "
    "hangisidir?",
    "Ödeme emrini düzenleyen daire yeri",
    ["Borçlunun ikametgâhının bulunduğu yer",
     "Borcun doğduğu işlemin yapıldığı yer",
     "Maliye Bakanlığının bulunduğu yer",
     "Haczin uygulandığı malın bulunduğu yer"],
    "Md. 37/c'ye göre Amme Alacaklarının Tahsil Usulü Kanununun uygulanmasında yetkili vergi mahkemesi, ödeme emrini düzenleyen "
    "dairenin bulunduğu yerdeki vergi mahkemesidir.", zorluk="hard")

P.q("İYUK md. 37",
    f"{K}, vergi uyuşmazlıklarında yetkili mahkemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tarhiyat davasında mükellefin ikametgâhı mahkemesi yetkilidir.",
    ["Tarh ve tahakkuk ettiren dairenin yeri yetkilidir.",
     "Ceza kesen dairenin yeri yetkilidir.",
     "Şikâyet yoluyla düzeltmenin reddinde tarh eden dairenin yeri yetkilidir.",
     "Diğer uyuşmazlıklarda işlemi yapan dairenin yeri yetkilidir."],
    "Md. 37'ye göre vergi uyuşmazlıklarında yetkili mahkeme vergiyi tarh ve tahakkuk ettiren, cezayı kesen dairenin bulunduğu "
    "yerdeki vergi mahkemesidir; mükellefin ikametgâhı esas alınmaz.")

P.q("İYUK md. 38",
    f"{K}, bağlantılı davalara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Biri Danıştayda ise dosya Danıştaya gönderilir.",
    ["Bağlantıya sadece taraf isteğiyle karar verilir.",
     "Bağlantılı davalar birbirinden bağımsız görülür.",
     "Farklı bölgelerdeki dosyalar ilk mahkemede kalır.",
     "Bağlantı kararları istinafa tabidir."],
    "Md. 38'e göre bağlantılı davalardan biri Danıştayda ise dosya Danıştaya, farklı bölge idare mahkemesi yargı çevrelerinde "
    "ise dosyalar Danıştaya, aynı yargı çevresinde ise bölge idare mahkemesine gönderilir; bağlantıya mahkemece doğrudan da "
    "karar verilebilir.")

P.q("İYUK md. 38",
    "Aynı maddi olaydan doğan iki dava, aynı bölge idare mahkemesinin yargı çevresindeki iki ayrı idare mahkemesinde "
    f"görülmektedir.\n\n{K}, bağlantı hâlinde dosyalar nereye gönderilir?",
    "O yer bölge idare mahkemesine",
    ["Danıştaya", "Davacının seçeceği mahkemeye", "Anayasa Mahkemesine", "Uyuşmazlık Mahkemesine"],
    "Md. 38/5'e göre bağlantılı davalar aynı bölge idare mahkemesinin yargı çevresindeki mahkemelerde bulunduğu takdirde "
    "dosyalar o yer bölge idare mahkemesine gönderilir.")

P.q("İYUK md. 42",
    f"{K}, bağlantılı davalarla ilgili diğer esaslara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bağlantı kararlarına karşı temyiz yoluna gidilebilir.",
    ["Bağlantı hakkında karar verilinceye kadar usuli işlemler durur.",
     "Yetkili kılınan mahkeme davalara kaldığı yerden devam eder.",
     "Bölge idare mahkemesinin bağlantı kararları kesindir.",
     "Danıştayın bağlantı kararları kesindir."],
    "Md. 42'ye göre bağlantının bulunup bulunmadığı yolundaki bölge idare mahkemesi ve Danıştay kararları kesindir.")

P.q("İYUK md. 43",
    f"{K}, görev ve yetki uyuşmazlıklarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu kararlar kesindir.",
    ["Kararlara karşı istinaf yoluna gidilebilir.",
     "Uyuşmazlığı Uyuşmazlık Mahkemesi çözer.",
     "Yeniden açılan davada harç iki katı alınır.",
     "Kararlar taraflara tebliğ edilmez."],
    "Md. 43'e göre görev ve yetki uyuşmazlıklarıyla ilgili Danıştay ve bölge idare mahkemesi kararları kesindir; bu kararlarla "
    "görevli ve yetkili kılınan mahkemeye yeniden dava açılırsa harç alınmaz.")

P.q("İYUK md. 43",
    "Bir idare mahkemesi yetkisizlik kararıyla dosyayı başka bir bölgedeki idare mahkemesine göndermiş, o mahkeme de kendini "
    f"yetkisiz görmüştür.\n\n{K}, bu uyuşmazlığı kim çözümler?",
    "Danıştay",
    ["Uyuşmazlık Mahkemesi", "Bölge idare mahkemesi", "Anayasa Mahkemesi",
     "Adalet Bakanlığı"],
    "Md. 43/1-b'ye göre mahkemeler aynı bölge idare mahkemesinin yargı çevresinde ise uyuşmazlık bölge idare mahkemesince, "
    "aksi hâlde Danıştayca çözümlenir.", zorluk="hard")

P.q("İYUK md. 44",
    f"{K}, aşağıdaki hâllerden hangisinde merci tayini istenmez?",
    "Davacının mahkemeyi değiştirmek istemesi",
    ["Yetkili mahkemeye hukuki engel çıkması",
     "Yetkili mahkemeye fiili engel çıkması",
     "Yargı çevresi sınırında tereddüt edilmesi",
     "İki mahkemenin de yetkili olduğuna karar vermesi"],
    "Md. 44'e göre merci tayini; yetkili mahkemeye fiili veya hukuki engel çıkması, yargı çevresi sınırlarında tereddüt veya iki "
    "mahkemenin de yetkili olduğuna karar vermesi hâllerinde istenir.")

P.q("İYUK md. 44",
    f"{K}, merci tayinine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Merci tayini kararlarına karşı istinaf yoluna gidilebilir.",
    ["Aynı yargı çevresinde uyuşmazlığı bölge idare mahkemesi çözer.",
     "Diğer hâllerde dosya Danıştaya gönderilir.",
     "Merci tayini tarafların veya mahkemelerin istemiyle yapılır.",
     "Görevli ve yetkili mahkemeyi karara bağlayan merci belirler."],
    "Md. 44/3'e göre Danıştay ve bölge idare mahkemesinin merci tayini konusunda verdiği kararlar kesindir.")

P.q("İYUK md. 9",
    f"{K}, adli yargıda açılıp görev yönünden reddedilen davanın idari yargıda yeniden açılmasına ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Görevsizlik kararından sonra dava hakkı düşer.",
    ["Karar kesinleşince otuz gün içinde dava açılabilir.",
     "Görevsiz yere başvuru tarihi dava tarihi sayılır.",
     "Dava süresi dolmamışsa o süre içinde de dava açılabilir.",
     "Süre kesinleşmeyi izleyen günden başlar."],
    "Md. 9'a göre görevsizlik kararı kesinleşince otuz gün içinde, idari dava süresi dolmamışsa o süre içinde görevli "
    "mahkemede dava açılabilir; dava hakkı düşmez.")

P.q("İYUK md. 24",
    f"{K}, aşağıdakilerden hangisi idari yargı kararlarında bulunması gereken hususlardan biri değildir?",
    "Tanıkların kimlik bilgileri",
    ["Tarafların ad ve soyadları",
     "Kararın dayandığı hukuki sebepler",
     "Yargılama giderlerinin kime yükletildiği",
     "Kararın oybirliği veya oyçokluğuyla verildiği"],
    "Md. 24'e göre kararlarda taraflar, olaylar ve savunma özeti, hukuki sebepler ve gerekçe, yargılama giderleri, kararın "
    "tarihi ve oybirliği ya da oyçokluğu ile verildiği gibi hususlar yer alır; tanık bilgileri sayılmamıştır.")

P.q("İYUK md. 15",
    "Ehliyetli bir kişi adına avukat olmayan vekili dava açmıştır."
    f"\n\n{K}, ilk incelemede bu durumda hangi karar verilir?",
    "Avukatla açılmak üzere dilekçe reddi",
    ["Davanın esastan reddi",
     "Dilekçenin gerçek hasma tebliği",
     "Dosyanın vekil ataması için baroya gönderilmesi",
     "Davanın açılmamış sayılması"],
    "Md. 15/1-d'ye göre ehliyetli olan şahsın avukat olmayan vekili tarafından dava açılmışsa, otuz gün içinde bizzat veya bir "
    "avukat vasıtasıyla dava açılmak üzere dilekçelerin reddine karar verilir.", zorluk="hard")

P.q("İYUK md. 14",
    f"{K}, Danıştayda dava dilekçelerinin ilk incelemesini kim yapar?",
    "Daire başkanının görevlendireceği tetkik hâkimi",
    ["Danıştay Başsavcısı", "Genel Sekreter", "Evrak Müdürü", "İdari İşler Kurulu Başkanı"],
    "Md. 14/3'e göre dilekçeler Danıştayda daire başkanının görevlendireceği bir tetkik hâkimi, idare ve vergi mahkemelerinde "
    "mahkeme başkanı veya görevlendireceği bir üye tarafından incelenir.")

P.q("İYUK md. 14",
    f"{K}, ilk incelemeden sonra ilk inceleme konularındaki bir eksikliğin tespit edilmesi hâlinde aşağıdakilerden "
    "hangisi doğrudur?",
    "Davanın her safhasında md. 15 uygulanır.",
    ["Eksiklik artık dikkate alınmaz.",
     "Dosya işlemden kaldırılır.",
     "Karar ancak temyizde verilebilir.",
     "Eksiklik esas kararla birlikte değerlendirilmez."],
    "Md. 14/6'ya göre ilk inceleme konularındaki hususların ilk incelemeden sonra tespit edilmesi hâlinde de davanın her "
    "safhasında md. 15 hükmü uygulanır.")

P.q("İYUK md. 36",
    f"{K}, tam yargı davalarında yetkili mahkemeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "İdari sözleşmeden doğanlar md. 36 kapsamı dışındadır.",
    ["Tüm tam yargı davalarında davacının ikametgâhı esastır.",
     "Tam yargı davaları sadece Ankara'da görülür.",
     "Yetkili mahkemeyi davalı idare seçer.",
     "Tam yargı davalarında yetki kuralı yoktur."],
    "Md. 36'daki sıralı yetki kuralı, idari sözleşmelerden doğanlar dışında kalan tam yargı davaları için öngörülmüştür; idari "
    "sözleşmelerde md. 32'ye göre sözleşmeyi yapan merciin bulunduğu yer mahkemesi yetkilidir.", zorluk="hard")

P.q("İYUK md. 26",
    f"{K}, dava sırasında gerçek kişi olan tarafın ölümü hâlinde aşağıdakilerden hangisi doğrudur?",
    "Dosya işlemden kaldırılır.",
    ["Dava doğrudan düşer.",
     "Dava esastan reddedilir.",
     "Dava vasi tarafından sürdürülür.",
     "Dava mirasçılar lehine sonuçlandırılır."],
    "Md. 26/1'e göre dava esnasında tarafın ölümü veya kişilik ve niteliğinde değişiklik olursa, takip hakkı kendisine geçenin "
    "başvurmasına veya idarenin mirasçılar aleyhine takibi yenilemesine kadar dosyanın işlemden kaldırılmasına karar verilir; "
    "sadece öleni ilgilendiren davalara ait dilekçeler iptal edilir.")

P.q("İYUK md. 40",
    f"{K}, bölge idare mahkemesinin bağlantılı davalarla ilgili incelemesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bağlantı yoksa dosyalar geri gönderilir.",
    ["Bağlantı yoksa dosyalar Danıştaya gönderilir.",
     "Bağlantı varsa dosyalar davacıya iade edilir.",
     "Bağlantı dosyaları olağan sırayla incelenir.",
     "Bağlantı kararı ancak duruşmayla verilir."],
    "Md. 40'a göre bölge idare mahkemesi bağlantılı dava dosyalarını öncelikle ve ivedilikle inceler; bağlantı varsa dosyaları "
    "yetkili kıldığı mahkemeye, yoksa ilgili mahkemelere geri gönderir.")

P.q("İYUK md. 34",
    f"{K}, aşağıdaki davalardan hangisinde taşınmazın bulunduğu yer idare mahkemesi yetkili değildir?",
    "Disiplin cezasına karşı dava",
    ["İmar planına karşı dava",
     "Yıkım kararına karşı dava",
     "İskân ruhsatına ilişkin dava",
     "Kamulaştırma işlemine karşı dava"],
    "Md. 34/1'e göre imar, kamulaştırma, yıkım, işgal, tahsis, ruhsat ve iskân gibi taşınmazlarla ilgili davalarda taşınmazın "
    "bulunduğu yer mahkemesi yetkilidir; disiplin cezasına karşı davada md. 33 uygulanır.")

P.q("İYUK md. 33",
    f"{K}, özel kanun hükümleri saklı kalmak kaydıyla hâkim ve savcıların mali ve sosyal haklarına ilişkin davalarda "
    "yetkili mahkeme aşağıdakilerden hangisidir?",
    "Bağlı olunan BİM’e en yakın BİM’in bulunduğu yer mahkemesi",
    ["Hâkim veya savcının görev yaptığı yer idare mahkemesi",
     "Adalet Bakanlığının bulunduğu Ankara idare mahkemesi",
     "Hâkim veya savcının ikametgâhındaki idare mahkemesi",
     "Hâkimler ve Savcılar Kurulunun belirlediği idare mahkemesi"],
    "Md. 33/4'e göre bu davalarda yetkili mahkeme, hâkim veya savcının görev yaptığı yerin bağlı olduğu bölge idare "
    "mahkemesine en yakın bölge idare mahkemesinin bulunduğu yer idare mahkemesidir.", zorluk="hard")

P.q("İYUK md. 20",
    f"{K}, mahkemelerin bilgi ve belge istemesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İdare, istenen belgeyi gerekçesiz olarak vermeyebilir.",
    ["Mahkemeler her türlü incelemeyi resen yapar.",
     "İstenen belgelerin süresinde verilmesi zorunludur.",
     "Haklı sebeple süre bir defa uzatılabilir.",
     "Verilmeyen belgeye dayanan savunmayla karar verilemez."],
    "Md. 20'ye göre istenen bilgi ve belgeleri ilgililerin süresinde vermesi zorunludur; sadece Devletin güvenliği veya yüksek "
    "menfaatleriyle ilgili belgeler gerekçe bildirilerek verilmeyebilir.")

P.q("İYUK md. 31",
    f"{K}, Kanunda hüküm bulunmayan bilirkişi, keşif ve feragat gibi hususlarda aşağıdaki kanunlardan hangisi uygulanır?",
    "Hukuk Muhakemeleri Kanunu",
    ["Ceza Muhakemesi Kanunu", "Kabahatler Kanunu", "İcra ve İflas Kanunu", "Harçlar Kanunu"],
    "Md. 31/1'e göre Kanunda hüküm bulunmayan hâkimin reddi, ehliyet, davaya katılma, feragat ve kabul, bilirkişi, keşif ve "
    "yargılama giderleri gibi hususlarda Hukuk Muhakemeleri Kanunu hükümleri uygulanır.", zorluk="easy")

P.q("İYUK md. 31",
    f"{K}, HMK’ya atıf yapılan hâller saklı kalmak üzere vergi uyuşmazlıklarının çözümünde hangi kanunun ilgili hükümleri "
    "uygulanır?",
    "Vergi Usul Kanunu",
    ["Hukuk Muhakemeleri Kanunu", "Amme Alacakları Kanunu", "Gelir Vergisi Kanunu", "Harçlar Kanunu"],
    "Md. 31/2'ye göre İYUK ve HMK'ya atıf yapılan hâller saklı kalmak üzere vergi uyuşmazlıklarının çözümünde Vergi Usul "
    "Kanununun ilgili hükümleri uygulanır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
