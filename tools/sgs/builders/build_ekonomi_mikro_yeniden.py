#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mikroekonomi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiline gore yeniden yazim (2019-2026, 108 gercek ekonomi sorusu: hesap agirlikli, kisa sik). 26 hesap sorusu (esneklik, tuketici/uretici fazlasi, tuketici dengesi, maliyet, kapatma noktasi, tam rekabet/monopol/Cournot dengesi, dara kaybi, Lerner, subvansiyon); tum hesaplar sympy ile bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Mikroekonomi teorisi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ekonomi/mikroekonomi.json"
STYLE_REF = 'SGS Ekonomi (gercek sinav profiline kalibre: hesap + kisa sik)'
ONEK = "eko-mikro-gen-"


def patch(stem, options, answer, solution, ref='Mikroekonomi teorisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir kafenin günlük limonata talebi Qd = 60 − 3P biçimindedir. Fiyat 8 ₺ iken talebin fiyat esnekliği ve kafenin bu noktadaki fiyat artışı kararının hasılata etkisi aşağıdakilerden hangisidir?',
        {
            'A': '3/2; talep elastiktir, fiyat artışı hasılatı azaltır',
            'B': '2/3; talep inelastiktir, fiyat artışı hasılatı artırır',
            'C': '2/3; talep inelastiktir, fiyat artışı hasılatı azaltır',
            'D': '1; talep birim esnektir, hasılat değişmez',
            'E': '3/2; talep elastiktir, fiyat artışı hasılatı artırır',
        },
        'B',
        "P = 8 iken Q = 60 − 24 = 36. Nokta esnekliği = (dQ/dP) × (P/Q) = −3 × 8/36 = −24/36 = −2/3; mutlak değeri **2/3**'tür. Değer 1'den küçük olduğu için talep **inelastiktir** ve fiyat artışı hasılatı artırır. 3/2 oranın ters kurulmasının sonucudur.",
        'Mikroekonomi: nokta esnekliği',
    ),
    # düzey 2
    '0002': patch(
        'A malının fiyatı %5 arttığında B malının talep edilen miktarı %10 azalmıştır. A ve B malları arasındaki ilişki ve çapraz esneklik katsayısı aşağıdakilerden hangisidir?',
        {
            'A': 'Tamamlayıcı mallar; −2',
            'B': 'Tamamlayıcı mallar; −0,5',
            'C': 'İkame mallar; −2',
            'D': 'Bağımsız mallar; 0',
            'E': 'İkame mallar; +2',
        },
        'A',
        "Çapraz esneklik = B'nin miktarındaki % değişme / A'nın fiyatındaki % değişme = −10 / 5 = **−2**. Negatif çapraz esneklik, A pahalandığında B'ye talebin de azaldığını, yani malların birlikte tüketildiğini (**tamamlayıcı**) gösterir. İkame mallarda katsayı pozitiftir.",
        'Mikroekonomi: çapraz esneklik',
    ),
    # düzey 3
    '0003': patch(
        "Talep fonksiyonu P = 50 − Q olan bir piyasada fiyat 20 ₺'den 30 ₺'ye yükselmiştir. Tüketici fazlasındaki kayıp kaç ₺'dir?",
        {
            'A': '200',
            'B': '100',
            'C': '250',
            'D': '450',
            'E': '300',
        },
        'C',
        'Fiyat 20 iken Q = 30 ve tüketici fazlası ½ × 30 × 30 = 450. Fiyat 30 iken Q = 20 ve tüketici fazlası ½ × 20 × 20 = 200. Kayıp = 450 − 200 = **250**. 200 yeni fazlanın kendisidir; kayıp iki durum arasındaki farktır.',
        'Mikroekonomi: tüketici fazlası',
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdakilerden hangileri X malının arz eğrisini sağa kaydırır?\n\nI. Üretim teknolojisinde gelişme\n\nII. Girdi fiyatlarının düşmesi\n\nIII. X malının kendi fiyatının yükselmesi\n\nIV. Üreticilere birim başına sübvansiyon verilmesi',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II ve IV',
            'E': 'I, II, III ve IV',
        },
        'D',
        'Teknolojik gelişme (I), girdi fiyatlarının düşmesi (II) ve birim sübvansiyon (IV) her fiyat düzeyinde daha fazla arz edilmesini sağlayarak **arz eğrisini sağa kaydırır**. Malın kendi fiyatının değişmesi (III) ise eğriyi kaydırmaz; **eğri üzerinde hareket** (arz edilen miktarda değişme) yaratır.',
        'Mikroekonomi: arz eğrisini kaydıran etkenler',
    ),
    # düzey 1
    '0005': patch(
        "Bir tüketicinin simit tüketiminden elde ettiği toplam fayda 1'den 6'ya kadar birimler için sırasıyla 20, 36, 48, 56, 60 ve 60'tır. Hangi birimde marjinal fayda sıfırdır?",
        {
            'A': '1. birim',
            'B': '5. birim',
            'C': '4. birim',
            'D': 'Marjinal fayda bu aralıkta sıfıra inmez',
            'E': '6. birim',
        },
        'E',
        'Marjinal fayda, ek birimin toplam faydada yarattığı değişmedir: 20, 16, 12, 8, 4 ve **0**. 6. birim toplam faydayı artırmadığı için marjinal faydası sıfırdır; bu nokta **doyum noktasıdır**. Azalan marjinal fayda ilkesi, ardışık birimlerin daha az ek fayda sağlamasıdır.',
        'Mikroekonomi: marjinal fayda',
    ),
    # düzey 2
    '0006': patch(
        "Fayda fonksiyonu U = X^0,5 · Y^0,5 olan bir tüketicinin geliri 200 ₺ ve X malının fiyatı 5 ₺'dir. Tüketicinin X malı talebi kaç birimdir?",
        {
            'A': '20',
            'B': '40',
            'C': '30',
            'D': '25',
            'E': '50',
        },
        'A',
        "Cobb-Douglas faydada tüketici gelirinin üslerle orantılı payını her mala harcar: X'in payı 0,5 / (0,5 + 0,5) = 1/2. X'e harcama 200 × 1/2 = 100 ₺; X = 100 / 5 = **20**. 40, gelirin tamamının X'e harcanmasının sonucudur.",
        'Mikroekonomi: Cobb-Douglas talep',
    ),
    # düzey 2
    '0007': patch(
        "Fayda fonksiyonu U = X · Y olan bir tüketicinin X = 4 ve Y = 8 birimlik bileşimde marjinal ikame oranı (Y cinsinden X'in MRS'i) kaçtır?",
        {
            'A': '8',
            'B': '0,5',
            'C': '32',
            'D': '2',
            'E': '4',
        },
        'D',
        "MRS = MUx / MUy = Y / X = 8 / 4 = **2**; tüketici bir birim ek X için 2 birim Y'den vazgeçmeye razıdır. 0,5 oranın ters kurulmasının, 32 ise toplam faydanın (4 × 8) sonucudur.",
        'Mikroekonomi: marjinal ikame oranı',
    ),
    # düzey 2
    '0008': patch(
        'Üretim fonksiyonu Q = K^0,6 · L^0,5 olan bir firma için ölçeğe göre getiri ve iki faktör aynı oranda %10 artırıldığında çıktıdaki değişim aşağıdakilerden hangisidir?',
        {
            'A': "Azalan getiri; çıktı %10'dan az artar",
            'B': "Artan getiri; çıktı %10'dan fazla artar",
            'C': 'Sabit getiri; çıktı tam %10 artar',
            'D': "Artan getiri; çıktı %10'dan az artar",
            'E': "Azalan getiri; çıktı %10'dan fazla artar",
        },
        'B',
        "Cobb-Douglas fonksiyonunda üslerin toplamı ölçeğe göre getiriyi belirler: 0,6 + 0,5 = 1,1 > 1, yani **ölçeğe göre artan getiri** vardır. Faktörler %10 artırıldığında çıktı yaklaşık 1,1^1,1 − 1 ≈ %11 artar; artış %10'dan fazladır.",
        'Mikroekonomi: ölçeğe göre getiri',
    ),
    # düzey 1
    '0009': patch(
        'Uzun dönemde iki faktör kullanan bir firmanın belirli bir üretimi en düşük maliyetle gerçekleştirmesinin koşulu aşağıdakilerden hangisidir? (MP: marjinal ürün; w: ücret; r: sermaye fiyatı)',
        {
            'A': 'MP_L = MP_K',
            'B': 'MP_L · w = MP_K · r',
            'C': 'w = r',
            'D': 'MP_L / MP_K = r / w',
            'E': 'MP_L / w = MP_K / r',
        },
        'E',
        'Maliyet minimizasyonunda her faktöre harcanan son liranın sağladığı marjinal ürün eşitlenir: **MP_L / w = MP_K / r**. Bu, eşürün eğrisinin eğimi olan marjinal teknik ikame oranının (MP_L / MP_K) faktör fiyatları oranına (w / r) eşit olması demektir.',
        'Mikroekonomi: maliyet minimizasyonu',
    ),
    # düzey 2
    '0010': patch(
        'Kısa dönem maliyet eğrileri arasındaki ilişkiye ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Marjinal maliyet eğrisi ortalama değişken maliyeti en düşük noktasında keser',
            'B': 'Marjinal maliyet eğrisi ortalama toplam maliyeti en düşük noktasında keser',
            'C': 'Ortalama sabit maliyet üretim arttıkça sürekli azalır',
            'D': 'Marjinal maliyet eğrisi ortalama sabit maliyet eğrisini en düşük noktasında keser',
            'E': 'Ortalama toplam ve ortalama değişken maliyet arasındaki fark üretim arttıkça daralır',
        },
        'D',
        'Marjinal maliyet, ortalama değişken ve ortalama toplam maliyet eğrilerini bunların **en düşük noktalarında** keser. Ortalama sabit maliyet (AFC = FC/Q) üretim arttıkça **sürekli azalır**; en düşük noktası yoktur. AFC azaldığı için ATC ile AVC arasındaki fark daralır.',
        'Mikroekonomi: kısa dönem maliyet eğrileri',
    ),
    # düzey 1
    '0011': patch(
        'Mikroekonomide kısa dönem ile uzun dönemi birbirinden ayıran temel ölçüt aşağıdakilerden hangisidir?',
        {
            'A': 'Kısa dönemde firmaların zarar edememesi',
            'B': 'Uzun dönemde teknolojinin değişmemesi',
            'C': 'Uzun dönemde fiyatların sabit kalması',
            'D': 'Kısa dönemin bir takvim yılından, uzun dönemin ise beş yıldan kısa olması',
            'E': 'Uzun dönemde bütün üretim faktörlerinin değişken olması',
        },
        'E',
        'Mikroekonomide dönemler takvim süresiyle değil **faktörlerin değişkenliğiyle** tanımlanır. Kısa dönemde en az bir faktör (tesis, sermaye) sabittir; uzun dönemde firma bütün faktörleri ayarlayabilir, piyasaya girip çıkabilir.',
        'Mikroekonomi: kısa ve uzun dönem',
    ),
    # düzey 3
    '0012': patch(
        "Bir monopolün karşılaştığı talep eğrisi P = 120 − 2Q, marjinal maliyeti sabit 20 ₺'dir. Monopolün kârı en yükselten fiyatı ve üretim miktarı aşağıdakilerden hangisidir?",
        {
            'A': 'P = 60 ₺; Q = 30',
            'B': 'P = 70 ₺; Q = 25',
            'C': 'P = 70 ₺; Q = 50',
            'D': 'P = 20 ₺; Q = 50',
            'E': 'P = 95 ₺; Q = 12,5',
        },
        'B',
        "Monopol MR = MC'de üretir. Doğrusal talepte MR = 120 − 4Q; 120 − 4Q = 20 → **Q = 25**. Fiyat talep eğrisinden bulunur: P = 120 − 50 = **70 ₺**. P = 20 ve Q = 50, fiyatın marjinal maliyete eşit olduğu tam rekabet sonucudur.",
        'Mikroekonomi: monopol dengesi',
    ),
    # düzey 2
    '0013': patch(
        'Kârını maksimize eden bir monopole ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Talep eğrisinin elastik (|e| > 1) kesiminde üretim yapar.\n\nII. Fiyatı marjinal maliyetin üzerinde belirler.\n\nIII. Arz eğrisi marjinal maliyet eğrisinin ortalama değişken maliyetin üzerindeki kısmıdır.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'A',
        "Monopol MR = MC'de üretir; MC pozitif olduğundan MR de pozitiftir, bu da talebin **elastik** kesimine karşılık gelir (I). Fiyat, talep eğrisinden MR'nin üzerinde belirlenir: P > MC (II). Monopolün fiyat ile miktar arasında tek bir ilişkisi olmadığı için **arz eğrisi yoktur**; tanımlanan arz eğrisi tam rekabetçi firmaya aittir (III yanlış).",
        'Mikroekonomi: monopol',
    ),
    # düzey 2
    '0014': patch(
        'Tekelci rekabet piyasasında uzun dönem dengesinde firmanın, ortalama maliyet eğrisinin en düşük noktasının solunda üretim yapmasına ne ad verilir?',
        {
            'A': 'Ölçek ekonomisi',
            'B': 'Kartel dengesi',
            'C': 'Dara kaybı',
            'D': 'Atıl kapasite',
            'E': 'Fiyat liderliği',
        },
        'D',
        'Tekelci rekabette ürünler farklılaştırılmış olduğu için firmanın talep eğrisi negatif eğimlidir. Uzun dönemde serbest giriş kârı sıfırlar ve talep eğrisi ortalama maliyet eğrisine onun **azalan** kesiminde teğet olur; firma optimum ölçeğin altında üretir: **atıl kapasite**.',
        'Mikroekonomi: tekelci rekabet',
    ),
    # düzey 3
    '0015': patch(
        'Piyasa talebi P = 100 − Q olan ve iki özdeş firmanın marjinal maliyetinin sabit 10 ₺ olduğu bir Cournot düopolünde denge piyasa fiyatı kaçtır?',
        {
            'A': '10 ₺',
            'B': '55 ₺',
            'C': '40 ₺',
            'D': '30 ₺',
            'E': '45 ₺',
        },
        'C',
        "Cournot'da her firma rakibinin miktarını veri alarak MR = MC yapar. Firma 1 için MR = 100 − 2q1 − q2 = 10 → q1 = 45 − q2/2; simetriden q1 = q2 = q → q = 45 − q/2 → **q = 30**. Toplam Q = 60, fiyat = 100 − 60 = **40 ₺**. 55 ₺ tek monopol (Q = 45) fiyatı, 10 ₺ tam rekabet (Bertrand) fiyatıdır.",
        'Mikroekonomi: Cournot düopolü',
    ),
    # düzey 1
    '0016': patch(
        'Tam rekabet piyasasındaki tek bir firmaya ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Daha fazla satabilmek için fiyatını düşürmesi gerekir',
            'B': 'Fiyat marjinal hasılata eşittir',
            'C': 'Fiyat ortalama hasılata eşittir',
            'D': 'Piyasa fiyatını veri kabul eder',
            'E': 'Karşılaştığı talep eğrisi piyasa fiyatı düzeyinde yataydır',
        },
        'A',
        "Tam rekabetçi firma piyasada çok küçük olduğu için piyasa fiyatından istediği kadar satabilir; talebi **yataydır** ve P = AR = MR'dir. Satışları artırmak için fiyat düşürmesi gerekmez; fiyatı piyasanın altına çekmesi yalnız hasılatını azaltır. Negatif eğimli talep, piyasa gücü olan firmalara özgüdür.",
        'Mikroekonomi: tam rekabetçi firmanın talebi',
    ),
    # düzey 2
    '0017': patch(
        "Bir öğrenci, saatine 150 ₺ kazandığı yarı zamanlı işini bırakarak 4 saatlik ücretsiz bir seminere katılmış ve seminer için 100 ₺ ulaşım gideri yapmıştır. Seminere katılmanın fırsat maliyeti kaç ₺'dir?",
        {
            'A': '600',
            'B': '250',
            'C': '700',
            'D': '100',
            'E': '150',
        },
        'C',
        'Fırsat maliyeti, vazgeçilen en iyi alternatifin değeri ile yapılan açık harcamaların toplamıdır: vazgeçilen kazanç 4 × 150 = 600 ₺ + ulaşım gideri 100 ₺ = **700 ₺**. 600 ₺ yalnız örtük maliyeti, 100 ₺ yalnız açık maliyeti gösterir.',
        'Mikroekonomi: fırsat maliyeti',
    ),
    # düzey 1
    '0018': patch(
        'Tüketicilerin geliri arttığında talep edilen miktarı azalan mallara ne ad verilir?',
        {
            'A': 'Veblen malları',
            'B': 'Düşük mallar',
            'C': 'Zorunlu mallar',
            'D': 'Lüks mallar',
            'E': 'Tamamlayıcı mallar',
        },
        'B',
        'Gelir esnekliği **negatif** olan mallar **düşük mallardır**; gelir arttıkça tüketiciler bunların yerine daha kaliteli ikamelere yönelir. Zorunlu ve lüks mallar ise gelir esnekliği pozitif olan normal mallardır.',
        'Mikroekonomi: düşük mal',
    ),
    # düzey 2
    '0019': patch(
        'Uzun dönem ortalama maliyet eğrisinin azalan kesiminde bulunan bir firmaya ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Azalan verimler kanunu nedeniyle ölçek büyümesi maliyeti artırır',
            'B': 'Üretim ölçeğini büyüttükçe birim maliyeti artar',
            'C': 'Uzun dönem marjinal maliyet ortalama maliyetin üzerindedir',
            'D': 'Firma optimum ölçekte üretim yapmaktadır',
            'E': 'Üretim ölçeğini büyüttükçe birim maliyeti düşer; ölçek ekonomisi vardır',
        },
        'E',
        "Uzun dönem ortalama maliyetin azaldığı kesimde ölçek büyüdükçe birim maliyet düşer: **ölçek ekonomisi**. Bu kesimde uzun dönem marjinal maliyet ortalama maliyetin **altındadır**; optimum ölçek, LAC'nin en düşük noktasıdır. Azalan verimler ise kısa döneme ait bir kavramdır.",
        'Mikroekonomi: ölçek ekonomileri',
    ),
    # düzey 3
    '0020': patch(
        "Tam rekabet piyasasında faaliyet gösteren bir firmanın ürettiği 100 birimde ortalama toplam maliyet 25 ₺, ortalama değişken maliyet 18 ₺'dir. Piyasa fiyatı 20 ₺ ise firmanın kısa dönemdeki kararı ve sonucu aşağıdakilerden hangisidir?",
        {
            'A': 'Üretime devam eder; 500 ₺ zarar eder',
            'B': 'Üretime devam eder; 200 ₺ kâr eder',
            'C': 'Üretimi durdurur; 700 ₺ zarar eder',
            'D': 'Üretimi durdurur; zararı sıfırlanır',
            'E': 'Üretime devam eder; 700 ₺ zarar eder',
        },
        'A',
        "Fiyat (20) ATC'nin (25) altında ama AVC'nin (18) üzerinde olduğundan firma zarar eder ancak değişken maliyetini karşılayıp sabit maliyetin bir kısmını çıkardığı için **üretime devam eder**. Zarar = (20 − 25) × 100 = **500 ₺**. Durdursaydı zarar, sabit maliyetin tamamı olan (25 − 18) × 100 = 700 ₺ olurdu.",
        'Mikroekonomi: tam rekabet ve kâr',
    ),
    # düzey 2
    '0021': patch(
        'Bir ilacın fiyatı %10 artırıldığında talep edilen miktar %4 azalmıştır. Talebin fiyat esnekliği ve tüketicilerin bu ilaca yaptığı toplam harcamadaki değişim aşağıdakilerden hangisidir?',
        {
            'A': '2,5; talep elastiktir ve toplam harcama azalır',
            'B': '2,5; talep elastiktir ve toplam harcama artar',
            'C': '0,4; talep inelastiktir ve toplam harcama azalır',
            'D': '0,4; talep birim esnektir ve toplam harcama değişmez',
            'E': '0,4; talep inelastiktir ve toplam harcama artar',
        },
        'E',
        "Esneklik = %4 / %10 = **0,4** (mutlak değer). Esneklik 1'den küçük olduğunda fiyat artışı miktarı oransal olarak daha az azaltır; bu nedenle **toplam harcama (satıcının hasılatı) artar**. Zorunlu ilaçlar gibi ikamesi az mallarda talep genellikle inelastiktir.",
        'Mikroekonomi: esneklik ve toplam harcama',
    ),
    # düzey 2
    '0022': patch(
        'Giffen malına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Düşük maldır.\n\nII. Fiyatı düştüğünde talep edilen miktar azalır.\n\nIII. Negatif gelir etkisi, ikame etkisinden büyüktür.\n\nIV. Talep eğrisi negatif eğimlidir.',
        {
            'A': 'I ve II',
            'B': 'I, II, III ve IV',
            'C': 'I, II ve III',
            'D': 'II ve IV',
            'E': 'I, III ve IV',
        },
        'C',
        'Giffen malı özel bir **düşük maldır** (I). Fiyat düşünce ikame etkisi tüketimi artırmaya çalışır, ama reel gelirdeki artışın negatif gelir etkisi bundan **büyük** olduğu için (III) talep edilen miktar **azalır** (II). Bu nedenle Giffen malının talep eğrisi **pozitif** eğimlidir (IV yanlış).',
        'Mikroekonomi: Giffen malı',
    ),
    # düzey 2
    '0023': patch(
        "Bir piyasada arz fonksiyonu P = 4 + 2Q biçimindedir. Piyasa fiyatı 16 ₺ ise üretici fazlası kaç ₺'dir?",
        {
            'A': '36',
            'B': '60',
            'C': '48',
            'D': '72',
            'E': '96',
        },
        'A',
        'P = 16 iken 16 = 4 + 2Q → Q = 6. Üretici fazlası, fiyat çizgisinin altında ve arz eğrisinin üzerinde kalan üçgendir: ½ × (16 − 4) × 6 = **36**. 72, üçgen yerine dikdörtgen alınmasının sonucudur.',
        'Mikroekonomi: üretici fazlası',
    ),
    # düzey 2
    '0024': patch(
        'Bir piyasada talep ve arz eğrileri aynı anda sağa kaymıştır. Yeni dengeye ilişkin aşağıdakilerden hangisi kesin olarak söylenebilir?',
        {
            'A': 'Denge fiyatı artar; miktar değişmez',
            'B': 'Denge miktarı artar; fiyatın yönü kaymaların büyüklüğüne bağlıdır',
            'C': 'Denge fiyatı düşer; miktarın yönü kaymaların büyüklüğüne bağlıdır',
            'D': 'Denge fiyatı ve miktarı birlikte artar',
            'E': 'Denge miktarı azalır; fiyat artar',
        },
        'B',
        'Talep artışı fiyatı ve miktarı artırır; arz artışı miktarı artırıp fiyatı düşürür. İkisinde de miktar arttığı için **denge miktarı kesin olarak artar**. Fiyat ise talep artışı büyükse yükselir, arz artışı büyükse düşer; yönü **belirsizdir**.',
        'Mikroekonomi: piyasa dengesinin değişimi',
    ),
    # düzey 3
    '0025': patch(
        "Fayda fonksiyonu U = 3X + Y olan bir tüketicinin geliri 100 ₺, X malının fiyatı 4 ₺, Y malının fiyatı 1 ₺'dir. Tüketicinin faydasını en yükseklettiği tüketim bileşimi aşağıdakilerden hangisidir?",
        {
            'A': 'X = 20, Y = 20',
            'B': 'X = 12,5, Y = 50',
            'C': 'X = 25, Y = 0',
            'D': 'X = 0, Y = 100',
            'E': 'X = 10, Y = 60',
        },
        'D',
        "Doğrusal fayda fonksiyonunda mallar **tam ikamedir**; tüketici liraya düşen faydası yüksek olan malı seçer. X için 3/4 = 0,75, Y için 1/1 = 1 fayda/₺ olduğundan tüm gelir Y'ye harcanır: **X = 0, Y = 100** (köşe çözümü). Bütçenin tamamı X'e harcansaydı (X = 25) fayda 75, Y'ye harcanınca 100 olur.",
        'Mikroekonomi: tam ikame mallar',
    ),
    # düzey 2
    '0026': patch(
        "Aşağıdaki ifadelerden hangileri bütçe doğrusuna ilişkin doğrudur?\n\nI. Fiyatlar sabitken gelir artarsa bütçe doğrusu dışa doğru paralel kayar.\n\nII. Gelir ve Y'nin fiyatı sabitken X'in fiyatı düşerse doğru X ekseni üzerinde dışa doğru döner.\n\nIII. Gelir sabitken iki malın fiyatı aynı oranda artarsa bütçe doğrusu dışa doğru paralel kayar.",
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'A',
        "Gelir artışı eğimi (−Px/Py) değiştirmeden doğruyu dışa kaydırır (I). X'in fiyatı düşünce X eksenindeki kesim noktası (M/Px) büyür, Y eksenindeki nokta sabit kalır; doğru dışa döner (II). Gelir sabitken fiyatlar aynı oranda artarsa eğim aynı kalır ama kesim noktaları küçülür; doğru **içe** doğru paralel kayar (III yanlış).",
        'Mikroekonomi: bütçe doğrusu',
    ),
    # düzey 1
    '0027': patch(
        'Standart tercih varsayımları altında farksızlık eğrilerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Orijinden uzaklaştıkça daha yüksek bir fayda düzeyini gösterir',
            'B': 'Eğimi marjinal ikame oranını gösterir',
            'C': 'Negatif eğimlidir',
            'D': 'Orijine göre dışbükeydir',
            'E': 'Farklı fayda düzeylerini gösteren iki eğri birbirini kesebilir',
        },
        'E',
        'Farksızlık eğrileri negatif eğimli, azalan marjinal ikame oranı nedeniyle orijine göre dışbükey ve orijinden uzaklaştıkça daha yüksek faydayı gösterir. İki eğri **kesişemez**: kesişme noktası iki farklı fayda düzeyine aynı anda ait olurdu ve geçişlilik varsayımı bozulurdu.',
        'Mikroekonomi: farksızlık eğrileri',
    ),
    # düzey 1
    '0028': patch(
        'Fiyatı yükseldikçe gösteriş amacıyla daha çok talep edilen pahalı mücevher ve lüks saatler gibi mallara ne ad verilir?',
        {
            'A': 'Düşük mallar',
            'B': 'Giffen malları',
            'C': 'Zorunlu mallar',
            'D': 'Veblen malları',
            'E': 'Tamamlayıcı mallar',
        },
        'D',
        '**Veblen malları**, yüksek fiyatın statü göstergesi olması nedeniyle fiyat arttıkça daha çok talep edilen gösteriş mallarıdır. Giffen malları ise fiyatı artınca, düşük mal olmaları ve güçlü gelir etkisi nedeniyle daha çok talep edilen temel tüketim mallarıdır.',
        'Mikroekonomi: talep kanununun istisnaları',
    ),
    # düzey 2
    '0029': patch(
        'Üretim fonksiyonu türlerine ilişkin aşağıdaki eşleştirmelerden (ikame esnekliği ve eşürün eğrisinin biçimi) hangisi yanlıştır?',
        {
            'A': 'Leontief (sabit oranlı) üretimde eşürün eğrisi – L biçimli',
            'B': 'Doğrusal (tam ikame) – Sonsuz',
            'C': 'Leontief (sabit oranlı) – Sonsuz',
            'D': 'Doğrusal üretimde eşürün eğrisi – Düz çizgi',
            'E': 'Cobb-Douglas – 1',
        },
        'C',
        'Leontief (sabit oranlı) fonksiyonda faktörler belirli oranda birlikte kullanılır, birbirinin yerine geçemez; ikame esnekliği **sıfırdır** ve eşürün eğrisi L biçimlidir. Cobb-Douglas fonksiyonunda ikame esnekliği 1, doğrusal fonksiyonda sonsuzdur ve eşürün eğrisi düz çizgidir.',
        'Mikroekonomi: ikame esnekliği',
    ),
    # düzey 2
    '0030': patch(
        'Kısa dönem toplam maliyet fonksiyonu TC = 50 + 10Q + Q² olan bir firmanın 15 birim üretimdeki marjinal maliyeti kaçtır?',
        {
            'A': '425',
            'B': '40',
            'C': '25',
            'D': '28,3',
            'E': '10',
        },
        'B',
        'Marjinal maliyet, toplam maliyetin üretime göre türevidir: MC = 10 + 2Q. Q = 15 için MC = 10 + 30 = **40**. 425 bu düzeydeki toplam maliyet (50 + 150 + 225), 28,3 ortalama toplam maliyet (425 / 15), 25 ise türevin hatalı alınmasının (10 + Q) sonucudur.',
        'Mikroekonomi: marjinal maliyet',
    ),
    # düzey 3
    '0031': patch(
        "Tam rekabetçi bir firmanın kısa dönem toplam maliyet fonksiyonu TC = Q³ − 6Q² + 20Q + 100'dür. Piyasa fiyatı hangi düzeyin altına düşerse firma kısa dönemde üretimi durdurur?",
        {
            'A': '3 ₺',
            'B': '20 ₺',
            'C': '100 ₺',
            'D': '11 ₺',
            'E': '9 ₺',
        },
        'D',
        'Firma, fiyat ortalama değişken maliyetin (AVC) minimumunun altına düşerse üretimi durdurur. Değişken maliyet Q³ − 6Q² + 20Q olduğundan AVC = Q² − 6Q + 20. Minimum noktada 2Q − 6 = 0 → Q = 3; AVC = 9 − 18 + 20 = **11 ₺**. Sabit maliyet (100) kısa dönemde batık olduğu için kapatma kararını etkilemez.',
        'Mikroekonomi: kapatma noktası',
    ),
    # düzey 3
    '0032': patch(
        "Talep eğrisi P = 120 − 2Q ve marjinal maliyeti sabit 20 ₺ olan bir piyasada, tam rekabet yerine monopol dengesi oluşması hâlinde ortaya çıkan dara (refah) kaybı kaç ₺'dir?",
        {
            'A': '2.500',
            'B': '625',
            'C': '300',
            'D': '1.250',
            'E': '1.225',
        },
        'B',
        'Monopol dengesi Q = 25, P = 70; tam rekabet dengesi P = MC = 20 → Q = 50. Dara kaybı, iki miktar arasındaki üçgendir: ½ × (70 − 20) × (50 − 25) = ½ × 50 × 25 = **625**. 1.250, üçgen yerine dikdörtgen alınmasının sonucudur ve monopolün tüketiciden aktardığı rantın (50 × 25) tutarına eşittir.',
        'Mikroekonomi: monopolün refah kaybı',
    ),
    # düzey 2
    '0033': patch(
        "Bir firmanın ürün fiyatı 50 ₺, marjinal maliyeti 30 ₺'dir. Firmanın piyasa gücünü ölçen Lerner endeksi kaçtır?",
        {
            'A': '1,67',
            'B': '20',
            'C': '0,6',
            'D': '0,25',
            'E': '0,4',
        },
        'E',
        "**Lerner endeksi** = (P − MC) / P = (50 − 30) / 50 = **0,4**. Tam rekabette P = MC olduğu için endeks sıfırdır; değer 1'e yaklaştıkça piyasa gücü artar. Kâr maksimize eden bir firmada endeks, talep esnekliğinin tersine (1/|e|) eşittir; burada |e| = 2,5.",
        'Mikroekonomi: Lerner endeksi',
    ),
    # düzey 1
    '0034': patch(
        'Bir monopolün her tüketiciye her birimi, o tüketicinin ödemeye razı olduğu en yüksek fiyattan satabildiği durumda aşağıdakilerden hangisi gerçekleşir?',
        {
            'A': 'Tüketici fazlasının tamamı monopole geçer; dara kaybı oluşmaz',
            'B': 'Dara kaybı en yüksek düzeye çıkar',
            'C': 'Monopol fiyatı marjinal maliyete eşitler, kâr sıfırlanır',
            'D': 'Tüketici fazlası artar; üretim azalır',
            'E': 'Üretim, tek fiyatlı monopolden daha az olur',
        },
        'A',
        '**Birinci derece (tam)** fiyat farklılaştırmasında monopol, talep eğrisinin marjinal maliyeti kestiği noktaya kadar üretir; bu nedenle üretim tam rekabet düzeyindedir ve **dara kaybı oluşmaz**. Ancak tüketici fazlasının **tamamı** üreticiye aktarılır.',
        'Mikroekonomi: birinci derece fiyat farklılaştırması',
    ),
    # düzey 2
    '0035': patch(
        'İki firma reklam kararı vermektedir. İkisi de reklam yapmazsa her biri 50, ikisi de yaparsa 30 kâr elde etmektedir. Yalnız biri reklam yaparsa reklam yapan 60, yapmayan 20 kâr elde etmektedir. Nash dengesi aşağıdakilerden hangisidir?',
        {
            'A': 'Nash dengesi yoktur',
            'B': 'Firmalar dönüşümlü olarak reklam yapar',
            'C': 'Bir firma reklam yapar, diğeri yapmaz; kârlar 60 ve 20 olur',
            'D': 'İki firma da reklam yapmaz; her biri 50 kâr elde eder',
            'E': 'İki firma da reklam yapar; her biri 30 kâr elde eder',
        },
        'E',
        "Rakip reklam yapmıyorsa reklam yapmak 60 > 50, yapıyorsa 30 > 20 sağlar; reklam yapmak her firma için **baskın stratejidir**. Nash dengesi (reklam, reklam) ve kârlar 30'ar olur. İkisi birlikte daha iyi durumda olabilecekken (50'şer) buna ulaşamaz: **tutsak ikilemi**.",
        'Mikroekonomi: oyun teorisi',
    ),
    # düzey 1
    '0036': patch(
        'Artan fırsat maliyetleri kanununun geçerli olduğu bir ekonomide üretim imkânları eğrisinin biçimi aşağıdakilerden hangisidir?',
        {
            'A': 'Yatay bir doğru',
            'B': 'Orijine göre dışbükey',
            'C': 'Negatif eğimli düz bir doğru',
            'D': 'Orijine göre içbükey',
            'E': 'Pozitif eğimli bir doğru',
        },
        'D',
        'Bir malın üretimi artırıldıkça ondan vazgeçilen diğer mal miktarı giderek arttığında eğrinin eğimi mutlak değerce büyür ve eğri **orijine göre içbükey** olur. Fırsat maliyeti sabit olsaydı üretim imkânları eğrisi düz bir doğru olurdu.',
        'Mikroekonomi: üretim imkânları eğrisi',
    ),
    # düzey 2
    '0037': patch(
        'Doğrusal ve negatif eğimli bir talep eğrisi boyunca fiyat esnekliğine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Eğrinin üst kesiminde elastik, orta noktasında birim esnek, alt kesiminde inelastiktir',
            'B': 'Eğrinin üst kesiminde inelastik, alt kesiminde elastiktir',
            'C': "Esneklik her noktada 1'e eşittir",
            'D': 'Eğri boyunca esneklik sabittir ve eğime eşittir',
            'E': 'Esneklik eğrinin eğimine eşittir, fiyat düzeyinden bağımsızdır',
        },
        'A',
        'Doğrusal talepte eğim sabittir ama esneklik (eğim × P/Q) P/Q oranına bağlıdır: yüksek fiyat ve düşük miktarda P/Q büyük olduğu için talep **elastik**, orta noktada **birim esnek**, düşük fiyatlarda **inelastiktir**. Sabit esneklik ancak P · Q = sabit türünden eğrisel talepte görülür.',
        'Mikroekonomi: talep esnekliği ve eğim',
    ),
    # düzey 2
    '0038': patch(
        'Eşürün (izokuant) eğrisinin eğimini gösteren marjinal teknik ikame oranı (MRTS_LK) aşağıdakilerden hangisine eşittir?',
        {
            'A': 'Sermayenin marjinal ürününün emeğin marjinal ürününe oranına',
            'B': 'Emeğin ortalama ürününün sermayenin ortalama ürününe oranına',
            'C': 'Emeğin marjinal ürününün sermayenin marjinal ürününe oranına',
            'D': 'Toplam ürünün emek miktarına oranına',
            'E': 'Ücretin sermayenin fiyatına oranına',
        },
        'C',
        'Eşürün eğrisi boyunca üretim sabittir: MP_L · ΔL + MP_K · ΔK = 0. Buradan eğim −ΔK/ΔL = **MP_L / MP_K** olur. Ücretin sermaye fiyatına oranı (w/r) eşmaliyet doğrusunun eğimidir; optimumda ikisi eşitlenir.',
        'Mikroekonomi: eşürün eğrisi',
    ),
    # düzey 2
    '0039': patch(
        'Bir tüketicinin X malından elde ettiği toplam fayda TU = 30X − X² biçimindedir. Tüketici 10. birimi tüketirken marjinal fayda ve toplam faydanın seyri aşağıdakilerden hangisidir?',
        {
            'A': "Marjinal fayda 200'dür; toplam fayda artmaya devam eder",
            'B': "Marjinal fayda 10'dur; toplam fayda artmaya devam eder",
            'C': "Marjinal fayda 10'dur; toplam fayda azalmaya başlamıştır",
            'D': "Marjinal fayda 0'dır; toplam fayda en yüksek düzeydedir",
            'E': "Marjinal fayda −10'dur; toplam fayda azalmaktadır",
        },
        'B',
        "Marjinal fayda MU = dTU/dX = 30 − 2X; X = 10 için MU = **10**. Marjinal fayda pozitif olduğu sürece toplam fayda **artmaya devam eder**; artış X = 15'te (MU = 0, doyum noktası) durur. 200, 10. birimdeki toplam faydadır (300 − 100).",
        'Mikroekonomi: marjinal fayda',
    ),
    # düzey 2
    '0040': patch(
        'Kahve ile şeker tamamlayıcı, kahve ile çay ikame mallar olsun. Kahve talebini sağa kaydıran gelişme aşağıdakilerden hangisidir?',
        {
            'A': 'Tüketicilerin kahve tercihinin azalması',
            'B': 'Şekerin fiyatının artması',
            'C': 'Kahvenin fiyatının düşmesi',
            'D': 'Çayın fiyatının artması',
            'E': 'Kahve üretim maliyetlerinin düşmesi',
        },
        'D',
        'İkame malın (çay) fiyatı artınca tüketiciler kahveye yönelir; kahve talebi **sağa kayar**. Tamamlayıcı malın (şeker) fiyatının artması kahve talebini azaltır. Kahvenin kendi fiyatının düşmesi eğri üzerinde hareket, maliyetlerin düşmesi ise arzda kaymadır.',
        'Mikroekonomi: talebi kaydıran etkenler',
    ),
    # düzey 2
    '0041': patch(
        'Tüketicilerin geliri %10 arttığında bir malın talep edilen miktarı %15 artmıştır. Bu mal aşağıdakilerden hangisidir?',
        {
            'A': 'Zorunlu (normal) mal',
            'B': 'Lüks mal',
            'C': 'Tamamlayıcı mal',
            'D': 'Giffen malı',
            'E': 'Düşük mal',
        },
        'B',
        "Gelir esnekliği = %15 / %10 = 1,5. Gelir esnekliği **1'den büyük** olan mallar **lüks** mallardır; talepleri gelirden daha hızlı artar. 0 ile 1 arasındaki esneklik zorunlu malı, negatif esneklik düşük malı gösterir. Tamamlayıcılık çapraz esneklikle ölçülür.",
        'Mikroekonomi: gelir esnekliği',
    ),
    # düzey 2
    '0042': patch(
        "Bir piyasada talep fonksiyonu P = 50 − Q biçimindedir. Piyasa fiyatı 20 ₺ ise tüketici fazlası kaç ₺'dir?",
        {
            'A': '450',
            'B': '600',
            'C': '1050',
            'D': '900',
            'E': '750',
        },
        'A',
        'P = 20 iken Q = 30. Tüketici fazlası, talep eğrisinin altında ve fiyat çizgisinin üzerinde kalan üçgendir: ½ × (50 − 20) × 30 = **450**. 900 üçgen yerine dikdörtgen alınmasının sonucudur.',
        'Mikroekonomi: tüketici fazlası',
    ),
    # düzey 2
    '0043': patch(
        "Bir malın arz fonksiyonu Qs = −10 + 5P'dir. Fiyat 6 ₺ iken arzın fiyat esnekliği kaçtır?",
        {
            'A': '0,67',
            'B': '3',
            'C': '1',
            'D': '5',
            'E': '1,5',
        },
        'E',
        'P = 6 iken Qs = −10 + 30 = 20. Arz esnekliği = (dQ/dP) × (P/Q) = 5 × 6 / 20 = **1,5**; arz bu noktada esnektir. 0,67 oranın ters kurulmasından, 5 ise yalnız eğimin alınmasından kaynaklanır.',
        'Mikroekonomi: arz esnekliği',
    ),
    # düzey 1
    '0044': patch(
        'Hükümetin bir mal için denge fiyatının altında azami fiyat (tavan fiyat) belirlemesinin sonuçlarından biri aşağıdakilerden hangisi değildir?',
        {
            'A': 'Talep fazlası (kıtlık)',
            'B': 'Satılan miktarın azalması',
            'C': 'Arz fazlası ve stok birikimi',
            'D': 'Kuyruk ve karne gibi dağıtım yöntemleri',
            'E': 'Karaborsa eğilimi',
        },
        'C',
        'Denge fiyatının altındaki tavan fiyatta talep edilen miktar arz edilen miktarı aşar: **talep fazlası** oluşur, satılan miktar arz edilen miktarla sınırlanır ve malın dağıtımı kuyruk, karne veya karaborsa gibi yollarla gerçekleşir. **Arz fazlası** ise denge fiyatının üzerindeki taban fiyatın sonucudur.',
        'Mikroekonomi: fiyat tavanı',
    ),
    # düzey 2
    '0045': patch(
        "Bir tüketici için X malının marjinal faydası 30, fiyatı 10 ₺; Y malının marjinal faydası 40, fiyatı 20 ₺'dir. Tüketici tüm gelirini harcamaktadır. Faydasını artırmak için ne yapmalıdır?",
        {
            'A': 'İki malın tüketimini de aynı oranda azaltmalıdır',
            'B': 'Mevcut bileşim dengededir, değişiklik gerekmez',
            'C': 'İki malın tüketimini de aynı oranda artırmalıdır',
            'D': 'X tüketimini artırıp Y tüketimini azaltmalıdır',
            'E': 'Y tüketimini artırıp X tüketimini azaltmalıdır',
        },
        'D',
        "Denge koşulu MUx/Px = MUy/Py'dir. Burada MUx/Px = 30/10 = 3, MUy/Py = 40/20 = 2. X'e harcanan son lira daha fazla fayda sağladığından tüketici **X'i artırıp Y'yi azaltmalıdır**; azalan marjinal fayda nedeniyle oranlar eşitlenene kadar bu sürer. Gelir tamamen harcandığı için iki malı birlikte artırmak mümkün değildir.",
        'Mikroekonomi: tüketici dengesi',
    ),
    # düzey 2
    '0046': patch(
        'Geliri 120 ₺, X malının fiyatı 4 ₺, Y malının fiyatı 6 ₺ olan bir tüketicinin bütçe doğrusuna (Y dikey eksende) ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Eğim −3/2'dir; en fazla 20 birim Y alınabilir",
            'B': "Eğim −2/3'tür; en fazla 30 birim X alınabilir",
            'C': "Eğim −1/3'tür; en fazla 30 birim X alınabilir",
            'D': "Eğim −2/3'tür; en fazla 20 birim X alınabilir",
            'E': "Eğim −3/2'dir; en fazla 30 birim X alınabilir",
        },
        'B',
        "Bütçe doğrusu 4X + 6Y = 120. Y dikey eksendeyken eğim = −Px/Py = −4/6 = **−2/3**. Tüm gelir X'e harcanırsa 120/4 = **30** birim, Y'ye harcanırsa 120/6 = 20 birim alınır.",
        'Mikroekonomi: bütçe doğrusu',
    ),
    # düzey 2
    '0047': patch(
        'Normal bir malın fiyatı düştüğünde gelir ve ikame etkilerine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gelir etkisi miktarı artırır, ikame etkisi azaltır',
            'B': 'İkame etkisi miktarı artırır, gelir etkisi azaltır',
            'C': 'İki etki de talep edilen miktarı azaltır',
            'D': 'Gelir etkisi sıfırdır, miktarı ikame etkisi belirler',
            'E': 'İki etki de talep edilen miktarı artırır',
        },
        'E',
        'Fiyat düşünce mal göreli olarak ucuzlar; **ikame etkisi** her zaman miktarı artırır. Reel gelir yükseldiği için **gelir etkisi**, normal malda talebi yine artırır. Düşük malda gelir etkisi ters yöndedir; Giffen malında ise bu ters etki ikame etkisini aşar.',
        'Mikroekonomi: gelir ve ikame etkisi',
    ),
    # düzey 1
    '0048': patch(
        'Diğer üretim faktörleri sabitken bir faktörün miktarı artırıldıkça, belirli bir noktadan sonra bu faktörün marjinal ürününün azalmasını ifade eden ilke hangisidir?',
        {
            'A': 'Ölçeğe göre azalan getiri',
            'B': 'Artan fırsat maliyeti kanunu',
            'C': 'Azalan verimler kanunu',
            'D': 'Engel kanunu',
            'E': 'Say kanunu',
        },
        'C',
        '**Azalan verimler kanunu** kısa döneme ilişkindir: en az bir faktör sabitken değişken faktör artırıldıkça marjinal ürünü sonunda azalır. **Ölçeğe göre getiri** ise uzun dönemde tüm faktörlerin aynı oranda artırılmasıyla çıktının nasıl değiştiğini inceler.',
        'Mikroekonomi: azalan verimler',
    ),
    # düzey 3
    '0049': patch(
        "Üretim fonksiyonu Q = 2L + 3K olan bir firma için emeğin birim fiyatı 10 ₺, sermayenin birim fiyatı 20 ₺'dir. Firma 60 birim üretimi en düşük maliyetle hangi faktör bileşimiyle gerçekleştirir?",
        {
            'A': 'L = 0, K = 20',
            'B': 'L = 30, K = 20',
            'C': 'L = 15, K = 10',
            'D': 'L = 30, K = 0',
            'E': 'L = 6, K = 16',
        },
        'D',
        'Doğrusal üretimde faktörler tam ikamedir; firma liraya düşen marjinal ürünü yüksek olan faktörü kullanır. Emek için 2/10 = 0,2, sermaye için 3/20 = 0,15 birim/₺ olduğundan yalnız emek kullanılır: 2L = 60 → **L = 30, K = 0**; maliyet 300 ₺. Yalnız sermaye kullanılsaydı K = 20 ve maliyet 400 ₺ olurdu.',
        'Mikroekonomi: maliyet minimizasyonu',
    ),
    # düzey 3
    '0050': patch(
        "Tam rekabet piyasasındaki bir firmanın toplam maliyet fonksiyonu TC = Q² + 6Q + 20, malın piyasa fiyatı 30 ₺'dir. Firmanın kârı en yükselten üretim düzeyi ve bu düzeydeki kârı aşağıdakilerden hangisidir?",
        {
            'A': 'Q = 12; kâr 124 ₺',
            'B': 'Q = 12; kâr 144 ₺',
            'C': 'Q = 15; kâr 115 ₺',
            'D': 'Q = 24; kâr 0 ₺',
            'E': 'Q = 12; kâr 360 ₺',
        },
        'A',
        'Tam rekabette kâr maksimizasyonu P = MC ile sağlanır: MC = 2Q + 6 = 30 → **Q = 12**. Hasılat = 30 × 12 = 360; toplam maliyet = 144 + 72 + 20 = 236; kâr = 360 − 236 = **124 ₺**. 360 kâr değil hasılattır.',
        'Mikroekonomi: tam rekabette firma dengesi',
    ),
    # düzey 1
    '0051': patch(
        'Aşağıdakilerden hangileri tam rekabet piyasasının varsayımlarındandır?\n\nI. Homojen ürün\n\nII. Firmaların fiyatı belirleyebilmesi\n\nIII. Piyasaya serbest giriş ve çıkış\n\nIV. Tam bilgi',
        {
            'A': 'II ve IV',
            'B': 'I, II, III ve IV',
            'C': 'I, III ve IV',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'C',
        'Tam rekabette çok sayıda alıcı ve satıcı, homojen ürün (I), serbest giriş-çıkış (III) ve tam bilgi (IV) vardır. Bu nedenle firmalar **fiyat kabul edicidir**; fiyatı piyasa belirler (II yanlış).',
        'Mikroekonomi: tam rekabet',
    ),
    # düzey 2
    '0052': patch(
        'Tam rekabet piyasasında uzun dönem dengesine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fiyat marjinal maliyetin üzerinde oluşur',
            'B': 'Firmalar ortalama maliyetin en düşük noktasının solunda üretir',
            'C': 'Firmalar pozitif ekonomik kâr elde etmeye devam eder',
            'D': 'Piyasaya giriş olmadığı için firma sayısı sabit kalır',
            'E': 'Fiyat uzun dönem ortalama maliyetin en düşük noktasına eşittir; ekonomik kâr sıfırdır',
        },
        'E',
        'Pozitif kâr yeni firmaları piyasaya çeker, zarar ise çıkışa yol açar; giriş-çıkış süreci fiyatı uzun dönem ortalama maliyetin **minimumuna** indirir. Bu noktada P = MC = min LAC ve **ekonomik kâr sıfırdır**; firmalar optimum ölçekte üretir.',
        'Mikroekonomi: tam rekabet uzun dönem',
    ),
    # düzey 2
    '0053': patch(
        'Bir sinema salonunun aynı film için öğrencilere ve emeklilere daha düşük, diğer izleyicilere daha yüksek bilet fiyatı uygulaması hangi fiyat farklılaştırmasıdır?',
        {
            'A': 'Üçüncü derece fiyat farklılaştırması',
            'B': 'Tepe yük fiyatlaması',
            'C': 'Zamanlar arası fiyat farklılaştırması',
            'D': 'Birinci derece fiyat farklılaştırması',
            'E': 'İkinci derece fiyat farklılaştırması',
        },
        'A',
        '**Üçüncü derece** fiyat farklılaştırmasında tüketiciler talep esnekliği farklı gruplara ayrılır ve her gruba farklı fiyat uygulanır; talebi daha esnek grup (öğrenci, emekli) daha düşük fiyat öder. **Birinci derece** her birimi rezervasyon fiyatından satmak, **ikinci derece** ise alınan miktara göre fiyat değiştirmektir.',
        'Mikroekonomi: fiyat farklılaştırması',
    ),
    # düzey 2
    '0054': patch(
        'Oligopol piyasasında fiyatların uzun süre değişmeden kalmasını, rakiplerin fiyat artışına uymayıp fiyat indirimine uyacağı varsayımına dayanarak açıklayan model hangisidir?',
        {
            'A': 'Bertrand modeli',
            'B': 'Dirsekli talep eğrisi modeli',
            'C': 'Fiyat liderliği (baskın firma) modeli',
            'D': 'Stackelberg modeli',
            'E': 'Cournot modeli',
        },
        'B',
        "**Sweezy'nin dirsekli talep eğrisi** modelinde firma, fiyat artırırsa rakiplerin uymayacağını (talep esnek), indirirse uyacağını (talep inelastik) varsayar. Talep eğrisinin dirsekli olması marjinal hasılat eğrisinde bir kesiklik yaratır; marjinal maliyetteki değişmeler bu aralıkta fiyatı değiştirmez.",
        'Mikroekonomi: oligopol',
    ),
    # düzey 2
    '0055': patch(
        'Kartellerin kalıcı olmakta zorlanmasının temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Kartel fiyatının marjinal maliyete eşit olması',
            'B': 'Kartelin piyasaya yeni girişi teşvik etmemesi',
            'C': 'Kartel üyelerinin toplam kârının rekabet dengesinin altında kalması',
            'D': 'Her üyenin kota üzerinde üretim yaparak kârını artırma teşviki taşıması',
            'E': 'Talep esnekliğinin kartel altında sıfıra inmesi',
        },
        'D',
        'Kartel fiyatı marjinal maliyetin çok üzerinde olduğu için her üye, diğerleri kotaya uyarken gizlice fazla üreterek kârını artırabilir. Herkes bu teşvike göre davranınca fiyat düşer ve anlaşma bozulur; bu durum tutsak ikilemiyle aynı yapıdadır.',
        'Mikroekonomi: kartel',
    ),
    # düzey 1
    '0056': patch(
        'Aşağıdakilerden hangisi monopolün ortaya çıkma nedenlerinden biri değildir?',
        {
            'A': 'Patent hakkının tek firmaya ait olması',
            'B': 'Ürünün çok sayıda yakın ikamesinin bulunması',
            'C': 'Ölçek ekonomileri nedeniyle doğal tekel oluşması',
            'D': 'Devletin tanıdığı yasal ayrıcalık',
            'E': 'Kritik bir hammaddenin tek elde toplanması',
        },
        'B',
        'Monopol; patent, kritik hammaddenin kontrolü, ölçek ekonomilerinin yol açtığı doğal tekel ve yasal ayrıcalıklar gibi **giriş engellerinden** doğar. Ürünün çok sayıda yakın ikamesinin bulunması ise firmanın piyasa gücünü azaltır; tekelci rekabet veya tam rekabete yakın bir yapıya işaret eder.',
        'Mikroekonomi: monopolün nedenleri',
    ),
    # düzey 2
    '0057': patch(
        'Talebin tam inelastik (dikey) olduğu bir mala birim başına vergi konulursa aşağıdakilerden hangisi gerçekleşir?',
        {
            'A': 'Fiyat değişmez; satılan miktar azalır',
            'B': 'Verginin tamamı üreticilerde kalır; miktar azalır',
            'C': 'Dara kaybı en yüksek düzeye çıkar',
            'D': 'Vergi yükü eşit paylaşılır; miktar azalır',
            'E': 'Verginin tamamı tüketicilere yansır; satılan miktar değişmez',
        },
        'E',
        'Talep tam inelastik olduğunda tüketiciler fiyat ne olursa olsun aynı miktarı satın alır; arz eğrisi vergi kadar yukarı kaydığında fiyat vergi tutarı kadar artar ve **yükün tamamını tüketiciler** taşır. Miktar değişmediği için **dara kaybı oluşmaz**.',
        'Mikroekonomi: vergi ve piyasa',
    ),
    # düzey 3
    '0058': patch(
        'Talep eğrisi P = 100 − Q, arz eğrisi P = 20 + Q olan bir piyasada üreticilere birim başına 20 ₺ sübvansiyon verilmiştir. Yeni denge miktarı ve tüketicilerin ödediği fiyat aşağıdakilerden hangisidir?',
        {
            'A': 'Q = 50; P = 50 ₺',
            'B': 'Q = 40; P = 60 ₺',
            'C': 'Q = 60; P = 40 ₺',
            'D': 'Q = 50; P = 70 ₺',
            'E': 'Q = 45; P = 55 ₺',
        },
        'A',
        "Sübvansiyon arz eğrisini 20 ₺ aşağı kaydırır: P = Q. Yeni denge 100 − Q = Q → **Q = 50**, tüketici fiyatı **P = 50 ₺**; üreticinin eline geçen 50 + 20 = 70 ₺'dir. Sübvansiyon öncesi denge 100 − Q = 20 + Q → Q = 40, P = 60 ₺ idi.",
        'Mikroekonomi: sübvansiyon ve piyasa',
    ),
    # düzey 2
    '0059': patch(
        'Bir bölgede tek işveren olan büyük bir madenin işgücü piyasasındaki durumuna ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Oligopsondur; ücreti işçiler belirler',
            'B': 'Tam rekabettir; ücret emeğin marjinal ürün değerine eşittir',
            'C': 'Monopsondur; rekabetçi piyasaya göre daha az işçi istihdam edip daha düşük ücret öder',
            'D': 'Monopoldür; rekabetçi piyasaya göre daha fazla işçi istihdam eder',
            'E': 'Monopsondur; rekabetçi piyasaya göre daha yüksek ücret ödeyerek bölgedeki işçilerin çoğunu çeker',
        },
        'C',
        'Tek alıcılı piyasa **monopsondur**. Monopsoncu işveren, daha fazla işçi çalıştırmak için ücreti yükseltmek zorunda olduğunu bildiğinden istihdamı rekabetçi düzeyin **altında** tutar ve ücreti emeğin marjinal ürün değerinin **altında** belirler.',
        'Mikroekonomi: monopson',
    ),
    # düzey 1
    '0060': patch(
        "Tüketici tercihlerine ilişkin 'daha çok, daha azdan iyidir' biçiminde ifade edilen varsayım aşağıdakilerden hangisidir?",
        {
            'A': 'Dışbükeylik',
            'B': 'Doymazlık',
            'C': 'Geçişlilik',
            'D': 'Süreklilik',
            'E': 'Tamlık',
        },
        'B',
        '**Doymazlık (monotonluk)** varsayımına göre tüketici bir malın daha fazlasını her zaman tercih eder; bu nedenle marjinal fayda pozitiftir ve farksızlık eğrileri negatif eğimlidir. Geçişlilik tercihlerin tutarlılığını, tamlık her iki sepetin karşılaştırılabilmesini ifade eder.',
        'Mikroekonomi: tüketici tercihleri',
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
    print(f"1 paket / {len(PATCHES)} soru ('Mikroekonomi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
