#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gelir Tablosu Hesaplari — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. 49 soru korundu; 11 'hangi hesapta izlenir' ezberi cikarildi. Yerine gercek sinav kalibinda 11 soru: tam gelir tablosundan olagan kar, vergili donem net kari, SMM'den faaliyet kari, KDV dahil tutarlardan net satis, brut kar oranindan faaliyet kari, 610/611'in 690'a kapanis kaydi, kar kademesi siniflandirmalari (64/65/67), olumsuz ve oncullu sorular. Kor ogrenci %20.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Tekduzen Hesap Plani 6 Gelir Tablosu Hesaplari, 690-692 · 1 Sira No'lu MSUGT (gelir tablosu ilkeleri)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/gelir_tablosu_hesaplari.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-gt-gen-"


def patch(stem, options, answer, solution, ref='Tekduzen Hesap Plani 6 Gelir Tablosu Hesaplari'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "'61 Satış İndirimleri (-)' grubu ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin satıcılara ve kredi kurumlarına olan kısa vadeli ticari borçlarını izleyen bir pasif grubudur.',
            'B': 'İşletmenin maddi duran varlıklarının maliyet ve birikmiş amortisman tutarlarını izleyen bir bilanço grubudur.',
            'C': 'Brüt satışları artıran ve yurt dışı satışlarla birlikte hasılata eklenen olağan bir gelir grubudur.',
            'D': 'Brüt satışlardan düşülen (satıştan iadeler, satış iskontoları vb.) negatif nitelikli hesapları içerir.',
            'E': 'Kullanılan kredilerin faizleri gibi borçlanma maliyetlerini kapsayan bir finansman gideri grubudur.',
        },
        'D',
        '**61 Satış İndirimleri (-)**; brüt satışlardan düşülen (610 Satıştan İadeler, 611 Satış İskontoları, 612 Diğer İndirimler) **negatif nitelikli** hesapları içerir. Net satışlara ulaşmak için brüt satışlardan indirilir.',
        "1 Sıra No'lu MSUGT - 61 Satış İndirimleri",
    ),
    # düzey 2
    '0002': patch(
        "Gelir tablosunda 'Brüt Satış Kârı (veya Zararı)' nasıl bulunur?",
        {
            'A': 'Net Satışlar + Satışların Maliyeti',
            'B': 'Brüt Satışlar − Faaliyet Giderleri',
            'C': 'Faaliyet Kârı − Finansman Giderleri',
            'D': 'Net Satışlar − Faaliyet Giderleri',
            'E': 'Net Satışlar − Satışların Maliyeti',
        },
        'E',
        '**Brüt Satış Kârı/Zararı = Net Satışlar − Satışların Maliyeti (62)**. Sonuç pozitifse brüt satış kârı, negatifse brüt satış zararıdır.',
        "1 Sıra No'lu MSUGT - Gelir Tablosu",
    ),
    # düzey 2
    '0003': patch(
        "Aşağıdaki hesaplardan hangisi '64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar' grubunda yer almaz?",
        {
            'A': '602 Diğer Gelirler',
            'B': '640 İştiraklerden Temettü Gelirleri',
            'C': '642 Faiz Gelirleri',
            'D': '643 Komisyon Gelirleri',
            'E': '645 Menkul Kıymet Satış Kârları',
        },
        'A',
        '640, 642, 643 ve 645 hesapları 64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar grubundadır. 602 Diğer Gelirler ise esas faaliyetle ilgili olup 60 Brüt Satışlar grubunda yer alır.',
        "1 Sıra No'lu MSUGT - 64 / 642",
    ),
    # düzey 3
    '0004': patch(
        'Aşağıdaki hesaplardan hangisi bir gelir tablosu (sonuç) hesabı değildir?',
        {
            'A': '621 Satılan Ticari Mallar Maliyeti (-)',
            'B': '642 Faiz Gelirleri',
            'C': '320 Satıcılar',
            'D': '632 Genel Yönetim Giderleri (-)',
            'E': '600 Yurt İçi Satışlar',
        },
        'C',
        '**320 Satıcılar** bir bilanço (pasif/borç) hesabıdır, gelir tablosu hesabı değildir. Diğerleri (600, 621, 632, 642) gelir tablosu (sonuç) hesaplarıdır.',
        "1 Sıra No'lu MSUGT - 6 grubu vs bilanço",
    ),
    # düzey 2
    '0005': patch(
        'İşletme, daha önce 100.000 ₺ + %20 KDV ile kredili sattığı mal için müşterisine 10.000 ₺ + %20 KDV tutarında satış iskontosu yapmıştır. İskonto tutarı müşterinin borcundan düşülmüştür.\n\nİskonto kaydı hangisidir?',
        {
            'A': '612 Diğer İndirimler 10.000 ₺ ve 191 İndirilecek KDV 2.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak',
            'B': '611 Satış İskontoları 10.000 ₺ ve 391 Hesaplanan KDV 2.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak',
            'C': '611 Satış İskontoları 10.000 ₺ borç / 120 Alıcılar 10.000 ₺ alacak; KDV için kayıt yapılmaz',
            'D': '611 Satış İskontoları 12.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak',
            'E': '120 Alıcılar 12.000 ₺ borç / 611 Satış İskontoları 10.000 ₺ ve 391 Hesaplanan KDV 2.000 ₺ alacak',
        },
        'B',
        'Satış iskontosu net satışları azaltan 611 hesaba borç yazılır. İskontoya isabet eden hesaplanan KDV de 391 hesabın borcuna alınır; müşteri borcu toplam **12.000 ₺** azaltılır.',
        "1 Sıra No'lu MSUGT - 120/391/611",
    ),
    # düzey 3
    '0006': patch(
        "Faaliyet kârı 160.000 ₺ olan işletmenin faiz gelirleri 25.000 ₺, kambiyo kârları 15.000 ₺, kambiyo zararları 20.000 ₺ ve finansman giderleri 30.000 ₺'dir. Başka olağan gelir veya gider yoktur.\n\nİşletmenin olağan kârı kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '130.000',
            'C': '140.000',
            'D': '120.000',
            'E': '150.000',
        },
        'E',
        "Olağan kâr = 160.000 + 25.000 + 15.000 − 20.000 − 30.000 = **150.000 ₺**'dir. 642 ve 646 olağan geliri; 656 ile finansman giderleri olağan sonucu azaltan kalemleri temsil eder.",
        "1 Sıra No'lu MSUGT - 642/646/656/66 hesap grubu",
    ),
    # düzey 2
    '0007': patch(
        'Gelir tablosu hesaplarının işleyişi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gelir hesapları (60, 64, 67) borç, gider hesapları (62, 63, 66) alacak kalanı verir ve dönem sonunda 590 Dönem Net Kârı hesabına aktarılarak topluca kapatılır.',
            'B': 'Gelir hesapları (60, 64, 67) alacak; gider/maliyet hesapları (62, 63, 65, 66, 68) borç çalışır ve dönem sonunda 690 Dönem Kârı veya Zararı hesabına aktarılır.',
            'C': 'Tüm gelir ve gider hesapları önce 391 Hesaplanan KDV hesabına, ardından 690 Dönem Kârı veya Zararı hesabına devredilerek kapatılır.',
            'D': 'Gelir ve gider hesapları dönem sonunda kapatılmayıp kalanlarıyla bilançoda gösterilir; sonuç ise 590 Dönem Net Kârı hesabında belirlenir.',
            'E': 'Gelir hesapları da gider hesapları da borç kalanı verir ve dönem sonunda doğrudan 692 Dönem Net Kârı veya Zararı hesabına aktarılır.',
        },
        'B',
        "**Gelir hesapları (60, 64, 67) alacak**; **gider/maliyet hesapları (62, 63, 65, 66, 68) borç** çalışır. Dönem sonunda hepsi **690 Dönem Kârı veya Zararı**'na aktarılarak sonuç bulunur.",
        "1 Sıra No'lu MSUGT - 6 grubu / 690",
    ),
    # düzey 2
    '0008': patch(
        'İşletme yıl içinde döviz cinsinden alacaklarının tahsilinde 40.000 ₺ kur farkı kârı, döviz cinsinden satıcı borcunun ödenmesinde ise 25.000 ₺ kur farkı zararı elde etmiştir.\n\nBu kambiyo kârları ve zararları gelir tablosunda hangi gruplarda izlenir?',
        {
            'A': 'Kambiyo kârları 645 Menkul Kıymet Satış Kârları, kambiyo zararları ise 655 Menkul Kıymet Satış Zararları grubunda izlenir.',
            'B': 'Kambiyo kârları 679 Diğer Olağandışı Gelir ve Kârlar (67), kambiyo zararları ise 689 Diğer Olağandışı Gider (68) grubunda izlenir.',
            'C': 'Her ikisi de 66 Finansman Giderleri grubunda; kambiyo kârları 660, kambiyo zararları 661 hesabında izlenir.',
            'D': 'Kambiyo kârları 646 (64 Diğer Faaliyetlerden Olağan Gelir), kambiyo zararları 656 (65 Diğer Faaliyetlerden Olağan Gider) grubunda',
            'E': 'Kambiyo kârları 642 Faiz Gelirleri, kambiyo zararları ise 657 Reeskont Faiz Giderleri hesabında izlenir.',
        },
        'D',
        '**Kambiyo kârları → 646 Kambiyo Kârları (64 grubu, olağan gelir)**; **kambiyo zararları → 656 Kambiyo Zararları (65 grubu, olağan gider)**.',
        "1 Sıra No'lu MSUGT - 646 / 656",
    ),
    # düzey 2
    '0009': patch(
        'Esas faaliyet konusu taşınmaz kiralama olmayan işletmenin, başka bir işletmeye kiraya verdiği deposuna ait 18.000 ₺ tutarındaki cari dönem kira geliri dönem sonunda tahakkuk etmiş; bedel henüz tahsil edilmemiştir.\n\nBu tahakkukun muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '181 Gelir Tahakkukları hesabı 18.000 ₺ borçlandırılır',
            'B': "Kira geliri 600 Yurt İçi Satışlar'a alacak yazılır",
            'C': 'Gelir 649 Diğer Olağan Gelir ve Kârlar hesabına yazılır',
            'D': 'Tahakkuk kaydı dönemsellik kavramının gereğidir',
            'E': 'Kira tahsil edildiğinde 181 hesabı alacaklandırılır',
        },
        'B',
        "Cari döneme ait olup tahsil edilmemiş gelir 181 Gelir Tahakkukları hesabına borç kaydedilir. Kira, esas faaliyet dışı olduğundan 600'e değil 649 Diğer Olağan Gelir ve Kârlar hesabına alacak yazılır. Tahsilde 181 kapatılır.",
        "1 Sıra No'lu MSUGT - 181/649",
    ),
    # düzey 2
    '0010': patch(
        "Satışların maliyeti hesaplarının (62 grubu) gelir tablosunda '(-)' negatif nitelikli olarak gösterilmesinin nedeni aşağıdakilerden hangisidir?",
        {
            'A': 'Net satışlardan düşülerek brüt satış kârına ulaşılmasını sağlayan bir gider/maliyet unsuru olması',
            'B': 'İşletmenin satıcılara olan kısa vadeli ticari borcunu gösteren bir pasif (yabancı kaynak) kalemi olması',
            'C': 'Bilançoda özkaynaklar içinde gösterilen bir dönem net kârı kalemi olması',
            'D': 'Net satışlara eklenerek brüt satış kârını artıran bir hasılat unsuru olması',
            'E': 'İşletmenin devreden stoklarını temsil eden bir dönen varlık kalemi olması',
        },
        'A',
        "**62 Satışların Maliyeti (-)**, satılan malların/hizmetlerin maliyetini gösteren bir gider unsurudur; net satışlardan **düşülerek** brüt satış kârına ulaşılmasını sağladığı için '(-)' negatif nitelikli gösterilir.",
        "1 Sıra No'lu MSUGT - 62",
    ),
    # düzey 3
    '0011': patch(
        'Dönem sonu aktarmalarından sonra 690 Dönem Kârı veya Zararı hesabı 260.000 ₺ alacak kalanı, 691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları hesabı ise 65.000 ₺ borç kalanı vermektedir.\n\nHer iki hesap 692 hesaba devredildiğinde 692 Dönem Net Kârı veya Zararı hesabı hangi kalanı verir?',
        {
            'A': '65.000 ₺ borç kalanı',
            'B': '260.000 ₺ alacak kalanı',
            'C': '325.000 ₺ alacak kalanı',
            'D': '195.000 ₺ alacak kalanı',
            'E': '195.000 ₺ borç kalanı',
        },
        'D',
        '690 hesabın alacak kalanı vergi öncesi kârı, 691 hesabın borç kalanı vergi ve yasal yükümlülük karşılığını gösterir. Net tutar 260.000 − 65.000 = **195.000 ₺** olup 692 hesap alacak kalanı verir.',
        "1 Sıra No'lu MSUGT - 690/691/692",
    ),
    # düzey 3
    '0012': patch(
        "İşletme 1 Ekim 2025'te açtığı bir yıl vadeli mevduatın 31 Aralık 2025'e kadar işlemiş faizini 181 Gelir Tahakkukları hesabına kaydetmiştir. Mevduat 30 Nisan 2026'da vadesinden önce kapatılmış ve banka faiz ödememiştir.\n\n2025'te kaydedilen faiz tahakkukunun iptalinde yapılacak kayıt hangisidir?",
        {
            'A': '681 Önceki Dönem Gider ve Zararları borç / 181 Gelir Tahakkukları alacak',
            'B': '642 Faiz Gelirleri borç / 181 Gelir Tahakkukları alacak',
            'C': '681 Önceki Dönem Gider ve Zararları borç / 642 Faiz Gelirleri alacak',
            'D': '181 Gelir Tahakkukları borç / 681 Önceki Dönem Gider ve Zararları alacak',
            'E': '671 Önceki Dönem Gelir ve Kârlar borç / 181 Gelir Tahakkukları alacak',
        },
        'A',
        "2025'te varlık olarak kaydedilen faiz alacağı erken kapama nedeniyle ortadan kalkmıştır. Önceki dönemde kayda alınan bu tutar 2026'da **681 Önceki Dönem Gider ve Zararları borç / 181 Gelir Tahakkukları alacak** kaydıyla iptal edilir.",
        "1 Sıra No'lu MSUGT - 181/681; 18 Temmuz 2026 SGS soru örüntüsü",
    ),
    # düzey 2
    '0013': patch(
        "Ticaret işletmesinde 'Satılan Ticari Mallar Maliyeti (621)' aşağıdaki hangi yolla hesaplanır?",
        {
            'A': 'Dönem Başı Mal Mevcudu + Dönem İçi Alışlar − Dönem Sonu Mal Mevcudu',
            'B': 'Dönem Sonu Mal Mevcudu − Dönem İçi Alışlar',
            'C': 'Net Satışlar − Faaliyet Giderleri',
            'D': 'Dönem Başı Mal Mevcudu + Dönem İçi Alışlar + Dönem Sonu Mal Mevcudu',
            'E': 'Dönem İçi Alışlar − Dönem Başı Mal Mevcudu',
        },
        'A',
        'Satılan Ticari Mallar Maliyeti = **Dönem Başı Mal Mevcudu + Dönem İçi Alışlar − Dönem Sonu Mal Mevcudu**. Örn: 80.000 + 400.000 − 90.000 = 390.000 ₺.',
        "1 Sıra No'lu MSUGT - 621; SMM",
    ),
    # düzey 3
    '0014': patch(
        "Dönem sonu gelir ve gider aktarmaları tamamlandığında 690 Dönem Kârı veya Zararı hesabı 300.000 ₺ alacak kalanı vermiştir. Hesaplanan dönem kârı vergi ve diğer yasal yükümlülük karşılığı 75.000 ₺'dir.\n\nKarşılık kaydından ve 690 ile 691 hesaplarının devrinden sonra 692 hesabın durumu hangisidir?",
        {
            'A': '300.000 ₺ alacak kalanı verir.',
            'B': '75.000 ₺ borç kalanı verir.',
            'C': '375.000 ₺ alacak kalanı verir.',
            'D': '225.000 ₺ alacak kalanı verir.',
            'E': '225.000 ₺ borç kalanı verir.',
        },
        'D',
        "Vergi karşılığı 691 borç / 370 alacak kaydedilir. 690'daki 300.000 ₺ vergi öncesi kâr ile 691'deki 75.000 ₺ karşılık 692 hesaba devredildiğinde net kâr 300.000 − 75.000 = **225.000 ₺** olur ve 692 hesap alacak kalanı verir.",
        "1 Sıra No'lu MSUGT - 370/690/691/692",
    ),
    # düzey 2
    '0015': patch(
        'İşletme, defter değeri 600.000 ₺ olan kısa vadeli yabancı para kredisini 630.000 ₺ karşılığında kapatmış ve ayrıca 25.000 ₺ faiz ödemiştir. Faizin tamamı cari döneme aittir.\n\nGelir tablosuna yansıtılacak tutarlar hangi seçenekte doğru verilmiştir?',
        {
            'A': '660 Kısa Vadeli Borçlanma Giderleri 55.000 ₺; kambiyo sonucu oluşmaz',
            'B': '681 Önceki Dönem Gider ve Zararları 30.000 ₺; 661 Uzun Vadeli Borçlanma Giderleri 25.000 ₺',
            'C': '656 Kambiyo Zararları 30.000 ₺; 660 Kısa Vadeli Borçlanma Giderleri 25.000 ₺',
            'D': '646 Kambiyo Kârları 30.000 ₺; 642 Faiz Gelirleri 25.000 ₺',
            'E': '656 Kambiyo Zararları 55.000 ₺; finansman gideri oluşmaz',
        },
        'C',
        'Kredinin TL karşılığındaki 630.000 − 600.000 = **30.000 ₺** artış kambiyo zararıdır ve 656 hesapta izlenir. Ayrıca ödenen **25.000 ₺ faiz**, kısa vadeli borçlanmaya ait finansman gideridir ve gelir tablosunda 660 hesaba yansıtılır.',
        "1 Sıra No'lu MSUGT - 656/660",
    ),
    # düzey 3
    '0016': patch(
        "Bir işletmenin brüt satışları 700.000 ₺, satıştan iadeleri 30.000 ₺, satış iskontoları 20.000 ₺ ve satışların maliyeti 390.000 ₺'dir. Faaliyet giderleri 120.000 ₺, faiz gelirleri 20.000 ₺, kambiyo kârları 10.000 ₺, reeskont faiz giderleri 5.000 ₺ ve finansman giderleri 35.000 ₺'dir.\n\nİşletmenin olağan kârı kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '160.000',
            'C': '260.000',
            'D': '135.000',
            'E': '130.000',
        },
        'E',
        "Net satışlar 700.000 − 30.000 − 20.000 = 650.000 ₺; brüt kâr 650.000 − 390.000 = 260.000 ₺ ve faaliyet kârı 260.000 − 120.000 = 140.000 ₺'dir. Olağan kâr 140.000 + 20.000 + 10.000 − 5.000 − 35.000 = **130.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - 60/61/62/63/64/65/66 hesap grupları",
    ),
    # düzey 3
    '0017': patch(
        "Bir işletmenin dönem verileri şöyledir: net satışlar 800.000 ₺, satışların maliyeti 480.000 ₺, faaliyet giderleri 150.000 ₺, diğer faaliyetlerden olağan gelir ve kârlar 30.000 ₺, diğer faaliyetlerden olağan gider ve zararlar 10.000 ₺, finansman giderleri 20.000 ₺, olağandışı gelir ve kârlar 5.000 ₺, olağandışı gider ve zararlar 15.000 ₺. Kurumlar vergisi oranının %25 olduğu ve kanunen kabul edilmeyen gider bulunmadığı varsayılmaktadır. Buna göre dönem net kârı kaç ₺'dir?",
        {
            'A': '160.000 ₺',
            'B': '117.500 ₺',
            'C': '120.000 ₺',
            'D': '112.500 ₺',
            'E': '105.000 ₺',
        },
        'C',
        'Dönem kârı: 800.000 − 480.000 − 150.000 + 30.000 − 10.000 − 20.000 + 5.000 − 15.000 = 160.000 ₺. Vergi 160.000 × %25 = 40.000 ₺; dönem net kârı **120.000 ₺** (692 → 590).',
        'THP 690, 691, 692',
    ),
    # düzey 2
    '0018': patch(
        'Bir işletmenin gelir hesapları sınıflandırılmaktadır. Buna göre aşağıdaki hesaplardan hangisi 67 Olağandışı Gelir ve Kârlar grubunda yer alır?',
        {
            'A': '649 Diğer Olağan Gelir ve Kârlar',
            'B': '671 Önceki Dönem Gelir ve Kârları',
            'C': '645 Menkul Kıymet Satış Kârları',
            'D': '642 Faiz Gelirleri',
            'E': '646 Kambiyo Kârları',
        },
        'B',
        '67 grubunda 671 Önceki Dönem Gelir ve Kârları ve 679 Diğer Olağandışı Gelir ve Kârlar yer alır. 642, 645, 646 ve 649 **64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar** grubundadır.',
        'THP 67 Olağandışı Gelir ve Kârlar',
    ),
    # düzey 2
    '0019': patch(
        'Bir işletmenin gelir tablosunda kâr kademeleri incelenmektedir. Buna göre aşağıdaki kalemlerden hangisi faaliyet kârını etkilemez, ancak olağan kârı etkiler?',
        {
            'A': 'Satıştan iadeler',
            'B': 'Genel yönetim giderleri',
            'C': 'Satılan ticari mallar maliyeti',
            'D': 'Kambiyo zararları',
            'E': 'Pazarlama giderleri',
        },
        'D',
        'Satış indirimleri, satışların maliyeti ve faaliyet giderleri faaliyet kârından önce düşülür. **Kambiyo zararları** (656) 65 grubundadır; faaliyet kârından sonra, olağan kâr hesaplanırken dikkate alınır.',
        'THP 6 Gelir Tablosu; kâr kademeleri',
    ),
    # düzey 3
    '0020': patch(
        "Bir işletmenin dönem içinde brüt satışları 1.000.000 ₺, satıştan iadeleri 50.000 ₺ ve satış iskontoları 30.000 ₺'dir. Net satışlar üzerinden brüt satış kârı oranı %35'tir. Dönemin pazarlama, satış ve dağıtım giderleri 90.000 ₺, genel yönetim giderleri 120.000 ₺, araştırma ve geliştirme giderleri 20.000 ₺ ve kısa vadeli borçlanma giderleri 15.000 ₺'dir.\n\nBuna göre işletmenin faaliyet kârı kaç ₺'dir?",
        {
            'A': '92.000',
            'B': '77.000',
            'C': '120.000',
            'D': '109.500',
            'E': '72.000',
        },
        'A',
        'Net satışlar = 1.000.000 − 50.000 − 30.000 = 920.000 ₺; brüt satış kârı = 920.000 × %35 = 322.000 ₺. Faaliyet giderleri 90.000 + 120.000 + 20.000 = 230.000 ₺. Faaliyet kârı = 322.000 − 230.000 = 92.000 ₺. Borçlanma giderleri 66 grubundadır; faaliyet kârından sonra düşülür.',
        'Gelir tablosu; brüt kâr oranı',
    ),
    # düzey 2
    '0021': patch(
        "Gelir tablosunda 'Net Satışlar' nasıl hesaplanır?",
        {
            'A': 'Brüt Satışlar − Satışların Maliyeti − Faaliyet Giderleri',
            'B': 'Brüt Satışlar − Satışların Maliyeti (62 grubu, negatif)',
            'C': 'Brüt Satışlar + Satış İndirimleri (satıştan iadeler, iskontolar vb.)',
            'D': 'Brüt Satışlar − Satış İndirimleri (satıştan iadeler, iskontolar vb.)',
            'E': 'Brüt Satışlar + Satışların Maliyeti + Faaliyet Giderleri',
        },
        'D',
        '**Net Satışlar = Brüt Satışlar − Satış İndirimleri** (satıştan iadeler + satış iskontoları + diğer indirimler).',
        "1 Sıra No'lu MSUGT - Gelir Tablosu",
    ),
    # düzey 2
    '0022': patch(
        "Aralıklı envanter yöntemini uygulayan bir ticaret işletmesinin dönem verileri şöyledir: dönem başı ticari mal stoku 80.000 ₺, dönem içi alışlar 520.000 ₺, alışlara ilişkin nakliye giderleri 12.000 ₺, satıcılara yapılan alış iadeleri 20.000 ₺, satıcılardan sonradan alınan alış iskontoları 8.000 ₺ ve dönem sonu sayımla belirlenen stok 110.000 ₺'dir. KDV ihmal edilecektir.\n\nBuna göre gelir tablosunda '621 Satılan Ticari Mallar Maliyeti' olarak gösterilecek tutar kaç ₺'dir?",
        {
            'A': '462.000',
            'B': '502.000',
            'C': '584.000',
            'D': '494.000',
            'E': '474.000',
        },
        'E',
        'Net alışlar = 520.000 + 12.000 (alış nakliyesi maliyete girer) − 20.000 (alış iadesi) − 8.000 (alış iskontosu) = 504.000 ₺. Satılan ticari mallar maliyeti = dönem başı stok 80.000 + net alışlar 504.000 − dönem sonu stok 110.000 = 474.000 ₺.',
        "1 Sıra No'lu MSUGT - Brüt satış kârı; 2024-2025 SGS dikey yüzde soru örüntüsü",
    ),
    # düzey 2
    '0023': patch(
        "Aşağıdaki hesaplardan hangisi '65 Diğer Faaliyetlerden Olağan Gider ve Zararlar (-)' grubunda yer almaz?",
        {
            'A': '653 Komisyon Giderleri (-)',
            'B': '654 Karşılık Giderleri (-)',
            'C': '620 Satılan Mamuller Maliyeti (-)',
            'D': '655 Menkul Kıymet Satış Zararları (-)',
            'E': '659 Diğer Olağan Gider ve Zararlar (-)',
        },
        'C',
        '653, 654, 655 ve 659 hesapları 65 Diğer Faaliyetlerden Olağan Gider ve Zararlar grubundadır. 620 Satılan Mamuller Maliyeti ise 62 Satışların Maliyeti grubunda yer alır.',
        "1 Sıra No'lu MSUGT - 65 / 654",
    ),
    # düzey 2
    '0024': patch(
        "Ticari mal satan bir işletme aynı gün iki satış yapmıştır: yurt dışındaki bir alıcıya 10.000 USD tutarında mal ihraç edilmiş, gümrük çıkış tarihindeki kur 32,00 ₺/USD olup bedel henüz tahsil edilmemiştir; yurt içinde bir müşteriye 50.000 ₺ + %20 KDV mal veresiye satılmıştır. İhracat teslimi KDV'den istisnadır. Satışların maliyet kayıtları ayrıca yapılacaktır.\n\nHasılat kayıtlarında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '600 Yurt İçi Satışlar hesabı toplam 370.000 ₺ alacaklandırılır',
            'B': '601 Yurt Dışı Satışlar hesabı 320.000 ₺ alacaklandırılır',
            'C': '391 Hesaplanan KDV hesabı 74.000 ₺ alacaklandırılır',
            'D': '601 Yurt Dışı Satışlar hesabı 10.000 ₺ alacaklandırılır',
            'E': '120 Alıcılar hesabı toplam 370.000 ₺ borçlandırılır',
        },
        'B',
        "İhracat 601 Yurt Dışı Satışlar hesabına Türk lirası karşılığıyla yazılır: 10.000 × 32,00 = 320.000 ₺; istisna olduğundan KDV hesaplanmaz. Yurt içi satış 600'e 50.000 ₺, KDV 391'e 10.000 ₺ yazılır. 120 Alıcılar toplam 320.000 + 60.000 = 380.000 ₺ borçlandırılır.",
        "1 Sıra No'lu MSUGT - 600 / 391",
    ),
    # düzey 3
    '0025': patch(
        "Aralıklı envanter yöntemini kullanan bir ticaret işletmesinin dönem başı mal mevcudu 70.000 ₺, dönem içi mal alışları 400.000 ₺, alış iadeleri 20.000 ₺ ve alışlara ait taşıma giderleri 10.000 ₺'dir. Dönem sonu mal mevcudu 90.000 ₺'dir.\n\nSatılan ticari malların maliyeti kaç ₺'dir?",
        {
            'A': '390.000',
            'B': '460.000',
            'C': '410.000',
            'D': '350.000',
            'E': '370.000',
        },
        'E',
        "Net alışlar = 400.000 − 20.000 + 10.000 = 390.000 ₺'dir. Satılan ticari mallar maliyeti = 70.000 + 390.000 − 90.000 = **370.000 ₺** olarak hesaplanır.",
        "1 Sıra No'lu MSUGT - 153/621; aralıklı envanter maliyet akışı",
    ),
    # düzey 3
    '0026': patch(
        "Maliyeti 200.000 ₺, birikmiş amortismanı 140.000 ₺ olan makine, esas faaliyet konusu duran varlık ticareti olmayan işletme tarafından 80.000 ₺ + %20 KDV ile kredili satılmıştır.\n\nSatış kaydında 679 Diğer Olağandışı Gelir ve Kârlar hesabına yazılacak tutar kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '80.000',
            'C': '60.000',
            'D': '16.000',
            'E': '140.000',
        },
        'A',
        "Makinenin net defter değeri 200.000 − 140.000 = 60.000 ₺'dir. KDV hariç satış bedeli 80.000 ₺ olduğundan duran varlık satış kârı 80.000 − 60.000 = **20.000 ₺**'dir ve 679 hesaba alacak kaydedilir.",
        "1 Sıra No'lu MSUGT - 120/253/257/391/679; 2025-2026 SGS duran varlık satışı soru örüntüsü",
    ),
    # düzey 2
    '0027': patch(
        "Dönem kârı üzerinden hesaplanan vergi ve diğer yasal yükümlülük karşılıkları, dönem net kârının belirlenmesinde Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '360 Ödenecek Vergi ve Fonlar hesabında bir gider olarak izlenir.',
            'B': '692 Dönem Net Kârı veya Zararı hesabında ayrıca izlenir.',
            'C': '770 Genel Yönetim Giderleri (-) hesabında gider yazılır.',
            'D': '691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları (-)',
            'E': '690 Dönem Kârı veya Zararı hesabında brüt kâr olarak izlenir.',
        },
        'D',
        "Dönem kârı üzerinden hesaplanan vergi karşılığı, sonuç hesabı olarak **691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları (-)** hesabında izlenir (690'dan düşülerek 692'ye ulaşılır).",
        "1 Sıra No'lu MSUGT - 691",
    ),
    # düzey 2
    '0028': patch(
        'Dönem sonunda işletme vadesi gelmemiş alacak senetleri için 6.000 ₺, borç senetleri için 4.000 ₺ reeskont hesaplayarak kayıtlarına almıştır.\n\nReeskont işlemlerinden doğan faiz gelir ve giderleri gelir tablosunda hangi hesaplarda izlenir?',
        {
            'A': 'Her ikisi de 66 Finansman Giderleri grubunda; gelirler 660, giderler 661 hesabındadır.',
            'B': 'Reeskont faiz gelirleri 600 Yurt İçi Satışlar, giderleri 621 Mallar Maliyeti hesabında izlenir.',
            'C': 'Reeskont faiz gelirleri 647 (64 grubu), reeskont faiz giderleri 657 (65 grubu)',
            'D': 'Reeskont faiz gelirleri 642 Faiz Gelirleri, giderleri 653 Komisyon Giderleri hesabındadır.',
            'E': 'Reeskont faiz gelirleri 679 (67 grubu), giderleri 689 (68 grubu) hesabında izlenir.',
        },
        'C',
        '**Reeskont faiz gelirleri → 647 Reeskont Faiz Gelirleri (64 grubu, olağan gelir)**; **reeskont faiz giderleri → 657 Reeskont Faiz Giderleri (65 grubu, olağan gider)**.',
        "1 Sıra No'lu MSUGT - 647 / 657",
    ),
    # düzey 2
    '0029': patch(
        "Aralıklı envanter yöntemini uygulayan bir ticaret işletmesinin dönem verileri şöyledir: brüt satışlar 800.000 ₺, satıştan iadeler 40.000 ₺, dönem başı ticari mal stoku 120.000 ₺, dönem içi net alışlar 500.000 ₺, dönem sonu sayımla belirlenen stok 140.000 ₺, faaliyet giderleri toplamı 110.000 ₺, komisyon gelirleri 10.000 ₺ ve kredi faiz giderleri 30.000 ₺. Olağandışı kalem ve kanunen kabul edilmeyen gider yoktur; soruda kullanılacak vergi oranı %25'tir.\n\nBuna göre işletmenin dönem net kârı kaç ₺'dir?",
        {
            'A': '150.000',
            'B': '127.500',
            'C': '142.500',
            'D': '112.500',
            'E': '120.000',
        },
        'D',
        'Satılan ticari mallar maliyeti = 120.000 + 500.000 − 140.000 = 480.000 ₺. Net satışlar 760.000 ₺; brüt satış kârı 280.000 ₺; faaliyet kârı 170.000 ₺. Dönem kârı = 170.000 + 10.000 − 30.000 = 150.000 ₺; vergi karşılığı 37.500 ₺; dönem net kârı 112.500 ₺.',
        "1 Sıra No'lu MSUGT - Brüt ve faaliyet kârı; 2024-2025 SGS dikey yüzde soru örüntüsü",
    ),
    # düzey 3
    '0030': patch(
        'Dönem sonunda 600 Yurt İçi Satışlar hesabı 500.000 ₺, 642 Faiz Gelirleri hesabı 20.000 ₺ ve 679 Diğer Olağandışı Gelir ve Kârlar hesabı 10.000 ₺ alacak kalanı vermektedir.\n\nBu gelir hesaplarının 690 Dönem Kârı veya Zararı hesabına devrinde yapılacak kayıt hangisidir?',
        {
            'A': '600 Yurt İçi Satışlar 500.000 ₺ borç / 690 Dönem Kârı veya Zararı 500.000 ₺ alacak; diğer gelirler devredilmez',
            'B': '600, 642 ve 679 hesapları toplam 530.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 530.000 ₺ alacak',
            'C': '600, 642 ve 679 hesapları toplam 530.000 ₺ borç / 690 Dönem Kârı veya Zararı 530.000 ₺ alacak',
            'D': '690 Dönem Kârı veya Zararı 530.000 ₺ borç / 600, 642 ve 679 hesapları toplam 530.000 ₺ alacak',
            'E': '690 Dönem Kârı veya Zararı 530.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 530.000 ₺ alacak',
        },
        'C',
        'Alacak kalanı veren gelir hesapları kapatılırken **borçlandırılır**; toplam 500.000 + 20.000 + 10.000 = **530.000 ₺**, 690 hesabın alacağına devredilir.',
        "1 Sıra No'lu MSUGT - Gelir hesaplarının 690 hesaba devri",
    ),
    # düzey 2
    '0031': patch(
        'Dönem sonunda 692 Dönem Net Kârı veya Zararı hesabı 40.000 ₺ borç kalanı vermiştir.\n\nBu hesabın kapatılmasında yapılacak kayıt hangisidir?',
        {
            'A': '591 Dönem Net Zararı 40.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 40.000 ₺ alacak',
            'B': '590 Dönem Net Kârı 40.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 40.000 ₺ alacak',
            'C': '692 Dönem Net Kârı veya Zararı 40.000 ₺ borç / 591 Dönem Net Zararı 40.000 ₺ alacak',
            'D': '690 Dönem Kârı veya Zararı 40.000 ₺ borç / 591 Dönem Net Zararı 40.000 ₺ alacak',
            'E': '692 Dönem Net Kârı veya Zararı 40.000 ₺ borç / 590 Dönem Net Kârı 40.000 ₺ alacak',
        },
        'A',
        "692 hesabın borç kalanı net zararı gösterir. Bu nedenle **591 Dönem Net Zararı borçlandırılır**, 692 hesap alacaklandırılarak kapatılır. Bu kapanış biçimi 18 Temmuz 2026 SGS'de de doğrudan ölçülmüştür.",
        "1 Sıra No'lu MSUGT - 692/591; 18 Temmuz 2026 SGS soru örüntüsü",
    ),
    # düzey 3
    '0032': patch(
        "Maliyeti 100.000 ₺, ayrılmış değer düşüklüğü karşılığı 15.000 ₺ olan hisse senetleri 120.000 ₺'ye banka aracılığıyla satılmıştır. Banka 2.000 ₺ komisyon keserek kalanı hesaba aktarmıştır.\n\nSatış kaydında yer alacak hesap ve tutarlarla ilgili doğru seçenek hangisidir?",
        {
            'A': '102 Bankalar 118.000 ₺, 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ borç; 110 Hisse Senetleri 153.000 ₺ alacak',
            'B': '102 Bankalar 118.000 ₺, 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ ve 653 Komisyon Giderleri 2.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺, 644 Konusu Kalmayan Karşılıklar 15.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ alacak',
            'C': '102 Bankalar 120.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ alacak',
            'D': '102 Bankalar 118.000 ₺ ve 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺ ve 649 Diğer Olağan Gelir ve Kârlar 33.000 ₺ alacak',
            'E': '102 Bankalar 118.000 ₺ ve 653 Komisyon Giderleri 2.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ alacak; karşılık kapatılmaz',
        },
        'B',
        'Bankaya net 118.000 ₺ girer ve 2.000 ₺ komisyon 653 hesaba borç yazılır. Satılan menkul kıymete ait 15.000 ₺ karşılık 119 borç / 644 alacak kaydıyla kapatılır. Satış bedeli ile maliyet arasındaki **20.000 ₺** fark 645 hesaba alacak kaydedilir.',
        "1 Sıra No'lu MSUGT - 102/110/119/644/645/653; 2024-2026 SGS menkul kıymet satışı soru örüntüsü",
    ),
    # düzey 2
    '0033': patch(
        "Dönem içinde 900.000 ₺ brüt satış yapan işletmenin müşterileri kusurlu bulunan 40.000 ₺'lik malı iade etmiş, bir müşteriye de erken ödeme nedeniyle sonradan 15.000 ₺ iskonto yapılmıştır.\n\nSatıştan iadeler (610) ve satış iskontolarının (611) gelir tablosundaki etkisiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Satışların maliyetine eklenerek brüt satış kârını azaltan gider unsurudur.',
            'B': 'Brüt satışlara eklenerek net satışları ve brüt satış kârını artıran gelir kalemleridir.',
            'C': 'Özkaynaklar içinde dönem kârını doğrudan artıran birer gelir kalemidir.',
            'D': 'Doğrudan 66 Finansman Giderleri grubunda gider olarak kaydedilirler.',
            'E': 'Brüt satışlardan düşülerek net satışları azaltırlar (negatif nitelikli hesaplardır).',
        },
        'E',
        '**610 Satıştan İadeler (-)** ve **611 Satış İskontoları (-)** negatif nitelikli hesaplardır; brüt satışlardan **düşülerek net satışları azaltırlar**.',
        "1 Sıra No'lu MSUGT - 610 / 611",
    ),
    # düzey 2
    '0034': patch(
        "Bir işletmenin ortalama stokları 50.000 ₺ ve stok devir hızı 2,4'tür. Brüt satış kârı oranı %40, faaliyet giderleri toplamı 95.000 ₺'dir.\n\nİşletmenin faaliyet sonucu aşağıdakilerden hangisidir?",
        {
            'A': '25.000 ₺ zarar',
            'B': '80.000 ₺ zarar',
            'C': '15.000 ₺ zarar',
            'D': '5.000 ₺ kâr',
            'E': '15.000 ₺ kâr',
        },
        'C',
        "Satışların maliyeti 50.000 × 2,4 = 120.000 ₺'dir. Maliyet, net satışların %60'ı olduğundan net satışlar 200.000 ₺ ve brüt kâr 80.000 ₺'dir. Faaliyet sonucu 80.000 − 95.000 = **15.000 ₺ zarar**dır.",
        "1 Sıra No'lu MSUGT - Faaliyet sonucu; 2025 SGS stok devir hızı soru örüntüsü",
    ),
    # düzey 2
    '0035': patch(
        "Bir işletmenin dönem içinde sattığı mamullerin maliyeti 120.000 ₺, ticari malların maliyeti 180.000 ₺ ve sunduğu hizmetlerin maliyeti 40.000 ₺'dir.\n\nGelir tablosunda 'Satışların Maliyeti' grubunda raporlanacak toplam tutar kaç ₺'dir?",
        {
            'A': '180.000',
            'B': '300.000',
            'C': '220.000',
            'D': '340.000',
            'E': '120.000',
        },
        'D',
        "620 Satılan Mamuller Maliyeti, 621 Satılan Ticari Mallar Maliyeti ve 622 Satılan Hizmet Maliyeti, 62 Satışların Maliyeti grubunda birlikte raporlanır. Toplam 120.000 + 180.000 + 40.000 = **340.000 ₺**'dir.",
        "1 Sıra No'lu MSUGT - 620/621/622",
    ),
    # düzey 3
    '0036': patch(
        'Bir işletmenin gelir tablosu verileri aşağıdaki gibidir:\n\n2025: Net satışlar 400.000 ₺, brüt satış kârı 120.000 ₺, faaliyet giderleri 80.000 ₺.\n2026: Net satışlar 500.000 ₺, brüt satış kârı 150.000 ₺, faaliyet giderleri 105.000 ₺.\n\nBu verilere göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Faaliyet giderlerinin net satışlara oranı iki yılda da aynıdır.',
            'B': 'Brüt kâr marjı sabit kalırken faaliyet kâr marjı düşmüştür.',
            'C': "Brüt kâr marjı 2026'da %5 azalmıştır.",
            'D': "Faaliyet kârı tutarı 2026'da azalmıştır.",
            'E': "2026'da faaliyet kârı oluşmamıştır.",
        },
        'B',
        "Brüt kâr marjı her iki yılda da %30'dur. Faaliyet kârı 2025'te 40.000 ₺ ve marjı %10; 2026'da 45.000 ₺ ve marjı %9'dur. Dolayısıyla brüt marj sabit kalmış, faaliyet kârı tutarı artsa da **faaliyet kâr marjı düşmüştür**.",
        "1 Sıra No'lu MSUGT - Gelir tablosu kârlılık basamakları; 2025 SGS yatay analiz soru örüntüsü",
    ),
    # düzey 3
    '0037': patch(
        'Gelir tablosu ve dönem sonu hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Net satışlar, brüt satışlardan satış indirimlerinin düşülmesiyle bulunur.\n\nII. 621 Satılan Ticari Mallar Maliyeti faaliyet gideri değil, satışların maliyeti grubundadır.\n\nIII. 690 hesabın alacak kalanı vergi öncesi kârı gösterir; 691 hesabın borç kalanı net kâra ulaşılırken bu tutarı azaltır.\n\nIV. 692 hesabın borç kalanı 591 Dönem Net Zararı hesabına devredilir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız IV',
            'C': 'I, III ve IV',
            'D': 'I ve II',
            'E': 'I, II, III ve IV',
        },
        'E',
        "Dört ifade de doğrudur. 61 grubu brüt satışlardan düşülür; 621 hesabı 62 grubundadır. 690'ın alacak kalanı vergi öncesi kârı, 691'in borç kalanı vergi karşılığını gösterir. 692 borç kalanı verdiğinde net zarar 591 hesaba devredilir.",
        "1 Sıra No'lu MSUGT - 61/62/690/691/692/591",
    ),
    # düzey 2
    '0038': patch(
        'Bir işletmenin dönem içindeki gelir ve kârları sınıflandırılmaktadır. Buna göre aşağıdaki hesaplardan hangisi 64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar grubunda yer almaz?',
        {
            'A': '656 Kambiyo Zararları',
            'B': '646 Kambiyo Kârları',
            'C': '643 Komisyon Gelirleri',
            'D': '642 Faiz Gelirleri',
            'E': '645 Menkul Kıymet Satış Kârları',
        },
        'A',
        '656 Kambiyo Zararları bir giderdir ve **65 Diğer Faaliyetlerden Olağan Gider ve Zararlar** grubundadır.',
        'THP 64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar',
    ),
    # düzey 3
    '0039': patch(
        "Aralıklı envanter yöntemini kullanan bir ticaret işletmesinin dönem başı mal mevcudu 100.000 ₺, dönem içi net alışları 500.000 ₺, dönem sonu mal mevcudu 150.000 ₺, net satışları 800.000 ₺ ve faaliyet giderleri 120.000 ₺'dir. Buna göre faaliyet kârı kaç ₺'dir?",
        {
            'A': '350.000 ₺',
            'B': '80.000 ₺',
            'C': '110.000 ₺',
            'D': '230.000 ₺',
            'E': '330.000 ₺',
        },
        'D',
        'SMM = 100.000 + 500.000 − 150.000 = 450.000 ₺; brüt satış kârı 350.000 ₺; faaliyet kârı 350.000 − 120.000 = **230.000 ₺**.',
        'Aralıklı envanter; kâr kademeleri',
    ),
    # düzey 3
    '0040': patch(
        "Dönem sonunda 600 Yurt İçi Satışlar hesabının alacak kalanı 800.000 ₺, 610 Satıştan İadeler hesabının borç kalanı 30.000 ₺ ve 611 Satış İskontoları hesabının borç kalanı 20.000 ₺'dir. Buna göre bu hesapların 690 Dönem Kârı veya Zararı hesabına aktarılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '611 Satış İskontoları hesabı 20.000 ₺ borçlandırılır',
            'B': '690 Dönem Kârı veya Zararı hesabı 800.000 ₺ borçlandırılır',
            'C': '610 Satıştan İadeler hesabı 30.000 ₺ alacaklandırılır',
            'D': '610 Satıştan İadeler hesabı 30.000 ₺ borçlandırılır',
            'E': '600 Yurt İçi Satışlar hesabı 800.000 ₺ alacaklandırılır',
        },
        'C',
        'Hesaplar kalanlarının ters tarafına kayıtla kapatılır: 600 (borç) 800.000 / 690 (alacak) 800.000; 690 (borç) 50.000 / **610 (alacak) 30.000** + 611 (alacak) 20.000.',
        'THP 600, 610, 611, 690',
    ),
    # düzey 2
    '0041': patch(
        "Ticaret ve bakım hizmeti sunan bir işletmenin dönem sonu kalanları şöyledir: 600 Yurt İçi Satışlar 1.500.000 ₺, 601 Yurt Dışı Satışlar 300.000 ₺, 610 Satıştan İadeler 60.000 ₺, 611 Satış İskontoları 20.000 ₺, 612 Diğer İndirimler 10.000 ₺, 621 Satılan Ticari Mallar Maliyeti 900.000 ₺, 622 Satılan Hizmet Maliyeti 50.000 ₺, 631 Pazarlama, Satış ve Dağıtım Giderleri 120.000 ₺, 632 Genel Yönetim Giderleri 140.000 ₺, 649 Diğer Olağan Gelir ve Kârlar 30.000 ₺, 653 Komisyon Giderleri 5.000 ₺.\n\nBuna göre işletmenin faaliyet kârı kaç ₺'dir?",
        {
            'A': '525.000',
            'B': '460.000',
            'C': '480.000',
            'D': '500.000',
            'E': '490.000',
        },
        'D',
        'Brüt satışlar = 1.500.000 + 300.000 = 1.800.000 ₺; satış indirimleri 90.000 ₺; net satışlar 1.710.000 ₺. Satışların maliyeti 900.000 + 50.000 = 950.000 ₺; brüt satış kârı 760.000 ₺. Faaliyet kârı = 760.000 − 120.000 − 140.000 = 500.000 ₺. 649 ve 653 diğer faaliyetlerden olağan kalemlerdir; faaliyet kârından sonra dikkate alınır.',
        "1 Sıra No'lu MSUGT - Gelir tablosu biçimi ve 60/61 hesap grupları",
    ),
    # düzey 2
    '0042': patch(
        "Bir ticaret işletmesinin dönem başı stoku 30.000 ₺, dönem sonu stoku 50.000 ₺'dir. Ortalama stoka göre hesaplanan stok devir hızı 3, net satışlar üzerinden brüt satış kârı oranı %40'tır. Dönemin faaliyet giderleri 35.000 ₺, diğer faaliyetlerden olağan gelirleri 5.000 ₺, finansman giderleri 8.000 ₺'dir.\n\nBuna göre işletmenin olağan kârı kaç ₺'dir?",
        {
            'A': '45.000',
            'B': '42.000',
            'C': '50.000',
            'D': '37.000',
            'E': '58.000',
        },
        'B',
        "Ortalama stok = (30.000 + 50.000) / 2 = 40.000 ₺; satışların maliyeti = 40.000 × 3 = 120.000 ₺. Maliyet net satışların %60'ı olduğundan net satışlar 200.000 ₺, brüt satış kârı 80.000 ₺. Faaliyet kârı 80.000 − 35.000 = 45.000 ₺; olağan kâr = 45.000 + 5.000 − 8.000 = 42.000 ₺.",
        "1 Sıra No'lu MSUGT - Faaliyet kârı; 2025 SGS stok devir hızı ve brüt kâr oranı soru örüntüsü",
    ),
    # düzey 2
    '0043': patch(
        'Gelir tablosunda kâr kademelerinin oluşum sırası aşağıdakilerden hangisidir?',
        {
            'A': 'Faaliyet Kârı → Brüt Satış Kârı → Olağan Kâr → Dönem Net Kârı → Dönem Kârı',
            'B': 'Dönem Kârı → Olağan Kâr → Faaliyet Kârı → Dönem Net Kârı → Brüt Satış Kârı',
            'C': 'Dönem Net Kârı → Dönem Kârı → Faaliyet Kârı → Brüt Satış Kârı → Olağan Kâr',
            'D': 'Olağan Kâr → Brüt Satış Kârı → Faaliyet Kârı → Dönem Kârı → Dönem Net Kârı',
            'E': 'Brüt Satış Kârı → Faaliyet Kârı → Olağan Kâr → Dönem Kârı → Dönem Net Kârı',
        },
        'E',
        'Gelir tablosunda kâr kademeleri sırasıyla: **Brüt Satış Kârı → Faaliyet Kârı → Olağan Kâr → Dönem Kârı → Dönem Net Kârı** biçiminde oluşur.',
        "1 Sıra No'lu MSUGT - Gelir Tablosu",
    ),
    # düzey 2
    '0044': patch(
        "Sürekli envanter yöntemini kullanan işletmede, daha önce kredili satılan malın 12.000 ₺ + %20 KDV tutarındaki kısmı müşteri tarafından iade edilmiştir. İade edilen malın maliyeti 8.000 ₺'dir.\n\nİade tarihinde yapılması gereken kayıtlar hangisidir?",
        {
            'A': '610 Satıştan İadeler 12.000 ₺ ve 391 Hesaplanan KDV 2.400 ₺ borç / 120 Alıcılar 14.400 ₺ alacak; 153 Ticari Mallar 8.000 ₺ borç / 621 Satılan Ticari Mallar Maliyeti 8.000 ₺ alacak',
            'B': '610 Satıştan İadeler 12.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak; maliyet kaydı yapılmaz',
            'C': '610 Satıştan İadeler 14.400 ₺ borç / 120 Alıcılar 14.400 ₺ alacak; 621 Satılan Ticari Mallar Maliyeti 8.000 ₺ borç / 153 Ticari Mallar 8.000 ₺ alacak',
            'D': '120 Alıcılar 14.400 ₺ borç / 600 Yurt İçi Satışlar 12.000 ₺ ve 391 Hesaplanan KDV 2.400 ₺ alacak',
            'E': '153 Ticari Mallar 12.000 ₺ borç / 610 Satıştan İadeler 12.000 ₺ alacak; 391 Hesaplanan KDV 2.400 ₺ borç / 120 Alıcılar 2.400 ₺ alacak',
        },
        'A',
        "Satış iadesi hasılatı ve satışta doğan KDV'yi tersine çevirir: 610 ve 391 borç, 120 alacak kaydedilir. Sürekli envanter yönteminde mal yeniden stoka girdiği için ayrıca **153 borç / 621 alacak 8.000 ₺** kaydı yapılır.",
        "1 Sıra No'lu MSUGT - 120/153/391/610/621",
    ),
    # düzey 3
    '0045': patch(
        "Bir işletmenin brüt satışları 500.000 ₺, satıştan iadeleri 20.000 ₺, satış iskontoları 10.000 ₺ ve satışların maliyeti 300.000 ₺'dir. Pazarlama, satış ve dağıtım giderleri 60.000 ₺; genel yönetim giderleri 40.000 ₺'dir.\n\nİşletmenin faaliyet kârı kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '70.000',
            'C': '170.000',
            'D': '100.000',
            'E': '30.000',
        },
        'B',
        "Net satışlar 500.000 − 20.000 − 10.000 = 470.000 ₺; brüt satış kârı 470.000 − 300.000 = 170.000 ₺'dir. Faaliyet kârı 170.000 − 60.000 − 40.000 = **70.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Net satışlardan faaliyet kârına geçiş",
    ),
    # düzey 2
    '0046': patch(
        "Bir işletmenin brüt satışları 90.000 ₺, satıştan iadeleri 10.000 ₺ ve satışların maliyeti 32.000 ₺'dir. Brüt satış kârı, dönem net kârının üç katıdır.\n\nİşletmenin dönem net kârı kaç ₺'dir?",
        {
            'A': '24.000',
            'B': '48.000',
            'C': '12.000',
            'D': '16.000',
            'E': '14.000',
        },
        'D',
        "Net satışlar 90.000 − 10.000 = 80.000 ₺; brüt satış kârı 80.000 − 32.000 = 48.000 ₺'dir. Brüt kâr net kârın üç katı olduğundan dönem net kârı 48.000 / 3 = **16.000 ₺** bulunur.",
        "1 Sıra No'lu MSUGT - Gelir tablosu kâr basamakları; 13 Temmuz 2024 SGS soru örüntüsü",
    ),
    # düzey 2
    '0047': patch(
        "Vergi karşılığı düşüldükten sonra kalan ve bilançodaki 590 Dönem Net Kârı'na aktarılacak sonuç Tekdüzen Hesap Planı'nda hangi hesapta belirlenir?",
        {
            'A': '691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları (-)',
            'B': '570 Geçmiş Yıllar Kârları',
            'C': '692 Dönem Net Kârı veya Zararı',
            'D': '690 Dönem Kârı veya Zararı',
            'E': '600 Yurt İçi Satışlar',
        },
        'C',
        "690'dan 691 (vergi karşılığı) düşüldükten sonra kalan tutar **692 Dönem Net Kârı veya Zararı** hesabında belirlenir ve bilançodaki **590 Dönem Net Kârı**'na aktarılır.",
        "1 Sıra No'lu MSUGT - 692 / 590",
    ),
    # düzey 2
    '0048': patch(
        "'631 Pazarlama, Satış ve Dağıtım Giderleri' ile '632 Genel Yönetim Giderleri' hesaplarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': '632 satış personelinin, 631 yönetimin giderlerini izler',
            'B': '631, ürünlerin pazarlanması ve dağıtımıyla ilgili giderleri izler',
            'C': '632, işletmenin genel yönetimine ilişkin giderleri izler',
            'D': 'İki hesap da 63 Faaliyet Giderleri grubundadır',
            'E': 'İki hesap da brüt satış kârından düşülerek faaliyet kârına ulaşılır',
        },
        'A',
        '631 ürünlerin pazarlanması, satışı ve dağıtımıyla ilgili giderleri; 632 işletmenin genel yönetimiyle ilgili giderleri izler. İkisi de 63 Faaliyet Giderleri grubundadır ve brüt satış kârından düşülerek faaliyet kârı bulunur. A şıkkı hesapların içeriğini yer değiştirmiştir.',
        "1 Sıra No'lu MSUGT - 631 / 632",
    ),
    # düzey 3
    '0049': patch(
        "Faaliyet kârı 120.000 ₺ olan işletmenin diğer faaliyetlerden olağan gelirleri 30.000 ₺, diğer faaliyetlerden olağan giderleri 10.000 ₺ ve finansman giderleri 25.000 ₺'dir. Ayrıca 8.000 ₺ olağandışı gelir ve 3.000 ₺ olağandışı gider bulunmaktadır.\n\nİşletmenin olağan kârı ile vergi öncesi dönem kârı sırasıyla kaç ₺'dir?",
        {
            'A': '115.000 ve 112.000',
            'B': '145.000 ve 150.000',
            'C': '120.000 ve 115.000',
            'D': '140.000 ve 145.000',
            'E': '115.000 ve 120.000',
        },
        'E',
        "Olağan kâr = 120.000 + 30.000 − 10.000 − 25.000 = **115.000 ₺**'dir. Vergi öncesi dönem kârı = 115.000 + 8.000 − 3.000 = **120.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Gelir tablosu kâr basamakları",
    ),
    # düzey 3
    '0050': patch(
        'Dönem sonunda 621 Satılan Ticari Mallar Maliyeti 280.000 ₺, 632 Genel Yönetim Giderleri 50.000 ₺, 656 Kambiyo Zararları 15.000 ₺ ve 660 Kısa Vadeli Borçlanma Giderleri 20.000 ₺ borç kalanı vermektedir.\n\nBu gider hesaplarının dönem sonu devrine ilişkin doğru kayıt hangisidir?',
        {
            'A': '690 Dönem Kârı veya Zararı 350.000 ₺ borç / 621, 632 ve 660 hesapları 350.000 ₺ alacak; 656 devredilmez',
            'B': '621, 632, 656 ve 660 hesapları toplam 365.000 ₺ borç / 690 Dönem Kârı veya Zararı 365.000 ₺ alacak',
            'C': '690 Dönem Kârı veya Zararı 365.000 ₺ borç / 621, 632, 656 ve 660 hesapları toplam 365.000 ₺ alacak',
            'D': '692 Dönem Net Kârı veya Zararı 365.000 ₺ borç / gider hesapları toplam 365.000 ₺ alacak',
            'E': 'Gider hesapları sonraki döneme devrettiği için kapanış kaydı yapılmaz',
        },
        'C',
        'Borç kalanı veren gider hesapları kapatılırken alacaklandırılır. Toplam gider 280.000 + 50.000 + 15.000 + 20.000 = **365.000 ₺** olduğundan aynı tutar 690 hesabın borcuna yazılır.',
        "1 Sıra No'lu MSUGT - Gider hesaplarının 690 hesaba devri",
    ),
    # düzey 3
    '0051': patch(
        "2025 hesap dönemi kapandıktan sonra, o dönemde sunulmuş ancak kayda alınmamış 30.000 ₺ tutarındaki danışmanlık hizmeti geliri 2026 yılında tespit edilmiştir. Tutar müşteriden alacaklıdır.\n\nTekdüzen Hesap Planı'na göre 2026 yılında yapılacak kayıt hangisidir?",
        {
            'A': '120 Alıcılar 30.000 ₺ borç / 679 Diğer Olağandışı Gelir ve Kârlar 30.000 ₺ alacak',
            'B': '181 Gelir Tahakkukları 30.000 ₺ borç / 649 Diğer Olağan Gelir ve Kârlar 30.000 ₺ alacak',
            'C': '671 Önceki Dönem Gelir ve Kârlar 30.000 ₺ borç / 120 Alıcılar 30.000 ₺ alacak',
            'D': '120 Alıcılar 30.000 ₺ borç / 600 Yurt İçi Satışlar 30.000 ₺ alacak',
            'E': '120 Alıcılar 30.000 ₺ borç / 671 Önceki Dönem Gelir ve Kârlar 30.000 ₺ alacak',
        },
        'E',
        'Gelir cari dönem faaliyetinden değil, kapanmış olan **önceki hesap döneminden** kaynaklanmaktadır. Tekdüzen Hesap Planı uygulamasında alacak 120 hesaba, önceki dönem geliri ise **671 hesaba** kaydedilir.',
        "1 Sıra No'lu MSUGT - 120/671",
    ),
    # düzey 2
    '0052': patch(
        "İşletme, 400.000 ₺ tutarında ve yıllık %18 faizli banka kredisini beş ay kullanmıştır. Faiz basit faiz yöntemiyle hesaplanacak ve tamamı kısa vadeli borçlanma gideri olarak gelir tablosuna yansıtılacaktır.\n\n660 Kısa Vadeli Borçlanma Giderleri hesabına aktarılacak tutar kaç ₺'dir?",
        {
            'A': '30.000',
            'B': '24.000',
            'C': '27.000',
            'D': '36.000',
            'E': '72.000',
        },
        'A',
        'Basit faiz = anapara × yıllık oran × süredir. 400.000 × %18 × 5/12 = **30.000 ₺** faiz gideri hesaplanır ve kısa vadeli borçlanmaya ait olduğu için 660 hesaba aktarılır.',
        "1 Sıra No'lu MSUGT - 660 Kısa Vadeli Borçlanma Giderleri",
    ),
    # düzey 3
    '0053': patch(
        'Aşağıdaki hesaplardan hangileri gelir tablosu (sonuç) hesabıdır?\n\nI. 320 Satıcılar\n\nII. 600 Yurt İçi Satışlar\n\nIII. 632 Genel Yönetim Giderleri (-)',
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'C',
        '**II (600 Yurt İçi Satışlar)** ve **III (632 Genel Yönetim Giderleri)** gelir tablosu (sonuç) hesaplarıdır. **I (320 Satıcılar)** ise bir bilanço (borç) hesabıdır. Doğru cevap **II ve III**.',
        "1 Sıra No'lu MSUGT - 6 grubu vs bilanço",
    ),
    # düzey 2
    '0054': patch(
        "İşletmenin 1 Ekim'de bankaya yatırdığı 300.000 ₺, yıllık %20 faizli vadeli mevduatın faizi vade sonunda tahsil edilecektir. 31 Aralık'ta üç aylık faiz tahakkuku yapılacaktır.\n\nYapılacak kayıt hangisidir?",
        {
            'A': '102 Bankalar 15.000 ₺ borç / 642 Faiz Gelirleri 15.000 ₺ alacak',
            'B': '181 Gelir Tahakkukları 15.000 ₺ borç / 642 Faiz Gelirleri 15.000 ₺ alacak',
            'C': '642 Faiz Gelirleri 15.000 ₺ borç / 181 Gelir Tahakkukları 15.000 ₺ alacak',
            'D': '181 Gelir Tahakkukları 15.000 ₺ borç / 671 Önceki Dönem Gelir ve Kârlar 15.000 ₺ alacak',
            'E': '181 Gelir Tahakkukları 60.000 ₺ borç / 642 Faiz Gelirleri 60.000 ₺ alacak',
        },
        'B',
        "Üç aylık faiz 300.000 × %20 × 3/12 = **15.000 ₺**'dir. Faiz cari dönemde kazanılmış ancak henüz tahsil edilmemiştir; bu nedenle 181 borçlandırılır, 642 alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 181/642; dönemsellik kavramı",
    ),
    # düzey 2
    '0055': patch(
        'Dönem sonu kapanış kayıtlarından sonra 692 Dönem Net Kârı veya Zararı hesabı 260.000 ₺ alacak kalanı vermiştir. İşletme bu sonucu, genel kurul kararıyla dağıtılıncaya kadar bilançoda göstermek üzere aktaracaktır.\n\nDönem sonunda belirlenen dönem net kârı (692) bilançoda hangi hesaba aktarılır?',
        {
            'A': '540 Yasal Yedekler',
            'B': '500 Sermaye',
            'C': '600 Yurt İçi Satışlar',
            'D': '570 Geçmiş Yıllar Kârları',
            'E': '590 Dönem Net Kârı',
        },
        'E',
        'Gelir tablosunda belirlenen **692 Dönem Net Kârı**, bilançodaki özkaynaklar içinde yer alan **590 Dönem Net Kârı** hesabına aktarılır.',
        "1 Sıra No'lu MSUGT - 692 / 590",
    ),
    # düzey 2
    '0056': patch(
        "Esas faaliyet konusu makine üretip satmak olan işletme, ürettiği bir makineyi 250.000 ₺ + %20 KDV ile kredili satmıştır. Makinenin maliyeti 170.000 ₺'dir.\n\nSatış hasılatının kaydında kullanılacak gelir hesabı hangisidir?",
        {
            'A': '645 Menkul Kıymet Satış Kârları',
            'B': '649 Diğer Olağan Gelir ve Kârlar',
            'C': '671 Önceki Dönem Gelir ve Kârlar',
            'D': '679 Diğer Olağandışı Gelir ve Kârlar',
            'E': '600 Yurt İçi Satışlar',
        },
        'E',
        'Makine işletmenin kullanılan duran varlığı değil, **esas faaliyet kapsamında üretilip satılan mamulüdür**. Bu nedenle KDV hariç 250.000 ₺ satış hasılatı 600 Yurt İçi Satışlar hesabına alacak kaydedilir; 679 kullanılmaz.',
        "1 Sıra No'lu MSUGT - 120/391/600; hasılat ile duran varlık satış kârı ayrımı",
    ),
    # düzey 3
    '0057': patch(
        "Bir işletmenin dönem sonu gelir tablosu hesapları şöyledir: 600 Yurt İçi Satışlar 1.200.000 ₺, 610 Satıştan İadeler 50.000 ₺, 611 Satış İskontoları 30.000 ₺, 621 Satılan Ticari Mallar Maliyeti 700.000 ₺, 631 Pazarlama Satış ve Dağıtım Giderleri 80.000 ₺, 632 Genel Yönetim Giderleri 120.000 ₺, 642 Faiz Gelirleri 20.000 ₺, 646 Kambiyo Kârları 15.000 ₺, 654 Karşılık Giderleri 10.000 ₺, 656 Kambiyo Zararları 5.000 ₺, 660 Kısa Vadeli Borçlanma Giderleri 40.000 ₺, 679 Diğer Olağandışı Gelir ve Kârlar 25.000 ₺ ve 689 Diğer Olağandışı Gider ve Zararlar 10.000 ₺. Buna göre olağan kâr kaç ₺'dir?",
        {
            'A': '215.000 ₺',
            'B': '220.000 ₺',
            'C': '210.000 ₺',
            'D': '200.000 ₺',
            'E': '240.000 ₺',
        },
        'D',
        'Net satışlar 1.120.000 ₺; brüt satış kârı 420.000 ₺; faaliyet kârı 220.000 ₺. Olağan kâr = 220.000 + 20.000 + 15.000 − 10.000 − 5.000 − 40.000 = **200.000 ₺**. 67 ve 68 grupları olağan kârdan sonra dikkate alınır: dönem kârı 215.000 ₺.',
        'THP 6 Gelir Tablosu Hesapları; kâr kademeleri',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletmenin dönem içindeki satışları %20 KDV dâhil toplam 1.440.000 ₺, satıştan iadeleri KDV dâhil 60.000 ₺'dir. Başka satış indirimi yoktur. Buna göre gelir tablosunda gösterilecek net satışlar kaç ₺'dir?",
        {
            'A': '1.150.000 ₺',
            'B': '1.200.000 ₺',
            'C': '1.380.000 ₺',
            'D': '1.140.000 ₺',
            'E': '1.100.000 ₺',
        },
        'A',
        'Hasılat KDV hariç tutarla izlenir: brüt satışlar 1.440.000 / 1,20 = 1.200.000 ₺; iadeler 60.000 / 1,20 = 50.000 ₺. Net satışlar 1.200.000 − 50.000 = **1.150.000 ₺**.',
        'THP 600, 610; KDV matrahı',
    ),
    # düzey 3
    '0059': patch(
        'Bir işletmenin gelir tablosu hazırlanmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Finansman giderleri faaliyet kârından sonra düşülür',
            'B': 'Önceki dönem gelirleri 67 grubunda izlenir',
            'C': 'Maddi duran varlık satış kârı faaliyet kârını artırır',
            'D': 'Faiz gelirleri olağan kârı artırır',
            'E': 'Satış iskontoları net satışları azaltır',
        },
        'C',
        "Esas faaliyeti duran varlık ticareti olmayan işletmede MDV satış kârı **679 Diğer Olağandışı Gelir ve Kârlar**'da izlenir; faaliyet kârını değil, olağan kârdan sonra dönem kârını etkiler.",
        'THP 6 Gelir Tablosu',
    ),
    # düzey 2
    '0060': patch(
        'Gelir tablosu hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 610 Satıştan İadeler ve 611 Satış İskontoları net satışları azaltır.\n\nII. 642 Faiz Gelirleri bir finansman gideri hesabıdır.\n\nIII. 689 Diğer Olağandışı Gider ve Zararlar 68 grubunda yer alır.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'B',
        'I ve III doğrudur. II yanlıştır: 642 Faiz Gelirleri 64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar grubunda bir **gelir** hesabıdır.',
        'THP 61, 64, 68',
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
    print(f"1 paket / {len(PATCHES)} soru ('Gelir Tablosu Hesaplari' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
