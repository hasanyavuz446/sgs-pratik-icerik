#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uretim Maliyeti Tablosu ve Maliyet Sistemleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

YENI KONU (maliyet muhasebesi). 2019-2026 cikmis sinavlarinda maliyet sorularinin ~%37'si (54/144) bu gruptan: satislarin/uretim maliyeti tablosu, tam/degisken/normal maliyet sistemleri ve kapasite, giderlerin siniflandirilmasi ve 7/A akisi, ilk madde stok degerlemesi. Havuzda karsiligi yoktu. 60 soru, her biri kendi verisiyle: SMM zinciri, iki donemli tablolarda devreden stok, DIMM stok akisi, brut kardan geriye hesap (satis iadesi dahil), birim maliyetten DSYM/uretim gideri, uretim+ticaret, FIFO ile mamul akisi, GUG kalemlerinin ayiklanmasi; tam-normal farki, yontem tutarlarindan kapasite orani, tersine sabit/degisken GUG, degisken maliyete geciste kar etkisi; 7/A 151-711/731 akisi, 620 tutari, 731 yukleme farki kaydi, iscilik siniflandirmasi; FIFO/tartili/hareketli ortalama ve ters hesaplar. Tutarlar Fraction ile hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Maliyet muhasebesi - uretim maliyeti, satislarin maliyeti tablosu, maliyet sistemleri · Tekduzen Hesap Plani 7/A
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliyet_muhasebesi/uretim_maliyeti_ve_sistemler.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (tablolu çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "mmuh-umt-gen-"


def patch(stem, options, answer, solution, ref='Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "Bir üretim işletmesinin döneme ait maliyet ve stok bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Direkt ilk madde ve malzeme giderleri | 180.000 |\n| Direkt işçilik giderleri | 120.000 |\n| Genel üretim giderleri | 150.000 |\n| Dönem başı yarı mamul | 30.000 |\n| Dönem sonu yarı mamul | 50.000 |\n| Dönem başı mamul | 60.000 |\n| Dönem sonu mamul | 85.000 |\n\nBuna göre satılan mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '405.000',
            'B': '450.000',
            'C': '430.000',
            'D': '445.000',
            'E': '455.000',
        },
        'A',
        'Üretim giderleri = 180.000 + 120.000 + 150.000 = 450.000 ₺. Üretilen mamul maliyeti = 450.000 + DBYM 30.000 − DSYM 50.000 = 430.000 ₺. Satılan mamuller maliyeti = 430.000 + DBM 60.000 − DSM 85.000 = **405.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0002': patch(
        "Satış iadeleri brüt satışların %10'u olan bir üretim işletmesinin bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Brüt satışlar | 300.000 |\n| Brüt satış kârı | 110.000 |\n| Üretilen mamuller maliyeti | 150.000 |\n| Dönem sonu mamul stokları | 45.000 |\n\nBuna göre dönem başı mamul stokları kaç ₺'dir?",
        {
            'A': '45.000',
            'B': '85.000',
            'C': '35.000',
            'D': '55.000',
            'E': '10.000',
        },
        'D',
        'Net satışlar = 300.000 − %10 iade = 270.000 ₺. Satılan mamuller maliyeti = net satışlar − brüt kâr = 270.000 − 110.000 = 160.000 ₺. SMM = DBM + üretilen − DSM → 160.000 = DBM + 150.000 − 45.000 → DBM = **55.000 ₺**. Brüt kâr net satışlardan hesaplanır.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0003': patch(
        "Bir üretim işletmesinin R1 mamulüne ait dönem verileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Direkt ilk madde ve malzeme giderleri | 12.000 |\n| Dönem başı yarı mamul | 3.000 |\n| Genel üretim giderleri | 15.000 |\n| Direkt işçilik giderleri | 9.000 |\n\nDönemde birim üretim maliyeti 110 ₺ olan 300 adet mamulün üretimi tamamlandığına göre dönem sonunda kalan yarı mamulün değeri kaç ₺'dir?",
        {
            'A': '9.000',
            'B': '39.000',
            'C': '3.000',
            'D': '33.000',
            'E': '6.000',
        },
        'E',
        'Dönemin toplam maliyeti = 12.000 + 9.000 + 15.000 + DBYM 3.000 = 39.000 ₺. Tamamlananlar 300 × 110 = 33.000 ₺. Dönem sonu yarı mamul = **6.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0004': patch(
        "Hem üretim hem ticaret yapan bir işletmede dönem sonunda yarı mamul ve mamul stoku bulunmamaktadır. Döneme ait bilgiler şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 40.000 |\n| Direkt işçilik giderleri | 25.000 |\n| Genel üretim giderleri | 35.000 |\n| Dönem başı yarı mamul | 8.000 |\n| Dönem başı mamul | 15.000 |\n| Dönem başı ticari mal | 20.000 |\n| Ticari mal alışları | 50.000 |\n| Dönem sonu ticari mal | 12.000 |\n\nBuna göre işletmenin satışların maliyeti toplamı kaç ₺'dir?",
        {
            'A': '123.000',
            'B': '181.000',
            'C': '158.000',
            'D': '173.000',
            'E': '193.000',
        },
        'B',
        'Satılan mamuller maliyeti = 100.000 + DBYM 8.000 + DBM 15.000 = 123.000 ₺. Satılan ticari mallar maliyeti = 20.000 + 50.000 − 12.000 = 58.000 ₺. Satışların maliyeti = **181.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0005': patch(
        "Tek tip mamul üreten bir işletmede dönemde 100 ton mamul tamamlanmış, 80 tonu satılmıştır. Dönem başında mamul stoku yoktur. Maliyet verileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 120.000 |\n| Genel üretim giderleri | 60.000 |\n| Direkt işçilik giderleri | 40.000 |\n| Dönem sonu yarı mamul | 50.000 |\n| Dönem başı yarı mamul | 30.000 |\n\nBuna göre dönem sonu mamul stokunun maliyeti kaç ₺'dir?",
        {
            'A': '44.000',
            'B': '40.000',
            'C': '48.000',
            'D': '50.000',
            'E': '160.000',
        },
        'B',
        "Üretilen mamul maliyeti = 220.000 + 30.000 − 50.000 = 200.000 ₺ → ton başına 2.000 ₺. Kalan 20 ton × 2.000 = **40.000 ₺**. Satılan mamuller maliyeti 160.000 ₺'dir.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0006': patch(
        'Bir üretim işletmesinin döneme ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM dönem başı stoku | 20.000 |\n| DİMM alışları | 90.000 |\n| DİMM dönem sonu stoku | 15.000 |\n| Direkt işçilik giderleri | 60.000 |\n| Genel üretim giderleri | 45.000 |\n| Dönem başı yarı mamul | 10.000 |\n| Dönem sonu yarı mamul | 25.000 |\n| Dönem başı mamul | 30.000 |\n| Dönem sonu mamul | 20.000 |\n| Net satışlar | 280.000 | Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Satılan mamuller maliyeti 195.000 ₺'dir.",
            'B': "Brüt satış kârı 85.000 ₺'dir.",
            'C': "Üretilen mamuller maliyeti 185.000 ₺'dir.",
            'D': "Satılabilir mamuller maliyeti 205.000 ₺'dir.",
            'E': "Direkt ilk madde ve malzeme gideri 95.000 ₺'dir.",
        },
        'D',
        "Satılabilir mamuller = üretilen 185.000 + DBM 30.000 = 215.000 ₺'dir; 205.000 ₺ yanlıştır. Diğerleri doğrudur: DİMM = 20.000 + 90.000 − 15.000 = 95.000; üretim giderleri 200.000; üretilen 200.000 + 10.000 − 25.000 = 185.000; SMM 215.000 − 20.000 = 195.000; brüt kâr 280.000 − 195.000 = 85.000 ₺.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0007': patch(
        "Bir üretim işletmesinde ekim ve kasım aylarında dönem sonu yarı mamul stoku bulunmamaktadır. İki aya ait bilgiler şöyledir:\n\n| Kalem | Ekim (₺) | Kasım (₺) |\n|---|---|---|\n| DİMM giderleri | 60.000 | 70.000 |\n| Direkt işçilik | 90.000 | 110.000 |\n| Genel üretim | 150.000 | 140.000 |\n| Dönem başı yarı mamul | 30.000 | ? |\n\nBuna göre kasım ayında üretilen mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '290.000',
            'B': '330.000',
            'C': '350.000',
            'D': '650.000',
            'E': '320.000',
        },
        'E',
        "Ekim sonunda yarı mamul kalmadığından kasımın dönem başı yarı mamulü **sıfırdır**. Kasım üretilen mamul maliyeti = 70.000 + 110.000 + 140.000 = **320.000 ₺**. Ekimin 30.000 ₺'lik başlangıç stoku ekimde tamamlanmıştır (ekim: 330.000 ₺).",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0008': patch(
        "Bir işletmenin dönem giderleri: DİMM 90.000 ₺, direkt işçilik 70.000 ₺ ve genel üretim giderleri 55.000 ₺'dir. Buna göre asal (birincil) maliyet ile dönüştürme (şekillendirme) maliyeti sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
        {
            'A': '125.000 ve 160.000',
            'B': '160.000 ve 145.000',
            'C': '215.000 ve 125.000',
            'D': '145.000 ve 125.000',
            'E': '160.000 ve 125.000',
        },
        'E',
        'Asal maliyet = DİMM + direkt işçilik = 160.000 ₺. Dönüştürme maliyeti = direkt işçilik + GÜG = 125.000 ₺. Direkt işçilik her ikisinde de yer alır.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0009': patch(
        "Bir üretim işletmesinin döneme ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 360.000 |\n| Direkt işçilik giderleri | 540.000 |\n| Genel üretim giderleri (%50'si değişken) | 600.000 |\n| Faaliyet giderleri (tamamı sabit) | 250.000 |\n\nÜretim kapasitesi 12.500 adet, dönemde üretilen miktar 10.000 adettir. Normal maliyet yöntemine göre birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '115,20',
            'B': '169',
            'C': '144',
            'D': '120',
            'E': '150',
        },
        'C',
        'Kapasite kullanım oranı 10.000 ÷ 12.500 = %80. Normal maliyet = DİMM + DİG + değişken GÜG + sabit GÜG × %80 = 360.000 + 540.000 + 300.000 + 240.000 = 1.440.000 ₺ → birim **144 ₺**. Faaliyet giderleri üretim maliyetine girmez.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0010': patch(
        'Tam maliyet sistemini benimsediğinde toplam maliyeti 90.000 ₺, direkt giderleri 50.000 ₺ olan bir işletme %75 kapasiteyle çalışmaktadır. Normal maliyet sistemi benimsendiğinde toplam maliyet 85.000 ₺ olmaktadır. İşletme değişken maliyet sistemini kullanır ve 2.000 birim üretirse birim maliyet kaç ₺ olur?',
        {
            'A': '32,50',
            'B': '35',
            'C': '42,50',
            'D': '45',
            'E': '25',
        },
        'B',
        "Tam − normal = kullanılmayan %25'lik kapasitenin sabit GÜG'ü: 5.000 ₺ → sabit GÜG = 5.000 ÷ 0,25 = 20.000 ₺. Değişken maliyet = 90.000 − 20.000 = 70.000 ₺ → birim **35 ₺** (değişken GÜG 20.000 ₺).",
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0011': patch(
        'Tam maliyetleme yöntemini kullanan bir işletmenin döneme ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 300.000 |\n| Direkt işçilik giderleri | 150.000 |\n| Genel üretim giderleri (%30 değişken, %70 sabit) | 400.000 |\n\nDönemde 10.000 adet üretilmiş, 7.000 adet satılmıştır; dönem başında stok yoktur. İşletme değişken maliyetleme yöntemine geçseydi dönem kârı nasıl değişirdi?',
        {
            'A': '84.000 ₺ azalırdı',
            'B': 'Değişmezdi',
            'C': '280.000 ₺ azalırdı',
            'D': '84.000 ₺ artardı',
            'E': '196.000 ₺ azalırdı',
        },
        'A',
        "Sabit GÜG = 400.000 × %70 = 280.000 ₺ → birim 28 ₺. Tam maliyette stokta kalan 3.000 adet bu sabit gideri taşır (84.000 ₺ ertelenir). Değişken maliyette sabit GÜG'ün tamamı dönem gideri olur; kâr **84.000 ₺ azalır**.",
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0012': patch(
        'Maliyet sistemleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Değişken maliyet sisteminde değişken genel yönetim giderleri de mamul maliyetine dahil edilir.\n\nII. Normal maliyet sisteminde sabit genel üretim giderleri kapasite kullanım oranında mamule yüklenir.\n\nIII. Tam maliyet sisteminde sabit ve değişken bütün üretim giderleri mamul maliyetine girer.',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        '**I yanlıştır:** değişken maliyette mamule yalnız değişken **üretim** giderleri (DİMM, DİG, değişken GÜG) yüklenir; yönetim giderleri dönem gideridir. **II doğrudur:** kullanılmayan kapasitenin payı dönem gideri olur. **III doğrudur.** Doğru cevap **II ve III**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0013': patch(
        "Bir üretim işletmesinde ocak ayında DİMM 540.000 ₺, direkt işçilik 380.000 ₺ ve sabit GÜG 160.000 ₺ gerçekleşmiştir; değişken GÜG bilinmemektedir. Aylık kapasitesi 12.000 adet olan işletme bu dönemde 9.000 adet üretmiş; yarı mamul stoku yoktur. Normal maliyet yöntemine göre birim maliyet 130 ₺ ise değişken GÜG kaç ₺'dir?",
        {
            'A': '90.000',
            'B': '250.000',
            'C': '170.000',
            'D': '50.000',
            'E': '130.000',
        },
        'E',
        'Normal maliyet = 130 × 9.000 = 1.170.000 ₺. Kapasite oranı %75 → yüklenen sabit GÜG 160.000 × %75 = 120.000 ₺. Değişken GÜG = 1.170.000 − 540.000 − 380.000 − 120.000 = **130.000 ₺**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0014': patch(
        'Normal kapasitesinin altında çalışan ve bütün giderleri pozitif olan bir üretim işletmesinde aynı üretim için hesaplanan birim maliyetlerin büyükten küçüğe sıralaması aşağıdakilerden hangisidir?',
        {
            'A': 'Normal > Tam > Değişken > Asal',
            'B': 'Tam > Değişken > Normal > Asal',
            'C': 'Değişken > Normal > Tam > Asal',
            'D': 'Tam > Normal > Asal > Değişken',
            'E': 'Tam > Normal > Değişken > Asal',
        },
        'E',
        "Asal maliyet yalnız DİMM + DİG'dir; değişken maliyet buna değişken GÜG'ü ekler; normal maliyet ayrıca sabit GÜG'ün kapasite kullanım oranı kadarını ekler; tam maliyet sabit GÜG'ün tamamını ekler. Kapasite altında çalışıldığı için normal < tam olur.",
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0015': patch(
        "7/A seçeneğini uygulayan bir üretim işletmesi 150.000 ₺'lik direkt hammadde ile 10.000 ₺'lik işletme malzemesini üretimde kullanmıştır. Üretim maliyetinin hesaplanması sırasında 151 Yarı Mamuller – Üretim hesabı borçlandırılırken alacaklandırılacak hesaplarla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '711 DİMM Yansıtma 150.000 ₺ ve 721 DİG Yansıtma 10.000 ₺',
            'B': '710 DİMM Giderleri 150.000 ₺ ve 730 GÜG 10.000 ₺',
            'C': '711 DİMM Yansıtma 150.000 ₺ ve 731 GÜG Yansıtma 10.000 ₺',
            'D': '150 İlk Madde ve Malzeme 160.000 ₺',
            'E': '711 DİMM Yansıtma 160.000 ₺',
        },
        'C',
        'Kullanımda önce 710 (150.000) ve 730 (10.000) borç, 150 alacak yazılır. Maliyete aktarımda 151 borçlandırılır; karşılığında yansıtma hesapları alacaklandırılır: 711 150.000 ₺ (direkt hammadde) ve 731 10.000 ₺ (işletme malzemesi endirekt malzeme olduğundan GÜG).',
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 2
    '0016': patch(
        '7/A seçeneğinde maliyet hesaplarının işleyişiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel yönetim giderleri 730 Genel Üretim Giderleri hesabında izlenir.\n\nII. Satılan mamullerin maliyeti 710 DİMM Giderleri hesabına borç kaydedilir.\n\nIII. 151 Yarı Mamuller – Üretim hesabı, üretim giderleri yansıtma hesapları aracılığıyla borçlandırılır.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'C',
        "**I yanlıştır:** genel yönetim giderleri 770'te izlenir. **II yanlıştır:** satılan mamullerin maliyeti 620'de izlenir; 710 DİMM giderlerini toplar. **III doğrudur:** 711, 721, 731 alacaklandırılarak 151 borçlandırılır. Doğru cevap **Yalnız III**.",
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 2
    '0017': patch(
        "Bir işletme 1 Ekim'de fabrika binasının 12 aylık kirası olarak 120.000 ₺'yi peşin ödemiştir. Buna göre 31 Aralık'ta sona eren dönemde bu tutarın ne kadarı genel üretim gideri olarak üretim maliyetine girer?",
        {
            'A': '40.000',
            'B': '30.000',
            'C': '90.000',
            'D': '10.000',
            'E': '120.000',
        },
        'B',
        'Ödeme bir harcamadır; gider yalnız döneme düşen kısımdır. Ekim-Aralık 3 ay: 120.000 × 3/12 = **30.000 ₺** GÜG olur. Kalan 90.000 ₺ gelecek aylara ait gider olarak (180) izlenir.',
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 3
    '0018': patch(
        "Bir üretim işletmesinin K hammaddesine ait eylül ayı hareketleri şöyledir:\n\n| Tarih | İşlem | Miktar (kg) |\n|---|---|---|\n| 1 Eylül | Dönem başı (500 ₺/kg) | 600 |\n| 8 Eylül | Alış (550 ₺/kg) | 400 |\n| 15 Eylül | Üretime sevk | 500 |\n| 22 Eylül | Alış (700 ₺/kg) | 600 |\n| 28 Eylül | Üretime sevk | 700 |\n\nİşletme ilk giren ilk çıkar (FIFO) yöntemini kullandığına göre eylül ayında üretime gönderilen hammaddenin maliyeti kaç ₺'dir?",
        {
            'A': '660.000',
            'B': '280.000',
            'C': '600.000',
            'D': '740.000',
            'E': '705.000',
        },
        'A',
        '15 Eylül: 500 kg dönem başı stoktan × 500 = 250.000 ₺. 28 Eylül: kalan 100 kg × 500 = 50.000 + 400 kg × 550 = 220.000 + 200 kg × 700 = 140.000 → 410.000 ₺. Toplam **660.000 ₺**; dönem sonu 400 kg × 700 = 280.000 ₺.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 2
    '0019': patch(
        'İlk madde ve malzeme stok değerleme yöntemleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiyatların sürekli yükseldiği dönemde FIFO yöntemi dönem sonu stoku ortalama yönteme göre daha yüksek değerler.\n\nII. Dönemsel (tartılı) ağırlıklı ortalamada birim maliyet dönem sonunda bir kez hesaplanır.\n\nIII. Hareketli ortalamada yeni birim maliyet her çıkıştan sonra yeniden hesaplanır.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'B',
        "**I doğrudur:** FIFO'da stokta son (pahalı) alışlar kalır. **II doğrudur.** **III yanlıştır:** hareketli ortalamada ortalama her **girişten** sonra yeniden hesaplanır; çıkışlar son ortalamayla yapılır. Doğru cevap **I ve II**.",
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 3
    '0020': patch(
        "Bir işletmenin C malzemesinin dönem başı stoku 200 birim × 25 ₺'dir. Dönemde 300 birim × 30 ₺ alış yapılmış, ardından 400 birim üretime sevk edilmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Hareketli ortalamaya göre birim maliyet 28 ₺'dir.",
            'B': "FIFO yöntemine göre üretime sevk maliyeti 12.000 ₺'dir.",
            'C': "Hareketli ortalamaya göre üretime sevk maliyeti 11.200 ₺'dir.",
            'D': "İki yöntemin sevk maliyetleri arasındaki fark 200 ₺'dir.",
            'E': "FIFO yöntemine göre dönem sonu stok 3.000 ₺'dir.",
        },
        'B',
        "FIFO'da önce dönem başı stok kullanılır: 200 × 25 + 200 × 30 = 11.000 ₺; 12.000 ₺ (400 × 30) yanlıştır. Diğerleri doğrudur: hareketli ortalama (5.000 + 9.000) ÷ 500 = 28 ₺ → sevk 400 × 28 = 11.200 ₺; FIFO dönem sonu 100 × 30 = 3.000 ₺; fark 11.200 − 11.000 = 200 ₺.",
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 2
    '0021': patch(
        "Bir üretim işletmesinde dönemin üretim giderleri 620.000 ₺'dir. Dönem başı yarı mamul stokları 25.000 ₺, dönem sonu yarı mamul stokları 18.000 ₺; dönem başı mamul stokları 40.000 ₺, dönem sonu mamul stokları 52.000 ₺'dir. Buna göre dönemde üretilen mamullerin maliyeti ile satılan mamullerin maliyeti sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
        {
            'A': '613.000 ve 601.000',
            'B': '627.000 ve 639.000',
            'C': '615.000 ve 627.000',
            'D': '620.000 ve 608.000',
            'E': '627.000 ve 615.000',
        },
        'E',
        'Üretilen mamuller maliyeti = 620.000 + 25.000 − 18.000 = **627.000 ₺**. Satılan mamuller maliyeti = 627.000 + 40.000 − 52.000 = **615.000 ₺**. Yarı mamul stokları üretim maliyetini, mamul stokları satılan mamuller maliyetini düzeltir.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0022': patch(
        "Bir üretim işletmesinin iki yıla ait direkt ilk madde ve malzeme (DİMM) bilgileri şöyledir:\n\n| Kalem | 2025 (₺) | 2026 (₺) |\n|---|---|---|\n| DİMM dönem başı stoku | 45.000 | ? |\n| DİMM alışları | 125.000 | ? |\n| DİMM dönem sonu stoku | 30.000 | 50.000 |\n| DİMM gideri | ? | 160.000 |\n\nBuna göre 2026 yılında yapılan DİMM alışları kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '180.000',
            'C': '160.000',
            'D': '165.000',
            'E': '210.000',
        },
        'B',
        "2026 dönem başı stoku 2025 dönem sonu stokudur: 30.000 ₺. DİMM gideri = DB + alış − DS → 160.000 = 30.000 + alış − 50.000 → alış = **180.000 ₺**. (2025 gideri 140.000 ₺'dir.)",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0023': patch(
        "Bir üretim işletmesinde ocak ayı üretim giderlerinin %40'ı direkt ilk madde ve malzemeden, kalanı şekillendirme giderlerinden oluşmaktadır. Toplam üretim maliyeti 600.000 ₺ olup dönem başında 90.000 ₺, dönem sonunda 70.000 ₺ yarı mamul bulunmaktadır. Direkt işçilik giderleri 148.000 ₺ olduğuna göre genel üretim giderleri kaç ₺'dir?",
        {
            'A': '212.000',
            'B': '232.000',
            'C': '224.000',
            'D': '348.000',
            'E': '200.000',
        },
        'E',
        'Toplam üretim maliyeti = üretim giderleri + DBYM − DSYM → üretim giderleri = 600.000 − 90.000 + 70.000 = 580.000 ₺. Şekillendirme = %60 × 580.000 = 348.000 ₺ = DİG + GÜG → GÜG = 348.000 − 148.000 = **200.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0024': patch(
        'Bir üretim işletmesinin satışların maliyeti tablosundan aşağıdakilerden hangisi elde edilemez?',
        {
            'A': 'Dönemin direkt ilk madde ve malzeme gideri',
            'B': 'Dönem sonu yarı mamul stoklarının tutarı',
            'C': 'Satılan ticari malların maliyeti',
            'D': 'Dönemde katlanılan genel yönetim giderlerinin tutarı',
            'E': 'Dönemde üretilen mamullerin maliyeti',
        },
        'D',
        "Satışların maliyeti tablosu DİMM, direkt işçilik ve GÜG'den başlayıp yarı mamul ve mamul stok değişimleriyle satılan mamuller maliyetine, ticari işletmelerde satılan ticari mallar maliyetine ulaşır. Genel yönetim giderleri faaliyet gideridir; bu tabloda yer almaz, gelir tablosunda faaliyet giderleri arasında gösterilir.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0025': patch(
        "Ağırlıklı ortalama maliyet yöntemini kullanan bir işletme mamul başına 25 kg hammadde kullanarak ürettiği 1.200 adet mamulün 2/3'ünü satmıştır. Dönem sonu mamul stoklarına düşen hammadde maliyeti 45.000 ₺'dir. Tek hammaddeyle tek çeşit mamul üreten işletmede hammaddenin kg maliyeti kaç ₺'dir?",
        {
            'A': '1,50',
            'B': '4,50',
            'C': '112,50',
            'D': '2,25',
            'E': '9',
        },
        'B',
        'Stokta kalan mamul = 1.200 × 1/3 = 400 adet; bunlardaki hammadde 400 × 25 = 10.000 kg. Kg maliyeti = 45.000 ÷ 10.000 = **4,50 ₺**.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 3
    '0026': patch(
        "Dönem başında yarı mamul ve mamul stoku, dönem sonunda yarı mamul stoku bulunmayan bir işletmede kg başına hammadde maliyeti 250 ₺'dir. Direkt işçilik giderleri 12.000 ₺, genel üretim giderleri 24.000 ₺, satılan mamuller maliyeti 90.000 ₺'dir. Dönemde tamamlanan 60 adet mamulün 3/4'ü satıldığına göre üretimde kaç kg hammadde kullanılmıştır?",
        {
            'A': '216',
            'B': '336',
            'C': '480',
            'D': '144',
            'E': '252',
        },
        'B',
        "Satılan 3/4'ün maliyeti 90.000 ₺ → üretilen mamul maliyeti 90.000 ÷ 3/4 = 120.000 ₺. DİMM = 120.000 − 12.000 − 24.000 = 84.000 ₺ → 84.000 ÷ 250 = **336 kg**.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0027': patch(
        "Bir işletmenin üretim dönemine ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 54.000 |\n| Direkt işçilik giderleri | 20.000 |\n| Dönem başı yarı mamul | 16.000 |\n| Endirekt işçilik giderleri | 26.000 |\n| Fabrika binası sigortası | 8.000 |\n| Fabrika binası amortismanı | 6.000 |\n| Dönem sonu yarı mamul | 10.000 |\n\nDönem başında 100 birim mamul stoku (10.000 ₺) vardır. Dönemde 1.000 birim üretilmiş, dönem sonunda 400 birim mamul kalmıştır. FIFO yöntemine göre satılan mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '48.000',
            'B': '58.000',
            'C': '72.000',
            'D': '84.000',
            'E': '82.000',
        },
        'E',
        "Endirekt işçilik, fabrika sigortası ve amortisman GÜG'dür. Üretim giderleri = 114.000 ₺; üretilen = 114.000 + 16.000 − 10.000 = 120.000 ₺ → birim 120 ₺. Satılan = 100 + 1.000 − 400 = 700 birim; FIFO: 10.000 + 600 × 120 = **82.000 ₺**.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0028': patch(
        "Dönem başı ve sonunda yarı mamul ile mamul stoku bulunmayan bir işletme dönemde 1.000 adet mamul üretmiştir. Döneme ait giderler şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 80.000 |\n| Direkt işçilik giderleri | 60.000 |\n| Endirekt malzeme | 12.000 |\n| Endirekt işçilik | 18.000 |\n| Fabrika binası kirası | 20.000 |\n| Makine amortismanı | 15.000 |\n| Fabrika enerji gideri | 9.000 |\n| Satış personeli ücreti | 14.000 |\n| Yönetim binası amortismanı | 8.000 |\n| Kredi faizi | 6.000 |\n\nBuna göre birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '214',
            'B': '228',
            'C': '242',
            'D': '140',
            'E': '236',
        },
        'A',
        'Üretim maliyeti = DİMM + DİG + GÜG. GÜG: endirekt malzeme, endirekt işçilik, fabrika kirası, makine amortismanı ve fabrika enerjisi = 74.000 ₺. Toplam 214.000 ₺ → birim **214 ₺**. Satış personeli ücreti pazarlama, yönetim binası amortismanı genel yönetim, faiz finansman gideridir.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0029': patch(
        'Bir üretim işletmesinin aynı üretim için farklı maliyet yöntemlerine göre hesaplanan üretim maliyetleri şöyledir:\n\n| Yöntem | Maliyet (₺) |\n|---|---|\n| Asal maliyet | 210.000 |\n| Değişken maliyet | 250.000 |\n| Normal maliyet | 280.000 |\n| Tam maliyet | 290.000 |\n\nBuna göre işletmenin dönemdeki kapasite kullanım oranı yüzde kaçtır?',
        {
            'A': '%86',
            'B': '%75',
            'C': '%97',
            'D': '%25',
            'E': '%72',
        },
        'B',
        "Tam − değişken = sabit GÜG = 40.000 ₺. Normal − değişken = kapasite oranında yüklenen sabit GÜG = 30.000 ₺. Oran = 30.000 ÷ 40.000 = **%75**. Değişken GÜG ise 40.000 ₺'dir.",
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0030': patch(
        "Aylık üretim kapasitesi 25.000 birim olan bir işletmede nisan ayında 15.000 birim mamul üretilmiş; DİMM 360.000 ₺, direkt işçilik 210.000 ₺ ve değişken GÜG 90.000 ₺ gerçekleşmiştir. Sabit GÜG de eklendiğinde normal maliyet sistemine göre birim maliyet 56 ₺ hesaplanmıştır. Buna göre tam maliyet sistemine göre birim maliyet kaç ₺'dir?",
        {
            'A': '64',
            'B': '38,40',
            'C': '60',
            'D': '56',
            'E': '44',
        },
        'A',
        'Normal maliyet = 56 × 15.000 = 840.000 ₺; değişken kısım 660.000 ₺ → yüklenen sabit GÜG 180.000 ₺ = sabit GÜG × %60 → sabit GÜG = 300.000 ₺. Tam maliyet = 660.000 + 300.000 = 960.000 ₺ → birim **64 ₺**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0031': patch(
        "Normal maliyet sistemini uygulayan bir işletmenin dönemlik sabit GÜG'ü 180.000 ₺, üretim kapasitesi 20.000 birimdir. Dönemde 15.000 birim üretildiğine göre mamul maliyetine yüklenmeyip dönem gideri olarak kaydedilecek kullanılmayan kapasite maliyeti kaç ₺'dir?",
        {
            'A': '36.000',
            'B': '180.000',
            'C': '60.000',
            'D': '135.000',
            'E': '45.000',
        },
        'E',
        'Kapasite kullanım oranı 15.000 ÷ 20.000 = %75. Mamule 135.000 ₺ yüklenir; kalan %25 = **45.000 ₺** kullanılmayan kapasite maliyetidir ve dönem gideri yazılır.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0032': patch(
        "Tam maliyet yöntemini benimseyen ve %75 kapasiteyle 400 ton mamul üreten bir işletmede birim DİMM gideri 120 ₺, birim şekillendirme gideri 80 ₺'dir. Değişken maliyet yöntemi benimsenseydi tamamlanan mamullerin maliyeti 70.000 ₺ olacaktı. Dönem başı ve sonunda stok yoktur. Normal maliyet yöntemine göre birim maliyet kaç ₺'dir?",
        {
            'A': '175',
            'B': '181,25',
            'C': '193,75',
            'D': '200',
            'E': '187,50',
        },
        'C',
        'Tam maliyet = 400 × (120 + 80) = 80.000 ₺. Sabit GÜG = tam − değişken = 10.000 ₺. Normal maliyet = 70.000 + 10.000 × %75 = 77.500 ₺ → birim **193,75 ₺**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0033': patch(
        "Normal maliyet yöntemini kullanan bir işletmede %75 kapasiteyle 12.000 adet mamul üretilmiştir. Döneme ait bilgiler şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 450.000 |\n| Direkt işçilik giderleri | 330.000 |\n| Değişken GÜG | 180.000 |\n| Normal maliyete göre toplam maliyet | 1.140.000 |\n\nBuna göre tam maliyet yöntemine göre birim maliyet kaç ₺'dir?",
        {
            'A': '110',
            'B': '95',
            'C': '100',
            'D': '65',
            'E': '80',
        },
        'C',
        'Normal maliyete giren sabit GÜG = 1.140.000 − 960.000 = 180.000 ₺ = sabit GÜG × %75 → sabit GÜG = 240.000 ₺. Tam maliyet = 960.000 + 240.000 = 1.200.000 ₺ → birim **100 ₺**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0034': patch(
        'Beyaz eşya üreten ve giderlerini 7/A seçeneğine göre izleyen bir fabrikada kesme, kaynak, boya ve montaj esas üretim gider yerleri bulunmaktadır. Buna göre aşağıdakilerden hangisi genel üretim giderlerinde muhasebeleştirilmesi gereken bir giderdir?',
        {
            'A': 'Boya bölümünde kullanılan fırça ve zımpara kâğıtlarının bedeli',
            'B': 'Kesme bölümünde sac kesen işçilerin normal ücretleri',
            'C': 'Genel müdürlük binasının kira gideri',
            'D': 'Montaj hattında buzdolabına takılan kompresörlerin bedeli',
            'E': 'Bayilere ürün taşıyan kamyonların yakıt gideri',
        },
        'A',
        "Fırça ve zımpara gibi mamule izlenemeyen yardımcı malzemeler endirekt malzemedir, GÜG'e (730) yazılır. Kompresör DİMM (710), sac kesen işçinin ücreti direkt işçilik (720), bayiye taşıma pazarlama-satış (760), genel müdürlük kirası genel yönetim (770) gideridir.",
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 3
    '0035': patch(
        "Tek mamul üreten ve maliyet hesaplarını 7/A seçeneğine göre izleyen bir işletmede dönem sonu kapanış öncesi gider hesaplarının borç kalanları ve stok bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| 710 DİMM Giderleri | 400.000 |\n| 720 Direkt İşçilik Giderleri | 250.000 |\n| 730 Genel Üretim Giderleri | 150.000 |\n| 770 Genel Yönetim Giderleri | 90.000 |\n| Dönem başı yarı mamul | 50.000 |\n| Dönem sonu yarı mamul | 70.000 |\n| Dönem başı mamul | 30.000 |\n| Dönem sonu mamul | 20.000 |\n\nBuna göre dönem sonunda 620 Satılan Mamuller Maliyeti hesabına aktarılacak tutar kaç ₺'dir?",
        {
            'A': '810.000',
            'B': '880.000',
            'C': '780.000',
            'D': '770.000',
            'E': '790.000',
        },
        'E',
        "151'e aktarılan üretim giderleri 400.000 + 250.000 + 150.000 = 800.000 ₺; 152'ye aktarılan = 800.000 + 50.000 − 70.000 = 780.000 ₺; 620 = 780.000 + 30.000 − 20.000 = **790.000 ₺**. 770 faaliyet gideridir, 631'e aktarılır.",
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 2
    '0036': patch(
        "Bir üretim işletmesinin dönemlik ücret bordrosundan elde edilen bilgiler şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Üretici işçilerin normal ücretleri | 80.000 |\n| Üretici işçilerin makine arızasında bekleme ücreti | 6.000 |\n| Ustabaşı ücretleri | 12.000 |\n| Bakım işçilerinin ücretleri | 9.000 |\n| Genel kapasite yetersizliğinden doğan fazla mesai zammı | 5.000 |\n| Satış personelinin ücretleri | 15.000 |\n\nBuna göre genel üretim giderlerine yazılacak işçilik tutarı kaç ₺'dir?",
        {
            'A': '47.000',
            'B': '21.000',
            'C': '32.000',
            'D': '112.000',
            'E': '27.000',
        },
        'C',
        "Endirekt işçilik GÜG'dür: bekleme ücreti 6.000 + ustabaşı 12.000 + bakım işçileri 9.000 + genel nitelikli fazla mesai zammı 5.000 = **32.000 ₺**. Üretici işçilerin normal ücreti direkt işçilik (720), satış personelinin ücreti pazarlama gideridir (760).",
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 3
    '0037': patch(
        "Üretime sevk maliyetinin hesaplanmasında dönemsel (tartılı) ağırlıklı ortalama maliyet yöntemi uygulanan bir hammadde stokuna ilişkin bilgiler şöyledir:\n\n| Kalem | Miktar | Tutar (₺) |\n|---|---|---|\n| Dönem başı stok | 500 | 70.000 |\n| Dönem içi tüketim | 2.000 | 300.000 |\n| Dönem sonu stok | 500 | 75.000 |\n\nBuna göre dönem içi alışların birim maliyeti kaç ₺'dir?",
        {
            'A': '187,50',
            'B': '150',
            'C': '152,50',
            'D': '140',
            'E': '115',
        },
        'C',
        'Tartılı ortalamada tüketim ve dönem sonu stok aynı birim maliyetle (150 ₺) değerlenir. Satılabilir toplam = (2.000 + 500) × 150 = 375.000 ₺. Alış miktarı = 2.000 + 500 − 500 = 2.000; alış tutarı = 375.000 − 70.000 = 305.000 ₺ → birim **152,50 ₺**.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 3
    '0038': patch(
        "Stoklarını hareketli ortalama maliyet yöntemiyle değerleyen bir işletmede M malzemesinin stok kartında 5 Mart itibarıyla 200 adet, birim 50 ₺'den 10.000 ₺ kalan vardır. 18 Mart'ta 300 adet alış yapılmış fakat karta işlenmemiştir. 25 Mart'ta 250 adet malzeme üretime sevk edilmiş ve sevk maliyeti 14.000 ₺ olarak hesaplanmıştır. Buna göre 18 Mart alışının birim fiyatı kaç ₺'dir?",
        {
            'A': '60',
            'B': '50',
            'C': '56',
            'D': '70',
            'E': '64',
        },
        'A',
        'Sevk birim maliyeti 14.000 ÷ 250 = 56 ₺ yeni hareketli ortalamadır. Toplam değer = 500 × 56 = 28.000 ₺; alış tutarı = 28.000 − 10.000 = 18.000 ₺ → birim **60 ₺**.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 2
    '0039': patch(
        "A hammaddesinin stok kayıtlarını aralıklı (dönemsel) envanter yöntemine göre tutan ve tartılı ağırlıklı ortalama maliyet yöntemini uygulayan bir işletmenin ocak ayı hareketleri şöyledir:\n\n| Tarih | İşlem | Miktar (kg) |\n|---|---|---|\n| 1 Ocak | Dönem başı (20 ₺/kg) | 1.000 |\n| 10 Ocak | Alış (24 ₺/kg) | 3.000 |\n| 24 Ocak | Alış (26 ₺/kg) | 2.000 |\n| 31 Ocak | Sayım: kalan | 1.500 |\n\nBuna göre ocak ayında üretime verilen hammaddenin maliyeti kaç ₺'dir?",
        {
            'A': '105.000',
            'B': '36.000',
            'C': '112.000',
            'D': '117.000',
            'E': '108.000',
        },
        'E',
        'Satılabilir toplam: 20.000 + 72.000 + 52.000 = 144.000 ₺, 6.000 kg → tartılı ortalama 24 ₺/kg. Kullanılan = 6.000 − 1.500 = 4.500 kg × 24 = **108.000 ₺**. FIFO 105.000 ₺ verirdi.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 2
    '0040': patch(
        "Bir işletme kg'ı 30 ₺'den 2.000 kg hammadde satın almış, ayrıca 4.000 ₺ nakliye ve 2.000 ₺ taşıma sigortası ödemiştir. Alış bedeli üzerinden %20 indirilebilir KDV hesaplanmıştır. Buna göre hammaddenin kg maliyeti kaç ₺'dir?",
        {
            'A': '30',
            'B': '39',
            'C': '32',
            'D': '33',
            'E': '31',
        },
        'D',
        'Maliyet bedeli = alış bedeli 60.000 + nakliye 4.000 + sigorta 2.000 = 66.000 ₺ → kg başına **33 ₺**. İndirilebilir KDV (191) maliyete eklenmez.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 3
    '0041': patch(
        "Bir üretim işletmesinin şubat ve mart aylarına ait satışların maliyeti tablolarından bazı bilgiler şöyledir:\n\n| Kalem | Şubat (₺) | Mart (₺) |\n|---|---|---|\n| Üretim giderleri | 410.000 | 480.000 |\n| DBYM | 35.000 | ? |\n| DSYM | 50.000 | 70.000 |\n| DBM | 20.000 | ? |\n| DSM | 40.000 | 55.000 |\n\nDBYM/DSYM: dönem başı/sonu yarı mamul · DBM/DSM: dönem başı/sonu mamul. Buna göre mart ayında satılan mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '460.000',
            'B': '445.000',
            'C': '480.000',
            'D': '430.000',
            'E': '425.000',
        },
        'B',
        'Mart başı stoklar şubat sonu stoklarıdır: DBYM 50.000 ₺, DBM 40.000 ₺. Mart üretilen mamul maliyeti = 480.000 + 50.000 − 70.000 = 460.000 ₺; satılan mamuller maliyeti = 460.000 + 40.000 − 55.000 = **445.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0042': patch(
        "Dönem başında ve sonunda yarı mamulü, dönem başında mamulü bulunmayan bir işletmenin net satışları 240.000 ₺, brüt satış kârı 90.000 ₺'dir. Dönem sonu mamul stoku 30.000 ₺, direkt işçilik giderleri 45.000 ₺ ve genel üretim giderleri 35.000 ₺'dir. Buna göre direkt ilk madde ve malzeme giderleri kaç ₺'dir?",
        {
            'A': '145.000',
            'B': '40.000',
            'C': '70.000',
            'D': '100.000',
            'E': '190.000',
        },
        'D',
        'SMM = 240.000 − 90.000 = 150.000 ₺. DBM olmadığından üretilen mamul maliyeti = SMM + DSM = 180.000 ₺; yarı mamul olmadığından bu tutar üretim giderlerine eşittir. DİMM = 180.000 − 45.000 − 35.000 = **100.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0043': patch(
        "Bir üretim işletmesinde dönemde 2.500 birim mamulün üretimi tamamlanmış ve birim üretim maliyeti 120 ₺ olarak gerçekleşmiştir. Dönem başı yarı mamul maliyeti 30.000 ₺, dönem sonu yarı mamul maliyeti 80.000 ₺, direkt işçilik giderleri 140.000 ₺ ve genel üretim giderleri 160.000 ₺'dir. Buna göre işletmenin dönemde katlandığı üretim giderleri toplamı kaç ₺'dir?",
        {
            'A': '380.000',
            'B': '330.000',
            'C': '300.000',
            'D': '350.000',
            'E': '250.000',
        },
        'D',
        'Üretilen mamul maliyeti = 2.500 × 120 = 300.000 ₺. Üretilen = üretim giderleri + DBYM − DSYM → üretim giderleri = 300.000 − 30.000 + 80.000 = **350.000 ₺** (DİMM payı 50.000 ₺).',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0044': patch(
        "Dönem başında 40 ton mamul stoku (36.000 ₺) bulunan bir işletmede dönemde 160 ton mamulün üretimi tamamlanmış ve 150 ton mamul satılmıştır. Stok değerlemesinde ilk giren ilk çıkar (FIFO) yöntemi kullanılmaktadır. Dönemin maliyet bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 40.000 |\n| Direkt işçilik giderleri | 30.000 |\n| Genel üretim giderleri | 60.000 |\n| Dönem başı yarı mamul | 5.000 |\n| Dönem sonu yarı mamul | 7.000 |\n\nBuna göre satılan mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '123.000',
            'B': '124.000',
            'C': '128.000',
            'D': '120.000',
            'E': '156.000',
        },
        'B',
        "Üretilen mamul maliyeti = 130.000 + 5.000 − 7.000 = 128.000 ₺ → ton başına 800 ₺. FIFO'da önce dönem başı stok satılır: 36.000 ₺ + 110 ton × 800 = 88.000 ₺ → **124.000 ₺**. Ağırlıklı ortalama 123.000 ₺ verirdi.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 2
    '0045': patch(
        "Tek tip mamul üreten bir işletmede dönemde üretilen 12.000 kg mamulün 9.000 kg'ı satılmıştır; dönem başında mamul, dönem sonunda yarı mamul stoku yoktur. Direkt üretim maliyetleri (%25'i direkt işçilik) 24.000 ₺, dönem başı yarı mamul 3.000 ₺ ve endirekt üretim maliyetleri 9.000 ₺'dir. Tam maliyet yöntemine göre satılan mamullerin maliyeti kaç ₺'dir?",
        {
            'A': '27.000',
            'B': '36.000',
            'C': '24.750',
            'D': '9.000',
            'E': '18.000',
        },
        'A',
        'Üretilen mamul maliyeti = 24.000 + 3.000 + 9.000 = 36.000 ₺ (tam maliyette endirekt giderler de mamule girer; %25 bilgisi sonucu etkilemez). Kg başına 3 ₺; satılan 9.000 kg → **27.000 ₺**.',
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0046': patch(
        "Bir işletmede dönemin üretim giderleri 300.000 ₺; dönem başı yarı mamul 40.000 ₺, dönem sonu yarı mamul 25.000 ₺; dönem başı mamul 35.000 ₺, dönem sonu mamul 50.000 ₺'dir. Buna göre aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üretilen mamuller maliyeti 315.000 ₺'dir.\n\nII. Satılan mamuller maliyeti, dönemin üretim giderlerinden 15.000 ₺ fazladır.\n\nIII. Yarı mamul stokundaki azalış, üretilen mamuller maliyetini üretim giderlerinin üzerine çıkarmıştır.",
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'D',
        "**I doğrudur:** 300.000 + 40.000 − 25.000 = 315.000 ₺. **II yanlıştır:** SMM = 315.000 + 35.000 − 50.000 = 300.000 ₺, üretim giderlerine eşittir. **III doğrudur:** yarı mamul 40.000'den 25.000'e azalmış, fark (15.000 ₺) üretilen mamuller maliyetine eklenmiştir.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0047': patch(
        "Bir işletmenin ocak ayı ilk madde ve malzeme alışları 60.000 ₺ olup bunun 15.000 ₺'si yardımcı malzeme ve işletme malzemesidir. Stok bilgileri şöyledir:\n\n| Hesap | 1 Ocak (₺) | 31 Ocak (₺) |\n|---|---|---|\n| 150.01 DİMM | 14.000 | 9.000 |\n| 150.02 Yardımcı malzeme | 3.000 | 2.000 |\n| 150.03 İşletme malzemesi | 1.000 | 1.500 |\n\nBuna göre ocak ayı direkt ilk madde ve malzeme gideri kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '65.500',
            'C': '54.000',
            'D': '59.000',
            'E': '45.000',
        },
        'A',
        "Yalnız direkt malzeme hesabı izlenir: DİMM alışı 60.000 − 15.000 = 45.000 ₺. DİMM gideri = 14.000 + 45.000 − 9.000 = **50.000 ₺**. Yardımcı ve işletme malzemesi kullanımı GÜG'e yazılır.",
        'Maliyet muhasebesi - üretim maliyeti ve satışların maliyeti tablosu',
    ),
    # düzey 3
    '0048': patch(
        "Bir üretim işletmesinin döneme ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 420.000 |\n| Direkt işçilik giderleri | 180.000 |\n| Değişken GÜG | 90.000 |\n| Sabit GÜG | 240.000 |\n| Finansman giderleri | 30.000 |\n\nÜretim kapasitesi 60.000 adet olup dönemde 45.000 adet üretilmiştir. Buna göre tam maliyet ve normal maliyet yöntemlerine göre hesaplanan toplam üretim maliyetleri arasındaki fark kaç ₺'dir?",
        {
            'A': '80.000',
            'B': '240.000',
            'C': '180.000',
            'D': '60.000',
            'E': '90.000',
        },
        'D',
        "Kapasite kullanım oranı 45.000 ÷ 60.000 = %75. Tam maliyet sabit GÜG'ün tamamını, normal maliyet %75'ini yükler. Fark = kullanılmayan kapasitenin sabit GÜG'ü = 240.000 × %25 = **60.000 ₺**. Finansman gideri iki yöntemde de üretim maliyetine girmez.",
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0049': patch(
        "Değişken maliyet sisteminin uygulandığı bir işletmede dönemde 200 ton mamul üretilmiştir. Genel üretim giderlerinin değişken kısmı toplam GÜG'ün 1/4'ü kadardır. Dönemin giderleri: DİMM 310.000 ₺, direkt işçilik 250.000 ₺, genel üretim 360.000 ₺. Buna göre bir kg mamulün maliyeti kaç ₺'dir?",
        {
            'A': '2,80',
            'B': '3.250',
            'C': '3,25',
            'D': '4,15',
            'E': '4,60',
        },
        'C',
        'Değişken maliyet = DİMM + DİG + değişken GÜG = 310.000 + 250.000 + (360.000 × 1/4 = 90.000) = 650.000 ₺. 200 ton = 200.000 kg → kg başına **3,25 ₺** (ton başına 3.250 ₺).',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0050': patch(
        "Aylık kapasitesi 12.000 birim olan bir işletme dönemde 8.000 birim mamul üretmiştir. Değişken maliyetleme yöntemini kullanan işletmede birim maliyet 52 ₺'dir. Dönemin giderleri: DİMM 180.000 ₺, direkt işçilik 140.000 ₺, değişken genel yönetim giderleri 30.000 ₺ ve değişken genel üretim giderleri (?). Buna göre değişken genel üretim giderleri kaç ₺'dir?",
        {
            'A': '416.000',
            'B': '126.000',
            'C': '96.000',
            'D': '320.000',
            'E': '66.000',
        },
        'C',
        'Değişken üretim maliyeti = 52 × 8.000 = 416.000 ₺ = DİMM + DİG + değişken GÜG. Değişken GÜG = 416.000 − 180.000 − 140.000 = **96.000 ₺**. Değişken genel yönetim gideri dönem gideridir, mamul maliyetine girmez.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0051': patch(
        'Tam maliyetleme yöntemini kullanan bir işletmenin aylık kapasitesi 10.000 birimdir. İşletme mayıs ayında 5.000 birim üretmiş ve birim üretim maliyetini 120 ₺ olarak belirlemiştir. Döneme ait bazı giderler: değişken GÜG 80.000 ₺, DİMM 250.000 ₺, sabit genel yönetim giderleri 60.000 ₺, direkt işçilik 170.000 ₺. İşletme normal maliyet yöntemini kullansaydı birim üretim maliyeti kaç ₺ olurdu?',
        {
            'A': '120',
            'B': '116',
            'C': '132',
            'D': '100',
            'E': '110',
        },
        'E',
        'Tam maliyet = 120 × 5.000 = 600.000 ₺; değişken kısım 500.000 ₺ → sabit GÜG 100.000 ₺ (genel yönetim gideri mamul maliyetine girmez). Kapasite %50 kullanıldığından normal maliyet = 500.000 + 50.000 = 550.000 ₺ → birim **110 ₺**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletmede DİMM 200.000 ₺, direkt işçilik 150.000 ₺, değişken GÜG 50.000 ₺ ve sabit GÜG 100.000 ₺'dir. Kapasite 10.000 birim olup 8.000 birim üretilmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Normal maliyete göre birim maliyet 62,50 ₺'dir.",
            'B': "Kullanılmayan kapasite maliyeti 20.000 ₺'dir.",
            'C': "Değişken maliyete göre birim maliyet 50 ₺'dir.",
            'D': "Tam maliyete göre toplam üretim maliyeti 500.000 ₺'dir.",
            'E': "Asal maliyet 350.000 ₺'dir.",
        },
        'A',
        "Normal maliyet = 400.000 + 100.000 × %80 = 480.000 ₺ → birim 60 ₺'dir; 62,50 ₺ tam maliyetin birim tutarıdır. Diğerleri doğrudur: değişken 400.000 ÷ 8.000 = 50 ₺; kullanılmayan kapasite 100.000 × %20 = 20.000 ₺; asal 350.000 ₺; tam 500.000 ₺.",
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 3
    '0053': patch(
        "Değişken maliyetleme sistemini kullanan bir işletmenin döneme ait verileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| DİMM giderleri | 120.000 |\n| Direkt işçilik giderleri | 60.000 |\n| Değişken GÜG | 60.000 |\n| Sabit GÜG | 150.000 |\n\nNormal kapasite 5.000 birimdir. Dönemde 3.600 birim tamamlanmış, 800 birim bütün maliyet unsurları açısından %50 tamamlanmış yarı mamul olarak kalmıştır. Buna göre dönem sonu yarı mamul stokunun değeri kaç ₺'dir?",
        {
            'A': '36.000',
            'B': '39.000',
            'C': '48.000',
            'D': '24.000',
            'E': '216.000',
        },
        'D',
        'Eşdeğer üretim = 3.600 + 800 × %50 = 4.000 birim. Değişken maliyet = 240.000 ₺ → birim 60 ₺ (sabit GÜG dönem gideridir). DSYM = 400 eşdeğer × 60 = **24.000 ₺**.',
        'Maliyet muhasebesi - maliyet sistemleri (tam, değişken, normal maliyet)',
    ),
    # düzey 2
    '0054': patch(
        'Daire üretip satan ve maliyetlerini daire başına hesaplayan bir inşaat işletmesinde aşağıdakilerden hangisi endirekt üretim gideri olarak değerlendirilmez?',
        {
            'A': 'Şantiyenin elektrik ve su gideri',
            'B': 'Şantiyede kullanılan iş makinelerinin amortismanı',
            'C': 'Dairelerin duvarlarında kullanılan tuğla ve çimentonun bedeli',
            'D': 'Birden çok daireyi yöneten şantiye şefinin ücreti',
            'E': 'Şantiye bekçisinin ücreti',
        },
        'C',
        'Tuğla ve çimento doğrudan dairelere izlenebildiğinden direkt ilk madde ve malzemedir. Bekçi, iş makinesi amortismanı, şantiye enerjisi ve şantiye şefinin ücreti birden çok daireye ortak olduğundan endirekt üretim gideridir.',
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 2
    '0055': patch(
        'İşçilik giderlerinin sınıflandırılmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Esas üretim gider yerlerinde yalnız malzeme taşıma işi yapan işçilerin ücreti direkt işçiliktir.\n\nII. Yemekhane, bakım-onarım gibi hizmet bölümlerinde çalışanların ücreti endirekt işçiliktir.\n\nIII. Genel kapasite yetersizliği nedeniyle sürekli yapılan fazla mesai zammı, zam ödenen işçinin o gün çalıştığı işe direkt işçilik olarak yüklenir.',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        "**I yanlıştır:** taşıma işi mamul üzerinde doğrudan çalışma değildir, endirekt işçiliktir. **II doğrudur.** **III yanlıştır:** genel kapasite yetersizliğinden doğan fazla mesai zammı belirli bir işe özgü değildir, GÜG'e yazılır; yalnız belirli bir müşterinin isteğinden doğan zam o işe yüklenir. Doğru cevap **Yalnız II**.",
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 3
    '0056': patch(
        "GÜG'ü tahmini yükleme oranıyla mamullere yükleyen bir işletme dönem sonunda aşağıdaki kaydı yapmıştır:\n\n| Hesap | Borç (₺) | Alacak (₺) |\n|---|---|---|\n| 731 GÜG Yansıtma | 600.000 |  |\n| 620 Satılan Mamuller Maliyeti | 72.000 |  |\n| 152 Mamuller | 18.000 |  |\n| 151 Yarı Mamuller – Üretim | 10.000 |  |\n| 730 Genel Üretim Giderleri |  | 700.000 |\n\nBuna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Fiili GÜG 600.000 ₺ olup mamullere 100.000 ₺ fazla yükleme yapılmıştır.',
            'B': "Yükleme farkının %72'si 152 Mamuller hesabına aktarılmıştır.",
            'C': 'Fiili GÜG 700.000 ₺ olup mamullere 100.000 ₺ eksik yükleme yapılmıştır.',
            'D': 'Mamullere yüklenen GÜG 700.000 ₺ olup 100.000 ₺ fazla yükleme yapılmıştır.',
            'E': '151 Yarı Mamuller – Üretim hesabı 10.000 ₺ alacaklandırılarak azaltılmıştır.',
        },
        'C',
        "730 fiili GÜG'ü taşır: 700.000 ₺. 731 yüklenen (tahmini) GÜG'ü taşır: 600.000 ₺. Fiili yüklenenden 100.000 ₺ fazla olduğundan eksik yükleme vardır; fark 620 (72.000), 152 (18.000) ve 151'e (10.000) **borç** kaydıyla dağıtılmış, bu hesapların maliyeti artırılmıştır.",
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 2
    '0057': patch(
        'Tam maliyet sistemini kullanan bir üretim işletmesinde aşağıdaki giderlerden hangisi mamul maliyetine girmeyip doğrudan dönem gideri olarak gelir tablosuna aktarılır?',
        {
            'A': 'Satış mağazasının kira gideri',
            'B': 'Ustabaşının ücreti',
            'C': 'Fabrikada kullanılan işletme malzemesi',
            'D': 'Üretim makinelerinin amortismanı',
            'E': 'Fabrika binasının kira gideri',
        },
        'A',
        'Tam maliyet sisteminde bütün üretim giderleri (fabrika kirası, makine amortismanı, ustabaşı ücreti, işletme malzemesi) mamul maliyetine girer. Satış mağazasının kirası pazarlama, satış ve dağıtım gideridir; dönem gideri olarak gelir tablosuna aktarılır.',
        'Maliyet muhasebesi - giderlerin sınıflandırılması ve 7/A hesap akışı',
    ),
    # düzey 3
    '0058': patch(
        "Üretime sevk maliyetinde FIFO yöntemi uygulanan bir işletmenin K hammaddesine ait bilgiler şöyledir:\n\n| Kalem | Miktar | Tutar (₺) |\n|---|---|---|\n| Dönem başı stok | 6.000 | 720.000 |\n| Dönem içi tüketim | 25.000 | 3.380.000 |\n| Dönem sonu stok | 5.000 | 700.000 |\n\nDönem içinde tek fiyattan alış yapıldığına göre alışların birim maliyeti kaç ₺'dir?",
        {
            'A': '136',
            'B': '145',
            'C': '135,20',
            'D': '140',
            'E': '120',
        },
        'D',
        "FIFO'da tüketim önce dönem başı stoktan yapılır: 6.000 × 120 = 720.000 ₺. Kalan 19.000 birim alışlardan: (3.380.000 − 720.000) ÷ 19.000 = **140 ₺**. Dönem sonu stok da bu fiyatla değerlenmiştir (5000 × 140).",
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 2
    '0059': patch(
        "Hareketli ortalama maliyet yöntemini kullanan bir işletmenin B malzemesine ait hareketler şöyledir:\n\n| Sıra | İşlem | Miktar |\n|---|---|---|\n| 1 | Dönem başı (40 ₺) | 100 |\n| 2 | Alış (44 ₺) | 300 |\n| 3 | Üretime sevk | 200 |\n| 4 | Alış (50 ₺) | 200 |\n| 5 | Üretime sevk | 250 |\n\nBuna göre dönem sonu malzeme stokunun değeri kaç ₺'dir?",
        {
            'A': '6.600',
            'B': '6.450',
            'C': '6.975',
            'D': '20.225',
            'E': '7.500',
        },
        'C',
        "İlk alıştan sonra ortalama (4.000 + 13.200) ÷ 400 = 43 ₺; 200 birim sevk edilince 200 × 43 = 8.600 ₺ kalır. İkinci alışla (8.600 + 10.000) ÷ 400 = 46,50 ₺. 250 birim sevk sonrası kalan 150 × 46,50 = **6.975 ₺**. FIFO'da kalan stok son alış fiyatından 7.500 ₺ olurdu.",
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
    ),
    # düzey 3
    '0060': patch(
        "Bir işletmenin dönem başında birim maliyeti 10 ₺ olan 500 kg hammaddesi vardır. Dönemde kg'ı 12 ₺'den 1.500 kg alış yapılmış ve 1.200 kg üretime sevk edilmiştir. İşletme FIFO yerine dönemsel ağırlıklı ortalama yöntemini kullansaydı üretime sevk edilen hammaddenin maliyeti nasıl değişirdi?",
        {
            'A': '1.000 ₺ artardı',
            'B': 'Değişmezdi',
            'C': '400 ₺ azalırdı',
            'D': '400 ₺ artardı',
            'E': '600 ₺ artardı',
        },
        'D',
        'FIFO: 500 × 10 + 700 × 12 = 13.400 ₺. Ağırlıklı ortalama: (5.000 + 18.000) ÷ 2.000 = 11,50 ₺ × 1.200 = 13.800 ₺. Maliyet **400 ₺ artar**; fiyatlar yükselirken FIFO en ucuz stoku önce tüketir.',
        'Maliyet muhasebesi - ilk madde ve malzeme stok değerlemesi',
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
    print(f"1 paket / {len(PATCHES)} soru ('Uretim Maliyeti Tablosu ve Maliyet Sistemleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
