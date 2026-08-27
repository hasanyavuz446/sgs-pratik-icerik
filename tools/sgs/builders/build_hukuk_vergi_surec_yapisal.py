#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vergilendirme Sureci — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Tanim kalibindan olay + kural uygulamasina: medyan kok 101->261, olumsuz kok %3->%33, duz tanim 3->0, kor ogrenci %26.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 13, 15, 19-26, 29-31, 34, 35, 93, 94, 101, 103, 106, 112, 114, 116, 122, 126, 371, 377, 378, Ek m.1 · 6183 m. 37, 48, 54, 55, 58, 102, 105 (resmi metinden dogrulandi)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/vergilendirme_sureci.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "vh-surec-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": '213 sayili Vergi Usul Kanunu ve 6183 sayili AATUHK'},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletme 20 Aralık 2025 tarihinde bir malı teslim etmiş, faturayı 3 Ocak 2026'da düzenlemiş ve bedeli 15 Şubat 2026'da tahsil etmiştir. Vergi dairesi, vergi alacağının hangi anda doğduğunu belirlemek istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Vergi alacağı beyannamenin verildiği tarihte doğar; beyan öncesinde idarenin bir alacağından söz edilemez',
            'B': "Vergi alacağı, kanunun vergiyi bağladığı olayın gerçekleştiği 20 Aralık 2025'te doğmuştur; fatura ve tahsilat tarihleri alacağın doğum anını değiştirmez",
            'C': 'Vergi alacağı verginin tarh edildiği tarihte doğar; tarh işlemi yapılmadıkça alacak hukuken var olmaz',
            'D': "Vergi alacağı bedelin tahsil edildiği 15 Şubat 2026'da doğar; tahsil edilmemiş bir bedel üzerinden vergi alacağı doğmaz",
            'E': "Vergi alacağı faturanın düzenlendiği 3 Ocak 2026'da doğar; belge düzenlenmeden vergiyi doğuran olay hukuken tamamlanmış sayılmadığından beyan da bu tarihe göre verilir",
        },
        'B',
        '**VUK m. 19:** vergi alacağı, **vergi kanunlarının vergiyi bağladıkları olayın vukuu veya hukuki durumun tekemmülü ile doğar.** Fatura, tahsilat, beyan ve tarh sonraki aşamalardır; alacağın doğum anını belirlemezler.',
    ),
    # düzey 2
    '0002': patch(
        'Bir vergi dairesi, aynı mükellef hakkında hem beyana dayanan bir tarhiyat hem de inceleme sonucu bulunan matrah farkı üzerinden ikinci bir tarhiyat yapmış; her iki işlem için de sürecin aşamalarını ayrı ayrı işletmiştir. Buna göre vergilendirme sürecinin aşamaları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tahakkuk, verginin kanuna uygun surette ödenmesi aşamasıdır ve bu aşamayla vergi alacağı sona erer',
            'B': 'Tarh, vergi alacağının kanunlarında gösterilen matrah ve nispetler üzerinden vergi dairesince hesaplanarak miktar itibarıyla tespit edilmesidir',
            'C': 'Tahsil, verginin kanuna uygun surette ödenmesi olup vergilendirme sürecinin son aşamasını oluşturur',
            'D': 'Tahakkuk, tarh ve tebliğ edilmiş bir verginin ödenmesi gereken bir safhaya gelmesidir',
            'E': 'Tebliğ, vergilendirmeyi ilgilendiren ve hüküm ifade eden hususların yetkili makamlarca mükellefe yazı ile bildirilmesidir',
        },
        'A',
        '**VUK m. 22** tahakkuku *ödenmesi gereken safhaya gelme*, **m. 23** ise tahsili *kanuna uygun surette ödenme* olarak tanımlar. Yanlış olan şık tahakkuk ile tahsili birbirine karıştırmaktadır.',
    ),
    # düzey 2
    '0003': patch(
        'Bir mükellef yıllık gelir vergisi beyannamesini süresinde vermiş, beyannamede matrahını doğru göstermiştir. Vergi dairesi beyanname üzerine işlem yapmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Beyan üzerine önce ihbarname düzenlenir, tahakkuk ise ihbarnamenin tebliğinden sonra ayrıca gerçekleşir',
            'B': 'Beyan üzerinden alınan vergilerde tarh işlemi takdir komisyonu kararına bağlanır ve tahakkuk bu kararla oluşur',
            'C': 'Beyan üzerinden alınan vergiler tahakkuk fişi ile tarh ve tahakkuk ettirilir; tarh ve tahakkuk aynı belgeyle birlikte gerçekleşir',
            'D': 'Beyanname verilmesi tek başına tahakkuk sonucunu doğurur; ayrıca bir belge düzenlenmesine gerek bulunmaz',
            'E': 'Beyan üzerinden alınan vergilerde tahakkuk, verginin fiilen ödendiği tarihte gerçekleşir ve öncesinde tarh edilmiş sayılmaz',
        },
        'C',
        "**VUK m. 25:** vergi kanunlarına göre **beyan üzerinden alınan vergiler 'tahakkuk fişi' ile tarh ve tahakkuk ettirilir.** İhbarname usulü, **m. 34** uyarınca ikmalen ve re'sen tarh edilen vergilere özgüdür.",
    ),
    # düzey 3
    '0004': patch(
        'Bir mükellef hakkında daha önce vergi tarh edilmiş; sonradan yapılan incelemede, mükellefin kendi defter ve belgelerine dayanılarak miktarı tespit edilebilen bir matrah farkı ortaya çıkmıştır. Buna göre uygulanacak tarh usulü bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Defter ve belgelere dayanan farklarda takdir komisyonu kararı zorunludur; komisyon kararı olmadan tarhiyat yapılamaz',
            'B': 'Matrah farkı için idarece tarh usulü uygulanır; bu usul mükellefin bildirim ödevini yerine getirdiği hâllerde işletilir',
            'C': "Matrah farkı sonradan ortaya çıktığı için re'sen tarhiyat yapılır; re'sen tarh her türlü matrah farkında uygulanan genel usuldür",
            'D': 'Matrah farkı defter ve belgelere dayanılarak tespit edilebildiğinden ikmalen tarhiyat yapılır; bu usul önceden bir tarhiyatın varlığını gerektirir',
            'E': 'Önceden bir tarhiyat yapılmış olduğundan aynı vergilendirme dönemi için yeniden tarhiyat yapılamaz; ortaya çıkan fark ancak düzeltme hükümleri uyarınca giderilebilir',
        },
        'D',
        "**VUK m. 29:** ikmalen vergi tarhı, **bir vergi tarh edildikten sonra** ortaya çıkan ve **defter, kayıt ve belgelere veya kanuni ölçülere dayanılarak miktarı tespit olunan** matrah farkı üzerinden yapılır. Re'sen tarh (m. 30) ise tam da bu tespitin **yapılamadığı** hâller içindir.",
    ),
    # düzey 2
    '0005': patch(
        'Bir mükellefin defter ve belgeleri yanmış, matrahın defter, kayıt ve belgelere veya kanuni ölçülere dayanılarak tespitine imkân kalmamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Mükellefin beyanı esas alınarak tahakkuk fişi düzenlenir; belgesizlik hâlinde beyan denetlenmeksizin kabul edilir',
            'B': 'Matrah, mükellefin bir önceki yıl beyanı esas alınarak idarece tarh edilir; bu usul belgesizlik hâllerine özgüdür',
            'C': 'Defterlerin yanması mücbir sebep sayıldığından hiçbir tarhiyat yapılamaz ve vergi alacağı düşer',
            'D': 'Belgeler bulunmadığından ikmalen tarhiyat yapılır; ikmalen tarh, matrahın belgelerle tespit edilemediği belgesizlik hâllerinde başvurulan usul olduğundan burada da uygulanır',
            'E': "Matrahın belgelere dayanılarak tespiti mümkün olmadığından re'sen tarhiyat yapılır; matrah takdir komisyonunca takdir edilir veya inceleme raporunda belirtilir",
        },
        'E',
        "**VUK m. 30:** re'sen vergi tarhı, matrahın **tamamen veya kısmen defter, kayıt ve belgelere veya kanuni ölçülere dayanılarak tespitine imkân bulunmayan hâllerde**, takdir komisyonlarınca takdir edilen veya inceleme raporlarında belirtilen matrah üzerinden yapılır.",
    ),
    # düzey 2
    '0006': patch(
        "Bir mükellef hakkında önce beyanına dayanan tarhiyat yapılmış, ardından inceleme sonucu bulunan matrah farkı için ikinci bir tarhiyat gerçekleştirilmiştir. Vergi dairesi iki tarhiyat için farklı belgeler düzenlemiştir. Buna göre ikmalen ve re'sen tarhiyat ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': "İkmalen ve re'sen tarh edilen vergiler, beyana dayanan vergilerde olduğu gibi tahakkuk fişi ile mükellefe bildirilir",
            'B': "Re'sen tarhta matrah, takdir komisyonunca takdir edilebileceği gibi vergi inceleme raporunda da belirtilebilir",
            'C': "Re'sen tarhiyat, matrahın defter ve belgelere dayanılarak tespitine imkân bulunmayan hâllerde uygulanır",
            'D': 'İkmalen tarhiyat, daha önce bir vergi tarh edilmiş olmasını gerektirir',
            'E': "İkmalen ve re'sen tarh edilen vergiler ihbarname ile ilgililere tebliğ olunur",
        },
        'A',
        "**VUK m. 34:** **ikmalen ve re'sen tarh edilen vergiler 'ihbarname' ile** ilgililere tebliğ olunur. Tahakkuk fişi ise **m. 25** uyarınca beyan üzerinden alınan vergilere özgüdür.",
    ),
    # düzey 3
    '0007': patch(
        "Vergi dairesi, hakkında re'sen tarhiyat yaptığı mükellefe ihbarname düzenlemiştir. İhbarnamede verginin nev'i, mükellefin kimliği ve tarh edilen vergi tutarı yer almakta; ancak vergi mahkemesinde dava açma süresi gösterilmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': "İhbarname yerine tahakkuk fişi düzenlenmesi gerektiğinden işlem baştan sakattır; re'sen tarhiyatta ihbarname kullanılması hukuka aykırılık oluşturur",
            'B': 'İhbarnamenin içeriği kanunda düzenlenmediğinden eksiklik iddiası dinlenmez; idare ihbarnamenin biçimini serbestçe belirleyebildiğinden mükellefin bu yöndeki savunması sonuç doğurmaz',
            'C': 'İhbarnamedeki her türlü eksiklik tebliği kendiliğinden hükümsüz kılar; bu nedenle tarhiyatın baştan yeniden yapılması ve yeni ihbarname düzenlenmesi gerekir',
            'D': 'İhbarnamede bulunması gereken bilgilerin eksikliği, verginin miktarında hata bulunmadıkça tebliği hükümsüz kılmaz; ancak vergi ve ceza miktarı ile ilgili bilgilerdeki eksiklik tebliği hükümsüz kılar',
            'E': 'Dava açma süresinin gösterilmemesi tebliği hükümsüz kılar; süre gösterilmeyen ihbarnameye dayanan tarhiyat kendiliğinden ortadan kalkar ve vergi alacağı düşer',
        },
        'D',
        "**VUK m. 35** ihbarnamenin içeriğini sayar; son fıkrası, bu bilgilerdeki eksikliğin **verginin miktarı ile ilgili olanlar dışında** tebliği hükümsüz kılmayacağını düzenler. Re'sen tarhta ihbarname kullanılması ise **m. 34** gereğidir.",
    ),
    # düzey 2
    '0008': patch(
        'Vergi dairesi, adresi bilinen bir mükellefe vergi/ceza ihbarnamesini tebliğ etmek istemektedir. Buna göre tebliğ usulü bakımından aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tahakkuk fişinden gayri, hüküm ifade eden vesikalar adresi bilinen kişilere posta ile tebliğ edilir',
            'B': 'Adresi bilinen mükelleflere tebliğ yalnız mükellefin vergi dairesine bizzat gelmesiyle yapılabilir',
            'C': 'Adresi bilinmeyen hâllerde ilan yoluyla tebliğ usulüne başvurulabilir',
            'D': 'Posta yoluyla yapılan tebliğ ilmühaberli taahhütlü olarak gönderilir',
            'E': 'Tebliğ mükelleflere, kanuni temsilcilerine veya umumi vekillerine yapılabilir',
        },
        'B',
        '**VUK m. 93:** adresleri bilinen kişilere tebliğ **posta vasıtasıyla ilmühaberli taahhütlü** olarak yapılır; kanun mükellefin bizzat daireye gelmesini bir tebliğ usulü olarak öngörmez.',
    ),
    # düzey 2
    '0009': patch(
        'Bir anonim şirket adına düzenlenen vergi/ceza ihbarnamesi şirketin merkez adresine gönderilmiş; şirketin yönetim kurulunda birden çok temsilci bulunmaktadır. Vergi dairesi tebliğin kime yapılacağını belirlemek istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tüzel kişilere tebliğ doğrudan ortaklara yapılır; şirketin tüzel kişiliği tebligat bakımından dikkate alınmadığından temsilciye yapılan tebliğ hükümsüzdür',
            'B': 'Tüzel kişilere tebliğ ancak bütün yönetim kurulu üyelerine ayrı ayrı yapılırsa geçerli olur; tek kişiye yapılan tebliğ şirketi bağlamadığından dava açma süresi işlemeye başlamaz',
            'C': 'Tüzel kişilere tebliğ yalnız ticaret sicili müdürlüğü aracılığıyla yapılabilir; doğrudan şirket adresine gönderilen tebligat usulsüz sayılır',
            'D': 'Tüzel kişilere tebliğ yapılamaz; vergi alacağı doğrudan kanuni temsilcinin şahsi borcu olarak takip edildiğinden tebligat da ona şahsen yapılır',
            'E': 'Tüzel kişilere yapılacak tebliğ, bunların başkan, müdür veya kanuni temsilcilerine yapılır; bu kişilerin birden çok olması hâlinde tebliğin birine yapılması yeterlidir',
        },
        'E',
        '**VUK m. 94:** tebliğ mükelleflere, kanuni temsilcilerine, umumi vekillerine veya vergi cezası kesilenlere yapılır; **tüzel kişilere yapılacak tebliğ bunların başkan, müdür veya kanuni temsilcilerine** yapılır ve bunlar birden çoksa tebliğin birine yapılması yeterlidir.',
    ),
    # düzey 3
    '0010': patch(
        'Vergi dairesi, mükellefin bilinen adreslerine tebligat çıkarmış; ancak adres tespit edilememiş ve tebliğ yapılamamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Adresi bilinmeyen veya bilinen adreste tebliğ yapılamayan hâllerde ilan yoluyla tebliğ yoluna başvurulur; ilan tarihinden başlayarak bir ay sonunda tebliğ yapılmış sayılır',
            'B': 'Bu hâlde tebliğ zorunluluğu ortadan kalkar ve vergi doğrudan tahakkuk eder; tahakkuk için tebliğ şartı yalnız beyana dayanan vergilerde aranır',
            'C': 'Tebliğ yapılamayan hâllerde ihbarname vergi dairesinde saklanır ve mükellef gelene kadar bekletilir; bu süre içinde dava açma süresi de işlemeye başlamaz',
            'D': 'Adres tespit edilemediğinde vergilendirme işlemi kendiliğinden düşer; tebliğ edilemeyen bir ihbarnameye dayanılarak takip yapılamayacağından alacak ortadan kalkar',
            'E': 'Adres bilinmiyorsa tebliğ mükellefin en yakın akrabasına yapılır; akrabaya yapılan tebliğ mükellefe yapılmış sayıldığından süreler o tarihte başlar',
        },
        'A',
        '**VUK m. 103** ilanen tebliğ hâllerini sayar (adresin bilinmemesi, bilinen adreste tebliğ yapılamaması vb.); **m. 106** uyarınca ilanın yapıldığı tarihten başlayarak **bir ayın sonunda** tebliğ yapılmış sayılır.',
    ),
    # düzey 2
    '0011': patch(
        'Bir vergi dairesi aynı dönemde hem beyana dayanan bir tahakkuk fişi düzenlemiş hem de ikmalen tarh ettiği bir vergi için ihbarname çıkarmış; ayrıca adresi tespit edilemeyen üçüncü bir mükellef için ilan yoluna başvurmuştur. Buna göre vergi tebliği ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Adresi bilinmeyen veya bilinen adreste tebliğ yapılamayan hâllerde ilan yoluyla tebliğ yapılabilir',
            'B': 'Adresleri bilinen gerçek ve tüzel kişilere yapılacak tebliğ posta vasıtasıyla ilmühaberli taahhütlü olarak gönderilir ve tebliğ tarihi buna göre belirlenir',
            'C': 'Adresleri bilinen gerçek ve tüzel kişilere tebliğ posta vasıtasıyla ilmühaberli taahhütlü olarak yapılır',
            'D': 'Tebliğ mükelleflere, kanuni temsilcilerine, umumi vekillerine veya vergi cezası kesilenlere yapılır',
            'E': 'Beyan üzerinden alınan vergilerde düzenlenen tahakkuk fişi de posta yoluyla ilmühaberli taahhütlü olarak tebliğ edilir ve tebliğ edilmedikçe vergi tahakkuk etmez',
        },
        'E',
        "**VUK m. 93** posta yoluyla tebliğ zorunluluğunu **'tahakkuk fişinden gayri'** vesikalar için öngörür. Tahakkuk fişi bu kapsamın dışındadır; beyan üzerine düzenlenip mükellefe verilir.",
    ),
    # düzey 3
    '0012': patch(
        "Bir mükellefe ikmalen tarh edilen vergiye ilişkin ihbarname 10 Mart'ta tebliğ edilmiş; mükellef yasal süresi içinde dava açmamıştır. Buna göre verginin tahakkuku bakımından aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Vergi ihbarnamenin tebliğ edildiği anda tahakkuk etmiştir; dava açma süresinin geçmesi tahakkuk bakımından sonuç doğurmadığından 10 Mart esas alınır',
            'B': 'Dava açma süresi dava açılmaksızın geçtiğinden vergi tahakkuk etmiş, yani ödenmesi gereken safhaya gelmiştir',
            'C': 'Tahakkuk için ayrıca bir tahakkuk fişi düzenlenmesi gerekir; ihbarnameye dayanan tarhiyatlarda fiş düzenlenmedikçe vergi tahakkuk etmiş sayılmaz',
            'D': 'Vergi ancak fiilen ödendiğinde tahakkuk eder; ödeme yapılmadığı sürece tahakkuktan söz edilemeyeceğinden takip de başlatılamaz',
            'E': 'Dava açılmaması verginin kesinleşmesini engellemez ancak tahakkuku engeller; tahakkuk yalnız yargı kararıyla gerçekleşebileceğinden idare takip yapamaz',
        },
        'B',
        '**VUK m. 22:** verginin tahakkuku, **tarh ve tebliğ edilen bir verginin ödenmesi gereken bir safhaya gelmesidir.** İhbarnameye bağlı tarhiyatta bu safha, dava açma süresinin dava açılmaksızın geçmesiyle (veya davanın kesin olarak sonuçlanmasıyla) oluşur.',
    ),
    # düzey 3
    '0013': patch(
        'Vergi alacağının 2020 takvim yılında doğduğu bir olayda vergi dairesi, tarh ve tebliğ işlemini 2026 yılının Şubat ayında yapmıştır. Mükellef zamanaşımı itirazında bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': "Tarh zamanaşımı, vergi alacağının doğduğu takvim yılını izleyen yılın başından itibaren beş yıldır; süre 31 Aralık 2025'te dolduğundan tarhiyat zamanaşımına uğramıştır",
            'B': "Tarh zamanaşımı on yıl olduğundan süre henüz dolmamıştır; idarenin 2026'da yaptığı tarhiyat bu nedenle hukuka uygundur ve itiraz reddedilir",
            'C': 'Zamanaşımı süresi beyanname verilmediği hâllerde işlemez; süre ancak beyanname verilmesiyle başlayacağından 2026 tarhiyatı süresinde sayılır',
            'D': 'Zamanaşımı vergi alacağının doğduğu tarihten itibaren işlediğinden süre 2025 yılı içinde dolar; ancak tebliğ yapıldığı için süre kesilmiş sayılır ve tarhiyat geçerli olur',
            'E': 'Tarh zamanaşımı yalnız mükellef ileri sürerse dikkate alınır; itiraz edilmediği takdirde süre dolmuş olsa bile tarhiyat kesinleşeceğinden idare işlemi sürdürür',
        },
        'A',
        "**VUK m. 114/1:** vergi alacağının doğduğu takvim yılını takip eden yılın başından başlayarak **beş yıl içinde tarh ve mükellefe tebliğ edilmeyen vergiler zamanaşımına uğrar.** 2020'de doğan alacakta süre 1 Ocak 2021'de başlar, 31 Aralık 2025'te dolar.",
    ),
    # düzey 3
    '0014': patch(
        'Vadesi 2020 yılı içinde dolan bir amme alacağı, tahsil dairesince 2026 yılına kadar tahsil edilememiş ve bu süre içinde zamanaşımını kesen bir işlem yapılmamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tahsil zamanaşımı yalnız ödeme emri tebliğ edilmişse işlemeye başlar; ödeme emri çıkarılmadığından süre henüz başlamamış sayılır',
            'B': "Tahsil zamanaşımı vergi alacağının doğduğu yıldan itibaren işler; vade tarihi süre bakımından belirleyici olmadığından hesaplama 2019'dan başlatılır",
            'C': 'Amme alacaklarında zamanaşımı işlemez; kamu alacağı niteliği süreye bağlı olmadığından alacak her zaman tahsil edilebilir durumda kalır',
            'D': 'Amme alacağı, vadesinin rastladığı takvim yılını takip eden yıl başından itibaren beş yıl içinde tahsil edilmediğinden tahsil zamanaşımına uğramıştır',
            'E': 'Tahsil zamanaşımı süresi on yıl olduğundan alacak hâlâ takip edilebilir; idare bu süre içinde her zaman cebri takip başlatabileceğinden itiraz dinlenmez',
        },
        'D',
        '**6183 m. 102:** amme alacağı, **vadesinin rastladığı takvim yılını takip eden takvim yılı başından itibaren 5 yıl** içinde tahsil edilmezse zamanaşımına uğrar. Tarh zamanaşımı (VUK m. 114) ise alacağın **doğduğu** yılı izleyen yıldan işler; iki süre farklı anlarda başlar.',
    ),
    # düzey 2
    '0015': patch(
        'Bir mükellefin 2019 yılında doğan bir vergi borcu ile vadesi 2019 yılında dolan ayrı bir amme alacağı bulunmaktadır. Vergi dairesi her iki alacak bakımından da süre hesabı yapmakta, iki sürenin aynı anda dolduğunu varsaymaktadır. Buna göre vergilendirmede zamanaşımı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Vergi hukukunda zamanaşımı süreleri kanunla belirlenmiş olup taraflarca değiştirilemez',
            'B': 'Tarh zamanaşımına uğrayan bir vergi artık tarh ve tebliğ edilemez',
            'C': 'Tarh zamanaşımı ve tahsil zamanaşımı aynı anda işlemeye başlar; her ikisi de vergi alacağının doğduğu takvim yılını izleyen yılın başından itibaren hesaplanır',
            'D': 'Tahsil zamanaşımı, alacağın vadesinin rastladığı takvim yılını takip eden yıl başından itibaren beş yıldır',
            'E': 'Tarh zamanaşımı ve tahsil zamanaşımı süreleri farklı uzunluktadır; tarh zamanaşımı beş, tahsil zamanaşımı on yıl olduğundan iki alacak için ayrı ayrı hesap yapılması gerekir',
        },
        'C',
        '**VUK m. 114** tarh zamanaşımını alacağın **doğduğu** yılı, **6183 m. 102** ise tahsil zamanaşımını alacağın **vadesinin rastladığı** yılı izleyen yıl başından başlatır. İki sürenin başlangıcı farklı olduğundan aynı anda işlemeye başladıklarını söyleyen ifade yanlıştır.',
    ),
    # düzey 2
    '0016': patch(
        'Bir mükellefin vergi matrahı hesaplanırken vergi dairesince toplama hatası yapılmış ve mükelleften fazla vergi istenmiştir. Mükellef bu durumu tarh zamanaşımı süresi içinde fark etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Vergiye ilişkin hesaplarda yapılan ve haksız yere fazla vergi istenmesine yol açan bu durum vergi hatasıdır; mükellef düzeltilmesini vergi dairesinden yazı ile isteyebilir',
            'B': 'Hesaplama hataları vergi hatası sayılmadığından ancak dava yoluyla ileri sürülebilir; idareye düzeltme başvurusu yapılması hukuken sonuç doğurmaz',
            'C': 'Vergi hatası yalnız mükellefin kendi beyanındaki hatalar için söz konusu olur; idarenin işlemlerindeki hatalar bu kapsamda değerlendirilmediğinden düzeltme istenemez',
            'D': 'Düzeltme talebi ancak sözlü olarak yapılabilir; yazılı başvuru usulü kanunda öngörülmediğinden yazıyla yapılan istem işleme konulmaz',
            'E': 'Fazla istenen vergi ödendikten sonra düzeltme istenemez; ödeme işlemi hatayı ortadan kaldırdığından iade talebi de dinlenmez',
        },
        'A',
        '**VUK m. 116:** vergi hatası, **vergiye müteallik hesaplarda veya vergilendirmede yapılan hatalar** yüzünden haksız yere fazla veya eksik vergi istenmesi veya alınmasıdır. **m. 122:** mükellefler düzeltmeyi vergi dairesinden **yazı ile** isteyebilirler.',
    ),
    # düzey 3
    '0017': patch(
        "Bir vergi hatası, VUK m. 114'teki beş yıllık zamanaşımı süresi dolduktan sonra ortaya çıkarılmıştır. Mükellef düzeltme talebinde bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Vergi hataları zamanaşımına tabi değildir; hatanın ortaya çıktığı her zaman düzeltme yapılabileceğinden talebin süre yönünden reddi hukuka aykırı olur',
            'B': 'Zamanaşımı dolduktan sonra düzeltme yalnız idare lehine yapılabilir; mükellef lehine düzeltme yasak olduğundan fazla alınan vergi iade edilmez',
            'C': 'Zamanaşımı süresi dolduktan sonra meydana çıkarılan vergi hataları kural olarak düzeltilemez; kanun yalnız sınırlı hâllerde düzeltme süresini uzatmıştır',
            'D': 'Düzeltme zamanaşımı tarh zamanaşımından bağımsız olup on yıldır; bu nedenle beş yıllık sürenin dolması düzeltmeye engel oluşturmaz',
            'E': 'Zamanaşımının dolması hatayı ortadan kaldırır; hata hukuken yok sayılacağından mükellefin dava açma hakkı da bulunmaz',
        },
        'C',
        "**VUK m. 126:** m. 114'te yazılı **zamanaşımı süresi dolduktan sonra meydana çıkarılan vergi hataları düzeltilemez.** Aynı madde, ilan yoluyla tebliğ, ihbarname/ödeme emri tebliği ve haciz gibi sınırlı hâller için düzeltme süresini uzatmaktadır.",
    ),
    # düzey 2
    '0018': patch(
        'Bir mükellef, kendi beyanındaki hesap hatası nedeniyle fazla vergi ödediğini; vergi dairesi ise aynı dönemde başka bir mükelleften hesap hatası nedeniyle eksik vergi alındığını tespit etmiştir. Her iki taraf da düzeltme yoluna başvurmak istemektedir. Buna göre vergi hataları ve düzeltme ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mükellefler vergi muamelelerindeki hataların düzeltilmesini vergi dairesinden yazı ile isteyebilirler',
            'B': 'Vergi hatası yalnız mükellef aleyhine sonuç doğuran hâlleri kapsar; eksik vergi alınmasına yol açan durumlar vergi hatası sayılmaz',
            'C': 'Düzeltme talebinin reddi hâlinde mükellefin başvurabileceği hukuki yollar kanunda düzenlenmiştir',
            'D': 'Tarh zamanaşımı süresi dolduktan sonra ortaya çıkarılan vergi hataları kural olarak düzeltilemez',
            'E': 'Vergi hatası, hesaplarda veya vergilendirmede yapılan hatalar yüzünden haksız yere fazla veya eksik vergi istenmesi ya da alınmasıdır',
        },
        'B',
        '**VUK m. 116** vergi hatasını *haksız yere fazla **veya eksik** vergi istenmesi veya alınması* olarak tanımlar; hata kavramı iki yönlüdür. Yalnız mükellef aleyhine hâlleri kapsadığını söyleyen ifade yanlıştır.',
    ),
    # düzey 3
    '0019': patch(
        'Beyana dayanan bir vergide vergi ziyaına yol açan fiili işleyen mükellef, durumu kendiliğinden ve resmî bir makama bildirmeden önce vergi dairesine dilekçeyle haber vermiş; hiç verilmemiş beyannamesini haber verme tarihinden itibaren on beş gün içinde vermiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Pişmanlık hükümleri bütün vergi türleri için uygulanır; beyana dayanmayan vergilerde de aynı sonuç doğduğundan ayrım yapılmaz',
            'B': 'Pişmanlık ancak vergi incelemesine başlandıktan sonra istenebilir; inceleme başlamadan yapılan başvurular erken sayıldığından işleme konulmaz',
            'C': 'Pişmanlık hükümleri yalnız beyanname verilmiş olması hâlinde uygulanır; hiç verilmemiş beyanname için pişmanlık talebi kabul edilmeyeceğinden mükellef adına vergi ziyaı cezası kesilir',
            'D': 'Pişmanlık başvurusu vergi aslını da ortadan kaldırır; mükellef yalnız pişmanlık zammını ödeyeceğinden vergi tahsil edilmez',
            'E': 'Şartların gerçekleşmesi hâlinde pişmanlık hükümleri uygulanır ve mükellef adına vergi ziyaı cezası kesilmez; ödenmemiş vergi ile pişmanlık zammı süresinde ödenmelidir',
        },
        'E',
        '**VUK m. 371:** beyana dayanan vergilerde vergi ziyaı cezasını gerektiren fiilleri işleyen mükellefler kanunda sayılan şartlarla kendiliğinden dilekçeyle haber verirse **vergi ziyaı cezası kesilmez**; hiç verilmemiş beyannamenin haber verme tarihinden itibaren **on beş gün içinde** verilmesi şartlardandır.',
    ),
    # düzey 2
    '0020': patch(
        'Vadesinde ödenmeyen bir amme alacağı için tahsil dairesi ödeme emri düzenlemiştir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Ödeme müddeti içinde ödenmeyen amme alacağı tahsil dairesince cebren tahsil olunur',
            'B': 'Ödeme emri tebliğ edilen borçluya borcunu ödemesi için altmış günlük bir süre tanınır; bu süre dolmadan cebri takip işlemlerine başlanamayacağından haciz uygulanamaz',
            'C': 'Ödeme emrinde borcun ödenmesi veya mal bildiriminde bulunulması istenir',
            'D': 'Ödeme emri tebliğ edilen borçluya, borcunu ödemesi için otuz günlük bir süre tanınır',
            'E': 'Ödeme emrine karşı tebliğ tarihinden itibaren on beş gün içinde dava açılabilir',
        },
        'D',
        "**6183 m. 55:** ödeme emriyle borçluya **on beş gün** süre verilir; otuz günlük süre kanunda öngörülmemiştir. Cebren tahsil m. 54, dava süresi m. 58'de düzenlenmiştir.",
    ),
    # düzey 3
    '0021': patch(
        'Kendisine ödeme emri tebliğ edilen bir borçlu, böyle bir borcunun bulunmadığını ileri sürmek istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Ödeme emrine karşı her türlü iddia ileri sürülebilir; kanun dava sebeplerini sınırlamadığından matraha ilişkin itirazlar da bu aşamada incelenir',
            'B': 'Ödeme emrine karşı dava süresi otuz gündür; genel dava açma süresi uygulandığından ayrı bir süre öngörülmemiştir',
            'C': 'Ödeme emrine karşı dava açılamaz; borçlu ancak borcu ödedikten sonra iade davası açabileceğinden ödeme emri aşamasında ileri sürülecek bir hukuki yol bulunmaz',
            'D': 'Ödeme emrine itiraz yalnız tahsil dairesine yapılır; idari başvuru zorunlu olduğundan doğrudan dava açılamaz',
            'E': 'Borçlu; böyle bir borcu olmadığı, kısmen ödediği veya alacağın zamanaşımına uğradığı iddialarıyla tebliğ tarihinden itibaren on beş gün içinde dava açabilir',
        },
        'E',
        '**6183 m. 58:** kendisine ödeme emri tebliğ olunan şahıs, **böyle bir borcu olmadığı veya kısmen ödediği veya zamanaşımına uğradığı** hakkında tebliğ tarihinden itibaren **on beş gün içinde** dava açabilir. Dava sebepleri kanunla sınırlanmıştır.',
    ),
    # düzey 2
    '0022': patch(
        'Amme borcunun vadesinde ödenmesi borçluyu çok zor duruma düşürecektir. Borçlu tahsil dairesine başvurmuştur. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Amme borcunun vadesinde ödenmesi borçluyu çok zor duruma düşürse dahi tecil istenemez; kanun ödeme güçlüğünü bir erteleme sebebi saymadığından başvuru reddedilir',
            'B': 'Tecil kural olarak teminat karşılığında yapılır',
            'C': 'Tecil kararı verilmesi hâlinde amme alacağı sona erer ve borçlunun ödeme yükümlülüğü ortadan kalkar',
            'D': 'Tecil, borcun ödenme zamanını erteleyen bir işlemdir',
            'E': 'Kanunda sayılan afetler nedeniyle zarara uğrayanların borçları terkin edilebilir',
        },
        'C',
        "**6183 m. 48** tecili ödemenin **ertelenmesi** olarak düzenler; alacak varlığını sürdürür. Alacağı gerçekten sona erdiren işlem **m. 105**'teki terkindir.",
    ),
    # düzey 2
    '0023': patch(
        'Doğal afet nedeniyle varlıklarının önemli bir bölümünü kaybeden bir mükellefin amme borçları gündeme gelmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kanunda sayılan afetler yüzünden zarara uğrayan mükelleflerin ilgili amme alacakları kısmen veya tamamen terkin edilebilir; terkin alacağı sona erdirir',
            'B': 'Afet hâlinde borçlar yalnız tecil edilebilir; terkin imkânı bulunmadığından borç ertelenmekle birlikte varlığını sürdürür ve tecil süresi sonunda tamamı yeniden istenir',
            'C': 'Terkin yalnız vergi cezaları için uygulanır; vergi aslı bakımından silme imkânı olmadığından asıl borç aynen kalır',
            'D': 'Afetten doğan zararlar yalnız gelecek dönem matrahından indirilebilir; mevcut borçlar üzerinde bir etkisi bulunmaz',
            'E': 'Terkin ancak mükellefin iflası hâlinde mümkündür; afet hâli terkin sebebi sayılmadığından talep reddedilir',
        },
        'A',
        '**6183 m. 105:** yangın, yer sarsıntısı, su basması, kuraklık gibi **afetler yüzünden zarara maruz kalan** mükelleflerin bu Kanun kapsamındaki borçları, kanunda belirtilen şartlarla **terkin** olunur. Terkin, alacağı sona erdiren bir işlemdir.',
    ),
    # düzey 2
    '0024': patch(
        'Vadesinde ödenmeyen bir amme alacağı için tahsil dairesi ödeme emri düzenlemiş; borçlu hem süre hem de ileri sürebileceği sebepler bakımından hakları konusunda bilgi almak istemiştir. Buna göre amme alacaklarının tahsili ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Ödeme müddeti içinde ödenmeyen amme alacağı tahsil dairesince cebren tahsil olunur',
            'B': 'Ödeme emri tebliğ edilen borçlu, tebliğ tarihinden itibaren otuz gün içinde ve her türlü sebebe dayanarak dava açabilir',
            'C': 'Amme alacağını vadesinde ödemeyenlere on beş gün içinde ödeme veya mal bildirimi için ödeme emri tebliğ olunur',
            'D': 'Amme alacağı, vadesinin rastladığı takvim yılını takip eden yıl başından itibaren beş yıl içinde tahsil edilmezse zamanaşımına uğrar',
            'E': 'Amme borcunun vadesinde ödenmesi borçluyu çok zor duruma düşürecekse alacak teminat karşılığında tecil edilebilir',
        },
        'B',
        '**6183 m. 58:** ödeme emrine karşı dava süresi **on beş gün**dür ve sebepler **borcun bulunmadığı, kısmen ödendiği veya zamanaşımına uğradığı** iddialarıyla sınırlıdır. Hem süreyi hem de sebep serbestisini yanlış gösteren şık hükme aykırıdır.',
    ),
    # düzey 3
    '0025': patch(
        'Bir mükellefin defter ve belgeleri, kendi iradesi dışında meydana gelen bir su baskını sonucu elden çıkmıştır. Mükellef bu durumu ispatlamıştır. Buna göre süreler bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Mücbir sebep yalnız ceza kesilmesini engeller; süreler bakımından bir sonuç doğurmadığından beyanname süresinde verilmelidir',
            'B': 'Mücbir sebep ortadan kalkıncaya kadar süreler işlemez ve tarh zamanaşımı işlemeyen süreler kadar uzar',
            'C': 'Mücbir sebep sürelerin işlemesini etkilemez; mükellef ödevlerini zamanında yerine getirmekle yükümlü olduğundan gecikme cezası uygulanır',
            'D': 'Mücbir sebep hâlinde süreler durmaz ancak kesilir; bu nedenle süreler mücbir sebebin sona ermesiyle baştan işlemeye başlar ve zamanaşımı uzamaz',
            'E': 'Mücbir sebep hâlinde vergi alacağı tümüyle ortadan kalkar; alacak doğmamış sayılacağından tarh işlemi de yapılamaz',
        },
        'B',
        '**VUK m. 13** mücbir sebepleri sayar (sahibinin iradesi dışında defter ve vesikaların elden çıkması dâhil); **m. 15:** mücbir sebeplerden birinin bulunması hâlinde **bu sebep ortadan kalkıncaya kadar süreler işlemez** ve **tarh zamanaşımı işlemeyen süreler kadar uzar**.',
    ),
    # düzey 3
    '0026': patch(
        'Bir mükellef, ihtirazi kayıt koymaksızın verdiği beyannamedeki matraha karşı vergi mahkemesinde dava açmak istemektedir; ortada bir vergi hatası da bulunmamaktadır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mükellefler beyan ettikleri matrahlara karşı serbestçe dava açabilirler; beyan mükellefi bağlamadığından bir sınırlama yoktur',
            'B': 'Dava açılabilmesi için verginin tarh edilmiş veya cezanın kesilmiş olması gerekir',
            'C': 'Beyana karşı dava ancak verginin ödenmesinden sonra açılabilir; ödeme yapılmadığı sürece dava şartı gerçekleşmediğinden mahkeme işin esasına giremez ve istem usulden reddedilir',
            'D': 'Vergi hatalarına ilişkin hükümler beyana karşı dava yasağının istisnasını oluşturur',
            'E': 'Mükellefler ve kendilerine ceza kesilenler tarh edilen vergilere karşı dava açabilirler',
        },
        'A',
        '**VUK m. 378/2:** mükellefler **beyan ettikleri matrahlara karşı dava açamazlar**; vergi hatalarına ilişkin hükümler saklıdır. Serbest dava hakkı tanıyan ifade bu hükme aykırıdır.',
    ),
    # düzey 2
    '0027': patch(
        'İkmalen tarh edilen bir vergi ve buna ilişkin vergi ziyaı cezası için mükellef uzlaşma talebinde bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Uzlaşma talebi dava açma süresini kesmez ve durdurmaz; bu nedenle uzlaşma isteyen mükellefin aynı süre içinde ayrıca dava açması gerekir, aksi hâlde vergi kesinleşir',
            'B': 'Uzlaşma bütün vergi cezalarını kapsar; kaçakçılık fiillerinden doğan cezalar da uzlaşma konusu olabildiğinden ayrım yapılmaz',
            'C': 'Uzlaşma ancak vergi mahkemesinin onayıyla geçerli olur; idare ile mükellef arasındaki anlaşma tek başına sonuç doğurmadığından karar beklenir',
            'D': 'Uzlaşma yalnız beyana dayanan vergilerde mümkündür; ikmalen tarh edilen vergilerde uzlaşma yoluna gidilemeyeceğinden talep reddedilir',
            'E': "İkmalen, re'sen veya idarece tarh edilen vergiler ile bunlara ilişkin vergi ziyaı cezaları uzlaşma konusu olabilir; kaçakçılık fiillerine bağlı cezalar kapsam dışındadır",
        },
        'E',
        "**VUK Ek m. 1:** mükellef tarafından **ikmalen, re'sen veya idarece tarh edilen vergilerle bunlara ilişkin vergi ziyaı cezalarının** (**m. 359**'da yazılı kaçakçılık fiilleriyle ziyaa uğratılanlar hariç) tarhiyat sonrası uzlaşma konusu yapılması mümkündür.",
    ),
    # düzey 2
    '0028': patch(
        'Mahiyeti itibarıyla tahakkuku tahsile bağlı olan bir vergide, verginin tahsil edilmesi hâlinde tahakkuk bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Bu vergilerde tahakkuk yalnız ihbarname ile sağlanır; tahsil işleminin tahakkuka etkisi bulunmadığından ayrıca ihbarname düzenlenir',
            'B': 'Bu vergilerde önce tahakkuk, sonra tahsil işlemi yapılır; sıralamanın değiştirilmesi mümkün olmadığından tahsil tek başına sonuç doğurmaz',
            'C': 'Bu vergilerde tahakkuk hiç gerçekleşmez; vergi doğrudan tahsil edildiğinden tahakkuk aşaması hukuken var olmaz ve zamanaşımı işlemez',
            'D': 'Bu vergilerde verginin tahsili tahakkuku da içine alır; ayrıca bir tahakkuk işlemi yapılmasına gerek kalmaz',
            'E': 'Bu vergilerde tahsil ancak tahakkuk fişi düzenlendikten sonra yapılabilir; fiş olmadan yapılan tahsilat hukuken geçersiz sayılır',
        },
        'D',
        '**VUK m. 24:** mahiyetleri itibarıyla **tahakkuku tahsile bağlı vergilerde verginin tahsili tahakkuku da içine alır.** Damga vergisinin pul yapıştırılarak ödenmesi bu türün tipik örneğidir.',
    ),
    # düzey 2
    '0029': patch(
        "Vergilendirme süreci ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergi alacağı, vergi kanunlarının vergiyi bağladıkları olayın vukuu veya hukuki durumun tekemmülü ile doğar.\n\nII. Beyan üzerinden alınan vergiler tahakkuk fişi ile tarh ve tahakkuk ettirilir.\n\nIII. İkmalen ve re'sen tarh edilen vergiler de tahakkuk fişi ile tebliğ olunur.",
        {
            'A': 'Yalnız I',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'C',
        "**I doğru:** m. 19. **II doğru:** m. 25. **III yanlış:** **m. 34** uyarınca ikmalen ve re'sen tarh edilen vergiler **ihbarname** ile tebliğ olunur.",
    ),
    # düzey 3
    '0030': patch(
        "Tarh usulleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İkmalen tarh, daha önce hiçbir vergi tarh edilmemiş olmasını gerektirir.\n\nII. Re'sen tarhta matrah, takdir komisyonunca takdir edilebileceği gibi vergi inceleme raporunda da belirtilebilir.\n\nIII. Re'sen tarh, matrahın defter ve belgelere dayanılarak tespitine imkân bulunmayan hâllerde uygulanır.",
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'B',
        '**I yanlış:** m. 29 uyarınca ikmalen tarh, **bir vergi tarh edildikten sonra** ortaya çıkan matrah farkı içindir; önceki tarhiyatın yokluğunu değil, varlığını arar. **II ve III doğru:** m. 30.',
    ),
    # düzey 3
    '0031': patch(
        'Bir mükellef beyannamesini süresinde vermiş; vergi dairesi beyannamedeki matrahı aynen kabul ederek tahakkuk fişi düzenlemiştir. Mükellef daha sonra beyanında maddi bir hesap hatası bulunduğunu fark etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Mükellef beyanına karşı doğrudan dava açabilir; beyana karşı dava yasağı bulunmadığından düzeltme yoluna gitmeye gerek kalmaz',
            'B': 'Beyan edilen matrah kesin olduğundan hiçbir düzeltme yapılamaz; mükellef kendi beyanıyla bağlı sayıldığından hata iddiası ne idari başvuruda ne de yargı önünde dinlenir',
            'C': 'Düzeltme yalnız idarenin yaptığı hatalar için mümkündür; mükellefin kendi beyanındaki hatalar düzeltme kapsamı dışında kaldığından talep reddedilir',
            'D': 'Beyana karşı dava yolu kural olarak kapalı olsa da ortada bir vergi hatası bulunduğundan mükellef düzeltme hükümlerine dayanarak vergi dairesinden düzeltme isteyebilir',
            'E': 'Hata ancak vergi incelemesi sırasında ortaya çıkarsa düzeltilebilir; mükellefin kendiliğinden yaptığı başvuru işleme konulmaz',
        },
        'D',
        '**VUK m. 378/2** beyana karşı dava yasağını düzenlerken **vergi hatalarına ilişkin hükümleri saklı tutar**. Hesap hatası **m. 116** kapsamında vergi hatasıdır; **m. 122** uyarınca düzeltme yazı ile istenir.',
    ),
    # düzey 2
    '0032': patch(
        'Vergi dairesi, mükellefin bilinen işyeri adresine tebligat çıkarmış; tebligat, adreste bulunan ve mükellefin yanında çalışan bir işçiye yapılmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İşyerinde bulunan herhangi bir kişiye yapılan tebliğ geçerlidir; kanun tebliğ yapılacak kişiler bakımından bir sınırlama getirmediğinden süreler işlemeye başlar',
            'B': 'Tebliğ mükellefe, kanuni temsilcisine, umumi vekiline veya ceza kesilene yapılır; kanunun aradığı sıfatı taşımayan kişiye yapılan tebliğ usulüne uygun sayılmaz',
            'C': 'Bu hâlde tebliğ ilanen yapılmış sayılır; adreste kimse bulunmadığı varsayıldığından bir ay sonunda tebliğ tamamlanmış kabul edilir',
            'D': 'Tebliğ yalnız mükellefin bizzat kendisine yapılabilir; kanuni temsilciye yapılan tebliğ dahi geçersiz olduğundan işlem baştan sakattır',
            'E': 'İşyeri adresine yapılan her tebligat geçerlidir; adresin doğruluğu tek başına yeterli sayıldığından tebliğ yapılan kişinin sıfatı önem taşımaz',
        },
        'B',
        '**VUK m. 94:** tebliğ **mükelleflere, bunların kanuni temsilcilerine, umumi vekillerine veya vergi cezası kesilenlere** yapılır. Kanunun saydığı sıfatlardan birini taşımayan kişiye yapılan tebliğ usulsüzdür.',
    ),
    # düzey 2
    '0033': patch(
        'Bir mükellefin vergi borcunun bir kısmı ödenmiş, bir kısmı için tecil kararı alınmış, ayrı bir dönemine ilişkin alacak ise tarh zamanaşımına uğramıştır. Mükellef bütün bu alacakların sona erdiğini ileri sürmektedir. Buna göre vergi alacağını sona erdiren hâller ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tahsil zamanaşımının dolması amme alacağının tahsil edilebilirliğini ortadan kaldırır',
            'B': 'Kanunda sayılan afetler nedeniyle terkin, amme alacağını sona erdirir',
            'C': 'Tarh zamanaşımının dolması hâlinde vergi artık tarh ve tebliğ edilemez',
            'D': 'Ödeme, vergi alacağını sona erdiren en olağan hâldir',
            'E': 'Tecil, amme alacağını sona erdiren hâllerden biri olup tecil kararıyla borç ortadan kalkar',
        },
        'E',
        '**6183 m. 48** tecili, ödemenin **belirli şartlarla ertelenmesi** olarak düzenler; borç sona ermez, yalnız ödeme zamanı değişir. Terkin (m. 105) ise alacağı gerçekten sona erdirir.',
    ),
    # düzey 3
    '0034': patch(
        "Bir mükellefe ikmalen tarh edilen vergiye ilişkin ihbarname 5 Nisan'da tebliğ edilmiş; mükellef 20 Nisan'da vergi mahkemesinde dava açmıştır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': 'Dava açılması verginin tarhını ortadan kaldırır; idarenin aynı dönem için yeniden tarhiyat yapması gerekir',
            'B': 'Mükellefler tarh edilen vergilere karşı vergi mahkemesinde dava açabilirler',
            'C': 'Tahakkuk, tarh ve tebliğ edilen verginin ödenmesi gereken safhaya gelmesidir',
            'D': 'İhbarnameye bağlı tarhiyatta süresinde açılan dava tahakkuku ertelemez; vergi tebliğ anında ödenmesi gereken safhaya geldiğinden idare yargılama sürerken cebri takibe geçebilir',
            'E': 'Dava açma süresi dava açılmaksızın geçerse vergi tahakkuk eder',
        },
        'A',
        'Dava, verginin **tahakkukunu** erteler (m. 22); **tarh işlemini ortadan kaldırmaz**. Tarhın hukuka aykırılığı ancak yargı kararıyla saptanır ve o zaman işlem iptal edilir.',
    ),
    # düzey 2
    '0035': patch(
        'Vergi hatalarında düzeltme ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mükellefler vergi muamelelerindeki hataların düzeltilmesini yalnız sözlü başvuruyla isteyebilirler.\n\nII. Vergi hatası, haksız yere fazla veya eksik vergi istenmesi ya da alınmasıdır.\n\nIII. Tarh zamanaşımı süresi dolduktan sonra ortaya çıkarılan vergi hataları her hâlde düzeltilir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'II ve III',
        },
        'D',
        '**I yanlış:** m. 122 düzeltmenin **yazı ile** istenmesini öngörür. **II doğru:** m. 116. **III yanlış:** m. 126 uyarınca zamanaşımı dolduktan sonra ortaya çıkarılan hatalar kural olarak **düzeltilemez**.',
    ),
    # düzey 2
    '0036': patch(
        'Vergilendirmede tebliğ ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tebliğ, hüküm ifade eden hususların yetkili makamlarca mükellefe yazı ile bildirilmesidir.\n\nII. Adresi bilinmeyen veya bilinen adreste tebliğ yapılamayan hâllerde ilan yoluyla tebliğ yapılır.\n\nIII. Tüzel kişilere tebliğ, ancak bütün yönetim kurulu üyelerine ayrı ayrı yapılırsa geçerli olur.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        '**I doğru:** m. 21. **II doğru:** m. 103. **III yanlış:** **m. 94** uyarınca tüzel kişilere tebliğ başkan, müdür veya kanuni temsilcilere yapılır ve bunlar **birden çoksa birine yapılması yeterlidir**.',
    ),
    # düzey 3
    '0037': patch(
        'Vergi dairesi bir mükellef hakkında vergi incelemesi yapmış; inceleme raporunda belirtilen matrah üzerinden tarhiyat yapmıştır. Mükellefin defterleri mevcut olmakla birlikte kayıtlar matrahın tespitine elverişli bulunmamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': "Matrahın kayıtlara dayanılarak tespitine imkân bulunmadığından re'sen tarhiyat yapılır ve matrah inceleme raporunda belirtilen tutar üzerinden belirlenir",
            'B': "Defterler mevcut olduğundan yalnız ikmalen tarhiyat yapılabilir; re'sen tarh defterlerin hiç bulunmadığı hâllere özgü olduğundan burada uygulanamaz",
            'C': "Bu hâlde idarece tarh usulü uygulanır; idarece tarh, mükellefin ödevlerini yerine getirmediği bütün hâlleri kapsadığından re'sen tarha gerek kalmaz",
            'D': 'Kayıtların elverişsizliği mücbir sebep sayılır; süreler işlemeyeceğinden tarhiyat yapılamaz ve zamanaşımı da uzar',
            'E': 'İnceleme raporu tek başına tarhiyata dayanak olamaz; matrahın mutlaka takdir komisyonunca belirlenmesi gerektiğinden rapora dayanan tarhiyat sakattır',
        },
        'A',
        "**VUK m. 30:** re'sen tarh, matrahın **tamamen veya kısmen** defter, kayıt ve belgelere veya kanuni ölçülere dayanılarak tespitine imkân bulunmayan hâllerde uygulanır; matrah takdir komisyonunca takdir edilebileceği gibi **vergi inceleme raporunda da belirtilebilir**.",
    ),
    # düzey 3
    '0038': patch(
        'Tarh zamanaşımı süresi içinde mücbir sebep hâli doğmuş ve altı ay sürmüştür. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Mücbir sebep hâlinde zamanaşımı süresi iki katına çıkar; süre on yıla uzayacağından idarenin ek bir işlem yapmasına gerek kalmaz',
            'B': 'Mücbir sebep zamanaşımını keser; süre yeniden başlayacağından beş yıllık süre baştan işlemeye başlar',
            'C': 'Mücbir sebep süresince süreler işlemez ve tarh zamanaşımı işlemeyen süreler kadar uzar; süre altı ay uzamış olur',
            'D': 'Mücbir sebep yalnız ceza kesilmesini engeller; zamanaşımı bakımından bir etkisi bulunmadığından süre aynen dolar',
            'E': 'Mücbir sebep zamanaşımına etki etmez; süre kesintisiz işlediğinden tarhiyatın beş yıl içinde tamamlanması gerekir',
        },
        'C',
        "**VUK m. 15:** m. 13'teki mücbir sebeplerden birinin bulunması hâlinde **bu sebep ortadan kalkıncaya kadar süreler işlemez** ve **tarh zamanaşımı işlemeyen süreler kadar uzar.** Durma söz konusudur, kesilme değil.",
    ),
    # düzey 2
    '0039': patch(
        "Bir vergi dairesi, üç ayrı mükellef hakkında sırasıyla beyana dayanan tarhiyat, ikmalen tarhiyat ve re'sen tarhiyat yapmış; her biri için farklı belge ve usul izlemiştir. Buna göre Vergi Usul Kanunu'na göre tarh usulleri ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': "Re'sen tarhta matrah takdir komisyonunca takdir edilebilir",
            'B': 'İkmalen tarhiyat, daha önce hiçbir vergi tarh edilmemiş olan hâllerde matrahın idarece belirlenmesi usulüdür',
            'C': "Re'sen tarh, matrahın defter ve belgelere dayanılarak tespitine imkân bulunmayan hâllerde uygulanır",
            'D': "İkmalen ve re'sen tarh edilen vergiler ihbarname ile tebliğ olunur",
            'E': 'Beyan üzerinden alınan vergiler tahakkuk fişi ile tarh ve tahakkuk ettirilir',
        },
        'B',
        '**VUK m. 29:** ikmalen tarh, **her ne şekilde olursa olsun bir vergi tarh edildikten sonra** ortaya çıkan matrah farkı üzerinden yapılır; önceden bir tarhiyatın varlığını gerektirir. Yanlış olan şık bunun tersini söylemektedir.',
    ),
    # düzey 2
    '0040': patch(
        'Bir amme borçlusuna ödeme emri tebliğ edilmiş; borçlu on beş günlük süre içinde ne ödeme yapmış ne de mal bildiriminde bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Borçlu mal bildiriminde bulunmadığı için takip düşer; mal bildirimi cebri takibin ön şartı olduğundan haciz uygulanamaz',
            'B': 'Süre geçmiş olsa dahi borçluya ayrıca otuz günlük ek süre verilir; bu süre dolmadan cebri işlem yapılamaz',
            'C': 'Ödeme müddeti içinde ödenmeyen amme alacağı tahsil dairesince cebren tahsil olunur; kanunda sayılan cebri takip yollarına başvurulabilir',
            'D': 'Cebri takip ancak mahkeme kararıyla başlatılabilir; idarenin resen haciz yetkisi bulunmadığından dava açılması gerekir',
            'E': 'Süre geçtikten sonra idarenin yeniden ödeme emri tebliğ etmesi gerekir; ilk ödeme emri hükümsüz hâle geldiğinden cebri takip baştan başlatılır ve süreler yeniden işler',
        },
        'C',
        "**6183 m. 54:** ödeme müddeti içinde ödenmeyen amme alacağı **tahsil dairesince cebren tahsil olunur**; madde cebri tahsil şekillerini sayar. Ödeme emri ve on beş günlük süre m. 55'te düzenlenmiştir.",
    ),
    # düzey 2
    '0041': patch(
        'Bir mükellef beyannamesini vermiş, vergi dairesi beyan üzerine tahakkuk fişi düzenlemiş ve vergi süresinde ödenmiştir. Mükellef, sürecin hangi aşamasında hangi işlemin gerçekleştiğini sormaktadır. Buna göre vergilendirme süreci ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tahsil, verginin kanuna uygun surette ödenmesidir',
            'B': 'Verginin tarhı, vergi alacağının mükellef tarafından hesaplanarak beyan edilmesi işlemidir',
            'C': 'Tahakkuk, tarh ve tebliğ edilen bir verginin ödenmesi gereken safhaya gelmesidir',
            'D': 'Verginin tarhı, vergi alacağının kanunlarında gösterilen matrah ve nispetler üzerinden vergi dairesince hesaplanmasıdır',
            'E': 'Tebliğ, hüküm ifade eden hususların yetkili makamlarca mükellefe yazı ile bildirilmesidir',
        },
        'B',
        '**VUK m. 20:** tarh, vergi alacağının matrah ve nispetler üzerinden **vergi dairesi tarafından** hesaplanarak miktar itibarıyla tespit edilmesini sağlayan **idari muameledir**. Mükellefin beyanı tarh işleminin dayanağıdır; tarhın kendisi değildir.',
    ),
    # düzey 3
    '0042': patch(
        'Bir mükellef, kendisine tebliğ edilen ihbarnameye karşı süresinde dava açmak yerine uzlaşma talebinde bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': "İkmalen, re'sen veya idarece tarh edilen vergiler ile bunlara ilişkin vergi ziyaı cezaları uzlaşma konusu yapılabilir; uzlaşmanın sağlanması hâlinde uzlaşılan hususlar dava konusu edilemez",
            'B': 'Uzlaşma talebi dava hakkını ortadan kaldırmaz; uzlaşma sağlansa dahi mükellef aynı hususlar için vergi mahkemesine başvurabileceğinden idarenin uzlaşma tutanağı yargı denetimini engellemez',
            'C': 'Uzlaşma yalnız vergi aslı için istenebilir; vergi ziyaı cezaları uzlaşma kapsamı dışında olduğundan ceza için ayrıca dava açılması gerekir',
            'D': 'Uzlaşma ancak tahsil aşamasında istenebilir; tarhiyat aşamasında yapılan başvurular erken sayıldığından reddedilir',
            'E': 'Uzlaşma talebi vergi dairesini bağlamaz ve hiçbir hukuki sonuç doğurmaz; idare talebi dikkate almaksızın takibe devam eder',
        },
        'A',
        "**VUK Ek m. 1** uzlaşma kapsamını ikmalen, re'sen veya idarece tarh edilen vergiler ve bunlara ilişkin vergi ziyaı cezaları olarak belirler (m. 359 fiilleri hariç). Uzlaşma sağlandığında uzlaşılan hususlar hakkında dava açılamaz.",
    ),
    # düzey 2
    '0043': patch(
        'Zamanaşımı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tarh zamanaşımı, vergi alacağının doğduğu takvim yılını takip eden yılın başından itibaren beş yıldır.\n\nII. Tahsil zamanaşımı, alacağın vadesinin rastladığı takvim yılını takip eden yıl başından itibaren beş yıldır.\n\nIII. Mücbir sebep hâlinde tarh zamanaşımı, işlemeyen süreler kadar uzar.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'Yalnız III',
            'E': 'I, II ve III',
        },
        'E',
        'Üçü de doğrudur. **I:** VUK m. 114. **II:** 6183 m. 102. **III:** VUK m. 15, mücbir sebep süresince süreler işlemez ve tarh zamanaşımı işlemeyen süreler kadar uzar.',
    ),
    # düzey 2
    '0044': patch(
        'Bir mükellefin bilinen adresleri arasında hem işe başlamada bildirdiği işyeri adresi hem de adres kayıt sistemindeki yerleşim yeri adresi bulunmaktadır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Adres kayıt sistemindeki yerleşim yeri adresi bilinen adreslerdendir',
            'B': 'Mükellef tarafından işe başlamada bildirilen işyeri adresleri bilinen adres sayılmaz; bu adrese yapılan tebligat usulsüz olduğundan süreler işlemeye başlamaz ve tarhiyat askıda kalır',
            'C': 'Bilinen adres kavramı kanunda tanımlanmadığından tebligatın hangi adrese yapılacağı tümüyle idarenin takdirindedir',
            'D': 'Tebliğ, kanunda sayılan bilinen adreslere yapılır',
            'E': 'Bilinen adreste tebliğ yapılamayan hâllerde ilan yoluna başvurulabilir',
        },
        'C',
        '**VUK m. 101** bilinen adresleri **tek tek sayarak** belirler; tebliğ bu adreslere yapılır. Kanunda tanım bulunmadığını ve seçimin tümüyle idarenin takdirinde olduğunu söyleyen ifade yanlıştır.',
    ),
    # düzey 2
    '0045': patch(
        "Bir mükellef, beyan ettiği matraha karşı dava açmak istemekte; ayrıca hakkında tarh edilen vergiyi ödemeden mahkemeye başvurup başvuramayacağını sormaktadır. Buna göre Vergi Usul Kanunu'na göre dava açma hakkı bakımından aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': 'Mükellefler kural olarak beyan ettikleri matrahlara karşı dava açamazlar',
            'B': 'Vergi mahkemesinde dava açabilmek için verginin ödenmiş olması şarttır; ödeme yapılmadan açılan davalar esasa girilmeksizin reddedilir',
            'C': 'Mükellefler ve kendilerine vergi cezası kesilenler, tarh edilen vergilere ve kesilen cezalara karşı vergi mahkemesinde dava açabilirler',
            'D': 'Vergi hatalarına ilişkin hükümler, beyana karşı dava yasağının istisnasını oluşturur',
            'E': 'Vergi mahkemesinde dava açabilmek için verginin tarh edilmiş veya cezanın kesilmiş olması gerekir',
        },
        'B',
        '**VUK m. 377** dava hakkını tanır, **m. 378** ise dava açılabilmesi için verginin tarh edilmiş, cezanın kesilmiş ya da komisyon kararlarının tebliğ edilmiş olmasını arar. **Ödeme şartı öngörülmemiştir**; yanlış olan şık budur.',
    ),
    # düzey 2
    '0046': patch(
        'İkmalen tarh olunan bir vergi, taksit süreleri geçtikten sonra tahakkuk etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Gecikme faizi tahsil aşamasında değil tarh aşamasında hesaplanır; tahakkuk etmemiş vergi için faiz işlemeye başlar',
            'B': "İkmalen, re'sen veya idarece tarh olunan vergilerde, kanunda gösterilen dönem için gecikme faizi hesaplanır ve vergi ile birlikte tahsil edilir",
            'C': 'Gecikme faizi yalnız beyana dayanan vergilerde uygulanır; ikmalen tarhiyatta faiz öngörülmediğinden yalnız vergi aslı istenir',
            'D': 'Bu vergilerde faiz hesaplanmaz; gecikme yalnız ceza kesilmesini gerektirdiğinden mükelleften vergi aslı ve ceza dışında ayrıca bir faiz yükü istenmesi mümkün olmaz',
            'E': 'Gecikme faizi vergi mahkemesi kararıyla belirlenir; idarenin resen faiz hesaplama yetkisi bulunmadığından tahsil edilemez',
        },
        'B',
        "**VUK m. 112:** ikmalen, re'sen veya idarece tarh olunan vergilerde, kanunda belirtilen dönemler için **gecikme faizi** hesaplanır ve verginin kendisiyle birlikte tahsil edilir.",
    ),
    # düzey 2
    '0047': patch(
        'Bir mükellefin defter ve belgeleri matrahın tespitine elverişli bulunmadığından matrah takdir komisyonuna sevk edilmiş; komisyon inceleme sonunda bir tutar belirlemiştir. Buna göre takdir komisyonunun belirlediği matrah bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': "Takdir komisyonu kararları yalnız beyana dayanan vergilerde uygulanır; re'sen tarhiyatta komisyona başvurulamaz",
            'B': 'Takdir komisyonu kararları tebliğ edilmeksizin kesinleşir; mükellefin bu kararlara karşı dava açma hakkı bulunmaz',
            'C': 'Takdir komisyonu kararları sözlü olarak bildirilir; yazılı karara bağlanma zorunluluğu bulunmadığından imza şartı da aranmaz ve karar tutanağa geçirilmeksizin uygulanır',
            'D': 'Takdir komisyonu yalnız görüş bildirir; matrah belirleme yetkisi bulunmadığından kararı idareyi bağlamaz',
            'E': 'Takdir komisyonunca belli edilen matrah veya matrah kısmı takdir kararına bağlanır ve karar komisyonun başkan ve üyelerince imzalanır',
        },
        'E',
        "**VUK m. 31:** takdir komisyonunca belli edilen matrah veya matrah kısmı **takdir kararına bağlanır** ve kararlar **komisyonun başkan ve üyeleri tarafından imzalanır.** Komisyon kararları re'sen tarhın (m. 30) dayanaklarındandır.",
    ),
    # düzey 2
    '0048': patch(
        "Bir vergi dairesi aynı gün içinde hem beyana dayanan bir vergi için tahakkuk fişi düzenlemiş hem de re'sen tarh ettiği bir vergi için belge çıkarmış; iki belgenin işlevini birbirine karıştırmamaya çalışmaktadır. Buna göre vergilendirme sürecinde ihbarname ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': "İhbarnamede verginin nev'i, mükellefin kimliği ve tarh edilen tutar gibi bilgiler yer alır",
            'B': "İkmalen ve re'sen tarh edilen vergiler ihbarname ile ilgililere tebliğ olunur",
            'C': 'İhbarname yalnız vergi cezaları için düzenlenir; tarh edilen vergiler istisnasız biçimde tahakkuk fişi ile bildirilir',
            'D': "Nev'i ve doğuşu ayrı olan vergiler için ayrı ihbarname kullanılır",
            'E': 'İhbarnamedeki bilgi eksiklikleri, verginin miktarına ilişkin olanlar dışında tebliği hükümsüz kılmaz',
        },
        'C',
        "**VUK m. 34:** **ikmalen ve re'sen tarh edilen vergiler** ihbarname ile tebliğ olunur; ihbarname yalnız cezalara özgü değildir. Tahakkuk fişi ise m. 25 uyarınca beyana dayanan vergilere aittir.",
    ),
    # düzey 3
    '0049': patch(
        'Bir mükellef, hakkında yapılan tarhiyata karşı süresinde dava açmamış ve vergi tahakkuk etmiştir. Mükellef daha sonra tarhiyatta bir hesap hatası bulunduğunu ileri sürmüştür. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Hata iddiası ancak yeni bir vergi incelemesiyle ileri sürülebilir; mükellefin doğrudan başvuru hakkı bulunmaz',
            'B': 'Vergi tahakkuk ettiğinden hata iddiası dinlenmez; tahakkuk işlemi bütün itirazları sona erdirdiğinden mükellefin düzeltme ve dava yolları birlikte kapanır',
            'C': 'Tahakkuk eden vergide düzeltme yalnız idarenin kendiliğinden yapacağı işlemle mümkündür; mükellefin talep hakkı yoktur',
            'D': 'Verginin tahakkuk etmiş olması vergi hatasının düzeltilmesine engel değildir; mükellef zamanaşımı süresi içinde düzeltme isteyebilir',
            'E': 'Düzeltme yalnız dava açma süresi içinde istenebilir; süre geçtikten sonra yapılan başvurular süre yönünden reddedilir',
        },
        'D',
        "**VUK m. 122** mükellefe düzeltme isteme hakkını tanır; bu hak dava açma süresinden bağımsızdır ve **m. 126**'daki düzeltme zamanaşımı süresi içinde kullanılabilir. Tahakkuk, hatanın düzeltilmesine engel oluşturmaz.",
    ),
    # düzey 2
    '0050': patch(
        'Vergilendirme süreci ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tahakkuku tahsile bağlı vergilerde verginin tahsili tahakkuku da içine alır.\n\nII. Mücbir sebep hâlinde süreler işlemeye devam eder ve tarh zamanaşımı uzamaz.\n\nIII. Beyan üzerinden alınan vergiler tahakkuk fişi ile tarh ve tahakkuk ettirilir.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'D',
        '**I doğru:** m. 24. **II yanlış:** m. 15 uyarınca mücbir sebep süresince **süreler işlemez** ve tarh zamanaşımı işlemeyen süreler kadar **uzar**. **III doğru:** m. 25.',
    ),
    # düzey 3
    '0051': patch(
        "Bir mükellef hakkında re'sen tarh edilen vergiye ilişkin ihbarname, mükellefin bilinen adresinde bulunamaması üzerine ilan yoluyla tebliğ edilmiştir. İlan 1 Mart'ta yapılmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'İlanen tebliğde süre üç ay sonra başlar; bu süre mükellefin savunma hakkını korumak için öngörülmüştür',
            'B': 'İlanen tebliğ hüküm doğurmaz; mükellefe fiilen ulaşılmadıkça süreler işlemeyeceğinden tarhiyat askıda kalır',
            'C': "İlanın yapıldığı tarihten başlayarak bir ayın sonunda, yani 1 Nisan'da tebliğ yapılmış sayılır ve süreler bu tarihten işlemeye başlar",
            'D': "İlanen tebliğde tebliğ tarihi on beş gün sonra gerçekleşir; süreler 16 Mart'tan itibaren işlemeye başlar",
            'E': "İlan tarihinde tebliğ yapılmış sayılır; 1 Mart'tan itibaren süreler işleyeceğinden dava açma süresi de o gün başlar ve ayrıca bir bekleme süresi öngörülmez",
        },
        'C',
        "**VUK m. 106:** ilan yoluyla yapılan tebliğde, **ilanın yapıldığı tarihten başlayarak bir ayın sonunda** tebliğ yapılmış sayılır. İlanen tebliğ hâlleri m. 103'te sayılmıştır.",
    ),
    # düzey 2
    '0052': patch(
        'Özel kanununda ödeme zamanı belirlenmiş bir amme alacağı ile ödeme zamanı belirlenmemiş başka bir amme alacağı aynı borçlu adına tahakkuk etmiştir. Borçlu her iki alacağı ne zaman ödeyeceğini sormaktadır. Buna göre amme alacaklarında ödeme ile ilgili aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Amme alacaklarında ödeme zamanı yalnız mahkeme kararıyla belirlenir; idarenin ve kanunun belirlemesi bağlayıcı sayılmaz',
            'B': 'Bütün amme alacakları takvim yılı sonunda topluca ödenir; özel kanunlardaki ödeme zamanları uygulanmadığından tek bir vade geçerlidir',
            'C': 'Ödeme zamanı belirlenmemiş alacaklar hiç tahsil edilemez; vade olmaksızın takip yapılamayacağından alacak düşer',
            'D': 'Amme alacaklarının ödeme zamanı borçlu tarafından serbestçe belirlenir; idarenin süre belirleme yetkisi bulunmadığından vade tartışmaya açıktır',
            'E': 'Amme alacakları hususi kanunlarında belli edilen zamanlarda ödenir; ödeme zamanı tespit edilmemiş alacaklarda ilgili idarece belirlenen süre uygulanır',
        },
        'E',
        '**6183 m. 37:** amme alacakları **hususi kanunlarında belli edilen zamanlarda** ödenir; hususi kanunlarında ödeme zamanı tespit edilmemiş amme alacakları ilgili idarece belirtilecek usule göre ödenir.',
    ),
    # düzey 2
    '0053': patch(
        'Bir mükellef, hakkındaki tarh zamanaşımı süresinin dolmak üzere olduğunu görerek vergi dairesinden sürenin uzatılmasını istemiş; ayrıca geçmişte yaşadığı mücbir sebep hâlinin süreye etkisini sormuştur. Buna göre vergi hukukunda süreler ve zamanaşımı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tarh zamanaşımı süresi, mükellefin talebi hâlinde vergi dairesince uzatılabilir',
            'B': 'Tarh zamanaşımı, vergi alacağının doğduğu takvim yılını takip eden yılın başından itibaren beş yıldır',
            'C': 'Mücbir sebep hâlinde süreler işlemez ve tarh zamanaşımı işlemeyen süreler kadar uzar',
            'D': 'Zamanaşımına uğrayan bir vergi tarh ve tebliğ edilemez',
            'E': 'Tahsil zamanaşımı, vadenin rastladığı takvim yılını takip eden yıl başından itibaren beş yıldır',
        },
        'A',
        "Zamanaşımı süreleri **kanunla** belirlenmiştir (VUK m. 114, 6183 m. 102); idarenin veya mükellefin talebiyle uzatılamaz. Süreyi uzatan tek hâl **m. 15**'teki mücbir sebeptir.",
    ),
    # düzey 3
    '0054': patch(
        'Bir mükellef, vergi ziyaına yol açan fiili nedeniyle hakkında inceleme başlatıldıktan sonra pişmanlık talebinde bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Pişmanlık talebi vergi aslını da ortadan kaldırır; inceleme başlamış olsa dahi yalnız pişmanlık zammı ödenir',
            'B': 'Pişmanlık hükümlerinden yararlanabilmek için haber vermenin, mükellef hakkında bir ihbar yapılmadan ve inceleme başlamadan önce yapılması gerekir; şart gerçekleşmediğinden talep kabul edilmez',
            'C': 'Pişmanlık her aşamada istenebilir; inceleme başlamış olması hükümlerin uygulanmasını engellemediğinden mükellef adına vergi ziyaı cezası kesilmez ve yalnız pişmanlık zammı aranır',
            'D': 'Pişmanlık yalnız inceleme sırasında istenebilir; inceleme öncesi yapılan başvurular erken sayıldığından işleme konulmaz',
            'E': 'Pişmanlık beyana dayanmayan vergilerde de uygulanır; kapsam bakımından bir sınırlama bulunmadığından talep kabul edilir',
        },
        'B',
        '**VUK m. 371** pişmanlık için haber vermenin, mükellef hakkında **ihbarda bulunulmadan ve vergi incelemesine başlanmadan** önce yapılmasını arar. Şartlar gerçekleşmezse vergi ziyaı cezası kesilir.',
    ),
    # düzey 2
    '0055': patch(
        'Vergi alacağının doğumu ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergi alacağı, vergi kanunlarının vergiyi bağladıkları olayın vukuu veya hukuki durumun tekemmülü ile doğar.\n\nII. Vergi alacağı, ancak mükellefin beyanname vermesiyle doğar.\n\nIII. Vergi alacağı ancak tarh işlemiyle doğar; tarh edilmeyen bir vergi alacağından söz edilemez.',
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'D',
        '**I doğru:** m. 19. **II ve III yanlış:** beyan ve tarh, doğmuş bir alacağın tespit ve bildirim aşamalarıdır; **m. 20** tarhı alacağın *miktar itibarıyla tespiti* olarak tanımlar, alacağı doğuran işlem olarak değil.',
    ),
    # düzey 3
    '0056': patch(
        'Bir vergi dairesi, mükellefe tebliğ ettiği ihbarnamede tarh edilen vergi tutarını sehven eksik göstermiş, hatayı tebliğden sonra fark etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tebliğ geçerli olmakla birlikte mükellefin dava açma süresi iki katına çıkar; bu suretle eksiklik telafi edilmiş sayılır',
            'B': 'Verginin miktarına ilişkin bilgilerdeki eksiklik tebliği hükümsüz kıldığından işlemin usulüne uygun biçimde yenilenmesi gerekir',
            'C': 'İhbarnamedeki her türlü eksiklik gibi bu eksiklik de tebliği etkilemez; tebliğ geçerli sayıldığından süreler işlemeye devam eder',
            'D': 'Eksik gösterilen tutar mükellef lehine sonuç doğurduğundan idare aradaki farkı sonradan talep edemez; ihbarnamedeki tutar idareyi bağladığından tarhiyat o miktarla sınırlı kalır',
            'E': 'Hata yalnız düzeltme yoluyla giderilir; tebliğin geçerliliği tartışılamayacağından yeni bir ihbarname düzenlenmesine gerek yoktur',
        },
        'B',
        '**VUK m. 35** son fıkrası, ihbarnamedeki bilgi eksikliklerinin tebliği hükümsüz kılmayacağını belirtirken **verginin miktarına ilişkin olanları bunun dışında** tutar; miktara ilişkin eksiklik tebliği hükümsüz kılar.',
    ),
    # düzey 2
    '0057': patch(
        "Bir mükellef, ticari faaliyetinde beklediği kârı elde edemediği için beyannamesini süresinde veremediğini ileri sürerek mücbir sebep hükümlerinden yararlanmak istemektedir. Buna göre Vergi Usul Kanunu'na göre mücbir sebepler ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': 'Vergi ödevlerinden birinin yerine getirilmesine engel olacak derecede ağır kaza, ağır hastalık ve tutukluluk mücbir sebeptir',
            'B': 'Vergi ödevlerinin yerine getirilmesine engel olacak yangın, yer sarsıntısı ve su basması gibi afetler mücbir sebeptir',
            'C': 'Mükellefin ticari faaliyetinde beklediği kârı elde edememesi mücbir sebep sayılır ve süreleri durdurur',
            'D': 'Sahibinin iradesi dışında defter ve vesikalarının elden çıkmış olması mücbir sebeptir',
            'E': 'Mücbir sebep hâlinde bu sebep ortadan kalkıncaya kadar süreler işlemez',
        },
        'C',
        '**VUK m. 13** mücbir sebepleri sınırlı biçimde sayar: ağır kaza/hastalık/tutukluluk, afetler, kişinin iradesi dışında kaybolma ve defter-vesikaların iradesi dışında elden çıkması. **Ticari başarısızlık mücbir sebep değildir.**',
    ),
    # düzey 2
    '0058': patch(
        'Bir amme borçlusu, kendisine tebliğ edilen ödeme emrinde gösterilen borcun bir kısmını daha önce ödediğini ileri sürmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kısmen ödeme iddiası ödeme emrine karşı ileri sürülebilecek sebeplerdendir; borçlu tebliğ tarihinden itibaren on beş gün içinde dava açabilir',
            'B': 'Ödeme emrine karşı yalnız borcun hiç bulunmadığı iddiasıyla dava açılabilir; kısmi ödeme iddiası kanunda sayılmadığından dinlenmez',
            'C': 'Kısmen ödeme iddiası ödeme emri aşamasında ileri sürülemez; bu iddia yalnız tahsil sonrası açılacak iade davasına konu olabileceğinden ödeme emri kesinleşir',
            'D': 'Kısmen ödeme iddiası için dava süresi otuz gündür; genel dava süresi uygulandığından ayrı bir süre öngörülmemiştir',
            'E': 'Bu iddia yalnız tahsil dairesine idari başvuruyla ileri sürülebilir; dava yolu kapalı olduğundan mahkemeye gidilemez',
        },
        'A',
        '**6183 m. 58:** ödeme emri tebliğ olunan şahıs, **böyle bir borcu olmadığı veya kısmen ödediği veya zamanaşımına uğradığı** hakkında tebliğ tarihinden itibaren **on beş gün içinde** dava açabilir.',
    ),
    # düzey 2
    '0059': patch(
        'Bir vergi dairesi, beyana dayanan bir vergiyi tahakkuk fişiyle, ikmalen tarh ettiği başka bir vergiyi ise ihbarnameyle işleme almış; mükellef ikinci vergiye karşı süresinde dava açmıştır. Buna göre vergilendirme sürecinde tahakkuk ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İhbarnameye bağlı tarhiyatta süresinde açılan dava tahakkuku erteler',
            'B': 'Beyan üzerinden alınan vergiler tahakkuk fişi ile tarh ve tahakkuk ettirilir',
            'C': 'Beyan üzerinden alınan vergilerde tahakkuk, verginin fiilen ödendiği tarihte gerçekleşir',
            'D': 'Tahakkuku tahsile bağlı vergilerde verginin tahsili tahakkuku da içine alır',
            'E': 'Tahakkuk, tarh ve tebliğ edilen bir verginin ödenmesi gereken safhaya gelmesidir',
        },
        'C',
        '**VUK m. 25** beyan üzerinden alınan vergilerde tarh ve tahakkukun **tahakkuk fişiyle birlikte** gerçekleştiğini düzenler; ödeme tahsil aşamasıdır (m. 23) ve tahakkukla karıştırılmamalıdır.',
    ),
    # düzey 3
    '0060': patch(
        "Bir mükellef hakkında 2021 yılında doğan vergi alacağı için 2026 yılı Mart ayında re'sen tarhiyat yapılmış ve ihbarname aynı ay tebliğ edilmiştir. Mükellefin 2023 yılında altı ay süren bir mücbir sebep hâli bulunmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': "Mücbir sebep zamanaşımını kestiğinden beş yıllık süre 2023'ten itibaren yeniden başlar; tarhiyat bu nedenle erken yapılmıştır",
            'B': "Tarh zamanaşımı on yıl olduğundan mücbir sebep hesabına gerek yoktur; süre 31 Aralık 2031'de dolacağından tarhiyat her hâlükârda süresinde sayılır",
            'C': "Re'sen tarhiyatta zamanaşımı işlemez; matrah takdire dayandığından süre şartı aranmaz",
            'D': "Beş yıllık tarh zamanaşımı 31 Aralık 2026'da dolacakken mücbir sebep nedeniyle altı ay uzadığından tarhiyat süresinde yapılmıştır",
            'E': "Zamanaşımı 31 Aralık 2025'te dolduğundan tarhiyat zamanaşımına uğramıştır; mücbir sebebin süreye etkisi bulunmaz",
        },
        'D',
        "2021'de doğan alacakta süre **1 Ocak 2022**'de başlar ve beş yıl sonra **31 Aralık 2026**'da dolar (**VUK m. 114**). **m. 15** uyarınca mücbir sebep süresince süreler işlemez ve zamanaşımı işlemeyen süreler kadar **uzar**; Mart 2026 tarhiyatı zaten süre içindedir.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Vergilendirme Sureci' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
