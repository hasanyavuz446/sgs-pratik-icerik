#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 2 Stoklar — biçim kalibrasyonu (içerik kapsamı zaten tam).

ÖLÇÜLEN KUSURLAR (2026-07-28):
  · para birimi **TL** (13 soru) — §8 "₺ sembolü kullanılır" der; havuzda 847 soru
    ₺, 88 soru TL. tms_2 en kötüsü.
  · olumsuz kök **%0** — oysa gerçek sınav TMS 2'yi olumsuz kökle de soruyor:
    2016-18 s.39 "satın alma maliyetinin hesaplanmasında dikkate ALINMAZ",
    2014-16 s.39 "kullanılabilecek yöntemlerden biri DEĞİLDİR",
    1-2-3 s.52 "açıklamalardan hangisinin yapılması GEREKLİ DEĞİLDİR".
  · kök kalıbı **38/60 aynı** ("…bakımından aşağıdakilerden hangisi doğrudur?") —
    §2: "Aynı kök kalıbı + aynı çözüm + aynı çeldirici mantığı seri üretimde
    kullanılmaz."
  · hesap soruları **tek adımlı** — gerçek sınav çok verili senaryo kuruyor:
    2022 "Müge'nin kurabiyelerinin stok maliyeti kaç ₺" · 2025 pirinç NGD toplam
    değeri · 2023 s.49 180.000 ₺ mal, NGD 150.000 ₺ · 2024 kalem bazında ölçüm.

Bu tur içerik değil BİÇİM düzeltir; kapsam ve doğruluk korunur.
Dayanak: KGK TMS 2 par. 6, 9-10, 11-13, 15-18, 21-27, 28-33, 34-36.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_2_stoklar.json"
STYLE_REF = "SGS Muhasebe Standartlari TMS 2"

# §8: "₺ sembolü kullanılır". Bu pakette 13 soru TL kullaniyordu; yamalananlar
# zaten ₺ ile yazildi, yamalanmayanlar burada mekanik olarak cevrilir.
TL = re.compile(r"(\d)\s*TL\b")


def std_patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "TMS 2 Stoklar"},
        "validYear": 2026, "mockExamId": None,
    }


PATCHES = {
    'std-tms2-gen-0003': std_patch(
        "TMS 2'ye göre stoklar finansal durum tablosunda hangi değerle ölçülür?",
        {
            'A': 'Maliyet ile net gerçekleşebilir değerden yüksek olanıyla',
            'B': 'Her zaman maliyet bedeliyle',
            'C': 'Her zaman net gerçekleşebilir değeriyle',
            'D': 'Maliyet ile gerçeğe uygun değerden yüksek olanıyla',
            'E': 'Maliyet ile net gerçekleşebilir değerden düşük olanıyla',
        },
        'E',
        'TMS 2 par. 9: stoklar, maliyet ile net gerçekleşebilir değerden düşük olanı ile ölçülür. Bu ölçüm, stokun satışından elde edilecek tutarın defter değerinin altına düşmesi hâlinde varlığın olduğundan yüksek gösterilmesini engeller.',
    ),
    'std-tms2-gen-0004': std_patch(
        'Net gerçekleşebilir değer nasıl hesaplanır?',
        {
            'A': 'Olağan iş akışındaki tahmini satış fiyatına tamamlanma maliyetleri eklenerek',
            'B': 'Olağan iş akışındaki tahmini satış fiyatından tamamlanma ve satış maliyetleri düşülerek',
            'C': 'Piyasadaki cari alış fiyatından ticari iskontolar düşülerek',
            'D': 'Stokun defter değerinden birikmiş değer düşüklüğü düşülerek',
            'E': 'Tahmini satış fiyatından yalnızca satış vergileri düşülerek',
        },
        'B',
        'TMS 2 par. 6: net gerçekleşebilir değer, işletmenin olağan iş akışı içinde tahmini satış fiyatından, tamamlanma maliyeti ile satışı gerçekleştirmek için gerekli tahmini maliyetlerin düşülmesiyle bulunur.',
    ),
    'std-tms2-gen-0007': std_patch(
        "Aşağıdakilerden hangisi TMS 2'nin ölçüm hükümlerinin kapsamı dışındadır?",
        {
            'A': 'Olağan iş akışı içinde satılmak üzere elde tutulan ticari mallar',
            'B': 'Üretim sürecinde bulunan yarı mamuller',
            'C': 'Üretim sürecinde kullanılacak ilk madde ve malzemeler',
            'D': 'Hasılatı henüz muhasebeleştirilmemiş hizmetin maliyetleri',
            'E': 'Aracı tacirlerin gerçeğe uygun değerinden satış maliyeti düşülerek ölçtüğü stoklar',
        },
        'E',
        "TMS 2 par. 3: tarımsal ve orman ürünleri ile değerli madenlerde üretim sonrası ölçüm ve aracı tacirlerin gerçeğe uygun değerinden satış maliyeti düşülerek ölçtüğü stoklar, standardın ölçüm hükümlerinin dışındadır. Diğer şıklardaki kalemler par. 6'daki stok tanımına girer.",
    ),
    'std-tms2-gen-0010': std_patch(
        "Bir işletmenin dönem sonu stokunda 4.000 kg buğday bulunmaktadır. Stokun birim maliyeti 22 ₺, olağan iş akışındaki tahmini satış fiyatı 25 ₺/kg, tahmini tamamlanma maliyeti 2 ₺/kg ve tahmini satış gideri 1,5 ₺/kg'dir. TMS 2'ye göre bu stok finansal tablolarda kaç ₺ ile gösterilir?",
        {
            'A': '88.000 ₺',
            'B': '100.000 ₺',
            'C': '92.000 ₺',
            'D': '84.000 ₺',
            'E': '86.000 ₺',
        },
        'E',
        'Birim net gerçekleşebilir değer: 25 − 2 − 1,5 = 21,5 ₺. Toplam NGD: 4.000 × 21,5 = 86.000 ₺. Toplam maliyet: 4.000 × 22 = 88.000 ₺. TMS 2 par. 9 düşük olanı öngördüğünden stok 86.000 ₺ ile gösterilir; aradaki 2.000 ₺ değer düşüklüğü olarak gider yazılır.',
    ),
    'std-tms2-gen-0012': std_patch(
        "Aşağıdakilerden hangisi TMS 2'ye göre stokların satın alma maliyetinin hesaplanmasında dikkate alınmaz?",
        {
            'A': 'Satıcıdan alınan ticari iskonto',
            'B': 'Satın alma fiyatı',
            'C': 'İade alınamayan alış vergileri',
            'D': 'Nakliye ve sigorta giderleri',
            'E': 'Yükleme ve boşaltma maliyetleri',
        },
        'A',
        'TMS 2 par. 11: satın alma maliyeti; satın alma fiyatı, iade alınamayan vergiler, nakliye, yükleme-boşaltma ve doğrudan ilişkilendirilebilen diğer maliyetlerden oluşur. Ticari iskontolar ve benzeri indirimler maliyetin hesaplanmasında düşülür, eklenmez.',
    ),
    'std-tms2-gen-0014': std_patch(
        'Sabit genel üretim giderleri stok maliyetine hangi ölçüye göre dağıtılır?',
        {
            'A': 'Dönemdeki fiili üretim miktarına göre',
            'B': 'Tesisin teorik azami kapasitesine göre',
            'C': 'Direkt işçilik saatlerinin gerçekleşen toplamına göre',
            'D': 'Üretim tesislerinin normal kapasitesine göre',
            'E': 'Dönem satış hasılatına göre',
        },
        'D',
        'TMS 2 par. 13: sabit genel üretim giderleri, üretim tesislerinin normal kapasitesi esas alınarak dönüştürme maliyetlerine dağıtılır. Böylece düşük üretim dönemlerinde birim maliyet yapay olarak şişmez.',
    ),
    'std-tms2-gen-0017': std_patch(
        'Değişken genel üretim giderleri stok maliyetine hangi ölçüye göre dağıtılır?',
        {
            'A': 'Normal kapasiteye göre',
            'B': 'Üretim tesislerinin fiili kullanımına göre',
            'C': 'Teorik azami kapasiteye göre',
            'D': 'Dönem başı stok miktarına göre',
            'E': 'Satış hasılatına göre',
        },
        'B',
        'TMS 2 par. 13: değişken genel üretim giderleri, üretim tesislerinin fiili kullanımı esas alınarak her bir üretim birimine dağıtılır. Sabit giderlerden farklı olarak normal kapasite ölçütü kullanılmaz.',
    ),
    'std-tms2-gen-0018': std_patch(
        "Aşağıdakilerden hangisi TMS 2'ye göre stok maliyetine dâhil edilir?",
        {
            'A': 'Normalin üstündeki fire ve kayıp tutarları',
            'B': 'Stokları mevcut konumuna getirmeyle ilgisi olmayan genel yönetim giderleri',
            'C': 'Satış ve pazarlama giderleri',
            'D': 'Üretim tamamlandıktan sonraki depolama giderleri',
            'E': 'Üretim sürecinde sonraki bir aşama için katlanılan depolama gideri',
        },
        'E',
        'TMS 2 par. 16: normalin üstündeki fire, üretim aşaması gerektirmeyen depolama, stokları mevcut konum ve duruma getirmeyle ilgisi bulunmayan genel yönetim giderleri ile satış giderleri stok maliyetine alınmaz ve oluştukları dönemde gider yazılır. Sonraki üretim aşaması için gerekli depolama gideri ise maliyete dâhildir.',
    ),
    'std-tms2-gen-0020': std_patch(
        "Bir işletme ticari mal alımına ilişkin şu bilgilere sahiptir: liste fiyatı 400.000 ₺, satıcının uyguladığı ticari iskonto 30.000 ₺, iade alınamayan alış vergisi 24.000 ₺, nakliye ve sigorta gideri 16.000 ₺, malların depoya yerleştirilmesi için ödenen boşaltma bedeli 5.000 ₺, satış sonrası reklam gideri 12.000 ₺. TMS 2'ye göre stokun satın alma maliyeti kaç ₺'dir?",
        {
            'A': '415.000 ₺',
            'B': '427.000 ₺',
            'C': '445.000 ₺',
            'D': '410.000 ₺',
            'E': '391.000 ₺',
        },
        'A',
        'TMS 2 par. 11: satın alma fiyatından ticari iskonto düşülür, iade alınamayan vergiler ile nakliye, sigorta ve yükleme-boşaltma maliyetleri eklenir. 400.000 − 30.000 + 24.000 + 16.000 + 5.000 = 415.000 ₺. Reklam gideri satış gideridir; par. 16 uyarınca maliyete alınmaz.',
    ),
    'std-tms2-gen-0021': std_patch(
        "Bir işletme 260.000 ₺'lik ticari mal almış, ayrıca sonradan vergi idaresinden iade alınabilecek 47.000 ₺ vergi ile malı depoya taşıma için 12.000 ₺ ödemiştir. TMS 2'ye göre stokun maliyeti kaç ₺'dir?",
        {
            'A': '260.000 ₺',
            'B': '307.000 ₺',
            'C': '319.000 ₺',
            'D': '272.000 ₺',
            'E': '248.000 ₺',
        },
        'D',
        'TMS 2 par. 11: satın alma maliyeti, satın alma fiyatı ile iade alınamayan vergileri ve taşıma maliyetlerini içerir. Sonradan iade alınabilen vergiler maliyete dâhil edilmez. 260.000 + 12.000 = 272.000 ₺.',
    ),
    'std-tms2-gen-0022': std_patch(
        "Bir üretim işletmesinin sabit genel üretim gideri 480.000 ₺, normal kapasitesi 16.000 birim, dönemdeki fiili üretimi ise 12.000 birimdir. TMS 2'ye göre stok maliyetine dağıtılacak sabit genel üretim gideri ile dönem gideri yazılacak tutar sırasıyla kaç ₺'dir?",
        {
            'A': '360.000 ₺ ve 120.000 ₺',
            'B': '480.000 ₺ ve 0 ₺',
            'C': '120.000 ₺ ve 360.000 ₺',
            'D': '400.000 ₺ ve 80.000 ₺',
            'E': '360.000 ₺ ve 0 ₺',
        },
        'A',
        'TMS 2 par. 13: sabit genel üretim giderleri normal kapasite esas alınarak dağıtılır. Birim pay 480.000 / 16.000 = 30 ₺. Fiili üretime dağıtılan 12.000 × 30 = 360.000 ₺. Düşük üretim nedeniyle dağıtılmayan 480.000 − 360.000 = 120.000 ₺ stok maliyetine eklenmez; oluştuğu dönemde gider yazılır.',
    ),
    'std-tms2-gen-0023': std_patch(
        "Bir üretim işletmesinin dönem verileri şöyledir: üretime verilen direkt ilk madde ve malzeme 300.000 ₺, direkt işçilik 180.000 ₺, normal kapasiteye göre dağıtılan genel üretim gideri 90.000 ₺, normalin üstündeki fire 20.000 ₺, satış personeli ücreti 40.000 ₺. TMS 2'ye göre dönemin stok maliyeti kaç ₺'dir?",
        {
            'A': '590.000 ₺',
            'B': '630.000 ₺',
            'C': '610.000 ₺',
            'D': '570.000 ₺',
            'E': '550.000 ₺',
        },
        'D',
        'TMS 2 par. 10 ve 12: stok maliyeti satın alma ve dönüştürme maliyetlerinden oluşur; dönüştürme maliyeti direkt işçilik ile sistematik dağıtılan genel üretim giderlerini içerir. 300.000 + 180.000 + 90.000 = 570.000 ₺. Normalin üstündeki fire ve satış personeli ücreti par. 16 uyarınca maliyete alınmaz, dönem gideri yazılır.',
    ),
    'std-tms2-gen-0027': std_patch(
        'Aşağıdakilerden hangisi TMS 2 kapsamında kullanılabilecek stok maliyeti hesaplama yöntemlerinden biri değildir?',
        {
            'A': 'Son giren ilk çıkar yöntemi',
            'B': 'İlk giren ilk çıkar yöntemi',
            'C': 'Ağırlıklı ortalama maliyet yöntemi',
            'D': 'Özel tanımlama (gerçek parti maliyeti) yöntemi',
            'E': 'Perakende yöntemi',
        },
        'A',
        'TMS 2 par. 23-25: normal şartlarda birbirinin yerine geçebilen stoklarda ilk giren ilk çıkar veya ağırlıklı ortalama; ikame edilemeyen ve özel projelere ayrılan stoklarda özel tanımlama kullanılır. Par. 21-22 perakende ve standart maliyet yöntemlerine kolaylık tekniği olarak izin verir. Son giren ilk çıkar (LIFO) standarttan çıkarılmıştır.',
    ),
    'std-tms2-gen-0030': std_patch(
        'İlk giren ilk çıkar yönteminde dönem sonu stok hangi maliyetlerden oluşur?',
        {
            'A': 'En önce alınan stokların maliyetlerinden',
            'B': 'En son alınan veya üretilen stokların maliyetlerinden',
            'C': 'Dönem içi alışların basit ortalamasından',
            'D': 'Dönem başı stokun birim maliyetinden',
            'E': 'En düşük birim maliyetli alışlardan',
        },
        'B',
        'TMS 2 par. 27: ilk giren ilk çıkar yönteminde ilk alınan stokların ilk satıldığı varsayılır; bu nedenle dönem sonunda kalan stoklar en son alınan veya üretilenlerden oluşur.',
    ),
    'std-tms2-gen-0031': std_patch(
        'Ağırlıklı ortalama maliyet yönteminde birim maliyet nasıl belirlenir?',
        {
            'A': 'Yalnızca dönem içi alımların ortalaması alınarak',
            'B': 'En son alışın birim fiyatı esas alınarak',
            'C': 'Dönem başı stokun birim fiyatı esas alınarak',
            'D': 'Alış fiyatlarının basit aritmetik ortalaması alınarak',
            'E': 'Dönem başı stok ile dönem içi alımların toplam maliyeti toplam miktara bölünerek',
        },
        'E',
        'TMS 2 par. 27: ağırlıklı ortalama maliyet yönteminde birim maliyet, dönem başı stok ile dönem içinde alınan veya üretilen benzer stokların ağırlıklı ortalaması alınarak belirlenir. Ortalama dönemsel olarak veya her ilave sevkiyatta hesaplanabilir.',
    ),
    'std-tms2-gen-0033': std_patch(
        "Bir işletmenin hammadde hareketleri şöyledir: dönem başı 200 birim × 40 ₺, 5 Mart alışı 300 birim × 50 ₺, 18 Mart alışı 200 birim × 60 ₺. Dönem içinde üretime 600 birim verilmiştir. İlk giren ilk çıkar yöntemine göre üretime verilen malzemenin maliyeti kaç ₺'dir?",
        {
            'A': '29.000 ₺',
            'B': '30.000 ₺',
            'C': '31.000 ₺',
            'D': '26.000 ₺',
            'E': '33.000 ₺',
        },
        'A',
        'İlk giren ilk çıkar yönteminde önce alınanlar önce çıkar: 200 × 40 = 8.000 ₺, ardından 300 × 50 = 15.000 ₺, kalan 100 birim son alıştan 100 × 60 = 6.000 ₺. Toplam 8.000 + 15.000 + 6.000 = 29.000 ₺. Dönem sonunda 100 birim × 60 = 6.000 ₺ stok kalır. Ağırlıklı ortalama uygulansaydı 35.000 / 700 = 50 ₺ birim maliyetle 30.000 ₺, son giren ilk çıkar uygulansaydı 31.000 ₺ bulunurdu.',
    ),
    'std-tms2-gen-0034': std_patch(
        "Bir işletmenin hammadde hareketleri şöyledir: dönem başı 500 birim × 36 ₺, 8 Nisan alışı 700 birim × 44 ₺, 22 Nisan alışı 800 birim × 50 ₺. Dönem içinde üretime 1.600 birim verilmiştir. Ağırlıklı ortalama maliyet yöntemine göre üretime verilen malzemenin maliyeti kaç ₺'dir?",
        {
            'A': '68.800 ₺',
            'B': '74.400 ₺',
            'C': '71.040 ₺',
            'D': '72.000 ₺',
            'E': '88.800 ₺',
        },
        'C',
        'Toplam maliyet: 500×36 + 700×44 + 800×50 = 18.000 + 30.800 + 40.000 = 88.800 ₺. Toplam miktar 2.000 birim. Ağırlıklı ortalama birim maliyet 88.800 / 2.000 = 44,40 ₺. Üretime verilen 1.600 × 44,40 = 71.040 ₺ (TMS 2 par. 27). İlk giren ilk çıkar uygulansaydı 68.800 ₺, son giren ilk çıkar uygulansaydı 74.400 ₺ bulunurdu; 88.800 ₺ ise kalan 400 birimlik stokun düşülmediği toplam alış maliyetidir.',
    ),
    'std-tms2-gen-0035': std_patch(
        "Bir işletmenin dönem başı stoku 400 birim × 45 ₺, dönem içi alışı 600 birim × 55 ₺'dir. Dönem içinde 700 birim satılmıştır. Ağırlıklı ortalama maliyet yöntemine göre dönem sonu stokunun değeri kaç ₺'dir?",
        {
            'A': '16.500 ₺',
            'B': '13.500 ₺',
            'C': '15.000 ₺',
            'D': '15.300 ₺',
            'E': '18.000 ₺',
        },
        'D',
        'Toplam maliyet: 400×45 + 600×55 = 18.000 + 33.000 = 51.000 ₺. Toplam miktar 1.000 birim. Ağırlıklı ortalama birim maliyet 51.000 / 1.000 = 51 ₺. Dönem sonu stok 1.000 − 700 = 300 birim; değeri 300 × 51 = 15.300 ₺.',
    ),
    'std-tms2-gen-0041': std_patch(
        'Bir stokun maliyeti net gerçekleşebilir değerinin üzerindeyse ne yapılır?',
        {
            'A': 'Stok maliyet bedeliyle taşınmaya devam eder',
            'B': 'Fark gelecek dönemlere yayılarak itfa edilir',
            'C': 'Fark doğrudan özkaynaklardan indirilir',
            'D': 'Stok net gerçekleşebilir değere indirgenir ve fark dönem gideri yazılır',
            'E': 'Stok net gerçekleşebilir değere indirgenir ve fark diğer kapsamlı gelire alınır',
        },
        'D',
        'TMS 2 par. 9 ve 34: maliyetin net gerçekleşebilir değerin üzerinde kalması hâlinde stok net gerçekleşebilir değere indirgenir; indirgeme tutarı, indirgemenin yapıldığı dönemde gider olarak muhasebeleştirilir.',
    ),
    'std-tms2-gen-0042': std_patch(
        'Net gerçekleşebilir değere indirgeme hangi düzeyde yapılır?',
        {
            'A': 'Her zaman stokların tamamı üzerinden toplu olarak',
            'B': 'Yalnızca ders veya ürün grubu düzeyinde',
            'C': 'Genellikle her bir stok kalemi bazında',
            'D': 'İşletmenin faaliyet bölümleri düzeyinde',
            'E': 'Yalnızca dönem sonunda tek seferde ve toplam üzerinden',
        },
        'C',
        'TMS 2 par. 29: indirgeme genellikle her bir stok kalemi bazında yapılır. Benzer veya birbiriyle ilişkili kalemlerin gruplanması bazı durumlarda uygun olabilir; ancak stokların tümü ya da bir faaliyet bölümüne ait tüm stoklar üzerinden toplu değerlendirme yapılamaz.',
    ),
    'std-tms2-gen-0043': std_patch(
        'Üretimde kullanılacak ilk madde ve malzemenin piyasa fiyatı düşmüş, ancak bunlarla üretilecek mamullerin maliyetin üzerinde satılması bekleniyorsa ne yapılır?',
        {
            'A': 'İlk madde ve malzeme piyasa fiyatına indirgenir',
            'B': 'İlk madde ve malzeme yerine mamul stoku indirgenir',
            'C': 'Fark gelecek dönem maliyetlerine aktarılır',
            'D': 'İlk madde ve malzeme gerçeğe uygun değerine yükseltilir',
            'E': 'İlk madde ve malzeme değer düşüklüğüne uğratılmaz; maliyetle taşınmaya devam eder',
        },
        'E',
        'TMS 2 par. 32: mamullerin maliyetin üzerinde satılması bekleniyorsa, üretimde kullanılacak ilk madde ve malzeme maliyetin altına indirgenmez. Malzeme fiyatındaki düşüş mamul maliyetinin geri kazanılamayacağını gösteriyorsa indirgeme yapılır.',
    ),
    'std-tms2-gen-0044': std_patch(
        'Önceki dönemde yapılmış bir değer düşüklüğü indirgemesi hangi sınıra kadar iptal edilebilir?',
        {
            'A': 'Yeni net gerçekleşebilir değere kadar sınırsız biçimde',
            'B': 'İndirgeme tutarının yarısına kadar',
            'C': 'Stokun orijinal maliyetini aşmayacak tutara kadar',
            'D': 'İptal yapılamaz; indirgeme kalıcıdır',
            'E': 'Stokun tahmini satış fiyatına kadar',
        },
        'C',
        'TMS 2 par. 33: net gerçekleşebilir değeri artıran koşullar oluştuğunda önceki indirgeme iptal edilir; iptal sonrası yeni defter değeri, maliyet ile yeni net gerçekleşebilir değerin düşük olanını aşamaz. Yani stok orijinal maliyetinin üzerine çıkarılamaz.',
    ),
    'std-tms2-gen-0045': std_patch(
        "Aşağıdakilerden hangisi TMS 2'ye göre stokların gider olarak muhasebeleştirilmesi bakımından yanlıştır?",
        {
            'A': 'Satılan stokun defter değeri, satışın yapıldığı dönemden bağımsız olarak dönem sonunda toplu yazılır',
            'B': 'Stok satıldığında defter değeri, hasılatın muhasebeleştirildiği dönemde gider yazılır',
            'C': 'Net gerçekleşebilir değere indirgemeden doğan tutar, indirgemenin yapıldığı dönemde gider yazılır',
            'D': 'İndirgemenin iptalinden doğan tutar, iptalin gerçekleştiği dönemde gider tutarından düşülür',
            'E': 'Başka bir varlığın maliyetine dağıtılan stoklar, o varlığın ömrü boyunca gider yazılır',
        },
        'A',
        'TMS 2 par. 34-35: stok satıldığında defter değeri, ilgili hasılatın muhasebeleştirildiği dönemde gider olarak kaydedilir — dönemsellik ve eşleştirme gereği. Toplu dönem sonu yazımı bu ilkeye aykırıdır.',
    ),
    'std-tms2-gen-0046': std_patch(
        "Bir işletmenin dönem sonu stokları üç kalemden oluşmaktadır: A malı maliyet 120.000 ₺ / net gerçekleşebilir değer 135.000 ₺; B malı maliyet 90.000 ₺ / net gerçekleşebilir değer 74.000 ₺; C malı maliyet 60.000 ₺ / net gerçekleşebilir değer 55.000 ₺. Stoklar kalem bazında değerlendiğine göre finansal durum tablosunda gösterilecek toplam tutar kaç ₺'dir?",
        {
            'A': '270.000 ₺',
            'B': '264.000 ₺',
            'C': '249.000 ₺',
            'D': '255.000 ₺',
            'E': '244.000 ₺',
        },
        'C',
        'TMS 2 par. 29: net gerçekleşebilir değere indirgeme genellikle her bir stok kalemi bazında yapılır. A: düşük olan 120.000 ₺; B: 74.000 ₺; C: 55.000 ₺. Toplam 120.000 + 74.000 + 55.000 = 249.000 ₺. Kalemlerin toplamı üzerinden karşılaştırma yapmak (270.000 ↔ 264.000) standarda aykırıdır.',
    ),
    'std-tms2-gen-0047': std_patch(
        "Maliyeti 36.000 ₺ olan bir mamulün tahmini satış fiyatı 40.000 ₺, tamamlanma maliyeti 2.000 ₺ ve satış gideri 3.000 ₺'dir. TMS 2'ye göre yapılacak işlem aşağıdakilerden hangisidir?",
        {
            'A': 'Stok 36.000 ₺ ile taşınmaya devam eder; işlem yapılmaz',
            'B': "Stok 38.000 ₺'ye indirgenir ve 2.000 ₺ gider yazılır",
            'C': "Stok 40.000 ₺'ye yükseltilir ve 4.000 ₺ kazanç yazılır",
            'D': "Stok 35.000 ₺'ye indirgenir; fark doğrudan özkaynağa alınır",
            'E': "Stok 35.000 ₺'ye indirgenir ve 1.000 ₺ gider yazılır",
        },
        'E',
        "Net gerçekleşebilir değer: 40.000 − 2.000 − 3.000 = 35.000 ₺. Maliyet 36.000 ₺ bunun üzerindedir; TMS 2 par. 9 ve 34 uyarınca stok 35.000 ₺'ye indirgenir ve 1.000 ₺ fark indirgemenin yapıldığı dönemde gider olarak muhasebeleştirilir.",
    ),
    'std-tms2-gen-0048': std_patch(
        "Maliyeti 90.000 ₺ olan bir stok, önceki dönemde net gerçekleşebilir değeri 72.000 ₺'ye düştüğü için indirgenmiştir. Cari dönemde koşullar iyileşmiş ve net gerçekleşebilir değer 96.000 ₺'ye yükselmiştir. TMS 2'ye göre stok cari dönem sonunda kaç ₺ ile ölçülür ve kaç ₺ iptal kaydedilir?",
        {
            'A': '96.000 ₺ ile ölçülür; 24.000 ₺ iptal edilir',
            'B': '72.000 ₺ ile ölçülür; iptal kaydedilmez',
            'C': '90.000 ₺ ile ölçülür; 18.000 ₺ iptal edilir',
            'D': '90.000 ₺ ile ölçülür; 6.000 ₺ iptal edilir',
            'E': '96.000 ₺ ile ölçülür; 18.000 ₺ iptal edilir',
        },
        'C',
        "TMS 2 par. 33: koşullar değiştiğinde önceki indirgeme iptal edilir; ancak yeni defter değeri maliyet ile yeni net gerçekleşebilir değerin düşük olanını aşamaz. Maliyet 90.000 ₺, NGD 96.000 ₺ olduğundan stok 90.000 ₺ ile ölçülür; iptal tutarı 90.000 − 72.000 = 18.000 ₺'dir.",
    ),
    'std-tms2-gen-0052': std_patch(
        "Aşağıdakilerden hangisinin TMS 2'ye göre dipnotlarda açıklanması gerekli değildir?",
        {
            'A': 'Stokların ölçümünde benimsenen muhasebe politikaları ve maliyet hesaplama yöntemi',
            'B': 'Stokların toplam defter değeri ve uygun sınıflar itibarıyla dağılımı',
            'C': 'Stokların tedarik edildiği satıcıların ticaret unvanları',
            'D': 'Dönem içinde gider olarak muhasebeleştirilen stok tutarı',
            'E': 'Net gerçekleşebilir değere indirgeme ve iptal tutarları ile iptali gerektiren koşullar',
        },
        'C',
        'TMS 2 par. 36: açıklanacaklar; muhasebe politikaları ve maliyet yöntemi, toplam defter değeri ve sınıflara göre dağılım, gerçeğe uygun değerinden satış maliyeti düşülerek ölçülen stoklar, dönem gideri yazılan tutar, indirgeme ve iptal tutarları ile bunların koşullarıdır. Satıcı unvanları standartta yer almaz.',
    ),
    'std-tms2-gen-0053': std_patch(
        'Stok maliyetine alınmayan giderler ne zaman muhasebeleştirilir?',
        {
            'A': 'Oluştukları dönemde gider olarak',
            'B': 'İlgili stok satıldığında gider olarak',
            'C': 'Stokun kalan ömrüne yayılarak',
            'D': 'Doğrudan özkaynaklardan indirim olarak',
            'E': 'Dönem sonunda stok maliyetine eklenerek',
        },
        'A',
        'TMS 2 par. 16-18: normalin üstündeki fire, gereksiz depolama, ilgisiz genel yönetim ve satış giderleri stok maliyetine alınmaz; oluştukları dönemde gider olarak muhasebeleştirilir. Satışa bağlanmaz, ertelenmez.',
    ),
    'std-tms2-gen-0055': std_patch(
        'Net gerçekleşebilir değer tahmininde hangi bilgiler esas alınır?',
        {
            'A': 'Tahmin tarihinde mevcut en güvenilir kanıtlar ile dönem sonu sonrası olayların doğruladığı bilgiler',
            'B': 'Yalnızca dönem sonu tarihindeki liste fiyatları',
            'C': 'Yalnızca stokun alış tarihindeki piyasa koşulları',
            'D': 'İşletmenin gelecek üç yıla ilişkin bütçe tahminleri',
            'E': 'Yalnızca bağımsız değerleme kuruluşunun raporu',
        },
        'A',
        'TMS 2 par. 30-31: net gerçekleşebilir değer tahmini, tahminin yapıldığı tarihte mevcut en güvenilir kanıtlara dayanır. Dönem sonundan sonra ortaya çıkan ve dönem sonundaki koşulları doğrulayan olaylar da dikkate alınır.',
    ),
    'std-tms2-gen-0056': std_patch(
        'Kesin bir satış sözleşmesine bağlanmış stoklarda net gerçekleşebilir değer neye göre belirlenir?',
        {
            'A': 'Dönem sonundaki genel piyasa fiyatına göre',
            'B': 'Sözleşme fiyatına göre',
            'C': 'Stokun alış maliyetine göre',
            'D': 'Sözleşme fiyatı ile piyasa fiyatının yüksek olanına göre',
            'E': 'Rakip işletmelerin satış fiyatlarına göre',
        },
        'B',
        'TMS 2 par. 31: elde bulunan stok miktarını aşmayan kesin satış sözleşmelerine konu stoklarda net gerçekleşebilir değer sözleşme fiyatı esas alınarak belirlenir. Sözleşme miktarını aşan kısım için genel satış fiyatları kullanılır.',
    ),
    'std-tms2-gen-0057': std_patch(
        'Net gerçekleşebilir değer ne sıklıkla yeniden değerlendirilir?',
        {
            'A': 'Yalnızca stok satıldığında',
            'B': 'Her raporlama döneminde',
            'C': 'Yalnızca değer düşüklüğü ilk kez oluştuğunda',
            'D': 'Üç yılda bir',
            'E': 'Yalnızca işletme yönetimi talep ettiğinde',
        },
        'B',
        'TMS 2 par. 33: stoklar sonraki her dönemde net gerçekleşebilir değer açısından yeniden değerlendirilir. Değeri düşüren koşullar ortadan kalkmışsa önceki indirgeme iptal edilir.',
    ),
    'std-tms2-gen-0058': std_patch(
        'Aşağıdakilerden hangisi hizmet sunan bir işletmenin stok maliyetine dâhil edilmez?',
        {
            'A': 'Satış ve genel yönetim personelinin ücretleri',
            'B': 'Hizmeti doğrudan sunan personelin ücretleri',
            'C': 'Hizmeti doğrudan sunan personelin gözetiminde çalışanların ücretleri',
            'D': 'Hizmet sunumuyla doğrudan ilişkili genel giderler',
            'E': 'Hizmeti doğrudan sunan personele ilişkin sosyal güvenlik yükleri',
        },
        'A',
        'TMS 2 par. 19: hizmet sunan işletmelerde stok maliyeti; hizmeti sunan personelin ücretleri, gözetim personeli giderleri ve ilgili genel giderlerden oluşur. Satış ve genel yönetim personelinin ücretleri maliyete alınmaz, gider olarak muhasebeleştirilir.',
    ),
    'std-tms2-gen-0059': std_patch(
        "Bir işletme liste fiyatı 150.000 ₺ olan ticari malı %10 ticari iskonto ile satın almıştır. Ayrıca sonradan vergi idaresinden iade alınabilecek 27.000 ₺ vergi ödenmiş, nakliye için 8.000 ₺ harcanmıştır. TMS 2'ye göre stokun maliyeti kaç ₺'dir?",
        {
            'A': '170.000 ₺',
            'B': '143.000 ₺',
            'C': '158.000 ₺',
            'D': '135.000 ₺',
            'E': '165.000 ₺',
        },
        'B',
        'Ticari iskonto düşülür: 150.000 × %10 = 15.000 ₺ indirim, kalan 135.000 ₺. Nakliye eklenir: 135.000 + 8.000 = 143.000 ₺. TMS 2 par. 11 uyarınca sonradan iade alınabilen vergiler maliyete dâhil edilmez.',
    ),
}


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
    for q in questions:
        yeni_stem = TL.sub(r"\1 ₺", q["stem"])
        yeni_coz = TL.sub(r"\1 ₺", q["solution"])
        yeni_opt = {L: TL.sub(r"\1 ₺", v) for L, v in q["options"].items()}
        if (yeni_stem, yeni_coz, yeni_opt) != (q["stem"], q["solution"], q["options"]):
            fark.append(f"{path}::{q['id']} TL→₺")
            if write:
                q["stem"], q["solution"], q["options"] = yeni_stem, yeni_coz, yeni_opt
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
    print(f"1 paket / {len(PATCHES)} soru (TMS 2 bicim kalibrasyonu) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
