#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vergi Hukuku Temel Kavramlar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim: Anayasa (m. 73, 90, 153, 161, 167) ve kaynaklar, ozelge-sirkuler (VUK 369, 413), yorum ve ispat, mukellef-sorumlu-ehliyet-temsilci-mirasci (VUK 8-12, 7103 m. 10/5-6), mucbir sebep ve sureler (VUK 13-18, 7537 m. 15/3), vergiyi doguran olay, mahremiyet, vergi turleri ve tarifeler. 11 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Anayasa ve 213 sayili VUK guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/vergi_hukuku_temel_kavramlar.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "vh-kavram-gen-"


def patch(stem, options, answer, solution, ref='213 sayili Vergi Usul Kanunu ve Anayasa'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Anayasa'nın 73. maddesine göre, kanunun belirttiği yukarı ve aşağı sınırlar içinde kalmak şartıyla aşağıdakilerden hangilerinde değişiklik yapma yetkisi Cumhurbaşkanına verilebilir?\n\nI. İstisna tutarları\n\nII. Vergi oranları\n\nIII. Yeni bir verginin konulması",
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'B',
        "Anayasa m. 73/4'e göre vergi, resim, harç ve benzeri mali yükümlülüklerin **muaflık, istisnalar ve indirimleriyle oranlarına** ilişkin hükümlerinde kanunun belirttiği sınırlar içinde değişiklik yapma yetkisi Cumhurbaşkanına verilebilir. m. 73/3'e göre vergi ise **kanunla konulur, değiştirilir veya kaldırılır**; yeni vergi koyma yetkisi devredilemez.",
        'Anayasa m. 73',
    ),
    # düzey 3
    '0002': patch(
        "Anayasa'nın 167. maddesine göre dış ticaretin ülke ekonomisinin yararına düzenlenmesi amacıyla kanunla Cumhurbaşkanına hangi yetki verilebilir?",
        {
            'A': 'Vergi dışındaki ek mali yükümlülükleri koyma ve kaldırma',
            'B': 'Dış ticaret işlemlerini vergi dışı bırakma',
            'C': 'KDV oranını sınırsız belirleme',
            'D': 'İthalat ve ihracat üzerine kanun olmaksızın yeni gümrük vergisi koyma',
            'E': 'Gümrük vergisini kanun olmaksızın kaldırma',
        },
        'A',
        "Anayasa m. 167/2'ye göre ithalat, ihracat ve diğer dış ticaret işlemleri üzerine **vergi ve benzeri yükümlülükler dışında ek mali yükümlülükler** koymaya ve bunları kaldırmaya kanunla Cumhurbaşkanına yetki verilebilir. Vergi koyma ise m. 73/3 uyarınca kanunla yapılır.",
        'Anayasa m. 167/2',
    ),
    # düzey 2
    '0003': patch(
        'Aşağıdakilerden hangileri vergi hukukunun bağlayıcı nitelikteki yazılı kaynaklarındandır?\n\nI. Usulüne göre yürürlüğe konulmuş vergi anlaşması\n\nII. Kanunun verdiği yetkiyle çıkarılan Cumhurbaşkanı kararı\n\nIII. Bir mükellefe verilen özelge\n\nIV. Vergi kanunu',
        {
            'A': 'II ve III',
            'B': 'I ve IV',
            'C': 'I, II ve IV',
            'D': 'I, II, III ve IV',
            'E': 'I, III ve IV',
        },
        'C',
        'Vergi hukukunun bağlayıcı yazılı kaynakları Anayasa, **kanun hükmündeki uluslararası anlaşmalar** (I), **vergi kanunları** (IV) ve kanunun verdiği yetkiye dayanan **Cumhurbaşkanı kararları** (II) ile yönetmeliklerdir. **Özelge** (III) ise idarenin mükellefin sorusuna verdiği yazılı görüştür; mükellefi ve yargıyı bağlamaz, ancak ona uyan mükellefe VUK m. 369 uyarınca ceza kesilmez.',
        'Anayasa m. 73, 90; kaynaklar',
    ),
    # düzey 2
    '0004': patch(
        "Lafzı açık olmayan bir vergi kanunu hükmünün uygulanmasında VUK'un 3. maddesinde sayılan ölçütlerden biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Hükmün diğer maddelerle bağlantısı',
            'B': 'Hükmün kanunun yapısındaki yeri',
            'C': 'Hükmün konuluşundaki maksat (kanun koyucunun amacı)',
            'D': 'Şüphe hâlinde mükellef lehine yorum',
            'E': 'Kanunun lafzı ve ruhu',
        },
        'D',
        "VUK m. 3/A'ya göre vergi kanunları **lafzı ve ruhu** ile hüküm ifade eder. Lafzın açık olmadığı hâllerde hükümler **konuluşundaki maksat**, **kanunun yapısındaki yeri** ve **diğer maddelerle olan bağlantısı** gözönünde tutularak uygulanır. 'Şüphede mükellef lehine' yorum VUK'ta sayılan bir ölçüt değildir.",
        '213 sayılı VUK m. 3/A',
    ),
    # düzey 3
    '0005': patch(
        "Vergi incelemesinde, bir mükellefin piyasa değeri yaklaşık 1.000.000 ₺ olan bir iş makinesini tanıdığı birine 100.000 ₺'ye sattığını beyan ettiği görülmüştür. Mükellef bedelin gerçekten bu olduğunu ileri sürmektedir. İspat yükü kime aittir?",
        {
            'A': 'Vergi idaresine',
            'B': 'Değeri belirleyecek olan takdir komisyonuna',
            'C': 'Vergi mahkemesine',
            'D': 'Makineyi satın alan kişiye',
            'E': 'Olağan dışı durumu iddia eden mükellefe',
        },
        'E',
        "VUK m. 3/B'ye göre vergilendirmede olayın gerçek mahiyeti esastır ve **iktisadi, ticari ve teknik icaplara uymayan veya olayın özelliğine göre normal ve mutat olmayan bir durumun iddia olunması hâlinde ispat külfeti bunu iddia eden tarafa** aittir. Piyasa değerinin onda birine satış olağan dışı olduğundan ispat mükellefe düşer.",
        '213 sayılı VUK m. 3/B',
    ),
    # düzey 2
    '0006': patch(
        'Bir işyeri kira sözleşmesinde, emlak vergisinin kiracı tarafından ödeneceği kararlaştırılmıştır. Vergi süresinde ödenmemiştir. Vergi dairesi vergiyi kimden aramalıdır?',
        {
            'A': 'Mükellef olan mal sahibinden',
            'B': 'Sözleşmeyi onaylayan noterden',
            'C': 'Sözleşme gereği kiracıdan',
            'D': 'Kiracı ile mal sahibinden yarı yarıya',
            'E': 'Kiracının kefilinden',
        },
        'A',
        "VUK m. 8/3'e göre vergi kanunlarıyla kabul edilen hâller dışında **mükellefiyete veya vergi sorumluluğuna ilişkin özel sözleşmeler vergi dairelerini bağlamaz**. Emlak vergisinin mükellefi bina sahibidir; kiracıyla yapılan anlaşma yalnız taraflar arasında hüküm doğurur.",
        '213 sayılı VUK m. 8',
    ),
    # düzey 2
    '0007': patch(
        'Kanunen yasak olan ruhsatsız bir faaliyetten kazanç elde eden kişinin vergisel durumu nedir?',
        {
            'A': 'Önce ruhsat alması şartıyla vergilenir',
            'B': 'Faaliyet yasak olduğu için vergi doğmaz',
            'C': 'Kazanç vergilenmez; faaliyet için ayrıca idari para cezası uygulanır',
            'D': 'Mükellefiyeti doğar; faaliyetin yasak olması engel değildir',
            'E': 'Kazanç müsadere edildiği için vergilenmez',
        },
        'D',
        "VUK m. 9/2'ye göre **vergiyi doğuran olayın kanunlarla yasak edilmiş bulunması mükellefiyeti ve vergi sorumluluğunu kaldırmaz**. Yasak faaliyetin başka kanunlardaki yaptırımları vergilendirmeye engel değildir.",
        '213 sayılı VUK m. 9/2',
    ),
    # düzey 3
    '0008': patch(
        "Tasfiye edilerek sicilden silinen bir limited şirket hakkında tasfiye öncesi döneme ait 400.000 ₺ vergi tarh edilmiştir. Şirket sermayesinin %25'ine sahip ortağın bu alacaktan sorumlu olduğu tutar kaç ₺'dir?",
        {
            'A': '400.000',
            'B': '100.000',
            'C': '200.000',
            'D': '0',
            'E': '80.000',
        },
        'B',
        "VUK m. 10/5'e göre **limited şirket ortakları**, tasfiye öncesi dönemlerle ilgili doğacak amme alacaklarından **şirkete koydukları sermaye hisseleri oranında** sorumludur: 400.000 × %25 = **100.000 ₺**.",
        '213 sayılı VUK m. 10/5',
    ),
    # düzey 2
    '0009': patch(
        "Bir mükellef, beyanname verme süresinin son haftasında ağır bir trafik kazası geçirerek iki ay hastanede kalmıştır. VUK'a göre bu durumun sonucu aşağıdakilerden hangisidir?",
        {
            'A': 'Süre işlemeye devam eder; geç verilen beyan için usulsüzlük cezası kesilir',
            'B': "Beyanname vergi dairesince re'sen düzenlenir",
            'C': 'Süre bir yıl uzar',
            'D': 'Beyan yükümlülüğü ortadan kalkar',
            'E': 'Mücbir sebep sürdükçe süre işlemez; durumun tevsiki gerekir',
        },
        'E',
        "VUK m. 15/1'e göre m. 13'teki mücbir sebeplerden biri bulunduğunda **bu sebep ortadan kalkıncaya kadar süreler işlemez** ve tarh zamanaşımı işlemeyen süreler kadar uzar. Bunun için mücbir sebebin malum olması veya **ilgililer tarafından ispat ya da tevsik edilmesi** gerekir.",
        '213 sayılı VUK m. 15/1',
    ),
    # düzey 3
    '0010': patch(
        "Hazine ve Maliye Bakanlığı, 6 Şubat 2026'da meydana gelen bir deprem nedeniyle bir il için mücbir sebep hâli ilan etmiştir. Ek bir belirleme yapılmazsa mücbir sebep hangi tarihte bitmiş sayılır ve Bakanlık bu süreyi en fazla hangi tarihe kadar uzatabilir?",
        {
            'A': '6 Mayıs 2026; 6 Şubat 2027',
            'B': '30 Nisan 2026; 31 Aralık 2026',
            'C': '31 Mayıs 2026; 31 Ağustos 2027',
            'D': '6 Ağustos 2026; 6 Ağustos 2027',
            'E': '31 Temmuz 2026; 28 Şubat 2027',
        },
        'C',
        "7537 sayılı Kanunla değişen m. 15/3'e göre mücbir sebep ilan edilen yerlerde mücbir sebep, **vukua geldiği tarihin rastladığı ayı izleyen üçüncü ayın son günü** itibarıyla bitmiş sayılır: Şubat'ı izleyen üçüncü ay Mayıs'tır, **31 Mayıs 2026**. Bakanlık bu süreyi **vukua gelme ayını izleyen on sekizinci ayın sonunu** geçmemek kaydıyla uzatabilir: **31 Ağustos 2027**.",
        '213 sayılı VUK m. 15/3 (7537 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0011': patch(
        "VUK'un 17. maddesine göre mühlet verilebilmesi için aşağıdakilerden hangisi aranmaz?",
        {
            'A': 'Teminat gösterilmesi',
            'B': 'Verginin alınmasının tehlikeye girmemesi',
            'C': 'Mazeretin kabule değer görülmesi',
            'D': 'Mükellefin zor durumda bulunması',
            'E': 'Sürenin bitmesinden önce yazılı istem',
        },
        'A',
        "VUK m. 17'ye göre mühlet, zor durumda bulunan mükellefe; **sürenin bitmesinden önce yazıyla istemde bulunması**, **mazeretin kabule layık görülmesi** ve **verginin alınmasının tehlikeye girmemesi** şartlarıyla verilebilir. Teminat şartı öngörülmemiştir; Bakanlık yetkisini yazılı başvuru aramaksızın da kullanabilir.",
        '213 sayılı VUK m. 17',
    ),
    # düzey 3
    '0012': patch(
        "10 Mart 2026'da tebliğ edilen bir ihbarnameye karşı 30 günlük dava açma süresi vardır. Bu süre hangi gün biter? (Aradaki günlerde süreyi etkileyen tatil yoktur.)",
        {
            'A': '31 Mart 2026',
            'B': '9 Nisan 2026',
            'C': '11 Nisan 2026',
            'D': '8 Nisan 2026',
            'E': '10 Nisan 2026',
        },
        'B',
        "VUK m. 18/1'e göre süre gün olarak belirlenmişse **başladığı gün hesaba katılmaz** ve son günün tatil saatinde biter. Sayım 11 Mart'tan başlar: Mart'ta 21 gün, Nisan'da 9 gün; otuzuncu gün **9 Nisan 2026**'dır (Perşembe).",
        '213 sayılı VUK m. 18/1',
    ),
    # düzey 3
    '0013': patch(
        "Aşağıdakilerden hangisinde vergi alacağı bir olayın vukuundan çok bir 'hukuki durumun tekemmülü' ile doğar?",
        {
            'A': 'Emlak vergisinde bina maliki olunması',
            'B': 'Damga vergisinde kâğıdın imzalanması',
            'C': 'Harçta işlemin yapılması',
            'D': "KDV'de malın teslim edilmesi",
            'E': 'Gelir vergisi stopajında ödemenin yapılması',
        },
        'A',
        "VUK m. 19'a göre vergi alacağı, vergi kanunlarının vergiyi bağladıkları **olayın vukuu veya hukuki durumun tekemmülü** ile doğar. Teslim, imza, işlem ve ödeme birer olaydır. Emlak vergisinde ise vergi, bina veya araziye **malik olma** gibi süregelen bir hukuki duruma bağlanır.",
        '213 sayılı VUK m. 19',
    ),
    # düzey 2
    '0014': patch(
        "Bir vergi müfettişi, beş yıl önce boşandığı eşine ait işletmenin vergi incelemesiyle görevlendirilmiştir. VUK'a göre bu durumda aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Takdir işlemini yapamaz, incelemeyi yapabilir',
            'B': 'Boşanma gerçekleştiği için incelemeyi yapabilir',
            'C': 'Mükellef yazılı onay verirse ve grup başkanı uygun görürse yapabilir',
            'D': 'İncelemeyi yapamaz; yasak boşanmış eşi de kapsar',
            'E': 'Beş yıl geçtiği için yapabilir',
        },
        'D',
        "VUK m. 6'ya göre m. 5'te sayılanlar kendilerine, nişanlılarına ve **boşanmış olsalar bile eşlerine** ait vergi inceleme ve takdir işleriyle uğraşamaz. Yasak ayrıca belirli derecelere kadar kan ve sıhri hısımları ile temsilcisi veya vekili olunan kişileri de kapsar.",
        '213 sayılı VUK m. 6',
    ),
    # düzey 2
    '0015': patch(
        'Tam ve dar mükellefiyete ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Kanuni veya iş merkezi Türkiye'de olan kurumlar tam mükelleftir",
            'B': "Türkiye'de yerleşme ölçütü tam mükellefiyeti belirler",
            'C': 'Dar mükellefler Türkiye dışında elde ettikleri kazançlardan da vergilenir',
            'D': 'Dar mükellefiyette kaynak (mülkilik) ilkesi esastır',
            'E': 'Tam mükellefiyette dünya çapında gelir esası geçerlidir',
        },
        'C',
        "Tam mükellefiyette kişinin Türkiye'de yerleşmiş olması (kurumlarda kanuni veya iş merkezinin Türkiye'de bulunması) esas alınır ve Türkiye içinde ve dışındaki kazançların tamamı vergilenir. Dar mükellefiyette **kaynak (mülkilik) ilkesi** uygulanır; dar mükellefler **sadece Türkiye'de elde ettikleri** kazanç ve iratlar üzerinden vergilendirilir.",
        'Vergi hukuku temel kavramlar: tam ve dar mükellefiyet',
    ),
    # düzey 2
    '0016': patch(
        'Bir üretici, kendisine yüklenen vergi nedeniyle hammadde tedarikçisinden daha düşük fiyatla alım yaparak vergi yükünü tedarikçiye aktarmıştır. Bu durum hangi yansıma türüdür?',
        {
            'A': 'Geriye doğru yansıma',
            'B': 'Vergi amortismanı',
            'C': 'İleriye doğru yansıma',
            'D': 'Yanal yansıma',
            'E': 'Verginin tecili',
        },
        'A',
        'Vergi yükünün fiyatların artırılması yoluyla alıcılara aktarılması **ileriye doğru yansıma**, satın alma fiyatlarının düşürülmesi yoluyla satıcılara (tedarikçilere) aktarılması ise **geriye doğru yansımadır**.',
        'Vergi hukuku temel kavramlar: yansıma türleri',
    ),
    # düzey 2
    '0017': patch(
        "Bir vergi kanununda verginin oranı 'idarece uygun görülecek oranda' biçiminde, herhangi bir alt ve üst sınır gösterilmeden düzenlenmiştir. Bu düzenleme hangi ilkeye aykırıdır?",
        {
            'A': 'Genellik ilkesine',
            'B': 'Yıllık esasına',
            'C': 'Belirlilik ve kanunilik ilkesine',
            'D': 'Vergilemede tarafsızlık ve ekonomik etkinlik ilkesine',
            'E': 'Verginin yansıması ilkesine',
        },
        'C',
        'Anayasa m. 73 uyarınca verginin konusu, mükellefi, matrahı ve oranı gibi temel unsurlarının **kanunda belirli** olması gerekir; Cumhurbaşkanına oran değiştirme yetkisi ancak **kanunun belirttiği yukarı ve aşağı sınırlar içinde** verilebilir. Sınırsız ve belirsiz yetki belirlilik ve kanunilik ilkelerine aykırıdır.',
        'Vergi hukuku temel kavramlar: belirlilik',
    ),
    # düzey 1
    '0018': patch(
        'Kurumlar vergisinde matrahın büyüklüğüne bakılmaksızın tek oran uygulanması hangi tarife türüne örnektir?',
        {
            'A': 'Azalan oranlı tarife',
            'B': 'Düz (sabit) oranlı tarife',
            'C': 'Dilim tarifesi',
            'D': 'Artan oranlı tarife',
            'E': 'Sınıf tarifesi',
        },
        'B',
        'Matrah ne olursa olsun **aynı oranın** uygulandığı tarifeler **düz (sabit, proporsiyonel) oranlı** tarifelerdir. Gelir vergisinde ise matrah arttıkça oranın yükseldiği artan oranlı dilim tarifesi uygulanır.',
        'Vergi hukuku temel kavramlar: düz oranlı tarife',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdakilerden hangisi vergi yükümlülüğü doğurabilecek bir kaynak değildir?',
        {
            'A': 'Anayasa',
            'B': 'Usulüne göre yürürlüğe konulmuş uluslararası anlaşma',
            'C': 'Kanun',
            'D': 'Kanunun verdiği yetkiyle çıkarılan Cumhurbaşkanı kararı',
            'E': 'Örf ve âdet',
        },
        'E',
        "Anayasa m. 73/3'teki kanunilik ilkesi gereği vergi yükümlülüğü **ancak kanunla veya kanunun sınırlarını çizdiği yetkiye dayanan düzenlemelerle** doğar. **Örf ve âdet** vergi hukukunda yükümlülük doğuran bir kaynak değildir.",
        'Vergi hukuku temel kavramlar: kaynaklar',
    ),
    # düzey 1
    '0020': patch(
        "Anayasa'nın 73. maddesinde vergi ödevi 'herkes' için öngörülmüştür. Bu ifadenin anlamı aşağıdakilerden hangisidir?",
        {
            'A': 'Türk vatandaşları',
            'B': "Türkiye'de ikamet eden vatandaşlar",
            'C': 'Vatandaş olsun olmasın mali gücü olan herkes',
            'D': 'Reşit olan vatandaşlar',
            'E': "Geliri asgari ücretin üzerinde olan ve Türkiye'de ikamet edenler",
        },
        'C',
        'Anayasa m. 73/1 vergi ödevini vatandaşlarla sınırlamamış, **herkes** için öngörmüştür. Bu ifade **genellik ilkesini** yansıtır: vatandaş olsun olmasın, mali gücü olan ve vergiyi doğuran olayla ilişki kuran herkes vergi ödemekle yükümlüdür.',
        'Anayasa m. 73',
    ),
    # düzey 1
    '0021': patch(
        "Anayasa'nın 73. maddesine göre vergi ödevinin ölçüsü ve maliye politikasının sosyal amacı sırasıyla aşağıdakilerden hangisidir?",
        {
            'A': 'Gelir düzeyi; kamu borcunun azaltılması',
            'B': 'Vatandaşlık; bütçe dengesinin sağlanması',
            'C': 'Kamu hizmetinden yararlanma; enflasyonun düşürülmesi',
            'D': 'Servet; tasarrufların artırılması',
            'E': 'Mali güç; vergi yükünün adaletli ve dengeli dağılımı',
        },
        'E',
        "Anayasa m. 73/1'e göre herkes, kamu giderlerini karşılamak üzere **mali gücüne göre** vergi ödemekle yükümlüdür. m. 73/2'ye göre **vergi yükünün adaletli ve dengeli dağılımı** maliye politikasının sosyal amacıdır. Yükümlülük 'herkes'e ait olup vatandaşlıkla sınırlı değildir.",
        'Anayasa m. 73',
    ),
    # düzey 2
    '0022': patch(
        'Usulüne göre yürürlüğe konulmuş bir çifte vergilendirmeyi önleme anlaşmasının hukuki niteliği aşağıdakilerden hangisidir?',
        {
            'A': 'Tebliğ hükmündedir; idareyi bağlar, mükellefi bağlamaz',
            'B': "Kanunların üstündedir; Anayasa'ya da üstündür",
            'C': "Kanun hükmündedir; AYM'ye aykırılık iddiasıyla başvurulamaz",
            'D': 'Yönetmelik hükmündedir; idare değiştirebilir',
            'E': 'Tavsiye hükmündedir; bağlayıcı değildir',
        },
        'C',
        "Anayasa m. 90/5'e göre **usulüne göre yürürlüğe konulmuş milletlerarası andlaşmalar kanun hükmündedir** ve bunlar hakkında **Anayasa'ya aykırılık iddiasıyla Anayasa Mahkemesine başvurulamaz**. Temel hak ve özgürlüklere ilişkin andlaşmalarla kanunların çatışmasında ise andlaşma hükümleri esas alınır.",
        'Anayasa m. 90/5',
    ),
    # düzey 3
    '0023': patch(
        'Gelir İdaresi Başkanlığı, bir hükmün uygulanma tarzına ilişkin görüşünü genel tebliğde değişiklik yaparak mükellefler aleyhine değiştirmiştir. Yeni görüş hangi dönemlere uygulanır?',
        {
            'A': 'Tebliğin yayımlandığı tarihten itibaren',
            'B': 'Zamanaşımı dolmamış bütün dönemlere',
            'C': 'Önceki beş yılın işlemlerine de',
            'D': 'Mükellefin talep ettiği tarihten itibaren',
            'E': 'Değişikliğin yapıldığı yılın başından itibaren',
        },
        'A',
        "VUK m. 369/2'ye göre yetkili makamların genel tebliğ veya sirkülerde değişiklik yaparak görüş ve kanaatlerini değiştirmesi hâlinde, yeni görüşe ilişkin tebliğ veya sirküler **yayımlandığı tarihten itibaren geçerlidir ve geriye dönük uygulanamaz**. Bu hüküm yargı mercilerince iptal edilen tebliğ ve sirkülerler hakkında uygulanmaz.",
        '213 sayılı VUK m. 369/2',
    ),
    # düzey 2
    '0024': patch(
        'Özelge ve sirkülere ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mükellef tereddüt ettiği konuda yazıyla izahat isteyebilir',
            'B': 'Özelge vergi mahkemelerini de bağlar',
            'C': 'Yazılı yanlış izahata uyan mükellefe ceza kesilmez',
            'D': 'Sirküler aynı durumdaki mükelleflere yön vermek için yayımlanır',
            'E': 'Özelgeler GİB tarafından internet ortamında yayımlanır',
        },
        'B',
        "VUK m. 413'e göre mükellefler müphem ve tereddütlü gördükleri hususlarda yazıyla izahat isteyebilir; GİB bunu özelgeyle cevaplandırabileceği gibi aynı durumdaki tüm mükellefler için **sirküler** de yayımlayabilir; özelgeler internet ortamında yayımlanır. Özelge idarenin görüşüdür, **yargı mercilerini bağlamaz**. Yanlış izahata uyan mükellefe m. 369 uyarınca ceza kesilmez.",
        '213 sayılı VUK m. 413',
    ),
    # düzey 2
    '0025': patch(
        "Aşağıdakilerden hangileri VUK'a göre vergiyi doğuran olayın ispatında kullanılamaz?\n\nI. Yemin\n\nII. Bilirkişi raporu\n\nIII. Ticari defter kayıtları",
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'D',
        "VUK m. 3/B'ye göre vergiyi doğuran olay ve buna ilişkin muamelelerin gerçek mahiyeti **yemin hariç her türlü delille** ispatlanabilir (I kullanılamaz). Bilirkişi raporu ve defter kayıtları delil olabilir. Ayrıca vergiyi doğuran olayla ilgisi tabii ve açık bulunmayan şahit ifadesi ispat aracı olarak kullanılamaz.",
        '213 sayılı VUK m. 3/B',
    ),
    # düzey 2
    '0026': patch(
        'On yaşındaki bir çocuk, mirasla edindiği dairelerden kira geliri elde etmektedir. Vergi hukuku bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çocuk mükelleftir; ödevlerini kanuni temsilcisi yerine getirir',
            'B': 'Mükellef velisidir; çocuğun kira geliri velinin beyannamesinde gösterilir',
            'C': 'Fiil ehliyeti olmadığı için mükellef değildir',
            'D': 'Gelir vergiden istisna edilir',
            'E': 'Mükellefiyet reşit olunca başlar',
        },
        'A',
        "VUK m. 9'a göre **mükellefiyet ve vergi sorumluluğu için kanuni ehliyet şart değildir**; çocuk mükelleftir. m. 10'a göre küçüklerin mükellef olması hâlinde bunlara düşen ödevler **kanuni temsilcileri** tarafından yerine getirilir.",
        '213 sayılı VUK m. 9-10',
    ),
    # düzey 3
    '0027': patch(
        'Bir anonim şirketin genel müdürü ve kanuni temsilcisi, şirketin KDV beyannamelerini vermemiştir. Tarh edilen vergi şirketin malvarlığından tahsil edilememiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Temsilci cezadan sorumlu olur, vergiden sorumlu olmaz',
            'B': 'Temsilci sorumlu değildir; şirket tüzel kişidir',
            'C': 'Vergi terkin edilir',
            'D': 'Vergi ortaklardan hisseleri oranında alınır',
            'E': 'Vergi temsilcinin şahsi varlığından alınır; şirkete rücu edebilir',
        },
        'E',
        "VUK m. 10/2'ye göre kanuni temsilcilerin ödevleri yerine getirmemeleri yüzünden mükelleflerin varlığından tamamen veya kısmen alınamayan vergi ve buna bağlı alacaklar, **ödevleri yerine getirmeyenlerin varlıklarından alınır**; temsilciler ödedikleri vergiler için **asıl mükellefe rücu edebilir**.",
        '213 sayılı VUK m. 10/2',
    ),
    # düzey 3
    '0028': patch(
        'Vergi kesenlerin sorumluluğuna (VUK m. 11) ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kesinti yapılmayan işleme taraf olanlar müteselsilen sorumlu tutulabilir',
            'B': 'Vergi kesen, verginin tam kesilip ödenmesinden sorumludur',
            'C': 'Ödediği vergi için asıl mükellefe rücu edebilir',
            'D': 'Kesinti yapılmayan alımda nihai tüketici de müteselsilen sorumludur',
            'E': 'Cumhurbaşkanı sektörlere göre farklı kesinti oranları belirleyebilir',
        },
        'D',
        "VUK m. 11'e göre vergi kesmeye mecbur olanlar verginin tam kesilip ödenmesinden sorumludur ve ödedikleri vergiler için asıl mükellefe rücu edebilir. Mal ve hizmet alımında kesinti yapılmazsa işleme taraf olanlar müteselsilen sorumlu tutulabilir; ancak bu **müteselsil sorumluluk mal üreten çiftçiler ile nihai tüketiciler için söz konusu değildir**.",
        '213 sayılı VUK m. 11',
    ),
    # düzey 3
    '0029': patch(
        "Ölen bir mükellefin 320.000 ₺ vergi borcu bulunmaktadır. Mirası reddetmeyen mirasçılardan eşin miras payı 1/4, iki çocuğun her birinin payı 3/8'dir. Çocuklardan birinin bu borçtan sorumlu olduğu tutar kaç ₺'dir?",
        {
            'A': '320.000',
            'B': '80.000',
            'C': '120.000',
            'D': '160.000',
            'E': '106.667',
        },
        'C',
        "VUK m. 12'ye göre ölüm hâlinde mükellefin ödevleri mirası reddetmemiş mirasçılara geçer ve **mirasçılardan her biri ölünün vergi borçlarından miras hisseleri nispetinde** sorumludur: 320.000 × 3/8 = **120.000 ₺**. Eşit paylaştırma 106.667 ₺, borcun tamamı 320.000 ₺ bulunmasına yol açar.",
        '213 sayılı VUK m. 12',
    ),
    # düzey 2
    '0030': patch(
        'Ölüm hâlinde vergi ödevleri ve borçlarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ödevler mirası reddetmemiş mirasçılara geçer',
            'B': 'Her mirasçı miras hissesi oranında sorumludur',
            'C': 'Mirası reddeden mirasçı sorumlu değildir',
            'D': 'Özel hüküm yoksa bildirim ve beyan sürelerine üç ay eklenir',
            'E': 'Ölünün vergi cezaları da mirasçılardan alınır',
        },
        'E',
        "VUK m. 372'ye göre **ölüm hâlinde vergi cezası düşer**; mirasçılardan yalnız vergi aslı ve ferileri aranabilir. m. 12'ye göre ödevler mirası reddetmemiş mirasçılara geçer ve her mirasçı hissesi oranında sorumludur; m. 16'ya göre özel hüküm yoksa mirasçılara geçen bildirim ve beyan sürelerine üç ay eklenir.",
        '213 sayılı VUK m. 12, 16, 372',
    ),
    # düzey 2
    '0031': patch(
        'Bir mükellefin vergi kanunlarında özel süre öngörülmemiş ve 15 günlük genel süreye tabi bir bildirim ödevi, mükellefin ölümüyle mirasçılarına geçmiştir. Mirasçıların bu bildirimi yapma süresi ne kadardır?',
        {
            'A': 'Üç ay',
            'B': '15 gün',
            'C': 'Bir yıl',
            'D': '15 gün ve üç ay',
            'E': '15 gün ve bir ay',
        },
        'D',
        "VUK m. 16'ya göre vergi kanunlarında hüküm bulunmayan hâllerde, ölüm dolayısıyla mirasçılara geçen ödevlerin yerine getirilmesinde **bildirme ve beyanname verme sürelerine üç ay eklenir**.",
        '213 sayılı VUK m. 16',
    ),
    # düzey 2
    '0032': patch(
        'Kanuni süresi 20 gün olan bir bildirimi zor durumu nedeniyle süresinde yapamayacak olan mükellefe Maliye Bakanlığınca verilebilecek mühlet en fazla ne kadardır?',
        {
            'A': 'Üç ay',
            'B': 'Bir ay',
            'C': '40 gün',
            'D': '20 gün',
            'E': '15 gün',
        },
        'B',
        "VUK m. 17'ye göre mühlet **kanuni sürenin bir katını**, kanuni sürenin **bir aydan az olması hâlinde bir ayı** geçmemek üzere verilebilir. Kanuni süre 20 gün olduğundan azami mühlet **bir aydır**.",
        '213 sayılı VUK m. 17',
    ),
    # düzey 3
    '0033': patch(
        "31 Ocak 2024'te başlayan ve bir ay olarak belirlenmiş bir süre hangi gün biter?",
        {
            'A': '2 Mart 2024',
            'B': '28 Şubat 2024',
            'C': '1 Mart 2024',
            'D': '31 Mart 2024',
            'E': '29 Şubat 2024',
        },
        'E',
        "VUK m. 18/2'ye göre süre ay olarak belirlenmişse başladığı güne son ayda karşılık gelen günün tatil saatinde biter; **sürenin bittiği ayda başladığı güne karşılık gelen gün yoksa süre o ayın son günü** biter. Şubat 2024'te 31. gün olmadığından ve 2024 artık yıl olduğundan süre **29 Şubat 2024**'te biter.",
        '213 sayılı VUK m. 18/2',
    ),
    # düzey 2
    '0034': patch(
        "Aşağıdakilerden hangileri VUK'a göre vergi mahremiyetine uymakla yükümlüdür?\n\nI. Vergi mahkemesi hâkimi\n\nII. Vergi işlerinde kullanılan bilirkişi\n\nIII. Takdir komisyonu üyesi\n\nIV. Görevinden ayrılmış vergi müfettişi",
        {
            'A': 'I, II, III ve IV',
            'B': 'I, III ve IV',
            'C': 'II ve IV',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'A',
        "VUK m. 5'e göre vergi muameleleri ve incelemeleriyle uğraşan memurlar (IV), vergi mahkemeleri, bölge idare mahkemeleri ve Danıştayda görevli olanlar (I), vergi kanunlarına göre kurulan komisyonlara katılanlar (III) ve vergi işlerinde kullanılan bilirkişiler (II) mahremiyete uymakla yükümlüdür. **Yasak görevden ayrılsalar dahi devam eder**.",
        '213 sayılı VUK m. 5',
    ),
    # düzey 3
    '0035': patch(
        'İlk 100.000 ₺ için %10, 100.000-300.000 ₺ arası için %20, 300.000 ₺ üzeri için %30 oranlı bir tarife dilim esası yerine sınıf esasıyla uygulansaydı, matrahı 400.000 ₺ olan mükellefin vergisi dilim esasına göre kaç ₺ fazla olurdu?',
        {
            'A': '120.000',
            'B': '20.000',
            'C': '40.000',
            'D': '80.000',
            'E': '0',
        },
        'C',
        "Sınıf artan oranlı tarifede matrahın **tamamına** girdiği sınıfın oranı uygulanır: 400.000 × %30 = 120.000 ₺. Dilim esasına göre vergi 10.000 + 40.000 + 30.000 = 80.000 ₺'dir. Fark **40.000 ₺**'dir; sınıf tarifesi sınır geçişlerinde ani vergi sıçramasına yol açtığı için dilim esası tercih edilir.",
        'Vergi hukuku temel kavramlar: sınıf ve dilim tarifesi',
    ),
    # düzey 2
    '0036': patch(
        'Gelir vergisinde engellilik indirimi uygulanması ve artan oranlı tarife kullanılması, bu verginin hangi niteliğini gösterir?',
        {
            'A': 'Harcama üzerinden alınan ve tüketiciye yansıtılan dolaylı vergi olmasını',
            'B': 'Objektif (ayni) vergi olmasını',
            'C': 'Spesifik vergi olmasını',
            'D': 'Mükellefin kişisel durumunu dikkate alan sübjektif vergi olmasını',
            'E': 'Servet üzerinden alınmasını',
        },
        'D',
        'Mükellefin kişisel ve ailevi durumunu, mali gücünü dikkate alan vergiler **sübjektif (şahsi) vergilerdir**. Engellilik indirimi ve artan oranlı tarife gelir vergisinin bu niteliğini gösterir. Objektif vergiler ise yalnızca vergi konusunu esas alır.',
        'Vergi hukuku temel kavramlar: sübjektif vergi',
    ),
    # düzey 2
    '0037': patch(
        'Yabancı diplomatların gelir vergisinden muaf olması ile konut kira gelirinin belli tutarının gelir vergisinden istisna edilmesi arasındaki fark aşağıdakilerden hangisidir?',
        {
            'A': 'Muafiyet kişiye, istisna vergi konusuna ilişkindir',
            'B': 'Aralarında hukuki bir fark yoktur',
            'C': 'Muafiyet geçicidir, istisna süreklidir',
            'D': 'İkisi de kurumlar vergisine özgü kavramlardır',
            'E': 'Muafiyet konuya, istisna kişiye ilişkindir',
        },
        'A',
        '**Muafiyet**, vergi kanununun kapsamına giren belirli **kişilerin** vergi dışında bırakılmasıdır (diplomat muaflığı). **İstisna** ise belirli **konuların** (gelir, işlem veya değer) vergi dışında bırakılmasıdır (konut kira geliri istisnası).',
        'Vergi hukuku temel kavramlar: muafiyet ve istisna',
    ),
    # düzey 2
    '0038': patch(
        "Aşağıdakilerden hangisi Anayasa'nın 73. maddesinden doğrudan çıkarılan ilkelerden biri değildir?",
        {
            'A': 'Mali güce göre vergilendirme',
            'B': 'Vergi ödevinin herkese ait olması (genellik)',
            'C': 'Verginin en düşük maliyetle toplanması (verimlilik)',
            'D': 'Verginin kanuniliği',
            'E': 'Vergi yükünün adaletli dağılımı',
        },
        'C',
        "Anayasa m. 73; **herkesin** (genellik) **mali gücüne göre** vergi ödemesini, **vergi yükünün adaletli ve dengeli dağılımını** ve verginin **kanunla** konulmasını düzenler. Verimlilik (tahsil maliyetinin düşüklüğü) maliye biliminde bir vergilendirme ilkesi olsa da m. 73'te yer almaz.",
        'Anayasa m. 73',
    ),
    # düzey 2
    '0039': patch(
        'Danıştay İçtihatları Birleştirme Kurulu kararlarının hukuki etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Kimseyi bağlamaz, yol gösterir',
            'B': 'Davanın taraflarını bağlar, başkalarını bağlamaz',
            'C': 'Kanunları yürürlükten kaldırır',
            'D': 'Benzer konularda idareyi ve idari yargı mercilerini bağlar',
            'E': 'Maliye Bakanlığını bağlar, vergi mahkemeleri ve Danıştay dairelerini bağlamaz',
        },
        'D',
        "Danıştay Kanunu'na göre **içtihatları birleştirme kararları**, benzer konularda Danıştay dava daireleri ve idari dava daireleri kurulları ile **idare mahkemeleri ve idare için bağlayıcıdır**. Bu nedenle vergi hukukunun yargısal kaynakları arasında bağlayıcı nitelik taşır.",
        'Vergi hukuku temel kavramlar: yargısal kaynaklar',
    ),
    # düzey 1
    '0040': patch(
        'Vergilendirme sürecinin aşamaları doğru sırayla aşağıdakilerden hangisinde verilmiştir?',
        {
            'A': 'Tarh, vergiyi doğuran olay, tahakkuk, tebliğ, tahsil',
            'B': 'Tebliğ, tarh, vergiyi doğuran olay, tahsil, tahakkuk',
            'C': 'Vergiyi doğuran olay, tebliğ, tarh, tahakkuk, tahsil',
            'D': 'Vergiyi doğuran olay, tahakkuk, tarh, tahsil, tebliğ',
            'E': 'Vergiyi doğuran olay, tarh, tebliğ, tahakkuk, tahsil',
        },
        'E',
        "VUK'a göre vergi alacağı **vergiyi doğuran olayla** doğar (m. 19), vergi dairesince miktar olarak **tarh** edilir (m. 20), mükellefe yazıyla **tebliğ** edilir (m. 21), ödenmesi gereken safhaya gelince **tahakkuk** eder (m. 22) ve kanuna uygun ödenmesiyle **tahsil** edilir (m. 23).",
        '213 sayılı VUK m. 19-23',
    ),
    # düzey 3
    '0041': patch(
        'Hükümet, yeni bir vergi istisnasını yıllık merkezî yönetim bütçe kanununa eklenecek bir madde ile getirmek istemektedir. Bu yöntem Anayasa bakımından nasıl değerlendirilir?',
        {
            'A': 'İstisna bir yıl için geçerli olmak şartıyla uygundur',
            'B': "Anayasa'ya aykırıdır; bütçe kanununa bütçe dışı hüküm konulamaz",
            'C': "Anayasa'ya uygundur; bütçe kanunu da TBMM'ce kabul edilen bir kanundur",
            'D': 'Cumhurbaşkanı onaylarsa uygundur',
            'E': 'TBMM nitelikli çoğunlukla kabul ederse uygundur',
        },
        'B',
        "Anayasa m. 161/2'ye göre **bütçe kanununa, bütçe ile ilgili hükümler dışında hiçbir hüküm konulamaz**. Vergi istisnası vergi kanunlarına ilişkin maddi bir düzenleme olduğundan ayrı bir kanunla yapılmalıdır; m. 73/3 de vergilerin kanunla konulup değiştirilmesini öngörür.",
        'Anayasa m. 161',
    ),
    # düzey 2
    '0042': patch(
        'Anayasa Mahkemesi bir vergi kanunu hükmünü iptal etmiş ve iptalin yürürlüğe gireceği tarih için ayrıca karar vermemiştir. Bu iptal kararının sonuçlarına ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Hüküm kararın Resmî Gazete'de yayımlandığı tarihte yürürlükten kalkar",
            'B': 'Karar yayımından bir yıl sonra yürürlüğe girer',
            'C': 'Hüküm yürürlüğe girdiği tarihten itibaren geçersiz sayılır',
            'D': 'Hüküm, TBMM boşluğu dolduracak yeni düzenlemeyi yapıncaya kadar yürürlükte kalır',
            'E': 'Karar davanın taraflarını bağlar, idareyi bağlamaz',
        },
        'A',
        "Anayasa m. 153'e göre kanun hükümleri **iptal kararlarının Resmî Gazete'de yayımlandığı tarihte yürürlükten kalkar**; Mahkeme gerekli hâllerde yürürlük tarihini ayrıca kararlaştırabilir, bu süre bir yılı geçemez. **İptal kararları geriye yürümez** ve yasama, yürütme, yargı organlarını, idareyi, gerçek ve tüzel kişileri bağlar.",
        'Anayasa m. 153',
    ),
    # düzey 3
    '0043': patch(
        'Bir mükellef, Gelir İdaresi Başkanlığından aldığı özelgeye uyarak beyanda bulunmuş; özelgenin hatalı olduğu sonradan anlaşılmış ve eksik vergi tespit edilmiştir. Bu durumda aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi de ceza da aranmaz',
            'B': 'Ceza kesilir, gecikme faizi hesaplanmaz',
            'C': 'Vergi yarı oranda tarh edilir',
            'D': 'Vergi tarh edilir ve vergi ziyaı cezası kesilir',
            'E': 'Vergi tarh edilir; ceza kesilmez ve gecikme faizi hesaplanmaz',
        },
        'E',
        "VUK m. 369/1'e göre yetkili makamların mükellefin kendisine **yazı ile yanlış izahat vermiş olmaları** hâlinde **vergi cezası kesilmez ve gecikme faizi hesaplanmaz**. Kanunen doğması gereken vergi asıl olarak aranır; korunan yalnız mükellefin ceza ve faiz yönünden güvenidir.",
        '213 sayılı VUK m. 369/1',
    ),
    # düzey 2
    '0044': patch(
        'Vergi idaresi, kanunda açıkça vergiye tabi tutulmamış bir işlemi, vergiye tabi bir işleme benzediği gerekçesiyle vergilendirmek istemektedir. Bu uygulama hangi ilkeye aykırıdır?',
        {
            'A': 'Vergide verimlilik',
            'B': 'Vergide yıllık esası',
            'C': 'Verginin kanuniliği ve kıyas yasağı',
            'D': 'Vergide tarafsızlık',
            'E': 'Vergide yansıma',
        },
        'C',
        "Anayasa m. 73/3'teki **verginin kanuniliği** ilkesi gereği vergi yükümlülüğü ancak kanunla doğar; kanunda öngörülmeyen bir yükümlülük **kıyas** yoluyla getirilemez. Benzerlik gerekçesiyle vergilendirme bu nedenle hukuka aykırıdır.",
        'Anayasa m. 73; kanunilik',
    ),
    # düzey 2
    '0045': patch(
        'İki kardeş, gerçekte bedel karşılığında yapılan bir taşınmaz satışını tapuda bağış olarak göstermiştir. Vergilendirmede bu işlem nasıl dikkate alınır?',
        {
            'A': 'Hem satış hem bağış olarak iki kez',
            'B': 'İşlem vergi dışı bırakılır',
            'C': 'Tarafların beyanına göre bağış olarak',
            'D': 'Gerçek mahiyetine göre satış olarak',
            'E': 'Tapudaki kayda göre bağış olarak',
        },
        'D',
        "VUK m. 3/B'ye göre **vergilendirmede vergiyi doğuran olay ve buna ilişkin muamelelerin gerçek mahiyeti esastır**. Muvazaalı olarak bağış görünümü verilen satış, gerçek mahiyeti ispatlandığında satış olarak vergilendirilir.",
        '213 sayılı VUK m. 3/B',
    ),
    # düzey 2
    '0046': patch(
        "Aşağıdakilerden hangisi verginin ödenmesi bakımından vergi dairesine karşı muhatap olan 'vergi sorumlusu' değildir?",
        {
            'A': 'Kira ödemesinden stopaj yapan şirket',
            'B': 'Kira ödemesinden stopaj yapılan dükkân sahibi',
            'C': 'Serbest meslek ödemesinden kesinti yapan banka',
            'D': 'KDV tevkifatı uygulayan alıcı',
            'E': 'Ücretten gelir vergisi kesen işveren',
        },
        'B',
        "VUK m. 8'e göre **vergi sorumlusu**, verginin ödenmesi bakımından alacaklı vergi dairesine karşı muhatap olan kişidir; ödemeyi yaparken vergiyi kesen işveren, alıcı, şirket ve banka bu durumdadır. Kira geliri elde eden ve adına stopaj yapılan dükkân sahibi ise **mükelleftir**.",
        '213 sayılı VUK m. 8',
    ),
    # düzey 3
    '0047': patch(
        'Tasfiye edilerek ticaret sicilinden silinmiş şirketlere ilişkin (VUK m. 10) aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Limited şirket ortakları sermaye payları oranında sorumludur',
            'B': 'Tasfiye öncesi dönem tarhiyatı kanuni temsilcilerden biri adına yapılır',
            'C': 'Tasfiye memurlarının sorumluluğunun bir sınırı yoktur',
            'D': 'Tarhiyat muhatapları müteselsilen sorumludur',
            'E': 'Tasfiye dönemi tarhiyatı tasfiye memurlarından biri adına yapılır',
        },
        'C',
        "7103 sayılı Kanunla eklenen m. 10/5'e göre sicilden silinmiş mükelleflerin tasfiye öncesi dönemlerine ilişkin tarhiyat **kanuni temsilcilerden**, tasfiye dönemine ilişkin tarhiyat **tasfiye memurlarından** herhangi biri adına, müteselsilen sorumlu olmak üzere yapılır; limited ortaklar tasfiye öncesi dönem alacaklarından sermaye payları oranında sorumludur. **Tasfiye memurlarının sorumluluğu tasfiye sonucu dağıtılan tutarla sınırlıdır**.",
        '213 sayılı VUK m. 10/5',
    ),
    # düzey 2
    '0048': patch(
        'İki ortaktan oluşan bir adi ortaklık faaliyetini sona erdirmiştir. Sona erme öncesi döneme ilişkin vergi tarhiyatı kimin adına yapılır?',
        {
            'A': 'Tarhiyat yapılamaz',
            'B': 'Ortaklar adına paylarına göre ayrı ayrı',
            'C': 'Ortaklardan herhangi biri adına',
            'D': 'Ortaklığın son müşterisi adına',
            'E': 'Adi ortaklık adına',
        },
        'C',
        "7103 sayılı Kanunla eklenen m. 10/6'ya göre tüzel kişiliği olmayan teşekküllerin sona ermesi hâlinde, sona erme öncesi dönemlere ilişkin tarhiyat ve ceza kesme işlemleri müteselsilen sorumlu olmak üzere bunları idare edenlerden, **adi ortaklıklarda ortaklardan herhangi biri** adına yapılır.",
        '213 sayılı VUK m. 10/6',
    ),
    # düzey 2
    '0049': patch(
        "Aşağıdakilerden hangileri VUK'un 13. maddesine göre mücbir sebep sayılır?\n\nI. Ödevin yerine getirilmesine engel olacak derecede ağır hastalık\n\nII. Defterlerin sahibinin iradesi dışında elinden çıkması\n\nIII. Mali müşavirin sözleşmeyi feshetmesi\n\nIV. Kişinin iradesi dışında vuku bulan mecburi gaybubet",
        {
            'A': 'II, III ve IV',
            'B': 'I ve II',
            'C': 'I, II, III ve IV',
            'D': 'I, II ve IV',
            'E': 'I ve IV',
        },
        'D',
        "VUK m. 13'e göre ödevin yerine getirilmesine engel olacak derecede **ağır kaza, ağır hastalık ve tutukluluk** (I), yangın, deprem, su baskını gibi afetler, **kişinin iradesi dışındaki mecburi gaybubetler** (IV) ve **defter ve vesikaların sahibinin iradesi dışında elinden çıkması** (II) mücbir sebeptir. Mali müşavirin ayrılması (III) bu nitelikte değildir.",
        '213 sayılı VUK m. 13',
    ),
    # düzey 3
    '0050': patch(
        "Bir mükellef hakkındaki tarh zamanaşımı 31 Aralık 2026'da dolacaktır. Mükellef 2026 yılında toplam dört ay tutuklu kalmış ve bu durum tevsik edilmiştir. Tarh zamanaşımı hangi tarihe kadar uzar?",
        {
            'A': '30 Nisan 2027',
            'B': '31 Aralık 2027',
            'C': '31 Aralık 2026',
            'D': '31 Mart 2027',
            'E': '30 Haziran 2027',
        },
        'A',
        "VUK m. 15/1'e göre mücbir sebep hâlinde süreler işlemez ve **tarh zamanaşımı işlemeyen süreler kadar uzar**. Tutukluluk m. 13'e göre mücbir sebeptir; dört aylık süre eklenince zamanaşımı **30 Nisan 2027**'ye kadar uzar.",
        '213 sayılı VUK m. 15/1',
    ),
    # düzey 3
    '0051': patch(
        "Yıl içinde ölen bir gelir vergisi mükellefinin yıllık beyannamesinin verilme süresine VUK'un 16. maddesindeki üç aylık ek süre uygulanır mı?",
        {
            'A': 'Uygulanır; beyan süresi yedi ay olur',
            'B': 'Uygulanmaz; beyanname verilmez',
            'C': "Uygulanmaz; GVK'da ölüm hâline özgü dört aylık süre vardır",
            'D': 'Mirasçılar diledikleri süreyi seçer',
            'E': 'Uygulanır; dört aylık süreye üç ay eklenir',
        },
        'C',
        "VUK m. 16 **vergi kanunlarında hüküm bulunmayan hâllerde** uygulanır. GVK m. 92'de ölüm hâlinde beyannamenin **ölüm tarihinden itibaren dört ay içinde** verileceği özel olarak düzenlendiğinden üç aylık ek süre uygulanmaz.",
        '213 sayılı VUK m. 16; GVK m. 92',
    ),
    # düzey 2
    '0052': patch(
        'Son günü 1 Ocak 2026 (resmî tatil) olan bir beyan süresi hangi gün biter?',
        {
            'A': '1 Ocak 2026',
            'B': '15 Ocak 2026',
            'C': '5 Ocak 2026',
            'D': '31 Aralık 2025',
            'E': '2 Ocak 2026',
        },
        'E',
        "VUK m. 18/4'e göre resmî tatil günleri süreye dâhildir; ancak **sürenin son günü resmî tatile rastlarsa süre tatili takip eden ilk iş gününün tatil saatinde biter**. 1 Ocak 2026 Perşembe'dir; izleyen ilk iş günü **2 Ocak 2026 Cuma**'dır.",
        '213 sayılı VUK m. 18/4',
    ),
    # düzey 2
    '0053': patch(
        "Aşağıdakilerden hangisi VUK'un 5. maddesine göre vergi mahremiyetinin ihlali sayılmaz?",
        {
            'A': 'Sahte belge düzenleyenin meslek odasına bildirilmesi',
            'B': 'Emekli vergi memurunun eski mükellef bilgisini açıklaması',
            'C': 'Takdir komisyonu üyesinin mükellefin hesaplarını paylaşması',
            'D': 'Bilirkişinin öğrendiği bilgiyi rakip firmaya aktarması',
            'E': 'Vergi mahkemesi personelinin dosya bilgisini yayması',
        },
        'A',
        "VUK m. 5'e göre vergi işleriyle uğraşan memurlar, yargı mensupları, komisyon üyeleri ve bilirkişiler öğrendikleri sırları ifşa edemez; **yasak görevden ayrılsalar dahi devam eder**. Ancak **sahte veya yanıltıcı belge düzenledikleri veya kullandıkları vergi inceleme raporuyla tespit olunanların meslek kuruluşlarına bildirilmesi** mahremiyeti ihlal sayılmaz.",
        '213 sayılı VUK m. 5',
    ),
    # düzey 3
    '0054': patch(
        "Varsayımsal bir tarifede ilk 100.000 ₺ için %10, 100.000-300.000 ₺ arası için %20, 300.000 ₺'yi aşan kısım için %30 oran uygulanmaktadır (dilim esaslı). Matrahı 400.000 ₺ olan mükellefin vergisi ve ortalama vergi oranı nedir?",
        {
            'A': '100.000 ₺; %25',
            'B': '80.000 ₺; %20',
            'C': '60.000 ₺; %15',
            'D': '120.000 ₺; %30',
            'E': '80.000 ₺; %30',
        },
        'B',
        "Dilim artan oranlı tarifede her dilim kendi oranıyla vergilenir: 100.000 × %10 = 10.000; 200.000 × %20 = 40.000; 100.000 × %30 = 30.000; toplam **80.000 ₺**. **Ortalama oran** 80.000 / 400.000 = **%20**, son dilime uygulanan **marjinal oran** ise %30'dur. 120.000 ₺ matrahın tamamına en yüksek oranın uygulanmasıyla bulunur.",
        'Vergi hukuku temel kavramlar: artan oranlı tarife',
    ),
    # düzey 1
    '0055': patch(
        'Akaryakıtın litresi başına fiyatından bağımsız olarak sabit tutarda alınan bir vergi, matrah bakımından hangi türdedir?',
        {
            'A': 'Ad valorem (nispi) vergi',
            'B': 'Servet vergisi',
            'C': 'Sübjektif vergi',
            'D': 'Spesifik (maktu) vergi',
            'E': 'Artan oranlı vergi',
        },
        'D',
        'Matrahı malın miktarı, ağırlığı veya hacmi gibi fiziki ölçüsü olan ve **birim başına sabit tutar** olarak alınan vergiler **spesifik (maktu)** vergilerdir. Malın değeri üzerinden yüzde olarak alınan vergiler ise **ad valorem (nispi)** vergilerdir.',
        'Vergi hukuku temel kavramlar: spesifik vergi',
    ),
    # düzey 2
    '0056': patch(
        "KDV'nin kanuni mükellefi satıcı olduğu hâlde vergi yükünün fiyat yoluyla tüketiciye aktarılması hangi kavramla açıklanır?",
        {
            'A': 'Verginin tecili',
            'B': 'Verginin yansıması',
            'C': 'Vergi muafiyeti',
            'D': 'Verginin terkini',
            'E': 'Vergi kaçakçılığı',
        },
        'B',
        '**Verginin yansıması**, kanuni mükellefin vergi yükünü fiyat mekanizmasıyla başkasına aktarmasıdır. Dolaylı vergilerde kanuni mükellef ile vergi yüklenicisi (nihai tüketici) çoğunlukla farklı kişilerdir.',
        'Vergi hukuku temel kavramlar: yansıma',
    ),
    # düzey 2
    '0057': patch(
        'Bir şirket, kanunun tanıdığı bir istisnadan yararlanmak için üretimini yasal olarak serbest bölgeye taşımıştır. Bu davranış hangi kavramla nitelendirilir?',
        {
            'A': 'Vergi kaçakçılığı',
            'B': 'Vergi ziyaı',
            'C': 'Sahte belge kullanma',
            'D': 'Muvazaa',
            'E': 'Vergiden kaçınma',
        },
        'E',
        '**Vergiden kaçınma**, mükellefin kanunun izin verdiği yollarla vergi yükünü azaltmasıdır ve hukuka uygundur. **Vergi kaçakçılığı** ve vergi ziyaı ise kanuna aykırı davranışlarla vergi borcunun gizlenmesi veya azaltılmasıdır.',
        'Vergi hukuku temel kavramlar: vergiden kaçınma',
    ),
    # düzey 2
    '0058': patch(
        'Aşağıdaki eşleştirmelerden hangisi yanlıştır?',
        {
            'A': 'Pasaport alınırken ödenen bedel – Vergi',
            'B': 'Belediyenin ilan ve reklamlardan aldığı pay – Vergi',
            'C': 'Gelir üzerinden karşılıksız alınan pay – Vergi',
            'D': 'Tapuda satış işlemi için ödenen bedel – Harç',
            'E': 'Kamu yatırımının sağladığı değer artışından alınan pay – Şerefiye',
        },
        'A',
        '**Vergi** karşılıksız alınan bir kamu geliridir (gelir vergisi, ilan ve reklam vergisi). **Harç**, kişinin özel olarak yararlandığı bir kamu hizmeti karşılığında alınır; pasaport ve tapu işlemleri için ödenen bedeller harçtır. **Şerefiye** (harcamalara katılma payı) kamu yatırımının taşınmazda sağladığı değer artışı nedeniyle alınır.',
        'Vergi hukuku temel kavramlar: vergi, harç, şerefiye',
    ),
    # düzey 1
    '0059': patch(
        'Gelir İdaresi Başkanlığının, aynı durumdaki tüm mükellefler bakımından uygulamaya yön vermek ve açıklık getirmek amacıyla yayımladığı düzenleme aşağıdakilerden hangisidir?',
        {
            'A': 'Mukteza',
            'B': 'İhbarname',
            'C': 'Sirküler',
            'D': 'Genel tebliğ taslağı',
            'E': 'Özelge',
        },
        'C',
        "VUK m. 413'e göre GİB, mükellefin sorusunu **özelge** ile cevaplandırabileceği gibi, **aynı durumda olan tüm mükellefler bakımından** uygulamaya yön vermek ve açıklık getirmek üzere **sirküler** de yayımlayabilir. Mukteza, özelgenin eski adıdır.",
        '213 sayılı VUK m. 413',
    ),
    # düzey 2
    '0060': patch(
        'Mahiyeti itibarıyla tahakkuku tahsile bağlı olan bir vergide, vergilendirme aşamalarına ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bu vergilerde tarh işlemi yapılmaz, tahakkuk yapılır',
            'B': 'Verginin tahsili tahakkuku da içine alır',
            'C': 'Tahsil, tahakkuktan bir ay sonra yapılır',
            'D': 'Tahakkuk tahsilden önce ayrı bir fişle yapılır',
            'E': 'Tahakkuk tebliğden önce gerçekleşir',
        },
        'B',
        "VUK m. 24'e göre mahiyetleri itibarıyla **tahakkuku tahsile bağlı vergilerde verginin tahsili tahakkuku da içine alır**; vergi ödendiği anda tahakkuk etmiş sayılır. Diğer vergilerde ise tarh ve tebliğ edilen vergi ödenmesi gereken safhaya geldiğinde tahakkuk eder (m. 22).",
        '213 sayılı VUK m. 24',
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
    print(f"1 paket / {len(PATCHES)} soru ('Vergi Hukuku Temel Kavramlar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
