#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Borc Iliskisi ve Kaynaklari — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surumde tanim sorulari agirlikliydi ve celdiricilerin buyuk kismi mutlak ifadeliydi, kor %43): alacak hakkinin nispiligi ve kaynak ayrimi, eksik borc (zamanasimi, kumar), vekaletsiz is gorme, halefiyet, ucuncu kisinin fiilini ustlenme, ucuncu kisi yararina sozlesme, sorumluluk sigortasi, alacagin devri (sekil, iyiniyetli ifa, savunma ve takas, garanti, ifaya yonelik devir), borcun ustlenilmesi, borca katilma, isletme devri, sozlesmenin devri ve sozlesmeye katilma. Gercek sinavdaki alacagin iradi devri yanlis listesi olaylara ve hesaplara cevrildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 49, 78, 127-130, 161, 183-206, 526-531, 604-605 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/borc_iliskisi_kaynaklari.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "borc-iliski-gen-"


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
        "A, B'den satın aldığı ve bedelini ödediği halıyı teslim almadan önce B, halıyı iyiniyetli C'ye satıp teslim etmiştir. A'nın hakları hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A'nın alacak hakkı B'ye yöneliktir; halıyı C'den isteyemez",
            'B': "C'nin satın alması kesin hükümsüzdür",
            'C': "A, mülkiyet hakkına dayanarak halıyı C'den geri alabilir",
            'D': "A, halıyı B ve C'den müteselsilen isteyebilir",
            'E': "A ve C'nin hakları eşit olduğundan halı aralarında paylaştırılır",
        },
        'A',
        "Borç ilişkisinden doğan **alacak hakkı nispi bir haktır; ancak borçluya karşı** ileri sürülebilir. Taşınır mülkiyeti zilyetliğin devriyle geçtiğinden (TMK m. 763) halı teslim alınmadıkça A malik olmamıştır; A, B'ye karşı borca aykırılık hükümlerine (TBK m. 112) başvurabilir.",
        '6098 sayılı TBK m. 112; 4721 sayılı TMK m. 763',
    ),
    # düzey 3
    '0002': patch(
        "B, 40.000 ₺'lik borcunun zamanaşımına uğradığını bilmeden alacaklıya ödeme yapmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Zamanaşımı borcu sona erdirmez, eksik borca dönüştürür',
            'B': 'Alacaklı yapılan ödemeyi alıkoyabilir',
            'C': 'Ödenen tutar sebepsiz zenginleşme sayılmaz',
            'D': 'B, zamanaşımını öğrenince ödediğini geri isteyebilir',
            'E': "Hâkim zamanaşımını re'sen dikkate alamaz",
        },
        'D',
        "Zamanaşımı borcu ortadan kaldırmaz; dava ile istenemeyen **eksik borç** hâline getirir. TBK m. 78/2'ye göre **zamanaşımına uğramış bir borcun ifası amacıyla yapılan edimler geri istenemez**; m. 161'e göre hâkim zamanaşımını kendiliğinden göz önünde tutamaz.",
        '6098 sayılı TBK m. 78/2, 161',
    ),
    # düzey 2
    '0003': patch(
        "Ergin olmayan ve sözleşme ehliyetinden yoksun A, komşusu adına vekâletsiz iş görmüş, ancak özensiz davranarak işi kötü yapmıştır. A'nın sorumluluğu hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Vekâlet hükümlerine göre sorumludur',
            'B': 'Kural olarak zenginleştiği ölçüde sorumludur',
            'C': 'Sorumluluk velisine geçer, kendisi sorumlu olmaz',
            'D': 'Her türlü ihmalinden tam olarak sorumludur',
            'E': 'Beklenmedik hâlden de sorumludur',
        },
        'B',
        "TBK m. 528'e göre işgören sözleşme ehliyetinden yoksunsa, yaptığı işlemden **ancak zenginleştiği ölçüde veya iyiniyetli olmaksızın elinden çıkardığı zenginleşme miktarıyla** sorumlu olur; haksız fiilden doğan daha kapsamlı sorumluluk saklıdır.",
        '6098 sayılı TBK m. 528',
    ),
    # düzey 1
    '0004': patch(
        "B tatildeyken komşusu A, B'nin çatısını onartmıştır. B, dönüşünde yapılan işi uygun bulduğunu bildirmiştir. Taraflar arasındaki ilişkiye hangi hükümler uygulanır?",
        {
            'A': 'Hizmet sözleşmesi hükümleri',
            'B': 'Sebepsiz zenginleşme hükümleri',
            'C': 'Vekâlet sözleşmesi hükümleri',
            'D': 'Haksız fiil hükümleri',
            'E': 'Eser sözleşmesi hükümleri',
        },
        'C',
        "TBK m. 531'e göre **iş sahibi yapılan işi uygun bulmuşsa vekâlet hükümleri** uygulanır.",
        '6098 sayılı TBK m. 531',
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdakilerden hangileri borç ilişkisine ilişkin olarak doğrudur?\n\nI. Alacak hakkı kural olarak ancak borçluya karşı ileri sürülebilir\n\nII. Zamanaşımına uğramış bir borcun ifası geri istenemez\n\nIII. Vekâletsiz işgören, işi sahibinin varsayılan iradesine uygun görmelidir',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'E',
        "Alacak hakkı nispidir (I). TBK m. 78/2'ye göre zamanaşımına uğramış borcun ifası geri istenemez (II). m. 526'ya göre vekâletsiz işgören işi sahibinin menfaatine ve varsayılan iradesine uygun görmelidir (III).",
        '6098 sayılı TBK m. 78, 526, 604',
    ),
    # düzey 3
    '0006': patch(
        "Borçlu B, borcunu ödemesi için arkadaşı C ile anlaşmış ve ifadan önce alacaklı A'ya C'nin kendisine halef olacağını bildirmiştir. C borcu ödemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Halefiyet A'nın yazılı rızasına bağlıdır",
            'B': 'Bildirimi borçlunun yapması öngörülmüştür',
            'C': 'Diğer halefiyet hâllerine ilişkin hükümler saklıdır',
            'D': "C, ifası ölçüsünde A'nın haklarına halef olur",
            'E': 'Halefiyet için bildirimin ifadan önce yapılması gerekir',
        },
        'A',
        "TBK m. 127/1-2'ye göre **alacaklıya ifada bulunan üçüncü kişinin ona halef olacağı, borçlu tarafından ifadan önce alacaklıya bildirilmişse** üçüncü kişi ifası ölçüsünde halef olur; alacaklının rızası aranmaz.",
        '6098 sayılı TBK m. 127',
    ),
    # düzey 3
    '0007': patch(
        "İşveren A, çalışanlarına karşı hukuki sorumluluğunu güvenceye almak için sigorta yaptırmıştır. İş kazasında yaralanan çalışan B'nin genel hükümlere göre tazminatı 300.000 ₺'dir; sigortadan B'ye 120.000 ₺ ödenmiştir. A'nın B'ye ayrıca ödemesi gereken tutar kaç ₺'dir?",
        {
            'A': '420.000',
            'B': '300.000',
            'C': '180.000',
            'D': '150.000',
            'E': '120.000',
        },
        'C',
        "TBK m. 130'a göre çalıştıran, çalışana karşı sorumluluğu için sigorta yaptırmışsa **sigortadan doğan haklar doğrudan çalışana ait olur**; ancak **çalışana ödenecek sigorta tazminatı, genel hükümlere göre ödenecek tazminattan indirilir**: 300.000 − 120.000 = **180.000 ₺**.",
        '6098 sayılı TBK m. 130',
    ),
    # düzey 3
    '0008': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Başkasının borcu için rehnedilen malını rehinden kurtaran malik, alacaklıya halef olur\n\nII. Üçüncü kişinin fiilini üstlenen, fiil gerçekleşmezse doğan zararı giderir\n\nIII. İşverenin çalışanı için yaptırdığı sorumluluk sigortasından doğan haklar işverene aittir',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'I ve II',
        },
        'E',
        "TBK m. 127'ye göre rehnedilen malını kurtaran malik halef olur (I); m. 128'e göre üçüncü kişinin fiilini üstlenen zararı giderir (II). m. 130'a göre sigortadan doğan haklar **doğrudan çalışana** aittir (III yanlış).",
        '6098 sayılı TBK m. 127-130',
    ),
    # düzey 2
    '0009': patch(
        "A, B'den olan alacağını C'ye sözlü olarak devretmiş; ayrıca başka bir alacağını D'ye devredeceğini sözlü olarak vaat etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "D'ye verilen devir sözü şekle bağlı değildir",
            'B': 'Alacağın devrinin geçerliliği yazılı şekle bağlıdır',
            'C': 'Devir sözü ile devir işlemi şekil bakımından ayrı değerlendirilir',
            'D': "A'nın C'ye yaptığı sözlü devir geçerlidir",
            'E': "C'ye yapılan devir şekil eksikliği nedeniyle geçersizdir",
        },
        'D',
        "TBK m. 184'e göre **alacağın devrinin geçerliliği yazılı şekilde yapılmış olmasına bağlıdır**; buna karşılık **alacağın devri sözü verme şekle bağlı değildir**.",
        '6098 sayılı TBK m. 184',
    ),
    # düzey 2
    '0010': patch(
        "Bir alacağın A'ya mı yoksa C'ye mi ait olduğu mahkemede çekişmelidir ve borç muacceldir. Borçlu B'nin durumu hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'B, çekişme bitene kadar temerrüt faizi öder',
            'B': 'B, dilediği alacaklıya ödeyerek sorumluluktan kurtulur',
            'C': 'B, alacağın yarısını her birine ödemelidir',
            'D': 'B, çekişme nedeniyle borçtan kurtulmuş sayılır',
            'E': 'B, edimi hâkimin belirlediği yere tevdi ederek borçtan kurtulabilir',
        },
        'E',
        "TBK m. 187'ye göre kime ait olduğu çekişmeli bulunan bir alacağın borçlusu **ifadan kaçınabilir ve alacağın konusunu hâkim tarafından belirlenen yere tevdi etmekle borçtan kurtulur**; borç muaccelse taraflardan her biri borçluyu tevdie zorlayabilir.",
        '6098 sayılı TBK m. 187',
    ),
    # düzey 3
    '0011': patch(
        "B, A'dan aldığı ayıplı mal nedeniyle bedelde indirim isteme hakkına sahiptir. A, bedel alacağını C'ye devretmiş; B devri öğrendiğinde ayıp zaten ortaya çıkmıştır. C bedelin tamamını istemektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Savunmalar devirle ortadan kalktığından B tamamını öder',
            'B': "B, önce tamamını ödeyip sonra A'ya başvurmalıdır",
            'C': "C'nin iyiniyeti B'nin savunmasını ortadan kaldırır",
            'D': "B, indirim savunmasını C'ye karşı da ileri sürebilir",
            'E': "B, savunmasını ancak A'ya karşı ileri sürebilir",
        },
        'D',
        "TBK m. 188/1'e göre **borçlu, devri öğrendiği sırada devredene karşı sahip olduğu savunmaları devralana karşı da ileri sürebilir**. Devir, borçlunun hukuki durumunu ağırlaştırmaz.",
        '6098 sayılı TBK m. 188/1',
    ),
    # düzey 3
    '0012': patch(
        "A, B'den olan 100.000 ₺'lik alacağını 90.000 ₺ karşılığında C'ye devretmiştir. Sonradan B'nin devir sırasında da ödeme gücünün bulunmadığı anlaşılmıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A, alacağın varlığını garanti eder; ödeme gücünden sorumlu değildir',
            'B': "A'nın garanti yükümlülüğü ancak açıkça kararlaştırılırsa doğar",
            'C': "A, devir sırasında B'nin ödeme gücünü garanti etmiş olur",
            'D': "Ödeme gücüzlüğü riski devirle C'ye geçmiştir",
            'E': "C, ancak B iflas ederse A'ya başvurabilir",
        },
        'C',
        "TBK m. 191/1'e göre **alacak bir edim karşılığında devredilmişse devreden, devir sırasında alacağın varlığını ve borçlunun ödeme gücüne sahip olduğunu garanti etmiş olur**.",
        '6098 sayılı TBK m. 191/1',
    ),
    # düzey 2
    '0013': patch(
        "A, B'den olan alacağını karşılıksız olarak yeğeni C'ye devretmiştir. Daha sonra B'nin ödeme gücünün olmadığı ortaya çıkmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Ödeme gücü garantisi ivazlı devirde söz konusudur',
            'B': 'A, alacağın varlığından da sorumlu değildir',
            'C': 'Ödeme gücüzlüğünün sonucuna C katlanır',
            'D': 'Devir bir edim karşılığı olmaksızın yapılmıştır',
            'E': "A, B'nin ödeme gücünden C'ye karşı sorumludur",
        },
        'E',
        "TBK m. 191/2'ye göre **alacak bir edim karşılığı olmaksızın devredilmiş ya da kanun gereğince başkasına geçmişse, devreden alacağın varlığından ve borçlunun ödeme gücünden sorumlu değildir**.",
        '6098 sayılı TBK m. 191/2',
    ),
    # düzey 3
    '0014': patch(
        "C, B ile yaptığı iç üstlenme sözleşmesinde B'yi A'ya olan borcundan kurtarmayı, B de buna karşılık C'ye 10.000 ₺ ödemeyi üstlenmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "B, kendi edimini ifa etmeden C'den ifa isteyebilir",
            'B': "C, borcu bizzat ifa ederek B'yi kurtarabilir",
            'C': "C, alacaklının rızasıyla borcu üstlenerek de B'yi kurtarabilir",
            'D': "Borçtan kurtarılmayan B, C'den güvence isteyebilir",
            'E': "C'nin yükümlülüğü B'ye karşıdır",
        },
        'A',
        "TBK m. 195'e göre üstlenen borcu bizzat ifa ederek veya alacaklının rızasıyla üstlenerek borçluyu kurtarır; **borçlu, iç üstlenme sözleşmesinden doğan borçlarını ifa etmedikçe, diğer taraftan yükümlülüğünü yerine getirmesini isteyemez**; kurtarılmamışsa güvence isteyebilir.",
        '6098 sayılı TBK m. 195',
    ),
    # düzey 2
    '0015': patch(
        "C, B'nin A'ya olan borcunu, B'nin yerine geçerek üstlenmek istemektedir. B'nin borçtan kurtulması için aşağıdakilerden hangisi gereklidir?",
        {
            'A': 'B ile C arasında yazılı iç üstlenme sözleşmesi',
            'B': 'C ile alacaklı A arasında dış üstlenme sözleşmesi',
            'C': 'A, B ve C arasında yapılacak bir sözleşmenin devri anlaşması',
            'D': "C'nin tek taraflı borç tanıması",
            'E': "A ile B arasında ibra ve C'nin kefaleti",
        },
        'B',
        "TBK m. 196/1'e göre **borçlunun yerine yenisinin geçmesi ve borcundan kurtarılması, borcu üstlenen ile alacaklı arasında yapılacak sözleşmeyle** olur (dış üstlenme).",
        '6098 sayılı TBK m. 196/1',
    ),
    # düzey 3
    '0016': patch(
        "C'nin B'nin borcunu üstlenme önerisi alacaklı A'ya yapılmıştır. A kabul etmeden önce B, D ile yeni bir iç üstlenme sözleşmesi yapmış ve bu ikinci üstlenme de A'ya önerilmiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "C ile D, A'ya karşı müteselsilen sorumlu olur",
            'B': 'Her iki üstlenen borçtan eşit paylarla sorumlu olur',
            'C': 'İlk öneride bulunan, önerisiyle bağlı olmaktan kurtulur',
            'D': 'A, iki öneriden dilediğini kabul edebilir',
            'E': 'İkinci öneri, ilki reddedilmedikçe geçersizdir',
        },
        'C',
        "TBK m. 197/2'ye göre önerinin alacaklı tarafından kabulünden önce **yeni bir iç üstlenme sözleşmesi yapılır ve bu ikinci üstlenmeye ilişkin olarak alacaklıya öneride bulunulursa, ilk öneride bulunan önerisi ile bağlı olmaktan kurtulur**.",
        '6098 sayılı TBK m. 197/2',
    ),
    # düzey 3
    '0017': patch(
        "A ile C arasındaki dış üstlenme sözleşmesi hükümsüz hâle gelmiştir. Eski borç, B'nin evi üzerindeki ipotekle güvence altındaydı. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Eski borç, bağlı borçlarıyla birlikte sona ermiş olur',
            'B': 'İyiniyetli üçüncü kişilerin hakları saklıdır',
            'C': "Güvencesini yitiren A, zararını C'den isteyebilir",
            'D': "C, kusursuzluğunu ispat etmedikçe A'nın zararını gidermelidir",
            'E': 'Eski borç bağlı borçlarıyla birlikte varlığını sürdürür',
        },
        'A',
        "TBK m. 200'e göre **dış üstlenme sözleşmesi hükümsüz hâle gelirse, iyiniyetli üçüncü kişilerin hakları saklı kalmak üzere, eski borç bütün bağlı borçlarıyla birlikte varlığını sürdürür**; üstlenen kusursuzluğunu ispat etmedikçe alacaklının zararını giderir.",
        '6098 sayılı TBK m. 200',
    ),
    # düzey 3
    '0018': patch(
        "A, işletmesini aktif ve pasifleriyle B'ye devretmiş; devir 1 Mart 2025'te ilan edilmiştir. İşletmenin C'ye olan bir borcu 1 Eylül 2025'te muaccel olacaktır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'B, ilan tarihinden itibaren alacaklılara karşı sorumludur',
            'B': "A'nın sorumluluğu 1 Eylül 2027'ye kadar sürer",
            'C': "Bu borç için iki yıllık süre 1 Eylül 2025'te başlar",
            'D': "A'nın bu borçtan sorumluluğu 1 Mart 2027'de sona erer",
            'E': 'A, iki yıl süreyle B ile müteselsilen sorumlu kalır',
        },
        'D',
        "TBK m. 202/2'ye göre önceki borçlunun iki yıllık müteselsil sorumluluk süresi, muaccel borçlar için duyuru tarihinden; **daha sonra muaccel olacak borçlar için ise muacceliyet tarihinden** işlemeye başlar. Bu borç için süre 1 Eylül 2025'te başlar ve 1 Eylül 2027'de dolar.",
        '6098 sayılı TBK m. 202',
    ),
    # düzey 2
    '0019': patch(
        "Kiracı A, kiraya veren B'nin de katıldığı bir anlaşmayla kira sözleşmesini bütün hak ve borçlarıyla birlikte C'ye devretmiştir. Bu işlem aşağıdakilerden hangisidir?",
        {
            'A': 'Borca katılma; A ve C müteselsilen sorumludur',
            'B': 'Taraf sıfatını da geçiren sözleşmenin devri',
            'C': 'Kiracılık alacaklarının devri',
            'D': 'Üçüncü kişi yararına sözleşme',
            'E': 'İç üstlenme sözleşmesi',
        },
        'B',
        "TBK m. 205/1'e göre **sözleşmenin devri**, devralan, devreden ve sözleşmede kalan taraf arasında yapılan ve **devredenin taraf olma sıfatı ile birlikte bütün hak ve borçlarını** devralana geçiren anlaşmadır.",
        '6098 sayılı TBK m. 205/1',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Karşılıksız alacak devrinde devreden, borçlunun ödeme gücünü garanti eder\n\nII. Sözleşmenin devrinin geçerliliği devredilen sözleşmenin şekline bağlıdır\n\nIII. Alacağın devri sözü şekle bağlı değildir',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'Yalnız II',
        },
        'C',
        "TBK m. 205/3'e göre sözleşmenin devri devredilen sözleşmenin şekline bağlıdır (II); m. 184/2'ye göre devir sözü şekle bağlı değildir (III). m. 191/2'ye göre karşılıksız devirde devreden ödeme gücünden **sorumlu değildir** (I yanlış).",
        '6098 sayılı TBK m. 184, 191, 205',
    ),
    # düzey 1
    '0021': patch(
        'Aşağıdaki borçlardan hangisi sözleşmeden doğmaz?',
        {
            'A': 'Kiracının kararlaştırılan kira bedelini ödeme borcu',
            'B': 'Yanlışlıkla havale edilen parayı iade borcu',
            'C': 'Satıcının malı teslim borcu',
            'D': 'Ödünç alanın parayı geri verme borcu',
            'E': 'Vekilin işi özenle görme borcu',
        },
        'B',
        'Kira, satış, ödünç ve vekâlet borçları taraf iradelerinin uyuşmasıyla kurulan **sözleşmeden** doğar. Yanlışlıkla gönderilen paranın iadesi ise haklı bir sebep olmaksızın zenginleşmeden, yani **sebepsiz zenginleşmeden** (TBK m. 77) doğar.',
        '6098 sayılı TBK m. 1, 77',
    ),
    # düzey 3
    '0022': patch(
        "A, arkadaşı B'ye iskambil oyununda kaybettiği 10.000 ₺ için B'ye bono vermiştir. B, bonoyu kumar borcundan kaynaklandığını bilen C'ye ciro etmiştir. Buna göre aşağıdakilerden hangileri doğrudur?\n\nI. B, kumar alacağı için dava açabilir, ancak icra takibi yapamaz\n\nII. C, bonoya dayanarak A aleyhine takip yapabilir\n\nIII. A borcu isteyerek ödeseydi, kural olarak ödediğini geri alamazdı",
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'D',
        "TBK m. 604'e göre kumar ve bahisten doğan alacak için **dava açılamaz ve takip yapılamaz** (I yanlış). m. 605/1'e göre kumar için imzalanan senet üçüncü kişiye devredilse bile ona dayanarak dava ve takip yapılamaz; yalnız kıymetli evrakın **iyiniyetli** üçüncü kişilere sağladığı haklar saklıdır. C kumarı bildiğinden korunmaz (II yanlış). m. 605/2'ye göre **isteyerek yapılan ödemeler kural olarak geri alınamaz** (III).",
        '6098 sayılı TBK m. 604, 605',
    ),
    # düzey 2
    '0023': patch(
        "A, komşusu B tatildeyken B'nin evinde patlayan su borusunu tamir ettirmiş ve 8.000 ₺ ödemiştir. İş, B'nin menfaatine ve varsayılan iradesine uygun olarak yapılmıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'B, masrafın yarısını öder',
            'B': 'A, masrafa ek olarak iş görme karşılığı ayrıca ücret isteyebilir',
            'C': 'B, zorunlu ve yararlı masrafı faiziyle ödemekle yükümlüdür',
            'D': 'B, ancak işi sonradan uygun bulursa masrafı öder',
            'E': "A'nın iş görmesi haksız fiil sayılır, masraf istenemez",
        },
        'C',
        "TBK m. 526'ya göre vekâleti olmaksızın başkasının hesabına iş gören, işi sahibinin menfaatine ve varsayılan iradesine uygun görmelidir. m. 529'a göre iş sahibinin menfaatine yapılmışsa iş sahibi **zorunlu ve yararlı bütün masrafları faiziyle** ödemekle yükümlüdür.",
        '6098 sayılı TBK m. 526, 529',
    ),
    # düzey 2
    '0024': patch(
        "A, komşusu B'nin menfaatine olarak B'nin bahçesine sökülebilir bir sulama sistemi kurmuştur. B, masrafları ödememekte ve A da bunları tahsil edememektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A, sebepsiz zenginleşme hükümlerine göre sistemi ayırıp alabilir',
            'B': 'A, sistemi ayırıp alamaz; masraf hakkı düşer',
            'C': "A, sistemi B'ye kiraya vermiş sayılır",
            'D': 'A, masrafları haksız fiil tazminatı olarak ister',
            'E': "A'nın masrafları bağışlama sayılır",
        },
        'A',
        "TBK m. 529/2'ye göre **işgören, yapmış olduğu giderleri alamadığı takdirde, sebepsiz zenginleşme hükümlerine göre ayırıp alma hakkına** sahiptir.",
        '6098 sayılı TBK m. 529/2',
    ),
    # düzey 3
    '0025': patch(
        "C, arkadaşı B'nin A'ya olan borcu için kendi otomobilini rehin vermiştir. B ödemeyince C, otomobilini rehinden kurtarmak için borcu A'ya ödemiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "C, ancak sebepsiz zenginleşme hükümleriyle B'den isteyebilir",
            'B': "C, B'nin onayı olmadıkça halef olamaz",
            'C': "A, C'nin ödemesini reddetmekle yükümlüdür",
            'D': "C'nin ödemesi bağışlama sayılır",
            'E': "C, ödediği ölçüde A'nın haklarına halef olur",
        },
        'E',
        "TBK m. 127/1-1'e göre **başkasının borcu için rehnedilen bir şeyi rehinden kurtaran ve bu şey üzerinde mülkiyet veya başka bir ayni hakkı bulunan** üçüncü kişi, ifası ölçüsünde alacaklının haklarına halef olur.",
        '6098 sayılı TBK m. 127',
    ),
    # düzey 2
    '0026': patch(
        "A, B'ye karşı C'nin bir fiilini 31 Aralık'a kadar üstlenmiş; taraflar, süre bitimine kadar A'ya yazılı başvurulmazsa sorumluluğunun sona ereceğini kararlaştırmıştır. B, A'ya ilk kez 15 Ocak'ta yazılı olarak başvurmuştur. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A, zararın yarısından sorumlu olur',
            'B': "Sorumluluk C'ye geçer",
            'C': "A'nın sorumluluğu sona ermiştir",
            'D': "A'nın sorumluluğu zamanaşımı dolana kadar sürer",
            'E': 'Kayıt geçersiz olduğundan A sorumlu kalır',
        },
        'C',
        "TBK m. 128/2'ye göre **belirli bir süre için yapılan üstlenmede, sürenin bitimine kadar üstlenene yazılı olarak başvurulmaması hâlinde sorumluluğun sona ereceği kararlaştırılabilir**. Başvuru süre geçtikten sonra yapıldığından A'nın sorumluluğu sona ermiştir.",
        '6098 sayılı TBK m. 128/2',
    ),
    # düzey 3
    '0027': patch(
        "A, mobilyacı B ile yaptığı sözleşmede mobilyaların kızı C'nin evine teslim edilmesini ve C'nin de teslimi isteyebileceğini kararlaştırmıştır. C, bu hakkı kullanmak istediğini B'ye bildirmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Bildirimden sonra da A, B'yi borçtan ibra edebilir",
            'B': "A, edimin C'ye ifa edilmesini isteyebilir",
            'C': "C'ye halef olanlar da ifayı isteyebilir",
            'D': 'C de edimin kendisine ifasını isteyebilir',
            'E': 'Bildirimden sonra borcun kapsamı A tarafından değiştirilemez',
        },
        'A',
        "TBK m. 129'a göre üçüncü kişi yararına sözleşmede alacaklı edimin üçüncü kişiye ifasını isteyebilir; amaç veya örf uygun düşerse üçüncü kişi ve halefleri de isteyebilir. **Üçüncü kişi hakkını kullanmak istediğini borçluya bildirdikten sonra alacaklı borçluyu ibra edemez, borcun nitelik ve kapsamını da değiştiremez**.",
        '6098 sayılı TBK m. 129',
    ),
    # düzey 2
    '0028': patch(
        "A, B'den olan 100.000 ₺'lik alacağını, B'ye haber vermeden C'ye yazılı olarak devretmiştir. Kanun, sözleşme veya işin niteliği devre engel değildir. Devir hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Devir borçlu B'ye bildirilmedikçe kesin hükümsüz sayılır",
            'B': "B, devre itiraz ederek alacağı A'da tutabilir",
            'C': 'Devir ancak noter onayıyla geçerli olur',
            'D': "Devir B'nin yazılı onayıyla geçerli olur",
            'E': "Devrin geçerliliği B'nin rızasına bağlı değildir",
        },
        'E',
        "TBK m. 183/1'e göre kanun, sözleşme veya işin niteliği engel olmadıkça **alacaklı, borçlunun rızasını aramaksızın alacağını üçüncü bir kişiye devredebilir**. Bildirim geçerlilik koşulu değildir; borçlunun iyiniyetli ifası m. 186 ile korunur.",
        '6098 sayılı TBK m. 183/1',
    ),
    # düzey 3
    '0029': patch(
        "A, B'den olan alacağını C'ye yazılı olarak devretmiş; ancak devir ne A ne de C tarafından B'ye bildirilmiştir. B, devirden habersiz olarak borcu A'ya ödemiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "B, borcu C'ye bir kez daha ödemelidir",
            'B': "İyiniyetle A'ya ödeyen B borcundan kurtulur",
            'C': "B'nin ödemesi yarı oranda geçerlidir",
            'D': "Ödeme geçersizdir; B, parayı A'dan geri almalıdır",
            'E': "B, C ile A'ya müteselsilen borçlu kalır",
        },
        'B',
        "TBK m. 186'ya göre **borçlu, alacağın devredildiği devreden veya devralan tarafından kendisine bildirilmemişse, önceki alacaklıya iyiniyetle ifada bulunarak borcundan kurtulur**. C, alacağı A'dan isteyebilir.",
        '6098 sayılı TBK m. 186',
    ),
    # düzey 3
    '0030': patch(
        "Bir alacak A'dan C'ye, C'den de D'ye devredilmiş; son devir borçlu B'ye bildirilmemiştir. B, iyiniyetle C'ye ödeme yapmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "B, C'ye yaptığı ödemeyle borcundan kurtulur",
            'B': 'Bildirim devreden veya devralan tarafından yapılabilir',
            'C': "B'nin iyiniyeti bu sonucun koşuludur",
            'D': "B, son devralan D'ye ayrıca ödeme yapmakla yükümlüdür",
            'E': "D'nin korunması için devrin B'ye bildirilmesi gerekirdi",
        },
        'D',
        "TBK m. 186'ya göre alacak birkaç kez devredilmişse borçlu, **son devralan yerine önceki devralanlardan birine iyiniyetle ifada bulunarak borcundan kurtulur**.",
        '6098 sayılı TBK m. 186',
    ),
    # düzey 3
    '0031': patch(
        "B'nin A'ya olan 100.000 ₺'lik borcunun vadesi 1 Mart'tır. A bu alacağı C'ye devretmiş, B devri 1 Ocak'ta öğrenmiştir. B'nin A'dan olan 40.000 ₺'lik alacağının vadesi ise 1 Nisan'dır. C, 1 Mart'ta ödeme istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "B, 40.000 ₺'lik alacağını C'ye karşı takas edebilir",
            'B': "B, 100.000 ₺'nin tamamını C'ye ödemelidir",
            'C': "B'nin alacağı 1 Mart'tan önce muaccel olsaydı takas mümkündü",
            'D': "B'nin alacağı devredilen alacaktan sonra muaccel olmaktadır",
            'E': "B, 40.000 ₺'yi A'dan vadesinde isteyebilir",
        },
        'A',
        "TBK m. 188/2'ye göre devri öğrendiği anda muaccel olmayan alacak, ancak **devredilen alacaktan önce veya onunla aynı anda muaccel oluyorsa** takas edilebilir. B'nin alacağı daha sonra muaccel olduğundan C'ye karşı takas ileri sürülemez.",
        '6098 sayılı TBK m. 188/2',
    ),
    # düzey 2
    '0032': patch(
        "A, B'den olan, faiz işlemiş ve ipotekle güvence altına alınmış 200.000 ₺'lik alacağını C'ye devretmiştir; devir sözleşmesinde başka bir hüküm yoktur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'İşlemiş faizler de devredilmiş sayılır',
            'B': "İpotek, bağlı hak olarak C'ye geçer",
            'C': 'C, alacağı güvencesiyle birlikte ileri sürebilir',
            'D': "İşlemiş faizler A'da kalır",
            'E': "A'nın kişiliğine özgü öncelik hakları C'ye geçmez",
        },
        'D',
        "TBK m. 189'a göre alacağın devri ile **devredenin kişiliğine özgü olanlar dışındaki öncelik hakları ve bağlı haklar da devralana geçer**; **asıl alacakla birlikte işlemiş faizler de devredilmiş sayılır**.",
        '6098 sayılı TBK m. 189',
    ),
    # düzey 3
    '0033': patch(
        "A, B'den olan alacağını 80.000 ₺ karşılığında C'ye devretmiş; sonradan alacağın hiç doğmamış olduğu anlaşılmıştır. C'nin ödediği bedelin faizi 4.000 ₺, devir giderleri 1.000 ₺, B'ye karşı yaptığı sonuçsuz tahsil girişimlerinin giderleri 2.000 ₺'dir. C'nin ayrıca 10.000 ₺ başka zararı vardır; A kusursuzluğunu ispat etmiştir. C, A'dan toplam kaç ₺ isteyebilir?",
        {
            'A': '85.000',
            'B': '87.000',
            'C': '97.000',
            'D': '80.000',
            'E': '84.000',
        },
        'B',
        "TBK m. 191/1'e göre ivazlı devirde devreden alacağın varlığını garanti eder. m. 193'e göre devralan; karşı edimi faiziyle (80.000 + 4.000), devir giderlerini (1.000) ve sonuçsuz girişim giderlerini (2.000) isteyebilir. Diğer zararlar ise devreden **kusursuzluğunu ispat etmedikçe** istenebilir; A ispat ettiğinden 10.000 ₺ istenemez. Toplam **87.000 ₺**.",
        '6098 sayılı TBK m. 191, 193',
    ),
    # düzey 2
    '0034': patch(
        'Alacağın devrine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Kanun gereği gerçekleşen devir özel bir şekle bağlı değildir\n\nII. Karşılıksız devirde devreden, borçlunun ödeme gücünden sorumludur\n\nIII. Çekişmeli alacağın borçlusu, edimi tevdi ederek borçtan kurtulabilir',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'E',
        "TBK m. 185'e göre yasal devir şekle bağlı değildir (I); m. 187'ye göre çekişmeli alacağın borçlusu tevdi ile borçtan kurtulur (III). m. 191/2'ye göre karşılıksız devirde devreden ödeme gücünden **sorumlu değildir** (II yanlış).",
        '6098 sayılı TBK m. 185, 187, 191',
    ),
    # düzey 3
    '0035': patch(
        "B'nin borcunu iç üstlenmeyle üstlenen C, bunu alacaklı A'ya bildirmiş; A da C'nin yaptığı ödemeyi çekince koymadan kabul etmiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "C'nin ödemesi bağışlama sayılır",
            'B': 'Kabul açık olmadığından B borçlu kalmaya devam eder',
            'C': 'A, borcun üstlenilmesini örtülü olarak kabul etmiş sayılır',
            'D': "A, ödemeyi aldıktan sonra da B'den ifa isteyebilir",
            'E': "A'nın kabulü yazılı yapılmadıkça hüküm doğurmaz",
        },
        'C',
        "TBK m. 196'ya göre iç üstlenmenin alacaklıya bildirilmesi dış üstlenme önerisidir. **Alacaklının kabulü açık veya örtülü olabilir**; çekince ileri sürmeksizin üstlenenin ifasını kabul eden alacaklı **borcun üstlenilmesini kabul etmiş sayılır**.",
        '6098 sayılı TBK m. 196',
    ),
    # düzey 3
    '0036': patch(
        "C, B'nin A'ya olan borcunu dış üstlenmeyle üstlenmiştir. Borç için D kefil olmuş, E de taşınmazını rehin vermiştir. D ve E üstlenmeye rıza göstermemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Borçlunun kişiliğine özgü olmayan bağlı haklar saklı kalır',
            'B': 'Kefil ve rehin verenin sorumluluğu yazılı rızalarına bağlıdır',
            'C': 'Yazılı rıza gösterselerdi sorumlulukları devam ederdi',
            'D': "Kefil D, C'nin borcu için de sorumlu kalır",
            'E': "E'nin rehin veren olarak sorumluluğu sona erer",
        },
        'D',
        "TBK m. 198'e göre borçlu değişse de kişiliğe özgü olmayan bağlı haklar saklı kalır; ancak **borcun güvencesi olarak rehin veren üçüncü kişinin ve kefilin sorumlulukları, ancak onların borcun üstlenilmesine yazılı olarak rıza göstermeleri hâlinde** devam eder.",
        '6098 sayılı TBK m. 198',
    ),
    # düzey 2
    '0037': patch(
        "D, B'nin A'ya olan borcuna, B'nin yanında yer almak üzere A ile yaptığı sözleşmeyle katılmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "D ve B, A'ya karşı müteselsilen sorumludur",
            'B': "A, borcun tamamını D'den isteyebilir",
            'C': "D, B'nin yanında yer alarak borca katılmıştır",
            'D': 'Katılma, D ile A arasında yapılan bir sözleşmedir',
            'E': "D'nin katılmasıyla B borçtan kurtulur",
        },
        'E',
        "TBK m. 201'e göre **borca katılma**, mevcut bir borca borçlunun yanında yer almak üzere katılan ile alacaklı arasında yapılan sözleşmedir; **borca katılan ile borçlu, alacaklıya karşı müteselsilen sorumlu** olur. Borçlu borçtan kurtulmaz.",
        '6098 sayılı TBK m. 201',
    ),
    # düzey 2
    '0038': patch(
        'Aşağıdakilerden hangileri malvarlığının veya işletmenin devralınmasına ilişkin olarak doğrudur?\n\nI. İşletmeyi aktif ve pasifleriyle devralan, ilan tarihinden başlayarak işletme borçlarından sorumlu olur\n\nII. Önceki borçlu, devirle birlikte işletme borçlarından kurtulur\n\nIII. Birleşen işletmelerin alacaklıları alacaklarını yeni işletmeden isteyemez',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'B',
        "TBK m. 202/1'e göre devralan, bildirim veya ilan tarihinden başlayarak borçlardan sorumlu olur (I). m. 202/2'ye göre önceki borçlu **iki yıl süreyle devralanla birlikte müteselsilen** sorumlu kalır (II yanlış); m. 203'e göre birleşmede her iki işletmenin alacaklıları **bütün alacaklarını yeni işletmeden** alabilir (III yanlış).",
        '6098 sayılı TBK m. 202, 203',
    ),
    # düzey 3
    '0039': patch(
        "A, taşınmaz satış vaadi sözleşmesinden doğan alıcı konumunu C'ye devretmek istemektedir; satıcı B buna önceden izin vermiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Devrin geçerliliği satış vaadinin şekline bağlıdır',
            'B': "B'nin sonradan onayı da aynı sonucu doğururdu",
            'C': 'Devir adi yazılı şekille geçerli olur',
            'D': "Devir, A ile C arasında B'nin önceden izniyle yapılabilir",
            'E': 'Taşınmaz satış vaadi resmî şekle tabidir',
        },
        'C',
        "TBK m. 205/2'ye göre devralan ile devreden arasında yapılan ve kalan tarafın **önceden verdiği izne dayanan veya sonradan onaylanan** anlaşma da sözleşmenin devridir. m. 205/3'e göre **devrin geçerliliği devredilen sözleşmenin şekline bağlıdır**; taşınmaz satış vaadi resmî şekle tabi olduğundan devir de resmî şekilde yapılmalıdır.",
        '6098 sayılı TBK m. 205, 237',
    ),
    # düzey 3
    '0040': patch(
        "C, aylık kirası 30.000 ₺ olan bir kira sözleşmesine kiracı A'nın yanında yer almak üzere katılmıştır; aksi kararlaştırılmamıştır. İki aylık kira ödenmemiştir. Kiraya veren B, C'den en fazla kaç ₺ isteyebilir?",
        {
            'A': '30.000',
            'B': '45.000',
            'C': '120.000',
            'D': '60.000',
            'E': '15.000',
        },
        'D',
        "TBK m. 206/2'ye göre aksi kararlaştırılmadıkça sözleşmeye katılan ile yanında yer aldığı taraf **müteselsilen borçlu** olur; B ödenmeyen iki aylık kiranın tamamını C'den isteyebilir: 2 × 30.000 = **60.000 ₺**.",
        '6098 sayılı TBK m. 206',
    ),
    # düzey 2
    '0041': patch(
        'Bir boyacı, sözleşmeyle boyamayı üstlendiği evde çalışırken dikkatsizliğiyle hem ev sahibinin mobilyasını hem de sokakta park hâlindeki bir yayanın aracını boyamıştır. Boyacının sorumluluğu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her ikisine karşı sebepsiz zenginleşmeden sorumludur',
            'B': 'Her ikisine vekâletsiz iş görme hükümleri uygulanır',
            'C': 'Her ikisine karşı sözleşmeye aykırılıktan sorumludur',
            'D': 'Yayaya karşı sorumluluk ev sahibine aittir',
            'E': 'Ev sahibine karşı sözleşmeye aykırılıktan, yayaya karşı haksız fiilden sorumludur',
        },
        'E',
        'Ev sahibiyle boyacı arasında sözleşme bulunduğundan mobilya zararı **borca aykırılık** (TBK m. 112) hükümlerine tabidir. Yaya ile boyacı arasında bir sözleşme yoktur; kusurlu ve hukuka aykırı fiille verilen zarar **haksız fiil** (TBK m. 49) hükümlerine göre giderilir.',
        '6098 sayılı TBK m. 49, 112',
    ),
    # düzey 3
    '0042': patch(
        'A, komşusunun açıkça yasaklamasına rağmen onun bahçesindeki ağacı budatmış; budamanın ardından çıkan fırtına ağaca zarar vermiştir. Yasaklama hukuka ve ahlaka aykırı değildir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Vekâletsiz işgören her türlü ihmalinden sorumludur',
            'B': 'Budama yapılmasaydı da zararın doğacağını ispat ederse A kurtulur',
            'C': 'Fırtına beklenmedik hâl olduğundan A sorumlu tutulamaz',
            'D': 'Yasaklamaya rağmen iş gördüğü için A beklenmedik hâlden de sorumludur',
            'E': 'Yasaklama hukuka aykırı olsaydı sonuç değişebilirdi',
        },
        'C',
        "TBK m. 527'ye göre vekâletsiz işgören her türlü ihmalinden sorumludur; iş sahibinin **hukuka ve ahlaka aykırı olmayan yasaklamasına karşın** işi yapmışsa **beklenmedik hâlden de sorumlu** olur. Ancak işi yapmasaydı da zararın gerçekleşeceğini ispat ederse sorumluluktan kurtulur.",
        '6098 sayılı TBK m. 527',
    ),
    # düzey 3
    '0043': patch(
        "A, komşusu B'nin boş arsasını, B'ye haber vermeden kendi hesabına otopark olarak işletmiş ve 50.000 ₺ gelir elde etmiştir. B'nin hakları hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'B, ancak emsal kira bedeli kadar isteyebilir',
            'B': "B'nin hakkı haksız fiil tazminatıyla sınırlıdır",
            'C': "Gelir, işi yapan A'ya kalır",
            'D': 'B, işten doğan faydaları edinme hakkına sahiptir',
            'E': 'Gelir A ile B arasında eşit paylaşılır',
        },
        'D',
        "TBK m. 530'a göre iş sahibi, **iş kendi menfaatine yapılmamış olsa bile işgörmeden doğan faydaları edinme hakkına** sahiptir; ancak zenginleştiği ölçüde işgörenin masraflarını ödemek ve giriştiği borçlardan onu kurtarmakla yükümlüdür.",
        '6098 sayılı TBK m. 530',
    ),
    # düzey 2
    '0044': patch(
        'Ücret kararlaştırılmayan ve ücret ödenmesi âdet de olmayan bir vekâlet sözleşmesinde vekil, işi görürken masraf yapmıştır. Bu sözleşme borç yükleme bakımından hangi türdendir?',
        {
            'A': 'Eksik iki tarafa borç yükleyen sözleşme',
            'B': 'Tek tarafa borç yükleyen, masraf istenemeyen sözleşme',
            'C': 'Sebepsiz zenginleşme ilişkisi',
            'D': 'Vekâletsiz iş görme ilişkisi',
            'E': 'Tam iki tarafa borç yükleyen sözleşme',
        },
        'A',
        'Ücretsiz vekâlette asıl edim yükümü vekildedir; müvekkilin masrafları ödeme borcu (TBK m. 510) sonradan ve koşullu olarak doğar. Bu nedenle sözleşme **eksik iki tarafa borç yükleyen** sözleşmedir.',
        '6098 sayılı TBK m. 393, 502, 510',
    ),
    # düzey 1
    '0045': patch(
        'Aşağıdaki sözleşmelerden hangisi tam iki tarafa borç yükleyen bir sözleşme değildir?',
        {
            'A': 'Eser sözleşmesi',
            'B': 'Bağışlama sözleşmesi',
            'C': 'Hizmet sözleşmesi',
            'D': 'Taşınmaz satış sözleşmesi',
            'E': 'Kira sözleşmesi',
        },
        'B',
        'Satış, kira, eser ve hizmet sözleşmelerinde tarafların edimleri **karşılıklıdır**. Bağışlamada (TBK m. 285) kural olarak yalnız bağışlayan edim yükü altına girer; sözleşme **tek tarafa borç yükler**.',
        '6098 sayılı TBK m. 207, 285',
    ),
    # düzey 3
    '0046': patch(
        "A, bir konser organizatörü olan B'ye, ünlü şarkıcı C'nin konsere çıkacağını üstlenmiştir. C ile B arasında bir sözleşme yoktur ve C konsere çıkmamıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A, C'yi konsere çıkmaya zorlamakla yükümlüdür",
            'B': "C, A'nın üstlenmesi nedeniyle B'ye karşı sorumludur",
            'C': "A'nın sorumluluğu C'nin kusuruna bağlıdır",
            'D': "A, C'nin çıkmamasından doğan B'nin zararını gidermelidir",
            'E': 'Üstlenmenin konusu başkasının fiili olduğundan sözleşme geçersizdir',
        },
        'D',
        "TBK m. 128/1'e göre **üçüncü bir kişinin fiilini başkasına karşı üstlenen, bu fiilin gerçekleşmemesinden doğan zararı gidermekle yükümlüdür**. C sözleşmenin tarafı olmadığından B'ye karşı borç altına girmez.",
        '6098 sayılı TBK m. 128',
    ),
    # düzey 2
    '0047': patch(
        "A, çiçekçi B'den arkadaşı C'nin evine çiçek gönderilmesini sipariş etmiştir. C'nin ifayı isteme hakkı kararlaştırılmamış; tarafların amacı ve örf de bunu gerektirmemektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Edimin C'ye ifasını A isteyebilir",
            'B': 'A, çiçeklerin kendisine teslimini isteyebilir',
            'C': 'C, edimin kendisine ifasını dava edebilir',
            'D': "Sözleşme C'nin onayıyla kurulmuş olur",
            'E': "Çiçekçi ancak C'nin rızasıyla ifa edebilir",
        },
        'A',
        "TBK m. 129/1'e göre **kendi adına sözleşme yapan kişi, sözleşmeye üçüncü kişi yararına bir edim yükümlülüğü koydurmuşsa, edimin üçüncü kişiye ifa edilmesini isteyebilir**. Üçüncü kişinin bağımsız istem hakkı ancak tarafların amacı veya örf ve âdet uygun düşerse doğar (eksik üçüncü kişi yararına sözleşme).",
        '6098 sayılı TBK m. 129/1',
    ),
    # düzey 3
    '0048': patch(
        "A ile B arasındaki sözleşmede alacağın devredilemeyeceği kararlaştırılmış; ancak B'nin verdiği yazılı borç tanıma belgesinde bu yasağa yer verilmemiştir. C, bu belgeye güvenerek alacağı A'dan devralmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Yasak belgede yer alsaydı C'ye karşı ileri sürülebilirdi",
            'B': 'Devir yasağı yazılı borç tanımasında yer almamıştır',
            'C': 'C, borç tanımasına güvenerek alacağı devralmıştır',
            'D': 'Alacak kural olarak borçlunun rızası aranmadan devredilebilir',
            'E': "B, devir yasağını C'ye karşı ileri sürebilir",
        },
        'E',
        "TBK m. 183/2'ye göre **borçlu, devir yasağı içermeyen yazılı bir borç tanımasına güvenerek alacağı devralmış olan üçüncü kişiye karşı, alacağın devredilemeyeceğinin kararlaştırılmış bulunduğu savunmasını ileri süremez**.",
        '6098 sayılı TBK m. 183/2',
    ),
    # düzey 2
    '0049': patch(
        "Bir alacak, mahkeme kararı gereğince A'dan C'ye geçmiştir. Bu devir hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A'nın açık rızası aranır",
            'B': 'Şekle ve önceki alacaklının rızasına bağlı olmadan ileri sürülebilir',
            'C': 'Yazılı şekilde yapılmadıkça devir üçüncü kişilere karşı ileri sürülemez',
            'D': 'Ancak ticaret siciline tescil edilirse ileri sürülebilir',
            'E': 'Borçlunun onayı olmadıkça hüküm doğurmaz',
        },
        'B',
        "TBK m. 185'e göre alacağın devri **kanun veya mahkeme kararı gereğince** gerçekleşmişse, bu devir **özel bir şekle ve önceki alacaklının rızasını açıklamasına gerek olmaksızın** üçüncü kişilere karşı ileri sürülebilir.",
        '6098 sayılı TBK m. 185',
    ),
    # düzey 3
    '0050': patch(
        "Kime ait olduğu mahkemede çekişmeli olan bir alacağın borçlusu B, çekişmeyi bildiği hâlde borcu A'ya ödemiştir. Dava henüz sonuçlanmamıştır ve borç muacceldir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'B, edimi hâkimin belirleyeceği yere tevdi edebilirdi',
            'B': 'B, bu ödemenin doğuracağı sonuçlardan sorumludur',
            'C': "B, A'ya ödeyerek sorumluluktan kurtulur",
            'D': "Taraflardan her biri B'yi tevdie zorlayabilirdi",
            'E': 'B, ifadan kaçınabilirdi',
        },
        'C',
        "TBK m. 187/2'ye göre **borçlu, alacağın çekişmeli olduğunu bildiği hâlde ifada bulunursa, bundan doğacak sonuçlardan sorumlu olur**. Borçlu ifadan kaçınıp tevdi edebilir; borç muaccelse taraflar tevdi isteyebilir.",
        '6098 sayılı TBK m. 187',
    ),
    # düzey 3
    '0051': patch(
        "B, A'ya 100.000 ₺ borçludur ve bu borcun vadesi 1 Mart'tır. A bu alacağını C'ye devretmiş, B de devri 1 Ocak'ta öğrenmiştir. B'nin A'dan 40.000 ₺ alacağı vardır ve vadesi 15 Şubat'tır. C, 1 Mart'ta ödeme istediğinde B'nin ödemesi gereken tutar en az kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '60.000',
            'C': '40.000',
            'D': '50.000',
            'E': '140.000',
        },
        'B',
        "TBK m. 188/2'ye göre borçlu, devri öğrendiği anda muaccel olmayan alacağını, **devredilen alacaktan önce veya onunla aynı anda muaccel olması koşuluyla** takas edebilir. B'nin alacağı 15 Şubat'ta, yani devredilen alacaktan önce muaccel olduğundan takas mümkündür: 100.000 − 40.000 = **60.000 ₺**.",
        '6098 sayılı TBK m. 188/2',
    ),
    # düzey 2
    '0052': patch(
        "A, B'den olan alacağını C'ye devretmiştir. A'nın devirden sonra C'ye karşı yükümlülükleri hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Alacak senedini ve ispata yarayan belgeleri C'ye teslim etmelidir",
            'B': "Devirden sonra C'ye bilgi vermekle yükümlü değildir",
            'C': "Belgeleri borçlu B'ye iade etmelidir",
            'D': 'Alacağı C adına bizzat tahsil etmelidir',
            'E': "B'nin borcuna kefil olmalıdır",
        },
        'A',
        "TBK m. 190'a göre **devreden, devralana alacak senedi ile elinde bulunan ispatla ilgili diğer belgeleri teslim etmek ve alacağını ileri sürebilmesi için gerekli bilgileri vermekle** yükümlüdür.",
        '6098 sayılı TBK m. 190',
    ),
    # düzey 3
    '0053': patch(
        "A, C'ye olan 100.000 ₺'lik borcunu ifa etmek amacıyla B'den olan 120.000 ₺'lik alacağını C'ye devretmiş; borca mahsup edilecek miktar belirlenmemiştir. C, gerekli özeni göstermeyerek B'den 70.000 ₺ tahsil etmiştir; gerekli özeni gösterseydi 90.000 ₺ tahsil edebilecekti. A'nın C'ye kalan borcu kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '0',
            'C': '50.000',
            'D': '10.000',
            'E': '30.000',
        },
        'D',
        "TBK m. 192'ye göre ifaya yönelik devirde mahsup edilecek miktar belirlenmemişse devralan, **borçludan aldığı veya gereken özeni gösterseydi alabilecek olduğu miktarı** kendi alacağına mahsup etmek zorundadır: 100.000 − 90.000 = **10.000 ₺**.",
        '6098 sayılı TBK m. 192',
    ),
    # düzey 2
    '0054': patch(
        "B, A'ya olan borcunu ödemesi için C ile anlaşmış; C de B'yi borçtan kurtarmayı üstlenmiştir. A bu anlaşmadan habersizdir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "B, A'ya karşı borçtan kurtulmuştur",
            'B': "A, borcu doğrudan C'den isteyebilir",
            'C': "Bu iç üstlenmedir; C, B'yi borçtan kurtarmakla yükümlüdür",
            'D': "Anlaşma alacaklı A'nın onayı olmadıkça kesin hükümsüz sayılır",
            'E': "C, A'ya karşı B ile müteselsilen sorumlu olur",
        },
        'C',
        "TBK m. 195/1'e göre borçlu ile **iç üstlenme sözleşmesi** yapan kişi, borcu bizzat ifa ederek veya alacaklının rızasıyla borcu üstlenerek **borçluyu borcundan kurtarma yükümlülüğü** altına girer. Alacaklıya karşı borçlu değişmez.",
        '6098 sayılı TBK m. 195',
    ),
    # düzey 3
    '0055': patch(
        "C, B'nin borcunu üstlenme önerisini alacaklı A'ya yapmış ve kabul için 30 günlük süre koymuştur. A, süre boyunca susmuştur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "B, A'ya karşı borçlu olmaya devam eder",
            'B': 'Öneri reddedilmiş sayılır',
            'C': 'Süre konmasaydı öneri daha sonra da kabul edilebilirdi',
            'D': 'Süreyi önceki borçlu da koyabilirdi',
            'E': "A'nın susması öneriyi kabul ettiği anlamına gelir",
        },
        'E',
        "TBK m. 197/1'e göre borcun üstlenilmesine ilişkin öneri alacaklı tarafından her zaman kabul edilebilir; ancak üstlenen veya önceki borçlu kabul için süre koyabilir. **Alacaklı bu sürenin bitimine kadar susarsa öneri reddedilmiş sayılır**.",
        '6098 sayılı TBK m. 197/1',
    ),
    # düzey 2
    '0056': patch(
        "C, B'nin A'ya olan satış bedeli borcunu dış üstlenmeyle üstlenmiştir; üstlenme sözleşmesinde savunmalara ilişkin bir hüküm yoktur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "C, iç üstlenmeden doğan savunmaları A'ya ileri sürebilir",
            'B': "Üstlenilen borca ilişkin savunma hakkı C'ye geçer",
            'C': 'C, borcun zamanaşımını ileri sürebilir',
            'D': "B'nin A'dan alacağıyla takası C ileri süremez",
            'E': "Aksi anlaşılmadıkça C, B'nin A'ya karşı kişisel savunmalarını kullanamaz",
        },
        'A',
        "TBK m. 199'a göre **üstlenilen borca ilişkin savunmaları ileri sürme hakkı yeni borçluya geçer**; aksi anlaşılmadıkça yeni borçlu önceki borçlunun **kişisel savunmalarında** bulunamaz ve **iç üstlenme sözleşmesinden kaynaklanan savunmaları** alacaklıya karşı ileri süremez.",
        '6098 sayılı TBK m. 199',
    ),
    # düzey 3
    '0057': patch(
        "A, ticari işletmesini aktif ve pasifleriyle B'ye devretmiş; devir 1 Mart 2025'te Ticaret Sicili Gazetesinde ilan edilmiştir. İşletmenin C'ye olan borcu ilan tarihinde muacceldir. A, bu borçtan en geç hangi tarihe kadar B ile birlikte müteselsilen sorumlu kalır?",
        {
            'A': '1 Eylül 2025',
            'B': '1 Mart 2030',
            'C': 'Borç ödeninceye kadar',
            'D': '1 Mart 2027',
            'E': '1 Mart 2026',
        },
        'D',
        "TBK m. 202'ye göre işletmeyi devralan, ilan tarihinden başlayarak borçlardan sorumlu olur; **önceki borçlu da iki yıl süreyle devralanla birlikte müteselsil borçlu olarak** sorumlu kalır. Süre muaccel borçlar için **duyuru tarihinden** işler: 1 Mart 2025 + 2 yıl = **1 Mart 2027**.",
        '6098 sayılı TBK m. 202',
    ),
    # düzey 3
    '0058': patch(
        'Aşağıdakilerden hangileri borcun üstlenilmesine ve borca katılmaya ilişkin olarak doğrudur?\n\nI. Borca katılan kişi, borçlunun yerine geçerek onu borçtan kurtarır\n\nII. Dış üstlenmede alacaklının kabulü örtülü olarak da yapılabilir\n\nIII. Kefilin sorumluluğu, üstlenmeye yazılı rıza göstermese de devam eder',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'B',
        "TBK m. 196/3'e göre alacaklının kabulü açık veya örtülü olabilir (II). m. 201'e göre borca katılan borçlunun **yanında** yer alır ve onunla müteselsilen sorumlu olur (I yanlış); m. 198/2'ye göre kefilin sorumluluğu ancak **yazılı rızasıyla** devam eder (III yanlış).",
        '6098 sayılı TBK m. 196, 198, 201',
    ),
    # düzey 2
    '0059': patch(
        "C, A ile B arasındaki kira sözleşmesine, kiracı A'nın yanında yer almak üzere taraflarla yaptığı anlaşmayla katılmıştır; aksi kararlaştırılmamıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A sözleşmeden çıkar, yerine C geçer',
            'B': 'C, kiranın yarısından sorumlu olur',
            'C': 'C, sözleşmeden doğan haklara sahip olmaz, borçlara katılır',
            'D': 'C, A ödemezse kefil gibi sorumlu olur',
            'E': "A ve C, B'ye karşı müteselsilen alacaklı ve borçludur",
        },
        'E',
        "TBK m. 206'ya göre sözleşmeye katılan, yanında yer aldığı tarafla birlikte onun hak ve borçlarına sahip olur; anlaşmada aksi kararlaştırılmamışsa **katılan ile yanında yer aldığı taraf, diğer tarafa karşı müteselsilen alacaklı ve borçlu** olurlar.",
        '6098 sayılı TBK m. 206',
    ),
    # düzey 2
    '0060': patch(
        'Aşağıdaki eşleştirmelerden hangisi yanlıştır?',
        {
            'A': 'Borca katılma – katılan ile borçlu müteselsilen sorumludur',
            'B': 'Sözleşmeye katılma – katılan, tarafın yerine geçer',
            'C': 'Alacağın devri – borçlunun rızası aranmaz',
            'D': 'Sözleşmenin devri – taraf sıfatı devralana geçer',
            'E': 'Dış üstlenme – alacaklı ile üstlenen arasında yapılır',
        },
        'B',
        "TBK m. 206'ya göre sözleşmeye katılan, taraflardan birinin **yanında** yer alır ve onunla birlikte hak ve borçlara sahip olur; onun yerine geçmez. Taraf değişikliği sözleşmenin devrinde (m. 205) gerçekleşir.",
        '6098 sayılı TBK m. 183, 196, 201, 205, 206',
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
    print(f"1 paket / {len(PATCHES)} soru ('Borc Iliskisi ve Kaynaklari' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
