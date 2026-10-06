#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Karsilastirmali Analiz — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Mali tablolar analizi tablolu tur. Gercek sinavin ~20 karsilastirmali analiz sorusu iki donemli tablolar, degisim yuzdesinden tutara geri donus, sifir/negatif baz, marjlarin artis hizindan yorum ve oran kisitli iki donemli bilanco istiyor; eski paketin cogu 'once X, cari Y, yuzde kac' idi. 15 kavram sorusu korundu (mutlak ifadeli celdiriciler yenilendi); 45 yeni soru her biri kendi verisiyle: iki donemli gelir tablosu ve bilanco, oranlarin (cari, NCS, devir, ozkaynak karliligi, marj) yatay degisimi, birlesik degisim, ters hesap, satis indirimi/finansman/vergi etkisi. Tek seferlik build_mta_yatay_drill.py (eski masaustu yolu, --check yok) silindi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Mali tablolar analizi - karsilastirmali (yatay) analiz
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/mali_tablolar_analizi/karsilastirmali_analiz.json"
STYLE_REF = 'SGS Mali Tablolar Analizi (oran zinciri, ters hesap; gerçek sınav profiline kalibre)'
ONEK = "mta-yatay-gen-"


def patch(stem, options, answer, solution, ref='Mali analiz - karşılaştırmalı (yatay) analiz'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Karşılaştırmalı (yatay) tablolar analizi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bilançoda her kalemi toplam aktife, gelir tablosunda ise net satışlara oranlayarak tek dönemin yüzde bileşimini gösteren dikey bir tekniktir.',
            'B': 'Bir dönemdeki her kalemi diğer bir kaleme bölerek oranlar üretir; tutar ve yüzde değişimini değil, kalemler arası ilişkiyi ölçmeyi amaçlar.',
            'C': 'Tek bir döneme ait mali tabloyu ele alır ve o dönemdeki kalemleri statik biçimde inceleyip dönemler arası değişimi dışarıda bırakır.',
            'D': 'Birbirini izleyen iki veya daha fazla döneme ait mali tablo kalemlerinin tutar ve yüzde olarak değişiminin (artış/azalış) incelenmesidir.',
            'E': 'Sadece dönemin vergi matrahını ve ödenecek vergiyi hesaplamayı amaçlayan, mali tablo kalemlerinin gelişimiyle ilgilenmeyen bir yöntemdir.',
        },
        'D',
        '**Karşılaştırmalı (yatay) analiz**; ardışık iki veya daha fazla döneme ait kalemlerin **tutar ve yüzde olarak değişiminin** karşılaştırılmasıdır. Dinamik bir analizdir.',
        'Mali analiz - karşılaştırmalı analiz',
    ),
    # düzey 2
    '0002': patch(
        'Karşılaştırmalı analizde yüzde değişim hesaplanırken bölme işleminde payda (temel) olarak hangi dönem alınır?',
        {
            'A': 'Bütçelenen gelecek dönem tahmini esas alınır',
            'B': 'Tutarı en yüksek olan dönem payda seçilir',
            'C': 'İki dönem tutarının aritmetik ortalaması alınır',
            'D': 'Cari (son) dönem, çünkü değişim güncel duruma göre ölçülür',
            'E': 'Önceki (baz/karşılaştırmaya esas) dönem',
        },
        'E',
        'Yüzde değişimde payda **önceki (baz) dönemdir**; değişim, karşılaştırmaya esas alınan önceki döneme göre ölçülür.',
        'Mali analiz - baz dönem',
    ),
    # düzey 2
    '0003': patch(
        "Karşılaştırmalı (yatay) analiz ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tek bir dönemin verisiyle yapılır.\n\nII. Değişim tutarı = Cari Dönem − Önceki Dönem'dir.\n\nIII. Yüzde değişimde payda önceki (baz) dönemdir.",
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'C',
        '**I yanlıştır:** Karşılaştırmalı (yatay) analiz **en az iki döneme** ait tabloyla yapılır; tek dönemin verisiyle yapılan, dikey (statik) analizdir. **II** (değişim tutarı = cari − önceki) ve **III** (yüzde değişimde payda önceki/baz dönem) doğrudur. Doğru cevap **II ve III**.',
        'Mali analiz - karşılaştırmalı analiz',
    ),
    # düzey 2
    '0004': patch(
        'Bir ev tekstili üreticisinin iki yıllık mali tablolarından alınan bazı kalemler aşağıdaki gibidir (₺):\n\n| Kalem | 2024 | 2025 |\n|---|---|---|\n| Stoklar | 400.000 | 540.000 |\n| Net satışlar | 2.000.000 | 2.040.000 |\n| Ticari alacaklar | 300.000 | 306.000 |\n\nStokların %35, net satışların %2 arttığını gösteren bu karşılaştırmalı bulgu en olası olarak neyi gösterir?',
        {
            'A': 'Satışlar artmadan stokların birikmesini; olası stok fazlalığı/satış yavaşlaması riskini',
            'B': 'İşletmenin stoksuz (stok bulundurmadan) çalışmaya geçtiğini ve tüm mamulü anında sattığını',
            'C': 'Stokların çok hızlı satıldığını ve stok devir hızının yükselerek satışları desteklediğini',
            'D': 'Satışlar sabit kalsa da stok artışının dönem kârını kesin biçimde yükselttiğini gösterdiğini',
            'E': 'Stok artışının kısa vadeli borçların ödenip azalmasından kaynaklandığını gösterdiğini',
        },
        'A',
        'Satışlar sabitken (%2) stokların %35 artması, **stok birikmesine** (olası stok fazlalığı/satış yavaşlaması) işaret eder; bu genelde olumsuz bir sinyaldir.',
        'Mali analiz - karşılaştırmalı yorum',
    ),
    # düzey 2
    '0005': patch(
        'Karşılaştırmalı analiz ile dikey analiz arasındaki temel fark ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Karşılaştırmalı analiz tek dönemi ele aldığından statik, dikey analiz ise dönemler arası değişimi izlediğinden dinamik bir analiz türü olarak nitelenir.',
            'B': 'İki teknik özünde aynı işlemi yapar; karşılaştırmalı analiz ile dikey analiz arasında yöntem, amaç veya sonuç bakımından herhangi bir fark bulunmaz.',
            'C': 'İkisi de tek bir döneme ait mali tabloyu inceler; aralarındaki fark kullanılan tablonun bilanço veya gelir tablosu olmasından ibarettir.',
            'D': 'Karşılaştırmalı analiz dönemler arası değişimi (dinamik) incelerken; dikey analiz tek bir dönemde kalemlerin bir bütüne oranını (statik) inceler.',
            'E': 'İkisi de kalemleri birbirine bölerek oran üretir; fark, karşılaştırmalının bilançoda, dikey analizin ise gelir tablosunda uygulanmasından ibarettir.',
        },
        'D',
        '**Karşılaştırmalı (yatay) analiz** dönemler arası değişimi inceler (**dinamik**); **dikey analiz** ise tek dönemde her kalemin bir bütüne (toplam aktif/net satışlar) oranını inceler (**statik**).',
        'Mali analiz - yatay/dikey',
    ),
    # düzey 2
    '0006': patch(
        'Yatay analizde satışların maliyetinin değişim oranı 2024 yılı için %70, 2025 yılı için %60 olarak hesaplanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satışların maliyeti 2025 yılında önceki yılla aynı kalmıştır.',
            'B': 'Satışların maliyeti iki yılda toplam %130 artmıştır.',
            'C': 'Satışların maliyeti 2025 yılında önceki yıla göre azalmıştır.',
            'D': "Satışların maliyetinin net satışlar içindeki payı 2025'te azalmıştır.",
            'E': 'Satışların maliyeti 2025 yılında da önceki yıla göre artmıştır.',
        },
        'E',
        "Değişim oranı pozitif olduğu sürece kalem artmaktadır; yalnızca artış hızı %70'ten %60'a düşmüştür. Satışlara oranı hakkında bilgi yoktur. Birleşik artış 1,70 × 1,60 − 1 = %172'dir; oranlar toplanmaz.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletmenin 2024–2025 yatay analiz sonuçlarına göre dönem kâr marjı, olağan kâr marjına göre daha düşük oranda artmıştır. Aşağıdakilerden hangisindeki artış bu sonucun bir nedeni olabilir?',
        {
            'A': 'Net satışlar',
            'B': 'Olağandışı gider ve zararlar',
            'C': 'Olağandışı gelir ve kârlar',
            'D': 'Brüt satış kârı',
            'E': 'Diğer faaliyetlerden olağan gelir ve kârlar',
        },
        'B',
        'Dönem kârı = olağan kâr + olağandışı gelir − olağandışı gider (vergiden önce). Olağan kârdan sonra gelen olağandışı gider ve zararların artması dönem kârının olağan kârdan daha yavaş artmasına yol açar. Diğer seçenekler olağan kârın üstündeki kalemlerdir ya da dönem kârını hızlandırır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0008': patch(
        "Önceki yılda aktiflerinin %70'i dönen varlıklardan oluşan bir işletmede cari yılda aktif toplamı değişmemiş, dönen varlıkların aktif içindeki ağırlığı %55'e düşmüştür. Buna göre duran varlıkların yatay analiz yüzdesi kaçtır?",
        {
            'A': '%45',
            'B': '%15',
            'C': '%50',
            'D': '%21,43',
            'E': '−%21,43',
        },
        'C',
        "Aktif 100 birim kabul edilirse duran varlıklar 30'dan 45'e çıkmıştır: (45 − 30) ÷ 30 = **%50**. Dönen varlıklar 70'ten 55'e düşmüştür (−%21,43). Paydaki puan farkı (%15) değişim oranı değildir.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0009': patch(
        'Bir ev aletleri üreticisinin gelir tablolarına uygulanan analiz sonuçlarına göre, önceki yıla göre cari yılda faaliyet kâr marjı brüt kâr marjına göre daha yüksek oranda artmıştır. Aynı dönemde işletmenin net satışları %18 artmıştır.\n\nBu işletme için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Faaliyet giderleri tutar olarak azalmıştır.',
            'B': 'Faaliyet giderlerinin net satışlara oranı azalmıştır.',
            'C': 'Net satışlar azalmıştır.',
            'D': 'Satışların maliyetinin net satışlara oranı artmıştır.',
            'E': 'Finansman giderlerinin net satışlara oranı azalmıştır.',
        },
        'B',
        'Faaliyet kâr marjı = brüt kâr marjı − faaliyet giderlerinin satışlara oranı. Faaliyet marjı brüt marjdan daha hızlı arttıysa aradaki fark, yani faaliyet giderlerinin satışlara oranı küçülmüştür. Tutarın ya da finansman giderlerinin yönü bu bilgiden çıkmaz.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0010': patch(
        "Bir işletmenin gelir tablosu kalemleri şöyledir:\n\n| Kalem | 2024 (₺) | 2025 (₺) |\n|---|---|---|\n| Net satışlar | 400.000 | 480.000 |\n| Satışların maliyeti | 240.000 | 300.000 |\n| Faaliyet giderleri | 80.000 | 86.000 |\n\nYatay analize göre 2025'te en yüksek oransal artış hangi kalemde gerçekleşmiştir?",
        {
            'A': 'Brüt satış kârı',
            'B': 'Faaliyet kârı',
            'C': 'Satışların maliyeti',
            'D': 'Faaliyet giderleri',
            'E': 'Net satışlar',
        },
        'C',
        'Net satışlar %20, satışların maliyeti **%25**, faaliyet giderleri %7,50, brüt satış kârı (160.000 → 180.000) %12,50, faaliyet kârı (80.000 → 94.000) %17,50 artmıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0011': patch(
        "Bir işletmenin 2024 yılı net satışları 800.000 ₺, brüt satış kârı 240.000 ₺'dir. 2025'te net satışlar %25, brüt satış kârı %10 artmıştır. Buna göre 2025 yılı satışların maliyeti kaç ₺'dir?",
        {
            'A': '264.000',
            'B': '828.000',
            'C': '760.000',
            'D': '772.000',
            'E': '736.000',
        },
        'E',
        "2025 net satışlar = 1.000.000 ₺, brüt kâr = 264.000 ₺. Satışların maliyeti = 1.000.000 − 264.000 = **736.000 ₺** (%31,43 artış). Brüt kâr marjı %30'dan %26,40'a inmiştir.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletmenin 2024 yılında dönen varlıkları 300.000 ₺, kısa vadeli yabancı kaynakları 200.000 ₺'dir. 2025'te dönen varlıklar %10, kısa vadeli yabancı kaynaklar %30 artmıştır. Buna göre net çalışma sermayesinin yatay analiz yüzdesi kaçtır?",
        {
            'A': '%20',
            'B': '%30',
            'C': '−%20',
            'D': '−%30',
            'E': '−%10',
        },
        'D',
        "2024 NÇS = 100.000 ₺. 2025: dönen varlıklar 330.000, KVYK 260.000 → NÇS 70.000 ₺. Değişim = −30.000 ÷ 100.000 = **−%30**. Oranların farkı (−%20) NÇS'nin değişimi değildir.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletmenin 2024 sonu özkaynakları 400.000 ₺'dir. 2025'te dönem net kârı 80.000 ₺ olmuş, ortaklara 30.000 ₺ kâr payı dağıtılmış ve 50.000 ₺ nakdi sermaye artırımı yapılmıştır. Başka özkaynak hareketi olmadığına göre özkaynakların yatay analiz yüzdesi kaçtır?",
        {
            'A': '%25',
            'B': '%20',
            'C': '%12,50',
            'D': '%7,50',
            'E': '%32,50',
        },
        'A',
        '2025 sonu özkaynak = 400.000 + 80.000 − 30.000 + 50.000 = 500.000 ₺ → **%25**. Kâr payını düşmemek %32,50, sermaye artırımını unutmak %12,50 verir.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0014': patch(
        "Bir hırdavat toptancısında 2024 yılında stok devir hızı 6'dır. 2025 yılında yeni bir depo açılması nedeniyle ortalama stoklar %40 artmış, satışların maliyeti ise yalnız %5 artmıştır. Yönetim, stok yönetiminin etkinliğini değerlendirmektedir.\n\nBuna göre 2025 yılı stok devir hızı kaçtır?",
        {
            'A': '2,10',
            'B': '4,29',
            'C': '7,50',
            'D': '6,30',
            'E': '4,50',
        },
        'E',
        'Stok devir hızı = satışların maliyeti ÷ ortalama stok → 6 × 1,05 ÷ 1,40 = **4,50**. Stoklar satışların maliyetinden çok daha hızlı arttığından devir hızı düşmüştür.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0015': patch(
        'Bir işletmenin gelir tablosu kalemleri şöyledir:\n\n| Kalem | 2024 (₺) | 2025 (₺) |\n|---|---|---|\n| Net satışlar | 900.000 | 1.080.000 |\n| Satışların maliyeti | 540.000 | 702.000 |\n| Faaliyet giderleri | 200.000 | 210.000 | Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Faaliyet kârı 2025'te azalmıştır.",
            'B': 'Satışların maliyeti %30 artmıştır.',
            'C': 'Faaliyet giderleri %5 artmıştır.',
            'D': 'Net satışlar %20 artmıştır.',
            'E': 'Brüt satış kârı %5 artmıştır.',
        },
        'A',
        'Brüt kâr 360.000 → 378.000 (%5); faaliyet kârı 160.000 → 168.000 ₺, yani %5 **artmıştır**; ifade yanlıştır. Net satışlar %20, satışların maliyeti %30, faaliyet giderleri %5 artmıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0016': patch(
        "Bir işletmenin 2024 yılı aktif toplamı 800.000 ₺, özkaynakları 320.000 ₺'dir. 2025'te aktif toplamı %25, özkaynaklar %10 artmıştır. Buna göre yabancı kaynakların yatay analiz yüzdesi kaçtır?",
        {
            'A': '%15',
            'B': '%35',
            'C': '%25',
            'D': '%30',
            'E': '%40',
        },
        'B',
        '2024 yabancı kaynak = 480.000 ₺. 2025: aktif 1.000.000, özkaynak 352.000 → yabancı kaynak 648.000 ₺. Değişim = 168.000 ÷ 480.000 = **%35**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0017': patch(
        'Önceki yıl bilançosunda hiç bulunmayan kısa vadeli banka kredisi cari yılda 150.000 ₺ olarak raporlanmıştır. Bu kalemin karşılaştırmalı analiziyle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Değişim oranı %150'dir.",
            'B': "Değişim oranı %100'dür.",
            'C': "Değişim tutarı 150.000 ₺'dir; yüzde değişim hesaplanamaz.",
            'D': 'Değişim tutarı da oranı da hesaplanamaz.',
            'E': 'Değişim oranı sonsuz olduğundan %100 kabul edilir.',
        },
        'C',
        "Tutar değişimi 150.000 − 0 = 150.000 ₺'dir. Baz sıfır olduğundan yüzde değişim tanımsızdır; tabloda boş bırakılır ya da 'hesaplanamaz' diye gösterilir.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0018': patch(
        "Bir işletmenin vergi öncesi kârı 2025'te %20 artmıştır. Kurumlar vergisi oranı ise %20'den %25'e yükselmiştir. Buna göre dönem net kârının yatay analiz yüzdesi kaçtır?",
        {
            'A': '%25',
            'B': '%15',
            'C': '%20',
            'D': '%12,50',
            'E': '%5',
        },
        'D',
        'Net kâr = vergi öncesi kâr × (1 − vergi oranı). Değişim = 1,20 × 0,75 ÷ 0,80 − 1 = **%12,50**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0019': patch(
        "Bir inşaat şirketinin borç/özkaynak oranı 2024'te 0,80'dir. 2025 yılında şirket bedelli sermaye artırımı yapmış ve dönemi kârla kapatmıştır; bu yıl yabancı kaynaklar %20, özkaynaklar %50 artmıştır.\n\nBuna göre 2025 yılı borç/özkaynak oranı kaçtır?",
        {
            'A': '0,64',
            'B': '1',
            'C': '0,50',
            'D': '0,96',
            'E': '0,53',
        },
        'A',
        'Oran = 0,80 × 1,20 ÷ 1,50 = **0,64**. Özkaynaklar yabancı kaynaklardan hızlı arttığı için oran düşmüştür.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0020': patch(
        "Bir kalem 2023'te 250.000 ₺'dir. 2024'te %40 artmış, 2025'te 2024'e göre %20 azalmıştır. Buna göre kalemin 2023'e göre 2025'teki değişim oranı yüzde kaçtır?",
        {
            'A': '%8',
            'B': '−%12',
            'C': '%12',
            'D': '%60',
            'E': '%20',
        },
        'C',
        '2024 = 250.000 × 1,40 = 350.000 ₺; 2025 = 350.000 × 0,80 = 280.000 ₺ → 30.000 ÷ 250.000 = **%12**. Oranları toplamak (%20) yanlıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0021': patch(
        'Karşılaştırmalı analiz, dönemler arası değişimi incelediği için hangi tür analiz sınıfına girer?',
        {
            'A': 'Oran analizi',
            'B': 'Nokta analizi',
            'C': 'Statik analiz',
            'D': 'Dikey analiz',
            'E': 'Dinamik analiz',
        },
        'E',
        'Karşılaştırmalı analiz birden fazla dönemi kapsayıp **dönemler arası değişimi** incelediğinden **dinamik analizdir**. (Tek dönemi inceleyen dikey analiz ise statiktir.)',
        'Mali analiz - statik/dinamik',
    ),
    # düzey 2
    '0022': patch(
        'Karşılaştırmalı analizin uygulanabilmesi için en az kaç döneme ait mali tablo gerekir?',
        {
            'A': 'En az beş dönem',
            'B': 'En az iki dönem',
            'C': 'Bir dönem yeterlidir',
            'D': 'En az on dönem',
            'E': 'Dönem sayısı önemli değildir',
        },
        'B',
        'Karşılaştırmalı analiz dönemler arası değişimi ölçtüğünden **en az iki döneme** ait mali tablo gerekir.',
        'Mali analiz - karşılaştırmalı analiz',
    ),
    # düzey 2
    '0023': patch(
        "Bir tıbbi cihaz distribütörünün ticari alacakları bir yılda 500.000 ₺'den 700.000 ₺'ye (%40), net satışları ise 4.000.000 ₺'den 4.400.000 ₺'ye (%10) yükselmiştir. İşletme bu dönemde satış politikasında yaptığı değişiklikleri henüz açıklamamıştır.\n\nBu karşılaştırmalı bulgu en olası olarak neyi düşündürür?",
        {
            'A': 'İşletmenin tüm satışlarını peşine çevirdiğini, bu nedenle ticari alacak bakiyesinin artık büyümediğini',
            'B': 'Alacaklar satışlardan hızlı büyüdüğü için tahsilat performansının belirgin biçimde iyileştiğini ve alacakların hızla nakde döndüğünü',
            'C': 'Alacakların satışlardan çok daha hızlı büyüdüğünü; tahsilatta yavaşlama veya vadeli satış artışı olabileceğini',
            'D': 'Ticari alacaklardaki artışın stokların eriyip azalmasından kaynaklandığını ve stok devir hızının yükseldiğini',
            'E': 'Alacak artışının doğrudan özkaynakların azalması anlamına geldiğini ve sermayenin eridiğini',
        },
        'C',
        'Alacaklar (%40), satışlardan (%10) **çok daha hızlı** büyümüşse; bu, tahsilatta yavaşlama ya da vadeli satışların artışına işaret edebilir (olumsuz sinyal olarak değerlendirilir).',
        'Mali analiz - karşılaştırmalı yorum',
    ),
    # düzey 2
    '0024': patch(
        'Bir gıda şirketinin iki yıllık bilançolarına uygulanan yatay analizde özkaynakların %20 arttığı, toplam yabancı kaynakların ise %10 azaldığı görülmüştür. Şirket bu dönemde kârının tamamını işletmede bırakmış ve vadesi gelen banka kredilerini geri ödemiştir.\n\nBu karşılaştırmalı bulgu mali yapı açısından neyi gösterir?',
        {
            'A': 'Borçların hızla büyüyüp işletmenin ödeme güçlüğüne (borç batağına) girdiğini işaret ettiğini',
            'B': 'Özkaynaktaki artışın doğrudan net satışların düşmesinden kaynaklandığını ortaya koyduğunu',
            'C': 'Özkaynak artışının nakit çıkışına yol açarak işletmenin likiditesini bozduğunu gösterdiğini',
            'D': 'Özkaynak ağırlığının arttığını, borçluluğun azaldığını; mali yapının güçlendiğini',
            'E': 'Yabancı kaynak ağırlığının artıp özkaynağın gerilemesiyle mali yapının zayıfladığını gösterdiğini',
        },
        'D',
        'Özkaynak artıp (%20) yabancı kaynak azalınca (%10), varlıklar içinde **özkaynak ağırlığı artar, borçluluk azalır** → mali yapı **güçlenir**.',
        'Mali analiz - karşılaştırmalı yorum',
    ),
    # düzey 2
    '0025': patch(
        'Bir yazılım şirketinin yatay analiz raporuna göre net satışları önceki yıla göre %25, dönem net kârı ise %60 artmıştır. Şirketin bu dönemde borçlanma düzeyinde önemli bir değişiklik olmamış ve olağandışı bir gelir elde edilmemiştir.\n\nBu karşılaştırmalı bulgu en olası olarak neyi gösterir?',
        {
            'A': 'Kâr artışının kaynağının borçlanmadaki yükseliş olduğunu ve mali yapının borç ağırlıklı hâle geldiğini',
            'B': 'Net kârın net satışlardan daha yavaş büyümesi nedeniyle net kâr marjının gerilediğini ve kârlılığın kötüleştiğini',
            'C': 'Giderlerin gelirleri aşması nedeniyle işletmenin cari dönemi net zararla kapattığını gösterdiğini',
            'D': 'Net satışların önceki döneme göre azaldığını ve bu daralmanın kârı düşürdüğünü ortaya koyduğunu',
            'E': 'Net kârın satışlardan daha hızlı büyümesi nedeniyle kârlılığın (net kâr marjının) iyileşme eğiliminde olduğunu',
        },
        'E',
        'Net kâr (%60), net satışlardan (%25) **daha hızlı** büyümüşse, net kâr marjı (net kâr/net satış) yükselme eğilimindedir → **kârlılık iyileşir**.',
        'Mali analiz - karşılaştırmalı yorum',
    ),
    # düzey 3
    '0026': patch(
        "Yatay analizde bir işletmenin gelir tablosuna ilişkin bazı sonuçlar şöyledir:\n\n| Kalem | 2025 değişim oranı |\n|---|---|\n| Satışların maliyeti | %40 |\n| Brüt satış kârı | %20 |\n\n2024 yılında satışların maliyeti 60.000 ₺, brüt satış kârı 25.000 ₺'dir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Net satışlar 2025'te %30 artmıştır.",
            'B': "2025 yılı brüt satış kârı 30.000 ₺'dir.",
            'C': "Brüt kâr marjı 2025'te düşmüştür.",
            'D': "2025 yılı net satışları 114.000 ₺'dir.",
            'E': "2025 yılı satışların maliyeti 84.000 ₺'dir.",
        },
        'A',
        "2025: satışların maliyeti 84.000 ₺, brüt kâr 30.000 ₺, net satışlar 114.000 ₺. 2024 net satışları 85.000 ₺ olduğundan artış 29.000 ÷ 85.000 ≈ %34,1'dir; %30 yanlıştır. Brüt kâr marjı %29,4'ten %26,3'e düşmüştür.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0027': patch(
        'Bir işletmenin bazı gelir tablosu kalemleri şöyledir:\n\n| Kalem | Önceki (₺) | Cari (₺) |\n|---|---|---|\n| Net satışlar | 1.200.000 | 1.500.000 |\n| Satışların maliyeti | 750.000 | 900.000 |\n| Faaliyet giderleri | 300.000 | 330.000 |\n| Faaliyet kârı | 150.000 | 270.000 |\n| Finansman giderleri | 40.000 | 60.000 |\n| Net kâr | 80.000 | 150.000 |\n\nBuna göre yatay analizde en yüksek oransal artış hangi kalemdedir?',
        {
            'A': 'Net kâr',
            'B': 'Faaliyet kârı',
            'C': 'Satışların maliyeti',
            'D': 'Finansman giderleri',
            'E': 'Net satışlar',
        },
        'A',
        'Değişim oranları: net satışlar %25, satışların maliyeti %20, faaliyet giderleri %10, faaliyet kârı %80, finansman giderleri %50, net kâr 70.000 ÷ 80.000 = **%87,50**. Tutarca en büyük artış net satışlarda olsa da oransal olarak en yüksek artış net kârdadır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0028': patch(
        'Bir işletmenin iki yıla ait bilanço verilerinin bir kısmı şöyledir:\n\n| Kalem (₺) | 2024 | 2025 |\n|---|---|---|\n| Dönen varlıklar | 300.000 | ? |\n| Duran varlıklar | 200.000 | 270.000 |\n| KVYK | 280.000 | 364.000 |\n| UVYK | 170.000 | 234.000 |\n\nKarşılaştırmalı analizde özkaynakların %60 arttığı görülmüştür. Buna göre dönen varlıkların yatay analiz yüzdesi kaçtır?',
        {
            'A': '%26,67',
            'B': '%36',
            'C': '%35',
            'D': '%60',
            'E': '%30',
        },
        'B',
        '2024 özkaynak = 500.000 − 450.000 = 50.000 ₺ → 2025: 80.000 ₺. 2025 pasif = 364.000 + 234.000 + 80.000 = 678.000 ₺ → dönen varlıklar = 678.000 − 270.000 = 408.000 ₺. Değişim = 108.000 ÷ 300.000 = **%36**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0029': patch(
        'Bilançoda önceki dönem sonunda 360.000 ₺ olan satıcılar kalemi izleyen dönem sonlarında sırasıyla 300.000 ₺, 0 ₺ ve 150.000 ₺ olmuştur. Son iki yıldaki değişim oranları için aşağıdakilerden hangisi doğrudur?',
        {
            'A': "İlk yıl −%100, ikinci yıl %100'dür.",
            'B': 'Her iki yılın değişim oranı da hesaplanamaz.',
            'C': "İlk yıl −%100'dür; ikinci yılın değişim oranı hesaplanamaz.",
            'D': "İlk yıl −%100, ikinci yıl %150'dir.",
            'E': "İlk yıl −%16,67, ikinci yıl %50'dir.",
        },
        'C',
        "300.000'den 0'a iniş −%100'dür. 0'dan 150.000'e çıkışta baz sıfır olduğundan yüzde değişim hesaplanamaz; yalnız 150.000 ₺'lik tutar değişimi raporlanır.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0030': patch(
        'Yatay analizde net satışları ile faaliyet giderlerinin arttığı, ancak faaliyet giderlerinin net satışlardan daha yavaş arttığı görülmüştür. Aşağıdakilerden hangisi bu durumla ilişkili bir sonuçtur?',
        {
            'A': 'Brüt satış kâr marjı artmıştır.',
            'B': 'Faaliyet giderlerinin net satışlar içindeki payı azalmıştır.',
            'C': 'Net kâr, net satışlardan daha hızlı artmıştır.',
            'D': 'Faaliyet giderleri tutar olarak azalmıştır.',
            'E': 'Satışların maliyetinin net satışlar içindeki payı azalmıştır.',
        },
        'B',
        'Pay (faaliyet giderleri) paydadan (net satışlar) yavaş artınca oran küçülür. Brüt marj ve satışların maliyeti hakkında bilgi yoktur; net kâr diğer kalemlere de bağlıdır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0031': patch(
        'Önceki yıl 50.000 ₺ zarar eden bir işletme cari yılda 30.000 ₺ kâr etmiştir. Dönem sonucunun yatay analiziyle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Değişim oranı %160'tır.",
            'B': 'Kâr ile zarar karşılaştırılamayacağından tutar değişimi de hesaplanamaz.',
            'C': "Değişim oranı −%160'tır ve sonuç kötüleşmiştir.",
            'D': 'Baz yıl tutarı negatif olduğundan yüzde değişim anlamlı yorumlanamaz; tutar değişimi 80.000 ₺ olarak raporlanır.',
            'E': "Değişim oranı %60'tır.",
        },
        'D',
        "Formül (30.000 − (−50.000)) ÷ (−50.000) = −%160 verir; oysa sonuç iyileşmiştir. Negatif bazla bulunan oran yanıltıcıdır; bu durumda yalnız 80.000 ₺'lik tutar değişimi yorumlanır.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0032': patch(
        "2024 yılında cari oranı 1,50 olan bir işletmenin 2025'te dönen varlıkları %20, kısa vadeli yabancı kaynakları %50 artmıştır. Buna göre 2025 yılı cari oranı kaçtır?",
        {
            'A': '1,80',
            'B': '0,80',
            'C': '2,25',
            'D': '1,50',
            'E': '1,20',
        },
        'E',
        'Cari oran = dönen varlıklar ÷ KVYK → 1,50 × 1,20 ÷ 1,50 = **1,20**. Pay %20, payda %50 arttığından oran düşmüştür.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0033': patch(
        "Bir perakende zincirinin aktif devir hızı 2024'te 2'dir. 2025'te şirket mevcut mağazalarında satışlarını artırmış ve yalnız sınırlı sayıda yeni yatırım yapmıştır: net satışlar %32, toplam aktifler %10 artmıştır.\n\nBuna göre 2025 yılı aktif devir hızı kaçtır?",
        {
            'A': '2,40',
            'B': '2,44',
            'C': '2,20',
            'D': '2,64',
            'E': '1,67',
        },
        'A',
        'Aktif devir hızı = net satışlar ÷ aktif → 2 × 1,32 ÷ 1,10 = **2,40**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0034': patch(
        "Cari dönemde 91.000 ₺ olan bir kalem önceki döneme göre %35 azalmıştır. Kalemin önceki dönem tutarı kaç ₺'dir?",
        {
            'A': '31.850',
            'B': '140.000',
            'C': '126.000',
            'D': '59.150',
            'E': '122.850',
        },
        'B',
        'Önceki tutar × 0,65 = 91.000 → önceki tutar = **140.000 ₺**. Cari tutara %35 eklemek 122.850 ₺ verir ve yanlıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0035': patch(
        "2024'te alacak tahsil süresi 45 gün olan bir işletmede 2025'te kredili net satışlar %25, ortalama ticari alacaklar %50 artmıştır. Buna göre 2025 yılı alacak tahsil süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '67,50',
            'B': '37,50',
            'C': '54',
            'D': '56,25',
            'E': '45',
        },
        'C',
        'Tahsil süresi = 360 × ortalama alacak ÷ satışlar; alacaklar 1,50, satışlar 1,25 katına çıktığından süre 45 × 1,50 ÷ 1,25 = **54 gün** olur.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0036': patch(
        "Bir işletmenin 2024 yılında brüt satışları 900.000 ₺, satış indirimleri 100.000 ₺'dir. 2025'te brüt satışlar %20, satış indirimleri %80 artmıştır. Buna göre net satışların yatay analiz yüzdesi kaçtır?",
        {
            'A': '%11,11',
            'B': '%12,50',
            'C': '%20',
            'D': '−%60',
            'E': '%13,33',
        },
        'B',
        '2024 net satışlar = 800.000 ₺. 2025: brüt 1.080.000 − indirim 180.000 = 900.000 ₺. Değişim = 100.000 ÷ 800.000 = **%12,50**. İndirimlerin hızlı artışı net satış artışını brüt satış artışının altında bırakmıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0037': patch(
        "Bir kalem 2023'te 100.000 ₺, 2024'te 80.000 ₺ ve 2025'te 100.000 ₺'dir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': "İki yıllık toplam değişim %5'tir.",
            'B': "2025'teki artış %20'dir.",
            'C': "Kalem 2025'te 2023'e göre %5 artmıştır.",
            'D': "2024'teki azalış ile 2025'teki artış aynı orandadır.",
            'E': "2025'teki %25'lik artış 2024'teki %20'lik azalışı telafi ederek kalemi 2023 düzeyine döndürmüştür.",
        },
        'E',
        "2024: (80 − 100) ÷ 100 = −%20; 2025: (100 − 80) ÷ 80 = %25. Bazlar farklı olduğundan %20'lik düşüşü telafi etmek için %25'lik artış gerekir; iki yıllık değişim sıfırdır.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0038': patch(
        "Özkaynak kârlılığı 2024'te %30 olan bir mobilya üreticisi 2025'te bedelli sermaye artırımı yapmış; bu yıl net kârı %20, özkaynakları ise %50 artmıştır. Ortaklar, artırımın kârlılığa etkisini görmek istemektedir.\n\nBuna göre özkaynak kârlılığı nasıl değişmiştir?",
        {
            'A': '6 puan azalmıştır.',
            'B': '6 puan artmıştır.',
            'C': '30 puan azalmıştır.',
            'D': 'Değişmemiştir.',
            'E': '%20 artmıştır.',
        },
        'A',
        '2025 özkaynak kârlılığı = %30 × 1,20 ÷ 1,50 = %24 → **6 puan azalmıştır** (oransal olarak %20 düşüş).',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0039': patch(
        "Bir işletmenin 2024 yılında faaliyet kârı 300.000 ₺, finansman giderleri 100.000 ₺'dir; başka olağan gelir ve gider yoktur. 2025'te faaliyet kârı %20, finansman giderleri %50 artmıştır. Buna göre olağan kârın yatay analiz yüzdesi kaçtır?",
        {
            'A': '%10',
            'B': '%20',
            'C': '%5',
            'D': '−%30',
            'E': '−%5',
        },
        'C',
        '2024 olağan kâr = 300.000 − 100.000 = 200.000 ₺; 2025 = 360.000 − 150.000 = 210.000 ₺ → **%5**. Finansman giderlerindeki hızlı artış faaliyet kârı artışının büyük kısmını eritmiştir.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0040': patch(
        "Bir işletmenin 2024 yılında dönen varlıkları 400.000 ₺, duran varlıkları 600.000 ₺'dir. 2025'te dönen varlıklar %30 artmış, duran varlıklar %10 azalmıştır. Buna göre aktif toplamının yatay analiz yüzdesi kaçtır?",
        {
            'A': '%20',
            'B': '−%6',
            'C': '%40',
            'D': '%6',
            'E': '%10',
        },
        'D',
        '2025 aktif = 520.000 + 540.000 = 1.060.000 ₺ → 60.000 ÷ 1.000.000 = **%6**. Grup oranlarının farkı (%20) aktif değişimi değildir; her grup kendi büyüklüğüyle ağırlıklandırılır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0041': patch(
        'Karşılaştırmalı analizde bir kalemin değişim (fark) tutarı nasıl hesaplanır?',
        {
            'A': 'Cari Dönem Tutarı − Önceki (baz) Dönem Tutarı',
            'B': 'Cari Dönem Tutarı × Önceki Dönem Tutarı',
            'C': 'Kalem Tutarı ÷ Toplam Aktif',
            'D': 'Cari Dönem Tutarı ÷ Önceki Dönem Tutarı',
            'E': 'Önceki Dönem Tutarı − Cari Dönem Tutarı',
        },
        'A',
        '**Değişim (fark) Tutarı = Cari Dönem Tutarı − Önceki (baz) Dönem Tutarı**. Pozitifse artış, negatifse azalıştır.',
        'Mali analiz - değişim tutarı',
    ),
    # düzey 2
    '0042': patch(
        'Bir fırın ürünleri üreticisinin iki yıllık gelir tabloları karşılaştırıldığında net satışlarının %20, satışların maliyetinin ise %35 arttığı görülmüştür. Bu dönemde un ve enerji fiyatlarında belirgin artışlar yaşanmıştır.\n\nBu karşılaştırmalı analiz bulgusu en olası olarak neyi gösterir?',
        {
            'A': 'Faaliyet dışı gelirlerin artması nedeniyle özkaynakların güçlendiğini ve borçluluğun azaldığını',
            'B': 'Satışların maliyetlerden daha hızlı arttığını ve bu nedenle brüt kâr marjının belirgin biçimde iyileştiğini',
            'C': 'Maliyetlerin satışlardan daha hızlı arttığını; bunun brüt kâr marjını olumsuz etkileme eğiliminde olduğunu',
            'D': 'Dönem sonunda stokların tamamen tükenerek sıfıra indiğini ve satın alma yapılmadığını',
            'E': 'İşletmenin satış hacminin daraldığını ve brüt kârın önceki yılın altına indiğini gösterdiğini',
        },
        'C',
        'Satışların maliyeti (%35), net satışlardan (%20) **daha hızlı artmışsa**, maliyet baskısı brüt kâr marjını **olumsuz** etkileme eğilimindedir. Yatay analizde kalemlerin göreli büyüme hızları bu şekilde yorumlanır.',
        'Mali analiz - karşılaştırmalı yorum',
    ),
    # düzey 2
    '0043': patch(
        'Bir işletmenin dönen varlıkları %30, kısa vadeli yabancı kaynakları %10 artmıştır. Bu karşılaştırmalı bulgu likidite açısından en olası olarak neyi gösterir?',
        {
            'A': 'Kısa vadeli borçların artmış olmasının işletmenin ödemelerini durdurup iflas ettiği anlamına geldiğini',
            'B': 'Kısa vadeli borçların dönen varlıklardan daha hızlı artması nedeniyle likiditenin (cari oranın) belirgin biçimde zayıfladığını',
            'C': 'Dönen varlıklardaki artışın stok birikiminden kaynaklandığını ve likiditenin zayıfladığını',
            'D': 'Dönen varlık artışının doğrudan dönem kârının düşmesinden kaynaklandığını ve kârlılığın gerilediğini',
            'E': 'Dönen varlıkların kısa vadeli borçlardan daha hızlı artması nedeniyle likiditenin (cari oranın) güçlenme eğiliminde olduğunu',
        },
        'E',
        'Dönen varlıklar (%30), kısa vadeli borçlardan (%10) **daha hızlı** artmışsa cari oran (DV/KVYK) yükselme eğilimindedir → **likidite güçlenir**.',
        'Mali analiz - karşılaştırmalı yorum',
    ),
    # düzey 2
    '0044': patch(
        'Karşılaştırmalı analizin temel amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Tek bir döneme ait mali tabloda her kalemi ait olduğu grup toplamına bölüp yüzdeleyerek o dönemin bileşimini (yapısını) ortaya koymak',
            'B': 'İşletmenin kalemlerinin dönemler arası gelişimini (artış/azalış eğilimini) izleyerek performans ve mali durumdaki değişimi değerlendirmek',
            'C': 'İşletmenin dönem vergi matrahını ve ödenecek vergisini hesaplayarak beyanname için gerekli tutarları tespit etmek',
            'D': 'Aynı döneme ait kalemleri birbirine bölerek likidite, kârlılık ve mali yapı oranları üretmek ve bu oranlar üzerinden değerlendirme yapmak',
            'E': 'Dönem kârını ortaklara ve yedeklere paylaştırarak kâr dağıtım tablosunu düzenlemek ve dağıtılacak tutarları belirlemek',
        },
        'B',
        'Karşılaştırmalı (yatay) analizin amacı; kalemlerin **dönemler arası gelişimini (artış/azalış)** izleyerek işletmenin performans ve mali durumundaki **değişimi** değerlendirmektir.',
        'Mali analiz - karşılaştırmalı analiz',
    ),
    # düzey 2
    '0045': patch(
        'Karşılaştırmalı (yatay) analiz ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yüzde değişim = (Değişim Tutarı ÷ Önceki Dönem) × 100.\n\nII. Statik bir analizdir; yalnızca tek bir döneme ait verilerle yapılır.\n\nIII. Tutar ve yüzde değişim birlikte değerlendirildiğinde daha sağlıklı yorum yapılır.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'D',
        '**II yanlıştır:** Karşılaştırmalı (yatay) analiz **dinamik** bir analizdir ve en az **iki dönemin** verilerinin karşılaştırılmasını gerektirir; tek dönemle yapılamaz. **I** yüzde değişim = (Değişim Tutarı ÷ Önceki Dönem) × 100; **III** tutar ve yüzde birlikte yorumlanır. Doğru cevap **I ve III**.',
        'Mali analiz - karşılaştırmalı analiz',
    ),
    # düzey 2
    '0046': patch(
        "Önceki dönemde tutarı 1.250 ₺ olan bir hesabın cari dönemdeki tutarı 900 ₺'ye inmiştir. Bu hesaptaki değişim oranı yüzde kaçtır?",
        {
            'A': '%38,89',
            'B': '−%28',
            'C': '%28',
            'D': '%72',
            'E': '−%38,89',
        },
        'B',
        'Değişim oranı = (900 − 1.250) ÷ 1.250 = **−%28**. Bölen önceki (baz) dönemdir; cari döneme bölmek −%38,89 verir.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0047': patch(
        "Bir işletmenin 2024 yılına göre 2025 yılında satışları %25, satışların maliyeti %15 artmıştır. 2025 yılı satışları 25.000 ₺ ve 2024 yılı satışların maliyeti 12.000 ₺ olduğuna göre brüt satış kârı 2025'te nasıl değişmiştir?",
        {
            'A': '%10 artmıştır.',
            'B': '%72,50 artmıştır.',
            'C': '%25 artmıştır.',
            'D': '%15 azalmıştır.',
            'E': '%40 artmıştır.',
        },
        'E',
        '2024 satışları = 25.000 ÷ 1,25 = 20.000 ₺ → brüt kâr 8.000 ₺. 2025 satışların maliyeti = 12.000 × 1,15 = 13.800 ₺ → brüt kâr 11.200 ₺. Değişim = 3.200 ÷ 8.000 = **%40**. Oranların farkını (%10) almak yanlıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0048': patch(
        'Bir işletmenin bazı gelir tablosu kalemleri şöyledir:\n\n| Kalem | Önceki (₺) | Cari (₺) |\n|---|---|---|\n| Brüt satışlar | 10.500.000 | 12.000.000 |\n| Net satışlar | 8.500.000 | 9.000.000 |\n| Satışların maliyeti | 4.500.000 | 4.000.000 |\n| Faaliyet giderleri | 1.500.000 | 2.000.000 |\n| Olağan kâr | 75.000 | 100.000 |\n\nBuna göre brüt satış kârının yatay analiz yüzdesi kaçtır?',
        {
            'A': '%33,33',
            'B': '%5,88',
            'C': '%20',
            'D': '%25',
            'E': '%14,29',
        },
        'D',
        'Brüt satış kârı = net satışlar − satışların maliyeti: önceki 4.000.000 ₺, cari 5.000.000 ₺ → **%25**. Brüt satışlardan hesaplamak %33,33, faaliyet kârına bakmak %20 verir.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0049': patch(
        "Cari dönemde satışlarının maliyeti 40.000 ₺ olan bir işletmenin karşılaştırmalı analizinde net satışların 10.000 ₺ tutarında ve %20 oranında arttığı görülmüştür. Buna göre cari dönem brüt satış kârı kaç ₺'dir?",
        {
            'A': '10.000',
            'B': '12.000',
            'C': '20.000',
            'D': '60.000',
            'E': '8.000',
        },
        'C',
        'Önceki dönem net satışları = 10.000 ÷ 0,20 = 50.000 ₺; cari = 60.000 ₺. Brüt satış kârı = 60.000 − 40.000 = **20.000 ₺**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0050': patch(
        "Bir işletmenin 2024 bilançosu şöyledir:\n\n| Kalem | 2024 (₺) |\n|---|---|\n| Dönen varlıklar | 40.000 |\n| Duran varlıklar | 60.000 |\n| KVYK | 40.000 |\n| UVYK | 20.000 |\n| Özkaynaklar | 40.000 |\n\n2025'te aktif toplamı %20, kaldıraç oranı (yabancı kaynak ÷ aktif) %25, cari oran %50 artmış; uzun vadeli yabancı kaynaklar değişmemiştir. Buna göre duran varlıkların yatay analiz yüzdesi kaçtır?",
        {
            'A': '−%75',
            'B': '−%50',
            'C': '−%25',
            'D': '%75',
            'E': '%20',
        },
        'A',
        '2025 aktif = 120.000 ₺. Kaldıraç 0,60 × 1,25 = 0,75 → yabancı kaynak 90.000 ₺; UVYK 20.000 → KVYK 70.000 ₺. Cari 1 × 1,5 = 1,5 → dönen varlıklar 105.000 ₺; duran varlıklar 120.000 − 105.000 = 15.000 ₺. Değişim = (15.000 − 60.000) ÷ 60.000 = **−%75**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletmenin net satışları 2023'ten 2024'e %20, 2024'ten 2025'e %25 artmıştır. Buna göre net satışların 2023'e göre 2025'teki artış oranı yüzde kaçtır?",
        {
            'A': '%48',
            'B': '%45',
            'C': '%5',
            'D': '%22,50',
            'E': '%50',
        },
        'E',
        'Artışlar birleşik olarak uygulanır: 1,20 × 1,25 = 1,50 → **%50**. Oranları toplamak (%45) yanlıştır; her yılın oranı farklı bir baza göre hesaplanmıştır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletmenin 2024 yılı net satışları 500.000 ₺ ve net kâr marjı %8'dir. 2025'te net satışlar %20 artmış, net kâr marjı %10 olmuştur. Buna göre net kârın yatay analiz yüzdesi kaçtır?",
        {
            'A': '%20',
            'B': '%50',
            'C': '%2',
            'D': '%25',
            'E': '%45',
        },
        'B',
        '2024 net kâr = 500.000 × %8 = 40.000 ₺; 2025 = 600.000 × %10 = 60.000 ₺. Değişim = 20.000 ÷ 40.000 = **%50**. Satış artışı (%20) ile marj artışı (%25) birleşik etki yapar: 1,20 × 1,25 = 1,50.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0053': patch(
        "Bir işletmenin 2024 yılı net satışları 1.000.000 ₺, faaliyet giderleri 150.000 ₺'dir. 2025'te net satışlar %20, faaliyet giderleri %10 artmıştır. Buna göre faaliyet giderlerinin net satışlara oranı nasıl değişmiştir?",
        {
            'A': '1,25 puan azalmıştır.',
            'B': '10 puan azalmıştır.',
            'C': 'Değişmemiştir.',
            'D': '%10 artmıştır.',
            'E': '1,25 puan artmıştır.',
        },
        'A',
        '2024: 150.000 ÷ 1.000.000 = %15. 2025: 165.000 ÷ 1.200.000 = %13,75. Oran **1,25 puan azalmıştır**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0054': patch(
        "Cari dönemde 546.000 ₺ olan bir kalem önceki döneme göre %30 artmıştır. Kalemin önceki dönem tutarı kaç ₺'dir?",
        {
            'A': '709.800',
            'B': '382.200',
            'C': '416.000',
            'D': '420.000',
            'E': '163.800',
        },
        'D',
        "Önceki tutar = 546.000 ÷ 1,30 = **420.000 ₺**. Cari tutarın %30'unu düşmek (382.200) yanlıştır; artış önceki tutar üzerinden hesaplanmıştır.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0055': patch(
        'Karşılaştırmalı analizle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bir kalemin art arda iki yıldaki değişim oranları toplanarak iki yıllık toplam değişim bulunur.\n\nII. Önceki dönem tutarı sıfır olan bir kalemin yüzde değişimi hesaplanamaz.\n\nIII. Önceki dönem tutarı negatif olan bir kalemin yüzde değişimi sonucun yönünü doğru gösterir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'C',
        '**I yanlıştır:** oranlar farklı bazlara göre hesaplandığından birleşik uygulanır (1,20 × 1,25). **II doğrudur.** **III yanlıştır:** negatif bazla oran işaret olarak yanıltıcıdır (zarardan kâra geçişte negatif çıkar). Doğru cevap **Yalnız II**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0056': patch(
        "Bir işletmenin 2024 yılında net satışları 1.000.000 ₺, satışların maliyeti 600.000 ₺, faaliyet giderleri 200.000 ₺'dir. 2025'te net satışlar %10, satışların maliyeti %5, faaliyet giderleri %20 artmıştır. Buna göre faaliyet kârının yatay analiz yüzdesi kaçtır?",
        {
            'A': '−%15',
            'B': '%25',
            'C': '%10',
            'D': '%15',
            'E': '%35',
        },
        'D',
        '2024 faaliyet kârı = 200.000 ₺. 2025: 1.100.000 − 630.000 − 240.000 = 230.000 ₺. Değişim = 30.000 ÷ 200.000 = **%15**. Oranları toplayıp çıkarmak (%10 − %5 − %20) anlamsızdır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0057': patch(
        "Bir işletmenin 2024 yılında satışların maliyetinin net satışlara oranı %60'tır. 2025'te net satışlar %25, satışların maliyeti %40 artmıştır. Buna göre 2025 yılı brüt kâr marjı yüzde kaçtır?",
        {
            'A': '%67,20',
            'B': '%40',
            'C': '%25',
            'D': '%35',
            'E': '%32,80',
        },
        'E',
        "2025 maliyet oranı = %60 × 1,40 ÷ 1,25 = %67,20 → brüt kâr marjı = %100 − %67,20 = **%32,80** (2024'te %40).",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletmenin dönen varlıkları 2024'te 500.000 ₺, 2025'te 600.000 ₺; kısa vadeli yabancı kaynakları her iki yılda 400.000 ₺'dir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Cari oran değişmemiştir.',
            'B': 'Cari oran %20 artarak 1,25 olmuştur.',
            'C': 'Net çalışma sermayesi %100 artmıştır.',
            'D': 'Net çalışma sermayesi %20 artmıştır.',
            'E': 'Net çalışma sermayesi 200.000 ₺ artmıştır.',
        },
        'C',
        "NÇS 100.000'den 200.000 ₺'ye çıkmış, **%100** (100.000 ₺) artmıştır. Cari oran 1,25'ten 1,50'ye, yani %20 artmıştır. Dönen varlıklardaki %20'lik artış, KVYK sabit kaldığı için NÇS'yi çok daha hızlı artırmıştır.",
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 3
    '0059': patch(
        "2024'te ortalama stokta kalma süresi 60 gün olan bir işletmede 2025'te satışların maliyeti %25 artmış, ortalama stoklar %20 azalmıştır. Buna göre 2025 yılı stokta kalma süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '93,75',
            'B': '38,40',
            'C': '48',
            'D': '57,60',
            'E': '45',
        },
        'B',
        'Süre = 360 × ortalama stok ÷ satışların maliyeti → 60 × 0,80 ÷ 1,25 = **38,40 gün**.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
    ),
    # düzey 2
    '0060': patch(
        'Genel fiyat düzeyinin hızla arttığı bir dönemde bir analist, enflasyon düzeltmesi yapılmamış ve cari fiyatlarla hazırlanmış iki yıllık mali tablolara karşılaştırmalı analiz uygulamıştır. Analiz sonucunda satışlar ve kârlarda yüksek oranlı artışlar görülmüştür.\n\nBu analizle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tutar artışları reel büyümeye eşit kabul edilir.',
            'B': 'Fiyat artışları yüzde değişimleri etkilemez, tutar değişimlerini etkiler.',
            'C': 'Karşılaştırmalı analiz enflasyonlu dönemlerde yapılamaz.',
            'D': 'Kalemlerdeki tutar artışları, reel büyümeyi olduğundan yüksek gösterebilir.',
            'E': 'Enflasyon bilanço kalemlerini değil, gelir tablosu kalemlerini etkiler.',
        },
        'D',
        'Cari fiyatlarla hazırlanan tablolarda artışın bir kısmı fiyat etkisidir; bu nedenle yüksek enflasyonda satış ve kârdaki artış reel büyümeyi abartabilir. Yorum yapılırken fiyat etkisi dikkate alınmalıdır.',
        'Mali analiz - karşılaştırmalı (yatay) analiz',
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
    print(f"1 paket / {len(PATCHES)} soru ('Karsilastirmali Analiz' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
