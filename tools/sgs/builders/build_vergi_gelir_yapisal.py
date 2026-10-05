#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gelir Vergisi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim: mukellefiyet, zarar mahsubu, ticari/zirai kazanc, basit usul, ucret, serbest meslek, GMSI, MSI, deger artisi, istisnalar (7582 m. 20/D dahil), beyan-indirim-odeme, tevkifat. 17 hesap sorusu bagimsiz dogrulandi; yila bagli tutar sorulmadi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 193 sayili GVK guncel metni (mevzuat.gov.tr, 7582 sayili Kanun dahil islenmis)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/gelir_vergisi.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "gelir-gen-"


def patch(stem, options, answer, solution, ref='193 sayili Gelir Vergisi Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "193 sayılı Gelir Vergisi Kanunu'na göre aşağıdaki kişilerden hangisi Türkiye'de yerleşmiş sayılmaz?",
        {
            'A': "İkametgâhı Türkiye'de olup yılın dört ayını yurt dışında geçiren kişi",
            'B': "İkametgâhı İzmir'de bulunan yabancı",
            'C': 'Tedavi için gelip yedi ay kalan yabancı',
            'D': 'Süresiz iş sözleşmesiyle yedi ay çalışan yabancı',
            'E': "Kısa yurt dışı izinleri dışında yıl boyu Türkiye'de oturan yabancı",
        },
        'C',
        "GVK m. 4'e göre ikametgâhı Türkiye'de bulunanlar ile bir takvim yılında Türkiye'de devamlı olarak altı aydan fazla oturanlar yerleşmiş sayılır; geçici ayrılmalar süreyi kesmez. m. 5 ise belli ve geçici görevle gelenler ile tahsil, **tedavi**, istirahat veya seyahat amacıyla gelen yabancıları altı aydan fazla kalsalar da yerleşmiş saymaz. Süresiz iş sözleşmesiyle çalışan yabancı geçici görevle gelmiş sayılmaz.",
        '193 sayılı Gelir Vergisi Kanunu m. 4-5',
    ),
    # düzey 3
    '0002': patch(
        "Kazancını bilanço esasına göre tespit eden bir tacirin 2020 yılı ticari zararı 150.000 ₺'dir. Sonraki yıllardaki ticari kazançları 2021: 20.000 ₺, 2022: 25.000 ₺, 2023: 30.000 ₺, 2024: 15.000 ₺, 2025: 40.000 ₺ ve 2026: 60.000 ₺'dir. Başka geliri olmayan tacirin 2026 yılı gelir vergisi matrahı kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '60.000',
            'C': '0',
            'D': '20.000',
            'E': '30.000',
        },
        'B',
        "Mahsup edilemeyen zarar sonraki yılların gelirinden indirilir; ancak arka arkaya **beş yıl** içinde mahsup edilemeyen bakiye sonraki yıllara devredilemez (m. 88). 2020 zararı 2021-2025 yıllarında 20 + 25 + 30 + 15 + 40 = 130.000 ₺ mahsup edilir; kalan 20.000 ₺ 2025 sonunda düşer. 2026 matrahı **60.000 ₺**'dir. 40.000 ₺, süre sınırı gözetilmeden kalan zararın 2026'da indirilmesiyle bulunur.",
        '193 sayılı Gelir Vergisi Kanunu m. 88',
    ),
    # düzey 2
    '0003': patch(
        "Aşağıdaki kazançlardan hangileri GVK'ya göre ticari kazanç sayılır?\n\nI. Faaliyetine devam eden işletmenin bir şubesinin satışından doğan kazanç\n\nII. İşletmeye kayıtlı amortismana tabi bir makinenin satış kazancı\n\nIII. Tacirin işletmesine kayıtlı olmayan konutunu iki yıl sonra satmasından doğan kazanç",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız III',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'E',
        "Mükerrer m. 80'in son fıkrasına göre faaliyetine devam eden ticari işletmenin kısmen veya tamamen satılmasından (I) ve işletmeye dâhil amortismana tabi iktisadi kıymetlerin elden çıkarılmasından (II) doğan kazançlar **ticari kazançtır**. Tüccara ait olsa da işletmeye dâhil olmayan gayrimenkule GMSİ hükümleri uygulanır; beş yıl içinde satışından doğan kazanç (III) **değer artışı kazancıdır**.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 80',
    ),
    # düzey 2
    '0004': patch(
        "Ticari kazancın tespitinde, 7577 sayılı Kanunla GVK m. 41'e eklenen hükümle aşağıdaki giderlerden hangisinin indirilmesi kabul edilmez?",
        {
            'A': 'Şans ve bahis oyunlarının reklam giderleri',
            'B': 'İşle ilgili ödenen sözleşmeden doğan tazminat',
            'C': "VUK'a göre ayrılan amortismanlar",
            'D': 'İşçilerin işyerindeki tedavi ve ilaç giderleri',
            'E': 'İşletmeyle ilgili ayni vergi, resim ve harçlar',
        },
        'A',
        "7577 sayılı Kanunla m. 41'e eklenen 12. bent (yürürlük 17/4/2026) uyarınca **her türlü şans ve bahis oyunlarına ait ilan ve reklam giderleri** gider olarak indirilemez. İşle ilgili sözleşme, ilam veya kanuna dayanan tazminatlar (m. 40/3), işletmeyle ilgili ayni vergi ve harçlar (m. 40/6), amortismanlar (m. 40/7) ve işçilerin tedavi giderleri (m. 40/2) indirilebilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 41',
    ),
    # düzey 2
    '0005': patch(
        "GVK m. 41'deki gider kısıtlamalarının uygulanmasında aşağıdakilerden hangileri teşebbüs sahibi sayılır?\n\nI. Kollektif şirket ortağı\n\nII. Adi komandit şirketin komanditer ortağı\n\nIII. Adi komandit şirketin komandite ortağı",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'C',
        "m. 41'in son fıkrasına göre **kollektif şirketlerin ortakları** ile adi ve eshamlı komandit şirketlerin **komandite ortakları** teşebbüs sahibi sayılır. Sorumluluğu sınırlı olan komanditer ortak teşebbüs sahibi değildir; kâr payı da m. 75 uyarınca menkul sermaye iradıdır.",
        '193 sayılı Gelir Vergisi Kanunu m. 41 son fıkra',
    ),
    # düzey 1
    '0006': patch(
        "Basit usule tabi olmanın şartlarından birini takvim yılı içinde kaybeden mükellef, GVK'ya göre ne zamandan itibaren gerçek usulde vergilendirilir?",
        {
            'A': 'Şartın kaybedildiği tarihten',
            'B': 'Ertesi takvim yılı başından',
            'C': 'İzleyen ayın başından',
            'D': 'İki yıl sonraki yılın başından',
            'E': 'İzleyen geçici vergi döneminden',
        },
        'B',
        "m. 46'ya göre basit usule tabi olmanın şartlarından herhangi birini takvim yılı içinde kaybedenler **ertesi takvim yılı başından** itibaren gerçek usulde vergilendirilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 46',
    ),
    # düzey 3
    '0007': patch(
        'Aşağıdaki çiftçilerden hangisinin zirai kazancı, işletme büyüklüğü ölçülerine bakılmaksızın gerçek usulde vergilendirilir?',
        {
            'A': 'On beş yaşında üç traktöre sahip çiftçi',
            'B': 'Hasılatından tevkifat yapılan çiftçi',
            'C': 'İki traktöre sahip çiftçi',
            'D': 'Ürününü kamyonetle pazara taşıyan çiftçi',
            'E': 'Bir biçerdövere sahip çiftçi',
        },
        'E',
        "m. 53'e göre işletme büyüklüğü ölçülerini aşan çiftçiler ile **bir biçerdövere** veya bu mahiyette bir motorlu araca ya da **on yaşına kadar ikiden fazla** traktöre sahip çiftçilerin kazançları gerçek usulde tespit edilir. İki traktör sınırı aşmaz; on beş yaşındaki traktörler hesaba girmez. Diğer çiftçilerin kazancı hasılatları üzerinden tevkifatla vergilendirilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 53',
    ),
    # düzey 2
    '0008': patch(
        "Aşağıdaki ücretlerden hangisi GVK m. 23'e göre gelir vergisinden istisna değildir?",
        {
            'A': 'Maden işçisinin yer altında çalıştığı süreye ait ücreti',
            'B': 'Evde çocuklara bakan mürebbiyenin ücreti',
            'C': 'Köy bütçesinden ödenen köy bekçisinin ücreti',
            'D': 'Çırağın asgari ücreti aşmayan ücreti',
            'E': 'Apartmanda çalışan kapıcının ücreti',
        },
        'B',
        'm. 23/6 özel fertler tarafından evlerde, bahçelerde ve apartmanlarda çalıştırılan hizmetçilerin (kapıcılar dâhil) ücretlerini istisna eder; ancak **mürebbiyelere ödenen ücretler** açıkça istisna dışında bırakılmıştır. Yer altı maden işçileri (m. 23/3), köy bütçesinden ödenen bekçi ücretleri (m. 23/5) ve çırakların asgari ücreti aşmayan ücretleri (m. 23/12) istisnadır.',
        '193 sayılı Gelir Vergisi Kanunu m. 23',
    ),
    # düzey 1
    '0009': patch(
        "Konser vermeyi mutat meslek hâline getirmiş bir müzik sanatçısının konserlerden elde ettiği kazanç GVK'ya göre hangi gelir unsuruna girer?",
        {
            'A': 'Ticari kazanç',
            'B': 'Arızi kazanç',
            'C': 'Ücret',
            'D': 'Serbest meslek kazancı',
            'E': 'Menkul sermaye iradı',
        },
        'D',
        "m. 66/4 uyarınca **konser veren müzik sanatçıları** bu işleri dolayısıyla serbest meslek erbabı sayılır. Faaliyet mutat meslek hâlinde yapıldığı için arızi kazanç söz konusu değildir; arızi olarak yapılan serbest meslek faaliyetinin hasılatı m. 82'ye göre arızi kazanç olurdu.",
        '193 sayılı Gelir Vergisi Kanunu m. 66/4',
    ),
    # düzey 2
    '0010': patch(
        "Serbest meslek erbabı bakımından aşağıdakilerden hangileri GVK'ya göre tahsil hükmündedir?\n\nI. Haberdar olması kaydıyla adına bankaya para yatırılması\n\nII. Meslek alacağının başka bir kişiye bedelsiz temliki\n\nIII. Meslek alacağının müşteriye olan borçla takası",
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'E',
        "m. 67'ye göre ıttıla hâsıl etmeleri (haberdar olmaları) kaydıyla serbest meslek erbabı adına kamu müessesesine, icra dairesine, bankaya, notere veya postaya para yatırılması (I); serbest meslek alacağının başka bir şahsa temliki, temlikin ivazlı olup olmadığına bakılmaksızın (II); ve alacağın müşteriye olan borçla takası (III) **tahsil hükmündedir**.",
        '193 sayılı Gelir Vergisi Kanunu m. 67',
    ),
    # düzey 2
    '0011': patch(
        "Bir kişi babasından miras kalan ve herhangi bir işletmeye dâhil olmayan markanın kullanım hakkını bir firmaya kiralamıştır. Elde ettiği kira geliri GVK'ya göre hangi gelir unsuruna girer?",
        {
            'A': 'Gayrimenkul sermaye iradı',
            'B': 'Menkul sermaye iradı',
            'C': 'Ticari kazanç',
            'D': 'Serbest meslek kazancı',
            'E': 'Arızi kazanç',
        },
        'A',
        'm. 70/5 uyarınca alameti farika, **marka**, ticaret unvanı gibi hakların kiraya verilmesinden elde edilen iratlar **gayrimenkul sermaye iradıdır**. Mal veya hak ticari bir işletmeye dâhil olsaydı irat ticari kazancın tespitine ilişkin hükümlere göre hesaplanırdı.',
        '193 sayılı Gelir Vergisi Kanunu m. 70/5',
    ),
    # düzey 2
    '0012': patch(
        "Aşağıdaki durumların hangisinde GVK m. 73'teki emsal kira bedeli esası uygulanır?",
        {
            'A': 'Konutun annesinin ikametine bedelsiz tahsisi',
            'B': 'Konutun belediyeye düşük bedelle kiralanması',
            'C': 'Konutun kardeşin ikametine bedelsiz tahsisi',
            'D': 'Boş konutun korunması için bir bekçiye bırakılması',
            'E': 'Konutun yeğene bedelsiz verilmesi',
        },
        'E',
        "m. 73'e göre bedelsiz olarak başkalarının intifasına bırakılan mal ve hakların emsal kira bedeli kira sayılır. İstisnalar: binaların mal sahibinin **usul, füru veya kardeşlerinin** ikametine tahsisi, boş kalan gayrimenkullerin korunması için bedelsiz ikamete bırakılması, akrabaların mal sahibiyle aynı evde oturması ve kamu idarelerince yapılan kiralamalar. **Yeğen** bu sayımda yer almaz; emsal kira bedeli uygulanır.",
        '193 sayılı Gelir Vergisi Kanunu m. 73',
    ),
    # düzey 2
    '0013': patch(
        "GVK m. 21'deki mesken kira geliri istisnasına ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ticari kazancını beyan eden tacir de yararlanır',
            'B': 'İşyeri kiraları istisnaya konu olmaz',
            'C': 'İstisnaya isabet eden giderler indirilmez',
            'D': 'Hadden fazla hasılat beyan edilmezse istisna kaybedilir',
            'E': 'İstisna binaların mesken olarak kiraya verilmesine ilişkindir',
        },
        'A',
        "m. 21'e göre istisna binaların **mesken** olarak kiraya verilmesinden elde edilen hasılata uygulanır. İstisna haddini aşan hasılat beyan edilmez veya eksik beyan edilirse istisnadan yararlanılamaz. **Ticari, zirai veya mesleki kazancını yıllık beyanname ile bildirmek mecburiyetinde olanlar** bu istisnadan faydalanamaz. m. 74'e göre istisna edilen hasılata isabet eden giderler indirilmez.",
        '193 sayılı Gelir Vergisi Kanunu m. 21, 74',
    ),
    # düzey 3
    '0014': patch(
        "Ticari kazancı nedeniyle beyanname verdiği için mesken istisnasından yararlanamayan bir kişi, 2024 yılında kredi kullanarak 3.000.000 ₺'ye aldığı tek dairesini konut olarak kiraya vermektedir. 2026'da kredi faizi 200.000 ₺, daire için ödediği emlak vergisi 5.000 ₺'dir. Gerçek gider usulünde indirebileceği toplam tutar kaç ₺'dir?",
        {
            'A': '155.000',
            'B': '150.000',
            'C': '205.000',
            'D': '5.000',
            'E': '355.000',
        },
        'A',
        "7566 sayılı Kanunla değişen m. 74/4'e göre borç faizleri **konutlar hariç** olmak üzere indirilebilir; konut için kullanılan kredinin faizi indirilemez. Buna karşılık konut olarak kiraya verilen bir adet gayrimenkulün iktisap yılından itibaren beş yıl süreyle **iktisap bedelinin %5'i** indirilir: 3.000.000 × %5 = 150.000 ₺. Emlak vergisi m. 74/5 uyarınca indirilir. Toplam 150.000 + 5.000 = **155.000 ₺**; faiz de indirilseydi 355.000 ₺ bulunurdu.",
        '193 sayılı Gelir Vergisi Kanunu m. 74/4 (7566 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0015': patch(
        'Gayrimenkul ticaretiyle uğraşmayan bir kişinin aşağıdaki satışlarından hangileri değer artışı kazancı olarak vergilendirilir?\n\nI. Satın aldığı konutu üç yıl sonra kârla satması\n\nII. Mirasla edindiği konutu bir yıl sonra kârla satması\n\nIII. Satın aldığı arsayı altı yıl sonra kârla satması',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'E',
        "Mükerrer m. 80/6'ya göre gayrimenkullerin iktisap tarihinden başlayarak **beş yıl içinde** elden çıkarılmasından doğan kazançlar değer artışı kazancıdır; ancak **ivazsız olarak** (miras, bağış) iktisap edilenler kapsam dışındadır. Üç yıl sonra satılan konut (I) vergilendirilir; mirasla edinilen konut (II) ve beş yıldan sonra satılan arsa (III) vergilendirilmez.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 80/6',
    ),
    # düzey 2
    '0016': patch(
        'Kazancını bilanço esasına göre tespit eden bir ferdi işletme sahibi, işletmesini aktif ve pasifiyle bütün hâlinde bir anonim şirkete devretmiş; devir bilançosu şirket bilançosuna aynen geçirilmiş ve karşılığında öz sermaye tutarında nama yazılı hisse senedi almıştır. Bu devir için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Arızi kazanç olarak vergilenir',
            'B': 'Değer artışı kazancı hesaplanmaz',
            'C': 'Ticari kazanç olarak vergilenir',
            'D': 'Değer artışı kazancı olarak vergilenir',
            'E': 'Kazancın yarısı vergilenir',
        },
        'B',
        "m. 81/2'ye göre bilanço esasına göre defter tutan ferdi işletmenin aktif ve pasifiyle bütün hâlinde bir sermaye şirketine devredilmesi, bilançonun aynen geçirilmesi ve sahibinin öz sermaye tutarında ortaklık payı alması hâlinde **değer artışı kazancı hesaplanmaz**. Ortaklık payını temsil eden hisse senetlerinin **nama yazılı** olması şarttır.",
        '193 sayılı Gelir Vergisi Kanunu m. 81/2',
    ),
    # düzey 2
    '0017': patch(
        'Esnaf muaflığına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Muaflar alış belgelerini saklar',
            'B': 'Muaflık tevkifat yoluyla alınan vergiyi de kapsar',
            'C': 'Motorsuz gezici perakendeci yararlanabilir',
            'D': 'Gerçek usulde vergilendirilenler yararlanamaz',
            'E': 'Talep edene vergi dairesince belge verilir',
        },
        'B',
        "m. 9'un son fıkrasına göre esnaf muaflığının **m. 94 uyarınca tevkif suretiyle kesilen vergiye şümulü yoktur**. Ticari, zirai veya mesleki kazancı nedeniyle gerçek usulde vergilendirilenler muaflıktan yararlanamaz; motorlu nakil vasıtası kullanmadan gezici perakende ticaret yapanlar muaftır. Muaflar alış ve gider belgelerini saklar ve talep edenlere vergi dairesince Esnaf Vergi Muafiyeti Belgesi verilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 9',
    ),
    # düzey 1
    '0018': patch(
        "Yıllık beyanname ile bildirilen gelir üzerinden tahakkuk eden gelir vergisi GVK'ya göre nasıl ödenir?",
        {
            'A': "Mart ve Kasım'da iki eşit taksitte",
            'B': 'Tamamı Mart ayında',
            'C': "Nisan ve Ekim'de iki eşit taksitte",
            'D': "Mart ve Temmuz'da iki eşit taksitte",
            'E': "Mart ve Haziran'da iki eşit taksitte",
        },
        'D',
        "7338 sayılı Kanunla değişen m. 117'ye göre yıllık beyanname ile bildirilen gelir üzerinden tahakkuk ettirilen gelir vergisi **Mart ve Temmuz** aylarında olmak üzere iki eşit taksitte ödenir.",
        '193 sayılı Gelir Vergisi Kanunu m. 117',
    ),
    # düzey 3
    '0019': patch(
        "Beyan edilen geliri 1.000.000 ₺ olan ve kalkınmada öncelikli yörede bulunmayan bir mükellef, kamu yararına çalışan bir derneğe 80.000 ₺ ve Türkiye Kızılay Derneğine 30.000 ₺ makbuz karşılığı nakdi bağış yapmıştır. Beyannamede indirilebilecek toplam bağış kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '110.000',
            'C': '30.000',
            'D': '80.000',
            'E': '100.000',
        },
        'D',
        "m. 89/4'e göre kamu yararına çalışan derneklere yapılan bağışlar beyan edilen gelirin **%5'i** ile sınırlıdır: 1.000.000 × %5 = 50.000 ₺. m. 89/11'e göre Türkiye Kızılay Derneğine yapılan nakdi bağışların ise **tamamı** indirilir: 30.000 ₺. Toplam **80.000 ₺**. Sınır gözetilmezse 110.000 ₺ bulunur.",
        '193 sayılı Gelir Vergisi Kanunu m. 89/4, 89/11',
    ),
    # düzey 2
    '0020': patch(
        "Aşağıdakilerden hangisi GVK'daki vergiye uyumlu mükelleflere vergi indiriminden yararlanamaz?",
        {
            'A': 'Serbest meslek erbabı',
            'B': 'Ücret geliri elde eden hizmet erbabı',
            'C': 'Bilanço esasına göre defter tutan tacir',
            'D': 'Kurumlar vergisi mükellefi imalatçı',
            'E': 'Gerçek usule tabi çiftçi',
        },
        'B',
        "Mükerrer m. 121'deki indirim, **ticari, zirai veya mesleki faaliyeti** nedeniyle gelir vergisi mükellefi olanlar ile kurumlar vergisi mükelleflerine (finans, bankacılık, sigorta ve emeklilik sektörü hariç) tanınır. Yalnız ücret geliri elde eden hizmet erbabı bu indirimin kapsamında değildir. İndirim, beyanname üzerinden hesaplanan verginin %5'idir.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 121',
    ),
    # düzey 2
    '0021': patch(
        "Merkezi Türkiye'de bulunan bir bankanın Londra şubesinde görevlendirilip orada oturan Türk vatandaşı, bu görevi nedeniyle aldığı ücret için İngiltere'de gelir vergisi ödemiştir. Bu ücretin Türkiye'deki vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Dar mükellefiyet kapsamında vergilendirilir',
            'B': "Türkiye'de tevkif yoluyla vergilendirilir",
            'C': "Yarısı Türkiye'de vergilendirilir",
            'D': "Türkiye'de ayrıca vergilendirilmez",
            'E': "Türkiye'de beyan edilip yabancı vergi mahsup edilir",
        },
        'D',
        "GVK m. 3/2'ye göre merkezi Türkiye'de bulunan teşebbüslerin işleri dolayısıyla yabancı memleketlerde oturan Türk vatandaşları **tam mükelleftir**. Ancak aynı bendin parantez içi hükmüne göre bulundukları ülkede bu kazanç ve iratlar nedeniyle gelir vergisine veya benzeri bir vergiye tabi tutulanlar, bu kazanç ve iratlar üzerinden Türkiye'de ayrıca vergilendirilmez.",
        '193 sayılı Gelir Vergisi Kanunu m. 3/2',
    ),
    # düzey 2
    '0022': patch(
        "Gelirin toplanmasında aşağıdaki zararlardan hangisi GVK'ya göre diğer gelir kaynaklarının kazanç ve iratlarından mahsup edilemez?",
        {
            'A': 'Limited şirket hissesinin satış zararı',
            'B': 'Ticari faaliyetten doğan zarar',
            'C': 'Zirai işletme hesabı esasındaki zarar',
            'D': 'Gerçek gider usulündeki GMSİ gider fazlası',
            'E': 'Serbest meslek faaliyetinden doğan zarar',
        },
        'A',
        "m. 88'e göre gelir kaynaklarının bir kısmından doğan zararlar diğer kaynakların kazanç ve iratlarından mahsup edilir; ancak **80. maddedeki diğer kazanç ve iratlardan** (değer artışı ve arızi kazançlar) doğan zararlar bu kuralın dışındadır. Ortaklık hissesinin satışı değer artışı kazancı konusudur. Sermaye iratlarında gider fazlasından doğan zarar ise zarar sayılır.",
        '193 sayılı Gelir Vergisi Kanunu m. 88',
    ),
    # düzey 2
    '0023': patch(
        "Bilanço esasına göre defter tutan bir tacirin öz sermayesi dönem başında 500.000 ₺, dönem sonunda 800.000 ₺'dir. Tacir dönem içinde işletmeye 100.000 ₺ nakit koymuş, işletmeden de 50.000 ₺ çekmiştir. Kanunen kabul edilmeyen gideri olmayan tacirin ticari kazancı kaç ₺'dir?",
        {
            'A': '150.000',
            'B': '300.000',
            'C': '350.000',
            'D': '400.000',
            'E': '250.000',
        },
        'E',
        'Bilanço esasında ticari kazanç, öz sermayenin dönem sonu ve dönem başı değerleri arasındaki müspet farktır: 800.000 − 500.000 = 300.000 ₺. Dönem içinde işletmeye ilave olunan değerler bu farktan **indirilir**, işletmeden çekilen değerler farka **ilave olunur** (m. 38): 300.000 − 100.000 + 50.000 = **250.000 ₺**. 350.000 ₺ düzeltmelerin ters yönde yapılmasının sonucudur.',
        '193 sayılı Gelir Vergisi Kanunu m. 38',
    ),
    # düzey 3
    '0024': patch(
        'Ticari kazancını gerçek usulde tespit eden bir tacirin aşağıdaki ödemelerinden hangisi ticari kazancın tespitinde gider olarak indirilebilir?',
        {
            'A': 'İşletmede çalışan küçük çocuğuna ödenen ücret',
            'B': 'İşletme aracı için ödenen trafik para cezası',
            'C': 'İşletmeye koyduğu sermaye için yürüttüğü faiz',
            'D': 'İşletmede çalışan reşit oğluna ödenen ücret',
            'E': 'Muhasebe işlerini yürüten eşine ödenen ücret',
        },
        'D',
        'GVK m. 41/2 teşebbüs sahibinin **kendisine, eşine ve küçük çocuklarına** ödenen ücretlerin gider yazılmasını yasaklar; reşit çocuklar bu sayımda yer almaz, fiilen çalışan reşit çocuğa emsale uygun ödenen ücret gider yazılabilir. Teşebbüs sahibinin sermayesi için yürütülen faiz (m. 41/3) ve her türlü para cezası (m. 41/6) kanunen kabul edilmeyen giderdir.',
        '193 sayılı Gelir Vergisi Kanunu m. 41',
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdaki mükelleflerden hangisi, diğer şartları taşısa bile ticari kazancını basit usulde tespit ettiremez?',
        {
            'A': 'Sigorta prodüktörü',
            'B': 'Mahallede çalışan berber',
            'C': 'Dükkânında terzilik yapan kişi',
            'D': 'Ev aletleri tamircisi',
            'E': 'Semtte çiçek satan esnaf',
        },
        'A',
        'GVK m. 51 basit usulden yararlanamayacakları sayar: kollektif şirket ortakları ve komandite ortaklar, ikrazatçılar, sarraflar, **sigorta prodüktörleri**, ilan ve reklam işleriyle uğraşanlar, gayrimenkul ve gemi alım satımıyla uğraşanlar, tavassut işi yapanlar ve şehirlerarası taşımacılık yapanlar bunlar arasındadır. Berber, terzi, çiçekçi ve tamirci bu sayımda yer almaz.',
        '193 sayılı Gelir Vergisi Kanunu m. 51',
    ),
    # düzey 2
    '0026': patch(
        "Gerçek usulde vergilendirilirken 2025 yılında işini terk eden bir mükellef, basit usul şartlarını taşıyarak yeniden işe başlamak istemektedir. GVK'ya göre bu kişi en erken hangi yılın başından itibaren basit usulden yararlanabilir?",
        {
            'A': '2028',
            'B': '2026',
            'C': '2016',
            'D': '2027',
            'E': '2025',
        },
        'A',
        "m. 46'ya göre gerçek usulde vergilendirilmekteyken işini terk eden mükellefler, terk tarihini **takip eden yılın başından itibaren iki yıl** geçmedikçe basit usule dönemez. 2025'te terk edilen iş için süre 1/1/2026'da başlar ve 31/12/2027'de dolar; en erken **2028** yılı başından basit usulden yararlanılabilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 46',
    ),
    # düzey 3
    '0027': patch(
        "İşveren ile işçi, hizmet sözleşmesini ikale (bozma) sözleşmesiyle sona erdirmiş ve işçiye tazminat ödenmiştir. Ödenen tutarın, İş Kanunu'na göre ödenmesi gereken kıdem tazminatı istisnasını aşan kısmı hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Değer artışı kazancı sayılır',
            'B': 'Tamamı gelir vergisinden istisnadır',
            'C': 'Arızi kazanç olarak vergilendirilir',
            'D': 'Serbest meslek kazancı sayılır',
            'E': 'Ücret olarak vergilendirilir',
        },
        'E',
        "GVK m. 61/7'ye göre hizmet sözleşmesi sona erdikten sonra ikale sözleşmesi kapsamında ödenen tazminatlar **ücret sayılır**. m. 25/7-b bu ödemeleri, kıdem tazminatı istisnasının hesabında dikkate alınmak şartıyla istisna kapsamına alır; istisna tutarını aşan kısım ücret olarak vergilendirilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 61/7, m. 25/7-b',
    ),
    # düzey 1
    '0028': patch(
        "GVK'ya göre evlenme veya doğum nedeniyle hizmet erbabına yapılan yardımların hangi tutara kadar olan kısmı gelir vergisinden istisnadır?",
        {
            'A': 'Bir aylık ücret tutarı',
            'B': "Brüt ücretin %15'i",
            'C': 'Asgari ücretin iki katı',
            'D': 'İki aylık ücret tutarı',
            'E': 'Üç aylık ücret tutarı',
        },
        'D',
        "m. 25/5'e göre evlenme ve doğum münasebetiyle hizmet erbabına yapılan yardımlarda istisna, hizmet erbabının **iki aylığına** veya buna karşılık gelen gündeliklerinin tutarına kadar olan kısma uygulanır; aşan kısım ücret olarak vergilendirilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 25/5',
    ),
    # düzey 3
    '0029': patch(
        "Bir mali müşavir, kirada oturduğu dairenin bir odasını büro olarak kullanmaktadır. Yıllık konut kirası 240.000 ₺, ısıtma ve aydınlatma giderleri 40.000 ₺'dir. Bu giderlerden serbest meslek kazancının tespitinde indirilebilecek toplam tutar kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '120.000',
            'C': '260.000',
            'D': '220.000',
            'E': '240.000',
        },
        'C',
        "m. 68/1'e göre ikametgâhının bir kısmını iş yeri olarak kullananlar, ikametgâh için ödedikleri **kiranın tamamını** ve ısıtma, aydınlatma gibi diğer giderlerin **yarısını** indirebilir: 240.000 + 40.000 / 2 = **260.000 ₺**. İkametgâh kendi mülkü olsaydı kira yerine amortismanın yarısı gider yazılabilirdi.",
        '193 sayılı Gelir Vergisi Kanunu m. 68/1',
    ),
    # düzey 2
    '0030': patch(
        'Serbest meslek kazancının tespitinde aşağıdakilerden hangisi gider olarak indirilemez?',
        {
            'A': 'Mesleki faaliyetle ilgili seyahat gideri',
            'B': 'Mesleki yayınlar için ödenen bedel',
            'C': 'Meslek odasına ödenen aidat',
            'D': "Binek otomobil yakıt giderinin %30'u",
            'E': 'Büro demirbaşının amortismanı',
        },
        'D',
        "m. 68/5'e göre işte kullanılan taşıtların giderleri indirilebilir; ancak **binek otomobillerine ilişkin giderlerin en fazla %70'i** gider yazılabilir, kalan %30 indirilemez. Mesleki yayınlar (m. 68/6), meslek teşekküllerine ödenen aidatlar (m. 68/8), mesleki seyahat giderleri (m. 68/3) ve demirbaş amortismanları (m. 68/4) indirilebilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 68/5',
    ),
    # düzey 2
    '0031': patch(
        "Tarlasını bir çiftçiye bırakan ve zirai faaliyete fiilen katılmadan yalnızca üründen pay alan arazi sahibinin bu geliri GVK'ya göre hangi gelir unsuruna girer?",
        {
            'A': 'Menkul sermaye iradı',
            'B': 'Zirai kazanç',
            'C': 'Gayrimenkul sermaye iradı',
            'D': 'Arızi kazanç',
            'E': 'Ticari kazanç',
        },
        'C',
        "m. 70'in son fıkrasına göre zirai faaliyete **bilfiil iştirak etmeksizin** sadece üründen pay alan arazi sahiplerinin gelirleri **gayrimenkul sermaye iradı** sayılır. Arazi sahibi faaliyete fiilen katılsaydı elde ettiği gelir zirai kazanç olurdu.",
        '193 sayılı Gelir Vergisi Kanunu m. 70 son fıkra',
    ),
    # düzey 2
    '0032': patch(
        "Vergi değeri 2.000.000 ₺ olan ve yetkili mercilerce takdir veya tespit edilmiş kirası bulunmayan bir daire, sahibinin arkadaşının oturması için bedelsiz olarak tahsis edilmiştir. GVK'ya göre bu daire için dikkate alınacak yıllık emsal kira bedeli kaç ₺'dir?",
        {
            'A': '0',
            'B': '300.000',
            'C': '200.000',
            'D': '150.000',
            'E': '100.000',
        },
        'E',
        "Bina ve arazide emsal kira bedeli, yetkili mercilerce takdir veya tespit edilmiş kira yoksa VUK'a göre belirlenen **vergi değerinin %5'idir** (m. 73): 2.000.000 × %5 = **100.000 ₺**. Diğer mal ve haklarda oran maliyet bedelinin %10'udur; 200.000 ₺ bu oranın binaya uygulanmasıyla bulunur. Arkadaş, emsal kira istisnasındaki yakınlar arasında değildir.",
        '193 sayılı Gelir Vergisi Kanunu m. 73',
    ),
    # düzey 2
    '0033': patch(
        'Kendisine ait daireyi konut olarak kiraya veren ve başka bir şehirde kirada oturan kişi gerçek gider usulünü seçmiştir. Oturduğu konut için ödediği kira hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gider olarak indirilemez',
            'B': 'Yarısı gider olarak indirilebilir',
            'C': 'Kira hasılatından gider olarak indirilebilir',
            'D': 'Gelecek yıla zarar olarak devreder',
            'E': 'Ticari kazançtan indirilebilir',
        },
        'C',
        "m. 74/10'a göre sahibi bulundukları konutları kiraya verenlerin **kira ile oturdukları konutun kira bedeli** gider olarak indirilir. İndirim, gayrisafi hasılattan diğer giderler düşüldükten sonra kalan tutar üzerinden yapılır; indirilemeyen kısım zarar (gider fazlası) sayılmaz.",
        '193 sayılı Gelir Vergisi Kanunu m. 74/10',
    ),
    # düzey 2
    '0034': patch(
        "Tam mükellef bir anonim şirketten 200.000 ₺ brüt kâr payı elde eden ve bu geliri yıllık beyannamesine dâhil etmesi gereken gerçek kişinin beyan edeceği tutar kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '50.000',
            'C': '100.000',
            'D': '150.000',
            'E': '0',
        },
        'C',
        "m. 22/3'e göre tam mükellef kurumlardan elde edilen kâr paylarının **yarısı** gelir vergisinden müstesnadır: 200.000 × %50 = **100.000 ₺** beyan edilir. İstisna edilen tutar üzerinden de tevkifat yapılır ve tevkif edilen verginin **tamamı** yıllık beyanname üzerinden hesaplanan vergiden mahsup edilir.",
        '193 sayılı Gelir Vergisi Kanunu m. 22/3',
    ),
    # düzey 1
    '0035': patch(
        "Mükerrer m. 80 uygulamasında aşağıdakilerden hangisi 'elden çıkarma' sayılmaz?",
        {
            'A': 'Şirkete sermaye konulması',
            'B': 'Trampa edilmesi',
            'C': 'Kamulaştırılması',
            'D': 'Bağışlanması',
            'E': 'Takas edilmesi',
        },
        'D',
        "Mükerrer m. 80'e göre elden çıkarma; satış, bir ivaz karşılığında devir ve temlik, **trampa**, **takas**, **kamulaştırma**, devletleştirme ve **ticaret şirketlerine sermaye olarak konulmayı** ifade eder. Karşılıksız (ivazsız) devir olan bağış elden çıkarma sayılmaz.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 80',
    ),
    # düzey 3
    '0036': patch(
        'Aşağıdaki kişilerden hangisi, diğer şartları taşıdığı varsayımıyla genç girişimcilerde kazanç istisnasından yararlanabilir?',
        {
            'A': 'Babasının ölümüyle işletmeyi devralan 25 yaşındaki kişi',
            'B': 'Mükellefiyet başlangıcında 30 yaşında olan kişi',
            'C': 'Mevcut bir işletmeye sonradan ortak olan 24 yaşındaki kişi',
            'D': 'Amcasının işletmesini devralan 26 yaşındaki kişi',
            'E': 'İşe başlamayı kanuni süreden sonra bildiren 23 yaşındaki kişi',
        },
        'A',
        "Mükerrer m. 20'ye göre istisnadan, ilk defa mükellefiyet tesis olunan ve mükellefiyet başlangıcında **29 yaşını doldurmamış** kişiler yararlanır. İşe başlamanın süresinde bildirilmesi, mevcut işletmeye sonradan ortak olunmaması ve işletmenin eş veya üçüncü dereceye kadar kan veya kayın hısımlarından devralınmamış olması şarttır; **ölüm nedeniyle eş ve çocuklarca devralma** bu yasağın dışındadır. Amca üçüncü derece kan hısmıdır.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 20',
    ),
    # düzey 2
    '0037': patch(
        "Sosyal içerik üreticiliği kazanç istisnasından yararlanabilmek için GVK'ya göre aşağıdakilerden hangisi şarttır?",
        {
            'A': 'İşyeri açılmış olması',
            'B': 'Hasılatın bankada açılan hesaptan tahsili',
            'C': 'Serbest meslek kazanç defteri tutulması',
            'D': 'Başka gelir unsuru elde edilmemesi',
            'E': 'Basit usule tabi olunması',
        },
        'B',
        "Mükerrer m. 20/B'ye göre istisna için Türkiye'de kurulu bir bankada hesap açılması ve bu faaliyetlere ilişkin **tüm hasılatın bu hesap aracılığıyla** tahsil edilmesi şarttır; bankalar aktarılan tutarlardan %15 tevkifat yapar. Başka faaliyetlerden kazanç elde edilmesi istisnaya engel değildir. Kazançları tarifenin dördüncü gelir dilimini aşanlar yararlanamaz.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 20/B',
    ),
    # düzey 2
    '0038': patch(
        "Takvim yılı içinde Türkiye'yi terk eden bir mükellef, GVK'ya göre yıllık beyannamesini ne zaman vermelidir?",
        {
            'A': 'Terkten sonraki 4 ay içinde',
            'B': 'Terkten sonraki 1 ay içinde',
            'C': 'İzleyen yılın Mart ayında',
            'D': 'Terkten önceki 15 gün içinde',
            'E': 'Terkten sonraki 15 gün içinde',
        },
        'D',
        "m. 92'ye göre takvim yılı içinde memleketi terk edenlerin beyannameleri **terke takaddüm eden (terkten önceki) 15 gün** içinde verilir. Ölüm hâlinde ise beyanname ölüm tarihinden itibaren 4 ay içinde verilir. Olağan beyan zamanı izleyen yılın Mart ayının 1-25'idir.",
        '193 sayılı Gelir Vergisi Kanunu m. 92',
    ),
    # düzey 2
    '0039': patch(
        'Geçici vergiye ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Dönemde tevkif edilen vergi geçici vergiden mahsup edilir',
            'B': 'Üçer aylık dönem kazançları üzerinden hesaplanır',
            'C': 'Mahsup edilemeyen tutar talep üzerine iade edilir',
            'D': 'Ücretliler de geçici vergi öder',
            'E': 'Oran tarifenin ilk gelir dilimi oranıdır',
        },
        'D',
        "Mükerrer m. 120'ye göre geçici vergiyi **ticari kazanç sahipleri ile serbest meslek erbabı** öder; ücretliler geçici vergi mükellefi değildir. Geçici vergi üçer aylık dönem kazançları üzerinden tarifenin ilk gelir dilimine uygulanan oranda hesaplanır, aynı dönemde tevkif edilen vergi mahsup edilir ve mahsup edilemeyen tutar yıl sonuna kadar yazılı talep üzerine iade edilir.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 120',
    ),
    # düzey 2
    '0040': patch(
        "Bir anonim şirketin aşağıdaki ödemelerinden hangisinden GVK m. 94'e göre tevkifat yapılmaz?",
        {
            'A': 'Avukata ödenen vekâlet ücreti',
            'B': 'Dar mükellefe patent satış bedeli',
            'C': 'Noterliğe ödenen serbest meslek ücreti',
            'D': 'Gerçek kişiye ödenen işyeri kirası',
            'E': 'Yıllara yaygın inşaat hakedişi',
        },
        'C',
        "m. 94/2 serbest meslek ödemelerinden tevkifat öngörür; ancak **noterlere** serbest meslek faaliyetleri dolayısıyla yapılan ödemeler hariç tutulmuştur. Avukatlık ücreti (m. 94/2), yıllara yaygın inşaat hakedişleri (m. 94/3), m. 70'teki mal ve hakların kira ödemeleri (m. 94/5) ve dar mükelleflere telif ve patent satışı nedeniyle yapılan ödemeler (m. 94/4) tevkifata tabidir.",
        '193 sayılı Gelir Vergisi Kanunu m. 94',
    ),
    # düzey 2
    '0041': patch(
        "Türkiye'de yerleşmiş olmayan bir yabancı mimar, serbest meslek faaliyeti kapsamında proje hizmeti vermektedir. GVK'ya göre bu kazanç hangi durumda Türkiye'de elde edilmiş sayılır?",
        {
            'A': "Mimar Türkiye'de altı aydan fazla kalırsa",
            'B': 'Ödeme yurt dışındaki bir bankadan yapılırsa',
            'C': "Sözleşme Türkiye'de imzalanırsa",
            'D': 'Bedel Türk lirası olarak ödenirse',
            'E': "Faaliyet Türkiye'de icra edilir veya değerlendirilirse",
        },
        'E',
        "Dar mükellefler bakımından serbest meslek kazançları, faaliyetin **Türkiye'de icra edilmesi** veya **Türkiye'de değerlendirilmesi** hâlinde Türkiye'de elde edilmiş sayılır (m. 7/4). Değerlendirme, ödemenin Türkiye'de yapılması ya da yurt dışında yapılmışsa Türkiye'de ödeyenin hesaplarına intikal ettirilmesi veya kârından ayrılmasıdır. Ödemenin para birimi veya sözleşmenin imza yeri ölçüt değildir.",
        '193 sayılı Gelir Vergisi Kanunu m. 7/4',
    ),
    # düzey 2
    '0042': patch(
        "Gayrimenkul ticaretiyle uğraşmayan bir kişi 2023 yılında satın aldığı tarlayı 2025 yılında parsellere ayırmış ve parselleri 2026 yılında satmıştır. Bu satıştan doğan kazanç GVK'ya göre hangi gelir unsuruna girer?",
        {
            'A': 'Ticari kazanç',
            'B': 'Gayrimenkul sermaye iradı',
            'C': 'Zirai kazanç',
            'D': 'Arızi kazanç',
            'E': 'Değer artışı kazancı',
        },
        'A',
        "GVK m. 37/6'ya göre satın alınan veya trampa yoluyla edinilen arazinin iktisap tarihinden itibaren **beş yıl içinde parsellenerek** bu süre içinde veya sonraki yıllarda satılmasından elde edilen kazanç **ticari kazanç** sayılır. Parselleme olmasaydı beş yıl içindeki satış değer artışı kazancı olarak değerlendirilirdi.",
        '193 sayılı Gelir Vergisi Kanunu m. 37/6',
    ),
    # düzey 2
    '0043': patch(
        "İşletme hesabı esasına göre defter tutan bir tacirin hesap dönemindeki hasılatı 900.000 ₺, giderleri 600.000 ₺'dir. Dönem başı emtia mevcudu 100.000 ₺, dönem sonu emtia mevcudu 150.000 ₺'dir. Tacirin ticari kazancı kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '400.000',
            'C': '250.000',
            'D': '350.000',
            'E': '450.000',
        },
        'D',
        'İşletme hesabı esasında kazanç hasılat ile giderler arasındaki farktır; emtia alım satımıyla uğraşanlarda dönem sonu emtia mevcudu **hasılata**, dönem başı mevcudu **giderlere** eklenir (m. 39): (900.000 + 150.000) − (600.000 + 100.000) = **350.000 ₺**. Emtia ters yönde eklenirse 250.000 ₺, hiç dikkate alınmazsa 300.000 ₺ bulunur.',
        '193 sayılı Gelir Vergisi Kanunu m. 39',
    ),
    # düzey 3
    '0044': patch(
        "2025 yılında başlayan bir yol inşaatı Aralık 2027'de fiilen tamamlanmış, geçici kabul tutanağı ise idarece 10 Ocak 2028'de onaylanmıştır. GVK'ya göre bu işin kârı hangi yılın geliri sayılır?",
        {
            'A': '2028',
            'B': '2027',
            'C': 'Hakedişlere göre her yıl',
            'D': '2026',
            'E': '2025',
        },
        'A',
        "Birden fazla takvim yılına yaygın inşaat ve onarım işlerinde kâr veya zarar **işin bittiği yıl** kesin olarak tespit edilir ve tamamı o yılın geliri sayılır (m. 42). Geçici ve kesin kabul usulüne tabi işlerde bitim tarihi, geçici kabul tutanağının **idarece onaylandığı** tarihtir (m. 44). Onay 2028'de olduğundan kâr **2028** yılının gelirine girer.",
        '193 sayılı Gelir Vergisi Kanunu m. 42-44',
    ),
    # düzey 2
    '0045': patch(
        'Birden fazla takvim yılına yaygın inşaat ve onarım işlerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hakediş ödemelerinden tevkifat yapılır',
            'B': 'Kazanç geçici vergi matrahına dâhil edilir',
            'C': 'Her işin hasılat ve giderleri ayrı izlenir',
            'D': 'Dekapaj işleri de inşaat işi sayılır',
            'E': 'Kâr veya zarar işin bittiği yıl tespit edilir',
        },
        'B',
        "Mükerrer m. 120'ye göre 42. madde kapsamındaki kazançlar **geçici vergi matrahına dâhil edilmez**; bu işlerden yapılan tevkifat da geçici vergiden mahsup edilmez. Kâr işin bittiği yıl tespit edilir (m. 42), dekapaj işleri inşaat sayılır, her işin hasılat ve giderleri ayrı defter veya sayfada gösterilir ve hakedişlerden m. 94/3 uyarınca tevkifat yapılır.",
        '193 sayılı Gelir Vergisi Kanunu m. 42, mük. m. 120',
    ),
    # düzey 1
    '0046': patch(
        "Kazancı basit usulde tespit edilen bir mükellefin GVK m. 46'ya göre hesaplanan ticari kazancı hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tarifeye göre vergilendirilir',
            'B': 'Geçici vergiye tabidir',
            'C': 'Gelir vergisinden istisnadır',
            'D': 'Yarısı vergilendirilir',
            'E': 'Götürü olarak vergilendirilir',
        },
        'C',
        "7338 sayılı Kanunla eklenen mükerrer m. 20/A uyarınca kazançları basit usulde tespit olunan mükelleflerin m. 46'ya göre tespit edilen kazançları **gelir vergisinden müstesnadır**. Basit usul mükellefleri geçici vergi de ödemez; geçici vergi ticari kazanç sahipleri ile serbest meslek erbabının gerçek usuldeki kazançlarına ilişkindir.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 20/A',
    ),
    # düzey 2
    '0047': patch(
        'Zirai kazancın vergilendirilmesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşletme büyüklüğünde yarıcılık ortaklık sayılır',
            'B': 'Gerçek usule tabi olmayan çiftçi yıllık beyanname verir',
            'C': 'Aşım için erkek damızlık beslemek zirai faaliyettir',
            'D': 'Kazanç kural olarak hasılattan tevkifatla vergilenir',
            'E': 'Bilanço esasını seçen çiftçi iki yıl bu usulden dönemez',
        },
        'B',
        "m. 53'e göre kazançları gerçek usulde vergilendirilmeyen çiftçiler **beyanname vermez**; vergileri hasılatları üzerinden tevkif yoluyla alınır. Aşım yaptırmak amacıyla erkek damızlık beslenmesi zirai faaliyettir (m. 52), yarıcılık ortaklık sayılır (m. 53) ve bilanço esasını kabul eden çiftçi iki yıl geçmedikçe bu usulden dönemez (m. 59).",
        '193 sayılı Gelir Vergisi Kanunu m. 52-53, 59',
    ),
    # düzey 3
    '0048': patch(
        "Bir işçinin aylık brüt ücreti 100.000 ₺'dir. Bu ay ücretinden 15.000 ₺ SGK işçi payı ve işsizlik sigortası primi kesilmiş, işçi 1.000 ₺ sendika aidatı ve kendisi için 20.000 ₺ şahıs sağlık sigortası primi ödemiştir. Başka indirim yoksa ücretin gerçek safi değeri kaç ₺'dir?",
        {
            'A': '85.000',
            'B': '70.000',
            'C': '64.000',
            'D': '84.000',
            'E': '69.000',
        },
        'E',
        "m. 63'e göre ücretin gerçek safi değeri, sosyal güvenlik primleri (m. 63/2), belgelenen sendika aidatı (m. 63/4) ve şahıs sigortası primleri (m. 63/3) indirilerek bulunur. Ancak şahıs sigortası primlerinin indirimi, ödendiği ayda elde edilen ücretin **%15'i** ile sınırlıdır: 100.000 × %15 = 15.000 ₺. Gerçek safi değer 100.000 − 15.000 − 1.000 − 15.000 = **69.000 ₺**. Primin tamamı indirilirse 64.000 ₺ bulunur.",
        '193 sayılı Gelir Vergisi Kanunu m. 63',
    ),
    # düzey 2
    '0049': patch(
        'Bir avukat, müvekkilinden dava harcı ve bilirkişi ücreti için para almış ve bu paranın tamamını bu amaçlarla harcamıştır. Alınan para serbest meslek kazancının tespitinde nasıl dikkate alınır?',
        {
            'A': 'Yarısı kazanç sayılır',
            'B': 'Hasılata eklenir',
            'C': 'Kazanç sayılmaz',
            'D': 'Arızi kazanç olarak beyan edilir',
            'E': 'Ertesi yılın hasılatı sayılır',
        },
        'C',
        "m. 67'ye göre vergi, resim, harç, keşif, şahitlik, bilirkişilik ve ekspertiz gibi hususlara harcanmak üzere müşteri veya müvekkilden alınan ve **tamamen bu hususlara sarf edilen** para ve ayınlar kazanç sayılmaz. Buna karşılık faaliyetle ilgili olarak alınan diğer gider karşılıkları kazanca eklenir.",
        '193 sayılı Gelir Vergisi Kanunu m. 67',
    ),
    # düzey 2
    '0050': patch(
        'Bir yazar, yeni romanının yayın hakkını bir yayınevine devretmiştir. Yazarın bu kapsamdaki kazançları tarifenin dördüncü gelir dilimi tutarını aşmamaktadır. Bu hasılat hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İstisnadır; tevkifat da yapılmaz',
            'B': 'Ticari kazanç olarak vergilenir',
            'C': 'Ücret olarak vergilenir',
            'D': 'Arızi kazanç olarak beyan edilir',
            'E': 'İstisnadır; ancak tevkifat yapılır',
        },
        'E',
        "m. 18'e göre müelliflerin eserlerini satmak veya üzerindeki haklarını devretmek suretiyle elde ettikleri hasılat **gelir vergisinden müstesnadır**. Ancak bu istisnanın m. 94 uyarınca yapılacak **tevkifata şümulü yoktur**; yayınevi ödemeden tevkifat yapar. Bu kapsamdaki kazançları tarifenin dördüncü gelir dilimini aşanlar ise istisnadan yararlanamaz.",
        '193 sayılı Gelir Vergisi Kanunu m. 18',
    ),
    # düzey 3
    '0051': patch(
        "Bir kişi, işletmesine dâhil olmayan dükkânını 2026 yılında aylık 40.000 ₺ brüt kira ile kiraya vermiş ve 12 aylık kirayı tahsil etmiştir. Kiracı ödemelerden %20 oranında tevkifat yapmıştır. Mükellef götürü gider usulünü seçmiştir. Beyan edilecek safi irat kaç ₺'dir?",
        {
            'A': '384.000',
            'B': '72.000',
            'C': '408.000',
            'D': '480.000',
            'E': '326.400',
        },
        'C',
        "Gayrisafi hasılat tahsil edilen brüt kiradır: 40.000 × 12 = 480.000 ₺. Götürü gider usulünde hasılatın **%15'i** indirilir (m. 74): 480.000 × %15 = 72.000 ₺; safi irat **408.000 ₺**. Tevkif edilen 96.000 ₺ matrahı azaltmaz, beyanname üzerinden hesaplanan vergiden mahsup edilir. 384.000 ₺ tevkifatın hasılattan düşülmesiyle bulunur.",
        '193 sayılı Gelir Vergisi Kanunu m. 72, 74',
    ),
    # düzey 2
    '0052': patch(
        'Gayrimenkul sermaye iradında götürü gider usulüne ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Usulü seçen iki yıl geçmedikçe usulden dönemez',
            'B': 'Hakları kiraya verenler de bu usulü seçebilir',
            'C': "Hasılatın %15'i götürü gider olarak indirilir",
            'D': 'Usulün seçimi mükellefin tercihine bağlıdır',
            'E': 'Bu usulde gerçek giderler ayrıca indirilmez',
        },
        'B',
        "m. 74'e göre mükellefler, **hakları kiraya verenler hariç**, gerçek giderlere karşılık olmak üzere hasılatlarının %15'ini götürü olarak indirebilir. Götürü gider seçimi isteğe bağlıdır; seçildiğinde gerçek giderler ayrıca indirilmez ve bu usulü kabul edenler **iki yıl** geçmedikçe usulden dönemez.",
        '193 sayılı Gelir Vergisi Kanunu m. 74',
    ),
    # düzey 2
    '0053': patch(
        "Adi komandit şirketin komanditer ortağına dağıtılan kâr payı GVK'ya göre hangi gelir unsuruna girer?",
        {
            'A': 'Menkul sermaye iradı',
            'B': 'Arızi kazanç',
            'C': 'Değer artışı kazancı',
            'D': 'Ücret',
            'E': 'Ticari kazanç',
        },
        'A',
        "m. 75/2'ye göre iştirak hisselerinden doğan kazançlar menkul sermaye iradıdır; limited şirket ortaklarının, iş ortaklığı ortaklarının ve **komanditerlerin** kâr payları bu gruba dâhildir. Adi komandit şirkette komanditerin kâr payı, şirket kârının ilişkin olduğu takvim yılında elde edilmiş sayılır. Komandite ortağın payı ise şahsi ticari kazanç hükmündedir (m. 37).",
        '193 sayılı Gelir Vergisi Kanunu m. 75/2',
    ),
    # düzey 2
    '0054': patch(
        'Menkul sermaye iradının safi tutarı bulunurken aşağıdaki giderlerden hangisi indirilemez?',
        {
            'A': 'Temettülerin tahsil gideri',
            'B': 'Şirket genel kuruluna katılım gideri',
            'C': 'Menkul kıymetlerin sigorta ücreti',
            'D': 'Menkul kıymet için ödenen harç',
            'E': 'Menkul kıymetlerin saklama ücreti',
        },
        'B',
        "m. 78'e göre menkul kıymetlerin muhafazası için yapılan depo ve sigorta giderleri, temettü ve faizlerin tahsil giderleri ile menkul kıymetler için ödenen vergi, resim ve harçlar indirilir. Ancak **şirket toplantılarına bizzat veya vekâleten katılma** gibi sermayenin idaresi için yapılan giderler irattan indirilmez.",
        '193 sayılı Gelir Vergisi Kanunu m. 78',
    ),
    # düzey 3
    '0055': patch(
        "Bir kişi Mart 2023'te 2.000.000 ₺'ye satın aldığı konutu Haziran 2026'da 5.000.000 ₺'ye satmış, kendi üstlendiği 100.000 ₺ tapu harcını ödemiştir. Endekslemede kullanılacak Yİ-ÜFE iktisap için 1.000, elden çıkarma için 2.200'dür. İstisna düşülmeden önceki safi değer artışı kazancı kaç ₺'dir?",
        {
            'A': '2.900.000',
            'B': '2.200.000',
            'C': '500.000',
            'D': '600.000',
            'E': '3.000.000',
        },
        'C',
        'Endeks artışı %120 olup %10 şartını sağladığından iktisap bedeli endekslenir: 2.000.000 × 2.200 / 1.000 = 4.400.000 ₺. Safi kazanç, satış bedelinden endekslenmiş maliyet ile satıcının üstlendiği gider ve harçlar düşülerek bulunur: 5.000.000 − 4.400.000 − 100.000 = **500.000 ₺**. Endeksleme yapılmazsa 2.900.000 ₺, harç düşülmezse 600.000 ₺ bulunur.',
        '193 sayılı Gelir Vergisi Kanunu mük. m. 81',
    ),
    # düzey 1
    '0056': patch(
        'Özel kreş ve gündüz bakımevleri ile özel okulların işletilmesinden elde edilen kazançlar, faaliyete geçilen dönemden başlayarak kaç vergilendirme dönemi gelir vergisinden istisnadır?',
        {
            'A': '4',
            'B': '10',
            'C': '2',
            'D': '5',
            'E': '3',
        },
        'D',
        "m. 20'ye göre özel kreş ve gündüz bakımevleri ile okul öncesi eğitim, ilköğretim, özel eğitim ve ortaöğretim özel okullarının işletilmesinden elde edilen kazançlar **beş vergilendirme dönemi** gelir vergisinden müstesnadır; istisna faaliyete geçilen dönemden itibaren başlar. Genç girişimci istisnası ise üç dönemdir.",
        '193 sayılı Gelir Vergisi Kanunu m. 20',
    ),
    # düzey 2
    '0057': patch(
        '7582 sayılı Kanunla eklenen yurt dışından elde edilen kazanç ve iratlar istisnasına (mükerrer m. 20/D) ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Şartlar taşınmıyorsa alınmayan vergi ziyaa uğramış sayılır',
            'B': 'İstisnaya ilişkin giderler vergiye tabi kazançtan düşülmez',
            'C': "Yurt dışında ödenen vergiler Türkiye'de mahsup edilir",
            'D': 'İstisna kapsamındaki kazançlar beyannameye dâhil edilmez',
            'E': "Önceden Türkiye'deki kira nedeniyle mükellefiyet engel değildir",
        },
        'C',
        "Mükerrer m. 20/D'ye göre istisna kapsamındaki kazançlar için beyanname verilmez, başka gelir nedeniyle verilse de beyannameye dâhil edilmez; bu kazançlara ilişkin gider ve maliyetler vergiye tabi kazançta dikkate alınmaz. Türkiye'de daha önce GMSİ, MSİ veya değer artışı nedeniyle mükellefiyet bulunması engel değildir. İstisna kapsamındaki kazançlar için yabancı ülkelerde ödenen vergiler **Türkiye'de mahsup edilemez**.",
        '193 sayılı Gelir Vergisi Kanunu mük. m. 20/D',
    ),
    # düzey 2
    '0058': patch(
        "GVK'ya göre aşağıdaki gelirlerden hangisi için yıllık beyanname verilmesi gerekir?",
        {
            'A': 'İstisna haddi içinde kalan konut kira geliri',
            'B': 'Dar mükellefin tevkifata tabi mevduat faizi',
            'C': 'Gerçek usule tabi olmayan çiftçinin zirai kazancı',
            'D': 'Tek işverenden alınan tevkifatlı düşük tutarlı ücret',
            'E': 'İşletme hesabı esasındaki tacirin ticari kazancı',
        },
        'E',
        "m. 85'e göre tacirler, çiftçiler ve serbest meslek erbabı kazanç elde etmeseler bile yıllık beyanname verir. m. 86 ise gerçek usulde vergilendirilmeyen zirai kazançları, tek işverenden alınan ve dördüncü gelir dilimini aşmayan tevkifatlı ücretleri, istisna hadleri içinde kalan kazanç ve iratları ve dar mükelleflerin tamamı tevkif yoluyla vergilendirilmiş gelirlerini beyan dışında bırakır.",
        '193 sayılı Gelir Vergisi Kanunu m. 85-86',
    ),
    # düzey 2
    '0059': patch(
        "Beyan edilen geliri 400.000 ₺ olan bir mükellef, kendisi ve çocukları için Türkiye'de belgeli olarak 60.000 ₺ eğitim ve sağlık harcaması yapmıştır. Beyannamede indirilebilecek tutar kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '0',
            'C': '40.000',
            'D': '30.000',
            'E': '60.000',
        },
        'C',
        "m. 89/2'ye göre mükellefin kendisi, eşi ve küçük çocuklarına ilişkin eğitim ve sağlık harcamaları, Türkiye'de yapılması ve gelir veya kurumlar vergisi mükelleflerinden alınan belgelerle tevsiki şartıyla, beyan edilen gelirin **%10'unu** aşmamak üzere indirilir: 400.000 × %10 = **40.000 ₺**.",
        '193 sayılı Gelir Vergisi Kanunu m. 89/2',
    ),
    # düzey 3
    '0060': patch(
        "Bir şirket, serbest meslek erbabına net 85.000 ₺ ödemeyi ve tevkif edilecek vergiyi kendisi üstlenmeyi kabul etmiştir. Tevkifat oranı %20 ise şirketin tevkif edip beyan edeceği vergi kaç ₺'dir?",
        {
            'A': '106.250',
            'B': '12.750',
            'C': '20.000',
            'D': '21.250',
            'E': '17.000',
        },
        'D',
        "m. 96'ya göre ücret dışındaki ödemelerde tevkifat **gayrisafi tutar** üzerinden yapılır; vergiyi ödeyen üstlenirse vergi, fiilen ödenen tutar ile üstlenilen verginin toplamı üzerinden hesaplanır. Brüt tutar 85.000 / (1 − 0,20) = 106.250 ₺, vergi 106.250 × %20 = **21.250 ₺**. 17.000 ₺, oranın net tutara uygulanmasıyla bulunur.",
        '193 sayılı Gelir Vergisi Kanunu m. 96',
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
    print(f"1 paket / {len(PATCHES)} soru ('Gelir Vergisi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
