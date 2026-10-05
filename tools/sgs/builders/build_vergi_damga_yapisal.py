#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Damga Vergisi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim: kagit ve mukellef, nusha-coklu islem-imza, olcu ve oran, odeme sekilleri ve zamani, sorumluluk, (1) sayili tablo uygulamalari ve (2) sayili tablo istisnalari. Yila bagli maktu tutar ve azami tutar sorulmadi; 14 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 488 sayili Damga Vergisi Kanunu guncel metni ve (1)-(2) sayili tablolar (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/damga_vergisi.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "damga-gen-"


def patch(stem, options, answer, solution, ref='488 sayili Damga Vergisi Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Aşağıdakilerden hangisi Damga Vergisi Kanunu'nun 1. maddesi anlamında 'kâğıt' sayılmaz?",
        {
            'A': 'İmza yerine şirket mührü basılmış taahhütname',
            'B': 'Islak imzalı kira sözleşmesi',
            'C': 'Taraflarca imzalanmamış taslak sözleşme metni',
            'D': 'Güvenli elektronik imzayla oluşturulan sözleşme',
            'E': 'İmza yerine parmak izi konulmuş makbuz',
        },
        'C',
        "m. 1'e göre kâğıt; **yazılıp imzalanmak veya imza yerine geçen bir işaret konmak suretiyle** düzenlenen ve bir hususu ispat veya belli etmek için ibraz edilebilecek belgeler ile **elektronik imza kullanılarak** elektronik veri şeklinde oluşturulan belgelerdir. İmzasız taslak bu unsurları taşımaz.",
        '488 sayılı Damga Vergisi Kanunu m. 1',
    ),
    # düzey 2
    '0002': patch(
        'Bir belediye ile bir inşaat şirketi arasında imzalanan hizmet sözleşmesinin damga vergisini kim öder?',
        {
            'A': 'Belediye',
            'B': 'İnşaat şirketi',
            'C': 'Sözleşmeyi hazırlayan taraf',
            'D': 'Belediye ve şirket yarı yarıya',
            'E': 'Sözleşmeyi onaylayan noter',
        },
        'B',
        "m. 3'e göre damga vergisinin mükellefi kâğıtları imza edenlerdir; ancak **resmî dairelerle kişiler arasındaki işlemlere ait kâğıtların vergisini kişiler öder**. Belediye m. 8'e göre resmî dairedir; vergiyi şirket öder.",
        '488 sayılı Damga Vergisi Kanunu m. 3',
    ),
    # düzey 3
    '0003': patch(
        "Bedeli 1.000.000 ₺ olan bir satış sözleşmesi üç nüsha olarak düzenlenmiştir. Oranın binde 9,48 olduğu dikkate alınırsa ödenecek toplam damga vergisi kaç ₺'dir?",
        {
            'A': '0',
            'B': '9.480',
            'C': '28.440',
            'D': '3.160',
            'E': '18.960',
        },
        'B',
        "6728 sayılı Kanunla değişen m. 5'e göre bir nüshadan fazla düzenlenen kâğıtlardan **maktu vergiye tabi olanların her nüshası** ayrı ayrı, **nispi vergiye tabi olanların ise sadece bir nüshası** vergiye tabidir. Nispi vergi 1.000.000 × binde 9,48 = **9.480 ₺**; üç nüshanın her biri vergilendirilseydi 28.440 ₺ bulunurdu.",
        '488 sayılı Damga Vergisi Kanunu m. 5',
    ),
    # düzey 3
    '0004': patch(
        "Bir kira sözleşmesine iki ayrı kişi ayrı ayrı adi kefil olarak imza atmıştır. Damga Vergisi Kanunu'na göre kefaletler için nasıl vergi alınır?",
        {
            'A': 'Kefaletler için maktu vergi alınır',
            'B': 'Kefil sayısı kadar vergi artırılır',
            'C': 'Adi kefaletlerden birinden vergi alınır',
            'D': 'Her kefaletten, kefil sayısı kadar ayrı ayrı vergi alınır',
            'E': 'Kefaletlerden vergi alınmaz',
        },
        'C',
        "6728 sayılı Kanunla m. 6'ya eklenen cümleye göre **bir kâğıt üzerinde birden fazla adi kefalet ve garanti taahhüdü bulunması hâlinde** bunlardan **birinden** damga vergisi alınır. Asıl işlem ayrıca vergilenir.",
        '488 sayılı Damga Vergisi Kanunu m. 6/3',
    ),
    # düzey 1
    '0005': patch(
        "Damga Vergisi Kanunu'na göre nispi ve maktu vergide vergilendirme ölçüsü sırasıyla aşağıdakilerden hangisidir?",
        {
            'A': 'Sözleşme süresi; nüsha sayısı',
            'B': 'Nüsha sayısı; imza sayısı',
            'C': 'Kâğıdın mahiyeti; belli para',
            'D': 'Belli para; kâğıdın mahiyeti',
            'E': 'Taraf sayısı; belli para',
        },
        'D',
        "m. 10'a göre damga vergisi nispi veya maktu alınır. **Nispi vergide kâğıtlarda yazılı belli para**, **maktu vergide kâğıtların mahiyeti** esastır. Belli para, kâğıdın içerdiği veya rakamlarının hâsıl edeceği paradır.",
        '488 sayılı Damga Vergisi Kanunu m. 10',
    ),
    # düzey 3
    '0006': patch(
        'Bir banka ile müşterisi arasında imzalanan cari hesap şeklindeki kredi sözleşmesinde kredi tutarı gösterilmemiştir. Sözleşme bankacılık kredisi istisnası dışında kalsaydı, vergi hangi tutara göre hesaplanırdı?',
        {
            'A': 'Sözleşme imza tarihindeki faiz tutarına',
            'B': 'Olayın ortaya çıktığı tarihte cari hesapta kayıtlı kredi miktarına',
            'C': 'Bankanın o yılki toplam kredi hacmine',
            'D': 'Müşterinin son yıl bilançosunda gösterilen öz kaynak ve kredi limitine',
            'E': 'Asgari maktu vergiye',
        },
        'B',
        "m. 11'e göre cari hesap şeklinde açılan kredilerle ikrazata ait taahhütname ve sözleşmelerde **ikraz edilen paranın veya azami haddinin gösterilmesi mecburidir**. Gösterilmezse vergi ve ceza, **olayın meydana çıktığı tarihte ilgili cari hesapta kayıtlı kredi miktarına** göre hesaplanır ve taraflar müteselsilen sorumludur.",
        '488 sayılı Damga Vergisi Kanunu m. 11',
    ),
    # düzey 2
    '0007': patch(
        'Damga vergisinde her bir kâğıt için uygulanan azami tutara ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Azami tutar kanunda sabittir ve yıllar itibarıyla değişmez',
            'B': '(1) sayılı tablodaki özel sınırlamalar saklıdır',
            'C': 'Cumhurbaşkanı artış oranını belirli sınırlar içinde belirleyebilir',
            'D': 'Azami tutar yeniden değerleme oranında artırılır',
            'E': 'Azami tutar her bir kâğıt için ayrı uygulanır',
        },
        'A',
        "m. 14'e göre her bir kâğıt için hesaplanacak vergi, (1) sayılı tablodaki sınırlamalar saklı kalmak üzere bir azami tutarı aşamaz. Bu tutar **her takvim yılı başından geçerli olmak üzere yeniden değerleme oranında artırılır**; Cumhurbaşkanı yeniden değerleme oranının %50 fazlasını geçmemek ve %20'sinden az olmamak üzere yeni oranlar belirleyebilir.",
        '488 sayılı Damga Vergisi Kanunu m. 14',
    ),
    # düzey 2
    '0008': patch(
        "Bedeli 1.000.000 ₺ olan ve vergisi ödenmiş bir hizmet sözleşmesinin süresi aynı bedelle bir yıl uzatılmıştır. Oranın binde 9,48 olduğu dikkate alınırsa süre uzatımı için ödenecek vergi kaç ₺'dir?",
        {
            'A': '2.370',
            'B': '4.740',
            'C': '7.110',
            'D': '9.480',
            'E': '0',
        },
        'D',
        "m. 14/3'e göre **mukavelenamelerin süresinin uzatılması hâlinde aynı miktar veya nispette vergi alınır**: 1.000.000 × binde 9,48 = **9.480 ₺**. Dörtte bir kuralı sözleşmenin devrinde ve akreditif süre uzatımında uygulanır.",
        '488 sayılı Damga Vergisi Kanunu m. 14/3',
    ),
    # düzey 2
    '0009': patch(
        "Basılı damga konulacak kâğıtlar için hesaplanan damga vergisi 100.000 ₺'dir. Vergi basılı damga şekliyle peşin ödenirse ödenecek tutar kaç ₺'dir?",
        {
            'A': '95.000',
            'B': '110.000',
            'C': '100.000',
            'D': '115.000',
            'E': '105.000',
        },
        'A',
        "m. 21'e göre basılı damga konulacak kâğıtların vergisi **yüzde beş noksanı ile peşin** ödenir: 100.000 × 0,95 = **95.000 ₺**.",
        '488 sayılı Damga Vergisi Kanunu m. 21',
    ),
    # düzey 2
    '0010': patch(
        "Damga vergisi ödenmemiş bir sözleşme, bir işlem için bankaya ibraz edilmiştir.\n\nDamga Vergisi Kanunu'na göre ibraz edenin sorumluluğuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İbraz eden vergiden sorumludur',
            'B': 'İbraz eden cezadan da sorumludur',
            'C': 'İbraz edenin mükelleflere rücu hakkı vardır',
            'D': 'Mükellef olmaması ibraz edenin sorumluluğunu kaldırmaz',
            'E': 'Banka ibrazı kabul ettiği için sorumluluk bankaya geçer',
        },
        'E',
        'DVK m. 24: vergiye tabi kâğıtların damga vergisinin ödenmemesinden veya noksan ödenmesinden doğan vergi ve cezadan, mükelleflere rücu hakkı olmak üzere kâğıtları ibraz edenler sorumludur; ibrazın kabul edilmesi sorumluluğu bankaya geçirmez.',
        '488 sayılı Damga Vergisi Kanunu m. 24',
    ),
    # düzey 2
    '0011': patch(
        "Vergi cezası kesilmesi gereken bir kâğıdın hamili, cezadan kurtulmak için kâğıdı terk etmiştir. Damga Vergisi Kanunu'na göre bu durum cezayı nasıl etkiler?",
        {
            'A': 'Cezanın alınmasına engel değildir',
            'B': 'Vergi aslını ortadan kaldırır',
            'C': 'Cezayı kaldırır; vergi aslı mükelleften aranır',
            'D': 'Cezayı yarıya indirir',
            'E': 'Cezayı ortadan kaldırır',
        },
        'A',
        "m. 28'e göre vergi cezası alınması gereken kâğıtların **hamilleri tarafından terk edilmesi bu cezanın alınmasına mani değildir**.",
        '488 sayılı Damga Vergisi Kanunu m. 28',
    ),
    # düzey 3
    '0012': patch(
        "Bir anonim şirket, genel müdürlük binası olarak kullanacağı taşınmazı aylık 50.000 ₺ bedelle iki yıllığına kiralamıştır. Kira sözleşmesi için binde 1,89 oran uygulanacağı dikkate alınırsa damga vergisi kaç ₺'dir?",
        {
            'A': '11.376',
            'B': '2.268',
            'C': '1.134',
            'D': '4.536',
            'E': '94,50',
        },
        'B',
        '(1) sayılı tablonun I-A-2 bendine göre kira mukavelenamelerinde vergi **mukavele süresine göre kira bedeli** üzerinden alınır: 50.000 × 24 = 1.200.000 ₺; 1.200.000 × binde 1,89 = **2.268 ₺**. Bir yıllık bedel esas alınırsa 1.134 ₺, genel sözleşme oranı uygulanırsa 11.376 ₺ bulunur.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo I-A-2',
    ),
    # düzey 3
    '0013': patch(
        "Bir işçinin aylık brüt ücreti 60.000 ₺'dir. Aylık brüt asgari ücretin 30.000 ₺ olduğu ve ücret makbuzlarına binde 7,59 oran uygulanacağı varsayılırsa bu ücret için damga vergisi kaç ₺'dir?",
        {
            'A': '227,70',
            'B': '568,80',
            'C': '455,40',
            'D': '284,40',
            'E': '0',
        },
        'A',
        "(1) sayılı tablonun IV-1-b bendine göre ücret makbuzları binde 7,59 oranında vergilenir. (2) sayılı tablonun IV-34 bendine göre GVK m. 23'teki ücretlere ilişkin kâğıtlar istisnadır ve **asgari ücret istisnasında istisna aylık brüt asgari ücrete isabet eden kısım için** uygulanır. Vergi: (60.000 − 30.000) × binde 7,59 = **227,70 ₺**. İstisna dikkate alınmazsa 455,40 ₺ bulunur.",
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo IV-1-b; (2) sayılı tablo IV-34',
    ),
    # düzey 2
    '0014': patch(
        "Trafik siciline kayıtlı ikinci el bir otomobilin 500.000 ₺ bedelle satışına ilişkin sözleşme için binde 1,89 oran uygulanacağı dikkate alınırsa damga vergisi kaç ₺'dir?",
        {
            'A': '4.740',
            'B': '945',
            'C': '472,50',
            'D': '1.890',
            'E': '3.795',
        },
        'B',
        '(1) sayılı tablonun I-A-6 bendine göre Karayolları Trafik Kanunu uyarınca kayıt ve tescil edilmiş **ikinci el araçların satış ve devrine ilişkin sözleşmeler binde 1,89** oranında vergilenir: 500.000 × binde 1,89 = **945 ₺**. Genel sözleşme oranı (binde 9,48) uygulanırsa 4.740 ₺ bulunur.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo I-A-6',
    ),
    # düzey 2
    '0015': patch(
        'Aşağıdaki kâğıtlardan hangileri maktu damga vergisine tabidir?\n\nI. Yıllık gelir vergisi beyannamesi\n\nII. İş yeri kira sözleşmesi\n\nIII. Ücret makbuzu',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'D',
        '(1) sayılı tabloya göre **vergi beyannameleri** (I) maktu vergiye tabidir. İş yeri kira sözleşmesi (II) süreye göre kira bedeli üzerinden binde 1,89; ücret makbuzu (III) ücret tutarı üzerinden binde 7,59 oranında **nispi** vergiye tabidir.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo',
    ),
    # düzey 3
    '0016': patch(
        'Ticari faaliyeti olmayan iki arkadaş arasında belli parayı içeren bir borç sözleşmesi imzalanmış, alacaklı bir süre sonra sözleşmeyi onaylatmak için notere ibraz etmiştir. Damga vergisi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gerçek kişiler arasında olduğu için vergi doğmaz',
            'B': 'Noter vergiyi ödeyip taraflara rücu eder',
            'C': 'Borç ödendiğinde vergiye tabi olur',
            'D': 'Notere ibraz tarihinde vergiye tabi olur; ibraz eden öder',
            'E': 'İmza tarihinde vergiye tabidir; taraflar müteselsilen ve eşit olarak öder',
        },
        'D',
        '(2) sayılı tablonun IV-34 bendine göre **ticari, zirai veya mesleki faaliyetlere ilişkin olmamak şartıyla gerçek kişiler arasında** düzenlenen akitlere ilişkin kâğıtlar istisnadır; ancak bu kâğıtlar **resmî dairelere veya noterlere ibraz edildiği takdirde bu tarih itibarıyla** vergiye tabi tutulur ve **ibraz edenlerce** ödenir.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-34',
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdaki kâğıtlardan hangileri damga vergisinden istisnadır?\n\nI. Sigorta sözleşmesi\n\nII. Kredi kartı üyelik sözleşmesi\n\nIII. Banka kredisinin teminatı için düzenlenen ipotek sözleşmesi\n\nIV. İki şirket arasındaki danışmanlık sözleşmesi',
        {
            'A': 'I, II, III ve IV',
            'B': 'I, III ve IV',
            'C': 'II ve IV',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'E',
        '(2) sayılı tabloya göre **sigorta sözleşmeleri** (IV-5), **kredi kartı üyelik sözleşmeleri** (IV-26) ve **bankalarca kullandırılan kredilerin teminatlarına** ilişkin kâğıtlar (IV-23) istisnadır. İki şirket arasındaki danışmanlık sözleşmesi (IV) istisna kapsamında değildir.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo',
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki kâğıtlardan hangisi damga vergisinden istisna değildir?',
        {
            'A': 'Velinin okul idaresine verdiği taahhütname',
            'B': 'Burs almak için öğrencinin verdiği taahhütname',
            'C': 'Okul ile veli arasında düzenlenen kayıt sözleşmesi',
            'D': 'Çıraklık sözleşmesi',
            'E': 'Özel okulun öğrenci servis firmasıyla yaptığı taşıma sözleşmesi',
        },
        'E',
        '(2) sayılı tablonun II-1 ve II-2 bentlerine göre çıraklık sözleşmeleri, burs ve öğrenim amacıyla verilen taahhütnameler ile **okul idareleriyle öğrenciler veya velileri arasında düzenlenen kâğıtlar** istisnadır. Okulun bir taşıma firmasıyla yaptığı ticari sözleşme bu kapsamda değildir.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo II-2',
    ),
    # düzey 2
    '0019': patch(
        'Tapu müdürlüğünde bir gayrimenkulün satışı nedeniyle düzenlenen ferağ ve intikal zaptı damga vergisi bakımından nasıl değerlendirilir?',
        {
            'A': 'Satış bedeli üzerinden binde 1,89 vergilenir',
            'B': 'Satış bedeli üzerinden binde 9,48 vergilenir',
            'C': 'Damga vergisinden istisnadır',
            'D': 'Maktu vergiye tabidir',
            'E': 'Alıcı ve satıcıdan ayrı ayrı vergi alınır',
        },
        'C',
        '(2) sayılı tablonun IV-7 bendine göre **gayrimenkullerin, ayni hakların ve gemilerin ferağ ve intikal zabıtları** damga vergisinden istisnadır; tapuda yapılan devir için ayrıca tapu harcı alınır.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-7',
    ),
    # düzey 2
    '0020': patch(
        "Damga Vergisi Kanunu'na göre nispi vergiye tabi makbuzların vergisinin istihkaktan kesinti yoluyla ödenmesine aşağıdakilerden hangisinin ödemelerinde izin verilebilir?",
        {
            'A': 'Bankaların',
            'B': 'Serbest meslek erbabının',
            'C': 'Adi ortaklıkların',
            'D': 'Basit usule tabi mükelleflerin',
            'E': 'Gerçek kişi tacirlerin',
        },
        'A',
        "m. 19'a göre **genel ve özel bütçeli daireler, il özel idareleri ve belediyeler, bankalar, iktisadi kamu teşekkülleri** ile bunların iştirak ve müesseselerinin ödemelerinde kullanılan nispi vergiye tabi makbuzların vergisinin ödeme veya avans sırasında istihkaktan kesinti yoluyla ödenmesine Maliye Bakanlığınca izin verilebilir.",
        '488 sayılı Damga Vergisi Kanunu m. 19',
    ),
    # düzey 2
    '0021': patch(
        "İmzalanmış olmakla birlikte Damga Vergisi Kanunu'na ekli (1) sayılı tabloda yer almayan bir kâğıt bulunmaktadır.\n\nBu kâğıtla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Damga vergisinin konusu (1) sayılı tabloyla sınırlıdır',
            'B': 'Tabloda yer almayan imzalı kâğıt maktu vergiye tabidir',
            'C': 'Tabloda yazılı kâğıtlar damga vergisine tabidir',
            'D': 'İmzalı olmak tek başına vergiyi doğurmaz',
            'E': 'Bu kâğıt damga vergisine tabi değildir',
        },
        'B',
        'DVK m. 1/1: Kanuna ekli (1) sayılı tabloda yazılı kâğıtlar damga vergisine tabidir. Verginin konusu tabloyla sınırlı olduğundan, imzalı olsa da tabloda yer almayan bir kâğıt nispi ya da maktu vergiye tabi değildir.',
        '488 sayılı Damga Vergisi Kanunu m. 1',
    ),
    # düzey 3
    '0022': patch(
        "Tarafların 'kira sözleşmesi' başlığıyla imzaladıkları bir kâğıtta, aslında taşınır bir malın mülkiyetinin bedel karşılığında kesin olarak devri düzenlenmiştir.\n\nDamga Vergisi Kanunu'na göre bu kâğıtla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Verginin tayininde kâğıdın mahiyetine bakılır',
            'B': 'Şekli belirtilmemiş kâğıtlarda yazının içerdiği hükme bakılır',
            'C': 'Kâğıda tarafların verdiği ad belirleyici değildir',
            'D': 'Kâğıt satış mahiyetine göre vergilendirilir',
            'E': 'Kâğıt başlığına göre kira sözleşmesi olarak vergilenir',
        },
        'E',
        'DVK m. 4: bir kâğıdın tabi olacağı verginin tayini için o kâğıdın mahiyetine bakılır; şekli kanunlarda belirtilmemiş kâğıtlarda üzerlerindeki yazının içerdiği hüküm ve manaya bakılır. Başlığın kira sözleşmesi olması sonucu değiştirmez; kâğıt satış olarak vergilenir.',
        '488 sayılı Damga Vergisi Kanunu m. 4',
    ),
    # düzey 2
    '0023': patch(
        "Maktu vergiye tabi, belli parayı içermeyen bir sulhname üç nüsha düzenlenmiştir. Bu kâğıt için maktu verginin 800 ₺ olduğu varsayılırsa ödenecek toplam vergi kaç ₺'dir?",
        {
            'A': '800',
            'B': '2.400',
            'C': '1.600',
            'D': '266',
            'E': '0',
        },
        'B',
        "m. 5'e göre maktu vergiye tabi kâğıtların **her bir nüshası ayrı ayrı aynı miktarda** vergiye tabidir: 800 × 3 = **2.400 ₺**. Nispi vergide ise yalnız bir nüsha vergilenir.",
        '488 sayılı Damga Vergisi Kanunu m. 5',
    ),
    # düzey 2
    '0024': patch(
        'Belli parayı içeren ve nispi vergiye tabi bir sözleşmeyi üç kişi imzalamıştır. Damga vergisi ve sorumluluk bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi imza sayısı kadar alınır',
            'B': 'Vergi imzacılar arasında eşit bölünür ve her biri kendi payından sorumludur',
            'C': 'Vergiyi ilk imzalayan öder',
            'D': 'Vergi artırılmış oranla alınır',
            'E': 'Vergi bir kez alınır; imzalayanlar müteselsilen sorumludur',
        },
        'E',
        "m. 7'ye göre kâğıtlara konulan imzanın birden fazla olması **verginin tekerrürünü gerektirmez**. m. 24'e göre birden fazla kişi tarafından imzalanan kâğıtlara ait vergi ve cezanın tamamından imza edenler **müteselsilen sorumludur**.",
        '488 sayılı Damga Vergisi Kanunu m. 7, 24',
    ),
    # düzey 3
    '0025': patch(
        "Maktu vergiye tabi bir ibra senedini üç kişi imzalamıştır. Damga Vergisi Kanunu'na göre vergi nasıl alınır?",
        {
            'A': 'İbra senetleri vergiden istisnadır',
            'B': 'İmzacılar arasında paylaştırılarak alınır',
            'C': 'Nispi orana dönüştürülerek alınır',
            'D': 'İmza adedine göre üç kez alınır',
            'E': 'İmza sayısına bakılmaksızın bir kez alınır',
        },
        'D',
        "m. 7'ye göre imzanın birden fazla olması kural olarak verginin tekerrürünü gerektirmez; ancak **maktu vergiye tabi olup birden fazla kişinin imzasını taşıyan makbuz ve ibra senetlerinin vergisi imza adedine göre** alınır. Bir tüzel kişi adına atılan birden fazla imza ise tek imza sayılır.",
        '488 sayılı Damga Vergisi Kanunu m. 7/2',
    ),
    # düzey 3
    '0026': patch(
        "Bedeli 1.000.000 ₺ olan ve vergisi ödenmiş bir sözleşmenin bedeli, diğer hükümleri de değiştirilerek 1.500.000 ₺'ye çıkarılmıştır. Oranın binde 9,48 olduğu dikkate alınırsa değişiklik için ödenecek vergi kaç ₺'dir?",
        {
            'A': '0',
            'B': '9.480',
            'C': '4.740',
            'D': '14.220',
            'E': '2.370',
        },
        'C',
        "m. 14/2'ye göre belli parayı içeren mukavelenamelerin değiştirilmesi hâlinde **artan miktar aynı nispette vergiye tabidir**: 500.000 × binde 9,48 = **4.740 ₺**. Yeni bedelin tamamı üzerinden hesaplanırsa 14.220 ₺ bulunur.",
        '488 sayılı Damga Vergisi Kanunu m. 14/2',
    ),
    # düzey 2
    '0027': patch(
        'Damga vergisinin hesaplanmasına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Akreditifin süresi uzatılırsa verginin tamamı yeniden alınır',
            'B': "Yabancı ülkeler arasında düzenlenip Türkiye'de tedavüle çıkan kâğıt yarı nispette vergilenir",
            'C': 'Sözleşmenin devrinde asıl verginin dörtte biri alınır',
            'D': 'Bedel artırılırsa artan kısım aynı nispette vergilenir',
            'E': 'Sözleşme süresi uzatılırsa aynı nispette vergi alınır',
        },
        'A',
        "m. 14'e göre **akreditif mektup ve telgraflarında süre uzatıldığında verginin dörtte biri** alınır. Mukavelename süresinin uzatılmasında aynı nispette vergi alınır, bedel artışında artan kısım vergilenir, devirde aslından alınan verginin dörtte biri alınır; yabancı memleketlerin birinden diğeri üzerine düzenlenip Türkiye'de tedavüle çıkarılan kâğıtlar yarı nispette vergilenir.",
        '488 sayılı Damga Vergisi Kanunu m. 14',
    ),
    # düzey 2
    '0028': patch(
        "Damga Vergisi Kanunu'na göre Cumhurbaşkanının (1) sayılı tablodaki nispi vergiler üzerindeki yetkisi aşağıdakilerden hangisidir?",
        {
            'A': 'On katına kadar artırmak, yarısına kadar indirmek',
            'B': 'İki katına kadar artırmak, yarıya indirmek',
            'C': 'Bir katına kadar artırmak, sıfıra kadar indirmek',
            'D': "Dört katına kadar artırmak, %1'e indirmek",
            'E': 'Oranları değiştirememek',
        },
        'C',
        "Mükerrer m. 30'a göre Cumhurbaşkanı, **maktu vergileri on katına** kadar artırmaya ve **yarısına** kadar indirmeye; **nispi vergileri bir katına kadar artırmaya ve sıfıra kadar indirmeye** yetkilidir. Maktu vergiler ayrıca her yıl yeniden değerleme oranında artırılır.",
        '488 sayılı Damga Vergisi Kanunu mük. m. 30',
    ),
    # düzey 2
    '0029': patch(
        "Maliye Bakanlığınca belirlenen mükellefler dışında kalan bir kişi, 3 Mayıs'ta damga vergisine tabi bir sözleşme imzalamıştır. Vergi en geç hangi tarihe kadar beyan edilip ödenmelidir?",
        {
            'A': '3 Haziran',
            'B': '31 Mayıs',
            'C': '20 Haziran',
            'D': '26 Haziran',
            'E': '18 Mayıs',
        },
        'E',
        "m. 22/b'ye göre (a) bendi dışındaki hâllerde vergi, **kâğıdın düzenlendiği tarihi izleyen on beş gün içinde** beyanname ile bildirilir ve aynı süre içinde ödenir: 3 Mayıs'ı izleyen on beş gün **18 Mayıs**'ta dolar.",
        '488 sayılı Damga Vergisi Kanunu m. 22/b',
    ),
    # düzey 3
    '0030': patch(
        'Bir noter tarafından düzenlenerek kişilere verilen bir kâğıdın damga vergisi hiç alınmamıştır. Vergi ve cezanın muhatabı kimdir?',
        {
            'A': 'Vergi ve ceza yarı yarıya paylaştırılır',
            'B': 'Vergi ve ceza mükellefe aittir; noterin görevi bildirimle sınırlıdır',
            'C': 'Vergi notere, ceza mükellefe aittir',
            'D': 'Vergi mükellefe, ceza kâğıdı düzenleyen notere aittir',
            'E': 'Vergi ve ceza notere aittir',
        },
        'D',
        "m. 24'e göre **resmî daireler veya noterlerce düzenlenerek** kişilere verilen veya dairede bırakılan ve damga vergisi alınmayan veya noksan alınan kâğıtların **vergisi mükelleflere, cezası düzenleyenlere** aittir; vergi ve ceza, vergi için mükellefe rücu hakkı olmak üzere düzenleyenlerden alınır.",
        '488 sayılı Damga Vergisi Kanunu m. 24/4',
    ),
    # düzey 2
    '0031': patch(
        'Vergisi ödenmemiş kâğıtlar karşısında noterler ve bankaların yükümlülüklerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Resmî daireler ibraz edilen kâğıdın vergisini arar',
            'B': 'Aykırı işlem yapan notere ayrıca ceza kesilir',
            'C': 'Bankalar vergisi ödenmemiş kâğıdı işleme koyamaz',
            'D': 'Noter, vergi ve cezası ödenmedikçe kâğıdın suretini veremez',
            'E': 'Noter, vergisi ödenmemiş kâğıdı tasdik edip vergiyi sonra tahsil edebilir',
        },
        'E',
        "m. 27'ye göre **noterler, damga vergisi ödenmemiş veya noksan ödenmiş kâğıtları vergi ve cezası ödenmedikçe tasdik edemez** veya suretlerini veremez; aksine işlem yapan notere ayrıca ceza kesilir. Bankalar ve KİT'ler de bu kâğıtları işleme koyamaz. m. 26'ya göre resmî daireler ibraz edilen kâğıtların vergisini aramakla yükümlüdür.",
        '488 sayılı Damga Vergisi Kanunu m. 26-27',
    ),
    # düzey 1
    '0032': patch(
        "Damga Vergisi Kanunu'nda hüküm bulunmayan usul konularında hangi kanunun damga resmine ilişkin hükümleri uygulanır?",
        {
            'A': 'Türk Borçlar Kanunu',
            'B': 'Amme Alacaklarının Tahsil Usulü Hakkında Kanun',
            'C': 'Gelir Vergisi Kanunu',
            'D': 'Vergi Usul Kanunu',
            'E': 'Harçlar Kanunu',
        },
        'D',
        "m. 30'a göre **Vergi Usul Kanunu'nun damga resmine ilişkin hükümleri** damga vergisi hakkında da uygulanır.",
        '488 sayılı Damga Vergisi Kanunu m. 30',
    ),
    # düzey 3
    '0033': patch(
        "Bir belediyenin yaptığı mal alımı ihalesi 2.000.000 ₺ bedelle bir şirkete verilmiş ve ihaleyi yapan idare ile sözleşme imzalanmıştır. İhale kararına binde 5,69, sözleşmeye binde 9,48 oran uygulanacağı dikkate alınırsa ödenecek toplam damga vergisi kaç ₺'dir?",
        {
            'A': '11.380',
            'B': '37.920',
            'C': '18.960',
            'D': '30.340',
            'E': '15.170',
        },
        'D',
        "(1) sayılı tabloya göre resmî daire ve kamu tüzel kişiliğini haiz kurumların **ihale kararları** binde 5,69 (II-2), **ihaleyi yapan idare ile düzenlenen sözleşmeler** binde 9,48 (I-A-9) oranında vergilenir: 2.000.000 × binde 5,69 = 11.380 ₺ ve 2.000.000 × binde 9,48 = 18.960 ₺; toplam **30.340 ₺**. Vergiyi m. 3'e göre şirket öder.",
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo I-A-9, II-2',
    ),
    # düzey 2
    '0034': patch(
        'Belli parayı içeren bir sözleşmenin feshine ilişkin fesihname için uygulanan damga vergisi oranı aşağıdakilerden hangisidir?',
        {
            'A': 'Binde 9,48',
            'B': 'Binde 7,59',
            'C': 'Maktu vergi',
            'D': 'Binde 5,69',
            'E': 'Binde 1,89',
        },
        'E',
        '(1) sayılı tablonun I-A-5 bendine göre **fesihnameler** (belli parayı içeren bir kâğıda taalluk edenler dâhil) **binde 1,89** oranında vergilenir. Mukavelenameler binde 9,48, ücret makbuzları binde 7,59, ihale kararları binde 5,69 oranındadır.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo I-A-5',
    ),
    # düzey 3
    '0035': patch(
        'Sermaye şirketlerine ilişkin kâğıtlarda damga vergisi istisnası bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kollektif şirketin kuruluş sözleşmesi de istisnadır',
            'B': 'Anonim şirket sermaye artırımına ilişkin kâğıtlar istisnadır',
            'C': "KVK'ya göre birleşme ve bölünme kâğıtları istisnadır",
            'D': 'Anonim şirketin süre uzatımına ilişkin kâğıtlar istisnadır',
            'E': 'Limited şirket pay devrine ilişkin kâğıtlar istisnadır',
        },
        'A',
        "(2) sayılı tablonun IV-16 bendine göre **anonim, eshamlı komandit ve limited şirketler ile yatırım fonlarının** kuruluş, pay devri, sermaye artırımı ve süre uzatımına ilişkin kâğıtlar; IV-17 bendine göre KVK'ya göre yapılan birleşme, devir ve bölünme kâğıtları istisnadır. **Kollektif şirket** bu sayımda yer almaz.",
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-16, 17',
    ),
    # düzey 2
    '0036': patch(
        'Bankaların kullandırdığı kredilere ilişkin damga vergisi istisnası bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yurt dışı kredi kuruluşlarının kredileri de kapsama girer',
            'B': 'Kredi teminatlarına ilişkin kâğıtlar istisnadır',
            'C': 'Kredinin geri ödenmesine ilişkin kâğıtlar istisnadır',
            'D': 'Kredinin devrine ilişkin kâğıtlar istisnadır',
            'E': 'Kredilerin kullanımına ilişkin kâğıtlar da istisnaya dâhildir',
        },
        'E',
        '(2) sayılı tablonun IV-23 bendine göre bankalar, yurt dışı kredi kuruluşları ve uluslararası kurumlarca kullandırılacak **kredilere, teminatlarına, geri ödenmelerine, devrine** ve kredi alacaklarının temlikine ilişkin kâğıtlar istisnadır; ancak parantez içinde **kredilerin kullanımları hariç** tutulmuştur.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-23',
    ),
    # düzey 2
    '0037': patch(
        'Aşağıdaki kâğıtlardan hangileri damga vergisinden istisnadır?\n\nI. İşçi ile işveren arasındaki bireysel iş sözleşmesi\n\nII. Anonim şirketin sermaye artırımına ilişkin kâğıtlar\n\nIII. İki şirket arasındaki mal satış sözleşmesi',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'B',
        '(2) sayılı tablonun III-1 bendine göre **bireysel ve toplu iş sözleşmeleri** (I), IV-16 bendine göre **anonim şirketlerin sermaye artırımına** ilişkin kâğıtlar (II) istisnadır. İki şirket arasındaki belli parayı içeren satış sözleşmesi (III) (1) sayılı tabloya göre binde 9,48 oranında vergiye tabidir.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo',
    ),
    # düzey 1
    '0038': patch(
        'İki bakanlık arasında imzalanan ve bir hizmetin yürütülmesine ilişkin protokol damga vergisi bakımından nasıl değerlendirilir?',
        {
            'A': 'Protokolü ilk imzalayan bakanlık vergiyi binde 9,48 oranında öder',
            'B': 'Maktu vergiye tabidir',
            'C': 'Noterce onaylanırsa vergilenir',
            'D': 'Binde 9,48 oranında vergilenir',
            'E': 'Resmî daireler arasındaki kâğıt olarak istisnadır',
        },
        'E',
        '(2) sayılı tablonun I-A-1 bendine göre **resmî daireler arasındaki işlemleri kapsayan her türlü kâğıt** ile bu dairelerin soruları üzerine kişilerce yazılan cevaplar damga vergisinden istisnadır.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo I-A-1',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdaki kâğıtlardan hangisi damga vergisinden istisnadır?',
        {
            'A': 'Şirketler arası yazılım lisans sözleşmesi',
            'B': 'İnşaat taahhüt sözleşmesi',
            'C': 'Anonim şirketin genel müdürüyle yaptığı danışmanlık sözleşmesi',
            'D': 'Faktoring şirketinin müşterisiyle yaptığı faktoring sözleşmesi',
            'E': 'İki şirket arasındaki reklam sözleşmesi',
        },
        'D',
        '(2) sayılı tablonun IV-20 bendine göre **faktoring şirketlerinin müşterileriyle yaptıkları faktoring sözleşmeleri** ve bunlara ilişkin kâğıtlar istisnadır; IV-19 bendine göre bankalar veya aracı kurumların taraf olduğu vadeli işlem ve opsiyon sözleşmeleri de istisnadır.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-19, 20',
    ),
    # düzey 2
    '0040': patch(
        'Toplu Konut İdaresi Başkanlığınca satılan konutlara ilişkin satış sözleşmelerinde damga vergisi istisnasının şartı aşağıdakilerden hangisidir?',
        {
            'A': 'Bedelin peşin ödenmesi',
            'B': "Konutun net alanının 80 m²'yi geçmemesi",
            'C': 'Konutun büyükşehirde bulunması',
            'D': 'Alıcının kamu görevlisi olması',
            'E': 'Alıcının ilk konutu olması',
        },
        'B',
        "(2) sayılı tablonun IV-39 bendine göre Toplu Konut İdaresi Başkanlığınca satışı yapılan ve **net alanı 80 m²'yi geçmeyen** konutlara ilişkin olarak İdare ile alıcı arasında imzalanan satış sözleşmeleri ve bu satışa ilişkin diğer kâğıtlar istisnadır.",
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-39',
    ),
    # düzey 3
    '0041': patch(
        "Almanya'da iki Türk şirketi arasında imzalanan belli parayı içeren bir satış sözleşmesi, Türkiye'de hangi durumda damga vergisine tabi tutulur?",
        {
            'A': 'Sözleşme süresi dolduğunda',
            'B': 'İmzalandığı anda',
            'C': "Türkiye'de resmî daireye ibraz edildiğinde",
            'D': 'Taraflar Türk şirketi olduğu için imza anında',
            'E': "Bedel Türkiye'ye transfer edildiğinde",
        },
        'C',
        "m. 1/3'e göre yabancı memleketlerde düzenlenen kâğıtlar, Türkiye'de **resmî dairelere ibraz edildiği, üzerinde devir veya ciro işlemi yapıldığı veya herhangi bir suretle hükümlerinden faydalanıldığı** takdirde vergiye tabi tutulur. m. 3/3'e göre vergiyi bu işlemleri yapanlar öder.",
        '488 sayılı Damga Vergisi Kanunu m. 1/3, 3/3',
    ),
    # düzey 2
    '0042': patch(
        "Damga vergisine tabi bir sözleşmenin süresini uzatmak için taraflar arasında yazışılan ve imzalanan bir mektup bulunmaktadır.\n\nDamga Vergisi Kanunu'na göre bu mektupla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sözleşmenin uzatılmasına ilişkin mektuplar vergiye tabidir',
            'B': 'Sözleşmenin değiştirilmesine ilişkin mektuplar vergiye tabidir',
            'C': 'Vergiye tabi kâğıtların yerini alan mektuplar vergiye tabidir',
            'D': 'Mektup biçiminde olduğu için vergi dışıdır',
            'E': 'Asıl sözleşmenin vergilenmiş olması mektubu vergi dışı bırakmaz',
        },
        'D',
        'DVK m. 2: vergiye tabi kâğıtlar mahiyetinde bulunan veya onların yerini alan mektup ve şerhlerle, bu kâğıtların hükümlerinin yenilenmesine, uzatılmasına, değiştirilmesine, devrine veya bozulmasına ilişkin mektup ve şerhler de damga vergisine tabidir.',
        '488 sayılı Damga Vergisi Kanunu m. 2',
    ),
    # düzey 3
    '0043': patch(
        "Bedeli 800.000 ₺ olan bir satış sözleşmesine, taraflardan başka bir üçüncü kişi aynı tutar için kefil olarak imza atmıştır. Oranın binde 9,48 olduğu dikkate alınırsa bu kâğıt için ödenecek toplam damga vergisi kaç ₺'dir?",
        {
            'A': '15.168',
            'B': '22.752',
            'C': '3.792',
            'D': '0',
            'E': '7.584',
        },
        'A',
        "m. 6'ya göre bir kâğıtta toplanan ve bir asıldan doğan işlemlerde en yüksek vergi alınır; ancak **asıl işlemin akitlerinden başka bir şahsın eklenen akit ve işlemi ayrıca vergiye tabidir**. Satış için 800.000 × binde 9,48 = 7.584 ₺, üçüncü kişinin kefaleti için de 7.584 ₺; toplam **15.168 ₺**.",
        '488 sayılı Damga Vergisi Kanunu m. 6',
    ),
    # düzey 2
    '0044': patch(
        "Bir satış sözleşmesinde, taraflardan biri yükümlülüğünü yerine getirmezse karşı tarafa ödeyeceği cezai şart kararlaştırılmıştır.\n\nDamga Vergisi Kanunu'na göre bu konuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Cezai şart ayrı bir sözleşmeye konu değilse vergi alınmaz',
            'B': 'Aynı kural pey akçesi için de uygulanır',
            'C': 'Aynı kural cayma tazminatı için de uygulanır',
            'D': 'Cezai şart için asıl sözleşmeye ek olarak ayrıca vergi alınır',
            'E': 'Asıl satış sözleşmesi vergiye tabidir',
        },
        'D',
        'DVK m. 6/4 (6728 sayılı Kanunla eklenen): pey akçesi, cayma tazminatı, ücret tevkifi, cezai şart gibi bir sözleşmenin müeyyidesi mahiyetindeki taahhütlerden, başlı başına bir sözleşmeye konu olmadıkça damga vergisi alınmaz; asıl sözleşme ise vergilenir.',
        '488 sayılı Damga Vergisi Kanunu m. 6/4',
    ),
    # düzey 2
    '0045': patch(
        "Aşağıdakilerden hangisi Damga Vergisi Kanunu'na göre resmî daire sayılmaz?",
        {
            'A': 'Özel bütçeli bir devlet üniversitesi',
            'B': 'Belediyeye bağlı, ayrı tüzel kişiliği olan otobüs A.Ş.',
            'C': 'Köy tüzel kişiliği',
            'D': 'İl özel idaresi',
            'E': 'Yatırım izleme ve koordinasyon başkanlığı',
        },
        'B',
        "m. 8'e göre resmî daire; **genel ve özel bütçeli idareler, il özel idareleri, yatırım izleme ve koordinasyon başkanlıkları, belediyeler ve köylerdir**. Bu dairelere bağlı olup **ayrı tüzel kişiliği bulunan iktisadi işletmeler** resmî daire sayılmaz.",
        '488 sayılı Damga Vergisi Kanunu m. 8',
    ),
    # düzey 1
    '0046': patch(
        'Damga vergisine tabi bir kâğıtta bedel yabancı para olarak yazılmıştır. Vergi matrahı Türk lirasına nasıl çevrilir?',
        {
            'A': 'Ödeme günündeki banka satış kuru üzerinden',
            'B': 'Sözleşmenin sona erdiği günkü kur üzerinden',
            'C': 'Tarafların sözleşmede kararlaştırdığı ve noterce onaylanan kur üzerinden',
            'D': 'Yılın son günündeki kur üzerinden',
            'E': 'Maliye Bakanlığınca ilan edilen fiyat üzerinden',
        },
        'E',
        "m. 12'ye göre damga vergisine tabi kâğıtlarda yazılı yabancı paralar **Maliye Bakanlığınca tayin ve ilan edilecek fiyat** üzerinden Türk parasına çevrilerek vergi alınır.",
        '488 sayılı Damga Vergisi Kanunu m. 12',
    ),
    # düzey 2
    '0047': patch(
        "Asıl sözleşmesi için 12.000 ₺ damga vergisi ödenmiş bir mukavelename başka bir kişiye devredilmiştir. Devir için alınacak vergi kaç ₺'dir?",
        {
            'A': '6.000',
            'B': '3.000',
            'C': '1.200',
            'D': '0',
            'E': '12.000',
        },
        'B',
        "m. 14/2'ye göre mukavelenamelerin devri hâlinde **aslından alınan verginin dörtte biri** alınır: 12.000 / 4 = **3.000 ₺**.",
        '488 sayılı Damga Vergisi Kanunu m. 14/2',
    ),
    # düzey 2
    '0048': patch(
        "Aşağıdakilerden hangisi günümüzde Damga Vergisi Kanunu'nda yer alan ödeme şekillerinden biri değildir?",
        {
            'A': 'Pul yapıştırılması',
            'B': 'Basılı damga konulması',
            'C': 'Makbuz karşılığı ödeme',
            'D': 'İstihkaktan kesinti yapılması',
            'E': 'Beyanname ile bildirilip makbuzla ödenmesi',
        },
        'A',
        "5281 sayılı Kanunla değişen m. 15'e göre damga vergisi **makbuz karşılığı, istihkaktan kesinti yapılması veya basılı damga konulması** şekillerinden biriyle ödenir. Pul yapıştırılmasına ilişkin m. 16 aynı Kanunla **yürürlükten kaldırılmıştır**.",
        '488 sayılı Damga Vergisi Kanunu m. 15-16',
    ),
    # düzey 2
    '0049': patch(
        'Maliye Bakanlığınca belirlenen mükellefler, bir ay içinde düzenledikleri kâğıtların damga vergisini ne zaman beyan edip öder?',
        {
            'A': "Ertesi ayın 26'sına kadar beyan, 28'ine kadar öder",
            'B': "Ertesi ayın 15'ine kadar beyan ve öder",
            'C': "Ertesi ayın 20'sine kadar beyan, 26'sına kadar öder",
            'D': 'Kâğıdın düzenlendiği gün beyan edip öder',
            'E': 'Yıl sonunda toplu beyan edip öder',
        },
        'C',
        "5281 sayılı Kanunla değişen m. 22/a'ya göre Bakanlıkça belirlenen mükellefler, kurum ve kuruluşlarca bir ay içinde düzenlenen kâğıtların vergisi **ertesi ayın 20'si akşamına kadar** beyanname ile bildirilir ve **26'sı akşamına kadar** ödenir.",
        '488 sayılı Damga Vergisi Kanunu m. 22/a',
    ),
    # düzey 3
    '0050': patch(
        'Damga vergisinden müstesna bir kurum ile bir anonim şirket arasında belli parayı içeren bir sözleşme imzalanmıştır. Sözleşmenin damga vergisi nasıl ödenir?',
        {
            'A': 'Kurum istisnalı olduğu için vergi alınmaz',
            'B': 'Vergi kurum ile şirket arasında paylaştırılır',
            'C': 'Şirket maktu vergi öder',
            'D': 'Şirket verginin yarısını öder',
            'E': 'Verginin tamamı şirket tarafından ödenir',
        },
        'E',
        "m. 24/2'ye göre birden fazla kişinin imzaladığı kâğıtlarda **aralarında vergiden müstesna olanların bulunması damga vergisinin noksan ödenmesini gerektirmez**; vergi, istisnası olmayan tarafça tam olarak ödenir.",
        '488 sayılı Damga Vergisi Kanunu m. 24/2',
    ),
    # düzey 3
    '0051': patch(
        "Yabancı bir ülkede düzenlenen bir poliçe Türkiye'de ilk kez bir tüccar tarafından kabul edilmiştir. Bu ticari kâğıdın damga vergisini kim öder?",
        {
            'A': 'Poliçeyi tahsil eden banka',
            'B': 'Poliçenin son hamili',
            'C': "Kâğıdı Türkiye'de ilk kabul eden veya kullanan kişi",
            'D': 'Vergi alınmaz',
            'E': 'Poliçeyi yabancı ülkede düzenleyen keşideci',
        },
        'C',
        "m. 3/3'e göre yabancı memleketlerde düzenlenen kâğıtlardan **ticari veya mütedavil** mahiyette olanların vergisini, **bunları Türkiye'de en evvel satan veya kabul veya başka suretle kullanan** kişiler öder. m. 25'e göre bu kâğıtların vergi ve cezası, mükelleflere rücu hakkı saklı kalmak üzere hamillerinden alınır.",
        '488 sayılı Damga Vergisi Kanunu m. 3/3, 25',
    ),
    # düzey 2
    '0052': patch(
        'Aşağıdaki kira sözleşmelerinden hangisi damga vergisinden istisna edilenlerden biri değildir?',
        {
            'A': 'Sabit üretim araçlarına ait kira sözleşmesi',
            'B': 'Basit usule tabi terzinin iş yeri kira sözleşmesi',
            'C': 'Anonim şirketin genel müdürlük binası için yaptığı kira sözleşmesi',
            'D': 'Derneğin yerleşim yeri olarak kiraladığı taşınmazın sözleşmesi',
            'E': 'Gerçek kişinin konut olarak kiraladığı dairenin sözleşmesi',
        },
        'C',
        '(2) sayılı tabloya göre **gerçek kişilerin mesken** olarak, dernek ve vakıfların yerleşim yeri olarak kiraladıkları ve iktisadi işletmeye dâhil olmayan taşınmazların kira sözleşmeleri (IV-31), muaf esnaf, muaf serbest meslek erbabı ve **basit usul** mükelleflerinin iş yeri kira sözleşmeleri (IV-32) ve **sabit üretim araçlarına ait kira sözleşmeleri** (IV-8) istisnadır. Anonim şirketin iş yeri kirası vergiye tabidir.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-8, 31, 32',
    ),
    # düzey 2
    '0053': patch(
        'Aşağıdaki sözleşmelerden hangisine uygulanan damga vergisi oranı Cumhurbaşkanı kararıyla sıfır olarak belirlenmiştir?',
        {
            'A': 'Resmî şekilde düzenlenen gayrimenkul satış vaadi sözleşmesi',
            'B': 'Paket tur sözleşmesi',
            'C': 'Mesafeli satış sözleşmesi',
            'D': '6502 sayılı Kanun kapsamında tüketiciyle yapılan taksitle satış sözleşmesi',
            'E': 'Toptan elektrik satış sözleşmesi',
        },
        'A',
        '(1) sayılı tabloda kanuni oranı binde 9,48 olan **resmî şekilde düzenlenen gayrimenkul satış vaadi sözleşmeleri** ile ön ödemeli konut satış sözleşmelerine uygulanacak oran 2017/9759 sayılı Kararla **sıfır** olarak belirlenmiştir; resmî kat karşılığı inşaat sözleşmelerinde de uygulanan oran sıfırdır. Taksitle satış, paket tur, mesafeli satış ve elektrik satış sözleşmeleri binde 9,48 oranındadır.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo I-A',
    ),
    # düzey 2
    '0054': patch(
        'Bir mükellef, kanuni beyan süresi içinde verdiği KDV beyannamesindeki hatayı düzeltmek için yine beyan süresi içinde ikinci bir beyanname vermiştir. Düzeltme beyannamesi için damga vergisi alınır mı?',
        {
            'A': 'İlk beyannamenin vergisi iade edilir',
            'B': 'Maktu vergi yeniden alınır',
            'C': 'Alınmaz; süre içindeki düzeltme beyannamesi hariçtir',
            'D': 'Nispi vergi alınır',
            'E': 'Maktu verginin yarısı alınır',
        },
        'C',
        '(1) sayılı tablonun IV-2-b bendine 6728 sayılı Kanunla eklenen hükme göre vergi beyannamelerinden, **beyanname verme süresi içerisinde düzeltme amacıyla verilen beyannameler hariç** tutulmuştur. Süresinden sonra verilen düzeltme beyannameleri ise maktu vergiye tabidir.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo IV-2-b',
    ),
    # düzey 3
    '0055': patch(
        'Aşağıdaki kâğıtlardan hangileri nispi damga vergisine tabidir?\n\nI. Belli parayı içeren kefalet senedi\n\nII. Resmî daireye ibraz edilen bilanço\n\nIII. Belediyenin ihale kararı\n\nIV. Konşimento',
        {
            'A': 'I, III ve IV',
            'B': 'I, II, III ve IV',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'II ve IV',
        },
        'D',
        '(1) sayılı tabloya göre belli parayı içeren **kefalet, teminat ve rehin senetleri** (I) binde 9,48 ve resmî dairelerin **ihale kararları** (III) binde 5,69 oranında nispi vergiye tabidir. Resmî dairelere ve bankalara ibraz edilen **bilançolar** (II) ile **konşimentolar** (IV) maktu vergiye tabidir.',
        '488 sayılı Damga Vergisi Kanunu (1) sayılı tablo',
    ),
    # düzey 2
    '0056': patch(
        'Kambiyo senetleri ve ticari kâğıtlara ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ciro, kabul ve tesellüm şerhleri istisnadır',
            'B': 'Hisse senedi ve tahvil kuponları istisnadır',
            'C': 'Poliçenin düzenlenen bütün nüshaları ayrı ayrı vergilenir',
            'D': 'Posta çekleri istisnadır',
            'E': 'Kambiyo senedi üzerindeki aval ve kefalet şerhleri istisnadır',
        },
        'C',
        "m. 5'e göre **poliçe ve emre yazılı ticari senetlerin yalnız tedavüle çıkarılan nüshaları** vergiye tabidir. (2) sayılı tabloya göre ticari kâğıtlar üzerindeki ciro, kabul ve tesellüm şerhleri (IV-1), hisse senedi ve tahvil kuponları (IV-3), posta çekleri (IV-6) ve kambiyo senetleri üzerindeki aval ve kefalet şerhleri (IV-29) istisnadır.",
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV',
    ),
    # düzey 2
    '0057': patch(
        'İşçilerle ilgili aşağıdaki kâğıtlardan hangisi damga vergisinden istisna değildir?',
        {
            'A': 'İşçinin işverenden ödünç aldığı para için verdiği makbuz',
            'B': 'Toplu iş sözleşmesi',
            'C': "İŞKUR'un işe yerleştirme için düzenlediği kâğıtlar",
            'D': 'Yer altı maden işçisinin yer altında çalıştığı güne ait ücret kâğıdı',
            'E': 'Bireysel iş sözleşmesi',
        },
        'A',
        "(2) sayılı tablonun III bölümüne göre iş sözleşmeleri, İŞKUR'un iş ve işçi bulmaya ilişkin kâğıtları ve **toprak altı madenlerinde yer altında çalışılan günlere ait ücret** kâğıtları istisnadır. **Ödünç alınan paralar için verilen makbuzlar** ise (1) sayılı tablonun IV-1-c bendine göre binde 7,59 oranında vergiye tabidir.",
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo III',
    ),
    # düzey 2
    '0058': patch(
        'Yatırım teşvik belgesi sahibi bir şirketin, belge kapsamındaki makineleri almak için üreticiyle imzaladığı sözleşme damga vergisi bakımından nasıl değerlendirilir?',
        {
            'A': 'Yatırım tamamlanınca vergilenir',
            'B': 'Damga vergisinden istisnadır',
            'C': 'Binde 9,48 oranında vergilenir',
            'D': 'Vergisi teşvik belgesiyle ertelenir',
            'E': 'Binde 1,89 oranında vergilenir',
        },
        'B',
        '(2) sayılı tablonun IV-43 bendine göre **yatırım teşvik belgesi kapsamındaki yatırım mallarına ilişkin olarak belge sahibi yatırımcılar ile bu malların üreticileri ve tedarikçileri arasında düzenlenen kâğıtlar** istisnadır.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-43',
    ),
    # düzey 2
    '0059': patch(
        "Aynı kâğıtta, birbirinden tamamen bağımsız bir makine satış sözleşmesi ile bir depo kira sözleşmesi yer almaktadır.\n\nDamga Vergisi Kanunu'na göre bu kâğıtla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Bağımsız akitlerin her birinden ayrı vergi alınır',
            'B': 'Kâğıt başına tek bir maktu vergi alınır',
            'C': 'Bağlı akitlerde en yüksek vergiyi gerektiren işlem esas alınır',
            'D': 'Akitlerin aynı kâğıtta bulunması vergiyi birleştirmez',
            'E': 'Bu kâğıtta iki ayrı vergi hesaplanır',
        },
        'B',
        'DVK m. 6/1: bir kâğıtta birbirinden tamamen ayrı birden fazla akit ve işlem bulunduğunda bunların her birinden ayrı ayrı vergi alınır. Akit ve işlemler birbirine bağlı ve bir asıldan doğmuşsa vergi en yüksek vergiyi gerektiren işlem üzerinden alınır.',
        '488 sayılı Damga Vergisi Kanunu m. 6/1',
    ),
    # düzey 2
    '0060': patch(
        'Bir gayrimenkul yatırım ortaklığının portföyüne almak üzere bir iş merkezi satın almasına ilişkin sözleşme damga vergisi bakımından nasıl değerlendirilir?',
        {
            'A': 'Damga vergisinden istisnadır',
            'B': 'Yarı oranda vergilenir',
            'C': 'Binde 9,48 oranında vergilenir',
            'D': 'Maktu vergiye tabidir',
            'E': 'Binde 1,89 oranında vergilenir',
        },
        'A',
        '(2) sayılı tablonun IV-21 bendine göre **gayrimenkul yatırım ortaklıklarının ve gayrimenkul yatırım fonlarının münhasıran gayrimenkul portföylerine ilişkin** alım satım sözleşmeleri ile gayrimenkul satış vaadi sözleşmeleri damga vergisinden istisnadır.',
        '488 sayılı Damga Vergisi Kanunu (2) sayılı tablo IV-21',
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
    print(f"1 paket / {len(PATCHES)} soru ('Damga Vergisi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
