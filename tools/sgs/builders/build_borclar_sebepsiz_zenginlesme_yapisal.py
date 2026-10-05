#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sebepsiz Zenginlesme — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surumde 101 celdirici mutlak ifadeliydi, kor %53): kosullar ve sebep turleri, borclanilmamis edimin ifasi, geri vermenin kapsami ve iyiniyet, giderler, geri istenememe, zamanasimi. Gercek sinavda en sik sorulan kaliplar (zamanasimi suresinin dogrudan sorulmasi, kotuniyetli zenginlesenin giderleri oncul listesi) tarih ve iade tutari hesaplarina cevrildi; 15 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 77-82 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/sebepsiz_zenginlesme.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "sebzen-gen-"


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
        "A, bankacılık uygulamasında hesap numarasını yanlış yazarak kiracısına göndereceği 15.000 ₺'yi tanımadığı B'nin hesabına göndermiştir.\n\nTBK'ya göre A'nın geri isteme hakkıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Haklı sebep olmaksızın zenginleşen geri vermekle yükümlüdür',
            'B': "Havale A'nın kusuruyla yapıldığından geri istenemez",
            'C': 'Zenginleşenin kötüniyetli olması şart değildir',
            'D': "İstem zenginleşen B'ye yöneltilir",
            'E': 'Zenginleşme banka aracılığıyla gerçekleşse de istem doğar',
        },
        'B',
        "TBK m. 77: haklı bir sebep olmaksızın bir başkasının malvarlığından zenginleşen, bu zenginleşmeyi geri vermekle yükümlüdür. Fakirleşenin kusuru veya zenginleşenin kötüniyeti bu yükümlülüğün şartı değildir; istem zenginleşen B'ye yöneltilir.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdakilerden hangileri sebepsiz zenginleşmeden doğan geri verme borcunun şartlarındandır?\n\nI. Bir zenginleşmenin bulunması\n\nII. Zenginleşmenin başkasının malvarlığından veya emeğinden sağlanması\n\nIII. Zenginleşenin kusurlu olması\n\nIV. Zenginleşmenin haklı bir sebebe dayanmaması',
        {
            'A': 'I, II, III ve IV',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve IV',
            'E': 'I, II ve III',
        },
        'D',
        "TBK m. 77'ye göre şartlar: **zenginleşme, zenginleşmenin başkasının malvarlığından veya emeğinden sağlanması (aralarında illiyet) ve haklı sebebin bulunmaması**. Sebepsiz zenginleşme bir kusur sorumluluğu değildir; zenginleşenin kusuru aranmaz.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 2
    '0003': patch(
        'Sebepsiz zenginleşme davasına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Dava ayni nitelikte olduğundan zenginleşen dışındaki herkese karşı açılabilir',
            'B': 'İstem iki ve on yıllık zamanaşımı sürelerine tabidir',
            'C': 'Dava zenginleşene karşı açılır',
            'D': 'Dava kişisel (nisbi) nitelikte bir davadır',
            'E': 'Davacı, zenginleşmenin haklı bir sebepten yoksun olduğunu ve malvarlığı kaymasını ispat eder',
        },
        'A',
        "Sebepsiz zenginleşmeden doğan istem, **zenginleşene karşı ileri sürülebilen kişisel (nisbi) bir alacak hakkıdır**; ayni hak gibi herkese karşı ileri sürülemez. Zamanaşımı m. 82'de düzenlenmiştir.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 3
    '0004': patch(
        "A, aynı faturayı dikkatsizlikle iki kez ödemiştir. İkinci ödemenin iadesini isteyen A'nın durumu hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İspat yükü alacaklıdadır; A bir şey ispat etmez',
            'B': "Çift ödemedeki dikkatsizlik ağır kusur sayıldığından A'nın geri isteme hakkı düşer",
            'C': 'İkinci ödeme bağışlama sayılır ve geri istenemez',
            'D': 'Kendini borçlu sanarak ödediğini ispat ederse ikinci ödemeyi geri isteyebilir',
            'E': 'Ancak alacaklı kötüniyetliyse geri isteyebilir',
        },
        'D',
        "TBK m. 78/1'e göre borçlanmadığı edimi kendi isteğiyle ifa eden, **kendisini borçlu sanarak** yerine getirdiğini ispat ederse geri isteyebilir; **ispat yükü geri isteyendedir**. Yanılarak yapılan çift ödeme bu kapsamdadır.",
        '6098 sayılı TBK m. 78/1',
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdakilerden hangilerinde yapılan ödemenin sebepsiz zenginleşme hükümlerine göre geri istenmesi mümkündür?\n\nI. Hesap numarası karıştırılarak yabancı birine yapılan havale\n\nII. Zamanaşımına uğramış bir borcun ödenmesi\n\nIII. Aldatma nedeniyle iptal edilen sözleşme için ödenen bedel',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'E',
        "Yanlış kişiye yapılan havale (I) ve iptal edilerek geçersiz hâle gelen sözleşmeye dayanan ödeme (III) haklı sebepten yoksundur. m. 78/2'ye göre **zamanaşımına uğramış borcun ifası** (II) geri istenemez.",
        '6098 sayılı TBK m. 78',
    ),
    # düzey 3
    '0006': patch(
        "A, kendisine karşı alacağı zamanaşımına uğramış olan B'ye, zamanaşımını bilerek bir kısım ödeme yapmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "B'nin aldığı ödeme haklı bir sebebe dayanır",
            'B': 'Zamanaşımı borcu sona erdirmez, dava edilebilirliğini etkiler',
            'C': "A'nın ödeme sırasındaki bilgisi sonucu değiştirmez",
            'D': 'Zamanaşımına uğramış borcun ifası geri istenemez',
            'E': 'A, zamanaşımını bildiği için yaptığı ödemeyi geri isteyebilir',
        },
        'E',
        "TBK m. 78/2'ye göre **zamanaşımına uğramış bir borcun ifasından** kaynaklanan zenginleşme geri istenemez; ödeyenin zamanaşımını bilip bilmemesi sonucu değiştirmez.",
        '6098 sayılı TBK m. 78',
    ),
    # düzey 3
    '0007': patch(
        "C, hesabına gelen bir havalenin yanlışlıkla yapıldığından habersizdir; ancak aynı gün gönderen banka kendisini arayarak paranın iade edilmesi gerekebileceğini bildirmiştir. C buna rağmen parayı harcamıştır. C'nin geri verme yükümlülüğü hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sadece paranın faizini geri verir',
            'B': 'Harcadığı kısmın yarısını geri verir',
            'C': 'İade ihtimalini hesaba katması gerektiğinden tamamını geri verir',
            'D': 'Banka kusurlu olduğundan geri verme yükümlülüğü doğmaz',
            'E': 'Havaleyi aldığı anda iyiniyetli olduğundan sonradan harcadığı kısmı geri vermez',
        },
        'C',
        "TBK m. 79/2'ye göre zenginleşen, **elden çıkarırken ileride geri vermek zorunda kalabileceğini hesaba katması gerekiyorsa** zenginleşmenin tamamını geri vermekle yükümlüdür.",
        '6098 sayılı TBK m. 79/2',
    ),
    # düzey 3
    '0008': patch(
        "Kötüniyetli zenginleşen F, geri vermesi gereken evde 10.000 ₺ zorunlu gider ve 40.000 ₺ yararlı gider yapmıştır. Yararlı giderin geri verme zamanında evde mevcut değer artışı 25.000 ₺'dir. F kaç ₺ isteyebilir?",
        {
            'A': '25.000',
            'B': '35.000',
            'C': '10.000',
            'D': '65.000',
            'E': '50.000',
        },
        'B',
        "TBK m. 80/2'ye göre **zenginleşen iyiniyetli değilse, zorunlu giderlerinin ve yararlı giderlerinden sadece geri verme zamanında mevcut olan değer artışının** ödenmesini isteyebilir: 10.000 + 25.000 = **35.000 ₺**.",
        '6098 sayılı TBK m. 80/2',
    ),
    # düzey 3
    '0009': patch(
        'Geri vermenin kapsamına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İyiniyetli zenginleşen, elinden çıkan kısmı ispat etmesine gerek olmadan düşebilir',
            'B': 'Geri vermeyi hesaba katması gereken zenginleşen tamamını geri verir',
            'C': 'Elden çıkma, geri isteme sırasındaki duruma göre değerlendirilir',
            'D': 'İyiniyetli zenginleşen, elinden çıktığını ispat ettiği kısım dışında kalanı geri verir',
            'E': 'Kötüniyetle elden çıkaran zenginleşmenin tamamını geri verir',
        },
        'A',
        "TBK m. 79/1'e göre iyiniyetli zenginleşen, zenginleşmenin geri istenmesi sırasında **elinden çıkmış olduğunu ispat ettiği** kısmın dışında kalanı geri verir; **ispat yükü zenginleşendedir**.",
        '6098 sayılı TBK m. 79/1',
    ),
    # düzey 3
    '0010': patch(
        "A'nın sebepsiz zenginleşmeye dayanan geri isteme hakkı olduğunu 5 Mayıs 2025'te öğrendiği, zenginleşmenin ise 2021 yılında gerçekleştiği bir olayda istem en geç hangi tarihte zamanaşımına uğrar?",
        {
            'A': '5 Mayıs 2026',
            'B': '5 Mayıs 2027',
            'C': '5 Mayıs 2035',
            'D': '2023 yılında',
            'E': '2031 yılında',
        },
        'B',
        "TBK m. 82/1'e göre istem hakkı, **hak sahibinin geri isteme hakkı olduğunu öğrendiği tarihten başlayarak iki yılın** ve her hâlde **zenginleşmenin gerçekleştiği tarihten başlayarak on yılın** geçmesiyle zamanaşımına uğrar. İki yıllık süre (5 Mayıs 2027) on yıllık süreden (2031) önce dolar.",
        '6098 sayılı TBK m. 82/1',
    ),
    # düzey 3
    '0011': patch(
        "A, geçersiz bir sözleşme nedeniyle B'ye bir bono vermiştir. A'nın bonoyu geri isteme hakkı zamanaşımına uğradıktan sonra B, bonoya dayanarak ödeme istemiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Zenginleşme bir alacak hakkı kazanılmasıyla da gerçekleşebilir',
            'B': 'Bu hâlde A borcunu ifadan kaçınabilir',
            'C': 'Geri isteme hakkı zamanaşımına uğradığından A ödemekle yükümlüdür',
            'D': 'Kaçınma hakkı geri isteme hakkı zamanaşımına uğrasa da kullanılır',
            'E': 'Geçersiz sözleşme bononun haklı sebebi olamaz',
        },
        'C',
        'TBK m. 82/2: zenginleşme, zenginleşenin bir alacak hakkı kazanması suretiyle gerçekleşmişse diğer taraf, istem hakkı zamanaşımına uğramış olsa bile her zaman bu borcunu ifadan kaçınabilir.',
        '6098 sayılı TBK m. 82/2',
    ),
    # düzey 3
    '0012': patch(
        'A, aldatılarak yaptığı bir satış sözleşmesini süresi içinde iptal etmiştir. A bedeli ödemiş, B de malı teslim etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İptal geçmişe etkili olmadığından ödenen bedel geri istenemez',
            'B': 'B de teslim ettiği malı geri isteyebilir',
            'C': 'Sözleşmenin iptaliyle ödemeler geçerli sebepten yoksun kalır',
            'D': 'A ödediği bedeli sebepsiz zenginleşme hükümlerine göre geri isteyebilir',
            'E': 'Geri isteme hakkı iki ve on yıllık zamanaşımına tabidir',
        },
        'A',
        "Aldatma nedeniyle iptal edilen sözleşme **baştan itibaren geçersiz** hâle gelir; bu sözleşmeye dayanan edimler TBK m. 77/2 anlamında **geçerli olmayan bir sebebe** dayandığından her iki taraf da verdiğini geri isteyebilir; istemler m. 82'deki zamanaşımına tabidir.",
        '6098 sayılı TBK m. 77/2',
    ),
    # düzey 2
    '0013': patch(
        'İyiniyetli zenginleşen C, kendisine sebepsiz olarak ödenen paranın bir kısmını harcadığını ileri sürmüş, ancak bunu ispat edememiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İspat edemediğinden zenginleşmenin tamamını geri verir',
            'B': 'İspat yükü geri isteyendedir',
            'C': 'Zenginleşme harcandığı için istem düşer',
            'D': 'İyiniyetli olduğundan harcadığını beyan ettiği kısmı ispat aranmadan geri vermez',
            'E': 'Harcadığını beyan ettiği kısmın yarısını geri verir',
        },
        'A',
        "TBK m. 79/1'e göre iyiniyetli zenginleşen ancak **elinden çıkmış olduğunu ispat ettiği** kısmı geri vermez; ispat yükü zenginleşendedir. İspat edilemeyen kısım için geri verme yükümlülüğü devam eder.",
        '6098 sayılı TBK m. 79/1',
    ),
    # düzey 2
    '0014': patch(
        "Hak sahibi, geri isteme hakkı olduğunu 20 Eylül 2024'te öğrenmiştir. Zenginleşme 2023 yılında gerçekleşmiştir. İstem en geç hangi tarihte zamanaşımına uğrar?",
        {
            'A': '31 Aralık 2026',
            'B': '20 Eylül 2034',
            'C': '20 Eylül 2026',
            'D': '20 Eylül 2025',
            'E': '2033 yılında',
        },
        'C',
        "TBK m. 82/1'e göre istem, öğrenmeden itibaren **iki yıl** (20 Eylül 2026) ve her hâlde zenginleşmeden itibaren on yıl (2033) geçmekle zamanaşımına uğrar; önce dolan iki yıllık süredir.",
        '6098 sayılı TBK m. 82/1',
    ),
    # düzey 3
    '0015': patch(
        "B, hesabına gelen 40.000 ₺'nin kendisine ait olmadığını ertesi gün öğrenmiş; bundan sonra 15.000 ₺'sini harcamıştır. B kaç ₺ geri vermekle yükümlüdür?",
        {
            'A': '32.500',
            'B': '15.000',
            'C': '25.000',
            'D': '20.000',
            'E': '40.000',
        },
        'E',
        "B paranın kendisine ait olmadığını öğrendikten sonra harcadığından zenginleşmeyi **iyiniyetli olmaksızın elden çıkarmıştır**. TBK m. 79/2'ye göre bu durumda **zenginleşmenin tamamı**, yani **40.000 ₺** geri verilir.",
        '6098 sayılı TBK m. 79/2',
    ),
    # düzey 3
    '0016': patch(
        "Bir toptancı, sipariş edilen 100 koli yerine yanlışlıkla 120 koli göndermiştir. Fazlalıktan habersiz olan alıcı, fazla kolilerden 10'unu satmış ve bunu belgelemiştir. Alıcı toptancıya kaç koli aynen geri vermekle yükümlüdür?",
        {
            'A': '20',
            'B': '5',
            'C': '15',
            'D': '0',
            'E': '10',
        },
        'E',
        "Fazla gönderilen 20 koli alıcıyı haklı sebep olmaksızın zenginleştirmiştir. TBK m. 79/1'e göre iyiniyetli zenginleşen **elinden çıktığını ispat ettiği** 10 koli dışında kalanı, yani **10 koliyi** geri verir.",
        '6098 sayılı TBK m. 79/1',
    ),
    # düzey 2
    '0017': patch(
        "A, sahipsiz sandığı B'ye ait bir tarlaya ekim yapmış, ancak B hasadı toplayarak satmıştır. B'nin elde ettiği gelir A'nın emeğinden kaynaklanmaktadır. A'nın istemi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Tarla B'nin mülkiyetinde olduğundan ekilen ürün de B'ye ait olur ve A bir hak ileri süremez",
            'B': "B, A'nın emeğinden zenginleştiğinden A sebepsiz zenginleşme istemi ileri sürebilir",
            'C': "A'nın istemi ancak haksız fiile dayanabilir",
            'D': 'B iyiniyetli olduğundan istem düşer',
            'E': 'A ancak tohum bedelini isteyebilir',
        },
        'B',
        "TBK m. 77'ye göre zenginleşme bir başkasının **malvarlığından veya emeğinden** sağlanabilir. B'nin hasattan elde ettiği değer A'nın emeğine dayanır ve bu zenginleşmenin haklı bir sebebi yoktur.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 3
    '0018': patch(
        'B, havalenin kendisine ait olmadığını bildiği hâlde parayı harcamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Zorunlu giderlerini geri isteyenden isteyebilir',
            'B': 'Yararlı giderden geri verme anında mevcut olan değer artışını geri isteyenden isteyebilir',
            'C': 'Kötüniyeti, elden çıkarma savunmasını engeller',
            'D': 'Harcadığı kısmı ispat ederse bu kısmı geri vermekle yükümlü olmaz',
            'E': 'Zenginleşmenin tamamını geri vermekle yükümlüdür',
        },
        'D',
        "TBK m. 79/2'ye göre zenginleşmeyi **iyiniyetli olmaksızın elden çıkaran** zenginleşmenin tamamını geri verir; elden çıkma savunması yalnız iyiniyetli zenginleşene tanınmıştır. Giderler m. 80/2'ye göre sınırlı olarak istenebilir.",
        '6098 sayılı TBK m. 79/2, 80',
    ),
    # düzey 2
    '0019': patch(
        'Sebepsiz zenginleşme ile haksız fiil arasındaki farklara ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Her ikisinde de iki ve on yıllık zamanaşımı süreleri öngörülmüştür',
            'B': 'Sebepsiz zenginleşmede de fakirleşenin uğradığı zararın tamamı tazmin edilir',
            'C': 'Her ikisi de borcun kaynaklarındandır',
            'D': 'Haksız fiilde tazminat zarara, sebepsiz zenginleşmede iade zenginleşmeye göre belirlenir',
            'E': 'Sebepsiz zenginleşmede zenginleşenin kusuru aranmaz',
        },
        'B',
        'Haksız fiilde tazminatın ölçüsü **zarar**, sebepsiz zenginleşmede geri vermenin ölçüsü **zenginleşmedir** (m. 79). Sebepsiz zenginleşmede kusur aranmaz; her ikisinde de iki ve on yıllık zamanaşımı vardır (m. 72, 82).',
        '6098 sayılı TBK m. 49, 77',
    ),
    # düzey 3
    '0020': patch(
        "Kendisine sebepsiz olarak ödenen 30.000 ₺'yi iyiniyetle alan C, aleyhine geri isteme davası açıldığını öğrendikten sonra paranın 18.000 ₺'sini harcamıştır. C kaç ₺ geri vermekle yükümlüdür?",
        {
            'A': '24.000',
            'B': '15.000',
            'C': '12.000',
            'D': '30.000',
            'E': '18.000',
        },
        'D',
        "C, dava açıldığını öğrendikten sonra harcadığından **ileride geri vermek zorunda kalabileceğini hesaba katması gereken** bir dönemde paranın bir kısmını elden çıkarmıştır. TBK m. 79/2'ye göre zenginleşmenin **tamamı**, yani **30.000 ₺** geri verilir.",
        '6098 sayılı TBK m. 79/2',
    ),
    # düzey 3
    '0021': patch(
        "A ile B, bir taşınmazın satışı için adi yazılı bir sözleşme yapmış ve A bedelin bir kısmını ödemiştir. Sözleşme, resmî şekilde yapılmadığı için geçersizdir. A'nın ödediği bedeli geri istemesi hangi sebep türüne dayanır?",
        {
            'A': 'Ahlaki ödevin ifası',
            'B': 'Geçerli olmayan sebep',
            'C': 'Sona ermiş sebep',
            'D': 'Borçlanılmamış edimin bilerek ifası',
            'E': 'Gerçekleşmemiş sebep',
        },
        'B',
        "TBK m. 77/2'ye göre geri verme yükümlülüğü **özellikle zenginleşmenin geçerli olmayan, gerçekleşmemiş veya sona ermiş bir sebebe dayanması** hâlinde doğar. Şekle aykırılık nedeniyle kesin hükümsüz olan sözleşmeye dayanan ödeme, **geçerli olmayan sebebe** dayanır.",
        '6098 sayılı TBK m. 77/2',
    ),
    # düzey 2
    '0022': patch(
        "Kiracı A, bir yıllık kira bedelini peşin ödemiş; kira sözleşmesi üçüncü ayın sonunda hukuka uygun biçimde sona ermiştir. A'nın kalan dokuz aya ait kira bedelini geri istemesi hangi sebep türüne dayanır?",
        {
            'A': 'Geçerli olmayan sebep',
            'B': 'Zamanaşımına uğramış borcun ifası',
            'C': 'Sona ermiş sebep',
            'D': 'Gerçekleşmemiş sebep',
            'E': 'Hukuka aykırı amaç',
        },
        'C',
        "TBK m. 77/2'deki **sona ermiş sebep**, başlangıçta geçerli olan bir sebebin sonradan ortadan kalkmasıdır. Sözleşme sona erdiğinden sonraki dönemler için ödenen kira haklı sebepten yoksun kalmıştır.",
        '6098 sayılı TBK m. 77/2',
    ),
    # düzey 2
    '0023': patch(
        'Sebepsiz zenginleşmeye ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Zenginleşenin iyiniyeti geri vermenin kapsamını etkiler',
            'B': 'Zenginleşme başkasının emeğinden de sağlanabilir',
            'C': 'Geri verme yükümlülüğü için zenginleşenin kusurlu davranması gerekir',
            'D': 'Sona eren bir hukuki ilişkiye dayanan ve sonraki döneme ait olan edim de geri istenebilir',
            'E': 'Geçerli olmayan bir sözleşmeye dayanan ödeme geri istenebilir',
        },
        'C',
        'Sebepsiz zenginleşme, **haklı sebepten yoksun malvarlığı kaymasını** düzeltir; kusur şartı yoktur. İyiniyet ise m. 79-80 uyarınca geri verme ve gider talebinin kapsamını belirler.',
        '6098 sayılı TBK m. 77-82',
    ),
    # düzey 2
    '0024': patch(
        "A, B'ye herhangi bir borcu olmadığını bildiği hâlde, onu zor durumdan kurtarmak için B'nin kira borcunu ödemiştir. Aradan bir süre geçtikten sonra A ödediği parayı geri istemektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ödemenin üzerinden bir yıl geçmediyse geri isteyebilir',
            'B': 'Ancak ödemeyi noter aracılığıyla yaptıysa geri isteyebilir',
            'C': "B'nin iyiniyetli olması hâlinde yarısını geri alır",
            'D': 'Borçlu olmadığını bilerek ödediğinden geri isteyemez',
            'E': 'Borçsuz ödeme olduğundan geri isteyebilir',
        },
        'D',
        "TBK m. 78/1'e göre borçlanmadığı edimi kendi isteğiyle yerine getiren kimse, bunu ancak **kendisini borçlu sanarak yerine getirdiğini ispat ederse** geri isteyebilir. Bilerek yapılan ödeme geri istenemez.",
        '6098 sayılı TBK m. 78/1',
    ),
    # düzey 3
    '0025': patch(
        'Borçlanılmamış edimin ifasına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Yanılmanın ispat yükü zenginleşene aittir\n\nII. Borçlu olmadığını bilerek ifa eden geri isteyemez\n\nIII. Kendini borçlu sanarak ifa ettiğini ispat eden geri isteyebilir',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'Yalnız III',
        },
        'D',
        "TBK m. 78/1'e göre borçlanmadığı edimi kendi isteğiyle yerine getiren, **kendisini borçlu sanarak** yerine getirdiğini **ispat ederse** geri isteyebilir (II, III); ispat yükü **geri isteyendedir** (I yanlış).",
        '6098 sayılı TBK m. 78',
    ),
    # düzey 3
    '0026': patch(
        "B, kendisine yanlışlıkla gönderilen 60.000 ₺'nin kendisine ait olmadığını bildiği hâlde 25.000 ₺'sini harcamıştır. B kaç ₺ geri vermekle yükümlüdür?",
        {
            'A': '30.000',
            'B': '45.000',
            'C': '25.000',
            'D': '35.000',
            'E': '60.000',
        },
        'E',
        "TBK m. 79/2'ye göre zenginleşen, **zenginleşmeyi iyiniyetli olmaksızın elden çıkarmışsa zenginleşmenin tamamını** geri vermekle yükümlüdür: **60.000 ₺**. Elden çıkan kısmın düşülmesi yalnız iyiniyetli zenginleşen içindir.",
        '6098 sayılı TBK m. 79/2',
    ),
    # düzey 3
    '0027': patch(
        'İyiniyetli zenginleşen E, geri vermesi gereken evde çatı onarımı için 10.000 ₺ zorunlu gider ve ısı yalıtımı için 40.000 ₺ yararlı gider yapmıştır. E, geri verme isteminde bulunandan kaç ₺ isteyebilir?',
        {
            'A': '40.000',
            'B': '25.000',
            'C': '10.000',
            'D': '35.000',
            'E': '50.000',
        },
        'E',
        "TBK m. 80/1'e göre **zenginleşen iyiniyetli ise, yaptığı zorunlu ve yararlı giderleri** geri verme isteminde bulunandan isteyebilir: 10.000 + 40.000 = **50.000 ₺**.",
        '6098 sayılı TBK m. 80/1',
    ),
    # düzey 3
    '0028': patch(
        'Kötüniyetli zenginleşen G, geri vermesi gereken eve kalorifer tesisatı (yararlı gider) yaptırmış ve bahçeye süs havuzu kurdurmuştur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Süs havuzu için yaptığı giderin tamamını geri isteyenden isteyebilir',
            'B': 'Kalorifer için geri verme anında mevcut değer artışını isteyebilir',
            'C': 'Zorunlu giderlerinin ödenmesini isteyebilir',
            'D': 'Karşılık önerilmezse zararsızca ayrılabilen eklemeleri ayırıp alabilir',
            'E': 'Kalorifer giderinin tamamını isteyemez',
        },
        'A',
        "TBK m. 80/3'e göre zenginleşen, **iyiniyetli olup olmadığına bakılmaksızın diğer giderlerinin ödenmesini isteyemez**; ancak kendisine karşılık önerilmezse zararsızca ayrılabilen eklemeleri ayırıp alabilir. Kötüniyetli zenginleşen yararlı giderden yalnız mevcut değer artışını isteyebilir (m. 80/2).",
        '6098 sayılı TBK m. 80',
    ),
    # düzey 2
    '0029': patch(
        'Aşağıdakilerden hangileri hukuka veya ahlaka aykırı amaçla verilen şeye ilişkin olarak doğrudur?\n\nI. Amaç gerçekleşmemişse verilen şey verene iade edilir\n\nII. Açılan davada hâkim şeyin Devlete mal edilmesine karar verebilir\n\nIII. Veren, amacın hukuka aykırı olduğunu bilmiyorsa geri isteyebilir',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'Yalnız II',
        },
        'E',
        "TBK m. 81'e göre hukuka veya ahlaka aykırı sonucun gerçekleşmesi amacıyla verilen şey **geri istenemez** ve hâkim **Devlete mal edilmesine** karar verebilir (II). Amacın gerçekleşmemesi (I) veya verenin iddia ettiği bilgisizlik (III) geri istenememe kuralını değiştirmez.",
        '6098 sayılı TBK m. 81',
    ),
    # düzey 3
    '0030': patch(
        'Bir öğrenci, sınav sorularını kendisine sızdırması için bir görevliye para vermiş; görevli soruları vermemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Görevli edimi yerine getirmediğinden öğrenci parayı geri isteyebilir',
            'B': 'Öğrenci verdiği parayı geri isteyemez',
            'C': 'Açılan davada hâkim paranın Devlete mal edilmesine karar verebilir',
            'D': 'Para ahlaka ve hukuka aykırı bir amaçla verilmiştir',
            'E': 'Görevlinin parayı elinde tutması sebepsiz zenginleşme istemi doğurmaz',
        },
        'A',
        "TBK m. 81'e göre **hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey geri istenemez**; amacın gerçekleşmemesi bu sonucu değiştirmez. Hâkim verilen şeyin Devlete mal edilmesine karar verebilir.",
        '6098 sayılı TBK m. 81',
    ),
    # düzey 2
    '0031': patch(
        'Sebepsiz zenginleşmede zamanaşımına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. İki yıllık süre hak sahibinin geri isteme hakkını öğrenmesiyle başlar\n\nII. On yıllık süre zenginleşmenin gerçekleştiği tarihten başlar\n\nIII. Zenginleşme alacak hakkı kazanılması biçimindeyse zamanaşımından sonra borcun ifasından kaçınılamaz',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'D',
        "TBK m. 82/1'e göre iki yıllık süre **öğrenmeden**, on yıllık süre **zenginleşmeden** başlar. m. 82/2'ye göre zenginleşme alacak hakkı kazanılması biçiminde gerçekleşmişse diğer taraf zamanaşımına rağmen **her zaman ifadan kaçınabilir** (III yanlış).",
        '6098 sayılı TBK m. 82',
    ),
    # düzey 3
    '0032': patch(
        'Sebepsiz zenginleşme isteminin zamanaşımına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Alacak hakkı kazanılmasıyla oluşan zenginleşmede ifadan kaçınma süresizdir',
            'B': 'On yıllık süre zenginleşmenin gerçekleştiği tarihten başlar',
            'C': 'İki yıllık süre, zenginleşenin zenginleştiğini öğrendiği tarihten başlar',
            'D': 'İki süreden önce dolanı zamanaşımını tamamlar',
            'E': 'İki yıllık süre hak sahibinin öğrenmesiyle başlar',
        },
        'C',
        "TBK m. 82'ye göre iki yıllık süre **hak sahibinin (fakirleşenin) geri isteme hakkı olduğunu öğrendiği tarihten** başlar; zenginleşenin bilgisi süreyi başlatmaz.",
        '6098 sayılı TBK m. 82',
    ),
    # düzey 3
    '0033': patch(
        "İyiniyetli zenginleşen B, kendisine yanlışlıkla gönderilen 50.000 ₺'nin 20.000 ₺'sini bir yakınına hediye etmiş ve bunu belgelemiştir. Geri istendiğinde B kaç ₺ geri vermekle yükümlüdür?",
        {
            'A': '20.000',
            'B': '30.000',
            'C': '25.000',
            'D': '50.000',
            'E': '35.000',
        },
        'B',
        "TBK m. 79/1'e göre iyiniyetli zenginleşen, **geri istenme sırasında elinden çıkmış olduğunu ispat ettiği** kısım dışında kalanı geri verir: 50.000 − 20.000 = **30.000 ₺**.",
        '6098 sayılı TBK m. 79/1',
    ),
    # düzey 3
    '0034': patch(
        'A ile B arasındaki araba satışı kesin hükümsüzdür; A arabayı teslim etmiş, B de bedeli ödemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İstemler öğrenmeden itibaren iki yıllık zamanaşımına tabidir',
            'B': 'Her iki taraf da verdiğini geri isteyebilir',
            'C': 'Tarafların geri verme istemleri sebepsiz zenginleşme hükümlerine göre çözümlenir',
            'D': 'Sözleşme kesin hükümsüz olduğundan arabayı teslim eden A geri isteyemez',
            'E': 'Edimler geçerli olmayan bir sebebe dayanmaktadır',
        },
        'D',
        "Kesin hükümsüz sözleşmeye dayanan edimler TBK m. 77/2 anlamında **geçerli olmayan sebebe** dayanır; **her iki taraf** da verdiğini geri isteyebilir ve istemler m. 82'deki sürelere tabidir.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 2
    '0035': patch(
        'Sebepsiz zenginleşmenin koşullarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Zenginleşme haklı bir sebebe dayanmamalıdır',
            'B': 'Kanunda sayılan üç sebep türü dışındaki hâllerde geri verme istenemez',
            'C': 'Zenginleşme malvarlığındaki artış biçiminde olabilir',
            'D': 'Ayırt etme gücü olmayan zenginleşen de haklı sebepten yoksun zenginleşmeyi geri vermekle yükümlüdür',
            'E': 'Zenginleşme başkasının emeğinden de sağlanabilir',
        },
        'B',
        'TBK m. 77/2, yükümlülüğün **özellikle** geçerli olmayan, gerçekleşmemiş veya sona ermiş sebep hâllerinde doğduğunu belirtir; sayım **örnek niteliğindedir**. Asıl ölçüt, zenginleşmenin haklı bir sebebe dayanmamasıdır.',
        '6098 sayılı TBK m. 77',
    ),
    # düzey 3
    '0036': patch(
        'Zenginleşenin, zorunlu ve yararlı giderler dışındaki diğer giderlerine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. İyiniyetli olup olmadığına bakılmaksızın bu giderlerin ödenmesini isteyemez\n\nII. Karşılık önerilmezse zararsızca ayrılabilen eklemeleri ayırıp alabilir\n\nIII. Karşılık önerilse bile eklemeleri ayırıp alma hakkı devam eder',
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        "TBK m. 80/3'e göre zenginleşen diğer giderlerinin ödenmesini **iyiniyetli olup olmadığına bakılmaksızın isteyemez** (I); ancak **kendisine karşılık önerilmezse** zararsızca ayrılabilen eklemeleri ayırıp alabilir (II). Karşılık önerilmişse ayırma hakkı yoktur (III yanlış).",
        '6098 sayılı TBK m. 80/3',
    ),
    # düzey 2
    '0037': patch(
        "A, kendisini boğulmaktan kurtaran B'ye minnettarlık duygusuyla 30.000 ₺ vermiştir. Daha sonra B ile arası bozulan A parayı geri istemektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bir yıl içinde istenirse geri alınabilir',
            'B': "B'nin iyiniyetli olması hâlinde geri istenebilir",
            'C': 'Paranın yarısı geri istenebilir',
            'D': 'Borçsuz ödeme olduğundan geri istenebilir',
            'E': 'Ahlaki bir ödevin yerine getirilmesi sayıldığından geri istenemez',
        },
        'E',
        "TBK m. 78/2'ye göre **ahlaki bir ödevin yerine getirilmiş olmasından** kaynaklanan zenginleşmeler geri istenemez.",
        '6098 sayılı TBK m. 78/2',
    ),
    # düzey 3
    '0038': patch(
        "Kötüniyetli zenginleşen J, sebepsiz olarak edindiği bir malı elden çıkarmamış; mal için 4.000 ₺ zorunlu gider ve 20.000 ₺ yararlı gider yapmıştır. Yararlı giderin geri verme anındaki değer artışı 6.000 ₺'dir. J malı geri verirken geri isteyenden kaç ₺ talep edebilir?",
        {
            'A': '24.000',
            'B': '26.000',
            'C': '4.000',
            'D': '10.000',
            'E': '6.000',
        },
        'D',
        "TBK m. 80/2'ye göre kötüniyetli zenginleşen **zorunlu giderlerini** ve yararlı giderlerden yalnız **geri verme zamanında mevcut değer artışını** isteyebilir: 4.000 + 6.000 = **10.000 ₺**.",
        '6098 sayılı TBK m. 79, 80',
    ),
    # düzey 2
    '0039': patch(
        'Sebepsiz zenginleşen B, geri verme borcunu ödemeden ölmüştür.\n\nBu durumla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Geri verme borcu malvarlığına ilişkin bir borçtur',
            'B': 'Borç mirası reddetmeyen mirasçılara geçer',
            'C': 'Geri verme borcu zenginleşenin ölümüyle sona erer',
            'D': 'Borç kişiye sıkı sıkıya bağlı bir yükümlülük değildir',
            'E': 'Mirasçıların sorumluluğu külli halefiyete dayanır',
        },
        'C',
        'Sebepsiz zenginleşmeden doğan geri verme borcu malvarlığına ilişkin bir borçtur; zenginleşenin ölümüyle sona ermez ve külli halefiyet gereği mirası reddetmeyen mirasçılara geçer. Kişiye sıkı sıkıya bağlı bir yükümlülük değildir.',
        '6098 sayılı TBK m. 77',
    ),
    # düzey 3
    '0040': patch(
        "E'ye yanlışlıkla teslim edilen bir bisiklet, bunu bilmeyen E'nin evinin önünden, E'nin bir kusuru olmaksızın çalınmıştır. Gerçek alıcı bisikletin geri verilmesini istemektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'E bisikletin bedelini ödemekle yükümlüdür',
            'B': "E'nin iyiniyeti sonucu değiştirmez; çalınan bisikletin tam değerini geri isteyene öder",
            'C': 'E bedelin yarısını öder',
            'D': 'İyiniyetli E, bisikletin elinden çıktığını ispat ederse geri verme yükümlülüğü doğmaz',
            'E': 'E ancak hırsız bulunursa sorumluluktan kurtulur',
        },
        'D',
        "TBK m. 79/1'e göre sebepsiz zenginleşen, **zenginleşmenin geri istenmesi sırasında elinden çıkmış olduğunu ispat ettiği kısmın** dışında kalanı geri verir. İyiniyetli E'nin elinden çıkan bisiklet için geri verme yükümlülüğü yoktur.",
        '6098 sayılı TBK m. 79/1',
    ),
    # düzey 2
    '0041': patch(
        "A, B ile ileride yapmayı planladıkları bir satış sözleşmesi için B'ye kapora ödemiş; ancak taraflar anlaşamadığından sözleşme hiç kurulmamıştır. A'nın ödediği paranın iadesi hangi sebep türüne dayanır?",
        {
            'A': 'Hukuka aykırı amaç',
            'B': 'Gerçekleşmemiş sebep',
            'C': 'Ahlaki ödev',
            'D': 'Geçerli olmayan sebep',
            'E': 'Sona ermiş sebep',
        },
        'B',
        "TBK m. 77/2'deki **gerçekleşmemiş sebep**, gelecekte gerçekleşmesi beklenen bir sebep için edimde bulunulmuş olup da bu sebebin hiç gerçekleşmemesini ifade eder. Kurulması beklenen sözleşme hiç kurulmamıştır.",
        '6098 sayılı TBK m. 77/2',
    ),
    # düzey 3
    '0042': patch(
        "Yedi yaşındaki C'nin banka hesabına, bir muhasebe hatası nedeniyle bir şirket tarafından 8.000 ₺ yatırılmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Geri verme yükümlülüğü zenginleşenin kusuruna bağlı değildir',
            'B': "C'nin durumdan haberdar olmaması istemi engellemez",
            'C': 'Şirket, sebepsiz zenginleşme hükümlerine göre parayı geri isteyebilir',
            'D': "Zenginleşme C'nin malvarlığındaki artış şeklinde gerçekleşmiştir",
            'E': 'C ayırt etme gücüne sahip olmadığından geri verme yükümlülüğü doğmaz',
        },
        'E',
        "TBK m. 77'deki geri verme yükümlülüğü **haksız fiil sorumluluğu değildir**; zenginleşenin kusuru, bilgisi veya ayırt etme gücü aranmaz. Haklı sebep olmaksızın malvarlığı artan küçük de zenginleşmeyi geri vermekle yükümlüdür.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 2
    '0043': patch(
        "A, adres karışıklığı nedeniyle B'nin evinin dış cephesini kendi evi sanarak boyamış; B, evinin boyanmış olmasından yararlanmıştır. A'nın istemi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'B boyanmasını istemediğinden bir yükümlülüğü doğmaz',
            'B': "A'nın istemi ancak haksız fiile dayandırılabilir",
            'C': "B, A'nın emeğinden haklı sebep olmaksızın zenginleştiğinden A istemde bulunabilir",
            'D': 'A ancak boyayı kazıyarak geri alabilir',
            'E': 'Zenginleşme para olarak değil emek olarak gerçekleştiğinden bir istem doğmaz',
        },
        'C',
        "TBK m. 77'ye göre zenginleşme **bir başkasının malvarlığından veya emeğinden** sağlanabilir. B'nin evindeki değer artışı A'nın emeğinden ve haklı bir sebep olmaksızın gerçekleşmiştir.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 3
    '0044': patch(
        'A, zamanaşımına uğradığını bilmediği bir borcu ödemiş, sonra zamanaşımını öğrenerek ödediğini geri istemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yarısını geri isteyebilir',
            'B': 'Alacaklı iyiniyetliyse geri isteyebilir',
            'C': 'Zamanaşımına uğramış borcun ifası geri istenemez',
            'D': 'Ödeme tarihinden itibaren bir yıl içinde geri isteyebilir',
            'E': 'Zamanaşımını bilmediğinden geri isteyebilir',
        },
        'C',
        "TBK m. 78/2'ye göre **zamanaşımına uğramış bir borcun ifasından** kaynaklanan zenginleşmeler geri istenemez. Zamanaşımı borcu sona erdirmez, yalnız dava edilebilirliğini ortadan kaldırır; ifa geçerli bir borcun ifasıdır.",
        '6098 sayılı TBK m. 78/2',
    ),
    # düzey 2
    '0045': patch(
        'A, kanunen bakmakla yükümlü olmadığı yaşlı teyzesine yıllarca düzenli olarak para göndermiştir. Teyzesiyle arası bozulan A, gönderdiği paraları geri istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'A, borçlu olmadığı ödemeleri yaptığı için paraları geri isteyebilir',
            'B': 'Ahlaki ödevin ifasından doğan zenginleşme geri istenemez',
            'C': 'Aradaki ilişkinin bozulması geri istenememe sonucunu değiştirmez',
            'D': "A'nın ödemeleri ahlaki bir ödevin yerine getirilmesidir",
            'E': "A'nın teyzesine karşı kanuni bir bakım borcu yoktur",
        },
        'A',
        "TBK m. 78/2'ye göre **ahlaki bir ödevin yerine getirilmiş olmasından** kaynaklanan zenginleşmeler geri istenemez; ödeyenin sonradan fikrini değiştirmesi bu sonucu etkilemez.",
        '6098 sayılı TBK m. 78/2',
    ),
    # düzey 3
    '0046': patch(
        "Bir işçiye bordro hatasıyla 20.000 ₺ fazla ücret ödenmiştir. Hatadan habersiz olan işçi paranın 12.000 ₺'lik kısmını tatilde harcamış ve bunu ispat etmiştir. İşverenin geri isteme tarihinde işçi kaç ₺ geri vermekle yükümlüdür?",
        {
            'A': '8.000',
            'B': '12.000',
            'C': '20.000',
            'D': '10.000',
            'E': '0',
        },
        'A',
        "TBK m. 79/1'e göre sebepsiz zenginleşen, **zenginleşmenin geri istenmesi sırasında elinden çıkmış olduğunu ispat ettiği kısmın dışında kalanı** geri vermekle yükümlüdür: 20.000 − 12.000 = **8.000 ₺**. İşçi iyiniyetli olduğundan m. 79/2 uygulanmaz.",
        '6098 sayılı TBK m. 79/1',
    ),
    # düzey 3
    '0047': patch(
        "İyiniyetli zenginleşen D, kendisine sebepsiz olarak devredilen bir malın 100.000 ₺ değerindeki kısmından 30.000 ₺'lik bölümünü elden çıkardığını ispat etmiş; malı korumak için 5.000 ₺ zorunlu gider yapmıştır. Geri verme isteminde bulunana karşı D'nin net geri verme yükümlülüğü kaç ₺'dir?",
        {
            'A': '70.000',
            'B': '65.000',
            'C': '95.000',
            'D': '75.000',
            'E': '100.000',
        },
        'B',
        "TBK m. 79/1'e göre iyiniyetli zenginleşen elinden çıktığını ispat ettiği kısım dışında kalanı geri verir: 100.000 − 30.000 = 70.000 ₺. m. 80/1'e göre iyiniyetli zenginleşen **zorunlu ve yararlı giderlerini** geri isteyenden isteyebilir: 70.000 − 5.000 = **65.000 ₺**.",
        '6098 sayılı TBK m. 79, 80',
    ),
    # düzey 2
    '0048': patch(
        "İyiniyetli zenginleşen H, geri vermesi gereken bir eve duvara vidalı, zarar vermeden sökülebilen bir dekoratif lamba takmıştır. Geri isteyen taraf lamba için bir bedel önermemiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İyiniyetli zenginleşen zorunlu ve yararlı giderlerini isteyebilir',
            'B': 'Zenginleşen diğer giderlerinin ödenmesini isteyemez',
            'C': 'Lamba eve bağlandığından H onu sökemez',
            'D': 'Karşılık önerilmezse zararsızca ayrılabilen ekleme alınabilir',
            'E': 'H lambayı evi geri vermeden önce sökebilir',
        },
        'C',
        'TBK m. 80: iyiniyetli zenginleşen zorunlu ve yararlı giderlerin ödenmesini isteyebilir; diğer giderlerinin ödenmesini isteyemez. Ancak kendisine karşılık önerilmezse, o şey ile birleştirdiği ve zararsızca ayrılması mümkün eklemeleri geri vermeden önce ayırıp alabilir.',
        '6098 sayılı TBK m. 80/3',
    ),
    # düzey 3
    '0049': patch(
        'A, bir kamu görevlisine kendisine haksız bir ihale verilmesi karşılığında rüşvet olarak 50.000 ₺ vermiş; ihale başkasına verilince parasını geri istemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Görevli iyiniyetliyse para A'ya iade edilir",
            'B': "Paranın yarısı A'ya, yarısı Devlete verilir",
            'C': 'A, rüşvet suçundan açılan ceza davası sonuçlandıktan sonra parayı geri isteyebilir',
            'D': "Amaç gerçekleşmediğinden para A'ya iade edilir",
            'E': 'Para geri istenemez; hâkim Devlete mal edilmesine karar verebilir',
        },
        'E',
        "TBK m. 81'e göre **hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey geri istenemez**; ancak açılan davada **hâkim, bu şeyin Devlete mal edilmesine** karar verebilir.",
        '6098 sayılı TBK m. 81',
    ),
    # düzey 3
    '0050': patch(
        "Zenginleşme 1 Nisan 2016'da gerçekleşmiş; hak sahibi geri isteme hakkı olduğunu 1 Şubat 2026'da öğrenmiştir. İstem en geç hangi tarihte zamanaşımına uğrar?",
        {
            'A': '1 Şubat 2028',
            'B': '1 Şubat 2027',
            'C': '1 Nisan 2036',
            'D': '1 Nisan 2026',
            'E': '1 Nisan 2018',
        },
        'D',
        "TBK m. 82/1'e göre öğrenmeden itibaren iki yıl (1 Şubat 2028) ve **her hâlde zenginleşmeden itibaren on yıl** (1 Nisan 2026) geçmekle zamanaşımı dolar; hangisi önce dolarsa o esas alınır: **1 Nisan 2026**.",
        '6098 sayılı TBK m. 82/1',
    ),
    # düzey 3
    '0051': patch(
        "Fazla ödeme 2023 yılında yapılmış, ödeyen A fazla ödeme yaptığını ve geri isteme hakkı olduğunu 10 Ocak 2024'te öğrenmiştir. A dava açmak için 15 Mart 2026'ya kadar beklemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Zamanaşımı öğrenme tarihinden işlemeye başlamıştır',
            'B': 'On yıllık süre dolmadığından istem zamanaşımına uğramamıştır',
            'C': "İki yıllık süre 10 Ocak 2026'da dolmuştur",
            'D': "Zenginleşen zamanaşımı def'ini ileri sürebilir",
            'E': 'On yıllık süre ancak üst sınır işlevi görür',
        },
        'B',
        "TBK m. 82/1'e göre istem, öğrenmeden itibaren **iki yılın ve her hâlde** zenginleşmeden itibaren on yılın geçmesiyle zamanaşımına uğrar; iki süreden **önce dolan** esas alınır. İki yıllık süre 10 Ocak 2026'da dolduğundan istem zamanaşımına uğramıştır.",
        '6098 sayılı TBK m. 82/1',
    ),
    # düzey 2
    '0052': patch(
        'Bir burs sözleşmesinde, öğrencinin okulu bırakması hâlinde bursun sona ereceği kararlaştırılmıştır. Öğrenci okulu bıraktıktan sonra da iki ay burs ödenmiştir. Bu iki aylık ödemenin geri istenmesi hangi sebep türüne dayanır?',
        {
            'A': 'Sona ermiş sebep',
            'B': 'Ahlaki ödev',
            'C': 'Geçerli olmayan sebep',
            'D': 'Gerçekleşmemiş sebep',
            'E': 'Hukuka aykırı amaç',
        },
        'A',
        "Başlangıçta geçerli olan burs ilişkisi, bozucu şartın (okulu bırakma) gerçekleşmesiyle **sona ermiştir**. Sonraki ödemeler TBK m. 77/2'deki **sona ermiş sebebe** dayanır ve geri istenebilir.",
        '6098 sayılı TBK m. 77/2',
    ),
    # düzey 2
    '0053': patch(
        'İyiniyetli zenginleşenin giderlerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yararlı giderlerinin tamamını isteyebilir',
            'B': 'Zorunlu giderlerinin tamamını isteyebilir',
            'C': 'Süs ve zevk için yaptığı giderlerin tamamını isteyebilir',
            'D': 'Giderleri geri verme isteminde bulunandan ister',
            'E': 'Karşılık önerilmezse ayrılabilir eklemeleri alabilir',
        },
        'C',
        "TBK m. 80/1'e göre iyiniyetli zenginleşen **zorunlu ve yararlı** giderlerini isteyebilir; m. 80/3'e göre iyiniyetli olup olmadığına bakılmaksızın **diğer giderlerinin ödenmesini isteyemez**, yalnız karşılık önerilmezse ayrılabilir eklemeleri alabilir.",
        '6098 sayılı TBK m. 80',
    ),
    # düzey 3
    '0054': patch(
        'İyiniyetli zenginleşen D, geri vermesi gereken dükkânda 8.000 ₺ zorunlu, 12.000 ₺ yararlı ve 20.000 ₺ süs gideri yapmıştır. D, geri isteyenden kaç ₺ isteyebilir?',
        {
            'A': '8.000',
            'B': '32.000',
            'C': '12.000',
            'D': '40.000',
            'E': '20.000',
        },
        'E',
        "TBK m. 80/1'e göre iyiniyetli zenginleşen **zorunlu ve yararlı giderlerini** isteyebilir: 8.000 + 12.000 = **20.000 ₺**. m. 80/3'e göre süs giderleri gibi **diğer giderler istenemez**.",
        '6098 sayılı TBK m. 80',
    ),
    # düzey 2
    '0055': patch(
        'Borçlanılmamış edimin ifasına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ahlaki bir ödevin yerine getirilmesiyle sağlanan zenginleşme geri istenebilir',
            'B': 'Kendini borçlu sanarak ifa ettiğini ispat eden geri isteyebilir',
            'C': 'Borç olmadığı hâlde ödenen edimin geri istenmesine ilişkin diğer kanun hükümleri saklıdır',
            'D': 'Zamanaşımına uğramış borcun ifası geri istenemez',
            'E': 'Borçlu olmadığını bilerek ifa eden geri isteyemez',
        },
        'A',
        "TBK m. 78/2'ye göre **zamanaşımına uğramış bir borcun ifasından veya ahlaki bir ödevin yerine getirilmiş olmasından** kaynaklanan zenginleşmeler geri istenemez; m. 78/3 diğer kanun hükümlerini saklı tutar.",
        '6098 sayılı TBK m. 78',
    ),
    # düzey 3
    '0056': patch(
        'Aşağıdakilerden hangileri gerçekleşmemiş veya sona ermiş sebebe dayanan edime örnektir?\n\nI. Resmî şekle uyulmadan yapılan taşınmaz satışı için ödenen bedel\n\nII. Kurulması beklenip kurulmayan bir sözleşme için önceden ödenen kapora\n\nIII. Sona eren kira sözleşmesinden sonraki dönem için peşin ödenmiş kira',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'Yalnız II',
            'D': 'Yalnız III',
            'E': 'I, II ve III',
        },
        'A',
        'Kurulmayan sözleşme için verilen kapora **gerçekleşmemiş** (II), sona eren sözleşmeden sonraki dönem kirası **sona ermiş** sebebe (III) dayanır. Şekle aykırı satışa dayanan ödeme ise **geçerli olmayan** sebebe dayanır (I).',
        '6098 sayılı TBK m. 77/2',
    ),
    # düzey 3
    '0057': patch(
        "Aldatılarak bir sözleşme yapan A, aldatmayı öğrenmesine rağmen kanuni süre içinde sözleşmeyi iptal etmemiştir.\n\nTBK'ya göre A'nın ödediği bedelle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Aldatılan, öğrendiği andan itibaren bir yıl içinde bağlı olmadığını bildirebilir',
            'B': 'Süre geçerse sözleşme onaylanmış sayılır',
            'C': 'Onaylanan sözleşme ödemenin haklı sebebidir',
            'D': 'Süre geçse de bedel sebepsiz zenginleşme yoluyla geri istenebilir',
            'E': 'Bu durumda sebepsiz zenginleşme istemi doğmaz',
        },
        'D',
        'TBK m. 39: aldatma nedeniyle yanılan taraf, aldatmayı öğrendiği andan başlayarak bir yıl içinde sözleşmeyle bağlı olmadığını bildirmezse sözleşmeyi onaylamış sayılır. Geçerli hâle gelen sözleşme ödemenin haklı sebebidir; sebepsiz zenginleşme istemi doğmaz.',
        '6098 sayılı TBK m. 39, 77',
    ),
    # düzey 2
    '0058': patch(
        'Bir aday, seçimde kendisine oy vermeleri için bazı seçmenlere para dağıtmış, seçimi kaybedince paraları geri istemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Amacın gerçekleşmemesi geri istenememe kuralını değiştirmez',
            'B': 'Paralar hukuka aykırı bir amaçla verilmiştir',
            'C': 'Seçim kaybedildiğinden amaç gerçekleşmemiştir; paralar adaya iade edilir',
            'D': 'Hâkim paraların Devlete mal edilmesine karar verebilir',
            'E': 'Aday dağıttığı paraları geri isteyemez',
        },
        'C',
        "TBK m. 81'e göre **hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey geri istenemez**; açılan davada hâkim bunun Devlete mal edilmesine karar verebilir.",
        '6098 sayılı TBK m. 81',
    ),
    # düzey 3
    '0059': patch(
        'A, geçerli bir satış sözleşmesiyle bir malı piyasa değerinin üzerinde bir bedelle satın almış; sonradan pahalı aldığını anlamıştır. Aşırı yararlanma koşulları oluşmamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Piyasa değerini aşan fark sebepsiz zenginleşme olarak geri istenebilir',
            'B': 'Geçerli sözleşme ödemenin haklı sebebidir',
            'C': 'Pahalı alım tek başına sebepsiz zenginleşme oluşturmaz',
            'D': 'Satıcının elde ettiği bedel haklı bir sebebe dayanır',
            'E': 'Aşırı yararlanma koşulları bulunsaydı sözleşmenin iptali gündeme gelebilirdi',
        },
        'A',
        "TBK m. 77'ye göre geri verme yükümlülüğü, zenginleşmenin **haklı bir sebebe dayanmaması** hâlinde doğar. Geçerli sözleşme ödemenin haklı sebebidir; aşırı yararlanma (m. 28) ayrı bir iptal sebebidir.",
        '6098 sayılı TBK m. 77',
    ),
    # düzey 2
    '0060': patch(
        "A, B'ye 10.000 ₺ borçlu olduğu hâlde hesap hatası nedeniyle 14.000 ₺ ödemiştir. A kendisini fazlaya da borçlu sanarak ödediğini ispat etmiştir. A kaç ₺ geri isteyebilir?",
        {
            'A': '2.000',
            'B': '4.000',
            'C': '14.000',
            'D': '10.000',
            'E': '0',
        },
        'B',
        "Ödemenin 10.000 ₺'lik kısmı mevcut borca, yani haklı bir sebebe dayanır. Borçlanılmayan 4.000 ₺'lik fazla ödeme, TBK m. 78/1'e göre **kendini borçlu sanarak** ödendiği ispat edildiğinden **4.000 ₺** geri istenebilir.",
        '6098 sayılı TBK m. 78/1',
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
    print(f"1 paket / {len(PATCHES)} soru ('Sebepsiz Zenginlesme' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
