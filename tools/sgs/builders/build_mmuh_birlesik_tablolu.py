#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Birlesik Maliyet — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Maliyet muhasebesi tablolu tur. Gercek sinavin 10 birlesik maliyet sorusunun 4'u katsayi (esdeger urun) yontemiyle; eski pakette bu yontem hic yoktu. 35 soru korundu (mutlak ifadeli celdiriciler yenilendi); 25 yeni soru, her biri kendi verisiyle: katsayi yontemi (pay, birim maliyet, katsayiyi bulma, miktar yontemiyle karsilastirma), yuzde esit + kalani katsayi/miktar karma dagitim, satis degeri ve net satis hasilati yontemleri (birim pay, toplam pay, ek maliyetli birim maliyet, stok degeri, brut kar ve kar orani, ters hesapla ortak maliyet), kac kati, yan urun (miktar yontemi ve NGD dusulmesi), ilave isleme kararlari. Tutarlar Fraction ile hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Maliyet muhasebesi - birlesik (ortak) urun maliyetlemesi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliyet_muhasebesi/birlesik_maliyet.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (tablolu çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "mmuh-birlesik-gen-"


def patch(stem, options, answer, solution, ref='Maliyet muhasebesi - birleşik maliyet'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "'Birleşik (ortak) üretim' kavramı ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': 'Aynı hammadde/üretim sürecinden aynı anda birden fazla farklı ürünün elde edilmesi',
            'B': 'Tek bir mamulün birbirini izleyen üretim safhalarında adım adım işlenerek tamamlanması',
            'C': 'Farklı tedarikçilerden alınan parçaların montaj hattında tek bir mamulde birleştirilmesi',
            'D': 'Her müşteri siparişinin diğerlerinden bağımsız, ayrı bir parti hâlinde üretilmesi',
            'E': 'Üretilen mamullerin depoda saklanıp sipariş geldikçe müşteriye sevk edilmesi süreci',
        },
        'A',
        '**Birleşik (ortak) üretim**, aynı hammadde/üretim sürecinden **aynı anda birden fazla farklı ürünün** elde edilmesidir (petrol rafinerisi, süt işleme, et işleme vb.).',
        'Maliyet muhasebesi - birleşik üretim',
    ),
    # düzey 2
    '0002': patch(
        "Birleşik maliyetin 'satış değeri (piyasa değeri) esaslı' dağıtımında pay nasıl belirlenir?",
        {
            'A': 'İşletmeye uygulanan kurumlar vergisi oranıyla doğru orantılı olarak belirlenir',
            'B': 'Her ürünün ürettiği fiziki miktar / tüm ürünlerin toplam fiziki üretim miktarı',
            'C': 'Her ürünün kilogram cinsinden ağırlığı / tüm ürünlerin toplam ağırlığı oranı',
            'D': 'Her ürüne düşen amortisman payı / tüm ürünlere ait toplam amortisman tutarı',
            'E': 'Her ürünün (ayrım noktasındaki) satış değeri / toplam satış değeri',
        },
        'E',
        'Satış değeri esaslı dağıtımda pay = **Her ürünün satış değeri ÷ Toplam satış değeri**; bu oran birleşik maliyetle çarpılır. Değeri yüksek ürün daha çok maliyet payı alır.',
        'Maliyet muhasebesi - satış değeri dağıtımı',
    ),
    # düzey 2
    '0003': patch(
        "Birleşik maliyeti 200.000 ₺ olan bir süreçte A 8.000 kg, B 2.000 kg ürün elde edilmiştir. Fiziki ölçü esasına göre dağıtım yapıldığında A ürünü 220.000 ₺'ye satılırsa A'nın brüt kârı kaç ₺'dir?",
        {
            'A': '220.000',
            'B': '160.000',
            'C': '80.000',
            'D': '60.000',
            'E': '20.000',
        },
        'D',
        'Toplam miktar 10.000 kg. A payı = 200.000 × (8.000 ÷ 10.000) = 160.000 ₺. A brüt kârı = 220.000 − 160.000 = **60.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0004': patch(
        "Toplam birleşik maliyeti 200.000 ₺ olan bir süreçte A ürününden 3.000 birim (birim fiyat 100 ₺), B ürününden 2.000 birim (birim fiyat 100 ₺) üretilmiştir. Satış değeri esasına göre A ürününe düşen pay kaç ₺'dir?",
        {
            'A': '160.000',
            'B': '120.000',
            'C': '140.000',
            'D': '60.000',
            'E': '200.000',
        },
        'B',
        'Satış değerleri: A = 3.000 × 100 = 300.000 ₺; B = 2.000 × 100 = 200.000 ₺; toplam = 500.000 ₺. A payı = 200.000 × (300.000 ÷ 500.000) = **120.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0005': patch(
        "Birleşik maliyeti 90.000 ₺ olan bir süreçte X 3.000 kg, Y 6.000 kg ve Z 1.000 kg ürün elde edilmiştir. Fiziki ölçü esasına göre Y ürününün BİRİM (kg) maliyeti kaç ₺'dir?",
        {
            'A': '5',
            'B': '54.000',
            'C': '12',
            'D': '15',
            'E': '9',
        },
        'E',
        'Toplam miktar = 3.000 + 6.000 + 1.000 = 10.000 kg. Y payı = 90.000 × (6.000 ÷ 10.000) = 54.000 ₺. Y birim = 54.000 ÷ 6.000 = **9 ₺/kg**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0006': patch(
        "Birleşik maliyeti 150.000 ₺ olan süreçte M ve N ürünleri elde edilir. M NGD 200.000 ₺, N NGD 100.000 ₺'dir. N ürünü 2.000 birim ise N ürününün BİRİM birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '75',
            'B': '100',
            'C': '25',
            'D': '50',
            'E': '20',
        },
        'C',
        'Toplam NGD = 300.000 ₺. N payı = 150.000 × (100.000 ÷ 300.000) = 50.000 ₺. N birim = 50.000 ÷ 2.000 = **25 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0007': patch(
        'Birleşik maliyet dağıtımı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiziki ölçü yönteminde pay, ürün miktarı / toplam miktar oranıyla bulunur.\n\nII. Satış değeri yönteminde pay, ürün satış değeri / toplam satış değeri oranıyla bulunur.\n\nIII. Dağıtım yöntemi değiştikçe toplam birleşik maliyet de değişir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        '**III yanlıştır:** Toplam **birleşik (ortak) maliyet**, ayrım noktasına kadar oluşan sabit bir tutardır; dağıtım yöntemi değişse **değişmez**, yalnızca bu maliyetin ürünlere düşen **payları** değişir. **I** fiziki ölçü payı = miktar/toplam miktar; **II** satış değeri payı = satış değeri/toplam satış değeri. Doğru cevap **I ve II**.',
        'Maliyet muhasebesi - dağıtım yöntemleri',
    ),
    # düzey 2
    '0008': patch(
        "Birleşik maliyeti 180.000 ₺ olan süreçte A ve B ürünleri elde edilir. A: nihai satış 200.000 ₺, ayrım sonrası ilave işleme 50.000 ₺; B: nihai satış 120.000 ₺, ilave işleme 30.000 ₺. Net gerçekleşebilir değer (NGD) esasına göre A'ya düşen pay kaç ₺'dir?",
        {
            'A': '67.500',
            'B': '112.500',
            'C': '90.000',
            'D': '150.000',
            'E': '120.000',
        },
        'B',
        'NGD = nihai satış − ilave işleme. A NGD = 200.000 − 50.000 = 150.000 ₺; B NGD = 120.000 − 30.000 = 90.000 ₺; toplam 240.000 ₺. A payı = 180.000 × (150.000 ÷ 240.000) = **112.500 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0009': patch(
        "Bir ürün ayrım noktasında 100.000 ₺'ye satılabilmektedir. İlave işlemeyle 150.000 ₺'ye satılabilecek; ilave işleme maliyeti 30.000 ₺'dir. İlave işleme yapılmalı mıdır?",
        {
            'A': 'Evet; ilave gelir (50.000 ₺) ilave maliyetten (30.000 ₺) büyük olduğundan 20.000 ₺ ek kâr sağlar',
            'B': 'Evet; ilave işleme yapılmalıdır, ancak birleşik maliyet de hesaba katıldığında karar net 30.000 ₺ zarar doğurur',
            'C': 'Bu verilerle karar verilemez; ilave işlemenin kârlı olup olmadığı eldeki bilgilerle belirlenemez',
            'D': 'Hayır; ayrım noktasına kadar oluşan birleşik maliyet çok yüksek olduğu için ilave işleme yapılması doğru olmaz',
            'E': 'Hayır; sağlanan ilave gelir katlanılan ilave işleme maliyetinden küçük kaldığı için ilave işleme yapılmamalıdır',
        },
        'A',
        'İlave gelir = 150.000 − 100.000 = 50.000 ₺. İlave maliyet = 30.000 ₺. İlave gelir > ilave maliyet → **ilave işleme yapılmalı** (50.000 − 30.000 = 20.000 ₺ ek kâr). Birleşik maliyet karara dahil edilmez.',
        'Maliyet muhasebesi - ilave işleme kararı',
    ),
    # düzey 2
    '0010': patch(
        "Bir birleşik ürün ayrım noktasında 100.000 ₺'ye satılabilmektedir. İlave işlemeden geçirilirse 150.000 ₺'ye satılabilecek, ilave işleme maliyeti 30.000 ₺ olacaktır. Doğru karar ve net etkisi nedir?",
        {
            'A': 'Fark etmez; iki seçenek eşittir',
            'B': 'İlave işlenmemeli; birleşik maliyet 100.000 ₺ aşılır',
            'C': 'İlave işlenmemeli; net 30.000 ₺ zarar eder',
            'D': 'İlave işlenmeli; net 50.000 ₺ katkı sağlar',
            'E': 'İlave işlenmeli; net 20.000 ₺ katkı sağlar',
        },
        'E',
        'Karar ayrım sonrası verilere göre verilir (birleşik maliyet batmıştır, dikkate alınmaz). Ek gelir = 150.000 − 100.000 = 50.000 ₺; ek maliyet = 30.000 ₺. Ek gelir > ek maliyet olduğundan ilave işlenmeli; net katkı = 50.000 − 30.000 = **20.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdakilerden hangisi birleşik maliyet konusuyla ilgili YANLIŞ bir ifadedir?',
        {
            'A': 'İlave işleme kararında birleşik maliyet dikkate alınmaz (batık maliyettir)',
            'B': 'Yan ürünün net değeri ana ürün maliyetinden düşülebilir',
            'C': 'Satış değeri yöntemi değeri yüksek ürüne daha çok maliyet yükler',
            'D': 'Birleşik maliyet dağıtım yöntemi değiştiğinde toplam birleşik maliyet de değişir',
            'E': 'Birleşik maliyet ayrım noktasına kadarki ortak maliyettir',
        },
        'D',
        'Yanlış ifade, dağıtım yöntemiyle ilgili olandır: dağıtım yöntemi değişse de ürünlere düşen paylar değişebilir ama **toplam birleşik maliyet DEĞİŞMEZ**. Diğer ifadeler doğrudur.',
        'Maliyet muhasebesi - birleşik maliyet',
    ),
    # düzey 2
    '0012': patch(
        "Birleşik maliyeti 240.000 ₺ olan süreçte P ve Q ürünleri elde edilir. P: nihai satış 300.000 ₺, ilave işleme 60.000 ₺; Q: nihai satış 200.000 ₺, ilave işleme 40.000 ₺. NGD esasına göre P'ye düşen pay kaç ₺'dir?",
        {
            'A': '144.000',
            'B': '108.000',
            'C': '96.000',
            'D': '138.000',
            'E': '120.000',
        },
        'A',
        'P NGD = 300.000 − 60.000 = 240.000 ₺; Q NGD = 200.000 − 40.000 = 160.000 ₺; toplam 400.000 ₺. P payı = 240.000 × (240.000 ÷ 400.000) = **144.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 3
    '0013': patch(
        "Birleşik bir süreçten R ürünü 12.000 litre, S ürünü 4.000 litre ve T ürünü 2.000 litre olarak elde edilmektedir. Ürünlerin yoğunluk ve işçilik özelliklerine göre belirlenen katsayılar sırasıyla 1, 2 ve 4'tür. Dönemin birleşik gideri 504.000 ₺ olduğuna göre katsayı yöntemine göre S ürününün litre başına maliyeti kaç ₺'dir?",
        {
            'A': '2',
            'B': '28',
            'C': '36',
            'D': '16',
            'E': '18',
        },
        'C',
        "Eşdeğer miktar = 12.000 × 1 + 4.000 × 2 + 2.000 × 4 = 28.000. Eşdeğer birim başına gider = 504.000 ÷ 28.000 = 18 ₺. S'nin bir litresi 2 eşdeğer birim sayıldığından birim maliyeti 18 × 2 = **36 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (katsayı yöntemi)',
    ),
    # düzey 3
    '0014': patch(
        "Bir işletme A, B ve C mamullerini 324.000 ₺ ortak maliyete katlanarak üretmekte; mamullerin üretimini ayrılma noktasından sonra ek maliyetlerle tamamlamaktadır. Döneme ait veriler şöyledir:\n\n| Mamul | Üretim (birim) | Satış fiyatı (₺) | Ek maliyet (₺) |\n|---|---|---|---|\n| A | 1.000 | 150 | 30.000 |\n| B | 2.000 | 180 | 60.000 |\n| C | 1.500 | 240 | 60.000 |\n\nNet satış hasılatı yöntemine göre A mamulünün ortak maliyetten birim başına aldığı pay kaç ₺'dir?",
        {
            'A': '90',
            'B': '54',
            'C': '67,50',
            'D': '72',
            'E': '84',
        },
        'B',
        'Net satış hasılatı = satış değeri − ek maliyet: A 150.000 − 30.000 = 120.000; B 300.000; C 300.000; toplam 720.000 ₺. Oran 324.000 ÷ 720.000 = 0,45. A payı 120.000 × 0,45 = 54.000 ₺; birim başına 54.000 ÷ 1.000 = **54 ₺**. Ek maliyet ortak maliyet payına dahil değildir.',
        'Maliyet muhasebesi - birleşik maliyet (net satış hasılatı yöntemi)',
    ),
    # düzey 3
    '0015': patch(
        "Birleşik gideri 512.000 ₺ olan bir süreçten X ana ürünü 3.000 kg, Y ana ürünü 2.000 kg ve Z yan ürünü 800 kg olarak elde edilmiştir. Z'nin satış fiyatı kg başına 18 ₺ olup satışı için 2.400 ₺ pazarlama gideri yapılacaktır. İşletme yan ürünün net gerçekleşebilir değerini birleşik giderden düşmekte, kalanı ana ürünlere üretim miktarı yöntemiyle dağıtmaktadır. Buna göre Y ürününün birleşik gider payı kaç ₺'dir?",
        {
            'A': '188.000',
            'B': '100.000',
            'C': '199.040',
            'D': '195.200',
            'E': '200.000',
        },
        'E',
        "Z'nin net gerçekleşebilir değeri = 800 × 18 − 2.400 = 12.000 ₺. Ana ürünlere kalan = 512.000 − 12.000 = 500.000 ₺. Y payı = 500.000 × 2.000 ÷ 5.000 = **200.000 ₺**. Pazarlama giderini düşmemek 199.040 ₺ verir.",
        'Maliyet muhasebesi - birleşik maliyet (yan ürün)',
    ),
    # düzey 3
    '0016': patch(
        "Bir ortak üretim sürecinde dönemin giderleri şöyledir:\n\n| Gider | Tutar (₺) |\n|---|---|\n| Direkt ilk madde ve malzeme | 280.000 |\n| Direkt işçilik | 150.000 |\n| Genel üretim | 170.000 |\n\nSüreçten A ürünü 2.000 kg (150 ₺/kg), B ürünü 3.000 kg (100 ₺/kg) ve C ürünü 1.000 kg (400 ₺/kg) olarak elde edilmiştir. Satış değeri yöntemine göre C ürününün kg başına maliyeti kaç ₺'dir?",
        {
            'A': '112',
            'B': '172',
            'C': '100',
            'D': '240',
            'E': '400',
        },
        'D',
        'Ortak maliyet = 280.000 + 150.000 + 170.000 = 600.000 ₺. Satış değerleri A 300.000, B 300.000, C 400.000; toplam 1.000.000 ₺. C payı = 600.000 × 0,40 = 240.000 ₺; kg başına **240 ₺**. Ortak maliyet üç unsurun toplamıdır; genel üretim gideri dışarıda bırakılamaz.',
        'Maliyet muhasebesi - birleşik maliyet (satış değeri yöntemi)',
    ),
    # düzey 3
    '0017': patch(
        "150.000 ₺ birleşik maliyetle X ürünü 1.000 kg (satış fiyatı 90 ₺/kg) ve Y ürünü 2.000 kg (satış fiyatı 30 ₺/kg) olarak üretilmiştir. Buna göre aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üretim miktarı yöntemine göre Y ürününün payı 60.000 ₺'dir.\n\nII. Satış değeri yöntemine göre X ürününün payı 90.000 ₺'dir.\n\nIII. Satış değeri yöntemine göre Y ürününün kg başına maliyeti 50 ₺'dir.",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'B',
        "**I yanlıştır:** miktar yönteminde Y payı 150.000 × 2/3 = 100.000 ₺'dir; 60.000 ₺ satış değeri yönteminin sonucudur. **II doğrudur:** satış değerleri X 90.000, Y 60.000; X payı 150.000 × 90/150 = 90.000 ₺. **III yanlıştır:** satış değeri yönteminde Y payı 60.000 ₺, kg başına 30 ₺'dir. Doğru cevap **Yalnız II**.",
        'Maliyet muhasebesi - birleşik maliyet (yöntem karşılaştırması)',
    ),
    # düzey 3
    '0018': patch(
        "300.000 ₺ ortak maliyetle üretilen A, B ve C mamulleri ayrılma noktasından sonra ek maliyetlerle tamamlanmaktadır:\n\n| Mamul | Üretim (birim) | Satış fiyatı (₺) | Ek maliyet (₺) |\n|---|---|---|---|\n| A | 2.000 | 90 | 30.000 |\n| B | 1.600 | 150 | 40.000 |\n| C | 1.000 | 250 | 100.000 |\n\nNet satış hasılatı yöntemine göre B mamulünün birim başına toplam üretim maliyeti kaç ₺'dir?",
        {
            'A': '125',
            'B': '200',
            'C': '100',
            'D': '150',
            'E': '175',
        },
        'C',
        "Net satış hasılatları: A 150.000, B 200.000, C 150.000; toplam 500.000 ₺. B'nin ortak maliyet payı 300.000 × 0,40 = 120.000 ₺. Toplam üretim maliyeti = ortak pay + ek maliyet = 120.000 + 40.000 = 160.000 ₺; birim başına **100 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (net satış hasılatı yöntemi)',
    ),
    # düzey 3
    '0019': patch(
        '180.000 ₺ ortak maliyetle üretilen K ve L ürünleri ayrılma noktasında satılabileceği gibi ilave işlemden sonra da satılabilmektedir:\n\n| Ürün | SD₁ (₺) | SD₂ (₺) | İİM (₺) |\n|---|---|---|---|\n| K | 200.000 | 260.000 | 70.000 |\n| L | 80.000 | 150.000 | 40.000 |\n\nSD₁: ayrılma noktasındaki satış değeri · SD₂: ilave işlem sonrası satış değeri · İİM: ilave işleme maliyeti\n\nBuna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Her iki ürün de ilave işlemden geçirilirse toplam kâr 140.000 ₺ olur.',
            'B': 'En kârlı kararla toplam kâr 130.000 ₺ olur.',
            'C': 'L ürününün ilave işlenmesi kârı 30.000 ₺ artırır.',
            'D': 'Karar verilirken 180.000 ₺ ortak maliyet dikkate alınmaz.',
            'E': 'K ürünü ayrılma noktasında satılmalıdır.',
        },
        'A',
        "İkisi de işlenirse kâr = 190.000 + 110.000 − 180.000 = 120.000 ₺'dir; 140.000 ₺ yanlıştır. Diğerleri doğrudur: K'nin ek geliri 60.000 < ek maliyet 70.000 (ayrılma noktasında satılır); L'nin net katkısı 70.000 − 40.000 = 30.000 ₺; en iyi kâr 200.000 + 110.000 − 180.000 = 130.000 ₺; ortak maliyet batık maliyettir.",
        'Maliyet muhasebesi - birleşik maliyet (ilave işleme kararı)',
    ),
    # düzey 3
    '0020': patch(
        "Satış değeri yöntemini kullanan bir işletmenin ortak üretim sürecinden elde ettiği ürünler şöyledir:\n\n| Ürün | Üretim (adet) | Satış fiyatı (₺) |\n|---|---|---|\n| A | 2.000 | 75 |\n| B | 1.000 | 150 |\n| C | 500 | 200 |\n\nA ürününe ortak maliyetten 120.000 ₺ pay düştüğüne göre dönemin toplam ortak maliyeti kaç ₺'dir?",
        {
            'A': '430.000',
            'B': '360.000',
            'C': '320.000',
            'D': '400.000',
            'E': '370.000',
        },
        'C',
        "Satış değerleri A 150.000, B 150.000, C 100.000; toplam 400.000 ₺. A'nın oranı 150.000 ÷ 400.000 = %37,5. Toplam ortak maliyet = 120.000 ÷ 0,375 = **320.000 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (satış değeri yöntemi)',
    ),
    # düzey 2
    '0021': patch(
        "Birleşik üretimde 'ayrım noktası (split-off point)' kavramı ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': 'Sabit kıymetler için yıllık amortisman payının ayrılıp gider olarak yazıldığı belirli gün',
            'B': 'Üretimde kullanılacak hammaddenin satın alınıp tedarikçiden işletme deposuna giriş yaptığı aşama',
            'C': 'Birleşik ürünlerin birbirinden ayrılıp tanımlanabilir hale geldiği üretim aşaması',
            'D': 'Dönem sonunda hesaplanan kurumlar vergisinin tahakkuk ettirilip kayda alındığı zaman noktası',
            'E': 'Mamullerin işletme deposundan çıkıp müşteriye teslim edildiği ve satış hasılatının doğduğu an',
        },
        'C',
        "**Ayrım noktası (split-off point)**, birleşik ürünlerin ortak süreçten çıkıp **birbirinden ayrılarak tanımlanabilir** hale geldiği üretim aşamasıdır. Bu noktaya kadarki maliyet 'birleşik maliyettir'.",
        'Maliyet muhasebesi - ayrım noktası',
    ),
    # düzey 2
    '0022': patch(
        'Aşağıdakilerden hangisi birleşik maliyet dağıtım yöntemi DEĞİLDİR?',
        {
            'A': 'Net gerçekleşebilir değer (NGD) esaslı yöntem',
            'B': 'Fiziki ölçü (miktar) esaslı yöntem',
            'C': 'Bunlardan biri değil (hepsi yöntemdir)',
            'D': 'Enflasyon düzeltmesi yöntemi',
            'E': 'Satış değeri (piyasa değeri) esaslı yöntem',
        },
        'D',
        'Birleşik maliyet dağıtımında fiziki ölçü, satış değeri ve NGD yöntemleri kullanılır. **Enflasyon düzeltmesi** bir birleşik maliyet dağıtım yöntemi değildir.',
        'Maliyet muhasebesi - dağıtım yöntemleri',
    ),
    # düzey 2
    '0023': patch(
        'Birleşik ve yan ürün maliyetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Birleşik (ortak) maliyet, ayrım noktasından sonra ortaya çıkan ve her ürüne ayrı ayrı yüklenebilen maliyettir.\n\nII. Ana ürün yüksek, yan ürün düşük değerlidir.\n\nIII. Birleşik maliyet fiziki ölçü veya satış değeri esasına göre dağıtılabilir.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'C',
        '**I yanlıştır:** Birleşik (ortak) maliyet, ayrım (split-off) noktasına KADAR oluşan ve ürünlere ortak olan maliyettir; ayrım noktasından SONRA ortaya çıkanlar ise her ürüne ayrı yüklenen ilave (ayrılabilir) maliyettir. **II** ana ürünün yüksek/yan ürünün düşük değerli olması ve **III** birleşik maliyetin fiziki ölçü veya satış değeri esasına göre dağıtılabilmesi doğrudur. Doğru cevap **II ve III**.',
        'Maliyet muhasebesi - birleşik/yan ürün',
    ),
    # düzey 2
    '0024': patch(
        "Birleşik maliyeti 240.000 ₺ olan süreçte A ve B elde edilir. A NGD 180.000 ₺, B NGD 60.000 ₺'dir. A ürünü 3.000 birim ise A'nın BİRİM birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '100',
            'B': '80',
            'C': '90',
            'D': '75',
            'E': '60',
        },
        'E',
        'Toplam NGD = 240.000 ₺. A payı = 240.000 × (180.000 ÷ 240.000) = 180.000 ₺. A birim = 180.000 ÷ 3.000 = **60 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0025': patch(
        "Birleşik maliyeti 480.000 ₺ olan bir süreçte P ürününden 5.000 birim (birim fiyat 100 ₺), Q ürününden 3.000 birim (birim fiyat 100 ₺) üretilmiştir. Satış değeri esasına göre Q ürününün BİRİM maliyeti kaç ₺'dir?",
        {
            'A': '90',
            'B': '84',
            'C': '100',
            'D': '60',
            'E': '72',
        },
        'D',
        'Satış değerleri: P = 500.000 ₺, Q = 300.000 ₺, toplam 800.000 ₺. Q payı = 480.000 × (300.000 ÷ 800.000) = 180.000 ₺. Q birim maliyeti = 180.000 ÷ 3.000 = **60 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0026': patch(
        'Birleşik maliyeti 120.000 ₺ olan süreçte A 2.000 kg (satış değeri 300.000 ₺), B 6.000 kg (satış değeri 100.000 ₺) elde edilmiştir. A ürününe düşen pay, satış değeri yöntemine göre fiziki ölçü yöntemine göre olandan kaç ₺ FAZLADIR?',
        {
            'A': '120.000',
            'B': '90.000',
            'C': '60.000',
            'D': '30.000',
            'E': '45.000',
        },
        'C',
        "Fiziki ölçü: A payı = 120.000 × (2.000 ÷ 8.000) = 30.000 ₺. Satış değeri: A payı = 120.000 × (300.000 ÷ 400.000) = 90.000 ₺. Fark = 90.000 − 30.000 = **60.000 ₺** (satış değeri yöntemi A'ya daha fazla pay verir).",
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0027': patch(
        'Birleşik maliyeti 150.000 ₺ olan süreçte M 5.000 kg (satış değeri 200.000 ₺), N 5.000 kg (satış değeri 100.000 ₺) elde edilmiştir. M ürününe düşen pay, satış değeri yöntemi ile fiziki ölçü yöntemi arasında kaç ₺ FARK eder?',
        {
            'A': '50.000',
            'B': '0',
            'C': '25.000',
            'D': '100.000',
            'E': '75.000',
        },
        'C',
        'Fiziki ölçü: M payı = 150.000 × (5.000 ÷ 10.000) = 75.000 ₺. Satış değeri: M payı = 150.000 × (200.000 ÷ 300.000) = 100.000 ₺. Fark = 100.000 − 75.000 = **25.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0028': patch(
        "'Net gerçekleşebilir değer (NGD)' aşağıdakilerden hangisiyle hesaplanır?",
        {
            'A': 'Ayrım noktasına kadarki birleşik maliyet − ilave işleme maliyeti',
            'B': 'Ayrım sonrası (ilave işleme) maliyeti − ürünün nihai satış değeri',
            'C': 'Nihai satış değeri + ilave işleme maliyeti',
            'D': 'Nihai satış değeri − ayrım sonrası (ilave işleme) maliyeti',
            'E': 'Ürünün nihai satış değerinin iki katı (satış değeri × 2) tutarı',
        },
        'D',
        '**Net gerçekleşebilir değer (NGD) = Nihai satış değeri − Ayrım sonrası (ilave işleme) maliyeti**. Ayrım noktasında satış değeri bilinmeyen ürünler için dağıtım anahtarı olarak kullanılır.',
        'Maliyet muhasebesi - net gerçekleşebilir değer',
    ),
    # düzey 2
    '0029': patch(
        'Yan ürünün muhasebeleştirilmesinde yaygın bir yaklaşım aşağıdakilerden hangisidir?',
        {
            'A': 'Yan ürün ne stok değeri ne de gelir olarak işletmenin muhasebe kayıtlarına yansıtılmadan geçilir',
            'B': 'Yan ürün, ana ürünle eşit değerli sayılıp bağımsız bir ana ürünmüş gibi ayrı stok hesabında muhasebeleştirilir',
            'C': 'Yan ürünün satış değeri ana ürünün birleşik maliyetine eklenerek ana ürün maliyeti artırılır',
            'D': 'Yan ürüne, ana üründen daha büyük bir birleşik maliyet payı yüklenerek yan ürünün maliyeti bilinçli biçimde kabartılır',
            'E': 'Yan ürünün net gerçekleşebilir değeri, ana ürünün birleşik maliyetinden düşülür (veya diğer gelir olarak kaydedilir)',
        },
        'E',
        'Yaygın yaklaşımda yan ürünün **net gerçekleşebilir değeri ana ürünün birleşik maliyetinden düşülür** (böylece ana ürün maliyeti azalır) ya da satıldığında **diğer gelir** olarak kaydedilir. Yan ürüne büyük bir birleşik maliyet payı verilmez.',
        'Maliyet muhasebesi - yan ürün muhasebesi',
    ),
    # düzey 2
    '0030': patch(
        "Bir ürün ayrım noktasında 80.000 ₺'ye satılabilmektedir. İlave işlemeyle 110.000 ₺'ye satılabilecek; ilave işleme maliyeti 40.000 ₺'dir. Doğru karar hangisidir?",
        {
            'A': 'Bu verilerle karar verilemez; ilave işlemenin kârlı olup olmadığı eldeki bilgilerle hesaplanarak belirlenemez',
            'B': 'İlave işleme yapılmamalı; ilave gelir (30.000 ₺) ilave maliyetten (40.000 ₺) küçük, 10.000 ₺ zarar',
            'C': 'İlave işleme yapılmalı; sağlanan ilave gelirin tamamı ek kâr olarak kalacağından toplam 30.000 ₺ ek kâr elde edilir',
            'D': 'İlave işleme yapılmalı; ilave gelir ile ilave maliyet birbirine eşit olduğundan karar kârı etkilemez',
            'E': 'İlave işleme yapılmalı; sağlanan ilave gelir katlanılan ilave maliyeti aştığından işletmeye 10.000 ₺ ek kâr sağlar',
        },
        'B',
        'İlave gelir = 110.000 − 80.000 = 30.000 ₺. İlave maliyet = 40.000 ₺. İlave gelir < ilave maliyet → **ilave işleme yapılmamalı** (yapılırsa 30.000 − 40.000 = 10.000 ₺ zarar). Ayrım noktasında satmak daha kârlıdır.',
        'Maliyet muhasebesi - ilave işleme kararı',
    ),
    # düzey 2
    '0031': patch(
        "A ürününe düşen birleşik maliyet payı 200.000 ₺, A ürününün ayrım sonrası ilave işleme maliyeti 50.000 ₺'dir. A ürününün toplam maliyeti kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '150.000',
            'C': '250.000',
            'D': '50.000',
            'E': '100.000',
        },
        'C',
        'A ürününün toplam maliyeti = birleşik maliyet payı + ayrım sonrası maliyet = 200.000 + 50.000 = **250.000 ₺**.',
        'Maliyet muhasebesi - ürün toplam maliyeti',
    ),
    # düzey 2
    '0032': patch(
        'Birleşik ve yan ürün maliyetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. NGD = nihai satış değeri − ayrım sonrası işleme maliyeti.\n\nII. Yan ürünün net değeri, ana ürünün birleşik maliyetine eklenerek ana ürünün maliyeti artırılır.\n\nIII. İlave işleme kararında birleşik maliyet batık maliyet olup dikkate alınmaz.',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'A',
        '**II yanlıştır:** Yan ürünün net (gerçekleşebilir) değeri ana ürünün birleşik maliyetine EKLENMEZ; tersine ana ürünün maliyetinden DÜŞÜLÜR (ya da diğer gelir yazılır) ve ana ürün maliyetini AZALTIR. **I** NGD = nihai satış değeri − ayrım sonrası işleme maliyeti ve **III** ilave işleme kararında birleşik maliyetin batık (dikkate alınmaz) olması doğrudur. Doğru cevap **I ve III**.',
        'Maliyet muhasebesi - birleşik/yan ürün',
    ),
    # düzey 3
    '0033': patch(
        "Bir işletmede M1, M2 ve M3 ortak ürünleri için toplanan birleşik gider 300.000 ₺'dir. Ürünlerin üretim miktarları sırasıyla 4.000, 3.000 ve 2.000 adet; katsayıları 1, 2 ve 3'tür. İşletme birleşik giderin %40'ını ürünlere eşit olarak dağıtmakta, kalanını katsayı yöntemiyle dağıtmaktadır. Buna göre M3 ürününün birleşik gider payı kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '80.000',
            'C': '67.500',
            'D': '102.500',
            'E': '107.500',
        },
        'E',
        'Eşit dağıtılan kısım 300.000 × %40 = 120.000 ₺ → ürün başına 40.000 ₺. Kalan 180.000 ₺ katsayıyla: eşdeğer miktar 4.000 + 6.000 + 6.000 = 16.000; M3 payı 180.000 × 6.000 ÷ 16.000 = 67.500 ₺. Toplam 40.000 + 67.500 = **107.500 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (katsayı yöntemi)',
    ),
    # düzey 3
    '0034': patch(
        "70.000 ₺ ortak maliyete katlanılarak toplam 1.000 kg üretim yapılan bir işletmede fiziksel miktarlara göre dağıtım yapıldığında ortak maliyetin %80'inin satış fiyatı 60 ₺ olan A ürününe, %20'sinin ise satış fiyatı 40 ₺ olan B ürününe ait olduğu hesaplanmıştır. Satış değeri yöntemi benimsenirse A ürününün ortak maliyetten alacağı pay, B ürününün alacağı payın kaç katı olur?",
        {
            'A': '6',
            'B': '1',
            'C': '3',
            'D': '4',
            'E': '1,5',
        },
        'A',
        "Fiziksel paylardan miktarlar bulunur: A 800 kg, B 200 kg. Satış değerleri: A 800 × 60 = 48.000 ₺, B 200 × 40 = 8.000 ₺. Paylar satış değeriyle orantılıdır: 48.000 ÷ 8.000 = **6 katı** (A 60.000 ₺, B 10.000 ₺). Fiziksel yöntemde oran 4, yalnız fiyat oranı 1,5'tir.",
        'Maliyet muhasebesi - birleşik maliyet (yöntem karşılaştırması)',
    ),
    # düzey 3
    '0035': patch(
        'Bir işletme ortak üretim sürecinden A, B ve C ürünlerini elde etmektedir. Ürünler ayrılma noktasında satılabileceği gibi ilave işlemden geçirilerek de satılabilmektedir:\n\n| Ürün | SD₁ (₺) | SD₂ (₺) | İİM (₺) |\n|---|---|---|---|\n| A | 90.000 | 140.000 | 40.000 |\n| B | 120.000 | 150.000 | 35.000 |\n| C | 60.000 | 100.000 | 30.000 |\n\nSD₁: ayrılma noktasındaki satış değeri · SD₂: ilave işlem sonrası satış değeri · İİM: ilave işleme maliyeti\n\nKârı en yüksek kılmak isteyen işletme hangi ürünleri ilave işlemden geçirmelidir?',
        {
            'A': 'A, B ve C ürünlerinin üçü',
            'B': 'B ürünü',
            'C': 'A ürünü',
            'D': 'A ve C ürünleri',
            'E': 'B ve C ürünleri',
        },
        'D',
        'Karar ek gelir ile ek maliyetin karşılaştırılmasına dayanır (ortak maliyet batık maliyettir): A 140.000 − 90.000 = 50.000 > 40.000 → +10.000 ₺; B 30.000 < 35.000 → −5.000 ₺; C 40.000 > 30.000 → +10.000 ₺. İlave işlenmesi gerekenler **A ve C**; B ayrılma noktasında satılmalıdır.',
        'Maliyet muhasebesi - birleşik maliyet (ilave işleme kararı)',
    ),
    # düzey 3
    '0036': patch(
        'Katsayı yöntemini kullanan bir işletmede 180.000 ₺ birleşik gider K, L ve M ortak ürünlerine dağıtılmaktadır. K ürününden 3.000 adet (katsayı 2), L ürününden 2.000 adet, M ürününden 1.000 adet (katsayı 4) üretilmiştir. L ürününün birleşik gider payı 67.500 ₺ olarak hesaplandığına göre L ürününün katsayısı kaçtır?',
        {
            'A': '1,5',
            'B': '2',
            'C': '2,5',
            'D': '4',
            'E': '3',
        },
        'E',
        "Eşdeğer birim başına gider g, L'nin katsayısı x olsun. K ve M'nin eşdeğeri 6.000 + 4.000 = 10.000; bunlara düşen pay 180.000 − 67.500 = 112.500 ₺ → g = 112.500 ÷ 10.000 = 11,25 ₺. L'nin eşdeğeri 67.500 ÷ 11,25 = 6.000 → x = 6.000 ÷ 2.000 = **3**.",
        'Maliyet muhasebesi - birleşik maliyet (katsayı yöntemi)',
    ),
    # düzey 3
    '0037': patch(
        'Bir ortak üretim sürecinde direkt ilk madde ve malzeme 200.000 ₺, direkt işçilik 120.000 ₺ ve genel üretim 160.000 ₺ gider oluşmuş; P ürünü 4.000 kg (60 ₺/kg) ve R ürünü 2.000 kg (180 ₺/kg) olarak elde edilmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Üretim miktarı yöntemine göre P ürününün kg başına maliyeti 120 ₺'dir.",
            'B': "Üretim miktarı yöntemine göre R ürününün payı 160.000 ₺'dir.",
            'C': "Satış değeri yöntemine göre P ürününün payı 192.000 ₺'dir.",
            'D': "Ürünlerin toplam satış değeri 600.000 ₺'dir.",
            'E': "Satış değeri yöntemine göre R ürününün kg başına maliyeti 144 ₺'dir.",
        },
        'A',
        "Ortak maliyet 480.000 ₺. Üretim miktarı yönteminde kg başına maliyet 480.000 ÷ 6.000 = 80 ₺'dir; 120 ₺ yanlıştır. Diğerleri doğrudur: satış değerleri 240.000 + 360.000 = 600.000 ₺; P payı 480.000 × 0,40 = 192.000 ₺; R payı 288.000 ₺ → kg başına 144 ₺; miktar yönteminde R 480.000 × 2/6 = 160.000 ₺.",
        'Maliyet muhasebesi - birleşik maliyet (yöntem karşılaştırması)',
    ),
    # düzey 3
    '0038': patch(
        "XYZ İşletmesinde A, B ve C mamulleri ortak maliyetlere katlanılarak üretilmektedir. Dönemin ortak maliyeti 480.000 ₺ olup diğer veriler aşağıdaki gibidir:\n\n| Mamul | Üretim miktarı | Satış fiyatı |\n|---|---|---|\n| A | 1.500 kg | 120 ₺/kg |\n| B | 2.500 kg | 90 ₺/kg |\n| C | 1.000 kg | 195 ₺/kg |\n\nSatış değeri yöntemine göre C mamulünün ortak maliyetten aldığı pay kaç ₺'dir?",
        {
            'A': '168.000',
            'B': '160.000',
            'C': '156.000',
            'D': '195.000',
            'E': '216.000',
        },
        'C',
        'Satış değerleri: A 180.000, B 225.000, C 195.000; toplam 600.000 ₺. Oran 480.000 ÷ 600.000 = 0,80. C payı = 195.000 × 0,80 = **156.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (satış değeri yöntemi)',
    ),
    # düzey 3
    '0039': patch(
        "Bir süreçte 630.000 ₺ birleşik maliyetle 6.000 kg A ana ürünü ile net gerçekleşebilir değeri 30.000 ₺ olan Z yan ürünü elde edilmiştir. İşletme yan ürünün net gerçekleşebilir değerini ana ürünün maliyetinden düşmektedir. Buna göre A ürününün kg başına maliyeti kaç ₺'dir?",
        {
            'A': '195',
            'B': '100',
            'C': '115',
            'D': '110',
            'E': '105',
        },
        'B',
        'Ana ürüne kalan maliyet = 630.000 − 30.000 = 600.000 ₺; kg başına 600.000 ÷ 6.000 = **100 ₺**. Yan ürün gelirini diğer gelir olarak kaydeden yöntemde ise ana ürün maliyeti 105 ₺/kg kalırdı.',
        'Maliyet muhasebesi - birleşik maliyet (yan ürün)',
    ),
    # düzey 3
    '0040': patch(
        "216.000 ₺ ortak maliyetle A ve B ürünleri üretilmiştir. A ayrılma noktasında birim başına 50 ₺'den satılmakta (3.000 birim); B ise 30.000 ₺ ek maliyetle tamamlanıp birim başına 120 ₺'den satılmaktadır (2.000 birim). İşletme net satış hasılatı yöntemini kullanmaktadır. Dönem sonunda B ürününden 400 birim satılmadan kaldığına göre bu stokun maliyeti kaç ₺'dir?",
        {
            'A': '37.200',
            'B': '31.200',
            'C': '25.200',
            'D': '48.000',
            'E': '6.000',
        },
        'B',
        "Net satış hasılatları: A 150.000, B 240.000 − 30.000 = 210.000; toplam 360.000 ₺. B'nin ortak maliyet payı 216.000 × 210.000 ÷ 360.000 = 126.000 ₺; ek maliyetle birlikte 156.000 ₺ → birim 78 ₺. 400 birimlik stok = 400 × 78 = **31.200 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (net satış hasılatı yöntemi)',
    ),
    # düzey 2
    '0041': patch(
        "Birleşik üretimde 'ana ürün' ile 'yan ürün' arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'Ana ürün üretimin temel amacı ve yüksek satış değerli olandır; yan ürün göreli olarak düşük değerli, ikincil üründür',
            'B': 'Ana ürün pazarda satılamaz; işletme içinde yeniden üretime girdi olarak verilir',
            'C': 'Ana ürün ile yan ürün eşit satış değerine sahiptir; aralarındaki fark üretim sırasından doğar',
            'D': 'Yan ürün ana üründen daha yüksek satış değerine sahiptir ve üretimin asıl hedeflenen çıktısıdır',
            'E': 'Yan ürün, işletmenin bilinçli tercihiyle ve önceden planlanmış biçimde, ayrı bir üretim hattında asıl hedef olarak üretilir',
        },
        'A',
        '**Ana ürün** üretimin temel amacı ve yüksek değerli olandır; **yan ürün** aynı süreçte kaçınılmaz biçimde ortaya çıkan, göreli olarak **düşük değerli** ikincil üründür.',
        'Maliyet muhasebesi - ana/yan ürün',
    ),
    # düzey 2
    '0042': patch(
        'Aşağıdaki üretim–yan ürün eşleştirmelerinden hangisi YANLIŞTIR?',
        {
            'A': 'Şeker üretimi → melas (yan ürün)',
            'B': 'Kereste işleme → talaş (yan ürün)',
            'C': 'Ayçiçeği yağı → küspe (yan ürün)',
            'D': 'Petrol rafinerisi → benzin (yan ürün)',
            'E': 'Un üretimi → kepek (yan ürün)',
        },
        'D',
        'Melas, kepek, talaş, küspe düşük değerli **yan ürünlerdir**. Petrol rafinerisinde **benzin** düşük değerli bir yan ürün değil, önemli bir **ana üründür**; eşleştirme yanlıştır.',
        'Maliyet muhasebesi - yan ürün',
    ),
    # düzey 2
    '0043': patch(
        "Bir işletme birleşik süreçte A ve B ürünlerini üretmektedir; toplam birleşik maliyet 300.000 ₺'dir. A ürününden 4.000 birim (birim satış fiyatı 150 ₺), B ürününden 2.000 birim (birim satış fiyatı 200 ₺) elde edilmiştir. Satış değeri esasına göre A ürününe düşen birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '90.000',
            'C': '150.000',
            'D': '160.000',
            'E': '180.000',
        },
        'E',
        'Satış değerleri: A = 4.000 × 150 = 600.000 ₺; B = 2.000 × 200 = 400.000 ₺; toplam = 1.000.000 ₺. A payı = Birleşik maliyet × (A satış değeri ÷ toplam) = 300.000 × (600.000 ÷ 1.000.000) = **180.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0044': patch(
        "Fiziki ölçü esaslı dağıtımda A ürününün birim maliyeti 10 ₺, A ürünü miktarı 6.000 kg'dır. Süreçte yalnızca A (6.000 kg) ve B (6.000 kg) üretilmiş ve toplam miktar 12.000 kg'dır. Toplam birleşik maliyet kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '90.000',
            'C': '240.000',
            'D': '30.000',
            'E': '120.000',
        },
        'E',
        'A payı = birim maliyet × miktar = 10 × 6.000 = 60.000 ₺. Fiziki dağıtımda A payı = J × (6.000 ÷ 12.000) = J × 0,5 = 60.000 → toplam birleşik maliyet J = 60.000 ÷ 0,5 = **120.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0045': patch(
        "Ana ürünün toplam birleşik maliyeti 200.000 ₺'dir; süreçte ortaya çıkan yan ürünün net gerçekleşebilir değeri 30.000 ₺'dir. Yan ürün değeri birleşik maliyetten düşülüyorsa ve ana üründen 8.500 birim elde edilmişse, ana ürünün BİRİM maliyeti kaç ₺'dir?",
        {
            'A': '20',
            'B': '30',
            'C': '23,53',
            'D': '17,65',
            'E': '25',
        },
        'A',
        "Yan ürün NGD'si ana ürün maliyetinden düşülür: net ana maliyet = 200.000 − 30.000 = 170.000 ₺. Ana ürün birim maliyeti = 170.000 ÷ 8.500 = **20 ₺**. (Yan ürünü düşmemek 23,53 verir.)",
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0046': patch(
        'Birleşik maliyeti 240.000 ₺ olan bir süreçte P ürününden 4.000 birim (birim fiyat 75 ₺), Q ürününden 1.000 birim (birim fiyat 100 ₺) üretilmiştir. Satış değeri esasına göre dağıtım yapıldığında Q ürününün BİRİM maliyeti, P ürününün birim maliyetinden kaç ₺ FAZLADIR?',
        {
            'A': '30',
            'B': '45',
            'C': '60',
            'D': '105',
            'E': '15',
        },
        'E',
        'Satış değerleri: P = 4.000 × 75 = 300.000 ₺; Q = 1.000 × 100 = 100.000 ₺; toplam 400.000 ₺. P payı = 240.000 × (300.000 ÷ 400.000) = 180.000 ₺ → P birim = 180.000 ÷ 4.000 = 45 ₺. Q payı = 60.000 ₺ → Q birim = 60.000 ÷ 1.000 = 60 ₺. Fark = 60 − 45 = **15 ₺** (Q daha yüksek).',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0047': patch(
        "Satış değeri esaslı dağıtımda A ürününe 120.000 ₺ pay düşmüştür. A ürününün satış değeri 400.000 ₺, tüm ürünlerin toplam satış değeri 1.000.000 ₺ olduğuna göre toplam birleşik maliyet kaç ₺'dir?",
        {
            'A': '480.000',
            'B': '48.000',
            'C': '250.000',
            'D': '300.000',
            'E': '120.000',
        },
        'D',
        'A payı = J × (A satış değeri ÷ toplam) → 120.000 = J × (400.000 ÷ 1.000.000) = J × 0,4. Toplam birleşik maliyet J = 120.000 ÷ 0,4 = **300.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0048': patch(
        "Bir ürünün nihai satış değeri 120.000 ₺, ayrım sonrası ilave işleme maliyeti 40.000 ₺'dir. Bu ürünün net gerçekleşebilir değeri (NGD) kaç ₺'dir?",
        {
            'A': '3.000',
            'B': '120.000',
            'C': '80.000',
            'D': '40.000',
            'E': '160.000',
        },
        'C',
        'NGD = nihai satış değeri − ayrım sonrası maliyet = 120.000 − 40.000 = **80.000 ₺**.',
        'Maliyet muhasebesi - NGD',
    ),
    # düzey 2
    '0049': patch(
        "Ana ürünün toplam birleşik maliyeti 200.000 ₺, süreçte ortaya çıkan yan ürünün net satış (gerçekleşebilir) değeri 20.000 ₺'dir. Yan ürün değeri ana ürün maliyetinden düşüldüğünde ana ürüne kalan net birleşik maliyet kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '180.000',
            'C': '220.000',
            'D': '160.000',
            'E': '20.000',
        },
        'B',
        'Ana ürüne kalan net birleşik maliyet = 200.000 − 20.000 = **180.000 ₺** (yan ürünün net değeri ana ürün maliyetinden düşülür).',
        'Maliyet muhasebesi - yan ürün muhasebesi',
    ),
    # düzey 2
    '0050': patch(
        "Birleşik maliyeti 360.000 ₺ olan bir süreçte A ürününden 5.000 birim (birim fiyat 120 ₺), B ürününden 3.000 birim (birim fiyat 100 ₺) elde edilmiştir. Satış değeri esasına göre dağıtım yapıldığında A ürününün brüt kârı (satış − birleşik maliyet payı) kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '180.000',
            'C': '240.000',
            'D': '360.000',
            'E': '600.000',
        },
        'D',
        'A satış = 5.000 × 120 = 600.000 ₺; B satış = 300.000 ₺; toplam 900.000 ₺. A payı = 360.000 × (600.000 ÷ 900.000) = 240.000 ₺. A brüt kârı = A satış − A payı = 600.000 − 240.000 = **360.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 2
    '0051': patch(
        "Birleşik maliyeti 60.000 ₺ olan bir süreçte K 2.000 kg ve L 1.000 kg ürün elde edilmiştir. Fiziki ölçü esasına göre K ürününün BİRİM (kg) maliyeti kaç ₺'dir?",
        {
            'A': '15',
            'B': '20',
            'C': '30',
            'D': '10',
            'E': '40.000',
        },
        'B',
        'Toplam miktar = 2.000 + 1.000 = 3.000 kg. K payı = 60.000 × (2.000 ÷ 3.000) = 40.000 ₺. K birim = 40.000 ÷ 2.000 = **20 ₺/kg**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletmede K, L ve M ortak ürünleri üretilmektedir. Bir esas üretim gider yerinde toplanan birleşik giderler 264.000 ₺'dir. Ürünlere ilişkin bilgiler şöyledir:\n\n| Ürün | Üretim miktarı (adet) | Katsayı |\n|---|---|---|\n| K | 6.000 | 1 |\n| L | 5.000 | 2 |\n| M | 1.000 | 6 |\n\nBirleşik giderler katsayı (eşdeğer ürün miktarı) yöntemiyle dağıtıldığına göre L ürününün birleşik gider payı kaç ₺'dir?",
        {
            'A': '110.000',
            'B': '120.000',
            'C': '144.000',
            'D': '60.000',
            'E': '72.000',
        },
        'B',
        'Eşdeğer ürün miktarları: K 6.000 × 1 = 6.000; L 5.000 × 2 = 10.000; M 1.000 × 6 = 6.000; toplam 22.000. Eşdeğer birim başına gider = 264.000 ÷ 22.000 = 12 ₺. L payı = 10.000 × 12 = **120.000 ₺**. Katsayıyı unutup adetle çarpmak 60.000 ₺ verir.',
        'Maliyet muhasebesi - birleşik maliyet (katsayı yöntemi)',
    ),
    # düzey 3
    '0053': patch(
        "A, B ve C ürünleri 252.000 ₺ ortak maliyete katlanılarak üretilmektedir. Döneme ait veriler şöyledir:\n\n| Ürün | Üretim miktarı | Satış fiyatı |\n|---|---|---|\n| A | 3.000 kg | 40 ₺/kg |\n| B | 1.000 kg | 120 ₺/kg |\n| C | 4.000 kg | 45 ₺/kg |\n\nİşletme ortak maliyetleri satış değeri yöntemiyle dağıttığına göre B ürününün ortak maliyetten kg başına alacağı pay kaç ₺'dir?",
        {
            'A': '27',
            'B': '24',
            'C': '31,50',
            'D': '120',
            'E': '72',
        },
        'E',
        'Satış değerleri: A 120.000, B 120.000, C 180.000; toplam 420.000 ₺. Dağıtım oranı 252.000 ÷ 420.000 = 0,60. B payı 120.000 × 0,60 = 72.000 ₺; kg başına 72.000 ÷ 1.000 = **72 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (satış değeri yöntemi)',
    ),
    # düzey 3
    '0054': patch(
        "A ve B ana ürünleri ile Z yan ürününün elde edildiği bir süreçte ortak maliyetler şöyledir: direkt ilk madde ve malzeme 420.000 ₺, direkt işçilik 300.000 ₺, genel üretim 180.000 ₺. Ayrılma noktasından sonra ek maliyete katlanılmamaktadır. Ürün bilgileri şöyledir:\n\n| Ürün | Üretim miktarı | Satış fiyatı |\n|---|---|---|\n| A | 4.000 ton | 250 ₺/ton |\n| B | 5.000 ton | 200 ₺/ton |\n| Z (yan ürün) | 100 ton | 20 ₺/ton |\n\nYan ürüne maliyetten pay vermeyen işletme üretim miktarları yöntemini kullandığına göre, tamamı satılan B ürününün ton başına satış kârı kaç ₺'dir?",
        {
            'A': '100',
            'B': '120',
            'C': '90',
            'D': '110',
            'E': '200',
        },
        'A',
        "Ortak maliyet = 420.000 + 300.000 + 180.000 = 900.000 ₺. Yan ürün pay almadığından yalnız ana ürünlerin miktarı esas alınır: 4.000 + 5.000 = 9.000 ton → ton başına 100 ₺. B'nin ton başına kârı = 200 − 100 = **100 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (yan ürün)',
    ),
    # düzey 3
    '0055': patch(
        '160.000 ₺ ortak maliyetle üretilen P ve Q ürünlerine ilişkin bilgiler şöyledir:\n\n| Ürün | SD₁ (₺) | SD₂ (₺) | İİM (₺) |\n|---|---|---|---|\n| P | 150.000 | 210.000 | 45.000 |\n| Q | 90.000 | 130.000 | 50.000 |\n\nSD₁: ayrılma noktasındaki satış değeri · SD₂: ilave işlem sonrası satış değeri · İİM: ilave işleme maliyeti\n\nİşletme her ürün için en kârlı kararı verirse toplam kârı kaç ₺ olur?',
        {
            'A': '15.000',
            'B': '95.000',
            'C': '85.000',
            'D': '70.000',
            'E': '80.000',
        },
        'B',
        "P: ek gelir 60.000 > ek maliyet 45.000 → işlenir, net 165.000 ₺. Q: ek gelir 40.000 < 50.000 → ayrılma noktasında 90.000 ₺'ye satılır. Toplam kâr = 165.000 + 90.000 − 160.000 = **95.000 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (ilave işleme kararı)',
    ),
    # düzey 3
    '0056': patch(
        "Ortak maliyeti 390.000 ₺ olan bir süreçten A ve B ürünleri elde edilmektedir. Ürünler ayrılma noktasından sonra ek işlemden geçirilerek satılmaktadır:\n\n| Ürün | Üretim (birim) | Satış fiyatı (₺) | Ek maliyet (₺) |\n|---|---|---|---|\n| A | 5.000 | 80 | 50.000 |\n| B | 2.500 | 160 | 100.000 |\n\nNet satış hasılatı yöntemi kullanıldığına göre tamamı satılan A ürününün brüt satış kârı kaç ₺'dir?",
        {
            'A': '90.000',
            'B': '140.000',
            'C': '260.000',
            'D': '190.000',
            'E': '155.000',
        },
        'B',
        "Net satış hasılatları: A 400.000 − 50.000 = 350.000; B 400.000 − 100.000 = 300.000. A payı = 390.000 × 350.000 ÷ 650.000 = 210.000 ₺. A'nın toplam maliyeti 210.000 + ek 50.000 = 260.000 ₺; kâr = 400.000 − 260.000 = **140.000 ₺**.",
        'Maliyet muhasebesi - birleşik maliyet (net satış hasılatı yöntemi)',
    ),
    # düzey 3
    '0057': patch(
        "Birleşik gideri 200.000 ₺ olan bir işletme E, F ve G ürünlerini üretmektedir. Üretim miktarları sırasıyla 2.000, 2.000 ve 1.000 birim, ağırlık katsayıları ise 1, 2 ve 4'tür. İşletme katsayı yöntemi yerine üretim miktarı yöntemini kullansaydı G ürününün birleşik gider payı nasıl değişirdi?",
        {
            'A': '40.000 ₺ azalırdı',
            'B': '20.000 ₺ azalırdı',
            'C': '80.000 ₺ azalırdı',
            'D': 'Değişmezdi',
            'E': '40.000 ₺ artardı',
        },
        'A',
        "Katsayı yöntemi: eşdeğer miktar 2.000 + 4.000 + 4.000 = 10.000 → birim eşdeğere 20 ₺; G payı 4.000 × 20 = 80.000 ₺. Miktar yöntemi: 200.000 × 1.000 ÷ 5.000 = 40.000 ₺. G'nin payı **40.000 ₺ azalır**; yüksek katsayılı ürün katsayı yönteminde daha çok pay alır.",
        'Maliyet muhasebesi - birleşik maliyet (katsayı yöntemi)',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletme A, B ve C mamullerini 640.000 ₺ ortak maliyete katlanarak üretmektedir. Ocak ayı verileri şöyledir:\n\n| Mamul | Üretim miktarı | Toplam satış değeri (₺) |\n|---|---|---|\n| A | 2.500 kg | 320.000 |\n| B | 3.500 kg | 384.000 |\n| C | 2.000 kg | 576.000 |\n\nÜretim miktarı yöntemine göre B mamulünün ortak maliyetten aldığı pay kaç ₺'dir?",
        {
            'A': '384.000',
            'B': '200.000',
            'C': '280.000',
            'D': '192.000',
            'E': '160.000',
        },
        'C',
        'Üretim miktarı yönteminde satış değerleri kullanılmaz. Toplam miktar 2.500 + 3.500 + 2.000 = 8.000 kg → kg başına 640.000 ÷ 8.000 = 80 ₺. B payı = 3.500 × 80 = **280.000 ₺**. Satış değeri yöntemi 192.000 ₺ verirdi.',
        'Maliyet muhasebesi - birleşik maliyet (üretim miktarı yöntemi)',
    ),
    # düzey 3
    '0059': patch(
        "Bir işletme 360.000 ₺ birleşik maliyetin %30'unu A, B ve C ürünlerine eşit olarak, kalanını ise üretim miktarlarına göre dağıtmaktadır. Ürünlerin üretim miktarları sırasıyla 5.000, 3.000 ve 2.000 kg'dır. Buna göre C ürününün birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '72.000',
            'B': '50.400',
            'C': '108.000',
            'D': '86.400',
            'E': '120.000',
        },
        'D',
        'Eşit kısım 360.000 × %30 = 108.000 ₺ → ürün başına 36.000 ₺. Kalan 252.000 ₺ miktarla: C payı 252.000 × 2.000 ÷ 10.000 = 50.400 ₺. Toplam 36.000 + 50.400 = **86.400 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (karma dağıtım)',
    ),
    # düzey 3
    '0060': patch(
        "Ortak maliyeti 360.000 ₺ olan bir süreçten A ürünü 4.000 birim (90 ₺'den) ve B ürünü 2.000 birim (120 ₺'den) elde edilmiş ve tamamı satılmıştır. Ek maliyet yoktur. Ortak maliyet satış değeri yöntemiyle dağıtıldığına göre A ürününün brüt kâr oranı (brüt kâr ÷ satışlar) yüzde kaçtır?",
        {
            'A': '%50',
            'B': '%36',
            'C': '%60',
            'D': '%40',
            'E': '%25',
        },
        'D',
        "Toplam satış değeri 360.000 + 240.000 = 600.000 ₺; ortak maliyet satışların 360.000 ÷ 600.000 = %60'ıdır. Satış değeri yönteminde her ürünün maliyeti kendi satışının %60'ı olduğundan tüm ürünlerin brüt kâr oranı eşittir: **%40**.",
        'Maliyet muhasebesi - birleşik maliyet (satış değeri yöntemi)',
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
    print(f"1 paket / {len(PATCHES)} soru ('Birlesik Maliyet' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
