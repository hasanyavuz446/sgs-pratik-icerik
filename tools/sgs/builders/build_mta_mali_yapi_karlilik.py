#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mali Yapi, Faaliyet ve Karlilik Oranlari — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

YENI KONU (mali tablolar analizi). Gercek sinavda mali yapi 14, devir 11, karlilik 11, piyasa 4 soru; trend ve fon akim analizinin (2019-2026'da 0 soru) yerine acildi. 60 soru her biri kendi verisiyle: kaldirac/ozkaynak orani/borc-ozkaynak/ozsermaye carpani (sinav tanimi: finansal kaldirac = YK/aktif), kredi limiti, ozkaynak hesabi, faiz karsilama, vade yapisi, islemlerin etkisi; alacak/borc/stok sureleri, nakit donusum suresi, duran varlik ve ozkaynak devir hizi, kredili satis; marjlar, ortalama aktif/ozkaynak ile karlilik, DuPont, kaldiracin olumlu etki kosulu; F/K, PD/DD, temettu verimi, kar dagitim orani, pay getirisi. Oranlar Fraction ile hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Mali tablolar analizi - mali yapi, faaliyet ve karlilik oranlari
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/mali_tablolar_analizi/mali_yapi_ve_karlilik.json"
STYLE_REF = 'SGS Mali Tablolar Analizi (oran zinciri, ters hesap; gerçek sınav profiline kalibre)'
ONEK = "mta-yapi-gen-"


def patch(stem, options, answer, solution, ref='Mali analiz - mali yapı oranları'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin bilançosunda aktif toplamı 800.000 ₺, kısa vadeli yabancı kaynaklar 200.000 ₺, uzun vadeli yabancı kaynaklar 280.000 ₺ ve özkaynaklar 320.000 ₺'dir. Buna göre finansal kaldıraç oranı, özkaynak oranı ve borç/özkaynak oranı sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
        {
            'A': '0,60 · 0,40 · 1,50',
            'B': '0,60 · 0,40 · 0,67',
            'C': '0,35 · 0,40 · 1,50',
            'D': '0,40 · 0,60 · 0,67',
            'E': '1,50 · 0,40 · 0,60',
        },
        'A',
        'Finansal kaldıraç = yabancı kaynaklar ÷ aktif = 480.000 ÷ 800.000 = **0,60**; özkaynak oranı = 320.000 ÷ 800.000 = **0,40**; borç/özkaynak = 480.000 ÷ 320.000 = **1,50**.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0002': patch(
        "Finansal kaldıraç oranı 0,70 olan bir işletmenin özkaynakları 90.000 ₺'dir. Buna göre toplam borçları kaç ₺'dir?",
        {
            'A': '210.000',
            'B': '357.000',
            'C': '300.000',
            'D': '291.000',
            'E': '90.000',
        },
        'A',
        'Özkaynak oranı 0,30 → aktif = 90.000 ÷ 0,30 = 300.000 ₺. Borçlar = 300.000 × 0,70 = **210.000 ₺**.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0003': patch(
        "Bir inşaat malzemesi üreticisi kapasite artırımı için yüksek tutarlı banka kredisi kullanmıştır. Dönem sonu gelir tablosuna göre işletmenin vergi öncesi kârı 360.000 ₺, kredilere ilişkin faiz giderleri 90.000 ₺'dir. Kredi veren banka, işletmenin faiz ödeme gücünü faiz karşılama oranıyla izlemektedir.\n\nBuna göre işletmenin faiz karşılama oranı kaçtır?",
        {
            'A': '2',
            'B': '0,25',
            'C': '5',
            'D': '3',
            'E': '4',
        },
        'C',
        'Faiz karşılama oranı = faiz ve vergi öncesi kâr ÷ faiz gideri = (360.000 + 90.000) ÷ 90.000 = **5**. Vergi öncesi kârı doğrudan bölmek (4) faizi iki kez düşmek olur.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0004': patch(
        'Kısa vadeli yabancı kaynakları 180.000 ₺, uzun vadeli yabancı kaynakları 120.000 ₺ olan bir işletmede kısa vadeli borçların toplam borçlar içindeki payı yüzde kaçtır?',
        {
            'A': '%66,67',
            'B': '%80',
            'C': '%30',
            'D': '%150',
            'E': '%60',
        },
        'E',
        '180.000 ÷ (180.000 + 120.000) = **%60**. Kısa vadeli borç ağırlığının yüksek olması vade uyumsuzluğu riskini artırır.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0005': patch(
        "Bir işletmenin bilançosunda aktif toplamı 1.000.000 ₺, kısa vadeli yabancı kaynaklar 250.000 ₺, uzun vadeli yabancı kaynaklar 350.000 ₺, duran varlıklar 650.000 ₺'dir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Duran varlıkların devamlı sermayeye oranı 0,87'dir.",
            'B': "Borç/özkaynak oranı 1,50'dir.",
            'C': 'Duran varlıklar özkaynaklarla tamamen karşılanmaktadır.',
            'D': "Finansal kaldıraç oranı 0,60'tır.",
            'E': "Özsermaye çarpanı 2,50'dir.",
        },
        'C',
        'Özkaynak = 1.000.000 − 600.000 = 400.000 ₺; duran varlıklar (650.000) özkaynaktan büyüktür, bir kısmı uzun vadeli borçla finanse edilir. Kaldıraç 0,60; çarpan 2,50; borç/özkaynak 1,50; duran ÷ devamlı sermaye = 650.000 ÷ 750.000 ≈ 0,87 doğrudur.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0006': patch(
        'Bir işletmenin yönetimi, yeni bir yatırımın özkaynakla mı yoksa banka kredisiyle mi finanse edileceğini değerlendirmektedir. Finans müdürü, borçla finansmanın ortakların özkaynak kârlılığını artırabileceğini, ancak bunun belirli bir koşula bağlı olduğunu belirtmiştir.\n\nFinansal kaldıracın özkaynak kârlılığını olumlu etkilemesi için aşağıdaki koşullardan hangisi sağlanmalıdır?',
        {
            'A': 'Özkaynaklar toplam borçlardan büyük olmalıdır.',
            'B': 'Borçlanma maliyeti aktif kârlılığından yüksek olmalıdır.',
            'C': 'Varlıkların getirisi (aktif kârlılığı) borçlanma maliyetinden yüksek olmalıdır.',
            'D': "Cari oran 1'den küçük olmalıdır.",
            'E': "Aktif devir hızı 1'in altında olmalıdır.",
        },
        'C',
        'Borçla sağlanan fon, maliyetinden fazla getiri sağlarsa aradaki fark ortaklara kalır ve özkaynak kârlılığı yükselir; tersi durumda kaldıraç özkaynak kârlılığını düşürür.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletmenin ortalama stokta kalma süresi 50 gün, ortalama alacak tahsil süresi 40 gün, ortalama borç ödeme süresi 30 gündür. Buna göre nakit dönüşüm süresi kaç gündür?',
        {
            'A': '20',
            'B': '80',
            'C': '90',
            'D': '60',
            'E': '120',
        },
        'D',
        'Faaliyet dönemi = 50 + 40 = 90 gün. Nakit dönüşüm süresi = faaliyet dönemi − borç ödeme süresi = 90 − 30 = **60 gün**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0008': patch(
        'Stok devir hızı 9, alacak devir hızı 12 olan bir işletmenin faaliyet dönemi kaç gündür? (1 yıl = 360 gün)',
        {
            'A': '40',
            'B': '30',
            'C': '70',
            'D': '21',
            'E': '10',
        },
        'C',
        'Stok süresi = 360 ÷ 9 = 40 gün; tahsil süresi = 360 ÷ 12 = 30 gün. Faaliyet dönemi = **70 gün**. Devir hızlarını toplamak (21) anlamsızdır.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0009': patch(
        "Bir beyaz eşya toptancısının yıllık satışlarının maliyeti 2.400.000 ₺'dir. İşletmenin stok politikasına göre mallar depoda ortalama 45 gün kalmakta, ticari alacaklar ise ortalama 60 günde tahsil edilmektedir.\n\nBuna göre işletmenin ortalama stokları kaç ₺'dir? (1 yıl = 360 gün)",
        {
            'A': '230.000',
            'B': '240.000',
            'C': '108.000',
            'D': '300.000',
            'E': '8',
        },
        'D',
        'Stok devir hızı = 360 ÷ 45 = 8 → ortalama stok = 2.400.000 ÷ 8 = **300.000 ₺**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0010': patch(
        "Bir ofis mobilyası üreticisinin yıllık net satışları 800.000 ₺, aktif devir hızı 1,6'dır. İşletme varlıklarının %40'ını yabancı kaynakla finanse etmektedir (finansal kaldıraç oranı 0,40); kısa vadeli yabancı kaynakları 120.000 ₺'dir.\n\nBuna göre işletmenin toplam borçları kaç ₺'dir?",
        {
            'A': '320.000',
            'B': '500.000',
            'C': '200.000',
            'D': '300.000',
            'E': '512.000',
        },
        'C',
        'Aktif = 800.000 ÷ 1,6 = 500.000 ₺. Borçlar = 500.000 × 0,40 = **200.000 ₺**; özkaynak 300.000 ₺.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0011': patch(
        'Bir işletmenin gelir tablosu bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Net satışlar | 800.000 |\n| Satışların maliyeti | 480.000 |\n| Faaliyet giderleri | 160.000 |\n| Finansman giderleri | 40.000 |\n| Vergi karşılığı | 30.000 |\n\nBuna göre net kâr marjı yüzde kaçtır?',
        {
            'A': '%15',
            'B': '%20',
            'C': '%11,25',
            'D': '%40',
            'E': '%12,50',
        },
        'C',
        "Brüt kâr 320.000; faaliyet kârı 160.000; vergi öncesi kâr 120.000; net kâr 90.000 ₺. Net kâr marjı = 90.000 ÷ 800.000 = **%11,25**. Faaliyet kâr marjı %20, vergi öncesi marj %15'tir.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletmenin net kârı 60.000 ₺, özkaynakları dönem başında 220.000 ₺, dönem sonunda 280.000 ₺'dir. Ortalama özkaynak kullanılarak hesaplanan özkaynak kârlılığı yüzde kaçtır?",
        {
            'A': '%24',
            'B': '%12',
            'C': '%20,73',
            'D': '%21,43',
            'E': '%20',
        },
        'A',
        'Ortalama özkaynak = 250.000 ₺. Özkaynak kârlılığı = 60.000 ÷ 250.000 = **%24**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0013': patch(
        "Bir kozmetik perakendecisinin yıllık net kârı 45.000 ₺'dir. Yatırımcılara sunulan raporda işletmenin aktif kârlılığı %9, aktif devir hızı 1,5 ve finansal kaldıraç oranı 0,45 olarak açıklanmıştır.\n\nBuna göre işletmenin net satışları kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '750.000',
            'C': '500.000',
            'D': '67.500',
            'E': '675.000',
        },
        'B',
        "Aktif = 45.000 ÷ 0,09 = 500.000 ₺; net satışlar = 500.000 × 1,5 = **750.000 ₺**. Net kâr marjı %6'dır.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0014': patch(
        'Faiz ve vergi öncesi kârı 150.000 ₺, toplam aktifleri 1.000.000 ₺ olan bir işletmenin faiz ve vergi öncesi aktif kârlılığı yüzde kaçtır?',
        {
            'A': '%20',
            'B': '%23,33',
            'C': '%15',
            'D': '%150',
            'E': '%1,50',
        },
        'C',
        'Oran = 150.000 ÷ 1.000.000 = **%15**. Faiz öncesi kâr kullanıldığından finansman yapısından bağımsız bir faaliyet başarısı ölçüsüdür.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0015': patch(
        "Bir lojistik şirketinin aktif toplamı 2.000.000 ₺'dir ve varlıklarının %60'ı yabancı kaynakla finanse edilmektedir (finansal kaldıraç oranı 0,60). Şirketin özkaynak kârlılığı %25, aktif devir hızı ise 1,2'dir.\n\nBuna göre şirketin net kârı kaç ₺'dir?",
        {
            'A': '320.000',
            'B': '200.000',
            'C': '300.000',
            'D': '500.000',
            'E': '280.000',
        },
        'B',
        'Özkaynak = 2.000.000 × 0,40 = 800.000 ₺. Net kâr = 800.000 × %25 = **200.000 ₺** (aktif kârlılığı %10).',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0016': patch(
        "Bir tekstil işletmesinin yıllık vergi öncesi kârı 200.000 ₺, özkaynakları 800.000 ₺'dir. İşletmenin kanunen kabul edilmeyen gideri bulunmamaktadır ve soruda kullanılacak vergi oranı %20'dir. Ortaklar vergi sonrası kâr üzerinden özkaynak getirisini öğrenmek istemektedir.\n\nBuna göre işletmenin özkaynak kârlılığı yüzde kaçtır?",
        {
            'A': '%35',
            'B': '%24',
            'C': '%20',
            'D': '%30',
            'E': '%25',
        },
        'C',
        'Net kâr = 200.000 × 0,80 = 160.000 ₺. Özkaynak kârlılığı = 160.000 ÷ 800.000 = **%20**. Vergi öncesi kârla %25 bulunur.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0017': patch(
        "Bir enerji şirketi bu yıl pay başına 0,60 ₺ nakit kâr payı dağıtmıştır. Şirketin paylarının borsadaki fiyatı 12 ₺'dir.\n\nBuna göre temettü verimi yüzde kaçtır?",
        {
            'A': '%0,60',
            'B': '%12',
            'C': '%20',
            'D': '%5',
            'E': '%50',
        },
        'D',
        'Temettü verimi = pay başına kâr payı ÷ pay fiyatı = 0,60 ÷ 12 = **%5**.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0018': patch(
        "Net kârı 4.000.000 ₺ ve dolaşımdaki pay sayısı 2.000.000 adet olan işletmenin pay fiyatı 20 ₺'dir. Buna göre F/K oranı kaçtır?",
        {
            'A': '10',
            'B': '0,10',
            'C': '2',
            'D': '5',
            'E': '20',
        },
        'A',
        'Pay başına kâr = 2 ₺; F/K = 20 ÷ 2 = **10**.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0019': patch(
        'Aynı sektördeki A işletmesinin net kâr marjı yüksek fakat aktif devir hızı düşük, B işletmesinin net kâr marjı düşük fakat aktif devir hızı yüksektir. İkisinin aktif kârlılığı eşittir. Buna göre aşağıdakilerden hangisi söylenebilir?',
        {
            'A': "B'nin satışlarının maliyeti A'nınkinden düşüktür.",
            'B': "B'nin net kârı A'nınkinden yüksektir.",
            'C': "A'nın özkaynak kârlılığı B'ninkinden yüksektir.",
            'D': "A varlıklarını B'den daha verimli kullanmaktadır.",
            'E': 'Aynı aktif kârlılığına A yüksek marjla, B yüksek satış hacmiyle ulaşmaktadır.',
        },
        'E',
        'Aktif kârlılığı = net kâr marjı × aktif devir hızı. Eşit sonuca farklı stratejilerle ulaşılmaktadır. Özkaynak kârlılığı kaldıraca bağlıdır; tutarlar ve maliyet yapısı bu bilgiden çıkmaz.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0020': patch(
        'Bir işletmenin satışları artarken alacak tahsil süresi kısalmış ve borç ödeme süresi uzamıştır. Bu gelişmelerin işletmenin nakit ihtiyacı üzerindeki etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Nakit dönüşüm süresi kısalacağından işletme sermayesi için gereken finansman azalır.',
            'B': 'Stok devir hızı düşer, nakit ihtiyacı artar.',
            'C': 'Faaliyet dönemi uzar, nakit dönüşüm süresi kısalır.',
            'D': 'Nakit dönüşüm süresi uzayacağından finansman ihtiyacı artar.',
            'E': 'Nakit dönüşüm süresi etkilenmez; kârlılık değişir.',
        },
        'A',
        'Tahsilatın hızlanması faaliyet dönemini kısaltır; ödemelerin gecikmesi nakit dönüşüm süresinden düşülen süreyi uzatır. İkisi birlikte nakdin işletmede bağlı kaldığı süreyi ve finansman ihtiyacını azaltır.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0021': patch(
        'Özsermaye çarpanı (toplam varlıklar ÷ özkaynaklar) 5 olan bir işletmenin finansal kaldıraç oranı kaçtır?',
        {
            'A': '0,80',
            'B': '0,20',
            'C': '4',
            'D': '0,25',
            'E': '1,25',
        },
        'A',
        "Özkaynaklar varlıkların 1/5'i = 0,20; finansal kaldıraç = 1 − 0,20 = **0,80**. Borç/özkaynak ise 4'tür.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0022': patch(
        "Toplam aktifleri 20.000.000 ₺ ve toplam borçları 9.000.000 ₺ olan bir firmanın kullanacağı yeni nakdî krediden sonra finansal kaldıraç oranı %60'ı geçmemelidir. Buna göre firma en fazla kaç ₺ kredi kullanabilir?",
        {
            'A': '5.000.000',
            'B': '12.000.000',
            'C': '4.500.000',
            'D': '3.000.000',
            'E': '7.500.000',
        },
        'E',
        '(9.000.000 + x) ÷ (20.000.000 + x) = 0,60 → 9.000.000 + x = 12.000.000 + 0,6x → 0,4x = 3.000.000 → x = **7.500.000 ₺**. Kredinin aktifi de artırdığını unutmak 3.000.000 ₺ verir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0023': patch(
        "Bir sanayi işletmesinin dönem sonu bilançosunda duran varlıkları 480.000 ₺, özkaynakları 400.000 ₺, uzun vadeli yabancı kaynakları 150.000 ₺'dir. Kredi analisti, duran varlıkların finansmanında özkaynakların yeterliliğini incelemektedir.\n\nBuna göre işletmenin duran varlıkların özkaynaklara oranı kaçtır?",
        {
            'A': '2,20',
            'B': '1,20',
            'C': '0,20',
            'D': '1,50',
            'E': '0,83',
        },
        'B',
        "Oran = 480.000 ÷ 400.000 = **1,20**. 1'in üzerinde olması, duran varlıkların bir kısmının yabancı kaynakla finanse edildiğini gösterir.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0024': patch(
        'Finansal kaldıraç oranı 0,60 ve cari oranı 1,20 olan bir işletme nakdi sermaye artırımı yapmıştır. Bu işlemin etkisiyle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her iki oran da düşer.',
            'B': 'Finansal kaldıraç oranı düşer, cari oran yükselir.',
            'C': 'Finansal kaldıraç oranı yükselir, cari oran düşer.',
            'D': 'Finansal kaldıraç oranı değişmez, cari oran yükselir.',
            'E': 'Finansal kaldıraç oranı düşer, cari oran değişmez.',
        },
        'B',
        'Nakit artışı aktifi ve dönen varlıkları büyütür; borçlar değişmez. Kaldıraç (borç ÷ aktif) düşer, cari oran (dönen ÷ KVYK) yükselir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdaki işlemlerden hangisi işletmenin finansal kaldıraç oranını azaltır?',
        {
            'A': 'Nakit karşılığı pay senedi ihracı',
            'B': 'Tahvil ihraç edilmesi',
            'C': 'Uzun vadeli banka kredisi kullanılması',
            'D': 'Ortaklara nakit kâr payı dağıtılması',
            'E': 'Kısa vadeli kredi ile ticari mal alınması',
        },
        'A',
        'Pay ihracı özkaynağı ve aktifi artırır, borç değişmez; kaldıraç düşer. Kredi ve tahvil borcu artırır; kâr payı dağıtımı özkaynak ve aktifi azaltarak kaldıracı yükseltir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0026': patch(
        "Kredili satışları 2.400.000 ₺ olan bir işletmenin ticari alacakları dönem başında 350.000 ₺, dönem sonunda 450.000 ₺'dir. Buna göre ortalama alacak tahsil süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '6',
            'B': '45',
            'C': '67,50',
            'D': '52,50',
            'E': '60',
        },
        'E',
        'Ortalama alacak = (350.000 + 450.000) ÷ 2 = 400.000 ₺; devir hızı = 2.400.000 ÷ 400.000 = 6 → tahsil süresi = 360 ÷ 6 = **60 gün**. Dönem sonu tutarıyla hesaplamak 67,50 gün verir.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0027': patch(
        "Net satışları 3.000.000 ₺ ve brüt kâr marjı %40 olan bir işletmenin ortalama stokları 300.000 ₺'dir. Buna göre ortalama stokta kalma süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '90',
            'B': '60',
            'C': '36',
            'D': '6',
            'E': '40',
        },
        'B',
        'Satışların maliyeti = 3.000.000 × %60 = 1.800.000 ₺; stok devir hızı = 1.800.000 ÷ 300.000 = 6 → süre = **60 gün**. Satışları kullanmak 36 gün verir.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0028': patch(
        "Bir danışmanlık şirketinin yıllık net satışları 1.500.000 ₺'dir; özkaynakları dönem başında 450.000 ₺, dönem sonunda 550.000 ₺'dir.\n\nOrtalama özkaynak kullanılarak hesaplanan özkaynak devir hızı kaçtır?",
        {
            'A': '0,33',
            'B': '4',
            'C': '2',
            'D': '3',
            'E': '1,50',
        },
        'D',
        'Özkaynak devir hızı = 1.500.000 ÷ 500.000 = **3**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0029': patch(
        'Bir hazır giyim üreticisinin son beş yıllık verileri incelendiğinde stok devir hızının her yıl bir önceki yıla göre düştüğü görülmüştür. Aynı dönemde işletmenin satışları yaklaşık aynı düzeyde kalmış, satış fiyatlarında önemli bir değişiklik olmamıştır.\n\nBu işletme için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Stokta kalma süresi kısalmaktadır.',
            'B': 'Stoklar satışlara göre birikmekte; stokta kalma süresi uzamaktadır.',
            'C': 'İşletmenin nakit dönüşüm süresi kısalmaktadır.',
            'D': 'Alacak tahsil süresi uzamaktadır.',
            'E': 'Stoklar daha hızlı satılmaktadır.',
        },
        'B',
        'Devir hızının düşmesi, stokların daha uzun sürede satıldığını gösterir; stok birikimi, eskime ve finansman yükü artabilir. Alacaklar hakkında bilgi yoktur.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0030': patch(
        'Net satışları 1.200.000 ₺, dönen varlıkları 300.000 ₺ ve duran varlıkları 500.000 ₺ olan bir işletmenin aktif devir hızı kaçtır?',
        {
            'A': '0,67',
            'B': '4',
            'C': '1,50',
            'D': '2',
            'E': '2,40',
        },
        'C',
        'Aktif devir hızı = 1.200.000 ÷ (300.000 + 500.000) = **1,50**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0031': patch(
        'Bir işletmenin alacak tahsil süresi 50 günden 40 güne düşerken borç ödeme süresi 30 günden 45 güne çıkmıştır. Stokta kalma süresi 60 gün olarak değişmemiştir. Buna göre nakit dönüşüm süresi nasıl değişmiştir?',
        {
            'A': 'Değişmemiştir.',
            'B': '80 günden 70 güne kısalmıştır.',
            'C': '80 günden 55 güne uzamıştır.',
            'D': '80 günden 55 güne kısalmıştır.',
            'E': '140 günden 145 güne uzamıştır.',
        },
        'D',
        'Önce: 60 + 50 − 30 = 80 gün. Sonra: 60 + 40 − 45 = **55 gün**. Tahsilatın hızlanması ve ödemelerin gecikmesi nakdin işletmede bağlı kaldığı süreyi kısaltmıştır.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0032': patch(
        'Net kâr marjı %6, aktif devir hızı 2,5 ve özsermaye çarpanı 2 olan bir işletmenin özkaynak kârlılığı yüzde kaçtır?',
        {
            'A': '%30',
            'B': '%15',
            'C': '%12',
            'D': '%7,50',
            'E': '%10,50',
        },
        'A',
        "DuPont: özkaynak kârlılığı = %6 × 2,5 × 2 = **%30**. Aktif kârlılığı %15'tir.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0033': patch(
        "Bir mutfak eşyası üreticisinin gelir tablosu analizine göre brüt kâr marjı %30, faaliyet kâr marjı %15'tir. İşletmenin faaliyet giderleri toplamı 90.000 ₺, finansman giderleri ise 25.000 ₺'dir.\n\nBuna göre işletmenin satışların maliyeti kaç ₺'dir?",
        {
            'A': '180.000',
            'B': '420.000',
            'C': '510.000',
            'D': '600.000',
            'E': '300.000',
        },
        'B',
        'Faaliyet giderleri = %30 − %15 = %15 → net satışlar = 90.000 ÷ 0,15 = 600.000 ₺. Satışların maliyeti = %70 = **420.000 ₺**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0034': patch(
        "Bir işletmenin brüt kâr marjı iki yıldır %35'te sabit kalırken net kâr marjı %9'dan %6'ya düşmüştür. Bu durumun en olası nedeni aşağıdakilerden hangisidir?",
        {
            'A': 'Satışların maliyetinin satışlara oranı artmıştır.',
            'B': 'Net satışlar azalmıştır.',
            'C': 'Satış indirimleri azalmıştır.',
            'D': 'Stok devir hızı artmıştır.',
            'E': 'Faaliyet giderleri veya finansman giderlerinin satışlara oranı artmıştır.',
        },
        'E',
        'Brüt marj sabit olduğundan sorun satışların maliyetinde değildir; brüt kârın altındaki giderlerin (faaliyet, finansman, vergi) satışlara oranı artmıştır.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0035': patch(
        "Brüt satış kârı 210.000 ₺ ve brüt kâr marjı %35 olan bir işletmenin satışların maliyeti kaç ₺'dir?",
        {
            'A': '283.500',
            'B': '600.000',
            'C': '136.500',
            'D': '390.000',
            'E': '73.500',
        },
        'D',
        'Net satışlar = 210.000 ÷ 0,35 = 600.000 ₺; satışların maliyeti = 600.000 − 210.000 = **390.000 ₺**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0036': patch(
        "Bir işletmenin 500.000 adet payının piyasa fiyatı 12 ₺, özkaynakları 4.000.000 ₺'dir. Buna göre piyasa değeri/defter değeri (PD/DD) oranı kaçtır?",
        {
            'A': '3',
            'B': '8',
            'C': '1,50',
            'D': '1,20',
            'E': '0,67',
        },
        'C',
        'Piyasa değeri = 500.000 × 12 = 6.000.000 ₺. PD/DD = 6.000.000 ÷ 4.000.000 = **1,50**.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0037': patch(
        "50 ₺'ye aldığı payı bir yıl sonra 56 ₺'ye satan yatırımcı, bu sürede pay başına 3 ₺ kâr payı almıştır. Buna göre pay senedinin getirisi yüzde kaçtır?",
        {
            'A': '%16,07',
            'B': '%18',
            'C': '%10,71',
            'D': '%6',
            'E': '%12',
        },
        'B',
        'Getiri = (56 − 50 + 3) ÷ 50 = 9 ÷ 50 = **%18**. Kâr payını unutmak %12 verir.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0038': patch(
        "Borsada işlem gören ve aynı sektörde faaliyet gösteren iki gıda şirketinden A'nın fiyat/kazanç (F/K) oranı 20, B'ninki 8'dir. İki şirketin büyüklükleri, borçluluk düzeyleri ve muhasebe politikaları birbirine benzemektedir.\n\nDiğer koşullar benzer kabul edildiğinde aşağıdakilerden hangisi söylenebilir?",
        {
            'A': "A'nın özkaynak kârlılığı B'ninkinden düşüktür.",
            'B': "Yatırımcılar A'nın kazançlarının B'ninkinden daha hızlı büyümesini bekliyor olabilir.",
            'C': "B'nin piyasa değeri A'nınkinden büyüktür.",
            'D': "B'nin payları A'nınkinden pahalıdır.",
            'E': "A'nın pay başına kârı B'ninkinden yüksektir.",
        },
        'B',
        'Yüksek F/K, yatırımcıların birim kazanç için daha fazla ödemeye razı olduğunu gösterir; genellikle yüksek büyüme beklentisini yansıtır. Pay başına kâr, piyasa değeri ya da kârlılık bu orandan tek başına çıkarılamaz.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdakilerden hangisi bir işletmenin mali yapısı hakkında bilgi vermez?',
        {
            'A': 'Finansal kaldıraç oranı',
            'B': 'Borç/özkaynak oranı',
            'C': 'Stok devir hızı',
            'D': 'Özsermaye çarpanı',
            'E': 'Duran varlıkların özkaynaklara oranı',
        },
        'C',
        'Stok devir hızı bir faaliyet oranıdır. Diğerleri kaynak yapısını ve varlıkların hangi kaynaklarla finanse edildiğini gösteren mali yapı oranlarıdır.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0040': patch(
        "Bir işletme 400.000 ₺ uzun vadeli kredi kullanarak kısa vadeli borçlarını kapatmıştır. İşlemden önce aktif toplamı 1.600.000 ₺, kısa vadeli yabancı kaynaklar 600.000 ₺, uzun vadeli yabancı kaynaklar 200.000 ₺'dir. Bu işlemin etkisiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Özkaynak oranı 0,50'den 0,25'e düşer.",
            'B': "Finansal kaldıraç oranı 0,50'den 0,75'e yükselir.",
            'C': "Finansal kaldıraç oranı 0,50'den 0,25'e düşer.",
            'D': "Finansal kaldıraç oranı 0,50'de kalır; kısa vadeli borçların toplam borçlar içindeki payı %75'ten %25'e iner.",
            'E': "Kısa vadeli borçların payı %75'ten %50'ye iner, kaldıraç yükselir.",
        },
        'D',
        "Toplam borç (800.000) ve aktif (1.600.000) değişmez; kaldıraç 0,50'de kalır. KVYK 200.000, UVYK 600.000 olur: kısa vadeli payı 600/800 = %75'ten 200/800 = **%25**'e iner. Vade yapısı iyileşir, borçluluk düzeyi değişmez.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0041': patch(
        'Borç/özkaynak oranı 1,5 olan bir işletmenin finansal kaldıraç oranı kaçtır?',
        {
            'A': '0,40',
            'B': '1,50',
            'C': '0,67',
            'D': '0,60',
            'E': '2,50',
        },
        'D',
        'Borç 1,5 birim, özkaynak 1 birim → aktif 2,5 birim. Finansal kaldıraç = 1,5 ÷ 2,5 = **0,60**.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0042': patch(
        "Bir işletmenin özkaynak kalemleri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Sermaye | 1.500.000 |\n| Ödenmemiş sermaye | 200.000 |\n| Sermaye düzeltmesi olumlu farkları | 100.000 |\n| Yasal yedekler | 150.000 |\n| Olağanüstü yedekler | 250.000 |\n| Geçmiş yıllar kârları | 120.000 |\n| Dönem net zararı | 170.000 |\n\nBuna göre özkaynaklar toplamı kaç ₺'dir?",
        {
            'A': '2.150.000',
            'B': '1.650.000',
            'C': '1.750.000',
            'D': '1.630.000',
            'E': '2.090.000',
        },
        'C',
        'Özkaynak = 1.500.000 − 200.000 + 100.000 + 150.000 + 250.000 + 120.000 − 170.000 = **1.750.000 ₺**. Ödenmemiş sermaye ve dönem net zararı indirim kalemidir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0043': patch(
        'Uzun vadeli yabancı kaynakları 150.000 ₺, özkaynakları 350.000 ₺ olan bir işletmenin uzun vadeli yabancı kaynakların devamlı sermayeye oranı kaçtır?',
        {
            'A': '0,43',
            'B': '2,33',
            'C': '0,15',
            'D': '0,70',
            'E': '0,30',
        },
        'E',
        'Devamlı sermaye = 150.000 + 350.000 = 500.000 ₺. Oran = 150.000 ÷ 500.000 = **0,30**. Özkaynağa bölmek 0,43 verir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0044': patch(
        "2024'te finansal kaldıraç oranı 0,50 olan bir işletmenin 2025'te aktif toplamı %25, toplam borçları %40 artmıştır. Buna göre 2025 yılı finansal kaldıraç oranı kaçtır?",
        {
            'A': '0,56',
            'B': '0,65',
            'C': '0,50',
            'D': '0,45',
            'E': '0,70',
        },
        'A',
        'Kaldıraç = 0,50 × 1,40 ÷ 1,25 = **0,56**. Borçlar aktiften hızlı büyüdüğü için oran yükselmiştir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0045': patch(
        'Borç/özkaynak oranı 0,25 olan bir işletmenin özsermaye çarpanı (toplam varlıklar ÷ özkaynaklar) kaçtır?',
        {
            'A': '4',
            'B': '5',
            'C': '0,25',
            'D': '0,80',
            'E': '1,25',
        },
        'E',
        "Özkaynak 1 birim, borç 0,25 birim → aktif 1,25 birim. Özsermaye çarpanı = **1,25**; kaldıraç oranı 0,20'dir.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0046': patch(
        "Satışların maliyeti 1.500.000 ₺ olan bir işletmenin stokları dönem başında 200.000 ₺, dönem sonunda 300.000 ₺'dir. Ortalama satıcılar (ticari borçlar) 200.000 ₺ olduğuna göre ortalama borç ödeme süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '8',
            'B': '48',
            'C': '36',
            'D': '42',
            'E': '45',
        },
        'E',
        'Alışlar = satışların maliyeti + stok artışı = 1.500.000 + 100.000 = 1.600.000 ₺. Borç devir hızı = 1.600.000 ÷ 200.000 = 8 → ödeme süresi 360 ÷ 8 = **45 gün**. Satışların maliyetini doğrudan kullanmak 48 gün verir.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0047': patch(
        'Net satışları 2.000.000 ₺, net duran varlıkları 800.000 ₺ olan bir işletmenin duran varlık devir hızı kaçtır?',
        {
            'A': '0,40',
            'B': '2,50',
            'C': '1,50',
            'D': '1,60',
            'E': '3,50',
        },
        'B',
        'Duran varlık devir hızı = 2.000.000 ÷ 800.000 = **2,50**. Her 1 ₺ duran varlık 2,50 ₺ satış yaratmaktadır.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0048': patch(
        "Bir medikal ürün toptancısının yıllık net satışları 2.100.000 ₺ olup bunun 1.500.000 ₺'si kredili satışlardan oluşmaktadır. İşletmenin ortalama alacak tahsil süresi 72 gündür.\n\nBuna göre işletmenin ortalama ticari alacakları kaç ₺'dir? (1 yıl = 360 gün)",
        {
            'A': '5',
            'B': '360.000',
            'C': '250.000',
            'D': '300.000',
            'E': '108.000',
        },
        'D',
        'Alacak devir hızı = 360 ÷ 72 = 5 → ortalama alacak = 1.500.000 ÷ 5 = **300.000 ₺**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0049': patch(
        "2024'te alacak tahsil süresi 60 gün olan bir işletmenin 2025'te kredili satışları %20, ortalama ticari alacakları %50 artmıştır. Buna göre 2025 yılı tahsil süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '90',
            'B': '48',
            'C': '60',
            'D': '72',
            'E': '75',
        },
        'E',
        'Tahsil süresi = 360 × ortalama alacak ÷ satışlar → 60 × 1,50 ÷ 1,20 = **75 gün**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0050': patch(
        "Net satışları 2.000.000 ₺ olan bir işletmenin satışlarının %60'ı kredilidir. Ortalama ticari alacakları 150.000 ₺ olduğuna göre ortalama alacak tahsil süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '8',
            'B': '60',
            'C': '30',
            'D': '45',
            'E': '27',
        },
        'D',
        'Alacak devir hızı kredili satışlarla hesaplanır: 1.200.000 ÷ 150.000 = 8 → **45 gün**. Toplam satışları kullanmak 27 gün verir ve tahsilatı olduğundan hızlı gösterir.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletmenin net kârı 90.000 ₺'dir. Aktif toplamı dönem başında 500.000 ₺, dönem sonunda 700.000 ₺'dir. Ortalama aktif kullanılarak hesaplanan aktif kârlılığı yüzde kaçtır?",
        {
            'A': '%18',
            'B': '%15',
            'C': '%12,86',
            'D': '%7,50',
            'E': '%16',
        },
        'B',
        'Ortalama aktif = (500.000 + 700.000) ÷ 2 = 600.000 ₺. Aktif kârlılığı = 90.000 ÷ 600.000 = **%15**. Dönem sonu aktifiyle %12,86 bulunur.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0052': patch(
        'Aktif kârlılığı %12 ve finansal kaldıraç oranı 0,40 olan bir işletmenin özkaynak kârlılığı yüzde kaçtır?',
        {
            'A': '%20',
            'B': '%4,80',
            'C': '%16,80',
            'D': '%30',
            'E': '%7,20',
        },
        'A',
        'Özkaynak oranı 0,60 → özsermaye çarpanı 1 ÷ 0,60. Özkaynak kârlılığı = %12 ÷ 0,60 = **%20**. Kaldıraçla çarpmak (%4,80) ya da kaldıraca bölmek (%30) yanlıştır.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0053': patch(
        'Özkaynak kârlılığı %18 ve toplam varlıklarının özkaynaklarına oranı 1,5 olan bir işletmenin aktif kârlılığı yüzde kaçtır?',
        {
            'A': '%19,50',
            'B': '%12',
            'C': '%16,50',
            'D': '%27',
            'E': '%6',
        },
        'B',
        'Aktif kârlılığı = özkaynak kârlılığı ÷ özsermaye çarpanı = %18 ÷ 1,5 = **%12**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0054': patch(
        'Kârlılık oranlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Özkaynak kârlılığı, aktif kârlılığı ile özsermaye çarpanının çarpımına eşittir.\n\nII. Aktif devir hızı arttıkça net kâr marjı da artar.\n\nIII. Faiz karşılama oranı, faiz ve vergi öncesi kârın faiz giderine oranıdır.',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'A',
        '**I doğrudur** (DuPont). **II yanlıştır:** aktif devir hızı ile kâr marjı bağımsız iki bileşendir. **III doğrudur.** Doğru cevap **I ve III**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletmenin net satışları 500.000 ₺, net kârı 40.000 ₺, aktif toplamı 400.000 ₺ ve özkaynakları 160.000 ₺'dir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Özsermaye çarpanı 2,50'dir.",
            'B': "Net kâr marjı %8'dir.",
            'C': "Aktif devir hızı 1,25'tir.",
            'D': "Özkaynak kârlılığı %10'dur.",
            'E': "Aktif kârlılığı %10'dur.",
        },
        'D',
        "Özkaynak kârlılığı = 40.000 ÷ 160.000 = %25'tir (= %10 × 2,50); %10 aktif kârlılığıdır. Diğerleri doğrudur.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0056': patch(
        'Net kârı 3.000.000 ₺ olan bir işletmenin dolaşımdaki pay sayısı 2.000.000 adettir. Pay fiyatı 12 ₺ olduğuna göre fiyat/kazanç (F/K) oranı kaçtır?',
        {
            'A': '0,13',
            'B': '1,50',
            'C': '6',
            'D': '4',
            'E': '8',
        },
        'E',
        'Pay başına kâr = 3.000.000 ÷ 2.000.000 = 1,50 ₺. F/K = 12 ÷ 1,50 = **8**; bugünkü kazançla fiyatın 8 yılda geri kazanılacağını gösterir.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0057': patch(
        'Pay başına kârı 1,50 ₺ olan bir işletme pay başına 0,60 ₺ nakit kâr payı dağıtmıştır. Buna göre kâr dağıtım oranı yüzde kaçtır?',
        {
            'A': '%40',
            'B': '%250',
            'C': '%60',
            'D': '%150',
            'E': '%90',
        },
        'A',
        "Kâr dağıtım oranı = 0,60 ÷ 1,50 = **%40**; kârın %60'ı işletmede bırakılmıştır.",
        'Mali analiz - piyasa oranları',
    ),
    # düzey 3
    '0058': patch(
        "Özkaynakları 6.000.000 ₺ ve dolaşımdaki pay sayısı 1.500.000 adet olan bir işletmenin pay fiyatı 10 ₺'dir. Buna göre pay başına defter değeri ve PD/DD oranı sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
        {
            'A': '6,67 ₺ ve 1,50',
            'B': '4 ₺ ve 0,40',
            'C': '10 ₺ ve 1',
            'D': '2,50 ₺ ve 4',
            'E': '4 ₺ ve 2,50',
        },
        'E',
        'Pay başına defter değeri = 6.000.000 ÷ 1.500.000 = **4 ₺**; PD/DD = 10 ÷ 4 = **2,50**.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0059': patch(
        "Mali yapı oranlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Özsermaye çarpanı 1'den küçük olabilir.\n\nII. Borç/özkaynak oranı 1 ise finansal kaldıraç oranı 1'dir.\n\nIII. Özkaynak oranı ile finansal kaldıraç oranının toplamı 1'dir.",
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'D',
        "**I yanlıştır:** aktif özkaynaktan küçük olamaz (özkaynak pozitifken çarpan ≥ 1). **II yanlıştır:** borç = özkaynak ise kaldıraç 0,50'dir. **III doğrudur:** varlıklar yabancı kaynak ve özkaynakla finanse edilir. Doğru cevap **Yalnız III**.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0060': patch(
        'Bir analist, borsada işlem gören bir perakende şirketinin finansal tablolarını inceleyerek aktif kârlılığını %8, özkaynak kârlılığını %20 olarak hesaplamıştır. Şirketin dönem içinde sermaye hareketi olmamıştır.\n\nBu şirket için aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Özsermaye çarpanı 1,60'tır.",
            'B': "Net kâr marjı %12'dir.",
            'C': "Borç/özkaynak oranı 0,40'tır.",
            'D': "Varlıklarının %40'ı yabancı kaynakla finanse edilmiştir.",
            'E': "Varlıklarının %60'ı yabancı kaynakla finanse edilmiştir.",
        },
        'E',
        "Özsermaye çarpanı = %20 ÷ %8 = 2,50 → özkaynak oranı 0,40, finansal kaldıraç **0,60**. Borç/özkaynak 1,50'dir; net kâr marjı aktif devir hızı bilinmeden bulunamaz.",
        'Mali analiz - kârlılık oranları',
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
    print(f"1 paket / {len(PATCHES)} soru ('Mali Yapi, Faaliyet ve Karlilik Oranlari' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
