#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi — çok adımlı (harder) kalibrasyon yamaları.

Tek-adımlı hesap sorularını ham veriden başlayan çok adımlı senaryolara dönüştürür
(katkı payı → başabaş/hedef kâr/güvenlik marjı/faaliyet kaldıracı; birleşik maliyette
satış değeri/NGD dağıtımı → birim/kâr, yan ürün, ilave işleme kararı, karşılaştırma,
ters-hesap). Aritmetik builder dışında bağımsız doğrulanmıştır. Kavram+öncüllü korunur;
ID'ler değişmez.  --check / --write
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
MHK_RELATIVE_PATH = "content/maliyet_muhasebesi/maliyet_hacim_kar.json"
BIRLESIK_RELATIVE_PATH = "content/maliyet_muhasebesi/birlesik_maliyet.json"
# gider_dagitimi.json -> build_mmuh_gider_dagitimi_tablolu.py (tek sahip)
SAFHA_RELATIVE_PATH = "content/maliyet_muhasebesi/safha_maliyeti.json"
# siparis_maliyeti.json -> build_siparis_maliyeti_onarim.py (tek sahip)
STANDART_RELATIVE_PATH = "content/maliyet_muhasebesi/standart_maliyet.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (çok adımlı hesap; 2024-2026 sınav zorluğuna kalibre)'


def cost_patch(stem, options, answer, solution, legislation_ref):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF, "legislationRef": legislation_ref},
        "validYear": 2026, "mockExamId": None,
    }


MHK_HARDER_PATCHES = {
    'mmuh-mhk-gen-0007': cost_patch(
        "Bir işletme ürününü birim 150 ₺'ye satmakta; birim değişken maliyeti 90 ₺, aylık toplam sabit maliyeti 300.000 ₺'dir. Başabaş noktası satış miktarı kaç adettir?",
        {
            'A': '5.000',
            'B': '2.000',
            'C': '3.333',
            'D': '10.000',
            'E': '4.000',
        },
        'A',
        'Birim katkı payı = 150 − 90 = **60 ₺**. Başabaş miktar = Toplam sabit maliyet ÷ birim katkı payı = 300.000 ÷ 60 = **5.000 adet**. (Fiyata bölmek 2.000, değişkene bölmek 3.333 verir — ikisi de yanlış; bölen katkı payıdır.)',
        'Maliyet muhasebesi - başabaş (çok adımlı)',
    ),
    'mmuh-mhk-gen-0009': cost_patch(
        "Birim satış fiyatı 200 ₺, birim değişken maliyeti 120 ₺ ve toplam sabit maliyeti 480.000 ₺ olan bir işletmenin başabaş noktası satış TUTARI kaç ₺'dir?",
        {
            'A': '6.000',
            'B': '1.200.000',
            'C': '480.000',
            'D': '2.400.000',
            'E': '800.000',
        },
        'B',
        'Birim katkı payı = 200 − 120 = 80 ₺; katkı payı oranı = 80 ÷ 200 = %40. Başabaş tutar = Sabit maliyet ÷ katkı payı oranı = 480.000 ÷ 0,40 = **1.200.000 ₺**. (Başabaş adet = 480.000 ÷ 80 = 6.000; tutar = 6.000 × 200 = 1.200.000 ₺ ile aynı.)',
        'Maliyet muhasebesi - başabaş tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0012': cost_patch(
        'Birim satış fiyatı 100 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 200.000 ₺ olan bir işletme dönem sonunda 120.000 ₺ kâr hedeflemektedir. Bu hedef için satması gereken miktar kaç adettir?',
        {
            'A': '8.000',
            'B': '5.000',
            'C': '3.000',
            'D': '3.200',
            'E': '800.000',
        },
        'A',
        'Birim katkı payı = 100 − 60 = 40 ₺. Hedef kâr için miktar = (Sabit maliyet + Hedef kâr) ÷ katkı payı = (200.000 + 120.000) ÷ 40 = 320.000 ÷ 40 = **8.000 adet**. (Yalnız başabaş 5.000; yalnız kârı bölmek 3.000 verir.)',
        'Maliyet muhasebesi - hedef kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0014': cost_patch(
        "Birim satış fiyatı 80 ₺, birim değişken maliyeti 50 ₺, toplam sabit maliyeti 150.000 ₺ olan bir işletme dönemde 8.000 adet satmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '490.000',
            'C': '10.000',
            'D': '150.000',
            'E': '90.000',
        },
        'E',
        'Birim katkı payı = 80 − 50 = 30 ₺. Toplam katkı payı = 8.000 × 30 = 240.000 ₺. Kâr = Toplam katkı payı − Sabit maliyet = 240.000 − 150.000 = **90.000 ₺**. (Sabiti düşmemek 240.000; değişkeni ihmal edip 8.000 × 80 − 150.000 = 490.000 verir — ikisi de yanlış.)',
        'Maliyet muhasebesi - kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0019': cost_patch(
        'Birim satış fiyatı 120 ₺, birim değişken maliyeti 80 ₺, toplam sabit maliyeti 320.000 ₺ olan bir işletme cari dönemde 12.000 adet satmıştır. Güvenlik marjı (adet) kaçtır?',
        {
            'A': '8.000',
            'B': '4.000',
            'C': '12.000',
            'D': '2.667',
            'E': '6.000',
        },
        'B',
        'Birim katkı payı = 120 − 80 = 40 ₺. Başabaş miktar = 320.000 ÷ 40 = 8.000 adet. Güvenlik marjı = Fiili satış − Başabaş satış = 12.000 − 8.000 = **4.000 adet**. (Başabaşın kendisi 8.000; fiili satış 12.000 değil.)',
        'Maliyet muhasebesi - güvenlik marjı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0022': cost_patch(
        'Birim katkı payı 50 ₺, toplam sabit maliyeti 400.000 ₺ olan bir işletme, vergi oranının %20 olarak dikkate alınacağı bir dönemde vergi SONRASI 160.000 ₺ net kâr hedeflemektedir. Gereken satış miktarı kaç adettir?',
        {
            'A': '12.000',
            'B': '11.200',
            'C': '8.000',
            'D': '4.000',
            'E': '10.000',
        },
        'A',
        'Vergi öncesi (brüt) hedef kâr = Net kâr ÷ (1 − vergi oranı) = 160.000 ÷ 0,80 = 200.000 ₺. Gereken miktar = (Sabit + brüt kâr) ÷ katkı payı = (400.000 + 200.000) ÷ 50 = **12.000 adet**. (Vergiyi ihmal edip 160.000 kullanmak 11.200 verir — yanlış.)',
        'Maliyet muhasebesi - vergili hedef kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0023': cost_patch(
        "Birim satış fiyatı 60 ₺, birim değişken maliyeti 36 ₺, toplam sabit maliyeti 180.000 ₺ olan bir işletme dönemde 10.000 adet satmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '420.000',
            'C': '60.000',
            'D': '24.000',
            'E': '180.000',
        },
        'C',
        'Birim katkı payı = 60 − 36 = 24 ₺. Toplam katkı payı = 10.000 × 24 = 240.000 ₺. Kâr = 240.000 − 180.000 = **60.000 ₺**. (Sabiti düşmemek 240.000; değişkeni ihmal 600.000 − 180.000 = 420.000 verir.)',
        'Maliyet muhasebesi - kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0027': cost_patch(
        "Birim satış fiyatı 250 ₺, birim değişken maliyeti 150 ₺, toplam sabit maliyeti 600.000 ₺ olan bir işletme 300.000 ₺ kâr hedeflemektedir. Gereken satış TUTARI kaç ₺'dir?",
        {
            'A': '9.000',
            'B': '2.250.000',
            'C': '1.500.000',
            'D': '900.000',
            'E': '3.750.000',
        },
        'B',
        "Birim katkı payı = 250 − 150 = 100 ₺; oran = 100 ÷ 250 = %40. Gereken tutar = (Sabit + Hedef kâr) ÷ katkı payı oranı = (600.000 + 300.000) ÷ 0,40 = **2.250.000 ₺**. (Yalnız başabaş tutarı 1.500.000 ₺'dir.)",
        'Maliyet muhasebesi - hedef kâr tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0028': cost_patch(
        "Birim satış fiyatı 40 ₺, birim değişken maliyeti 24 ₺, toplam sabit maliyeti 240.000 ₺ olan bir işletme 120.000 ₺ kâr hedeflemektedir. Gereken satış TUTARI kaç ₺'dir?",
        {
            'A': '900.000',
            'B': '600.000',
            'C': '360.000',
            'D': '1.500.000',
            'E': '562.500',
        },
        'A',
        'Birim katkı payı = 40 − 24 = 16 ₺; oran = 16 ÷ 40 = %40. Gereken tutar = (Sabit + Hedef kâr) ÷ katkı payı oranı = (240.000 + 120.000) ÷ 0,40 = **900.000 ₺**. (Yalnız başabaş tutarı 240.000 ÷ 0,40 = 600.000.)',
        'Maliyet muhasebesi - hedef kâr tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0032': cost_patch(
        "Birim satış fiyatı 100 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 200.000 ₺ olan bir işletmede sabit maliyet 250.000 ₺'ye yükselmiştir. Diğer koşullar sabitken başabaş noktası satış miktarı kaç adet ARTAR?",
        {
            'A': '6.250',
            'B': '5.000',
            'C': '50.000',
            'D': '1.250',
            'E': '625',
        },
        'D',
        'Birim katkı payı = 100 − 60 = 40 ₺. Eski başabaş = 200.000 ÷ 40 = 5.000; yeni başabaş = 250.000 ÷ 40 = 6.250. Artış = 6.250 − 5.000 = **1.250 adet**. (6.250 yeni başabaşın kendisi, artış değil.)',
        'Maliyet muhasebesi - başabaş duyarlılık (çok adımlı)',
    ),
    'mmuh-mhk-gen-0037': cost_patch(
        "Bir ürünün satış fiyatı 200 ₺ ve katkı payı oranı %35'tir. İşletmenin toplam sabit maliyeti 490.000 ₺ olduğuna göre başabaş noktası satış miktarı kaç adettir?",
        {
            'A': '2.450',
            'B': '7.000',
            'C': '3.500',
            'D': '14.000',
            'E': '4.900',
        },
        'B',
        "Birim katkı payı = Fiyat × katkı payı oranı = 200 × %35 = 70 ₺. Başabaş miktar = 490.000 ÷ 70 = **7.000 adet**. (Fiyata bölmek 2.450 verir; katkı payı 70 ₺'dir.)",
        'Maliyet muhasebesi - başabaş (orandan; çok adımlı)',
    ),
    'mmuh-mhk-gen-0038': cost_patch(
        "Birim satış fiyatı 100 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 240.000 ₺ olan bir işletmede birim değişken maliyet 68 ₺'ye yükselmiştir. Diğer koşullar sabitken yeni başabaş noktası satış miktarı kaç adettir?",
        {
            'A': '6.000',
            'B': '1.500',
            'C': '3.529',
            'D': '8.000',
            'E': '7.500',
        },
        'E',
        'Yeni birim katkı payı = 100 − 68 = 32 ₺ (eskisi 40 ₺ idi). Yeni başabaş miktar = 240.000 ÷ 32 = **7.500 adet**. (Eski başabaş 240.000 ÷ 40 = 6.000 idi; değişken maliyet artışı katkı payını düşürüp başabaşı yükseltir.)',
        'Maliyet muhasebesi - başabaş duyarlılık (çok adımlı)',
    ),
    'mmuh-mhk-gen-0039': cost_patch(
        "Bir işletme ürününü birim 150 ₺'ye satmakta ve toplam sabit maliyeti 300.000 ₺'dir. Dönemde 6.000 adet satıp 60.000 ₺ kâr elde ettiğine göre ürünün birim değişken maliyeti kaç ₺'dir?",
        {
            'A': '90',
            'B': '60',
            'C': '100',
            'D': '110',
            'E': '50',
        },
        'A',
        'Kâr = Toplam katkı payı − Sabit maliyet olduğundan toplam katkı payı = 60.000 + 300.000 = 360.000 ₺. Birim katkı payı = 360.000 ÷ 6.000 = 60 ₺. Birim değişken maliyet = Satış fiyatı − katkı payı = 150 − 60 = **90 ₺**.',
        'Maliyet muhasebesi - birim değişken (ters; çok adımlı)',
    ),
    'mmuh-mhk-gen-0042': cost_patch(
        'Birim satış fiyatı 50 ₺, birim değişken maliyeti 30 ₺, toplam sabit maliyeti 240.000 ₺ olan bir işletme dönemde 16.000 adet satmıştır. Güvenlik marjı ORANI yüzde kaçtır?',
        {
            'A': '%75',
            'B': '%33,33',
            'C': '%25',
            'D': '%20',
            'E': '%40',
        },
        'C',
        "Birim katkı payı = 50 − 30 = 20 ₺. Başabaş = 240.000 ÷ 20 = 12.000 adet. Güvenlik marjı = 16.000 − 12.000 = 4.000 adet; oran = 4.000 ÷ 16.000 = **%25**. (Başabaşın satışa oranı %75'tir, güvenlik marjı değil.)",
        'Maliyet muhasebesi - güvenlik marjı oranı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0044': cost_patch(
        "Bir işletmenin başabaş noktası 5.000 adet, birim katkı payı 10 ₺'dir. İşletme dönemde başabaş noktasının 3.000 adet üzerinde (toplam 8.000 adet) satış yapmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '80.000',
            'B': '30.000',
            'C': '50.000',
            'D': '3.000',
            'E': '20.000',
        },
        'B',
        'Başabaş noktasından sonraki her birimin katkı payı doğrudan kâra dönüşür (sabit maliyet zaten karşılanmıştır). Kâr = Başabaş üzeri miktar × birim katkı payı = 3.000 × 10 = **30.000 ₺**.',
        'Maliyet muhasebesi - güvenlik marjı × katkı payı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0046': cost_patch(
        "Bir işletmenin dönem toplam katkı payı 360.000 ₺, dönem kârı ise 60.000 ₺'dir. İşletmenin faaliyet (çalışma) kaldıracı derecesi kaçtır?",
        {
            'A': '5',
            'B': '0,17',
            'C': '420.000',
            'D': '6',
            'E': '300.000',
        },
        'D',
        'Faaliyet kaldıracı derecesi = Toplam katkı payı ÷ Kâr = 360.000 ÷ 60.000 = **6**. Yani satışlar %1 arttığında kâr yaklaşık %6 artar; kaldıraç, kârın satış değişimine duyarlılığını gösterir.',
        'Maliyet muhasebesi - faaliyet kaldıracı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0049': cost_patch(
        "Katkı payı oranı %40, toplam sabit maliyeti 480.000 ₺ olan bir işletme, vergi oranının %25 dikkate alınacağı bir dönemde vergi SONRASI 270.000 ₺ net kâr hedeflemektedir. Gereken satış TUTARI kaç ₺'dir?",
        {
            'A': '2.100.000',
            'B': '1.875.000',
            'C': '1.200.000',
            'D': '900.000',
            'E': '2.400.000',
        },
        'A',
        'Vergi öncesi kâr = 270.000 ÷ (1 − 0,25) = 270.000 ÷ 0,75 = 360.000 ₺. Gereken tutar = (Sabit + brüt kâr) ÷ katkı payı oranı = (480.000 + 360.000) ÷ 0,40 = **2.100.000 ₺**. (Vergiyi ihmal edip 270.000 kullanmak 1.875.000 verir.)',
        'Maliyet muhasebesi - vergili hedef kâr tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0051': cost_patch(
        "Bir işletmenin katkı payı oranı %20 ve başabaş noktası satış TUTARI 600.000 ₺'dir. Buna göre işletmenin toplam sabit maliyeti kaç ₺'dir?",
        {
            'A': '600.000',
            'B': '120.000',
            'C': '3.000.000',
            'D': '480.000',
            'E': '150.000',
        },
        'B',
        'Başabaş tutar = Sabit maliyet ÷ katkı payı oranı olduğundan Sabit maliyet = Başabaş tutar × katkı payı oranı = 600.000 × 0,20 = **120.000 ₺**. (Oranı bölmek 3.000.000 verir — ters işlem, yanlış.)',
        'Maliyet muhasebesi - sabit maliyet (ters; çok adımlı)',
    ),
    'mmuh-mhk-gen-0052': cost_patch(
        "Birim satış fiyatı 100 ₺, birim değişken maliyeti 76 ₺, toplam sabit maliyeti 120.000 ₺ olan bir işletme dönemde 8.000 adet satmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '192.000',
            'B': '680.000',
            'C': '24.000',
            'D': '120.000',
            'E': '72.000',
        },
        'E',
        'Birim katkı payı = 100 − 76 = 24 ₺. Toplam katkı payı = 8.000 × 24 = 192.000 ₺. Kâr = 192.000 − 120.000 = **72.000 ₺**.',
        'Maliyet muhasebesi - kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0057': cost_patch(
        'Birim satış fiyatı 90 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 180.000 ₺ olan bir işletmenin başabaş noktası satış miktarı kaç adettir?',
        {
            'A': '2.000',
            'B': '3.000',
            'C': '6.000',
            'D': '12.000',
            'E': '5.000',
        },
        'C',
        'Birim katkı payı = 90 − 60 = 30 ₺. Başabaş miktar = 180.000 ÷ 30 = **6.000 adet**.',
        'Maliyet muhasebesi - başabaş (çok adımlı)',
    ),
    'mmuh-mhk-gen-0058': cost_patch(
        'Birim satış fiyatı 120 ₺, birim değişken maliyeti 90 ₺, toplam sabit maliyeti 180.000 ₺ olan bir işletme 90.000 ₺ kâr hedeflemektedir. Gereken satış miktarı kaç adettir?',
        {
            'A': '6.000',
            'B': '3.000',
            'C': '2.250',
            'D': '9.000',
            'E': '7.500',
        },
        'D',
        'Birim katkı payı = 120 − 90 = 30 ₺. Gereken miktar = (180.000 + 90.000) ÷ 30 = **9.000 adet**. (Yalnız başabaş 6.000.)',
        'Maliyet muhasebesi - hedef kâr (çok adımlı)',
    ),
}

BIRLESIK_HARDER_PATCHES = {
    'mmuh-birlesik-gen-0021': cost_patch(
        "Bir işletme birleşik süreçte A ve B ürünlerini üretmektedir; toplam birleşik maliyet 300.000 ₺'dir. A ürününden 4.000 birim (birim satış fiyatı 150 ₺), B ürününden 2.000 birim (birim satış fiyatı 200 ₺) elde edilmiştir. Satış değeri esasına göre A ürününe düşen birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '200.000',
            'C': '180.000',
            'D': '150.000',
            'E': '90.000',
        },
        'C',
        'Satış değerleri: A = 4.000 × 150 = 600.000 ₺; B = 2.000 × 200 = 400.000 ₺; toplam = 1.000.000 ₺. A payı = Birleşik maliyet × (A satış değeri ÷ toplam) = 300.000 × (600.000 ÷ 1.000.000) = **180.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0026': cost_patch(
        "Toplam birleşik maliyeti 200.000 ₺ olan bir süreçte A ürününden 3.000 birim (birim fiyat 100 ₺), B ürününden 2.000 birim (birim fiyat 100 ₺) üretilmiştir. Satış değeri esasına göre A ürününe düşen pay kaç ₺'dir?",
        {
            'A': '80.000',
            'B': '100.000',
            'C': '120.000',
            'D': '60.000',
            'E': '200.000',
        },
        'C',
        'Satış değerleri: A = 3.000 × 100 = 300.000 ₺; B = 2.000 × 100 = 200.000 ₺; toplam = 500.000 ₺. A payı = 200.000 × (300.000 ÷ 500.000) = **120.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0027': cost_patch(
        "Birleşik maliyeti 480.000 ₺ olan bir süreçte P ürününden 5.000 birim (birim fiyat 100 ₺), Q ürününden 3.000 birim (birim fiyat 100 ₺) üretilmiştir. Satış değeri esasına göre Q ürününün BİRİM maliyeti kaç ₺'dir?",
        {
            'A': '36',
            'B': '100',
            'C': '60',
            'D': '48',
            'E': '90',
        },
        'C',
        'Satış değerleri: P = 500.000 ₺, Q = 300.000 ₺, toplam 800.000 ₺. Q payı = 480.000 × (300.000 ÷ 800.000) = 180.000 ₺. Q birim maliyeti = 180.000 ÷ 3.000 = **60 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0032': cost_patch(
        'Birleşik maliyeti 240.000 ₺ olan bir süreçte P ürününden 4.000 birim (birim fiyat 75 ₺), Q ürününden 1.000 birim (birim fiyat 100 ₺) üretilmiştir. Satış değeri esasına göre dağıtım yapıldığında Q ürününün BİRİM maliyeti, P ürününün birim maliyetinden kaç ₺ FAZLADIR?',
        {
            'A': '15',
            'B': '60',
            'C': '45',
            'D': '105',
            'E': '30',
        },
        'A',
        'Satış değerleri: P = 4.000 × 75 = 300.000 ₺; Q = 1.000 × 100 = 100.000 ₺; toplam 400.000 ₺. P payı = 240.000 × (300.000 ÷ 400.000) = 180.000 ₺ → P birim = 180.000 ÷ 4.000 = 45 ₺. Q payı = 60.000 ₺ → Q birim = 60.000 ÷ 1.000 = 60 ₺. Fark = 60 − 45 = **15 ₺** (Q daha yüksek).',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0052': cost_patch(
        "Birleşik maliyeti 360.000 ₺ olan bir süreçte A ürününden 5.000 birim (birim fiyat 120 ₺), B ürününden 3.000 birim (birim fiyat 100 ₺) elde edilmiştir. Satış değeri esasına göre dağıtım yapıldığında A ürününün brüt kârı (satış − birleşik maliyet payı) kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '360.000',
            'C': '600.000',
            'D': '180.000',
            'E': '300.000',
        },
        'B',
        'A satış = 5.000 × 120 = 600.000 ₺; B satış = 300.000 ₺; toplam 900.000 ₺. A payı = 360.000 × (600.000 ÷ 900.000) = 240.000 ₺. A brüt kârı = A satış − A payı = 600.000 − 240.000 = **360.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0030': cost_patch(
        "Birleşik maliyeti 90.000 ₺ olan bir süreçte X 3.000 kg, Y 6.000 kg ve Z 1.000 kg ürün elde edilmiştir. Fiziki ölçü esasına göre Y ürününün BİRİM (kg) maliyeti kaç ₺'dir?",
        {
            'A': '6',
            'B': '9',
            'C': '54.000',
            'D': '15',
            'E': '5',
        },
        'B',
        'Toplam miktar = 3.000 + 6.000 + 1.000 = 10.000 kg. Y payı = 90.000 × (6.000 ÷ 10.000) = 54.000 ₺. Y birim = 54.000 ÷ 6.000 = **9 ₺/kg**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0055': cost_patch(
        "Birleşik maliyeti 60.000 ₺ olan bir süreçte K 2.000 kg ve L 1.000 kg ürün elde edilmiştir. Fiziki ölçü esasına göre K ürününün BİRİM (kg) maliyeti kaç ₺'dir?",
        {
            'A': '30',
            'B': '20',
            'C': '40.000',
            'D': '10',
            'E': '15',
        },
        'B',
        'Toplam miktar = 2.000 + 1.000 = 3.000 kg. K payı = 60.000 × (2.000 ÷ 3.000) = 40.000 ₺. K birim = 40.000 ÷ 2.000 = **20 ₺/kg**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0022': cost_patch(
        "Birleşik maliyeti 200.000 ₺ olan bir süreçte A 8.000 kg, B 2.000 kg ürün elde edilmiştir. Fiziki ölçü esasına göre dağıtım yapıldığında A ürünü 220.000 ₺'ye satılırsa A'nın brüt kârı kaç ₺'dir?",
        {
            'A': '160.000',
            'B': '20.000',
            'C': '220.000',
            'D': '60.000',
            'E': '40.000',
        },
        'D',
        'Toplam miktar 10.000 kg. A payı = 200.000 × (8.000 ÷ 10.000) = 160.000 ₺. A brüt kârı = 220.000 − 160.000 = **60.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0044': cost_patch(
        "Birleşik maliyeti 180.000 ₺ olan süreçte A ve B ürünleri elde edilir. A: nihai satış 200.000 ₺, ayrım sonrası ilave işleme 50.000 ₺; B: nihai satış 120.000 ₺, ilave işleme 30.000 ₺. Net gerçekleşebilir değer (NGD) esasına göre A'ya düşen pay kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '67.500',
            'C': '90.000',
            'D': '150.000',
            'E': '112.500',
        },
        'E',
        'NGD = nihai satış − ilave işleme. A NGD = 200.000 − 50.000 = 150.000 ₺; B NGD = 120.000 − 30.000 = 90.000 ₺; toplam 240.000 ₺. A payı = 180.000 × (150.000 ÷ 240.000) = **112.500 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0059': cost_patch(
        "Birleşik maliyeti 240.000 ₺ olan süreçte P ve Q ürünleri elde edilir. P: nihai satış 300.000 ₺, ilave işleme 60.000 ₺; Q: nihai satış 200.000 ₺, ilave işleme 40.000 ₺. NGD esasına göre P'ye düşen pay kaç ₺'dir?",
        {
            'A': '96.000',
            'B': '120.000',
            'C': '180.000',
            'D': '144.000',
            'E': '150.000',
        },
        'D',
        'P NGD = 300.000 − 60.000 = 240.000 ₺; Q NGD = 200.000 − 40.000 = 160.000 ₺; toplam 400.000 ₺. P payı = 240.000 × (240.000 ÷ 400.000) = **144.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0033': cost_patch(
        "Birleşik maliyeti 150.000 ₺ olan süreçte M ve N ürünleri elde edilir. M NGD 200.000 ₺, N NGD 100.000 ₺'dir. N ürünü 2.000 birim ise N ürününün BİRİM birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '50',
            'B': '20',
            'C': '100',
            'D': '75',
            'E': '25',
        },
        'E',
        'Toplam NGD = 300.000 ₺. N payı = 150.000 × (100.000 ÷ 300.000) = 50.000 ₺. N birim = 50.000 ÷ 2.000 = **25 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0028': cost_patch(
        "Ana ürünün toplam birleşik maliyeti 200.000 ₺'dir; süreçte ortaya çıkan yan ürünün net gerçekleşebilir değeri 30.000 ₺'dir. Yan ürün değeri birleşik maliyetten düşülüyorsa ve ana üründen 8.500 birim elde edilmişse, ana ürünün BİRİM maliyeti kaç ₺'dir?",
        {
            'A': '23,53',
            'B': '25',
            'C': '30',
            'D': '20',
            'E': '17,65',
        },
        'D',
        "Yan ürün NGD'si ana ürün maliyetinden düşülür: net ana maliyet = 200.000 − 30.000 = 170.000 ₺. Ana ürün birim maliyeti = 170.000 ÷ 8.500 = **20 ₺**. (Yan ürünü düşmemek 23,53 verir.)",
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0031': cost_patch(
        'Birleşik maliyeti 120.000 ₺ olan süreçte A 2.000 kg (satış değeri 300.000 ₺), B 6.000 kg (satış değeri 100.000 ₺) elde edilmiştir. A ürününe düşen pay, satış değeri yöntemine göre fiziki ölçü yöntemine göre olandan kaç ₺ FAZLADIR?',
        {
            'A': '30.000',
            'B': '90.000',
            'C': '60.000',
            'D': '120.000',
            'E': '45.000',
        },
        'C',
        "Fiziki ölçü: A payı = 120.000 × (2.000 ÷ 8.000) = 30.000 ₺. Satış değeri: A payı = 120.000 × (300.000 ÷ 400.000) = 90.000 ₺. Fark = 90.000 − 30.000 = **60.000 ₺** (satış değeri yöntemi A'ya daha fazla pay verir).",
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0035': cost_patch(
        'Birleşik maliyeti 150.000 ₺ olan süreçte M 5.000 kg (satış değeri 200.000 ₺), N 5.000 kg (satış değeri 100.000 ₺) elde edilmiştir. M ürününe düşen pay, satış değeri yöntemi ile fiziki ölçü yöntemi arasında kaç ₺ FARK eder?',
        {
            'A': '50.000',
            'B': '75.000',
            'C': '100.000',
            'D': '25.000',
            'E': '0',
        },
        'D',
        'Fiziki ölçü: M payı = 150.000 × (5.000 ÷ 10.000) = 75.000 ₺. Satış değeri: M payı = 150.000 × (200.000 ÷ 300.000) = 100.000 ₺. Fark = 100.000 − 75.000 = **25.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0053': cost_patch(
        "Bir birleşik ürün ayrım noktasında 100.000 ₺'ye satılabilmektedir. İlave işlemeden geçirilirse 150.000 ₺'ye satılabilecek, ilave işleme maliyeti 30.000 ₺ olacaktır. Doğru karar ve net etkisi nedir?",
        {
            'A': 'İlave işlenmemeli; net 30.000 ₺ zarar eder',
            'B': 'İlave işlenmeli; net 50.000 ₺ katkı sağlar',
            'C': 'Fark etmez; iki seçenek eşittir',
            'D': 'İlave işlenmemeli; birleşik maliyet 100.000 ₺ aşılır',
            'E': 'İlave işlenmeli; net 20.000 ₺ katkı sağlar',
        },
        'E',
        'Karar ayrım sonrası verilere göre verilir (birleşik maliyet batmıştır, dikkate alınmaz). Ek gelir = 150.000 − 100.000 = 50.000 ₺; ek maliyet = 30.000 ₺. Ek gelir > ek maliyet olduğundan ilave işlenmeli; net katkı = 50.000 − 30.000 = **20.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0023': cost_patch(
        "Birleşik maliyeti 240.000 ₺ olan süreçte A ve B elde edilir. A NGD 180.000 ₺, B NGD 60.000 ₺'dir. A ürünü 3.000 birim ise A'nın BİRİM birleşik maliyet payı kaç ₺'dir?",
        {
            'A': '80',
            'B': '45',
            'C': '60',
            'D': '90',
            'E': '20',
        },
        'C',
        'Toplam NGD = 240.000 ₺. A payı = 240.000 × (180.000 ÷ 240.000) = 180.000 ₺. A birim = 180.000 ÷ 3.000 = **60 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
    'mmuh-birlesik-gen-0024': cost_patch(
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
    'mmuh-birlesik-gen-0038': cost_patch(
        "Satış değeri esaslı dağıtımda A ürününe 120.000 ₺ pay düşmüştür. A ürününün satış değeri 400.000 ₺, tüm ürünlerin toplam satış değeri 1.000.000 ₺ olduğuna göre toplam birleşik maliyet kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '480.000',
            'C': '300.000',
            'D': '48.000',
            'E': '250.000',
        },
        'C',
        'A payı = J × (A satış değeri ÷ toplam) → 120.000 = J × (400.000 ÷ 1.000.000) = J × 0,4. Toplam birleşik maliyet J = 120.000 ÷ 0,4 = **300.000 ₺**.',
        'Maliyet muhasebesi - birleşik maliyet (çok adımlı)',
    ),
}

STANDART_HARDER_PATCHES = {
    'mmuh-standart-gen-0011': cost_patch(
        "Bir mamulün birim başına standart DİMM tüketimi 5 kg, standart fiyatı 10 ₺/kg'dır. Dönemde 1.000 birim üretilmiş; fiilen 5.200 kg malzeme kullanılmış ve kg başına 11 ₺ ödenmiştir. Toplam DİMM sapması ne kadardır ve yönü nedir?",
        {
            'A': '7.200 ₺ lehte',
            'B': '5.200 ₺ aleyhte',
            'C': '7.200 ₺ aleyhte',
            'D': '2.000 ₺ aleyhte',
            'E': '1.000 ₺ aleyhte',
        },
        'C',
        'Standart maliyet = 1.000 birim × 5 kg × 10 ₺ = 50.000 ₺. Fiili maliyet = 5.200 kg × 11 ₺ = 57.200 ₺. Toplam sapma = fiili − standart = 57.200 − 50.000 = **7.200 ₺ aleyhte** (fiili > standart). Bu sapma 5.200 ₺ fiyat + 2.000 ₺ miktar sapmasından oluşur.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0012': cost_patch(
        'Bir mobilya atölyesinde mamul başına standart malzeme tüketimi 5 kg, standart alış fiyatı kg başına 10 ₺ olarak belirlenmiştir. Ay içinde 1.000 birim üretilirken depodan 5.200 kg malzeme çekilmiş; tedarikçi faturasında kg fiyatı 11 ₺ görünmektedir. Malzemenin birim fiyatındaki farklılıktan doğan sapma ne kadardır ve yönü nedir?',
        {
            'A': '5.000 ₺ aleyhte',
            'B': '5.200 ₺ lehte',
            'C': '7.200 ₺ aleyhte',
            'D': '2.000 ₺ aleyhte',
            'E': '5.200 ₺ aleyhte',
        },
        'E',
        'Fiyat sapması = (fiili fiyat − standart fiyat) × **fiili miktar** = (11 − 10) × 5.200 = **5.200 ₺ aleyhte**. Fiyat sapmasında standart miktar değil fiili miktar kullanılır; standart miktarla (5.000 kg) hesaplamak 5.000 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0013': cost_patch(
        "Bir mamulün birim başına standart DİMM tüketimi 5 kg, standart fiyatı 10 ₺/kg'dır. Dönemde 1.000 birim üretilmiş, fiilen 5.200 kg malzeme kullanılmıştır. DİMM MİKTAR (kullanım) sapması ne kadardır ve yönü nedir?",
        {
            'A': '2.200 ₺ aleyhte',
            'B': '2.000 ₺ aleyhte',
            'C': '2.000 ₺ lehte',
            'D': '5.200 ₺ aleyhte',
            'E': '200 ₺ aleyhte',
        },
        'B',
        'Standart miktar = 1.000 birim × 5 kg = 5.000 kg. Miktar sapması = (fiili miktar − standart miktar) × **standart fiyat** = (5.200 − 5.000) × 10 = **2.000 ₺ aleyhte**. Miktar sapmasında fiili fiyat değil standart fiyat kullanılır (aksi hâlde 2.200 ₺ bulunur).',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0015': cost_patch(
        "Bir mamulün birim başına standart direkt işçilik süresi 2 saat, standart saat ücreti 20 ₺'dir. Dönemde 1.000 birim üretilmiş; fiilen 2.100 saat çalışılmış ve saat başına 22 ₺ ödenmiştir. Toplam direkt işçilik sapması ne kadardır ve yönü nedir?",
        {
            'A': '6.200 ₺ aleyhte',
            'B': '6.200 ₺ lehte',
            'C': '4.200 ₺ aleyhte',
            'D': '2.000 ₺ aleyhte',
            'E': '2.100 ₺ aleyhte',
        },
        'A',
        'Standart DİG = 1.000 birim × 2 saat × 20 ₺ = 40.000 ₺. Fiili DİG = 2.100 saat × 22 ₺ = 46.200 ₺. Toplam sapma = 46.200 − 40.000 = **6.200 ₺ aleyhte**. Bu sapma 4.200 ₺ ücret + 2.000 ₺ süre sapmasının toplamıdır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0016': cost_patch(
        "Bir mamulün birim başına standart direkt işçilik süresi 2 saat, standart saat ücreti 20 ₺'dir. Dönemde 1.000 birim üretilmiş; fiilen 2.100 saat çalışılmış ve saat başına 22 ₺ ödenmiştir. Direkt işçilik ÜCRET (fiyat) sapması ne kadardır ve yönü nedir?",
        {
            'A': '4.000 ₺ aleyhte',
            'B': '4.200 ₺ lehte',
            'C': '6.200 ₺ aleyhte',
            'D': '4.200 ₺ aleyhte',
            'E': '2.000 ₺ aleyhte',
        },
        'D',
        'Ücret sapması = (fiili ücret − standart ücret) × **fiili süre** = (22 − 20) × 2.100 = **4.200 ₺ aleyhte**. Standart süre (2.000 saat) ile hesaplamak 4.000 ₺ verir ve yanlıştır; ücret sapmasında fiili süre esas alınır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0017': cost_patch(
        "Bir mamulün birim başına standart direkt işçilik süresi 2 saat, standart saat ücreti 20 ₺'dir. Dönemde 1.000 birim üretilmiş, fiilen 2.100 saat çalışılmıştır. Direkt işçilik SÜRE (verimlilik) sapması ne kadardır ve yönü nedir?",
        {
            'A': '2.200 ₺ aleyhte',
            'B': '2.000 ₺ lehte',
            'C': '2.000 ₺ aleyhte',
            'D': '4.200 ₺ aleyhte',
            'E': '100 ₺ aleyhte',
        },
        'C',
        'Standart süre = 1.000 birim × 2 saat = 2.000 saat. Süre sapması = (fiili süre − standart süre) × **standart ücret** = (2.100 − 2.000) × 20 = **2.000 ₺ aleyhte**. Fiili ücretle (22 ₺) hesaplamak 2.200 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0023': cost_patch(
        "Bir işletme 2.000 birim mamul üretmiştir; birim başına standart DİMM 3 kg ve standart fiyat 12 ₺/kg'dır. Dönemde fiilen 6.500 kg malzeme kullanılmış ve kg başına 11 ₺ ödenmiştir. DİMM FİYAT sapması ne kadardır ve yönü nedir?",
        {
            'A': '6.000 ₺ lehte',
            'B': '6.500 ₺ aleyhte',
            'C': '500 ₺ lehte',
            'D': '6.000 ₺ aleyhte',
            'E': '6.500 ₺ lehte',
        },
        'E',
        'Fiyat sapması = (fiili fiyat − standart fiyat) × fiili miktar = (11 − 12) × 6.500 = −6.500 ₺, yani **6.500 ₺ lehte** (standarttan düşük fiyata alınmış). Standart miktar (6.000 kg) ile hesaplamak 6.000 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0024': cost_patch(
        "Bir işletme 2.000 birim mamul üretmiştir; birim başına standart DİMM 3 kg ve standart fiyat 12 ₺/kg'dır. Dönemde fiilen 6.500 kg malzeme kullanılmıştır. DİMM MİKTAR (kullanım) sapması ne kadardır ve yönü nedir?",
        {
            'A': '6.000 ₺ aleyhte',
            'B': '5.500 ₺ aleyhte',
            'C': '6.000 ₺ lehte',
            'D': '500 ₺ aleyhte',
            'E': '6.500 ₺ aleyhte',
        },
        'A',
        'Standart miktar = 2.000 birim × 3 kg = 6.000 kg. Miktar sapması = (6.500 − 6.000) × standart fiyat 12 = **6.000 ₺ aleyhte** (standarttan 500 kg fazla kullanılmış). Fiili fiyatla (11 ₺) hesaplamak 5.500 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0025': cost_patch(
        "Bir işletme 2.000 birim mamul üretmiştir; birim başına standart DİMM 3 kg ve standart fiyat 12 ₺/kg'dır. Dönemde fiilen 6.500 kg malzeme kullanılmış ve kg başına 11 ₺ ödenmiştir. Toplam (net) DİMM sapması ne kadardır ve yönü nedir?",
        {
            'A': '500 ₺ aleyhte',
            'B': '500 ₺ lehte',
            'C': '12.500 ₺ aleyhte',
            'D': '6.500 ₺ lehte',
            'E': '6.000 ₺ aleyhte',
        },
        'B',
        'Standart maliyet = 6.000 kg × 12 = 72.000 ₺; fiili maliyet = 6.500 kg × 11 = 71.500 ₺. Toplam sapma = 71.500 − 72.000 = −500 ₺, yani **500 ₺ lehte**. (Kontrol: 6.500 ₺ lehte fiyat sapması + 6.000 ₺ aleyhte miktar sapması = 500 ₺ lehte.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0028': cost_patch(
        "Bir işletme 500 birim mamul üretmiştir; birim başına standart DİMM 2 kg ve standart fiyat 20 ₺/kg'dır. Dönemde fiilen 1.100 kg malzeme kullanılmış ve kg başına 18 ₺ ödenmiştir. DİMM FİYAT sapması ne kadardır ve yönü nedir?",
        {
            'A': '2.000 ₺ lehte',
            'B': '2.200 ₺ aleyhte',
            'C': '200 ₺ lehte',
            'D': '2.200 ₺ lehte',
            'E': '2.000 ₺ aleyhte',
        },
        'D',
        'Fiyat sapması = (18 − 20) × fiili miktar 1.100 = −2.200 ₺, yani **2.200 ₺ lehte**. Standart miktar (1.000 kg) kullanılırsa 2.000 ₺ bulunur; fiyat sapmasında fiili miktar esastır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0029': cost_patch(
        "Bir atölyede üretilen 500 birim mamul için malzeme standardı birim başına 2 kg, standart fiyat ise kg başına 20 ₺'dir. Dönem sonu kayıtları 1.100 kg tüketim ve kg başına 18 ₺ alış fiyatı göstermektedir. Malzeme açısından standart maliyet ile fiili maliyet arasındaki NET fark ne kadardır ve yönü nedir?",
        {
            'A': '200 ₺ aleyhte',
            'B': '4.200 ₺ lehte',
            'C': '200 ₺ lehte',
            'D': '2.000 ₺ aleyhte',
            'E': '2.200 ₺ lehte',
        },
        'C',
        'Standart maliyet = 500 × 2 × 20 = 20.000 ₺; fiili maliyet = 1.100 × 18 = 19.800 ₺. Toplam sapma = 19.800 − 20.000 = **200 ₺ lehte**. (Kontrol: 2.200 ₺ lehte fiyat + 2.000 ₺ aleyhte miktar sapması = 200 ₺ lehte.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0031': cost_patch(
        "Bir işletme dönemde 2.000 birim mamul üretmiştir. Bu üretim için hesaplanan standart DİMM maliyeti 72.000 ₺ ve standart malzeme fiyatı 12 ₺/kg olduğuna göre mamulün birim başına standart malzeme tüketimi kaç kg'dır?",
        {
            'A': '3',
            'B': '6',
            'C': '36',
            'D': '2',
            'E': '1,5',
        },
        'A',
        'Standart maliyet = üretim × birim standart miktar × standart fiyat. Toplam standart miktar = 72.000 ÷ 12 = 6.000 kg. Birim başına standart tüketim = 6.000 ÷ 2.000 = **3 kg**.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0032': cost_patch(
        "Bir imalatçıda mamul başına malzeme standardı 4 kg olup standart fiyat 15 ₺/kg'dır. Dönem boyunca 1.500 birim imal edilmiş, depo kayıtlarına göre 6.300 kg malzeme çıkışı yapılmış ve malzeme kg başına 14 ₺'ye temin edilmiştir. Standart maliyet ile fiili maliyet karşılaştırıldığında ortaya çıkan net sapma ne kadardır ve yönü nedir?",
        {
            'A': '1.800 ₺ aleyhte',
            'B': '6.300 ₺ lehte',
            'C': '4.500 ₺ aleyhte',
            'D': '10.800 ₺ lehte',
            'E': '1.800 ₺ lehte',
        },
        'E',
        'Standart maliyet = 1.500 × 4 × 15 = 90.000 ₺; fiili maliyet = 6.300 × 14 = 88.200 ₺. Toplam sapma = 88.200 − 90.000 = **1.800 ₺ lehte**. (Kontrol: 6.300 ₺ lehte fiyat + 4.500 ₺ aleyhte miktar = 1.800 ₺ lehte.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0033': cost_patch(
        "Bir işletme 1.500 birim mamul üretmiştir; birim başına standart DİMM 4 kg ve standart fiyat 15 ₺/kg'dır. Dönemde fiilen 6.300 kg malzeme kullanılmıştır. DİMM MİKTAR (kullanım) sapması ne kadardır ve yönü nedir?",
        {
            'A': '4.200 ₺ aleyhte',
            'B': '4.500 ₺ aleyhte',
            'C': '4.500 ₺ lehte',
            'D': '300 ₺ aleyhte',
            'E': '6.300 ₺ aleyhte',
        },
        'B',
        'Standart miktar = 1.500 × 4 = 6.000 kg. Miktar sapması = (6.300 − 6.000) × standart fiyat 15 = **4.500 ₺ aleyhte**. Fiili fiyatla (14 ₺) hesaplamak 4.200 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0036': cost_patch(
        'Bir üründe standart DİMM 4 kg × 15 ₺ = 60 ₺/birim olarak belirlenmiştir. Dönemde 1.000 birim üretilmiş; fiilen 4.200 kg malzeme kullanılmış ve kg başına 16 ₺ ödenmiştir. DİMM FİYAT sapması ne kadardır ve yönü nedir?',
        {
            'A': '4.000 ₺ aleyhte',
            'B': '4.200 ₺ lehte',
            'C': '7.200 ₺ aleyhte',
            'D': '4.200 ₺ aleyhte',
            'E': '3.000 ₺ aleyhte',
        },
        'D',
        'Fiyat sapması = (16 − 15) × fiili miktar 4.200 = **4.200 ₺ aleyhte**. Standart miktar (1.000 × 4 = 4.000 kg) ile hesaplamak 4.000 ₺ verir; fiyat sapmasında fiili miktar kullanılır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0037': cost_patch(
        "Bir işletmede dönemde 1.000 birim üretilmiş (birim standart DİMM 4 kg, standart fiyat 15 ₺/kg) ve fiilen 4.200 kg malzeme kullanılmıştır. DİMM fiyat sapması 4.200 ₺ aleyhte olarak hesaplandığına göre malzemenin fiili alış fiyatı kaç ₺/kg'dır?",
        {
            'A': '14',
            'B': '15',
            'C': '16',
            'D': '16,05',
            'E': '17',
        },
        'C',
        'Fiyat sapması = (fiili fiyat − standart fiyat) × fiili miktar. Buradan fiili fiyat = standart fiyat + (sapma ÷ fiili miktar) = 15 + (4.200 ÷ 4.200) = 15 + 1 = **16 ₺/kg**. Sapma aleyhte olduğundan fiili fiyat standardın üzerindedir.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0039': cost_patch(
        "Bir işletme 800 birim mamul üretmiştir; birim başına standart DİMM 5 kg ve standart fiyat 10 ₺/kg'dır. Dönemde fiilen 3.800 kg malzeme kullanılmıştır. DİMM MİKTAR (kullanım) sapması ne kadardır ve yönü nedir?",
        {
            'A': '2.000 ₺ lehte',
            'B': '2.000 ₺ aleyhte',
            'C': '200 ₺ lehte',
            'D': '4.000 ₺ lehte',
            'E': '38.000 ₺ lehte',
        },
        'A',
        'Standart miktar = 800 × 5 = 4.000 kg. Miktar sapması = (3.800 − 4.000) × 10 = −2.000 ₺, yani **2.000 ₺ lehte** (standarttan 200 kg az malzeme kullanılmış; verimli kullanım).',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0043': cost_patch(
        "Bir işletme 1.200 birim mamul üretmiştir; birim başına standart direkt işçilik süresi 3 saat ve standart saat ücreti 25 ₺'dir. Dönemde fiilen 3.500 saat çalışılmış ve saat başına 26 ₺ ödenmiştir. Direkt işçilik ÜCRET sapması ne kadardır ve yönü nedir?",
        {
            'A': '3.600 ₺ aleyhte',
            'B': '3.500 ₺ lehte',
            'C': '1.000 ₺ aleyhte',
            'D': '2.500 ₺ aleyhte',
            'E': '3.500 ₺ aleyhte',
        },
        'E',
        'Ücret sapması = (26 − 25) × fiili süre 3.500 = **3.500 ₺ aleyhte**. Standart süre (1.200 × 3 = 3.600 saat) ile hesaplamak 3.600 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0044': cost_patch(
        "Bir işletme 1.200 birim mamul üretmiştir; birim başına standart direkt işçilik süresi 3 saat ve standart saat ücreti 25 ₺'dir. Dönemde fiilen 3.500 saat çalışılmıştır. Direkt işçilik SÜRE (verimlilik) sapması ne kadardır ve yönü nedir?",
        {
            'A': '2.600 ₺ lehte',
            'B': '2.500 ₺ lehte',
            'C': '2.500 ₺ aleyhte',
            'D': '3.500 ₺ lehte',
            'E': '100 ₺ lehte',
        },
        'B',
        'Standart süre = 1.200 × 3 = 3.600 saat. Süre sapması = (3.500 − 3.600) × standart ücret 25 = −2.500 ₺, yani **2.500 ₺ lehte** (standarttan 100 saat az çalışılmış). Fiili ücretle (26 ₺) hesaplamak 2.600 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0045': cost_patch(
        "Bir işletme 1.200 birim mamul üretmiştir; birim başına standart direkt işçilik süresi 3 saat ve standart saat ücreti 25 ₺'dir. Dönemde fiilen 3.500 saat çalışılmış ve saat başına 26 ₺ ödenmiştir. Toplam (net) direkt işçilik sapması ne kadardır ve yönü nedir?",
        {
            'A': '1.000 ₺ lehte',
            'B': '6.000 ₺ aleyhte',
            'C': '3.500 ₺ aleyhte',
            'D': '1.000 ₺ aleyhte',
            'E': '2.500 ₺ lehte',
        },
        'D',
        'Standart DİG = 1.200 × 3 × 25 = 90.000 ₺; fiili DİG = 3.500 × 26 = 91.000 ₺. Toplam sapma = 91.000 − 90.000 = **1.000 ₺ aleyhte**. (Kontrol: 3.500 ₺ aleyhte ücret + 2.500 ₺ lehte süre sapması = 1.000 ₺ aleyhte.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0049': cost_patch(
        'Bir işletme 1.200 birim mamul üretmiştir; birim başına standart süre 3 saat ve standart GÜG yükleme oranı 5 ₺/saattir. Dönemin fiili genel üretim gideri 19.500 ₺ olduğuna göre GÜG toplam sapması ne kadardır ve yönü nedir?',
        {
            'A': '1.500 ₺ lehte',
            'B': '18.000 ₺ aleyhte',
            'C': '3.900 ₺ aleyhte',
            'D': 'Sapma oluşmaz',
            'E': '1.500 ₺ aleyhte',
        },
        'E',
        "Mamullere yüklenen (standart) GÜG = standart saat × oran = (1.200 × 3) × 5 = 3.600 × 5 = 18.000 ₺. Fiili GÜG 19.500 ₺'dir. Toplam sapma = 19.500 − 18.000 = **1.500 ₺ aleyhte** (fiili gider standardın üzerinde).",
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0052': cost_patch(
        'Bir tekstil işletmesinde 1.000 birim üretim için birim başına standart süre 3 saat, standart saat ücreti 25 ₺ olarak belirlenmiştir. Dönem sonunda direkt işçilik süre (verimlilik) sapması 2.500 ₺ LEHTE olarak hesaplandığına göre dönemde fiilen kaç saat çalışılmıştır?',
        {
            'A': '2.900',
            'B': '3.100',
            'C': '3.000',
            'D': '2.500',
            'E': '2.800',
        },
        'A',
        'Standart süre = 1.000 × 3 = 3.000 saat. Süre sapması = (fiili süre − standart süre) × standart ücret olduğundan sapma tutarının karşılığı 2.500 ÷ 25 = 100 saattir. Sapma **lehte** olduğu için fiili süre standardın altındadır: 3.000 − 100 = **2.900 saat**. (Aleyhte olsaydı 3.100 saat bulunurdu.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0059': cost_patch(
        'Bir üründe standart direkt işçilik 4 saat/birim ve standart ücret 30 ₺/saat olarak belirlenmiştir. Dönemde 1.000 birim üretilmiş; fiilen 4.200 saat çalışılmış ve saat başına 28 ₺ ödenmiştir. Toplam (net) direkt işçilik sapması ne kadardır ve yönü nedir?',
        {
            'A': '2.400 ₺ aleyhte',
            'B': '8.400 ₺ lehte',
            'C': '6.000 ₺ aleyhte',
            'D': '200 ₺ lehte',
            'E': '2.400 ₺ lehte',
        },
        'E',
        'Standart DİG = 1.000 × 4 × 30 = 120.000 ₺; fiili DİG = 4.200 × 28 = 117.600 ₺. Toplam sapma = 117.600 − 120.000 = **2.400 ₺ lehte**. (Kontrol: ücret sapması (28 − 30) × 4.200 = 8.400 ₺ lehte; süre sapması (4.200 − 4.000) × 30 = 6.000 ₺ aleyhte; net 2.400 ₺ lehte.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    'mmuh-standart-gen-0021': cost_patch(
        'Direkt ilk madde ve malzeme (DİMM) FİYAT sapması nasıl hesaplanır?',
        {
            'A': '(Fiili miktar − Standart miktar) × Standart fiyat',
            'B': '(Fiili fiyat − Standart fiyat) × Fiili miktar',
            'C': '(Fiili fiyat − Standart fiyat) × Standart miktar',
            'D': 'Fiili maliyet + Standart maliyet',
            'E': 'Fiili fiyat × Standart miktar',
        },
        'B',
        'DİMM **fiyat sapması = (Fiili fiyat − Standart fiyat) × Fiili miktar**. Fiyat farkı, fiilen kullanılan miktar üzerinden ölçülür.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
}

PATCHES_BY_PATH = {
    MHK_RELATIVE_PATH: MHK_HARDER_PATCHES,
    BIRLESIK_RELATIVE_PATH: BIRLESIK_HARDER_PATCHES,
    STANDART_RELATIVE_PATH: STANDART_HARDER_PATCHES,
}


def apply_or_check(path, patches, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    mismatches = []
    for qid, fields in patches.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{qid}")
        for field, expected in fields.items():
            if q.get(field) != expected:
                mismatches.append(f"{path}::{qid}.{field}")
                if write:
                    q[field] = expected
        if write and len(set(q["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true"); g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    mismatches = []
    for rel, patches in PATCHES_BY_PATH.items():
        for path in (ROOT / rel, APP_ROOT / rel):
            mismatches.extend(apply_or_check(path, patches, args.write))
    if args.check and mismatches:
        print("Eşleşmeyen alanlar:")
        for m in mismatches: print(f"- {m}")
        return 1
    total = sum(len(p) for p in PATCHES_BY_PATH.values())
    print(f"{len(PATCHES_BY_PATH)} paket / {total} soru (harder) iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
