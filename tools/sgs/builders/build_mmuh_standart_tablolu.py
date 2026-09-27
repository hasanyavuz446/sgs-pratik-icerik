#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Standart Maliyet — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Maliyet muhasebesi tablolu tur. Gercek sinavin 18 standart maliyet sorusu tersine hesap (fiili ucret, uretim miktari, standart gider), 710-713/720-723/730-734 kapanis kayitlari, GUG farklari ve farklarin 151/152/620'ye dagitimini soruyor; eski paketin yarisi formul ezberiydi. 26 soru korundu (lehte/aleyhte -> sinavin olumlu/olumsuz terimi; mutlak ifadeli celdiriciler yenilendi); 34 yeni soru, her biri kendi verisiyle: DIMM toplam/fiyat/miktar farki, dakika-saat donusumlu sure farki, fiili ucret/uretim miktari/standart fiyat/fiili sure/birim standart sure tersine sorulari, GUG toplam ve uclu analiz (butce, verimlilik, kapasite), eksik farklar tablosu, DIMM/DIG/GUG kapanis kayitlari, farklarin bakiyeler oraninda dagitimi, yari mamul esdegeriyle standart sure, standart maliyet karti. Tutarlar Fraction ile hesaplandi; her veri setinde fark toplamlari assert edildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Maliyet muhasebesi - standart maliyet sistemi ve fark analizi · Tekduzen Hesap Plani 7/A
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliyet_muhasebesi/standart_maliyet.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (tablolu çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "mmuh-standart-gen-"


def patch(stem, options, answer, solution, ref='Maliyet muhasebesi - standart maliyet'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Aşağıdakilerden hangisi standart maliyet sisteminin temel amaçlarından biri DEĞİLDİR?',
        {
            'A': 'Bütçeleme ve planlamaya temel oluşturmak',
            'B': 'Performans değerlendirme ve sorumluluk belirleme',
            'C': 'Sapmaları saptayıp düzeltici önlem almak',
            'D': 'Satış hasılatını doğrudan artırmak',
            'E': 'Maliyet kontrolü sağlamak',
        },
        'D',
        'Standart maliyet; maliyet kontrolü, bütçeleme, performans değerlendirme ve sapma analizi amaçlarına hizmet eder. **Satış hasılatını doğrudan artırmak** standart maliyetin amacı değildir.',
        'Maliyet muhasebesi - standart maliyet amaçları',
    ),
    # düzey 2
    '0002': patch(
        'Bir mobilya atölyesinde mamul başına standart malzeme tüketimi 5 kg, standart alış fiyatı kg başına 10 ₺ olarak belirlenmiştir. Ay içinde 1.000 birim üretilirken depodan 5.200 kg malzeme çekilmiş; tedarikçi faturasında kg fiyatı 11 ₺ görünmektedir. Malzemenin birim fiyatındaki farklılıktan doğan sapma ne kadardır ve yönü nedir?',
        {
            'A': '5.000 ₺ olumsuz',
            'B': '5.200 ₺ olumsuz',
            'C': '2.000 ₺ olumsuz',
            'D': '5.200 ₺ olumlu',
            'E': '7.200 ₺ olumsuz',
        },
        'B',
        'Fiyat sapması = (fiili fiyat − standart fiyat) × **fiili miktar** = (11 − 10) × 5.200 = **5.200 ₺ olumsuz**. Fiyat sapmasında standart miktar değil fiili miktar kullanılır; standart miktarla (5.000 kg) hesaplamak 5.000 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0003': patch(
        'Standart maliyet ve sapma ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Standart maliyet olması gereken (hedef) maliyettir.\n\nII. Sapma = fiili maliyet − standart maliyet.\n\nIII. Fiili maliyet standart maliyetten büyükse sapma olumludur.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        "**III yanlıştır:** Fiili maliyet standart maliyetten **büyükse** (fiili > standart) fazladan maliyet oluştuğundan sapma **olumsuz**'dur; olumlu değildir. **I** standart maliyet hedef maliyettir; **II** sapma = fiili − standart. Doğru cevap **I ve II**.",
        'Maliyet muhasebesi - standart maliyet',
    ),
    # düzey 2
    '0004': patch(
        'DİMM miktar (kullanım) sapmasından genellikle hangi bölüm sorumlu tutulur?',
        {
            'A': 'Pazarlama bölümü',
            'B': 'Finansman bölümü',
            'C': 'Hukuk bölümü',
            'D': 'Satın alma bölümü',
            'E': 'Üretim bölümü',
        },
        'E',
        'DİMM **miktar (kullanım) sapması** malzemenin üretimde ne kadar kullanıldığıyla ilgili olduğundan genellikle **üretim bölümünün** sorumluluğundadır (fire, verimsizlik vb.).',
        'Maliyet muhasebesi - miktar sapması sorumluluğu',
    ),
    # düzey 2
    '0005': patch(
        "Bir işletmede dönemde 1.000 birim üretilmiş (birim standart DİMM 4 kg, standart fiyat 15 ₺/kg) ve fiilen 4.200 kg malzeme kullanılmıştır. DİMM fiyat sapması 4.200 ₺ olumsuz olarak hesaplandığına göre malzemenin fiili alış fiyatı kaç ₺/kg'dır?",
        {
            'A': '15',
            'B': '16,05',
            'C': '16',
            'D': '17',
            'E': '14',
        },
        'C',
        'Fiyat sapması = (fiili fiyat − standart fiyat) × fiili miktar. Buradan fiili fiyat = standart fiyat + (sapma ÷ fiili miktar) = 15 + (4.200 ÷ 4.200) = 15 + 1 = **16 ₺/kg**. Sapma olumsuz olduğundan fiili fiyat standardın üzerindedir.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme 1.200 birim mamul üretmiştir; birim başına standart direkt işçilik süresi 3 saat ve standart saat ücreti 25 ₺'dir. Dönemde fiilen 3.500 saat çalışılmıştır. Direkt işçilik SÜRE (verimlilik) sapması ne kadardır ve yönü nedir?",
        {
            'A': '2.600 ₺ olumlu',
            'B': '2.500 ₺ olumsuz',
            'C': '100 ₺ olumlu',
            'D': '2.500 ₺ olumlu',
            'E': '3.500 ₺ olumlu',
        },
        'D',
        'Standart süre = 1.200 × 3 = 3.600 saat. Süre sapması = (3.500 − 3.600) × standart ücret 25 = −2.500 ₺, yani **2.500 ₺ olumlu** (standarttan 100 saat az çalışılmış). Fiili ücretle (26 ₺) hesaplamak 2.600 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0007': patch(
        'DİG süre (verimlilik) sapmasından genellikle hangi bölüm sorumlu tutulur?',
        {
            'A': 'Satın alma (tedarik) bölümü sorumludur',
            'B': 'Pazarlama ve satış bölümü sorumludur',
            'C': 'Üretim bölümü (işçilik verimliliği)',
            'D': 'Finansman (fon yönetimi) birimi',
            'E': 'Genel muhasebe ve raporlama birimi',
        },
        'C',
        'DİG **süre (verimlilik) sapması** işçilerin bir mamulü ne kadar sürede ürettiğiyle ilgili olduğundan genellikle **üretim bölümünün** sorumluluğundadır.',
        'Maliyet muhasebesi - süre sapması sorumluluğu',
    ),
    # düzey 2
    '0008': patch(
        'Standart saat ücreti 25 ₺, fiili saat ücreti 24 ₺, fiili süre 2.900 saattir. DİG ücret sapması ne kadardır ve yönü nedir?',
        {
            'A': '2.900 ₺ olumlu',
            'B': 'Sapma yoktur',
            'C': '2.500 ₺ olumlu',
            'D': '2.900 ₺ olumsuz',
            'E': '100 ₺ olumsuz',
        },
        'A',
        'Ücret sapması = (24 − 25) × 2.900 = (−1) × 2.900 = −2.900 ₺ → **2.900 ₺ olumlu** (standarttan düşük ücret ödenmiş).',
        'Maliyet muhasebesi - DİG ücret sapması',
    ),
    # düzey 2
    '0009': patch(
        'Bir üründe standart direkt işçilik 4 saat/birim ve standart ücret 30 ₺/saat olarak belirlenmiştir. Dönemde 1.000 birim üretilmiş; fiilen 4.200 saat çalışılmış ve saat başına 28 ₺ ödenmiştir. Toplam (net) direkt işçilik sapması ne kadardır ve yönü nedir?',
        {
            'A': '200 ₺ olumlu',
            'B': '8.400 ₺ olumlu',
            'C': '6.000 ₺ olumsuz',
            'D': '2.400 ₺ olumsuz',
            'E': '2.400 ₺ olumlu',
        },
        'E',
        'Standart DİG = 1.000 × 4 × 30 = 120.000 ₺; fiili DİG = 4.200 × 28 = 117.600 ₺. Toplam sapma = 117.600 − 120.000 = **2.400 ₺ olumlu**. (Kontrol: ücret sapması (28 − 30) × 4.200 = 8.400 ₺ olumlu; süre sapması (4.200 − 4.000) × 30 = 6.000 ₺ olumsuz; net 2.400 ₺ olumlu.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 3
    '0010': patch(
        'Standart maliyet sistemini uygulayan bir işletmenin standart maliyet kartına göre bir birim mamul için 4 kg direkt ilk madde kullanılması ve bir birim mamulün direkt ilk madde giderinin 480 ₺ olması gerekmektedir. Dönemde 61.500 kg direkt ilk madde kullanılarak 15.000 birim mamul üretilmiş ve direkt ilk madde gideri toplam 7.564.500 ₺ olarak gerçekleşmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Direkt ilk maddenin fiili birim fiyatı 123 ₺/kg olarak gerçekleşmiştir.',
            'B': 'Fiyat farkı standart miktar üzerinden hesaplanır ve 180.000 ₺ olumsuzdur.',
            'C': "Fiili üretim için standart direkt ilk madde miktarı 60.000 kg'dır.",
            'D': 'Direkt ilk madde miktar farkı 180.000 ₺ olumsuzdur.',
            'E': "Mamullere yüklenmesi gereken standart gider 7.200.000 ₺'dir.",
        },
        'B',
        'Fiyat farkı **fiili miktar** üzerinden hesaplanır: (123 − 120) × 61.500 = 184.500 ₺ olumsuz; standart miktarla bulunan 180.000 ₺ yanlıştır. Diğerleri doğrudur: standart miktar 15.000 × 4 = 60.000 kg; miktar farkı (61.500 − 60.000) × 120 = 180.000 ₺ olumsuz; fiili fiyat 7.564.500 ÷ 61.500 = 123 ₺; standart gider 60.000 × 120 = 7.200.000 ₺.',
        'Maliyet muhasebesi - standart maliyet (DİMM farkları)',
    ),
    # düzey 3
    '0011': patch(
        "Standart maliyet sistemini uygulayan bir işletmede direkt işçilik standartları şöyledir:\n\n| Standart | Değer |\n|---|---|\n| Standart direkt işçilik süresi | 45 dakika/birim |\n| Standart direkt işçilik ücreti | 16 ₺/saat |\n\nDönemde üretilen 8.000 birim için gerçekleşen direkt işçilik süresi 372.000 dakika, gerçekleşen saat ücreti 17 ₺'dir. Buna göre direkt işçilik süre (zaman) farkı aşağıdakilerden hangisidir?",
        {
            'A': '3.400 ₺ olumsuz',
            'B': '6.200 ₺ olumsuz',
            'C': '3.200 ₺ olumsuz',
            'D': '192.000 ₺ olumsuz',
            'E': '3.200 ₺ olumlu',
        },
        'C',
        'Süreler saate çevrilir: standart 8.000 × 45 dk = 360.000 dk = 6.000 saat; fiili 372.000 dk = 6.200 saat. Süre farkı = (6.200 − 6.000) × standart ücret 16 = **3.200 ₺ olumsuz**. Dakikayı saate çevirmeden saat ücretiyle çarpmak 192.000 ₺ gibi anlamsız bir sonuç verir.',
        'Maliyet muhasebesi - standart maliyet (DİG süre farkı)',
    ),
    # düzey 3
    '0012': patch(
        'Standart maliyet yöntemini uygulayan bir işletme bir adet mamul için standart olarak 6 direkt işçilik saati (DİS) çalışılması ve DİS ücretinin 30 ₺ olması gerektiğini belirlemiştir. Dönemde üretilen 20.000 adet mamul için 126.000 DİS harcanmış ve 252.000 ₺ olumsuz direkt işçilik ücret farkı ortaya çıkmıştır. Buna göre direkt işçilik toplam farkı aşağıdakilerden hangisidir?',
        {
            'A': '180.000 ₺ olumsuz',
            'B': '72.000 ₺ olumsuz',
            'C': '444.000 ₺ olumsuz',
            'D': '432.000 ₺ olumlu',
            'E': '432.000 ₺ olumsuz',
        },
        'E',
        'Standart süre = 20.000 × 6 = 120.000 DİS. Süre farkı = (126.000 − 120.000) × 30 = 180.000 ₺ olumsuz. Toplam = ücret farkı 252.000 + süre farkı 180.000 = **432.000 ₺ olumsuz**. Kontrol: fiili 126.000 × 32 = 4.032.000 ₺ − standart 3.600.000 ₺.',
        'Maliyet muhasebesi - standart maliyet (DİG farkları)',
    ),
    # düzey 3
    '0013': patch(
        'Genel üretim giderlerini mamullere direkt işçilik saati (DİS) esasına göre yükleyen ve standart maliyet sistemini uygulayan bir işletmenin bilgileri şöyledir:\n\n| Bilgi | Değer |\n|---|---|\n| Birim başına standart DİS | 1,5 saat |\n| GÜG yükleme oranı | 40 ₺/DİS |\n| Dönemde üretilen | 2.000 birim |\n| Gerçekleşen DİS | 3.100 saat |\n| Fiili genel üretim giderleri | 118.000 ₺ |\n\nBuna göre genel üretim giderleri toplam farkı aşağıdakilerden hangisidir?',
        {
            'A': '2.000 ₺ olumsuz',
            'B': '2.000 ₺ olumlu',
            'C': '6.000 ₺ olumsuz',
            'D': '4.000 ₺ olumsuz',
            'E': '6.000 ₺ olumlu',
        },
        'B',
        'Mamullere yüklenen (standart) GÜG = standart süre × oran = (2.000 × 1,5 = 3.000 DİS) × 40 = 120.000 ₺. Toplam fark = fiili 118.000 − 120.000 = **2.000 ₺ olumlu**. Fiili DİS ile (124.000 ₺) karşılaştırmak yanlıştır; yükleme fiili üretimin standart süresiyle yapılır.',
        'Maliyet muhasebesi - standart maliyet (GÜG farkı)',
    ),
    # düzey 3
    '0014': patch(
        'Standart maliyet sistemini kullanan bir üretim işletmesinin genel üretim giderlerine ilişkin bütçe ve dönem verileri aşağıda ayrı ayrı gösterilmiştir:\n\n| Bütçe verisi | Tutar |\n|---|---|\n| Normal kapasite | 8.000 DİS |\n| Sabit GÜG | 96.000 ₺ |\n| Değişken GÜG | 8 ₺/DİS |\n| Standart süre | 2 DİS/birim |\n\n| Dönem verisi | Tutar |\n|---|---|\n| Üretim | 4.100 birim |\n| Fiili çalışma | 7.900 DİS |\n| Fiili GÜG | 162.000 ₺ |\n\nİşletme GÜG farklarını bütçe, verimlilik ve kapasite farkı olarak üçe ayırmakta; verimlilik farkını standart yükleme oranıyla, bütçe farkını fiili çalışma saatine göre esnek bütçeyle hesaplamaktadır. Buna göre GÜG verimlilik farkı ne kadardır?',
        {
            'A': '6.000 ₺ olumsuz',
            'B': '2.400 ₺ olumlu',
            'C': '6.000 ₺ olumlu',
            'D': '3.600 ₺ olumlu',
            'E': '2.000 ₺ olumsuz',
        },
        'C',
        'Standart süre = 4.100 × 2 = 8.200 DİS; standart oran 12 + 8 = 20 ₺/DİS. Verimlilik farkı = (fiili 7.900 − standart 8.200) × 20 = **6.000 ₺ olumlu**. Fiili süre standarttan 300 saat az olduğundan işçilik verimli çalışmış, fark olumlu çıkmıştır.',
        'Maliyet muhasebesi - standart maliyet (GÜG verimlilik farkı)',
    ),
    # düzey 3
    '0015': patch(
        "Standart maliyet yöntemini uygulayan bir işletmenin dönem sonu kapanış kaydında 721 Direkt İşçilik Giderleri Yansıtma hesabının tutarı 640.000 ₺'dir. 722 Direkt İşçilik Ücret Farkları hesabına 24.000 ₺ alacak, 723 Direkt İşçilik Süre Farkları hesabına 56.000 ₺ borç kaydı yapılmıştır. Buna göre 720 Direkt İşçilik Giderleri hesabının kapanış kaydındaki tutarı kaç ₺'dir?",
        {
            'A': '672.000',
            'B': '696.000',
            'C': '608.000',
            'D': '720.000',
            'E': '616.000',
        },
        'A',
        'Kapanış kaydında borç ve alacak eşittir. Borç: 721 640.000 + 723 56.000 = 696.000 ₺. Alacak: 720 x + 722 24.000. x = 696.000 − 24.000 = **672.000 ₺** (fiili direkt işçilik gideri). Süre farkı olumsuz (borç), ücret farkı olumlu (alacak).',
        'Maliyet muhasebesi - standart maliyet (kapanış kaydı)',
    ),
    # düzey 3
    '0016': patch(
        "Standart maliyet sistemini uygulayan bir işletmenin direkt işçilik farklarının toplamı 80.000 ₺ olumsuzdur. Dönem sonunda 151 Yarı Mamuller – Üretim hesabının borç bakiyesi 60.000 ₺, 152 Mamuller hesabının borç bakiyesi 140.000 ₺, 620 Satılan Mamuller Maliyeti hesabının borç bakiyesi 600.000 ₺'dir. Fark önemli tutarda olduğundan bu hesapların bakiyeleri oranında dağıtılacaktır. Buna göre 620 hesabıyla ilgili kayıt aşağıdakilerden hangisidir?",
        {
            'A': '620 hesabı 80.000 ₺ borçlandırılır.',
            'B': '620 hesabı 74.000 ₺ alacaklandırılır.',
            'C': '620 hesabı 60.000 ₺ alacaklandırılır.',
            'D': '620 hesabı 60.000 ₺ borçlandırılır.',
            'E': '620 hesabı 14.000 ₺ borçlandırılır.',
        },
        'D',
        "Dağıtım anahtarı: 60.000 + 140.000 + 600.000 = 800.000 ₺. 620'nin payı = 80.000 × 600.000 ÷ 800.000 = 60.000 ₺. Olumsuz fark maliyeti artırır; fark hesabı alacaklandırılırken 151 (6.000 ₺), 152 (14.000 ₺) ve **620 (60.000 ₺) borçlandırılır**.",
        'Maliyet muhasebesi - standart maliyet (farkların kapatılması)',
    ),
    # düzey 3
    '0017': patch(
        "Tek malzemeden tek işçilik operasyonuyla tek çeşit mamul üreten ve standart maliyet sistemini kullanan bir işletmede dönem sonunda üretim giderlerine ilişkin toplam fark 12.000 ₺ olumsuzdur. Direkt ilk madde ve malzeme toplam farkı 18.000 ₺ olumlu, genel üretim giderleri toplam farkı 21.000 ₺ olumsuzdur. Dönemde 900 direkt işçilik saati çalışılmış; fiili üretim için standart süre 750 saattir. Direkt işçilik ücret farkı sıfır olduğuna göre standart saat ücreti kaç ₺'dir?",
        {
            'A': '80',
            'B': '20',
            'C': '60',
            'D': '12',
            'E': '10',
        },
        'C',
        'Toplam fark = DİMM + DİG + GÜG → 12.000 (olumsuz) = −18.000 + DİG + 21.000 → DİG = 12.000 + 18.000 − 21.000 = 9.000 ₺ olumsuz. Ücret farkı sıfır olduğundan DİG farkının tamamı süre farkıdır: (900 − 750) × SÜ = 9.000 → SÜ = 9.000 ÷ 150 = **60 ₺**.',
        'Maliyet muhasebesi - standart maliyet (tersine)',
    ),
    # düzey 3
    '0018': patch(
        'Bir işletmenin standart maliyet kartı aşağıdaki gibidir:\n\n| Maliyet unsuru | Standart miktar | Standart fiyat |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 2,5 kg | 40 ₺/kg |\n| Direkt işçilik | 1,2 DİS | 50 ₺/DİS |\n| Genel üretim gideri | 1,2 DİS | 35 ₺/DİS |\n\nDönemde 3.000 birim mamul üretilmiş, 3.700 DİS çalışılmış ve fiili genel üretim giderleri 131.000 ₺ olarak gerçekleşmiştir. Buna göre genel üretim giderleri toplam farkı aşağıdakilerden hangisidir?',
        {
            'A': '5.000 ₺ olumlu',
            'B': '1.500 ₺ olumsuz',
            'C': '5.000 ₺ olumsuz',
            'D': '26.000 ₺ olumsuz',
            'E': '3.500 ₺ olumsuz',
        },
        'C',
        'Yüklenen standart GÜG = 3.000 birim × 1,2 DİS × 35 = 126.000 ₺ (birim 42 ₺). Toplam fark = 131.000 − 126.000 = **5.000 ₺ olumsuz**. Fiili DİS ile yüklemek (129.500 ₺) yanlıştır.',
        'Maliyet muhasebesi - standart maliyet (GÜG farkı)',
    ),
    # düzey 3
    '0019': patch(
        "Standart maliyet sistemini uygulayan bir işletmede dönemde 1.500 birim mamul üretilmiştir. Standart süre 0,4 saat/birim, standart saat ücreti 900 ₺'dir. Dönemde toplam 640 saat çalışılmış ve direkt işçilik giderleri 569.600 ₺ olarak gerçekleşmiştir. Buna göre direkt işçilik ücret farkı aşağıdakilerden hangisidir?",
        {
            'A': '29.600 ₺ olumsuz',
            'B': '36.000 ₺ olumsuz',
            'C': '6.000 ₺ olumlu',
            'D': '6.400 ₺ olumsuz',
            'E': '6.400 ₺ olumlu',
        },
        'E',
        'Fiili saat ücreti = 569.600 ÷ 640 = 890 ₺. Ücret farkı = (890 − 900) × fiili süre 640 = **6.400 ₺ olumlu**. Süre farkı (640 − 600) × 900 = 36.000 ₺ olumsuz ayrı bir farktır.',
        'Maliyet muhasebesi - standart maliyet (DİG ücret farkı)',
    ),
    # düzey 3
    '0020': patch(
        'Standart maliyet sistemini kullanan bir işletmede dönemde 2.500 birim mamul üretilmiş, 5.300 saat direkt işçilik çalışılmıştır. Standart saat ücreti 40 ₺ olup 12.000 ₺ olumsuz süre farkı hesaplanmıştır. Buna göre birim başına standart direkt işçilik süresi kaç saattir?',
        {
            'A': '2,12',
            'B': '2,24',
            'C': '2,20',
            'D': '0,12',
            'E': '2',
        },
        'E',
        'Süre farkı = (fiili − standart) × standart ücret → 12.000 = (5.300 − SS) × 40 → 5.300 − SS = 300 → SS = 5.000 saat. Birim başına standart süre = 5.000 ÷ 2.500 = **2** saat. Fark olumsuz olduğundan fiili süre standarttan fazladır.',
        'Maliyet muhasebesi - standart maliyet (tersine)',
    ),
    # düzey 2
    '0021': patch(
        'Sapma analizinin yapılmasının temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Duran varlıkların dönem amortismanını hesaplayarak ilgili gider kayıtlarını oluşturmak',
            'B': 'Fiili ile standart arasındaki farkın nedenini bulup sorumluları belirlemek ve düzeltici önlem almak',
            'C': 'Yasal defterlerdeki fiili maliyet kayıtlarını standart tutarlarla değiştirerek dönem kârını yeniden hesaplamak',
            'D': 'Ürünün gerçek maliyetini müşteriden gizleyip satış fiyatını olduğundan yüksek göstermek',
            'E': 'Standart ile fiili arasındaki farkı vergi matrahından indirerek ödenecek kurumlar vergisini azaltmak',
        },
        'B',
        'Sapma analizi; fiili ile standart arasındaki farkın **nedenini (fiyat/miktar/süre)** bulup **sorumlu bölümü** belirlemeye ve **düzeltici önlem** almaya olanak sağlar.',
        'Maliyet muhasebesi - sapma analizi',
    ),
    # düzey 2
    '0022': patch(
        "Bir mamulün birim başına standart direkt işçilik süresi 2 saat, standart saat ücreti 20 ₺'dir. Dönemde 1.000 birim üretilmiş; fiilen 2.100 saat çalışılmış ve saat başına 22 ₺ ödenmiştir. Direkt işçilik ÜCRET (fiyat) sapması ne kadardır ve yönü nedir?",
        {
            'A': '4.200 ₺ olumsuz',
            'B': '4.200 ₺ olumlu',
            'C': '6.200 ₺ olumsuz',
            'D': '2.000 ₺ olumsuz',
            'E': '4.000 ₺ olumsuz',
        },
        'A',
        'Ücret sapması = (fiili ücret − standart ücret) × **fiili süre** = (22 − 20) × 2.100 = **4.200 ₺ olumsuz**. Standart süre (2.000 saat) ile hesaplamak 4.000 ₺ verir ve yanlıştır; ücret sapmasında fiili süre esas alınır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0023': patch(
        "Bir işletme 2.000 birim mamul üretmiştir; birim başına standart DİMM 3 kg ve standart fiyat 12 ₺/kg'dır. Dönemde fiilen 6.500 kg malzeme kullanılmıştır. DİMM MİKTAR (kullanım) sapması ne kadardır ve yönü nedir?",
        {
            'A': '500 ₺ olumsuz',
            'B': '5.500 ₺ olumsuz',
            'C': '6.500 ₺ olumsuz',
            'D': '6.000 ₺ olumlu',
            'E': '6.000 ₺ olumsuz',
        },
        'E',
        'Standart miktar = 2.000 birim × 3 kg = 6.000 kg. Miktar sapması = (6.500 − 6.000) × standart fiyat 12 = **6.000 ₺ olumsuz** (standarttan 500 kg fazla kullanılmış). Fiili fiyatla (11 ₺) hesaplamak 5.500 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0024': patch(
        "Bir atölyede üretilen 500 birim mamul için malzeme standardı birim başına 2 kg, standart fiyat ise kg başına 20 ₺'dir. Dönem sonu kayıtları 1.100 kg tüketim ve kg başına 18 ₺ alış fiyatı göstermektedir. Malzeme açısından standart maliyet ile fiili maliyet arasındaki NET fark ne kadardır ve yönü nedir?",
        {
            'A': '200 ₺ olumlu',
            'B': '4.200 ₺ olumlu',
            'C': '200 ₺ olumsuz',
            'D': '2.000 ₺ olumsuz',
            'E': '2.200 ₺ olumlu',
        },
        'A',
        'Standart maliyet = 500 × 2 × 20 = 20.000 ₺; fiili maliyet = 1.100 × 18 = 19.800 ₺. Toplam sapma = 19.800 − 20.000 = **200 ₺ olumlu**. (Kontrol: 2.200 ₺ olumlu fiyat + 2.000 ₺ olumsuz miktar sapması = 200 ₺ olumlu.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0025': patch(
        'Toplam DİMM sapmasının fiyat ve miktar sapmalarına ayrılmasının temel yararı aşağıdakilerden hangisidir?',
        {
            'A': 'Mamulün piyasadaki satış fiyatını ve uygulanacak kâr marjını hesaplamaya yönelik bir fiyatlandırma aracı işlevi görür',
            'B': 'Sapmanın fiyattan mı yoksa kullanım (miktar) verimliliğinden mi kaynaklandığını ayırt ederek doğru sorumluya yönelmek',
            'C': 'Fiyat ve miktar farkları ayrıştırılınca toplam fark ortadan kalkar; böylece dönem sonunda fark kapanış kaydı gerekmez',
            'D': 'Ödenecek verginin hesaplanacağı matrahı değiştirir; böylece işletmenin kurumlar vergisi yükünü doğrudan azaltır',
            'E': 'Toplam sapmayı olduğundan daha büyük göstererek dönem kârını yapay biçimde düşürmeyi ve vergiyi ertelemeyi sağlar',
        },
        'B',
        'Toplam sapmayı **fiyat** ve **miktar** bileşenlerine ayırmak, sapmanın alış fiyatından mı yoksa üretimdeki kullanım verimliliğinden mi kaynaklandığını gösterir; böylece doğru bölüm (satın alma / üretim) sorumlu tutulur.',
        'Maliyet muhasebesi - sapma ayrıştırma',
    ),
    # düzey 2
    '0026': patch(
        "Bir işletme 1.200 birim mamul üretmiştir; birim başına standart direkt işçilik süresi 3 saat ve standart saat ücreti 25 ₺'dir. Dönemde fiilen 3.500 saat çalışılmış ve saat başına 26 ₺ ödenmiştir. Toplam (net) direkt işçilik sapması ne kadardır ve yönü nedir?",
        {
            'A': '1.000 ₺ olumlu',
            'B': '1.000 ₺ olumsuz',
            'C': '3.500 ₺ olumsuz',
            'D': '2.500 ₺ olumlu',
            'E': '6.000 ₺ olumsuz',
        },
        'B',
        'Standart DİG = 1.200 × 3 × 25 = 90.000 ₺; fiili DİG = 3.500 × 26 = 91.000 ₺. Toplam sapma = 91.000 − 90.000 = **1.000 ₺ olumsuz**. (Kontrol: 3.500 ₺ olumsuz ücret + 2.500 ₺ olumlu süre sapması = 1.000 ₺ olumsuz.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0027': patch(
        "GÜG 'bütçe (harcama) sapması' ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': 'Fiili GÜG ile fiili faaliyet düzeyine göre bütçelenmesi gereken GÜG arasındaki fark (harcama kontrolü)',
            'B': 'Duran varlıklar için ayrılan dönem amortismanı ile önceki dönemin amortismanı arasında oluşan tutar farkı',
            'C': 'Dönem satış hasılatı ile satılan mamullerin toplam maliyeti arasındaki brüt kâra ilişkin fark',
            'D': 'Dönemde fiilen gerçekleşen üretim miktarı ile başlangıçta bütçelenen üretim miktarı arasındaki hacim farkı',
            'E': 'Yabancı para cinsinden borçların dönem sonu kur değerlemesinden doğan kur farkı tutarı',
        },
        'A',
        'GÜG **bütçe (harcama) sapması**, fiili GÜG ile fiili faaliyet düzeyine göre olması gereken (esnek bütçe) GÜG arasındaki farktır; **harcama kontrolünü** ifade eder.',
        'Maliyet muhasebesi - GÜG bütçe sapması',
    ),
    # düzey 2
    '0028': patch(
        'Dönem sonunda önemsiz (küçük) tutarlı sapmalar genellikle nasıl işleme tabi tutulur?',
        {
            'A': 'Sapma hesaplarında bakiye olarak bırakılır ve izleyen dönemin standartları bu bakiyeye göre düzeltilir',
            'B': 'Özkaynaklar içinde ayrı bir yedek hesabına aktarılarak dönem sonucu dışında bırakılır',
            'C': 'Dönem kârından ortaklara dağıtılacak kâr payı olarak hesaplanıp temettü şeklinde ödenir',
            'D': 'Doğrudan dönemin satılan malın maliyetine/gelir tablosuna aktarılarak kapatılır',
            'E': 'Bir sonraki hesap dönemine olduğu gibi devredilir ve o dönemin sapmalarına eklenir',
        },
        'D',
        'Önemsiz tutarlı sapmalar genellikle dönem sonunda **satılan malın maliyetine / gelir tablosuna** aktarılarak kapatılır. (Önemli tutarlı sapmalar ise stok ve SMM arasında dağıtılabilir.)',
        'Maliyet muhasebesi - sapma kapatma',
    ),
    # düzey 3
    '0029': patch(
        'Standart maliyet sistemini uygulayan bir işletmenin standart maliyet kartına göre bir birim mamul için 4 kg direkt ilk madde kullanılması ve bir birim mamulün direkt ilk madde giderinin 480 ₺ olması gerekmektedir. Dönemde 61.500 kg direkt ilk madde kullanılarak 15.000 birim mamul üretilmiş ve direkt ilk madde gideri toplam 7.564.500 ₺ olarak gerçekleşmiştir. Buna göre işletmenin direkt ilk madde ve malzeme toplam farkı aşağıdakilerden hangisidir?',
        {
            'A': '4.500 ₺ olumsuz',
            'B': '364.500 ₺ olumlu',
            'C': '364.500 ₺ olumsuz',
            'D': '184.500 ₺ olumsuz',
            'E': '180.000 ₺ olumsuz',
        },
        'C',
        'Standart birim fiyat = 480 ÷ 4 = 120 ₺/kg; fiili fiyat = 7.564.500 ÷ 61.500 = 123 ₺/kg. Standart miktar = 15.000 × 4 = 60.000 kg; standart gider = 60.000 × 120 = 7.200.000 ₺. Toplam fark = 7.564.500 − 7.200.000 = **364.500 ₺ olumsuz**. Ayrıştırma: fiyat farkı (123 − 120) × 61.500 = 184.500 ₺ olumsuz; miktar farkı (61.500 − 60.000) × 120 = 180.000 ₺ olumsuz.',
        'Maliyet muhasebesi - standart maliyet (DİMM farkları)',
    ),
    # düzey 3
    '0030': patch(
        "Bir işletmede mamul başına standart direkt işçilik süresi 36 dakika, standart saat ücreti 20 ₺'dir. Dönemde 10.000 birim üretilmiş; toplam 369.000 dakika çalışılmış ve saat başına 19 ₺ ödenmiştir. Buna göre direkt işçilik toplam farkı aşağıdakilerden hangisidir?",
        {
            'A': '6.150 ₺ olumlu',
            'B': '3.150 ₺ olumsuz',
            'C': '9.150 ₺ olumsuz',
            'D': '3.150 ₺ olumlu',
            'E': '3.000 ₺ olumsuz',
        },
        'D',
        'Süreler saate çevrilir: standart 10.000 × 36 dk = 6.000 saat; fiili 369.000 dk = 6.150 saat. Fiili gider 6.150 × 19 = 116.850 ₺; standart gider 6.000 × 20 = 120.000 ₺. Toplam fark = **3.150 ₺ olumlu**. Ayrıştırma: ücret farkı (19 − 20) × 6.150 = 6.150 ₺ olumlu; süre farkı (6.150 − 6.000) × 20 = 3.000 ₺ olumsuz. Farklar ters yönlü olduğu için birbirini kısmen dengeler.',
        'Maliyet muhasebesi - standart maliyet (DİG farkları)',
    ),
    # düzey 3
    '0031': patch(
        'Standart maliyet yöntemini uygulayan bir işletmeye ait bilgiler şöyledir:\n\n| Bilgi | Değer |\n|---|---|\n| Olumsuz direkt ilk madde ve malzeme miktar farkı | 2.000.000 ₺ |\n| Toplam fiili tüketim | 15.000 kg |\n| Standart fiyat | 2.000 ₺/kg |\n| Standart miktar | 8 kg/mamul |\n\nBu bilgilere göre dönemde üretilen mamul miktarı kaç adettir?',
        {
            'A': '1.750',
            'B': '2.000',
            'C': '125',
            'D': '1.875',
            'E': '1.000',
        },
        'A',
        'Miktar farkı = (fiili miktar − standart miktar) × standart fiyat → 2.000.000 = (15.000 − SM) × 2.000 → 15.000 − SM = 1.000 → SM = 14.000 kg. Fark olumsuz olduğu için standart miktar fiiliden azdır. Üretim = 14.000 ÷ 8 = **1.750** adet.',
        'Maliyet muhasebesi - standart maliyet (tersine)',
    ),
    # düzey 3
    '0032': patch(
        "Standart maliyet sistemini uygulayan bir işletme genel üretim giderlerini (GÜG) direkt işçilik saati (DİS) esasına göre yüklemektedir. Döneme ait bilgiler şöyledir:\n\n| Bilgi | Değer |\n|---|---|\n| Normal kapasite | 5.000 DİS |\n| Bütçelenen sabit GÜG | 100.000 ₺ |\n| Değişken GÜG oranı | 12 ₺/DİS |\n| Birim başına standart süre | 2 DİS |\n| Dönemde üretilen | 2.200 birim |\n| Gerçekleşen süre | 4.600 DİS |\n| Fiili GÜG | 158.000 ₺ |\n\nFarklar üçlü analizle incelenmektedir: bütçe farkı fiili DİS'e göre esnek bütçeyle, verimlilik farkı standart GÜG yükleme oranıyla hesaplanmaktadır. Buna göre GÜG bütçe farkı aşağıdakilerden hangisidir?",
        {
            'A': '2.800 ₺ olumlu',
            'B': '17.200 ₺ olumsuz',
            'C': '2.000 ₺ olumlu',
            'D': '5.200 ₺ olumsuz',
            'E': '2.800 ₺ olumsuz',
        },
        'E',
        "Fiili DİS'e göre esnek bütçe = sabit 100.000 + değişken 12 × 4.600 = 155.200 ₺. Bütçe farkı = fiili 158.000 − 155.200 = **2.800 ₺ olumsuz**. Harcamanın, fiilen çalışılan saat için öngörülenden fazla olduğunu gösterir.",
        'Maliyet muhasebesi - standart maliyet (GÜG bütçe farkı)',
    ),
    # düzey 3
    '0033': patch(
        "Standart maliyet sistemini uygulayan bir işletme genel üretim giderlerini (GÜG) direkt işçilik saati (DİS) esasına göre yüklemektedir. Döneme ait bilgiler şöyledir:\n\n| Bilgi | Değer |\n|---|---|\n| Normal kapasite | 5.000 DİS |\n| Bütçelenen sabit GÜG | 100.000 ₺ |\n| Değişken GÜG oranı | 12 ₺/DİS |\n| Birim başına standart süre | 2 DİS |\n| Dönemde üretilen | 2.200 birim |\n| Gerçekleşen süre | 4.600 DİS |\n| Fiili GÜG | 158.000 ₺ |\n\nFarklar üçlü analizle incelenmektedir: bütçe farkı fiili DİS'e göre esnek bütçeyle, verimlilik farkı standart GÜG yükleme oranıyla hesaplanmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Standart GÜG yükleme oranı 32 ₺/DİS'tir.",
            'B': 'GÜG bütçe farkı 5.200 ₺ olumsuzdur.',
            'C': 'GÜG kapasite farkı 8.000 ₺ olumsuzdur.',
            'D': 'GÜG toplam farkı 17.200 ₺ olumsuzdur.',
            'E': "Mamullere yüklenen standart GÜG 140.800 ₺'dir.",
        },
        'B',
        "Bütçe farkı fiili DİS'e göre esnek bütçeyle bulunur: 158.000 − (100.000 + 12 × 4.600) = 2.800 ₺ olumsuz; standart DİS'e göre bütçeyle bulunan 5.200 ₺ yanlıştır. Diğerleri doğrudur: oran 20 + 12 = 32; yüklenen 4.400 × 32 = 140.800 ₺; kapasite farkı 8.000 ₺ olumsuz; toplam 158.000 − 140.800 = 17.200 ₺ olumsuz (= 2.800 + 6.400 + 8.000).",
        'Maliyet muhasebesi - standart maliyet (GÜG farkları)',
    ),
    # düzey 3
    '0034': patch(
        'Standart maliyet sistemini kullanan bir işletmede dönem sonunda fiili ve standart maliyetlerin karşılaştırılması sonucunda toplam fark 4.600 ₺ olumsuz olarak hesaplanmıştır. Farkların bir kısmı aşağıdaki tabloda verilmiştir; negatif değerler olumsuz farkı göstermektedir.\n\n| Fark | DİMM | Direkt işçilik | GÜG |\n|---|---|---|---|\n| Fiyat farkı | −8.000 |  |  |\n| Miktar farkı | 6.000 |  |  |\n| Ücret farkı |  | ? |  |\n| Zaman farkı |  | −7.000 |  |\n| Bütçe farkı |  |  | ? |\n| Verim farkı |  |  | 2.400 |\n| Kapasite farkı |  |  | −2.000 |\n| Toplam |  | −3.500 |  |\n\nBuna göre ücret farkı ve bütçe farkı sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
        {
            'A': '3.500 ₺ olumlu ve 5.300 ₺ olumlu',
            'B': '3.500 ₺ olumlu ve 500 ₺ olumlu',
            'C': '3.500 ₺ olumsuz ve 500 ₺ olumsuz',
            'D': '3.500 ₺ olumlu ve 900 ₺ olumlu',
            'E': '10.500 ₺ olumsuz ve 500 ₺ olumlu',
        },
        'B',
        'DİG: toplam −3.500 = ücret + zaman (−7.000) → ücret = +3.500, yani **3.500 ₺ olumlu**. DİMM toplamı = −8.000 + 6.000 = −2.000. GÜG toplamı = genel toplam −4.600 − DİMM (−2.000) − DİG (−3.500) = +900. Bütçe = +900 − verim (+2.400) − kapasite (−2.000) = +500, yani **500 ₺ olumlu**.',
        'Maliyet muhasebesi - standart maliyet (farklar tablosu)',
    ),
    # düzey 3
    '0035': patch(
        "Standart maliyet yöntemini uygulayan bir üretim işletmesinin dönemin fiili direkt işçilik giderleri toplamı 900.000 ₺, standart direkt işçilik giderleri toplamı 860.000 ₺'dir. Bu giderlerle ilgili 30.000 ₺ olumlu ücret farkı ve 70.000 ₺ olumsuz süre farkı ortaya çıkmıştır. Buna göre dönem sonunda yapılacak kapanış kaydıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': '721 Direkt İşçilik Giderleri Yansıtma hesabı 860.000 ₺ borçlandırılır.',
            'B': 'Kaydın borç ve alacak toplamı 930.000 ₺ olarak eşitlenir.',
            'C': '723 Direkt İşçilik Süre Farkları hesabı 70.000 ₺ borçlandırılır.',
            'D': '722 Direkt İşçilik Ücret Farkları hesabı 30.000 ₺ borçlandırılır.',
            'E': '720 Direkt İşçilik Giderleri hesabı 900.000 ₺ alacaklandırılır.',
        },
        'D',
        "Olumlu fark kapanış kaydında **alacak** tarafına yazılır; 722'nin 30.000 ₺ borçlandırılması yanlıştır. Doğru kayıt: 721 860.000 B, 723 70.000 B / 720 900.000 A, 722 30.000 A. Borç 930.000 = alacak 930.000 ₺.",
        'Maliyet muhasebesi - standart maliyet (kapanış kaydı)',
    ),
    # düzey 3
    '0036': patch(
        "Standart maliyet sistemini uygulayan bir işletmede dönemde 1.100 adet mamul tamamlanmış, 400 adet yarı mamul direkt işçilik açısından %50 tamamlanmış olarak kalmıştır. Standart süre 0,4 DİS/adet, standart ücret 25 ₺/DİS'tir. Dönemde 530 DİS çalışılmış ve saat başına 24 ₺ ödenmiştir. Buna göre direkt işçilik toplam farkı aşağıdakilerden hangisidir?",
        {
            'A': '280 ₺ olumsuz',
            'B': '2.280 ₺ olumlu',
            'C': '530 ₺ olumlu',
            'D': '280 ₺ olumlu',
            'E': '1.720 ₺ olumsuz',
        },
        'D',
        'Eşdeğer üretim = 1.100 + (400 × %50) = 1.300 adet; standart süre 1.300 × 0,4 = 520 DİS; standart gider 520 × 25 = 13.000 ₺. Fiili gider 530 × 24 = 12.720 ₺. Toplam fark = **280 ₺ olumlu** = ücret farkı 530 ₺ olumlu + süre farkı (530 − 520) × 25 = 250 ₺ olumsuz.',
        'Maliyet muhasebesi - standart maliyet (eşdeğer üretim)',
    ),
    # düzey 2
    '0037': patch(
        "Bir işletmenin standart maliyet kartı aşağıdaki gibidir:\n\n| Maliyet unsuru | Standart miktar | Standart fiyat |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 2,5 kg | 40 ₺/kg |\n| Direkt işçilik | 1,2 DİS | 50 ₺/DİS |\n| Genel üretim gideri | 1,2 DİS | 35 ₺/DİS |\n\nBuna göre bir birim mamulün standart maliyeti kaç ₺'dir?",
        {
            'A': '160',
            'B': '195',
            'C': '202',
            'D': '125',
            'E': '244',
        },
        'C',
        'DİMM 2,5 × 40 = 100 ₺; direkt işçilik 1,2 × 50 = 60 ₺; GÜG 1,2 DİS × 35 = 42 ₺. Birim standart maliyet **202 ₺**. GÜG, yükleme esası olan DİS ile çarpılmadan toplanamaz.',
        'Maliyet muhasebesi - standart maliyet kartı',
    ),
    # düzey 3
    '0038': patch(
        'Standart maliyet sistemini uygulayan bir işletmede standart direkt işçilik saat ücreti 150 ₺/DİS, standart süre 0,8 DİS/adettir. 2.500 adet mamulün üretildiği dönemde 2.100 DİS çalışılmış ve direkt işçilik gideri olarak 310.800 ₺ ödenmiştir. Buna göre direkt işçilik süre farkı ve yönü aşağıdakilerden hangisidir?',
        {
            'A': '15.000 ₺ olumlu',
            'B': '14.800 ₺ olumsuz',
            'C': '15.000 ₺ olumsuz',
            'D': '4.200 ₺ olumlu',
            'E': '10.800 ₺ olumsuz',
        },
        'C',
        'Standart süre = 2.500 × 0,8 = 2.000 DİS. Süre farkı = (2.100 − 2.000) × standart ücret 150 = **15.000 ₺ olumsuz**. Fiili ücret (310.800 ÷ 2.100 = 148 ₺) yalnız ücret farkında kullanılır: (148 − 150) × 2.100 = 4.200 ₺ olumlu.',
        'Maliyet muhasebesi - standart maliyet (DİG süre farkı)',
    ),
    # düzey 3
    '0039': patch(
        "Bir işletmede K mamulünün bir kg'ını üretmek için standart olarak 3 direkt işçilik saati (DİS) harcanacağı ve standart saat ücretinin 20 ₺ olacağı planlanmıştır. Ay içinde üretilen 9.000 kg K mamulü için 28.000 DİS harcanmış, gerçekleşen direkt işçilik gideri 574.000 ₺ olmuştur. Buna göre direkt işçilik süre farkı kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '380.000',
            'C': '34.000',
            'D': '14.000',
            'E': '20.500',
        },
        'A',
        'Standart süre = 9.000 × 3 = 27.000 DİS. Süre farkı = (28.000 − 27.000) × standart ücret 20 = **20.000 ₺** (olumsuz). Fiili ücret 20,50 ₺ yalnız ücret farkında kullanılır (14.000 ₺ olumsuz).',
        'Maliyet muhasebesi - standart maliyet (DİG süre farkı)',
    ),
    # düzey 2
    '0040': patch(
        'Standart maliyet sisteminin muhasebeleştirilmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Olumlu fark veren fark hesapları, gider ve yansıtma hesaplarının kapanış kaydında borçlandırılır.\n\nII. Olumlu fark veren fark hesapları, gider ve yansıtma hesaplarının kapanış kaydında alacaklandırılır.\n\nIII. Olumsuz fark veren fark hesapları, gider ve yansıtma hesaplarının kapanış kaydında borçlandırılır.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'D',
        'Kapanışta yansıtma hesabı standart tutarla borçlandırılır, gider hesabı fiili tutarla alacaklandırılır. Fiili standarttan büyükse (olumsuz fark) eksik kalan borç tarafı fark hesabının **borcuyla** (III doğru), fiili standarttan küçükse (olumlu fark) eksik kalan alacak tarafı fark hesabının **alacağıyla** (II doğru) tamamlanır. **I yanlıştır.** Doğru cevap **II ve III**.',
        'Maliyet muhasebesi - standart maliyet (kapanış kaydı)',
    ),
    # düzey 2
    '0041': patch(
        "Standart maliyet ile 'tahmini maliyet' arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'Her ikisi de geçmiş dönemin fiili kayıtlarından türetilen tarihsel maliyetlerdir; gelecek dönem için hedef veya norm niteliği taşımazlar',
            'B': 'Tahmini maliyet direkt ilk madde için, standart maliyet ise genel üretim giderleri için belirlenen ayrı birer öngörüdür',
            'C': 'Standart maliyet bilimsel/teknik esaslarla belirlenen olması gereken maliyettir; tahmini maliyet ise daha çok geçmiş verilere dayalı bir öngörüdür',
            'D': 'Tahmini maliyet bilimsel ve teknik analizlerle belirlenen olması gereken maliyettir; standart maliyet ise geçmişe dayalı kaba bir öngörüdür',
            'E': 'Standart maliyet dönem sonunda fiili maliyetler kesinleştikten sonra belirlenir; bu nedenle aralarında fark oluşması beklenmez',
        },
        'C',
        '**Standart maliyet** bilimsel/teknik analizle belirlenen **olması gereken** maliyettir (hedef/norm). **Tahmini maliyet** ise genellikle geçmiş verilere dayalı bir **öngörüdür**; kontrol standardı olma niteliği daha zayıftır.',
        'Maliyet muhasebesi - standart maliyet',
    ),
    # düzey 2
    '0042': patch(
        "Standart maliyet ve sapma analizinin 'sorumluluk muhasebesi' ile ilişkisi aşağıdakilerden hangisidir?",
        {
            'A': 'Sapma analizi sadece dönem satış hasılatını ölçmeye yarar; maliyet kontrolü veya bölüm performansı ile herhangi bir ilişkisi bulunmamaktadır',
            'B': 'Her sapma, ilgili bölüm/yöneticinin sorumluluğuyla ilişkilendirilerek performans değerlendirmesine ve hesap verebilirliğe olanak sağlar',
            'C': 'Sapma analizi ödenecek verginin hesaplanmasında kullanılır; bölümlerin performansı veya sorumluluğu ile ilgilenmez',
            'D': 'Sapmalar sorumluluk merkezlerine değil mamullere göre izlenir; bölüm yöneticileri bütçe farkları dışında sorumlu tutulmaz',
            'E': 'Tüm sapmalar genel müdürlüğün sorumluluğunda toplanır; fiyat ve miktar sapmaları ayrı bölümlere yüklenmez',
        },
        'B',
        'Sapma analizi, her sapmayı **sorumlu bölüm/yönetici** ile ilişkilendirir (ör. fiyat sapması satın alma, miktar sapması üretim). Böylece sorumluluk muhasebesi ve performans değerlendirmesi desteklenir.',
        'Maliyet muhasebesi - sorumluluk muhasebesi',
    ),
    # düzey 2
    '0043': patch(
        'DİMM fiyat sapmasından genellikle hangi bölüm sorumlu tutulur?',
        {
            'A': 'Üretim (imalat) bölümü',
            'B': 'Genel muhasebe ve raporlama',
            'C': 'İnsan kaynakları birimi',
            'D': 'Pazarlama ve satış bölümü',
            'E': 'Satın alma (tedarik) bölümü',
        },
        'E',
        'DİMM **fiyat sapması** malzemenin alış fiyatıyla ilgili olduğundan genellikle **satın alma (tedarik) bölümünün** sorumluluğundadır.',
        'Maliyet muhasebesi - fiyat sapması sorumluluğu',
    ),
    # düzey 2
    '0044': patch(
        "Bir imalatçıda mamul başına malzeme standardı 4 kg olup standart fiyat 15 ₺/kg'dır. Dönem boyunca 1.500 birim imal edilmiş, depo kayıtlarına göre 6.300 kg malzeme çıkışı yapılmış ve malzeme kg başına 14 ₺'ye temin edilmiştir. Standart maliyet ile fiili maliyet karşılaştırıldığında ortaya çıkan net sapma ne kadardır ve yönü nedir?",
        {
            'A': '10.800 ₺ olumlu',
            'B': '1.800 ₺ olumlu',
            'C': '6.300 ₺ olumlu',
            'D': '4.500 ₺ olumsuz',
            'E': '1.800 ₺ olumsuz',
        },
        'B',
        'Standart maliyet = 1.500 × 4 × 15 = 90.000 ₺; fiili maliyet = 6.300 × 14 = 88.200 ₺. Toplam sapma = 88.200 − 90.000 = **1.800 ₺ olumlu**. (Kontrol: 6.300 ₺ olumlu fiyat + 4.500 ₺ olumsuz miktar = 1.800 ₺ olumlu.)',
        'Maliyet muhasebesi - standart maliyet ve sapma analizi (çok adımlı)',
    ),
    # düzey 2
    '0045': patch(
        'DİMM sapmaları ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiyat sapması = (fiili fiyat − standart fiyat) × fiili miktar.\n\nII. Miktar sapması = (fiili miktar − standart miktar) × standart fiyat.\n\nIII. Toplam DİMM sapması = fiyat sapması + miktar sapması.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'D',
        'Üçü de doğrudur: **I** fiyat sapması formülü; **II** miktar sapması formülü; **III** toplam = fiyat + miktar. Doğru cevap **I, II ve III**.',
        'Maliyet muhasebesi - DİMM sapması',
    ),
    # düzey 2
    '0046': patch(
        'DİG ücret sapmasından genellikle hangi taraf/bölüm sorumlu tutulur?',
        {
            'A': 'Malzeme alış fiyatını görüşen satın alma (tedarik) bölümü',
            'B': 'Çalışma verimliliğinden sorumlu tutulan üretim ustabaşı',
            'C': 'Ücret politikasını belirleyen insan kaynakları / yönetim',
            'D': 'Mamulü teslim alan nihai müşteri ile bayi ağı',
            'E': 'Ürünün tanıtımını yürüten pazarlama ve satış bölümü',
        },
        'C',
        'DİG **ücret sapması** saat ücreti düzeyiyle ilgili olduğundan genellikle **ücret politikasını belirleyen insan kaynakları/yönetimin** sorumluluğundadır. (Süre/verimlilik sapması ise üretim yönetiminin sorumluluğundadır.)',
        'Maliyet muhasebesi - ücret sapması sorumluluğu',
    ),
    # düzey 2
    '0047': patch(
        "GÜG 'kapasite (hacim) sapması' ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': "Planlanan (normal) kapasite ile fiili kullanılan kapasite farkından doğan, sabit GÜG'ün eksik/fazla yüklenmesine ilişkin sapma",
            'B': 'Dönem kazancı üzerinden hesaplanan vergi ile önceki dönem vergisi arasındaki farkı gösteren bir vergi kalemi',
            'C': 'Satılan mamullerden dönem içinde geri alınanların hasılattan düşülmesiyle ortaya çıkan satış iadesi tutarı',
            'D': 'Malzemenin fiili alış fiyatı ile standart fiyatı arasındaki farktan doğan, ilk madde giderine ait fiyat sapması',
            'E': 'İşçilere ödenen fiili saat ücreti ile bütçelenen standart saat ücreti arasındaki farktan doğan, işçilik giderine ilişkin ücret sapması',
        },
        'A',
        "GÜG **kapasite (hacim) sapması**, planlanan (normal) kapasite ile fiilen kullanılan kapasite arasındaki farktan doğar; özellikle **sabit GÜG'ün** eksik ya da fazla yüklenmesini yansıtır.",
        'Maliyet muhasebesi - GÜG kapasite sapması',
    ),
    # düzey 2
    '0048': patch(
        'Aşağıdakilerden hangisi direkt işçilik sapmalarından biri DEĞİLDİR?',
        {
            'A': 'Süre (zaman/verimlilik) sapması',
            'B': 'Malzeme fiyat sapması',
            'C': 'Toplam DİG sapması bu ikisinin toplamıdır',
            'D': 'Ücret (fiyat) sapması',
            'E': 'Bunların ikisi de direkt işçilik sapmasıdır',
        },
        'B',
        'Direkt işçilik sapmaları **ücret (fiyat)** ve **süre (verimlilik)** sapmalarıdır; toplamları toplam DİG sapmasını verir. **Malzeme fiyat sapması** ise DİMM (malzeme) sapmasıdır, işçilik sapması değildir.',
        'Maliyet muhasebesi - DİG sapmaları',
    ),
    # düzey 2
    '0049': patch(
        'Standart maliyet ve sapma analizi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. DİG toplam sapması = ücret sapması + süre sapması.\n\nII. Fiili maliyet standarttan düşükse sapma olumsuzdur.\n\nIII. GÜG toplam sapması = fiili GÜG − mamullere yüklenen (standart) GÜG.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'E',
        '**II yanlıştır:** Fiili maliyet standarttan DÜŞÜKSE işletme öngörülenden az harcamış demektir; bu OLUMLU sapmadır, olumsuz değildir (olumsuz sapma fiili > standart durumunda oluşur). **I** DİG toplam sapması = ücret sapması + süre sapması ve **III** GÜG toplam sapması = fiili GÜG − yüklenen (standart) GÜG doğrudur. Doğru cevap **I ve III**.',
        'Maliyet muhasebesi - standart maliyet',
    ),
    # düzey 3
    '0050': patch(
        'Standart maliyet sistemini uygulayan bir işletmenin standart maliyet kartına göre bir birim mamul için 4 kg direkt ilk madde kullanılması ve bir birim mamulün direkt ilk madde giderinin 480 ₺ olması gerekmektedir. Dönemde 61.500 kg direkt ilk madde kullanılarak 15.000 birim mamul üretilmiş ve direkt ilk madde gideri toplam 7.564.500 ₺ olarak gerçekleşmiştir. İşletme dönem sonunda 710, 711, 712 ve 713 numaralı hesapları birbirine kapatmaktadır. Buna göre kapanış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma hesabı 7.564.500 ₺ borçlandırılır.',
            'B': '713 Direkt İlk Madde ve Malzeme Miktar Farkı hesabı 180.000 ₺ alacaklandırılır.',
            'C': '711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma hesabı 7.200.000 ₺ alacaklandırılır.',
            'D': '710 Direkt İlk Madde ve Malzeme Giderleri hesabı 7.564.500 ₺ alacaklandırılır.',
            'E': '712 Direkt İlk Madde ve Malzeme Fiyat Farkı hesabı 184.500 ₺ alacaklandırılır.',
        },
        'D',
        "Fiili gider 710'un borcunda, standart gider 711'in alacağında birikir. Kapanışta 711 standart tutarla (7.200.000 ₺) borçlandırılır, 710 fiili tutarla (**7.564.500 ₺**) alacaklandırılır. Olumsuz farklar borç tarafına yazılır: 712 fiyat farkı 184.500 ₺ ve 713 miktar farkı 180.000 ₺ borç. Sağlama: 7.200.000 + 184.500 + 180.000 = 7.564.500 ₺.",
        'Maliyet muhasebesi - standart maliyet (kapanış kaydı)',
    ),
    # düzey 3
    '0051': patch(
        "Standart maliyet yöntemini uygulayan bir işletme bir adet mamul için standart olarak 6 direkt işçilik saati (DİS) çalışılması ve DİS ücretinin 30 ₺ olması gerektiğini belirlemiştir. Dönemde üretilen 20.000 adet mamul için 126.000 DİS harcanmış ve 252.000 ₺ olumsuz direkt işçilik ücret farkı ortaya çıkmıştır. Buna göre dönemde gerçekleşen DİS ücreti kaç ₺'dir?",
        {
            'A': '28',
            'B': '34',
            'C': '32,10',
            'D': '30',
            'E': '32',
        },
        'E',
        'Ücret farkı = (fiili ücret − standart ücret) × **fiili süre**. 252.000 = (x − 30) × 126.000 → x − 30 = 2 → x = **32 ₺**. Fark olumsuz olduğundan fiili ücret standardın üzerindedir; standart süreye (120.000 DİS) bölmek 32,10 ₺ verir ve yanlıştır.',
        'Maliyet muhasebesi - standart maliyet (DİG ücret farkı)',
    ),
    # düzey 3
    '0052': patch(
        "Standart maliyet sistemini kullanan bir işletmede dönemde 2.000 adet mamulün üretimi tamamlanmıştır. Mamul başına standart direkt ilk madde miktarı 6 kg'dır. Dönemde kg'ı 18 ₺'den 13.000 kg direkt ilk madde tüketilmiş ve 20.000 ₺ olumsuz miktar farkı hesaplanmıştır. Buna göre mamullerin tamamı için yüklenmesi gereken standart direkt ilk madde ve malzeme gideri kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '234.000',
            'C': '214.000',
            'D': '216.000',
            'E': '260.000',
        },
        'A',
        'Standart miktar = 2.000 × 6 = 12.000 kg. Miktar farkı (13.000 − 12.000) × SF = 20.000 → SF = 20.000 ÷ 1.000 = 20 ₺/kg. Standart gider = 12.000 kg × 20 = **240.000 ₺**. Fiili fiyat (18 ₺) standart gideri belirlemez.',
        'Maliyet muhasebesi - standart maliyet (tersine)',
    ),
    # düzey 3
    '0053': patch(
        "Bir fabrikada genel üretim giderleri direkt işçilik saati esasına göre mamullere yüklenmektedir. 6.000 DİS olarak belirlenen normal kapasite için sabit GÜG bütçesi 150.000 ₺, değişken GÜG oranı ise saat başına 10 ₺'dir. Mamul başına standart süre 3 DİS'tir. Dönemde 1.500 birim mamul üretilmiş, 4.800 DİS çalışılmış ve 205.000 ₺ fiili genel üretim gideri oluşmuştur. Üçlü analizde bütçe farkı fiili DİS'e göre esnek bütçeyle, verimlilik farkı standart yükleme oranıyla bulunmaktadır. Buna göre kapasite farkının tutarı ve yönü aşağıdakilerden hangisidir?",
        {
            'A': '47.500 ₺ olumsuz',
            'B': '30.000 ₺ olumsuz',
            'C': '30.000 ₺ olumlu',
            'D': '10.500 ₺ olumsuz',
            'E': '37.500 ₺ olumsuz',
        },
        'B',
        'Standart yükleme oranı = sabit oran 150.000 ÷ 6.000 = 25 + değişken 10 = 35 ₺/DİS. Esnek bütçe (fiili DİS) = 150.000 + 10 × 4.800 = 198.000 ₺. Kapasite farkı = 198.000 − (4.800 × 35 = 168.000) = **30.000 ₺ olumsuz**. Aynı sonuç: kullanılmayan kapasite (6.000 − 4.800) × sabit oran 25 = 30.000 ₺.',
        'Maliyet muhasebesi - standart maliyet (GÜG kapasite farkı)',
    ),
    # düzey 3
    '0054': patch(
        "Standart maliyet sistemini uygulayan bir işletme genel üretim giderlerini (GÜG) direkt işçilik saati (DİS) esasına göre yüklemektedir. Döneme ait bilgiler şöyledir:\n\n| Bilgi | Değer |\n|---|---|\n| Normal kapasite | 5.000 DİS |\n| Bütçelenen sabit GÜG | 100.000 ₺ |\n| Değişken GÜG oranı | 12 ₺/DİS |\n| Birim başına standart süre | 2 DİS |\n| Dönemde üretilen | 2.200 birim |\n| Gerçekleşen süre | 4.600 DİS |\n| Fiili GÜG | 158.000 ₺ |\n\nFarklar üçlü analizle incelenmektedir: bütçe farkı fiili DİS'e göre esnek bütçeyle, verimlilik farkı standart GÜG yükleme oranıyla hesaplanmaktadır. Dönem sonunda 730 ve 731 hesapları farklar ayrıştırılarak birbirine kapatılmaktadır. Buna göre kapanış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '731 Genel Üretim Giderleri Yansıtma hesabı 140.800 ₺ borçlandırılır.',
            'B': '733 GÜG Verimlilik Farkları hesabı 6.400 ₺ alacaklandırılır.',
            'C': '734 GÜG Kapasite Farkları hesabı 8.000 ₺ alacaklandırılır.',
            'D': '731 Genel Üretim Giderleri Yansıtma hesabı 158.000 ₺ borçlandırılır.',
            'E': '730 Genel Üretim Giderleri hesabı 140.800 ₺ alacaklandırılır.',
        },
        'A',
        "Yüklenen (standart) GÜG 731'in alacağında birikmiştir; kapanışta **731 140.800 ₺ borçlandırılır**, fiili GÜG'ü taşıyan 730 158.000 ₺ alacaklandırılır. Üç fark da olumsuz olduğundan borç tarafına yazılır: 732 bütçe 2.800 ₺, 733 verimlilik 6.400 ₺, 734 kapasite 8.000 ₺. Sağlama: 140.800 + 2.800 + 6.400 + 8.000 = 158.000 ₺.",
        'Maliyet muhasebesi - standart maliyet (kapanış kaydı)',
    ),
    # düzey 3
    '0055': patch(
        'Aylık raporlama yapan ve standart maliyet yöntemini uygulayan bir işletme direkt işçilik giderleriyle ilgili aşağıdaki kapanış kaydını yapmıştır:\n\n| Hesap | Borç (₺) | Alacak (₺) |\n|---|---|---|\n| 721 Direkt İşçilik Giderleri Yansıtma | 480.000 |  |\n| 722 Direkt İşçilik Ücret Farkları | 36.000 |  |\n| 720 Direkt İşçilik Giderleri |  | 500.000 |\n| 723 Direkt İşçilik Süre Farkları |  | 16.000 |\n\nBuna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fiili direkt işçilik gideri 480.000 ₺ olup toplam fark 20.000 ₺ olumludur.',
            'B': 'Ücret farkı 36.000 ₺ olumlu, süre farkı 16.000 ₺ olumsuzdur.',
            'C': 'Fiili direkt işçilik gideri 500.000 ₺ olup süre farkı 16.000 ₺ olumludur.',
            'D': 'Toplam direkt işçilik farkı 52.000 ₺ olumsuz olarak gerçekleşmiştir.',
            'E': 'Standart direkt işçilik gideri 500.000 ₺ olup ücret farkı 36.000 ₺ olumsuzdur.',
        },
        'C',
        '720 fiili gideri taşır ve kapanışta alacaklandırılır: fiili gider 500.000 ₺. 721 standart gideri (480.000 ₺) gösterir. Olumsuz farklar borç, olumlu farklar alacak tarafına yazılır: 722 ücret farkı 36.000 ₺ olumsuz, 723 süre farkı **16.000 ₺ olumlu**. Toplam fark = 500.000 − 480.000 = 20.000 ₺ olumsuz (= 36.000 − 16.000).',
        'Maliyet muhasebesi - standart maliyet (kapanış kaydı)',
    ),
    # düzey 3
    '0056': patch(
        'Tek mamul üreten bir işletmede dönemde 900 adet mamul tamamlanmış, 300 adet yarı mamul olarak kalmıştır. Yarı mamuller direkt işçilik açısından %40 tamamlanmıştır. Direkt işçiliğe ilişkin veriler şöyledir:\n\n| Veri | Değer |\n|---|---|\n| Standart süre | 0,5 DİS/adet |\n| Standart ücret | 20 ₺/DİS |\n| Fiili ücret | 22 ₺/DİS |\n| Fiili süre | 540 DİS |\n\nBuna göre direkt işçilik süre farkı aşağıdakilerden hangisidir?',
        {
            'A': '600 ₺ olumlu',
            'B': '1.800 ₺ olumsuz',
            'C': '660 ₺ olumsuz',
            'D': '600 ₺ olumsuz',
            'E': '1.200 ₺ olumlu',
        },
        'D',
        'Standart süre fiili üretimin **eşdeğeri** üzerinden bulunur: 900 + (300 × %40) = 1.020 eşdeğer adet × 0,5 = 510 DİS. Süre farkı = (540 − 510) × 20 = **600 ₺ olumsuz**. Yarı mamulü tam saymak (600 DİS) ya da hiç saymamak (450 DİS) standart süreyi bozar.',
        'Maliyet muhasebesi - standart maliyet (eşdeğer üretim)',
    ),
    # düzey 3
    '0057': patch(
        "Bir işletmenin standart maliyet kartı aşağıdaki gibidir:\n\n| Maliyet unsuru | Standart miktar | Standart fiyat |\n|---|---|---|\n| Direkt ilk madde ve malzeme | 2,5 kg | 40 ₺/kg |\n| Direkt işçilik | 1,2 DİS | 50 ₺/DİS |\n| Genel üretim gideri | 1,2 DİS | 35 ₺/DİS |\n\nDönemde 3.000 birim mamul üretilmiş, kg'ı 42 ₺'den 7.800 kg direkt ilk madde kullanılmıştır. Buna göre direkt ilk madde miktar farkı aşağıdakilerden hangisidir?",
        {
            'A': '12.000 ₺ olumsuz',
            'B': '12.600 ₺ olumsuz',
            'C': '27.600 ₺ olumsuz',
            'D': '15.600 ₺ olumsuz',
            'E': '12.000 ₺ olumlu',
        },
        'A',
        'Standart miktar = 3.000 × 2,5 = 7.500 kg. Miktar farkı = (7.800 − 7.500) × standart fiyat 40 = **12.000 ₺ olumsuz**. Fiyat farkı ayrıca (42 − 40) × 7.800 = 15.600 ₺ olumsuzdur.',
        'Maliyet muhasebesi - standart maliyet (DİMM farkları)',
    ),
    # düzey 3
    '0058': patch(
        "Standart maliyet sistemini kullanan bir işletme dönemde 4.000 birim mamul üretmiştir. Mamulde kullanılan hammaddenin standart tüketimi birim başına 5 kg, standart fiyatı kg başına 14 ₺'dir. Dönemde 21.000 kg hammadde kullanılmış ve hammadde maliyeti 283.500 ₺ olarak gerçekleşmiştir. Buna göre direkt ilk madde ve malzeme fiyat farkı ve yönü aşağıdakilerden hangisidir?",
        {
            'A': '3.500 ₺ olumsuz',
            'B': '10.500 ₺ olumsuz',
            'C': '10.500 ₺ olumlu',
            'D': '14.000 ₺ olumsuz',
            'E': '10.000 ₺ olumlu',
        },
        'C',
        'Fiili fiyat = 283.500 ÷ 21.000 = 13,50 ₺/kg. Fiyat farkı = (13,50 − 14) × fiili miktar 21.000 = **10.500 ₺ olumlu** (hammadde standarttan ucuza alınmış). Miktar farkı ise (21.000 − 20.000) × 14 = 14.000 ₺ olumsuzdur.',
        'Maliyet muhasebesi - standart maliyet (DİMM fiyat farkı)',
    ),
    # düzey 3
    '0059': patch(
        "Standart maliyet sistemini uygulayan bir işletmede birim başına standart direkt işçilik süresi 2 saat, standart saat ücreti 45 ₺'dir. Dönemde 5.000 birim mamul üretilmiş ve 18.000 ₺ olumlu direkt işçilik süre farkı hesaplanmıştır. Buna göre dönemde fiilen çalışılan süre kaç saattir?",
        {
            'A': '10.000',
            'B': '10.400',
            'C': '400',
            'D': '9.200',
            'E': '9.600',
        },
        'E',
        'Standart süre = 5.000 × 2 = 10.000 saat. Süre farkı = (fiili − standart) × standart ücret → −18.000 = (x − 10.000) × 45 → x − 10.000 = −400 → x = **9.600** saat. Fark olumlu olduğundan standarttan az çalışılmıştır.',
        'Maliyet muhasebesi - standart maliyet (tersine)',
    ),
    # düzey 2
    '0060': patch(
        'Genel üretim gideri farklarının üçlü analizi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kapasite farkı, fiili çalışılan süre ile fiili üretim için izin verilen standart süre arasındaki farktan doğar.\n\nII. Bütçe farkı, fiili GÜG ile fiili faaliyet düzeyine göre hazırlanan esnek bütçe arasındaki farktır.\n\nIII. Verimlilik farkı, normal kapasite ile fiilen kullanılan kapasite arasındaki farktan doğar.',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'Yalnız II',
            'E': 'II ve III',
        },
        'D',
        '**II doğrudur:** bütçe (harcama) farkı fiili GÜG ile fiili faaliyet düzeyindeki esnek bütçe arasındaki farktır. **I ve III yer değiştirmiştir:** fiili süre ile standart süre arasındaki farktan doğan **verimlilik** farkıdır; normal kapasite ile fiili kapasite arasındaki farktan doğan ise **kapasite** farkıdır. Doğru cevap **Yalnız II**.',
        'Maliyet muhasebesi - standart maliyet (GÜG farkları)',
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
    print(f"1 paket / {len(PATCHES)} soru ('Standart Maliyet' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
