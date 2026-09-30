# -*- coding: utf-8 -*-
"""Hukuk · Borçlar Hukuku · Borcun İfası ve İfa Edilmemesinin Sonuçları — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında TBK soruları "6098 sayılı Türk Borçlar Kanunu’na göre …" kalıbıyla; ifa yeri, ifa
zamanı, temerrüt ve faiz sınırları gibi kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 6098 sayılı TBK md. 83-131. Yıllık değişen yasal faiz oranı
soru konusu yapılmamış; hesaplarda oran kökte varsayım olarak verilmiştir.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_borcun_ifasi_2026.json", lesson="borclar_hukuku", topic="borcun_ifasi",
          konu_adi="Borcun İfası", seed=2026093016, surum="6098 sayılı TBK güncel metni; 29.09.2026 kontrolü")

K = "6098 sayılı Türk Borçlar Kanunu’na göre"

P.sayisal("TBK md. 88",
    "Taraflar bir ödünç sözleşmesinde akdî faiz kararlaştıracaktır. Faiz borcunun doğduğu tarihte mevzuata göre belirlenen "
    f"yıllık faiz oranının %20 olduğu varsayılmaktadır.\n\n{K}, sözleşmeyle kararlaştırılabilecek yıllık faiz oranı en çok "
    "yüzde kaçtır?",
    "30", ["20", "25", "40", "60"],
    "Md. 88'e göre sözleşmeyle kararlaştırılacak yıllık faiz oranı, mevzuata göre belirlenen oranın yüzde elli fazlasını "
    "aşamaz: 20 × 1,5 = %30.", zorluk="hard")

P.q("TBK md. 83",
    f"{K}, borçlunun borcunu şahsen ifa etme yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Alacaklının menfaati yoksa şahsen ifa gerekmez.",
    ["Borçlu her borcu şahsen ifa etmelidir.",
     "Şahsen ifa sadece para borçlarında gerekir.",
     "Borçlu ifayı başkasına bırakamaz.",
     "Şahsen ifa zorunluluğu sadece tacirlere aittir."],
    "Md. 83'e göre borcun bizzat borçlu tarafından ifa edilmesinde alacaklının menfaati bulunmadıkça borçlu borcunu şahsen ifa "
    "etmekle yükümlü değildir.", zorluk="easy")

P.q("TBK md. 84",
    f"{K}, kısmen ifaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Belli ve muaccelse reddedebilir.",
    ["Alacaklı kısmen ifayı reddedemez.",
     "Kısmen ifa borcu sona erdirir.",
     "Kısmen ifa sadece mahkeme izniyle yapılır.",
     "Borçlu ikrar ettiği kısmı ifadan kaçınabilir."],
    "Md. 84'e göre borcun tamamı belli ve muaccel ise alacaklı kısmen ifayı reddedebilir; kabul ederse borçlu ikrar ettiği kısmı "
    "ifadan kaçınamaz.")

P.sayisal("TBK md. 120",
    "Faiz borcunun doğduğu tarihte mevzuata göre belirlenen yıllık faiz oranının %20 olduğu varsayılmaktadır."
    f"\n\n{K}, sözleşmeyle kararlaştırılabilecek yıllık temerrüt faizi oranı en çok yüzde kaçtır?",
    "40", ["20", "25", "30", "60"],
    "Md. 120'ye göre sözleşmeyle kararlaştırılacak yıllık temerrüt faizi oranı, mevzuata göre belirlenen oranın yüzde yüz "
    "fazlasını aşamaz: 20 × 2 = %40.", zorluk="hard")

P.q("TBK md. 85",
    f"{K}, bölünemeyen borcun birden çok borçlusu varsa aşağıdakilerden hangisi doğrudur?",
    "Her borçlu borcun tamamını ifa eder.",
    ["Her borçlu sadece kendi payını öder.",
     "Borç doğrudan bölünür.",
     "Sadece ilk borçlu sorumludur.",
     "İfa eden diğer borçlulara rücu edemez."],
    "Md. 85'e göre bölünemeyen borcun birden çok borçlusu varsa her biri borcun tamamını ifa etmekle yükümlüdür; ifa eden "
    "alacaklıya halef olur ve diğerlerinden payları oranında isteyebilir.")

P.q("TBK md. 86",
    f"{K}, çeşit borçlarında edimin seçimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ortalamanın altında edim seçilebilir.",
    ["Kural olarak seçim borçluya aittir.",
     "Hukuki ilişkiden aksi anlaşılabilir.",
     "İşin özelliğinden aksi anlaşılabilir.",
     "Seçilen edim ortalama nitelikte olmalıdır."],
    "Md. 86'ya göre çeşit borçlarında seçim kural olarak borçluya aittir; ancak borçlunun seçeceği edim ortalama nitelikten daha "
    "düşük olamaz.")

P.sayisal("TBK md. 91",
    f"{K}, borcun ifası için “mayıs ayının ortası” belirlenmişse, borç mayıs ayının kaçıncı günü ifa edilir?",
    "15", ["10", "14", "16", "20"],
    "Md. 91'e göre ayın ortası belirlenmişse bundan ayın on beşinci günü anlaşılır; ayın başı veya sonu belirlenmişse ayın ilk "
    "veya son günü anlaşılır.", zorluk="easy")

P.q("TBK md. 87",
    f"{K}, seçimlik borçlarda edimlerden birinin seçim hakkı kural olarak kime aittir?",
    "Borçluya",
    ["Alacaklıya", "Hâkime", "Üçüncü kişiye", "Taraflara birlikte"],
    "Md. 87'ye göre seçimlik borçlarda, hukuki ilişkiden ve işin özelliğinden aksi anlaşılmadıkça edimlerden birinin seçimi "
    "borçluya aittir.", zorluk="easy")

P.q("TBK md. 88",
    f"{K}, faiz oranı sözleşmede kararlaştırılmamışsa uygulanacak oran nasıl belirlenir?",
    "Doğduğu tarihteki mevzuata göre",
    ["Alacaklının talep ettiği orana göre",
     "Ödeme günündeki banka oranına göre",
     "Hâkimin hakkaniyet takdirine göre",
     "Ticaret odasının açıkladığı orana göre"],
    "Md. 88'e göre faiz oranı sözleşmede kararlaştırılmamışsa faiz borcunun doğduğu tarihte yürürlükte olan mevzuat hükümlerine "
    "göre belirlenir.")

P.sayisal("TBK md. 92",
    "Sözleşme 3 Mart’ta kurulmuş ve borcun sözleşmenin kurulmasından başlayarak 15 gün içinde ifası kararlaştırılmıştır."
    f"\n\n{K}, süre mart ayının kaçıncı günü dolar?",
    "18", ["15", "17", "19", "20"],
    "Md. 92'ye göre gün olarak belirlenen süre sözleşmenin kurulduğu gün sayılmaksızın son günün dolmasıyla biter; on beş gün "
    "iki hafta değil tam on beş gündür: 3 + 15 = 18 Mart.", zorluk="hard")

P.q("TBK md. 89",
    f"{K}, aksine anlaşma yoksa para borçlarının ifa yeri aşağıdakilerden hangisidir?",
    "Alacaklının yerleşim yeri",
    ["Borçlunun yerleşim yeri",
     "Sözleşmenin kurulduğu yer",
     "Borç konusunun bulunduğu yer",
     "Borçlunun seçeceği bir banka şubesi"],
    "Md. 89'a göre para borçları alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir.", zorluk="easy")

P.q("TBK md. 89",
    f"{K}, aksine anlaşma yoksa ifa yerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Parça borçları alacaklının yerleşim yerinde ifa edilir.",
    ["Para borçları alacaklının yerleşim yerinde ifa edilir.",
     "Diğer borçlar borçlunun yerleşim yerinde ifa edilir.",
     "İfa yeri tarafların örtülü iradesine göre de belirlenir.",
     "Alacaklı yer değiştirirse önceki yerde ifa mümkündür."],
    "Md. 89'a göre parça borçları sözleşmenin kurulduğu sırada borç konusunun bulunduğu yerde ifa edilir.")

P.q("TBK md. 89",
    "İstanbul’da oturan (A), Bursa’daki deposunda bulunan belirli bir tabloyu İzmir’de oturan (B)’ye satmıştır; ifa yeri "
    f"kararlaştırılmamıştır.\n\n{K}, tablonun teslim borcu nerede ifa edilir?",
    "Bursa’da",
    ["İstanbul’da", "İzmir’de", "Ankara’da", "(B)’nin seçeceği yerde"],
    "Md. 89'a göre parça borçları sözleşmenin kurulduğu sırada borç konusunun bulunduğu yerde ifa edilir; tablo Bursa'daki "
    "depodadır.", zorluk="hard")

P.q("TBK md. 90",
    f"{K}, ifa zamanı kararlaştırılmamış ve hukuki ilişkinin özelliğinden de anlaşılamayan borç ne zaman muaccel olur?",
    "Doğumu anında",
    ["Bir ay sonra",
     "Alacaklının ihtarından bir hafta sonra",
     "Takvim yılı sonunda",
     "Borçlunun uygun göreceği zamanda"],
    "Md. 90'a göre ifa zamanı kararlaştırılmadıkça veya hukuki ilişkinin özelliğinden anlaşılmadıkça her borç doğumu anında "
    "muaccel olur.", zorluk="easy")

P.q("TBK md. 91",
    f"{K}, borcun ifası için gün belirtilmeksizin sadece ay belirlenmişse ifa günü aşağıdakilerden hangisidir?",
    "O ayın son günü",
    ["O ayın ilk günü", "O ayın on beşinci günü", "Takip eden ayın ilk günü", "Alacaklının belirleyeceği gün"],
    "Md. 91'e göre borcun ifası için gün belirtilmeksizin sadece ay belirlenmişse bundan o ayın son günü anlaşılır.")

P.q("TBK md. 92",
    f"{K}, sekiz gün olarak belirlenmiş sürenin anlamına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tam sekiz günü ifade eder.",
    ["Bir haftayı ifade eder.",
     "Yedi iş gününü ifade eder.",
     "İki haftayı ifade eder.",
     "Takip eden ayın sekizinci gününü ifade eder."],
    "Md. 92'ye göre sekiz veya on beş gün olarak belirlenmiş süre bir veya iki haftayı değil, tam sekiz veya on beş günü ifade "
    "eder.")

P.q("TBK md. 93",
    f"{K}, ifa zamanının veya sürenin son gününün resmî tatile rastlaması hâlinde aşağıdakilerden hangisi doğrudur?",
    "Tatili izleyen ilk iş gününe geçer.",
    ["Tatilden önceki iş gününe çekilir.",
     "Tatil günü ifa zorunludur.",
     "Borç düşer.",
     "Süre bir hafta uzar ve aksine anlaşma yapılamaz."],
    "Md. 93'e göre ifa zamanı veya sürenin son günü tatile rastlarsa bu günü izleyen tatil olmayan ilk güne geçer; aksine anlaşma "
    "geçerlidir.")

P.q("TBK md. 95",
    f"{K}, süre uzatılmışsa yeni süre ne zaman başlar?",
    "Bitimi izleyen ilk gün",
    ["Uzatma kararının verildiği gün",
     "Önceki sürenin başladığı gün",
     "Alacaklının onay verdiği gün",
     "Takip eden ayın ilk iş günü"],
    "Md. 95'e göre süre uzatılmışsa yeni süre, aksi kararlaştırılmadıkça önceki sürenin sona ermesini izleyen birinci günden "
    "başlar.")

P.q("TBK md. 96",
    f"{K}, erken ifaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Erken ifada kural olarak indirim yapılabilir.",
    ["Aksi anlaşılmadıkça borçlu erken ifa edebilir.",
     "Kanun gereği indirim mümkün olabilir.",
     "Sözleşmeyle indirim kararlaştırılabilir.",
     "Âdet gereği indirim mümkün olabilir."],
    "Md. 96'ya göre kanun, sözleşme veya âdet gereği olmadıkça borçlu erken ifada bulunması sebebiyle indirim yapamaz.")

P.q("TBK md. 97",
    f"{K}, karşılıklı borç yükleyen sözleşmede ifa isteyen tarafa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kendi borcunu ifa etmiş veya önermiş olmalıdır.",
    ["Kendi borcunu ifa etmesi gerekmez.",
     "Önce mahkemeye başvurup ifa kararı almalıdır.",
     "Sadece noter ihtarı yeterlidir.",
     "Karşı tarafın kusurunu ispat etmelidir."],
    "Md. 97'ye göre karşılıklı borç yükleyen sözleşmede ifa isteyen taraf, daha sonra ifa hakkı olmadıkça kendi borcunu ifa etmiş "
    "ya da ifasını önermiş olmalıdır.")

P.q("TBK md. 98",
    "Karşılıklı borç yükleyen bir sözleşmede (B) hakkındaki haciz işlemi sonuçsuz kalmış ve (A)’nın hakkı tehlikeye "
    f"düşmüştür.\n\n{K}, (A) aşağıdakilerden hangisini yapabilir?",
    "Güvence verilinceye kadar ifadan kaçınabilir.",
    ["Sözleşmeyi derhal ve güvence istemeden feshedebilir.",
     "(B)’yi cezalandırabilir.",
     "Kendi edimini iki katına çıkarabilir.",
     "Sözleşmeyi sadece (B)’nin rızasıyla sona erdirebilir."],
    "Md. 98'e göre taraflardan biri ifada güçsüzlüğe düşer ve diğerinin hakkı tehlikeye girerse bu taraf karşı edim güvence "
    "altına alınıncaya kadar ifadan kaçınabilir; uygun sürede güvence verilmezse sözleşmeden dönebilir.", zorluk="hard")

P.q("TBK md. 99",
    "Borç ABD doları olarak kararlaştırılmış, sözleşmede aynen ödeme kaydı bulunmamaktadır; borçlu vadede ödeme yapmamıştır."
    f"\n\n{K}, alacaklı aşağıdakilerden hangisini isteyebilir?",
    "Aynen veya vade ya da ödeme günü rayiciyle TL",
    ["Sadece vade günü rayiciyle TL",
     "Sadece döviz olarak aynen ödeme",
     "Sözleşme tarihindeki rayiçle TL",
     "Döviz tutarının iki katı TL"],
    "Md. 99'a göre yabancı para borcu ödeme gününde ödenmezse alacaklı, alacağın aynen veya vade ya da fiilî ödeme günündeki "
    "rayiç üzerinden Türk parasıyla ödenmesini isteyebilir.", zorluk="hard")

P.q("TBK md. 100",
    f"{K}, kısmi ödemelerin mahsubuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ana borca mahsup hakkı sözleşmeyle kaldırılabilir.",
    ["Faiz ve giderde gecikmeyen borçlu ana borca mahsup edebilir.",
     "Güvenceli kısma mahsup hakkı borçluya ait değildir.",
     "Borçlu birden çok borçtan hangisini ödediğini bildirebilir.",
     "Bildirim yoksa makbuzdaki borç ödenmiş sayılır."],
    "Md. 100'e göre faiz veya giderleri ödemede gecikmemiş borçlu kısmi ödemeyi ana borçtan düşme hakkına sahiptir; aksine "
    "anlaşma yapılamaz.", zorluk="hard")

P.q("TBK md. 102",
    f"{K}, geçerli açıklama yapılmamışsa ve birden çok borç muaccelse ödeme hangi borç için yapılmış sayılır?",
    "Borçluya karşı ilk takip edilen borç",
    ["En yüksek tutarlı borç",
     "En son doğan borç",
     "Güvencesi en iyi olan borç",
     "Alacaklının sonradan seçeceği borç"],
    "Md. 102'ye göre birden çok borç muaccelse ödeme borçluya karşı ilk olarak takip edilen borç için; takip yoksa vadesi ilk "
    "gelen borç için yapılmış sayılır.", zorluk="hard")

P.q("TBK md. 102",
    f"{K}, borçlardan hiçbirinin vadesi gelmemişse yapılan ödeme hangi borç için yapılmış sayılır?",
    "Güvencesi en az olan borç",
    ["Güvencesi en fazla olan borç",
     "Tutarı en yüksek borç",
     "İlk doğan borç",
     "Faizi en yüksek olan borç"],
    "Md. 102'ye göre borçlardan hiçbirinin vadesi gelmemişse ödeme güvencesi en az olan borç için yapılmış sayılır.")

P.q("TBK md. 104",
    f"{K}, makbuzların hükümlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Borç senedinin geri verilmesi borcun sürdüğünü gösterir.",
    ["Çekincesiz dönemsel makbuz önceki dönemleri de kapsar.",
     "Anapara makbuzu faizlerin de alındığını gösterir.",
     "Borç senedi geri verilmişse borç sona ermiş sayılır.",
     "Kira bedeli için çekincesiz makbuz önceki kiraları kapsar."],
    "Md. 104'e göre borç senedi borçluya geri verilmişse borç sona ermiş sayılır.")

P.q("TBK md. 106",
    f"{K}, alacaklının temerrüdünün koşullarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Edimi haklı sebep olmadan kabulden kaçınmak",
    ["Alacaklının borçluya ihtar çekmesi",
     "Borçlunun edimi önermemesi",
     "Alacaklının ifa gününü unutması, haklı sebeple",
     "Edimin kısmen ifa edilmesi"],
    "Md. 106'ya göre gereği gibi önerilen edimi haklı sebep olmaksızın kabulden veya gerekli hazırlık fiillerini yapmaktan kaçınan "
    "alacaklı temerrüde düşer.")

P.q("TBK md. 107",
    f"{K}, alacaklının temerrüdünde bir şeyin teslimine ilişkin borçlarda borçlunun hakkı aşağıdakilerden hangisidir?",
    "Şeyi tevdi ederek borçtan kurtulmak",
    ["Şeyi kendisi için kullanmak",
     "Şeyi imha etmek",
     "Alacaklıya ceza kesmek",
     "Borcu iki katına çıkarıp sonra ifa etmek"],
    "Md. 107'ye göre alacaklının temerrüdünde borçlu, hasar ve giderleri alacaklıya ait olmak üzere teslim edeceği şeyi tevdi "
    "ederek borcundan kurtulabilir.")

P.q("TBK md. 107",
    f"{K}, alacaklının temerrüdünde tevdi yerine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ticari mallar hâkim kararı olmadan ardiyeye tevdi edilebilir.",
    ["Tevdi yerini alacaklı belirler.",
     "Tevdi sadece notere ve alacaklının onayıyla yapılabilir.",
     "Ticari mallar tevdi edilemez.",
     "Tevdi yeri borçlunun evidir."],
    "Md. 107'ye göre tevdi yerini ifa yerindeki hâkim belirler; ticari mallar hâkim kararı olmadan da bir ardiyeye tevdi "
    "edilebilir.", zorluk="hard")

P.q("TBK md. 108",
    f"{K}, alacaklının temerrüdünde bozulabilecek şeyin satılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hâkim izni olmadan sattırabilir.",
    ["Satış için kural olarak önceden ihtar gerekir.",
     "Bedel tevdi edilir.",
     "Borsada kayıtlı malda açık artırma zorunlu değildir.",
     "Piyasa fiyatı olan malda ihtar aranmayabilir."],
    "Md. 108'e göre borçlu, alacaklıya önceden ihtarda bulunması koşuluyla hâkimin izniyle şeyi açık artırmayla sattırıp "
    "bedelini tevdi edebilir.")

P.q("TBK md. 109",
    f"{K}, borçlunun tevdi edilen şeyi geri almasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Alacaklı kabul etmemişse geri alabilir.",
    ["Tevdiden sonra geri alamaz.",
     "Geri alınca alacak sona erer.",
     "Geri almak için hâkim izni şarttır.",
     "Rehin kaldırılmış olsa da geri alabilir."],
    "Md. 109'a göre alacaklı kabulünü açıklamamış veya tevdi bir rehni kaldırmamışsa borçlu tevdi edilen şeyi geri alabilir; bu "
    "durumda alacak bütün yan haklarıyla varlığını sürdürür.")

P.q("TBK md. 110",
    f"{K}, borcun konusu bir şeyin teslimini gerektirmiyorsa alacaklının temerrüdü hâlinde borçlunun hakkı "
    "aşağıdakilerden hangisidir?",
    "Borçlu temerrüdü hükümlerine göre dönmek",
    ["Edimi tevdi etmek",
     "Alacaklıyı hapsettirmek",
     "Borcu doğrudan düşürmek",
     "Edimi başkasına devretmek"],
    "Md. 110'a göre borcun konusu bir şeyin teslimini gerektirmiyorsa alacaklının temerrüdünde borçlu, borçlunun temerrüdüne "
    "ilişkin hükümlere göre sözleşmeden dönebilir.", zorluk="hard")

P.q("TBK md. 112",
    f"{K}, borcun hiç veya gereği gibi ifa edilmemesinde borçlunun sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kusursuzluğunu ispat etmedikçe zararı giderir.",
    ["Alacaklı kusuru ispat etmedikçe sorumlu olmaz.",
     "Sadece kastından sorumludur.",
     "Sadece ağır kusurundan sorumludur.",
     "Kural olarak sorumlu olmaz."],
    "Md. 112'ye göre borç hiç veya gereği gibi ifa edilmezse borçlu kendisine hiçbir kusur yüklenemeyeceğini ispat etmedikçe "
    "alacaklının zararını gidermekle yükümlüdür.")

P.q("TBK md. 113",
    f"{K}, yapma borcu ifa edilmediğinde alacaklının hakkı aşağıdakilerden hangisidir?",
    "Başkasınca ifaya izin istemek",
    ["Borçluyu hapsettirmek",
     "Borcu doğrudan düşürmek",
     "Borçlunun mallarına doğrudan el koymak",
     "Sadece manevi tazminat istemek"],
    "Md. 113'e göre yapma borcu ifa edilmezse alacaklı masrafı borçluya ait olmak üzere edimin kendisi veya başkası tarafından "
    "ifasına izin verilmesini isteyebilir; giderim hakkı saklıdır.")

P.q("TBK md. 114",
    f"{K}, borçlunun sorumluluğunun kapsamına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Borçlu sadece ağır kusurundan sorumludur.",
    ["Borçlu genel olarak her türlü kusurdan sorumludur.",
     "Kapsam işin özel niteliğine göre belirlenir.",
     "Borçluya yarar sağlamayan işte sorumluluk hafifler.",
     "Haksız fiil hükümleri kıyasen uygulanır."],
    "Md. 114'e göre borçlu genel olarak her türlü kusurdan sorumludur; iş borçluya yarar sağlamıyorsa sorumluluk daha hafif "
    "değerlendirilir.")

P.q("TBK md. 115",
    f"{K}, aşağıdaki sorumsuzluk anlaşmalarından hangisi kesin hükümsüz değildir?",
    "Hafif kusurdan sorumsuzluk (izin gerektirmeyen iş)",
    ["Ağır kusurdan önceden sorumsuzluk",
     "Hizmet sözleşmesinden doğan borçta sorumsuzluk",
     "İzinli uzmanlık mesleğinde hafif kusurdan sorumsuzluk",
     "İşçiye karşı önceden her türlü sorumsuzluk"],
    "Md. 115'e göre ağır kusurdan, hizmet sözleşmesinden doğan borçlardan ve izinle yürütülen uzmanlık mesleklerinde hafif "
    "kusurdan önceden sorumsuzluk anlaşmaları kesin hükümsüzdür; diğer işlerde hafif kusurdan sorumsuzluk geçerli olabilir.",
    zorluk="hard")

P.q("TBK md. 116",
    f"{K}, yardımcı kişilerin fiillerinden sorumluluğa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sorumluluk kural olarak önceden kaldırılabilir.",
    ["Sorumluluk kaldırılamaz.",
     "Borçlu yardımcıların fiilinden sorumlu değildir.",
     "Sorumluluk sadece yazılı talimatla doğar.",
     "İzinli uzmanlık mesleğinde de kaldırılabilir."],
    "Md. 116'ya göre yardımcı kişilerin fiilinden doğan sorumluluk önceden yapılan anlaşmayla kaldırılabilir; ancak izinle "
    "yürütülen uzmanlık gerektiren işlerde bu anlaşma kesin hükümsüzdür.", zorluk="hard")

P.q("TBK md. 117",
    f"{K}, aşağıdaki hâllerin hangisinde borçlunun temerrüdü için ihtar gerekir?",
    "Vadesi belirlenmemiş muaccel borç",
    ["Birlikte belirlenen ifa gününün geçmesi",
     "Haksız fiilden doğan borç",
     "Kötüniyetli sebepsiz zenginleşme borcu",
     "Bildirimle belirlenen ifa gününün geçmesi"],
    "Md. 117'ye göre muaccel borcun borçlusu alacaklının ihtarıyla temerrüde düşer; belirlenen günün geçmesi, haksız fiil ve "
    "kötüniyetli sebepsiz zenginleşmede ihtar aranmaz.", zorluk="hard")

P.q("TBK md. 117",
    f"{K}, haksız fiilden doğan tazminat borcunda borçlu ne zaman temerrüde düşer?",
    "Fiilin işlendiği tarihte",
    ["İhtar tarihinde",
     "Dava tarihinde",
     "Kararın kesinleştiği tarihte",
     "İcra takibinin başladığı tarihte"],
    "Md. 117'ye göre haksız fiilde fiilin işlendiği tarihte borçlu temerrüde düşmüş olur.")

P.q("TBK md. 118",
    f"{K}, temerrüde düşen borçlunun gecikme tazminatı sorumluluğundan kurtulması için neyi ispat etmesi gerekir?",
    "Temerrüde düşmekte kusuru olmadığını",
    ["Alacaklının zarara uğramadığını",
     "Borcun küçük tutarlı olduğunu",
     "Ekonomik zorluk içinde olduğunu",
     "Alacaklının ihtar çekmediğini ve süre vermediğini"],
    "Md. 118'e göre temerrüde düşen borçlu, temerrüde düşmekte kusuru olmadığını ispat etmedikçe geç ifadan doğan zararı "
    "gidermekle yükümlüdür.")

P.q("TBK md. 119",
    f"{K}, temerrüde düşen borçlunun beklenmedik hâlden sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Beklenmedik hâlden sorumlu değildir.",
    ["Kural olarak beklenmedik hâlden sorumludur.",
     "Temerrütte kusursuzluğunu ispatla kurtulabilir.",
     "Zamanında ifada da zararın doğacağını ispatla kurtulabilir.",
     "Sorumluluk temerrütle birlikte başlar."],
    "Md. 119'a göre temerrüde düşen borçlu beklenmedik hâl sebebiyle doğacak zarardan sorumludur; kusursuzluğunu veya zamanında "
    "ifada da zararın doğacağını ispat ederek kurtulabilir.")

P.q("TBK md. 120",
    f"{K}, akdî faiz kararlaştırılıp temerrüt faizi kararlaştırılmamışsa ve akdî faiz yasal orandan yüksekse temerrüt faizi "
    "oranı hakkında aşağıdakilerden hangisi doğrudur?",
    "Akdî faiz oranı geçerli olur.",
    ["Yasal faiz oranı geçerli olur.",
     "Temerrüt faizi istenemez.",
     "Hâkim hakkaniyete göre belirler.",
     "Akdî faizin yarısı uygulanır."],
    "Md. 120'ye göre akdî faiz kararlaştırılmakla birlikte temerrüt faizi kararlaştırılmamışsa ve akdî faiz yasal orandan fazla "
    "ise temerrüt faizi hakkında akdî faiz oranı geçerli olur.", zorluk="hard")

P.q("TBK md. 121",
    f"{K}, faiz borcunu ödemekte temerrüde düşen borçlu temerrüt faizini ne zamandan itibaren öder?",
    "İcra takibi veya dava tarihinden",
    ["İhtar tarihinden",
     "Faiz borcunun doğduğu tarihten",
     "Anapara vadesinden",
     "Kararın kesinleştiği tarihten"],
    "Md. 121'e göre faiz veya irat borcunu ya da bağışladığı parayı ödemekte temerrüde düşen borçlu icra takibine girişildiği veya "
    "dava açıldığı günden itibaren temerrüt faizi öder; temerrüt faizine ayrıca temerrüt faizi yürütülemez.", zorluk="hard")

P.q("TBK md. 122",
    f"{K}, temerrüt faizini aşan zarara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Borçlu kusursuzluğunu ispatlamadıkça öder.",
    ["Aşkın zarar istenemez.",
     "Alacaklı borçlunun kastını ispatlamalıdır.",
     "Aşkın zarar ayrı davada istenir.",
     "Aşkın zarar faizin yarısıyla sınırlıdır."],
    "Md. 122'ye göre temerrüt faizini aşan zararı borçlu, hiçbir kusuru bulunmadığını ispat etmedikçe gidermekle yükümlüdür; "
    "miktar görülen davada belirlenebiliyorsa hâkim ona da hükmeder.")

P.q("TBK md. 124",
    f"{K}, karşılıklı borç yükleyen sözleşmelerde temerrüt hâlinde süre verilmesine gerek olmayan durumlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Borcun küçük tutarlı olması",
    ["Süre vermenin etkisiz olacağının anlaşılması",
     "İfanın alacaklı için yararsız kalması",
     "Kesin vadeli işin gecikmesi",
     "Borçlunun tutumundan sürenin etkisiz olacağı"],
    "Md. 124'e göre borçlunun durumundan süre vermenin etkisiz olacağı anlaşılıyorsa, ifa alacaklı için yararsız kalmışsa veya "
    "kesin vadeli işte ifa artık kabul edilmeyecekse süre verilmesine gerek yoktur.")

P.q("TBK md. 125",
    f"{K}, temerrüde düşen borçluya verilen süre içinde de ifa gerçekleşmezse alacaklının seçimlik hakları arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Borçluyu doğrudan hapsettirme",
    ["İfa ve gecikme tazminatı istemek",
     "İfadan vazgeçip müspet zarar istemek",
     "Sözleşmeden dönmek",
     "Dönmede menfi zarar istemek"],
    "Md. 125'e göre alacaklı ifa ve gecikme tazminatı isteyebilir veya ifadan vazgeçtiğini bildirerek ifa edilmemeden doğan "
    "zararın giderilmesini isteyebilir ya da sözleşmeden dönebilir.", zorluk="easy")

P.q("TBK md. 126",
    f"{K}, ifasına başlanmış sürekli edimli sözleşmelerde borçlunun temerrüdü hâlinde alacaklı aşağıdakilerden hangisini "
    "yapabilir?",
    "Sözleşmeyi feshedip erken sona erme zararını isteyebilir.",
    ["Sadece geçmişe etkili dönebilir.",
     "Sadece bekleyebilir.",
     "Sadece manevi tazminat isteyebilir.",
     "Borçluyu temerrütten kurtarabilir."],
    "Md. 126'ya göre ifasına başlanmış sürekli edimli sözleşmelerde alacaklı ifa ve gecikme tazminatı isteyebileceği gibi "
    "sözleşmeyi feshederek süresinden önce sona ermesinden doğan zararın giderilmesini de isteyebilir.", zorluk="hard")

P.q("TBK md. 127",
    f"{K}, alacaklıya ifada bulunan üçüncü kişinin alacaklıya halef olduğu hâller arasında aşağıdakilerden hangisi yer "
    "alır?",
    "Rehinden kurtaran ayni hak sahibi",
    ["Borçlunun rızası olmadan ödeme yapan herkes",
     "Borçlunun akrabası olan herkes",
     "Borcu bağış kastıyla ödeyen kişi",
     "Borçluyla aynı işyerinde çalışan kişi"],
    "Md. 127'ye göre başkasının borcu için rehnedilen şeyi rehinden kurtaran ve üzerinde mülkiyet veya ayni hakkı bulunan kişi "
    "ile borçlunun ifadan önce halefiyeti alacaklıya bildirdiği kişi alacaklıya halef olur.", zorluk="hard")

P.q("TBK md. 128",
    f"{K}, üçüncü kişinin fiilini başkasına karşı üstlenen kişinin sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Doğan zararı giderir.",
    ["Sadece üçüncü kişi sorumludur.",
     "Üstlenen sorumlu olmaz.",
     "Üstlenme sadece noterde yapılabilir.",
     "Sorumluluk üçüncü kişinin kusuruna bağlıdır."],
    "Md. 128'e göre üçüncü bir kişinin fiilini başkasına karşı üstlenen, bu fiilin gerçekleşmemesinden doğan zararı gidermekle "
    "yükümlüdür.")

P.q("TBK md. 129",
    "Üçüncü kişi yararına sözleşmede üçüncü kişi (C), hakkını kullanmak istediğini borçluya bildirmiştir."
    f"\n\n{K}, bu bildirimden sonra alacaklının yetkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Borçluyu ibra edemez.",
    ["Borçluyu dilediği gibi ibra edebilir.",
     "Borcun kapsamını tek başına değiştirebilir.",
     "Edimi kendisine ifa ettirmelidir.",
     "Sözleşmeyi (C)’ye bildirmeden feshedebilir."],
    "Md. 129'a göre üçüncü kişi hakkını kullanmak istediğini borçluya bildirdikten sonra alacaklı borçluyu ibra edemez ve borcun "
    "nitelik ve kapsamını değiştiremez.", zorluk="hard")

P.q("TBK md. 130",
    f"{K}, işverenin çalışana karşı sorumluluğu için yaptırdığı sigortadan doğan haklar kime aittir?",
    "Doğrudan çalışana",
    ["İşverene", "Sigorta şirketine", "Sosyal Güvenlik Kurumuna", "İşverenin alacaklılarına"],
    "Md. 130'a göre başkasını çalıştıran kişi çalıştırdığına karşı sorumluluğunu güvence altına almak üzere sigorta yaptırmışsa "
    "sigortadan doğan haklar doğrudan çalışana ait olur; ödenen tazminat genel hükümlere göre ödenecek tazminattan indirilir.")

P.q("TBK md. 131",
    f"{K}, asıl borcun sona ermesinin buna bağlı hak ve borçlara etkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Rehin ve kefalet de sona erer.",
    ["Kefalet varlığını sürdürür.",
     "Rehin hakkı devam eder.",
     "Ceza koşulu istenebilir.",
     "İşlemiş faiz istenemez."],
    "Md. 131'e göre asıl borç sona erince rehin, kefalet, faiz ve ceza koşulu gibi bağlı hak ve borçlar da sona erer; işlemiş faiz "
    "ve ceza koşulu saklı tutulmuşsa istenebilir.")

P.oncul("TBK md. 89",
    f"{K} aksine anlaşma yoksa aşağıdaki ifa yeri kuralları değerlendirilmektedir:",
    ["Para borcu alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir.",
     "Parça borcu borçlunun yerleşim yerinde ifa edilir.",
     "Çeşit borcu doğumu sırasında borçlunun yerleşim yerinde ifa edilir.",
     "Para borcu borçlunun yerleşim yerinde ifa edilir."],
    "Yukarıdakilerden hangileri doğrudur?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 89'a göre para borçları alacaklının ödeme zamanındaki yerleşim yerinde (I), parça borçları borç konusunun bulunduğu "
    "yerde, diğer borçlar doğumları sırasında borçlunun yerleşim yerinde (III) ifa edilir.", zorluk="hard")

P.q("TBK md. 93",
    f"{K}, ifa zamanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tatile rastlayan son gün için aksine anlaşma yapılamaz.",
    ["Borç alışılmış iş saatlerinde ifa edilir.",
     "Ay belirlenmişse ayın son günü anlaşılır.",
     "Ayın başı ilk gün olarak anlaşılır.",
     "Süre uzatılırsa yeni süre ertesi gün başlar."],
    "Md. 93'e göre ifa zamanı veya sürenin son günü tatile rastlarsa izleyen ilk iş gününe geçer; ancak aksine anlaşma "
    "geçerlidir.", zorluk="hard")

P.q("TBK md. 94",
    f"{K}, borç hangi saatlerde ifa ve kabul edilir?",
    "Alışılmış iş saatlerinde",
    ["Günün herhangi bir saatinde",
     "Sadece sabah saatlerinde",
     "Alacaklının belirleyeceği saatte",
     "Noterin mesai saatlerinde"],
    "Md. 94'e göre borç alışılmış iş saatlerinde ifa ve kabul edilir.", zorluk="easy")

P.q("TBK md. 103",
    f"{K}, ödeme yapan borçlunun makbuz ve senede ilişkin haklarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kısmi ödemede senedin iadesi istenebilir.",
    ["Ödeyen borçlu makbuz isteyebilir.",
     "Tam ödemede senedin iadesi istenebilir.",
     "Tam ödemede senedin iptali istenebilir.",
     "Kısmi ödeme senede işletilebilir."],
    "Md. 103'e göre borcun tamamı ödenmemişse borçlu ancak makbuz verilmesini ve ödemenin borç senedine işlenmesini isteyebilir; "
    "senedin iadesi tam ödemede istenir.")

P.q("TBK md. 105",
    f"{K}, alacaklının borç senedini kaybettiğini iddia etmesi hâlinde ödeme yapan borçlu ne isteyebilir?",
    "Senedin iptalini gösteren onaylı belge",
    ["Borcun yarısını ödeyerek kurtulmayı",
     "Senedin bulunmasını beklemek için süre",
     "Ödemeyi mahkeme veznesine yatırıp faiz almayı",
     "Alacaklıdan teminat olarak ayrıca senet"],
    "Md. 105'e göre alacaklı senedi kaybettiğini iddia ederse borçlunun istemi üzerine, senedin iptalini ve borcun sona erdiğini "
    "gösteren resmen düzenlenmiş veya onaylanmış bir belge vermek zorundadır.")

P.q("TBK md. 106",
    f"{K}, alacaklının müteselsil borçlulardan birine karşı temerrüde düşmesi hâlinde aşağıdakilerden hangisi doğrudur?",
    "Diğerlerine karşı da temerrüde düşer.",
    ["Sadece o borçluya karşı temerrüde düşer.",
     "Temerrüt oluşmaz.",
     "Diğer borçlular borçtan kurtulur.",
     "Temerrüt borçluların sayısına bölünür."],
    "Md. 106'ya göre alacaklı müteselsil borçlulardan birine karşı temerrüde düşerse diğerlerine karşı da temerrüde düşmüş olur.")

P.q("TBK md. 111",
    "Borçlu, kusuru olmaksızın alacağın kime ait olduğu konusunda duraksama yaşadığından borcunu ifa edememektedir."
    f"\n\n{K}, borçlu bu durumda ne yapabilir?",
    "Tevdi veya sözleşmeden dönme",
    ["Borcu doğrudan düşürmek",
     "Alacaklıyı seçip ona ödemek",
     "İfayı süresiz ertelemek",
     "Borcu devlete bağışlamak"],
    "Md. 111'e göre alacağın kime ait olduğunda veya alacaklının kimliğinde duraksama gibi sebeplerle ifa edilemezse borçlu, "
    "alacaklının temerrüdünde olduğu gibi tevdi veya sözleşmeden dönme hakkını kullanabilir.", zorluk="hard")

P.q("TBK md. 123",
    f"{K}, karşılıklı borç yükleyen sözleşmelerde taraflardan biri temerrüde düşerse diğer taraf kural olarak ne yapabilir?",
    "Uygun bir süre verebilir.",
    ["Borçluyu hapsettirebilir.",
     "Kendi borcunu iki katına çıkarır.",
     "Süre vermeksizin hemen döner.",
     "Borcu doğrudan düşürür."],
    "Md. 123'e göre karşılıklı borç yükleyen sözleşmelerde taraflardan biri temerrüde düşerse diğeri ifa için uygun bir süre "
    "verebilir veya süre verilmesini hâkimden isteyebilir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
