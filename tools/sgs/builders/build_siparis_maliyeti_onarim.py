#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Siparis Maliyeti — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

60 soru (26'si hesapli) korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 24 mutlak ifadeli celdirici ayni dogruluk degerini koruyacak bicimde yeniden yazildi (0048/0049'da 'duzeltme gerektirmez' celdiricileri ters yonlu duzeltmeye cevrildi). Kor ogrenci %33 -> %23 (UYARI kapandi).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Maliyet muhasebesi - siparis maliyeti sistemi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliyet_muhasebesi/siparis_maliyeti.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (kavram-sipariş; sınav stiline kalibre)'
ONEK = "mmuh-siparis-gen-"


def patch(stem, options, answer, solution, ref='Maliyet muhasebesi - sipariş maliyeti sistemi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Sipariş maliyeti sistemi aşağıdaki üretim biçimlerinden hangisinde kullanılır?',
        {
            'A': 'Hizmet üreten, stok tutmayan işletmelerin standart maliyet hesaplamalarında',
            'B': 'Üretim faaliyeti bulunmayan, alım satım yapan ticaret işletmelerinde',
            'C': 'Tarımsal ürün yetiştiren işletmelerin sürekli ve tek tip üretiminde',
            'D': 'Birbirinden farklı, ayırt edilebilir, sipariş veya partiler halinde üretim (inşaat, gemi, mobilya, matbaa)',
            'E': 'Birbirinin aynı olan mamullerin sürekli ve kitle halinde akış tipi üretimi (şeker, çimento, un, akaryakıt)',
        },
        'D',
        '**Sipariş maliyeti sistemi**, birbirinden farklı, ayırt edilebilir, **sipariş/parti** halinde üretim yapan işletmelerde kullanılır (inşaat, gemi, mobilya, matbaa, özel makine). Sürekli/kitle üretimde ise safha maliyeti kullanılır.',
        'Maliyet muhasebesi - sipariş maliyeti sistemi',
    ),
    # düzey 2
    '0002': patch(
        'Bir siparişin maliyet kartında toplanan üç temel maliyet unsuru hangileridir?',
        {
            'A': 'Direkt ilk madde ve malzeme + direkt işçilik + (yüklenen) genel üretim giderleri',
            'B': 'Ödenen faiz giderleri + tahakkuk eden vergiler + duran varlık amortisman payları',
            'C': 'Dönem içi malzeme alışları + alıştan iadeler + satıcıdan alınan iskonto tutarları',
            'D': 'Fabrika binası kira gideri + tüketilen enerji gideri + kullanılan su gideri',
            'E': 'Satış giderleri + pazarlama satış dağıtım giderleri + genel yönetim giderleri toplamı',
        },
        'A',
        'Sipariş maliyet kartında **direkt ilk madde ve malzeme (DİMM) + direkt işçilik (DİG) + yüklenen genel üretim giderleri (GÜG)** toplanır. Bu üçünün toplamı siparişin üretim maliyetidir.',
        'Maliyet muhasebesi - sipariş maliyeti unsurları',
    ),
    # düzey 3
    '0003': patch(
        "Bir işletmenin dönem başında bütçelediği genel üretim gideri 600.000 ₺, tahmini makine saati 30.000'dir. 101 no'lu siparişin maliyet kartında DİMM 50.000 ₺, DİG 30.000 ₺ yer almakta olup sipariş 1.000 makine saati kullanmıştır. Siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '680.000',
            'B': '90.000',
            'C': '120.000',
            'D': '80.000',
            'E': '100.000',
        },
        'E',
        "Yükleme oranı = bütçelenen GÜG ÷ tahmini makine saati = 600.000 ÷ 30.000 = 20 ₺/saat. Siparişe yüklenen GÜG = 1.000 × 20 = 20.000 ₺. Toplam maliyet = DİMM + DİG + yüklenen GÜG = 50.000 + 30.000 + 20.000 = **100.000 ₺**. (GÜG'ü atlamak 80.000 ₺ verir.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0004': patch(
        "Bir dönemde tamamlanan iki sipariş vardır: 101 no'lu siparişin toplam maliyeti 100.000 ₺ olup 500 adet, 102 no'lu siparişin toplam maliyeti 160.000 ₺ olup 400 adet mamul üretilmiştir. 102 no'lu siparişin birim maliyeti, 101 no'lu siparişin birim maliyetinden kaç ₺ FAZLADIR?",
        {
            'A': '600',
            'B': '100',
            'C': '200',
            'D': '400',
            'E': '60.000',
        },
        'C',
        "101'in birim maliyeti = 100.000 ÷ 500 = 200 ₺; 102'nin birim maliyeti = 160.000 ÷ 400 = 400 ₺. Fark = 400 − 200 = **200 ₺**. Sipariş maliyeti sisteminde her siparişin birim maliyeti, kendi maliyet kartı ve üretim miktarına bağlı olduğundan farklılaşır.",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0005': patch(
        'Sipariş maliyeti sisteminde TAMAMLANAN bir siparişin maliyeti hangi hesaba aktarılır?',
        {
            'A': '153 TİCARİ MALLAR',
            'B': '152 MAMULLER',
            'C': '600 YURT İÇİ SATIŞLAR',
            'D': '151 YARI MAMULLER – ÜRETİM',
            'E': '710 DİREKT İLK MADDE VE MALZEME GİDERLERİ',
        },
        'B',
        'Tamamlanan siparişin üretim maliyeti **152 MAMULLER** hesabına aktarılır. Henüz tamamlanmamış siparişler ise 151 YARI MAMULLER – ÜRETİM hesabında izlenir.',
        'TDHP 152 Mamuller',
    ),
    # düzey 2
    '0006': patch(
        'Sipariş maliyeti ile safha maliyeti sistemleri arasındaki temel fark aşağıdakilerden hangisidir?',
        {
            'A': 'Sipariş maliyeti hizmet işletmelerinde, safha maliyeti sanayi işletmelerinde kullanılır',
            'B': 'İki sistem arasında maliyetin toplanması bakımından fark yoktur',
            'C': 'Safha maliyetinde birim maliyet hesaplanmaz; birim maliyet sipariş maliyetine özgüdür',
            'D': 'Sipariş maliyetinde maliyet unsuru ayrımı yapılmaz; bu ayrım safha maliyetine özgüdür',
            'E': 'Sipariş maliyetinde maliyet her siparişe/işe göre; safha maliyetinde ise üretim aşamalarına (safhalara) göre toplanır',
        },
        'E',
        'Temel fark maliyetin toplanma biriminde: **sipariş maliyetinde** maliyet her **sipariş/iş** için ayrı; **safha maliyetinde** ise üretim **aşamaları (safhalar)** itibarıyla toplanır.',
        'Maliyet muhasebesi - sipariş vs safha',
    ),
    # düzey 3
    '0007': patch(
        'Sipariş maliyeti sistemi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Her sipariş için ayrı bir maliyet kartı açılır.\n\nII. Sipariş birim maliyeti = sipariş toplam maliyeti ÷ sipariş adedi.\n\nIII. DİMM ve DİG siparişlere yükleme oranıyla, GÜG ise siparişe doğrudan yüklenir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'B',
        '**III yanlıştır:** İlişki terstir; DİMM (direkt ilk madde ve malzeme) ve DİG (direkt işçilik) her siparişe DOĞRUDAN izlenir, endirekt nitelikteki GÜG ise önceden belirlenen YÜKLEME ORANIYLA yüklenir. **I** her siparişe ayrı maliyet kartı açılması ve **II** birim maliyet = toplam maliyet ÷ adet olması doğrudur. Doğru cevap **I ve II**.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 3
    '0008': patch(
        "Bir işletmenin tahmini genel üretim gideri 300.000 ₺, tahmini direkt işçilik saati 15.000'dir. 106 no'lu siparişin DİMM'i 40.000 ₺, DİG'i 24.000 ₺ olup sipariş 800 direkt işçilik saati kullanmıştır. Siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '64.000',
            'B': '364.000',
            'C': '80.000',
            'D': '88.000',
            'E': '96.000',
        },
        'C',
        'Yükleme oranı = 300.000 ÷ 15.000 = 20 ₺/direkt işçilik saati. Yüklenen GÜG = 800 × 20 = 16.000 ₺. Toplam maliyet = 40.000 + 24.000 + 16.000 = **80.000 ₺**.',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0009': patch(
        "Bir işletmenin tahmini genel üretim gideri 240.000 ₺, tahmini direkt işçilik tutarı 480.000 ₺'dir. 107 no'lu siparişin DİMM'i 90.000 ₺, DİG'i 70.000 ₺ olduğuna göre siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '230.000',
            'B': '400.000',
            'C': '160.000',
            'D': '195.000',
            'E': '180.000',
        },
        'D',
        'Direkt işçilik tutarı esaslı yükleme oranı = 240.000 ÷ 480.000 = %50. Yüklenen GÜG = 70.000 × %50 = 35.000 ₺. Toplam maliyet = 90.000 + 70.000 + 35.000 = **195.000 ₺**.',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0010': patch(
        'GÜG yükleme oranının, dönem başında TAHMİNİ verilerle önceden belirlenmesinin temel amacı aşağıdakilerden hangisidir?',
        {
            'A': "Sipariş tamamlandığında fiili GÜG'ün dönem sonuna kadar beklenmeden, siparişin maliyetini zamanında hesaplayabilmek",
            'B': 'Genel üretim giderlerini muhasebe kayıtlarında sıfıra indirip üretim maliyetini olduğundan düşük göstermek',
            'C': 'Siparişe yüklenen direkt işçilik tutarını yapay biçimde artırıp birim maliyeti yükseltmiş göstermek',
            'D': 'Dönemin gerçek satış tutarını mali tablolarda gizleyerek kârlılığı olduğundan farklı biçimde sunmak',
            'E': 'İşletmenin ödemesi gereken kurumlar vergisini yasal olmayan biçimde azaltıp ödenecek vergi yükünden büsbütün kurtulmak',
        },
        'A',
        'Fiili GÜG ancak dönem sonunda kesinleşir. Önceden belirlenen yükleme oranı sayesinde, bir sipariş tamamlandığında **dönem sonu beklenmeden** siparişin maliyeti zamanında hesaplanabilir (fiyatlama, teslim vb. için).',
        'Maliyet muhasebesi - önceden belirlenmiş yükleme oranı',
    ),
    # düzey 2
    '0011': patch(
        'Bir dönemde fiili genel üretim gideri 385.000 ₺ olarak gerçekleşmiş ve dönem sonunda 15.000 ₺ fazla yüklenmiş genel üretim gideri belirlenmiştir. Makine saati esaslı yükleme oranı 20 ₺/saat olduğuna göre dönemde fiilen kaç makine saati çalışılmıştır?',
        {
            'A': '19.250',
            'B': '18.500',
            'C': '19.000',
            'D': '8.000.000',
            'E': '20.000',
        },
        'E',
        "Fazla yükleme, yüklenen GÜG'ün fiili GÜG'ü aşan kısmıdır: yüklenen = 385.000 + 15.000 = 400.000 ₺. Fiili makine saati = yüklenen ÷ oran = 400.000 ÷ 20 = **20.000 saat**. (Yalnız fiili GÜG'ü bölmek 19.250 saat verir.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0012': patch(
        "Sipariş maliyet kartında 'yüklenen GÜG' tutarı hangi verilerle hesaplanır?",
        {
            'A': 'Önceden belirlenen yükleme oranı × siparişin fiili ölçüsü (makine/işçilik saati vb.)',
            'B': 'Siparişe yüklenen direkt ilk madde ve malzeme tutarının iki katının alınması yoluyla',
            'C': 'Siparişin birim satış fiyatı ile siparişte üretilen mamul adedinin çarpılması biçiminde',
            'D': 'Siparişin satış fiyatına eklenen birim kâr marjı tutarının esas alınması yoluyla',
            'E': 'Dönemin toplam fiili genel üretim gideri ÷ dönemdeki toplam sipariş sayısı olarak',
        },
        'A',
        'Siparişe yüklenen GÜG = **önceden belirlenen yükleme oranı × siparişin fiili ölçüsü** (makine saati, direkt işçilik saati/tutarı vb.).',
        'Maliyet muhasebesi - GÜG yükleme',
    ),
    # düzey 3
    '0013': patch(
        "112 no'lu siparişin maliyet kartında DİMM 70.000 ₺, DİG 50.000 ₺ yer almaktadır. Sipariş 1.200 makine saati kullanmış olup işletmenin yükleme oranı 25 ₺/makine saatidir. Bu siparişin dönüştürme (işleme) maliyeti kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '30.000',
            'C': '120.000',
            'D': '150.000',
            'E': '80.000',
        },
        'E',
        'Yüklenen GÜG = 1.200 × 25 = 30.000 ₺. Dönüştürme (işleme) maliyeti = DİG + GÜG = 50.000 + 30.000 = **80.000 ₺**. (DİMM + DİG = 120.000 ₺ ise birincil/asal maliyettir; dönüştürme maliyetine DİMM girmez.)',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0014': patch(
        'Sipariş maliyeti sisteminde bir siparişe malzeme verildiğinde maliyet kaydında hangi hesap borçlandırılır?',
        {
            'A': '320 SATICILAR hesabı borçlandırılır',
            'B': '710 DİREKT İLK MADDE VE MALZEME GİDERLERİ (7/A)',
            'C': '600 YURT İÇİ SATIŞLAR hesabı borçlandırılır',
            'D': '150 İLK MADDE VE MALZEME hesabı borçlandırılır',
            'E': '770 GENEL YÖNETİM GİDERLERİ hesabı borçlandırılır',
        },
        'B',
        "Siparişe direkt malzeme verildiğinde 7/A'da **710 DİREKT İLK MADDE VE MALZEME GİDERLERİ** borçlandırılır (karşılığında 150 İLK MADDE VE MALZEME alacaklandırılır).",
        'TDHP 710 Direkt İlk Madde ve Malzeme Giderleri',
    ),
    # düzey 2
    '0015': patch(
        'Bir sipariş tamamlanıp müşteriye satıldığında, siparişin üretim maliyeti hangi hesaba aktarılır?',
        {
            'A': '710 DİREKT İLK MADDE VE MALZEME GİDERLERİ',
            'B': '153 TİCARİ MALLAR',
            'C': '620 SATILAN MAMULLER MALİYETİ',
            'D': '151 YARI MAMULLER – ÜRETİM',
            'E': "152 MAMULLER'de kalır",
        },
        'C',
        "Sipariş satıldığında maliyeti 152 MAMULLER'den **620 SATILAN MAMULLER MALİYETİ** hesabına aktarılır (satış hasılatı ise 600 YURT İÇİ SATIŞLAR'a kaydedilir).",
        'TDHP 620 Satılan Mamuller Maliyeti',
    ),
    # düzey 3
    '0016': patch(
        "121 no'lu siparişte 400 adet mamul üretilmiş olup siparişin toplam üretim maliyeti 100.000 ₺'dir. Dönem içinde bu mamullerin 300 adedi satıldığına göre dönem sonunda stokta kalan mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '35.000',
            'B': '75.000',
            'C': '10.000',
            'D': '25.000',
            'E': '100.000',
        },
        'D',
        "Birim maliyet = 100.000 ÷ 400 = 250 ₺. Stokta kalan = 400 − 300 = 100 adet. Stok maliyeti = 100 × 250 = **25.000 ₺**. (Satılanların maliyeti 75.000 ₺'dir; ikisinin toplamı siparişin 100.000 ₺'lik maliyetini verir.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0017': patch(
        "130 no'lu siparişin maliyet kartında DİMM 140.000 ₺, DİG 100.000 ₺ yer almaktadır. İşletme genel üretim giderlerini direkt işçiliğin %60'ı oranında yüklediğine göre siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '300.000',
            'C': '60.000',
            'D': '324.000',
            'E': '384.000',
        },
        'B',
        "Yüklenen GÜG = 100.000 × %60 = 60.000 ₺. Toplam maliyet = DİMM + DİG + GÜG = 140.000 + 100.000 + 60.000 = **300.000 ₺**. (GÜG'ü atlamak 240.000 ₺ verir; oranı DİMM'e uygulamak yanlıştır.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0018': patch(
        'Sipariş maliyeti sisteminde birim maliyetlerin siparişler arasında farklılık göstermesinin temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Siparişlerin satış fiyatının farklı olması, tüketilen kaynakların aynı kalması',
            'B': 'Sipariş maliyeti sisteminde birim maliyetin ayrı ayrı hesaplanmaması',
            'C': 'Her siparişin farklı miktarda DİMM, DİG ve makine/işçilik saati (dolayısıyla GÜG) tüketmesi',
            'D': 'Bütün siparişlerin birbirinin tıpatıp aynısı olması ve aynı miktarda kaynak tüketmesi',
            'E': 'Genel üretim giderlerinin siparişlere eşit tutarda dağıtılması',
        },
        'C',
        "Sipariş maliyeti sisteminde her sipariş farklı özellikte olduğundan **farklı miktarda DİMM, DİG ve makine/işçilik saati** tüketir; bu da yüklenen GÜG'ü ve dolayısıyla birim maliyeti siparişten siparişe farklılaştırır.",
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 3
    '0019': patch(
        "141 no'lu sipariş: DİMM 150.000 ₺, DİG 90.000 ₺, yüklenen GÜG 60.000 ₺; üretilen 1.500 adettir. İşletme birim maliyetin %25 fazlasına satış yapmaktadır. Birim satış fiyatı kaç ₺'dir?",
        {
            'A': '250',
            'B': '225',
            'C': '160',
            'D': '200',
            'E': '300',
        },
        'A',
        'Toplam maliyet = 150.000 + 90.000 + 60.000 = 300.000 ₺. Birim maliyet = 300.000 ÷ 1.500 = 200 ₺. Satış fiyatı = 200 × 1,25 = **250 ₺/adet**.',
        'Maliyet muhasebesi - maliyete dayalı fiyatlama',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdakilerden hangisi sipariş maliyeti sisteminin bir SAKINCASI (dezavantajı) olarak gösterilebilir?',
        {
            'A': 'Sistemin tek tip mamul üreten kitle üretimine uygun olması',
            'B': 'Her siparişe ait ayrıntılı kayıt tutma zorunluluğu, kayıt ve izleme maliyetini/iş yükünü artırır',
            'C': 'Sipariş bazında kârlılığın ölçülememesi ve analiz edilememesi sorunu',
            'D': 'Tamamlanan siparişlerde birim maliyetin hesaplanamıyor olması',
            'E': 'Genel üretim giderlerinin siparişlere yüklenememesi sorunu',
        },
        'B',
        "Sipariş maliyeti sisteminde her siparişe ait DİMM, DİG ve GÜG'ün ayrı ayrı izlenmesi gerektiğinden **ayrıntılı kayıt tutma** zorunluluğu iş yükünü ve maliyeti artırır; bu sistemin başlıca sakıncasıdır.",
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 2
    '0021': patch(
        'Aşağıdaki işletmelerden hangisi tipik olarak sipariş maliyeti sistemini kullanır?',
        {
            'A': 'Akaryakıt üreten büyük rafineri',
            'B': 'Buğday öğüten un fabrikası',
            'C': 'Çimento üreten büyük fabrika',
            'D': 'Gemi inşa (tersane) işletmesi',
            'E': 'Toz şeker işleyen büyük tesis',
        },
        'D',
        '**Gemi inşa (tersane)** her siparişi ayrı, ayırt edilebilir üretim olduğundan sipariş maliyeti kullanır. Şeker, çimento, un, rafineri sürekli/kitle üretim → safha maliyeti.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 2
    '0022': patch(
        'Bir siparişin toplam üretim maliyeti nasıl hesaplanır?',
        {
            'A': 'DİMM × DİG × GÜG çarpımı',
            'B': 'Satış fiyatı − birim kâr',
            'C': 'Kullanılan DİMM',
            'D': 'DİMM + DİG + Yüklenen GÜG',
            'E': 'DİMM − DİG − Yüklenen GÜG farkı',
        },
        'D',
        'Sipariş toplam üretim maliyeti = **Direkt ilk madde ve malzeme + Direkt işçilik + Yüklenen genel üretim giderleri**.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 3
    '0023': patch(
        "102 no'lu siparişin maliyet kartında DİMM 60.000 ₺, DİG 40.000 ₺ yer almaktadır. İşletme genel üretim giderlerini direkt işçilik giderinin %50'si oranında yüklemekte olup siparişte 500 adet mamul üretilmiştir. Siparişin birim maliyeti kaç ₺'dir?",
        {
            'A': '240',
            'B': '300',
            'C': '280',
            'D': '200',
            'E': '120',
        },
        'A',
        "Yüklenen GÜG = DİG × %50 = 40.000 × 0,50 = 20.000 ₺. Toplam maliyet = 60.000 + 40.000 + 20.000 = 120.000 ₺. Birim maliyet = 120.000 ÷ 500 = **240 ₺**. (GÜG'ü atlamak 100.000 ÷ 500 = 200 ₺ verir.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0024': patch(
        'Sipariş maliyeti sisteminde direkt ilk madde ve malzeme (DİMM) siparişe nasıl yüklenir?',
        {
            'A': 'Siparişin satış tutarı içindeki payına göre orantılı biçimde bölüştürülerek',
            'B': 'Dönem başında saptanan tahmini bir yükleme oranıyla siparişe dağıtılarak',
            'C': 'Dönem sonunda toplam malzemeden tahmini pay ayrılıp yüklenerek',
            'D': 'Siparişe yüklenmez, doğrudan dönemin gideri olarak kaydedilerek',
            'E': 'Malzeme istek fişleri ile siparişe doğrudan (direkt) izlenerek',
        },
        'E',
        'DİMM, siparişe **doğrudan (direkt)** izlenebilir; malzeme istek fişleriyle hangi siparişte ne kadar kullanıldığı belirlenip o siparişe yüklenir. Dağıtım/tahmin gerekmez.',
        'Maliyet muhasebesi - direkt malzeme',
    ),
    # düzey 3
    '0025': patch(
        'Sipariş maliyeti sisteminde genel üretim giderleri (GÜG) siparişlere neden doğrudan değil, önceden belirlenen bir yükleme oranıyla yüklenir?',
        {
            'A': 'GÜG vergiye tabi olmayan bir gider kalemi kabul edildiği için siparişe bölünmez',
            'B': 'GÜG siparişlere yüklenmediği ve dönem gideri sayıldığı için',
            'C': 'GÜG bir satış gideri olup üretim maliyetiyle ilişkilendirilemediği için',
            'D': 'GÜG tutarı üretimin her aşamasında sıfır olduğundan yükleme yapmaya gerek olmadığı için',
            'E': 'GÜG endirekt ve ortak nitelikte olup tek siparişe doğrudan izlenemediği için',
        },
        'E',
        'GÜG (kira, amortisman, endirekt malzeme/işçilik) **endirekt ve ortak** niteliktedir; tek bir siparişe doğrudan izlenemez. Bu nedenle önceden belirlenen **yükleme oranı** (tahmini GÜG ÷ tahmini ölçü) ile siparişlere yüklenir.',
        'Maliyet muhasebesi - genel üretim giderleri',
    ),
    # düzey 3
    '0026': patch(
        "Bir dönemde üç siparişle çalışılmıştır: 101 no'lu sipariş (maliyeti 100.000 ₺) ve 102 no'lu sipariş (maliyeti 160.000 ₺) tamamlanmış; 103 no'lu sipariş (maliyeti 90.000 ₺) dönem sonunda henüz tamamlanmamıştır. Dönem sonunda 152 MAMULLER hesabına aktarılacak tutar kaç ₺'dir?",
        {
            'A': '350.000',
            'B': '160.000',
            'C': '260.000',
            'D': '190.000',
            'E': '90.000',
        },
        'C',
        "Yalnız **tamamlanan** siparişlerin maliyeti mamullere aktarılır: 100.000 + 160.000 = **260.000 ₺** (152 MAMULLER). Tamamlanmamış 103 no'lu siparişin 90.000 ₺'lik maliyeti 151 YARI MAMULLER hesabında izlenmeye devam eder; üç siparişin toplamı (350.000 ₺) mamullere aktarılmaz.",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0027': patch(
        'Önceden belirlenen genel üretim gideri yükleme oranı nasıl hesaplanır?',
        {
            'A': 'Dönem sonunda gerçekleşen fiili GÜG ÷ dönemde fiilen ulaşılan gerçekleşmiş dağıtım ölçüsü (makine saati, işçilik saati vb.)',
            'B': 'Dönemin toplam satış hasılatı ÷ dönemde gerçekleşen toplam genel üretim gideri tutarı',
            'C': 'Gerçekleşen genel üretim gideri × siparişte kullanılan makine saati ölçüsünün çarpımı',
            'D': 'Tahmini (bütçelenen) GÜG ÷ tahmini (bütçelenen) dağıtım ölçüsü (makine saati, direkt işçilik saati/tutarı vb.)',
            'E': 'Tahmini (bütçelenen) dağıtım ölçüsü ÷ tahmini (bütçelenen) genel üretim gideri tutarı',
        },
        'D',
        'Önceden belirlenen yükleme oranı = **Tahmini (bütçelenen) GÜG ÷ Tahmini dağıtım ölçüsü** (makine saati, direkt işçilik saati/tutarı vb.). Yıl başında belirlenir, yıl boyunca siparişlere uygulanır.',
        'Maliyet muhasebesi - GÜG yükleme oranı',
    ),
    # düzey 2
    '0028': patch(
        'Makine saati esaslı yükleme oranı 20 ₺/saat olan bir işletmede dönemde fiilen 21.000 makine saati çalışılmış; dönemin fiili genel üretim gideri 400.000 ₺ olarak gerçekleşmiştir. Genel üretim giderleri bakımından dönem sonunda ortaya çıkan fark ne kadardır ve niteliği nedir?',
        {
            'A': 'Fark oluşmaz',
            'B': '20.000 ₺ fazla yüklenmiş GÜG',
            'C': '420.000 ₺ fazla yüklenmiş GÜG',
            'D': '20.000 ₺ eksik yüklenmiş GÜG',
            'E': '1.000 ₺ fazla yüklenmiş GÜG',
        },
        'B',
        "Yüklenen GÜG = fiili saat × oran = 21.000 × 20 = 420.000 ₺. Fiili GÜG 400.000 ₺'dir. Yüklenen > fiili olduğundan **20.000 ₺ fazla (aşırı) yüklenmiş GÜG** doğar; bu tutar dönem sonunda satılan mamul maliyetinden düşülerek düzeltilir.",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0029': patch(
        "105 no'lu siparişin verileri: DİMM 45.000 ₺, DİG 25.000 ₺, kullanılan makine saati 1.500. GÜG yükleme oranı 20 ₺/makine saatidir. Siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '115.000',
            'B': '70.000',
            'C': '90.000',
            'D': '30.000',
            'E': '100.000',
        },
        'E',
        'Yüklenen GÜG = 20 × 1.500 = 30.000 ₺. Toplam maliyet = DİMM 45.000 + DİG 25.000 + GÜG 30.000 = **100.000 ₺**.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 3
    '0030': patch(
        "110 no'lu sipariş: DİMM 100.000 ₺, DİG 60.000 ₺. GÜG, direkt işçiliğin %50'si oranında yüklenmektedir. Siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '190.000',
            'B': '210.000',
            'C': '160.000',
            'D': '180.000',
            'E': '240.000',
        },
        'A',
        'Yüklenen GÜG = 60.000 × %50 = 30.000 ₺. Toplam maliyet = 100.000 + 60.000 + 30.000 = **190.000 ₺**.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 2
    '0031': patch(
        "Yükleme oranı 20 ₺/makine saati olan işletmede dönemde fiilen 21.000 makine saati çalışılmış, fiili GÜG 400.000 ₺ olmuştur. Yüklenen GÜG ile yükleme farkı sırasıyla kaç ₺'dir?",
        {
            'A': 'Yüklenen 420.000; 20.000 fazla yükleme',
            'B': 'Yüklenen 420.000; 20.000 eksik yükleme',
            'C': 'Yüklenen 380.000; 20.000 eksik yükleme',
            'D': 'Yüklenen 400.000; fark yok',
            'E': 'Yüklenen 21.000; 379.000 fazla',
        },
        'A',
        'Yüklenen GÜG = 20 × 21.000 = 420.000 ₺. Fiili 400.000 ₺. Yüklenen > fiili → **420.000 yüklenmiş, 20.000 ₺ fazla (aşırı) yükleme**.',
        'Maliyet muhasebesi - yükleme farkı',
    ),
    # düzey 2
    '0032': patch(
        "Bir siparişin 'dönüştürme (işleme) maliyeti' aşağıdakilerden hangisidir?",
        {
            'A': 'Kullanılan direkt ilk madde ve malzeme tutarı',
            'B': 'Pazarlama satış dağıtım gideri + genel yönetim gideri',
            'C': 'Direkt ilk madde ve malzeme + direkt işçilik (DİMM + DİG)',
            'D': 'Direkt ilk madde ve malzeme + genel üretim gideri (DİMM + GÜG)',
            'E': 'Direkt işçilik + genel üretim giderleri (DİG + GÜG)',
        },
        'E',
        "**Dönüştürme (işleme) maliyeti = Direkt işçilik + Genel üretim giderleri (DİG + GÜG)**; ilk maddeyi mamule dönüştürmek için katlanılan maliyettir. (DİMM + DİG ise 'birincil/asal maliyet'tir.)",
        'Maliyet muhasebesi - dönüştürme maliyeti',
    ),
    # düzey 3
    '0033': patch(
        "113 no'lu siparişin maliyet kartında DİMM 70.000 ₺, DİG 50.000 ₺ ve yüklenen GÜG 30.000 ₺ yer almaktadır. Bu siparişin birincil (asal) maliyeti ile dönüştürme (işleme) maliyeti arasındaki fark kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '40.000',
            'C': '200.000',
            'D': '80.000',
            'E': '20.000',
        },
        'B',
        'Birincil (asal) maliyet = DİMM + DİG = 70.000 + 50.000 = 120.000 ₺. Dönüştürme maliyeti = DİG + GÜG = 50.000 + 30.000 = 80.000 ₺. Fark = 120.000 − 80.000 = **40.000 ₺** (DİMM ile GÜG arasındaki farka eşittir; DİG her ikisinde de yer alır).',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0034': patch(
        '7/A maliyet hesaplama seçeneğinde direkt işçilik giderlerinin izlendiği hesap aşağıdakilerden hangisidir?',
        {
            'A': '720 DİREKT İŞÇİLİK GİDERLERİ',
            'B': '730 GENEL ÜRETİM GİDERLERİ',
            'C': '770 GENEL YÖNETİM GİDERLERİ',
            'D': '710 DİREKT İLK MADDE VE MALZEME GİDERLERİ',
            'E': '740 HİZMET ÜRETİM MALİYETİ',
        },
        'A',
        "7/A'da direkt işçilik giderleri **720 DİREKT İŞÇİLİK GİDERLERİ** hesabında izlenir.",
        'TDHP 720 Direkt İşçilik Giderleri',
    ),
    # düzey 3
    '0035': patch(
        "120 no'lu siparişin toplam üretim maliyeti 100.000 ₺ olup 400 adet mamul üretilmiştir. Bu siparişten 300 adet, adet başına 350 ₺'ye satıldığına göre satılan mamullerden elde edilen brüt kâr kaç ₺'dir?",
        {
            'A': '105.000',
            'B': '5.000',
            'C': '40.000',
            'D': '30.000',
            'E': '25.000',
        },
        'D',
        'Birim maliyet = 100.000 ÷ 400 = 250 ₺. Satılan 300 adedin maliyeti = 300 × 250 = 75.000 ₺; satış hasılatı = 300 × 350 = 105.000 ₺. Brüt kâr = 105.000 − 75.000 = **30.000 ₺** (birim kâr 100 ₺ × 300 adet).',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0036': patch(
        "Sipariş maliyeti sisteminde dönem sonunda 'fazla (aşırı) yüklenmiş GÜG' bulunuyorsa, bu durum satılan mamul maliyeti üzerinde nasıl bir düzeltme gerektirir (basit yaklaşım)?",
        {
            'A': 'Satılan mamul maliyetini artırır (fazla yükleme gider olarak eklenir)',
            'B': 'Satılan mamul maliyetini azaltır (mamullere fazla yüklenen kısım geri düzeltilir)',
            'C': 'Dönemin direkt işçilik giderini azaltır; fark işçilik hesabından geri çekilir',
            'D': 'Dönemin satış hasılatını artırır; fark 600 numaralı satış hesabına eklenir',
            'E': 'Satılan mamul maliyetini artırır; mamullere eksik yüklenen kısım sonradan eklenir',
        },
        'B',
        '**Fazla yüklenmiş GÜG**, mamullere fiili giderden daha fazla yüklendiğini gösterir; basit yaklaşımda bu fark satılan mamul maliyetinden düşülerek **SMM azaltılır** (maliyet gerçeğe getirilir).',
        'Maliyet muhasebesi - yükleme farkı düzeltme',
    ),
    # düzey 3
    '0037': patch(
        "131 no'lu siparişin toplam üretim maliyeti 360.000 ₺ olup 900 adet mamul üretilmiştir. İşletme birim maliyetin üzerine %25 kâr marjı ekleyerek satış fiyatı belirlediğine göre birim satış fiyatı kaç ₺'dir?",
        {
            'A': '320',
            'B': '525',
            'C': '400',
            'D': '500',
            'E': '450',
        },
        'D',
        "Birim maliyet = 360.000 ÷ 900 = 400 ₺. Satış fiyatı = 400 × (1 + %25) = **500 ₺**. (Birim maliyetin kendisi 400 ₺'dir; kâr marjı eklenmemiş olur.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0038': patch(
        "140 no'lu sipariş: DİMM 90.000 ₺, DİG 60.000 ₺, kullanılan makine saati 2.500, yükleme oranı 24 ₺/makine saati. Siparişin toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '210.000',
            'C': '240.000',
            'D': '174.000',
            'E': '150.000',
        },
        'B',
        'Yüklenen GÜG = 24 × 2.500 = 60.000 ₺. Toplam = 90.000 + 60.000 + 60.000 = **210.000 ₺**.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 2
    '0039': patch(
        'Sipariş maliyeti sisteminde dönem sonu üretim maliyetlerinin (7/A) 151 YARI MAMULLER veya 152 MAMULLER hesaplarına aktarılmasında köprü görevi gören yansıtma hesabı grubu aşağıdakilerden hangisidir?',
        {
            'A': '6XX Gelir tablosu hesapları (ör. 600, 620, 631 numaralı hesaplar)',
            'B': '3XX Kısa vadeli yabancı kaynak hesapları (ör. 300, 320, 360)',
            'C': '71X–73X Yansıtma hesapları (ör. 711, 721, 731 Yansıtma Hesapları)',
            'D': '1XX Dönen varlıklar hesapları (ör. 100, 120, 153 numaralı hesaplar)',
            'E': '5XX Özkaynak hesapları (ör. 500, 540, 570 numaralı hesaplar)',
        },
        'C',
        "7/A'da gider hesaplarında (710, 720, 730) biriken üretim maliyetleri, **71X–73X yansıtma hesapları** (711, 721, 731 …) aracılığıyla üretim/stok hesaplarına (151/152) aktarılır. Yansıtma hesapları köprü görevi görür.",
        'TDHP 7/A yansıtma hesapları',
    ),
    # düzey 3
    '0040': patch(
        "Sipariş maliyeti sistemi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. GÜG, her siparişe doğrudan izlenerek yükleme oranı kullanılmadan yüklenir.\n\nII. Heterojen, ayırt edilebilir üretim yapan işletmeler için uygundur.\n\nIII. Tamamlanan sipariş 152 MAMULLER, devam eden sipariş 151 YARI MAMULLER'de izlenir.",
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        "**I yanlıştır:** GÜG (genel üretim giderleri) endirekt niteliktedir; siparişlere doğrudan izlenemez, önceden belirlenen bir YÜKLEME ORANIYLA yüklenir. **II** sistemin heterojen/ayırt edilebilir üretime uygunluğu ve **III** tamamlanan siparişin 152 MAMULLER, devam edenin 151 YARI MAMULLER'de izlenmesi doğrudur. Doğru cevap **II ve III**.",
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 3
    '0041': patch(
        'Aşağıdaki üretim türlerinden hangisi sipariş maliyeti sistemine UYGUN DEĞİLDİR?',
        {
            'A': 'Köprü/bina inşaatı',
            'B': 'Matbaada özel kitap baskısı',
            'C': 'Sipariş üzerine özel mobilya üretimi',
            'D': 'Özel tasarım makine imalatı',
            'E': 'Sürekli akışlı şeker üretimi',
        },
        'E',
        'Özel mobilya, kitap baskısı, inşaat, özel makine ayırt edilebilir siparişlerdir → sipariş maliyeti. **Sürekli akışlı şeker üretimi** birbirinin aynı kitle üretimdir → **safha maliyeti** kullanılır.',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 2
    '0042': patch(
        'Sipariş maliyeti sisteminde her siparişin maliyetinin ayrı ayrı izlendiği belge aşağıdakilerden hangisidir?',
        {
            'A': 'Satış faturası belgesi',
            'B': 'Sipariş (iş) maliyet kartı',
            'C': 'Aylık ücret bordrosu',
            'D': 'Amortisman gider tablosu',
            'E': 'Genel geçici mizan cetveli',
        },
        'B',
        'Sipariş maliyeti sisteminde her sipariş için ayrı bir **sipariş (iş) maliyet kartı** açılır; siparişe ait DİMM, DİG ve yüklenen GÜG bu kartta toplanır.',
        'Maliyet muhasebesi - sipariş maliyet kartı',
    ),
    # düzey 2
    '0043': patch(
        'Bir siparişin birim maliyeti nasıl hesaplanır?',
        {
            'A': 'Sipariş toplam maliyeti ÷ sipariş adedi',
            'B': 'Sipariş toplam maliyeti × sipariş adedi',
            'C': 'Toplam maliyet + sipariş adedi',
            'D': 'Sipariş adedi ÷ toplam maliyet',
            'E': 'Satış fiyatı ÷ adet',
        },
        'A',
        'Sipariş birim maliyeti = **Sipariş toplam üretim maliyeti ÷ Sipariş adedi (üretilen birim sayısı)**.',
        'Maliyet muhasebesi - birim maliyet',
    ),
    # düzey 3
    '0044': patch(
        "103 no'lu siparişin toplam üretim maliyeti 160.000 ₺ olarak hesaplanmıştır. Siparişin maliyet kartındaki DİMM 80.000 ₺, DİG 40.000 ₺'dir. İşletmede makine saati esaslı genel üretim gideri yükleme oranı 20 ₺/saat olduğuna göre bu sipariş kaç makine saati kullanmıştır?",
        {
            'A': '4.000',
            'B': '800.000',
            'C': '1.000',
            'D': '2.000',
            'E': '6.000',
        },
        'D',
        'Siparişe yüklenen GÜG = toplam maliyet − DİMM − DİG = 160.000 − 80.000 − 40.000 = 40.000 ₺. Kullanılan makine saati = yüklenen GÜG ÷ oran = 40.000 ÷ 20 = **2.000 saat**.',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0045': patch(
        'Sipariş maliyeti sisteminde direkt işçilik (DİG) siparişe nasıl yüklenir?',
        {
            'A': 'Siparişte kullanılan direkt ilk madde ve malzeme miktarıyla orantılı olarak dağıtılarak',
            'B': 'Siparişin öngörülen satış fiyatı içindeki paya göre orantılı biçimde bölüştürülerek',
            'C': 'Dönem başında saptanan tahmini bir işçilik yükleme oranıyla siparişlere paylaştırılarak',
            'D': 'İşçilik zaman kartları ile siparişte harcanan süreye göre doğrudan (direkt)',
            'E': 'Siparişe yüklenmez, dönemin genel yönetim gideri olarak kaydedilerek',
        },
        'D',
        'Direkt işçilik, **işçilik zaman kartları** ile hangi siparişte ne kadar süre çalışıldığı belirlenip siparişe **doğrudan** yüklenir.',
        'Maliyet muhasebesi - direkt işçilik',
    ),
    # düzey 2
    '0046': patch(
        'Dönem sonunda henüz TAMAMLANMAMIŞ (devam eden) siparişlerin maliyeti hangi hesapta izlenir?',
        {
            'A': '151 YARI MAMULLER – ÜRETİM',
            'B': '620 SATILAN MAMULLER MALİYETİ',
            'C': '153 TİCARİ MALLAR',
            'D': '600 YURT İÇİ SATIŞLAR',
            'E': '152 MAMULLER',
        },
        'A',
        'Dönem sonunda tamamlanmamış siparişlerin (devam eden işlerin) maliyeti **151 YARI MAMULLER – ÜRETİM** hesabında izlenir.',
        'TDHP 151 Yarı Mamuller',
    ),
    # düzey 3
    '0047': patch(
        "104 no'lu siparişin maliyet kartında DİMM 60.000 ₺, DİG 20.000 ₺ yer almaktadır. Genel üretim giderleri direkt işçiliğin %50'si oranında yüklenmekte olup siparişte 300 adet mamul üretilmiştir. Siparişin birim maliyeti kaç ₺'dir?",
        {
            'A': '330',
            'B': '300',
            'C': '200',
            'D': '267',
            'E': '350',
        },
        'B',
        "Yüklenen GÜG = 20.000 × %50 = 10.000 ₺. Toplam maliyet = 60.000 + 20.000 + 10.000 = 90.000 ₺. Birim maliyet = 90.000 ÷ 300 = **300 ₺**. (GÜG'ü atlamak 80.000 ÷ 300 ≈ 267 ₺ verir.)",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0048': patch(
        "Bir işletmenin dönem için tahmini genel üretim gideri 400.000 ₺, tahmini makine saati 20.000'dir. 105 no'lu sipariş bu dönemde 1.500 makine saati kullandığına göre siparişe yüklenecek genel üretim gideri kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '13.333',
            'C': '20.000',
            'D': '400.000',
            'E': '30.000',
        },
        'E',
        'Yükleme oranı = 400.000 ÷ 20.000 = 20 ₺/makine saati. Siparişe yüklenen GÜG = 1.500 × 20 = **30.000 ₺**. Oran dönem başında tahmini verilerle belirlenir; böylece sipariş tamamlandığında fiili GÜG beklenmeden maliyet hesaplanabilir.',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0049': patch(
        "Bir dönemde siparişlere yüklenen genel üretim gideri 380.000 ₺, fiili genel üretim gideri 400.000 ₺'dir. Düzeltme öncesi satılan mamul maliyeti 900.000 ₺ olduğuna göre basit yaklaşımda düzeltme sonrası satılan mamul maliyeti kaç ₺'dir?",
        {
            'A': '1.280.000',
            'B': '880.000',
            'C': '920.000',
            'D': '1.300.000',
            'E': '900.000',
        },
        'C',
        'Yüklenen (380.000) < fiili (400.000) olduğundan 20.000 ₺ **eksik yüklenmiş** GÜG vardır; maliyetler olduğundan düşük hesaplanmıştır. Basit yaklaşımda fark satılan mamul maliyetine **eklenir**: 900.000 + 20.000 = **920.000 ₺**. (Fazla yükleme durumunda düşülürdü.)',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0050': patch(
        "Direkt işçilik tutarı esaslı GÜG yükleme oranı %50 olan işletmede, bir siparişin direkt işçiliği 60.000 ₺'dir. Bu siparişe yüklenecek GÜG kaç ₺'dir?",
        {
            'A': '30.000',
            'B': '120.000',
            'C': '60.000',
            'D': '12.000',
            'E': '50.000',
        },
        'A',
        'Yüklenen GÜG = direkt işçilik × oran = 60.000 × %50 = 60.000 × 0,50 = **30.000 ₺**.',
        'Maliyet muhasebesi - GÜG yükleme',
    ),
    # düzey 2
    '0051': patch(
        'Makine saati esaslı yükleme oranı 25 ₺/saat olan bir işletmede dönemde fiilen 19.000 makine saati çalışılmış; fiili genel üretim gideri 500.000 ₺ olmuştur. Dönem sonunda genel üretim giderleri bakımından ortaya çıkan fark ne kadardır ve niteliği nedir?',
        {
            'A': '475.000 ₺ eksik yüklenmiş GÜG',
            'B': '25.000 ₺ fazla yüklenmiş GÜG',
            'C': '1.000 ₺ eksik yüklenmiş GÜG',
            'D': 'Fark oluşmaz',
            'E': '25.000 ₺ eksik yüklenmiş GÜG',
        },
        'E',
        'Yüklenen GÜG = 19.000 × 25 = 475.000 ₺; fiili GÜG 500.000 ₺. Yüklenen < fiili olduğundan **25.000 ₺ eksik (az) yüklenmiş GÜG** doğar; bu tutar satılan mamul maliyetine eklenerek düzeltilir.',
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 3
    '0052': patch(
        "111 no'lu sipariş: DİMM 120.000 ₺, DİG 80.000 ₺, kullanılan makine saati 4.000, yükleme oranı 25 ₺/makine saati. Üretilen mamul 600 adettir. Birim maliyet kaç ₺'dir?",
        {
            'A': '400',
            'B': '600',
            'C': '500',
            'D': '450',
            'E': '300',
        },
        'C',
        'Yüklenen GÜG = 25 × 4.000 = 100.000 ₺. Toplam = 120.000 + 80.000 + 100.000 = 300.000 ₺. Birim = 300.000 ÷ 600 = **500 ₺/adet**.',
        'Maliyet muhasebesi - birim maliyet',
    ),
    # düzey 2
    '0053': patch(
        "Bir siparişin 'birincil (asal/temel) maliyeti' aşağıdakilerden hangisidir?",
        {
            'A': 'Direkt işçilik + genel üretim giderleri (DİG + GÜG) toplamı',
            'B': 'Pazarlama satış dağıtım gideri + genel yönetim gideri toplamı',
            'C': 'Direkt ilk madde ve malzeme + genel üretim giderleri (DİMM + GÜG)',
            'D': 'Direkt ilk madde ve malzeme + direkt işçilik (DİMM + DİG)',
            'E': 'Siparişe yüklenen genel üretim giderleri (GÜG) tutarı',
        },
        'D',
        '**Birincil (asal/temel) maliyet = Direkt ilk madde ve malzeme + Direkt işçilik (DİMM + DİG)**; mamule doğrudan izlenebilen maliyetlerin toplamıdır.',
        'Maliyet muhasebesi - asal maliyet',
    ),
    # düzey 3
    '0054': patch(
        "GÜG yükleme oranı ve yükleme farkı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yükleme oranı dönem başında tahmini verilerle belirlenir.\n\nII. Yüklenen GÜG fiili GÜG'den fazlaysa eksik yükleme vardır.\n\nIII. Yüklenen GÜG = yükleme oranı × siparişin fiili ölçüsü.",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'C',
        "**II yanlıştır:** Yüklenen GÜG fiili GÜG'den **fazlaysa fazla (aşırı) yükleme**, **azsa eksik yükleme** söz konusudur; öncül bunun tersini söylemektedir. **I** yükleme oranı dönem başında tahmini belirlenir; **III** yüklenen GÜG = yükleme oranı × fiili ölçüdür. Doğru cevap **I ve III**.",
        'Maliyet muhasebesi - GÜG yükleme',
    ),
    # düzey 2
    '0055': patch(
        'Sipariş maliyeti sisteminde maliyeti oluşan tamamlanmış bir siparişin mamule dönüşmesi kaydında hangi hesap borçlandırılır?',
        {
            'A': '620 SATILAN MAMULLER MALİYETİ',
            'B': '152 MAMULLER',
            'C': '600 YURT İÇİ SATIŞLAR',
            'D': '710 DİREKT İLK MADDE VE MALZEME GİDERLERİ',
            'E': '151 YARI MAMULLER – ÜRETİM',
        },
        'B',
        'Tamamlanan sipariş mamule dönüştüğünde **152 MAMULLER** borçlandırılır (karşılığında 151 YARI MAMULLER – ÜRETİM veya ilgili üretim hesabı alacaklandırılır).',
        'TDHP 152 Mamuller',
    ),
    # düzey 3
    '0056': patch(
        "121 no'lu siparişin toplam maliyeti 180.000 ₺, üretilen 600 adettir. İşletme birim maliyet üzerine %40 kâr ekleyerek satış fiyatı belirlemektedir. Birim satış fiyatı kaç ₺'dir?",
        {
            'A': '180',
            'B': '300',
            'C': '500',
            'D': '420',
            'E': '120',
        },
        'D',
        'Birim maliyet = 180.000 ÷ 600 = 300 ₺. Satış fiyatı = birim maliyet × (1 + kâr oranı) = 300 × 1,40 = **420 ₺/adet**.',
        'Maliyet muhasebesi - maliyete dayalı fiyatlama',
    ),
    # düzey 2
    '0057': patch(
        "Dönem sonunda 'eksik (az) yüklenmiş GÜG' bulunuyorsa, basit yaklaşımda satılan mamul maliyeti nasıl düzeltilir?",
        {
            'A': 'Satılan mamul maliyeti azaltılır; mamullere fazla yüklenen kısım geri çekilir',
            'B': 'Satılan mamul maliyeti artırılır (mamullere eksik yüklenen kısım eklenir)',
            'C': 'Dönemin satış hasılatı azaltılır; fark 600 numaralı satış hesabından düşülür',
            'D': 'Genel üretim giderleri sıfırlanır; tüm yükleme kayıtları dönem sonunda iptal edilir',
            'E': 'Satılan mamul maliyeti azaltılır (eksik yükleme gelir sayılır)',
        },
        'B',
        '**Eksik yüklenmiş GÜG**, mamullere fiili giderden daha az yüklendiğini gösterir; basit yaklaşımda bu fark satılan mamul maliyetine eklenerek **SMM artırılır**.',
        'Maliyet muhasebesi - yükleme farkı düzeltme',
    ),
    # düzey 3
    '0058': patch(
        "Bir dönemde dört siparişle çalışılmıştır: 101 (100.000 ₺), 102 (160.000 ₺) ve 103 (90.000 ₺) no'lu siparişler tamamlanmış; 104 no'lu sipariş (70.000 ₺) dönem sonunda devam etmektedir. Dönem sonunda 151 YARI MAMULLER hesabında izlenecek tutar kaç ₺'dir?",
        {
            'A': '70.000',
            'B': '160.000',
            'C': '420.000',
            'D': '90.000',
            'E': '350.000',
        },
        'A',
        "Tamamlanmamış (devam eden) siparişin maliyeti dönem sonunda **151 YARI MAMULLER** hesabında kalır: **70.000 ₺**. Tamamlanan üç siparişin 350.000 ₺'lik maliyeti 152 MAMULLER'e aktarılır; dönemin toplam üretim maliyeti ise 420.000 ₺'dir.",
        'Maliyet muhasebesi - sipariş maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdakilerden hangisi sipariş maliyeti sisteminin bir üstünlüğüdür?',
        {
            'A': 'Ayrıntılı kayıt gerektirmediğinden kayıt ve izleme maliyetinin çok düşük düzeyde kalması ve iş yükünün oldukça az olması',
            'B': 'Birim maliyet hesaplanmadan siparişlerin doğrudan satılabilmesi',
            'C': 'Her siparişin maliyetinin ayrı ayrı, ayrıntılı biçimde bilinebilmesi (özel fiyatlama ve kârlılık analizine olanak)',
            'D': 'Tek tip, birbirinin aynı mamul üreten kitle üretimine uygun olması',
            'E': 'Genel üretim giderlerinin siparişlere dağıtılmayıp dönem gideri sayılması',
        },
        'C',
        'Sipariş maliyeti sisteminin üstünlüğü, **her siparişin maliyetinin ayrı ve ayrıntılı** izlenebilmesidir; bu, özel fiyatlama ve sipariş bazlı kârlılık analizine olanak sağlar. (Dezavantajı ise ayrıntılı kayıt yükünün fazla olmasıdır.)',
        'Maliyet muhasebesi - sipariş maliyeti',
    ),
    # düzey 3
    '0060': patch(
        "150 no'lu sipariş yıl sonunda henüz tamamlanmamıştır. Kartında biriken DİMM 40.000 ₺, DİG 30.000 ₺, yüklenen GÜG 20.000 ₺'dir. Bu siparişin dönem sonunda 151 YARI MAMULLER hesabında görünecek maliyeti kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '70.000',
            'C': '90.000',
            'D': '60.000',
            'E': '50.000',
        },
        'C',
        "Devam eden siparişin maliyeti = DİMM + DİG + yüklenen GÜG = 40.000 + 30.000 + 20.000 = **90.000 ₺** (151 YARI MAMULLER – ÜRETİM'de izlenir).",
        'Maliyet muhasebesi - yarı mamul',
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
    print(f"1 paket / {len(PATCHES)} soru ('Siparis Maliyeti' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
