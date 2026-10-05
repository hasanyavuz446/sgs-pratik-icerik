#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Oran Analizi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Mali tablolar analizi tablolu tur. Gercek sinavin ~75/144 MTA sorusu oran analizinden ve hep oran zincirinden geriye hesap istiyor (cari + duran/devamli sermaye -> KVYK, nakit orani -> donen varlik, DuPont, PD/DD, kaldirac sinirindan kredi limiti, islemlerin oranlara etkisi); eski paket formul + tek islemdi (medyan kok 106). 9 kavram sorusu korundu (mutlak ifadeli celdiriciler yenilendi); sinavin 'finansal kaldirac = yabanci kaynak/aktif' tanimiyla celisen borc/ozkaynak sorulari cikarildi. 51 yeni soru her biri kendi verisiyle: likidite ve calisma sermayesi 17, mali yapi 11, devir hizlari 8, karlilik/DuPont/gelir tablosu 10, piyasa oranlari 4, genel 1. Oranlar Fraction ile hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Mali tablolar analizi - oran analizi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/mali_tablolar_analizi/oran_analizi.json"
STYLE_REF = 'SGS Mali Tablolar Analizi (oran zinciri, ters hesap; gerçek sınav profiline kalibre)'
ONEK = "mta-oran-gen-"


def patch(stem, options, answer, solution, ref='Mali analiz - oran analizi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Asit-test oranının hesabında stokların dönen varlıklardan düşülmesinin nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Stokların dönen varlıklar içindeki en likit kalem olması ve nakde en hızlı dönüşen değer sayılması nedeniyle dışlanması gerekmesi',
            'B': 'Stokların özkaynaklar grubunda izlenen ve ortakların işletmeye koyduğu sermayeyi temsil eden bir kalem sayılması',
            'C': 'Stokların nakde dönüşmesinin diğer dönen varlıklara göre daha uzun ve belirsiz olması (en az likit dönen varlık olması)',
            'D': 'Stokların bilançoda kısa vadeli yabancı kaynaklar arasında gösterilen bir borç kalemi olarak sınıflandırılması',
            'E': 'Stokların bilançoda dönen varlık değil duran varlık grubunda raporlanan bir kalem olması ve bu yüzden hesaba katılmaması',
        },
        'C',
        'Stoklar, satılıp tahsil edilene kadar nakde dönüşmesi daha **uzun ve belirsiz** olan (en az likit) dönen varlıktır. Bu nedenle asit-testte dışlanarak daha ihtiyatlı bir likidite ölçüsü elde edilir.',
        'Mali analiz - asit-test oranı',
    ),
    # düzey 2
    '0002': patch(
        'Bir işletmenin kaldıraç oranının (yabancı kaynak/toplam varlık) yüksek olması genel olarak neyi gösterir?',
        {
            'A': 'İşletmenin dönen varlıklarının kısa vadeli borçlarını birkaç kez karşılayacak kadar yüksek olduğunu ve likiditenin güçlü olduğunu gösterir.',
            'B': 'İşletmenin en likit varlıklarının kısa vadeli borçlarını fazlasıyla karşıladığını ve nakit likiditesinin çok yüksek olduğunu gösterir.',
            'C': 'İşletmenin varlıklarını ağırlıkla özkaynakla finanse ettiğini; borç yükünün ve finansal riskin oldukça düşük bir düzeyde kaldığını gösterir.',
            'D': 'İşletmenin varlıklarını ağırlıkla yabancı kaynakla (borçla) finanse ettiğini; finansal riskin ve faiz yükünün göreli olarak yüksek olduğunu',
            'E': 'İşletmenin dönen varlıklarıyla kısa vadeli borçlarını rahatça karşıladığını ve kısa vadeli ödeme gücünün mükemmel olduğunu gösterir.',
        },
        'D',
        'Yüksek kaldıraç oranı, varlıkların büyük ölçüde **yabancı kaynakla (borçla)** finanse edildiğini gösterir; bu da **finansal risk ve faiz yükünün** göreli olarak yüksek olduğuna işaret eder.',
        'Mali analiz - kaldıraç yorumu',
    ),
    # düzey 2
    '0003': patch(
        'Aşağıdaki oranlardan hangileri kârlılık oranıdır?\n\nI. Net kâr marjı\n\nII. Cari oran\n\nIII. Aktif kârlılığı (ROA)',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'A',
        '**II yanlıştır:** Cari oran bir **likidite** oranıdır (Dönen Varlıklar ÷ KVYK); kârlılık oranı değildir. **I** net kâr marjı ve **III** aktif kârlılığı (ROA) ise kârlılık oranlarıdır. Doğru cevap **I ve III**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletmenin cari oranı 2,50, likidite (asit-test) oranı 0,90'dur. Stoklarının değeri 48.000 ₺ olduğuna göre kısa vadeli yabancı kaynaklar toplamı kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '40.800',
            'C': '76.800',
            'D': '33.000',
            'E': '30.000',
        },
        'E',
        'Cari oran − asit-test oranı = stoklar ÷ KVYK → 2,50 − 0,90 = 1,60 = 48.000 ÷ KVYK → KVYK = **30.000 ₺**. (Dönen varlıklar 75.000 ₺.)',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0005': patch(
        "Bir işletmenin dönem sonu bilançosunda brüt çalışma sermayesi 90.000 ₺ ve cari oranı 2,50'tir. Aynı tarihte menkul kıymetler 10.800 ₺, hazır değerler 5.400 ₺'dir. Buna göre işletmenin nakit oranı kaçtır?",
        {
            'A': '0,15',
            'B': '0,45',
            'C': '0,30',
            'D': '0,18',
            'E': '2,05',
        },
        'B',
        'Brüt çalışma sermayesi dönen varlıkların toplamıdır. KVYK = 90.000 ÷ 2,50 = 36.000 ₺. Nakit oranı = (5.400 + 10.800) ÷ 36.000 = **0,45**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0006': patch(
        'Cari oranı 2,40 ve asit-test oranı 0,80 olan bir işletme için aşağıdakilerden hangisi kesinlikle doğrudur?',
        {
            'A': 'Stoklar, kısa vadeli yabancı kaynakların 1,6 katıdır.',
            'B': 'İşletme kısa vadeli borçlarını stok satmadan tamamen ödeyebilir.',
            'C': 'Stoklar, dönen varlıkların yarısıdır.',
            'D': "Nakit oranı en az 0,80'dir.",
            'E': 'Net çalışma sermayesi negatiftir.',
        },
        'A',
        "Cari − asit-test = stoklar ÷ KVYK = 2,40 − 0,80 = **1,60**. Stoklar dönen varlıkların 1,6 ÷ 2,4 = 2/3'üdür. Cari oran 1'den büyük olduğundan NÇS pozitiftir. Nakit oranı asit-test oranından büyük olamaz (en fazla 0,80). Asit-test 1'in altında olduğundan borçların tamamı stok satılmadan ödenemez.",
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletmenin bilanço verileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Hazır değerler | 12.000 |\n| Menkul kıymetler | 8.000 |\n| Kısa vadeli ticari alacaklar | 30.000 |\n| Stoklar | 50.000 |\n| Kısa vadeli yabancı kaynaklar | 100.000 |\n\nBuna göre işletmenin stok bağımlılık oranı kaçtır?',
        {
            'A': '1,50',
            'B': '2',
            'C': '1,60',
            'D': '1',
            'E': '1,40',
        },
        'D',
        'Stok bağımlılık oranı = [KVYK − (hazır değerler + menkul kıymetler + kısa vadeli alacaklar)] ÷ stoklar = (100.000 − 50.000) ÷ 50.000 = **1**. Kısa vadeli borçların, stoklar dışındaki likit varlıklarla karşılanamayan kısmının stoklara oranıdır.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 2
    '0008': patch(
        'Bilanço kalemleri arasındaki aşağıdaki ilişkilerin hangisinde net çalışma sermayesi kesinlikle negatiftir?',
        {
            'A': 'Stoklar, kısa vadeli yabancı kaynaklardan küçüktür.',
            'B': 'Özkaynaklar, duran varlıklardan büyüktür.',
            'C': 'Duran varlıklar, devamlı (sürekli) sermayeden büyüktür.',
            'D': 'Hazır değerler, kısa vadeli yabancı kaynaklardan küçüktür.',
            'E': 'Uzun vadeli yabancı kaynaklar, özkaynaklardan büyüktür.',
        },
        'C',
        "Dönen varlıklar + duran varlıklar = KVYK + devamlı sermaye olduğundan NÇS = dönen varlıklar − KVYK = devamlı sermaye − duran varlıklar. Duran varlıklar devamlı sermayeden büyükse NÇS kesinlikle negatiftir. Diğer ilişkiler NÇS'nin işaretini tek başına belirlemez.",
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 2
    '0009': patch(
        'Aşağıdakilerden hangisi bir işletmenin likidite durumu hakkında bilgi vermez?',
        {
            'A': 'Nakit oranı',
            'B': 'Cari oran',
            'C': 'Net çalışma sermayesi',
            'D': 'Asit-test oranı',
            'E': 'Aktif kârlılık oranı',
        },
        'E',
        'Aktif kârlılık oranı (net kâr ÷ toplam varlıklar) bir kârlılık oranıdır. Cari, asit-test ve nakit oranı ile net çalışma sermayesi kısa vadeli borç ödeme gücünü ölçer.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0010': patch(
        "Toplam aktifleri 12.000.000 ₺ ve toplam borçları 5.000.000 ₺ olan bir firma bankadan kısa vadeli nakdî kredi talep etmiştir. Banka, finansal kaldıraç oranını %60'ın üzerine çıkarmayacak tutarda kredi verebileceğini bildirmiştir. Buna göre firma en fazla kaç ₺ kredi kullanabilir?",
        {
            'A': '7.000.000',
            'B': '5.500.000',
            'C': '2.200.000',
            'D': '7.200.000',
            'E': '2.000.000',
        },
        'B',
        'Kredi x olsun; nakit girdiği için hem borç hem aktif x kadar artar: (5.000.000 + x) ÷ (12.000.000 + x) = 0,60 → 5.000.000 + x = 7.200.000 + 0,6x → 0,4x = 2.200.000 → x = **5.500.000 ₺**. Aktifteki artışı unutmak 2.200.000 ₺ verir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0011': patch(
        "Aktif devir hızı 2,50, net satışları 750.000 ₺ ve finansal kaldıraç oranı 0,35 olan bir işletmenin özkaynakları kaç ₺'dir?",
        {
            'A': '487.500',
            'B': '105.000',
            'C': '300.000',
            'D': '262.500',
            'E': '195.000',
        },
        'E',
        'Aktif = 750.000 ÷ 2,50 = 300.000 ₺. Finansal kaldıraç 0,35 → yabancı kaynaklar 105.000 ₺. Özkaynaklar = 300.000 × (1 − 0,35) = **195.000 ₺**.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletmenin duran varlıklarının devamlı (sürekli) sermayeye oranı 0,80 ve kısa vadeli yabancı kaynakların pasif toplamına oranı %25'tir. Buna göre işletmenin cari oranı kaçtır?",
        {
            'A': '2,40',
            'B': '2',
            'C': '1,60',
            'D': '3,20',
            'E': '0,80',
        },
        'C',
        'Pasif 100 birim olsun: KVYK 25, devamlı sermaye 75. Duran varlıklar = 0,80 × 75 = 60; dönen varlıklar = 100 − 60 = 40. Cari oran = 40 ÷ 25 = **1,60**.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0013': patch(
        'Özkaynakları dönen varlıklarından daha fazla olan bir işletme için aşağıdakilerden hangisi kesinlikle doğrudur?',
        {
            'A': "Finansal kaldıraç oranı %50'nin altındadır.",
            'B': "Cari oranı 1'den büyüktür.",
            'C': 'Kısa vadeli yabancı kaynakları uzun vadeli yabancı kaynaklarından azdır.',
            'D': 'Duran varlıkları toplam yabancı kaynaklarından fazladır.',
            'E': 'Net çalışma sermayesi negatiftir.',
        },
        'D',
        'Dönen + duran = yabancı kaynaklar + özkaynaklar. Özkaynaklar dönen varlıklardan büyükse eşitliğin kalan kısmında duran varlıklar yabancı kaynaklardan büyük olmak zorundadır. Diğer ifadeler bu bilgiyle kesinleşmez.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0014': patch(
        'Bir işletmenin döneme ait bilgileri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Dönem başı stoklar | 400.000 |\n| Dönem başı ticari alacaklar | 700.000 |\n| Brüt satış kârı | 3.600.000 |\n| Dönem sonu ticari alacaklar | 800.000 |\n| Dönem sonu stoklar | 500.000 |\n| Net satışlar | 9.000.000 |\n\nBuna göre işletmenin stok devir hızı kaçtır?',
        {
            'A': '12',
            'B': '16',
            'C': '13,50',
            'D': '20',
            'E': '13,20',
        },
        'A',
        'Satışların maliyeti = 9.000.000 − 3.600.000 = 5.400.000 ₺. Ortalama stok = (400.000 + 500.000) ÷ 2 = 450.000 ₺. Stok devir hızı = 5.400.000 ÷ 450.000 = **12**. Alacak verileri bu oran için gerekmez.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0015': patch(
        "Net satışları 9.000.000 ₺ olan bir işletmenin aktifleri özkaynaklarının 2,5 katıdır ve aktif devir hızı 3'tür. Buna göre işletmenin borçlarının toplamı kaç ₺'dir?",
        {
            'A': '3.000.000',
            'B': '1.800.000',
            'C': '1.200.000',
            'D': '1.500.000',
            'E': '3.600.000',
        },
        'B',
        'Aktif = 9.000.000 ÷ 3 = 3.000.000 ₺; özkaynak = 3.000.000 ÷ 2,5 = 1.200.000 ₺. Borçlar = 3.000.000 − 1.200.000 = **1.800.000 ₺**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0016': patch(
        "Faaliyet kârı 600.000 ₺ olan bir işletmenin aktif devir hızı 0,40 ve faaliyet kâr marjı %30'dur. Buna göre işletmenin aktif toplamı kaç ₺'dir?",
        {
            'A': '5.000.000',
            'B': '2.600.000',
            'C': '2.000.000',
            'D': '1.500.000',
            'E': '800.000',
        },
        'A',
        'Net satışlar = faaliyet kârı ÷ faaliyet kâr marjı = 600.000 ÷ 0,30 = 2.000.000 ₺. Aktif = net satışlar ÷ aktif devir hızı = 2.000.000 ÷ 0,40 = **5.000.000 ₺**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0017': patch(
        'Özsermaye kârlılığı %24 ve toplam varlıklarının özkaynaklarına oranı 3 olan bir işletmenin varlık (aktif) kârlılık oranı yüzde kaçtır?',
        {
            'A': '%12',
            'B': '%72',
            'C': '%8',
            'D': '%16',
            'E': '%21',
        },
        'C',
        'DuPont eşitliği: özsermaye kârlılığı = aktif kârlılığı × (toplam varlıklar ÷ özkaynaklar) → %24 = aktif kârlılığı × 3 → aktif kârlılığı = **%8**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0018': patch(
        "Bir işletmenin gelir tablosu verileri şöyledir:\n\n| Kalem | Tutar |\n|---|---|\n| Brüt satışlar | 330.000 ₺ |\n| Satış indirimleri | 30.000 ₺ |\n| Faaliyet giderleri | 60.000 ₺ |\n| Diğer faaliyetlerden olağan gelir ve kârlar | 15.000 ₺ |\n| Finansman giderleri | 25.000 ₺ |\n| Brüt satış kârı oranı | 0,45 |\n\nBuna göre işletmenin olağan kârı kaç ₺'dir?",
        {
            'A': '35.000',
            'B': '75.000',
            'C': '115.000',
            'D': '78.500',
            'E': '65.000',
        },
        'E',
        'Net satışlar = 330.000 − 30.000 = 300.000 ₺; brüt satış kârı = 300.000 × 0,45 = 135.000 ₺. Faaliyet kârı = 135.000 − 60.000 = 75.000 ₺. Olağan kâr = 75.000 + 15.000 − 25.000 = **65.000 ₺**. Oran net satışlara uygulanır.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0019': patch(
        'Toplam aktifleri 16.000.000 ₺ ve özkaynak/borç oranı 0,60 olan bir işletmenin dolaşımda, piyasa fiyatı 8 ₺ olan 1.500.000 adet hisse senedi bulunmaktadır. Buna göre PD/DD oranı kaçtır?',
        {
            'A': '1,25',
            'B': '0,75',
            'C': '1,20',
            'D': '2',
            'E': '0,50',
        },
        'D',
        "Özkaynak/borç = 0,6 → özkaynak 3 birim, borç 5 birim; özkaynak aktifin 3/8'i = 6.000.000 ₺. Piyasa değeri = 1.500.000 × 8 = 12.000.000 ₺. PD/DD = 12.000.000 ÷ 6.000.000 = **2**.",
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdaki oranlardan hangisi, pay senedine yatırılan paranın mevcut kazançla ortalama kaç yılda geri kazanılacağını ifade eder?',
        {
            'A': 'Fiyat/kazanç (F/K) oranı',
            'B': 'Piyasa değeri/defter değeri (PD/DD) oranı',
            'C': 'Temettü verimi',
            'D': 'Özsermaye kârlılığı',
            'E': 'Pay başına kâr',
        },
        'A',
        'F/K = pay fiyatı ÷ pay başına kâr; pay başına kâr değişmezse ödenen fiyatın kaç yıllık kârla karşılanacağını gösterir.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0021': patch(
        'Bir işletmenin cari oranı 2,0 iken asit-test oranı 0,7 olarak hesaplanmıştır. Bu durum en olası olarak neyi gösterir?',
        {
            'A': 'İşletmenin kısa vadeli borçlarının uzun vadeli borçlarından az olduğunu ve vadenin uzadığını gösterir.',
            'B': 'İşletmenin dönem sonunda yüksek net kâr elde ettiğini ve kârlılığının sektör ortalamasının üzerinde olduğunu gösterir.',
            'C': 'İşletmenin dönen varlıkları içinde stokların ağırlığı yüksektir (likidite büyük ölçüde stoklara bağlıdır).',
            'D': 'İşletmenin duran varlıklarının devamlı sermayeden fazla olduğunu ve net çalışma sermayesinin negatife döndüğünü gösterir.',
            'E': 'İşletmenin stoklarının dönen varlıklar içinde önemsiz kaldığını ve varlıklarının nakit ile alacaklardan oluştuğunu gösterir.',
        },
        'C',
        'Cari oran yüksek (2,0) ama asit-test düşükse (0,7), aradaki farkı **stoklar** oluşturur; yani dönen varlıklar büyük ölçüde stoklardan oluşur ve likidite stokların satışına bağımlıdır.',
        'Mali analiz - likidite yorumu',
    ),
    # düzey 2
    '0022': patch(
        'Stok devir hızının yüksek olması genel olarak neyi gösterir?',
        {
            'A': 'Stokların satılamadığını ve elde uzun süre kaldığını',
            'B': 'Stokların hızlı satıldığını; stok yönetiminin etkin olduğunu',
            'C': 'İşletmenin zarar ettiğini',
            'D': 'Özkaynakların azaldığını',
            'E': 'Kısa vadeli borcun ödenemediğini',
        },
        'B',
        'Yüksek stok devir hızı, stokların **hızlı satıldığını** ve stok yönetiminin **etkin** olduğunu gösterir (stoklar elde daha kısa süre kalır).',
        'Mali analiz - stok devir hızı yorumu',
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdaki oranlardan hangisi bir likidite oranı DEĞİLDİR?',
        {
            'A': 'Net işletme sermayesi (dönen varlık − KVYK ilişkisi)',
            'B': 'Asit-test oranı',
            'C': 'Cari oran',
            'D': 'Nakit oranı',
            'E': 'Stok devir hızı',
        },
        'E',
        '**Stok devir hızı** bir faaliyet (devir hızı) oranıdır, likidite oranı değildir. Cari, asit-test ve nakit oranı ile net işletme sermayesi likidite/kısa vadeli ödeme gücüyle ilgilidir.',
        'Mali analiz - oran sınıflaması',
    ),
    # düzey 2
    '0024': patch(
        "Bir işletmenin 2025 yılı bilançosunda dönen varlıklar 360.000 ₺, stoklar 60.000 ₺ ve kısa vadeli yabancı kaynaklar 120.000 ₺'dir. Buna göre işletmenin cari oranı ve asit-test oranı sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
        {
            'A': '3,50 ve 2,50',
            'B': '2,50 ve 3',
            'C': '2,50 ve 0,50',
            'D': '3 ve 2,50',
            'E': '3 ve 0,50',
        },
        'D',
        'Cari oran = 360.000 ÷ 120.000 = **3**. Asit-test oranı = (360.000 − 60.000) ÷ 120.000 = **2,50**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0025': patch(
        "Bir işletmenin net çalışma sermayesi 15.000 ₺, nakit oranı 0,40, hazır değerleri 8.000 ₺ ve menkul kıymetleri 12.000 ₺'dir. Buna göre işletmenin dönen varlıklar toplamı kaç ₺'dir?",
        {
            'A': '65.000',
            'B': '35.000',
            'C': '50.000',
            'D': '20.000',
            'E': '80.000',
        },
        'A',
        'KVYK = (hazır + menkul) ÷ nakit oranı = 20.000 ÷ 0,40 = 50.000 ₺. Net çalışma sermayesi = dönen varlıklar − KVYK → dönen varlıklar = 50.000 + 15.000 = **65.000 ₺**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0026': patch(
        'Dönen varlıkları 400.000 ₺, kısa vadeli yabancı kaynakları 500.000 ₺ olan bir işletmede aşağıdaki işlemlerden hangisi cari oranı artırır?',
        {
            'A': 'Kısa vadeli banka kredisiyle makine satın alınması',
            'B': 'Kısa vadeli borçların bir kısmının kasadaki nakitle ödenmesi',
            'C': 'Stokların bir kısmının maliyet bedeline peşin satılması',
            'D': 'Ticari alacakların bir kısmının tahsil edilmesi',
            'E': 'Uzun vadeli banka kredisi kullanılarak kasaya nakit girişi sağlanması',
        },
        'E',
        "Cari oran 0,80'dir. Uzun vadeli kredi dönen varlıkları artırır, KVYK'yı değiştirmez → oran yükselir. Oran 1'in altındayken nakitle kısa vadeli borç ödemek oranı düşürür (örneğin 100.000 ₺ ödeme: 300 ÷ 400 = 0,75). Kısa vadeli krediyle makine almak KVYK'yı artırır. Stok satışı ve alacak tahsili dönen varlıklar içinde yer değiştirmedir; oranı etkilemez.",
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0027': patch(
        'Bir işletmeye ait iki döneme ilişkin bazı bilgiler şöyledir:\n\n| Kalem (₺) | Cari dönem | Önceki dönem |\n|---|---|---|\n| Toplam aktif | 1.200.000 | 950.000 |\n| Dönen varlıklar | 720.000 | 500.000 |\n| KVYK | 480.000 | 300.000 |\n| Net satışlar | 1.440.000 | 900.000 |\n| Stoklar | 120.000 | 90.000 |\n\nBuna göre cari döneme ait net işletme sermayesi devir hızı ve asit-test oranı sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
        {
            'A': '2 ve 1,25',
            'B': '1,20 ve 1,25',
            'C': '6 ve 1,25',
            'D': '3 ve 1,25',
            'E': '6 ve 1,50',
        },
        'C',
        'Net işletme sermayesi = 720.000 − 480.000 = 240.000 ₺; devir hızı = 1.440.000 ÷ 240.000 = **6**. Asit-test = (720.000 − 120.000) ÷ 480.000 = **1,25**. Önceki dönem verileri bu iki oran için gerekmez.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0028': patch(
        'Pasif toplamı 30.000 ₺ olan bir işletmenin duran varlıkları dönen varlıklarının 4 katıdır. Devamlı (sürekli) sermayesi 27.000 ₺ olduğuna göre işletmenin cari oranı kaçtır?',
        {
            'A': '2,50',
            'B': '3,00',
            'C': '3,50',
            'D': '2',
            'E': '8',
        },
        'D',
        'Dönen varlıklar x ise duran varlıklar 4x; x + 4x = 30.000 → x = 6.000 ₺. KVYK = pasif − devamlı sermaye = 30.000 − 27.000 = 3.000 ₺. Cari oran = 6.000 ÷ 3.000 = **2**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0029': patch(
        'Cari oranı 1,8 olan bir işletmede aşağıdaki işlemlerden hangisi cari oranı azaltır?',
        {
            'A': 'Ortakların nakit sermaye artırımına katılması',
            'B': 'Kısa vadeli banka kredisiyle üretim makinesi satın alınması',
            'C': 'Stokların bir kısmının maliyet bedeline peşin satılması',
            'D': 'Kısa vadeli borçların bir kısmının kasadaki nakitle ödenmesi',
            'E': 'Uzun vadeli kredi kullanılarak kasaya nakit girişi sağlanması',
        },
        'B',
        "Kısa vadeli krediyle makine almak KVYK'yı artırır, dönen varlıkları artırmaz → oran düşer. Uzun vadeli kredi ve nakit sermaye artırımı dönen varlıkları artırır → oran yükselir. Oran 1'den büyükken nakitle kısa vadeli borç ödemek oranı yükseltir (ör. 180 ve 100 → 160 ve 80: 2,0). Stok satışı dönen varlıklar arasında yer değiştirmedir.",
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 2
    '0030': patch(
        'Özsermaye çarpanı (toplam varlıklar ÷ özkaynaklar) 4 olan bir firmanın finansal kaldıraç oranı kaçtır?',
        {
            'A': '3',
            'B': '0,25',
            'C': '0,75',
            'D': '0,80',
            'E': '1,33',
        },
        'C',
        "Özsermaye çarpanı 4 ise özkaynaklar varlıkların 1/4'ü, yani 0,25'idir. Finansal kaldıraç oranı (toplam yabancı kaynaklar ÷ toplam varlıklar) = 1 − 0,25 = **0,75**.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletmenin duran varlıklarının aktif toplamına oranı %80, özkaynak toplamı 30.000 ₺ ve özkaynakların pasif toplamına oranı %12'dir. Buna göre dönen varlıkların toplamı kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '200.000',
            'C': '20.000',
            'D': '50.000',
            'E': '220.000',
        },
        'D',
        "Pasif toplamı = 30.000 ÷ 0,12 = 250.000 ₺ = aktif toplamı. Dönen varlıklar aktifin %20'si: 250.000 × 0,20 = **50.000 ₺**.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0032': patch(
        'Uzun vadeli banka kredisi kullanarak ticari mal satın alan bir işletmede aşağıdaki oranlardan hangisi bu işlemden etkilenmez?',
        {
            'A': 'Net çalışma sermayesi',
            'B': 'Cari oran',
            'C': 'Özkaynak oranı',
            'D': 'Finansal kaldıraç oranı',
            'E': 'Asit-test oranı',
        },
        'E',
        'Stoklar ve uzun vadeli borç aynı tutarda artar. Asit-test oranında stoklar paydan düşüldüğü ve KVYK değişmediği için oran aynı kalır. Cari oran ve NÇS dönen varlıklar arttığı için; kaldıraç ve özkaynak oranı yabancı kaynak ve aktif arttığı için değişir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0033': patch(
        'Satışlarının maliyeti 7.200.000 ₺, ortalama alacak tahsil süresi 75 gün ve ortalama stokları 900.000 ₺ olan bir işletmenin ortalama stokta kalma süresi kaç gündür? (1 yıl = 360 gün)',
        {
            'A': '120',
            'B': '45',
            'C': '75',
            'D': '30',
            'E': '8',
        },
        'B',
        'Stok devir hızı = 7.200.000 ÷ 900.000 = 8; stokta kalma süresi = 360 ÷ 8 = **45 gün**. Tahsil süresi (75 gün) alacaklarla ilgilidir; ikisinin toplamı (120 gün) faaliyet dönemidir.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0034': patch(
        "Net satışları 150.000 ₺ ve brüt satış kârı oranı %25 olan bir işletmenin ortalama stokları 25.000 ₺'dir. Buna göre ortalama stokta kalma süresi kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '80',
            'B': '240',
            'C': '60',
            'D': '90',
            'E': '72',
        },
        'A',
        'Satışların maliyeti = 150.000 × %75 = 112.500 ₺. Stok devir hızı = 112.500 ÷ 25.000 = 4,50. Süre = 360 ÷ 4,50 = **80 gün**. Satışları kullanmak 60 gün verir; stok devrinde satışların maliyeti esas alınır.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0035': patch(
        "Bir işletmenin net satışları 2024'te 20.000 ₺ iken 2025'te 24.000 ₺'ye yükselmiştir. Aktif devir hızı 2024'te 2,50 iken 2025'te 2 olmuştur. Buna göre toplam varlıklarda 2024'e göre nasıl bir değişim olmuştur?",
        {
            'A': 'Değişmemiştir.',
            'B': '%20 artmıştır.',
            'C': '%25 artmıştır.',
            'D': '%20 azalmıştır.',
            'E': '%50 artmıştır.',
        },
        'E',
        '2024 varlıkları = 20.000 ÷ 2,50 = 8.000 ₺; 2025 = 24.000 ÷ 2 = 12.000 ₺. Değişim = (12.000 − 8.000) ÷ 8.000 = **%50 artış**. Satışlar %20 artmış, devir hızı %20 düşmüştür; varlıklar satışlardan hızlı büyümüştür.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0036': patch(
        'Finansal kaldıraç oranı %60, aktif kârlılık oranı %18 ve aktif toplamı 3.000.000 ₺ olan bir işletmenin özsermaye kârlılık oranı yüzde kaçtır?',
        {
            'A': '%30',
            'B': '%7,20',
            'C': '%12',
            'D': '%45',
            'E': '%10,80',
        },
        'D',
        "Özkaynaklar aktifin %40'ıdır (1 − 0,60). Özsermaye kârlılığı = aktif kârlılığı × özsermaye çarpanı = %18 × (1 ÷ 0,40) = %18 × 2,5 = **%45**. Tutarla: net kâr = 3.000.000 × %18 = 540.000 ₺; özkaynak = 1.200.000 ₺; 540.000 ÷ 1.200.000 = %45.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletmenin brüt satış kârı oranı 0,35, faaliyet kârı oranı 0,20 ve satışların maliyeti 130.000 ₺'dir. Buna göre işletmenin faaliyet giderleri toplamı kaç ₺'dir?",
        {
            'A': '30.000',
            'B': '19.500',
            'C': '70.000',
            'D': '45.500',
            'E': '40.000',
        },
        'A',
        "Satışların maliyeti satışların %65'i → net satışlar = 130.000 ÷ 0,65 = 200.000 ₺. Brüt kâr 70.000 ₺, faaliyet kârı 40.000 ₺. Faaliyet giderleri = 70.000 − 40.000 = **30.000 ₺**.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0038': patch(
        "Bir işletmenin brüt kârlılık oranı 2024'te %40 iken 2025'te %32'ye düşmüştür. Net satışlar iki yılda da aynı olduğuna göre satışların maliyetinin net satışlar içindeki payı nasıl değişmiştir?",
        {
            'A': 'Değişmemiştir.',
            'B': '%20 azalmıştır.',
            'C': '8 puan artmıştır.',
            'D': '8 puan azalmıştır.',
            'E': '32 puan artmıştır.',
        },
        'C',
        "Satışların maliyetinin payı = 1 − brüt kârlılık oranı: 2024'te %60, 2025'te %68. Pay **8 puan artmıştır** (oransal olarak 8 ÷ 60 ≈ %13,3). Brüt kârlılıktaki 8 puanlık düşüş maliyet payındaki artışın karşılığıdır.",
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdakilerden hangisi bir işletmenin kârlılık durumu hakkında bilgi vermez?',
        {
            'A': 'Net kâr marjı',
            'B': 'Asit-test oranı',
            'C': 'Faaliyet kâr marjı',
            'D': 'Aktif kârlılık oranı',
            'E': 'Özsermaye kârlılığı',
        },
        'B',
        'Asit-test oranı ((dönen varlıklar − stoklar) ÷ KVYK) bir likidite oranıdır. Diğerleri kârın satışlara, varlıklara veya özkaynaklara oranını ölçen kârlılık oranlarıdır.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0040': patch(
        "40 ₺'ye aldığı pay senedini aynı dönem içinde 46 ₺'ye satan bir yatırımcı, payı elinde tuttuğu sürede 2 ₺ temettü almıştır. Buna göre yatırımcının pay senedi getiri oranı yüzde kaçtır?",
        {
            'A': '%5',
            'B': '%15',
            'C': '%13,04',
            'D': '%20',
            'E': '%17,39',
        },
        'D',
        'Getiri = (satış fiyatı − alış fiyatı + temettü) ÷ alış fiyatı = (46 − 40 + 2) ÷ 40 = 8 ÷ 40 = **%20**. Temettüyü unutmak %15, yalnız temettü %5 verir.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0041': patch(
        'En katıdan en esnek likidite oranına doğru sıralama aşağıdakilerden hangisidir?',
        {
            'A': 'Nakit oranı → Cari oran → Asit-test oranı',
            'B': 'Asit-test oranı → Cari oran → Nakit oranı',
            'C': 'Nakit oranı → Asit-test oranı → Cari oran',
            'D': 'Cari oran → Asit-test oranı → Nakit oranı',
            'E': 'Cari oran → Nakit oranı → Asit-test oranı',
        },
        'C',
        'En **katı** (en az varlık kalemi içeren) orandan en **esnek** orana: **Nakit oranı → Asit-test oranı → Cari oran**. Nakit oranı yalnız en likit değerleri, cari oran tüm dönen varlıkları içerir.',
        'Mali analiz - likidite oranları',
    ),
    # düzey 2
    '0042': patch(
        'Aşağıdaki oranlardan hangileri faaliyet (devir hızı) oranıdır?\n\nI. Stok devir hızı\n\nII. Alacak devir hızı\n\nIII. Cari oran',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'A',
        '**I (stok devir hızı)** ve **II (alacak devir hızı)** faaliyet (devir hızı) oranlarıdır. **III (cari oran)** ise bir likidite oranıdır. Doğru cevap **I ve II**.',
        'Mali analiz - faaliyet oranları',
    ),
    # düzey 2
    '0043': patch(
        'Oran analizi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Cari oran = Dönen Varlıklar ÷ Özkaynaklar.\n\nII. Kaldıraç oranı, varlıkların ne kadarının yabancı kaynakla finanse edildiğini gösterir.\n\nIII. Özkaynak kârlılığı (ROE) = Net Kâr ÷ Özkaynaklar.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'B',
        "**I yanlıştır:** Cari oran = Dönen Varlıklar ÷ **Kısa Vadeli Yabancı Kaynaklar**'dır; paydada özkaynaklar değil kısa vadeli yabancı kaynaklar yer alır. **II** (kaldıraç oranının anlamı) ve **III** (ROE = Net Kâr ÷ Özkaynaklar) doğrudur. Doğru cevap **II ve III**.",
        'Mali analiz - oran analizi',
    ),
    # düzey 3
    '0044': patch(
        "Bir işletmenin hazır değerleri 3.000 ₺, menkul kıymetleri 5.000 ₺, stokları 16.000 ₺; cari oranı 1,75 ve nakit oranı 0,25'tir. Buna göre işletmenin likidite (asit-test) oranı kaçtır?",
        {
            'A': '2,00',
            'B': '1,75',
            'C': '1,50',
            'D': '1,5',
            'E': '1,25',
        },
        'E',
        'Nakit oranı = (hazır + menkul) ÷ KVYK → 0,25 = 8.000 ÷ KVYK → KVYK = 32.000 ₺. Dönen varlıklar = 1,75 × 32.000 = 56.000 ₺. Asit-test = (56.000 − 16.000) ÷ 32.000 = **1,25**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0045': patch(
        "Bir işletmenin devamlı (sürekli) sermayesi 5.000.000 ₺, kısa vadeli yabancı kaynakları 2.500.000 ₺ ve net çalışma sermayesi 600.000 ₺'dir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Pasif toplamı 7.500.000 ₺'dir.",
            'B': 'Duran varlıkların bir kısmı kısa vadeli yabancı kaynaklarla finanse edilmektedir.',
            'C': "Dönen varlıklar 3.100.000 ₺'dir.",
            'D': "Duran varlıklar 4.400.000 ₺'dir.",
            'E': "Devamlı sermayenin 600.000 ₺'lik kısmı dönen varlıkları finanse etmektedir.",
        },
        'B',
        "Pasif = devamlı sermaye + KVYK = 7.500.000 ₺; dönen varlıklar = KVYK + NÇS = 3.100.000 ₺; duran varlıklar = 7.500.000 − 3.100.000 = 4.400.000 ₺. Duran varlıklar devamlı sermayeden küçüktür; devamlı sermayenin 600.000 ₺'si dönen varlıklara gider. Duran varlıkların KVYK ile finanse edilmesi ancak NÇS negatif olsaydı söz konusu olurdu; ifade yanlıştır.",
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0046': patch(
        'Cari oranı 1,5 olan bir işletmede gerçekleştirilecek aşağıdaki işlemlerden hangileri cari oranı artırır?\n\nI. Uzun vadeli banka kredisiyle satıcılara olan borcun ödenmesi\n\nII. Kasadaki nakitle ticari mal satın alınması\n\nIII. Kısa vadeli banka kredisiyle üretim makinesi alınması',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'E',
        '**I artırır:** KVYK azalır, dönen varlıklar değişmez. **II etkilemez:** nakit stoka dönüşür, dönen varlıklar toplamı aynı kalır. **III azaltır:** KVYK artar, dönen varlık artmaz (makine duran varlıktır). Doğru cevap **Yalnız I**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 2
    '0047': patch(
        "Bir işletmenin dönen varlıkları 3.600.000 ₺, kısa vadeli yükümlülükleri 1.800.000 ₺ ve net çalışma sermayesi devir hızı 4'tür. Buna göre işletmenin net satışları kaç ₺'dir?",
        {
            'A': '21.600.000',
            'B': '14.400.000',
            'C': '7.200.000',
            'D': '450.000',
            'E': '12.600.000',
        },
        'C',
        'Net çalışma sermayesi = 3.600.000 − 1.800.000 = 1.800.000 ₺. Devir hızı = net satışlar ÷ NÇS → net satışlar = 1.800.000 × 4 = **7.200.000 ₺**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0048': patch(
        "Bir işletmenin dönem sonunda cari oranı 3 ve net çalışma sermayesi 20.000 ₺'dir. Duran varlıkların devamlı (sürekli) sermayeye oranı 0,50'dir. Buna göre kısa vadeli yabancı kaynakların kaynak toplamına oranı yüzde kaçtır?",
        {
            'A': '%40',
            'B': '%25',
            'C': '%33,33',
            'D': '%20',
            'E': '%60',
        },
        'D',
        'Cari 3 ise dönen varlıklar = 3 × KVYK; NÇS = 2 × KVYK = 20.000 → KVYK = 10.000 ₺, dönen varlıklar 30.000 ₺. NÇS = devamlı sermaye − duran varlıklar = devamlı sermaye × (1 − 0,5) → devamlı sermaye = 40.000 ₺. Kaynak toplamı = 10.000 + 40.000 = 50.000 ₺. Oran = 10.000 ÷ 50.000 = **%20**.',
        'Mali analiz - likidite oranları ve çalışma sermayesi',
    ),
    # düzey 3
    '0049': patch(
        "Bir işletmenin özkaynak kalemleri şöyledir:\n\n| Kalem | Tutar (₺) |\n|---|---|\n| Sermaye | 3.000.000 |\n| Ödenmemiş sermaye | 500.000 |\n| Hisse senedi ihraç primleri | 400.000 |\n| Kâr yedekleri | 900.000 |\n| Geçmiş yıllar zararları | 700.000 |\n| Dönem net kârı | 350.000 |\n\nBuna göre işletmenin özkaynakları kaç ₺'dir?",
        {
            'A': '3.450.000',
            'B': '2.450.000',
            'C': '3.100.000',
            'D': '3.050.000',
            'E': '2.050.000',
        },
        'A',
        'Özkaynak = sermaye − ödenmemiş sermaye + ihraç primi + kâr yedekleri − geçmiş yıl zararları + dönem net kârı = 3.000.000 − 500.000 + 400.000 + 900.000 − 700.000 + 350.000 = **3.450.000 ₺**. Ödenmemiş sermaye ve geçmiş yıl zararları indirim kalemidir.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0050': patch(
        "Net satışları 6.000.000 ₺ ve aktif devir hızı 3 olan bir işletmenin borç/özsermaye oranı 3'tür. Buna göre işletmenin finansal kaldıraç oranı yüzde kaçtır?",
        {
            'A': '%25',
            'B': '%60',
            'C': '%75',
            'D': '%300',
            'E': '%33,33',
        },
        'C',
        'Borç/özsermaye = 3 ise borç 3 birim, özsermaye 1 birimdir; aktif 4 birim. Finansal kaldıraç = 3 ÷ 4 = **%75**. Aktif (6.000.000 ÷ 3 = 2.000.000 ₺) oranın kendisini değiştirmez; borçlar 1.500.000 ₺, özsermaye 500.000 ₺ olur.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletmenin yabancı kaynak oranı 0,55'tir. Aynı tarihte özkaynakları 45.000 ₺, duran varlıkları 50.000 ₺ ve cari oranı 1,25'tir. Buna göre uzun vadeli yabancı kaynaklar toplamı kaç ₺'dir?",
        {
            'A': '55.000',
            'B': '15.000',
            'C': '5.000',
            'D': '10.000',
            'E': '40.000',
        },
        'B',
        'Özkaynak oranı 1 − 0,55 = 0,45 → aktif = 45.000 ÷ 0,45 = 100.000 ₺; yabancı kaynaklar 55.000 ₺. Dönen varlıklar = 100.000 − 50.000 = 50.000 ₺ → KVYK = 50.000 ÷ 1,25 = 40.000 ₺. UVYK = 55.000 − 40.000 = **15.000 ₺**.',
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 2
    '0052': patch(
        'Aşağıdaki durumların hangisinde bir işletmenin özkaynakları negatif olur?',
        {
            'A': 'Uzun vadeli yabancı kaynaklar özkaynaklardan büyük olduğunda',
            'B': 'Dönem net zarar ile kapandığında',
            'C': 'Duran varlıklar devamlı sermayeden büyük olduğunda',
            'D': 'Toplam yabancı kaynaklar toplam varlıklardan büyük olduğunda',
            'E': 'Kısa vadeli yabancı kaynaklar dönen varlıklardan büyük olduğunda',
        },
        'D',
        "Özkaynaklar = toplam varlıklar − toplam yabancı kaynaklar olduğundan yabancı kaynaklar varlıkları aştığında özkaynak negatife düşer. Dönem zararı özkaynağı azaltır ama tek başına negatif yapmaz; KVYK'nın dönen varlıkları aşması NÇS'yi negatif yapar.",
        'Mali analiz - mali yapı oranları',
    ),
    # düzey 3
    '0053': patch(
        "Bir işletmenin yıllık satışları 6.000.000 ₺, brüt kâr marjı %30'dur. Üçer aylık dönem sonlarındaki stok değerleri şöyledir:\n\n| Dönem | Stoklar (₺) |\n|---|---|\n| I | 900.000 |\n| II | 1.100.000 |\n| III | 1.300.000 |\n| IV | 700.000 |\n\nBuna göre işletmenin stok devir hızı kaçtır?",
        {
            'A': '3,50',
            'B': '1,80',
            'C': '5,25',
            'D': '6',
            'E': '4,20',
        },
        'E',
        'Satışların maliyeti = 6.000.000 × %70 = 4.200.000 ₺. Ortalama stok dört dönem sonunun ortalamasıdır: 4.000.000 ÷ 4 = 1.000.000 ₺. Stok devir hızı = 4.200.000 ÷ 1.000.000 = **4,20**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0054': patch(
        "Bir işletmenin faaliyet giderleri toplamı 30.000 ₺, brüt satış kârı oranı %40 ve ortalama stokları 45.000 ₺'dir. Stok devir hızı 3 olduğuna göre işletmenin faaliyet kârı kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '90.000',
            'C': '30.000',
            'D': '225.000',
            'E': '24.000',
        },
        'A',
        "Satışların maliyeti = 45.000 × 3 = 135.000 ₺. Maliyet satışların %60'ı → net satışlar = 135.000 ÷ 0,60 = 225.000 ₺; brüt kâr 90.000 ₺. Faaliyet kârı = 90.000 − 30.000 = **60.000 ₺**.",
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 3
    '0055': patch(
        "Satışlarının tamamı kredili olan bir işletmenin net satışları 1.800.000 ₺, ortalama ticari alacakları 300.000 ₺, satışların maliyeti 1.200.000 ₺ ve ortalama stokları 200.000 ₺'dir. Buna göre işletmenin faaliyet dönemi (stok süresi + tahsil süresi) kaç gündür? (1 yıl = 360 gün)",
        {
            'A': '150',
            'B': '60',
            'C': '12',
            'D': '100',
            'E': '120',
        },
        'E',
        'Alacak devir hızı = 1.800.000 ÷ 300.000 = 6 → tahsil süresi 60 gün. Stok devir hızı = 1.200.000 ÷ 200.000 = 6 → stok süresi 60 gün. Faaliyet dönemi = **120 gün**.',
        'Mali analiz - faaliyet (devir hızı) oranları',
    ),
    # düzey 2
    '0056': patch(
        "Aktif devir hızı 2,50 olan bir işletmede aktif kârlılık oranı %20 ve net kâr 80.000 ₺'dir. Buna göre işletmenin net satışları kaç ₺'dir?",
        {
            'A': '1.000.000',
            'B': '400.000',
            'C': '160.000',
            'D': '800.000',
            'E': '200.000',
        },
        'A',
        'Aktif = net kâr ÷ aktif kârlılığı = 80.000 ÷ 0,20 = 400.000 ₺. Net satışlar = aktif × devir hızı = 400.000 × 2,50 = **1.000.000 ₺**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0057': patch(
        "Bir ticaret işletmesinin faaliyet kârı 45.000 ₺, faaliyet giderleri toplamı 55.000 ₺ ve brüt satış kârı oranı 0,20'dir. Buna göre işletmenin satılan ticari mallar maliyeti kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '225.000',
            'C': '100.000',
            'D': '180.000',
            'E': '400.000',
        },
        'E',
        'Brüt satış kârı = faaliyet kârı + faaliyet giderleri = 45.000 + 55.000 = 100.000 ₺. Net satışlar = 100.000 ÷ 0,20 = 500.000 ₺. Satılan ticari mallar maliyeti = 500.000 − 100.000 = **400.000 ₺**.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 3
    '0058': patch(
        'Bir işletmenin faaliyet kârlılığı oranı, olağan kârlılık oranından küçük ise aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Finansman giderleri, faaliyet giderlerinden büyüktür.',
            'B': 'Diğer faaliyetlerden olağan gelir ve kârlar, olağan gider ve zararlar ile finansman giderlerinin toplamından büyüktür.',
            'C': 'Olağandışı gelir ve kârlar, olağandışı gider ve zararlardan büyüktür.',
            'D': 'Brüt satış kârı, faaliyet kârından küçüktür.',
            'E': 'Faaliyet giderleri, diğer faaliyetlerden olağan gelir ve kârlardan büyüktür.',
        },
        'B',
        'Olağan kâr = faaliyet kârı + diğer faaliyetlerden olağan gelir ve kârlar − olağan gider ve zararlar − finansman giderleri. Olağan kâr faaliyet kârından büyükse eklenen gelirler düşülen gider ve finansman giderlerinden büyüktür. Olağandışı kalemler olağan kârın altında yer alır, bu karşılaştırmayı etkilemez.',
        'Mali analiz - kârlılık oranları',
    ),
    # düzey 2
    '0059': patch(
        "Bir işletmenin dolaşımdaki pay senedi sayısı 20.000 adet, payın piyasa değeri 6 ₺'dir. Aktif toplamı 300.000 ₺, toplam yabancı kaynakları 240.000 ₺ olduğuna göre piyasa değeri/defter değeri (PD/DD) oranı kaçtır?",
        {
            'A': '2,50',
            'B': '2',
            'C': '1,50',
            'D': '0,40',
            'E': '0,50',
        },
        'B',
        'Piyasa değeri = 20.000 × 6 = 120.000 ₺. Defter değeri = özkaynaklar = 300.000 − 240.000 = 60.000 ₺. PD/DD = **2**.',
        'Mali analiz - piyasa oranları',
    ),
    # düzey 2
    '0060': patch(
        'Oranlarla analizde bir bilanço kalemindeki tutar ile bir gelir tablosu kalemindeki tutar birbirine oranlanacaksa aşağıdakilerden hangisinin yapılması gerekir?',
        {
            'A': 'Gelir tablosu kalemi on iki aya bölünerek aylık tutara çevrilmelidir.',
            'B': 'Her iki kalem de enflasyona göre düzeltilmeden oran hesaplanamaz.',
            'C': 'Bilanço kaleminin dönem başı tutarı esas alınmalıdır.',
            'D': 'Gelir tablosu kalemi önceki dönemin tutarıyla toplanmalıdır.',
            'E': 'Bilanço kaleminin dönem başı ve dönem sonu tutarlarının ortalaması alınmalıdır.',
        },
        'E',
        'Gelir tablosu kalemi bir dönem boyunca oluşan akış tutarıdır; bilanço kalemi ise bir andaki stok tutarıdır. İkisini uyumlu kılmak için bilanço kaleminin dönem içi ortalaması (dönem başı + dönem sonu ÷ 2) kullanılır; stok ve alacak devir hızlarında olduğu gibi.',
        'Mali analiz - oran analizinin ilkeleri',
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
    print(f"1 paket / {len(PATCHES)} soru ('Oran Analizi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
