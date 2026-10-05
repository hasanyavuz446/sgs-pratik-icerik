#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Amme Alacaklarinin Tahsil Usulu — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim: kapsam ve borclu, teminat, ihtiyati haciz ve tahakkuk, ruchan ve sorumluluk (m. 21-36), odeme-mahsup, tecil (7582 ile 72 ay; CK 11414 teminatsiz sinir), gecikme zammi, cebren tahsil, haciz ve satis, zamanasimi, terkin, cezalar. 17 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6183 sayili AATUHK guncel metni (mevzuat.gov.tr; 7582 m. 48 dahil, yururluk tablosu kontrol edildi)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/amme_alacaklari.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "amme-gen-"


def patch(stem, options, answer, solution, ref='6183 sayili Amme Alacaklarinin Tahsil Usulu Hakkinda Kanun'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Aşağıdaki alacaklardan hangisi 6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun hükümlerine göre takip edilmez?',
        {
            'A': 'Belediyenin kiraya verdiği dükkânın kira alacağı',
            'B': 'Vergi cezasına bağlı gecikme zammı',
            'C': 'Kesinleşmiş idari para cezası',
            'D': 'Belediyenin emlak vergisi ile buna bağlı gecikme zammı alacağı',
            'E': 'Ceza tahkikine ait muhakeme masrafı',
        },
        'A',
        "m. 1'e göre Kanun; Devlete, il özel idarelerine ve belediyelere ait vergi, resim, harç, ceza tahkik ve takiplerine ait muhakeme masrafı, vergi ve para cezası gibi asli, gecikme zammı ve faiz gibi fer'i alacaklar ile **akitten, haksız fiil ve haksız iktisaptan doğanlar dışında** kalan kamu hizmeti kaynaklı alacaklara uygulanır. Kira sözleşmesinden doğan alacak **akitten doğduğu** için genel hükümlere göre takip edilir.",
        '6183 sayılı Kanun m. 1',
    ),
    # düzey 1
    '0002': patch(
        'Amme borçlusunun eşinin ölümü hâlinde borçlu hakkındaki takip, ölüm günü dâhil kaç gün geri bırakılır?',
        {
            'A': '3',
            'B': '7',
            'C': '15',
            'D': '1',
            'E': '30',
        },
        'A',
        "m. 50'ye göre karısı veya kocası, kan ve sıhriyet itibarıyla usul veya fürunundan birisi ölen borçlu hakkındaki takip **ölüm günü ile beraber üç gün** geri bırakılır. Borçlunun kendi ölümünde de terekenin borçları için takip üç gün geri bırakılır.",
        '6183 sayılı Kanun m. 50',
    ),
    # düzey 2
    '0003': patch(
        'Hükümetçe belli edilen ve teminatın kabulüne en yakın borsa cetveline göre değeri 200.000 ₺ olan millî tahviller teminat olarak gösterilmiştir. Bu tahviller kaç ₺ olarak değerlendirilir?',
        {
            'A': '190.000',
            'B': '185.000',
            'C': '200.000',
            'D': '240.000',
            'E': '170.000',
        },
        'E',
        "m. 10/4'e göre hükümetçe belli edilecek millî esham ve tahvilat, teminatın kabul edilmesine en yakın borsa cetvelleri üzerinden **%15 noksanıyla** değerlendirilir: 200.000 × 0,85 = **170.000 ₺**.",
        '6183 sayılı Kanun m. 10/4',
    ),
    # düzey 2
    '0004': patch(
        "6183 sayılı Kanun'un 9. maddesine göre tahsil dairesi hangi durumda borçludan teminat ister?",
        {
            'A': 'Borçlu tecil talebinde bulunmuşsa',
            'B': 'Borçlu adres değişikliği bildirmişse',
            'C': 'Borçlu beyannamesini süresinde verip vergisini son ödeme gününde ödemişse',
            'D': 'Borçlunun başka ilde şubesi varsa',
            'E': "VUK m. 359'daki fiillere temas eden tarhiyat için işlemlere başlanmışsa",
        },
        'E',
        "m. 9'a göre VUK m. 344 uyarınca vergi ziyaı cezası kesilmesini gerektiren hâller ile **m. 359'da sayılan hâllere temas eden** bir amme alacağının salınması için işlemlere başlanmışsa, inceleme elemanlarının ilk hesaplarına göre belirlenen miktar üzerinden teminat istenir. Türkiye'de ikametgâhı olmayan borçludan da tahsilin tehlikede olduğu durumlarda teminat istenebilir.",
        '6183 sayılı Kanun m. 9',
    ),
    # düzey 2
    '0005': patch(
        "6183 sayılı Kanun'a göre ihtiyati tahakkuk kimin yazılı emriyle yapılır?",
        {
            'A': 'Vergi mahkemesi hâkiminin',
            'B': 'İtiraz komisyonu başkanının',
            'C': 'VD müdürünün talebiyle defterdar veya VD başkanının',
            'D': "Vergi müfettişinin re'sen",
            'E': 'Tahsil memurunun',
        },
        'C',
        "m. 17'ye göre ihtiyati tahakkuk, vergi dairesi müdürünün (vergi dairesi başkanlıklarında grup müdürü veya müdürün) yazılı talebi üzerine **defterdar ve/veya vergi dairesi başkanının** yazılı emriyle yapılır ve vergi dairesi müdürünce derhal uygulanır.",
        '6183 sayılı Kanun m. 17',
    ),
    # düzey 3
    '0006': patch(
        'İpotekli bir taşınmaz haczedilip satılmıştır. Satış bedelinden, aynı taşınmaza ait emlak vergisi borcu hangi sırada ödenir?',
        {
            'A': 'İpotekli alacaklardan önce',
            'B': 'İpotekli (rehinli) alacaklardan sonra',
            'C': 'İpotekli alacakla birlikte satış bedelinden garameten',
            'D': 'Diğer amme alacaklarından sonra',
            'E': 'Satış masraflarından önce',
        },
        'B',
        "m. 21/2'ye göre rehinli alacaklıların hakları saklıdır. 7101 sayılı Kanunla değişen cümleye göre **gümrük resmi, bina ve arazi vergisi gibi eşya ve gayrimenkulün aynından doğan amme alacakları**, o eşya ve gayrimenkul bedelinden tahsilde **rehinli alacaklardan sonra** gelir.",
        '6183 sayılı Kanun m. 21/2',
    ),
    # düzey 3
    '0007': patch(
        'Vergi borcu olan bir tacir, dört yıl önce borcun tahsilini engellemek amacıyla, bu amacı bilen arkadaşına fabrikasını satmıştır. Tacirin başka malı yoktur. Bu satış hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi dairesi onaylarsa geçerli olur',
            'B': 'Satış ceza davası açılmadıkça geçerlidir',
            'C': 'Hükümsüzdür; iptal davası açılabilir',
            'D': 'İki yıldan eski olduğu için iptal edilemez',
            'E': 'Bedel ödendiği için geçerlidir',
        },
        'C',
        "m. 30'a göre borçlunun malı bulunmadığı veya borca yetmediği hâlde amme alacağının tahsiline imkân bırakmamak maksadıyla yapılan tek taraflı işlemler ile **borçlunun maksadını bilen veya bilmesi gereken kişilerle** yapılan işlemler **tarihleri ne olursa olsun hükümsüzdür**. m. 26'daki beş yıllık süre dolmadığından iptal davası açılabilir.",
        '6183 sayılı Kanun m. 30, 26',
    ),
    # düzey 3
    '0008': patch(
        "Bir limited şirketten tahsil edilemeyen amme alacağı 600.000 ₺'dir. Ortak A şirket sermayesinin %60'ına, ortak B %40'ına sahiptir. 6183 sayılı Kanun'a göre bu alacaktan A'nın doğrudan sorumlu olduğu tutar kaç ₺'dir?",
        {
            'A': '0',
            'B': '300.000',
            'C': '600.000',
            'D': '360.000',
            'E': '240.000',
        },
        'D',
        "m. 35'e göre limited şirket ortakları, şirketten tamamen veya kısmen tahsil edilemeyen veya tahsil edilemeyeceği anlaşılan amme alacağından **sermaye hisseleri oranında doğrudan doğruya** sorumludur: 600.000 × %60 = **360.000 ₺**. 600.000 ₺ müteselsil ve tam sorumluluk, 300.000 ₺ eşit paylaşım varsayımıyla bulunur.",
        '6183 sayılı Kanun m. 35',
    ),
    # düzey 2
    '0009': patch(
        'Kanuni temsilcilerin sorumluluğuna (6183 sayılı Kanun mükerrer m. 35) ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tüzel kişiliği olmayan teşekkülleri idare edenler de sorumludur',
            'B': 'Tasfiye, tasfiyeden önceki döneme ait sorumluluğu kaldırmaz',
            'C': 'Tüzel kişiden alınamayan alacak şahsi malvarlıklarından alınır',
            'D': 'Ödedikleri tutarlar için asıl borçluya rücu edemezler',
            'E': "Yabancı kurumların Türkiye'deki mümessillerine de uygulanır",
        },
        'D',
        "Mükerrer m. 35'e göre tüzel kişilerin ve tüzel kişiliği olmayan teşekküllerin malvarlığından tahsil edilemeyen amme alacakları kanuni temsilcilerin ve teşekkülü idare edenlerin şahsi malvarlıklarından alınır; hüküm yabancı kurumların Türkiye'deki mümessillerine de uygulanır ve tasfiye, önceki döneme ait sorumluluğu kaldırmaz. Temsilciler ödedikleri tutarlar için **asıl amme borçlusuna rücu edebilir**.",
        '6183 sayılı Kanun mük. m. 35',
    ),
    # düzey 2
    '0010': patch(
        "Amme alacağının kredi kartıyla ödenmesi hâlinde ödeme 6183 sayılı Kanun'a göre hangi gün yapılmış sayılır?",
        {
            'A': 'İşlemin kartla yapıldığı gün',
            'B': 'Bankanın parayı Merkez Bankasına aktardığı gün',
            'C': 'Tahsilatın vergi dairesi hesabına geçtiği gün',
            'D': 'Kart borcunun bankaya ödendiği gün',
            'E': 'Hesap özetinin kesildiği gün',
        },
        'A',
        "m. 44'e göre 41. madde uyarınca yapılan ödemelerde çekin tahsil dairesine veya bankaya verildiği, paranın bankaya veya postaneye yatırıldığı, **banka kartı, kredi kartı ve benzeri kartlarla yapılan ödemelerde işlemin kartla yapıldığı** gün ödeme yapılmış sayılır.",
        '6183 sayılı Kanun m. 44',
    ),
    # düzey 3
    '0011': patch(
        "Teminatsız tecil sınırının Cumhurbaşkanı Kararıyla 10.000.000 ₺ olarak uygulandığı varsayımıyla, bir borçlunun tahsil dairesi itibarıyla tecil edilecek toplam borcu 16.000.000 ₺'dir. 6183 sayılı Kanun'a göre gösterilmesi zorunlu teminat tutarı kaç ₺'dir?",
        {
            'A': '16.000.000',
            'B': '0',
            'C': '8.000.000',
            'D': '3.000.000',
            'E': '6.000.000',
        },
        'D',
        "m. 48/2'ye göre tecil edilen borçlar toplamı sınırı aşmadığında teminat aranmaz; sınırın üzerindeki alacakların tecilinde **gösterilmesi zorunlu teminat tutarı, sınırı aşan kısmın yarısıdır**: (16.000.000 − 10.000.000) / 2 = **3.000.000 ₺**. Kanundaki sınır 7582 sayılı Kanunla 1.000.000 ₺ yapılmış, Cumhurbaşkanı 11414 sayılı Kararla bu tutarın 10.000.000 ₺ uygulanmasına karar vermiştir.",
        '6183 sayılı Kanun m. 48/2',
    ),
    # düzey 2
    '0012': patch(
        'Vergiye uyumlu mükelleflerin borçlarının tecili (6183 sayılı Kanun m. 48/A) bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vadesi üç yılı geçmemiş alacaklar kapsama girer',
            'B': 'Son 3 yılın beyannameleri kanuni sürede verilmiş olmalıdır',
            'C': 'Faiz ve teminat alınarak tecil edilir',
            'D': 'Başvuru tarihinde en az 3 yıllık mükellefiyet aranır',
            'E': 'Tecil süresi 36 ayı geçemez',
        },
        'A',
        "m. 48/A'ya göre bu tecil, **vadesi bir yılı geçmemiş** alacaklar için Maliye Bakanınca **36 ayı geçmemek üzere faiz ve teminat alınarak** yapılabilir. Borçlunun başvuru tarihinde en az üç yıl süreyle ticari, zirai veya mesleki faaliyet nedeniyle yıllık gelir veya kurumlar vergisi mükellefi olması ve son üç yıla ait beyannamelerini kanuni sürelerinde vermiş olması gerekir.",
        '6183 sayılı Kanun m. 48/A',
    ),
    # düzey 3
    '0013': patch(
        "Belediye sınırları dışındaki bir köyde oturan borçluya ait ödeme emri muhtarlığa verilmiş, ancak 15 gün içinde tebliğ edilememiştir. 6183 sayılı Kanun'a göre ne yapılır?",
        {
            'A': 'Takip bir yıl ertelenir',
            'B': 'Tebligat, ilan yoluyla ve borçlunun son adresine yapıştırılarak yapılır',
            'C': 'Ödeme emri iptal edilir ve takip durur',
            'D': 'Borçlu hakkında doğrudan haciz uygulanır',
            'E': 'Borçlu ödeme cetveline alınır; cetvel 10 gün asılır',
        },
        'E',
        "m. 55'e göre köylerdeki borçlulara ödeme emirleri muhtarlıkça tebliğ edilir; muhtarlığa tevdiden itibaren 15 gün içinde tebliğ yapılamazsa borçluların isimleri ödeme emri niteliğindeki bir **ödeme cetveline** alınır. Cetvel köy ihtiyar kurulu kapısına ve herkesin görebileceği bir yere **10 gün** asılarak tebliğ olunur; takip cetvelin indirilmesi tarihinde başlamış olur.",
        '6183 sayılı Kanun m. 55',
    ),
    # düzey 2
    '0014': patch(
        'Ödeme emrine itiraza ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İtiraz komisyonunun bu konudaki kararları kesindir',
            'B': 'Kısmi itirazda itiraz edilen kısım açıkça gösterilir',
            'C': 'Borcun bir kısmına itiraz, mal bildirimi süresini uzatır',
            'D': 'Komisyon itirazı en geç 7 gün içinde karara bağlar',
            'E': 'İtiraz tebliğden itibaren 15 gün içinde yapılır',
        },
        'C',
        "m. 58'e göre ödeme emrine tebliğden itibaren **15 gün** içinde vergi itiraz komisyonunda itiraz edilir; komisyon itirazı **en geç 7 gün** içinde karara bağlar ve kararları kesindir. Borcun bir kısmına itiraz edenin o kısmın cihet ve miktarını açıkça göstermesi gerekir. **Borcun bir kısmına yapılan itirazlar mal bildiriminde bulunma süresini uzatamaz**.",
        '6183 sayılı Kanun m. 58',
    ),
    # düzey 2
    '0015': patch(
        "Tahsil dairesi, borçlunun bir kısım mallarını haczedecektir. Borçlunun başkasına ait olduğunu beyan ettiği mallar hakkında 6183 sayılı Kanun'a göre nasıl davranılır?",
        {
            'A': 'Önce bu mallar haczedilir',
            'B': 'Bu malların haczi en sonraya bırakılır',
            'C': 'Beyan üzerine mallar üçüncü kişiye teslim edilir',
            'D': 'Mallar yarı değerle haczedilir',
            'E': 'Bu mallar haczedilemez',
        },
        'B',
        "m. 62'ye göre borçlu tarafından başkasının olduğu beyan edilen veya üçüncü şahıs tarafından ihtiyaten haciz ya da istihkak iddia edilen **malların haczi en sonraya bırakılır**. Tahsil dairesi alacaklı idare ile borçlunun menfaatlerini mümkün olduğunca bağdaştırmakla yükümlüdür.",
        '6183 sayılı Kanun m. 62',
    ),
    # düzey 3
    '0016': patch(
        "Aylık net geliri asgari ücretin üzerinde olan borçlunun aylık maaşı 90.000 ₺'dir. 6183 sayılı Kanun'a göre bu maaştan haczedilecek aylık tutarın alt ve üst sınırı nedir?",
        {
            'A': '9.000 ile 30.000 ₺ arası',
            'B': '22.500 ile 30.000 ₺ arası',
            'C': '22.500 ile 45.000 ₺ arası',
            'D': '9.000 ile 22.500 ₺ arası',
            'E': '30.000 ile 45.000 ₺ arası',
        },
        'B',
        "m. 71'e göre aylıklar, ücretler ve emekli aylıkları kısmen haczolunabilir; haczolunacak miktar bunların **üçte birinden çok, dörtte birinden az olamaz**: alt sınır 90.000 / 4 = 22.500 ₺, üst sınır 90.000 / 3 = 30.000 ₺. Asgari ücreti aşmayan aylık gelirlerde ise ayrı bir sınır uygulanır.",
        '6183 sayılı Kanun m. 71',
    ),
    # düzey 3
    '0017': patch(
        "Haczedilen ve 200.000 ₺ değer biçilen bir menkul mal için ilk açık artırmada verilen en yüksek teklif 140.000 ₺'dir. 6183 sayılı Kanun'a göre ne yapılır?",
        {
            'A': 'Satış yapılmaz; mal 15 gün içinde tekrar artırmaya çıkarılır',
            'B': 'Mal pazarlıkla satılır',
            'C': 'Mal borçluya iade edilir',
            'D': "Mal en yüksek teklif olan 140.000 ₺'ye satılır ve haciz kaldırılır",
            'E': 'Mal idarece teferruğ edilir',
        },
        'A',
        "m. 87'ye göre menkul mallara verilen bedel biçilen değerin **%75'inden** (burada 150.000 ₺) aşağı olursa veya alıcı çıkmazsa, ilk artırma tarihinden itibaren **15 gün içinde** mal tekrar satışa çıkarılır; bu ikinci artırmada verilen bedel ne olursa olsun satış yapılır. 140.000 ₺ bu sınırın altındadır.",
        '6183 sayılı Kanun m. 87',
    ),
    # düzey 2
    '0018': patch(
        "Rayiç değeri 1.000.000 ₺ biçilen ve artırmalarda satılamayan bir gayrimenkul, satış komisyonu kararıyla alacaklı amme idaresince teferruğ edilecektir. Teferruğ bedeli kaç ₺'dir?",
        {
            'A': '900.000',
            'B': '750.000',
            'C': '250.000',
            'D': '1.000.000',
            'E': '500.000',
        },
        'E',
        "m. 98'e göre ikinci artırmadan itibaren bir yıl içinde en az bir kez daha satışa çıkarıldığı hâlde satılamayan gayrimenkul alacaklı idarece teferruğ edilebilir; **teferruğ bedeli biçilen rayiç değerin %50'sidir**. Borçlu teferruğ kararından itibaren bir yıl içinde borcunu gecikme zammıyla öderse gayrimenkul kendisine geri verilir.",
        '6183 sayılı Kanun m. 98',
    ),
    # düzey 1
    '0019': patch(
        "İflas eden amme borçlusu için mahkemece tasdik edilen konkordato, 6183 sayılı Kanun'a göre amme alacakları bakımından nasıl bir sonuç doğurur?",
        {
            'A': 'Amme idaresi iflas istemişse bağlar',
            'B': 'Vergi aslını bağlar, cezaları bağlamaz',
            'C': 'Amme alacaklarını yarı oranda bağlar',
            'D': 'Amme alacakları için mecburi değildir',
            'E': 'Amme alacaklarını da bağlar',
        },
        'D',
        "m. 101'e göre amme idaresi tarafından iflas talebinde bulunulmuş olsa dahi **tasdik edilen konkordato amme alacakları için mecburi değildir**.",
        '6183 sayılı Kanun m. 101',
    ),
    # düzey 2
    '0020': patch(
        "Hakkında takip başlatılan bir amme borçlusu, tahsili engellemek amacıyla malını muvazaalı olarak yakınına devretmiş ve kalan malları borcu karşılamamıştır. 6183 sayılı Kanun'a göre öngörülen yaptırım nedir?",
        {
            'A': 'Borcun iki katı idari para cezası',
            'B': 'Altı aydan üç yıla kadar hapis',
            'C': 'Üç aya kadar hapis',
            'D': 'Elli güne kadar adli para cezası',
            'E': 'Bir yıldan beş yıla kadar hapis',
        },
        'B',
        "m. 110'a göre takip muamelelerine başlanan borçlu tahsile engel olmak veya zorlaştırmak maksadıyla mallarını gizleyerek, kaçırarak **muvazaa yoluyla başkasına geçirerek** varlığını yok eder veya azaltırsa ve kalan mallar borcu karşılamazsa **altı aydan üç yıla kadar hapis** cezası ile cezalandırılır. Suç, alacaklı idarenin en büyük memurunun ihbarı üzerine savcılıkça takip edilir.",
        '6183 sayılı Kanun m. 110',
    ),
    # düzey 1
    '0021': patch(
        "6183 sayılı Kanun'un 3. maddesine göre 'alacaklı amme idaresi' terimi aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'Devlet ve Sosyal Güvenlik Kurumu',
            'B': 'Devlet, belediyeler ve meslek kuruluşları',
            'C': 'Devlet, il özel idareleri ve belediyeler',
            'D': 'Devlet ve kamu iktisadi teşebbüsleri',
            'E': 'Devlet, belediyeler ve köyler',
        },
        'C',
        "m. 3'e göre alacaklı amme idaresi terimi **Devleti, il özel idarelerini ve belediyeleri** ifade eder. Tahsil dairesi ise alacaklı amme idaresinin Kanunu uygulamakla görevli dairesi, servisi veya memurlarıdır.",
        '6183 sayılı Kanun m. 3',
    ),
    # düzey 2
    '0022': patch(
        'Amme borçlusunun ölümü üzerine mirasçı, mirası resmî defter tutulması yoluyla kabul etmiştir. Defterde yer almayan bir vergi borcu sonradan ortaya çıkmıştır. Mirasçının bu borçtan sorumluluğu nasıldır?',
        {
            'A': 'Diğer mirasçılar ödemezse sorumludur',
            'B': 'Borcun yarısından sorumludur',
            'C': 'Mirastan kendisine düşen miktarla sorumludur',
            'D': 'Deftere kaydedilmediği için sorumlu değildir',
            'E': 'Kendi malvarlığıyla sınırsız sorumludur',
        },
        'C',
        "m. 7'ye göre mirasın tutulan defter gereğince kabulü hâlinde mirasçı, amme alacağı **deftere kaydedilmemiş olsa dahi** mirastan kendisine düşen miktar ile sorumludur. Defter tutma işlemi sürdükçe satış yapılamaz.",
        '6183 sayılı Kanun m. 7',
    ),
    # düzey 2
    '0023': patch(
        'Teminat gösteremeyen borçlunun şahsi kefil göstermesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kefil, müteselsil kefil ve müşterek borçlu olur',
            'B': 'Kefil, asıl borçlunun tabi olduğu usullerle takip edilir',
            'C': 'Borcu ödeyen kefile bunu gösteren belge verilir',
            'D': 'Kefalet noterden onaylı sözleşmeyle kurulur',
            'E': 'Tahsil dairesi gösterilen kefili reddedemez',
        },
        'E',
        "m. 11'e göre teminat sağlayamayanlar muteber bir şahsı müteselsil kefil ve müşterek müteselsil borçlu gösterebilir; kefalet noterden tasdikli sözleşmeyle kurulur ve ödeyen kefile belge verilir. Ancak **şahsi kefaleti ve gösterilen kişiyi kabul edip etmemekte tahsil dairesi muhtardır**. m. 57'ye göre kefil asıl borçlular gibi takip edilir.",
        '6183 sayılı Kanun m. 11, 57',
    ),
    # düzey 2
    '0024': patch(
        "Aşağıdakilerden hangileri 6183 sayılı Kanun'a göre ihtiyati haciz sebebidir?\n\nI. Borçlunun belli bir ikametgâhının bulunmaması\n\nII. İstenen teminatın belli sürede gösterilmemesi\n\nIII. Para cezası gerektiren fiil nedeniyle kamu davası açılmış olması\n\nIV. Borçlunun tecil talebinin reddedilmiş olması",
        {
            'A': 'I, II ve III',
            'B': 'II, III ve IV',
            'C': 'I, II, III ve IV',
            'D': 'I ve IV',
            'E': 'I ve II',
        },
        'A',
        "m. 13'e göre borçlunun belli ikametgâhının olmaması (I), teminat istendiği hâlde belli sürede teminat veya kefil gösterilmemesi (II) ve hüküm verilmiş olsun olmasın **para cezası gerektiren fiil nedeniyle kamu davası açılması** (III) ihtiyati haciz sebepleridir. Tecil talebinin reddedilmesi (IV) sayılan sebepler arasında değildir.",
        '6183 sayılı Kanun m. 13',
    ),
    # düzey 3
    '0025': patch(
        'İhtiyati tahakkuka ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Matrahı belli olmayanlar geçici olarak takdir edilir',
            'B': 'İhtiyaten tahakkuk eden vergi derhal tahsil edilir',
            'C': 'Tahakkuk eden vergiler için derhal ihtiyati haciz uygulanır',
            'D': 'Matrahı belli olanlar itirazlı olsun olmasın tahakkuk ettirilir',
            'E': 'Geçici takdirler en geç bir hafta içinde yapılır',
        },
        'B',
        "m. 18'e göre ihtiyati tahakkuk eden vergi ve resimler **kanunlarına göre ödeme zamanları gelmeden tahsil olunmaz**; ancak bunlar için derhal ihtiyati haciz uygulanır. Matrahı belli olanlar itirazlı olsun olmasın tahakkuk ettirilir, belli olmayanlar dış karinelere göre geçici takdirle hesaplanır ve takdirler talepten itibaren en geç bir hafta içinde yapılır.",
        '6183 sayılı Kanun m. 18',
    ),
    # düzey 3
    '0026': patch(
        "6183 sayılı Kanun'un 22/A maddesi kapsamında borç sorgulaması gereken bir kamu ödemesine ilişkin alacağı devralan kişinin hakkı hangi tutar üzerinde hüküm ifade eder?",
        {
            'A': 'Alacağın yarısı',
            'B': 'Vergi borcuyla garameten paylaşılan tutar',
            'C': 'Alacağın tamamı',
            'D': 'Vadesi geçmiş vergi borcu ayrıldıktan sonra kalan tutar',
            'E': 'Devir tarihindeki nominal tutar',
        },
        'D',
        "m. 22/A'ya göre zorunluluk getirilen ödemelere ilişkin olarak, işçi ücreti alacakları hariç, yapılacak her türlü devir, temlik ve el değiştirme, Maliye Bakanlığına bağlı tahsil dairelerine **vadesi geçmiş borcu karşılayacak kısım ayrıldıktan sonra kalan kısım** üzerinde hüküm ifade eder.",
        '6183 sayılı Kanun m. 22/A',
    ),
    # düzey 2
    '0027': patch(
        "6183 sayılı Kanun'a göre hükümsüz sayılan bir tasarrufla borçludan mal edinen üçüncü kişinin durumu aşağıdakilerden hangisidir?",
        {
            'A': 'Malı iade eder ve karşılık olarak verdiği bedeli idareden geri alır',
            'B': 'Malı veya bedelini verir; verdiği karşılığı idareden isteyemez',
            'C': 'İyi niyetli olduğu için yükümlülüğü doğmaz',
            'D': 'Malın yarısını iade eder',
            'E': 'Malı elinde tutar; bedel üzerinden faiz öder',
        },
        'B',
        "m. 31'e göre 27-30. maddelerdeki tasarruf ve işlemlerden faydalananlar elde ettiklerini, elden çıkarmışlarsa takdir edilecek bedelini vermekle yükümlüdür. Bunlar **karşılık olarak verdikleri şeyden dolayı alacaklı amme idaresinden talepte bulunamazlar**.",
        '6183 sayılı Kanun m. 31',
    ),
    # düzey 3
    '0028': patch(
        "Bir anonim şirketin tasfiye memuru, 300.000 ₺ tutarındaki vergi borcunu ödemeden veya ayırmadan tasfiye sonucunda elde edilen 200.000 ₺'yi ortaklara dağıtmıştır. Tasfiye memurunun bu vergi borcundan şahsen sorumlu olacağı azami tutar kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '300.000',
            'C': '200.000',
            'D': '250.000',
            'E': '400.000',
        },
        'C',
        "m. 33'e göre tasfiye memurları amme alacaklarını ödemeden veya ayırmadan tasfiye sonucunu dağıtırlarsa şahsen ve müteselsilen sorumlu olur; ancak **bu sorumluluk yapılan tasarrufların ifade ettiği para miktarını geçemez**. Dağıtılan tutar 200.000 ₺ olduğundan sorumluluk da bu tutarla sınırlıdır. Tasfiye memurunun ortaklara rücu hakkı saklıdır.",
        '6183 sayılı Kanun m. 33',
    ),
    # düzey 2
    '0029': patch(
        "Amme borçlusunun başka malı bulunmamakta, ancak bir kollektif şirkette ortaklık payı bulunmaktadır. Amme alacağının bu paydan tahsili için 6183 sayılı Kanun'a göre ne istenebilir?",
        {
            'A': 'Şirketin iflası',
            'B': 'Ortaklığın feshi',
            'C': 'Diğer ortakların hapisle tazyiki',
            'D': 'Şirketin tüm borçlarının ödenmesi',
            'E': 'Payın bedelsiz devri',
        },
        'B',
        "m. 34'e göre borçluya ait mal bulunmadığı, amme alacağını karşılamaya yetmediği veya teminat gösterilmediği takdirde, borçlunun **sermayesi paylara bölünmemiş** ortaklıklardaki hisselerinden amme alacağının tahsili için genel hükümler çerçevesinde **ortaklığın feshi** istenebilir. Sermayesi paylara bölünmüş komandit şirketlerin komandite ortakları için de bu hüküm uygulanır.",
        '6183 sayılı Kanun m. 34',
    ),
    # düzey 2
    '0030': patch(
        "7582 sayılı Kanunla yapılan değişiklikten sonra, 6183 sayılı Kanun'un 48. maddesine göre amme alacağı en fazla kaç ay süreyle tecil edilebilir?",
        {
            'A': '60',
            'B': '36',
            'C': '24',
            'D': '72',
            'E': '48',
        },
        'D',
        "7582 sayılı Kanunla (yürürlük 4/6/2026) m. 48/1'deki **36 ay** ibaresi **72 ay** olarak değiştirilmiştir. Tecil, vadesinde ödeme veya haciz ya da haczedilen malın paraya çevrilmesi borçluyu çok zor duruma düşürecekse, yazılı talep ve teminat şartıyla faiz alınarak yapılır. Vergiye uyumlu mükelleflere özgü m. 48/A'daki tecil süresi ise 36 aydır.",
        '6183 sayılı Kanun m. 48',
    ),
    # düzey 3
    '0031': patch(
        "Tecil talebi uygun görülmeyerek reddedilen borçlu, reddin tebliğinden sonra idarece verilen 20 günlük süre içinde borcunu ödemiştir. 6183 sayılı Kanun'a göre bu ödeme nasıl sonuç doğurur?",
        {
            'A': 'Tecil reddedildiği için hapisle tazyik uygulanır',
            'B': 'Faiz ve gecikme zammı alınmaz, borç kapanır',
            'C': 'Ödeme geçersiz sayılır ve takip sürer',
            'D': 'Gecikme zammıyla birlikte tahsil edilir',
            'E': 'Ödeme tarihine kadar faiz alınarak tecil olunur',
        },
        'E',
        "m. 48/3'e göre tecil talebi reddedilen borçlular, reddin tebliği tarihinden itibaren **idarece 30 güne kadar verilebilecek** ödeme süresi içinde borçlarını öderlerse bu alacak, **ödendiği tarihe kadar faiz alınmak suretiyle tecil olunur**.",
        '6183 sayılı Kanun m. 48/3',
    ),
    # düzey 2
    '0032': patch(
        "Hakkında aciz hâli tespit edilen bir amme borçlusu için 6183 sayılı Kanun'a göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Zamanaşımı işlemez hâle gelir',
            'B': 'Borç derhal terkin edilir',
            'C': 'Borçlu hapisle tazyik edilir',
            'D': 'Teminat ve faiz aranmadan tecil yapılabilir',
            'E': 'Alacak özel alacaklılara devredilir',
        },
        'D',
        "m. 76'ya göre aciz hâlindeki borçlu hakkında **teminat ve faiz aranmadan** m. 48 hükmü (tecil) uygulanabilir. Alacaklı tahsil dairesi aciz hâlindeki borçlunun mali durumunu zamanaşımı süresi içinde sürekli takip eder.",
        '6183 sayılı Kanun m. 76',
    ),
    # düzey 2
    '0033': patch(
        "Aşağıdakilerden hangisi 6183 sayılı Kanun'un 54. maddesinde sayılan cebren tahsil şekillerinden biri değildir?",
        {
            'A': 'Kefilin takip edilmesi',
            'B': 'Malların haczedilerek paraya çevrilmesi',
            'C': 'Borçlunun hapisle tazyik edilmesi',
            'D': 'Teminatın paraya çevrilmesi',
            'E': 'Borçlunun iflasının istenmesi',
        },
        'C',
        "m. 54'e göre cebren tahsil; teminat gösterilmişse **teminatın paraya çevrilmesi veya kefilin takibi**, borca yetecek **malların haczedilerek paraya çevrilmesi** ve şartları varsa **iflas istenmesi** yollarıyla yapılır. Hapisle tazyik ise mal bildiriminde bulunmayan borçluya m. 60 uyarınca uygulanan bir yaptırımdır.",
        '6183 sayılı Kanun m. 54',
    ),
    # düzey 1
    '0034': patch(
        'Mal bildiriminde borca yetecek malı olmadığını bildiren borçlu, sonradan edindiği malları edinme tarihinden itibaren kaç gün içinde tahsil dairesine bildirmelidir?',
        {
            'A': '60',
            'B': '23',
            'C': '15',
            'D': '30',
            'E': '20',
        },
        'C',
        "m. 61'e göre mal bildiriminde malı olmadığını gösteren veya borca yetecek kadar mal göstermeyen borçlu, sonradan edindiği malları ve gelirindeki artmaları **edinme ve artma tarihinden itibaren 15 gün içinde** bildirmek zorundadır. Bildirmeyenler m. 112'ye göre bir yıla kadar hapisle cezalandırılır.",
        '6183 sayılı Kanun m. 61',
    ),
    # düzey 3
    '0035': patch(
        'Vergi dairesinin haczettiği bir mala, bu hacizden önce tahakkuk etmiş alacağı için belediye de mal paraya çevrilmeden hacze iştirak etmiştir. Satış bedeli nasıl kullanılır?',
        {
            'A': 'Önce belediyenin alacağı ödenir',
            'B': 'Önce haczi yapan vergi dairesinin alacağı ödenir',
            'C': 'Alacaklar arasında satış bedelinden garameten paylaştırılır',
            'D': 'Bedel iki idareye eşit bölünür',
            'E': 'Belediye hacze iştirak edemez',
        },
        'B',
        "m. 69'a göre her amme idaresi, alacağı haciz tarihinden önce tahakkuk etmiş olmak şartıyla diğer bir amme idaresinin hacizlerine, mal paraya çevrilinceye kadar iştirak edebilir. Bu durumda **ilk önce haczi yapan dairenin alacağı** tahsil edilir; artan kısım iştirak tarihi sırasıyla iştirak eden dairelere ödenir. Özel alacaklı ile birlikte hacizde ise m. 21 uyarınca garame uygulanır.",
        '6183 sayılı Kanun m. 69',
    ),
    # düzey 3
    '0036': patch(
        "Vergi dairesince haczedilen bir otomobile 500.000 ₺ değer biçilmiştir. 6183 sayılı Kanun'un 74/A maddesine göre haczin kaldırılması için takip masrafları dışında en az kaç ₺ ödenmelidir?",
        {
            'A': '450.000',
            'B': '400.000',
            'C': '550.000',
            'D': '500.000',
            'E': '525.000',
        },
        'C',
        "m. 74/A'ya göre m. 10/5'te sayılan mallardan olan mahcuz mal üzerindeki haciz; **mala biçilen değer ile %10 fazlasının** ilk sırada haciz uygulayan tahsil dairesine ödenmesi, takip masraflarının ayrıca ödenmesi ve hacze karşı dava açılmaması şartıyla kaldırılır: 500.000 × 1,10 = **550.000 ₺**. Ödenecek tutar tahsil dairelerine olan vadesi gelmiş borçların toplamını aşamaz.",
        '6183 sayılı Kanun m. 74/A',
    ),
    # düzey 2
    '0037': patch(
        'Haciz işlemlerine (6183 sayılı Kanun m. 78) ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gıyapta hacizde zaptın örneği borçluya tebliğ edilir',
            'B': 'Gece çalışan yerlerde hasılat haczi gece yapılabilir',
            'C': 'Gıyapta hacizde iki komşu veya zabıta memuru bulunur',
            'D': 'Tatil günlerinde haciz yapılmasına genel bir sınır yoktur',
            'E': 'Haciz zaptı elektronik ortamda düzenlenebilir',
        },
        'D',
        "m. 78'e göre **güneş battıktan doğuncaya kadar ve tatil günlerinde haciz yapılamaz**; tatil günlerinde veya geceleri çalışılan yerlerdeki hasılat haczi ile mal kaçırıldığının anlaşıldığı hâller istisnadır. Gıyapta hacizde zabıta memuru, muhtar, ihtiyar kurulu üyesi veya iki komşu bulundurulur ve zaptın örneği derhal tebliğ edilir. 7491 sayılı Kanunla haciz zaptının elektronik ortamda düzenlenmesine imkân tanınmıştır.",
        '6183 sayılı Kanun m. 78',
    ),
    # düzey 3
    '0038': patch(
        "Rayiç değeri 1.000.000 ₺ olan bir gayrimenkulün artırmasında en yüksek teklif 700.000 ₺ olmuştur. Rüçhanlı alacak yoktur. 6183 sayılı Kanun'a göre ne yapılır?",
        {
            'A': "Gayrimenkul en yüksek teklif olan 700.000 ₺'ye hemen ihale edilir",
            'B': 'Artırma iptal edilir, haciz kalkar',
            'C': 'Satış bir yıl sonraya ertelenir',
            'D': 'Gayrimenkul idarece teferruğ edilir',
            'E': 'Artırma 7 gün uzatılır; sonra en çok artırana ihale edilir',
        },
        'E',
        "m. 94'e göre ihale için artırma bedelinin biçilen değerin **%75'ini** (750.000 ₺) bulması gerekir. m. 95'e göre bu miktar elde edilmezse en çok artıranın taahhüdü baki kalmak şartıyla artırma **7 gün daha uzatılır** ve 7. gün aynı saatte gayrimenkul en çok artırana ihale edilir.",
        '6183 sayılı Kanun m. 94-95',
    ),
    # düzey 3
    '0039': patch(
        'Vadesi 2020 yılında olan bir amme alacağı için 2023 yılında ödeme emri tebliğ edilmiş, başka bir kesme veya durma sebebi olmamıştır. Alacak hangi tarihin sonunda zamanaşımına uğrar?',
        {
            'A': '31 Aralık 2028',
            'B': '31 Aralık 2027',
            'C': '31 Aralık 2025',
            'D': '31 Aralık 2029',
            'E': '31 Aralık 2030',
        },
        'A',
        "Normal hesapla vade 2020 olduğundan zamanaşımı 31/12/2025'te dolardı. m. 103'e göre ödeme emri tebliği zamanaşımını keser ve zamanaşımı **kesilmenin rastladığı takvim yılını takip eden takvim yılı başından** itibaren yeniden işler: 1/1/2024'ten başlayan beş yıl **31/12/2028**'de dolar.",
        '6183 sayılı Kanun m. 103',
    ),
    # düzey 2
    '0040': patch(
        "Aşağıdakilerden hangisi 6183 sayılı Kanun'a göre tahsil zamanaşımının işlememesine (durmasına) yol açan durumlardan biridir?",
        {
            'A': 'Takibe imkân vermeyecek şekilde yurt dışında bulunma',
            'B': 'Borçlunun kefil göstermesi',
            'C': 'Borçlunun tecil talebinde bulunması',
            'D': 'Borçlunun başka bir ile taşınması',
            'E': 'Borçlunun itiraz komisyonuna başvurması',
        },
        'A',
        "m. 104'e göre **borçlunun yabancı memlekette bulunması, hileli iflas etmesi veya terekesinin tasfiyesi** dolayısıyla hakkında takip yapılmasına imkân yoksa, bu hâllerin devamı süresince zamanaşımı işlemez. Durma sebebi kalkınca zamanaşımı başlar veya kaldığı yerden devam eder; bu sonuç, zamanaşımını yeniden başlatan kesilmeden farklıdır.",
        '6183 sayılı Kanun m. 104',
    ),
    # düzey 2
    '0041': patch(
        "Aşağıdakilerden hangisi 6183 sayılı Kanun'a göre amme borçlusu sayılmaz?",
        {
            'A': 'Borca kefil olan kişi',
            'B': 'Tüzel kişinin kanuni temsilcisi',
            'C': 'Vergi sorumlusu',
            'D': "Yabancı kurumun Türkiye'deki temsilcisi",
            'E': 'Borçlunun mirasını reddeden mirasçısı',
        },
        'E',
        "m. 3'e göre amme borçlusu; amme alacağını ödemek mecburiyetinde olan gerçek ve tüzel kişiler ile bunların kanuni temsilcileri veya mirasçıları, vergi mükellefleri, vergi sorumlusu, kefil ve yabancı şahıs ve kurumların temsilcileridir. m. 7'ye göre Kanun hükümleri **mirası reddetmemiş** mirasçılar hakkında uygulanır; mirası reddeden mirasçı borçlu sayılmaz.",
        '6183 sayılı Kanun m. 3, 7',
    ),
    # düzey 2
    '0042': patch(
        "Aşağıdakilerden hangileri 6183 sayılı Kanun'a göre teminat olarak kabul edilir?\n\nI. Bankaların verdiği süresiz ve şartsız teminat mektubu\n\nII. Sigorta şirketlerinin verdiği süresiz ve şartsız kefalet senedi\n\nIII. Borçlunun müşterisinden aldığı vadeli çek",
        {
            'A': 'Yalnız III',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        "7417 sayılı Kanunla değişen m. 10/2'ye göre bankaların verdiği süresiz ve şartsız teminat mektupları (I) ile **sigorta şirketlerinin verdiği süresiz ve şartsız kefalet senetleri** (II) teminat olarak kabul edilir. Para, Devlet iç borçlanma senetleri, hükümetçe belli edilen tahviller ve haczedilen mallar da teminattır. Müşteri çeki (III) bu sayımda yer almaz.",
        '6183 sayılı Kanun m. 10',
    ),
    # düzey 2
    '0043': patch(
        "Bir otelin işletilmesinden doğan amme borçları için otelde bulunan eşyadan hangisi 6183 sayılı Kanun'a göre teminat hükmünde değildir?",
        {
            'A': 'Resepsiyondaki bilgisayarlar',
            'B': 'Lobi dekorasyon eşyaları',
            'C': 'Otelin mutfak malzemeleri',
            'D': 'Oda mobilyaları',
            'E': 'Otelde kalan misafirlerin kendi eşyaları',
        },
        'E',
        "m. 12'ye göre bar, otel, han, pansiyon gibi yerlerdeki eşya ve malzeme bu işletmelerden doğan amme borçlarına karşı teminat hükmündedir. Ancak noterden tasdikli kira sözleşmesinde gayrimenkul sahibinin demirbaşı olarak kayıtlı eşya ile **otel, han ve pansiyonlardaki misafir ve kiracıların kendilerine ait eşyaları** bu hükmün dışındadır.",
        '6183 sayılı Kanun m. 12',
    ),
    # düzey 3
    '0044': patch(
        "İhtiyati haczin kaldırılması için borçlunun göstereceği teminatlardan hangisi 6183 sayılı Kanun'a göre haczin kaldırılmasını sağlamaz?",
        {
            'A': 'Nakit para',
            'B': 'Devlet iç borçlanma senedi',
            'C': 'Haczedilen menkul mal',
            'D': 'Süresiz ve şartsız banka teminat mektubu',
            'E': 'Hükümetçe belli edilen millî tahvil',
        },
        'C',
        "m. 16'ya göre borçlu, **m. 10'un 5. bendinde yazılı menkul mallar hariç** olmak üzere bu maddeye göre teminat gösterirse ihtiyati haciz, haczi koyan merci tarafından kaldırılır. Haczedilen menkul mal teminat olarak gösterilse de ihtiyati haciz kalkmaz.",
        '6183 sayılı Kanun m. 16',
    ),
    # düzey 2
    '0045': patch(
        'Bir özel alacaklının icra dairesi aracılığıyla haczettiği mal paraya çevrilmeden önce aynı mala vergi dairesi de haciz koymuştur. Satış bedeli nasıl paylaştırılır?',
        {
            'A': 'Vergi dairesi hacze katılamaz',
            'B': 'Bedel yarı yarıya bölünür',
            'C': 'Önce ilk haczi koyan özel alacaklı alır',
            'D': 'Önce amme alacağı, kalan bedelle özel alacak ödenir',
            'E': 'Alacaklar arasında garameten paylaştırılır',
        },
        'E',
        "m. 21'e göre üçüncü şahıslar tarafından haczedilen mallar paraya çevrilmeden önce o mal üzerine amme alacağı için de haciz konulursa bu alacak da hacze iştirak eder ve **satış bedeli aralarında garameten taksim olunur**. Amme idareleri arasındaki hacze iştirakte ise m. 69'a göre önce haczi yapan dairenin alacağı ödenir.",
        '6183 sayılı Kanun m. 21',
    ),
    # düzey 1
    '0046': patch(
        "6183 sayılı Kanun'un 27-30. maddelerinde sayılan tasarrufların iptali için, tasarrufun yapıldığı tarihten itibaren kaç yıl geçtikten sonra dava açılamaz?",
        {
            'A': '2',
            'B': '1',
            'C': '10',
            'D': '5',
            'E': '3',
        },
        'D',
        "m. 26'ya göre 27, 28, 29 ve 30. maddelerde sözü geçen tasarrufların **vukuu tarihinden beş yıl** geçtikten sonra bu maddelere dayanılarak dava açılamaz. İptal davaları genel mahkemelerde açılır ve diğer işlere öncelikle görülür (m. 24).",
        '6183 sayılı Kanun m. 26',
    ),
    # düzey 3
    '0047': patch(
        "Mal bildiriminde bulunmayan bir amme borçlusunun, ödeme süresinin başlamasından sonra yaptığı aşağıdaki işlemlerden hangileri 6183 sayılı Kanun'un 29. maddesine göre hükümsüzdür?\n\nI. Vadesi gelmemiş bir borcunu ödemesi\n\nII. Borcuna karşılık alacaklısına mal vermesi\n\nIII. Vadesi gelmiş borcunu nakden ödemesi\n\nIV. Önceden taahhüt etmediği hâlde mevcut bir borç için rehin vermesi",
        {
            'A': 'I, II ve IV',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, III ve IV',
            'E': 'I, II, III ve IV',
        },
        'A',
        "m. 29'a göre bu durumdaki borçluların ödeme süresinin başladığı tarihten geriye doğru iki yıl içinde veya sonrasında yaptıkları; önceden taahhüt edilmemiş olup mevcut bir borcu teminat altına almak için verilen **rehinler** (IV), borca karşılık **para veya mutat ödeme araçları dışında** yapılan ödemeler (II) ve **vadesi gelmemiş** borç için yapılan ödemeler (I) hükümsüzdür. Muaccel borcun nakden ödenmesi (III) hükümsüz sayılmaz.",
        '6183 sayılı Kanun m. 29',
    ),
    # düzey 2
    '0048': patch(
        'Limited şirket ortağı, sermaye payını üçüncü bir kişiye devretmiştir. Devirden önceki döneme ait şirket amme alacaklarından kim sorumludur?',
        {
            'A': 'Payı devreden ve devralan müteselsilen',
            'B': 'Devreden ortak',
            'C': 'Şirketin müdürü',
            'D': 'Devralan ortak',
            'E': 'Diğer ortaklar paylarına göre',
        },
        'A',
        "5766 sayılı Kanunla eklenen m. 35/2'ye göre ortağın şirketteki sermaye payını devretmesi hâlinde, **payı devreden ve devralan** şahıslar devir öncesine ait amme alacaklarının ödenmesinden birinci fıkraya göre **müteselsilen** sorumlu tutulur.",
        '6183 sayılı Kanun m. 35/2',
    ),
    # düzey 1
    '0049': patch(
        "Özel kanununda ödeme zamanı belirlenmemiş bir amme alacağı, 6183 sayılı Kanun'a göre tebliğden itibaren ne kadar süre içinde ödenir?",
        {
            'A': 'Yedi gün',
            'B': 'İki ay',
            'C': 'Üç ay',
            'D': 'Bir ay',
            'E': 'On beş gün',
        },
        'D',
        "m. 37'ye göre amme alacakları özel kanunlarında belirtilen zamanlarda ödenir; özel kanununda ödeme zamanı tespit edilmemiş amme alacakları yapılacak **tebliğden itibaren bir ay** içinde ödenir. Bu sürenin son günü alacağın vade günüdür.",
        '6183 sayılı Kanun m. 37',
    ),
    # düzey 2
    '0050': patch(
        "6183 sayılı Kanun'a göre amme alacaklarının ödenmesine ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Özel kanunda ödeme yeri yoksa borçlunun ikametgâhındaki tahsil dairesine ödenir',
            'B': 'Başka tahsil dairesine yapılan ödeme tahsildara da yapılabilir',
            'C': 'Makbuzlar zamanaşımı süresi sonuna kadar saklanır',
            'D': 'Makbuz karşılığı yapılmayan ödeme alacağa mahsup edilmez',
            'E': 'Borçlu borcunu vadesinden önce ödeyebilir',
        },
        'B',
        "m. 39'a göre özel kanununda ödeme yeri gösterilmemiş alacaklar borçlunun ikametgâhının bulunduğu tahsil dairesine ödenir; alacaklı dairedeki hesap bildirilerek diğer tahsil dairelerine de ödeme yapılabilir, ancak **bu ödemeler tahsildarlara yapılamaz**. m. 40'a göre makbuz karşılığı yapılmayan ödemeler mahsup edilmez ve makbuzlar zamanaşımı sonuna kadar saklanır; m. 37'ye göre vadeden önce ödeme mümkündür.",
        '6183 sayılı Kanun m. 39-40',
    ),
    # düzey 3
    '0051': patch(
        "Birden fazla amme borcu bulunan bir borçlu, hangi borca mahsup edileceğini belirtmeden rızaen ödeme yapmıştır. Bu ödeme 6183 sayılı Kanun'a göre ilk olarak hangi alacağa mahsup edilir?",
        {
            'A': 'Vadesi en eski olan alacağa',
            'B': 'Borçlunun seçtiği alacağa',
            'C': 'Tutarı en yüksek olan alacağa',
            'D': 'Teminatı en fazla olan alacağa',
            'E': 'Ödeme süresi başlamış, vadesi geçmemiş alacağa',
        },
        'E',
        "m. 47'ye göre rızaen yapılan ödemeler sırasıyla: **ödeme süresi başlamış henüz vadesi geçmemiş**, içinde bulunulan yıl sonunda zamanaşımına uğrayacak, aynı tarihte zamanaşımına uğrayacaklarda orantılı olarak, vadesi önce gelen ve teminatsız veya az teminatlı olan alacaklara mahsup edilir.",
        '6183 sayılı Kanun m. 47',
    ),
    # düzey 3
    '0052': patch(
        "100.000 ₺ tutarındaki vergi aslı vadesinden itibaren iki buçuk ay gecikmeyle ödenmiştir. Gecikme zammı oranının Cumhurbaşkanı Kararıyla her ay için %3,7 uygulandığı varsayımıyla hesaplanacak gecikme zammı kaç ₺'dir?",
        {
            'A': '11.100',
            'B': '9.250',
            'C': '10.000',
            'D': '7.400',
            'E': '3.700',
        },
        'B',
        "m. 51'e göre ödeme süresi içinde ödenmeyen kısma vadenin bitiminden itibaren **her ay için ayrı ayrı** gecikme zammı uygulanır; ay kesirleri günlük hesaplanır. 100.000 × %3,7 × 2,5 = **9.250 ₺**. 10.000 ₺, kanun metnindeki %4 oranının uygulanmasıyla bulunur; oran 10556 sayılı Cumhurbaşkanı Kararıyla %3,7'ye indirilmiştir.",
        '6183 sayılı Kanun m. 51',
    ),
    # düzey 2
    '0053': patch(
        'Gecikme zammına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi ziyaı cezalarına madde oranında uygulanır',
            'B': 'Gecikme zammının önceden bildirilmesi gerekmez',
            'C': 'Usulsüzlük cezalarına gecikme zammı uygulanır',
            'D': 'Aslın ödenmesi gecikme zammının takibine engel değildir',
            'E': 'Mahkemece verilen ceza nitelikli alacaklara yarı oranda uygulanır',
        },
        'C',
        "m. 51'e göre gecikme zammı VUK'a göre uygulanan **vergi ziyaı cezalarında** madde oranında, mahkemelerce verilen ceza mahiyetindeki alacaklarda bu oranın yarısı ölçüsünde uygulanır; **bunların dışındaki ceza mahiyetindeki alacaklara gecikme zammı uygulanmaz**. m. 52'ye göre gecikme zammının önceden bildirilmesi gerekmez ve aslın ödenmesi gecikme zammının takip ve tahsiline engel değildir.",
        '6183 sayılı Kanun m. 51-52',
    ),
    # düzey 2
    '0054': patch(
        'Mal bildiriminde bulunmayan borçlunun hapisle tazyikine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tazyik kararını vergi dairesi müdürü verir',
            'B': 'Tazyik bir defaya mahsustur',
            'C': 'Tazyik kararları her türlü harç ve resimden muaftır',
            'D': 'Tazyik süresi üç ayı geçemez',
            'E': 'Karar Cumhuriyet savcılığınca derhal infaz edilir',
        },
        'A',
        "m. 60'a göre ödeme emrinin tebliğini ve 15 günlük sürenin bitmesini müteakip **tahsil dairesinin yazılı talebi üzerine icra tetkik mercii hâkimi** hapisle tazyik kararı verir. Tazyik mal bildiriminde bulununcaya kadar **bir defaya mahsus** ve **üç ayı geçmemek** üzere uygulanır; kararlar savcılıkça derhal infaz edilir ve her türlü harç ve resimden muaftır.",
        '6183 sayılı Kanun m. 60',
    ),
    # düzey 3
    '0055': patch(
        'Haciz sırasında borçlunun elinde bulunan bir makine için üçüncü bir kişi mülkiyet iddiasında bulunmuştur. Tahsil dairesi haciz zaptını aldığı tarihten itibaren 7 gün içinde bu iddiayı reddetmemiştir. Sonuç nedir?',
        {
            'A': 'Üçüncü kişi dava açmakla yükümlü olur',
            'B': 'Makine satılır, bedeli bankaya yatırılır',
            'C': 'Haciz kalkar ve takip durur',
            'D': 'İstihkak iddiası kabul edilmiş sayılır',
            'E': 'İddia reddedilmiş sayılır',
        },
        'D',
        "m. 66'ya göre borçlunun elindeki mala üçüncü şahıs mülkiyet veya rehin iddia ederse, tahsil dairesi **haciz zaptını aldığı tarihten itibaren 7 gün içinde iddiayı reddetmezse istihkak iddiasını kabul etmiş sayılır**. İddia reddedilirse üçüncü şahsa 7 gün içinde mahkemeye başvurması gerektiği bildirilir.",
        '6183 sayılı Kanun m. 66',
    ),
    # düzey 2
    '0056': patch(
        "Aşağıdakilerden hangileri 6183 sayılı Kanun'a göre haczedilemez?\n\nI. Harcırah Kanunu'na göre yapılan ödemeler\n\nII. Borçlunun bankadaki vadeli mevduatı\n\nIII. Borçlunun kiracısından olan kira alacağı",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'C',
        "m. 70/12'ye göre **Harcırah Kanunu'na göre yapılan ödemeler** (I) haczedilemez. Borçlunun banka mevduatı (II) ve kira alacağı (III) ise m. 79'a göre üçüncü şahıslara haciz bildirisi tebliğ edilerek haczedilebilir.",
        '6183 sayılı Kanun m. 70',
    ),
    # düzey 3
    '0057': patch(
        'Üçüncü şahıslardaki alacakların haczine (6183 sayılı Kanun m. 79) ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Menfi tespit davasında haksız çıkana %10 inkâr tazminatı uygulanır',
            'B': 'Haciz bildirisine yedi gün içinde itiraz edilir',
            'C': 'Bankalara haciz bildirisi genel müdürlüğe de tebliğ edilebilir',
            'D': 'Süresinde itiraz etmeyen üçüncü şahıs sonradan dava açamaz',
            'E': 'Süresinde itiraz edilmezse mal elinde ve borç zimmetinde sayılır',
        },
        'D',
        "m. 79'a göre haciz bildirisi tebliğ edilen üçüncü şahıs yedi gün içinde itiraz etmezse mal elinde ve borç zimmetinde sayılır. Ancak itiraz süresini geçiren üçüncü şahıs, haciz bildirisinin tebliğinden itibaren **bir yıl içinde genel mahkemelerde menfi tespit davası açabilir**; davada haksız çıkarsa haksız çıktığı tutarın %10'u tutarında inkâr tazminatı ödenir.",
        '6183 sayılı Kanun m. 79',
    ),
    # düzey 2
    '0058': patch(
        "Rayiç değeri 2.000.000 ₺ biçilen bir gayrimenkulün açık artırmasına katılmak isteyenden alınacak teminat kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '1.500.000',
            'C': '150.000',
            'D': '40.000',
            'E': '100.000',
        },
        'C',
        "m. 94'e göre artırmaya katılacaklardan gayrimenkule biçilen rayiç değerin **%7,5'i** oranında m. 10'un 1-4. bentlerinde yazılı türden teminat alınır: 2.000.000 × %7,5 = **150.000 ₺**. Menkul mal artırmalarında ise m. 85'e göre biçilen değerin %5'i oranında para teminat alınır.",
        '6183 sayılı Kanun m. 94',
    ),
    # düzey 3
    '0059': patch(
        "Vadesi 15 Mart 2021 olan bir vergi borcu için hiçbir kesme veya durma sebebi gerçekleşmemiştir. Bu alacak 6183 sayılı Kanun'a göre hangi tarihin sonunda zamanaşımına uğrar?",
        {
            'A': '31 Aralık 2027',
            'B': '31 Aralık 2026',
            'C': '15 Mart 2026',
            'D': '15 Mart 2031',
            'E': '31 Aralık 2025',
        },
        'B',
        "m. 102'ye göre amme alacağı, **vadesinin rastladığı takvim yılını takip eden takvim yılı başından itibaren 5 yıl** içinde tahsil edilmezse zamanaşımına uğrar. Vade 2021'de olduğundan süre 1/1/2022'de başlar ve **31/12/2026**'da dolar. Zamanaşımından sonra rızaen yapılan ödemeler kabul olunur.",
        '6183 sayılı Kanun m. 102',
    ),
    # düzey 2
    '0060': patch(
        "6183 sayılı Kanun'a göre doğal afet nedeniyle terkinden yararlanabilmek için borçlunun afet sebebiyle varlık ve mahsullerinin en az ne kadarını kaybetmiş olması gerekir?",
        {
            'A': 'Üçte birini',
            'B': 'Yarısını',
            'C': 'Dörtte birini',
            'D': 'Üçte ikisini',
            'E': 'Tamamını',
        },
        'A',
        "m. 105'e göre yangın, deprem, sel, kuraklık gibi afetler yüzünden **varlıklarının ve mahsullerinin en az üçte birini** kaybedenler adına tahakkuk ettirilmiş ve afetin zarar verdiği gelir kaynaklarıyla ilgili amme alacakları Cumhurbaşkanı kararıyla kısmen veya tamamen terkin edilir. Başvuru afetten itibaren **6 ay** içinde yazılı yapılır.",
        '6183 sayılı Kanun m. 105',
    ),
}

PATCHES = {ONEK + k: v for k, v in _PATCHES.items()}


def apply_or_check(path, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    fark = []
    for qid, alanlar in PATCHES.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadi: {path}::{qid}")
        for alan, beklenen in alanlar.items():
            if q.get(alan) != beklenen:
                fark.append(f"{path}::{qid}.{alan}")
                if write:
                    q[alan] = beklenen
        if write:
            if len(set(q["options"].values())) != 5:
                raise SystemExit(f"Secenek cakismasi: {path}::{qid}")
            if q["answer"] not in q["options"]:
                raise SystemExit(f"Cevap secenekte yok: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return fark


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    fark = []
    for path in (ROOT / RELATIVE_PATH, APP_ROOT / RELATIVE_PATH):
        fark.extend(apply_or_check(path, args.write))
    if args.check and fark:
        print("Eslesmeyen alanlar:")
        for f in fark[:20]:
            print(f"- {f}")
        return 1
    print(f"1 paket / {len(PATCHES)} soru ('Amme Alacaklarinin Tahsil Usulu' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
