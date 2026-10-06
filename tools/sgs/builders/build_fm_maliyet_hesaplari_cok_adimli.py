#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maliyet Hesaplari — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. 51 soru korundu; 9 'hangi hesapta izlenir' ezberi cikarildi, 12 mutlak ifadeli sik onarildi. Yerine 7/A akisinin cok adimli sorulari: tamamlanan uretimin 152'ye ve satilan mamullerin 620'ye aktarimi, yansitma kaydi (olumsuz), amortismanin ve ucretin fonksiyonlara dagitimi, ilk madde kullaniminin direkt/endirekt ayrimi, 7/B hesabi, uretim maliyetine girmeyen gider, oncullu soru. '710' atma-sikki tekrari 5 -> 3'e indirildi. Kor ogrenci %20.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Tekduzen Hesap Plani 7 Maliyet Hesaplari (7/A, 7/B), 15, 62 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/maliyet_hesaplari.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-mlh-gen-"


def patch(stem, options, answer, solution, ref='Tekduzen Hesap Plani 7 Maliyet Hesaplari'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Maliyet hesaplarında '7/A' ve '7/B' seçenekleri ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '7/A giderleri fonksiyon (işlev) esasına göre (yansıtma hesaplarıyla) izler ve genellikle büyük işletmelerce; 7/B ise giderleri çeşit esasına göre izler ve genellikle küçük işletmelerce kullanılır.',
            'B': '7/A küçük işletmeler için basit çeşit esasını, 7/B ise büyük işletmeler için ayrıntılı fonksiyon esasını temsil eder.',
            'C': '7/A satış ve iade işlemlerini, 7/B ise dönem içi alış ve stok hareketlerini izlemek için kullanılır.',
            'D': '7/A ve 7/B seçeneklerinin ikisi de bilanço hesabıdır ve dönem sonunda varlık olarak aktife devredilir.',
            'E': '7/A ile 7/B tamamen aynı hesapları içerir; işletme dilerse ikisini aynı dönemde birlikte kullanarak giderlerini hem çeşit hem de fonksiyon esasına göre iki ayrı defterde ayrıntılı çift kayıtla izleyebilir.',
        },
        'A',
        '**7/A** giderleri **fonksiyon (işlev) esasına** göre, yansıtma hesaplarıyla izler (büyük işletmeler); **7/B** giderleri **çeşit esasına** göre (790-799) izler (küçük işletmeler). İşletme büyüklüğüne göre biri seçilir.',
        "1 Sıra No'lu MSUGT - 7/A ve 7/B",
    ),
    # düzey 2
    '0002': patch(
        "7/A seçeneğinde üretim gider hesaplarının (710, 720, 730) yansıtılmasıyla oluşan üretim maliyeti, tamamlanmamış üretim için Tekdüzen Hesap Planı'nda hangi hesaba aktarılır?",
        {
            'A': '600 Yurt İçi Satışlar',
            'B': '621 Satılan Ticari Mallar Maliyeti (-)',
            'C': '632 Genel Yönetim Giderleri (-)',
            'D': '320 Satıcılar',
            'E': '151 Yarı Mamuller - Üretim',
        },
        'E',
        "Üretim giderleri (710/720/730) yansıtma hesapları aracılığıyla, tamamlanmamış üretim için **151 Yarı Mamuller - Üretim** hesabına aktarılır; üretim tamamlanınca 152 Mamuller'e geçer.",
        "1 Sıra No'lu MSUGT - 151 / 711-721-731",
    ),
    # düzey 2
    '0003': patch(
        'Üretim maliyetinin üç temel unsuru aşağıdakilerden hangisinde birlikte ve doğru verilmiştir?',
        {
            'A': 'Sermaye + Yedekler + Dönem kârı',
            'B': 'Kasa + Banka + Alacaklar',
            'C': 'Satışlar + Satış iadeleri + Satış iskontoları',
            'D': 'Direkt ilk madde ve malzeme + Direkt işçilik + Genel üretim giderleri',
            'E': 'Pazarlama giderleri + Genel yönetim giderleri + Finansman giderleri',
        },
        'D',
        'Üretim maliyetinin üç temel unsuru: **Direkt İlk Madde ve Malzeme (710) + Direkt İşçilik (720) + Genel Üretim Giderleri (730)**.',
        "1 Sıra No'lu MSUGT - 710/720/730",
    ),
    # düzey 2
    '0004': patch(
        '7/A seçeneğini kullanan bir üretim işletmesi, ambardan üretime 200.000 ₺ direkt hammadde ve 30.000 ₺ işletme malzemesi vermiştir. İşletme malzemesi endirekt niteliktedir.\n\nMalzemelerin üretime verilmesine ilişkin kayıt hangisidir?',
        {
            'A': '151 Yarı Mamuller - Üretim 230.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak',
            'B': '710 Direkt İlk Madde ve Malzeme Giderleri 230.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak',
            'C': '710 Direkt İlk Madde ve Malzeme Giderleri 200.000 ₺ ve 730 Genel Üretim Giderleri 30.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak',
            'D': '710 Direkt İlk Madde ve Malzeme Giderleri 200.000 ₺ ve 770 Genel Yönetim Giderleri 30.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak',
            'E': '150 İlk Madde ve Malzeme 230.000 ₺ borç / 710 Direkt İlk Madde ve Malzeme Giderleri 200.000 ₺ ve 730 Genel Üretim Giderleri 30.000 ₺ alacak',
        },
        'C',
        'Mamule doğrudan izlenebilen 200.000 ₺ hammadde **710** hesaba, endirekt nitelikteki 30.000 ₺ işletme malzemesi **730** hesaba borç kaydedilir. Stoktan toplam 230.000 ₺ çıktığı için 150 hesap alacaklandırılır.',
        "1 Sıra No'lu MSUGT - 150/710/730; 18 Temmuz 2026 SGS 7/A malzeme kullanımı soru örüntüsü",
    ),
    # düzey 3
    '0005': patch(
        "Dönemde tahakkuk eden brüt ücretlerin 250.000 ₺'si mamul üzerinde doğrudan çalışan işçilere, 50.000 ₺'si fabrika ustabaşılarına, 40.000 ₺'si satış personeline ve 30.000 ₺'si genel yönetim personeline aittir. İşletme 7/A seçeneğini kullanmaktadır.\n\nÜcret tahakkukunda borçlandırılacak hesaplar hangisidir?",
        {
            'A': '791 hesabı 370.000 ₺',
            'B': '720 hesabı 250.000 ₺; 730 hesabı 50.000 ₺; 760 hesabı 40.000 ₺; 770 hesabı 30.000 ₺',
            'C': '720 hesabı 300.000 ₺; 760 hesabı 40.000 ₺; 770 hesabı 30.000 ₺',
            'D': '720 hesabı 250.000 ₺; 730 hesabı 120.000 ₺',
            'E': '730 hesabı 300.000 ₺; 760 hesabı 40.000 ₺; 770 hesabı 30.000 ₺',
        },
        'B',
        'Doğrudan üretim işçiliği **720**, ustabaşı gibi endirekt üretim işçiliği **730**, satış personeli **760** ve genel yönetim personeli **770** hesapta izlenir. 791 hesabı 7/B seçeneğine aittir.',
        "1 Sıra No'lu MSUGT - 720/730/760/770",
    ),
    # düzey 2
    '0006': patch(
        "7/B seçeneğini uygulayan bir üretim işletmesinin dönem sonunda gider çeşitleri hesaplarındaki tutarlar ve dağılımları şöyledir: 790 İlk Madde ve Malzeme Giderleri 400.000 ₺ (tamamı üretim), 791 İşçi Ücret ve Giderleri 300.000 ₺ (tamamı üretim), 792 Memur Ücret ve Giderleri 120.000 ₺ (80.000 ₺ yönetim, 40.000 ₺ satış), 793 Dışarıdan Sağlanan Fayda ve Hizmetler 100.000 ₺ (60.000 ₺ üretim, 40.000 ₺ yönetim), 796 Amortisman ve Tükenme Payları 80.000 ₺ (50.000 ₺ üretim, 30.000 ₺ yönetim), 797 Finansman Giderleri 30.000 ₺.\n\nBuna göre dönem sonunda '799 Üretim Maliyet Hesabı'na aktarılacak tutar kaç ₺'dir?",
        {
            'A': '1.030.000',
            'B': '700.000',
            'C': '810.000',
            'D': '730.000',
            'E': '760.000',
        },
        'C',
        "7/B'de gider çeşitleri dönem sonunda 798 Gider Çeşitleri Yansıtma hesabı aracılığıyla dağıtılır: üretime ait kısım 799 Üretim Maliyet Hesabı'na, yönetim ve satış payları 632 ve 631'e, finansman giderleri 66 grubuna aktarılır. Üretim payı = 400.000 + 300.000 + 60.000 + 50.000 = 810.000 ₺.",
        "1 Sıra No'lu MSUGT - 780/781 → 660/661",
    ),
    # düzey 2
    '0007': patch(
        "Satılan mamullerin üretim maliyeti gelir tablosunda Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '620 Satılan Mamuller Maliyeti (-)',
            'B': '152 Mamuller',
            'C': '730 Genel Üretim Giderleri',
            'D': '600 Yurt İçi Satışlar',
            'E': '621 Satılan Ticari Mallar Maliyeti (-)',
        },
        'A',
        "Satılan mamullerin üretim maliyeti **620 Satılan Mamuller Maliyeti (-)** hesabında izlenir (üretim işletmesi). Ticaret işletmesinde ise satılan ticari malların maliyeti 621'de izlenir.",
        "1 Sıra No'lu MSUGT - 620",
    ),
    # düzey 3
    '0008': patch(
        "Standart maliyet yöntemini uygulayan işletmede 711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma Hesabı 500.000 ₺'dir. Dönemde 20.000 ₺ olumlu fiyat farkı ve 35.000 ₺ olumsuz miktar farkı oluşmuştur.\n\n710 Direkt İlk Madde ve Malzeme Giderleri hesabının fiilî tutarı kaç ₺'dir?",
        {
            'A': '475.000',
            'B': '500.000',
            'C': '515.000',
            'D': '485.000',
            'E': '495.000',
        },
        'C',
        "Fiilî maliyet = standart maliyet − olumlu fark + olumsuz fark olarak bulunur. 500.000 − 20.000 + 35.000 = **515.000 ₺**'dir. Olumlu fiyat farkı maliyeti azaltırken olumsuz miktar farkı artırır.",
        "1 Sıra No'lu MSUGT - 710/711/712/713; 2024-2026 SGS standart maliyet kapanışı soru örüntüsü",
    ),
    # düzey 2
    '0009': patch(
        "Normal kapasitesi 20.000 birim olan işletmenin sabit genel üretim giderleri 400.000 ₺'dir. Dönemde olağan nedenlerle 15.000 birim üretilmiştir.\n\nTMS 2'ye göre sabit genel üretim giderinin stok maliyetine yüklenecek ve dönem gideri yazılacak kısımları sırasıyla kaç ₺'dir?",
        {
            'A': '400.000 ve 0',
            'B': '200.000 ve 200.000',
            'C': '100.000 ve 300.000',
            'D': '300.000 ve 75.000',
            'E': '300.000 ve 100.000',
        },
        'E',
        'Normal kapasiteye göre sabit GÜG oranı 400.000 / 20.000 = 20 ₺/birimdir. 15.000 birime **300.000 ₺** yüklenebilir; kalan **100.000 ₺** düşük kapasite nedeniyle stok maliyetine eklenmez ve oluştuğu dönemde giderleştirilir.',
        'TMS 2 Stoklar, par. 13 - normal kapasite ve dağıtılmayan sabit genel üretim gideri',
    ),
    # düzey 3
    '0010': patch(
        "7/B seçeneğinde 790-797 gider çeşidi hesaplarında toplam 800.000 ₺ gider birikmiştir. Yapılan gider yeri dağıtımında bu tutarın 600.000 ₺'sinin üretime, 120.000 ₺'sinin pazarlamaya ve 80.000 ₺'sinin genel yönetime ait olduğu belirlenmiştir.\n\nYansıtma kaydında 799 Üretim Maliyet Hesabına borç kaydedilecek tutar kaç ₺'dir?",
        {
            'A': '680.000',
            'B': '800.000',
            'C': '80.000',
            'D': '600.000',
            'E': '120.000',
        },
        'D',
        '799 hesap yalnız **üretim fonksiyonuna ait 600.000 ₺** için borçlandırılır. Pazarlama ve genel yönetim payları ilgili gelir tablosu fonksiyon hesaplarına aktarılır; gider çeşitlerinin toplamı ise 798 hesap aracılığıyla yansıtılır.',
        "1 Sıra No'lu MSUGT - 7/B gider çeşitlerinin fonksiyonlara dağıtımı",
    ),
    # düzey 3
    '0011': patch(
        "Bir üretim işletmesinin dönem başı yarı mamul maliyeti 80.000 ₺, dönemin üretim giderleri 520.000 ₺ ve dönem sonu yarı mamul maliyeti 100.000 ₺'dir. Dönemde 2.000 birim mamul tamamlanmıştır.\n\nTamamlanan mamullerin birim maliyeti kaç ₺'dir?",
        {
            'A': '100',
            'B': '200',
            'C': '250',
            'D': '240',
            'E': '220',
        },
        'C',
        "Tamamlanan mamul maliyeti = 80.000 + 520.000 − 100.000 = **500.000 ₺**'dir. 2.000 birim tamamlandığına göre birim maliyet 500.000 / 2.000 = **250 ₺** olur.",
        "1 Sıra No'lu MSUGT - 151/152 ve Satışların Maliyeti Tablosu",
    ),
    # düzey 2
    '0012': patch(
        "Fabrika personeline ait 350.000 ₺ brüt ücretin %80'i mamullere doğrudan izlenebilmekte, %20'si bakım ve ustabaşı işçiliğinden oluşmaktadır.\n\n7/A seçeneğinde 720 Direkt İşçilik Giderleri ile 730 Genel Üretim Giderleri hesaplarına borç yazılacak tutarlar sırasıyla kaç ₺'dir?",
        {
            'A': '350.000 ve 0',
            'B': '280.000 ve 70.000',
            'C': '210.000 ve 140.000',
            'D': '300.000 ve 50.000',
            'E': '70.000 ve 280.000',
        },
        'B',
        'Doğrudan izlenebilen işçilik 350.000 × %80 = **280.000 ₺** olup 720 hesaba yazılır. Bakım ve ustabaşı işçiliği endirekttir; 350.000 × %20 = **70.000 ₺** 730 hesaba kaydedilir.',
        "1 Sıra No'lu MSUGT - 720/730",
    ),
    # düzey 2
    '0013': patch(
        "Bir üretim işletmesinde direkt ilk madde ve malzeme giderleri 240.000 ₺, direkt işçilik giderleri 150.000 ₺ ve genel üretim giderleri 110.000 ₺'dir.\n\nDirekt (temel) maliyet ile şekillendirme (dönüştürme) maliyeti sırasıyla kaç ₺'dir?",
        {
            'A': '350.000 ve 390.000',
            'B': '390.000 ve 500.000',
            'C': '240.000 ve 500.000',
            'D': '500.000 ve 260.000',
            'E': '390.000 ve 260.000',
        },
        'E',
        "Direkt maliyet = direkt ilk madde ve malzeme + direkt işçilik = 240.000 + 150.000 = **390.000 ₺**'dir. Şekillendirme maliyeti = direkt işçilik + genel üretim giderleri = 150.000 + 110.000 = **260.000 ₺** olur.",
        'Maliyet muhasebesi - direkt maliyet ve şekillendirme maliyeti',
    ),
    # düzey 3
    '0014': patch(
        "Normal maliyet yöntemini kullanan işletme dönemde 25.000 birim üretmiştir. Direkt ilk madde ve malzeme giderleri 400.000 ₺, direkt işçilik giderleri 250.000 ₺, değişken genel üretim giderleri 150.000 ₺ ve sabit genel üretim giderleri 300.000 ₺'dir. Dönemin kapasite kullanım oranı %80'dir.\n\nNormal maliyete göre birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '41,60',
            'B': '46,40',
            'C': '51,20',
            'D': '44,80',
            'E': '44,00',
        },
        'A',
        "Sabit GÜG'nin maliyete yüklenecek kısmı 300.000 × %80 = 240.000 ₺'dir. Toplam normal maliyet 400.000 + 250.000 + 150.000 + 240.000 = 1.040.000 ₺; birim maliyet 1.040.000 / 25.000 = **41,60 ₺**'dir.",
        'TMS 2 Stoklar, par. 12-13; 18 Temmuz 2026 SGS normal maliyet ve kapasite soru örüntüsü',
    ),
    # düzey 2
    '0015': patch(
        'Dönem sonunda üretim makineleri için 40.000 ₺, genel yönetimde kullanılan demirbaşlar için 10.000 ₺ amortisman hesaplanmıştır. İşletme 7/A seçeneğini kullanmaktadır.\n\nAmortisman kaydında borçlandırılacak maliyet hesapları hangisidir?',
        {
            'A': '720 Direkt İşçilik Giderleri 40.000 ₺ ve 760 Pazarlama, Satış ve Dağıtım Giderleri 10.000 ₺',
            'B': '730 Genel Üretim Giderleri 40.000 ₺ ve 770 Genel Yönetim Giderleri 10.000 ₺',
            'C': '796 Amortisman ve Tükenme Payları 50.000 ₺',
            'D': '730 Genel Üretim Giderleri 50.000 ₺',
            'E': '770 Genel Yönetim Giderleri 50.000 ₺',
        },
        'B',
        'Üretim makinelerinin amortismanı üretimle ilgili endirekt giderdir ve **730 hesaba 40.000 ₺** yazılır. Genel yönetim demirbaşı amortismanı ise **770 hesaba 10.000 ₺** kaydedilir. 796 hesabı 7/B seçeneğinde kullanılır.',
        "1 Sıra No'lu MSUGT - 730/770/257",
    ),
    # düzey 3
    '0016': patch(
        "7/B seçeneğinde gider çeşidi hesaplarında 790 İlk Madde ve Malzeme Giderleri 180.000 ₺, 791 İşçi Ücret ve Giderleri 120.000 ₺ ve 793 Dışarıdan Sağlanan Fayda ve Hizmetler 40.000 ₺ birikmiştir. Yapılan dağıtımda toplamın 300.000 ₺'si üretime, 40.000 ₺'si genel yönetime aittir.\n\nYansıtma kaydı hangisidir?",
        {
            'A': '799 Üretim Maliyet Hesabı 340.000 ₺ borç / 798 Gider Çeşitleri Yansıtma 340.000 ₺ alacak',
            'B': '151 Yarı Mamuller - Üretim 300.000 ₺ ve 770 Genel Yönetim Giderleri 40.000 ₺ borç / 790, 791 ve 793 hesapları 340.000 ₺ alacak',
            'C': '798 Gider Çeşitleri Yansıtma 340.000 ₺ borç / 799 Üretim Maliyet Hesabı 300.000 ₺ ve 632 Genel Yönetim Giderleri 40.000 ₺ alacak',
            'D': '799 Üretim Maliyet Hesabı 300.000 ₺ ve 632 Genel Yönetim Giderleri 40.000 ₺ borç / 798 Gider Çeşitleri Yansıtma 340.000 ₺ alacak',
            'E': '710, 720 ve 730 hesapları toplam 300.000 ₺ ve 770 hesap 40.000 ₺ borç / 798 hesap 340.000 ₺ alacak',
        },
        'D',
        "7/B'de gider çeşitleri 798 hesap aracılığıyla fonksiyonlara yansıtılır. Üretim payı **799 hesaba 300.000 ₺**, genel yönetim payı **632 hesaba 40.000 ₺ borç**; toplam **340.000 ₺ 798 hesaba alacak** kaydedilir.",
        "1 Sıra No'lu MSUGT - 7/B, 790-799 ve 632",
    ),
    # düzey 2
    '0017': patch(
        "Dönemde üretimi tamamlanan mamullerin maliyeti 420.000 ₺, bunlardan satılanların maliyeti 300.000 ₺'dir.\n\nTamamlanma ve satış maliyeti kayıtları hangisidir?",
        {
            'A': '152 Mamuller 120.000 ₺ borç ve 620 Satılan Mamuller Maliyeti 300.000 ₺ borç / 151 Yarı Mamuller - Üretim 420.000 ₺ alacak',
            'B': '152 Mamuller 420.000 ₺ borç / 620 Satılan Mamuller Maliyeti 420.000 ₺ alacak; satışta ayrı maliyet kaydı yapılmaz',
            'C': '151 Yarı Mamuller - Üretim 420.000 ₺ borç / 152 Mamuller 420.000 ₺ alacak; 152 Mamuller 300.000 ₺ borç / 620 Satılan Mamuller Maliyeti 300.000 ₺ alacak',
            'D': '620 Satılan Mamuller Maliyeti 420.000 ₺ borç / 151 Yarı Mamuller - Üretim 420.000 ₺ alacak; 152 Mamuller 300.000 ₺ borç / 620 Satılan Mamuller Maliyeti 300.000 ₺ alacak',
            'E': '152 Mamuller 420.000 ₺ borç / 151 Yarı Mamuller - Üretim 420.000 ₺ alacak; 620 Satılan Mamuller Maliyeti 300.000 ₺ borç / 152 Mamuller 300.000 ₺ alacak',
        },
        'E',
        'Tamamlanan üretim **152 borç / 151 alacak 420.000 ₺** kaydıyla mamul stoklarına alınır. Satılan kısmın maliyeti ise **620 borç / 152 alacak 300.000 ₺** kaydıyla gelir tablosuna aktarılır.',
        "1 Sıra No'lu MSUGT - 151/152/620",
    ),
    # düzey 3
    '0018': patch(
        "Bir üretim işletmesinde dönem içinde tamamlanıp 152 Mamuller hesabına alınan üretim maliyeti 500.000 ₺'dir. Dönem başı mamul stoku 60.000 ₺, dönem sonu sayımla belirlenen mamul stoku 90.000 ₺'dir. Buna göre 620 Satılan Mamuller Maliyeti kaç ₺'dir?",
        {
            'A': '470.000 ₺',
            'B': '530.000 ₺',
            'C': '560.000 ₺',
            'D': '410.000 ₺',
            'E': '500.000 ₺',
        },
        'A',
        'Satılan mamuller maliyeti = dönem başı mamul + tamamlanan üretim − dönem sonu mamul = 60.000 + 500.000 − 90.000 = **470.000 ₺**.',
        'THP 152, 620',
    ),
    # düzey 3
    '0019': patch(
        "7/A seçeneğini uygulayan bir üretim işletmesinde dönemde tahakkuk eden brüt ücretlerin 300.000 ₺'si mamul üzerinde doğrudan çalışan işçilere, 80.000 ₺'si ustabaşı ve bakım personeline, 70.000 ₺'si satış personeline, 50.000 ₺'si yönetim personeline aittir. Buna göre ücret tahakkuk kaydında aşağıdakilerden hangisi yer almaz?",
        {
            'A': '770 Genel Yönetim Giderleri hesabı 50.000 ₺ borçlandırılır',
            'B': '730 Genel Üretim Giderleri hesabı 80.000 ₺ borçlandırılır',
            'C': '720 Direkt İşçilik Giderleri hesabı 380.000 ₺ borçlandırılır',
            'D': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 70.000 ₺ borçlandırılır',
            'E': '720 Direkt İşçilik Giderleri hesabı 300.000 ₺ borçlandırılır',
        },
        'C',
        "Direkt işçilik yalnız mamule doğrudan izlenebilen 300.000 ₺'dir; ustabaşı ve bakım personelinin ücreti endirekt işçiliktir ve 730'a yazılır. Satış ve yönetim personeli ücretleri dönem gideridir (760, 770).",
        'THP 720, 730, 760, 770',
    ),
    # düzey 2
    '0020': patch(
        'Bir üretim işletmesinin dönem giderleri sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi üretim maliyetine girmez?',
        {
            'A': 'Genel yönetim bölümündeki personelin ücreti',
            'B': 'Mamul üzerinde çalışan işçinin ücreti',
            'C': 'Üretimde kullanılan yardımcı malzeme',
            'D': 'Fabrika binasının amortismanı',
            'E': 'Ustabaşının ücreti',
        },
        'A',
        'Üretim maliyeti direkt ilk madde, direkt işçilik ve genel üretim giderlerinden oluşur. **Genel yönetim** personelinin ücreti dönem gideridir (770).',
        'THP 7/A; üretim maliyeti',
    ),
    # düzey 2
    '0021': patch(
        'Direkt gider ile endirekt gider ayrımıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Direkt ilk madde ve malzeme bir direkt giderdir',
            'B': 'Direkt işçilik mamule doğrudan yüklenebilir',
            'C': 'Endirekt giderler mamullere dağıtım anahtarlarıyla yüklenir',
            'D': 'İşletme malzemesi genellikle endirekt gider sayılır',
            'E': 'Direkt giderler mamullere dağıtım anahtarıyla yüklenir',
        },
        'E',
        'Direkt giderler (direkt ilk madde ve malzeme, direkt işçilik) mamule doğrudan yüklenebilir; endirekt giderler (işletme malzemesi, endirekt işçilik vb.) ise ancak dağıtım anahtarlarıyla mamullere yüklenir. Dağıtım anahtarı endirekt giderler için kullanılır.',
        "1 Sıra No'lu MSUGT - 710/720/730",
    ),
    # düzey 3
    '0022': patch(
        "Normal maliyet yöntemini kullanan işletmede direkt ilk madde ve malzeme giderleri 360.000 ₺, direkt işçilik giderleri 240.000 ₺, değişken genel üretim giderleri 180.000 ₺ ve sabit genel üretim giderleri 300.000 ₺'dir. Normal kapasite 10.000 birim, fiilî üretim 8.000 birimdir.\n\nStok maliyetine yüklenecek toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '840.000',
            'B': '1.020.000',
            'C': '960.000',
            'D': '780.000',
            'E': '1.080.000',
        },
        'B',
        "Direkt giderler ile değişken GÜG'nin tamamı maliyete girer. Sabit GÜG'nin yüklenecek kısmı 300.000 × 8.000/10.000 = 240.000 ₺'dir. Toplam maliyet 360.000 + 240.000 + 180.000 + 240.000 = **1.020.000 ₺**; dağıtılmayan 60.000 ₺ dönem gideridir.",
        'TMS 2 Stoklar, par. 12-13; normal kapasiteye göre sabit genel üretim gideri',
    ),
    # düzey 2
    '0023': patch(
        'İşletmenin finansman fonksiyonuyla ilgili giderleri, 7/A seçeneğinde önce hangi maliyet hesabında izlenir?',
        {
            'A': '710 Direkt İlk Madde ve Malzeme Giderleri',
            'B': '730 Genel Üretim Giderleri',
            'C': '660 Kısa Vadeli Borçlanma Giderleri (-)',
            'D': '780 Finansman Giderleri',
            'E': '770 Genel Yönetim Giderleri',
        },
        'D',
        "7/A'da finansman giderleri önce **780 Finansman Giderleri** maliyet hesabında izlenir; dönem sonunda 781 yansıtma ile gelir tablosundaki 66 grubuna (660/661) aktarılır.",
        "1 Sıra No'lu MSUGT - 780 / 660",
    ),
    # düzey 2
    '0024': patch(
        "Aşağıdaki hesaplardan hangisi '7 Maliyet Hesapları' grubunda yer almaz?",
        {
            'A': '760 Pazarlama, Satış ve Dağıtım Giderleri',
            'B': '150 İlk Madde ve Malzeme',
            'C': '770 Genel Yönetim Giderleri',
            'D': '730 Genel Üretim Giderleri',
            'E': '710 Direkt İlk Madde ve Malzeme Giderleri',
        },
        'B',
        '**150 İlk Madde ve Malzeme** bir stok (bilanço) hesabıdır, maliyet hesabı değildir. Diğerleri (710, 730, 770, 760) 7 Maliyet Hesapları grubundadır.',
        "1 Sıra No'lu MSUGT - 7 grubu vs 15 stoklar",
    ),
    # düzey 3
    '0025': patch(
        '7/A seçeneğini kullanan işletmede dönemin üretim giderleri 710 hesapta 150.000 ₺, 720 hesapta 100.000 ₺ ve 730 hesapta 80.000 ₺ olarak birikmiştir. Giderlerin tamamı yarı mamul maliyetine yansıtılacaktır.\n\n151 Yarı Mamuller - Üretim hesabının borçlandırıldığı yansıtma kaydında hangi hesaplar alacaklandırılır?',
        {
            'A': '710 hesabı 150.000 ₺, 720 hesabı 100.000 ₺ ve 730 hesabı 80.000 ₺',
            'B': '620 hesabı 150.000 ₺, 621 hesabı 100.000 ₺ ve 622 hesabı 80.000 ₺',
            'C': '711 hesabı 330.000 ₺; 721 ve 731 hesapları kullanılmaz',
            'D': '150 hesabı 150.000 ₺, 335 hesabı 100.000 ₺ ve 381 hesabı 80.000 ₺',
            'E': '711 hesabı 150.000 ₺, 721 hesabı 100.000 ₺ ve 731 hesabı 80.000 ₺',
        },
        'E',
        "7/A'da giderler önce fonksiyon hesaplarında toplanır, üretim maliyetine ise ilgili **yansıtma hesapları** aracılığıyla aktarılır. Bu nedenle 151 hesap 330.000 ₺ borçlandırılır; 711, 721 ve 731 hesapları sırasıyla 150.000, 100.000 ve 80.000 ₺ alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 151/711/721/731",
    ),
    # düzey 2
    '0026': patch(
        "7/A seçeneğini uygulayan bir üretim işletmesinde dönem sonunda gider hesaplarının borç kalanları şöyledir: 710 Direkt İlk Madde ve Malzeme Giderleri 360.000 ₺, 720 Direkt İşçilik Giderleri 210.000 ₺, 730 Genel Üretim Giderleri 150.000 ₺, 760 Pazarlama Satış ve Dağıtım Giderleri 45.000 ₺, 770 Genel Yönetim Giderleri 65.000 ₺, 780 Finansman Giderleri 35.000 ₺. Dönem başında yarı mamul ve mamul stoku yoktur; dönemde başlanan üretimin tamamı tamamlanmış ve tamamlanan mamullerin %80'i satılmıştır.\n\nBuna göre yansıtma ve aktarma kayıtlarından sonra '620 Satılan Mamuller Maliyeti' hesabının kalanı kaç ₺'dir?",
        {
            'A': '576.000',
            'B': '720.000',
            'C': '456.000',
            'D': '624.000',
            'E': '672.000',
        },
        'A',
        "Üretim maliyeti yalnız 710, 720 ve 730'dan oluşur: 360.000 + 210.000 + 150.000 = 720.000 ₺ (151'e yansıtılır, tamamlanınca 152'ye aktarılır). Satılan %80: 720.000 × 0,80 = 576.000 ₺ (620 borç / 152 alacak). 760, 770 ve 780 dönem gideridir; 631, 632 ve 66 grubuna yansıtılır.",
        "1 Sıra No'lu MSUGT - 770/771 → 632",
    ),
    # düzey 2
    '0027': patch(
        '7/A seçeneğindeki yansıtma hesaplarının (711, 721, 731 …) niteliği ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşletmenin satıcılara ve kredi kurumlarına olan yükümlülüklerini gösteren bir borç (kaynak) hesabıdır.',
            'B': 'İşletmeye konulan sermaye ile yedekleri kalıcı olarak izleyen bir özkaynak hesabıdır.',
            'C': 'İlgili gider hesabını dönem sonunda kapatmak/aktarmak için kullanılan, gider hesabının karşı yönünde (alacak) çalışan hesaplardır.',
            'D': 'Dönem içinde elde edilen satış gelirlerini biriktiren ve dönem sonunda kâra aktarılan bir gelir hesabıdır.',
            'E': 'Dönem sonunda üretilen mamullerin ve yarı mamullerin üretim maliyetini stoklarda izleyen, aktife dâhil bir varlık hesabıdır.',
        },
        'C',
        'Yansıtma hesapları, ilgili gider hesabını dönem sonunda **kapatmak/aktarmak** için kullanılır; gider hesabı borç çalışırken yansıtma hesabı **alacak** çalışarak aktarımı sağlar ve sonunda gider hesabıyla karşılıklı kapatılır.',
        "1 Sıra No'lu MSUGT - yansıtma hesapları",
    ),
    # düzey 3
    '0028': patch(
        "Bir üretim işletmesinde fabrika müdürü ücreti 70.000 ₺, bakım işçiliği 30.000 ₺, üretim makinelerinin amortismanı 40.000 ₺, fabrika elektrik gideri 25.000 ₺ ve pazarlama bölümü kirası 35.000 ₺'dir.\n\nGenel üretim giderleri toplamı kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '200.000',
            'C': '165.000',
            'D': '150.000',
            'E': '130.000',
        },
        'C',
        "Fabrika müdürü, bakım işçiliği, üretim makinesi amortismanı ve fabrika elektriği GÜG'dür: 70.000 + 30.000 + 40.000 + 25.000 = **165.000 ₺**. Pazarlama bölümü kirası 760 hesapta dönem gideridir.",
        "1 Sıra No'lu MSUGT - 730/760",
    ),
    # düzey 2
    '0029': patch(
        "7/B seçeneğinde gider çeşidi hesaplarında biriken giderlerin 300.000 ₺'lık kısmı üretim faaliyetine aittir. Bu tutar üretim maliyetine yansıtılacaktır.\n\nYansıtma kaydında kullanılacak hesaplar hangisidir?",
        {
            'A': '799 Üretim Maliyet Hesabı borç / 790 İlk Madde ve Malzeme Giderleri alacak',
            'B': '151 Yarı Mamuller - Üretim borç / 790 İlk Madde ve Malzeme Giderleri alacak',
            'C': '798 Gider Çeşitleri Yansıtma borç / 799 Üretim Maliyet Hesabı alacak',
            'D': '799 Üretim Maliyet Hesabı borç / 798 Gider Çeşitleri Yansıtma Hesabı alacak',
            'E': '710 Direkt İlk Madde ve Malzeme Giderleri borç / 711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma alacak',
        },
        'D',
        "7/B'de giderler 790-797 gider çeşidi hesaplarında izlenir. Üretimle ilgili kısım **799 Üretim Maliyet Hesabına borç**, gider çeşitlerinin yansıtılması ise **798 hesaba alacak** kaydedilir.",
        "1 Sıra No'lu MSUGT - 7/B seçeneği, 798/799",
    ),
    # düzey 2
    '0030': patch(
        '7/B seçeneğinde giderlerin çeşit esasına göre izlendiği hesaplardan biri aşağıdakilerden hangisidir?',
        {
            'A': '320 Satıcılar',
            'B': '151 Yarı Mamuller - Üretim',
            'C': '600 Yurt İçi Satışlar',
            'D': '710 Direkt İlk Madde ve Malzeme Giderleri',
            'E': '790 İlk Madde ve Malzeme Giderleri',
        },
        'E',
        "7/B'de gider çeşitleri **790 İlk Madde ve Malzeme Giderleri, 791 İşçi Ücret ve Giderleri, 793 Dışarıdan Sağlanan Fayda ve Hizmetler, 796 Amortismanlar** gibi 790-797 hesaplarında izlenir. (710 ise 7/A hesabıdır.)",
        "1 Sıra No'lu MSUGT - 790-797",
    ),
    # düzey 3
    '0031': patch(
        "Normal maliyet yöntemini kullanan bir işletmenin direkt ilk madde ve malzeme giderleri 500.000 ₺, direkt işçilik giderleri 300.000 ₺ ve sabit genel üretim giderleri 200.000 ₺'dir. Normal kapasite 10.000 birim, fiilî üretim 8.000 birimdir. Dönem başı ve sonu yarı mamulü bulunmayan işletmenin normal maliyete göre toplam üretim maliyeti 1.140.000 ₺'dir.\n\nDeğişken genel üretim giderleri kaç ₺'dir?",
        {
            'A': '180.000',
            'B': '100.000',
            'C': '140.000',
            'D': '160.000',
            'E': '200.000',
        },
        'A',
        "Maliyete yüklenen sabit GÜG 200.000 × 8.000/10.000 = 160.000 ₺'dir. Değişken GÜG = 1.140.000 − 500.000 − 300.000 − 160.000 = **180.000 ₺** bulunur.",
        'TMS 2 Stoklar, par. 12-13; 2025-2026 SGS normal maliyet ters hesaplama soru örüntüsü',
    ),
    # düzey 2
    '0032': patch(
        "Üretime verilen 300.000 ₺ tutarındaki ilk madde ve malzemenin %75'i mamule doğrudan yüklenebilmekte, kalanı endirekt nitelik taşımaktadır. İşletme 7/A seçeneğini kullanmaktadır.\n\nKayıtta 710 ve 730 hesaplarına borç yazılacak tutarlar sırasıyla kaç ₺'dir?",
        {
            'A': '240.000 ve 60.000',
            'B': '75.000 ve 225.000',
            'C': '150.000 ve 150.000',
            'D': '225.000 ve 75.000',
            'E': '300.000 ve 0',
        },
        'D',
        'Direkt kısım 300.000 × %75 = **225.000 ₺** olup 710 hesaba; kalan **75.000 ₺** endirekt malzeme ise 730 hesaba borç kaydedilir. Toplam 300.000 ₺ için 150 hesap alacaklandırılır.',
        "1 Sıra No'lu MSUGT - 150/710/730; 18 Temmuz 2026 SGS direkt-endirekt ayrımı soru örüntüsü",
    ),
    # düzey 2
    '0033': patch(
        '7/A ve 7/B seçenekleri arasındaki temel fark ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '7/A giderleri çeşit esasına göre (790-799 hesaplarında yansıtmasız) izler; 7/B ise giderleri fonksiyon esasına göre yansıtmalı olarak izler.',
            'B': '7/A giderleri fonksiyon esasına göre (yansıtmalı) izler; 7/B giderleri çeşit esasına göre (790-799) izler. İşletme ikisinden birini seçer.',
            'C': '7/A bir bilanço hesap grubu, 7/B ise bir gelir tablosu hesap grubudur; ikisi farklı finansal tablolarda yer alır.',
            'D': '7/A ile 7/B arasında hiçbir fark yoktur; ikisi de aynı hesapları içerir ve işletme her ikisini birlikte kullanır.',
            'E': '7/A dönemin satışlarını, 7/B ise dönem içindeki alış ve stok hareketlerini izlemek için kullanılır.',
        },
        'B',
        '**7/A** giderleri **fonksiyon esasına** göre (yansıtma hesaplarıyla), **7/B** ise **çeşit esasına** göre (790-799) izler. İşletme, ölçeğine göre bu iki seçenekten birini kullanır.',
        "1 Sıra No'lu MSUGT - 7/A ve 7/B",
    ),
    # düzey 2
    '0034': patch(
        "Normal kapasitesi 10.000 birim olan işletmede sabit genel üretim gideri 250.000 ₺'dir. Dönemde 7.000 birim üretilmiştir.\n\nTam maliyet yöntemiyle normal maliyet yöntemine göre hesaplanan toplam üretim maliyetleri arasındaki fark kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '50.000',
            'C': '100.000',
            'D': '175.000',
            'E': '75.000',
        },
        'E',
        "Tam maliyet sabit GÜG'nin tamamı olan 250.000 ₺'yı ürüne yükler. Normal maliyette yüklenen sabit GÜG 250.000 × 7.000/10.000 = 175.000 ₺'dir. Aradaki **75.000 ₺** dağıtılmayan sabit giderdir.",
        'TMS 2 Stoklar, par. 13; 26 Ekim 2024 SGS tam-normal maliyet farkı soru örüntüsü',
    ),
    # düzey 3
    '0035': patch(
        "Bir üretim işletmesinin dönemin üretim giderleri 780.000 ₺, dönem başı ve sonu yarı mamul stokları sırasıyla 90.000 ve 70.000 ₺, dönem başı ve sonu mamul stokları ise sırasıyla 60.000 ve 110.000 ₺'dir.\n\nTamamlanan mamul maliyeti ile satılan mamuller maliyeti sırasıyla kaç ₺'dir?",
        {
            'A': '820.000 ve 770.000',
            'B': '800.000 ve 750.000',
            'C': '800.000 ve 850.000',
            'D': '780.000 ve 730.000',
            'E': '760.000 ve 810.000',
        },
        'B',
        "Tamamlanan mamul maliyeti = 90.000 + 780.000 − 70.000 = **800.000 ₺**'dir. Satılan mamuller maliyeti = 60.000 + 800.000 − 110.000 = **750.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Satışların Maliyeti Tablosu; 18 Nisan 2026 SGS iki dönemli tablo soru örüntüsü",
    ),
    # düzey 2
    '0036': patch(
        '7/A seçeneğini kullanan bir hizmet işletmesinde 740 Hizmet Üretim Maliyeti hesabında dönem boyunca 240.000 ₺ gider birikmiş ve hizmetlerin tamamı müşterilere sunulmuştur.\n\nHizmet maliyetinin gelir tablosuna yansıtılmasında yapılacak kayıt hangisidir?',
        {
            'A': '622 Satılan Hizmet Maliyeti 240.000 ₺ borç / 741 Hizmet Üretim Maliyeti Yansıtma 240.000 ₺ alacak',
            'B': '151 Yarı Mamuller - Üretim borç / 741 Hizmet Üretim Maliyeti Yansıtma alacak',
            'C': '741 Hizmet Üretim Maliyeti Yansıtma borç / 622 Satılan Hizmet Maliyeti alacak',
            'D': '740 Hizmet Üretim Maliyeti borç / 622 Satılan Hizmet Maliyeti alacak',
            'E': '621 Satılan Ticari Mallar Maliyeti 240.000 ₺ borç / 740 Hizmet Üretim Maliyeti 240.000 ₺ alacak',
        },
        'A',
        'Sunulmuş hizmetlerin maliyeti gelir tablosunda **622 Satılan Hizmet Maliyeti** hesabına borç, **741 Hizmet Üretim Maliyeti Yansıtma** hesabına alacak kaydedilir. Ayrı kapanış kaydında 741 borçlandırılıp 740 alacaklandırılır.',
        "1 Sıra No'lu MSUGT - 740/741/622",
    ),
    # düzey 3
    '0037': patch(
        "Bir üretim işletmesinde dönem başı ilk madde ve malzeme stoku 40.000 ₺, dönem içi alışlar 260.000 ₺ ve dönem sonu stok 50.000 ₺'dir. Kullanılan malzemenin tamamı direkt niteliktedir. Direkt işçilik 150.000 ₺, genel üretim giderleri 100.000 ₺, dönem başı ve sonu yarı mamul stokları 30.000 ve 20.000 ₺, dönem başı ve sonu mamul stokları ise 60.000 ve 70.000 ₺'dir.\n\nSatılan mamuller maliyeti kaç ₺'dir?",
        {
            'A': '480.000',
            'B': '490.000',
            'C': '500.000',
            'D': '510.000',
            'E': '470.000',
        },
        'C',
        "Kullanılan direkt malzeme 40.000 + 260.000 − 50.000 = 250.000 ₺; üretim giderleri 250.000 + 150.000 + 100.000 = 500.000 ₺'dir. Tamamlanan mamul maliyeti 30.000 + 500.000 − 20.000 = 510.000 ₺; satılan mamuller maliyeti 60.000 + 510.000 − 70.000 = **500.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Satışların Maliyeti Tablosu",
    ),
    # düzey 3
    '0038': patch(
        "7/A seçeneğini uygulayan bir üretim işletmesinde dönem içinde 710 hesabında 300.000 ₺, 720 hesabında 200.000 ₺ ve 730 hesabında 150.000 ₺ gider toplanmıştır. Dönem başı yarı mamul stoku 50.000 ₺, dönem sonu yarı mamul stoku 80.000 ₺'dir. Buna göre dönemde tamamlanarak 152 Mamuller hesabına aktarılan üretim maliyeti kaç ₺'dir?",
        {
            'A': '680.000 ₺',
            'B': '650.000 ₺',
            'C': '620.000 ₺',
            'D': '570.000 ₺',
            'E': '700.000 ₺',
        },
        'C',
        "Üretim giderleri yansıtma hesaplarıyla 151'e aktarılır: 650.000 ₺. Tamamlanan üretim = dönem başı yarı mamul + dönem giderleri − dönem sonu yarı mamul = 50.000 + 650.000 − 80.000 = **620.000 ₺** (152 borç / 151 alacak).",
        'THP 710-731, 151, 152',
    ),
    # düzey 3
    '0039': patch(
        '7/A seçeneğini uygulayan işletmede dönem sonunda üretim makineleri için 60.000 ₺, satış bölümünün taşıtları için 20.000 ₺ ve yönetim binası için 30.000 ₺ amortisman hesaplanmıştır. Buna göre amortisman kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '257 Birikmiş Amortismanlar hesabı 110.000 ₺ borçlandırılır',
            'B': '730 Genel Üretim Giderleri hesabı 20.000 ₺ borçlandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı 20.000 ₺ borçlandırılır',
            'D': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 20.000 ₺ borçlandırılır',
            'E': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 110.000 ₺ borçlandırılır',
        },
        'D',
        'Kayıt: 730 (borç) 60.000 + **760 (borç) 20.000** + 770 (borç) 30.000 / 257 (alacak) 110.000. Amortisman varlığın kullanıldığı fonksiyona göre gider hesaplarına dağıtılır.',
        'THP 730, 760, 770, 257',
    ),
    # düzey 2
    '0040': patch(
        'Maliyet hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 7/A seçeneğinde giderler fonksiyon esasına göre izlenir.\n\nII. 760 Pazarlama Satış ve Dağıtım Giderleri üretim maliyetine dâhil edilir.\n\nIII. Yansıtma hesapları dönem sonunda ilgili gider hesaplarıyla karşılıklı kapatılır.',
        {
            'A': 'I ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'A',
        'I ve III doğrudur. II yanlıştır: pazarlama, satış ve dağıtım giderleri **dönem gideridir**; 761 aracılığıyla 631 hesabına aktarılır, üretim maliyetine girmez.',
        'THP 7/A',
    ),
    # düzey 3
    '0041': patch(
        "Bir üretim işletmesinde döneme ait giderler şöyledir: endirekt malzeme 55.000 ₺, endirekt işçilik 90.000 ₺, fabrika binası kirası 70.000 ₺, üretim makinelerinin amortismanı 45.000 ₺ ve genel müdürlük personeli ücreti 60.000 ₺.\n\n730 Genel Üretim Giderleri hesabında toplanacak tutar kaç ₺'dir?",
        {
            'A': '275.000',
            'B': '320.000',
            'C': '200.000',
            'D': '215.000',
            'E': '260.000',
        },
        'E',
        'Endirekt malzeme, endirekt işçilik, fabrika kirası ve üretim makinelerinin amortismanı genel üretim gideridir: 55.000 + 90.000 + 70.000 + 45.000 = **260.000 ₺**. Genel müdürlük personeli ücreti 770 Genel Yönetim Giderlerinde izlenir.',
        "1 Sıra No'lu MSUGT - 730 Genel Üretim Giderleri; 18 Nisan 2026 SGS gider sınıflandırma soru örüntüsü",
    ),
    # düzey 2
    '0042': patch(
        '7/A seçeneğinde, dönem içinde ilgili gider hesabında (ör. 730) biriken giderleri dönem sonunda ilgili maliyet/sonuç hesabına aktarmak için kullanılan hesaplara ne ad verilir?',
        {
            'A': 'Bilanço varlık ve kaynak hesapları',
            'B': 'Karşılık ayırma hesapları (ör. 129)',
            'C': 'Düzenleyici aktif (pasif) hesaplar',
            'D': 'Yansıtma hesapları (ör. 711, 721, 731 …)',
            'E': 'Nazım (bilgi amaçlı takip edilen) hesaplar',
        },
        'D',
        "7/A'da dönem sonunda gider hesaplarını kapatıp ilgili maliyet (151/152) veya sonuç (630/631/632/660) hesaplarına aktarmak için **yansıtma hesapları** (711 DİMM Yansıtma, 721, 731, 761, 771, 781 vb.) kullanılır.",
        "1 Sıra No'lu MSUGT - 71x/72x/73x yansıtma",
    ),
    # düzey 2
    '0043': patch(
        '7/B seçeneğinde giderler hangi esasa göre izlenir?',
        {
            'A': 'Dönemin satış hasılatı esasına göre',
            'B': 'Gider çeşidi esasına göre (790-797 gider çeşitleri hesaplarında)',
            'C': 'Fonksiyon (işlev) esasına göre, yansıtma hesaplarıyla birlikte ayrıntılı biçimde',
            'D': 'Giderin oluştuğu gider yeri esasına göre',
            'E': 'İşletmenin aktif varlıkları esasına göre izlenir',
        },
        'B',
        '**7/B** seçeneğinde giderler **çeşit esasına** göre 790-797 hesaplarında (İlk Madde ve Malzeme, İşçi Ücret ve Giderleri, Dışarıdan Sağlanan Fayda ve Hizmetler, Amortismanlar vb.) izlenir.',
        "1 Sıra No'lu MSUGT - 7/B (790-799)",
    ),
    # düzey 2
    '0044': patch(
        "Maliyet muhasebesinde 'gider yeri' kavramıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Gider yeri, giderin oluştuğu bölüm veya faaliyet birimidir',
            'B': 'Üretim, montaj ve yönetim bölümleri birer gider yeridir',
            'C': 'Gider yeri, giderlerin türlerine göre ayrılmasıdır',
            'D': 'Gider yerleri esas ve yardımcı gider yerleri olarak ayrılabilir',
            'E': 'Endirekt giderler önce gider yerlerine dağıtılabilir',
        },
        'C',
        "Gider yeri, giderin oluştuğu veya katlanıldığı bölüm, kısım ya da faaliyet birimidir (üretim, montaj, yönetim vb.); esas ve yardımcı gider yerleri olarak ayrılır, endirekt giderler önce gider yerlerine dağıtılır. Giderin türüne göre sınıflandırılması 'gider çeşidi' kavramıdır.",
        "1 Sıra No'lu MSUGT - gider yeri/çeşidi",
    ),
    # düzey 2
    '0045': patch(
        "7/A seçeneğini uygulayan işletmenin dönem sonunda gider hesaplarının kalanları şöyledir: 730 Genel Üretim Giderleri 150.000 ₺, 750 Araştırma ve Geliştirme Giderleri 30.000 ₺, 760 Pazarlama Satış ve Dağıtım Giderleri 80.000 ₺, 770 Genel Yönetim Giderleri 110.000 ₺, 780 Finansman Giderleri 40.000 ₺. Gider hesapları ilgili yansıtma hesapları aracılığıyla kapatılmıştır.\n\nBuna göre gelir tablosunda '63 Faaliyet Giderleri' grubunda gösterilecek toplam tutar kaç ₺'dir?",
        {
            'A': '260.000',
            'B': '190.000',
            'C': '300.000',
            'D': '220.000',
            'E': '210.000',
        },
        'D',
        "63 grubu: 630 Araştırma ve Geliştirme Giderleri (750'den) 30.000 ₺ + 631 Pazarlama, Satış ve Dağıtım Giderleri (760'tan) 80.000 ₺ + 632 Genel Yönetim Giderleri (770'ten) 110.000 ₺ = 220.000 ₺. 730 üretim maliyetine, 780 ise 66 Finansman Giderleri grubuna aktarılır.",
        "1 Sıra No'lu MSUGT - 760/761 → 631",
    ),
    # düzey 3
    '0046': patch(
        "Bir üretim işletmesinde dönem başı ilk madde ve malzeme stoku 50.000 ₺, dönem içi alışlar 300.000 ₺ ve dönem sonu stok 40.000 ₺'dir. Kullanılan malzemenin 20.000 ₺'si endirekt olup 140.000 ₺ tutarındaki genel üretim giderine dâhildir. Direkt işçilik 180.000 ₺; dönem başı ve sonu yarı mamul stokları sırasıyla 60.000 ve 90.000 ₺; dönem başı ve sonu mamul stokları ise 70.000 ve 50.000 ₺'dir.\n\nTamamlanan mamul maliyeti ile satılan mamuller maliyeti sırasıyla kaç ₺'dir?",
        {
            'A': '600.000 ve 580.000',
            'B': '580.000 ve 600.000',
            'C': '610.000 ve 630.000',
            'D': '580.000 ve 560.000',
            'E': '560.000 ve 580.000',
        },
        'B',
        "Kullanılan toplam malzeme 50.000 + 300.000 − 40.000 = 310.000 ₺; direkt kısmı 290.000 ₺'dir. Üretim giderleri 290.000 + 180.000 + 140.000 = 610.000 ₺; tamamlanan mamul maliyeti 60.000 + 610.000 − 90.000 = **580.000 ₺**'dir. Satılan mamuller maliyeti 70.000 + 580.000 − 50.000 = **600.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Satışların Maliyeti Tablosu; 2025-2026 SGS tablo akışı soru örüntüsü",
    ),
    # düzey 2
    '0047': patch(
        "Üretimi tamamlanan mamullerin, üretim maliyetiyle stoklara alınması Tekdüzen Hesap Planı'nda hangi hesaba yapılır?",
        {
            'A': '152 Mamuller',
            'B': '151 Yarı Mamuller - Üretim',
            'C': '153 Ticari Mallar',
            'D': '150 İlk Madde ve Malzeme',
            'E': '620 Satılan Mamuller Maliyeti',
        },
        'A',
        "Üretimi tamamlanan mamuller, üretim maliyetiyle **152 Mamuller** hesabına alınır (151 Yarı Mamuller - Üretim'den aktarılır). Satılınca 620 Satılan Mamuller Maliyeti'ne geçer.",
        "1 Sıra No'lu MSUGT - 152 / 151",
    ),
    # düzey 2
    '0048': patch(
        "7/A seçeneğinde '750 Araştırma ve Geliştirme Giderleri', dönem sonunda 751 yansıtma hesabı aracılığıyla gelir tablosundaki hangi hesaba aktarılır?",
        {
            'A': '263 Araştırma ve Geliştirme Giderleri',
            'B': '660 Kısa Vadeli Borçlanma Giderleri (-)',
            'C': '631 Pazarlama, Satış ve Dağıtım Giderleri (-)',
            'D': '632 Genel Yönetim Giderleri (-)',
            'E': '630 Araştırma ve Geliştirme Giderleri (-)',
        },
        'E',
        '750 Araştırma ve Geliştirme Giderleri, 751 yansıtma ile gelir tablosundaki **630 Araştırma ve Geliştirme Giderleri (-)** hesabına aktarılır.',
        "1 Sıra No'lu MSUGT - 750/751 → 630",
    ),
    # düzey 2
    '0049': patch(
        "'Dönem gideri' niteliğindeki genel yönetim (770) ve pazarlama-satış-dağıtım (760) giderleri ile 'üretim maliyeti' arasındaki fark ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '770 ve 760 dönem içinde elde edilen yurt içi satış hasılatının birer unsuru olarak gelir tablosunda gösterilir.',
            'B': '770 ve 760 giderleri bilançoda aktifleştirilen birer varlık kalemi olup dönem sonunda amortismana tabi tutulur.',
            'C': 'Üretim maliyeti 770 Genel Yönetim ve 760 Pazarlama giderlerinden oluşur; 710/720/730 ise dönem gideridir.',
            'D': "770 ve 760 üretim maliyetine girmez; dönem gideri olarak gelir tablosunda (632/631) yer alır. Üretim maliyeti ise 710+720+730'dan oluşur.",
            'E': '770 ve 760 giderleri üretim maliyetinin bir unsurudur; dönem içinde 151 ve 152 stok hesaplarına eklenerek doğrudan mamul maliyetine dâhil edilir.',
        },
        'D',
        "**770 Genel Yönetim** ve **760 Pazarlama Satış Dağıtım** giderleri üretim maliyetine **girmez**; dönem gideri olarak gelir tablosunda (632/631) yer alır. **Üretim maliyeti = 710 + 720 + 730**'dan oluşur.",
        "1 Sıra No'lu MSUGT - üretim maliyeti / dönem gideri",
    ),
    # düzey 2
    '0050': patch(
        "Hizmet işletmelerinde '740 Hizmet Üretim Maliyeti', dönem sonunda 741 yansıtma hesabı aracılığıyla gelir tablosunda hangi hesaba aktarılır?",
        {
            'A': '620 Satılan Mamuller Maliyeti (-)',
            'B': '622 Satılan Hizmet Maliyeti (-)',
            'C': '621 Satılan Ticari Mallar Maliyeti (-)',
            'D': '631 Pazarlama, Satış ve Dağıtım Giderleri (-)',
            'E': '632 Genel Yönetim Giderleri (-)',
        },
        'B',
        '740 Hizmet Üretim Maliyeti, 741 yansıtma ile gelir tablosundaki **622 Satılan Hizmet Maliyeti (-)** hesabına aktarılır.',
        "1 Sıra No'lu MSUGT - 740/741 → 622",
    ),
    # düzey 3
    '0051': patch(
        "Standart maliyet yöntemini uygulayan işletmede 721 Direkt İşçilik Giderleri Yansıtma Hesabı 600.000 ₺'dir. Dönemde 25.000 ₺ olumlu ücret farkı ve 40.000 ₺ olumsuz süre farkı oluşmuştur.\n\n720 Direkt İşçilik Giderleri hesabının fiilî tutarı kaç ₺'dir?",
        {
            'A': '640.000',
            'B': '600.000',
            'C': '615.000',
            'D': '575.000',
            'E': '665.000',
        },
        'C',
        'Fiilî direkt işçilik maliyeti = standart maliyet − olumlu ücret farkı + olumsuz süre farkıdır. 600.000 − 25.000 + 40.000 = **615.000 ₺** bulunur.',
        "1 Sıra No'lu MSUGT - 720/721/722/723; 2024-2026 SGS standart işçilik farkları soru örüntüsü",
    ),
    # düzey 2
    '0052': patch(
        '7/A seçeneğinde yansıtma yoluyla giderlerin aktarıldığı gelir tablosu hesaplarıyla ilgili aşağıdaki eşleştirmelerden hangisi doğrudur?',
        {
            'A': '760 → 631 ; 770 → 632 ; 780 → 660/661',
            'B': '760 → 600 ; 770 → 601 ; 780 → 602',
            'C': '760 → 620 ; 770 → 621 ; 780 → 622',
            'D': '760 → 632 ; 770 → 631 ; 780 → 621',
            'E': '760 → 151 ; 770 → 152 ; 780 → 153',
        },
        'A',
        'Doğru eşleştirme: **760 Pazarlama → 631**; **770 Genel Yönetim → 632**; **780 Finansman → 660/661** (66 grubu). Üretim giderleri (710/720/730) ise 151/152 üretim maliyetine gider.',
        "1 Sıra No'lu MSUGT - 760/770/780 yansıtma",
    ),
    # düzey 2
    '0053': patch(
        "Bir üretim işletmesi dönem için 600.000 ₺ genel üretim gideri ve 30.000 makine saati öngörmüştür. GÜG mamullere makine saatine göre yüklenecektir. K45 siparişi 350 makine saati kullanmıştır.\n\nK45 siparişine yüklenecek genel üretim gideri kaç ₺'dir?",
        {
            'A': '6.500',
            'B': '6.000',
            'C': '3.500',
            'D': '5.250',
            'E': '7.000',
        },
        'E',
        'Tahminî GÜG yükleme oranı 600.000 / 30.000 = **20 ₺/makine saati**dir. K45 siparişine 350 × 20 = **7.000 ₺** genel üretim gideri yüklenir.',
        'Maliyet muhasebesi - tahminî genel üretim gideri yükleme oranı; 2024-2026 SGS soru örüntüsü',
    ),
    # düzey 3
    '0054': patch(
        "Standart maliyet yöntemini kullanan işletmede dönem sonunda 50.000 ₺ olumsuz toplam maliyet farkı oluşmuştur. Fark dağıtılmadan önce standart maliyetle 151 Yarı Mamuller - Üretim 100.000 ₺, 152 Mamuller 150.000 ₺ ve 620 Satılan Mamuller Maliyeti 250.000 ₺ borç bakiyesi vermektedir. Fark bu hesaplara bakiyeleri oranında dağıtılacaktır.\n\nDağıtımda 620 hesaba borç yazılacak tutar kaç ₺'dir?",
        {
            'A': '15.000',
            'B': '12.500',
            'C': '25.000',
            'D': '35.000',
            'E': '10.000',
        },
        'C',
        "Toplam standart maliyet bakiyesi 100.000 + 150.000 + 250.000 = 500.000 ₺'dir. 620 hesabın payı %50 olduğundan olumsuz farkın 50.000 × %50 = **25.000 ₺** kısmı 620 hesaba borç yazılır.",
        "1 Sıra No'lu MSUGT - standart maliyet farklarının 151/152/620 hesaplarına dağıtımı; 18 Temmuz 2026 SGS soru örüntüsü",
    ),
    # düzey 3
    '0055': patch(
        "Standart maliyet yöntemini kullanan işletmede 710 Direkt İlk Madde ve Malzeme Giderleri 520.000 ₺, 711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma 500.000 ₺'dir. Ayrıca 15.000 ₺ olumlu fiyat farkı ve 35.000 ₺ olumsuz miktar farkı bulunmaktadır.\n\nDönem sonu kapanış kaydı hangisidir?",
        {
            'A': '711 hesabı 500.000 ₺ ve 712 hesabı 15.000 ₺ borç; 710 hesabı 520.000 ₺ alacak; 713 hesabı kullanılmaz',
            'B': '710 hesabı 520.000 ₺ borç; 711 hesabı 500.000 ₺ ve 712 hesabı 20.000 ₺ alacak',
            'C': '710 hesabı 520.000 ₺ ve 713 hesabı 35.000 ₺ borç; 711 hesabı 500.000 ₺ ve 712 hesabı 55.000 ₺ alacak',
            'D': '711 hesabı 500.000 ₺ ve 713 hesabı 35.000 ₺ borç; 710 hesabı 520.000 ₺ ve 712 hesabı 15.000 ₺ alacak',
            'E': '711 hesabı 500.000 ₺ ve 712 hesabı 15.000 ₺ borç; 710 hesabı 480.000 ₺ ve 713 hesabı 35.000 ₺ alacak',
        },
        'D',
        "Kapanışta yansıtma hesabı 711 **500.000 ₺ borç**, olumsuz miktar farkı 713 **35.000 ₺ borç** kaydedilir. Fiilî gider hesabı 710 **520.000 ₺ alacak**, olumlu fiyat farkı 712 ise **15.000 ₺ alacak** kaydedilir; borç ve alacak toplamı 535.000 ₺'dir.",
        "1 Sıra No'lu MSUGT - 710/711/712/713; standart maliyet kapanışı",
    ),
    # düzey 2
    '0056': patch(
        'Fabrika makinelerinin elektrik tüketimine ait gider, 7/A ve 7/B seçeneklerinde sırasıyla hangi hesaplarda izlenir?',
        {
            'A': '760 Pazarlama, Satış ve Dağıtım Giderleri; 794 Çeşitli Giderler',
            'B': '730 Genel Üretim Giderleri; 793 Dışarıdan Sağlanan Fayda ve Hizmetler',
            'C': '720 Direkt İşçilik Giderleri; 791 İşçi Ücret ve Giderleri',
            'D': '710 Direkt İlk Madde ve Malzeme Giderleri; 790 İlk Madde ve Malzeme Giderleri',
            'E': '770 Genel Yönetim Giderleri; 797 Finansman Giderleri',
        },
        'B',
        '7/A giderleri fonksiyon esasına göre izlediğinden fabrika elektriği **730 Genel Üretim Giderleri** hesabındadır. 7/B gider çeşidi esasını kullandığından aynı gider **793 Dışarıdan Sağlanan Fayda ve Hizmetler** hesabında izlenir.',
        "1 Sıra No'lu MSUGT - 7/A ve 7/B hesap ayrımı, 730/793",
    ),
    # düzey 3
    '0057': patch(
        'Maliyet hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Normal maliyet yönteminde değişken genel üretim giderleri fiilî üretime, sabit genel üretim giderleri normal kapasiteye göre maliyete yüklenir.\n\nII. Düşük kapasite nedeniyle dağıtılmayan sabit genel üretim gideri stok maliyetine eklenmez.\n\nIII. 7/A seçeneğinde 710, 720 ve 730 hesaplarda toplanan üretim giderleri 711, 721 ve 731 yansıtma hesapları aracılığıyla 151 hesaba aktarılır.\n\nIV. 7/B seçeneğinde giderler çeşit esasına göre 790-797 hesaplarda izlenir; 798 yansıtma ve 799 üretim maliyeti hesapları kullanılır.',
        {
            'A': 'I, II, III ve IV',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'Yalnız IV',
        },
        'A',
        'Dört ifade de doğrudur. Normal maliyet düşük kapasitenin stok maliyetini yapay biçimde artırmasını önler. 7/A fonksiyon ve ilgili yansıtma hesaplarını; 7/B ise gider çeşitleriyle 798 ve 799 hesaplarını kullanır.',
        "TMS 2 Stoklar, par. 12-13; 1 Sıra No'lu MSUGT - 7/A ve 7/B",
    ),
    # düzey 3
    '0058': patch(
        '7/A seçeneğini uygulayan işletmede dönem sonunda 710 hesabında 150.000 ₺, 720 hesabında 100.000 ₺ ve 730 hesabında 70.000 ₺ bulunmaktadır; yarı mamul stoku yoktur. Üretim giderleri yansıtma hesapları aracılığıyla üretim hesabına aktarılmaktadır. Buna göre aktarma kaydında aşağıdakilerden hangisi yer almaz?',
        {
            'A': '151 Yarı Mamuller - Üretim hesabı 320.000 ₺ borçlandırılır',
            'B': '711 Direkt İlk Madde ve Malzeme Yansıtma hesabı 150.000 ₺ alacaklandırılır',
            'C': '721 Direkt İşçilik Giderleri Yansıtma hesabı 100.000 ₺ alacaklandırılır',
            'D': '731 Genel Üretim Giderleri Yansıtma hesabı 70.000 ₺ alacaklandırılır',
            'E': '710 Direkt İlk Madde ve Malzeme Giderleri hesabı 150.000 ₺ alacaklandırılır',
        },
        'E',
        "Kayıt: 151 (borç) 320.000 / 711 (alacak) 150.000 + 721 (alacak) 100.000 + 731 (alacak) 70.000. 7/A'da gider hesapları doğrudan alacaklandırılmaz; yansıtma hesaplarıyla aktarılır, dönem sonunda 710 ile 711 karşılıklı kapatılır.",
        'THP 711, 721, 731, 151',
    ),
    # düzey 2
    '0059': patch(
        '7/B seçeneğini uygulayan bir işletmenin maliyet hesapları incelenmektedir.\n\nBuna göre aşağıdaki hesaplardan hangisi 7/B seçeneğinde kullanılmaz?',
        {
            'A': '791 İşçi Ücret ve Giderleri',
            'B': '792 Memur Ücret ve Giderleri',
            'C': '730 Genel Üretim Giderleri',
            'D': '795 Vergi, Resim ve Harçlar',
            'E': '796 Amortisman ve Tükenme Payları',
        },
        'C',
        '7/B seçeneğinde giderler çeşit esasına göre 790-797 gider çeşidi hesaplarında izlenir; 791, 792, 795 ve 796 bu hesaplardandır. 730 Genel Üretim Giderleri ise fonksiyon esasına dayanan 7/A seçeneğine aittir.',
        'THP 7/B Gider Çeşitleri',
    ),
    # düzey 3
    '0060': patch(
        "Bir üretim işletmesinin dönem başı ilk madde ve malzeme stoku 50.000 ₺, dönem içi alışları 320.000 ₺ ve dönem sonu stoku 70.000 ₺'dir. Üretime verilen malzemenin %80'i mamule doğrudan yüklenebilmekte, kalanı yardımcı malzeme niteliğindedir (7/A seçeneği). Buna göre 730 Genel Üretim Giderleri hesabına yazılacak tutar kaç ₺'dir?",
        {
            'A': '240.000 ₺',
            'B': '300.000 ₺',
            'C': '74.000 ₺',
            'D': '60.000 ₺',
            'E': '64.000 ₺',
        },
        'D',
        'Kullanılan malzeme 50.000 + 320.000 − 70.000 = 300.000 ₺. Direkt kısım 240.000 ₺ (710), endirekt (yardımcı) kısım 300.000 × %20 = **60.000 ₺** (730).',
        'THP 150, 710, 730',
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
    print(f"1 paket / {len(PATCHES)} soru ('Maliyet Hesaplari' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
