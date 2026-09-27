#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Likidite Oranlari ve Calisma Sermayesi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

YENI KONU (mali tablolar analizi). Gercek sinavda MTA sorularinin ~yarisi oran analizinden, en buyuk grup likidite (28 soru); tek oran paketi bunu karsilamiyordu, trend ve fon akim analizinin (2019-2026'da 0 soru) yerine acildi. 60 soru her biri kendi verisiyle: tablodan cari/asit/nakit, katı asit-test, brut/net/safi calisma sermayesi, stok bagimlilik, oran zincirinden geriye (stok, KVYK, donen varlik, alacak), hedef orana ulasma (odeme/kredi/alim), devamli sermaye ve duran varlik oranlariyla bilanco kurgusu, islemlerin cari/asit/NCS'ye etkisi (oran 1'in ustu/alti), vade aktarimi, supheli alacak karsiligi, FIFO etkisi, iki donem karsilastirma. Oranlar Fraction ile hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Mali tablolar analizi - likidite oranlari ve calisma sermayesi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/mali_tablolar_analizi/likidite_ve_calisma_sermayesi.json"
STYLE_REF = 'SGS Mali Tablolar Analizi (oran zinciri, ters hesap; gerçek sınav profiline kalibre)'
ONEK = "mta-likid-gen-"


def patch(stem, options, answer, solution, ref='Mali analiz - likidite oranları'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir işletmenin bilançosundan alınan bilgiler şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Hazır değerler | 18.000 |\n| Menkul kıymetler | 12.000 |\n| Ticari alacaklar | 80.000 |\n| Stoklar | 100.000 |\n| Diğer dönen varlıklar | 10.000 |\n| Kısa vadeli yabancı kaynaklar | 100.000 |\n\nBuna göre cari oran, asit-test oranı ve nakit oranı sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
        {
            'A': '2,20 · 1,20 · 0,30',
            'B': '2,20 · 1 · 0,30',
            'C': '1,20 · 2,20 · 0,30',
            'D': '2,20 · 1,10 · 0,30',
            'E': '2,20 · 1,20 · 0,18',
        },
        'A',
        'Dönen varlıklar = 220.000 ₺. Cari = 220.000 ÷ 100.000 = 2,20; asit-test = (220.000 − 100.000) ÷ 100.000 = 1,20; nakit = (18.000 + 12.000) ÷ 100.000 = 0,30. Asit-testte yalnız stoklar düşülür.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0002': patch(
        'Bir işletmenin iki yıla ait bilgileri şöyledir:\n\n| Kalem | 2024 (₺) | 2025 (₺) |\n|---|---|---|\n| Dönen varlıklar | 450.000 | 540.000 |\n| Stoklar | 180.000 | 300.000 |\n| KVYK | 300.000 | 300.000 |\n\nBuna göre işletmenin likiditesiyle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Cari oran ve asit-test oranı birlikte yükselmiş; likidite her açıdan güçlenmiştir.',
            'B': "Cari oran 1,50'den 1,80'e yükselirken asit-test oranı 0,90'dan 0,80'e düşmüş; artış stoklardan kaynaklanmıştır.",
            'C': 'Net çalışma sermayesi azalmıştır.',
            'D': 'Cari oran düşmüş, asit-test oranı yükselmiştir.',
            'E': "Cari oran 1,50'den 1,80'e yükselmiş, asit-test oranı değişmemiştir.",
        },
        'B',
        "2024: cari 450 ÷ 300 = 1,50, asit (450 − 180) ÷ 300 = 0,90. 2025: cari 1,80, asit (540 − 300) ÷ 300 = 0,80. Dönen varlık artışı (90.000) stok artışından (120.000) küçük; diğer dönen varlıklar azalmıştır. NÇS 150.000'den 240.000 ₺'ye çıkmıştır.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0003': patch(
        'Net satışları 1.200.000 ₺, dönen varlıkları 500.000 ₺ ve kısa vadeli yabancı kaynakları 300.000 ₺ olan bir işletmenin net çalışma sermayesi devir hızı kaçtır?',
        {
            'A': '6',
            'B': '2,40',
            'C': '4',
            'D': '1,50',
            'E': '0,17',
        },
        'A',
        'NÇS = 500.000 − 300.000 = 200.000 ₺. Devir hızı = 1.200.000 ÷ 200.000 = **6**. Dönen varlıklara bölmek brüt çalışma sermayesi devir hızını (2,40) verir.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0004': patch(
        "Nakit oranı 0,25 olan bir işletmenin hazır değerleri 9.000 ₺, menkul kıymetleri 6.000 ₺'dir. Net çalışma sermayesi 36.000 ₺ olduğuna göre cari oran kaçtır?",
        {
            'A': '3,40',
            'B': '0,60',
            'C': '1,36',
            'D': '1,60',
            'E': '2,40',
        },
        'D',
        'KVYK = 15.000 ÷ 0,25 = 60.000 ₺. Dönen varlıklar = 60.000 + 36.000 = 96.000 ₺. Cari oran = 96.000 ÷ 60.000 = **1,60**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0005': patch(
        "Kısa vadeli yabancı kaynakları 80.000 ₺ olan bir işletmenin cari oranı 1,50'dir. İşletme 20.000 ₺ uzun vadeli kredi alıp bunun tamamıyla kısa vadeli borç öderse yeni cari oranı kaç olur?",
        {
            'A': '1,50',
            'B': '2,50',
            'C': '2',
            'D': '1,75',
            'E': '1,25',
        },
        'C',
        'Başlangıçta dönen varlıklar 120.000 ₺. Kredi nakdi getirir (+20.000), aynı nakitle KVYK ödenir (−20.000): dönen varlıklar 120.000 ₺ kalır, KVYK 60.000 ₺ olur. Cari oran = **2**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0006': patch(
        "Asit-test oranı 1,20 olan bir işletmenin stokları 30.000 ₺, dönen varlıkları 90.000 ₺'dir. Buna göre cari oran kaçtır?",
        {
            'A': '3',
            'B': '1,80',
            'C': '1,50',
            'D': '1,20',
            'E': '0,60',
        },
        'B',
        'Asit-test payı = 90.000 − 30.000 = 60.000 ₺ → KVYK = 60.000 ÷ 1,20 = 50.000 ₺. Cari oran = 90.000 ÷ 50.000 = **1,80**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0007': patch(
        "Dönen varlıkları 200.000 ₺, kısa vadeli yabancı kaynakları 100.000 ₺ olan bir işletme kısa vadeli kredi kullanarak ticari mal satın alacaktır. Cari oranın 1,50'nin altına düşmemesi için en fazla kaç ₺'lik alım yapılabilir?",
        {
            'A': '50.000',
            'B': '150.000',
            'C': '75.000',
            'D': '100.000',
            'E': '200.000',
        },
        'D',
        "(200.000 + x) ÷ (100.000 + x) = 1,50 → 200.000 + x = 150.000 + 1,5x → 0,5x = 50.000 → x = **100.000 ₺**. Pay ve payda aynı tutarda arttığından oran 2'den 1,50'ye iner.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0008': patch(
        "Bir işletmenin duran varlıklarının devamlı sermayeye oranı 0,90'dır. Devamlı sermaye 500.000 ₺, kısa vadeli yabancı kaynaklar 125.000 ₺ olduğuna göre cari oran kaçtır?",
        {
            'A': '0,90',
            'B': '1,10',
            'C': '4',
            'D': '0,40',
            'E': '1,40',
        },
        'E',
        'Duran varlıklar = 450.000 ₺. Aktif = pasif = 625.000 ₺ → dönen varlıklar = 175.000 ₺. Cari oran = 175.000 ÷ 125.000 = **1,40**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0009': patch(
        "Duran varlıklarının toplamı dönen varlıklarının 1,5 katı olan bir işletmenin devamlı sermayesi 90.000 ₺, net çalışma sermayesi 15.000 ₺'dir. Buna göre işletmenin aktif toplamı kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '150.000',
            'C': '112.500',
            'D': '125.000',
            'E': '105.000',
        },
        'D',
        'Duran varlıklar = devamlı sermaye − NÇS = 75.000 ₺. Dönen varlıklar = 75.000 ÷ 1,5 = 50.000 ₺. Aktif = **125.000 ₺**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0010': patch(
        'Cari oranı 1,60 olan bir işletmede aşağıdaki işlemlerden hangisi cari oranı artırır?',
        {
            'A': 'Ticari alacakların bir kısmının tahsil edilmesi',
            'B': 'Kısa vadeli kredi ile demirbaş satın alınması',
            'C': 'Kasadaki nakitle hisse senedi (menkul kıymet) satın alınması',
            'D': 'Kısa vadeli borçların bir kısmının kasadaki nakitle ödenmesi',
            'E': 'Kısa vadeli kredi ile ticari mal satın alınması',
        },
        'D',
        "Oran 1'den büyükken pay ve payda aynı tutarda azalınca oran yükselir (ör. 160/100 → 140/80 = 1,75). Kısa vadeli krediyle mal almak oranı 1'e yaklaştırır (düşürür); demirbaş almak KVYK'yı artırır. Alacak tahsili ve nakitle menkul kıymet alımı dönen varlıklar içinde yer değiştirmedir.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdaki işlemlerden hangisi net çalışma sermayesini değiştirmez?',
        {
            'A': 'Nakdi sermaye artırımı yapılması',
            'B': 'Uzun vadeli kredi ile kasaya nakit girişi sağlanması',
            'C': 'Kısa vadeli borçların kasadaki nakitle ödenmesi',
            'D': 'Kısa vadeli kredi ile makine satın alınması',
            'E': 'Nakitle arsa satın alınması',
        },
        'C',
        "Nakitle kısa vadeli borç ödemede dönen varlıklar ve KVYK aynı tutarda azalır; NÇS (farkları) değişmez. Diğer işlemler dönen varlıkları ya da KVYK'yı tek başına değiştirir.",
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0012': patch(
        "Cari oranı 1,20 olan bir işletmede aşağıdaki işlemlerden hangileri cari oranı artırır?\n\nI. Maliyeti 40.000 ₺ olan malın 55.000 ₺'ye peşin satılması\n\nII. Kısa vadeli kredi ile taşıt satın alınması\n\nIII. Vadesine bir yıldan az kalan uzun vadeli banka kredisinin kısa vadeli borçlara aktarılması",
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        '**I artırır:** dönen varlıklar kâr kadar (15.000) artar. **II azaltır:** KVYK artar, taşıt duran varlıktır. **III azaltır:** KVYK artar. Doğru cevap **Yalnız I**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0013': patch(
        "Dönen varlıkları 200.000 ₺ (stoklar 80.000 ₺), kısa vadeli yabancı kaynakları 100.000 ₺ olan bir işletme, maliyeti 40.000 ₺ olan stokunu 60.000 ₺'ye peşin satmıştır. Bu işlemden sonra asit-test oranı kaçtır?",
        {
            'A': '1,20',
            'B': '1,60',
            'C': '2,20',
            'D': '1,40',
            'E': '1,80',
        },
        'E',
        "Stoklar 40.000 ₺'ye iner, nakit 60.000 ₺ artar: dönen varlıklar 220.000 ₺. Asit-test = (220.000 − 40.000) ÷ 100.000 = **1,80** (işlemden önce 1,20).",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0014': patch(
        'Sektör ortalamasının çok üzerinde, örneğin 5 düzeyinde cari oranı olan bir işletme için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'İşletme kısa vadeli borç ödeme güçlüğü çekmektedir.',
            'B': 'Net çalışma sermayesi negatiftir.',
            'C': 'Stoklar dönen varlıkların tamamını oluşturur.',
            'D': 'İşletmenin özkaynakları negatiftir.',
            'E': 'Dönen varlıklarda atıl fon bulunabilir; kaynaklar kârlılığı düşürecek biçimde verimsiz kullanılıyor olabilir.',
        },
        'E',
        "Çok yüksek cari oran likiditenin güçlü olduğunu gösterir; ancak getirisi düşük nakit, stok ya da alacakta fazla fon tutulduğuna da işaret edebilir. Bu nedenle 'ne kadar yüksek o kadar iyi' denemez.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0015': patch(
        'Aşağıdakilerden hangisi bir işletmenin likidite durumu hakkında bilgi vermez?',
        {
            'A': 'Nakit oranı',
            'B': 'Asit-test oranı',
            'C': 'Stok bağımlılık oranı',
            'D': 'Özsermaye kârlılığı',
            'E': 'Net çalışma sermayesi',
        },
        'D',
        'Özsermaye kârlılığı (net kâr ÷ özkaynak) bir kârlılık oranıdır. Diğerleri kısa vadeli borç ödeme gücüyle ilgilidir.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0016': patch(
        'Bir işletmenin cari oranı önceki yıla göre yükselmiş, nakit oranı ise düşmüştür. Bu durumun en olası açıklaması aşağıdakilerden hangisidir?',
        {
            'A': 'Kısa vadeli yabancı kaynaklar önemli ölçüde artmıştır.',
            'B': 'Stoklar ve alacaklar önemli ölçüde azalmıştır.',
            'C': 'Dönen varlıklar içinde stok ve alacakların payı artmış, hazır değer ve menkul kıymetlerin payı azalmıştır.',
            'D': 'Hazır değerler dönen varlıklardan hızlı artmıştır.',
            'E': 'Dönen varlıklar azalırken hazır değerler artmıştır.',
        },
        'C',
        'Cari oranın yükselip nakit oranının düşmesi, dönen varlıklardaki artışın en likit olmayan kalemlerden (stok, alacak) geldiğini ve en likit kalemlerin payının azaldığını gösterir.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0017': patch(
        "Bir işletmenin hazır değer ve menkul kıymetleri 2024'te 40.000 ₺, 2025'te 30.000 ₺; kısa vadeli yabancı kaynakları 2024'te 100.000 ₺, 2025'te 120.000 ₺'dir. Buna göre nakit oranı nasıl değişmiştir?",
        {
            'A': 'Değişmemiştir.',
            'B': "0,40'tan 0,25'e düşmüştür.",
            'C': "0,40'tan 0,30'a düşmüştür.",
            'D': '%25 azalmıştır.',
            'E': "0,25'ten 0,40'a yükselmiştir.",
        },
        'B',
        '2024: 40.000 ÷ 100.000 = 0,40; 2025: 30.000 ÷ 120.000 = **0,25**. Pay azalırken payda arttığından düşüş belirgindir.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0018': patch(
        "Bir işletmenin 2024'te dönen varlıkları 500.000 ₺, kısa vadeli yabancı kaynakları 400.000 ₺'dir. 2025'te dönen varlıklar %20, kısa vadeli yabancı kaynaklar %10 artmıştır. Buna göre net çalışma sermayesinin değişim oranı yüzde kaçtır?",
        {
            'A': '%60',
            'B': '%20',
            'C': '%30',
            'D': '%10',
            'E': '%50',
        },
        'A',
        "2024 NÇS = 100.000 ₺; 2025 = 600.000 − 440.000 = 160.000 ₺ → **%60** artış. Kalemlerdeki küçük oransal farklar, farkları olan NÇS'yi büyük ölçüde değiştirir.",
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0019': patch(
        "Devamlı sermayesinin %25'i dönen varlıkların finansmanında kullanılan bir işletmenin devamlı sermayesi 400.000 ₺ ve kısa vadeli yabancı kaynakları 200.000 ₺'dir. Buna göre cari oran kaçtır?",
        {
            'A': '3',
            'B': '0,50',
            'C': '1,50',
            'D': '1,25',
            'E': '2',
        },
        'C',
        'Devamlı sermayenin dönen varlıkları finanse eden kısmı net çalışma sermayesidir: 400.000 × %25 = 100.000 ₺. Dönen varlıklar = 200.000 + 100.000 = 300.000 ₺. Cari oran = **1,50**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0020': patch(
        'Net çalışma sermayesi devir hızı sektör ortalamasının çok üzerinde olan bir işletme için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Cari oranı sektör ortalamasının çok üzerindedir.',
            'B': 'İşletmenin satışları sektöre göre düşüktür.',
            'C': 'Net çalışma sermayesinde atıl fon birikmiştir.',
            'D': "Dönen varlıkları KVYK'dan küçüktür.",
            'E': 'Satış hacmine göre net çalışma sermayesi yetersiz kalmış olabilir.',
        },
        'E',
        'Yüksek devir hızı, satışların görece küçük bir net çalışma sermayesiyle yürütüldüğünü gösterir; bu verimlilik anlamına gelebileceği gibi sermaye yetersizliği ve likidite baskısına da işaret edebilir.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0021': patch(
        "Bir işletmenin dönen varlıkları 540.000 ₺ olup bunun 180.000 ₺'si stoklar, 36.000 ₺'si gelecek aylara ait giderlerdir. Kısa vadeli yabancı kaynakları 240.000 ₺'dir. Stoklarla birlikte nakde dönüşmeyecek peşin ödenmiş giderlerin de düşüldüğü likidite (asit-test) oranı kaçtır?",
        {
            'A': '1,50',
            'B': '1,35',
            'C': '2,25',
            'D': '0,90',
            'E': '2,10',
        },
        'B',
        'Nakde dönüşmeyecek kalemler (stok ve peşin ödenmiş gider) düşülür: (540.000 − 180.000 − 36.000) ÷ 240.000 = **1,35**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0022': patch(
        "Bir işletmenin hazır değerleri 24.000 ₺, menkul kıymetleri 16.000 ₺, ticari alacakları 60.000 ₺ ve kısa vadeli yabancı kaynakları 80.000 ₺'dir. Buna göre nakit oranı kaçtır?",
        {
            'A': '0,75',
            'B': '0,20',
            'C': '1,25',
            'D': '0,50',
            'E': '0,30',
        },
        'D',
        'Nakit oranı = (hazır değerler + menkul kıymetler) ÷ KVYK = 40.000 ÷ 80.000 = **0,50**. Ticari alacaklar asit-test oranına girer, nakit oranına girmez.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0023': patch(
        'Net satışları 1.800.000 ₺ ve ortalama dönen varlıkları 600.000 ₺ olan bir işletmenin dönen varlık devir hızı kaçtır ve bir dönen varlık devri kaç gün sürer? (1 yıl = 360 gün)',
        {
            'A': '0,33 ve 120 gün',
            'B': '3 ve 120 gün',
            'C': '4 ve 90 gün',
            'D': '3 ve 90 gün',
            'E': '3 ve 60 gün',
        },
        'B',
        'Dönen varlık devir hızı = 1.800.000 ÷ 600.000 = **3**; süre = 360 ÷ 3 = **120 gün**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0024': patch(
        "Cari oranı 1,75 olan bir işletmenin net çalışma sermayesi 45.000 ₺'dir. Buna göre işletmenin kısa vadeli yabancı kaynakları ve dönen varlıkları sırasıyla kaç ₺'dir?",
        {
            'A': '60.000 ve 105.000',
            'B': '45.000 ve 78.750',
            'C': '25.000 ve 70.000',
            'D': '60.000 ve 78.750',
            'E': '105.000 ve 60.000',
        },
        'A',
        'Dönen varlıklar = 1,75 × KVYK; NÇS = 0,75 × KVYK = 45.000 → KVYK = **60.000 ₺**, dönen varlıklar = **105.000 ₺**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0025': patch(
        "Bir işletmenin cari oranı 1,80'dir. Stokları dönen varlıklarının %40'ı olduğuna göre asit-test oranı kaçtır?",
        {
            'A': '1,44',
            'B': '1,80',
            'C': '0,72',
            'D': '1,40',
            'E': '1,08',
        },
        'E',
        "Asit-test = cari × (1 − stok payı) = 1,80 × 0,60 = **1,08**. Stoklar KVYK'nın 1,80 × 0,40 = 0,72 katıdır.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0026': patch(
        "Net satışları 900.000 ₺ olan bir işletmenin net çalışma sermayesi devir hızı 6, cari oranı 2,50'dir. Buna göre dönen varlıkları kaç ₺'dir?",
        {
            'A': '375.000',
            'B': '250.000',
            'C': '360.000',
            'D': '150.000',
            'E': '100.000',
        },
        'B',
        'NÇS = 900.000 ÷ 6 = 150.000 ₺ = 1,5 × KVYK → KVYK = 100.000 ₺. Dönen varlıklar = 2,50 × 100.000 = **250.000 ₺**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0027': patch(
        "Hazır değerleri ve menkul kıymetleri toplamı 30.000 ₺, kısa vadeli yabancı kaynakları 120.000 ₺ olan bir işletme nakit oranını 0,40'a çıkarmak için uzun vadeli kredi kullanarak kasaya nakit girişi sağlayacaktır. Kaç ₺ kredi kullanmalıdır?",
        {
            'A': '30.000',
            'B': '20.000',
            'C': '18.000',
            'D': '48.000',
            'E': '12.000',
        },
        'C',
        "(30.000 + x) ÷ 120.000 = 0,40 → x = **18.000 ₺**. Uzun vadeli kredi KVYK'yı değiştirmez; yalnız pay artar.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0028': patch(
        "Aktif toplamı 400.000 ₺ olan bir işletmede duran varlıklar dönen varlıkların 3 katıdır. Devamlı sermaye 350.000 ₺ olduğuna göre net çalışma sermayesi kaç ₺'dir?",
        {
            'A': '−50.000',
            'B': '250.000',
            'C': '100.000',
            'D': '50.000',
            'E': '300.000',
        },
        'D',
        'Dönen varlıklar = 400.000 ÷ 4 = 100.000 ₺; duran varlıklar 300.000 ₺. NÇS = devamlı sermaye − duran varlıklar = 350.000 − 300.000 = **50.000 ₺** (KVYK 50.000 ₺).',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0029': patch(
        "Pasif toplamı 60.000 ₺ olan bir işletmede duran varlıklar dönen varlıkların 3 katıdır ve sürekli sermaye 54.000 ₺'dir. Buna göre cari oran kaçtır?",
        {
            'A': '0,40',
            'B': '1,50',
            'C': '2,50',
            'D': '2',
            'E': '3',
        },
        'C',
        'Dönen varlıklar = 60.000 ÷ 4 = 15.000 ₺; KVYK = 60.000 − 54.000 = 6.000 ₺. Cari oran = 15.000 ÷ 6.000 = **2,50**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0030': patch(
        "Aktif toplamı 500.000 ₺ olan bir işletmede duran varlıklar aktifin %70'i, devamlı sermaye pasifin %60'ıdır. Buna göre cari oran kaçtır?",
        {
            'A': '0,86',
            'B': '1,17',
            'C': '0,75',
            'D': '1,33',
            'E': '0,43',
        },
        'C',
        'Dönen varlıklar %30 (150.000 ₺), KVYK %40 (200.000 ₺). Cari oran = 150.000 ÷ 200.000 = **0,75**; NÇS −50.000 ₺. Duran varlıkların bir kısmı kısa vadeli kaynakla finanse edilmektedir.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0031': patch(
        'Cari oranı 0,80 olan bir işletmede aşağıdaki işlemlerden hangisi cari oranı düşürür?',
        {
            'A': 'Kısa vadeli borçların bir kısmının kasadaki nakitle ödenmesi',
            'B': 'Stokların bir kısmının maliyet bedeline peşin satılması',
            'C': 'Ticari alacakların bir kısmının tahsil edilmesi',
            'D': 'Nakdi sermaye artırımı yapılması',
            'E': 'Uzun vadeli kredi ile kasaya nakit girişi sağlanması',
        },
        'A',
        "Oran 1'in altındayken pay ve payda aynı tutarda azalınca oran düşer (ör. 80/100 → 60/80 = 0,75). Uzun vadeli kredi ve sermaye artırımı payı artırır; tahsilat ve maliyet bedeline satış dönen varlıklar içinde yer değiştirmedir.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0032': patch(
        'Dönen varlıkları 300.000 ₺, kısa vadeli yabancı kaynakları 150.000 ₺ olan bir işletme önce 50.000 ₺ kısa vadeli borcunu nakitle ödemiş, ardından 25.000 ₺ kısa vadeli kredi ile makine satın almıştır. Bu işlemlerden sonra cari oran kaçtır?',
        {
            'A': '2,20',
            'B': '2',
            'C': '1,83',
            'D': '2,50',
            'E': '1,67',
        },
        'B',
        'Ödemeden sonra: 250.000 ÷ 100.000 = 2,50. Kredili makine alımıyla KVYK 125.000 ₺ olur; dönen varlıklar değişmez. Cari oran = 250.000 ÷ 125.000 = **2**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0033': patch(
        'Cari oranı 0,90 olan bir işletme için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Özkaynaklar negatiftir.',
            'B': 'Nakit oranı cari orandan büyüktür.',
            'C': "Asit-test oranı 1'den büyüktür.",
            'D': 'Duran varlıklar devamlı sermayeden küçüktür.',
            'E': 'Net çalışma sermayesi negatiftir.',
        },
        'E',
        "Cari oran 1'in altındaysa dönen varlıklar KVYK'dan küçüktür; NÇS negatiftir ve duran varlıkların bir kısmı kısa vadeli kaynakla finanse edilir. Asit-test ve nakit oranı cari orandan büyük olamaz; özkaynak hakkında bilgi yoktur.",
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0034': patch(
        'Cari oranı 2,00, asit-test oranı 0,60 ve nakit oranı 0,10 olan bir işletme için aşağıdakilerden hangisi kesin olarak doğrudur?',
        {
            'A': 'Stoklar dönen varlıkların yarısıdır.',
            'B': 'Ticari alacaklar kısa vadeli yabancı kaynakların yarısıdır.',
            'C': "Hazır değerler kısa vadeli yabancı kaynakların %10'udur.",
            'D': 'Stoklar kısa vadeli yabancı kaynakların 1,4 katıdır.',
            'E': 'Net çalışma sermayesi negatiftir.',
        },
        'D',
        "Stoklar ÷ KVYK = cari − asit = 1,40 (dönen varlıkların %70'i). Asit − nakit = 0,50 alacak ve diğer likit kalemleri gösterir; alacakların tek başına payı kesin değildir. Nakit oranı hazır değer ile menkul kıymetin toplamıdır, hazır değerin tek başına payı bilinmez.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0035': patch(
        'Likidite oranlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aynı işletmede nakit oranı asit-test oranından, asit-test oranı da cari orandan büyük olamaz.\n\nII. Asit-test oranı 1 ise kısa vadeli borçlar stoklar satılmadan karşılanabilir.\n\nIII. Cari oran 2 ise net çalışma sermayesi aktif toplamının yarısıdır.',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'C',
        "**I doğrudur:** paylar sırasıyla genişler (hazır+menkul ⊂ stok dışı dönen ⊂ dönen). **II doğrudur.** **III yanlıştır:** cari 2 ise NÇS KVYK'ya eşittir; aktif içindeki payı bilinmez. Doğru cevap **I ve II**.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0036': patch(
        "Bir işletmenin 2024'te dönen varlıkları 400.000 ₺, kısa vadeli yabancı kaynakları 250.000 ₺; 2025'te dönen varlıkları 450.000 ₺, kısa vadeli yabancı kaynakları 330.000 ₺'dir. Buna göre net çalışma sermayesi nasıl değişmiştir?",
        {
            'A': '%20 azalmıştır.',
            'B': '30.000 ₺ artmıştır.',
            'C': '%32 azalmıştır.',
            'D': 'Değişmemiştir.',
            'E': '%12,50 artmıştır.',
        },
        'A',
        "NÇS 150.000 ₺'den 120.000 ₺'ye düşmüştür: −30.000 ÷ 150.000 = **−%20**. Dönen varlıklar %12,50, KVYK %32 artmıştır.",
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0037': patch(
        "Net satışları 2024'te 1.200.000 ₺, 2025'te 1.500.000 ₺ olan bir işletmenin net çalışma sermayesi 2024'te 200.000 ₺, 2025'te 300.000 ₺'dir. Buna göre net çalışma sermayesi devir hızı nasıl değişmiştir?",
        {
            'A': "6'dan 7,50'ye yükselmiştir.",
            'B': "6'dan 5'e düşmüştür.",
            'C': 'Değişmemiştir.',
            'D': '%25 artmıştır.',
            'E': "5'ten 6'ya yükselmiştir.",
        },
        'B',
        '2024: 1.200.000 ÷ 200.000 = 6; 2025: 1.500.000 ÷ 300.000 = **5**. NÇS (%50) satışlardan (%25) hızlı arttığı için devir hızı düşmüştür.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0038': patch(
        "Net çalışma sermayesi aktif toplamının %30'u olan ve cari oranı 2,50 olan bir işletmede kısa vadeli yabancı kaynakların aktif toplamına oranı yüzde kaçtır?",
        {
            'A': '%12',
            'B': '%30',
            'C': '%50',
            'D': '%75',
            'E': '%20',
        },
        'E',
        'Dönen varlıklar = 2,50 × KVYK; NÇS = 1,50 × KVYK = %30 → KVYK = **%20**, dönen varlıklar %50.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0039': patch(
        'Fiyatların sürekli yükseldiği bir dönemde stoklarını FIFO yöntemiyle değerleyen işletme, ağırlıklı ortalama yöntemi kullanan benzer bir işletmeye göre likidite oranları bakımından nasıl görünür?',
        {
            'A': 'Likidite oranları arasında fark oluşmaz.',
            'B': 'Asit-test oranı daha yüksek, cari oranı daha düşük görünür.',
            'C': 'Nakit oranı daha yüksek görünür.',
            'D': 'Cari oranı daha yüksek görünür; asit-test oranı stok değerlemesinden etkilenmez.',
            'E': 'Her iki oran da daha düşük görünür.',
        },
        'D',
        "FIFO'da dönem sonu stoklar son (yüksek) alış fiyatlarıyla değerlenir; dönen varlıklar ve cari oran yükselir. Asit-test ve nakit oranında stoklar paya girmediğinden değerleme yönteminden etkilenmez.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0040': patch(
        "Dönen varlıkları 200.000 ₺ olup bunun 60.000 ₺'si stok olan bir işletmenin kısa vadeli yabancı kaynakları 80.000 ₺'dir. Buna göre asit-test oranı kaçtır?",
        {
            'A': '3,25',
            'B': '2,50',
            'C': '1,75',
            'D': '0,75',
            'E': '1,40',
        },
        'C',
        "Asit-test = (200.000 − 60.000) ÷ 80.000 = **1,75**. Cari oran 2,50; stokların KVYK'ya oranı 0,75'tir.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0041': patch(
        "Dönen varlıkları 300.000 ₺, kısa vadeli yabancı kaynakları 120.000 ₺, uzun vadeli yabancı kaynakları 100.000 ₺ olan bir işletmenin brüt çalışma sermayesi ve net çalışma sermayesi sırasıyla kaç ₺'dir?",
        {
            'A': '300.000 ve 180.000',
            'B': '180.000 ve 80.000',
            'C': '180.000 ve 300.000',
            'D': '420.000 ve 180.000',
            'E': '300.000 ve 80.000',
        },
        'A',
        'Brüt çalışma sermayesi dönen varlıkların toplamıdır: **300.000 ₺**. Net çalışma sermayesi = dönen varlıklar − KVYK = **180.000 ₺**. Dönen varlıklardan tüm yabancı kaynakların düşülmesi (80.000 ₺) safi çalışma sermayesidir.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0042': patch(
        'Bir işletmenin bilanço verileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Hazır değerler | 10.000 |\n| Menkul kıymetler | 15.000 |\n| Kısa vadeli ticari alacaklar | 95.000 |\n| Stoklar | 100.000 |\n| Kısa vadeli yabancı kaynaklar | 200.000 |\n\nBuna göre stok bağımlılık oranı kaçtır?',
        {
            'A': '0,80',
            'B': '1,75',
            'C': '1,05',
            'D': '0,50',
            'E': '2',
        },
        'A',
        "Stok bağımlılık oranı = [KVYK − (hazır + menkul + kısa vadeli alacak)] ÷ stok = (200.000 − 120.000) ÷ 100.000 = **0,80**. Kısa vadeli borçların %80'lik kısmı stok satılmadan ödenemez.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0043': patch(
        "Cari oranı 2,20 ve asit-test oranı 1,10 olan bir işletmenin stokları 66.000 ₺'dir. Buna göre işletmenin dönen varlıkları kaç ₺'dir?",
        {
            'A': '145.200',
            'B': '60.000',
            'C': '132.000',
            'D': '72.600',
            'E': '66.000',
        },
        'C',
        'Cari − asit-test = stoklar ÷ KVYK → 1,10 = 66.000 ÷ KVYK → KVYK = 60.000 ₺. Dönen varlıklar = 2,20 × 60.000 = **132.000 ₺**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0044': patch(
        "Bir işletmenin likidite (asit-test) oranı 0,80, nakit oranı 0,30 ve kısa vadeli yabancı kaynakları 150.000 ₺'dir. Stoklar dışındaki dönen varlıklar yalnız hazır değer, menkul kıymet ve ticari alacaklardan oluştuğuna göre ticari alacaklar kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '120.000',
            'C': '75.000',
            'D': '165.000',
            'E': '45.000',
        },
        'C',
        'Asit-test payı = 0,80 × 150.000 = 120.000 ₺; nakit oranı payı = 0,30 × 150.000 = 45.000 ₺. Ticari alacaklar = 120.000 − 45.000 = **75.000 ₺**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0045': patch(
        "Brüt çalışma sermayesi 150.000 ₺ ve cari oranı 2,50 olan bir işletmenin hazır değerleri 9.000 ₺, menkul kıymetleri 15.000 ₺'dir. Buna göre nakit oranı kaçtır?",
        {
            'A': '0,40',
            'B': '0,60',
            'C': '0,27',
            'D': '2,10',
            'E': '0,16',
        },
        'A',
        'Brüt çalışma sermayesi dönen varlıklardır; KVYK = 150.000 ÷ 2,50 = 60.000 ₺. Nakit oranı = 24.000 ÷ 60.000 = **0,40**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0046': patch(
        "Dönen varlıkları 240.000 ₺, kısa vadeli yabancı kaynakları 160.000 ₺ olan bir işletme cari oranını 2'ye çıkarmak için kasadaki nakitle kısa vadeli borç ödemek istemektedir. Kaç ₺ ödeme yapmalıdır?",
        {
            'A': '60.000',
            'B': '120.000',
            'C': '160.000',
            'D': '80.000',
            'E': '40.000',
        },
        'D',
        "(240.000 − x) ÷ (160.000 − x) = 2 → 240.000 − x = 320.000 − 2x → x = **80.000 ₺**. Kontrol: 160.000 ÷ 80.000 = 2. Oran 1'in üzerindeyken eşit tutarda pay ve payda azalışı oranı yükseltir.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0047': patch(
        "Dönen varlıkları 240.000 ₺, kısa vadeli yabancı kaynakları 200.000 ₺ olan bir işletme cari oranını 1,50'ye çıkarmak için uzun vadeli kredi kullanarak kasaya nakit sağlayacaktır. Gereken kredi tutarı kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '40.000',
            'C': '300.000',
            'D': '80.000',
            'E': '100.000',
        },
        'A',
        '(240.000 + x) ÷ 200.000 = 1,50 → 240.000 + x = 300.000 → x = **60.000 ₺**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0048': patch(
        "Kısa vadeli yabancı kaynaklar toplamı 30.000 ₺ olan bir işletmenin cari oranı 1,60 ve duran varlıkların devamlı sermayeye oranı 0,75'tir. Buna göre duran varlıklar kaç ₺'dir?",
        {
            'A': '18.000',
            'B': '72.000',
            'C': '54.000',
            'D': '22.500',
            'E': '48.000',
        },
        'C',
        'Dönen varlıklar = 48.000 ₺, NÇS = 18.000 ₺. NÇS = devamlı sermaye × (1 − 0,75) → devamlı sermaye = 72.000 ₺. Duran varlıklar = 0,75 × 72.000 = **54.000 ₺**.',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0049': patch(
        "Bir işletmede kısa vadeli yabancı kaynakların pasif toplamına oranı %20, duran varlıkların aktif toplamına oranı %56'dır. Buna göre cari oran kaçtır?",
        {
            'A': '1,25',
            'B': '0,44',
            'C': '2,80',
            'D': '2,20',
            'E': '0,70',
        },
        'D',
        "Dönen varlıklar aktifin %44'ü; KVYK %20. Cari oran = 44 ÷ 20 = **2,20**. Devamlı sermaye %80, duran varlıklar %56 → NÇS aktifin %24'üdür.",
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0050': patch(
        'Bir işletmenin bilançosuna ait bilgiler şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Dönen varlıklar | 120.000 |\n| Duran varlıklar | 160.000 |\n| Uzun vadeli yabancı kaynaklar | 60.000 |\n| Özkaynaklar | 140.000 |\n\nKısa vadeli yabancı kaynaklar verilmediğine göre işletmenin cari oranı ve net çalışma sermayesi sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
        {
            'A': '0,86 ve −20.000',
            'B': '1,50 ve 40.000',
            'C': '0,60 ve −80.000',
            'D': '2 ve 40.000',
            'E': '1,50 ve 80.000',
        },
        'B',
        'KVYK = aktif − UVYK − özkaynak = 280.000 − 60.000 − 140.000 = 80.000 ₺. Cari = 120.000 ÷ 80.000 = **1,50**; NÇS = **40.000 ₺** (= devamlı sermaye 200.000 − duran varlıklar 160.000).',
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 3
    '0051': patch(
        'Aşağıdaki işlemlerden hangisi asit-test oranını değiştirmez?',
        {
            'A': 'Kısa vadeli borçların kasadaki nakitle ödenmesi',
            'B': 'Stokların bir kısmının maliyet bedeline peşin satılması',
            'C': 'Kasadaki nakitle ticari mal satın alınması',
            'D': 'Kısa vadeli kredi ile ticari mal satın alınması',
            'E': 'Ticari alacakların bir kısmının tahsil edilmesi',
        },
        'E',
        'Alacak tahsilinde alacak azalır, nakit artar; ikisi de asit-test payındadır. Nakitle mal almak payı azaltır (nakit stoka döner), stok satışı payı artırır, kredili mal alımı paydayı artırır, borç ödemesi hem payı hem paydayı değiştirir.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0052': patch(
        "Dönen varlıkları 180.000 ₺, kısa vadeli yabancı kaynakları 90.000 ₺ olan bir işletmede uzun vadeli banka kredisinin gelecek yıl ödenecek 30.000 ₺'lik taksiti kısa vadeli borçlara aktarılmıştır. Buna göre cari oran nasıl değişir?",
        {
            'A': "2'den 1,50'ye düşer ve net çalışma sermayesi değişmez.",
            'B': 'Değişmez; net çalışma sermayesi azalır.',
            'C': "2'den 2,50'ye yükselir.",
            'D': "2'den 1,67'ye düşer.",
            'E': "2'den 1,50'ye düşer.",
        },
        'E',
        "Taksit aktarımı KVYK'yı 120.000 ₺'ye çıkarır: cari oran 180.000 ÷ 120.000 = **1,50**. Net çalışma sermayesi de 90.000 ₺'den 60.000 ₺'ye düşer.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0053': patch(
        "Dönen varlıkları 300.000 ₺, kısa vadeli yabancı kaynakları 120.000 ₺ ve uzun vadeli yabancı kaynakları 100.000 ₺ olan bir işletmenin safi (öz) çalışma sermayesi kaç ₺'dir?",
        {
            'A': '180.000',
            'B': '80.000',
            'C': '−20.000',
            'D': '200.000',
            'E': '300.000',
        },
        'B',
        "Safi çalışma sermayesi dönen varlıklardan toplam yabancı kaynakların düşülmesiyle bulunur: 300.000 − 220.000 = **80.000 ₺**; dönen varlıkların özkaynakla finanse edilen kısmını gösterir. Net çalışma sermayesi 180.000 ₺'dir.",
        'Mali analiz - çalışma sermayesi',
    ),
    # düzey 2
    '0054': patch(
        'Stok bağımlılık oranının yüksek olması aşağıdakilerden hangisini gösterir?',
        {
            'A': 'İşletmenin stoklarının dönen varlıklar içinde önemsiz olduğunu',
            'B': 'Özkaynakların stok yatırımını finanse ettiğini',
            'C': 'Kısa vadeli borçların hazır değerlerle karşılanabildiğini',
            'D': 'Stokların hızlı satıldığını ve devir hızının yüksek olduğunu',
            'E': 'Kısa vadeli borçların ödenmesinin büyük ölçüde stokların satışına bağlı olduğunu',
        },
        'E',
        'Stok bağımlılık oranı, stok dışındaki likit varlıklarla ödenemeyen kısa vadeli borçların stoklara oranıdır; yükseldikçe borç ödemesi stok satışına daha çok bağımlı hâle gelir.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletmenin dönen varlıkları 250.000 ₺ (stoklar 100.000 ₺, hazır değerler 15.000 ₺, menkul kıymetler 10.000 ₺), kısa vadeli yabancı kaynakları 125.000 ₺'dir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Nakit oranı 0,12'dir.",
            'B': "Asit-test oranı 1,20'dir.",
            'C': 'Stoklar kısa vadeli yabancı kaynakların 0,8 katıdır.',
            'D': "Cari oran 2'dir.",
            'E': "Net çalışma sermayesi 125.000 ₺'dir.",
        },
        'A',
        "Nakit oranı = (15.000 + 10.000) ÷ 125.000 = 0,20'dir; 0,12 yalnız hazır değerleri almaktır. Cari 2, asit-test 150.000 ÷ 125.000 = 1,20, NÇS 125.000 ₺, stok ÷ KVYK = 0,80 doğrudur.",
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0056': patch(
        "2024'te cari oranı 2 ve asit-test oranı 1,20 olan bir işletmenin 2025'te cari oranı 2,50, asit-test oranı 1'dir. Buna göre stokların dönen varlıklar içindeki payı nasıl değişmiştir?",
        {
            'A': "%60'tan %40'a düşmüştür.",
            'B': "%40'tan %60'a yükselmiştir.",
            'C': 'Değişmemiştir.',
            'D': "%40'tan %50'ye yükselmiştir.",
            'E': "%80'den %150'ye yükselmiştir.",
        },
        'B',
        'Stok payı = (cari − asit) ÷ cari. 2024: 0,80 ÷ 2 = %40; 2025: 1,50 ÷ 2,50 = **%60**. Cari oranın yükselmesi stoklara bağlıdır.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0057': patch(
        "2024'te cari oranı 1,60 olan bir işletmenin 2025'te dönen varlıkları %25, kısa vadeli yabancı kaynakları %60 artmıştır. Buna göre 2025 yılı cari oranı kaçtır?",
        {
            'A': '1,00',
            'B': '1,25',
            'C': '1,60',
            'D': '2,05',
            'E': '2,00',
        },
        'B',
        'Cari oran = 1,60 × 1,25 ÷ 1,60 = **1,25**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0058': patch(
        'Brüt çalışma sermayesinin yarısı stoklardan oluşan ve cari oranı 2 olan bir işletmenin asit-test oranı kaçtır?',
        {
            'A': '0,50',
            'B': '1,50',
            'C': '4',
            'D': '2',
            'E': '1',
        },
        'E',
        'Asit-test = cari × (1 − stok payı) = 2 × 0,50 = **1**.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0059': patch(
        'Kısa vadeli banka kredisinin vadesi uzatılarak uzun vadeli krediye dönüştürülmesi (yeniden yapılandırma) likidite oranlarını nasıl etkiler?',
        {
            'A': 'KVYK arttığından likidite oranları düşer.',
            'B': 'Net çalışma sermayesi değişir, oranlar aynı kalır.',
            'C': 'Dönen varlıklar arttığından cari oran yükselir, asit-test değişmez.',
            'D': 'Likidite oranları değişmez, borç yapısı değişir.',
            'E': 'KVYK azaldığından cari, asit-test ve nakit oranı yükselir.',
        },
        'E',
        'Borcun vadesi uzayınca KVYK azalır, dönen varlıklar değişmez; paydası KVYK olan bütün likidite oranları yükselir ve net çalışma sermayesi artar.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 3
    '0060': patch(
        'Bir işletme dönem sonunda tahsili şüpheli hâle gelen ticari alacakları için karşılık ayırmıştır. Bu işlemin likidite oranlarına etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Cari oran ve nakit oranı düşer; asit-test oranı değişmez.',
            'B': 'Nakit oranı düşer, diğerleri değişmez.',
            'C': 'Cari oran düşer, asit-test oranı yükselir.',
            'D': 'Cari oran ve asit-test oranı düşer; nakit oranı değişmez.',
            'E': 'Likidite oranları değişmez, borç yapısı değişir.',
        },
        'D',
        'Karşılık, alacakların net tutarını azaltır: dönen varlıklar ve stok dışı likit varlıklar düşer; cari ve asit-test oranı azalır. Hazır değer ve menkul kıymetler etkilenmediğinden nakit oranı aynı kalır.',
        'Mali analiz - likidite oranları',
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
    print(f"1 paket / {len(PATCHES)} soru ('Likidite Oranlari ve Calisma Sermayesi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
