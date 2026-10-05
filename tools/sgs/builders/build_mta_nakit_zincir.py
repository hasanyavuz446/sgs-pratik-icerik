#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nakit Akim Analizi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Mali tablolar analizi tablolu tur. Pakette 20 soru 'giris - cikis' ya da 'donem basi + net akis' klonuydu; 5 kavram sorusu cok sayida mutlak ifadeli celdirici tasiyordu. 35 soru korundu (tek bayrakli celdiriciler yenilendi); 25 yeni soru: dolayli yontem (amortisman, karsilik, duran varlik satis kari/zarari, isletme sermayesi degisimleri, tablodan), dogrudan yontem (musteri tahsilati, tedarikci, vergi, faiz, personel odemesi), uc bolumden donem sonu nakit, yatirim ve finansman net akisi, nakit disi islemler, brut raporlama, TMS 7 faiz siniflandirmasi, tablo yorumu. Tutarlar Fraction ile hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Mali tablolar analizi - nakit akis tablosu · TMS 7
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/mali_tablolar_analizi/nakit_akim_analizi.json"
STYLE_REF = 'SGS Mali Tablolar Analizi (oran zinciri, ters hesap; gerçek sınav profiline kalibre)'
ONEK = "mta-nakit-gen-"


def patch(stem, options, answer, solution, ref='Mali analiz - nakit akış tablosu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Nakit akım tablosu ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşletmenin stok giriş ve çıkış hareketlerini miktar bazında izleyen bir yardımcı tablodur.',
            'B': 'İşletmenin bir dönemdeki nakit ve nakit benzeri giriş ve çıkışlarını gösteren tablodur.',
            'C': 'İşletmenin dağıttığı kâr paylarını dönemler itibarıyla karşılaştırmalı gösteren tablodur.',
            'D': 'İşletmenin belirli bir andaki varlık ve kaynak yapısını ayrıntılı biçimde gösteren temel tablodur.',
            'E': 'İşletmenin döneme ait vergi matrahını beyan etmek için düzenlenen resmî bir beyanname belgesidir.',
        },
        'B',
        '**Nakit akım tablosu**; işletmenin bir dönemdeki **nakit ve nakit benzeri giriş ve çıkışlarını** gösteren, dönem başı nakitten dönem sonu nakite ulaşmayı sağlayan tablodur.',
        'TMS 7; Mali analiz - nakit akım tablosu',
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdakilerden hangisi bir nakit ÇIKIŞIdır?',
        {
            'A': 'Nakit sermaye artırımı',
            'B': 'Satışlardan tahsilat',
            'C': 'Duran varlık satılıp bedelin tahsil edilmesi',
            'D': 'Banka kredisi kullanılması',
            'E': 'Tedarikçilere (satıcılara) nakit ödeme yapılması',
        },
        'E',
        '**Tedarikçilere nakit ödeme** işletmeden nakit çıkışıdır. Diğerleri nakit girişidir.',
        'Mali analiz - nakit çıkışları',
    ),
    # düzey 2
    '0003': patch(
        "TMS 7'ye (Nakit Akış Tablosu standardı) göre nakit akışları hangi üç faaliyet grubunda sınıflandırılır?",
        {
            'A': 'Alış, satış ve stok faaliyetleri',
            'B': 'Üretim, pazarlama ve yönetim faaliyetleri',
            'C': 'İşletme, yatırım ve finansman faaliyetleri',
            'D': 'Kısa, orta ve uzun vadeli faaliyetler',
            'E': 'Vergi, SGK ve damga faaliyetleri',
        },
        'C',
        "TMS 7'ye göre nakit akışları **işletme (esas faaliyet), yatırım ve finansman** faaliyetleri olmak üzere üç grupta sınıflandırılır.",
        'TMS 7 - üç faaliyet',
    ),
    # düzey 2
    '0004': patch(
        'Finansman faaliyetlerinden nakit akışları temel olarak neyi kapsar?',
        {
            'A': 'İşletmenin özkaynak ve yabancı kaynak yapısındaki değişimlerden doğan nakit akışlarını (sermaye artırımı, borçlanma, borç anapara ödemesi, temettü ödemesi)',
            'B': 'İşletmenin esas faaliyeti kapsamında müşterilerinden yaptığı mal ve hizmet satış tahsilatlarından doğan nakit girişlerini kapsar',
            'C': 'İşletmenin satışa konu ettiği ticari mal ve üretimde kullandığı hammadde stoklarının peşin alımından doğan nakit çıkışlarını kapsar',
            'D': 'İşletmenin üretim ve hizmet faaliyetinde uzun süre kullanmak üzere edindiği bina, makine gibi maddi duran varlıkların satın alınmasından doğan nakit çıkışlarını kapsar',
            'E': 'İşletmenin sahip olduğu duran varlıklar için dönem boyunca ayırdığı amortisman giderlerinin toplam tutarından oluşan kalemleri kapsar',
        },
        'A',
        '**Finansman faaliyetlerinden nakit akışları**; özkaynak ve yabancı kaynak yapısındaki değişimlerden doğar: sermaye artırımı (giriş), borçlanma (giriş), borç anapara ödemesi (çıkış), temettü ödemesi (çıkış).',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0005': patch(
        'Tedarikçilere mal bedeli için yapılan nakit ödeme, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetleri (nakit çıkışı)',
            'B': 'Finansman faaliyetleri (nakit girişi)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'Yatırım faaliyetleri (nakit girişi)',
            'E': 'İşletme faaliyetleri (nakit çıkışı)',
        },
        'E',
        'Tedarikçilere mal bedeli ödemesi esas faaliyetle ilgilidir → **işletme faaliyetleri** grubunda bir **nakit çıkışıdır**.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0006': patch(
        "Nakit akım tablosuyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Nakit ve nakit benzeri giriş-çıkışlarını gösterir.\n\nII. TMS 7'ye göre işletme, yatırım ve finansman faaliyetleri olarak üç grupta sınıflandırılır.\n\nIII. Dönem Sonu Nakit = Dönem Başı Nakit − Net Nakit Akışı.",
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'A',
        "**III yanlıştır:** Dönem Sonu Nakit = Dönem Başı Nakit **+** Net Nakit Akışı'dır; net nakit akışı dönem başı nakde eklenir, çıkarılmaz. **I** (nakit giriş-çıkışını gösterir) ve **II** (TMS 7 üç faaliyet grubu: işletme, yatırım, finansman) doğrudur. Doğru cevap **I ve II**.",
        'TMS 7; Mali analiz - nakit akım',
    ),
    # düzey 2
    '0007': patch(
        'Ortaklara ödenen nakit kâr payı (temettü), nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'İşletme faaliyetleri (nakit girişi)',
            'B': 'Finansman faaliyetleri (nakit girişi)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'İşletme faaliyetleri (nakit çıkışı)',
            'E': 'Yatırım faaliyetleri (nakit girişi)',
        },
        'C',
        'Ortaklara temettü ödemesi özkaynakla ilgili bir nakit çıkışıdır → genel uygulamada **finansman faaliyetleri** grubunda bir **nakit çıkışıdır**.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0008': patch(
        'Uzun vadeli banka kredisinin anaparasının geri ödenmesi, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'İşletme faaliyetleri (nakit girişi)',
            'B': 'Finansman faaliyetleri (nakit çıkışı)',
            'C': 'Yatırım faaliyetleri (nakit çıkışı)',
            'D': 'Yatırım faaliyetleri (nakit girişi)',
            'E': 'Finansman faaliyetleri (nakit girişi)',
        },
        'B',
        'Kredi anaparasının geri ödenmesi yabancı kaynağı azaltır → **finansman faaliyetleri** grubunda bir **nakit çıkışıdır**.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0009': patch(
        'Aşağıdaki nakit akışlarından hangileri FİNANSMAN faaliyeti kapsamındadır?\n\nI. Satışlardan tahsilat\n\nII. Nakit sermaye artırımı\n\nIII. Uzun vadeli borç anapara ödemesi',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'D',
        '**II (sermaye artırımı)** ve **III (borç anapara ödemesi)** finansman faaliyetidir. **I (satış tahsilatı)** ise işletme faaliyetidir. Doğru cevap **II ve III**.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0010': patch(
        'Aşağıdaki nakit akışı-faaliyet eşleştirmelerinden hangisi YANLIŞTIR?',
        {
            'A': 'Temettü ödemesi → İşletme faaliyeti',
            'B': 'Satışlardan tahsilat → İşletme faaliyeti',
            'C': 'Maddi duran varlık alımı → Yatırım faaliyeti',
            'D': 'Kredi kullanımı (borçlanma) → Finansman faaliyeti',
            'E': 'Tedarikçilere ödeme → İşletme faaliyeti',
        },
        'A',
        "**YANLIŞ olan D'dir:** Ortaklara temettü ödemesi genel uygulamada **finansman faaliyetidir**, işletme faaliyeti değil. Diğer eşleştirmeler doğrudur.",
        'TMS 7 - faaliyet sınıflaması',
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdakilerden hangisi işletme faaliyetlerinden bir nakit ÇIKIŞIdır?',
        {
            'A': 'Duran varlık satışından tahsilat',
            'B': 'Tedarikçilere mal bedeli ödemesi',
            'C': 'Nakit sermaye artırımı sağlanması',
            'D': 'Satışlardan nakit tahsilat yapılması',
            'E': 'Bankadan kredi kullanılması',
        },
        'B',
        '**Tedarikçilere mal bedeli ödemesi** işletme faaliyetlerinden bir **nakit çıkışıdır**. Diğerleri ya nakit girişidir ya da farklı faaliyet grubundadır.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0012': patch(
        'Bir işletmenin makine (maddi duran varlık) satışından elde ettiği nakit, hangi faaliyet grubunda ve hangi yönde gösterilir?',
        {
            'A': 'Yatırım faaliyeti - çıkış',
            'B': 'Finansman faaliyeti - çıkış',
            'C': 'Finansman faaliyeti - giriş',
            'D': 'Yatırım faaliyeti - giriş',
            'E': 'İşletme faaliyeti - çıkış',
        },
        'D',
        'Makine (duran varlık) satışından elde edilen nakit → **yatırım faaliyeti** grubunda bir **nakit girişidir**.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletmenin dolaylı yöntemle hazırlanacak nakit akış tablosu için bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Dönem net kârı | 300.000 |\n| Amortisman giderleri | 60.000 |\n| Maddi duran varlık satış kârı | 20.000 |\n| Ticari alacaklardaki azalış | 25.000 |\n| Stoklardaki artış | 40.000 |\n| Satıcılardaki azalış | 15.000 |\n\nBuna göre işletme faaliyetlerinden sağlanan nakit akışı kaç ₺'dir?",
        {
            'A': '350.000',
            'B': '340.000',
            'C': '360.000',
            'D': '330.000',
            'E': '310.000',
        },
        'E',
        '300.000 + 60.000 (amortisman) − 20.000 (satış kârı; tahsilat yatırım faaliyetlerinde gösterilir) + 25.000 − 40.000 − 15.000 = **310.000 ₺**. Satış kârını düşmemek aynı nakdi iki kez saymak olur.',
        'Mali analiz - nakit akış tablosu (dolaylı yöntem)',
    ),
    # düzey 3
    '0014': patch(
        'Bir işletmenin nakit akış tablosunda işletme faaliyetlerinden nakit akışı pozitif, yatırım ve finansman faaliyetlerinden nakit akışları negatiftir; dönemde nakit mevcudu artmıştır. Bu tablo için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'Esas faaliyetlerin nakit açığı sermaye artırımıyla kapatılmıştır.',
            'B': 'İşletmenin dönem net kârı negatiftir.',
            'C': 'Esas faaliyetlerden yaratılan nakit, yatırım harcamalarını ve finansman ödemelerini karşılamaya yetmiştir.',
            'D': 'İşletme duran varlık satarak nakit sağlamıştır.',
            'E': 'İşletme yatırımlarını borçlanarak finanse etmiştir.',
        },
        'C',
        'Yatırım ve finansman akışları negatif olduğundan nakit bu faaliyetlerden sağlanmamış, kullanılmıştır. Nakit yine de arttığına göre işletme faaliyetlerinden gelen nakit bu kullanımları aşmıştır. Net kârın işareti tablodan çıkarılamaz.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0015': patch(
        "Bir işletmenin döneme ait kurumlar vergisi gideri 90.000 ₺'dir. Ödenecek vergi hesabının bakiyesi dönem başında 30.000 ₺, dönem sonunda 45.000 ₺'dir. Buna göre dönemde ödenen vergi kaç ₺'dir?",
        {
            'A': '105.000',
            'B': '90.000',
            'C': '45.000',
            'D': '60.000',
            'E': '75.000',
        },
        'E',
        'Ödenen vergi = dönem başı borç + dönem gideri − dönem sonu borç = 30.000 + 90.000 − 45.000 = **75.000 ₺**. Borcun 15.000 ₺ artması giderin bir kısmının henüz ödenmediğini gösterir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0016': patch(
        'Aşağıdakilerden hangisi nakit akış tablosunda nakit kullanımları (nakit çıkışları) arasında yer almaz?',
        {
            'A': 'Ortaklara ödenen kâr payı',
            'B': 'Satın alınan makine bedeli',
            'C': 'Dönemin amortisman gideri',
            'D': 'Ödenen kurumlar vergisi',
            'E': 'Personele ödenen ücretler',
        },
        'C',
        'Amortisman bir giderdir fakat nakit çıkışı doğurmaz; bu yüzden nakit kullanımı değildir (dolaylı yöntemde kâra eklenir). Diğerleri fiilî nakit ödemeleridir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0017': patch(
        'Nakit akış tablosuyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşletmenin belirli bir dönemdeki nakit kaynaklarını ve kullanım yerlerini gösterir.\n\nII. Tahakkuk esasına göre düzenlenir.\n\nIII. Dolaylı yöntemde ticari alacaklardaki net azalışlar nakde olumlu etki olarak eklenir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'D',
        '**I doğrudur.** **II yanlıştır:** nakit akış tablosu nakit esasına göre düzenlenir; tahakkuk esası gelir tablosu ve bilançonundur. **III doğrudur:** alacağın azalması tahsilat demektir. Doğru cevap **I ve III**.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0018': patch(
        "Bir işletme dönemde 300.000 ₺ nakitle makine satın almış, defter değeri 60.000 ₺ olan bir aracı 80.000 ₺ nakit karşılığında satmış ve 50.000 ₺ nakit ödeyerek bir iştirak payı edinmiştir. Buna göre yatırım faaliyetlerinden net nakit akışı kaç ₺'dir?",
        {
            'A': '−170.000',
            'B': '−270.000',
            'C': '−230.000',
            'D': '−250.000',
            'E': '−190.000',
        },
        'B',
        'Yatırım faaliyetlerinde nakit tutarlar esas alınır: −300.000 + 80.000 − 50.000 = **−270.000 ₺**. Aracın defter değeri (60.000) değil, tahsil edilen tutar (80.000) gösterilir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0019': patch(
        "Bir işletmenin dönem net kârı 90.000 ₺, amortisman giderleri 25.000 ₺'dir. İşletme sermayesi kalemleri şöyledir:\n\n| Kalem | Dönem başı (₺) | Dönem sonu (₺) |\n|---|---|---|\n| Ticari alacaklar | 80.000 | 110.000 |\n| Stoklar | 120.000 | 100.000 |\n| Satıcılar | 60.000 | 75.000 |\n| Ödenecek vergi | 20.000 | 15.000 |\n\nDolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç ₺'dir?",
        {
            'A': '115.000',
            'B': '85.000',
            'C': '75.000',
            'D': '90.000',
            'E': '175.000',
        },
        'A',
        'Alacak artışı −30.000; stok azalışı +20.000; satıcı artışı +15.000; ödenecek vergideki azalış −5.000. 90.000 + 25.000 − 30.000 + 20.000 + 15.000 − 5.000 = **115.000 ₺**.',
        'Mali analiz - nakit akış tablosu (dolaylı yöntem)',
    ),
    # düzey 2
    '0020': patch(
        "TMS 7'ye göre ödenen faizlerin nakit akış tablosunda sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ödenen faiz her yıl farklı bir faaliyet grubunda gösterilir.',
            'B': 'İşletme faaliyetleri veya finansman faaliyetleri arasında sınıflandırılabilir; seçilen yöntem tutarlı uygulanır.',
            'C': 'Nakit akış tablosunda gösterilmez, dipnotta açıklanır.',
            'D': 'Dönemin net kârından düşüldüğü için ayrıca gösterilmez.',
            'E': 'Yatırım faaliyetleri arasında gösterilir.',
        },
        'B',
        'TMS 7, ödenen faizlerin işletme faaliyetleri (kârın belirlenmesine girdiği için) ya da finansman faaliyetleri (finansman maliyeti olduğu için) arasında sınıflandırılmasına izin verir; seçim dönemden döneme tutarlı olmalıdır.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0021': patch(
        'Nakit akım tablosunun temel amacı aşağıdakilerden hangisidir?',
        {
            'A': 'İşletmenin nakit yaratma gücünü ve nakdi nerelerden sağlayıp nerelerde kullandığını göstererek nakit yönetimini değerlendirmek',
            'B': 'İşletmenin duran varlıkları için ayrılacak amortisman tutarını seçilen yönteme göre hesaplayıp ilgili dönemlere dağıtmaktır',
            'C': 'İşletmenin sermayedar ortaklarını sahip oldukları pay oranlarıyla birlikte eksiksiz biçimde listeleyip raporda sunmaktır',
            'D': 'İşletmenin gelecek döneme ait reklam, tanıtım ve pazarlama harcamalarının bütçesini kalem kalem planlayıp yönetime sunmaktır',
            'E': 'İşletmenin elde ettiği dönem kârını olduğundan çok daha düşük göstererek hem ortaklardan hem de kamu otoritesinden gizli tutmaya çalışmaktır',
        },
        'A',
        'Nakit akım tablosunun amacı; işletmenin **nakit yaratma gücünü** ve nakdi **nereden sağlayıp nerede kullandığını** göstererek nakit (likidite) yönetimini değerlendirmektir.',
        'TMS 7',
    ),
    # düzey 2
    '0022': patch(
        'Nakit akım tablosunda dönem sonu nakit mevcudu nasıl bulunur?',
        {
            'A': 'Dönem Başı Nakit − Net Nakit Akışı',
            'B': 'Net Nakit Akışı − Dönem Sonu Borçlar',
            'C': 'Dönem Başı Nakit × Net Nakit Akışı',
            'D': 'Dönem Başı Nakit + Net Nakit Akışı',
            'E': 'Net Nakit Akışı − Dönem Başı Nakit',
        },
        'D',
        '**Dönem Sonu Nakit = Dönem Başı Nakit + Net Nakit Akışı** (net akış = toplam giriş − toplam çıkış).',
        'Mali analiz - nakit akım',
    ),
    # düzey 2
    '0023': patch(
        'İşletme faaliyetlerinden nakit akışları temel olarak neyi kapsar?',
        {
            'A': 'İşletmenin uzun vadeli iştirak ve bağlı ortaklık paylarının satın alınmasından doğan nakit akışlarını kapsar',
            'B': 'İşletmenin esas (ana) faaliyetlerinden doğan nakit akışlarını (satış tahsilatları, tedarikçi/personel ödemeleri, vergi ödemeleri vb.)',
            'C': 'İşletmenin maddi ve maddi olmayan duran varlıklarının ve uzun vadeli yatırımlarının alım ile satımından doğan nakit akışlarını kapsar',
            'D': 'İşletmenin özkaynak ve yabancı kaynağındaki değişimlerden, sermaye artırımı ve borçlanmadan doğan nakit akışlarını kapsar',
            'E': 'İşletmenin ortaklarına dağıttığı nakit kâr paylarının (temettü) ödemelerinden doğan nakit çıkışlarını kapsar',
        },
        'B',
        '**İşletme faaliyetlerinden nakit akışları**; işletmenin esas faaliyetlerinden doğan nakit akışlarıdır (satışlardan tahsilat, tedarikçilere/personele ödemeler, vergi ödemeleri vb.).',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0024': patch(
        "Nakit akım tablosunda 'nakit benzeri' aşağıdakilerden hangisiyle en iyi tanımlanır?",
        {
            'A': 'İşletmenin uzun vadeli olarak elinde bulundurduğu, dönemsel faiz getirisi sağlayan devlet tahvilleri, hazine bonoları ve benzeri sabit getirili kıymetlerdir',
            'B': 'İşletmenin üretim ve hizmet faaliyetinde birden fazla dönem boyunca kullandığı bina, makine gibi maddi duran varlıklardır',
            'C': 'Vadesi kısa (genellikle 3 ay veya daha az), yüksek likiditeye sahip, değer kaybı riski önemsiz ve kolayca nakde çevrilebilen yatırımlar',
            'D': 'İşletmenin satmak amacıyla stoklarında tuttuğu ve piyasa talebine göre değeri sürekli dalgalanabilen ticari mallardır',
            'E': 'İşletmenin uzun vadeli olarak elde tuttuğu ve kâr elde etmeyi amaçladığı iştirak ile bağlı ortaklık paylarıdır',
        },
        'C',
        '**Nakit benzerleri**; vadesi kısa (genellikle 3 ay ve altı), yüksek likit, değer kaybı riski önemsiz ve kolayca nakde çevrilebilen yatırımlardır.',
        'TMS 7 - nakit benzeri',
    ),
    # düzey 2
    '0025': patch(
        'Maddi duran varlık satın alınması için yapılan nakit ödeme, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Finansman faaliyetleri (nakit girişi)',
            'B': 'Yatırım faaliyetleri (nakit çıkışı)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'İşletme faaliyetleri (nakit girişi)',
            'E': 'İşletme faaliyetleri (nakit çıkışı)',
        },
        'B',
        'Maddi duran varlık alımı bir yatırımdır → **yatırım faaliyetleri** grubunda bir **nakit çıkışıdır**.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 2
    '0026': patch(
        'Bir maddi duran varlığın satışından elde edilen nakit, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetleri (nakit girişi)',
            'B': 'Finansman faaliyetleri (nakit çıkışı)',
            'C': 'Finansman faaliyetleri (nakit girişi)',
            'D': 'İşletme faaliyetleri (nakit çıkışı)',
            'E': 'İşletme faaliyetleri (nakit girişi)',
        },
        'A',
        'Maddi duran varlık satışından elde edilen nakit → **yatırım faaliyetleri** grubunda bir **nakit girişidir**.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 2
    '0027': patch(
        'Personele ödenen nakit ücretler, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetleri (nakit girişi)',
            'B': 'Finansman faaliyetleri (nakit çıkışı)',
            'C': 'İşletme faaliyetleri (nakit çıkışı)',
            'D': 'Finansman faaliyetleri (nakit girişi)',
            'E': 'Yatırım faaliyetleri (nakit çıkışı)',
        },
        'C',
        'Personele ücret ödemesi esas faaliyetle ilgilidir → **işletme faaliyetleri** grubunda bir **nakit çıkışıdır**.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0028': patch(
        'Ödenen kurumlar/gelir vergisi, nakit akım tablosunda genel olarak hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetleri (nakit girişi)',
            'B': 'Yatırım faaliyetleri (nakit çıkışı)',
            'C': 'Finansman faaliyetleri (nakit girişi)',
            'D': 'İşletme faaliyetleri (nakit çıkışı)',
            'E': 'Finansman faaliyetleri (nakit çıkışı)',
        },
        'D',
        'Ödenen vergiler genel olarak (aksi belirtilmedikçe) **işletme faaliyetleri** grubunda bir **nakit çıkışı** olarak sınıflandırılır.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0029': patch(
        'Aşağıdaki nakit akışlarından hangileri İŞLETME faaliyeti kapsamındadır?\n\nI. Satışlardan tahsilat\n\nII. Tedarikçilere ödeme\n\nIII. Duran varlık alımı için ödeme',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'E',
        '**I (satış tahsilatı)** ve **II (tedarikçi ödemesi)** işletme faaliyetidir. **III (duran varlık alımı)** ise yatırım faaliyetidir. Doğru cevap **I ve II**.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0030': patch(
        'Bir marka (maddi olmayan duran varlık) satın almak için ödenen nakit, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'İşletme faaliyetleri (nakit girişi)',
            'B': 'Yatırım faaliyetleri (nakit çıkışı)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'Finansman faaliyetleri (nakit girişi)',
            'E': 'İşletme faaliyetleri (nakit çıkışı)',
        },
        'B',
        'Maddi olmayan duran varlık (marka) alımı bir yatırımdır → **yatırım faaliyetleri** grubunda **nakit çıkışıdır**.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 2
    '0031': patch(
        'Nakit akım tablosu, dönem başı bilanço ile dönem sonu bilanço arasında hangi kalem açısından bağ kurar?',
        {
            'A': 'Nakit ve nakit benzeri mevcudu (dönem başı nakitten dönem sonu nakite geçişi açıklar)',
            'B': 'İşletmenin maddi duran varlıkları (dönem başı tutardan dönem sonu net değere geçişi açıklar)',
            'C': 'İşletmenin toplam aktif büyüklüğü (dönem başı aktiften dönem sonu aktife geçişi açıklar)',
            'D': 'İşletmenin stok mevcudu (dönem başı stoktan dönem sonu stok tutarına geçişi açıklar)',
            'E': 'İşletmenin özkaynak toplamı (dönem başı özkaynaktan dönem sonu özkaynağa geçişi açıklar)',
        },
        'A',
        'Nakit akım tablosu, **dönem başı nakit ve nakit benzeri** mevcudundan **dönem sonu** mevcuduna geçişi (aradaki tüm nakit hareketlerini) açıklayarak iki bilanço arasında bağ kurar.',
        'TMS 7',
    ),
    # düzey 2
    '0032': patch(
        'Nakit akım analiziyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Duran varlık alımı işletme, kredi kullanımı yatırım, mal satış tahsilatı finansman faaliyetidir.\n\nII. Net nakit akışı = Toplam Nakit Girişleri − Toplam Nakit Çıkışları.\n\nIII. Dönem Sonu Nakit = Dönem Başı Nakit + Net Nakit Akışı.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'B',
        "**I yanlıştır:** TMS 7'ye göre doğru sınıflama şöyledir: **duran varlık alımı yatırım**, **kredi kullanımı finansman**, **mal satış tahsilatı işletme** faaliyetidir; öncüldeki eşleştirme yanlıştır. **II** net nakit akışı = girişler − çıkışlar; **III** dönem sonu nakit = dönem başı nakit + net nakit akışı. Doğru cevap **II ve III**.",
        'TMS 7; Mali analiz - nakit akım',
    ),
    # düzey 3
    '0033': patch(
        "Bir işletmenin dönem net kârı 120.000 ₺'dir. Dönemde 30.000 ₺ amortisman, 10.000 ₺ kıdem tazminatı karşılık gideri ve 8.000 ₺ maddi duran varlık satış zararı gelir tablosuna yansımıştır. Ticari borçlar 12.000 ₺ artmış, ticari alacaklar 20.000 ₺ artmıştır. Dolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç ₺'dir?",
        {
            'A': '150.000',
            'B': '144.000',
            'C': '124.000',
            'D': '160.000',
            'E': '168.000',
        },
        'D',
        'Nakit çıkışı gerektirmeyen giderler (amortisman 30.000, karşılık 10.000) ve satış zararı (8.000; tahsilat yatırım faaliyetinde) kâra eklenir: 120.000 + 30.000 + 10.000 + 8.000 + 12.000 − 20.000 = **160.000 ₺**.',
        'Mali analiz - nakit akış tablosu (dolaylı yöntem)',
    ),
    # düzey 3
    '0034': patch(
        "Bir işletmenin net satışları 900.000 ₺'dir. Dönemde ticari alacaklar 60.000 ₺ artmıştır. Satışların tamamı ticari alacaklar üzerinden izlendiğine göre doğrudan yönteme göre müşterilerden nakit tahsilat kaç ₺'dir?",
        {
            'A': '840.000',
            'B': '960.000',
            'C': '900.000',
            'D': '780.000',
            'E': '60.000',
        },
        'A',
        'Tahsilat = satışlar − alacak artışı = 900.000 − 60.000 = **840.000 ₺**. Alacağın artması satışların bir kısmının henüz tahsil edilmediğini gösterir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0035': patch(
        "Bir işletmenin faiz giderleri 50.000 ₺'dir. Tahakkuk etmiş faiz borçları dönem başında 8.000 ₺, dönem sonunda 12.000 ₺'dir. Buna göre dönemde ödenen faiz kaç ₺'dir?",
        {
            'A': '58.000',
            'B': '50.000',
            'C': '46.000',
            'D': '54.000',
            'E': '62.000',
        },
        'C',
        'Ödenen faiz = 8.000 + 50.000 − 12.000 = **46.000 ₺**.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0036': patch(
        'Aşağıdaki nakit akışlarından hangisi finansman faaliyetleri kapsamında değildir?',
        {
            'A': 'Bankadan kredi kullanılması',
            'B': 'Nakdi sermaye artırımı',
            'C': 'Ortaklara nakit kâr payı ödenmesi',
            'D': 'Kredinin anapara taksitinin geri ödenmesi',
            'E': 'Maddi duran varlık satışından tahsilat',
        },
        'E',
        'Maddi duran varlık satışı yatırım faaliyetidir. Kredi kullanımı ve geri ödemesi, sermaye artırımı ve kâr payı ödemesi işletmenin kaynak yapısını değiştirdiğinden finansman faaliyetidir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletmenin dönem net kârı 100.000 ₺, işletme faaliyetlerinden nakit akışı 40.000 ₺'dir. Dolaylı yöntemde net kâra yapılan düzeltmeler yalnız 20.000 ₺ amortisman ile ticari alacaklardaki değişimden oluşmaktadır. Buna göre ticari alacaklar nasıl değişmiştir?",
        {
            'A': '80.000 ₺ azalmıştır.',
            'B': '40.000 ₺ artmıştır.',
            'C': '120.000 ₺ artmıştır.',
            'D': '80.000 ₺ artmıştır.',
            'E': '60.000 ₺ artmıştır.',
        },
        'D',
        '100.000 + 20.000 − alacak değişimi = 40.000 → alacak düzeltmesi = −80.000 ₺. Kârdan düşülen düzeltme alacakların **80.000 ₺ arttığını** gösterir: satışların bir kısmı tahsil edilmemiştir.',
        'Mali analiz - nakit akış tablosu (dolaylı yöntem)',
    ),
    # düzey 3
    '0038': patch(
        "Bir işletmenin döneme ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Dönem başı nakit | 90.000 |\n| Dönem net kârı | 150.000 |\n| Amortisman | 40.000 |\n| Ticari alacaklardaki artış | 30.000 |\n| Nakitle makine alımı | 200.000 |\n| Alınan banka kredisi | 100.000 |\n| Ödenen kâr payı | 20.000 |\n\nBuna göre dönem sonu nakit mevcudu kaç ₺'dir?",
        {
            'A': '190.000',
            'B': '130.000',
            'C': '150.000',
            'D': '170.000',
            'E': '40.000',
        },
        'B',
        'İşletme: 150.000 + 40.000 − 30.000 = 160.000 ₺. Yatırım: −200.000 ₺. Finansman: 100.000 − 20.000 = 80.000 ₺. Net artış 40.000 ₺ → dönem sonu 90.000 + 40.000 = **130.000 ₺**.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdaki işlemlerden hangisi nakit akış tablosunda herhangi bir nakit akışı olarak gösterilmez?',
        {
            'A': 'İç kaynaklardan bedelsiz sermaye artırımı yapılması',
            'B': 'Kısa vadeli banka kredisinin nakit ödenmesi',
            'C': 'Hisse senedi ihraç primi tahsili',
            'D': 'Ortaklara nakit kâr payı ödenmesi',
            'E': 'Nakdi sermaye artırımı yapılması',
        },
        'A',
        'Bedelsiz sermaye artırımı yedeklerin sermayeye aktarılmasıdır; özkaynak içinde yer değiştirmedir ve nakit hareketi doğurmaz.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0040': patch(
        "Satıcıya olan 50.000 ₺'lik ticari borcun vadesinde ödenmeyip borç senediyle değiştirilmesi nakit akış tablosunda nasıl gösterilir?",
        {
            'A': 'Finansman faaliyetlerinde 50.000 ₺ nakit girişi olarak gösterilir.',
            'B': 'İşletme faaliyetlerinde 50.000 ₺ nakit çıkışı olarak gösterilir.',
            'C': 'Hem giriş hem çıkış olarak brüt gösterilir.',
            'D': 'Nakit hareketi olmadığından nakit akış tablosunda gösterilmez.',
            'E': 'Yatırım faaliyetlerinde 50.000 ₺ nakit çıkışı olarak gösterilir.',
        },
        'D',
        'Borcun türü değişmiş, nakit el değiştirmemiştir. Nakit akış tablosu yalnız nakit ve nakit benzerlerindeki hareketleri raporlar.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0041': patch(
        'Aşağıdakilerden hangisi bir nakit GİRİŞİdir?',
        {
            'A': 'Personele ücret ödenmesi',
            'B': 'Satışlardan nakit tahsilat yapılması',
            'C': 'Duran varlık satın alınması',
            'D': 'Vergi ödenmesi',
            'E': 'Peşin mal alımı için ödeme yapılması',
        },
        'B',
        '**Satışlardan nakit tahsilat** işletmeye nakit girişi sağlar. Diğer seçenekler nakit çıkışıdır.',
        'Mali analiz - nakit girişleri',
    ),
    # düzey 2
    '0042': patch(
        'Net nakit akışı nasıl hesaplanır?',
        {
            'A': 'Toplam Nakit Girişleri − Toplam Nakit Çıkışları',
            'B': 'Dönem Sonu Nakit + Dönem Başı Nakit',
            'C': 'Toplam Nakit Çıkışları − Toplam Nakit Girişleri',
            'D': 'Dönem Başı Nakit − Dönem Sonu Nakit',
            'E': 'Nakit Girişleri × Nakit Çıkışları',
        },
        'A',
        '**Net Nakit Akışı = Toplam Nakit Girişleri − Toplam Nakit Çıkışları**. Pozitifse dönemde nakit artmış, negatifse azalmıştır.',
        'Mali analiz - net nakit akışı',
    ),
    # düzey 2
    '0043': patch(
        'Yatırım faaliyetlerinden nakit akışları temel olarak neyi kapsar?',
        {
            'A': 'İşletmenin bankalardan kullandığı kısa ve uzun vadeli kredilerden doğan nakit girişlerini kapsar',
            'B': 'İşletmenin ortaklarından sağladığı nakit sermaye artırımından doğan nakit girişlerini kapsar',
            'C': 'İşletmenin esas faaliyeti kapsamında müşterilerinden mal ve hizmet karşılığı yaptığı satış tahsilatlarından doğan nakit girişlerini kapsar',
            'D': 'Duran varlıkların (maddi/maddi olmayan) ve uzun vadeli yatırımların (iştirak vb.) alım-satımından doğan nakit akışlarını',
            'E': 'İşletmenin çalışanlarına ödediği ücret, maaş ve sosyal haklardan doğan nakit çıkışlarını kapsar',
        },
        'D',
        '**Yatırım faaliyetlerinden nakit akışları**; duran varlıkların (maddi/maddi olmayan) ve uzun vadeli yatırımların (iştirak, bağlı ortaklık vb.) **alım-satımından** doğan nakit akışlarını kapsar.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 2
    '0044': patch(
        'Satışlardan yapılan nakit tahsilat, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetleri (nakit girişi)',
            'B': 'Yatırım faaliyetleri (nakit çıkışı)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'Finansman faaliyetleri (nakit girişi)',
            'E': 'İşletme faaliyetleri (nakit girişi)',
        },
        'E',
        'Satışlardan tahsilat, esas faaliyetten doğduğundan **işletme faaliyetleri** grubunda bir **nakit girişidir**.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 2
    '0045': patch(
        'Nakit sermaye artırımından sağlanan nakit, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'İşletme faaliyetleri (nakit girişi)',
            'B': 'Yatırım faaliyetleri (nakit girişi)',
            'C': 'Finansman faaliyetleri (nakit girişi)',
            'D': 'Yatırım faaliyetleri (nakit çıkışı)',
            'E': 'Finansman faaliyetleri (nakit çıkışı)',
        },
        'C',
        'Sermaye artırımı özkaynak yapısını değiştirir → **finansman faaliyetleri** grubunda bir **nakit girişidir**.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0046': patch(
        'Bankadan kullanılan (alınan) kredinin sağladığı nakit, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'İşletme faaliyetleri (nakit çıkışı)',
            'B': 'İşletme faaliyetleri (nakit girişi)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'Finansman faaliyetleri (nakit girişi)',
            'E': 'Yatırım faaliyetleri (nakit girişi)',
        },
        'D',
        'Kredi kullanımı (borçlanma) yabancı kaynak yapısını değiştirir → **finansman faaliyetleri** grubunda bir **nakit girişidir**. (Anapara ödemesi ise finansmanda çıkıştır.)',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0047': patch(
        'Bir iştirak (uzun vadeli pay) satın almak için ödenen nakit, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Finansman faaliyetleri (nakit çıkışı)',
            'B': 'İşletme faaliyetleri (nakit girişi)',
            'C': 'Yatırım faaliyetleri (nakit çıkışı)',
            'D': 'İşletme faaliyetleri (nakit çıkışı)',
            'E': 'Finansman faaliyetleri (nakit girişi)',
        },
        'C',
        'İştirak (uzun vadeli yatırım) alımı → **yatırım faaliyetleri** grubunda bir **nakit çıkışıdır**.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 2
    '0048': patch(
        'Aşağıdaki nakit akışlarından hangileri YATIRIM faaliyeti kapsamındadır?\n\nI. Maddi duran varlık alımı için ödeme\n\nII. Ortaklara temettü ödemesi\n\nIII. Mal satışından tahsilat',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'B',
        '**I (maddi duran varlık alımı)** yatırım faaliyetidir. **II (ortaklara temettü ödemesi)** finansman, **III (mal satışından tahsilat)** ise işletme faaliyetidir. Doğru cevap **Yalnız I**.',
        'TMS 7 - yatırım faaliyetleri',
    ),
    # düzey 2
    '0049': patch(
        'Aşağıdakilerden hangisi nakit benzeri olarak değerlendirilmeye en uygun kalemdir?',
        {
            'A': 'Vadesine 2 ay kalmış, kolayca nakde çevrilebilen bir para piyasası fonu/mevduat',
            'B': 'Satılmak amacıyla depoda bekletilen ve değeri talebe göre değişen ticari mal stoğu',
            'C': 'Faiz getirisi için elde tutulan, vadesine 10 yıl kalmış uzun vadeli bir devlet tahvili',
            'D': 'Kâr amacıyla uzun vadeli elde tutulan bir iştirak (bağlı ortaklık) payı yatırımı',
            'E': 'Üretimde uzun yıllar boyunca kullanılmak üzere edinilen bir makine (maddi duran varlık)',
        },
        'A',
        '**Vadesi kısa (ör. 2 ay), yüksek likit ve kolayca nakde çevrilebilen** bir para piyasası aracı/mevduat nakit benzeri sayılır. Uzun vadeli/likit olmayan kalemler nakit benzeri değildir.',
        'TMS 7 - nakit benzeri',
    ),
    # düzey 2
    '0050': patch(
        'Hisse senedi ihraç ederek (nominalin üzerinde) sağlanan nakit, nakit akım tablosunda hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetleri (nakit girişi)',
            'B': 'İşletme faaliyetleri (nakit çıkışı)',
            'C': 'Finansman faaliyetleri (nakit çıkışı)',
            'D': 'İşletme faaliyetleri (nakit girişi)',
            'E': 'Finansman faaliyetleri (nakit girişi)',
        },
        'E',
        'Hisse senedi ihracı özkaynak yapısını değiştirir → **finansman faaliyetleri** grubunda bir **nakit girişidir**.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0051': patch(
        'Aşağıdaki nakit akışlarından hangileri FİNANSMAN faaliyeti kapsamındadır?\n\nI. Ortaklara temettü ödemesi\n\nII. Maddi duran varlık alımı için ödeme\n\nIII. Tahvil ihracından sağlanan nakit',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'D',
        '**I (temettü ödemesi)** ve **III (tahvil ihracı)** finansman faaliyetidir. **II (MDV alımı)** ise yatırım faaliyetidir. Doğru cevap **I ve III**.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletmenin döneme ait bilgileri şöyledir: dönem net kârı 180.000 ₺, amortisman giderleri 50.000 ₺, ticari alacaklardaki artış 35.000 ₺, stoklardaki azalış 15.000 ₺, satıcılardaki artış 10.000 ₺. Dolaylı yönteme göre işletme faaliyetlerinden sağlanan nakit akışı kaç ₺'dir?",
        {
            'A': '220.000',
            'B': '200.000',
            'C': '170.000',
            'D': '210.000',
            'E': '120.000',
        },
        'A',
        'Net kâr 180.000 + amortisman (nakit çıkışı gerektirmez) 50.000 − alacak artışı 35.000 + stok azalışı 15.000 + satıcı borcu artışı 10.000 = **220.000 ₺**. Varlık artışı nakdi azaltır, borç artışı nakdi artırır.',
        'Mali analiz - nakit akış tablosu (dolaylı yöntem)',
    ),
    # düzey 2
    '0053': patch(
        "Bir işletmenin nakit akış tablosunda işletme faaliyetlerinden nakit akışı +400.000 ₺, yatırım faaliyetlerinden −120.000 ₺, finansman faaliyetlerinden −80.000 ₺'dir. Dönem başı nakit ve nakit benzerleri 150.000 ₺ olduğuna göre dönem sonu nakit ve nakit benzerleri kaç ₺'dir?",
        {
            'A': '550.000',
            'B': '190.000',
            'C': '750.000',
            'D': '350.000',
            'E': '200.000',
        },
        'D',
        'Net nakit artışı = 400.000 − 120.000 − 80.000 = 200.000 ₺. Dönem sonu = 150.000 + 200.000 = **350.000 ₺**.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0054': patch(
        "Bir işletmenin satışların maliyeti 500.000 ₺'dir. Dönemde stoklar 40.000 ₺, satıcılar (ticari borçlar) 25.000 ₺ artmıştır. Doğrudan yönteme göre tedarikçilere yapılan nakit ödeme kaç ₺'dir?",
        {
            'A': '435.000',
            'B': '485.000',
            'C': '515.000',
            'D': '540.000',
            'E': '565.000',
        },
        'C',
        'Alışlar = satışların maliyeti + stok artışı = 540.000 ₺. Ödeme = alışlar − satıcı borcu artışı = 540.000 − 25.000 = **515.000 ₺**.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdaki işlemlerden hangisi nakit akış tablosunda yer almaz, dipnotlarda açıklanır?',
        {
            'A': 'Makinenin peşin bedelle satın alınması',
            'B': 'Bankadan uzun vadeli kredi alınması',
            'C': 'Müşterilerden peşin tahsilat yapılması',
            'D': 'Ortaklara nakit kâr payı ödenmesi',
            'E': 'Bir binanın uzun vadeli borç karşılığında doğrudan satın alınması',
        },
        'E',
        'Binanın borç karşılığında edinilmesinde nakit girişi ya da çıkışı olmaz; önemli bir yatırım ve finansman işlemi olarak dipnotlarda açıklanır. Diğerlerinin hepsinde nakit hareketi vardır.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 2
    '0056': patch(
        'Bir işlemle ilgili hem nakit girişi hem nakit çıkışı söz konusu ise bu işlem nakit akış tablosunda genel kural olarak nasıl raporlanır?',
        {
            'A': 'Çıkış gösterilir, giriş dipnotta açıklanır.',
            'B': 'Girişler ve çıkışlar netleştirilerek tek tutar gösterilir.',
            'C': 'Girişler ve çıkışlar ayrı ayrı, brüt tutarlarıyla gösterilir.',
            'D': 'Giriş gösterilir, çıkış dipnotta açıklanır.',
            'E': 'İşlem nakit akış tablosuna alınmaz.',
        },
        'C',
        'Genel kural brüt raporlamadır: nakit girişleri ve çıkışları ayrı gösterilir. Netleştirme ancak devir hızı yüksek, tutarı büyük ve vadesi kısa kalemler gibi standardın izin verdiği sınırlı durumlarda yapılır.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0057': patch(
        'Dolaylı yöntemle işletme faaliyetlerinden nakit akışı hesaplanırken aşağıdakilerden hangisi dönem net kârına eklenir?',
        {
            'A': 'Peşin ödenmiş giderlerdeki artış',
            'B': 'Maddi duran varlık satış kârı',
            'C': 'Satıcılardaki azalış',
            'D': 'Ticari alacaklardaki artış',
            'E': 'Stoklardaki azalış',
        },
        'E',
        'Stok azalışı, maliyeti gider yazılan fakat bu dönem nakit ödenmeyen malı gösterir; kâra eklenir. Alacak ve peşin ödenmiş gider artışı, satıcı borcundaki azalış ve satış kârı ise kârdan düşülür.',
        'Mali analiz - nakit akış tablosu (dolaylı yöntem)',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletme dönemde bankadan 200.000 ₺ kredi almış, önceki kredilerin 120.000 ₺'lik anaparasını ödemiş, ortaklara 50.000 ₺ kâr payı dağıtmış ve 100.000 ₺ nakdi sermaye artırımı yapmıştır. Buna göre finansman faaliyetlerinden net nakit akışı kaç ₺'dir?",
        {
            'A': '470.000',
            'B': '130.000',
            'C': '230.000',
            'D': '180.000',
            'E': '30.000',
        },
        'B',
        '200.000 − 120.000 − 50.000 + 100.000 = **130.000 ₺**. Kâr payı ödemesini unutmak 180.000 ₺ verir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0059': patch(
        'Bir işletmenin nakit akış tablosunda işletme faaliyetlerinden nakit akışı negatif, finansman faaliyetlerinden nakit akışı pozitif ve yüksektir; yatırım faaliyetleri önemsizdir. Bu durum en çok neyi gösterir?',
        {
            'A': 'İşletme nakdini ağırlıkla yatırımlara ayırmıştır.',
            'B': 'İşletme esas faaliyetlerinden yüksek nakit yaratmıştır.',
            'C': 'İşletmenin dönem net kârı yüksektir.',
            'D': 'Esas faaliyetlerden doğan nakit açığı borçlanma ya da sermaye artırımıyla kapatılmıştır.',
            'E': 'İşletme borçlarını esas faaliyet nakdiyle geri ödemiştir.',
        },
        'D',
        'İşletme faaliyetleri nakit tüketmiş, açık dış kaynakla (finansman) karşılanmıştır. Bu durum uzun sürerse sürdürülebilir değildir.',
        'Mali analiz - nakit akış tablosu',
    ),
    # düzey 3
    '0060': patch(
        "Bir işletmenin döneme ait personel ücret giderleri 240.000 ₺'dir. Personele borçlar hesabının bakiyesi dönem başında 20.000 ₺, dönem sonunda 35.000 ₺'dir. Doğrudan yönteme göre personele yapılan nakit ödeme kaç ₺'dir?",
        {
            'A': '255.000',
            'B': '205.000',
            'C': '225.000',
            'D': '275.000',
            'E': '240.000',
        },
        'C',
        'Ödeme = dönem başı borç + dönem gideri − dönem sonu borç = 20.000 + 240.000 − 35.000 = **225.000 ₺**.',
        'Mali analiz - nakit akış tablosu',
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
    print(f"1 paket / {len(PATCHES)} soru ('Nakit Akim Analizi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
