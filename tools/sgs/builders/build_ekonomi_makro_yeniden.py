#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Makroekonomi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiline gore yeniden yazim: milli gelir hesaplari, issizlik, enflasyon, Keynesyen model ve carpanlar, IS-LM, AD-AS ve makro okullar, tuketim ve yatirim teorileri, Solow ve buyume. 18 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Makroekonomi teorisi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ekonomi/makroekonomi.json"
STYLE_REF = 'SGS Ekonomi (gercek sinav profiline kalibre: hesap + kisa sik)'
ONEK = "eko-makro-gen-"


def patch(stem, options, answer, solution, ref='Makroekonomi teorisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir ülkenin gayrisafi yurt içi hasılası 1.000 milyar ₺'dir. Ülke yerleşiklerinin yurt dışından elde ettiği faktör gelirleri 60 milyar ₺, yabancıların bu ülkede elde edip kendi ülkelerine aktardığı faktör gelirleri 90 milyar ₺'dir. Gayrisafi milli hasıla kaç milyar ₺'dir?",
        {
            'A': '1.150',
            'B': '1.000',
            'C': '1.030',
            'D': '910',
            'E': '970',
        },
        'E',
        "GSMH = GSYH + yurt dışından elde edilen faktör gelirleri − yurt dışına ödenen faktör gelirleri = 1.000 + 60 − 90 = **970**. Net dış faktör geliri negatif olduğu için GSMH, GSYH'nin altında kalır. 1.030 ise işaretlerin ters alınmasının sonucudur.",
        'Makroekonomi: GSYH ve GSMH',
    ),
    # düzey 3
    '0002': patch(
        'Açık bir ekonomide özel yatırımlar 200, kamu harcamaları 300, vergiler 250 ve net ihracat −30 birimdir. Milli gelir özdeşliğine göre özel kesim tasarrufu kaç birimdir?',
        {
            'A': '220',
            'B': '280',
            'C': '250',
            'D': '170',
            'E': '150',
        },
        'A',
        'Y = C + I + G + NX ve özel tasarruf S = Y − T − C olduğundan S = I + (G − T) + NX olur. S = 200 + (300 − 250) + (−30) = **220**. Özel tasarruf yatırımları, bütçe açığını (50) ve dış fazlayı finanse eder; dış açık (−30) ise yurt dışı tasarrufun kullanıldığını gösterir.',
        'Makroekonomi: milli gelir özdeşliği',
    ),
    # düzey 2
    '0003': patch(
        'Talebin geçici olarak daraldığı bir resesyon döneminde bir otomobil fabrikasının üretimi azaltıp işçilerinin bir kısmını işten çıkarmasıyla ortaya çıkan işsizlik türü hangisidir?',
        {
            'A': 'Yapısal işsizlik',
            'B': 'Gizli işsizlik',
            'C': 'Konjonktürel (devrevi) işsizlik',
            'D': 'Mevsimsel işsizlik',
            'E': 'Friksiyonel işsizlik',
        },
        'C',
        'Toplam talebin konjonktür dalgalanmasına bağlı olarak düşmesinden kaynaklanan işsizlik **konjonktürel (devrevi)** işsizliktir; ekonomi toparlandığında azalır. Yapısal işsizlik teknoloji veya üretim yapısındaki kalıcı değişimlerden, friksiyonel işsizlik iş arama sürecinden kaynaklanır.',
        'Makroekonomi: işsizlik türleri',
    ),
    # düzey 1
    '0004': patch(
        'Bir tarım işletmesinde çalışan aile bireylerinden bazıları işten ayrıldığında toplam üretimin değişmediği durumda görülen işsizlik türü hangisidir?',
        {
            'A': 'Yapısal işsizlik',
            'B': 'Konjonktürel işsizlik',
            'C': 'Friksiyonel işsizlik',
            'D': 'Gizli işsizlik',
            'E': 'Mevsimsel işsizlik',
        },
        'D',
        '**Gizli işsizlikte** kişiler çalışıyor görünür, ancak marjinal verimlilikleri sıfıra yakındır; işten ayrılmaları toplam üretimi azaltmaz. Az gelişmiş ekonomilerin tarım kesiminde sık görülür.',
        'Makroekonomi: gizli işsizlik',
    ),
    # düzey 2
    '0005': patch(
        'Petrol fiyatlarındaki ani ve büyük artışın hem genel fiyat düzeyini yükseltip hem de üretim ve istihdamı düşürmesi aşağıdakilerden hangisiyle açıklanır?',
        {
            'A': 'Dezenflasyon sonucunda büyüme',
            'B': 'Talep enflasyonu sonucunda aşırı ısınma',
            'C': 'Maliyet enflasyonu sonucunda stagflasyon',
            'D': 'Parasal genişleme sonucunda hiperenflasyon',
            'E': 'Deflasyon sonucunda resesyon',
        },
        'C',
        'Enerji gibi temel bir girdinin fiyat artışı **toplam arzı sola kaydırır**: fiyatlar yükselirken üretim ve istihdam düşer. Bu **maliyet enflasyonu**, durgunlukla birlikte görülen enflasyon olan **stagflasyona** yol açar. Talep enflasyonunda ise fiyat ve üretim birlikte artar.',
        'Makroekonomi: enflasyon türleri',
    ),
    # düzey 3
    '0006': patch(
        'Marjinal tüketim eğilimi 0,8, gelir vergisi oranı %25 ve marjinal ithalat eğilimi 0,1 olan açık bir ekonomide kamu harcamaları 50 birim artırılırsa denge gelir kaç birim artar?',
        {
            'A': '100',
            'B': '250',
            'C': '200',
            'D': '50',
            'E': '125',
        },
        'A',
        'Vergi oranı ve ithalatın bulunduğu modelde çarpan = 1 / [1 − c(1 − t) + m] = 1 / [1 − 0,8 × 0,75 + 0,1] = 1 / 0,5 = 2. ΔY = 2 × 50 = **100**. 250 basit çarpanın (1 / 0,2 = 5) vergi ve ithalat sızıntıları dikkate alınmadan kullanılmasının sonucudur.',
        'Makroekonomi: çarpan',
    ),
    # düzey 2
    '0007': patch(
        'Tam istihdam gelirinin 2.000, denge gelirin 1.500 olduğu ve harcama çarpanının 4 olduğu bir ekonomide tam istihdama ulaşmak için otonom harcamaların ne kadar artırılması gerekir?',
        {
            'A': '2.000',
            'B': '4',
            'C': '375',
            'D': '125',
            'E': '500',
        },
        'D',
        "Gelir açığı 2.000 − 1.500 = 500'dür. Çarpan 4 olduğundan gereken harcama artışı 500 / 4 = **125**'tir; bu tutar **deflasyonist açık** olarak adlandırılır. 500, harcama değil gelir açığıdır.",
        'Makroekonomi: deflasyonist açık',
    ),
    # düzey 2
    '0008': patch(
        'IS-LM modelinde eğrilerin eğimine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatırımların faize duyarlılığı arttıkça IS eğrisi yatıklaşır.\n\nII. Para talebinin faize duyarlılığı arttıkça LM eğrisi dikleşir.\n\nIII. Çarpanın büyümesi IS eğrisini dikleştirir.',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'B',
        'Faiz duyarlılığı yüksek yatırımlar, faizdeki küçük bir değişmeyle geliri çok değiştirir ve IS eğrisini **yatıklaştırır** (I doğru). Çarpan büyüdükçe aynı yatırım değişmesi daha büyük gelir değişmesi yaratır; IS yine **yatıklaşır**, dikleşmez (III yanlış). Para talebinin faize duyarlılığı arttıkça LM eğrisi **yatıklaşır** (II yanlış); duyarlılık sıfıra yaklaştıkça LM dikeyleşir.',
        'Makroekonomi: IS-LM eğimleri',
    ),
    # düzey 2
    '0009': patch(
        'LM eğrisinin dikey olduğu klasik durumda genişletici maliye politikasının sonucu aşağıdakilerden hangisidir?',
        {
            'A': 'Faiz düşer, gelir artar',
            'B': 'Gelir ve faiz birlikte artar',
            'C': 'Gelir artar, fiyatlar düşer',
            'D': 'Gelir artar, faiz değişmez',
            'E': 'Faiz yükselir, gelir değişmez; tam dışlama gerçekleşir',
        },
        'E',
        'LM dikeyken para talebi faize duyarsızdır ve reel para arzı yalnız belirli bir gelir düzeyiyle uyumludur. IS sağa kaydığında faiz yükselir, ancak artan faiz özel yatırımı kamu harcaması artışı kadar azaltır: **tam dışlama**; gelir değişmez.',
        'Makroekonomi: klasik durum',
    ),
    # düzey 2
    '0010': patch(
        'IS eğrisi üzerindeki her noktaya ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mal piyasası dengededir; planlanan harcama gelire eşittir',
            'B': 'Hem mal hem para piyasası dengededir',
            'C': 'Para piyasası dengededir; para arzı para talebine eşittir',
            'D': 'Dış denge sağlanmıştır; cari işlemler dengesi sıfırdır',
            'E': 'Emek piyasası tam istihdam dengesindedir',
        },
        'A',
        "IS eğrisi, **mal piyasasının** dengede olduğu (planlanan harcama = gelir, yatırım = tasarruf) faiz-gelir bileşimlerini gösterir. Para piyasası dengesi LM eğrisidir; iki piyasanın birlikte dengesi IS ile LM'nin kesiştiği tek noktadadır.",
        'Makroekonomi: IS eğrisi',
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdaki makro okullar–bekleyiş varsayımı eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': 'Yeni Keynesyen okul – Ücret ve fiyat katılıkları',
            'B': 'Yeni Keynesyen okul – Rasyonel bekleyişler',
            'C': 'Parasalcı okul – Uyarlayıcı bekleyişler',
            'D': 'Yeni Klasik okul – Piyasaların sürekli temizlenmesi',
            'E': 'Yeni Klasik okul – Uyarlayıcı bekleyişler',
        },
        'E',
        '**Yeni Klasik okul** rasyonel bekleyişler ve piyasaların sürekli temizlenmesi varsayımlarına dayanır; uyarlayıcı bekleyişler **parasalcılara** aittir. Yeni Keynesyenler rasyonel bekleyişleri kabul eder, ancak menü maliyetleri ve sözleşmeler nedeniyle ücret-fiyat katılıklarını modele katar.',
        'Makroekonomi: makro okullar',
    ),
    # düzey 1
    '0012': patch(
        'Konjonktür dalgalanmalarını esas olarak teknoloji ve verimlilik şoklarıyla açıklayan, dalgalanmaları piyasa başarısızlığı değil optimal tepki olarak gören yaklaşım hangisidir?',
        {
            'A': 'Yeni Keynesyen teori',
            'B': 'Reel konjonktür teorisi',
            'C': 'Politik konjonktür teorisi',
            'D': 'Parasalcı teori',
            'E': 'Keynesyen teori',
        },
        'B',
        '**Reel konjonktür teorisi** (Kydland-Prescott), dalgalanmaların kaynağını teknoloji ve verimlilik gibi **reel** şoklarda görür; hanehalkı ve firmaların bu şoklara verdiği optimal tepkiler dalgalanmayı oluşturur. Politik konjonktür teorisi ise seçim takvimine bağlı politika değişikliklerini esas alır.',
        'Makroekonomi: reel konjonktür teorisi',
    ),
    # düzey 3
    '0013': patch(
        "Modigliani'nin yaşam boyu gelir hipotezine göre 40 yıl çalışıp her yıl 60.000 ₺ kazanacak, başlangıç serveti olmayan ve toplam 60 yıl daha yaşayacağını bekleyen bir birey tüketimini eşit dağıtmak istemektedir. Faiz sıfır ise çalışma yıllarındaki yıllık tasarrufu kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '40.000',
            'C': '0',
            'D': '60.000',
            'E': '30.000',
        },
        'A',
        "Yaşam boyu toplam gelir 40 × 60.000 = 2.400.000 ₺'dir; bunu 60 yıla eşit dağıtan birey yılda 2.400.000 / 60 = 40.000 ₺ tüketir. Çalışma yıllarında yıllık tasarruf 60.000 − 40.000 = **20.000 ₺**'dir; bu birikim emeklilikteki 20 yılın tüketimini finanse eder. 40.000 ₺ tasarruf değil yıllık tüketimdir.",
        'Makroekonomi: yaşam boyu gelir hipotezi',
    ),
    # düzey 2
    '0014': patch(
        "Tobin'in q oranına ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'q, firmanın piyasa değerinin sermayesinin yenileme maliyetine oranıdır',
            'B': 'q > 1 olduğunda yatırımların artması beklenir',
            'C': 'q < 1 olduğunda yeni yatırım yapmak mevcut firmaları satın almaktan kârlıdır',
            'D': 'q oranı yatırım kararını geleceğe ilişkin beklentilerle ilişkilendirir',
            'E': 'Hisse senedi fiyatlarının yükselmesi q oranını artırır',
        },
        'C',
        'Tobin q, piyasa değerinin sermayenin yenileme maliyetine oranıdır. q > 1 ise yeni sermaye kurmak piyasada değer yaratır ve yatırım artar; hisse fiyatları beklentileri yansıttığı için q yatırımı beklentilere bağlar. **q < 1** olduğunda ise mevcut firmaları (varlıkları) satın almak yeni yatırımdan **daha ucuzdur**; yeni yatırım cazip değildir.',
        "Makroekonomi: Tobin'in q oranı",
    ),
    # düzey 1
    '0015': patch(
        "Kişi başı reel gelirin yıllık %3,5 büyüdüğü bir ülkede '70 kuralına' göre kişi başı gelir yaklaşık kaç yılda iki katına çıkar?",
        {
            'A': '35',
            'B': '20',
            'C': '70',
            'D': '24,5',
            'E': '10',
        },
        'B',
        '**70 kuralına** göre bir büyüklüğün iki katına çıkma süresi yaklaşık 70 / büyüme oranı kadardır: 70 / 3,5 = **20** yıl. Kural bileşik büyümenin yaklaşık hesabıdır.',
        'Makroekonomi: 70 kuralı',
    ),
    # düzey 2
    '0016': patch(
        'Diğer koşullar benzerken kişi başı sermayesi düşük olan ülkelerin, sermayenin azalan marjinal verimi nedeniyle zengin ülkelerden daha hızlı büyüyerek onlara yaklaşacağını öngören görüş hangisidir?',
        {
            'A': 'Tasarruf paradoksu',
            'B': 'Ricardo denkliği',
            'C': 'Kuznets hipotezi',
            'D': "Kaldor'un stilize gerçekleri",
            'E': 'Koşullu yakınsama hipotezi',
        },
        'E',
        "**Yakınsama hipotezi** Solow modelinden türetilir: kişi başı sermayesi düşük ekonomilerde sermayenin marjinal verimi yüksek olduğu için büyüme hızlıdır. 'Koşullu' ifadesi, yakınsamanın tasarruf oranı ve nüfus artışı gibi temel özellikleri benzer ülkeler arasında beklendiğini gösterir.",
        'Makroekonomi: yakınsama hipotezi',
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdakilerden hangileri talep enflasyonunun nedenleri arasında yer alır?\n\nI. Para arzının üretimden hızlı artması\n\nII. Kamu harcamalarının hızla artırılması\n\nIII. Ücretlerin verimlilikten hızlı artması\n\nIV. Tüketici güveninin artmasıyla harcamaların yükselmesi',
        {
            'A': 'I, II, III ve IV',
            'B': 'I, II ve III',
            'C': 'I, II ve IV',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'C',
        'Para arzının genişlemesi (I), kamu harcamalarının artması (II) ve özel harcamaların yükselmesi (IV) **toplam talebi** artırarak talep enflasyonuna yol açar. Ücretlerin verimlilikten hızlı artması (III) ise üretim maliyetlerini yükselterek **maliyet enflasyonuna** neden olur.',
        'Makroekonomi: enflasyon ve işsizlik',
    ),
    # düzey 2
    '0018': patch(
        'Bir merkez bankasının düşük enflasyon hedefini açıklayıp kamuoyu beklentilerini buna göre şekillendirdikten sonra işsizliği azaltmak için sürpriz bir genişlemeye yönelme eğilimi hangi sorunla ifade edilir?',
        {
            'A': 'Zaman tutarsızlığı',
            'B': 'Likidite tuzağı',
            'C': 'Dışlama etkisi',
            'D': 'Tasarruf paradoksu',
            'E': 'Lucas eleştirisi',
        },
        'A',
        '**Zaman tutarsızlığında** bugün açıklanan optimal politika, beklentiler oluştuktan sonra politika yapıcı açısından artık optimal değildir; sapma teşviki olduğunu bilen kamuoyu açıklamaya güvenmez. Bu sorun, bağımsız merkez bankası ve kurallı politika gerekçelerinden biridir.',
        'Makroekonomi: zaman tutarsızlığı',
    ),
    # düzey 2
    '0019': patch(
        'Keynesyen yaklaşımda yatırım kararını belirleyen iki temel değişken aşağıdakilerden hangisidir?',
        {
            'A': 'Beklenen enflasyon oranı ile nominal ücret düzeyi',
            'B': 'Sermayenin marjinal etkinliği ile faiz oranı',
            'C': 'Döviz kuru ile ithalat eğilimi',
            'D': 'Marjinal tüketim eğilimi ile vergi oranı',
            'E': 'Para arzı ile dolaşım hızı',
        },
        'B',
        "Keynes'e göre firmalar bir yatırımın beklenen getirisini gösteren **sermayenin marjinal etkinliğini** faiz oranıyla karşılaştırır; beklenen getiri faizin üzerindeyse yatırım yapılır. Bu nedenle faiz düştükçe veya beklentiler iyileştikçe yatırımlar artar.",
        'Makroekonomi: yatırım ve faiz',
    ),
    # düzey 2
    '0020': patch(
        'Klasik modelde paranın yansızlığı ilkesine göre para arzının iki katına çıkmasının sonucu aşağıdakilerden hangisidir?',
        {
            'A': 'Fiyatlar ve nominal ücretler iki katına çıkar; reel değişkenler değişmez',
            'B': 'Faiz oranı yarıya iner, yatırım artar',
            'C': 'Reel ücretler iki katına çıkar',
            'D': 'Reel hasıla iki katına çıkar, fiyatlar değişmez',
            'E': 'İstihdam artar, fiyatlar sabit kalır',
        },
        'A',
        '**Paranın yansızlığı** ilkesine göre para miktarındaki değişme yalnız nominal değişkenleri (fiyat düzeyi, nominal ücret) etkiler; reel hasıla, istihdam, reel ücret ve reel faiz gibi reel değişkenler reel faktörlerle belirlenir. Para arzı iki katına çıkınca fiyatlar ve nominal ücretler de iki katına çıkar.',
        'Makroekonomi: klasik model',
    ),
    # düzey 2
    '0021': patch(
        "Bir çiftçi ürettiği buğdayı (girdisi olmadan) değirmene 100 ₺'ye, değirmen buğdaydan ürettiği unu fırına 250 ₺'ye, fırın da unla ürettiği ekmeği tüketicilere 400 ₺'ye satmıştır. Bu üretim zincirinin GSYH'ye katkısı kaç ₺'dir?",
        {
            'A': '400',
            'B': '650',
            'C': '250',
            'D': '750',
            'E': '150',
        },
        'A',
        "GSYH'ye yalnız **nihai** mallar dahil edilir; aynı sonuca her aşamanın **katma değeri** toplanarak da ulaşılır: 100 (çiftçi) + 150 (değirmen) + 150 (fırın) = **400**, yani nihai malın değeri. Bütün satışların toplamı (750) ara malları birden çok kez sayar (mükerrer sayım).",
        'Makroekonomi: katma değer yöntemi',
    ),
    # düzey 2
    '0022': patch(
        "Aşağıdakilerden hangileri bir ülkenin cari yıl GSYH'sine dahil edilir?\n\nI. Yıl içinde üretilip satılamayan ve stoklara eklenen mallar\n\nII. Bir yatırımcının borsadan satın aldığı hisse senetleri\n\nIII. Emeklilere ödenen aylıklar\n\nIV. Kendi konutunda oturan ev sahibinin konutu için tahmin edilen kira değeri",
        {
            'A': 'I ve II',
            'B': 'I, II, III ve IV',
            'C': 'I, III ve IV',
            'D': 'II ve III',
            'E': 'I ve IV',
        },
        'E',
        "Yıl içinde üretilip stoğa eklenen mallar **stok yatırımı** olarak (I), ev sahibinin kendi konutunun tahmini kira değeri ise konut hizmeti üretimi olarak (IV) GSYH'ye dahil edilir. Hisse senedi alımı mülkiyetin el değiştirdiği finansal bir işlemdir, üretim değildir (II); emekli aylıkları karşılığında üretim yapılmayan **transfer** ödemeleridir (III).",
        'Makroekonomi: GSYH kapsamı',
    ),
    # düzey 3
    '0023': patch(
        'İşgücü 200 bin kişi olan bir ekonomide 6 bin friksiyonel, 8 bin yapısal ve 10 bin konjonktürel işsiz vardır. Doğal işsizlik oranı ve fiilî işsizlik oranı sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': '%9 ve %12',
            'B': '%12 ve %7',
            'C': '%7 ve %12',
            'D': '%5 ve %12',
            'E': '%7 ve %5',
        },
        'C',
        '**Doğal işsizlik** friksiyonel ve yapısal işsizliğin toplamıdır: (6 + 8) / 200 = **%7**. Fiilî işsizlik bunlara konjonktürel işsizliğin eklenmesiyle bulunur: 24 / 200 = **%12**. Konjonktürel işsizlik (%5), ekonomi potansiyel düzeyinin altında çalıştığında ortaya çıkan kısımdır.',
        'Makroekonomi: doğal işsizlik oranı',
    ),
    # düzey 2
    '0024': patch(
        'Bir ülkede yıllık enflasyon oranı dört yıl boyunca sırasıyla %12, %8, %5 ve %3 olarak gerçekleşmiştir. Bu dönemdeki fiyat hareketi aşağıdakilerden hangisiyle nitelendirilir?',
        {
            'A': 'Deflasyon',
            'B': 'Dezenflasyon',
            'C': 'Hiperenflasyon',
            'D': 'Reflasyon',
            'E': 'Stagflasyon',
        },
        'B',
        'Enflasyon oranı pozitif kalmakla birlikte **azalan hızla** gerçekleşmektedir; fiyatlar artmaya devam eder ama artış hızı düşer: **dezenflasyon**. Deflasyon genel fiyat düzeyinin **düşmesi**, yani enflasyon oranının negatif olmasıdır.',
        'Makroekonomi: enflasyon hesaplama',
    ),
    # düzey 2
    '0025': patch(
        "Friedman-Phelps'in doğal oran hipotezine göre Phillips eğrisine ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kısa dönemde yataydır',
            'B': 'Uzun dönemde negatif eğimli ve daha yatıktır',
            'C': 'Uzun dönemde doğal işsizlik oranında dikeydir',
            'D': 'Enflasyon beklentilerinden bağımsızdır',
            'E': 'Uzun dönemde de enflasyon ile işsizlik arasında kalıcı bir seçim imkânı vardır',
        },
        'C',
        'Kısa dönemde beklenen enflasyon veriyken işsizlik ile enflasyon arasında ters ilişki olabilir. Ancak beklentiler fiilî enflasyona uyum sağladığında işsizlik **doğal orana** döner; uzun dönem Phillips eğrisi **dikeydir** ve kalıcı bir seçim imkânı sunmaz.',
        'Makroekonomi: Phillips eğrisi',
    ),
    # düzey 1
    '0026': patch(
        'Enflasyon nedeniyle firmaların fiyat listelerini, katalog ve etiketlerini sık sık yenilemek zorunda kalmalarının yarattığı maliyete ne ad verilir?',
        {
            'A': 'Batık maliyet',
            'B': 'Ajans maliyeti',
            'C': 'Fırsat maliyeti',
            'D': 'Ayakkabı eskitme maliyeti',
            'E': 'Menü maliyeti',
        },
        'E',
        '**Menü maliyeti**, fiyatları değiştirmenin idari ve fiziki maliyetidir. **Ayakkabı eskitme maliyeti** ise enflasyon döneminde nakit tutmanın maliyeti arttığı için bankaya daha sık gidip daha az nakit tutmanın yarattığı zaman ve çaba kaybıdır.',
        'Makroekonomi: enflasyonun maliyetleri',
    ),
    # düzey 2
    '0027': patch(
        'Basit Keynesyen modelde hanehalklarının hep birlikte tasarruf eğilimlerini artırmaları aşağıdaki sonuçlardan hangisine yol açar?',
        {
            'A': 'Denge gelir düşer; toplam tasarruf artmaz',
            'B': 'Faiz düşer ve yatırım aynı ölçüde artar',
            'C': 'Toplam tasarruf ve yatırım birlikte artar',
            'D': 'Denge gelir değişmez; toplam tasarruf artar',
            'E': 'Denge gelir artar; toplam tasarruf artar',
        },
        'A',
        'Tasarruf eğilimi artınca tüketim harcamaları ve dolayısıyla toplam talep düşer; gelir çarpan etkisiyle azalır. Yatırımlar sabitken dengede tasarruf yatırıma eşit olacağından toplam tasarruf artmaz: **tasarruf paradoksu**. Bireysel düzeyde erdem olan davranış toplumsal düzeyde geliri düşürür.',
        'Makroekonomi: tasarruf paradoksu',
    ),
    # düzey 2
    '0028': patch(
        'Aşağıdaki gelişmelerden hangisi LM eğrisini sağa kaydırır?',
        {
            'A': 'Hanehalkının para talebinin artması',
            'B': 'Kamu harcamalarının artması',
            'C': 'Vergilerin azaltılması',
            'D': 'Fiyatlar genel düzeyinin düşmesi',
            'E': 'Otonom yatırımların artması',
        },
        'D',
        "LM eğrisi reel para arzına (M/P) bağlıdır. **Fiyat düzeyinin düşmesi** reel para arzını artırır ve LM'yi sağa kaydırır. Kamu harcaması, vergi ve otonom yatırım değişmeleri **IS** eğrisini kaydırır; para talebinin artması ise LM'yi **sola** kaydırır.",
        'Makroekonomi: IS ve LM kaymaları',
    ),
    # düzey 3
    '0029': patch(
        'IS-LM modelinde genişletici maliye politikası ile genişletici para politikası birlikte uygulanırsa denge gelir ve faiz oranına ilişkin aşağıdakilerden hangisi kesin olarak söylenebilir?',
        {
            'A': 'Gelir değişmez, faiz artar',
            'B': 'Gelir azalır, faiz düşer',
            'C': 'Gelir artar; faizin yönü politikaların göreli büyüklüğüne bağlıdır',
            'D': 'Gelir artar, faiz düşer',
            'E': 'Gelir ve faiz birlikte artar',
        },
        'C',
        "Genişletici maliye politikası IS'yi sağa kaydırarak geliri ve faizi artırır; genişletici para politikası LM'yi sağa kaydırarak geliri artırıp faizi düşürür. İkisinde de gelir arttığı için **gelir kesin olarak artar**; faiz üzerindeki etkiler ters yönde olduğundan **faizin yönü belirsizdir**.",
        'Makroekonomi: politika bileşimi',
    ),
    # düzey 2
    '0030': patch(
        'Toplam arz eğrisine ilişkin aşağıdakilerden hangisi doğrudur? (Dikey eksen: fiyat düzeyi, yatay eksen: hasıla)',
        {
            'A': 'Keynesyen yaklaşımda eksik istihdamda toplam arz eğrisi dikeydir',
            'B': 'Klasik yaklaşımda toplam arz eğrisi potansiyel hasıla düzeyinde dikeydir',
            'C': 'Klasik yaklaşımda toplam talepteki artış hasılayı kalıcı olarak artırır',
            'D': 'Keynesyen yaklaşımda fiyatlar ve ücretler tam esnektir',
            'E': 'Klasik yaklaşımda toplam arz eğrisi yataydır',
        },
        'B',
        'Klasik yaklaşımda ücret ve fiyatlar tam esnek olduğu için ekonomi her zaman tam istihdamdadır; toplam arz eğrisi **potansiyel hasılada dikeydir** ve talep artışı yalnız fiyatları yükseltir. Keynesyen yaklaşımda eksik istihdamda fiyatlar katıdır ve toplam arz eğrisi yataydır.',
        'Makroekonomi: toplam arz',
    ),
    # düzey 2
    '0031': patch(
        'Ekonomik birimlerin davranışlarının politika değiştiğinde değişeceğini, bu nedenle geçmiş verilerle tahmin edilen ekonometrik modellerin yeni politikaların etkisini doğru öngöremeyeceğini ileri süren görüş hangisidir?',
        {
            'A': 'Ricardo denkliği',
            'B': 'Tasarruf paradoksu',
            'C': 'Terkip hatası',
            'D': 'Zaman tutarsızlığı',
            'E': 'Lucas eleştirisi',
        },
        'E',
        '**Lucas eleştirisine** göre model parametreleri (tüketim eğilimi, beklenti oluşumu) politika rejimine bağlıdır; politika değişince birimlerin davranışları ve dolayısıyla parametreler değişir. Zaman tutarsızlığı ise bugün optimal görünen bir politikanın ileride uygulanmak istenmeyecek olmasıdır.',
        'Makroekonomi: Lucas eleştirisi',
    ),
    # düzey 2
    '0032': patch(
        "Friedman'ın sürekli gelir hipotezine göre bir çalışanın tek seferlik yüksek bir ikramiye almasının tüketimine etkisi aşağıdakilerden hangisidir?",
        {
            'A': 'Tüketim marjinal tüketim eğilimi 1 olacak biçimde artar',
            'B': 'Tüketim değişmez, ikramiyenin tamamı borç ödemesine gider',
            'C': 'Tüketim ikramiye kadar artar',
            'D': 'Tüketim az artar; ikramiyenin büyük bölümü tasarruf edilir',
            'E': 'Tüketim azalır, tasarruf artar',
        },
        'D',
        '**Sürekli gelir hipotezine** göre tüketim, bireyin uzun dönemde beklediği ortalama (sürekli) gelire bağlıdır. Tek seferlik ikramiye **geçici gelirdir**; sürekli geliri az artırdığı için tüketimi de az artırır, büyük bölümü tasarruf edilir.',
        'Makroekonomi: sürekli gelir hipotezi',
    ),
    # düzey 1
    '0033': patch(
        "Gelir düştüğünde tüketicilerin alışık oldukları yaşam düzeyini korumak için tüketimlerini gelirdeki düşüş kadar azaltmamasını açıklayan 'mandal (ratchet) etkisi' hangi tüketim teorisine aittir?",
        {
            'A': "Friedman'ın sürekli gelir hipotezi",
            'B': "Duesenberry'nin nispi gelir hipotezi",
            'C': "Modigliani'nin yaşam boyu gelir hipotezi",
            'D': "Fisher'in zamanlar arası tercih modeli",
            'E': "Keynes'in mutlak gelir hipotezi",
        },
        'B',
        "**Duesenberry'nin nispi gelir hipotezi**, tüketimin hem çevredeki kişilerin tüketimine (gösteriş etkisi) hem de kişinin geçmişte ulaştığı en yüksek gelire bağlı olduğunu savunur; gelir düşünce tüketim eski düzeyinden kolayca aşağı inmez (**mandal etkisi**).",
        'Makroekonomi: nispi gelir hipotezi',
    ),
    # düzey 3
    '0034': patch(
        "Solow modelinde kişi başı üretim fonksiyonu y = √k, tasarruf oranı 0,3, nüfus artış hızı ile amortisman oranının toplamı 0,1'dir. Durağan durumdaki kişi başı sermaye (k*) ve kişi başı üretim (y*) aşağıdakilerden hangisidir?",
        {
            'A': 'k* = 9; y* = 3',
            'B': 'k* = 30; y* = √30',
            'C': 'k* = 9; y* = 9',
            'D': 'k* = 3; y* = √3',
            'E': 'k* = 0,3; y* = 0,55',
        },
        'A',
        'Durağan durumda kişi başı tasarruf, sermayeyi sabit tutmak için gereken yatırıma eşittir: s × √k = (n + d) × k → 0,3√k = 0,1k → √k = 3 → **k* = 9**, **y* = √9 = 3**.',
        'Makroekonomi: Solow modeli',
    ),
    # düzey 2
    '0035': patch(
        "Harcama yöntemiyle GSYH hesabında 'kamu mal ve hizmet alımları' kalemine aşağıdakilerden hangisi dahil edilir?",
        {
            'A': 'Devlet iç borçlanma senetlerine ödenen faizler',
            'B': 'İşsizlere ödenen sigorta ödemeleri',
            'C': 'Emeklilere ödenen aylıklar',
            'D': 'Kamu hastanesindeki doktorlara ödenen maaşlar',
            'E': 'Çiftçilere yapılan doğrudan gelir desteği',
        },
        'D',
        "Kamu mal ve hizmet alımları, devletin üretim karşılığı yaptığı harcamalardır; kamu görevlilerinin maaşları devletin satın aldığı emek hizmetinin bedeli olarak bu kaleme girer. Emekli aylıkları, işsizlik ödemeleri, faizler ve gelir destekleri karşılığında üretim yapılmayan **transfer** ödemeleridir ve GSYH'ye doğrudan girmez.",
        'Makroekonomi: harcama yöntemi',
    ),
    # düzey 2
    '0036': patch(
        'Aşağıdakilerden hangileri friksiyonel (arızi) işsizliğe örnektir?\n\nI. Mezun olduktan sonra ilk işini arayan bir mühendis\n\nII. Faaliyet alanı ortadan kalktığı için yeni beceri edinmesi gereken bir dizgici\n\nIII. Daha iyi bir iş bulmak için kendi isteğiyle işinden ayrılan bir muhasebeci',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        'İş arayanlar ile boş işlerin eşleşmesinin zaman almasından kaynaklanan işsizlik **friksiyonel** işsizliktir: ilk kez iş arayan mezun (I) ve daha iyi iş için ayrılan kişi (III) bu kapsamdadır. Mesleğin teknolojik değişimle ortadan kalkması ve yeni beceri gerektirmesi (II) ise **yapısal** işsizliktir.',
        'Makroekonomi: işsizlik türleri',
    ),
    # düzey 2
    '0037': patch(
        'Basit Keynesyen gelir-harcama modelinin varsayımlarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tüketim cari harcanabilir gelire bağlıdır',
            'B': 'Fiyatlar genel düzeyi sabittir',
            'C': 'Eksik istihdamda üretim talebe uyum sağlar',
            'D': 'Ekonomi ücret ve fiyat esnekliğiyle tam istihdam dengesine ulaşır',
            'E': 'Toplam harcama denge geliri belirler',
        },
        'D',
        'Basit Keynesyen modelde fiyatlar sabittir, üretim toplam talebe uyum sağlar ve tüketim cari gelire bağlıdır. Modelin temel iddiası, dengenin **eksik istihdamda** oluşabileceğidir; ekonominin kendiliğinden tam istihdama ulaşması klasik modelin varsayımıdır.',
        'Makroekonomi: Keynesyen model',
    ),
    # düzey 2
    '0038': patch(
        'Aşağıdaki tüketim teorisi–temel önerme eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': "Modigliani'nin yaşam boyu hipotezi – Birey tüketimini yaşam boyu gelirine göre planlar",
            'B': "Friedman'ın sürekli gelir hipotezi – Tüketim beklenen uzun dönem gelire bağlıdır",
            'C': "Keynes'in mutlak gelir hipotezi – Ortalama tüketim eğilimi gelir arttıkça artar",
            'D': "Duesenberry'nin nispi gelir hipotezi – Tüketim geçmişteki en yüksek gelirden etkilenir",
            'E': "Hall'un rassal yürüyüş hipotezi – Tüketimdeki değişmeler öngörülemez",
        },
        'C',
        "Keynes'in mutlak gelir hipotezinde otonom tüketim nedeniyle **ortalama tüketim eğilimi gelir arttıkça azalır**. Diğer eşleştirmeler teorilerin temel önermelerini doğru yansıtır; Hall'a göre rasyonel bekleyişlerle tüketim yalnız yeni bilgiye tepki verdiği için değişmeleri öngörülemez.",
        'Makroekonomi: tüketim teorileri',
    ),
    # düzey 1
    '0039': patch(
        'Çalışmak istediği hâlde uzun süre iş bulamadığı için umudunu yitirip iş aramayı bırakan kişiler işgücü istatistiklerinde nasıl sınıflandırılır?',
        {
            'A': 'İstihdam edilen',
            'B': 'İşgücü dışındaki kişiler',
            'C': 'İşsiz',
            'D': 'Friksiyonel işsiz',
            'E': 'Eksik istihdam edilen işgücü',
        },
        'B',
        'İşsiz sayılmak için aktif olarak iş aramak gerekir. İş aramayı bırakanlar **işgücü dışında** sayılır; bu nedenle umudu kırılmış işçilerin artması işsizlik oranını olduğundan düşük gösterebilir.',
        'Makroekonomi: işgücü',
    ),
    # düzey 2
    '0040': patch(
        'Gelir vergisi oranı yükseltildiğinde basit Keynesyen modelde harcama çarpanının değeri ve ekonominin şoklara duyarlılığı nasıl değişir?',
        {
            'A': 'Çarpan büyür; ekonomi harcama şoklarına daha duyarlı hâle gelir',
            'B': 'Çarpan büyür; duyarlılık değişmez',
            'C': 'Çarpan küçülür; ekonomi şoklara daha duyarlı hâle gelir',
            'D': 'Çarpan değişmez; duyarlılık artar',
            'E': 'Çarpan küçülür; ekonomi şoklara daha az duyarlı hâle gelir',
        },
        'E',
        'Gelir vergisi oranı t yükseldikçe çarpan 1 / [1 − c(1 − t)] **küçülür**: her ek gelirin daha büyük bir kısmı vergiyle sızar. Bu nedenle harcama şoklarının gelir üzerindeki etkisi azalır; orantılı gelir vergisi bu yolla **otomatik istikrarlandırıcı** işlev görür.',
        'Makroekonomi: otomatik istikrarlandırıcılar',
    ),
    # düzey 2
    '0041': patch(
        "Bir ekonomide cari yılın nominal GSYH'si 1.320, sabit fiyatlarla (reel) GSYH'si 1.100 birimdir. Bir önceki yılın reel GSYH'si 1.000 birim ise GSYH deflatörü ve reel büyüme oranı aşağıdakilerden hangisidir?",
        {
            'A': 'Deflatör 132; reel büyüme %10',
            'B': 'Deflatör 120; reel büyüme %10',
            'C': 'Deflatör 110; reel büyüme %20',
            'D': 'Deflatör 83; reel büyüme %10',
            'E': 'Deflatör 120; reel büyüme %32',
        },
        'B',
        "**GSYH deflatörü** = nominal GSYH / reel GSYH × 100 = 1.320 / 1.100 × 100 = **120**. Reel büyüme reel GSYH'deki değişimle ölçülür: (1.100 − 1.000) / 1.000 = **%10**. %32 nominal büyümedir; fiyat artışını da içerir.",
        'Makroekonomi: GSYH deflatörü',
    ),
    # düzey 2
    '0042': patch(
        'Çalışma çağındaki nüfusu 300 bin olan bir ekonomide 180 bin kişi çalışmakta, 20 bin kişi iş aramaktadır; kalanlar işgücüne dahil değildir. İşsizlik oranı ve işgücüne katılma oranı aşağıdakilerden hangisidir?',
        {
            'A': 'İşsizlik %6,7; katılma %66,7',
            'B': 'İşsizlik %10; katılma %60',
            'C': 'İşsizlik %6,7; katılma %60',
            'D': 'İşsizlik %10; katılma %66,7',
            'E': 'İşsizlik %11,1; katılma %66,7',
        },
        'D',
        'İşgücü = çalışanlar + iş arayanlar = 180 + 20 = 200 bin. İşsizlik oranı = 20 / 200 = **%10**; işgücüne katılma oranı = 200 / 300 = **%66,7**. %6,7 işsizlerin çalışma çağı nüfusuna, %11,1 ise çalışanlara bölünmesinin hatalı sonucudur.',
        'Makroekonomi: işsizlik oranı',
    ),
    # düzey 2
    '0043': patch(
        'Okun katsayısının 2 olduğu bir ekonomide fiilî işsizlik oranı doğal oranın 3 puan üzerindedir. Okun yasasına göre fiilî hasılanın potansiyel hasıladan sapması yaklaşık ne kadardır?',
        {
            'A': 'Potansiyelin %6 altında',
            'B': 'Potansiyelin %6 üzerinde',
            'C': 'Potansiyelin %3 altında',
            'D': 'Potansiyelin %1,5 altında',
            'E': 'Potansiyele eşit',
        },
        'A',
        '**Okun yasası**, işsizlik oranının doğal orandan sapması ile hasıla açığı arasındaki ters ilişkiyi gösterir: hasıla açığı ≈ −Okun katsayısı × (fiilî işsizlik − doğal işsizlik) = −2 × 3 = **%−6**. Hasıla potansiyelin yaklaşık %6 altındadır.',
        'Makroekonomi: Okun yasası',
    ),
    # düzey 1
    '0044': patch(
        'Bir ülkede tüketici fiyat endeksi önceki yıl 250, bu yıl 275 olarak hesaplanmıştır. Bu yılın enflasyon oranı yüzde kaçtır?',
        {
            'A': '25',
            'B': '27,5',
            'C': '110',
            'D': '9,1',
            'E': '10',
        },
        'E',
        'Enflasyon oranı = (275 − 250) / 250 × 100 = **%10**. 25 endeks puanındaki mutlak artıştır; 9,1 ise artışın yeni endekse (275) bölünmesinin hatalı sonucudur.',
        'Makroekonomi: enflasyon hesaplama',
    ),
    # düzey 2
    '0045': patch(
        "Tüketim fonksiyonu C = 150 + cYd biçiminde olan bir ekonomide harcanabilir gelir 1.000 iken tüketim 850'dir. Marjinal tüketim eğilimi (MPC) ve ortalama tüketim eğilimi (APC) sırasıyla aşağıdakilerden hangisidir?",
        {
            'A': '0,85 ve 0,85',
            'B': '0,85 ve 0,70',
            'C': '0,70 ve 0,85',
            'D': '0,70 ve 0,70',
            'E': '0,15 ve 0,85',
        },
        'C',
        "850 = 150 + c × 1.000 → c = **0,70** (MPC). Ortalama tüketim eğilimi = C / Yd = 850 / 1.000 = **0,85**. Otonom tüketim nedeniyle Keynesyen tüketim fonksiyonunda APC, MPC'den büyüktür ve gelir arttıkça azalır.",
        'Makroekonomi: tüketim fonksiyonu',
    ),
    # düzey 3
    '0046': patch(
        "Kapalı bir ekonomide C = 100 + 0,75(Y − T), vergiler götürü T = 100, yatırım I = 150, kamu harcamaları G = 200'dür. Denge milli gelir kaçtır?",
        {
            'A': '1.200',
            'B': '1.900',
            'C': '450',
            'D': '1.800',
            'E': '1.500',
        },
        'E',
        'Y = 100 + 0,75(Y − 100) + 150 + 200 → Y = 100 + 0,75Y − 75 + 350 → 0,25Y = 375 → **Y = 1.500**. 1.800, vergilerin ihmal edilmesinin (0,25Y = 450) sonucudur.',
        'Makroekonomi: denge gelir',
    ),
    # düzey 1
    '0047': patch(
        "'Her arz kendi talebini yaratır' biçiminde özetlenen ve klasik iktisatta genel bir talep yetersizliğinin kalıcı olamayacağını savunan ilke aşağıdakilerden hangisidir?",
        {
            'A': 'Wagner yasası',
            'B': 'Say yasası',
            'C': 'Okun yasası',
            'D': 'Gresham yasası',
            'E': 'Engel yasası',
        },
        'B',
        '**Say yasasına** göre üretim, üretim faktörlerine gelir yaratır ve bu gelir üretilen malların satın alınmasında kullanılır; bu nedenle genel bir aşırı üretim veya talep yetersizliği kalıcı olamaz. Keynes bu ilkeyi reddederek efektif talep yetersizliğini ön plana çıkarmıştır.',
        'Makroekonomi: Say yasası',
    ),
    # düzey 2
    '0048': patch(
        'IS-LM modelinde aşağıdaki durumlardan hangileri para politikasını etkisiz kılar?\n\nI. Ekonominin likidite tuzağında olması\n\nII. Yatırımların faize tamamen duyarsız olması\n\nIII. Para talebinin faize tamamen duyarsız olması',
        {
            'A': 'Yalnız III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'D',
        'Likidite tuzağında (LM yatay) para arzı artışı faizi düşüremez (I); yatırımlar faize duyarsızsa (IS dikey) faiz düşse bile yatırım ve gelir artmaz (II). Para talebi faize duyarsızsa LM **dikeydir** ve bu durumda para politikası en etkili, maliye politikası ise etkisizdir (III yanlış).',
        'Makroekonomi: IS-LM ve politika etkinliği',
    ),
    # düzey 2
    '0049': patch(
        'IS-LM modelinde maliye politikası çarpanının değerine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatırımların faize duyarlılığı küçüldükçe çarpan büyür.\n\nII. Para talebinin faize duyarlılığı büyüdükçe çarpan büyür.\n\nIII. Para talebinin gelire duyarlılığı büyüdükçe çarpan büyür.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'C',
        'Maliye politikası çarpanı dışlama etkisi azaldıkça büyür. Yatırım faize az duyarlıysa faiz artışı yatırımı az dışlar (I). Para talebi faize çok duyarlıysa gelir artışının yarattığı ek para talebi küçük bir faiz artışıyla karşılanır (II). Para talebinin **gelire** duyarlılığı arttıkça gelir artışı faizi daha çok yükseltir, dışlama güçlenir ve çarpan **küçülür** (III yanlış).',
        'Makroekonomi: IS-LM ve çarpan',
    ),
    # düzey 2
    '0050': patch(
        'Fiyatlar genel düzeyi düştüğünde reel servetin (reel para balansının) artması nedeniyle tüketimin artmasını ifade eden ve toplam talep eğrisinin negatif eğimini açıklayan etki hangisidir?',
        {
            'A': 'Pigou etkisi',
            'B': 'Dışlama etkisi',
            'C': 'Keynes faiz etkisi',
            'D': 'Hızlandıran etkisi',
            'E': 'Dış ticaret etkisi',
        },
        'A',
        '**Pigou (reel balans) etkisinde** fiyat düşüşü para varlıklarının satın alma gücünü artırır, hanehalkı kendini daha zengin hisseder ve tüketimi artırır. **Keynes faiz etkisinde** fiyat düşüşü reel para arzını artırıp faizi düşürerek yatırımı; **dış ticaret etkisinde** ise yerli malları ucuzlatarak net ihracatı artırır.',
        'Makroekonomi: toplam talep',
    ),
    # düzey 3
    '0051': patch(
        'Yeni Klasik modele göre merkez bankasının kamuoyuna duyurmadığı ve ekonomik birimlerin öngöremediği bir para genişlemesinin etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Ne kısa ne uzun dönemde hasıla veya fiyatlar değişir',
            'B': 'Kısa dönemde fiyatlar yükselir, uzun dönemde düşer',
            'C': 'Kısa dönemde hasıla artabilir; uzun dönemde etkisi fiyatlarda kalır',
            'D': 'Hasıla kalıcı olarak artar, fiyatlar değişmez',
            'E': 'Hasıla hemen düşer, fiyatlar değişmez',
        },
        'C',
        'Rasyonel bekleyişlerde **öngörülen** politika bekleyişlere hemen yansıdığı için reel etki yaratmaz. **Sürpriz** bir para genişlemesi ise ekonomik birimleri fiyat artışını göreli fiyat değişmesi sanmaya yöneltir ve kısa dönemde hasılayı artırabilir; beklentiler düzeltildiğinde hasıla potansiyel düzeye döner ve kalıcı etki fiyatlarda kalır.',
        'Makroekonomi: yeni klasik model',
    ),
    # düzey 2
    '0052': patch(
        'Yeni Keynesyen iktisadın para politikasının kısa dönemde reel etkileri olabileceğini açıklamak için dayandığı temel unsur aşağıdakilerden hangisidir?',
        {
            'A': 'Paranın uzun dönemde de yansız olmaması',
            'B': 'Menü maliyetleri ve sözleşmeler nedeniyle ücret ve fiyatların katı olması',
            'C': 'Bekleyişlerin uyarlayıcı biçimde oluşması',
            'D': 'Piyasaların sürekli temizlenmesi',
            'E': 'Toplam arz eğrisinin her dönemde yatay olması',
        },
        'B',
        'Yeni Keynesyenler rasyonel bekleyişleri kabul eder, ancak **menü maliyetleri**, kademeli fiyat ayarlaması ve uzun vadeli ücret sözleşmeleri gibi nedenlerle nominal katılıkların varlığını gösterir. Fiyatlar hemen uyum sağlamadığı için para politikası kısa dönemde üretimi etkileyebilir; uzun dönemde para yansızdır.',
        'Makroekonomi: yeni Keynesyen model',
    ),
    # düzey 2
    '0053': patch(
        'Sermaye/hasıla oranının 3 olduğu bir ekonomide hasılanın 100 birim artması beklenmektedir. Hızlandıran (akseleratör) ilkesine göre gereken net yatırım kaç birimdir?',
        {
            'A': '103',
            'B': '100',
            'C': '33,3',
            'D': '400',
            'E': '300',
        },
        'E',
        '**Hızlandıran ilkesine** göre net yatırım, hasıladaki değişmenin sermaye/hasıla oranıyla çarpımıdır: I = v × ΔY = 3 × 100 = **300**. Hasıladaki küçük değişmeler yatırımda oransal olarak daha büyük dalgalanmalar yaratır.',
        'Makroekonomi: hızlandıran ilkesi',
    ),
    # düzey 2
    '0054': patch(
        'Solow büyüme modeline ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasarruf oranının artması kişi başı gelirin büyüme hızını kalıcı olarak artırır',
            'B': 'Nüfus artış hızının yükselmesi durağan durumdaki kişi başı geliri düşürür',
            'C': 'Kişi başı gelirin uzun dönemde sürekli büyümesi teknolojik ilerlemeye bağlıdır',
            'D': 'Sermayenin marjinal verimi sermaye biriktikçe azalır',
            'E': 'Teknolojik ilerleme yoksa durağan durumda kişi başı sermaye sabittir',
        },
        'A',
        "Solow modelinde sermayenin **azalan marjinal verimi** nedeniyle sermaye birikimi tek başına kalıcı büyüme sağlayamaz. Tasarruf oranının artması durağan durumdaki kişi başı gelir **düzeyini** yükseltir; geçiş sürecinde büyüme hızlanır ama durağan durumda büyüme hızı yeniden teknolojik ilerleme oranına döner. Bu nedenle 'kalıcı olarak artırır' ifadesi yanlıştır.",
        'Makroekonomi: Solow modeli',
    ),
    # düzey 2
    '0055': patch(
        'Yurt içinde üretilmeyip ithal edilen bir tüketim malının fiyatındaki artış, TÜFE ve GSYH deflatörünü nasıl etkiler?',
        {
            'A': 'İkisini de etkilemez',
            'B': "GSYH deflatörünü yükseltir, TÜFE'yi ise doğrudan etkilemez",
            'C': 'İkisini de aynı oranda yükseltir',
            'D': "TÜFE'yi yükseltir, GSYH deflatörünü doğrudan etkilemez",
            'E': "TÜFE'yi düşürür, GSYH deflatörünü yükseltir",
        },
        'D',
        '**TÜFE** tüketicilerin satın aldığı sabit bir sepetin fiyatını ölçer; ithal tüketim malları sepete dahildir. **GSYH deflatörü** ise yalnız yurt içinde üretilen malların fiyatlarını kapsar; ithal malın fiyat artışı onu doğrudan etkilemez.',
        'Makroekonomi: TÜFE ve deflatör',
    ),
    # düzey 2
    '0056': patch(
        'Toplam talebin azaldığı bir durumda kısa dönem toplam arz eğrisi pozitif eğimliyse kısa dönemde aşağıdakilerden hangisi gerçekleşir?',
        {
            'A': 'Fiyat düzeyi ve hasıla birlikte artar',
            'B': 'Fiyat düzeyi düşer, hasıla artar',
            'C': 'Fiyat düzeyi ve hasıla birlikte düşer',
            'D': 'Hasıla değişmez, fiyat düzeyi düşer',
            'E': 'Fiyat düzeyi artar, hasıla düşer',
        },
        'C',
        'Toplam talep eğrisi sola kayınca pozitif eğimli kısa dönem arz eğrisi boyunca **fiyat düzeyi ve hasıla birlikte düşer**. Fiyatın düşüp hasılanın değişmemesi dikey (klasik) arz eğrisinde, fiyat artıp hasılanın düşmesi ise arz şokunda görülür.',
        'Makroekonomi: AD-AS',
    ),
    # düzey 2
    '0057': patch(
        'Bir ekonomide fiilî hasılanın potansiyel hasılanın üzerinde olmasının kısa dönemde beklenen sonucu aşağıdakilerden hangisidir?',
        {
            'A': 'Kapasite kullanım oranı düşer',
            'B': 'İşsizlik doğal oranın altına iner, enflasyon baskısı artar',
            'C': 'Konjonktürel işsizlik artar',
            'D': 'İşsizlik doğal oranın üzerine çıkar, fiyatlar genel düzeyi düşer',
            'E': 'Deflasyonist açık oluşur',
        },
        'B',
        'Pozitif hasıla açığında ekonomi kapasitesinin üzerinde çalışır: işsizlik doğal oranın altına iner, kapasite kullanımı yükselir ve ücret-fiyat baskısı nedeniyle **enflasyonist açık** oluşur. Deflasyonist açık ve konjonktürel işsizlik, hasılanın potansiyelin altında olduğu durumlara aittir.',
        'Makroekonomi: potansiyel hasıla',
    ),
    # düzey 3
    '0058': patch(
        "Kapalı bir ekonomide denge gelir 2.000, vergiler T = 0,2Y, kamu harcamaları 350 ve transfer ödemeleri 80'dir. Hükümet bütçesinin durumu aşağıdakilerden hangisidir?",
        {
            'A': '30 birim bütçe fazlası',
            'B': '50 birim bütçe fazlası',
            'C': 'Bütçe dengededir',
            'D': '30 birim bütçe açığı',
            'E': '400 birim bütçe fazlası',
        },
        'D',
        'Vergi gelirleri = 0,2 × 2.000 = 400. Kamu harcamaları ve transferlerin toplamı 350 + 80 = 430. Bütçe dengesi = 400 − 430 = −30, yani **30 birim açık**. 50 birim fazla, transferlerin harcamalara eklenmemesinin sonucudur.',
        'Makroekonomi: bütçe dengesi ve gelir',
    ),
    # düzey 1
    '0059': patch(
        'Bir konjonktür dalgasının evreleri, bir dip noktasından başlayarak aşağıdakilerden hangisinde doğru sıralanmıştır?',
        {
            'A': 'Genişleme – Dip – Daralma – Tepe',
            'B': 'Daralma – Tepe – Genişleme – Dip',
            'C': 'Tepe – Genişleme – Dip – Daralma',
            'D': 'Dip – Daralma – Tepe – Genişleme',
            'E': 'Genişleme – Tepe – Daralma – Dip',
        },
        'E',
        'Konjonktür dalgası dipten sonra üretim ve istihdamın arttığı **genişleme** (canlanma) evresiyle başlar, ekonomik faaliyetin en yüksek düzeyine ulaştığı **tepe** noktasından sonra **daralma** (resesyon) evresine girer ve yeni bir **dip** noktasına iner.',
        'Makroekonomi: konjonktür evreleri',
    ),
    # düzey 3
    '0060': patch(
        'Bir ekonomide 20 bin işsiz iş aramayı bırakıp işgücünden çıkmıştır. Başlangıçta işgücü 400 bin, işsiz sayısı 40 bindir. Diğer koşullar sabitken işsizlik oranındaki değişim aşağıdakilerden hangisidir?',
        {
            'A': "%10'dan %5'e düşer",
            'B': "%10'dan yaklaşık %5,3'e düşer",
            'C': "%10'dan %15'e yükselir",
            'D': "%10'da kalır",
            'E': "%10'dan yaklaşık %11,1'e yükselir",
        },
        'B',
        'Başlangıçta işsizlik oranı 40 / 400 = %10. İş aramayı bırakan 20 bin kişi hem işsiz sayısından hem işgücünden düşer: 20 / 380 ≈ **%5,3**. İstihdam değişmediği hâlde oranın düşmesi, umudu kırılmış işçiler nedeniyle işsizlik oranının yanıltıcı olabileceğini gösterir. %5, işgücünün değişmediği varsayımıyla yapılan hatalı hesaptır.',
        'Makroekonomi: işsizlik ve katılım',
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
    print(f"1 paket / {len(PATCHES)} soru ('Makroekonomi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
