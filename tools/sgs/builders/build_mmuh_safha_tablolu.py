#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Safha Maliyeti — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Maliyet muhasebesi tablolu tur. Gercek sinavin 15 safha sorusu hep donem basi yari mamul (DBYM) ve FIFO/ortalama ayrimi iceriyor; eski pakette DBYM hic yoktu. 26 soru korundu (mutlak ifadeli celdiriciler gercek icerikle yenilendi); 34 yeni tablolu soru: FIFO ve ortalama esdeger birim, birim maliyet, tamamlanan ve DSYM maliyeti, yontem farki, uc unsurlu farkli tamamlanma dereceleri, DBYM'yi tamamlama maliyeti, tersine sorular (DBYM/DSYM tamamlanma derecesi, hedef birim maliyet icin DBYM tutari, eksik DSYM miktari), iki safhali miktar saglama, onceki safha maliyeti, normal/anormal fire. Tutarlar Fraction ile hesaplandi, her veri setinde tamamlanan + DSYM (+ anormal fire) = toplam maliyet saglamasi assert edildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Maliyet muhasebesi - safha (evre) maliyet sistemi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliyet_muhasebesi/safha_maliyeti.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (tablolu çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "mmuh-safha-gen-"


def patch(stem, options, answer, solution, ref='Maliyet muhasebesi - safha maliyeti'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Safha (evre) maliyeti sistemi aşağıdaki üretim biçimlerinden hangisinde kullanılır?',
        {
            'A': 'Fiziki mamul çıkarmayan hizmet işletmelerinin dönem gideri dağıtımında (danışmanlık, bağımsız denetim)',
            'B': 'Birbirinin aynı/benzer, sürekli ve kitle halinde, aşamalar (safhalar) izleyen üretim (şeker, çimento, un, tekstil)',
            'C': 'Birbirinden farklı, her biri müşteri siparişine göre ayrı ayrı ayırt edilebilen üretim (gemi, özel yat, özel mobilya)',
            'D': 'Her proje için tek bir birimin müşteri çizimine göre üretildiği işlerde (köprü, baraj, özel makine)',
            'E': 'Satın aldığı malı işlemeden satan ticaret işletmelerinin stok maliyetlemesinde (toptan gıda, beyaz eşya bayisi)',
        },
        'B',
        '**Safha maliyeti sistemi**, birbirinin aynı/benzer, sürekli ve kitle halinde, ardışık **aşamalar (safhalar)** izleyen üretimde kullanılır (şeker, çimento, un, tekstil, kağıt, petrol).',
        'Maliyet muhasebesi - safha maliyeti sistemi',
    ),
    # düzey 2
    '0002': patch(
        "Bir safhada direkt ilk madde ve malzeme (DİMM) safha başında topluca verilmektedir. Dönemde 9.000 birim tamamlanmış, dönem sonunda 3.000 birim yarı mamul kalmıştır (DİMM bakımından %100, dönüştürme bakımından %60 tamamlanmış). DİMM maliyeti 360.000 ₺, dönüştürme (DİG + GÜG) maliyeti 378.000 ₺ olduğuna göre tamamlanmış bir birimin toplam maliyeti kaç ₺'dir?",
        {
            'A': '70',
            'B': '60',
            'C': '65',
            'D': '61,50',
            'E': '55',
        },
        'C',
        'DİMM eşdeğeri = 9.000 + 3.000 = 12.000 birim → DİMM birim maliyeti = 360.000 ÷ 12.000 = 30 ₺. Dönüştürme eşdeğeri = 9.000 + (3.000 × %60) = 10.800 birim → dönüştürme birim maliyeti = 378.000 ÷ 10.800 = 35 ₺. Tam birim maliyeti = 30 + 35 = **65 ₺**. (İki unsura tek eşdeğer uygulamak yanlıştır; DİMM ile dönüştürmenin tamamlanma dereceleri farklıdır.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0003': patch(
        "Bir safhaya dönemde 10.000 birim girmiş, üretim sırasında %10 oranında normal fire oluşmuş ve kalan birimlerin tamamı tamamlanmıştır. Safhanın toplam maliyeti 450.000 ₺ olduğuna göre sağlam mamulün birim maliyeti kaç ₺'dir?",
        {
            'A': '10',
            'B': '45',
            'C': '40',
            'D': '50',
            'E': '35',
        },
        'D',
        'Normal fire = 10.000 × %10 = 1.000 birim; sağlam üretim = 10.000 − 1.000 = 9.000 birim. Normal fire kaçınılmaz sayıldığından maliyeti ayrı zarar yazılmaz, sağlam birimlere yüklenir: birim maliyet = 450.000 ÷ 9.000 = **50 ₺**. (Fireyi dikkate almadan 450.000 ÷ 10.000 = 45 ₺ bulunur — eksik.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0004': patch(
        "Bir safhada dönemde 8.000 birim tamamlanmış, dönem sonunda 4.000 birim yarı mamul kalmıştır (dönüştürme bakımından %50 tamamlanmış). Dönemin dönüştürme (DİG + GÜG) maliyeti 400.000 ₺ olduğuna göre tamamlanan birimlere yüklenen dönüştürme maliyeti kaç ₺'dir?",
        {
            'A': '320.000',
            'B': '266.667',
            'C': '400.000',
            'D': '80.000',
            'E': '200.000',
        },
        'A',
        'Dönüştürme eşdeğeri = 8.000 + (4.000 × %50) = 10.000 birim. Dönüştürme birim maliyeti = 400.000 ÷ 10.000 = 40 ₺. Tamamlananlara yüklenen = 8.000 × 40 = **320.000 ₺**. (Kalan 80.000 ₺ yarı mamulün dönüştürme payıdır.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0005': patch(
        "Bir safhada DİMM maliyeti 360.000 ₺ (birim maliyeti 30 ₺), dönüştürme maliyeti 400.000 ₺ (birim maliyeti 40 ₺) olarak hesaplanmıştır. Dönemde 8.000 birim tamamlanmıştır. Safhanın toplam 760.000 ₺'lik maliyetinden tamamlananlara düşen pay çıkarıldığında dönem sonu yarı mamullere düşen tutar kaç ₺'dir?",
        {
            'A': '760.000',
            'B': '160.000',
            'C': '560.000',
            'D': '120.000',
            'E': '200.000',
        },
        'E',
        'Tam birim maliyeti = 30 + 40 = 70 ₺. Tamamlananların maliyeti = 8.000 × 70 = 560.000 ₺. Yarı mamullere düşen = 760.000 − 560.000 = **200.000 ₺**. (Kontrol: yarı mamul 4.000 birim DİMM %100 ve dönüştürme %50 ise 4.000 × 30 + 2.000 × 40 = 120.000 + 80.000 = 200.000 ₺ ile aynı sonuç.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0006': patch(
        "Bir safhada eşdeğer birim maliyet 55 ₺ olarak hesaplanmış ve tamamlanan birimlerin toplam maliyeti 825.000 ₺ olarak bulunmuştur. Dönem sonu yarı mamulün eşdeğer ürün miktarı 3.000 birim olduğuna göre safhanın dönem toplam maliyeti kaç ₺'dir?",
        {
            'A': '990.000',
            'B': '880.000',
            'C': '1.155.000',
            'D': '825.000',
            'E': '165.000',
        },
        'A',
        "Tamamlanan birim sayısı = 825.000 ÷ 55 = 15.000 birim. Toplam eşdeğer ürün = 15.000 + 3.000 = 18.000 birim. Dönem toplam maliyeti = 18.000 × 55 = **990.000 ₺**. (Yarı mamulün payı 3.000 × 55 = 165.000 ₺'dir.)",
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0007': patch(
        "Safha maliyeti sisteminde 'normal fire' ile 'anormal fire' arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'Normal fire de anormal fire de kalan sağlam mamullerin maliyetine yüklenir; ikisi arasında herhangi bir işlem ya da kayıt farkı bulunmaz ve tümü sağlam mamule biner',
            'B': 'Anormal fire kalan sağlam mamulün maliyetine yüklenir; normal fire ise beklenmedik sayılıp dönem zararı olarak ayrılır',
            'C': 'Normal fire üretimin doğası gereği kaçınılmazdır ve mamul maliyetine yüklenir; anormal fire beklenenin üzerindedir ve genellikle dönem gideri/zararı yazılır',
            'D': 'Normal fire ile anormal fire arasında hiçbir fark yoktur; her ikisi de aynı biçimde doğrudan mamul maliyetine dahil edilir ve stok değerini artırır',
            'E': 'Normal fire de anormal fire de doğrudan dönem gideri/zararı olarak yazılır; hiçbiri kalan sağlam mamulün maliyetine yüklenmez',
        },
        'C',
        '**Normal fire** üretimin doğası gereği kaçınılmazdır; kalan sağlam mamullerin **maliyetine yüklenir**. **Anormal fire** beklenen düzeyin üzerindedir; genellikle **dönem gideri/zararı** olarak ayrılır, mamul maliyetini şişirmez.',
        'Maliyet muhasebesi - fire',
    ),
    # düzey 2
    '0008': patch(
        "Bir safhaya dönemde 20.000 birim girmiş, %10 oranında normal fire oluşmuş ve kalan birimler tamamlanmıştır. Safhanın toplam maliyeti 720.000 ₺'dir. Normal fire nedeniyle sağlam mamulün birim maliyeti, hiç fire olmaması durumuna göre kaç ₺ ARTMIŞTIR?",
        {
            'A': '72',
            'B': '8',
            'C': '36',
            'D': '40',
            'E': '4',
        },
        'E',
        'Normal fire = 20.000 × %10 = 2.000 birim; sağlam üretim = 18.000 birim. Fireli durumda birim maliyet = 720.000 ÷ 18.000 = 40 ₺. Fire olmasaydı = 720.000 ÷ 20.000 = 36 ₺. Artış = 40 − 36 = **4 ₺**. Normal fire maliyeti sağlam birimlere yüklendiği için birim maliyeti yükseltir.',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0009': patch(
        'Aşağıdakilerden hangisi safha maliyeti sisteminin kullanıldığı bir üretim türü DEĞİLDİR?',
        {
            'A': 'Akaryakıt (rafineri) üretimi',
            'B': 'Köprü/baraj inşaatı (taahhüt)',
            'C': 'Un üretimi',
            'D': 'Çimento üretimi',
            'E': 'Şeker üretimi',
        },
        'B',
        'Çimento, şeker, un, rafineri sürekli/kitle üretimdir → safha maliyeti. **Köprü/baraj inşaatı** her projesi ayrı, ayırt edilebilir bir iş olduğundan **sipariş maliyeti** kullanır.',
        'Maliyet muhasebesi - safha maliyeti',
    ),
    # düzey 3
    '0010': patch(
        "Tek safhada tek tip mamul üreten ve üretim kaybı bulunmayan bir işletmenin döneme ait bilgileri aşağıdaki gibidir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul (DBYM) | 2.000 |\n| Dönemde üretime başlanan | 18.000 |\n| Dönemde tamamlanan | 16.000 |\n| Dönem sonu yarı mamul (DSYM) | 4.000 |\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 29.000 | 288.000 |\n| Direkt işçilik | 10.200 | 168.000 |\n| Genel üretim | 15.300 | 252.000 |\n\nDirekt ilk madde ve malzeme üretimin başında verilmektedir. Şekillendirme (direkt işçilik + genel üretim) açısından DBYM %60, DSYM %50 oranında tamamlanmıştır.\n\nAğırlıklı ortalama maliyet yöntemine göre direkt ilk madde ve malzeme açısından eşdeğer birim maliyeti kaç ₺'dir?",
        {
            'A': '17,20',
            'B': '16',
            'C': '17,30',
            'D': '15,85',
            'E': '18',
        },
        'D',
        "Ortalama yöntemde DBYM maliyeti dönem maliyetine eklenir: 29.000 + 288.000 = 317.000 ₺. Eşdeğer birim = tamamlanan + DSYM eşdeğeri = 16.000 + 4.000 = 20.000. Birim maliyet = 317.000 ÷ 20.000 = **15,85 ₺**. FIFO'da ise yalnız dönem maliyeti 18.000 birime bölünür ve 16 ₺ bulunur.",
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 3
    '0011': patch(
        'Tek safhada tek tip mamul üreten ve üretim kaybı bulunmayan bir işletmenin döneme ait bilgileri aşağıdaki gibidir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul (DBYM) | 3.000 |\n| Dönemde üretime başlanan | 15.000 |\n| Dönemde tamamlanan | 14.000 |\n| Dönem sonu yarı mamul (DSYM) | 4.000 |\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 42.000 | 300.000 |\n| Direkt işçilik | 9.600 | 194.400 |\n| Genel üretim | 14.400 | 291.600 |\n\nDirekt ilk madde ve malzeme üretimin başında verilmektedir. Şekillendirme (direkt işçilik + genel üretim) açısından DBYM %50, DSYM %25 oranında tamamlanmıştır.\n\nİşletme FIFO yerine ağırlıklı ortalama maliyet yöntemini kullansaydı dönemde tamamlanan mamullerin toplam maliyeti nasıl değişirdi?',
        {
            'A': '6.000 ₺ azalırdı',
            'B': '24.000 ₺ artardı',
            'C': 'Değişmezdi; toplam maliyet aynı kalır',
            'D': '8.000 ₺ artardı',
            'E': '6.000 ₺ artardı',
        },
        'E',
        'FIFO: DİMM 300.000 ÷ (14.000 − 3.000 + 4.000 = 15.000) = 20 ₺; şekillendirme 486.000 ÷ (14.000 − 1.500 + 1.000 = 13.500) = 36 ₺; DSYM 4.000 × 20 + 1.000 × 36 = 116.000 ₺; tamamlanan 852.000 − 116.000 = 736.000 ₺. Ortalama: DİMM 342.000 ÷ 18.000 = 19 ₺; şekillendirme 510.000 ÷ 15.000 = 34 ₺; tamamlanan 14.000 × 53 = 742.000 ₺, DSYM 110.000 ₺. Toplam maliyet aynıdır; tamamlananlar 6.000 ₺ artar, DSYM aynı tutarda azalır.',
        'Maliyet muhasebesi - safha maliyeti (FIFO/ortalama)',
    ),
    # düzey 2
    '0012': patch(
        "Tek safhada üretim yapan ve üretim kaybı bulunmayan bir işletmede dönem başı yarı mamul 3.000 kg, dönemde üretime başlanan 24.000 kg, dönemde tamamlanan 22.000 kg ve dönem sonu yarı mamul 5.000 kg'dır. Yarı mamullerin tamamlanma dereceleri şöyledir:\n\n| Maliyet unsuru | DBYM | DSYM |\n|---|---|---|\n| DİMM | %100 | %100 |\n| Direkt işçilik | %40 | %70 |\n| Genel üretim | %30 | %50 |\n\nAğırlıklı ortalama maliyet yöntemine göre genel üretim giderleri açısından eşdeğer birim sayısı kaçtır?",
        {
            'A': '23.600',
            'B': '23.500',
            'C': '24.500',
            'D': '23.300',
            'E': '23.400',
        },
        'C',
        "Ortalama yöntemde DBYM ayrıştırılmaz: tamamlanan 22.000 + DSYM eşdeğeri 5.000 × %50 = 22.000 + 2.500 = **24.500** kg. DBYM'nin tamamlanma derecesi yalnız FIFO'da kullanılır.",
        'Maliyet muhasebesi - safha maliyeti (ortalama eşdeğer birim)',
    ),
    # düzey 3
    '0013': patch(
        "Safha maliyet sisteminde ilk giren ilk çıkar (FIFO) yöntemini uygulayan bir işletmenin döneme ait bilgileri şöyledir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul | 4.000 |\n| Dönemde üretime alınan | 16.000 |\n| Dönemde tamamlanan | 15.000 |\n| Dönem sonu yarı mamul | 5.000 |\n\nDSYM'nin direkt işçilik açısından tamamlanma derecesi %40, dönemin direkt işçilik giderleri 324.000 ₺ ve eşdeğer birim başına direkt işçilik gideri 20 ₺'dir. Buna göre, dönem başı yarı mamullerin direkt işçilik açısından tamamlanma derecesi yüzde kaçtır?",
        {
            'A': '%25',
            'B': '%20',
            'C': '%60',
            'D': '%40',
            'E': '%80',
        },
        'B',
        'FIFO eşdeğer birim = dönem gideri ÷ birim gider = 324.000 ÷ 20 = 16.200. FIFO formülü: 15.000 − (4.000 × x) + (5.000 × %40) = 16.200 → 17.000 − 4.000x = 16.200 → 4.000x = 800 → x = **%20**. DBYM önceki dönemde %20 tamamlanmış, bu dönem kalan %80 eklenmiştir.',
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 3
    '0014': patch(
        "Tek safhada tek tip mamul üreten ve ortalama maliyet yöntemini kullanan bir işletmede üretim kaybı yoktur. DSYM direkt ilk madde ve malzeme açısından %100, şekillendirme açısından %30 tamamlanmıştır. Döneme ait bilgiler şöyledir:\n\n| Veri | DBYM | Dönem |\n|---|---|---|\n| Miktar (ton) | 1.500 | 4.000 başlanan, 4.500 tamamlanan |\n| DİMM (₺) | 10.000 | 45.000 |\n| Direkt işçilik (₺) | 1.000 | 11.000 |\n| Genel üretim (₺) | 1.400 | 15.400 |\n\nBuna göre, dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '10.000',
            'B': '4.800',
            'C': '5.900',
            'D': '11.800',
            'E': '7.600',
        },
        'D',
        'Önce DSYM miktarı: 1.500 + 4.000 − 4.500 = 1.000 ton. DİMM birim = (10.000 + 45.000) ÷ (4.500 + 1.000) = 10 ₺. Şekillendirme birim = (2.400 + 26.400) ÷ (4.500 + 300) = 6 ₺. DSYM = 1.000 × 10 + 300 × 6 = **11.800 ₺**.',
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 3
    '0015': patch(
        "İki safhada üretim yapan ve ortalama maliyet yöntemini kullanan bir işletmenin II. safhasına ait bilgiler şöyledir:\n\n| Veri | Tutar |\n|---|---|\n| Dönem başı yarı mamul miktarı | 1.000 birim |\n| DBYM'nin önceki safha maliyeti | 38.000 ₺ |\n| DBYM'nin şekillendirme maliyeti | 6.000 ₺ |\n| I. safhadan devralınan miktar | 9.000 birim |\n| Devralınan birimlerin maliyeti | 378.000 ₺ |\n| II. safhanın şekillendirme gideri | 264.000 ₺ |\n\nDönemde 8.000 birim tamamlanarak mamul ambarına aktarılmış, 2.000 birim yarı mamul kalmıştır. II. safhada yarı mamuller şekillendirme açısından DBYM %40, DSYM %50 tamamlanmıştır; II. safhada ayrıca malzeme verilmemektedir.\n\nBuna göre, II. safhanın dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '112.400',
            'B': '30.000',
            'C': '71.600',
            'D': '113.200',
            'E': '83.200',
        },
        'D',
        'Önceki safha maliyeti II. safhaya başta girdiğinden yarı mamuller bu unsur için %100 tamamdır. Önceki safha birim maliyeti = (38.000 + 378.000) ÷ (8.000 + 2.000) = 41,60 ₺; şekillendirme = (6.000 + 264.000) ÷ (8.000 + 1.000) = 30 ₺. DSYM = 2.000 × 41,60 + 1.000 × 30 = 83.200 + 30.000 = **113.200 ₺**. Önceki safha maliyetini unutmak en sık yapılan hatadır.',
        'Maliyet muhasebesi - safha maliyeti (önceki safha maliyeti)',
    ),
    # düzey 3
    '0016': patch(
        "Tek safhada üretim yapan bir işletmede dönem başı yarı mamul yoktur. Dönemde 20.000 birimin üretimine başlanmış; 16.000 birim tamamlanmış, 2.500 birim dönem sonu yarı mamul kalmıştır. Üretim sürecinin sonundaki kontrolde 1.000 birim normal, 500 birim anormal fire tespit edilmiştir. DİMM üretimin başında verilmekte, DSYM şekillendirme açısından %40 tamamlanmış bulunmaktadır. Dönemin DİMM gideri 380.000 ₺, şekillendirme gideri 262.500 ₺'dir. Normal fire eşdeğer birime katılmamakta, anormal fire ise katılmaktadır.\n\nBuna göre, anormal fire nedeniyle dönem zararı olarak kaydedilecek tutar kaç ₺'dir?",
        {
            'A': '52.500',
            'B': '17.500',
            'C': '27.500',
            'D': '35.000',
            'E': '25.000',
        },
        'B',
        'Fire sürecin sonunda tespit edildiğinden fire birimleri her iki unsur açısından %100 tamamdır. DİMM eşdeğeri = 16.000 + 2.500 + 500 = 19.000 → 380.000 ÷ 19.000 = 20 ₺. Şekillendirme eşdeğeri = 16.000 + 1.000 + 500 = 17.500 → 262.500 ÷ 17.500 = 15 ₺. Anormal fire = 500 × 35 = **17.500 ₺** dönem zararıdır; normal firenin maliyeti sağlam birimlerin üzerinde kalır.',
        'Maliyet muhasebesi - safha maliyeti (fire)',
    ),
    # düzey 3
    '0017': patch(
        "Tek safhada üretim yapan ve ilk giren ilk çıkar (FIFO) yöntemini kullanan bir işletmede üretim kaybı yoktur. Dönem başında 800 ton yarı mamul bulunan işletmede dönemde 6.000 tonun üretimine başlanmış, 5.800 ton tamamlanmıştır. DİMM üretimin başında verilmektedir; şekillendirme açısından DBYM %25, DSYM %60 tamamlanmıştır. Maliyet bilgileri:\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 19.200 | 150.000 |\n| Direkt işçilik | 2.400 | 105.400 |\n| Genel üretim | 3.200 | 142.600 |\n\nBuna göre, dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '35.000',
            'B': '33.000',
            'C': '41.000',
            'D': '49.000',
            'E': '25.000',
        },
        'D',
        'DSYM miktarı 800 + 6.000 − 5.800 = 1.000 ton. FIFO eşdeğerleri: DİMM 5.800 − 800 + 1.000 = 6.000; şekillendirme 5.800 − 200 + 600 = 6.200. Birim maliyetler 150.000 ÷ 6.000 = 25 ₺ ve 248.000 ÷ 6.200 = 40 ₺. DSYM = 1.000 × 25 + 600 × 40 = **49.000 ₺**.',
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 2
    '0018': patch(
        'Tek safhada üretim yapan ve ilk giren ilk çıkar (FIFO) yöntemini kullanan bir işletmede üretim kaybı yoktur. Dönem başında 800 ton yarı mamul bulunan işletmede dönemde 6.000 tonun üretimine başlanmış, 5.800 ton tamamlanmıştır. DİMM üretimin başında verilmektedir; şekillendirme açısından DBYM %25, DSYM %60 tamamlanmıştır. Maliyet bilgileri:\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 19.200 | 150.000 |\n| Direkt işçilik | 2.400 | 105.400 |\n| Genel üretim | 3.200 | 142.600 |\n\nBuna göre, şekillendirme açısından eşdeğer birim sayısı kaç tondur?',
        {
            'A': '6.200',
            'B': '5.600',
            'C': '6.000',
            'D': '5.400',
            'E': '5.800',
        },
        'A',
        "FIFO: tamamlanan − DBYM'nin önceki dönemde yapılmış kısmı + DSYM eşdeğeri = 5.800 − (800 × %25) + (1.000 × %60) = 5.800 − 200 + 600 = **6.200** ton.",
        'Maliyet muhasebesi - safha maliyeti (FIFO eşdeğer birim)',
    ),
    # düzey 3
    '0019': patch(
        'Tek safhada üretim yapan ve ilk giren ilk çıkar (FIFO) yöntemini kullanan bir işletmede üretim kaybı yoktur. Dönem başında 1.200 ton yarı mamul bulunan işletmede dönemde 9.000 tonun üretimine başlanmış, 8.700 ton tamamlanmıştır. DİMM üretimin başında verilmektedir; şekillendirme açısından DBYM %30, DSYM %40 tamamlanmıştır. Maliyet bilgileri:\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 30.000 | 234.000 |\n| Direkt işçilik | 3.600 | 196.800 |\n| Genel üretim | 5.400 | 295.200 |\n\nBuna göre aşağıdaki ifadelerden hangileri doğrudur?\n\nI. DİMM açısından eşdeğer birim sayısı 9.000 tondur.\n\nII. Dönem başı yarı mamullerin şekillendirme açısından tamamlanması için bu dönemde 360 ton eşdeğer birim gerekmiştir.\n\nIII. Dönemde üretimine başlanıp aynı dönemde tamamlanan miktar 7.500 tondur.',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'E',
        'I doğrudur: 8.700 − 1.200 + 1.500 = 9.000. II yanlıştır: DBYM şekillendirme yönünden %30 tamamdır; 360 ton önceki dönemde yapılmış kısımdır, bu dönem tamamlanması için kalan %70 gerekir: 1.200 × %70 = 840 ton. III doğrudur: 8.700 tonun 1.200 tonu dönem başı yarı mamuldür; başlanıp tamamlanan 7.500 tondur.',
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 3
    '0020': patch(
        "Safha maliyeti yöntemini uygulayan bir işletmede birinci safhaya ilişkin bilgiler şöyledir:\n\n| Bilgi | Tutar |\n|---|---|\n| Üretimine başlanan | 30.000 adet |\n| Üretimi tamamlanan | 27.000 adet |\n| Dönem sonu yarı mamul | 3.000 adet |\n| Direkt ilk madde ve malzeme giderleri | 600.000 ₺ |\n| Direkt işçilik giderleri | 338.400 ₺ |\n| Genel üretim giderleri | 507.600 ₺ |\n\nDönem başında yarı mamul yoktur. Dönem sonu yarı mamuller DİMM açısından %100, şekillendirme açısından %40 tamamlanmıştır. Buna göre, dönem sonu yarı mamullerin şekillendirme giderleri toplamı kaç ₺'dir?",
        {
            'A': '54.000',
            'B': '38.160',
            'C': '90.000',
            'D': '84.600',
            'E': '36.000',
        },
        'E',
        'Şekillendirme = direkt işçilik + genel üretim = 338.400 + 507.600 = 846.000 ₺. Eşdeğer birim = 27.000 + (3.000 × %40) = 28.200; birim maliyet 846.000 ÷ 28.200 = 30 ₺. DSYM şekillendirme payı = 1.200 × 30 = **36.000 ₺**. DİMM tutarı bu soruda kullanılmaz.',
        'Maliyet muhasebesi - safha maliyeti (eşdeğer birim)',
    ),
    # düzey 2
    '0021': patch(
        'Aşağıdaki işletmelerden hangisi tipik olarak safha maliyeti sistemini kullanır?',
        {
            'A': 'İnşaat taahhüt firması',
            'B': 'Matbaa (özel kitap baskısı)',
            'C': 'Şeker fabrikası',
            'D': 'Gemi inşa (tersane)',
            'E': 'Özel tasarım mobilya atölyesi',
        },
        'C',
        '**Şeker fabrikası** sürekli, birbirinin aynı kitle üretim yaptığından safha maliyeti kullanır. Gemi, özel mobilya, özel baskı, inşaat ayırt edilebilir siparişler → sipariş maliyeti.',
        'Maliyet muhasebesi - safha maliyeti',
    ),
    # düzey 2
    '0022': patch(
        'Bir safhada dönemde 9.000 birim tamamlanmış, dönem sonunda 4.000 fiziksel birim yarı mamul kalmıştır. Safhanın toplam eşdeğer ürün miktarı 11.000 birim olarak hesaplandığına göre dönem sonu yarı mamulünün tamamlanma derecesi yüzde kaçtır?',
        {
            'A': '%50',
            'B': '%80',
            'C': '%76',
            'D': '%75',
            'E': '%56',
        },
        'A',
        'Yarı mamulün eşdeğer ürün miktarı = toplam eşdeğer − tamamlanan = 11.000 − 9.000 = 2.000 birim. Tamamlanma derecesi = eşdeğer ÷ fiziksel = 2.000 ÷ 4.000 = **%50**. (Eşdeğeri toplam eşdeğere bölmek (2.000 ÷ 11.000) anlamsızdır; bölen fiziksel yarı mamul miktarıdır.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0023': patch(
        "Bir işletmede üretim iki safhadan geçmektedir. I. safhada birim maliyeti 40 ₺ olan 5.000 birim tamamlanıp II. safhaya devredilmiştir. II. safhada bu birimler için 150.000 ₺ ek maliyet oluşmuş ve 5.000 birimin tamamı tamamlanmıştır (yarı mamul yoktur). II. safha sonunda mamulün birim maliyeti kaç ₺'dir?",
        {
            'A': '30',
            'B': '40',
            'C': '70',
            'D': '50',
            'E': '110',
        },
        'C',
        'II. safhaya devreden maliyet = 5.000 × 40 = 200.000 ₺. II. safhanın toplam maliyeti = devreden + eklenen = 200.000 + 150.000 = 350.000 ₺. Birim maliyet = 350.000 ÷ 5.000 = **70 ₺**. (Yalnız II. safhada eklenen maliyeti bölmek 30 ₺ verir; önceki safha maliyeti mamulün üzerinde taşınır.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0024': patch(
        "Bir safhada DİMM maliyeti 360.000 ₺ olup DİMM eşdeğer ürün miktarı 12.000 birim, dönüştürme maliyeti 340.000 ₺ olup dönüştürme eşdeğer ürün miktarı 10.000 birimdir. Bu safhada tamamlanmış bir birimin toplam maliyeti kaç ₺'dir?",
        {
            'A': '70',
            'B': '30',
            'C': '58,33',
            'D': '34',
            'E': '64',
        },
        'E',
        'DİMM birim maliyeti = 360.000 ÷ 12.000 = 30 ₺; dönüştürme birim maliyeti = 340.000 ÷ 10.000 = 34 ₺. Tam birim maliyeti = 30 + 34 = **64 ₺**. (Toplam maliyeti tek bir eşdeğer sayıya bölmek — 700.000 ÷ 12.000 = 58,33 — yanlıştır; her unsurun eşdeğeri ayrıdır.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0025': patch(
        'Bir işletmede üç ayrı üretim safhası (I → II → III) bulunmaktadır. Safha maliyeti sisteminde maliyet akışı nasıl gerçekleşir?',
        {
            'A': 'Önceki safhaların maliyeti dönem gideri sayılır; mamul maliyeti son safhada katlanılan giderlerden oluşur',
            'B': 'I. safhanın tamamlanan maliyeti II. safhaya, II. safhanın maliyeti III. safhaya devredilir; son safha çıktısı mamul olur',
            'C': 'Maliyet akışı geriye doğrudur; III. safhanın maliyeti II. safhaya, oradan da I. safhaya aktarılır',
            'D': 'Her safhanın maliyeti ayrı ayrı doğrudan mamuller hesabına aktarılır; safhalar arasında yarı mamul devri kaydedilmez',
            'E': 'Tamamlanan mamullerin maliyeti üretimden safhalara geri döner; maliyet mamulden safhaya doğru akar',
        },
        'B',
        "Maliyet akışı ileriye doğrudur: **I. safhanın tamamlanan birim maliyeti II. safhaya**, II. safhanınki III. safhaya devredilir (devreden maliyet). Son safhanın çıktısı bitmiş mamul olarak 152 MAMULLER'e aktarılır.",
        'Maliyet muhasebesi - safhalar arası devir',
    ),
    # düzey 2
    '0026': patch(
        "Bir safhada eşdeğer birim maliyet 55 ₺'dir. Dönem sonunda 6.000 fiziksel birim yarı mamul kalmış ve bu stokun maliyeti 165.000 ₺ olarak hesaplanmıştır. Dönem sonu yarı mamulünün tamamlanma derecesi yüzde kaçtır?",
        {
            'A': '%100',
            'B': '%80',
            'C': '%75',
            'D': '%50',
            'E': '%70',
        },
        'D',
        'Yarı mamulün eşdeğer ürün miktarı = maliyet ÷ eşdeğer birim maliyet = 165.000 ÷ 55 = 3.000 birim. Tamamlanma derecesi = 3.000 ÷ 6.000 = **%50**.',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0027': patch(
        "Bir safhada üretime başlanan 20.000 birimden 16.000'i tamamlanmış, 4.000 birim dönem sonu yarı mamul kalmıştır (DİMM %100, dönüştürme %25 tamamlanmış). DİMM maliyeti 600.000 ₺, dönüştürme maliyeti 340.000 ₺ olduğuna göre tamamlanan birimlerin toplam maliyeti kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '640.000',
            'C': '752.000',
            'D': '800.000',
            'E': '940.000',
        },
        'D',
        'DİMM eşdeğeri = 16.000 + 4.000 = 20.000 → DİMM birim = 600.000 ÷ 20.000 = 30 ₺. Dönüştürme eşdeğeri = 16.000 + (4.000 × %25) = 17.000 → dönüştürme birim = 340.000 ÷ 17.000 = 20 ₺. Tam birim = 30 + 20 = 50 ₺. Tamamlananların maliyeti = 16.000 × 50 = **800.000 ₺**. (Kalan 140.000 ₺ yarı mamule aittir.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0028': patch(
        'Aşağıdakilerden hangisi safha maliyeti sisteminin bir üstünlüğüdür?',
        {
            'A': 'Üretilen her bir mamul için ayrıntılı bir maliyet kartının tek tek ve birbirinden ayrı olarak tutulmasının zorunlu olması',
            'B': 'Genel üretim giderlerinin safhalara dağıtılmasına gerek kalmadan doğrudan mamule yüklenebilmesi',
            'C': 'Yarı mamul stoklarının dönem sonunda eşdeğer birime çevrilmeden fiziki miktarla değerlenebilmesi',
            'D': 'Her müşteri siparişinin maliyetinin ayrı ayrı izlenip siparişe özgü kârın doğrudan bulunabilmesi',
            'E': 'Birbirinin benzeri kitle üretimde maliyet takibinin sipariş sistemine göre daha basit ve az maliyetli olması',
        },
        'E',
        'Safha maliyetinde mamuller benzer olduğundan her birim için ayrı kart tutulmaz; maliyet safhada toplanıp ortalama alınır. Bu, kitle üretimde takibi sipariş sistemine göre **daha basit ve az maliyetli** kılar.',
        'Maliyet muhasebesi - safha maliyeti',
    ),
    # düzey 2
    '0029': patch(
        'Safha maliyeti sistemi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Maliyetler safhalar itibarıyla toplanır ve safha çıktısı sonraki safhaya devredilir.\n\nII. Birbirinden farklı, tek tek üretilen özel siparişlerde kullanılır.\n\nIII. Yarı mamuller eşdeğer ürüne çevrilerek birim maliyet ve maliyet dağıtımı yapılır.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'B',
        '**II yanlıştır:** Birbirinden farklı, tek tek üretilen özel siparişlerde **sipariş maliyeti** sistemi kullanılır; safha maliyeti ise **sürekli/kitle üretim** yapan işletmelere uygundur. **I** maliyetler safhalarda toplanır, çıktı sonraki safhaya devreder; **III** yarı mamuller eşdeğer ürüne çevrilir. Doğru cevap **I ve III**.',
        'Maliyet muhasebesi - safha maliyeti',
    ),
    # düzey 3
    '0030': patch(
        "Tek safhada tek tip mamul üreten ve üretim kaybı bulunmayan bir işletmenin döneme ait bilgileri aşağıdaki gibidir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul (DBYM) | 2.000 |\n| Dönemde üretime başlanan | 18.000 |\n| Dönemde tamamlanan | 16.000 |\n| Dönem sonu yarı mamul (DSYM) | 4.000 |\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 29.000 | 288.000 |\n| Direkt işçilik | 10.200 | 168.000 |\n| Genel üretim | 15.300 | 252.000 |\n\nDirekt ilk madde ve malzeme üretimin başında verilmektedir. Şekillendirme (direkt işçilik + genel üretim) açısından DBYM %60, DSYM %50 oranında tamamlanmıştır.\n\nİlk giren ilk çıkar (FIFO) yöntemine göre dönemde tamamlanan mamullerin toplam maliyeti kaç ₺'dir?",
        {
            'A': '647.400',
            'B': '628.500',
            'C': '648.500',
            'D': '594.000',
            'E': '641.000',
        },
        'C',
        "FIFO'da eşdeğer birim maliyetleri yalnız dönem maliyetinden bulunur: DİMM 288.000 ÷ 18.000 = 16 ₺; şekillendirme 420.000 ÷ 16.800 = 25 ₺. Tamamlananlar üç parçadır: DBYM'nin devreden maliyeti 54.500 ₺; DBYM'yi tamamlama 800 × 25 = 20.000 ₺; başlanıp tamamlanan 14.000 × 41 = 574.000 ₺. Toplam **648.500 ₺**. Sağlama: toplam maliyet 762.500 − DSYM 114.000 = 648.500 ₺.",
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 3
    '0031': patch(
        'Tek safhada tek tip mamul üreten ve üretim kaybı bulunmayan bir işletmenin döneme ait bilgileri aşağıdaki gibidir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul (DBYM) | 2.500 |\n| Dönemde üretime başlanan | 12.500 |\n| Dönemde tamamlanan | 12.000 |\n| Dönem sonu yarı mamul (DSYM) | 3.000 |\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 40.000 | 200.000 |\n| Direkt işçilik | 10.000 | 128.000 |\n| Genel üretim | 15.000 | 192.000 |\n\nDirekt ilk madde ve malzeme üretimin başında verilmektedir. Şekillendirme (direkt işçilik + genel üretim) açısından DBYM %40, DSYM %60 oranında tamamlanmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "FIFO'ya göre şekillendirme eşdeğer birim sayısı 13.800'dür.",
            'B': "Ortalama yönteme göre tamamlanan mamullerin maliyeti 492.000 ₺'dir.",
            'C': "FIFO yönteminde DİMM açısından eşdeğer birim sayısı 12.500'dür.",
            'D': "Ortalama yönteme göre dönem sonu yarı mamul stoku 93.000 ₺'dir.",
            'E': "Ortalama yönteme göre DİMM eşdeğer birim maliyeti 16 ₺'dir.",
        },
        'A',
        "FIFO'da şekillendirme eşdeğeri 12.000 − (2.500 × %40) + (3.000 × %60) = 12.800'dür; 13.800 ortalama yöntemin sonucudur, ifade yanlıştır. Diğerleri doğrudur: FIFO DİMM eşdeğeri 12.000 − 2.500 + 3.000 = 12.500; ortalama DİMM birim maliyeti 240.000 ÷ 15.000 = 16 ₺, şekillendirme 345.000 ÷ 13.800 = 25 ₺; tamamlanan 12.000 × 41 = 492.000 ₺; DSYM 3.000 × 16 + 1.800 × 25 = 93.000 ₺.",
        'Maliyet muhasebesi - safha maliyeti (FIFO/ortalama)',
    ),
    # düzey 3
    '0032': patch(
        "Tek safhada üretim yapan ve üretim kaybı bulunmayan bir işletmede dönem başı yarı mamul 3.000 kg, dönemde üretime başlanan 24.000 kg, dönemde tamamlanan 22.000 kg ve dönem sonu yarı mamul 5.000 kg'dır. Yarı mamullerin tamamlanma dereceleri şöyledir:\n\n| Maliyet unsuru | DBYM | DSYM |\n|---|---|---|\n| DİMM | %100 | %100 |\n| Direkt işçilik | %40 | %70 |\n| Genel üretim | %30 | %50 |\n\nDönemde katlanılan giderler: DİMM 432.000 ₺, direkt işçilik 291.600 ₺, genel üretim 354.000 ₺.\n\nİlk giren ilk çıkar (FIFO) yöntemine göre dönem başı yarı mamullerin tamamlanması için bu dönemde katlanılan maliyet kaç ₺'dir?",
        {
            'A': '135.000',
            'B': '107.100',
            'C': '81.900',
            'D': '33.300',
            'E': '53.100',
        },
        'E',
        'DBYM malzeme yönünden %100 tamam olduğundan bu dönemde DİMM eklenmez. Eksik kısımlar: direkt işçilik 3.000 × %60 = 1.800 kg × 12 ₺ = 21.600 ₺; genel üretim 3.000 × %70 = 2.100 kg × 15 ₺ = 31.500 ₺. Toplam **53.100 ₺**. Birim maliyetler dönem maliyetinin FIFO eşdeğerine bölünmesiyle bulunur (DİMM 18, DİG 12, GÜG 15 ₺).',
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 3
    '0033': patch(
        "Safha maliyet sistemini ve ortalama maliyet yöntemini kullanan bir işletmede direkt ilk madde ve malzeme üretim süreci boyunca verilmektedir. Döneme ait bilgiler şöyledir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul | 1.500 |\n| Üretime başlanan | 8.500 |\n| Tamamlanan | 8.000 |\n| Dönem sonu yarı mamul | 2.000 |\n\nDSYM direkt ilk madde ve malzeme açısından %60 tamamlanmıştır. Dönemde katlanılan DİMM gideri 196.000 ₺'dir. Buna göre, DİMM açısından eşdeğer birim maliyetinin 25 ₺ olması için dönem başı yarı mamullerin DİMM maliyeti kaç ₺ olmalıdır?",
        {
            'A': '30.500',
            'B': '34.000',
            'C': '4.000',
            'D': '14.000',
            'E': '24.000',
        },
        'B',
        'Ortalama eşdeğer birim = 8.000 + (2.000 × %60) = 9.200. Hedef toplam DİMM = 9.200 × 25 = 230.000 ₺. Ortalama yöntemde bu toplam DBYM maliyeti + dönem maliyetidir: DBYM = 230.000 − 196.000 = **34.000 ₺**.',
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 2
    '0034': patch(
        "Safha maliyet sistemini uygulayan bir işletmede dönemde 1.200 adet mamulün üretimine başlanmış, bunların 900 adedi tamamlanarak mamul ambarına alınmıştır. Dönem başında yarı mamul yoktur; dönem sonu yarı mamullerin tamamlanma derecesi bütün maliyet unsurları için %40'tır. Eşdeğer birim maliyeti 850 ₺ ise dönemde katlanılan toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '867.000',
            'B': '102.000',
            'C': '918.000',
            'D': '1.020.000',
            'E': '765.000',
        },
        'A',
        'DSYM = 1.200 − 900 = 300 adet; eşdeğeri 300 × %40 = 120. Toplam eşdeğer birim 900 + 120 = 1.020. Toplam maliyet = 1.020 × 850 = **867.000 ₺**.',
        'Maliyet muhasebesi - safha maliyeti (eşdeğer birim)',
    ),
    # düzey 3
    '0035': patch(
        "İki safhada üretim yapan ve ortalama maliyet yöntemini kullanan bir işletmenin II. safhasına ait bilgiler şöyledir:\n\n| Veri | Tutar |\n|---|---|\n| Dönem başı yarı mamul miktarı | 1.000 birim |\n| DBYM'nin önceki safha maliyeti | 38.000 ₺ |\n| DBYM'nin şekillendirme maliyeti | 6.000 ₺ |\n| I. safhadan devralınan miktar | 9.000 birim |\n| Devralınan birimlerin maliyeti | 378.000 ₺ |\n| II. safhanın şekillendirme gideri | 264.000 ₺ |\n\nDönemde 8.000 birim tamamlanarak mamul ambarına aktarılmış, 2.000 birim yarı mamul kalmıştır. II. safhada yarı mamuller şekillendirme açısından DBYM %40, DSYM %50 tamamlanmıştır; II. safhada ayrıca malzeme verilmemektedir.\n\nBuna göre, II. safhada tamamlanarak mamul ambarına aktarılan ürünlerin toplam maliyeti kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '572.000',
            'C': '572.800',
            'D': '576.000',
            'E': '686.000',
        },
        'C',
        'Birim maliyetler: önceki safha 41,60 ₺ ((38.000 + 378.000) ÷ 10.000), şekillendirme 30 ₺ ((6.000 + 264.000) ÷ 9.000). Tamamlananlar = 8.000 × 71,60 = **572.800 ₺**. Sağlama: toplam 686.000 − DSYM 113.200 = 572.800 ₺. Devralınan birim maliyeti (42 ₺) ortalama yöntemde DBYM ile birleştirildiği için doğrudan kullanılmaz.',
        'Maliyet muhasebesi - safha maliyeti (önceki safha maliyeti)',
    ),
    # düzey 3
    '0036': patch(
        "Tek safhada üretim yapan bir işletmede dönem başı yarı mamul yoktur. Dönemde 20.000 birimin üretimine başlanmış; 16.000 birim tamamlanmış, 2.500 birim dönem sonu yarı mamul kalmıştır. Üretim sürecinin sonundaki kontrolde 1.000 birim normal, 500 birim anormal fire tespit edilmiştir. DİMM üretimin başında verilmekte, DSYM şekillendirme açısından %40 tamamlanmış bulunmaktadır. Dönemin DİMM gideri 380.000 ₺, şekillendirme gideri 262.500 ₺'dir. Normal fire eşdeğer birime katılmamakta, anormal fire ise katılmaktadır.\n\nBuna göre, dönemde tamamlanan mamullerin toplam maliyeti kaç ₺'dir?",
        {
            'A': '595.000',
            'B': '560.000',
            'C': '642.500',
            'D': '577.500',
            'E': '625.000',
        },
        'B',
        'Birim maliyetler DİMM 20 ₺, şekillendirme 15 ₺ (normal fire eşdeğerden dışlandığı için maliyeti sağlam birimlere yayılmıştır). Tamamlanan = 16.000 × 35 = **560.000 ₺**. Sağlama: DSYM 65.000 ₺ + anormal fire 17.500 ₺ + tamamlanan 560.000 ₺ = 642.500 ₺.',
        'Maliyet muhasebesi - safha maliyeti (fire)',
    ),
    # düzey 3
    '0037': patch(
        "Tek safhada üretim yapan ve ilk giren ilk çıkar (FIFO) yöntemini kullanan bir işletmede üretim kaybı yoktur. Dönem başında 600 ton yarı mamul bulunan işletmede dönemde 7.000 tonun üretimine başlanmış, 6.800 ton tamamlanmıştır. DİMM üretimin başında verilmektedir; şekillendirme açısından DBYM %20, DSYM %50 tamamlanmıştır. Maliyet bilgileri:\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 15.000 | 175.000 |\n| Direkt işçilik | 1.800 | 141.600 |\n| Genel üretim | 2.400 | 212.400 |\n\nBuna göre, dönem başındaki 600 ton yarı mamulün tamamlanmasıyla elde edilen mamullerin toplam maliyeti kaç ₺'dir?",
        {
            'A': '19.200',
            'B': '49.200',
            'C': '38.400',
            'D': '43.200',
            'E': '24.000',
        },
        'D',
        "FIFO'da DBYM ayrı bir parti gibi izlenir: devreden maliyeti 15.000 + 1.800 + 2.400 = 19.200 ₺. Şekillendirme eşdeğeri 6.800 − 120 + 400 = 7.080; birim maliyet 354.000 ÷ 7.080 = 50 ₺. Malzeme başta verildiğinden bu dönem yalnız şekillendirme eklenir: 600 × %80 = 480 ton × 50 ₺ = 24.000 ₺. Toplam 43.200 ₺.",
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 3
    '0038': patch(
        "Ağırlıklı ortalama maliyet yöntemini kullanan, tek safhada üretim yapan bir işletmede üretim kaybı yoktur. Dönem başında 3.000 birim yarı mamul bulunmakta olup bunların DİMM maliyeti 60.000 ₺, şekillendirme maliyeti 21.000 ₺'dir. Dönemde 9.000 birimin üretimine başlanmış, 10.000 birim tamamlanmıştır. Dönem giderleri DİMM 204.000 ₺, direkt işçilik 78.000 ₺, genel üretim 117.000 ₺'dir. DİMM üretimin başında verilmekte; yarı mamuller şekillendirme açısından DBYM %50, DSYM %40 tamamlanmış bulunmaktadır.\n\nBuna göre, dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '84.000',
            'B': '44.000',
            'C': '60.000',
            'D': '64.000',
            'E': '68.000',
        },
        'C',
        "DSYM miktarı 3.000 + 9.000 − 10.000 = 2.000 birim. Birim maliyetler DİMM 22 ₺, şekillendirme 20 ₺. DSYM = 2.000 × 22 + 800 × 20 = 44.000 + 16.000 = **60.000 ₺**. DBYM'nin tamamlanma derecesi (%50) ortalama yöntemde kullanılmaz.",
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 2
    '0039': patch(
        'Safha maliyet sisteminde eşdeğer birim hesaplama yöntemleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. FIFO yönteminde dönem başı yarı mamullerin önceki dönemden devreden maliyeti, eşdeğer birim maliyetinin hesaplanmasında dönem maliyetine eklenir.\n\nII. Ortalama yöntemde dönem başı yarı mamullerin tamamlanma derecesi, eşdeğer birim sayısını azaltır.\n\nIII. Dönem başında yarı mamul stoku bulunmuyorsa iki yöntem aynı eşdeğer birim sayısını verir.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'E',
        "**I yanlıştır:** DBYM maliyetini dönem maliyetine ekleyip ortalama alan, ortalama yöntemdir; FIFO'da birim maliyet yalnız dönem maliyetinden bulunur, DBYM maliyeti doğrudan tamamlananlara aktarılır. **II yanlıştır:** DBYM'nin tamamlanma derecesini düşen FIFO'dur; ortalama yöntemde eşdeğer birim = tamamlanan + DSYM eşdeğeri. **III doğrudur:** FIFO'da düşülen tek kalem DBYM eşdeğeridir; DBYM yoksa iki formül aynı sonucu verir.",
        'Maliyet muhasebesi - ortalama/FIFO',
    ),
    # düzey 3
    '0040': patch(
        "Ortalama maliyet yöntemini kullanan bir işletmede dönem başı yarı mamullerin direkt işçilik maliyeti 18.000 ₺, dönemde katlanılan direkt işçilik gideri 262.000 ₺'dir. Dönemde 13.000 birim tamamlanmış, 2.500 birim dönem sonu yarı mamul kalmıştır; üretim kaybı yoktur. Eşdeğer birim başına direkt işçilik gideri 20 ₺ olarak hesaplandığına göre dönem sonu yarı mamullerin direkt işçilik açısından tamamlanma derecesi yüzde kaçtır?",
        {
            'A': '%80',
            'B': '%50',
            'C': '%4',
            'D': '%40',
            'E': '%60',
        },
        'D',
        'Ortalama yöntemde birim maliyet = (DBYM + dönem) ÷ eşdeğer birim. Eşdeğer birim = (18.000 + 262.000) ÷ 20 = 14.000. DSYM eşdeğeri = 14.000 − 13.000 = 1.000; tamamlanma derecesi 1.000 ÷ 2.500 = **%40**. DBYM maliyetini unutup yalnız 262.000 ÷ 20 = 13.100 alan, derecenin %4 olduğunu bulur.',
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 2
    '0041': patch(
        'Sipariş maliyeti ile safha maliyeti sistemi arasındaki temel fark aşağıdakilerden hangisidir?',
        {
            'A': 'Safha maliyetinde genel üretim giderleri mamule yüklenmez; doğrudan dönem gideri olarak gelir tablosuna aktarılır',
            'B': 'Sipariş maliyeti sürekli ve birbirinin benzeri kitle üretim yapan işletmelerde, safha maliyeti ise özel siparişlerde kullanılır',
            'C': 'Sipariş maliyetinde maliyet siparişe/işe; safha maliyetinde ise üretim aşamalarına (safhalara) göre toplanır',
            'D': 'Sipariş maliyetinde yarı mamuller eşdeğer birime çevrilir; safha maliyetinde her iş için ayrı maliyet kartı tutulur',
            'E': 'Safha maliyetinde birim maliyet dönem sonunda tamamlanan mamul sayısına bölünerek bulunur; yarı mamul dikkate alınmaz',
        },
        'C',
        'Temel fark maliyetin toplanma biriminde: **sipariş maliyetinde** her sipariş/iş ayrı; **safha maliyetinde** üretim **aşamaları (safhalar)** itibarıyla toplanır.',
        'Maliyet muhasebesi - sipariş vs safha',
    ),
    # düzey 2
    '0042': patch(
        'Safha maliyeti sistemi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Birbirinden farklı, tek tek ayırt edilebilen siparişlerin üretiminde kullanılır.\n\nII. Maliyetler safhalar itibarıyla toplanır.\n\nIII. Yarı mamuller eşdeğer ürüne çevrilerek birim maliyet hesaplanır.',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'A',
        '**I yanlıştır:** Tek tek ayırt edilebilen, birbirinden farklı siparişlerin üretimi SİPARİŞ maliyeti sisteminin konusudur; safha (evre) maliyeti ise SÜREKLİ, kitle ve birbirinin benzeri üretimde kullanılır. **II** maliyetlerin safhalar itibarıyla toplanması ve **III** yarı mamullerin eşdeğer ürüne çevrilerek birim maliyet hesaplanması doğrudur. Doğru cevap **II ve III**.',
        'Maliyet muhasebesi - safha maliyeti',
    ),
    # düzey 2
    '0043': patch(
        "Safha maliyeti sisteminde 'ortalama maliyet yöntemi' ile 'ilk giren ilk çıkar (FIFO) yöntemi' arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'FIFO yönteminde dönem başı yarı mamullerin maliyeti ile dönem maliyetleri ayrı tutulur; ortalama yöntemde bunlar birleştirilerek ortalama alınır',
            'B': 'FIFO yönteminde dönem sonu yarı mamuller dönem başı stokun birim maliyetiyle, tamamlananlar dönem maliyetiyle değerlenir',
            'C': 'Ortalama yöntemde eşdeğer ürün kullanılmaz; yarı mamuller doğrudan tamamlanmış birim gibi sayılarak birim maliyet bulunur',
            'D': 'İki yöntem tamamen aynıdır; dönem başı yarı mamulün maliyeti her ikisinde de aynı biçimde işleme alınır',
            'E': 'Ortalama yöntemde dönem başı yarı mamullerin tamamlanma derecesi eşdeğer birimden düşülür; FIFO yönteminde bu düşme yapılmaz',
        },
        'A',
        '**FIFO** yönteminde dönem başı yarı mamullerin maliyeti dönem maliyetlerinden ayrı izlenir (önce başlayan önce biter mantığı). **Ortalama** yöntemde ise dönem başı yarı mamul maliyeti ile dönem maliyetleri birleştirilip ortalama birim maliyet bulunur.',
        'Maliyet muhasebesi - ortalama/FIFO',
    ),
    # düzey 2
    '0044': patch(
        "Bir safhaya 10.000 birim girmiştir. Dönemde 500 birim normal fire, 500 birim de anormal fire oluşmuş; kalan 9.000 birim tamamlanmıştır. Safhanın toplam maliyeti 475.000 ₺ olduğuna göre anormal fire nedeniyle döneme zarar olarak yazılacak tutar kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '25.000',
            'C': '475.000',
            'D': '23.750',
            'E': '0',
        },
        'B',
        'Anormal fire maliyeti mamule yüklenmez, ayrıca zarar yazılır; bu nedenle eşdeğer ürüne dahil edilir: 9.000 sağlam + 500 anormal fire = 9.500 birim. Birim maliyet = 475.000 ÷ 9.500 = 50 ₺. Zarar yazılacak tutar = 500 × 50 = **25.000 ₺**. Normal fire ise sağlam birimlere yüklenir.',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0045': patch(
        'Eşdeğer ürün ve safha birim maliyeti ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Eşdeğer ürün = tamamlanan + (yarı mamul × tamamlanma derecesi).\n\nII. DİMM safha başında veriliyorsa yarı mamul malzeme yönünden genelde %100 sayılır.\n\nIII. Eşdeğer birim maliyet = toplam maliyet ÷ eşdeğer ürün.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'E',
        'Üçü de doğrudur: **I** eşdeğer ürün formülü; **II** DİMM başta veriliyorsa yarı mamul malzeme yönünden %100; **III** eşdeğer birim maliyet = toplam ÷ eşdeğer ürün. Doğru cevap **I, II ve III**.',
        'Maliyet muhasebesi - eşdeğer ürün',
    ),
    # düzey 2
    '0046': patch(
        "Safha maliyeti sisteminde 'fire (kayıp)' aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'Satılan mamulün ayıplı çıkması nedeniyle müşteri tarafından işletmeye geri gönderilmesi durumu (satış iadesi)',
            'B': 'Üretim sürecinde buharlaşma, kırılma, kesinti gibi nedenlerle miktarda meydana gelen azalma (üretim kaybı)',
            'C': 'Dönem sonunda dağıtılmak üzere ortaklara ayrılan kâr payının üretim maliyetine eklenen tutarı',
            'D': 'Duran varlıkların yıpranma payının dönem üretim maliyetine yüklenen kısmı (amortisman gideri)',
            'E': 'Devlete ödenen dolaylı vergilerin üretilen mamulün maliyetinden indirilen kısmı (vergi indirimi)',
        },
        'B',
        '**Fire (kayıp)**, üretim sürecinde buharlaşma, kırılma, kesinti, kuruma gibi nedenlerle üretim miktarında meydana gelen azalmadır. Normal fire maliyete yüklenir; anormal fire ise dönem gideri/zararı olarak ayrılabilir.',
        'Maliyet muhasebesi - fire',
    ),
    # düzey 2
    '0047': patch(
        "Bir safhada DİMM maliyeti 600.000 ₺ (eşdeğer ürün 20.000 birim), dönüştürme maliyeti 340.000 ₺ (eşdeğer ürün 17.000 birim) olarak hesaplanmıştır. Dönem sonunda 4.000 birim yarı mamul kalmıştır; bu birimler DİMM bakımından %100, dönüştürme bakımından %25 tamamlanmıştır. Dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '188.000',
            'C': '200.000',
            'D': '140.000',
            'E': '50.000',
        },
        'D',
        'DİMM birim = 600.000 ÷ 20.000 = 30 ₺; dönüştürme birim = 340.000 ÷ 17.000 = 20 ₺. Yarı mamulün DİMM payı = 4.000 × 30 = 120.000 ₺; dönüştürme payı = (4.000 × %25) × 20 = 1.000 × 20 = 20.000 ₺. Toplam = 120.000 + 20.000 = **140.000 ₺**. (İki unsuru da %100 saymak 4.000 × 50 = 200.000 ₺ verir.)',
        'Maliyet muhasebesi - safha maliyeti (çok adımlı)',
    ),
    # düzey 2
    '0048': patch(
        'Safha maliyeti sisteminde son safhada tamamlanan mamuller hangi hesaba aktarılır?',
        {
            'A': '710 DİREKT İLK MADDE VE MALZEME GİDERLERİ',
            'B': '600 YURT İÇİ SATIŞLAR',
            'C': '152 MAMULLER',
            'D': '320 SATICILAR',
            'E': '151 YARI MAMULLER – ÜRETİM',
        },
        'C',
        "Son safhada tamamlanan mamullerin maliyeti **152 MAMULLER** hesabına aktarılır. Ara safhalardaki devam eden üretim ise 151 YARI MAMULLER – ÜRETİM'de izlenir.",
        'TDHP 152 Mamuller',
    ),
    # düzey 2
    '0049': patch(
        'Tek safhada tek tip mamul üreten ve üretim kaybı bulunmayan bir işletmenin döneme ait bilgileri aşağıdaki gibidir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul (DBYM) | 3.000 |\n| Dönemde üretime başlanan | 25.000 |\n| Dönemde tamamlanan | 24.000 |\n| Dönem sonu yarı mamul (DSYM) | 4.000 |\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 66.000 | 575.000 |\n| Direkt işçilik | 9.000 | 258.000 |\n| Genel üretim | 13.500 | 387.000 |\n\nDirekt ilk madde ve malzeme üretimin başında verilmektedir. Şekillendirme (direkt işçilik + genel üretim) açısından DBYM %40, DSYM %75 oranında tamamlanmıştır.\n\nİlk giren ilk çıkar (FIFO) yöntemine göre şekillendirme açısından eşdeğer birim sayısı kaçtır?',
        {
            'A': '25.800',
            'B': '27.000',
            'C': '24.000',
            'D': '26.200',
            'E': '28.000',
        },
        'A',
        "FIFO'da DBYM'nin önceki dönemde yapılmış kısmı düşülür: 24.000 − (3.000 × %40) + (4.000 × %75) = 24.000 − 1.200 + 3.000 = 25.800. Aynı sonuç: DBYM'yi tamamlama 1.800 + başlanıp tamamlanan 21.000 + DSYM 3.000. Ortalama yöntemde düşme yapılmaz ve sonuç 27.000 olur.",
        'Maliyet muhasebesi - safha maliyeti (FIFO eşdeğer birim)',
    ),
    # düzey 3
    '0050': patch(
        "Tek safhada tek tip mamul üreten ve üretim kaybı bulunmayan bir işletmenin döneme ait bilgileri aşağıdaki gibidir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul (DBYM) | 1.500 |\n| Dönemde üretime başlanan | 13.500 |\n| Dönemde tamamlanan | 12.000 |\n| Dönem sonu yarı mamul (DSYM) | 3.000 |\n\n| Maliyet unsuru | DBYM maliyeti (₺) | Dönem maliyeti (₺) |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 21.000 | 204.000 |\n| Direkt işçilik | 6.000 | 99.600 |\n| Genel üretim | 9.000 | 149.400 |\n\nDirekt ilk madde ve malzeme üretimin başında verilmektedir. Şekillendirme (direkt işçilik + genel üretim) açısından DBYM %50, DSYM %40 oranında tamamlanmıştır.\n\nAğırlıklı ortalama maliyet yöntemine göre dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '105.000',
            'B': '69.000',
            'C': '45.000',
            'D': '72.000',
            'E': '60.000',
        },
        'B',
        'Ortalama birim maliyetler: DİMM (21.000 + 204.000) ÷ 15.000 = 15 ₺; şekillendirme (15.000 + 249.000) ÷ (12.000 + 1.200) = 20 ₺. DSYM: DİMM 3.000 × 15 = 45.000 ₺ + şekillendirme 1.200 × 20 = 24.000 ₺ = 69.000 ₺. Sağlama: tamamlanan 12.000 × 35 = 420.000 ₺; 420.000 + 69.000 = 489.000 ₺.',
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 2
    '0051': patch(
        "Tek safhada üretim yapan ve üretim kaybı bulunmayan bir işletmede dönem başı yarı mamul 3.000 kg, dönemde üretime başlanan 24.000 kg, dönemde tamamlanan 22.000 kg ve dönem sonu yarı mamul 5.000 kg'dır. Yarı mamullerin tamamlanma dereceleri şöyledir:\n\n| Maliyet unsuru | DBYM | DSYM |\n|---|---|---|\n| DİMM | %100 | %100 |\n| Direkt işçilik | %40 | %70 |\n| Genel üretim | %30 | %50 |\n\nİlk giren ilk çıkar (FIFO) yöntemine göre direkt işçilik açısından eşdeğer birim sayısı kaçtır?",
        {
            'A': '23.600',
            'B': '23.700',
            'C': '25.500',
            'D': '24.300',
            'E': '22.500',
        },
        'D',
        "FIFO: 22.000 − (3.000 × %40) + (5.000 × %70) = 22.000 − 1.200 + 3.500 = **24.300** kg. Her unsurun eşdeğeri kendi tamamlanma derecesiyle ayrı hesaplanır; genel üretim için sonuç 23.600 kg'dır.",
        'Maliyet muhasebesi - safha maliyeti (FIFO eşdeğer birim)',
    ),
    # düzey 3
    '0052': patch(
        "Tek safhada üretim yapan ve üretim kaybı bulunmayan bir işletmede dönem başı yarı mamul 3.000 kg, dönemde üretime başlanan 24.000 kg, dönemde tamamlanan 22.000 kg ve dönem sonu yarı mamul 5.000 kg'dır. Yarı mamullerin tamamlanma dereceleri şöyledir:\n\n| Maliyet unsuru | DBYM | DSYM |\n|---|---|---|\n| DİMM | %100 | %100 |\n| Direkt işçilik | %40 | %70 |\n| Genel üretim | %30 | %50 |\n\nDönemde katlanılan giderler: DİMM 432.000 ₺, direkt işçilik 291.600 ₺, genel üretim 354.000 ₺.\n\nİlk giren ilk çıkar (FIFO) yöntemine göre dönem sonu yarı mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '169.500',
            'B': '225.000',
            'C': '136.500',
            'D': '79.500',
            'E': '157.500',
        },
        'A',
        'FIFO birim maliyetleri: DİMM 432.000 ÷ 24.000 = 18 ₺; direkt işçilik 291.600 ÷ 24.300 = 12 ₺; genel üretim 354.000 ÷ 23.600 = 15 ₺. DSYM = 5.000 × 18 + 3.500 × 12 + 2.500 × 15 = 90.000 + 42.000 + 37.500 = **169.500 ₺**.',
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
    ),
    # düzey 3
    '0053': patch(
        'Tek tip mamulü tek safhada üreten ve ortalama maliyet yöntemini kullanan bir işletmede dönem başında yarı mamul stoku yoktur. Dönemde 6.000 birimin üretimine başlanmış, 4.800 birim tamamlanmıştır; üretim kaybı yoktur. Dönemin giderleri şöyledir:\n\n| Gider | Tutar (₺) |\n|---|---|\n| Direkt ilk madde ve malzeme | 600.000 |\n| Direkt işçilik | 108.000 |\n| Genel üretim | 135.000 |\n\nEşdeğer birim maliyetleri DİMM açısından 100 ₺, şekillendirme açısından 45 ₺ olarak hesaplanmıştır. Buna göre, dönem sonu yarı mamullerin şekillendirme açısından tamamlanma derecesi yüzde kaçtır?',
        {
            'A': '%40',
            'B': '%50',
            'C': '%75',
            'D': '%25',
            'E': '%60',
        },
        'B',
        "DİMM eşdeğeri 600.000 ÷ 100 = 6.000 birimdir; yani DSYM malzeme yönünden %100'dür. Şekillendirme eşdeğeri = (108.000 + 135.000) ÷ 45 = 5.400 birim. DSYM = 6.000 − 4.800 = 1.200 birim; şekillendirme eşdeğeri 5.400 − 4.800 = 600 birim. Tamamlanma derecesi 600 ÷ 1.200 = **%50**.",
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 2
    '0054': patch(
        'İki safhada üretim yapan ve üretim kaybı bulunmayan bir işletmenin adet cinsinden miktar bilgileri şöyledir:\n\n| Miktar | I. Safha | II. Safha |\n|---|---|---|\n| Dönem başı yarı mamul | 6.000 | 9.000 |\n| Dönem sonu yarı mamul | 4.000 | 7.000 |\n| Dönemde üretime alınan | 50.000 | ? |\n| Dönemde tamamlanan | ? | ? |\n\nBuna göre, II. safhada üretime alınan ve tamamlanan miktarlar sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
        {
            'A': '48.000 ve 50.000',
            'B': '50.000 ve 52.000',
            'C': '52.000 ve 54.000',
            'D': '52.000 ve 50.000',
            'E': '54.000 ve 52.000',
        },
        'C',
        'I. safha: tamamlanan = DBYM + alınan − DSYM = 6.000 + 50.000 − 4.000 = 52.000. I. safhada tamamlananlar II. safhanın üretime aldığı miktardır: 52.000. II. safha tamamlanan = 9.000 + 52.000 − 7.000 = 54.000. Cevap **52.000 ve 54.000**.',
        'Maliyet muhasebesi - safha maliyeti (miktar sağlama)',
    ),
    # düzey 3
    '0055': patch(
        'İki safhada üretim yapan bir işletmenin yarı mamul bilgileri şöyledir:\n\n| Miktar (birim) | I. Safha | II. Safha |\n|---|---|---|\n| Dönem başı yarı mamul | 8.000 | 10.000 |\n| Dönem sonu yarı mamul | 12.000 | 15.000 |\n\nMiktar sağlama tablosunda üretime giren ve üretimden çıkan toplam miktar I. safhada 90.000, II. safhada 88.000 birimdir. Üretim kaybı bulunmadığına göre II. safhada dönemde tamamlanan miktar kaç birimdir?',
        {
            'A': '78.000',
            'B': '63.000',
            'C': '68.000',
            'D': '83.000',
            'E': '73.000',
        },
        'E',
        'Sağlama toplamı = DBYM + üretime alınan = tamamlanan + DSYM. I. safha: alınan 90.000 − 8.000 = 82.000, tamamlanan 90.000 − 12.000 = 78.000. II. safha: alınan 88.000 − 10.000 = 78.000 (I. safhanın tamamladığıyla tutarlı), tamamlanan 88.000 − 15.000 = **73.000** birim.',
        'Maliyet muhasebesi - safha maliyeti (miktar sağlama)',
    ),
    # düzey 3
    '0056': patch(
        "İki safhada üretim yapan ve ilk giren ilk çıkar (FIFO) yöntemini kullanan bir işletmenin II. safhasına ait bilgiler şöyledir:\n\n| Veri | Tutar |\n|---|---|\n| Dönem başı yarı mamul miktarı | 1.500 birim |\n| DBYM'nin önceki safha maliyeti | 63.000 ₺ |\n| DBYM'nin şekillendirme maliyeti | 9.000 ₺ |\n| I. safhadan devralınan miktar | 12.000 birim |\n| Devralınan birimlerin maliyeti | 504.000 ₺ |\n| II. safhanın şekillendirme gideri | 325.500 ₺ |\n\nDönemde 11.000 birim tamamlanarak mamul ambarına aktarılmış, 2.500 birim yarı mamul kalmıştır. II. safhada yarı mamuller şekillendirme açısından DBYM %60, DSYM %30 tamamlanmıştır; II. safhada ayrıca malzeme verilmemektedir.\n\nBuna göre, II. safhada önceki safha maliyeti ve şekillendirme açısından eşdeğer birim sayıları sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
        {
            'A': '12.000 ve 10.850',
            'B': '12.000 ve 12.000',
            'C': '13.500 ve 10.850',
            'D': '11.000 ve 10.850',
            'E': '13.500 ve 11.750',
        },
        'A',
        'Önceki safha maliyeti açısından DBYM ve DSYM %100 tamamdır: 11.000 − 1.500 + 2.500 = 12.000 (devralınan miktara eşittir). Şekillendirme: 11.000 − (1.500 × %60) + (2.500 × %30) = 11.000 − 900 + 750 = 10.850. Cevap 12.000 ve 10.850.',
        'Maliyet muhasebesi - safha maliyeti (önceki safha maliyeti)',
    ),
    # düzey 3
    '0057': patch(
        "Tek safhada üretim yapan bir işletmenin döneme ait miktar bilgileri şöyledir:\n\n| Miktar verileri | Birim |\n|---|---|\n| Dönem başı yarı mamul | 3.000 |\n| Dönemde üretime başlanan | 25.000 |\n| Dönemde tamamlanan | 24.000 |\n| Dönem sonu yarı mamul | 2.500 |\n\nİşletmede dönemde üretime başlanan miktarın %4'ü normal fire kabul edilmekte, bunu aşan kayıp anormal fire sayılmaktadır. Buna göre, dönemin anormal fire miktarı kaç birimdir?",
        {
            'A': '1.500',
            'B': '380',
            'C': '540',
            'D': '1.000',
            'E': '500',
        },
        'E',
        'Toplam fire = girişler − çıkışlar = (3.000 + 25.000) − (24.000 + 2.500) = 1.500 birim. Normal fire = 25.000 × %4 = 1.000 birim. Anormal fire = 1.500 − 1.000 = **500** birim. Normal fire oranı başlanan miktara uygulanır, DBYM eklenmez.',
        'Maliyet muhasebesi - safha maliyeti (fire)',
    ),
    # düzey 3
    '0058': patch(
        "Ağırlıklı ortalama maliyet yöntemini kullanan, tek safhada üretim yapan bir işletmede üretim kaybı yoktur. Dönem başında 3.000 birim yarı mamul bulunmakta olup bunların DİMM maliyeti 60.000 ₺, şekillendirme maliyeti 21.000 ₺'dir. Dönemde 9.000 birimin üretimine başlanmış, 10.000 birim tamamlanmıştır. Dönem giderleri DİMM 204.000 ₺, direkt işçilik 78.000 ₺, genel üretim 117.000 ₺'dir. DİMM üretimin başında verilmekte; yarı mamuller şekillendirme açısından DBYM %50, DSYM %40 tamamlanmış bulunmaktadır.\n\nBuna göre, tamamlanan bir birim mamulün maliyeti kaç ₺'dir?",
        {
            'A': '42',
            'B': '48',
            'C': '40',
            'D': '43,60',
            'E': '37',
        },
        'A',
        'DİMM birim = (60.000 + 204.000) ÷ (10.000 + 2.000) = 22 ₺. Şekillendirme birim = (21.000 + 78.000 + 117.000) ÷ (10.000 + 800) = 20 ₺. Tamamlanan birim maliyet **42 ₺**. Toplam maliyeti tek bir eşdeğere bölmek yanlıştır; her unsurun eşdeğeri ayrıdır.',
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 3
    '0059': patch(
        "Ağırlıklı ortalama maliyet yöntemini kullanan, tek safhada üretim yapan bir işletmede üretim kaybı yoktur. Dönem başında 2.000 birim yarı mamul bulunmakta olup bunların DİMM maliyeti 50.000 ₺, şekillendirme maliyeti 18.000 ₺'dir. Dönemde 10.000 birimin üretimine başlanmış, 9.000 birim tamamlanmıştır. Dönem giderleri DİMM 262.000 ₺, direkt işçilik 100.800 ₺, genel üretim 151.200 ₺'dir. DİMM üretimin başında verilmekte; yarı mamuller şekillendirme açısından DBYM %40, DSYM %60 tamamlanmış bulunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Dönem sonu yarı mamul stokunun maliyeti 123.000 ₺'dir.",
            'B': "DİMM açısından eşdeğer birim sayısı 12.000'dir.",
            'C': "Tamamlanan mamullerin toplam maliyeti 477.000 ₺'dir.",
            'D': "Şekillendirme açısından eşdeğer birim sayısı 10.800'dür.",
            'E': "Şekillendirme açısından eşdeğer birim maliyeti 25 ₺'dir.",
        },
        'C',
        "Tamamlanan mamuller 9.000 × (26 + 25) = 459.000 ₺'dir; 477.000 ₺ DBYM şekillendirme maliyetinin iki kez sayılmasıyla bulunur, ifade yanlıştır. Diğerleri doğrudur: DİMM eşdeğeri 9.000 + 3.000 = 12.000, birim 312.000 ÷ 12.000 = 26 ₺; şekillendirme eşdeğeri 9.000 + 1.800 = 10.800, birim 270.000 ÷ 10.800 = 25 ₺; DSYM 3.000 × 26 + 1.800 × 25 = 123.000 ₺. Sağlama: 459.000 + 123.000 = 582.000 ₺.",
        'Maliyet muhasebesi - safha maliyeti (ortalama yöntem)',
    ),
    # düzey 3
    '0060': patch(
        "Tek safhada üretim yapan ve ilk giren ilk çıkar (FIFO) yöntemini kullanan bir işletmede üretim kaybı yoktur. Yarı mamuller DİMM açısından %100 tamamdır. Haziran ayı bilgileri şöyledir:\n\n| Bilgi | Adet |\n|---|---|\n| Dönem başı yarı mamul | 4.000 |\n| Dönemde üretime başlanan | 12.500 |\n| Dönemde tamamlanan | 14.000 |\n| DSYM'nin şekillendirme açısından eşdeğer birimi | 1.500 |\n| Şekillendirme açısından toplam eşdeğer birim (FIFO) | 14.300 |\n\nBuna göre, dönem başı yarı mamullerin şekillendirme açısından tamamlanma derecesi yüzde kaçtır?",
        {
            'A': '%40',
            'B': '%70',
            'C': '%60',
            'D': '%25',
            'E': '%30',
        },
        'E',
        "DSYM miktarı = 4.000 + 12.500 − 14.000 = 2.500 adet (DSYM tamamlanma derecesi 1.500 ÷ 2.500 = %60). FIFO: 14.000 − (4.000 × x) + 1.500 = 14.300 → 4.000x = 1.200 → x = **%30**. Yani DBYM'nin %70'u bu dönemde tamamlanmıştır.",
        'Maliyet muhasebesi - safha maliyeti (FIFO)',
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
    print(f"1 paket / {len(PATCHES)} soru ('Safha Maliyeti' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
