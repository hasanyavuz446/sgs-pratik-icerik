#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Borcun Ifasi ve Sona Ermesi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (v192 hukuk bandi surumu mutlak ifadeli celdiriciler nedeniyle FATAL, kor %38): ifa kisi-konu-yer-zaman, sure hesaplari, odeme ve mahsup, makbuz, bagli haklar, ibra, yenileme, birlesme, takas, zamanasimi. Gercek sinav kaliplari (ifa yeri listesi, takas ve zamanasimi 'yanlis/dogru' listeleri, durma halleri listesi) olaylara ve tarih-tutar hesaplarina cevrildi; 15 hesap sorusu bagimsiz dogrulandi. Temerrut ve ifa imkansizligi temerrut paketindedir.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 83-105, 131-135, 139-161 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/borcun_ifasi_sona_ermesi.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "ifa-gen-"


def patch(stem, options, answer, solution, ref='6098 sayili Turk Borclar Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "A'nın B'ye olan 20.000 ₺'lik kira borcunu, A'nın haberi olmadan kardeşi C ödemek istemiştir. B, ödemeyi yalnız A'dan kabul edeceğini söyleyerek reddetmek istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Para borcunun bizzat borçluca ödenmesinde alacaklının kural olarak menfaati yoktur',
            'B': 'Borcun A tarafından şahsen ödenmesi zorunlu olduğundan B ödemeyi reddedebilir',
            'C': 'Borçlu, borcunu şahsen ifa etmekle kural olarak yükümlü değildir',
            'D': "C'nin ödemesi borcu sona erdirebilir",
            'E': 'Portre yapımı gibi kişisel edimlerde durum farklı olabilir',
        },
        'B',
        "TBK m. 83'e göre **borcun bizzat borçlu tarafından ifa edilmesinde alacaklının menfaati bulunmadıkça borçlu, borcunu şahsen ifa etmekle yükümlü değildir**. Para borcunda böyle bir menfaat kural olarak yoktur; ünlü bir ressamın portresi gibi kişisel edimlerde ise menfaat bulunabilir.",
        '6098 sayılı TBK m. 83',
    ),
    # düzey 3
    '0002': patch(
        "A, B ve C, belirli bir yarış atını D'ye teslim etmeyi birlikte üstlenmiştir; aralarında eşit paylıdırlar. At değeri 90.000 ₺'dir. Atı tek başına teslim eden A, diğer iki borçludan toplam kaç ₺ isteyebilir?",
        {
            'A': '60.000',
            'B': '90.000',
            'C': '0',
            'D': '45.000',
            'E': '30.000',
        },
        'A',
        "TBK m. 85'e göre **bölünemeyen borcun birden çok borçlusu varsa her biri borcun tamamını ifa etmekle yükümlüdür**; ifada bulunan borçlu alacaklıya halef olur ve **diğer borçlulardan payları oranında** isteyebilir: B ve C'nin payları 30.000 + 30.000 = **60.000 ₺**.",
        '6098 sayılı TBK m. 85',
    ),
    # düzey 2
    '0003': patch(
        "Para borcunun alacaklısı A, sözleşme yapıldığında İzmir'de, ödeme zamanında ise Ankara'da oturmaktadır. Borçlu B İstanbul'dadır. Taraflar ifa yerini kararlaştırmamıştır. Borç nerede ifa edilir?",
        {
            'A': 'Sözleşmenin yapıldığı yer',
            'B': 'İstanbul',
            'C': 'Ankara',
            'D': 'Borçlunun seçeceği yer',
            'E': 'İzmir',
        },
        'C',
        "TBK m. 89/1'e göre aksine anlaşma yoksa **para borçları alacaklının ödeme zamanındaki yerleşim yerinde** ifa edilir.",
        '6098 sayılı TBK m. 89/1',
    ),
    # düzey 2
    '0004': patch(
        "Adana'da oturan A, belirli bir kalite belirtmeden 100 ton kömür teslim etmeyi Konya'da oturan B'ye borçlanmıştır. A daha sonra Mersin'e taşınmıştır. İfa yeri kararlaştırılmamıştır. Borç nerede ifa edilir?",
        {
            'A': 'Konya',
            'B': 'Mersin',
            'C': 'Kömürün bulunduğu yer',
            'D': 'Adana',
            'E': "B'nin ödeme zamanındaki yerleşim yeri",
        },
        'D',
        "TBK m. 89/1'e göre para ve parça borçları dışındaki **bütün borçlar, doğumları sırasında borçlunun yerleşim yerinde** ifa edilir. Çeşit borcu doğduğunda A Adana'da oturmaktadır.",
        '6098 sayılı TBK m. 89/1',
    ),
    # düzey 3
    '0005': patch(
        "31 Ocak'ta kurulan bir sözleşmede borcun 'bir ay sonra' ifa edileceği kararlaştırılmıştır. Yıl artık yıl değildir. Vade hangi gündür?",
        {
            'A': '2 Mart',
            'B': '27 Şubat',
            'C': '3 Mart',
            'D': '1 Mart',
            'E': '28 Şubat',
        },
        'E',
        "TBK m. 92/1-3'e göre ay olarak belirlenen süre, sözleşmenin kurulduğu gün ayın kaçıncı günü ise **son ayın bunu karşılayan gününde** dolar; **son ayda bunu karşılayan gün yoksa süre bu ayın son günü dolmuş sayılır**: 28 Şubat.",
        '6098 sayılı TBK m. 92',
    ),
    # düzey 2
    '0006': patch(
        'Vadenin belirlenmesine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Gün belirtilmeksizin yalnız ay belirlenmişse o ayın son günü anlaşılır\n\nII. Sekiz gün olarak belirlenen süre bir haftayı ifade eder\n\nIII. Son gün tatile rastlarsa süre tatili izleyen ilk iş gününe geçer',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'A',
        "TBK m. 91'e göre yalnız ay belirlenmişse **ayın son günü** anlaşılır (I). m. 92'ye göre **sekiz gün bir haftayı değil tam sekiz günü** ifade eder (II yanlış). m. 93'e göre son gün tatile rastlarsa **izleyen ilk iş gününe** geçer (III).",
        '6098 sayılı TBK m. 91-93',
    ),
    # düzey 3
    '0007': patch(
        'Vadeli satışta satıcı malı teslim etmeden önce, alıcı hakkındaki icra takiplerinde hacizlerin sonuçsuz kaldığını öğrenmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Alıcının ifa güçsüzlüğü satıcıya ödemezlik hakkı verir',
            'B': 'Satıcı bedel güvence altına alınıncaya kadar teslimden kaçınabilir',
            'C': 'Satıcının hakkı tehlikeye düşmüştür',
            'D': 'Satıcı, teslim borcunu öne alarak derhâl ifa etmekle yükümlüdür',
            'E': 'Uygun sürede güvence verilmezse satıcı sözleşmeden dönebilir',
        },
        'D',
        "TBK m. 98'e göre taraflardan birinin **ifada güçsüzlüğe düşmesi, özellikle iflas etmesi ya da hakkındaki haciz işleminin sonuçsuz kalması** sebebiyle diğer tarafın hakkı tehlikeye düşerse, bu taraf karşı edimin ifası **güvence altına alınıncaya kadar** kendi ediminden kaçınabilir; uygun sürede güvence verilmezse sözleşmeden dönebilir.",
        '6098 sayılı TBK m. 98',
    ),
    # düzey 2
    '0008': patch(
        "Faiz ve giderleri ödemede gecikmemiş olan borçlu, 100.000 ₺'lik ana borcu için 30.000 ₺ kısmi ödeme yapmış ve bunun ana borçtan düşülmesini istemiştir. Sözleşmede aksine bir kayıt vardır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ödemenin nereye sayılacağını alacaklı belirler',
            'B': 'Ödeme ana borçtan düşülür; aksine kayıt geçersizdir',
            'C': 'Ödeme giderlere mahsup edilir',
            'D': 'Kısmi ödeme kabul edilemez',
            'E': 'Aksine kayıt geçerli olduğundan ödeme önce faize sayılır',
        },
        'B',
        "TBK m. 100/1'e göre **borçlu, faiz veya giderleri ödemede gecikmemiş ise, kısmen yaptığı ödemeyi ana borçtan düşme hakkına sahiptir; aksine anlaşma yapılamaz**.",
        '6098 sayılı TBK m. 100',
    ),
    # düzey 2
    '0009': patch(
        "Borcunu tamamen ödemek isteyen borçluya alacaklı, borç senedini kaybettiğini söylemiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Borçlu, senedin iptalini gösteren bir belge isteyebilir',
            'B': 'Belge resmen düzenlenmiş ya da usulüne göre onaylanmış olmalıdır',
            'C': 'Belge borcun sona erdiğini de göstermelidir',
            'D': 'Belge borçlunun istemi üzerine verilir',
            'E': 'Senet bulunmadıkça borçlu ödeme yapamaz; borç askıda kalır',
        },
        'E',
        'TBK m. 105: alacaklı borç senedini kaybettiğini iddia ederse borçlu, ödeme sırasında alacaklıdan senedin iptalini ve borcun sona ermiş olduğunu gösteren, resmen düzenlenmiş veya usulüne göre onaylanmış bir belge vermesini isteyebilir; borç askıda kalmaz.',
        '6098 sayılı TBK m. 105',
    ),
    # düzey 3
    '0010': patch(
        "10 Ocak'ta kurulan bir sözleşmede borcun 'bir buçuk ay içinde' ifa edileceği kararlaştırılmıştır. Süre hangi gün dolar?",
        {
            'A': '25 Şubat',
            'B': '10 Şubat',
            'C': '28 Şubat',
            'D': '24 Şubat',
            'E': '1 Mart',
        },
        'A',
        "TBK m. 92/1-4'e göre **yarım aydan on beş günlük süre** anlaşılır; bir veya birden çok ay ve yarım ay olarak belirlenmiş sürenin dolduğu gün, **son aya on beş gün eklenerek** belirlenir: bir ay 10 Şubat'ta dolar, buna 15 gün eklenir → **25 Şubat**.",
        '6098 sayılı TBK m. 92/1-4',
    ),
    # düzey 3
    '0011': patch(
        'Kiracı, birikmiş kira borcu için kiraya verene bir bono vermiştir. Taraflar yenileme konusunda açık bir irade açıklamamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kiraya veren hem kira ilişkisine hem bonoya dayanabilir',
            'B': 'Mevcut borç için kambiyo taahhüdü kural olarak yenileme sayılmaz',
            'C': 'Kira borcu varlığını sürdürür',
            'D': 'Yenileme ancak tarafların açık iradesiyle olur',
            'E': 'Bono verilmesiyle kira borcu yenilenmiş ve sona ermiştir',
        },
        'E',
        "TBK m. 133'e göre yeni bir borçla mevcut borcun sona erdirilmesi **ancak tarafların bu yöndeki açık iradesiyle** olur; özellikle **mevcut borç için kambiyo taahhüdünde bulunulması**, açık yenileme iradesi olmadıkça yenileme sayılmaz.",
        '6098 sayılı TBK m. 133',
    ),
    # düzey 2
    '0012': patch(
        'Oğul, babasına 200.000 ₺ borçludur. Baba ölmüş ve tek mirasçısı olan oğul mirası kabul etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Alacaklı ve borçlu sıfatları oğulda birleşmiştir',
            'B': 'Oğul, mirasçı sıfatıyla borcu kendine ödemeye devam eder',
            'C': 'Borç birleşmeyle sona erer',
            'D': 'Oğul mirası reddetseydi borç varlığını sürdürürdü',
            'E': 'Alacak üzerinde önceden hakkı olan üçüncü kişiler etkilenmez',
        },
        'B',
        "TBK m. 135'e göre **alacaklı ve borçlu sıfatlarının aynı kişide birleşmesiyle borç sona erer**; üçüncü kişilerin önceden mevcut hakları etkilenmez; birleşme geçmişe etkili olarak ortadan kalkarsa borç varlığını sürdürür.",
        '6098 sayılı TBK m. 135',
    ),
    # düzey 3
    '0013': patch(
        "A ile B'nin karşılıklı para alacakları 2014'te muaccel olmuş ve o tarihte takas edilebilir hâle gelmiştir. A'nın alacağı 2024'te zamanaşımına uğramıştır. B, 2026'da A'dan alacağını istemiş; A takas bildiriminde bulunmuştur. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A takası ileri sürebilir; o anda süre dolmamıştı',
            'B': 'Zamanaşımına uğramış alacak takas konusu yapılamaz',
            'C': "A'nın alacağı zamanaşımına uğradığından takas ileri sürülemez",
            'D': 'A, alacağının yarısını takas edebilir',
            'E': "Takas ancak B'nin rızasıyla yapılabilir",
        },
        'A',
        "TBK m. 139/3'e göre **zamanaşımına uğramış bir alacağın takası, ancak takas edilebileceği anda henüz zamanaşımına uğramamış olması koşuluyla** ileri sürülebilir. Alacaklar 2014'te takas edilebilir iken A'nın alacağı henüz zamanaşımına uğramamıştı.",
        '6098 sayılı TBK m. 139/3',
    ),
    # düzey 3
    '0014': patch(
        "İşveren, işçisine verdiği 30.000 ₺'lik borç parayı, işçinin rızası olmadan onun aylık ücretinden takas etmek istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'İşçi ücreti bakım için zorunlu bir alacaktır',
            'B': 'Takas ancak işçinin rızasıyla yapılabilir',
            'C': 'Nafaka alacakları da aynı kurala tabidir',
            'D': 'Borçlar karşılıklı ve muaccel olduğundan işveren tek başına takas edebilir',
            'E': 'Tevdi edilen eşyanın iadesi alacağı da rızasız takas edilemez',
        },
        'D',
        "TBK m. 144'e göre **nafaka ve işçi ücreti gibi, borçlunun ve ailesinin bakımı için zorunlu** alacaklar ile tevdi edilmiş veya haksız alınmış eşyanın iadesine ilişkin alacaklar, **ancak alacaklıların rızasıyla** takas edilebilir.",
        '6098 sayılı TBK m. 144',
    ),
    # düzey 2
    '0015': patch(
        'Aşağıdakilerden hangileri takasın koşullarındandır?\n\nI. Tarafların karşılıklı olarak birbirine borçlu olması\n\nII. Borçların konusunun para veya özdeş edim olması\n\nIII. Her iki alacağın da çekişmesiz olması',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'C',
        "TBK m. 139'a göre takas için **karşılıklılık** (I), **para veya özdeş edimler** (II) ve kural olarak her iki borcun **muaccel** olması gerekir. m. 139/2'ye göre **alacaklardan biri çekişmeli olsa bile takas ileri sürülebilir** (III gerekli değildir).",
        '6098 sayılı TBK m. 139',
    ),
    # düzey 2
    '0016': patch(
        'Aşağıdaki alacaklardan hangileri beş yıllık zamanaşımına tabidir?\n\nI. Lokantada yenen yemeğin bedeli\n\nII. Ticari simsarlık ücreti alacağı\n\nIII. Bir fabrikanın toptan sattığı makinenin bedeli',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'A',
        "TBK m. 147'ye göre **lokanta ve benzeri yerlerdeki yeme içme bedelleri** (I) beş yıllık zamanaşımına tabidir. m. 147/5 simsarlık alacaklarını beş yıla bağlarken **ticari simsarlık ücreti alacağını** hariç tutar (II); küçük çapta perakende olmayan satış bedeli de (III) m. 146'daki on yıllık zamanaşımına tabidir.",
        '6098 sayılı TBK m. 147',
    ),
    # düzey 3
    '0017': patch(
        "Ömür boyu gelir sözleşmesinde gelir borçlusu, 1 Mart 2015'te muaccel olan taksitten itibaren hiçbir ödeme yapmamıştır. Alacağın tamamı için zamanaşımı hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sözleşmenin kurulduğu tarihte başlar',
            'B': 'Son taksitin muaccel olduğu tarihte başlar',
            'C': 'İfa edilmeyen ilk taksitin muaccel olduğu gün başlar',
            'D': 'Her taksit için ayrı ayrı ve o taksitle sınırlı işler',
            'E': 'Gelir alacaklısının ölümüyle başlar',
        },
        'C',
        "TBK m. 150'ye göre **ömür boyunca gelir ve benzeri dönemsel edimlerde, alacağın tamamı için zamanaşımı, ifa edilmemiş ilk dönemsel edimin muaccel olduğu günde** işlemeye başlar; alacağın tamamı zamanaşımına uğrarsa ifa edilmemiş dönemsel edimler de zamanaşımına uğrar.",
        '6098 sayılı TBK m. 150',
    ),
    # düzey 3
    '0018': patch(
        'Beş yıllık zamanaşımına tabi bir kira alacağı mahkeme kararına bağlanmış ve karar kesinleşmiştir. Karar sonrasında işleyecek yeni zamanaşımı süresi kaç yıldır?',
        {
            'A': '20',
            'B': '10',
            'C': '5',
            'D': '2',
            'E': '1',
        },
        'B',
        "TBK m. 156/2'ye göre **borç bir senetle ikrar edilmiş veya bir mahkeme ya da hakem kararına bağlanmış ise, yeni süre her zaman on yıldır**; alacağın önceki süresinin beş yıl olması sonucu değiştirmez.",
        '6098 sayılı TBK m. 156/2',
    ),
    # düzey 3
    '0019': patch(
        'Bir alacak, alacaklıya teslim edilmiş bir altın kolye üzerindeki taşınır rehniyle güvence altındadır. Alacak zamanaşımına uğramıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Alacaklı kolyeyi paraya çevirterek alacağını alabilir',
            'B': 'Alacaklının hakkını rehinden alma yetkisi devam eder',
            'C': 'Borçlu zamanaşımını ileri sürebilir',
            'D': 'Taşınır rehni zamanaşımının işlemesine engel olmaz',
            'E': 'Rehin bulunduğundan zamanaşımı işlemez',
        },
        'E',
        "TBK m. 159'a göre **alacağın bir taşınır rehniyle güvenceye bağlanmış olması, zamanaşımının işlemesine engel olmaz; bununla birlikte alacaklının hakkını rehinden alma yetkisi devam eder**.",
        '6098 sayılı TBK m. 159',
    ),
    # düzey 3
    '0020': patch(
        "A, 2015 yılında B'ye süre belirlemeden ödünç para vermiş; ödünç alan ancak bildirim üzerine geri vermekle yükümlüdür. A, parayı hiç istememiştir. Zamanaşımının başlangıcı hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bildirimden itibaren beş yıl sonra başlar',
            'B': 'Ödünç alanın parayı harcadığı gün başlar',
            'C': 'Bildirimin yapılabileceği günden işlemeye başlar',
            'D': 'Alacaklı bildirim yapmadıkça zamanaşımı işlemeye başlamaz',
            'E': 'Alacaklının ölümüyle işlemeye başlar',
        },
        'C',
        "TBK m. 149/2'ye göre **alacağın muaccel olmasının bir bildirime bağlı olduğu hâllerde, zamanaşımı bu bildirimin yapılabileceği günden** işlemeye başlar; alacaklının bildirimi geciktirmesi başlangıcı ertelemez.",
        '6098 sayılı TBK m. 149/2',
    ),
    # düzey 2
    '0021': patch(
        'Borcun tamamı 100.000 ₺ olarak belli ve muaccel iken borçlu, alacaklıya yalnız 40.000 ₺ ödemeyi önermiştir. Alacaklının durumu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ancak borçlunun rızasıyla reddedebilir',
            'B': 'Kısmen ifayı kabul etmekle yükümlüdür',
            'C': 'Kısmi ödemeyi kabul ederse kalan alacağından vazgeçmiş olur',
            'D': 'Reddederse alacaklı temerrüdüne düşer',
            'E': 'Alacaklı kısmen ifayı haklı olarak reddedebilir',
        },
        'E',
        "TBK m. 84/1'e göre **borcun tamamı belli ve muaccel ise alacaklı kısmen ifayı reddedebilir**; bu ret haklı bir sebebe dayandığından alacaklı temerrüdü doğmaz.",
        '6098 sayılı TBK m. 84/1',
    ),
    # düzey 2
    '0022': patch(
        "A, B'ye olan borcunu 'ya 10 ton demir teslim ederek ya da 200.000 ₺ ödeyerek' yerine getirmeyi üstlenmiştir. Sözleşmede seçimin kime ait olduğu belirtilmemiştir. Seçim kime aittir?",
        {
            'A': 'Hâkime',
            'B': 'Taraflara birlikte',
            'C': "Borçlu A'ya",
            'D': 'Ödeme gününde yüksek değerli olana',
            'E': "Alacaklı B'ye",
        },
        'C',
        "TBK m. 87'ye göre **seçimlik borçlarda**, hukuki ilişkiden ve işin özelliğinden aksi anlaşılmadıkça **edimlerden birinin seçimi borçluya** aittir.",
        '6098 sayılı TBK m. 87',
    ),
    # düzey 3
    '0023': patch(
        "Bir kapital faizi borcunun doğduğu tarihte mevzuata göre yıllık faiz oranı %24'tür. Taraflar sözleşmeyle en fazla yıllık yüzde kaçlık faiz kararlaştırabilir?",
        {
            'A': '%36',
            'B': '%48',
            'C': '%24',
            'D': '%30',
            'E': '%72',
        },
        'A',
        "TBK m. 88/2'ye göre **sözleşmeyle kararlaştırılacak yıllık faiz oranı**, faiz borcunun doğduğu tarihte mevzuata göre belirlenen **yıllık faiz oranının yüzde elli fazlasını aşamaz**: 24 × 1,5 = **%36**.",
        '6098 sayılı TBK m. 88',
    ),
    # düzey 2
    '0024': patch(
        "Bir sözleşmede borcun 'Mayıs ayının ortasında', diğer bir borcun ise yalnızca 'Haziran ayında' ifa edileceği kararlaştırılmıştır. Vadeler sırasıyla hangi günlerdir?",
        {
            'A': '31 Mayıs ve 30 Haziran',
            'B': '15 Mayıs ve 30 Haziran',
            'C': '14 Mayıs ve 15 Haziran',
            'D': '15 Mayıs ve 1 Haziran',
            'E': '16 Mayıs ve 1 Haziran',
        },
        'B',
        "TBK m. 91'e göre **ayın ortası belirlenmişse ayın on beşinci günü**, **gün belirtilmeksizin sadece ay belirlenmişse o ayın son günü** anlaşılır.",
        '6098 sayılı TBK m. 91',
    ),
    # düzey 3
    '0025': patch(
        "10 Mayıs'ta dolacak ifa süresi, taraflarca başka bir kayıt konulmadan 15 gün uzatılmıştır. Yeni süre hangi gün dolar?",
        {
            'A': '26 Mayıs',
            'B': '15 Mayıs',
            'C': '10 Haziran',
            'D': '25 Mayıs',
            'E': '24 Mayıs',
        },
        'D',
        "TBK m. 95'e göre süre uzatılmışsa yeni süre, aksi kararlaştırılmış olmadıkça, **önceki sürenin sona ermesini izleyen birinci günden** başlar: 11 Mayıs birinci gün olmak üzere 15. gün **25 Mayıs**'tır.",
        '6098 sayılı TBK m. 95',
    ),
    # düzey 2
    '0026': patch(
        'Peşin satış sözleşmesinde alıcı, bedeli ödemeden ve ödemeyi önermeden malın teslimini istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Satıcı, alıcı ödemese de malı derhâl teslim etmekle yükümlüdür',
            'B': 'Alıcı kendi borcunu ifa etmeden karşı edimi isteyemez',
            'C': "Satıcı ödemezlik def'i ileri sürebilir",
            'D': 'Sözleşme karşılıklı borç yükleyen bir sözleşmedir',
            'E': 'Alıcı ödemeyi önerirse satıcı teslimden kaçınamaz',
        },
        'A',
        "TBK m. 97'ye göre karşılıklı borç yükleyen sözleşmenin ifasını isteyen taraf, daha sonra ifa etme hakkı olmadıkça **kendi borcunu ifa etmiş ya da ifasını önermiş olmalıdır**; aksi hâlde karşı taraf ifadan kaçınabilir (ödemezlik def'i).",
        '6098 sayılı TBK m. 97',
    ),
    # düzey 3
    '0027': patch(
        "Sözleşmede 'aynen ödeme' kaydı bulunmayan 10.000 USD'lik borç vadesinde ödenmemiştir. Vade günü kur 32 ₺, fiili ödeme günü kur 35 ₺'dir. Alacaklı fiili ödeme günündeki rayici seçerse Türk lirası olarak kaç ₺ ister?",
        {
            'A': '300.000',
            'B': '335.000',
            'C': '320.000',
            'D': '10.000',
            'E': '350.000',
        },
        'E',
        "TBK m. 99/3'e göre yabancı para borcu ödeme gününde ödenmezse alacaklı, alacağının **aynen veya vade ya da fiilî ödeme günündeki rayiç** üzerinden Türk lirasıyla ödenmesini isteyebilir: 10.000 × 35 = **350.000 ₺**.",
        '6098 sayılı TBK m. 99/3',
    ),
    # düzey 3
    '0028': patch(
        'Borçlunun aynı alacaklıya karşı vadesi henüz gelmemiş iki borcu vardır; biri ipotekle güvence altında, diğeri güvencesizdir. Borçlu açıklama yapmadan ödeme yapmış, makbuzda da açıklık yoktur. Ödeme hangi borca sayılır?',
        {
            'A': 'Alacaklının dilediği borca',
            'B': 'Güvencesiz borca',
            'C': 'İpotekli borca',
            'D': 'İki borca orantılı olarak',
            'E': 'Vadesi daha uzak olana',
        },
        'B',
        "TBK m. 102/2'ye göre **borçlardan hiçbirinin vadesi gelmemişse ödeme, güvencesi en az olan borç için** yapılmış sayılır.",
        '6098 sayılı TBK m. 102',
    ),
    # düzey 2
    '0029': patch(
        'Ödeme ve makbuza ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çekincesiz makbuz önceki dönem kiralarının ödendiği sonucunu doğurur',
            'B': 'Borcun tamamını ödeyen borçlu senedin geri verilmesini isteyebilir',
            'C': 'Anapara makbuzu, faizlerin alındığı sonucunu doğurmaz',
            'D': 'Kısmi ödemede borçlu makbuz ve ödemenin senede işlenmesini isteyebilir',
            'E': 'Borç senedinin borçluya geri verilmesi borcun sona erdiği sonucunu doğurur',
        },
        'C',
        "TBK m. 104/2'ye göre **alacaklı anaparanın tamamı için makbuz vermişse, faizlerini de almış olduğu kabul edilir**; senet borçluya geri verilmişse borç sona ermiş sayılır. m. 103 senedin iadesi ve kısmi ödemeyi düzenler.",
        '6098 sayılı TBK m. 103, 104',
    ),
    # düzey 2
    '0030': patch(
        "Teslim borcu olan satıcı, malı gece saat 23.00'te alıcının kapalı olan dükkânına getirmiş; alıcı teslim almayı reddetmiştir. Taraflar arasında teslim saatine ilişkin bir anlaşma yoktur. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Teslim her saatte yapılabilir',
            'B': 'Alıcı haklı olarak reddedebilir',
            'C': 'Satıcı malı kapının önüne bırakarak borcundan kurtulur',
            'D': 'Alıcı teslim almakla yükümlüdür; aksi hâlde temerrüde düşer',
            'E': 'Ret nedeniyle sözleşme sona erer',
        },
        'B',
        "TBK m. 94'e göre **borç, alışılmış iş saatlerinde ifa ve kabul edilir**. İş saatleri dışındaki öneriyi reddeden alacaklı haklı sebebe dayandığından temerrüde düşmez.",
        '6098 sayılı TBK m. 94',
    ),
    # düzey 3
    '0031': patch(
        'İki tacir arasında işleyen cari hesaba çeşitli kalemler kaydedilmiş; yıl sonunda hesap kesilmiş ve bakiye karşı tarafça kabul edilmiştir. Kalemlerden biri ipotekle güvence altındadır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Aksi kararlaştırılmadıkça ipotek güvencesi devam eder',
            'B': 'Hesap kesilip bakiye kabul edilince borç yenilenir',
            'C': 'Kalemlerin kaydı tek başına yenileme sayılmaz',
            'D': 'Kalemlerin cari hesaba kaydıyla borçlar yenilenmiş olur',
            'E': 'Bakiye üzerinden yeni bir borç doğmuştur',
        },
        'D',
        "TBK m. 134'e göre kalemlerin cari hesaba **sadece kaydedilmesi yenileme değildir**; **hesabın kesilmiş ve sonucun diğer tarafça kabul edilmiş** olmasıyla borç yenilenir. Kalemlerden birinin güvencesi varsa, aksi kararlaştırılmadıkça **güvence sona ermez**.",
        '6098 sayılı TBK m. 134',
    ),
    # düzey 3
    '0032': patch(
        'Babasının tek mirasçısı olan ve babasına borçlu bulunan oğul, mirası yasal süresi içinde reddetmiştir. Oğulun babasına olan borcu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Borç mirasın reddiyle yarıya iner',
            'B': 'Birleşme geçmişe etkili kalktığından borç sürer',
            'C': 'Birleşmeyle bir kez sona eren borç, mirasın reddedilmesiyle yeniden doğmaz',
            'D': 'Borç ancak alacaklılar isterse canlanır',
            'E': 'Borç Hazineye devredilerek sona erer',
        },
        'B',
        "TBK m. 135/2'ye göre **birleşme geçmişe etkili olarak ortadan kalkarsa, borç varlığını sürdürür**. Mirasın reddi, oğulun mirasçı sıfatını geçmişe etkili olarak ortadan kaldırır.",
        '6098 sayılı TBK m. 135/2',
    ),
    # düzey 2
    '0033': patch(
        "A'nın B'den 80.000 ₺, B'nin de A'dan 50.000 ₺ muaccel para alacağı vardır. A takas iradesini B'ye bildirmiştir. Takas sonrası A'nın B'den kalan alacağı kaç ₺'dir?",
        {
            'A': '130.000',
            'B': '80.000',
            'C': '0',
            'D': '50.000',
            'E': '30.000',
        },
        'E',
        "TBK m. 139'a göre karşılıklı ve muaccel para borçları takas edilebilir; m. 143'e göre takas **bildirimle** gerçekleşir ve her iki borç **daha az olan borç tutarınca** sona erer: 80.000 − 50.000 = **30.000 ₺**.",
        '6098 sayılı TBK m. 139, 143',
    ),
    # düzey 3
    '0034': patch(
        "Müflis X'in C'den 60.000 ₺ alacağı, C'nin de X'ten 40.000 ₺ alacağı vardır; C'nin alacağının vadesi henüz gelmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "C'nin alacağı muaccel olmadığından takas yapılamaz",
            'B': "Takas edilmeseydi C'nin alacağı iflas masasına kaydedilirdi",
            'C': "Takas C'nin bildirimiyle gerçekleşir",
            'D': 'İflasta muaccel olmayan alacak da takas edilebilir',
            'E': "Takasla C'nin masaya borcu 20.000 ₺'ye iner",
        },
        'A',
        "TBK m. 142'ye göre **borçlunun iflası hâlinde alacaklılar, muaccel olmasalar bile, alacaklarını müflise olan borçlarıyla takas edebilirler**: 60.000 − 40.000 = 20.000 ₺.",
        '6098 sayılı TBK m. 142',
    ),
    # düzey 2
    '0035': patch(
        "Bir satış sözleşmesinden doğan bedel alacağı 1 Mart 2020'de muaccel olmuştur. Kanunda özel bir süre öngörülmemiştir. Zamanaşımı hangi günün sonunda dolar?",
        {
            'A': '28 Şubat 2030',
            'B': '1 Mart 2025',
            'C': '1 Mart 2030',
            'D': '1 Mart 2022',
            'E': '31 Aralık 2029',
        },
        'C',
        "TBK m. 146'ya göre kanunda aksine hüküm bulunmadıkça her alacak **on yıllık** zamanaşımına tabidir; m. 149'a göre süre muacceliyetle başlar, m. 151'e göre başladığı gün sayılmaz ve son gün de geçince dolar: **1 Mart 2030**.",
        '6098 sayılı TBK m. 146, 149, 151',
    ),
    # düzey 2
    '0036': patch(
        "Kira sözleşmesinde kira alacaklarının iki yıllık zamanaşımına tabi olacağı kararlaştırılmıştır. Ocak 2021'de muaccel olan kira bedeli 2025 yılında istenmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "2025'te istenen kira alacağı zamanaşımına uğramamıştır",
            'B': 'Kira bedelleri beş yıllık zamanaşımına tabidir',
            'C': 'Zamanaşımı süreleri sözleşmeyle değiştirilemez',
            'D': 'Taraflar zamanaşımını iki yıl olarak geçerli biçimde kararlaştırmıştır',
            'E': "Ocak 2021'de muaccel olan alacakta süre Ocak 2026'da dolar",
        },
        'D',
        "TBK m. 148'e göre **zamanaşımı süreleri sözleşmeyle değiştirilemez**; m. 147/1'e göre kira bedelleri beş yıllık zamanaşımına tabidir.",
        '6098 sayılı TBK m. 147, 148',
    ),
    # düzey 3
    '0037': patch(
        "Evlilik birliği içinde koca, karısına 2012 yılında muaccel olan bir borç ödeyecektir. Evlilik 10 Haziran 2024'te boşanma kararının kesinleşmesiyle sona ermiştir. On yıllık zamanaşımı hangi tarihte dolar?",
        {
            'A': '10 Haziran 2034',
            'B': '10 Haziran 2029',
            'C': '2034 yılı sonunda',
            'D': '2022 yılında',
            'E': '10 Haziran 2026',
        },
        'A',
        "TBK m. 153/3'e göre **evlilik devam ettiği sürece eşlerin diğerinden olan alacakları için zamanaşımı işlemeye başlamaz**; durdurma sebebinin ortadan kalktığı günün bitiminde işlemeye başlar. On yıllık süre 10 Haziran 2034'te dolar.",
        '6098 sayılı TBK m. 153',
    ),
    # düzey 3
    '0038': patch(
        'Alacaklı yalnız kefile karşı icra takibi başlatmıştır. Asıl borçluya karşı herhangi bir işlem yapılmamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Müteselsil borçlulardan birine karşı kesilme diğerlerini de etkiler',
            'B': 'Asıl borçluya karşı zamanaşımı işlemeye devam eder',
            'C': 'Kefile karşı kesilme asıl borçluya karşı da kesilme sayılır',
            'D': 'Asıl borçluya karşı kesilme olsaydı kefile karşı da kesilirdi',
            'E': 'Zamanaşımı kefile karşı kesilmiştir',
        },
        'C',
        "TBK m. 155'e göre zamanaşımı **asıl borçluya karşı kesilince kefile karşı da kesilmiş olur**; ancak **kefile karşı kesilince asıl borçluya karşı kesilmiş olmaz**. Müteselsil borçlulardan birine karşı kesilme diğerlerini de etkiler.",
        '6098 sayılı TBK m. 155',
    ),
    # düzey 3
    '0039': patch(
        'Zamanaşımı dolduktan sonra asıl borçlu, zamanaşımını ileri sürmeyeceğini (feragat ettiğini) alacaklıya yazılı olarak bildirmiştir. Alacaklı kefile başvurmuştur. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kefil borcun yarısından sorumludur',
            'B': 'Kefil zamanaşımını ileri sürebilir',
            'C': 'Feragat geçersizdir; kimse borçtan sorumlu değildir',
            'D': 'Kefil, asıl borçlunun onayı olmadan zamanaşımını ileri süremez',
            'E': 'Asıl borçlunun feragati kefili de bağlar',
        },
        'B',
        "TBK m. 160'a göre zamanaşımından **önceden** feragat edilemez; dolmuş zamanaşımından feragat mümkündür. Ancak **asıl borçlunun feragati kefile karşı ileri sürülemez**; kefil zamanaşımını ileri sürebilir.",
        '6098 sayılı TBK m. 160',
    ),
    # düzey 2
    '0040': patch(
        'Asıl borç ifa ile sona erdiğinde aşağıdakilerden hangileri de sona erer?\n\nI. Borca kefalet\n\nII. Borcu güvenceye alan rehin\n\nIII. Saklı tutulmamış işlemiş faiz',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'D',
        "TBK m. 131'e göre asıl borç ifa veya başka bir sebeple sona erince **rehin, kefalet, faiz ve ceza koşulu gibi bağlı hak ve borçlar da** sona erer; işlemiş faiz ancak saklı tutulmuşsa istenebilir. m. 152'ye göre asıl alacak zamanaşımına uğrayınca bağlı faiz de zamanaşımına uğrar.",
        '6098 sayılı TBK m. 131, 152',
    ),
    # düzey 3
    '0041': patch(
        "Borçlu, 100.000 ₺ olarak talep edilen borcun 70.000 ₺'sini kabul etmekte, 30.000 ₺'lik kısmına itiraz etmektedir. Alacaklı kısmen ifayı kabul ettiğini bildirmiştir. Borçlunun ifadan kaçınamayacağı tutar kaç ₺'dir?",
        {
            'A': '30.000',
            'B': '70.000',
            'C': '100.000',
            'D': '50.000',
            'E': '0',
        },
        'B',
        "TBK m. 84/2'ye göre **alacaklı kısmen ifayı kabul ederse borçlu, borcun kendisi tarafından ikrar olunan kısmını ifadan kaçınamaz**: borçlunun kabul ettiği **70.000 ₺**.",
        '6098 sayılı TBK m. 84/2',
    ),
    # düzey 2
    '0042': patch(
        'Bir un fabrikası, belirli bir kalite belirtilmeksizin 50 ton buğday satın almıştır. Satıcı elindeki en düşük kaliteli buğdayı teslim etmek istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kalite belirtilmediğinden satıcı en düşük kaliteyi seçebilir',
            'B': 'Aksi kararlaştırılsaydı seçim alıcıya ait olabilirdi',
            'C': 'Edimin seçimi satıcıya aittir',
            'D': 'Satıcı ortalama nitelikten düşük edim seçemez',
            'E': 'Satılan buğday bir çeşit borcu konusudur',
        },
        'A',
        "TBK m. 86'ya göre **çeşit borçlarında** aksi anlaşılmadıkça **edimin seçimi borçluya aittir**; ancak borçlunun seçeceği edim **ortalama nitelikten daha düşük olamaz**.",
        '6098 sayılı TBK m. 86',
    ),
    # düzey 3
    '0043': patch(
        "Para borcunun alacaklısı, borç doğduktan sonra İzmir'den yurt dışında ulaşılması güç bir yere taşınmış; bu durum ödemeyi önemli ölçüde güçleştirmiştir.\n\nTBK'ya göre ifa yeriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Para borçları kural olarak alacaklının yerleşim yerinde ödenir',
            'B': 'Bu olayda borç alacaklının önceki yerleşim yerinde ifa edilebilir',
            'C': 'Kural, ifanın önemli ölçüde güçleşmesi koşuluna bağlıdır',
            'D': 'Taraflar ifa yerini sözleşmeyle ayrıca belirleyebilir',
            'E': 'Borçlu borcu alacaklının yeni yerleşim yerinde ödemekle yükümlüdür',
        },
        'E',
        'TBK m. 89: para borçları alacaklının ödeme zamanındaki yerleşim yerinde ödenir; ancak alacaklının yerleşim yerini borcun doğumundan sonra değiştirmesi ifayı önemli ölçüde güçleştirmişse borç alacaklının önceki yerleşim yerinde ifa edilebilir. Taraflar ifa yerini açıkça veya örtülü olarak kararlaştırabilir.',
        '6098 sayılı TBK m. 89/2',
    ),
    # düzey 2
    '0044': patch(
        "A, Bursa'daki deposunda bulunan belirli bir baskı makinesini, İstanbul'da imzaladıkları sözleşmeyle Ankara'da oturan B'ye satmıştır. İfa yeri kararlaştırılmamıştır. Makine nerede teslim edilir?",
        {
            'A': 'İstanbul',
            'B': "B'nin ödeme zamanındaki yerleşim yeri",
            'C': 'Bursa',
            'D': 'Ankara',
            'E': "A'nın yerleşim yeri",
        },
        'C',
        "TBK m. 89/1'e göre aksine anlaşma yoksa **parça borçları, sözleşmenin kurulduğu sırada borç konusunun bulunduğu yerde** ifa edilir.",
        '6098 sayılı TBK m. 89/1',
    ),
    # düzey 2
    '0045': patch(
        "3 Mart Salı günü kurulan bir sözleşmede borcun 'sekiz gün içinde' ifa edileceği kararlaştırılmıştır. Süre hangi gün dolar?",
        {
            'A': '9 Mart',
            'B': '12 Mart',
            'C': '17 Mart',
            'D': '11 Mart',
            'E': '10 Mart',
        },
        'D',
        "TBK m. 92/1-1'e göre gün olarak belirlenen süre, **sözleşmenin kurulduğu gün sayılmaksızın** son günü dolmuş olur; **sekiz gün olarak belirlenmiş süre bir haftayı değil tam sekiz günü** ifade eder: 3 + 8 = **11 Mart**.",
        '6098 sayılı TBK m. 92',
    ),
    # düzey 2
    '0046': patch(
        "Vadesi bir ay sonra olan 100.000 ₺'lik borcunu erken ödemek isteyen borçlu, erken ödeme nedeniyle %3 indirim yaparak 97.000 ₺ ödemeyi önermiştir. Kanun, sözleşme veya âdette erken ödeme indirimi yoktur. Borçlu erken ödemede kaç ₺ ödemelidir?",
        {
            'A': '97.000',
            'B': '100.000',
            'C': '98.500',
            'D': '99.000',
            'E': '103.000',
        },
        'B',
        "TBK m. 96'ya göre borçlu edimini sürenin sona ermesinden önce ifa edebilir; ancak **kanun veya sözleşme ya da âdet gereği olmadıkça, erken ifada bulunması sebebiyle indirim yapamaz**.",
        '6098 sayılı TBK m. 96',
    ),
    # düzey 2
    '0047': patch(
        "Sözleşmede 'aynen ödeme' kaydı bulunmayan 5.000 EUR'luk borcun vadesinde borçlu, Türk lirası ödemek istemektedir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yabancı parayla ödeme kararlaştırılabilir',
            'B': 'Aynen ödeme kaydı yoksa borç Türk lirasıyla da ödenebilir',
            'C': 'Ödeme, ödeme günündeki rayiç üzerinden yapılır',
            'D': 'Aynen ödeme kaydı bulunsaydı borç avro olarak ödenirdi',
            'E': 'Türk lirasıyla ödeme için alacaklının rızası gerekir',
        },
        'E',
        'TBK m. 99/2: yabancı para ile ödeme kararlaştırılmışsa, sözleşmede aynen ödeme veya bu anlama gelen bir ifade bulunmadıkça borç, ödeme günündeki rayiç üzerinden Ülke parasıyla da ödenebilir; alacaklının rızası aranmaz.',
        '6098 sayılı TBK m. 99/2',
    ),
    # düzey 3
    '0048': patch(
        'Borçlunun aynı alacaklıya karşı iki muaccel borcu vardır: vadesi 1 Mart olan ve takip edilmeyen X borcu ile vadesi 1 Nisan olan ve icra takibine konu Y borcu. Borçlu ödeme yaparken açıklama yapmamış, makbuzda da açıklık yoktur. Ödeme hangi borca sayılır?',
        {
            'A': 'İki borca orantılı olarak',
            'B': 'Alacaklının dilediği borca',
            'C': 'İcra takibine konu olan Y borcuna',
            'D': 'Güvencesi en az olan borca',
            'E': 'Vadesi önce gelen X borcuna',
        },
        'C',
        "TBK m. 102'ye göre geçerli açıklama ve makbuzda açıklık yoksa ödeme muaccel borca sayılır; **birden çok borç muaccel ise ödeme, borçluya karşı ilk olarak takip edilen borç için** yapılmış kabul edilir. Takip yoksa vadesi önce gelen borca sayılırdı.",
        '6098 sayılı TBK m. 101, 102',
    ),
    # düzey 3
    '0049': patch(
        'Kiraya veren, Mart ayı kirası için çekince koymaksızın makbuz vermiştir. Kiracının Ocak ve Şubat kiralarını ödeyip ödemediği tartışmalıdır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Çekince konulsaydı önceki kiralar için bu sonuç doğmazdı',
            'B': 'Ocak ve Şubat kiralarının da ödendiği kabul edilir',
            'C': 'Makbuz çekince konulmaksızın verilmiştir',
            'D': 'Makbuz Mart ayı dışındaki kiralar için sonuç doğurmaz',
            'E': 'Kira bedeli dönemsel bir edimdir',
        },
        'D',
        "TBK m. 104/1'e göre **faiz veya kira bedeli gibi dönemsel edimlerden biri için, alacaklı tarafından çekince belirtilmeksizin makbuz verilmişse, önceki dönemlere ait edimler de ifa edilmiş sayılır**.",
        '6098 sayılı TBK m. 104',
    ),
    # düzey 3
    '0050': patch(
        'Borçlu anaparayı ödemiş; alacaklı, işlemiş faiz alacağını ne sözleşmede ne de ödeme anına kadar yaptığı bir bildirimle saklı tutmuştur ve durumdan da böyle bir saklı tutma anlaşılmamaktadır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşlemiş faiz alacağı da sona ermiştir',
            'B': 'Faiz alacağı bağımsız olduğundan devam eder',
            'C': 'Faizin sona ermesi için ayrıca ibra gerekir',
            'D': 'Faiz alacağı yarı oranda devam eder',
            'E': 'Faiz on yıl içinde ayrıca istenebilir',
        },
        'A',
        "TBK m. 131'e göre asıl borç sona erdiğinde **rehin, kefalet, faiz ve ceza koşulu gibi bağlı haklar da sona erer**; işlemiş faiz ancak sözleşmeyle veya **ifa anına kadar yapılacak bir bildirimle saklı tutulmuşsa** ya da bu durumdan anlaşılıyorsa istenebilir.",
        '6098 sayılı TBK m. 131',
    ),
    # düzey 2
    '0051': patch(
        'Kanunen yazılı şekle tabi bir sözleşmeden doğan borcu alacaklı, borçluyla telefonda yaptığı anlaşmayla tamamen ortadan kaldırmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İbra sözleşmesi şekle bağlı değildir',
            'B': 'Taraflar borcu kısmen de ibra edebilirdi',
            'C': 'Borç yazılı şekle tabi olduğundan ibra da yazılı yapılmalıdır',
            'D': 'Borç tamamen ortadan kalkmıştır',
            'E': 'İbra, taraflar arasında yapılan bir sözleşmedir',
        },
        'C',
        "TBK m. 132'ye göre **borcu doğuran işlem kanunen veya taraflarca belli bir şekle bağlı tutulmuş olsa bile** borç, tarafların **şekle bağlı olmaksızın yapacakları ibra sözleşmesiyle** tamamen veya kısmen ortadan kaldırılabilir.",
        '6098 sayılı TBK m. 132',
    ),
    # düzey 2
    '0052': patch(
        'Aşağıdakilerden hangileri borcu sona erdirir?\n\nI. Alacaklı ile borçlunun şekle bağlı olmadan yaptığı ibra sözleşmesi\n\nII. Mevcut borç için açık yenileme iradesi olmadan bono verilmesi\n\nIII. Alacaklı ve borçlu sıfatlarının aynı kişide birleşmesi',
        {
            'A': 'Yalnız III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'E',
        "TBK m. 132'ye göre **ibra** (I) ve m. 135'e göre **birleşme** (III) borcu sona erdirir. m. 133'e göre açık yenileme iradesi olmadıkça kambiyo taahhüdü yenileme sayılmaz (II).",
        '6098 sayılı TBK m. 132-135',
    ),
    # düzey 3
    '0053': patch(
        "Asıl borçlu B'nin alacaklı A'dan muaccel bir para alacağı bulunmakta ve B bunu henüz takas etmemiştir. A, kefil K'ye başvurmuştur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Kefil, asıl borçlunun takas hakkına dayanamaz ve borcu ödemekle yükümlüdür',
            'B': 'Takas asıl borçlunun bildirimiyle gerçekleşir',
            'C': 'Asıl borçlu takas hakkına sahiptir',
            'D': 'Kefil ifada bulunmaktan kaçınabilir',
            'E': 'Takas hakkı sürdükçe kefilin kaçınma hakkı da sürer',
        },
        'A',
        "TBK m. 140'a göre **asıl borçlunun takası ileri sürme hakkı bulundukça, kefili de alacaklıya ifada bulunmaktan kaçınabilir**; m. 143'e göre takas bildirimle gerçekleşir.",
        '6098 sayılı TBK m. 140',
    ),
    # düzey 2
    '0054': patch(
        "A, B ile yaptığı sözleşmede B'nin kızı C'ye her ay para ödemeyi üstlenmiştir (üçüncü kişi yararına sözleşme). A'nın da B'den muaccel bir alacağı vardır.\n\nTBK'ya göre takasla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Takas için karşılıklı ve muaccel alacaklar aranır',
            'B': 'Takas, karşı tarafa yapılan bildirimle gerçekleşir',
            'C': "A, C'ye olan borcunu B'den olan alacağıyla takas edebilir",
            'D': 'Üçüncü kişi yararına borçlanan bu borcu takas edemez',
            'E': "Bu olayda C'ye ödeme borcu sürer",
        },
        'C',
        "TBK m. 139-141: takas karşılıklı, aynı türden ve muaccel alacaklar arasında bildirimle gerçekleşir; ancak m. 141'e göre üçüncü kişi yararına borçlanan kişi, bu borcu ile sözleşmenin diğer tarafından olan alacağını takas edemez.",
        '6098 sayılı TBK m. 141',
    ),
    # düzey 3
    '0055': patch(
        'Takasa ilişkin olaylardan hangisinde varılan sonuç yanlıştır?',
        {
            'A': 'Borçlunun önceden takastan feragat etmesi geçerli sayılmıştır',
            'B': 'Takas bildirimiyle borçlar, takas edilebilecekleri anda küçük olan tutarda sona ermiştir',
            'C': 'Çekişmeli bir alacak olmasına rağmen takas ileri sürülmüştür',
            'D': 'Borçlar bildirim aranmaksızın takas edilebilir anda sona ermiştir',
            'E': 'Para ile özdeş edimler takas edilmiştir',
        },
        'D',
        "TBK m. 143'e göre **takas, ancak borçlunun takas iradesini alacaklıya bildirmesiyle gerçekleşir**; bildirim yapılınca borçlar takas edilebilecekleri anda küçük olan tutarda sona erer. m. 139/2 çekişmeli alacakta takasa, m. 145 önceden feragate izin verir.",
        '6098 sayılı TBK m. 139, 143, 145',
    ),
    # düzey 3
    '0056': patch(
        'Yüklenici, bir binanın çatısını ağır kusuruyla hiç gereği gibi yapmamıştır. İş sahibinin eser sözleşmesinden doğan tazminat alacağı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zamanaşımına tabi değildir',
            'B': 'On yıllık zamanaşımına tabidir',
            'C': 'Bir yıllık hak düşürücü süreye tabidir',
            'D': 'İki yıllık zamanaşımına tabidir',
            'E': 'Eser sözleşmesinden doğduğu için beş yıllık zamanaşımına tabidir',
        },
        'B',
        "TBK m. 147/6'ya göre eser sözleşmesinden doğan alacaklar beş yıllık zamanaşımına tabidir; ancak **yüklenicinin yükümlülüklerini ağır kusuruyla hiç ya da gereği gibi ifa etmemesi** hâli bu kapsamın dışında bırakılmıştır. Bu durumda m. 146'daki **on yıllık** süre uygulanır.",
        '6098 sayılı TBK m. 147/6',
    ),
    # düzey 3
    '0057': patch(
        "On yıllık zamanaşımına tabi bir alacak 2018'de muaccel olmuş; borçlu 15 Nisan 2022'de faiz ödemesi yapmıştır. Zamanaşımı hangi tarihte dolar?",
        {
            'A': '15 Nisan 2027',
            'B': '15 Nisan 2024',
            'C': '2032 yılı sonunda',
            'D': '2028 yılında',
            'E': '15 Nisan 2032',
        },
        'E',
        "TBK m. 154'e göre **borçlu borcu ikrar etmişse, özellikle faiz ödemiş** veya kısmen ifada bulunmuşsa zamanaşımı kesilir; m. 156'ya göre kesilmeyle **yeni bir süre** (on yıl) işlemeye başlar: **15 Nisan 2032**.",
        '6098 sayılı TBK m. 154, 156',
    ),
    # düzey 3
    '0058': patch(
        'Alacaklının açtığı dava, mahkemenin yetkisiz olması nedeniyle reddedilmiş; bu arada zamanaşımı süresi dolmuştur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Zamanaşımı dolduğundan alacaklı alacağını ileri süremez',
            'B': 'Alacaklının altmış günlük ek süresi vardır',
            'C': 'Ek süre hak düşürücü süreler bakımından da geçerlidir',
            'D': 'Dava yetkisizlik nedeniyle reddedilmiştir',
            'E': 'Ek süre görevsizlik nedeniyle ret hâlinde de uygulanır',
        },
        'A',
        "TBK m. 158'e göre dava veya def'i, **mahkemenin yetkili veya görevli olmaması**, düzeltilebilecek bir yanlışlık veya vaktinden önce açılma nedeniyle reddedilmiş olup o arada **zamanaşımı veya hak düşürücü süre** dolmuşsa, alacaklı **altmış günlük ek süre** içinde haklarını kullanabilir.",
        '6098 sayılı TBK m. 158',
    ),
    # düzey 3
    '0059': patch(
        "Velayet altındaki C'nin annesinden olan ve 2010 yılında muaccel hâle gelen bir alacağı bulunmaktadır; C 1 Eylül 2020'de ergin olmuş ve velayet sona ermiştir. Alacak on yıllık zamanaşımına tabidir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Zamanaşımı velayetin sona erdiği günün bitiminde işlemeye başlar',
            'B': 'Velayet süresince zamanaşımı işlemeye başlamaz',
            'C': "Zamanaşımı muacceliyetle 2010'da başladığından 2020'de dolmuştur",
            'D': 'Eşlerin birbirinden alacakları için de evlilik süresince zamanaşımı işlemez',
            'E': "On yıllık süre 1 Eylül 2030'da dolar",
        },
        'C',
        "TBK m. 153/1'e göre **velayet süresince çocukların ana ve babalarından olan alacakları için zamanaşımı işlemeye başlamaz**; durdurma sebebinin ortadan kalktığı günün bitiminde işlemeye başlar. m. 153/3 aynı kuralı evlilik süresince eşler için öngörür.",
        '6098 sayılı TBK m. 153',
    ),
    # düzey 2
    '0060': patch(
        'Zamanaşımına uğramış bir alacak için açılan davada davalı borçlu zamanaşımı savunmasında bulunmamıştır. Hâkim dosyadan sürenin dolduğunu görmüştür. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Zamanaşımı borçluya bir savunma hakkı verir',
            'B': 'Davalı zamanaşımını ileri sürseydi istem reddedilebilirdi',
            'C': 'Zamanaşımı borcu sona erdirmez',
            'D': "Hâkim zamanaşımını re'sen dikkate alarak davayı reddeder",
            'E': 'Davalı ileri sürmedikçe zamanaşımı gözetilmez',
        },
        'D',
        "TBK m. 161'e göre **zamanaşımı ileri sürülmedikçe, hâkim bunu kendiliğinden göz önüne alamaz**; zamanaşımı borcu sona erdirmez, borçluya bir def'i hakkı verir.",
        '6098 sayılı TBK m. 161',
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
    print(f"1 paket / {len(PATCHES)} soru ('Borcun Ifasi ve Sona Ermesi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
