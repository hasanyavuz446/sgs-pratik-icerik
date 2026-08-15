#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kambiyo Senetleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

    olcut                gercek   once   sonra
    medyan kok              257     78     122
    olumsuz kok           %41,5     %0     %38
    kor ogrenci               —    %23       —
    boy egilimi               —   9/22       —   (TERS tuzak: dogru sik KISAYDI)

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TTK md. 670-823 · police md. 671-749 · bono md. 776-779 · cek md. 780-823 · aval md. 700-702 · zamanasimi md. 749, 814 · sebepsiz zenginlesme md. 732.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/kambiyo_senetleri.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "kmb-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": '6102 sayili Turk Ticaret Kanunu'},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "Bir senette 'poliçe' kelimesi yer almakta ancak vade kaydı bulunmamaktadır. Başka bir senette ise 'bono' kelimesi bulunmamakta, yalnızca ödeme vaadi yazmaktadır. Buna göre kambiyo senetlerinde şekle bağlılık ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Her iki senet de geçersizdir ve hiçbir sonuç doğurmaz',
            'B': 'Her iki senet de geçerli kambiyo senedi sayılır',
            'C': 'Eksik unsurlar hamil tarafından her zaman serbestçe tamamlanabilir',
            'D': "Vadesi yazılmayan poliçe görüldüğünde ödenecek sayılır; 'bono' kelimesini taşımayan senet ise bono sayılmaz",
            'E': "Vadesi gösterilmeyen poliçe geçersiz sayılır; 'bono' kelimesindeki eksiklik ise kanunen tamamlanabilir",
        },
        'D',
        "TTK md. 671-672: poliçede vade zorunlu unsurdur; ancak vade gösterilmemişse senet GÖRÜLDÜĞÜNDE ödenecek poliçe sayılır (kanuni tamamlama). md. 776-777: bonoda 'BONO' veya 'emre muharrer senet' kelimesi kanunen tamamlanamayan zorunlu unsurdur; yokluğu senedi bono olmaktan çıkarır.",
    ),
    # düzey 3
    '0002': patch(
        'Bir kambiyo senedinde üç imza bulunmaktadır: birincisi ehliyetsiz bir kişiye, ikincisi sahte bir imzaya, üçüncüsü ise geçerli bir imzaya aittir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ehliyetsizlik hâlinde tüm imza sahipleri sorumluluktan kurtulur',
            'B': 'Sahte imza bulunması hâlinde senet hükümsüz olur',
            'C': 'Bir imzanın geçersizliği senedin tamamını geçersiz kılar',
            'D': 'Geçersiz imzalar diğerlerinin geçerliliğini etkilemez; geçerli imza sahibi sorumlu kalır',
            'E': 'Geçerli imza sahibi, ancak senetteki bütün diğer imzalar da geçerli olduğu takdirde sorumlu olur',
        },
        'D',
        'TTK md. 677 (imzaların bağımsızlığı): kambiyo senedi, borç altına girme ehliyeti bulunmayan kişilerin imzasını, sahte imzaları, hayali kişilerin imzalarını veya imzalayanı bağlamayan imzaları taşırsa, DİĞER İMZALARIN GEÇERLİLİĞİ bundan etkilenmez.',
    ),
    # düzey 3
    '0003': patch(
        'Bir bono, mal alım satımından doğan bir borç için düzenlenmiştir. Satış sözleşmesi sonradan geçersiz sayılmış; senedi ciro yoluyla devralan iyiniyetli hamil ödeme talep etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Temel ilişkinin geçersizliği senedi de geçersiz kılar',
            'B': "Kambiyo senedi temel ilişkiden bağımsızdır; borçlu temel ilişkiye dayanan def'iyi iyiniyetli hamile karşı ileri süremez",
            'C': 'Hamil ancak temel ilişki geçerliyse ödeme talep edebilir',
            'D': "Borçlu, temel ilişkiye dayanan def'iyi hamilin iyiniyetli olup olmadığına bakılmaksızın herkese karşı ileri sürebilir",
            'E': 'Mücerretlik yalnızca poliçe için geçerlidir',
        },
        'B',
        "Kambiyo senetleri MÜCERRET (soyut) senetlerdir; senetteki borç temel ilişkiden bağımsızdır. TTK md. 687: borçlu, temel ilişkiye dayanan kişisel def'ileri, hamil senedi devralırken bilerek borçlunun zararına hareket etmiş olmadıkça ileri süremez.",
    ),
    # düzey 2
    '0004': patch(
        "Bir bononun üzerine 'emre yazılı değildir' kaydı düşülmüştür. Buna göre senedin devri bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Senet hamiline yazılı hâle gelir ve bundan sonra yalnızca zilyetliğin devriyle devredilir',
            'B': 'Senet devredilemez hâle gelir',
            'C': 'Senet yine ciro ile devredilir; kayıt sonuç doğurmaz',
            'D': 'Kayıt senedi geçersiz kılar',
            'E': 'Senet nama yazılı hâle gelir ve alacağın temliki hükümlerine göre devredilir',
        },
        'E',
        "TTK md. 681: kambiyo senetleri KANUNEN EMRE YAZILIDIR; ciro ile devredilir. Ancak senede 'EMRE YAZILI DEĞİLDİR' ya da buna eş bir kayıt konulmuşsa senet nama yazılı hâle gelir ve ALACAĞIN TEMLİKİ hükümlerine göre devredilir.",
    ),
    # düzey 3
    '0005': patch(
        'Bir bonoyu düzenleyen, iki ciranta ve bir aval veren bulunmaktadır. Hamil vadede ödeme alamamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk imza sırasına göre tek tek işler',
            'B': 'Aval verenin sorumluluğu yalnızca düzenleyen ödeme yapmazsa doğar',
            'C': 'Cirantalar hamile karşı sorumlu değildir',
            'D': 'Düzenleyen, cirantalar ve aval veren hamile karşı müteselsilen sorumludur; hamil dilediğine başvurabilir',
            'E': 'Hamil önce düzenleyene başvurur; ondan sonuç alamadığı takdirde cirantalara yönelebilir',
        },
        'D',
        'TTK md. 724: bir poliçeyi düzenleyen, kabul eden, ciro eden veya aval veren kişiler hamile karşı MÜTESELSİLEN borçludur. Hamil bunlardan birine, birkaçına veya hepsine, borç altına girişlerindeki sıraya bağlı kalmaksızın başvurabilir.',
    ),
    # düzey 3
    '0006': patch(
        'Üç senet incelenmektedir: (A) düzenleyen, muhatap ve lehtar olmak üzere üç taraflı ve muhataba havale içeren senet; (B) düzenleyenin bizzat ödeme vaadi içeren iki taraflı senet; (C) muhatabı banka olan ve görüldüğünde ödenen senet. Buna göre bu senetler sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': 'Poliçe – bono – çek',
            'B': 'Bono – poliçe – çek',
            'C': 'Çek – bono – poliçe',
            'D': 'Poliçe – çek – bono',
            'E': 'Bono – çek – poliçe',
        },
        'A',
        "TTK md. 671: POLİÇE üç taraflıdır (düzenleyen, muhatap, lehtar) ve muhataba yönelik kayıtsız şartsız havale içerir. md. 776: BONO iki taraflıdır ve düzenleyenin bizzat ÖDEME VAADİNİ içerir; muhatap yoktur. md. 780 ve 782: ÇEK'te muhatap ancak BANKA olabilir ve çek görüldüğünde ödenir.",
    ),
    # düzey 3
    '0007': patch(
        'Bir çekin üzerine ileri bir tarih vade olarak yazılmış; ayrıca muhatap bankaya kabul için ibraz edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çekte vade bulunmaz; çek görüldüğünde ödenir ve kabul yasaktır, kabul şerhi yazılmamış sayılır',
            'B': 'Vade yazılması çeki geçersiz kılar',
            'C': 'Kabul için ibraz çeki bonoya dönüştürür',
            'D': 'Çekteki vade geçerlidir; çek vade tarihinde ödenir',
            'E': 'Çekte kabul mümkün olup kabul şerhiyle birlikte muhatap banka çekin asıl borçlusu hâline gelir',
        },
        'A',
        'TTK md. 795: çek GÖRÜLDÜĞÜNDE ödenir; buna aykırı herhangi bir kayıt yazılmamış hükmündedir. md. 784: çekte KABUL YASAKTIR; çek üzerine yazılan kabul şerhi yazılmamış sayılır. Muhatap banka kabul yoluyla asıl borçlu hâline gelmez.',
    ),
    # düzey 2
    '0008': patch(
        "Türk Ticaret Kanunu'na göre kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Poliçe, bono ve çek kambiyo senetleridir. II. Kambiyo senetleri kanunen emre yazılıdır. III. Konşimento da bir kambiyo senedidir.",
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'C',
        'I doğrudur (TTK md. 670 vd.). II doğrudur (md. 681, 824). III YANLIŞTIR: konşimento bir emtia senedidir; kambiyo senedi değildir.',
    ),
    # düzey 3
    '0009': patch(
        'Bir bonoyu düzenleyen kişi, sorumluluğunun poliçeyi kabul eden muhataptan daha hafif olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bono düzenleyeni yalnızca lehtara karşı sorumludur',
            'B': 'Bono düzenleyeninin sorumluluğu, senedi ciro eden kişilerin sorumluluğuyla aynıdır',
            'C': 'Bono düzenleyeni yalnızca ikinci derecede sorumludur',
            'D': 'Bono düzenleyeni protesto çekilmedikçe sorumlu olmaz',
            'E': 'Bono düzenleyeni, poliçeyi kabul eden muhatap gibi sorumludur',
        },
        'E',
        'TTK md. 778/3: bononun düzenleyeni, POLİÇEYİ KABUL EDEN MUHATAP GİBİ sorumludur. Yani asıl borçludur; sorumluluğu için protesto çekilmesi gerekmez ve tüm hamillere karşı devam eder.',
    ),
    # düzey 3
    '0010': patch(
        'Bir poliçe muhataba ibraz edilmiş ve muhatap poliçeyi kabul etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kabul edilen poliçede protesto çekilmesi gerekmez',
            'B': 'Kabul eden muhatap poliçenin asıl borçlusu hâline gelir',
            'C': 'Kabulle düzenleyenin sorumluluğu sona erer',
            'D': 'Kabul yalnızca muhatabın ödeme niyetini gösterir; borç doğurmaz',
            'E': 'Kabul eden muhatap ikinci derecede sorumlu olur',
        },
        'B',
        'TTK md. 691: muhatap kabul ile poliçe bedelini vadesinde ödemek yükümlülüğü altına girer; poliçenin ASIL BORÇLUSU olur. Düzenleyenin sorumluluğu sona ermez; kabul etmeme ya da ödememe hâlinde müracaat hakkı için protesto gerekir.',
    ),
    # düzey 3
    '0011': patch(
        'Bir poliçede ödeme yeri ve düzenlenme yeri gösterilmemiştir; muhatabın adı yanında bir yer, düzenleyenin adı yanında da başka bir yer yazılıdır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her iki eksiklik de poliçeyi geçersiz kılar',
            'B': 'Ödeme yeri eksikliği poliçeyi geçersiz kılar; düzenlenme yeri eksikliği ise kanun gereği tamamlanabilir',
            'C': 'Her iki yer de hamil tarafından serbestçe doldurulur',
            'D': 'Eksik yerler muhatabın beyanına göre belirlenir',
            'E': 'Muhatabın adı yanındaki yer ödeme yeri, düzenleyenin adı yanındaki yer düzenlenme yeri sayılır',
        },
        'E',
        'TTK md. 672: ödeme yeri gösterilmeyen poliçede muhatabın adı yanında yazılı yer ödeme yeri ve aynı zamanda muhatabın yerleşim yeri sayılır. Düzenlenme yeri gösterilmeyen poliçe, düzenleyenin adı yanında yazılı yerde düzenlenmiş sayılır.',
    ),
    # düzey 2
    '0012': patch(
        'Bir senedin bono sayılabilmesi için taşıması gereken unsurlar belirlenmektedir. Buna göre aşağıdakilerden hangisi bononun zorunlu unsurlarından biri değildir?',
        {
            'A': 'Muhatabın adı ve soyadı ile ticaret unvanı',
            'B': "Senet metninde 'bono' veya 'emre muharrer senet' kelimesi",
            'C': 'Kayıtsız ve şartsız belirli bir bedeli ödemek vaadi',
            'D': 'Lehtarın adı ve soyadı ile ticaret unvanı',
            'E': 'Düzenlenme tarihi ile düzenleyenin imzası',
        },
        'A',
        "TTK md. 776: bononun zorunlu unsurları 'bono' veya 'emre muharrer senet' kelimesi, kayıtsız şartsız ödeme vaadi, vade, ödeme yeri, lehtar, düzenlenme tarihi ve yeri ile düzenleyenin imzasıdır. Bonoda MUHATAP YOKTUR; muhatap poliçe ve çeke özgüdür.",
    ),
    # düzey 2
    '0013': patch(
        'Bir senedin çek sayılabilmesi için taşıması gereken unsurlar belirlenmektedir. Buna göre aşağıdakilerden hangisi çekin zorunlu unsurlarından biri değildir?',
        {
            'A': 'Düzenlenme tarihi ve yeri ile düzenleyenin imzası',
            'B': 'Kayıtsız ve şartsız belirli bir bedelin ödenmesi için havale',
            'C': 'Senedin vadesini gösteren kayıt',
            'D': 'Muhatap bankanın ticaret unvanı',
            'E': "Senet metninde 'çek' kelimesi",
        },
        'C',
        "TTK md. 780: çekin zorunlu unsurları arasında VADE YOKTUR; md. 795 uyarınca çek görüldüğünde ödenir ve aksine kayıtlar yazılmamış sayılır. Muhatabın BANKA olması ise md. 782'nin gereğidir.",
    ),
    # düzey 3
    '0014': patch(
        "Bir poliçede vade olarak 'düzenlenme gününden üç ay sonra' yazılmıştır. Bir diğerinde 'görüldükten on gün sonra' kaydı bulunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Düzenlenme gününden belirli süre sonra vadesi geçersizdir',
            'B': 'Görüldükten belirli süre sonra vadesi kanunda öngörülmemiştir',
            'C': 'Her iki vade türü de kanunda öngörülmüştür ve geçerlidir',
            'D': 'Poliçede yalnızca görüldüğünde ödeme mümkündür',
            'E': 'Yalnızca belirli bir günde ödeme vadesi geçerlidir',
        },
        'C',
        'TTK md. 703: poliçe görüldüğünde, görüldükten belirli bir süre sonra, düzenlenme gününden belirli bir süre sonra ya da belirli bir günde ödenmek üzere düzenlenebilir. Bunlardan başka vadeleri gösteren veya birbirini izleyen vadeleri içeren poliçeler geçersizdir.',
    ),
    # düzey 3
    '0015': patch(
        'Bir çek, düzenlendiği yerde ödenecek biçimde düzenlenmiştir. Hamil çeki düzenlenme tarihinden 20 gün sonra bankaya ibraz etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İbraz süresi bir ay olduğundan ibraz süresindedir',
            'B': 'Süre geçse de müracaat hakkı devam eder',
            'C': 'Çekte ibraz süresi yalnızca yurt dışında düzenlenip yurt içinde ödenecek çekler bakımından geçerlidir',
            'D': 'Çekte ibraz süresi öngörülmemiştir',
            'E': 'Düzenlendiği yerde ödenecek çek on gün içinde ibraz edilmelidir; süre geçtiğinden müracaat hakkı düşer',
        },
        'E',
        'TTK md. 796: bir çek düzenlendiği yerde ödenecekse ON GÜN, düzenlendiği yerden başka bir yerde ödenecekse BİR AY içinde muhataba ibraz edilmelidir. Süresinde ibraz edilmeyen çekte hamilin cirantalara ve düzenleyene karşı MÜRACAAT HAKKI düşer (md. 808).',
    ),
    # düzey 3
    '0016': patch(
        'Bir bonoya aval veren kişi, lehine aval verdiği cirantanın imzasının sahte olduğunu öğrenmiş ve kendi taahhüdünün de geçersiz olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Lehine aval verilen kişinin borcu herhangi bir sebeple geçersiz sayılırsa aval taahhüdü de kendiliğinden geçersiz olur',
            'B': 'Aval verenin sorumluluğu lehine aval verilenden daha hafiftir',
            'C': 'Aval verenin taahhüdü, şekle ilişkin noksanlık dışında lehine aval verilenin borcu geçersiz olsa da geçerlidir',
            'D': 'Aval veren yalnızca lehtara karşı sorumlu olur',
            'E': 'Aval yalnızca poliçede mümkündür',
        },
        'C',
        'TTK md. 702: aval veren kişi, kimin için taahhüt altına girmişse tam olarak onun GİBİ sorumlu olur. Aval verenin taahhüdü, lehine taahhüt altına girdiği kişinin borcu ŞEKLE İLİŞKİN noksanlık dışında herhangi bir sebeple geçersiz olsa da GEÇERLİDİR.',
    ),
    # düzey 3
    '0017': patch(
        "Bir hamil, vadesinde ödenmeyen bonoyu protesto ettirmeden doğrudan cirantalara başvurmuştur. Senette 'protestosuz' kaydı bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Protesto yalnızca poliçede gereklidir',
            'B': 'Protesto çekilmesi gerekmez; hamil müracaat hakkını doğrudan bütün cirantalara karşı kullanabilir',
            'C': 'Protesto eksikliği düzenleyene başvuruyu da engeller',
            'D': 'Cirantalara başvurabilmek için ödememe protestosu çekilmesi gerekir; protestosuz başvuru hakkı düşürür',
            'E': "Protesto yalnızca 'protestosuz' kaydı varsa gerekir",
        },
        'D',
        "TTK md. 714 ve 725: kabul etmeme veya ödememe, PROTESTO adı verilen resmî bir belgeyle belirlenir; hamilin cirantalara, düzenleyene ve diğer borçlulara müracaat hakkı protestonun çekilmesine bağlıdır. 'PROTESTOSUZ' kaydı bu külfeti kaldırır. Bono düzenleyeni asıl borçlu olduğundan ona başvuru için protesto gerekmez.",
    ),
    # düzey 2
    '0018': patch(
        "Bir kambiyo senedinin arkasına 'bedeli teminattır' kaydıyla ciro yapılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Beyaz cirodur; lehtar gösterilmemiştir',
            'B': 'Temlik cirosudur; mülkiyet ciro edilene geçer',
            'C': 'Rehin cirosudur; hamil senetten doğan hakları kullanır ancak mülkiyeti kazanmaz',
            'D': 'Tahsil cirosudur; hamile senedin mülkiyeti geçmeksizin yalnızca tahsil yetkisi verilir',
            'E': 'Kayıt geçersiz olup ciro temlik cirosu sayılır',
        },
        'C',
        "TTK md. 689: 'bedeli teminattır', 'bedeli rehindir' veya rehni ifade eden diğer kayıtları taşıyan ciro REHİN CİROSUDUR. Hamil poliçeden doğan bütün hakları kullanabilir; ancak mülkiyeti kazanmadığından yaptığı ciro tahsil cirosu hükmündedir.",
    ),
    # düzey 3
    '0019': patch(
        'Bir hamil, kambiyo senedinden doğan hakkını zamanaşımı nedeniyle kaybetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zamanaşımı sonrası hiçbir talep hakkı kalmaz',
            'B': 'Zamanaşımı kambiyo senetlerinde işlemez',
            'C': 'Hamil, zarara uğradığı ölçüde düzenleyen ve kabul edene karşı sebepsiz zenginleşme davası açabilir',
            'D': 'Hamil yalnızca cirantalara başvurabilir',
            'E': 'Hamil, kambiyo hakkıyla birlikte temel ilişkiye dayanan bütün talep haklarını da tümüyle kaybeder',
        },
        'C',
        'TTK md. 732: zamanaşımı veya kambiyo hukukuna özgü işlemlerin yapılmasına gerekli sürelerin geçmesi nedeniyle poliçeden doğan haklar düşmüş olsa bile, düzenleyen ve KABUL EDEN, hamilin zararına SEBEPSİZ ZENGİNLEŞTİKLERİ ölçüde borçlu kalır.',
    ),
    # düzey 3
    '0020': patch(
        "Bir bonoda vade 1 Haziran'dır. Hamil, kabul eden konumundaki düzenleyene karşı hakkını ne kadar süreyle ileri sürebileceğini araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kabul edene karşı talepler on yıllık zamanaşımına tabidir',
            'B': 'Kabul edene karşı talepler vadeden itibaren üç yıllık zamanaşımına tabidir',
            'C': 'Poliçeyi kabul edene karşı ileri sürülecek talepler vadeden itibaren bir yıllık zamanaşımına tabidir',
            'D': 'Kabul edene karşı talepler altı aylık zamanaşımına tabidir',
            'E': 'Kambiyo senetlerinde zamanaşımı işlemez',
        },
        'B',
        'TTK md. 749: poliçeyi kabul edene karşı ileri sürülecek talepler VADEDEN itibaren ÜÇ YIL geçmekle zamanaşımına uğrar. Hamilin cirantalarla düzenleyene karşı talepleri protesto tarihinden itibaren bir yıl, cirantaların birbirlerine ve düzenleyene karşı talepleri ise altı ay içinde zamanaşımına uğrar.',
    ),
    # düzey 2
    '0021': patch(
        'Bir tacir, elindeki poliçe, bono ve çeki ortak özellikleri bakımından karşılaştırmaktadır. Buna göre kambiyo senetleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kambiyo senetlerinde imzaların bağımsızlığı ilkesi kanun tarafından benimsenmiştir',
            'B': 'Kambiyo senetleri poliçe, bono ve çektir',
            'C': 'Kambiyo senetleri mücerret (soyut) senetlerdir',
            'D': 'Kambiyo senetleri şekle sıkı biçimde bağlıdır',
            'E': 'Kambiyo senetleri kanunen nama yazılı olup alacağın temliki ile devredilir',
        },
        'E',
        "TTK md. 681 ve 824: kambiyo senetleri KANUNEN EMRE YAZILIDIR ve ciro ile devredilir; nama yazılı hâle gelmeleri ancak 'emre yazılı değildir' kaydıyla mümkündür.",
    ),
    # düzey 2
    '0022': patch(
        'Bir senette üç imzadan biri ehliyetsiz bir kişiye aittir. Buna göre imzaların bağımsızlığı ilkesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Geçersiz imza diğer imzaların geçerliliğini etkilemez',
            'B': 'Sahte imza bulunması senedi hükümsüz kılmaz',
            'C': 'Bir imzanın geçersizliği senetteki tüm imzaları geçersiz kılar',
            'D': 'Hayali kişilerin imzası diğerlerini etkilemez',
            'E': 'İlke kambiyo senetlerinin tedavül güvenliğine hizmet eder',
        },
        'C',
        'TTK md. 677: kambiyo senedi borç altına girme ehliyeti bulunmayan kişilerin imzasını, sahte imzaları veya hayali kişilerin imzalarını taşırsa DİĞER İMZALARIN GEÇERLİLİĞİ bundan ETKİLENMEZ.',
    ),
    # düzey 2
    '0023': patch(
        'Bir çekin hukuki rejimi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çekte kabul yasaktır',
            'B': 'Çekte muhatap herhangi bir gerçek veya tüzel kişi olabilir',
            'C': 'Çekin muhatap bankaya ibraz süreleri kanunda ayrıca düzenlenmiştir',
            'D': 'Çek görüldüğünde ödenir',
            'E': 'Çekte muhatap ancak banka olabilir',
        },
        'B',
        'TTK md. 782: çek ancak bir BANKA üzerine düzenlenebilir; banka dışındaki kişiler üzerine düzenlenen belge çek sayılmaz. md. 795 çekin görüldüğünde ödeneceğini, md. 784 kabul yasağını, md. 796 ibraz sürelerini düzenler.',
    ),
    # düzey 2
    '0024': patch(
        'Bono ile poliçe karşılaştırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bono iki taraflıdır: düzenleyen ve lehtar',
            'B': 'Bono düzenleyeni poliçeyi kabul eden muhatap gibi sorumludur',
            'C': 'Poliçe üç taraflıdır: düzenleyen, muhatap ve lehtar',
            'D': 'Bonoda düzenleyen bizzat ödeme vaadinde bulunur',
            'E': 'Bonoda muhatap bulunur ve düzenleyen muhataba havale verir',
        },
        'E',
        'TTK md. 776: bonoda MUHATAP YOKTUR; düzenleyen bizzat ödeme vaadinde bulunur ve senet iki taraflıdır. Havale ve muhatap POLİÇEYE (md. 671) ve çeke özgüdür.',
    ),
    # düzey 2
    '0025': patch(
        'Bir poliçenin zorunlu unsurları incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vadesi gösterilmeyen poliçe zorunlu unsur eksikliği nedeniyle geçersizdir',
            'B': 'Vadesi gösterilmeyen poliçe görüldüğünde ödenecek sayılır',
            'C': 'Ödeme yeri gösterilmemişse muhatabın adı yanındaki yer esas alınır',
            'D': "Poliçe metninde 'poliçe' kelimesi bulunmalıdır",
            'E': 'Kayıtsız şartsız belirli bir bedelin ödenmesi için havale bulunmalıdır',
        },
        'A',
        'TTK md. 672: vadesi gösterilmemiş poliçe GÖRÜLDÜĞÜNDE ödenecek poliçe sayılır; bu kanuni bir tamamlamadır ve senedi geçersiz kılmaz.',
    ),
    # düzey 2
    '0026': patch(
        'Kambiyo senetlerinde sorumluluk incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hamil borçlulardan birine, birkaçına veya hepsine başvurabilir',
            'B': 'Düzenleyen, kabul eden, ciranta ve aval veren müteselsilen sorumludur',
            'C': 'Bono düzenleyeni asıl borçludur',
            'D': 'Hamil, borçlulara borç altına girişlerindeki sıraya uygun biçimde başvurur',
            'E': 'Aval veren, lehine aval verdiği kişi gibi sorumludur',
        },
        'D',
        'TTK md. 724: hamil, bu kişilerden birine, birkaçına veya hepsine, borç altına girişlerindeki SIRAYA BAĞLI KALMAKSIZIN başvurabilir.',
    ),
    # düzey 2
    '0027': patch(
        'Aval kurumu incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aval kambiyo senetlerinde mümkündür',
            'B': 'Lehine aval verilenin borcu herhangi bir sebeple geçersizse aval de geçersiz olur',
            'C': 'Aval, senet bedelinin ödenmesini güvence altına alır',
            'D': 'Aval veren kişi, kimin için taahhüt altına girmişse tam olarak onun gibi sorumlu olur',
            'E': 'Avalin taahhüdü şekle ilişkin noksanlık dışında geçerli kalır',
        },
        'B',
        'TTK md. 702: aval verenin taahhüdü, lehine taahhüt altına girdiği kişinin borcu ŞEKLE İLİŞKİN NOKSANLIK DIŞINDA herhangi bir sebeple geçersiz olsa da GEÇERLİDİR.',
    ),
    # düzey 2
    '0028': patch(
        'Kambiyo senetlerinde protesto incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bono düzenleyenine başvuru için protesto gerekmez',
            'B': 'Protesto kabul etmeme veya ödememenin resmî belgeyle tespitidir',
            'C': 'Cirantalara müracaat için kural olarak protesto gerekir',
            'D': 'Protesto, senedin geçerliliği için aranan bir şekil şartıdır',
            'E': "'Protestosuz' kaydı protesto külfetini kaldırır",
        },
        'D',
        'TTK md. 714 vd.: protesto senedin GEÇERLİLİK ŞARTI DEĞİLDİR; müracaat hakkının korunması için aranan bir işlemdir. Senedin geçerliliği zorunlu şekil unsurlarına bağlıdır.',
    ),
    # düzey 2
    '0029': patch(
        'Kambiyo senetlerinde mücerretlik ilkesi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mücerretlik senedin tedavülünü kolaylaştırır',
            'B': 'Temel ilişkinin geçersizliği kambiyo senedini de kendiliğinden geçersiz kılar',
            'C': 'Kambiyo senedindeki borç temel ilişkiden bağımsızdır',
            'D': "Bilerek borçlunun zararına hareket eden hamile karşı def'i ileri sürülebilir",
            'E': "Borçlu temel ilişkiye dayanan def'iyi iyiniyetli hamile karşı ileri süremez",
        },
        'B',
        'Kambiyo senetleri MÜCERRETTİR: senetteki borç temel ilişkiden bağımsızdır ve temel ilişkinin geçersizliği senedi kendiliğinden geçersiz KILMAZ (TTK md. 687).',
    ),
    # düzey 2
    '0030': patch(
        'Çekte ibraz süreleri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Süresinde ibraz edilmeyen çekte müracaat hakkı düşer',
            'B': 'Düzenlendiği yerde ödenecek olan çek, on gün içinde muhatap bankaya ibraz edilir',
            'C': 'Başka yerde ödenecek çek bir ay içinde ibraz edilir',
            'D': 'Çekte ibraz süresi öngörülmemiş olup çek her zaman ibraz edilebilir',
            'E': 'İbraz süreleri kanunda düzenlenmiştir',
        },
        'D',
        'TTK md. 796: çek düzenlendiği yerde ödenecekse ON GÜN, başka yerde ödenecekse BİR AY içinde muhataba ibraz edilmelidir; süreler kanunda açıkça öngörülmüştür.',
    ),
    # düzey 2
    '0031': patch(
        'Kambiyo senetlerinde zamanaşımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Zamanaşımı dolsa da sebepsiz zenginleşme davası açılabilir',
            'B': 'Cirantaların birbirlerine karşı talepleri altı ayda zamanaşımına uğrar',
            'C': 'Kabul edene karşı talepler vadeden itibaren üç yılda zamanaşımına uğrar',
            'D': 'Hamilin cirantalara karşı talepleri protesto tarihinden itibaren bir yılda zamanaşımına uğrar',
            'E': 'Kabul edene karşı talepler on yıllık genel zamanaşımına tabidir',
        },
        'E',
        'TTK md. 749: poliçeyi kabul edene karşı talepler VADEDEN itibaren ÜÇ YIL geçmekle zamanaşımına uğrar; genel on yıllık süre uygulanmaz.',
    ),
    # düzey 2
    '0032': patch(
        'Kambiyo senetlerinde ciro incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Temlik cirosu mülkiyeti devreder',
            'B': 'Beyaz ciro yalnızca cirantanın imzasıyla yapılabilir',
            'C': 'Ciro senedin arkasına veya alonj üzerine yazılır',
            'D': 'Rehin cirosu senedi teminat olarak verir',
            'E': 'Tahsil cirosuyla senedin mülkiyeti ciro edilene geçer',
        },
        'E',
        'TTK md. 688: tahsil cirosunda hamil senetten doğan hakları kullanabilir ancak MÜLKİYET GEÇMEZ; hamil yalnızca tahsil yetkisine sahiptir.',
    ),
    # düzey 2
    '0033': patch(
        'Kambiyo senetlerinin devri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nama yazılı hâle gelen senet alacağın temliki ile devredilir',
            'B': "Senede konulan 'emre yazılı değildir' kaydı, senedi nama yazılı senet hâline getirir",
            'C': "Kambiyo senedine konulan 'emre yazılı değildir' kaydı yazılmamış sayılır",
            'D': 'Kambiyo senetleri kural olarak ciro ve teslimle devredilir',
            'E': 'Kambiyo senetleri kanunen emre yazılıdır',
        },
        'C',
        "TTK md. 681: 'EMRE YAZILI DEĞİLDİR' kaydı yazılmamış sayılmaz; tam tersine senedi nama yazılı hâle getirir ve alacağın temliki hükümlerine tabi kılar.",
    ),
    # düzey 2
    '0034': patch(
        'Poliçede kabul kurumu incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kabul poliçe üzerine yazılır ve imzalanır',
            'B': 'Muhatap kabul ile poliçenin asıl borçlusu olur',
            'C': 'Çekte kabul yasaktır',
            'D': 'Kabulle birlikte düzenleyenin sorumluluğu sona erer',
            'E': 'Kabul etmeme hâlinde protesto çekilebilir',
        },
        'D',
        'TTK md. 691 ve 725: muhatap kabul ile asıl borçlu olur; ancak DÜZENLEYENİN sorumluluğu SONA ERMEZ, müracaat borçlusu olarak devam eder.',
    ),
    # düzey 2
    '0035': patch(
        'Bir hamil zamanaşımı nedeniyle kambiyo hakkını kaybetmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Talep hamilin zararıyla sınırlıdır',
            'B': 'Zamanaşımının dolmasıyla hamilin bütün talep hakları kesin olarak sona erer',
            'C': 'Temel ilişkiye dayanan talep ayrıca değerlendirilebilir',
            'D': 'Sebepsiz zenginleşme davası kanunda düzenlenmiştir',
            'E': 'Düzenleyen ile kabul eden kişi, hamilin zararına sebepsiz zenginleştikleri ölçüde borçlu kalır',
        },
        'B',
        'TTK md. 732: zamanaşımı nedeniyle poliçeden doğan haklar düşmüş olsa bile düzenleyen ve kabul eden, hamilin zararına SEBEPSİZ ZENGİNLEŞTİKLERİ ÖLÇÜDE borçlu kalır.',
    ),
    # düzey 2
    '0036': patch(
        'Poliçede vade türleri incelenmektedir. Buna göre aşağıdakilerden hangisi bir vade türü değildir?',
        {
            'A': 'Belirli bir günde ödenecek poliçe',
            'B': 'Görüldüğünde ödenecek poliçe',
            'C': 'Alacaklının talep ettiği tarihte ödenmek üzere düzenlenen poliçe',
            'D': 'Görüldükten belirli bir süre sonra ödenecek poliçe',
            'E': 'Düzenlenme gününden belirli bir süre geçtikten sonra ödenmek üzere düzenlenen poliçe',
        },
        'C',
        'TTK md. 703: poliçe görüldüğünde, görüldükten belirli süre sonra, düzenlenme gününden belirli süre sonra ya da belirli bir günde ödenmek üzere düzenlenebilir. Bunlardan BAŞKA vadeleri içeren poliçeler GEÇERSİZDİR; alacaklının takdirine bırakılan vade kanunda yoktur.',
    ),
    # düzey 0
    '0037': patch(
        'Bir tacir elindeki senetleri sınıflandırırken kambiyo senetlerini ayırmaktadır. Buna göre aşağıdakilerden hangisi bir kambiyo senedi değildir?',
        {
            'A': 'Emre yazılı olarak düzenlenmiş poliçe',
            'B': 'Konşimento',
            'C': 'Bono',
            'D': 'Çek',
            'E': 'Poliçe',
        },
        'B',
        'TTK md. 670 vd.: kambiyo senetleri POLİÇE, BONO ve ÇEKTİR. Konşimento bir emtia senedidir.',
    ),
    # düzey 0
    '0038': patch(
        'Muhatabı yalnızca banka olabilen kambiyo senedi aşağıdakilerden hangisidir?',
        {
            'A': 'Makbuz senedi',
            'B': 'Konşimento',
            'C': 'Poliçe',
            'D': 'Bono',
            'E': 'Çek',
        },
        'E',
        'TTK md. 782: çek ancak bir BANKA üzerine düzenlenebilir; poliçede muhatap herhangi bir kişi olabilir, bonoda ise muhatap yoktur.',
    ),
    # düzey 0
    '0039': patch(
        'Düzenleyenin bizzat ödeme vaadini içeren ve muhatabı bulunmayan kambiyo senedi aşağıdakilerden hangisidir?',
        {
            'A': 'Bono',
            'B': 'Varant',
            'C': 'Çek',
            'D': 'Konşimento',
            'E': 'Poliçe',
        },
        'A',
        'TTK md. 776: bono, düzenleyenin kayıtsız şartsız belirli bir bedeli ödeme vaadini içerir ve iki taraflıdır; muhatap yoktur.',
    ),
    # düzey 0
    '0040': patch(
        'Kambiyo senedi bedelinin ödenmesini güvence altına alan kambiyo hukuku kurumu aşağıdakilerden hangisidir?',
        {
            'A': 'Ciro',
            'B': 'Protesto',
            'C': 'Kabul',
            'D': 'İbraz',
            'E': 'Aval',
        },
        'E',
        'TTK md. 700: poliçede bedelin ödenmesi, aval şerhiyle tamamen veya kısmen güvence altına alınabilir; AVAL bir kambiyo taahhüdüdür.',
    ),
    # düzey 0
    '0041': patch(
        'Kabul etmeme veya ödememenin resmî bir belgeyle tespit edilmesi işlemi aşağıdakilerden hangisidir?',
        {
            'A': 'Ciro',
            'B': 'Protesto',
            'C': 'Aval',
            'D': 'Ödeme yasağı',
            'E': 'Kabul',
        },
        'B',
        'TTK md. 714: kabul etmeme veya ödememe, PROTESTO adı verilen resmî bir belgeyle belirlenir; müracaat hakkının korunması için gereklidir.',
    ),
    # düzey 0
    '0042': patch(
        'Bir kambiyo senedinin ciro ve teslimle devredilmesini sağlayan özelliği aşağıdakilerden hangisidir?',
        {
            'A': 'Mücerret olması',
            'B': 'Kanunen emre yazılı olması',
            'C': 'Nama yazılı olması',
            'D': 'Şekle bağlı olması',
            'E': 'Hamiline yazılı olması',
        },
        'B',
        'TTK md. 681 ve 824: kambiyo senetleri KANUNEN EMRE YAZILIDIR; bu nedenle ayrıca emre kaydı aranmaksızın ciro ve teslimle devredilir.',
    ),
    # düzey 1
    '0043': patch(
        'Bir poliçe muhataba ibraz edilmiş ancak muhatap kabulden kaçınmıştır. Buna göre hamilin izleyeceği yol aşağıdakilerden hangisidir?',
        {
            'A': 'Muhatabı kabule zorlamak için dava açmak',
            'B': 'Protesto çekmeksizin doğrudan icra takibi başlatmak ve müracaat hakkını kullanmak',
            'C': 'Vadenin gelmesini beklemek dışında bir yol izlememek',
            'D': 'Senedi geçersiz saymak',
            'E': 'Kabul etmeme protestosu çekerek müracaat hakkını kullanmak',
        },
        'E',
        'TTK md. 714 ve 716: muhatap kabulden kaçınırsa hamil KABUL ETMEME PROTESTOSU çekerek vadeden önce müracaat hakkını kullanabilir; muhatabı kabule zorlama imkânı yoktur.',
    ),
    # düzey 1
    '0044': patch(
        'Bir bononun düzenleyeni ödeme yapmamıştır. Hamil düzenleyene başvurmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bono düzenleyeni asıl borçlu olduğundan ona başvuru için protesto gerekmez',
            'B': 'Düzenleyenin sorumluluğu vadeyle sona erer',
            'C': 'Düzenleyene başvuru için mahkeme kararı gerekir',
            'D': 'Bono düzenleyeni, yalnızca cirantalar ödeme yapmadığı takdirde ikinci derecede sorumlu tutulur',
            'E': 'Düzenleyene başvuru için de protesto çekilmesi gerekir',
        },
        'A',
        'TTK md. 778/3: bono düzenleyeni poliçeyi KABUL EDEN MUHATAP gibi sorumludur; asıl borçlu olduğundan ona başvurmak için protesto çekilmesi gerekmez.',
    ),
    # düzey 1
    '0045': patch(
        "Bir çekin üzerine 'kabul edilmiştir' şerhi düşülmüştür. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Çekte kabul yasak olduğundan şerh yazılmamış sayılır',
            'B': 'Kabul şerhi, yalnızca muhatap bankanın ayrıca yazılı onay vermesi hâlinde geçerli olur',
            'C': 'Şerh geçerlidir ve banka asıl borçlu olur',
            'D': 'Şerh çeki bonoya dönüştürür',
            'E': 'Şerh çeki geçersiz kılar',
        },
        'A',
        'TTK md. 784: çekte KABUL YASAKTIR; çek üzerine yazılan kabul şerhi YAZILMAMIŞ sayılır. Banka kabul yoluyla asıl borçlu hâline gelmez.',
    ),
    # düzey 1
    '0046': patch(
        'Bir poliçede vade gösterilmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vade hamil tarafından serbestçe doldurulur',
            'B': 'Vade muhatabın belirlediği tarihtir',
            'C': 'Poliçe geçersizdir',
            'D': 'Poliçe görüldüğünde ödenecek sayılır',
            'E': 'Poliçe bir yıl sonra ödenecek sayılır',
        },
        'D',
        'TTK md. 672: vadesi gösterilmemiş poliçe, GÖRÜLDÜĞÜNDE ödenecek poliçe sayılır.',
    ),
    # düzey 1
    '0047': patch(
        "Bir senette 'bono' veya 'emre muharrer senet' kelimesi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Senet çek sayılır',
            'B': 'Senet bono sayılmaz; kanunen tamamlanamayan bir zorunlu unsur eksiktir',
            'C': 'Senet yine bono sayılır',
            'D': "Senet metnindeki 'bono' kelimesi eksikliği, sonradan hamil tarafından tamamlanabilir",
            'E': 'Senet poliçeye dönüşür',
        },
        'B',
        "TTK md. 776-777: senet metninde 'BONO' veya 'EMRE MUHARRER SENET' kelimesinin bulunması zorunludur ve bu eksiklik kanunen tamamlanamaz; senet bono sayılmaz.",
    ),
    # düzey 1
    '0048': patch(
        "Bir hamil, senedi devralırken borçlunun zararına hareket ettiğini bilmektedir. Buna göre def'iler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Hamilin bilgisi def'i rejimini etkilemez",
            'B': "Def'i ileri sürmek için ayrıca dava açılması gerekir",
            'C': "Borçlu hiçbir def'iyi ileri süremez",
            'D': "Borçlu, temel ilişkiye dayanan kişisel def'ilerini bu hamile karşı ileri sürebilir",
            'E': "Borçlu, hamilin bilgisine bakılmaksızın yalnızca senedin metninden anlaşılan def'ileri ileri sürebilir",
        },
        'D',
        "TTK md. 687: borçlu, önceki hamillerle arasındaki kişisel ilişkilere dayanan def'ileri, hamil senedi devralırken BİLEREK BORÇLUNUN ZARARINA HAREKET ETMİŞ olmadıkça ileri süremez; bu koşul gerçekleşince def'iler ileri sürülebilir.",
    ),
    # düzey 1
    '0049': patch(
        "Bir kambiyo senedinde 'protestosuz' kaydı bulunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kayıt yalnızca çeklerde kullanılabilir',
            'B': 'Kayıt geçersizdir ve protesto yine gereklidir',
            'C': 'Hamil, müracaat hakkını kullanmak için protesto çekme külfetinden kurtulur',
            'D': "'Protestosuz' kaydı, hamilin cirantalara ve düzenleyene karşı müracaat hakkını tümüyle ortadan kaldırır",
            'E': 'Kayıt senedi geçersiz kılar',
        },
        'C',
        "TTK md. 722: düzenleyen, ciranta veya aval veren, senede 'PROTESTOSUZ' ya da 'masrafsız' kaydını koyarak hamili protesto çekme külfetinden kurtarabilir; müracaat hakkı devam eder.",
    ),
    # düzey 1
    '0050': patch(
        'Bir cirantanın sorumluluğu incelenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ciranta, aksi kararlaştırılmadıkça kabul edilmeme ve ödenmemeden sorumludur',
            'B': 'Ciranta hiçbir sorumluluk üstlenmez',
            'C': 'Ciranta yalnızca kendisinden sonraki hamillere karşı sorumsuzdur',
            'D': 'Ciranta yalnızca asıl borçlu ödeme yapmazsa ve mahkeme kararıyla sorumlu olur',
            'E': 'Cirantanın sorumluluğu senet üzerinde açıkça yazılmadıkça doğmaz',
        },
        'A',
        "TTK md. 685: ciranta, aksi kararlaştırılmadıkça poliçenin KABUL EDİLMEMESİNDEN ve ÖDENMEMESİNDEN sorumludur; sorumluluk kanundan doğar. Ciranta 'ciro edilemez' kaydıyla sonraki hamillere karşı sorumluluğunu kaldırabilir.",
    ),
    # düzey 2
    '0051': patch(
        'Kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kambiyo senetleri kanunen emre yazılıdır. II. Kambiyo senetleri mücerret senetlerdir. III. Çekte vade gösterilebilir.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'A',
        'I doğrudur (TTK md. 681, 824). II doğrudur. III YANLIŞTIR: md. 795 uyarınca çek görüldüğünde ödenir; aksine kayıtlar yazılmamış sayılır.',
    ),
    # düzey 3
    '0052': patch(
        'Kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Bonoda muhatap bulunur. II. Çekte muhatap ancak banka olabilir. III. İmzaların bağımsızlığı ilkesi geçerlidir. IV. Vadesi gösterilmeyen poliçe geçersizdir.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve IV',
            'D': 'I ve II',
            'E': 'I, III ve IV',
        },
        'C',
        'I YANLIŞ: bonoda muhatap yoktur (TTK md. 776). IV YANLIŞ: vadesi gösterilmeyen poliçe görüldüğünde ödenecek sayılır (md. 672). II (md. 782) ve III (md. 677) doğrudur.',
    ),
    # düzey 2
    '0053': patch(
        'Aval ve ciro ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Aval veren, lehine aval verdiği kişi gibi sorumludur. II. Tahsil cirosu mülkiyeti devretmez. III. Beyaz ciro geçersizdir.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'A',
        'I doğrudur (TTK md. 702). II doğrudur (md. 688). III YANLIŞTIR: md. 683 uyarınca beyaz ciro geçerlidir ve yalnızca cirantanın imzasıyla yapılır.',
    ),
    # düzey 3
    '0054': patch(
        'Zamanaşımı ve müracaat ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kabul edene karşı talepler vadeden itibaren üç yılda zamanaşımına uğrar. II. Protesto senedin geçerlilik şartıdır. III. Zamanaşımı dolsa da sebepsiz zenginleşme davası açılabilir. IV. Bono düzenleyenine başvuru için protesto gerekir.',
        {
            'A': 'I, II ve IV',
            'B': 'II ve IV',
            'C': 'Yalnız II',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'B',
        'II YANLIŞ: protesto geçerlilik şartı değil, müracaat hakkının korunması için gereken bir işlemdir. IV YANLIŞ: bono düzenleyeni asıl borçludur, ona başvuru için protesto gerekmez (TTK md. 778/3). I (md. 749) ve III (md. 732) doğrudur.',
    ),
    # düzey 2
    '0055': patch(
        'Çek ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Çek görüldüğünde ödenir. II. Çekte kabul yasaktır. III. Çekte muhatap herhangi bir tüzel kişi olabilir.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        'I doğrudur (TTK md. 795). II doğrudur (md. 784). III YANLIŞTIR: md. 782 uyarınca çekte muhatap ancak BANKA olabilir.',
    ),
    # düzey 2
    '0056': patch(
        'Bir poliçede ödeme yeri gösterilmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Muhatabın adı yanında yazılı yer ödeme yeri sayılır',
            'B': 'Ödeme yeri mahkemece belirlenir',
            'C': 'Poliçe geçersizdir',
            'D': 'Ödeme yeri hamilin yerleşim yeridir',
            'E': 'Ödeme yeri, poliçeyi düzenleyen kişinin yerleşim yeri olarak kabul edilir',
        },
        'A',
        'TTK md. 672: ödeme yeri gösterilmemiş poliçede, MUHATABIN ADI YANINDA yazılı olan yer ödeme yeri ve aynı zamanda muhatabın yerleşim yeri sayılır.',
    ),
    # düzey 2
    '0057': patch(
        'Bir kambiyo senedinde düzenlenme tarihi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Düzenlenme tarihindeki eksiklik, borçlunun onayı aranmaksızın hamil tarafından her zaman serbestçe doldurulabilir',
            'B': 'Tarih eksikliği senedi etkilemez',
            'C': 'Düzenlenme tarihi kanunen tamamlanamayan zorunlu bir unsurdur; senet o tür kambiyo senedi sayılmaz',
            'D': 'Tarih eksikliği yalnızca çekte sonuç doğurur',
            'E': 'Tarih muhatabın beyanına göre belirlenir',
        },
        'C',
        'TTK md. 671, 776 ve 780: DÜZENLENME TARİHİ poliçe, bono ve çekin zorunlu unsurlarındandır ve kanunen tamamlanamaz; yokluğu senedi o tür kambiyo senedi olmaktan çıkarır.',
    ),
    # düzey 2
    '0058': patch(
        'Bir hamil, süresinde ibraz etmediği çekin bedelini cirantadan istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çekte ibraz süresi bulunmadığından sorun doğmaz',
            'B': 'İbraz süresi geçmiş olsa dahi hamilin cirantalara ve düzenleyene karşı müracaat hakkı devam eder',
            'C': 'İbraz süresi geçtiğinde çek geçersiz olur',
            'D': 'Süresinde ibraz edilmeyen çekte hamilin cirantalara karşı müracaat hakkı düşer',
            'E': 'Müracaat hakkı yalnızca düzenleyene karşı düşer',
        },
        'D',
        'TTK md. 808: süresi içinde ibraz edilmeyen çekte hamilin cirantalara, düzenleyene ve diğer borçlulara karşı MÜRACAAT HAKKI DÜŞER. Çek geçersiz olmaz; sebepsiz zenginleşme ve temel ilişkiye dayanan talepler ayrıca değerlendirilir.',
    ),
    # düzey 2
    '0059': patch(
        'Kambiyo senetlerinde şekle bağlılık incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tamamlanamayan unsur eksikse senet o tür kambiyo senedi sayılmaz',
            'B': 'Zorunlu unsurların tamamı kanunen tamamlanabilir niteliktedir',
            'C': 'Bazı eksiklikler kanunen tamamlanır (vade, ödeme yeri, düzenlenme yeri)',
            'D': 'Senet kelimesi ve imza gibi unsurlar tamamlanamaz',
            'E': 'Kambiyo senetleri şekle sıkı biçimde bağlıdır',
        },
        'B',
        'TTK md. 671-672, 776-777, 780-781: zorunlu unsurların yalnızca BİR KISMI (vade, ödeme yeri, düzenlenme yeri) kanunen tamamlanır. Senet kelimesi, imza ve düzenlenme tarihi gibi unsurlar TAMAMLANAMAZ.',
    ),
    # düzey 3
    '0060': patch(
        'Kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kambiyo senetleri poliçe, bono ve çektir. II. Aval veren, lehine aval verilenin borcu şekil noksanı dışında geçersiz olsa da sorumludur. III. Tahsil cirosu mülkiyeti devreder. IV. Çekte kabul mümkündür.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'III ve IV',
            'D': 'I, III ve IV',
            'E': 'Yalnız III',
        },
        'C',
        'III YANLIŞ: tahsil cirosu mülkiyeti devretmez (TTK md. 688). IV YANLIŞ: md. 784 uyarınca çekte KABUL YASAKTIR. I (md. 670 vd.) ve II (md. 702) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Kambiyo Senetleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
